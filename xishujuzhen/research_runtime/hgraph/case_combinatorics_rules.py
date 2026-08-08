"""
组合/概率案例6个Q的规则初始化（泛化验证用）。

案例：n人围坐猜帽子颜色策略题，求最优策略使成功概率最大。
领域：组合/概率。推理过程涉及策略设计、概率分析、Hamming码类比、信息论。

从case_combinatorics.py的QA序列提取Q1-Q6的Level和非特定性，
根据每轮A_i后的T_t节点类型和六元组状态定义LHS图模式，
为Q1-Q6创建6条HeuristicRule，全部初始化为published状态。

泛化验证目标：A3后应触发Q4（引导者问"理清Hamming码策略的逻辑"）。
A3状态：stall节点（策略逻辑需要理清），U_t有"Hamming码策略逻辑需要理清"，
O_t有"理清Hamming码策略的猜/pass逻辑"（in_progress）。
"""

from typing import List
from .hgraph_store import HeuristicRule, HeuristicRuleGraph


# 组合案例Q1-Q6的Level和非特定性（从QA_SEQUENCE提取）
_Q_LEVELS = {
    "Q1": 1.0, "Q2": 0.5, "Q3": 0.4,
    "Q4": 0.4, "Q5": 0.3, "Q6": 0.5,
}

_Q_NON_SPECIFICITY = {
    "Q1": 0.1, "Q2": 0.6, "Q3": 0.7,
    "Q4": 0.6, "Q5": 0.8, "Q6": 0.5,
}

# 每个Q的LHS定义（图模式）：node_types + 特征描述
# 特征描述包含泛化关键词，用于activation-score权重标定
_Q_LHS = {
    "Q1": {"node_types": ["observation"],
           "feature": "博弈策略优化问题——最大化成功概率结构分析"},
    "Q2": {"node_types": ["representation", "resolution", "stall"],
           "feature": "奇偶性策略——约定S的值推断帽子颜色"},
    "Q3": {"node_types": ["representation", "candidate", "stall"],
           "feature": "Hamming码策略——n=2^m-1完美码覆盖半径1"},
    "Q4": {"node_types": ["representation", "candidate", "stall"],
           "feature": "理清Hamming码策略逻辑——猜/pass条件不明确"},
    "Q5": {"node_types": ["operation", "stall"],
           "feature": "反转Hamming码策略设计——码字pass非码字猜"},
    "Q6": {"node_types": ["resolution"],
           "feature": "推广k色策略——成功率1/k上界信息论"},
}

# 每个Q的guard（额外约束条件）
_Q_GUARDS = {
    "Q1": [],
    "Q2": ["1/2是否最优"],
    "Q3": ["Hamming码策略"],
    "Q4": ["Hamming码策略逻辑"],
    "Q5": ["方向反了"],
    "Q6": [],
}

# 每个Q的RHS提示文本（Q的内容）
_Q_RHS = {
    "Q1": "Q1: 你观察到了什么？题目的结构是什么？结论是什么类型？",
    "Q2": "Q2: 先看k=2的简单情况。n个人，每人看到其他人的帽子。你能设计什么策略？考虑奇偶性。",
    "Q3": "Q3: 你得到了1/2。能否超过1/2？考虑Hamming码的思路——n=2^m-1时有什么特殊结构？",
    "Q4": "Q4: 理清Hamming码策略的逻辑。关键问题：(a)当c是码字时各人行为？(b)当c不是码字时各人行为？(c)成功条件何时满足？",
    "Q5": "Q5: 你发现1/(n+1)太差。反过来想：当c是码字时全员pass，当c不是码字时恰好一人猜对。重新设计策略。",
    "Q6": "Q6: 回到本质。关键洞察：约定一个S值，当观察到的S_{-i}与约定矛盾时pass，一致时猜。重新分析成功概率，并推广到k色。",
}

# 每个Q的RHS义务ID标注（"解决O_t中的哪个义务"）
_Q_OBLIGATION_IDS = {
    "Q1": "求最优策略及成功概率",
    "Q2": "k=2时能否超过1/2",
    "Q3": "超过1/2",
    "Q4": "理清Hamming码策略",
    "Q5": "设计正确的策略",
    "Q6": "推广到k色",
}

_Q_IDS = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]


def build_case_combinatorics_rules() -> List[HeuristicRule]:
    """
    构建组合/概率案例Q1-Q6的6条HeuristicRule。

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


def init_case_combinatorics_graph(graph: HeuristicRuleGraph) -> HeuristicRuleGraph:
    """
    将组合/概率案例Q1-Q6的6条规则装入给定的H图存储。

    返回传入的graph（已填充）。
    """
    for rule in build_case_combinatorics_rules():
        graph.add_rule(rule)
    return graph


def create_case_combinatorics_graph() -> HeuristicRuleGraph:
    """创建并返回已填充组合/概率案例6条规则的H图存储。"""
    graph = HeuristicRuleGraph()
    return init_case_combinatorics_graph(graph)
