#!/usr/bin/env python3
"""入库DART-Math-Hard数据集 - 批量版本，跳过已存在记录"""
import json, hashlib, os, glob, sys
import pyarrow.parquet as pq
from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
col = db.collection('problem_extraction_progress')

def ph(text):
    return hashlib.md5(text.strip().lower()[:500].encode()).hexdigest()

# 先查已有数量
existing = db.aql.execute('FOR d IN problem_extraction_progress FILTER d.source_dataset == "dart_math_hard" COLLECT WITH COUNT INTO c RETURN c').next()
print(f'已有dart_math_hard记录: {existing}', flush=True)

count = 0
skipped = 0
batch = []
batch_size = 5000
base = '/data/math-manify/raw_downloads/DART-Math-Hard'

for pf in sorted(glob.glob(os.path.join(base, '**/*.parquet'), recursive=True)):
    if '.cache' in pf:
        continue
    t = pq.read_table(pf)
    data = t.to_pylist()
    for row in data:
        query = row.get('query', '')
        if not query.strip():
            continue
        # GSM8K是小学题，跳过
        has_latex = '\\' in query and ('frac' in query or 'begin' in query or 'sqrt' in query or 'cdot' in query or 'alpha' in query or 'beta' in query or 'theta' in query or 'angle' in query or 'triangle' in query or 'leq' in query or 'geq' in query)
        is_short = len(query) < 100
        if is_short and not has_latex:
            skipped += 1
            continue

        # 用problem_hash做key的一部分，避免冲突
        h = ph(query)
        record = {
            '_key': f'dart_math_{h[:16]}',
            'problem_text': query,
            'solution_text': row.get('response', ''),
            'source_dataset': 'dart_math_hard',
            'source_subset': os.path.basename(pf).replace('.parquet', ''),
            'difficulty_tier': 2,
            'priority': 2,
            'extraction_status': 'pending',
            'skip_reason': None,
            'problem_hash': h,
            'local_path': pf,
            'ingest_date': '2026-08-12',
        }
        batch.append(record)
        count += 1
        if len(batch) >= batch_size:
            col.import_bulk(batch, on_duplicate='ignore')
            batch = []
            print(f'  已处理 {count}题...(skipped {skipped})', flush=True)

# 剩余
if batch:
    col.import_bulk(batch, on_duplicate='ignore')

print(f'DART-Math-Hard: {count}题处理完成 (skipped {skipped})', flush=True)
total = db.aql.execute('RETURN LENGTH(problem_extraction_progress)').next()
print(f'DB总量: {total}', flush=True)
