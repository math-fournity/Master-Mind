"""tree_store.py单元测试（in_memory模式）。"""

import sys
import os
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, str(REPO_ROOT))

from xishujuzhen.research_runtime.tree_engine.tree_store import (
    TreeStore, TreeNode, TreeEdge, AIInstance,
)


def test_create_problem_and_root():
    """创建题目时自动创建根节点。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "求x^2+1=0的解")

    assert root_key, "root_key should not be empty"

    problem = store.get_problem("test_problem")
    assert problem is not None
    assert problem["problem_text"] == "求x^2+1=0的解"
    assert problem["status"] == "growing"
    assert problem["root_node_key"] == root_key
    assert problem["total_nodes"] == 1

    root = store.get_node(root_key)
    assert root is not None
    assert root.node_type == "root"
    assert root.depth == 0
    assert root.path_from_root == [root_key]
    assert root.situation_text == "求x^2+1=0的解"

    print("✅ test_create_problem_and_root")


def test_add_node_and_edge():
    """添加子节点和边，验证path_from_root。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "题目")

    # 添加边 root → child
    edge = TreeEdge(
        problem_id="test_problem",
        _from=f"tree_nodes/{root_key}",
        _to="",  # 先创建边再设_to
        hint_q="考虑复数解",
        ai_instance_id="ai_1",
    )
    edge_key = store.add_edge("test_problem", edge)

    # 添加子节点
    child = TreeNode(
        problem_id="test_problem",
        node_type="internal",
        situation={"V_t": ["x=i"], "O_t": []},
        situation_text="发现复数解x=i",
        parent_edge_key=edge_key,
        created_by_ai="ai_1",
    )
    child_key = store.add_node("test_problem", child)

    # 更新边的_to
    edge._to = f"tree_nodes/{child_key}"
    store._memory["tree_edges"][edge_key]["_to"] = edge._to

    # 验证
    child_node = store.get_node(child_key)
    assert child_node is not None
    assert child_node.depth == 1
    assert child_node.path_from_root == [root_key, child_key]

    problem = store.get_problem("test_problem")
    assert problem["total_nodes"] == 2
    assert problem["total_edges"] == 1

    print("✅ test_add_node_and_edge")


def test_path_query():
    """测试路径查询：get_path_from_root / get_path_nodes / get_path_edges。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "题目")

    # 构建三层树：root → n1 → n2
    edge1 = TreeEdge(problem_id="test_problem", _from=f"tree_nodes/{root_key}", hint_q="Q1", ai_instance_id="ai_1")
    ek1 = store.add_edge("test_problem", edge1)

    n1 = TreeNode(problem_id="test_problem", situation_text="节点1", parent_edge_key=ek1, created_by_ai="ai_1")
    nk1 = store.add_node("test_problem", n1)
    store._memory["tree_edges"][ek1]["_to"] = f"tree_nodes/{nk1}"

    edge2 = TreeEdge(problem_id="test_problem", _from=f"tree_nodes/{nk1}", hint_q="Q2", ai_instance_id="ai_2")
    ek2 = store.add_edge("test_problem", edge2)

    n2 = TreeNode(problem_id="test_problem", situation_text="节点2", parent_edge_key=ek2, created_by_ai="ai_2")
    nk2 = store.add_node("test_problem", n2)
    store._memory["tree_edges"][ek2]["_to"] = f"tree_nodes/{nk2}"

    # 测试路径查询
    path = store.get_path_from_root(nk2)
    assert path == [root_key, nk1, nk2], f"Expected [root, n1, n2], got {path}"

    nodes = store.get_path_nodes(nk2)
    assert len(nodes) == 3
    assert nodes[0].node_type == "root"
    assert nodes[1].situation_text == "节点1"
    assert nodes[2].situation_text == "节点2"

    edges = store.get_path_edges(nk2)
    assert len(edges) == 2
    assert edges[0].hint_q == "Q1"
    assert edges[1].hint_q == "Q2"

    print("✅ test_path_query")


def test_ai_instance():
    """测试AI实例注册和更新。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "题目")

    ai = AIInstance(
        problem_id="test_problem",
        entry_node_key=root_key,
        hint_q="",
        tmux_session="harness-test-1",
        trajectory_dir="/tmp/test",
    )
    ai_key = store.register_ai(ai)
    assert ai_key

    ai_loaded = store.get_ai(ai_key)
    assert ai_loaded is not None
    assert ai_loaded.status == "running"
    assert ai_loaded.tmux_session == "harness-test-1"

    # 更新状态
    store.update_ai_status(ai_key, "completed", end_reason="token_limit", nodes_contributed=["n1", "n2"])
    ai_updated = store.get_ai(ai_key)
    assert ai_updated.status == "completed"
    assert ai_updated.end_reason == "token_limit"
    assert ai_updated.nodes_contributed == ["n1", "n2"]
    assert ai_updated.ended_at > 0

    # 验证题目计数器
    problem = store.get_problem("test_problem")
    assert problem["ai_instances_used"] == 1

    print("✅ test_ai_instance")


def test_get_growing_nodes():
    """测试获取growing状态节点。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "题目")

    # root是growing
    growing = store.get_growing_nodes("test_problem")
    assert len(growing) == 1
    assert growing[0]._key == root_key

    # 添加一个completed节点
    n1 = TreeNode(problem_id="test_problem", status="completed", parent_edge_key=None, created_by_ai="ai_1")
    nk1 = store.add_node("test_problem", n1)

    growing = store.get_growing_nodes("test_problem")
    assert len(growing) == 1  # 只有root还是growing

    # 把root标记为completed
    store.update_node_status(root_key, "completed")
    growing = store.get_growing_nodes("test_problem")
    assert len(growing) == 0

    print("✅ test_get_growing_nodes")


def test_get_child_edges():
    """测试获取子边。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "题目")

    # 添加两条从root出发的边
    e1 = TreeEdge(problem_id="test_problem", _from=f"tree_nodes/{root_key}", hint_q="Q1", ai_instance_id="ai_1")
    ek1 = store.add_edge("test_problem", e1)

    e2 = TreeEdge(problem_id="test_problem", _from=f"tree_nodes/{root_key}", hint_q="Q2", ai_instance_id="ai_2")
    ek2 = store.add_edge("test_problem", e2)

    children = store.get_child_edges(root_key)
    assert len(children) == 2
    hints = {e.hint_q for e in children}
    assert hints == {"Q1", "Q2"}

    print("✅ test_get_child_edges")


def test_update_node():
    """测试通用节点更新。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "题目")

    store.update_node(root_key, {
        "retrieval_done": True,
        "directions_identified": ["Q1", "Q3"],
    })

    node = store.get_node(root_key)
    assert node.retrieval_done == True
    assert node.directions_identified == ["Q1", "Q3"]

    print("✅ test_update_node")


if __name__ == "__main__":
    test_create_problem_and_root()
    test_add_node_and_edge()
    test_path_query()
    test_ai_instance()
    test_get_growing_nodes()
    test_get_child_edges()
    test_update_node()
    print("\n全部测试通过 ✅")
