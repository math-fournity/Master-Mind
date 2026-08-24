"""Side-effect-free ImplementationCompletionBundle assembler.

This module builds candidate completion bundles for ordinary
implementer-owned work packages.  It is intentionally not a CAS writer, not a
state-transition service, and not an audit substitute.  It only turns a
verified WorkPackagePlan plus caller-supplied refs into a schema-valid
``ImplementationCompletionBundle`` when the package contract permits that
object and the side-effect claims remain zero.
"""

from __future__ import annotations

from copy import deepcopy
import hashlib
from pathlib import Path
from typing import Any

from ..contracts.completion_contract import load_dag_index, verify_completion_contract
from ..contracts.work_package_plan import verify_work_package_plan_file
from ..hashing import canonical_json_bytes


ZERO_IMPLEMENTATION_BUNDLE_SIDE_EFFECT_COUNTS = {
    "database_connections": 0,
    "database_reads": 0,
    "database_writes": 0,
    "redis_connections": 0,
    "redis_reads": 0,
    "redis_writes": 0,
    "d_volume_writes": 0,
    "model_invocations_by_profile": {},
    "solver_launches": 0,
    "human_gate_decisions": 0,
}

_OPTIONAL_ARRAY_FIELDS = (
    "modified_files",
    "schema_ids_and_hashes",
    "code_entrypoints",
    "state_transitions_implemented",
    "fault_injection_receipts",
    "capability_reports",
    "artifact_refs",
    "claims",
    "nonclaims",
    "known_limitations",
    "protocol_deviations",
    "unresolved_findings",
    "inherited_audit_debt",
    "recovery_notes",
)

_REQUIRED_INPUT_FIELDS = {
    "bundle_id",
    "wp_id",
    "implementation_attempt_id",
    "implementation_subject",
    "requirement_coverage",
    "test_receipts",
    "audit_replay_commands",
    "created_at",
    "creator",
}

_ALLOWED_INPUT_FIELDS = _REQUIRED_INPUT_FIELDS | set(_OPTIONAL_ARRAY_FIELDS)


