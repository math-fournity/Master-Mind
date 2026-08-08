"""
DevinCliParserProvider测试：验证devin cli作为parser LLM的完整流程。

测试目标：
1. DevinCliParserProvider能正确调用devin cli
2. devin cli返回的JSON能被正确提取
3. 提取的JSON能被MathParser处理为ParseResult
4. 整个流程与mock LLM结果可比

测试用例：用253号A7的文本作为输入，验证devin cli能解析出结构化结果。

运行：
    cd ~/master-mind-glm5.2-worktree
    .venv/bin/python3 -m xishujuzhen.research_runtime.realtime.test_devin_cli_parser
"""

import sys
import os
import json
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from xishujuzhen.research_runtime.parser.models import (
    ParseRequest, ParseResult, SixTuple, TurnRecord,
)
from xishujuzhen.research_runtime.parser.parser import MathParser
from xishujuzhen.research_runtime.parser.llm_parser import LLMParser
from xishujuzhen.research_runtime.parser.test_data.case_253 import (
    PROBLEM_TEXT, QA_SEQUENCE, PREVIOUS_SIX_TUPLE_A6,
)
from xishujuzhen.research_runtime.realtime.devin_cli_parser import DevinCliParserProvider


def test_devin_cli_parser_basic():
    """
    测试DevinCliParserProvider基本功能：
    用253号A7文本调用devin cli做解析。
    """
    print("=" * 60)
    print("测试: DevinCliParserProvider (253号A7)")
    print("=" * 60)

    # 构造A7的ParseRequest
    history = []
    for i in range(6):
        qa = QA_SEQUENCE[i]
        history.append(TurnRecord(
            q_text=qa["q_text"],
            a_text=qa["a_text"],
            round_index=i + 1,
        ))

    a7_data = QA_SEQUENCE[6]  # round 7
    request = ParseRequest(
        agent_output=a7_data["a_text"],
        round_index=7,
        problem_text=PROBLEM_TEXT,
        history=history,
        current_six_tuple=SixTuple.from_dict(PREVIOUS_SIX_TUPLE_A6),
        run_id="test_devin_cli_parser",
        model_version="devin-cli",
    )

    # 创建DevinCliParserProvider
    print("\n[1] 创建DevinCliParserProvider...")
    provider = DevinCliParserProvider(
        model="glm-5-2",
        timeout=180,  # 给devin cli足够时间
        max_retries=1,
    )
    print(f"    work_dir: {provider.work_dir}")

    # 调用devin cli做解析
    print("\n[2] 调用devin cli做解析（可能需要1-3分钟）...")
    start_time = time.time()
    result = provider(request)
    elapsed = time.time() - start_time

    print(f"\n[3] 解析完成（{elapsed:.1f}s）")
    print(f"    semantic_events: {len(result.get('semantic_events', []))}个")
    print(f"    trajectory_nodes: {len(result.get('trajectory_nodes', []))}个")
    print(f"    parse_confidence: {result.get('parse_confidence', 'N/A')}")
    print(f"    parse_warnings: {result.get('parse_warnings', [])}")

    # 验证基本结构
    assert "semantic_events" in result, "结果应包含semantic_events"
    assert "trajectory_nodes" in result, "结果应包含trajectory_nodes"
    assert "six_tuple" in result, "结果应包含six_tuple"

    events = result.get("semantic_events", [])
    if events:
        print(f"\n[4] 第一个事件:")
        evt = events[0]
        print(f"    type: {evt.get('type', 'N/A')}")
        print(f"    description: {evt.get('description', 'N/A')[:100]}")

    nodes = result.get("trajectory_nodes", [])
    if nodes:
        print(f"\n[5] 前沿节点:")
        for node in nodes:
            if node.get("is_frontier"):
                print(f"    type: {node.get('type', 'N/A')}")
                print(f"    content: {node.get('content', 'N/A')[:100]}")
                break

    six_tuple = result.get("six_tuple", {})
    print(f"\n[6] 六元组:")
    print(f"    V_t: {len(six_tuple.get('V_t', []))}条")
    print(f"    F_t: {len(six_tuple.get('F_t', []))}条")
    print(f"    O_t: {len(six_tuple.get('O_t', []))}条")
    print(f"    U_t: {len(six_tuple.get('U_t', []))}条")

    # 保存原始结果供调试
    output_path = "/tmp/devin_cli_parser_test_result.json"
    with open(output_path, "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n    原始结果已保存到: {output_path}")

    # 检查math_objects格式
    for i, v in enumerate(result.get("six_tuple", {}).get("V_t", [])[:3]):
        mos = v.get("math_objects", [])
        for j, mo in enumerate(mos):
            print(f"    V_t[{i}].math_objects[{j}] type={type(mo).__name__}: {str(mo)[:80]}")

    # 用MathParser处理
    print("\n[7] 用MathParser处理devin cli的输出...")
    llm_parser = LLMParser(mock_response_provider=lambda req: result)
    math_parser = MathParser(llm_parser=llm_parser)
    parse_result = math_parser.parse(request)

    print(f"    ParseResult:")
    print(f"      semantic_events: {len(parse_result.semantic_events)}个")
    print(f"      trajectory_nodes: {len(parse_result.trajectory_nodes)}个")
    print(f"      parse_confidence: {parse_result.parse_confidence:.2f}")
    print(f"      sympy_verified: {sum(parse_result.sympy_verified)}/{len(parse_result.sympy_verified)}")

    six_tuple_result = parse_result.six_tuple
    print(f"      六元组: V_t={len(six_tuple_result.V_t)}, F_t={len(six_tuple_result.F_t)}, "
          f"O_t={len(six_tuple_result.O_t)}, U_t={len(six_tuple_result.U_t)}")

    print("\n" + "=" * 60)
    print("✅ DevinCliParserProvider测试完成")
    print("=" * 60)

    return result


def main():
    print("\n" + "=" * 60)
    print("DevinCliParserProvider测试")
    print("用devin cli作为parser LLM，解析253号A7")
    print("=" * 60 + "\n")

    try:
        result = test_devin_cli_parser_basic()

        # 保存结果供分析
        output_path = "/tmp/devin_cli_parser_test_result.json"
        with open(output_path, "w") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"\n结果已保存到: {output_path}")

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
