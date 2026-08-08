#!/usr/bin/env python3
"""
tree_store.py —— 两棵树的ArangoDB存储

按267号设计文档的schema，在ArangoDB中维护：
- tree_nodes：树节点（每个节点=一个数学处境）
- tree_edges：树边（每条边=一个提示Q，引导从一个处境到另一个）
- problems：题目（每道题一棵树）
- ai_instances：推理AI实例

设计原则：
1. 先做最小可用版本——节点/边/题目/AI实例的CRUD
2. 不要求六元组完美——先用situation_text（自然语言描述）代替六元组
3. 边的hint_q先存Pattern的Q字段——后续可以扩展为更丰富的方向描述
4. 每个实验都调用tree_store记录树的生长——边做实验边长树
"""

import os
import time
import json
import uuid
from typing import Optional
from arango import ArangoClient


# ============================================================
# 连接
# ============================================================

def get_db():
    """连接到本repo专用的ArangoDB数据库。"""
    host = os.environ.get('ARANGO_HOST', 'http://localhost:8529')
    db_name = os.environ.get('ARANGO_DB', 'xishujuzhen_math_glm52')
    user = os.environ.get('ARANGO_USER', 'root')
    password = os.environ.get('ARANGO_PASS', 'REDACTED-DB-PASSWORD')
    client = ArangoClient(hosts=host)
    return client.db(db_name, username=user, password=password)


def ensure_collections(db):
    """确保树相关的集合存在。"""
    existing = {c['name'] for c in db.collections() if not c['name'].startswith('_')}

    # document collections
    for name in ['tree_nodes', 'problems', 'ai_instances']:
        if name not in existing:
            db.create_collection(name)
            print(f"  created collection: {name}")

    # edge collections
    if 'tree_edges' not in existing:
        db.create_collection('tree_edges', edge=True)
        print(f"  created edge collection: tree_edges")

    # 索引
    nodes = db.collection('tree_nodes')
    nodes.add_persistent_index(['problem_id'], sparse=False)
    nodes.add_persistent_index(['status'], sparse=False)

    edges = db.collection('tree_edges')
    edges.add_persistent_index(['problem_id'], sparse=False)

    problems = db.collection('problems')
    problems.add_persistent_index(['status'], sparse=False)

    ai = db.collection('ai_instances')
    ai.add_persistent_index(['problem_id'], sparse=False)
    ai.add_persistent_index(['status'], sparse=False)


# ============================================================
# Problem CRUD
# ============================================================

def create_problem(db, problem_id: str, problem_text: str, metadata: dict = None) -> dict:
    """创建一道题（一棵树的根）。"""
    doc = {
        '_key': problem_id,
        'problem_text': problem_text,
        'root_node_key': None,  # 创建根节点后回填
        'status': 'growing',
        'solution_path': [],
        'created_at': time.time(),
        'solved_at': None,
        'total_nodes': 0,
        'total_edges': 0,
        'ai_instances_used': 0,
        'metadata': metadata or {},
    }
    db.collection('problems').insert(doc)
    return doc


def get_problem(db, problem_id: str) -> Optional[dict]:
    try:
        return db.collection('problems').get(problem_id)
    except Exception:
        return None


def update_problem_status(db, problem_id: str, status: str, solution_path: list = None):
    patch = {'status': status}
    if status == 'solved':
        patch['solved_at'] = time.time()
    if solution_path is not None:
        patch['solution_path'] = solution_path
    patch['_key'] = problem_id
    db.collection('problems').update(patch)


# ============================================================
# Node CRUD
# ============================================================

def create_node(db, problem_id: str, node_type: str, situation_text: str,
                depth: int, parent_edge_key: str = None,
                path_from_root: list = None,
                created_by_ai: str = None,
                trajectory_segment: dict = None,
                status: str = 'growing',
                metadata: dict = None) -> dict:
    """创建一个树节点。"""
    node_key = str(uuid.uuid4())[:12]
    doc = {
        '_key': node_key,
        'problem_id': problem_id,
        'node_type': node_type,  # root/internal/leaf_success/leaf_deadend/leaf_truncated
        'situation': metadata or {},  # 后续填六元组
        'situation_text': situation_text,
        'depth': depth,
        'parent_edge_key': parent_edge_key,
        'path_from_root': path_from_root or [node_key],
        'created_by_ai': created_by_ai,
        'created_at': time.time(),
        'trajectory_segment': trajectory_segment or {},
        'status': status,
        'retrieval_done': False,
        'directions_identified': [],
        'ai_instances_started': [],
    }
    db.collection('tree_nodes').insert(doc)

    # 更新problem的node计数
    prob = db.collection('problems').get(problem_id)
    if prob:
        db.collection('problems').update({
            '_key': problem_id,
            'total_nodes': prob.get('total_nodes', 0) + 1
        })

    return doc


def get_node(db, node_key: str) -> Optional[dict]:
    try:
        return db.collection('tree_nodes').get(node_key)
    except Exception:
        return None


def get_tree_nodes(db, problem_id: str) -> list:
    """获取某棵树的所有节点。"""
    aql = "FOR n IN tree_nodes FILTER n.problem_id == @pid SORT n.depth RETURN n"
    return list(db.aql.execute(aql, bind_vars={'pid': problem_id}))


def get_growing_nodes(db, problem_id: str) -> list:
    """获取所有status=growing的节点。"""
    aql = "FOR n IN tree_nodes FILTER n.problem_id == @pid AND n.status == 'growing' RETURN n"
    return list(db.aql.execute(aql, bind_vars={'pid': problem_id}))


def update_node_status(db, node_key: str, status: str, node_type: str = None):
    patch = {'status': status}
    if node_type:
        patch['node_type'] = node_type
    patch['_key'] = node_key
    db.collection('tree_nodes').update(patch)


