"""VMS-42 State Normalizer sealed reviewer judgment contract.

This contract validates the object a future blind reviewer would seal after
looking only at the public VMS-42 manifest and a candidate bundle.  It does not
perform the review, does not run the hidden join, and does not read hidden
dictionaries, acceptable sets, reference candidates or mechanical evaluations.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.tests.solve_vein_analysis import build_vms42_state_normalizer_pack as pack_builder
from system.tests.solve_vein_analysis import vms42_state_normalizer_hidden_join as hidden_join


SCHEMA_VERSION = "solve-vein/vms42-state-normalizer-sealed-reviewer-judgment/v1"
CONTRACT_SUMMARY_SCHEMA_VERSION = "solve-vein/vms42-state-normalizer-reviewer-judgment-contract/v1"
VALID_AXIS_VERDICTS = {"PASS", "FAIL", "INCONCLUSIVE"}
VALID_FINAL_VERDICTS = {"MANUAL_PASS", "MANUAL_FAIL", "MANUAL_INCONCLUSIVE"}
REQUIRED_AXES = (
    "candidate_bundle_integrity",
    "public_manifest_alignment",
    "occurrence_set_fidelity",
    "required_axis_coverage_fidelity",
    "raw_axis_claim_source_fidelity",
    "no_hidden_gold_in_candidate",
)
REQUIRED_NONCLAIMS = {
    "does_not_run_hidden_join",
    "does_not_reveal_dictionary_or_acceptable_set",
    "does_not_qualify_profile_without_hidden_join",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class VMS42ManualJudgmentError(RuntimeError):
    """Fail-closed manual/reviewer judgment validation error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def expected_candidate_rows(candidate_bundle: Mapping[str, Any]) -> list[dict[str, str]]:
    bundle = _candidate_bundle(candidate_bundle)
    rows = [
        {
            "case_id": candidate["case_id"],
            "candidate_id": candidate["candidate_id"],
            "candidate_input_sha256": candidate["candidate_input_sha256"],
        }
        for candidate in bundle["candidates"]
    ]
    return sorted(rows, key=lambda row: (row["case_id"], row["candidate_id"]))


