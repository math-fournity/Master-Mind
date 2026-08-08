"""
激活分数计算模块（261号§4.2）。

从ParseResult提取7维特征向量p_t，用权重矩阵W计算稀疏激活分数 a_t = W^T · p_t，
取top-K候选规则。

7种数值维度（261号§4.2）：
0. stability_equation_presence  — 稳定性方程存在度
1. integer_dependency            — 整数依赖度
2. lower_bound_demand            — 下界需求度
3. knowledge_gap                 — 知识缺口度
4. reasoning_depth               — 推理深度
5. representation_richness       — 表示丰富度
6. stall_severity                — 卡点严重度
"""

from dataclasses import dataclass
from typing import List

import numpy as np

from ..parser.models import ParseResult, TrajectoryNode
from ..hgraph.hgraph_store import HeuristicRule


# ---------------------------------------------------------------------------
# 数据结构
# ---------------------------------------------------------------------------

@dataclass
class ScoredRule:
    """带激活分数的规则候选。"""
    rule_id: str
    score: float
    rule: HeuristicRule

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "score": self.score,
            "rule": self.rule.to_dict(),
        }


# ---------------------------------------------------------------------------
# 维度定义
# ---------------------------------------------------------------------------

# 7个维度的名称（索引0-6）
DIMENSION_NAMES = [
    "stability_equation_presence",  # 0: 稳定性方程存在度
    "integer_dependency",           # 1: 整数依赖度
    "lower_bound_demand",           # 2: 下界需求度
    "knowledge_gap",                # 3: 知识缺口度
    "reasoning_depth",              # 4: 推理深度
    "representation_richness",      # 5: 表示丰富度
    "stall_severity",               # 6: 卡点严重度
]

NUM_DIMENSIONS = 7

# 标定用：每个维度对应的特征关键词（在规则的LHS feature字符串或node_types中匹配）
_DIMENSION_KEYWORDS = {
    0: "稳定性方程",    # stability_equation_presence
    1: "整数",         # integer_dependency
    2: "下界",         # lower_bound_demand
    3: "未知",         # knowledge_gap（"未知"代表知识缺口）
    4: "第一步",       # reasoning_depth（浅层推理规则）
    5: "投影",         # representation_richness（涉及表示变换）
}

# stall_severity维度通过node_types匹配
_STALL_NODE_TYPE = "stall"


# ---------------------------------------------------------------------------
# 激活分数计算器
# ---------------------------------------------------------------------------

