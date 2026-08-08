#!/usr/bin/env python3
"""
FATE批量测试脚本：用devin cli在指定Solver工作目录中批量解答FATE题目。

用法：
  python3 scripts/fate_batch_test.py <batch_json> <work_dir> <run_id>

例如：
  python3 scripts/fate_batch_test.py fate_batch_1.json /data/math-agent-glm5.2-1 fate_batch_1

工作方式：
  - 读取batch_json中的题目列表
  - 对每道题，调用 devin -p "题目" 在work_dir中运行
  - 导出conversation.json到runs/<run_id>/
  - 收集结果到solutions.json和summary.json
"""
import json
import os
import sys
import time
import subprocess
import hashlib
from datetime import datetime, timezone
from pathlib import Path


def run_one_problem(problem: dict, work_dir: str, run_dir: str, model: str = "glm-5-2", timeout: int = 300) -> dict:
    """对单道题调用devin cli"""
    pid = problem.get("id", "?")
    level = problem.get("level", "?")
    statement = problem.get("informal_statement", "")
    formal = problem.get("formal_statement", "")

    # 构造prompt：给自然语言题目，要求证明
    prompt = f"""你是数学大师。请证明以下数学命题。

题目（{level} #{pid}）：
{statement}

要求：
1. 给出完整的证明，不要跳步
2. 数学公式用LaTeX
3. 证明完成后用"证毕"标记
4. 如果你不知道如何证明，明确说"我不知道"
5. 禁止搜索网络

请开始证明："""

    # 铁律：长题目写入文件，devin -p只传短指令（防止题目截断）
    problem_file = os.path.join(work_dir, "problem.txt")
    with open(problem_file, "w") as f:
        f.write(prompt)

    export_path = os.path.abspath(os.path.join(run_dir, f"problem_{level}_{pid}_conversation.json"))

    cmd = ["devin", "-p", "请读取当前目录下的problem.txt文件，解答其中的数学题。",
           "--model", model, "--respect-workspace-trust", "false",
           "--export", export_path]

    start = time.time()
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout,
            cwd=work_dir,
        )
        elapsed = time.time() - start
        response = result.stdout.strip()
        if result.returncode != 0:
            response = f"[ERROR returncode={result.returncode}] {result.stderr[:500]}\n{response}"
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        response = "[TIMEOUT]"
    finally:
        # 清理problem.txt（session隔离铁律）
        if os.path.exists(problem_file):
            os.remove(problem_file)

    # 判断状态
    status = "unknown"
    resp_lower = response.lower()
    if "证毕" in response or "QED" in response or "qed" in resp_lower or "证明完毕" in response:
        status = "solved"
    elif "我不知道" in response or "无法" in response or "不知道" in response:
        status = "stuck"
    elif "[TIMEOUT]" in response or "[ERROR" in response:
        status = "error"
    elif len(response) > 200:
        status = "partial"
    else:
        status = "stuck"

    # 提取session_id
    session_id = ""
    if os.path.exists(export_path):
        try:
            with open(export_path) as f:
                conv = json.load(f)
            session_id = conv.get("session_id", "")
        except (json.JSONDecodeError, IOError):
            pass

    return {
        "id": pid,
        "level": level,
        "statement": statement[:200],
        "status": status,
        "response_length": len(response),
        "elapsed_seconds": round(elapsed, 1),
        "session_id": session_id,
        "response_preview": response[:500],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    if len(sys.argv) < 4:
        print("用法: python3 fate_batch_test.py <batch_json> <work_dir> <run_id>")
        sys.exit(1)

    batch_json = sys.argv[1]
    work_dir = sys.argv[2]
    run_id = sys.argv[3]
    model = sys.argv[4] if len(sys.argv) > 4 else "glm-5-2"
    timeout = int(sys.argv[5]) if len(sys.argv) > 5 else 300

    # 读取题目
    with open(batch_json) as f:
        problems = json.load(f)

    # 创建run目录
    repo_root = "/data/master-mind-glm5.2-grove"
    run_dir = os.path.join(repo_root, "runs", run_id)
    os.makedirs(run_dir, exist_ok=True)

    print(f"=== FATE Batch Test: {run_id} ===")
    print(f"题目数: {len(problems)}")
    print(f"工作目录: {work_dir}")
    print(f"模型: {model}")
    print(f"超时: {timeout}s/题")
    print(f"Run目录: {run_dir}")
    print()

    # 逐题测试
    solutions = []
    for i, problem in enumerate(problems):
        pid = problem.get("id", "?")
        level = problem.get("level", "?")
        print(f"[{i+1}/{len(problems)}] {level} #{pid} ... ", end="", flush=True)

        # 铁律：每道题必须是全新的devin cli session
        # 1. 清理work_dir下的残留文件，防止devin cli读到上一题的数据
        for fname in os.listdir(work_dir):
            if fname in ('solutions.json', 'summary.json', 'fate_batch.json', 'fate_hard_batch.json',
                         'fate_hard_sample.json', 'failed_problems.json', 'hard_batch.json',
                         'retry_batch.json', 'download_top10.log'):
                os.remove(os.path.join(work_dir, fname))
        # 2. 清理work_dir下的.devin/sessions目录（如果有）
        sessions_dir = os.path.join(work_dir, '.devin', 'sessions')
        if os.path.isdir(sessions_dir):
            import shutil
            shutil.rmtree(sessions_dir)

        result = run_one_problem(problem, work_dir, run_dir, model, timeout)
        solutions.append(result)

        print(f"{result['status']} ({result['elapsed_seconds']}s, {result['response_length']}chars)")

        # 只写run_dir，不写work_dir——防止下一题读到上一题的结果
        if (i + 1) % 10 == 0:
            with open(os.path.join(run_dir, "solutions_partial.json"), "w") as f:
                json.dump(solutions, f, ensure_ascii=False, indent=2)

    # 统计
    stats = {"solved": 0, "partial": 0, "stuck": 0, "error": 0, "unknown": 0}
    for s in solutions:
        stats[s["status"]] = stats.get(s["status"], 0) + 1

    summary = {
        "run_id": run_id,
        "total": len(solutions),
        "stats": stats,
        "model": model,
        "timeout": timeout,
        "work_dir": work_dir,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # 只写run_dir，不写work_dir
    with open(os.path.join(run_dir, "summary.json"), "w") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    with open(os.path.join(run_dir, "solutions.json"), "w") as f:
        json.dump(solutions, f, ensure_ascii=False, indent=2)

    print(f"\n=== 完成 ===")
    print(f"总计: {len(solutions)}题")
    print(f"统计: {stats}")
    print(f"结果: {work_dir}/solutions.json")
    print(f"      {work_dir}/summary.json")
    print(f"      {run_dir}/solutions.json")
    print(f"      {run_dir}/summary.json")


if __name__ == "__main__":
    main()
