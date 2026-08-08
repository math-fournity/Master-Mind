#!/usr/bin/env python3
"""
Pattern提炼器 —— POC-VMS-1

从虚拟群论题的trajectory中提炼Pattern。
Pattern = "在什么数学处境下，应该往什么方向探索"

Pattern结构（对应267号树生长引擎中的"方向Q"）：
{
  "pattern_id": "VG-001-...",
  "domain": "virtual_group_theory",
  "trigger_conditions": {
    "deterministic": {        # 可被形式化方法查询的字段
      "task_type": "find_subgroups",
      "group_order": {"op": ">", "value": 4},
      "has_multiplication_table": true
    },
    "non_deterministic": {    # 需要AI判断的字段
      "reasoning_state": "AI is enumerating subsets without checking closure"
    }
  },
  "Q": "子群的阶必须整除群的阶。先列出群阶的所有因子，再逐一检查各阶子群。",
  "Level": 0.4,               # 0=纯知识，1=纯思维模式
  "non_specificity": 0.8,     # 0=具体指令，1=最非特定
  "situation_type": "思维操作引导",
  "source": "virtual_group_VG_001, thinking_round_2"
}

提炼方法：
1. 从thinking_readable.txt中提取AI的推理步骤
2. 识别每个推理步骤对应的"思维操作"（元素阶计算/Lagrange定理/群结构识别等）
3. 把思维操作抽象为Pattern
4. 从题目元数据提取deterministic字段
5. 从thinking内容提取non_deterministic字段
"""

import json
import os
import re
from typing import Optional


# ============================================================
# Pattern模板库
# ============================================================

# 从AI推理过程中识别的8种思维操作Pattern
# 每种Pattern对应一个"在什么处境下应该往什么方向探索"的指导

