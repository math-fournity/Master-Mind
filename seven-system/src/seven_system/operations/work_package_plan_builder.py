"""Side-effect-free WorkPackagePlan assembler.

This module is a small bridge between the canonical work-package DAG and the
ordinary ``ImplementationCompletionBundle`` builder.  It turns caller supplied
package-specific planning text into a schema-valid, self-hashed
``WorkPackagePlan`` while deriving the brittle parts from machine sources:

* canonical DAG hash and activation dependencies;
* normative index hash and signed review-record binding;
* requirement IDs and normative clause IDs assigned to the selected work package
  by the verified review record;
* source document hashes for the consumed normative clauses;
* zero side-effect authorization fields for ``SIDE_EFFECT_FREE`` plans.

It deliberately does not create or sign a NormativeRequirementReviewRecord,
does not write artifacts, does not change work-package state, and does not
authorize live work.
"""

from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
from typing import Any

from ..contracts.normative_review_record import verify_normative_requirement_review_record_file
from ..hashing import canonical_json_bytes, file_sha256


ZERO_PLAN_SIDE_EFFECT_BUDGET = {
    "db_connections": 0,
    "db_writes": 0,
    "redis_connections": 0,
    "remote_model_calls": 0,
    "target_solver_launches": 0,
    "d_volume_writes": 0,
}

_REQUIRED_PLAN_INPUT_FIELDS = {
    "wp_id",
    "implementation_attempt_id",
    "baseline",
    "normative_review_record_ref_and_hash",
    "development_dependency_bundles",
    "inherited_audit_debt",
    "goals",
    "non_goals",
    "allowed_path_rules",
    "forbidden_boundaries",
    "input_object_types_and_hashes",
    "output_object_types",
    "interfaces_and_schema_ids",
    "state_machines_and_registries",
    "security_and_view_contracts",
    "idempotency_fence_recovery_rules",
    "test_plan_ids",
    "pass_criteria",
    "stop_conditions",
    "explicit_nonclaims",
}

_OPTIONAL_PLAN_INPUT_FIELDS = {
    "plan_timing",
    "protocol_deviations",
}

_ALLOWED_PLAN_INPUT_FIELDS = _REQUIRED_PLAN_INPUT_FIELDS | _OPTIONAL_PLAN_INPUT_FIELDS

_ARRAY_FIELDS = {
    "development_dependency_bundles",
    "inherited_audit_debt",
    "goals",
    "non_goals",
    "allowed_path_rules",
    "forbidden_boundaries",
    "input_object_types_and_hashes",
    "output_object_types",
    "interfaces_and_schema_ids",
    "state_machines_and_registries",
    "security_and_view_contracts",
    "idempotency_fence_recovery_rules",
    "test_plan_ids",
    "pass_criteria",
    "stop_conditions",
    "explicit_nonclaims",
    "protocol_deviations",
}


