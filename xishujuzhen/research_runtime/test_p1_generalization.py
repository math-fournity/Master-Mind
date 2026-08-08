"""
P1泛化验证测试脚本。

在2个新案例（数论题、组合/概率题）上验证4个P1原语的泛化能力：
1. activation-score：正确Q的激活分数是否排top-3？
2. pattern-matching：正确Q的match_score是否≥0.6？Guard是否通过？
3. retrieval-pipeline：正确Q是否在top-5结果中？
4. constrained-policy：是否选中正确Q而非其他Q？

验证场景：
- 数论案例：A3后应触发Q4（引导者问"改用分圆多项式Φ_n(A)呢？"）
- 组合案例：A3后应触发Q4（引导者问"理清Hamming码策略的逻辑"）

运行：
    cd /data/master-mind-glm5.2-grove
    .venv/bin/python3 -m xishujuzhen.research_runtime.test_p1_generalization
"""

import sys
from typing import List, Tuple

from .parser.models import (
    ParseResult,
    SixTuple,
    TrajectoryNode,
    MathObject,
)
from .parser.test_data.gold_standard_new_cases import (
    NT_GOLD_STANDARD_A3,
    CB_GOLD_STANDARD_A3,
)
from .hgraph import (
    HeuristicRuleGraph,
    build_case_number_theory_rules,
    create_case_number_theory_graph,
    build_case_combinatorics_rules,
    create_case_combinatorics_graph,
)
from .activation import ActivationScoreCalculator, ScoredRule
from .matching import PatternMatcher, MatchedRule as MatchingMatchedRule
from .retrieval import RetrievalPipeline
from .policy.constrained_optimizer import (
    ConstrainedPolicy,
    MatchedRule as PolicyMatchedRule,
    SelectionResult,
)


# ===========================================================================
# 辅助函数：从Gold Standard构造ParseResult
# ===========================================================================

def _gold_to_parse_result(gold: dict, round_index: int) -> ParseResult:
    """
    将Gold Standard字典转换为ParseResult对象。

    Gold Standard包含trajectory_nodes（带type/content/math_objects/is_frontier/confidence）
    和six_tuple（V_t/F_t/O_t/R_t/E_t/U_t），需要转换为对应的dataclass对象。
    """
    # 构造TrajectoryNode列表
    trajectory_nodes: List[TrajectoryNode] = []
    for i, node_dict in enumerate(gold.get("trajectory_nodes", [])):
        # math_objects在gold standard中是字符串列表（名称），转换为MathObject
        math_objects = []
        for mo_name in node_dict.get("math_objects", []):
            if isinstance(mo_name, str):
                math_objects.append(MathObject(name=mo_name, latex=""))
            else:
                math_objects.append(MathObject.from_dict(mo_name))
        trajectory_nodes.append(TrajectoryNode(
            node_id=f"node_{round_index}_{i}",
            type=node_dict["type"],
            round_index=round_index,
            content=node_dict["content"],
            math_objects=math_objects,
            is_frontier=node_dict.get("is_frontier", False),
            confidence=node_dict.get("confidence", 1.0),
        ))

    # 构造SixTuple
    six_tuple = SixTuple.from_dict(gold.get("six_tuple", {}))

    # 注意：activation-score/pattern-matching/retrieval-pipeline/constrained-policy
    # 只使用trajectory_nodes和six_tuple，不使用semantic_events，因此传空列表。
    return ParseResult(
        semantic_events=[],
        trajectory_nodes=trajectory_nodes,
        trajectory_edges=[],
        six_tuple=six_tuple,
        parse_confidence=gold.get("parse_confidence", 0.85),
        parse_warnings=gold.get("parse_warnings", []),
    )


# ===========================================================================
# 数论案例验证
# ===========================================================================

