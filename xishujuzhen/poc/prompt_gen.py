"""提示生成：把依赖子图转为 AI 可读的 JSON 提示。

对应 64 号文档 §5 的提示生成方案。
"""

import json
import networkx as nx
from typing import Dict, Any, List
from cycle_detect import classify_cycles


# study-notes 知识指针映射
KNOWLEDGE_POINTERS = {
    "庙旺平陷": "study-notes/08-状态判断.md",
    "五行生克": "study-notes/星学意识/五行生克.md",
    "阴阳昼夜": "study-notes/星学意识/阴阳昼夜.md",
}


def extract_subgraph(g: nx.DiGraph, start_node: str,
                     max_depth: int = 3) -> nx.DiGraph:
    """从起始节点出发，BFS 遍历提取依赖子图。

    POC 图很小（5 节点），max_depth=3 覆盖全图。
    """
    # BFS 前驱树（沿边方向遍历依赖）
    bfs_tree = nx.bfs_tree(g, start_node, depth_limit=max_depth)
    # 提取子图（保留所有元数据）
    sub_nodes = set(bfs_tree.nodes) | {start_node}
    # 对于环路，需要把环路中的所有边都包含进来
    # BFS 树不包含回边，所以从原图中补全
    sub = g.subgraph(sub_nodes).copy()
    return sub


def graph_to_json(g: nx.DiGraph, start_node: str,
                  chart_data: Dict[str, Any]) -> Dict[str, Any]:
    """把依赖图 + 星盘数据转为 AI 可读的提示 JSON。"""

    cycles = classify_cycles(g)

    # 节点列表
    nodes = []
    for n, d in g.nodes(data=True):
        nodes.append({
            "id": n,
            "type": d.get("type", ""),
            "context": d.get("context", ""),
            "desc": d.get("desc", "")
        })

    # 边列表
    edges = []
    for u, v, d in g.edges(data=True):
        edges.append({
            "from": u,
            "to": v,
            "type": d.get("type", ""),
            "desc": d.get("desc", "")
        })

    # 知识指针
    pointers = {}
    for n in g.nodes():
        if g.nodes[n].get("type") == "意识":
            ptr = KNOWLEDGE_POINTERS.get(n)
            if ptr:
                pointers[n] = ptr

    # 分析引导（沿依赖路径）
    guidance = _build_analysis_guidance(g, start_node, cycles)

    # 星盘摘要（精简版）
    chart_summary = _build_chart_summary(chart_data)

    return {
        "analysis_task": "分析此命的命宫",
        "current_context": "命宫",
        "chart_data": chart_summary,
        "dependency_graph": {
            "nodes": nodes,
            "edges": edges
        },
        "cycles": cycles,
        "knowledge_pointers": pointers,
        "analysis_guidance": guidance
    }


def _build_chart_summary(chart_data: Dict[str, Any]) -> Dict[str, Any]:
    """从 chart_data.json 构建精简的星盘摘要。"""
    mg = chart_data["命宫"]
    stars_in_mg = [s for s in chart_data["命宫星曜"] if s["在命宫"]]

    return {
        "命宫地支": mg["地支"],
        "命宫五行": mg["五行"],
        "命宫主星": mg["宫主"],
        "命宫星曜": [s["星曜"] for s in stars_in_mg],
        "昼生": chart_data["命主信息"]["昼生"],
        "庙旺状态": {
            s["星曜"]: {
                "状态": s["庙旺状态"],
                "依据": s["庙旺依据"]
            }
            for s in stars_in_mg
        }
    }


def _build_analysis_guidance(g: nx.DiGraph, start_node: str,
                             cycles: List[Dict]) -> str:
    """沿依赖图路径生成分析引导文字。"""
    steps = [
        "请沿依赖图路径分析：",
        "1) 先判断命主星木星的庙旺状态（庙旺平陷意识）——寅属木，木星同宫为庙；",
        "2) 判断木星五行强弱（五行生克意识），注意寅属木、木星同宫；",
        "3) 结合昼生条件判断五行强弱（阴阳昼夜意识），昼生木旺；",
        "4) 综合判断命主星强弱；",
        "5) 判断命宫其他星曜（太阳、月亮、火星、水星）的庙旺和配置吉凶；",
        "6) 综合判断命宫整体格局。",
    ]

    # 环路提示
    for c in cycles:
        if c["type"] == "spiral":
            steps.append(
                f"\n注意：{' → '.join(c['nodes'])} 是螺旋环路，"
                f"第二次调用时在{'、'.join(c['contexts'])}上下文中深化判断，"
                "不是循环论证。"
            )
        elif c["type"] == "planar":
            steps.append(
                f"\n注意：{' → '.join(c['nodes'])} 是平面环路，"
                f"上下文相同（{c['context']}），"
                "是循环论证，应停止追溯。"
            )

    return "".join(steps)


def generate_prompt_json(g: nx.DiGraph, start_node: str,
                         chart_data: Dict[str, Any]) -> str:
    """生成完整的提示 JSON 字符串。"""
    prompt = graph_to_json(g, start_node, chart_data)
    return json.dumps(prompt, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '.')

    from graph import build_graph

    g = build_graph()
    with open("chart_data.json", "r") as f:
        chart_data = json.load(f)

    prompt_json = generate_prompt_json(g, "命宫分析", chart_data)
    print(prompt_json)
