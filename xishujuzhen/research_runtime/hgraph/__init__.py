"""
hgraph: 启发规则图（H图）存储模块（261号§4.1）。

内存存储启发规则，每条规则是 (lhs, guard, rhs) 三元组，
附带 Level、非特定性、生命周期状态、义务ID标注。

简化原型：内存字典存储，不连ArangoDB。
"""

from .hgraph_store import HeuristicRule, HeuristicRuleGraph
from .case_253_rules import (
    build_case_253_rules,
    init_case_253_graph,
    create_case_253_graph,
)
from .case_number_theory_rules import (
    build_case_number_theory_rules,
    init_case_number_theory_graph,
    create_case_number_theory_graph,
)
from .case_combinatorics_rules import (
    build_case_combinatorics_rules,
    init_case_combinatorics_graph,
    create_case_combinatorics_graph,
)

__all__ = [
    "HeuristicRule",
    "HeuristicRuleGraph",
    "build_case_253_rules",
    "init_case_253_graph",
    "create_case_253_graph",
    "build_case_number_theory_rules",
    "init_case_number_theory_graph",
    "create_case_number_theory_graph",
    "build_case_combinatorics_rules",
    "init_case_combinatorics_graph",
    "create_case_combinatorics_graph",
]
