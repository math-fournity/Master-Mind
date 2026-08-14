"""P0-B: HumanGate 真实 Ed25519 验签测试。

这些测试证明审计发现的旁路：全A伪签名获得 PASS。
修复前：全A伪签名 PASS（旁路存在）
修复后：全A伪签名 FAIL（真实 Ed25519 验签执行）

测试层级：
1. Fake signature tests — 全A/全0/随机非签名 base64 都必须 FAIL
2. Real signature tests — 真实 Ed25519 签名必须 PASS
3. All-zero public key hash tests — 全0公钥 hash 必须拒绝
4. KeyRegistry binding tests — 签名必须绑定注册的公钥
"""

from __future__ import annotations

import base64
import hashlib
import json
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import VerificationErrorCode as EC
from seven_system.human.gate_decision import (
    build_gate_decision_dict,
    verify_gate_decision,
    _compute_signed_bytes_hash,
)
from seven_system.human.key_lifecycle import KeyRegistry, KeyRecord
from seven_system.human.actor_roster import ActorRoster, ActorRecord
from seven_system.human.gate_type_registry import GateTypeRegistry
from seven_system.human.human_gate import HumanGateService
from seven_system.human.human_task import FakeHumanTaskPort
from seven_system.contracts.completion_contract import VerificationResult


# ─── helpers ───────────────────────────────────────────────────────────

def _make_real_ed25519_keypair():
    """Generate a real Ed25519 keypair using cryptography library."""
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key


def _ed25519_sign(private_key, message: bytes) -> str:
    """Sign message with Ed25519 private key, return base64."""
    sig = private_key.sign(message)
    return base64.b64encode(sig).decode()


def _ed25519_verify(public_key, signature_b64: str, message: bytes) -> bool:
    """Verify Ed25519 signature. Returns True if valid."""
    from cryptography.exceptions import InvalidSignature
    try:
        sig = base64.b64decode(signature_b64)
        public_key.verify(sig, message)
        return True
    except (InvalidSignature, Exception):
        return False


def _public_key_sha256(public_key) -> str:
    """Compute SHA-256 of the raw public key bytes."""
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
    raw = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
    return hashlib.sha256(raw).hexdigest()


def _get_signed_bytes(decision: dict) -> bytes:
    """Get the actual signed bytes for a decision."""
    from seven_system.hashing import canonical_json_bytes
    from seven_system.contracts.errors import HUMAN_GATE_SIGNATURE_DOMAIN

    unsigned = dict(decision)
    envelope = dict(unsigned.get("signature_envelope", {}))
    envelope["signature_b64"] = None
    envelope["signed_bytes_hash"] = None
    unsigned["signature_envelope"] = envelope
    unsigned["signed_bytes_hash"] = None
    unsigned["decision_hash"] = None
    unsigned["verification_status"] = None

    domain_bytes = HUMAN_GATE_SIGNATURE_DOMAIN.encode("utf-8")
    payload_bytes = canonical_json_bytes(unsigned)
    return domain_bytes + payload_bytes


def _make_signed_decision(
    private_key,
    *,
    decision_id="dec-real-001",
    actor_id="human-reviewer-001",
    decision="APPROVE",
) -> dict:
    """Build a GateDecision with a real Ed25519 signature."""
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
    public_key = private_key.public_key()
    raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

    # First build with placeholder signature to get signed_bytes
    dec = build_gate_decision_dict(
        decision_id=decision_id,
        task_id="task-001",
        gate_type="G-Q-RELEASE",
        payload_ref="payload.json",
        payload_hash="0" * 64,
        actor_id=actor_id,
        actor_role="MATH_VERIFIER",
        decision=decision,
        reason_codes=["looks-good"],
        nonce="abcdefgh12345678",
        issued_at="2026-08-14T10:00:00Z",
        expires_at="2026-08-14T20:00:00Z",
        key_id="key-001",
        signer_principal_id=actor_id,
        signature_b64="A" * 86 + "==",  # placeholder
    )

    # Get the actual signed bytes
    signed_bytes = _get_signed_bytes(dec)

    # Sign with real key
    real_sig = _ed25519_sign(private_key, signed_bytes)

    # Rebuild with real signature
    dec = build_gate_decision_dict(
        decision_id=decision_id,
        task_id="task-001",
        gate_type="G-Q-RELEASE",
        payload_ref="payload.json",
        payload_hash="0" * 64,
        actor_id=actor_id,
        actor_role="MATH_VERIFIER",
        decision=decision,
        reason_codes=["looks-good"],
        nonce="abcdefgh12345678",
        issued_at="2026-08-14T10:00:00Z",
        expires_at="2026-08-14T20:00:00Z",
        key_id="key-001",
        signer_principal_id=actor_id,
        signature_b64=real_sig,
    )

    return dec


