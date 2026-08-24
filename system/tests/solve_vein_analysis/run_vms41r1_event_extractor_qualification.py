"""Zero-model runner shell for POC-VMS-41R1 Event Extractor qualification.

The default command validates the frozen VMS-41R1 preexecution manifest and
derives the future live attempt/workspace plan.  It does not start Devin, call a
model, connect DB/Redis, invoke Solver, or write a live result bundle.

Live execution is deliberately not implemented in this stage.  Passing
``--execute`` fails closed with ``LIVE_NOT_AUTHORIZED`` until a later explicit
permit and blind-review seal protocol are implemented.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.tests.solve_vein_analysis.freeze_vms41r1_event_extractor_preexecution import (
    FINAL_ROOT,
    FREEZE_TARGET,
    PARTIAL_ROOT,
    POC_ID,
    RUN_ID,
    SCHEMA_VERSION as FREEZE_SCHEMA_VERSION,
    sha256_file,
)
from system.tests.solve_vein_analysis.historical_binding import (
    HistoricalBindingError,
    validate_current_or_historical_binding,
)


EXPECTED_VISIBLE_FILES = (
    "AGENTS.md",
    "TASK.md",
    "problem.md",
    "raw_solver_trajectory.txt",
    "reasoning-trajectory-candidate-v2.md",
    "input-manifest.json",
    "devin-config.json",
    "catalog-snapshot.txt",
)
EXPECTED_WRITABLE_FILES = (
    "reasoning-trajectory-candidate-v2.json",
    "DONE.md",
)
HIDDEN_FORBIDDEN_FILES = (
    "acceptable-sets.json",
    "reference-candidates.json",
    "negative-checks.json",
    "thresholds.json",
    "blind-review-rubric.md",
)
RECEIPT_SCHEMA_VERSION = "solve-vein/vms41r1-runner-preflight/v1"


class VMS41R1RunnerError(RuntimeError):
    """Fail-closed VMS-41R1 runner-shell error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def _load_json_object(path: Path, label: str) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise VMS41R1RunnerError("UNSAFE_JSON", f"{label}: {path}")
    try:
        value = json.loads(path.read_text())
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise VMS41R1RunnerError("INVALID_JSON", f"{label}: {exc}") from exc
    if not isinstance(value, dict):
        raise VMS41R1RunnerError("JSON_NOT_OBJECT", label)
    return value


