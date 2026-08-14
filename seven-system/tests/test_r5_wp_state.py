"""R5: WorkPackageStateService — DAG 依赖强制执行测试。

这些测试证明 22 个工作包不能越级 start（development dependency 未满足）。
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.operations.work_package_state import WorkPackageStateService
from seven_system.contracts.errors import VerificationErrorCode as EC


DAG_PATH = SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"


class TestWorkPackageStateService(unittest.TestCase):
    """WorkPackageStateService 基本功能测试。"""

    def test_wp_doc0_can_start_no_deps(self):
        """WP-DOC0 没有 development dependencies，可以直接 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        ok, errors, details = service.can_start("WP-DOC0")
        self.assertTrue(ok, f"WP-DOC0 should be startable: {details}")

    def test_wp_gv0_cannot_start_without_doc0(self):
        """WP-GV0 依赖 WP-DOC0，DOC0 未完成时不能 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-GV0", "plan.json", "0" * 64)
        ok, errors, details = service.can_start("WP-GV0")
        self.assertFalse(ok, "WP-GV0 should not be startable without WP-DOC0")
        self.assertIn(EC.WP_DEPENDENCY_NOT_MET, errors)

    def test_wp_gv0_can_start_after_doc0_ready(self):
        """WP-GV0 在 WP-DOC0 READY_FOR_AUDIT 后可以 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-GV0", "plan.json", "0" * 64)
        service.wp_states["WP-DOC0"] = "READY_FOR_AUDIT"
        ok, errors, details = service.can_start("WP-GV0")
        self.assertTrue(ok, f"WP-GV0 should be startable after DOC0 READY_FOR_AUDIT: {details}")

    def test_unknown_wp_rejected(self):
        """未知 WP 必须被拒绝。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        ok, errors, details = service.can_start("WP-UNKNOWN")
        self.assertFalse(ok)
        self.assertIn(EC.WP_UNKNOWN, errors)

    def test_already_started_rejected(self):
        """已 start 的 WP 不能再次 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.wp_states["WP-DOC0"] = "IN_PROGRESS"
        ok, errors, details = service.can_start("WP-DOC0")
        self.assertFalse(ok)
        self.assertIn(EC.WP_ALREADY_STARTED, errors)


class Test22OverclaimWPsAllRejected(unittest.TestCase):
    """R5 核心测试：22 个越级 WP 全部被拒绝 start。

    这 22 个 WP 曾被越级标为 IMPLEMENTED_PENDING_EVIDENCE，
    但 development dependency 未满足（GV0 未到 READY_FOR_AUDIT）。
    """

    # 从 DAG 中所有有 development_dependencies 的 WP
    OVERCLAIM_WPS = [
        "WP-GV0",      # deps: WP-DOC0
        "WP-VLT0",     # deps: WP-GV0
        "WP-HG0",      # deps: WP-GV0, WP-VLT0
        "WP-CW0",      # deps: WP-GV0, WP-VLT0
        "WP-CW-D1",    # deps: WP-CW0
        "WP-CW-C1",    # deps: WP-CW0
        "WP-QA0",      # deps: WP-HG0, WP-CW-D1, WP-CW-C1
        "WP-DB1L",     # deps: WP-GV0
        "WP-DB1I",     # deps: WP-DB1L, WP-HG0, WP-VLT0
        "WP-RT1",      # deps: WP-DB1I, WP-VLT0
        "WP-SV1",      # deps: WP-VLT0, WP-RT1
        "WP-IN1",      # deps: WP-GV0
        "WP-TX1",      # deps: WP-IN1, WP-VLT0, WP-RT1, WP-HG0
        "WP-CW1",      # deps: WP-RT1, WP-CW-D1, WP-CW-C1
        "WP-QA1",      # deps: WP-QA0, WP-SV1, WP-RT1, WP-HG0
        "WP-CS1",      # deps: WP-IN1, WP-TX1, WP-CW1, WP-HG0, WP-QA1, WP-SV1
        "WP-ST1",      # deps: WP-TX1, WP-CW1, WP-SV1
        "WP-EX1",      # deps: WP-CS1, WP-QA1, WP-SV1, WP-ST1
        "WP-AU1",      # deps: WP-EX1, WP-CW1
        "WP-EV1",      # deps: WP-AU1
        "WP-RV1",      # deps: WP-EV1, WP-HG0
        "WP-VR1",      # deps: WP-RV1
        "WP-GA1",      # deps: WP-VR1
        "WP-OP1",      # deps: WP-VR1
    ]

    def test_all_22_wps_rejected_without_deps(self):
        """所有 22+ 个有依赖的 WP 在依赖未满足时全部被拒绝 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        # 所有 WP 都处于 NOT_STARTED（初始状态）
        rejected = []
        for wp_id in self.OVERCLAIM_WPS:
            ok, errors, details = service.can_start(wp_id)
            if not ok:
                rejected.append(wp_id)
            else:
                # 这个 WP 不应该能 start
                self.fail(f"{wp_id} should be rejected but was allowed: {details}")

        self.assertEqual(
            len(rejected), len(self.OVERCLAIM_WPS),
            f"all {len(self.OVERCLAIM_WPS)} WPs should be rejected, "
            f"only {len(rejected)} were rejected"
        )

    def test_start_rejected_for_all_22(self):
        """start() 对所有 22+ 个有依赖的 WP 返回 False。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        for wp_id in self.OVERCLAIM_WPS:
            ok, errors, details = service.start(wp_id)
            self.assertFalse(ok, f"{wp_id} start should be rejected")
            self.assertIn(EC.WP_DEPENDENCY_NOT_MET, errors)


