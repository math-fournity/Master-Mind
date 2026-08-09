#!/usr/bin/env python3
"""
修正5个新v3 profile的situation_type和hint_level。
- situation_type: 从subagent自创的值映射到6个规范值
- hint_level: 从1-4整数归一化到0-1浮点数
"""
from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
profiles = db.collection('problem_profiles')

# situation_type映射表
SIT_MAP = {
    # 规范值（保留）
    '纯元认知观察': '纯元认知观察',
    '自由列举': '自由列举',
    '小尝试': '小尝试',
    '思维操作引导': '思维操作引导',
    '推进': '推进',
    '能量传递引导': '能量传递引导',
    # 英文自创→规范
    'metacognitive': '纯元认知观察',
    'problem_understanding': '纯元认知观察',
    'understanding_constraint': '纯元认知观察',
    'reflection': '纯元认知观察',
    'thinking': '纯元认知观察',
    'strategic': '自由列举',
    'method_selection': '自由列举',
    'direct_attempt': '小尝试',
    'direct_calculation': '小尝试',
    '直接计算': '小尝试',
    'constraint_extraction': '小尝试',
    'case_analysis': '小尝试',
    'edge_case_resolution': '小尝试',
    'key_insight': '思维操作引导',
    '关键洞察': '思维操作引导',
    'knowledge': '思维操作引导',
    'knowledge_application': '思维操作引导',
    '知识瓶颈': '思维操作引导',
    'structural_transformation': '思维操作引导',
    'calculation': '推进',
    'execution': '推进',
    '验证': '推进',
    'refinement': '能量传递引导',
}

def normalize_level(val):
    """将hint_level归一化到0-1。"""
    if isinstance(val, float) and 0 <= val <= 1:
        return val
    if isinstance(val, int):
        if val <= 1:
            return float(val)
        # 1-4整数→0-1浮点数
        return min(1.0, (val - 1) / 3.0)
    return 0.5  # fallback

# 5个新v3 profile
new_keys = ['compfiles_imo1970p6', 'compfiles_imo1971p5', 'compfiles_imo1971p6', 
            'compfiles_imo1972p5', 'compfiles_imo1973p5']

for key in new_keys:
    p = profiles.get(key)
    if not p:
        print(f'  {key}: NOT FOUND')
        continue
    
    fixed_sits = 0
    fixed_levels = 0
    
    # 修局部pairs
    for pair in p.get('tell_hint_pairs', []):
        old_sit = pair.get('situation_type', '')
        if old_sit in SIT_MAP:
            new_sit = SIT_MAP[old_sit]
            if new_sit != old_sit:
                pair['situation_type'] = new_sit
                fixed_sits += 1
        else:
            print(f'  {key}: 未知situation_type="{old_sit}"，保留')
        
        old_level = pair.get('hint_level', 0.5)
        new_level = normalize_level(old_level)
        if new_level != old_level:
            pair['hint_level'] = new_level
            fixed_levels += 1
    
    # 修全局pairs
    for gpair in p.get('global_tell_hint_pairs', []):
        old_level = gpair.get('hint_level', 0.5)
        new_level = normalize_level(old_level)
        if new_level != old_level:
            gpair['hint_level'] = new_level
            fixed_levels += 1
    
    profiles.update(p)
    print(f'  {key}: 修正{fixed_sits}个situation_type, {fixed_levels}个hint_level')

print('\n完成')
