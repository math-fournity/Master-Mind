"""
解析器测试脚本：用253号A7案例做完整走通 + A1-A10全序列走通。

测试步骤：
1. A7完整走通：
   - 构造ParseRequest（A7的文本 + history + previous_six_tuple）
   - 用mock LLM调用MathParser.parse()
   - 验证输出：
     - semantic_events有4个（1个REPRESENTATION + 3个RESOLUTION）
     - trajectory_nodes有4个，前沿节点是"稳定性方程(3)"
     - six_tuple的F_t包含"稳定性方程"，O_t包含"估计D的下界"，U_t包含"D的量级问题"
     - sympy_verified全部为True
     - parse_confidence > 0.8
   - 打印解析结果

2. A1-A10全序列走通：
   - 逐轮调用MathParser.parse()
   - 每轮的输出作为下一轮的previous_six_tuple
   - 验证A10结束后O_t全部solved
"""

import json
import sys

from ..models.event import SemanticEvent
from .models import (
    ParseRequest,
    ParseResult,
    SixTuple,
    TurnRecord,
)
from .parser import MathParser
from .llm_parser import LLMParser
from .test_data.case_253 import (
    PROBLEM_TEXT,
    QA_SEQUENCE,
    PREVIOUS_SIX_TUPLE_A6,
)
from .test_data.mock_llm_responses import make_mock_provider


