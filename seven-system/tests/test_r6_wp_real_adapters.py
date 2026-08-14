"""R6 深度补全 + 第 7 节 WP 真实但禁用 adapter 测试。

测试每个 WP 的真实 adapter 代码路径：
- 默认禁用——通过 AdapterRegistry.check_enabled 检查
- 禁用时 execute fail-closed
- 启用后执行真实代码路径
- 真实代码路径包含完整的连接、调用、错误处理逻辑
"""

import unittest

from seven_system.operations.adapter_registry import AdapterRegistry, SIDE_EFFECT_PORTS
from seven_system.operations.wp_real_adapters import (
    VLT0DCasAdapter, HG0ReplayableComponent, DB1LReadOnlyAdapter,
    DB1ISchemaApplyAdapter, RT1RedisProjectionAdapter,
    CWD1DevinCliAdapter, CWC1CodexAdapter, SV1DevinSolverAdapter,
)


class TestVLT0DCasAdapter(unittest.TestCase):
    """WP-VLT0: D 盘 root-bound CAS 真实 adapter。"""

    def test_disabled_by_default(self):
        """默认禁用——execute fail-closed。"""
        registry = AdapterRegistry()
        adapter = VLT0DCasAdapter()
        result = adapter.execute(registry, "write_artifact", artifact_id="a1", content=b"test")
        self.assertFalse(result["ok"])

    def test_enabled_write_and_read(self):
        """启用后可写入和读取。"""
        registry = AdapterRegistry()
        registry.enable("VLT0_CAS", authorization_ref="auth-001")
        adapter = VLT0DCasAdapter()
        result = adapter.execute(registry, "write_artifact", artifact_id="a1", content=b"test")
        self.assertTrue(result["ok"])
        self.assertIn("cas_hash", result)
        self.assertIn("opaque_id", result)

        read_result = adapter.execute(registry, "read_artifact", artifact_id="a1")
        self.assertTrue(read_result["ok"])
        self.assertEqual(read_result["content"], b"test")

    def test_symlink_path_rejected(self):
        """symlink 路径被拒绝。"""
        registry = AdapterRegistry()
        registry.enable("VLT0_CAS", authorization_ref="auth-001")
        adapter = VLT0DCasAdapter()
        result = adapter.execute(registry, "write_artifact", artifact_id="../symlink-evil", content=b"test")
        self.assertFalse(result["ok"])

    def test_seal_artifact(self):
        """seal artifact 状态转换。"""
        registry = AdapterRegistry()
        registry.enable("VLT0_CAS", authorization_ref="auth-001")
        adapter = VLT0DCasAdapter()
        adapter.execute(registry, "write_artifact", artifact_id="a1", content=b"test")
        adapter.execute(registry, "partial_artifact", artifact_id="a1")
        result = adapter.execute(registry, "seal_artifact", artifact_id="a1")
        self.assertTrue(result["ok"])
        self.assertEqual(result["state"], "sealed")


class TestHG0ReplayableComponent(unittest.TestCase):
    """WP-HG0: 完整可重放 HumanGate 组件。"""

    def test_create_task_without_auth(self):
        """create_task 不需要 HumanGate 授权。"""
        component = HG0ReplayableComponent()
        result = component.execute(None, "create_task", task_id="t1", gate_type="PROOF_REVIEW")
        self.assertTrue(result["ok"])

    def test_append_decision_without_auth_rejected(self):
        """append_decision 没有 HumanGate 授权时被拒绝。"""
        component = HG0ReplayableComponent()
        result = component.execute(None, "append_decision", decision={"decision_id": "d1"})
        self.assertFalse(result["ok"])

    def test_append_decision_with_auth(self):
        """append_decision 有 HumanGate 授权时通过。"""
        component = HG0ReplayableComponent()
        component.authorize({"decision": "APPROVE", "verification_status": "VERIFIED"})
        result = component.execute(None, "append_decision", decision={"decision_id": "d1"})
        self.assertTrue(result["ok"])

    def test_append_only_no_duplicate(self):
        """append-only: 重复 decision_id 被拒绝。"""
        component = HG0ReplayableComponent()
        component.authorize({"decision": "APPROVE", "verification_status": "VERIFIED"})
        component.execute(None, "append_decision", decision={"decision_id": "d1"})
        result = component.execute(None, "append_decision", decision={"decision_id": "d1"})
        self.assertFalse(result["ok"])

    def test_replay_chain(self):
        """replay_chain 返回完整决策链。"""
        component = HG0ReplayableComponent()
        component.authorize({"decision": "APPROVE", "verification_status": "VERIFIED"})
        component.execute(None, "append_decision", decision={"decision_id": "d1"})
        component.execute(None, "append_decision", decision={"decision_id": "d2"})
        result = component.execute(None, "replay_chain")
        self.assertTrue(result["ok"])
        self.assertEqual(len(result["chain"]), 2)


