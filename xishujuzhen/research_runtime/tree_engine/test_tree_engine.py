"""node_extractor / path_constructor / termination_detector 单元测试。"""

import sys
import os
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, str(REPO_ROOT))

from xishujuzhen.research_runtime.tree_engine.tree_store import (
    TreeStore, TreeNode, TreeEdge, AIInstance,
)
from xishujuzhen.research_runtime.tree_engine.path_constructor import PathConstructor
from xishujuzhen.research_runtime.tree_engine.termination_detector import TerminationDetector


def test_path_constructor():
    """测试脉络构造。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "求x^2+1=0的所有复数解")

    # root → n1 (via edge Q1)
    edge1 = TreeEdge(
        problem_id="test_problem",
        _from=f"tree_nodes/{root_key}",
        hint_q="考虑设x=a+bi并展开",
        ai_instance_id="ai_1",
    )
    ek1 = store.add_edge("test_problem", edge1)

    n1 = TreeNode(
        problem_id="test_problem",
        situation={
            "V_t": [{"description": "x=i是解"}],
            "F_t": ["x^2+1=(x-i)(x+i)"],
            "O_t": [],
            "U_t": [{"description": "需要验证x=-i也是解", "severity": "minor"}],
        },
        situation_text="展开(a+bi)^2+1=0，得到a^2-b^2+2abi+1=0",
        parent_edge_key=ek1,
        created_by_ai="ai_1",
    )
    nk1 = store.add_node("test_problem", n1)
    store._memory["tree_edges"][ek1]["_to"] = f"tree_nodes/{nk1}"

    # 构造脉络
    constructor = PathConstructor(store)
    path_text = constructor.construct_path_text(nk1, "验证x=-i也是解")

    # 验证脉络文本
    assert "求x^2+1=0的所有复数解" in path_text, "应包含题目原文"
    assert "考虑设x=a+bi并展开" in path_text, "应包含提示Q1"
    assert "展开(a+bi)^2+1=0" in path_text, "应包含节点1的处境"
    assert "x=i是解" in path_text, "应包含已证明的结论"
    assert "验证x=-i也是解" in path_text, "应包含方向Q"
    assert "继续推理" in path_text, "应包含继续推理指令"

    print("✅ test_path_constructor")


def test_path_constructor_single_node():
    """测试只有根节点时的脉络构造。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "证明根号2是无理数")

    constructor = PathConstructor(store)
    path_text = constructor.construct_path_text(root_key, "考虑反证法")

    assert "证明根号2是无理数" in path_text
    assert "考虑反证法" in path_text
    assert "初始处境" in path_text

    print("✅ test_path_constructor_single_node")


def test_path_constructor_degraded():
    """测试降级情况（situation_text为空）。"""
    store = TreeStore(in_memory=True)
    root_key = store.create_problem("test_problem", "题目")

    edge1 = TreeEdge(
        problem_id="test_problem",
        _from=f"tree_nodes/{root_key}",
        hint_q="Q1",
        ai_instance_id="ai_1",
    )
    ek1 = store.add_edge("test_problem", edge1)

    # 创建一个situation_text为空的节点，但有trajectory_segment
    n1 = TreeNode(
        problem_id="test_problem",
        situation={},
        situation_text="",  # 空
        parent_edge_key=ek1,
        created_by_ai="ai_1",
        trajectory_segment={"thinking": "这是thinking的降级内容，parser失败了"},
    )
    nk1 = store.add_node("test_problem", n1)
    store._memory["tree_edges"][ek1]["_to"] = f"tree_nodes/{nk1}"

    constructor = PathConstructor(store)
    path_text = constructor.construct_path_text(nk1, "方向Q")

    # 降级时应从trajectory_segment提取
    assert "这是thinking的降级内容" in path_text, "降级时应从trajectory_segment提取"

    print("✅ test_path_constructor_degraded")


def test_termination_detector_session_ended():
    """测试session_ended检测（tmux session不存在）。"""
    detector = TerminationDetector(timeout=1.0)
    # 用一个不存在的session名
    event = detector.check_terminated("nonexistent-session-12345", "nonexistent-exp")
    assert event is not None
    assert event.reason == "session_ended"

    print("✅ test_termination_detector_session_ended")


def test_termination_detector_reset():
    """测试reset方法。"""
    detector = TerminationDetector(timeout=1.0)
    detector._last_thinking_size = 999
    detector._last_thinking_mtime = 12345.0
    detector.reset()
    assert detector._last_thinking_size == 0
    assert detector._last_thinking_mtime == 0.0

    print("✅ test_termination_detector_reset")


if __name__ == "__main__":
    test_path_constructor()
    test_path_constructor_single_node()
    test_path_constructor_degraded()
    test_termination_detector_session_ended()
    test_termination_detector_reset()
    print("\n全部测试通过 ✅")
