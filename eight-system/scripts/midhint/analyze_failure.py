#!/usr/bin/env python3
"""
选题对照分析脚本——区分"方向出错"与"token不够"

输入：题号（OlympiadBench ID，如1631）
输出：对照分析报告，判定失败原因

用法：
  python3 eight-system/scripts/midhint/analyze_failure.py --problem 1631 --exp-id eight-p0-1631-R

如果不知道exp_id，用 --list 查看所有包含该题号的trajectory目录：
  python3 eight-system/scripts/midhint/analyze_failure.py --problem 1631 --list
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

# === TellCore v0 关键词 ===
# 这些是"局部-全局表示切换"方向的关键词
# 如果thinking中出现了这些词，说明AI走了目标方向
# TellCore v0的核心机制：切换到局部表示（Z/pZ或Q_p），在局部表示下揭示隐藏结构
TELLCORE_KEYWORDS = {
    # 二次剩余方向（1631用的）
    "quadratic residue": "二次剩余",
    "Euler criterion": "Euler准则",
    "Legendre": "Legendre符号",
    "quadratic character": "二次特征",
    # mod p分组方向（1843用的mod 4，1631用的mod 8）
    "mod 4": "mod 4分组",
    "mod 8": "mod 8分析",
    "mod p": "mod p分析",
    "modulo 4": "mod 4分组",
    "modulo 8": "mod 8分析",
    "modulo p": "mod p分析",
    "congruen": "同余分析",  # 匹配congruent/congruence/congruent
    # p-adic方向（1962/1709用的）
    "p-adic": "p-adic赋值",
    "2-adic": "2-adic赋值",
    "valuation": "赋值",
    # 局部-全局方向
    "local representation": "局部表示",
    "local-global": "局部-全局",
    "local structure": "局部结构",
    "lift": "提升",
    "hensel": "Hensel引理",
}

# 这些是"非目标方向"的关键词——AI走了其他方向
NON_TARGET_KEYWORDS = {
    "covering system": "covering system",
    "case analysis": "case analysis",
    "enumerate": "枚举",
    "Cunningham": "Cunningham链",
    "Mersenne prime": "Mersenne素数列举",
    "gcd": "GCD分析",
    "divisibility": "整除性分析",
}


def get_standard_solution(problem_id):
    """从OlympiadBench test.json获取标准解答"""
    with open(OLYMPIADBENCH_JSON) as f:
        data = json.load(f)
    for item in data:
        if item.get("id") == problem_id:
            solution = item.get("solution", "")
            if isinstance(solution, list):
                solution = " ".join(solution)
            return {
                "id": item["id"],
                "subfield": item.get("subfield", "?"),
                "final_answer": item.get("final_answer", "?"),
                "solution": solution,
                "question": item.get("question", ""),
            }
    return None


def find_trajectory_dirs(problem_id):
    """查找包含该题号的trajectory目录"""
    dirs = []
    if not os.path.exists(TRAJECTORY_BASE):
        return dirs
    for name in os.listdir(TRAJECTORY_BASE):
        # 匹配包含题号的目录名
        if str(problem_id) in name:
            full_path = os.path.join(TRAJECTORY_BASE, name)
            if os.path.isdir(full_path):
                dirs.append(name)
    return dirs


def get_thinking_text(exp_id):
    """从trajectory目录获取thinking文本"""
    traj_dir = os.path.join(TRAJECTORY_BASE, exp_id)
    if not os.path.exists(traj_dir):
        return None, f"trajectory目录不存在: {traj_dir}"

    # 优先用mitm/thinking_readable.txt
    thinking_path = os.path.join(traj_dir, "mitm", "thinking_readable.txt")
    if os.path.exists(thinking_path):
        with open(thinking_path) as f:
            return f.read(), f"从 {thinking_path} 读取"

    # 备选：从exports/conversation.json提取thinking
    export_path = os.path.join(traj_dir, "exports", "conversation.json")
    if os.path.exists(export_path):
        with open(export_path) as f:
            conv = json.load(f)
        # 提取thinking内容
        thinking_parts = []
        if isinstance(conv, list):
            for msg in conv:
                if isinstance(msg, dict):
                    content = msg.get("content", "")
                    if isinstance(content, str) and "thinking" in content.lower():
                        thinking_parts.append(content)
        elif isinstance(conv, dict):
            messages = conv.get("messages", [])
            for msg in messages:
                if isinstance(msg, dict):
                    content = msg.get("content", "")
                    if isinstance(content, str):
                        thinking_parts.append(content)
        if thinking_parts:
            return "\n".join(thinking_parts), f"从 {export_path} 提取"
        return None, f"无法从 {export_path} 提取thinking"

    return None, f"找不到thinking文件: {traj_dir}"


def analyze_direction(thinking_text, standard_solution):
    """分析AI的thinking方向 vs 标准解答方向"""
    thinking_lower = thinking_text.lower()
    solution_lower = standard_solution.lower()

    # 检查thinking中是否出现了TellCore v0关键词
    target_hits = {}
    for kw, desc in TELLCORE_KEYWORDS.items():
        count = thinking_lower.count(kw.lower())
        if count > 0:
            target_hits[kw] = count

    # 检查thinking中是否出现了非目标方向关键词
    non_target_hits = {}
    for kw, desc in NON_TARGET_KEYWORDS.items():
        count = thinking_lower.count(kw.lower())
        if count > 0:
            non_target_hits[kw] = count

    # 检查标准解答中是否出现了TellCore v0关键词
    solution_target_hits = {}
    for kw, desc in TELLCORE_KEYWORDS.items():
        count = solution_lower.count(kw.lower())
        if count > 0:
            solution_target_hits[kw] = count

    # 判定
    target_in_thinking = len(target_hits) > 0
    target_in_solution = len(solution_target_hits) > 0

    if target_in_solution and not target_in_thinking:
        verdict = "DIRECTION_ERROR"
        verdict_desc = "方向出错——标准解答用了TellCore方向，但AI的thinking中没有走这个方向"
    elif target_in_solution and target_in_thinking:
        verdict = "TOKEN_LIMIT"
        verdict_desc = "token不够——AI走了正确方向但可能没完成proof"
    elif not target_in_solution:
        verdict = "NO_TARGET_IN_SOLUTION"
        verdict_desc = "标准解答中没有TellCore关键词——可能这道题不适合用TellCore v0测试"
    else:
        verdict = "UNKNOWN"
        verdict_desc = "无法判定"

    return {
        "verdict": verdict,
        "verdict_desc": verdict_desc,
        "target_hits_in_thinking": target_hits,
        "non_target_hits_in_thinking": non_target_hits,
        "target_hits_in_solution": solution_target_hits,
        "thinking_length": len(thinking_text),
        "solution_length": len(standard_solution),
    }


def extract_key_turning_point(solution_text):
    """从标准解答中提取关键转折点（简化版）"""
    # 找包含TellCore关键词的句子
    sentences = re.split(r"[.\n]+", solution_text)
    key_sentences = []
    for s in sentences:
        s_lower = s.lower()
        for kw in TELLCORE_KEYWORDS:
            if kw.lower() in s_lower:
                key_sentences.append(s.strip())
                break
    return key_sentences[:5]  # 最多返回5个关键句子


def main():
    parser = argparse.ArgumentParser(description="选题对照分析——区分方向出错与token不够")
    parser.add_argument("--problem", type=int, required=True, help="OlympiadBench题号")
    parser.add_argument("--exp-id", type=str, help="trajectory目录名（exp_id）")
    parser.add_argument("--list", action="store_true", help="列出所有包含该题号的trajectory目录")
    args = parser.parse_args()

    # 步骤1：获取标准解答
    print(f"=== 步骤1：获取题号 {args.problem} 的标准解答 ===")
    sol = get_standard_solution(args.problem)
    if not sol:
        print(f"ERROR: 在OlympiadBench中找不到题号 {args.problem}")
        sys.exit(1)
    print(f"  领域: {sol['subfield']}")
    print(f"  答案: {sol['final_answer']}")
    print(f"  解答长度: {len(sol['solution'])} chars")

    # 提取关键转折点
    key_sentences = extract_key_turning_point(sol["solution"])
    print(f"  关键转折点（含TellCore关键词的句子）:")
    for i, s in enumerate(key_sentences):
        print(f"    [{i+1}] {s[:150]}...")

    # 步骤2：查找或使用trajectory目录
    if args.list:
        print(f"\n=== 包含题号 {args.problem} 的trajectory目录 ===")
        dirs = find_trajectory_dirs(args.problem)
        if not dirs:
            print(f"  找不到包含 {args.problem} 的trajectory目录")
        else:
            for d in dirs:
                print(f"  {d}")
        return

    if not args.exp_id:
        print(f"\nERROR: 需要指定 --exp-id")
        print(f"  用 --list 查看可用的trajectory目录")
        sys.exit(1)

    # 步骤3：获取thinking文本
    print(f"\n=== 步骤2：获取 {args.exp_id} 的thinking文本 ===")
    thinking, source = get_thinking_text(args.exp_id)
    if not thinking:
        print(f"ERROR: {source}")
        sys.exit(1)
    print(f"  来源: {source}")
    print(f"  长度: {len(thinking)} chars")

    # 步骤4：对照分析
    print(f"\n=== 步骤3：对照分析 ===")
    result = analyze_direction(thinking, sol["solution"])

    print(f"\n  判定: {result['verdict']}")
    print(f"  描述: {result['verdict_desc']}")
    print(f"\n  标准解答中的TellCore关键词: {result['target_hits_in_solution']}")
    print(f"  AI thinking中的TellCore关键词: {result['target_hits_in_thinking']}")
    print(f"  AI thinking中的非目标方向关键词: {result['non_target_hits_in_thinking']}")
    print(f"\n  thinking长度: {result['thinking_length']} chars")
    print(f"  解答长度: {result['solution_length']} chars")

    # 步骤5：输出结论
    print(f"\n=== 结论 ===")
    if result["verdict"] == "DIRECTION_ERROR":
        print(f"  ✅ 适合测试——AI方向出错，半路Hint有纠正方向的价值")
    elif result["verdict"] == "TOKEN_LIMIT":
        print(f"  ❌ 不适合测试——AI方向已经对了，需要的是更多token不是方向纠正")
    elif result["verdict"] == "NO_TARGET_IN_SOLUTION":
        print(f"  ⚠️ 标准解答没有用TellCore方向——这道题可能不适合用TellCore v0测试")
    else:
        print(f"  ❓ 无法判定——需要人工检查")

    # 输出JSON结果
    print(f"\n=== JSON结果 ===")
    output = {
        "problem_id": args.problem,
        "exp_id": args.exp_id,
        "subfield": sol["subfield"],
        "final_answer": sol["final_answer"],
        "verdict": result["verdict"],
        "verdict_desc": result["verdict_desc"],
        "target_hits_in_thinking": result["target_hits_in_thinking"],
        "non_target_hits_in_thinking": result["non_target_hits_in_thinking"],
        "target_hits_in_solution": result["target_hits_in_solution"],
        "thinking_length": result["thinking_length"],
        "solution_length": result["solution_length"],
        "key_turning_points": key_sentences,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
