"""CrossEpochBudgetLedger — 跨 Epoch 预算追踪。

来自 WP-OP1：cross-Epoch budget、budget 不在 Epoch 间重置、
holdout 消费跨 Epoch 追踪（无 holdout 重用）。

关键约束（blocker）：
- budget 不守恒 → OP_BUDGET_NOT_CONSERVED
- holdout 跨 Epoch 重用 → OP_HOLDOUT_REUSE_ACROSS_EPOCHS
- budget kind 不在 OP_BUDGET_KINDS → OP_BUDGET_KIND_INVALID

SIDE_EFFECT_FREE：纯内存模拟。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    OP_BUDGET_KINDS,
    VerificationErrorCode as EC,
)


class BudgetLedgerError(Exception):
    """Budget ledger 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class BudgetEntry:
    """单条 budget 消费记录。"""

    epoch_id: str
    budget_kind: str
    allocated: int
    consumed: int
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "epoch_id": self.epoch_id,
            "budget_kind": self.budget_kind,
            "allocated": self.allocated,
            "consumed": self.consumed,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()

    @property
    def remainder(self) -> int:
        return self.allocated - self.consumed


@dataclass
class HoldoutConsumptionEntry:
    """跨 Epoch holdout 消费记录。"""

    epoch_id: str
    holdout_id: str
    case_ids: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "epoch_id": self.epoch_id,
            "holdout_id": self.holdout_id,
            "case_ids": list(self.case_ids),
        }


