"""构建 POC 最小依赖图。

5 个知识节点 + 7 条依赖边 + 1 个螺旋环路。
对应 64 号文档 §3 中的原型范围。
"""

import networkx as nx


def build_graph() -> nx.DiGraph:
    """构建命宫分析的最小依赖图。"""
    g = nx.DiGraph()

    # ── 节点（带元数据）──────────────────────────────
    g.add_node("命宫分析", type="step", context="命宫",
               desc="分析任务的入口节点")
    g.add_node("命主星判断", type="substep", context="命宫/命主木星",
               desc="判断命主星（木星）的强弱")
    g.add_node("庙旺平陷", type="意识", context="命宫/星曜庙旺",
               desc="星曜在宫位的庙旺平陷状态判断")
    g.add_node("五行生克", type="意识", context="命宫/五行关系",
               desc="五行生克关系判断（木火土金水）")
    g.add_node("阴阳昼夜", type="意识", context="命宫/昼生",
               desc="昼夜阴阳对星曜强弱的影响")

    # ── 边（带依赖类型）──────────────────────────────
    g.add_edge("命宫分析", "命主星判断", type="depends_on",
               desc="命宫分析需要先判断命主星")
    g.add_edge("命宫分析", "庙旺平陷", type="calls",
               desc="命宫分析需要查各星曜庙旺")
    g.add_edge("命主星判断", "庙旺平陷", type="calls",
               desc="命主星强弱需要庙旺判断")
    g.add_edge("命主星判断", "五行生克", type="calls",
               desc="命主星强弱需要五行生克")
    g.add_edge("庙旺平陷", "五行生克", type="calls",
               desc="庙旺判断本身依赖五行（寅属木，木星同宫为庙）")
    g.add_edge("五行生克", "阴阳昼夜", type="calls",
               desc="五行强弱受昼夜影响（昼生木旺）")
    g.add_edge("阴阳昼夜", "五行生克", type="calls",
               desc="昼夜对五行的影响需要回到五行生克判断")

    return g


def print_graph(g: nx.DiGraph) -> None:
    """打印图的节点和边，用于调试。"""
    print("=== 节点 ===")
    for n, d in g.nodes(data=True):
        print(f"  {n}  type={d['type']}  context={d['context']}")

    print("\n=== 边 ===")
    for u, v, d in g.edges(data=True):
        print(f"  {u} --{d['type']}--> {v}")

    print(f"\n节点数: {g.number_of_nodes()}  边数: {g.number_of_edges()}")


if __name__ == "__main__":
    g = build_graph()
    print_graph(g)