def test_number_theory() -> Tuple[bool, dict]:
    """
    数论案例泛化验证。

    A3后应触发Q4（改用分圆多项式Φ_n(A)）。
    A3状态：stall（阶可能是真因子），U_t有"阶可能是n的真因子"，
    O_t有"保证ord_q(A) = n（排除真因子）"（open）。
    """
    print("\n--- 数论案例 ---")

    # 构造A3的ParseResult
    parse_result = _gold_to_parse_result(NT_GOLD_STANDARD_A3, round_index=3)

    # 打印A3状态摘要
    print(f"  A3 trajectory_nodes ({len(parse_result.trajectory_nodes)}):")
    for n in parse_result.trajectory_nodes:
        frontier = "★" if n.is_frontier else " "
        print(f"    {frontier} [{n.type}] {n.content[:50]}")
    print(f"  A3 U_t: {parse_result.six_tuple.U_t[0].description[:60] if parse_result.six_tuple.U_t else '(空)'}")
    print(f"  A3 O_t (open): {[o.description[:30] for o in parse_result.six_tuple.O_t if o.status == 'open']}")

    results = {}
    all_pass = True

    # ---- 步骤⑥ activation-score ----
    rules = build_case_number_theory_rules()
    calculator = ActivationScoreCalculator()
    p_t = calculator.extract_features(parse_result)
    print(f"\n  [INFO] A3特征向量p_t: {p_t}")

    scored_rules = calculator.calculate(parse_result, rules, top_k=6)
    print(f"  [INFO] 激活分数排名:")
    for i, sr in enumerate(scored_rules):
        print(f"    {i+1}. {sr.rule_id}: score={sr.score:.4f}")

    top3_ids = [sr.rule_id for sr in scored_rules[:3]]
    q4_score = next((sr.score for sr in scored_rules if sr.rule_id == "Q4"), None)
    act_pass = "Q4" in top3_ids
    results["activation_score"] = {
        "pass": act_pass,
        "q4_score": q4_score,
        "top3": top3_ids,
    }
    status = "✅" if act_pass else "❌"
    print(f"  步骤⑥ activation-score: Q4={q4_score:.1f}, top-3={top3_ids} {status}")
    if not act_pass:
        all_pass = False
        print(f"  [FAIL] Q4未在top-3中")

    # ---- 步骤⑦ pattern-matching ----
    matcher = PatternMatcher()
    matched_rules = matcher.match(parse_result, scored_rules)

    print(f"\n  [INFO] 模式匹配结果:")
    for mr in matched_rules:
        print(f"    {mr.rule_id}: match_score={mr.match_score:.2f}, guard_passed={mr.guard_passed}")

    q4_match = next((mr for mr in matched_rules if mr.rule_id == "Q4"), None)
    pm_pass = q4_match is not None and q4_match.match_score >= 0.6 and q4_match.guard_passed
    results["pattern_matching"] = {
        "pass": pm_pass,
        "q4_score": q4_match.match_score if q4_match else None,
        "guard_passed": q4_match.guard_passed if q4_match else None,
    }
    status = "✅" if pm_pass else "❌"
    if q4_match:
        print(f"  步骤⑦ pattern-matching: Q4 score={q4_match.match_score:.1f}, guard通过={q4_match.guard_passed} {status}")
    else:
        print(f"  步骤⑦ pattern-matching: Q4不在匹配结果中 ❌")
    if not pm_pass:
        all_pass = False

    # ---- 步骤⑧ retrieval-pipeline ----
    hgraph = create_case_number_theory_graph()
    pipeline = RetrievalPipeline()
    retrieval_results = pipeline.retrieve(parse_result, hgraph, top_k=5)

    print(f"\n  [INFO] 检索结果（top-5）:")
    for i, mr in enumerate(retrieval_results):
        print(f"    {i+1}. {mr.rule_id}: match_score={mr.match_score:.2f}, guard_passed={mr.guard_passed}")

    retrieval_ids = [mr.rule_id for mr in retrieval_results]
    rp_pass = "Q4" in retrieval_ids
    results["retrieval_pipeline"] = {
        "pass": rp_pass,
        "top5": retrieval_ids,
    }
    status = "✅" if rp_pass else "❌"
    print(f"  步骤⑧ retrieval-pipeline: top-5={retrieval_ids} {status}")
    if not rp_pass:
        all_pass = False

    # ---- 步骤⑩ constrained-policy ----
    # 转换：matching模块的MatchedRule → policy模块的MatchedRule
    policy_candidates = [
        PolicyMatchedRule(rule=mr.rule, match_score=mr.match_score)
        for mr in retrieval_results
    ]

    policy = ConstrainedPolicy()
    selection = policy.select(policy_candidates, parse_result.six_tuple)

    selected_id = selection.selected_rule.rule_id if selection.selected_rule else None
    print(f"\n  [INFO] 策略选择: selected={selected_id}, abstain={selection.is_abstain}")
    print(f"  [INFO] 理由: {selection.reason}")
    for rid, cv in selection.constraint_values.items():
        print(f"    {rid}: progress={cv.progress}, leakage={cv.leakage:.4f},"
              f" dependency={cv.dependency}, cost={cv.cost}")

    cp_pass = selected_id == "Q4"
    results["constrained_policy"] = {
        "pass": cp_pass,
        "selected": selected_id,
    }
    status = "✅" if cp_pass else "❌"
    print(f"  步骤⑩ constrained-policy: 选中{selected_id} {status}")
    if not cp_pass:
        all_pass = False

    return all_pass, results


