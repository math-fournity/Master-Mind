"""只读 P0 preflight。

本模块不会连接数据库、创建目录、启动进程或修改队列。
"""

from __future__ import annotations

import json
import hashlib
import os
import re
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from .config import (
    CANONICAL_DATABASE_ADAPTER,
    CANONICAL_DATABASE_ID,
    LIVE_MODES,
    SevenConfig,
)
from .hashing import file_sha256, object_hash


ACTUAL_REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


REQUIRED_CAPABILITY_CLAIMS: dict[str, tuple[str, ...]] = {
    "database": (
        "expected_database_fail_closed",
        "reads_have_no_schema_side_effects",
        "cas_and_unique_indexes_verified",
    ),
    "safe_launch": (
        "structured_argv_or_readonly_prompt_file",
        "single_canonical_prompt_render",
        "launch_receipt_is_persisted",
    ),
    "no_tool": (
        "tool_surface_removed_or_empty_registry",
        "missing_observation_fails_closed",
        "all_terminal_states_are_audited",
        "solver_has_no_db_or_vault_credentials",
    ),
    "answer_isolation": (
        "solver_cannot_access_vault",
        "role_views_are_minimum_privilege",
        "access_is_append_only_audited",
    ),
}


@dataclass(frozen=True)
class Check:
    check_id: str
    verdict: str
    message: str
    evidence: Optional[dict[str, Any]] = None


def _inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def capability_subject_hashes(config: SevenConfig) -> dict[str, str]:
    """返回与当前代码、站点和隔离边界绑定的能力对象哈希。"""

    solver_asset = config.repository_root / "assets" / "solver" / "AGENTS.md"
    harness_hash = (
        file_sha256(config.harness_path)
        if config.harness_path.is_file() and not config.harness_path.is_symlink()
        else "MISSING"
    )
    asset_hash = (
        file_sha256(solver_asset)
        if solver_asset.is_file() and not solver_asset.is_symlink()
        else "MISSING"
    )
    subjects: dict[str, dict[str, Any]] = {
        "database": {
            "expected_database": config.expected_database,
            "adapter_contract": config.database_adapter,
        },
        "safe_launch": {
            "harness_path": str(config.harness_path.resolve()),
            "harness_sha256": harness_hash,
            "solver_asset_sha256": asset_hash,
            "launch_interval_seconds": config.launch_interval_seconds,
        },
        "no_tool": {
            "harness_sha256": harness_hash,
            "solver_asset_sha256": asset_hash,
            "tool_policy": config.tool_policy,
        },
        "answer_isolation": {
            "data_root": str(config.data_root.resolve()),
            "vault_root": str(config.vault_root.resolve()),
            "solver_work_root": str(config.solver_work_root.resolve()),
            "trajectory_root": str(config.trajectory_root.resolve()),
        },
    }
    return {
        name: object_hash("CapabilitySubject", f"{name}/v1", subject)
        for name, subject in subjects.items()
    }


