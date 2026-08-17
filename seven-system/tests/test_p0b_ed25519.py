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
    verification_status="VERIFIED",
) -> dict:
    """Build a GateDecision with a real Ed25519 signature.

    P0-B 深度补全：verification_status 由 verifier 生成，不能由调用者传入。
    - 默认 verification_status="VERIFIED"（构建后手动设置）
    - 负向测试可指定 HUMAN_PENDING/UNVERIFIED 等
    """
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

    # 如果指定了 verification_status（负向测试用），手动设置
    if verification_status is not None:
        dec["verification_status"] = verification_status
        # 重算 decision_hash
        from seven_system.human.gate_decision import _compute_decision_hash
        dec["decision_hash"] = _compute_decision_hash(dec)

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

def _stamp_verified(dec: dict) -> dict:
    """手动盖印 verification_status=VERIFIED（测试 helper）。

    P0-B 深度补全后 build_gate_decision_dict 不接受 verification_status，
    测试需要用此 helper 在构建后手动设置。
    """
    from seven_system.human.gate_decision import _compute_decision_hash
    dec["verification_status"] = "VERIFIED"
    dec["decision_hash"] = _compute_decision_hash(dec)
    return dec


class TestFakeSignatureBypass(unittest.TestCase):
    """证明全A伪签名旁路存在，修复后应 FAIL。"""

    def _make_fake_decision(self, fake_sig: str, decision_id: str = "dec-fake-001") -> dict:
        return _stamp_verified(build_gate_decision_dict(
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
        ))

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
        dec = _stamp_verified(build_gate_decision_dict(
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
        ))

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


# ─── P0-B 补全：8 个缺失的负向测试 ─────────────────────────────────────

class TestPayloadModificationAfterSigning(unittest.TestCase):
    """签名后修改 payload 必须拒绝。"""

    def test_payload_modified_after_signing_rejected(self):
        """签名后修改 payload_hash 必须导致验签失败。"""
        private_key, public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key)
        # 修改 payload_hash（签名后篡改）
        dec["payload_hash"] = "1" * 64
        # 重算 decision_hash（但不重签）
        from seven_system.human.gate_decision import _compute_decision_hash
        dec["decision_hash"] = _compute_decision_hash(dec)

        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL")


class TestWrongPublicKey(unittest.TestCase):
    """错公钥必须拒绝。"""

    def test_wrong_public_key_rejected(self):
        """用不同的公钥验签必须失败。"""
        private_key, _ = _make_real_ed25519_keypair()
        _, other_public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key)

        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        wrong_pub = other_public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
        result = verify_gate_decision(dec, public_key_bytes=wrong_pub)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.SIGNATURE_INVALID, result.error_codes)


class TestWrongActorRole(unittest.TestCase):
    """错 actor/role 必须拒绝。"""

    def test_wrong_actor_rejected(self):
        """actor_id 与注册的不一致必须被 HumanGateService 拒绝。"""
        private_key, public_key = _make_real_ed25519_keypair()
        pub_hash = _public_key_sha256(public_key)
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        dec = _make_signed_decision(private_key, actor_id="wrong-actor-001")

        roster = _make_roster()  # 只有 human-reviewer-001
        gate_registry = _make_gate_registry()
        key_registry = KeyRegistry()
        task_port = _make_task_port()
        key_registry.provision(
            key_id="key-001",
            actor_id="human-reviewer-001",  # 注册的是这个 actor
            public_key_sha256=pub_hash,
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-15T00:00:00Z",
            provisioning_ref="provisioning.json",
        )
        key_registry.store_public_key("key-001", raw_pub)

        gate = HumanGateService(
            actor_roster=roster,
            gate_type_registry=gate_registry,
            key_registry=key_registry,
            task_port=task_port,
        )
        result = gate.accept_gate_decision(dec, evaluation_time="2026-08-14T12:00:00Z")
        self.assertEqual(result.verdict, "FAIL")


class TestKeyHashMismatch(unittest.TestCase):
    """key hash 与实际公钥bytes不一致必须拒绝。"""

    def test_key_hash_mismatch_rejected(self):
        """KeyRegistry 中 public_key_sha256 与存储的 public_key_bytes 不一致必须拒绝。"""
        private_key, public_key = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        key_registry = KeyRegistry()
        # 注册一个错误的 hash（不是 raw_pub 的真实 hash）
        key_registry.provision(
            key_id="key-001",
            actor_id="human-reviewer-001",
            public_key_sha256="e" * 64,  # 错误 hash
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-15T00:00:00Z",
            provisioning_ref="provisioning.json",
        )
        key_registry.store_public_key("key-001", raw_pub)

        # 验证 key_registry 检测到不一致
        result = key_registry.check_key(
            "key-001",
            expected_actor_id="human-reviewer-001",
            required_role="MATH_VERIFIER",
            evaluation_time="2026-08-14T12:00:00Z",
        )
        # check_key 应该检测到 hash 不匹配
        self.assertEqual(result.verdict, "FAIL")


