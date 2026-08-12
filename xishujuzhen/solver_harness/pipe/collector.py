#!/usr/bin/env python3
"""collector.py — 服务3：状态收集+判定（眼见为实版）

扫描Redis running队列，用"眼见为实"原则检测devin cli终态。

核心改进：
1. 真实thinking检测——检查pane内容是否有thinking标记和数学内容
2. 真实proof验证——PROOF COMPLETE标记+proof内容≥100字符
3. AI放弃检测——检查"I CANNOT SOLVE"/"无法"等放弃标记
4. 失败分类——区分基础设施失败(重试)和模型能力失败(Profile)

用法:
  python collector.py --poll-interval 10 --timeout 1800
  python collector.py --dry-run
"""
import sys
import os
import time
import json
import re
import argparse
import subprocess
import sqlite3
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

TRAJECTORY_BASE = Path("/data/math-agent-glm5.2-tmux-agents-trajectory")

# === 标记模式 ===
PROOF_COMPLETE_MARKER = "PROOF COMPLETE"
ANSWER_LEAK_MARKER = "ANSWER LEAK DETECTED"
AI_GAVE_UP_PATTERNS = [
    "I CANNOT SOLVE", "I cannot solve", "i cannot solve",
    "无法解决", "无法做出", "做不出来",
    "I give up", "i give up", "I'm unable", "无法完成",
    "### I CANNOT SOLVE THIS",
]
RATE_LIMIT_PATTERNS = ["rate limit", "rate_limit", "429", "Too Many Requests"]
TOKEN_LIMIT_PATTERNS = ["token limit", "context limit", "context_length", "maximum context"]
CONNECTION_PATTERNS = ["connection error", "ECONNREFUSED", "ETIMEDOUT", "socket hang up", "fetch failed"]
THINKING_PATTERNS = ["Thinking ·", "Thinking...", "thinking", "⠐", "⠒"]  # devin cli的thinking状态标记

# ANSI转义码清理
ANSI_ESCAPE = re.compile(r'\x1b\[[0-9;]*[a-zA-Z]|\x1b\][^\x07]*\x07|\x1b\[[0-9;]*m|\[\d+m|\[0m|\[K|\[2A|\[2C|\[\?25[a-z]|\[\?2026[a-z]')


def clean_ansi(text: str) -> str:
    """清理ANSI转义码和tmux格式字符"""
    text = ANSI_ESCAPE.sub('', text)
    text = re.sub(r'[\u2800-\u28ff]', '', text)  # braille spinner
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)
    return text


# === 基础设施失败（重试，不计入Profile）===
INFRA_FAILURES = {"failed_connection", "rate_limited", "launch_error", "dead_session"}

# === 模型能力失败（Profile数据，不重试）===
MODEL_FAILURES = {
    "failed_token_limit", "failed_output_limit", "ai_gave_up",
    "failed_thinking_spin", "failed_no_proof", "failed_stall",
    "invalid_tool_use",
}


def tmux_running(session_name: str) -> bool:
    try:
        result = subprocess.run(
            ["tmux", "has-session", "-t", session_name],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False, timeout=5
        )
        return result.returncode == 0
    except Exception:
        return False


