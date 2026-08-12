#!/usr/bin/env python3
"""runner.py — 服务2：纯启动

从Redis pending队列取题，启动devin cli，不做任何状态判定。
独立进程，维持固定并发数。

用法:
  python runner.py --concurrency 30
  python runner.py --concurrency 3 --dry-run  # dry-run：不启动devin cli
"""
import sys
import os
import time
import json
import uuid
import argparse
import subprocess
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.dirname(__file__))

from redis_queue import (
    get_redis, dequeue_pending, add_running, get_all_running, running_count, update_stats, ping,
)
from arango import ArangoClient

DB_HOST = "http://localhost:8529"
DB_NAME = "xishujuzhen_math_glm52"
DB_USER = "root"
DB_PASS = "REDACTED-DB-PASSWORD"
COLLECTION = "problem_extraction_progress"
ATTEMPT_COLLECTION = "devin_problem_runs"

TRAJECTORY_BASE = Path("/data/math-agent-glm5.2-tmux-agents-trajectory")
PIPE_DIR = TRAJECTORY_BASE / "_pipe"
PROBLEMS_DIR = PIPE_DIR / "problems"

# solver_harness.py的路径
HARNESS_SCRIPT = Path(__file__).parent.parent / "solver_harness.py"
VENV_PYTHON = Path(__file__).parent.parent.parent.parent / ".venv" / "bin" / "python3"


def load_problem_text(db, problem_key: str) -> str:
    """从ArangoDB读取题目文本"""
    doc = db.collection(COLLECTION).get(problem_key)
    if not doc:
        return ""
    return doc.get("problem_text", "")


def write_problem_file(problem_key: str, problem_text: str, exp_id: str) -> Path:
    """写题目文件到problems目录"""
    problem_dir = PROBLEMS_DIR / exp_id
    problem_dir.mkdir(parents=True, exist_ok=True)
    problem_file = problem_dir / "AGENTS.md"
    # 写入题目+解题指令
    content = f"""# Problem

{problem_text}

## Instructions

Solve this problem step by step. When you have completed your proof, output:

```
### PROOF COMPLETE
```

If you detect that the problem statement contains the answer or solution (answer leak), output:

```
### ANSWER LEAK DETECTED
```
"""
    problem_file.write_text(content, encoding="utf-8")
    return problem_file


def launch_devin_cli(exp_id: str, problem_file: Path, model: str = "glm-5.2-high") -> str:
    """启动devin cli——直接调用solver_harness.py launch（它自己创建harness-xxx tmux session）
    返回solver_harness创建的tmux session名（harness-{exp_id}）
    """
    cmd = [
        str(VENV_PYTHON), str(HARNESS_SCRIPT),
        "launch",
        "--exp-id", exp_id,
        "--problem-file", str(problem_file),
        "--model", model,
        "--no-mitm",
        "--interactive",
    ]

    log_file = PROBLEMS_DIR / exp_id / "launch.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # 直接运行solver_harness.py launch（它是同步的，会创建harness-xxx tmux session）
    with open(log_file, "w") as f:
        result = subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, timeout=60)

    # solver_harness创建的session名是 harness-{exp_id}
    tmux_session = f"harness-{exp_id}"
    return tmux_session


def create_attempt_record(db, problem_key: str, exp_id: str, tmux_session: str) -> str:
    """在ArangoDB中创建attempt记录"""
    attempt_key = f"pipe_{exp_id[:40]}"
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    doc = {
        "_key": attempt_key,
        "batch_id": "pipe-runner",
        "problem_id": problem_key,
        "exp_id": exp_id,
        "tmux_session": tmux_session,
        "status": "running",
        "started_at": now,
        "model": "glm-5.2-high",
    }
    try:
        db.collection(ATTEMPT_COLLECTION).insert(doc)
    except Exception as e:
        # 已存在则更新
        db.collection(ATTEMPT_COLLECTION).update({"_key": attempt_key, "status": "running", "started_at": now})
    return attempt_key


