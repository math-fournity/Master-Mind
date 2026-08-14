"""ActiveLearningScheduler — 跨 Epoch active learning。

来自 WP-OP1：多 Epoch/active learning、CoverageTensor、EpochSelectionRecord。

这是跨 Epoch 的 active learning——根据 evidence gap 选择下一个 coverage cell。
NOT 单 Epoch P9（那是 VR1）。

关键约束（blocker）：
- CoverageTensor 无效 → OP_COVERAGE_TENSOR_INVALID
- EpochSelectionRecord 无效 → OP_SELECTION_RECORD_INVALID
- Coverage delta 无效 → OP_COVERAGE_DELTA_INVALID

SIDE_EFFECT_FREE：纯内存模拟。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


class ActiveLearningError(Exception):
    """Active learning 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class CoverageTensorSnapshot:
    """Coverage tensor 快照——记录每个 coverage cell 的证据覆盖状态。

    coverage_cells: {cell_id: evidence_count}
    """

    snapshot_id: str
    epoch_id: str
    coverage_cells: dict[str, int] = field(default_factory=dict)
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "snapshot_id": self.snapshot_id,
            "epoch_id": self.epoch_id,
            "coverage_cells": dict(self.coverage_cells),
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
    def total_coverage(self) -> int:
        return sum(self.coverage_cells.values())

    @property
    def covered_cells(self) -> int:
        return sum(1 for c in self.coverage_cells.values() if c > 0)

    @property
    def gap_cells(self) -> list[str]:
        return [k for k, v in self.coverage_cells.items() if v == 0]


@dataclass
class CoverageTensorDelta:
    """两个 CoverageTensorSnapshot 之间的 delta。"""

    delta_id: str
    from_snapshot_id: str
    to_snapshot_id: str
    new_cells: list[str] = field(default_factory=list)
    increased_cells: dict[str, int] = field(default_factory=dict)
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "delta_id": self.delta_id,
            "from_snapshot_id": self.from_snapshot_id,
            "to_snapshot_id": self.to_snapshot_id,
            "new_cells": list(self.new_cells),
            "increased_cells": dict(self.increased_cells),
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
class EpochSelectionRecord:
    """单个 Epoch 的 selection 记录——选择了哪些 coverage cell。"""

    selection_id: str
    epoch_id: str
    selected_cells: list[str] = field(default_factory=list)
    selection_reason: str = ""
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "selection_id": self.selection_id,
            "epoch_id": self.epoch_id,
            "selected_cells": list(self.selected_cells),
            "selection_reason": self.selection_reason,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


