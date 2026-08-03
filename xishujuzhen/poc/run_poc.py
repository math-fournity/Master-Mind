"""POC 执行入口。

运行后生成：
1. 依赖图可视化（文本）
2. 环检测结果
3. B 组提示 JSON（保存到 prompt_b.json）
4. A 组材料清单（保存到 material_a.txt）

用法：
    cd xishujuzhen/poc
    python3 run_poc.py
"""

import json
import sys
import os

# 确保能 import 同目录模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from graph import build_graph, print_graph
from cycle_detect import classify_cycles, print_cycles
from prompt_gen import generate_prompt_json


def main():
    print("=" * 60)
    print("xishujuzhen POC — 最小依赖图验证")
    print("=" * 60)

    # 1. 构建依赖图
    print("\n【1】构建依赖图\n")
    g = build_graph()
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

    # 4. 生成 B 组提示 JSON
    print("\n\n【4】生成 B 组提示 JSON\n")
    prompt_json = generate_prompt_json(g, "命宫分析", chart_data)

    # 保存
    with open("prompt_b.json", "w") as f:
        f.write(prompt_json)
    print(f"  已保存到 prompt_b.json（{len(prompt_json)} 字符）")

    # 5. 生成 A 组材料清单
    print("\n\n【5】A 组材料清单\n")
    material_a = """# A 组材料（对照组）

A 组 AI 拿到的是 study-notes 中的命宫相关内容，不含依赖图结构。

## 需要提取的 study-notes 内容

以下文件中与命宫分析相关的部分：

1. study-notes/04-安命安身.md — 命宫安法、命主星定义
2. study-notes/08-状态判断.md — 庙旺平陷判断方法
3. study-notes/星学意识/五行生克.md — 五行生克关系（如已存在）
4. study-notes/星学意识/阴阳昼夜.md — 昼夜对星曜强弱的影响（如已存在）

## 提取方式

从上述文件中提取与命宫分析直接相关的段落，拼成一份 Markdown 文档。
不含依赖图结构、不含环路提示、不含分析路径引导。

## A 组 AI 指令

你是一位七政四余星学分析师。请分析以下命盘的命宫。

[星盘摘要]

[study-notes 相关内容]

请给出完整的命宫分析，包括：
- 命主星判断
- 命宫星曜配置吉凶
- 命宫整体格局判断
"""
    with open("material_a.txt", "w") as f:
        f.write(material_a)
    print("  已保存到 material_a.txt")

    # 6. 生成星盘摘要（两组共用）
    print("\n\n【6】星盘摘要（两组共用）\n")
    chart_summary = f"""# 星盘摘要

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
    for s in chart_data["命宫星曜"]:
        chart_summary += f"- {s['星曜']}：黄经{s['黄经']}°，在{s['所在宿']}，庙旺={s['庙旺状态']}（{s['庙旺依据']}）\n"

    chart_summary += "\n## 不在命宫的星曜\n"
    for s in chart_data["不在命宫的星曜"]:
        chart_summary += f"- {s['星曜']}：黄经{s['黄经']}°，在{s['所在宫']}宫\n"

    with open("chart_summary.txt", "w") as f:
        f.write(chart_summary)
    print("  已保存到 chart_summary.txt")

    print("\n\n" + "=" * 60)
    print("POC 材料生成完毕。")
    print("  - chart_summary.txt  : 两组共用的星盘摘要")
    print("  - prompt_b.json      : B 组依赖图提示")
    print("  - material_a.txt     : A 组材料清单")
    print("=" * 60)


if __name__ == "__main__":
    main()
