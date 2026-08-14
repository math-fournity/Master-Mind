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

    gv0_store = sub.add_parser(
        "gv0-store-put",
        help="WP-GV0: 向 CompletionArtifactStore 写入 JSON 对象（content-addressed append-once）",
    )
    gv0_store.add_argument("--volume-root", required=True, type=Path)
    gv0_store.add_argument("--store-root", required=True, type=Path)
    gv0_store.add_argument("--input", required=True, type=Path)

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
    return {
        "version": __version__,
        "implemented": [
            "P0_READ_ONLY_PREFLIGHT",
            "P1_EPOCH_SCAFFOLD",
            "P1_IDEMPOTENT_SINGLE_FILE_COMMIT",
            "P1_CONTENT_CONFLICT_REJECTION",
            "P1_APPEND_ONLY_GATE_CHECKPOINT_AND_SEAL",
            "P1_LOCAL_ROOT_RECEIPT",
            "P1_EPOCH_VALIDATION",
            "WP1_SITE_STORAGE_PREREQUISITE",
            "WP1_STRICT_DB_OFFLINE_CONTRACT_REPORT",
            "WP_GV0_COMPLETION_CONTRACT_VERIFIER",
            "WP_GV0_SECURITY_CONTRACT_VERIFIER",
            "WP_GV0_COMPLETION_ARTIFACT_STORE",
            "WP_GV0_RESERVATION_BACKEND_PORT",
        ],
        "not_implemented": [
            "DATABASE_SITE_CAPABILITY_OR_MIGRATION_APPLY",
            "REDIS_OR_DISTRIBUTED_WORKERS",
            "P1_FULL_LEASE_FENCING_CRASH_RECOVERY_MATRIX",
            "REAL_SOLVER_DISPATCH",
            "NO_TOOL_CAPABILITY_ENFORCEMENT",
            "ANSWER_OR_HOLDOUT_VAULT",
            "CANDIDATE_OR_CASEPACK_IMPORT",
            "THREE_VIEW_AUDIT",
            "EVIDENCE_ASSEMBLY",
            "REVISION_OR_PROMOTION",
            "ARTIFACT_GC_OR_DELETE",
            "REAL_ED25519_SIGNATURE_VERIFICATION",
            "DB_V2_TRANSACTIONAL_LEDGER_BACKEND",
            "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER_BACKEND",
        ],
        "implementation_ceiling": "P1_DRY_RUN",
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


def _gv0_store_put(
    volume_root: Path, store_root: Path, input_path: Path
) -> dict[str, Any]:
    from .storage.artifact_store import CompletionArtifactStore

    with open(input_path) as f:
        payload = json.load(f)
    store = CompletionArtifactStore(root=store_root, volume_root=volume_root)
    ref = store.put_json(payload)
    return {
        "status": "PUT",
        "ref": ref.ref,
        "sha256": ref.sha256,
        "size_bytes": ref.size_bytes,
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
        if args.command == "gv0-store-put":
            result = _gv0_store_put(
                volume_root=args.volume_root,
                store_root=args.store_root,
                input_path=args.input,
            )
            _emit(result)
            return 0
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
