"""WP-HG0 HumanGate 测试。

测试层级：Golden → Negative → Fault injection
覆盖：
- ActorRoster 注册/检查/停用
- GateTypeRegistry 注册/查询
- KeyRegistry 生命周期（注册→撤销→过期→使用后撤销）
- HumanTask 创建/分配/完成
- GateDecision 结构验证（签名、hash、domain）
- HumanGateService 完整门控链编排
- ModelRole 不能自我批准（职责分离）
- replay 防护（相同 nonce/payload/actor）
- payload 改写检测
- 职责冲突（同一 actor 创建+批准）
- 消费 GV0 CompletionContractVerifier（不复制）

所有 blocker test 失败 → 工作包 FAIL。
"""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import VerificationErrorCode as EC
from seven_system.hashing import canonical_json_bytes
from seven_system.human.actor_roster import ActorRoster, ActorRecord
from seven_system.human.gate_type_registry import GateTypeRegistry, GateTypeSpec
from seven_system.human.key_lifecycle import KeyRegistry
from seven_system.human.gate_decision import (
    build_gate_decision_dict,
    verify_gate_decision,
)
from seven_system.human.human_task import FakeHumanTaskPort
from seven_system.human.human_gate import HumanGateService


# ─── helpers ───────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64
_SIG_B64 = "A" * 86 + "=="

DAG_PATH = SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"


