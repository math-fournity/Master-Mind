"""
预算管理模块（261号§4.8）。

管理研究运行时的各类预算：token/计算/工具/分支/Hint。
每种预算有 remaining 和 spent 两个值。
Hint预算单独追踪（253号10轮QA消耗Hint预算的场景）。
"""

from dataclasses import dataclass, field
from typing import Dict, Optional
from enum import Enum


class BudgetType(str, Enum):
    """预算类型（261号§4.8）。"""
    TOKEN = "token"            # token预算
    COMPUTE = "compute"        # 计算预算
    TOOL = "tool"              # 工具调用预算
    BRANCH = "branch"          # 分支预算
    HINT = "hint"              # Hint预算（单独追踪）


@dataclass
class BudgetItem:
    """单项预算的余额状态。"""
    total: float = 0.0
    spent: float = 0.0

    @property
    def remaining(self) -> float:
        return self.total - self.spent

    def to_dict(self) -> dict:
        return {
            "total": self.total,
            "spent": self.spent,
            "remaining": self.remaining,
        }


class BudgetManager:
    """
    预算管理器（261号§4.8）。

    管理token/计算/工具/分支/Hint五类预算。
    超限触发硬性停止（consume返回False）。
    Hint预算单独追踪。
    """

    def __init__(self) -> None:
        self._budgets: Dict[str, BudgetItem] = {
            bt.value: BudgetItem() for bt in BudgetType
        }

    def set_budget(self, budget_type: str, total: float) -> None:
        """设置某类预算的总额。"""
        key = self._key(budget_type)
        self._budgets[key] = BudgetItem(total=total, spent=0.0)

    def consume(self, budget_type: str, amount: float) -> bool:
        """
        消耗预算。

        若剩余不足则不消耗，返回False（硬性停止信号）。
        若足够则扣减，返回True。
        """
        key = self._key(budget_type)
        item = self._budgets.get(key)
        if item is None:
            return False
        if amount < 0:
            return False
        if item.remaining < amount:
            return False
        item.spent += amount
        return True

    def check_remaining(self, budget_type: str) -> float:
        """检查某类预算的余额。"""
        key = self._key(budget_type)
        item = self._budgets.get(key)
        if item is None:
            return 0.0
        return item.remaining

    def is_exhausted(self, budget_type: str) -> bool:
        """某类预算是否超限（余额<=0）。"""
        return self.check_remaining(budget_type) <= 0

    def get_status(self) -> dict:
        """获取所有预算状态。"""
        return {k: v.to_dict() for k, v in self._budgets.items()}

    def get_hint_remaining(self) -> float:
        """Hint预算单独追踪：获取Hint余额。"""
        return self.check_remaining(BudgetType.HINT.value)

    def consume_hint(self, amount: float = 1.0) -> bool:
        """Hint预算单独追踪：消耗1个Hint。"""
        return self.consume(BudgetType.HINT.value, amount)

    def is_hint_exhausted(self) -> bool:
        """Hint预算单独追踪：是否超限。"""
        return self.is_exhausted(BudgetType.HINT.value)

    @staticmethod
    def _key(budget_type: str) -> str:
        """统一预算类型key（支持传BudgetType枚举或字符串）。"""
        if isinstance(budget_type, BudgetType):
            return budget_type.value
        return budget_type
