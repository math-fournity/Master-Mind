"""POC-7 提示生成：12限全量+动态螺旋环路+交叉审计。"""

import json
import networkx as nx
from typing import Dict, Any, List
from graph_v7 import build_graph_v7, LIMITS_12
from knowledge_content_v7 import get_knowledge_content
from cycle_detect import classify_cycles


def _node_to_dict(n: str, d: dict) -> dict:
    """将节点转为JSON字典。"""
    node_dict = {
        "id": n,
        "type": d.get("type", ""),
        "context": d.get("context", ""),
    }
    if "desc" in d:
        node_dict["desc"] = d["desc"]
    kc = get_knowledge_content(n)
    if kc:
        node_dict["knowledge_content"] = kc
    return node_dict


def _edge_to_dict(u: str, v: str, d: dict) -> dict:
    """将边转为JSON字典。"""
    edge_dict = {"from": u, "to": v, "type": d.get("type", "")}
    if "desc" in d:
        edge_dict["desc"] = d["desc"]
        if d["desc"].startswith("跨宫"):
            edge_dict["cross_palace"] = True
    return edge_dict


def graph_to_json_v7(g: nx.DiGraph, start_node: str,
                     chart_data: Dict[str, Any]) -> Dict[str, Any]:
    """生成POC-7提示JSON。"""
    nodes = [_node_to_dict(n, d) for n, d in g.nodes(data=True)]
    edges = [_edge_to_dict(u, v, d) for u, v, d in g.edges(data=True)]

    cross_count = sum(1 for e in edges if e.get("cross_palace"))
    kc_count = sum(1 for n in nodes if "knowledge_content" in n)

    cycles = classify_cycles(g)
    cycles_list = []
    for c in cycles:
        cycles_list.append({
            "type": c.get("type", "unknown"),
            "nodes": c.get("nodes", []),
            "contexts": [g.nodes[n].get("context", "") for n in c.get("nodes", [])]
        })

    prompt = {
        "chart_summary": {
            "命主": "1985年3月15日 06:00（卯时），昼生",
            "命宫": "寅，木，宫主木星",
            "官禄宫": "亥，木，宫主木星（命官同主），空宫",
            "当前年龄": "35岁（2020年）",
            "分析范围": "静态分析（命宫+官禄宫）+ 12限全量动态分析",
        },
        "dependency_graph": {
            "nodes": nodes,
            "edges": edges,
            "stats": {
                "total_nodes": g.number_of_nodes(),
                "total_edges": g.number_of_edges(),
                "cross_palace_edges": cross_count,
                "knowledge_content_nodes": kc_count,
            }
        },
        "cycles": cycles_list,
        "analysis_guidance": {
            "start_node": start_node,
            "analysis_type": "静态分析（命宫+官禄宫）+ 12限全量动态分析",
            "key_points": [
                "命主木星三得俱全极强——全盘核心基调",
                "命官同主——命强官强",
                "12限全量分析——逐限判断限宫主、限内星曜、限运吉凶",
                "动态螺旋环路——限运吉凶→回溯命主→修正限运（走三圈）",
                "颠倒颠跨宫传递——命主极强则凶限均为可承之凶",
                "8条跨宫依赖边（4静态跨宫+2静态→动态跨宫+2动态螺旋跨宫）",
            ],
        },
        "cross_audit_requirement": {
            "required": True,
            "audit_type": "交叉审计——由独立审计AI审计大师提示词的转译忠实性",
            "audit_subject": "大师提示词（解读AI的输出）",
            "audit_baseline": "此JSON（依赖图+星盘数据+知识嵌入）",
            "audit_executor": "独立审计AI实例",
            "must_include": {
                "node_coverage": "逐节点列出是否已解读",
                "edge_coverage": "逐边列出是否已解读",
                "cross_palace_coverage": "逐条跨宫边列出是否已解读",
                "cycle_coverage": "环路是否已解读，几圈上下文变化",
                "knowledge_content_embedding": "逐个含knowledge_content的节点检查嵌入",
                "constraint_adherence": "是否添加未有的节点/边，是否跳过",
            },
        },
        "execution_audit_requirement": {
            "required": True,
            "must_include": {
                "node_coverage": "逐节点列出是否已处理",
                "edge_coverage": "逐边列出是否沿其思考",
                "cycle_coverage": "螺旋环路走了几圈",
                "cross_palace_coverage": "逐条跨宫边列出是否传递",
                "path_faithfulness": "对照大师提示词逐点验证",
            },
        },
        "workflow": {
            "step_1": "系统已生成此JSON",
            "step_2a": "解读AI解读此JSON，输出大师级提示词",
            "step_2b": "审计AI交叉审计，输出交叉审计报告",
            "step_3": "AI在此JSON+大师提示词下分析，输出结果+审计报告",
        },
    }

    return prompt


def generate_prompt_json_v7(g: nx.DiGraph, start_node: str,
                            chart_data: Dict[str, Any]) -> str:
    prompt = graph_to_json_v7(g, start_node, chart_data)
    return json.dumps(prompt, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    g = build_graph_v7()
    prompt_json = generate_prompt_json_v7(g, "命宫分析", {})
    print(f"JSON长度: {len(prompt_json)} 字符")
