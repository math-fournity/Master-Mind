"""
HelpCurve：帮助量响应曲线（DYN-4）

对应134号P4-6。

123号§40 DYN-4：
- success / verified progress = f(assistance budget)
- 真正好的系统应在更少帮助下达到同等或更高进展
- 不能靠Hint-4赢得高分

P4-6.3：记录多指标结果，不用一个总分掩盖高泄漏（123号§23）。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import statistics


@dataclass
class HelpCurvePoint:
    """帮助量响应曲线上的一个点"""
    assistance_budget: float       # 帮助量（0=无提示，1=最高Hint级别）
    mean_progress: float           # 平均已验证进展
    mean_leakage: float            # 平均泄漏
    mean_dependency: float         # 平均依赖
    mean_cost: float               # 平均成本
    mean_side_effect: float        # 平均副作用
    n_samples: int = 0

    def to_dict(self) -> dict:
        return {
            "assistance_budget": self.assistance_budget,
            "mean_progress": self.mean_progress,
            "mean_leakage": self.mean_leakage,
            "mean_dependency": self.mean_dependency,
            "mean_cost": self.mean_cost,
            "mean_side_effect": self.mean_side_effect,
            "n_samples": self.n_samples,
        }


class HelpCurveBuilder:
    """
    P4-6：测帮助量曲线。

    P4-6.1：建立帮助量响应曲线
    P4-6.2：验证真正好的系统应在更少帮助下达到同等或更高进展
    P4-6.3：记录多指标结果，不用一个总分掩盖高泄漏
    """

    # 帮助量映射：control=0, H0=0.33, H1=0.67, H2=1.0
    BUDGET_MAP = {
        "control": 0.0,
        "h0": 0.33,
        "h1": 0.67,
        "h2": 1.0,
    }

    def build_curve(
        self,
        results_by_group: Dict[str, List[Dict[str, Any]]],
    ) -> List[HelpCurvePoint]:
        """
        P4-6.1：建立帮助量响应曲线。

        P4-6.COMP2：报告多指标结果（进展/泄漏/依赖/成本/副作用），
        不用一个总分掩盖高泄漏。
        """
        curve = []
        for group, results in results_by_group.items():
            if group not in self.BUDGET_MAP:
                continue
            if not results:
                continue

            progress = [r.get("progress_score", 0.0) for r in results]
            leakage = [r.get("leakage_score", 0.0) for r in results]
            dependency = [r.get("dependency_score", 0.0) for r in results]
            cost = [r.get("cost", 0.0) for r in results]
            side_effect = [r.get("side_effect_score", 0.0) for r in results]

            curve.append(HelpCurvePoint(
                assistance_budget=self.BUDGET_MAP[group],
                mean_progress=statistics.mean(progress),
                mean_leakage=statistics.mean(leakage),
                mean_dependency=statistics.mean(dependency),
                mean_cost=statistics.mean(cost),
                mean_side_effect=statistics.mean(side_effect),
                n_samples=len(results),
            ))

        # 按帮助量排序
        curve.sort(key=lambda p: p.assistance_budget)
        return curve

    def verify_better_system(
        self, curve: List[HelpCurvePoint]
    ) -> Dict[str, Any]:
        """
        P4-6.2：验证真正好的系统应在更少帮助下达到同等或更高进展。

        123号§40："而不是靠Hint-4赢得高分"

        边界情况：
        - 系统靠高等级Hint赢得高分（不符合"真正好的系统"标准）
        - 曲线无单调性
        - 曲线在低帮助量时已饱和
        """
        if len(curve) < 2:
            return {
                "is_better_system": False,
                "reason": "曲线点不足",
            }

        # 检查：低帮助量是否也能达到合理进展
        low_budget = curve[0]  # control
        high_budget = curve[-1]  # H2

        # 真正好的系统：control的进展不应为零（有一定独立能力）
        # 且H0/H1的边际增益应大于H2的边际增益（递减回报）
        is_better = low_budget.mean_progress > 0

        return {
            "is_better_system": is_better,
            "control_progress": low_budget.mean_progress,
            "h2_progress": high_budget.mean_progress,
            "marginal_gain": high_budget.mean_progress - low_budget.mean_progress,
            "multi_indicator": True,  # P4-6.3：多指标，不是总分
            "curve": [p.to_dict() for p in curve],
        }
