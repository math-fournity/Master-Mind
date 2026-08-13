#!/usr/bin/env python3
"""pipe_control.py — 管道化系统控制工具

启动/停止/状态查询4个服务。

用法:
  python pipe_control.py start --concurrency 30
  python pipe_control.py start --concurrency 3 --dry-run  # dry-run模式
  python pipe_control.py stop
  python pipe_control.py status
  python pipe_control.py health  # 并发+网络+tmux泄漏检查
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


def stop_service(name: str, graceful: bool = True, timeout: int = 10):
    """停止一个服务

    graceful=True: 发送SIGTERM让服务优雅退出（不kill harness session）
    graceful=False: 直接kill-session（强制停止）
    """
    session_name = f"pipe-{name}"
    if not tmux_running(session_name):
        print(f"  [{name}] 未运行")
        return

    if graceful:
        # 优雅退出：通过tmux发送SIGTERM给session中的进程
        # tmux send-keys C-c 会发送Ctrl-C（SIGINT），但更可靠的方式是用kill-pane
        # 实际上tmux session中的主进程是python，用send-keys发送C-c最可靠
        subprocess.run(["tmux", "send-keys", "-t", session_name, "C-c", ""],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        print(f"  [{name}] 发送SIGINT, 等待优雅退出...")

        # 等待服务退出
        for i in range(timeout):
            time.sleep(1)
            if not tmux_running(session_name):
                print(f"  [{name}] 已优雅退出 (等待{i+1}s)")
                return

        # 超时后强制kill
        print(f"  [{name}] 优雅退出超时({timeout}s), 强制停止")
        subprocess.run(["tmux", "kill-session", "-t", session_name],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        print(f"  [{name}] 已强制停止")
    else:
        subprocess.run(["tmux", "kill-session", "-t", session_name],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        print(f"  [{name}] 已强制停止")


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
        stop_service(name, graceful=not args.force, timeout=args.timeout)

    if not args.keep_harness:
        # 默认不kill harness session——它们独立运行，Collector重启后会继续处理
        # 只有明确指定--kill-harness时才kill
        pass

    if args.kill_harness:
        # kill所有harness-xxx session
        result = subprocess.run(["tmux", "list-sessions", "-F", "#{session_name}"],
                                capture_output=True, text=True, check=False)
        harness_sessions = [s.strip() for s in result.stdout.strip().split("\n")
                           if s.strip().startswith("harness-")]
        if harness_sessions:
            print(f"\n  发现{len(harness_sessions)}个harness session:")
            for s in harness_sessions:
                subprocess.run(["tmux", "kill-session", "-t", s],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
                print(f"    killed: {s}")
        else:
            print(f"\n  无harness session")

    print("\n所有服务已停止。")
    if not args.kill_harness:
        print("  注意: harness-xxx session仍在独立运行（这是正常的——解耦设计）。")
        print("  Collector重启后会继续处理running队列中的attempt。")
        print("  如需停止所有harness session: python pipe_control.py stop --kill-harness")


def cmd_concurrency(args):
    """实时调整并发数——Runner下次poll时生效（通常2-5秒内）"""
    r = get_redis()
    old = r.get("math:config:concurrency")
    old_val = int(old) if old else "?"
    r.set("math:config:concurrency", args.value)
    print(f"并发数: {old_val} → {args.value}")
    print(f"Runner会在下次poll时自动读取新值（通常2-5秒内生效）")
    print(f"当前running不会受影响——只影响后续新启动的题")
    # 如果runner没在运行，提示
    if not tmux_running("pipe-runner"):
        print(f"⚠️ Runner未运行，新值会在Runner启动时生效")


def cmd_poll_interval(args):
    """实时调整poll间隔"""
    r = get_redis()
    old = r.get("math:config:poll_interval")
    old_val = int(old) if old else "?"
    r.set("math:config:poll_interval", args.value)
    print(f"poll间隔: {old_val}s → {args.value}s")
    print(f"Runner会在下次poll时自动读取新值")


def cmd_recover(args):
    """断电恢复"""
    # 直接调用recover_from_crash.py
    cmd = [sys.executable, os.path.join(os.path.dirname(__file__), "recover_from_crash.py")]
    if args.dry_run:
        cmd.append("--dry-run")
    if args.auto_restart:
        cmd.append("--auto-restart")
    subprocess.run(cmd)


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

    # 实时配置
    conc = r.get("math:config:concurrency")
    poll = r.get("math:config:poll_interval")
    conc_str = conc.decode() if isinstance(conc, bytes) else (conc if conc else "?")
    poll_str = poll.decode() if isinstance(poll, bytes) else (poll if poll else "?")
    print(f"\n  实时配置:")
    print(f"    concurrency:   {conc_str}")
    print(f"    poll_interval: {poll_str}s")
    print(f"    (修改: python pipe_control.py concurrency 50)")

    if running > 0 and args.verbose:
        print(f"\n  Running attempts:")
        all_running = get_all_running(r)
        for exp_id, meta in list(all_running.items())[:10]:
            elapsed = time.time() - meta.get("start_time", time.time())
            print(f"    {exp_id[:20]}  {meta.get('problem_key', '')[:30]}  {elapsed:.0f}s")
        if len(all_running) > 10:
            print(f"    ... 还有 {len(all_running) - 10} 个")


def cmd_health(args):
    """检查并发量、网络连接稳定性、tmux session泄漏——一键健康检查"""
    import json

    print("系统健康检查:")
    print()

    if not ping():
        print("  ❌ Redis连接失败")
        return
    r = get_redis()

    # 1. 并发量
    conc_raw = r.get("math:config:concurrency")
    conc = int(conc_raw.decode() if isinstance(conc_raw, bytes) else conc_raw) if conc_raw else 0
    running = r.hgetall("math:running")
    running_count = len(running)

    # tmux session统计
    result = subprocess.run(["tmux", "list-sessions"], capture_output=True, text=True)
    harness_p = 0
    harness_dbmon = 0
    tmux_dbmon_exp_ids = set()
    for line in result.stdout.split("\n"):
        if "harness-dbmon-p" in line:
            harness_dbmon += 1
            tmux_dbmon_exp_ids.add(line.split("harness-dbmon-")[1].split(":")[0])
        elif "harness-p" in line:
            harness_p += 1

    running_exp_ids = set()
    for k, v in running.items():
        data = json.loads(v)
        running_exp_ids.add(data.get("exp_id", ""))

    leaked_dbmon = tmux_dbmon_exp_ids - running_exp_ids

    print(f"  并发量:")
    print(f"    设定:          {conc}")
    print(f"    Redis running: {running_count}")
    print(f"    harness-p:     {harness_p}")
    print(f"    harness-dbmon: {harness_dbmon}")
    if leaked_dbmon:
        print(f"    ⚠️  dbmon泄漏:  {len(leaked_dbmon)}个")
    else:
        print(f"    dbmon泄漏:     0 ✅")
    print()

    # 2. 网络连接——检查所有running session的pane
    network_errors = []
    truncated = 0
    thinking = 0
    other = 0
    error_patterns = [
        "connection error", "econnrefused", "econnreset", "socket hang up",
        "fetch failed", "network error", "network request failed",
        "429", "rate limit", "too many requests", "etimedout",
    ]

    for k, v in running.items():
        data = json.loads(v)
        eid = data.get("exp_id", "")
        tmux_sess = f"harness-{eid}"
        res = subprocess.run(["tmux", "capture-pane", "-t", tmux_sess, "-p", "-S", "-200"],
                             capture_output=True, text=True)
        pane = res.stdout
        pane_lower = pane.lower()
        found_err = False
        for p in error_patterns:
            if p in pane_lower:
                network_errors.append((data.get("problem_key", ""), eid, p))
                found_err = True
                break
        if found_err:
            continue
        if "Response truncated" in pane or "Send a message to continue" in pane:
            truncated += 1
        elif "Thinking" in pane:
            thinking += 1
        else:
            other += 1

    print(f"  网络连接:")
    print(f"    网络错误:      {len(network_errors)}/{running_count}", "❌" if network_errors else "✅")
    print(f"    Response truncated: {truncated}")
    print(f"    Thinking中:   {thinking}")
    print(f"    其他状态:     {other}")
    if network_errors:
        print(f"    错误详情:")
        for pk, eid, p in network_errors:
            print(f"      {pk} {eid}: \"{p}\"")
    print()

    # 3. failed队列网络相关
    failed = r.lrange("math:failed", 0, -1)
    from collections import Counter
    verdicts = Counter()
    conn_failures = 0
    for item in failed:
        data = json.loads(item)
        v = data.get("verdict", "?")
        verdicts[v] += 1
        if v in ("failed_connection", "rate_limited"):
            conn_failures += 1

    print(f"  failed队列:")
    print(f"    总计:         {len(failed)}")
    print(f"    网络相关:     {conn_failures}", "❌" if conn_failures else "✅")
    for v, c in verdicts.most_common():
        print(f"    {v}: {c}")
    print()

    # 4. 整体判定
    issues = []
    if leaked_dbmon:
        issues.append(f"dbmon泄漏{len(leaked_dbmon)}个")
    if network_errors:
        issues.append(f"网络错误{len(network_errors)}个")
    if conn_failures:
        issues.append(f"failed队列网络相关{conn_failures}个")
    if truncated:
        issues.append(f"Response truncated {truncated}个")

    if issues:
        print(f"  判定: ⚠️ 有问题需要关注: {', '.join(issues)}")
    else:
        print(f"  判定: ✅ 健康")


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
    p_stop.add_argument("--force", action="store_true", help="强制停止（不等待优雅退出）")
    p_stop.add_argument("--timeout", type=int, default=10, help="优雅退出等待超时秒数")
    p_stop.add_argument("--kill-harness", action="store_true", help="同时kill所有harness-xxx session（默认不kill）")
    p_stop.add_argument("--keep-harness", action="store_true", help="保留harness session（默认行为，这里仅为显式声明）")
    p_stop.set_defaults(func=cmd_stop)

    p_recover = sub.add_parser("recover", help="断电恢复+僵尸清理")
    p_recover.add_argument("--dry-run", action="store_true", help="只检查不修改")
    p_recover.add_argument("--auto-restart", action="store_true", help="恢复后自动重启服务")
    p_recover.set_defaults(func=cmd_recover)

    p_status = sub.add_parser("status", help="查看状态")
    p_status.add_argument("-v", "--verbose", action="store_true")
    p_status.set_defaults(func=cmd_status)

    p_health = sub.add_parser("health", help="并发+网络+tmux泄漏一键检查")
    p_health.set_defaults(func=cmd_health)

    p_clear = sub.add_parser("clear", help="清空Redis队列")
    p_clear.set_defaults(func=cmd_clear)

    p_conc = sub.add_parser("concurrency", help="实时调整并发数")
    p_conc.add_argument("value", type=int, help="新的并发数（如50）")
    p_conc.set_defaults(func=cmd_concurrency)

    p_poll = sub.add_parser("poll-interval", help="实时调整poll间隔")
    p_poll.add_argument("value", type=int, help="新的poll间隔秒数")
    p_poll.set_defaults(func=cmd_poll_interval)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
