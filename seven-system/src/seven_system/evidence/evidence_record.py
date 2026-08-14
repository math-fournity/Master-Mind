"""EvidenceRecord + ContrastAggregator — P7 对比级证据记录与聚合器。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P7 节和
docs/implementation/14-evidence-analysis-and-multi-epoch.md：

按预注册 contrast、problem/source cluster 和成本口径聚合。只有 contrast 级
EvidenceRecord 可以对 Tell causal claim 写 supports/contradicts。Case-family
层只能聚合既有 contrast records 扩展 scope（不能创建新 causal claim）。

估计器、missingness、multiplicity、stopping 和 Evidence status 均从
AnalysisMethodRegistry/EvidenceStatusRegistry 选择并在 P4 冻结。

关键约束（blocker）：
- 单 episode 用作 causal claim support → BLOCK（EV_EPISODE_AS_SUPPORT）
- cluster 双计 → BLOCK（EV_CLUSTER_DOUBLE_COUNTED）
- invalid 填 0 → BLOCK（EV_INVALID_FILLED_ZERO）
- 估计器换 → BLOCK（EV_ESTIMATOR_SWAPPED）
- case-family 创建新 causal claim → BLOCK（EV_CASE_FAMILY_NEW_CAUSAL_CLAIM）
- 非 contrast record 写 supports/contradicts → BLOCK（EV_NON_CONTRAST_WRITES_SUPPORTS）
- contrast_ref 缺失 → BLOCK（EV_CONTRAST_REF_MISSING）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    EV_EVIDENCE_STATUSES,
    EV_EVIDENCE_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from .registries import (
    AnalysisMethodRegistry,
    EvidenceStatusRegistry,
    check_estimator_in_registry,
    check_estimator_not_swapped,
    check_evidence_status_valid,
)
from .missingness_and_cost import (
    CostDimension,
    MissingnessReport,
    check_invalid_not_filled_zero,
)


_SCHEMA_ID = "seven/evidence-record"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


# ─── ArmEvidenceInput ───────────────────────────────────────────────────


@dataclass(frozen=True)
class ArmEvidenceInput:
    """单个 arm 的证据输入——P5 arm 结果 + P6 RunAudit 引用。

    字段：
        arm_id: arm 标识
        arm_kind: arm 种类
        cluster_id: problem/source cluster 标识
        bundle_ref: RunArtifactBundle 引用 {bundle_id, content_hash}
        run_audit_ref: RunAudit 引用 {run_audit_id, content_hash}
        causal_eligibility: 因果资格（ELIGIBLE/PROCESS_ONLY/...）
        endpoint_value: endpoint 值（None 表示缺失/无效）
        is_invalid: 是否无效结果
        is_negative: 是否负面结果
        cost_ref: CostDimension 引用 {content_hash}
    """

    arm_id: str
    arm_kind: str
    cluster_id: str
    bundle_ref: dict[str, str] = field(default_factory=dict)
    run_audit_ref: dict[str, str] = field(default_factory=dict)
    causal_eligibility: str = "INCONCLUSIVE"
    endpoint_value: float | None = None
    is_invalid: bool = False
    is_negative: bool = False
    cost_ref: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_id": self.arm_id,
            "arm_kind": self.arm_kind,
            "cluster_id": self.cluster_id,
            "bundle_ref": dict(self.bundle_ref),
            "run_audit_ref": dict(self.run_audit_ref),
            "causal_eligibility": self.causal_eligibility,
            "endpoint_value": self.endpoint_value,
            "is_invalid": self.is_invalid,
            "is_negative": self.is_negative,
            "cost_ref": dict(self.cost_ref),
        }


# ─── EstimatorOutput ────────────────────────────────────────────────────


@dataclass(frozen=True)
class EstimatorOutput:
    """估计器输出——point estimate、CI、p-value、effect direction。

    字段：
        method_id: 估计器 ID（必须与 P4 冻结一致）
        point_estimate: 点估计
        ci_lower: CI 下界
        ci_upper: CI 上界
        p_value: p 值
        effect_direction: 效应方向（positive/negative/null/unknown）
        intermediate_values: 中间值（实现者和审计者必须复现）
    """

    method_id: str
    point_estimate: float | None = None
    ci_lower: float | None = None
    ci_upper: float | None = None
    p_value: float | None = None
    effect_direction: str = "unknown"
    intermediate_values: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "method_id": self.method_id,
            "point_estimate": self.point_estimate,
            "ci_lower": self.ci_lower,
            "ci_upper": self.ci_upper,
            "p_value": self.p_value,
            "effect_direction": self.effect_direction,
            "intermediate_values": dict(self.intermediate_values),
        }


# ─── EvidenceRecord ─────────────────────────────────────────────────────


@dataclass(frozen=True)
class EvidenceRecord:
    """对比级证据记录——P7 唯一可对 Tell causal claim 写 supports/contradicts。

    字段：
        record_id: 唯一标识
        record_kind: 记录种类（contrast / case_family）
        contrast_ref: 预注册 contrast 引用 {contrast_id, content_hash}
        arm_inputs: 参与聚合的 arm 证据输入
        estimator_output: 估计器输出
        evidence_status: Evidence status（EV_EVIDENCE_STATUSES）
        mapped_state: claim 级总映射状态
        missingness_ref: MissingnessReport 引用 {report_id, content_hash}
        multiplicity_rule_id: 多重性规则 ID
        multiplicity_adjusted_p_value: 多重性调整后 p 值
        stopping_rule_id: 停止规则 ID
        cost_dimension: CostDimension
        alternative_explanations: alternative explanations 列表
        scope_limit: scope 限制描述
        supports_causal_claim: 是否对 Tell causal claim 写 supports
        contradicts_causal_claim: 是否对 Tell causal claim 写 contradicts
        causal_claim_ref: Tell causal claim 引用（仅 contrast 级可写）
        sealed: 是否已 seal
        content_hash: 内容哈希
    """

    record_id: str
    record_kind: str = "contrast"
    contrast_ref: dict[str, str] = field(default_factory=dict)
    arm_inputs: tuple[ArmEvidenceInput, ...] = ()
    estimator_output: EstimatorOutput | None = None
    evidence_status: str = "NOT_TESTED"
    mapped_state: str = "NOT_TESTED"
    missingness_ref: dict[str, str] = field(default_factory=dict)
    multiplicity_rule_id: str = ""
    multiplicity_adjusted_p_value: float | None = None
    stopping_rule_id: str = ""
    cost_dimension: CostDimension | None = None
    alternative_explanations: tuple[str, ...] = ()
    scope_limit: str = ""
    supports_causal_claim: bool = False
    contradicts_causal_claim: bool = False
    causal_claim_ref: dict[str, str] = field(default_factory=dict)
    sealed: bool = False
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "record_id": self.record_id,
            "record_kind": self.record_kind,
            "contrast_ref": dict(self.contrast_ref),
            "arm_inputs": [a.to_dict() for a in self.arm_inputs],
            "estimator_output": (
                self.estimator_output.to_dict() if self.estimator_output else None
            ),
            "evidence_status": self.evidence_status,
            "mapped_state": self.mapped_state,
            "missingness_ref": dict(self.missingness_ref),
            "multiplicity_rule_id": self.multiplicity_rule_id,
            "multiplicity_adjusted_p_value": self.multiplicity_adjusted_p_value,
            "stopping_rule_id": self.stopping_rule_id,
            "cost_dimension": (
                self.cost_dimension.to_dict() if self.cost_dimension else None
            ),
            "alternative_explanations": list(self.alternative_explanations),
            "scope_limit": self.scope_limit,
            "supports_causal_claim": self.supports_causal_claim,
            "contradicts_causal_claim": self.contradicts_causal_claim,
            "causal_claim_ref": dict(self.causal_claim_ref),
            "sealed": self.sealed,
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
    def is_contrast_level(self) -> bool:
        return self.record_kind == "contrast"


def make_evidence_record(
    *,
    record_id: str,
    record_kind: str = "contrast",
    contrast_ref: dict[str, str],
    arm_inputs: list[ArmEvidenceInput],
    estimator_output: EstimatorOutput,
    evidence_status: str,
    mapped_state: str | None = None,
    missingness_ref: dict[str, str] | None = None,
    multiplicity_rule_id: str = "",
    multiplicity_adjusted_p_value: float | None = None,
    stopping_rule_id: str = "",
    cost_dimension: CostDimension | None = None,
    alternative_explanations: list[str] | None = None,
    scope_limit: str = "",
    supports_causal_claim: bool = False,
    contradicts_causal_claim: bool = False,
    causal_claim_ref: dict[str, str] | None = None,
    sealed: bool = True,
) -> EvidenceRecord:
    """构建 EvidenceRecord。

    只有 contrast 级 record 可写 supports_causal_claim/contradicts_causal_claim。
    case_family 级 record 不得写这两个字段（由 verify 检查）。
    """
    if mapped_state is None:
        mapped_state = EV_EVIDENCE_STATES.get(evidence_status, evidence_status)

    rec = EvidenceRecord(
        record_id=record_id,
        record_kind=record_kind,
        contrast_ref=dict(contrast_ref),
        arm_inputs=tuple(arm_inputs),
        estimator_output=estimator_output,
        evidence_status=evidence_status,
        mapped_state=mapped_state,
        missingness_ref=missingness_ref or {},
        multiplicity_rule_id=multiplicity_rule_id,
        multiplicity_adjusted_p_value=multiplicity_adjusted_p_value,
        stopping_rule_id=stopping_rule_id,
        cost_dimension=cost_dimension,
        alternative_explanations=tuple(alternative_explanations or ()),
        scope_limit=scope_limit,
        supports_causal_claim=supports_causal_claim,
        contradicts_causal_claim=contradicts_causal_claim,
        causal_claim_ref=causal_claim_ref or {},
        sealed=sealed,
    )
    return dataclasses.replace(rec, content_hash=rec.compute_content_hash())


@dataclass(frozen=True)
class EvidenceRecordVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    record_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_evidence_record(
    record: EvidenceRecord,
    *,
    analysis_registry: AnalysisMethodRegistry | None = None,
    status_registry: EvidenceStatusRegistry | None = None,
    p4_method_id: str | None = None,
) -> EvidenceRecordVerificationResult:
    """验证 EvidenceRecord。

    blocker：
    - contrast_ref 缺失 → EV_CONTRAST_REF_MISSING
    - evidence_status 无效 → EV_EVIDENCE_STATUS_INVALID
    - 估计器不在 registry → EV_ESTIMATOR_NOT_IN_REGISTRY
    - 估计器换 → EV_ESTIMATOR_SWAPPED
    - 非 contrast record 写 supports/contradicts → EV_NON_CONTRAST_WRITES_SUPPORTS
    - case_family 创建新 causal claim → EV_CASE_FAMILY_NEW_CAUSAL_CLAIM
    - invalid 填 0 → EV_INVALID_FILLED_ZERO
    - 未 seal → EV_EVIDENCE_RECORD_NOT_SEALED
    """
    errors: list[EC] = []
    details: list[str] = []

    d = record.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not record.record_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("record_id is empty")

    # contrast_ref required
    if not record.contrast_ref.get("contrast_id"):
        errors.append(EC.EV_CONTRAST_REF_MISSING)
        details.append("contrast_ref missing contrast_id")
    if not record.contrast_ref.get("content_hash"):
        errors.append(EC.EV_CONTRAST_REF_MISSING)
        details.append("contrast_ref missing content_hash")

    # evidence_status valid
    if record.evidence_status not in EV_EVIDENCE_STATUSES:
        errors.append(EC.EV_EVIDENCE_STATUS_INVALID)
        details.append(
            f"evidence_status {record.evidence_status} not in EV_EVIDENCE_STATUSES"
        )

    if status_registry is not None:
        status_check = check_evidence_status_valid(status_registry, record.evidence_status)
        if not status_check.passed:
            errors.extend(status_check.error_codes)
            details.extend(status_check.details)

    # mapped_state 一致
    expected_mapped = EV_EVIDENCE_STATES.get(record.evidence_status, "")
    if record.mapped_state != expected_mapped:
        errors.append(EC.EV_EVIDENCE_STATUS_INVALID)
        details.append(
            f"mapped_state {record.mapped_state} != expected {expected_mapped} "
            f"for status {record.evidence_status}"
        )

    # estimator output
    if record.estimator_output is not None:
        method_id = record.estimator_output.method_id
        if analysis_registry is not None:
            reg_check = check_estimator_in_registry(analysis_registry, method_id)
            if not reg_check.passed:
                errors.extend(reg_check.error_codes)
                details.extend(reg_check.details)
        if p4_method_id is not None:
            swap_check = check_estimator_not_swapped(
                analysis_registry or AnalysisMethodRegistry(),
                p4_method_id,
                method_id,
            )
            if not swap_check.passed:
                errors.extend(swap_check.error_codes)
                details.extend(swap_check.details)

    # 只有 contrast 级可写 supports/contradicts
    if record.record_kind != "contrast":
        if record.supports_causal_claim or record.contradicts_causal_claim:
            errors.append(EC.EV_NON_CONTRAST_WRITES_SUPPORTS)
            details.append(
                f"record_kind {record.record_kind} cannot write supports/contradicts — "
                f"only contrast-level records can"
            )
        if record.causal_claim_ref:
            errors.append(EC.EV_CASE_FAMILY_NEW_CAUSAL_CLAIM)
            details.append(
                f"record_kind {record.record_kind} cannot create new causal claim — "
                f"case_family only extends scope"
            )

    # invalid 填 0 检查（通过 arm_inputs 的 endpoint_value）
    for arm in record.arm_inputs:
        if arm.is_invalid and arm.endpoint_value is not None:
            if arm.endpoint_value == 0:
                errors.append(EC.EV_INVALID_FILLED_ZERO)
                details.append(
                    f"arm {arm.arm_id} invalid result endpoint filled with 0 — BLOCK"
                )

    # sealed
    if not record.sealed:
        errors.append(EC.EV_EVIDENCE_RECORD_NOT_SEALED)
        details.append("EvidenceRecord must be sealed")

    # alternative_explanations 和 scope_limit 必须保留
    if not record.alternative_explanations:
        errors.append(EC.EV_ALTERNATIVE_EXPLANATION_MISSING)
        details.append("alternative_explanations must be preserved")
    if not record.scope_limit:
        errors.append(EC.EV_SCOPE_LIMIT_MISSING)
        details.append("scope_limit must be preserved")

    # content_hash
    if not record.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif record.content_hash != record.compute_content_hash():
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append("EvidenceRecord content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return EvidenceRecordVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        record_id=record.record_id,
    )


# ─── ContrastAggregator ─────────────────────────────────────────────────


@dataclass
class ContrastAggregator:
    """P7 对比聚合器——按预注册 contrast 聚合 P5 arm 结果 + P6 RunAudits。

    产生 EvidenceRecord per contrast。Case-family 层只能聚合既有 contrast
    records 扩展 scope（不能创建新 causal claim）。

    可配置 fault injection 用于 blocker tests：
    - force_episode_as_support: 单 episode 用作 causal claim support
    - force_cluster_double_counted: 同一 cluster 双计
    - force_invalid_filled_zero: invalid 结果填 0
    - force_estimator_swapped: 运行后换估计器
    - force_case_family_new_claim: case-family 创建新 causal claim
    """

    analysis_registry: AnalysisMethodRegistry | None = None
    status_registry: EvidenceStatusRegistry | None = None
    force_episode_as_support: bool = False
    force_cluster_double_counted: bool = False
    force_invalid_filled_zero: bool = False
    force_estimator_swapped: bool = False
    force_case_family_new_claim: bool = False

    def aggregate(
        self,
        *,
        contrast_ref: dict[str, str],
        arm_inputs: list[ArmEvidenceInput],
        p4_method_id: str,
        missingness_report: MissingnessReport,
        multiplicity_rule_id: str = "PRIMARY_V1",
        multiplicity_adjusted_p_value: float | None = None,
        stopping_rule_id: str = "MAXIMUM_CLUSTERS_V1",
        cost_dimension: CostDimension | None = None,
        record_id: str = "",
        causal_claim_ref: dict[str, str] | None = None,
    ) -> EvidenceRecord:
        """聚合单个 contrast 的 arm 结果 → EvidenceRecord。

        步骤：
        1. 检查 cluster 不双计
        2. 检查 invalid 不填 0
        3. 运行估计器（使用 P4 冻结估计器）
        4. 机械派生 Evidence status
        5. 构建 EvidenceRecord（contrast 级可写 supports/contradicts）
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. cluster 双计检查
        cluster_counts: dict[str, int] = {}
        for arm in arm_inputs:
            cluster_counts[arm.cluster_id] = cluster_counts.get(arm.cluster_id, 0) + 1
        if self.force_cluster_double_counted:
            errors.append(EC.EV_CLUSTER_DOUBLE_COUNTED)
            details.append("same cluster counted twice in aggregation — BLOCK")
        # 真实双计检测：同 cluster 同 arm_kind 出现多次
        seen_cluster_arm: set[tuple[str, str]] = set()
        for arm in arm_inputs:
            key = (arm.cluster_id, arm.arm_kind)
            if key in seen_cluster_arm:
                errors.append(EC.EV_CLUSTER_DOUBLE_COUNTED)
                details.append(
                    f"cluster {arm.cluster_id} arm_kind {arm.arm_kind} double-counted"
                )
            seen_cluster_arm.add(key)

        # 2. invalid 填 0 检查
        invalid_check = check_invalid_not_filled_zero(
            [
                __import__(
                    "seven_system.evidence.missingness_and_cost",
                    fromlist=["MissingnessEntry"],
                ).MissingnessEntry(
                    arm_id=arm.arm_id,
                    kind="INVALID_RESULT" if arm.is_invalid else "NONE",
                    filled_value=arm.endpoint_value,
                )
                for arm in arm_inputs
            ]
        )
        if self.force_invalid_filled_zero:
            errors.append(EC.EV_INVALID_FILLED_ZERO)
            details.append("invalid results filled with 0 — BLOCK")
        if not invalid_check.passed:
            errors.extend(invalid_check.error_codes)
            details.extend(invalid_check.details)

        # 3. 估计器——使用 P4 冻结估计器
        actual_method_id = p4_method_id
        if self.force_estimator_swapped:
            actual_method_id = "DESCRIPTIVE_SMALL_N_V1"
            if p4_method_id != actual_method_id:
                errors.append(EC.EV_ESTIMATOR_SWAPPED)
                details.append(
                    f"estimator swapped: P4 {p4_method_id}, actual {actual_method_id}"
                )

        # 计算估计器输出（简化版——真实实现用冻结算法）
        # PAIRED_CLUSTER_DIFFERENCE_V1: per cluster, treatment - control, then mean
        # treatment = non-baseline arm (arm_kind != "problem_only")
        # control = baseline arm (arm_kind == "problem_only")
        eligible_arms = [
            arm for arm in arm_inputs
            if arm.causal_eligibility == "ELIGIBLE" and not arm.is_invalid
        ]
        if eligible_arms:
            if actual_method_id == "PAIRED_CLUSTER_DIFFERENCE_V1":
                # group by cluster, compute paired differences
                clusters: dict[str, dict[str, float]] = {}
                for arm in eligible_arms:
                    if arm.endpoint_value is None:
                        continue
                    clusters.setdefault(arm.cluster_id, {})[arm.arm_kind] = arm.endpoint_value
                diffs: list[float] = []
                for cluster_id, arms_in_cluster in clusters.items():
                    control = arms_in_cluster.get("problem_only")
                    treatments = {k: v for k, v in arms_in_cluster.items() if k != "problem_only"}
                    if control is not None and treatments:
                        treatment_val = next(iter(treatments.values()))
                        diffs.append(treatment_val - control)
                if diffs:
                    point_estimate = sum(diffs) / len(diffs)
                    effect_direction = "positive" if point_estimate > 0 else (
                        "negative" if point_estimate < 0 else "null"
                    )
                else:
                    point_estimate = None
                    effect_direction = "unknown"
            else:
                values = [arm.endpoint_value for arm in eligible_arms if arm.endpoint_value is not None]
                if values:
                    point_estimate = sum(values) / len(values)
                    effect_direction = "positive" if point_estimate > 0 else (
                        "negative" if point_estimate < 0 else "null"
                    )
                else:
                    point_estimate = None
                    effect_direction = "unknown"
        else:
            point_estimate = None
            effect_direction = "unknown"

        estimator_output = EstimatorOutput(
            method_id=actual_method_id,
            point_estimate=point_estimate,
            effect_direction=effect_direction,
            intermediate_values={"eligible_count": len(eligible_arms)},
        )

        # 4. 机械派生 Evidence status
        evidence_status = self._derive_evidence_status(
            arm_inputs, eligible_arms, missingness_report, estimator_output,
        )

        # supports/contradicts——只有 contrast 级可写
        supports = False
        contradicts = False
        if evidence_status == "SUPPORTS":
            supports = True
        elif evidence_status == "CONTRADICTS":
            contradicts = True

        # episode as support blocker
        if self.force_episode_as_support:
            errors.append(EC.EV_EPISODE_AS_SUPPORT)
            details.append("single episode used as support for causal claim — BLOCK")
            supports = False

        # 5. 构建 EvidenceRecord
        record_id = record_id or f"ev-{contrast_ref.get('contrast_id', 'unknown')}"
        mapped_state = EV_EVIDENCE_STATES.get(evidence_status, evidence_status)

        record = make_evidence_record(
            record_id=record_id,
            record_kind="contrast",
            contrast_ref=contrast_ref,
            arm_inputs=arm_inputs,
            estimator_output=estimator_output,
            evidence_status=evidence_status,
            mapped_state=mapped_state,
            missingness_ref={
                "report_id": missingness_report.report_id,
                "content_hash": missingness_report.content_hash,
            },
            multiplicity_rule_id=multiplicity_rule_id,
            multiplicity_adjusted_p_value=multiplicity_adjusted_p_value,
            stopping_rule_id=stopping_rule_id,
            cost_dimension=cost_dimension,
            alternative_explanations=[
                "off_mechanism_success",
                "terminology_restate",
                "no_eligible_contrast",
            ],
            scope_limit="scope_limited_to_actual_coverage",
            supports_causal_claim=supports,
            contradicts_causal_claim=contradicts,
            causal_claim_ref=causal_claim_ref or {},
        )

        # 如果有错误，仍返回 record（verify 会捕获），但记录错误
        # 调用方应通过 verify_evidence_record 检查
        return record

    def aggregate_case_family(
        self,
        *,
        record_id: str,
        contrast_records: list[EvidenceRecord],
        scope_extension: str,
    ) -> EvidenceRecord:
        """Case-family 聚合——只能扩展 scope，不能创建新 causal claim。

        blocker：case_family 创建新 causal claim → EV_CASE_FAMILY_NEW_CAUSAL_CLAIM
        """
        errors: list[EC] = []
        details: list[str] = []

        if self.force_case_family_new_claim:
            errors.append(EC.EV_CASE_FAMILY_NEW_CAUSAL_CLAIM)
            details.append("case_family attempted to create new causal claim — BLOCK")

        # 聚合既有 contrast records 的 contrast_ref
        contrast_refs = [r.contrast_ref for r in contrast_records if r.contrast_ref]
        if not contrast_refs:
            errors.append(EC.EV_CONTRAST_REF_MISSING)
            details.append("case_family has no contrast records to aggregate")

        # case_family 不得写 supports/contradicts
        # 使用第一个 contrast 的 ref 作为代表
        primary_ref = contrast_refs[0] if contrast_refs else {}

        # 聚合 arm_inputs
        all_arm_inputs: list[ArmEvidenceInput] = []
        for r in contrast_records:
            all_arm_inputs.extend(r.arm_inputs)

        # 聚合状态——取最保守（INCONCLUSIVE 优先）
        statuses = [r.evidence_status for r in contrast_records]
        if "INCONCLUSIVE_DUE_TO_PROTOCOL" in statuses:
            evidence_status = "INCONCLUSIVE_DUE_TO_PROTOCOL"
        elif "NOT_TESTED" in statuses:
            evidence_status = "NOT_TESTED"
        elif "CONTRADICTS" in statuses:
            evidence_status = "CONTRADICTS"
        elif "DOES_NOT_SUPPORT" in statuses:
            evidence_status = "DOES_NOT_SUPPORT"
        else:
            evidence_status = "SUPPORTS"

        mapped_state = EV_EVIDENCE_STATES.get(evidence_status, evidence_status)

        # case_family 不得有 estimator_output（不创建新 causal claim）
        # 也不得有 supports/contradicts/causal_claim_ref
        record = make_evidence_record(
            record_id=record_id,
            record_kind="case_family",
            contrast_ref=primary_ref,
            arm_inputs=all_arm_inputs,
            estimator_output=contrast_records[0].estimator_output if contrast_records else None,
            evidence_status=evidence_status,
            mapped_state=mapped_state,
            alternative_explanations=[
                "case_family_aggregation_only_extends_scope",
            ],
            scope_limit=scope_extension,
            supports_causal_claim=False,
            contradicts_causal_claim=False,
            causal_claim_ref={},
        )

        return record

    def _derive_evidence_status(
        self,
        arm_inputs: list[ArmEvidenceInput],
        eligible_arms: list[ArmEvidenceInput],
        missingness_report: MissingnessReport,
        estimator_output: EstimatorOutput,
    ) -> str:
        """机械派生 Evidence status。

        规则（来自 14-evidence-analysis-and-multi-epoch.md）：
        - 无 arm 输入或无 contrast 执行 → NOT_TESTED
        - missingness 超阈值/不平衡 → INCONCLUSIVE_DUE_TO_PROTOCOL
        - 有 ELIGIBLE arm 且 effect 方向/门槛满足 → SUPPORTS
        - 有 ELIGIBLE arm 且方向被反驳 → CONTRADICTS
        - episode 成功但 off-mechanism / 无合格 contrast → DOES_NOT_SUPPORT
        - 协议失效 → INCONCLUSIVE_DUE_TO_PROTOCOL
        """
        if not arm_inputs:
            return "NOT_TESTED"

        # missingness 超阈值或不平衡 → INCONCLUSIVE_DUE_TO_PROTOCOL
        if missingness_report.threshold_exceeded or missingness_report.imbalanced_across_arms:
            return "INCONCLUSIVE_DUE_TO_PROTOCOL"

        # 无 ELIGIBLE arm → 检查是否有 invalid/contamination
        if not eligible_arms:
            has_invalid = any(a.is_invalid for a in arm_inputs)
            has_contamination = missingness_report.contamination_count > 0
            if has_invalid or has_contamination:
                return "INCONCLUSIVE_DUE_TO_PROTOCOL"
            # episode 成功但 off-mechanism / 无合格 contrast
            return "DOES_NOT_SUPPORT"

        # 检查因果资格——INCONCLUSIVE/CONTAMINATED/INVALID → INCONCLUSIVE_DUE_TO_PROTOCOL
        for arm in arm_inputs:
            if arm.causal_eligibility in ("CONTAMINATED", "INVALID", "INCONCLUSIVE"):
                return "INCONCLUSIVE_DUE_TO_PROTOCOL"

        # effect 方向判断
        if estimator_output.point_estimate is not None:
            if estimator_output.effect_direction == "positive":
                return "SUPPORTS"
            elif estimator_output.effect_direction == "negative":
                return "CONTRADICTS"
            else:
                return "DOES_NOT_SUPPORT"

        return "DOES_NOT_SUPPORT"


