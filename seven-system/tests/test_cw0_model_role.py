"""WP-CW0 ModelRolePort / attempt / receipt / reconcile 测试。

测试层级：Golden → Negative → Fault injection
覆盖：
- RoleRegistry 冻结验证
- RoleExecutionContract 验证
- Attempt 状态机
- AttemptReceipt 验证
- FakeModelRoleAdapter 完整 dispatch 链
- 确定性输出验证
- AttemptReconciler 识别 unknown-start / stale-fence / sensitive-sink / illegal-state

所有 blocker test 失败 → 工作包 FAIL。
"""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import (
    ATTEMPT_STATES,
    ATTEMPT_TERMINAL_STATES,
    ATTEMPT_TRANSITIONS,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.cognitive.role_registry import (
    RoleDefinition,
    RoleRegistry,
    ROLE_REGISTRY_FROZEN_V1,
    verify_role_registry,
)
from seven_system.cognitive.role_execution_contract import (
    RoleExecutionContract,
    build_role_execution_contract,
    verify_role_execution_contract,
)
from seven_system.cognitive.model_role_port import (
    DispatchRequest,
    DispatchResult,
    ModelRolePort,
)
from seven_system.cognitive.attempt import (
    Attempt,
    AttemptReceipt,
    AttemptState,
    build_attempt_receipt,
    verify_attempt_receipt,
)
from seven_system.cognitive.fake_adapter import FakeModelRoleAdapter
from seven_system.cognitive.reconcile import (
    AttemptReconciler,
    ReconcileResult,
)


# ─── helpers ───────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64


def _policy_hash(kind: str, kind_field: str = "view_policy_kind") -> str:
    """计算 policy kind 的 hash（与 role_execution_contract.py 中一致）。"""
    return hashlib.sha256(
        canonical_json_bytes({kind_field: kind})
    ).hexdigest()


def _make_ref(ref_id: str, sha256: str = _ZERO_HASH) -> dict[str, str]:
    return {"ref_id": ref_id, "sha256": sha256}


def _make_contract(
    *,
    role_type_id: str = "question_architect",
    adapter_kind: str = "FAKE",
    role_job_id: str = "job-001",
    view_policy_kind: str | None = None,
    tool_policy_kind: str | None = None,
    carrier_profile_hash: str = _ZERO_HASH,
) -> RoleExecutionContract:
    """构建一个合法的 RoleExecutionContract。"""
    registry = ROLE_REGISTRY_FROZEN_V1
    role_def = registry.get_role(role_type_id)

    # 使用 role_def 的 policy kind，除非显式覆盖或角色不存在
    if role_def is not None:
        vp_kind = view_policy_kind or role_def.view_policy_kind
        tp_kind = tool_policy_kind or role_def.tool_policy_kind
    else:
        vp_kind = view_policy_kind or "PUBLIC_ONLY"
        tp_kind = tool_policy_kind or "NO_TOOLS"

    view_policy_hash = _policy_hash(vp_kind, "view_policy_kind")
    tool_policy_hash = _policy_hash(tp_kind, "tool_policy_kind")

    return build_role_execution_contract(
        role_job_id=role_job_id,
        epoch_id="epoch-001",
        role_type_registry_ref_and_hash=registry.ref_and_hash,
        role_type_id=role_type_id,
        carrier_profile_ref_and_hash=_make_ref("profile-001", carrier_profile_hash),
        view_policy_ref_and_hash=_make_ref("view-policy-001", view_policy_hash),
        tool_policy_ref_and_hash=_make_ref("tool-policy-001", tool_policy_hash),
        adapter_kind=adapter_kind,
        vault_access_capability_ref_and_hash=_make_ref("vault-cap-001"),
        output_schema_ref_and_hash=_make_ref("output-schema-001"),
        budget_contract_ref_and_hash=_make_ref("budget-001"),
        prompt_release_ref_and_hash=_make_ref("prompt-001"),
        idempotency_key="idem-001",
    )


def _make_dispatch_request(
    *,
    contract: RoleExecutionContract | None = None,
    input_view_bytes: bytes = b"test input view",
    input_view_id: str = "view-001",
    sink_id: str = "sink-001",
    fence_token: str = "fence-001",
    timeout_seconds: float = 0.0,
) -> DispatchRequest:
    return DispatchRequest(
        contract=contract or _make_contract(),
        input_view_bytes=input_view_bytes,
        input_view_id=input_view_id,
        sink_id=sink_id,
        fence_token=fence_token,
        timeout_seconds=timeout_seconds,
    )


# ═══════════════════════════════════════════════════════════════════════
# Golden: RoleRegistry
# ═══════════════════════════════════════════════════════════════════════


class TestRoleRegistryGolden(unittest.TestCase):
    """Golden: RoleRegistry 冻结验证。"""

    def test_frozen_v1_has_all_11_roles(self):
        """冻结 v1 注册表包含全部 11 个角色。"""
        role_ids = ROLE_REGISTRY_FROZEN_V1.all_role_type_ids()
        expected = {
            "question_architect",
            "adversarial_editor",
            "math_verifier",
            "trace_analyst",
            "solution_analyst",
            "adjudicator",
            "process_auditor",
            "proof_judge",
            "leakage_auditor",
            "selector",
            "hint_renderer",
        }
        self.assertEqual(set(role_ids), expected)

    def test_frozen_v1_verifies(self):
        """冻结 v1 注册表通过验证。"""
        result = verify_role_registry(ROLE_REGISTRY_FROZEN_V1)
        self.assertTrue(result.passed, f"Registry verification failed: {result.details}")

    def test_frozen_v1_has_content_hash(self):
        """冻结 v1 注册表有非空 content_hash。"""
        self.assertTrue(ROLE_REGISTRY_FROZEN_V1.content_hash)
        self.assertEqual(len(ROLE_REGISTRY_FROZEN_V1.content_hash), 64)

    def test_frozen_v1_status_is_frozen(self):
        """冻结 v1 注册表 status 为 FROZEN。"""
        self.assertEqual(ROLE_REGISTRY_FROZEN_V1.status, "FROZEN")

    def test_all_roles_have_no_tools(self):
        """所有角色 tool_policy_kind 为 NO_TOOLS。"""
        for rd in ROLE_REGISTRY_FROZEN_V1.role_definitions:
            self.assertEqual(
                rd.tool_policy_kind, "NO_TOOLS",
                f"role {rd.role_type_id} has tool_policy_kind={rd.tool_policy_kind}"
            )

    def test_all_roles_have_required_profile_fields(self):
        """所有角色有 required_profile_fields。"""
        for rd in ROLE_REGISTRY_FROZEN_V1.role_definitions:
            self.assertTrue(rd.required_profile_fields,
                            f"role {rd.role_type_id} has empty required_profile_fields")
            # 必须包含 carrier 和 model_uid
            self.assertIn("carrier", rd.required_profile_fields)
            self.assertIn("model_uid", rd.required_profile_fields)

    def test_all_roles_have_view_policy(self):
        """所有角色有 view_policy_kind。"""
        for rd in ROLE_REGISTRY_FROZEN_V1.role_definitions:
            self.assertTrue(rd.view_policy_kind,
                            f"role {rd.role_type_id} has empty view_policy_kind")

    def test_ref_and_hash_format(self):
        """ref_and_hash 格式正确。"""
        ref = ROLE_REGISTRY_FROZEN_V1.ref_and_hash
        self.assertIn("ref_id", ref)
        self.assertIn("sha256", ref)
        self.assertEqual(ref["sha256"], ROLE_REGISTRY_FROZEN_V1.content_hash)

    def test_get_role_returns_definition(self):
        """get_role 返回正确的 RoleDefinition。"""
        rd = ROLE_REGISTRY_FROZEN_V1.get_role("question_architect")
        self.assertIsNotNone(rd)
        self.assertEqual(rd.role_type_id, "question_architect")

    def test_get_role_unknown_returns_none(self):
        """get_role 对未知角色返回 None。"""
        self.assertIsNone(ROLE_REGISTRY_FROZEN_V1.get_role("nonexistent_role"))


# ═══════════════════════════════════════════════════════════════════════
# Negative: RoleRegistry
# ═══════════════════════════════════════════════════════════════════════


class TestRoleRegistryNegative(unittest.TestCase):
    """Negative: RoleRegistry 异常情况。"""

    def test_registry_with_duplicate_roles_fails(self):
        """重复 role_type_id 验证失败。"""
        roles = (
            RoleDefinition(
                role_type_id="duplicate_role",
                required_profile_fields=("carrier", "model_uid"),
                view_policy_kind="PUBLIC_ONLY",
                tool_policy_kind="NO_TOOLS",
                description="first",
            ),
            RoleDefinition(
                role_type_id="duplicate_role",
                required_profile_fields=("carrier", "model_uid"),
                view_policy_kind="PUBLIC_ONLY",
                tool_policy_kind="NO_TOOLS",
                description="second",
            ),
        )
        registry = RoleRegistry(
            registry_id="seven_model_role_types",
            registry_version="2.0.0",
            schema_version="role_type_registry.v1",
            status="FROZEN",
            role_definitions=roles,
        )
        result = verify_role_registry(registry)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_UNKNOWN_ROLE, result.error_codes)

    def test_registry_not_frozen_fails(self):
        """status 不是 FROZEN 验证失败。"""
        registry = RoleRegistry(
            registry_id="seven_model_role_types",
            registry_version="2.0.0",
            schema_version="role_type_registry.v1",
            status="DRAFT",
            role_definitions=(),
        )
        result = verify_role_registry(registry)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_ROLE_NOT_FROZEN, result.error_codes)

    def test_registry_with_reserved_word_role_fails(self):
        """role_type_id 为保留字验证失败。"""
        roles = (
            RoleDefinition(
                role_type_id="ANY",
                required_profile_fields=("carrier",),
                view_policy_kind="PUBLIC_ONLY",
                tool_policy_kind="NO_TOOLS",
                description="reserved",
            ),
        )
        registry = RoleRegistry(
            registry_id="seven_model_role_types",
            registry_version="2.0.0",
            schema_version="role_type_registry.v1",
            status="FROZEN",
            role_definitions=roles,
        )
        result = verify_role_registry(registry)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_UNKNOWN_ROLE, result.error_codes)

    def test_registry_with_invalid_view_policy_fails(self):
        """无效 view_policy_kind 验证失败。"""
        roles = (
            RoleDefinition(
                role_type_id="bad_role",
                required_profile_fields=("carrier",),
                view_policy_kind="INVALID",
                tool_policy_kind="NO_TOOLS",
                description="bad",
            ),
        )
        registry = RoleRegistry(
            registry_id="seven_model_role_types",
            registry_version="2.0.0",
            schema_version="role_type_registry.v1",
            status="FROZEN",
            role_definitions=roles,
        )
        result = verify_role_registry(registry)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_ROLE_MISSING_VIEW_POLICY, result.error_codes)

    def test_registry_with_invalid_tool_policy_fails(self):
        """无效 tool_policy_kind 验证失败。"""
        roles = (
            RoleDefinition(
                role_type_id="bad_role",
                required_profile_fields=("carrier",),
                view_policy_kind="PUBLIC_ONLY",
                tool_policy_kind="INVALID",
                description="bad",
            ),
        )
        registry = RoleRegistry(
            registry_id="seven_model_role_types",
            registry_version="2.0.0",
            schema_version="role_type_registry.v1",
            status="FROZEN",
            role_definitions=roles,
        )
        result = verify_role_registry(registry)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_ROLE_TOOL_POLICY_ALLOWS_TOOLS, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# Golden: RoleExecutionContract
