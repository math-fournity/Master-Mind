"""
253号端到端测试（真实LLM响应版）：A7 → Q8 完整检索流程。

用real_llm_responses（GLM-5.2真实解析结果）代替mock_llm_responses，
跑端到端测试：
1. 用real_llm_responses作为LLMParser的mock_response_provider
2. 跑A7→Q8完整流程
3. 验证是否仍然选中Q8

运行：
    cd ~/master-mind-glm5.2-worktree
    .venv/bin/python3 -m xishujuzhen.research_runtime.test_e2e_real
"""

import sys

# ---- P0 解析器 ----
from .parser.models import (
    ParseRequest,
    ParseResult,
    SixTuple,
    TurnRecord,
)
from .parser.parser import MathParser
from .parser.llm_parser import LLMParser
from .parser.test_data.case_253 import (
    PROBLEM_TEXT,
    QA_SEQUENCE,
    PREVIOUS_SIX_TUPLE_A6,
)
from .parser.test_data.real_llm_responses import make_real_provider

# ---- P1 基础 ----
from .hgraph import create_case_253_graph, build_case_253_rules
from .hgraph.hgraph_store import HeuristicRule, HeuristicRuleGraph
from .lifecycle import LifecycleManager, LifecycleState
from .budget import BudgetManager, BudgetType

# ---- P1 核心 ----
from .activation import ActivationScoreCalculator, ScoredRule
from .matching import PatternMatcher
from .matching.pattern_matcher import MatchedRule as MatchingMatchedRule
from .retrieval import RetrievalPipeline

# ---- P1 决策 ----
from .policy.constrained_optimizer import (
    ConstrainedPolicy,
    MatchedRule as PolicyMatchedRule,
    ConstraintValues,
    SelectionResult,
    leakage_risk,
)
from .gradient.hint_gradient import HintGradient
from .attribution.gain_attribution import GainAttribution, GainRecord


# ===========================================================================
# 辅助函数
# ===========================================================================

def build_a7_parse_result() -> ParseResult:
    """
    用253号A7的真实LLM响应，通过MathParser解析，构造A7的ParseResult。

    流程：
    1. 构造real provider（按round_index返回真实LLM响应）
    2. 构造A7的ParseRequest（含A6之后的六元组作为previous_six_tuple）
    3. 调用MathParser.parse()
    """
    real_provider = make_real_provider()
    llm_parser = LLMParser(mock_response_provider=real_provider)
    math_parser = MathParser(llm_parser=llm_parser)

    # 构造A7的history（Q1-Q6, A1-A6）
    history = []
    for i in range(6):
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
        run_id="test_e2e_real",
        model_version="glm-5.2",
    )

    return math_parser.parse(request)


def convert_matched_rule(mr: MatchingMatchedRule) -> PolicyMatchedRule:
    """
    适配转换：matching模块的MatchedRule → policy模块的MatchedRule。
    """
    return PolicyMatchedRule(rule=mr.rule, match_score=mr.match_score)


# ===========================================================================
# 第一层：状态感知（P0）
# ===========================================================================

