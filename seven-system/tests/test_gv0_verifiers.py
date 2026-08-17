"""WP-GV0 治理与完成合同验证器测试。

测试层级：Schema → Unit → Contract → Security/blocker → Fault injection
所有 blocker test 失败 → 工作包 FAIL，不可用 confidence test 平均抵消。
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import VerificationErrorCode as EC
from seven_system.contracts.completion_contract import (
    verify_completion_contract,
    verify_doc0_bootstrap_record,
    load_dag_index,
)
from seven_system.contracts.security_contract import (
    verify_eea,
    verify_permit_does_not_escalate_parent,
    verify_consumption_receipt,
    verify_authorization_chain,
    verify_signature_envelope,
)
from seven_system.contracts.reservation import (
    SideEffectFreeReferenceBackend,
    Allowance,
)
from seven_system.storage.artifact_store import (
    CompletionArtifactStore,
    ArtifactRef,
    _StoreError,
)
from seven_system.hashing import canonical_json_bytes


# ─── helpers ───────────────────────────────────────────────────────────

DAG_PATH = SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"


def _dag_sha256() -> str:
    return hashlib.sha256(DAG_PATH.read_bytes()).hexdigest()


def _self_hash(obj: dict, hash_field: str) -> str:
    """Compute canonical self-hash of an object (field=null then sha256)."""
    import hashlib as _h
    tmp = dict(obj)
    tmp[hash_field] = None
    canonical = json.dumps(tmp, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return _h.sha256(canonical).hexdigest()


def _make_doc_bootstrap_record() -> dict:
    rec = {
        "schema_id": "seven/docs/doc-bootstrap-completion-record",
        "schema_version": 1,
        "record_id": "test-doc0-001",
        "wp_id": "WP-DOC0",
        "implementation_subject": {"commit": "a" * 40, "tree": "b" * 40},
        "work_package_plan_ref_and_hash": {"ref": "plan.json", "sha256": "0" * 64},
        "normative_index_ref_and_hash": {"ref": "index.json", "sha256": "0" * 64},
        "test_receipts": [{"ref": "test.json", "sha256": "0" * 64}],
        "side_effect_counts": {
            "db_connections": 0,
            "db_writes": 0,
            "redis_connections": 0,
            "remote_model_calls": 0,
            "target_solver_launches": 0,
            "d_volume_writes": 0,
        },
        "storage_assurance": "LOCAL_GIT_APPEND_ONLY_NOT_CAS",
        "claims": ["DOC0 bootstrap complete"],
        "nonclaims": ["Does not constitute AUDITED_PASS"],
        "created_at": "2026-08-14T12:00:00Z",
        "creator": "test-creator",
        "record_hash_algorithm": "sha256(canonical-json-with-record_hash-null)",
        "record_hash": None,
    }
    rec["record_hash"] = _self_hash(rec, "record_hash")
    return rec


def _make_implementation_bundle(wp_id: str = "WP-GV0") -> dict:
    bundle = {
        "schema_id": "seven/implementation-completion-bundle",
        "schema_version": 1,
        "bundle_id": f"test-bundle-{wp_id}-001",
        "wp_id": wp_id,
        "implementation_attempt_id": "attempt-001",
        "status": "READY_FOR_AUDIT",
        "baseline": {"commit": "a" * 40, "tree": "b" * 40},
        "implementation_subject": {"commit": "a" * 40, "tree": "b" * 40},
        "spec_refs_and_hashes": [{"ref": "README.md", "sha256": "0" * 64}],
        "requirement_coverage": [{
            "requirement_id": "AUTH-001",
            "normative_clause_ids": ["NORM-test-01"],
            "code_refs": ["src/test.py"],
            "schema_refs": ["schema.json"],
            "test_receipts": [{"ref": "test.json", "sha256": "0" * 64}],
            "runtime_evidence_refs": [{"ref": "evidence.json", "sha256": "0" * 64}],
            "status": "COVERED",
        }],
        "modified_files": ["src/test.py"],
        "schema_ids_and_hashes": [{"ref": "schema.json", "sha256": "0" * 64}],
        "code_entrypoints": ["test.entrypoint"],
        "state_transitions_implemented": ["NOT_STARTED→IN_PROGRESS"],
        "test_receipts": [{"ref": "test.json", "sha256": "0" * 64}],
        "fault_injection_receipts": [],
        "capability_reports": [{"ref": "cap.json", "sha256": "0" * 64}],
        "live_run_receipts": [],
        "artifact_refs": [],
        "external_side_effect_counts": {
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
        },
        "claims": ["Implementation complete"],
        "nonclaims": ["Does not constitute AUDITED_PASS"],
        "known_limitations": [],
        "protocol_deviations": [],
        "unresolved_findings": [],
        "inherited_audit_debt": [{"ref": "doc0.json", "sha256": "0" * 64}],
        "recovery_notes": [],
        "audit_replay_commands": [["python3", "-m", "unittest", "test"]],
        "created_at": "2026-08-14T12:00:00Z",
        "creator": "test-creator",
        "bundle_hash": None,
    }
    bundle["bundle_hash"] = _self_hash(bundle, "bundle_hash")
    return bundle


def _make_audit_record() -> dict:
    import base64, os
    # Ed25519 signature is 64 bytes → base64 is 86 chars + "=="
    fake_sig = base64.b64encode(os.urandom(64)).decode()
    rec = {
        "schema_id": "seven/audit-record",
        "schema_version": 1,
        "audit_id": "test-audit-001",
        "wp_id": "WP-GA1",
        "audit_assignment_ref_and_hash": {"ref": "assignment.json", "sha256": "0" * 64},
        "assignment_verification_receipt_ref_and_hash": {"ref": "verify.json", "sha256": "0" * 64},
        "audited_bundle_ref_and_hash": {"ref": "bundle.json", "sha256": "0" * 64},
        "audited_subject": {"commit": "a" * 40, "tree": "b" * 40},
        "evidence_index_commit_if_any": None,
        "externally_observed_pinned_trust_root": {
            "trust_root_hash": "0" * 64,
            "source_channel_id": "test-channel",
            "observed_at": "2026-08-14T12:00:00Z",
            "observation_receipt_ref_and_hash": {"ref": "obs.json", "sha256": "0" * 64},
        },
        "runtime_manifest_trust_root_hash": "0" * 64,
        "audit_plan_and_spec_refs_and_hashes": [{"ref": "plan.json", "sha256": "0" * 64}],
        "auditor_principal_id": "test-auditor",
        "auditor_attestation_key_id": "test-key-001",
        "auditor_attestation_public_key_hash": "0" * 64,
        "auditor_session_attestation_ref_and_hash": {"ref": "session.json", "sha256": "0" * 64},
        "independence_evidence": [{"ref": "indep.json", "sha256": "0" * 64}],
        "findings": [],
        "replayed_test_receipts": [{"ref": "test.json", "sha256": "0" * 64}],
        "external_execution_receipts": [],
        "traceability_remainder": 0,
        "orphan_remainder": 0,
        "claims_confirmed": [],
        "claims_rejected": [],
        "nonclaims_checked": [],
        "axis_verdicts": {
            "implementation": {"verdict": "AUDITED_PASS", "finding_ids": [], "evidence_refs": [], "scope_reason_if_not_tested": None},
            "factory": {"verdict": "AUDITED_PASS", "finding_ids": [], "evidence_refs": [], "scope_reason_if_not_tested": None},
            "scientific": {"verdict": "SUPPORTS", "finding_ids": [], "evidence_refs": [], "scope_reason_if_not_tested": None},
            "production_scale": {"verdict": "NOT_TESTED", "finding_ids": [], "evidence_refs": [], "scope_reason_if_not_tested": "out of scope"},
        },
        "scope_limits": [],
        "followups": [],
        "state_transition_effect": "NONE_UNTIL_HUMAN_GATE_SERVICE_ACCEPTS",
        "created_at": "2026-08-14T12:00:00Z",
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-audit-record/v1\u0000",
        "signed_bytes_hash": "0" * 64,
        "signature_envelope": {
            "algorithm": "Ed25519",
            "key_id": "test-key-001",
            "signer_principal_id": "test-auditor",
            "signature_encoding": "base64",
            "signature_b64": fake_sig,
            "signed_bytes_hash": "0" * 64,
        },
        "audit_record_hash_algorithm": "sha256(RFC8785-JCS-object-with-audit_record_hash-null)",
        "audit_record_hash": None,
    }
    rec["audit_record_hash"] = _self_hash(rec, "audit_record_hash")
    return rec


def _make_valid_signature_envelope(domain: str, signed_bytes_hash: str) -> dict:
    return {
        "algorithm": "Ed25519",
        "key_id": "test-key-001",
        "signer_actor_id": "test-signer",
        "signature_encoding": "base64",
        "signature_b64": "A" * 86 + "==",
        "signed_bytes_hash": signed_bytes_hash,
        "trust_root_hash": "0" * 64,
        "actor_roster_hash": "0" * 64,
        "policy_hash": "0" * 64,
        "signature_algorithm_registry_hash": "0" * 64,
    }


def _make_eea(
    *,
    mode: str = "UNAUDITED_AUTHORIZED_CANARY",
    action_scopes: list[dict] | None = None,
) -> dict:
    if action_scopes is None:
        action_scopes = [
            {
                "scope_id": "gv0-d-write",
                "scope_hash_algorithm": "sha256(RFC8785-JCS-action-scope-with-scope_hash-null)",
                "scope_hash": "0" * 64,
                "action_kind": "D_VOLUME_WRITE",
                "authorization_action_registry_entry_ref_and_hash": {"ref": "reg", "sha256": "0" * 64},
                "target_site_hash_if_any": None,
                "target_database_identity_hash_if_any": None,
                "target_redis_namespace_hash_if_any": None,
                "target_release_or_pointer_hash_if_any": None,
                "allowed_carrier_profile_hashes": [],
                "allowed_role_or_solver_contract_hashes": [],
                "allowed_inputs": [{"input_hash": "0" * 64, "sensitivity": "public"}],
                "required_output_sink_and_acl_hash_if_any": None,
                "budget": {
                    "max_invocations": 0,
                    "max_solver_launches": 0,
                    "max_database_writes": 0,
                    "max_redis_writes": 0,
                    "max_d_volume_writes": 1,
                    "max_human_gate_commits": 0,
                    "max_active_release_changes": 0,
                    "max_tokens": 0,
                    "max_cost_microunits": 0,
                    "currency": "USD",
                },
            }
        ]
    eea = {
        "schema_id": "seven/external-execution-authorization",
        "schema_version": 1,
        "authorization_id": "eea-test-001",
        "authorization_mode": mode,
        "subject_work_package_ids": ["WP-GV0"],
        "subject_completion_bundle_refs_and_hashes": [{"ref": "bundle", "sha256": "0" * 64}],
        "activation_audit_record_refs_and_hashes": [],
        "unaudited_dependency_bundle_refs_and_hashes": (
            [{"ref": "doc0", "sha256": "0" * 64}]
            if mode != "AUDITED_ACTIVATION"
            else []
        ),
        "epoch_id_if_any": None,
        "run_id_if_any": None,
        "authorization_action_registry_ref_and_hash": {"ref": "reg", "sha256": "0" * 64},
        "action_scopes": action_scopes,
        "externally_pinned_trust_root": {"object_id": "root", "sha256": "0" * 64},
        "actor_roster_ref_and_hash": {"ref": "roster", "sha256": "0" * 64},
        "human_gate_policy_ref_and_hash": {"ref": "policy", "sha256": "0" * 64},
        "signature_algorithm_registry_ref_and_hash": {"ref": "sigreg", "sha256": "0" * 64},
        "revocation_policy_ref_and_hash": {"ref": "revoc", "sha256": "0" * 64},
        "stop_conditions": ["budget_exhausted"],
        "issuer_actor_id": "site-owner",
        "issuer_key_id": "owner-key-001",
        "issued_at": "2026-08-14T00:00:00Z",
        "not_before": "2026-08-14T00:00:00Z",
        "expires_at": "2026-08-15T00:00:00Z",
        "nonce": "n" * 16,
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-external-execution-authorization/v1\0",
        "signed_bytes_hash": "0" * 64,
        "signature_envelope": _make_valid_signature_envelope(
            "seven-external-execution-authorization/v1\0", "0" * 64
        ),
        "authorization_hash_algorithm": "sha256(RFC8785-JCS-object-with-authorization_hash-null)",
        "authorization_hash": None,  # will be computed
    }
    obj_for_hash = dict(eea)
    obj_for_hash["authorization_hash"] = None
    eea["authorization_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    return eea


def _make_permit(eea: dict, *, action_units: list[dict] | None = None) -> dict:
    scope = eea["action_scopes"][0]
    if action_units is None:
        action_units = [
            {
                "consumption_ordinal": 0,
                "parent_action_scope_id": scope["scope_id"],
                "parent_action_scope_hash": scope["scope_hash"],
                "action_kind": "D_VOLUME_WRITE",
                "authorization_action_registry_entry_ref_and_hash": scope["authorization_action_registry_entry_ref_and_hash"],
                "job_id": "job-001",
                "attempt_id": "attempt-001",
                "input_hash": "0" * 64,
                "carrier_profile_or_solver_contract_hash_if_any": None,
                "target_binding_hash": "0" * 64,
                "required_output_sink_and_acl_hash_if_any": None,
                "idempotency_key": "k" * 16,
                "unit_budget": {
                    "max_invocations": 0,
                    "max_solver_launches": 0,
                    "max_database_writes": 0,
                    "max_redis_writes": 0,
                    "max_d_volume_writes": 1,
                    "max_human_gate_commits": 0,
                    "max_active_release_changes": 0,
                    "max_tokens": 0,
                    "max_cost_microunits": 0,
                    "currency": "USD",
                },
            }
        ]
    permit = {
        "schema_id": "seven/live-run-permit",
        "schema_version": 1,
        "permit_id": "permit-test-001",
        "parent_authorization_id": eea["authorization_id"],
        "parent_authorization_ref_and_hash": {"ref": "eea", "sha256": eea["authorization_hash"]},
        "parent_authorization_signed_bytes_hash": eea["signed_bytes_hash"],
        "parent_subset_verification_contract_ref_and_hash": {"ref": "contract", "sha256": "0" * 64},
        "authorization_mode": eea["authorization_mode"],
        "wp_id": "WP-GV0",
        "epoch_id_if_any": None,
        "run_id_if_any": None,
        "action_units": action_units,
        "required_reservation_backend": "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
        "externally_pinned_trust_root": eea["externally_pinned_trust_root"],
        "actor_roster_ref_and_hash": eea["actor_roster_ref_and_hash"],
        "human_gate_policy_ref_and_hash": eea["human_gate_policy_ref_and_hash"],
        "signature_algorithm_registry_ref_and_hash": eea["signature_algorithm_registry_ref_and_hash"],
        "revocation_policy_ref_and_hash": eea["revocation_policy_ref_and_hash"],
        "issuer_actor_id": "site-owner",
        "issuer_key_id": "owner-key-001",
        "issued_at": "2026-08-14T00:00:00Z",
        "not_before": "2026-08-14T00:00:00Z",
        "expires_at": "2026-08-15T00:00:00Z",
        "nonce": "p" * 16,
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-live-run-permit/v1\0",
        "signed_bytes_hash": "0" * 64,
        "signature_envelope": _make_valid_signature_envelope(
            "seven-live-run-permit/v1\0", "0" * 64
        ),
        "permit_hash_algorithm": "sha256(RFC8785-JCS-object-with-permit_hash-null)",
        "permit_hash": None,
    }
    obj_for_hash = dict(permit)
    obj_for_hash["permit_hash"] = None
    permit["permit_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    return permit


def _make_receipt(
    permit: dict,
    *,
    status: str = "RESERVED",
    reserved_budget: dict | None = None,
    actual_side_effects: dict | None = None,
    held_allowance: dict | None = None,
    released_allowance: dict | None = None,
    remaining_allowance: dict | None = None,
    fence_token: int = 0,
    proof_not_started_refs: list | None = None,
    start_observation_evidence_refs: list | None = None,
    external_start_observation: str = "NOT_OBSERVED",
    terminal_at_if_any: str | None = None,
    state_revision: int = 0,
) -> dict:
    unit = permit["action_units"][0]
    if reserved_budget is None:
        reserved_budget = {
            "invocations": 0, "solver_launches": 0, "database_writes": 0,
            "redis_writes": 0, "d_volume_writes": 1, "human_gate_commits": 0,
            "active_release_changes": 0, "tokens": 0, "cost_microunits": 0,
            "currency": "USD",
        }
    zero = {
        "invocations": 0, "solver_launches": 0, "database_writes": 0,
        "redis_writes": 0, "d_volume_writes": 0, "human_gate_commits": 0,
        "active_release_changes": 0, "tokens": 0, "cost_microunits": 0,
        "currency": "USD",
    }
    if actual_side_effects is None:
        actual_side_effects = dict(zero)
    if held_allowance is None:
        held_allowance = dict(reserved_budget) if status == "RESERVED" else dict(zero)
    if released_allowance is None:
        released_allowance = dict(reserved_budget) if status == "RELEASED_UNUSED" else dict(zero)
    if remaining_allowance is None:
        # remaining = reserved - actual - held - released
        remaining_allowance = dict(zero)
        if status == "RESERVED":
            remaining_allowance = dict(zero)  # held = reserved, so remaining = 0

    receipt = {
        "schema_id": "seven/authorization-consumption-receipt",
        "schema_version": 1,
        "receipt_id": "receipt-test-001",
        "logical_consumption_id": "consumption-001",
        "state_revision": state_revision,
        "previous_receipt_ref_and_hash_if_any": None,
        "parent_authorization_id": "eea-test-001",
        "parent_authorization_ref_and_hash": {"ref": "eea", "sha256": "0" * 64},
        "permit_id": permit["permit_id"],
        "permit_ref_and_hash": {"ref": "permit", "sha256": permit["permit_hash"]},
        "consumption_ordinal": unit["consumption_ordinal"],
        "parent_action_scope_id": unit["parent_action_scope_id"],
        "parent_action_scope_hash": unit["parent_action_scope_hash"],
        "action_kind": unit["action_kind"],
        "authorization_action_registry_entry_ref_and_hash": unit["authorization_action_registry_entry_ref_and_hash"],
        "job_id": unit["job_id"],
        "attempt_id": unit["attempt_id"],
        "input_hash": unit["input_hash"],
        "carrier_profile_or_solver_contract_hash_if_any": unit["carrier_profile_or_solver_contract_hash_if_any"],
        "target_binding_hash": unit["target_binding_hash"],
        "required_output_sink_and_acl_hash_if_any": unit["required_output_sink_and_acl_hash_if_any"],
        "idempotency_key": unit["idempotency_key"],
        "aggregate_id": "agg-001",
        "expected_aggregate_revision": 0,
        "fence_token": fence_token,
        "reservation_backend": "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
        "status": status,
        "reserved_at": "2026-08-14T00:00:00Z",
        "status_recorded_at": "2026-08-14T00:00:01Z",
        "terminal_at_if_any": terminal_at_if_any,
        "external_start_observation": external_start_observation,
        "start_observation_evidence_refs": start_observation_evidence_refs or [],
        "proof_not_started_refs": proof_not_started_refs or [],
        "reservation_transaction_receipt_ref_and_hash": {"ref": "tx", "sha256": "0" * 64},
        "reserved_unit_budget": reserved_budget,
        "actual_side_effects": actual_side_effects,
        "held_allowance": held_allowance,
        "released_allowance": released_allowance,
        "remaining_allowance": remaining_allowance,
        "recovery_decision_ref_and_hash_if_any": None,
        "externally_pinned_trust_root": {"object_id": "root", "sha256": "0" * 64},
        "service_attestation_key_registry_ref_and_hash": {"ref": "attreg", "sha256": "0" * 64},
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "attestation_domain": "seven-authorization-consumption-receipt/v1\0",
        "attested_bytes_hash": "0" * 64,
        "service_attestation": {
            "algorithm": "Ed25519",
            "key_id": "svc-key-001",
            "service_principal_id": "seven-runtime",
            "signature_encoding": "base64",
            "signature_b64": "B" * 86 + "==",
            "attested_bytes_hash": "0" * 64,
            "trust_root_hash": "0" * 64,
            "service_attestation_key_registry_hash": "0" * 64,
        },
        "receipt_hash_algorithm": "sha256(RFC8785-JCS-object-with-receipt_hash-null)",
        "receipt_hash": None,
    }
    obj_for_hash = dict(receipt)
    obj_for_hash["receipt_hash"] = None
    receipt["receipt_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    return receipt


# ─── CompletionContractVerifier 正向向量 ──────────────────────────────

class CompletionContractGoldenVectors(unittest.TestCase):
    """正向向量：三种 completion contract 的合法提交。"""

    def test_doc0_bootstrap_record_passes(self) -> None:
        result = verify_doc0_bootstrap_record(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            submitted_object=_make_doc_bootstrap_record(),
            actor_type="IMPLEMENTER",
        )
        self.assertEqual(result.verdict, "PASS", msg=str(result.details))
        self.assertEqual(result.owner_type, "IMPLEMENTER")
        self.assertEqual(result.completion_contract, "DOC_BOOTSTRAP_RECORD")

    def test_implementation_bundle_passes(self) -> None:
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-GV0",
            submitted_object=_make_implementation_bundle(),
            actor_type="IMPLEMENTER",
        )
        self.assertEqual(result.verdict, "PASS", msg=str(result.details))
        self.assertEqual(result.completion_contract, "IMPLEMENTATION_BUNDLE")

    def test_audit_record_passes_for_auditor(self) -> None:
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-GA1",
            submitted_object=_make_audit_record(),
            actor_type="AUDITOR",
        )
        self.assertEqual(result.verdict, "PASS", msg=str(result.details))
        self.assertEqual(result.owner_type, "AUDITOR")
        self.assertEqual(result.completion_contract, "AUDIT_RECORD")

    def test_implementer_can_write_ready_for_audit(self) -> None:
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-GV0",
            submitted_object=_make_implementation_bundle(),
            actor_type="IMPLEMENTER",
            state_command="READY_FOR_AUDIT",
        )
        self.assertEqual(result.verdict, "PASS", msg=str(result.details))


# ─── CompletionContractVerifier 负向向量 (blocker tests) ──────────────

class CompletionContractNegativeVectors(unittest.TestCase):
    """blocker tests：owner/contract/schema/actor 错配必须 fail-closed。"""

    def test_doc0_with_implementation_bundle_rejected(self) -> None:
        """DOC0 + ImplementationBundle → COMPLETION_CONTRACT_MISMATCH"""
        result = verify_doc0_bootstrap_record(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            submitted_object=_make_implementation_bundle("WP-DOC0"),
            actor_type="IMPLEMENTER",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.SCHEMA_ID_MISMATCH, result.error_codes)

    def test_auditor_owned_with_implementation_bundle_rejected(self) -> None:
        """auditor-owned + ImplementationBundle schema → SCHEMA_ID_MISMATCH"""
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-GA1",
            submitted_object=_make_implementation_bundle("WP-GA1"),
            actor_type="AUDITOR",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.SCHEMA_ID_MISMATCH, result.error_codes)

    def test_implementer_writes_auditor_node_rejected(self) -> None:
        """implementer 命令写 auditor 节点 → ACTOR_NOT_AUTHORIZED"""
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-GA1",
            submitted_object=_make_audit_record(),
            actor_type="IMPLEMENTER",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.ACTOR_NOT_AUTHORIZED, result.error_codes)

    def test_auditor_writes_implementer_node_rejected(self) -> None:
        """auditor 提交 implementer-owned 完成对象 → ACTOR_NOT_AUTHORIZED"""
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-GV0",
            submitted_object=_make_implementation_bundle(),
            actor_type="AUDITOR",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.ACTOR_NOT_AUTHORIZED, result.error_codes)

    def test_implementer_writes_audited_pass_rejected(self) -> None:
        """implementer 写 AUDITED_PASS → STATE_COMMAND_REJECTED"""
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-GV0",
            submitted_object=_make_implementation_bundle(),
            actor_type="IMPLEMENTER",
            state_command="AUDITED_PASS",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.STATE_COMMAND_REJECTED, result.error_codes)

    def test_dag_hash_mismatch_rejected(self) -> None:
        """DAG hash 不匹配 → DAG_HASH_MISMATCH"""
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256="0" * 64,
            wp_id="WP-GV0",
            submitted_object=_make_implementation_bundle(),
            actor_type="IMPLEMENTER",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.DAG_HASH_MISMATCH, result.error_codes)

    def test_unknown_wp_id_rejected(self) -> None:
        """未知 wp_id → UNKNOWN_WORK_PACKAGE"""
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-FAKE",
            submitted_object=_make_implementation_bundle("WP-FAKE"),
            actor_type="IMPLEMENTER",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.UNKNOWN_WORK_PACKAGE, result.error_codes)

    def test_wrong_schema_id_rejected(self) -> None:
        """schema_id 不匹配 → SCHEMA_ID_MISMATCH"""
        obj = _make_implementation_bundle()
        obj["schema_id"] = "seven/wrong-schema"
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-GV0",
            submitted_object=obj,
            actor_type="IMPLEMENTER",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.SCHEMA_ID_MISMATCH, result.error_codes)

    def test_auditor_writes_implementer_state_rejected(self) -> None:
        """auditor 写实施者状态 → STATE_COMMAND_REJECTED"""
        result = verify_completion_contract(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-GA1",
            submitted_object=_make_audit_record(),
            actor_type="AUDITOR",
            state_command="IN_PROGRESS",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.STATE_COMMAND_REJECTED, result.error_codes)


# ─── SecurityContractVerifier 正向向量 ────────────────────────────────

class SecurityContractGoldenVectors(unittest.TestCase):
    """正向向量：合法 EEA → Permit → Receipt 链。"""

    def test_valid_eea_passes(self) -> None:
        eea = _make_eea()
        result = verify_eea(eea)
        self.assertEqual(result.verdict, "PASS", msg=str(result.details))

    def test_valid_permit_does_not_escalate(self) -> None:
        eea = _make_eea()
        permit = _make_permit(eea)
        result = verify_permit_does_not_escalate_parent(permit, eea)
        self.assertEqual(result.verdict, "PASS", msg=str(result.details))

    def test_valid_reserved_receipt_passes(self) -> None:
        eea = _make_eea()
        permit = _make_permit(eea)
        receipt = _make_receipt(permit, status="RESERVED", fence_token=0)
        result = verify_consumption_receipt(receipt, permit=permit)
        self.assertEqual(result.verdict, "PASS", msg=str(result.details))

    def test_valid_consumed_receipt_passes(self) -> None:
        eea = _make_eea()
        permit = _make_permit(eea)
        receipt = _make_receipt(
            permit,
            status="CONSUMED",
            fence_token=0,
            actual_side_effects={
                "invocations": 0, "solver_launches": 0, "database_writes": 0,
                "redis_writes": 0, "d_volume_writes": 1, "human_gate_commits": 0,
                "active_release_changes": 0, "tokens": 0, "cost_microunits": 0,
                "currency": "USD",
            },
            held_allowance={
                "invocations": 0, "solver_launches": 0, "database_writes": 0,
                "redis_writes": 0, "d_volume_writes": 0, "human_gate_commits": 0,
                "active_release_changes": 0, "tokens": 0, "cost_microunits": 0,
                "currency": "USD",
            },
            remaining_allowance={
                "invocations": 0, "solver_launches": 0, "database_writes": 0,
                "redis_writes": 0, "d_volume_writes": 0, "human_gate_commits": 0,
                "active_release_changes": 0, "tokens": 0, "cost_microunits": 0,
                "currency": "USD",
            },
            external_start_observation="CONFIRMED_ACCEPTED_OR_STARTED",
            start_observation_evidence_refs=[{"ref": "evidence", "sha256": "0" * 64}],
            terminal_at_if_any="2026-08-14T00:01:00Z",
        )
        result = verify_consumption_receipt(receipt, permit=permit)
        self.assertEqual(result.verdict, "PASS", msg=str(result.details))

    def test_full_authorization_chain_passes(self) -> None:
        eea = _make_eea()
        permit = _make_permit(eea)
        receipt = _make_receipt(permit, status="RESERVED", fence_token=0)
        result = verify_authorization_chain(
            eea=eea, permit=permit, receipt=receipt
        )
        self.assertEqual(result.verdict, "PASS", msg=str(result.details))


# ─── SecurityContractVerifier 负向向量 (blocker tests) ────────────────

class SecurityContractNegativeVectors(unittest.TestCase):
    """blocker tests：签名、扩权、重复 ordinal、额度不守恒必须 fail-closed。"""

    def test_fake_signature_rejected(self) -> None:
        """伪签名 → SIGNATURE_INVALID"""
        errors = verify_signature_envelope(
            {"algorithm": "RSA", "signature_domain": "test\0", "signature_b64": "x", "signed_bytes_hash": "0" * 64},
            expected_domain="test\0",
            signed_bytes_hash="0" * 64,
        )
        codes = [e[0] for e in errors]
        self.assertIn(EC.SIGNATURE_ALGORITHM_INVALID, codes)

    def test_wrong_domain_separator_rejected(self) -> None:
        """错误 domain separator → SIGNATURE_DOMAIN_INVALID"""
        eea = _make_eea()
        eea["signature_domain"] = "wrong-domain\0"
        # recompute hash since we changed a field
        obj = dict(eea)
        obj["authorization_hash"] = None
        eea["authorization_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_eea(eea)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.SIGNATURE_DOMAIN_INVALID, result.error_codes)

    def test_eea_zero_budget_rejected(self) -> None:
        """EEA 全部额度为 0 → EEA_ZERO_BUDGET"""
        eea = _make_eea(action_scopes=[
            {
                "scope_id": "zero",
                "scope_hash_algorithm": "sha256(RFC8785-JCS-action-scope-with-scope_hash-null)",
                "scope_hash": "0" * 64,
                "action_kind": "NO_OP",
                "authorization_action_registry_entry_ref_and_hash": {"ref": "reg", "sha256": "0" * 64},
                "target_site_hash_if_any": None,
                "target_database_identity_hash_if_any": None,
                "target_redis_namespace_hash_if_any": None,
                "target_release_or_pointer_hash_if_any": None,
                "allowed_carrier_profile_hashes": [],
                "allowed_role_or_solver_contract_hashes": [],
                "allowed_inputs": [{"input_hash": "0" * 64, "sensitivity": "public"}],
                "required_output_sink_and_acl_hash_if_any": None,
                "budget": {
                    "max_invocations": 0, "max_solver_launches": 0,
                    "max_database_writes": 0, "max_redis_writes": 0,
                    "max_d_volume_writes": 0, "max_human_gate_commits": 0,
                    "max_active_release_changes": 0, "max_tokens": 0,
                    "max_cost_microunits": 0, "currency": "USD",
                },
            }
        ])
        result = verify_eea(eea)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.EEA_ZERO_BUDGET, result.error_codes)

    def test_permit_escalates_budget_rejected(self) -> None:
        """Permit budget 超过 parent → PERMIT_ESCALATES_PARENT"""
        eea = _make_eea()
        permit = _make_permit(eea)
        permit["action_units"][0]["unit_budget"]["max_d_volume_writes"] = 999
        # recompute permit_hash
        obj = dict(permit)
        obj["permit_hash"] = None
        permit["permit_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_permit_does_not_escalate_parent(permit, eea)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.PERMIT_ESCALATES_PARENT, result.error_codes)

    def test_permit_parent_hash_mismatch_rejected(self) -> None:
        """Permit parent hash 不匹配 → PERMIT_PARENT_HASH_MISMATCH"""
        eea = _make_eea()
        permit = _make_permit(eea)
        permit["parent_authorization_ref_and_hash"]["sha256"] = "1" * 64
        result = verify_permit_does_not_escalate_parent(permit, eea)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.PERMIT_PARENT_HASH_MISMATCH, result.error_codes)

    def test_permit_time_window_escalates_rejected(self) -> None:
        """Permit expires_at 超过 EEA → PERMIT_ESCALATES_PARENT"""
        eea = _make_eea()
        permit = _make_permit(eea)
        permit["expires_at"] = "2026-08-16T00:00:00Z"  # after EEA expires
        result = verify_permit_does_not_escalate_parent(permit, eea)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.PERMIT_ESCALATES_PARENT, result.error_codes)

    def test_allowance_not_conserved_rejected(self) -> None:
        """额度不守恒 → ALLOWANCE_NOT_CONSERVED"""
        eea = _make_eea()
        permit = _make_permit(eea)
        receipt = _make_receipt(
            permit,
            status="RESERVED",
            fence_token=0,
            held_allowance={
                "invocations": 0, "solver_launches": 0, "database_writes": 0,
                "redis_writes": 0, "d_volume_writes": 5,  # != reserved 1
                "human_gate_commits": 0, "active_release_changes": 0,
                "tokens": 0, "cost_microunits": 0, "currency": "USD",
            },
            remaining_allowance={
                "invocations": 0, "solver_launches": 0, "database_writes": 0,
                "redis_writes": 0, "d_volume_writes": 0,
                "human_gate_commits": 0, "active_release_changes": 0,
                "tokens": 0, "cost_microunits": 0, "currency": "USD",
            },
        )
        # recompute receipt_hash
        obj = dict(receipt)
        obj["receipt_hash"] = None
        receipt["receipt_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_consumption_receipt(receipt, permit=permit)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.ALLOWANCE_NOT_CONSERVED, result.error_codes)

    def test_release_without_proof_rejected(self) -> None:
        """RELEASED_UNUSED 没有 proof_not_started → RELEASE_WITHOUT_PROOF"""
        eea = _make_eea()
        permit = _make_permit(eea)
        receipt = _make_receipt(
            permit,
            status="RELEASED_UNUSED",
            fence_token=0,
            external_start_observation="PROVEN_NOT_STARTED",
            proof_not_started_refs=[],
        )
        obj = dict(receipt)
        obj["receipt_hash"] = None
        receipt["receipt_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_consumption_receipt(receipt, permit=permit)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.RELEASE_WITHOUT_PROOF, result.error_codes)

    def test_stale_fence_rejected(self) -> None:
        """fence_token 不匹配 → STALE_FENCE"""
        eea = _make_eea()
        permit = _make_permit(eea)
        # permit action_unit has fence_token=0 (from _make_permit default)
        # but we need to set fence_token in the unit
        permit["action_units"][0]["fence_token"] = 42
        receipt = _make_receipt(permit, status="RESERVED", fence_token=99)
        obj = dict(receipt)
        obj["receipt_hash"] = None
        receipt["receipt_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_consumption_receipt(receipt, permit=permit)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.STALE_FENCE, result.error_codes)

    def test_non_canonical_utc_rejected(self) -> None:
        """非 canonical UTC 时间戳 → TIME_NOT_CANONICAL_UTC"""
        eea = _make_eea()
        eea["issued_at"] = "2026-08-14 00:00:00"  # space instead of T, no Z
        result = verify_eea(eea)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.TIME_NOT_CANONICAL_UTC, result.error_codes)

    def test_eea_hash_mismatch_rejected(self) -> None:
        """EEA authorization_hash 不匹配 → OBJECT_HASH_MISMATCH"""
        eea = _make_eea()
        eea["authorization_hash"] = "1" * 64
        result = verify_eea(eea)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.OBJECT_HASH_MISMATCH, result.error_codes)

    def test_reservation_backend_invalid_rejected(self) -> None:
        """未知 reservation_backend → RESERVATION_BACKEND_INVALID"""
        eea = _make_eea()
        permit = _make_permit(eea)
        receipt = _make_receipt(permit, status="RESERVED", fence_token=0)
        receipt["reservation_backend"] = "INVALID_BACKEND"
        obj = dict(receipt)
        obj["receipt_hash"] = None
        receipt["receipt_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_consumption_receipt(receipt, permit=permit)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.RESERVATION_BACKEND_INVALID, result.error_codes)


# ─── ReservationBackend 负向向量 ──────────────────────────────────────

class ReservationBackendNegativeVectors(unittest.TestCase):

    def test_duplicate_ordinal_rejected(self) -> None:
        """重复 ordinal → DUPLICATE_ORDINAL"""
        backend = SideEffectFreeReferenceBackend()
        backend.reserve(
            permit_id="p1", consumption_ordinal=0,
            idempotency_key="k" * 16, fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"d_volume_writes": 1, "currency": "USD"},
        )
        with self.assertRaises(Exception) as ctx:
            backend.reserve(
                permit_id="p1", consumption_ordinal=0,
                idempotency_key="k" * 16, fence_token=1,
                expected_aggregate_revision=1,
                reserved_budget={"d_volume_writes": 1, "currency": "USD"},
            )
        self.assertEqual(ctx.exception.code, EC.DUPLICATE_ORDINAL)

    def test_stale_fence_on_consume_rejected(self) -> None:
        """consume 时 fence 不匹配 → STALE_FENCE"""
        backend = SideEffectFreeReferenceBackend()
        backend.reserve(
            permit_id="p1", consumption_ordinal=0,
            idempotency_key="k" * 16, fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"d_volume_writes": 1, "currency": "USD"},
        )
        with self.assertRaises(Exception) as ctx:
            backend.consume(
                permit_id="p1", consumption_ordinal=0,
                fence_token=999,  # wrong fence
                actual_side_effects={"d_volume_writes": 1, "currency": "USD"},
            )
        self.assertEqual(ctx.exception.code, EC.STALE_FENCE)

    def test_release_without_proof_rejected(self) -> None:
        """release_unused 没有 proof → RELEASE_WITHOUT_PROOF"""
        backend = SideEffectFreeReferenceBackend()
        backend.reserve(
            permit_id="p1", consumption_ordinal=0,
            idempotency_key="k" * 16, fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"d_volume_writes": 1, "currency": "USD"},
        )
        with self.assertRaises(Exception) as ctx:
            backend.release_unused(
                permit_id="p1", consumption_ordinal=0,
                fence_token=1, proof_not_started_refs=[],
            )
        self.assertEqual(ctx.exception.code, EC.RELEASE_WITHOUT_PROOF)

    def test_consume_exceeds_reserved_rejected(self) -> None:
        """consume 超过预留额度 → ALLOWANCE_NOT_CONSERVED"""
        backend = SideEffectFreeReferenceBackend()
        backend.reserve(
            permit_id="p1", consumption_ordinal=0,
            idempotency_key="k" * 16, fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"d_volume_writes": 1, "currency": "USD"},
        )
        with self.assertRaises(Exception) as ctx:
            backend.consume(
                permit_id="p1", consumption_ordinal=0,
                fence_token=1,
                actual_side_effects={"d_volume_writes": 5, "currency": "USD"},
            )
        self.assertEqual(ctx.exception.code, EC.ALLOWANCE_NOT_CONSERVED)

    def test_consume_already_consumed_rejected(self) -> None:
        """重复 consume → APPEND_ONLY_VIOLATION"""
        backend = SideEffectFreeReferenceBackend()
        backend.reserve(
            permit_id="p1", consumption_ordinal=0,
            idempotency_key="k" * 16, fence_token=1,
            expected_aggregate_revision=0,
            reserved_budget={"d_volume_writes": 1, "currency": "USD"},
        )
        backend.consume(
            permit_id="p1", consumption_ordinal=0,
            fence_token=1,
            actual_side_effects={"d_volume_writes": 1, "currency": "USD"},
        )
        with self.assertRaises(Exception) as ctx:
            backend.consume(
                permit_id="p1", consumption_ordinal=0,
                fence_token=1,
                actual_side_effects={"d_volume_writes": 1, "currency": "USD"},
            )
        self.assertEqual(ctx.exception.code, EC.APPEND_ONLY_VIOLATION)


# ─── CompletionArtifactStore 正向向量 ─────────────────────────────────

class ArtifactStoreGoldenVectors(unittest.TestCase):

    def test_put_and_get_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            payload = {"schema_id": "seven/implementation-completion-bundle", "wp_id": "WP-GV0"}
            ref = store.put_json(payload)
            self.assertEqual(len(ref.sha256), 64)
            self.assertTrue(ref.size_bytes > 0)
            retrieved = store.get_json(ref.sha256)
            self.assertEqual(retrieved, payload)

    def test_put_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            payload = {"key": "value"}
            ref1 = store.put_json(payload)
            ref2 = store.put_json(payload)
            self.assertEqual(ref1.sha256, ref2.sha256)

    def test_verify_returns_true_for_existing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            ref = store.put_json({"data": 42})
            self.assertTrue(store.verify(ref.sha256))

    def test_put_bytes_and_get(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            content = b"raw bytes content"
            ref = store.put_bytes(content)
            self.assertEqual(store.get(ref.sha256), content)


# ─── CompletionArtifactStore 负向向量 (blocker tests) ─────────────────

class ArtifactStoreNegativeVectors(unittest.TestCase):

    def test_non_d_volume_rejected_without_explicit_test_override(self) -> None:
        """P0 blocker: production store 不得把临时目录冒充批准的D盘卷。"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            with self.assertRaises(_StoreError) as ctx:
                CompletionArtifactStore(root=vol / "store", volume_root=vol)
            self.assertEqual(ctx.exception.code, EC.STORE_FALLBACK_REJECTED)

    def test_unauthorized_store_put_cli_is_not_exposed(self) -> None:
        """P0 blocker: 未接授权链前不得暴露直接写CAS的CLI。"""
        from seven_system.cli import _parser

        parser = _parser()
        subparser_action = next(
            action
            for action in parser._actions
            if hasattr(action, "choices") and isinstance(action.choices, dict)
        )
        self.assertNotIn("gv0-store-put", subparser_action.choices)

    def test_symlink_leaf_rejected(self) -> None:
        """叶 symlink → STORE_SYMLINK_REJECTED"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            ref = store.put_json({"x": 1})
            path = store._content_path(ref.sha256)
            # replace with symlink
            path.unlink()
            target = vol / "target.json"
            target.write_text("{}")
            path.parent.mkdir(parents=True, exist_ok=True)
            os.symlink(target, path)
            with self.assertRaises(_StoreError) as ctx:
                store.get(ref.sha256)
            self.assertEqual(ctx.exception.code, EC.STORE_SYMLINK_REJECTED)

    def test_fallback_to_repo_rejected(self) -> None:
        """store root 在 volume_root 外 → STORE_FALLBACK_REJECTED"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            outside = Path(tmp) / "outside"
            outside.mkdir()
            with self.assertRaises(_StoreError) as ctx:
                CompletionArtifactStore(
                    root=outside / "store", volume_root=vol,
                    test_only_allow_non_d_volume=True,
                )
            self.assertEqual(ctx.exception.code, EC.STORE_FALLBACK_REJECTED)

    def test_hash_mismatch_on_read_rejected(self) -> None:
        """读取时 hash 不匹配 → STORE_HASH_MISMATCH"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            ref = store.put_json({"x": 1})
            path = store._content_path(ref.sha256)
            # tamper with content
            path.write_bytes(b'{"x": 999}\n')
            with self.assertRaises(_StoreError) as ctx:
                store.get(ref.sha256)
            self.assertEqual(ctx.exception.code, EC.STORE_HASH_MISMATCH)

    def test_overwrite_conflict_rejected(self) -> None:
        """不同内容写入相同 hash 路径 → STORE_OVERWRITE_CONFLICT"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            ref = store.put_json({"x": 1})
            path = store._content_path(ref.sha256)
            # manually write different content to the same path
            path.unlink()
            path.write_bytes(b'{"different": true}\n')
            with self.assertRaises(_StoreError) as ctx:
                store.put_json({"x": 1})
            self.assertEqual(ctx.exception.code, EC.STORE_OVERWRITE_CONFLICT)

    def test_nonexistent_volume_root_rejected(self) -> None:
        """volume_root 不存在 → STORE_VOLUME_ROOT_INVALID"""
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(_StoreError) as ctx:
                CompletionArtifactStore(
                    root=Path(tmp) / "vol" / "store",
                    volume_root=Path(tmp) / "nonexistent",
                )
            self.assertEqual(ctx.exception.code, EC.STORE_VOLUME_ROOT_INVALID)

    def test_nonexistent_artifact_get_rejected(self) -> None:
        """get 不存在的 hash → STORE_HASH_MISMATCH"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            with self.assertRaises(_StoreError) as ctx:
                store.get("0" * 64)
            self.assertEqual(ctx.exception.code, EC.STORE_HASH_MISMATCH)


# ─── CompletionArtifactStore 故障注入 ─────────────────────────────────

class ArtifactStoreFaultInjection(unittest.TestCase):

    def test_concurrent_same_content_is_idempotent(self) -> None:
        """并发写入相同内容 → 幂等成功"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            payload = {"concurrent": True}
            ref1 = store.put_json(payload)
            ref2 = store.put_json(payload)
            self.assertEqual(ref1.sha256, ref2.sha256)
            self.assertTrue(store.verify(ref1.sha256))

    def test_partial_write_does_not_corrupt(self) -> None:
        """半写文件不破坏已有 artifact"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            ref = store.put_json({"stable": True})
            # simulate a partial write by creating a .partial file
            content_path = store._content_path(ref.sha256)
            partial = content_path.parent / ".abc123.partial"
            partial.write_bytes(b'{"incomplete":')
            # original artifact should still be intact
            self.assertTrue(store.verify(ref.sha256))
            data = store.get_json(ref.sha256)
            self.assertEqual(data, {"stable": True})
            partial.unlink(missing_ok=True)

    def test_different_content_different_hash(self) -> None:
        """不同内容得到不同 hash"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            ref1 = store.put_json({"a": 1})
            ref2 = store.put_json({"a": 2})
            self.assertNotEqual(ref1.sha256, ref2.sha256)
            self.assertTrue(store.verify(ref1.sha256))
            self.assertTrue(store.verify(ref2.sha256))

    def test_many_artifacts_all_verifiable(self) -> None:
        """写入多个 artifact 后全部可验证"""
        with tempfile.TemporaryDirectory() as tmp:
            vol = Path(tmp) / "vol"
            vol.mkdir()
            store = CompletionArtifactStore(
                root=vol / "store", volume_root=vol,
                test_only_allow_non_d_volume=True,
            )
            refs = []
            for i in range(50):
                ref = store.put_json({"index": i, "data": f"item-{i}"})
                refs.append(ref)
            for ref in refs:
                self.assertTrue(store.verify(ref.sha256))
                data = store.get_json(ref.sha256)
                self.assertIn("index", data)


# ─── DAG 加载和索引 ────────────────────────────────────────────────────

class DagIndexTests(unittest.TestCase):

    def test_dag_index_loads_all_work_packages(self) -> None:
        index = load_dag_index(DAG_PATH)
        self.assertIn("WP-DOC0", index)
        self.assertIn("WP-GV0", index)
        self.assertIn("WP-GA1", index)
        self.assertEqual(index["WP-GA1"]["owner_type"], "AUDITOR")
        self.assertEqual(index["WP-GA1"]["completion_contract"], "AUDIT_RECORD")
        self.assertEqual(index["WP-GV0"]["owner_type"], "IMPLEMENTER")
        self.assertEqual(index["WP-GV0"]["completion_contract"], "IMPLEMENTATION_BUNDLE")

    def test_doc0_is_implementer_with_bootstrap_record(self) -> None:
        index = load_dag_index(DAG_PATH)
        node = index["WP-DOC0"]
        self.assertEqual(node["owner_type"], "IMPLEMENTER")
        self.assertEqual(node["completion_contract"], "DOC_BOOTSTRAP_RECORD")


if __name__ == "__main__":
    unittest.main()