class ActivationScoreCalculator:
    """
    激活分数计算器（261号§4.2）。

    流程：
    1. extract_features: 从ParseResult提取7维特征向量p_t
    2. calibrate_weights: 用标定数据计算权重矩阵W（7维 × N规则数）
    3. calculate: 对每条规则计算激活分数 a_t = W^T · p_t，返回top-K候选
    """

    def __init__(self) -> None:
        # 权重矩阵 W（7 × N_rules），标定后填充
        self._weights: np.ndarray = np.zeros((NUM_DIMENSIONS, 0))

    # ---- 特征提取 ----

    def extract_features(self, parse_result: ParseResult) -> np.ndarray:
        """
        从ParseResult提取7维特征向量p_t（261号§4.2）。

        Args:
            parse_result: 解析器输出

        Returns:
            7维numpy数组，各维度含义见模块docstring
        """
        p_t = np.zeros(NUM_DIMENSIONS, dtype=float)

        nodes = parse_result.trajectory_nodes
        six_tuple = parse_result.six_tuple

        # 维度0: stability_equation_presence
        # T_t中是否有resolution节点包含"稳定性方程"
        p_t[0] = self._check_stability_equation(nodes)

        # 维度1: integer_dependency
        # U_t中是否有"取决于整数关系"的条目
        p_t[1] = self._check_integer_dependency(six_tuple.U_t)

        # 维度2: lower_bound_demand
        # O_t中是否有"估计下界"的open义务
        p_t[2] = self._check_lower_bound_demand(six_tuple.O_t)

        # 维度3: knowledge_gap
        # U_t中是否有knowledge_gap标注（含"知识"、"瓶颈"、"knowledge_gap"）
        p_t[3] = self._check_knowledge_gap(six_tuple.U_t)

        # 维度4: reasoning_depth
        # T_t的路径长度（节点数）
        p_t[4] = float(len(nodes))

        # 维度5: representation_richness
        # R_t的条目数
        p_t[5] = float(len(six_tuple.R_t))

        # 维度6: stall_severity
        # 是否有stall节点（0或1）
        p_t[6] = self._check_stall(nodes)

        return p_t

    @staticmethod
    def _check_stability_equation(nodes: List[TrajectoryNode]) -> float:
        """检查T_t中是否有resolution节点包含'稳定性方程'。"""
        for node in nodes:
            if node.type == "resolution" and "稳定性方程" in node.content:
                return 1.0
        return 0.0

    @staticmethod
    def _check_integer_dependency(unsolved_problems) -> float:
        """检查U_t中是否有'取决于整数'的条目。"""
        for u in unsolved_problems:
            if "取决于整数" in u.description or "整数关系" in u.description:
                return 1.0
        return 0.0

    @staticmethod
    def _check_lower_bound_demand(obligations) -> float:
        """检查O_t中是否有'估计下界'的open义务。"""
        for o in obligations:
            if o.status != "open":
                continue
            if "下界" in o.description or ("估计" in o.description and "D" in o.description):
                return 1.0
        return 0.0

    @staticmethod
    def _check_knowledge_gap(unsolved_problems) -> float:
        """检查U_t中是否有knowledge_gap标注。"""
        keywords = ["knowledge_gap", "知识", "瓶颈"]
        for u in unsolved_problems:
            for kw in keywords:
                if kw in u.description:
                    return 1.0
        return 0.0

    @staticmethod
    def _check_stall(nodes: List[TrajectoryNode]) -> float:
        """检查是否有stall节点。"""
        for node in nodes:
            if node.type == "stall":
                return 1.0
        return 0.0

    # ---- 权重标定 ----

    def calibrate_weights(
        self,
        rules: List[HeuristicRule],
        parse_results: List[ParseResult] = None,
    ) -> np.ndarray:
        """
        标定权重矩阵W（261号§4.2）。

        简化标定：对每个维度i，如果规则的LHS特征（feature字符串或node_types）
        包含该维度对应的特征关键词，权重设为1.0，否则0.0。

        Args:
            rules: 规则列表
            parse_results: 标定数据（简化标定中未使用，保留接口供后续精确标定）

        Returns:
            权重矩阵 W（NUM_DIMENSIONS × len(rules)）
        """
        n_rules = len(rules)
        W = np.zeros((NUM_DIMENSIONS, n_rules), dtype=float)

        for j, rule in enumerate(rules):
            feature_str = rule.lhs.get("feature", "")
            node_types = rule.lhs.get("node_types", [])

            for dim in range(NUM_DIMENSIONS):
                if dim == 6:
                    # stall_severity: 检查node_types中是否有stall
                    if _STALL_NODE_TYPE in node_types:
                        W[dim, j] = 1.0
                else:
                    # 其他维度: 检查feature字符串中是否包含关键词
                    keyword = _DIMENSION_KEYWORDS.get(dim, "")
                    if keyword and keyword in feature_str:
                        W[dim, j] = 1.0

        self._weights = W
        return W

    # ---- 激活分数计算 ----

    def calculate(
        self,
        parse_result: ParseResult,
        rules: List[HeuristicRule],
        top_k: int = 10,
    ) -> List[ScoredRule]:
        """
        计算激活分数，返回top-K候选（261号§4.2）。

        流程：
        1. 提取特征向量p_t
        2. 标定权重矩阵W（如未标定）
        3. 稀疏矩阵乘法 a_t = W^T · p_t
        4. 按分数降序排列，取top-K

        Args:
            parse_result: 解析器输出
            rules: 候选规则列表
            top_k: 返回的候选数量上限

        Returns:
            按激活分数降序排列的ScoredRule列表
        """
        # 提取特征向量
        p_t = self.extract_features(parse_result)

        # 标定权重（如未标定或规则数不匹配，重新标定）
        if self._weights.shape[1] != len(rules):
            self.calibrate_weights(rules)

        # 稀疏矩阵乘法 a_t = W^T · p_t
        # W: (7, N), p_t: (7,) → a_t: (N,)
        scores = self._weights.T @ p_t  # type: ignore

        # 组装ScoredRule列表
        scored_rules: List[ScoredRule] = []
        for j, rule in enumerate(rules):
            scored_rules.append(ScoredRule(
                rule_id=rule.rule_id,
                score=float(scores[j]),
                rule=rule,
            ))

        # 按分数降序排列
        scored_rules.sort(key=lambda x: x.score, reverse=True)

        # 取top-K
        return scored_rules[:top_k]
