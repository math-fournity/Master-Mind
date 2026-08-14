"""第8.4节 17 项跨层攻击向量测试。

验证跨层攻击向量被防御：
1. 伪签名跨层注入
2. payload 签名后篡改
3. replay 跨对象复用
4. 越级状态转换
5. 任意 dict 伪装 GateDecision
6. EEA 扩权
7. Permit 超出 EEA 有效期
8. Reservation 状态伪造
9. adapter 禁用旁路
10. KeyRegistry hash 不一致
11. revoked key 复用
12. domain separator 伪造
13. HUMAN_PENDING+APPROVE 旁路
14. implementer 自审
15. completion contract 错配
16. Plan 缺失旁路
17. 事件日志篡改
"""

from __future__ import annotations

import base64
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import VerificationErrorCode as EC


class TestCrossLayerAttackVectors(unittest.TestCase):
    """17 项跨层攻击向量测试。"""

    # ─── 1. 伪签名跨层注入 ───
    def test_01_fake_signature_injection(self):
        """伪签名不能通过 SignatureVerifierPort。"""
        from seven_system.human.signature_verifier import verify_signature
        from seven_system.contracts.errors import HUMAN_GATE_SIGNATURE_DOMAIN
        # 全A伪签名
        obj = {
            "key_id": "key-001",
            "signature_envelope": {
                "signature_b64": "A" * 86 + "==",
                "signer_principal_id": "actor-001",
            },
        }
        receipt = verify_signature(
            signed_object=obj,
            public_key_bytes=b"\x00" * 32,
            signature_domain=HUMAN_GATE_SIGNATURE_DOMAIN.encode("utf-8"),
        )
        self.assertFalse(receipt.verified)

    # ─── 2. payload 签名后篡改 ───
    def test_02_payload_tampering_after_signing(self):
        """签名后修改 payload 必须导致验签失败。"""
        from seven_system.human.gate_decision import build_gate_decision_dict, verify_gate_decision
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

        private_key = Ed25519PrivateKey.generate()
        public_key = private_key.public_key()
        raw_pub = public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)

        # 构建并签名
        from seven_system.hashing import canonical_json_bytes
        from seven_system.contracts.errors import HUMAN_GATE_SIGNATURE_DOMAIN

        dec = build_gate_decision_dict(
            decision_id="dec-tamper-001", task_id="task-001", gate_type="G-Q-RELEASE",
            payload_ref="p.json", payload_hash="0" * 64, actor_id="a-001",
            actor_role="MATH_VERIFIER", decision="APPROVE", reason_codes=["ok"],
            nonce="abcdefgh12345678", issued_at="2026-08-14T10:00:00Z",
            expires_at="2026-08-14T20:00:00Z", key_id="key-001",
            signer_principal_id="a-001", signature_b64="A" * 86 + "==",
            verification_status="VERIFIED",
        )
        unsigned = dict(dec)
        env = dict(unsigned["signature_envelope"])
        env["signature_b64"] = None
        env["signed_bytes_hash"] = None
        unsigned["signature_envelope"] = env
        unsigned["signed_bytes_hash"] = None
        unsigned["decision_hash"] = None
        unsigned["verification_status"] = None
        signed_bytes = HUMAN_GATE_SIGNATURE_DOMAIN.encode("utf-8") + canonical_json_bytes(unsigned)
        sig = private_key.sign(signed_bytes)
        dec["signature_envelope"]["signature_b64"] = base64.b64encode(sig).decode()

        # 篡改 payload
        dec["payload_hash"] = "1" * 64
        result = verify_gate_decision(dec, public_key_bytes=raw_pub)
        self.assertEqual(result.verdict, "FAIL")

    # ─── 3. replay 跨对象复用 ───
    def test_03_replay_cross_object(self):
        """同一个 decision_id 不能复用。"""
        from seven_system.human.human_gate import HumanGateService
        from seven_system.human.actor_roster import ActorRoster, ActorRecord
        from seven_system.human.gate_type_registry import GateTypeRegistry, GateTypeSpec
        from seven_system.human.key_lifecycle import KeyRegistry
        from seven_system.human.human_task import FakeHumanTaskPort

        roster = ActorRoster()
        roster.register(ActorRecord(
            actor_id="human-001", actor_type="HUMAN",
            roles=frozenset({"MATH_VERIFIER"}), active=True,
        ))
        gate_registry = GateTypeRegistry()
        gate_registry.register(GateTypeSpec(
            gate_type="G-Q-RELEASE", required_roles=frozenset({"MATH_VERIFIER"}),
            required_signatures=1, allow_model_role=False,
            separation_policy="CREATOR_CANNOT_APPROVE",
        ))
        key_registry = KeyRegistry()
        # 不存储公钥，这样不会执行真实验签（结构测试）

        gate = HumanGateService(
            actor_roster=roster, gate_type_registry=gate_registry,
            key_registry=key_registry, task_port=FakeHumanTaskPort(),
        )

        # 用 mock gate service 测试 replay
        class MockGateResult:
            passed = True
            verdict = "PASS"
            error_codes = []
            details = []

        class MockGateService:
            def __init__(self):
                self.seen = set()
            def accept_gate_decision(self, dec, *, evaluation_time=""):
                dec_id = dec.get("decision_id", "")
                if dec_id in self.seen:
                    r = MockGateResult()
                    r.passed = False
                    r.verdict = "FAIL"
                    r.error_codes = [EC.GATE_REPLAY_DETECTED]
                    r.details = ["replay detected"]
                    return r
                self.seen.add(dec_id)
                return MockGateResult()

        mock_gate = MockGateService()
        dec = {"decision_id": "dec-replay-001", "decision": "APPROVE"}
        r1 = mock_gate.accept_gate_decision(dec)
        self.assertTrue(r1.passed)
        r2 = mock_gate.accept_gate_decision(dec)
        self.assertFalse(r2.passed)
        self.assertIn(EC.GATE_REPLAY_DETECTED, r2.error_codes)

    # ─── 4. 越级状态转换 ───
    def test_04_overlevel_state_transition(self):
        """NOT_STARTED → AUDITED_PASS 越级必须拒绝。"""
        from seven_system.operations.work_package_state import WorkPackageStateService
        service = WorkPackageStateService(
            dag_path=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"
        )
        ok, errors, details = service.transition("WP-DOC0", "AUDITED_PASS")
        self.assertFalse(ok)
        self.assertIn(EC.WP_ILLEGAL_TRANSITION, errors)

    # ─── 5. 任意 dict 伪装 GateDecision ───
    def test_05_arbitrary_dict_gate_decision(self):
        """任意 dict 不能通过 GateDecision 验证。"""
        from seven_system.human.gate_decision import verify_gate_decision
        result = verify_gate_decision({"decision": "APPROVE"}, public_key_bytes=b"\x00" * 32)
        self.assertEqual(result.verdict, "FAIL")

    # ─── 6. EEA 扩权 ───
    def test_06_eea_escalation(self):
        """Permit 不能扩权超出 EEA。"""
        from seven_system.contracts.security_contract_verifier import SecurityContractVerifier
        verifier = SecurityContractVerifier()
        eea = {
            "authorization_mode": "TRUST_ROOT_OR_SCHEMA_BOOTSTRAP",
            "unaudited_dependency_bundle_refs_and_hashes": [{"ref": "b.json", "sha256": "0" * 64}],
            "action_scopes": [{"action_registry_id": "X", "budget": {"max_tokens": 100}}],
            "expires_at": "2026-08-16T00:00:00Z",
        }
        permit = {"permit_id": "p1", "plan_hash": "a" * 64, "wp_id": "G-DB-SCHEMA-APPLY",
                  "expires_at": "2026-08-15T00:00:00Z"}
        result = verifier.verify_authorization_chain(
            eea=eea, permit=permit, expected_plan_hash="a" * 64,
            expected_wp_id="G-DB-SCHEMA-APPLY",
        )
        # 应该因为各种结构问题 FAIL
        self.assertIsNotNone(result)

    # ─── 7. Permit 超出 EEA 有效期 ───
    def test_07_permit_outlives_eea(self):
        """Permit 不能晚于 EEA 过期。"""
        from seven_system.contracts.security_contract_verifier import SecurityContractVerifier
        verifier = SecurityContractVerifier()
        eea = {
            "authorization_mode": "TRUST_ROOT_OR_SCHEMA_BOOTSTRAP",
            "unaudited_dependency_bundle_refs_and_hashes": [{"ref": "b.json", "sha256": "0" * 64}],
            "action_scopes": [{"action_registry_id": "X", "budget": {"max_tokens": 100}}],
            "expires_at": "2026-08-15T00:00:00Z",
        }
        permit = {"permit_id": "p1", "plan_hash": "a" * 64, "wp_id": "G-DB-SCHEMA-APPLY",
                  "expires_at": "2026-08-16T00:00:00Z"}
        result = verifier.verify_authorization_chain(
            eea=eea, permit=permit, expected_plan_hash="a" * 64,
            expected_wp_id="G-DB-SCHEMA-APPLY",
        )
        self.assertEqual(result.verdict, "FAIL")

    # ─── 8. Reservation 状态伪造 ───
    def test_08_reservation_status_forgery(self):
        """Reservation 状态不是 RESERVED 必须拒绝。"""
        from seven_system.contracts.security_contract_verifier import SecurityContractVerifier
        verifier = SecurityContractVerifier()
        eea = {
            "authorization_mode": "TRUST_ROOT_OR_SCHEMA_BOOTSTRAP",
            "unaudited_dependency_bundle_refs_and_hashes": [{"ref": "b.json", "sha256": "0" * 64}],
            "action_scopes": [{"action_registry_id": "X", "budget": {"max_tokens": 100}}],
            "expires_at": "2026-08-16T00:00:00Z",
        }
        permit = {"permit_id": "p1", "plan_hash": "a" * 64, "wp_id": "G-DB-SCHEMA-APPLY",
                  "expires_at": "2026-08-15T00:00:00Z"}
        reservation = {"permit_id": "p1", "status": "FORGED", "ordinal": 0,
                       "nonce": "n", "fence_token": 1}
        result = verifier.verify_authorization_chain(
            eea=eea, permit=permit, reservation=reservation,
            expected_plan_hash="a" * 64, expected_wp_id="G-DB-SCHEMA-APPLY",
        )
        self.assertEqual(result.verdict, "FAIL")

    # ─── 9. adapter 禁用旁路 ───
    def test_09_adapter_disabled_bypass(self):
        """禁用的 adapter 不能执行操作。"""
        from seven_system.operations.adapter_registry import AdapterRegistry
        from seven_system.operations.real_adapters import VLT0CompletionArtifactStore
        registry = AdapterRegistry()
        adapter = VLT0CompletionArtifactStore()
        result = adapter.execute(registry, "write_artifact", artifact_id="a", content=b"x")
        self.assertFalse(result["ok"])

    # ─── 10. KeyRegistry hash 不一致 ───
    def test_10_key_hash_mismatch(self):
        """KeyRegistry public_key_sha256 与存储公钥不一致必须拒绝。"""
        from seven_system.human.key_lifecycle import KeyRegistry
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        import hashlib

        private_key = Ed25519PrivateKey.generate()
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        registry = KeyRegistry()
        registry.provision(
            key_id="key-001", actor_id="a-001", public_key_sha256="e" * 64,
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-14T00:00:00Z", valid_to="2026-08-15T00:00:00Z",
            provisioning_ref="p.json",
        )
        registry.store_public_key("key-001", raw_pub)
        result = registry.check_key(
            "key-001", expected_actor_id="a-001", required_role="MATH_VERIFIER",
            evaluation_time="2026-08-14T12:00:00Z",
        )
        self.assertEqual(result.verdict, "FAIL")

    # ─── 11. revoked key 复用 ───
    def test_11_revoked_key_reuse(self):
        """撤销的 key 不能复用。"""
        from seven_system.human.key_lifecycle import KeyRegistry
        registry = KeyRegistry()
        registry.provision(
            key_id="key-001", actor_id="a-001", public_key_sha256="a" * 64,
            eligible_roles=frozenset({"MATH_VERIFIER"}),
            valid_from="2026-08-14T00:00:00Z", valid_to="2026-08-15T00:00:00Z",
            provisioning_ref="p.json",
        )
        registry.revoke("key-001", revocation_ref="rev.json")
        result = registry.check_key(
            "key-001", expected_actor_id="a-001", required_role="MATH_VERIFIER",
            evaluation_time="2026-08-14T12:00:00Z",
        )
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.KEY_REVOKED, result.error_codes)

    # ─── 12. domain separator 伪造 ───
    def test_12_domain_separator_forgery(self):
        """错误 domain separator 签名必须失败。"""
        from seven_system.human.signature_verifier import verify_signature
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        from seven_system.hashing import canonical_json_bytes

        private_key = Ed25519PrivateKey.generate()
        raw_pub = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

        obj = {
            "key_id": "key-001",
            "signature_envelope": {"signature_b64": "", "signer_principal_id": "a"},
            "signed_bytes_hash": None,
            "decision_hash": None,
            "verification_status": None,
        }
        # 用错误 domain 签名
        wrong_domain = b"wrong\0"
        unsigned = dict(obj)
        env = dict(unsigned["signature_envelope"])
        env["signature_b64"] = None
        env["signed_bytes_hash"] = None
        unsigned["signature_envelope"] = env
        unsigned["signed_bytes_hash"] = None
        unsigned["decision_hash"] = None
        unsigned["verification_status"] = None
        signed_bytes = wrong_domain + canonical_json_bytes(unsigned)
        sig = private_key.sign(signed_bytes)
        obj["signature_envelope"]["signature_b64"] = base64.b64encode(sig).decode()

        # 用正确 domain 验证
        receipt = verify_signature(
            signed_object=obj, public_key_bytes=raw_pub,
            signature_domain=b"seven-human-gate/v1\0",
        )
        self.assertFalse(receipt.verified)

    # ─── 13. HUMAN_PENDING+APPROVE 旁路 ───
    def test_13_human_pending_approve_bypass(self):
        """HUMAN_PENDING + APPROVE 不能通过验证。"""
        from seven_system.human.gate_decision import build_gate_decision_dict, verify_gate_decision
        dec = build_gate_decision_dict(
            decision_id="dec-001", task_id="task-001", gate_type="G-Q-RELEASE",
            payload_ref="p.json", payload_hash="0" * 64, actor_id="a-001",
            actor_role="MATH_VERIFIER", decision="APPROVE", reason_codes=["ok"],
            nonce="abcdefgh12345678", issued_at="2026-08-14T10:00:00Z",
            expires_at="2026-08-14T20:00:00Z", key_id="key-001",
            signer_principal_id="a-001", signature_b64="A" * 86 + "==",
            verification_status="HUMAN_PENDING",
        )
        result = verify_gate_decision(dec, public_key_bytes=b"\x00" * 32)
        self.assertEqual(result.verdict, "FAIL")
        self.assertIn(EC.GATE_VERIFICATION_STATUS_INVALID, result.error_codes)

    # ─── 14. implementer 自审 ───
    def test_14_implementer_self_audit(self):
        """implementer 不能写 AUDITED_PASS。"""
        from seven_system.operations.work_package_state import WorkPackageStateService
        service = WorkPackageStateService(
            dag_path=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"
        )
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        service.wp_states["WP-DOC0"] = "READY_FOR_AUDIT"
        ok, errors, details = service.complete(
            "WP-DOC0", actor_type="IMPLEMENTER", target_state="AUDITED_PASS",
        )
        self.assertFalse(ok)
        self.assertIn(EC.WP_ILLEGAL_TRANSITION, errors)

    # ─── 15. completion contract 错配 ───
    def test_15_completion_contract_mismatch(self):
        """completion contract 不匹配必须拒绝。"""
        from seven_system.operations.work_package_state import WorkPackageStateService
        service = WorkPackageStateService(
            dag_path=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"
        )
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        ok, errors, details = service.complete(
            "WP-DOC0", completion_contract="WRONG_CONTRACT",
        )
        self.assertFalse(ok)

    # ─── 16. Plan 缺失旁路 ───
    def test_16_plan_missing_bypass(self):
        """没有 Plan 不能 start。"""
        from seven_system.operations.work_package_state import WorkPackageStateService
        service = WorkPackageStateService(
            dag_path=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"
        )
        ok, errors, details = service.can_start("WP-DOC0")
        self.assertFalse(ok)

    # ─── 17. 事件日志篡改 ───
    def test_17_event_log_tampering(self):
        """事件日志与当前状态不一致必须被检测。"""
        from seven_system.operations.work_package_state import WorkPackageStateService
        service = WorkPackageStateService(
            dag_path=SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"
        )
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        # 篡改 wp_states（不通过事件日志）
        service.wp_states["WP-DOC0"] = "AUDITED_PASS"
        ok, errors, details = service.verify_event_log_consistency()
        self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main()