class TestDB1LReadOnlyAdapter(unittest.TestCase):
    """WP-DB1L: 只读 StrictDatabasePort。"""

    def test_disabled_by_default(self):
        """默认禁用。"""
        registry = AdapterRegistry()
        adapter = DB1LReadOnlyAdapter()
        result = adapter.execute(registry, "read_site_identity")
        self.assertFalse(result["ok"])

    def test_read_enabled(self):
        """启用后可读取。"""
        registry = AdapterRegistry()
        registry.enable("DB_ARANGO", authorization_ref="auth-001")
        adapter = DB1LReadOnlyAdapter()
        result = adapter.execute(registry, "read_site_identity")
        self.assertTrue(result["ok"])
        self.assertIn("site", result)

    def test_write_rejected(self):
        """写操作被拒绝——DB1L 是只读的。"""
        registry = AdapterRegistry()
        registry.enable("DB_ARANGO", authorization_ref="auth-001")
        adapter = DB1LReadOnlyAdapter()
        result = adapter.execute(registry, "write_collection", collection="test")
        self.assertFalse(result["ok"])


class TestDB1ISchemaApplyAdapter(unittest.TestCase):
    """WP-DB1I: deterministic plan/apply/readback/reconcile。"""

    def test_disabled_by_default(self):
        """默认禁用。"""
        registry = AdapterRegistry()
        adapter = DB1ISchemaApplyAdapter()
        result = adapter.execute(registry, "apply_schema_action", action_id="a1")
        self.assertFalse(result["ok"])

    def test_apply_schema_action(self):
        """启用后可 apply schema action。"""
        registry = AdapterRegistry()
        registry.enable("DB_ARANGO", authorization_ref="auth-001")
        adapter = DB1ISchemaApplyAdapter()
        result = adapter.execute(registry, "apply_schema_action",
                                 action_id="a1", ordinal=0, fence_token=1,
                                 pre_state_catalog_hash="0" * 64)
        self.assertTrue(result["ok"])
        self.assertEqual(result["terminal_state"], "COMMITTED")

    def test_duplicate_ordinal_rejected(self):
        """重复 ordinal 被拒绝。"""
        registry = AdapterRegistry()
        registry.enable("DB_ARANGO", authorization_ref="auth-001")
        adapter = DB1ISchemaApplyAdapter()
        adapter.execute(registry, "apply_schema_action",
                        action_id="a1", ordinal=0, fence_token=1,
                        pre_state_catalog_hash="0" * 64)
        result = adapter.execute(registry, "apply_schema_action",
                                 action_id="a2", ordinal=0, fence_token=2,
                                 pre_state_catalog_hash="0" * 64)
        self.assertFalse(result["ok"])

    def test_reconcile(self):
        """reconcile 返回统计信息。"""
        registry = AdapterRegistry()
        registry.enable("DB_ARANGO", authorization_ref="auth-001")
        adapter = DB1ISchemaApplyAdapter()
        adapter.execute(registry, "apply_schema_action",
                        action_id="a1", ordinal=0, fence_token=1,
                        pre_state_catalog_hash="0" * 64)
        result = adapter.execute(registry, "reconcile")
        self.assertTrue(result["ok"])
        self.assertEqual(result["total_actions"], 1)


