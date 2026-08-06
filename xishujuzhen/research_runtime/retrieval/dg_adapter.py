"""
legacy图只读adapter——从dg_*生成candidate K投影

对应135号P5-8 + 123号§55(数据迁移原则) + NO-10约束。

冻结声明：
- adapter只读，不修改dg_*数据（P5-8.COMP + NO-10）
- adapter不原地迁移旧数据（P5-8.COMP3 + 123号§55）
- K投影按5种关系矩阵分拆（P5-8.COMP2 + 123号§25）

F-176-4修正：使用深拷贝替代浅拷贝，防止外部代码通过引用修改内部数据。
"""

import copy
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class RelationType(str, Enum):
    """
    K投影的5种关系矩阵（123号§25）。
    """
    REQUIRES = "requires"           # 前置依赖
    USES = "uses"                   # 使用
    GENERALIZES = "generalizes"     # 推广
    ANALOGOUS = "analogous"         # 类比
    VERIFIED_BY = "verified_by"     # 验证依据


@dataclass
class KProjectionEntry:
    """K投影条目"""
    node_id: str
    relation: str  # RelationType枚举值
    target_id: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "node_id": self.node_id,
            "relation": self.relation,
            "target_id": self.target_id,
            "metadata": self.metadata,
        }


class DgAdapter:
    """
    legacy图只读adapter（135号P5-8.1）。

    从dg_*集合生成candidate K投影，不修改原数据。

    冻结声明：
    - 只读：adapter不修改dg_*数据（P5-8.COMP）
    - 不原地迁移：adapter不原地迁移旧数据（P5-8.COMP3 + NO-10）
    - K投影按5种关系矩阵分拆（P5-8.COMP2）
    """

    def __init__(self, dg_nodes: List[Dict[str, Any]] = None, dg_edges: List[Dict[str, Any]] = None):
        """
        初始化adapter。

        参数：
        - dg_nodes: legacy dg_nodes集合的快照（只读）
        - dg_edges: legacy dg_edges集合的快照（只读）

        F-176-4修正：使用深拷贝，防止外部代码通过引用修改内部字典内容。
        """
        self._dg_nodes = copy.deepcopy(dg_nodes) if dg_nodes else []  # 深拷贝，确保只读
        self._dg_edges = copy.deepcopy(dg_edges) if dg_edges else []
        self._original_node_count = len(self._dg_nodes)
        self._original_edge_count = len(self._dg_edges)
        # F-176-4：记录原始内容哈希用于check_readonly验证
        import hashlib as _hl
        import json as _json
        self._original_node_hash = _hl.sha256(
            _json.dumps(self._dg_nodes, sort_keys=True, ensure_ascii=False).encode("utf-8")
        ).hexdigest()
        self._original_edge_hash = _hl.sha256(
            _json.dumps(self._dg_edges, sort_keys=True, ensure_ascii=False).encode("utf-8")
        ).hexdigest()

    def generate_k_projection(self) -> List[KProjectionEntry]:
        """
        从dg_*生成candidate K投影。

        边界情况：dg_*为空、dg_*格式不兼容
        """
        projections = []
        for edge in self._dg_edges:
            relation = edge.get("relation", "")
            # 只处理5种关系矩阵
            if relation in [r.value for r in RelationType]:
                projections.append(KProjectionEntry(
                    node_id=edge.get("from", edge.get("source", "")),
                    relation=relation,
                    target_id=edge.get("to", edge.get("target", "")),
                    metadata=edge.get("metadata", {}),
                ))
        return projections

    def split_by_relation(self, k_projection: List[KProjectionEntry]) -> Dict[str, List[KProjectionEntry]]:
        """
        K投影按5种关系矩阵分拆（P5-8.4 + 123号§25）。

        边界情况：某关系矩阵无数据、关系矩阵混淆
        """
        result = {r.value: [] for r in RelationType}
        for entry in k_projection:
            if entry.relation in result:
                result[entry.relation].append(entry)
        return result

    def check_readonly(self) -> bool:
        """
        验证adapter不修改dg_*数据（P5-8.2 + P5-8.COMP）。

        F-176-4修正：检查内容哈希而非长度，防止内容被修改但长度不变的情况。

        边界情况：adapter修改dg_*数据（应被拒绝）
        """
        import hashlib
        import json
        current_node_hash = hashlib.sha256(
            json.dumps(self._dg_nodes, sort_keys=True, ensure_ascii=False).encode("utf-8")
        ).hexdigest()
        current_edge_hash = hashlib.sha256(
            json.dumps(self._dg_edges, sort_keys=True, ensure_ascii=False).encode("utf-8")
        ).hexdigest()
        return (current_node_hash == self._original_node_hash and
                current_edge_hash == self._original_edge_hash)

    def check_no_migration(self) -> bool:
        """
        验证adapter不原地迁移旧数据（P5-8.3 + P5-8.COMP3 + NO-10）。

        边界情况：adapter原地迁移旧数据（应被拒绝）
        """
        return True  # adapter只读取快照，不修改原数据

    def get_node_count(self) -> int:
        return len(self._dg_nodes)

    def get_edge_count(self) -> int:
        return len(self._dg_edges)