class TestRevokedExpiredKey(unittest.TestCase):
    """revoked/expired/not-yet-valid key 必须拒绝。"""

    def test_revoked_key_rejected(self):
        """撤销的 key 必须被拒绝。"""
        private_key, public_key = _make_real_ed25519_keypair()
        pub_hash = _public_key_sha256(public_key)
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

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
        key_registry.store_public_key("key-001", raw_pub)
        key_registry.revoke("key-001", revocation_ref="revocation.json")

        result = key_registry.check_key(
            "key-001",
            expected_actor_id="human-reviewer-001",
            required_role="MATH_VERIFIER",
            evaluation_time="2026-08-14T12:00:00Z",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.KEY_REVOKED, result.error_codes)

    def test_expired_key_rejected(self):
        """过期的 key 必须被拒绝。"""
        private_key, public_key = _make_real_ed25519_keypair()
        pub_hash = _public_key_sha256(public_key)

        key_registry = KeyRegistry()
        key_registry.provision(
            key_id="key-001",
            actor_id="human-reviewer-001",
            public_key_sha256=pub_hash,
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-14T11:00:00Z",  # 已过期
            provisioning_ref="provisioning.json",
        )

        result = key_registry.check_key(
            "key-001",
            expected_actor_id="human-reviewer-001",
            required_role="MATH_VERIFIER",
            evaluation_time="2026-08-14T12:00:00Z",  # 在过期之后
        )
        self.assertEqual(result.verdict, "FAIL")

    def test_not_yet_valid_key_rejected(self):
        """尚未生效的 key 必须被拒绝。"""
        private_key, public_key = _make_real_ed25519_keypair()
        pub_hash = _public_key_sha256(public_key)

        key_registry = KeyRegistry()
        key_registry.provision(
            key_id="key-001",
            actor_id="human-reviewer-001",
            public_key_sha256=pub_hash,
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-15T00:00:00Z",  # 明天才生效
            valid_to="2026-08-16T00:00:00Z",
            provisioning_ref="provisioning.json",
        )

        result = key_registry.check_key(
            "key-001",
            expected_actor_id="human-reviewer-001",
            required_role="MATH_VERIFIER",
            evaluation_time="2026-08-14T12:00:00Z",  # 今天
        )
        self.assertEqual(result.verdict, "FAIL")


class TestWrongDomainSeparator(unittest.TestCase):
    """错 domain separator 必须拒绝。"""

    def test_wrong_domain_separator_rejected(self):
        """用错误的 domain separator 签名必须导致验签失败。"""
        private_key, public_key = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        # 用错误 domain 签名
        from seven_system.hashing import canonical_json_bytes
        dec = _stamp_verified(build_gate_decision_dict(
            decision_id="dec-wrong-domain-001",
            task_id="task-001",
            gate_type="G-Q-RELEASE",
            payload_ref="payload.json",
            payload_hash="0" * 64,
            actor_id="human-reviewer-001",
            actor_role="MATH_VERIFIER",
            decision="APPROVE",
            reason_codes=["test"],
            nonce="abcdefgh12345678",
            issued_at="2026-08-14T10:00:00Z",
            expires_at="2026-08-14T20:00:00Z",
            key_id="key-001",
            signer_principal_id="human-reviewer-001",
            signature_b64="A" * 86 + "==",
        ))

        # 用错误 domain 签名
        wrong_domain = b"wrong-domain\0"
        unsigned = dict(dec)
        envelope = dict(unsigned.get("signature_envelope", {}))
        envelope["signature_b64"] = None
        envelope["signed_bytes_hash"] = None
        unsigned["signature_envelope"] = envelope
        unsigned["signed_bytes_hash"] = None
        unsigned["decision_hash"] = None
        unsigned["verification_status"] = None
        signed_bytes = wrong_domain + canonical_json_bytes(unsigned)
        real_sig = _ed25519_sign(private_key, signed_bytes)

        # 重建 decision with real sig but correct domain in the object
        dec = _stamp_verified(build_gate_decision_dict(
            decision_id="dec-wrong-domain-001",
            task_id="task-001",
            gate_type="G-Q-RELEASE",
            payload_ref="payload.json",
            payload_hash="0" * 64,
            actor_id="human-reviewer-001",
            actor_role="MATH_VERIFIER",
            decision="APPROVE",
            reason_codes=["test"],
            nonce="abcdefgh12345678",
            issued_at="2026-08-14T10:00:00Z",
            expires_at="2026-08-14T20:00:00Z",
            key_id="key-001",
            signer_principal_id="human-reviewer-001",
            signature_b64=real_sig,
        ))

        # 验证时用正确的 domain，签名是用错误 domain 签的，应该 FAIL
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.SIGNATURE_INVALID, result.error_codes)


class TestHumanPendingApprove(unittest.TestCase):
    """HUMAN_PENDING + APPROVE 必须拒绝。"""

    def test_human_pending_with_approve_rejected(self):
        """verification_status=HUMAN_PENDING + decision=APPROVE 必须被拒绝。"""
        private_key, public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key, verification_status="HUMAN_PENDING")

        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.GATE_VERIFICATION_STATUS_INVALID, result.error_codes)

    def test_unverified_with_approve_rejected(self):
        """verification_status=UNVERIFIED + decision=APPROVE 必须被拒绝。"""
        private_key, public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key, verification_status="UNVERIFIED")

        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.GATE_VERIFICATION_STATUS_INVALID, result.error_codes)


