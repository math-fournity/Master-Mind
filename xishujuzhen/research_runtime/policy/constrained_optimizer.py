"""
受约束多目标策略（261号§4.4）。

按261号§4.4的实现路径，对每条候选规则计算四个约束值，
选Pareto最优的动作（进展高/泄漏低/依赖低/成本低）。

四个约束：
1. 进展估计：Pattern自带义务ID标签——RHS标注"解决O_t中的哪个义务"，
   constrained-policy只做义务ID匹配（不需要理解数学内容）。
2. 泄漏估计：从Level和非特定性计算
   （Level越低 + 非特定性越低 = 泄漏风险越高）。
3. 依赖估计：Q只依赖已有稳定性方程（简化为1或0）。
4. 成本估计：1轮交互（固定值）。

ABSTAIN是合法选择：如果所有候选泄漏风险都>0.5，则放弃。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

from ..hgraph.hgraph_store import HeuristicRule
from ..parser.models import SixTuple


# ---------------------------------------------------------------------------
# 数据结构
# ---------------------------------------------------------------------------

@dataclass
class MatchedRule:
    """
    检索管线产出的匹配规则（261号§4.3）。

    pattern-matching / retrieval-pipeline 模块的输出单位：
    - rule：匹配到的HeuristicRule
    - match_score：图模式匹配分数（0-1）
    """
    rule: HeuristicRule
    match_score: float = 0.0

    def to_dict(self) -> dict:
        return {
            "rule": self.rule.to_dict(),
            "match_score": self.match_score,
        }


@dataclass
class ConstraintValues:
    """
    单条候选规则的四个约束值（261号§4.4）。

    - progress：进展估计（0-1，越高越好）
    - leakage：泄漏估计（0-1，越低越好）
    - dependency：依赖估计（0或1，越低越好）
    - cost：成本估计（固定1.0，越低越好）
    """
    progress: float = 0.0
    leakage: float = 0.0
    dependency: float = 0.0
    cost: float = 1.0

    def to_dict(self) -> dict:
        return {
            "progress": self.progress,
            "leakage": self.leakage,
            "dependency": self.dependency,
            "cost": self.cost,
        }


@dataclass
class SelectionResult:
    """
    策略选择结果（261号§4.4）。

    - selected_rule：选中的规则（ABSTAIN时为None）
    - reason：选择理由（人话描述）
    - constraint_values：每条候选规则的约束值，rule_id -> ConstraintValues
    - is_abstain：是否放弃（所有候选泄漏风险都>0.5）
    """
    selected_rule: Optional[HeuristicRule] = None
    reason: str = ""
    constraint_values: Dict[str, ConstraintValues] = field(default_factory=dict)
    is_abstain: bool = False

    def to_dict(self) -> dict:
        return {
            "selected_rule": self.selected_rule.to_dict() if self.selected_rule else None,
            "reason": self.reason,
            "constraint_values": {k: v.to_dict() for k, v in self.constraint_values.items()},
            "is_abstain": self.is_abstain,
        }


# ---------------------------------------------------------------------------
# 受约束策略
# ---------------------------------------------------------------------------

# 包含特定知识的关键词——出现这些词的规则泄漏风险额外+0.5（261号§4.4）
_SPECIFIC_KNOWLEDGE_KEYWORDS: List[str] = [
    "badly approximable",
    "连分数",
    "部分商有界",
    "二次无理数",
]

# 泄漏风险阈值——超过此值视为高泄漏，ABSTAIN触发
_LEAKAGE_ABSTAIN_THRESHOLD = 0.5

# 特定知识泄漏加成
_SPECIFIC_KNOWLEDGE_BONUS = 0.5


def leakage_risk(rule: HeuristicRule) -> float:
    """
    泄漏风险计算（261号§4.4，模块级共享函数）。

    leakage_risk = (1 - level) * (1 - non_specificity)
    Level越低（越接近知识注入）+ 非特定性越低 → 泄漏风险越高。

    对包含特定知识关键词的规则（如"badly approximable"），leakage额外+0.5。

    示例：
    - Q9: Level=0.2, 非特定性=0.9 → base = 0.8*0.1 = 0.08，
      但Q9包含特定知识"badly approximable" → 0.08 + 0.5 = 0.58
    - Q8: Level=0.5, 非特定性=0.7 → 0.5*0.3 = 0.15
    """
    base = (1.0 - rule.level) * (1.0 - rule.non_specificity)
    if _contains_specific_knowledge(rule):
        base += _SPECIFIC_KNOWLEDGE_BONUS
    return base


def _contains_specific_knowledge(rule: HeuristicRule) -> bool:
    """检查规则的rhs/guard/obligation_id是否包含特定知识关键词。"""
    text = f"{rule.rhs} {' '.join(rule.guard)} {rule.obligation_id}".lower()
    return any(kw.lower() in text for kw in _SPECIFIC_KNOWLEDGE_KEYWORDS)


class ConstrainedPolicy:
    """
    受约束多目标策略（261号§4.4）。

    对每条候选规则计算四个约束值（进展/泄漏/依赖/成本），
    选Pareto最优的动作。ABSTAIN是合法选择。
    """

    def estimate_progress(self, rule: HeuristicRule, six_tuple: SixTuple) -> float:
        """
        进展估计（261号§4.4）。

        从rule.obligation_id获取标注的义务，
        检查six_tuple.O_t中是否有匹配的open义务。
        匹配成功 → 进展潜力高（1.0）；匹配失败 → 进展潜力低（0.0）。
        不需要理解数学内容，只做义务ID匹配。
        """
        if not rule.obligation_id:
            return 0.0
        for obligation in six_tuple.O_t:
            if obligation.status not in ("open", "in_progress"):
                continue
            if _obligation_matches(rule.obligation_id, obligation.description):
                return 1.0
        return 0.0

    def estimate_leakage(self, rule: HeuristicRule) -> float:
        """
        泄漏估计（261号§4.4）。

        leakage_risk = (1 - level) * (1 - non_specificity)
        Level越低 + 非特定性越低 → 泄漏风险越高。
        对包含特定知识关键词的规则，leakage额外+0.5。
        """
        return leakage_risk(rule)

    def estimate_dependency(self, rule: HeuristicRule, six_tuple: SixTuple) -> float:
        """
        依赖估计（261号§4.4）。

        Q只依赖已有稳定性方程（简化为1或0）。
        若当前六元组已有表示形式（R_t非空，说明稳定性方程等已建立），
        则依赖已满足 → 0.0；否则 → 1.0。
        """
        # 已有表示形式 → 依赖已满足
        if six_tuple.R_t:
            return 0.0
        return 1.0

    def estimate_cost(self, rule: HeuristicRule) -> float:
        """
        成本估计（261号§4.4）。

        1轮交互（固定值1.0）。
        """
        return 1.0

    def select(self, matched_rules: List[MatchedRule], six_tuple: SixTuple) -> SelectionResult:
        """
        Pareto最优选择（261号§4.4）。

        对每条候选规则计算四个约束值，
        选Pareto最优的动作（进展高/泄漏低/依赖低/成本低）。
        ABSTAIN是合法选择（如果所有候选泄漏风险都>0.5）。
        """
        if not matched_rules:
            return SelectionResult(
                selected_rule=None,
                reason="无候选规则，放弃",
                is_abstain=True,
            )

        # 计算每条候选的四个约束值
        constraint_values: Dict[str, ConstraintValues] = {}
        for matched in matched_rules:
            rule = matched.rule
            constraint_values[rule.rule_id] = ConstraintValues(
                progress=self.estimate_progress(rule, six_tuple),
                leakage=self.estimate_leakage(rule),
                dependency=self.estimate_dependency(rule, six_tuple),
                cost=self.estimate_cost(rule),
            )

        # ABSTAIN：所有候选泄漏风险都>0.5
        all_high_leakage = all(
            constraint_values[m.rule.rule_id].leakage > _LEAKAGE_ABSTAIN_THRESHOLD
            for m in matched_rules
        )
        if all_high_leakage:
            return SelectionResult(
                selected_rule=None,
                reason="所有候选规则泄漏风险都>0.5，放弃以避免知识泄漏",
                constraint_values=constraint_values,
                is_abstain=True,
            )

        # Pareto最优选择
        pareto_set = self._pareto_front(matched_rules, constraint_values)

        # 在Pareto前沿中选进展最高的（同前沿时优先进展）
        best = max(pareto_set, key=lambda m: constraint_values[m.rule.rule_id].progress)
        best_values = constraint_values[best.rule.rule_id]
        reason = (
            f"选中{best.rule.rule_id}：Pareto最优"
            f"（进展={best_values.progress:.2f}, 泄漏={best_values.leakage:.2f},"
            f" 依赖={best_values.dependency:.2f}, 成本={best_values.cost:.2f}）"
        )
        return SelectionResult(
            selected_rule=best.rule,
            reason=reason,
            constraint_values=constraint_values,
            is_abstain=False,
        )

    @staticmethod
    def _pareto_front(
        matched_rules: List[MatchedRule],
        constraint_values: Dict[str, ConstraintValues],
    ) -> List[MatchedRule]:
        """
        计算Pareto前沿。

        目标：最大化progress，最小化leakage/dependency/cost。
        规则A被规则B支配当且仅当B在所有目标上不劣于A且至少一个目标严格更优。
        Pareto前沿 = 不被任何其他规则支配的规则集合。
        """
        front: List[MatchedRule] = []
        for a in matched_rules:
            va = constraint_values[a.rule.rule_id]
            dominated = False
            for b in matched_rules:
                if b is a:
                    continue
                vb = constraint_values[b.rule.rule_id]
                if _dominates(vb, va):
                    dominated = True
                    break
            if not dominated:
                front.append(a)
        return front


def _dominates(b: ConstraintValues, a: ConstraintValues) -> bool:
    """
    判断约束值b是否支配a（261号§4.4 Pareto定义）。

    目标：最大化progress，最小化leakage/dependency/cost。
    b支配a ⟺ b在所有目标上不劣于a，且至少一个目标严格更优。
    """
    # b在所有目标上不劣于a
    if not (b.progress >= a.progress
            and b.leakage <= a.leakage
            and b.dependency <= a.dependency
            and b.cost <= a.cost):
        return False
    # 至少一个目标严格更优
    return (b.progress > a.progress
            or b.leakage < a.leakage
            or b.dependency < a.dependency
            or b.cost < a.cost)


def _normalize_obligation(text: str) -> str:
    """
    归一化义务描述用于匹配（261号§4.4）。

    去掉常见语法助词（的/了/等）和空白，转小写，
    使"用数论性质估计D下界"与"估计D的下界"能匹配。
    """
    text = text.strip().lower()
    for ch in ("的", "了", " ", "\t", "。", "，", "、", "|", "·", "=", "—", "-"):
        text = text.replace(ch, "")
    return text


def _obligation_matches(rule_obligation: str, open_obligation: str) -> bool:
    """
    义务ID匹配（261号§4.4）。

    不需要理解数学内容，只做归一化后的字符串匹配（双向子串包含）。
    例如 rule_obligation="估计D的下界" 匹配 open_obligation="估计D的下界"；
    rule_obligation="用数论性质估计D下界" 匹配 open_obligation="估计D的下界"
    （归一化后"估计d下界"是"用数论性质估计d下界"的子串）。
    """
    r = _normalize_obligation(rule_obligation)
    o = _normalize_obligation(open_obligation)
    if not r or not o:
        return False
    return r in o or o in r
