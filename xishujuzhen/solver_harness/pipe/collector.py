#!/usr/bin/env python3
"""collector.py — 服务3：状态收集+判定

扫描Redis running队列，检测devin cli终态，更新Redis和ArangoDB。
独立进程，定期轮询所有running attempt。

用法:
  python collector.py --poll-interval 10 --timeout 1800
  python collector.py --dry-run  # dry-run：直接把running标记为completed
"""
import sys
import os
import time
import json
import argparse
import subprocess
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.dirname(__file__))

from redis_queue import (
    get_redis, get_all_running, remove_running, add_completed, add_failed,
    update_stats, ping,
)
from arango import ArangoClient

DB_HOST = "http://localhost:8529"
DB_NAME = "xishujuzhen_math_glm52"
DB_USER = "root"
DB_PASS = "REDACTED-DB-PASSWORD"
ATTEMPT_COLLECTION = "devin_problem_runs"
COLLECTION = "problem_extraction_progress"

# 终态标记模式
PROOF_COMPLETE_MARKER = "PROOF COMPLETE"
ANSWER_LEAK_MARKER = "ANSWER LEAK DETECTED"
RATE_LIMIT_PATTERNS = ["rate limit", "rate_limit", "429", "Too Many Requests"]
TOKEN_LIMIT_PATTERNS = ["token limit", "context limit", "context_length"]
CONNECTION_PATTERNS = ["connection error", "ECONNREFUSED", "ETIMEDOUT", "socket hang up"]


def tmux_running(session_name: str) -> bool:
    """检查tmux session是否还在"""
    try:
        result = subprocess.run(
            ["tmux", "has-session", "-t", session_name],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False, timeout=5
        )
        return result.returncode == 0
    except Exception:
        return False


def capture_pane(session_name: str, lines: int = 500) -> str:
    """抓取tmux pane内容"""
    try:
        result = subprocess.run(
            ["tmux", "capture-pane", "-t", session_name, "-p", "-S", f"-{lines}"],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout
    except Exception:
        return ""


def pane_is_empty(session_name: str) -> bool:
    """检查pane是否空白（Devin CLI已退出）"""
    text = capture_pane(session_name, 50)
    # 去掉空白行后如果几乎没内容，认为是空pane
    stripped = "\n".join(l for l in text.split("\n") if l.strip())
    return len(stripped) < 20


def classify(attempt_meta: dict, pane_text: str, is_running: bool, elapsed: float,
             timeout: int, stall_time: int, last_activity: float) -> tuple[str, dict]:
    """判定终态，返回 (status, result_dict)"""
    problem_key = attempt_meta.get("problem_key", "")
    exp_id = attempt_meta.get("exp_id", "")
    tmux_session = attempt_meta.get("tmux_session", "")

    # 1. 答案泄漏
    if ANSWER_LEAK_MARKER in pane_text:
        return "answer_leak", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "answer_leak", "elapsed": elapsed}

    # 2. PROOF COMPLETE
    if PROOF_COMPLETE_MARKER in pane_text:
        return "candidate_solved", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "candidate_solved", "elapsed": elapsed}

    # 3. 超时
    if elapsed > timeout:
        return "failed_timeout", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_timeout", "elapsed": elapsed}

    # 4. tmux session已结束
    if not is_running:
        # 检查是否有错误标记
        for p in RATE_LIMIT_PATTERNS:
            if p.lower() in pane_text.lower():
                return "rate_limited", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "rate_limited", "elapsed": elapsed}
        for p in TOKEN_LIMIT_PATTERNS:
            if p.lower() in pane_text.lower():
                return "failed_token_limit", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_token_limit", "elapsed": elapsed}
        for p in CONNECTION_PATTERNS:
            if p.lower() in pane_text.lower():
                return "failed_connection", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_connection", "elapsed": elapsed}
        return "failed_no_proof", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_no_proof", "elapsed": elapsed}

    # 5. 僵尸session（tmux在但pane空）
    if tmux_running and pane_is_empty(tmux_session):
        return "dead_session", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "dead_session", "elapsed": elapsed}

    # 6. stall（长时间无活动）
    if time.time() - last_activity > stall_time:
        return "failed_stall", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_stall", "elapsed": elapsed}

    # 未结束，返回None
    return None, None


def stop_tmux(session_name: str):
    """kill tmux session"""
    subprocess.run(["tmux", "kill-session", "-t", session_name],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)


