"""
P1决策模块测试脚本：constrained-policy + hint-gradient + gain-attribution。

测试1：constrained-policy
- 构造A7后的六元组（O_t中有"估计D的下界"open义务）
- 构造候选列表：Q8（match_score=0.9）+ Q9（match_score=0.5）
- 用ConstrainedPolicy.select()选择
- 验证选中Q8而非Q9
- 验证Q9的泄漏估计高（包含"badly approximable"）

测试2：hint-gradient
- 构造Q9（leakage_risk > 0.5）
- 用HintGradient.degrade()降级
- 验证降级后Level更高（从0.2升到0.5或更高）
- 验证降级后去掉了特定知识

测试3：gain-attribution
- 模拟253号10轮QA的增益归因
- 记录Q1-Q10
- 对A8归因：验证进展增量归因给Q8
- 反事实估计：验证"没有Q8不太可能自发分析D的下界"

运行：
    cd /data/master-mind-glm5.2-grove
    .venv/bin/python3 -m xishujuzhen.research_runtime.test_p1_decision
"""

from .hgraph.hgraph_store import HeuristicRule, HeuristicRuleGraph
from .hgraph.case_253_rules import build_case_253_rules
from .parser.models import (
    ParseResult,
    SixTuple,
    VerifiedProp,
    Conjecture,
    Obligation,
    Representation,
    Evidence,
    UnsolvedProblem,
)
from .policy.constrained_optimizer import (
    ConstrainedPolicy,
    MatchedRule,
    leakage_risk,
)
from .gradient.hint_gradient import HintGradient
from .attribution.gain_attribution import GainAttribution


# ===========================================================================
# 辅助：构造A7后的六元组（O_t中有"估计D的下界"open义务）
# ===========================================================================

def _build_six_tuple_after_a7() -> SixTuple:
    """构造A7后的六元组（253号A7解析结果，参考GOLD_STANDARD_A7）。"""
    return SixTuple(
        V_t=[
            VerifiedProp(statement="中心化：x_i=a_i-1, Σx_i=0, Σx_i²=n, Σx_i³=-n",
                         verified_by="logic", verified_at_round=1),
            VerifiedProp(statement="q(x)=x²+x-1, 根r,s, s-r=√5",
                         verified_by="logic", verified_at_round=2),
            VerifiedProp(statement="两个恒等式：Σq(x_i)=0, Σx_i·q(x_i)=0",
                         verified_by="logic", verified_at_round=3),
            VerifiedProp(statement="紧性归约：δ≤1时所有x_i落在[r-1,s+1]",
                         verified_by="logic", verified_at_round=4),
            VerifiedProp(statement="投影：ζ_i∈{r,s}, e_i=x_i-ζ_i, q(x_i)=±√5·e_i+e_i²",
                         verified_by="logic", verified_at_round=6),
        ],
        F_t=[
            Conjecture(statement="稳定性方程5D=3√5(B_r-B_s)+2C", status="exploring"),
            Conjecture(statement="D=√5(pn-k), p=(5-√5)/10", status="exploring"),
        ],
        O_t=[
            Obligation(description="复用q(x)和恒等式", status="solved"),
            Obligation(description="做紧性归约", status="solved"),
            Obligation(description="从矩条件和投影展开式导出恒等式", status="solved"),
            Obligation(description="估计D的下界", status="open"),
            Obligation(description="把D下界传递到δ下界", status="open"),
            Obligation(description="证明极差≥√5+C₂n^(-3/2)", status="open"),
        ],
        R_t=[
            Representation(name="中心化", description="x_i=a_i-1", introduced_at_round=1),
            Representation(name="紧性归约", description="R=√5+δ, δ≤1", introduced_at_round=4),
            Representation(name="投影到根", description="ζ_i∈{r,s}, e_i=x_i-ζ_i", introduced_at_round=6),
            Representation(name="稳定性方程表示", description="D=√5(pn-k), A_r,A_s,B_r,B_s,C", introduced_at_round=7),
        ],
        E_t=[],
        U_t=[
            UnsolvedProblem(
                description="D的量级问题——D=√5(pn-k)取决于整数k和n的关系，需要估计|D|的下界",
                severity="blocking", identified_at_round=7,
            ),
        ],
    )