def build_synthetic_reviewer_judgment(
    candidate_bundle: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a valid development-only sealed judgment fixture."""

    bundle = candidate_bundle if candidate_bundle is not None else hidden_join.build_reference_candidate_bundle()
    bundle = _candidate_bundle(bundle)
    return {
        "schema_version": SCHEMA_VERSION,
        "review_id": "vms42-reviewer-judgment-fixture-001",
        "pack_id": pack_builder.PACK_ID,
        "public_manifest_sha256": bundle["public_manifest_sha256"],
        "candidate_bundle_sha256": sha256_json(bundle),
        "reviewed_candidates": expected_candidate_rows(bundle),
        "reviewer_blinding_attestation": {
            "reviewer_view_only": True,
            "dictionary_seen": False,
            "acceptable_set_seen": False,
            "reference_candidates_seen": False,
            "hidden_join_result_seen": False,
        },
        "axis_verdicts": {axis: "PASS" for axis in REQUIRED_AXES},
        "final_manual_verdict": "MANUAL_PASS",
        "reviewer_notes": "Synthetic contract fixture; not a real reviewer judgment.",
        "sealed_status": "SEALED_REVIEWER_JUDGMENT",
        "explicit_nonclaims": sorted(REQUIRED_NONCLAIMS),
    }


def validate_manual_judgment(
    value: Mapping[str, Any],
    *,
    candidate_bundle: Mapping[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []
    expected_keys = {
        "schema_version",
        "review_id",
        "pack_id",
        "public_manifest_sha256",
        "candidate_bundle_sha256",
        "reviewed_candidates",
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
        "vms42-reviewer-judgment-"
    ):
        errors.append("review_id_invalid")
    if value["pack_id"] != pack_builder.PACK_ID:
        errors.append("pack_id_mismatch")
    if not isinstance(value["public_manifest_sha256"], str) or not SHA256_RE.fullmatch(
        value["public_manifest_sha256"]
    ):
        errors.append("public_manifest_sha256_invalid")
    if not isinstance(value["candidate_bundle_sha256"], str) or not SHA256_RE.fullmatch(
        value["candidate_bundle_sha256"]
    ):
        errors.append("candidate_bundle_sha256_invalid")

    if candidate_bundle is not None:
        bundle = _candidate_bundle(candidate_bundle)
        if value["candidate_bundle_sha256"] != sha256_json(bundle):
            errors.append("candidate_bundle_sha256_mismatch")
        if value["public_manifest_sha256"] != bundle["public_manifest_sha256"]:
            errors.append("public_manifest_sha256_mismatch")
        if value["reviewed_candidates"] != expected_candidate_rows(bundle):
            errors.append("reviewed_candidates_mismatch")

    attestation = value["reviewer_blinding_attestation"]
    expected_attestation = {
        "reviewer_view_only": True,
        "dictionary_seen": False,
        "acceptable_set_seen": False,
        "reference_candidates_seen": False,
        "hidden_join_result_seen": False,
    }
    if not isinstance(attestation, dict) or attestation != expected_attestation:
        errors.append("reviewer_blinding_attestation_invalid")

    reviewed = value["reviewed_candidates"]
    if not isinstance(reviewed, list) or not reviewed:
        errors.append("reviewed_candidates_invalid")
    else:
        seen: set[tuple[str, str]] = set()
        for index, row in enumerate(reviewed):
            if not isinstance(row, dict) or set(row) != {"case_id", "candidate_id", "candidate_input_sha256"}:
                errors.append(f"reviewed_candidate_keys_invalid:{index}")
                continue
            pair = (row["case_id"], row["candidate_id"])
            if pair in seen:
                errors.append(f"reviewed_candidate_duplicate:{pair}")
            seen.add(pair)
            if not isinstance(row["candidate_input_sha256"], str) or not SHA256_RE.fullmatch(
                row["candidate_input_sha256"]
            ):
                errors.append(f"reviewed_candidate_sha_invalid:{index}")

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
    if value["sealed_status"] != "SEALED_REVIEWER_JUDGMENT":
        errors.append("sealed_status_invalid")
    nonclaims = value["explicit_nonclaims"]
    if not isinstance(nonclaims, list) or not REQUIRED_NONCLAIMS.issubset(set(nonclaims)):
        errors.append("explicit_nonclaims_missing")
    return errors


def build_contract_summary() -> dict[str, Any]:
    return {
        "schema_version": CONTRACT_SUMMARY_SCHEMA_VERSION,
        "judgment_schema_version": SCHEMA_VERSION,
        "pack_id": pack_builder.PACK_ID,
        "candidate_bundle_schema_version": hidden_join.CANDIDATE_BUNDLE_SCHEMA_VERSION,
        "public_manifest_sha256": "NOT_COMPUTED_BY_CONTRACT_SUMMARY",
        "reference_candidate_bundle_sha256": "NOT_COMPUTED_BY_CONTRACT_SUMMARY",
        "required_axes": list(REQUIRED_AXES),
        "valid_axis_verdicts": sorted(VALID_AXIS_VERDICTS),
        "valid_final_verdicts": sorted(VALID_FINAL_VERDICTS),
        "required_nonclaims": sorted(REQUIRED_NONCLAIMS),
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "hidden_join_calls": 0,
            "hidden_dictionary_reads": 0,
            "hidden_acceptable_set_reads": 0,
            "database_connections": 0,
            "solver_calls": 0,
            "files_written": 0,
        },
        "explicit_nonclaims": [
            "does_not_perform_reviewer_judgment",
            "does_not_import_real_model_output",
            "does_not_run_hidden_join",
            "does_not_qualify_state_extractor_profile",
        ],
    }


def assert_no_forbidden_imports(path: Path) -> tuple[str, ...]:
    tree = ast.parse(path.read_text())
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".")[0])
    forbidden = roots & {"arango", "requests", "socket", "subprocess", "urllib"}
    if forbidden:
        raise VMS42ManualJudgmentError("FORBIDDEN_IMPORT", ",".join(sorted(forbidden)))
    return tuple(sorted(roots))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", type=Path, help="validate a sealed reviewer judgment JSON")
    parser.add_argument("--candidate-bundle", type=Path, help="optional candidate bundle JSON for stronger validation")
    args = parser.parse_args()
    if args.validate:
        value = json.loads(args.validate.read_text())
        if not isinstance(value, dict):
            print("REVIEWER_JUDGMENT_ERROR: JSON_NOT_OBJECT", file=sys.stderr)
            return 2
        candidate_bundle = None
        if args.candidate_bundle:
            loaded = json.loads(args.candidate_bundle.read_text())
            if not isinstance(loaded, dict):
                print("REVIEWER_JUDGMENT_ERROR: CANDIDATE_BUNDLE_NOT_OBJECT", file=sys.stderr)
                return 2
            candidate_bundle = loaded
        errors = validate_manual_judgment(value, candidate_bundle=candidate_bundle)
        if errors:
            print("REVIEWER_JUDGMENT_ERROR: " + ";".join(errors), file=sys.stderr)
            return 2
        print(json.dumps({"verdict": "PASS", "schema_version": SCHEMA_VERSION}, sort_keys=True))
        return 0
    print(json.dumps(build_contract_summary(), ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _candidate_bundle(value: Mapping[str, Any]) -> Mapping[str, Any]:
    hidden_join._candidate_bundle(value)  # noqa: SLF001 - shared fail-closed bundle validator
    return value


if __name__ == "__main__":
    raise SystemExit(main())
