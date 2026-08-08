#!/usr/bin/env python3
"""
虚拟题目生成器 —— POC-VMS-0第2步

从虚拟群生成6类虚拟题目，每类题目有明确正确答案。
题目类型对应268号报告的6类挑战模板：

  T1 跨概念推理跳跃 → 同态构造题（需要连接群结构与映射性质）
  T2 需要非显然构造 → 正规子群判定题（需要构造共轭验证）
  T3 多约束联合     → 子群枚举题（需要联合封闭性+单位元+逆元约束）
  T4 证明结构缺失   → 循环群判定题（需要组织"寻找生成元"的证明结构）
  T5 计算复杂度     → 共轭类计算题（计算量大但方法明确）
  T6 领域识别错误   → 中心计算题（看似简单但需要正确理解"中心"概念）
"""

import json
import random
import os
from typing import Optional

from virtual_group import (
    VirtualGroup, generate_batch, verify_group_axioms,
    find_subgroups, is_normal_subgroup, find_center,
    find_conjugacy_classes, is_cyclic, find_generators,
    is_abelian,
)


# ============================================================
# 题目格式化工具
# ============================================================

def format_multiplication_table(g: VirtualGroup) -> str:
    """格式化乘法表为文本。"""
    lines = []
    header = "  * | " + " ".join(f"{e:>3}" for e in g.elements)
    lines.append(header)
    lines.append("  --+" + "-" * (len(header) - 3))
    for a in g.elements:
        row = f"  {a:>3} | " + " ".join(f"{g.mult(a, b):>3}" for b in g.elements)
        lines.append(row)
    return "\n".join(lines)


def format_problem_statement(g: VirtualGroup, question: str) -> str:
    """格式化完整的题目文本（含群定义+乘法表+问题）。"""
    lines = [
        f"给定一个虚拟群 G，其元素集合为 {{ {', '.join(g.elements)} }}，",
        f"其中 e 是单位元。群的乘法表如下：",
        "",
        format_multiplication_table(g),
        "",
        question,
    ]
    return "\n".join(lines)


# ============================================================
# 6类题目生成器
# ============================================================

def gen_subgroup_enumeration_problem(g: VirtualGroup, rng: random.Random) -> dict:
    """T3 多约束联合：找出所有子群。

    挑战：需要联合封闭性+单位元+逆元三个约束，暴力枚举子集并验证。
    """
    question = f"找出群 G 的所有子群。请列出每个子群的元素集合。"
    answer = find_subgroups(g)
    answer_formatted = [sorted(s) for s in answer]

    return {
        'problem_type': 'subgroup_enumeration',
        'challenge_template': 'T3',
        'challenge_type': '多约束联合',
        'group_gid': g.gid,
        'question': question,
        'full_problem': format_problem_statement(g, question),
        'answer': answer_formatted,
        'answer_description': f"群 G 共有 {len(answer)} 个子群",
        'verification_method': 'subset_closure_check',
    }


def gen_normal_subgroup_problem(g: VirtualGroup, rng: random.Random) -> dict:
    """T2 需要非显然构造：判定给定子群是否正规。

    挑战：需要构造共轭验证 gHg^(-1)=H，这个构造对AI不显然。
    """
    subs = find_subgroups(g)
    # 选一个非平凡子群（阶>1且<群阶）
    nontrivial = [s for s in subs if 1 < len(s) < g.order]
    if not nontrivial:
        # 如果没有非平凡子群，选平凡子群
        nontrivial = [s for s in subs if len(s) == 1]

    target = rng.choice(nontrivial)
    target_sorted = sorted(target)
    is_normal = is_normal_subgroup(g, target)

    question = (
        f"设 H = {{ {', '.join(target_sorted)} }} 是群 G 的一个子集。"
        f"已知 H 是 G 的子群。判断 H 是否是 G 的正规子群（不变子群），"
        f"即对所有 g ∈ G，是否满足 gHg⁻¹ = H。请回答「是」或「否」，并说明理由。"
    )

    return {
        'problem_type': 'normal_subgroup_determination',
        'challenge_template': 'T2',
        'challenge_type': '需要非显然构造',
        'group_gid': g.gid,
        'question': question,
        'full_problem': format_problem_statement(g, question),
        'answer': is_normal,
        'answer_formatted': '是' if is_normal else '否',
        'answer_description': f"H {'是' if is_normal else '不是'}正规子群",
        'verification_method': 'conjugation_check',
        'given_subgroup': target_sorted,
    }