# ═══════════════════════════════════════════════════════════════════════


class TestRoleExecutionContractGolden(unittest.TestCase):
    """Golden: RoleExecutionContract 验证。"""

    def test_valid_contract_verifies(self):
        """合法 contract 通过验证。"""
        contract = _make_contract()
        result = verify_role_execution_contract(contract, registry=ROLE_REGISTRY_FROZEN_V1)
        self.assertTrue(result.passed, f"Contract verification failed: {result.details}")

    def test_contract_has_hash(self):
        """contract 有非空 contract_hash。"""
        contract = _make_contract()
        self.assertTrue(contract.contract_hash)
        self.assertEqual(len(contract.contract_hash), 64)

    def test_contract_hash_is_deterministic(self):
        """相同输入产生相同 contract_hash。"""
        c1 = _make_contract(role_job_id="job-001")
        c2 = _make_contract(role_job_id="job-001")
        self.assertEqual(c1.contract_hash, c2.contract_hash)

    def test_contract_hash_differs_for_different_roles(self):
        """不同 role_type_id 产生不同 contract_hash。"""
        c1 = _make_contract(role_type_id="question_architect", role_job_id="job-001")
        c2 = _make_contract(role_type_id="math_verifier", role_job_id="job-001")
        self.assertNotEqual(c1.contract_hash, c2.contract_hash)

    def test_contract_to_dict_roundtrip(self):
        """contract to_dict 包含所有字段。"""
        contract = _make_contract()
        d = contract.to_dict()
        required_fields = {
            "role_job_id", "epoch_id", "role_type_registry_ref_and_hash",
            "role_type_id", "carrier_profile_ref_and_hash",
            "view_policy_ref_and_hash", "tool_policy_ref_and_hash",
            "adapter_kind", "vault_access_capability_ref_and_hash",
            "output_schema_ref_and_hash", "budget_contract_ref_and_hash",
            "prompt_release_ref_and_hash", "idempotency_key",
            "contract_hash_algorithm", "contract_hash",
        }
        self.assertEqual(set(d.keys()), required_fields)