def _dag_sha256() -> str:
    raw = DAG_PATH.read_bytes()
    canonical = json.dumps(
        json.loads(raw), ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _make_implementation_bundle(wp_id: str = "WP-HG0") -> dict:
    return {
        "schema_id": "seven/implementation-completion-bundle",
        "schema_version": 1,
        "bundle_id": f"test-bundle-{wp_id}-001",
        "wp_id": wp_id,
        "implementation_attempt_id": "attempt-001",
        "status": "READY_FOR_AUDIT",
    }


def _make_roster() -> ActorRoster:
    """构建测试用 ActorRoster：一个人类审查者 + 一个 ModelRole。"""
    roster = ActorRoster()
    roster.register(ActorRecord(
        actor_id="human-reviewer-001",
        actor_type="HUMAN",
        roles=frozenset({"MATH_VERIFIER", "PROOF_JUDGE"}),
        active=True,
    ))
    roster.register(ActorRecord(
        actor_id="human-architect-001",
        actor_type="HUMAN",
        roles=frozenset({"QUESTION_ARCHITECT"}),
        active=True,
    ))
    roster.register(ActorRecord(
        actor_id="model-role-001",
        actor_type="MODEL_ROLE",
        roles=frozenset({"MATH_VERIFIER"}),
        active=True,
    ))
    return roster


def _make_gate_type_registry() -> GateTypeRegistry:
    """构建测试用 GateTypeRegistry。"""
    registry = GateTypeRegistry()
    registry.register(GateTypeSpec(
        gate_type="PROOF_REVIEW",
        required_roles=frozenset({"PROOF_JUDGE"}),
        required_signatures=1,
        allow_model_role=False,
        separation_policy="CREATOR_CANNOT_APPROVE",
    ))
    registry.register(GateTypeSpec(
        gate_type="QUESTION_RELEASE_APPROVAL",
        required_roles=frozenset({"QUESTION_ARCHITECT"}),
        required_signatures=1,
        allow_model_role=False,
        separation_policy="CREATOR_CANNOT_APPROVE",
    ))
    registry.register(GateTypeSpec(
        gate_type="INTERNAL_CHECK",
        required_roles=frozenset({"MATH_VERIFIER"}),
        required_signatures=1,
        allow_model_role=True,
        separation_policy="NONE",
    ))
    return registry


def _make_key_registry() -> KeyRegistry:
    """构建测试用 KeyRegistry：一个活跃的人类签名密钥。"""
    registry = KeyRegistry()
    registry.provision(
        key_id="key-human-001",
        actor_id="human-reviewer-001",
        public_key_sha256=_ZERO_HASH,
        eligible_roles=frozenset({"MATH_VERIFIER", "PROOF_JUDGE"}),
        valid_from="2026-08-14T00:00:00Z",
        valid_to="2026-08-20T00:00:00Z",
        provisioning_ref="prov-ceremony-001",
    )
    registry.provision(
        key_id="key-architect-001",
        actor_id="human-architect-001",
        public_key_sha256=_ZERO_HASH,
        eligible_roles=frozenset({"QUESTION_ARCHITECT"}),
        valid_from="2026-08-14T00:00:00Z",
        valid_to="2026-08-20T00:00:00Z",
        provisioning_ref="prov-ceremony-001",
    )
    return registry


def _make_gate_service() -> HumanGateService:
    """构建完整的 HumanGateService 实例。"""
    return HumanGateService(
        actor_roster=_make_roster(),
        gate_type_registry=_make_gate_type_registry(),
        key_registry=_make_key_registry(),
        task_port=FakeHumanTaskPort(),
    )


def _make_valid_decision(
    *,
    decision_id: str = "dec-001",
    task_id: str = "task-001",
    gate_type: str = "PROOF_REVIEW",
    actor_id: str = "human-reviewer-001",
    actor_role: str = "PROOF_JUDGE",
    decision: str = "APPROVE",
    reason_codes: list[str] | None = None,
    nonce: str = "nonce-aaaaaaaaaaaaaaaa",
    key_id: str = "key-human-001",
    payload_hash: str | None = None,
    issued_at: str = "2026-08-14T12:00:00Z",
    expires_at: str = "2026-08-15T12:00:00Z",
    verification_status: str = "HUMAN_PENDING",
) -> dict:
    """构建一个结构合法的 GateDecision dict。"""
    ph = payload_hash or _ZERO_HASH
    return build_gate_decision_dict(
        decision_id=decision_id,
        task_id=task_id,
        gate_type=gate_type,
        payload_ref="payload-ref-001",
        payload_hash=ph,
        actor_id=actor_id,
        actor_role=actor_role,
        decision=decision,
        reason_codes=reason_codes or ["REVIEW_PASS"],
        nonce=nonce,
        issued_at=issued_at,
        expires_at=expires_at,
        key_id=key_id,
        signer_principal_id=actor_id,
        signature_b64=_SIG_B64,
        separation_evidence_refs=["sep-evidence-001"],
        verification_status=verification_status,
    )


def _create_task_for_decision(
    service: HumanGateService,
    decision: dict,
    *,
    creator_actor_id: str = "human-architect-001",
) -> None:
    """在 task_port 中创建与 decision 匹配的 task。"""
    service.task_port.create_task(
        task_id=decision["task_id"],
        gate_type=decision["gate_type"],
        payload_ref="payload-ref-001",
        payload_hash=decision["payload_hash"],
        allowed_view="PROOF_VIEW",
        deadline="2026-08-16T00:00:00Z",
        eligible_roles=frozenset({"PROOF_JUDGE"}),
        separation_policy="CREATOR_CANNOT_APPROVE",
        required_signatures=1,
        nonce="task-nonce-aaaaaaaaaaaa",
        creator_actor_id=creator_actor_id,
    )


# ═══════════════════════════════════════════════════════════════════════
# ActorRoster 测试
# ═══════════════════════════════════════════════════════════════════════


class TestActorRoster(unittest.TestCase):
    """ActorRoster 注册/检查/停用测试。"""

    def test_register_valid_actor(self):
        """Golden: 注册合法 actor。"""
        roster = ActorRoster()
        record = ActorRecord(
            actor_id="human-001",
            actor_type="HUMAN",
            roles=frozenset({"MATH_VERIFIER"}),
            active=True,
        )
        result = roster.register(record)
        self.assertTrue(result.passed)
        self.assertEqual(roster.size, 1)

    def test_register_duplicate_actor_rejected(self):
        """Negative: 重复注册同一 actor 被拒绝。"""
        roster = ActorRoster()
        record = ActorRecord(
            actor_id="human-001",
            actor_type="HUMAN",
            roles=frozenset({"MATH_VERIFIER"}),
            active=True,
        )
        roster.register(record)
        result = roster.register(record)
        self.assertFalse(result.passed)
        self.assertIn(EC.ACTOR_NOT_IN_ROSTER, result.error_codes)

    def test_register_invalid_actor_type(self):
        """Negative: 非法 actor_type 被拒绝。"""
        roster = ActorRoster()
        record = ActorRecord(
            actor_id="human-001",
            actor_type="ALIEN",
            roles=frozenset({"MATH_VERIFIER"}),
            active=True,
        )
        result = roster.register(record)
        self.assertFalse(result.passed)
        self.assertIn(EC.ACTOR_TYPE_INVALID, result.error_codes)

    def test_register_invalid_role(self):
        """Negative: 非法角色被拒绝。"""
        roster = ActorRoster()
        record = ActorRecord(
            actor_id="human-001",
            actor_type="HUMAN",
            roles=frozenset({"SUPER_ADMIN"}),
            active=True,
        )
        result = roster.register(record)
        self.assertFalse(result.passed)
        self.assertIn(EC.ACTOR_ROLE_MISSING, result.error_codes)

    def test_check_actor_missing_role(self):
        """Negative: actor 缺少要求的角色。"""
        roster = ActorRoster()
        roster.register(ActorRecord(
            actor_id="human-001",
            actor_type="HUMAN",
            roles=frozenset({"MATH_VERIFIER"}),
            active=True,
        ))
        result = roster.check_actor("human-001", required_roles=frozenset({"PROOF_JUDGE"}))
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_REQUIRED_ROLE_MISSING, result.error_codes)

    def test_check_inactive_actor(self):
        """Negative: 停用的 actor 不能通过检查。"""
        roster = ActorRoster()
        roster.register(ActorRecord(
            actor_id="human-001",
            actor_type="HUMAN",
            roles=frozenset({"MATH_VERIFIER"}),
            active=True,
        ))
        roster.deactivate("human-001")
        result = roster.check_actor("human-001")
        self.assertFalse(result.passed)
        self.assertIn(EC.ACTOR_INACTIVE, result.error_codes)

    def test_check_unknown_actor(self):
        """Negative: 不存在的 actor。"""
        roster = ActorRoster()
        result = roster.check_actor("nobody-001")
        self.assertFalse(result.passed)
        self.assertIn(EC.ACTOR_NOT_IN_ROSTER, result.error_codes)

    def test_is_model_role(self):
        """Golden: ModelRole 类型检测。"""
        roster = ActorRoster()
        roster.register(ActorRecord(
            actor_id="model-001",
            actor_type="MODEL_ROLE",
            roles=frozenset({"MATH_VERIFIER"}),
            active=True,
        ))
        roster.register(ActorRecord(
            actor_id="human-001",
            actor_type="HUMAN",
            roles=frozenset({"MATH_VERIFIER"}),
            active=True,
        ))
        self.assertTrue(roster.is_model_role("model-001"))
        self.assertFalse(roster.is_model_role("human-001"))


