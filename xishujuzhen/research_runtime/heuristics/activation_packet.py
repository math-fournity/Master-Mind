"""
ActivationPacketDesigner: 设计H0—H2激活包

对应133号P3-4。

123号§39（DYN-3定义H0/H1/H2）+ §21（激活包优先加入项）+
128号§3（Ramsey案例干预阶梯）。

128号§3.2 Ramsey案例冻结的干预阶梯：
- Hint-0（元检查）："你是否只在改指数？先列出表达式中可变化的结构部分。"
- Hint-1（研究操作）："把底数和指数分开分析，并说明递归障碍影响哪一部分。"
- Hint-2（概念/工具候选）："递归规模缩减有时由迭代对数描述；把它作为候选工具而非结论。"
- 禁止（答案等价）："底数变成log k，指数k/3不变"

123号§21激活包优先加入：
- 一个检查问题（H0）
- 一个研究操作（H1）
- 一个新表示
- 一个开放子目标
- 一个工具调用
- 一个反例方向
- 一个有接口的定理候选

其中H0/H1/H2分别对应：
- H0 → 检查问题
- H1 → 研究操作
- H2 → 概念/工具候选
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List
from enum import Enum


class HintLevel(str, Enum):
    """123号§39 DYN-3定义的Hint级别"""
    H0 = "h0"   # 元检查
    H1 = "h1"   # 思维操作
    H2 = "h2"   # 概念/工具候选


@dataclass
class ActivationPacket:
    """
    激活包——HeuristicRule.RHS的具体化。

    冻结声明（127号§7）：
    - 激活包不应直接把目标结论加入V_t（P3-3.COMP4）
    """
    packet_id: str
    level: HintLevel
    text: str                           # Hint文本
    match_condition: Dict[str, Any] = field(default_factory=dict)
    check_question: str = ""
    research_action: str = ""
    new_representation: str = ""
    open_subgoal: str = ""
    tool_call: str = ""
    counterexample_direction: str = ""
    theorem_candidate: str = ""

    def to_dict(self) -> dict:
        return {
            "packet_id": self.packet_id,
            "level": self.level.value,
            "text": self.text,
            "match_condition": self.match_condition,
            "check_question": self.check_question,
            "research_action": self.research_action,
            "new_representation": self.new_representation,
            "open_subgoal": self.open_subgoal,
            "tool_call": self.tool_call,
            "counterexample_direction": self.counterexample_direction,
            "theorem_candidate": self.theorem_candidate,
        }


class ActivationPacketDesigner:
    """
    P3-4：设计H0—H2激活包。

    基于128号§3.2 Ramsey案例冻结的干预阶梯。
    """

    # 128号§3.2 Ramsey案例冻结的干预阶梯
    RAMSEY_HINTS = {
        HintLevel.H0: "你是否只在改指数？先列出表达式中可变化的结构部分。",
        HintLevel.H1: "把底数和指数分开分析，并说明递归障碍影响哪一部分。",
        HintLevel.H2: "递归规模缩减有时由迭代对数描述；把它作为候选工具而非结论。",
    }

    # 128号§3.2 禁止级别（答案等价内容）
    RAMSEY_FORBIDDEN = "底数变成log k，指数k/3不变"

    def __init__(self):
        self.packet_counter = 0

    def design_h0(self, match_condition: Dict[str, Any]) -> ActivationPacket:
        """
        P3-4.1：设计H0（元检查）——一个检查问题。

        Ramsey案例H0："你是否只在改指数？先列出表达式中可变化的结构部分。"（128号§3.2）

        深度标准：有可执行的H0激活包对象，含检查问题文本和匹配条件。
        """
        self.packet_counter += 1
        text = self.RAMSEY_HINTS[HintLevel.H0]
        return ActivationPacket(
            packet_id=f"packet_h0_{self.packet_counter}",
            level=HintLevel.H0,
            text=text,
            match_condition=match_condition,
            check_question=text,
        )

    def design_h1(self, match_condition: Dict[str, Any]) -> ActivationPacket:
        """
        P3-4.2：设计H1（思维操作）——一个研究操作。

        Ramsey案例H1："把底数和指数分开分析，并说明递归障碍影响哪一部分。"（128号§3.2）

        深度标准：有可执行的H1激活包对象，含研究操作描述和匹配条件。
        """
        self.packet_counter += 1
        text = self.RAMSEY_HINTS[HintLevel.H1]
        return ActivationPacket(
            packet_id=f"packet_h1_{self.packet_counter}",
            level=HintLevel.H1,
            text=text,
            match_condition=match_condition,
            research_action=text,
        )

    def design_h2(self, match_condition: Dict[str, Any]) -> ActivationPacket:
        """
        P3-4.3：设计H2（概念/工具候选）——一个概念或工具候选。

        Ramsey案例H2："递归规模缩减有时由迭代对数描述；把它作为候选工具而非结论。"（128号§3.2）

        深度标准：有可执行的H2激活包对象，含概念/工具候选描述和匹配条件。
        """
        self.packet_counter += 1
        text = self.RAMSEY_HINTS[HintLevel.H2]
        return ActivationPacket(
            packet_id=f"packet_h2_{self.packet_counter}",
            level=HintLevel.H2,
            text=text,
            match_condition=match_condition,
            tool_call=text,
        )

    def check_forbidden(self, hint_text: str) -> Dict[str, Any]:
        """
        P3-4.4：定义禁止级别——答案等价内容。

        Ramsey案例禁止："底数变成log k，指数k/3不变"（128号§3.2）

        深度标准：有可执行的禁止级别判定函数，检测Hint是否包含答案等价内容。

        边界情况：
        - Hint刚好等于答案等价内容 → 应被拒绝
        - Hint接近但不等于答案等价内容 → 标记为"接近禁止边界"
        """
        forbidden = self.RAMSEY_FORBIDDEN

        # 精确匹配
        if hint_text == forbidden:
            return {
                "is_forbidden": True,
                "reason": "Hint等于答案等价内容",
                "matched": "exact",
            }

        # 部分匹配——Hint包含禁止内容的关键部分
        forbidden_parts = ["底数变成log k", "指数k/3不变"]
        matched_parts = [p for p in forbidden_parts if p in hint_text]
        if matched_parts:
            return {
                "is_forbidden": True,
                "reason": f"Hint包含答案等价内容的关键部分：{matched_parts}",
                "matched": "partial",
            }

        # 接近禁止边界——检查相似度
        # 简化版：检查是否同时包含"底数"和"log"和"指数"和"k/3"
        if all(kw in hint_text for kw in ["底数", "log", "指数", "k/3"]):
            return {
                "is_forbidden": False,
                "reason": "Hint接近禁止边界，需人工审查",
                "matched": "near_boundary",
            }

        return {
            "is_forbidden": False,
            "reason": "Hint不包含答案等价内容",
            "matched": "none",
        }

    def design_all_levels(self, match_condition: Dict[str, Any]) -> List[ActivationPacket]:
        """
        设计H0/H1/H2全部三个级别的激活包。

        P3-4.COMP：H0/H1/H2分别对应123号§21激活包优先加入的
        "检查问题/研究操作/概念工具候选"。
        """
        return [
            self.design_h0(match_condition),
            self.design_h1(match_condition),
            self.design_h2(match_condition),
        ]

    def to_rhs_dict(self, packet: ActivationPacket) -> Dict[str, Any]:
        """
        将激活包转换为RHS字典格式（供RuleExtractor.extract_rhs使用）。
        """
        return {
            "activation_packet": packet.to_dict(),
            "check_question": packet.check_question,
            "research_action": packet.research_action,
            "new_representation": packet.new_representation,
            "open_subgoal": packet.open_subgoal,
            "tool_call": packet.tool_call,
            "counterexample_direction": packet.counterexample_direction,
            "theorem_candidate": packet.theorem_candidate,
        }
