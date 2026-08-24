"""DOC0 bootstrap evidence assembler.

This module is deliberately side-effect-free.  It does not run tests, write
files, sign anything, or upgrade a work package state.  It only takes already
sealed documentation/test receipts and builds the small DOC0 bootstrap
completion record when their identities and zero-side-effect claims agree.
"""

from __future__ import annotations

from copy import deepcopy
import hashlib
from typing import Any

from ..hashing import canonical_json_bytes


ZERO_DOC0_SIDE_EFFECT_COUNTS = {
    "db_connections": 0,
    "db_writes": 0,
    "redis_connections": 0,
    "remote_model_calls": 0,
    "target_solver_launches": 0,
    "d_volume_writes": 0,
}


class Doc0BootstrapEvidenceError(ValueError):
    """Raised when DOC0 bootstrap evidence would overclaim or drift."""


def _record_hash(record: dict[str, Any]) -> str:
    candidate = deepcopy(record)
    candidate["record_hash"] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise Doc0BootstrapEvidenceError(message)


def _committed_subject_from_doc_contract(
    doc_contract_receipt: dict[str, Any],
) -> dict[str, str]:
    subject = doc_contract_receipt.get("implementation_subject", {})
    _require(
        subject.get("working_tree_clean") is True,
        "doc contract receipt is not bound to a clean committed tree",
    )
    _require(
        subject.get("source_relation") == "COMMITTED_TREE",
        "doc contract receipt source relation is not COMMITTED_TREE",
    )
    commit = subject.get("commit")
    tree = subject.get("tree")
    _require(isinstance(commit, str) and len(commit) == 40, "missing committed subject commit")
    _require(isinstance(tree, str) and len(tree) == 40, "missing committed subject tree")
    return {"commit": commit, "tree": tree}


def build_doc0_bootstrap_completion_record(
    *,
    record_id: str,
    doc_contract_receipt: dict[str, Any],
    doc_contract_receipt_ref_and_hash: dict[str, str],
    doc0_test_receipt: dict[str, Any],
    doc0_test_receipt_ref_and_hash: dict[str, str],
    created_at: str,
    creator: str,
) -> dict[str, Any]:
    """Build a DOC0 bootstrap completion record from two sealed receipts.

    The builder is intentionally stricter than the individual receipt schemas:
    a dirty working-tree doc-contract receipt is useful as a status receipt, but
    cannot be used to create a DOC0 bootstrap completion record.
    """

    _require(record_id, "record_id is required")
    _require(created_at, "created_at is required")
    _require(creator, "creator is required")

    _require(doc_contract_receipt.get("schema_id") == "seven/docs/doc-contract-verification-receipt", "wrong doc contract receipt schema")
    _require(doc_contract_receipt.get("verdict") == "PASS", "doc contract receipt is not PASS")
    _require(not doc_contract_receipt.get("errors"), "doc contract receipt has errors")
    subject = _committed_subject_from_doc_contract(doc_contract_receipt)

    _require(doc0_test_receipt.get("schema_id") == "seven/docs/doc0-test-execution-receipt", "wrong DOC0 test receipt schema")
    _require(doc0_test_receipt.get("wp_id") == "WP-DOC0", "test receipt is not for WP-DOC0")
    _require(doc0_test_receipt.get("aggregate_verdict") == "PASS", "DOC0 test receipt is not PASS")
    _require(
        doc0_test_receipt.get("side_effect_counts") == ZERO_DOC0_SIDE_EFFECT_COUNTS,
        "DOC0 test receipt has nonzero side effects",
    )

    test_subject = doc0_test_receipt.get("implementation_subject", {})
    _require(test_subject.get("working_tree_clean_before_tests") is True, "tests were not run from a clean committed tree")
    _require(test_subject.get("source_relation") == "COMMITTED_TREE", "test receipt source relation is not COMMITTED_TREE")
    _require(test_subject.get("commit") == subject["commit"], "doc contract and test receipt commits differ")
    _require(test_subject.get("tree") == subject["tree"], "doc contract and test receipt trees differ")

    plan_ref = doc_contract_receipt.get("work_package_plan_ref_and_hash")
    index_ref = doc_contract_receipt.get("normative_index_ref_and_hash")
    _require(plan_ref == doc0_test_receipt.get("work_package_plan_ref_and_hash"), "work package plan refs differ")
    _require(index_ref == doc0_test_receipt.get("normative_index_ref_and_hash"), "normative index refs differ")

    record: dict[str, Any] = {
        "schema_id": "seven/docs/doc-bootstrap-completion-record",
        "schema_version": 1,
        "record_id": record_id,
        "wp_id": "WP-DOC0",
        "implementation_subject": subject,
        "work_package_plan_ref_and_hash": plan_ref,
        "normative_index_ref_and_hash": index_ref,
        "test_receipts": [
            doc_contract_receipt_ref_and_hash,
            doc0_test_receipt_ref_and_hash,
        ],
        "side_effect_counts": dict(ZERO_DOC0_SIDE_EFFECT_COUNTS),
        "storage_assurance": "LOCAL_GIT_APPEND_ONLY_NOT_CAS",
        "claims": [
            "The bound committed DOC0 documentation subject passed the documentation contract verifier.",
            "The bound committed DOC0 documentation subject passed the DOC0 test receipt aggregate verdict.",
            "The DOC0 bootstrap record is derived from matching plan, normative index, commit, and tree receipts.",
        ],
        "nonclaims": [
            "This record is not an ImplementationCompletionBundle for any non-DOC0 work package.",
            "This record does not constitute independent semantic review or AUDITED_PASS.",
            "This record does not authorize DB, Redis, D-volume CAS/Vault, model, Solver, HumanGate, scientific, or production side effects.",
            "This record is protected only by local Git append-only history unless separately imported into a stronger trust anchor.",
        ],
        "created_at": created_at,
        "creator": creator,
        "record_hash_algorithm": "sha256(canonical-json-with-record_hash-null)",
        "record_hash": None,
    }
    record["record_hash"] = _record_hash(record)
    return record


__all__ = [
    "Doc0BootstrapEvidenceError",
    "ZERO_DOC0_SIDE_EFFECT_COUNTS",
    "build_doc0_bootstrap_completion_record",
]
