"""
Phase 24b: 郑氏星案命格判断验证
用格局引擎对40例排盘结果自动判断，与郑希诚原判对比。

验证维度：
1. 格局引擎匹配数 vs 郑氏所喜星格数（覆盖度）
2. 郑氏所喜星格在规则库中的命中率
3. 郑氏所忌星格在规则库中的命中率
4. 命格等级与格局匹配数的相关性
"""

import sys
sys.path.insert(0, ".")
from qizheng import core, chart
from qizheng.zheng_cases import ZHENG_40_CASES
from qizheng.test_phase24 import case_to_chart
import re

def extract_star_patterns(case_id):
    """从星案原文提取所喜星格和所忌星格"""
    path = f"dev-docs/原典/郑氏星案/星案{case_id}.txt"
    with open(path, encoding='utf-8') as f:
        text = f.read()

    good = []
    bad = []

    m_good = re.search(r'所喜星格︰(.+?)(?:\n|所忌)', text)
    m_bad = re.search(r'所忌星格︰(.+?)(?:\n|命|诸|七|太|于|亲)', text)

    if m_good:
        raw = m_good.group(1).strip()
        good = [x.strip() for x in raw.replace('、', ',').split(',') if x.strip()]
    if m_bad:
        raw = m_bad.group(1).strip()
        bad = [x.strip() for x in raw.replace('、', ',').split(',') if x.strip()]

    return good, bad

