"""VMS-41R1 sealed manual judgment contract.

The functions in this module validate the future blind manual-review judgment
object.  They do not perform a review, do not access hidden acceptable sets, and
do not run the mechanical grader.  The contract is intentionally strict so that
a future sealed manual judgment can be joined with hidden references only after
the reviewer-visible package has been sealed.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.tests.solve_vein_analysis.build_vms41r1_live_permit_review_plan import (
    build_plan,
)


SCHEMA_VERSION = "solve-vein/vms41r1-sealed-manual-judgment/v1"
VALID_AXIS_VERDICTS = {"PASS", "FAIL", "INCONCLUSIVE"}
VALID_FINAL_VERDICTS = {"MANUAL_PASS", "MANUAL_FAIL", "MANUAL_INCONCLUSIVE"}
REQUIRED_AXES = (
    "occurrence_fidelity",
    "source_span_fidelity",
    "typed_relation_fidelity",
    "temporal_status_fidelity",
    "merge_contribution_fidelity",
    "file_boundary_cleanliness",
)
REQUIRED_NONCLAIMS = {
    "does_not_run_mechanical_hidden_grader",
    "does_not_reveal_hidden_acceptable_set",
    "does_not_qualify_profile_without_hidden_join",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def expected_attempt_map() -> dict[str, str]:
    receipt = build_plan()
    return {
        row["case_id"]: row["attempt_id"]
        for row in receipt["blind_review_plan"]["case_plans"]
    }


def validate_manual_judgment(
    value: Mapping[str, Any],
    *,
    attempt_map: Mapping[str, str] | None = None,
) -> list[str]:
    errors: list[str] = []
    expected_keys = {
        "schema_version",
        "review_id",
        "case_id",
        "attempt_id",
        "blinded_package_sha256",
        "reviewer_blinding_attestation",
        "axis_verdicts",
        "final_manual_verdict",
        "reviewer_notes",
        "sealed_status",
        "explicit_nonclaims",
    }
    actual_keys = set(value)
    if actual_keys != expected_keys:
        errors.append(
            f"keys_mismatch missing={sorted(expected_keys - actual_keys)} unknown={sorted(actual_keys - expected_keys)}"
        )
        return errors

    if value["schema_version"] != SCHEMA_VERSION:
        errors.append("schema_version_mismatch")
    if not isinstance(value["review_id"], str) or not value["review_id"].startswith(
        "vms41r1-manual-review-"
    ):
        errors.append("review_id_invalid")
    case_id = value["case_id"]
    attempt_id = value["attempt_id"]
    if attempt_map is None:
        attempt_map = expected_attempt_map()
    if not isinstance(case_id, str) or case_id not in attempt_map:
        errors.append("case_id_unknown")
    elif attempt_id != attempt_map[case_id]:
        errors.append("attempt_id_mismatch")
    if not isinstance(attempt_id, str):
        errors.append("attempt_id_invalid")
    if not isinstance(value["blinded_package_sha256"], str) or not SHA256_RE.fullmatch(
        value["blinded_package_sha256"]
    ):
        errors.append("blinded_package_sha256_invalid")

    attestation = value["reviewer_blinding_attestation"]
    expected_attestation = {
        "reviewer_view_only": True,
        "hidden_acceptable_set_seen": False,
        "reference_candidate_seen": False,
        "mechanical_grader_result_seen": False,
    }
    if not isinstance(attestation, dict) or attestation != expected_attestation:
        errors.append("reviewer_blinding_attestation_invalid")

    axes = value["axis_verdicts"]
    if not isinstance(axes, dict):
        errors.append("axis_verdicts_not_object")
    else:
        axis_keys = set(axes)
        if axis_keys != set(REQUIRED_AXES):
            errors.append(
                f"axis_keys_mismatch missing={sorted(set(REQUIRED_AXES) - axis_keys)} unknown={sorted(axis_keys - set(REQUIRED_AXES))}"
            )
        for axis, verdict in axes.items():
            if verdict not in VALID_AXIS_VERDICTS:
                errors.append(f"axis_verdict_invalid:{axis}")

    final = value["final_manual_verdict"]
    if final not in VALID_FINAL_VERDICTS:
        errors.append("final_manual_verdict_invalid")
    if isinstance(axes, dict):
        if final == "MANUAL_PASS" and any(verdict != "PASS" for verdict in axes.values()):
            errors.append("manual_pass_requires_all_axes_pass")
        if final == "MANUAL_FAIL" and not any(verdict == "FAIL" for verdict in axes.values()):
            errors.append("manual_fail_requires_at_least_one_axis_fail")

    if not isinstance(value["reviewer_notes"], str):
        errors.append("reviewer_notes_not_string")
    if value["sealed_status"] != "SEALED_MANUAL_JUDGMENT":
        errors.append("sealed_status_invalid")
    nonclaims = value["explicit_nonclaims"]
    if not isinstance(nonclaims, list) or not REQUIRED_NONCLAIMS.issubset(set(nonclaims)):
        errors.append("explicit_nonclaims_missing")
    return errors


def build_contract_summary() -> dict[str, Any]:
    attempt_map = expected_attempt_map()
    return {
        "schema_version": "solve-vein/vms41r1-manual-judgment-contract/v1",
        "judgment_schema_version": SCHEMA_VERSION,
        "case_count": len(attempt_map),
        "case_attempt_map": dict(sorted(attempt_map.items())),
        "required_axes": list(REQUIRED_AXES),
        "valid_axis_verdicts": sorted(VALID_AXIS_VERDICTS),
        "valid_final_verdicts": sorted(VALID_FINAL_VERDICTS),
        "required_nonclaims": sorted(REQUIRED_NONCLAIMS),
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "mechanical_hidden_grader_calls": 0,
            "hidden_acceptable_set_reads": 0,
            "database_connections": 0,
            "solver_calls": 0,
        },
        "explicit_nonclaims": [
            "does_not_perform_manual_review",
            "does_not_import_real_judgment",
            "does_not_run_mechanical_hidden_grader",
            "does_not_qualify_event_extractor_profile",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", type=Path, help="validate a sealed manual judgment JSON")
    args = parser.parse_args()
    if args.validate:
        value = json.loads(args.validate.read_text())
        if not isinstance(value, dict):
            print("MANUAL_JUDGMENT_ERROR: JSON_NOT_OBJECT", file=sys.stderr)
            return 2
        errors = validate_manual_judgment(value)
        if errors:
            print("MANUAL_JUDGMENT_ERROR: " + ";".join(errors), file=sys.stderr)
            return 2
        print(json.dumps({"verdict": "PASS", "schema_version": SCHEMA_VERSION}, sort_keys=True))
        return 0
    print(json.dumps(build_contract_summary(), ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
