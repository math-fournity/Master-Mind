"""RuntimeCheckpoint + recovery receipts。

Checkpoint 绑定 event log root hash、outbox hash、lease 状态和
aggregate revisions，用于崩溃恢复。

恢复流程：
1. 加载 checkpoint
2. 重放 WorkEvent log（验证完整性）
3. 检查 outbox 未 ACK 消息（补投递）
4. 检查 lease 过期/stale
5. 运行 reconcile
6. 生成 RuntimeRecoveryReceipt

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    RUNTIME_CHECKPOINT_STATES,
    VerificationErrorCode as EC,
)
from .work_event import WorkEventLog
from .outbox import Outbox
from .lease_fence import LeaseFenceManager


class CheckpointError(Exception):
    """Checkpoint 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class RuntimeCheckpoint:
    """Runtime checkpoint — 绑定运行时状态 hash。"""

    checkpoint_id: str
    created_at: str
    event_log_hash: str
    outbox_hash: str
    lease_snapshot: dict[str, Any]
    aggregate_revisions: dict[str, int]
    event_count: int
    outbox_count: int
    state: str = "RECORDED"

    def to_dict(self) -> dict[str, Any]:
        return {
            "checkpoint_id": self.checkpoint_id,
            "created_at": self.created_at,
            "event_log_hash": self.event_log_hash,
            "outbox_hash": self.outbox_hash,
            "lease_snapshot": dict(self.lease_snapshot),
            "aggregate_revisions": dict(self.aggregate_revisions),
            "event_count": self.event_count,
            "outbox_count": self.outbox_count,
            "state": self.state,
        }

    @property
    def is_verified(self) -> bool:
        return self.state == "VERIFIED"

    @property
    def is_recovered(self) -> bool:
        return self.state == "RECOVERED"


@dataclass
class RuntimeRecoveryReceipt:
    """恢复收据 — 记录恢复过程的结果。"""

    receipt_id: str
    checkpoint_id: str
    recovered_at: str
    event_log_verified: bool
    outbox_redelivered: list[str]  # message_ids
    leases_expired: list[str]  # lease_ids
    leases_stale: list[str]  # lease_ids with stale fence
    aggregate_revisions_restored: dict[str, int]
    errors: list[tuple[str, str]] = field(default_factory=list)  # (error_code, detail)
    state: str = "RECOVERED"  # RECOVERED / FAILED

    def to_dict(self) -> dict[str, Any]:
        return {
            "receipt_id": self.receipt_id,
            "checkpoint_id": self.checkpoint_id,
            "recovered_at": self.recovered_at,
            "event_log_verified": self.event_log_verified,
            "outbox_redelivered": list(self.outbox_redelivered),
            "leases_expired": list(self.leases_expired),
            "leases_stale": list(self.leases_stale),
            "aggregate_revisions_restored": dict(
                self.aggregate_revisions_restored
            ),
            "errors": [(ec, d) for ec, d in self.errors],
            "state": self.state,
        }

    @property
    def is_recovered(self) -> bool:
        return self.state == "RECOVERED"