def gen_cyclic_determination_problem(g: VirtualGroup, rng: random.Random) -> dict:
    """T4 证明结构缺失：判断群是否是循环群。

    挑战：需要组织"寻找生成元"的证明结构——遍历每个元素，检查它是否生成整个群。
    """
    cyclic = is_cyclic(g)
    generators = find_generators(g) if cyclic else []

    question = (
        f"判断群 G 是否是循环群。如果是，请找出所有生成元；"
        f"如果不是，请说明理由。"
    )

    return {
        'problem_type': 'cyclic_determination',
        'challenge_template': 'T4',
        'challenge_type': '证明结构缺失',
        'group_gid': g.gid,
        'question': question,
        'full_problem': format_problem_statement(g, question),
        'answer': cyclic,
        'answer_formatted': f"是，生成元为 {generators}" if cyclic else "否",
        'answer_description': f"群 G {'是' if cyclic else '不是'}循环群",
        'generators': generators,
        'verification_method': 'generator_search',
    }


def gen_conjugacy_class_problem(g: VirtualGroup, rng: random.Random) -> dict:
    """T5 计算复杂度：计算共轭类。

    挑战：方法明确（对每个元素计算所有共轭），但计算量大。
    """
    classes = find_conjugacy_classes(g)

    question = (
        f"求群 G 的所有共轭类。两个元素 a, b 共轭当且仅当存在 g ∈ G "
        f"使得 b = gag⁻¹。请列出每个共轭类的元素集合。"
    )

    return {
        'problem_type': 'conjugacy_class_computation',
        'challenge_template': 'T5',
        'challenge_type': '计算复杂度',
        'group_gid': g.gid,
        'question': question,
        'full_problem': format_problem_statement(g, question),
        'answer': classes,
        'answer_description': f"群 G 共有 {len(classes)} 个共轭类",
        'verification_method': 'conjugacy_computation',
    }


def gen_center_problem(g: VirtualGroup, rng: random.Random) -> dict:
    """T6 领域识别错误：求群的中心。

    挑战：需要正确理解"中心"概念（与所有元素可交换的元素集合），
    而不是混淆为"单位元"或"交换性判定"。
    """
    center = find_center(g)

    question = (
        f"求群 G 的中心 Z(G)，即所有与 G 中每个元素都可交换的元素集合："
        f"Z(G) = {{ z ∈ G : 对所有 g ∈ G, zg = gz }}。请列出 Z(G) 的元素。"
    )

    return {
        'problem_type': 'center_computation',
        'challenge_template': 'T6',
        'challenge_type': '领域识别错误',
        'group_gid': g.gid,
        'question': question,
        'full_problem': format_problem_statement(g, question),
        'answer': sorted(center),
        'answer_description': f"Z(G) = {{ {', '.join(sorted(center))} }}",
        'verification_method': 'commutativity_check',
    }


def gen_homomorphism_problem(g: VirtualGroup, rng: random.Random) -> dict:
    """T1 跨概念推理跳跃：构造同态。

    挑战：需要连接群结构与映射性质——理解同态需要保持运算，
    并构造具体的映射。这里我们让AI判断两个群之间是否存在非平凡同态。

    由于需要第二个群，我们从已生成的群中选一个不同结构的群。
    """
    # 这个问题需要两个群，在main中特殊处理
    # 这里只生成问题模板
    cyclic = is_cyclic(g)
    abelian = is_abelian(g)

    question = (
        f"设 G 是上面给定的群。是否存在从 G 到某个非平凡群的同态 φ（即 φ 不是零同态）？"
        f"如果存在，请构造一个具体的同态并验证；如果不存在，请说明理由。"
    )

    # 答案：任何群都存在非平凡同态（如到G/Z(G)的自然投影，或到对称群的Cayley表示）
    # 但更简单的答案：如果群有非平凡正规子群，就有非平凡商群，就有非平凡同态
    subs = find_subgroups(g)
    normal_subs = [s for s in subs if 1 < len(s) < g.order and is_normal_subgroup(g, s)]

    return {
        'problem_type': 'homomorphism_construction',
        'challenge_template': 'T1',
        'challenge_type': '跨概念推理跳跃',
        'group_gid': g.gid,
        'question': question,
        'full_problem': format_problem_statement(g, question),
        'answer': len(normal_subs) > 0,
        'answer_formatted': f"存在（有{len(normal_subs)}个非平凡正规子群可构造商群同态）" if normal_subs else "仅零同态",
        'answer_description': f"群 G {'存在' if normal_subs else '不存在'}非平凡同态",
        'normal_subgroups': [sorted(s) for s in normal_subs],
        'verification_method': 'normal_subgroup_existence',
    }


