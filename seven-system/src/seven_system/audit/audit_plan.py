"""AuditPlan — WP-AU1 冻结 P6 审计计划。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P6 节和
docs/implementation/14-evidence-analysis-and-multi-epoch.md：

冻结输入：sealed P5 runs、AuditPlan/views。
AuditPlan 指定：哪些 P5 runs 要审计、哪些审计角色、哪些 adapter、
独立性要求、盲化规格。冻结后不可变。

关键约束（blocker）：
- 冻结后不可变（AU_AUDIT_PLAN_MODIFIED）
- 必须包含三个审计角色（process_auditor / proof_judge / leakage_auditor）
- 每个 role 必须绑定独立 adapter + blinding spec
- 未预注册的分歧规则不得由 Aggregator 自行裁决

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
    AU_VIEW_KINDS,
    VerificationErrorCode as EC,
)


_SCHEMA_ID = "seven/audit-plan"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class AuditRoleBinding:
    """单个审计角色的绑定规格——adapter + blinding spec + independence。

    字段：
        role_type_id: 审计角色（AU_AUDIT_ROLES: process_auditor/proof_judge/leakage_auditor）
        adapter_id: 承担该角色的 adapter 标识（devin / codex / ...）
        model_uid: 模型 UID
        carrier_id: 载体 ID
        carrier_profile_hash: 载体 profile 哈希
        view_kind: 盲化 view 种类（AU_VIEW_KINDS）
        independence_kind: 独立性种类（DIFFERENT_SESSION / DIFFERENT_MODEL / ...）
        session_id: 独立 session ID
        disagreement_rule_ref: 分歧处理规则引用（预注册；空表示无预注册规则）
    """

    role_type_id: str
    adapter_id: str
    model_uid: str
    carrier_id: str
    carrier_profile_hash: str
    view_kind: str
    independence_kind: str = "DIFFERENT_SESSION"
    session_id: str = ""
    disagreement_rule_ref: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "role_type_id": self.role_type_id,
            "adapter_id": self.adapter_id,
            "model_uid": self.model_uid,
            "carrier_id": self.carrier_id,
            "carrier_profile_hash": self.carrier_profile_hash,
            "view_kind": self.view_kind,
            "independence_kind": self.independence_kind,
            "session_id": self.session_id,
            "disagreement_rule_ref": dict(self.disagreement_rule_ref),
        }


@dataclass(frozen=True)
class AuditPlan:
    """冻结 P6 审计计划——不可变，冻结后修改必须创建新 plan。

    字段：
        plan_id: 唯一标识
        state: 计划状态（DRAFT / FROZEN / STARTED / COMPLETED / SUPERSEDED）
        run_refs: 要审计的 P5 RunArtifactBundle 引用列表
            [{bundle_id, arm_id, content_hash}]
        role_bindings: 三个审计角色的绑定规格
        blinding_spec: 盲化规格（redaction 规则 per view_kind）
        independence_requirements: 独立性要求
        leakage_budget: 预注册 leakage budget
        required_lanes: 必需的 lane（默认三审全部）
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    plan_id: str
    state: str = "DRAFT"
    run_refs: tuple[dict[str, str], ...] = ()
    role_bindings: tuple[AuditRoleBinding, ...] = ()
    blinding_spec: dict[str, Any] = field(default_factory=dict)
    independence_requirements: dict[str, Any] = field(default_factory=dict)
    leakage_budget: dict[str, Any] = field(default_factory=dict)
    required_lanes: tuple[str, ...] = (
        "process_auditor", "proof_judge", "leakage_auditor",
    )
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "plan_id": self.plan_id,
            "state": self.state,
            "run_refs": [dict(r) for r in self.run_refs],
            "role_bindings": [rb.to_dict() for rb in self.role_bindings],
            "blinding_spec": dict(self.blinding_spec),
            "independence_requirements": dict(self.independence_requirements),
            "leakage_budget": dict(self.leakage_budget),
            "required_lanes": list(self.required_lanes),
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
    def role_type_ids(self) -> set[str]:
        return {rb.role_type_id for rb in self.role_bindings}


