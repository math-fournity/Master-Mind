"""CrossEpochDuplicateAssessment — 跨 Epoch 重复计数防护。

来自 WP-OP1：防止跨 Epoch 重复计数。
同一 problem/source cluster 不得跨 Epoch 重复计数。

关键约束（blocker）：
- 跨 Epoch 重复计数 → OP_CROSS_EPOCH_DUPLICATE
- duplicate kind 不在 OP_DUPLICATE_KINDS → OP_DUPLICATE_KIND_INVALID

SIDE_EFFECT_FREE：纯内存模拟。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    OP_DUPLICATE_KINDS,
    VerificationErrorCode as EC,
)


class DuplicateAssessmentError(Exception):
    """Cross-Epoch duplicate assessment 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class DuplicateRecord:
    """单条重复计数记录。"""

    epoch_id: str
    kind: str  # OP_DUPLICATE_KINDS
    fingerprint: str  # problem/source cluster/evidence cell 的指纹
    counted: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "epoch_id": self.epoch_id,
            "kind": self.kind,
            "fingerprint": self.fingerprint,
            "counted": self.counted,
        }


@dataclass
class CrossEpochDuplicateAssessment:
    """跨 Epoch 重复计数评估。

    记录每个 Epoch 中被计数的 problem/source cluster/evidence cell。
    同一 fingerprint 不得在多个 Epoch 中被 counted=True。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    assessment_id: str
    records: list[DuplicateRecord] = field(default_factory=list)
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "assessment_id": self.assessment_id,
            "records": [r.to_dict() for r in self.records],
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


class CrossEpochDuplicateAssessor:
    """跨 Epoch 重复计数评估器。

    SIDE_EFFECT_FREE：纯内存模拟。
    """

    def __init__(self, assessment_id: str) -> None:
        self._assessment = CrossEpochDuplicateAssessment(
            assessment_id=assessment_id,
        )
        self._counted: dict[tuple[str, str], str] = {}  # (kind, fp) → epoch

    @property
    def assessment(self) -> CrossEpochDuplicateAssessment:
        return self._assessment

    def record_counted(
        self,
        *,
        epoch_id: str,
        kind: str,
        fingerprint: str,
    ) -> DuplicateRecord:
        """记录一个被计数的 item。

        blocker：同一 (kind, fingerprint) 跨 Epoch 重复计数。
        """
        if kind not in OP_DUPLICATE_KINDS:
            raise DuplicateAssessmentError(
                EC.OP_DUPLICATE_KIND_INVALID,
                f"kind {kind!r} not in OP_DUPLICATE_KINDS",
            )
        key = (kind, fingerprint)
        if key in self._counted and self._counted[key] != epoch_id:
            raise DuplicateAssessmentError(
                EC.OP_CROSS_EPOCH_DUPLICATE,
                f"{kind} fingerprint {fingerprint} counted in epoch "
                f"{self._counted[key]}, re-counted in epoch {epoch_id}",
            )
        self._counted[key] = epoch_id
        record = DuplicateRecord(
            epoch_id=epoch_id,
            kind=kind,
            fingerprint=fingerprint,
            counted=True,
        )
        self._assessment.records.append(record)
        return record

    def record_not_counted(
        self,
        *,
        epoch_id: str,
        kind: str,
        fingerprint: str,
    ) -> DuplicateRecord:
        """记录一个已知重复但不计数的 item（去重后不重复计数）。"""
        if kind not in OP_DUPLICATE_KINDS:
            raise DuplicateAssessmentError(
                EC.OP_DUPLICATE_KIND_INVALID,
                f"kind {kind!r} not in OP_DUPLICATE_KINDS",
            )
        record = DuplicateRecord(
            epoch_id=epoch_id,
            kind=kind,
            fingerprint=fingerprint,
            counted=False,
        )
        self._assessment.records.append(record)
        return record

    def finalize(self) -> None:
        """计算 assessment content_hash。"""
        self._assessment.content_hash = (
            self._assessment.compute_content_hash()
        )

    def verify_no_cross_epoch_duplicate(self) -> list[tuple[EC, str]]:
        """验证无跨 Epoch 重复计数。"""
        errors: list[tuple[EC, str]] = []
        seen: dict[tuple[str, str], str] = {}
        for r in self._assessment.records:
            if not r.counted:
                continue
            key = (r.kind, r.fingerprint)
            if key in seen and seen[key] != r.epoch_id:
                errors.append((
                    EC.OP_CROSS_EPOCH_DUPLICATE,
                    f"{r.kind} fingerprint {r.fingerprint} counted in "
                    f"epoch {seen[key]} and epoch {r.epoch_id}",
                ))
            seen[key] = r.epoch_id
        return errors

    def verify_kinds(self) -> list[tuple[EC, str]]:
        """验证所有 record kind 合法。"""
        errors: list[tuple[EC, str]] = []
        for r in self._assessment.records:
            if r.kind not in OP_DUPLICATE_KINDS:
                errors.append((
                    EC.OP_DUPLICATE_KIND_INVALID,
                    f"record kind {r.kind!r} invalid",
                ))
        return errors

    def verify_hash(self) -> list[tuple[EC, str]]:
        """验证 assessment hash 有效。"""
        errors: list[tuple[EC, str]] = []
        if not self._assessment.is_hash_valid:
            errors.append((
                EC.OP_CROSS_EPOCH_DUPLICATE,
                "CrossEpochDuplicateAssessment content_hash invalid",
            ))
        return errors
