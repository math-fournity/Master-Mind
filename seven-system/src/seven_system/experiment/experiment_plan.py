"""ExperimentPlan — WP-EX1 冻结 P4 实验计划。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 84-96 (P4 Preregister):

Freeze:
- TaxonomySnapshot, TellCore, TellStrategyRelease and all component hashes
- arms, contrasts, randomization block/seed
- BranchSnapshot and ResourceContract
- solver/model/profile, repeat and stop
- blind views, endpoints, cost and statistics
- technical failure handling
- audit roles and independence

Plan modification after start must create new ExperimentPlan.

关键约束（blocker）：
- 冻结后不可变（EX_PLAN_MODIFIED_AFTER_START）
- 启动后修改必须创建新 ExperimentPlan
- 所有 arm 必须等资源（EX_ARMS_NOT_EQUAL_RESOURCE）
- 所有 arm 必须共享 BranchSnapshot
- 所有对比必须预注册（EX_CONTRAST_NOT_PREREGISTERED）
- solver/model/profile/repeat/stop 规则冻结

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    EX_ARM_KINDS,
    EX_PLAN_STATES,
    VerificationErrorCode as EC,
)
from .resource_contract import ResourceContract, verify_resource_contract
from .branch_snapshot import BranchSnapshot, verify_branch_snapshot
from .randomization_plan import RandomizationPlan, verify_randomization_plan
from .experiment_arm import ExperimentArm, verify_experiment_arm
from .contrast_spec import ContrastSpec, verify_contrast_spec


_SCHEMA_ID = "seven/experiment-plan"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class ExperimentPlan:
    """冻结 P4 实验计划——不可变，启动后修改必须创建新 plan。

    字段：
        plan_id: 唯一标识
        state: 计划状态（EX_PLAN_STATES: DRAFT/FROZEN/STARTED/COMPLETED/SUPERSEDED）
        arms: 实验臂列表
        contrasts: 对比规格列表
        randomization_plan: 随机化计划
        branch_snapshot: 共享前置状态
        resource_contract: 等资源合同
        solver_spec: solver/model/profile 规格
        repeat_stop_rules: 重复/停止规则
        blind_views: 盲视规格
        endpoints: 终点定义
        cost_statistics: 成本/统计规格
        technical_failure_handling: 技术故障处理
        audit_roles: 审计角色/独立性
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    plan_id: str
    state: str = "DRAFT"
    arms: tuple[ExperimentArm, ...] = ()
    contrasts: tuple[ContrastSpec, ...] = ()
    randomization_plan: RandomizationPlan | None = None
    branch_snapshot: BranchSnapshot | None = None
    resource_contract: ResourceContract | None = None
    solver_spec: dict[str, Any] = field(default_factory=dict)
    repeat_stop_rules: dict[str, Any] = field(default_factory=dict)
    blind_views: dict[str, Any] = field(default_factory=dict)
    endpoints: dict[str, Any] = field(default_factory=dict)
    cost_statistics: dict[str, Any] = field(default_factory=dict)
    technical_failure_handling: dict[str, Any] = field(default_factory=dict)
    audit_roles: dict[str, Any] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "plan_id": self.plan_id,
            "state": self.state,
            "arms": [arm.to_dict() for arm in self.arms],
            "contrasts": [c.to_dict() for c in self.contrasts],
            "randomization_plan": (
                self.randomization_plan.to_dict() if self.randomization_plan else None
            ),
            "branch_snapshot": (
                self.branch_snapshot.to_dict() if self.branch_snapshot else None
            ),
            "resource_contract": (
                self.resource_contract.to_dict() if self.resource_contract else None
            ),
            "solver_spec": dict(self.solver_spec),
            "repeat_stop_rules": dict(self.repeat_stop_rules),
            "blind_views": dict(self.blind_views),
            "endpoints": dict(self.endpoints),
            "cost_statistics": dict(self.cost_statistics),
            "technical_failure_handling": dict(self.technical_failure_handling),
            "audit_roles": dict(self.audit_roles),
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
    def is_frozen(self) -> bool:
        return self.state in ("FROZEN", "STARTED", "COMPLETED")

    @property
    def is_started(self) -> bool:
        return self.state in ("STARTED", "COMPLETED")

    @property
    def arm_kinds(self) -> set[str]:
        return {arm.arm_kind for arm in self.arms}


def make_experiment_plan(
    *,
    plan_id: str,
    arms: list[ExperimentArm] | tuple[ExperimentArm, ...] = (),
    contrasts: list[ContrastSpec] | tuple[ContrastSpec, ...] = (),
    randomization_plan: RandomizationPlan | None = None,
    branch_snapshot: BranchSnapshot | None = None,
    resource_contract: ResourceContract | None = None,
    solver_spec: dict[str, Any] | None = None,
    repeat_stop_rules: dict[str, Any] | None = None,
    blind_views: dict[str, Any] | None = None,
    endpoints: dict[str, Any] | None = None,
    cost_statistics: dict[str, Any] | None = None,
    technical_failure_handling: dict[str, Any] | None = None,
    audit_roles: dict[str, Any] | None = None,
    frozen_at: str = "2026-08-14T12:00:00Z",
) -> ExperimentPlan:
    plan = ExperimentPlan(
        plan_id=plan_id,
        state="FROZEN",
        arms=tuple(arms),
        contrasts=tuple(contrasts),
        randomization_plan=randomization_plan,
        branch_snapshot=branch_snapshot,
        resource_contract=resource_contract,
        solver_spec=solver_spec or {},
        repeat_stop_rules=repeat_stop_rules or {},
        blind_views=blind_views or {},
        endpoints=endpoints or {},
        cost_statistics=cost_statistics or {},
        technical_failure_handling=technical_failure_handling or {},
        audit_roles=audit_roles or {},
        frozen_at=frozen_at,
    )
    return dataclasses.replace(plan, content_hash=plan.compute_content_hash())


