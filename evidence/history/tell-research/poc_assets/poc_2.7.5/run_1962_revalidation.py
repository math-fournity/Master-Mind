#!/usr/bin/env python3
"""
POC-2.7.5 · 1962补验证驱动脚本
================================
对1962（三元组ab-c/bc-a/ca-b均为2的幂）做bare+续传（最多5轮），
判定VMS-8时代的bare失败是截断错误还是真正的思维错误。

与batch_continue_948.py的区别：
- 1962不在948道DIRECTION_ERROR列表中（它是VMS-8的题，无原始export）
- Round 1不复用seed_export，而是新跑一次bare
- 续传轮使用v1方案（机械拼接reasoning_content）——VMS-8失败形态是
  纯thinking spin，该场景下v1已被POC-2.6验证有效；单题验证不需要
  v2的Pipe A交接文档开销

判定标准（416号§5.2）：
- 续传后COMPLETED → 截断错误 → POC-1因果取商结论需重新审视
- 续传后TRUNCATED_AT_MAX → 真思维错误候选 → POC-1结论仍然有效

用法（必须在tmux中启动）：
    tmux new-session -d -s poc275-1962 \
      "cd <项目根> && .venv/bin/python3 'Tell分类学研究过程文档/poc_assets/poc_2.7.5/run_1962_revalidation.py' 2>&1 | tee 'Tell分类学研究过程文档/poc_assets/poc_2.7.5/run.log'"
"""

import json
import subprocess
import sys
import time
from pathlib import Path

# 复用POC-2.7脚本的检测与prompt构造函数
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR.parent / "poc_2.7"))
from batch_continue_948 import (  # noqa: E402
    INITIAL_PROMPT_TEMPLATE,
    build_continue_prompt,
    is_completed,
    is_truncated,
    extract_reasoning,
)

POC_DIR = SCRIPT_DIR
WORK_DIR = POC_DIR / "workdirs" / "p275-1962"
TRAJ_DIR = POC_DIR / "trajectories" / "p275-1962"
RESULTS_FILE = POC_DIR / "results_1962.json"
PROBLEM_FILE = Path("~/master-mind-glm5.2-worktree/runs/vms_poc_0/vms8_problem_files/1962_bare.txt")

MODEL = "glm-5-2"
MAX_ROUNDS = 5


def run_round(prompt_file, export_path, tmux_session, work_dir):
    """在一轮中启动devin -p并等待完成，返回export是否存在。"""
    export_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "devin", "-p",
        "--prompt-file", str(prompt_file),
        "--model", MODEL,
        "--respect-workspace-trust", "false",
        "--permission-mode", "dangerous",
        "--export", str(export_path),
    ]
    subprocess.run(["tmux", "kill-session", "-t", tmux_session],
                   capture_output=True, timeout=5)
    tmux_cmd = " ".join(cmd)
    subprocess.run(["tmux", "new-session", "-d", "-s", tmux_session,
                    f"cd {work_dir} && {tmux_cmd}"],
                   capture_output=True, timeout=10)
    while True:
        r = subprocess.run(["tmux", "has-session", "-t", tmux_session],
                           capture_output=True, timeout=5)
        if r.returncode != 0:
            break
        time.sleep(15)
    return export_path.exists()


def save(results):
    RESULTS_FILE.write_text(json.dumps(results, ensure_ascii=False, indent=2))


def main():
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    problem_text = PROBLEM_FILE.read_text().strip()
    # 剥离VMS-8时代追加的要求行（INITIAL_PROMPT_TEMPLATE自带要求）
    problem_core = problem_text.split("要求：")[0].strip()

    results = {"problem_id": "1962", "rounds": [], "model": MODEL,
               "max_rounds": MAX_ROUNDS, "method": "v1"}
    save(results)

    # ---- Round 1: 新跑bare ----
    round_num = 1
    prompt_text = INITIAL_PROMPT_TEMPLATE.format(original_problem=problem_core)
    prompt_file = WORK_DIR / f"round{round_num}_prompt.txt"
    prompt_file.write_text(prompt_text)
    export_path = TRAJ_DIR / f"round{round_num}" / "exports" / "conversation.json"

    print(f"[1962] R{round_num}: bare启动...")
    exists = run_round(prompt_file, export_path, f"p275-1962-r{round_num}", WORK_DIR)
    if not exists:
        results["rounds"].append({"round": 1, "export": None,
                                  "truncated": False, "reason": "no export"})
        results["final_status"] = "ERROR_NO_EXPORT"
        save(results)
        print("[1962] R1无export，异常终止")
        return

    truncated, reason = is_truncated(str(export_path))
    completed, _ = is_completed(str(export_path))
    rc = extract_reasoning(str(export_path))
    all_reasoning = [rc]
    results["rounds"].append({"round": 1, "export": str(export_path),
                              "truncated": truncated, "completed": completed,
                              "reason": reason, "rc_chars": len(rc)})
    save(results)
    print(f"[1962] R{round_num}: truncated={truncated}, completed={completed}, {reason}")

    if completed and not truncated:
        results["final_status"] = "COMPLETED"
        results["final_export"] = str(export_path)
        save(results)
        print("[1962] R1直接完成")
        return

    # ---- Round 2..N: v1续传 ----
    for round_num in range(2, MAX_ROUNDS + 1):
        if not truncated:
            break
        prev_reasoning = "\n\n".join(all_reasoning)
        prompt_text = build_continue_prompt(problem_core, prev_reasoning, round_num - 1)
        prompt_file = WORK_DIR / f"round{round_num}_prompt.txt"
        prompt_file.write_text(prompt_text)
        export_path = TRAJ_DIR / f"round{round_num}" / "exports" / "conversation.json"

        rc_total = sum(len(p) for p in all_reasoning)
        print(f"[1962] R{round_num}: v1续传（累积reasoning: {rc_total}c）...")
        exists = run_round(prompt_file, export_path, f"p275-1962-r{round_num}", WORK_DIR)
        if not exists:
            results["rounds"].append({"round": round_num, "export": None,
                                      "truncated": False, "reason": "no export"})
            break

        truncated, reason = is_truncated(str(export_path))
        completed, _ = is_completed(str(export_path))
        rc = extract_reasoning(str(export_path))
        all_reasoning.append(rc)
        results["rounds"].append({"round": round_num, "export": str(export_path),
                                  "truncated": truncated, "completed": completed,
                                  "reason": reason, "rc_chars": len(rc)})
        save(results)
        print(f"[1962] R{round_num}: truncated={truncated}, completed={completed}, {reason}")

        if completed:
            results["final_status"] = "COMPLETED"
            results["final_export"] = str(export_path)
            save(results)
            print(f"[1962] R{round_num}完成 → COMPLETED")
            return

    if results.get("final_status") != "COMPLETED":
        last_trunc = results["rounds"][-1].get("truncated")
        results["final_status"] = "TRUNCATED_AT_MAX" if last_trunc else "ENDED_NOT_COMPLETED"
        save(results)
    print(f"[1962] 最终状态: {results['final_status']}")


if __name__ == "__main__":
    main()
