"""Seven System v0.1.0 的统一命令行入口。"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from . import __version__
from .config import ConfigError, load_config
from .database import (
    DatabaseContractError,
    StrictDbContractReportError,
    StrictDatabaseContractSubject,
    build_strict_db_contract_report,
    strict_db_implementation_tree_hash,
    verify_strict_db_contract_report,
)
from .epoch import EpochError, dry_run_epoch, init_epoch, validate_epoch
from .preflight import run_preflight
from .storage import ContentConflictError, commit_json_once, read_json


SYSTEM_ROOT = Path(__file__).resolve().parents[2]


def _emit(payload: Any, *, stream: Any = None) -> None:
    if stream is None:
        stream = sys.stdout
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), file=stream)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="seven",
        description="非特化证据工厂控制面（当前仅 P0/P1）",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("version", help="显示版本和实现边界")

    preflight = sub.add_parser("preflight", help="只读检查，不连接数据库或启动Solver")
    preflight.add_argument("--config", required=True, type=Path)

    initialize = sub.add_parser("init-epoch", help="初始化一个P0/P1 Epoch")
    initialize.add_argument("--config", required=True, type=Path)
    initialize.add_argument("--epoch-id", required=True)

    dry_run = sub.add_parser("dry-run", help="初始化并运行幂等/冲突拒绝演练")
    dry_run.add_argument("--config", required=True, type=Path)
    dry_run.add_argument("--epoch-id", required=True)

    status = sub.add_parser("status", help="查看Epoch完整性与当前边界")
    status.add_argument("--epoch-root", required=True, type=Path)

    validate = sub.add_parser("validate-epoch", help="验证Epoch必需文件和manifest hash")
    validate.add_argument("--epoch-root", required=True, type=Path)

    contract = sub.add_parser(
        "wp1-db-contract-report",
        help="运行零DB副作用的Strict DB离线测试并提交本地报告",
    )
    contract.add_argument("--config", required=True, type=Path)
    contract.add_argument("--report-id", required=True)

    sub.add_parser("capabilities", help="列出已实现与明确未实现的能力")

    # 第 10 节深度补全：registry-consistency-check 命令
    consistency = sub.add_parser(
        "registry-consistency-check",
        help="检查 CLI capabilities 与 ImplementationCapabilityRegistry 的一致性",
    )

    gv0_verify = sub.add_parser(
        "gv0-verify-completion-contract",
        help="WP-GV0: 验证完成合同（DAG-aware owner/contract/schema/actor）",
    )
    gv0_verify.add_argument("--dag-path", required=True, type=Path)
    gv0_verify.add_argument("--expected-dag-sha256", required=True)
    gv0_verify.add_argument("--wp-id", required=True)
    gv0_verify.add_argument("--submitted-object", required=True, type=Path)
    gv0_verify.add_argument(
        "--actor-type", required=True, choices=["IMPLEMENTER", "AUDITOR", "SYSTEM"]
    )
    gv0_verify.add_argument("--state-command", default=None)

    bundle = sub.add_parser(
        "build-implementation-completion-bundle",
        help="组装side-effect-free普通ImplementationCompletionBundle候选JSON到stdout",
    )
    bundle.add_argument("--bundle-input", required=True, type=Path)
    bundle.add_argument("--plan", required=True, type=Path)
    bundle.add_argument("--plan-sha256", required=True)
    bundle.add_argument(
        "--dag",
        default=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json",
        type=Path,
    )

    plan = sub.add_parser(
        "build-work-package-plan",
        help="从canonical DAG、规范索引和已签规范复核记录组装side-effect-free普通WorkPackagePlan到stdout",
    )
    plan.add_argument("--plan-input", required=True, type=Path)
    plan.add_argument(
        "--dag",
        default=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json",
        type=Path,
    )
    plan.add_argument(
        "--normative-index",
        default=SYSTEM_ROOT / "docs" / "implementation" / "normative-requirement-index.v1.json",
        type=Path,
    )
    plan.add_argument("--normative-review-record", required=True, type=Path)
    plan.add_argument("--normative-review-public-key-hex", required=True)

    review = sub.add_parser(
        "verify-normative-review-record",
        help="语义验证已签名NormativeRequirementReviewRecord；不签名、不改状态",
    )
    review.add_argument("--record", required=True, type=Path)
    review.add_argument(
        "--normative-index",
        default=SYSTEM_ROOT / "docs" / "implementation" / "normative-requirement-index.v1.json",
        type=Path,
    )
    review.add_argument("--public-key-hex", required=True)
    review.add_argument("--expected-index-sha256", default=None)
    review.add_argument("--expected-record-sha256", default=None)

    audit_input = sub.add_parser(
        "validate-audit-input-pack",
        help="只读验证交给独立GA1审计者的机械输入包；不签审计、不改状态",
    )
    audit_input.add_argument("--pack", required=True, type=Path)
    audit_input.add_argument(
        "--schema",
        default=SYSTEM_ROOT / "docs" / "implementation" / "audit-input-pack.v1.schema.json",
        type=Path,
    )
    audit_input.add_argument(
        "--dag",
        default=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json",
        type=Path,
    )

    build_audit_input = sub.add_parser(
        "build-audit-input-pack",
        help="从候选完成对象refs组装GA1机械输入包到stdout；不签审计、不改状态",
    )
    build_audit_input.add_argument("--pack-input", required=True, type=Path)
    build_audit_input.add_argument(
        "--schema",
        default=SYSTEM_ROOT / "docs" / "implementation" / "audit-input-pack.v1.schema.json",
        type=Path,
    )
    build_audit_input.add_argument(
        "--dag",
        default=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json",
        type=Path,
    )

    audit_report = sub.add_parser(
        "audit-input-pack-report",
        help="只读生成GA1机械输入覆盖报告；不签审计、不改状态",
    )
    audit_report.add_argument("--pack", required=True, type=Path)
    audit_report.add_argument("--report-id", required=True)
    audit_report.add_argument(
        "--expected-scope",
        choices=["PACK_TARGETS_ONLY", "GA1_DEVELOPMENT_CLOSURE"],
        default="GA1_DEVELOPMENT_CLOSURE",
    )
    audit_report.add_argument("--created-at", required=True)
    audit_report.add_argument("--creator", required=True)
    audit_report.add_argument(
        "--schema",
        default=SYSTEM_ROOT / "docs" / "implementation" / "audit-input-pack.v1.schema.json",
        type=Path,
    )
    audit_report.add_argument(
        "--dag",
        default=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json",
        type=Path,
    )

    db1l_report = sub.add_parser(
        "db1l-logical-site-report",
        help="生成DB1L只读逻辑站点报告；fixture零DB，environment-readonly只读连接Arango",
    )
    db1l_report.add_argument(
        "--source",
        required=True,
        choices=["fixture", "environment-readonly"],
    )
    db1l_report.add_argument(
        "--ack-readonly-db",
        action="store_true",
        help="source=environment-readonly 时必须显式确认将进行只读DB连接",
    )

    db1l_verify = sub.add_parser(
        "db1l-verify-logical-site-report",
        help="语义验证DB1L只读逻辑站点报告；不连接DB、不改状态",
    )
    db1l_verify.add_argument("--report", required=True, type=Path)
    db1l_verify.add_argument(
        "--schema",
        default=SYSTEM_ROOT / "docs" / "implementation" / "database-logical-site-capability-report.v1.schema.json",
        type=Path,
    )

    return parser


def _wp1_db_contract_report(config_path: Path, report_id: str) -> dict[str, Any]:
    if re.fullmatch(r"[a-z0-9][a-z0-9._-]{0,63}", report_id) is None:
        raise DatabaseContractError("report-id must be a safe lowercase slug")
    config = load_config(config_path)
    if config.mode != "dry_run":
        raise DatabaseContractError("WP-1 offline contract requires dry_run mode")
    preflight = run_preflight(config)
    if preflight["overall_verdict"] != "PASS":
        raise DatabaseContractError("P0 preflight must PASS before contract reporting")

    destination = (
        config.data_root
        / "capabilities"
        / "strict-db-contract"
        / f"{report_id}.json"
    )
    implementation_hash = strict_db_implementation_tree_hash(SYSTEM_ROOT)
    subject_hash = StrictDatabaseContractSubject(
        implementation_sha256=implementation_hash
    ).subject_hash

    if destination.is_file() and not destination.is_symlink():
        existing = read_json(destination, boundary_root=config.data_root)
        errors = verify_strict_db_contract_report(
            existing,
            system_root=SYSTEM_ROOT,
        )
        if errors or not isinstance(existing, dict) or existing.get(
            "subject_hash"
        ) != subject_hash:
            raise DatabaseContractError(
                "existing WP-1 contract report is invalid or bound to stale code"
            )
        return {
            "status": "ALREADY_COMMITTED",
            "path": str(destination),
            "subject_hash": subject_hash,
            "report": existing,
        }

    report = build_strict_db_contract_report(system_root=SYSTEM_ROOT)
    status = commit_json_once(destination, report, boundary_root=config.data_root)
    return {
        "status": status,
        "path": str(destination),
        "subject_hash": report["subject_hash"],
        "report": report,
    }


def _capabilities() -> dict[str, Any]:
    """列出已实现与明确未实现的能力。

    第 10 节深度补全：使用 ImplementationCapabilityRegistry 作为机器真值源，
    确保 CLI capabilities 与 registry 一致。
    """
    from .operations.capability_registry import create_default_registry
    registry = create_default_registry()
    all_caps = registry.all_capabilities()

    implemented = []
    not_implemented = []
    for cap_id, entry in all_caps.items():
        if entry.implementation_status == "NOT_IMPLEMENTED":
            not_implemented.append(cap_id)
        else:
            implemented.append(cap_id)

    return {
        "version": __version__,
        "implemented": sorted(implemented),
        "not_implemented": sorted(not_implemented),
        "implementation_ceiling": "P1_DRY_RUN",
        "registry_source": "ImplementationCapabilityRegistry",
        "total_capabilities": len(all_caps),
    }


def _registry_consistency_check() -> dict[str, Any]:
    """第 10 节深度补全：检查 CLI capabilities 与 registry 的一致性。

    验证 CLI 报告的能力与 ImplementationCapabilityRegistry 完全一致。
    """
    from .operations.capability_registry import (
        create_default_registry, TruthConsistencyChecker,
    )
    registry = create_default_registry()
    checker = TruthConsistencyChecker(registry=registry)

    caps = _capabilities()
    cli_caps = caps.get("implemented", []) + caps.get("not_implemented", [])

    result = checker.check_capabilities_consistency(cli_caps)

    return {
        "verdict": result.verdict,
        "error_codes": [e.value for e in result.error_codes],
        "details": result.details,
        "cli_capabilities_count": len(cli_caps),
        "registry_capabilities_count": len(registry.all_capabilities()),
    }


def _gv0_verify_completion_contract(
    dag_path: Path,
    expected_dag_sha256: str,
    wp_id: str,
    submitted_object_path: Path,
    actor_type: str,
    state_command: str | None,
) -> dict[str, Any]:
    from .contracts.completion_contract import verify_completion_contract

    with open(submitted_object_path) as f:
        submitted_object = json.load(f)
    result = verify_completion_contract(
        dag_path=dag_path,
        expected_dag_sha256=expected_dag_sha256,
        wp_id=wp_id,
        submitted_object=submitted_object,
        actor_type=actor_type,
        state_command=state_command,
    )
    return {
        "verdict": result.verdict,
        "error_codes": [e.value for e in result.error_codes],
        "details": result.details,
        "dag_sha256": result.dag_sha256,
        "wp_id": result.wp_id,
        "owner_type": result.owner_type,
        "completion_contract": result.completion_contract,
        "expected_schema_id": result.expected_schema_id,
    }


def _build_implementation_completion_bundle(
    bundle_input_path: Path,
    plan_path: Path,
    plan_sha256: str,
    dag_path: Path,
) -> dict[str, Any]:
    from .operations.implementation_bundle_evidence import (
        build_side_effect_free_implementation_completion_bundle,
    )

    bundle_input = read_json(bundle_input_path)
    if not isinstance(bundle_input, dict):
        raise ValueError("bundle input must be a JSON object")
    return build_side_effect_free_implementation_completion_bundle(
        bundle_input=bundle_input,
        plan_path=plan_path,
        expected_plan_sha256=plan_sha256,
        dag_path=dag_path,
    )


def _build_work_package_plan(
    plan_input_path: Path,
    dag_path: Path,
    normative_index_path: Path,
    normative_review_record_path: Path,
    normative_review_public_key_hex: str,
) -> dict[str, Any]:
    from .operations.work_package_plan_builder import (
        build_side_effect_free_work_package_plan,
    )

    try:
        public_key_bytes = bytes.fromhex(normative_review_public_key_hex)
    except ValueError as exc:
        raise ValueError("normative-review-public-key-hex must be hexadecimal Ed25519 raw public key bytes") from exc
    if len(public_key_bytes) != 32:
        raise ValueError("normative-review-public-key-hex must encode exactly 32 Ed25519 raw public key bytes")

    plan_input = read_json(plan_input_path)
    if not isinstance(plan_input, dict):
        raise ValueError("plan input must be a JSON object")
    return build_side_effect_free_work_package_plan(
        plan_input=plan_input,
        dag_path=dag_path,
        normative_index_path=normative_index_path,
        normative_review_record_path=normative_review_record_path,
        normative_review_public_key_bytes=public_key_bytes,
    )


def _verify_normative_review_record(
    *,
    record_path: Path,
    normative_index_path: Path,
    public_key_hex: str,
    expected_index_sha256: str | None,
    expected_record_sha256: str | None,
) -> dict[str, Any]:
    from .contracts.normative_review_record import (
        verify_normative_requirement_review_record_file,
    )

    try:
        public_key_bytes = bytes.fromhex(public_key_hex)
    except ValueError as exc:
        raise ValueError("public-key-hex must be lowercase hexadecimal Ed25519 raw public key bytes") from exc
    if len(public_key_bytes) != 32:
        raise ValueError("public-key-hex must encode exactly 32 Ed25519 public key bytes")

    return verify_normative_requirement_review_record_file(
        record_path=record_path,
        normative_index_path=normative_index_path,
        public_key_bytes=public_key_bytes,
        expected_index_sha256=expected_index_sha256,
        expected_record_sha256=expected_record_sha256,
    ).to_dict()


def _validate_audit_input_pack(pack_path: Path, schema_path: Path, dag_path: Path) -> dict[str, Any]:
    from .audit.audit_input_pack import load_and_validate_audit_input_pack

    result = load_and_validate_audit_input_pack(
        pack_path=pack_path,
        schema_path=schema_path,
        dag_path=dag_path,
    )
    return result.to_dict()


def _build_audit_input_pack(pack_input_path: Path, schema_path: Path, dag_path: Path) -> dict[str, Any]:
    from .audit.audit_input_pack import build_audit_input_pack_from_refs

    pack_input = read_json(pack_input_path)
    if not isinstance(pack_input, dict):
        raise ValueError("pack input must be a JSON object")
    return build_audit_input_pack_from_refs(
        pack_input=pack_input,
        pack_base_dir=pack_input_path.parent,
        schema_path=schema_path,
        dag_path=dag_path,
    )


def _audit_input_pack_report(
    *,
    pack_path: Path,
    report_id: str,
    expected_scope: str,
    created_at: str,
    creator: str,
    schema_path: Path,
    dag_path: Path,
) -> dict[str, Any]:
    from .audit.audit_input_pack import build_audit_readiness_report

    return build_audit_readiness_report(
        report_id=report_id,
        pack_path=pack_path,
        input_pack_schema_path=schema_path,
        dag_path=dag_path,
        expected_scope=expected_scope,
        created_at=created_at,
        creator=creator,
    )


def _db1l_logical_site_report(*, source: str, ack_readonly_db: bool) -> dict[str, Any]:
    from .database.logical_site_report import build_logical_site_report
    from .database.site_adapter import FakeLogicalSiteAdapter

    if source == "fixture":
        return build_logical_site_report(FakeLogicalSiteAdapter())
    if source == "environment-readonly":
        if not ack_readonly_db:
            raise DatabaseContractError(
                "source=environment-readonly requires --ack-readonly-db"
            )
        from .database.arango_port import ArangoDatabasePort

        return build_logical_site_report(ArangoDatabasePort.from_environment())
    raise DatabaseContractError(f"unsupported DB1L report source: {source}")


def _db1l_verify_logical_site_report(report_path: Path, schema_path: Path) -> dict[str, Any]:
    from .database.logical_site_report import verify_logical_site_report
    from .schema_validation import validate_schema

    report = read_json(report_path)
    schema = read_json(schema_path)
    schema_errors = (
        validate_schema(report, schema)
        if isinstance(schema, dict)
        else ["schema root must be an object"]
    )
    semantic_errors = verify_logical_site_report(report)
    return {
        "verdict": "PASS" if not schema_errors and not semantic_errors else "FAIL",
        "schema_errors": schema_errors,
        "semantic_errors": [
            {"code": code.value, "detail": detail}
            for code, detail in semantic_errors
        ],
        "report_ref": str(report_path),
    }


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "version":
            _emit({"system": "seven-system", **_capabilities()})
            return 0
        if args.command == "capabilities":
            _emit(_capabilities())
            return 0
        if args.command == "registry-consistency-check":
            result = _registry_consistency_check()
            _emit(result)
            return 0 if result["verdict"] == "PASS" else 3
        if args.command == "preflight":
            report = run_preflight(load_config(args.config))
            _emit(report)
            return 2 if report["overall_verdict"] == "BLOCKED" else 0
        if args.command == "init-epoch":
            result = init_epoch(load_config(args.config), args.epoch_id)
            _emit(result)
            return 0
        if args.command == "dry-run":
            result = dry_run_epoch(load_config(args.config), args.epoch_id)
            _emit(result)
            return 0 if result["verdict"] == "PASS" else 3
        if args.command == "wp1-db-contract-report":
            _emit(_wp1_db_contract_report(args.config, args.report_id))
            return 0
        if args.command == "gv0-verify-completion-contract":
            result = _gv0_verify_completion_contract(
                dag_path=args.dag_path,
                expected_dag_sha256=args.expected_dag_sha256,
                wp_id=args.wp_id,
                submitted_object_path=args.submitted_object,
                actor_type=args.actor_type,
                state_command=args.state_command,
            )
            _emit(result)
            return 0 if result["verdict"] == "PASS" else 3
        if args.command == "build-implementation-completion-bundle":
            try:
                result = _build_implementation_completion_bundle(
                    bundle_input_path=args.bundle_input,
                    plan_path=args.plan,
                    plan_sha256=args.plan_sha256,
                    dag_path=args.dag,
                )
            except (ValueError, OSError, json.JSONDecodeError) as exc:
                _emit(
                    {
                        "status": "ERROR",
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                    },
                    stream=sys.stderr,
                )
                return 3
            _emit(result)
            return 0
        if args.command == "build-work-package-plan":
            try:
                result = _build_work_package_plan(
                    plan_input_path=args.plan_input,
                    dag_path=args.dag,
                    normative_index_path=args.normative_index,
                    normative_review_record_path=args.normative_review_record,
                    normative_review_public_key_hex=args.normative_review_public_key_hex,
                )
            except (ValueError, OSError, json.JSONDecodeError) as exc:
                _emit(
                    {
                        "status": "ERROR",
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                    },
                    stream=sys.stderr,
                )
                return 3
            _emit(result)
            return 0
        if args.command == "verify-normative-review-record":
            try:
                result = _verify_normative_review_record(
                    record_path=args.record,
                    normative_index_path=args.normative_index,
                    public_key_hex=args.public_key_hex,
                    expected_index_sha256=args.expected_index_sha256,
                    expected_record_sha256=args.expected_record_sha256,
                )
            except (ValueError, OSError, json.JSONDecodeError) as exc:
                _emit(
                    {
                        "status": "ERROR",
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                    },
                    stream=sys.stderr,
                )
                return 3
            _emit(result)
            return 0 if result["verdict"] == "PASS" else 3
        if args.command == "validate-audit-input-pack":
            result = _validate_audit_input_pack(
                pack_path=args.pack,
                schema_path=args.schema,
                dag_path=args.dag,
            )
            _emit(result)
            return 0 if result["verdict"] == "PASS" else 3
        if args.command == "build-audit-input-pack":
            try:
                result = _build_audit_input_pack(
                    pack_input_path=args.pack_input,
                    schema_path=args.schema,
                    dag_path=args.dag,
                )
            except (ValueError, OSError, json.JSONDecodeError) as exc:
                _emit(
                    {
                        "status": "ERROR",
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                    },
                    stream=sys.stderr,
                )
                return 3
            _emit(result)
            return 0
        if args.command == "audit-input-pack-report":
            try:
                result = _audit_input_pack_report(
                    pack_path=args.pack,
                    report_id=args.report_id,
                    expected_scope=args.expected_scope,
                    created_at=args.created_at,
                    creator=args.creator,
                    schema_path=args.schema,
                    dag_path=args.dag,
                )
            except (ValueError, OSError, json.JSONDecodeError) as exc:
                _emit(
                    {
                        "status": "ERROR",
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                    },
                    stream=sys.stderr,
                )
                return 3
            _emit(result)
            return 0 if result["mechanical_handoff_status"] == "COMPLETE" else 3
        if args.command == "db1l-logical-site-report":
            try:
                result = _db1l_logical_site_report(
                    source=args.source,
                    ack_readonly_db=args.ack_readonly_db,
                )
            except (ValueError, OSError, json.JSONDecodeError) as exc:
                _emit(
                    {
                        "status": "ERROR",
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                    },
                    stream=sys.stderr,
                )
                return 3
            _emit(result)
            return 0
        if args.command == "db1l-verify-logical-site-report":
            try:
                result = _db1l_verify_logical_site_report(
                    report_path=args.report,
                    schema_path=args.schema,
                )
            except (ValueError, OSError, json.JSONDecodeError) as exc:
                _emit(
                    {
                        "status": "ERROR",
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                    },
                    stream=sys.stderr,
                )
                return 3
            _emit(result)
            return 0 if result["verdict"] == "PASS" else 3
        if args.command == "validate-epoch":
            result = validate_epoch(args.epoch_root)
            _emit(result)
            return (
                0
                if result["verdict"] == "PASS"
                and result["current_runtime_compatibility"] == "PASS"
                else 3
            )
        if args.command == "status":
            validation = validate_epoch(args.epoch_root)
            manifest_path = args.epoch_root / "runtime-manifest.json"
            manifest = read_json(manifest_path) if manifest_path.is_file() else {}
            dry_report_path = args.epoch_root / "dry-run-report.json"
            dry_report = read_json(dry_report_path) if dry_report_path.is_file() else None
            p1_verdict_path = args.epoch_root / "p1-verdict.json"
            p1_verdict = (
                read_json(p1_verdict_path) if p1_verdict_path.is_file() else None
            )
            checkpoint_path = (
                args.epoch_root
                / "runtime-checkpoints"
                / "0001-p1-verified.json"
            )
            checkpoint = (
                read_json(checkpoint_path) if checkpoint_path.is_file() else None
            )
            _emit(
                {
                    "epoch_id": manifest.get("epoch_id"),
                    "manifest_hash": manifest.get("manifest_hash"),
                    "mode": manifest.get("mode"),
                    "implementation_ceiling": "P1_DRY_RUN",
                    "epoch_validation": validation,
                    "dry_run_verdict": None if dry_report is None else dry_report.get("verdict"),
                    "runtime_state": (
                        "INITIALIZED" if checkpoint is None else checkpoint.get("state")
                    ),
                    "p1_scaffold_verdict": (
                        None if p1_verdict is None else p1_verdict.get("overall_verdict")
                    ),
                    "scientific_claim": "NOT_TESTED",
                }
            )
            return (
                0
                if validation["verdict"] == "PASS"
                and validation["current_runtime_compatibility"] == "PASS"
                else 3
            )
    except (
        ConfigError,
        DatabaseContractError,
        StrictDbContractReportError,
        EpochError,
        ContentConflictError,
        OSError,
        json.JSONDecodeError,
    ) as exc:
        _emit(
            {
                "status": "ERROR",
                "error_type": type(exc).__name__,
                "message": str(exc),
            },
            stream=sys.stderr,
        )
        return 2
    return 2