# ═══════════════════════════════════════════════════════════════════════
# GateTypeRegistry 测试
# ═══════════════════════════════════════════════════════════════════════


class TestGateTypeRegistry(unittest.TestCase):

    def test_register_valid_gate_type(self):
        """Golden: 注册合法 gate type。"""
        registry = GateTypeRegistry()
        spec = GateTypeSpec(
            gate_type="PROOF_REVIEW",
            required_roles=frozenset({"PROOF_JUDGE"}),
            required_signatures=1,
            allow_model_role=False,
            separation_policy="CREATOR_CANNOT_APPROVE",
        )
        result = registry.register(spec)
        self.assertTrue(result.passed)

    def test_register_zero_signatures_rejected(self):
        """Negative: required_signatures=0 被拒绝。"""
        registry = GateTypeRegistry()
        spec = GateTypeSpec(
            gate_type="BAD_GATE",
            required_roles=frozenset({"PROOF_JUDGE"}),
            required_signatures=0,
            allow_model_role=False,
            separation_policy="NONE",
        )
        result = registry.register(spec)
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_REQUIRED_SIGNATURES_NOT_MET, result.error_codes)

    def test_register_invalid_separation_policy(self):
        """Negative: 非法分离策略被拒绝。"""
        registry = GateTypeRegistry()
        spec = GateTypeSpec(
            gate_type="BAD_GATE",
            required_roles=frozenset({"PROOF_JUDGE"}),
            required_signatures=1,
            allow_model_role=False,
            separation_policy="WHATEVER",
        )
        result = registry.register(spec)
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_DUTY_CONFLICT, result.error_codes)

    def test_check_unknown_gate_type(self):
        """Negative: 未知 gate type。"""
        registry = GateTypeRegistry()
        result = registry.check_gate_type("NONEXISTENT")
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_TYPE_UNKNOWN, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# KeyRegistry / Key lifecycle 测试
# ═══════════════════════════════════════════════════════════════════════


