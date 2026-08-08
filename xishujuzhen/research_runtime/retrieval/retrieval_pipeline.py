"""
检索管线模块（258号§3.2步骤⑧ + 261号实现路径）。

三级递进检索：种子选择 → 图遍历 → 预算剪枝。
整合activation-score和pattern-matching，完成从ParseResult到top-K匹配规则的完整检索流程。
"""

from typing import List

from ..parser.models import ParseResult, TrajectoryNode
from ..hgraph.hgraph_store import HeuristicRule, HeuristicRuleGraph
from ..activation.score_calculator import ActivationScoreCalculator, ScoredRule
from ..matching.pattern_matcher import PatternMatcher, MatchedRule
from ..budget.budget_manager import BudgetManager, BudgetType


class RetrievalPipeline:
    """
    检索管线（258号§3.2步骤⑧ + 261号实现路径）。

    三级递进检索：
    1. 种子选择：从T_t的前沿节点出发，选择前沿节点的数学对象作为种子
    2. 图遍历：用activation-score计算候选，用pattern-matching做精排
    3. 预算剪枝：按匹配分数降序，截断到预算允许的数量

    整合ActivationScoreCalculator和PatternMatcher。
    """

    def __init__(
        self,
        score_calculator: ActivationScoreCalculator = None,
        pattern_matcher: PatternMatcher = None,
    ) -> None:
        self.score_calculator = score_calculator or ActivationScoreCalculator()
        self.pattern_matcher = pattern_matcher or PatternMatcher()

    def select_seeds(self, parse_result: ParseResult) -> List[str]:
        """
        种子选择：从T_t的前沿节点出发（258号§3.2步骤⑧）。

        选择前沿节点（is_frontier=True）的数学对象名称作为种子。
        如果没有前沿节点，取最后一个节点的数学对象。

        Args:
            parse_result: 解析器输出

        Returns:
            种子列表（数学对象名称）
        """
        seeds: List[str] = []

        # 找前沿节点
        frontier_nodes = [
            n for n in parse_result.trajectory_nodes if n.is_frontier
        ]

        # 如果没有前沿节点，取最后一个节点
        target_nodes = frontier_nodes if frontier_nodes else (
            parse_result.trajectory_nodes[-1:]
            if parse_result.trajectory_nodes else []
        )

        for node in target_nodes:
            for mo in node.math_objects:
                if mo.name and mo.name not in seeds:
                    seeds.append(mo.name)

        return seeds

    def traverse(
        self,
        seeds: List[str],
        rules: List[HeuristicRule],
        parse_result: ParseResult,
    ) -> List[MatchedRule]:
        """
        图遍历：用activation-score计算候选，用pattern-matching做精排（261号实现路径）。

        Args:
            seeds: 种子列表（当前未直接用于过滤，保留接口供后续图遍历扩展）
            rules: 候选规则列表
            parse_result: 解析器输出

        Returns:
            匹配的规则列表（MatchedRule）
        """
        # 第一级：activation-score粗筛（取top-K候选）
        scored_rules: List[ScoredRule] = self.score_calculator.calculate(
            parse_result, rules, top_k=len(rules),
        )

        # 第二级：pattern-matching精排
        matched_rules: List[MatchedRule] = self.pattern_matcher.match(
            parse_result, scored_rules,
        )

        return matched_rules

    def prune(
        self,
        matched_rules: List[MatchedRule],
        top_k: int = 5,
    ) -> List[MatchedRule]:
        """
        预算剪枝：按匹配分数降序，截断到预算允许的数量（258号§3.2步骤⑧）。

        过滤掉match_score=0.0的规则（完全不匹配），
        然后按match_score降序排列，截断到top_k。

        Args:
            matched_rules: 匹配的规则列表
            top_k: 预算允许的返回数量上限

        Returns:
            剪枝后的规则列表（≤top_k条）
        """
        # 过滤掉完全不匹配的规则
        filtered = [r for r in matched_rules if r.match_score > 0.0]

        # 按匹配分数降序排列
        filtered.sort(key=lambda x: x.match_score, reverse=True)

        # 截断到top_k
        return filtered[:top_k]

    def retrieve(
        self,
        parse_result: ParseResult,
        hgraph: HeuristicRuleGraph,
        top_k: int = 5,
    ) -> List[MatchedRule]:
        """
        主方法：完整检索流程（258号§3.2步骤⑧ + 261号实现路径）。

        三级递进：
        1. 种子选择 → select_seeds
        2. 图遍历（activation-score + pattern-matching）→ traverse
        3. 预算剪枝 → prune

        Args:
            parse_result: 解析器输出
            hgraph: H图存储（启发规则图）
            top_k: 返回的匹配规则数量上限

        Returns:
            top-K匹配规则列表（MatchedRule）
        """
        # 获取published规则
        rules = hgraph.get_published_rules()

        # 第一级：种子选择
        seeds = self.select_seeds(parse_result)

        # 第二级：图遍历（activation-score + pattern-matching）
        matched_rules = self.traverse(seeds, rules, parse_result)

        # 第三级：预算剪枝
        return self.prune(matched_rules, top_k=top_k)
