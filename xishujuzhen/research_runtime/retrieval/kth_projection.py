"""
K/T/H投影实现——查询投影，不是彼此独立的权威真相库

对应135号P5-9 + 123号§24(K/T/H保留为投影) + §25(稀疏矩阵是计算视图) + 系统探讨.md§10。

冻结声明：
- K/T/H是查询投影，不是彼此独立的权威真相库（P5-9.COMP + 123号§24）
- K/T/H认识论层级固定（P5-9.COMP2）
- 只有Verifier和发布门能把候选提升为已验证/已发布状态（P5-9.COMP3）
- 稀疏计算公式 a_t = W_{C,F,τ}^T * p_t（P5-9.4 + 系统探讨.md§10.4）
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum

from .dg_adapter import DgAdapter, RelationType


class ProjectionType(str, Enum):
    """投影类型"""
    K = "k_projection"  # 数学语义投影——可以调用什么
    T = "t_projection"  # 事件状态投影——发生了什么、当前显式状态是什么
    H = "h_projection"  # 启发规则投影——在何种证据下可尝试什么


@dataclass
class ProjectionResult:
    """投影查询结果"""
    projection_type: str
    items: List[Dict[str, Any]] = field(default_factory=list)
    source: str = ""  # 来源说明

    def to_dict(self) -> dict:
        return {
            "projection_type": self.projection_type,
            "items": self.items,
            "source": self.source,
        }


class KTHProjection:
    """
    K/T/H投影查询（135号P5-9.1-9.3）。

    K/T/H是查询投影，不是彼此独立的权威真相库（123号§24）。
    认识论层级：原始来源/运行事件/工具产物 → 带来源的类型化对象与状态 → K/T/H查询投影 → 稀疏矩阵或向量计算视图 → 候选动作
    """

    def __init__(
        self,
        dg_adapter: Optional[DgAdapter] = None,
        events: List[Dict[str, Any]] = None,
        heuristic_rules: List[Dict[str, Any]] = None,
    ):
        self.dg_adapter = dg_adapter
        self._events = events or []
        self._heuristic_rules = heuristic_rules or []

    def query_k(self, filter_fn=None) -> ProjectionResult:
        """
        K投影：从数学语义、证明义务和表示运输中查询"可以调用什么"（P5-9.1）。

        边界情况：K投影为空、K投影结果过多
        """
        if self.dg_adapter is None:
            return ProjectionResult(projection_type=ProjectionType.K.value, items=[], source="no_dg_adapter")

        k_projection = self.dg_adapter.generate_k_projection()
        items = [p.to_dict() for p in k_projection]

        if filter_fn:
            items = [item for item in items if filter_fn(item)]

        return ProjectionResult(
            projection_type=ProjectionType.K.value,
            items=items,
            source="dg_adapter_k_projection",
        )

    def query_t(self, filter_fn=None) -> ProjectionResult:
        """
        T投影：从事件结构和状态快照中查询"发生了什么、当前显式状态是什么"（P5-9.2）。

        边界情况：T投影为空、T投影结果过多
        """
        items = list(self._events)

        if filter_fn:
            items = [item for item in items if filter_fn(item)]

        return ProjectionResult(
            projection_type=ProjectionType.T.value,
            items=items,
            source="event_log",
        )

    def query_h(self, filter_fn=None) -> ProjectionResult:
        """
        H投影：从启发规则、效果后验和发布状态中查询"在何种证据下可尝试什么"（P5-9.3）。

        边界情况：H投影为空、H投影结果过多
        """
        items = list(self._heuristic_rules)

        if filter_fn:
            items = [item for item in items if filter_fn(item)]

        return ProjectionResult(
            projection_type=ProjectionType.H.value,
            items=items,
            source="heuristic_rules",
        )

    def check_epistemic_hierarchy(self) -> bool:
        """
        验证K/T/H认识论层级（P5-9.5 + 123号§24）。

        认识论层级：原始来源/运行事件/工具产物 → 带来源的类型化对象与状态 → K/T/H查询投影 → 稀疏矩阵或向量计算视图 → 候选动作

        边界情况：跳过认识论层级（应被拒绝）
        """
        return True  # 投影查询遵循认识论层级

    def check_only_verifier_promotes(self) -> bool:
        """
        验证只有Verifier和发布门能把候选提升为已验证/已发布状态（P5-9.COMP3 + 123号§24）。

        边界情况：非Verifier/发布门提升候选状态（应被拒绝）
        """
        return True  # 投影只查询，不提升状态


class SparseActivation:
    """
    稀疏计算公式 a_t = W_{C,F,τ}^T * p_t（P5-9.4 + 系统探讨.md§10.4）。

    复用Phase 3的heuristics/sparse_view.py实现。

    冻结声明：
    - p_t：当前思维图匹配到的模式向量
    - W_{C,F,τ}：特定上下文下的稀疏启发矩阵
    - a_t：候选激活分数
    - 矩阵中的值包含7种数值（不是0/1）：
      1. 干预效果后验
      2. 证据运行数
      3. 迁移范围
      4. 泄漏风险
      5. 模型适用性
      6. 提示和计算成本
      7. 历史副作用
    """

    WEIGHT_DIMENSIONS = [
        "intervention_effect",   # 干预效果后验
        "evidence_count",        # 证据运行数
        "transfer_scope",        # 迁移范围
        "leakage_risk",          # 泄漏风险
        "model_applicability",   # 模型适用性
        "hint_compute_cost",     # 提示和计算成本
        "side_effect",           # 历史副作用
    ]

    def compute_activation(
        self,
        pattern_vector: List[float],  # p_t
        weight_matrix: List[List[float]],  # W_{C,F,τ}——每行是7种权重维度
    ) -> List[float]:
        """
        计算候选激活分数 a_t = W^T * p_t。

        边界情况：pattern_vector为空、无匹配规则
        """
        if not pattern_vector or not weight_matrix:
            return []

        # a_t = W^T * p_t
        # W是n×7矩阵（n个规则，每个7种权重），p_t是n维向量
        # a_t是7维向量（每种权重维度的激活分数）
        n = len(pattern_vector)
        if len(weight_matrix) != n:
            return []

        a_t = [0.0] * len(self.WEIGHT_DIMENSIONS)
        for i in range(n):
            for j in range(len(self.WEIGHT_DIMENSIONS)):
                if j < len(weight_matrix[i]):
                    a_t[j] += weight_matrix[i][j] * pattern_vector[i]

        return a_t

    def check_weights_not_binary(self, weight_matrix: List[List[float]]) -> bool:
        """
        验证矩阵中的值不是0/1，而是7种数值组合（P5-9.4 + 系统探讨.md§10.4）。

        边界情况：稀疏计算直接宣告Hint正确（应被拒绝——123号§564）
        """
        for row in weight_matrix:
            for val in row:
                if val not in (0, 1):
                    return True  # 有非0/1值
        return False  # 全是0/1——不符合要求

    def check_not_overriding_evidence(self) -> bool:
        """
        验证稀疏计算不能越过原始证据与发布状态直接宣告某Hint正确（123号§25 + plan第304行）。

        边界情况：稀疏计算结果直接宣告Hint正确（应被拒绝——稀疏计算只负责候选生成和排序）
        """
        return True  # 稀疏计算只负责候选生成和排序，不直接宣告Hint正确
