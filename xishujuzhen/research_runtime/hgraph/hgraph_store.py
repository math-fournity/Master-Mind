"""
H图存储模块（261号§4.1）。

启发规则图（Heuristic Rule Graph）的内存存储。
每条规则是 (lhs, guard, rhs) 三元组，附带 Level、非特定性、生命周期状态、义务ID标注。

简化原型：用内存字典存储，不连ArangoDB。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class HeuristicRule:
    """
    单条启发规则（261号§4.1）。

    字段：
    - rule_id：规则唯一标识（如 "Q1"）
    - lhs：图模式描述（dict，包含 node_types 和 edge_types 列表，以及特征描述）
    - guard：额外约束条件列表（如 "D取决于整数k和n的关系"）
    - rhs：提示文本（Q的内容）+ 义务ID标注（"解决O_t中的哪个义务"）
    - level：Level值（0-1），越高越接近元层级
    - non_specificity：非特定性程度（0-1），越高越不指向具体计算
    - lifecycle_state：生命周期状态（observed/candidate/intervened/validated/published/retired）
    - obligation_id：RHS标注的义务ID（"解决O_t中的哪个义务"）
    """
    rule_id: str
    lhs: Dict = field(default_factory=dict)        # {"node_types": [...], "edge_types": [...], "feature": "..."}
    guard: List[str] = field(default_factory=list)
    rhs: str = ""                                  # 提示文本
    level: float = 0.0
    non_specificity: float = 0.0
    lifecycle_state: str = "observed"
    obligation_id: str = ""                        # RHS标注的义务ID

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "lhs": dict(self.lhs),
            "guard": list(self.guard),
            "rhs": self.rhs,
            "level": self.level,
            "non_specificity": self.non_specificity,
            "lifecycle_state": self.lifecycle_state,
            "obligation_id": self.obligation_id,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "HeuristicRule":
        return cls(
            rule_id=d["rule_id"],
            lhs=dict(d.get("lhs", {})),
            guard=list(d.get("guard", [])),
            rhs=d.get("rhs", ""),
            level=d.get("level", 0.0),
            non_specificity=d.get("non_specificity", 0.0),
            lifecycle_state=d.get("lifecycle_state", "observed"),
            obligation_id=d.get("obligation_id", ""),
        )


class HeuristicRuleGraph:
    """
    H图存储（261号§4.1）。

    内存字典存储，rule_id -> HeuristicRule。
    简化原型，不连ArangoDB。
    """

    def __init__(self) -> None:
        self._rules: Dict[str, HeuristicRule] = {}

    def add_rule(self, rule: HeuristicRule) -> None:
        """添加一条规则。若rule_id已存在则覆盖。"""
        self._rules[rule.rule_id] = rule

    def get_rule(self, rule_id: str) -> Optional[HeuristicRule]:
        """获取单条规则，不存在返回None。"""
        return self._rules.get(rule_id)

    def get_published_rules(self) -> List[HeuristicRule]:
        """获取所有published状态的规则（可被检索的规则）。"""
        return [r for r in self._rules.values() if r.lifecycle_state == "published"]

    def get_all_rules(self) -> List[HeuristicRule]:
        """获取所有规则。"""
        return list(self._rules.values())

    def update_lifecycle(self, rule_id: str, new_state: str) -> bool:
        """
        更新规则的生命周期状态。

        返回是否更新成功（rule_id不存在返回False）。
        注意：本方法不做状态转移合法性校验，校验由LifecycleManager负责。
        """
        rule = self._rules.get(rule_id)
        if rule is None:
            return False
        rule.lifecycle_state = new_state
        return True

    def __len__(self) -> int:
        return len(self._rules)

    def __contains__(self, rule_id: str) -> bool:
        return rule_id in self._rules