class TestRT1RedisProjectionAdapter(unittest.TestCase):
    """WP-RT1: Redis 投影 + WorkEvent + lease/fence。"""

    def test_disabled_by_default(self):
        """默认禁用。"""
        registry = AdapterRegistry()
        adapter = RT1RedisProjectionAdapter()
        result = adapter.execute(registry, "set", key="k1", value="v1")
        self.assertFalse(result["ok"])

    def test_set_and_get(self):
        """启用后可 set 和 get。"""
        registry = AdapterRegistry()
        registry.enable("RT_REDIS", authorization_ref="auth-001")
        adapter = RT1RedisProjectionAdapter()
        adapter.execute(registry, "set", key="k1", value="v1")
        result = adapter.execute(registry, "get", key="k1")
        self.assertTrue(result["ok"])
        self.assertEqual(result["value"], "v1")

    def test_acquire_lease(self):
        """acquire lease with fence token。"""
        registry = AdapterRegistry()
        registry.enable("RT_REDIS", authorization_ref="auth-001")
        adapter = RT1RedisProjectionAdapter()
        result = adapter.execute(registry, "acquire_lease", lease_id="l1", fence_token=1)
        self.assertTrue(result["ok"])

    def test_duplicate_lease_rejected(self):
        """重复 lease 被拒绝。"""
        registry = AdapterRegistry()
        registry.enable("RT_REDIS", authorization_ref="auth-001")
        adapter = RT1RedisProjectionAdapter()
        adapter.execute(registry, "acquire_lease", lease_id="l1", fence_token=1)
        result = adapter.execute(registry, "acquire_lease", lease_id="l1", fence_token=2)
        self.assertFalse(result["ok"])

    def test_reconstruct_projection(self):
        """reconstruct projection from KV store。"""
        registry = AdapterRegistry()
        registry.enable("RT_REDIS", authorization_ref="auth-001")
        adapter = RT1RedisProjectionAdapter()
        adapter.execute(registry, "set", key="k1", value="v1")
        result = adapter.execute(registry, "reconstruct_projection")
        self.assertTrue(result["ok"])
        self.assertEqual(result["kv_store"]["k1"], "v1")


class TestCWD1DevinCliAdapter(unittest.TestCase):
    """WP-CW-D1: DevinCliModelRoleAdapter。"""

    def test_disabled_by_default(self):
        """默认禁用。"""
        registry = AdapterRegistry()
        adapter = CWD1DevinCliAdapter()
        result = adapter.execute(registry, "invoke", prompt="test")
        self.assertFalse(result["ok"])

    def test_invoke_with_prompt(self):
        """启用后可 invoke。"""
        registry = AdapterRegistry()
        registry.enable("MODEL_ROLE_DEVIN", authorization_ref="auth-001")
        adapter = CWD1DevinCliAdapter()
        result = adapter.execute(registry, "invoke", prompt="test")
        self.assertTrue(result["ok"])
        self.assertEqual(result["model_uid"], "glm-5-2")
        self.assertEqual(result["session"], "fresh")

    def test_solver_harness_rejected(self):
        """prompt 中包含 solver_harness 被拒绝。"""
        registry = AdapterRegistry()
        registry.enable("MODEL_ROLE_DEVIN", authorization_ref="auth-001")
        adapter = CWD1DevinCliAdapter()
        result = adapter.execute(registry, "invoke", prompt="call solver_harness")
        self.assertFalse(result["ok"])


class TestCWC1CodexAdapter(unittest.TestCase):
    """WP-CW-C1: Codex adapter。"""

    def test_disabled_by_default(self):
        """默认禁用。"""
        registry = AdapterRegistry()
        adapter = CWC1CodexAdapter()
        result = adapter.execute(registry, "invoke", prompt="test")
        self.assertFalse(result["ok"])

    def test_invoke_with_prompt(self):
        """启用后可 invoke。"""
        registry = AdapterRegistry()
        registry.enable("MODEL_ROLE_CODEX", authorization_ref="auth-001")
        adapter = CWC1CodexAdapter()
        result = adapter.execute(registry, "invoke", prompt="test")
        self.assertTrue(result["ok"])
        self.assertEqual(result["model"], "gpt-5.6-sol")
        self.assertEqual(result["effort"], "high")


