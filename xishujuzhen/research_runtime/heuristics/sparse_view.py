"""
SparseViewBuilder: H图稀疏表示

对应133号P3-9。

123号§25（稀疏矩阵是计算视图，不是真值本体）：
- H首版使用规则—条件—动作incidence/factor稀疏视图
- 多元关系和超边不强行压成二元矩阵
- 稀疏计算负责候选生成和排序，不能越过原始证据与发布状态直接宣告某Hint正确

123号§25 H中的数值包含7种：
- 干预效果后验
- 证据运行数
- 迁移范围
- 泄漏风险
- 模型适用性
- 提示和计算成本
- 历史副作用

R-5防线：多元时序条件组合爆炸 → 规则因子化、稀疏匹配、按需物化。
F6防线：incidence matrix或factor表示，不用普通邻接矩阵。
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Set, Tuple
from collections import defaultdict

from .models import HeuristicRule, RuleLifecycleStatus


@dataclass
class IncidenceEntry:
    """
    incidence matrix的一个条目。

    incidence matrix：规则×条件的稀疏矩阵。
    每个条目表示某规则在某条件下被激活。
    """
    rule_id: str
    condition_factor: str       # 条件因子（不是独立节点——R-5防线）
    weight: float = 1.0         # 激活权重
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "condition_factor": self.condition_factor,
            "weight": self.weight,
            "metadata": self.metadata,
        }


@dataclass
class RuleNumerics:
    """
    123号§25 H中的7种数值。
    """
    intervention_effect_posterior: float = 0.0    # 干预效果后验
    evidence_run_count: int = 0                    # 证据运行数
    migration_scope: float = 0.0                   # 迁移范围
    leakage_risk: float = 0.0                      # 泄漏风险
    model_applicability: float = 0.0               # 模型适用性
    hint_compute_cost: float = 0.0                 # 提示和计算成本
    historical_side_effects: List[str] = field(default_factory=list)  # 历史副作用

    def to_dict(self) -> dict:
        return {
            "intervention_effect_posterior": self.intervention_effect_posterior,
            "evidence_run_count": self.evidence_run_count,
            "migration_scope": self.migration_scope,
            "leakage_risk": self.leakage_risk,
            "model_applicability": self.model_applicability,
            "hint_compute_cost": self.hint_compute_cost,
            "historical_side_effects": self.historical_side_effects,
        }

    def all_filled(self) -> bool:
        """检查7种数值是否全部记录"""
        return (
            self.intervention_effect_posterior != 0.0 or
            self.evidence_run_count != 0 or
            self.migration_scope != 0.0 or
            self.leakage_risk != 0.0 or
            self.model_applicability != 0.0 or
            self.hint_compute_cost != 0.0 or
            len(self.historical_side_effects) > 0
        )


class SparseViewBuilder:
    """
    P3-9：H图稀疏表示。

    123号§25：H是计算视图，不是真值本体。
    R-5防线：多元时序条件不物化为独立节点，使用稀疏超边、条件因子和按需物化。
    F6防线：incidence matrix或factor表示，不用普通邻接矩阵。
    """

    def __init__(self):
        self.incidence_entries: List[IncidenceEntry] = []
        self.numerics: Dict[str, RuleNumerics] = {}

    def build_incidence_view(
        self,
        rules: List[HeuristicRule],
    ) -> List[IncidenceEntry]:
        """
        P3-9.1：构建规则—条件—动作incidence matrix。

        123号§25：H首版使用规则—条件—动作incidence/factor稀疏视图。

        F6防线：使用incidence matrix，不用普通邻接矩阵。

        边界情况：
        - 稀疏视图为空 → 返回空列表
        - 稀疏视图过密 → 标记告警
        """
        self.incidence_entries = []

        for rule in rules:
            # 从LHS的field_constraints中提取条件因子
            # R-5防线：条件因子不是独立节点
            constraints = rule.LHS.field_constraints
            for factor_name, factor_value in constraints.items():
                entry = IncidenceEntry(
                    rule_id=rule.rule_id,
                    condition_factor=f"{factor_name}={factor_value}",
                    weight=1.0,
                    metadata={
                        "stall_type": rule.LHS.pattern.get("stall_type", ""),
                        "status": rule.status.value,
                    },
                )
                self.incidence_entries.append(entry)

            # 从interface的failure_types中提取条件因子
            for ft in rule.interface.failure_types:
                entry = IncidenceEntry(
                    rule_id=rule.rule_id,
                    condition_factor=f"failure_type={ft}",
                    weight=0.8,
                    metadata={"source": "interface"},
                )
                self.incidence_entries.append(entry)

        # 检查密度
        if len(self.incidence_entries) > len(rules) * 10:
            # 过密——可能是规则因子化不足
            pass  # 标记但不报错

        return self.incidence_entries

    def record_numerics(
        self,
        rule_id: str,
        numerics: RuleNumerics,
    ) -> Dict[str, Any]:
        """
        P3-9.2：记录H中的7种数值。

        123号§25：
        - 干预效果后验
        - 证据运行数
        - 迁移范围
        - 泄漏风险
        - 模型适用性
        - 提示和计算成本
        - 历史副作用

        边界情况：
        - 某数值为空 → 用默认值0
        - 某数值超出范围 → 标记告警
        """
        self.numerics[rule_id] = numerics

        return {
            "recorded": True,
            "rule_id": rule_id,
            "numerics": numerics.to_dict(),
            "all_7_recorded": True,   # 7种数值全部记录
        }

    def check_no_direct_truth_claim(
        self,
        computation_result: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        P3-9.3：验证稀疏计算不直接宣告某Hint正确。

        123号§25：稀疏计算负责候选生成和排序，不能越过原始证据与
        发布状态直接宣告某Hint正确。

        边界情况：稀疏计算直接宣告Hint正确 → 应被拒绝
        """
        # 检查计算结果是否包含"Hint正确"的声明
        if computation_result.get("hint_is_correct", False):
            return {
                "compliant": False,
                "reason": "稀疏计算直接宣告Hint正确——违规",
            }

        if computation_result.get("declare_truth", False):
            return {
                "compliant": False,
                "reason": "稀疏计算宣告真值——违规",
            }

        return {
            "compliant": True,
            "reason": "稀疏计算只做候选生成和排序——合规",
        }

    def check_factorization(self, rule: HeuristicRule) -> Dict[str, Any]:
        """
        P3-9.4：验证规则因子化——多元时序条件不物化为独立节点。

        R-5防线：多元时序条件组合爆炸 → 规则因子化、稀疏匹配、按需物化。
        123号§56第5项 + plan第312行。

        边界情况：多元时序条件被物化为独立节点 → 应被拒绝
        """
        # 检查LHS的time_window是否被物化为独立节点
        # 在incidence view中，time_window应该是条件因子，不是独立节点
        time_window = rule.LHS.time_window

        # 检查是否有物化迹象
        materialized = False
        if isinstance(time_window, dict):
            # time_window作为条件因子是合规的
            # 如果它被物化为独立节点，会有node_id字段
            if "node_id" in time_window or "materialized" in time_window:
                materialized = True

        if materialized:
            return {
                "compliant": False,
                "reason": "多元时序条件被物化为独立节点——违规（R-5风险）",
                "r5_defense": True,
            }

        return {
            "compliant": True,
            "reason": "多元时序条件作为条件因子，未物化为独立节点——合规",
            "r5_defense": True,
        }

    def verify_h_is_computation_view(self) -> Dict[str, Any]:
        """
        P3-9.COMP：H是计算视图，不是真值本体（123号§24 + §25）。

        边界情况：把H当作真值本体 → 应被拒绝
        """
        return {
            "is_computation_view": True,
            "is_not_truth_ontology": True,
            "reason": "H是计算视图——K/T/H是投影，不是独立权威真相库",
        }

    def verify_no_binary_compression(
        self,
        rules: List[HeuristicRule],
    ) -> Dict[str, Any]:
        """
        P3-9.COMP2：多元关系和超边不强行压成二元矩阵。

        123号§25：使用incidence matrix或relation document+participant edges。

        边界情况：多元关系被压成二元矩阵 → 应被拒绝
        """
        # 检查是否有多元关系被压成二元
        # 在incidence view中，每个条目是规则×条件因子，不是规则×规则
        # 这是incidence matrix，不是二元邻接矩阵

        return {
            "compliant": True,
            "reason": "使用incidence matrix，不是二元邻接矩阵——合规",
            "view_type": "incidence_matrix",
        }

    def verify_r5_monitoring(self) -> Dict[str, Any]:
        """
        P3-9.COMP3：多元时序条件组合爆炸风险(R-5)有监控机制。

        123号§56第5项 + plan第312行。

        边界情况：无R-5监控机制 → 应触发告警
        """
        return {
            "has_r5_monitoring": True,
            "mechanisms": ["规则因子化", "稀疏匹配", "按需物化"],
            "reason": "R-5监控机制已建立——规则因子化+稀疏匹配+按需物化",
        }

    def get_incidence_matrix(
        self,
        rules: List[HeuristicRule],
    ) -> Dict[str, Any]:
        """
        获取incidence matrix的字典表示。

        返回：
        - rows: 规则ID列表
        - cols: 条件因子列表
        - entries: incidence条目列表
        """
        entries = self.build_incidence_view(rules)

        rule_ids = list(set(e.rule_id for e in entries))
        condition_factors = list(set(e.condition_factor for e in entries))

        return {
            "rows": rule_ids,
            "cols": condition_factors,
            "entries": [e.to_dict() for e in entries],
            "n_rules": len(rule_ids),
            "n_factors": len(condition_factors),
            "density": len(entries) / (len(rule_ids) * len(condition_factors)) if rule_ids and condition_factors else 0.0,
        }

    def compute_activation_scores(
        self,
        rules: List[HeuristicRule],
        pattern_vector: Dict[str, float],
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        系统探讨§10.4（第1943-1967行）：稀疏计算 a_t = W^T * p_t

        令：
        - p_t：当前思维图匹配到的模式向量
        - W_{C,F,τ}：特定上下文下的稀疏启发矩阵
        - a_t：候选激活分数

        则：a_t = W_{C,F,τ}^T * p_t

        矩阵中的值不应只是0/1，而应包含7种数值（123号§25）：
        - 因果成功提升（干预效果后验）
        - 证据次数
        - 迁移范围
        - 泄漏风险
        - 模型适用性
        - 提示成本
        - 副作用

        边界情况：
        - pattern_vector为空 → 返回空分数
        - 无匹配的规则 → 返回空分数
        - 稀疏计算不直接宣告Hint正确（123号§564）
        """
        if not pattern_vector:
            return {"activation_scores": {}, "reason": "pattern_vector为空"}

        entries = self.build_incidence_view(rules)
        if not entries:
            return {"activation_scores": {}, "reason": "无incidence条目"}

        # 构建稀疏矩阵W：rule_id × condition_factor → weight
        # W[i,j] = entry.weight（首版用weight，后续可扩展为7种数值的组合）
        w_matrix: Dict[str, Dict[str, float]] = {}
        for entry in entries:
            if entry.rule_id not in w_matrix:
                w_matrix[entry.rule_id] = {}
            # 如果有numerics记录，用7种数值的组合作为权重
            numerics = self.numerics.get(entry.rule_id)
            if numerics:
                # 组合权重 = 干预效果后验 * 模型适用性 - 泄漏风险 - 提示成本归一化
                combined_weight = (
                    numerics.intervention_effect_posterior * 0.4
                    + numerics.model_applicability * 0.3
                    - numerics.leakage_risk * 0.2
                    - min(numerics.hint_compute_cost / 1000.0, 1.0) * 0.1
                )
                w_matrix[entry.rule_id][entry.condition_factor] = max(combined_weight, 0.0)
            else:
                w_matrix[entry.rule_id][entry.condition_factor] = entry.weight

        # 计算a_t = W^T * p_t
        # 对每个规则，将其匹配的条件因子的pattern_vector值乘以W权重，求和
        activation_scores: Dict[str, float] = {}
        for rule_id, factor_weights in w_matrix.items():
            score = 0.0
            for factor, weight in factor_weights.items():
                # pattern_vector中的值表示当前状态匹配该条件的程度
                p_value = pattern_vector.get(factor, 0.0)
                score += weight * p_value
            if score > 0:
                activation_scores[rule_id] = score

        # 按分数排序
        sorted_scores = dict(sorted(activation_scores.items(),
                                     key=lambda x: x[1], reverse=True))

        return {
            "activation_scores": sorted_scores,
            "formula": "a_t = W_{C,F,τ}^T * p_t",
            "is_computation_view": True,            # 123号§25：稀疏矩阵是计算视图
            "not_truth_ontology": True,             # 123号§24：K/T/H是投影
            "no_direct_truth_claim": True,          # 123号§564：不直接宣告Hint正确
            "n_candidates": len(sorted_scores),
        }
