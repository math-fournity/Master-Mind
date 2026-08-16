"""Build the zero-model VMS-41R1 LiveRunPermit and blind-review plan.

This command does not create a consumable live permit.  It reads the frozen
VMS-41R1 preexecution manifest and the runner-shell preflight plan, then emits a
deterministic plan that says exactly what a future human-signed permit and blind
review package must bind.

No Devin session, model call, Solver call, DB/Redis connection, network call, or
workspace materialization is performed here.
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

from system.solve_vein_analysis.models import canonical_json_bytes
from system.tests.solve_vein_analysis.run_vms41r1_event_extractor_qualification import (
    FREEZE_TARGET,
    HIDDEN_FORBIDDEN_FILES,
    POC_ID,
    RUN_ID,
    VMS41R1RunnerError,
    build_preflight_receipt,
    sha256_file,
)


SCHEMA_VERSION = "solve-vein/vms41r1-live-permit-review-plan/v1"
PROTOCOL_PATH = (
    REPO_ROOT
    / "第六代系统研发过程文档"
    / "374-v0-2026-08-14-POC-VMS-41R1-LiveRunPermit与盲审包计划-零模型冻结.md"
)


class VMS41R1PlanError(RuntimeError):
    """Fail-closed plan builder error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def _case_plan(attempt: Mapping[str, Any]) -> dict[str, Any]:
    case_id = attempt.get("case_id")
    attempt_id = attempt.get("attempt_id")
    if not isinstance(case_id, str) or not isinstance(attempt_id, str):
        raise VMS41R1PlanError("ATTEMPT_PLAN_INVALID", str(attempt))
    forbidden = set(HIDDEN_FORBIDDEN_FILES)
    reviewer_visible = [
        "problem.md",
        "raw_solver_trajectory.txt",
        "reasoning-trajectory-candidate-v2.json",
        "DONE.md",
        "candidate-output-manifest.json",
    ]
    if forbidden.intersection(reviewer_visible):
        raise VMS41R1PlanError("HIDDEN_FILE_VISIBLE", f"{case_id}:{sorted(forbidden)}")
    return {
        "case_id": case_id,
        "attempt_id": attempt_id,
        "future_live_workspace_status": "NOT_MATERIALIZED_IN_THIS_PLAN",
        "future_candidate_outputs_required": [
            "reasoning-trajectory-candidate-v2.json",
            "DONE.md",
        ],
        "blind_review_visible_files_after_live": reviewer_visible,
        "blind_review_forbidden_files": sorted(forbidden),
        "manual_judgment_required_before_hidden_join": True,
        "mechanical_grading_before_manual_seal": "FORBIDDEN",
    }


def build_plan(freeze: Path = FREEZE_TARGET) -> dict[str, Any]:
    preflight = build_preflight_receipt(freeze)
    if preflight["overall_status"] != "READY_FOR_AUTHORIZATION":
        raise VMS41R1PlanError("PREFLIGHT_NOT_READY", str(preflight["overall_status"]))
    if preflight["live_authorization_status"] != "NOT_AUTHORIZED":
        raise VMS41R1PlanError(
            "PREFLIGHT_ALREADY_AUTHORIZED",
            str(preflight["live_authorization_status"]),
        )
    if preflight["output_root_status"] != "CLEAR":
        raise VMS41R1PlanError("OUTPUT_ROOT_NOT_CLEAR", str(preflight["output_root_status"]))
    attempts = preflight["attempt_plan"]
    if not isinstance(attempts, list) or len(attempts) != 6:
        raise VMS41R1PlanError("ATTEMPT_PLAN_COUNT_INVALID", str(len(attempts)))
    case_plans = [_case_plan(row) for row in attempts]
    if len({row["attempt_id"] for row in case_plans}) != len(case_plans):
        raise VMS41R1PlanError("ATTEMPT_IDS_DUPLICATED", "future plan")
    protocol_ref: dict[str, Any]
    if PROTOCOL_PATH.exists() and not PROTOCOL_PATH.is_symlink():
        protocol_ref = {
            "path": PROTOCOL_PATH.relative_to(REPO_ROOT).as_posix(),
            "sha256": sha256_file(PROTOCOL_PATH),
        }
    else:
        protocol_ref = {
            "path": PROTOCOL_PATH.relative_to(REPO_ROOT).as_posix(),
            "sha256": "NOT_YET_WRITTEN",
        }
    return {
        "schema_version": SCHEMA_VERSION,
        "poc_id": POC_ID,
        "run_id": RUN_ID,
        "freeze_path": preflight["freeze_path"],
        "freeze_sha256": preflight["freeze_sha256"],
        "runner_preflight_status": preflight["overall_status"],
        "runner_live_authorization_status": preflight["live_authorization_status"],
        "protocol_ref": protocol_ref,
        "live_run_permit": {
            "permit_status": "DRAFT_NOT_SIGNED",
            "permit_consumable": False,
            "authorized_live_attempts": 0,
            "required_human_authorization_ref": None,
            "required_parent_freeze_sha256": preflight["freeze_sha256"],
            "required_runner_preflight_status": "READY_FOR_AUTHORIZATION",
            "future_template_not_executable": {
                "planned_attempts": len(case_plans),
                "retry_limit": 0,
                "requested_cli_model_arg": "glm-5-2",
                "normalized_effort": "high",
                "fresh_session_required": True,
                "resume_allowed": False,
                "dangerous_permission_mode_required": True,
            },
        },
        "blind_review_plan": {
            "package_status": "PLAN_ONLY_NO_CANDIDATE_OUTPUTS",
            "case_count": len(case_plans),
            "case_plans": case_plans,
            "manual_judgment_schema_status": "NOT_IMPLEMENTED",
            "sealed_manual_judgment_required_before_hidden_join": True,
            "hidden_acceptable_set_access_before_manual_seal": "FORBIDDEN",
            "mechanical_reference_grading_before_manual_seal": "FORBIDDEN",
        },
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "workspace_materializations": 0,
            "database_connections": 0,
            "redis_connections": 0,
            "solver_calls": 0,
            "network_calls": 0,
            "subagent_calls": 0,
        },
        "explicit_nonclaims": [
            "does_not_authorize_live_execution",
            "does_not_create_live_workspace",
            "does_not_create_blind_review_package_from_candidate_outputs",
            "does_not_start_devin_session",
            "does_not_complete_manual_review",
            "does_not_qualify_event_extractor_profile",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze", type=Path, default=FREEZE_TARGET)
    parser.add_argument(
        "--canonical",
        action="store_true",
        help="emit canonical JSON bytes instead of pretty JSON",
    )
    args = parser.parse_args()
    plan = build_plan(args.freeze)
    if args.canonical:
        sys.stdout.buffer.write(canonical_json_bytes(plan))
        sys.stdout.write("\n")
    else:
        print(json.dumps(plan, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, VMS41R1PlanError, VMS41R1RunnerError) as exc:
        print(f"VMS41R1_PLAN_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
