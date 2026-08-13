#!/usr/bin/env python3
"""检查export文件内容质量——ATIF-v1.7格式"""
import json, random, sys
from pathlib import Path
from collections import Counter

TRAJ = Path('/data/math-agent-glm5.2-tmux-agents-trajectory')

exports = list(TRAJ.glob('p*/exports/conversation.json'))
print(f'总export数: {len(exports)}')

# 全量统计
size_buckets = {'0B': 0, '<10KB': 0, '10-50KB': 0, '50-100KB': 0, '100-200KB': 0, '>200KB': 0}
step_counts = []
source_dist = Counter()
has_proof_complete = 0
has_thinking = 0
has_tool_calls = 0
has_reasoning = 0
empty_assistant = 0
total_assistant_text = 0

for p in exports:
    size = p.stat().st_size
    if size == 0: size_buckets['0B'] += 1
    elif size < 10240: size_buckets['<10KB'] += 1
    elif size < 51200: size_buckets['50-100KB'] += 1  # placeholder, fixed below
    elif size < 102400: size_buckets['50-100KB'] += 1
    elif size < 204800: size_buckets['100-200KB'] += 1
    else: size_buckets['>200KB'] += 1

    try:
        data = json.loads(p.read_text())
        steps = data.get('steps', [])
        step_counts.append(len(steps))

        assistant_text_len = 0
        for step in steps:
            src = step.get('source', 'unknown')
            source_dist[src] += 1
            msg = step.get('message', '')
            if isinstance(msg, str):
                content = msg
            else:
                content = str(msg)

            if src in ('assistant', 'chat', 'model'):
                assistant_text_len += len(content)
                if 'PROOF COMPLETE' in content.upper():
                    has_proof_complete += 1
                if step.get('reasoning_content'):
                    has_reasoning += 1
                if step.get('tool_calls'):
                    has_tool_calls += 1

        if assistant_text_len == 0:
            empty_assistant += 1
        total_assistant_text += assistant_text_len
    except Exception as e:
        print(f'  PARSE ERROR: {p.parent.parent.name}: {e}', file=sys.stderr)

# 修正size bucket（<50KB的归类错误）
size_buckets['50-100KB'] = 0
for p in exports:
    size = p.stat().st_size
    if size == 0: pass
    elif size < 10240: pass
    elif size < 51200: size_buckets['50-100KB'] = size_buckets.get('50-100KB', 0)  # will recount
# 重新计算
size_buckets = {'0B': 0, '<10KB': 0, '10-50KB': 0, '50-100KB': 0, '100-200KB': 0, '>200KB': 0}
for p in exports:
    size = p.stat().st_size
    if size == 0: size_buckets['0B'] += 1
    elif size < 10240: size_buckets['<10KB'] += 1
    elif size < 51200: size_buckets['10-50KB'] += 1
    elif size < 102400: size_buckets['50-100KB'] += 1
    elif size < 204800: size_buckets['100-200KB'] += 1
    else: size_buckets['>200KB'] += 1

print(f'\n=== 文件大小分布 ===')
for k, v in size_buckets.items():
    print(f'  {k:12s}: {v}')

print(f'\n=== step数量分布 ===')
if step_counts:
    print(f'  min={min(step_counts)} max={max(step_counts)} avg={sum(step_counts)/len(step_counts):.1f}')
    sc = Counter()
    for n in step_counts:
        if n == 0: sc['0步'] += 1
        elif n < 5: sc['1-4步'] += 1
        elif n < 10: sc['5-9步'] += 1
        elif n < 20: sc['10-19步'] += 1
        elif n < 50: sc['20-49步'] += 1
        else: sc['50+步'] += 1
    for k in ['0步', '1-4步', '5-9步', '10-19步', '20-49步', '50+步']:
        print(f'  {k:10s}: {sc.get(k, 0)}')

print(f'\n=== source分布(前10) ===')
for src, cnt in source_dist.most_common(10):
    print(f'  {src:20s}: {cnt}')

print(f'\n=== 内容质量 ===')
print(f'  含PROOF COMPLETE:     {has_proof_complete}')
print(f'  含reasoning_content:  {has_reasoning}')
print(f'  含tool_calls:         {has_tool_calls}')
print(f'  assistant文本为空:    {empty_assistant}')
print(f'  assistant总文本量:    {total_assistant_text}B (avg={total_assistant_text/len(exports):.0f}B/题)')

# 抽样看3个完整的assistant step内容
print(f'\n=== 抽样：3个export的assistant最后一条消息(前500字) ===')
random.seed(123)
samples = random.sample(exports, min(3, len(exports)))
for p in samples:
    data = json.loads(p.read_text())
    steps = data.get('steps', [])
    eid = p.parent.parent.name
    last_asst = None
    for step in steps:
        if step.get('source') in ('assistant', 'chat', 'model'):
            last_asst = step
    if last_asst:
        msg = last_asst.get('message', '')
        reasoning = last_asst.get('reasoning_content', '')
        tool_calls = last_asst.get('tool_calls', [])
        print(f'\n  [{eid}]')
        print(f'    message前500字: {str(msg)[:500]!r}')
        if reasoning:
            print(f'    reasoning前300字: {str(reasoning)[:300]!r}')
        if tool_calls:
            print(f'    tool_calls数: {len(tool_calls)}')
    else:
        print(f'\n  [{eid}] 无assistant step')