def main():
    parser = argparse.ArgumentParser(description="Runner: 纯启动服务")
    parser.add_argument("--concurrency", type=int, default=30, help="并发数")
    parser.add_argument("--poll-interval", type=int, default=5, help="检查间隔秒数")
    parser.add_argument("--model", type=str, default="glm-5.2-high", help="模型名")
    parser.add_argument("--dry-run", action="store_true", help="dry-run：不启动devin cli")
    args = parser.parse_args()

    if not ping():
        print("[runner] ❌ Redis连接失败", flush=True)
        sys.exit(1)
    print(f"[runner] ✅ Redis连接成功, concurrency={args.concurrency}", flush=True)

    client = ArangoClient(hosts=DB_HOST, request_timeout=300)
    db = client.db(DB_NAME, username=DB_USER, password=DB_PASS)
    print(f"[runner] ✅ ArangoDB连接成功", flush=True)

    r = get_redis()
    total_launched = 0

    while True:
        # 统计当前running数
        current_running = running_count(r)
        slots = args.concurrency - current_running

        if slots <= 0:
            print(f"[runner] running={current_running}, 满载, 等待...", flush=True)
            time.sleep(args.poll_interval)
            continue

        # 从Redis取题
        items = dequeue_pending(r, slots)
        if not items:
            print(f"[runner] pending空, 等待feeder补充...", flush=True)
            time.sleep(args.poll_interval)
            continue

        for problem_key, priority in items:
            exp_id = f"p{uuid.uuid4().hex[:20]}"

            if args.dry_run:
                # dry-run：不启动devin cli，直接模拟running
                metadata = {
                    "problem_key": problem_key,
                    "exp_id": exp_id,
                    "tmux_session": f"dry-{exp_id[:20]}",
                    "start_time": time.time(),
                    "priority": priority,
                    "dry_run": True,
                }
                add_running(r, exp_id, metadata)
                total_launched += 1
                print(f"[runner] DRY-RUN 启动 {problem_key} (exp={exp_id[:20]})", flush=True)
                continue

            # 真实模式：读取题目文本
            problem_text = load_problem_text(db, problem_key)
            if not problem_text.strip():
                print(f"[runner] ⚠️ 题目文本为空: {problem_key}, 跳过", flush=True)
                from redis_queue import add_failed
                add_failed(r, {"problem_key": problem_key, "error": "empty_problem_text", "exp_id": exp_id, "verdict": "empty_problem_text"})
                continue

            # 答案泄漏检查：检查题目文本是否因清洗疏忽包含了答案
            doc = db.collection(COLLECTION).get(problem_key)
            answer = doc.get("answer", "") if doc else ""
            solution = doc.get("solution_text", "") if doc else ""
            leak_found = False
            if answer and len(str(answer).strip()) > 3:
                ans_clean = str(answer).strip().replace(" ", "").replace("\\", "").replace("$", "").lower()
                text_clean = problem_text.lower().replace(" ", "").replace("\\", "").replace("$", "")
                if ans_clean in text_clean:
                    leak_found = True
                    print(f"[runner] ⚠️ 答案泄漏: {problem_key} 题目文本包含answer字段值", flush=True)
            if not leak_found and solution and len(solution.strip()) > 20:
                sol_prefix = solution.strip()[:100].lower()
                if sol_prefix in problem_text.lower():
                    leak_found = True
                    print(f"[runner] ⚠️ 答案泄漏: {problem_key} 题目文本包含solution片段", flush=True)
            if leak_found:
                from redis_queue import add_failed
                add_failed(r, {
                    "problem_key": problem_key, "exp_id": exp_id,
                    "verdict": "answer_leak_in_input",
                    "error": "题目文本包含答案/solution，不入running",
                })
                # 更新DB
                attempt_key = f"pipe_{exp_id[:40]}"
                now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                try:
                    db.collection(ATTEMPT_COLLECTION).insert({
                        "_key": attempt_key, "batch_id": "pipe-runner",
                        "problem_id": problem_key, "exp_id": exp_id,
                        "status": "answer_leak_in_input", "verdict": "answer_leak_in_input",
                        "started_at": now, "ended_at": now,
                        "end_reason": "题目文本包含答案/solution",
                    })
                except Exception:
                    pass
                continue

            # 写题目文件
            problem_file = write_problem_file(problem_key, problem_text, exp_id)

            # 启动devin cli
            try:
                tmux_session = launch_devin_cli(exp_id, problem_file, args.model)
            except Exception as e:
                print(f"[runner] ❌ 启动失败 {problem_key}: {e}", flush=True)
                from redis_queue import add_failed
                add_failed(r, {"problem_key": problem_key, "error": str(e), "exp_id": exp_id})
                continue

            # 创建attempt记录
            attempt_key = create_attempt_record(db, problem_key, exp_id, tmux_session)

            # 写入Redis running队列
            metadata = {
                "problem_key": problem_key,
                "exp_id": exp_id,
                "attempt_key": attempt_key,
                "tmux_session": tmux_session,
                "start_time": time.time(),
                "priority": priority,
            }
            add_running(r, exp_id, metadata)
            total_launched += 1
            print(f"[runner] 启动 {problem_key} → tmux={tmux_session} (total={total_launched})", flush=True)

            # 启动间隔
            time.sleep(1)

        update_stats(r)

    # 不会到达这里


if __name__ == "__main__":
    main()
