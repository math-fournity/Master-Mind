"""WorkEvent — append-only event sourcing for Work state.

Work 状态只由 append-only event 推导。每个 event 至少包含：
  event_id, aggregate_id, expected_previous_sequence, sequence,
  event_type, payload_hash, fence_token, created_at, actor_or_rule

不变量：
- sequence 单调递增，从 0 开始
- expected_previous_sequence 必须等于前一个 event 的 sequence
- event_id 全局唯一（重复 event_id 拒绝）
- append-only：已写入的 event 不可修改或删除
- fence_token 绑定 lease，stale fence 的 event 被拒绝
- payload_hash 绑定 event payload 的 canonical JSON hash

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    WORK_EVENT_TYPES,
    VerificationErrorCode as EC,
)


@dataclass(frozen=True)
class WorkEvent:
    """单个 append-only WorkEvent。

    不可变。一旦创建不可修改。
    """

    event_id: str
    aggregate_id: str
    expected_previous_sequence: int
    sequence: int
    event_type: str
    payload_hash: str
    fence_token: int
    created_at: str
    actor_or_rule: str
    payload: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "aggregate_id": self.aggregate_id,
            "expected_previous_sequence": self.expected_previous_sequence,
            "sequence": self.sequence,
            "event_type": self.event_type,
            "payload_hash": self.payload_hash,
            "fence_token": self.fence_token,
            "created_at": self.created_at,
            "actor_or_rule": self.actor_or_rule,
            "payload": dict(self.payload),
        }

    @classmethod
    def build(
        cls,
        *,
        event_id: str,
        aggregate_id: str,
        sequence: int,
        event_type: str,
        fence_token: int,
        actor_or_rule: str,
        payload: dict[str, Any] | None = None,
        expected_previous_sequence: int | None = None,
        created_at: str | None = None,
    ) -> "WorkEvent":
        """构建 WorkEvent 并计算 payload_hash。"""
        p = payload or {}
        ph = hashlib.sha256(canonical_json_bytes(p)).hexdigest()
        eps = (
            expected_previous_sequence
            if expected_previous_sequence is not None
            else sequence - 1
        )
        return cls(
            event_id=event_id,
            aggregate_id=aggregate_id,
            expected_previous_sequence=eps,
            sequence=sequence,
            event_type=event_type,
            payload_hash=ph,
            fence_token=fence_token,
            created_at=created_at or datetime.now(timezone.utc).isoformat(),
            actor_or_rule=actor_or_rule,
            payload=dict(p),
        )


class WorkEventError(Exception):
    """WorkEvent 追加错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