class TestSV1DevinSolverAdapter(unittest.TestCase):
    """WP-SV1: DevinSolverAdapter。"""

    def test_disabled_by_default(self):
        """默认禁用——launch_count 必须为 0。"""
        registry = AdapterRegistry()
        adapter = SV1DevinSolverAdapter()
        result = adapter.execute(registry, "launch_solver", problem_id="p1")
        self.assertFalse(result["ok"])
        self.assertEqual(adapter._launch_count, 0)

    def test_launch_solver(self):
        """启用后可 launch solver。"""
        registry = AdapterRegistry()
        registry.enable("SOLVER_HARNESS", authorization_ref="auth-001")
        adapter = SV1DevinSolverAdapter()
        result = adapter.execute(registry, "launch_solver", problem_id="p1")
        self.assertTrue(result["ok"])
        self.assertEqual(adapter._launch_count, 1)

    def test_trajectory_missing_invalid(self):
        """trajectory.jsonl 缺失 → invalid。"""
        registry = AdapterRegistry()
        registry.enable("SOLVER_HARNESS", authorization_ref="auth-001")
        adapter = SV1DevinSolverAdapter()
        launch_result = adapter.execute(registry, "launch_solver", problem_id="p1")
        session_id = launch_result["session_id"]
        result = adapter.execute(registry, "get_trajectory", session_id=session_id)
        self.assertFalse(result["ok"])

    def test_no_tool_check_pass(self):
        """no_tool 检查通过（无 tool event）。"""
        registry = AdapterRegistry()
        registry.enable("SOLVER_HARNESS", authorization_ref="auth-001")
        adapter = SV1DevinSolverAdapter()
        launch_result = adapter.execute(registry, "launch_solver", problem_id="p1")
        session_id = launch_result["session_id"]
        # 手动添加非 tool trajectory
        adapter._sessions[session_id]["trajectory"] = [{"type": "thinking", "content": "..."}]
        result = adapter.execute(registry, "check_no_tool", session_id=session_id)
        self.assertTrue(result["ok"])

    def test_no_tool_check_fail(self):
        """no_tool 检查失败（有 tool event）。"""
        registry = AdapterRegistry()
        registry.enable("SOLVER_HARNESS", authorization_ref="auth-001")
        adapter = SV1DevinSolverAdapter()
        launch_result = adapter.execute(registry, "launch_solver", problem_id="p1")
        session_id = launch_result["session_id"]
        # 手动添加 tool trajectory
        adapter._sessions[session_id]["trajectory"] = [{"type": "tool_use", "tool": "bash"}]
        result = adapter.execute(registry, "check_no_tool", session_id=session_id)
        self.assertFalse(result["ok"])


class TestAllAdaptersFailClosed(unittest.TestCase):
    """所有 adapter 默认 fail-closed。"""

    def test_all_side_effect_adapters_disabled_by_default(self):
        """所有 SIDE_EFFECT adapter 默认禁用。"""
        registry = AdapterRegistry()
        adapters = [
            (VLT0DCasAdapter(), "VLT0_CAS", "write_artifact"),
            (DB1LReadOnlyAdapter(), "DB_ARANGO", "read_site_identity"),
            (DB1ISchemaApplyAdapter(), "DB_ARANGO", "apply_schema_action"),
            (RT1RedisProjectionAdapter(), "RT_REDIS", "set"),
            (CWD1DevinCliAdapter(), "MODEL_ROLE_DEVIN", "invoke"),
            (CWC1CodexAdapter(), "MODEL_ROLE_CODEX", "invoke"),
            (SV1DevinSolverAdapter(), "SOLVER_HARNESS", "launch_solver"),
        ]
        for adapter, port_id, op in adapters:
            result = adapter.execute(registry, op)
            self.assertFalse(result["ok"], f"{port_id} should be disabled by default")


if __name__ == "__main__":
    unittest.main()
