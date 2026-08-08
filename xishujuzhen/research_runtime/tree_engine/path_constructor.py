"""PathConstructor: 脉络构造。

从根到当前节点的路径，构造给新推理AI的输入文本。

脉络文本格式（267号§7.2）：
  你正在解答以下数学题：
  [题目原文]

  之前已经进行了以下探索：

  [节点0] 初始处境：题目给出的条件和目标
    → 提示Q1：[Q1内容]
  [节点1] 处境：[从thinking中提取的数学处境描述]
    已证明：[已确立的结论]
    当前表示：[当前的数学表示]
    → 提示Q2：[Q2内容]
  ...
  [节点n] 当前处境：[当前节点的数学处境描述]
    卡在：[当前卡点]

  请理解验证以上路径后，继续探索以下方向：
  [方向Q的内容]

  继续推理，给出完整的推理过程。
"""

from typing import Optional

from .tree_store import TreeStore, TreeNode, TreeEdge


class PathConstructor:
    """
    脉络构造器。

    用法：
        constructor = PathConstructor(tree_store=store)
        path_text = constructor.construct_path_text(
            node_key="abc123",
            direction_q="考虑复数解",
        )
    """

    def __init__(self, tree_store: TreeStore):
        self.tree_store = tree_store

    def construct_path_text(
        self,
        node_key: str,
        direction_q: str,
    ) -> str:
        """
        构造脉络文本。

        Args:
            node_key: 当前节点（脉络终点）
            direction_q: 给新AI的引导方向Q

        Returns:
            脉络文本
        """
        # 获取路径上的所有节点和边
        path_nodes = self.tree_store.get_path_nodes(node_key)
        path_edges = self.tree_store.get_path_edges(node_key)

        if not path_nodes:
            return f"请解答以下数学题：\n\n请继续探索以下方向：\n{direction_q}\n\n继续推理，给出完整的推理过程。"

        # 获取题目原文
        problem_id = path_nodes[0].problem_id
        problem = self.tree_store.get_problem(problem_id)
        problem_text = problem.get("problem_text", "") if problem else ""

        # 构造脉络文本
        lines = []
        lines.append(f"你正在解答以下数学题：")
        lines.append(problem_text)
        lines.append("")
        lines.append("之前已经进行了以下探索：")
        lines.append("")

        for i, node in enumerate(path_nodes):
            if i == 0:
                # 根节点
                lines.append(f"[节点{i}] 初始处境：{self._get_node_summary(node)}")
            else:
                lines.append(f"[节点{i}] 处境：{self._get_node_summary(node)}")
                # 输出已证明/当前表示（如果situation中有）
                proven = self._extract_proven(node)
                if proven:
                    lines.append(f"  已证明：{proven}")
                representation = self._extract_representation(node)
                if representation:
                    lines.append(f"  当前表示：{representation}")

            # 如果有对应的边（提示Q），输出
            if i < len(path_edges):
                edge = path_edges[i]
                lines.append(f"  → 提示：{edge.hint_q}")

        # 最后一个节点的卡点
        last_node = path_nodes[-1]
        stuck = self._extract_stuck(last_node)
        if stuck:
            lines.append(f"  卡在：{stuck}")

        lines.append("")
        lines.append("请理解验证以上路径后，继续探索以下方向：")
        lines.append(direction_q)
        lines.append("")
        lines.append("继续推理，给出完整的推理过程。")

        return "\n".join(lines)

    def _get_node_summary(self, node: TreeNode) -> str:
        """获取节点的简要描述。"""
        if node.situation_text:
            # 取前300字符作为摘要
            text = node.situation_text[:300]
            if len(node.situation_text) > 300:
                text += "..."
            return text

        # 降级：从trajectory_segment提取
        segment = node.trajectory_segment or {}
        thinking = segment.get("thinking", "")
        if thinking:
            return thinking[:300] + ("..." if len(thinking) > 300 else "")

        return "(无处境描述)"

    def _extract_proven(self, node: TreeNode) -> str:
        """从节点situation提取已证明的结论。"""
        situation = node.situation or {}
        v_t = situation.get("V_t", [])
        if v_t:
            # V_t是已确立的数学对象/结论
            summaries = []
            for v in v_t:
                if isinstance(v, dict):
                    summaries.append(v.get("description", str(v)))
                else:
                    summaries.append(str(v))
            return "; ".join(summaries)[:500]
        return ""

    def _extract_representation(self, node: TreeNode) -> str:
        """从节点situation提取当前数学表示。"""
        situation = node.situation or {}
        f_t = situation.get("F_t", [])
        if f_t:
            return "; ".join(str(f) for f in f_t)[:300]
        return ""

    def _extract_stuck(self, node: TreeNode) -> str:
        """从节点situation提取当前卡点。"""
        situation = node.situation or {}
        u_t = situation.get("U_t", [])
        if u_t:
            summaries = []
            for u in u_t:
                if isinstance(u, dict):
                    desc = u.get("description", str(u))
                    severity = u.get("severity", "")
                    if severity:
                        summaries.append(f"{desc}({severity})")
                    else:
                        summaries.append(desc)
                else:
                    summaries.append(str(u))
            return "; ".join(summaries)[:500]
        return ""
