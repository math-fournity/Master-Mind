"""POC-7 执行入口。12限全量+动态螺旋环路+交叉审计。"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from graph_v7 import build_graph_v7, print_graph_v7, LIMITS_12
from cycle_detect import classify_cycles, print_cycles
from prompt_gen_v7 import generate_prompt_json_v7


def main():
    print("=" * 60)
    print("xishujuzhen POC-7 — 12限全量+动态螺旋+交叉审计")
    print("=" * 60)

    # 1. 构建依赖图
    print("\n【1】构建依赖图（12限全量+动态螺旋）\n")
    g = build_graph_v7()
    print_graph_v7(g)

    # 2. 环检测
    print("\n\n【2】环检测与分类\n")
    cycles = classify_cycles(g)
    print_cycles(cycles)

    # 3. 生成B组提示JSON
    print("\n\n【3】生成B组提示JSON\n")
    with open("chart_data_v5.json", "r") as f:
        chart_data = json.load(f)
    prompt_json = generate_prompt_json_v7(g, "命宫分析", chart_data)
    with open("poc7_prompt_b.json", "w") as f:
        f.write(prompt_json)
    print(f"  已保存到 poc7_prompt_b.json（{len(prompt_json)} 字符）")

    # 4. 星盘摘要（复用POC-5）
    print("\n\n【4】星盘摘要（复用POC-5）\n")
    from run_poc5 import _build_chart_summary_text_v5
    chart_summary = _build_chart_summary_text_v5(chart_data)
    with open("poc7_chart_summary.txt", "w") as f:
        f.write(chart_summary)
    print("  已保存到 poc7_chart_summary.txt")

    print("\n\n" + "=" * 60)
    print("POC-7 第一步完成。")
    print("  - poc7_prompt_b.json : B组提示（71节点106边10跨宫，含动态螺旋）")
    print("  - material_a_v5.md   : A组参考材料（知识充分，复用POC-5）")
    print("  - poc7_chart_summary.txt : 星盘摘要")
    print("=" * 60)


if __name__ == "__main__":
    main()
