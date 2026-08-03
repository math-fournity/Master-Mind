"""POC-2 提示生成：含知识嵌入 + 审计要求。

对应 65 号文档 §5（知识嵌入）和 §6（审计要求）。
"""

import json
import networkx as nx
from typing import Dict, Any, List
from cycle_detect import classify_cycles
from knowledge_content import get_knowledge_content


# study-notes 知识指针映射（保留指针，但主要靠嵌入内容）
KNOWLEDGE_POINTERS = {
    "庙旺平陷": "study-notes/08-状态判断.md",
    "升殿判断": "study-notes/08-状态判断.md",
    "宿位泄气": "study-notes/08-状态判断.md",
    "五行生克": "study-notes/星学意识/01-五行生克意识.md",
    "阴阳昼夜": "study-notes/星学意识/（待建）阴阳昼夜.md",
    "恩用仇难定局": "study-notes/星学意识/01-五行生克意识.md",
    "颠倒颠": "study-notes/星学意识/01-五行生克意识.md",
}


def graph_to_json_v2(g: nx.DiGraph, start_node: str,
                     chart_data: Dict[str, Any]) -> Dict[str, Any]:
    """把扩展依赖图 + 星盘数据 + 知识嵌入 + 审计要求转为 AI 可读的提示 JSON。"""

    cycles = classify_cycles(g)

    # 节点列表（含知识内容嵌入）
    nodes = []
    for n, d in g.nodes(data=True):
        node_entry = {
            "id": n,
            "type": d.get("type", ""),
            "context": d.get("context", ""),
            "desc": d.get("desc", "")
        }
        # 意识节点嵌入知识内容
        if d.get("type") == "意识":
            kc = get_knowledge_content(n)
            if kc:
                node_entry["knowledge_content"] = kc
            ptr = KNOWLEDGE_POINTERS.get(n)
            if ptr:
                node_entry["knowledge_pointer"] = ptr
        nodes.append(node_entry)

    # 边列表
    edges = []
    for u, v, d in g.edges(data=True):
        edges.append({
            "from": u,
            "to": v,
            "type": d.get("type", ""),
            "desc": d.get("desc", "")
        })

    # 星盘摘要
    chart_summary = _build_chart_summary(chart_data)

    # 分析引导
    guidance = _build_analysis_guidance(g, start_node, cycles)

    # 审计要求
    audit_requirement = {
        "required": True,
        "output_format": "markdown",
        "must_include": {
            "node_coverage": "逐节点列出：节点ID、是否已处理(是/否)、处理时的上下文、产出的中间结论",
            "edge_coverage": "逐边列出：起点、终点、是否沿其思考(是/否)、推理过程简述",
            "cycle_handling": "逐环路列出：环路节点、类型(螺旋/平面)、走了几圈、每圈上下文变化",
            "completeness_statement": "完备性声明：全部覆盖，或列出未覆盖项及原因"
        },
        "output_file": "请将审计结果作为独立的Markdown文件输出，与结果文件配对"
    }

    return {
        "analysis_task": "分析此命的命宫",
        "current_context": "命宫",
        "chart_data": chart_summary,
        "dependency_graph": {
            "nodes": nodes,
            "edges": edges
        },
        "cycles": cycles,
        "analysis_guidance": guidance,
        "audit_requirement": audit_requirement
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
        },
        "星曜宿位": {
            s["星曜"]: s["所在宿"]
            for s in stars_in_mg
        }
    }


def _build_analysis_guidance(g: nx.DiGraph, start_node: str,
                             cycles: List[Dict]) -> str:
    """沿依赖图路径生成分析引导文字。"""
    steps = [
        "请沿依赖图路径分析：",
        "1) 判断命主星木星的庙旺状态（庙旺平陷意识）——寅属木，木星同宫为庙；",
        "2) 判断木星五行强弱（五行生克意识），注意寅属木、木星同宫为比和；",
        "3) 判断度主星（命度在尾宿，度主为火星）的升殿和宿位状态（升殿判断+宿位泄气意识）；",
        "4) 结合昼生条件判断五行强弱（阴阳昼夜意识），昼生木旺——此为螺旋环路的第二圈；",
        "5) 确定恩用仇难定局（恩用仇难定局意识），分析命宫内恩用配置；",
        "6) 考虑颠倒颠（颠倒颠意识）——命主极强时仇星反为激发（煞为权）；",
        "7) 分析仇难外避（仇难外避分析）——仇星金星在卯宫、难星土星在巳宫，皆不在命宫；",
        "8) 分析间接影响（间接影响分析）——命宫外星曜对命宫的间接影响；",
        "9) 综合判断命主星强弱、命宫星曜配置吉凶、命宫整体格局。",
    ]

    for c in cycles:
        if c["type"] == "spiral":
            steps.append(
                f"\n注意：{' → '.join(c['nodes'])} 是螺旋环路，"
                f"第二次调用时在{'、'.join(c['contexts'])}上下文中深化判断，"
                "不是循环论证。请在审计文件中记录两圈的上下文变化。"
            )
        elif c["type"] == "planar":
            steps.append(
                f"\n注意：{' → '.join(c['nodes'])} 是平面环路，"
                f"上下文相同（{c['context']}），"
                "是循环论证，应停止追溯。"
            )

    return "".join(steps)


def generate_prompt_json_v2(g: nx.DiGraph, start_node: str,
                            chart_data: Dict[str, Any]) -> str:
    """生成完整的 POC-2 提示 JSON 字符串。"""
    prompt = graph_to_json_v2(g, start_node, chart_data)
    return json.dumps(prompt, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    from graph_v2 import build_graph_v2

    g = build_graph_v2()
    with open("chart_data.json", "r") as f:
        chart_data = json.load(f)

    prompt_json = generate_prompt_json_v2(g, "命宫分析", chart_data)
    print(prompt_json)