PATTERN_TEMPLATES = [
    {
        'pattern_id': 'VG-element-order-computation',
        'name': '元素阶计算',
        'description': '面对群论问题时，首先计算每个元素的阶',
        'trigger_deterministic': {
            'task_type': 'any',
            'has_multiplication_table': True,
        },
        'trigger_nondeterministic': {
            'reasoning_state': 'AI is looking at the multiplication table but has not yet computed element orders',
        },
        'Q': '计算每个元素的阶——对每个元素a，计算a, a², a³, ...直到回到e。元素的阶是群论分析的基础。',
        'Level': 0.3,
        'non_specificity': 0.9,
        'situation_type': '基础操作引导',
        'thinking_keywords': ['order', '阶', 'power', '幂', 'a²', 'a^2', 'generate'],
    },
    {
        'pattern_id': 'VG-lagrange-theorem-application',
        'name': 'Lagrange定理应用',
        'description': '当需要找子群时，用Lagrange定理确定子群的可能阶',
        'trigger_deterministic': {
            'task_type': 'subgroup_enumeration',
            'has_multiplication_table': True,
        },
        'trigger_nondeterministic': {
            'reasoning_state': 'AI is trying to enumerate subsets without using Lagrange theorem to constrain possible subgroup orders',
        },
        'Q': '子群的阶必须整除群的阶（Lagrange定理）。先列出群阶的所有因子，再逐一检查各阶子群——这比暴力枚举所有子集高效得多。',
        'Level': 0.4,
        'non_specificity': 0.8,
        'situation_type': '定理应用引导',
        'thinking_keywords': ['Lagrange', 'divide', '整除', 'factor', '因子', 'subgroup order'],
    },
    {
        'pattern_id': 'VG-cyclic-group-identification',
        'name': '循环群识别',
        'description': '通过寻找生成元判断群是否是循环群',
        'trigger_deterministic': {
            'task_type': 'cyclic_determination',
            'has_multiplication_table': True,
        },
        'trigger_nondeterministic': {
            'reasoning_state': 'AI is checking if the group is cyclic but has not yet searched for a generator',
        },
        'Q': '群是循环群当且仅当存在一个阶等于群阶的元素（生成元）。检查是否有元素的阶等于|G|。',
        'Level': 0.5,
        'non_specificity': 0.8,
        'situation_type': '概念判定引导',
        'thinking_keywords': ['cyclic', '循环', 'generator', '生成元', 'Z_n', 'Z₄', 'isomorphic'],
    },
    {
        'pattern_id': 'VG-conjugacy-class-computation',
        'name': '共轭类计算',
        'description': '对每个元素计算所有共轭，归类共轭类',
        'trigger_deterministic': {
            'task_type': 'conjugacy_class_computation',
            'has_multiplication_table': True,
        },
        'trigger_nondeterministic': {
            'reasoning_state': 'AI needs to compute conjugacy classes but has not started conjugation calculation',
        },
        'Q': '对每个元素a，计算所有gag⁻¹（g遍历整个群）。相同共轭的元素归为一类。共轭类构成群的划分。',
        'Level': 0.6,
        'non_specificity': 0.7,
        'situation_type': '计算方法引导',
        'thinking_keywords': ['conjugacy', '共轭', 'conjugate', 'gag', 'class', '类'],
    },
    {
        'pattern_id': 'VG-center-computation',
        'name': '中心计算',
        'description': '检查每个元素是否与所有元素可交换',
        'trigger_deterministic': {
            'task_type': 'center_computation',
            'has_multiplication_table': True,
        },
        'trigger_nondeterministic': {
            'reasoning_state': 'AI needs to find the center but has not checked commutativity',
        },
        'Q': '群的中心Z(G)是所有与每个元素都可交换的元素集合。对每个元素z，检查是否对所有g满足zg=gz。如果群是交换群，中心=整个群。',
        'Level': 0.3,
        'non_specificity': 0.9,
        'situation_type': '概念应用引导',
        'thinking_keywords': ['center', '中心', 'commute', '可交换', 'abelian', '交换', 'Z(G)'],
    },
    {
        'pattern_id': 'VG-normal-subgroup-determination',
        'name': '正规子群判定',
        'description': '验证gHg⁻¹=H判断正规子群',
        'trigger_deterministic': {
            'task_type': 'normal_subgroup_determination',
            'has_multiplication_table': True,
        },
        'trigger_nondeterministic': {
            'reasoning_state': 'AI needs to determine if a subgroup is normal but has not checked conjugation invariance',
        },
        'Q': 'H是正规子群当且仅当对所有g∈G，gHg⁻¹=H。对每个g，计算gHg⁻¹并检查是否等于H。如果群是交换群，所有子群都是正规子群。',
        'Level': 0.5,
        'non_specificity': 0.7,
        'situation_type': '概念判定引导',
        'thinking_keywords': ['normal', '正规', 'invariant', '不变', 'gHg', 'conjugation', '共轭'],
    },
    {
        'pattern_id': 'VG-python-verification',
        'name': 'Python验证',
        'description': '当计算量大时，用Python暴力枚举验证',
        'trigger_deterministic': {
            'task_type': 'any',
            'group_order': {'op': '>', 'value': 8},
            'has_multiplication_table': True,
        },
        'trigger_nondeterministic': {
            'reasoning_state': 'AI is doing manual computation that could be error-prone for large groups',
        },
        'Q': '用Python解析乘法表，暴力枚举验证。对于大群（阶>8），手动计算容易出错，Python可以自动检查封闭性/共轭/交换性。',
        'Level': 0.1,
        'non_specificity': 0.5,
        'situation_type': '工具使用引导',
        'thinking_keywords': ['python', 'verify', '验证', 'compute', '计算', 'enumerate', '枚举', 'brute'],
    },
    {
        'pattern_id': 'VG-group-structure-identification',
        'name': '群结构识别',
        'description': '通过元素阶分布识别群的同构类型',
        'trigger_deterministic': {
            'task_type': 'any',
            'group_order': {'op': 'in', 'value': [4, 6, 8, 12, 24]},
            'has_multiplication_table': True,
        },
        'trigger_nondeterministic': {
            'reasoning_state': 'AI has computed element orders but has not yet identified the group isomorphism type',
        },
        'Q': '通过元素阶分布识别群的同构类型。例如：4阶群中若有阶4元素则是Z₄，否则是V₄；24阶群中若有1个阶1+9个阶2+8个阶3+6个阶4则是S₄。',
        'Level': 0.7,
        'non_specificity': 0.6,
        'situation_type': '模式识别引导',
        'thinking_keywords': ['isomorphic', '同构', 'S_4', 'S₄', 'D_n', 'D₆', 'Z_n', 'Z₄', 'V_4', 'V₄', 'Klein', 'quaternion', 'Q_8', 'Q₈', 'structure'],
    },
]


# ============================================================
# Trajectory分析
# ============================================================

