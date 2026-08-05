"""
TreatmentGroups：四组处理定义（control/H0/H1/H2）

对应134号P4-2。

123号§39 DYN-3定义四组处理：
- control：无提示
- H0：元检查（一个检查问题）
- H1：思维操作（一个研究操作）
- H2：概念/工具候选

128号§3.2 Ramsey案例冻结的干预阶梯：
- Hint-0："你是否只在改指数？先列出表达式中可变化的结构部分。"
- Hint-1："把底数和指数分开分析，并说明递归障碍影响哪一部分。"
- Hint-2："递归规模缩减有时由迭代对数描述；把它作为候选工具而非结论。"
- 禁止（答案等价）："底数变成log k，指数k/3不变"

P4-2.3边界情况：H0/H1/H2包含答案等价内容（应被拒绝）
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List
from enum import Enum


class TreatmentGroup(str, Enum):
    """123号§39 DYN-3定义的四组处理"""
    CONTROL = "control"   # 无提示
    H0 = "h0"             # 元检查（一个检查问题）
    H1 = "h1"             # 思维操作（一个研究操作）
    H2 = "h2"             # 概念/工具候选


# 128号§3.2冻结的Ramsey案例干预阶梯文本
RAMSEY_HINT_TEXTS = {
    TreatmentGroup.CONTROL: "",  # 无提示
    TreatmentGroup.H0: "你是否只在改指数？先列出表达式中可变化的结构部分。",
    TreatmentGroup.H1: "把底数和指数分开分析，并说明递归障碍影响哪一部分。",
    TreatmentGroup.H2: "递归规模缩减有时由迭代对数描述；把它作为候选工具而非结论。",
}

# 128号§3.2禁止的答案等价内容——用于P4-2.3验证
FORBIDDEN_ANSWER_EQUIVALENT = "底数变成log k，指数k/3不变"


@dataclass
class TreatmentDefinition:
    """单组处理定义"""
    group: TreatmentGroup
    hint_text: str
    description: str
    is_answer_equivalent: bool = False  # P4-2.3：验证是否含答案等价内容

    def to_dict(self) -> dict:
        return {
            "group": self.group.value,
            "hint_text": self.hint_text,
            "description": self.description,
            "is_answer_equivalent": self.is_answer_equivalent,
        }


class TreatmentGroupDesigner:
    """
    P4-2：无提示/H0/H1/H2四组处理定义。

    P4-2.1：定义四组处理
    P4-2.2：使用Phase 3设计的H0/H1/H2激活包
    P4-2.3：验证H0/H1/H2不含答案等价内容
    """

    def __init__(self):
        self._definitions = self._build_definitions()

    def _build_definitions(self) -> Dict[TreatmentGroup, TreatmentDefinition]:
        """构建四组处理定义"""
        return {
            TreatmentGroup.CONTROL: TreatmentDefinition(
                group=TreatmentGroup.CONTROL,
                hint_text=RAMSEY_HINT_TEXTS[TreatmentGroup.CONTROL],
                description="无提示——对照组",
                is_answer_equivalent=False,
            ),
            TreatmentGroup.H0: TreatmentDefinition(
                group=TreatmentGroup.H0,
                hint_text=RAMSEY_HINT_TEXTS[TreatmentGroup.H0],
                description="元检查——一个检查问题（128号§3.2 Hint-0）",
                is_answer_equivalent=False,
            ),
            TreatmentGroup.H1: TreatmentDefinition(
                group=TreatmentGroup.H1,
                hint_text=RAMSEY_HINT_TEXTS[TreatmentGroup.H1],
                description="思维操作——一个研究操作（128号§3.2 Hint-1）",
                is_answer_equivalent=False,
            ),
            TreatmentGroup.H2: TreatmentDefinition(
                group=TreatmentGroup.H2,
                hint_text=RAMSEY_HINT_TEXTS[TreatmentGroup.H2],
                description="概念/工具候选（128号§3.2 Hint-2）",
                is_answer_equivalent=False,
            ),
        }

    def get_all_groups(self) -> List[TreatmentDefinition]:
        """P4-2.COMP：4组全部定义"""
        return list(self._definitions.values())

    def get_definition(self, group: TreatmentGroup) -> TreatmentDefinition:
        return self._definitions[group]

    def verify_no_answer_equivalent(self) -> Dict[str, Any]:
        """
        P4-2.3：验证H0/H1/H2不含答案等价内容。

        边界情况：H0/H1/H2包含答案等价内容（应被拒绝）

        检查方法：对照128号§3.2禁止的答案等价内容。
        """
        violations = []
        for group, defn in self._definitions.items():
            if group == TreatmentGroup.CONTROL:
                continue
            if FORBIDDEN_ANSWER_EQUIVALENT in defn.hint_text:
                violations.append({
                    "group": group.value,
                    "hint_text": defn.hint_text,
                    "forbidden_content": FORBIDDEN_ANSWER_EQUIVALENT,
                })
                defn.is_answer_equivalent = True

        return {
            "all_clear": len(violations) == 0,
            "violations": violations,
            "checked_groups": [g.value for g in self._definitions if g != TreatmentGroup.CONTROL],
            "forbidden_reference": FORBIDDEN_ANSWER_EQUIVALENT,
        }

    def build_prompt(self, group: TreatmentGroup, task_prompt: str) -> str:
        """
        为指定处理组构建完整prompt。

        Args:
            group: 处理组
            task_prompt: 任务prompt（Q_0相关）

        Returns:
            完整prompt（含Hint文本，如果是control则不含Hint）
        """
        defn = self._definitions[group]
        if group == TreatmentGroup.CONTROL:
            return task_prompt
        else:
            hint_prefix = f"[提示] {defn.hint_text}\n\n"
            return hint_prefix + task_prompt
