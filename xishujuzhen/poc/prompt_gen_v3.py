"""POC-3 提示生成：含 interpretation_requirement（AI 自解读要求）。

对应 66 号文档 §4 的三步流程设计。
在 POC-2 的基础上新增 interpretation_requirement 字段，
要求 AI 在分析前先输出解读文件（大师级提示词）。
"""

import json
import networkx as nx
from typing import Dict, Any, List
from cycle_detect import classify_cycles
from knowledge_content import get_knowledge_content
from prompt_gen_v2 import (
    KNOWLEDGE_POINTERS,
    _build_chart_summary,
    _build_analysis_guidance,
)


def graph_to_json_v3(g: nx.DiGraph, start_node: str,
                     chart_data: Dict[str, Any]) -> Dict[str, Any]:
    """把扩展依赖图 + 星盘数据 + 知识嵌入 + 审计要求 + 解读要求转为 AI 可读的提示 JSON。"""

    # 复用 POC-2 的基础结构
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

    # 分析引导（复用 POC-2）
    guidance = _build_analysis_guidance(g, start_node, cycles)

    # 审计要求（扩展：双重对照）
    audit_requirement = {
        "required": True,
        "output_format": "markdown",
        "must_include": {
            "json_coverage": {
                "node_coverage": "逐节点列出：节点ID、是否已处理(是/否)、处理时的上下文、产出的中间结论",
                "edge_coverage": "逐边列出：起点、终点、是否沿其思考(是/否)、推理过程简述",
                "cycle_handling": "逐环路列出：环路节点、类型(螺旋/平面)、走了几圈、每圈上下文变化",
                "completeness_statement": "JSON覆盖完备性声明：全部覆盖，或列出未覆盖项及原因"
            },
            "prompt_fidelity": {
                "path_fidelity_table": "对照大师型提示词中的引导点，逐点列出：引导位置、是否循其引导(是/否)、实际思考过程",
                "fidelity_statement": "思考路径忠实性声明：引导点总数、已循其引导的点数、未循其引导的点（列出并说明原因）"
            }
        },
        "output_file": "请将审计结果作为独立的Markdown文件输出，与结果文件配对"
    }

    # 解读要求（新增：AI 自解读）
    interpretation_requirement = {
        "required": True,
        "output_format": "markdown",
        "output_file": "请将解读结果作为独立的Markdown文件输出，在结果文件和审计文件之前",
        "must_include": {
            "node_interpretation": "逐节点解读：这个节点是什么意思？在这个上下文中要判断什么？",
            "edge_interpretation": "逐边解读：为什么从这个节点到那个节点？这条依赖关系的命理含义是什么？",
            "cycle_interpretation": "逐环路解读：这个螺旋环路意味着什么？第一圈和第二圈的上下文变化在命理上代表什么深化？",
            "overall_interpretation": "整体解读：把所有依赖关系串成一条思维路径，用占星大师的语言循循善诱地引导"
        },
        "style_requirement": {
            "goal": "把生硬的依赖图JSON转译为占星大师级别的循循善诱提示词",
            "self_addressed": "这份提示词是AI自己写给自己的——用最适合自己的引导方式表达",
            "not_a_checklist": "不是清单（'第一步、第二步……'），是带着走的引导（'你看……我们要先……但还不够……'）",
            "embed_knowledge": "在引导中自然嵌入knowledge_content中的命理知识",
            "explain_dependencies": "解释为什么有这条依赖边——为什么从这一步到下一步"
        },
        "constraint": {
            "no_modification": "解读时不能改变JSON中的依赖关系——不能添加JSON中没有的节点或边，不能跳过JSON中的任何节点或边",
            "transcription_not_creation": "解读是转译，不是创造",
            "missing_dimensions": "如果发现JSON缺少了某些应该有的依赖，在解读末尾标注'依赖图中未覆盖但可能需要的分析维度'，不自行添加"
        }
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
        "interpretation_requirement": interpretation_requirement,
        "audit_requirement": audit_requirement,
        "workflow": {
            "step_1": "系统已生成此JSON（经典计算，无AI参与）",
            "step_2": "AI解读此JSON，输出大师级提示词Markdown文档（interpretation_requirement）",
            "step_3": "AI在此JSON + 大师级提示词的共同提示下分析，输出结果文件 + 审计文件（audit_requirement）",
            "note": "JSON是审计基准（客观，可逐项核对）。大师型提示词是引导（循循善诱，自然语言）。两者缺一不可。"
        }
    }


def generate_prompt_json_v3(g: nx.DiGraph, start_node: str,
                            chart_data: Dict[str, Any]) -> str:
    """生成完整的 POC-3 提示 JSON 字符串。"""
    prompt = graph_to_json_v3(g, start_node, chart_data)
    return json.dumps(prompt, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    from graph_v2 import build_graph_v2

    g = build_graph_v2()
    with open("chart_data.json", "r") as f:
        chart_data = json.load(f)

    prompt_json = generate_prompt_json_v3(g, "命宫分析", chart_data)
    print(prompt_json)