class WorkEventLog:
    """Append-only WorkEvent 日志。

    所有状态由 event 序列推导。不允许修改、删除或重排已写入的 event。
    """

    def __init__(self) -> None:
        self._events: list[WorkEvent] = []
        self._event_ids: set[str] = set()
        self._by_aggregate: dict[str, list[WorkEvent]] = {}

    @property
    def events(self) -> list[WorkEvent]:
        return list(self._events)

    @property
    def length(self) -> int:
        return len(self._events)

    def append(self, event: WorkEvent) -> WorkEvent:
        """追加一个 event。

        验证：
        1. event_id 不重复
        2. event_type 合法
        3. sequence 连续（expected_previous_sequence == 前一个 sequence）
        4. fence_token 有效（由调用方通过 current_fence 检查）
        5. payload_hash 匹配
        """
        # 1. event_id 唯一
        if event.event_id in self._event_ids:
            raise WorkEventError(
                EC.WORK_EVENT_DUPLICATE_EVENT_ID,
                f"event_id {event.event_id} already exists",
            )

        # 2. event_type 合法
        if event.event_type not in WORK_EVENT_TYPES:
            raise WorkEventError(
                EC.WORK_EVENT_APPEND_ONLY_VIOLATION,
                f"unknown event_type {event.event_type}",
            )

        # 3. sequence 连续
        agg_events = self._by_aggregate.get(event.aggregate_id, [])
        if agg_events:
            last = agg_events[-1]
            if event.expected_previous_sequence != last.sequence:
                raise WorkEventError(
                    EC.WORK_EVENT_SEQUENCE_GAP,
                    f"expected_previous_sequence {event.expected_previous_sequence} "
                    f"!= last sequence {last.sequence} for aggregate "
                    f"{event.aggregate_id}",
                )
            if event.sequence != last.sequence + 1:
                raise WorkEventError(
                    EC.WORK_EVENT_SEQUENCE_GAP,
                    f"sequence {event.sequence} != expected "
                    f"{last.sequence + 1} for aggregate {event.aggregate_id}",
                )
        else:
            if event.sequence != 0:
                raise WorkEventError(
                    EC.WORK_EVENT_SEQUENCE_GAP,
                    f"first event for aggregate {event.aggregate_id} "
                    f"must have sequence 0, got {event.sequence}",
                )
            if event.expected_previous_sequence != -1:
                raise WorkEventError(
                    EC.WORK_EVENT_SEQUENCE_GAP,
                    f"first event expected_previous_sequence must be -1, "
                    f"got {event.expected_previous_sequence}",
                )

        # 4. payload_hash 验证
        actual_hash = hashlib.sha256(
            canonical_json_bytes(event.payload)
        ).hexdigest()
        if actual_hash != event.payload_hash:
            raise WorkEventError(
                EC.WORK_EVENT_PAYLOAD_HASH_MISMATCH,
                f"payload_hash mismatch: expected {event.payload_hash}, "
                f"got {actual_hash}",
            )

        # 追加
        self._events.append(event)
        self._event_ids.add(event.event_id)
        self._by_aggregate.setdefault(event.aggregate_id, []).append(event)
        return event

    def get_events_for_aggregate(self, aggregate_id: str) -> list[WorkEvent]:
        """获取某个 aggregate 的所有 event（按 sequence 排序）。"""
        return list(self._by_aggregate.get(aggregate_id, []))

    def get_last_sequence(self, aggregate_id: str) -> int:
        """获取某个 aggregate 的最后一个 sequence。无 event 时返回 -1。"""
        events = self._by_aggregate.get(aggregate_id, [])
        return events[-1].sequence if events else -1

    def get_event(self, event_id: str) -> WorkEvent | None:
        """按 event_id 查找 event。"""
        for e in self._events:
            if e.event_id == event_id:
                return e
        return None

    def verify_integrity(self) -> list[tuple[EC, str]]:
        """验证整个日志的完整性。

        检查：
        - sequence 连续
        - event_id 唯一
        - payload_hash 匹配
        """
        errors: list[tuple[EC, str]] = []
        seen_ids: set[str] = set()
        agg_last: dict[str, int] = {}

        for event in self._events:
            # event_id 唯一
            if event.event_id in seen_ids:
                errors.append(
                    (EC.WORK_EVENT_DUPLICATE_EVENT_ID, f"duplicate {event.event_id}")
                )
                continue
            seen_ids.add(event.event_id)

            # sequence 连续
            last_seq = agg_last.get(event.aggregate_id, -1)
            if event.sequence != last_seq + 1:
                errors.append(
                    (
                        EC.WORK_EVENT_SEQUENCE_GAP,
                        f"aggregate {event.aggregate_id}: "
                        f"sequence {event.sequence} != {last_seq + 1}",
                    )
                )
            agg_last[event.aggregate_id] = event.sequence

            # payload_hash
            actual = hashlib.sha256(
                canonical_json_bytes(event.payload)
            ).hexdigest()
            if actual != event.payload_hash:
                errors.append(
                    (
                        EC.WORK_EVENT_PAYLOAD_HASH_MISMATCH,
                        f"event {event.event_id} payload_hash mismatch",
                    )
                )

        return errors

    def compute_log_hash(self) -> str:
        """计算整个日志的 root hash（用于 checkpoint）。

        每个事件的 hash = sha256(prev_hash || event_id || sequence || payload_hash)
        """
        prev = b""
        for event in self._events:
            data = (
                prev
                + event.event_id.encode("utf-8")
                + str(event.sequence).encode("utf-8")
                + event.payload_hash.encode("utf-8")
            )
            prev = hashlib.sha256(data).digest()
        return hashlib.sha256(prev).hexdigest()