def _build_q8_rule() -> HeuristicRule:
    """构造Q8规则（量级感知级，Level=0.5）。"""
    return HeuristicRule(
        rule_id="Q8",
        lhs={"node_types": ["resolution"], "feature": "稳定性方程中有量取决于整数关系"},
        guard=["D取决于整数k和n的关系"],
        rhs="Q8: 稳定性方程中有量取决于整数关系，你能估计D的下界吗？",
        level=0.5,
        non_specificity=0.7,
        lifecycle_state="published",
        obligation_id="估计D的下界",
    )


def _build_q9_rule() -> HeuristicRule:
    """构造Q9规则（知识注入级，Level=0.2，包含"badly approximable"特定知识）。"""
    return HeuristicRule(
        rule_id="Q9",
        lhs={"node_types": ["claim", "stall"], "feature": "D≠0但下界未知"},
        guard=["U_t中有knowledge_gap"],
        # rhs包含特定知识"badly approximable"（对应253号Q9原文）
        rhs="Q9: D≠0但下界未知，p是二次无理数，它是badly approximable，"
            "你能用这个事实推出|D|的下界吗？",
        level=0.2,
        non_specificity=0.9,
        lifecycle_state="published",
        obligation_id="用数论性质估计D下界",
    )


# ===========================================================================
# 测试1：constrained-policy
# ===========================================================================

def test_constrained_policy() -> None:
    """测试1：constrained-policy受约束多目标策略。"""
    print("\n" + "=" * 70)
    print("测试1：constrained-policy（受约束多目标策略）")
    print("=" * 70)

    six_tuple = _build_six_tuple_after_a7()
    q8 = _build_q8_rule()
    q9 = _build_q9_rule()

    # 构造候选列表：Q8（match_score=0.9）+ Q9（match_score=0.5）
    matched_rules = [
        MatchedRule(rule=q8, match_score=0.9),
        MatchedRule(rule=q9, match_score=0.5),
    ]

    policy = ConstrainedPolicy()

    # 验证Q9的泄漏估计高（包含"badly approximable"）
    q9_leakage = policy.estimate_leakage(q9)
    q8_leakage = policy.estimate_leakage(q8)
    print(f"  Q8 leakage = {q8_leakage:.4f}（期望≈0.15）")
    print(f"  Q9 leakage = {q9_leakage:.4f}（期望≈0.58，含特定知识加成）")
    assert q9_leakage > 0.5, f"Q9泄漏应>0.5，实际={q9_leakage}"
    assert q9_leakage > q8_leakage, "Q9泄漏应高于Q8"

    # 验证进展估计：Q8和Q9都能匹配open义务"估计D的下界"
    q8_progress = policy.estimate_progress(q8, six_tuple)
    q9_progress = policy.estimate_progress(q9, six_tuple)
    print(f"  Q8 progress = {q8_progress}（期望1.0，义务ID匹配）")
    print(f"  Q9 progress = {q9_progress}（期望1.0，义务ID子串匹配）")
    assert q8_progress == 1.0, f"Q8进展应为1.0，实际={q8_progress}"
    assert q9_progress == 1.0, f"Q9进展应为1.0，实际={q9_progress}"

    # 用ConstrainedPolicy.select()选择
    result = policy.select(matched_rules, six_tuple)
    print(f"  选择结果：selected={result.selected_rule.rule_id if result.selected_rule else None},"
          f" abstain={result.is_abstain}")
    print(f"  理由：{result.reason}")
    for rid, cv in result.constraint_values.items():
        print(f"    {rid}: progress={cv.progress}, leakage={cv.leakage:.4f},"
              f" dependency={cv.dependency}, cost={cv.cost}")

    # 验证选中Q8而非Q9
    assert result.selected_rule is not None, "应选中一条规则"
    assert result.selected_rule.rule_id == "Q8", (
        f"应选中Q8（Pareto最优：同进展、低泄漏），实际选中{result.selected_rule.rule_id}"
    )
    assert not result.is_abstain, "不应放弃（Q8泄漏低）"

    print("  ✓ 验证通过：选中Q8而非Q9，Q9泄漏估计高")