class TestStateTransitions(unittest.TestCase):
    """状态转换合法性测试。"""

    def test_not_started_to_in_progress_legal(self):
        """NOT_STARTED → IN_PROGRESS 是合法转换。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        ok, errors, details = service.transition("WP-DOC0", "IN_PROGRESS")
        self.assertTrue(ok, f"NOT_STARTED → IN_PROGRESS should be legal: {details}")

    def test_not_started_to_audited_pass_illegal(self):
        """NOT_STARTED → AUDITED_PASS 是非法转换（越级）。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        ok, errors, details = service.transition("WP-DOC0", "AUDITED_PASS")
        self.assertFalse(ok)
        self.assertIn(EC.WP_ILLEGAL_TRANSITION, errors)

    def test_not_started_to_ready_for_audit_illegal(self):
        """NOT_STARTED → READY_FOR_AUDIT 是非法转换（越级）。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        ok, errors, details = service.transition("WP-DOC0", "READY_FOR_AUDIT")
        self.assertFalse(ok)
        self.assertIn(EC.WP_ILLEGAL_TRANSITION, errors)

    def test_not_started_to_implemented_pending_illegal(self):
        """NOT_STARTED → IMPLEMENTED_PENDING_EVIDENCE 是非法转换（越级）。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        ok, errors, details = service.transition("WP-DOC0", "IMPLEMENTED_PENDING_EVIDENCE")
        self.assertFalse(ok)
        self.assertIn(EC.WP_ILLEGAL_TRANSITION, errors)


class TestBoardProjection(unittest.TestCase):
    """Board 投影一致性测试。"""

    def test_board_projection_all_wps(self):
        """board 投影包含所有 WP。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        board = service.project_to_board()
        self.assertGreater(len(board), 20)
        for row in board:
            self.assertIn("wp_id", row)
            self.assertIn("state", row)
            self.assertEqual(row["state"], "NOT_STARTED")

    def test_board_consistency_check(self):
        """board 一致性检查通过。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        board = service.project_to_board()
        ok, errors, details = service.verify_board_consistency(board)
        self.assertTrue(ok, f"board should be consistent: {details}")

    def test_board_inconsistency_detected(self):
        """board 不一致被检测。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        # 手动让 WP-DOC0 进入 IN_PROGRESS
        service.wp_states["WP-DOC0"] = "IN_PROGRESS"
        # 但 board 仍然显示 NOT_STARTED
        board = service.project_to_board()
        # 篡改 board
        for row in board:
            if row["wp_id"] == "WP-DOC0":
                row["state"] = "NOT_STARTED"  # 不一致
        ok, errors, details = service.verify_board_consistency(board)
        self.assertFalse(ok)
        self.assertIn(EC.WP_ILLEGAL_TRANSITION, errors)


# ─── R5 补全：complete/activate/Plan/audit debt/event log 测试 ──────────

class TestCompleteCommand(unittest.TestCase):
    """R5 补全: complete 命令测试。"""

    def test_complete_from_in_progress(self):
        """IN_PROGRESS → READY_FOR_AUDIT 合法。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        ok, errors, details = service.complete(
            "WP-DOC0", completion_contract="DOC_BOOTSTRAP_RECORD",
        )
        self.assertTrue(ok, f"complete should succeed: {details}")
        self.assertEqual(service.get_state("WP-DOC0"), "READY_FOR_AUDIT")

    def test_complete_from_not_started_rejected(self):
        """NOT_STARTED → READY_FOR_AUDIT 非法。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        ok, errors, details = service.complete("WP-DOC0")
        self.assertFalse(ok)
        self.assertIn(EC.WP_ILLEGAL_TRANSITION, errors)

    def test_complete_wrong_contract_rejected(self):
        """completion contract 不匹配必须拒绝。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        ok, errors, details = service.complete(
            "WP-DOC0", completion_contract="WRONG_CONTRACT",
        )
        self.assertFalse(ok)

    def test_implementer_cannot_write_audited_pass(self):
        """implementer 不能写 AUDITED_PASS。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        service.wp_states["WP-DOC0"] = "READY_FOR_AUDIT"
        ok, errors, details = service.complete(
            "WP-DOC0", actor_type="IMPLEMENTER", target_state="AUDITED_PASS",
        )
        self.assertFalse(ok)
        self.assertIn(EC.WP_ILLEGAL_TRANSITION, errors)


class TestActivateCommand(unittest.TestCase):
    """R5 补全: activate 命令测试。"""

    def test_activate_without_audited_pass_rejected(self):
        """非 AUDITED_PASS 状态不能 activate。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        ok, errors, details = service.activate(
            "WP-DOC0", permit_ref="permit.json", reservation_ref="res.json",
        )
        self.assertFalse(ok)

    def test_activate_without_permit_rejected(self):
        """没有 permit 不能 activate。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.wp_states["WP-DOC0"] = "AUDITED_PASS"
        ok, errors, details = service.activate("WP-DOC0")
        self.assertFalse(ok)

    def test_activate_with_all_deps_rejected_if_dep_not_audited(self):
        """activation dependency 未 AUDITED_PASS 不能 activate。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        # WP-GV0 的 activation_dependencies 是 ["WP-DOC0"]
        service.wp_states["WP-GV0"] = "AUDITED_PASS"
        # WP-DOC0 不是 AUDITED_PASS
        ok, errors, details = service.activate(
            "WP-GV0", permit_ref="permit.json", reservation_ref="res.json",
        )
        self.assertFalse(ok)
        self.assertIn(EC.WP_DEPENDENCY_NOT_MET, errors)


