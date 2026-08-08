"""
数论案例6个Q的规则初始化（泛化验证用）。

案例：证明任意正整数n，存在无穷多个素数p使得p ≡ 1 (mod n)。
领域：数论。推理过程涉及反证法、构造法、分圆多项式、元素阶。

从case_number_theory.py的QA序列提取Q1-Q6的Level和非特定性，
根据每轮A_i后的T_t节点类型和六元组状态定义LHS图模式，
为Q1-Q6创建6条HeuristicRule，全部初始化为published状态。

泛化验证目标：A3后应触发Q4（引导者问"改用分圆多项式Φ_n(A)呢？"）。
A3状态：stall节点（阶可能是真因子），U_t有"阶可能是n的真因子"，
O_t有"保证ord_q(A) = n（排除真因子）"（open）。
"""

from typing import List
from .hgraph_store import HeuristicRule, HeuristicRuleGraph


# 数论案例Q1-Q6的Level和非特定性（从QA_SEQUENCE提取）
_Q_LEVELS = {
    "Q1": 1.0, "Q2": 0.7, "Q3": 0.5,
    "Q4": 0.3, "Q5": 0.5, "Q6": 0.6,
}

_Q_NON_SPECIFICITY = {
    "Q1": 0.1, "Q2": 0.5, "Q3": 0.7,
    "Q4": 0.8, "Q5": 0.6, "Q6": 0.4,
}

# 每个Q的LHS定义（图模式）：node_types + 特征描述
# 特征描述包含泛化关键词，用于activation-score权重标定
_Q_LHS = {
    "Q1": {"node_types": ["observation"],
           "feature": "存在无穷多个型命题——素数无穷结构分析"},
    "Q2": {"node_types": ["observation", "candidate"],
           "feature": "反证法构造——假设有限个素数"},
    "Q3": {"node_types": ["representation", "resolution", "stall"],
           "feature": "构造N的素因子不保证≡1(mod n)——需要阶的关系"},
    "Q4": {"node_types": ["stall", "representation", "resolution"],
           "feature": "阶可能是真因子——用分圆多项式排除真因子"},
    "Q5": {"node_types": ["resolution"],
           "feature": "确认分圆多项式构造有效性——有素因子且q是新的"},
    "Q6": {"node_types": ["resolution"],
           "feature": "组织完整证明——逻辑闭环确认"},
}

# 每个Q的guard（额外约束条件）
_Q_GUARDS = {
    "Q1": [],
    "Q2": [],
    "Q3": ["构造N的素因子不保证"],
    "Q4": ["阶可能是n的真因子"],
    "Q5": ["ord_q(A) = n已知"],
    "Q6": [],
}

# 每个Q的RHS提示文本（Q的内容）
_Q_RHS = {
    "Q1": "Q1: 你观察到了什么？题目的结构是什么？结论是什么类型？",
    "Q2": "Q2: 反证法的话，假设只有有限个p≡1(mod n)的素数，你能构造新数使它有新素因子吗？",
    "Q3": "Q3: N的素因子q满足什么关系？考虑N mod q和阶的关系——q | N意味着什么？",
    "Q4": "Q4: 你用了A^n - 1。如果改用分圆多项式Φ_n(A)呢？Φ_n(A)的素因子q满足什么？",
    "Q5": "Q5: 现在你有了构造。但还需要确认：(1) Φ_n(A)有素因子q且q∤n；(2) q是新的。你能处理吗？",
    "Q6": "Q6: 把完整的证明组织一下，确认逻辑闭环。",
}

# 每个Q的RHS义务ID标注（"解决O_t中的哪个义务"）
_Q_OBLIGATION_IDS = {
    "Q1": "理解题目结构",
    "Q2": "构造使新素因子≡1(mod n)的数",
    "Q3": "构造使新素因子≡1(mod n)的数",
    "Q4": "排除真因子",
    "Q5": "确认Φ_n(A)有素因子且q是新的",
    "Q6": "组织完整证明确认逻辑闭环",
}

_Q_IDS = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]


def build_case_number_theory_rules() -> List[HeuristicRule]:
    """
    构建数论案例Q1-Q6的6条HeuristicRule。

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


def init_case_number_theory_graph(graph: HeuristicRuleGraph) -> HeuristicRuleGraph:
    """
    将数论案例Q1-Q6的6条规则装入给定的H图存储。

    返回传入的graph（已填充）。
    """
    for rule in build_case_number_theory_rules():
        graph.add_rule(rule)
    return graph


def create_case_number_theory_graph() -> HeuristicRuleGraph:
    """创建并返回已填充数论案例6条规则的H图存储。"""
    graph = HeuristicRuleGraph()
    return init_case_number_theory_graph(graph)
