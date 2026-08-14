"""EpochManager — 多 Epoch 生命周期管理。

来自 WP-OP1：create → seal → next Epoch、跨 Epoch remainder=0。

关键约束（blocker）：
- Epoch 未 seal 就开下一个 → OP_EPOCH_NOT_SEALED
- 跨 Epoch remainder != 0 → OP_CROSS_EPOCH_REMAINDER_NONZERO
- Epoch 状态不在 OP_EPOCH_STATES → OP_EPOCH_STATE_INVALID
- 非法状态转换 → OP_EPOCH_TRANSITION_INVALID
- EpochSealRecord hash 不匹配 → OP_EPOCH_SEAL_HASH_MISMATCH

SIDE_EFFECT_FREE：纯内存模拟。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    OP_EPOCH_STATES,
    OP_EPOCH_TRANSITIONS,
    VerificationErrorCode as EC,
)


class EpochManagerError(Exception):
    """Epoch 管理错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class EpochSealRecord:
    """单个 Epoch 的 seal 记录。

    记录 Epoch seal 时的状态 hash、remainder、work count。
    """

    epoch_id: str
    seal_sequence: int
    state: str  # SEALED
    work_count: int
    remainder: int
    epoch_hash: str
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "epoch_id": self.epoch_id,
            "seal_sequence": self.seal_sequence,
            "state": self.state,
            "work_count": self.work_count,
            "remainder": self.remainder,
            "epoch_hash": self.epoch_hash,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


@dataclass
class EpochState:
    """单个 Epoch 的状态。"""

    epoch_id: str
    state: str = "CREATED"
    work_count: int = 0
    remainder: int = 0
    epoch_hash: str = ""
    seal_record: EpochSealRecord | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "epoch_id": self.epoch_id,
            "state": self.state,
            "work_count": self.work_count,
            "remainder": self.remainder,
            "epoch_hash": self.epoch_hash,
            "seal_record": self.seal_record.to_dict() if self.seal_record else None,
        }


