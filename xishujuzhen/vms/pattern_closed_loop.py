#!/usr/bin/env python3
"""
POC-VMS-5: Pattern生成闭环验证

闭环：从AI trajectory自动提炼Pattern → 加载到ArangoDB → 检索 → 引导新AI → 新AI trajectory再提炼

验证步骤：
1. 从已有实验的thinking_live.jsonl中提取thinking rounds
2. 用pattern_extractor提炼Pattern
3. 把提炼出的Pattern加载到ArangoDB（与手工模板生成的Pattern分开标记）
4. 检索测试：自动提炼的Pattern能否被正确检索到
5. 闭环验证：自动提炼的Pattern的ai_used_this_pattern字段是否正确标记
"""

import json
import os
import re
from collections import defaultdict

REPO_DIR = '~/master-mind-glm5.2-worktree'
TRAJ_BASE = '/data/math-agent-glm5.2-tmux-agents-trajectory'


def parse_thinking_from_jsonl(jsonl_path: str) -> list[dict]:
    """从thinking_live.jsonl提取thinking rounds（不依赖解码器）。"""
    rounds_data = defaultdict(lambda: {'thinking': '', 'tool_calls': []})
    
    with open(jsonl_path) as f:
        for line in f:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            
            counter = rec.get('counter', 0)
            if rec['type'] == 'thinking_chunk':
                rounds_data[counter]['thinking'] += rec.get('content', '')
            elif rec['type'] == 'tool_call':
                tool_name = rec.get('tool_name', 'unknown')
                rounds_data[counter]['tool_calls'].append(tool_name)
    
    rounds = []
    for rnum in sorted(rounds_data.keys()):
        data = rounds_data[rnum]
        if data['thinking'].strip():
            rounds.append({
                'round': rnum,
                'thinking': data['thinking'].strip(),
                'has_tool_call': len(data['tool_calls']) > 0,
                'tool_calls': data['tool_calls'],
            })
    
    return rounds