def update_db_status(db, attempt_key: str, status: str, verdict: str):
    """更新ArangoDB中attempt和problem的状态"""
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    try:
        db.collection(ATTEMPT_COLLECTION).update({
            "_key": attempt_key,
            "status": status,
            "verdict": verdict,
            "ended_at": now,
        })
    except Exception:
        pass

    # 如果solved，更新problem_extraction_progress
    problem_key = None
    try:
        attempt = db.collection(ATTEMPT_COLLECTION).get(attempt_key)
        if attempt:
            problem_key = attempt.get("problem_id")
    except Exception:
        pass

    if problem_key and status == "candidate_solved":
        try:
            db.collection(COLLECTION).update({
                "_key": problem_key,
                "extraction_status": "completed",
            })
        except Exception:
            pass
    elif problem_key and status.startswith("failed"):
        try:
            db.collection(COLLECTION).update({
                "_key": problem_key,
                "extraction_status": "pending",  # 失败的题回到pending，可以重试
            })
        except Exception:
            pass


def main():
    parser = argparse.ArgumentParser(description="Collector: 状态收集+判定")
    parser.add_argument("--poll-interval", type=int, default=10, help="扫描间隔秒数")
    parser.add_argument("--timeout", type=int, default=1800, help="超时秒数（默认30分钟）")
    parser.add_argument("--stall-time", type=int, default=300, help="stall判定秒数（默认5分钟）")
    parser.add_argument("--dry-run", action="store_true", help="dry-run：直接标记完成")
    args = parser.parse_args()

    if not ping():
        print("[collector] ❌ Redis连接失败", flush=True)
        sys.exit(1)
    print(f"[collector] ✅ Redis连接成功, poll={args.poll_interval}s, timeout={args.timeout}s", flush=True)

    client = ArangoClient(hosts=DB_HOST, request_timeout=300)
    db = client.db(DB_NAME, username=DB_USER, password=DB_PASS)
    print(f"[collector] ✅ ArangoDB连接成功", flush=True)

    r = get_redis()

    while True:
        running = get_all_running(r)
        if not running:
            print(f"[collector] 无running attempt, 等待...", flush=True)
            time.sleep(args.poll_interval)
            continue

        print(f"[collector] 扫描 {len(running)} 个running attempt", flush=True)
        completed_this_round = 0
        failed_this_round = 0

        for exp_id, meta in running.items():
            if args.dry_run:
                # dry-run：直接标记为completed
                result = {"problem_key": meta.get("problem_key", ""), "exp_id": exp_id, "verdict": "dry_run_complete", "elapsed": 0}
                add_completed(r, result)
                remove_running(r, exp_id)
                completed_this_round += 1
                print(f"[collector] DRY-RUN 完成 {exp_id[:20]}", flush=True)
                continue

            tmux_session = meta.get("tmux_session", "")
            start_time = meta.get("start_time", time.time())
            last_activity = meta.get("last_activity", start_time)
            elapsed = time.time() - start_time

            # 检查tmux session
            is_running = tmux_running(tmux_session) if tmux_session else False

            # 抓取pane内容
            pane_text = capture_pane(tmux_session) if is_running else ""

            # 判定终态
            status, result = classify(
                meta, pane_text, is_running, elapsed,
                args.timeout, args.stall_time, last_activity
            )

            if status is None:
                # 还在运行中，更新last_activity
                meta["last_activity"] = time.time()
                r.hset("math:running", exp_id, json.dumps(meta))
                continue

            # 终态确定
            result["attempt_key"] = meta.get("attempt_key", "")
            result["tmux_session"] = tmux_session

            if status == "candidate_solved":
                add_completed(r, result)
                completed_this_round += 1
                print(f"[collector] ✅ SOLVED {meta.get('problem_key', '')} ({elapsed:.0f}s)", flush=True)
            elif status == "answer_leak":
                add_completed(r, result)
                completed_this_round += 1
                print(f"[collector] ⚠️ ANSWER LEAK {meta.get('problem_key', '')}", flush=True)
            else:
                add_failed(r, result)
                failed_this_round += 1
                print(f"[collector] ❌ {status} {meta.get('problem_key', '')} ({elapsed:.0f}s)", flush=True)

            # 停tmux session
            if tmux_session:
                stop_tmux(tmux_session)

            # 从running移除
            remove_running(r, exp_id)

            # 更新ArangoDB
            attempt_key = meta.get("attempt_key", "")
            if attempt_key:
                update_db_status(db, attempt_key, status, result.get("verdict", ""))

        update_stats(r)
        print(f"[collector] 本轮: completed={completed_this_round}, failed={failed_this_round}", flush=True)

        time.sleep(args.poll_interval)


if __name__ == "__main__":
    main()
