"""MissingnessReport + CostDimension — P7 缺失报告与成本维度。

来自 docs/implementation/14-evidence-analysis-and-multi-epoch.md：

缺失与协议失效：
- 科学负结果进入 ITT 失败分子；
- 预注册拒绝/abstain 是 policy 结果，不是 missing；
- 基础设施 invalid、观测不足、泄漏污染分别记数，不填 0 或当失败；
- 按 arm 报告 missing/invalid/contamination 率。若超过 ExperimentPlan 阈值或
  arm 间不平衡，主 contrast 为 INCONCLUSIVE_DUE_TO_PROTOCOL；
- 停止后仍按冻结 analysis set 分析已纳入 cluster，不删除不利结果。

成本维度：tokens、wallclock、rate_limit、quota、human_minutes、provider_billed_amount。
provider_billed_amount UNOBSERVABLE 时不填值；usage_completeness != COMPLETE
阻止正式 cost metrics。

关键约束（blocker）：
- invalid 结果填 0 → BLOCK（EV_INVALID_FILLED_ZERO）
- missingness 不完整 → BLOCK（EV_MISSINGNESS_INCOMPLETE）
- provider_billed_amount 不可观测时填值 → BLOCK（EV_COST_UNOBSERVABLE_FILLED）
- usage_completeness 无效 → BLOCK（EV_USAGE_COMPLETENESS_INVALID）
- cost 不完整 → BLOCK（EV_COST_INCOMPLETE）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    EV_COST_KINDS,
    EV_MISSINGNESS_KINDS,
    EV_USAGE_COMPLETENESS_STATUSES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


# ─── MissingnessReport ──────────────────────────────────────────────────


@dataclass(frozen=True)
class MissingnessEntry:
    """单条缺失记录——哪个 arm/episode 缺失、原因、对估计的影响。

    字段：
        arm_id: arm 标识
        episode_id: episode 标识（空表示整 arm 缺失）
        kind: 缺失种类（EV_MISSINGNESS_KINDS）
        reason: 缺失原因
        impact_on_estimate: 对估计的影响
        filled_value: 填充值（INVALID_RESULT 时必须为 None，不得填 0）
    """

    arm_id: str
    episode_id: str = ""
    kind: str = "NONE"
    reason: str = ""
    impact_on_estimate: str = ""
    filled_value: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_id": self.arm_id,
            "episode_id": self.episode_id,
            "kind": self.kind,
            "reason": self.reason,
            "impact_on_estimate": self.impact_on_estimate,
            "filled_value": self.filled_value,
        }


@dataclass(frozen=True)
class MissingnessReport:
    """P7 缺失报告——按 arm 报告 missing/invalid/contamination 率。

    invalid 结果不得填 0；缺失/invalid/contamination 分别记数。
    """

    report_id: str
    plan_id: str
    entries: tuple[MissingnessEntry, ...] = ()
    per_arm_rates: dict[str, dict[str, float]] = field(default_factory=dict)
    threshold_exceeded: bool = False
    imbalanced_across_arms: bool = False
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "report_id": self.report_id,
            "plan_id": self.plan_id,
            "entries": [e.to_dict() for e in self.entries],
            "per_arm_rates": {k: dict(v) for k, v in self.per_arm_rates.items()},
            "threshold_exceeded": self.threshold_exceeded,
            "imbalanced_across_arms": self.imbalanced_across_arms,
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
    def missing_count(self) -> int:
        return sum(1 for e in self.entries if e.kind in ("ARM_MISSING", "EPISODE_MISSING"))

    @property
    def invalid_count(self) -> int:
        return sum(1 for e in self.entries if e.kind == "INVALID_RESULT")

    @property
    def contamination_count(self) -> int:
        return sum(1 for e in self.entries if e.kind == "CONTAMINATION")


def make_missingness_report(
    *,
    report_id: str,
    plan_id: str,
    entries: list[MissingnessEntry],
    per_arm_rates: dict[str, dict[str, float]] | None = None,
    threshold_exceeded: bool = False,
    imbalanced_across_arms: bool = False,
) -> MissingnessReport:
    """构建 MissingnessReport。"""
    report = MissingnessReport(
        report_id=report_id,
        plan_id=plan_id,
        entries=tuple(entries),
        per_arm_rates=per_arm_rates or {},
        threshold_exceeded=threshold_exceeded,
        imbalanced_across_arms=imbalanced_across_arms,
    )
    return dataclasses.replace(report, content_hash=report.compute_content_hash())


def verify_missingness_report(
    report: MissingnessReport,
) -> VerificationResult:
    """验证 MissingnessReport。

    blocker：
    - invalid 结果填 0 → EV_INVALID_FILLED_ZERO
    - kind 不在 EV_MISSINGNESS_KINDS → EV_MISSINGNESS_INCOMPLETE
    - 缺少 per_arm_rates → EV_MISSINGNESS_INCOMPLETE
    """
    errors: list[EC] = []
    details: list[str] = []

    if not report.report_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("report_id is empty")

    if not report.plan_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("plan_id is empty")

    for e in report.entries:
        if e.kind not in EV_MISSINGNESS_KINDS:
            errors.append(EC.EV_MISSINGNESS_INCOMPLETE)
            details.append(f"entry arm {e.arm_id} kind {e.kind} not in EV_MISSINGNESS_KINDS")
        # invalid 结果不得填 0
        if e.kind == "INVALID_RESULT" and e.filled_value is not None:
            if e.filled_value == 0:
                errors.append(EC.EV_INVALID_FILLED_ZERO)
                details.append(
                    f"entry arm {e.arm_id} invalid result filled with 0 — BLOCK"
                )

    # per_arm_rates 必须报告
    if not report.per_arm_rates:
        errors.append(EC.EV_MISSINGNESS_INCOMPLETE)
        details.append("per_arm_rates must be reported per arm")

    if not report.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif report.content_hash != report.compute_content_hash():
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append("MissingnessReport content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_invalid_not_filled_zero(
    entries: list[MissingnessEntry],
) -> VerificationResult:
    """检查所有 invalid 结果未填 0。"""
    errors: list[EC] = []
    details: list[str] = []

    for e in entries:
        if e.kind == "INVALID_RESULT" and e.filled_value is not None:
            if e.filled_value == 0:
                errors.append(EC.EV_INVALID_FILLED_ZERO)
                details.append(
                    f"arm {e.arm_id} invalid result filled with 0 — BLOCK"
                )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# ─── CostDimension ──────────────────────────────────────────────────────


@dataclass(frozen=True)
class CostDimension:
    """P7 成本维度聚合。

    tokens、wallclock、rate_limit、quota、human_minutes 可观测时聚合。
    provider_billed_amount UNOBSERVABLE 时不填值（保持 None）。
    usage_completeness != COMPLETE 阻止正式 cost metrics。

    字段：
        tokens: token 总量（可观测时）
        wallclock_seconds: 墙钟秒
        rate_limit_hits: 限速命中数
        quota_consumed: 配额消耗
        human_minutes: 人工分钟
        provider_billed_amount: provider 计费金额（UNOBSERVABLE 时为 None）
        usage_completeness: 使用完整性（EV_USAGE_COMPLETENESS_STATUSES）
        unobservable_dimensions: 不可观测的维度列表
    """

    tokens: int | None = None
    wallclock_seconds: float | None = None
    rate_limit_hits: int | None = None
    quota_consumed: float | None = None
    human_minutes: float | None = None
    provider_billed_amount: float | None = None
    usage_completeness: str = "COMPLETE"
    unobservable_dimensions: tuple[str, ...] = ()
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "tokens": self.tokens,
            "wallclock_seconds": self.wallclock_seconds,
            "rate_limit_hits": self.rate_limit_hits,
            "quota_consumed": self.quota_consumed,
            "human_minutes": self.human_minutes,
            "provider_billed_amount": self.provider_billed_amount,
            "usage_completeness": self.usage_completeness,
            "unobservable_dimensions": list(self.unobservable_dimensions),
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
    def formal_cost_blocked(self) -> bool:
        """usage_completeness != COMPLETE 阻止正式 cost metrics。"""
        return self.usage_completeness != "COMPLETE"


def make_cost_dimension(
    *,
    tokens: int | None = None,
    wallclock_seconds: float | None = None,
    rate_limit_hits: int | None = None,
    quota_consumed: float | None = None,
    human_minutes: float | None = None,
    provider_billed_amount: float | None = None,
    usage_completeness: str = "COMPLETE",
    unobservable_dimensions: tuple[str, ...] = (),
) -> CostDimension:
    """构建 CostDimension。

    provider_billed_amount 不可观测时传 None 并加入 unobservable_dimensions。
    """
    cd = CostDimension(
        tokens=tokens,
        wallclock_seconds=wallclock_seconds,
        rate_limit_hits=rate_limit_hits,
        quota_consumed=quota_consumed,
        human_minutes=human_minutes,
        provider_billed_amount=provider_billed_amount,
        usage_completeness=usage_completeness,
        unobservable_dimensions=unobservable_dimensions,
    )
    return dataclasses.replace(cd, content_hash=cd.compute_content_hash())


def verify_cost_dimension(
    cost: CostDimension,
) -> VerificationResult:
    """验证 CostDimension。

    blocker：
    - usage_completeness 无效 → EV_USAGE_COMPLETENESS_INVALID
    - provider_billed_amount 不可观测时填值 → EV_COST_UNOBSERVABLE_FILLED
    - cost 不完整（缺维度且未声明 UNOBSERVABLE）→ EV_COST_INCOMPLETE
    """
    errors: list[EC] = []
    details: list[str] = []

    if cost.usage_completeness not in EV_USAGE_COMPLETENESS_STATUSES:
        errors.append(EC.EV_USAGE_COMPLETENESS_INVALID)
        details.append(
            f"usage_completeness {cost.usage_completeness} not in "
            f"EV_USAGE_COMPLETENESS_STATUSES"
        )

    # provider_billed_amount 不可观测时不得填值
    if "provider_billed_amount" in cost.unobservable_dimensions:
        if cost.provider_billed_amount is not None:
            errors.append(EC.EV_COST_UNOBSERVABLE_FILLED)
            details.append(
                "provider_billed_amount declared UNOBSERVABLE but has a value — BLOCK"
            )

    # 不可观测维度必须在 EV_COST_KINDS 中
    for dim in cost.unobservable_dimensions:
        if dim not in EV_COST_KINDS:
            errors.append(EC.EV_COST_INCOMPLETE)
            details.append(f"unobservable dimension {dim} not in EV_COST_KINDS")

    # cost 完整性：usage_completeness == COMPLETE 时所有可观测维度必须有值或显式 None
    # 这里只检查不阻塞——完整性的严格检查由 capability report 负责

    if not cost.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif cost.content_hash != cost.compute_content_hash():
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append("CostDimension content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_cost_completeness(
    cost: CostDimension,
    required_dimensions: tuple[str, ...] = (
        "tokens", "wallclock", "human_minutes",
    ),
) -> VerificationResult:
    """检查 cost 维度完整性。

    required_dimensions 中的维度必须有值或声明 UNOBSERVABLE。
    usage_completeness != COMPLETE 阻止正式 cost metrics（记录但不 BLOCK 构造）。
    """
    errors: list[EC] = []
    details: list[str] = []

    dim_values: dict[str, Any] = {
        "tokens": cost.tokens,
        "wallclock": cost.wallclock_seconds,
        "rate_limit": cost.rate_limit_hits,
        "quota": cost.quota_consumed,
        "human_minutes": cost.human_minutes,
        "provider_billed_amount": cost.provider_billed_amount,
    }

    for dim in required_dimensions:
        val = dim_values.get(dim)
        is_unobservable = dim in cost.unobservable_dimensions
        if val is None and not is_unobservable:
            errors.append(EC.EV_COST_INCOMPLETE)
            details.append(
                f"cost dimension {dim} missing and not declared UNOBSERVABLE"
            )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
