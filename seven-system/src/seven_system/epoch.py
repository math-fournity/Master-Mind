"""P0/P1 单 Epoch 初始化、dry-run 与完整性验证。"""

from __future__ import annotations

import json
import os
import re
import subprocess
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import SevenConfig
from .hashing import HASH_SPEC_VERSION, file_sha256, object_hash
from .preflight import run_preflight
from .schema_validation import validate_schema
from .storage import (
    ContentConflictError,
    commit_json_once,
    commit_text_once,
    read_json,
)


EPOCH_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
SCHEMA_ROOT = Path(__file__).resolve().parents[2] / "schemas"

CORE_JSON_FILES = (
    "runtime-manifest.json",
    "preflight-report.json",
    "phase-plan.json",
    "logging-contract.json",
    "scenario-matrix.json",
    "runtime-checkpoint.json",
    "evidence-index.json",
    "verdict.json",
)
REQUIRED_JSON_FILES = CORE_JSON_FILES + ("integrity-index.json",)
REQUIRED_TEXT_FILES = ("runbook.md", "summary.md")
INITIAL_SEALED_FILES = CORE_JSON_FILES + REQUIRED_TEXT_FILES
REQUIRED_DIRECTORIES = (
    "alerts",
    "artifacts",
    "audits",
    "evidence",
    "gate-decisions",
    "ledger",
    "quarantine",
    "revisions",
    "runtime-checkpoints",
)
P1_SEALED_FILES = (
    "dry-run-report.json",
    "gate-decisions/P1.json",
    "runtime-checkpoints/0001-p1-verified.json",
    "p1-verdict.json",
    "ledger/idempotency-probe.json",
)


class EpochError(RuntimeError):
    pass


def _jsonable_config(config: SevenConfig) -> dict[str, Any]:
    raw = asdict(config)
    for key, value in list(raw.items()):
        if isinstance(value, Path):
            raw[key] = str(value)
    return raw


