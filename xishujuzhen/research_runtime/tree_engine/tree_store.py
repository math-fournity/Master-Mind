"""TreeStore: ArangoDB树存储，管理tree_nodes/tree_edges/problems/ai_instances 4个集合。

对应267号§6.1的数据库表设计。

集合结构：
  tree_nodes (document)  - 节点=数学处境（六元组+path_from_root）
  tree_edges (edge)      - 边=提示Q（_from父→_to子）
  problems (document)    - 题目（每题一棵树）
  ai_instances (document)- 推理AI实例注册

连接方式复用rule_store.py的模式：环境变量ARANGO_DB=grove_math。
in_memory=True模式供单元测试用。
"""

import os
import time
import uuid
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

# ArangoDB连接配置（与rule_store.py一致）
DB_NAME = os.environ.get("ARANGO_DB", "grove_math")
DB_USER = os.environ.get("ARANGO_USER", "root")
DB_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")
ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")


# ============================================================
# 数据类
# ============================================================

@dataclass
class TreeNode:
    """树节点 = 一个数学处境（267号§6.1 tree_nodes）。"""
    problem_id: str
    node_type: str = "internal"  # root/internal/leaf_success/leaf_deadend/leaf_truncated
    situation: Dict[str, Any] = field(default_factory=dict)  # 六元组 V_t/F_t/O_t/U_t/T_t/S_t
    situation_text: str = ""     # 从thinking提取的自然语言描述
    depth: int = 0
    parent_edge_key: Optional[str] = None
    parent_node_key: str = ""  # 父节点key（同一AI内的轮次间无edge但有父子关系）
    path_from_root: List[str] = field(default_factory=list)  # node_key序列
    created_by_ai: str = ""      # ai_instance_id
    created_at: float = field(default_factory=time.time)
    trajectory_segment: Dict[str, Any] = field(default_factory=dict)  # thinking片段+tool_calls
    status: str = "growing"      # growing/completed/deadend/truncated
    retrieval_done: bool = False
    directions_identified: List[str] = field(default_factory=list)  # 方向Q的ID列表
    ai_instances_started: List[str] = field(default_factory=list)  # 从此节点启动的AI实例ID列表
    _key: str = ""

    def to_dict(self) -> dict:
        d = {
            "problem_id": self.problem_id,
            "node_type": self.node_type,
            "situation": dict(self.situation),
            "situation_text": self.situation_text,
            "depth": self.depth,
            "parent_edge_key": self.parent_edge_key,
            "parent_node_key": self.parent_node_key,
            "path_from_root": list(self.path_from_root),
            "created_by_ai": self.created_by_ai,
            "created_at": self.created_at,
            "trajectory_segment": dict(self.trajectory_segment),
            "status": self.status,
            "retrieval_done": self.retrieval_done,
            "directions_identified": list(self.directions_identified),
            "ai_instances_started": list(self.ai_instances_started),
        }
        if self._key:
            d["_key"] = self._key
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "TreeNode":
        return cls(
            _key=d.get("_key", ""),
            problem_id=d.get("problem_id", ""),
            node_type=d.get("node_type", "internal"),
            situation=dict(d.get("situation", {})),
            situation_text=d.get("situation_text", ""),
            depth=d.get("depth", 0),
            parent_edge_key=d.get("parent_edge_key"),
            parent_node_key=d.get("parent_node_key", ""),
            path_from_root=list(d.get("path_from_root", [])),
            created_by_ai=d.get("created_by_ai", ""),
            created_at=d.get("created_at", 0.0),
            trajectory_segment=dict(d.get("trajectory_segment", {})),
            status=d.get("status", "growing"),
            retrieval_done=d.get("retrieval_done", False),
            directions_identified=list(d.get("directions_identified", [])),
            ai_instances_started=list(d.get("ai_instances_started", [])),
        )


