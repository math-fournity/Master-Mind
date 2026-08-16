"""Development-only hidden-join simulator for VMS-41R1.

This simulator joins synthetic sealed manual judgments with hidden mechanical
evaluation using the frozen VMS-41R1 reference candidates as fake candidate
outputs.  It is deliberately not a live runner and not a profile qualification
result.  Its purpose is to prove the ordering and join semantics before any real
Devin attempt exists.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.event_extraction_projection import (
    EventExtractionAcceptableSetPackV2,
    evaluate_candidate_json_v2,
)
from system.tests.solve_vein_analysis.build_vms41r1_qualification_pack import (
    CASE_ORDER,
    FIXTURE_ROOT,
    apply_pointer_mutation,
)
from system.tests.solve_vein_analysis.vms41r1_manual_judgment_contract import (
    REQUIRED_AXES,
    REQUIRED_NONCLAIMS,
    SCHEMA_VERSION as MANUAL_JUDGMENT_SCHEMA_VERSION,
    validate_manual_judgment,
)


SCHEMA_VERSION = "solve-vein/vms41r1-hidden-join-simulator/v1"


class VMS41R1HiddenJoinError(RuntimeError):
    """Fail-closed hidden-join simulation error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def _load_json(path: Path) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise VMS41R1HiddenJoinError("UNSAFE_JSON", str(path))
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise VMS41R1HiddenJoinError("JSON_NOT_OBJECT", str(path))
    return value


def _candidate_text(value: Mapping[str, Any]) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def _fake_manual_judgment(case_id: str, attempt_id: str) -> dict[str, Any]:
    blinded_hash = hashlib.sha256(f"fake-blinded-package:{case_id}:{attempt_id}".encode()).hexdigest()
    return {
        "schema_version": MANUAL_JUDGMENT_SCHEMA_VERSION,
        "review_id": f"vms41r1-manual-review-fake-{case_id.lower()}",
        "case_id": case_id,
        "attempt_id": attempt_id,
        "blinded_package_sha256": blinded_hash,
        "reviewer_blinding_attestation": {
            "reviewer_view_only": True,
            "hidden_acceptable_set_seen": False,
            "reference_candidate_seen": False,
            "mechanical_grader_result_seen": False,
        },
        "axis_verdicts": {axis: "PASS" for axis in REQUIRED_AXES},
        "final_manual_verdict": "MANUAL_PASS",
        "reviewer_notes": "Synthetic sealed judgment for hidden-join simulator only.",
        "sealed_status": "SEALED_MANUAL_JUDGMENT",
        "explicit_nonclaims": sorted(REQUIRED_NONCLAIMS),
    }


def simulate_hidden_join(
    *,
    candidate_overrides: Mapping[str, Mapping[str, Any]] | None = None,
    manual_judgment_overrides: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    acceptable_pack = _load_json(FIXTURE_ROOT / "acceptable-sets.json")
    reference_candidates = _load_json(FIXTURE_ROOT / "reference-candidates.json")
    manifest = _load_json(FIXTURE_ROOT / "pack-manifest.json")
    pack = EventExtractionAcceptableSetPackV2.from_dict(acceptable_pack)
    case_by_id = {case.case_id: case for case in pack.cases}
    attempt_map = manifest["attempt_ids"]
    if set(attempt_map) != set(CASE_ORDER):
        raise VMS41R1HiddenJoinError("ATTEMPT_MAP_INVALID", str(attempt_map))

    candidates = dict(reference_candidates["candidates"])
    if candidate_overrides:
        candidates.update(candidate_overrides)

    rows: list[dict[str, Any]] = []
    for case_id in CASE_ORDER:
        attempt_id = attempt_map[case_id]
        manual = (
            dict(manual_judgment_overrides[case_id])
            if manual_judgment_overrides and case_id in manual_judgment_overrides
            else _fake_manual_judgment(case_id, attempt_id)
        )
        manual_errors = validate_manual_judgment(manual, attempt_map=attempt_map)
        if manual_errors:
            raise VMS41R1HiddenJoinError(
                "MANUAL_JUDGMENT_INVALID_BEFORE_HIDDEN_JOIN",
                f"{case_id}:{manual_errors}",
            )

        candidate = candidates[case_id]
        source = (FIXTURE_ROOT / case_id / "raw_solver_trajectory.txt").read_bytes()
        text = _candidate_text(candidate)
        evaluation = evaluate_candidate_json_v2(text, case_by_id[case_id], source)
        mechanical = evaluation.mechanical_scientific_verdict.value
        manual_verdict = manual["final_manual_verdict"]
        joined = (
            "JOIN_PASS_DEVELOPMENT_ONLY"
            if manual_verdict == "MANUAL_PASS"
            and evaluation.overall_status.value == "PENDING_BLIND_MANUAL_AUDIT"
            and mechanical == "PASS"
            else "JOIN_FAIL_OR_INCONCLUSIVE_DEVELOPMENT_ONLY"
        )
        rows.append(
            {
                "case_id": case_id,
                "attempt_id": attempt_id,
                "manual_judgment_validated_before_hidden_eval": True,
                "manual_verdict": manual_verdict,
                "mechanical_overall_status": evaluation.overall_status.value,
                "mechanical_scientific_verdict": mechanical,
                "candidate_sha256": hashlib.sha256(text.encode()).hexdigest(),
                "join_verdict": joined,
            }
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "simulator_status": "DEVELOPMENT_ONLY",
        "case_count": len(rows),
        "join_rows": rows,
        "overall_join_verdict": (
            "PASS_DEVELOPMENT_SIMULATION_ONLY"
            if all(row["join_verdict"] == "JOIN_PASS_DEVELOPMENT_ONLY" for row in rows)
            else "FAIL_OR_INCONCLUSIVE_DEVELOPMENT_SIMULATION_ONLY"
        ),
        "side_effects": {
            "model_calls": 0,
            "devin_sessions": 0,
            "manual_review_imports": 0,
            "database_connections": 0,
            "solver_calls": 0,
        },
        "explicit_nonclaims": [
            "does_not_use_real_candidate_output",
            "does_not_import_real_manual_review",
            "does_not_authorize_live_execution",
            "does_not_qualify_event_extractor_profile",
        ],
    }


def mutated_reference_candidate(case_id: str, check_index: int = 0) -> dict[str, Any]:
    reference_candidates = _load_json(FIXTURE_ROOT / "reference-candidates.json")
    checks = _load_json(FIXTURE_ROOT / "negative-checks.json")
    matching = [check for check in checks["checks"] if check["case_id"] == case_id]
    if not matching:
        raise VMS41R1HiddenJoinError("NO_NEGATIVE_CHECK_FOR_CASE", case_id)
    check = matching[check_index]
    return apply_pointer_mutation(reference_candidates["candidates"][case_id], check["mutation"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print(json.dumps(simulate_hidden_join(), ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, VMS41R1HiddenJoinError) as exc:
        print(f"VMS41R1_HIDDEN_JOIN_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
