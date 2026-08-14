"""RedisProjection — 可重建的 Redis 调度投影。

Redis 只做可重建调度投影，不保存历史真值或唯一结论。
Redis 丢失时从 DB event/outbox 重建。

投影内容：
- lease-ready 队列
- 优先级
- 心跳投影

不变量：
- Redis 数据可从 WorkEvent + Outbox 完全重建
- Redis 丢失不影响真值（真值在 DB event/outbox）
- 重建后投影 hash 必须与丢失前一致（确定性重建）

SIDE_EFFECT_FREE：纯内存模拟 Redis。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    REDIS_PROJECTION_STATES,
    VerificationErrorCode as EC,
)
from .work_event import WorkEvent, WorkEventLog
from .outbox import Outbox, OutboxMessage


class RedisProjectionError(Exception):
    """Redis 投影错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class ProjectionEntry:
    """单条 Redis 投影条目。"""

    key: str
    value: dict[str, Any]
    source_event_id: str
    source_sequence: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "key": self.key,
            "value": dict(self.value),
            "source_event_id": self.source_event_id,
            "source_sequence": self.source_sequence,
        }


class RedisProjection:
    """可重建的 Redis 调度投影。

    从 WorkEventLog + Outbox 重建。
    重建是确定性的：相同输入产生相同投影。
    """

    PREFIX = "evidence:seven:"

    def __init__(self) -> None:
        self._entries: dict[str, ProjectionEntry] = {}
        self._state: str = "FRESH"

    @property
    def state(self) -> str:
        return self._state

    @property
    def entries(self) -> list[ProjectionEntry]:
        return list(self._entries.values())

    @property
    def size(self) -> int:
        return len(self._entries)

    def put(
        self,
        *,
        key: str,
        value: dict[str, Any],
        source_event_id: str,
        source_sequence: int,
    ) -> ProjectionEntry:
        """写入一条投影。"""
        full_key = self.PREFIX + key
        entry = ProjectionEntry(
            key=full_key,
            value=dict(value),
            source_event_id=source_event_id,
            source_sequence=source_sequence,
        )
        self._entries[full_key] = entry
        self._state = "FRESH"
        return entry

    def get(self, key: str) -> ProjectionEntry | None:
        return self._entries.get(self.PREFIX + key)

    def delete(self, key: str) -> bool:
        full_key = self.PREFIX + key
        if full_key in self._entries:
            del self._entries[full_key]
            return True
        return False

    def clear(self) -> None:
        """模拟 Redis 全丢。"""
        self._entries.clear()
        self._state = "LOST"

    def compute_projection_hash(self) -> str:
        """计算当前投影的 hash（用于验证重建一致性）。"""
        data: list[dict[str, Any]] = []
        for key in sorted(self._entries.keys()):
            entry = self._entries[key]
            data.append(entry.to_dict())
        return hashlib.sha256(canonical_json_bytes(data)).hexdigest()

    def rebuild_from_events(
        self,
        *,
        event_log: WorkEventLog,
        outbox: Outbox,
    ) -> str:
        """从 WorkEventLog + Outbox 重建投影。

        重建是确定性的：相同输入产生相同投影。
        返回重建后的投影 hash。
        """
        self._entries.clear()

        # 从 events 重建
        for event in event_log.events:
            key = f"event:{event.aggregate_id}:{event.sequence}"
            self.put(
                key=key,
                value=event.to_dict(),
                source_event_id=event.event_id,
                source_sequence=event.sequence,
            )

        # 从 outbox 重建
        for msg in outbox.messages:
            key = f"outbox:{msg.aggregate_id}:{msg.sequence}"
            self.put(
                key=key,
                value=msg.to_dict(),
                source_event_id=msg.message_id,
                source_sequence=msg.sequence,
            )

        self._state = "REBUILT"
        return self.compute_projection_hash()

    def verify_rebuild(
        self,
        *,
        event_log: WorkEventLog,
        outbox: Outbox,
        expected_hash: str | None = None,
    ) -> list[tuple[EC, str]]:
        """验证重建的投影与源数据一致。

        如果提供了 expected_hash（丢失前的 hash），验证重建后 hash 一致。
        """
        errors: list[tuple[EC, str]] = []

        # 重建到临时投影
        temp = RedisProjection()
        temp_hash = temp.rebuild_from_events(event_log=event_log, outbox=outbox)

        if expected_hash is not None and temp_hash != expected_hash:
            errors.append(
                (
                    EC.RUNTIME_REDIS_REBUILD_HASH_MISMATCH,
                    f"rebuild hash {temp_hash} != expected {expected_hash}",
                )
            )

        # 验证当前投影与临时投影一致
        current_hash = self.compute_projection_hash()
        if current_hash != temp_hash:
            errors.append(
                (
                    EC.RUNTIME_REDIS_REBUILD_HASH_MISMATCH,
                    f"current projection hash {current_hash} != "
                    f"rebuilt {temp_hash}",
                )
            )

        # 验证每个 event 都有对应投影
        for event in event_log.events:
            key = self.PREFIX + f"event:{event.aggregate_id}:{event.sequence}"
            if key not in self._entries:
                errors.append(
                    (
                        EC.RUNTIME_REDIS_PROJECTION_LOST,
                        f"event {event.event_id} not projected",
                    )
                )

        # 验证每个 outbox 消息都有对应投影
        for msg in outbox.messages:
            key = self.PREFIX + f"outbox:{msg.aggregate_id}:{msg.sequence}"
            if key not in self._entries:
                errors.append(
                    (
                        EC.RUNTIME_REDIS_PROJECTION_LOST,
                        f"outbox message {msg.message_id} not projected",
                    )
                )

        return errors
