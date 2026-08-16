"""Create the zero-model preexecution freeze for POC-VMS-41R1.

This command binds the VMS-41R1 qualification pack, V2 role asset release,
attempt IDs, hidden grader artifacts and blind-review rubric.  It does not start
Devin, does not call a model, does not connect a database/Redis, and does not
invoke a Solver.  Live execution still requires a separate explicit
authorization and a runner that consumes this frozen manifest.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import platform
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.models import canonical_json_bytes
from system.tests.solve_vein_analysis.build_vms41r1_qualification_pack import (
    ATTEMPT_IDS,
    CASE_ORDER,
    FIXTURE_ROOT,
    PACK_ID,
    PARENT_PROTOCOL_PATH,
    PROTOCOL_PATH,
    load_vms41r1_qualification_pack,
    sha256_file,
)


HERE = Path(__file__).resolve().parent
LIVE_FIXTURES = HERE / "live_fixtures"
FREEZE_TARGET = LIVE_FIXTURES / "poc_vms_41r1.freeze.json"
ASSET_RELEASE = (
    REPO_ROOT / "system" / "assets" / "solve_vein_analysis" / "releases" / "0.4.1"
)
FINAL_ROOT = Path(
    "/data/master-mind-solve-vein-data/poc-results/"
    "poc-vms-41r1-event-extractor-qualification-20260814"
)
PARTIAL_ROOT = FINAL_ROOT.parent / f".{FINAL_ROOT.name}.partial"
SCHEMA_VERSION = "solve-vein/vms41r1-preexecution-freeze/v1"
POC_ID = "POC-VMS-41R1"
RUN_ID = "poc-vms-41r1-event-extractor-qualification-20260814"
EXPLICIT_NONCLAIMS = (
    "DOES_NOT_AUTHORIZE_LIVE_EXECUTION",
    "DOES_NOT_START_DEVIN_SESSION",
    "DOES_NOT_CALL_MODEL_SOLVER_DB_REDIS_OR_NETWORK",
    "DOES_NOT_QUALIFY_EVENT_EXTRACTOR_PROFILE",
    "DOES_NOT_COMPLETE_BLIND_MANUAL_AUDIT",
)


class VMS41R1FreezeError(RuntimeError):
    """Fail-closed preexecution-freeze error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def _safe_file(path: Path) -> Path:
    if path.is_symlink() or not path.is_file():
        raise VMS41R1FreezeError("UNSAFE_FILE", str(path))
    return path


def _safe_tree_files(root: Path) -> list[Path]:
    if root.is_symlink() or not root.is_dir():
        raise VMS41R1FreezeError("UNSAFE_TREE", str(root))
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if "__pycache__" in path.parts:
            continue
        if path.is_symlink():
            raise VMS41R1FreezeError("TREE_SYMLINK_MEMBER", str(path))
        if path.is_file():
            files.append(path)
    return files


def _manifest_members() -> list[Path]:
    roots = [
        ASSET_RELEASE,
        FIXTURE_ROOT,
    ]
    files = [
        PROTOCOL_PATH,
        PARENT_PROTOCOL_PATH,
        HERE / "build_vms41r1_qualification_pack.py",
        HERE / "build_vms41r1_qualification_pack.ref",
        HERE / "build_vms41r1_qualification_pack.ai-check",
        HERE / "freeze_vms41r1_event_extractor_preexecution.py",
        HERE / "test_event_extractor_qualification_v2.py",
        REPO_ROOT / "system" / "solve_vein_analysis" / "event_extraction_projection.py",
        REPO_ROOT / "system" / "solve_vein_analysis" / "file_effect_audit.py",
    ]
    members = [_safe_file(path) for path in files]
    for root in roots:
        members.extend(_safe_tree_files(root))
    unique = {path.resolve(strict=True): path for path in members}
    return [unique[key] for key in sorted(unique)]


def _file_record(path: Path) -> dict[str, Any]:
    return {
        "path": path.relative_to(REPO_ROOT).as_posix(),
        "sha256": sha256_file(path),
        "size_bytes": path.stat().st_size,
    }


