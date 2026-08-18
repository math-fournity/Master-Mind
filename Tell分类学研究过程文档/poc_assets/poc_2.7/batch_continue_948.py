#!/usr/bin/env python3
"""
POC-2.7 批量续传脚本
====================
对948道被Pipe 1判定为DIRECTION_ERROR的题启动续传机制。

这些题的原始run全部是failed_token_limit——thinking spin被截断。
续传机制把截断的reasoning_content作为新prompt注入，让AI继续思考。

数据来源：
- ArangoDB analysis_results（d1=DIRECTION_ERROR的948题）
- ArangoDB devin_problem_runs（原始做题的export路径）
- /data/math-agent-glm5.2-tmux-agents-dir/{exp_id}/AGENTS.md（题目文本）
- /data/math-agent-glm5.2-tmux-agents-trajectory/{exp_id}/exports/conversation.json（原始export）

用法：
    # 导出题目列表
    python3 batch_continue_948.py export-list

    # 批量续传（并发5）
    python3 batch_continue_948.py batch --concurrency 5 --max-rounds 5

    # 批量续传（指定题目前缀，如只跑aime_前缀的题）
    python3 batch_continue_948.py batch --filter-prefix aime_ --concurrency 5

    # 检查进度
    python3 batch_continue_948.py status

    # 单题续传（从原始export开始）
    python3 batch_continue_948.py single --problem-id aime_2024_0014
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# === 路径常量 ===
SCRIPT_DIR = Path(__file__).resolve().parent
POC_2_7_DIR = SCRIPT_DIR / "poc_2.7"
POC_2_7_DIR.mkdir(parents=True, exist_ok=True)

WORK_DIR = POC_2_7_DIR / "workdirs"
TRAJ_DIR = POC_2_7_DIR / "trajectories"
WORK_DIR.mkdir(parents=True, exist_ok=True)
TRAJ_DIR.mkdir(parents=True, exist_ok=True)

LIST_FILE = POC_2_7_DIR / "problem_list.json"
RESULTS_FILE = POC_2_7_DIR / "results.json"

# D盘路径
D_SOLVER_DIR = Path("/data/math-agent-glm5.2-tmux-agents-dir")
D_TRAJ_DIR = Path("/data/math-agent-glm5.2-tmux-agents-trajectory")

# === 截断判定 ===
TRUNC_COMP_TOKENS_MIN = 24000


# =============================================================================
# §1 从ArangoDB导出题目列表
# =============================================================================

def export_problem_list():
    """从ArangoDB导出948道DIRECTION_ERROR题的列表。"""
    from arango import ArangoClient

    client = ArangoClient(hosts="http://localhost:8529")
    db = client.db("xishujuzhen_math_glm52", username="root", password="REDACTED-DB-PASSWORD")

    # 获取DIRECTION_ERROR的problem_id
    col = db.collection("analysis_results")
    direction_error_pids = set()
    for doc in col.find({}):
        if doc.get("dimension1_verdict") == "DIRECTION_ERROR":
            direction_error_pids.add(doc.get("problem_id", ""))

    print(f"DIRECTION_ERROR去重题数: {len(direction_error_pids)}")

    # 获取每道题的export路径和题目文件路径
    runs_col = db.collection("devin_problem_runs")
    problems = []
    seen = set()

    for doc in runs_col.find({}):
        pid = doc.get("problem_id", "")
        if pid not in direction_error_pids or pid in seen:
            continue
        if doc.get("status") != "failed_token_limit":
            continue

        exp_id = doc.get("exp_id", "")
        paths = doc.get("paths", {})

        # export路径
        export_path = paths.get("export_path", "")
        if not export_path and exp_id:
            export_path = str(D_TRAJ_DIR / exp_id / "exports" / "conversation.json")

        # 题目文件路径
        problem_path = paths.get("problem_path", "")
        if not problem_path and exp_id:
            problem_path = str(D_SOLVER_DIR / exp_id / "problem.txt")

        # AGENTS.md路径（题目可能在AGENTS.md中）
        agents_md_path = str(D_SOLVER_DIR / exp_id / "AGENTS.md") if exp_id else ""

        # 验证export存在
        export_exists = os.path.exists(export_path) if export_path else False

        if not export_exists:
            continue

        seen.add(pid)
        problems.append({
            "problem_id": pid,
            "exp_id": exp_id,
            "seed_export": export_path,
            "problem_path": problem_path,
            "agents_md_path": agents_md_path,
            "export_exists": export_exists,
        })

    print(f"有export的题: {len(problems)}")

    with open(LIST_FILE, "w") as f:
        json.dump(problems, f, ensure_ascii=False, indent=2)
    print(f"已保存到 {LIST_FILE}")
    return problems


def load_problem_list():
    """加载题目列表。"""
    if not LIST_FILE.exists():
        print(f"题目列表不存在，请先运行 export-list")
        return []
    with open(LIST_FILE) as f:
        return json.load(f)


# =============================================================================
# §2 题目文本提取
# =============================================================================

def extract_problem_text(problem_entry):
    """从problem.txt或AGENTS.md中提取题目文本。"""
    # 方法1: problem.txt
    problem_path = problem_entry.get("problem_path", "")
    if problem_path and os.path.exists(problem_path):
        with open(problem_path) as f:
            text = f.read().strip()
        if text:
            return text

    # 方法2: AGENTS.md中的## Problem部分
    agents_md_path = problem_entry.get("agents_md_path", "")
    if agents_md_path and os.path.exists(agents_md_path):
        with open(agents_md_path) as f:
            content = f.read()
        # 提取 ## Problem 后的内容
        m = re.search(r"## Problem\s*(.*?)(?:### PROOF COMPLETE|$)", content, re.DOTALL)
        if m:
            return m.group(1).strip()

    # 方法3: 从export的system message中找AGENTS.md内容
    export_path = problem_entry.get("seed_export", "")
    if export_path and os.path.exists(export_path):
        with open(export_path) as f:
            d = json.load(f)
        for s in d.get("steps", []):
            if s.get("source") == "system":
                msg = s.get("message", "") or ""
                # 找 ## Problem 部分
                m = re.search(r"## Problem\s*(.*?)(?:### PROOF COMPLETE|$)", msg, re.DOTALL)
                if m:
                    return m.group(1).strip()

    return None


# =============================================================================
# §3 截断检测与reasoning提取
# =============================================================================

def is_truncated(export_path):
    """检测export是否被截断。"""
    with open(export_path) as f:
        d = json.load(f)
    steps = [s for s in d.get("steps", []) if s.get("source") == "agent"]
    if not steps:
        return False, "no agent step"
    last = steps[-1]
    rc = len(last.get("reasoning_content", "") or "")
    msg = len(last.get("message", "") or "")
    tc = len(last.get("tool_calls", []) or [])
    comp = (last.get("metrics", {}) or {}).get("completion_tokens", 0)
    if rc > 1000 and msg == 0 and tc == 0 and comp >= TRUNC_COMP_TOKENS_MIN:
        return True, f"rc={rc}c, msg=0, tc=0, comp={comp}"
    if msg > 0 or tc > 0:
        return False, f"completed: rc={rc}c, msg={msg}c, tc={tc}, comp={comp}"
    return False, f"unknown: rc={rc}c, msg={msg}c, tc={tc}, comp={comp}"


def is_completed(export_path):
    """检测export是否已完成。"""
    with open(export_path) as f:
        d = json.load(f)
    steps = [s for s in d.get("steps", []) if s.get("source") == "agent"]
    if not steps:
        return False, "no agent step"
    last = steps[-1]
    msg = len(last.get("message", "") or "")
    tc = len(last.get("tool_calls", []) or [])
    if msg > 0 or tc > 0:
        return True, f"msg={msg}c, tc={tc}"
    return False, "no working output"


def extract_reasoning(export_path):
    """从export提取所有agent step的reasoning_content。"""
    with open(export_path) as f:
        d = json.load(f)
    parts = []
    for s in d.get("steps", []):
        if s.get("source") == "agent":
            rc = str(s.get("reasoning_content", "") or "")
            if rc:
                parts.append(rc)
    return "\n\n".join(parts)


# =============================================================================
# §4 续传prompt构造
# =============================================================================

CONTINUE_PROMPT_TEMPLATE = """{original_problem}

