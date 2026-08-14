"""ApplicabilityBoundary / TellHintRelation / HintRenderer / HintInstance /
SelectorDecision / InjectionPolicy / Progress/Termination/Critic/CompositionContract.

WP-TX1 的适用性边界、Tell↔Hint M:N 关系、渲染器、选择器、注入策略和执行合同。

关键约束（blocker）：
- TellHintRelation 必须是 M:N（一个 Tell → 多个 Hint，一个 Hint ← 多个 Tell）
- ApplicabilityBoundary negative guard 不可被违反
- SelectorDecision abstain 时不得同时 select
- InjectionPolicy 版本不可漂移
- Contract kind 必须在 TX_CONTRACT_KINDS 中

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    TX_BOUNDARY_GUARD_KINDS,
    TX_HINT_RELATION_KINDS,
    TX_SELECTOR_DECISION_KINDS,
    TX_INJECTION_POSITIONS,
    TX_CONTRACT_KINDS,
    VerificationErrorCode as EC,
)


_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"

_BOUNDARY_SCHEMA_ID = "seven/applicability-boundary"
_BOUNDARY_SCHEMA_VERSION = 1

_HINT_RELATION_SCHEMA_ID = "seven/tell-hint-relation"
_HINT_RELATION_SCHEMA_VERSION = 1

_RENDERER_SCHEMA_ID = "seven/hint-renderer"
_RENDERER_SCHEMA_VERSION = 1

_HINT_INSTANCE_SCHEMA_ID = "seven/hint-instance"
_HINT_INSTANCE_SCHEMA_VERSION = 1

_SELECTOR_SCHEMA_ID = "seven/selector-decision"
_SELECTOR_SCHEMA_VERSION = 1

_INJECTION_SCHEMA_ID = "seven/injection-policy"
_INJECTION_SCHEMA_VERSION = 1

_CONTRACT_SCHEMA_ID = "seven/tell-contract"
_CONTRACT_SCHEMA_VERSION = 1


# ─── ApplicabilityBoundary ───────────────────────────────────────────


@dataclass(frozen=True)
class BoundaryGuard:
    """单个 guard——trigger 或 negative guard。"""

    guard_id: str
    kind: str  # TX_BOUNDARY_GUARD_KINDS
    condition: str = ""
    binding_roles: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "guard_id": self.guard_id,
            "kind": self.kind,
            "condition": self.condition,
            "binding_roles": list(self.binding_roles),
        }


@dataclass(frozen=True)
class ApplicabilityBoundary:
    """Tell 的适用性边界。

    字段：
        boundary_id: 唯一标识
        core_id: 关联的 TellCore ID
        trigger: 触发条件
        negative_guards: 否定 guard 列表（不可被违反）
        binding_roles: 绑定角色列表
        applicable_transformations: 适用变换列表
        content_hash: 内容哈希
    """

    boundary_id: str
    core_id: str
    trigger: str = ""
    negative_guards: tuple[BoundaryGuard, ...] = ()
    binding_roles: tuple[str, ...] = ()
    applicable_transformations: tuple[str, ...] = ()
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _BOUNDARY_SCHEMA_ID,
            "schema_version": _BOUNDARY_SCHEMA_VERSION,
            "boundary_id": self.boundary_id,
            "core_id": self.core_id,
            "trigger": self.trigger,
            "negative_guards": [g.to_dict() for g in self.negative_guards],
            "binding_roles": list(self.binding_roles),
            "applicable_transformations": list(self.applicable_transformations),
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


def make_applicability_boundary(
    *,
    boundary_id: str,
    core_id: str,
    trigger: str = "",
    negative_guards: tuple[BoundaryGuard, ...] = (),
    binding_roles: tuple[str, ...] = (),
    applicable_transformations: tuple[str, ...] = (),
    frozen_at: str = "",
) -> ApplicabilityBoundary:
    b = ApplicabilityBoundary(
        boundary_id=boundary_id,
        core_id=core_id,
        trigger=trigger,
        negative_guards=negative_guards,
        binding_roles=binding_roles,
        applicable_transformations=applicable_transformations,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(b, content_hash=b.compute_content_hash())


@dataclass(frozen=True)
class ApplicabilityBoundaryVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    boundary_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_applicability_boundary(
    boundary: ApplicabilityBoundary,
    *,
    violated_guard_ids: set[str] | None = None,
) -> ApplicabilityBoundaryVerificationResult:
    """验证 ApplicabilityBoundary。

    参数：
        violated_guard_ids: 被违反的 negative guard ID 集合（用于 blocker 测试）
    """
    errors: list[EC] = []
    details: list[str] = []

    d = boundary.to_dict()
    if d.get("schema_id") != _BOUNDARY_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_BOUNDARY_SCHEMA_ID}")

    # trigger required
    if not boundary.trigger:
        errors.append(EC.TX_BOUNDARY_TRIGGER_MISSING)
        details.append("trigger is empty — boundary must have a trigger")

    # binding_roles required
    if not boundary.binding_roles:
        errors.append(EC.TX_BOUNDARY_BINDING_ROLE_INVALID)
        details.append("binding_roles is empty — must have at least one role")

    # negative guards kind valid
    for g in boundary.negative_guards:
        if g.kind not in TX_BOUNDARY_GUARD_KINDS:
            errors.append(EC.TX_BOUNDARY_GUARD_KIND_INVALID)
            details.append(
                f"guard {g.guard_id} kind '{g.kind}' not in "
                f"{sorted(TX_BOUNDARY_GUARD_KINDS)}"
            )

    # blocker: negative guard violated
    if violated_guard_ids:
        for g in boundary.negative_guards:
            if g.guard_id in violated_guard_ids:
                errors.append(EC.TX_BOUNDARY_NEGATIVE_GUARD_VIOLATED)
                details.append(
                    f"negative guard {g.guard_id} was violated — "
                    f"applicability boundary breached"
                )

    if not boundary.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif boundary.content_hash != boundary.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {boundary.content_hash}, "
            f"computed {boundary.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return ApplicabilityBoundaryVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        boundary_id=boundary.boundary_id,
    )


# ─── TellHintRelation (M:N) ──────────────────────────────────────────


@dataclass(frozen=True)
class TellHintRelation:
    """Tell ↔ Hint 的显式 M:N 边。

    字段：
        relation_id: 唯一标识
        tell_core_id: 关联的 TellCore ID
        hint_renderer_id: 关联的 HintRenderer ID
        kind: 关系 kind（TX_HINT_RELATION_KINDS）
        applicability_condition: 适用条件
        content_hash: 内容哈希
    """

    relation_id: str
    tell_core_id: str
    hint_renderer_id: str
    kind: str
    applicability_condition: str = ""
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _HINT_RELATION_SCHEMA_ID,
            "schema_version": _HINT_RELATION_SCHEMA_VERSION,
            "relation_id": self.relation_id,
            "tell_core_id": self.tell_core_id,
            "hint_renderer_id": self.hint_renderer_id,
            "kind": self.kind,
            "applicability_condition": self.applicability_condition,
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


def make_tell_hint_relation(
    *,
    relation_id: str,
    tell_core_id: str,
    hint_renderer_id: str,
    kind: str,
    applicability_condition: str = "",
    frozen_at: str = "",
) -> TellHintRelation:
    rel = TellHintRelation(
        relation_id=relation_id,
        tell_core_id=tell_core_id,
        hint_renderer_id=hint_renderer_id,
        kind=kind,
        applicability_condition=applicability_condition,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(rel, content_hash=rel.compute_content_hash())


@dataclass(frozen=True)
class TellHintRelationVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    relation_id: str = ""
    is_mn: bool = False

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_tell_hint_relation(
    relation: TellHintRelation,
    *,
    all_relations: tuple[TellHintRelation, ...] = (),
) -> TellHintRelationVerificationResult:
    """验证单个 TellHintRelation，并检查 M:N 性质。

    M:N 检查：在 all_relations 集合中，一个 tell_core_id 必须关联多个
    hint_renderer_id，一个 hint_renderer_id 必须被多个 tell_core_id 关联。
    至少需要 all_relations 提供足够样本来判定 M:N。
    """
    errors: list[EC] = []
    details: list[str] = []

    d = relation.to_dict()
    if d.get("schema_id") != _HINT_RELATION_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_HINT_RELATION_SCHEMA_ID}")

    if relation.kind not in TX_HINT_RELATION_KINDS:
        errors.append(EC.TX_HINT_RELATION_KIND_INVALID)
        details.append(
            f"kind '{relation.kind}' not in {sorted(TX_HINT_RELATION_KINDS)}"
        )

    if not relation.applicability_condition:
        errors.append(EC.TX_HINT_RELATION_APPLICABILITY_MISSING)
        details.append("applicability_condition is empty — M:N edge must have condition")

    # M:N check
    is_mn = False
    if all_relations:
        tell_to_hints: dict[str, set[str]] = {}
        hint_to_tells: dict[str, set[str]] = {}
        for r in all_relations:
            tell_to_hints.setdefault(r.tell_core_id, set()).add(r.hint_renderer_id)
            hint_to_tells.setdefault(r.hint_renderer_id, set()).add(r.tell_core_id)
        # one tell -> many hints
        tell_many = any(len(hs) > 1 for hs in tell_to_hints.values())
        # one hint <- many tells
        hint_many = any(len(ts) > 1 for ts in hint_to_tells.values())
        is_mn = tell_many and hint_many
        if not is_mn:
            errors.append(EC.TX_HINT_RELATION_NOT_MN)
            details.append(
                f"relation set is not M:N: tell_many={tell_many}, "
                f"hint_many={hint_many} — one Tell must map to many Hints "
                f"AND one Hint must be mapped by many Tells"
            )

    if not relation.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif relation.content_hash != relation.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {relation.content_hash}, "
            f"computed {relation.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return TellHintRelationVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        relation_id=relation.relation_id,
        is_mn=is_mn,
    )


# ─── HintRenderer / HintInstance ─────────────────────────────────────


@dataclass(frozen=True)
class HintRenderer:
    """Model-facing 表达策略。

    字段：
        renderer_id: 唯一标识
        version: 版本号（冻结）
        expression_strategy: 表达策略描述
        leakage_budget: 泄漏预算
        specificity_level: 具体度级别
        supersedes_ref: 前一个版本引用
        frozen_at: 冻结时间
        content_hash: 内容哈希
    """

    renderer_id: str
    version: str
    expression_strategy: str = ""
    leakage_budget: str = ""
    specificity_level: str = ""
    supersedes_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _RENDERER_SCHEMA_ID,
            "schema_version": _RENDERER_SCHEMA_VERSION,
            "renderer_id": self.renderer_id,
            "version": self.version,
            "expression_strategy": self.expression_strategy,
            "leakage_budget": self.leakage_budget,
            "specificity_level": self.specificity_level,
            "supersedes_ref": dict(self.supersedes_ref),
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
        return bool(self.version) and bool(self.content_hash)


def make_hint_renderer(
    *,
    renderer_id: str,
    version: str,
    expression_strategy: str = "",
    leakage_budget: str = "",
    specificity_level: str = "",
    supersedes_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> HintRenderer:
    r = HintRenderer(
        renderer_id=renderer_id,
        version=version,
        expression_strategy=expression_strategy,
        leakage_budget=leakage_budget,
        specificity_level=specificity_level,
        supersedes_ref=supersedes_ref or {},
        frozen_at=frozen_at,
    )
    return dataclasses.replace(r, content_hash=r.compute_content_hash())


@dataclass(frozen=True)
class HintInstance:
    """绑定的 payload 实例——renderer 的具体执行 payload。

    字段：
        instance_id: 唯一标识
        renderer_ref: 关联的 HintRenderer 引用（{renderer_id, version, content_hash}）
        payload: 绑定的 payload 内容
        payload_hash: payload 内容哈希
        bound_at: 绑定时间
        content_hash: 完整内容哈希
    """

    instance_id: str
    renderer_ref: dict[str, str] = field(default_factory=dict)
    payload: dict[str, Any] = field(default_factory=dict)
    payload_hash: str = ""
    bound_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _HINT_INSTANCE_SCHEMA_ID,
            "schema_version": _HINT_INSTANCE_SCHEMA_VERSION,
            "instance_id": self.instance_id,
            "renderer_ref": dict(self.renderer_ref),
            "payload": dict(self.payload),
            "payload_hash": self.payload_hash,
            "bound_at": self.bound_at,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def compute_payload_hash(self) -> str:
        return hashlib.sha256(canonical_json_bytes(self.payload)).hexdigest()

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()

    @property
    def is_payload_hash_valid(self) -> bool:
        return self.payload_hash == self.compute_payload_hash()


def make_hint_instance(
    *,
    instance_id: str,
    renderer_ref: dict[str, str] | None = None,
    payload: dict[str, Any] | None = None,
    bound_at: str = "",
) -> HintInstance:
    inst = HintInstance(
        instance_id=instance_id,
        renderer_ref=renderer_ref or {},
        payload=payload or {},
        bound_at=bound_at,
    )
    ph = inst.compute_payload_hash()
    inst = dataclasses.replace(inst, payload_hash=ph)
    return dataclasses.replace(inst, content_hash=inst.compute_content_hash())


@dataclass(frozen=True)
class HintInstanceVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    instance_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_hint_instance(instance: HintInstance) -> HintInstanceVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = instance.to_dict()
    if d.get("schema_id") != _HINT_INSTANCE_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_HINT_INSTANCE_SCHEMA_ID}")

    # renderer_ref required
    if not instance.renderer_ref.get("renderer_id"):
        errors.append(EC.TX_HINT_INSTANCE_RENDERER_REF_MISSING)
        details.append("renderer_ref must contain renderer_id")

    # payload_hash
    if not instance.payload_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("payload_hash is empty")
    elif instance.payload_hash != instance.compute_payload_hash():
        errors.append(EC.TX_HINT_INSTANCE_PAYLOAD_HASH_MISMATCH)
        details.append(
            f"payload_hash mismatch: claims {instance.payload_hash}, "
            f"computed {instance.compute_payload_hash()}"
        )

    if not instance.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif instance.content_hash != instance.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {instance.content_hash}, "
            f"computed {instance.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return HintInstanceVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        instance_id=instance.instance_id,
    )


# ─── SelectorDecision ────────────────────────────────────────────────


@dataclass(frozen=True)
class SelectorDecision:
    """检索/排序/弃权决定。

    字段：
        decision_id: 唯一标识
        kind: 决定 kind（TX_SELECTOR_DECISION_KINDS）
        selected_core_ids: 选中的 TellCore ID 列表
        ranking: 排序列表（core_id 顺序）
        abstain_reason: 弃权原因（kind=ABSTAIN 时非空）
        fallback_core_id: 回退 Core ID
        content_hash: 内容哈希
    """

    decision_id: str
    kind: str
    selected_core_ids: tuple[str, ...] = ()
    ranking: tuple[str, ...] = ()
    abstain_reason: str = ""
    fallback_core_id: str = ""
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SELECTOR_SCHEMA_ID,
            "schema_version": _SELECTOR_SCHEMA_VERSION,
            "decision_id": self.decision_id,
            "kind": self.kind,
            "selected_core_ids": list(self.selected_core_ids),
            "ranking": list(self.ranking),
            "abstain_reason": self.abstain_reason,
            "fallback_core_id": self.fallback_core_id,
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


def make_selector_decision(
    *,
    decision_id: str,
    kind: str,
    selected_core_ids: tuple[str, ...] = (),
    ranking: tuple[str, ...] = (),
    abstain_reason: str = "",
    fallback_core_id: str = "",
    frozen_at: str = "",
) -> SelectorDecision:
    sd = SelectorDecision(
        decision_id=decision_id,
        kind=kind,
        selected_core_ids=selected_core_ids,
        ranking=ranking,
        abstain_reason=abstain_reason,
        fallback_core_id=fallback_core_id,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(sd, content_hash=sd.compute_content_hash())


@dataclass(frozen=True)
class SelectorDecisionVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    decision_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_selector_decision(
    decision: SelectorDecision,
) -> SelectorDecisionVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = decision.to_dict()
    if d.get("schema_id") != _SELECTOR_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SELECTOR_SCHEMA_ID}")

    if decision.kind not in TX_SELECTOR_DECISION_KINDS:
        errors.append(EC.TX_SELECTOR_DECISION_KIND_INVALID)
        details.append(
            f"kind '{decision.kind}' not in {sorted(TX_SELECTOR_DECISION_KINDS)}"
        )

    # blocker: abstain violation — abstain but also selecting
    if decision.kind == "ABSTAIN":
        if decision.selected_core_ids:
            errors.append(EC.TX_SELECTOR_ABSTAIN_VIOLATED)
            details.append(
                "kind=ABSTAIN but selected_core_ids is non-empty — "
                "abstain must not select any core"
            )
        if not decision.abstain_reason:
            errors.append(EC.TX_SELECTOR_ABSTAIN_VIOLATED)
            details.append("kind=ABSTAIN but abstain_reason is empty")
    else:
        if decision.kind == "SELECT" and not decision.selected_core_ids:
            errors.append(EC.TX_SELECTOR_RANKING_EMPTY)
            details.append("kind=SELECT but selected_core_ids is empty")
        if decision.kind == "RANK" and not decision.ranking:
            errors.append(EC.TX_SELECTOR_RANKING_EMPTY)
            details.append("kind=RANK but ranking is empty")

    if not decision.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif decision.content_hash != decision.compute_content_hash():
        errors.append(EC.TX_TAXONOMY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {decision.content_hash}, "
            f"computed {decision.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return SelectorDecisionVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        decision_id=decision.decision_id,
    )


# ─── InjectionPolicy ─────────────────────────────────────────────────


@dataclass(frozen=True)
class InjectionPolicy:
    """注入策略——注入位置、策略版本。

    字段：
        policy_id: 唯一标识
        version: 策略版本
        injection_position: 注入位置（TX_INJECTION_POSITIONS）
        content_hash: 内容哈希
    """

    policy_id: str
    version: str
    injection_position: str = ""
    supersedes_ref: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _INJECTION_SCHEMA_ID,
            "schema_version": _INJECTION_SCHEMA_VERSION,
            "policy_id": self.policy_id,
            "version": self.version,
            "injection_position": self.injection_position,
            "supersedes_ref": dict(self.supersedes_ref),
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


def make_injection_policy(
    *,
    policy_id: str,
    version: str,
    injection_position: str = "",
    supersedes_ref: dict[str, str] | None = None,
    frozen_at: str = "",
) -> InjectionPolicy:
    p = InjectionPolicy(
        policy_id=policy_id,
        version=version,
        injection_position=injection_position,
        supersedes_ref=supersedes_ref or {},
        frozen_at=frozen_at,
    )
    return dataclasses.replace(p, content_hash=p.compute_content_hash())


@dataclass(frozen=True)
class InjectionPolicyVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    policy_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_injection_policy(
    policy: InjectionPolicy,
    *,
    expected_version: str | None = None,
) -> InjectionPolicyVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = policy.to_dict()
    if d.get("schema_id") != _INJECTION_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_INJECTION_SCHEMA_ID}")

    if policy.injection_position not in TX_INJECTION_POSITIONS:
        if policy.injection_position:
            errors.append(EC.TX_INJECTION_POSITION_INVALID)
            details.append(
                f"injection_position '{policy.injection_position}' not in "
                f"{sorted(TX_INJECTION_POSITIONS)}"
            )

    # blocker: version drift
    if expected_version is not None and policy.version != expected_version:
        errors.append(EC.TX_INJECTION_POLICY_VERSION_DRIFT)
        details.append(
            f"version drift: policy version '{policy.version}' != "
            f"expected '{expected_version}'"
        )

    if not policy.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif policy.content_hash != policy.compute_content_hash():
        errors.append(EC.TX_INJECTION_POLICY_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {policy.content_hash}, "
            f"computed {policy.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return InjectionPolicyVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        policy_id=policy.policy_id,
    )


# ─── Progress / Termination / Critic / CompositionContract ──────────


@dataclass(frozen=True)
class TellContract:
    """执行/退出/纠正/多Tell关系合同。

    字段：
        contract_id: 唯一标识
        kind: 合同 kind（TX_CONTRACT_KINDS）
        core_id: 关联的 TellCore ID
        specification: 合同规格
        content_hash: 内容哈希
    """

    contract_id: str
    kind: str
    core_id: str = ""
    specification: str = ""
    related_core_ids: tuple[str, ...] = ()
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _CONTRACT_SCHEMA_ID,
            "schema_version": _CONTRACT_SCHEMA_VERSION,
            "contract_id": self.contract_id,
            "kind": self.kind,
            "core_id": self.core_id,
            "specification": self.specification,
            "related_core_ids": list(self.related_core_ids),
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


def make_tell_contract(
    *,
    contract_id: str,
    kind: str,
    core_id: str = "",
    specification: str = "",
    related_core_ids: tuple[str, ...] = (),
    frozen_at: str = "",
) -> TellContract:
    c = TellContract(
        contract_id=contract_id,
        kind=kind,
        core_id=core_id,
        specification=specification,
        related_core_ids=related_core_ids,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(c, content_hash=c.compute_content_hash())


@dataclass(frozen=True)
class TellContractVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    contract_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_tell_contract(
    contract: TellContract,
    *,
    known_contracts: dict[str, TellContract] | None = None,
) -> TellContractVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = contract.to_dict()
    if d.get("schema_id") != _CONTRACT_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_CONTRACT_SCHEMA_ID}")

    if contract.kind not in TX_CONTRACT_KINDS:
        errors.append(EC.TX_CONTRACT_KIND_INVALID)
        details.append(
            f"kind '{contract.kind}' not in {sorted(TX_CONTRACT_KINDS)}"
        )

    # composition contract cycle check (self-reference)
    if contract.kind == "COMPOSITION_CONTRACT":
        if contract.core_id and contract.core_id in contract.related_core_ids:
            errors.append(EC.TX_COMPOSITION_CONTRACT_CYCLE)
            details.append(
                f"composition contract references itself: core_id "
                f"{contract.core_id} in related_core_ids"
            )

    if not contract.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif contract.content_hash != contract.compute_content_hash():
        errors.append(EC.TX_CONTRACT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {contract.content_hash}, "
            f"computed {contract.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return TellContractVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        contract_id=contract.contract_id,
    )
