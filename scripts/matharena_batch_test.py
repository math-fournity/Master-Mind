#!/usr/bin/env python3
"""
MathArena竞赛题批量测试脚本：用devin cli测试2024+年世界级竞赛最难题。

用法：
  python3 scripts/matharena_batch_test.py <batch_json> <work_dir> <run_id> [model] [timeout]
"""
import json
import os
import sys
import time
import subprocess
import re
from datetime import datetime, timezone


def normalize_answer(s: str) -> str:
    """标准化答案用于比较"""
    s = s.strip()
    # 去除$和空格
    s = s.replace('$', '').replace(' ', '').replace('\\,', '').replace('\\!', '')
    # 去除末尾的.或,
    s = s.rstrip('.,')
    return s


def check_answer(response: str, expected_answer: str) -> str:
    """检查答案是否正确"""
    if not expected_answer:
        return "no_answer"
    
    # 在response中搜索boxed{}或最终答案
    boxed = re.findall(r'\\boxed\{([^}]+)\}', response)
    if boxed:
        given = normalize_answer(boxed[-1])
        expected = normalize_answer(expected_answer)
        if given == expected:
            return "correct"
        # 尝试数值比较
        try:
            if abs(float(given) - float(expected)) < 1e-6:
                return "correct"
        except:
            pass
        return "wrong_answer"
    
    # 没有boxed，检查是否提到答案
    expected = normalize_answer(expected_answer)
    if expected and len(expected) > 2 and expected in normalize_answer(response):
        return "likely_correct"
    
    return "no_answer"


def run_one_problem(problem: dict, work_dir: str, run_dir: str, model: str, timeout: int) -> dict:
    """测试单道题"""
    pid = problem['id']
    problem_text = problem['problem']
    answer = problem.get('answer', '')
    has_sol = problem.get('has_sample_solution', False)
    is_proof = has_sol or not answer  # 有sample_solution或无答案的是证明题

    if is_proof:
        prompt = f"""你是数学大师。请证明/解答以下竞赛数学题。

题目（{pid}）：
{problem_text}

要求：
1. 给出完整的证明或解答，不要跳步
2. 数学公式用LaTeX
3. 证明完成后用"证毕"标记
4. 如果你不知道如何证明，明确说"我不知道"
5. 禁止搜索网络

请开始："""
    else:
        prompt = f"""你是数学大师。请解答以下竞赛数学题。

题目（{pid}）：
{problem_text}

要求：
1. 给出完整的解答过程
2. 最终答案用\\boxed{{答案}}格式给出
3. 数学公式用LaTeX
4. 如果你不知道，明确说"我不知道"
5. 禁止搜索网络

请开始："""

    export_path = os.path.abspath(os.path.join(run_dir, f"problem_{pid}_conversation.json"))
    cmd = ["devin", "-p", prompt, "--model", model, "--respect-workspace-trust", "false", "--export", export_path]

    start = time.time()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=work_dir)
        elapsed = time.time() - start
        response = result.stdout.strip()
        if result.returncode != 0:
            response = f"[ERROR returncode={result.returncode}] {result.stderr[:500]}\n{response}"
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        response = "[TIMEOUT]"

    # 判断状态
    status = "unknown"
    answer_check = "n/a"
    
    if "[TIMEOUT]" in response or "[ERROR" in response:
        status = "error"
    elif "我不知道" in response or "无法" in response:
        status = "stuck"
    elif is_proof:
        if "证毕" in response or "QED" in response.lower() or "证明完毕" in response:
            status = "solved"
        elif len(response) > 500:
            status = "partial"
        else:
            status = "stuck"
    else:
        # 数值题——检查答案
        answer_check = check_answer(response, answer)
        if answer_check == "correct":
            status = "correct"
        elif answer_check == "likely_correct":
            status = "likely_correct"
        elif answer_check == "wrong_answer":
            status = "wrong_answer"
        elif "我不知道" in response:
            status = "stuck"
        elif len(response) > 300:
            status = "no_answer_format"
        else:
            status = "stuck"

    return {
        "id": pid,
        "dataset": problem['dataset'],
        "problem_idx": problem['idx'] if 'idx' in problem else problem.get('problem_idx', 0),
        "diff_score": problem.get('diff_score', 0),
        "is_proof": is_proof,
        "expected_answer": answer[:100],
        "answer_check": answer_check,
        "status": status,
        "response_length": len(response),
        "elapsed_seconds": round(elapsed, 1),
        "response_preview": response[:500],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    if len(sys.argv) < 4:
        print("用法: python3 matharena_batch_test.py <batch_json> <work_dir> <run_id> [model] [timeout]")
        sys.exit(1)

    batch_json = sys.argv[1]
    work_dir = sys.argv[2]
    run_id = sys.argv[3]
    model = sys.argv[4] if len(sys.argv) > 4 else "glm-5-2"
    timeout = int(sys.argv[5]) if len(sys.argv) > 5 else 600

    with open(batch_json) as f:
        problems = json.load(f)

    repo_root = "~/master-mind-glm5.2-worktree"
    run_dir = os.path.join(repo_root, "runs", run_id)
    os.makedirs(run_dir, exist_ok=True)

    print(f"=== MathArena Hard Test: {run_id} ===")
    print(f"题目数: {len(problems)}")
    print(f"工作目录: {work_dir}")
    print(f"模型: {model} | 超时: {timeout}s/题")
    print(f"Run目录: {run_dir}")
    print()

    solutions = []
    for i, problem in enumerate(problems):
        pid = problem['id']
        print(f"[{i+1}/{len(problems)}] {pid} ... ", end="", flush=True)
        result = run_one_problem(problem, work_dir, run_dir, model, timeout)
        solutions.append(result)
        print(f"{result['status']} ({result['elapsed_seconds']}s, {result['response_length']}chars)")

        if (i + 1) % 3 == 0:
            with open(os.path.join(work_dir, "solutions.json"), "w") as f:
                json.dump(solutions, f, ensure_ascii=False, indent=2)

    with open(os.path.join(work_dir, "solutions.json"), "w") as f:
        json.dump(solutions, f, ensure_ascii=False, indent=2)

    stats = {}
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

    with open(os.path.join(work_dir, "summary.json"), "w") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    with open(os.path.join(run_dir, "summary.json"), "w") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    with open(os.path.join(run_dir, "solutions.json"), "w") as f:
        json.dump(solutions, f, ensure_ascii=False, indent=2)

    print(f"\n=== 完成 ===")
    print(f"总计: {len(solutions)}题")
    print(f"统计: {stats}")


if __name__ == "__main__":
    main()
