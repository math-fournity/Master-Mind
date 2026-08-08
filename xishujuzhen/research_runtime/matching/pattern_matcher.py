"""
模式匹配模块（261号§4.3）。

对activation-score筛出的top-K候选，逐一做LHS子图匹配+Guard条件检查。

近似匹配容差（261号§4.3）：
- 精确匹配：T_t的子图与LHS完全匹配 → 匹配分数1.0
- 近似匹配（1步偏差）：多或少1个节点类型 → 匹配分数0.8
- 近似匹配（2步偏差）：多或少2个节点类型 → 匹配分数0.6
- 超过2步偏差 → 不匹配（0.0）

附加规则：当对称差≥3但T_t与LHS的节点类型数量相同（类型完全不同），
给0.5分表示"同规模但类型不匹配"的部分匹配。
"""

from dataclasses import dataclass
from typing import List, Set

from ..parser.models import ParseResult, TrajectoryNode
from ..hgraph.hgraph_store import HeuristicRule
from ..activation.score_calculator import ScoredRule


# ---------------------------------------------------------------------------
# 数据结构
# ---------------------------------------------------------------------------

@dataclass
class MatchedRule:
    """带模式匹配结果的规则。"""
    rule_id: str
    match_score: float
    guard_passed: bool
    rule: HeuristicRule

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "match_score": self.match_score,
            "guard_passed": self.guard_passed,
            "rule": self.rule.to_dict(),
        }


# ---------------------------------------------------------------------------
# 模式匹配器
# ---------------------------------------------------------------------------

class PatternMatcher:
    """
    模式匹配器（261号§4.3）。

    对activation-score筛出的top-K候选，逐一做：
    1. LHS子图匹配：比较T_t节点类型集合与LHS要求的节点类型集合
    2. Guard条件检查：检查parse_result的六元组中是否满足所有guard条件
    """

    # 匹配分数映射（按对称差大小）
    _SCORE_MAP = {0: 1.0, 1: 0.8, 2: 0.6}

    def match_node_types(
        self,
        trajectory_nodes: List[TrajectoryNode],
        lhs_node_types: List[str],
    ) -> float:
        """
        LHS子图匹配：比较T_t节点类型集合与LHS要求的节点类型集合（261号§4.3）。

        计算集合差异（对称差），按差异大小确定匹配分数：
        - 对称差=0 → 1.0（精确匹配）
        - 对称差=1 → 0.8（1步偏差）
        - 对称差=2 → 0.6（2步偏差）
        - 对称差≥3 → 0.0（超过2步偏差）
          - 附加：若|T_t类型|=|LHS类型|（同规模不同类型）→ 0.5（部分匹配）

        Args:
            trajectory_nodes: T_t的节点列表
            lhs_node_types: LHS要求的节点类型列表

        Returns:
            匹配分数（0.0-1.0）
        """
        t_types: Set[str] = {n.type for n in trajectory_nodes}
        lhs_types: Set[str] = set(lhs_node_types)

        sym_diff = t_types.symmetric_difference(lhs_types)
        diff_size = len(sym_diff)

        # 按对称差大小查表
        if diff_size in self._SCORE_MAP:
            return self._SCORE_MAP[diff_size]

        # 对称差≥3
        if diff_size > 2:
            # 附加规则：同规模不同类型 → 0.5部分匹配
            if len(t_types) == len(lhs_types):
                return 0.5
            return 0.0

        return 0.0

    def check_guards(
        self,
        parse_result: ParseResult,
        guards: List[str],
    ) -> bool:
        """
        Guard条件检查：检查parse_result的六元组中是否满足所有guard条件（261号§4.3）。

        Guard示例：
        - "D取决于整数k和n的关系" → 检查U_t中是否有相关条目
        - "U_t中有knowledge_gap" → 检查U_t中是否有knowledge_gap标注
        - "Σe²≥c/n已知" → 检查V_t中是否有相关已验证命题

        Args:
            parse_result: 解析器输出
            guards: guard条件列表

        Returns:
            所有guard条件是否都满足
        """
        if not guards:
            # 无guard条件 → 自动通过
            return True

        six_tuple = parse_result.six_tuple

        for guard in guards:
            if not self._check_single_guard(guard, six_tuple):
                return False

        return True

    @staticmethod
    def _check_single_guard(guard: str, six_tuple) -> bool:
        """
        检查单个guard条件。

        根据guard内容在六元组的相应字段中查找匹配。
        """
        guard_lower = guard.lower()

        # Guard: "U_t中有knowledge_gap"
        if "knowledge_gap" in guard_lower or "知识" in guard:
            keywords = ["knowledge_gap", "知识", "瓶颈"]
            for u in six_tuple.U_t:
                for kw in keywords:
                    if kw in u.description:
                        return True
            return False

        # Guard: "D取决于整数k和n的关系"
        if "取决于整数" in guard:
            for u in six_tuple.U_t:
                if "取决于整数" in u.description or "整数关系" in u.description:
                    return True
            return False

        # Guard: "Σe²≥c/n已知" — 检查V_t中是否有相关已验证命题
        if "已知" in guard or "Σe" in guard:
            for v in six_tuple.V_t:
                if "e" in v.statement and ("n" in v.statement or "≥" in v.statement):
                    return True
            return False

        # 默认：在U_t和V_t中搜索guard关键词
        keywords = [w for w in guard.split() if len(w) > 1]
        if not keywords:
            return True

        for u in six_tuple.U_t:
            if any(kw in u.description for kw in keywords):
                return True
        for v in six_tuple.V_t:
            if any(kw in v.statement for kw in keywords):
                return True

        return False

    def match(
        self,
        parse_result: ParseResult,
        scored_rules: List[ScoredRule],
    ) -> List[MatchedRule]:
        """
        主方法：对每条候选规则做LHS匹配+Guard检查（261号§4.3）。

        Args:
            parse_result: 解析器输出
            scored_rules: activation-score筛出的候选规则列表

        Returns:
            MatchedRule列表（rule_id, match_score, guard_passed, rule）
        """
        matched_rules: List[MatchedRule] = []

        for scored in scored_rules:
            rule = scored.rule

            # LHS子图匹配
            lhs_node_types = rule.lhs.get("node_types", [])
            match_score = self.match_node_types(
                parse_result.trajectory_nodes,
                lhs_node_types,
            )

            # Guard条件检查
            guard_passed = self.check_guards(parse_result, rule.guard)

            matched_rules.append(MatchedRule(
                rule_id=rule.rule_id,
                match_score=match_score,
                guard_passed=guard_passed,
                rule=rule,
            ))

        return matched_rules