class ImplementationBundleEvidenceError(ValueError):
    """Raised when a candidate bundle would overclaim or violate its plan."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ImplementationBundleEvidenceError(message)


def _bundle_hash(bundle: dict[str, Any]) -> str:
    candidate = deepcopy(bundle)
    candidate["bundle_hash"] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def _as_array(bundle_input: dict[str, Any], field: str) -> list[Any]:
    value = bundle_input.get(field, [])
    _require(isinstance(value, list), f"{field} must be an array")
    return deepcopy(value)


def _ref_key(ref: dict[str, Any]) -> tuple[str, str] | None:
    if not isinstance(ref, dict):
        return None
    ref_value = ref.get("ref")
    sha = ref.get("sha256")
    if isinstance(ref_value, str) and isinstance(sha, str):
        return (ref_value, sha)
    return None


def _ensure_ref_present(refs: list[Any], required_ref: dict[str, str]) -> list[Any]:
    result = deepcopy(refs)
    required_key = _ref_key(required_ref)
    _require(required_key is not None, "required ref/hash is malformed")
    if not any(_ref_key(item) == required_key for item in result):
        result.append(deepcopy(required_ref))
    return result


def _validate_requirement_coverage(
    *,
    coverage: Any,
    plan_requirement_ids: set[str],
    plan_normative_clause_ids: set[str],
) -> list[dict[str, Any]]:
    _require(isinstance(coverage, list) and coverage, "requirement_coverage must be a non-empty array")
    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in coverage:
        _require(isinstance(item, dict), "each requirement_coverage item must be an object")
        requirement_id = item.get("requirement_id")
        _require(isinstance(requirement_id, str), "coverage item missing requirement_id")
        _require(requirement_id in plan_requirement_ids, f"coverage requirement {requirement_id} is not in the plan")
        _require(requirement_id not in seen, f"duplicate coverage requirement {requirement_id}")
        seen.add(requirement_id)
        clause_ids = item.get("normative_clause_ids", [])
        _require(isinstance(clause_ids, list), f"coverage {requirement_id} normative_clause_ids must be an array")
        extra_clauses = sorted(set(clause_ids) - plan_normative_clause_ids)
        _require(not extra_clauses, f"coverage {requirement_id} references clauses outside the plan: {extra_clauses}")
        normalized.append(deepcopy(item))
    missing = sorted(plan_requirement_ids - seen)
    _require(not missing, f"missing requirement coverage for plan requirements: {missing}")
    return normalized


def build_side_effect_free_implementation_completion_bundle(
    *,
    bundle_input: dict[str, Any],
    plan_path: Path,
    expected_plan_sha256: str,
    dag_path: Path,
) -> dict[str, Any]:
    """Build one ordinary implementer-owned candidate bundle.

    The function validates the WorkPackagePlan, checks the canonical DAG
    owner/contract, enforces side-effect-free evidence shape, computes the
    bundle hash, and then reuses the DAG-aware CompletionContractVerifier.
    """

    _require(isinstance(bundle_input, dict), "bundle_input must be a JSON object")
    unknown = sorted(set(bundle_input) - _ALLOWED_INPUT_FIELDS)
    _require(not unknown, f"unknown bundle_input fields: {unknown}")
    missing = sorted(_REQUIRED_INPUT_FIELDS - set(bundle_input))
    _require(not missing, f"missing bundle_input fields: {missing}")

    wp_id = bundle_input.get("wp_id")
    _require(isinstance(wp_id, str) and wp_id.startswith("WP-"), "wp_id is required")
    _require(wp_id not in {"WP-DOC0", "WP-GA1"}, f"{wp_id} does not use ImplementationCompletionBundle")

    plan_result = verify_work_package_plan_file(
        plan_path=plan_path,
        dag_path=dag_path,
        expected_wp_id=wp_id,
        expected_file_sha256=expected_plan_sha256,
    )
    if not plan_result.passed or plan_result.verified_plan is None:
        details = "; ".join(plan_result.details) or "plan verification failed"
        raise ImplementationBundleEvidenceError(details)
    verified_plan = plan_result.verified_plan
    plan = verified_plan.plan
    _require(plan.get("execution_mode") == "SIDE_EFFECT_FREE", "only SIDE_EFFECT_FREE candidate bundles are supported")
    _require(
        bundle_input["implementation_attempt_id"] == plan.get("implementation_attempt_id"),
        "implementation_attempt_id must match the verified WorkPackagePlan",
    )

    dag_node = load_dag_index(dag_path).get(wp_id)
    _require(isinstance(dag_node, dict), f"unknown work package in DAG: {wp_id}")
    _require(dag_node.get("owner_type") == "IMPLEMENTER", f"{wp_id} is not implementer-owned")
    _require(dag_node.get("completion_contract") == "IMPLEMENTATION_BUNDLE", f"{wp_id} does not use IMPLEMENTATION_BUNDLE")

    implementation_subject = deepcopy(bundle_input["implementation_subject"])
    _require(isinstance(implementation_subject, dict), "implementation_subject must be an object")

    test_receipts = _as_array(bundle_input, "test_receipts")
    _require(test_receipts, "test_receipts must be non-empty")
    live_run_receipts: list[Any] = []

    plan_ref = {"ref": str(plan_path), "sha256": expected_plan_sha256}
    spec_refs = deepcopy(plan.get("normative_spec_refs_and_hashes", []))
    _require(isinstance(spec_refs, list) and spec_refs, "plan normative_spec_refs_and_hashes must be a non-empty array")
    spec_refs = _ensure_ref_present(spec_refs, plan["canonical_dag"])
    spec_refs = _ensure_ref_present(spec_refs, plan["normative_index_ref_and_hash"])
    artifact_refs = _ensure_ref_present(_as_array(bundle_input, "artifact_refs"), plan_ref)

    coverage = _validate_requirement_coverage(
        coverage=bundle_input["requirement_coverage"],
        plan_requirement_ids=set(plan.get("requirement_ids", [])),
        plan_normative_clause_ids=set(plan.get("normative_clause_ids", [])),
    )

    nonclaims = _as_array(bundle_input, "nonclaims")
    _require(nonclaims, "nonclaims must be non-empty")
    nonclaims = list(nonclaims)
    nonclaims.append("This bundle is a side-effect-free READY_FOR_AUDIT candidate, not AUDITED_PASS.")
    nonclaims.append("This bundle does not authorize DB, Redis, D-volume CAS/Vault, model, Solver, HumanGate, scientific, or production side effects.")

    bundle: dict[str, Any] = {
        "schema_id": "seven/implementation-completion-bundle",
        "schema_version": 1,
        "bundle_id": bundle_input["bundle_id"],
        "wp_id": wp_id,
        "implementation_attempt_id": bundle_input["implementation_attempt_id"],
        "status": "READY_FOR_AUDIT",
        "baseline": deepcopy(plan["baseline"]),
        "implementation_subject": implementation_subject,
        "spec_refs_and_hashes": spec_refs,
        "requirement_coverage": coverage,
        "modified_files": _as_array(bundle_input, "modified_files"),
        "schema_ids_and_hashes": _as_array(bundle_input, "schema_ids_and_hashes"),
        "code_entrypoints": _as_array(bundle_input, "code_entrypoints"),
        "state_transitions_implemented": _as_array(bundle_input, "state_transitions_implemented"),
        "test_receipts": test_receipts,
        "fault_injection_receipts": _as_array(bundle_input, "fault_injection_receipts"),
        "capability_reports": _as_array(bundle_input, "capability_reports"),
        "live_run_receipts": live_run_receipts,
        "artifact_refs": artifact_refs,
        "external_side_effect_counts": deepcopy(ZERO_IMPLEMENTATION_BUNDLE_SIDE_EFFECT_COUNTS),
        "claims": _as_array(bundle_input, "claims"),
        "nonclaims": nonclaims,
        "known_limitations": _as_array(bundle_input, "known_limitations"),
        "protocol_deviations": _as_array(bundle_input, "protocol_deviations"),
        "unresolved_findings": _as_array(bundle_input, "unresolved_findings"),
        "inherited_audit_debt": _as_array(bundle_input, "inherited_audit_debt"),
        "recovery_notes": _as_array(bundle_input, "recovery_notes"),
        "audit_replay_commands": deepcopy(bundle_input["audit_replay_commands"]),
        "created_at": bundle_input["created_at"],
        "creator": bundle_input["creator"],
        "bundle_hash": None,
    }
    bundle["bundle_hash"] = _bundle_hash(bundle)

    verification = verify_completion_contract(
        dag_path=dag_path,
        expected_dag_sha256=verified_plan.canonical_dag_sha256,
        wp_id=wp_id,
        submitted_object=bundle,
        actor_type="IMPLEMENTER",
        state_command="READY_FOR_AUDIT",
        expected_subject_commit=implementation_subject.get("commit"),
        expected_subject_tree=implementation_subject.get("tree"),
    )
    if not verification.passed:
        detail = "; ".join(verification.details) or "CompletionContractVerifier rejected bundle"
        raise ImplementationBundleEvidenceError(detail)

    return bundle


__all__ = [
    "ImplementationBundleEvidenceError",
    "ZERO_IMPLEMENTATION_BUNDLE_SIDE_EFFECT_COUNTS",
    "build_side_effect_free_implementation_completion_bundle",
]