def mark_retrieval_done(db, node_key: str, directions: list):
    """标记节点已完成检索，记录识别出的方向。"""
    db.collection('tree_nodes').update({
        '_key': node_key,
        'retrieval_done': True,
        'directions_identified': directions,
    })


# ============================================================
# Edge CRUD
# ============================================================

def create_edge(db, problem_id: str, from_key: str, to_key: str,
                hint_q: str, hint_q_id: str = None, hint_level: float = None,
                ai_instance_id: str = None, edge_status: str = 'growing') -> dict:
    """创建一条树边（一个提示Q引导的转移）。"""
    edge_key = str(uuid.uuid4())[:12]
    doc = {
        '_key': edge_key,
        '_from': f'tree_nodes/{from_key}',
        '_to': f'tree_nodes/{to_key}',
        'problem_id': problem_id,
        'hint_q': hint_q,
        'hint_q_id': hint_q_id,
        'hint_level': hint_level,
        'ai_instance_id': ai_instance_id,
        'created_at': time.time(),
        'edge_status': edge_status,
    }
    db.collection('tree_edges').insert(doc)

    # 更新problem的edge计数
    prob = db.collection('problems').get(problem_id)
    if prob:
        db.collection('problems').update({
            '_key': problem_id,
            'total_edges': prob.get('total_edges', 0) + 1
        })

    return doc


def get_tree_edges(db, problem_id: str) -> list:
    """获取某棵树的所有边。"""
    aql = "FOR e IN tree_edges FILTER e.problem_id == @pid RETURN e"
    return list(db.aql.execute(aql, bind_vars={'pid': problem_id}))


# ============================================================
# AI Instance CRUD
# ============================================================

def register_ai_instance(db, ai_id: str, problem_id: str,
                         entry_node_key: str, entry_edge_key: str = None,
                         hint_q: str = None, path_text: str = None,
                         tmux_session: str = None, devin_session_id: str = None,
                         trajectory_dir: str = None) -> dict:
    """注册一个推理AI实例。"""
    doc = {
        '_key': ai_id,
        'problem_id': problem_id,
        'entry_node_key': entry_node_key,
        'entry_edge_key': entry_edge_key,
        '脉络文本': path_text,
        'hint_q': hint_q,
        'tmux_session': tmux_session,
        'devin_session_id': devin_session_id,
        'status': 'running',
        'started_at': time.time(),
        'ended_at': None,
        'end_reason': None,
        'trajectory_dir': trajectory_dir,
        'nodes_contributed': [],
    }
    db.collection('ai_instances').insert(doc)

    # 更新problem的AI计数
    prob = db.collection('problems').get(problem_id)
    if prob:
        db.collection('problems').update({
            '_key': problem_id,
            'ai_instances_used': prob.get('ai_instances_used', 0) + 1
        })

    # 在entry_node上记录AI启动
    node = db.collection('tree_nodes').get(entry_node_key)
    if node:
        ai_list = node.get('ai_instances_started', [])
        ai_list.append(ai_id)
        db.collection('tree_nodes').update({
            '_key': entry_node_key,
            'ai_instances_started': ai_list
        })

    return doc


def update_ai_status(db, ai_id: str, status: str, end_reason: str = None,
                     nodes_contributed: list = None):
    patch = {'status': status}
    if status in ('completed', 'crashed', 'truncated'):
        patch['ended_at'] = time.time()
    if end_reason:
        patch['end_reason'] = end_reason
    if nodes_contributed is not None:
        patch['nodes_contributed'] = nodes_contributed
    patch['_key'] = ai_id
    db.collection('ai_instances').update(patch)


# ============================================================
# 树可视化（调试用）
# ============================================================

def print_tree(db, problem_id: str):
    """打印某棵树的结构。"""
    nodes = get_tree_nodes(db, problem_id)
    edges = get_tree_edges(db, problem_id)
    prob = get_problem(db, problem_id)

    if not prob:
        print(f"problem {problem_id} not found")
        return

    print(f"\n=== Tree: {problem_id} ===")
    print(f"  status: {prob['status']}")
    print(f"  nodes: {len(nodes)}, edges: {len(edges)}")
    print(f"  ai_instances: {prob.get('ai_instances_used', 0)}")

    if prob.get('solution_path'):
        print(f"  solution_path: {' → '.join(prob['solution_path'])}")

    # 构建邻接表
    children = {}
    for e in edges:
        from_key = e['_from'].split('/')[1]
        to_key = e['_to'].split('/')[1]
        if from_key not in children:
            children[from_key] = []
        children[from_key].append((to_key, e.get('hint_q', '?')[:50]))

    # 找根节点
    root = None
    for n in nodes:
        if n['node_type'] == 'root':
            root = n
            break

    if not root:
        print("  NO ROOT NODE")
        return

    # 递归打印
    def print_node(node, indent=0):
        prefix = '  ' * indent
        status_icon = {'growing': '🔄', 'completed': '✅', 'deadend': '❌', 'truncated': '✂️'}
        icon = status_icon.get(node['status'], '?')
        print(f"{prefix}{icon} [{node['_key'][:8]}] d{node['depth']} {node['node_type']} | {node['situation_text'][:60]}")
        for child_key, hint_q in children.get(node['_key'], []):
            child = next((n for n in nodes if n['_key'] == child_key), None)
            if child:
                print(f"{prefix}  └─ ({hint_q})")
                print_node(child, indent + 2)

    print_node(root)


# ============================================================
# 初始化
# ============================================================

def init():
    """初始化树存储——创建集合和索引。"""
    db = get_db()
    print("=== 初始化树存储 ===")
    ensure_collections(db)
    print("=== 初始化完成 ===")
    return db


if __name__ == '__main__':
    init()
