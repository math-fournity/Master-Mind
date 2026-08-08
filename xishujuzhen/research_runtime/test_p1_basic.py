"""
P1基础模块测试脚本。

测试1：H图存储（hgraph）
测试2：生命周期管理（lifecycle）
测试3：预算管理（budget）

运行：
    cd ~/master-mind-glm5.2-worktree
    .venv/bin/python3 -m xishujuzhen.research_runtime.test_p1_basic
"""

import sys

from xishujuzhen.research_runtime.hgraph import (
    HeuristicRule,
    HeuristicRuleGraph,
    build_case_253_rules,
    create_case_253_graph,
)
from xishujuzhen.research_runtime.lifecycle import LifecycleManager, LifecycleState
from xishujuzhen.research_runtime.budget import BudgetManager, BudgetType


# ---------------------------------------------------------------------------
# 测试1：H图存储
# ---------------------------------------------------------------------------

def test_hgraph_store() -> None:
    print("=" * 60)
    print("测试1：H图存储（hgraph）")
    print("=" * 60)

    errors = []

    # 初始化253号10个Q为规则
    graph = create_case_253_graph()

    # 验证10条规则正确存储
    all_rules = graph.get_all_rules()
    if len(all_rules) != 10:
        errors.append(f"规则数应为10，实际{len(all_rules)}")
    print(f"  [OK] 规则总数: {len(all_rules)}")

    # 验证rule_id为Q1-Q10
    expected_ids = {f"Q{i}" for i in range(1, 11)}
    actual_ids = {r.rule_id for r in all_rules}
    if actual_ids != expected_ids:
        errors.append(f"rule_id不匹配，期望{expected_ids}，实际{actual_ids}")
    print(f"  [OK] rule_id集合: {sorted(actual_ids)}")

    # 验证所有规则为published状态
    for r in all_rules:
        if r.lifecycle_state != "published":
            errors.append(f"{r.rule_id}状态应为published，实际{r.lifecycle_state}")
    print(f"  [OK] 所有规则状态为published")

    # 验证get_published_rules()返回10条
    published = graph.get_published_rules()
    if len(published) != 10:
        errors.append(f"published规则数应为10，实际{len(published)}")
    print(f"  [OK] get_published_rules()返回: {len(published)}条")

    # 验证Level和非特定性（抽查Q1, Q6, Q9）
    q1 = graph.get_rule("Q1")
    if q1 is None or q1.level != 1.0 or q1.non_specificity != 0.9:
        errors.append(f"Q1 Level/非特定性错误: {q1}")
    q6 = graph.get_rule("Q6")
    if q6 is None or q6.level != 0.7 or q6.non_specificity != 0.8:
        errors.append(f"Q6 Level/非特定性错误: {q6}")
    q9 = graph.get_rule("Q9")
    if q9 is None or q9.level != 0.2 or q9.non_specificity != 0.9:
        errors.append(f"Q9 Level/非特定性错误: {q9}")
    print(f"  [OK] Level/非特定性抽查通过 (Q1: L={q1.level},ns={q1.non_specificity}; "
          f"Q6: L={q6.level},ns={q6.non_specificity}; Q9: L={q9.level},ns={q9.non_specificity})")

    # 验证LHS定义（抽查Q8的guard）
    q8 = graph.get_rule("Q8")
    if q8 is None or "D取决于整数k和n的关系" not in q8.guard:
        errors.append(f"Q8 guard错误: {q8}")
    print(f"  [OK] Q8 guard: {q8.guard}")

    # 验证义务ID标注（抽查Q5）
    q5 = graph.get_rule("Q5")
    if q5 is None or q5.obligation_id != "识别差距":
        errors.append(f"Q5 obligation_id错误: {q5}")
    print(f"  [OK] Q5 obligation_id: {q5.obligation_id}")

    # 验证build_case_253_rules独立可用
    rules_list = build_case_253_rules()
    if len(rules_list) != 10:
        errors.append(f"build_case_253_rules返回数应为10，实际{len(rules_list)}")
    print(f"  [OK] build_case_253_rules()返回: {len(rules_list)}条")

    if errors:
        print(f"\n  [FAIL] 测试1失败，{len(errors)}个错误：")
        for e in errors:
            print(f"    - {e}")
        return False
    print(f"\n  [PASS] 测试1全部通过\n")
    return True


# ---------------------------------------------------------------------------
# 测试2：生命周期管理
# ---------------------------------------------------------------------------

