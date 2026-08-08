"""
一致性检查模块：260号§3.3。

检查事件序列与六元组一致性、节点与事件对应、依赖关系合理性。
返回警告列表。
"""

from typing import List

from .models import (
    SemanticEvent,
    TrajectoryNode,
    SixTuple,
    MathObject,
)


# 节点类型与语义事件类型的映射（260号附录B）
EVENT_TYPE_TO_NODE_TYPE = {
    "observation": "observation",
    "claim": "claim",
    "representation": "representation",
    "subgoal": "subgoal",
    "candidate": "candidate",
    "test": "operation",
    "tool_result": "tool_result",
    "contradiction": "contradiction",
    "stall": "stall",
    "backtrack": "backtrack",
    "resolution": "resolution",
    "verification": "resolution",  # VERIFICATION可能对应resolution节点
    # HINT_INJECTION和STATE_REDUCTION不直接对应T_t节点
}


class ConsistencyChecker:
    """
    一致性检查模块（260号§3.3）。

    检查：
    1. 事件序列与六元组一致性
    2. 节点与事件对应
    3. 依赖关系合理性

    返回警告列表。一致性检查失败不阻塞流程，只记录warning。
    """

    def check(
        self,
        semantic_events: List[SemanticEvent],
        trajectory_nodes: List[TrajectoryNode],
        six_tuple: SixTuple,
    ) -> List[str]:
        """
        执行一致性检查，返回警告列表。

        Args:
            semantic_events: 语义事件序列
            trajectory_nodes: 思维轨迹图节点
            six_tuple: 六元组状态

        Returns:
            警告列表（空列表表示无警告）
        """
        warnings: List[str] = []

        warnings.extend(
            self._check_event_node_correspondence(
                semantic_events, trajectory_nodes
            )
        )
        warnings.extend(
            self._check_six_tuple_consistency(
                semantic_events, six_tuple
            )
        )
        warnings.extend(
            self._check_frontier_node(trajectory_nodes)
        )
        warnings.extend(
            self._check_dependency_reasonableness(semantic_events)
        )

        return warnings

    def _check_event_node_correspondence(
        self,
        semantic_events: List[SemanticEvent],
        trajectory_nodes: List[TrajectoryNode],
    ) -> List[str]:
        """
        检查2：节点与事件是否对应（260号§4.2.4）。

        每个能对应到节点类型的语义事件应该有对应的节点。
        """
        warnings: List[str] = []

        # 统计可对应节点的事件类型
        mappable_events = [
            e for e in semantic_events
            if e.type in EVENT_TYPE_TO_NODE_TYPE
        ]

        # 节点数量应该与可对应事件数量大致一致
        if len(trajectory_nodes) == 0 and len(mappable_events) > 0:
            warnings.append(
                f"有{len(mappable_events)}个可对应节点的语义事件，但无轨迹节点"
            )

        # 检查前沿节点是否唯一
        frontier_count = sum(1 for n in trajectory_nodes if n.is_frontier)
        if frontier_count == 0 and len(trajectory_nodes) > 0:
            warnings.append("有轨迹节点但无前沿节点（is_frontier）")
        elif frontier_count > 1:
            warnings.append(
                f"有{frontier_count}个前沿节点，应只有一个"
            )

        return warnings

    def _check_six_tuple_consistency(
        self,
        semantic_events: List[SemanticEvent],
        six_tuple: SixTuple,
    ) -> List[str]:
        """
        检查1：事件序列与六元组是否一致（260号§4.2.4）。

        - RESOLUTION事件应对应V_t或F_t中的条目
        - REPRESENTATION事件应对应R_t中的条目
        - STALL事件应对应U_t中的blocking问题
        """
        warnings: List[str] = []

        # RESOLUTION事件应该反映在V_t或F_t中
        resolution_count = sum(
            1 for e in semantic_events if e.type == "resolution"
        )
        v_f_total = len(six_tuple.V_t) + len(six_tuple.F_t)
        if resolution_count > 0 and v_f_total == 0:
            warnings.append(
                f"有{resolution_count}个RESOLUTION事件，但V_t和F_t都为空"
            )

        # REPRESENTATION事件应该反映在R_t中
        representation_count = sum(
            1 for e in semantic_events if e.type == "representation"
        )
        if representation_count > 0 and len(six_tuple.R_t) == 0:
            warnings.append(
                f"有{representation_count}个REPRESENTATION事件，但R_t为空"
            )

        # STALL事件应该反映在U_t中
        stall_count = sum(
            1 for e in semantic_events if e.type == "stall"
        )
        if stall_count > 0 and len(six_tuple.U_t) == 0:
            warnings.append(
                f"有{stall_count}个STALL事件，但U_t为空"
            )

        return warnings

    def _check_frontier_node(
        self,
        trajectory_nodes: List[TrajectoryNode],
    ) -> List[str]:
        """
        检查前沿节点是否合理（260号§4.2.4）。

        前沿节点应该是最后一个产出节点。
        """
        warnings: List[str] = []

        if not trajectory_nodes:
            return warnings

        frontier_nodes = [n for n in trajectory_nodes if n.is_frontier]
        if len(frontier_nodes) == 1:
            # 前沿节点应该是round_index最大的
            max_round = max(n.round_index for n in trajectory_nodes)
            frontier = frontier_nodes[0]
            if frontier.round_index < max_round:
                warnings.append(
                    f"前沿节点(round={frontier.round_index})不是最大轮次(max={max_round})"
                )

        return warnings

    def _check_dependency_reasonableness(
        self,
        semantic_events: List[SemanticEvent],
    ) -> List[str]:
        """
        检查3：依赖关系是否合理（260号§4.2.4）。

        depends_on引用的event_id应该存在。
        """
        warnings: List[str] = []

        event_ids = {e.event_id for e in semantic_events}
        for event in semantic_events:
            for dep_id in event.causal_predecessors:
                if dep_id not in event_ids:
                    warnings.append(
                        f"事件{event.event_id}依赖不存在的event_id: {dep_id}"
                    )

        return warnings