def capture_pane(session_name: str, lines: int = 500) -> str:
    try:
        result = subprocess.run(
            ["tmux", "capture-pane", "-t", session_name, "-p", "-S", f"-{lines}"],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout
    except Exception:
        return ""


def pane_is_empty(session_name: str) -> bool:
    text = capture_pane(session_name, 50)
    stripped = "\n".join(l for l in text.split("\n") if l.strip())
    return len(stripped) < 20


def is_thinking(pane_text: str) -> bool:
    """检测AI是否正在thinking——眼见为实"""
    cleaned = clean_ansi(pane_text)
    # 检查devin cli的thinking状态标记
    for pattern in THINKING_PATTERNS:
        if pattern in cleaned:
            return True
    # 检查是否有数学内容（LaTeX符号、推理步骤）
    math_indicators = ["\\frac", "\\sum", "\\int", "\\Rightarrow", "therefore", "hence", "thus", "since",
                       "minimize", "maximize", "constraint", "feasible", "denote", "define", "lemma"]
    math_count = sum(1 for ind in math_indicators if ind in cleaned.lower())
    if math_count >= 2:
        return True
    return False


def has_real_proof(pane_text: str) -> bool:
    """验证是否有真实的proof内容——眼见为实"""
    cleaned = clean_ansi(pane_text)
    if PROOF_COMPLETE_MARKER not in cleaned:
        return False
    # 找到PROOF COMPLETE标记的位置
    idx = cleaned.index(PROOF_COMPLETE_MARKER)
    # 检查标记之前的内容（proof主体）
    proof_body = cleaned[:idx]
    # 去掉空白和题目部分
    lines = [l.strip() for l in proof_body.split("\n") if l.strip()]
    # 过滤掉纯标记行
    content_lines = [l for l in lines if not l.startswith("#") and not l.startswith("###")]
    # proof内容至少100字符
    proof_content = "\n".join(content_lines)
    if len(proof_content) < 100:
        return False
    # 检查是否有数学推理内容
    math_indicators = ["\\frac", "\\sum", "\\int", "\\Rightarrow", "therefore", "hence", "thus",
                       "prove", "proof", "since", "let", "assume", "suppose", "consider", "we have",
                       "minimize", "maximize", "constraint", "feasible", "denote", "define", "lemma"]
    math_count = sum(1 for ind in math_indicators if ind in proof_content.lower())
    return math_count >= 2


def check_ai_gave_up(pane_text: str) -> bool:
    """检测AI是否主动放弃"""
    for pattern in AI_GAVE_UP_PATTERNS:
        if pattern in pane_text:
            return True
    return False


def check_tool_use(exp_id: str) -> bool:
    """检查是否有工具调用——查sessions.db"""
    # trajectory目录
    traj_dir = TRAJECTORY_BASE / exp_id / "sessions_db"
    if not traj_dir.exists():
        return False  # 没有sessions.db，无法检查，假设无工具调用

    # 查找sessions.db文件
    db_files = list(traj_dir.glob("*.db"))
    if not db_files:
        return False

    for db_file in db_files:
        try:
            conn = sqlite3.connect(str(db_file))
            cursor = conn.cursor()
            # 查message_nodes表中是否有tool_call类型
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [r[0] for r in cursor.fetchall()]
            if "message_nodes" in tables:
                cursor.execute("SELECT COUNT(*) FROM message_nodes WHERE type LIKE '%tool%' OR role LIKE '%tool%'")
                count = cursor.fetchone()[0]
                if count > 0:
                    conn.close()
                    return True
            conn.close()
        except Exception:
            continue
    return False


def classify(attempt_meta: dict, pane_text: str, is_running: bool, elapsed: float,
             timeout: int, stall_time: int, last_activity: float) -> tuple[str, dict]:
    """眼见为实的终态判定"""
    problem_key = attempt_meta.get("problem_key", "")
    exp_id = attempt_meta.get("exp_id", "")
    tmux_session = attempt_meta.get("tmux_session", "")

    # 1. 答案泄漏（最高优先级）
    if ANSWER_LEAK_MARKER in pane_text:
        return "answer_leak", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "answer_leak", "elapsed": elapsed}

    # 2. AI主动放弃——模型能力边界
    if check_ai_gave_up(pane_text):
        return "ai_gave_up", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "ai_gave_up", "elapsed": elapsed}

    # 3. 真实PROOF COMPLETE——验证有真实proof内容
    if has_real_proof(pane_text):
        # 检查是否有工具调用
        if check_tool_use(exp_id):
            return "invalid_tool_use", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "invalid_tool_use", "elapsed": elapsed}
        return "candidate_solved", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "candidate_solved", "elapsed": elapsed}

    # 4. 超时——区分thinking spin和真超时
    if elapsed > timeout:
        if is_thinking(pane_text):
            # AI还在thinking但超时了——thinking spin
            return "failed_thinking_spin", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_thinking_spin", "elapsed": elapsed}
        return "failed_timeout", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_timeout", "elapsed": elapsed}

    # 5. tmux session已结束——区分基础设施失败和模型能力失败
    if not is_running:
        # 检查基础设施错误
        for p in RATE_LIMIT_PATTERNS:
            if p.lower() in pane_text.lower():
                return "rate_limited", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "rate_limited", "elapsed": elapsed}
        for p in TOKEN_LIMIT_PATTERNS:
            if p.lower() in pane_text.lower():
                return "failed_token_limit", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_token_limit", "elapsed": elapsed}
        for p in CONNECTION_PATTERNS:
            if p.lower() in pane_text.lower():
                return "failed_connection", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_connection", "elapsed": elapsed}
        # 没有错误标记——AI没做完就结束了
        return "failed_no_proof", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_no_proof", "elapsed": elapsed}

    # 6. 僵尸session（tmux在但pane空白）——基础设施失败
    if tmux_session and tmux_running(tmux_session) and pane_is_empty(tmux_session):
        return "dead_session", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "dead_session", "elapsed": elapsed}

    # 7. stall——区分thinking spin和真stall
    if time.time() - last_activity > stall_time:
        if is_thinking(pane_text):
            return "failed_thinking_spin", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_thinking_spin", "elapsed": elapsed}
        return "failed_stall", {"problem_key": problem_key, "exp_id": exp_id, "verdict": "failed_stall", "elapsed": elapsed}

    # 未结束
    return None, None


def stop_tmux(session_name: str):
    subprocess.run(["tmux", "kill-session", "-t", session_name],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)


def save_pane_snapshot(exp_id: str, session_name: str) -> Path | None:
    """在判定终态前，保存完整的tmux pane内容到文件——眼见为实的物理证据"""
    if not session_name:
        return None
    pane_text = capture_pane(session_name, 2000)  # 抓2000行
    if not pane_text.strip():
        return None
    snapshot_dir = TRAJECTORY_BASE / exp_id / "collector"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    snapshot_file = snapshot_dir / "pane_snapshot.txt"
    snapshot_file.write_text(pane_text, encoding="utf-8")
    # 同时保存清理ANSI后的版本
    cleaned = clean_ansi(pane_text)
    clean_file = snapshot_dir / "pane_snapshot_clean.txt"
    clean_file.write_text(cleaned, encoding="utf-8")
    return snapshot_file


