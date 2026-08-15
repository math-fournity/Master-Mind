#!/usr/bin/env python3
"""
筛选适合mid-hint实验的候选题

步骤1：从DB获取所有bare失败题
步骤2：匹配OlympiadBench标准解答
步骤3：筛选标准解答中包含TellCore关键词的题（只有这些题才可能测试TellCore v0）
步骤4：对每道题查找trajectory目录
步骤5：输出候选题列表

用法：
  python3 eight-system/scripts/midhint/find_candidates.py
  python3 eight-system/scripts/midhint/find_candidates.py --output candidates.json
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# === 路径常量 ===
OLYMPIADBENCH_JSON = "knowledge/problem_banks/aops_instruct/eval/data/olympiadbench/test.json"
TRAJECTORY_BASE = "/data/math-agent-glm5.2-tmux-agents-trajectory"

# === TellCore v0 关键词（与analyze_failure.py一致）===
TELLCORE_KEYWORDS = [
    "quadratic residue", "Euler criterion", "Legendre", "quadratic character",
    "mod 4", "mod 8", "mod p", "modulo 4", "modulo 8", "modulo p", "congruen",
    "p-adic", "2-adic", "valuation",
    "local representation", "local-global", "local structure", "lift", "hensel",
]


def get_failed_problems():
    """从DB获取所有bare失败题的problem_id"""
    os.environ['ARANGO_DB'] = 'xishujuzhen_math_glm52'
    from arango import ArangoClient
    client = ArangoClient(hosts='http://localhost:8529')
    db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
    aql = '''FOR r IN devin_problem_runs 
      FILTER r.status IN ["failed_no_proof","failed_token_limit","failed_tool_stall"]
      RETURN DISTINCT r.problem_id'''
    return set(pid for pid in db.aql.execute(aql) if pid)


def load_olympiadbench():
    """加载OlympiadBench，返回{id: item}"""
    with open(OLYMPIADBENCH_JSON) as f:
        data = json.load(f)
    return {item["id"]: item for item in data if item.get("solution")}


def check_tellcore_in_solution(solution_text):
    """检查标准解答中是否包含TellCore关键词"""
    solution_lower = solution_text.lower()
    hits = {}
    for kw in TELLCORE_KEYWORDS:
        count = solution_lower.count(kw)
        if count > 0:
            hits[kw] = count
    return hits


def find_trajectory_dirs(problem_id):
    """查找包含该题号的trajectory目录"""
    dirs = []
    if not os.path.exists(TRAJECTORY_BASE):
        return dirs
    # 提取数字部分用于匹配
    nums = re.findall(r'\d+', str(problem_id))
    for name in os.listdir(TRAJECTORY_BASE):
        if str(problem_id) in name or any(n in name for n in nums if len(n) >= 4):
            full_path = os.path.join(TRAJECTORY_BASE, name)
            if os.path.isdir(full_path):
                # 检查是否有thinking文件
                has_thinking = (
                    os.path.exists(os.path.join(full_path, "mitm", "thinking_readable.txt")) or
                    os.path.exists(os.path.join(full_path, "exports", "conversation.json"))
                )
                if has_thinking:
                    dirs.append(name)
    return dirs


def main():
    parser = argparse.ArgumentParser(description="筛选适合mid-hint实验的候选题")
    parser.add_argument("--output", type=str, default=None, help="输出JSON文件路径")
    args = parser.parse_args()

    print("=== 步骤1：从DB获取bare失败题 ===")
    failed_pids = get_failed_problems()
    print(f"  失败题总数: {len(failed_pids)}")

    print("\n=== 步骤2：匹配OlympiadBench标准解答 ===")
    olympiad = load_olympiadbench()
    print(f"  OlympiadBench有解答的题: {len(olympiad)}")

    # 匹配：从failed_pids中提取数字，看是否在olympiad中
    matched = []
    for pid in failed_pids:
        nums = re.findall(r'\d+', pid)
        for n in nums:
            oid = int(n)
            if oid in olympiad:
                matched.append({
                    "db_pid": pid,
                    "olympiad_id": oid,
                    "subfield": olympiad[oid].get("subfield", "?"),
                    "final_answer": olympiad[oid].get("final_answer", "?"),
                    "solution_length": len(olympiad[oid].get("solution", "")),
                })
                break
    print(f"  匹配到的失败题: {len(matched)}")

    print("\n=== 步骤3：筛选标准解答中包含TellCore关键词的题 ===")
    candidates = []
    for item in matched:
        oid = item["olympiad_id"]
        sol = olympiad[oid].get("solution", "")
        if isinstance(sol, list):
            sol = " ".join(sol)
        hits = check_tellcore_in_solution(sol)
        if hits:
            item["tellcore_hits_in_solution"] = hits
            candidates.append(item)
    print(f"  标准解答含TellCore关键词的题: {len(candidates)}")

    print("\n=== 步骤4：查找trajectory目录 ===")
    with_trajectory = []
    for item in candidates:
        oid = item["olympiad_id"]
        dirs = find_trajectory_dirs(oid)
        if dirs:
            item["trajectory_dirs"] = dirs
            with_trajectory.append(item)
    print(f"  有trajectory数据的题: {len(with_trajectory)}")

    print(f"\n=== 候选题列表（{len(with_trajectory)}道）===")
    for item in with_trajectory:
        print(f"  OlympiadBench {item['olympiad_id']} ({item['subfield']}): "
              f"TellCore关键词={list(item['tellcore_hits_in_solution'].keys())[:3]}, "
              f"trajectory_dirs={len(item['trajectory_dirs'])}")

    # 输出JSON
    output = {
        "total_failed": len(failed_pids),
        "total_with_solution": len(matched),
        "total_with_tellcore": len(candidates),
        "total_with_trajectory": len(with_trajectory),
        "candidates": with_trajectory,
    }
    if args.output:
        with open(args.output, "w") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f"\n结果已保存到: {args.output}")
    else:
        print(f"\n=== JSON结果 ===")
        print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