@dataclass
class TreeEdge:
    """树边 = 一个提示Q（267号§6.1 tree_edges）。"""
    problem_id: str
    _from: str = ""          # 父节点 tree_nodes/xxx
    _to: str = ""            # 子节点 tree_nodes/yyy
    hint_q: str = ""         # 提示Q内容
    hint_q_id: str = ""      # Pattern ID（如有）
    hint_level: float = 0.0
    ai_instance_id: str = "" # 沿这条边探索的AI实例ID
    created_at: float = field(default_factory=time.time)
    edge_status: str = "growing"  # growing/completed/deadend/truncated
    _key: str = ""

    def to_dict(self) -> dict:
        d = {
            "problem_id": self.problem_id,
            "hint_q": self.hint_q,
            "hint_q_id": self.hint_q_id,
            "hint_level": self.hint_level,
            "ai_instance_id": self.ai_instance_id,
            "created_at": self.created_at,
            "edge_status": self.edge_status,
        }
        if self._from:
            d["_from"] = self._from
        if self._to:
            d["_to"] = self._to
        if self._key:
            d["_key"] = self._key
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "TreeEdge":
        return cls(
            _key=d.get("_key", ""),
            problem_id=d.get("problem_id", ""),
            _from=d.get("_from", ""),
            _to=d.get("_to", ""),
            hint_q=d.get("hint_q", ""),
            hint_q_id=d.get("hint_q_id", ""),
            hint_level=d.get("hint_level", 0.0),
            ai_instance_id=d.get("ai_instance_id", ""),
            created_at=d.get("created_at", 0.0),
            edge_status=d.get("edge_status", "growing"),
        )


@dataclass
class AIInstance:
    """推理AI实例注册（267号§6.1 ai_instances）。"""
    problem_id: str
    entry_node_key: str      # 进入树的节点
    entry_edge_key: Optional[str] = None  # 沿哪条边进入（从根开始则null）
    path_text: str = ""      # 给AI的脉络输入
    hint_q: str = ""         # 给AI的引导方向Q
    tmux_session: str = ""
    devin_session_id: str = ""
    status: str = "running"  # running/completed/crashed/truncated
    started_at: float = field(default_factory=time.time)
    ended_at: float = 0.0
    end_reason: str = ""     # token_limit/crash/solution_found/manual_stop
    trajectory_dir: str = ""
    nodes_contributed: List[str] = field(default_factory=list)
    _key: str = ""

    def to_dict(self) -> dict:
        d = {
            "problem_id": self.problem_id,
            "entry_node_key": self.entry_node_key,
            "entry_edge_key": self.entry_edge_key,
            "path_text": self.path_text,
            "hint_q": self.hint_q,
            "tmux_session": self.tmux_session,
            "devin_session_id": self.devin_session_id,
            "status": self.status,
            "started_at": self.started_at,
            "ended_at": self.ended_at,
            "end_reason": self.end_reason,
            "trajectory_dir": self.trajectory_dir,
            "nodes_contributed": list(self.nodes_contributed),
        }
        if self._key:
            d["_key"] = self._key
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "AIInstance":
        return cls(
            _key=d.get("_key", ""),
            problem_id=d.get("problem_id", ""),
            entry_node_key=d.get("entry_node_key", ""),
            entry_edge_key=d.get("entry_edge_key"),
            path_text=d.get("path_text", ""),
            hint_q=d.get("hint_q", ""),
            tmux_session=d.get("tmux_session", ""),
            devin_session_id=d.get("devin_session_id", ""),
            status=d.get("status", "running"),
            started_at=d.get("started_at", 0.0),
            ended_at=d.get("ended_at", 0.0),
            end_reason=d.get("end_reason", ""),
            trajectory_dir=d.get("trajectory_dir", ""),
            nodes_contributed=list(d.get("nodes_contributed", [])),
        )


# ============================================================
# TreeStore
# ============================================================

COLLECTION_NODES = "tree_nodes"
COLLECTION_EDGES = "tree_edges"
COLLECTION_PROBLEMS = "problems"
COLLECTION_AI_INSTANCES = "ai_instances"