def test_layer1_state_perception(a7_result: ParseResult) -> bool:
    """
    第一层：状态感知（P0解析器）。

    验证真实LLM响应解析出的semantic_events、trajectory_nodes、six_tuple。
    """
    print("--- 第一层：状态感知（真实LLM响应） ---")
    errors = []

    # ---- 步骤① event-sourcing ----
    events = a7_result.semantic_events
    event_count = len(events)
    rep_count = sum(1 for e in events if e.type == "representation")
    res_count = sum(1 for e in events if e.type == "resolution")

    print(f"步骤① event-sourcing: {event_count}个语义事件")
    for e in events:
        desc = e.payload.get("description", "")
        print(f"  - {e.type.upper()}: {desc[:60]}")

    if event_count != 4:
        errors.append(f"semantic_events应为4个，实际{event_count}")
    if rep_count != 1:
        errors.append(f"REPRESENTATION应为1个，实际{rep_count}")
    if res_count != 3:
        errors.append(f"RESOLUTION应为3个，实际{res_count}")

    # ---- 步骤② thinking-trajectory-graph ----
    nodes = a7_result.trajectory_nodes
    node_count = len(nodes)
    frontier_nodes = [n for n in nodes if n.is_frontier]

    print(f"步骤② thinking-trajectory-graph: {node_count}个节点，前沿=稳定性方程")
    for n in nodes:
        mark = "★" if n.is_frontier else " "
        print(f"  {mark} [{n.type}] {n.content[:50]}")

    if node_count != 4:
        errors.append(f"trajectory_nodes应为4个，实际{node_count}")
    if len(frontier_nodes) != 1:
        errors.append(f"前沿节点应为1个，实际{len(frontier_nodes)}")
    elif "稳定性方程" not in frontier_nodes[0].content:
        errors.append(f"前沿节点应含'稳定性方程'，实际='{frontier_nodes[0].content}'")

    # ---- 步骤③ dynamic-workspace ----
    st = a7_result.six_tuple
    v_count = len(st.V_t)
    f_count = len(st.F_t)
    o_open = sum(1 for o in st.O_t if o.status == "open")
    u_count = len(st.U_t)

    print(f"步骤③ dynamic-workspace: V_t={v_count}, F_t={f_count}, "
          f"O_t={o_open}(open), U_t={u_count}(blocking)")

    # 验证F_t包含"稳定性方程"
    f_t_strs = [f.statement for f in st.F_t]
    has_stability = any("稳定性方程" in s for s in f_t_strs)
    if not has_stability:
        errors.append(f"F_t应包含'稳定性方程'，实际F_t={f_t_strs}")

    # 验证O_t包含"估计D的下界"
    o_t_strs = [o.description for o in st.O_t]
    has_d_bound = any("D的下界" in d or "估计D" in d for d in o_t_strs)
    if not has_d_bound:
        errors.append(f"O_t应包含'估计D的下界'，实际O_t={o_t_strs}")

    # 验证U_t包含"D的量级问题"
    u_t_strs = [u.description for u in st.U_t]
    has_d_magnitude = any("D的量级" in d or "D" in d for d in u_t_strs)
    if not has_d_magnitude:
        errors.append(f"U_t应包含'D的量级问题'，实际U_t={u_t_strs}")

    if errors:
        for e in errors:
            print(f"  ❌ {e}")
        return False
    print("  ✓ 第一层验证通过\n")
    return True


# ===========================================================================
# 第二层：Pattern提取（P1核心）
# ===========================================================================

def test_layer2_pattern_extraction(
    a7_result: ParseResult,
    hgraph: HeuristicRuleGraph,
) -> tuple:
    """
    第二层：Pattern提取（P1核心：activation + matching + retrieval）。
    """
    print("--- 第二层：Pattern提取 ---")
    errors = []

    rules = hgraph.get_published_rules()

    # ---- 步骤⑥ activation-score ----
    calculator = ActivationScoreCalculator()
    scored_rules = calculator.calculate(a7_result, rules, top_k=len(rules))

    print(f"步骤⑥ activation-score:")
    for sr in scored_rules:
        print(f"  {sr.rule_id}: score={sr.score:.1f}")

    # 验证Q8激活分数高
    q8_scored = next((sr for sr in scored_rules if sr.rule_id == "Q8"), None)
    if q8_scored is None:
        errors.append("Q8不在激活分数结果中")
    elif q8_scored.score < 1.0:
        errors.append(f"Q8激活分数应≥1.0，实际{q8_scored.score}")

    # ---- 步骤⑦ pattern-matching ----
    matcher = PatternMatcher()
    matched_rules = matcher.match(a7_result, scored_rules)

    print(f"步骤⑦ pattern-matching:")
    for mr in matched_rules:
        guard_str = "通过" if mr.guard_passed else "不通过"
        print(f"  {mr.rule_id}: score={mr.match_score:.1f}(guard{guard_str})")

    # 验证Q8的match_score≥0.6且guard通过
    q8_matched = next((mr for mr in matched_rules if mr.rule_id == "Q8"), None)
    if q8_matched is None:
        errors.append("Q8不在模式匹配结果中")
    else:
        if q8_matched.match_score < 0.6:
            errors.append(f"Q8 match_score应≥0.6，实际{q8_matched.match_score}")
        if not q8_matched.guard_passed:
            errors.append("Q8 guard应通过")

    # 验证Q9的match_score低于Q8
    q9_matched = next((mr for mr in matched_rules if mr.rule_id == "Q9"), None)
    if q9_matched is None:
        errors.append("Q9不在模式匹配结果中")
    elif q8_matched and q9_matched.match_score >= q8_matched.match_score:
        errors.append(
            f"Q9 match_score({q9_matched.match_score})应低于Q8({q8_matched.match_score})"
        )

    # ---- 步骤⑧ retrieval-pipeline ----
    pipeline = RetrievalPipeline()
    retrieval_results = pipeline.retrieve(a7_result, hgraph, top_k=10)

    result_ids = [mr.rule_id for mr in retrieval_results]
    print(f"步骤⑧ retrieval-pipeline: top-{len(retrieval_results)} = {result_ids}")

    # 验证Q8在返回结果中
    if "Q8" not in result_ids:
        errors.append(f"Q8应在检索结果中，实际={result_ids}")

    # 验证Q8的match_score≥0.6
    q8_ret = next((mr for mr in retrieval_results if mr.rule_id == "Q8"), None)
    if q8_ret is None:
        errors.append("Q8应在检索结果中")
    elif q8_ret.match_score < 0.6:
        errors.append(f"Q8 match_score应≥0.6，实际{q8_ret.match_score}")

    # 验证Q9在结果中但match_score低于Q8
    q9_ret = next((mr for mr in retrieval_results if mr.rule_id == "Q9"), None)
    if q9_ret is None:
        errors.append(f"Q9应在检索结果中，实际={result_ids}")
    elif q8_ret and q9_ret.match_score >= q8_ret.match_score:
        errors.append(
            f"Q9 match_score({q9_ret.match_score})应低于Q8({q8_ret.match_score})"
        )

    if errors:
        for e in errors:
            print(f"  ❌ {e}")
        return (False, retrieval_results, scored_rules, matched_rules)
    print("  ✓ 第二层验证通过\n")
    return (True, retrieval_results, scored_rules, matched_rules)


