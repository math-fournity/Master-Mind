"""
policy模块：受约束动作选择

对应134号P4-CODE-2。

123号§23最小提示是受约束的多目标选择问题：
max_π E[ΔProgress_κ] - λ1*C_hint - λ2*L_answer - λ3*D_dependence - λ4*C_compute

约束：
- L_answer和D_dependence明确是代理分数，不是互信息或真实依赖度
- 各λ和代理定义必须随策略版本冻结
- 必须报告多指标结果
- 不能用一个总分掩盖高泄漏
"""

from .constraint_optimizer import ConstraintOptimizer, PolicyConfig, ActionScore
from .constrained_optimizer import (
    ConstrainedPolicy,
    MatchedRule,
    ConstraintValues,
    SelectionResult,
    leakage_risk,
)

__all__ = [
    # 旧版（134号P4-CODE-2 / 123号§23）
    "ConstraintOptimizer", "PolicyConfig", "ActionScore",
    # 新版（261号§4.4 受约束多目标策略）
    "ConstrainedPolicy", "MatchedRule", "ConstraintValues", "SelectionResult",
    "leakage_risk",
]