def test_lifecycle() -> None:
    print("=" * 60)
    print("测试2：生命周期管理（lifecycle）")
    print("=" * 60)

    errors = []

    # 初始化253号10个Q为published
    graph = create_case_253_graph()
    manager = LifecycleManager(graph)

    # 验证253号10个Q为published
    for i in range(1, 11):
        qid = f"Q{i}"
        if not manager.is_publishable(qid):
            errors.append(f"{qid}应为publishable")
    print(f"  [OK] 253号10个Q均为published（可发布）")

    # 验证published状态的规则可被检索
    publishable = manager.get_publishable_rules()
    if len(publishable) != 10:
        errors.append(f"可发布规则数应为10，实际{len(publishable)}")
    print(f"  [OK] get_publishable_rules()返回: {len(publishable)}条")

    # 测试状态转移：observed→candidate→intervened→validated→published
    # 用一条新规则走完整链
    test_rule = HeuristicRule(
        rule_id="TEST_R1",
        lhs={"node_types": ["observation"], "feature": "测试模式"},
        guard=[],
        rhs="测试提示",
        level=0.5,
        non_specificity=0.5,
        lifecycle_state="observed",
        obligation_id="测试义务",
    )
    graph.add_rule(test_rule)

    # observed -> candidate
    if not manager.can_transition("TEST_R1", "observed", "candidate"):
        errors.append("observed->candidate应合法")
    if not manager.transition("TEST_R1", "candidate"):
        errors.append("observed->candidate转移失败")
    print(f"  [OK] observed->candidate 转移成功")

    # candidate -> intervened
    if not manager.transition("TEST_R1", "intervened"):
        errors.append("candidate->intervened转移失败")
    print(f"  [OK] candidate->intervened 转移成功")

    # intervened -> validated
    if not manager.transition("TEST_R1", "validated"):
        errors.append("intervened->validated转移失败")
    print(f"  [OK] intervened->validated 转移成功")

    # validated -> published
    if not manager.transition("TEST_R1", "published"):
        errors.append("validated->published转移失败")
    print(f"  [OK] validated->published 转移成功")

    # 验证TEST_R1现在可发布
    if not manager.is_publishable("TEST_R1"):
        errors.append("TEST_R1转移到published后应可发布")
    print(f"  [OK] TEST_R1 现在可发布")

    # 测试非法转移（published -> observed 不合法）
    if manager.can_transition("TEST_R1", "published", "observed"):
        errors.append("published->observed应不合法")
    if manager.transition("TEST_R1", "observed"):
        errors.append("published->observed转移应失败")
    print(f"  [OK] 非法转移 published->observed 被拒绝")

    # 测试 published -> retired 合法
    if not manager.transition("TEST_R1", "retired"):
        errors.append("published->retired转移应成功")
    print(f"  [OK] published->retired 转移成功")

    # retired是终态，不能再转移
    if manager.transition("TEST_R1", "published"):
        errors.append("retired->published应失败（终态）")
    print(f"  [OK] retired终态无法再转移")

    # 验证转移条件描述
    cond = manager.transition_condition("observed", "candidate")
    if not cond:
        errors.append("observed->candidate应有转移条件描述")
    print(f"  [OK] 转移条件描述: observed->candidate = '{cond}'")

    if errors:
        print(f"\n  [FAIL] 测试2失败，{len(errors)}个错误：")
        for e in errors:
            print(f"    - {e}")
        return False
    print(f"\n  [PASS] 测试2全部通过\n")
    return True


# ---------------------------------------------------------------------------
# 测试3：预算管理
# ---------------------------------------------------------------------------

def test_budget() -> None:
    print("=" * 60)
    print("测试3：预算管理（budget）")
    print("=" * 60)

    errors = []

    bm = BudgetManager()

    # 初始化Hint预算=10
    bm.set_budget(BudgetType.HINT.value, 10)
    if bm.get_hint_remaining() != 10:
        errors.append(f"Hint余额应为10，实际{bm.get_hint_remaining()}")
    print(f"  [OK] Hint预算初始化: remaining={bm.get_hint_remaining()}")

    # 模拟253号10轮QA消耗Hint预算（每轮消耗1个Hint）
    for i in range(1, 11):
        ok = bm.consume_hint(1)
        if not ok:
            errors.append(f"第{i}轮消耗Hint应成功")
        remaining = bm.get_hint_remaining()
        print(f"  [OK] 第{i}轮消耗Hint: ok={ok}, remaining={remaining}")

    # 验证第10轮后Hint预算exhausted
    if not bm.is_hint_exhausted():
        errors.append(f"第10轮后Hint应exhausted，remaining={bm.get_hint_remaining()}")
    print(f"  [OK] 第10轮后Hint exhausted: remaining={bm.get_hint_remaining()}")

    # 验证超限触发硬性停止（第11轮消耗应返回False）
    ok11 = bm.consume_hint(1)
    if ok11:
        errors.append("第11轮消耗Hint应返回False（硬性停止）")
    print(f"  [OK] 第11轮消耗Hint被拒绝（硬性停止）: ok={ok11}")

    # 验证超限后余额仍为0（未被扣减）
    if bm.get_hint_remaining() != 0:
        errors.append(f"超限后余额应仍为0，实际{bm.get_hint_remaining()}")
    print(f"  [OK] 超限后余额未被扣减: remaining={bm.get_hint_remaining()}")

    # 验证其他预算类型也可用
    bm.set_budget(BudgetType.TOKEN.value, 1000)
    if not bm.consume(BudgetType.TOKEN.value, 300):
        errors.append("消耗token预算应成功")
    if bm.check_remaining(BudgetType.TOKEN.value) != 700:
        errors.append(f"token余额应为700，实际{bm.check_remaining(BudgetType.TOKEN.value)}")
    print(f"  [OK] token预算: consumed=300, remaining={bm.check_remaining(BudgetType.TOKEN.value)}")

    # 验证get_status返回所有预算状态
    status = bm.get_status()
    if "hint" not in status or "token" not in status:
        errors.append(f"get_status应包含hint和token，实际keys={list(status.keys())}")
    print(f"  [OK] get_status() keys: {list(status.keys())}")
    print(f"       hint={status['hint']}, token={status['token']}")

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
    print("# P1基础模块测试：hgraph + lifecycle + budget")
    print("#" * 60 + "\n")

    results = []
    results.append(("H图存储", test_hgraph_store()))
    results.append(("生命周期管理", test_lifecycle()))
    results.append(("预算管理", test_budget()))

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
