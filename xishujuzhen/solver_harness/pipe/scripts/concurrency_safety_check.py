#!/usr/bin/env python3
"""concurrency_safety_check.py — 管道化系统并发安全性专项检查

检查多进程同时操作共享资源时的竞态条件和资源泄漏。
pipe_control.py health检查运行时健康，本脚本检查并发安全性。

检查维度：
  A. Redis操作原子性——dequeue+add_running间隙的丢题风险
  B. DB-Redis一致性——DB running数 vs Redis running数，孤儿记录
  C. 重复attempt检测——同一problem_key被多个attempt同时running
  D. 并发上限实际验证——设定并发 vs Redis running vs harness session数
  E. devin进程数 vs 并发数——僵尸devin进程堆积
  F. collector处理速率 vs runner启动速率——速率比，running是否堆积
  G. auto-restart验证——服务退出后是否真的5秒内重启
  H. 日志重复写入——tee -a + RotatingFileHandler导致每行写两遍

用法:
  cd ~/master-mind-glm5.2-worktree
  set -a; source .env; set +a
  PYTHONPATH=xishujuzhen/solver_harness/pipe .venv/bin/python3 \\
    xishujuzhen/solver_harness/pipe/scripts/concurrency_safety_check.py
"""
import json
import os
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from redis_queue import get_redis, get_all_running, running_count, pending_count

from arango import ArangoClient

TRAJ = Path("/data/math-agent-glm5.2-tmux-agents-trajectory")
LOG_DIR = TRAJ / "_pipe" / "logs"


def check_a_redis_atomicity(r):
    """A. Redis操作原子性——检查dequeue+add_running间隙的丢题风险"""
    print("【A. Redis操作原子性】")
    # zpopmin是原子的，但dequeue_pending→add_running之间crash会丢题
    # 检查方法：看pending中是否有刚被dequeue但没add_running的题
    # 间接检查：running中的attempt是否都在DB中有对应记录
    print("  zpopmin是原子操作 ✅")
    print("  dequeue→add_running间隙crash会丢题（已知风险，auto-restart兜底）")
    # 检查running中是否有attempt_key为空的记录（dequeue后没来得及写DB）
    running = get_all_running(r)
    no_attempt_key = sum(1 for v in running.values() if not v.get("attempt_key"))
    print(f"  running中attempt_key为空: {no_attempt_key}", "❌" if no_attempt_key else "✅")
    return no_attempt_key


def check_b_db_redis_consistency(db, r):
    """B. DB-Redis一致性——DB running数 vs Redis running数"""
    print("【B. DB-Redis一致性】")
    redis_running = r.hlen("math:running")
    redis_running_keys = set(r.hkeys("math:running"))

    db_running = list(db.aql.execute('''
        FOR r IN devin_problem_runs
            FILTER r.exp_id LIKE "p%"
            FILTER r.status == "running"
            RETURN r.exp_id
    '''))
    db_running_set = set(db_running)

    print(f"  Redis running: {redis_running}")
    print(f"  DB running:    {len(db_running)}")

    # Redis有但DB没有——runner还没来得及写DB
    redis_not_db = redis_running_keys - db_running_set
    # DB有但Redis没有——孤儿记录（collector先remove_running后update_db_status的旧bug）
    db_not_redis = db_running_set - redis_running_keys

    print(f"  Redis有DB无: {len(redis_not_db)}", "⚠️" if redis_not_db else "✅", "(runner正在写DB)")
    print(f"  DB有Redis无(孤儿): {len(db_not_redis)}", "❌" if db_not_redis else "✅")
    if db_not_redis:
        print(f"    孤儿示例: {list(db_not_redis)[:3]}")
    return len(db_not_redis)


def check_c_duplicate_attempt(r):
    """C. 重复attempt检测——同一problem_key被多个attempt同时running"""
    print("【C. 重复attempt检测】")
    running = get_all_running(r)
    pks = [v.get("problem_key", "") for v in running.values()]
    dupes = {k: v for k, v in Counter(pks).items() if v > 1}
    print(f"  running中attempt数: {len(pks)}")
    print(f"  唯一problem_key数: {len(set(pks))}")
    print(f"  重复problem_key: {len(dupes)}", "❌" if dupes else "✅")
    if dupes:
        for pk, cnt in dupes.items():
            print(f"    {pk}: {cnt}次")
    return len(dupes)