class ActiveLearningScheduler:
    """跨 Epoch active learning 调度器。

    根据 evidence gap 选择下一个 coverage cell。
    维护 CoverageTensorSnapshot 序列和 EpochSelectionRecord。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    def __init__(self) -> None:
        self._snapshots: list[CoverageTensorSnapshot] = []
        self._deltas: list[CoverageTensorDelta] = []
        self._selections: list[EpochSelectionRecord] = []
        self._all_cells: set[str] = set()

    @property
    def snapshots(self) -> list[CoverageTensorSnapshot]:
        return list(self._snapshots)

    @property
    def deltas(self) -> list[CoverageTensorDelta]:
        return list(self._deltas)

    @property
    def selections(self) -> list[EpochSelectionRecord]:
        return list(self._selections)

    def register_cells(self, cell_ids: list[str]) -> None:
        """注册所有 coverage cell。"""
        self._all_cells.update(cell_ids)

    def take_snapshot(
        self,
        *,
        snapshot_id: str,
        epoch_id: str,
        coverage_cells: dict[str, int],
    ) -> CoverageTensorSnapshot:
        """拍摄 CoverageTensor 快照。"""
        snap = CoverageTensorSnapshot(
            snapshot_id=snapshot_id,
            epoch_id=epoch_id,
            coverage_cells=dict(coverage_cells),
        )
        snap.content_hash = snap.compute_content_hash()
        self._snapshots.append(snap)
        return snap

    def compute_delta(
        self,
        *,
        delta_id: str,
        from_snap: CoverageTensorSnapshot,
        to_snap: CoverageTensorSnapshot,
    ) -> CoverageTensorDelta:
        """计算两个快照之间的 delta。"""
        new_cells: list[str] = []
        increased: dict[str, int] = {}
        all_keys = set(from_snap.coverage_cells) | set(to_snap.coverage_cells)
        for k in sorted(all_keys):
            old = from_snap.coverage_cells.get(k, 0)
            new = to_snap.coverage_cells.get(k, 0)
            if old == 0 and new > 0:
                new_cells.append(k)
            elif new > old:
                increased[k] = new - old
        delta = CoverageTensorDelta(
            delta_id=delta_id,
            from_snapshot_id=from_snap.snapshot_id,
            to_snapshot_id=to_snap.snapshot_id,
            new_cells=new_cells,
            increased_cells=increased,
        )
        delta.content_hash = delta.compute_content_hash()
        self._deltas.append(delta)
        return delta

    def select_next_cells(
        self,
        *,
        selection_id: str,
        epoch_id: str,
        snapshot: CoverageTensorSnapshot,
        max_cells: int = 5,
    ) -> EpochSelectionRecord:
        """根据 evidence gap 选择下一个 coverage cell。

        选择策略：优先选择 evidence_count=0 的 gap cell。
        """
        gaps = snapshot.gap_cells
        selected = sorted(gaps)[:max_cells]
        record = EpochSelectionRecord(
            selection_id=selection_id,
            epoch_id=epoch_id,
            selected_cells=selected,
            selection_reason="evidence_gap" if selected else "no_gaps",
        )
        record.content_hash = record.compute_content_hash()
        self._selections.append(record)
        return record

    def verify_coverage_tensor(
        self,
        snapshot: CoverageTensorSnapshot,
    ) -> list[tuple[EC, str]]:
        """验证 CoverageTensorSnapshot。"""
        errors: list[tuple[EC, str]] = []
        if not snapshot.snapshot_id:
            errors.append((EC.OP_COVERAGE_TENSOR_INVALID, "snapshot_id empty"))
        if not snapshot.epoch_id:
            errors.append((EC.OP_COVERAGE_TENSOR_INVALID, "epoch_id empty"))
        for cell, count in snapshot.coverage_cells.items():
            if not isinstance(count, int) or count < 0:
                errors.append((
                    EC.OP_COVERAGE_TENSOR_INVALID,
                    f"cell {cell} count {count} invalid",
                ))
        if not snapshot.is_hash_valid:
            errors.append((
                EC.OP_COVERAGE_TENSOR_INVALID,
                f"snapshot {snapshot.snapshot_id} content_hash invalid",
            ))
        return errors

    def verify_selection_record(
        self,
        record: EpochSelectionRecord,
    ) -> list[tuple[EC, str]]:
        """验证 EpochSelectionRecord。"""
        errors: list[tuple[EC, str]] = []
        if not record.selection_id:
            errors.append((EC.OP_SELECTION_RECORD_INVALID, "selection_id empty"))
        if not record.epoch_id:
            errors.append((EC.OP_SELECTION_RECORD_INVALID, "epoch_id empty"))
        if not record.selection_reason:
            errors.append((
                EC.OP_SELECTION_RECORD_INVALID,
                "selection_reason empty",
            ))
        if not record.is_hash_valid:
            errors.append((
                EC.OP_SELECTION_RECORD_INVALID,
                f"selection {record.selection_id} content_hash invalid",
            ))
        return errors

    def verify_delta(self, delta: CoverageTensorDelta) -> list[tuple[EC, str]]:
        """验证 CoverageTensorDelta。"""
        errors: list[tuple[EC, str]] = []
        if not delta.delta_id:
            errors.append((EC.OP_COVERAGE_DELTA_INVALID, "delta_id empty"))
        if not delta.from_snapshot_id or not delta.to_snapshot_id:
            errors.append((
                EC.OP_COVERAGE_DELTA_INVALID,
                "from/to snapshot_id empty",
            ))
        if not delta.is_hash_valid:
            errors.append((
                EC.OP_COVERAGE_DELTA_INVALID,
                f"delta {delta.delta_id} content_hash invalid",
            ))
        return errors