# ═══════════════════════════════════════════════════════════════════════
# Negative: RoleExecutionContract
# ═══════════════════════════════════════════════════════════════════════


class TestRoleExecutionContractNegative(unittest.TestCase):
    """Negative: RoleExecutionContract 异常情况。"""

    def test_unknown_role_fails(self):
        """未知 role_type_id 验证失败。"""
        contract = _make_contract(role_type_id="nonexistent_role")
        result = verify_role_execution_contract(contract, registry=ROLE_REGISTRY_FROZEN_V1)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_UNKNOWN_ROLE, result.error_codes)

    def test_registry_hash_mismatch_fails(self):
        """registry hash 不匹配验证失败。"""
        contract = _make_contract()
        # 篡改 registry ref hash
        d = contract.to_dict()
        d["role_type_registry_ref_and_hash"]["sha256"] = "1" * 64
        result = verify_role_execution_contract(d, registry=ROLE_REGISTRY_FROZEN_V1)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_REGISTRY_HASH_MISMATCH, result.error_codes)

    def test_view_policy_mismatch_fails(self):
        """view policy hash 与 role 定义不匹配验证失败。"""
        contract = _make_contract(role_type_id="question_architect")
        d = contract.to_dict()
        # 篡改 view policy hash
        d["view_policy_ref_and_hash"]["sha256"] = _ZERO_HASH
        result = verify_role_execution_contract(d, registry=ROLE_REGISTRY_FROZEN_V1)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_CONTRACT_VIEW_POLICY_MISMATCH, result.error_codes)

    def test_tool_policy_mismatch_fails(self):
        """tool policy hash 与 role 定义不匹配验证失败。"""
        contract = _make_contract(role_type_id="question_architect")
        d = contract.to_dict()
        # 篡改 tool policy hash
        d["tool_policy_ref_and_hash"]["sha256"] = _ZERO_HASH
        result = verify_role_execution_contract(d, registry=ROLE_REGISTRY_FROZEN_V1)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_CONTRACT_TOOL_POLICY_MISMATCH, result.error_codes)

    def test_invalid_adapter_kind_fails(self):
        """无效 adapter_kind 验证失败。"""
        contract = _make_contract(adapter_kind="INVALID_ADAPTER")
        result = verify_role_execution_contract(contract, registry=ROLE_REGISTRY_FROZEN_V1)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_CONTRACT_ADAPTER_MISMATCH, result.error_codes)

    def test_contract_hash_mismatch_fails(self):
        """contract_hash 不匹配验证失败。"""
        contract = _make_contract()
        d = contract.to_dict()
        d["contract_hash"] = "1" * 64
        result = verify_role_execution_contract(d, registry=ROLE_REGISTRY_FROZEN_V1)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_CONTRACT_HASH_MISMATCH, result.error_codes)

    def test_role_with_tool_policy_allowing_tools_fails(self):
        """角色 tool_policy 允许工具（非 NO_TOOLS）验证失败。"""
        # 创建一个 tool_policy_kind 不是 NO_TOOLS 的角色
        bad_role = RoleDefinition(
            role_type_id="bad_tool_role",
            required_profile_fields=("carrier", "model_uid"),
            view_policy_kind="PUBLIC_ONLY",
            tool_policy_kind="READ_ONLY_TOOLS",
            description="bad tools",
        )
        registry = RoleRegistry(
            registry_id="seven_model_role_types",
            registry_version="2.0.0",
            schema_version="role_type_registry.v1",
            status="FROZEN",
            role_definitions=(bad_role,),
        )
        # 构建一个 contract 引用这个角色
        tool_policy_hash = _policy_hash("READ_ONLY_TOOLS", "tool_policy_kind")
        contract = build_role_execution_contract(
            role_job_id="job-001",
            epoch_id="epoch-001",
            role_type_registry_ref_and_hash=registry.ref_and_hash,
            role_type_id="bad_tool_role",
            carrier_profile_ref_and_hash=_make_ref("profile-001"),
            view_policy_ref_and_hash=_make_ref("view-policy-001", _policy_hash("PUBLIC_ONLY", "view_policy_kind")),
            tool_policy_ref_and_hash=_make_ref("tool-policy-001", tool_policy_hash),
            adapter_kind="FAKE",
            vault_access_capability_ref_and_hash=_make_ref("vault-cap-001"),
            output_schema_ref_and_hash=_make_ref("output-schema-001"),
            budget_contract_ref_and_hash=_make_ref("budget-001"),
            prompt_release_ref_and_hash=_make_ref("prompt-001"),
            idempotency_key="idem-001",
        )
        result = verify_role_execution_contract(contract, registry=registry)
        self.assertFalse(result.passed)
        self.assertIn(EC.CW0_ROLE_TOOL_POLICY_ALLOWS_TOOLS, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# Golden: Attempt state machine
# ═══════════════════════════════════════════════════════════════════════


class TestAttemptStateMachineGolden(unittest.TestCase):
    """Golden: Attempt 状态机。"""

    def test_created_to_accepted(self):
        """CREATED → ACCEPTED 合法。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
        )
        result = attempt.transition_to(AttemptState.ACCEPTED, "2026-08-14T12:00:00Z")
        self.assertTrue(result.passed)
        self.assertEqual(attempt.state, AttemptState.ACCEPTED)
        self.assertEqual(attempt.accepted_at, "2026-08-14T12:00:00Z")

    def test_full_lifecycle(self):
        """完整生命周期：CREATED → ACCEPTED → STARTED → COMPLETED。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
        )
        self.assertTrue(attempt.transition_to(AttemptState.ACCEPTED, "t1").passed)
        self.assertTrue(attempt.transition_to(AttemptState.STARTED, "t2").passed)
        self.assertTrue(attempt.transition_to(AttemptState.COMPLETED, "t3").passed)
        self.assertEqual(attempt.state, AttemptState.COMPLETED)

    def test_is_terminal(self):
        """终态识别。"""
        self.assertTrue(AttemptState.is_terminal(AttemptState.COMPLETED))
        self.assertTrue(AttemptState.is_terminal(AttemptState.TERMINATED))
        self.assertTrue(AttemptState.is_terminal(AttemptState.CANCELLED))
        self.assertTrue(AttemptState.is_terminal(AttemptState.TIMED_OUT))
        self.assertFalse(AttemptState.is_terminal(AttemptState.CREATED))
        self.assertFalse(AttemptState.is_terminal(AttemptState.ACCEPTED))
        self.assertFalse(AttemptState.is_terminal(AttemptState.STARTED))

    def test_can_transition(self):
        """状态转换合法性。"""
        self.assertTrue(AttemptState.can_transition(AttemptState.CREATED, AttemptState.ACCEPTED))
        self.assertTrue(AttemptState.can_transition(AttemptState.ACCEPTED, AttemptState.STARTED))
        self.assertTrue(AttemptState.can_transition(AttemptState.STARTED, AttemptState.COMPLETED))
        self.assertFalse(AttemptState.can_transition(AttemptState.CREATED, AttemptState.STARTED))
        self.assertFalse(AttemptState.can_transition(AttemptState.CREATED, AttemptState.COMPLETED))