class TreeStore:
    """
    ArangoDB树存储。

    用法：
        store = TreeStore()  # 连接ArangoDB
        store = TreeStore(in_memory=True)  # 内存模式（测试用）

        # 创建题目
        root_key = store.create_problem("case_253", "题目原文...")

        # 添加节点
        node = TreeNode(problem_id="case_253", ...)
        node_key = store.add_node("case_253", node)

        # 获取路径
        path = store.get_path_from_root(node_key)
    """

    def __init__(
        self,
        db_name: str = DB_NAME,
        username: str = DB_USER,
        password: str = DB_PASS,
        host: str = ARANGO_HOST,
        in_memory: bool = False,
    ):
        self.in_memory = in_memory
        self._memory: Dict[str, Dict[str, dict]] = {
            COLLECTION_NODES: {},
            COLLECTION_EDGES: {},
            COLLECTION_PROBLEMS: {},
            COLLECTION_AI_INSTANCES: {},
        }

        if not in_memory:
            from arango import ArangoClient
            client = ArangoClient(hosts=host)
            self.db = client.db(db_name, username=username, password=password)
            self._ensure_collections()
        else:
            self.db = None

    def _ensure_collections(self):
        """确保4个集合存在，不存在则创建。"""
        for name in [COLLECTION_NODES, COLLECTION_PROBLEMS, COLLECTION_AI_INSTANCES]:
            if not self.db.has_collection(name):
                self.db.create_collection(name)

        if not self.db.has_collection(COLLECTION_EDGES):
            self.db.create_collection(COLLECTION_EDGES, edge=True)

    def _gen_key(self) -> str:
        """生成唯一key。"""
        return uuid.uuid4().hex[:16]

    # ============================================================
    # problems
    # ============================================================

    def create_problem(self, problem_id: str, problem_text: str) -> str:
        """创建题目，同时创建根节点。返回root_node_key。"""
        root_key = self._gen_key()
        now = time.time()

        problem_doc = {
            "_key": problem_id,
            "problem_text": problem_text,
            "root_node_key": root_key,
            "status": "growing",  # growing/solved/exhausted
            "solution_path": [],
            "created_at": now,
            "solved_at": 0.0,
            "total_nodes": 1,
            "total_edges": 0,
            "ai_instances_used": 0,
        }

        root_node = TreeNode(
            _key=root_key,
            problem_id=problem_id,
            node_type="root",
            situation={},
            situation_text=problem_text,
            depth=0,
            parent_edge_key=None,
            path_from_root=[root_key],
            created_by_ai="",
            created_at=now,
            trajectory_segment={},
            status="growing",
        )

        if self.in_memory:
            self._memory[COLLECTION_PROBLEMS][problem_id] = problem_doc
            self._memory[COLLECTION_NODES][root_key] = root_node.to_dict()
        else:
            col_p = self.db.collection(COLLECTION_PROBLEMS)
            col_n = self.db.collection(COLLECTION_NODES)
            col_p.insert(problem_doc)
            col_n.insert(root_node.to_dict())

        return root_key

    def get_problem(self, problem_id: str) -> Optional[dict]:
        """获取题目文档。"""
        if self.in_memory:
            return self._memory[COLLECTION_PROBLEMS].get(problem_id)
        col = self.db.collection(COLLECTION_PROBLEMS)
        return col.get(problem_id)

    def update_problem_status(self, problem_id: str, status: str, **extra):
        """更新题目状态。"""
        if self.in_memory:
            doc = self._memory[COLLECTION_PROBLEMS].get(problem_id)
            if doc:
                doc["status"] = status
                doc.update(extra)
            return

        col = self.db.collection(COLLECTION_PROBLEMS)
        doc = col.get(problem_id)
        if doc:
            doc["status"] = status
            doc.update(extra)
            col.replace(doc)

    def _increment_problem_counter(self, problem_id: str, field: str, amount: int = 1):
        """内部方法：递增题目的计数器（total_nodes/total_edges/ai_instances_used）。"""
        if self.in_memory:
            doc = self._memory[COLLECTION_PROBLEMS].get(problem_id)
            if doc:
                doc[field] = doc.get(field, 0) + amount
            return

        col = self.db.collection(COLLECTION_PROBLEMS)
        doc = col.get(problem_id)
        if doc:
            doc[field] = doc.get(field, 0) + amount
            col.replace(doc)

    # ============================================================
    # tree_nodes
    # ============================================================

    def add_node(self, problem_id: str, node: TreeNode) -> str:
        """添加节点。返回node_key。"""
        if not node._key:
            node._key = self._gen_key()

        # 确保path_from_root包含自己
        if not node.path_from_root or node.path_from_root[-1] != node._key:
            # 优先通过parent_edge_key找父节点
            if node.parent_edge_key:
                parent_edge = self.get_edge(node.parent_edge_key)
                if parent_edge and parent_edge._from:
                    # _from是完整文档ID（tree_nodes/xxx），提取key
                    parent_key = parent_edge._from.split("/")[-1]
                    parent_node = self.get_node(parent_key)
                    if parent_node:
                        node.path_from_root = parent_node.path_from_root + [node._key]
                        node.depth = parent_node.depth + 1
            # 其次通过parent_node_key找父节点（同一AI内的轮次间无edge）
            elif node.parent_node_key:
                parent_node = self.get_node(node.parent_node_key)
                if parent_node:
                    node.path_from_root = parent_node.path_from_root + [node._key]
                    node.depth = parent_node.depth + 1
            elif node.depth == 0:
                node.path_from_root = [node._key]

        doc = node.to_dict()
        if self.in_memory:
            self._memory[COLLECTION_NODES][node._key] = doc
        else:
            self.db.collection(COLLECTION_NODES).insert(doc)

        self._increment_problem_counter(problem_id, "total_nodes")
        return node._key

    def get_node(self, node_key: str) -> Optional[TreeNode]:
        """获取单个节点。"""
        if self.in_memory:
            doc = self._memory[COLLECTION_NODES].get(node_key)
        else:
            doc = self.db.collection(COLLECTION_NODES).get(node_key)

        if doc is None:
            return None
        return TreeNode.from_dict(doc)

    def get_nodes_by_problem(self, problem_id: str) -> List[TreeNode]:
        """获取某棵树的所有节点。"""
        if self.in_memory:
            docs = [d for d in self._memory[COLLECTION_NODES].values()
                    if d.get("problem_id") == problem_id]
        else:
            cursor = self.db.aql.execute(
                "FOR node IN tree_nodes FILTER node.problem_id == @pid RETURN node",
                bind_vars={"pid": problem_id},
            )
            docs = list(cursor)

        return [TreeNode.from_dict(d) for d in docs]

    def get_growing_nodes(self, problem_id: str) -> List[TreeNode]:
        """获取所有status=growing的节点（可分配新AI的节点）。"""
        if self.in_memory:
            docs = [d for d in self._memory[COLLECTION_NODES].values()
                    if d.get("problem_id") == problem_id and d.get("status") == "growing"]
        else:
            cursor = self.db.aql.execute(
                "FOR node IN tree_nodes "
                "FILTER node.problem_id == @pid AND node.status == 'growing' "
                "RETURN node",
                bind_vars={"pid": problem_id},
            )
            docs = list(cursor)

        return [TreeNode.from_dict(d) for d in docs]

    def update_node_status(self, node_key: str, status: str, **extra):
        """更新节点状态。"""
        if self.in_memory:
            doc = self._memory[COLLECTION_NODES].get(node_key)
            if doc:
                doc["status"] = status
                doc.update(extra)
            return

        col = self.db.collection(COLLECTION_NODES)
        doc = col.get(node_key)
        if doc:
            doc["status"] = status
            doc.update(extra)
            col.replace(doc)

    def update_node(self, node_key: str, updates: dict):
        """通用更新节点字段。"""
        if self.in_memory:
            doc = self._memory[COLLECTION_NODES].get(node_key)
            if doc:
                doc.update(updates)
            return

        col = self.db.collection(COLLECTION_NODES)
        doc = col.get(node_key)
        if doc:
            doc.update(updates)
            col.replace(doc)

    # ============================================================
    # tree_edges
    # ============================================================

    def add_edge(self, problem_id: str, edge: TreeEdge) -> str:
        """添加边。返回edge_key。"""
        if not edge._key:
            edge._key = self._gen_key()

        doc = edge.to_dict()
        if self.in_memory:
            self._memory[COLLECTION_EDGES][edge._key] = doc
        else:
            self.db.collection(COLLECTION_EDGES).insert(doc)

        self._increment_problem_counter(problem_id, "total_edges")
        return edge._key

    def get_edge(self, edge_key: str) -> Optional[TreeEdge]:
        """获取单条边。"""
        if self.in_memory:
            doc = self._memory[COLLECTION_EDGES].get(edge_key)
        else:
            doc = self.db.collection(COLLECTION_EDGES).get(edge_key)

        if doc is None:
            return None
        return TreeEdge.from_dict(doc)

    def get_edges_by_problem(self, problem_id: str) -> List[TreeEdge]:
        """获取某棵树的所有边。"""
        if self.in_memory:
            docs = [d for d in self._memory[COLLECTION_EDGES].values()
                    if d.get("problem_id") == problem_id]
        else:
            cursor = self.db.aql.execute(
                "FOR edge IN tree_edges FILTER edge.problem_id == @pid RETURN edge",
                bind_vars={"pid": problem_id},
            )
            docs = list(cursor)

        return [TreeEdge.from_dict(d) for d in docs]

    def get_child_edges(self, node_key: str) -> List[TreeEdge]:
        """获取从某节点出发的所有子边。"""
        from_key = f"tree_nodes/{node_key}"
        if self.in_memory:
            docs = [d for d in self._memory[COLLECTION_EDGES].values()
                    if d.get("_from") == from_key]
        else:
            cursor = self.db.aql.execute(
                "FOR edge IN tree_edges FILTER edge._from == @from RETURN edge",
                bind_vars={"from": from_key},
            )
            docs = list(cursor)

        return [TreeEdge.from_dict(d) for d in docs]

    # ============================================================
    # ai_instances
    # ============================================================

    def register_ai(self, ai: AIInstance) -> str:
        """注册AI实例。返回ai_key。"""
        if not ai._key:
            ai._key = self._gen_key()

        doc = ai.to_dict()
        if self.in_memory:
            self._memory[COLLECTION_AI_INSTANCES][ai._key] = doc
        else:
            self.db.collection(COLLECTION_AI_INSTANCES).insert(doc)

        self._increment_problem_counter(ai.problem_id, "ai_instances_used")
        return ai._key

    def get_ai(self, ai_key: str) -> Optional[AIInstance]:
        """获取AI实例。"""
        if self.in_memory:
            doc = self._memory[COLLECTION_AI_INSTANCES].get(ai_key)
        else:
            doc = self.db.collection(COLLECTION_AI_INSTANCES).get(ai_key)

        if doc is None:
            return None
        return AIInstance.from_dict(doc)

    def update_ai_status(
        self, ai_key: str, status: str,
        end_reason: str = "",
        nodes_contributed: Optional[List[str]] = None,
    ):
        """更新AI实例状态。"""
        updates = {
            "status": status,
            "ended_at": time.time(),
            "end_reason": end_reason,
        }
        if nodes_contributed is not None:
            updates["nodes_contributed"] = nodes_contributed

        if self.in_memory:
            doc = self._memory[COLLECTION_AI_INSTANCES].get(ai_key)
            if doc:
                doc.update(updates)
            return

        col = self.db.collection(COLLECTION_AI_INSTANCES)
        doc = col.get(ai_key)
        if doc:
            doc.update(updates)
            col.replace(doc)

    def get_ais_by_problem(self, problem_id: str) -> List[AIInstance]:
        """获取某题目的所有AI实例。"""
        if self.in_memory:
            docs = [d for d in self._memory[COLLECTION_AI_INSTANCES].values()
                    if d.get("problem_id") == problem_id]
        else:
            cursor = self.db.aql.execute(
                "FOR ai IN ai_instances FILTER ai.problem_id == @pid RETURN ai",
                bind_vars={"pid": problem_id},
            )
            docs = list(cursor)

        return [AIInstance.from_dict(d) for d in docs]

    # ============================================================
    # 路径查询
    # ============================================================

    def get_path_from_root(self, node_key: str) -> List[str]:
        """获取从根到某节点的路径（node_key列表）。

        利用path_from_root冗余字段直接获取，无需递归查询。
        """
        node = self.get_node(node_key)
        if node is None:
            return []
        return list(node.path_from_root)

    def get_path_nodes(self, node_key: str) -> List[TreeNode]:
        """获取从根到某节点的路径上的所有节点对象。"""
        path_keys = self.get_path_from_root(node_key)
        nodes = []
        for k in path_keys:
            n = self.get_node(k)
            if n:
                nodes.append(n)
        return nodes

    def get_path_edges(self, node_key: str) -> List[TreeEdge]:
        """获取从根到某节点的路径上的所有边。

        通过遍历路径中每个节点的parent_edge_key获取。
        """
        path_nodes = self.get_path_nodes(node_key)
        edges = []
        for n in path_nodes:
            if n.parent_edge_key:
                e = self.get_edge(n.parent_edge_key)
                if e:
                    edges.append(e)
        return edges