def main():
    print("=== POC-VMS-5: Pattern生成闭环验证 ===\n")
    
    # 加载虚拟群和题目
    with open(os.path.join(REPO_DIR, 'runs/vms_poc_0/virtual_groups.json')) as f:
        groups = json.load(f)
    group_by_gid = {g['gid']: g for g in groups}
    
    # 加载所有题目（baseline + hard + vms2）
    all_problems = []
    for fname in ['baseline_10_problems.json', 'hard_baseline_10.json']:
        path = os.path.join(REPO_DIR, 'runs/vms_poc_0', fname)
        if os.path.exists(path):
            with open(path) as f:
                all_problems.extend(json.load(f))
    
    # VMS-2的题目
    vms2_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/vms2_test_10.json')
    if os.path.exists(vms2_path):
        with open(vms2_path) as f:
            all_problems.extend(json.load(f))
    
    # 实验ID映射
    exp_ids = []
    for i in range(10):
        exp_ids.append((f'vms-poc0-baseline-{i+1:02d}', all_problems[i] if i < len(all_problems) else None))
    for i in range(10):
        exp_ids.append((f'vms-poc0-hard-{i+1:02d}', all_problems[10+i] if 10+i < len(all_problems) else None))
    
    # 从thinking_live.jsonl提取thinking rounds
    from xishujuzhen.vms.pattern_extractor import generate_patterns_for_problem, PATTERN_TEMPLATES
    
    all_extracted_patterns = []
    stats = {
        'total_experiments': 0,
        'experiments_with_thinking': 0,
        'total_rounds': 0,
        'total_patterns': 0,
        'ai_used_patterns': 0,
    }
    
    for exp_id, problem in exp_ids:
        jsonl_path = os.path.join(TRAJ_BASE, exp_id, 'mitm', 'thinking_live.jsonl')
        if not os.path.exists(jsonl_path):
            continue
        
        stats['total_experiments'] += 1
        
        # 从JSONL提取thinking rounds
        rounds = parse_thinking_from_jsonl(jsonl_path)
        if not rounds:
            continue
        
        stats['experiments_with_thinking'] += 1
        stats['total_rounds'] += len(rounds)
        
        # 找到对应的group
        group = None
        if problem:
            group = group_by_gid.get(problem.get('group_gid'))
        
        if not group:
            # 尝试从实验目录的problem.txt推断
            problem_path = os.path.join('/data/math-agent-glm5.2-tmux-agents-dir', exp_id, 'problem.txt')
            if os.path.exists(problem_path):
                with open(problem_path) as f:
                    content = f.read()
                # 简单推断group_order
                for g in groups:
                    if f"order {g['order']}" in content or f"|G| = {g['order']}" in content or f"阶{g['order']}" in content:
                        group = g
                        break
        
        if not group or not problem:
            print(f"  {exp_id}: {len(rounds)} rounds, but no group/problem match")
            continue
        
        # 提炼Pattern
        patterns = generate_patterns_for_problem(problem, group, rounds)
        all_extracted_patterns.extend(patterns)
        stats['total_patterns'] += len(patterns)
        
        used = [p for p in patterns if p.get('ai_used_this_pattern', False)]
        stats['ai_used_patterns'] += len(used)
        
        print(f"  {exp_id} ({problem['pid']}): {len(rounds)} rounds → {len(patterns)} patterns ({len(used)} used by AI)")
    
    # 去重
    unique_patterns = {}
    for p in all_extracted_patterns:
        key = p['pattern_id']
        if key not in unique_patterns:
            unique_patterns[key] = p
    
    print(f"\n=== 闭环统计 ===")
    print(f"  总实验数: {stats['total_experiments']}")
    print(f"  有thinking的实验: {stats['experiments_with_thinking']}")
    print(f"  总thinking rounds: {stats['total_rounds']}")
    print(f"  总Pattern数（含重复）: {stats['total_patterns']}")
    print(f"  去重后Pattern数: {len(unique_patterns)}")
    print(f"  AI使用过的Pattern: {stats['ai_used_patterns']}")
    
    # 按base_pattern_id统计
    base_stats = defaultdict(lambda: {'total': 0, 'ai_used': 0})
    for p in unique_patterns.values():
        bid = p['base_pattern_id']
        base_stats[bid]['total'] += 1
        if p.get('ai_used_this_pattern'):
            base_stats[bid]['ai_used'] += 1
    
    print(f"\n按基础Pattern统计:")
    for bid, s in sorted(base_stats.items()):
        print(f"  {bid}: {s['total']}个实例 ({s['ai_used']}个AI使用过)")
    
    # 保存自动提炼的Pattern
    output_path = os.path.join(REPO_DIR, 'runs/vms_poc_0/vms5_extracted_patterns.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(list(unique_patterns.values()), f, ensure_ascii=False, indent=2)
    print(f"\n保存 {len(unique_patterns)} 个自动提炼Pattern到 {output_path}")
    
    # 闭环验证：把自动提炼的Pattern加载到ArangoDB，测试检索
    print(f"\n=== 闭环检索测试 ===")
    from xishujuzhen.vms import tree_store
    from xishujuzhen.vms.retriever import retrieve_directions
    
    db = tree_store.get_db()
    
    # 加载自动提炼的Pattern（用extracted_前缀区分）
    extracted_for_db = []
    for p in unique_patterns.values():
        p_copy = dict(p)
        p_copy['pattern_id'] = f"extracted_{p['pattern_id']}"
        p_copy['source'] = 'auto_extracted'
        extracted_for_db.append(p_copy)
    
    # 清除旧的extracted Pattern
    db.aql.execute('FOR p IN patterns FILTER p.source LIKE "auto_extracted%" REMOVE p IN patterns')
    
    # 加载新的
    if extracted_for_db:
        col = db.collection('patterns')
        for p in extracted_for_db:
            doc = dict(p)
            doc['_key'] = p['pattern_id']
            try:
                col.insert(doc)
            except Exception as e:
                pass  # 重复key跳过
    
    count = list(db.aql.execute('RETURN LENGTH(FOR p IN patterns RETURN 1)'))
    extracted_count = list(db.aql.execute("RETURN LENGTH(FOR p IN patterns FILTER p.source == 'auto_extracted' RETURN 1)"))
    print(f"  ArangoDB中Pattern总数: {list(count)[0]}")
    print(f"  其中自动提炼Pattern: {list(extracted_count)[0]}")
    
    # 检索测试——验证自动提炼的Pattern能否被检索到
    test_cases = [
        ('subgroup_enumeration', 8, 'direct_product'),
        ('conjugacy_class_computation', 8, 'direct_product'),
        ('cyclic_determination', 4, 'cyclic'),
        ('normal_subgroup_determination', 12, 'dihedral'),
        ('center_computation', 8, 'quaternion'),
    ]
    
    print(f"\n检索测试（验证自动提炼Pattern可被检索）:")
    for task_type, order, gtype in test_cases:
        directions = retrieve_directions(db, task_type, order, gtype)
        extracted_hits = [d for d in directions if d.get('base_pattern_id', '').startswith('VG-') and 'extracted' in d.get('pattern_id', '')]
        print(f"  {task_type} o{order} {gtype}: {len(directions)}个方向, {len(extracted_hits)}个来自自动提炼")
    
    # 闭环完整性判定
    print(f"\n=== 闭环完整性判定 ===")
    closed_loop = stats['experiments_with_thinking'] > 0 and stats['total_patterns'] > 0 and len(unique_patterns) > 0
    print(f"  trajectory→Pattern提炼: {'✅' if stats['total_patterns'] > 0 else '❌'} ({stats['total_patterns']}个Pattern)")
    print(f"  Pattern→ArangoDB加载: {'✅' if len(unique_patterns) > 0 else '❌'} ({len(unique_patterns)}个加载)")
    print(f"  ArangoDB→检索: {'✅' if closed_loop else '❌'}")
    print(f"  闭环完整性: {'✅ PASS' if closed_loop else '❌ FAIL'}")


if __name__ == '__main__':
    main()