def run_phase24b():
    """Phase 24b: 命格判断验证"""
    EPHE = "ephe"
    core.init_ephe(EPHE)

    print("=" * 70)
    print("Phase 24b: 郑氏星案命格判断验证")
    print("=" * 70)

    # 收集所有郑氏星格
    all_zheng_good = set()
    all_zheng_bad = set()
    for case in ZHENG_40_CASES:
        good, bad = extract_star_patterns(case["id"])
        all_zheng_good.update(good)
        all_zheng_bad.update(bad)

    # 规则库中的格局名
    rules = core.load_rules_library()
    rule_names = [r["name"] for r in rules]

    # 统计规则库覆盖度
    good_in_rules = 0
    good_not_in_rules = 0
    good_matched_examples = []
    good_unmatched_examples = []

    for g in sorted(all_zheng_good):
        found = any(g in r or r in g for r in rule_names)
        if found:
            good_in_rules += 1
            good_matched_examples.append(g)
        else:
            good_not_in_rules += 1
            good_unmatched_examples.append(g)

    bad_in_rules = 0
    bad_not_in_rules = 0
    bad_matched_examples = []
    bad_unmatched_examples = []

    for b in sorted(all_zheng_bad):
        found = any(b in r or r in b for r in rule_names)
        if found:
            bad_in_rules += 1
            bad_matched_examples.append(b)
        else:
            bad_not_in_rules += 1
            bad_unmatched_examples.append(b)

    print(f"\n=== 规则库覆盖度 ===")
    print(f"郑氏所喜星格: {len(all_zheng_good)}种, 规则库命中: {good_in_rules}, 未命中: {good_not_in_rules}")
    print(f"郑氏所忌星格: {len(all_zheng_bad)}种, 规则库命中: {bad_in_rules}, 未命中: {bad_not_in_rules}")
    print(f"覆盖率: 喜格{good_in_rules}/{len(all_zheng_good)}={good_in_rules/len(all_zheng_good)*100:.1f}%, "
          f"忌格{bad_in_rules}/{len(all_zheng_bad)}={bad_in_rules/len(all_zheng_bad)*100:.1f}%")

    print(f"\n=== 规则库命中的喜格 ===")
    for g in good_matched_examples:
        print(f"  ✓ {g}")
    print(f"\n=== 规则库未命中的喜格（前20） ===")
    for g in good_unmatched_examples[:20]:
        print(f"  ✗ {g}")

    print(f"\n=== 规则库命中的忌格 ===")
    for b in bad_matched_examples:
        print(f"  ✓ {b}")
    print(f"\n=== 规则库未命中的忌格（前20） ===")
    for b in bad_unmatched_examples[:20]:
        print(f"  ✗ {b}")

    # 逐例验证
    print(f"\n=== 逐例格局匹配 ===")
    results = []
    for case in ZHENG_40_CASES:
        c, msg = case_to_chart(case)
        if not c:
            results.append({"id": case["id"], "grade": case["grade"], "matched": 0, "good": [], "bad": []})
            continue

        rule_result = core.eval_rules(c)
        matched_count = rule_result["matched_count"]
        matched_names = [m["name"] for m in rule_result["matched"]]

        good, bad = extract_star_patterns(case["id"])
        results.append({
            "id": case["id"],
            "grade": case["grade"],
            "gender": case["gender"],
            "matched": matched_count,
            "total": rule_result["total"],
            "good": good,
            "bad": bad,
            "matched_names": matched_names,
        })

    # 命格等级 vs 格局匹配数
    print(f"\n=== 命格等级 vs 格局匹配数 ===")
    grade_stats = {}
    for r in results:
        g = r["grade"]
        if g not in grade_stats:
            grade_stats[g] = []
        grade_stats[g].append(r["matched"])

    print(f"{'命格':<12} {'例数':>4} {'平均匹配':>8} {'最小':>6} {'最大':>6}")
    for g, counts in sorted(grade_stats.items(), key=lambda x: -sum(x[1])/len(x[1])):
        avg = sum(counts) / len(counts)
        print(f"{g:<12} {len(counts):>4} {avg:>8.1f} {min(counts):>6} {max(counts):>6}")

    # 高命格 vs 低命格
    high_grades = ["三品命", "四品命", "黄堂命", "科第命", "监司命", "府官命", "州邑命", "邑长命"]
    low_grades = ["寻常命", "中平命", "安常命", "起倒命", "常人带疾命", "带疾延寿命"]

    high_counts = [r["matched"] for r in results if r["grade"] in high_grades]
    low_counts = [r["matched"] for r in results if r["grade"] in low_grades]

    if high_counts and low_counts:
        print(f"\n高命格({len(high_counts)}例): 平均{sum(high_counts)/len(high_counts):.1f}个格局")
        print(f"低命格({len(low_counts)}例): 平均{sum(low_counts)/len(low_counts):.1f}个格局")
        if sum(high_counts)/len(high_counts) > sum(low_counts)/len(low_counts):
            print("✓ 高命格的平均格局匹配数 > 低命格（符合预期）")
        else:
            print("✗ 高命格的平均格局匹配数 <= 低命格（不符合预期）")

    # 输出每例详情
    print(f"\n=== 40例详情 ===")
    print(f"{'ID':>3} {'命格':<12} {'匹配':>4} {'喜格数':>6} {'忌格数':>6}")
    for r in results:
        print(f"{r['id']:>3} {r['grade']:<12} {r['matched']:>4} {len(r['good']):>6} {len(r['bad']):>6}")

    # 总结
    print(f"\n{'='*70}")
    print(f"Phase 24b 总结:")
    print(f"  规则库覆盖率: 喜格{good_in_rules/len(all_zheng_good)*100:.1f}%, 忌格{bad_in_rules/len(all_zheng_bad)*100:.1f}%")
    print(f"  高命格平均格局数: {sum(high_counts)/len(high_counts):.1f}" if high_counts else "  高命格: 无数据")
    print(f"  低命格平均格局数: {sum(low_counts)/len(low_counts):.1f}" if low_counts else "  低命格: 无数据")
    print(f"  主要缺口: 郑氏星格中{good_not_in_rules}种喜格和{bad_not_in_rules}种忌格未在规则库中")
    print(f"{'='*70}")

if __name__ == "__main__":
    run_phase24b()
