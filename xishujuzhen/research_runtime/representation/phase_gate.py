"""
P7-8.4/P7-8.5 分阶段进入顺序+防止过早数学包装。

plan行1167（系统探讨.md）："类型论、超图、可实现事件结构、因果实验和操作化泄漏指标先行；
严格信息论、范畴、层、TDA、HoTT在对象与分布假设成熟后进入。"

plan行1210（系统探讨.md）："何时高级几何/拓扑分析的数据量足够，而不是过早数学包装？"

分阶段进入顺序（P7-8.4）：
  先行阶段：类型论、超图、可实现事件结构、因果实验、操作化泄漏指标
  成熟后阶段：严格信息论、范畴、层、TDA、HoTT
  只有先行阶段全部完成后才进入成熟后阶段

防止过早数学包装（P7-8.5）：
  3项判定：样本量判定、状态空间完整性、基线比较可行性
"""

from typing import Dict, Any, List
from enum import Enum


class PhaseStage(Enum):
    """分阶段进入的两个阶段。"""
    PREREQUISITE = "prerequisite"  # 先行阶段
    ADVANCED = "advanced"          # 成熟后阶段


# 先行阶段方法（plan行1167）
PREREQUISITE_METHODS = [
    "type_theory",           # 类型论
    "hypergraph",            # 超图
    "event_structure",       # 可实现事件结构
    "causal_experiment",     # 因果实验
    "operational_leakage",   # 操作化泄漏指标
]

# 成熟后阶段方法（plan行1167）
ADVANCED_METHODS = [
    "strict_information_theory",  # 严格信息论
    "category",                   # 范畴
    "sheaf",                      # 层
    "tda",                        # TDA
    "hott",                       # HoTT
]


class PhaseGate:
    """
    P7-8.4：分阶段进入顺序。

    plan行1167："类型论、超图、可实现事件结构、因果实验和操作化泄漏指标先行；
    严格信息论、范畴、层、TDA、HoTT在对象与分布假设成熟后进入。"
    """

    def __init__(self):
        self._prerequisite_completed: Dict[str, bool] = {
            m: False for m in PREREQUISITE_METHODS
        }

    def mark_prerequisite_completed(self, method: str) -> None:
        if method not in self._prerequisite_completed:
            raise ValueError(f"未知先行阶段方法: {method}")
        self._prerequisite_completed[method] = True

    def check_all_prerequisites_completed(self) -> Dict[str, Any]:
        """检查先行阶段是否全部完成。"""
        completed = [m for m, v in self._prerequisite_completed.items() if v]
        not_completed = [m for m, v in self._prerequisite_completed.items() if not v]
        return {
            "n_prerequisites": len(PREREQUISITE_METHODS),
            "n_completed": len(completed),
            "completed": completed,
            "not_completed": not_completed,
            "all_completed": len(not_completed) == 0,
        }

    def can_enter_advanced(self, method: str) -> Dict[str, Any]:
        """
        检查是否可以进入成熟后阶段的指定方法。

        强制机制：只有先行阶段全部完成后才进入成熟后阶段。
        """
        if method not in ADVANCED_METHODS:
            return {
                "can_enter": False,
                "reason": f"未知成熟后阶段方法: {method}",
                "legitimate_methods": ADVANCED_METHODS,
            }

        check = self.check_all_prerequisites_completed()
        if not check["all_completed"]:
            return {
                "can_enter": False,
                "reason": f"先行阶段未全部完成: {check['not_completed']}",
                "prerequisite_check": check,
            }

        return {
            "can_enter": True,
            "method": method,
            "prerequisite_check": check,
        }

    def assert_can_enter_advanced(self, method: str) -> Dict[str, Any]:
        """断言可以进入成熟后阶段——先行阶段未全部完成时拒绝。"""
        check = self.can_enter_advanced(method)
        if not check["can_enter"]:
            raise PermissionError(
                f"不能进入成熟后阶段方法'{method}'：{check['reason']}"
            )
        return check


class PrematureMathPackagingGuard:
    """
    P7-8.5：防止过早数学包装。

    plan行1210："何时高级几何/拓扑分析的数据量足够，而不是过早数学包装？"
    """

    def __init__(self):
        self._sample_size: int = 0
        self._state_space_complete: bool = False
        self._baseline_feasible: bool = False

    def set_sample_size(self, n: int) -> None:
        self._sample_size = n

    def set_state_space_complete(self, complete: bool) -> None:
        self._state_space_complete = complete

    def set_baseline_feasible(self, feasible: bool) -> None:
        self._baseline_feasible = feasible

    def check_3_conditions(self, min_sample_size: int = 10) -> Dict[str, Any]:
        """
        3项判定：样本量判定、状态空间完整性、基线比较可行性。

        plan行1210："何时高级几何/拓扑分析的数据量足够，而不是过早数学包装？"
        """
        conditions = {
            "sample_size_sufficient": self._sample_size >= min_sample_size,
            "state_space_complete": self._state_space_complete,
            "baseline_feasible": self._baseline_feasible,
        }

        return {
            "conditions": conditions,
            "n_conditions_met": sum(1 for v in conditions.values() if v),
            "n_conditions_required": 3,
            "all_met": all(conditions.values()),
            "min_sample_size": min_sample_size,
            "current_sample_size": self._sample_size,
        }

    def assert_not_premature(self, min_sample_size: int = 10) -> Dict[str, Any]:
        """
        断言不是过早数学包装——3项判定未全部满足时拒绝。

        强制机制：过早数学包装→拒绝。
        """
        check = self.check_3_conditions(min_sample_size)
        if not check["all_met"]:
            unmet = [k for k, v in check["conditions"].items() if not v]
            raise PermissionError(
                f"过早数学包装：3项判定未全部满足。"
                f"plan行1210：何时高级几何/拓扑分析的数据量足够，而不是过早数学包装？"
                f"未满足的判定: {unmet}"
            )

        return {
            "not_premature": True,
            "conditions_met": 3,
            "check": check,
        }