def check_d_concurrency_limit(r):
    """D. 并发上限实际验证——设定并发 vs Redis running vs harness session数"""
    print("【D. 并发上限实际验证】")
    conc_raw = r.get("math:config:concurrency")
    conc = int(conc_raw) if conc_raw else 0
    redis_running = r.hlen("math:running")

    result = subprocess.run(["tmux", "list-sessions"], capture_output=True, text=True)
    harness_p = sum(1 for line in result.stdout.split("\n") if "harness-p" in line and "harness-dbmon" not in line)
    harness_dbmon = sum(1 for line in result.stdout.split("\n") if "harness-dbmon-p" in line)

    print(f"  设定并发:        {conc}")
    print(f"  Redis running:   {redis_running}")
    print(f"  harness-p:       {harness_p}")
    print(f"  harness-dbmon:   {harness_dbmon}")

    # running不应超过并发+5（允许少量超出，runner取题到add_running有间隙）
    over_limit = redis_running > conc + 5
    print(f"  running超并发:   {'❌' if over_limit else '✅'} (允许+5)")
    return 1 if over_limit else 0


def check_e_devin_process_count():
    """E. devin进程数 vs 并发数——僵尸devin进程堆积"""
    print("【E. devin进程数 vs 并发数】")
    result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
    devin_procs = [line for line in result.stdout.split("\n") if "devin" in line and "grep" not in line and "concurrency_safety" not in line]
    # 过滤掉devin cli自身的管理进程（只看node进程）
    node_procs = [p for p in devin_procs if "node" in p]

    print(f"  devin相关进程: {len(devin_procs)}")
    print(f"  其中node进程:  {len(node_procs)}")

    # 正常情况：每个并发1个devin cli进程 + 1个node子进程
    # 僵尸进程 = 总进程数 - 2*并发数
    return len(devin_procs)


def check_f_rate_balance(r):
    """F. collector处理速率 vs runner启动速率"""
    print("【F. collector处理速率 vs runner启动速率】")
    # 从collector日志中提取最近几轮的completed/failed数
    collector_log = LOG_DIR / "collector.log"
    if not collector_log.exists():
        print("  collector.log不存在")
        return 0

    import re
    log_text = collector_log.read_text(errors="ignore")
    rounds = re.findall(r"第(\d+)轮扫描结束: 本轮 completed=(\d+) failed=(\d+) infra=(\d+)", log_text)
    if len(rounds) < 2:
        print(f"  collector日志中只有{len(rounds)}轮，不足以计算速率")
        return 0

    recent_rounds = rounds[-5:] if len(rounds) >= 5 else rounds
    total_processed = sum(int(c) + int(f) + int(i) for _, c, f, i in recent_rounds)
    avg_per_round = total_processed / len(recent_rounds)
    print(f"  最近{len(recent_rounds)}轮平均每轮处理: {avg_per_round:.1f}题")

    # runner每3秒启动1个，collector每poll_interval秒扫一轮
    # 如果collector每轮处理 < runner每轮启动，running会堆积
    print(f"  runner每3秒启动1题 = 每分钟20题")
    print(f"  collector每轮处理{avg_per_round:.1f}题")
    if avg_per_round < 20:
        print(f"  ⚠️ collector速率可能跟不上runner（每轮{avg_per_round:.1f} < 每分钟20）")
        return 1
    else:
        print(f"  ✅ collector速率跟上runner")
        return 0


def check_g_auto_restart():
    """G. auto-restart验证——服务是否在auto-restart模式下运行

    检查方法：看tmux session的主进程是否是bash while循环（auto-restart），
    而不是直接python进程。用ps检查session对应的进程树。
    """
    print("【G. auto-restart验证】")
    result = subprocess.run(["tmux", "list-sessions"], capture_output=True, text=True)
    services = ["feeder", "runner", "collector", "reporter", "retry"]
    issues = 0
    for svc in services:
        session_name = f"pipe-{svc}"
        if session_name not in result.stdout:
            print(f"  {svc}: ❌ 未运行")
            issues += 1
            continue

        # 检查tmux session的pane进程——auto-restart模式下主进程是zsh/bash（while循环）
        # 非auto-restart模式下主进程是python
        pane_pid_result = subprocess.run(
            ["tmux", "list-panes", "-t", session_name, "-F", "#{pane_pid}"],
            capture_output=True, text=True
        )
        pane_pid = pane_pid_result.stdout.strip().split("\n")[0] if pane_pid_result.stdout.strip() else ""

        # 检查pane_pid的子进程是否包含while循环
        # 用ps看pane_pid的完整进程树
        ps_result = subprocess.run(
            ["ps", "-o", "pid,ppid,command", "-p", pane_pid],
            capture_output=True, text=True
        )
        # 看pane_pid的子进程
        children = subprocess.run(
            ["pgrep", "-P", pane_pid],
            capture_output=True, text=True
        ).stdout.strip().split("\n") if pane_pid else []

        # 检查子进程中是否有python（说明while循环在运行python）
        # 或检查pane_pid的command是否包含while
        has_auto_restart = False
        if pane_pid:
            # 看pane进程的命令行
            cmd_result = subprocess.run(
                ["ps", "-o", "command=", "-p", pane_pid],
                capture_output=True, text=True
            )
            cmd = cmd_result.stdout.strip()
            if "while true" in cmd or "auto-restart" in cmd:
                has_auto_restart = True
            # 检查子进程链——auto-restart的while循环会fork出zsh→python
            if not has_auto_restart and children and children[0]:
                for child_pid in children:
                    if not child_pid:
                        continue
                    child_cmd = subprocess.run(
                        ["ps", "-o", "command=", "-p", child_pid],
                        capture_output=True, text=True
                    ).stdout.strip()
                    if "while true" in child_cmd or "auto-restart" in child_cmd:
                        has_auto_restart = True
                        break

        print(f"  {svc}: {'✅ auto-restart' if has_auto_restart else '⚠️ 无auto-restart（手动启动）'}")
        if not has_auto_restart:
            issues += 1
    return issues


