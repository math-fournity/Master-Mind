#!/usr/bin/env python3
"""全量检查export内容质量 + 与数据库交叉验证"""
import json, sys
from pathlib import Path
from collections import Counter

TRAJ = Path('/data/math-agent-glm5.2-tmux-agents-trajectory')

# 连接ArangoDB
from arango import ArangoClient
client = ArangoClient(hosts='http://localhost:8529', request_timeout=300)
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')

# 从数据库获取所有candidate_solved记录
cursor = db.aql.execute(
    'FOR a IN devin_problem_runs FILTER a.batch_id == "pipe-runner" AND a.status == "candidate_solved" RETURN {exp_id: a.exp_id, problem_key: a.problem_key, verdict: a.verdict}',
    ttl=120
)
db_records = {r['exp_id']: r for r in cursor}
print(f'数据库中candidate_solved: {len(db_records)}')

exports = list(TRAJ.glob('p*/exports/conversation.json'))
print(f'磁盘上export文件: {len(exports)}')

# 全量分析
stats = {
    'total': 0,
    'has_reasoning': 0,
    'has_message': 0,  # agent message非空
    'has_tool_calls': 0,
    'has_proof_complete_in_reasoning': 0,
    'has_proof_complete_in_message': 0,
    'has_boxed': 0,
    'has_qed': 0,
    'reasoning_empty': 0,
    'reasoning_lt_1kb': 0,
    'reasoning_1_10kb': 0,
    'reasoning_10_50kb': 0,
    'reasoning_50_100kb': 0,
    'reasoning_gt_100kb': 0,
}

# 交叉验证
db_says_solved_but_export_no_proof = []
export_has_proof_but_db_not_solved = []
no_db_record = []

for p in exports:
    eid = p.parent.parent.name
    stats['total'] += 1
    try:
        data = json.loads(p.read_text())
        steps = data.get('steps', [])
        agent_step = None
        for step in steps:
            if step.get('source') == 'agent':
                agent_step = step
                break

        if not agent_step:
            stats['reasoning_empty'] += 1
            continue

        reasoning = agent_step.get('reasoning_content', '') or ''
        message = agent_step.get('message', '') or ''
        tool_calls = agent_step.get('tool_calls', []) or []

        rlen = len(str(reasoning))
        mlen = len(str(message))

        if rlen > 0: stats['has_reasoning'] += 1
        if mlen > 0: stats['has_message'] += 1
        if tool_calls: stats['has_tool_calls'] += 1

        if rlen == 0: stats['reasoning_empty'] += 1
        elif rlen < 1024: stats['reasoning_lt_1kb'] += 1
        elif rlen < 10240: stats['reasoning_1_10kb'] += 1
        elif rlen < 51200: stats['reasoning_10_50kb'] += 1
        elif rlen < 102400: stats['reasoning_50_100kb'] += 1
        else: stats['reasoning_gt_100kb'] += 1

        r_upper = str(reasoning).upper()
        m_upper = str(message).upper()
        combined = r_upper + m_upper

        has_proof = 'PROOF COMPLETE' in combined or '证明完成' in str(reasoning) + str(message)
        has_boxed = 'BOXED' in combined or '\\BOXED' in str(reasoning) + str(message)
        has_qed = 'QED' in combined or '∎' in str(reasoning) + str(message)

        if has_proof: stats['has_proof_complete_in_reasoning'] += 1
        if 'PROOF COMPLETE' in m_upper: stats['has_proof_complete_in_message'] += 1
        if has_boxed: stats['has_boxed'] += 1
        if has_qed: stats['has_qed'] += 1

        # 交叉验证
        if eid in db_records:
            db_verdict = db_records[eid].get('verdict', '')
            if db_verdict == 'candidate_solved' and not has_proof and not has_boxed and not has_qed:
                db_says_solved_but_export_no_proof.append((eid, db_records[eid]['problem_key'], rlen, mlen))
        else:
            no_db_record.append(eid)

    except Exception as e:
        print(f'PARSE ERROR {eid}: {e}', file=sys.stderr)

print(f'\n=== Export内容质量统计 ===')
print(f'  总export数:              {stats["total"]}')
print(f'  有reasoning_content:     {stats["has_reasoning"]}')
print(f'  agent message非空:       {stats["has_message"]}')
print(f'  有tool_calls:            {stats["has_tool_calls"]}')
print(f'  含PROOF COMPLETE:        {stats["has_proof_complete_in_reasoning"]}')
print(f'  含boxed:                 {stats["has_boxed"]}')
print(f'  含QED:                   {stats["has_qed"]}')
print()
print(f'=== reasoning_content大小分布 ===')
print(f'  空(0B):           {stats["reasoning_empty"]}')
print(f'  <1KB:             {stats["reasoning_lt_1kb"]}')
print(f'  1-10KB:           {stats["reasoning_1_10kb"]}')
print(f'  10-50KB:          {stats["reasoning_10_50kb"]}')
print(f'  50-100KB:         {stats["reasoning_50_100kb"]}')
print(f'  >100KB:           {stats["reasoning_gt_100kb"]}')

print(f'\n=== 交叉验证 ===')
print(f'  DB有记录的export:        {stats["total"] - len(no_db_record)}')
print(f'  DB无记录的export:        {len(no_db_record)}')
print(f'  DB说solved但export无证明标记: {len(db_says_solved_but_export_no_proof)}')

if db_says_solved_but_export_no_proof:
    print(f'\n=== DB说solved但export无PROOF COMPLETE的样本(前10) ===')
    for eid, pk, rlen, mlen in db_says_solved_but_export_no_proof[:10]:
        print(f'  {eid} {pk} reasoning={rlen}B message={mlen}B')