class TestPlanValidation(unittest.TestCase):
    """R5 补全: Plan 验证测试。"""

    def test_start_without_plan_rejected(self):
        """没有注册 Plan 不能 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        # WP-DOC0 没有 dev deps，但没有 Plan
        ok, errors, details = service.can_start("WP-DOC0")
        self.assertFalse(ok)
        # 应该因为缺 Plan 而失败
        has_plan_error = any("Plan" in d for d in details)
        self.assertTrue(has_plan_error, f"should mention missing Plan: {details}")

    def test_start_with_plan_succeeds(self):
        """有注册 Plan 时可以 start（如果 deps 满足）。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        ok, errors, details = service.can_start("WP-DOC0")
        self.assertTrue(ok, f"WP-DOC0 with Plan should be startable: {details}")


class TestAuditDebtInheritance(unittest.TestCase):
    """R5 补全: audit debt 继承测试。"""

    def test_inherit_audit_debt(self):
        """可以继承 audit debt。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        debt = [{"ref": "doc0-debt.json", "sha256": "0" * 64}]
        service.inherit_audit_debt("WP-GV0", debt)
        self.assertEqual(service.get_audit_debt("WP-GV0"), debt)

    def test_no_audit_debt_by_default(self):
        """默认没有 audit debt。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        self.assertEqual(service.get_audit_debt("WP-GV0"), [])


class TestEventLog(unittest.TestCase):
    """R5 补全: append-only 事件日志测试。"""

    def test_event_log_records_start(self):
        """start 命令记录事件。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        events = service.get_event_log()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["wp_id"], "WP-DOC0")
        self.assertEqual(events[0]["from_state"], "NOT_STARTED")
        self.assertEqual(events[0]["to_state"], "IN_PROGRESS")
        self.assertEqual(events[0]["command"], "start")

    def test_event_log_records_complete(self):
        """complete 命令记录事件。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        service.complete("WP-DOC0", completion_contract="DOC_BOOTSTRAP_RECORD")
        events = service.get_event_log()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["command"], "start")
        self.assertEqual(events[1]["command"], "complete")

    def test_event_log_append_only(self):
        """事件日志是 append-only（不能修改）。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        events_before = service.get_event_log()
        # 再次操作
        service.wp_states["WP-DOC0"] = "IN_PROGRESS"  # 不通过 start
        events_after = service.get_event_log()
        # 事件日志不应该改变（只有通过 start/complete/activate/transition 才记录）
        self.assertEqual(len(events_before), len(events_after))

    def test_event_log_consistency(self):
        """事件日志与当前状态一致。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        service.register_plan("WP-DOC0", "plan.json", "0" * 64)
        service.start("WP-DOC0")
        service.complete("WP-DOC0", completion_contract="DOC_BOOTSTRAP_RECORD")
        ok, errors, details = service.verify_event_log_consistency()
        self.assertTrue(ok, f"event log should be consistent: {details}")


# ─── R5 深度补全：双向对账测试 ─────────────────────────────────────────

