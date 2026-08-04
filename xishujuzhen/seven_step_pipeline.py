#!/usr/bin/env python3
"""seven_step_pipeline.py —— 七步骤工作流集成脚本

把七步骤工作流从"手动编排"升级为"脚本化执行"。
步骤2从"meta AI生成G'_topo"升级为"经典计算生成骨架+AI语义细化"。

使用方式：
  # 执行步骤1-3（依赖图导入+经典计算展开+拓扑验证）
  .venv/bin/python3 xishujuzhen/seven_step_pipeline.py --steps 1,2,3

  # 执行步骤1-7完整流程（需要AI参与的步骤会输出提示）
  .venv/bin/python3 xishujuzhen/seven_step_pipeline.py --steps 1,2,3,4,5,6,7

  # 指定源图和目标图
  .venv/bin/python3 xishujuzhen/seven_step_pipeline.py --source dependency_graph --target unfold_topo
"""
import argparse
import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))


def step1_import_graph(sdk, source_graph="dependency_graph"):
    """步骤1：依赖图导入ArangoDB

    前提：dg_nodes/dg_edges/loops已在ArangoDB中（由import_math_graph_to_arangodb.py导入）
    本步骤验证数据完整性。
    """
    print("=" * 60)
    print("步骤1：依赖图导入验证")
    print("=" * 60)

    nodes = list(sdk.db.collection("dg_nodes").all())
    edges = list(sdk.db.collection("dg_edges").all())
    loops = list(sdk.db.collection("loops").find({"graph": source_graph}))

    from collections import Counter
    node_types = Counter(n.get("type", "?") for n in nodes)
    edge_types = Counter(e.get("edge_type", "?") for e in edges)

    print(f"  节点: {len(nodes)}个 ({dict(node_types)})")
    print(f"  边: {len(edges)}条 ({dict(edge_types)})")
    print(f"  螺旋环路: {len(loops)}个")

    # 验证数据完整性
    assert len(nodes) > 0, "dg_nodes为空"
    assert len(edges) > 0, "dg_edges为空"

    print("  ✅ 步骤1完成")
    return {"nodes": len(nodes), "edges": len(edges), "loops": len(loops)}


def step2_generate_g_prime_topo(sdk, target_graph="unfold_topo"):
    """步骤2：经典计算生成G'_topo骨架（L0+L1+L2）+ AI语义细化（L3）

    升级版：topo_generator.py生成骨架，保证全覆盖。
    AI只需在L3阶段做语义标注（section命名、spiral类型确认）。
    """
    print("\n" + "=" * 60)
    print("步骤2：经典计算生成G'_topo骨架")
    print("=" * 60)

    from topo_generator import TopoGenerator
    gen = TopoGenerator()
    ut_nodes, ut_edges, ut_loops = gen.generate(write_to_db=True)

    print(f"  L0骨架: {len(ut_nodes)}节点, {len(ut_edges)}边")
    print(f"  L1类型推断: 完成")
    print(f"  L2 section划分: 完成")

    # L3提示：AI需要做的语义细化
    print("\n  L3语义细化（AI需要做）:")
    print("    - section命名（如'第一章：矩条件与sqrt5下界'）")
    print("    - spiral_static/dynamic最终确认")
    print("    - section边界调整（如需要）")

    # 输出section划分供AI参考
    print("\n  经典计算的section划分推荐:")
    for n in ut_nodes:
        print(f"    [{n['traversal_order']:2d}] {n['node_id']:20s} → {n.get('section', '?')}")

    print("  ✅ 步骤2完成（骨架已生成，L3待AI细化）")
    return {"ut_nodes": len(ut_nodes), "ut_edges": len(ut_edges), "ut_loops": len(ut_loops)}