# ===========================================================================
# 测试2：hint-gradient
# ===========================================================================

def test_hint_gradient() -> None:
    """测试2：hint-gradient提示梯度降级。"""
    print("\n" + "=" * 70)
    print("测试2：hint-gradient（提示梯度降级）")
    print("=" * 70)

    q8 = _build_q8_rule()
    q9 = _build_q9_rule()

    # 构造Q9（leakage_risk > 0.5）
    q9_risk = leakage_risk(q9)
    print(f"  Q9 leakage_risk = {q9_risk:.4f}（期望>0.5触发降级）")
    assert q9_risk > 0.5, f"Q9泄漏应>0.5，实际={q9_risk}"

    # 候选列表：Q8 + Q9（Q8义务ID不同，无法替代Q9）
    matched_rules = [
        MatchedRule(rule=q8, match_score=0.9),
        MatchedRule(rule=q9, match_score=0.5),
    ]

    gradient = HintGradient()

    # 用HintGradient.degrade()降级
    degraded = gradient.degrade(q9, matched_rules)
    print(f"  降级后：rule_id={degraded.rule_id}, level={degraded.level},"
          f" rhs={degraded.rhs!r}")
    print(f"  原Q9：level={q9.level}, rhs={q9.rhs!r}")

    # 验证降级后Level更高（从0.2升到0.5或更高）
    assert degraded.level > q9.level, (
        f"降级后Level应更高：原={q9.level}, 降级后={degraded.level}"
    )
    assert degraded.level >= 0.5, f"降级后Level应>=0.5，实际={degraded.level}"

    # 验证降级后去掉了特定知识（不含"badly approximable"）
    assert "badly approximable" not in degraded.rhs.lower(), (
        f"降级后rhs应去掉特定知识'badly approximable'，实际={degraded.rhs!r}"
    )

    # 验证降级后泄漏风险降低
    degraded_risk = leakage_risk(degraded)
    print(f"  降级后 leakage_risk = {degraded_risk:.4f}（应<原{q9_risk:.4f}）")
    assert degraded_risk < q9_risk, "降级后泄漏风险应降低"

    # 额外验证：generate_gradient从H图生成梯度
    hgraph = HeuristicRuleGraph()
    for rule in build_case_253_rules():
        hgraph.add_rule(rule)
    # 添加一个同义务ID的更高Level规则用于梯度测试
    hgraph.add_rule(HeuristicRule(
        rule_id="Q8b",
        lhs={"node_types": ["resolution"], "feature": "D量级"},
        rhs="D能等于0吗？",
        level=0.5,
        non_specificity=0.7,
        obligation_id="估计D的下界",
    ))
    grad_list = gradient.generate_gradient("估计D的下界", hgraph)
    print(f"  generate_gradient('估计D的下界')：{[r.rule_id for r in grad_list]}")
    assert len(grad_list) >= 1, "梯度列表不应为空"
    # 验证按Level降序排列
    levels = [r.level for r in grad_list]
    assert levels == sorted(levels, reverse=True), f"梯度应按Level降序，实际={levels}"

    print("  ✓ 验证通过：Q9降级后Level升高、去掉特定知识、泄漏风险降低")


# ===========================================================================
# 测试3：gain-attribution
# ===========================================================================

