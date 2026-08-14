"""Selector — WP-ST1 从冻结 TellStrategyRelease 检索/排序/弃权 Tell 候选。

关键约束（blocker）：
- Selector 从冻结 TellStrategyRelease 检索候选，不接触 live Case
- Selector 可以 abstain（不选任何 Tell）
- abstain 时不得同时 select（ST_SELECTOR_ABSTAIN_NOT_RESPECTED）
- SelectorDecision 记录完整推理，引用 TellStrategyRelease by hash
- 组件版本必须与 release 锁定的版本一致（ST_COMPONENT_DRIFT）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ST_SELECTOR_DECISIONS,
    VerificationErrorCode as EC,
)
from ..taxonomy.boundary import SelectorDecision, make_selector_decision


_SELECTOR_RECEIPT_SCHEMA_ID = "seven/selector-receipt"
_SELECTOR_RECEIPT_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class SelectorReceipt:
    """Selector 运行收据——记录选择决策和完整推理。

    字段：
        receipt_id: 唯一标识
        release_ref: TellStrategyRelease 引用 {release_id, content_hash}
        decision: SelectorDecision（来自 TX1）
        kind: 决策 kind（ST_SELECTOR_DECISIONS）
        selected_core_ids: 选中的 TellCore ID 列表
        ranking: 排序列表
        abstain_reason: 弃权原因（kind=ABSTAIN 时非空）
        reasoning: 完整推理记录
        component_version: selector 组件版本（必须与 release 一致）
        content_hash: 内容哈希
    """

    receipt_id: str
    release_ref: dict[str, str] = field(default_factory=dict)
    decision: SelectorDecision | None = None
    kind: str = "SELECT"
    selected_core_ids: tuple[str, ...] = ()
    ranking: tuple[str, ...] = ()
    abstain_reason: str = ""
    reasoning: str = ""
    component_version: str = ""
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SELECTOR_RECEIPT_SCHEMA_ID,
            "schema_version": _SELECTOR_RECEIPT_SCHEMA_VERSION,
            "receipt_id": self.receipt_id,
            "release_ref": dict(self.release_ref),
            "decision": self.decision.to_dict() if self.decision else None,
            "kind": self.kind,
            "selected_core_ids": list(self.selected_core_ids),
            "ranking": list(self.ranking),
            "abstain_reason": self.abstain_reason,
            "reasoning": self.reasoning,
            "component_version": self.component_version,
            "frozen_at": self.frozen_at,
            "hash_algorithm": self.hash_algorithm,
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
    def is_abstain(self) -> bool:
        return self.kind == "ABSTAIN"


def make_selector_receipt(
    *,
    receipt_id: str,
    release_ref: dict[str, str] | None = None,
    kind: str = "SELECT",
    selected_core_ids: tuple[str, ...] = (),
    ranking: tuple[str, ...] = (),
    abstain_reason: str = "",
    reasoning: str = "",
    component_version: str = "",
    frozen_at: str = "",
) -> SelectorReceipt:
    """构建 SelectorReceipt，内部自动构建 SelectorDecision。"""
    decision = make_selector_decision(
        decision_id=f"{receipt_id}-decision",
        kind=kind,
        selected_core_ids=selected_core_ids,
        ranking=ranking,
        abstain_reason=abstain_reason,
        frozen_at=frozen_at,
    )
    r = SelectorReceipt(
        receipt_id=receipt_id,
        release_ref=release_ref or {},
        decision=decision,
        kind=kind,
        selected_core_ids=selected_core_ids,
        ranking=ranking,
        abstain_reason=abstain_reason,
        reasoning=reasoning,
        component_version=component_version,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(r, content_hash=r.compute_content_hash())


@dataclass(frozen=True)
class SelectorReceiptVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    receipt_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_selector_receipt(
    receipt: SelectorReceipt,
    *,
    expected_release_hash: str | None = None,
    expected_component_version: str | None = None,
) -> SelectorReceiptVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = receipt.to_dict()
    if d.get("schema_id") != _SELECTOR_RECEIPT_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SELECTOR_RECEIPT_SCHEMA_ID}")

    # kind valid
    if receipt.kind not in ST_SELECTOR_DECISIONS:
        errors.append(EC.ST_SELECTOR_KIND_INVALID)
        details.append(
            f"kind '{receipt.kind}' not in {sorted(ST_SELECTOR_DECISIONS)}"
        )

    # release_ref required — must reference TellStrategyRelease by hash
    if not receipt.release_ref.get("release_id"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain release_id")
    if not receipt.release_ref.get("content_hash"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain content_hash")

    # release hash match
    if expected_release_hash is not None:
        if receipt.release_ref.get("content_hash") != expected_release_hash:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"release_ref content_hash mismatch: claims "
                f"{receipt.release_ref.get('content_hash')}, "
                f"expected {expected_release_hash}"
            )

    # component version drift
    if expected_component_version is not None:
        if receipt.component_version != expected_component_version:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"component_version drift: claims "
                f"{receipt.component_version}, expected "
                f"{expected_component_version}"
            )

    # blocker: abstain not respected — abstain but also selecting
    if receipt.kind == "ABSTAIN":
        if receipt.selected_core_ids:
            errors.append(EC.ST_SELECTOR_ABSTAIN_NOT_RESPECTED)
            details.append(
                "kind=ABSTAIN but selected_core_ids is non-empty — "
                "abstain must not select any core"
            )
        if not receipt.abstain_reason:
            errors.append(EC.ST_SELECTOR_ABSTAIN_NOT_RESPECTED)
            details.append("kind=ABSTAIN but abstain_reason is empty")
    else:
        if receipt.kind == "SELECT" and not receipt.selected_core_ids:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("kind=SELECT but selected_core_ids is empty")

    # decision must be present
    if receipt.decision is None:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("decision (SelectorDecision) is missing")

    # content_hash
    if not receipt.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif receipt.content_hash != receipt.compute_content_hash():
        errors.append(EC.ST_RENDERER_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {receipt.content_hash}, "
            f"computed {receipt.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return SelectorReceiptVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        receipt_id=receipt.receipt_id,
    )


class Selector:
    """Selector — 从冻结 TellStrategyRelease 检索/排序/弃权 Tell 候选。

    纯程序实现：给定 release_ref + candidate_core_ids + ranking 决策，
    产出 SelectorReceipt。可以 abstain。
    """

    def __init__(self, *, component_version: str = "st1-selector-v1") -> None:
        self.component_version = component_version

    def select(
        self,
        *,
        receipt_id: str,
        release_ref: dict[str, str],
        candidate_core_ids: tuple[str, ...],
        ranking: tuple[str, ...] | None = None,
        reasoning: str = "",
        frozen_at: str = "",
    ) -> SelectorReceipt:
        """执行选择——从候选中选出并排序。"""
        selected = candidate_core_ids
        rank = ranking if ranking is not None else candidate_core_ids
        return make_selector_receipt(
            receipt_id=receipt_id,
            release_ref=release_ref,
            kind="SELECT",
            selected_core_ids=selected,
            ranking=rank,
            reasoning=reasoning,
            component_version=self.component_version,
            frozen_at=frozen_at,
        )

    def rank(
        self,
        *,
        receipt_id: str,
        release_ref: dict[str, str],
        ranking: tuple[str, ...],
        reasoning: str = "",
        frozen_at: str = "",
    ) -> SelectorReceipt:
        """执行排序——产出有序排名。"""
        return make_selector_receipt(
            receipt_id=receipt_id,
            release_ref=release_ref,
            kind="RANK",
            ranking=ranking,
            reasoning=reasoning,
            component_version=self.component_version,
            frozen_at=frozen_at,
        )

    def abstain(
        self,
        *,
        receipt_id: str,
        release_ref: dict[str, str],
        abstain_reason: str,
        reasoning: str = "",
        frozen_at: str = "",
    ) -> SelectorReceipt:
        """执行弃权——不选任何 Tell。"""
        return make_selector_receipt(
            receipt_id=receipt_id,
            release_ref=release_ref,
            kind="ABSTAIN",
            abstain_reason=abstain_reason,
            reasoning=reasoning,
            component_version=self.component_version,
            frozen_at=frozen_at,
        )