def test_a7():
    """
    测试1：A7完整走通。

    用mock LLM（返回260号§4.2.2的JSON）调用MathParser.parse()，
    验证输出符合预期。
    """
    print("=" * 70)
    print("测试1：A7完整走通")
    print("=" * 70)

    # 构造mock provider
    mock_provider = make_mock_provider()

    # 构造LLMParser（用mock）
    llm_parser = LLMParser(mock_response_provider=mock_provider)

    # 构造MathParser
    math_parser = MathParser(llm_parser=llm_parser)

    # 构造A7的history（Q1-Q6, A1-A6）
    history = []
    for i in range(6):  # round 1-6
        qa = QA_SEQUENCE[i]
        history.append(TurnRecord(
            q_text=qa["q_text"],
            a_text=qa["a_text"],
            q_level=qa["q_level"],
            q_non_specificity=qa["q_non_specificity"],
            round_index=qa["round"],
        ))

    # 构造previous_six_tuple（A6之后的六元组）
    previous_six_tuple = SixTuple.from_dict(PREVIOUS_SIX_TUPLE_A6)

    # 构造A7的ParseRequest
    a7_data = QA_SEQUENCE[6]  # round 7
    request = ParseRequest(
        agent_output=a7_data["a_text"],
        round_index=7,
        problem_text=PROBLEM_TEXT,
        history=history,
        current_six_tuple=previous_six_tuple,
        run_id="test_253_a7",
        model_version="mock",
    )

    # 调用MathParser.parse()
    result = math_parser.parse(request)

    # ---- 验证输出 ----
    print("\n--- 验证 ---")
    all_passed = True

    # 1. semantic_events有4个（1个REPRESENTATION + 3个RESOLUTION）
    event_count = len(result.semantic_events)
    rep_count = sum(1 for e in result.semantic_events if e.type == "representation")
    res_count = sum(1 for e in result.semantic_events if e.type == "resolution")
    print(f"  事件数量: {event_count} (期望4), REPRESENTATION: {rep_count} (期望1), RESOLUTION: {res_count} (期望3)")
    if event_count != 4:
        print(f"  ❌ 事件数量不符: {event_count} != 4")
        all_passed = False
    if rep_count != 1:
        print(f"  ❌ REPRESENTATION事件数量不符: {rep_count} != 1")
        all_passed = False
    if res_count != 3:
        print(f"  ❌ RESOLUTION事件数量不符: {res_count} != 3")
        all_passed = False

    # 2. trajectory_nodes有4个，前沿节点是"稳定性方程(3)"
    node_count = len(result.trajectory_nodes)
    frontier_nodes = [n for n in result.trajectory_nodes if n.is_frontier]
    print(f"  节点数量: {node_count} (期望4), 前沿节点数: {len(frontier_nodes)} (期望1)")
    if node_count != 4:
        print(f"  ❌ 节点数量不符: {node_count} != 4")
        all_passed = False
    if len(frontier_nodes) != 1:
        print(f"  ❌ 前沿节点数量不符: {len(frontier_nodes)} != 1")
        all_passed = False
    else:
        frontier_content = frontier_nodes[0].content
        print(f"  前沿节点内容: {frontier_content}")
        if "稳定性方程" not in frontier_content:
            print(f"  ❌ 前沿节点不是稳定性方程: {frontier_content}")
            all_passed = False
        else:
            print(f"  ✓ 前沿节点是稳定性方程")

    # 3. six_tuple的F_t包含"稳定性方程"
    f_t_statements = [f.statement for f in result.six_tuple.F_t]
    print(f"  F_t: {f_t_statements}")
    has_stability = any("稳定性方程" in s for s in f_t_statements)
    if not has_stability:
        print(f"  ❌ F_t不包含稳定性方程")
        all_passed = False
    else:
        print(f"  ✓ F_t包含稳定性方程")

    # O_t包含"估计D的下界"
    o_t_descs = [o.description for o in result.six_tuple.O_t]
    print(f"  O_t: {o_t_descs}")
    has_d_bound = any("D的下界" in d or "估计D" in d for d in o_t_descs)
    if not has_d_bound:
        print(f"  ❌ O_t不包含'估计D的下界'")
        all_passed = False
    else:
        print(f"  ✓ O_t包含'估计D的下界'")

    # U_t包含"D的量级问题"
    u_t_descs = [u.description for u in result.six_tuple.U_t]
    print(f"  U_t: {u_t_descs}")
    has_d_magnitude = any("D的量级" in d or "D" in d for d in u_t_descs)
    if not has_d_magnitude:
        print(f"  ❌ U_t不包含'D的量级问题'")
        all_passed = False
    else:
        print(f"  ✓ U_t包含'D的量级问题'")

    # 4. sympy_verified全部为True
    all_verified = all(result.sympy_verified)
    print(f"  sympy_verified: {result.sympy_verified} (全部True: {all_verified})")
    if not all_verified:
        print(f"  ❌ 不是所有事件都通过SymPy验证")
        all_passed = False
    else:
        print(f"  ✓ 所有事件通过SymPy验证")

    # 5. parse_confidence > 0.8
    print(f"  parse_confidence: {result.parse_confidence:.4f} (期望>0.8)")
    if result.parse_confidence <= 0.8:
        print(f"  ❌ parse_confidence <= 0.8")
        all_passed = False
    else:
        print(f"  ✓ parse_confidence > 0.8")

    # 打印警告
    if result.parse_warnings:
        print(f"\n  解析警告:")
        for w in result.parse_warnings:
            print(f"    - {w}")

    # 打印完整解析结果
    print("\n--- 完整解析结果 ---")
    print(f"  semantic_events ({len(result.semantic_events)}):")
    for i, e in enumerate(result.semantic_events):
        print(f"    [{i}] type={e.type}, confidence={e.confidence:.2f}")
        print(f"        description: {e.payload.get('description', '')[:80]}")
        for mo in e.payload.get("math_objects", []):
            print(f"        math_object: {mo.get('name', '')} (verified={mo.get('sympy_verified', False)})")

    print(f"\n  trajectory_nodes ({len(result.trajectory_nodes)}):")
    for n in result.trajectory_nodes:
        frontier_mark = "★" if n.is_frontier else " "
        print(f"    {frontier_mark} [{n.type}] {n.content[:60]}")

    print(f"\n  trajectory_edges ({len(result.trajectory_edges)}):")
    for edge in result.trajectory_edges:
        print(f"    {edge.edge_type}: {edge.description[:60]}")

    print(f"\n  six_tuple:")
    print(f"    V_t ({len(result.six_tuple.V_t)}):")
    for v in result.six_tuple.V_t:
        print(f"      - {v.statement[:60]}")
    print(f"    F_t ({len(result.six_tuple.F_t)}):")
    for f in result.six_tuple.F_t:
        print(f"      - {f.statement[:60]} (status={f.status})")
    print(f"    O_t ({len(result.six_tuple.O_t)}):")
    for o in result.six_tuple.O_t:
        print(f"      - {o.description[:60]} (status={o.status})")
    print(f"    R_t ({len(result.six_tuple.R_t)}):")
    for r in result.six_tuple.R_t:
        print(f"      - {r.name}: {r.description[:40]}")
    print(f"    E_t ({len(result.six_tuple.E_t)}):")
    for e in result.six_tuple.E_t:
        print(f"      - [{e.kind}] {e.content[:60]}")
    print(f"    U_t ({len(result.six_tuple.U_t)}):")
    for u in result.six_tuple.U_t:
        print(f"      - [{u.severity}] {u.description[:60]}")

    if all_passed:
        print("\n" + "=" * 70)
        print("✅ A7测试全部通过")
        print("=" * 70)
    else:
        print("\n" + "=" * 70)
        print("❌ A7测试有失败项")
        print("=" * 70)

    return all_passed