class TestKeyLifecycle(unittest.TestCase):

    def test_provision_valid_key(self):
        """Golden: 注册合法签名密钥。"""
        registry = KeyRegistry()
        result = registry.provision(
            key_id="key-001",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-20T00:00:00Z",
            provisioning_ref="prov-001",
        )
        self.assertTrue(result.passed)

    def test_provision_no_self_authorization(self):
        """Negative: 缺少 provisioning_ref（自我授权）被拒绝。"""
        registry = KeyRegistry()
        result = registry.provision(
            key_id="key-001",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-20T00:00:00Z",
            provisioning_ref="",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_provision_invalid_time_window(self):
        """Negative: valid_from >= valid_to 被拒绝。"""
        registry = KeyRegistry()
        result = registry.provision(
            key_id="key-001",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-20T00:00:00Z",
            valid_to="2026-08-14T00:00:00Z",
            provisioning_ref="prov-001",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.TIME_WINDOW_INVALID, result.error_codes)

    def test_revoke_then_use_after_revoke(self):
        """Fault: 注册→撤销→使用被拒绝。"""
        registry = KeyRegistry()
        registry.provision(
            key_id="key-001",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-20T00:00:00Z",
            provisioning_ref="prov-001",
        )
        # 撤销前 key 有效
        result_before = registry.check_key(
            "key-001", evaluation_time="2026-08-15T00:00:00Z"
        )
        self.assertTrue(result_before.passed)

        # 撤销
        revoke_result = registry.revoke("key-001", revocation_ref="rev-001")
        self.assertTrue(revoke_result.passed)

        # 撤销后使用被拒绝
        result_after = registry.check_key(
            "key-001", evaluation_time="2026-08-15T00:00:00Z"
        )
        self.assertFalse(result_after.passed)
        self.assertIn(EC.KEY_REVOKED, result_after.error_codes)

    def test_key_expired(self):
        """Negative: 过期密钥被拒绝。"""
        registry = KeyRegistry()
        registry.provision(
            key_id="key-001",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-15T00:00:00Z",
            provisioning_ref="prov-001",
        )
        result = registry.check_key(
            "key-001", evaluation_time="2026-08-16T00:00:00Z"
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.KEY_EXPIRED, result.error_codes)

    def test_key_not_yet_valid(self):
        """Negative: 未生效密钥被拒绝。"""
        registry = KeyRegistry()
        registry.provision(
            key_id="key-001",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-16T00:00:00Z",
            valid_to="2026-08-20T00:00:00Z",
            provisioning_ref="prov-001",
        )
        result = registry.check_key(
            "key-001", evaluation_time="2026-08-15T00:00:00Z"
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.KEY_NOT_YET_VALID, result.error_codes)

    def test_key_actor_mismatch(self):
        """Negative: key 绑定的 actor 不匹配。"""
        registry = KeyRegistry()
        registry.provision(
            key_id="key-001",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-20T00:00:00Z",
            provisioning_ref="prov-001",
        )
        result = registry.check_key(
            "key-001",
            expected_actor_id="human-002",
            evaluation_time="2026-08-15T00:00:00Z",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.KEY_ACTOR_MISMATCH, result.error_codes)

    def test_key_role_not_eligible(self):
        """Negative: key 不具备要求的角色资格。"""
        registry = KeyRegistry()
        registry.provision(
            key_id="key-001",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-20T00:00:00Z",
            provisioning_ref="prov-001",
        )
        result = registry.check_key(
            "key-001",
            required_role="MATH_VERIFIER",
            evaluation_time="2026-08-15T00:00:00Z",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.KEY_ROLE_NOT_ELIGIBLE, result.error_codes)

    def test_key_rotation_with_predecessor(self):
        """Golden: 密钥轮换引用前驱。"""
        registry = KeyRegistry()
        registry.provision(
            key_id="key-old",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-14T00:00:00Z",
            valid_to="2026-08-20T00:00:00Z",
            provisioning_ref="prov-001",
        )
        result = registry.provision(
            key_id="key-new",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-18T00:00:00Z",
            valid_to="2026-08-25T00:00:00Z",
            provisioning_ref="prov-002",
            rotation_predecessor="key-old",
        )
        self.assertTrue(result.passed)

    def test_key_rotation_unknown_predecessor(self):
        """Negative: 轮换引用未知前驱被拒绝。"""
        registry = KeyRegistry()
        result = registry.provision(
            key_id="key-new",
            actor_id="human-001",
            public_key_sha256=_ZERO_HASH,
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            valid_from="2026-08-18T00:00:00Z",
            valid_to="2026-08-25T00:00:00Z",
            provisioning_ref="prov-002",
            rotation_predecessor="key-nonexistent",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.KEY_NOT_REGISTERED, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# HumanTask 测试
# ═══════════════════════════════════════════════════════════════════════


class TestHumanTask(unittest.TestCase):

    def test_create_valid_task(self):
        """Golden: 创建合法 HumanTask。"""
        port = FakeHumanTaskPort()
        result = port.create_task(
            task_id="task-001",
            gate_type="PROOF_REVIEW",
            payload_ref="payload-001",
            payload_hash=_ZERO_HASH,
            allowed_view="PROOF_VIEW",
            deadline="2026-08-16T00:00:00Z",
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            separation_policy="CREATOR_CANNOT_APPROVE",
            required_signatures=1,
            nonce="nonce-aaaaaaaaaaaaaaaa",
            creator_actor_id="human-architect-001",
        )
        self.assertTrue(result.passed)
        self.assertEqual(port.size, 1)

    def test_create_duplicate_task(self):
        """Negative: 重复创建 task 被拒绝。"""
        port = FakeHumanTaskPort()
        port.create_task(
            task_id="task-001",
            gate_type="PROOF_REVIEW",
            payload_ref="payload-001",
            payload_hash=_ZERO_HASH,
            allowed_view="PROOF_VIEW",
            deadline="2026-08-16T00:00:00Z",
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            separation_policy="CREATOR_CANNOT_APPROVE",
            required_signatures=1,
            nonce="nonce-aaaaaaaaaaaaaaaa",
            creator_actor_id="human-architect-001",
        )
        result = port.create_task(
            task_id="task-001",
            gate_type="PROOF_REVIEW",
            payload_ref="payload-001",
            payload_hash=_ZERO_HASH,
            allowed_view="PROOF_VIEW",
            deadline="2026-08-16T00:00:00Z",
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            separation_policy="CREATOR_CANNOT_APPROVE",
            required_signatures=1,
            nonce="nonce-bbbbbbbbbbbbbbbb",
            creator_actor_id="human-architect-001",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_REPLAY_DETECTED, result.error_codes)

    def test_assign_task(self):
        """Golden: 分配任务给 actor。"""
        port = FakeHumanTaskPort()
        port.create_task(
            task_id="task-001",
            gate_type="PROOF_REVIEW",
            payload_ref="payload-001",
            payload_hash=_ZERO_HASH,
            allowed_view="PROOF_VIEW",
            deadline="2026-08-16T00:00:00Z",
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            separation_policy="CREATOR_CANNOT_APPROVE",
            required_signatures=1,
            nonce="nonce-aaaaaaaaaaaaaaaa",
            creator_actor_id="human-architect-001",
        )
        result = port.assign_task("task-001", "human-reviewer-001")
        self.assertTrue(result.passed)
        task = port.get_task("task-001")
        self.assertEqual(task.status, "ASSIGNED")
        self.assertEqual(task.assigned_actor_id, "human-reviewer-001")

    def test_assign_completed_task_rejected(self):
        """Negative: 分配已完成任务被拒绝。"""
        port = FakeHumanTaskPort()
        port.create_task(
            task_id="task-001",
            gate_type="PROOF_REVIEW",
            payload_ref="payload-001",
            payload_hash=_ZERO_HASH,
            allowed_view="PROOF_VIEW",
            deadline="2026-08-16T00:00:00Z",
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            separation_policy="CREATOR_CANNOT_APPROVE",
            required_signatures=1,
            nonce="nonce-aaaaaaaaaaaaaaaa",
            creator_actor_id="human-architect-001",
        )
        decision = _make_valid_decision()
        port.complete_task("task-001", decision)
        result = port.assign_task("task-001", "human-reviewer-001")
        self.assertFalse(result.passed)
        self.assertIn(EC.STATE_COMMAND_REJECTED, result.error_codes)

    def test_complete_task_payload_mismatch(self):
        """Negative: complete_task 时 payload_hash 不匹配。"""
        port = FakeHumanTaskPort()
        port.create_task(
            task_id="task-001",
            gate_type="PROOF_REVIEW",
            payload_ref="payload-001",
            payload_hash=_ZERO_HASH,
            allowed_view="PROOF_VIEW",
            deadline="2026-08-16T00:00:00Z",
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            separation_policy="CREATOR_CANNOT_APPROVE",
            required_signatures=1,
            nonce="nonce-aaaaaaaaaaaaaaaa",
            creator_actor_id="human-architect-001",
        )
        decision = _make_valid_decision(payload_hash="1" * 64)
        result = port.complete_task("task-001", decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_PAYLOAD_HASH_MISMATCH, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# GateDecision 结构验证测试
# ═══════════════════════════════════════════════════════════════════════


class TestGateDecisionStructure(unittest.TestCase):

    def test_valid_decision_passes(self):
        """Golden: 合法 GateDecision 通过结构验证。"""
        decision = _make_valid_decision()
        result = verify_gate_decision(decision)
        self.assertTrue(result.passed, msg=str(result.details))

    def test_unsigned_decision_rejected(self):
        """Negative: 未签名（空 signature_b64）的 decision 被拒绝。"""
        decision = _make_valid_decision()
        decision["signature_envelope"]["signature_b64"] = ""
        # 需要重算 hash 因为修改了内容
        from seven_system.human.gate_decision import (
            _compute_signed_bytes_hash, _compute_decision_hash,
        )
        decision["signed_bytes_hash"] = _compute_signed_bytes_hash(decision)
        decision["signature_envelope"]["signed_bytes_hash"] = decision["signed_bytes_hash"]
        decision["decision_hash"] = _compute_decision_hash(decision)
        result = verify_gate_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.SIGNATURE_INVALID, result.error_codes)

    def test_wrong_signature_domain(self):
        """Negative: 错误的 signature_domain 被拒绝。"""
        decision = _make_valid_decision()
        decision["signature_domain"] = "wrong-domain\0"
        from seven_system.human.gate_decision import (
            _compute_signed_bytes_hash, _compute_decision_hash,
        )
        decision["signed_bytes_hash"] = _compute_signed_bytes_hash(decision)
        decision["signature_envelope"]["signed_bytes_hash"] = decision["signed_bytes_hash"]
        decision["decision_hash"] = _compute_decision_hash(decision)
        result = verify_gate_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.SIGNATURE_DOMAIN_INVALID, result.error_codes)

    def test_payload_hash_mismatch_with_expected(self):
        """Negative: payload_hash 与期望值不匹配。"""
        decision = _make_valid_decision(payload_hash=_ZERO_HASH)
        result = verify_gate_decision(decision, expected_payload_hash="1" * 64)
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_PAYLOAD_HASH_MISMATCH, result.error_codes)

    def test_decision_hash_tampering(self):
        """Negative: decision_hash 被篡改后不匹配。"""
        decision = _make_valid_decision()
        decision["decision_hash"] = "0" * 64
        result = verify_gate_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_DECISION_HASH_MISMATCH, result.error_codes)

    def test_signed_bytes_hash_tampering(self):
        """Negative: signed_bytes_hash 被篡改后不匹配。"""
        decision = _make_valid_decision()
        decision["signed_bytes_hash"] = "0" * 64
        result = verify_gate_decision(decision)
        self.assertFalse(result.passed)
        # signed_bytes_hash 重算不匹配 → GATE_DECISION_HASH_MISMATCH
        self.assertIn(EC.GATE_DECISION_HASH_MISMATCH, result.error_codes)

    def test_invalid_nonce(self):
        """Negative: 非法 nonce 格式。"""
        decision = _make_valid_decision()
        decision["nonce"] = "short"
        from seven_system.human.gate_decision import (
            _compute_signed_bytes_hash, _compute_decision_hash,
        )
        decision["signed_bytes_hash"] = _compute_signed_bytes_hash(decision)
        decision["signature_envelope"]["signed_bytes_hash"] = decision["signed_bytes_hash"]
        decision["decision_hash"] = _compute_decision_hash(decision)
        result = verify_gate_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_NONCE_INVALID, result.error_codes)

    def test_invalid_decision_value(self):
        """Negative: 非法 decision 值。"""
        decision = _make_valid_decision()
        decision["decision"] = "MAYBE"
        from seven_system.human.gate_decision import (
            _compute_signed_bytes_hash, _compute_decision_hash,
        )
        decision["signed_bytes_hash"] = _compute_signed_bytes_hash(decision)
        decision["signature_envelope"]["signed_bytes_hash"] = decision["signed_bytes_hash"]
        decision["decision_hash"] = _compute_decision_hash(decision)
        result = verify_gate_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.STATE_COMMAND_REJECTED, result.error_codes)

    def test_invalid_algorithm(self):
        """Negative: 非 Ed25519 算法被拒绝。"""
        decision = _make_valid_decision()
        decision["signature_algorithm"] = "RSA"
        from seven_system.human.gate_decision import (
            _compute_signed_bytes_hash, _compute_decision_hash,
        )
        decision["signed_bytes_hash"] = _compute_signed_bytes_hash(decision)
        decision["signature_envelope"]["signed_bytes_hash"] = decision["signed_bytes_hash"]
        decision["signature_envelope"]["algorithm"] = "RSA"
        decision["decision_hash"] = _compute_decision_hash(decision)
        result = verify_gate_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.SIGNATURE_ALGORITHM_INVALID, result.error_codes)

    def test_invalid_time_window(self):
        """Negative: issued_at >= expires_at 被拒绝。"""
        decision = _make_valid_decision(
            issued_at="2026-08-15T12:00:00Z",
            expires_at="2026-08-15T12:00:00Z",
        )
        from seven_system.human.gate_decision import (
            _compute_signed_bytes_hash, _compute_decision_hash,
        )
        decision["signed_bytes_hash"] = _compute_signed_bytes_hash(decision)
        decision["signature_envelope"]["signed_bytes_hash"] = decision["signed_bytes_hash"]
        decision["decision_hash"] = _compute_decision_hash(decision)
        result = verify_gate_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.TIME_WINDOW_INVALID, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# HumanGateService 完整门控链测试
