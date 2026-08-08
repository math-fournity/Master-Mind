"""
P1核心检索模块测试脚本。

测试1：activation-score（激活分数）
测试2：pattern-matching（模式匹配）
测试3：retrieval-pipeline（检索管线）

运行：
    cd ~/master-mind-glm5.2-worktree
    .venv/bin/python3 -m xishujuzhen.research_runtime.test_p1_core
"""

import sys

from xishujuzhen.research_runtime.parser.models import (
    ParseRequest,
    ParseResult,
    SixTuple,
    TurnRecord,
)
from xishujuzhen.research_runtime.parser.parser import MathParser
from xishujuzhen.research_runtime.parser.llm_parser import LLMParser
from xishujuzhen.research_runtime.parser.test_data.case_253 import (
    PROBLEM_TEXT,
    QA_SEQUENCE,
    PREVIOUS_SIX_TUPLE_A6,
)
from xishujuzhen.research_runtime.parser.test_data.mock_llm_responses import (
    make_mock_provider,
)
from xishujuzhen.research_runtime.hgraph import (
    create_case_253_graph,
    build_case_253_rules,
)
from xishujuzhen.research_runtime.activation import (
    ActivationScoreCalculator,
    ScoredRule,
)
from xishujuzhen.research_runtime.matching import (
    PatternMatcher,
    MatchedRule,
)
from xishujuzhen.research_runtime.retrieval import RetrievalPipeline


# ---------------------------------------------------------------------------
# 辅助函数：构造A7的ParseResult
# ---------------------------------------------------------------------------

def build_a7_parse_result() -> ParseResult:
    """
    用253号A7的mock数据，通过MathParser解析，构造A7的ParseResult。

    复用parser/test_parser.py的测试逻辑：
    - 构造mock provider
    - 构造A7的ParseRequest（含A6之后的六元组作为previous_six_tuple）
    - 调用MathParser.parse()
    """
    mock_provider = make_mock_provider()
    llm_parser = LLMParser(mock_response_provider=mock_provider)
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
    a7_data = QA_SEQUENCE[6]
    request = ParseRequest(
        agent_output=a7_data["a_text"],
        round_index=7,
        problem_text=PROBLEM_TEXT,
        history=history,
        current_six_tuple=previous_six_tuple,
        run_id="test_p1_core_a7",
        model_version="mock",
    )

    return math_parser.parse(request)


# ---------------------------------------------------------------------------
# 测试1：activation-score
# ---------------------------------------------------------------------------

def test_activation_score(a7_result: ParseResult) -> bool:
    print("=" * 60)
    print("测试1：activation-score（激活分数）")
    print("=" * 60)

    errors = []

    # 获取253号10个Q作为规则集
    rules = build_case_253_rules()

    # 创建激活分数计算器
    calculator = ActivationScoreCalculator()

    # 提取特征向量p_t
    p_t = calculator.extract_features(a7_result)
    print(f"  [INFO] A7特征向量p_t: {p_t}")
    print(f"         stability_equation_presence={p_t[0]}")
    print(f"         integer_dependency={p_t[1]}")
    print(f"         lower_bound_demand={p_t[2]}")
    print(f"         knowledge_gap={p_t[3]}")
    print(f"         reasoning_depth={p_t[4]}")
    print(f"         representation_richness={p_t[5]}")
    print(f"         stall_severity={p_t[6]}")

    # 验证特征向量
    if p_t[0] != 1.0:
        errors.append(f"stability_equation_presence应为1.0，实际{p_t[0]}")
    print(f"  [OK] stability_equation_presence={p_t[0]} (期望1.0)")

    if p_t[1] != 1.0:
        errors.append(f"integer_dependency应为1.0，实际{p_t[1]}")
    print(f"  [OK] integer_dependency={p_t[1]} (期望1.0)")

    if p_t[2] != 1.0:
        errors.append(f"lower_bound_demand应为1.0，实际{p_t[2]}")
    print(f"  [OK] lower_bound_demand={p_t[2]} (期望1.0)")

    if p_t[6] != 0.0:
        errors.append(f"stall_severity应为0.0（A7无stall节点），实际{p_t[6]}")
    print(f"  [OK] stall_severity={p_t[6]} (期望0.0)")

    # 计算激活分数
    scored_rules = calculator.calculate(a7_result, rules, top_k=10)

    # 打印所有规则的激活分数
    print(f"\n  [INFO] 激活分数排名（top-10）:")
    for i, sr in enumerate(scored_rules):
        print(f"    {i + 1}. {sr.rule_id}: score={sr.score:.4f}")

    # 验证Q8的激活分数排在top-3
    top3_ids = [sr.rule_id for sr in scored_rules[:3]]
    if "Q8" not in top3_ids:
        errors.append(f"Q8应在top-3中，实际top-3={top3_ids}")
    print(f"\n  [OK] top-3规则: {top3_ids}，Q8在其中")

    # 验证Q1的激活分数低（触发条件不匹配A7后的状态）
    q1_score = next((sr.score for sr in scored_rules if sr.rule_id == "Q1"), None)
    q8_score = next((sr.score for sr in scored_rules if sr.rule_id == "Q8"), None)
    if q1_score is None or q8_score is None:
        errors.append("Q1或Q8不在结果中")
    else:
        print(f"  [INFO] Q1 score={q1_score:.4f}, Q8 score={q8_score:.4f}")
        if q1_score >= q8_score:
            errors.append(f"Q1分数应低于Q8，Q1={q1_score}, Q8={q8_score}")
        if q1_score > 0.5:
            errors.append(f"Q1分数应低（≤0.5），实际{q1_score}")
    print(f"  [OK] Q1分数低（{q1_score:.4f} < Q8的{q8_score:.4f}）")

    if errors:
        print(f"\n  [FAIL] 测试1失败，{len(errors)}个错误：")
        for e in errors:
            print(f"    - {e}")
        return False
    print(f"\n  [PASS] 测试1全部通过\n")
    return True