@dataclass
class CrossEpochBudgetLedger:
    """跨 Epoch 预算账本。

    budget 不在 Epoch 间重置——全局累计。
    holdout 消费跨 Epoch 追踪——同一 holdout 不得跨 Epoch 重用。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    ledger_id: str
    entries: list[BudgetEntry] = field(default_factory=list)
    holdout_consumptions: list[HoldoutConsumptionEntry] = field(default_factory=list)
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "ledger_id": self.ledger_id,
            "entries": [e.to_dict() for e in self.entries],
            "holdout_consumptions": [
                h.to_dict() for h in self.holdout_consumptions
            ],
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
class GlobalBudgetLedger:
    """全局预算账本——所有 Epoch 的 budget 汇总。

    budget 不在 Epoch 间重置。
    """

    ledger_id: str
    global_allocated: dict[str, int] = field(default_factory=dict)
    global_consumed: dict[str, int] = field(default_factory=dict)
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "ledger_id": self.ledger_id,
            "global_allocated": dict(self.global_allocated),
            "global_consumed": dict(self.global_consumed),
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


class CrossEpochBudgetLedgerManager:
    """跨 Epoch budget ledger 管理器。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    def __init__(self, ledger_id: str) -> None:
        self._ledger = CrossEpochBudgetLedger(ledger_id=ledger_id)
        self._global = GlobalBudgetLedger(ledger_id=f"global:{ledger_id}")
        self._holdout_seen: dict[str, str] = {}  # holdout_id → first epoch

    @property
    def ledger(self) -> CrossEpochBudgetLedger:
        return self._ledger

    @property
    def global_ledger(self) -> GlobalBudgetLedger:
        return self._global

    def add_entry(
        self,
        *,
        epoch_id: str,
        budget_kind: str,
        allocated: int,
        consumed: int,
    ) -> BudgetEntry:
        """添加一条 budget 消费记录。"""
        if budget_kind not in OP_BUDGET_KINDS:
            raise BudgetLedgerError(
                EC.OP_BUDGET_KIND_INVALID,
                f"budget_kind {budget_kind!r} not in OP_BUDGET_KINDS",
            )
        if consumed > allocated:
            raise BudgetLedgerError(
                EC.OP_BUDGET_NOT_CONSERVED,
                f"consumed {consumed} > allocated {allocated}",
            )
        entry = BudgetEntry(
            epoch_id=epoch_id,
            budget_kind=budget_kind,
            allocated=allocated,
            consumed=consumed,
        )
        entry.content_hash = entry.compute_content_hash()
        self._ledger.entries.append(entry)

        # 更新全局
        self._global.global_allocated[budget_kind] = (
            self._global.global_allocated.get(budget_kind, 0) + allocated
        )
        self._global.global_consumed[budget_kind] = (
            self._global.global_consumed.get(budget_kind, 0) + consumed
        )
        return entry

    def record_holdout_consumption(
        self,
        *,
        epoch_id: str,
        holdout_id: str,
        case_ids: list[str],
    ) -> HoldoutConsumptionEntry:
        """记录 holdout 消费。

        blocker：同一 holdout 跨 Epoch 重用 → OP_HOLDOUT_REUSE_ACROSS_EPOCHS
        """
        if holdout_id in self._holdout_seen:
            first_epoch = self._holdout_seen[holdout_id]
            if first_epoch != epoch_id:
                raise BudgetLedgerError(
                    EC.OP_HOLDOUT_REUSE_ACROSS_EPOCHS,
                    f"holdout {holdout_id} consumed in epoch "
                    f"{first_epoch}, reused in epoch {epoch_id}",
                )
        self._holdout_seen[holdout_id] = epoch_id
        entry = HoldoutConsumptionEntry(
            epoch_id=epoch_id,
            holdout_id=holdout_id,
            case_ids=list(case_ids),
        )
        self._ledger.holdout_consumptions.append(entry)
        return entry

    def finalize(self) -> None:
        """计算 ledger 和 global ledger 的 content_hash。"""
        self._ledger.content_hash = self._ledger.compute_content_hash()
        self._global.content_hash = self._global.compute_content_hash()

    def verify_budget_conserved(self) -> list[tuple[EC, str]]:
        """验证 budget 守恒：consumed <= allocated（全局）。"""
        errors: list[tuple[EC, str]] = []
        for kind in self._global.global_allocated:
            allocated = self._global.global_allocated[kind]
            consumed = self._global.global_consumed.get(kind, 0)
            if consumed > allocated:
                errors.append((
                    EC.OP_BUDGET_NOT_CONSERVED,
                    f"budget {kind}: consumed {consumed} > "
                    f"allocated {allocated}",
                ))
        # 验证每条 entry
        for entry in self._ledger.entries:
            if entry.consumed > entry.allocated:
                errors.append((
                    EC.OP_BUDGET_NOT_CONSERVED,
                    f"epoch {entry.epoch_id} {entry.budget_kind}: "
                    f"consumed {entry.consumed} > allocated "
                    f"{entry.allocated}",
                ))
        return errors

    def verify_no_holdout_reuse(self) -> list[tuple[EC, str]]:
        """验证无 holdout 跨 Epoch 重用。"""
        errors: list[tuple[EC, str]] = []
        seen: dict[str, str] = {}
        for h in self._ledger.holdout_consumptions:
            if h.holdout_id in seen and seen[h.holdout_id] != h.epoch_id:
                errors.append((
                    EC.OP_HOLDOUT_REUSE_ACROSS_EPOCHS,
                    f"holdout {h.holdout_id} consumed in epoch "
                    f"{seen[h.holdout_id]} and epoch {h.epoch_id}",
                ))
            seen[h.holdout_id] = h.epoch_id
        return errors

    def verify_hashes(self) -> list[tuple[EC, str]]:
        """验证 ledger hash 有效。"""
        errors: list[tuple[EC, str]] = []
        if not self._ledger.is_hash_valid:
            errors.append((
                EC.OP_BUDGET_LEDGER_HASH_MISMATCH,
                "CrossEpochBudgetLedger content_hash invalid",
            ))
        if not self._global.is_hash_valid:
            errors.append((
                EC.OP_BUDGET_LEDGER_HASH_MISMATCH,
                "GlobalBudgetLedger content_hash invalid",
            ))
        for entry in self._ledger.entries:
            if not entry.is_hash_valid:
                errors.append((
                    EC.OP_BUDGET_LEDGER_HASH_MISMATCH,
                    f"BudgetEntry {entry.epoch_id}/{entry.budget_kind} "
                    f"content_hash invalid",
                ))
        return errors