def build_freeze_payload() -> dict[str, Any]:
    pack = load_vms41r1_qualification_pack()
    if pack["pack_id"] != PACK_ID or pack["case_count"] != len(CASE_ORDER):
        raise VMS41R1FreezeError("PACK_IDENTITY_INVALID", str(pack))
    if tuple(sorted(ATTEMPT_IDS)) != tuple(sorted(CASE_ORDER)):
        raise VMS41R1FreezeError("ATTEMPT_MAP_INCOMPLETE", "attempts must cover cases")
    if len(set(ATTEMPT_IDS.values())) != len(ATTEMPT_IDS):
        raise VMS41R1FreezeError("ATTEMPT_IDS_DUPLICATED", "attempt IDs must be unique")
    return {
        "schema_version": SCHEMA_VERSION,
        "poc_id": POC_ID,
        "run_id": RUN_ID,
        "freeze_status": "ZERO_MODEL_PREFREEZE_ONLY",
        "qualification_pack": {
            "pack_id": PACK_ID,
            "manifest_path": (
                FIXTURE_ROOT / "pack-manifest.json"
            ).relative_to(REPO_ROOT).as_posix(),
            "manifest_sha256": pack["manifest_sha256"],
            "case_count": pack["case_count"],
            "reference_candidate_count": pack["reference_candidate_count"],
            "negative_check_count": pack["negative_check_count"],
            "reference_self_check_verdict": pack["summary"]["verdict"],
            "mechanical_status_ceiling": "PENDING_BLIND_MANUAL_AUDIT",
        },
        "protocols": [
            _file_record(PARENT_PROTOCOL_PATH),
            _file_record(PROTOCOL_PATH),
        ],
        "asset_release": {
            "release_id": "solve-vein-event-extractor-assets-0.4.1",
            "path": ASSET_RELEASE.relative_to(REPO_ROOT).as_posix(),
            "files": [_file_record(path) for path in _safe_tree_files(ASSET_RELEASE)],
        },
        "case_order": list(CASE_ORDER),
        "attempt_ids": dict(ATTEMPT_IDS),
        "planned_live_attempts": len(CASE_ORDER),
        "runtime_profile_request": {
            "carrier": "devin_cli",
            "adapter_surface": "ModelRolePort/DevinCliModelRoleAdapter",
            "role": "REASONING_EVENT_EXTRACTOR_V2",
            "requested_cli_model_arg": "glm-5-2",
            "normalized_model_name": "GLM-5.2",
            "normalized_effort": "high",
            "effort_encoding": "model_uid",
            "fresh_session": True,
            "resume_allowed": False,
            "sandbox_requested": False,
            "permission_mode": "dangerous",
            "effective_model_probe": "NOT_RUN_IN_THIS_PREFREEZE",
        },
        "output_roots": {
            "final_root": str(FINAL_ROOT),
            "partial_root": str(PARTIAL_ROOT),
            "existence_checked_by_this_prefreeze": False,
        },
        "blind_review": {
            "rubric_path": (
                FIXTURE_ROOT / "blind-review-rubric.md"
            ).relative_to(REPO_ROOT).as_posix(),
            "rubric_sha256": sha256_file(FIXTURE_ROOT / "blind-review-rubric.md"),
            "status": "NOT_STARTED",
        },
        "side_effect_authorization": {
            "model_calls_authorized": 0,
            "devin_sessions_authorized": 0,
            "solver_calls_authorized": 0,
            "database_connections_authorized": 0,
            "redis_connections_authorized": 0,
            "network_calls_authorized": 0,
            "subagent_calls_authorized": 0,
            "future_live_attempts_require_new_explicit_authorization": True,
        },
        "frozen_members": [_file_record(path) for path in _manifest_members()],
        "explicit_nonclaims": list(EXPLICIT_NONCLAIMS),
        "platform": platform.platform(),
    }


def write_or_verify_freeze(target: Path = FREEZE_TARGET) -> dict[str, Any]:
    payload = build_freeze_payload()
    encoded = canonical_json_bytes(payload)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() or target.is_symlink():
        if target.is_symlink() or not target.is_file():
            raise VMS41R1FreezeError("FREEZE_TARGET_UNSAFE", str(target))
        if target.read_bytes() != encoded:
            raise VMS41R1FreezeError("FREEZE_TARGET_DRIFT", str(target))
        operation = "ALREADY_FROZEN"
    else:
        fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        try:
            os.write(fd, encoded)
            os.fsync(fd)
        finally:
            os.close(fd)
        operation = "FROZEN"
    try:
        display_path = target.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        display_path = str(target)
    return {
        "schema_version": "solve-vein/vms41r1-freeze-operation/v1",
        "operation": operation,
        "freeze_path": display_path,
        "freeze_sha256": sha256_file(target),
        "planned_live_attempts": len(CASE_ORDER),
        "model_calls_authorized": 0,
        "devin_sessions_authorized": 0,
        "database_connections_authorized": 0,
        "solver_calls_authorized": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=FREEZE_TARGET)
    args = parser.parse_args()
    result = write_or_verify_freeze(args.output)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, VMS41R1FreezeError) as exc:
        print(f"VMS41R1_FREEZE_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