def step3_topology_verify(sdk):
    """步骤3：TopologyVerifier拓扑覆盖验证

    升级版：经典计算生成的骨架必然1次通过100%覆盖。
    """
    print("\n" + "=" * 60)
    print("步骤3：TopologyVerifier拓扑覆盖验证")
    print("=" * 60)

    from topology_verifier import TopologyVerifier
    tv = TopologyVerifier(db_name="xishujuzhen_math")
    report = tv.verify_all()
    print(report.summary())

    if report.passed:
        print("  ✅ 步骤3完成：1次通过100%覆盖")
    else:
        print("  ❌ 步骤3失败：覆盖不完整")
        print("  注意：经典计算生成的骨架应该1次通过。如果失败，检查topo_generator.py")

    return {"passed": report.passed}


def step4_translate(sdk):
    """步骤4：normal AI按G'_topo转译

    这一步需要AI参与——按G'_topo的结构，把每个节点的知识内容转译为大师提示词。
    脚本只输出提示，不代替AI做转译。
    """
    print("\n" + "=" * 60)
    print("步骤4：normal AI按G'_topo转译")
    print("=" * 60)

    ut_nodes = list(sdk.db.collection("ut_nodes").all())
    ut_nodes.sort(key=lambda n: n.get("traversal_order", 0))

    print(f"  G'_topo有{len(ut_nodes)}个节点需要转译")
    print("  AI需要按traversal_order顺序，为每个节点转译知识内容")
    print("  转译输入：ut_nodes（结构）+ kcs（知识内容）")
    print("  转译输出：大师提示词文本")
    print("  ⏳ 步骤4待AI执行")

    return {"ut_nodes_count": len(ut_nodes)}


def step5_kc_audit(sdk):
    """步骤5：KC忠实审计

    这一步需要meta AI参与——审计步骤4的转译是否忠实于知识内容。
    """
    print("\n" + "=" * 60)
    print("步骤5：KC忠实审计")
    print("=" * 60)
    print("  meta AI需要审计步骤4的转译是否忠实于kcs中的知识内容")
    print("  审计标准：每个节点的转译文本是否包含对应的knowledge_content")
    print("  ⏳ 步骤5待meta AI执行")
    return {}


def step6_analyze(sdk):
    """步骤6：normal AI分析（做数学证明）"""
    print("\n" + "=" * 60)
    print("步骤6：normal AI分析")
    print("=" * 60)
    print("  normal AI在大师提示词引导下做数学证明")
    print("  ⏳ 步骤6待AI执行")
    return {}


def step7_coverage_audit(sdk):
    """步骤7：分析覆盖审计"""
    print("\n" + "=" * 60)
    print("步骤7：分析覆盖审计")
    print("=" * 60)
    print("  meta AI审计步骤6的分析是否覆盖G'_topo的所有节点和边")
    print("  ⏳ 步骤7待meta AI执行")
    return {}


def main():
    parser = argparse.ArgumentParser(description="七步骤工作流集成脚本")
    parser.add_argument("--steps", default="1,2,3",
                        help="要执行的步骤，逗号分隔（如1,2,3或1,2,3,4,5,6,7）")
    parser.add_argument("--source", default="dependency_graph", help="源图名")
    parser.add_argument("--target", default="unfold_topo", help="目标图名")
    args = parser.parse_args()

    from cognition_sdk_math import CognitionSDK
    sdk = CognitionSDK()

    steps_to_run = [int(s.strip()) for s in args.steps.split(",")]
    results = {}

    step_funcs = {
        1: lambda: step1_import_graph(sdk, args.source),
        2: lambda: step2_generate_g_prime_topo(sdk, args.target),
        3: lambda: step3_topology_verify(sdk),
        4: lambda: step4_translate(sdk),
        5: lambda: step5_kc_audit(sdk),
        6: lambda: step6_analyze(sdk),
        7: lambda: step7_coverage_audit(sdk),
    }

    for step_num in steps_to_run:
        if step_num in step_funcs:
            results[f"step{step_num}"] = step_funcs[step_num]()

    print("\n" + "=" * 60)
    print("执行总结")
    print("=" * 60)
    for step_num in steps_to_run:
        status = "✅" if results.get(f"step{step_num}") else "⏳"
        print(f"  {status} 步骤{step_num}")
    print(f"\n结果: {json.dumps(results, ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    main()