def _git_metadata(repository_root: Path) -> dict[str, Any]:
    def run(*args: str) -> str | None:
        result = subprocess.run(
            ["git", "-C", str(repository_root), *args],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            return None
        return result.stdout.strip()

    branch = run("branch", "--show-current")
    commit = run("rev-parse", "HEAD")
    status = run("status", "--short", "--untracked-files=normal", "--", ".")
    ignored_parts = {"__pycache__", ".pytest_cache", ".runtime", ".git"}
    tree_entries = []
    for path in sorted(repository_root.rglob("*")):
        relative = path.relative_to(repository_root)
        if path.is_symlink() or any(part in ignored_parts for part in relative.parts):
            continue
        if not path.is_file() or relative.as_posix() == "config/runtime.local.json":
            continue
        tree_entries.append(
            {
                "path": relative.as_posix(),
                "sha256": file_sha256(path),
                "size": path.stat().st_size,
            }
        )
    return {
        "root": str(repository_root),
        "branch": branch,
        "commit": commit,
        "dirty": bool(status),
        "status_digest": object_hash(
            "GitStatus", "git-status/v1", {"status": status or ""}
        ),
        "source_tree_hash": object_hash(
            "SevenSourceTree", "source-tree/v1", tree_entries
        ),
        "source_file_count": len(tree_entries),
    }


def _phase_plan(epoch_id: str, manifest_hash: str) -> dict[str, Any]:
    phases = []
    definitions = [
        ("P0", "Preflight", [], "IMPLEMENTED"),
        ("P1", "Dry Run Primitives", ["P0"], "IMPLEMENTED"),
        ("P2", "Intake/Bare", ["P1"], "NOT_IMPLEMENTED"),
        ("P3", "CaseLab", ["P2"], "NOT_IMPLEMENTED"),
        ("P4", "Preregister", ["P3"], "NOT_IMPLEMENTED"),
        ("P5", "Experiment", ["P4"], "NOT_IMPLEMENTED"),
        ("P6", "Audit", ["P5"], "NOT_IMPLEMENTED"),
        ("P7", "Evidence", ["P6"], "NOT_IMPLEMENTED"),
        ("P8", "Revision/NO_CHANGE", ["P7"], "NOT_IMPLEMENTED"),
        ("P9", "Verdict", ["P8"], "NOT_IMPLEMENTED"),
    ]
    for phase_id, name, dependencies, status in definitions:
        phases.append(
            {
                "phase_id": phase_id,
                "name": name,
                "dependencies": dependencies,
                "status": status,
                "gate": f"G{phase_id[1:]}",
            }
        )
    return {
        "schema_version": "phase-plan/v1",
        "epoch_id": epoch_id,
        "manifest_hash": manifest_hash,
        "implementation_ceiling": "P1",
        "phases": phases,
        "stop_condition": "P1 dry-run verified or any blocker/protocol conflict",
    }


def _logging_contract(epoch_id: str, manifest_hash: str) -> dict[str, Any]:
    return {
        "schema_version": "logging-contract/v1",
        "epoch_id": epoch_id,
        "manifest_hash": manifest_hash,
        "required_context": [
            "epoch_id",
            "job_id",
            "logical_episode_id",
            "physical_attempt_id",
            "case_id",
            "arm_id",
            "strategy_release_id",
        ],
        "event_format": "jsonl",
        "redaction": {
            "forbidden": ["credentials", "sealed_solution", "holdout_payload"],
            "store_references_instead": True,
        },
        "alert_actions": {
            "P0": "abort_epoch",
            "P1": "pause_lane",
            "P2": "warn_or_backpressure",
            "P3": "work_item_policy",
        },
    }


def _scenario_matrix(epoch_id: str, manifest_hash: str) -> dict[str, Any]:
    scenarios = [
        ("SCF-0", "manifest and preflight scaffold", "IMPLEMENTED"),
        ("IDM-1", "same-content idempotent commit", "IMPLEMENTED"),
        ("IDM-2", "different-content conflict rejection", "IMPLEMENTED"),
        ("GS-0", "canonical 387 prerequisite gate", "NOT_IMPLEMENTED"),
        ("GS-1", "bare qualification", "NOT_IMPLEMENTED"),
        ("GS-2", "CaseLab and mathematical verification", "NOT_IMPLEMENTED"),
        ("GS-3", "lineage x oracle direction", "NOT_IMPLEMENTED"),
        ("GS-4", "operation path and critic", "NOT_IMPLEMENTED"),
        ("GS-5", "injection position", "NOT_IMPLEMENTED"),
        ("GS-6", "selector and forced misuse", "NOT_IMPLEMENTED"),
        ("GS-7", "three-view audit projection", "NOT_IMPLEMENTED"),
        ("GS-8", "coverage cells", "NOT_IMPLEMENTED"),
        ("GS-9", "revision or NO_CHANGE", "NOT_IMPLEMENTED"),
        ("GS-10", "canonical 387 crash/retry/rebuild matrix", "NOT_IMPLEMENTED"),
        ("GS-11", "evidence DAG replay", "NOT_IMPLEMENTED"),
        ("GS-C", "two independent TellCore composition", "FUTURE_NON_BLOCKING"),
    ]
    return {
        "schema_version": "scenario-matrix/v1",
        "epoch_id": epoch_id,
        "manifest_hash": manifest_hash,
        "scenarios": [
            {"scenario_id": item[0], "purpose": item[1], "status": item[2]}
            for item in scenarios
        ],
    }


def _runbook(epoch_id: str, manifest_hash: str) -> str:
    return f"""# Epoch {epoch_id} 运行手册

> RuntimeManifest: `{manifest_hash}`

本 Epoch 由 Seven System v0.1.0 创建，只允许P0与P1 scaffold dry-run。

1. 运行 `status`，确认 manifest 与文件完整性。
2. 运行 `dry-run`，验证同内容重复提交幂等、异内容冲突被拒绝。
3. 不连接数据库，不启动 Devin CLI，不访问答案 Vault。
4. 任一 BLOCK/冲突都停止；不得手工改写已提交文件。
5. PASS后读取append-only P1 Gate/checkpoint/verdict；它不代表387号完整P1。
6. 真实运行请回到 `seven-system/docs/operations.md` 检查前置能力。
"""


def _summary(epoch_id: str) -> str:
    return f"""# Epoch {epoch_id} 初始摘要

- 当前范围：P0 preflight + P1 scaffold dry-run。
- Solver：未启动；真实 dispatch 未实现。
- 数据库：未连接；未写入。
- 科学结论：NOT_TESTED。
- 下一步：运行dry-run并联合读取report、GateDecision、后续checkpoint与P1 verdict。
"""


def _initial_verdict(epoch_id: str, manifest_hash: str) -> dict[str, Any]:
    return {
        "schema_version": "scaffold-verdict/v1",
        "epoch_id": epoch_id,
        "manifest_hash": manifest_hash,
        "factory_pipeline": "NOT_TESTED",
        "p0_static_preflight": "PASS",
        "p1_dry_run_primitives": "READY",
        "p1_orchestration": "NOT_IMPLEMENTED",
        "scientific_analyzability": "NOT_TESTED",
        "tell_evidence": "NOT_TESTED",
        "six_gates": {
            "selectable": "NOT_TESTED",
            "executable": "NOT_TESTED",
            "terminable": "NOT_TESTED",
            "composable": "NOT_TESTED",
            "attributable": "NOT_TESTED",
            "longitudinal_continual_learning": "NOT_TESTED",
        },
        "blockers": ["P2_TO_P9_NOT_IMPLEMENTED"],
        "explicit_nonclaims": [
            "no real Solver was launched",
            "no database capability was exercised",
            "no Tell causal claim was tested",
        ],
        "overall_verdict": "SCAFFOLD_INITIALIZED",
    }


def _integrity_index(
    epoch_root: Path,
    *,
    epoch_id: str,
    manifest_hash: str,
    paths: tuple[str, ...],
    index_kind: str,
    previous_index_hash: str | None = None,
) -> dict[str, Any]:
    entries = []
    for relative in paths:
        path = epoch_root / relative
        entries.append(
            {
                "path": relative,
                "sha256": file_sha256(path),
                "size": path.stat().st_size,
            }
        )
    payload = {
        "schema_version": "epoch-integrity-index/v1",
        "index_kind": index_kind,
        "epoch_id": epoch_id,
        "manifest_hash": manifest_hash,
        "previous_index_hash": previous_index_hash,
        "entries": entries,
    }
    index_hash = object_hash(
        "EpochIntegrityIndex", payload["schema_version"], payload
    )
    return {**payload, "index_hash": index_hash}


def _local_receipt(
    *,
    epoch_id: str,
    manifest_hash: str,
    receipt_kind: str,
    index_hash: str,
    generated_at: str,
    previous_receipt_hash: str | None = None,
) -> dict[str, Any]:
    payload = {
        "schema_version": "local-root-receipt/v1",
        "receipt_kind": receipt_kind,
        "epoch_id": epoch_id,
        "manifest_hash": manifest_hash,
        "index_hash": index_hash,
        "previous_receipt_hash": previous_receipt_hash,
        "generated_at": generated_at,
        "trust_scope": "LOCAL_APPEND_ONCE_API_NOT_WORM",
    }
    return {
        **payload,
        "receipt_hash": object_hash(
            "LocalRootReceipt", payload["schema_version"], payload
        ),
    }


def _verify_local_receipt(
    path: Path,
    *,
    expected_kind: str,
    epoch_id: str,
    manifest_hash: str,
    index_hash: str,
    previous_receipt_hash: str | None,
    errors: list[str],
) -> dict[str, Any] | None:
    if not path.is_file() or path.is_symlink():
        errors.append(f"missing or invalid external receipt: {path.name}")
        return None
    try:
        payload = read_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid external receipt {path.name}: {exc}")
        return None
    if not isinstance(payload, dict):
        errors.append(f"external receipt root is not an object: {path.name}")
        return None
    _apply_schema(payload, "local-root-receipt.schema.json", path.name, errors)
    without_hash = {
        key: value for key, value in payload.items() if key != "receipt_hash"
    }
    actual_hash = object_hash(
        "LocalRootReceipt", payload.get("schema_version", ""), without_hash
    )
    if payload.get("receipt_hash") != actual_hash:
        errors.append(f"external receipt self-hash mismatch: {path.name}")
    expected = {
        "receipt_kind": expected_kind,
        "epoch_id": epoch_id,
        "manifest_hash": manifest_hash,
        "index_hash": index_hash,
        "previous_receipt_hash": previous_receipt_hash,
        "trust_scope": "LOCAL_APPEND_ONCE_API_NOT_WORM",
    }
    for key, value in expected.items():
        if payload.get(key) != value:
            errors.append(f"external receipt {key} mismatch: {path.name}")
    return payload


def init_epoch(config: SevenConfig, epoch_id: str) -> dict[str, Any]:
    if not EPOCH_ID_PATTERN.fullmatch(epoch_id):
        raise EpochError("invalid epoch_id; use letters, digits, dot, underscore or dash")

    preflight = run_preflight(config)
    if preflight["overall_verdict"] != "PASS":
        raise EpochError(
            "preflight did not PASS: blockers="
            + ",".join(preflight.get("blockers", []))
            + "; warnings="
            + ",".join(preflight.get("warnings", []))
        )

    config_payload = _jsonable_config(config)
    config_hash = object_hash("SevenConfig", config.schema_version, config_payload)
    epochs_root = config.data_root / "epochs"
    receipts_root = config.data_root / "receipts"
    if epochs_root.is_symlink() or (epochs_root.exists() and not epochs_root.is_dir()):
        raise EpochError("data_root/epochs must be a real directory, never a symlink")
    if receipts_root.is_symlink() or (
        receipts_root.exists() and not receipts_root.is_dir()
    ):
        raise EpochError("data_root/receipts must be a real directory, never a symlink")
    epochs_root.mkdir(exist_ok=True)
    receipts_root.mkdir(exist_ok=True)
    epoch_root = epochs_root / epoch_id
    if epoch_root.is_symlink() or (epoch_root.exists() and not epoch_root.is_dir()):
        raise EpochError("epoch_root must be a real directory, never a symlink")
    existing_manifest = epoch_root / "runtime-manifest.json"
    if existing_manifest.is_file():
        manifest = read_json(existing_manifest)
        if not isinstance(manifest, dict):
            raise EpochError("existing runtime manifest is not an object")
        if manifest.get("epoch_id") != epoch_id or manifest.get("config_hash") != config_hash:
            raise EpochError("existing epoch has a different identity or config")
        validation = validate_epoch(epoch_root)
        if (
            validation["verdict"] != "PASS"
            or validation["current_runtime_compatibility"] != "PASS"
        ):
            raise EpochError(
                "existing epoch is incomplete or corrupted: "
                + "; ".join(
                    validation["errors"] + validation["compatibility_errors"]
                )
            )
        return {
            "status": "ALREADY_INITIALIZED",
            "epoch_root": str(epoch_root),
            "manifest_hash": manifest.get("manifest_hash"),
        }

    epoch_root.mkdir(exist_ok=False)
    for directory in REQUIRED_DIRECTORIES:
        (epoch_root / directory).mkdir(exist_ok=True)

    created_at = datetime.now(timezone.utc).isoformat()
    preflight_hash = object_hash(
        "PreflightReport", preflight["schema_version"], preflight
    )
    device_evidence = next(
        (
            check.get("evidence", {})
            for check in preflight.get("checks", [])
            if check.get("check_id") == "data_root_device"
        ),
        {},
    )
    manifest_payload = {
        "schema_version": "runtime-manifest/v1",
        "epoch_id": epoch_id,
        "generated_at": created_at,
        "mode": config.mode,
        "config_hash": config_hash,
        "hash_spec_version": HASH_SPEC_VERSION,
        "repositories": {
            "evidence_factory": _git_metadata(config.repository_root),
            "solver_harness": {
                "path": str(config.harness_path),
                "capability_status": "NOT_EXERCISED_IN_DRY_RUN",
            },
            "sixth_generation_system": {
                "integration": "FROZEN_BUNDLE_ONLY",
                "direct_import": False,
            },
        },
        "database": {
            "expected_database": config.expected_database,
            "adapter_contract": config.database_adapter,
            "writes_enabled": False,
            "capability_report": None,
        },
        "storage": {
            "volume_root": str(config.volume_root),
            "data_root": str(config.data_root),
            "epoch_root": str(epoch_root),
            "vault_root": str(config.vault_root),
            "volume_device": device_evidence.get("volume_device"),
            "volume_readme_sha256": device_evidence.get("volume_readme_sha256"),
        },
        "runtime": {
            "tool_policy": config.tool_policy,
            "launch_interval_seconds": config.launch_interval_seconds,
            "max_concurrency": config.max_concurrency,
            "live_solver_dispatch": False,
            "redis_namespace": config.redis_namespace,
        },
        "inputs": {
            "candidate_manifest_hashes": [],
            "casepack_hash": None,
            "experiment_plan_hash": None,
            "tell_strategy_release_hash": None,
            "taxonomy_snapshot_hash": None,
            "tell_hint_relation_hash": None,
            "holdout_pack_hash": None,
        },
        "outputs": {
            "artifact_schema_version": "NOT_IMPLEMENTED",
            "evidence_schema_version": "evidence-record/v1-reserved",
            "verdict_schema_version": "scaffold-verdict/v1",
        },
        "preflight_report_hash": preflight_hash,
        "implementation": {
            "implemented_capabilities": [
                "P0_READ_ONLY_PREFLIGHT",
                "P1_SINGLE_FILE_IDEMPOTENCY",
                "P1_LOCAL_APPEND_ONCE_GATE_CHECKPOINT_AND_RECEIPT",
            ],
            "canonical_387_p1": "NOT_IMPLEMENTED",
            "not_implemented_phases": [f"P{number}" for number in range(2, 10)],
        },
    }
    manifest_hash = object_hash(
        "RuntimeManifest", manifest_payload["schema_version"], manifest_payload
    )
    manifest = {**manifest_payload, "manifest_hash": manifest_hash}

    commit_json_once(existing_manifest, manifest, boundary_root=epoch_root)
    commit_json_once(
        epoch_root / "preflight-report.json", preflight, boundary_root=epoch_root
    )
    commit_json_once(
        epoch_root / "phase-plan.json",
        _phase_plan(epoch_id, manifest_hash),
        boundary_root=epoch_root,
    )
    commit_json_once(
        epoch_root / "logging-contract.json",
        _logging_contract(epoch_id, manifest_hash),
        boundary_root=epoch_root,
    )
    commit_json_once(
        epoch_root / "scenario-matrix.json",
        _scenario_matrix(epoch_id, manifest_hash),
        boundary_root=epoch_root,
    )
    commit_json_once(
        epoch_root / "runtime-checkpoint.json",
        {
            "schema_version": "runtime-checkpoint/v1",
            "epoch_id": epoch_id,
            "manifest_hash": manifest_hash,
            "state": "INITIALIZED",
            "ledger_cursor": 0,
            "active_leases": [],
            "budgets": {},
        },
        boundary_root=epoch_root,
    )
    commit_json_once(
        epoch_root / "evidence-index.json",
        {
            "schema_version": "evidence-index/v1",
            "epoch_id": epoch_id,
            "manifest_hash": manifest_hash,
            "records": [],
            "status": "NOT_STARTED",
        },
        boundary_root=epoch_root,
    )
    commit_json_once(
        epoch_root / "verdict.json",
        _initial_verdict(epoch_id, manifest_hash),
        boundary_root=epoch_root,
    )
    commit_text_once(
        epoch_root / "runbook.md",
        _runbook(epoch_id, manifest_hash),
        boundary_root=epoch_root,
    )
    commit_text_once(
        epoch_root / "summary.md", _summary(epoch_id), boundary_root=epoch_root
    )
    initial_index = _integrity_index(
        epoch_root,
        epoch_id=epoch_id,
        manifest_hash=manifest_hash,
        paths=INITIAL_SEALED_FILES,
        index_kind="INITIAL_SCAFFOLD",
    )
    commit_json_once(
        epoch_root / "integrity-index.json",
        initial_index,
        boundary_root=epoch_root,
    )
    commit_json_once(
        receipts_root / f"{epoch_id}.initial.json",
        _local_receipt(
            epoch_id=epoch_id,
            manifest_hash=manifest_hash,
            receipt_kind="INITIAL_SCAFFOLD",
            index_hash=initial_index["index_hash"],
            generated_at=created_at,
        ),
        boundary_root=config.data_root,
    )

    initial_validation = validate_epoch(epoch_root)
    if (
        initial_validation["verdict"] != "PASS"
        or initial_validation["current_runtime_compatibility"] != "PASS"
    ):
        raise EpochError(
            "new epoch failed final validation: "
            + "; ".join(
                initial_validation["errors"]
                + initial_validation["compatibility_errors"]
            )
        )

    return {
        "status": "INITIALIZED",
        "epoch_root": str(epoch_root),
        "manifest_hash": manifest_hash,
    }


EXPECTED_SCHEMAS = {
    "runtime-manifest.json": "runtime-manifest/v1",
    "preflight-report.json": "preflight-report/v1",
    "phase-plan.json": "phase-plan/v1",
    "logging-contract.json": "logging-contract/v1",
    "scenario-matrix.json": "scenario-matrix/v1",
    "runtime-checkpoint.json": "runtime-checkpoint/v1",
    "evidence-index.json": "evidence-index/v1",
    "verdict.json": "scaffold-verdict/v1",
    "integrity-index.json": "epoch-integrity-index/v1",
}
SCHEMA_FILES = {
    "runtime-manifest.json": "runtime-manifest.schema.json",
    "preflight-report.json": "preflight-report.schema.json",
    "phase-plan.json": "phase-plan.schema.json",
    "logging-contract.json": "logging-contract.schema.json",
    "scenario-matrix.json": "scenario-matrix.schema.json",
    "runtime-checkpoint.json": "runtime-checkpoint.schema.json",
    "evidence-index.json": "evidence-index.schema.json",
    "verdict.json": "scaffold-verdict.schema.json",
    "integrity-index.json": "epoch-integrity-index.schema.json",
}
P1_SCHEMA_FILES = {
    "dry-run-report.json": "dry-run-report.schema.json",
    "gate-decisions/P1.json": "gate-decision.schema.json",
    "runtime-checkpoints/0001-p1-verified.json": "runtime-checkpoint.schema.json",
    "p1-verdict.json": "scaffold-verdict.schema.json",
    "ledger/idempotency-probe.json": "idempotency-probe.schema.json",
}


def _apply_schema(
    payload: dict[str, Any], schema_filename: str, artifact: str, errors: list[str]
) -> None:
    try:
        schema = read_json(SCHEMA_ROOT / schema_filename)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot load schema for {artifact}: {exc}")
        return
    if not isinstance(schema, dict):
        errors.append(f"schema root is not an object: {schema_filename}")
        return
    errors.extend(
        f"schema validation failed for {artifact}: {detail}"
        for detail in validate_schema(payload, schema)
    )


def _verify_integrity_index(
    epoch_root: Path,
    payload: dict[str, Any],
    *,
    expected_paths: tuple[str, ...],
    expected_kind: str,
    errors: list[str],
) -> None:
    claimed_hash = payload.get("index_hash")
    without_hash = {key: value for key, value in payload.items() if key != "index_hash"}
    actual_hash = object_hash(
        "EpochIntegrityIndex", payload.get("schema_version", ""), without_hash
    )
    if claimed_hash != actual_hash:
        errors.append(f"{expected_kind} integrity index hash mismatch")

    entries = payload.get("entries")
    if not isinstance(entries, list):
        errors.append(f"{expected_kind} integrity entries must be a list")
        return
    by_path: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            errors.append(f"{expected_kind} integrity entry is invalid")
            continue
        if entry["path"] in by_path:
            errors.append(f"duplicate integrity path: {entry['path']}")
        by_path[entry["path"]] = entry
    if set(by_path) != set(expected_paths):
        errors.append(f"{expected_kind} integrity path set mismatch")
    for relative in expected_paths:
        entry = by_path.get(relative)
        path = epoch_root / relative
        if entry is None:
            continue
        if not path.is_file() or path.is_symlink():
            errors.append(f"invalid sealed file path: {relative}")
            continue
        if entry.get("sha256") != file_sha256(path):
            errors.append(f"content hash mismatch: {relative}")
        if entry.get("size") != path.stat().st_size:
            errors.append(f"content size mismatch: {relative}")
    if payload.get("index_kind") != expected_kind:
        errors.append(f"integrity index kind mismatch: {expected_kind}")


def validate_epoch(epoch_root: Path) -> dict[str, Any]:
    errors: list[str] = []
    compatibility_errors: list[str] = []
    parsed: dict[str, Any] = {}
    initial_receipt_payload: dict[str, Any] | None = None
    if epoch_root.is_symlink() or epoch_root.parent.is_symlink() or epoch_root.parent.parent.is_symlink():
        errors.append("epoch path or approved ancestors contain a symlink")

    for filename in REQUIRED_JSON_FILES:
        path = epoch_root / filename
        if not path.is_file() or path.is_symlink():
            errors.append(f"missing or invalid file: {filename}")
            continue
        try:
            payload = read_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON {filename}: {exc}")
            continue
        if not isinstance(payload, dict):
            errors.append(f"JSON root must be an object: {filename}")
            continue
        parsed[filename] = payload
        if payload.get("schema_version") != EXPECTED_SCHEMAS[filename]:
            errors.append(f"schema_version mismatch in {filename}")
        _apply_schema(payload, SCHEMA_FILES[filename], filename, errors)

    for filename in REQUIRED_TEXT_FILES:
        path = epoch_root / filename
        if not path.is_file() or path.is_symlink():
            errors.append(f"missing or invalid file: {filename}")

    for directory in REQUIRED_DIRECTORIES:
        path = epoch_root / directory
        if not path.is_dir() or path.is_symlink():
            errors.append(f"missing or invalid directory: {directory}")

    manifest = parsed.get("runtime-manifest.json")
    if manifest is not None:
        claimed_hash = manifest.get("manifest_hash")
        without_hash = {
            key: value for key, value in manifest.items() if key != "manifest_hash"
        }
        actual_hash = object_hash(
            "RuntimeManifest", manifest.get("schema_version", ""), without_hash
        )
        if claimed_hash != actual_hash:
            errors.append("runtime-manifest hash mismatch")
        epoch_id = manifest.get("epoch_id")
        manifest_hash = manifest.get("manifest_hash")
        if not isinstance(epoch_id, str) or not EPOCH_ID_PATTERN.fullmatch(epoch_id):
            errors.append("runtime-manifest epoch_id is invalid")

        repositories = manifest.get("repositories")
        evidence_factory = (
            repositories.get("evidence_factory")
            if isinstance(repositories, dict)
            else None
        )
        if isinstance(evidence_factory, dict):
            source_root = Path(str(evidence_factory.get("root", "")))
            if source_root.is_dir() and not source_root.is_symlink():
                current_tree = _git_metadata(source_root)
                if current_tree.get("source_tree_hash") != evidence_factory.get(
                    "source_tree_hash"
                ):
                    compatibility_errors.append("evidence factory source tree drift")
            else:
                compatibility_errors.append(
                    "evidence factory source root is unavailable"
                )
        else:
            errors.append("runtime-manifest lacks evidence factory fingerprint")

        storage = manifest.get("storage")
        if isinstance(storage, dict):
            volume_root = Path(str(storage.get("volume_root", "")))
            volume_readme = volume_root / "README.md"
            if not volume_readme.is_file() or volume_readme.is_symlink():
                compatibility_errors.append("volume README is unavailable")
            elif file_sha256(volume_readme) != storage.get("volume_readme_sha256"):
                compatibility_errors.append("volume README hash drift")
            if volume_root.is_dir() and os.stat(volume_root).st_dev != storage.get(
                "volume_device"
            ):
                compatibility_errors.append("volume device drift")
        else:
            errors.append("runtime-manifest lacks storage fingerprint")
        for filename, payload in parsed.items():
            if filename == "runtime-manifest.json":
                continue
            if filename != "preflight-report.json" and payload.get("epoch_id") != epoch_id:
                errors.append(f"epoch_id mismatch in {filename}")
            if filename != "preflight-report.json" and payload.get("manifest_hash") != manifest_hash:
                errors.append(f"manifest_hash mismatch in {filename}")

        preflight = parsed.get("preflight-report.json")
        if preflight is not None:
            actual_preflight_hash = object_hash(
                "PreflightReport", preflight.get("schema_version", ""), preflight
            )
            if manifest.get("preflight_report_hash") != actual_preflight_hash:
                errors.append("preflight-report hash mismatch")
            if preflight.get("overall_verdict") != "PASS":
                errors.append("initialized epoch preflight was not PASS")

        runbook = epoch_root / "runbook.md"
        if runbook.is_file() and not runbook.is_symlink():
            try:
                if manifest_hash not in runbook.read_text(encoding="utf-8"):
                    errors.append("manifest_hash missing from runbook.md")
            except OSError as exc:
                errors.append(f"cannot read runbook.md: {exc}")

        index = parsed.get("integrity-index.json")
        if index is not None:
            _verify_integrity_index(
                epoch_root,
                index,
                expected_paths=INITIAL_SEALED_FILES,
                expected_kind="INITIAL_SCAFFOLD",
                errors=errors,
            )
            receipts_root = epoch_root.parent.parent / "receipts"
            if receipts_root.is_symlink() or not receipts_root.is_dir():
                errors.append("external receipt root is missing or a symlink")
            else:
                initial_receipt_payload = _verify_local_receipt(
                    receipts_root / f"{epoch_id}.initial.json",
                    expected_kind="INITIAL_SCAFFOLD",
                    epoch_id=epoch_id,
                    manifest_hash=manifest_hash,
                    index_hash=index.get("index_hash"),
                    previous_receipt_hash=None,
                    errors=errors,
                )

    phase_plan = parsed.get("phase-plan.json")
    if phase_plan is not None:
        phases = phase_plan.get("phases")
        if not isinstance(phases, list) or len(phases) != 10:
            errors.append("phase plan must contain ten phase objects")
        else:
            phase_ids = {
                item.get("phase_id") for item in phases if isinstance(item, dict)
            }
            if phase_ids != {f"P{number}" for number in range(10)}:
                errors.append("phase plan does not contain exactly P0-P9")

    logging_contract = parsed.get("logging-contract.json")
    if logging_contract is not None and (
        logging_contract.get("event_format") != "jsonl"
        or not isinstance(logging_contract.get("required_context"), list)
        or not logging_contract.get("required_context")
    ):
        errors.append("logging contract is incomplete")

    scenario_matrix = parsed.get("scenario-matrix.json")
    if scenario_matrix is not None:
        scenarios = scenario_matrix.get("scenarios")
        if not isinstance(scenarios, list) or not scenarios:
            errors.append("scenario catalog is incomplete")
        else:
            scenario_by_id = {
                item.get("scenario_id"): item
                for item in scenarios
                if isinstance(item, dict)
            }
            if len(scenario_by_id) != len(scenarios):
                errors.append("scenario IDs must be unique objects")
            for canonical_id in ("GS-0", "GS-10"):
                if scenario_by_id.get(canonical_id, {}).get("status") != "NOT_IMPLEMENTED":
                    errors.append(f"{canonical_id} must not be claimed implemented")

    initial_checkpoint = parsed.get("runtime-checkpoint.json")
    if initial_checkpoint is not None and (
        initial_checkpoint.get("state") != "INITIALIZED"
        or initial_checkpoint.get("ledger_cursor") != 0
        or initial_checkpoint.get("active_leases") != []
    ):
        errors.append("initial checkpoint is inconsistent")

    evidence_index = parsed.get("evidence-index.json")
    if evidence_index is not None and (
        evidence_index.get("status") != "NOT_STARTED"
        or evidence_index.get("records") != []
    ):
        errors.append("scaffold evidence index must remain empty")

    verdict = parsed.get("verdict.json")
    if verdict is not None and (
        verdict.get("factory_pipeline") != "NOT_TESTED"
        or verdict.get("tell_evidence") != "NOT_TESTED"
        or verdict.get("overall_verdict") != "SCAFFOLD_INITIALIZED"
    ):
        errors.append("initial scaffold verdict contains an unauthorized claim")

    p1_index_path = epoch_root / "p1-integrity-index.json"
    p1_paths = [epoch_root / relative for relative in P1_SEALED_FILES] + [
        p1_index_path
    ]
    p1_presence = [path.is_file() and not path.is_symlink() for path in p1_paths]
    p1_any_path = [path.exists() or path.is_symlink() for path in p1_paths]
    if any(p1_any_path):
        if not all(p1_presence):
            errors.append("P1 dry-run artifact set is incomplete")
        else:
            try:
                p1_payloads = {
                    relative: read_json(epoch_root / relative)
                    for relative in P1_SEALED_FILES
                }
                p1_index = read_json(p1_index_path)
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"invalid P1 artifact: {exc}")
            else:
                if not all(isinstance(item, dict) for item in p1_payloads.values()) or not isinstance(p1_index, dict):
                    errors.append("P1 JSON roots must be objects")
                else:
                    expected_p1_schemas = {
                        "dry-run-report.json": "dry-run-report/v1",
                        "gate-decisions/P1.json": "gate-decision/v1",
                        "runtime-checkpoints/0001-p1-verified.json": "runtime-checkpoint/v1",
                        "p1-verdict.json": "scaffold-verdict/v1",
                        "ledger/idempotency-probe.json": "idempotency-probe/v1",
                    }
                    for relative, payload in p1_payloads.items():
                        if payload.get("schema_version") != expected_p1_schemas[relative]:
                            errors.append(f"P1 schema mismatch in {relative}")
                        _apply_schema(
                            payload, P1_SCHEMA_FILES[relative], relative, errors
                        )
                    if p1_index.get("schema_version") != "epoch-integrity-index/v1":
                        errors.append("P1 integrity index schema mismatch")
                    _apply_schema(
                        p1_index,
                        "epoch-integrity-index.schema.json",
                        "p1-integrity-index.json",
                        errors,
                    )
                    _verify_integrity_index(
                        epoch_root,
                        p1_index,
                        expected_paths=P1_SEALED_FILES,
                        expected_kind="P1_DRY_RUN",
                        errors=errors,
                    )
                    base_index = parsed.get("integrity-index.json", {})
                    if p1_index.get("previous_index_hash") != base_index.get("index_hash"):
                        errors.append("P1 integrity chain does not reference initial index")
                    manifest_epoch_id = (
                        manifest.get("epoch_id") if isinstance(manifest, dict) else None
                    )
                    manifest_hash = (
                        manifest.get("manifest_hash")
                        if isinstance(manifest, dict)
                        else None
                    )
                    receipts_root = epoch_root.parent.parent / "receipts"
                    previous_receipt_hash = (
                        initial_receipt_payload.get("receipt_hash")
                        if isinstance(initial_receipt_payload, dict)
                        else None
                    )
                    _verify_local_receipt(
                        receipts_root / f"{manifest_epoch_id}.p1.json",
                        expected_kind="P1_DRY_RUN",
                        epoch_id=manifest_epoch_id,
                        manifest_hash=manifest_hash,
                        index_hash=p1_index.get("index_hash"),
                        previous_receipt_hash=previous_receipt_hash,
                        errors=errors,
                    )
                    if p1_index.get("epoch_id") != manifest_epoch_id:
                        errors.append("P1 integrity index epoch_id mismatch")
                    if p1_index.get("manifest_hash") != manifest_hash:
                        errors.append("P1 integrity index manifest_hash mismatch")
                    for relative, payload in p1_payloads.items():
                        if payload.get("epoch_id") != manifest_epoch_id:
                            errors.append(f"P1 epoch_id mismatch in {relative}")
                        if (
                            relative != "ledger/idempotency-probe.json"
                            and payload.get("manifest_hash") != manifest_hash
                        ):
                            errors.append(f"P1 manifest_hash mismatch in {relative}")
                    report = p1_payloads["dry-run-report.json"]
                    outcome = report.get("verdict")
                    if outcome not in {"PASS", "FAIL"}:
                        errors.append("dry-run report has an invalid outcome")
                    if report.get("scientific_claim") != "NOT_TESTED":
                        errors.append("dry-run report contains a scientific claim")
                    report_sha256 = file_sha256(epoch_root / "dry-run-report.json")

                    gate = p1_payloads["gate-decisions/P1.json"]
                    if gate.get("verdict") != outcome:
                        errors.append("P1 gate outcome disagrees with dry-run report")
                    if gate.get("evidence") != [
                        {"path": "dry-run-report.json", "sha256": report_sha256}
                    ]:
                        errors.append("P1 gate evidence does not bind the dry-run report")
                    if gate.get("next_allowed_phase") is not None:
                        errors.append("P1 gate must not unlock an unimplemented phase")
                    gate_sha256 = file_sha256(epoch_root / "gate-decisions" / "P1.json")

                    checkpoint = p1_payloads[
                        "runtime-checkpoints/0001-p1-verified.json"
                    ]
                    expected_state = (
                        "P1_DRY_RUN_VERIFIED"
                        if outcome == "PASS"
                        else "P1_DRY_RUN_FAILED"
                    )
                    if checkpoint.get("state") != expected_state:
                        errors.append("P1 checkpoint state is inconsistent")
                    if checkpoint.get("gate_decision_sha256") != gate_sha256:
                        errors.append("P1 checkpoint does not bind the gate decision")

                    p1_verdict = p1_payloads["p1-verdict.json"]
                    if p1_verdict.get("gate_decision_sha256") != gate_sha256:
                        errors.append("P1 verdict does not bind the gate decision")
                    if p1_verdict.get("p1_dry_run_primitives") != outcome:
                        errors.append("P1 verdict is inconsistent")
                    expected_overall = (
                        "P1_SCAFFOLD_VERIFIED"
                        if outcome == "PASS"
                        else "P1_SCAFFOLD_FAILED"
                    )
                    expected_orchestration = (
                        "SCAFFOLD_GATE_PASS" if outcome == "PASS" else "FAIL"
                    )
                    if (
                        p1_verdict.get("factory_pipeline") != "NOT_TESTED"
                        or p1_verdict.get("scientific_analyzability") != "NOT_TESTED"
                        or p1_verdict.get("tell_evidence") != "NOT_TESTED"
                        or p1_verdict.get("p1_orchestration")
                        != expected_orchestration
                        or p1_verdict.get("overall_verdict") != expected_overall
                    ):
                        errors.append("P1 scaffold verdict contains a scientific overclaim")

    return {
        "schema_version": "epoch-validation/v1",
        "epoch_root": str(epoch_root),
        "verdict": "PASS" if not errors else "FAIL",
        "artifact_integrity": "PASS" if not errors else "FAIL",
        "current_runtime_compatibility": (
            "PASS" if not compatibility_errors else "BLOCKED"
        ),
        "errors": errors,
        "compatibility_errors": compatibility_errors,
        "required_file_count": len(REQUIRED_JSON_FILES) + len(REQUIRED_TEXT_FILES),
        "required_directory_count": len(REQUIRED_DIRECTORIES),
        "p1_dry_run_present": all(p1_presence),
    }


