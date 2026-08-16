"""Development-only final qualification join receipt for VMS-41R1.

This module joins the fake live bundle materializer and the hidden-join
simulator into one auditable, zero-model receipt.  It deliberately does not
qualify the Event Extractor profile: the candidate outputs are still hidden
reference candidates, not real Devin outputs, and the manual judgments are still
synthetic fixtures.
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

from system.tests.solve_vein_analysis import vms41r1_fake_live_bundle_materializer
from system.tests.solve_vein_analysis import vms41r1_hidden_join_simulator


SCHEMA_VERSION = "solve-vein/vms41r1-final-qualification-join-receipt/v1"


class VMS41R1FinalJoinReceiptError(RuntimeError):
    """Fail-closed final qualification receipt error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def _side_effect_errors(label: str, side_effects: Any) -> list[str]:
    if not isinstance(side_effects, Mapping):
        return [f"{label}:side_effects_not_object"]
    return [
        f"{label}:side_effect_nonzero:{key}={value}"
        for key, value in sorted(side_effects.items())
        if value != 0
    ]


def _validate_materializer_receipt(receipt: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    if receipt.get("schema_version") != vms41r1_fake_live_bundle_materializer.SCHEMA_VERSION:
        errors.append("materializer:schema_version_mismatch")
    if receipt.get("materializer_status") != "PLAN_ONLY_NO_FILES_WRITTEN":
        errors.append("materializer:status_invalid")
    if receipt.get("hidden_public_split_verdict") != "PASS":
        errors.append("materializer:hidden_public_split_not_pass")
    errors.extend(_side_effect_errors("materializer", receipt.get("side_effects")))
    rows = receipt.get("case_rows")
    if not isinstance(rows, list) or len(rows) != len(vms41r1_fake_live_bundle_materializer.CASE_ORDER):
        errors.append("materializer:case_rows_invalid")
        return errors
    for row in rows:
        if not isinstance(row, Mapping):
            errors.append("materializer:case_row_not_object")
            continue
        if row.get("hidden_files_exposed") != []:
            errors.append(f"materializer:hidden_files_exposed:{row.get('case_id')}")
        if row.get("candidate_output_source") != "HIDDEN_REFERENCE_CANDIDATE_AS_FAKE_LIVE_OUTPUT":
            errors.append(f"materializer:candidate_source_invalid:{row.get('case_id')}")
        visible = row.get("reviewer_visible_files")
        if not isinstance(visible, Mapping) or set(visible) != set(
            vms41r1_fake_live_bundle_materializer.VISIBLE_REVIEW_FILES
        ):
            errors.append(f"materializer:visible_files_invalid:{row.get('case_id')}")
    return errors


def _validate_hidden_join_receipt(receipt: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    if receipt.get("schema_version") != vms41r1_hidden_join_simulator.SCHEMA_VERSION:
        errors.append("hidden_join:schema_version_mismatch")
    if receipt.get("simulator_status") != "DEVELOPMENT_ONLY":
        errors.append("hidden_join:status_invalid")
    errors.extend(_side_effect_errors("hidden_join", receipt.get("side_effects")))
    rows = receipt.get("join_rows")
    if not isinstance(rows, list) or len(rows) != len(vms41r1_fake_live_bundle_materializer.CASE_ORDER):
        errors.append("hidden_join:join_rows_invalid")
        return errors
    for row in rows:
        if not isinstance(row, Mapping):
            errors.append("hidden_join:join_row_not_object")
            continue
        if row.get("manual_judgment_validated_before_hidden_eval") is not True:
            errors.append(f"hidden_join:manual_not_validated_first:{row.get('case_id')}")
    return errors


def assemble_final_qualification_join_receipt(
    *,
    materializer_receipt: Mapping[str, Any],
    hidden_join_receipt: Mapping[str, Any],
) -> dict[str, Any]:
    """Assemble the final development-only receipt from two frozen subreceipts."""

    input_errors = _validate_materializer_receipt(materializer_receipt)
    input_errors.extend(_validate_hidden_join_receipt(hidden_join_receipt))
    if input_errors:
        raise VMS41R1FinalJoinReceiptError(
            "INPUT_RECEIPT_INVALID",
            ";".join(input_errors),
        )

    materializer_rows = {
        row["case_id"]: row
        for row in materializer_receipt["case_rows"]
    }
    hidden_rows = {
        row["case_id"]: row
        for row in hidden_join_receipt["join_rows"]
    }
    if set(materializer_rows) != set(hidden_rows):
        raise VMS41R1FinalJoinReceiptError(
            "CASE_SET_MISMATCH",
            f"materializer={sorted(materializer_rows)} hidden={sorted(hidden_rows)}",
        )

    rows: list[dict[str, Any]] = []
    for case_id in vms41r1_fake_live_bundle_materializer.CASE_ORDER:
        materialized = materializer_rows[case_id]
        joined = hidden_rows[case_id]
        if materialized["attempt_id"] != joined["attempt_id"]:
            raise VMS41R1FinalJoinReceiptError("ATTEMPT_ID_MISMATCH", case_id)
        if materialized["candidate_output_sha256"] != joined["candidate_sha256"]:
            raise VMS41R1FinalJoinReceiptError("CANDIDATE_HASH_MISMATCH", case_id)
        rows.append(
            {
                "case_id": case_id,
                "attempt_id": materialized["attempt_id"],
                "fake_bundle_status": materialized["fake_live_bundle_status"],
                "blind_review_package_status": materialized["blind_review_package_status"],
                "hidden_public_split_verdict": materializer_receipt["hidden_public_split_verdict"],
                "manual_judgment_validated_before_hidden_eval": joined[
                    "manual_judgment_validated_before_hidden_eval"
                ],
                "manual_verdict": joined["manual_verdict"],
                "mechanical_scientific_verdict": joined["mechanical_scientific_verdict"],
                "candidate_sha256": joined["candidate_sha256"],
                "join_verdict": joined["join_verdict"],
            }
        )

    hidden_overall = hidden_join_receipt["overall_join_verdict"]
    final_verdict = (
        "PASS_DEVELOPMENT_SIMULATION_ONLY"
        if hidden_overall == "PASS_DEVELOPMENT_SIMULATION_ONLY"
        else "FAIL_OR_INCONCLUSIVE_DEVELOPMENT_SIMULATION_ONLY"
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "receipt_status": "FINAL_JOIN_RECEIPT_DEVELOPMENT_ONLY",
        "case_count": len(rows),
        "case_rows": rows,
        "materializer_status": materializer_receipt["materializer_status"],
        "hidden_join_overall_verdict": hidden_overall,
        "final_join_verdict": final_verdict,
        "profile_qualification_verdict": "NOT_QUALIFIED_LIVE_NOT_AUTHORIZED",
        "mechanical_status_ceiling": "DEVELOPMENT_ONLY_SYNTHETIC_REFERENCES",
        "side_effects": {
            "files_written": 0,
            "model_calls": 0,
            "devin_sessions": 0,
            "manual_review_imports": 0,
            "database_connections": 0,
            "solver_calls": 0,
        },
        "explicit_nonclaims": [
            "does_not_use_real_devin_output",
            "does_not_import_real_manual_review",
            "does_not_authorize_live_execution",
            "does_not_qualify_event_extractor_profile",
            "does_not_replace_future_hidden_join_with_real_outputs",
        ],
    }


def build_final_qualification_join_receipt(
    *,
    materializer_candidate_overrides: Mapping[str, Mapping[str, Any]] | None = None,
    hidden_join_candidate_overrides: Mapping[str, Mapping[str, Any]] | None = None,
    manual_judgment_overrides: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    materializer_receipt = vms41r1_fake_live_bundle_materializer.build_fake_materialization_plan(
        candidate_overrides=materializer_candidate_overrides
    )
    hidden_join_receipt = vms41r1_hidden_join_simulator.simulate_hidden_join(
        candidate_overrides=hidden_join_candidate_overrides,
        manual_judgment_overrides=manual_judgment_overrides,
    )
    return assemble_final_qualification_join_receipt(
        materializer_receipt=materializer_receipt,
        hidden_join_receipt=hidden_join_receipt,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print(
        json.dumps(
            build_final_qualification_join_receipt(),
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (
        OSError,
        VMS41R1FinalJoinReceiptError,
        vms41r1_hidden_join_simulator.VMS41R1HiddenJoinError,
        vms41r1_fake_live_bundle_materializer.VMS41R1FakeBundleError,
    ) as exc:
        print(f"VMS41R1_FINAL_JOIN_RECEIPT_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