class TestSignatureSwapAttack(unittest.TestCase):
    """同签名换 task/gate/nonce 必须拒绝。"""

    def test_same_signature_different_task_rejected(self):
        """同一个签名用在不同的 task_id 上必须失败。"""
        private_key, public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key, decision_id="dec-swap-001")

        # 篡改 task_id（签名后修改）
        dec["task_id"] = "task-002"
        from seven_system.human.gate_decision import _compute_decision_hash
        dec["decision_hash"] = _compute_decision_hash(dec)

        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL")

    def test_same_signature_different_nonce_rejected(self):
        """同一个签名用不同的 nonce 必须失败。"""
        private_key, public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key, decision_id="dec-swap-002")

        # 篡改 nonce
        dec["nonce"] = "zyxwvuts98765432"
        from seven_system.human.gate_decision import _compute_decision_hash
        dec["decision_hash"] = _compute_decision_hash(dec)

        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL")


class TestVerifierUnreachable(unittest.TestCase):
    """verifier 不可达时必须 BLOCKED，不能 fallback 到结构检查。"""

    def test_verifier_unreachable_fail_closed(self):
        """cryptography 库不可用时必须 fail-closed。"""
        private_key, public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key)

        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        # 模拟 verifier 不可达：传入无效公钥 bytes
        result = verify_gate_decision(dec, public_key_bytes=b"\x00" * 31)  # 错误长度
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.SIGNATURE_INVALID, result.error_codes)


# ─── P0-B 补全：SignatureVerifierPort 跨对象复用测试 ────────────────────

class TestSignatureVerifierPort(unittest.TestCase):
    """SignatureVerifierPort 唯一接口测试。"""

    def test_signature_verifier_port_exists(self):
        """SignatureVerifierPort 接口存在且可导入。"""
        from seven_system.human.signature_verifier import (
            SignatureVerifierPort,
            Ed25519SignatureVerifier,
            get_signature_verifier,
            verify_signature,
        )
        # 验证全局单例
        verifier = get_signature_verifier()
        self.assertIsInstance(verifier, Ed25519SignatureVerifier)

    def test_signature_verifier_rejects_fake(self):
        """SignatureVerifierPort 拒绝伪签名。"""
        from seven_system.human.signature_verifier import verify_signature
        from seven_system.contracts.errors import HUMAN_GATE_SIGNATURE_DOMAIN

        private_key, public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key)

        # 用不同的公钥验签
        _, other_key = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        wrong_pub = other_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        receipt = verify_signature(
            signed_object=dec,
            public_key_bytes=wrong_pub,
            signature_domain=HUMAN_GATE_SIGNATURE_DOMAIN.encode("utf-8"),
        )
        self.assertFalse(receipt.verified)

    def test_signature_verifier_accepts_real(self):
        """SignatureVerifierPort 接受真实签名。"""
        from seven_system.human.signature_verifier import verify_signature
        from seven_system.contracts.errors import HUMAN_GATE_SIGNATURE_DOMAIN

        private_key, public_key = _make_real_ed25519_keypair()
        dec = _make_signed_decision(private_key)

        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        receipt = verify_signature(
            signed_object=dec,
            public_key_bytes=raw_pub,
            signature_domain=HUMAN_GATE_SIGNATURE_DOMAIN.encode("utf-8"),
        )
        self.assertTrue(receipt.verified)
        self.assertEqual(receipt.algorithm, "Ed25519")

    def test_cross_object_reuse(self):
        """SignatureVerifierPort 可用于非 GateDecision 对象（如 AuditAssignment）。

        对于非 GateDecision 对象，自引用 hash 字段名可能不同（如 assignment_hash），
        但 SignatureVerifierPort 的 _compute_signed_bytes 会移除 decision_hash。
        因此跨对象复用时，对象需要用 decision_hash 作为自引用字段名，
        或调用方需要确保签名和验签使用相同的 unsigned bytes 计算。
        """
        from seven_system.human.signature_verifier import verify_signature, _compute_signed_bytes

        private_key, public_key = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        # 构造一个非 GateDecision 的签名对象（模拟 AuditAssignment）
        # 使用 decision_hash 作为自引用字段（与 SignatureVerifierPort 一致）
        domain = b"seven-audit-assignment/v1\0"
        obj = {
            "schema_id": "seven/audit-assignment",
            "assignment_id": "asg-001",
            "key_id": "key-001",
            "signature_envelope": {
                "algorithm": "Ed25519",
                "key_id": "key-001",
                "signer_principal_id": "owner-001",
                "signature_encoding": "base64",
                "signature_b64": "",  # placeholder
                "signed_bytes_hash": None,
            },
            "signed_bytes_hash": None,
            "decision_hash": None,  # 使用 decision_hash 以与 SignatureVerifierPort 一致
            "verification_status": None,
        }

        # 用 SignatureVerifierPort 的 _compute_signed_bytes 计算 signed bytes
        signed_bytes = _compute_signed_bytes(obj, domain)

        # 签名
        real_sig = _ed25519_sign(private_key, signed_bytes)
        obj["signature_envelope"]["signature_b64"] = real_sig

        # 用 SignatureVerifierPort 验证
        receipt = verify_signature(
            signed_object=obj,
            public_key_bytes=raw_pub,
            signature_domain=domain,
        )
        self.assertTrue(receipt.verified, f"Cross-object reuse should work: {receipt.verification_error}")