def dry_run_epoch(config: SevenConfig, epoch_id: str) -> dict[str, Any]:
    initialized = init_epoch(config, epoch_id)
    epoch_root = Path(initialized["epoch_root"])
    report_path = epoch_root / "dry-run-report.json"
    p1_index_path = epoch_root / "p1-integrity-index.json"
    if p1_index_path.is_file():
        validation = validate_epoch(epoch_root)
        if (
            validation["verdict"] != "PASS"
            or validation["current_runtime_compatibility"] != "PASS"
        ):
            raise EpochError(
                "existing P1 dry-run is corrupted or incompatible: "
                + "; ".join(
                    validation["errors"] + validation["compatibility_errors"]
                )
            )
        return read_json(report_path)

    initial_validation = validate_epoch(epoch_root)
    if (
        initial_validation["verdict"] != "PASS"
        or initial_validation["current_runtime_compatibility"] != "PASS"
    ):
        raise EpochError(
            "initial scaffold validation failed: "
            + "; ".join(
                initial_validation["errors"]
                + initial_validation["compatibility_errors"]
            )
        )

    probe_path = epoch_root / "ledger" / "idempotency-probe.json"
    probe_payload = {
        "schema_version": "idempotency-probe/v1",
        "epoch_id": epoch_id,
        "value": "frozen",
    }
    first = commit_json_once(probe_path, probe_payload, boundary_root=epoch_root)
    second = commit_json_once(probe_path, probe_payload, boundary_root=epoch_root)
    conflict_rejected = False
    try:
        commit_json_once(
            probe_path,
            {**probe_payload, "value": "conflict"},
            boundary_root=epoch_root,
        )
    except ContentConflictError:
        conflict_rejected = True

    passed = (
        first in {"COMMITTED", "ALREADY_COMMITTED"}
        and second == "ALREADY_COMMITTED"
        and conflict_rejected
        and initial_validation["verdict"] == "PASS"
    )
    generated_at = datetime.now(timezone.utc).isoformat()
    report = {
        "schema_version": "dry-run-report/v1",
        "epoch_id": epoch_id,
        "manifest_hash": initialized["manifest_hash"],
        "generated_at": generated_at,
        "verdict": "PASS" if passed else "FAIL",
        "checks": {
            "probe_present_or_committed": first
            in {"COMMITTED", "ALREADY_COMMITTED"},
            "duplicate_commit_is_idempotent": second == "ALREADY_COMMITTED",
            "content_conflict_rejected": conflict_rejected,
            "initial_scaffold_validation": initial_validation,
        },
        "side_effects": {
            "database_connections": 0,
            "solver_launches": 0,
            "redis_writes": 0,
            "measurement_method": "static P0/P1 command scope; no live adapters exist",
        },
        "scientific_claim": "NOT_TESTED",
    }
    commit_json_once(report_path, report, boundary_root=epoch_root)
    report_hash = file_sha256(report_path)

    gate = {
        "schema_version": "gate-decision/v1",
        "gate_id": "G1",
        "phase_id": "P1",
        "epoch_id": epoch_id,
        "manifest_hash": initialized["manifest_hash"],
        "generated_at": generated_at,
        "verdict": "PASS" if passed else "FAIL",
        "evidence": [{"path": "dry-run-report.json", "sha256": report_hash}],
        "next_allowed_phase": None,
        "implementation_ceiling": "P1_DRY_RUN_SCAFFOLD",
    }
    gate_path = epoch_root / "gate-decisions" / "P1.json"
    commit_json_once(gate_path, gate, boundary_root=epoch_root)
    gate_hash = file_sha256(gate_path)

    checkpoint = {
        "schema_version": "runtime-checkpoint/v1",
        "checkpoint_id": "0001-p1-verified",
        "sequence": 1,
        "epoch_id": epoch_id,
        "manifest_hash": initialized["manifest_hash"],
        "generated_at": generated_at,
        "state": "P1_DRY_RUN_VERIFIED" if passed else "P1_DRY_RUN_FAILED",
        "gate_decision_sha256": gate_hash,
        "active_leases": [],
        "ledger_cursor": 1,
        "recovery": "NO_LIVE_WORK_TO_RECOVER",
    }
    commit_json_once(
        epoch_root / "runtime-checkpoints" / "0001-p1-verified.json",
        checkpoint,
        boundary_root=epoch_root,
    )

    p1_verdict = {
        "schema_version": "scaffold-verdict/v1",
        "epoch_id": epoch_id,
        "manifest_hash": initialized["manifest_hash"],
        "generated_at": generated_at,
        "factory_pipeline": "NOT_TESTED",
        "p0_static_preflight": "PASS",
        "p1_dry_run_primitives": "PASS" if passed else "FAIL",
        "p1_orchestration": "SCAFFOLD_GATE_PASS" if passed else "FAIL",
        "scientific_analyzability": "NOT_TESTED",
        "tell_evidence": "NOT_TESTED",
        "gate_decision_sha256": gate_hash,
        "explicit_nonclaims": [
            "canonical 387 P1 fault/recovery matrix was not executed",
            "no real Solver, database, Redis, Vault or scientific arm was exercised",
        ],
        "overall_verdict": "P1_SCAFFOLD_VERIFIED" if passed else "P1_SCAFFOLD_FAILED",
    }
    commit_json_once(
        epoch_root / "p1-verdict.json", p1_verdict, boundary_root=epoch_root
    )

    base_index = read_json(epoch_root / "integrity-index.json")
    p1_index = _integrity_index(
        epoch_root,
        epoch_id=epoch_id,
        manifest_hash=initialized["manifest_hash"],
        paths=P1_SEALED_FILES,
        index_kind="P1_DRY_RUN",
        previous_index_hash=base_index["index_hash"],
    )
    commit_json_once(
        p1_index_path,
        p1_index,
        boundary_root=epoch_root,
    )
    receipts_root = config.data_root / "receipts"
    initial_receipt = read_json(receipts_root / f"{epoch_id}.initial.json")
    commit_json_once(
        receipts_root / f"{epoch_id}.p1.json",
        _local_receipt(
            epoch_id=epoch_id,
            manifest_hash=initialized["manifest_hash"],
            receipt_kind="P1_DRY_RUN",
            index_hash=p1_index["index_hash"],
            generated_at=generated_at,
            previous_receipt_hash=initial_receipt["receipt_hash"],
        ),
        boundary_root=config.data_root,
    )
    final_validation = validate_epoch(epoch_root)
    if (
        final_validation["verdict"] != "PASS"
        or final_validation["current_runtime_compatibility"] != "PASS"
    ):
        raise EpochError(
            "P1 dry-run seal validation failed: "
            + "; ".join(
                final_validation["errors"]
                + final_validation["compatibility_errors"]
            )
        )
    return report