# ===========================================================================
# 第三层：知识悖论破解（P1决策）
# ===========================================================================

def test_layer3_knowledge_paradox(
    a7_result: ParseResult,
    retrieval_results: list,
    hgraph: HeuristicRuleGraph,
) -> bool:
    """
    第三层：知识悖论破解（P1决策：policy + gradient + attribution）。
    """
    print("--- 第三层：知识悖论破解 ---")
    errors = []

    six_tuple = a7_result.six_tuple

    # 将matching.MatchedRule转换为policy.MatchedRule
    policy_candidates = [convert_matched_rule(mr) for mr in retrieval_results]

    # ---- 步骤⑩ constrained-policy ----
    policy = ConstrainedPolicy()
    selection = policy.select(policy_candidates, six_tuple)

    selected_id = selection.selected_rule.rule_id if selection.selected_rule else None
    print(f"步骤⑩ constrained-policy: 选中{selected_id}")

    # 打印每条候选的四个约束值
    for rid, cv in selection.constraint_values.items():
        print(f"  - {rid}: progress={cv.progress:.1f}, leakage={cv.leakage:.2f}, "
              f"dependency={cv.dependency:.0f}, cost={cv.cost:.0f}")

    # 验证选中Q8而非Q9
    if selected_id != "Q8":
        errors.append(f"应选中Q8，实际选中{selected_id}")

    # 验证is_abstain=False
    if selection.is_abstain:
        errors.append("不应放弃（is_abstain应为False）")

    # 验证选择理由可解释
    if not selection.constraint_values:
        errors.append("constraint_values不应为空（理由应可解释）")
    else:
        q8_cv = selection.constraint_values.get("Q8")
        q9_cv = selection.constraint_values.get("Q9")
        if q8_cv is None:
            errors.append("Q8的约束值缺失")
        if q9_cv is None:
            errors.append("Q9的约束值缺失")
        if q8_cv and q9_cv:
            print(f"  - Pareto最优: Q8 (同进展，低泄漏)")
            if q9_cv.leakage <= q8_cv.leakage:
                errors.append(
                    f"Q9 leakage({q9_cv.leakage:.2f})应>Q8 leakage({q8_cv.leakage:.2f})"
                )

    # ---- 步骤⑪ hint-gradient ----
    gradient = HintGradient()
    q8_rule = hgraph.get_rule("Q8")
    q8_leakage = leakage_risk(q8_rule)

    degraded = gradient.degrade(q8_rule, policy_candidates)
    needs_degrade = (degraded.rule_id != q8_rule.rule_id)

    print(f"步骤⑪ hint-gradient: Q8不需要降级 "
          f"(leakage={q8_leakage:.2f} < 0.5)")

    if q8_leakage >= 0.5:
        errors.append(f"Q8 leakage_risk应<0.5，实际{q8_leakage:.2f}")
    if needs_degrade:
        errors.append(
            f"Q8不应触发降级，但降级为{degraded.rule_id}"
        )

    # 额外验证：Q9需要降级（leakage>0.5）
    q9_rule = hgraph.get_rule("Q9")
    q9_leakage = leakage_risk(q9_rule)
    q9_degraded = gradient.degrade(q9_rule, policy_candidates)
    q9_needs_degrade = (q9_degraded.rule_id != q9_rule.rule_id)
    if q9_leakage > 0.5 and not q9_needs_degrade:
        print(f"  [INFO] Q9 leakage={q9_leakage:.2f}>0.5 但无替代规则，生成降级版")
    elif q9_leakage > 0.5:
        print(f"  [INFO] Q9 leakage={q9_leakage:.2f}>0.5 → 降级为{q9_degraded.rule_id}")

    # ---- 步骤⑭ gain-attribution ----
    attribution = GainAttribution()

    attribution.record_hint(8, q8_rule)
    recorded = attribution.get_hint(8)

    print(f"步骤⑭ gain-attribution: Q8已记录为第8轮hint")

    if recorded is None:
        errors.append("Q8应被记录为第8轮hint")
    elif recorded.rule_id != "Q8":
        errors.append(f"第8轮hint应为Q8，实际{recorded.rule_id}")

    if recorded:
        print(f"  [INFO] 提示链第8轮: {recorded.rule_id} "
              f"(obligation={recorded.obligation_id})")

    if errors:
        for e in errors:
            print(f"  ❌ {e}")
        return False
    print("  ✓ 第三层验证通过\n")
    return True