def update_db_status(db, attempt_key: str, status: str, verdict: str, result: dict):
    """更新ArangoDB中attempt和problem的状态"""
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    elapsed = result.get("elapsed", 0)
    try:
        db.collection(ATTEMPT_COLLECTION).update({
            "_key": attempt_key,
            "status": status,
            "verdict": verdict,
            "ended_at": now,
            "runtime_seconds": int(elapsed),
            "end_reason": f"collector判定: {verdict}",
        })
    except Exception:
        pass

    # 更新problem状态
    problem_key = result.get("problem_key")
    if not problem_key:
        try:
            attempt = db.collection(ATTEMPT_COLLECTION).get(attempt_key)
            if attempt:
                problem_key = attempt.get("problem_id")
        except Exception:
            pass

    if problem_key:
        if status == "candidate_solved":
            try:
                db.collection(COLLECTION).update({"_key": problem_key, "extraction_status": "completed"})
            except Exception:
                pass
        elif verdict in INFRA_FAILURES:
            # 基础设施失败——回到pending，可以重试
            try:
                db.collection(COLLECTION).update({"_key": problem_key, "extraction_status": "pending"})
            except Exception:
                pass
        elif verdict in MODEL_FAILURES:
            # 模型能力失败——标记为failed，不重试
            try:
                db.collection(COLLECTION).update({"_key": problem_key, "extraction_status": "failed"})
            except Exception:
                pass


def main():
    parser = argparse.ArgumentParser(description="Collector: 状态收集+判定（眼见为实版）")
    parser.add_argument("--poll-interval", type=int, default=10)
    parser.add_argument("--timeout", type=int, default=1800, help="超时秒数（默认30分钟）")
    parser.add_argument("--stall-time", type=int, default=300, help="stall判定秒数（默认5分钟）")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not ping():
        print("[collector] ❌ Redis连接失败", flush=True)
        sys.exit(1)
    print(f"[collector] ✅ Redis连接成功, poll={args.poll_interval}s, timeout={args.timeout}s", flush=True)
    print(f"[collector] 眼见为实模式: 真实thinking检测+真实proof验证+无工具调用验证", flush=True)

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
        infra_failures_this_round = 0

        for exp_id, meta in running.items():
            if args.dry_run:
                result = {"problem_key": meta.get("problem_key", ""), "exp_id": exp_id, "verdict": "dry_run_complete", "elapsed": 0}
                add_completed(r, result)
                remove_running(r, exp_id)
                completed_this_round += 1
                continue

            tmux_session = meta.get("tmux_session", "")
            start_time = meta.get("start_time", time.time())
            last_activity = meta.get("last_activity", start_time)
            elapsed = time.time() - start_time

            is_running = tmux_running(tmux_session) if tmux_session else False
            pane_text = capture_pane(tmux_session) if is_running else ""

            status, result = classify(
                meta, pane_text, is_running, elapsed,
                args.timeout, args.stall_time, last_activity
            )

            if status is None:
                # 还在运行中——更新last_activity
                meta["last_activity"] = time.time()
                r.hset("math:running", exp_id, json.dumps(meta))
                continue

            # 终态确定
            result["attempt_key"] = meta.get("attempt_key", "")
            result["tmux_session"] = tmux_session

            # 眼见为实：保存完整pane内容作为物理证据
            if is_running and tmux_session:
                snapshot = save_pane_snapshot(exp_id, tmux_session)
                if snapshot:
                    result["pane_snapshot"] = str(snapshot)

            if status == "candidate_solved":
                add_completed(r, result)
                completed_this_round += 1
                print(f"[collector] ✅ SOLVED {meta.get('problem_key', '')} ({elapsed:.0f}s)", flush=True)
            elif status == "answer_leak":
                add_completed(r, result)
                completed_this_round += 1
                print(f"[collector] ⚠️ ANSWER LEAK {meta.get('problem_key', '')}", flush=True)
            elif status in INFRA_FAILURES:
                add_failed(r, result)
                infra_failures_this_round += 1
                print(f"[collector] 🔧 INFRA {status} {meta.get('problem_key', '')} ({elapsed:.0f}s) → 可重试", flush=True)
            else:
                add_failed(r, result)
                failed_this_round += 1
                print(f"[collector] ❌ MODEL {status} {meta.get('problem_key', '')} ({elapsed:.0f}s) → Profile数据", flush=True)

            # 停tmux
            if tmux_session:
                stop_tmux(tmux_session)

            remove_running(r, exp_id)

            # 更新DB
            attempt_key = meta.get("attempt_key", "")
            if attempt_key:
                update_db_status(db, attempt_key, status, result.get("verdict", ""), result)

        update_stats(r)
        print(f"[collector] 本轮: solved={completed_this_round}, infra={infra_failures_this_round}, model_fail={failed_this_round}", flush=True)

        time.sleep(args.poll_interval)


if __name__ == "__main__":
    main()