class CheckpointManager:
    """Checkpoint 管理器 — 创建、验证、恢复。"""

    def __init__(self) -> None:
        self._checkpoints: dict[str, RuntimeCheckpoint] = {}
        self._receipts: dict[str, RuntimeRecoveryReceipt] = {}

    @property
    def checkpoints(self) -> list[RuntimeCheckpoint]:
        return list(self._checkpoints.values())

    @property
    def receipts(self) -> list[RuntimeRecoveryReceipt]:
        return list(self._receipts.values())

    def create_checkpoint(
        self,
        *,
        checkpoint_id: str,
        event_log: WorkEventLog,
        outbox: Outbox,
        lease_manager: LeaseFenceManager,
        aggregate_revisions: dict[str, int],
        created_at: str | None = None,
    ) -> RuntimeCheckpoint:
        """创建一个 checkpoint。"""
        if checkpoint_id in self._checkpoints:
            raise CheckpointError(
                EC.RUNTIME_CHECKPOINT_INCOMPLETE,
                f"checkpoint {checkpoint_id} already exists",
            )

        event_log_hash = event_log.compute_log_hash()
        outbox_hash = outbox.compute_outbox_hash()

        # lease snapshot
        lease_snapshot: dict[str, Any] = {}
        for lease in lease_manager.leases:
            lease_snapshot[lease.lease_id] = lease.to_dict()

        checkpoint = RuntimeCheckpoint(
            checkpoint_id=checkpoint_id,
            created_at=created_at or datetime.now(timezone.utc).isoformat(),
            event_log_hash=event_log_hash,
            outbox_hash=outbox_hash,
            lease_snapshot=lease_snapshot,
            aggregate_revisions=dict(aggregate_revisions),
            event_count=event_log.length,
            outbox_count=len(outbox.messages),
            state="RECORDED",
        )
        self._checkpoints[checkpoint_id] = checkpoint
        return checkpoint

    def verify_checkpoint(
        self,
        *,
        checkpoint_id: str,
        event_log: WorkEventLog,
        outbox: Outbox,
    ) -> RuntimeCheckpoint:
        """验证一个 checkpoint 的完整性。"""
        checkpoint = self._checkpoints.get(checkpoint_id)
        if checkpoint is None:
            raise CheckpointError(
                EC.RUNTIME_CHECKPOINT_INCOMPLETE,
                f"checkpoint {checkpoint_id} not found",
            )

        errors: list[tuple[EC, str]] = []

        # 验证 event log hash
        current_log_hash = event_log.compute_log_hash()
        if current_log_hash != checkpoint.event_log_hash:
            errors.append(
                (
                    EC.RUNTIME_CHECKPOINT_HASH_MISMATCH,
                    f"event_log_hash mismatch: "
                    f"checkpoint={checkpoint.event_log_hash}, "
                    f"current={current_log_hash}",
                )
            )

        # 验证 event log 完整性
        integrity_errors = event_log.verify_integrity()
        errors.extend(integrity_errors)

        # 验证 outbox hash
        current_outbox_hash = outbox.compute_outbox_hash()
        if current_outbox_hash != checkpoint.outbox_hash:
            errors.append(
                (
                    EC.RUNTIME_CHECKPOINT_HASH_MISMATCH,
                    f"outbox_hash mismatch: "
                    f"checkpoint={checkpoint.outbox_hash}, "
                    f"current={current_outbox_hash}",
                )
            )

        # 验证 event count
        if event_log.length != checkpoint.event_count:
            errors.append(
                (
                    EC.RUNTIME_CHECKPOINT_INCOMPLETE,
                    f"event_count mismatch: "
                    f"checkpoint={checkpoint.event_count}, "
                    f"current={event_log.length}",
                )
            )

        if errors:
            checkpoint.state = "INCOMPLETE"
            raise CheckpointError(
                errors[0][0],
                f"checkpoint {checkpoint_id} verification failed: "
                + "; ".join(f"{e[0].value}:{e[1]}" for e in errors),
            )

        checkpoint.state = "VERIFIED"
        return checkpoint

    def recover(
        self,
        *,
        receipt_id: str,
        checkpoint_id: str,
        event_log: WorkEventLog,
        outbox: Outbox,
        lease_manager: LeaseFenceManager,
        current_time: str,
    ) -> RuntimeRecoveryReceipt:
        """从 checkpoint 恢复。

        1. 验证 checkpoint
        2. 重放 event log
        3. 补投递 outbox 未 ACK 消息
        4. 过期 stale lease
        5. 生成 recovery receipt
        """
        checkpoint = self._checkpoints.get(checkpoint_id)
        if checkpoint is None:
            raise CheckpointError(
                EC.RUNTIME_CHECKPOINT_INCOMPLETE,
                f"checkpoint {checkpoint_id} not found",
            )

        errors: list[tuple[str, str]] = []
        event_log_verified = True
        outbox_redelivered: list[str] = []
        leases_expired: list[str] = []
        leases_stale: list[str] = []

        # 1. 验证 event log 完整性
        integrity_errors = event_log.verify_integrity()
        if integrity_errors:
            event_log_verified = False
            for ec, detail in integrity_errors:
                errors.append((ec.value, detail))

        # 2. 验证 event log hash
        current_log_hash = event_log.compute_log_hash()
        if current_log_hash != checkpoint.event_log_hash:
            event_log_verified = False
            errors.append(
                (
                    EC.RUNTIME_CHECKPOINT_HASH_MISMATCH.value,
                    f"event_log_hash mismatch after recovery",
                )
            )

        # 3. 补投递 outbox 未 ACK 消息
        for msg in outbox.get_unprojected():
            try:
                outbox.deliver(msg.message_id)
                outbox_redelivered.append(msg.message_id)
            except Exception as e:
                errors.append(
                    (EC.RUNTIME_RECOVERY_FAILED.value, str(e))
                )

        # 4. 过期 stale lease
        expired = lease_manager.expire_stale(current_time)
        leases_expired = expired

        # 5. 检查 stale fence lease
        for lease in lease_manager.leases:
            current_fence = lease_manager.get_current_fence(lease.aggregate_id)
            if lease.fence_token < current_fence and lease.state == "ACTIVE":
                leases_stale.append(lease.lease_id)

        # 6. 恢复 aggregate revisions
        aggregate_revisions_restored = dict(checkpoint.aggregate_revisions)

        state = "RECOVERED" if not errors else "FAILED"

        receipt = RuntimeRecoveryReceipt(
            receipt_id=receipt_id,
            checkpoint_id=checkpoint_id,
            recovered_at=current_time,
            event_log_verified=event_log_verified,
            outbox_redelivered=outbox_redelivered,
            leases_expired=leases_expired,
            leases_stale=leases_stale,
            aggregate_revisions_restored=aggregate_revisions_restored,
            errors=errors,
            state=state,
        )
        self._receipts[receipt_id] = receipt

        if state == "RECOVERED":
            checkpoint.state = "RECOVERED"

        return receipt

    def get_checkpoint(self, checkpoint_id: str) -> RuntimeCheckpoint | None:
        return self._checkpoints.get(checkpoint_id)

    def get_receipt(self, receipt_id: str) -> RuntimeRecoveryReceipt | None:
        return self._receipts.get(receipt_id)