# ═══════════════════════════════════════════════════════════════════════
# Negative: Attempt state machine
# ═══════════════════════════════════════════════════════════════════════


class TestAttemptStateMachineNegative(unittest.TestCase):
    """Negative: Attempt 状态机非法转换。"""

    def test_created_to_started_illegal(self):
        """CREATED → STARTED 非法（跳过 ACCEPTED）。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
        )
        result = attempt.transition_to(AttemptState.STARTED)
        self.assertFalse(result.passed)
        self.assertIn(EC.ATTEMPT_ILLEGAL_STATE_TRANSITION, result.error_codes)

    def test_created_to_completed_illegal(self):
        """CREATED → COMPLETED 非法（跳过中间状态）。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
        )
        result = attempt.transition_to(AttemptState.COMPLETED)
        self.assertFalse(result.passed)
        self.assertIn(EC.ATTEMPT_ILLEGAL_STATE_TRANSITION, result.error_codes)

    def test_terminal_to_any_illegal(self):
        """终态不能转换到其他状态。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.COMPLETED,
        )
        result = attempt.transition_to(AttemptState.STARTED)
        self.assertFalse(result.passed)
        self.assertIn(EC.ATTEMPT_ALREADY_TERMINATED, result.error_codes)

    def test_unknown_state_illegal(self):
        """未知状态非法。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
        )
        result = attempt.transition_to("INVALID_STATE")
        self.assertFalse(result.passed)
        self.assertIn(EC.ATTEMPT_ILLEGAL_STATE_TRANSITION, result.error_codes)

    def test_completed_to_started_illegal(self):
        """COMPLETED → STARTED 非法。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.COMPLETED,
        )
        result = attempt.transition_to(AttemptState.STARTED)
        self.assertFalse(result.passed)


# ═══════════════════════════════════════════════════════════════════════
# Golden: AttemptReceipt
# ═══════════════════════════════════════════════════════════════════════


class TestAttemptReceiptGolden(unittest.TestCase):
    """Golden: AttemptReceipt 验证。"""

    def test_valid_receipt_verifies(self):
        """合法 receipt 通过验证。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.COMPLETED,
            output_artifact_hashes=[_ZERO_HASH],
            output_sink_ref="sink-001",
            output_sink_kind="RESTRICTED_VAULT",
            terminal_reason="COMPLETED",
        )
        receipt = build_attempt_receipt(attempt=attempt)
        result = verify_attempt_receipt(receipt)
        self.assertTrue(result.passed, f"Receipt verification failed: {result.details}")

    def test_receipt_has_hash(self):
        """receipt 有非空 receipt_hash。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.COMPLETED,
            output_artifact_hashes=[_ZERO_HASH],
            output_sink_ref="sink-001",
            output_sink_kind="RESTRICTED_VAULT",
            terminal_reason="COMPLETED",
        )
        receipt = build_attempt_receipt(attempt=attempt)
        self.assertTrue(receipt.receipt_hash)
        self.assertEqual(len(receipt.receipt_hash), 64)

    def test_receipt_hash_deterministic(self):
        """相同 attempt 产生相同 receipt_hash。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.COMPLETED,
            output_artifact_hashes=[_ZERO_HASH],
            output_sink_ref="sink-001",
            output_sink_kind="RESTRICTED_VAULT",
            terminal_reason="COMPLETED",
        )
        r1 = build_attempt_receipt(attempt=attempt)
        r2 = build_attempt_receipt(attempt=attempt)
        self.assertEqual(r1.receipt_hash, r2.receipt_hash)

    def test_receipt_lifecycle_events(self):
        """receipt 包含生命周期事件。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.ACCEPTED,
            created_at="t1",
            accepted_at="t2",
        )
        receipt = build_attempt_receipt(attempt=attempt)
        states = [e["state"] for e in receipt.lifecycle_events]
        self.assertIn(AttemptState.CREATED, states)
        self.assertIn(AttemptState.ACCEPTED, states)


# ═══════════════════════════════════════════════════════════════════════
# Negative: AttemptReceipt
# ═══════════════════════════════════════════════════════════════════════


class TestAttemptReceiptNegative(unittest.TestCase):
    """Negative: AttemptReceipt 异常情况。"""

    def test_terminal_without_reason_fails(self):
        """终态没有 terminal_reason 验证失败。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.COMPLETED,
            output_artifact_hashes=[_ZERO_HASH],
            output_sink_ref="sink-001",
            output_sink_kind="RESTRICTED_VAULT",
            terminal_reason="",  # 空 terminal_reason
        )
        receipt = build_attempt_receipt(attempt=attempt)
        result = verify_attempt_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_completed_without_output_fails(self):
        """COMPLETED 状态没有 output_artifact_hashes 验证失败。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.COMPLETED,
            output_artifact_hashes=[],  # 空
            terminal_reason="COMPLETED",
        )
        receipt = build_attempt_receipt(attempt=attempt)
        result = verify_attempt_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_receipt_hash_mismatch_fails(self):
        """receipt_hash 不匹配验证失败。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.COMPLETED,
            output_artifact_hashes=[_ZERO_HASH],
            output_sink_ref="sink-001",
            output_sink_kind="RESTRICTED_VAULT",
            terminal_reason="COMPLETED",
        )
        receipt = build_attempt_receipt(attempt=attempt)
        d = receipt.to_dict()
        d["receipt_hash"] = "1" * 64
        result = verify_attempt_receipt(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.ATTEMPT_RECEIPT_HASH_MISMATCH, result.error_codes)

    def test_invalid_sink_kind_fails(self):
        """无效 output_sink_kind 验证失败。"""
        attempt = Attempt(
            attempt_id="a-001", role_job_id="j-001", role_type_id="question_architect",
            contract_hash=_ZERO_HASH, carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE", fence_token="f-001",
            state=AttemptState.COMPLETED,
            output_artifact_hashes=[_ZERO_HASH],
            output_sink_ref="sink-001",
            output_sink_kind="INVALID_SINK",
            terminal_reason="COMPLETED",
        )
        receipt = build_attempt_receipt(attempt=attempt)
        result = verify_attempt_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ATTEMPT_SENSITIVE_SINK, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# Golden: FakeModelRoleAdapter
