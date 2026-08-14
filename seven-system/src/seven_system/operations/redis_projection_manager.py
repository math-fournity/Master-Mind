"""RedisProjectionManager — 多 worker 状态的 Redis 投影管理。

来自 WP-OP1：Redis 投影、Redis 全丢 → 从 event 重建。

复用 RT1 RedisProjection。管理多 worker 调度状态的投影：
- worker 状态投影
- 队列长度投影
- epoch 状态投影

关键约束（blocker）：
- Redis 投影不可重建 → OP_REDIS_NOT_REBUILDABLE
- 重建后 hash 不匹配 → OP_REDIS_NOT_REBUILDABLE

SIDE_EFFECT_FREE：纯内存模拟 Redis。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from ..runtime.redis_projection import RedisProjection
from ..runtime.work_event import WorkEvent, WorkEventLog
from ..runtime.outbox import Outbox


class RedisProjectionManagerError(Exception):
    """Redis 投影管理错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class RedisProjectionRebuild:
    """Redis 重建记录——证明 Redis 可从 event 重建。"""

    rebuild_id: str
    before_hash: str
    after_hash: str
    event_count: int
    outbox_count: int
    hash_match: bool
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "rebuild_id": self.rebuild_id,
            "before_hash": self.before_hash,
            "after_hash": self.after_hash,
            "event_count": self.event_count,
            "outbox_count": self.outbox_count,
            "hash_match": self.hash_match,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


class RedisProjectionManager:
    """多 worker Redis 投影管理器。

    管理 worker 状态、队列、epoch 状态的 Redis 投影。
    Redis 全丢时从 WorkEventLog + Outbox 重建。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    PREFIX = "op1:seven:"

    def __init__(self) -> None:
        self._projection = RedisProjection()
        self._worker_state_keys: set[str] = set()

    @property
    def projection(self) -> RedisProjection:
        return self._projection

    @property
    def size(self) -> int:
        return self._projection.size

    def project_worker_state(
        self,
        *,
        worker_id: str,
        state: str,
        assigned_count: int,
        completed_count: int,
        source_event_id: str,
        source_sequence: int,
    ) -> None:
        """投影 worker 状态。"""
        key = f"worker:{worker_id}"
        self._projection.put(
            key=key,
            value={
                "worker_id": worker_id,
                "state": state,
                "assigned_count": assigned_count,
                "completed_count": completed_count,
            },
            source_event_id=source_event_id,
            source_sequence=source_sequence,
        )
        self._worker_state_keys.add(key)

    def project_epoch_state(
        self,
        *,
        epoch_id: str,
        state: str,
        source_event_id: str,
        source_sequence: int,
    ) -> None:
        """投影 epoch 状态。"""
        self._projection.put(
            key=f"epoch:{epoch_id}",
            value={"epoch_id": epoch_id, "state": state},
            source_event_id=source_event_id,
            source_sequence=source_sequence,
        )

    def project_queue_length(
        self,
        *,
        queue_length: int,
        source_event_id: str,
        source_sequence: int,
    ) -> None:
        """投影队列长度。"""
        self._projection.put(
            key="queue:length",
            value={"queue_length": queue_length},
            source_event_id=source_event_id,
            source_sequence=source_sequence,
        )

    def compute_projection_hash(self) -> str:
        """计算当前投影 hash。"""
        return self._projection.compute_projection_hash()

    def simulate_full_loss(self) -> str:
        """模拟 Redis 全丢，返回丢失前的 hash。"""
        before_hash = self.compute_projection_hash()
        self._projection.clear()
        return before_hash

    def rebuild_from_events(
        self,
        *,
        rebuild_id: str,
        event_log: WorkEventLog,
        outbox: Outbox,
        before_hash: str,
    ) -> RedisProjectionRebuild:
        """从 WorkEventLog + Outbox 重建投影。

        返回 RedisProjectionRebuild 记录，包含重建前后 hash 和匹配验证。
        """
        after_hash = self._projection.rebuild_from_events(
            event_log=event_log,
            outbox=outbox,
        )
        record = RedisProjectionRebuild(
            rebuild_id=rebuild_id,
            before_hash=before_hash,
            after_hash=after_hash,
            event_count=event_log.length,
            outbox_count=len(outbox.messages),
            hash_match=(before_hash == after_hash),
        )
        # set content_hash
        record.content_hash = record.compute_content_hash()
        return record

    def verify_rebuildable(
        self,
        *,
        event_log: WorkEventLog,
        outbox: Outbox,
    ) -> list[tuple[EC, str]]:
        """验证 Redis 投影可从 event 重建。

        blocker：不可重建 → OP_REDIS_NOT_REBUILDABLE
        """
        errors: list[tuple[EC, str]] = []
        temp = RedisProjection()
        try:
            temp.rebuild_from_events(event_log=event_log, outbox=outbox)
        except Exception as exc:
            errors.append((
                EC.OP_REDIS_NOT_REBUILDABLE,
                f"rebuild failed: {exc}",
            ))
            return errors

        # 验证每个 event 都有投影
        for event in event_log.events:
            key = temp.PREFIX + f"event:{event.aggregate_id}:{event.sequence}"
            if temp.get(f"event:{event.aggregate_id}:{event.sequence}") is None:
                errors.append((
                    EC.OP_REDIS_NOT_REBUILDABLE,
                    f"event {event.event_id} not rebuildable",
                ))

        # 验证每个 outbox 消息都有投影
        for msg in outbox.messages:
            if temp.get(f"outbox:{msg.aggregate_id}:{msg.sequence}") is None:
                errors.append((
                    EC.OP_REDIS_NOT_REBUILDABLE,
                    f"outbox message {msg.message_id} not rebuildable",
                ))

        return errors

    def verify_rebuild_hash(
        self,
        *,
        rebuild_record: RedisProjectionRebuild,
    ) -> list[tuple[EC, str]]:
        """验证重建 hash 匹配 + record hash 有效。"""
        errors: list[tuple[EC, str]] = []
        if not rebuild_record.hash_match:
            errors.append((
                EC.OP_REDIS_NOT_REBUILDABLE,
                f"rebuild hash mismatch: before "
                f"{rebuild_record.before_hash} != after "
                f"{rebuild_record.after_hash}",
            ))
        if not rebuild_record.is_hash_valid:
            errors.append((
                EC.OP_REDIS_NOT_REBUILDABLE,
                "RedisProjectionRebuild content_hash invalid",
            ))
        return errors
