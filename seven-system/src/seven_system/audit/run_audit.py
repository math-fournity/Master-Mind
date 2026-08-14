"""RunAudit — 从三审 sealed 组装；AuditLaneStatus；CausalEligibility；DisagreementResolution。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P6 节和
docs/implementation/14-evidence-analysis-and-multi-epoch.md：

分别 seal 后组装 RunAudit。单 episode 只陈述观察事实。

单 lane 状态：
    VALID / INVALID_PROTOCOL / INCONCLUSIVE / MISSING / JUDGE_DISAGREEMENT / CONTAMINATED
优先级：CONTAMINATED > INVALID_PROTOCOL > JUDGE_DISAGREEMENT/MISSING/INCONCLUSIVE > VALID
- MISSING/INVALID_PROTOCOL/CONTAMINATED 不能被填成负结果
- 数学 Judge 分歧时，按 AuditPlan 预注册规则增加第三个独立 Judge；
  没有预注册规则时保留 JUDGE_DISAGREEMENT，禁止 Aggregator 自选"看起来对"的报告

RunAudit 因果资格：
    ELIGIBLE | PROCESS_ONLY | RESULT_ONLY | CONTAMINATED | INVALID | INCONCLUSIVE
- 任一确认污染 → CONTAMINATED
- 任一必需 lane 协议无效 → INVALID
- 任一必需 lane 缺失/分歧/不可观测 → INCONCLUSIVE
- 只有 process 有效且结果 lane 按计划不可评 → PROCESS_ONLY
- 只有结果有效且 process 按计划不可评 → RESULT_ONLY
- 全部必需 lane 有效且无 blind/leakage breach → ELIGIBLE
- 除此之外不存在默认分支

关键约束（blocker）：
- 三审必须分别 seal（AU_AUDIT_NOT_SEALED_SEPARATELY）
- seal hash 必须验证（AU_SEAL_HASH_MISMATCH）
- 缺失审计必须记为 MISSING terminal（AU_MISSING_NOT_TERMINAL）
- 污染必须标记（AU_CONTAMINATION_NOT_FLAGGED）
- 分歧不得由 Aggregator 自行裁决（AU_DISAGREEMENT_AUTO_RESOLVED）
- process-only 不得进入 result-layer 因果资格（AU_PROCESS_ONLY_IN_RESULT_LAYER）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    AU_AUDIT_ROLES,
    AU_CAUSAL_ELIGIBILITY_STATUSES,
    AU_CAUSAL_ELIGIBILITY_TRANSITIONS,
    AU_LANE_PRIORITY,
    AU_LANE_STATUSES,
    AU_LANE_TERMINAL_STATUSES,
    AU_LANE_TRANSITIONS,
    AU_RUN_AUDIT_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/run-audit"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


# ─── AuditLaneStatus ────────────────────────────────────────────────────


@dataclass(frozen=True)
class AuditLaneStatus:
    """单个 lane 的终端状态。

    字段：
        lane: lane 名称（AU_AUDIT_ROLES: process_auditor/proof_judge/leakage_auditor）
        status: 终端状态（AU_LANE_STATUSES）
        audit_ref: 对应审计的引用 {audit_id, content_hash}（MISSING 时为空）
        is_terminal: 是否为终态
        upgrade_rule: 升级规则（如 audit_retry 保留原 attempt）
    """

    lane: str
    status: str
    audit_ref: dict[str, str] = field(default_factory=dict)
    is_terminal: bool = True
    upgrade_rule: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "lane": self.lane,
            "status": self.status,
            "audit_ref": dict(self.audit_ref),
            "is_terminal": self.is_terminal,
            "upgrade_rule": self.upgrade_rule,
        }


def is_valid_lane_transition(from_status: str, to_status: str) -> bool:
    """检查 lane 状态转换是否合法。"""
    allowed = AU_LANE_TRANSITIONS.get(from_status, frozenset())
    return to_status in allowed


def lane_priority(status: str) -> int:
    """返回 lane 状态的优先级（数值越大优先级越高）。"""
    return AU_LANE_PRIORITY.get(status, -1)


def aggregate_lane_statuses(
    lane_statuses: list[AuditLaneStatus],
) -> AuditLaneStatus:
    """聚合多个 lane 状态——取最高优先级的无效状态。

    有利 lane 不能平均掉更高优先级的无效状态。
    返回一个代表整体 lane 状态的 AuditLaneStatus（lane="aggregated"）。
    """
    if not lane_statuses:
        return AuditLaneStatus(lane="aggregated", status="MISSING", is_terminal=True)

    # 取最高优先级状态
    highest = max(lane_statuses, key=lambda ls: lane_priority(ls.status))
    return AuditLaneStatus(
        lane="aggregated",
        status=highest.status,
        is_terminal=True,
        upgrade_rule=highest.upgrade_rule,
    )


# ─── CausalEligibility ──────────────────────────────────────────────────


@dataclass(frozen=True)
class CausalEligibility:
    """RunAudit 因果资格——机械地从 P6 三 lane 输入推导。

    字段：
        status: 因果资格（AU_CAUSAL_ELIGIBILITY_STATUSES）
        derived_from_lanes: 推导来源的 lane 状态映射
        blind_breach: 是否有 blind breach
        leakage_breach: 是否有 leakage breach
        is_terminal: 是否为终态
    """

    status: str
    derived_from_lanes: dict[str, str] = field(default_factory=dict)
    blind_breach: bool = False
    leakage_breach: bool = False
    is_terminal: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "derived_from_lanes": dict(self.derived_from_lanes),
            "blind_breach": self.blind_breach,
            "leakage_breach": self.leakage_breach,
            "is_terminal": self.is_terminal,
        }


def derive_causal_eligibility(
    *,
    lane_statuses: dict[str, str],
    required_lanes: tuple[str, ...] = (
        "process_auditor", "proof_judge", "leakage_auditor",
    ),
    blind_breach: bool = False,
    leakage_breach: bool = False,
    process_lane: str = "process_auditor",
    result_lanes: tuple[str, ...] = ("proof_judge", "leakage_auditor"),
) -> CausalEligibility:
    """机械地从 P6 三 lane 输入推导因果资格。

    规则（来自 14-evidence-analysis-and-multi-epoch.md）：
    - 任一确认污染 → CONTAMINATED
    - 任一必需 lane 协议无效 → INVALID
    - 任一必需 lane 缺失/分歧/不可观测 → INCONCLUSIVE
    - 只有 process 有效且结果 lane 按计划不可评 → PROCESS_ONLY
    - 只有结果有效且 process 按计划不可评 → RESULT_ONLY
    - 全部必需 lane 有效且无 blind/leakage breach → ELIGIBLE
    - 除此之外不存在默认分支

    process_lane 是 process 类 lane；result_lanes 是 result 类 lane。
    PROCESS_ONLY 不得进入 result-layer（由调用方保证 result_lanes 不含 process_lane）。
    """
    # 校验：process_lane 不得在 result_lanes 中（process-only 不得进入 result layer）
    if process_lane in result_lanes:
        # 这本身是一个违规，但此处返回 INVALID 表示机械规则拒绝
        return CausalEligibility(
            status="INVALID",
            derived_from_lanes=dict(lane_statuses),
            blind_breach=blind_breach,
            leakage_breach=leakage_breach,
            is_terminal=True,
        )

    # 检查所有 required lane 都有状态
    for lane in required_lanes:
        if lane not in lane_statuses:
            # 缺失 lane 状态 → INCONCLUSIVE
            return CausalEligibility(
                status="INCONCLUSIVE",
                derived_from_lanes=dict(lane_statuses),
                blind_breach=blind_breach,
                leakage_breach=leakage_breach,
                is_terminal=True,
            )

    statuses = {lane: lane_statuses[lane] for lane in required_lanes}

    # 任一确认污染 → CONTAMINATED
    if any(s == "CONTAMINATED" for s in statuses.values()):
        return CausalEligibility(
            status="CONTAMINATED",
            derived_from_lanes=dict(lane_statuses),
            blind_breach=blind_breach,
            leakage_breach=leakage_breach,
            is_terminal=True,
        )

    # blind/leakage breach → CONTAMINATED
    if blind_breach or leakage_breach:
        return CausalEligibility(
            status="CONTAMINATED",
            derived_from_lanes=dict(lane_statuses),
            blind_breach=blind_breach,
            leakage_breach=leakage_breach,
            is_terminal=True,
        )

    # 任一必需 lane 协议无效 → INVALID
    if any(s == "INVALID_PROTOCOL" for s in statuses.values()):
        return CausalEligibility(
            status="INVALID",
            derived_from_lanes=dict(lane_statuses),
            blind_breach=blind_breach,
            leakage_breach=leakage_breach,
            is_terminal=True,
        )

    # 任一必需 lane 缺失/分歧/不可观测 → INCONCLUSIVE
    if any(s in ("MISSING", "JUDGE_DISAGREEMENT", "INCONCLUSIVE") for s in statuses.values()):
        return CausalEligibility(
            status="INCONCLUSIVE",
            derived_from_lanes=dict(lane_statuses),
            blind_breach=blind_breach,
            leakage_breach=leakage_breach,
            is_terminal=True,
        )

    # 此时所有 required lane 都是 VALID
    process_valid = statuses.get(process_lane) == "VALID"
    result_valid = all(statuses.get(l) == "VALID" for l in result_lanes if l in required_lanes)

    # 只有 process 有效且结果 lane 按计划不可评 → PROCESS_ONLY
    # "按计划不可评" = result_lanes 不在 required_lanes 中（计划不要求结果 lane）
    result_required = [l for l in result_lanes if l in required_lanes]
    if process_valid and not result_required:
        return CausalEligibility(
            status="PROCESS_ONLY",
            derived_from_lanes=dict(lane_statuses),
            blind_breach=blind_breach,
            leakage_breach=leakage_breach,
            is_terminal=True,
        )

    # 只有结果有效且 process 按计划不可评 → RESULT_ONLY
    process_required = process_lane in required_lanes
    if result_valid and not process_required:
        return CausalEligibility(
            status="RESULT_ONLY",
            derived_from_lanes=dict(lane_statuses),
            blind_breach=blind_breach,
            leakage_breach=leakage_breach,
            is_terminal=True,
        )

    # 全部必需 lane 有效且无 blind/leakage breach → ELIGIBLE
    if process_valid and result_valid:
        return CausalEligibility(
            status="ELIGIBLE",
            derived_from_lanes=dict(lane_statuses),
            blind_breach=blind_breach,
            leakage_breach=leakage_breach,
            is_terminal=True,
        )

    # 除此之外不存在默认分支 → INCONCLUSIVE
    return CausalEligibility(
        status="INCONCLUSIVE",
        derived_from_lanes=dict(lane_statuses),
        blind_breach=blind_breach,
        leakage_breach=leakage_breach,
        is_terminal=True,
    )


def is_valid_causal_transition(from_status: str, to_status: str) -> bool:
    """检查因果资格转换是否合法。"""
    allowed = AU_CAUSAL_ELIGIBILITY_TRANSITIONS.get(from_status, frozenset())
    return to_status in allowed


# ─── DisagreementResolution ─────────────────────────────────────────────


@dataclass(frozen=True)
class DisagreementResolution:
    """Judge 分歧处理记录。

    未预注册的分歧不得由 Aggregator 自行裁决。分歧被记录，不静默解决。

    字段：
        disagreement_id: 唯一标识
        plan_id: 对应的 AuditPlan ID
        judge_conclusions: 各 Judge 的结论 {judge_id: conclusion}
        is_disagreement: 是否为分歧
        preregistered_rule: 预注册规则引用（空表示无预注册规则）
        resolution: 解决方式
            - "PRESERVED": 保留 JUDGE_DISAGREEMENT（无预注册规则时）
            - "THIRD_JUDGE": 按预注册规则增加第三个独立 Judge
            - "HUMAN_EXPERT": 按预注册规则引入人工专家
            - "FORMAL_CHECKER": 按预注册规则引入 formal checker
        auto_resolved: 是否被 Aggregator 自行裁决（必须为 False）
        recorded: 是否被记录（必须为 True）
    """

    disagreement_id: str
    plan_id: str
    judge_conclusions: dict[str, str] = field(default_factory=dict)
    is_disagreement: bool = False
    preregistered_rule: dict[str, str] = field(default_factory=dict)
    resolution: str = "PRESERVED"
    auto_resolved: bool = False
    recorded: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "disagreement_id": self.disagreement_id,
            "plan_id": self.plan_id,
            "judge_conclusions": dict(self.judge_conclusions),
            "is_disagreement": self.is_disagreement,
            "preregistered_rule": dict(self.preregistered_rule),
            "resolution": self.resolution,
            "auto_resolved": self.auto_resolved,
            "recorded": self.recorded,
        }


def make_disagreement_resolution(
    *,
    disagreement_id: str,
    plan_id: str,
    judge_conclusions: dict[str, str],
    preregistered_rule: dict[str, str] | None = None,
) -> DisagreementResolution:
    """构建分歧处理记录。

    如果有预注册规则，按规则选择 resolution；
    如果没有预注册规则，保留 JUDGE_DISAGREEMENT（PRESERVED）。
    auto_resolved 始终为 False——Aggregator 不得自行裁决。
    """
    conclusions = list(judge_conclusions.values())
    is_disagreement = len(set(conclusions)) > 1

    rule = preregistered_rule or {}
    if not is_disagreement:
        return DisagreementResolution(
            disagreement_id=disagreement_id,
            plan_id=plan_id,
            judge_conclusions=dict(judge_conclusions),
            is_disagreement=False,
            preregistered_rule=dict(rule),
            resolution="NO_DISAGREEMENT",
            auto_resolved=False,
            recorded=True,
        )

    # 有预注册规则 → 按规则
    if rule.get("rule_kind") == "third_judge":
        resolution = "THIRD_JUDGE"
    elif rule.get("rule_kind") == "human_expert":
        resolution = "HUMAN_EXPERT"
    elif rule.get("rule_kind") == "formal_checker":
        resolution = "FORMAL_CHECKER"
    else:
        # 无预注册规则 → 保留 JUDGE_DISAGREEMENT
        resolution = "PRESERVED"

    return DisagreementResolution(
        disagreement_id=disagreement_id,
        plan_id=plan_id,
        judge_conclusions=dict(judge_conclusions),
        is_disagreement=True,
        preregistered_rule=dict(rule),
        resolution=resolution,
        auto_resolved=False,
        recorded=True,
    )


def verify_disagreement_resolution(
    dr: DisagreementResolution,
) -> VerificationResult:
    """验证分歧处理记录。"""
    errors: list[EC] = []
    details: list[str] = []

    if not dr.disagreement_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("disagreement_id is empty")

    if not dr.plan_id:
        errors.append(EC.AU_AUDIT_PLAN_REF_MISSING)
        details.append("plan_id is empty")

    # auto_resolved 必须为 False
    if dr.auto_resolved:
        errors.append(EC.AU_DISAGREEMENT_AUTO_RESOLVED)
        details.append("disagreement must not be auto-resolved by Aggregator")

    # recorded 必须为 True
    if not dr.recorded:
        errors.append(EC.AU_DISAGREEMENT_NOT_RECORDED)
        details.append("disagreement must be recorded, not silently resolved")

    # 如果是分歧但 resolution 是 NO_DISAGREEMENT → 违规
    if dr.is_disagreement and dr.resolution == "NO_DISAGREEMENT":
        errors.append(EC.AU_DISAGREEMENT_AUTO_RESOLVED)
        details.append("disagreement recorded as no_disagreement")

    # 如果是分歧且无预注册规则，resolution 必须为 PRESERVED
    if dr.is_disagreement and not dr.preregistered_rule:
        if dr.resolution != "PRESERVED":
            errors.append(EC.AU_DISAGREEMENT_AUTO_RESOLVED)
            details.append(
                f"disagreement without preregistered rule must be PRESERVED, "
                f"got {dr.resolution}"
            )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# ─── RunAudit ───────────────────────────────────────────────────────────


@dataclass(frozen=True)
class RunAudit:
    """从三审 sealed 组装的 RunAudit。单 episode 只陈述观察事实。

    字段：
        run_audit_id: 唯一标识
        plan_id: 对应的 AuditPlan ID
        bundle_ref: 源 RunArtifactBundle 引用 {bundle_id, content_hash}
        process_audit_ref: ProcessAudit 引用 {audit_id, content_hash}
        proof_judgment_ref: ProofJudgment 引用 {judgment_id, content_hash}
        leakage_audit_ref: LeakageAudit 引用 {audit_id, content_hash}
        lane_statuses: 三个 lane 的终端状态
        causal_eligibility: 因果资格
        disagreement_resolution: 分歧处理记录（如有）
        observed_facts: 观察事实列表（单 episode，只陈述事实）
        state: 组装状态（AU_RUN_AUDIT_STATES）
        sealed: 是否已 seal（组装后整体 seal）
        content_hash: 内容哈希
    """

    run_audit_id: str
    plan_id: str
    bundle_ref: dict[str, str] = field(default_factory=dict)
    process_audit_ref: dict[str, str] = field(default_factory=dict)
    proof_judgment_ref: dict[str, str] = field(default_factory=dict)
    leakage_audit_ref: dict[str, str] = field(default_factory=dict)
    lane_statuses: dict[str, str] = field(default_factory=dict)
    causal_eligibility: str = "INCONCLUSIVE"
    disagreement_resolution: dict[str, Any] = field(default_factory=dict)
    observed_facts: list[dict[str, Any]] = field(default_factory=list)
    state: str = "PENDING"
    sealed: bool = False
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "run_audit_id": self.run_audit_id,
            "plan_id": self.plan_id,
            "bundle_ref": dict(self.bundle_ref),
            "process_audit_ref": dict(self.process_audit_ref),
            "proof_judgment_ref": dict(self.proof_judgment_ref),
            "leakage_audit_ref": dict(self.leakage_audit_ref),
            "lane_statuses": dict(self.lane_statuses),
            "causal_eligibility": self.causal_eligibility,
            "disagreement_resolution": dict(self.disagreement_resolution),
            "observed_facts": [dict(f) for f in self.observed_facts],
            "state": self.state,
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


def make_run_audit(
    *,
    run_audit_id: str,
    plan_id: str,
    bundle_ref: dict[str, str],
    process_audit_ref: dict[str, str],
    proof_judgment_ref: dict[str, str],
    leakage_audit_ref: dict[str, str],
    lane_statuses: dict[str, str],
    causal_eligibility: str,
    disagreement_resolution: dict[str, Any] | None = None,
    observed_facts: list[dict[str, Any]] | None = None,
    state: str = "ASSEMBLED",
    sealed: bool = True,
) -> RunAudit:
    run_audit = RunAudit(
        run_audit_id=run_audit_id,
        plan_id=plan_id,
        bundle_ref=bundle_ref,
        process_audit_ref=process_audit_ref,
        proof_judgment_ref=proof_judgment_ref,
        leakage_audit_ref=leakage_audit_ref,
        lane_statuses=dict(lane_statuses),
        causal_eligibility=causal_eligibility,
        disagreement_resolution=disagreement_resolution or {},
        observed_facts=observed_facts or [],
        state=state,
        sealed=sealed,
    )
    return dataclasses.replace(run_audit, content_hash=run_audit.compute_content_hash())


@dataclass(frozen=True)
class RunAuditVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    run_audit_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_run_audit(
    run_audit: RunAudit,
    *,
    expected_process_hash: str | None = None,
    expected_proof_hash: str | None = None,
    expected_leakage_hash: str | None = None,
) -> RunAuditVerificationResult:
    """验证 RunAudit 的组装合法性。"""
    errors: list[EC] = []
    details: list[str] = []

    d = run_audit.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not run_audit.run_audit_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("run_audit_id is empty")

    if not run_audit.plan_id:
        errors.append(EC.AU_AUDIT_PLAN_REF_MISSING)
        details.append("plan_id is empty")

    # bundle_ref required
    if not run_audit.bundle_ref.get("bundle_id"):
        errors.append(EC.AU_BUNDLE_REF_MISSING)
        details.append("bundle_ref missing bundle_id")

    # 三审引用必须齐全——但 MISSING lane 允许空引用
    process_status = run_audit.lane_statuses.get("process_auditor", "")
    proof_status = run_audit.lane_statuses.get("proof_judge", "")
    leakage_status = run_audit.lane_statuses.get("leakage_auditor", "")

    if not run_audit.process_audit_ref.get("audit_id"):
        if process_status != "MISSING":
            errors.append(EC.AU_AUDIT_REF_MISSING)
            details.append("process_audit_ref missing audit_id")
    if not run_audit.proof_judgment_ref.get("judgment_id"):
        if proof_status != "MISSING":
            errors.append(EC.AU_AUDIT_REF_MISSING)
            details.append("proof_judgment_ref missing judgment_id")
    if not run_audit.leakage_audit_ref.get("audit_id"):
        if leakage_status != "MISSING":
            errors.append(EC.AU_AUDIT_REF_MISSING)
            details.append("leakage_audit_ref missing audit_id")

    # seal hash 验证
    if expected_process_hash is not None:
        if run_audit.process_audit_ref.get("content_hash") != expected_process_hash:
            errors.append(EC.AU_SEAL_HASH_MISMATCH)
            details.append("process_audit_ref content_hash mismatch")
    if expected_proof_hash is not None:
        if run_audit.proof_judgment_ref.get("content_hash") != expected_proof_hash:
            errors.append(EC.AU_SEAL_HASH_MISMATCH)
            details.append("proof_judgment_ref content_hash mismatch")
    if expected_leakage_hash is not None:
        if run_audit.leakage_audit_ref.get("content_hash") != expected_leakage_hash:
            errors.append(EC.AU_SEAL_HASH_MISMATCH)
            details.append("leakage_audit_ref content_hash mismatch")

    # lane_statuses 必须覆盖三个 lane
    for lane in AU_AUDIT_ROLES:
        if lane not in run_audit.lane_statuses:
            errors.append(EC.AU_LANE_STATUS_INVALID)
            details.append(f"lane_statuses missing lane {lane}")
        else:
            status = run_audit.lane_statuses[lane]
            if status not in AU_LANE_STATUSES:
                errors.append(EC.AU_LANE_STATUS_INVALID)
                details.append(
                    f"lane {lane} status {status} not in AU_LANE_STATUSES"
                )
            # MISSING 必须是合法 terminal
            if status == "MISSING":
                if status not in AU_LANE_TERMINAL_STATUSES:
                    errors.append(EC.AU_MISSING_NOT_TERMINAL)
                    details.append(f"lane {lane} MISSING not recorded as terminal")

    # causal_eligibility 必须合法
    if run_audit.causal_eligibility not in AU_CAUSAL_ELIGIBILITY_STATUSES:
        errors.append(EC.AU_CAUSAL_ELIGIBILITY_INVALID)
        details.append(
            f"causal_eligibility {run_audit.causal_eligibility} not in "
            f"AU_CAUSAL_ELIGIBILITY_STATUSES"
        )

    # process-only 不得进入 result-layer
    # 检查方式：如果 causal_eligibility 是 RESULT_ONLY 或 ELIGIBLE，
    # 但 process lane 不是 VALID，则违规
    if run_audit.causal_eligibility in ("RESULT_ONLY", "ELIGIBLE"):
        process_status = run_audit.lane_statuses.get("process_auditor", "")
        if process_status != "VALID":
            errors.append(EC.AU_PROCESS_ONLY_IN_RESULT_LAYER)
            details.append(
                f"causal_eligibility {run_audit.causal_eligibility} requires "
                f"process_auditor VALID, got {process_status}"
            )
    # 如果 causal_eligibility 是 PROCESS_ONLY，result lane 不得是 VALID
    if run_audit.causal_eligibility == "PROCESS_ONLY":
        for rlane in ("proof_judge", "leakage_auditor"):
            rstatus = run_audit.lane_statuses.get(rlane, "")
            if rstatus == "VALID":
                errors.append(EC.AU_PROCESS_ONLY_IN_RESULT_LAYER)
                details.append(
                    f"causal_eligibility PROCESS_ONLY but result lane {rlane} "
                    f"is VALID — process-only entered result layer"
                )

    # state 必须合法
    if run_audit.state not in AU_RUN_AUDIT_STATES:
        errors.append(EC.AU_RUN_AUDIT_STATE_INVALID)
        details.append(
            f"state {run_audit.state} not in AU_RUN_AUDIT_STATES"
        )

    # ASSEMBLED 状态必须 sealed
    if run_audit.state == "ASSEMBLED" and not run_audit.sealed:
        errors.append(EC.AU_AUDIT_NOT_SEALED_SEPARATELY)
        details.append("ASSEMBLED run audit must be sealed")

    # observed_facts 必须是观察事实
    for fact in run_audit.observed_facts:
        if not isinstance(fact, dict) or not fact.get("observed", False):
            errors.append(EC.AU_OBSERVATION_NOT_FACT)
            details.append("observed_facts contains non-observed fact")
            break

    # content_hash
    if not run_audit.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif run_audit.content_hash != run_audit.compute_content_hash():
        errors.append(EC.AU_SEAL_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {run_audit.content_hash}, "
            f"computed {run_audit.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return RunAuditVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        run_audit_id=run_audit.run_audit_id,
    )


# ─── RunAuditAssembler — 纯程序 Aggregator ──────────────────────────────


@dataclass
class RunAuditAssembler:
    """纯程序 Aggregator——从三审 sealed 组装 RunAudit。

    硬约束：
    - 三审必须分别 sealed
    - 缺失审计必须记为 MISSING terminal
    - 污染必须标记
    - 分歧不得由 Aggregator 自行裁决
    - 单 episode 只陈述观察事实
    """

    def assemble(
        self,
        *,
        run_audit_id: str,
        plan_id: str,
        bundle_ref: dict[str, str],
        process_audit: Any | None = None,
        proof_judgment: Any | None = None,
        leakage_audit: Any | None = None,
        required_lanes: tuple[str, ...] = (
            "process_auditor", "proof_judge", "leakage_auditor",
        ),
        preregistered_disagreement_rule: dict[str, str] | None = None,
        blind_breach: bool = False,
        leakage_breach: bool = False,
    ) -> tuple[RunAuditVerificationResult, RunAudit | None]:
        """从三审 sealed 组装 RunAudit。

        缺失的审计记为 MISSING terminal。
        返回 (verification_result, run_audit)。
        """
        errors: list[EC] = []
        details: list[str] = []

        # 构建 lane_statuses
        lane_statuses: dict[str, str] = {}
        process_ref: dict[str, str] = {}
        proof_ref: dict[str, str] = {}
        leakage_ref: dict[str, str] = {}

        # ProcessAudit
        if process_audit is not None:
            if not process_audit.sealed:
                errors.append(EC.AU_AUDIT_NOT_SEALED_SEPARATELY)
                details.append("process audit not sealed separately")
            else:
                process_ref = {
                    "audit_id": process_audit.audit_id,
                    "content_hash": process_audit.content_hash,
                }
                lane_statuses["process_auditor"] = process_audit.lane_status
        else:
            if "process_auditor" in required_lanes:
                lane_statuses["process_auditor"] = "MISSING"
            else:
                lane_statuses["process_auditor"] = "VALID"

        # ProofJudgment
        if proof_judgment is not None:
            if not proof_judgment.sealed:
                errors.append(EC.AU_AUDIT_NOT_SEALED_SEPARATELY)
                details.append("proof judgment not sealed separately")
            else:
                proof_ref = {
                    "judgment_id": proof_judgment.judgment_id,
                    "content_hash": proof_judgment.content_hash,
                }
                lane_statuses["proof_judge"] = proof_judgment.lane_status
        else:
            if "proof_judge" in required_lanes:
                lane_statuses["proof_judge"] = "MISSING"
            else:
                lane_statuses["proof_judge"] = "VALID"

        # LeakageAudit
        if leakage_audit is not None:
            if not leakage_audit.sealed:
                errors.append(EC.AU_AUDIT_NOT_SEALED_SEPARATELY)
                details.append("leakage audit not sealed separately")
            else:
                leakage_ref = {
                    "audit_id": leakage_audit.audit_id,
                    "content_hash": leakage_audit.content_hash,
                }
                lane_statuses["leakage_auditor"] = leakage_audit.lane_status
        else:
            if "leakage_auditor" in required_lanes:
                lane_statuses["leakage_auditor"] = "MISSING"
            else:
                lane_statuses["leakage_auditor"] = "VALID"

        # 污染检查
        if leakage_audit is not None:
            contamination_detected = leakage_audit.solver_payload_analysis.get(
                "contamination_detected", False
            )
            if contamination_detected and not leakage_audit.contamination_flagged:
                errors.append(EC.AU_CONTAMINATION_NOT_FLAGGED)
                details.append("contamination detected but not flagged")

        # 分歧处理
        disagreement_dict: dict[str, Any] = {}
        if proof_judgment is not None and "proof_judge" in lane_statuses:
            if lane_statuses["proof_judge"] == "JUDGE_DISAGREEMENT":
                # 构建分歧处理记录
                judge_conclusions = proof_judgment.math_correctness.get(
                    "judge_conclusions", {}
                )
                if not judge_conclusions:
                    judge_conclusions = {"judge_a": proof_judgment.conclusion}
                dr = make_disagreement_resolution(
                    disagreement_id=f"disagree-{run_audit_id}",
                    plan_id=plan_id,
                    judge_conclusions=judge_conclusions,
                    preregistered_rule=preregistered_disagreement_rule,
                )
                dr_result = verify_disagreement_resolution(dr)
                if not dr_result.passed:
                    errors.extend(dr_result.error_codes)
                    details.extend(dr_result.details)
                disagreement_dict = dr.to_dict()

        # 推导因果资格
        causal = derive_causal_eligibility(
            lane_statuses=lane_statuses,
            required_lanes=required_lanes,
            blind_breach=blind_breach,
            leakage_breach=leakage_breach,
        )

        if errors:
            # 即使有错误也构建一个 INCOMPLETE 的 run audit 用于返回
            run_audit = make_run_audit(
                run_audit_id=run_audit_id,
                plan_id=plan_id,
                bundle_ref=bundle_ref,
                process_audit_ref=process_ref,
                proof_judgment_ref=proof_ref,
                leakage_audit_ref=leakage_ref,
                lane_statuses=lane_statuses,
                causal_eligibility=causal.status,
                disagreement_resolution=disagreement_dict,
                state="INCOMPLETE",
                sealed=False,
            )
            return RunAuditVerificationResult(
                verdict="FAIL",
                error_codes=errors,
                details=details,
                run_audit_id=run_audit_id,
            ), run_audit

        run_audit = make_run_audit(
            run_audit_id=run_audit_id,
            plan_id=plan_id,
            bundle_ref=bundle_ref,
            process_audit_ref=process_ref,
            proof_judgment_ref=proof_ref,
            leakage_audit_ref=leakage_ref,
            lane_statuses=lane_statuses,
            causal_eligibility=causal.status,
            disagreement_resolution=disagreement_dict,
            state="ASSEMBLED",
            sealed=True,
        )

        result = verify_run_audit(run_audit)
        return result, run_audit