# ═══════════════════════════════════════════════════════════════════════


class TestHumanGateServiceGolden(unittest.TestCase):
    """Golden: 完整门控链——合法签名、合法 actor、合法 key。"""

    def test_accept_valid_gate_decision(self):
        """Golden: 接受合法的签名 GateDecision。"""
        service = _make_gate_service()
        decision = _make_valid_decision()
        _create_task_for_decision(service, decision)

        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertEqual(service.accepted_count, 1)

    def test_accept_reject_decision(self):
        """Golden: 接受 REJECT 决定（也是合法的）。"""
        service = _make_gate_service()
        decision = _make_valid_decision(decision="REJECT", reason_codes=["REVIEW_FAIL"])
        _create_task_for_decision(service, decision)

        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertTrue(result.passed, msg=str(result.details))


class TestHumanGateServiceNegative(unittest.TestCase):
    """Negative: 各种违规场景。"""

    def test_model_role_self_approval_rejected(self):
        """Negative: ModelRole 不能自我批准。"""
        service = _make_gate_service()
        # ModelRole actor 用 INTERNAL_CHECK gate（allow_model_role=True）
        # 但 APPROVE 仍然被拒绝
        decision = _make_valid_decision(
            actor_id="model-role-001",
            actor_role="MATH_VERIFIER",
            gate_type="INTERNAL_CHECK",
            decision="APPROVE",
            key_id="key-human-001",  # key 绑定到 human-reviewer-001
        )
        # key 不匹配会导致 KEY_ACTOR_MISMATCH，但 self-approval 也会触发
        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result.passed)
        # ModelRole APPROVE → GATE_SELF_APPROVAL_REJECTED
        self.assertIn(EC.GATE_SELF_APPROVAL_REJECTED, result.error_codes)

    def test_model_role_on_no_model_gate_rejected(self):
        """Negative: ModelRole 参与 allow_model_role=False 的 gate。"""
        service = _make_gate_service()
        decision = _make_valid_decision(
            actor_id="model-role-001",
            actor_role="PROOF_JUDGE",
            gate_type="PROOF_REVIEW",
            decision="REJECT",
            key_id="key-human-001",
        )
        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_SELF_APPROVAL_REJECTED, result.error_codes)

    def test_expired_key_rejected(self):
        """Negative: 过期 key 被拒绝。"""
        service = _make_gate_service()
        decision = _make_valid_decision()
        _create_task_for_decision(service, decision)

        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-21T00:00:00Z",  # key 已过期
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.KEY_EXPIRED, result.error_codes)

    def test_revoked_key_rejected(self):
        """Fault: 撤销 key 后使用被拒绝。"""
        service = _make_gate_service()
        decision = _make_valid_decision()
        _create_task_for_decision(service, decision)

        # 先接受一次合法 decision
        result1 = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertTrue(result1.passed)

        # 撤销 key
        service.revoke_key("key-human-001", revocation_ref="rev-001")

        # 用同一 key 的新 decision 被拒绝
        decision2 = _make_valid_decision(
            decision_id="dec-002",
            nonce="nonce-bbbbbbbbbbbbbbbb",
        )
        _create_task_for_decision(service, decision2, creator_actor_id="human-architect-001")
        # 需要新 task
        service.task_port.create_task(
            task_id="task-002",
            gate_type="PROOF_REVIEW",
            payload_ref="payload-ref-001",
            payload_hash=decision2["payload_hash"],
            allowed_view="PROOF_VIEW",
            deadline="2026-08-16T00:00:00Z",
            eligible_roles=frozenset({"PROOF_JUDGE"}),
            separation_policy="CREATOR_CANNOT_APPROVE",
            required_signatures=1,
            nonce="task-nonce-bbbbbbbbbbbb",
            creator_actor_id="human-architect-001",
        )
        decision2["task_id"] = "task-002"
        from seven_system.human.gate_decision import (
            _compute_signed_bytes_hash, _compute_decision_hash,
        )
        decision2["signed_bytes_hash"] = _compute_signed_bytes_hash(decision2)
        decision2["signature_envelope"]["signed_bytes_hash"] = decision2["signed_bytes_hash"]
        decision2["decision_hash"] = _compute_decision_hash(decision2)

        result2 = service.accept_gate_decision(
            decision2,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result2.passed)
        self.assertIn(EC.KEY_REVOKED, result2.error_codes)

    def test_replay_same_nonce_payload_actor(self):
        """Fault: replay 攻击——相同 nonce/payload/actor 的 decision 被拒绝。"""
        service = _make_gate_service()
        decision = _make_valid_decision()
        _create_task_for_decision(service, decision)

        # 第一次接受
        result1 = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertTrue(result1.passed)

        # 第二次重放被拒绝
        result2 = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result2.passed)
        self.assertIn(EC.GATE_REPLAY_DETECTED, result2.error_codes)

    def test_replay_same_decision_id(self):
        """Negative: 相同 decision_id 被拒绝（即使其他字段不同）。"""
        service = _make_gate_service()
        decision = _make_valid_decision()
        _create_task_for_decision(service, decision)

        result1 = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertTrue(result1.passed)

        # 新 decision 但相同 decision_id
        decision2 = _make_valid_decision(
            decision_id="dec-001",  # 相同 ID
            nonce="nonce-bbbbbbbbbbbbbbbb",
            task_id="task-002",
        )
        from seven_system.human.gate_decision import (
            _compute_signed_bytes_hash, _compute_decision_hash,
        )
        decision2["signed_bytes_hash"] = _compute_signed_bytes_hash(decision2)
        decision2["signature_envelope"]["signed_bytes_hash"] = decision2["signed_bytes_hash"]
        decision2["decision_hash"] = _compute_decision_hash(decision2)

        result2 = service.accept_gate_decision(
            decision2,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result2.passed)
        self.assertIn(EC.GATE_REPLAY_DETECTED, result2.error_codes)

    def test_payload_tampering_detected(self):
        """Negative: payload 改写后签名 hash 不匹配。"""
        service = _make_gate_service()
        decision = _make_valid_decision()
        _create_task_for_decision(service, decision)

        # 篡改 payload_hash 但不重算签名
        decision["payload_hash"] = "1" * 64
        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result.passed)
        # 结构验证就会失败：signed_bytes_hash 不匹配
        self.assertIn(EC.GATE_DECISION_HASH_MISMATCH, result.error_codes)

    def test_duty_conflict_creator_approves(self):
        """Negative: 职责冲突——创建者不能批准自己的 payload。"""
        service = _make_gate_service()
        decision = _make_valid_decision()
        # 创建者和批准者是同一人
        _create_task_for_decision(
            service, decision, creator_actor_id="human-reviewer-001"
        )

        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_DUTY_CONFLICT, result.error_codes)

    def test_missing_required_role(self):
        """Negative: actor 缺少 gate 要求的角色。"""
        service = _make_gate_service()
        # human-architect-001 只有 QUESTION_ARCHITECT，没有 PROOF_JUDGE
        decision = _make_valid_decision(
            actor_id="human-architect-001",
            actor_role="QUESTION_ARCHITECT",
            gate_type="PROOF_REVIEW",
            key_id="key-architect-001",
        )
        _create_task_for_decision(service, decision)

        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_REQUIRED_ROLE_MISSING, result.error_codes)

    def test_unknown_gate_type(self):
        """Negative: 未知 gate type。"""
        service = _make_gate_service()
        decision = _make_valid_decision(gate_type="NONEXISTENT_GATE")
        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.GATE_TYPE_UNKNOWN, result.error_codes)

    def test_unsigned_decision_rejected_by_service(self):
        """Negative: 未签名的 decision 被 HumanGateService 拒绝。"""
        service = _make_gate_service()
        decision = _make_valid_decision()
        decision["signature_envelope"]["signature_b64"] = ""
        from seven_system.human.gate_decision import (
            _compute_signed_bytes_hash, _compute_decision_hash,
        )
        decision["signed_bytes_hash"] = _compute_signed_bytes_hash(decision)
        decision["signature_envelope"]["signed_bytes_hash"] = decision["signed_bytes_hash"]
        decision["decision_hash"] = _compute_decision_hash(decision)

        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.SIGNATURE_INVALID, result.error_codes)

    def test_inactive_actor_rejected(self):
        """Negative: 停用的 actor 被拒绝。"""
        service = _make_gate_service()
        service.actor_roster.deactivate("human-reviewer-001")
        decision = _make_valid_decision()
        _create_task_for_decision(service, decision)

        result = service.accept_gate_decision(
            decision,
            evaluation_time="2026-08-14T12:30:00Z",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.ACTOR_INACTIVE, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# GV0 消费测试
# ═══════════════════════════════════════════════════════════════════════


class TestGV0Consumption(unittest.TestCase):
    """HumanGateService 必须消费 GV0 CompletionContractVerifier 做状态命令验证。"""

    def test_consume_gv0_valid_state_command(self):
        """Golden: HumanGateService 消费 GV0 验证合法状态命令。"""
        service = _make_gate_service()
        bundle = _make_implementation_bundle("WP-HG0")
        result = service.verify_state_command(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-HG0",
            submitted_object=bundle,
            actor_type="IMPLEMENTER",
            state_command="READY_FOR_AUDIT",
        )
        self.assertTrue(result.passed, msg=str(result.details))

    def test_consume_gv0_reject_invalid_state(self):
        """Negative: GV0 拒绝实施者写 AUDITED_* 状态。"""
        service = _make_gate_service()
        bundle = _make_implementation_bundle("WP-HG0")
        result = service.verify_state_command(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-HG0",
            submitted_object=bundle,
            actor_type="IMPLEMENTER",
            state_command="AUDITED_PASS",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.STATE_COMMAND_REJECTED, result.error_codes)

    def test_consume_gv0_reject_wrong_schema(self):
        """Negative: GV0 拒绝错误 schema_id。"""
        service = _make_gate_service()
        bundle = _make_implementation_bundle("WP-HG0")
        bundle["schema_id"] = "wrong-schema"
        result = service.verify_state_command(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-HG0",
            submitted_object=bundle,
            actor_type="IMPLEMENTER",
            state_command="READY_FOR_AUDIT",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.SCHEMA_ID_MISMATCH, result.error_codes)

    def test_consume_gv0_reject_dag_hash_mismatch(self):
        """Negative: GV0 拒绝 DAG hash 不匹配。"""
        service = _make_gate_service()
        bundle = _make_implementation_bundle("WP-HG0")
        result = service.verify_state_command(
            dag_path=DAG_PATH,
            expected_dag_sha256="0" * 64,
            wp_id="WP-HG0",
            submitted_object=bundle,
            actor_type="IMPLEMENTER",
            state_command="READY_FOR_AUDIT",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.DAG_HASH_MISMATCH, result.error_codes)

    def test_consume_gv0_reject_auditor_on_implementer_wp(self):
        """Negative: GV0 拒绝审计者写实施者工作包。"""
        service = _make_gate_service()
        bundle = _make_implementation_bundle("WP-HG0")
        result = service.verify_state_command(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-HG0",
            submitted_object=bundle,
            actor_type="AUDITOR",
            state_command="READY_FOR_AUDIT",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.ACTOR_NOT_AUTHORIZED, result.error_codes)

    def test_gv0_consumption_not_copied(self):
        """验证 HumanGateService.verify_state_command 返回的是 GV0 VerificationResult。

        这证明 HG0 消费 GV0 而非复制——返回类型和字段与 GV0 一致。
        """
        service = _make_gate_service()
        bundle = _make_implementation_bundle("WP-HG0")
        result = service.verify_state_command(
            dag_path=DAG_PATH,
            expected_dag_sha256=_dag_sha256(),
            wp_id="WP-HG0",
            submitted_object=bundle,
            actor_type="IMPLEMENTER",
            state_command="READY_FOR_AUDIT",
        )
        # GV0 VerificationResult 有 dag_sha256/wp_id/owner_type 等字段
        self.assertEqual(result.wp_id, "WP-HG0")
        self.assertEqual(result.owner_type, "IMPLEMENTER")
        self.assertEqual(
            result.completion_contract, "IMPLEMENTATION_BUNDLE"
        )


# ═══════════════════════════════════════════════════════════════════════
# 多签 Gate 测试
# ═══════════════════════════════════════════════════════════════════════


class TestMultiSignatureGate(unittest.TestCase):
    """多签 Gate：required_signatures > 1 时的累积逻辑。"""

    def test_multi_sig_gate_requires_multiple(self):
        """Golden: 多签 gate 注册和验证。"""
        registry = GateTypeRegistry()
        registry.register(GateTypeSpec(
            gate_type="PROMOTION_GATE",
            required_roles=frozenset({"MATH_VERIFIER", "PROOF_JUDGE"}),
            required_signatures=2,
            allow_model_role=False,
            separation_policy="INDEPENDENT_REVIEW",
        ))
        spec = registry.get("PROMOTION_GATE")
        self.assertEqual(spec.required_signatures, 2)


if __name__ == "__main__":
    unittest.main()
