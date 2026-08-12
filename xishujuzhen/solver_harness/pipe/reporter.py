#!/usr/bin/env python3
"""reporter.py — 服务4：统计报告

定时从Redis读统计，输出进度报告和告警。
独立进程，轻量级。

用法:
  python reporter.py --interval 60
"""
import sys
import os
import time
import argparse

sys.path.insert(0, os.path.dirname(__file__))

from redis_queue import (
    get_redis, pending_count, running_count, completed_count, failed_count,
    update_stats, get_stats, ping,
)

LOG_DIR = "/data/math-agent-glm5.2-tmux-agents-trajectory/_pipe/logs"


def main():
    parser = argparse.ArgumentParser(description="Reporter: 统计报告")
    parser.add_argument("--interval", type=int, default=60, help="报告间隔秒数")
    args = parser.parse_args()

    if not ping():
        print("[reporter] ❌ Redis连接失败", flush=True)
        sys.exit(1)
    print(f"[reporter] ✅ Redis连接成功, interval={args.interval}s", flush=True)

    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(LOG_DIR, "reporter.log")

    r = get_redis()
    start_time = time.time()

    while True:
        update_stats(r)
        pending = pending_count(r)
        running = running_count(r)
        completed = completed_count(r)
        failed = failed_count(r)
        total = pending + running + completed + failed

        elapsed = time.time() - start_time
        if completed + failed > 0:
            success_rate = completed / (completed + failed) * 100
        else:
            success_rate = 0

        # 估算完成时间
        done = completed + failed
        if done > 0 and elapsed > 0:
            rate = done / elapsed  # 题/秒
            if rate > 0 and pending > 0:
                eta_seconds = pending / rate
                eta_str = f"{eta_seconds/3600:.1f}h"
            else:
                eta_str = "N/A"
        else:
            eta_str = "N/A"

        report = (
            f"{'='*60}\n"
            f"[reporter] {time.strftime('%H:%M:%S')} (运行 {elapsed/3600:.1f}h)\n"
            f"  pending:   {pending:>8}\n"
            f"  running:   {running:>8}\n"
            f"  completed: {completed:>8}\n"
            f"  failed:    {failed:>8}\n"
            f"  total:     {total:>8}\n"
            f"  success率: {success_rate:.1f}%\n"
            f"  完成速率:  {rate:.2f} 题/秒 ({done}/{int(elapsed)}s)\n"
            f"  ETA:       {eta_str}\n"
            f"{'='*60}"
        )

        print(report, flush=True)

        # 写日志
        with open(log_file, "a") as f:
            f.write(report + "\n")

        # 告警检测
        if running == 0 and pending > 0:
            print(f"[reporter] ⚠️ 告警: running=0 但pending={pending}，Runner可能挂了!", flush=True)
        if failed > 0 and success_rate < 50 and done > 10:
            print(f"[reporter] ⚠️ 告警: 失败率>{100-success_rate:.0f}%，检查连接", flush=True)

        time.sleep(args.interval)


if __name__ == "__main__":
    main()