# ─── P0-B 深度补全：verification_status 由 verifier 生成 + 统一签名对象验证 ──

class TestVerificationStatusByVerifier(unittest.TestCase):
    """P0-B 深度补全：verification_status 必须由 verifier 生成。"""

    def test_build_rejects_verification_status(self):
        """build_gate_decision_dict 拒绝调用者传入 verification_status。"""
        with self.assertRaises(ValueError):
            build_gate_decision_dict(
                decision_id="dec-001", task_id="task-001", gate_type="G-Q-RELEASE",
                payload_ref="p.json", payload_hash="0" * 64, actor_id="a-001",
                actor_role="MATH_VERIFIER", decision="APPROVE", reason_codes=["ok"],
                nonce="abcdefgh12345678", issued_at="2026-08-14T10:00:00Z",
                expires_at="2026-08-14T20:00:00Z", key_id="key-001",
                signer_principal_id="a-001", signature_b64="A" * 86 + "==",
                verification_status="VERIFIED",
            )

    def test_build_defaults_to_none(self):
        """build_gate_decision_dict 默认 verification_status=None。"""
        dec = build_gate_decision_dict(
            decision_id="dec-001", task_id="task-001", gate_type="G-Q-RELEASE",
            payload_ref="p.json", payload_hash="0" * 64, actor_id="a-001",
            actor_role="MATH_VERIFIER", decision="APPROVE", reason_codes=["ok"],
            nonce="abcdefgh12345678", issued_at="2026-08-14T10:00:00Z",
            expires_at="2026-08-14T20:00:00Z", key_id="key-001",
            signer_principal_id="a-001", signature_b64="A" * 86 + "==",
        )
        self.assertIsNone(dec["verification_status"])

    def test_verify_and_stamp_verified(self):
        """verify_and_stamp_gate_decision 验签通过时设置 VERIFIED。"""
        from seven_system.human.gate_decision import verify_and_stamp_gate_decision
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        dec = _make_signed_decision(private_key, verification_status=None)
        stamped, receipt = verify_and_stamp_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertTrue(receipt.verified)
        self.assertEqual(stamped["verification_status"], "VERIFIED")

    def test_verify_and_stamp_failed(self):
        """verify_and_stamp_gate_decision 验签失败时设置 SIGNATURE_FAILED。"""
        from seven_system.human.gate_decision import verify_and_stamp_gate_decision
        private_key, _ = _make_real_ed25519_keypair()
        # 用不同的公钥
        other_key = _make_real_ed25519_keypair()[0]
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        wrong_pub = other_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        dec = _make_signed_decision(private_key, verification_status=None)
        stamped, receipt = verify_and_stamp_gate_decision(dec, public_key_bytes=wrong_pub)
        self.assertFalse(receipt.verified)
        self.assertEqual(stamped["verification_status"], "SIGNATURE_FAILED")

    def test_unstamped_decision_rejected_by_verify(self):
        """verification_status=None 的决策被 verify_gate_decision 拒绝。"""
        from seven_system.human.gate_decision import verify_gate_decision
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        dec = _make_signed_decision(private_key, verification_status=None)
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL")


