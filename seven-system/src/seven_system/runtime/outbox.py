"""Outbox — 与状态事件同一 DB 事务提交。

outbox 与状态事件同一 DB 事务提交，unique key 绑定 aggregate revision。
published/ACK 失败只影响投影，不影响真值；Redis 可从 event/outbox 重建。

不变量：
- outbox 消息与 WorkEvent 在同一事务中写入
- unique key = aggregate_id + sequence（绑定 aggregate revision）
- 重复 unique key 被拒绝
- delivery 是 at-least-once，ACK 是幂等的
- 重复 delivery（相同 unique key 已 ACK）被拒绝（不重复投影）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import OUTBOX_STATES, VerificationErrorCode as EC


class OutboxError(Exception):
    """Outbox 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class OutboxMessage:
    """单条 outbox 消息。"""

    message_id: str
    aggregate_id: str
    sequence: int  # 绑定的 WorkEvent sequence
    unique_key: str  # aggregate_id:sequence
    event_type: str
    payload: dict[str, Any] = field(default_factory=dict)
    payload_hash: str = ""
    created_at: str = ""
    state: str = "PENDING"  # PENDING / DELIVERED / ACKED
    deliver_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "message_id": self.message_id,
            "aggregate_id": self.aggregate_id,
            "sequence": self.sequence,
            "unique_key": self.unique_key,
            "event_type": self.event_type,
            "payload": dict(self.payload),
            "payload_hash": self.payload_hash,
            "created_at": self.created_at,
            "state": self.state,
            "deliver_count": self.deliver_count,
        }


class Outbox:
    """Outbox — 与状态事件同一 DB 事务。

    append 与 WorkEvent.append 必须在同一事务中调用。
    unique_key = aggregate_id:sequence 保证每个 aggregate revision 只有一条 outbox 消息。
    """

    def __init__(self) -> None:
        self._messages: dict[str, OutboxMessage] = {}  # message_id → message
        self._unique_keys: dict[str, str] = {}  # unique_key → message_id
        self._by_aggregate: dict[str, list[str]] = {}  # aggregate_id → [message_id]

    @property
    def messages(self) -> list[OutboxMessage]:
        return list(self._messages.values())

    @property
    def pending(self) -> list[OutboxMessage]:
        return [m for m in self._messages.values() if m.state == "PENDING"]

    @property
    def acked(self) -> list[OutboxMessage]:
        return [m for m in self._messages.values() if m.state == "ACKED"]

    def append(
        self,
        *,
        message_id: str,
        aggregate_id: str,
        sequence: int,
        event_type: str,
        payload: dict[str, Any] | None = None,
        created_at: str | None = None,
    ) -> OutboxMessage:
        """追加一条 outbox 消息。

        与 WorkEvent.append 在同一事务中调用。
        unique_key = aggregate_id:sequence 必须唯一。
        """
        unique_key = f"{aggregate_id}:{sequence}"

        if unique_key in self._unique_keys:
            raise OutboxError(
                EC.OUTBOX_DUPLICATE_KEY,
                f"unique_key {unique_key} already exists",
            )

        if message_id in self._messages:
            raise OutboxError(
                EC.OUTBOX_DUPLICATE_KEY,
                f"message_id {message_id} already exists",
            )

        p = payload or {}
        ph = hashlib.sha256(canonical_json_bytes(p)).hexdigest()
        msg = OutboxMessage(
            message_id=message_id,
            aggregate_id=aggregate_id,
            sequence=sequence,
            unique_key=unique_key,
            event_type=event_type,
            payload=dict(p),
            payload_hash=ph,
            created_at=created_at or datetime.now(timezone.utc).isoformat(),
            state="PENDING",
        )
        self._messages[message_id] = msg
        self._unique_keys[unique_key] = message_id
        self._by_aggregate.setdefault(aggregate_id, []).append(message_id)
        return msg

    def deliver(self, message_id: str) -> OutboxMessage:
        """标记消息为已投递（at-least-once）。

        可以多次 deliver（幂等投递），但 ACK 后不再允许 deliver。
        """
        msg = self._messages.get(message_id)
        if msg is None:
            raise OutboxError(
                EC.OUTBOX_NOT_FOUND,
                f"message {message_id} not found",
            )
        if msg.state == "ACKED":
            raise OutboxError(
                EC.OUTBOX_ALREADY_DELIVERED,
                f"message {message_id} already ACKED",
            )
        msg.deliver_count += 1
        msg.state = "DELIVERED"
        return msg

    def ack(self, message_id: str) -> OutboxMessage:
        """ACK 一条消息（幂等）。

        ACK 后重复 ACK 被拒绝（防止重复投影）。
        """
        msg = self._messages.get(message_id)
        if msg is None:
            raise OutboxError(
                EC.OUTBOX_NOT_FOUND,
                f"message {message_id} not found",
            )
        if msg.state == "ACKED":
            raise OutboxError(
                EC.OUTBOX_REDELIVERY_REJECTED,
                f"message {message_id} already ACKED, "
                f"redelivery rejected to prevent duplicate projection",
            )
        msg.state = "ACKED"
        return msg

    def reject_redelivery(self, unique_key: str) -> bool:
        """拒绝重复投递。

        如果 unique_key 对应的消息已 ACK，返回 True（拒绝重复投递）。
        """
        msg_id = self._unique_keys.get(unique_key)
        if msg_id is None:
            return False
        msg = self._messages.get(msg_id)
        if msg is None:
            return False
        return msg.state == "ACKED"

    def get_message(self, message_id: str) -> OutboxMessage | None:
        return self._messages.get(message_id)

    def get_by_unique_key(self, unique_key: str) -> OutboxMessage | None:
        msg_id = self._unique_keys.get(unique_key)
        if msg_id is None:
            return None
        return self._messages.get(msg_id)

    def get_messages_for_aggregate(self, aggregate_id: str) -> list[OutboxMessage]:
        ids = self._by_aggregate.get(aggregate_id, [])
        return [self._messages[mid] for mid in ids]

    def get_unprojected(self) -> list[OutboxMessage]:
        """获取所有未 ACK 的消息（用于 Redis 重建时补投影）。"""
        return [m for m in self._messages.values() if m.state != "ACKED"]

    def compute_outbox_hash(self) -> str:
        """计算整个 outbox 的 hash（用于 checkpoint）。"""
        data = b""
        for msg in sorted(self._messages.values(), key=lambda m: m.unique_key):
            data += msg.unique_key.encode("utf-8")
            data += msg.state.encode("utf-8")
            data += msg.payload_hash.encode("utf-8")
        return hashlib.sha256(data).hexdigest()