class EpochManager:
    """多 Epoch 生命周期管理器。

    生命周期：CREATED → RUNNING → SEALING → SEALED → SUPERSEDED（下一个 Epoch）
    跨 Epoch remainder=0 验证。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    def __init__(self) -> None:
        self._epochs: dict[str, EpochState] = {}
        self._epoch_order: list[str] = []
        self._seal_records: list[EpochSealRecord] = []
        self._seal_seq: int = 0

    @property
    def epochs(self) -> list[EpochState]:
        return [self._epochs[eid] for eid in self._epoch_order]

    @property
    def seal_records(self) -> list[EpochSealRecord]:
        return list(self._seal_records)

    @property
    def current_epoch_id(self) -> str | None:
        return self._epoch_order[-1] if self._epoch_order else None

    def create_epoch(self, epoch_id: str) -> EpochState:
        """创建新 Epoch。

        前置条件：前一个 Epoch 必须 SEALED（如果有）。
        """
        if epoch_id in self._epochs:
            raise EpochManagerError(
                EC.REQUIRED_FIELD_MISSING,
                f"epoch {epoch_id} already exists",
            )
        # 前一个 Epoch 必须 SEALED
        if self._epoch_order:
            prev = self._epochs[self._epoch_order[-1]]
            if prev.state != "SEALED":
                raise EpochManagerError(
                    EC.OP_EPOCH_NOT_SEALED,
                    f"previous epoch {prev.epoch_id} not sealed "
                    f"(state={prev.state})",
                )
        epoch = EpochState(epoch_id=epoch_id, state="CREATED")
        self._epochs[epoch_id] = epoch
        self._epoch_order.append(epoch_id)
        return epoch

    def _check_transition(self, epoch: EpochState, new_state: str) -> None:
        if epoch.state not in OP_EPOCH_STATES:
            raise EpochManagerError(
                EC.OP_EPOCH_STATE_INVALID,
                f"epoch {epoch.epoch_id} state {epoch.state!r} invalid",
            )
        if new_state not in OP_EPOCH_STATES:
            raise EpochManagerError(
                EC.OP_EPOCH_STATE_INVALID,
                f"new state {new_state!r} invalid",
            )
        if (epoch.state, new_state) not in OP_EPOCH_TRANSITIONS:
            raise EpochManagerError(
                EC.OP_EPOCH_TRANSITION_INVALID,
                f"illegal transition {epoch.state}→{new_state} "
                f"for epoch {epoch.epoch_id}",
            )

    def start_epoch(self, epoch_id: str) -> EpochState:
        """开始 Epoch：CREATED → RUNNING。"""
        epoch = self._epochs.get(epoch_id)
        if epoch is None:
            raise EpochManagerError(
                EC.REQUIRED_FIELD_MISSING,
                f"epoch {epoch_id} not found",
            )
        self._check_transition(epoch, "RUNNING")
        epoch.state = "RUNNING"
        return epoch

    def add_work(self, epoch_id: str, count: int = 1) -> EpochState:
        """向 Epoch 添加 work。"""
        epoch = self._epochs.get(epoch_id)
        if epoch is None:
            raise EpochManagerError(
                EC.REQUIRED_FIELD_MISSING,
                f"epoch {epoch_id} not found",
            )
        if epoch.state != "RUNNING":
            raise EpochManagerError(
                EC.OP_EPOCH_TRANSITION_INVALID,
                f"epoch {epoch_id} not RUNNING, cannot add work",
            )
        epoch.work_count += count
        return epoch

    def set_remainder(self, epoch_id: str, remainder: int) -> EpochState:
        """设置 Epoch 的 remainder。"""
        epoch = self._epochs.get(epoch_id)
        if epoch is None:
            raise EpochManagerError(
                EC.REQUIRED_FIELD_MISSING,
                f"epoch {epoch_id} not found",
            )
        epoch.remainder = remainder
        return epoch

    def seal_epoch(self, epoch_id: str) -> EpochSealRecord:
        """Seal Epoch：RUNNING → SEALING → SEALED。

        生成 EpochSealRecord。
        """
        epoch = self._epochs.get(epoch_id)
        if epoch is None:
            raise EpochManagerError(
                EC.REQUIRED_FIELD_MISSING,
                f"epoch {epoch_id} not found",
            )
        self._check_transition(epoch, "SEALING")
        epoch.state = "SEALING"

        # 计算 epoch hash
        epoch.epoch_hash = self._compute_epoch_hash(epoch)

        self._check_transition(epoch, "SEALED")
        epoch.state = "SEALED"

        self._seal_seq += 1
        record = EpochSealRecord(
            epoch_id=epoch_id,
            seal_sequence=self._seal_seq,
            state="SEALED",
            work_count=epoch.work_count,
            remainder=epoch.remainder,
            epoch_hash=epoch.epoch_hash,
        )
        record.content_hash = record.compute_content_hash()
        epoch.seal_record = record
        self._seal_records.append(record)
        return record

    def supersede_epoch(self, epoch_id: str) -> EpochState:
        """将已 seal 的 Epoch 标记为 SUPERSEDED（被下一个 Epoch 取代）。"""
        epoch = self._epochs.get(epoch_id)
        if epoch is None:
            raise EpochManagerError(
                EC.REQUIRED_FIELD_MISSING,
                f"epoch {epoch_id} not found",
            )
        self._check_transition(epoch, "SUPERSEDED")
        epoch.state = "SUPERSEDED"
        return epoch

    def _compute_epoch_hash(self, epoch: EpochState) -> str:
        """计算 Epoch 的 hash。"""
        data = {
            "epoch_id": epoch.epoch_id,
            "work_count": epoch.work_count,
            "remainder": epoch.remainder,
        }
        return hashlib.sha256(canonical_json_bytes(data)).hexdigest()

    def verify_cross_epoch_remainder_zero(self) -> list[tuple[EC, str]]:
        """验证跨 Epoch remainder=0。

        所有已 seal 的 Epoch 的 remainder 之和必须为 0。
        """
        errors: list[tuple[EC, str]] = []
        total = 0
        for record in self._seal_records:
            total += record.remainder
            if record.remainder != 0:
                errors.append((
                    EC.OP_CROSS_EPOCH_REMAINDER_NONZERO,
                    f"epoch {record.epoch_id} remainder "
                    f"{record.remainder} != 0",
                ))
        if total != 0:
            errors.append((
                EC.OP_CROSS_EPOCH_REMAINDER_NONZERO,
                f"cross-epoch total remainder {total} != 0",
            ))
        return errors

    def verify_epoch_sealed_before_next(self) -> list[tuple[EC, str]]:
        """验证每个 Epoch 在下一个 Epoch 创建前已 seal。"""
        errors: list[tuple[EC, str]] = []
        for i, eid in enumerate(self._epoch_order[:-1]):
            epoch = self._epochs[eid]
            next_eid = self._epoch_order[i + 1]
            if epoch.state != "SEALED" and epoch.state != "SUPERSEDED":
                errors.append((
                    EC.OP_EPOCH_NOT_SEALED,
                    f"epoch {eid} not sealed before "
                    f"epoch {next_eid} created "
                    f"(state={epoch.state})",
                ))
        return errors

    def verify_seal_record_hashes(self) -> list[tuple[EC, str]]:
        """验证所有 EpochSealRecord 的 hash 有效。"""
        errors: list[tuple[EC, str]] = []
        for record in self._seal_records:
            if not record.is_hash_valid:
                errors.append((
                    EC.OP_EPOCH_SEAL_HASH_MISMATCH,
                    f"EpochSealRecord {record.epoch_id} content_hash invalid",
                ))
            # 验证 epoch_hash 一致
            epoch = self._epochs.get(record.epoch_id)
            if epoch and epoch.epoch_hash != record.epoch_hash:
                errors.append((
                    EC.OP_EPOCH_SEAL_HASH_MISMATCH,
                    f"epoch {record.epoch_id} hash mismatch: "
                    f"epoch={epoch.epoch_hash} record={record.epoch_hash}",
                ))
        return errors

    def verify_epoch_states(self) -> list[tuple[EC, str]]:
        """验证所有 Epoch 状态合法。"""
        errors: list[tuple[EC, str]] = []
        for epoch in self._epochs.values():
            if epoch.state not in OP_EPOCH_STATES:
                errors.append((
                    EC.OP_EPOCH_STATE_INVALID,
                    f"epoch {epoch.epoch_id} state {epoch.state!r} invalid",
                ))
        return errors
