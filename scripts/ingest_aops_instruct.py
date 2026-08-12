#!/usr/bin/env python3
"""入库AoPS-Instruct数据集 - 600K AoPS论坛QA pairs
字段: original_question, rewritten_question, original_answers(list), rewritten_answers(list)
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
base = '/data/math-manify/raw_downloads/AoPS-Instruct'

for pf in sorted(glob.glob(os.path.join(base, '**/*.parquet'), recursive=True)):
    if '.cache' in pf:
        continue
    t = pq.read_table(pf)
    data = t.to_pylist()
    for row in data:
        # 用rewritten_question（改写后的题目，质量更高）
        question = row.get('rewritten_question', '') or row.get('original_question', '')
        if not question.strip():
            skipped += 1
            continue
        # 用rewritten_answers（改写后的解答，step-by-step）
        rewritten = row.get('rewritten_answers', [])
        original = row.get('original_answers', [])
        # 取第一个改写解答
        answer = rewritten[0] if rewritten and isinstance(rewritten, list) and len(rewritten) > 0 else ''
        if not answer and original:
            answer = original[0] if isinstance(original, list) and len(original) > 0 else str(original)

        h = ph(question)
        record = {
            '_key': f'aops_instruct_{h[:16]}',
            'problem_text': question,
            'solution_text': answer,
            'source_dataset': 'aops_instruct',
            'source_subset': os.path.basename(pf).replace('.parquet', ''),
            'difficulty_tier': 2,  # AoPS论坛题，奥赛级别
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

if batch:
    col.import_bulk(batch, on_duplicate='ignore')

print(f'AoPS-Instruct: {count}题处理完成 (skipped {skipped})', flush=True)
total = db.aql.execute('RETURN LENGTH(problem_extraction_progress)').next()
print(f'DB总量: {total}', flush=True)
