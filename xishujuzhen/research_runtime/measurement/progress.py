"""
progress-measurement 原语（261号§3.4）。

从dynamic-workspace的六元组状态 (V_t, F_t, O_t, R_t, E_t, U_t) 中
提取5个可测量分量，计算进展偏序 P_κ(S_t)。

5个进展分量：
1. step_progress: 已完成步骤数 / 总步骤数 (0-1)
2. verified_core_count: V_t 条目数
3. open_obligation_count: O_t 中 open 状态数
4. unresolved_severity: U_t 中 blocking 数量
5. representation_richness: R_t 条目数

偏序比较：分量级比较，产生4种结果（superior/inferior/incomparable/equal）。
- 分量 1,2,5: 越大越好
- 分量 3,4: 越小越好（open义务少=进展高，未解决问题少=进展高）
"""

from dataclasses import dataclass
from typing import Union

from ..parser.models import SixTuple


@dataclass
class ProgressVector:
    """进展向量——5个分量"""
    step_progress: float         # 分量1: 已完成步骤数/总步骤数 (0-1)
    verified_core_count: int     # 分量2: V_t条目数
    open_obligation_count: int   # 分量3: O_t中open状态数
    unresolved_severity: int     # 分量4: U_t中blocking数量
    representation_richness: int # 分量5: R_t条目数

    def __repr__(self) -> str:
        return (
            f"ProgressVector(step={self.step_progress:.2f}, "
            f"V={self.verified_core_count}, "
            f"O={self.open_obligation_count}, "
            f"U={self.unresolved_severity}, "
            f"R={self.representation_richness})"
        )


@dataclass
class ProgressComparison:
    """进展偏序比较结果"""
    result: str   # "superior" / "inferior" / "incomparable" / "equal"
    details: str  # 比较细节

    def __repr__(self) -> str:
        return f"ProgressComparison(result={self.result}, details={self.details})"


class ProgressMeasurer:
    """进展度量器：从六元组提取进展向量，并支持偏序比较与瓶颈识别。"""

    def __init__(self, total_steps: int = 10):
        self.total_steps = total_steps

    def measure(self, six_tuple: Union[SixTuple, dict], current_step: int) -> ProgressVector:
        """
        从六元组提取5个进展分量。

        Args:
            six_tuple: SixTuple 对象或其 to_dict() 的 dict 表示
            current_step: 当前已完成步骤数（1-based 的轮次索引）

        Returns:
            ProgressVector
        """
        # 兼容 SixTuple 对象与 dict 两种输入
        if isinstance(six_tuple, SixTuple):
            V_t = six_tuple.V_t
            O_t = six_tuple.O_t
            R_t = six_tuple.R_t
            U_t = six_tuple.U_t
            open_obligation_count = sum(1 for o in O_t if o.status == "open")
            unresolved_severity = sum(1 for u in U_t if u.severity == "blocking")
            verified_core_count = len(V_t)
            representation_richness = len(R_t)
        else:
            V_t = six_tuple.get("V_t", [])
            O_t = six_tuple.get("O_t", [])
            R_t = six_tuple.get("R_t", [])
            U_t = six_tuple.get("U_t", [])
            open_obligation_count = sum(1 for o in O_t if o.get("status") == "open")
            unresolved_severity = sum(1 for u in U_t if u.get("severity") == "blocking")
            verified_core_count = len(V_t)
            representation_richness = len(R_t)

        step_progress = current_step / self.total_steps if self.total_steps > 0 else 0.0

        return ProgressVector(
            step_progress=step_progress,
            verified_core_count=verified_core_count,
            open_obligation_count=open_obligation_count,
            unresolved_severity=unresolved_severity,
            representation_richness=representation_richness,
        )

    def compare(self, v1: ProgressVector, v2: ProgressVector) -> ProgressComparison:
        """
        偏序比较两个进展向量。

        分量方向：
        - step_progress, verified_core_count, representation_richness: 越大越好
        - open_obligation_count, unresolved_severity: 越小越好

        规则：
        - v1 在所有分量上 ≥ v2 → superior
        - v1 在所有分量上 ≤ v2 → inferior
        - v1 在所有分量上 == v2 → equal
        - 否则 → incomparable
        """
        # 规范化：把"越大越好"的分量保持原值，"越小越好"的分量取负，
        # 这样统一成"越大越好"的偏序。
        def _norm(v: ProgressVector):
            return (
                v.step_progress,
                v.verified_core_count,
                -v.open_obligation_count,
                -v.unresolved_severity,
                v.representation_richness,
            )

        n1 = _norm(v1)
        n2 = _norm(v2)

        ge_all = all(a >= b for a, b in zip(n1, n2))
        le_all = all(a <= b for a, b in zip(n1, n2))
        eq_all = all(a == b for a, b in zip(n1, n2))

        if eq_all:
            return ProgressComparison(result="equal", details="所有5个分量完全相等")
        if ge_all and not le_all:
            return ProgressComparison(result="superior", details="v1在所有分量上≥v2（至少一个严格>）")
        if le_all and not ge_all:
            return ProgressComparison(result="inferior", details="v1在所有分量上≤v2（至少一个严格<）")
        return ProgressComparison(
            result="incomparable",
            details="v1与v2存在分量交叉，无法偏序比较",
        )

    def identify_bottleneck(self, v: ProgressVector) -> str:
        """
        识别进展瓶颈。

        优先级（从最严重到最轻）：
        1. unresolved_severity > 0 → "未解决问题是瓶颈"
        2. open_obligation_count > 2 → "开放义务过多"
        3. step_progress < 0.5 → "步骤进展不足"
        4. 否则 → "无明显瓶颈"
        """
        if v.unresolved_severity > 0:
            return "未解决问题是瓶颈"
        if v.open_obligation_count > 2:
            return "开放义务过多"
        if v.step_progress < 0.5:
            return "步骤进展不足"
        return "无明显瓶颈"