# ═══════════════════════════════════════════════════════════════════════


class TestFakeAdapterGolden(unittest.TestCase):
    """Golden: FakeModelRoleAdapter 完整 dispatch 链。"""

    def test_dispatch_accepted_started_completed(self):
        """valid role dispatch → accepted → started → completed with receipt。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        self.assertTrue(result.accepted)
        self.assertEqual(result.attempt.state, AttemptState.COMPLETED)
        self.assertTrue(result.receipt.is_completed)
        self.assertTrue(result.receipt.output_artifact_hashes)
        self.assertEqual(result.receipt.output_sink_kind, "RESTRICTED_VAULT")
        self.assertEqual(result.receipt.terminal_reason, "COMPLETED")

    def test_receipt_verifies(self):
        """dispatch 产生的 receipt 通过验证。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        receipt_result = verify_attempt_receipt(result.receipt)
        self.assertTrue(receipt_result.passed,
                        f"Receipt verification failed: {receipt_result.details}")

    def test_deterministic_output_same_input_profile(self):
        """fake adapter 对相同 input + profile 返回确定性输出。"""
        adapter1 = FakeModelRoleAdapter()
        adapter2 = FakeModelRoleAdapter()

        contract = _make_contract()
        request = _make_dispatch_request(contract=contract, input_view_bytes=b"same input")

        result1 = adapter1.dispatch(request)
        result2 = adapter2.dispatch(request)

        # 相同 input + profile → 相同 output
        self.assertEqual(
            result1.receipt.output_artifact_hashes,
            result2.receipt.output_artifact_hashes,
        )

    def test_different_input_different_output(self):
        """不同 input 产生不同 output。"""
        adapter = FakeModelRoleAdapter()
        contract = _make_contract(role_job_id="job-001")

        request1 = _make_dispatch_request(contract=contract, input_view_bytes=b"input A")
        request2 = _make_dispatch_request(contract=contract, input_view_bytes=b"input B")

        # 需要不同的 role_job_id 以避免 attempt_id 冲突
        contract2 = _make_contract(role_job_id="job-002")
        request2 = _make_dispatch_request(contract=contract2, input_view_bytes=b"input B")

        result1 = adapter.dispatch(request1)
        result2 = adapter.dispatch(request2)

        self.assertNotEqual(
            result1.receipt.output_artifact_hashes,
            result2.receipt.output_artifact_hashes,
        )

    def test_different_profile_different_output(self):
        """不同 carrier_profile_hash 产生不同 output。"""
        adapter = FakeModelRoleAdapter()

        contract1 = _make_contract(role_job_id="job-001", carrier_profile_hash="a" * 64)
        contract2 = _make_contract(role_job_id="job-002", carrier_profile_hash="b" * 64)

        request1 = _make_dispatch_request(contract=contract1, input_view_bytes=b"same input")
        request2 = _make_dispatch_request(contract=contract2, input_view_bytes=b"same input")

        result1 = adapter.dispatch(request1)
        result2 = adapter.dispatch(request2)

        self.assertNotEqual(
            result1.receipt.output_artifact_hashes,
            result2.receipt.output_artifact_hashes,
        )

    def test_get_receipt_after_dispatch(self):
        """dispatch 后 get_receipt 返回相同 receipt。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        receipt = adapter.get_receipt(result.attempt_id)
        self.assertEqual(receipt.receipt_hash, result.receipt.receipt_hash)

    def test_adapter_implements_model_role_port(self):
        """FakeModelRoleAdapter 实现 ModelRolePort 协议。"""
        adapter = FakeModelRoleAdapter()
        self.assertIsInstance(adapter, ModelRolePort)

    def test_lifecycle_events_in_receipt(self):
        """receipt 包含完整生命周期事件。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        states = [e["state"] for e in result.receipt.lifecycle_events]
        self.assertIn(AttemptState.CREATED, states)
        self.assertIn(AttemptState.ACCEPTED, states)
        self.assertIn(AttemptState.STARTED, states)
        self.assertIn(AttemptState.COMPLETED, states)

    def test_usage_in_receipt(self):
        """receipt 包含 usage 信息。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        self.assertTrue(result.receipt.usage)
        self.assertIn("input_tokens", result.receipt.usage)
        self.assertIn("output_tokens", result.receipt.usage)


# ═══════════════════════════════════════════════════════════════════════
# Negative: FakeModelRoleAdapter
# ═══════════════════════════════════════════════════════════════════════


class TestFakeAdapterNegative(unittest.TestCase):
    """Negative: FakeModelRoleAdapter 异常情况。"""

    def test_unknown_role_dispatch_fails(self):
        """未知角色 dispatch 不 accepted。"""
        adapter = FakeModelRoleAdapter()
        contract = _make_contract(role_type_id="nonexistent_role")
        request = _make_dispatch_request(contract=contract)
        result = adapter.dispatch(request)

        self.assertFalse(result.accepted)
        self.assertNotEqual(result.attempt.state, AttemptState.COMPLETED)

    def test_force_wrong_sink(self):
        """敏感 sink 违规：output 写入错误 sink。"""
        adapter = FakeModelRoleAdapter(force_wrong_sink=True)
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        self.assertEqual(result.attempt.output_sink_kind, "EPHEMERAL_MODEL_OUTPUT")
        self.assertNotEqual(result.attempt.output_sink_kind, "RESTRICTED_VAULT")

    def test_force_skip_accepted_unknown_start(self):
        """跳过 ACCEPTED 直接 STARTED → unknown-start。"""
        adapter = FakeModelRoleAdapter(force_skip_accepted=True)
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        self.assertFalse(result.accepted)
        self.assertEqual(result.attempt.state, AttemptState.STARTED)
        # accepted_at 应该为空
        self.assertFalse(result.attempt.accepted_at)


# ═══════════════════════════════════════════════════════════════════════
# Fault: FakeModelRoleAdapter
# ═══════════════════════════════════════════════════════════════════════


class TestFakeAdapterFault(unittest.TestCase):
    """Fault injection: 超时、取消、reattach。"""

    def test_timeout(self):
        """attempt timeout。"""
        adapter = FakeModelRoleAdapter(force_timeout=True)
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        self.assertEqual(result.attempt.state, AttemptState.TIMED_OUT)
        self.assertEqual(result.receipt.terminal_reason, "TIMEOUT")
        self.assertTrue(result.receipt.is_terminal)

    def test_cancel_after_accepted(self):
        """ACCEPTED 后 cancel。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        # dispatch 已完成，不能 cancel（已终态）
        # 需要一个新的测试方式：直接测试 cancel 方法
        # 先创建一个可取消的 attempt
        from seven_system.cognitive.attempt import Attempt, AttemptState
        attempt = Attempt(
            attempt_id="cancel-test-001",
            role_job_id="job-cancel",
            role_type_id="question_architect",
            contract_hash=_ZERO_HASH,
            carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE",
            fence_token="fence-cancel",
            state=AttemptState.ACCEPTED,
        )
        adapter._attempts["cancel-test-001"] = attempt

        receipt = adapter.cancel("cancel-test-001", "fence-cancel")
        self.assertEqual(receipt.state, AttemptState.CANCELLED)
        self.assertEqual(receipt.terminal_reason, "CANCELLED")

    def test_cancel_with_wrong_fence_token(self):
        """错误 fence token cancel 失败。"""
        adapter = FakeModelRoleAdapter()
        attempt = Attempt(
            attempt_id="cancel-fence-001",
            role_job_id="job-fence",
            role_type_id="question_architect",
            contract_hash=_ZERO_HASH,
            carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE",
            fence_token="correct-fence",
            state=AttemptState.ACCEPTED,
        )
        adapter._attempts["cancel-fence-001"] = attempt

        receipt = adapter.cancel("cancel-fence-001", "wrong-fence")
        self.assertNotEqual(receipt.state, AttemptState.CANCELLED)
        self.assertIn("FENCE_TOKEN_MISMATCH", receipt.failure_or_quarantine_state)

    def test_cancel_already_terminal(self):
        """终态 attempt 不能 cancel。"""
        adapter = FakeModelRoleAdapter()
        attempt = Attempt(
            attempt_id="cancel-terminal-001",
            role_job_id="job-terminal",
            role_type_id="question_architect",
            contract_hash=_ZERO_HASH,
            carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE",
            fence_token="fence-terminal",
            state=AttemptState.COMPLETED,
            terminal_reason="COMPLETED",
        )
        adapter._attempts["cancel-terminal-001"] = attempt

        receipt = adapter.cancel("cancel-terminal-001", "fence-terminal")
        self.assertNotEqual(receipt.state, AttemptState.CANCELLED)
        self.assertIn("ALREADY_TERMINATED", receipt.failure_or_quarantine_state)

    def test_reattach_after_cancel_fails(self):
        """cancel 后 reattach 失败。"""
        adapter = FakeModelRoleAdapter()
        attempt = Attempt(
            attempt_id="reattach-cancel-001",
            role_job_id="job-reattach",
            role_type_id="question_architect",
            contract_hash=_ZERO_HASH,
            carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE",
            fence_token="fence-reattach",
            state=AttemptState.ACCEPTED,
        )
        adapter._attempts["reattach-cancel-001"] = attempt

        # 先 cancel
        adapter.cancel("reattach-cancel-001", "fence-reattach")

        # 再 reattach → 应该失败
        receipt = adapter.reattach("reattach-cancel-001", "fence-reattach")
        self.assertIn("ATTEMPT_CANCELLED", receipt.failure_or_quarantine_state)

    def test_reattach_with_wrong_fence(self):
        """错误 fence token reattach 失败。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request(fence_token="correct-fence")
        result = adapter.dispatch(request)

        receipt = adapter.reattach(result.attempt_id, "wrong-fence")
        self.assertIn("FENCE_TOKEN_MISMATCH", receipt.failure_or_quarantine_state)

    def test_reattach_nonexistent_attempt(self):
        """reattach 不存在的 attempt。"""
        adapter = FakeModelRoleAdapter()
        receipt = adapter.reattach("nonexistent-001", "any-fence")
        self.assertIn("ATTEMPT_NOT_FOUND", receipt.failure_or_quarantine_state)

    def test_get_receipt_nonexistent(self):
        """get_receipt 不存在的 attempt。"""
        adapter = FakeModelRoleAdapter()
        receipt = adapter.get_receipt("nonexistent-001")
        self.assertIn("ATTEMPT_NOT_FOUND", receipt.failure_or_quarantine_state)

    def test_force_unknown_start(self):
        """UNKNOWN_START_QUARANTINED 状态。"""
        adapter = FakeModelRoleAdapter(force_unknown_start=True)
        request = _make_dispatch_request()
        result = adapter.dispatch(request)

        self.assertEqual(result.attempt.state, AttemptState.UNKNOWN_START_QUARANTINED)
        self.assertIn("UNKNOWN_START", result.receipt.failure_or_quarantine_state)


# ═══════════════════════════════════════════════════════════════════════
# Golden: AttemptReconciler
# ═══════════════════════════════════════════════════════════════════════


class TestReconcilerGolden(unittest.TestCase):
    """Golden: AttemptReconciler 一致性检查。"""

    def test_consistent_attempt(self):
        """一致的 attempt → CONSISTENT。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request(fence_token="fence-001")
        result = adapter.dispatch(request)

        reconciler = AttemptReconciler()
        reconcile_result = reconciler.reconcile(
            result.attempt, result.receipt,
            expected_fence_token="fence-001",
        )
        self.assertEqual(reconcile_result.verdict, "CONSISTENT")
        self.assertTrue(reconcile_result.is_consistent)

    def test_reconcile_batch(self):
        """批量对账。"""
        adapter = FakeModelRoleAdapter()
        request1 = _make_dispatch_request(fence_token="fence-001")
        request2 = _make_dispatch_request(
            fence_token="fence-002",
            contract=_make_contract(role_job_id="job-002"),
        )
        result1 = adapter.dispatch(request1)
        result2 = adapter.dispatch(request2)

        reconciler = AttemptReconciler()
        results = reconciler.reconcile_batch(
            [(result1.attempt, result1.receipt), (result2.attempt, result2.receipt)],
            expected_fence_tokens={
                result1.attempt_id: "fence-001",
                result2.attempt_id: "fence-002",
            },
        )
        self.assertEqual(len(results), 2)
        for r in results:
            self.assertEqual(r.verdict, "CONSISTENT")