@dataclass(frozen=True)
class ExperimentPlanVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    plan_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_experiment_plan(
    plan: ExperimentPlan,
) -> ExperimentPlanVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = plan.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    # state valid
    if plan.state not in EX_PLAN_STATES:
        errors.append(EC.EX_PLAN_STATE_INVALID)
        details.append(
            f"state '{plan.state}' not in {sorted(EX_PLAN_STATES)}"
        )

    # frozen check — plan must be FROZEN or beyond
    if plan.state == "DRAFT":
        errors.append(EC.EX_PLAN_MODIFIED_AFTER_START)
        details.append("plan state is DRAFT — must be FROZEN before experiment")

    # arms
    if not plan.arms:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("arms must not be empty")

    arm_kinds_seen: set[str] = set()
    for arm in plan.arms:
        arm_result = verify_experiment_arm(arm)
        if not arm_result.passed:
            errors.extend(arm_result.error_codes)
            details.extend(arm_result.details)
        arm_kinds_seen.add(arm.arm_kind)

    # all 7 arm kinds present
    if arm_kinds_seen != EX_ARM_KINDS:
        errors.append(EC.EX_ARM_KIND_INVALID)
        details.append(
            f"arm kinds must exactly match EX_ARM_KINDS, "
            f"got {sorted(arm_kinds_seen)}, expected {sorted(EX_ARM_KINDS)}"
        )

    # equal resource check — all arms must reference same resource_contract
    if plan.arms and plan.resource_contract is not None:
        rc_hash = plan.resource_contract.content_hash
        for arm in plan.arms:
            if arm.resource_contract_ref.get("content_hash") != rc_hash:
                errors.append(EC.EX_ARMS_NOT_EQUAL_RESOURCE)
                details.append(
                    f"arm {arm.arm_id} resource_contract_ref hash "
                    f"{arm.resource_contract_ref.get('content_hash')} != "
                    f"plan resource_contract hash {rc_hash}"
                )

    # all arms share same branch_snapshot
    if plan.arms and plan.branch_snapshot is not None:
        bs_hash = plan.branch_snapshot.content_hash
        for arm in plan.arms:
            if arm.branch_snapshot_ref.get("content_hash") != bs_hash:
                errors.append(EC.EX_BRANCH_SNAPSHOT_HASH_MISMATCH)
                details.append(
                    f"arm {arm.arm_id} branch_snapshot_ref hash "
                    f"{arm.branch_snapshot_ref.get('content_hash')} != "
                    f"plan branch_snapshot hash {bs_hash}"
                )

    # resource_contract
    if plan.resource_contract is None:
        errors.append(EC.EX_RESOURCE_CONTRACT_NOT_FROZEN)
        details.append("resource_contract is required")
    else:
        rc_result = verify_resource_contract(plan.resource_contract)
        if not rc_result.passed:
            errors.extend(rc_result.error_codes)
            details.extend(rc_result.details)

    # branch_snapshot
    if plan.branch_snapshot is None:
        errors.append(EC.EX_BRANCH_SNAPSHOT_NOT_FROZEN)
        details.append("branch_snapshot is required")
    else:
        bs_result = verify_branch_snapshot(plan.branch_snapshot)
        if not bs_result.passed:
            errors.extend(bs_result.error_codes)
            details.extend(bs_result.details)

    # randomization_plan
    if plan.randomization_plan is None:
        errors.append(EC.EX_RANDOMIZATION_NOT_REPLAYABLE)
        details.append("randomization_plan is required")
    else:
        rp_result = verify_randomization_plan(plan.randomization_plan)
        if not rp_result.passed:
            errors.extend(rp_result.error_codes)
            details.extend(rp_result.details)

    # contrasts
    if not plan.contrasts:
        errors.append(EC.EX_CONTRAST_NOT_PREREGISTERED)
        details.append("contrasts must not be empty — at least one pre-registered contrast required")

    for contrast in plan.contrasts:
        c_result = verify_contrast_spec(
            contrast, available_arm_kinds=arm_kinds_seen
        )
        if not c_result.passed:
            errors.extend(c_result.error_codes)
            details.extend(c_result.details)

    # solver_spec required
    if not plan.solver_spec:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("solver_spec must not be empty")

    # content_hash
    if not plan.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif plan.content_hash != plan.compute_content_hash():
        errors.append(EC.EX_PLAN_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {plan.content_hash}, "
            f"computed {plan.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return ExperimentPlanVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        plan_id=plan.plan_id,
    )


def check_plan_modified_after_start(
    plan: ExperimentPlan,
    original_hash: str,
) -> bool:
    """检查 plan 是否在启动后被修改。

    返回 True 表示被修改（blocker）。
    """
    if plan.is_started:
        return plan.content_hash != original_hash
    return False
