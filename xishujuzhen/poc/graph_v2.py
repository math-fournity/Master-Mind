"""POC-2 扩展依赖图：12 节点 16 边。

对应 65 号文档 §4 的扩展依赖图设计。
"""

import networkx as nx


def build_graph_v2() -> nx.DiGraph:
    """构建命宫分析的扩展依赖图（12 节点 16 边）。"""
    g = nx.DiGraph()

    # ── 节点（12 个）──────────────────────────────────
    g.add_node("命宫分析", type="step", context="命宫",
               desc="分析任务的入口节点")
    g.add_node("命主星判断", type="substep", context="命宫/命主木星",
               desc="判断命主星（木星）的强弱")
    g.add_node("度主星判断", type="substep", context="命宫/命度尾宿",
               desc="判断度主星（命度所在宿的五行主星）的强弱")
    g.add_node("庙旺平陷", type="意识", context="命宫/星曜庙旺",
               desc="星曜在宫位的庙旺平陷状态判断")
    g.add_node("升殿判断", type="意识", context="命宫/宿位升殿",
               desc="星曜五行与宿五行一致时升殿，力量最强")
    g.add_node("宿位泄气", type="意识", context="命宫/宿位泄气",
               desc="星曜在非本五行宿位时泄气或克宿")
    g.add_node("五行生克", type="意识", context="命宫/五行关系",
               desc="五行生克关系判断（木火土金水）")
    g.add_node("阴阳昼夜", type="意识", context="命宫/昼生",
               desc="昼夜阴阳对星曜强弱的影响")
    g.add_node("恩用仇难定局", type="意识", context="命宫/恩用仇难",
               desc="以命主为核心的生克四分类")
    g.add_node("颠倒颠", type="意识", context="命宫/颠倒颠",
               desc="生太过反为害、煞为权")
    g.add_node("仇难外避分析", type="substep", context="命宫/仇难外避",
               desc="仇星难星不在命宫的影响")
    g.add_node("间接影响分析", type="substep", context="命宫/间接影响",
               desc="命宫外星曜对命宫的间接影响")

    # ── 边（16 条）──────────────────────────────────────
    g.add_edge("命宫分析", "命主星判断", type="depends_on",
               desc="命宫分析需要先判断命主星")
    g.add_edge("命宫分析", "度主星判断", type="depends_on",
               desc="命宫分析需要判断度主星")
    g.add_edge("命宫分析", "庙旺平陷", type="calls",
               desc="命宫分析需要查各星曜庙旺")
    g.add_edge("命宫分析", "仇难外避分析", type="depends_on",
               desc="命宫分析需要检查仇难是否外避")
    g.add_edge("命宫分析", "间接影响分析", type="depends_on",
               desc="命宫分析需要检查宫外星曜间接影响")
    g.add_edge("命主星判断", "庙旺平陷", type="calls",
               desc="命主星强弱需要庙旺判断")
    g.add_edge("命主星判断", "五行生克", type="calls",
               desc="命主星强弱需要五行生克")
    g.add_edge("命主星判断", "恩用仇难定局", type="calls",
               desc="命主星分析需要恩用仇难定局")
    g.add_edge("度主星判断", "升殿判断", type="calls",
               desc="度主星强弱需要升殿判断")
    g.add_edge("度主星判断", "宿位泄气", type="calls",
               desc="度主星在非本五行宿位时需判断泄气")
    g.add_edge("庙旺平陷", "五行生克", type="calls",
               desc="庙旺判断依赖五行（寅属木，木星同宫为庙）")
    g.add_edge("庙旺平陷", "升殿判断", type="calls",
               desc="庙旺判断需要结合升殿")
    g.add_edge("五行生克", "阴阳昼夜", type="calls",
               desc="五行强弱受昼夜影响（昼生木旺）")
    g.add_edge("阴阳昼夜", "五行生克", type="calls",
               desc="昼夜对五行的影响需要回到五行生克判断（螺旋）")
    g.add_edge("恩用仇难定局", "颠倒颠", type="calls",
               desc="恩用仇难需要考虑颠倒颠（生太过反为害）")
    g.add_edge("仇难外避分析", "间接影响分析", type="calls",
               desc="仇难外避后需要分析间接影响")

    return g


def print_graph(g: nx.DiGraph) -> None:
    """打印图的节点和边。"""
    print("=== 节点 ===")
    for n, d in g.nodes(data=True):
        print(f"  {n}  type={d['type']}  context={d['context']}")

    print("\n=== 边 ===")
    for u, v, d in g.edges(data=True):
        print(f"  {u} --{d['type']}--> {v}")

    print(f"\n节点数: {g.number_of_nodes()}  边数: {g.number_of_edges()}")


if __name__ == "__main__":
    g = build_graph_v2()
    print_graph(g)
