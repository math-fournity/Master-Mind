#!/usr/bin/env python3
"""入库OpenR1-Math-Raw数据集 - 516K NuminaMath去重
字段: problem, solution, answer, problem_type, question_type, problem_is_valid, solution_is_valid, source, synthetic, generations, generations_count, correctness, reparsed_answers
"""
import json, hashlib, os, glob
import pyarrow.parquet as pq
from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
col = db.collection('problem_extraction_progress')

def ph(text):
    return hashlib.md5(text.strip().lower()[:500].encode()).hexdigest()

count = 0
skipped = 0
batch = []
batch_size = 5000
base = '/data/math-manify/raw_downloads/OpenR1-Math-Raw'

for pf in sorted(glob.glob(os.path.join(base, '**/*.parquet'), recursive=True)):
    if '.cache' in pf:
        continue
    t = pq.read_table(pf)
    data = t.to_pylist()
    for row in data:
        problem = row.get('problem', '')
        if not problem.strip():
            skipped += 1
            continue
        # 只入库valid的题目
        if row.get('problem_is_valid') is False:
            skipped += 1
            continue

        h = ph(problem)
        answer = row.get('answer', '')
        if not answer:
            # 尝试reparsed_answers
            reparsed = row.get('reparsed_answers', [])
            if reparsed and isinstance(reparsed, list) and len(reparsed) > 0:
                answer = reparsed[0] if reparsed[0] else ''

        record = {
            '_key': f'openr1_math_{h[:16]}',
            'problem_text': problem,
            'solution_text': row.get('solution', ''),
            'answer': str(answer) if answer else '',
            'source_dataset': 'openr1_math_raw',
            'source_subset': row.get('source', ''),
            'problem_type': row.get('problem_type', ''),
            'question_type': row.get('question_type', ''),
            'difficulty_tier': 2,  # NuminaMath去重，竞赛级别
            'priority': 2,
            'extraction_status': 'pending',
            'skip_reason': None,
            'problem_hash': h,
            'synthetic': row.get('synthetic', False),
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

print(f'OpenR1-Math-Raw: {count}题处理完成 (skipped {skipped})', flush=True)
total = db.aql.execute('RETURN LENGTH(problem_extraction_progress)').next()
print(f'DB总量: {total}', flush=True)
