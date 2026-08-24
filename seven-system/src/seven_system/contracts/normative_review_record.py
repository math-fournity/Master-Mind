"""Semantic verification for NormativeRequirementReviewRecord.

This verifier is deliberately side-effect free.  It does not create an
independent review, does not sign a record, and does not grant AUDITED_PASS.
It only checks that a supplied, signed review record is mechanically bound to
the frozen NormativeRequirementIndex and that its zero-remainder claim is true.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
from typing import Any

from ..hashing import file_sha256
from ..human.signed_object_verifier import verify_normative_requirement_review_record


@dataclass(frozen=True)
class NormativeReviewRecordVerificationResult:
    """Result returned by the review-record semantic verifier."""

    verdict: str
    error_codes: list[str] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    reviewed_clause_count: int = 0
    index_clause_count: int = 0
    reviewer_actor_id: str | None = None
    index_sha256: str | None = None
    record_sha256: str | None = None

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"

    def to_dict(self) -> dict[str, Any]:
        return {
            "verdict": self.verdict,
            "error_codes": self.error_codes,
            "details": self.details,
            "reviewed_clause_count": self.reviewed_clause_count,
            "index_clause_count": self.index_clause_count,
            "reviewer_actor_id": self.reviewer_actor_id,
            "index_sha256": self.index_sha256,
            "record_sha256": self.record_sha256,
        }


def _load_json_object(path: Path, label: str) -> tuple[dict[str, Any] | None, list[str]]:
    if path.is_symlink():
        return None, [f"{label} path must not be a symlink: {path}"]
    if not path.is_file():
        return None, [f"{label} file does not exist: {path}"]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, [f"cannot read {label} JSON: {exc}"]
    if not isinstance(payload, dict):
        return None, [f"{label} must be a JSON object"]
    return payload, []


def _known_requirement_ids(index: dict[str, Any]) -> set[str]:
    catalog = index.get("requirement_catalog", [])
    return {
        item["requirement_id"]
        for item in catalog
        if isinstance(item, dict) and isinstance(item.get("requirement_id"), str)
    }


def _known_wp_ids(index: dict[str, Any]) -> set[str]:
    values = index.get("canonical_work_package_ids", [])
    return {item for item in values if isinstance(item, str)}


def _known_clause_ids(index: dict[str, Any]) -> set[str]:
    clauses = index.get("clauses", [])
    return {
        item["clause_id"]
        for item in clauses
        if isinstance(item, dict) and isinstance(item.get("clause_id"), str)
    }


def _computed_remainder(record: dict[str, Any], index: dict[str, Any]) -> dict[str, int]:
    known_clauses = _known_clause_ids(index)
    known_requirements = _known_requirement_ids(index)
    known_wps = _known_wp_ids(index)

    decisions = record.get("decisions", [])
    seen: set[str] = set()
    duplicate_count = 0
    unknown_requirement_count = 0
    unknown_work_package_count = 0
    consumer_unassigned_count = 0
    unconsumed_clause_count = 0
    reclassification_required_count = 0
    invalid_clause_count = 0
    unknown_clause_count = 0

    if not isinstance(decisions, list):
        decisions = []

    for decision in decisions:
        if not isinstance(decision, dict):
            continue
        clause_id = decision.get("clause_id")
        if isinstance(clause_id, str):
            if clause_id in seen:
                duplicate_count += 1
            seen.add(clause_id)
            if clause_id not in known_clauses:
                unknown_clause_count += 1

        requirement_ids = decision.get("requirement_ids", [])
        if isinstance(requirement_ids, list):
            unknown_requirement_count += sum(
                1 for requirement_id in requirement_ids
                if not isinstance(requirement_id, str) or requirement_id not in known_requirements
            )

        wp_values: list[Any] = []
        for field in ("applicable_wp_ids", "consumer_wp_ids"):
            value = decision.get(field, [])
            if isinstance(value, list):
                wp_values.extend(value)
        unknown_work_package_count += sum(
            1 for wp_id in wp_values
            if not isinstance(wp_id, str) or wp_id not in known_wps
        )

        consumer_wp_ids = decision.get("consumer_wp_ids", [])
        if not isinstance(consumer_wp_ids, list) or not consumer_wp_ids:
            consumer_unassigned_count += 1
            if clause_id in known_clauses:
                unconsumed_clause_count += 1

        if decision.get("decision") == "RECLASSIFY_REQUIRED":
            reclassification_required_count += 1
        if decision.get("decision") == "INVALID_CLAUSE":
            invalid_clause_count += 1

    unreviewed = len(known_clauses - seen)
    return {
        "unreviewed_clause_count": unreviewed,
        "duplicate_clause_decision_count": duplicate_count,
        "unknown_requirement_count": unknown_requirement_count,
        "unknown_work_package_count": unknown_work_package_count,
        "consumer_unassigned_count": consumer_unassigned_count,
        "unconsumed_clause_count": unconsumed_clause_count,
        "reclassification_required_count": reclassification_required_count,
        "invalid_clause_count": invalid_clause_count + unknown_clause_count,
    }


def verify_normative_requirement_review_record_file(
    *,
    record_path: Path,
    normative_index_path: Path,
    public_key_bytes: bytes,
    expected_index_sha256: str | None = None,
    expected_record_sha256: str | None = None,
) -> NormativeReviewRecordVerificationResult:
    """Verify one signed review record against a frozen normative index."""

    record_path = Path(record_path)
    normative_index_path = Path(normative_index_path)
    errors: list[str] = []
    details: list[str] = []

    record, record_load_errors = _load_json_object(record_path, "review record")
    index, index_load_errors = _load_json_object(normative_index_path, "normative index")
    if record_load_errors or index_load_errors or record is None or index is None:
        return NormativeReviewRecordVerificationResult(
            verdict="FAIL",
            error_codes=["JSON_LOAD_FAILED"],
            details=record_load_errors + index_load_errors,
        )

    record_sha = hashlib.sha256(record_path.read_bytes()).hexdigest()
    index_sha = file_sha256(normative_index_path)
    if expected_record_sha256 is not None and record_sha != expected_record_sha256:
        errors.append("RECORD_HASH_MISMATCH")
        details.append(f"record hash mismatch: expected {expected_record_sha256}, got {record_sha}")
    if expected_index_sha256 is not None and index_sha != expected_index_sha256:
        errors.append("INDEX_HASH_MISMATCH")
        details.append(f"index hash mismatch: expected {expected_index_sha256}, got {index_sha}")

    binding = record.get("index_ref_and_hash")
    if not isinstance(binding, dict) or binding.get("sha256") != index_sha:
        errors.append("INDEX_BINDING_MISMATCH")
        details.append(
            "record index_ref_and_hash.sha256 does not match normative index file"
        )

    expected_policy_id = None
    consumer_policy = index.get("consumer_policy")
    if isinstance(consumer_policy, dict):
        expected_policy_id = consumer_policy.get("policy_id")
    if record.get("reviewed_consumer_policy_id") != expected_policy_id:
        errors.append("CONSUMER_POLICY_MISMATCH")
        details.append(
            f"reviewed_consumer_policy_id {record.get('reviewed_consumer_policy_id')!r} "
            f"!= index policy {expected_policy_id!r}"
        )

    signed = verify_normative_requirement_review_record(
        record,
        public_key_bytes=public_key_bytes,
    )
    if signed.verdict != "PASS":
        errors.append("SIGNED_OBJECT_INVALID")
        details.extend(signed.details)

    computed = _computed_remainder(record, index)
    declared = record.get("remainder")
    if not isinstance(declared, dict):
        errors.append("REMAINDER_INVALID")
        details.append("remainder must be an object")
    else:
        for key, value in computed.items():
            if declared.get(key) != value:
                errors.append("REMAINDER_MISMATCH")
                details.append(
                    f"{key}: declared {declared.get(key)!r}, computed {value}"
                )
        if any(value != 0 for value in computed.values()):
            errors.append("REVIEW_REMAINDER_NONZERO")
            details.append(f"computed review remainder is non-zero: {computed}")

    decisions = record.get("decisions", [])
    reviewed_count = len(decisions) if isinstance(decisions, list) else 0
    index_count = len(_known_clause_ids(index))
    return NormativeReviewRecordVerificationResult(
        verdict="PASS" if not errors else "FAIL",
        error_codes=sorted(set(errors)),
        details=details,
        reviewed_clause_count=reviewed_count,
        index_clause_count=index_count,
        reviewer_actor_id=record.get("reviewer_actor_id") if isinstance(record.get("reviewer_actor_id"), str) else None,
        index_sha256=index_sha,
        record_sha256=record_sha,
    )


__all__ = [
    "NormativeReviewRecordVerificationResult",
    "verify_normative_requirement_review_record_file",
]
