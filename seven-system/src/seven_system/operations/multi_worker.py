"""MultiWorkerScheduler — 多 worker 并行调度。

来自 WP-OP1：multi-worker、公平调度、无饥饿、队列不丢失。

关键约束（blocker）：
- worker 饥饿（某 worker 永远拿不到 work）→ OP_WORKER_STARVATION
- 队列丢失（调度过程中 queue item 丢失）→ OP_QUEUE_LOSS
- worker 状态不在 OP_WORKER_STATES → OP_WORKER_STATE_INVALID

公平保证：round-robin 调度，每个 worker 都有机会拿到 work。
队列持久化：所有入队的 item 都在 schedule log 中记录，可重放验证无丢失。

SIDE_EFFECT_FREE：纯内存模拟，不部署真实 multi-worker。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    OP_WORKER_STATES,
    VerificationErrorCode as EC,
)


class MultiWorkerError(Exception):
    """Multi-worker 调度错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class WorkItem:
    """单个 work item。"""

    item_id: str
    payload: dict[str, Any] = field(default_factory=dict)
    assigned_worker: str | None = None
    completed: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "item_id": self.item_id,
            "payload": dict(self.payload),
            "assigned_worker": self.assigned_worker,
            "completed": self.completed,
        }


@dataclass
class WorkerState:
    """单个 worker 的状态。"""

    worker_id: str
    state: str = "IDLE"
    assigned_count: int = 0
    completed_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "worker_id": self.worker_id,
            "state": self.state,
            "assigned_count": self.assigned_count,
            "completed_count": self.completed_count,
        }


@dataclass
class ScheduleEntry:
    """调度日志中的一条记录——证明 queue item 没有丢失。"""

    sequence: int
    item_id: str
    worker_id: str
    action: str  # ENQUEUE / ASSIGN / COMPLETE

    def to_dict(self) -> dict[str, Any]:
        return {
            "sequence": self.sequence,
            "item_id": self.item_id,
            "worker_id": self.worker_id,
            "action": self.action,
        }