def _capability_check(
    check_id: str,
    path: Optional[Path],
    *,
    required: bool,
    expected_capability: str,
    expected_subject_hash: str,
) -> Check:
    if expected_capability == "database":
        if required:
            return Check(
                check_id,
                "BLOCK",
                "legacy capability-report/v1 is not accepted for database site capability; "
                "the dedicated semantic verifier is not implemented",
            )
        return Check(
            check_id,
            "NOT_REQUIRED",
            "dry_run does not consume any database capability report",
        )
    if path is None:
        if required:
            return Check(check_id, "BLOCK", "required capability report is not configured")
        return Check(check_id, "NOT_REQUIRED", "not required for dry_run")
    if not path.is_absolute():
        return Check(check_id, "BLOCK", "capability report path must be absolute")
    if path.is_symlink():
        return Check(check_id, "BLOCK", "capability report must not be a symlink")
    if not path.is_file():
        return Check(check_id, "BLOCK" if required else "WARN", f"missing report: {path}")
    try:
        report_bytes = path.read_bytes()
        payload = json.loads(report_bytes)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return Check(check_id, "BLOCK", f"invalid capability report: {exc}")
    report_sha256 = hashlib.sha256(report_bytes).hexdigest()
    if not isinstance(payload, dict):
        return Check(
            check_id,
            "BLOCK" if required else "WARN",
            "capability report JSON root must be an object",
            {"sha256": report_sha256},
        )
    claims = payload.get("claims")
    report_checks = payload.get("checks")
    required_claims = REQUIRED_CAPABILITY_CLAIMS[expected_capability]
    shape_ok = (
        payload.get("schema_version") == "capability-report/v1"
        and payload.get("capability") == expected_capability
        and isinstance(payload.get("generated_at"), str)
        and isinstance(payload.get("subject_hash"), str)
        and re.fullmatch(r"[0-9a-f]{64}", payload.get("subject_hash")) is not None
        and payload.get("subject_hash") == expected_subject_hash
        and isinstance(report_checks, list)
        and bool(report_checks)
        and all(
            isinstance(item, dict)
            and isinstance(item.get("check_id"), str)
            and bool(item.get("check_id"))
            and item.get("verdict") == "PASS"
            for item in report_checks
        )
        and isinstance(claims, dict)
        and all(claims.get(claim) is True for claim in required_claims)
    )
    verdict = payload.get("verdict")
    if verdict != "PASS" or not shape_ok:
        return Check(
            check_id,
            "BLOCK" if required else "WARN",
            "capability report is not a valid, claim-complete PASS",
            {
                "sha256": report_sha256,
                "expected_subject_hash": expected_subject_hash,
                "actual_subject_hash": payload.get("subject_hash"),
            },
        )
    return Check(
        check_id,
        "PASS",
        "capability report is present and PASS",
        {"path": str(path), "sha256": report_sha256},
    )