def _exact_keys(value: Mapping[str, Any], expected: set[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        raise VMS41R1RunnerError(
            "KEYS_MISMATCH",
            f"{label}: missing={sorted(expected - actual)}, unknown={sorted(actual - expected)}",
        )


def load_and_validate_freeze(path: Path = FREEZE_TARGET) -> dict[str, Any]:
    freeze = _load_json_object(path, "VMS41R1 freeze")
    _exact_keys(
        freeze,
        {
            "schema_version",
            "poc_id",
            "run_id",
            "freeze_status",
            "qualification_pack",
            "protocols",
            "asset_release",
            "case_order",
            "attempt_ids",
            "planned_live_attempts",
            "runtime_profile_request",
            "output_roots",
            "blind_review",
            "side_effect_authorization",
            "frozen_members",
            "explicit_nonclaims",
            "platform",
        },
        "freeze",
    )
    if freeze["schema_version"] != FREEZE_SCHEMA_VERSION:
        raise VMS41R1RunnerError("FREEZE_SCHEMA_MISMATCH", str(freeze["schema_version"]))
    if freeze["poc_id"] != POC_ID or freeze["run_id"] != RUN_ID:
        raise VMS41R1RunnerError("FREEZE_IDENTITY_MISMATCH", str(path))
    if freeze["freeze_status"] != "ZERO_MODEL_PREFREEZE_ONLY":
        raise VMS41R1RunnerError("FREEZE_STATUS_MISMATCH", str(freeze["freeze_status"]))

    case_order = freeze["case_order"]
    attempts = freeze["attempt_ids"]
    if (
        not isinstance(case_order, list)
        or len(case_order) != 6
        or any(not isinstance(case_id, str) for case_id in case_order)
    ):
        raise VMS41R1RunnerError("CASE_ORDER_INVALID", str(case_order))
    if (
        not isinstance(attempts, dict)
        or set(attempts) != set(case_order)
        or len(set(attempts.values())) != len(case_order)
    ):
        raise VMS41R1RunnerError("ATTEMPT_MAP_INVALID", str(attempts))
    if freeze["planned_live_attempts"] != len(case_order):
        raise VMS41R1RunnerError("ATTEMPT_COUNT_MISMATCH", str(freeze["planned_live_attempts"]))

    side_effects = freeze["side_effect_authorization"]
    required_zero = {
        "model_calls_authorized",
        "devin_sessions_authorized",
        "solver_calls_authorized",
        "database_connections_authorized",
        "redis_connections_authorized",
        "network_calls_authorized",
        "subagent_calls_authorized",
    }
    if not isinstance(side_effects, dict):
        raise VMS41R1RunnerError("SIDE_EFFECTS_INVALID", "not object")
    for key in required_zero:
        if side_effects.get(key) != 0:
            raise VMS41R1RunnerError("SIDE_EFFECT_NOT_ZERO", key)
    if side_effects.get("future_live_attempts_require_new_explicit_authorization") is not True:
        raise VMS41R1RunnerError("LIVE_AUTH_FLAG_INVALID", "future authorization flag missing")

    _verify_frozen_members(freeze["frozen_members"])
    _verify_asset_release(freeze["asset_release"])
    _verify_pack_binding(freeze["qualification_pack"])
    _verify_blind_review_binding(freeze["blind_review"])
    return freeze


def _verify_frozen_members(rows: Any) -> None:
    if not isinstance(rows, list) or not rows:
        raise VMS41R1RunnerError("FROZEN_MEMBERS_INVALID", "empty")
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise VMS41R1RunnerError("FROZEN_MEMBER_INVALID", str(index))
        _exact_keys(row, {"path", "sha256", "size_bytes"}, f"frozen_members[{index}]")
        relative = row["path"]
        if not isinstance(relative, str) or relative in seen:
            raise VMS41R1RunnerError("FROZEN_MEMBER_PATH_INVALID", str(relative))
        seen.add(relative)
        try:
            validate_current_or_historical_binding(
                REPO_ROOT,
                relative,
                row["sha256"],
                expected_size=row["size_bytes"],
            )
        except HistoricalBindingError as exc:
            code = (
                "FROZEN_MEMBER_UNSAFE"
                if exc.code.startswith("CURRENT_PATH_") or exc.code == "PATH_INVALID"
                else "FROZEN_MEMBER_DRIFT"
            )
            raise VMS41R1RunnerError(code, f"{relative}: {exc.code}") from exc


def _verify_asset_release(binding: Any) -> None:
    if not isinstance(binding, dict):
        raise VMS41R1RunnerError("ASSET_RELEASE_INVALID", "not object")
    _exact_keys(binding, {"release_id", "path", "files"}, "asset_release")
    if binding["release_id"] != "solve-vein-event-extractor-assets-0.4.1":
        raise VMS41R1RunnerError("ASSET_RELEASE_ID_MISMATCH", str(binding["release_id"]))
    files = binding["files"]
    if not isinstance(files, list):
        raise VMS41R1RunnerError("ASSET_RELEASE_FILES_INVALID", "not list")
    names = {Path(row["path"]).name for row in files if isinstance(row, dict) and "path" in row}
    expected = {
        "AGENTS_event_extractor.md",
        "TASK_event_extractor.template.md",
        "reasoning-trajectory-candidate-v2.md",
        "README.md",
    }
    if names != expected:
        raise VMS41R1RunnerError("ASSET_RELEASE_FILE_SET_MISMATCH", str(sorted(names)))


def _verify_pack_binding(binding: Any) -> None:
    if not isinstance(binding, dict):
        raise VMS41R1RunnerError("PACK_BINDING_INVALID", "not object")
    required = {
        "pack_id",
        "manifest_path",
        "manifest_sha256",
        "case_count",
        "reference_candidate_count",
        "negative_check_count",
        "reference_self_check_verdict",
        "mechanical_status_ceiling",
    }
    _exact_keys(binding, required, "qualification_pack")
    if binding["case_count"] != 6 or binding["reference_candidate_count"] != 6:
        raise VMS41R1RunnerError("PACK_COUNT_MISMATCH", str(binding))
    if binding["negative_check_count"] != 4:
        raise VMS41R1RunnerError("PACK_NEGATIVE_COUNT_MISMATCH", str(binding))
    if binding["reference_self_check_verdict"] != "PASS":
        raise VMS41R1RunnerError("PACK_SELF_CHECK_NOT_PASS", str(binding))
    if binding["mechanical_status_ceiling"] != "PENDING_BLIND_MANUAL_AUDIT":
        raise VMS41R1RunnerError("PACK_CEILING_MISMATCH", str(binding))
    manifest = REPO_ROOT / str(binding["manifest_path"])
    if manifest.is_symlink() or not manifest.is_file() or sha256_file(manifest) != binding["manifest_sha256"]:
        raise VMS41R1RunnerError("PACK_MANIFEST_DRIFT", str(manifest))


def _verify_blind_review_binding(binding: Any) -> None:
    if not isinstance(binding, dict):
        raise VMS41R1RunnerError("BLIND_REVIEW_INVALID", "not object")
    _exact_keys(binding, {"rubric_path", "rubric_sha256", "status"}, "blind_review")
    if binding["status"] != "NOT_STARTED":
        raise VMS41R1RunnerError("BLIND_REVIEW_STATUS_MISMATCH", str(binding["status"]))
    rubric = REPO_ROOT / str(binding["rubric_path"])
    if rubric.is_symlink() or not rubric.is_file() or sha256_file(rubric) != binding["rubric_sha256"]:
        raise VMS41R1RunnerError("BLIND_REVIEW_RUBRIC_DRIFT", str(rubric))


def derive_attempt_plan(freeze: Mapping[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    attempts = freeze["attempt_ids"]
    for case_id in freeze["case_order"]:
        case_root = (
            REPO_ROOT
            / "system/tests/solve_vein_analysis/qualification_fixtures/vms41r1"
            / case_id
        )
        public_files = ("problem.md", "raw_solver_trajectory.txt", "input-manifest.json")
        missing = [
            name
            for name in public_files
            if (case_root / name).is_symlink() or not (case_root / name).is_file()
        ]
        hidden_present = [
            name
            for name in HIDDEN_FORBIDDEN_FILES
            if (case_root / name).exists() or (case_root / name).is_symlink()
        ]
        if missing:
            raise VMS41R1RunnerError("PUBLIC_CASE_FILE_MISSING", f"{case_id}:{missing}")
        if hidden_present:
            raise VMS41R1RunnerError("HIDDEN_FILE_IN_PUBLIC_CASE_DIR", f"{case_id}:{hidden_present}")
        rows.append(
            {
                "case_id": case_id,
                "attempt_id": attempts[case_id],
                "candidate_visible_files": list(EXPECTED_VISIBLE_FILES),
                "candidate_writable_files": list(EXPECTED_WRITABLE_FILES),
                "hidden_files_forbidden": list(HIDDEN_FORBIDDEN_FILES),
                "problem_sha256": sha256_file(case_root / "problem.md"),
                "raw_solver_trajectory_sha256": sha256_file(
                    case_root / "raw_solver_trajectory.txt"
                ),
                "input_manifest_sha256": sha256_file(case_root / "input-manifest.json"),
                "workspace_materialization_status": "PLANNED_NOT_WRITTEN",
            }
        )
    return rows


def build_preflight_receipt(path: Path = FREEZE_TARGET) -> dict[str, Any]:
    freeze = load_and_validate_freeze(path)
    attempt_plan = derive_attempt_plan(freeze)
    final_root = Path(freeze["output_roots"]["final_root"])
    partial_root = Path(freeze["output_roots"]["partial_root"])
    output_root_status = (
        "CLEAR"
        if not final_root.exists()
        and not final_root.is_symlink()
        and not partial_root.exists()
        and not partial_root.is_symlink()
        else "OCCUPIED_OR_REQUIRES_RECONCILIATION"
    )
    return {
        "schema_version": RECEIPT_SCHEMA_VERSION,
        "poc_id": POC_ID,
        "run_id": RUN_ID,
        "freeze_path": path.relative_to(REPO_ROOT).as_posix()
        if path.is_relative_to(REPO_ROOT)
        else str(path),
        "freeze_sha256": sha256_file(path),
        "case_count": len(attempt_plan),
        "attempt_count": len({row["attempt_id"] for row in attempt_plan}),
        "attempt_plan": attempt_plan,
        "workspace_plan_verdict": "PASS",
        "hidden_public_split_verdict": "PASS",
        "output_root_status": output_root_status,
        "live_authorization_status": "NOT_AUTHORIZED",
        "overall_status": "READY_FOR_AUTHORIZATION",
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "database_connections": 0,
            "redis_connections": 0,
            "solver_calls": 0,
            "network_calls": 0,
            "subagent_calls": 0,
        },
        "explicit_nonclaims": [
            "does_not_authorize_live_execution",
            "does_not_start_devin_session",
            "does_not_observe_effective_model",
            "does_not_grade_candidates",
            "does_not_complete_blind_review",
            "does_not_qualify_event_extractor_profile",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze", type=Path, default=FREEZE_TARGET)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="reserved for a future explicitly authorized live run; currently fails closed",
    )
    args = parser.parse_args()
    if args.execute:
        raise VMS41R1RunnerError(
            "LIVE_NOT_AUTHORIZED",
            "VMS-41R1 live execution requires a future explicit permit",
        )
    receipt = build_preflight_receipt(args.freeze)
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, VMS41R1RunnerError) as exc:
        print(f"VMS41R1_RUNNER_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
