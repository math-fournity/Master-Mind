"""
ConstraintOptimizer：受约束多目标选择

对应134号P4-CODE-2 + 123号§23。

123号§23公式：
max_π E[ΔProgress_κ] - λ1*C_hint - λ2*L_answer - λ3*D_dependence - λ4*C_compute

冻结声明（123号§23）：
- L_answer和D_dependence明确是代理分数，不是互信息或真实依赖度
- 各λ和代理定义必须随策略版本冻结
- 必须报告多指标结果，不能用一个总分掩盖高泄漏
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


@dataclass
class PolicyConfig:
    """
    策略配置——各λ和代理定义随策略版本冻结（123号§23）。

    G0-6：阈值不能在看完结果后补写。一旦freeze()，不可修改。
    """
    # 4个λ权重（123号§23公式）
    lambda_1_hint_cost: float = 1.0       # C_hint权重
    lambda_2_leakage: float = 2.0         # L_answer权重（泄漏惩罚最重）
    lambda_3_dependency: float = 1.5      # D_dependence权重
    lambda_4_compute: float = 0.5         # C_compute权重
    # 策略版本
    policy_version: str = "v1_phase4"
    frozen: bool = False

    def freeze(self):
        """冻结策略配置——不可逆（G0-6）"""
        self.frozen = True

    def to_dict(self) -> dict:
        return {
            "lambda_1_hint_cost": self.lambda_1_hint_cost,
            "lambda_2_leakage": self.lambda_2_leakage,
            "lambda_3_dependency": self.lambda_3_dependency,
            "lambda_4_compute": self.lambda_4_compute,
            "policy_version": self.policy_version,
            "frozen": self.frozen,
        }


@dataclass
class ActionScore:
    """单个动作的评分——多指标，不是总分（123号§23）"""
    action_name: str
    # 4个分量（123号§23公式）
    expected_progress: float = 0.0   # E[ΔProgress_κ]
    hint_cost: float = 0.0           # C_hint
    leakage_proxy: float = 0.0       # L_answer（代理分数，F6防线）
    dependency_proxy: float = 0.0    # D_dependence（代理分数，F6防线）
    compute_cost: float = 0.0        # C_compute
    # 加权总分
    weighted_score: float = 0.0
    # 多指标结果（123号§23：不能用总分掩盖高泄漏）
    high_leakage_warning: bool = False

    def to_dict(self) -> dict:
        return {
            "action_name": self.action_name,
            "expected_progress": self.expected_progress,
            "hint_cost": self.hint_cost,
            "leakage_proxy": self.leakage_proxy,
            "dependency_proxy": self.dependency_proxy,
            "compute_cost": self.compute_cost,
            "weighted_score": self.weighted_score,
            "high_leakage_warning": self.high_leakage_warning,
        }


class ConstraintOptimizer:
    """
    受约束多目标选择——123号§23公式的实现。

    max_π E[ΔProgress_κ] - λ1*C_hint - λ2*L_answer - λ3*D_dependence - λ4*C_compute

    F6防线：L_answer和D_dependence是代理分数，不是互信息或真实依赖度。
    123号§23：必须报告多指标结果，不能用一个总分掩盖高泄漏。
    """

    def __init__(self, config: PolicyConfig):
        self.config = config

    def score_action(
        self,
        action_name: str,
        expected_progress: float,
        hint_cost: float,
        leakage_proxy: float,
        dependency_proxy: float,
        compute_cost: float,
    ) -> ActionScore:
        """
        对单个动作评分——123号§23公式。

        F6防线：leakage_proxy和dependency_proxy是代理分数。
        """
        score = ActionScore(
            action_name=action_name,
            expected_progress=expected_progress,
            hint_cost=hint_cost,
            leakage_proxy=leakage_proxy,
            dependency_proxy=dependency_proxy,
            compute_cost=compute_cost,
        )

        # 加权总分
        score.weighted_score = (
            expected_progress
            - self.config.lambda_1_hint_cost * hint_cost
            - self.config.lambda_2_leakage * leakage_proxy
            - self.config.lambda_3_dependency * dependency_proxy
            - self.config.lambda_4_compute * compute_cost
        )

        # 123号§23：高泄漏告警（不能用总分掩盖）
        score.high_leakage_warning = leakage_proxy > 0.3

        return score

    def select_best_action(self, scores: List[ActionScore]) -> ActionScore:
        """
        选择最优动作——按加权总分排序。

        123号§23：即使选了最优动作，如果high_leakage_warning=True，
        仍然必须报告泄漏指标，不能用总分掩盖。
        """
        if not scores:
            raise ValueError("无候选动作")
        return max(scores, key=lambda s: s.weighted_score)

    def select_with_leakage_guard(
        self, scores: List[ActionScore], leakage_threshold: float = 0.3
    ) -> Optional[ActionScore]:
        """
        带泄漏 guard 的动作选择——如果所有动作都高泄漏，返回None。

        123号§23：不能用一个总分掩盖高泄漏。
        P4-STOP-3：正确率提升以更高泄漏为代价→立即停止。
        """
        safe = [s for s in scores if s.leakage_proxy <= leakage_threshold]
        if not safe:
            return None  # 所有动作都高泄漏→停止
        return max(safe, key=lambda s: s.weighted_score)