def make_audit_plan(
    *,
    plan_id: str,
    run_refs: list[dict[str, str]] | tuple[dict[str, str], ...] = (),
    role_bindings: list[AuditRoleBinding] | tuple[AuditRoleBinding, ...] = (),
    blinding_spec: dict[str, Any] | None = None,
    independence_requirements: dict[str, Any] | None = None,
    leakage_budget: dict[str, Any] | None = None,
    required_lanes: tuple[str, ...] = (
        "process_auditor", "proof_judge", "leakage_auditor",
    ),
    frozen_at: str = "2026-08-14T12:00:00Z",
) -> AuditPlan:
    plan = AuditPlan(
        plan_id=plan_id,
        state="FROZEN",
        run_refs=tuple(run_refs),
        role_bindings=tuple(role_bindings),
        blinding_spec=blinding_spec or {},
        independence_requirements=independence_requirements or {},
        leakage_budget=leakage_budget or {},
        required_lanes=required_lanes,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(plan, content_hash=plan.compute_content_hash())


@dataclass(frozen=True)
class AuditPlanVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    plan_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_audit_plan(plan: AuditPlan) -> AuditPlanVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = plan.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    # state must be FROZEN or beyond
    if plan.state == "DRAFT":
        errors.append(EC.AU_AUDIT_PLAN_NOT_FROZEN)
        details.append("plan state is DRAFT — must be FROZEN before audit")

    # run_refs required
    if not plan.run_refs:
        errors.append(EC.AU_BUNDLE_REF_MISSING)
        details.append("run_refs must not be empty — at least one P5 bundle required")
    else:
        for r in plan.run_refs:
            if not r.get("bundle_id"):
                errors.append(EC.AU_BUNDLE_REF_MISSING)
                details.append("run_refs entry missing bundle_id")
            if not r.get("content_hash"):
                errors.append(EC.AU_BUNDLE_REF_MISSING)
                details.append(f"run_refs entry {r.get('bundle_id', '?')} missing content_hash")

    # role_bindings must cover all three audit roles
    if not plan.role_bindings:
        errors.append(EC.AU_AUDIT_ROLE_UNKNOWN)
        details.append("role_bindings must not be empty")
    else:
        role_ids = plan.role_type_ids
        if role_ids != AU_AUDIT_ROLES:
            errors.append(EC.AU_AUDIT_ROLE_UNKNOWN)
            details.append(
                f"role_bindings must exactly cover AU_AUDIT_ROLES, "
                f"got {sorted(role_ids)}, expected {sorted(AU_AUDIT_ROLES)}"
            )
        for rb in plan.role_bindings:
            if rb.role_type_id not in AU_AUDIT_ROLES:
                errors.append(EC.AU_AUDIT_ROLE_UNKNOWN)
                details.append(f"role {rb.role_type_id} not in AU_AUDIT_ROLES")
            if rb.view_kind not in AU_VIEW_KINDS:
                errors.append(EC.AU_BLINDING_INVALID)
                details.append(
                    f"role {rb.role_type_id} view_kind {rb.view_kind} not in AU_VIEW_KINDS"
                )
            if not rb.adapter_id:
                errors.append(EC.AU_AUDIT_ROLE_UNKNOWN)
                details.append(f"role {rb.role_type_id} missing adapter_id")
            if not rb.session_id:
                errors.append(EC.AU_INDEPENDENCE_VIOLATED)
                details.append(f"role {rb.role_type_id} missing session_id")

        # independence: all sessions distinct
        sessions = [rb.session_id for rb in plan.role_bindings]
        if len(set(sessions)) != len(sessions):
            errors.append(EC.AU_INDEPENDENCE_VIOLATED)
            details.append("role_bindings sessions must all be distinct")

        # independence: all view_kinds distinct
        view_kinds = [rb.view_kind for rb in plan.role_bindings]
        if len(set(view_kinds)) != len(view_kinds):
            errors.append(EC.AU_BLINDING_INVALID)
            details.append("role_bindings view_kinds must all be distinct")

    # required_lanes must be subset of AU_AUDIT_ROLES
    for lane in plan.required_lanes:
        if lane not in AU_AUDIT_ROLES:
            errors.append(EC.AU_AUDIT_ROLE_UNKNOWN)
            details.append(f"required_lanes entry {lane} not in AU_AUDIT_ROLES")

    # content_hash
    if not plan.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif plan.content_hash != plan.compute_content_hash():
        errors.append(EC.AU_AUDIT_PLAN_MODIFIED)
        details.append(
            f"content_hash mismatch: claims {plan.content_hash}, "
            f"computed {plan.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return AuditPlanVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        plan_id=plan.plan_id,
    )


def check_audit_plan_modified_after_start(
    plan: AuditPlan,
    original_hash: str,
) -> bool:
    """检查 plan 是否在启动后被修改。返回 True 表示被修改（blocker）。"""
    if plan.is_started:
        return plan.content_hash != original_hash
    return False