def run_preflight(config: SevenConfig) -> dict[str, Any]:
    checks: list[Check] = []
    live = config.mode in LIVE_MODES

    checks.append(
        Check(
            "system_identity",
            "PASS" if config.system_id == "seven-system" else "BLOCK",
            f"system_id={config.system_id}",
        )
    )

    database_contract_ok = (
        config.expected_database == CANONICAL_DATABASE_ID
        and config.database_adapter == CANONICAL_DATABASE_ADAPTER
    )
    checks.append(
        Check(
            "database_contract_identity",
            "PASS" if database_contract_ok else "BLOCK",
            "database identity and adapter contract must match the canonical Seven values",
        )
    )

    repository_root = config.repository_root
    repository_identity_ok = (
        repository_root.is_absolute()
        and repository_root.is_dir()
        and repository_root.resolve() == ACTUAL_REPOSITORY_ROOT.resolve()
    )
    checks.append(
        Check(
            "repository_root",
            "PASS" if repository_identity_ok else "BLOCK",
            (
                f"configured={repository_root}; actual={ACTUAL_REPOSITORY_ROOT}"
            ),
        )
    )

    volume_ok = (
        config.volume_root.is_absolute()
        and config.volume_root.is_dir()
        and not config.volume_root.is_symlink()
        and os.path.ismount(config.volume_root)
    )
    checks.append(
        Check(
            "volume_mounted",
            "PASS" if volume_ok else "BLOCK",
            f"volume_root={config.volume_root}; is_mount={os.path.ismount(config.volume_root)}",
        )
    )

    volume_readme = config.volume_root / "README.md"
    readme_ok = (
        config.require_volume_readme
        and volume_readme.is_file()
        and not volume_readme.is_symlink()
    )
    checks.append(
        Check(
            "volume_readme",
            "PASS" if readme_ok else "BLOCK",
            (
                "volume README present"
                if readme_ok
                else f"required volume README is missing: {volume_readme}"
            ),
        )
    )

    epochs_root = config.data_root / "epochs"
    receipts_root = config.data_root / "receipts"
    data_path_safe = (
        config.data_root.is_absolute()
        and config.data_root != config.volume_root
        and _inside(config.data_root, config.volume_root)
        and not _inside(config.data_root, repository_root)
        and not _inside(repository_root, config.data_root)
        and not config.data_root.is_symlink()
        and (not epochs_root.exists() or (epochs_root.is_dir() and not epochs_root.is_symlink()))
        and (
            not receipts_root.exists()
            or (receipts_root.is_dir() and not receipts_root.is_symlink())
        )
    )
    checks.append(
        Check(
            "data_root_boundary",
            "PASS" if data_path_safe else "BLOCK",
            "data_root must be an absolute strict child of volume_root and outside the repo",
            {"data_root": str(config.data_root)},
        )
    )
    data_root_ready = config.data_root.is_dir() and os.access(config.data_root, os.W_OK)
    checks.append(
        Check(
            "data_root_ready",
            "PASS" if data_root_ready else "BLOCK",
            (
                f"data_root exists and is writable: {config.data_root}"
                if data_root_ready
                else f"data_root must already exist and be writable: {config.data_root}"
            ),
        )
    )

    same_device = False
    if volume_ok and data_root_ready:
        same_device = os.stat(config.volume_root).st_dev == os.stat(config.data_root).st_dev
    device_verdict = (
        "PASS"
        if same_device
        else ("BLOCK" if volume_ok and data_root_ready else "NOT_EVALUABLE")
    )
    checks.append(
        Check(
            "data_root_device",
            device_verdict,
            "data_root must reside on the mounted volume device",
            {
                "volume_device": os.stat(config.volume_root).st_dev if volume_ok else None,
                "data_device": os.stat(config.data_root).st_dev if data_root_ready else None,
                "volume_readme_sha256": file_sha256(volume_readme) if readme_ok else None,
            },
        )
    )

    if volume_ok:
        free_bytes = shutil.disk_usage(config.volume_root).free
        enough_space = free_bytes >= config.minimum_free_bytes
        checks.append(
            Check(
                "disk_capacity",
                "PASS" if enough_space else "BLOCK",
                f"free_bytes={free_bytes}, required={config.minimum_free_bytes}",
                {"free_bytes": free_bytes},
            )
        )

    db_env = os.environ.get("ARANGO_DB")
    db_required = live or config.allow_database_writes
    if db_required:
        db_ok = db_env == config.expected_database
        checks.append(
            Check(
                "expected_database",
                "PASS" if db_ok else "BLOCK",
                (
                    "ARANGO_DB matches expected database"
                    if db_ok
                    else "ARANGO_DB is unset or does not match expected database"
                ),
                {
                    "expected": config.expected_database,
                    "present": db_env is not None,
                    "matches": db_ok,
                },
            )
        )
    else:
        checks.append(
            Check(
                "expected_database",
                "NOT_REQUIRED",
                "dry_run performs no database connection or write",
                {"expected": config.expected_database},
            )
        )

    checks.append(
        Check(
            "database_writes_disabled",
            "PASS" if not config.allow_database_writes else "BLOCK",
            (
                "v0.1.0 has no database write path"
                if not config.allow_database_writes
                else "database.allow_writes must remain false in P0/P1"
            ),
        )
    )

    namespace_ok = (
        config.redis_namespace.startswith("evidence:seven:")
        and not config.redis_namespace.startswith("math:")
    )
    checks.append(
        Check(
            "queue_namespace",
            "PASS" if namespace_ok else "BLOCK",
            f"redis_namespace={config.redis_namespace}",
        )
    )

    harness_ok = (
        config.harness_path.is_absolute()
        and config.harness_path.is_file()
        and not config.harness_path.is_symlink()
    )
    checks.append(
        Check(
            "solver_harness_present",
            ("PASS" if harness_ok else "BLOCK") if live else "NOT_REQUIRED",
            (
                f"harness_path={config.harness_path}"
                if live
                else "dry_run does not load or execute a Solver Harness"
            ),
        )
    )

    roots_ok = all(
        path.is_absolute()
        and not _inside(path, repository_root)
        and _inside(path, config.data_root)
        for path in (config.solver_work_root, config.trajectory_root)
    ) and config.solver_work_root.resolve() != config.trajectory_root.resolve()
    checks.append(
        Check(
            "solver_root_isolation",
            "PASS" if roots_ok else "BLOCK",
            "solver roots must be distinct children of Seven data_root and outside the repo",
        )
    )

    checks.append(
        Check(
            "no_tool_policy",
            "PASS" if config.tool_policy == "forbid_all" else "BLOCK",
            f"tool_policy={config.tool_policy}",
        )
    )
    checks.append(
        Check(
            "launch_interval_floor",
            "PASS" if config.launch_interval_seconds >= 3 else "BLOCK",
            f"launch_interval_seconds={config.launch_interval_seconds}",
        )
    )

    solver_asset = repository_root / "assets" / "solver" / "AGENTS.md"
    asset_ok = False
    if solver_asset.is_file():
        text = solver_asset.read_text(encoding="utf-8")
        required_phrases = (
            "不要使用任何工具",
            "### PROOF COMPLETE",
            "### I CANNOT SOLVE THIS",
        )
        asset_ok = all(phrase in text for phrase in required_phrases)
    checks.append(
        Check(
            "solver_asset_contract",
            "PASS" if asset_ok else "BLOCK",
            f"canonical solver asset={solver_asset}",
        )
    )

    vault_boundary_ok = (
        config.vault_root.is_absolute()
        and _inside(config.vault_root, config.data_root)
        and not _inside(config.vault_root, config.solver_work_root)
        and not _inside(config.solver_work_root, config.vault_root)
        and not _inside(config.vault_root, config.trajectory_root)
        and not _inside(config.trajectory_root, config.vault_root)
    )
    checks.append(
        Check(
            "answer_vault_boundary",
            "PASS" if vault_boundary_ok else "BLOCK",
            "vault must be inside data_root and outside solver work root",
        )
    )

    subject_hashes = capability_subject_hashes(config)
    checks.extend(
        [
            _capability_check(
                "database_capability",
                config.database_capability_report,
                required=live,
                expected_capability="database",
                expected_subject_hash=subject_hashes["database"],
            ),
            _capability_check(
                "safe_launch_capability",
                config.safe_launch_capability_report,
                required=live,
                expected_capability="safe_launch",
                expected_subject_hash=subject_hashes["safe_launch"],
            ),
            _capability_check(
                "no_tool_capability",
                config.no_tool_capability_report,
                required=live,
                expected_capability="no_tool",
                expected_subject_hash=subject_hashes["no_tool"],
            ),
            _capability_check(
                "answer_isolation_capability",
                config.answer_isolation_capability_report,
                required=live,
                expected_capability="answer_isolation",
                expected_subject_hash=subject_hashes["answer_isolation"],
            ),
        ]
    )

    if live:
        checks.append(
            Check(
                "live_execution_implementation",
                "BLOCK",
                "v0.1.0 implements P0/P1 only; live Solver dispatch is NOT_IMPLEMENTED",
            )
        )
    elif config.allow_live_solver_dispatch:
        checks.append(
            Check(
                "live_dispatch_disabled",
                "BLOCK",
                "dry_run config must set allow_live_dispatch=false",
            )
        )
    else:
        checks.append(
            Check(
                "live_dispatch_disabled",
                "PASS",
                "dry_run cannot dispatch a real Solver",
            )
        )

    blockers = [check.check_id for check in checks if check.verdict == "BLOCK"]
    warnings = [check.check_id for check in checks if check.verdict == "WARN"]
    overall = "BLOCKED" if blockers else ("PARTIAL" if warnings else "PASS")

    return {
        "schema_version": "preflight-report/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "system_id": config.system_id,
        "mode": config.mode,
        "overall_verdict": overall,
        "implementation_ceiling": "P1_DRY_RUN",
        "allowed_phases": ["P0", "P1"] if not blockers else [],
        "forbidden_phases": [f"P{number}" for number in range(2, 10)],
        "checks": [asdict(check) for check in checks],
        "blockers": blockers,
        "warnings": warnings,
        "side_effects": "NONE",
    }