def parse_thinking(thinking_path: str) -> list[dict]:
    """解析thinking_readable.txt，提取每个thinking round的内容。"""
    with open(thinking_path, 'r', encoding='utf-8') as f:
        content = f.read()

    rounds = []
    # 按Thinking Round分割
    pattern = r'=== Thinking Round (\d+) START ===\n(.*?)\n--- \[Tool Call:'
    matches = re.findall(pattern, content, re.DOTALL)

    for round_num, thinking_text in matches:
        rounds.append({
            'round': int(round_num),
            'thinking': thinking_text.strip(),
            'has_tool_call': True,
        })

    # 也处理没有tool call的round
    pattern2 = r'=== Thinking Round (\d+) START ===\n(.*?)\n={50}'
    matches2 = re.findall(pattern2, content, re.DOTALL)
    for round_num, thinking_text in matches2:
        if not any(r['round'] == int(round_num) for r in rounds):
            rounds.append({
                'round': int(round_num),
                'thinking': thinking_text.strip(),
                'has_tool_call': False,
            })

    return rounds


def identify_thinking_operations(thinking: str) -> list[str]:
    """从thinking内容识别AI使用了哪些思维操作。"""
    thinking_lower = thinking.lower()
    matched_patterns = []

    for template in PATTERN_TEMPLATES:
        keywords = template['thinking_keywords']
        for kw in keywords:
            if kw.lower() in thinking_lower:
                matched_patterns.append(template['pattern_id'])
                break

    return matched_patterns


# ============================================================
# Pattern生成
# ============================================================

def generate_patterns_for_problem(
    problem: dict,
    group: dict,
    thinking_rounds: list[dict],
) -> list[dict]:
    """为一道题的trajectory生成Pattern。"""
    patterns = []
    seen_pattern_ids = set()

    task_type = problem['problem_type']
    group_order = group['order']

    # 从thinking中识别AI使用的思维操作
    all_operations = []
    for r in thinking_rounds:
        ops = identify_thinking_operations(r['thinking'])
        all_operations.extend(ops)

    # 对每个识别到的思维操作，生成一个Pattern
    for template in PATTERN_TEMPLATES:
        pid = template['pattern_id']

        # 检查这个Pattern是否适用于本题
        # 1. task_type匹配（any匹配所有）
        tt = template['trigger_deterministic'].get('task_type', 'any')
        if tt != 'any' and tt != task_type:
            continue

        # 2. group_order条件检查
        go_cond = template['trigger_deterministic'].get('group_order')
        if go_cond:
            op = go_cond.get('op')
            val = go_cond.get('value')
            if op == '>' and not (group_order > val):
                continue
            if op == 'in' and group_order not in val:
                continue

        # 3. 检查AI是否真的使用了这个思维操作
        if pid not in all_operations:
            # 即使AI没有使用，如果task_type匹配也生成（作为"应该使用"的Pattern）
            pass

        # 生成Pattern
        pattern = {
            'pattern_id': f"{pid}-{problem['pid']}",
            'base_pattern_id': pid,
            'name': template['name'],
            'description': template['description'],
            'domain': 'virtual_group_theory',
            'trigger_conditions': {
                'deterministic': {
                    **template['trigger_deterministic'],
                    'group_order': group_order,
                    'group_type': group['group_type'],
                },
                'non_deterministic': template['trigger_nondeterministic'],
            },
            'Q': template['Q'],
            'Level': template['Level'],
            'non_specificity': template['non_specificity'],
            'situation_type': template['situation_type'],
            'source': f"{problem['pid']}, thinking_rounds_{len(thinking_rounds)}",
            'ai_used_this_pattern': pid in all_operations,
            'challenge_template': problem.get('challenge_template', ''),
            'challenge_type': problem.get('challenge_type', ''),
        }
        patterns.append(pattern)

    return patterns


# ============================================================
# 主函数
# ============================================================

