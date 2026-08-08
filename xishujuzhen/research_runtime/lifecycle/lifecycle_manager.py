"""
生命周期管理模块（261号§4.6）。

管理模式的生命周期状态转移：
observed → candidate → intervened → validated → published → retired

转移条件定义：每个状态转移到下一状态需要满足的条件。
253号10个Q初始化为published。
"""

from enum import Enum
from typing import List, Optional, Dict

from ..hgraph.hgraph_store import HeuristicRuleGraph


class LifecycleState(str, Enum):
    """生命周期状态枚举（261号§4.6）。"""
    OBSERVED = "observed"        # 观察到模式
    CANDIDATE = "candidate"      # 提升为候选模式
    INTERVENED = "intervened"    # 已介入干预
    VALIDATED = "validated"      # 已验证有效
    PUBLISHED = "published"      # 已发布，可被检索
    RETIRED = "retired"          # 已退役


# 合法的状态转移路径（线性链 + 允许跳转到published）
_TRANSITIONS: Dict[str, List[str]] = {
    "observed":   ["candidate"],
    "candidate":  ["intervened"],
    "intervened": ["validated"],
    "validated":  ["published"],
    "published":  ["retired"],
    "retired":    [],            # 终态
}

# 每个转移需要满足的条件描述（简化原型：仅描述，不做实质校验逻辑）
_TRANSITION_CONDITIONS: Dict[str, str] = {
    "observed->candidate":   "模式被多次观察到，提取为候选",
    "candidate->intervened": "候选模式被选择用于介入干预",
    "intervened->validated": "介入后验证模式有效",
    "validated->published":  "验证通过，发布供检索",
    "published->retired":    "模式失效或被替代，退役",
}


class LifecycleManager:
    """
    生命周期管理器（261号§4.6）。

    管理H图中规则的生命周期状态转移。
    依赖HeuristicRuleGraph做实际的状态存储。
    """

    def __init__(self, graph: Optional[HeuristicRuleGraph] = None) -> None:
        self.graph = graph if graph is not None else HeuristicRuleGraph()

    @staticmethod
    def valid_states() -> List[str]:
        """所有合法状态。"""
        return [s.value for s in LifecycleState]

    @staticmethod
    def can_transition(rule_id: str, from_state: str, to_state: str) -> bool:
        """
        判断从 from_state 到 to_state 的转移是否合法。

        注意：rule_id参数保留以备未来扩展（如基于规则历史的条件校验），
        当前简化原型只做状态链合法性校验。
        """
        allowed = _TRANSITIONS.get(from_state, [])
        return to_state in allowed

    def transition(self, rule_id: str, to_state: str) -> bool:
        """
        执行状态转移。

        校验当前状态到目标状态的转移是否合法，合法则更新H图中的规则状态。
        返回是否转移成功。
        """
        rule = self.graph.get_rule(rule_id)
        if rule is None:
            return False
        from_state = rule.lifecycle_state
        if not self.can_transition(rule_id, from_state, to_state):
            return False
        return self.graph.update_lifecycle(rule_id, to_state)

    def is_publishable(self, rule_id: str) -> bool:
        """
        判断规则是否可发布（published状态可被检索）。

        published状态 = 可被检索引擎检索。
        """
        rule = self.graph.get_rule(rule_id)
        if rule is None:
            return False
        return rule.lifecycle_state == LifecycleState.PUBLISHED.value

    def get_publishable_rules(self) -> List:
        """获取所有可发布（published）的规则。"""
        return self.graph.get_published_rules()

    @staticmethod
    def transition_condition(from_state: str, to_state: str) -> Optional[str]:
        """获取转移条件的描述。"""
        return _TRANSITION_CONDITIONS.get(f"{from_state}->{to_state}")
