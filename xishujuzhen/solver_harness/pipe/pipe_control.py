#!/usr/bin/env python3
"""pipe_control.py — 管道化系统控制工具

启动/停止/状态查询4个服务。

用法:
  python pipe_control.py start --concurrency 30
  python pipe_control.py start --concurrency 3 --dry-run  # dry-run模式
  python pipe_control.py stop
  python pipe_control.py status
  python pipe_control.py clear  # 清空Redis队列
"""
import sys
import os
import time
import argparse
import subprocess
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))

from redis_queue import (
    get_redis, pending_count, running_count, completed_count, failed_count,
    get_all_running, clear_all, ping, update_stats,
)

PIPE_DIR = Path(__file__).parent
VENV_PYTHON = Path(__file__).parent.parent.parent.parent / ".venv" / "bin" / "python3"

SESSIONS = {
    "feeder": {"script": "feeder.py", "args": []},
    "runner": {"script": "runner.py", "args": ["--concurrency"]},
    "collector": {"script": "collector.py", "args": []},
    "reporter": {"script": "reporter.py", "args": []},
}

LOG_DIR = "/data/math-agent-glm5.2-tmux-agents-trajectory/_pipe/logs"


def tmux_running(name: str) -> bool:
    try:
        r = subprocess.run(
            ["tmux", "has-session", "-t", name],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False, timeout=5
        )
        return r.returncode == 0
    except Exception:
        return False


def start_service(name: str, script: str, extra_args: list[str], dry_run: bool = False):
    """启动一个服务到tmux session"""
    session_name = f"pipe-{name}"
    if tmux_running(session_name):
        print(f"  [{name}] 已在运行, 跳过")
        return

    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(LOG_DIR, f"{name}.log")

    cmd = [str(VENV_PYTHON), str(PIPE_DIR / script)] + extra_args
    if dry_run:
        cmd.append("--dry-run")

    full_cmd = " ".join(cmd) + f" 2>&1 | tee -a {log_file}"
    subprocess.run(
        ["tmux", "new-session", "-d", "-s", session_name, full_cmd],
        check=False, timeout=10
    )
    print(f"  [{name}] 启动 → tmux:{session_name}")


def stop_service(name: str):
    """停止一个服务"""
    session_name = f"pipe-{name}"
    if tmux_running(session_name):
        subprocess.run(["tmux", "kill-session", "-t", session_name],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        print(f"  [{name}] 已停止")
    else:
        print(f"  [{name}] 未运行")


def cmd_start(args):
    print("启动管道化系统:")
    if not ping():
        print("  ❌ Redis连接失败，请先启动Redis容器")
        sys.exit(1)
    print("  ✅ Redis连接正常")

    runner_args = ["--concurrency", str(args.concurrency)]
    feeder_args = ["--tier", args.tier, "--batch-size", str(args.batch_size),
                   "--low-water-mark", str(args.low_water_mark)]
    collector_args = ["--poll-interval", str(args.collector_poll), "--timeout", str(args.timeout)]
    reporter_args = ["--interval", str(args.report_interval)]

    if args.clear:
        r = get_redis()
        clear_all(r)
        print("  已清空Redis队列")

    start_service("feeder", "feeder.py", feeder_args, dry_run=args.dry_run)
    time.sleep(2)
    start_service("runner", "runner.py", runner_args, dry_run=args.dry_run)
    time.sleep(1)
    start_service("collector", "collector.py", collector_args, dry_run=args.dry_run)
    time.sleep(1)
    start_service("reporter", "reporter.py", reporter_args, dry_run=args.dry_run)

    print("\n所有服务已启动。用 'python pipe_control.py status' 查看状态。")


def cmd_stop(args):
    print("停止管道化系统:")
    for name in ["feeder", "runner", "collector", "reporter"]:
        stop_service(name)
    print("所有服务已停止。")


def cmd_status(args):
    print("管道化系统状态:")
    print()

    # tmux session状态
    for name in ["feeder", "runner", "collector", "reporter"]:
        session_name = f"pipe-{name}"
        running = tmux_running(session_name)
        status = "✅ 运行中" if running else "❌ 未运行"
        print(f"  {name:12s} {status}")

    print()

    # Redis队列状态
    if not ping():
        print("  ❌ Redis连接失败")
        return

    r = get_redis()
    update_stats(r)
    pending = pending_count(r)
    running = running_count(r)
    completed = completed_count(r)
    failed = failed_count(r)
    total = pending + running + completed + failed

    print(f"  Redis队列:")
    print(f"    pending:   {pending:>8}")
    print(f"    running:   {running:>8}")
    print(f"    completed: {completed:>8}")
    print(f"    failed:    {failed:>8}")
    print(f"    total:     {total:>8}")

    if running > 0 and args.verbose:
        print(f"\n  Running attempts:")
        all_running = get_all_running(r)
        for exp_id, meta in list(all_running.items())[:10]:
            elapsed = time.time() - meta.get("start_time", time.time())
            print(f"    {exp_id[:20]}  {meta.get('problem_key', '')[:30]}  {elapsed:.0f}s")
        if len(all_running) > 10:
            print(f"    ... 还有 {len(all_running) - 10} 个")


def cmd_clear(args):
    print("清空Redis队列:")
    if not ping():
        print("  ❌ Redis连接失败")
        return
    r = get_redis()
    clear_all(r)
    print("  ✅ 已清空所有队列")


def main():
    parser = argparse.ArgumentParser(description="管道化系统控制工具")
    sub = parser.add_subparsers(dest="command")

    p_start = sub.add_parser("start", help="启动所有服务")
    p_start.add_argument("--concurrency", type=int, default=30)
    p_start.add_argument("--tier", type=str, default="1,2,3")
    p_start.add_argument("--batch-size", type=int, default=100)
    p_start.add_argument("--low-water-mark", type=int, default=50)
    p_start.add_argument("--collector-poll", type=int, default=10)
    p_start.add_argument("--timeout", type=int, default=1800)
    p_start.add_argument("--report-interval", type=int, default=60)
    p_start.add_argument("--clear", action="store_true", help="启动前清空Redis队列")
    p_start.add_argument("--dry-run", action="store_true", help="dry-run模式")
    p_start.set_defaults(func=cmd_start)

    p_stop = sub.add_parser("stop", help="停止所有服务")
    p_stop.set_defaults(func=cmd_stop)

    p_status = sub.add_parser("status", help="查看状态")
    p_status.add_argument("-v", "--verbose", action="store_true")
    p_status.set_defaults(func=cmd_status)

    p_clear = sub.add_parser("clear", help="清空Redis队列")
    p_clear.set_defaults(func=cmd_clear)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
