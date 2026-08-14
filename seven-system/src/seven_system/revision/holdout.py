"""HoldoutConsumption — holdout 消费追踪。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P8 节和
docs/implementation/15-work-package-implementation-contracts.md WP-RV1：

Same evidence cannot be both fit and confirmation; viewed holdout immediately
consumed.

关键约束（blocker）：
- 同一证据不得同时用作 fit 和 confirmation → RV_FIT_EQUALS_CONFIRMATION
- viewed holdout 立即 consumed，不得反复偷看 → RV_HOLDOUT_REPEATED_PEEK
- 单例 split（同一 case 既作 fit 又作 test）→ RV_SINGLE_CASE_SPLIT
- 已 consumed 的 holdout 不得再 view → RV_HOLDOUT_ALREADY_CONSUMED
- holdout status 不在 RV_HOLDOUT_STATUSES → RV_HOLDOUT_STATUS_INVALID
- content_hash 不匹配 → RV_HOLDOUT_CONSUMPTION_HASH_MISMATCH

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    RV_HOLDOUT_STATUSES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/holdout-consumption"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class HoldoutView:
    """单次 holdout view 记录。

    字段：
        view_id: 唯一标识
        holdout_id: holdout 标识
        purpose: 用途（FIT / CONFIRMATION / TEST）
        case_ids: 涉及的 case ID 列表
        viewed_at: view 时间
        status: 消费状态（RV_HOLDOUT_STATUSES）
    """

    view_id: str
    holdout_id: str
    purpose: str = "FIT"
    case_ids: tuple[str, ...] = ()
    viewed_at: str = ""
    status: str = "VIEWED"

    def to_dict(self) -> dict[str, Any]:
        return {
            "view_id": self.view_id,
            "holdout_id": self.holdout_id,
            "purpose": self.purpose,
            "case_ids": list(self.case_ids),
            "viewed_at": self.viewed_at,
            "status": self.status,
        }


@dataclass(frozen=True)
class HoldoutConsumption:
    """Holdout 消费追踪——记录每次 holdout view + 消费状态。

    字段：
        consumption_id: 唯一标识
        provenance_snapshot_hash: 引用的 ProvenanceSnapshot content_hash
        views: holdout view 记录列表
        fit_case_ids: 用作 fit 的 case ID 集合
        confirmation_case_ids: 用作 confirmation 的 case ID 集合
        test_case_ids: 用作 test 的 case ID 集合
        consumed_holdout_ids: 已 consumed 的 holdout ID 集合
        hash_algorithm: 哈希算法
        content_hash: 内容哈希
    """

    consumption_id: str
    provenance_snapshot_hash: str = ""
    views: tuple[HoldoutView, ...] = ()
    fit_case_ids: tuple[str, ...] = ()
    confirmation_case_ids: tuple[str, ...] = ()
    test_case_ids: tuple[str, ...] = ()
    consumed_holdout_ids: tuple[str, ...] = ()
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "consumption_id": self.consumption_id,
            "provenance_snapshot_hash": self.provenance_snapshot_hash,
            "views": [v.to_dict() for v in self.views],
            "fit_case_ids": list(self.fit_case_ids),
            "confirmation_case_ids": list(self.confirmation_case_ids),
            "test_case_ids": list(self.test_case_ids),
            "consumed_holdout_ids": list(self.consumed_holdout_ids),
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


@dataclass(frozen=True)
class HoldoutConsumptionVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    consumption_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def make_holdout_consumption(
    *,
    consumption_id: str,
    provenance_snapshot_hash: str,
    views: list[HoldoutView] | None = None,
) -> HoldoutConsumption:
    """构建 HoldoutConsumption。

    自动从 views 派生 fit/confirmation/test case_ids 和 consumed_holdout_ids。
    viewed holdout 立即 consumed。
    """
    views = views or []
    fit_cases: list[str] = []
    confirmation_cases: list[str] = []
    test_cases: list[str] = []
    consumed: list[str] = []
    for v in views:
        if v.purpose == "FIT":
            fit_cases.extend(v.case_ids)
        elif v.purpose == "CONFIRMATION":
            confirmation_cases.extend(v.case_ids)
        elif v.purpose == "TEST":
            test_cases.extend(v.case_ids)
        # viewed holdout 立即 consumed
        if v.status == "VIEWED" and v.holdout_id not in consumed:
            consumed.append(v.holdout_id)

    hc = HoldoutConsumption(
        consumption_id=consumption_id,
        provenance_snapshot_hash=provenance_snapshot_hash,
        views=tuple(views),
        fit_case_ids=tuple(fit_cases),
        confirmation_case_ids=tuple(confirmation_cases),
        test_case_ids=tuple(test_cases),
        consumed_holdout_ids=tuple(consumed),
    )
    return dataclasses.replace(hc, content_hash=hc.compute_content_hash())


def record_holdout_view(
    hc: HoldoutConsumption,
    view: HoldoutView,
) -> HoldoutConsumption:
    """记录一次新的 holdout view，返回新的 HoldoutConsumption。

    viewed holdout 立即 consumed。
    """
    views = list(hc.views) + [view]
    return make_holdout_consumption(
        consumption_id=hc.consumption_id,
        provenance_snapshot_hash=hc.provenance_snapshot_hash,
        views=views,
    )


def verify_holdout_consumption(
    hc: HoldoutConsumption,
) -> HoldoutConsumptionVerificationResult:
    """验证 HoldoutConsumption。

    blocker：
    - fit=confirmation（同一 case 同时用作 fit 和 confirmation）→ RV_FIT_EQUALS_CONFIRMATION
    - 单例 split（同一 case 既作 fit 又作 test）→ RV_SINGLE_CASE_SPLIT
    - 反复偷看（同一 holdout 被 view 多次）→ RV_HOLDOUT_REPEATED_PEEK
    - 已 consumed 的 holdout 再 view → RV_HOLDOUT_ALREADY_CONSUMED
    - holdout status 不合法 → RV_HOLDOUT_STATUS_INVALID
    - content_hash 不匹配 → RV_HOLDOUT_CONSUMPTION_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = hc.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not hc.consumption_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("consumption_id is empty")

    if not hc.provenance_snapshot_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("provenance_snapshot_hash is empty")

    # holdout status 合法性
    for v in hc.views:
        if v.status not in RV_HOLDOUT_STATUSES:
            errors.append(EC.RV_HOLDOUT_STATUS_INVALID)
            details.append(f"view {v.view_id} status {v.status!r} not in RV_HOLDOUT_STATUSES")

    # fit=confirmation 检查
    fit_set = set(hc.fit_case_ids)
    confirmation_set = set(hc.confirmation_case_ids)
    overlap_fc = fit_set & confirmation_set
    if overlap_fc:
        errors.append(EC.RV_FIT_EQUALS_CONFIRMATION)
        details.append(
            f"cases used as both fit and confirmation: {sorted(overlap_fc)}"
        )

    # 单例 split 检查（同一 case 既作 fit 又作 test）
    test_set = set(hc.test_case_ids)
    overlap_ft = fit_set & test_set
    if overlap_ft:
        errors.append(EC.RV_SINGLE_CASE_SPLIT)
        details.append(
            f"cases used as both fit and test (single-case split): {sorted(overlap_ft)}"
        )

    # 反复偷看检查（同一 holdout 被 view 多次）
    seen_holdouts: list[str] = []
    consumed_set = set(hc.consumed_holdout_ids)
    for v in hc.views:
        if v.holdout_id in seen_holdouts:
            errors.append(EC.RV_HOLDOUT_REPEATED_PEEK)
            details.append(
                f"holdout {v.holdout_id} viewed multiple times (repeated peek)"
            )
        # 已 consumed 的 holdout 再 view
        if v.holdout_id in consumed_set and v.status == "VIEWED":
            # 如果是同一 holdout 第二次 view，consumed 已包含它
            if seen_holdouts.count(v.holdout_id) >= 1:
                errors.append(EC.RV_HOLDOUT_ALREADY_CONSUMED)
                details.append(
                    f"holdout {v.holdout_id} already consumed but viewed again"
                )
        seen_holdouts.append(v.holdout_id)

    # content_hash
    if not hc.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif hc.content_hash != hc.compute_content_hash():
        errors.append(EC.RV_HOLDOUT_CONSUMPTION_HASH_MISMATCH)
        details.append("HoldoutConsumption content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return HoldoutConsumptionVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        consumption_id=hc.consumption_id,
    )


