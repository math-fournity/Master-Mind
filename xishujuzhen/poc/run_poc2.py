"""POC-2 执行入口。

运行后生成：
1. 扩展依赖图可视化（文本）
2. 环检测结果
3. B 组提示 JSON（含知识嵌入+审计要求，保存到 poc2_prompt_b.json）
4. A 组材料清单

用法：
    cd xishujuzhen/poc
    python3 run_poc2.py
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from graph_v2 import build_graph_v2, print_graph
from cycle_detect import classify_cycles, print_cycles
from prompt_gen_v2 import generate_prompt_json_v2


def main():
    print("=" * 60)
    print("xishujuzhen POC-2 — 扩展依赖图 + 知识嵌入 + 审计要求")
    print("=" * 60)

    # 1. 构建扩展依赖图
    print("\n【1】构建扩展依赖图（12节点16边）\n")
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

    # 4. 生成 B 组提示 JSON（含知识嵌入+审计要求）
    print("\n\n【4】生成 B 组提示 JSON（含知识嵌入+审计要求）\n")
    prompt_json = generate_prompt_json_v2(g, "命宫分析", chart_data)

    with open("poc2_prompt_b.json", "w") as f:
        f.write(prompt_json)
    print(f"  已保存到 poc2_prompt_b.json（{len(prompt_json)} 字符）")

    # 5. 生成星盘摘要
    print("\n\n【5】星盘摘要（两组共用）\n")
    chart_summary = _build_chart_summary_text(chart_data)
    with open("poc2_chart_summary.txt", "w") as f:
        f.write(chart_summary)
    print("  已保存到 poc2_chart_summary.txt")

    print("\n\n" + "=" * 60)
    print("POC-2 材料生成完毕。")
    print("  - poc2_chart_summary.txt : 两组共用的星盘摘要")
    print("  - poc2_prompt_b.json      : B组提示（12节点+知识嵌入+审计要求）")
    print("=" * 60)


def _build_chart_summary_text(chart_data):
    s = f"""# 星盘摘要

## 命主信息
- 公历：{chart_data['命主信息']['公历']}
- 经度：{chart_data['命主信息']['经度']}，纬度：{chart_data['命主信息']['纬度']}
- 昼生：{chart_data['命主信息']['昼生']}

## 命宫
- 地支：{chart_data['命宫']['地支']}
- 五行：{chart_data['命宫']['五行']}
- 宫主：{chart_data['命宫']['宫主']}

## 命宫星曜
"""
    for star in chart_data["命宫星曜"]:
        s += f"- {star['星曜']}：黄经{star['黄经']}°，在{star['所在宿']}，庙旺={star['庙旺状态']}（{star['庙旺依据']}）\n"

    s += "\n## 不在命宫的星曜\n"
    for star in chart_data["不在命宫的星曜"]:
        s += f"- {star['星曜']}：黄经{star['黄经']}°，在{star['所在宫']}宫\n"

    return s


if __name__ == "__main__":
    main()