class TestImplementationCapabilityRegistry(unittest.TestCase):
    """R5 深度补全：ImplementationCapabilityRegistry 测试。"""

    def test_default_registry_created(self):
        """默认能力注册表可创建。"""
        from seven_system.operations.capability_registry import create_default_registry
        registry = create_default_registry()
        self.assertIsNotNone(registry)

    def test_known_capabilities_registered(self):
        """已知能力已注册。"""
        from seven_system.operations.capability_registry import create_default_registry
        registry = create_default_registry()
        for cap_id in ["P1_DRY_RUN", "COMPLETION_CONTRACT_VERIFIER", "HUMAN_GATE_ED25519"]:
            self.assertIsNotNone(registry.get(cap_id), f"{cap_id} should be registered")

    def test_unknown_capability_returns_not_implemented(self):
        """未知能力一律 NOT_IMPLEMENTED。"""
        from seven_system.operations.capability_registry import create_default_registry
        registry = create_default_registry()
        self.assertEqual(registry.get_status("UNKNOWN_CAP"), "NOT_IMPLEMENTED")
        self.assertFalse(registry.is_reachable("UNKNOWN_CAP"))

    def test_not_implemented_capabilities_listed(self):
        """未实现的能力明确列出。"""
        from seven_system.operations.capability_registry import create_default_registry
        registry = create_default_registry()
        for cap_id in ["VLT0_D_CAS", "DB_ARANGO_LIVE", "TARGET_SOLVER_PORT"]:
            entry = registry.get(cap_id)
            self.assertIsNotNone(entry, f"{cap_id} should be in registry")
            self.assertEqual(entry.implementation_status, "NOT_IMPLEMENTED")


class TestTruthConsistencyChecker(unittest.TestCase):
    """R5 深度补全：文档/机器真值双向对账。"""

    def test_board_consistent_with_registry_passes(self):
        """board 与 registry 一致时 PASS。"""
        from seven_system.operations.capability_registry import (
            create_default_registry, TruthConsistencyChecker,
        )
        registry = create_default_registry()
        checker = TruthConsistencyChecker(registry=registry)
        board = {
            "P1_DRY_RUN": "IMPLEMENTED_PENDING_EVIDENCE",
            "VLT0_D_CAS": "NOT_IMPLEMENTED",
        }
        result = checker.check_board_consistency(board)
        self.assertEqual(result.verdict, "PASS")

    def test_board_overclaim_detected(self):
        """board 过度声明被检测。"""
        from seven_system.operations.capability_registry import (
            create_default_registry, TruthConsistencyChecker,
        )
        registry = create_default_registry()
        checker = TruthConsistencyChecker(registry=registry)
        board = {
            "VLT0_D_CAS": "IMPLEMENTED_PENDING_EVIDENCE",  # overclaim
        }
        result = checker.check_board_consistency(board)
        self.assertEqual(result.verdict, "FAIL")

    def test_capabilities_consistent_with_registry(self):
        """CLI capabilities 与 registry 一致时 PASS。"""
        from seven_system.operations.capability_registry import (
            create_default_registry, TruthConsistencyChecker,
        )
        registry = create_default_registry()
        checker = TruthConsistencyChecker(registry=registry)
        cli_caps = ["P1_DRY_RUN", "COMPLETION_CONTRACT_VERIFIER"]
        result = checker.check_capabilities_consistency(cli_caps)
        self.assertEqual(result.verdict, "PASS")

    def test_cli_reports_unknown_capability_detected(self):
        """CLI 报告未知能力被检测。"""
        from seven_system.operations.capability_registry import (
            create_default_registry, TruthConsistencyChecker,
        )
        registry = create_default_registry()
        checker = TruthConsistencyChecker(registry=registry)
        cli_caps = ["P1_DRY_RUN", "FAKE_CAPABILITY"]
        result = checker.check_capabilities_consistency(cli_caps)
        self.assertEqual(result.verdict, "FAIL")

    def test_no_stub_as_real(self):
        """stub/fake 不能被声明为真实能力。"""
        from seven_system.operations.capability_registry import (
            create_default_registry, TruthConsistencyChecker,
        )
        registry = create_default_registry()
        checker = TruthConsistencyChecker(registry=registry)
        result = checker.check_no_stub_as_real(["VLT0_D_CAS"])
        # VLT0_D_CAS is NOT_IMPLEMENTED, declaring it real should not trigger stub check
        # because it's not a stub, it's just not implemented
        # Let's test with ADAPTER_REGISTRY which has "mock" in nonclaims
        result2 = checker.check_no_stub_as_real(["ADAPTER_REGISTRY"])
        # ADAPTER_REGISTRY has "mock" in nonclaims, so declaring it real should FAIL
        self.assertEqual(result2.verdict, "FAIL")


if __name__ == "__main__":
    unittest.main()