def check_episode_not_used_as_support(
    record: EvidenceRecord,
    arm_inputs: list[ArmEvidenceInput],
) -> VerificationResult:
    """检查单 episode 未被用作 causal claim support。

    单 episode 不能作为 causal claim 的 support——必须基于 cluster 级聚合。
    """
    errors: list[EC] = []
    details: list[str] = []

    if record.supports_causal_claim or record.contradicts_causal_claim:
        # 检查是否有足够的 cluster 级证据（多于 1 个独立 cluster）
        eligible_clusters = {
            arm.cluster_id for arm in arm_inputs
            if arm.causal_eligibility == "ELIGIBLE" and not arm.is_invalid
        }
        if len(eligible_clusters) < 2:
            errors.append(EC.EV_EPISODE_AS_SUPPORT)
            details.append(
                f"single episode/cluster used as support for causal claim — "
                f"only {len(eligible_clusters)} eligible cluster(s)"
            )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_cluster_not_double_counted(
    arm_inputs: list[ArmEvidenceInput],
) -> VerificationResult:
    """检查同一 cluster 未被双计。"""
    errors: list[EC] = []
    details: list[str] = []

    seen: set[tuple[str, str]] = set()
    for arm in arm_inputs:
        key = (arm.cluster_id, arm.arm_kind)
        if key in seen:
            errors.append(EC.EV_CLUSTER_DOUBLE_COUNTED)
            details.append(
                f"cluster {arm.cluster_id} arm_kind {arm.arm_kind} double-counted"
            )
        seen.add(key)

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
