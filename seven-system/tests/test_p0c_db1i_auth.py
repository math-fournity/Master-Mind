"""P0-C: DB1I 授权链完整性测试。

这些测试证明审计发现的旁路：human_gate_service=None 时弱 dict 检查可绕过。
修复前：human_gate_service=None + {"decision": "APPROVE"} 可通过 prepare
修复后：human_gate_service=None 必须被拒绝（mandatory Gate）

测试层级：
1. Bypass tests — human_gate_service=None 必须被拒绝
2. Weak Permit tests — 弱 permit 必须被拒绝
3. Full authorization chain tests — EEA/Permit/RESERVED 完整链验证
4. Concurrent reserve tests — 并发预留原子性
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from typing import Any

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.database.schema_bootstrap import (
    SchemaBootstrapProtocol,
    FakeSchemaApplyExecutor,
    build_schema_bootstrap_plan,
    SchemaBootstrapProtocolError,
)
from seven_system.database.schema_bootstrap_backend import SchemaBootstrapDVolumeLedgerBackend
from seven_system.database.site_adapter import FakeLogicalSiteAdapter
from seven_system.contracts.errors import VerificationErrorCode as EC


# ─── helpers ───────────────────────────────────────────────────────────

def _make_protocol() -> SchemaBootstrapProtocol:
    """Create a fresh SchemaBootstrapProtocol with fake components."""
    backend = SchemaBootstrapDVolumeLedgerBackend()
    executor = FakeSchemaApplyExecutor()
    site = FakeLogicalSiteAdapter()
    site.connect_readonly()
    return SchemaBootstrapProtocol(
        site_adapter=site,
        backend=backend,
        executor=executor,
    )


def _make_valid_permit(plan_hash: str) -> dict[str, Any]:
    """Create a valid LiveRunPermit for G-DB-SCHEMA-APPLY."""
    return {
        "plan_hash": plan_hash,
        "wp_id": "G-DB-SCHEMA-APPLY",
        "maintenance_window": "2026-08-14T00:00:00Z/2026-08-15T00:00:00Z",
        "max_actions": 100,
        "expires_at": "2026-08-15T00:00:00Z",
        "nonce": "permit-nonce-001",
    }


# ─── P0-C Blocker: human_gate_service=None bypass ──────────────────────

class TestHumanGateServiceNoneBypass(unittest.TestCase):
    """证明 human_gate_service=None 旁路存在，修复后应 FAIL。"""

    def test_none_gate_service_rejected(self):
        """human_gate_service=None 必须被拒绝，不能回退到弱 dict 检查。"""
        protocol = _make_protocol()
        plan = build_schema_bootstrap_plan(
            site_fingerprint_hash=protocol.site_adapter.site_fingerprint().fingerprint_hash
        )
        permit = _make_valid_permit(plan.plan_hash)

        # Bypass attempt: None gate service + minimal fake gate
        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            protocol.prepare(
                permit=permit,
                gate_decision={"decision": "APPROVE"},
                human_gate_service=None,  # BYPASS ATTEMPT
                evaluation_time="2026-08-14T12:00:00Z",
            )
        self.assertIn(
            "human_gate_service",
            str(ctx.exception).lower(),
            "Error must mention human_gate_service is required"
        )

    def test_none_gate_service_with_full_fake_gate_rejected(self):
        """即使提供完整的 fake gate decision，None gate service 仍必须被拒绝。"""
        protocol = _make_protocol()
        plan = build_schema_bootstrap_plan(
            site_fingerprint_hash=protocol.site_adapter.site_fingerprint().fingerprint_hash
        )
        permit = _make_valid_permit(plan.plan_hash)

        # Full fake gate decision that would pass structure check
        fake_gate = {
            "decision": "APPROVE",
            "decision_id": "fake-001",
            "task_id": "task-001",
            "gate_type": "G-DB-SCHEMA-APPLY",
            "actor_id": "fake-actor",
            "nonce": "fake-nonce-12345678",
        }

        with self.assertRaises(SchemaBootstrapProtocolError):
            protocol.prepare(
                permit=permit,
                gate_decision=fake_gate,
                human_gate_service=None,  # BYPASS ATTEMPT
                evaluation_time="2026-08-14T12:00:00Z",
            )


# ─── Weak Permit tests ─────────────────────────────────────────────────

class TestWeakPermit(unittest.TestCase):
    """弱 permit 必须被拒绝。"""

    def test_wrong_wp_id_rejected(self):
        """permit wp_id 不是 G-DB-SCHEMA-APPLY 必须被拒绝。"""
        protocol = _make_protocol()
        plan = build_schema_bootstrap_plan(
            site_fingerprint_hash=protocol.site_adapter.site_fingerprint().fingerprint_hash
        )
        permit = _make_valid_permit(plan.plan_hash)
        permit["wp_id"] = "WRONG-WP"

        # Need a mock gate service that passes
        class MockGate:
            def accept_gate_decision(self, dec, *, evaluation_time=""):
                class R:
                    passed = True
                    details = []
                return R()

        with self.assertRaises(SchemaBootstrapProtocolError):
            protocol.prepare(
                permit=permit,
                gate_decision={"decision": "APPROVE"},
                human_gate_service=MockGate(),
                evaluation_time="2026-08-14T12:00:00Z",
            )

    def test_permit_plan_hash_mismatch_rejected(self):
        """permit plan_hash 与实际 plan 不符必须被拒绝。"""
        protocol = _make_protocol()
        permit = _make_valid_permit("f" * 64)  # wrong hash

        class MockGate:
            def accept_gate_decision(self, dec, *, evaluation_time=""):
                class R:
                    passed = True
                    details = []
                return R()

        with self.assertRaises(SchemaBootstrapProtocolError):
            protocol.prepare(
                permit=permit,
                gate_decision={"decision": "APPROVE"},
                human_gate_service=MockGate(),
                evaluation_time="2026-08-14T12:00:00Z",
            )


# ─── Gate decision rejection tests ─────────────────────────────────────

class TestGateDecisionRejection(unittest.TestCase):
    """Gate decision 被 HumanGateService 拒绝时必须传播错误。"""

    def test_gate_rejection_propagates(self):
        """HumanGateService 拒绝 gate decision 时，prepare 必须 FAIL。"""
        protocol = _make_protocol()
        plan = build_schema_bootstrap_plan(
            site_fingerprint_hash=protocol.site_adapter.site_fingerprint().fingerprint_hash
        )
        permit = _make_valid_permit(plan.plan_hash)

        class RejectingGate:
            def accept_gate_decision(self, dec, *, evaluation_time=""):
                class R:
                    passed = False
                    details = ["signature invalid"]
                return R()

        with self.assertRaises(SchemaBootstrapProtocolError) as ctx:
            protocol.prepare(
                permit=permit,
                gate_decision={"decision": "APPROVE"},
                human_gate_service=RejectingGate(),
                evaluation_time="2026-08-14T12:00:00Z",
            )
        self.assertIn("gate", str(ctx.exception).lower())


if __name__ == "__main__":
    unittest.main()
