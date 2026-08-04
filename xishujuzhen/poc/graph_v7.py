"""POC-7 扩展依赖图：静态分析（19节点）+ 12限全量分析（52节点）= 71节点，~103边，含动态螺旋环路。

在POC-5的graph_v5基础上：
- 静态分析部分不变（19节点25边+4静态跨宫边）
- 动态分析从当前单限扩展到12限全量
- 新增动态螺旋环路（限运吉凶→限运回溯命主→限运修正→限运吉凶）
"""

import networkx as nx
from graph_v4 import build_graph_v4


# 12限框架数据
LIMITS_12 = [
    {"idx": 0, "age": "0-9", "palace": "寅", "name": "命宫", "element": "木", "lord": "木星",
     "stars": ["木星", "太阳", "月亮", "火星", "水星"]},
    {"idx": 1, "age": "9-19", "palace": "卯", "name": "财帛宫", "element": "火", "lord": "火星",
     "stars": ["金星"]},
    {"idx": 2, "age": "19-30", "palace": "辰", "name": "兄弟宫", "element": "金", "lord": "金星",
     "stars": []},
    {"idx": 3, "age": "30-45", "palace": "巳", "name": "田宅宫", "element": "水", "lord": "水星",
     "stars": ["土星", "罗睺"]},
    {"idx": 4, "age": "45-55", "palace": "午", "name": "男女宫", "element": "火", "lord": "火星",
     "stars": []},
    {"idx": 5, "age": "55-62", "palace": "未", "name": "奴仆宫", "element": "水", "lord": "水星",
     "stars": []},
    {"idx": 6, "age": "62-68", "palace": "申", "name": "夫妻宫", "element": "水", "lord": "水星",
     "stars": []},
    {"idx": 7, "age": "68-73", "palace": "酉", "name": "疾厄宫", "element": "金", "lord": "金星",
     "stars": []},
    {"idx": 8, "age": "73-77", "palace": "戌", "name": "迁移宫", "element": "火", "lord": "火星",
     "stars": []},
    {"idx": 9, "age": "77-80", "palace": "亥", "name": "官禄宫", "element": "木", "lord": "木星",
     "stars": []},
    {"idx": 10, "age": "80-83", "palace": "子", "name": "福德宫", "element": "土", "lord": "土星",
     "stars": []},
    {"idx": 11, "age": "83-86", "palace": "丑", "name": "相貌宫", "element": "土", "lord": "土星",
     "stars": ["计都"]},
]