# ---------------------------------------------------------------------------
# 测试2：pattern-matching
# ---------------------------------------------------------------------------

def test_pattern_matching(a7_result: ParseResult) -> bool:
    print("=" * 60)
    print("测试2：pattern-matching（模式匹配）")
    print("=" * 60)

    errors = []

    # 先用activation-score获取top候选
    rules = build_case_253_rules()
    calculator = ActivationScoreCalculator()
    scored_rules = calculator.calculate(a7_result, rules, top_k=10)

    # 创建模式匹配器
    matcher = PatternMatcher()

    # 对所有候选做模式匹配
    matched_rules = matcher.match(a7_result, scored_rules)

    # 打印所有匹配结果
    print(f"  [INFO] 模式匹配结果:")
    for mr in matched_rules:
        print(
            f"    {mr.rule_id}: match_score={mr.match_score:.2f}, "
            f"guard_passed={mr.guard_passed}"
        )

    # 验证Q8的匹配分数≥0.8（LHS匹配+Guard通过）
    q8_match = next((mr for mr in matched_rules if mr.rule_id == "Q8"), None)
    if q8_match is None:
        errors.append("Q8不在匹配结果中")
    else:
        print(f"\n  [INFO] Q8: match_score={q8_match.match_score:.2f}, guard_passed={q8_match.guard_passed}")
        if q8_match.match_score < 0.8:
            errors.append(f"Q8匹配分数应≥0.8，实际{q8_match.match_score}")
        if not q8_match.guard_passed:
            errors.append("Q8 guard应通过")
    print(f"  [OK] Q8 match_score={q8_match.match_score:.2f} (≥0.8), guard_passed={q8_match.guard_passed}")

    # 验证Q9的匹配分数~0.5（部分匹配，Guard不通过）
    q9_match = next((mr for mr in matched_rules if mr.rule_id == "Q9"), None)
    if q9_match is None:
        errors.append("Q9不在匹配结果中")
    else:
        print(f"  [INFO] Q9: match_score={q9_match.match_score:.2f}, guard_passed={q9_match.guard_passed}")
        # Q9的LHS节点类型{claim,stall}与A7的{representation,resolution}对称差=4
        # 同规模不同类型 → 0.5部分匹配
        if not (0.3 <= q9_match.match_score <= 0.6):
            errors.append(f"Q9匹配分数应在0.3-0.6之间（~0.5），实际{q9_match.match_score}")
        if q9_match.guard_passed:
            errors.append("Q9 guard应不通过（A7的U_t无knowledge_gap标注）")
    print(f"  [OK] Q9 match_score={q9_match.match_score:.2f} (~0.5), guard_passed={q9_match.guard_passed} (False)")

    if errors:
        print(f"\n  [FAIL] 测试2失败，{len(errors)}个错误：")
        for e in errors:
            print(f"    - {e}")
        return False
    print(f"\n  [PASS] 测试2全部通过\n")
    return True


# ---------------------------------------------------------------------------
# 测试3：retrieval-pipeline
# ---------------------------------------------------------------------------

