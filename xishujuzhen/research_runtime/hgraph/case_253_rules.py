"""
253号10个Q的规则初始化（261号§4.1 + 253号§2.3）。

从253号文档提取Q1-Q10的Level和非特定性，
从253号§2.3的QA序列和260号§4.1的A1-A10解析目标定义LHS图模式，
为Q1-Q10创建10条HeuristicRule，全部初始化为published状态。
"""

from typing import List
from .hgraph_store import HeuristicRule, HeuristicRuleGraph


# 253号Q1-Q10的Level和非特定性（从253号文档提取）
_Q_LEVELS = {
    "Q1": 1.0, "Q2": 1.0, "Q3": 1.0, "Q4": 1.0, "Q5": 1.0,
    "Q6": 0.7, "Q7": 0.8, "Q8": 0.5, "Q9": 0.2, "Q10": 0.6,
}

_Q_NON_SPECIFICITY = {
    "Q1": 0.9, "Q2": 0.9, "Q3": 0.9, "Q4": 0.9, "Q5": 0.9,
    "Q6": 0.8, "Q7": 0.4, "Q8": 0.7, "Q9": 0.9, "Q10": 0.7,
}

# 每个Q的LHS定义（图模式）：node_types + 特征描述
_Q_LHS = {
    "Q1":  {"node_types": ["observation"],                              "feature": "题目结构分析"},
    "Q2":  {"node_types": ["observation", "candidate"],                 "feature": "列出所有方向"},
    "Q3":  {"node_types": ["candidate", "subgoal"],                     "feature": "选择方向并描述第一步"},
    "Q4":  {"node_types": ["subgoal", "representation", "resolution"],  "feature": "做紧性归约"},
    "Q5":  {"node_types": ["resolution", "stall"],                      "feature": "紧性归约完成但缺定量下界"},
    "Q6":  {"node_types": ["stall", "representation", "resolution"],    "feature": "投影到根并展开"},
    "Q7":  {"node_types": ["representation", "resolution"],             "feature": "组合矩条件和展开式"},
    "Q8":  {"node_types": ["resolution"],                               "feature": "稳定性方程中有量取决于整数关系"},
    "Q9":  {"node_types": ["claim", "stall"],                           "feature": "D≠0但下界未知"},
    "Q10": {"node_types": ["resolution"],                               "feature": "有偏差能量下界需要传递到极差"},
}

# 每个Q的guard（额外约束条件）
_Q_GUARDS = {
    "Q1": [], "Q2": [], "Q3": [], "Q4": [], "Q5": [],
    "Q6": [], "Q7": [],
    "Q8": ["D取决于整数k和n的关系"],
    "Q9": ["U_t中有knowledge_gap"],
    "Q10": ["Σe²≥c/n已知"],
}

# 每个Q的RHS提示文本（Q的内容）
_Q_RHS = {
    "Q1":  "Q1: 你观察到了什么？题目的结构是什么？",
    "Q2":  "Q2: 你能列出所有可能的方向吗？",
    "Q3":  "Q3: 你选择哪个方向？第一步是什么？",
    "Q4":  "Q4: 你能做紧性归约吗？",
    "Q5":  "Q5: 紧性归约完成了，但定量下界是什么？差距在哪里？",
    "Q6":  "Q6: 你能投影到根并展开吗？",
    "Q7":  "Q7: 你能组合矩条件和展开式吗？",
    "Q8":  "Q8: 稳定性方程中有量取决于整数关系，你能估计D的下界吗？",
    "Q9":  "Q9: p=(5-√5)/10是二次无理数，它的连分数部分商有界，因此是badly approximable——存在c₀>0使|p-k/n|≥c₀/n²。你能用这个事实推出|D|的下界吗？",
    "Q10": "Q10: 有偏差能量下界，你能传递到极差吗？",
}

# 每个Q的RHS义务ID标注（"解决O_t中的哪个义务"）
_Q_OBLIGATION_IDS = {
    "Q1":  "理解题目结构",
    "Q2":  "列出所有方向",
    "Q3":  "选择方向",
    "Q4":  "做紧性归约",
    "Q5":  "识别差距",
    "Q6":  "投影到根",
    "Q7":  "组合矩条件",
    "Q8":  "估计D的下界",
    "Q9":  "用数论性质估计D下界",
    "Q10": "传递下界到极差",
}

_Q_IDS = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]


def build_case_253_rules() -> List[HeuristicRule]:
    """
    构建253号Q1-Q10的10条HeuristicRule。

    所有规则初始化为published状态。
    """
    rules: List[HeuristicRule] = []
    for qid in _Q_IDS:
        rule = HeuristicRule(
            rule_id=qid,
            lhs=dict(_Q_LHS[qid]),
            guard=list(_Q_GUARDS[qid]),
            rhs=_Q_RHS[qid],
            level=_Q_LEVELS[qid],
            non_specificity=_Q_NON_SPECIFICITY[qid],
            lifecycle_state="published",
            obligation_id=_Q_OBLIGATION_IDS[qid],
        )
        rules.append(rule)
    return rules


def init_case_253_graph(graph: HeuristicRuleGraph) -> HeuristicRuleGraph:
    """
    将253号Q1-Q10的10条规则装入给定的H图存储。

    返回传入的graph（已填充）。
    """
    for rule in build_case_253_rules():
        graph.add_rule(rule)
    return graph


def create_case_253_graph() -> HeuristicRuleGraph:
    """创建并返回已填充253号10条规则的H图存储。"""
    graph = HeuristicRuleGraph()
    return init_case_253_graph(graph)
