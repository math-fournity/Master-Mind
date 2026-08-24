"""Seal and verify the non-confirmatory post-hoc audit for POC-VMS-41.

This module was created after the four VMS-41 attempts were sealed.  It is not
part of the frozen candidate, grader, or execution protocol.  Its only purpose
is to bind a disclosed, non-blind failure-localization review to the immutable
live bundle without mutating that bundle or upgrading its scientific verdict.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.role_runtime import sha256_file
from system.solve_vein_analysis.event_extraction_qualification import (
    EventExtractionAcceptableSetPack,
    OverallQualificationStatus,
    evaluate_candidate_json,
)
from system.tests.solve_vein_analysis.run_event_extractor_qualification import (
    DEFAULT_FINAL_ROOT as DEFAULT_LIVE_BUNDLE,
    DEFAULT_FREEZE,
    EXPECTED_CASE_IDS,
    _invocation_protocol_errors,
    audit_tool_boundary,
    qualification_test_source_files,
    verify_attempt_file_set,
)


AUDIT_ID = "poc-vms-41-posthoc-diagnostic-audit-20260814"
DEFAULT_REVIEW = (
    Path(__file__).resolve().parent
    / "posthoc_audits"
    / "vms41-manual-diagnostic.json"
)
APPROVED_VOLUME = Path("/data")
APPROVED_RESULTS_ROOT = (
    APPROVED_VOLUME / "master-mind-solve-vein-data" / "poc-results"
)
DEFAULT_FINAL_ROOT = APPROVED_RESULTS_ROOT / (
    "poc-vms-41-event-extractor-diagnostic-audit-20260814"
)
DEFAULT_PARTIAL_ROOT = APPROVED_RESULTS_ROOT / (
    ".poc-vms-41-event-extractor-diagnostic-audit-20260814.partial"
)

EXPECTED_ROOT_KEYS = {
    "schema_version",
    "audit_id",
    "source_poc_id",
    "source_run_id",
    "review_completed_at",
    "auditor",
    "blindness",
    "purpose",
    "confirmation_eligible",
    "component_qualification",
    "source_final_receipt_file_sha256",
    "source_artifact_tree_sha256",
    "case_audits",
    "required_revision_codes",
    "explicit_nonclaims",
}
EXPECTED_CASE_KEYS = {
    "case_id",
    "attempt_id",
    "content_fidelity",
    "occurrence_segmentation",
    "temporal_status_fidelity",
    "relation_projection_fidelity",
    "merge_fidelity",
    "tool_boundary_posthoc",
    "diagnostic_verdict",
    "finding_codes",
    "notes",
}
EXPECTED_AUDITOR_KEYS = {"actor_id", "actor_type", "independence"}
RFC3339_UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
FROZEN_FREEZE_SHA256 = "2ae350c66d2d94bd63a8de1a702278a9d1b9e49d96f3ba39401d8147859db59e"
HISTORICAL_SOURCE_COMMIT = "3b2668404ce42a3bd6eacd76f0ed1a5cfe880769"


class DiagnosticAuditError(RuntimeError):
    """Raised when a post-hoc audit cannot be trusted or sealed."""


def _reject_nonfinite(value: str) -> Any:
    raise ValueError(f"non-finite JSON number: {value}")


def _canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _historical_git_blob(relative: str) -> bytes:
    try:
        result = subprocess.run(
            ["git", "show", f"{HISTORICAL_SOURCE_COMMIT}:{relative}"],
            cwd=REPO_ROOT,
            capture_output=True,
            check=False,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise DiagnosticAuditError("historical Git source unavailable") from exc
    if result.returncode != 0:
        raise DiagnosticAuditError(f"historical Git source absent: {relative}")
    return result.stdout


def _validate_current_or_historical_binding(
    relative: str,
    expected_hash: str,
    label: str,
) -> str:
    relative_path = Path(relative)
    if (
        not relative
        or relative_path.is_absolute()
        or ".." in relative_path.parts
        or relative_path.as_posix() != relative
        or not HEX64.fullmatch(expected_hash)
    ):
        raise DiagnosticAuditError(f"unsafe historical binding: {label}")
    current = REPO_ROOT / relative_path
    if current.is_symlink():
        raise DiagnosticAuditError(f"current historical binding is a symlink: {label}")
    if current.is_file() and sha256_file(current) == expected_hash:
        return "CURRENT_WORKTREE"
    historical = _historical_git_blob(relative)
    if _sha256_bytes(historical) != expected_hash:
        raise DiagnosticAuditError(f"historical Git hash drift: {label}")
    return "PINNED_GIT_COMMIT"


def _load_object(path: Path, label: str) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise DiagnosticAuditError(f"{label} is absent, unsafe, or not a file")
    try:
        value = json.loads(path.read_text(), parse_constant=_reject_nonfinite)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise DiagnosticAuditError(f"{label} is invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise DiagnosticAuditError(f"{label} must be a JSON object")
    return value


def _require_exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    observed = set(value)
    if observed != expected:
        missing = sorted(expected - observed)
        unknown = sorted(observed - expected)
        raise DiagnosticAuditError(
            f"{label} keys differ; missing={missing}, unknown={unknown}"
        )


def _require_nonempty_strings(values: Any, label: str) -> list[str]:
    if (
        not isinstance(values, list)
        or not values
        or any(not isinstance(item, str) or not item.strip() for item in values)
        or len(values) != len(set(values))
    ):
        raise DiagnosticAuditError(f"{label} must be unique non-empty strings")
    return values


def validate_manual_review(review: dict[str, Any]) -> dict[str, Any]:
    """Validate the deliberately non-confirmatory manual review contract."""

    _require_exact_keys(review, EXPECTED_ROOT_KEYS, "manual review")
    fixed = {
        "schema_version": "solve-vein/vms41-posthoc-manual-diagnostic/v1",
        "audit_id": AUDIT_ID,
        "source_poc_id": "POC-VMS-41",
        "source_run_id": "poc-vms-41-event-extractor-qualification-20260814",
        "blindness": "BREACHED_BEFORE_MANUAL_AUDIT",
        "purpose": "FAILURE_LOCALIZATION_ONLY",
        "confirmation_eligible": False,
        "component_qualification": "NOT_QUALIFIED",
    }
    for key, expected in fixed.items():
        if review.get(key) != expected:
            raise DiagnosticAuditError(f"manual review {key} must equal {expected!r}")
    if not isinstance(review.get("review_completed_at"), str) or not RFC3339_UTC.fullmatch(
        review["review_completed_at"]
    ):
        raise DiagnosticAuditError("review_completed_at must be second-precision UTC")
    for key in ("source_final_receipt_file_sha256", "source_artifact_tree_sha256"):
        if not isinstance(review.get(key), str) or not HEX64.fullmatch(review[key]):
            raise DiagnosticAuditError(f"manual review {key} must be lowercase SHA-256")
    auditor = review.get("auditor")
    if not isinstance(auditor, dict):
        raise DiagnosticAuditError("manual review auditor must be an object")
    _require_exact_keys(auditor, EXPECTED_AUDITOR_KEYS, "manual review auditor")
    if auditor != {
        "actor_id": "codex-root-primary",
        "actor_type": "PRIMARY_AGENT",
        "independence": "NOT_INDEPENDENT",
    }:
        raise DiagnosticAuditError("manual review must disclose the non-independent auditor")

    cases = review.get("case_audits")
    if not isinstance(cases, list) or len(cases) != len(EXPECTED_CASE_IDS):
        raise DiagnosticAuditError("manual review must contain exactly four case audits")
    observed_case_ids: list[str] = []
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            raise DiagnosticAuditError(f"case audit {index} must be an object")
        _require_exact_keys(case, EXPECTED_CASE_KEYS, f"case audit {index}")
        case_id = case.get("case_id")
        if case_id != EXPECTED_CASE_IDS[index]:
            raise DiagnosticAuditError("case audits must use the frozen case order")
        observed_case_ids.append(case_id)
        for key in EXPECTED_CASE_KEYS - {"finding_codes"}:
            if not isinstance(case.get(key), str) or not case[key].strip():
                raise DiagnosticAuditError(f"{case_id}.{key} must be a non-empty string")
        _require_nonempty_strings(case.get("finding_codes"), f"{case_id}.finding_codes")
    if len(observed_case_ids) != len(set(observed_case_ids)):
        raise DiagnosticAuditError("manual review contains duplicate case IDs")
    _require_nonempty_strings(review.get("required_revision_codes"), "revision codes")
    nonclaims = _require_nonempty_strings(
        review.get("explicit_nonclaims"), "explicit nonclaims"
    )
    mandatory_nonclaims = {
        "does_not_restore_blindness",
        "does_not_convert_vms41_into_confirmatory_evidence",
        "does_not_qualify_the_event_extractor_profile",
        "does_not_authorize_any_additional_model_call",
    }
    if not mandatory_nonclaims.issubset(nonclaims):
        raise DiagnosticAuditError("manual review omits mandatory nonclaims")
    return review


def _build_source_binding(
    live_bundle: Path = DEFAULT_LIVE_BUNDLE,
    freeze_path: Path = DEFAULT_FREEZE,
) -> tuple[dict[str, Any], dict[str, Any]]:
    freeze = _validate_historical_freeze(freeze_path)
    replay = _historical_verify_live_bundle(live_bundle, freeze_path, freeze)
    if replay.get("errors") != []:
        raise DiagnosticAuditError(f"live bundle replay failed: {replay['errors']}")
    if replay.get("artifact_integrity") != "PASS":
        raise DiagnosticAuditError("live bundle artifact integrity did not PASS")
    if replay.get("mechanical_replay") != "PASS":
        raise DiagnosticAuditError("live bundle mechanical replay did not PASS")
    if replay.get("live_attempt_status") != "INCONCLUSIVE_PROTOCOL":
        raise DiagnosticAuditError("live bundle status drifted from INCONCLUSIVE_PROTOCOL")

    receipt_path = live_bundle / "final-receipt.json"
    receipt = _load_object(receipt_path, "live final receipt")
    case_bindings: list[dict[str, Any]] = []
    for case_id in EXPECTED_CASE_IDS:
        attempt_id = freeze["attempt_ids"][case_id]
        attempt = live_bundle / "attempts" / attempt_id
        paths = {
            "candidate": attempt / "reasoning-trajectory.json",
            "export": attempt / "devin-export.json",
            "invocation_receipt": attempt / "invocation-receipt.json",
            "evaluation": live_bundle / "evaluations" / f"{case_id}.json",
        }
        for label, path in paths.items():
            if path.is_symlink() or not path.is_file():
                raise DiagnosticAuditError(f"unsafe source {case_id}.{label}")
        case_bindings.append(
            {
                "case_id": case_id,
                "attempt_id": attempt_id,
                "candidate_sha256": sha256_file(paths["candidate"]),
                "export_sha256": sha256_file(paths["export"]),
                "invocation_receipt_sha256": sha256_file(paths["invocation_receipt"]),
                "evaluation_sha256": sha256_file(paths["evaluation"]),
            }
        )
    binding = {
        "schema_version": "solve-vein/vms41-posthoc-source-binding/v1",
        "source_poc_id": "POC-VMS-41",
        "source_run_id": receipt.get("run_id"),
        "source_bundle": str(live_bundle),
        "source_final_receipt_file_sha256": sha256_file(receipt_path),
        "source_artifact_tree_sha256": receipt.get("artifact_tree_sha256"),
        "freeze_manifest_sha256": sha256_file(freeze_path),
        "cases": case_bindings,
    }
    return binding, replay


def _historical_test_source_rows(freeze: dict[str, Any]) -> list[dict[str, str]]:
    support_names = {
        "build_vms41_qualification_pack.py",
        "freeze_event_extractor_qualification.py",
        "run_event_extractor_qualification.py",
        "verify_event_extractor_qualification.py",
    }
    rows: list[dict[str, str]] = []
    for row in freeze["frozen_files"]:
        path = Path(row["path"])
        is_package_source = (
            path.parent.as_posix() == "system/solve_vein_analysis"
            and path.suffix == ".py"
        )
        is_test_source = (
            path.parent.as_posix() == "system/tests/solve_vein_analysis"
            and path.name.startswith("test_")
            and path.suffix == ".py"
        )
        is_support_source = (
            path.parent.as_posix() == "system/tests/solve_vein_analysis"
            and path.name in support_names
        )
        if is_package_source or is_test_source or is_support_source:
            rows.append({"path": row["path"], "sha256": row["sha256"]})
    return sorted(rows, key=lambda row: row["path"])


def _validate_historical_freeze(path: Path) -> dict[str, Any]:
    """Validate the immutable manifest members while allowing later new files.

    The original verifier intentionally hashes the *current* qualification
    source set.  That was correct before execution, but after sealing it makes
    any newly added post-hoc test look like historical evidence drift.  This
    validator instead checks every manifest member and reconstructs the frozen
    test-tree hash from those exact members. Current files may evolve after the
    freeze; changed or retired members are verified byte-for-byte from the pinned
    pre-reconstruction Git commit instead of rewriting the freeze.
    """

    if sha256_file(path) != FROZEN_FREEZE_SHA256:
        raise DiagnosticAuditError("historical freeze file hash drift")
    freeze = _load_object(path, "historical freeze")
    if freeze.get("schema_version") != "solve-vein/vms41-preexecution-freeze/v1":
        raise DiagnosticAuditError("historical freeze schema mismatch")
    if freeze.get("poc_id") != "POC-VMS-41":
        raise DiagnosticAuditError("historical freeze POC mismatch")
    if freeze.get("run_id") != "poc-vms-41-event-extractor-qualification-20260814":
        raise DiagnosticAuditError("historical freeze run mismatch")
    frozen_files = freeze.get("frozen_files")
    if not isinstance(frozen_files, list) or len(frozen_files) != 90:
        raise DiagnosticAuditError("historical freeze must contain 90 file bindings")
    observed: set[str] = set()
    for index, row in enumerate(frozen_files):
        if not isinstance(row, dict) or set(row) != {"path", "sha256"}:
            raise DiagnosticAuditError(f"malformed frozen file binding {index}")
        relative, expected_hash = row["path"], row["sha256"]
        if (
            not isinstance(relative, str)
            or relative in observed
            or Path(relative).is_absolute()
            or ".." in Path(relative).parts
            or not isinstance(expected_hash, str)
            or not HEX64.fullmatch(expected_hash)
        ):
            raise DiagnosticAuditError(f"unsafe frozen file binding {index}")
        observed.add(relative)
        _validate_current_or_historical_binding(
            relative,
            expected_hash,
            f"frozen file {index}",
        )
    for binding_name in ("protocol", "acceptable_set_pack"):
        binding = freeze.get(binding_name)
        if not isinstance(binding, dict) or set(binding) != {"path", "sha256"}:
            raise DiagnosticAuditError(f"historical {binding_name} binding malformed")
        _validate_current_or_historical_binding(
            binding["path"],
            binding["sha256"],
            binding_name,
        )

    historic_rows = _historical_test_source_rows(freeze)
    payload = "".join(
        f"{row['sha256']}  {row['path']}\n" for row in historic_rows
    ).encode("utf-8")
    test_gate = freeze.get("test_gate")
    if not isinstance(test_gate, dict):
        raise DiagnosticAuditError("historical test gate missing")
    if _sha256_bytes(payload) != test_gate.get("test_source_tree_sha256"):
        raise DiagnosticAuditError("historical test source subset hash mismatch")
    if (
        test_gate.get("tests_run") != 112
        or test_gate.get("failures") != 0
        or test_gate.get("errors") != 0
        or test_gate.get("skipped") != 0
        or test_gate.get("successful") is not True
        or test_gate.get("verdict") != "PASS"
    ):
        raise DiagnosticAuditError("historical test gate was not an exact PASS")
    _validate_current_or_historical_binding(
        test_gate["protected_absorb_baseline_path"],
        test_gate["protected_absorb_baseline_sha256"],
        "protected absorb baseline",
    )
    if test_gate.get("protected_absorb_file_count") != 161:
        raise DiagnosticAuditError("protected baseline file count drift")

    attempts = freeze.get("attempt_ids")
    if not isinstance(attempts, dict) or set(attempts) != set(EXPECTED_CASE_IDS):
        raise DiagnosticAuditError("historical attempt map mismatch")
    if len(set(attempts.values())) != len(EXPECTED_CASE_IDS):
        raise DiagnosticAuditError("historical attempt IDs are not unique")
    case_specs = freeze.get("case_specs")
    if not isinstance(case_specs, list) or tuple(
        row.get("case_id") for row in case_specs if isinstance(row, dict)
    ) != EXPECTED_CASE_IDS:
        raise DiagnosticAuditError("historical case spec set/order mismatch")
    for row in case_specs:
        for path_field, hash_field in (
            ("problem_path", "problem_sha256"),
            ("raw_path", "raw_sha256"),
        ):
            _validate_current_or_historical_binding(
                row[path_field],
                row[hash_field],
                f"historical case source {row['case_id']}.{path_field}",
            )
        if row.get("source_receipt_path") is not None:
            _validate_current_or_historical_binding(
                row["source_receipt_path"],
                row["source_receipt_sha256"],
                f"historical source receipt {row['case_id']}",
            )
    return freeze


def _recursive_artifact_inventory(bundle: Path) -> tuple[list[dict[str, Any]], str]:
    rows: list[dict[str, Any]] = []
    for path in sorted(bundle.rglob("*")):
        if path.is_symlink():
            raise DiagnosticAuditError(
                f"symlink in live bundle: {path.relative_to(bundle)}"
            )
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
    return rows, _sha256_bytes(payload)


def _historical_verify_live_bundle(
    live_bundle: Path,
    freeze_path: Path,
    freeze: dict[str, Any],
) -> dict[str, Any]:
    errors: list[str] = []
    if live_bundle.is_symlink() or not live_bundle.is_dir():
        return _historical_replay_result(["live bundle is absent or unsafe"], [])
    receipt = _load_object(live_bundle / "final-receipt.json", "live final receipt")
    aggregate = _load_object(live_bundle / "live-aggregate.json", "live aggregate")
    copied_freeze = live_bundle / "preexecution-freeze-manifest.json"
    if (
        copied_freeze.is_symlink()
        or not copied_freeze.is_file()
        or sha256_file(copied_freeze) != sha256_file(freeze_path)
    ):
        errors.append("sealed freeze copy mismatch")
    try:
        actual_rows, actual_tree_hash = _recursive_artifact_inventory(live_bundle)
    except DiagnosticAuditError as exc:
        errors.append(str(exc))
        actual_rows, actual_tree_hash = [], ""
    if receipt.get("artifacts") != actual_rows:
        errors.append("live final receipt artifact inventory mismatch")
    if receipt.get("artifact_tree_sha256") != actual_tree_hash:
        errors.append("live final receipt artifact tree mismatch")
    marker = live_bundle / "COMMITTED"
    expected_marker = (
        "final-receipt.json SHA256="
        + sha256_file(live_bundle / "final-receipt.json")
        + "\n"
    )
    if marker.is_symlink() or not marker.is_file() or marker.read_text() != expected_marker:
        errors.append("live COMMITTED marker mismatch")

    acceptable_binding = freeze["acceptable_set_pack"]
    acceptable_pack = EventExtractionAcceptableSetPack.from_json_text(
        (REPO_ROOT / acceptable_binding["path"]).read_text()
    )
    case_rows: list[dict[str, str]] = []
    terminal_case_ids: list[str] = []
    for case_id in EXPECTED_CASE_IDS:
        attempt_id = freeze["attempt_ids"][case_id]
        attempt = live_bundle / "attempts" / attempt_id
        stored = _load_object(
            live_bundle / "evaluations" / f"{case_id}.json",
            f"stored evaluation {case_id}",
        )
        invocation = _load_object(
            attempt / "invocation-receipt.json", f"invocation {case_id}"
        )
        if attempt.is_dir() and not attempt.is_symlink():
            terminal_case_ids.append(case_id)
        candidate_path = attempt / "reasoning-trajectory.json"
        raw_path = attempt / "raw_solver_trajectory.txt"
        if candidate_path.is_symlink() or not candidate_path.is_file():
            errors.append(f"candidate missing or unsafe: {case_id}")
            continue
        if raw_path.is_symlink() or not raw_path.is_file():
            errors.append(f"raw trajectory missing or unsafe: {case_id}")
            continue
        evaluation = evaluate_candidate_json(
            candidate_path.read_text(),
            acceptable_pack.case_by_id(case_id),
            raw_path.read_bytes(),
        )
        tool_audit = audit_tool_boundary(
            attempt / "devin-export.json",
            attempt,
            attempt_id,
            historical_attempt_bundle=(
                live_bundle.parent
                / f".{live_bundle.name}.partial"
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
        comparisons = {
            "mechanical_evaluation": evaluation.to_dict(),
            "tool_boundary_audit": tool_audit,
            "attempt_file_set_audit": file_set_audit,
            "protocol_errors": protocol_errors,
            "case_status": case_status,
        }
        for key, expected in comparisons.items():
            if stored.get(key) != expected:
                errors.append(f"stored {key} replay mismatch: {case_id}")
        if stored.get("attempt_id") != attempt_id:
            errors.append(f"stored attempt ID mismatch: {case_id}")
        if stored.get("manual_semantic_audit") != "PENDING":
            errors.append(f"premature manual verdict in live bundle: {case_id}")
        case_rows.append(
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
        or any(row["case_status"] == "INCONCLUSIVE_PROTOCOL" for row in case_rows)
        else "PENDING_MANUAL_AUDIT"
        if all(row["case_status"] == "PENDING_MANUAL_AUDIT" for row in case_rows)
        else "FAIL"
    )
    if aggregate.get("terminal_case_ids") != terminal_case_ids:
        errors.append("live aggregate terminal case mismatch")
    if aggregate.get("case_results") != case_rows:
        errors.append("live aggregate case projection mismatch")
    if aggregate.get("overall_status") != expected_status:
        errors.append("live aggregate status mismatch")
    if receipt.get("live_attempt_status") != expected_status:
        errors.append("live final receipt status mismatch")
    if receipt.get("manual_semantic_audit") != "PENDING":
        errors.append("live final receipt has premature manual verdict")
    if receipt.get("component_qualification") != "NOT_YET_DECIDABLE":
        errors.append("live final receipt has premature component verdict")

    frozen_source_paths = {row["path"] for row in _historical_test_source_rows(freeze)}
    current_source_paths = {
        path.relative_to(REPO_ROOT).as_posix()
        for path in qualification_test_source_files()
    }
    additions = sorted(current_source_paths - frozen_source_paths)
    return _historical_replay_result(errors, additions, expected_status)


def _historical_replay_result(
    errors: list[str],
    postfreeze_source_additions: list[str],
    expected_status: str = "NOT_EVALUATED",
) -> dict[str, Any]:
    return {
        "schema_version": "solve-vein/vms41-historical-membership-replay/v1",
        "replay_policy": "VERIFY_EVERY_FROZEN_MEMBER_IGNORE_DECLARED_POSTFREEZE_ADDITIONS",
        "artifact_integrity": "PASS" if not errors else "FAIL",
        "mechanical_replay": "PASS" if not errors else "FAIL",
        "live_attempt_status": expected_status,
        "manual_semantic_audit": "PENDING" if not errors else "NOT_DECIDABLE",
        "component_qualification": "NOT_YET_DECIDABLE",
        "postfreeze_source_additions": postfreeze_source_additions,
        "errors": errors,
    }


def _build_summary(review: dict[str, Any]) -> dict[str, Any]:
    cases = review["case_audits"]
    return {
        "schema_version": "solve-vein/vms41-posthoc-diagnostic-summary/v1",
        "audit_id": AUDIT_ID,
        "source_poc_id": "POC-VMS-41",
        "blindness": "BREACHED_BEFORE_MANUAL_AUDIT",
        "audit_purpose": "FAILURE_LOCALIZATION_ONLY",
        "manual_audit_status": "COMPLETE_POSTHOC_NONCONFIRMATORY",
        "confirmation_eligible": False,
        "vms41_protocol_verdict": "INCONCLUSIVE_PROTOCOL",
        "event_extractor_profile_qualification": "NOT_QUALIFIED",
        "model_global_capability": "NOT_DECIDABLE_FROM_THIS_POC",
        "original_attempt_retry": "PROHIBITED",
        "case_count": len(cases),
        "content_fidelity_pass_count": sum(
            case["content_fidelity"] == "PASS" for case in cases
        ),
        "content_fidelity_partial_count": sum(
            case["content_fidelity"] == "PARTIAL" for case in cases
        ),
        "confirmed_tool_deviation_case_count": sum(
            case["tool_boundary_posthoc"].startswith("FAIL_CONFIRMED")
            for case in cases
        ),
        "frozen_tool_auditor_false_positive_case_count": sum(
            case["tool_boundary_posthoc"] == "PASS_FROZEN_AUDITOR_FALSE_POSITIVE"
            for case in cases
        ),
        "case_verdicts": [
            {
                "case_id": case["case_id"],
                "diagnostic_verdict": case["diagnostic_verdict"],
                "tool_boundary_posthoc": case["tool_boundary_posthoc"],
            }
            for case in cases
        ],
        "required_revision_codes": review["required_revision_codes"],
        "next_qualification_requirement": "NEW_CONTRACT_NEW_FREEZE_FRESH_UNSEEN_HOLDOUT",
        "explicit_nonclaims": review["explicit_nonclaims"],
    }


def _write_once(path: Path, payload: bytes) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    fd = os.open(path, flags, 0o600)
    try:
        offset = 0
        while offset < len(payload):
            offset += os.write(fd, payload[offset:])
        os.fsync(fd)
    finally:
        os.close(fd)


def _artifact_inventory(bundle: Path) -> tuple[list[dict[str, Any]], str]:
    rows: list[dict[str, Any]] = []
    for path in sorted(bundle.iterdir()):
        if path.is_symlink():
            raise DiagnosticAuditError(f"symlink artifact cannot be sealed: {path.name}")
        if path.is_file() and path.name not in {"final-receipt.json", "COMMITTED"}:
            rows.append(
                {
                    "path": path.name,
                    "size_bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    payload = "".join(
        f"{row['sha256']}  {row['path']}\n" for row in rows
    ).encode("utf-8")
    return rows, _sha256_bytes(payload)


def _fsync_directory(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _validate_production_paths(final_root: Path, partial_root: Path) -> None:
    if final_root != DEFAULT_FINAL_ROOT or partial_root != DEFAULT_PARTIAL_ROOT:
        raise DiagnosticAuditError("production CLI cannot redirect the audit roots")
    if not os.path.ismount(APPROVED_VOLUME):
        raise DiagnosticAuditError("D volume is not mounted")
    if APPROVED_RESULTS_ROOT.is_symlink() or not APPROVED_RESULTS_ROOT.is_dir():
        raise DiagnosticAuditError("approved results root is absent or unsafe")
    if APPROVED_RESULTS_ROOT.resolve(strict=True) != APPROVED_RESULTS_ROOT:
        raise DiagnosticAuditError("approved results root resolves through a symlink")
    if APPROVED_RESULTS_ROOT.stat().st_dev != APPROVED_VOLUME.stat().st_dev:
        raise DiagnosticAuditError("approved results root is not on the D device")


def seal_diagnostic_audit(
    *,
    review_path: Path = DEFAULT_REVIEW,
    live_bundle: Path = DEFAULT_LIVE_BUNDLE,
    freeze_path: Path = DEFAULT_FREEZE,
    final_root: Path = DEFAULT_FINAL_ROOT,
    partial_root: Path = DEFAULT_PARTIAL_ROOT,
) -> dict[str, Any]:
    """Seal one immutable diagnostic audit, or verify the identical existing one."""

    review = validate_manual_review(_load_object(review_path, "manual review"))
    binding, replay = _build_source_binding(live_bundle, freeze_path)
    if review["source_final_receipt_file_sha256"] != binding[
        "source_final_receipt_file_sha256"
    ]:
        raise DiagnosticAuditError("manual review binds another final receipt")
    if review["source_artifact_tree_sha256"] != binding[
        "source_artifact_tree_sha256"
    ]:
        raise DiagnosticAuditError("manual review binds another artifact tree")
    expected_attempts = {
        row["case_id"]: row["attempt_id"] for row in binding["cases"]
    }
    for case in review["case_audits"]:
        if expected_attempts.get(case["case_id"]) != case["attempt_id"]:
            raise DiagnosticAuditError("manual case audit binds another attempt")

    if final_root.exists() or final_root.is_symlink():
        result = verify_diagnostic_audit(
            audit_root=final_root,
            live_bundle=live_bundle,
            freeze_path=freeze_path,
        )
        if result["artifact_integrity"] != "PASS":
            raise DiagnosticAuditError(f"existing audit is invalid: {result['errors']}")
        result["commit_status"] = "ALREADY_COMMITTED"
        return result
    if partial_root.exists() or partial_root.is_symlink():
        raise DiagnosticAuditError("partial audit root already exists; recovery is manual")
    if final_root.parent != partial_root.parent or not final_root.parent.is_dir():
        raise DiagnosticAuditError("audit roots must share an existing parent")
    if final_root.parent.is_symlink():
        raise DiagnosticAuditError("audit parent cannot be a symlink")

    partial_root.mkdir(mode=0o700)
    try:
        _write_once(partial_root / "source-binding.json", _canonical_json_bytes(binding))
        _write_once(partial_root / "verifier-replay.json", _canonical_json_bytes(replay))
        _write_once(partial_root / "manual-diagnostic.json", _canonical_json_bytes(review))
        summary = _build_summary(review)
        _write_once(partial_root / "diagnostic-summary.json", _canonical_json_bytes(summary))
        artifacts, tree_hash = _artifact_inventory(partial_root)
        receipt = {
            "schema_version": "solve-vein/vms41-posthoc-final-receipt/v1",
            "audit_id": AUDIT_ID,
            "sealed_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "source_final_receipt_file_sha256": binding[
                "source_final_receipt_file_sha256"
            ],
            "source_artifact_tree_sha256": binding["source_artifact_tree_sha256"],
            "manual_diagnostic_sha256": sha256_file(
                partial_root / "manual-diagnostic.json"
            ),
            "artifacts": artifacts,
            "artifact_tree_sha256": tree_hash,
            "artifact_integrity": "PASS",
            "manual_audit_status": "COMPLETE_POSTHOC_NONCONFIRMATORY",
            "blindness": "BREACHED_BEFORE_MANUAL_AUDIT",
            "confirmation_eligible": False,
            "component_qualification": "NOT_QUALIFIED",
            "original_attempt_retry": "PROHIBITED",
        }
        _write_once(partial_root / "final-receipt.json", _canonical_json_bytes(receipt))
        _write_once(
            partial_root / "COMMITTED",
            (
                "final-receipt.json SHA256="
                + sha256_file(partial_root / "final-receipt.json")
                + "\n"
            ).encode("utf-8"),
        )
        _fsync_directory(partial_root)
        os.replace(partial_root, final_root)
        _fsync_directory(final_root.parent)
    except Exception:
        # Preserve a partial directory for diagnosis; never erase evidence here.
        raise

    result = verify_diagnostic_audit(
        audit_root=final_root,
        live_bundle=live_bundle,
        freeze_path=freeze_path,
    )
    if result["artifact_integrity"] != "PASS":
        raise DiagnosticAuditError(f"sealed audit failed verification: {result['errors']}")
    result["commit_status"] = "COMMITTED"
    return result


def verify_diagnostic_audit(
    *,
    audit_root: Path = DEFAULT_FINAL_ROOT,
    live_bundle: Path = DEFAULT_LIVE_BUNDLE,
    freeze_path: Path = DEFAULT_FREEZE,
) -> dict[str, Any]:
    """Read-only verification of the audit and its immutable source bindings."""

    errors: list[str] = []
    expected_names = {
        "source-binding.json",
        "verifier-replay.json",
        "manual-diagnostic.json",
        "diagnostic-summary.json",
        "final-receipt.json",
        "COMMITTED",
    }
    if audit_root.is_symlink() or not audit_root.is_dir():
        return _verification_result(["audit root is absent or unsafe"])
    observed_names = {path.name for path in audit_root.iterdir()}
    if observed_names != expected_names:
        errors.append(
            f"audit file set mismatch: missing={sorted(expected_names-observed_names)}, "
            f"unknown={sorted(observed_names-expected_names)}"
        )
    if any(path.is_symlink() for path in audit_root.iterdir()):
        errors.append("audit contains a symlink")
    try:
        receipt = _load_object(audit_root / "final-receipt.json", "audit receipt")
        review = validate_manual_review(
            _load_object(audit_root / "manual-diagnostic.json", "sealed manual review")
        )
        binding = _load_object(audit_root / "source-binding.json", "source binding")
        replay = _load_object(audit_root / "verifier-replay.json", "verifier replay")
        summary = _load_object(audit_root / "diagnostic-summary.json", "summary")
    except DiagnosticAuditError as exc:
        return _verification_result(errors + [str(exc)])

    try:
        artifacts, tree_hash = _artifact_inventory(audit_root)
    except DiagnosticAuditError as exc:
        errors.append(str(exc))
        artifacts, tree_hash = [], ""
    if receipt.get("artifacts") != artifacts:
        errors.append("audit artifact inventory mismatch")
    if receipt.get("artifact_tree_sha256") != tree_hash:
        errors.append("audit artifact tree mismatch")
    if receipt.get("manual_diagnostic_sha256") != sha256_file(
        audit_root / "manual-diagnostic.json"
    ):
        errors.append("manual diagnostic hash mismatch")
    marker = audit_root / "COMMITTED"
    expected_marker = (
        "final-receipt.json SHA256="
        + sha256_file(audit_root / "final-receipt.json")
        + "\n"
    )
    if marker.is_symlink() or not marker.is_file() or marker.read_text() != expected_marker:
        errors.append("COMMITTED marker mismatch")
    if summary != _build_summary(review):
        errors.append("diagnostic summary is not a deterministic review projection")
    fixed_receipt = {
        "artifact_integrity": "PASS",
        "manual_audit_status": "COMPLETE_POSTHOC_NONCONFIRMATORY",
        "blindness": "BREACHED_BEFORE_MANUAL_AUDIT",
        "confirmation_eligible": False,
        "component_qualification": "NOT_QUALIFIED",
        "original_attempt_retry": "PROHIBITED",
    }
    for key, expected in fixed_receipt.items():
        if receipt.get(key) != expected:
            errors.append(f"audit receipt {key} drift")

    try:
        current_binding, current_replay = _build_source_binding(live_bundle, freeze_path)
    except Exception as exc:  # read-only fail-closed boundary
        errors.append(f"source re-verification failed: {exc}")
    else:
        if binding != current_binding:
            errors.append("source binding drift")
        stored_replay_core = dict(replay)
        current_replay_core = dict(current_replay)
        stored_additions = stored_replay_core.pop("postfreeze_source_additions", None)
        current_additions = current_replay_core.pop("postfreeze_source_additions", None)
        if replay != current_replay and stored_replay_core != current_replay_core:
            errors.append("stored verifier replay drift")
        if (
            not isinstance(stored_additions, list)
            or not isinstance(current_additions, list)
            or not set(stored_additions).issubset(current_additions)
        ):
            errors.append("postfreeze source addition provenance drift")
        if review["source_final_receipt_file_sha256"] != binding.get(
            "source_final_receipt_file_sha256"
        ):
            errors.append("review/source final receipt mismatch")
        if review["source_artifact_tree_sha256"] != binding.get(
            "source_artifact_tree_sha256"
        ):
            errors.append("review/source artifact tree mismatch")
        if receipt.get("source_final_receipt_file_sha256") != binding.get(
            "source_final_receipt_file_sha256"
        ):
            errors.append("receipt/source final receipt mismatch")
        if receipt.get("source_artifact_tree_sha256") != binding.get(
            "source_artifact_tree_sha256"
        ):
            errors.append("receipt/source artifact tree mismatch")
    return _verification_result(errors)


def _verification_result(errors: list[str]) -> dict[str, Any]:
    return {
        "schema_version": "solve-vein/vms41-posthoc-verification/v1",
        "audit_id": AUDIT_ID,
        "artifact_integrity": "PASS" if not errors else "FAIL",
        "manual_audit_status": (
            "COMPLETE_POSTHOC_NONCONFIRMATORY" if not errors else "UNTRUSTED"
        ),
        "confirmation_eligible": False,
        "component_qualification": "NOT_QUALIFIED",
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    try:
        if args.verify:
            result = verify_diagnostic_audit()
        else:
            _validate_production_paths(DEFAULT_FINAL_ROOT, DEFAULT_PARTIAL_ROOT)
            result = seal_diagnostic_audit()
    except (DiagnosticAuditError, OSError, ValueError) as exc:
        print(json.dumps({"artifact_integrity": "FAIL", "error": str(exc)}))
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["artifact_integrity"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
