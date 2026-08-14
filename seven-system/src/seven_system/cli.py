"""Seven System v0.1.0 的统一命令行入口。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from . import __version__
from .config import ConfigError, load_config
from .epoch import EpochError, dry_run_epoch, init_epoch, validate_epoch
from .preflight import run_preflight
from .storage import ContentConflictError, read_json


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

    sub.add_parser("capabilities", help="列出已实现与明确未实现的能力")
    return parser


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
        ],
        "not_implemented": [
            "DATABASE_MIGRATIONS_OR_WRITES",
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
        ],
        "implementation_ceiling": "P1_DRY_RUN",
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
    except (ConfigError, EpochError, ContentConflictError, OSError, json.JSONDecodeError) as exc:
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