# ═══════════════════════════════════════════════════════════════════════
# Fault: AttemptReconciler identifies problems
# ═══════════════════════════════════════════════════════════════════════


class TestReconcilerFault(unittest.TestCase):
    """Fault: reconcile 识别 unknown-start / stale-fence / sensitive-sink / illegal-state。"""

    def test_identifies_unknown_start(self):
        """reconcile 识别 unknown-start。"""
        adapter = FakeModelRoleAdapter(force_skip_accepted=True)
        request = _make_dispatch_request(fence_token="fence-001")
        result = adapter.dispatch(request)

        reconciler = AttemptReconciler()
        reconcile_result = reconciler.reconcile(
            result.attempt, result.receipt,
            expected_fence_token="fence-001",
        )
        self.assertEqual(reconcile_result.verdict, "UNKNOWN_START")
        self.assertIn(EC.ATTEMPT_UNKNOWN_START, reconcile_result.error_codes)

    def test_identifies_stale_fence(self):
        """reconcile 识别 stale-fence。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request(fence_token="correct-fence")
        result = adapter.dispatch(request)

        reconciler = AttemptReconciler()
        reconcile_result = reconciler.reconcile(
            result.attempt, result.receipt,
            expected_fence_token="wrong-fence",  # 不匹配
        )
        self.assertEqual(reconcile_result.verdict, "STALE_FENCE")
        self.assertIn(EC.ATTEMPT_STALE_FENCE, reconcile_result.error_codes)

    def test_identifies_sensitive_sink(self):
        """reconcile 识别 sensitive-sink。"""
        adapter = FakeModelRoleAdapter(force_wrong_sink=True)
        request = _make_dispatch_request(fence_token="fence-001")
        result = adapter.dispatch(request)

        reconciler = AttemptReconciler()
        reconcile_result = reconciler.reconcile(
            result.attempt, result.receipt,
            expected_fence_token="fence-001",
        )
        self.assertEqual(reconcile_result.verdict, "SENSITIVE_SINK")
        self.assertIn(EC.ATTEMPT_SENSITIVE_SINK, reconcile_result.error_codes)

    def test_identifies_illegal_state(self):
        """reconcile 识别 illegal-state。"""
        # 构造一个非法状态转换的 attempt
        attempt = Attempt(
            attempt_id="illegal-001",
            role_job_id="job-illegal",
            role_type_id="question_architect",
            contract_hash=_ZERO_HASH,
            carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE",
            fence_token="fence-001",
            state=AttemptState.COMPLETED,
            output_artifact_hashes=[_ZERO_HASH],
            output_sink_ref="sink-001",
            output_sink_kind="RESTRICTED_VAULT",
            terminal_reason="COMPLETED",
        )
        # 构造一个有非法 lifecycle 的 receipt
        receipt = build_attempt_receipt(
            attempt=attempt,
            requested_model_uid="fake",
            effective_model_uid="fake",
        )
        # 篡改 lifecycle_events：CREATED → COMPLETED（跳过 ACCEPTED 和 STARTED）
        d = receipt.to_dict()
        d["lifecycle_events"] = [
            {"state": "CREATED", "timestamp": "t1"},
            {"state": "COMPLETED", "timestamp": "t2"},
        ]
        # 重新计算 hash
        obj_for_hash = dict(d)
        obj_for_hash["receipt_hash"] = None
        d["receipt_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()

        reconciler = AttemptReconciler()
        reconcile_result = reconciler.reconcile(
            attempt, d,
            expected_fence_token="fence-001",
        )
        self.assertEqual(reconcile_result.verdict, "ILLEGAL_STATE")
        self.assertIn(EC.ATTEMPT_ILLEGAL_STATE_TRANSITION, reconcile_result.error_codes)

    def test_state_mismatch_identified(self):
        """reconcile 识别 attempt 和 receipt 状态不一致。"""
        attempt = Attempt(
            attempt_id="mismatch-001",
            role_job_id="job-mismatch",
            role_type_id="question_architect",
            contract_hash=_ZERO_HASH,
            carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE",
            fence_token="fence-001",
            state=AttemptState.STARTED,
            accepted_at="t1",  # 有 accepted_at 避免 unknown-start 误判
        )
        # receipt 状态与 attempt 不同
        receipt_attempt = Attempt(
            attempt_id="mismatch-001",
            role_job_id="job-mismatch",
            role_type_id="question_architect",
            contract_hash=_ZERO_HASH,
            carrier_profile_hash=_ZERO_HASH,
            adapter_kind="FAKE",
            fence_token="fence-001",
            state=AttemptState.COMPLETED,
            accepted_at="t1",  # 设置 accepted_at 使 lifecycle 包含 ACCEPTED
            started_at="t2",
            completed_at="t3",
            output_artifact_hashes=[_ZERO_HASH],
            output_sink_ref="sink-001",
            output_sink_kind="RESTRICTED_VAULT",
            terminal_reason="COMPLETED",
        )
        receipt = build_attempt_receipt(attempt=receipt_attempt)

        reconciler = AttemptReconciler()
        result = reconciler.reconcile(attempt, receipt, expected_fence_token="fence-001")
        # 状态不一致 → ILLEGAL_STATE (优先级高于其他)
        self.assertEqual(result.verdict, "ILLEGAL_STATE")

    def test_reconcile_result_to_dict(self):
        """ReconcileResult.to_dict 格式正确。"""
        result = ReconcileResult(
            verdict="CONSISTENT",
            attempt_id="a-001",
            error_codes=[],
            details=[],
        )
        d = result.to_dict()
        self.assertEqual(d["verdict"], "CONSISTENT")
        self.assertEqual(d["attempt_id"], "a-001")
        self.assertTrue(d["is_consistent"] if "is_consistent" in d else True)


# ═══════════════════════════════════════════════════════════════════════
# Integration: full dispatch → reconcile
# ═══════════════════════════════════════════════════════════════════════


class TestIntegrationDispatchReconcile(unittest.TestCase):
    """Integration: 完整 dispatch → receipt → reconcile 链。"""

    def test_full_golden_path(self):
        """完整 golden path：dispatch → receipt 验证 → reconcile CONSISTENT。"""
        adapter = FakeModelRoleAdapter()
        request = _make_dispatch_request(fence_token="fence-001")
        dispatch_result = adapter.dispatch(request)

        # 1. dispatch 成功
        self.assertTrue(dispatch_result.accepted)
        self.assertEqual(dispatch_result.attempt.state, AttemptState.COMPLETED)

        # 2. receipt 验证
        receipt_result = verify_attempt_receipt(dispatch_result.receipt)
        self.assertTrue(receipt_result.passed)

        # 3. reconcile 一致
        reconciler = AttemptReconciler()
        reconcile_result = reconciler.reconcile(
            dispatch_result.attempt,
            dispatch_result.receipt,
            expected_fence_token="fence-001",
        )
        self.assertEqual(reconcile_result.verdict, "CONSISTENT")

    def test_multiple_roles_dispatch(self):
        """多个角色 dispatch 都成功。"""
        adapter = FakeModelRoleAdapter()

        for role_id in ("question_architect", "math_verifier", "adjudicator"):
            contract = _make_contract(role_type_id=role_id, role_job_id=f"job-{role_id}")
            request = _make_dispatch_request(
                contract=contract,
                fence_token=f"fence-{role_id}",
            )
            result = adapter.dispatch(request)
            self.assertTrue(result.accepted, f"dispatch failed for {role_id}")
            self.assertEqual(result.attempt.state, AttemptState.COMPLETED)

    def test_dispatch_summary(self):
        """DispatchRequest.to_summary 格式正确。"""
        request = _make_dispatch_request()
        summary = request.to_summary()
        self.assertEqual(summary["role_type_id"], "question_architect")
        self.assertEqual(summary["adapter_kind"], "FAKE")
        self.assertEqual(summary["input_view_id"], "view-001")
        self.assertEqual(summary["sink_id"], "sink-001")


# ═══════════════════════════════════════════════════════════════════════
# Constants verification
# ═══════════════════════════════════════════════════════════════════════


class TestConstants(unittest.TestCase):
    """验证 CW0 常量。"""

    def test_attempt_states_complete(self):
        """ATTEMPT_STATES 包含所有状态。"""
        expected = {
            "CREATED", "ACCEPTED", "STARTED", "COMPLETED",
            "TERMINATED", "CANCELLED", "TIMED_OUT", "UNKNOWN_START_QUARANTINED",
        }
        self.assertEqual(set(ATTEMPT_STATES), expected)

    def test_attempt_terminal_states(self):
        """ATTEMPT_TERMINAL_STATES 正确。"""
        expected = {"COMPLETED", "TERMINATED", "CANCELLED", "TIMED_OUT"}
        self.assertEqual(set(ATTEMPT_TERMINAL_STATES), expected)

    def test_attempt_transitions_created_only_to_accepted(self):
        """CREATED 只能转到 ACCEPTED。"""
        allowed = ATTEMPT_TRANSITIONS["CREATED"]
        self.assertEqual(allowed, frozenset({"ACCEPTED"}))

    def test_attempt_transitions_accepted(self):
        """ACCEPTED 可以转到 STARTED / CANCELLED / TIMED_OUT / UNKNOWN_START_QUARANTINED。"""
        allowed = ATTEMPT_TRANSITIONS["ACCEPTED"]
        self.assertEqual(allowed, frozenset({"STARTED", "CANCELLED", "TIMED_OUT", "UNKNOWN_START_QUARANTINED"}))

    def test_attempt_transitions_started(self):
        """STARTED 可以转到 COMPLETED / TERMINATED / CANCELLED / TIMED_OUT。"""
        allowed = ATTEMPT_TRANSITIONS["STARTED"]
        self.assertEqual(allowed, frozenset({"COMPLETED", "TERMINATED", "CANCELLED", "TIMED_OUT"}))

    def test_terminal_states_have_no_transitions(self):
        """终态没有后续转换。"""
        for state in ATTEMPT_TERMINAL_STATES:
            self.assertEqual(ATTEMPT_TRANSITIONS[state], frozenset(),
                             f"terminal state {state} should have no transitions")


if __name__ == "__main__":
    unittest.main()