def test_a1_a10_sequence():
    """
    测试2：A1-A10全序列走通。

    逐轮调用MathParser.parse()，
    每轮的输出作为下一轮的previous_six_tuple，
    验证A10结束后O_t全部solved。
    """
    print("\n" + "=" * 70)
    print("测试2：A1-A10全序列走通")
    print("=" * 70)

    # 构造mock provider和MathParser
    mock_provider = make_mock_provider()
    llm_parser = LLMParser(mock_response_provider=mock_provider)
    math_parser = MathParser(llm_parser=llm_parser)

    # 逐轮解析
    history: list[TurnRecord] = []
    current_six_tuple: SixTuple | None = None
    results: list[ParseResult] = []

    for i in range(10):
        round_idx = i + 1
        qa = QA_SEQUENCE[i]

        request = ParseRequest(
            agent_output=qa["a_text"],
            round_index=round_idx,
            problem_text=PROBLEM_TEXT,
            history=list(history),  # 传入副本
            current_six_tuple=current_six_tuple,
            run_id="test_253_seq",
            model_version="mock",
        )

        result = math_parser.parse(request)
        results.append(result)

        # 更新history和six_tuple
        history.append(TurnRecord(
            q_text=qa["q_text"],
            a_text=qa["a_text"],
            q_level=qa["q_level"],
            q_non_specificity=qa["q_non_specificity"],
            round_index=round_idx,
            parsed_events=result.semantic_events,
        ))
        current_six_tuple = result.six_tuple

        # 打印每轮摘要
        event_types = [e.type for e in result.semantic_events]
        frontier_nodes = [n for n in result.trajectory_nodes if n.is_frontier]
        frontier_content = frontier_nodes[0].content[:40] if frontier_nodes else "无"
        open_obligations = [o for o in result.six_tuple.O_t if o.status != "solved"]
        print(
            f"  A{round_idx}: events={event_types}, "
            f"frontier={frontier_content}, "
            f"confidence={result.parse_confidence:.3f}, "
            f"open_O={len(open_obligations)}"
        )

    # ---- 验证A10结束后O_t全部solved ----
    print("\n--- 验证A10结束后的状态 ---")
    all_passed = True

    final_six_tuple = results[-1].six_tuple
    open_obligations = [o for o in final_six_tuple.O_t if o.status != "solved"]
    solved_obligations = [o for o in final_six_tuple.O_t if o.status == "solved"]

    print(f"  O_t总数: {len(final_six_tuple.O_t)}")
    print(f"  solved: {len(solved_obligations)}, open: {len(open_obligations)}")

    for o in final_six_tuple.O_t:
        print(f"    [{o.status}] {o.description[:60]}")

    if open_obligations:
        print(f"  ❌ A10结束后仍有{len(open_obligations)}个open义务")
        all_passed = False
    else:
        print(f"  ✓ A10结束后O_t全部solved")

    # 验证V_t非空（有已验证核心）
    print(f"\n  V_t条目数: {len(final_six_tuple.V_t)}")
    if len(final_six_tuple.V_t) == 0:
        print(f"  ❌ V_t为空")
        all_passed = False
    else:
        print(f"  ✓ V_t非空")
        for v in final_six_tuple.V_t:
            print(f"    - {v.statement[:60]}")

    # 验证U_t为空（无未解决问题）
    print(f"\n  U_t条目数: {len(final_six_tuple.U_t)}")
    if final_six_tuple.U_t:
        print(f"  ⚠️  U_t非空（有未解决问题）:")
        for u in final_six_tuple.U_t:
            print(f"    - [{u.severity}] {u.description[:60]}")
    else:
        print(f"  ✓ U_t为空（所有问题已解决）")

    # 验证最终结论在V_t中
    has_final = any("δ" in v.statement and "n" in v.statement for v in final_six_tuple.V_t)
    if not has_final:
        print(f"  ❌ V_t中无最终结论δ≥c₈/n^(3/2)")
        all_passed = False
    else:
        print(f"  ✓ V_t包含最终结论")

    if all_passed:
        print("\n" + "=" * 70)
        print("✅ A1-A10全序列测试通过")
        print("=" * 70)
    else:
        print("\n" + "=" * 70)
        print("❌ A1-A10全序列测试有失败项")
        print("=" * 70)

    return all_passed


def main():
    """主测试入口"""
    print("解析器测试：253号A7案例 + A1-A10全序列")
    print()

    a7_passed = test_a7()
    seq_passed = test_a1_a10_sequence()

    print("\n" + "=" * 70)
    print("测试总结")
    print("=" * 70)
    print(f"  A7完整走通: {'✅ 通过' if a7_passed else '❌ 失败'}")
    print(f"  A1-A10全序列: {'✅ 通过' if seq_passed else '❌ 失败'}")

    if a7_passed and seq_passed:
        print("\n  🎉 所有测试通过！")
        return 0
    else:
        print("\n  ⚠️  有测试失败")
        return 1


if __name__ == "__main__":
    sys.exit(main())
