"""R6: AdapterRegistry — 默认禁用的副作用端口测试。

这些测试证明所有副作用端口默认禁用，未授权调用 fail-closed。
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.operations.adapter_registry import AdapterRegistry, SIDE_EFFECT_PORTS
from seven_system.contracts.errors import VerificationErrorCode as EC


class TestAdapterRegistryDefaultDisabled(unittest.TestCase):
    """所有副作用端口默认禁用。"""

    def test_all_ports_disabled_by_default(self):
        """新建 registry 时所有端口默认禁用。"""
        registry = AdapterRegistry()
        self.assertTrue(registry.all_disabled())
        for port_id in SIDE_EFFECT_PORTS:
            self.assertFalse(registry.is_enabled(port_id), f"{port_id} should be disabled by default")

    def test_disabled_port_check_fails(self):
        """禁用端口的 check_enabled 返回错误。"""
        registry = AdapterRegistry()
        for port_id in SIDE_EFFECT_PORTS:
            ok, errors, details = registry.check_enabled(port_id)
            self.assertFalse(ok, f"{port_id} should fail check when disabled")
            self.assertIn(EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED, errors)

    def test_enable_requires_authorization(self):
        """启用端口需要 authorization_ref。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.enable("VLT0_CAS", authorization_ref="")
        self.assertFalse(ok)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, errors)

    def test_enable_with_authorization_succeeds(self):
        """有 authorization_ref 时启用成功。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.enable(
            "VLT0_CAS", authorization_ref="auth-001"
        )
        self.assertTrue(ok, f"enable should succeed: {details}")
        self.assertTrue(registry.is_enabled("VLT0_CAS"))

    def test_enabled_port_check_passes(self):
        """启用端口的 check_enabled 通过。"""
        registry = AdapterRegistry()
        registry.enable("VLT0_CAS", authorization_ref="auth-001")
        ok, errors, details = registry.check_enabled("VLT0_CAS")
        self.assertTrue(ok)

    def test_disable_after_enable(self):
        """禁用已启用的端口。"""
        registry = AdapterRegistry()
        registry.enable("VLT0_CAS", authorization_ref="auth-001")
        ok, _, _ = registry.disable("VLT0_CAS")
        self.assertTrue(ok)
        self.assertFalse(registry.is_enabled("VLT0_CAS"))


class TestAllSideEffectPorts(unittest.TestCase):
    """所有 6 个副作用端口都被管理。"""

    def test_all_6_ports_present(self):
        """注册表管理所有 6 个副作用端口。"""
        expected = {
            "VLT0_CAS",
            "DB_ARANGO",
            "RT_REDIS",
            "SOLVER_HARNESS",
            "MODEL_ROLE_CODEX",
            "MODEL_ROLE_DEVIN",
        }
        self.assertEqual(SIDE_EFFECT_PORTS, expected)

    def test_all_ports_default_disabled(self):
        """所有 6 个端口默认禁用。"""
        registry = AdapterRegistry()
        for port_id in SIDE_EFFECT_PORTS:
            ok, errors, details = registry.check_enabled(port_id)
            self.assertFalse(ok, f"{port_id} should be disabled by default")

    def test_unknown_port_rejected(self):
        """未知端口被拒绝。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.check_enabled("UNKNOWN_PORT")
        self.assertFalse(ok)
        self.assertIn(EC.WP_UNKNOWN, errors)

    def test_enable_unknown_port_rejected(self):
        """启用未知端口被拒绝。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.enable("UNKNOWN_PORT", authorization_ref="auth")
        self.assertFalse(ok)
        self.assertIn(EC.WP_UNKNOWN, errors)


class TestFailClosedOnDisabled(unittest.TestCase):
    """禁用状态下调用 fail-closed。"""

    def test_vlt0_cas_fail_closed(self):
        """VLT0 CAS 禁用时 fail-closed。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.check_enabled("VLT0_CAS")
        self.assertFalse(ok)
        self.assertIn("DISABLED", details[0])

    def test_db_arango_fail_closed(self):
        """DB Arango 禁用时 fail-closed。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.check_enabled("DB_ARANGO")
        self.assertFalse(ok)

    def test_rt_redis_fail_closed(self):
        """RT Redis 禁用时 fail-closed。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.check_enabled("RT_REDIS")
        self.assertFalse(ok)

    def test_solver_harness_fail_closed(self):
        """Solver harness 禁用时 fail-closed。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.check_enabled("SOLVER_HARNESS")
        self.assertFalse(ok)

    def test_model_role_codex_fail_closed(self):
        """ModelRole Codex 禁用时 fail-closed。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.check_enabled("MODEL_ROLE_CODEX")
        self.assertFalse(ok)

    def test_model_role_devin_fail_closed(self):
        """ModelRole Devin 禁用时 fail-closed。"""
        registry = AdapterRegistry()
        ok, errors, details = registry.check_enabled("MODEL_ROLE_DEVIN")
        self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main()
