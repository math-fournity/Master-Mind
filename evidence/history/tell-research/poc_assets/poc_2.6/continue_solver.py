#!/usr/bin/env python3
"""
POC-2.6 续传机制验证脚本
========================
解决 glm-5-2 单次 API 调用 completion_tokens=25000 上限导致 thinking spin 被截断的问题。

机制：把 AI 之前完成的 reasoning_content（thinking）作为新 prompt 的上下文注入，
让 AI 在新的 API 调用中继续思考。每轮 25000 completion_tokens 推进一部分，多轮累积完成。

用法：
    # 单题测试（CC-101-bare，最多3轮）
    python3 continue_solver.py single --problem CC-101_bare --max-rounds 3

    # 从已有的 round1 export 开始续传（跳过 round1 重新运行）
    python3 continue_solver.py single --problem CC-101_bare --max-rounds 3 \
        --seed-export /path/to/round1/conversation.json

    # 批量运行（16个run）
    python3 continue_solver.py batch --max-rounds 5

设计依据：399号 POC-2.6 方案 §2
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

# === 路径常量 ===
SCRIPT_DIR = Path(__file__).resolve().parent
POC_2_6_DIR = SCRIPT_DIR                      # .../poc_assets/poc_2.6/
POC_ASSETS_DIR = POC_2_6_DIR.parent            # .../poc_assets/
POC_2_5_ROUND1_DIR = POC_ASSETS_DIR / "poc_2.5_round1"
PROBLEMS_DIR = POC_2_5_ROUND1_DIR / "problems"  # 16个problem文件

# POC-2.6 的工作根目录
POC_2_6_WORK_DIR = POC_2_6_DIR / "workdirs"
POC_2_6_TRAJ_DIR = POC_2_6_DIR / "trajectories"

# === 截断判定阈值 ===
TRUNC_RC_MIN_CHARS = 1000        # reasoning_content 至少这么多字符才算"有thinking"
TRUNC_COMP_TOKENS_MIN = 24000    # completion_tokens 接近 25000 上限才算被截断


# =============================================================================
# §1 截断检测
# =============================================================================

def load_agent_steps(export_path):
    """从 conversation.json 加载 agent steps。"""
    with open(export_path) as f:
        data = json.load(f)
    return [s for s in data.get("steps", []) if s.get("source") == "agent"], data


def get_last_agent_step(export_path):
    """返回最后一个 agent step（或 None）。"""
    agent_steps, _ = load_agent_steps(export_path)
    if not agent_steps:
        return None
    return agent_steps[-1]


def is_truncated(export_path):
    """
    检测 export 是否被 completion_tokens 截断。

    截断判定（399号 §2.2）：
    - 有 thinking（reasoning_content > 1000 字符）
    - 没有 working 产出（message=0 且 tool_calls=0）
    - completion_tokens 接近 25000 上限（>= 24000）
    """
    step = get_last_agent_step(export_path)
    if step is None:
        return False, "no agent step"

    rc = str(step.get("reasoning_content", "") or "")
    msg = str(step.get("message", "") or "")
    tc = step.get("tool_calls", []) or []
    metrics = step.get("metrics", {}) or {}
    comp_tokens = metrics.get("completion_tokens", 0)

    has_thinking = len(rc) > TRUNC_RC_MIN_CHARS
    has_working = len(msg) > 0 or len(tc) > 0
    near_limit = comp_tokens >= TRUNC_COMP_TOKENS_MIN

    truncated = has_thinking and (not has_working) and near_limit
    reason = (
        f"rc={len(rc)}c, msg={len(msg)}c, tc={len(tc)}, "
        f"comp_tokens={comp_tokens}, near_limit={near_limit}, "
        f"has_working={has_working}"
    )
    return truncated, reason


def is_completed(export_path):
    """
    检测 export 是否完成（有 working 产出）。

    完成判定：
    - 有 message（最终答案）或
    - 有 tool_calls（工具调用，进入 working 阶段）
    """
    step = get_last_agent_step(export_path)
    if step is None:
        return False, "no agent step"

    rc = str(step.get("reasoning_content", "") or "")
    msg = str(step.get("message", "") or "")
    tc = step.get("tool_calls", []) or []

    has_working = len(msg) > 0 or len(tc) > 0
    reason = f"rc={len(rc)}c, msg={len(msg)}c, tc={len(tc)}"
    return has_working, reason


def extract_reasoning(export_path):
    """从 export 提取最后一个 agent step 的 reasoning_content。"""
    step = get_last_agent_step(export_path)
    if step is None:
        return ""
    return str(step.get("reasoning_content", "") or "")


def extract_all_reasoning(export_path):
    """从 export 提取所有 agent step 的 reasoning_content（拼接）。"""
    agent_steps, _ = load_agent_steps(export_path)
    parts = []
    for s in agent_steps:
        rc = str(s.get("reasoning_content", "") or "")
        if rc:
            parts.append(rc)
    return "\n\n".join(parts)


# =============================================================================
# §2 续传 prompt 构造
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


def build_continue_prompt(original_problem_text, previous_reasoning, prev_round):
    """
    构造续传 prompt（399号 §2.3）。

    参数：
    - original_problem_text: 原始 problem 文件的完整内容
    - previous_reasoning: 上一轮的 reasoning_content（thinking）
    - prev_round: 上一轮的轮次号（用于 prompt 中标注）
    """
    return CONTINUE_PROMPT_TEMPLATE.format(
        original_problem=original_problem_text,
        previous_reasoning=previous_reasoning,
        prev_round=prev_round,
    )


# =============================================================================
# §3 进程管理——基于 cwd 的 devin 进程识别
# =============================================================================
#
# 设计原则（用户确认 2026-08-18）：
#   - 不设超时限制，让 devin 自然运行到完成
#   - 需要 kill 时，跟用户确认后通过 cwd 精确识别并杀掉
#   - 每个 run 在独有的 work_dir 中启动，cwd 就是进程身份标识
#
# 识别方法：
#   lsof -p <pid> | grep cwd  →  进程的工作目录
#   我们的进程 cwd 都在 POC_2_6_WORK_DIR 下（如 .../poc_2.6/workdirs/p26-CC-101_bare）
#   别的系统的进程 cwd 在别处（如 /data/math-agent-glm5.2-tmux-agents-dir/...）
#   两者不会混淆

def find_devin_processes(work_dir_prefix=None):
    """
    查找属于本脚本启动的 devin -p 进程。

    参数：
    - work_dir_prefix: 如果提供，只返回 cwd 匹配该前缀的进程；
                      如果 None，返回所有 cwd 在 POC_2_6_WORK_DIR 下的进程

    返回：[{pid, cwd, elapsed, cmd}, ...]
    """
    if work_dir_prefix is None:
        work_dir_prefix = str(POC_2_6_WORK_DIR)

    # 找所有 devin -p 进程（排除 acp 子进程和 grep 自身）
    result = subprocess.run(
        ["ps", "aux"], capture_output=True, text=True, timeout=10,
    )
    processes = []
    for line in result.stdout.splitlines():
        if "devin -p" not in line:
            continue
        if "grep" in line:
            continue
        if "/devin acp" in line:
            continue
        parts = line.split(None, 10)
        if len(parts) < 11:
            continue
        pid = int(parts[1])
        cmd = parts[10]

        # 用 lsof 查 cwd
        try:
            lsof_result = subprocess.run(
                ["lsof", "-p", str(pid)],
                capture_output=True, text=True, timeout=5,
            )
            cwd = None
            for lsof_line in lsof_result.stdout.splitlines():
                if "cwd" in lsof_line:
                    cwd_fields = lsof_line.split()
                    cwd = cwd_fields[-1] if cwd_fields else None
                    break
        except Exception:
            cwd = None

        if cwd and cwd.startswith(work_dir_prefix):
            # 查 elapsed time
            try:
                etime_result = subprocess.run(
                    ["ps", "-p", str(pid), "-o", "etime="],
                    capture_output=True, text=True, timeout=5,
                )
                elapsed = etime_result.stdout.strip()
            except Exception:
                elapsed = "?"
            processes.append({
                "pid": pid, "cwd": cwd,
                "elapsed": elapsed, "cmd": cmd[:120],
            })

    return processes


def kill_devin_process(pid, signal="TERM"):
    """杀掉指定 PID 的 devin 进程。先 TERM，必要时 KILL。"""
    import signal as sig_module
    sig = sig_module.SIGTERM if signal == "TERM" else sig_module.SIGKILL
    try:
        os.kill(pid, sig)
        print(f"  已发送 {signal} 到 PID={pid}")
        return True
    except ProcessLookupError:
        print(f"  PID={pid} 已不存在")
        return False
    except PermissionError:
        print(f"  无权限杀 PID={pid}")
        return False


def kill_processes_in_workdir(work_dir, signal="TERM"):
    """杀掉所有 cwd 在指定 work_dir 下的 devin 进程。"""
    procs = find_devin_processes(work_dir_prefix=str(work_dir))
    if not procs:
        print(f"  没有找到 cwd 在 {work_dir} 下的 devin 进程")
        return 0
    killed = 0
    for p in procs:
        print(f"  杀掉 PID={p['pid']} (cwd={p['cwd']}, elapsed={p['elapsed']})")
        if kill_devin_process(p["pid"], signal):
            killed += 1
    return killed


# =============================================================================
# §3.5 运行单轮 devin（无超时，自然等待完成）
# =============================================================================

def run_devin_round(prompt_file, export_path, work_dir, model="glm-5-2",
                    tmux_session=None, poll_interval=15):
    """
    运行一轮 devin -p（无超时限制）。

    用 tmux 提供 PTY（避免 "Scrollback error: io error"）。
    数据采集靠 --export 的 conversation.json，不靠 tmux。

    无超时：devin 会自然运行到完成（输出 message 后自动退出）。
    如果需要中断，用 kill 命令（基于 cwd 识别进程），或跟用户确认后手动 kill。

    返回：export_path 是否生成。
    """
    work_dir.mkdir(parents=True, exist_ok=True)
    export_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "devin", "-p",
        "--prompt-file", str(prompt_file),
        "--model", model,
        "--respect-workspace-trust", "false",
        "--permission-mode", "dangerous",
        "--export", str(export_path),
    ]

    if tmux_session:
        # 用 tmux 提供 PTY
        # 先杀掉同名 session（如果存在）
        subprocess.run(
            ["tmux", "kill-session", "-t", tmux_session],
            capture_output=True, timeout=5,
        )
        # 启动新 session 运行命令
        tmux_cmd = " ".join(cmd)
        subprocess.run(
            ["tmux", "new-session", "-d", "-s", tmux_session,
             f"cd {work_dir} && {tmux_cmd}"],
            capture_output=True, timeout=10,
        )
        # 等待完成（轮询 tmux session 结束，无超时）
        while True:
            result = subprocess.run(
                ["tmux", "has-session", "-t", tmux_session],
                capture_output=True, timeout=5,
            )
            if result.returncode != 0:
                # session 结束了，devin 已退出
                break
            time.sleep(poll_interval)
    else:
        # 直接前台运行
        subprocess.run(
            cmd, cwd=str(work_dir),
            capture_output=True, text=True,
        )

    return export_path.exists()


# =============================================================================
# §4 多轮续传循环
# =============================================================================

def solve_with_continuation(problem_name, max_rounds=5, model="glm-5-2",
                             seed_export=None, verbose=True):
    """
    对一道题运行多轮续传，直到完成或达到最大轮次。

    参数：
    - problem_name: problem 文件名（不含 .txt），如 "CC-101_bare"
    - max_rounds: 最大轮次
    - model: 模型名
    - seed_export: 如果提供，跳过 round 1 的运行，从这个 export 开始续传
                   （用于复用 POC-2.5 已有的 round1 数据）

    返回 dict：
    {
        "problem": problem_name,
        "rounds": [{"round": 1, "export": ..., "truncated": True, "reason": ...}, ...],
        "final_status": "COMPLETED" | "TRUNCATED_AT_MAX" | "NO_EXPORT",
        "final_export": path or None,
    }
    """
    problem_file = PROBLEMS_DIR / f"{problem_name}.txt"
    if not problem_file.exists():
        print(f"[ERROR] problem file not found: {problem_file}")
        return {"problem": problem_name, "final_status": "ERROR",
                "error": f"problem file not found: {problem_file}"}

    original_problem_text = problem_file.read_text()

    # 准备工作目录和 trajectory 目录
    run_name = f"p26-{problem_name}"
    work_dir = POC_2_6_WORK_DIR / run_name
    traj_dir = POC_2_6_TRAJ_DIR / run_name
    work_dir.mkdir(parents=True, exist_ok=True)
    traj_dir.mkdir(parents=True, exist_ok=True)

    rounds_log = []
    all_reasoning_parts = []  # 累积所有轮次的 reasoning

    # ---------- Round 1 ----------
    if seed_export and Path(seed_export).exists():
        # 复用已有的 round1 export（来自 POC-2.5）
        round1_export = traj_dir / "round1" / "exports" / "conversation.json"
        round1_export.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(seed_export, round1_export)
        if verbose:
            print(f"[Round 1] 复用 seed export: {seed_export}")
        export_path = round1_export
    else:
        # 运行 round 1
        round1_prompt = work_dir / "round1_prompt.txt"
        round1_prompt.write_text(original_problem_text)
        export_path = traj_dir / "round1" / "exports" / "conversation.json"
        if verbose:
            print(f"[Round 1] 运行 devin -p ...")
        tmux_session = f"p26-{problem_name}-r1"
        ok = run_devin_round(
            round1_prompt, export_path, work_dir,
            model=model, tmux_session=tmux_session,
        )
        if not ok:
            if verbose:
                print(f"[Round 1] 失败：未生成 export")
            rounds_log.append({"round": 1, "export": None,
                               "truncated": False, "reason": "no export generated"})
            return {"problem": problem_name, "rounds": rounds_log,
                    "final_status": "NO_EXPORT", "final_export": None}

    # 检测 round 1
    truncated, reason = is_truncated(export_path)
    completed, comp_reason = is_completed(export_path)
    if verbose:
        print(f"[Round 1] truncated={truncated}, completed={completed}, {reason}")

    rc = extract_reasoning(export_path)
    all_reasoning_parts.append(rc)
    rounds_log.append({
        "round": 1, "export": str(export_path),
        "truncated": truncated, "reason": reason,
        "rc_chars": len(rc),
    })

    if completed and not truncated:
        if verbose:
            print(f"[Round 1] 已完成（有 working 产出）")
        return {"problem": problem_name, "rounds": rounds_log,
                "final_status": "COMPLETED", "final_export": str(export_path)}

    # ---------- Round 2..N（续传） ----------
    for round_num in range(2, max_rounds + 1):
        if not truncated:
            # 上一轮没被截断但也没完成？可能是其他错误
            if verbose:
                print(f"[Round {round_num}] 上一轮未截断但也未完成，停止")
            break

        # 构造续传 prompt
        # 累积所有前序轮次的 reasoning
        previous_reasoning = "\n\n".join(all_reasoning_parts)
        continue_prompt_text = build_continue_prompt(
            original_problem_text, previous_reasoning, prev_round=round_num - 1,
        )
        prompt_file = work_dir / f"round{round_num}_prompt.txt"
        prompt_file.write_text(continue_prompt_text)

        if verbose:
            rc_total = sum(len(p) for p in all_reasoning_parts)
            print(f"[Round {round_num}] 续传运行（累积 reasoning: {rc_total} chars）...")

        export_path = traj_dir / f"round{round_num}" / "exports" / "conversation.json"
        tmux_session = f"p26-{problem_name}-r{round_num}"
        ok = run_devin_round(
            prompt_file, export_path, work_dir,
            model=model, tmux_session=tmux_session,
        )

        if not ok:
            if verbose:
                print(f"[Round {round_num}] 失败：未生成 export")
            rounds_log.append({"round": round_num, "export": None,
                               "truncated": False, "reason": "no export generated"})
            break

        # 检测
        truncated, reason = is_truncated(export_path)
        completed, comp_reason = is_completed(export_path)
        rc = extract_reasoning(export_path)
        all_reasoning_parts.append(rc)
        rounds_log.append({
            "round": round_num, "export": str(export_path),
            "truncated": truncated, "reason": reason,
            "rc_chars": len(rc),
            "completed": completed,
        })
        if verbose:
            print(f"[Round {round_num}] truncated={truncated}, "
                  f"completed={completed}, {reason}")

        if completed:
            if verbose:
                print(f"[Round {round_num}] 已完成（有 working 产出）")
            return {"problem": problem_name, "rounds": rounds_log,
                    "final_status": "COMPLETED",
                    "final_export": str(export_path)}

    # 达到最大轮次仍未完成
    final_export = rounds_log[-1].get("export") if rounds_log else None
    return {"problem": problem_name, "rounds": rounds_log,
            "final_status": "TRUNCATED_AT_MAX", "final_export": final_export}


# =============================================================================
# §5 批量运行
# =============================================================================

ALL_PROBLEMS = [
    "CC-101_bare", "CC-101_vein", "CC-101_vein_hint", "CC-101_hint",
    "CC-103_bare", "CC-103_vein", "CC-103_vein_hint", "CC-103_hint",
    "CC-104_bare", "CC-104_vein", "CC-104_vein_hint", "CC-104_hint",
    "CC-105_bare", "CC-105_vein", "CC-105_vein_hint", "CC-105_hint",
]

# POC-2.5 round1 的 export 路径映射（用于 seed_export 复用）
POC_2_5_EXPORT_MAP = {
    "CC-101_bare":      "p25-CC-101-bare",
    "CC-101_vein":      "p25-CC-101-vein",
    "CC-101_vein_hint": "p25-CC-101-vein_hint",
    "CC-101_hint":      "p25-CC-101-hint",
    "CC-103_bare":      None,  # 无 export
    "CC-103_vein":      "p25-CC-103-vein",
    "CC-103_vein_hint": "p25-CC-103-vein_hint",
    "CC-103_hint":      "p25-CC-103-hint",
    "CC-104_bare":      None,  # 无 export
    "CC-104_vein":      "p25-CC-104-vein",
    "CC-104_vein_hint": "p25-CC-104-vein_hint",
    "CC-104_hint":      "p25-CC-104-hint",
    "CC-105_bare":      "p25-CC-105-bare",
    "CC-105_vein":      None,  # 无 export
    "CC-105_vein_hint": "p25-CC-105-vein_hint",
    "CC-105_hint":      "p25-CC-105-hint",
}


def get_seed_export(problem_name):
    """获取 POC-2.5 round1 的 export 路径（如果存在）。"""
    traj_name = POC_2_5_EXPORT_MAP.get(problem_name)
    if traj_name is None:
        return None
    export = POC_2_5_ROUND1_DIR / "trajectories" / traj_name / "exports" / "conversation.json"
    return str(export) if export.exists() else None


def run_batch(max_rounds=5, model="glm-5-2", problems=None, reuse_round1=True):
    """批量运行续传。"""
    if problems is None:
        problems = ALL_PROBLEMS

    results = []
    print(f"\n{'='*70}")
    print(f"POC-2.6 批量续传运行：{len(problems)} 个 problem, max_rounds={max_rounds}")
    print(f"{'='*70}\n")

    for i, prob in enumerate(problems, 1):
        print(f"\n--- [{i}/{len(problems)}] {prob} ---")
        seed = get_seed_export(prob) if reuse_round1 else None
        if seed:
            print(f"  复用 POC-2.5 round1 export: {seed}")
        else:
            print(f"  无可复用的 round1 export，将从 round1 开始运行")

        result = solve_with_continuation(
            prob, max_rounds=max_rounds, model=model,
            seed_export=seed, verbose=True,
        )
        results.append(result)
        print(f"  => final_status: {result['final_status']}")

    # 汇总
    print(f"\n{'='*70}")
    print(f"批量运行汇总")
    print(f"{'='*70}")
    completed = sum(1 for r in results if r["final_status"] == "COMPLETED")
    truncated = sum(1 for r in results if r["final_status"] == "TRUNCATED_AT_MAX")
    no_export = sum(1 for r in results if r["final_status"] == "NO_EXPORT")
    print(f"COMPLETED: {completed}/{len(results)}")
    print(f"TRUNCATED_AT_MAX: {truncated}/{len(results)}")
    print(f"NO_EXPORT: {no_export}/{len(results)}")

    for r in results:
        status = r["final_status"]
        rounds = len(r.get("rounds", []))
        print(f"  {r['problem']:<20} {status:<20} rounds={rounds}")

    # 保存汇总
    summary_path = POC_2_6_DIR / "batch_results.json"
    with open(summary_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n汇总已保存: {summary_path}")

    return results


# =============================================================================
# §6 CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="POC-2.6 续传机制验证")
    sub = parser.add_subparsers(dest="command")

    # single 命令
    p_single = sub.add_parser("single", help="单题续传测试")
    p_single.add_argument("--problem", required=True,
                          help="problem 文件名（不含.txt），如 CC-101_bare")
    p_single.add_argument("--max-rounds", type=int, default=3)
    p_single.add_argument("--model", default="glm-5-2")
    p_single.add_argument("--seed-export", default=None,
                          help="复用已有的 round1 export 路径")
    p_single.add_argument("--no-reuse", action="store_true",
                          help="不复用 POC-2.5 round1 export，从 round1 重新运行")

    # batch 命令
    p_batch = sub.add_parser("batch", help="批量续传运行")
    p_batch.add_argument("--max-rounds", type=int, default=5)
    p_batch.add_argument("--model", default="glm-5-2")
    p_batch.add_argument("--problems", nargs="*", default=None,
                         help="指定 problem 列表（默认全部16个）")
    p_batch.add_argument("--no-reuse", action="store_true",
                         help="不复用 POC-2.5 round1 export")

    # detect 命令（工具：检测单个 export 是否被截断）
    p_detect = sub.add_parser("detect", help="检测 export 是否被截断")
    p_detect.add_argument("export", help="conversation.json 路径")

    # find 命令（查找本脚本启动的 devin 进程，基于 cwd 识别）
    p_find = sub.add_parser("find", help="查找属于本脚本的 devin -p 进程（基于 cwd）")
    p_find.add_argument("--workdir", default=None,
                        help="只查找 cwd 匹配此路径的进程（默认所有 poc_2.6 下的）")

    # kill 命令（杀掉本脚本启动的 devin 进程，基于 cwd 识别）
    p_kill = sub.add_parser("kill", help="杀掉属于本脚本的 devin -p 进程（基于 cwd）")
    p_kill.add_argument("--workdir", required=True,
                        help="杀掉 cwd 匹配此路径的进程")
    p_kill.add_argument("--force", action="store_true",
                        help="用 SIGKILL 而非 SIGTERM")

    args = parser.parse_args()

    if args.command == "find":
        procs = find_devin_processes(
            work_dir_prefix=args.workdir if args.workdir else None,
        )
        if not procs:
            print("没有找到属于本脚本的 devin -p 进程")
        else:
            print(f"找到 {len(procs)} 个进程：")
            for p in procs:
                print(f"  PID={p['pid']:<8} elapsed={p['elapsed']:<12} "
                      f"cwd={p['cwd']}")
                print(f"    cmd: {p['cmd']}")

    elif args.command == "kill":
        print(f"即将杀掉 cwd 匹配 {args.workdir} 的 devin 进程...")
        procs = find_devin_processes(work_dir_prefix=args.workdir)
        if not procs:
            print("没有找到匹配的进程")
        else:
            print(f"找到 {len(procs)} 个进程：")
            for p in procs:
                print(f"  PID={p['pid']:<8} elapsed={p['elapsed']:<12} cwd={p['cwd']}")
            sig = "KILL" if args.force else "TERM"
            killed = kill_processes_in_workdir(args.workdir, signal=sig)
            print(f"已杀掉 {killed} 个进程")

    elif args.command == "single":
        seed = args.seed_export
        if seed is None and not args.no_reuse:
            seed = get_seed_export(args.problem)
            if seed:
                print(f"自动复用 POC-2.5 round1 export: {seed}")

        result = solve_with_continuation(
            args.problem, max_rounds=args.max_rounds,
            model=args.model, seed_export=seed, verbose=True,
        )
        print(f"\n{'='*50}")
        print(f"最终结果: {result['final_status']}")
        print(f"轮次: {len(result.get('rounds', []))}")
        for r in result.get("rounds", []):
            print(f"  Round {r['round']}: truncated={r.get('truncated')}, "
                  f"rc={r.get('rc_chars', 0)}c, {r.get('reason', '')}")

    elif args.command == "batch":
        run_batch(
            max_rounds=args.max_rounds, model=args.model,
            problems=args.problems,
            reuse_round1=not args.no_reuse,
        )

    elif args.command == "detect":
        trunc, reason = is_truncated(args.export)
        completed, comp_reason = is_completed(args.export)
        print(f"truncated: {trunc}")
        print(f"  reason: {reason}")
        print(f"completed: {completed}")
        print(f"  reason: {comp_reason}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
