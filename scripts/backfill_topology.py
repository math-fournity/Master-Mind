#!/usr/bin/env python3
"""
回补8个已有profile的per-pair tell_topology和tell_small_concepts。
根据每对的is_knowledge_bottleneck标志和profile级拓扑推断per-pair拓扑。
"""
from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
profiles = db.collection('problem_profiles')

# 获取所有profile
all_profiles = list(db.aql.execute('FOR p IN problem_profiles RETURN p'))

for p in all_profiles:
    pid = p['_key']
    profile_topology = p.get('tell_topology', {})
    profile_concepts = p.get('tell_small_concepts', [])
    
    # 回补局部tell_hint_pairs
    updated_pairs = []
    for pair in p.get('tell_hint_pairs', []):
        if 'tell_topology' not in pair:
            # 根据is_knowledge_bottleneck推断gap_type
            if pair.get('is_knowledge_bottleneck', False):
                gap_type = 'knowledge_gap'
            else:
                gap_type = profile_topology.get('gap_type', 'method_problem_mismatch')
            
            pair['tell_topology'] = {
                'problem_type': profile_topology.get('problem_type', ''),
                'ai_method_type': profile_topology.get('ai_method_type', ''),
                'gap_type': gap_type,
            }
            pair['tell_small_concepts'] = profile_concepts[:]
        
        updated_pairs.append(pair)
    
    # 回补全局global_tell_hint_pairs
    updated_globals = []
    for gpair in p.get('global_tell_hint_pairs', []):
        if 'tell_topology' not in gpair:
            gpair['tell_topology'] = {
                'problem_type': profile_topology.get('problem_type', ''),
                'ai_method_type': profile_topology.get('ai_method_type', ''),
                'gap_type': profile_topology.get('gap_type', 'method_problem_mismatch'),
            }
            gpair['tell_small_concepts'] = profile_concepts[:]
        
        updated_globals.append(gpair)
    
    # 更新数据库
    p['tell_hint_pairs'] = updated_pairs
    p['global_tell_hint_pairs'] = updated_globals
    p['schema_version'] = 3
    profiles.update(p)
    
    print(f'回补: {pid} ({len(updated_pairs)} local pairs, {len(updated_globals)} global pairs)')

print(f'\n完成，共回补 {len(all_profiles)} 个profile')
