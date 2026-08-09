#!/usr/bin/env python3
"""
修正5个新v3 profile的qa_sequence.rounds中的situation_type和level。
之前的fix_v3_profiles.py只修了tell_hint_pairs，遗漏了qa_sequence.rounds。
"""
from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
profiles = db.collection('problem_profiles')

SIT_MAP = {
    '纯元认知观察': '纯元认知观察', '自由列举': '自由列举', '小尝试': '小尝试',
    '思维操作引导': '思维操作引导', '推进': '推进', '能量传递引导': '能量传递引导',
    'metacognitive': '纯元认知观察', 'problem_understanding': '纯元认知观察',
    'understanding_constraint': '纯元认知观察', 'reflection': '纯元认知观察',
    'global_reflection': '纯元认知观察', 'thinking': '纯元认知观察',
    'strategic': '自由列举', 'method_selection': '自由列举', '方法选择': '自由列举',
    'direct_attempt': '小尝试', 'direct_calculation': '小尝试', '直接计算': '小尝试',
    'case_analysis': '小尝试', 'constraint_extraction': '小尝试',
    'edge_case_resolution': '小尝试',
    'key_insight': '思维操作引导', '关键洞察': '思维操作引导', 'knowledge': '思维操作引导',
    'knowledge_application': '思维操作引导', '知识瓶颈': '思维操作引导',
    'structural_transformation': '思维操作引导',
    'calculation': '推进', 'execution': '推进', '验证': '推进',
    'refinement': '能量传递引导',
}

def normalize_level(val):
    if isinstance(val, float) and 0 <= val <= 1:
        return val
    if isinstance(val, int):
        if val <= 1:
            return float(val)
        return min(1.0, (val - 1) / 3.0)
    return 0.5

new_keys = ['compfiles_imo1970p6', 'compfiles_imo1971p5', 'compfiles_imo1971p6',
            'compfiles_imo1972p5', 'compfiles_imo1973p5']

for key in new_keys:
    p = profiles.get(key)
    if not p:
        print(f'  {key}: NOT FOUND')
        continue
    
    fixed_sits = 0
    fixed_levels = 0
    unknown_sits = []
    
    for r in p.get('qa_sequence', {}).get('rounds', []):
        old_sit = r.get('situation_type', '')
        if old_sit in SIT_MAP:
            new_sit = SIT_MAP[old_sit]
            if new_sit != old_sit:
                r['situation_type'] = new_sit
                fixed_sits += 1
        else:
            unknown_sits.append(old_sit)
        
        old_level = r.get('level', 0.5)
        new_level = normalize_level(old_level)
        if new_level != old_level:
            r['level'] = new_level
            fixed_levels += 1
    
    # Also fix qa_sequence.stats if needed
    stats = p.get('qa_sequence', {}).get('stats', {})
    if 'level_sum' in stats:
        # Recalculate level_sum from fixed levels
        levels = [r.get('level', 0.5) for r in p.get('qa_sequence', {}).get('rounds', [])]
        stats['level_sum'] = sum(levels)
    
    profiles.update(p)
    unknown_str = f', unknown: {unknown_sits}' if unknown_sits else ''
    print(f'  {key}: 修正{fixed_sits}个sit, {fixed_levels}个level{unknown_str}')

print('\n完成')