# ===========================================================================
# 预算检查
# ===========================================================================

def test_budget_check(q8_rule: HeuristicRule) -> bool:
    """
    预算检查：BudgetManager。
    """
    print("--- 预算检查 ---")
    errors = []

    budget = BudgetManager()
    budget.set_budget(BudgetType.HINT, 10)
    initial = budget.get_hint_remaining()

    print(f"Hint预算: {int(initial)} → ", end="")

    ok = budget.consume_hint(1)
    if not ok:
        errors.append("消耗Hint预算应成功")
        print("消耗失败")

    remaining = budget.get_hint_remaining()
    print(f"{int(remaining)} (消耗1)")

    if remaining != 9:
        errors.append(f"剩余Hint预算应为9，实际{remaining}")

    if errors:
        for e in errors:
            print(f"  ❌ {e}")
        return False
    print("  ✓ 预算检查通过\n")
    return True


# ===========================================================================
# 主入口
# ===========================================================================

def main() -> int:
    print()
    print("=" * 60)
    print("=== 253号端到端测试（真实LLM响应）：A7 → Q8 ===")
    print("=" * 60)
    print()
    print("使用GLM-5.2真实解析结果（real_llm_responses）替代mock响应")
    print()

    # ---- 准备：构造A7的ParseResult（用真实LLM响应） ----
    a7_result = build_a7_parse_result()

    # ---- 准备：初始化H图 + 生命周期管理器 ----
    hgraph = create_case_253_graph()
    lifecycle = LifecycleManager(graph=hgraph)
    # 验证所有规则为published
    published = lifecycle.get_publishable_rules()
    if len(published) != 10:
        print(f"  ❌ H图应有10条published规则，实际{len(published)}")
        return 1

    # ---- 第一层：状态感知 ----
    layer1_passed = test_layer1_state_perception(a7_result)

    # ---- 第二层：Pattern提取 ----
    layer2_passed, retrieval_results, scored_rules, matched_rules = (
        test_layer2_pattern_extraction(a7_result, hgraph)
    )

    # ---- 第三层：知识悖论破解 ----
    layer3_passed = test_layer3_knowledge_paradox(
        a7_result, retrieval_results, hgraph
    )

    # ---- 预算检查 ----
    q8_rule = hgraph.get_rule("Q8")
    budget_passed = test_budget_check(q8_rule)

    # ---- 汇总 ----
    print("=" * 60)
    print("=== 端到端测试结果（真实LLM响应） ===")
    print(f"  第一层（状态感知）: {'✅ 通过' if layer1_passed else '❌ 失败'}")
    print(f"  第二层（Pattern提取）: {'✅ 通过' if layer2_passed else '❌ 失败'}")
    print(f"  第三层（知识悖论）: {'✅ 通过' if layer3_passed else '❌ 失败'}")
    print(f"  预算检查: {'✅ 通过' if budget_passed else '❌ 失败'}")
    print()

    all_passed = layer1_passed and layer2_passed and layer3_passed and budget_passed
    if all_passed:
        print("  🎉 端到端测试通过！真实LLM响应下系统仍正确从A7检索出Q8。")
        return 0
    else:
        print("  ⚠️  端到端测试有失败项。")
        return 1


if __name__ == "__main__":
    sys.exit(main())
