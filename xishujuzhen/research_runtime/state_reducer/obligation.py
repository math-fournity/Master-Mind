"""
研究义务图：AND/OR超图 + DAG验证

对应132号P2-3。

123号§16定义：
- 义务图 O=(N, H_and, H_or)
- N是带类型和状态的研究义务
- AND超边(U,v)：U中全部前置义务达到证据门，v才释放
- OR超边(U,v)：U中任一充分候选达到证据门，v即释放

127号§4定义10种义务类型枚举。

冻结声明：
- 循环依赖不自动释放义务，产生待审计的SCC（P2-3.COMP2）
- 超边本体存relation document，不用普通depends_on边（P2-3.COMP）

边界情况（132号P2-3.3）：
- 自环（节点指向自己——Phase 1教训）
- 双向往返环
- 多节点环
- SCC（强连通分量——不自动释放，产生待审计的SCC）
"""

import os
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Set, Tuple
from datetime import datetime, timezone
from arango import ArangoClient

DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
DB_USER = "root"
DB_PASS = "REDACTED-DB-PASSWORD"
ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")


class ObligationType(str, Enum):
    """
    127号§4权威定义的10种义务类型枚举。

    注意：这与123号§14的TaskType（9种任务类型）是不同的概念。
    TaskType用于Q_0的κ字段；ObligationType用于O_t中义务的type字段。
    """
    PROVE = "prove"                     # 待证明
    REFUTE = "refute"                   # 待证伪
    CONSTRUCT = "construct"             # 待构造
    COMPUTE = "compute"                 # 待计算
    SEARCH = "search"                   # 待搜索
    COMPARE = "compare"                 # 待比较
    EVALUATE = "evaluate"               # 待评估
    INTERFACE = "interface"             # 跨表示运输保真义务
    VERIFICATION = "verification"       # 数值支持仍需证明或反例搜索
    VALUE = "value"                     # 方向判断（重要性/可行性/信息增益/成本）


class ObligationStatus(str, Enum):
    """
    义务状态枚举（127号§4权威定义）。
    """
    OPEN = "open"                       # 开放——尚未达到证据门
    DISCHARGED = "discharged"           # 已释放——达到证据门
    SUSPENDED = "suspended"             # 暂停
    FAILED = "failed"                   # 失败——被证伪或反例否定


class HyperedgeMode(str, Enum):
    """
    超边模式（123号§16）。
    """
    ALL = "all"     # AND超边：全部前置义务达到证据门
    ANY = "any"     # OR超边：任一充分候选达到证据门


@dataclass
class Obligation:
    """
    研究义务（127号§4权威定义 + 123号§16）。

    N是带类型和状态的研究义务。
    127号§4的9个字段：obligation_id/type/status/task_id/parent_obligation/
    description/evidence_refs/evidence_gate/sub_obligations
    """
    obligation_id: str
    task_id: str
    type: ObligationType
    status: ObligationStatus = ObligationStatus.OPEN
    description: str = ""                           # 义务描述
    parent_obligation: Optional[str] = None         # 父义务ID（127号§4字段名）
    evidence_refs: List[str] = field(default_factory=list)  # 关联证据ID（127号§4）
    evidence_gate: Optional[str] = None             # 证据门（达到什么标准才释放）
    sub_obligations: List[str] = field(default_factory=list)  # 子义务ID列表（127号§4）
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "obligation_id": self.obligation_id,
            "task_id": self.task_id,
            "type": self.type.value,
            "status": self.status.value,
            "description": self.description,
            "parent_obligation": self.parent_obligation,
            "evidence_refs": self.evidence_refs,
            "evidence_gate": self.evidence_gate,
            "sub_obligations": self.sub_obligations,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


@dataclass
class ObligationHyperedge:
    """
    义务超边relation document（123号§16 + 127号§4）。

    超边(U,v)其中U是前置义务集合，v是父义务。
    超边本体存relation document，participant edges连接义务。
    """
    relation_id: str
    mode: HyperedgeMode                               # all=AND / any=OR
    parent_obligation: str                             # v（父义务，127号§4字段名）
    source_obligation_ids: List[str] = field(default_factory=list)  # U（前置义务集合）
    sufficiency_condition: Optional[str] = None        # 充分性条件
    evidence_gate: Optional[str] = None                # 证据门
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "relation_id": self.relation_id,
            "mode": self.mode.value,
            "parent_obligation": self.parent_obligation,
            "source_obligation_ids": self.source_obligation_ids,
            "sufficiency_condition": self.sufficiency_condition,
            "evidence_gate": self.evidence_gate,
            "created_at": self.created_at,
        }


