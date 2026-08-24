#!/usr/bin/env python3
"""检查最近1小时吞吐量，区分全部终态和正常结束（排除基础设施失败）"""
import os
from datetime import datetime, timedelta, timezone
from arango import ArangoClient

c = ArangoClient(hosts=os.environ.get('ARANGO_HOST', 'http://localhost:8529'))
db = c.db(os.environ['ARANGO_DB'], username=os.environ.get('ARANGO_USER', 'root'),
          password=os.environ.get('ARANGO_PASS', ''))

now = datetime.now(timezone.utc)
start = now - timedelta(hours=1)
s_str = start.strftime('%Y-%m-%dT%H:%M')

# 全部终态
all_rows = list(db.aql.execute(
    'FOR r IN devin_problem_runs FILTER r.ended_at >= @s FILTER r.fixed_by == null '
    'COLLECT status = r.status WITH COUNT INTO cnt SORT cnt DESC RETURN {status, cnt}',
    bind_vars={'s': s_str}))

# 基础设施失败（devin cli上来就偶发失败，不算正常结束）
infra_failures = {
    'rate_limited', 'dead_session', 'launch_error', 'failed_connection',
    'failed_network_stuck', 'crash_recovered', 'answer_leak_in_input',
    'empty_problem_text', 'export_missing'
}
normal_rows = [r for r in all_rows if r['status'] not in infra_failures]

all_total = sum(r['cnt'] for r in all_rows)
normal_total = sum(r['cnt'] for r in normal_rows)
normal_solved = sum(r['cnt'] for r in normal_rows if r['status'] == 'candidate_solved')

print(f'=== 最近1小时（当前并发: 30）===')
print(f'全部终态: {all_total}题/时')
print(f'正常结束（排除基础设施失败）: {normal_total}题/时')
if normal_total:
    print(f'  其中solved: {normal_solved} ({normal_solved/normal_total*100:.0f}%)')
print()
print('全部终态分布:')
for r in all_rows:
    tag = ' [基础设施]' if r['status'] in infra_failures else ''
    print(f'  {r["status"]:25s} {r["cnt"]:>4}{tag}')
print()
print('正常结束分布:')
for r in normal_rows:
    print(f'  {r["status"]:25s} {r["cnt"]:>4}')

# solved的平均解题时间
solved_times = list(db.aql.execute(
    'FOR r IN devin_problem_runs FILTER r.ended_at >= @s '
    'FILTER r.status == "candidate_solved" '
    'FILTER r.solve_time_seconds != null AND r.solve_time_seconds > 0 '
    'RETURN r.solve_time_seconds',
    bind_vars={'s': s_str}))
if solved_times:
    solved_times.sort()
    n = len(solved_times)
    avg = sum(solved_times) / n
    median = solved_times[n // 2]
    print(f'\nsolved解题时间: avg={avg:.0f}s median={median:.0f}s n={n}')