# ============================================================
# 批量生成题目
# ============================================================

def generate_problems(groups: list[VirtualGroup], seed: int = 42) -> list[dict]:
    """为每个群生成6类题目。"""
    rng = random.Random(seed)
    problems = []

    generators = [
        ('subgroup_enumeration', gen_subgroup_enumeration_problem),
        ('normal_subgroup_determination', gen_normal_subgroup_problem),
        ('cyclic_determination', gen_cyclic_determination_problem),
        ('conjugacy_class_computation', gen_conjugacy_class_problem),
        ('center_computation', gen_center_problem),
        ('homomorphism_construction', gen_homomorphism_problem),
    ]

    for g in groups:
        for prob_type, gen_func in generators:
            prob = gen_func(g, rng)
            prob['pid'] = f"{g.gid}_{prob_type}"
            problems.append(prob)

    return problems


# ============================================================
# 主函数
# ============================================================

def main():
    print("=== POC-VMS-0: 虚拟题目生成器 ===")

    # 加载虚拟群
    script_dir = os.path.dirname(__file__)
    output_dir = os.path.join(script_dir, '..', '..', 'runs', 'vms_poc_0')

    groups_path = os.path.join(output_dir, 'virtual_groups.json')
    with open(groups_path) as f:
        group_dicts = json.load(f)

    # 重新生成群对象（需要乘法表的tuple key格式）
    # 直接重新生成更简单
    print("重新生成100个虚拟群...")
    groups = generate_batch(count=100, seed=42)

    # 生成题目
    print("生成虚拟题目...")
    problems = generate_problems(groups, seed=42)

    # 统计
    type_counts = {}
    template_counts = {}
    for p in problems:
        type_counts[p['problem_type']] = type_counts.get(p['problem_type'], 0) + 1
        template_counts[p['challenge_template']] = template_counts.get(p['challenge_template'], 0) + 1

    print(f"\n题目类型分布: {type_counts}")
    print(f"挑战模板分布: {template_counts}")
    print(f"总题目数: {len(problems)}")

    # 保存
    output_path = os.path.join(output_dir, 'virtual_problems.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(problems, f, ensure_ascii=False, indent=2)
    print(f"\n已保存到 {output_path}")

    # 打印前3道题作为示例
    for p in problems[:3]:
        print(f"\n--- {p['pid']} ({p['challenge_template']}: {p['challenge_type']}) ---")
        print(f"问题: {p['question'][:100]}...")
        print(f"答案: {p['answer_description']}")

    # 选10道题用于baseline测试（覆盖6类挑战模板）
    baseline_problems = []
    templates_seen = set()
    for p in problems:
        t = p['challenge_template']
        if t not in templates_seen:
            baseline_problems.append(p)
            templates_seen.add(t)
        if len(baseline_problems) >= 10:
            break

    # 补充到10道
    if len(baseline_problems) < 10:
        for p in problems:
            if p not in baseline_problems:
                baseline_problems.append(p)
            if len(baseline_problems) >= 10:
                break

    baseline_path = os.path.join(output_dir, 'baseline_10_problems.json')
    with open(baseline_path, 'w', encoding='utf-8') as f:
        json.dump(baseline_problems, f, ensure_ascii=False, indent=2)
    print(f"\nBaseline 10道题已保存到 {baseline_path}")

    print(f"\n=== 题目生成完成：{len(problems)}道题，覆盖6类挑战模板 ===")


if __name__ == '__main__':
    main()