class ObligationStore:
    """
    义务图ArangoDB存储。

    超边存储方式（P2-3.COMP）：
    - 超边本体存relation document（obligation_relations collection）
    - participant edges存obligation_edges collection（role=source/target）
    - 不用普通depends_on边
    """

    def __init__(
        self,
        db_name: str = DB_NAME,
        username: str = DB_USER,
        password: str = DB_PASS,
        host: str = ARANGO_HOST,
    ):
        client = ArangoClient(hosts=host)
        self.db = client.db(db_name, username=username, password=password)
        self.obl_col = self.db.collection("obligations")
        self.rel_col = self.db.collection("obligation_relations")
        self.edge_col = self.db.collection("obligation_edges")

    def insert_obligation(self, obl: Obligation) -> str:
        """插入义务节点。"""
        doc = obl.to_dict()
        doc["_key"] = obl.obligation_id
        result = self.obl_col.insert(doc)
        return result["_key"]

    def get_obligation(self, obligation_id: str) -> Optional[Dict[str, Any]]:
        """读取义务节点。"""
        doc = self.obl_col.get(obligation_id)
        if doc is None:
            return None
        doc.pop("_id", None)
        doc.pop("_rev", None)
        return doc

    def update_obligation_status(
        self,
        obligation_id: str,
        status: ObligationStatus,
    ) -> bool:
        """更新义务状态。"""
        doc = self.obl_col.get(obligation_id)
        if doc is None:
            return False
        doc["status"] = status.value
        doc["updated_at"] = datetime.now(timezone.utc).isoformat()
        self.obl_col.replace(doc)
        return True

    def insert_hyperedge(self, edge: ObligationHyperedge) -> str:
        """
        插入超边。

        超边本体存relation document，participant edges连接义务。
        每个source义务和parent义务之间各有一条participant edge。
        """
        # 1. 存relation document
        rel_doc = edge.to_dict()
        rel_doc["_key"] = edge.relation_id
        self.rel_col.insert(rel_doc)

        # 2. 存participant edges
        # source edges: obligation → relation
        for src_id in edge.source_obligation_ids:
            self.edge_col.insert({
                "_from": f"obligations/{src_id}",
                "_to": f"obligation_relations/{edge.relation_id}",
                "role": "source",
                "relation_id": edge.relation_id,
            })
        # target edge: relation → parent obligation
        self.edge_col.insert({
            "_from": f"obligation_relations/{edge.relation_id}",
            "_to": f"obligations/{edge.parent_obligation}",
            "role": "target",
            "relation_id": edge.relation_id,
        })

        return edge.relation_id

    def get_hyperedge(self, relation_id: str) -> Optional[Dict[str, Any]]:
        """读取超边relation document。"""
        doc = self.rel_col.get(relation_id)
        if doc is None:
            return None
        doc.pop("_id", None)
        doc.pop("_rev", None)
        return doc

    def get_parent_obligations(self, obligation_id: str) -> List[str]:
        """获取一个义务的父义务（通过超边）。"""
        # 找到所有指向该义务的target edge
        aql = """
        FOR e IN obligation_edges
            FILTER e._to == @obl_ref AND e.role == 'target'
            LET rel = DOCUMENT(e._from)
            RETURN rel.parent_obligation
        """
        cursor = self.db.aql.execute(aql, bind_vars={"obl_ref": f"obligations/{obligation_id}"})
        return list(cursor)

    def get_source_obligations(self, relation_id: str) -> List[str]:
        """获取一个超边的所有source义务。"""
        aql = """
        FOR e IN obligation_edges
            FILTER e._from == @rel_ref AND e.role == 'source'
            LET obl = DOCUMENT(e._to)
            RETURN obl.obligation_id
        """
        cursor = self.db.aql.execute(aql, bind_vars={"rel_ref": f"obligation_relations/{relation_id}"})
        return list(cursor)

    def check_dag(self) -> Dict[str, Any]:
        """
        验证义务图是DAG（无环）。

        边界情况（132号P2-3.3）：
        - 自环（节点指向自己）
        - 双向往返环
        - 多节点环
        - SCC（强连通分量——不自动释放，产生待审计的SCC）

        返回：
        - is_dag: 是否是DAG
        - cycles: 检测到的环列表
        - sccs: 强连通分量列表
        - self_loops: 自环列表
        """
        # 构建邻接表：obligation_id → [parent_obligations]
        # 超边展开为普通边：每个source → parent
        aql = """
        FOR rel IN obligation_relations
            FOR src IN rel.source_obligation_ids
                RETURN {source: src, target: rel.parent_obligation}
        """
        cursor = self.db.aql.execute(aql)
        edges = list(cursor)

        # 构建邻接表
        adj: Dict[str, List[str]] = {}
        nodes: Set[str] = set()
        for e in edges:
            src, tgt = e["source"], e["target"]
            adj.setdefault(src, []).append(tgt)
            nodes.add(src)
            nodes.add(tgt)

        # 检测自环
        self_loops = [n for n in nodes if n in adj.get(n, [])]

        # 检测环（DFS）
        cycles = self._find_cycles(adj, nodes)

        # 计算SCC（Tarjan算法简化版）
        sccs = self._find_sccs(adj, nodes)

        is_dag = len(cycles) == 0 and len(self_loops) == 0

        return {
            "is_dag": is_dag,
            "cycles": cycles,
            "sccs": sccs,
            "self_loops": self_loops,
            "node_count": len(nodes),
            "edge_count": len(edges),
        }

    def _find_cycles(self, adj: Dict[str, List[str]], nodes: Set[str]) -> List[List[str]]:
        """DFS检测环。"""
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {n: WHITE for n in nodes}
        cycles = []

        def dfs(node: str, path: List[str]):
            color[node] = GRAY
            path.append(node)
            for neighbor in adj.get(node, []):
                if color.get(neighbor, WHITE) == GRAY:
                    # 找到环
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    cycles.append(cycle)
                elif color.get(neighbor, WHITE) == WHITE:
                    dfs(neighbor, path)
            path.pop()
            color[node] = BLACK

        for n in nodes:
            if color[n] == WHITE:
                dfs(n, [])

        return cycles

    def _find_sccs(self, adj: Dict[str, List[str]], nodes: Set[str]) -> List[List[str]]:
        """Tarjan算法计算SCC。"""
        index_counter = [0]
        stack: List[str] = []
        lowlink: Dict[str, int] = {}
        index: Dict[str, int] = {}
        on_stack: Dict[str, bool] = {}
        sccs: List[List[str]] = []

        def strongconnect(node: str):
            index[node] = index_counter[0]
            lowlink[node] = index_counter[0]
            index_counter[0] += 1
            stack.append(node)
            on_stack[node] = True

            for successor in adj.get(node, []):
                if successor not in index:
                    strongconnect(successor)
                    lowlink[node] = min(lowlink[node], lowlink[successor])
                elif on_stack.get(successor, False):
                    lowlink[node] = min(lowlink[node], index[successor])

            if lowlink[node] == index[node]:
                scc = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    scc.append(w)
                    if w == node:
                        break
                if len(scc) > 1:  # 只记录大小>1的SCC
                    sccs.append(scc)

        for n in nodes:
            if n not in index:
                strongconnect(n)

        return sccs

    def check_release_conditions(self, obligation_id: str) -> Dict[str, Any]:
        """
        检查义务是否可以释放。

        AND超边：所有source义务都达到证据门
        OR超边：任一source义务达到证据门

        循环依赖不自动释放（P2-3.COMP2）——如果义务在SCC中，不自动释放。
        """
        # 获取指向该义务的所有超边
        aql = """
        FOR e IN obligation_edges
            FILTER e._to == @obl_ref AND e.role == 'target'
            LET rel = DOCUMENT(e._from)
            RETURN rel
        """
        cursor = self.db.aql.execute(aql, bind_vars={"obl_ref": f"obligations/{obligation_id}"})
        relations = list(cursor)

        if not relations:
            return {
                "can_release": True,
                "reason": "无前置义务",
                "relations": [],
            }

        # 检查每个超边的释放条件
        dag_check = self.check_dag()
        in_scc = any(obligation_id in scc for scc in dag_check["sccs"])

        if in_scc:
            return {
                "can_release": False,
                "reason": "循环依赖不自动释放——产生待审计的SCC（P2-3.COMP2）",
                "relations": relations,
            }

        all_satisfied = True
        any_satisfied = False
        for rel in relations:
            source_ids = rel["source_obligation_ids"]
            mode = rel["mode"]

            # 检查source义务状态
            sources_released = []
            for src_id in source_ids:
                src_doc = self.get_obligation(src_id)
                if src_doc and src_doc["status"] == ObligationStatus.DISCHARGED.value:
                    sources_released.append(src_id)

            if mode == HyperedgeMode.ALL.value:
                if len(sources_released) != len(source_ids):
                    all_satisfied = False
            elif mode == HyperedgeMode.ANY.value:
                if len(sources_released) > 0:
                    any_satisfied = True

        # AND超边全部满足 或 OR超边任一满足
        can_release = all_satisfied or any_satisfied

        return {
            "can_release": can_release,
            "reason": "所有前置义务达到证据门" if can_release else "前置义务未全部达到证据门",
            "relations": relations,
            "in_scc": in_scc,
        }