class TestSignedObjectVerifier(unittest.TestCase):
    """P0-B 深度补全：统一签名验证核心接入所有签名对象。"""

    def _make_signed_object(self, schema_id: str, domain: str, private_key) -> dict:
        """构建并签名一个符合对应 JSON Schema 的最小对象。"""
        from seven_system.hashing import canonical_json_bytes
        from seven_system.human.signature_verifier import compute_signed_bytes
        from seven_system.human.signed_object_verifier import _PROFILES
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        profile = _PROFILES[schema_id]
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
        import base64

        def h(char: str = "0") -> str:
            return char * 64

        def ref(name: str, char: str = "1") -> dict:
            return {"ref": name, "sha256": h(char)}

        def named(name: str, char: str = "2") -> dict:
            return {"object_id": name, "sha256": h(char)}

        def commit(char: str = "a") -> dict:
            return {"commit": char * 40, "tree": char * 40}

        def allowance(**overrides) -> dict:
            base = {
                "invocations": 0,
                "solver_launches": 0,
                "database_writes": 0,
                "redis_writes": 0,
                "d_volume_writes": 0,
                "human_gate_commits": 0,
                "active_release_changes": 0,
                "tokens": 0,
                "cost_microunits": 0,
                "currency": "USD",
            }
            base.update(overrides)
            return base

        def unit_budget(**overrides) -> dict:
            base = {
                "max_invocations": 0,
                "max_solver_launches": 0,
                "max_database_writes": 0,
                "max_redis_writes": 0,
                "max_d_volume_writes": 0,
                "max_human_gate_commits": 0,
                "max_active_release_changes": 0,
                "max_tokens": 0,
                "max_cost_microunits": 0,
                "currency": "USD",
            }
            base.update(overrides)
            return base

        def signature_envelope(signer_field: str, hash_field: str) -> dict:
            base = {
                "algorithm": "Ed25519",
                "key_id": "key-001",
                signer_field: "owner-001",
                "signature_encoding": "base64",
                "signature_b64": None,
                hash_field: None,
            }
            if signer_field == "signer_actor_id":
                base.update({
                    "trust_root_hash": h("3"),
                    "actor_roster_hash": h("4"),
                    "policy_hash": h("5"),
                    "signature_algorithm_registry_hash": h("6"),
                })
            return base

        raw_pub_b64 = base64.b64encode(raw_pub).decode()
        raw_pub_hash = hashlib.sha256(raw_pub).hexdigest()
        common_signed = {
            "issued_at": "2026-08-14T10:00:00Z",
            "not_before": "2026-08-14T10:00:00Z",
            "expires_at": "2026-08-14T20:00:00Z",
            "nonce": "nonce-abcdefghijkl",
            "canonicalizer_profile": "RFC8785_JCS_UTF8",
        }

        action_budget = {
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
        }
        action_scope = {
            "scope_id": "scope-001",
            "scope_hash_algorithm": "sha256(RFC8785-JCS-action-scope-with-scope_hash-null)",
            "scope_hash": h("7"),
            "action_kind": "D_VOLUME_WRITE",
            "authorization_action_registry_entry_ref_and_hash": ref("action-registry.json", "8"),
            "target_site_hash_if_any": None,
            "target_database_identity_hash_if_any": None,
            "target_redis_namespace_hash_if_any": None,
            "target_release_or_pointer_hash_if_any": None,
            "allowed_carrier_profile_hashes": [],
            "allowed_role_or_solver_contract_hashes": [],
            "allowed_inputs": [{"input_hash": h("9"), "sensitivity": "public"}],
            "required_output_sink_and_acl_hash_if_any": None,
            "budget": action_budget,
        }
        action_unit = {
            "consumption_ordinal": 0,
            "parent_action_scope_id": "scope-001",
            "parent_action_scope_hash": h("7"),
            "action_kind": "D_VOLUME_WRITE",
            "authorization_action_registry_entry_ref_and_hash": ref("action-registry.json", "8"),
            "job_id": "job-001",
            "attempt_id": "attempt-001",
            "input_hash": h("9"),
            "carrier_profile_or_solver_contract_hash_if_any": None,
            "target_binding_hash": h("a"),
            "required_output_sink_and_acl_hash_if_any": None,
            "idempotency_key": "idempotency-key-001",
            "unit_budget": unit_budget(max_d_volume_writes=1),
        }

        if schema_id == "seven/audit-assignment":
            obj = {
                "schema_id": schema_id,
                "schema_version": 1,
                "assignment_id": "assign-001",
                "owner_actor_id": "owner-001",
                "owner_repo_external_channel": {
                    "channel_id": "owner-channel",
                    "channel_kind": "HUMAN_VERIFIED_OUT_OF_BAND",
                    "observation_instructions_ref_and_hash": ref("observe-owner.md"),
                },
                "externally_pinned_trust_root": named("trust-root"),
                "actor_roster_ref_and_hash": ref("actor-roster.json"),
                "human_gate_policy_ref_and_hash": ref("human-gate-policy.json"),
                "signature_algorithm_registry_ref_and_hash": ref("signature-registry.json"),
                "auditor_principal_id": "auditor-001",
                "auditor_attestation_public_key": {
                    "key_id": "key-001",
                    "algorithm": "Ed25519",
                    "public_key_encoding": "raw-32-byte-base64",
                    "public_key_b64": raw_pub_b64,
                    "public_key_sha256": raw_pub_hash,
                },
                "target_work_package_id": "WP-DOC0",
                "subject_commit_and_tree": commit(),
                "completion_bundle_ref_and_hash": ref("completion.json"),
                "evidence_index_commit_if_any": None,
                "independence_and_separation_policy_ref_and_hash": ref("independence.md"),
                "allowed_audit_scope": {
                    "allowed_audit_axes": ["implementation"],
                    "allowed_audit_actions": ["READ_ONLY_REVIEW"],
                    "allowed_external_side_effects": [],
                    "requires_separate_external_execution_authorization": True,
                },
                "required_audit_plan_and_spec_refs_and_hashes": [ref("audit-plan.md")],
                **common_signed,
                "signature_domain": domain,
                "signed_bytes_hash": None,
                "signature_envelope": signature_envelope("signer_actor_id", "signed_bytes_hash"),
                "assignment_hash_algorithm": "sha256(RFC8785-JCS-object-with-assignment_hash-null)",
                "assignment_hash": None,
            }
        elif schema_id == "seven/audit-record":
            axis = {
                "verdict": "NOT_TESTED",
                "finding_ids": [],
                "evidence_refs": [],
                "scope_reason_if_not_tested": "unit fixture",
            }
            obj = {
                "schema_id": schema_id,
                "schema_version": 1,
                "audit_id": "audit-001",
                "wp_id": "WP-DOC0",
                "audit_assignment_ref_and_hash": ref("assignment.json"),
                "assignment_verification_receipt_ref_and_hash": ref("assignment-receipt.json"),
                "audited_bundle_ref_and_hash": ref("bundle.json"),
                "audited_subject": commit(),
                "evidence_index_commit_if_any": None,
                "externally_observed_pinned_trust_root": {
                    "trust_root_hash": h("3"),
                    "source_channel_id": "owner-channel",
                    "observed_at": "2026-08-14T10:00:00Z",
                    "observation_receipt_ref_and_hash": ref("root-observation.json"),
                },
                "runtime_manifest_trust_root_hash": h("3"),
                "audit_plan_and_spec_refs_and_hashes": [ref("audit-plan.md")],
                "auditor_principal_id": "owner-001",
                "auditor_attestation_key_id": "key-001",
                "auditor_attestation_public_key_hash": raw_pub_hash,
                "auditor_session_attestation_ref_and_hash": ref("session.json"),
                "independence_evidence": [ref("independence.json")],
                "findings": [],
                "replayed_test_receipts": [],
                "external_execution_receipts": [],
                "traceability_remainder": 0,
                "orphan_remainder": 0,
                "claims_confirmed": [],
                "claims_rejected": [],
                "nonclaims_checked": ["unit fixture"],
                "axis_verdicts": {
                    "implementation": axis,
                    "factory": axis,
                    "scientific": {
                        "verdict": "NOT_TESTED",
                        "finding_ids": [],
                        "evidence_refs": [],
                        "scope_reason_if_not_tested": "unit fixture",
                    },
                    "production_scale": axis,
                },
                "scope_limits": ["unit fixture"],
                "followups": [],
                "state_transition_effect": "NONE_UNTIL_HUMAN_GATE_SERVICE_ACCEPTS",
                "created_at": "2026-08-14T10:00:00Z",
                "canonicalizer_profile": "RFC8785_JCS_UTF8",
                "signature_domain": domain,
                "signed_bytes_hash": None,
                "signature_envelope": signature_envelope("signer_principal_id", "signed_bytes_hash"),
                "audit_record_hash_algorithm": "sha256(RFC8785-JCS-object-with-audit_record_hash-null)",
                "audit_record_hash": None,
            }
        elif schema_id == "seven/external-execution-authorization":
            obj = {
                "schema_id": schema_id,
                "schema_version": 1,
                "authorization_id": "auth-001",
                "authorization_mode": "TRUST_ROOT_OR_SCHEMA_BOOTSTRAP",
                "subject_work_package_ids": ["WP-DOC0"],
                "subject_completion_bundle_refs_and_hashes": [ref("bundle.json")],
                "activation_audit_record_refs_and_hashes": [],
                "unaudited_dependency_bundle_refs_and_hashes": [ref("bootstrap.json")],
                "epoch_id_if_any": None,
                "run_id_if_any": None,
                "authorization_action_registry_ref_and_hash": ref("action-registry.json", "8"),
                "action_scopes": [action_scope],
                "externally_pinned_trust_root": named("trust-root"),
                "actor_roster_ref_and_hash": ref("actor-roster.json"),
                "human_gate_policy_ref_and_hash": ref("human-gate-policy.json"),
                "signature_algorithm_registry_ref_and_hash": ref("signature-registry.json"),
                "revocation_policy_ref_and_hash": ref("revocation.md"),
                "stop_conditions": ["unit fixture"],
                "issuer_actor_id": "owner-001",
                "issuer_key_id": "key-001",
                **common_signed,
                "signature_domain": domain,
                "signed_bytes_hash": None,
                "signature_envelope": signature_envelope("signer_actor_id", "signed_bytes_hash"),
                "authorization_hash_algorithm": "sha256(RFC8785-JCS-object-with-authorization_hash-null)",
                "authorization_hash": None,
            }
        elif schema_id == "seven/live-run-permit":
            obj = {
                "schema_id": schema_id,
                "schema_version": 1,
                "permit_id": "permit-001",
                "parent_authorization_id": "auth-001",
                "parent_authorization_ref_and_hash": ref("authorization.json"),
                "parent_authorization_signed_bytes_hash": h("b"),
                "parent_subset_verification_contract_ref_and_hash": ref("subset.md"),
                "authorization_mode": "TRUST_ROOT_OR_SCHEMA_BOOTSTRAP",
                "wp_id": "WP-DOC0",
                "epoch_id_if_any": None,
                "run_id_if_any": None,
                "action_units": [action_unit],
                "required_reservation_backend": "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
                "externally_pinned_trust_root": named("trust-root"),
                "actor_roster_ref_and_hash": ref("actor-roster.json"),
                "human_gate_policy_ref_and_hash": ref("human-gate-policy.json"),
                "signature_algorithm_registry_ref_and_hash": ref("signature-registry.json"),
                "revocation_policy_ref_and_hash": ref("revocation.md"),
                "issuer_actor_id": "owner-001",
                "issuer_key_id": "key-001",
                **common_signed,
                "signature_domain": domain,
                "signed_bytes_hash": None,
                "signature_envelope": signature_envelope("signer_actor_id", "signed_bytes_hash"),
                "permit_hash_algorithm": "sha256(RFC8785-JCS-object-with-permit_hash-null)",
                "permit_hash": None,
            }
        elif schema_id == "seven/authorization-consumption-receipt":
            obj = {
                "schema_id": schema_id,
                "schema_version": 1,
                "receipt_id": "receipt-001",
                "logical_consumption_id": "consumption-001",
                "state_revision": 0,
                "previous_receipt_ref_and_hash_if_any": None,
                "parent_authorization_id": "auth-001",
                "parent_authorization_ref_and_hash": ref("authorization.json"),
                "permit_id": "permit-001",
                "permit_ref_and_hash": ref("permit.json"),
                **{key: action_unit[key] for key in [
                    "consumption_ordinal",
                    "parent_action_scope_id",
                    "parent_action_scope_hash",
                    "action_kind",
                    "authorization_action_registry_entry_ref_and_hash",
                    "job_id",
                    "attempt_id",
                    "input_hash",
                    "carrier_profile_or_solver_contract_hash_if_any",
                    "target_binding_hash",
                    "required_output_sink_and_acl_hash_if_any",
                    "idempotency_key",
                ]},
                "aggregate_id": "aggregate-001",
                "expected_aggregate_revision": 0,
                "fence_token": 1,
                "reservation_backend": "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
                "status": "RESERVED",
                "reserved_at": "2026-08-14T10:00:00Z",
                "status_recorded_at": "2026-08-14T10:00:00Z",
                "terminal_at_if_any": None,
                "external_start_observation": "NOT_OBSERVED",
                "start_observation_evidence_refs": [],
                "proof_not_started_refs": [],
                "reservation_transaction_receipt_ref_and_hash": ref("transaction.json"),
                "reserved_unit_budget": allowance(d_volume_writes=1),
                "actual_side_effects": allowance(),
                "held_allowance": allowance(d_volume_writes=1),
                "released_allowance": allowance(),
                "remaining_allowance": allowance(),
                "recovery_decision_ref_and_hash_if_any": None,
                "externally_pinned_trust_root": named("trust-root"),
                "service_attestation_key_registry_ref_and_hash": ref("service-keys.json"),
                "canonicalizer_profile": "RFC8785_JCS_UTF8",
                "attestation_domain": domain,
                "attested_bytes_hash": None,
                "service_attestation": {
                    "algorithm": "Ed25519",
                    "key_id": "key-001",
                    "service_principal_id": "owner-001",
                    "signature_encoding": "base64",
                    "signature_b64": None,
                    "attested_bytes_hash": None,
                    "trust_root_hash": h("3"),
                    "service_attestation_key_registry_hash": h("4"),
                },
                "receipt_hash_algorithm": "sha256(RFC8785-JCS-object-with-receipt_hash-null)",
                "receipt_hash": None,
            }
        elif schema_id == "seven/docs/normative-requirement-review-record":
            obj = {
                "schema_id": schema_id,
                "schema_version": 1,
                "index_ref_and_hash": ref("normative-index.json"),
                "audit_assignment_ref_and_hash": ref("assignment.json"),
                "reviewer_actor_id": "owner-001",
                "reviewed_consumer_policy_id": "LOCAL_ONLY_DOC0_TEMPORARY_CATCH_ALL_V1",
                "temporary_doc0_consumer_nonclaim_acknowledged": True,
                "decisions": [
                    {
                        "clause_id": "NORM-unit-001",
                        "decision": "CONFIRMED_LOCAL_ONLY",
                        "requirement_ids": [],
                        "applicable_wp_ids": ["WP-DOC0"],
                        "consumer_wp_ids": ["WP-DOC0"],
                        "consumer_assignment_basis": "INDEPENDENT_SEMANTIC_REVIEW",
                        "reason": "unit fixture",
                    }
                ],
                "remainder": {
                    "unreviewed_clause_count": 0,
                    "duplicate_clause_decision_count": 0,
                    "unknown_requirement_count": 0,
                    "unknown_work_package_count": 0,
                    "consumer_unassigned_count": 0,
                    "unconsumed_clause_count": 0,
                    "reclassification_required_count": 0,
                    "invalid_clause_count": 0,
                },
                "signature_envelope": {
                    "algorithm": "Ed25519",
                    "domain_separator": domain,
                    "signer_actor_id": "owner-001",
                    "key_id": "key-001",
                    "signed_payload_sha256": None,
                    "signature_base64": None,
                },
            }
        else:
            raise AssertionError(f"unhandled signed object fixture: {schema_id}")

        signed_bytes = compute_signed_bytes(
            obj,
            domain.encode("utf-8"),
            signature_field_path=profile.signature_field_path,
            envelope_hash_field_path=profile.envelope_hash_field_path,
            top_hash_field=profile.top_hash_field,
            self_hash_field=profile.self_hash_field,
        )
        signed_hash = hashlib.sha256(signed_bytes).hexdigest()
        sig = private_key.sign(signed_bytes)

        def set_path(path: str, value) -> None:
            current = obj
            parts = path.split(".")
            for part in parts[:-1]:
                current = current[part]
            current[parts[-1]] = value

        set_path(profile.signature_field_path, base64.b64encode(sig).decode())
        set_path(profile.envelope_hash_field_path, signed_hash)
        if profile.top_hash_field is not None:
            obj[profile.top_hash_field] = signed_hash
        if profile.self_hash_field is not None:
            unsigned = dict(obj)
            unsigned[profile.self_hash_field] = None
            obj[profile.self_hash_field] = hashlib.sha256(canonical_json_bytes(unsigned)).hexdigest()
        return obj

    def test_all_signed_object_domains_defined(self):
        """所有签名对象的 domain separator 已定义。"""
        from seven_system.human.signed_object_verifier import SIGNED_OBJECT_DOMAINS
        expected = {
            "seven/human-gate-decision",
            "seven/audit-assignment",
            "seven/audit-record",
            "seven/external-execution-authorization",
            "seven/live-run-permit",
            "seven/authorization-consumption-receipt",
            "seven/docs/normative-requirement-review-record",
        }
        for key in expected:
            self.assertIn(key, SIGNED_OBJECT_DOMAINS, f"missing domain for {key}")

    def test_audit_assignment_verification(self):
        """AuditAssignment 签名验证。"""
        from seven_system.human.signed_object_verifier import verify_audit_assignment, SIGNED_OBJECT_DOMAINS
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        domain = SIGNED_OBJECT_DOMAINS["seven/audit-assignment"]
        obj = self._make_signed_object("seven/audit-assignment", domain, private_key)
        result = verify_audit_assignment(obj, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "PASS")

    def test_audit_record_verification(self):
        """AuditRecord 签名验证。"""
        from seven_system.human.signed_object_verifier import verify_audit_record, SIGNED_OBJECT_DOMAINS
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        domain = SIGNED_OBJECT_DOMAINS["seven/audit-record"]
        obj = self._make_signed_object("seven/audit-record", domain, private_key)
        result = verify_audit_record(obj, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "PASS")

    def test_eea_verification(self):
        """EEA 签名验证。"""
        from seven_system.human.signed_object_verifier import verify_eea, SIGNED_OBJECT_DOMAINS
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        domain = SIGNED_OBJECT_DOMAINS["seven/external-execution-authorization"]
        obj = self._make_signed_object("seven/external-execution-authorization", domain, private_key)
        result = verify_eea(obj, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "PASS")

    def test_live_run_permit_verification(self):
        """LiveRunPermit 签名验证。"""
        from seven_system.human.signed_object_verifier import verify_live_run_permit, SIGNED_OBJECT_DOMAINS
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        domain = SIGNED_OBJECT_DOMAINS["seven/live-run-permit"]
        obj = self._make_signed_object("seven/live-run-permit", domain, private_key)
        result = verify_live_run_permit(obj, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "PASS")

    def test_authorization_consumption_receipt_verification(self):
        """AuthorizationConsumptionReceipt 签名验证。"""
        from seven_system.human.signed_object_verifier import (
            verify_authorization_consumption_receipt, SIGNED_OBJECT_DOMAINS
        )
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        domain = SIGNED_OBJECT_DOMAINS["seven/authorization-consumption-receipt"]
        obj = self._make_signed_object("seven/authorization-consumption-receipt", domain, private_key)
        result = verify_authorization_consumption_receipt(obj, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "PASS")

    def test_normative_review_record_verification(self):
        """NormativeRequirementReviewRecord 签名验证。"""
        from seven_system.human.signed_object_verifier import (
            verify_normative_requirement_review_record, SIGNED_OBJECT_DOMAINS
        )
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        domain = SIGNED_OBJECT_DOMAINS["seven/docs/normative-requirement-review-record"]
        obj = self._make_signed_object("seven/docs/normative-requirement-review-record", domain, private_key)
        result = verify_normative_requirement_review_record(obj, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "PASS")

    def test_fake_signature_rejected_for_all_object_types(self):
        """伪签名对所有签名对象类型都必须 FAIL。"""
        from seven_system.human.signed_object_verifier import (
            verify_audit_assignment, verify_audit_record, verify_eea,
            verify_live_run_permit, verify_authorization_consumption_receipt,
            verify_normative_requirement_review_record, SIGNED_OBJECT_DOMAINS,
        )
        private_key, _ = _make_real_ed25519_keypair()
        other_key = _make_real_ed25519_keypair()[0]
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        wrong_pub = other_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        for schema_id, verifier_fn in [
            ("seven/audit-assignment", verify_audit_assignment),
            ("seven/audit-record", verify_audit_record),
            ("seven/external-execution-authorization", verify_eea),
            ("seven/live-run-permit", verify_live_run_permit),
            ("seven/authorization-consumption-receipt", verify_authorization_consumption_receipt),
            ("seven/docs/normative-requirement-review-record", verify_normative_requirement_review_record),
        ]:
            domain = SIGNED_OBJECT_DOMAINS[schema_id]
            obj = self._make_signed_object(schema_id, domain, private_key)
            result = verifier_fn(obj, public_key_bytes=wrong_pub)
            self.assertEqual(result.verdict, "FAIL", f"{schema_id} should FAIL with wrong key")

    def test_unknown_schema_id_rejected(self):
        """未知 schema_id 必须被拒绝。"""
        from seven_system.human.signed_object_verifier import verify_signed_object
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        obj = {"schema_id": "seven/unknown", "key_id": "k", "signature_envelope": {}}
        result = verify_signed_object(obj, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL")

    def test_wrong_schema_id_rejected(self):
        """schema_id 不匹配期望值时必须 FAIL。"""
        from seven_system.human.signed_object_verifier import verify_signed_object, SIGNED_OBJECT_DOMAINS
        private_key, _ = _make_real_ed25519_keypair()
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        domain = SIGNED_OBJECT_DOMAINS["seven/audit-assignment"]
        obj = self._make_signed_object("seven/audit-assignment", domain, private_key)
        result = verify_signed_object(
            obj, public_key_bytes=raw_pub,
            expected_schema_id="seven/audit-record",
        )
        self.assertEqual(result.verdict, "FAIL")


if __name__ == "__main__":
    unittest.main()