def build_graph_v7() -> nx.DiGraph:
    """构建POC-7扩展依赖图：静态+12限全量+动态螺旋，71节点~103边。"""
    # 先构建POC-4的静态分析图（19节点25边）
    g = build_graph_v4()

    # ===== 动态分析节点 =====

    # 大限框架（1个）
    g.add_node("大限框架计算", type="step", context="大限",
               desc="计算12限框架，童限9年，从命宫寅起顺行")

    # 逐限分析节点（12限×4子节点=48个）
    for lim in LIMITS_12:
        idx = lim["idx"]
        suffix = f"_{idx}"

        g.add_node(f"限{idx}_宫位判断", type="substep", context=f"大限/第{idx}限",
                   desc=f"第{idx}限({lim['age']}岁)落在{lim['palace']}宫({lim['name']}),五行{lim['element']}")
        g.add_node(f"限{idx}_宫主判断", type="substep", context=f"大限/第{idx}限",
                   desc=f"第{idx}限宫主为{lim['lord']}")
        g.add_node(f"限{idx}_星曜配置", type="substep", context=f"大限/第{idx}限",
                   desc=f"第{idx}限内星曜: {lim['stars'] if lim['stars'] else '无(空宫)'}")
        g.add_node(f"限{idx}_吉凶判断", type="substep", context=f"大限/第{idx}限",
                   desc=f"第{idx}限限运吉凶初步判断")

    # 动态螺旋环路节点（2个）
    g.add_node("限运回溯命主", type="意识", context="动态螺旋/回溯",
               desc="带着12限初步吉凶回到命主星判断——命主极强则修正凶限为可承之凶，命主弱则修正吉限为虚浮之吉")
    g.add_node("限运修正", type="意识", context="动态螺旋/修正",
               desc="基于命主回溯修正12限吉凶判断——凶限修正为可承/不可承，吉限修正为实吉/虚吉")

    # 限运综合排序（1个）
    g.add_node("限运综合排序", type="substep", context="大限/综合排序",
               desc="12限修正后的综合排序——一生运势走势图")

    # ===== 动态分析边 =====

    # 大限框架→逐限（12条）
    for lim in LIMITS_12:
        idx = lim["idx"]
        g.add_edge("大限框架计算", f"限{idx}_宫位判断", type="depends_on",
                   desc=f"12限框架后判断第{idx}限宫位")

    # 逐限内部边（12限×3=36条）
    for lim in LIMITS_12:
        idx = lim["idx"]
        g.add_edge(f"限{idx}_宫位判断", f"限{idx}_宫主判断", type="depends_on",
                   desc=f"第{idx}限宫位确定后判断宫主")
        g.add_edge(f"限{idx}_宫主判断", f"限{idx}_星曜配置", type="depends_on",
                   desc=f"第{idx}限宫主确定后分析星曜")
        g.add_edge(f"限{idx}_星曜配置", f"限{idx}_吉凶判断", type="depends_on",
                   desc=f"第{idx}限星曜配置后判断吉凶")

    # 逐限→动态螺旋（12条）
    for lim in LIMITS_12:
        idx = lim["idx"]
        g.add_edge(f"限{idx}_吉凶判断", "限运回溯命主", type="calls",
                   desc=f"第{idx}限吉凶判断汇入回溯命主")

    # 动态螺旋环路（2条）★新增
    g.add_edge("限运回溯命主", "限运修正", type="calls",
               desc="回溯命主后修正限运——螺旋第一圈到第二圈")
    g.add_edge("限运修正", "限运回溯命主", type="calls",
               desc="修正后再回溯命主——螺旋第二圈到第三圈（验证修正一致性）")

    # 逐限→综合排序（12条）
    for lim in LIMITS_12:
        idx = lim["idx"]
        g.add_edge(f"限{idx}_吉凶判断", "限运综合排序", type="depends_on",
                   desc=f"第{idx}限吉凶判断汇入综合排序")
    g.add_edge("限运修正", "限运综合排序", type="calls",
               desc="修正后的限运判断汇入综合排序")

    # ===== 静态→动态跨宫依赖边（4条，复用POC-5）=====

    g.add_edge("命主星判断", "限3_宫主判断", type="depends_on",
               desc="跨宫依赖：命主星判断结果决定限宫主判断——限宫主水星是命主木星的恩星（水生木），命主极强则恩星有力")
    g.add_edge("恩用仇难定局", "限3_星曜配置", type="calls",
               desc="跨宫依赖：恩用仇难定局决定限内星曜的吉凶分类——土星是难星（命主能制），罗睺是用星（命主能承泄）")
    g.add_edge("颠倒颠", "限运综合排序", type="calls",
               desc="跨宫依赖：命主极强则能承限内凶星之克（煞为权），颠倒颠传递到12限综合排序")
    g.add_edge("官禄宫分析", "限运综合排序", type="calls",
               desc="跨宫依赖：官禄格局（有实权之象）影响12限综合运势判断")

    # ===== 动态螺旋的静态→动态跨宫边（2条）=====

    g.add_edge("命主星判断", "限运回溯命主", type="calls",
               desc="跨宫依赖：动态螺旋环路回溯到命主星判断——命主极强是修正12限吉凶的根基")
    g.add_edge("颠倒颠", "限运修正", type="calls",
               desc="跨宫依赖：颠倒颠的煞为权原则用于修正12限凶限——命主极强则凶限修正为可承")

    return g


def print_graph_v7(g: nx.DiGraph):
    """打印POC-7扩展依赖图。"""
    print("=== 节点 ===")
    for n, d in g.nodes(data=True):
        ctx = d.get("context", "")
        tag = ""
        if ctx.startswith("跨宫"):
            tag = " [跨宫]"
        elif ctx.startswith("大限") or ctx.startswith("流年") or ctx.startswith("动态螺旋"):
            tag = " [动态]"
        print(f"  {n}  type={d.get('type', '')}  context={ctx}{tag}")

    print(f"\n=== 边 ===")
    for u, v, d in g.edges(data=True):
        cross = " ★跨宫" if d.get("desc", "").startswith("跨宫") else ""
        print(f"  {u} --{d.get('type', '')}--> {v}{cross}")

    cross_count = sum(1 for u, v, d in g.edges(data=True) if d.get("desc", "").startswith("跨宫"))
    print(f"\n节点数: {g.number_of_nodes()}  边数: {g.number_of_edges()}  跨宫边: {cross_count}")


if __name__ == "__main__":
    g = build_graph_v7()
    print_graph_v7(g)
