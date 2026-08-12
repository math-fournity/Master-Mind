#!/usr/bin/env python3
"""入库OpenMathReasoning数据集 - 306K+193K AoPS竞赛题
字段: problem, inference_mode, problem_type, expected_answer, used_in_kaggle, generation_model, pass_rate_72b_tir, generated_solution, problem_source
inference_mode: cot / tir
"""
import json, hashlib, os, glob
import pyarrow.parquet as pq
from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529', request_timeout=300)
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
col = db.collection('problem_extraction_progress')

def ph(text):
    return hashlib.md5(text.strip().lower()[:500].encode()).hexdigest()

count = 0
skipped = 0
seen_hashes = set()
batch = []
batch_size = 5000
base = '/data/math-manify/raw_downloads/OpenMathReasoning'

for pf in sorted(glob.glob(os.path.join(base, '**/*.parquet'), recursive=True)):
    if '.cache' in pf:
        continue
    t = pq.read_table(pf)
    data = t.to_pylist()
    fname = os.path.basename(pf).replace('.parquet', '')
    for row in data:
        problem = row.get('problem', '')
        if not problem.strip():
            skipped += 1
            continue

        h = ph(problem)
        # 同一题目可能有cot和tir两个版本，去重
        if h in seen_hashes:
            skipped += 1
            continue
        seen_hashes.add(h)

        record = {
            '_key': f'openmath_reasoning_{h[:16]}',
            'problem_text': problem,
            'solution_text': row.get('generated_solution', ''),
            'answer': str(row.get('expected_answer', '')),
            'source_dataset': 'openmath_reasoning',
            'source_subset': fname,
            'inference_mode': row.get('inference_mode', ''),
            'problem_type': row.get('problem_type', ''),
            'problem_source': row.get('problem_source', ''),
            'difficulty_tier': 2,  # AoPS竞赛题
            'priority': 2,
            'extraction_status': 'pending',
            'skip_reason': None,
            'problem_hash': h,
            'pass_rate_72b_tir': row.get('pass_rate_72b_tir', None),
            'used_in_kaggle': row.get('used_in_kaggle', False),
            'local_path': pf,
            'ingest_date': '2026-08-12',
        }
        batch.append(record)
        count += 1
        if len(batch) >= batch_size:
            col.import_bulk(batch, on_duplicate='ignore')
            batch = []
            print(f'  已处理 {count}题...(skipped {skipped})', flush=True)

if batch:
    col.import_bulk(batch, on_duplicate='ignore')

print(f'OpenMathReasoning: {count}题处理完成 (skipped {skipped})', flush=True)
total = db.aql.execute('RETURN LENGTH(problem_extraction_progress)').next()
print(f'DB总量: {total}', flush=True)
