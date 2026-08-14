"""WP-OP1 Operations/Scale 测试。

测试层级：MultiWorkerScheduler → RedisProjectionManager →
          EpochManager → ActiveLearningScheduler → SoakTestRunner →
          CrossEpochBudgetLedger → ActiveReleasePointer →
          CrossEpochDuplicateAssessment → LongitudinalLearningVerdict →
          OperationsCapabilityReport →
          Negative → Determinism → Boundary → Constants

覆盖：
- Golden path: multi-worker scheduling (no starvation) → Redis projection →
  create Epoch → seal Epoch → next Epoch → cross-Epoch remainder=0
- Soak test simulation
- Active learning scheduling (coverage tensor, selection record)
- Cross-Epoch budget ledger
- Redis rebuild from events
- Negative: unaudited live, worker starvation, queue loss, mid-Epoch version
  change, holdout reuse, cross-Epoch duplicate, Redis not rebuildable,
  Epoch not sealed, cross-Epoch remainder != 0, active release not gated
- Cross-Epoch duplicate assessment
- Longitudinal learning verdict
- Deterministic hash tests
- OP1 boundary tests (allowed/forbidden output kinds — real scaling FORBIDDEN
  without GA1)
- All constants verified

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
    OP_ALLOWED_OUTPUT_KINDS,
    OP_BUDGET_KINDS,
    OP_CHECK_IDS,
    OP_CLAIMS,
    OP_DUPLICATE_KINDS,
    OP_EPOCH_STATES,
    OP_EPOCH_TRANSITIONS,
    OP_FORBIDDEN_OUTPUT_KINDS,
    OP_NONCLAIMS,
    OP_RELEASE_STATES,
    OP_SIDE_EFFECT_KEYS,
    OP_SOAK_STATES,
    OP_WORKER_STATES,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.operations.multi_worker import (
    MultiWorkerError,
    MultiWorkerScheduler,
    WorkItem,
)
from seven_system.operations.redis_projection_manager import (
    RedisProjectionManager,
    RedisProjectionRebuild,
)
from seven_system.operations.epoch_manager import (
    EpochManager,
    EpochManagerError,
    EpochSealRecord,
)
from seven_system.operations.active_learning import (
    ActiveLearningScheduler,
    CoverageTensorDelta,
    CoverageTensorSnapshot,
    EpochSelectionRecord,
)
from seven_system.operations.soak import (
    SoakTestError,
    SoakTestReport,
    SoakTestRunner,
)
from seven_system.operations.budget import (
    BudgetLedgerError,
    CrossEpochBudgetLedger,
    CrossEpochBudgetLedgerManager,
    GlobalBudgetLedger,
)
from seven_system.operations.release_pointer import (
    ActiveReleasePointer,
    ActiveReleasePointerError,
    ActiveReleasePointerManager,
)
from seven_system.operations.duplicate_assessment import (
    CrossEpochDuplicateAssessment,
    CrossEpochDuplicateAssessor,
    DuplicateAssessmentError,
)
from seven_system.operations.longitudinal_verdict import (
    EpochLearningSummary,
    LongitudinalLearningVerdict,
    build_longitudinal_learning_verdict,
    verify_longitudinal_learning_verdict,
)
from seven_system.operations.capability_report import (
    OPERATIONS_REPORT_SCHEMA_VERSION,
    OPERATIONS_REPORT_SCOPE,
    OperationsCapabilityReportError,
    build_operations_capability_report,
    verify_operations_capability_report,
)
from seven_system.runtime.work_event import WorkEvent, WorkEventLog
from seven_system.runtime.outbox import Outbox


def _sha256(payload) -> str:
    return hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def _make_event_log(n: int = 3) -> tuple[WorkEventLog, Outbox]:
    """构建测试用的 event log + outbox。"""
    log = WorkEventLog()
    outbox = Outbox()
    for i in range(n):
        event = WorkEvent.build(
            event_id=f"evt-{i}",
            aggregate_id="agg-1",
            sequence=i,
            event_type="WORK_ITEM_STATE_CHANGED",
            fence_token=1,
            actor_or_rule="test",
            payload={"step": i},
        )
        log.append(event)
        outbox.append(
            message_id=f"msg-{i}",
            aggregate_id="agg-1",
            sequence=i,
            event_type="WORK_ITEM_STATE_CHANGED",
            payload={"step": i},
        )
    return log, outbox


# ─── MultiWorkerScheduler ──────────────────────────────────────────────


class TestMultiWorkerScheduler(unittest.TestCase):
    """Multi-worker 调度测试。"""

    def test_no_starvation_round_robin(self) -> None:
        """Golden path: round-robin 调度，无饥饿。"""
        sched = MultiWorkerScheduler(["w0", "w1", "w2"])
        for i in range(9):
            sched.enqueue(WorkItem(item_id=f"item-{i}"))

        assigned = []
        for _ in range(9):
            result = sched.assign_next()
            self.assertIsNotNone(result)
            item, wid = result
            assigned.append(wid)
            sched.complete(item.item_id, wid)

        # 每个 worker 都拿到 3 个
        self.assertEqual(assigned.count("w0"), 3)
        self.assertEqual(assigned.count("w1"), 3)
        self.assertEqual(assigned.count("w2"), 3)
        self.assertEqual(sched.verify_no_starvation(), [])
        self.assertEqual(sched.verify_no_queue_loss(), [])

    def test_no_queue_loss(self) -> None:
        """队列不丢失：所有 item 都有完整生命周期。"""
        sched = MultiWorkerScheduler(["w0", "w1"])
        for i in range(4):
            sched.enqueue(WorkItem(item_id=f"item-{i}"))

        for _ in range(4):
            result = sched.assign_next()
            self.assertIsNotNone(result)
            item, wid = result
            sched.complete(item.item_id, wid)

        self.assertEqual(sched.verify_no_queue_loss(), [])
        # schedule log 有 4 ENQUEUE + 4 ASSIGN + 4 COMPLETE = 12
        self.assertEqual(len(sched.schedule_log), 12)

    def test_deterministic_schedule_hash(self) -> None:
        """调度 hash 确定性。"""
        def build() -> str:
            sched = MultiWorkerScheduler(["w0", "w1"])
            for i in range(4):
                sched.enqueue(WorkItem(item_id=f"item-{i}"))
            for _ in range(4):
                result = sched.assign_next()
                item, wid = result
                sched.complete(item.item_id, wid)
            return sched.compute_schedule_hash()

        self.assertEqual(build(), build())

    def test_worker_states_valid(self) -> None:
        """worker 状态合法。"""
        sched = MultiWorkerScheduler(["w0", "w1"])
        self.assertEqual(sched.verify_worker_states(), [])

    def test_negative_starvation(self) -> None:
        """Blocker: worker 饥饿。"""
        sched = MultiWorkerScheduler(["w0", "w1", "w2"])
        # w2 永远 DRAINED，不拿 work
        sched.drain_worker("w2")
        for i in range(4):
            sched.enqueue(WorkItem(item_id=f"item-{i}"))
        for _ in range(4):
            result = sched.assign_next()
            item, wid = result
            sched.complete(item.item_id, wid)

        # w0 和 w1 各拿到 2 个，w2 拿到 0 个但 DRAINED 不算饥饿
        errors = sched.verify_no_starvation()
        # w2 是 DRAINED，不算 eligible，所以无饥饿
        self.assertEqual(errors, [])

    def test_negative_starvation_real(self) -> None:
        """Blocker: 真实饥饿——eligible worker 拿不到 work。

        通过手动篡改 assigned_count 模拟饥饿。
        """
        sched = MultiWorkerScheduler(["w0", "w1", "w2"])
        for i in range(6):
            sched.enqueue(WorkItem(item_id=f"item-{i}"))
        for _ in range(6):
            result = sched.assign_next()
            item, wid = result
            sched.complete(item.item_id, wid)

        # 篡改 w2 的 assigned_count 为 0 模拟饥饿
        sched._workers["w2"].assigned_count = 0
        errors = sched.verify_no_starvation()
        self.assertTrue(any(e[0] == EC.OP_WORKER_STARVATION for e in errors))

    def test_negative_queue_loss(self) -> None:
        """Blocker: 队列丢失。"""
        sched = MultiWorkerScheduler(["w0", "w1"])
        sched.enqueue(WorkItem(item_id="item-0"))
        sched.enqueue(WorkItem(item_id="item-1"))

        # 篡改：从 items 中删除 item-1 模拟丢失
        del sched._items["item-1"]
        errors = sched.verify_no_queue_loss()
        self.assertTrue(any(e[0] == EC.OP_QUEUE_LOSS for e in errors))

    def test_duplicate_item_rejected(self) -> None:
        """重复 item_id 被拒绝。"""
        sched = MultiWorkerScheduler(["w0"])
        sched.enqueue(WorkItem(item_id="item-0"))
        with self.assertRaises(MultiWorkerError) as ctx:
            sched.enqueue(WorkItem(item_id="item-0"))
        self.assertEqual(ctx.exception.code, EC.OP_QUEUE_LOSS)

    def test_complete_wrong_worker(self) -> None:
        """错误 worker complete 被拒绝。"""
        sched = MultiWorkerScheduler(["w0", "w1"])
        sched.enqueue(WorkItem(item_id="item-0"))
        result = sched.assign_next()
        item, wid = result
        with self.assertRaises(MultiWorkerError) as ctx:
            sched.complete(item.item_id, "w1")
        self.assertEqual(ctx.exception.code, EC.OP_QUEUE_LOSS)


# ─── RedisProjectionManager ────────────────────────────────────────────


class TestRedisProjectionManager(unittest.TestCase):
    """Redis 投影管理测试。"""

    def test_rebuild_from_events(self) -> None:
        """Golden path: Redis 全丢 → 从 event 重建。"""
        mgr = RedisProjectionManager()
        log, outbox = _make_event_log(3)

        # 投影 worker 状态
        mgr.project_worker_state(
            worker_id="w0",
            state="IDLE",
            assigned_count=0,
            completed_count=0,
            source_event_id="evt-0",
            source_sequence=0,
        )
        before_hash = mgr.compute_projection_hash()
        self.assertGreater(mgr.size, 0)

        # 模拟全丢
        lost_hash = mgr.simulate_full_loss()
        self.assertEqual(lost_hash, before_hash)
        self.assertEqual(mgr.size, 0)

        # 从 event 重建
        record = mgr.rebuild_from_events(
            rebuild_id="rebuild-0",
            event_log=log,
            outbox=outbox,
            before_hash=before_hash,
        )
        self.assertIsInstance(record, RedisProjectionRebuild)
        self.assertTrue(record.is_hash_valid)

    def test_rebuild_hash_match(self) -> None:
        """重建 hash 匹配验证。"""
        mgr = RedisProjectionManager()
        log, outbox = _make_event_log(3)

        # 先用 event/outbox 填充投影
        mgr.rebuild_from_events(
            rebuild_id="init",
            event_log=log,
            outbox=outbox,
            before_hash="",
        )
        before_hash = mgr.compute_projection_hash()

        # 全丢后重建
        mgr.simulate_full_loss()
        record = mgr.rebuild_from_events(
            rebuild_id="rebuild-1",
            event_log=log,
            outbox=outbox,
            before_hash=before_hash,
        )
        self.assertTrue(record.hash_match)
        self.assertEqual(mgr.verify_rebuild_hash(rebuild_record=record), [])

    def test_verify_rebuildable(self) -> None:
        """验证 Redis 可重建。"""
        mgr = RedisProjectionManager()
        log, outbox = _make_event_log(3)
        self.assertEqual(mgr.verify_rebuildable(event_log=log, outbox=outbox), [])

    def test_deterministic_rebuild_hash(self) -> None:
        """重建 hash 确定性。"""
        log, outbox = _make_event_log(3)

        def rebuild() -> str:
            mgr = RedisProjectionManager()
            mgr.rebuild_from_events(
                rebuild_id="r",
                event_log=log,
                outbox=outbox,
                before_hash="",
            )
            return mgr.compute_projection_hash()

        self.assertEqual(rebuild(), rebuild())

    def test_negative_rebuild_hash_mismatch(self) -> None:
        """Blocker: 重建 hash 不匹配。"""
        mgr = RedisProjectionManager()
        log, outbox = _make_event_log(3)
        record = mgr.rebuild_from_events(
            rebuild_id="rebuild-bad",
            event_log=log,
            outbox=outbox,
            before_hash="deadbeef" * 8,
        )
        self.assertFalse(record.hash_match)
        errors = mgr.verify_rebuild_hash(rebuild_record=record)
        self.assertTrue(any(e[0] == EC.OP_REDIS_NOT_REBUILDABLE for e in errors))


# ─── EpochManager ──────────────────────────────────────────────────────


class TestEpochManager(unittest.TestCase):
    """Epoch 管理测试。"""

    def test_create_seal_next_epoch(self) -> None:
        """Golden path: create → seal → next Epoch。"""
        mgr = EpochManager()

        e0 = mgr.create_epoch("epoch-0")
        self.assertEqual(e0.state, "CREATED")
        mgr.start_epoch("epoch-0")
        mgr.add_work("epoch-0", 5)
        mgr.set_remainder("epoch-0", 0)
        record0 = mgr.seal_epoch("epoch-0")
        self.assertEqual(record0.state, "SEALED")
        self.assertTrue(record0.is_hash_valid)

        # 下一个 Epoch
        e1 = mgr.create_epoch("epoch-1")
        self.assertEqual(e1.state, "CREATED")
        mgr.start_epoch("epoch-1")
        mgr.add_work("epoch-1", 3)
        mgr.set_remainder("epoch-1", 0)
        record1 = mgr.seal_epoch("epoch-1")
        self.assertEqual(record1.state, "SEALED")

        # 跨 Epoch remainder=0
        self.assertEqual(mgr.verify_cross_epoch_remainder_zero(), [])
        self.assertEqual(mgr.verify_epoch_sealed_before_next(), [])
        self.assertEqual(mgr.verify_seal_record_hashes(), [])

    def test_cross_epoch_remainder_zero(self) -> None:
        """跨 Epoch remainder=0 验证。"""
        mgr = EpochManager()
        for i in range(3):
            eid = f"epoch-{i}"
            mgr.create_epoch(eid)
            mgr.start_epoch(eid)
            mgr.add_work(eid, 2)
            mgr.set_remainder(eid, 0)
            mgr.seal_epoch(eid)
        self.assertEqual(mgr.verify_cross_epoch_remainder_zero(), [])

    def test_epoch_seal_record_hash(self) -> None:
        """EpochSealRecord hash 确定性。"""
        mgr = EpochManager()
        mgr.create_epoch("epoch-0")
        mgr.start_epoch("epoch-0")
        mgr.add_work("epoch-0", 5)
        mgr.set_remainder("epoch-0", 0)
        record = mgr.seal_epoch("epoch-0")
        self.assertTrue(record.is_hash_valid)
        self.assertEqual(mgr.verify_seal_record_hashes(), [])

    def test_negative_epoch_not_sealed_before_next(self) -> None:
        """Blocker: Epoch 未 seal 就开下一个。"""
        mgr = EpochManager()
        mgr.create_epoch("epoch-0")
        mgr.start_epoch("epoch-0")
        # 不 seal 就开下一个
        with self.assertRaises(EpochManagerError) as ctx:
            mgr.create_epoch("epoch-1")
        self.assertEqual(ctx.exception.code, EC.OP_EPOCH_NOT_SEALED)

    def test_negative_cross_epoch_remainder_nonzero(self) -> None:
        """Blocker: 跨 Epoch remainder != 0。"""
        mgr = EpochManager()
        mgr.create_epoch("epoch-0")
        mgr.start_epoch("epoch-0")
        mgr.add_work("epoch-0", 5)
        mgr.set_remainder("epoch-0", 3)  # remainder != 0
        mgr.seal_epoch("epoch-0")
        errors = mgr.verify_cross_epoch_remainder_zero()
        self.assertTrue(
            any(e[0] == EC.OP_CROSS_EPOCH_REMAINDER_NONZERO for e in errors)
        )

    def test_negative_illegal_transition(self) -> None:
        """Blocker: 非法状态转换。"""
        mgr = EpochManager()
        mgr.create_epoch("epoch-0")
        # CREATED → SEALED 非法（必须经过 RUNNING → SEALING）
        with self.assertRaises(EpochManagerError) as ctx:
            mgr.seal_epoch("epoch-0")
        self.assertEqual(ctx.exception.code, EC.OP_EPOCH_TRANSITION_INVALID)

    def test_epoch_states_valid(self) -> None:
        """Epoch 状态合法。"""
        mgr = EpochManager()
        mgr.create_epoch("epoch-0")
        self.assertEqual(mgr.verify_epoch_states(), [])


# ─── ActiveLearningScheduler ───────────────────────────────────────────


class TestActiveLearningScheduler(unittest.TestCase):
    """Active learning 调度测试。"""

    def test_coverage_tensor_snapshot(self) -> None:
        """CoverageTensor 快照。"""
        sched = ActiveLearningScheduler()
        snap = sched.take_snapshot(
            snapshot_id="snap-0",
            epoch_id="epoch-0",
            coverage_cells={"cell-a": 0, "cell-b": 2, "cell-c": 0},
        )
        self.assertTrue(snap.is_hash_valid)
        self.assertEqual(snap.covered_cells, 1)
        self.assertEqual(snap.gap_cells, ["cell-a", "cell-c"])
        self.assertEqual(sched.verify_coverage_tensor(snap), [])

    def test_coverage_tensor_delta(self) -> None:
        """CoverageTensor delta。"""
        sched = ActiveLearningScheduler()
        snap0 = sched.take_snapshot(
            snapshot_id="snap-0",
            epoch_id="epoch-0",
            coverage_cells={"cell-a": 0, "cell-b": 2},
        )
        snap1 = sched.take_snapshot(
            snapshot_id="snap-1",
            epoch_id="epoch-1",
            coverage_cells={"cell-a": 3, "cell-b": 2, "cell-c": 1},
        )
        delta = sched.compute_delta(
            delta_id="delta-0",
            from_snap=snap0,
            to_snap=snap1,
        )
        self.assertTrue(delta.is_hash_valid)
        # cell-a: 0→3 is a new cell (was 0), cell-c: 0→1 is also new
        self.assertIn("cell-a", delta.new_cells)
        self.assertIn("cell-c", delta.new_cells)
        self.assertEqual(sched.verify_delta(delta), [])

    def test_selection_record(self) -> None:
        """EpochSelectionRecord——根据 gap 选择。"""
        sched = ActiveLearningScheduler()
        snap = sched.take_snapshot(
            snapshot_id="snap-0",
            epoch_id="epoch-0",
            coverage_cells={"cell-a": 0, "cell-b": 2, "cell-c": 0, "cell-d": 0},
        )
        record = sched.select_next_cells(
            selection_id="sel-0",
            epoch_id="epoch-1",
            snapshot=snap,
            max_cells=2,
        )
        self.assertEqual(len(record.selected_cells), 2)
        self.assertEqual(record.selection_reason, "evidence_gap")
        self.assertTrue(record.is_hash_valid)
        self.assertEqual(sched.verify_selection_record(record), [])

    def test_deterministic_snapshot_hash(self) -> None:
        """快照 hash 确定性。"""
        def build() -> CoverageTensorSnapshot:
            s = CoverageTensorSnapshot(
                snapshot_id="snap-0",
                epoch_id="epoch-0",
                coverage_cells={"cell-a": 0, "cell-b": 2},
            )
            s.content_hash = s.compute_content_hash()
            return s

        s1 = build()
        s2 = build()
        self.assertEqual(s1.content_hash, s2.content_hash)

    def test_negative_coverage_tensor_invalid(self) -> None:
        """Blocker: CoverageTensor 无效。"""
        snap = CoverageTensorSnapshot(
            snapshot_id="",
            epoch_id="epoch-0",
            coverage_cells={"cell-a": -1},
        )
        snap.content_hash = snap.compute_content_hash()
        errors = ActiveLearningScheduler().verify_coverage_tensor(snap)
        codes = {e[0] for e in errors}
        self.assertIn(EC.OP_COVERAGE_TENSOR_INVALID, codes)

    def test_negative_selection_record_invalid(self) -> None:
        """Blocker: EpochSelectionRecord 无效。"""
        record = EpochSelectionRecord(
            selection_id="",
            epoch_id="",
            selected_cells=[],
            selection_reason="",
        )
        record.content_hash = record.compute_content_hash()
        errors = ActiveLearningScheduler().verify_selection_record(record)
        codes = {e[0] for e in errors}
        self.assertIn(EC.OP_SELECTION_RECORD_INVALID, codes)


# ─── SoakTestRunner ────────────────────────────────────────────────────


class TestSoakTestRunner(unittest.TestCase):
    """Soak test 测试。"""

    def test_soak_continuous_execution(self) -> None:
        """Golden path: 连续执行。"""
        runner = SoakTestRunner()
        runner.start()
        for _ in range(5):
            runner.tick()
        runner.complete()
        report = runner.build_report("soak-0")
        self.assertTrue(report.completed)
        self.assertTrue(report.is_hash_valid)
        self.assertEqual(runner.verify_crash_recovery(), [])
        self.assertEqual(runner.verify_continuous_execution(), [])
        self.assertEqual(runner.verify_state(), [])

    def test_soak_crash_and_recover(self) -> None:
        """Soak: 崩溃 + 恢复。"""
        runner = SoakTestRunner()
        runner.start()
        runner.tick()
        runner.tick()
        runner.inject_crash()
        runner.recover()
        runner.tick()
        runner.complete()
        report = runner.build_report("soak-1")
        self.assertEqual(report.crashes, 1)
        self.assertEqual(report.recoveries, 1)
        self.assertEqual(runner.verify_crash_recovery(), [])

    def test_deterministic_soak_report_hash(self) -> None:
        """Soak 报告 hash 确定性。"""
        def build() -> SoakTestReport:
            runner = SoakTestRunner()
            runner.start()
            for _ in range(3):
                runner.tick(resource_usage={"cpu": 0.5, "mem": 0.3})
            runner.complete()
            return runner.build_report("soak-d")

        r1 = build()
        r2 = build()
        self.assertEqual(r1.content_hash, r2.content_hash)

    def test_negative_crash_not_recovered(self) -> None:
        """Blocker: 崩溃未恢复。"""
        runner = SoakTestRunner()
        runner.start()
        runner.tick()
        runner.inject_crash()
        # 不 recover 就 complete
        with self.assertRaises(SoakTestError) as ctx:
            runner.complete()
        self.assertEqual(ctx.exception.code, EC.OP_SOAK_CRASH_NOT_RECOVERED)

    def test_negative_unrecovered_crash_verify(self) -> None:
        """Blocker: 验证检测到未恢复崩溃。"""
        runner = SoakTestRunner()
        runner.start()
        runner.tick()
        runner.inject_crash()
        # 手动恢复状态但不通过 recover()
        runner._state = "COMPLETED"
        runner._unrecovered_crash = True
        errors = runner.verify_crash_recovery()
        self.assertTrue(any(e[0] == EC.OP_SOAK_CRASH_NOT_RECOVERED for e in errors))

    def test_negative_tick_gap(self) -> None:
        """Blocker: tick 序列有 gap。"""
        runner = SoakTestRunner()
        runner.start()
        runner.tick()
        runner.tick()
        # 篡改 tick 序号
        runner._ticks[1].tick = 99
        errors = runner.verify_continuous_execution()
        self.assertTrue(any(e[0] == EC.OP_SOAK_STATE_INVALID for e in errors))


# ─── CrossEpochBudgetLedger ────────────────────────────────────────────


class TestCrossEpochBudgetLedger(unittest.TestCase):
    """Cross-Epoch budget ledger 测试。"""

    def test_budget_not_reset_between_epochs(self) -> None:
        """Golden path: budget 不在 Epoch 间重置。"""
        mgr = CrossEpochBudgetLedgerManager("ledger-0")
        mgr.add_entry(
            epoch_id="epoch-0",
            budget_kind="COMPUTE",
            allocated=100,
            consumed=60,
        )
        mgr.add_entry(
            epoch_id="epoch-1",
            budget_kind="COMPUTE",
            allocated=50,
            consumed=40,
        )
        mgr.finalize()
        # 全局累计
        self.assertEqual(mgr.global_ledger.global_allocated["COMPUTE"], 150)
        self.assertEqual(mgr.global_ledger.global_consumed["COMPUTE"], 100)
        self.assertEqual(mgr.verify_budget_conserved(), [])
        self.assertEqual(mgr.verify_hashes(), [])

    def test_holdout_no_reuse(self) -> None:
        """holdout 跨 Epoch 不重用。"""
        mgr = CrossEpochBudgetLedgerManager("ledger-1")
        mgr.record_holdout_consumption(
            epoch_id="epoch-0",
            holdout_id="holdout-A",
            case_ids=["case-1", "case-2"],
        )
        mgr.finalize()
        self.assertEqual(mgr.verify_no_holdout_reuse(), [])

    def test_deterministic_ledger_hash(self) -> None:
        """ledger hash 确定性。"""
        def build() -> CrossEpochBudgetLedger:
            mgr = CrossEpochBudgetLedgerManager("ledger-d")
            mgr.add_entry(
                epoch_id="epoch-0",
                budget_kind="COMPUTE",
                allocated=100,
                consumed=50,
            )
            mgr.finalize()
            return mgr.ledger

        l1 = build()
        l2 = build()
        self.assertEqual(l1.content_hash, l2.content_hash)

    def test_negative_holdout_reuse(self) -> None:
        """Blocker: holdout 跨 Epoch 重用。"""
        mgr = CrossEpochBudgetLedgerManager("ledger-2")
        mgr.record_holdout_consumption(
            epoch_id="epoch-0",
            holdout_id="holdout-A",
            case_ids=["case-1"],
        )
        with self.assertRaises(BudgetLedgerError) as ctx:
            mgr.record_holdout_consumption(
                epoch_id="epoch-1",
                holdout_id="holdout-A",
                case_ids=["case-1"],
            )
        self.assertEqual(ctx.exception.code, EC.OP_HOLDOUT_REUSE_ACROSS_EPOCHS)

    def test_negative_budget_not_conserved(self) -> None:
        """Blocker: budget 不守恒。"""
        mgr = CrossEpochBudgetLedgerManager("ledger-3")
        with self.assertRaises(BudgetLedgerError) as ctx:
            mgr.add_entry(
                epoch_id="epoch-0",
                budget_kind="COMPUTE",
                allocated=10,
                consumed=20,
            )
        self.assertEqual(ctx.exception.code, EC.OP_BUDGET_NOT_CONSERVED)

    def test_negative_budget_kind_invalid(self) -> None:
        """Blocker: budget kind 无效。"""
        mgr = CrossEpochBudgetLedgerManager("ledger-4")
        with self.assertRaises(BudgetLedgerError) as ctx:
            mgr.add_entry(
                epoch_id="epoch-0",
                budget_kind="INVALID_KIND",
                allocated=10,
                consumed=5,
            )
        self.assertEqual(ctx.exception.code, EC.OP_BUDGET_KIND_INVALID)

    def test_global_budget_ledger_hash(self) -> None:
        """GlobalBudgetLedger hash。"""
        mgr = CrossEpochBudgetLedgerManager("ledger-5")
        mgr.add_entry(
            epoch_id="epoch-0",
            budget_kind="COMPUTE",
            allocated=100,
            consumed=50,
        )
        mgr.finalize()
        self.assertTrue(mgr.global_ledger.is_hash_valid)


# ─── ActiveReleasePointer ──────────────────────────────────────────────


class TestActiveReleasePointer(unittest.TestCase):
    """Active release pointer 测试。"""

    def test_activation_with_human_gate(self) -> None:
        """Golden path: activation 经过 HumanGate。"""
        mgr = ActiveReleasePointerManager()
        ptr = mgr.create_pointer(
            pointer_id="ptr-0",
            release_version="v1.0",
            bound_epoch_id="epoch-0",
        )
        self.assertEqual(ptr.state, "FROZEN")
        mgr.request_activation(pointer_id="ptr-0")
        mgr.gate_activation(pointer_id="ptr-0", human_gate_ref="hg-001")
        activated = mgr.activate("ptr-0")
        self.assertEqual(activated.state, "ACTIVATED")
        self.assertEqual(activated.human_gate_ref, "hg-001")
        self.assertEqual(mgr.verify_activation_gated(), [])
        self.assertEqual(mgr.verify_hashes(), [])

    def test_no_mid_epoch_version_change(self) -> None:
        """mid-Epoch 无版本变更。"""
        mgr = ActiveReleasePointerManager()
        mgr.create_pointer(
            pointer_id="ptr-0",
            release_version="v1.0",
            bound_epoch_id="epoch-0",
        )
        mgr.request_activation(pointer_id="ptr-0")
        mgr.gate_activation(pointer_id="ptr-0", human_gate_ref="hg-001")
        mgr.activate("ptr-0")
        self.assertEqual(mgr.verify_no_mid_epoch_version_change(epoch_id="epoch-0"), [])

    def test_deterministic_pointer_hash(self) -> None:
        """pointer hash 确定性。"""
        def build() -> ActiveReleasePointer:
            p = ActiveReleasePointer(
                pointer_id="ptr-0",
                release_version="v1.0",
                state="FROZEN",
                bound_epoch_id="epoch-0",
            )
            p.content_hash = p.compute_content_hash()
            return p

        p1 = build()
        p2 = build()
        self.assertEqual(p1.content_hash, p2.content_hash)

    def test_negative_mid_epoch_version_change(self) -> None:
        """Blocker: mid-Epoch 版本变更。"""
        mgr = ActiveReleasePointerManager()
        # 同一 epoch 两个 activated pointer
        for i in range(2):
            pid = f"ptr-{i}"
            mgr.create_pointer(
                pointer_id=pid,
                release_version=f"v{i}.0",
                bound_epoch_id="epoch-0",
            )
            mgr.request_activation(pointer_id=pid)
            mgr.gate_activation(pointer_id=pid, human_gate_ref=f"hg-{i}")
            mgr.activate(pid)
        errors = mgr.verify_no_mid_epoch_version_change(epoch_id="epoch-0")
        self.assertTrue(
            any(e[0] == EC.OP_MID_EPOCH_VERSION_CHANGE for e in errors)
        )

    def test_negative_activation_not_gated(self) -> None:
        """Blocker: activation 未经过 HumanGate。"""
        mgr = ActiveReleasePointerManager()
        mgr.create_pointer(
            pointer_id="ptr-0",
            release_version="v1.0",
            bound_epoch_id="epoch-0",
        )
        mgr.request_activation(pointer_id="ptr-0")
        with self.assertRaises(ActiveReleasePointerError) as ctx:
            mgr.activate("ptr-0")
        self.assertEqual(ctx.exception.code, EC.OP_ACTIVE_RELEASE_NOT_GATED)

    def test_negative_gate_without_human_gate_ref(self) -> None:
        """Blocker: gate 没有 HumanGate ref。"""
        mgr = ActiveReleasePointerManager()
        mgr.create_pointer(
            pointer_id="ptr-0",
            release_version="v1.0",
            bound_epoch_id="epoch-0",
        )
        mgr.request_activation(pointer_id="ptr-0")
        with self.assertRaises(ActiveReleasePointerError) as ctx:
            mgr.gate_activation(pointer_id="ptr-0", human_gate_ref="")
        self.assertEqual(ctx.exception.code, EC.OP_ACTIVE_RELEASE_NOT_GATED)

    def test_release_states_valid(self) -> None:
        """release 状态合法。"""
        mgr = ActiveReleasePointerManager()
        mgr.create_pointer(
            pointer_id="ptr-0",
            release_version="v1.0",
            bound_epoch_id="epoch-0",
        )
        self.assertEqual(mgr.verify_states(), [])


# ─── CrossEpochDuplicateAssessment ─────────────────────────────────────


class TestCrossEpochDuplicateAssessment(unittest.TestCase):
    """Cross-Epoch duplicate assessment 测试。"""

    def test_no_duplicate_counting(self) -> None:
        """Golden path: 无跨 Epoch 重复计数。"""
        assessor = CrossEpochDuplicateAssessor("assess-0")
        assessor.record_counted(
            epoch_id="epoch-0",
            kind="SAME_PROBLEM",
            fingerprint="prob-A",
        )
        assessor.record_counted(
            epoch_id="epoch-1",
            kind="SAME_PROBLEM",
            fingerprint="prob-B",
        )
        assessor.finalize()
        self.assertEqual(assessor.verify_no_cross_epoch_duplicate(), [])
        self.assertEqual(assessor.verify_kinds(), [])
        self.assertEqual(assessor.verify_hash(), [])

    def test_dedup_not_counted(self) -> None:
        """已知重复但不计数。"""
        assessor = CrossEpochDuplicateAssessor("assess-1")
        assessor.record_counted(
            epoch_id="epoch-0",
            kind="SAME_SOURCE_CLUSTER",
            fingerprint="cluster-A",
        )
        # epoch-1 中同一 cluster 不计数
        assessor.record_not_counted(
            epoch_id="epoch-1",
            kind="SAME_SOURCE_CLUSTER",
            fingerprint="cluster-A",
        )
        assessor.finalize()
        self.assertEqual(assessor.verify_no_cross_epoch_duplicate(), [])

    def test_deterministic_assessment_hash(self) -> None:
        """assessment hash 确定性。"""
        def build() -> CrossEpochDuplicateAssessment:
            a = CrossEpochDuplicateAssessor("assess-d")
            a.record_counted(
                epoch_id="epoch-0",
                kind="SAME_PROBLEM",
                fingerprint="prob-A",
            )
            a.finalize()
            return a.assessment

        a1 = build()
        a2 = build()
        self.assertEqual(a1.content_hash, a2.content_hash)

    def test_negative_cross_epoch_duplicate(self) -> None:
        """Blocker: 跨 Epoch 重复计数。"""
        assessor = CrossEpochDuplicateAssessor("assess-2")
        assessor.record_counted(
            epoch_id="epoch-0",
            kind="SAME_PROBLEM",
            fingerprint="prob-A",
        )
        with self.assertRaises(DuplicateAssessmentError) as ctx:
            assessor.record_counted(
                epoch_id="epoch-1",
                kind="SAME_PROBLEM",
                fingerprint="prob-A",
            )
        self.assertEqual(ctx.exception.code, EC.OP_CROSS_EPOCH_DUPLICATE)

    def test_negative_duplicate_kind_invalid(self) -> None:
        """Blocker: duplicate kind 无效。"""
        assessor = CrossEpochDuplicateAssessor("assess-3")
        with self.assertRaises(DuplicateAssessmentError) as ctx:
            assessor.record_counted(
                epoch_id="epoch-0",
                kind="INVALID_KIND",
                fingerprint="prob-A",
            )
        self.assertEqual(ctx.exception.code, EC.OP_DUPLICATE_KIND_INVALID)


# ─── LongitudinalLearningVerdict ───────────────────────────────────────


class TestLongitudinalLearningVerdict(unittest.TestCase):
    """Longitudinal learning verdict 测试。"""

    def test_build_longitudinal_verdict(self) -> None:
        """Golden path: 构建长期学习结论。"""
        summaries = [
            EpochLearningSummary(
                epoch_id="epoch-0",
                coverage_gain=5,
                evidence_count=10,
                verdict="PASS",
            ),
            EpochLearningSummary(
                epoch_id="epoch-1",
                coverage_gain=8,
                evidence_count=15,
                verdict="PASS",
            ),
        ]
        verdict = build_longitudinal_learning_verdict(
            verdict_id="llv-0",
            epoch_summaries=summaries,
        )
        self.assertEqual(verdict.total_coverage_gain, 13)
        self.assertEqual(verdict.total_evidence, 25)
        self.assertEqual(verdict.overall_verdict, "PASS")
        self.assertEqual(verdict.learning_trend, "IMPROVING")
        self.assertTrue(verdict.is_hash_valid)
        self.assertEqual(verify_longitudinal_learning_verdict(verdict), [])

    def test_learning_trend_stable(self) -> None:
        """学习趋势 STABLE。"""
        summaries = [
            EpochLearningSummary("e0", 5, 10, "PASS"),
            EpochLearningSummary("e1", 5, 10, "PASS"),
        ]
        verdict = build_longitudinal_learning_verdict(
            verdict_id="llv-1",
            epoch_summaries=summaries,
        )
        self.assertEqual(verdict.learning_trend, "STABLE")

    def test_learning_trend_declining(self) -> None:
        """学习趋势 DECLINING。"""
        summaries = [
            EpochLearningSummary("e0", 10, 20, "PASS"),
            EpochLearningSummary("e1", 2, 5, "PASS"),
        ]
        verdict = build_longitudinal_learning_verdict(
            verdict_id="llv-2",
            epoch_summaries=summaries,
        )
        self.assertEqual(verdict.learning_trend, "DECLINING")

    def test_overall_verdict_fail(self) -> None:
        """overall verdict FAIL（任一 epoch FAIL）。"""
        summaries = [
            EpochLearningSummary("e0", 5, 10, "PASS"),
            EpochLearningSummary("e1", 3, 5, "FAIL"),
        ]
        verdict = build_longitudinal_learning_verdict(
            verdict_id="llv-3",
            epoch_summaries=summaries,
        )
        self.assertEqual(verdict.overall_verdict, "FAIL")

    def test_deterministic_verdict_hash(self) -> None:
        """verdict hash 确定性。"""
        def build() -> LongitudinalLearningVerdict:
            return build_longitudinal_learning_verdict(
                verdict_id="llv-d",
                epoch_summaries=[
                    EpochLearningSummary("e0", 5, 10, "PASS"),
                    EpochLearningSummary("e1", 8, 15, "PASS"),
                ],
            )

        v1 = build()
        v2 = build()
        self.assertEqual(v1.content_hash, v2.content_hash)

    def test_negative_verdict_invalid(self) -> None:
        """Blocker: longitudinal verdict 无效。"""
        verdict = LongitudinalLearningVerdict(
            verdict_id="",
            epoch_summaries=[],
            total_coverage_gain=0,
            total_evidence=0,
            overall_verdict="INVALID",
            learning_trend="INVALID",
        )
        verdict.content_hash = verdict.compute_content_hash()
        errors = verify_longitudinal_learning_verdict(verdict)
        codes = {e[0] for e in errors}
        self.assertIn(EC.OP_LONGITUDINAL_VERDICT_INVALID, codes)

    def test_negative_hash_mismatch(self) -> None:
        """Blocker: hash 不匹配。"""
        summaries = [
            EpochLearningSummary("e0", 5, 10, "PASS"),
        ]
        verdict = build_longitudinal_learning_verdict(
            verdict_id="llv-bad",
            epoch_summaries=summaries,
        )
        # 篡改 content_hash
        verdict.content_hash = "deadbeef" * 8
        errors = verify_longitudinal_learning_verdict(verdict)
        self.assertTrue(
            any(e[0] == EC.OP_LONGITUDINAL_VERDICT_HASH_MISMATCH for e in errors)
        )


# ─── OperationsCapabilityReport ────────────────────────────────────────


class TestOperationsCapabilityReport(unittest.TestCase):
    """OperationsCapabilityReport 测试。"""

    def _make_valid_report_kwargs(self) -> dict:
        h = _sha256({"test": True})
        return {
            "dag_hash": h,
            "schedule_hash": h,
            "redis_rebuild_hash": h,
            "epoch_seal_hash": h,
            "coverage_tensor_hash": h,
            "selection_record_hash": h,
            "soak_report_hash": h,
            "budget_ledger_hash": h,
            "release_pointer_hash": h,
            "duplicate_assessment_hash": h,
            "longitudinal_verdict_hash": h,
            "multi_worker_no_starvation": True,
            "worker_queue_no_loss": True,
            "redis_rebuildable": True,
            "redis_rebuild_hash_match": True,
            "epoch_create_seal_next": True,
            "epoch_sealed_before_next": True,
            "cross_epoch_remainder_zero": True,
            "coverage_tensor_valid": True,
            "selection_record_valid": True,
            "soak_crash_recovered": True,
            "soak_continuous_execution": True,
            "budget_conserved": True,
            "holdout_no_reuse": True,
            "release_mid_epoch_no_change": True,
            "release_activation_gated": True,
            "no_cross_epoch_duplicate": True,
            "longitudinal_verdict_valid": True,
            "real_scaling_blocked_without_ga1": True,
            "verifier_identity": "test-verifier",
        }

    def test_build_valid_report(self) -> None:
        """Golden path: 构建有效报告。"""
        report = build_operations_capability_report(
            **self._make_valid_report_kwargs()
        )
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(report["blockers"], [])
        self.assertEqual(len(report["checks"]), len(OP_CHECK_IDS))
        self.assertEqual(set(report["claims"]), set(OP_CLAIMS))
        self.assertEqual(set(report["side_effects"]), set(OP_SIDE_EFFECT_KEYS))
        self.assertEqual(set(report["explicit_nonclaims"]), set(OP_NONCLAIMS))
        # verify passes
        self.assertEqual(verify_operations_capability_report(report), ())

    def test_report_schema_and_scope(self) -> None:
        """报告 schema 和 scope。"""
        report = build_operations_capability_report(
            **self._make_valid_report_kwargs()
        )
        self.assertEqual(
            report["schema_version"], OPERATIONS_REPORT_SCHEMA_VERSION
        )
        self.assertEqual(report["scope"], OPERATIONS_REPORT_SCOPE)
        self.assertEqual(report["report_kind"], "OperationsCapabilityReport")

    def test_all_side_effects_zero(self) -> None:
        """所有 side-effect 键为 0。"""
        report = build_operations_capability_report(
            **self._make_valid_report_kwargs()
        )
        for key in OP_SIDE_EFFECT_KEYS:
            self.assertEqual(report["side_effects"][key], 0)

    def test_negative_unaudited_live(self) -> None:
        """Blocker: 未审即 live（real_scaling_blocked_without_ga1=False）。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["real_scaling_blocked_without_ga1"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(EC.OP_UNAUDITED_LIVE.value, str(ctx.exception))

    def test_negative_worker_starvation_flag(self) -> None:
        """Blocker: worker starvation flag=False。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["multi_worker_no_starvation"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(EC.OP_WORKER_STARVATION.value, str(ctx.exception))

    def test_negative_queue_loss_flag(self) -> None:
        """Blocker: queue loss flag=False。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["worker_queue_no_loss"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(EC.OP_QUEUE_LOSS.value, str(ctx.exception))

    def test_negative_mid_epoch_version_change_flag(self) -> None:
        """Blocker: mid-Epoch version change flag=False。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["release_mid_epoch_no_change"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(EC.OP_MID_EPOCH_VERSION_CHANGE.value, str(ctx.exception))

    def test_negative_holdout_reuse_flag(self) -> None:
        """Blocker: holdout reuse flag=False。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["holdout_no_reuse"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(
            EC.OP_HOLDOUT_REUSE_ACROSS_EPOCHS.value, str(ctx.exception)
        )

    def test_negative_cross_epoch_duplicate_flag(self) -> None:
        """Blocker: cross-Epoch duplicate flag=False。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["no_cross_epoch_duplicate"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(EC.OP_CROSS_EPOCH_DUPLICATE.value, str(ctx.exception))

    def test_negative_redis_not_rebuildable_flag(self) -> None:
        """Blocker: redis not rebuildable flag=False。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["redis_rebuildable"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(EC.OP_REDIS_NOT_REBUILDABLE.value, str(ctx.exception))

    def test_negative_epoch_not_sealed_flag(self) -> None:
        """Blocker: epoch not sealed flag=False。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["epoch_create_seal_next"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(EC.OP_EPOCH_NOT_SEALED.value, str(ctx.exception))

    def test_negative_remainder_nonzero_flag(self) -> None:
        """Blocker: cross-Epoch remainder nonzero flag=False。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["cross_epoch_remainder_zero"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(
            EC.OP_CROSS_EPOCH_REMAINDER_NONZERO.value, str(ctx.exception)
        )

    def test_negative_active_release_not_gated_flag(self) -> None:
        """Blocker: active release not gated flag=False。"""
        kwargs = self._make_valid_report_kwargs()
        kwargs["release_activation_gated"] = False
        with self.assertRaises(OperationsCapabilityReportError) as ctx:
            build_operations_capability_report(**kwargs)
        self.assertIn(
            EC.OP_ACTIVE_RELEASE_NOT_GATED.value, str(ctx.exception)
        )

    def test_negative_side_effects_nonzero(self) -> None:
        """Blocker: side-effect 非 0。"""
        report = build_operations_capability_report(
            **self._make_valid_report_kwargs()
        )
        report["side_effects"]["solver_launches"] = 1
        errors = verify_operations_capability_report(report)
        self.assertTrue(any(e[0] == EC.OP_OUTPUT_KIND_FORBIDDEN for e in errors))

    def test_negative_forbidden_output_kind(self) -> None:
        """Blocker: 禁止输出 kind。"""
        report = build_operations_capability_report(
            **self._make_valid_report_kwargs()
        )
        report["report_kind"] = "LiveMultiWorkerDeployment"
        errors = verify_operations_capability_report(report)
        self.assertTrue(any(e[0] == EC.OP_OUTPUT_KIND_FORBIDDEN for e in errors))

    def test_negative_checks_mismatch(self) -> None:
        """Blocker: checks 不匹配。"""
        report = build_operations_capability_report(
            **self._make_valid_report_kwargs()
        )
        report["checks"] = report["checks"][:-1]
        errors = verify_operations_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_negative_claims_mismatch(self) -> None:
        """Blocker: claims 不匹配。"""
        report = build_operations_capability_report(
            **self._make_valid_report_kwargs()
        )
        report["claims"]["extra_claim"] = True
        errors = verify_operations_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))


# ─── Golden Path Integration ───────────────────────────────────────────


class TestGoldenPathIntegration(unittest.TestCase):
    """Golden path 集成测试：multi-worker → Redis → Epoch → AL → soak →
    budget → release → duplicate → longitudinal → capability report。"""

    def test_full_golden_path(self) -> None:
        """完整 golden path。"""
        h = _sha256({"golden": True})

        # 1. Multi-worker scheduling (no starvation)
        sched = MultiWorkerScheduler(["w0", "w1", "w2"])
        for i in range(9):
            sched.enqueue(WorkItem(item_id=f"item-{i}"))
        for _ in range(9):
            result = sched.assign_next()
            item, wid = result
            sched.complete(item.item_id, wid)
        self.assertEqual(sched.verify_no_starvation(), [])
        self.assertEqual(sched.verify_no_queue_loss(), [])
        schedule_hash = sched.compute_schedule_hash()

        # 2. Redis projection
        redis_mgr = RedisProjectionManager()
        log, outbox = _make_event_log(3)
        redis_mgr.project_worker_state(
            worker_id="w0",
            state="IDLE",
            assigned_count=3,
            completed_count=3,
            source_event_id="evt-0",
            source_sequence=0,
        )
        before_hash = redis_mgr.compute_projection_hash()
        redis_mgr.simulate_full_loss()
        rebuild_record = redis_mgr.rebuild_from_events(
            rebuild_id="rebuild-golden",
            event_log=log,
            outbox=outbox,
            before_hash=before_hash,
        )
        self.assertEqual(
            redis_mgr.verify_rebuildable(event_log=log, outbox=outbox), []
        )

        # 3. Epoch: create → seal → next
        epoch_mgr = EpochManager()
        for i in range(3):
            eid = f"epoch-{i}"
            epoch_mgr.create_epoch(eid)
            epoch_mgr.start_epoch(eid)
            epoch_mgr.add_work(eid, 3)
            epoch_mgr.set_remainder(eid, 0)
            epoch_mgr.seal_epoch(eid)
        self.assertEqual(epoch_mgr.verify_cross_epoch_remainder_zero(), [])
        self.assertEqual(epoch_mgr.verify_epoch_sealed_before_next(), [])
        self.assertEqual(epoch_mgr.verify_seal_record_hashes(), [])

        # 4. Active learning
        al = ActiveLearningScheduler()
        snap0 = al.take_snapshot(
            snapshot_id="snap-0",
            epoch_id="epoch-0",
            coverage_cells={"cell-a": 0, "cell-b": 0, "cell-c": 1},
        )
        sel = al.select_next_cells(
            selection_id="sel-0",
            epoch_id="epoch-1",
            snapshot=snap0,
            max_cells=2,
        )
        self.assertEqual(al.verify_coverage_tensor(snap0), [])
        self.assertEqual(al.verify_selection_record(sel), [])

        # 5. Soak test
        soak = SoakTestRunner()
        soak.start()
        for _ in range(5):
            soak.tick()
        soak.inject_crash()
        soak.recover()
        soak.tick()
        soak.complete()
        soak_report = soak.build_report("soak-golden")
        self.assertEqual(soak.verify_crash_recovery(), [])

        # 6. Budget ledger
        budget = CrossEpochBudgetLedgerManager("ledger-golden")
        budget.add_entry(
            epoch_id="epoch-0", budget_kind="COMPUTE",
            allocated=100, consumed=50,
        )
        budget.add_entry(
            epoch_id="epoch-1", budget_kind="COMPUTE",
            allocated=50, consumed=30,
        )
        budget.record_holdout_consumption(
            epoch_id="epoch-0", holdout_id="holdout-A",
            case_ids=["case-1"],
        )
        budget.finalize()
        self.assertEqual(budget.verify_budget_conserved(), [])
        self.assertEqual(budget.verify_no_holdout_reuse(), [])

        # 7. Release pointer
        release = ActiveReleasePointerManager()
        release.create_pointer(
            pointer_id="ptr-golden",
            release_version="v1.0",
            bound_epoch_id="epoch-0",
        )
        release.request_activation(pointer_id="ptr-golden")
        release.gate_activation(
            pointer_id="ptr-golden", human_gate_ref="hg-golden"
        )
        release.activate("ptr-golden")
        self.assertEqual(release.verify_activation_gated(), [])
        self.assertEqual(
            release.verify_no_mid_epoch_version_change(epoch_id="epoch-0"), []
        )

        # 8. Duplicate assessment
        dup = CrossEpochDuplicateAssessor("assess-golden")
        dup.record_counted(
            epoch_id="epoch-0", kind="SAME_PROBLEM",
            fingerprint="prob-A",
        )
        dup.record_counted(
            epoch_id="epoch-1", kind="SAME_PROBLEM",
            fingerprint="prob-B",
        )
        dup.finalize()
        self.assertEqual(dup.verify_no_cross_epoch_duplicate(), [])

        # 9. Longitudinal verdict
        llv = build_longitudinal_learning_verdict(
            verdict_id="llv-golden",
            epoch_summaries=[
                EpochLearningSummary("epoch-0", 5, 10, "PASS"),
                EpochLearningSummary("epoch-1", 8, 15, "PASS"),
                EpochLearningSummary("epoch-2", 10, 20, "PASS"),
            ],
        )
        self.assertEqual(verify_longitudinal_learning_verdict(llv), [])

        # 10. Capability report
        report = build_operations_capability_report(
            dag_hash=h,
            schedule_hash=schedule_hash,
            redis_rebuild_hash=rebuild_record.after_hash,
            epoch_seal_hash=epoch_mgr.seal_records[-1].content_hash,
            coverage_tensor_hash=snap0.content_hash,
            selection_record_hash=sel.content_hash,
            soak_report_hash=soak_report.content_hash,
            budget_ledger_hash=budget.ledger.content_hash,
            release_pointer_hash=release.active_pointer.content_hash,
            duplicate_assessment_hash=dup.assessment.content_hash,
            longitudinal_verdict_hash=llv.content_hash,
            multi_worker_no_starvation=True,
            worker_queue_no_loss=True,
            redis_rebuildable=True,
            redis_rebuild_hash_match=True,
            epoch_create_seal_next=True,
            epoch_sealed_before_next=True,
            cross_epoch_remainder_zero=True,
            coverage_tensor_valid=True,
            selection_record_valid=True,
            soak_crash_recovered=True,
            soak_continuous_execution=True,
            budget_conserved=True,
            holdout_no_reuse=True,
            release_mid_epoch_no_change=True,
            release_activation_gated=True,
            no_cross_epoch_duplicate=True,
            longitudinal_verdict_valid=True,
            real_scaling_blocked_without_ga1=True,
            verifier_identity="golden-path-verifier",
        )
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(verify_operations_capability_report(report), ())


# ─── Boundary Tests ────────────────────────────────────────────────────


class TestOP1Boundary(unittest.TestCase):
    """OP1 boundary 测试——allowed/forbidden output kinds。"""

    def test_allowed_output_kinds(self) -> None:
        """OP1 允许的输出对象种类。"""
        expected = {
            "MultiWorkerSchedule",
            "RedisProjectionRebuild",
            "EpochSealRecord",
            "CoverageTensorSnapshot",
            "CoverageTensorDelta",
            "EpochSelectionRecord",
            "SoakTestReport",
            "CrossEpochBudgetLedger",
            "GlobalBudgetLedger",
            "ActiveReleasePointer",
            "CrossEpochDuplicateAssessment",
            "LongitudinalLearningVerdict",
            "OperationsCapabilityReport",
        }
        self.assertEqual(OP_ALLOWED_OUTPUT_KINDS, expected)

    def test_forbidden_output_kinds(self) -> None:
        """OP1 禁止的输出对象种类（real scaling without GA1）。"""
        expected = {
            "LiveMultiWorkerDeployment",
            "LiveSolverDispatch",
            "LiveModelCall",
            "LiveRedisWrite",
            "LiveActiveReleaseActivation",
            "AuditRecord",
            "SystemCompletionBundle",
        }
        self.assertEqual(OP_FORBIDDEN_OUTPUT_KINDS, expected)

    def test_allowed_and_forbidden_disjoint(self) -> None:
        """allowed 和 forbidden 不相交。"""
        self.assertEqual(
            OP_ALLOWED_OUTPUT_KINDS & OP_FORBIDDEN_OUTPUT_KINDS, set()
        )

    def test_real_scaling_forbidden_without_ga1(self) -> None:
        """real scaling FORBIDDEN without GA1 AUDITED_PASS。"""
        # 所有 forbidden kind 都是 real scaling outputs
        for kind in OP_FORBIDDEN_OUTPUT_KINDS:
            self.assertIn(kind, {
                "LiveMultiWorkerDeployment",
                "LiveSolverDispatch",
                "LiveModelCall",
                "LiveRedisWrite",
                "LiveActiveReleaseActivation",
                "AuditRecord",
                "SystemCompletionBundle",
            })

    def test_capability_report_not_in_forbidden(self) -> None:
        """OperationsCapabilityReport 不在 forbidden 中。"""
        self.assertNotIn(
            "OperationsCapabilityReport", OP_FORBIDDEN_OUTPUT_KINDS
        )
        self.assertIn(
            "OperationsCapabilityReport", OP_ALLOWED_OUTPUT_KINDS
        )


# ─── Constants Verification ────────────────────────────────────────────


class TestOP1Constants(unittest.TestCase):
    """OP1 常量验证。"""

    def test_worker_states(self) -> None:
        """OP_WORKER_STATES。"""
        self.assertEqual(OP_WORKER_STATES, frozenset(
            {"IDLE", "BUSY", "DRAINED", "CRASHED", "RECOVERED"}
        ))

    def test_epoch_states(self) -> None:
        """OP_EPOCH_STATES。"""
        self.assertEqual(OP_EPOCH_STATES, frozenset(
            {"CREATED", "RUNNING", "SEALING", "SEALED", "SUPERSEDED"}
        ))

    def test_epoch_transitions(self) -> None:
        """OP_EPOCH_TRANSITIONS。"""
        expected = frozenset({
            ("CREATED", "RUNNING"),
            ("RUNNING", "SEALING"),
            ("SEALING", "SEALED"),
            ("SEALED", "SUPERSEDED"),
        })
        self.assertEqual(OP_EPOCH_TRANSITIONS, expected)

    def test_soak_states(self) -> None:
        """OP_SOAK_STATES。"""
        self.assertEqual(OP_SOAK_STATES, frozenset(
            {"IDLE", "RUNNING", "CRASHED", "RECOVERING",
             "RECOVERED", "COMPLETED"}
        ))

    def test_budget_kinds(self) -> None:
        """OP_BUDGET_KINDS。"""
        self.assertEqual(OP_BUDGET_KINDS, frozenset(
            {"COMPUTE", "HOLDOUT", "MODEL_CALLS", "SOLVER_RUNS",
             "WALL_TIME"}
        ))

    def test_release_states(self) -> None:
        """OP_RELEASE_STATES。"""
        self.assertEqual(OP_RELEASE_STATES, frozenset(
            {"FROZEN", "ACTIVATION_REQUESTED", "GATED", "ACTIVATED",
             "REJECTED"}
        ))

    def test_duplicate_kinds(self) -> None:
        """OP_DUPLICATE_KINDS。"""
        self.assertEqual(OP_DUPLICATE_KINDS, frozenset(
            {"SAME_PROBLEM", "SAME_SOURCE_CLUSTER", "SAME_EVIDENCE_CELL"}
        ))

    def test_side_effect_keys(self) -> None:
        """OP_SIDE_EFFECT_KEYS。"""
        expected = (
            "database_writes",
            "redis_writes",
            "solver_launches",
            "model_live_calls",
            "real_multi_worker_deployment",
            "live_active_release_activation",
        )
        self.assertEqual(OP_SIDE_EFFECT_KEYS, expected)

    def test_check_ids(self) -> None:
        """OP_CHECK_IDS。"""
        self.assertEqual(len(OP_CHECK_IDS), 19)
        # 无重复
        self.assertEqual(len(OP_CHECK_IDS), len(set(OP_CHECK_IDS)))
        # 全部以 op1. 开头
        for cid in OP_CHECK_IDS:
            self.assertTrue(cid.startswith("op1."))

    def test_claims(self) -> None:
        """OP_CLAIMS。"""
        self.assertEqual(len(OP_CLAIMS), 18)
        self.assertEqual(len(OP_CLAIMS), len(set(OP_CLAIMS)))

    def test_nonclaims(self) -> None:
        """OP_NONCLAIMS。"""
        self.assertEqual(len(OP_NONCLAIMS), 9)
        self.assertEqual(len(OP_NONCLAIMS), len(set(OP_NONCLAIMS)))
        # real scaling blocked nonclaim 存在
        self.assertIn(
            "real_scaling_blocked_needs_ga1_audited_pass", OP_NONCLAIMS
        )
        self.assertIn("status_implemented_pending_evidence", OP_NONCLAIMS)

    def test_error_codes_exist(self) -> None:
        """所有 OP1 error codes 存在。"""
        codes = [
            EC.OP_UNAUDITED_LIVE,
            EC.OP_WORKER_STARVATION,
            EC.OP_QUEUE_LOSS,
            EC.OP_MID_EPOCH_VERSION_CHANGE,
            EC.OP_HOLDOUT_REUSE_ACROSS_EPOCHS,
            EC.OP_CROSS_EPOCH_DUPLICATE,
            EC.OP_REDIS_NOT_REBUILDABLE,
            EC.OP_EPOCH_NOT_SEALED,
            EC.OP_CROSS_EPOCH_REMAINDER_NONZERO,
            EC.OP_BUDGET_NOT_CONSERVED,
            EC.OP_ACTIVE_RELEASE_NOT_GATED,
            EC.OP_SOAK_CRASH_NOT_RECOVERED,
            EC.OP_EPOCH_SEAL_HASH_MISMATCH,
            EC.OP_COVERAGE_TENSOR_INVALID,
            EC.OP_SELECTION_RECORD_INVALID,
            EC.OP_LONGITUDINAL_VERDICT_INVALID,
            EC.OP_WORKER_STATE_INVALID,
            EC.OP_EPOCH_STATE_INVALID,
            EC.OP_EPOCH_TRANSITION_INVALID,
            EC.OP_SOAK_STATE_INVALID,
            EC.OP_BUDGET_KIND_INVALID,
            EC.OP_RELEASE_STATE_INVALID,
            EC.OP_DUPLICATE_KIND_INVALID,
            EC.OP_OUTPUT_KIND_FORBIDDEN,
            EC.OP_CAPABILITY_HASH_MISMATCH,
            EC.OP_WORKER_QUEUE_HASH_MISMATCH,
            EC.OP_EPOCH_SEAL_RECORD_INVALID,
            EC.OP_COVERAGE_DELTA_INVALID,
            EC.OP_BUDGET_LEDGER_HASH_MISMATCH,
            EC.OP_RELEASE_POINTER_HASH_MISMATCH,
            EC.OP_LONGITUDINAL_VERDICT_HASH_MISMATCH,
        ]
        for code in codes:
            self.assertIsInstance(code, EC)
            self.assertTrue(code.value.startswith("OP_"))


if __name__ == "__main__":
    unittest.main()
