"""
实时管线+devin cli parser完整测试：253号A7 → Q8。

用DevinCliParserProvider替代mock LLM，验证RealtimePipeline
在真实devin cli解析下的完整流程。

运行：
    cd ~/master-mind-glm5.2-worktree
    .venv/bin/python3 -m xishujuzhen.research_runtime.realtime.test_realtime_devin_cli
"""

import sys
import os
import json
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from xishujuzhen.research_runtime.realtime.trajectory_watcher import Round
from xishujuzhen.research_runtime.realtime.pipeline import RealtimePipeline
from xishujuzhen.research_runtime.realtime.devin_cli_parser import DevinCliParserProvider

from xishujuzhen.research_runtime.parser.models import (
    ParseRequest, ParseResult, SixTuple, TurnRecord,
)
from xishujuzhen.research_runtime.parser.parser import MathParser
from xishujuzhen.research_runtime.parser.llm_parser import LLMParser
from xishujuzhen.research_runtime.parser.test_data.case_253 import (
    PROBLEM_TEXT, QA_SEQUENCE, PREVIOUS_SIX_TUPLE_A6,
)
from xishujuzhen.research_runtime.hgraph import create_case_253_graph, build_case_253_rules
from xishujuzhen.research_runtime.retrieval import RetrievalPipeline
from xishujuzhen.research_runtime.policy.constrained_optimizer import ConstrainedPolicy
from xishujuzhen.research_runtime.budget import BudgetManager, BudgetType


def main():
    print("\n" + "=" * 60)
    print("实时管线+devin cli parser完整测试")
    print("253号A7 → Q8（用devin cli作为parser LLM）")
    print("=" * 60 + "\n")

    # 构建253号H图
    print("[1] 构建253号H图...")
    hgraph = create_case_253_graph()
    rules = build_case_253_rules()
    for rule in rules:
        hgraph.add_rule(rule)
    print(f"    {len(rules)}条规则")

    # 构建devin cli parser
    print("\n[2] 创建DevinCliParserProvider...")
    provider = DevinCliParserProvider(timeout=180, max_retries=1)
    llm_parser = LLMParser(mock_response_provider=provider)
    math_parser = MathParser(llm_parser=llm_parser)
    print(f"    work_dir: {provider.work_dir}")

    # 构建pipeline
    print("\n[3] 构建RealtimePipeline...")
    budget = BudgetManager()
    budget.set_budget(BudgetType.HINT, 10)
    pipeline = RealtimePipeline(
        session_id="test-devin-cli-001",
        hgraph=hgraph,
        problem_text=PROBLEM_TEXT,
        math_parser=math_parser,
        retrieval_pipeline=RetrievalPipeline(),
        policy=ConstrainedPolicy(),
        budget_manager=budget,
        tmux_session="",  # 不注入
    )

    # 设置A6之后的六元组状态
    pipeline._current_six_tuple = SixTuple.from_dict(PREVIOUS_SIX_TUPLE_A6)

    # 设置历史
    for i in range(6):
        qa = QA_SEQUENCE[i]
        pipeline._history.append(TurnRecord(
            q_text=qa["q_text"],
            a_text=qa["a_text"],
            round_index=i + 1,
        ))

    # 构造A7的Round
    a7_data = QA_SEQUENCE[6]
    a7_round = Round(
        round_index=7,
        agent_output=a7_data["a_text"],
        thinking="",
        content=a7_data["a_text"],
        tool_calls=[],
        node_ids=[701, 702, 703],
        start_timestamp=time.time(),
        end_timestamp=time.time(),
        is_complete=True,
    )

    # 处理A7
    print("\n[4] 处理A7轮次（调用devin cli解析，可能需要30-60秒）...")
    start_time = time.time()
    result = pipeline.process_round(a7_round)
    elapsed = time.time() - start_time

    print(f"\n[5] 处理完成（{elapsed:.1f}s）")

    if result.error:
        print(f"    ❌ 错误: {result.error}")

    if result.parse_result:
        pr = result.parse_result
        print(f"    ✅ 解析: {len(pr.semantic_events)}事件, {len(pr.trajectory_nodes)}节点, confidence={pr.parse_confidence:.2f}")
        st = pr.six_tuple
        print(f"    ✅ 六元组: V_t={len(st.V_t)}, F_t={len(st.F_t)}, O_t={len(st.O_t)}, U_t={len(st.U_t)}")

    if result.matched_rules:
        print(f"    ✅ 检索: {len(result.matched_rules)}条匹配规则")
        for i, mr in enumerate(result.matched_rules[:3]):
            print(f"       top-{i+1}: {mr.rule_id} score={mr.match_score:.2f}")

    if result.selection_result and result.selection_result.selected_rule:
        selected = result.selection_result.selected_rule
        print(f"    ✅ 策略选择: {selected.rule_id}")
        if "Q8" in selected.rule_id:
            print(f"    🎉 选中Q8！与离线test_e2e_253一致")
        else:
            print(f"    ⚠️  选中{selected.rule_id}而非Q8")
        if result.selected_q:
            print(f"    ✅ 提示文本: {result.selected_q[:80]}...")
    else:
        print(f"    ⚠️  策略未选中任何规则")

    # 保存完整结果
    output_path = "/tmp/realtime_devin_cli_result.json"
    save_data = {
        "elapsed_seconds": elapsed,
        "round_index": result.round_index,
        "error": result.error,
        "selected_q": result.selected_q,
        "matched_rules": [
            {"rule_id": mr.rule_id, "match_score": mr.match_score}
            for mr in result.matched_rules
        ],
    }
    if result.selection_result:
        save_data["selection"] = {
            "selected_rule_id": result.selection_result.selected_rule.rule_id if result.selection_result.selected_rule else None,
            "is_abstain": result.selection_result.is_abstain,
            "reason": result.selection_result.reason,
        }
    with open(output_path, "w") as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)
    print(f"\n    结果已保存到: {output_path}")

    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
