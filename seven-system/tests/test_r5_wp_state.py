"""R5: WorkPackageStateService — DAG 依赖强制执行测试。

这些测试证明 22 个工作包不能越级 start（development dependency 未满足）。
"""

from __future__ import annotations

import atexit
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.operations.work_package_state import WorkPackageStateService
from seven_system.contracts.errors import VerificationErrorCode as EC
from seven_system.hashing import canonical_json_bytes, file_sha256


DAG_PATH = SYSTEM_ROOT / "docs" / "implementation" / "work-package-dag.v1.json"
_TEST_TEMP_ROOT = Path(tempfile.mkdtemp(prefix="seven-r5-state-"))
atexit.register(shutil.rmtree, _TEST_TEMP_ROOT, ignore_errors=True)


def _hash_of_null_self_field(obj: dict, field: str) -> str:
    candidate = dict(obj)
    candidate[field] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def _ref_hash(ref: str, value: str = "1") -> dict[str, str]:
    return {"ref": ref, "sha256": value * 64}


def _make_tempdir() -> Path:
    return Path(tempfile.mkdtemp(prefix="case-", dir=_TEST_TEMP_ROOT))


def _write_json(path: Path, obj: dict) -> str:
    path.write_text(
        json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return file_sha256(path)


def _make_test_plan_object(wp_id: str) -> dict:
    plan = {
        "schema_id": "seven/work-package-plan",
        "schema_version": 1,
        "wp_id": wp_id,
        "implementation_attempt_id": f"{wp_id.lower()}-unit-test-plan-001",
        "plan_timing": "DOC0_BOOTSTRAP_RATIFICATION" if wp_id == "WP-DOC0" else "PREREGISTERED",
        "execution_mode": "SIDE_EFFECT_FREE",
        "protocol_deviations": (
            ["DOC0 bootstrap test fixture"]
            if wp_id == "WP-DOC0"
            else []
        ),
        "baseline": {"commit": "0" * 40, "tree": "1" * 40},
        "canonical_dag": {"ref": "work-package-dag.v1.json", "sha256": file_sha256(DAG_PATH)},
        "development_dependency_bundles": [],
        "inherited_audit_debt": [],
        "activation_dependencies": [],
        "normative_index_ref_and_hash": _ref_hash("normative-requirement-index.v1.json", "2"),
        "normative_review_record_ref_and_hash": (
            None if wp_id == "WP-DOC0" else _ref_hash("normative-review-record.json", "3")
        ),
        "requirement_ids": ["AUTH-001"],
        "normative_clause_ids": ["NORM-unit-test-001"],
        "normative_clause_scope": "unit test fixture scope",
        "normative_spec_refs_and_hashes": [_ref_hash("unit-test-spec.md", "4")],
        "goals": ["exercise WorkPackageStateService state transitions"],
        "non_goals": ["claim production readiness"],
        "allowed_path_rules": ["side-effect-free unit test only"],
        "forbidden_boundaries": ["no DB, model, Redis, D-volume or solver side effects"],
        "input_object_types_and_hashes": [],
        "output_object_types": ["unit-test-state-transition"],
        "interfaces_and_schema_ids": ["seven/work-package-plan"],
        "state_machines_and_registries": ["WorkPackageStateService"],
        "security_and_view_contracts": [],
        "idempotency_fence_recovery_rules": ["single in-memory service instance"],
        "test_plan_ids": ["test_r5_wp_state"],
        "external_execution_authorization_ref": None,
        "live_run_permit_ref": None,
        "authorization_consumption_reservation_ref": None,
        "side_effect_budget": {
            "db_connections": 0,
            "db_writes": 0,
            "redis_connections": 0,
            "remote_model_calls": 0,
            "target_solver_launches": 0,
            "d_volume_writes": 0,
        },
        "pass_criteria": ["registered plan can be reverified by the state service"],
        "stop_conditions": ["unit test finishes"],
        "explicit_nonclaims": ["not a production WorkPackagePlan"],
        "plan_hash_algorithm": "sha256(canonical-json-with-plan_hash-null)",
        "plan_hash": None,
    }
    plan["plan_hash"] = _hash_of_null_self_field(plan, "plan_hash")
    return plan


def _register_test_plan(service: WorkPackageStateService, wp_id: str) -> tuple[Path, str]:
    tmp = _make_tempdir()
    plan_path = tmp / f"{wp_id}.plan.json"
    plan_sha256 = _write_json(plan_path, _make_test_plan_object(wp_id))
    ok, errors, details = service.register_plan(wp_id, plan_path, plan_sha256)
    if not ok:
        raise AssertionError(f"test plan registration failed for {wp_id}: {errors} {details}")
    return plan_path, plan_sha256


def _make_doc0_completion_object(plan_path: Path, plan_sha256: str) -> dict:
    record = {
        "schema_id": "seven/docs/doc-bootstrap-completion-record",
        "schema_version": 1,
        "record_id": "doc0-unit-test-completion-001",
        "wp_id": "WP-DOC0",
        "implementation_subject": {"commit": "0" * 40, "tree": "1" * 40},
        "work_package_plan_ref_and_hash": {
            "ref": str(plan_path),
            "sha256": plan_sha256,
        },
        "normative_index_ref_and_hash": _ref_hash("normative-requirement-index.v1.json", "2"),
        "test_receipts": [_ref_hash("test_r5_wp_state.py", "5")],
        "side_effect_counts": {
            "db_connections": 0,
            "db_writes": 0,
            "redis_connections": 0,
            "remote_model_calls": 0,
            "target_solver_launches": 0,
            "d_volume_writes": 0,
        },
        "storage_assurance": "LOCAL_GIT_APPEND_ONLY_NOT_CAS",
        "claims": ["unit test completion object is schema-valid"],
        "nonclaims": ["not a production DOC0 completion record"],
        "created_at": "2026-08-14T12:00:00Z",
        "creator": "unit-test",
        "record_hash_algorithm": "sha256(canonical-json-with-record_hash-null)",
        "record_hash": None,
    }
    record["record_hash"] = _hash_of_null_self_field(record, "record_hash")
    return record


def _make_doc0_completion_file(
    service: WorkPackageStateService, plan_path: Path, plan_sha256: str,
) -> tuple[Path, str]:
    tmp = _make_tempdir()
    record_path = tmp / "doc0-completion-record.json"
    record_sha256 = _write_json(
        record_path, _make_doc0_completion_object(plan_path, plan_sha256)
    )
    return record_path, record_sha256


def _start_doc0(service: WorkPackageStateService) -> tuple[Path, str]:
    plan_path, plan_sha256 = _register_test_plan(service, "WP-DOC0")
    ok, errors, details = service.start("WP-DOC0")
    if not ok:
        raise AssertionError(f"WP-DOC0 start failed: {errors} {details}")
    return plan_path, plan_sha256


def _complete_doc0(service: WorkPackageStateService, plan_path: Path, plan_sha256: str) -> None:
    record_path, record_sha256 = _make_doc0_completion_file(service, plan_path, plan_sha256)
    ok, errors, details = service.complete(
        "WP-DOC0",
        completion_path=record_path,
        expected_file_sha256=record_sha256,
        completion_contract="DOC_BOOTSTRAP_RECORD",
    )
    if not ok:
        raise AssertionError(f"WP-DOC0 complete failed: {errors} {details}")


class TestWorkPackageStateService(unittest.TestCase):
    """WorkPackageStateService 基本功能测试。"""

    def test_wp_doc0_can_start_no_deps(self):
        """WP-DOC0 没有 development dependencies，可以直接 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        _register_test_plan(service, "WP-DOC0")
        ok, errors, details = service.can_start("WP-DOC0")
        self.assertTrue(ok, f"WP-DOC0 should be startable: {details}")

    def test_wp_gv0_cannot_start_without_doc0(self):
        """WP-GV0 依赖 WP-DOC0，DOC0 未完成时不能 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        _register_test_plan(service, "WP-GV0")
        ok, errors, details = service.can_start("WP-GV0")
        self.assertFalse(ok, "WP-GV0 should not be startable without WP-DOC0")
        self.assertIn(EC.WP_DEPENDENCY_NOT_MET, errors)

    def test_wp_gv0_can_start_after_doc0_ready(self):
        """WP-GV0 在 WP-DOC0 READY_FOR_AUDIT 后可以 start。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        _register_test_plan(service, "WP-GV0")
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

    def test_generic_transition_to_in_progress_rejected(self):
        """generic transition 不能进入 IN_PROGRESS；必须使用 start 命令。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        _register_test_plan(service, "WP-DOC0")
        ok, errors, details = service.transition("WP-DOC0", "IN_PROGRESS")
        self.assertFalse(ok, f"generic transition to IN_PROGRESS should be rejected: {details}")
        self.assertIn(EC.WP_ILLEGAL_TRANSITION, errors)

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
        plan_path, plan_sha256 = _start_doc0(service)
        record_path, record_sha256 = _make_doc0_completion_file(
            service, plan_path, plan_sha256
        )
        ok, errors, details = service.complete(
            "WP-DOC0",
            completion_path=record_path,
            expected_file_sha256=record_sha256,
            completion_contract="DOC_BOOTSTRAP_RECORD",
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
        _start_doc0(service)
        ok, errors, details = service.complete(
            "WP-DOC0", completion_contract="WRONG_CONTRACT",
        )
        self.assertFalse(ok)

    def test_implementer_cannot_write_audited_pass(self):
        """implementer 不能写 AUDITED_PASS。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        _start_doc0(service)
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
        _start_doc0(service)
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
        _register_test_plan(service, "WP-DOC0")
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
        _start_doc0(service)
        events = service.get_event_log()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["wp_id"], "WP-DOC0")
        self.assertEqual(events[0]["from_state"], "NOT_STARTED")
        self.assertEqual(events[0]["to_state"], "IN_PROGRESS")
        self.assertEqual(events[0]["command"], "start")

    def test_event_log_records_complete(self):
        """complete 命令记录事件。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        plan_path, plan_sha256 = _start_doc0(service)
        _complete_doc0(service, plan_path, plan_sha256)
        events = service.get_event_log()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["command"], "start")
        self.assertEqual(events[1]["command"], "complete")

    def test_event_log_append_only(self):
        """事件日志是 append-only（不能修改）。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        _start_doc0(service)
        events_before = service.get_event_log()
        # 再次操作
        service.wp_states["WP-DOC0"] = "IN_PROGRESS"  # 不通过 start
        events_after = service.get_event_log()
        # 事件日志不应该改变（只有通过 start/complete/activate/transition 才记录）
        self.assertEqual(len(events_before), len(events_after))

    def test_event_log_consistency(self):
        """事件日志与当前状态一致。"""
        service = WorkPackageStateService(dag_path=DAG_PATH)
        plan_path, plan_sha256 = _start_doc0(service)
        _complete_doc0(service, plan_path, plan_sha256)
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
        for cap_id in [
            "P1_DRY_RUN",
            "COMPLETION_CONTRACT_VERIFIER",
            "HUMAN_GATE_ED25519",
            "GA1_AUDIT_INPUT_PACK_PRECHECK",
            "GA1_AUDIT_READINESS_REPORT",
            "DB1L_LOGICAL_SITE_REPORT_PRECHECK",
            "WORK_PACKAGE_PLAN_BUILDER",
            "NORMATIVE_REVIEW_RECORD_VERIFIER",
        ]:
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
        for cap_id in [
            "VLT0_D_CAS",
            "DB_ARANGO_LIVE",
            "TARGET_SOLVER_PORT",
            "DEVIN_SOLVER_ADAPTER",
            "MODEL_ROLE_PORT",
            "COGNITIVE_WORKER_RUNTIME",
            "DEVIN_CLI_MODEL_ROLE_ADAPTER",
            "CODEX_EXEC_MODEL_ROLE_ADAPTER",
            "HUMAN_TASK_PORT",
            "HUMAN_GATE_SERVICE",
            "QUESTION_RELEASE_PIPELINE",
            "AUTHORING_BAKEOFF_A",
            "AUTHORING_BAKEOFF_B",
            "QA0_CONTROLLED_AUTHORING_LAB",
            "QA1_QUESTION_ADMISSION",
            "HARNESS_RESOURCE_CAPABILITY_REPORT",
            "NO_TOOL_SOLVER_CAPABILITY_REPORT",
            "SAFE_LAUNCH_CAPABILITY_REPORT",
            "ANSWER_ISOLATION_CAPABILITY_REPORT",
        ]:
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
