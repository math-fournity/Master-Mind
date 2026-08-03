"""环检测与分类：平面环路 vs 螺旋环路。

对应 63 号文档 §四延伸的 classify_cycles 算法，
以及 64 号文档 §4.2 的实现。
"""

import networkx as nx
from typing import List, Dict, Any


def classify_cycles(g: nx.DiGraph) -> List[Dict[str, Any]]:
    """检测有向图中的所有环路，并分类为平面环路或螺旋环路。

    判别标准（来自 63 号文档）：
    - 平面环路：SCC 内所有节点上下文相同 → 循环论证，应停止
    - 螺旋环路：SCC 内节点上下文不同 → 深化分析，应继续

    Returns:
        环路列表，每个环路是一个 dict：
        - type: 'planar' | 'spiral'
        - nodes: 环中的节点列表
        - context(s): 环中的上下文
        - note: 说明文字
    """
    sccs = list(nx.strongly_connected_components(g))
    cycles = []

    for scc in sccs:
        # 单节点无自环的 SCC 不是环
        if len(scc) < 2:
            # 检查是否有自环
            has_self_loop = any(g.has_edge(n, n) for n in scc)
            if not has_self_loop:
                continue

        nodes = list(scc)
        contexts = {g.nodes[n].get('context', '') for n in scc}

        if len(contexts) <= 1:
            cycles.append({
                'type': 'planar',
                'nodes': nodes,
                'context': contexts.pop() if contexts else '',
                'note': '平面环路：同一上下文中的循环，循环论证，应停止追溯'
            })
        else:
            cycles.append({
                'type': 'spiral',
                'nodes': nodes,
                'contexts': sorted(contexts),
                'note': '螺旋环路：跨上下文的深化，应继续追溯。'
                        f'上下文变化：{" → ".join(sorted(contexts))}'
            })

    return cycles


def print_cycles(cycles: List[Dict[str, Any]]) -> None:
    """打印环路检测结果。"""
    if not cycles:
        print("未检测到环路。")
        return

    for i, c in enumerate(cycles):
        print(f"\n--- 环路 {i+1} ---")
        print(f"  类型: {c['type']}")
        print(f"  节点: {c['nodes']}")
        if c['type'] == 'planar':
            print(f"  上下文: {c['context']}")
        else:
            print(f"  上下文: {c['contexts']}")
        print(f"  说明: {c['note']}")


if __name__ == "__main__":
    from graph import build_graph

    g = build_graph()
    cycles = classify_cycles(g)
    print_cycles(cycles)
