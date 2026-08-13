#!/usr/bin/env python3
"""fix_false_positive_solved.py — 修复collector误判的candidate_solved记录

Bug: collector的has_real_proof匹配了提示词中的"PROOF COMPLETE"，
导致267个实际未完成的题被误判为candidate_solved。

修复策略：
1. 遍历所有candidate_solved记录
2. 用新的find_ai_proof_marker检查pane_snapshot
3. 对pane无真实PROOF COMPLETE的，再检查export文件
4. 如果export也无真实PROOF COMPLETE，重新分类：
   - 无export → dead_session（基础设施失败）
   - export有reasoning>50KB → failed_token_limit
   - export有放弃标记 → ai_gave_up
   - 其他 → failed_stall
5. 把题目重新入队pending
"""
import json, re, sys, time
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent.parent / "xishujuzhen" / "solver_harness" / "pipe"))
from collector import find_ai_proof_marker, clean_ansi, AI_GAVE_UP_PATTERNS
from redis_queue import get_redis, enqueue_pending

TRAJ = Path("/data/math-agent-glm5.2-tmux-agents-trajectory")

from arango import ArangoClient
client = ArangoClient(hosts='http://localhost:8529', request_timeout=300)
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')

# 1. 获取所有candidate_solved记录
cursor = db.aql.execute(
    'FOR a IN devin_problem_runs FILTER a.batch_id == "pipe-runner" AND a.status == "candidate_solved" '
    'RETURN {_key: a._key, exp_id: a.exp_id, problem_id: a.problem_id, '
    'started_at: a.started_at, ended_at: a.ended_at, runtime_seconds: a.runtime_seconds}',
    ttl=120
)
solved_records = list(cursor)
print(f"DB中candidate_solved: {len(solved_records)}")

# 2. 逐个检查
r = get_redis()
to_fix = []
real_solved = 0

for rec in solved_records:
    eid = rec['exp_id']
    pk = rec.get('problem_key')

    # 检查pane
    pane_file = TRAJ / eid / 'collector' / 'pane_snapshot.txt'
    pane_has_proof = False
    if pane_file.exists():
        pane_text = pane_file.read_text(errors='ignore')
        idx, marker = find_ai_proof_marker(clean_ansi(pane_text))
        pane_has_proof = idx is not None

    if pane_has_proof:
        real_solved += 1
        continue

    # pane无真实PROOF COMPLETE——检查export
    export_file = TRAJ / eid / 'exports' / 'conversation.json'
    export_has_proof = False
    export_info = {}

    if export_file.exists():
        try:
            data = json.loads(export_file.read_text())
            steps = data.get('steps', [])
            agent_step = next((s for s in steps if s.get('source') == 'agent'), None)
            if agent_step:
                reasoning = str(agent_step.get('reasoning_content', '') or '')
                message = str(agent_step.get('message', '') or '')
                combined = reasoning + message
                all_matches = list(re.finditer(r'PROOF COMPLETE', combined, re.IGNORECASE))
                ai_proofs = sum(1 for m in all_matches
                                if '结尾输出' not in combined[max(0, m.start()-30):m.end()+30]
                                and 'Pro ·' not in combined[max(0, m.start()-30):m.end()+30])
                export_has_proof = ai_proofs > 0
                export_info = {'reasoning_len': len(reasoning), 'message_len': len(message)}
        except Exception:
            pass

    if export_has_proof:
        real_solved += 1
        continue

    # 真正的误判——确定新status
    if not export_file.exists():
        new_status = 'dead_session'
        new_verdict = 'dead_session'
    elif export_info.get('reasoning_len', 0) > 50000:
        new_status = 'failed_token_limit'
        new_verdict = 'failed_token_limit'
    else:
        # 检查是否有放弃标记
        combined_check = ''
        if export_file.exists():
            try:
                data = json.loads(export_file.read_text())
                steps = data.get('steps', [])
                agent_step = next((s for s in steps if s.get('source') == 'agent'), None)
                if agent_step:
                    combined_check = str(agent_step.get('reasoning_content', '') or '') + \
                                     str(agent_step.get('message', '') or '')
            except Exception:
                pass

        gave_up = any(p in combined_check for p in AI_GAVE_UP_PATTERNS)
        if gave_up:
            new_status = 'ai_gave_up'
            new_verdict = 'ai_gave_up'
        else:
            new_status = 'failed_stall'
            new_verdict = 'failed_stall'

    to_fix.append({
        '_key': rec['_key'],
        'exp_id': eid,
        'problem_id': rec.get('problem_id'),
        'new_status': new_status,
        'new_verdict': new_verdict,
        'pane_size': pane_file.stat().st_size if pane_file.exists() else 0,
        'has_export': export_file.exists(),
        **export_info,
    })

print(f"\n真实解题: {real_solved}")
print(f"误判需修复: {len(to_fix)}")

# 统计新分类
new_status_dist = Counter(f['new_status'] for f in to_fix)
print(f"\n新分类分布:")
for s, c in new_status_dist.most_common():
    print(f"  {s}: {c}")

# 3. 执行修复
print(f"\n=== 执行数据库修复 ===")
collection = db.collection('devin_problem_runs')
fixed = 0
requeued = 0
for item in to_fix:
    try:
        # 更新数据库——python-arango需要_key在文档内
        collection.update({
            '_key': item['_key'],
            'status': item['new_status'],
            'verdict': item['new_verdict'],
            'reclassified_at': time.time(),
            'reclassified_reason': 'collector_bug: 提示词PROOF COMPLETE误匹配',
        })
        fixed += 1

        # 重新入队
        pid = item['problem_id']
        if pid:
            enqueue_pending(r, pid, priority=1)
            requeued += 1
    except Exception as e:
        print(f"  ERROR fixing {item['exp_id']}: {e}", file=sys.stderr)

print(f"数据库修复: {fixed}条")
print(f"重新入队: {requeued}条")

# 4. 更新Redis completed/failed队列
# 从completed队列移除误判的，加入failed队列
print(f"\n=== 更新Redis队列 ===")
completed_items = r.lrange('math:completed', 0, -1)
removed = 0
for item_bytes in completed_items:
    try:
        item = json.loads(item_bytes)
        if item.get('exp_id') in {f['exp_id'] for f in to_fix}:
            r.lrem('math:completed', 1, item_bytes)
            # 加入failed队列
            item['status'] = item.get('status', 'dead_session')
            item['verdict'] = item.get('verdict', 'dead_session')
            item['reclassified'] = True
            r.lpush('math:failed', json.dumps(item))
            removed += 1
    except Exception:
        pass

print(f"从completed移除: {removed}条")
print(f"加入failed: {removed}条")

# 最终状态
print(f"\n=== 最终状态 ===")
print(f"  completed: {r.llen('math:completed')}")
print(f"  failed: {r.llen('math:failed')}")
print(f"  pending: {r.zcard('math:pending')}")
print(f"  running: {r.hlen('math:running')}")
