"""WP-VLT0 Vault 访问链测试。

测试层级：Golden → Negative → Fault injection
覆盖：
- VaultAccessCapability 验证
- AccessDecision 验证
- ViewDerivation 验证
- AccessEvent ledger 完整性
- VaultBroker 完整访问链编排
- Artifact seal 协议 (live→partial→seal)
- CAS/DB reconcile
- CAS 核心复用强制（禁止第二套 store）

所有 blocker test 失败 → 工作包 FAIL。
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import VerificationErrorCode as EC
from seven_system.hashing import canonical_json_bytes
from seven_system.storage.artifact_store import CompletionArtifactStore, ArtifactRef
from seven_system.storage.artifact_seal import (
    ArtifactSealProtocol,
    CommitIntent,
    ArtifactManifest,
)
from seven_system.storage.reconcile import (
    ArtifactReconciler,
    DBArtifactRecord,
)
from seven_system.vault.sensitivity import (
    SensitivityLevel,
    SensitivityRegistry,
    VaultObjectRecord,
)
from seven_system.vault.access_capability import (
    verify_vault_access_capability,
)
from seven_system.vault.access_decision import (
    verify_access_decision,
)
from seven_system.vault.view_derivation import (
    verify_view_derivation,
)
from seven_system.vault.access_event import (
    verify_access_event,
    AccessEventLedger,
)
from seven_system.vault.broker import VaultBroker


# ─── helpers ───────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64
_SIG_B64 = "A" * 86 + "=="


def _make_principal(*, principal_type: str = "TARGET_SOLVER") -> dict:
    if principal_type == "TARGET_SOLVER":
        return {
            "principal_id": "solver-001",
            "principal_type": "TARGET_SOLVER",
            "role_type_id": None,
            "carrier_profile_sha256": None,
            "target_solver_contract_sha256": _ZERO_HASH,
            "execution_attempt_id": "attempt-001",
        }
    elif principal_type == "MODEL_ROLE":
        return {
            "principal_id": "model-001",
            "principal_type": "MODEL_ROLE",
            "role_type_id": "role-001",
            "carrier_profile_sha256": _ZERO_HASH,
            "target_solver_contract_sha256": None,
            "execution_attempt_id": "attempt-001",
        }
    elif principal_type == "SERVICE":
        return {
            "principal_id": "service-001",
            "principal_type": "SERVICE",
            "role_type_id": None,
            "carrier_profile_sha256": None,
            "target_solver_contract_sha256": None,
            "execution_attempt_id": None,
        }
    return {
        "principal_id": "human-001",
        "principal_type": principal_type,
        "role_type_id": None,
        "carrier_profile_sha256": None,
        "target_solver_contract_sha256": None,
        "execution_attempt_id": None,
    }


def _make_object_binding(*, sensitivity: str = "PUBLIC", object_id: str = "obj-001") -> dict:
    return {
        "object_id": object_id,
        "object_sha256": _ZERO_HASH,
        "sensitivity": sensitivity,
    }


def _make_view_binding(*, view_id: str = "view-001") -> dict:
    return {
        "view_id": view_id,
        "view_sha256": _ZERO_HASH,
        "view_policy_sha256": _ZERO_HASH,
    }


def _make_sink_binding(*, sink_kind: str = "EPHEMERAL_MODEL_INPUT", sink_id: str = "sink-001") -> dict:
    return {
        "sink_id": sink_id,
        "sink_kind": sink_kind,
        "sink_policy_sha256": _ZERO_HASH,
    }


def _make_issuer() -> dict:
    return {
        "issuer_principal_id": "vault-issuer-001",
        "issuer_key_id": "key-001",
        "issuer_public_key_sha256": _ZERO_HASH,
    }


def _make_revocation(*, handle: str = "revoc-001") -> dict:
    return {
        "revocable": True,
        "revocation_handle": handle,
        "status_at_issue": "ACTIVE",
        "registry_ref_and_hash": {"ref_id": "revoc-reg-001", "sha256": _ZERO_HASH},
    }


def _make_signature_envelope(signed_bytes_hash: str = _ZERO_HASH) -> dict:
    return {
        "algorithm": "Ed25519",
        "key_id": "key-001",
        "signer_principal_id": "vault-issuer-001",
        "signature_encoding": "base64",
        "signature_b64": _SIG_B64,
        "signed_bytes_hash": signed_bytes_hash,
        "trust_root_hash": _ZERO_HASH,
        "issuer_key_registry_hash": _ZERO_HASH,
    }


def _make_capability(
    *,
    operation: str = "READ_DERIVED_VIEW",
    principal_type: str = "TARGET_SOLVER",
    sensitivity: str = "PUBLIC",
    sink_kind: str = "EPHEMERAL_MODEL_INPUT",
    deny_by_default: bool = True,
    raw_vault_path_disclosure: bool = False,
    nonce: str = "nonce-aaaaaaaaaaaaaaaa",
    not_before: str = "2026-08-14T00:00:00Z",
    expires_at: str = "2026-08-15T00:00:00Z",
    revocation_handle: str = "revoc-001",
    capability_id: str = "cap-001",
) -> dict:
    cap = {
        "schema_id": "seven/vault-access-capability",
        "schema_version": 1,
        "object_type": "VaultAccessCapability",
        "capability_id": capability_id,
        "principal": _make_principal(principal_type=principal_type),
        "operation": operation,
        "object_binding": _make_object_binding(sensitivity=sensitivity),
        "view_binding": _make_view_binding(),
        "sink_binding": _make_sink_binding(sink_kind=sink_kind),
        "access_policy_ref_and_hash": {"ref_id": "policy-001", "sha256": _ZERO_HASH},
        "deny_by_default": deny_by_default,
        "raw_vault_path_disclosure": raw_vault_path_disclosure,
        "issued_at": "2026-08-14T00:00:00Z",
        "not_before": not_before,
        "expires_at": expires_at,
        "nonce": nonce,
        "issuer": _make_issuer(),
        "revocation": _make_revocation(handle=revocation_handle),
        "externally_pinned_trust_root": {"object_id": "trust-root-001", "sha256": _ZERO_HASH},
        "issuer_key_registry_ref_and_hash": {"ref_id": "keyreg-001", "sha256": _ZERO_HASH},
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-vault-access-capability/v1\0",
        "signed_bytes_hash": _ZERO_HASH,
        "signature_envelope": _make_signature_envelope(),
        "capability_hash_algorithm": "sha256(RFC8785-JCS-object-with-capability_hash-null)",
        "capability_hash": None,
    }
    obj_for_hash = dict(cap)
    obj_for_hash["capability_hash"] = None
    cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    return cap


def _make_decision(
    *,
    capability: dict | None = None,
    decision: str = "ALLOW",
    reason_codes: list[str] | None = None,
    checks_pass: bool = True,
    revocation_status: str = "ACTIVE",
    evaluated_at: str = "2026-08-14T12:00:00Z",
    access_request_id: str = "req-001",
    nonce: str = "nonce-aaaaaaaaaaaaaaaa",
) -> dict:
    cap = capability or _make_capability()
    check_value = "PASS" if checks_pass else "FAIL"
    checks = {
        "capability_signature": check_value,
        "issuer_trust": check_value,
        "time_window": check_value,
        "principal": check_value,
        "operation": check_value,
        "object_hash": check_value,
        "view_hash": check_value,
        "sink": check_value,
        "nonce_replay": check_value,
        "access_policy": check_value,
    }
    if reason_codes is None:
        reason_codes = ["POLICY_ALLOW"] if decision == "ALLOW" else ["POLICY_DENY"]

    dec = {
        "schema_id": "seven/access-decision",
        "schema_version": 1,
        "object_type": "AccessDecision",
        "decision_id": f"dec-{access_request_id}",
        "access_request_id": access_request_id,
        "capability_ref_and_hash": {"ref_id": cap["capability_id"], "sha256": cap["capability_hash"]},
        "principal": cap["principal"],
        "operation": cap["operation"],
        "object_binding": cap["object_binding"],
        "view_binding": cap["view_binding"],
        "sink_binding": cap["sink_binding"],
        "nonce": nonce,
        "access_policy_ref_and_hash": cap["access_policy_ref_and_hash"],
        "deny_by_default": True,
        "raw_vault_path_disclosed": False,
        "checks": checks,
        "revocation_check": {
            "revocation_handle": cap["revocation"]["revocation_handle"],
            "status": revocation_status,
            "registry_ref_and_hash": cap["revocation"]["registry_ref_and_hash"],
            "checked_at": evaluated_at,
            "revocation_record_ref_and_hash": None if revocation_status == "ACTIVE" else {
                "ref_id": "rev-rec-001", "sha256": _ZERO_HASH,
            },
        },
        "decision": decision,
        "reason_codes": reason_codes,
        "evaluated_at": evaluated_at,
        "issuer": cap["issuer"],
        "externally_pinned_trust_root": cap["externally_pinned_trust_root"],
        "issuer_key_registry_ref_and_hash": cap["issuer_key_registry_ref_and_hash"],
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-access-decision/v1\0",
        "signed_bytes_hash": cap["signed_bytes_hash"],
        "signature_envelope": cap["signature_envelope"],
        "decision_hash_algorithm": "sha256(RFC8785-JCS-object-with-decision_hash-null)",
        "decision_hash": None,
    }
    obj_for_hash = dict(dec)
    obj_for_hash["decision_hash"] = None
    dec["decision_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    return dec


def _make_derivation(
    *,
    capability: dict | None = None,
    decision: dict | None = None,
    derived_view_bytes: bytes = b'{"view":"derived"}',
    derived_at: str = "2026-08-14T12:00:01Z",
) -> dict:
    cap = capability or _make_capability()
    dec = decision or _make_decision(capability=cap)

    view_sha256 = hashlib.sha256(derived_view_bytes).hexdigest()
    view_binding = dict(cap["view_binding"])
    view_binding["view_sha256"] = view_sha256

    deriv = {
        "schema_id": "seven/view-derivation",
        "schema_version": 1,
        "object_type": "ViewDerivation",
        "derivation_id": f"deriv-{cap['capability_id']}",
        "capability_ref_and_hash": {"ref_id": cap["capability_id"], "sha256": cap["capability_hash"]},
        "access_decision_ref_and_hash": {"ref_id": dec["decision_id"], "sha256": dec["decision_hash"]},
        "principal": dict(cap["principal"]),
        "operation": cap["operation"],
        "source_object": dict(cap["object_binding"]),
        "derived_view": view_binding,
        "sink_binding": dict(cap["sink_binding"]),
        "view_policy_ref_and_hash": {"ref_id": "vpol-001", "sha256": _ZERO_HASH},
        "derivation_rule_ref_and_hash": {"ref_id": "rule-001", "sha256": _ZERO_HASH},
        "generator_ref_and_hash": {"ref_id": "gen-001", "sha256": _ZERO_HASH},
        "redaction_manifest_ref_and_hash": {"ref_id": "redact-001", "sha256": _ZERO_HASH},
        "sink_write_receipt_ref_and_hash": {"ref_id": "sink-rec-001", "sha256": _ZERO_HASH},
        "revocation_check": {
            "revocation_handle": cap["revocation"]["revocation_handle"],
            "status": "ACTIVE",
            "registry_ref_and_hash": cap["revocation"]["registry_ref_and_hash"],
            "checked_at": derived_at,
            "revocation_record_ref_and_hash": None,
        },
        "nonce": cap["nonce"],
        "deny_by_default": True,
        "raw_vault_path_disclosed": False,
        "model_delivery": {
            "delivery_mode": "OPAQUE_HANDLE_AND_DERIVED_BYTES",
            "delivered_view_binding_source": "TOP_LEVEL_DERIVED_VIEW",
            "raw_vault_locator_exposed": False,
            "capability_token_exposed": False,
        },
        "derived_at": derived_at,
        "issuer": cap["issuer"],
        "externally_pinned_trust_root": cap["externally_pinned_trust_root"],
        "issuer_key_registry_ref_and_hash": cap["issuer_key_registry_ref_and_hash"],
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-view-derivation/v1\0",
        "signed_bytes_hash": cap["signed_bytes_hash"],
        "signature_envelope": cap["signature_envelope"],
        "derivation_hash_algorithm": "sha256(RFC8785-JCS-object-with-derivation_hash-null)",
        "derivation_hash": None,
    }
    obj_for_hash = dict(deriv)
    obj_for_hash["derivation_hash"] = None
    deriv["derivation_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    return deriv


def _make_event(
    *,
    capability: dict | None = None,
    decision: dict | None = None,
    derivation: dict | None = None,
    ledger_id: str = "ledger-001",
    sequence: int = 1,
    previous_event_hash: str | None = None,
    result: str = "ACCESS_GRANTED",
    occurred_at: str = "2026-08-14T12:00:02Z",
    access_request_id: str = "req-001",
    nonce: str = "nonce-aaaaaaaaaaaaaaaa",
) -> dict:
    cap = capability or _make_capability()
    dec = decision or _make_decision(capability=cap)

    event = {
        "schema_id": "seven/access-event",
        "schema_version": 1,
        "object_type": "AccessEvent",
        "event_id": f"evt-{ledger_id}-{sequence}",
        "ledger_id": ledger_id,
        "sequence": sequence,
        "previous_event_hash": previous_event_hash,
        "access_request_id": access_request_id,
        "capability_ref_and_hash": {"ref_id": cap["capability_id"], "sha256": cap["capability_hash"]},
        "decision_ref_and_hash": {"ref_id": dec["decision_id"], "sha256": dec["decision_hash"]},
        "view_derivation_ref_and_hash": (
            {"ref_id": derivation["derivation_id"], "sha256": derivation["derivation_hash"]}
            if derivation else None
        ),
        "sink_write_receipt_ref_and_hash": (
            {"ref_id": "sink-rec-001", "sha256": _ZERO_HASH}
            if derivation else None
        ),
        "principal": cap["principal"],
        "operation": cap["operation"],
        "object_binding": cap["object_binding"],
        "view_binding": cap["view_binding"],
        "sink_binding": cap["sink_binding"],
        "nonce": nonce,
        "revocation_check": dec["revocation_check"],
        "deny_by_default": True,
        "raw_vault_path_disclosed": False,
        "result": result,
        "occurred_at": occurred_at,
        "issuer": cap["issuer"],
        "externally_pinned_trust_root": cap["externally_pinned_trust_root"],
        "issuer_key_registry_ref_and_hash": cap["issuer_key_registry_ref_and_hash"],
        "canonicalizer_profile": "RFC8785_JCS_UTF8",
        "signature_domain": "seven-access-event/v1\0",
        "signed_bytes_hash": cap["signed_bytes_hash"],
        "signature_envelope": cap["signature_envelope"],
        "event_hash_algorithm": "sha256(RFC8785-JCS-object-with-event_hash-null)",
        "event_hash": None,
    }
    obj_for_hash = dict(event)
    obj_for_hash["event_hash"] = None
    event["event_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    return event


def _make_store() -> CompletionArtifactStore:
    """创建临时 CompletionArtifactStore。"""
    tmpdir = tempfile.mkdtemp(prefix="seven-vault-test-")
    volume_root = Path(tmpdir) / "volume"
    volume_root.mkdir(parents=True, exist_ok=True)
    root = volume_root / "cas"  # root must be under volume_root
    return CompletionArtifactStore(
        root=root,
        volume_root=volume_root,
        test_only_allow_non_d_volume=True,
    )


# ═══════════════════════════════════════════════════════════════════════
# Sensitivity Registry Tests
# ═══════════════════════════════════════════════════════════════════════


class SensitivityRegistryTests(unittest.TestCase):

    def test_all_four_levels_exist(self):
        levels = SensitivityLevel.all_levels()
        self.assertEqual(len(levels), 4)
        self.assertIn("PUBLIC", levels)
        self.assertIn("RESTRICTED", levels)
        self.assertIn("SOLUTION_BEARING", levels)
        self.assertIn("HOLDOUT_BEARING", levels)

    def test_rank_ordering(self):
        self.assertLess(SensitivityLevel.rank("PUBLIC"), SensitivityLevel.rank("RESTRICTED"))
        self.assertLess(SensitivityLevel.rank("RESTRICTED"), SensitivityLevel.rank("SOLUTION_BEARING"))
        self.assertLess(SensitivityLevel.rank("SOLUTION_BEARING"), SensitivityLevel.rank("HOLDOUT_BEARING"))

    def test_solver_accessible_only_public_restricted(self):
        self.assertTrue(SensitivityLevel.solver_accessible("PUBLIC"))
        self.assertTrue(SensitivityLevel.solver_accessible("RESTRICTED"))
        self.assertFalse(SensitivityLevel.solver_accessible("SOLUTION_BEARING"))
        self.assertFalse(SensitivityLevel.solver_accessible("HOLDOUT_BEARING"))

    def test_registry_register_and_get(self):
        reg = SensitivityRegistry()
        record = VaultObjectRecord(
            object_id="obj-001",
            object_sha256=_ZERO_HASH,
            sensitivity="RESTRICTED",
        )
        reg.register(record)
        self.assertEqual(reg.get_sensitivity("obj-001"), "RESTRICTED")
        self.assertTrue(reg.check_solver_access("obj-001"))
        self.assertIsNone(reg.get("nonexistent"))

    def test_registry_solver_cannot_access_solution_bearing(self):
        reg = SensitivityRegistry()
        record = VaultObjectRecord(
            object_id="obj-sol",
            object_sha256=_ZERO_HASH,
            sensitivity="SOLUTION_BEARING",
        )
        reg.register(record)
        self.assertFalse(reg.check_solver_access("obj-sol"))


# ═══════════════════════════════════════════════════════════════════════
# VaultAccessCapability Tests
# ═══════════════════════════════════════════════════════════════════════


class VaultAccessCapabilityGoldenVectors(unittest.TestCase):

    def test_valid_capability_passes(self):
        cap = _make_capability()
        result = verify_vault_access_capability(cap)
        self.assertTrue(result.passed, f"Expected PASS, got errors: {result.details}")

    def test_valid_capability_with_model_role(self):
        cap = _make_capability(principal_type="MODEL_ROLE", sensitivity="PUBLIC")
        result = verify_vault_access_capability(cap)
        self.assertTrue(result.passed, f"Expected PASS, got errors: {result.details}")

    def test_valid_write_restricted_object(self):
        cap = _make_capability(
            operation="WRITE_RESTRICTED_OBJECT",
            principal_type="SERVICE",
            sensitivity="RESTRICTED",
            sink_kind="RESTRICTED_VAULT",
        )
        result = verify_vault_access_capability(cap)
        self.assertTrue(result.passed, f"Expected PASS, got errors: {result.details}")

    def test_valid_seal_restricted_object(self):
        cap = _make_capability(
            operation="SEAL_RESTRICTED_OBJECT",
            principal_type="SERVICE",
            sensitivity="SOLUTION_BEARING",
            sink_kind="RESTRICTED_CAS",
        )
        result = verify_vault_access_capability(cap)
        self.assertTrue(result.passed, f"Expected PASS, got errors: {result.details}")

    def test_capability_hash_is_correct(self):
        cap = _make_capability()
        obj_for_hash = dict(cap)
        obj_for_hash["capability_hash"] = None
        expected = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
        self.assertEqual(cap["capability_hash"], expected)


class VaultAccessCapabilityNegativeVectors(unittest.TestCase):

    def test_deny_by_default_false_rejected(self):
        cap = _make_capability(deny_by_default=False)
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_DENY_BY_DEFAULT_FALSE, result.error_codes)

    def test_raw_vault_path_disclosure_true_rejected(self):
        cap = _make_capability(raw_vault_path_disclosure=True)
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_RAW_PATH_DISCLOSED, result.error_codes)

    def test_read_raw_object_operation_rejected(self):
        cap = _make_capability(operation="READ_RAW_OBJECT")
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_READ_RAW_OBJECT_REJECTED, result.error_codes)

    def test_solver_accessing_solution_bearing_rejected(self):
        cap = _make_capability(
            principal_type="TARGET_SOLVER",
            operation="READ_DERIVED_VIEW",
            sensitivity="SOLUTION_BEARING",
        )
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)

    def test_solver_accessing_holdout_bearing_rejected(self):
        cap = _make_capability(
            principal_type="TARGET_SOLVER",
            operation="DERIVE_VIEW",
            sensitivity="HOLDOUT_BEARING",
        )
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)

    def test_write_with_ephemeral_sink_rejected(self):
        cap = _make_capability(
            operation="WRITE_RESTRICTED_OBJECT",
            principal_type="SERVICE",
            sink_kind="EPHEMERAL_MODEL_INPUT",
        )
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_SINK_MISMATCH, result.error_codes)

    def test_wrong_capability_hash_rejected(self):
        cap = _make_capability()
        cap["capability_hash"] = "f" * 64
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_CAPABILITY_HASH_MISMATCH, result.error_codes)

    def test_revocable_false_rejected(self):
        cap = _make_capability()
        cap["revocation"]["revocable"] = False
        # Need to recompute hash
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_CAPABILITY_REVOKED, result.error_codes)

    def test_status_at_issue_not_active_rejected(self):
        cap = _make_capability()
        cap["revocation"]["status_at_issue"] = "REVOKED"
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)

    def test_invalid_nonce_too_short_rejected(self):
        cap = _make_capability(nonce="short")
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)

    def test_wrong_signature_domain_rejected(self):
        cap = _make_capability()
        cap["signature_domain"] = "wrong-domain\0"
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_vault_access_capability(cap)
        self.assertFalse(result.passed)
        self.assertIn(EC.SIGNATURE_DOMAIN_INVALID, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# AccessDecision Tests
# ═══════════════════════════════════════════════════════════════════════


class AccessDecisionGoldenVectors(unittest.TestCase):

    def test_valid_allow_decision_passes(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap, decision="ALLOW")
        result = verify_access_decision(dec, capability=cap)
        self.assertTrue(result.passed, f"Expected PASS, got errors: {result.details}")

    def test_valid_deny_decision_passes(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap, decision="DENY", reason_codes=["POLICY_DENY"], checks_pass=False)
        result = verify_access_decision(dec, capability=cap)
        self.assertTrue(result.passed, f"Expected PASS, got errors: {result.details}")

    def test_decision_hash_is_correct(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        obj = dict(dec)
        obj["decision_hash"] = None
        expected = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        self.assertEqual(dec["decision_hash"], expected)


class AccessDecisionNegativeVectors(unittest.TestCase):

    def test_deny_by_default_false_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        dec["deny_by_default"] = False
        obj = dict(dec)
        obj["decision_hash"] = None
        dec["decision_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_decision(dec, capability=cap)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_DENY_BY_DEFAULT_FALSE, result.error_codes)

    def test_raw_vault_path_disclosed_true_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        dec["raw_vault_path_disclosed"] = True
        obj = dict(dec)
        obj["decision_hash"] = None
        dec["decision_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_decision(dec, capability=cap)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_RAW_PATH_DISCLOSED, result.error_codes)

    def test_allow_with_failing_check_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap, decision="ALLOW")
        dec["checks"]["principal"] = "FAIL"
        obj = dict(dec)
        obj["decision_hash"] = None
        dec["decision_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_decision(dec)
        self.assertFalse(result.passed)

    def test_allow_with_revoked_capability_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap, decision="ALLOW", revocation_status="REVOKED")
        result = verify_access_decision(dec)
        self.assertFalse(result.passed)

    def test_allow_with_wrong_reason_codes_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap, decision="ALLOW", reason_codes=["POLICY_DENY"])
        obj = dict(dec)
        obj["decision_hash"] = None
        dec["decision_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_decision(dec)
        self.assertFalse(result.passed)

    def test_principal_mismatch_with_capability(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        dec["principal"] = _make_principal(principal_type="SERVICE")
        obj = dict(dec)
        obj["decision_hash"] = None
        dec["decision_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_decision(dec, capability=cap)
        self.assertFalse(result.passed)

    def test_operation_mismatch_with_capability(self):
        cap = _make_capability(operation="READ_DERIVED_VIEW")
        dec = _make_decision(capability=cap)
        dec["operation"] = "DERIVE_VIEW"
        obj = dict(dec)
        obj["decision_hash"] = None
        dec["decision_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_decision(dec, capability=cap)
        self.assertFalse(result.passed)

    def test_nonce_replay_detected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        seen = {cap["nonce"]}
        result = verify_access_decision(dec, capability=cap, seen_nonces=seen)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_NONCE_REPLAY, result.error_codes)

    def test_expired_capability_rejected(self):
        cap = _make_capability(not_before="2026-08-14T00:00:00Z", expires_at="2026-08-14T06:00:00Z")
        dec = _make_decision(capability=cap)
        result = verify_access_decision(dec, capability=cap, evaluation_time="2026-08-14T12:00:00Z")
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_CAPABILITY_EXPIRED, result.error_codes)

    def test_not_yet_valid_capability_rejected(self):
        cap = _make_capability(not_before="2026-08-15T00:00:00Z", expires_at="2026-08-16T00:00:00Z")
        dec = _make_decision(capability=cap)
        result = verify_access_decision(dec, capability=cap, evaluation_time="2026-08-14T12:00:00Z")
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_CAPABILITY_NOT_YET_VALID, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# ViewDerivation Tests
# ═══════════════════════════════════════════════════════════════════════


class ViewDerivationGoldenVectors(unittest.TestCase):

    def test_valid_derivation_passes(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        result = verify_view_derivation(deriv, capability=cap, access_decision=dec)
        self.assertTrue(result.passed, f"Expected PASS, got errors: {result.details}")

    def test_derivation_hash_is_correct(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        obj = dict(deriv)
        obj["derivation_hash"] = None
        expected = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        self.assertEqual(deriv["derivation_hash"], expected)


class ViewDerivationNegativeVectors(unittest.TestCase):

    def test_raw_vault_locator_exposed_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        deriv["model_delivery"]["raw_vault_locator_exposed"] = True
        obj = dict(deriv)
        obj["derivation_hash"] = None
        deriv["derivation_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_view_derivation(deriv)
        self.assertFalse(result.passed)
        self.assertIn(EC.VIEW_RAW_LOCATOR_EXPOSED, result.error_codes)

    def test_capability_token_exposed_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        deriv["model_delivery"]["capability_token_exposed"] = True
        obj = dict(deriv)
        obj["derivation_hash"] = None
        deriv["derivation_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_view_derivation(deriv)
        self.assertFalse(result.passed)
        self.assertIn(EC.VIEW_CAPABILITY_TOKEN_EXPOSED, result.error_codes)

    def test_wrong_delivery_mode_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        deriv["model_delivery"]["delivery_mode"] = "RAW_PATH"
        obj = dict(deriv)
        obj["derivation_hash"] = None
        deriv["derivation_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_view_derivation(deriv)
        self.assertFalse(result.passed)
        self.assertIn(EC.VIEW_DELIVERY_MODE_INVALID, result.error_codes)

    def test_revocation_not_active_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        deriv["revocation_check"]["status"] = "REVOKED"
        obj = dict(deriv)
        obj["derivation_hash"] = None
        deriv["derivation_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_view_derivation(deriv)
        self.assertFalse(result.passed)

    def test_deny_by_default_false_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        deriv["deny_by_default"] = False
        obj = dict(deriv)
        obj["derivation_hash"] = None
        deriv["derivation_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_view_derivation(deriv)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_DENY_BY_DEFAULT_FALSE, result.error_codes)

    def test_source_object_mismatch_with_capability(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        deriv["source_object"]["object_id"] = "wrong-obj"
        obj = dict(deriv)
        obj["derivation_hash"] = None
        deriv["derivation_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_view_derivation(deriv, capability=cap)
        self.assertFalse(result.passed)

    def test_solver_accessing_solution_bearing_in_derivation(self):
        cap = _make_capability(
            principal_type="TARGET_SOLVER",
            operation="DERIVE_VIEW",
            sensitivity="SOLUTION_BEARING",
        )
        # Fix capability hash after sensitivity change
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        result = verify_view_derivation(deriv)
        self.assertFalse(result.passed)


# ═══════════════════════════════════════════════════════════════════════
# AccessEvent Ledger Tests
# ═══════════════════════════════════════════════════════════════════════


class AccessEventGoldenVectors(unittest.TestCase):

    def test_valid_single_event_passes(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv)
        result = verify_access_event(event)
        self.assertTrue(result.passed, f"Expected PASS, got errors: {result.details}")

    def test_event_hash_is_correct(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv)
        obj = dict(event)
        obj["event_hash"] = None
        expected = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        self.assertEqual(event["event_hash"], expected)

    def test_first_event_has_null_previous_hash(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=1, previous_event_hash=None)
        result = verify_access_event(event)
        self.assertTrue(result.passed)

    def test_access_granted_requires_derivation_ref(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        event = _make_event(capability=cap, decision=dec, derivation=None, result="ACCESS_GRANTED")
        result = verify_access_event(event)
        self.assertFalse(result.passed)
        self.assertIn(EC.VIEW_SINK_RECEIPT_MISSING, result.error_codes)


class AccessEventNegativeVectors(unittest.TestCase):

    def test_deny_by_default_false_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv)
        event["deny_by_default"] = False
        obj = dict(event)
        obj["event_hash"] = None
        event["event_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_event(event)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_DENY_BY_DEFAULT_FALSE, result.error_codes)

    def test_raw_vault_path_disclosed_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv)
        event["raw_vault_path_disclosed"] = True
        obj = dict(event)
        obj["event_hash"] = None
        event["event_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_event(event)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_RAW_PATH_DISCLOSED, result.error_codes)

    def test_sequence_zero_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=0)
        obj = dict(event)
        obj["event_hash"] = None
        event["event_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_event(event)
        self.assertFalse(result.passed)
        self.assertIn(EC.ACCESS_LEDGER_SEQUENCE_CONFLICT, result.error_codes)

    def test_first_event_with_non_null_previous_hash_rejected(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=1, previous_event_hash=_ZERO_HASH)
        obj = dict(event)
        obj["event_hash"] = None
        event["event_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()
        result = verify_access_event(event)
        self.assertFalse(result.passed)


class AccessEventLedgerFaultInjection(unittest.TestCase):

    def test_ledger_append_in_order(self):
        ledger = AccessEventLedger("ledger-001")
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)

        event1 = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=1, previous_event_hash=None)
        result1 = ledger.append(event1)
        self.assertTrue(result1.passed, f"Event 1: {result1.details}")

        event2 = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=2,
                             previous_event_hash=event1["event_hash"],
                             nonce="nonce-bbbbbbbbbbbbbbbb")
        # Recompute hash for event2
        obj = dict(event2)
        obj["event_hash"] = None
        event2["event_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        result2 = ledger.append(event2)
        self.assertTrue(result2.passed, f"Event 2: {result2.details}")
        self.assertEqual(ledger.length, 2)

    def test_ledger_sequence_conflict_rejected(self):
        ledger = AccessEventLedger("ledger-001")
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)

        event1 = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=1, previous_event_hash=None)
        ledger.append(event1)

        # Try to append event with sequence 1 again (different event_id)
        event_dup = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=1,
                                previous_event_hash=None, access_request_id="req-002",
                                nonce="nonce-bbbbbbbbbbbbbbbb")
        obj = dict(event_dup)
        obj["event_hash"] = None
        event_dup["event_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        result = ledger.append(event_dup)
        self.assertFalse(result.passed)
        self.assertIn(EC.ACCESS_LEDGER_SEQUENCE_CONFLICT, result.error_codes)

    def test_ledger_previous_hash_mismatch_rejected(self):
        ledger = AccessEventLedger("ledger-001")
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)

        event1 = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=1, previous_event_hash=None)
        ledger.append(event1)

        # Try to append event with wrong previous_event_hash
        event2 = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=2,
                             previous_event_hash="f" * 64,
                             nonce="nonce-bbbbbbbbbbbbbbbb")
        obj = dict(event2)
        obj["event_hash"] = None
        event2["event_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        result = ledger.append(event2)
        self.assertFalse(result.passed)
        self.assertIn(EC.ACCESS_LEDGER_PREVIOUS_HASH_MISMATCH, result.error_codes)

    def test_ledger_nonce_replay_rejected(self):
        ledger = AccessEventLedger("ledger-001")
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)

        event1 = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=1, previous_event_hash=None)
        ledger.append(event1)

        # Same nonce, different sequence
        event2 = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=2,
                             previous_event_hash=event1["event_hash"],
                             nonce=cap["nonce"])  # replay!
        obj = dict(event2)
        obj["event_hash"] = None
        event2["event_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        result = ledger.append(event2)
        self.assertFalse(result.passed)
        self.assertIn(EC.VAULT_NONCE_REPLAY, result.error_codes)

    def test_ledger_integrity_verification_after_tamper(self):
        ledger = AccessEventLedger("ledger-001")
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)

        event1 = _make_event(capability=cap, decision=dec, derivation=deriv, sequence=1, previous_event_hash=None)
        ledger.append(event1)

        # Tamper with the event in the ledger
        ledger._events[0]["result"] = "ACCESS_DENIED"

        result = ledger.verify_integrity()
        self.assertFalse(result.passed)

    def test_ledger_wrong_ledger_id_rejected(self):
        ledger = AccessEventLedger("ledger-001")
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)

        event = _make_event(capability=cap, decision=dec, derivation=deriv, ledger_id="wrong-ledger")
        obj = dict(event)
        obj["event_hash"] = None
        event["event_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        result = ledger.append(event)
        self.assertFalse(result.passed)
        self.assertIn(EC.ACCESS_LEDGER_TAMPERED, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# VaultBroker Tests — Full Access Chain
# ═══════════════════════════════════════════════════════════════════════


class VaultBrokerGoldenVectors(unittest.TestCase):

    def test_full_access_chain_allow(self):
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        # Register a vault object
        content = b'{"problem":"1+1=?","view":"public"}'
        sha = broker.register_vault_object("obj-001", content, "PUBLIC")

        # Create capability matching the object
        cap = _make_capability(
            operation="READ_DERIVED_VIEW",
            principal_type="TARGET_SOLVER",
            sensitivity="PUBLIC",
        )
        cap["object_binding"]["object_sha256"] = sha

        # Recompute capability hash
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        derived_bytes = b'{"view":"derived_public_view"}'
        result, decision, derivation, event = broker.process_access_request(
            capability=cap,
            access_request_id="req-001",
            evaluation_time="2026-08-14T12:00:00Z",
            derived_view_bytes=derived_bytes,
        )

        self.assertTrue(result.passed, f"Expected PASS, got: {result.details}")
        self.assertIsNotNone(decision)
        self.assertEqual(decision["decision"], "ALLOW")
        self.assertIsNotNone(derivation)
        self.assertIsNotNone(event)
        self.assertEqual(event["result"], "ACCESS_GRANTED")
        self.assertEqual(ledger.length, 1)

    def test_broker_does_not_expose_raw_path(self):
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        content = b'{"secret":"answer"}'
        sha = broker.register_vault_object("obj-001", content, "RESTRICTED")

        # The raw path is only accessible inside broker
        raw = broker.get_raw_vault_path("obj-001")
        self.assertEqual(raw, sha)

        # But process_access_request never returns raw filesystem paths
        cap = _make_capability(sensitivity="RESTRICTED")
        cap["object_binding"]["object_sha256"] = sha
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        result, decision, derivation, event = broker.process_access_request(
            capability=cap,
            access_request_id="req-001",
            evaluation_time="2026-08-14T12:00:00Z",
            derived_view_bytes=b'{"view":"redacted"}',
        )

        self.assertTrue(result.passed)
        # Verify no raw filesystem path in any returned object.
        # The sha256 hash in object_binding is legitimate (content-addressed),
        # but the actual CAS filesystem path must never appear.
        store_root_str = str(store.root)
        for obj_dict in [decision, derivation, event]:
            if obj_dict is not None:
                serialized = json.dumps(obj_dict)
                self.assertNotIn(store_root_str, serialized, "Raw CAS filesystem path leaked in response")
                # Check no path-like strings with /data or store root
                self.assertNotIn("/Volumes/", serialized, "Volume path leaked in response")


class VaultBrokerNegativeVectors(unittest.TestCase):

    def test_revoked_capability_denied(self):
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        cap = _make_capability()
        broker.revoke_capability(cap["revocation"]["revocation_handle"])

        result, decision, derivation, event = broker.process_access_request(
            capability=cap,
            access_request_id="req-001",
            evaluation_time="2026-08-14T12:00:00Z",
        )

        self.assertFalse(result.passed)
        self.assertIsNotNone(decision)
        self.assertEqual(decision["decision"], "DENY")
        self.assertIsNone(derivation)
        self.assertIsNotNone(event)
        self.assertEqual(event["result"], "ACCESS_DENIED")

    def test_expired_capability_denied(self):
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        cap = _make_capability(not_before="2026-08-14T00:00:00Z", expires_at="2026-08-14T06:00:00Z")

        result, decision, derivation, event = broker.process_access_request(
            capability=cap,
            access_request_id="req-001",
            evaluation_time="2026-08-14T12:00:00Z",
        )

        self.assertFalse(result.passed)
        self.assertEqual(decision["decision"], "DENY")

    def test_nonce_replay_denied(self):
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        cap = _make_capability()

        # First request succeeds
        result1, _, _, _ = broker.process_access_request(
            capability=cap,
            access_request_id="req-001",
            evaluation_time="2026-08-14T12:00:00Z",
            derived_view_bytes=b'{"view":"v1"}',
        )
        self.assertTrue(result1.passed)

        # Second request with same nonce fails
        result2, decision2, _, _ = broker.process_access_request(
            capability=cap,
            access_request_id="req-002",
            evaluation_time="2026-08-14T12:00:00Z",
        )
        self.assertFalse(result2.passed)
        self.assertEqual(decision2["decision"], "DENY")

    def test_solver_accessing_solution_bearing_denied(self):
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        # Register a solution-bearing object
        content = b'{"answer":"42"}'
        sha = broker.register_vault_object("obj-sol", content, "SOLUTION_BEARING")

        cap = _make_capability(
            operation="READ_DERIVED_VIEW",
            principal_type="TARGET_SOLVER",
            sensitivity="SOLUTION_BEARING",
        )
        cap["object_binding"]["object_sha256"] = sha
        cap["object_binding"]["object_id"] = "obj-sol"
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        result, decision, _, _ = broker.process_access_request(
            capability=cap,
            access_request_id="req-001",
            evaluation_time="2026-08-14T12:00:00Z",
        )

        self.assertFalse(result.passed)
        self.assertEqual(decision["decision"], "DENY")

    def test_invalid_capability_denied(self):
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        cap = _make_capability()
        cap["deny_by_default"] = False  # Invalid
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        result, decision, _, _ = broker.process_access_request(
            capability=cap,
            access_request_id="req-001",
            evaluation_time="2026-08-14T12:00:00Z",
        )

        self.assertFalse(result.passed)
        self.assertEqual(decision["decision"], "DENY")

    def test_read_raw_object_operation_denied(self):
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        cap = _make_capability(operation="READ_RAW_OBJECT")
        obj = dict(cap)
        obj["capability_hash"] = None
        cap["capability_hash"] = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

        result, decision, _, _ = broker.process_access_request(
            capability=cap,
            access_request_id="req-001",
            evaluation_time="2026-08-14T12:00:00Z",
        )

        self.assertFalse(result.passed)


# ═══════════════════════════════════════════════════════════════════════
# CAS Core Reuse Enforcement
# ═══════════════════════════════════════════════════════════════════════


class CASCOREReuseEnforcement(unittest.TestCase):

    def test_vault_broker_uses_same_completion_artifact_store(self):
        """VaultBroker 必须复用 GV0 CompletionArtifactStore，不另造第二套 store。"""
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        # The broker's artifact_store IS the same CompletionArtifactStore
        self.assertIsInstance(broker.artifact_store, CompletionArtifactStore)
        self.assertIs(broker.artifact_store, store)

    def test_vault_object_written_to_cas_is_retrievable(self):
        """Vault 对象通过 broker 写入后，可以通过同一个 CAS store 检索。"""
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        content = b'{"data":"test"}'
        sha = broker.register_vault_object("obj-001", content, "PUBLIC")

        # Retrieve through the same store
        retrieved = store.get(sha)
        self.assertEqual(retrieved, content)

    def test_no_second_bundle_store_created(self):
        """验证 VaultBroker 不创建第二套 store — 只有一个 CompletionArtifactStore 实例。"""
        store = _make_store()
        registry = SensitivityRegistry()
        ledger = AccessEventLedger("ledger-001")
        broker = VaultBroker(
            sensitivity_registry=registry,
            artifact_store=store,
            ledger=ledger,
        )

        # Write multiple objects — all go to the same store
        sha1 = broker.register_vault_object("obj-001", b'{"a":1}', "PUBLIC")
        sha2 = broker.register_vault_object("obj-002", b'{"b":2}', "RESTRICTED")

        # Both should be in the same store
        self.assertTrue(store.exists(sha1))
        self.assertTrue(store.exists(sha2))


# ═══════════════════════════════════════════════════════════════════════
# Artifact Seal Protocol Tests
# ═══════════════════════════════════════════════════════════════════════


class ArtifactSealGoldenVectors(unittest.TestCase):

    def test_live_to_partial_to_seal(self):
        store = _make_store()
        protocol = ArtifactSealProtocol(store)

        # Start live writer
        protocol.start_live_writer("job-001")

        # Drain writer
        protocol.drain_writer("job-001")
        self.assertFalse(protocol.is_writer_alive("job-001"))

        # Create partial
        files = [{"file_id": "f1", "size_bytes": 100, "sha256": _ZERO_HASH}]
        manifest = protocol.create_partial(
            job_id="job-001",
            attempt_id="attempt-001",
            files=files,
            schema_id="seven/implementation-completion-bundle",
        )
        self.assertEqual(protocol.get_seal_state("attempt-001"), "PARTIAL")

        # Record CommitIntent
        intent = CommitIntent(
            intent_id="intent-001",
            job_id="job-001",
            attempt_id="attempt-001",
            input_hash=_ZERO_HASH,
            manifest_hash=manifest.manifest_hash,
            expected_terminal="COMPLETED",
            target_cas_uri="cas://seven/bundle",
            authorization_hash=_ZERO_HASH,
            permit_hash=_ZERO_HASH,
            fence_token=100,
            expiry="2026-08-16T00:00:00Z",
            created_at="2026-08-14T12:00:00Z",
        )
        protocol.record_commit_intent(intent)

        # Seal
        bundle_content = canonical_json_bytes({
            "manifest_hash": manifest.manifest_hash,
            "bundle_id": "bundle-001",
        })
        ref = protocol.seal(
            attempt_id="attempt-001",
            intent_id="intent-001",
            bundle_content=bundle_content,
            current_time="2026-08-14T13:00:00Z",
            current_fence=100,
        )

        self.assertEqual(protocol.get_seal_state("attempt-001"), "SEALED")
        self.assertTrue(store.exists(ref.sha256))

    def test_manifest_hash_is_deterministic(self):
        files = [{"file_id": "f1", "size_bytes": 100, "sha256": _ZERO_HASH}]
        m1 = ArtifactManifest.build(manifest_id="m1", job_id="j1", attempt_id="a1", files=files)
        m2 = ArtifactManifest.build(manifest_id="m1", job_id="j1", attempt_id="a1", files=files)
        self.assertEqual(m1.manifest_hash, m2.manifest_hash)


class ArtifactSealNegativeVectors(unittest.TestCase):

    def test_seal_with_live_writer_rejected(self):
        store = _make_store()
        protocol = ArtifactSealProtocol(store)
        protocol.start_live_writer("job-001")
        # Don't drain — writer still alive

        with self.assertRaises(Exception):
            protocol.create_partial(job_id="job-001", attempt_id="a1", files=[])

    def test_seal_already_sealed_rejected(self):
        store = _make_store()
        protocol = ArtifactSealProtocol(store)
        protocol.start_live_writer("job-001")
        protocol.drain_writer("job-001")
        manifest = protocol.create_partial(job_id="job-001", attempt_id="a1", files=[])
        intent = CommitIntent(
            intent_id="i1", job_id="job-001", attempt_id="a1",
            input_hash=_ZERO_HASH, manifest_hash=manifest.manifest_hash,
            expected_terminal="COMPLETED", target_cas_uri="cas://x",
            authorization_hash=_ZERO_HASH, permit_hash=_ZERO_HASH,
            fence_token=1, expiry="2026-08-16T00:00:00Z", created_at="2026-08-14T00:00:00Z",
        )
        protocol.record_commit_intent(intent)
        protocol.seal(
            attempt_id="a1", intent_id="i1",
            bundle_content=b'{"manifest_hash":"' + manifest.manifest_hash.encode() + b'"}',
            current_time="2026-08-14T12:00:00Z", current_fence=1,
        )

        with self.assertRaises(Exception):
            protocol.seal(
                attempt_id="a1", intent_id="i1",
                bundle_content=b'{}',
                current_time="2026-08-14T13:00:00Z", current_fence=1,
            )

    def test_seal_without_intent_rejected(self):
        store = _make_store()
        protocol = ArtifactSealProtocol(store)
        protocol.start_live_writer("job-001")
        protocol.drain_writer("job-001")
        protocol.create_partial(job_id="job-001", attempt_id="a1", files=[])

        with self.assertRaises(Exception):
            protocol.seal(
                attempt_id="a1", intent_id="nonexistent",
                bundle_content=b'{}',
                current_time="2026-08-14T12:00:00Z", current_fence=1,
            )

    def test_seal_with_stale_fence_rejected(self):
        store = _make_store()
        protocol = ArtifactSealProtocol(store)
        protocol.start_live_writer("job-001")
        protocol.drain_writer("job-001")
        manifest = protocol.create_partial(job_id="job-001", attempt_id="a1", files=[])
        intent = CommitIntent(
            intent_id="i1", job_id="job-001", attempt_id="a1",
            input_hash=_ZERO_HASH, manifest_hash=manifest.manifest_hash,
            expected_terminal="COMPLETED", target_cas_uri="cas://x",
            authorization_hash=_ZERO_HASH, permit_hash=_ZERO_HASH,
            fence_token=100, expiry="2026-08-16T00:00:00Z", created_at="2026-08-14T00:00:00Z",
        )
        protocol.record_commit_intent(intent)

        with self.assertRaises(Exception):
            protocol.seal(
                attempt_id="a1", intent_id="i1",
                bundle_content=b'{}',
                current_time="2026-08-14T12:00:00Z", current_fence=200,  # wrong fence
            )

    def test_seal_with_expired_intent_rejected(self):
        store = _make_store()
        protocol = ArtifactSealProtocol(store)
        protocol.start_live_writer("job-001")
        protocol.drain_writer("job-001")
        manifest = protocol.create_partial(job_id="job-001", attempt_id="a1", files=[])
        intent = CommitIntent(
            intent_id="i1", job_id="job-001", attempt_id="a1",
            input_hash=_ZERO_HASH, manifest_hash=manifest.manifest_hash,
            expected_terminal="COMPLETED", target_cas_uri="cas://x",
            authorization_hash=_ZERO_HASH, permit_hash=_ZERO_HASH,
            fence_token=1, expiry="2026-08-14T06:00:00Z", created_at="2026-08-14T00:00:00Z",
        )
        protocol.record_commit_intent(intent)

        with self.assertRaises(Exception):
            protocol.seal(
                attempt_id="a1", intent_id="i1",
                bundle_content=b'{}',
                current_time="2026-08-14T12:00:00Z", current_fence=1,  # expired
            )

    def test_seal_with_revoked_intent_rejected(self):
        store = _make_store()
        protocol = ArtifactSealProtocol(store)
        protocol.start_live_writer("job-001")
        protocol.drain_writer("job-001")
        manifest = protocol.create_partial(job_id="job-001", attempt_id="a1", files=[])
        intent = CommitIntent(
            intent_id="i1", job_id="job-001", attempt_id="a1",
            input_hash=_ZERO_HASH, manifest_hash=manifest.manifest_hash,
            expected_terminal="COMPLETED", target_cas_uri="cas://x",
            authorization_hash=_ZERO_HASH, permit_hash=_ZERO_HASH,
            fence_token=1, expiry="2026-08-16T00:00:00Z", created_at="2026-08-14T00:00:00Z",
        )
        protocol.record_commit_intent(intent)
        protocol.revoke_intent("i1")

        with self.assertRaises(Exception):
            protocol.seal(
                attempt_id="a1", intent_id="i1",
                bundle_content=b'{}',
                current_time="2026-08-14T12:00:00Z", current_fence=1,
            )


# ═══════════════════════════════════════════════════════════════════════
# CAS/DB Reconcile Tests
# ═══════════════════════════════════════════════════════════════════════


class ReconcileTests(unittest.TestCase):

    def test_sealed_and_committed(self):
        store = _make_store()
        reconciler = ArtifactReconciler(store)

        sha = "a" * 64
        cas_attempts = {
            "a1": {"job_id": "j1", "has_sealed": True, "cas_sha256": sha, "writer_alive": False},
        }
        db_records = {
            "a1": DBArtifactRecord(attempt_id="a1", job_id="j1", committed=True, artifact_sha256=sha),
        }

        results = reconciler.reconcile(cas_attempts=cas_attempts, db_records=db_records)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].state, "SEALED_AND_COMMITTED")
        self.assertFalse(reconciler.needs_recovery(results[0]))

    def test_live_writer_active(self):
        store = _make_store()
        reconciler = ArtifactReconciler(store)

        cas_attempts = {
            "a1": {"job_id": "j1", "has_sealed": False, "writer_alive": True},
        }
        db_records = {}

        results = reconciler.reconcile(cas_attempts=cas_attempts, db_records=db_records)
        self.assertEqual(results[0].state, "LIVE_WRITER_ACTIVE")

    def test_partial_writer_dead(self):
        store = _make_store()
        reconciler = ArtifactReconciler(store)

        cas_attempts = {
            "a1": {"job_id": "j1", "has_partial": True, "has_sealed": False, "writer_alive": False},
        }
        db_records = {}

        results = reconciler.reconcile(cas_attempts=cas_attempts, db_records=db_records)
        self.assertEqual(results[0].state, "PARTIAL_WRITER_DEAD")
        self.assertTrue(reconciler.needs_recovery(results[0]))

    def test_sealed_db_uncommitted(self):
        store = _make_store()
        reconciler = ArtifactReconciler(store)

        sha = "a" * 64
        cas_attempts = {
            "a1": {"job_id": "j1", "has_sealed": True, "cas_sha256": sha, "writer_alive": False,
                   "intent_id": "i1", "intent_valid": True, "fence_token": 100},
        }
        db_records = {}

        results = reconciler.reconcile(cas_attempts=cas_attempts, db_records=db_records, current_fence=100)
        self.assertEqual(results[0].state, "SEALED_DB_UNCOMMITTED")
        self.assertTrue(reconciler.can_reconcile_db(results[0]))

    def test_db_committed_artifact_missing(self):
        store = _make_store()
        reconciler = ArtifactReconciler(store)

        cas_attempts = {}
        db_records = {
            "a1": DBArtifactRecord(attempt_id="a1", job_id="j1", committed=True, artifact_sha256="a" * 64),
        }

        results = reconciler.reconcile(cas_attempts=cas_attempts, db_records=db_records)
        self.assertEqual(results[0].state, "DB_COMMITTED_ARTIFACT_MISSING")
        self.assertTrue(reconciler.needs_recovery(results[0]))

    def test_hash_mismatch_conflict(self):
        store = _make_store()
        reconciler = ArtifactReconciler(store)

        cas_attempts = {
            "a1": {"job_id": "j1", "has_sealed": True, "cas_sha256": "a" * 64, "writer_alive": False},
        }
        db_records = {
            "a1": DBArtifactRecord(attempt_id="a1", job_id="j1", committed=True, artifact_sha256="b" * 64),
        }

        results = reconciler.reconcile(cas_attempts=cas_attempts, db_records=db_records)
        self.assertEqual(results[0].state, "CONFLICT")
        self.assertTrue(reconciler.needs_recovery(results[0]))

    def test_missing(self):
        store = _make_store()
        reconciler = ArtifactReconciler(store)

        results = reconciler.reconcile(cas_attempts={}, db_records={})
        self.assertEqual(len(results), 0)

    def test_stale_fence_cannot_reconcile(self):
        store = _make_store()
        reconciler = ArtifactReconciler(store)

        sha = "a" * 64
        cas_attempts = {
            "a1": {"job_id": "j1", "has_sealed": True, "cas_sha256": sha, "writer_alive": False,
                   "intent_id": "i1", "intent_valid": True, "fence_token": 100},
        }
        db_records = {}

        results = reconciler.reconcile(cas_attempts=cas_attempts, db_records=db_records, current_fence=200)
        self.assertEqual(results[0].state, "SEALED_DB_UNCOMMITTED")
        self.assertFalse(reconciler.can_reconcile_db(results[0]))


# ═══════════════════════════════════════════════════════════════════════
# Cross-object Consistency Tests
# ═══════════════════════════════════════════════════════════════════════


class CrossObjectConsistencyTests(unittest.TestCase):

    def test_decision_capability_ref_matches_capability_hash(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        self.assertEqual(
            dec["capability_ref_and_hash"]["sha256"],
            cap["capability_hash"],
        )

    def test_derivation_decision_ref_matches_decision_hash(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        self.assertEqual(
            deriv["access_decision_ref_and_hash"]["sha256"],
            dec["decision_hash"],
        )

    def test_event_decision_ref_matches_decision_hash(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv)
        self.assertEqual(
            event["decision_ref_and_hash"]["sha256"],
            dec["decision_hash"],
        )

    def test_event_derivation_ref_matches_derivation_hash(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv)
        self.assertEqual(
            event["view_derivation_ref_and_hash"]["sha256"],
            deriv["derivation_hash"],
        )

    def test_all_objects_share_same_principal_operation_nonce(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv)

        for obj in [cap, dec, deriv, event]:
            self.assertEqual(obj["principal"], cap["principal"])
            self.assertEqual(obj["operation"], cap["operation"])
            self.assertEqual(obj["nonce"], cap["nonce"])

    def test_all_objects_have_deny_by_default_true(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv)

        for obj in [cap, dec, deriv, event]:
            self.assertTrue(obj["deny_by_default"])

    def test_all_objects_have_raw_vault_path_not_disclosed(self):
        cap = _make_capability()
        dec = _make_decision(capability=cap)
        deriv = _make_derivation(capability=cap, decision=dec)
        event = _make_event(capability=cap, decision=dec, derivation=deriv)

        for obj in [cap, dec, deriv, event]:
            if "raw_vault_path_disclosure" in obj:
                self.assertFalse(obj["raw_vault_path_disclosure"])
            if "raw_vault_path_disclosed" in obj:
                self.assertFalse(obj["raw_vault_path_disclosed"])


if __name__ == "__main__":
    unittest.main()
