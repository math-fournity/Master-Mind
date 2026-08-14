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
        ok, errors, details = service.can_start("WP-DOC0")
        self.assertTrue(ok, f"WP-DOC0 should be startable: {details}")

    def test_wp_gv0_cannot_start_without_doc0(self):
        """WP-GV0 依赖 WP-DOC0，DOC0 未完成时不能 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        ok, errors, details = service.can_start("WP-GV0")
        self.assertFalse(ok, "WP-GV0 should not be startable without WP-DOC0")
        self.assertIn(EC.WP_DEPENDENCY_NOT_MET, errors)

    def test_wp_gv0_can_start_after_doc0_ready(self):
        """WP-GV0 在 WP-DOC0 READY_FOR_AUDIT 后可以 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
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


if __name__ == "__main__":
    unittest.main()