def check_h_log_duplication():
    """H. 日志重复写入——tee -a + RotatingFileHandler导致每行写两遍"""
    print("【H. 日志重复写入】")
    collector_log = LOG_DIR / "collector.log"
    if not collector_log.exists():
        print("  collector.log不存在")
        return 0

    lines = collector_log.read_text(errors="ignore").strip().split("\n")
    if len(lines) < 10:
        print(f"  日志行数太少({len(lines)})，无法判断")
        return 0

    # 检查最近20行中是否有连续重复行
    recent = lines[-20:]
    dupes = sum(1 for i in range(1, len(recent)) if recent[i] == recent[i-1])
    dupe_rate = dupes / len(recent) * 100
    print(f"  最近20行中连续重复: {dupes}行 ({dupe_rate:.0f}%)")
    if dupe_rate > 50:
        print(f"  ⚠️ 日志重复写入严重（tee -a + RotatingFileHandler双写）")
        return 1
    elif dupe_rate > 10:
        print(f"  ⚠️ 日志有少量重复")
        return 0
    else:
        print(f"  ✅ 日志无重复")
        return 0


def main():
    print("=" * 70)
    print("管道化系统并发安全性专项检查")
    print(f"时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print()

    r = get_redis()

    # 连接DB
    c = ArangoClient(hosts=os.environ.get("ARANGO_HOST", "http://localhost:8529"))
    db = c.db(
        os.environ["ARANGO_DB"],
        username=os.environ.get("ARANGO_USER", "root"),
        password=os.environ.get("ARANGO_PASS", ""),
    )

    issues = []
    issues += [("A", check_a_redis_atomicity(r))]
    print()
    issues_b = check_b_db_redis_consistency(db, r)
    issues.append(("B", issues_b))
    print()
    issues_c = check_c_duplicate_attempt(r)
    issues.append(("C", issues_c))
    print()
    issues_d = check_d_concurrency_limit(r)
    issues.append(("D", issues_d))
    print()
    devin_count = check_e_devin_process_count()
    # devin进程数和并发数对比需要外部传入并发数
    conc_raw = r.get("math:config:concurrency")
    conc = int(conc_raw) if conc_raw else 0
    expected_devin = conc * 2  # 每个并发1个devin cli + 1个node子进程
    zombie_devin = max(0, devin_count - expected_devin - 10)  # 允许10个余量
    if zombie_devin > 0:
        print(f"  僵尸devin进程: ~{zombie_devin}个 (进程{devin_count} - 预期{expected_devin}) ❌")
        issues.append(("E", zombie_devin))
    else:
        print(f"  僵尸devin进程: 0 (进程{devin_count} ≈ 预期{expected_devin}) ✅")
    print()
    issues_f = check_f_rate_balance(r)
    issues.append(("F", issues_f))
    print()
    issues_g = check_g_auto_restart()
    issues.append(("G", issues_g))
    print()
    issues_h = check_h_log_duplication()
    issues.append(("H", issues_h))

    # 总结
    print()
    print("=" * 70)
    real_issues = [(k, v) for k, v in issues if v and v != 0]
    if real_issues:
        print(f"判定: ⚠️ 有 {len(real_issues)} 个并发安全问题:")
        for k, v in real_issues:
            print(f"  - [{k}] {v}")
    else:
        print("判定: ✅ 并发安全性全部通过")
    print("=" * 70)


if __name__ == "__main__":
    main()