class MultiWorkerScheduler:
    """多 worker 公平调度器。

    round-robin 调度保证无饥饿。
    schedule log 记录所有 enqueue/assign/complete，可重放验证无队列丢失。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    def __init__(self, worker_ids: list[str]) -> None:
        if not worker_ids:
            raise MultiWorkerError(EC.REQUIRED_FIELD_MISSING, "worker_ids empty")
        self._workers: dict[str, WorkerState] = {
            wid: WorkerState(worker_id=wid) for wid in worker_ids
        }
        self._queue: list[WorkItem] = []
        self._items: dict[str, WorkItem] = {}
        self._schedule_log: list[ScheduleEntry] = []
        self._next_seq: int = 0
        self._rr_index: int = 0

    @property
    def workers(self) -> list[WorkerState]:
        return list(self._workers.values())

    @property
    def queue(self) -> list[WorkItem]:
        return list(self._queue)

    @property
    def schedule_log(self) -> list[ScheduleEntry]:
        return list(self._schedule_log)

    @property
    def queue_length(self) -> int:
        return len(self._queue)

    def _log(self, item_id: str, worker_id: str, action: str) -> None:
        self._schedule_log.append(
            ScheduleEntry(
                sequence=self._next_seq,
                item_id=item_id,
                worker_id=worker_id,
                action=action,
            )
        )
        self._next_seq += 1

    def enqueue(self, item: WorkItem) -> WorkItem:
        """入队一个 work item。"""
        if item.item_id in self._items:
            raise MultiWorkerError(
                EC.OP_QUEUE_LOSS,
                f"duplicate item_id {item.item_id}",
            )
        self._items[item.item_id] = item
        self._queue.append(item)
        self._log(item.item_id, "", "ENQUEUE")
        return item

    def assign_next(self) -> tuple[WorkItem, str] | None:
        """round-robin 分配下一个 work item 给一个 worker。

        公平保证：跳过 BUSY worker，给 IDLE worker。
        如果所有 worker 都 BUSY，返回 None。
        如果队列为空，返回 None。
        """
        if not self._queue:
            return None

        # 找一个 IDLE worker（round-robin 起始）
        worker_ids = list(self._workers.keys())
        n = len(worker_ids)
        chosen: str | None = None
        for i in range(n):
            idx = (self._rr_index + i) % n
            wid = worker_ids[idx]
            if self._workers[wid].state == "IDLE":
                chosen = wid
                self._rr_index = (idx + 1) % n
                break

        if chosen is None:
            return None

        item = self._queue.pop(0)
        item.assigned_worker = chosen
        self._workers[chosen].state = "BUSY"
        self._workers[chosen].assigned_count += 1
        self._log(item.item_id, chosen, "ASSIGN")
        return item, chosen

    def complete(self, item_id: str, worker_id: str) -> WorkItem:
        """标记一个 work item 完成。"""
        item = self._items.get(item_id)
        if item is None:
            raise MultiWorkerError(
                EC.OP_QUEUE_LOSS,
                f"item {item_id} not found (queue loss)",
            )
        if item.assigned_worker != worker_id:
            raise MultiWorkerError(
                EC.OP_QUEUE_LOSS,
                f"item {item_id} not assigned to worker {worker_id}",
            )
        item.completed = True
        ws = self._workers[worker_id]
        ws.state = "IDLE"
        ws.completed_count += 1
        self._log(item_id, worker_id, "COMPLETE")
        return item

    def drain_worker(self, worker_id: str) -> None:
        """将 worker 标记为 DRAINED（不再接受新 work）。"""
        if worker_id not in self._workers:
            raise MultiWorkerError(
                EC.OP_WORKER_STATE_INVALID,
                f"unknown worker {worker_id}",
            )
        self._workers[worker_id].state = "DRAINED"

    def crash_worker(self, worker_id: str) -> None:
        """模拟 worker 崩溃。"""
        if worker_id not in self._workers:
            raise MultiWorkerError(
                EC.OP_WORKER_STATE_INVALID,
                f"unknown worker {worker_id}",
            )
        self._workers[worker_id].state = "CRASHED"

    def recover_worker(self, worker_id: str) -> None:
        """恢复崩溃的 worker。"""
        if worker_id not in self._workers:
            raise MultiWorkerError(
                EC.OP_WORKER_STATE_INVALID,
                f"unknown worker {worker_id}",
            )
        self._workers[worker_id].state = "RECOVERED"

    def compute_schedule_hash(self) -> str:
        """计算调度日志的 hash（用于验证无队列丢失）。"""
        data = [e.to_dict() for e in self._schedule_log]
        return hashlib.sha256(canonical_json_bytes(data)).hexdigest()

    def verify_no_starvation(self) -> list[tuple[EC, str]]:
        """验证无饥饿：每个非 DRAINED/CRASHED worker 都拿到过 work
        （当有足够 work 时）。

        判定：如果总入队数 >= worker 数，每个 IDLE-eligible worker
        的 assigned_count 应 > 0。
        """
        errors: list[tuple[EC, str]] = []
        total_enqueued = sum(
            1 for e in self._schedule_log if e.action == "ENQUEUE"
        )
        eligible = [
            w for w in self._workers.values()
            if w.state not in ("DRAINED", "CRASHED")
        ]
        if total_enqueued >= len(eligible) and eligible:
            for w in eligible:
                if w.assigned_count == 0:
                    errors.append((
                        EC.OP_WORKER_STARVATION,
                        f"worker {w.worker_id} never got work "
                        f"(starvation)",
                    ))
        return errors

    def verify_no_queue_loss(self) -> list[tuple[EC, str]]:
        """验证无队列丢失：每个 ENQUEUE 的 item 都有 ASSIGN + COMPLETE，
        或仍在 queue 中。
        """
        errors: list[tuple[EC, str]] = []
        enqueued: set[str] = set()
        assigned: set[str] = set()
        completed: set[str] = set()
        for e in self._schedule_log:
            if e.action == "ENQUEUE":
                enqueued.add(e.item_id)
            elif e.action == "ASSIGN":
                assigned.add(e.item_id)
            elif e.action == "COMPLETE":
                completed.add(e.item_id)

        for item_id in enqueued:
            item = self._items.get(item_id)
            if item is None:
                errors.append((
                    EC.OP_QUEUE_LOSS,
                    f"item {item_id} enqueued but not found",
                ))
                continue
            # item 要么在 queue 中，要么 assigned，要么 completed
            in_queue = any(q.item_id == item_id for q in self._queue)
            if not in_queue and item_id not in assigned and item_id not in completed:
                errors.append((
                    EC.OP_QUEUE_LOSS,
                    f"item {item_id} lost (not in queue, not assigned, "
                    f"not completed)",
                ))

        return errors

    def verify_worker_states(self) -> list[tuple[EC, str]]:
        """验证所有 worker 状态合法。"""
        errors: list[tuple[EC, str]] = []
        for w in self._workers.values():
            if w.state not in OP_WORKER_STATES:
                errors.append((
                    EC.OP_WORKER_STATE_INVALID,
                    f"worker {w.worker_id} state {w.state!r} invalid",
                ))
        return errors