# ===========================================================================
# 组合案例验证
# ===========================================================================

def test_combinatorics() -> Tuple[bool, dict]:
    """
    组合/概率案例泛化验证。

    A3后应触发Q4（理清Hamming码策略的逻辑）。
    A3状态：stall（策略逻辑需要理清），U_t有"Hamming码策略逻辑需要理清"，
    O_t有"理清Hamming码策略的猜/pass逻辑"（in_progress）。
    """
    print("\n--- 组合案例 ---")

    # 构造A3的ParseResult
    parse_result = _gold_to_parse_result(CB_GOLD_STANDARD_A3, round_index=3)

    # 打印A3状态摘要
    print(f"  A3 trajectory_nodes ({len(parse_result.trajectory_nodes)}):")
    for n in parse_result.trajectory_nodes:
        frontier = "★" if n.is_frontier else " "
        print(f"    {frontier} [{n.type}] {n.content[:50]}")
    print(f"  A3 U_t: {parse_result.six_tuple.U_t[0].description[:60] if parse_result.six_tuple.U_t else '(空)'}")
    print(f"  A3 O_t: {[(o.status, o.description[:30]) for o in parse_result.six_tuple.O_t]}")

    results = {}
    all_pass = True

    # ---- 步骤⑥ activation-score ----
    rules = build_case_combinatorics_rules()
    calculator = ActivationScoreCalculator()
    p_t = calculator.extract_features(parse_result)
    print(f"\n  [INFO] A3特征向量p_t: {p_t}")

    scored_rules = calculator.calculate(parse_result, rules, top_k=6)
    print(f"  [INFO] 激活分数排名:")
    for i, sr in enumerate(scored_rules):
        print(f"    {i+1}. {sr.rule_id}: score={sr.score:.4f}")

    top3_ids = [sr.rule_id for sr in scored_rules[:3]]
    q4_score = next((sr.score for sr in scored_rules if sr.rule_id == "Q4"), None)
    act_pass = "Q4" in top3_ids
    results["activation_score"] = {
        "pass": act_pass,
        "q4_score": q4_score,
        "top3": top3_ids,
    }
    status = "✅" if act_pass else "❌"
    print(f"  步骤⑥ activation-score: Q4={q4_score:.1f}, top-3={top3_ids} {status}")
    if not act_pass:
        all_pass = False
        print(f"  [FAIL] Q4未在top-3中")

    # ---- 步骤⑦ pattern-matching ----
    matcher = PatternMatcher()
    matched_rules = matcher.match(parse_result, scored_rules)

    print(f"\n  [INFO] 模式匹配结果:")
    for mr in matched_rules:
        print(f"    {mr.rule_id}: match_score={mr.match_score:.2f}, guard_passed={mr.guard_passed}")

    q4_match = next((mr for mr in matched_rules if mr.rule_id == "Q4"), None)
    pm_pass = q4_match is not None and q4_match.match_score >= 0.6 and q4_match.guard_passed
    results["pattern_matching"] = {
        "pass": pm_pass,
        "q4_score": q4_match.match_score if q4_match else None,
        "guard_passed": q4_match.guard_passed if q4_match else None,
    }
    status = "✅" if pm_pass else "❌"
    if q4_match:
        print(f"  步骤⑦ pattern-matching: Q4 score={q4_match.match_score:.1f}, guard通过={q4_match.guard_passed} {status}")
    else:
        print(f"  步骤⑦ pattern-matching: Q4不在匹配结果中 ❌")
    if not pm_pass:
        all_pass = False

    # ---- 步骤⑧ retrieval-pipeline ----
    hgraph = create_case_combinatorics_graph()
    pipeline = RetrievalPipeline()
    retrieval_results = pipeline.retrieve(parse_result, hgraph, top_k=5)

    print(f"\n  [INFO] 检索结果（top-5）:")
    for i, mr in enumerate(retrieval_results):
        print(f"    {i+1}. {mr.rule_id}: match_score={mr.match_score:.2f}, guard_passed={mr.guard_passed}")

    retrieval_ids = [mr.rule_id for mr in retrieval_results]
    rp_pass = "Q4" in retrieval_ids
    results["retrieval_pipeline"] = {
        "pass": rp_pass,
        "top5": retrieval_ids,
    }
    status = "✅" if rp_pass else "❌"
    print(f"  步骤⑧ retrieval-pipeline: top-5={retrieval_ids} {status}")
    if not rp_pass:
        all_pass = False

    # ---- 步骤⑩ constrained-policy ----
    # 转换：matching模块的MatchedRule → policy模块的MatchedRule
    policy_candidates = [
        PolicyMatchedRule(rule=mr.rule, match_score=mr.match_score)
        for mr in retrieval_results
    ]

    policy = ConstrainedPolicy()
    selection = policy.select(policy_candidates, parse_result.six_tuple)

    selected_id = selection.selected_rule.rule_id if selection.selected_rule else None
    print(f"\n  [INFO] 策略选择: selected={selected_id}, abstain={selection.is_abstain}")
    print(f"  [INFO] 理由: {selection.reason}")
    for rid, cv in selection.constraint_values.items():
        print(f"    {rid}: progress={cv.progress}, leakage={cv.leakage:.4f},"
              f" dependency={cv.dependency}, cost={cv.cost}")

    cp_pass = selected_id == "Q4"
    results["constrained_policy"] = {
        "pass": cp_pass,
        "selected": selected_id,
    }
    status = "✅" if cp_pass else "❌"
    print(f"  步骤⑩ constrained-policy: 选中{selected_id} {status}")
    if not cp_pass:
        all_pass = False

    return all_pass, results