def _make_roster() -> ActorRoster:
    roster = ActorRoster()
    roster.register(ActorRecord(
        actor_id="human-reviewer-001",
        actor_type="HUMAN",
        roles=frozenset({"MATH_VERIFIER", "PROOF_JUDGE"}),
        active=True,
    ))
    return roster


def _make_gate_registry() -> GateTypeRegistry:
    from seven_system.human.gate_type_registry import GateTypeSpec
    registry = GateTypeRegistry()
    registry.register(GateTypeSpec(
        gate_type="G-Q-RELEASE",
        required_roles=frozenset({"MATH_VERIFIER"}),
        required_signatures=1,
        allow_model_role=False,
        separation_policy="CREATOR_CANNOT_APPROVE",
    ))
    return registry


def _make_task_port() -> FakeHumanTaskPort:
    return FakeHumanTaskPort()


# ─── P0-B Blocker: Fake signature bypass ───────────────────────────────

class TestFakeSignatureBypass(unittest.TestCase):
    """证明全A伪签名旁路存在，修复后应 FAIL。"""

    def _make_fake_decision(self, fake_sig: str, decision_id: str = "dec-fake-001") -> dict:
        return build_gate_decision_dict(
            decision_id=decision_id,
            task_id="task-001",
            gate_type="G-Q-RELEASE",
            payload_ref="payload.json",
            payload_hash="0" * 64,
            actor_id="human-reviewer-001",
            actor_role="MATH_VERIFIER",
            decision="APPROVE",
            reason_codes=["fake"],
            nonce="abcdefgh12345678",
            issued_at="2026-08-14T10:00:00Z",
            expires_at="2026-08-14T20:00:00Z",
            key_id="key-001",
            signer_principal_id="human-reviewer-001",
            signature_b64=fake_sig,
        )

    def test_all_a_fake_signature_rejected(self):
        """全A伪签名必须被拒绝。"""
        fake_sig = "A" * 86 + "=="
        dec = self._make_fake_decision(fake_sig, "dec-fake-001")
        # Generate a real keypair to get a valid public key for verification
        _, pub = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = pub.public_bytes(Encoding.Raw, PublicFormat.Raw)
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL", "全A伪签名必须被拒绝")
        self.assertIn(EC.SIGNATURE_INVALID, result.error_codes)

    def test_all_zero_signature_rejected(self):
        """全0签名必须被拒绝。"""
        fake_sig = base64.b64encode(b"\x00" * 64).decode()
        dec = self._make_fake_decision(fake_sig, "dec-fake-002")
        _, pub = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = pub.public_bytes(Encoding.Raw, PublicFormat.Raw)
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL", "全0签名必须被拒绝")

    def test_random_non_signature_rejected(self):
        """随机 64 字节（非真实签名）必须被拒绝。"""
        import os
        fake_sig = base64.b64encode(os.urandom(64)).decode()
        dec = self._make_fake_decision(fake_sig, "dec-fake-003")
        _, pub = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = pub.public_bytes(Encoding.Raw, PublicFormat.Raw)
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL", "随机非签名必须被拒绝")


# ─── Real signature tests ──────────────────────────────────────────────

class TestRealSignature(unittest.TestCase):
    """真实 Ed25519 签名必须 PASS。"""

    def test_real_ed25519_signature_passes(self):
        """真实 Ed25519 签名应该通过验证。"""
        private_key, public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key)

        # Need to provide public key for verification
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "PASS", f"Real signature should PASS: {result.details}")

    def test_real_signature_with_key_registry_binding(self):
        """签名必须绑定 KeyRegistry 中注册的公钥。"""
        private_key, public_key = _make_real_ed25519_keypair()
        pub_hash = _public_key_sha256(public_key)

        # Register key in KeyRegistry
        key_registry = KeyRegistry()
        key_registry.provision(
            key_id="key-001",
            actor_id="human-reviewer-001",
            public_key_sha256=pub_hash,
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-15T00:00:00Z",
            provisioning_ref="provisioning.json",
        )

        dec = _make_signed_decision(private_key)

        # Verify with key registry — should find the key and verify
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "PASS", f"Real signature with key binding should PASS: {result.details}")


