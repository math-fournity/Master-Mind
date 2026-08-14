"""InvalidationPropagation — 失效传播。

来自 WP-QA0 work package contract：

"修题不失效"（question modified but downstream not invalidated）= blocker。

题面变化 → 旧 reviews, verification, release, bare results, case roles 全部失效。

失效传播目标（QA_INVALIDATION_TARGETS）：
- AdversarialReview
- VerificationDossier
- QuestionRelease
- BareBaseline
- BareQualificationResult
- CaseRoleAssignment
- AuthoringEvaluationPack

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import (
    QA_INVALIDATION_TARGETS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


@dataclass
class InvalidationRecord:
    """单条失效记录。"""

    target_kind: str
    target_ref: str
    invalidated_by_draft_hash: str
    invalidated: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_kind": self.target_kind,
            "target_ref": self.target_ref,
            "invalidated_by_draft_hash": self.invalidated_by_draft_hash,
            "invalidated": self.invalidated,
        }


@dataclass
class InvalidationPropagation:
    """InvalidationPropagation — 失效传播器。

    当 QuestionDraftVersion 的 public_statement 变化时（新版本），
    所有引用旧版本 hash 的下游对象必须被标记为失效。

    硬约束：
    - 题面变化 → 所有 QA_INVALIDATION_TARGETS 中的下游失效
    - 未失效 = QA_QUESTION_MODIFIED_DOWNSTREAM_NOT_INVALIDATED
    - 未知失效目标 = QA_INVALIDATION_TARGET_UNKNOWN
    """

    # 已注册的下游对象：target_kind → list of (ref, draft_hash)
    _downstream: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    # 失效记录
    _invalidations: list[InvalidationRecord] = field(default_factory=list)

    def register_downstream(
        self,
        target_kind: str,
        target_ref: str,
        draft_hash: str,
    ) -> VerificationResult:
        """注册一个下游对象引用某个 draft hash。"""
        if target_kind not in QA_INVALIDATION_TARGETS:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_INVALIDATION_TARGET_UNKNOWN],
                details=[f"unknown invalidation target: {target_kind!r}"],
            )
        self._downstream.setdefault(target_kind, []).append((target_ref, draft_hash))
        return VerificationResult(verdict="PASS")

    def invalidate_for_new_draft(
        self,
        old_draft_hash: str,
        new_draft_hash: str,
    ) -> VerificationResult:
        """题面变化（old draft → new draft），失效所有引用 old draft 的下游。

        检查所有 QA_INVALIDATION_TARGETS 中注册的下游对象是否都被失效。
        """
        errors: list[EC] = []
        details: list[str] = []

        invalidated_kinds: set[str] = set()

        for target_kind in QA_INVALIDATION_TARGETS:
            entries = self._downstream.get(target_kind, [])
            for ref, draft_hash in entries:
                if draft_hash == old_draft_hash:
                    # 这个下游引用了旧 draft hash，必须失效
                    record = InvalidationRecord(
                        target_kind=target_kind,
                        target_ref=ref,
                        invalidated_by_draft_hash=old_draft_hash,
                        invalidated=True,
                    )
                    self._invalidations.append(record)
                    invalidated_kinds.add(target_kind)

        # 检查是否有注册了但没被失效的
        for target_kind in QA_INVALIDATION_TARGETS:
            entries = self._downstream.get(target_kind, [])
            for ref, draft_hash in entries:
                if draft_hash == old_draft_hash:
                    # 检查是否在 _invalidations 中
                    found = any(
                        ir.target_kind == target_kind
                        and ir.target_ref == ref
                        and ir.invalidated
                        for ir in self._invalidations
                    )
                    if not found:
                        errors.append(EC.QA_QUESTION_MODIFIED_DOWNSTREAM_NOT_INVALIDATED)
                        details.append(
                            f"{target_kind} {ref} references old draft {old_draft_hash[:8]}... "
                            f"but was not invalidated"
                        )

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)
        return VerificationResult(verdict="PASS")

    def check_all_invalidated(
        self,
        old_draft_hash: str,
    ) -> VerificationResult:
        """检查所有引用 old_draft_hash 的下游是否都已失效。"""
        errors: list[EC] = []
        details: list[str] = []

        for target_kind in QA_INVALIDATION_TARGETS:
            entries = self._downstream.get(target_kind, [])
            for ref, draft_hash in entries:
                if draft_hash == old_draft_hash:
                    found = any(
                        ir.target_kind == target_kind
                        and ir.target_ref == ref
                        and ir.invalidated
                        and ir.invalidated_by_draft_hash == old_draft_hash
                        for ir in self._invalidations
                    )
                    if not found:
                        errors.append(EC.QA_QUESTION_MODIFIED_DOWNSTREAM_NOT_INVALIDATED)
                        details.append(
                            f"{target_kind} {ref} references old draft but not invalidated"
                        )

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)
        return VerificationResult(verdict="PASS")

    @property
    def invalidation_records(self) -> list[InvalidationRecord]:
        return list(self._invalidations)

    def is_invalidated(self, target_kind: str, target_ref: str) -> bool:
        """检查某个下游对象是否已被失效。"""
        return any(
            ir.target_kind == target_kind
            and ir.target_ref == target_ref
            and ir.invalidated
            for ir in self._invalidations
        )