def check_fit_not_confirmation(hc: HoldoutConsumption) -> VerificationResult:
    """检查 fit≠confirmation（同一证据不得同时用作 fit 和 confirmation）。"""
    errors: list[EC] = []
    details: list[str] = []
    fit_set = set(hc.fit_case_ids)
    confirmation_set = set(hc.confirmation_case_ids)
    overlap = fit_set & confirmation_set
    if overlap:
        errors.append(EC.RV_FIT_EQUALS_CONFIRMATION)
        details.append(f"cases used as both fit and confirmation: {sorted(overlap)}")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_no_repeated_peek(hc: HoldoutConsumption) -> VerificationResult:
    """检查不得反复偷看 holdout。"""
    errors: list[EC] = []
    details: list[str] = []
    seen: set[str] = set()
    for v in hc.views:
        if v.holdout_id in seen:
            errors.append(EC.RV_HOLDOUT_REPEATED_PEEK)
            details.append(f"holdout {v.holdout_id} viewed multiple times")
        seen.add(v.holdout_id)
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_no_single_case_split(hc: HoldoutConsumption) -> VerificationResult:
    """检查单例 split（同一 case 既作 fit 又作 test）。"""
    errors: list[EC] = []
    details: list[str] = []
    fit_set = set(hc.fit_case_ids)
    test_set = set(hc.test_case_ids)
    overlap = fit_set & test_set
    if overlap:
        errors.append(EC.RV_SINGLE_CASE_SPLIT)
        details.append(f"cases used as both fit and test: {sorted(overlap)}")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