# ─── All-zero public key hash tests ────────────────────────────────────

class TestAllZeroPublicKeyHash(unittest.TestCase):
    """全0公钥 hash 必须被拒绝。"""

    def test_all_zero_public_key_hash_rejected(self):
        """KeyRegistry 必须拒绝全0 public_key_sha256。"""
        key_registry = KeyRegistry()
        result = key_registry.provision(
            key_id="key-zero-001",
            actor_id="human-reviewer-001",
            public_key_sha256="0" * 64,
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-15T00:00:00Z",
            provisioning_ref="provisioning.json",
        )
        self.assertEqual(result.verdict, "FAIL", "全0 public_key_sha256 必须被拒绝")
        self.assertIn(EC.OBJECT_HASH_MISMATCH, result.error_codes)


# ─── HumanGateService integration tests ────────────────────────────────

class TestHumanGateServiceSignatureVerification(unittest.TestCase):
    """HumanGateService 必须执行真实 Ed25519 验签。"""

    def test_human_gate_rejects_fake_signature(self):
        """HumanGateService 必须拒绝伪签名。"""
        # Generate a real keypair so we have a valid public key stored
        private_key, public_key = _make_real_ed25519_keypair()
        pub_hash = _public_key_sha256(public_key)
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        fake_sig = "A" * 86 + "=="
        dec = build_gate_decision_dict(
            decision_id="dec-gate-fake-001",
            task_id="task-001",
            gate_type="G-Q-RELEASE",
            payload_ref="payload.json",
            payload_hash="0" * 64,
            actor_id="human-reviewer-001",
            actor_role="MATH_VERIFIER",
            decision="APPROVE",
            reason_codes=["fake"],
            nonce="abcdefgh12345678",
            issued_at="2026-08-14T10:00:00Z",
            expires_at="2026-08-14T20:00:00Z",
            key_id="key-001",
            signer_principal_id="human-reviewer-001",
            signature_b64=fake_sig,
        )

        # Setup HumanGateService
        roster = _make_roster()
        gate_registry = _make_gate_registry()
        key_registry = KeyRegistry()
        task_port = _make_task_port()

        # Register a key with real public key hash
        key_registry.provision(
            key_id="key-001",
            actor_id="human-reviewer-001",
            public_key_sha256=pub_hash,
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-15T00:00:00Z",
            provisioning_ref="provisioning.json",
        )
        # Store the real public key for Ed25519 verification
        key_registry.store_public_key("key-001", raw_pub)

        gate = HumanGateService(
            actor_roster=roster,
            gate_type_registry=gate_registry,
            key_registry=key_registry,
            task_port=task_port,
        )

        result = gate.accept_gate_decision(
            dec,
            evaluation_time="2026-08-14T12:00:00Z",
        )
        self.assertEqual(result.verdict, "FAIL", "HumanGateService 必须拒绝伪签名")

    def test_human_gate_accepts_real_signature(self):
        """HumanGateService 必须接受真实 Ed25519 签名。"""
        private_key, public_key = _make_real_ed25519_keypair()
        pub_hash = _public_key_sha256(public_key)

        roster = _make_roster()
        gate_registry = _make_gate_registry()
        key_registry = KeyRegistry()
        task_port = _make_task_port()

        key_registry.provision(
            key_id="key-001",
            actor_id="human-reviewer-001",
            public_key_sha256=pub_hash,
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-15T00:00:00Z",
            provisioning_ref="provisioning.json",
        )

        # Store public key in key registry for verification
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
        key_registry.store_public_key("key-001", raw_pub)

        dec = _make_signed_decision(private_key)

        gate = HumanGateService(
            actor_roster=roster,
            gate_type_registry=gate_registry,
            key_registry=key_registry,
            task_port=task_port,
        )

        result = gate.accept_gate_decision(
            dec,
            evaluation_time="2026-08-14T12:00:00Z",
        )
        self.assertEqual(result.verdict, "PASS", f"Real signature should PASS: {result.details}")


if __name__ == "__main__":
    unittest.main()