def test_retrieval_pipeline(a7_result: ParseResult) -> bool:
    print("=" * 60)
    print("测试3：retrieval-pipeline（检索管线）")
    print("=" * 60)

    errors = []

    # 创建H图存储（253号10个Q）
    hgraph = create_case_253_graph()

    # 创建检索管线
    pipeline = RetrievalPipeline()

    # 种子选择
    seeds = pipeline.select_seeds(a7_result)
    print(f"  [INFO] 种子选择: {seeds}")
    if not seeds:
        print(f"  [WARN] 无种子（A7前沿节点的数学对象可能为空）")

    # 完整检索流程（top_k=5）
    top_k = 5
    results = pipeline.retrieve(a7_result, hgraph, top_k=top_k)

    # 打印检索结果
    print(f"\n  [INFO] 检索结果（top-{top_k}）:")
    for i, mr in enumerate(results):
        print(
            f"    {i + 1}. {mr.rule_id}: match_score={mr.match_score:.2f}, "
            f"guard_passed={mr.guard_passed}"
        )

    # 验证Q8在返回结果中
    result_ids = [mr.rule_id for mr in results]
    if "Q8" not in result_ids:
        errors.append(f"Q8应在检索结果中，实际结果={result_ids}")
    print(f"\n  [OK] Q8在检索结果中: {'Q8' in result_ids}")

    # 验证结果规模≤top_k
    if len(results) > top_k:
        errors.append(f"结果规模应≤{top_k}，实际{len(results)}")
    print(f"  [OK] 结果规模={len(results)} (≤{top_k})")

    # 验证结果按match_score降序排列
    scores = [mr.match_score for mr in results]
    if scores != sorted(scores, reverse=True):
        errors.append(f"结果应按match_score降序排列，实际={scores}")
    print(f"  [OK] 结果按match_score降序排列: {scores}")

    # 验证Q8的匹配分数和guard状态
    q8_result = next((mr for mr in results if mr.rule_id == "Q8"), None)
    if q8_result is None:
        errors.append("Q8应在检索结果中")
    else:
        if q8_result.match_score < 0.8:
            errors.append(f"Q8匹配分数应≥0.8，实际{q8_result.match_score}")
        if not q8_result.guard_passed:
            errors.append("Q8 guard应通过")
        print(f"  [OK] Q8: match_score={q8_result.match_score:.2f}, guard_passed={q8_result.guard_passed}")

    if errors:
        print(f"\n  [FAIL] 测试3失败，{len(errors)}个错误：")
        for e in errors:
            print(f"    - {e}")
        return False
    print(f"\n  [PASS] 测试3全部通过\n")
    return True


# ---------------------------------------------------------------------------
# 主入口
# ---------------------------------------------------------------------------

def main() -> int:
    print("\n" + "#" * 60)
    print("# P1核心检索模块测试：activation-score + pattern-matching + retrieval-pipeline")
    print("#" * 60 + "\n")

    # 构造A7的ParseResult
    print("构造A7的ParseResult...\n")
    a7_result = build_a7_parse_result()

    # 打印A7解析结果摘要
    print(f"  A7 trajectory_nodes ({len(a7_result.trajectory_nodes)}):")
    for n in a7_result.trajectory_nodes:
        frontier = "★" if n.is_frontier else " "
        print(f"    {frontier} [{n.type}] {n.content[:50]}")
    print(f"  A7 U_t ({len(a7_result.six_tuple.U_t)}):")
    for u in a7_result.six_tuple.U_t:
        print(f"    - [{u.severity}] {u.description[:60]}")
    print(f"  A7 O_t ({len(a7_result.six_tuple.O_t)}):")
    for o in a7_result.six_tuple.O_t:
        print(f"    - [{o.status}] {o.description[:60]}")
    print(f"  A7 R_t ({len(a7_result.six_tuple.R_t)}):")
    for r in a7_result.six_tuple.R_t:
        print(f"    - {r.name}: {r.description[:40]}")
    print()

    # 运行三个测试
    results = []
    results.append(("activation-score", test_activation_score(a7_result)))
    results.append(("pattern-matching", test_pattern_matching(a7_result)))
    results.append(("retrieval-pipeline", test_retrieval_pipeline(a7_result)))

    # 汇总
    print("=" * 60)
    print("测试汇总")
    print("=" * 60)
    all_pass = True
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")
        if not passed:
            all_pass = False

    print()
    if all_pass:
        print(">>> 全部测试通过 <<<")
        return 0
    else:
        print(">>> 存在失败测试 <<<")
        return 1


if __name__ == "__main__":
    sys.exit(main())
