"""Read-only integrity and mechanical replay verifier for POC-VMS-41.

This verifier never writes the sealed live bundle.  It recomputes its complete
artifact tree, freeze bindings, four candidate evaluations, tool/file audits,
and aggregate status.  A clean result deliberately remains
``PENDING_MANUAL_AUDIT``; semantic fidelity and final role qualification are
decided only in a separate append-only audit bundle.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.event_extraction_qualification import (
    EventExtractionAcceptableSetPack,
    OverallQualificationStatus,
    evaluate_candidate_json,
)
from system.solve_vein_analysis.role_runtime import sha256_file
from system.tests.solve_vein_analysis.run_event_extractor_qualification import (
    DEFAULT_FINAL_ROOT,
    DEFAULT_FREEZE,
    EXPECTED_CASE_IDS,
    QualificationRunError,
    _invocation_protocol_errors,
    audit_tool_boundary,
    validate_freeze_manifest,
    verify_attempt_file_set,
)


def _load_object(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        errors.append(f"{label} is absent, unsafe, or not a file")
        return {}
    try:
        value = json.loads(path.read_text(), parse_constant=_reject_nonfinite)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        errors.append(f"{label} is invalid JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return {}
    return value


def _reject_nonfinite(value: str) -> Any:
    raise ValueError(f"non-finite JSON number: {value}")


def _artifact_tree(bundle: Path, errors: list[str]) -> tuple[list[dict[str, Any]], str]:
    rows: list[dict[str, Any]] = []
    for path in sorted(bundle.rglob("*")):
        if path.is_symlink():
            errors.append(f"symlink artifact: {path.relative_to(bundle)}")
            continue
        if path.is_file() and path.name not in {"final-receipt.json", "COMMITTED"}:
            rows.append(
                {
                    "path": path.relative_to(bundle).as_posix(),
                    "size_bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    payload = "".join(
        f"{row['sha256']}  {row['path']}\n" for row in rows
    ).encode("utf-8")
    return rows, hashlib.sha256(payload).hexdigest()


def verify_live_bundle(
    bundle: Path = DEFAULT_FINAL_ROOT,
    freeze_path: Path = DEFAULT_FREEZE,
) -> dict[str, Any]:
    errors: list[str] = []
    if bundle.is_symlink() or not bundle.is_dir():
        return _result(["live bundle is absent, unsafe, or not a directory"])
    try:
        freeze = validate_freeze_manifest(freeze_path)
    except (QualificationRunError, OSError) as exc:
        return _result([f"freeze validation failed: {exc}"])
    receipt = _load_object(bundle / "final-receipt.json", errors, "final receipt")
    aggregate = _load_object(bundle / "live-aggregate.json", errors, "live aggregate")
    copied_freeze = bundle / "preexecution-freeze-manifest.json"
    if (
        copied_freeze.is_symlink()
        or not copied_freeze.is_file()
        or sha256_file(copied_freeze) != sha256_file(freeze_path)
    ):
        errors.append("sealed freeze copy mismatch")
    actual_rows, actual_tree_hash = _artifact_tree(bundle, errors)
    if receipt.get("artifacts") != actual_rows:
        errors.append("final receipt artifact inventory mismatch")
    if receipt.get("artifact_tree_sha256") != actual_tree_hash:
        errors.append("final receipt artifact tree mismatch")
    if receipt.get("freeze_manifest_sha256") != sha256_file(freeze_path):
        errors.append("final receipt freeze hash mismatch")
    expected_marker = (
        "final-receipt.json SHA256="
        + sha256_file(bundle / "final-receipt.json")
        + "\n"
        if (bundle / "final-receipt.json").is_file()
        else ""
    )
    marker = bundle / "COMMITTED"
    if marker.is_symlink() or not marker.is_file() or marker.read_text() != expected_marker:
        errors.append("COMMITTED marker mismatch")

    acceptable_binding = freeze["acceptable_set_pack"]
    try:
        acceptable_pack = EventExtractionAcceptableSetPack.from_json_text(
            (REPO_ROOT / acceptable_binding["path"]).read_text()
        )
    except Exception as exc:  # fail closed at the verifier boundary
        return _result(errors + [f"acceptable set cannot be loaded: {exc}"])

    recomputed_case_rows: list[dict[str, str]] = []
    terminal_case_ids: list[str] = []
    for case_id in EXPECTED_CASE_IDS:
        attempt_id = freeze["attempt_ids"][case_id]
        attempt = bundle / "attempts" / attempt_id
        evaluation_path = bundle / "evaluations" / f"{case_id}.json"
        stored = _load_object(evaluation_path, errors, f"evaluation {case_id}")
        invocation = _load_object(
            attempt / "invocation-receipt.json", errors, f"invocation {case_id}"
        )
        if attempt.is_dir() and not attempt.is_symlink():
            terminal_case_ids.append(case_id)
        candidate_path = attempt / "reasoning-trajectory.json"
        raw_path = attempt / "raw_solver_trajectory.txt"
        if candidate_path.is_symlink() or not candidate_path.is_file():
            errors.append(f"candidate is missing or unsafe: {case_id}")
            continue
        if raw_path.is_symlink() or not raw_path.is_file():
            errors.append(f"raw source is missing or unsafe: {case_id}")
            continue
        acceptable = acceptable_pack.case_by_id(case_id)
        evaluation = evaluate_candidate_json(
            candidate_path.read_text(), acceptable, raw_path.read_bytes()
        )
        tool_audit = audit_tool_boundary(
            attempt / "devin-export.json",
            attempt,
            attempt_id,
            historical_attempt_bundle=(
                bundle.parent
                / f".{bundle.name}.partial"
                / "attempts"
                / attempt_id
            ),
        )
        file_set_audit = verify_attempt_file_set(attempt)
        protocol_errors = _invocation_protocol_errors(invocation, freeze)
        if tool_audit["verdict"] != "PASS":
            protocol_errors.append("tool boundary audit did not PASS")
        if file_set_audit["verdict"] != "PASS":
            protocol_errors.append("attempt file set audit did not PASS")
        case_status = (
            "INCONCLUSIVE_PROTOCOL"
            if protocol_errors
            else "PENDING_MANUAL_AUDIT"
            if evaluation.overall_status
            is OverallQualificationStatus.PENDING_MANUAL_AUDIT
            else "FAIL"
        )
        if stored.get("attempt_id") != attempt_id:
            errors.append(f"stored attempt identity mismatch: {case_id}")
        if stored.get("invocation_receipt_sha256") != sha256_file(
            attempt / "invocation-receipt.json"
        ):
            errors.append(f"stored invocation hash mismatch: {case_id}")
        if stored.get("mechanical_evaluation") != evaluation.to_dict():
            errors.append(f"mechanical evaluation replay mismatch: {case_id}")
        if stored.get("tool_boundary_audit") != tool_audit:
            errors.append(f"tool audit replay mismatch: {case_id}")
        if stored.get("attempt_file_set_audit") != file_set_audit:
            errors.append(f"file-set audit replay mismatch: {case_id}")
        if stored.get("protocol_errors") != protocol_errors:
            errors.append(f"protocol error replay mismatch: {case_id}")
        if stored.get("manual_semantic_audit") != "PENDING":
            errors.append(f"live bundle contains a premature manual verdict: {case_id}")
        if stored.get("case_status") != case_status:
            errors.append(f"case status replay mismatch: {case_id}")
        recomputed_case_rows.append(
            {
                "case_id": case_id,
                "attempt_id": attempt_id,
                "case_status": case_status,
                "mechanical_scientific_verdict": (
                    evaluation.mechanical_scientific_verdict.value
                ),
            }
        )

    expected_status = (
        "INCONCLUSIVE_PROTOCOL"
        if tuple(terminal_case_ids) != EXPECTED_CASE_IDS
        or any(
            row["case_status"] == "INCONCLUSIVE_PROTOCOL"
            for row in recomputed_case_rows
        )
        else "PENDING_MANUAL_AUDIT"
        if all(
            row["case_status"] == "PENDING_MANUAL_AUDIT"
            for row in recomputed_case_rows
        )
        else "FAIL"
    )
    if aggregate.get("terminal_case_ids") != terminal_case_ids:
        errors.append("aggregate terminal case set mismatch")
    if aggregate.get("case_results") != recomputed_case_rows:
        errors.append("aggregate case projection mismatch")
    if aggregate.get("overall_status") != expected_status:
        errors.append("aggregate overall status mismatch")
    if aggregate.get("component_qualification") != "NOT_YET_DECIDABLE":
        errors.append("live aggregate prematurely decides component qualification")
    if aggregate.get("manual_semantic_audit") != (
        "PENDING" if tuple(terminal_case_ids) == EXPECTED_CASE_IDS else "NOT_REACHED"
    ):
        errors.append("aggregate manual-audit state mismatch")
    if receipt.get("artifact_integrity") != "PASS":
        errors.append("final receipt does not preserve artifact integrity PASS")
    if receipt.get("live_attempt_status") != expected_status:
        errors.append("final receipt live status mismatch")
    if receipt.get("manual_semantic_audit") != "PENDING":
        errors.append("final receipt manual audit must remain pending")
    if receipt.get("component_qualification") != "NOT_YET_DECIDABLE":
        errors.append("final receipt prematurely qualifies the component")
    return _result(errors, expected_status=expected_status)


def _result(
    errors: list[str], *, expected_status: str = "NOT_EVALUATED"
) -> dict[str, Any]:
    return {
        "schema_version": "solve-vein/vms41-read-only-verification/v1",
        "artifact_integrity": "PASS" if not errors else "FAIL",
        "mechanical_replay": "PASS" if not errors else "FAIL",
        "live_attempt_status": expected_status,
        "manual_semantic_audit": "PENDING" if not errors else "NOT_DECIDABLE",
        "component_qualification": "NOT_YET_DECIDABLE",
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_FINAL_ROOT)
    parser.add_argument("--freeze", type=Path, default=DEFAULT_FREEZE)
    args = parser.parse_args()
    result = verify_live_bundle(args.bundle, args.freeze)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if result["artifact_integrity"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
