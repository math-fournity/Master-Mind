"""P7 冻结注册表——AnalysisMethodRegistry / MultiplicityRuleRegistry /
StoppingRuleRegistry / EvidenceStatusRegistry。

来自 docs/implementation/14-evidence-analysis-and-multi-epoch.md：

- AnalysisMethodRegistry v1：估计器在 P4 冻结，禁止运行后挑有利估计器。
  每个 method entry 冻结 method_id/version、endpoint、cluster/block key、
  missingness policy、contrast 方向、精确算术/舍入、CI/p-value 算法、
  随机源、seed 派生、迭代/枚举上限、tie rule、输出 Schema、golden test vectors。
- MultiplicityRuleRegistry v1：primary/hierarchical/Holm/exploratory 精确算法。
  HOLM_V1 按 (raw_p, contrast_id) 排序；探索性永不进入 confirmatory family。
- StoppingRuleRegistry v1：maximum_clusters、资源上限、安全 tripwire、序贯边界。
  禁止 "run until significant"。
- EvidenceStatusRegistry v1：SUPPORTS/CONTRADICTS/DOES_NOT_SUPPORT/
  INCONCLUSIVE_DUE_TO_PROTOCOL/NOT_TESTED。机器条件机械派生，不接受自由文本。

关键约束（blocker）：
- 估计器不在 registry → BLOCK（EV_ESTIMATOR_NOT_IN_REGISTRY）
- 估计器运行后换 → BLOCK（EV_ESTIMATOR_SWAPPED）
- 多重性规则不在 registry → BLOCK（EV_MULTIPLICITY_RULE_NOT_IN_REGISTRY）
- 停止规则不在 registry → BLOCK（EV_STOPPING_RULE_NOT_IN_REGISTRY）
- run until significant → BLOCK（EV_STOPPING_RUN_UNTIL_SIGNIFICANT）
- Evidence status 不在 registry → BLOCK（EV_EVIDENCE_STATUS_INVALID）
- registry 未冻结 → BLOCK（EV_REGISTRY_NOT_FROZEN）
- registry hash 漂移 → BLOCK（EV_REGISTRY_HASH_MISMATCH）

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
    EV_ESTIMATOR_KINDS,
    EV_MULTIPLICITY_KINDS,
    EV_STOPPING_KINDS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


# ─── AnalysisMethodRegistry ─────────────────────────────────────────────


@dataclass(frozen=True)
class AnalysisMethodEntry:
    """单个估计器 entry——冻结参数、输入形状、伪随机算法/seed、tie rule、golden vectors。

    字段：
        method_id: 估计器 ID（EV_ESTIMATOR_KINDS）
        version: 版本
        endpoint_kind: endpoint 类型
        cluster_key: cluster/block key
        missingness_policy: 缺失策略
        contrast_direction: contrast 方向
        arithmetic_rounding: 精确算术/舍入规则
        ci_pvalue_algorithm: CI 或 p-value 算法
        random_source: 随机源（HMAC-SHA256(seed, method_id || contrast_id || counter)）
        seed_derivation: seed 派生规则
        iteration_limit: 迭代/枚举上限
        tie_rule: tie 规则
        output_schema: 输出 Schema
        golden_vectors: golden test vectors
        parameters: 其他冻结参数
    """

    method_id: str
    version: str = "v1"
    endpoint_kind: str = "binary_success"
    cluster_key: str = "problem_source_cluster"
    missingness_policy: str = "invalid_not_filled_zero"
    contrast_direction: str = "two_sided"
    arithmetic_rounding: str = "decimal_rational"
    ci_pvalue_algorithm: str = "none"
    random_source: str = "HMAC-SHA256"
    seed_derivation: str = "seed||method_id||contrast_id||counter"
    iteration_limit: int = 10000
    tie_rule: str = "canonical_contrast_id"
    output_schema: dict[str, Any] = field(default_factory=dict)
    golden_vectors: list[dict[str, Any]] = field(default_factory=list)
    parameters: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "method_id": self.method_id,
            "version": self.version,
            "endpoint_kind": self.endpoint_kind,
            "cluster_key": self.cluster_key,
            "missingness_policy": self.missingness_policy,
            "contrast_direction": self.contrast_direction,
            "arithmetic_rounding": self.arithmetic_rounding,
            "ci_pvalue_algorithm": self.ci_pvalue_algorithm,
            "random_source": self.random_source,
            "seed_derivation": self.seed_derivation,
            "iteration_limit": self.iteration_limit,
            "tie_rule": self.tie_rule,
            "output_schema": dict(self.output_schema),
            "golden_vectors": [dict(v) for v in self.golden_vectors],
            "parameters": dict(self.parameters),
        }


@dataclass(frozen=True)
class AnalysisMethodRegistry:
    """冻结的 P7 估计器注册表。版本化，带 content_hash。

    P4 冻结后不可变；运行后换估计器 → EV_ESTIMATOR_SWAPPED。
    """

    registry_id: str = "analysis-method-registry"
    version: str = "v1"
    entries: tuple[AnalysisMethodEntry, ...] = ()
    frozen: bool = False
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "registry_id": self.registry_id,
            "version": self.version,
            "entries": [e.to_dict() for e in self.entries],
            "frozen": self.frozen,
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

    def method_ids(self) -> frozenset[str]:
        return frozenset(e.method_id for e in self.entries)

    def get(self, method_id: str) -> AnalysisMethodEntry | None:
        for e in self.entries:
            if e.method_id == method_id:
                return e
        return None


def build_default_analysis_method_registry() -> AnalysisMethodRegistry:
    """构建默认 AnalysisMethodRegistry——包含 4 个 P7 估计器。"""
    entries = (
        AnalysisMethodEntry(
            method_id="PAIRED_CLUSTER_DIFFERENCE_V1",
            endpoint_kind="binary_success",
            ci_pvalue_algorithm="paired_normal_approx",
            golden_vectors=[
                {
                    "name": "two_cluster_paired_mean",
                    "clusters": 2,
                    "expected_effect": 0.5,
                },
            ],
        ),
        AnalysisMethodEntry(
            method_id="STRATIFIED_CLUSTER_BOOTSTRAP_V1",
            endpoint_kind="binary_success",
            ci_pvalue_algorithm="bootstrap_percentile",
            iteration_limit=10000,
            golden_vectors=[
                {
                    "name": "first_bootstrap_indices",
                    "seed": "seed-001",
                    "expected_first_index": 0,
                },
            ],
        ),
        AnalysisMethodEntry(
            method_id="RANDOMIZATION_INFERENCE_V1",
            endpoint_kind="binary_success",
            ci_pvalue_algorithm="randomization_distribution",
            iteration_limit=10000,
            golden_vectors=[
                {
                    "name": "exhaustive_assignment_hash",
                    "expected_assignments": 8,
                },
            ],
        ),
        AnalysisMethodEntry(
            method_id="DESCRIPTIVE_SMALL_N_V1",
            endpoint_kind="binary_success",
            ci_pvalue_algorithm="none",
            golden_vectors=[
                {
                    "name": "small_n_effect_direction",
                    "expected_direction": "no_significance_claim",
                },
            ],
        ),
    )
    reg = AnalysisMethodRegistry(
        registry_id="analysis-method-registry",
        version="v1",
        entries=entries,
        frozen=True,
    )
    return dataclasses.replace(reg, content_hash=reg.compute_content_hash())


def verify_analysis_method_registry(
    registry: AnalysisMethodRegistry,
) -> VerificationResult:
    """验证 AnalysisMethodRegistry。"""
    errors: list[EC] = []
    details: list[str] = []

    if not registry.frozen:
        errors.append(EC.EV_REGISTRY_NOT_FROZEN)
        details.append("AnalysisMethodRegistry must be frozen in P4")

    if not registry.entries:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("AnalysisMethodRegistry must have at least one entry")

    seen: set[str] = set()
    for e in registry.entries:
        if e.method_id in seen:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"duplicate method_id {e.method_id}")
        seen.add(e.method_id)
        if e.method_id not in EV_ESTIMATOR_KINDS:
            errors.append(EC.EV_ESTIMATOR_NOT_IN_REGISTRY)
            details.append(
                f"method_id {e.method_id} not in EV_ESTIMATOR_KINDS"
            )
        if not e.golden_vectors:
            errors.append(EC.EV_GOLDEN_VECTOR_MISMATCH)
            details.append(f"method {e.method_id} missing golden vectors")

    if not registry.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif registry.content_hash != registry.compute_content_hash():
        errors.append(EC.EV_REGISTRY_HASH_MISMATCH)
        details.append("AnalysisMethodRegistry content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_estimator_in_registry(
    registry: AnalysisMethodRegistry,
    method_id: str,
) -> VerificationResult:
    """检查估计器是否在冻结 registry 中（不在 → EV_ESTIMATOR_NOT_IN_REGISTRY）。"""
    errors: list[EC] = []
    details: list[str] = []

    if not registry.frozen:
        errors.append(EC.EV_REGISTRY_NOT_FROZEN)
        details.append("registry not frozen")

    if method_id not in EV_ESTIMATOR_KINDS:
        errors.append(EC.EV_ESTIMATOR_NOT_IN_REGISTRY)
        details.append(f"method_id {method_id} not a known estimator kind")

    if registry.get(method_id) is None:
        errors.append(EC.EV_ESTIMATOR_NOT_IN_REGISTRY)
        details.append(f"method_id {method_id} not in frozen registry")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_estimator_not_swapped(
    registry: AnalysisMethodRegistry,
    p4_method_id: str,
    actual_method_id: str,
) -> VerificationResult:
    """检查运行时估计器与 P4 冻结估计器一致（不一致 → EV_ESTIMATOR_SWAPPED）。"""
    errors: list[EC] = []
    details: list[str] = []

    if p4_method_id != actual_method_id:
        errors.append(EC.EV_ESTIMATOR_SWAPPED)
        details.append(
            f"estimator swapped: P4 frozen {p4_method_id}, actual {actual_method_id}"
        )

    if actual_method_id not in EV_ESTIMATOR_KINDS:
        errors.append(EC.EV_ESTIMATOR_NOT_IN_REGISTRY)
        details.append(f"actual method_id {actual_method_id} not a known estimator kind")

    if registry.get(actual_method_id) is None:
        errors.append(EC.EV_ESTIMATOR_NOT_IN_REGISTRY)
        details.append(f"actual method_id {actual_method_id} not in frozen registry")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# ─── MultiplicityRuleRegistry ───────────────────────────────────────────


@dataclass(frozen=True)
class MultiplicityRuleEntry:
    """单个多重性规则 entry。

    字段：
        rule_id: 规则 ID（EV_MULTIPLICITY_KINDS）
        version: 版本
        algorithm: 精确算法描述
        applicable_conditions: 适用条件
        is_confirmatory: 是否进入 confirmatory family
        alpha: 显著性水平
        tie_breaker: tie 打破规则
    """

    rule_id: str
    version: str = "v1"
    algorithm: str = ""
    applicable_conditions: str = ""
    is_confirmatory: bool = True
    alpha: str = "0.05"
    tie_breaker: str = "canonical_contrast_id"

    def to_dict(self) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "version": self.version,
            "algorithm": self.algorithm,
            "applicable_conditions": self.applicable_conditions,
            "is_confirmatory": self.is_confirmatory,
            "alpha": self.alpha,
            "tie_breaker": self.tie_breaker,
        }


@dataclass(frozen=True)
class MultiplicityRuleRegistry:
    """冻结的多重性规则注册表。"""

    registry_id: str = "multiplicity-rule-registry"
    version: str = "v1"
    entries: tuple[MultiplicityRuleEntry, ...] = ()
    confirmatory_family: tuple[str, ...] = ()
    frozen: bool = False
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "registry_id": self.registry_id,
            "version": self.version,
            "entries": [e.to_dict() for e in self.entries],
            "confirmatory_family": list(self.confirmatory_family),
            "frozen": self.frozen,
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

    def rule_ids(self) -> frozenset[str]:
        return frozenset(e.rule_id for e in self.entries)

    def get(self, rule_id: str) -> MultiplicityRuleEntry | None:
        for e in self.entries:
            if e.rule_id == rule_id:
                return e
        return None


def build_default_multiplicity_rule_registry() -> MultiplicityRuleRegistry:
    """构建默认 MultiplicityRuleRegistry。"""
    entries = (
        MultiplicityRuleEntry(
            rule_id="PRIMARY_V1",
            algorithm="single_primary_no_adjustment",
            is_confirmatory=True,
        ),
        MultiplicityRuleEntry(
            rule_id="HIERARCHICAL_V1",
            algorithm="ordered_hierarchical_gate",
            is_confirmatory=True,
        ),
        MultiplicityRuleEntry(
            rule_id="HOLM_V1",
            algorithm="sort_by_raw_p_then_contrast_id_compare_alpha_over_m_minus_i_plus_1",
            is_confirmatory=True,
            tie_breaker="canonical_contrast_id",
        ),
        MultiplicityRuleEntry(
            rule_id="EXPLORATORY_V1",
            algorithm="no_adjustment_exploratory_only",
            is_confirmatory=False,
        ),
    )
    reg = MultiplicityRuleRegistry(
        registry_id="multiplicity-rule-registry",
        version="v1",
        entries=entries,
        confirmatory_family=("PRIMARY_V1", "HIERARCHICAL_V1", "HOLM_V1"),
        frozen=True,
    )
    return dataclasses.replace(reg, content_hash=reg.compute_content_hash())


def verify_multiplicity_rule_registry(
    registry: MultiplicityRuleRegistry,
) -> VerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    if not registry.frozen:
        errors.append(EC.EV_REGISTRY_NOT_FROZEN)
        details.append("MultiplicityRuleRegistry must be frozen in P4")

    if not registry.entries:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("MultiplicityRuleRegistry must have at least one entry")

    seen: set[str] = set()
    for e in registry.entries:
        if e.rule_id in seen:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"duplicate rule_id {e.rule_id}")
        seen.add(e.rule_id)
        if e.rule_id not in EV_MULTIPLICITY_KINDS:
            errors.append(EC.EV_MULTIPLICITY_RULE_NOT_IN_REGISTRY)
            details.append(f"rule_id {e.rule_id} not in EV_MULTIPLICITY_KINDS")

    # exploratory 不得在 confirmatory family 中
    for cid in registry.confirmatory_family:
        entry = registry.get(cid)
        if entry is not None and not entry.is_confirmatory:
            errors.append(EC.EV_MULTIPLICITY_INCOMPLETE)
            details.append(
                f"exploratory rule {cid} must not be in confirmatory family"
            )

    if not registry.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif registry.content_hash != registry.compute_content_hash():
        errors.append(EC.EV_REGISTRY_HASH_MISMATCH)
        details.append("MultiplicityRuleRegistry content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_multiplicity_rule_in_registry(
    registry: MultiplicityRuleRegistry,
    rule_id: str,
) -> VerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    if not registry.frozen:
        errors.append(EC.EV_REGISTRY_NOT_FROZEN)
        details.append("registry not frozen")

    if rule_id not in EV_MULTIPLICITY_KINDS:
        errors.append(EC.EV_MULTIPLICITY_RULE_NOT_IN_REGISTRY)
        details.append(f"rule_id {rule_id} not a known multiplicity kind")

    if registry.get(rule_id) is None:
        errors.append(EC.EV_MULTIPLICITY_RULE_NOT_IN_REGISTRY)
        details.append(f"rule_id {rule_id} not in frozen registry")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_exploratory_not_in_family(
    registry: MultiplicityRuleRegistry,
    contrast_id: str,
    rule_id: str,
) -> VerificationResult:
    """检查探索性 contrast 不进入 confirmatory family。"""
    errors: list[EC] = []
    details: list[str] = []

    entry = registry.get(rule_id)
    if entry is not None and not entry.is_confirmatory:
        if contrast_id in registry.confirmatory_family:
            errors.append(EC.EV_MULTIPLICITY_INCOMPLETE)
            details.append(
                f"exploratory contrast {contrast_id} must not be in confirmatory family"
            )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# ─── StoppingRuleRegistry ───────────────────────────────────────────────


@dataclass(frozen=True)
class StoppingRuleEntry:
    """单个停止规则 entry。

    字段：
        rule_id: 规则 ID（EV_STOPPING_KINDS）
        version: 版本
        maximum_clusters: 最大 cluster 数
        resource_limit: 资源上限
        safety_tripwire: 安全 tripwire 描述
        sequential_boundary: 序贯边界描述
        look_schedule: 查看 schedule
        action: 动作
        allows_run_until_significant: 是否允许 run until significant（必须 False）
    """

    rule_id: str
    version: str = "v1"
    maximum_clusters: int = 0
    resource_limit: dict[str, Any] = field(default_factory=dict)
    safety_tripwire: str = ""
    sequential_boundary: str = ""
    look_schedule: str = ""
    action: str = ""
    allows_run_until_significant: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "version": self.version,
            "maximum_clusters": self.maximum_clusters,
            "resource_limit": dict(self.resource_limit),
            "safety_tripwire": self.safety_tripwire,
            "sequential_boundary": self.sequential_boundary,
            "look_schedule": self.look_schedule,
            "action": self.action,
            "allows_run_until_significant": self.allows_run_until_significant,
        }


@dataclass(frozen=True)
class StoppingRuleRegistry:
    """冻结的停止规则注册表。禁止 run until significant。"""

    registry_id: str = "stopping-rule-registry"
    version: str = "v1"
    entries: tuple[StoppingRuleEntry, ...] = ()
    frozen: bool = False
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "registry_id": self.registry_id,
            "version": self.version,
            "entries": [e.to_dict() for e in self.entries],
            "frozen": self.frozen,
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

    def rule_ids(self) -> frozenset[str]:
        return frozenset(e.rule_id for e in self.entries)

    def get(self, rule_id: str) -> StoppingRuleEntry | None:
        for e in self.entries:
            if e.rule_id == rule_id:
                return e
        return None


def build_default_stopping_rule_registry() -> StoppingRuleRegistry:
    """构建默认 StoppingRuleRegistry。"""
    entries = (
        StoppingRuleEntry(
            rule_id="MAXIMUM_CLUSTERS_V1",
            maximum_clusters=100,
            action="stop_at_maximum_clusters",
        ),
        StoppingRuleEntry(
            rule_id="RESOURCE_LIMIT_V1",
            resource_limit={"token_budget": 1000000, "wallclock_seconds": 36000},
            action="stop_at_resource_limit",
        ),
        StoppingRuleEntry(
            rule_id="SAFETY_TRIPWIRE_V1",
            safety_tripwire="contamination_rate_exceeds_threshold",
            action="stop_on_safety_tripwire",
        ),
        StoppingRuleEntry(
            rule_id="SEQUENTIAL_BOUNDARY_V1",
            sequential_boundary="pre_registered_group_sequential",
            look_schedule="pre_registered_look_schedule",
            action="stop_on_boundary_cross",
        ),
    )
    reg = StoppingRuleRegistry(
        registry_id="stopping-rule-registry",
        version="v1",
        entries=entries,
        frozen=True,
    )
    return dataclasses.replace(reg, content_hash=reg.compute_content_hash())


def verify_stopping_rule_registry(
    registry: StoppingRuleRegistry,
) -> VerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    if not registry.frozen:
        errors.append(EC.EV_REGISTRY_NOT_FROZEN)
        details.append("StoppingRuleRegistry must be frozen in P4")

    if not registry.entries:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("StoppingRuleRegistry must have at least one entry")

    seen: set[str] = set()
    for e in registry.entries:
        if e.rule_id in seen:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"duplicate rule_id {e.rule_id}")
        seen.add(e.rule_id)
        if e.rule_id not in EV_STOPPING_KINDS:
            errors.append(EC.EV_STOPPING_RULE_NOT_IN_REGISTRY)
            details.append(f"rule_id {e.rule_id} not in EV_STOPPING_KINDS")
        # run until significant 严禁
        if e.allows_run_until_significant:
            errors.append(EC.EV_STOPPING_RUN_UNTIL_SIGNIFICANT)
            details.append(
                f"rule {e.rule_id} allows run until significant — BLOCK"
            )

    if not registry.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif registry.content_hash != registry.compute_content_hash():
        errors.append(EC.EV_REGISTRY_HASH_MISMATCH)
        details.append("StoppingRuleRegistry content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_stopping_rule_in_registry(
    registry: StoppingRuleRegistry,
    rule_id: str,
) -> VerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    if not registry.frozen:
        errors.append(EC.EV_REGISTRY_NOT_FROZEN)
        details.append("registry not frozen")

    if rule_id not in EV_STOPPING_KINDS:
        errors.append(EC.EV_STOPPING_RULE_NOT_IN_REGISTRY)
        details.append(f"rule_id {rule_id} not a known stopping kind")

    if registry.get(rule_id) is None:
        errors.append(EC.EV_STOPPING_RULE_NOT_IN_REGISTRY)
        details.append(f"rule_id {rule_id} not in frozen registry")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_no_run_until_significant(
    rule: StoppingRuleEntry,
) -> VerificationResult:
    """检查停止规则不是 run until significant。"""
    errors: list[EC] = []
    details: list[str] = []

    if rule.allows_run_until_significant:
        errors.append(EC.EV_STOPPING_RUN_UNTIL_SIGNIFICANT)
        details.append(
            f"rule {rule.rule_id} allows run until significant — BLOCK"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# ─── EvidenceStatusRegistry ─────────────────────────────────────────────


@dataclass(frozen=True)
class EvidenceStatusEntry:
    """单个 Evidence status entry——机器条件。

    字段：
        status: Evidence status（EV_EVIDENCE_STATUSES）
        machine_conditions: 机器条件描述
        mapped_state: claim 级总映射状态（EV_EVIDENCE_STATES）
    """

    status: str
    machine_conditions: str = ""
    mapped_state: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "machine_conditions": self.machine_conditions,
            "mapped_state": self.mapped_state,
        }


@dataclass(frozen=True)
class EvidenceStatusRegistry:
    """冻结的 Evidence status 注册表。

    Evidence Assembler 不接受自由文本状态；从冻结 claim 规则、contrast result
    和 audit eligibility 机械派生，并保留 alternative explanations 和 scope limit。
    """

    registry_id: str = "evidence-status-registry"
    version: str = "v1"
    entries: tuple[EvidenceStatusEntry, ...] = ()
    frozen: bool = False
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "registry_id": self.registry_id,
            "version": self.version,
            "entries": [e.to_dict() for e in self.entries],
            "frozen": self.frozen,
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

    def statuses(self) -> frozenset[str]:
        return frozenset(e.status for e in self.entries)

    def get(self, status: str) -> EvidenceStatusEntry | None:
        for e in self.entries:
            if e.status == status:
                return e
        return None


def build_default_evidence_status_registry() -> EvidenceStatusRegistry:
    """构建默认 EvidenceStatusRegistry——5 个 status。"""
    entries = (
        EvidenceStatusEntry(
            status="SUPPORTS",
            machine_conditions=(
                "primary contrast, protocol usable, effect direction/threshold met, "
                "no excess leakage; scope limited to actual coverage"
            ),
            mapped_state=EV_EVIDENCE_STATES["SUPPORTS"],
        ),
        EvidenceStatusEntry(
            status="CONTRADICTS",
            machine_conditions=(
                "protocol usable and pre-registered claim direction/safety bound refuted"
            ),
            mapped_state=EV_EVIDENCE_STATES["CONTRADICTS"],
        ),
        EvidenceStatusEntry(
            status="DOES_NOT_SUPPORT",
            machine_conditions=(
                "episode success but off-mechanism, only restating terminology, "
                "or target claim has no eligible contrast"
            ),
            mapped_state=EV_EVIDENCE_STATES["DOES_NOT_SUPPORT"],
        ),
        EvidenceStatusEntry(
            status="INCONCLUSIVE_DUE_TO_PROTOCOL",
            machine_conditions=(
                "resource, blind, missing, leakage, observation or plan drift "
                "prevents interpretation"
            ),
            mapped_state=EV_EVIDENCE_STATES["INCONCLUSIVE_DUE_TO_PROTOCOL"],
        ),
        EvidenceStatusEntry(
            status="NOT_TESTED",
            machine_conditions="no corresponding plan executed",
            mapped_state=EV_EVIDENCE_STATES["NOT_TESTED"],
        ),
    )
    reg = EvidenceStatusRegistry(
        registry_id="evidence-status-registry",
        version="v1",
        entries=entries,
        frozen=True,
    )
    return dataclasses.replace(reg, content_hash=reg.compute_content_hash())


def verify_evidence_status_registry(
    registry: EvidenceStatusRegistry,
) -> VerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    if not registry.frozen:
        errors.append(EC.EV_REGISTRY_NOT_FROZEN)
        details.append("EvidenceStatusRegistry must be frozen in P4")

    if not registry.entries:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("EvidenceStatusRegistry must have at least one entry")

    seen: set[str] = set()
    for e in registry.entries:
        if e.status in seen:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"duplicate status {e.status}")
        seen.add(e.status)
        if e.status not in EV_EVIDENCE_STATUSES:
            errors.append(EC.EV_EVIDENCE_STATUS_INVALID)
            details.append(f"status {e.status} not in EV_EVIDENCE_STATUSES")
        if e.mapped_state != EV_EVIDENCE_STATES.get(e.status, ""):
            errors.append(EC.EV_EVIDENCE_STATUS_INVALID)
            details.append(
                f"status {e.status} mapped_state {e.mapped_state} != "
                f"{EV_EVIDENCE_STATES.get(e.status)}"
            )

    # 必须覆盖全部 5 个 status
    if registry.statuses() != EV_EVIDENCE_STATUSES:
        errors.append(EC.EV_EVIDENCE_STATUS_INVALID)
        details.append(
            f"registry must cover all EV_EVIDENCE_STATUSES, got {sorted(registry.statuses())}"
        )

    if not registry.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif registry.content_hash != registry.compute_content_hash():
        errors.append(EC.EV_REGISTRY_HASH_MISMATCH)
        details.append("EvidenceStatusRegistry content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_evidence_status_valid(
    registry: EvidenceStatusRegistry,
    status: str,
) -> VerificationResult:
    """检查 Evidence status 在冻结 registry 中。"""
    errors: list[EC] = []
    details: list[str] = []

    if not registry.frozen:
        errors.append(EC.EV_REGISTRY_NOT_FROZEN)
        details.append("registry not frozen")

    if status not in EV_EVIDENCE_STATUSES:
        errors.append(EC.EV_EVIDENCE_STATUS_INVALID)
        details.append(f"status {status} not in EV_EVIDENCE_STATUSES")

    if registry.get(status) is None:
        errors.append(EC.EV_EVIDENCE_STATUS_INVALID)
        details.append(f"status {status} not in frozen registry")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