class WorkPackagePlanBuilderError(ValueError):
    """Raised when an input would produce an unsafe or invalid plan."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise WorkPackagePlanBuilderError(message)


def _plan_hash(plan: dict[str, Any]) -> str:
    candidate = deepcopy(plan)
    candidate["plan_hash"] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def _load_object(path: Path, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WorkPackagePlanBuilderError(f"cannot load {label}: {exc}") from exc
    _require(isinstance(payload, dict), f"{label} must be a JSON object")
    return payload


def _require_ref_hash(value: Any, label: str) -> dict[str, str]:
    _require(isinstance(value, dict), f"{label} must be an object")
    ref = value.get("ref")
    sha = value.get("sha256")
    _require(isinstance(ref, str) and ref, f"{label}.ref is required")
    _require(
        isinstance(sha, str) and len(sha) == 64 and all(ch in "0123456789abcdef" for ch in sha),
        f"{label}.sha256 must be lowercase hex sha256",
    )
    return {"ref": ref, "sha256": sha}


def _require_array(payload: dict[str, Any], field: str, *, non_empty: bool = False) -> list[Any]:
    value = payload.get(field, [])
    _require(isinstance(value, list), f"{field} must be an array")
    _require(not non_empty or bool(value), f"{field} must be non-empty")
    return deepcopy(value)


def _dag_node(dag: dict[str, Any], wp_id: str) -> dict[str, Any]:
    packages = dag.get("work_packages")
    _require(isinstance(packages, list), "canonical DAG work_packages must be an array")
    matches = [item for item in packages if isinstance(item, dict) and item.get("wp_id") == wp_id]
    _require(matches, f"unknown work package in DAG: {wp_id}")
    _require(len(matches) == 1, f"duplicate work package in DAG: {wp_id}")
    return deepcopy(matches[0])


def _normative_payload_for_wp(
    index: dict[str, Any],
    review_record: dict[str, Any],
    wp_id: str,
) -> tuple[list[str], list[str], list[dict[str, str]]]:
    clauses = index.get("clauses")
    _require(isinstance(clauses, list), "normative index clauses must be an array")
    clause_by_id = {
        item["clause_id"]: item
        for item in clauses
        if isinstance(item, dict) and isinstance(item.get("clause_id"), str)
    }

    requirement_ids: set[str] = set()
    source_refs: dict[str, str] = {}
    clause_ids: set[str] = set()
    decisions = review_record.get("decisions")
    _require(isinstance(decisions, list), "normative review decisions must be an array")

    for decision in decisions:
        if not isinstance(decision, dict):
            continue
        if wp_id not in decision.get("consumer_wp_ids", []):
            continue
        clause_id = decision.get("clause_id")
        _require(isinstance(clause_id, str) and clause_id in clause_by_id, "selected review decision has unknown clause_id")
        clause = clause_by_id[clause_id]
        clause_ids.add(clause_id)
        for requirement_id in decision.get("requirement_ids", []):
            _require(isinstance(requirement_id, str), "selected clause has invalid requirement_id")
            requirement_ids.add(requirement_id)
        source_file = clause.get("source_file")
        source_sha = clause.get("source_file_sha256")
        _require(isinstance(source_file, str) and source_file, "selected clause missing source_file")
        _require(isinstance(source_sha, str) and len(source_sha) == 64, "selected clause missing source sha")
        source_refs[source_file] = source_sha

    _require(clause_ids, f"no normative review decisions assigned to {wp_id}")
    _require(requirement_ids, f"no requirement IDs assigned to {wp_id}")
    spec_refs = [
        {"ref": ref, "sha256": sha}
        for ref, sha in sorted(source_refs.items())
    ]
    return sorted(requirement_ids), sorted(clause_ids), spec_refs


def build_side_effect_free_work_package_plan(
    *,
    plan_input: dict[str, Any],
    dag_path: Path,
    normative_index_path: Path,
    normative_review_record_path: Path,
    normative_review_public_key_bytes: bytes,
) -> dict[str, Any]:
    """Build a schema-ready ``SIDE_EFFECT_FREE`` plan for one ordinary package."""

    _require(isinstance(plan_input, dict), "plan_input must be a JSON object")
    unknown = sorted(set(plan_input) - _ALLOWED_PLAN_INPUT_FIELDS)
    _require(not unknown, f"unknown plan_input fields: {unknown}")
    missing = sorted(_REQUIRED_PLAN_INPUT_FIELDS - set(plan_input))
    _require(not missing, f"missing plan_input fields: {missing}")

    wp_id = plan_input.get("wp_id")
    _require(isinstance(wp_id, str) and wp_id.startswith("WP-"), "wp_id is required")
    _require(wp_id not in {"WP-DOC0", "WP-GA1"}, f"{wp_id} cannot use ordinary side-effect-free WorkPackagePlan builder")

    dag_path = Path(dag_path)
    normative_index_path = Path(normative_index_path)
    dag = _load_object(dag_path, "canonical DAG")
    index = _load_object(normative_index_path, "normative index")
    node = _dag_node(dag, wp_id)
    _require(node.get("owner_type") == "IMPLEMENTER", f"{wp_id} is not implementer-owned")
    _require(
        node.get("completion_contract") == "IMPLEMENTATION_BUNDLE",
        f"{wp_id} does not use ImplementationCompletionBundle",
    )

    baseline = plan_input["baseline"]
    _require(isinstance(baseline, dict), "baseline must be an object")
    _require(isinstance(baseline.get("commit"), str) and len(baseline["commit"]) == 40, "baseline.commit must be a 40-char hash")
    _require(isinstance(baseline.get("tree"), str) and len(baseline["tree"]) == 40, "baseline.tree must be a 40-char hash")

    for field in _ARRAY_FIELDS:
        _require_array(plan_input, field, non_empty=field in {
            "goals",
            "allowed_path_rules",
            "output_object_types",
            "test_plan_ids",
            "pass_criteria",
            "stop_conditions",
            "explicit_nonclaims",
        })

    normative_review = _require_ref_hash(
        plan_input["normative_review_record_ref_and_hash"],
        "normative_review_record_ref_and_hash",
    )
    development_dependency_bundles = [
        _require_ref_hash(item, f"development_dependency_bundles[{idx}]")
        for idx, item in enumerate(plan_input["development_dependency_bundles"])
    ]
    input_object_types_and_hashes = [
        _require_ref_hash(item, f"input_object_types_and_hashes[{idx}]")
        for idx, item in enumerate(plan_input["input_object_types_and_hashes"])
    ]

    dag_sha = file_sha256(dag_path)
    index_sha = file_sha256(normative_index_path)
    review_result = verify_normative_requirement_review_record_file(
        record_path=normative_review_record_path,
        normative_index_path=normative_index_path,
        public_key_bytes=normative_review_public_key_bytes,
        expected_index_sha256=index_sha,
        expected_record_sha256=normative_review["sha256"],
    )
    _require(
        review_result.passed,
        "NormativeRequirementReviewRecord verification failed: "
        + "; ".join(review_result.error_codes + review_result.details),
    )
    review_record = _load_object(Path(normative_review_record_path), "normative review record")
    requirement_ids, normative_clause_ids, spec_refs = _normative_payload_for_wp(index, review_record, wp_id)

    nonclaims = _require_array(plan_input, "explicit_nonclaims", non_empty=True)
    nonclaims = list(nonclaims)
    nonclaims.append("This WorkPackagePlan is SIDE_EFFECT_FREE and does not authorize live execution.")
    nonclaims.append("This WorkPackagePlan does not create an ImplementationCompletionBundle, AuditRecord, or AUDITED_PASS.")

    plan: dict[str, Any] = {
        "schema_id": "seven/work-package-plan",
        "schema_version": 1,
        "wp_id": wp_id,
        "implementation_attempt_id": plan_input["implementation_attempt_id"],
        "plan_timing": plan_input.get("plan_timing", "PREREGISTERED"),
        "execution_mode": "SIDE_EFFECT_FREE",
        "protocol_deviations": _require_array(plan_input, "protocol_deviations"),
        "baseline": deepcopy(baseline),
        "canonical_dag": {"ref": str(dag_path), "sha256": dag_sha},
        "development_dependency_bundles": development_dependency_bundles,
        "inherited_audit_debt": _require_array(plan_input, "inherited_audit_debt"),
        "activation_dependencies": deepcopy(node.get("activation_dependencies", [])),
        "normative_index_ref_and_hash": {"ref": str(normative_index_path), "sha256": index_sha},
        "normative_review_record_ref_and_hash": normative_review,
        "requirement_ids": requirement_ids,
        "normative_clause_ids": normative_clause_ids,
        "normative_clause_scope": f"consumer clauses assigned to {wp_id} in the frozen NormativeRequirementIndex",
        "normative_spec_refs_and_hashes": spec_refs,
        "goals": _require_array(plan_input, "goals", non_empty=True),
        "non_goals": _require_array(plan_input, "non_goals"),
        "allowed_path_rules": _require_array(plan_input, "allowed_path_rules", non_empty=True),
        "forbidden_boundaries": _require_array(plan_input, "forbidden_boundaries"),
        "input_object_types_and_hashes": input_object_types_and_hashes,
        "output_object_types": _require_array(plan_input, "output_object_types", non_empty=True),
        "interfaces_and_schema_ids": _require_array(plan_input, "interfaces_and_schema_ids"),
        "state_machines_and_registries": _require_array(plan_input, "state_machines_and_registries"),
        "security_and_view_contracts": _require_array(plan_input, "security_and_view_contracts"),
        "idempotency_fence_recovery_rules": _require_array(plan_input, "idempotency_fence_recovery_rules"),
        "test_plan_ids": _require_array(plan_input, "test_plan_ids", non_empty=True),
        "external_execution_authorization_ref": None,
        "live_run_permit_ref": None,
        "authorization_consumption_reservation_ref": None,
        "side_effect_budget": deepcopy(ZERO_PLAN_SIDE_EFFECT_BUDGET),
        "pass_criteria": _require_array(plan_input, "pass_criteria", non_empty=True),
        "stop_conditions": _require_array(plan_input, "stop_conditions", non_empty=True),
        "explicit_nonclaims": nonclaims,
        "plan_hash_algorithm": "sha256(canonical-json-with-plan_hash-null)",
        "plan_hash": None,
    }
    plan["plan_hash"] = _plan_hash(plan)
    return plan


__all__ = [
    "WorkPackagePlanBuilderError",
    "ZERO_PLAN_SIDE_EFFECT_BUDGET",
    "build_side_effect_free_work_package_plan",
]