=== 你之前的思考过程（Round {prev_round}，被截断）===

你已经在上一轮中开始了这道题的思考，但因为输出长度限制，思考过程被截断了。
以下是你之前的完整思考过程，请仔细阅读，在此基础上**继续**思考并完成解答（不要从头开始）：

{previous_reasoning}

=== 请继续思考并完成解答 ===

你之前的思考在上方被截断了。请从截断处继续，完成这道题的解答。

要求：
1. **在之前的思考基础上继续**，不要重复已经做过的分析
2. 给出完整的解答过程
3. 最终答案用 \\boxed{{答案}} 格式给出
4. 数学公式用LaTeX
5. 把证明写到proof.md文件中，不要在对话里输出完整证明
"""

INITIAL_PROMPT_TEMPLATE = """{original_problem}

请解答上面的数学题。

要求：
1. 给出完整的解答过程
2. 最终答案用 \\boxed{{答案}} 格式给出
3. 数学公式用LaTeX
4. 把证明写到proof.md文件中，不要在对话里输出完整证明
"""


def build_continue_prompt(original_problem, previous_reasoning, prev_round):
    return CONTINUE_PROMPT_TEMPLATE.format(
        original_problem=original_problem,
        previous_reasoning=previous_reasoning,
        prev_round=prev_round,
    )


# =============================================================================
# §5 单题续传
# =============================================================================

def solve_single(problem_entry, max_rounds=5, model="glm-5-2", verbose=True):
    """
    对一道题运行多轮续传。

    problem_entry: {problem_id, exp_id, seed_export, problem_path, agents_md_path}
    """
    pid = problem_entry["problem_id"]
    run_name = f"p27-{pid}"
    work_dir = WORK_DIR / run_name
    traj_dir = TRAJ_DIR / run_name
    work_dir.mkdir(parents=True, exist_ok=True)
    traj_dir.mkdir(parents=True, exist_ok=True)

    # 提取题目文本
    problem_text = extract_problem_text(problem_entry)
    if not problem_text:
        return {"problem_id": pid, "final_status": "NO_PROBLEM_TEXT",
                "rounds": [], "final_export": None}

    # Round 1: 复用原始export
    seed_export = problem_entry["seed_export"]
    round1_export = traj_dir / "round1" / "exports" / "conversation.json"
    round1_export.parent.mkdir(parents=True, exist_ok=True)

    if not round1_export.exists():
        import shutil
        shutil.copy(seed_export, round1_export)

    truncated, reason = is_truncated(str(round1_export))
    completed, comp_reason = is_completed(str(round1_export))
    rc = extract_reasoning(str(round1_export))

    rounds_log = [{"round": 1, "export": str(round1_export),
                    "truncated": truncated, "reason": reason, "rc_chars": len(rc)}]

    if verbose:
        print(f"[{pid}] R1: truncated={truncated}, completed={completed}, {reason}")

    if completed and not truncated:
        return {"problem_id": pid, "rounds": rounds_log,
                "final_status": "COMPLETED", "final_export": str(round1_export)}

    all_reasoning = [rc]

    # Round 2..N
    for round_num in range(2, max_rounds + 1):
        if not truncated:
            break

        prev_reasoning = "\n\n".join(all_reasoning)
        prompt_text = build_continue_prompt(problem_text, prev_reasoning, round_num - 1)
        prompt_file = work_dir / f"round{round_num}_prompt.txt"
        prompt_file.write_text(prompt_text)

        export_path = traj_dir / f"round{round_num}" / "exports" / "conversation.json"
        export_path.parent.mkdir(parents=True, exist_ok=True)

        tmux_session = f"p27-{pid}-r{round_num}"
        if verbose:
            rc_total = sum(len(p) for p in all_reasoning)
            print(f"[{pid}] R{round_num}: 续传（累积reasoning: {rc_total}c）...")

        # 启动devin
        cmd = [
            "devin", "-p",
            "--prompt-file", str(prompt_file),
            "--model", model,
            "--respect-workspace-trust", "false",
            "--permission-mode", "dangerous",
            "--export", str(export_path),
        ]
        subprocess.run(
            ["tmux", "kill-session", "-t", tmux_session],
            capture_output=True, timeout=5,
        )
        tmux_cmd = " ".join(cmd)
        subprocess.run(
            ["tmux", "new-session", "-d", "-s", tmux_session,
             f"cd {work_dir} && {tmux_cmd}"],
            capture_output=True, timeout=10,
        )

        # 等待完成
        while True:
            result = subprocess.run(
                ["tmux", "has-session", "-t", tmux_session],
                capture_output=True, timeout=5,
            )
            if result.returncode != 0:
                break
            time.sleep(15)

        if not export_path.exists():
            rounds_log.append({"round": round_num, "export": None,
                               "truncated": False, "reason": "no export"})
            break

        truncated, reason = is_truncated(str(export_path))
        completed, comp_reason = is_completed(str(export_path))
        rc = extract_reasoning(str(export_path))
        all_reasoning.append(rc)
        rounds_log.append({"round": round_num, "export": str(export_path),
                           "truncated": truncated, "reason": reason,
                           "rc_chars": len(rc), "completed": completed})

        if verbose:
            print(f"[{pid}] R{round_num}: truncated={truncated}, completed={completed}, {reason}")

        if completed:
            return {"problem_id": pid, "rounds": rounds_log,
                    "final_status": "COMPLETED", "final_export": str(export_path)}

    return {"problem_id": pid, "rounds": rounds_log,
            "final_status": "TRUNCATED_AT_MAX",
            "final_export": rounds_log[-1].get("export")}


# =============================================================================
# §6 并发批量续传
# =============================================================================

def run_batch(problems, max_rounds=5, concurrency=5, model="glm-5-2"):
    """并发批量续传。"""
    results = {}
    # 加载已有结果（支持断点续传）
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE) as f:
            results = json.load(f)

    # 过滤已完成的题
    todo = [p for p in problems
            if p["problem_id"] not in results
            or results[p["problem_id"]]["final_status"] not in ("COMPLETED",)]
    done = len(problems) - len(todo)

    print(f"\n{'='*70}")
    print(f"POC-2.7 批量续传: {len(problems)}题, 已完成{done}, 待运行{len(todo)}")
    print(f"并发={concurrency}, max_rounds={max_rounds}")
    print(f"{'='*70}\n")

    # 使用ThreadPoolExecutor并发
    # 但tmux session是全局的，需要确保session名不冲突
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {}
        for p in todo:
            future = executor.submit(solve_single, p, max_rounds, model, verbose=True)
            futures[future] = p["problem_id"]

        for future in as_completed(futures):
            pid = futures[future]
            try:
                result = future.result()
                results[pid] = result
                print(f"\n=> {pid}: {result['final_status']}\n")

                # 实时保存结果
                with open(RESULTS_FILE, "w") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"\n=> {pid}: ERROR {e}\n")
                results[pid] = {"problem_id": pid,
                                "final_status": "ERROR", "error": str(e),
                                "rounds": [], "final_export": None}
                with open(RESULTS_FILE, "w") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)

    # 汇总
    completed = sum(1 for r in results.values() if r["final_status"] == "COMPLETED")
    truncated = sum(1 for r in results.values() if r["final_status"] == "TRUNCATED_AT_MAX")
    errors = sum(1 for r in results.values() if r["final_status"] in ("ERROR", "NO_PROBLEM_TEXT"))

    print(f"\n{'='*70}")
    print(f"汇总: COMPLETED={completed}, TRUNCATED_AT_MAX={truncated}, ERROR={errors}")
    print(f"总计: {len(results)}/{len(problems)}")
    print(f"{'='*70}")

    return results


# =============================================================================
# §7 状态检查
# =============================================================================

def check_status():
    """检查续传进度。"""
    problems = load_problem_list()
    if not problems:
        print("无题目列表")
        return

    results = {}
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE) as f:
            results = json.load(f)

    completed = sum(1 for r in results.values() if r["final_status"] == "COMPLETED")
    truncated = sum(1 for r in results.values() if r["final_status"] == "TRUNCATED_AT_MAX")
    errors = sum(1 for r in results.values() if r["final_status"] in ("ERROR", "NO_PROBLEM_TEXT"))
    pending = len(problems) - len(results)

    print(f"\nPOC-2.7 续传进度:")
    print(f"  总题数: {len(problems)}")
    print(f"  COMPLETED: {completed}")
    print(f"  TRUNCATED_AT_MAX: {truncated}")
    print(f"  ERROR: {errors}")
    print(f"  PENDING: {pending}")
    print(f"  进度: {len(results)}/{len(problems)} ({len(results)*100//len(problems)}%)")

    # 检查proof.md
    proof_count = 0
    for p in problems:
        pid = p["problem_id"]
        proof_path = WORK_DIR / f"p27-{pid}" / "proof.md"
        if proof_path.exists():
            proof_count += 1
    print(f"  proof.md存在: {proof_count}")

    # 运行中的tmux session
    result = subprocess.run(["tmux", "list-sessions"], capture_output=True, text=True)
    p27_sessions = [l for l in result.stdout.splitlines() if "p27-" in l]
    print(f"  运行中的p27 tmux session: {len(p27_sessions)}")
    for s in p27_sessions[:5]:
        print(f"    {s}")
    if len(p27_sessions) > 5:
        print(f"    ... (共{len(p27_sessions)}个)")


# =============================================================================
# §8 CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="POC-2.7 批量续传948道DIRECTION_ERROR题")
    sub = parser.add_subparsers(dest="command")

    # export-list
    sub.add_parser("export-list", help="从ArangoDB导出题目列表")

    # batch
    p_batch = sub.add_parser("batch", help="批量续传")
    p_batch.add_argument("--concurrency", type=int, default=5)
    p_batch.add_argument("--max-rounds", type=int, default=5)
    p_batch.add_argument("--model", default="glm-5-2")
    p_batch.add_argument("--filter-prefix", default=None,
                         help="只跑problem_id以指定前缀开头的题")
    p_batch.add_argument("--limit", type=int, default=None,
                         help="只跑前N道题（测试用）")

    # single
    p_single = sub.add_parser("single", help="单题续传")
    p_single.add_argument("--problem-id", required=True)
    p_single.add_argument("--max-rounds", type=int, default=5)
    p_single.add_argument("--model", default="glm-5-2")

    # status
    sub.add_parser("status", help="检查进度")

    args = parser.parse_args()

    if args.command == "export-list":
        export_problem_list()

    elif args.command == "batch":
        problems = load_problem_list()
        if args.filter_prefix:
            problems = [p for p in problems if p["problem_id"].startswith(args.filter_prefix)]
        if args.limit:
            problems = problems[:args.limit]
        run_batch(problems, max_rounds=args.max_rounds,
                  concurrency=args.concurrency, model=args.model)

    elif args.command == "single":
        problems = load_problem_list()
        entry = next((p for p in problems if p["problem_id"] == args.problem_id), None)
        if not entry:
            print(f"未找到: {args.problem_id}")
            sys.exit(1)
        result = solve_single(entry, max_rounds=args.max_rounds, model=args.model)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif args.command == "status":
        check_status()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