# ===========================================================================
# 主入口
# ===========================================================================

def main() -> int:
    print("\n" + "=" * 60)
    print("=== P1泛化验证 ===")
    print("=" * 60)

    # 运行两个案例的验证
    nt_pass, nt_results = test_number_theory()
    cb_pass, cb_results = test_combinatorics()

    # 汇总结果
    print("\n" + "=" * 60)
    print("--- 泛化验证结果 ---")
    print("=" * 60)

    modules = ["activation_score", "pattern_matching", "retrieval_pipeline", "constrained_policy"]
    module_labels = {
        "activation_score": "activation-score",
        "pattern_matching": "pattern-matching",
        "retrieval_pipeline": "retrieval-pipeline",
        "constrained_policy": "constrained-policy",
    }

    all_module_pass = True
    for mod in modules:
        nt_ok = nt_results.get(mod, {}).get("pass", False)
        cb_ok = cb_results.get(mod, {}).get("pass", False)
        passed = nt_ok and cb_ok
        count = sum([nt_ok, cb_ok])
        status = "✅" if passed else "❌"
        label = module_labels[mod]
        if "activation" in mod:
            print(f"{label}: {status} 通过（{count}/2案例正确Q排top-3）")
        elif "pattern" in mod:
            print(f"{label}: {status} 通过（{count}/2案例正确Q match_score≥0.6）")
        elif "retrieval" in mod:
            print(f"{label}: {status} 通过（{count}/2案例正确Q在top-5）")
        elif "constrained" in mod:
            print(f"{label}: {status} 通过（{count}/2案例选中正确Q）")
        if not passed:
            all_module_pass = False

    print()
    if all_module_pass and nt_pass and cb_pass:
        print("🎉 P1泛化验证通过！")
        print("   activation-score + pattern-matching + retrieval-pipeline + constrained-policy")
        print("   在数论和组合2个新案例上全部通过，P1原语可泛化。")
        return 0
    else:
        print("❌ P1泛化验证未通过")
        if not nt_pass:
            print("   数论案例失败")
        if not cb_pass:
            print("   组合案例失败")
        # 记录失败原因
        for mod in modules:
            nt_ok = nt_results.get(mod, {}).get("pass", False)
            cb_ok = cb_results.get(mod, {}).get("pass", False)
            if not nt_ok:
                print(f"   数论-{module_labels[mod]}: 失败，结果={nt_results.get(mod)}")
            if not cb_ok:
                print(f"   组合-{module_labels[mod]}: 失败，结果={cb_results.get(mod)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
