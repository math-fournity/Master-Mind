"""POC-3 执行入口。

三步流程：
1. 系统生成 JSON（含 interpretation_requirement）
2. AI 解读 JSON → 大师级提示词（subagent 阶段一）
3. AI 在 JSON + 大师级提示词共同提示下分析 → 结果+审计（subagent 阶段二）

用法：
    cd xishujuzhen/poc
    python3 run_poc3.py
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from graph_v2 import build_graph_v2, print_graph
from cycle_detect import classify_cycles, print_cycles
from prompt_gen_v3 import generate_prompt_json_v3
from run_poc2 import _build_chart_summary_text


def main():
    print("=" * 60)
    print("xishujuzhen POC-3 — AI自解读 + 双重提示 + 双重对照审计")
    print("=" * 60)

    # 1. 构建扩展依赖图
    print("\n【1】构建扩展依赖图（复用POC-2，12节点16边）\n")
    g = build_graph_v2()
    print_graph(g)

    # 2. 环检测
    print("\n\n【2】环检测与分类\n")
    cycles = classify_cycles(g)
    print_cycles(cycles)

    # 3. 加载星盘数据
    print("\n\n【3】加载星盘数据\n")
    with open("chart_data.json", "r") as f:
        chart_data = json.load(f)
    print(f"  命宫: {chart_data['命宫']['地支']}（{chart_data['命宫']['五行']}）")
    print(f"  命主: {chart_data['命宫']['宫主']}")
    print(f"  命宫星曜: {[s['星曜'] for s in chart_data['命宫星曜']]}")
    print(f"  昼生: {chart_data['命主信息']['昼生']}")

    # 4. 生成 B 组提示 JSON（含 interpretation_requirement）
    print("\n\n【4】生成 B 组提示 JSON（含 interpretation_requirement）\n")
    prompt_json = generate_prompt_json_v3(g, "命宫分析", chart_data)

    with open("poc3_prompt_b.json", "w") as f:
        f.write(prompt_json)
    print(f"  已保存到 poc3_prompt_b.json（{len(prompt_json)} 字符）")

    # 5. 生成星盘摘要
    print("\n\n【5】星盘摘要（两组共用）\n")
    chart_summary = _build_chart_summary_text(chart_data)
    with open("poc3_chart_summary.txt", "w") as f:
        f.write(chart_summary)
    print("  已保存到 poc3_chart_summary.txt")

    print("\n\n" + "=" * 60)
    print("POC-3 第一步完成：材料生成完毕。")
    print("  - poc3_chart_summary.txt : 两组共用的星盘摘要")
    print("  - poc3_prompt_b.json      : B组提示（含interpretation_requirement）")
    print("")
    print("下一步：")
    print("  阶段一：AI解读JSON → poc3_output_b_interpretation.md")
    print("  阶段二：AI在JSON+大师级提示词共同提示下分析 → result + audit")
    print("  并行：A组分析 → poc3_output_a.md")
    print("=" * 60)


if __name__ == "__main__":
    main()