def test_gain_attribution() -> None:
    """测试3：gain-attribution增益归因。"""
    print("\n" + "=" * 70)
    print("测试3：gain-attribution（增益归因）")
    print("=" * 70)

    # 构建253号10条规则
    rules = {r.rule_id: r for r in build_case_253_rules()}

    attribution = GainAttribution()

    # 记录Q1-Q10提示链
    for i in range(1, 11):
        rule_id = f"Q{i}"
        attribution.record_hint(i, rules[rule_id])
    print(f"  已记录提示链 Q1-Q10：{sorted(attribution._hint_chain.keys())}")

    # 构造A7后的六元组（previous，即A8的previous_six_tuple）
    six_tuple_after_a7 = _build_six_tuple_after_a7()

    # 构造A8后的六元组（current，即A8的parse_result.six_tuple）
    # A8：分析D=√5(pn-k)，D≠0（p是无理数），但|D|下界未知——知识瓶颈
    six_tuple_after_a8 = SixTuple(
        V_t=six_tuple_after_a7.V_t + [
            # A8新增：D≠0
            VerifiedProp(
                statement="D≠0：p=(5-√5)/10是无理数，k/n≠p，故D=√5(pn-k)≠0",
                verified_by="logic", verified_at_round=8,
            ),
        ],
        F_t=six_tuple_after_a7.F_t + [
            Conjecture(statement="D的下界未知，需要数论性质", status="exploring"),
        ],
        O_t=[
            Obligation(description="复用q(x)和恒等式", status="solved"),
            Obligation(description="做紧性归约", status="solved"),
            Obligation(description="从矩条件和投影展开式导出恒等式", status="solved"),
            # "估计D的下界"仍open（A8只证了D≠0，未得下界）
            Obligation(description="估计D的下界", status="open"),
            Obligation(description="把D下界传递到δ下界", status="open"),
            Obligation(description="证明极差≥√5+C₂n^(-3/2)", status="open"),
        ],
        R_t=six_tuple_after_a7.R_t,
        E_t=[],
        U_t=[
            UnsolvedProblem(
                description="D的量级问题——D=√5(pn-k)取决于整数k和n的关系，需要估计|D|的下界",
                severity="blocking", identified_at_round=7,
            ),
        ],
    )

    parse_result_a8 = ParseResult(six_tuple=six_tuple_after_a8, parse_confidence=0.85)

    # 对A8归因：验证进展增量归因给Q8
    gain_record = attribution.attribute_gain(
        round_index=8,
        parse_result=parse_result_a8,
        previous_six_tuple=six_tuple_after_a7,
    )
    print(f"  A8归因：rule_id={gain_record.rule_id},"
          f" progress_delta={gain_record.progress_delta},"
          f" type={gain_record.attribution_type}")
    print(f"  细节：{gain_record.detail}")

    # 验证归因给Q8
    assert gain_record.rule_id == "Q8", (
        f"A8的进展增量应归因给Q8，实际归因给{gain_record.rule_id}"
    )
    # 验证进展增量=1（V_t新增1条"D≠0"，O_t无open→solved）
    assert gain_record.progress_delta == 1.0, (
        f"A8进展增量应为1（V_t新增1），实际={gain_record.progress_delta}"
    )
    assert gain_record.attribution_type == "progress"

    # 反事实估计：验证"没有Q8不太可能自发分析D的下界"
    counterfactual = attribution.estimate_counterfactual(
        round_index=8,
        gain_record=gain_record,
        six_tuple=six_tuple_after_a7,  # A7后六元组，U_t中有blocking
    )
    print(f"  反事实估计：{counterfactual}")

    # Q8的obligation_id="估计D的下界"，U_t中"D的量级问题...估计|D|的下界"为blocking
    assert "没有Q8" in counterfactual, f"反事实估计应提及'没有Q8'，实际={counterfactual}"
    assert "不太可能自发" in counterfactual, (
        f"反事实估计应含'不太可能自发'（blocking义务），实际={counterfactual}"
    )

    # 额外验证：minor义务的反事实估计
    minor_six_tuple = SixTuple(
        U_t=[UnsolvedProblem(description="估计D的下界", severity="minor")],
    )
    minor_cf = attribution.estimate_counterfactual(
        round_index=8, gain_record=gain_record, six_tuple=minor_six_tuple,
    )
    print(f"  minor义务反事实：{minor_cf}")
    assert "也可能达到进展" in minor_cf, (
        f"minor义务应'也可能达到进展'，实际={minor_cf}"
    )

    print("  ✓ 验证通过：A8进展增量归因给Q8，反事实估计为blocking")


# ===========================================================================
# 主入口
# ===========================================================================

def main() -> None:
    """运行全部P1决策模块测试。"""
    print("=" * 70)
    print("P1决策模块测试：constrained-policy + hint-gradient + gain-attribution")
    print("=" * 70)

    test_constrained_policy()
    test_hint_gradient()
    test_gain_attribution()

    print("\n" + "=" * 70)
    print("全部测试通过 ✓")
    print("=" * 70)


if __name__ == "__main__":
    main()
