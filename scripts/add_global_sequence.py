#!/usr/bin/env python3
"""
给problem_extraction_progress中每条记录加global_sequence字段。
排序规则：difficulty_tier ASC, problem_id ASC
这样global_sequence就是题目的全局顺序编号，可以用来记录"处理到了第几题"。
"""
from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')

# 按difficulty_tier + problem_id排序
docs = list(db.aql.execute(
    'FOR p IN problem_extraction_progress SORT p.difficulty_tier, p.problem_id RETURN p._key'
))

print(f'总共{len(docs)}条记录，开始添加global_sequence...')

# 批量更新
coll = db.collection('problem_extraction_progress')
batch = []
for i, key in enumerate(docs, 1):
    batch.append({'_key': key, 'global_sequence': i})
    if len(batch) >= 1000:
        coll.update_many(batch)
        batch = []
        if i % 5000 == 0:
            print(f'  已处理 {i}/{len(docs)}')
if batch:
    coll.update_many(batch)

print(f'完成，已为{len(docs)}条记录添加global_sequence (1~{len(docs)})')

# 验证
sample = list(db.aql.execute(
    'FOR p IN problem_extraction_progress SORT p.global_sequence LIMIT 3 RETURN {seq: p.global_sequence, key: p._key, pid: p.problem_id, tier: p.difficulty_tier}'
))
print('验证（前3条）:')
for s in sample:
    print(f'  seq={s["seq"]} key={s["key"]} pid={s["pid"]} tier={s["tier"]}')

# Tier 1的seq范围
tier1 = list(db.aql.execute(
    'FOR p IN problem_extraction_progress FILTER p.difficulty_tier == 1 SORT p.global_sequence RETURN {min: MIN(p.global_sequence), max: MAX(p.global_sequence)}'
))
print(f'Tier 1: global_sequence范围 {tier1}')