def main():
    print("=== POC-VMS-1: Pattern提炼器 ===\n")

    REPO_DIR = '~/master-mind-glm5.2-worktree'
    TRAJ_BASE = '/data/math-agent-glm5.2-tmux-agents-trajectory'

    # 加载虚拟群和题目
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/virtual_groups.json')) as f:
        groups = json.load(f)
    group_by_gid = {g['gid']: g for g in groups}

    # 加载baseline题目（4阶+24阶）
    all_problems = []
    for fname in ['baseline_10_problems.json', 'hard_baseline_10.json']:
        path = os.path.join(REPO_DIR, 'runs/vms_poc_0', fname)
        with open(path) as f:
            all_problems.extend(json.load(f))

    # 为每道题提炼Pattern
    all_patterns = []
    stats = {'total_problems': 0, 'problems_with_thinking': 0, 'total_patterns': 0}

    for i, problem in enumerate(all_problems):
        # 确定实验ID
        if i < 10:
            exp_id = f'vms-poc0-baseline-{i+1:02d}'
        else:
            exp_id = f'vms-poc0-hard-{i-9:02d}'

        group = group_by_gid.get(problem['group_gid'])
        if not group:
            continue

        # 读取thinking
        thinking_path = os.path.join(TRAJ_BASE, exp_id, 'mitm', 'thinking_readable.txt')
        if not os.path.exists(thinking_path):
            print(f"  {exp_id}: no thinking data")
            continue

        thinking_rounds = parse_thinking(thinking_path)
        if not thinking_rounds:
            print(f"  {exp_id}: no thinking rounds parsed")
            continue

        stats['total_problems'] += 1
        stats['problems_with_thinking'] += 1

        # 生成Pattern
        patterns = generate_patterns_for_problem(problem, group, thinking_rounds)
        all_patterns.extend(patterns)
        stats['total_patterns'] += len(patterns)

        # 统计AI使用的Pattern
        used = [p for p in patterns if p['ai_used_this_pattern']]
        print(f"  {exp_id} ({problem['pid']}): {len(thinking_rounds)} rounds, {len(patterns)} patterns ({len(used)} used by AI)")

    # 去重（按base_pattern_id + task_type + group_order）
    unique_patterns = {}
    for p in all_patterns:
        key = f"{p['base_pattern_id']}_{p['trigger_conditions']['deterministic'].get('task_type', 'any')}_{p['trigger_conditions']['deterministic'].get('group_order', 0)}"
        if key not in unique_patterns:
            unique_patterns[key] = p

    print(f"\n=== 统计 ===")
    print(f"  总题数: {stats['total_problems']}")
    print(f"  有thinking的题数: {stats['problems_with_thinking']}")
    print(f"  总Pattern数（含重复）: {stats['total_patterns']}")
    print(f"  去重后Pattern数: {len(unique_patterns)}")

    # 按base_pattern_id统计
    base_stats = {}
    for p in unique_patterns.values():
        bid = p['base_pattern_id']
        if bid not in base_stats:
            base_stats[bid] = {'total': 0, 'ai_used': 0}
        base_stats[bid]['total'] += 1
        if p['ai_used_this_pattern']:
            base_stats[bid]['ai_used'] += 1

    print(f"\n按基础Pattern统计:")
    for bid, s in sorted(base_stats.items()):
        print(f"  {bid}: {s['total']}个实例 ({s['ai_used']}个AI使用过)")

    # 验证Pattern结构完整性
    print(f"\n=== Pattern结构验证 ===")
    required_fields = ['pattern_id', 'domain', 'trigger_conditions', 'Q', 'Level', 'non_specificity', 'situation_type', 'source']
    struct_ok = True
    for p in unique_patterns.values():
        for f in required_fields:
            if f not in p:
                print(f"  ❌ {p['pattern_id']}: missing field {f}")
                struct_ok = False
        tc = p.get('trigger_conditions', {})
        if 'deterministic' not in tc or 'non_deterministic' not in tc:
            print(f"  ❌ {p['pattern_id']}: trigger_conditions missing deterministic/non_deterministic")
            struct_ok = False

    if struct_ok:
        print(f"  ✅ 所有{len(unique_patterns)}个Pattern结构完整")

    # 保存
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/patterns.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(list(unique_patterns.values()), f, ensure_ascii=False, indent=2)
    print(f"\n已保存 {len(unique_patterns)} 个Pattern到 {output_path}")

    # 保存基础Pattern模板（去重到base_pattern_id级别）
    base_patterns = {}
    for p in unique_patterns.values():
        bid = p['base_pattern_id']
        if bid not in base_patterns:
            base_patterns[bid] = {
                'pattern_id': bid,
                'name': p['name'],
                'description': p['description'],
                'domain': p['domain'],
                'trigger_conditions': {
                    'deterministic': p['trigger_conditions']['deterministic'],
                    'non_deterministic': p['trigger_conditions']['non_deterministic'],
                },
                'Q': p['Q'],
                'Level': p['Level'],
                'non_specificity': p['non_specificity'],
                'situation_type': p['situation_type'],
                'instance_count': 0,
                'ai_used_count': 0,
            }
        base_patterns[bid]['instance_count'] += 1
        if p['ai_used_this_pattern']:
            base_patterns[bid]['ai_used_count'] += 1

    base_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/base_patterns.json')
    with open(base_path, 'w', encoding='utf-8') as f:
        json.dump(list(base_patterns.values()), f, ensure_ascii=False, indent=2)
    print(f"已保存 {len(base_patterns)} 个基础Pattern到 {base_path}")


if __name__ == '__main__':
    main()
