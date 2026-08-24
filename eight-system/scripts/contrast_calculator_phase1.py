#!/usr/bin/env python3
"""contrast_calculator_phase1.py: Phase 1 contrast计算脚本。

从3道题×4组Solver实验结果中计算contrast，分proof-level和route-level。
每道题独立计算C1/C2/C3，再计算跨题contrast C4/C5。

数据来源：
  - tmux pipe log（落盘层判定 + exit code）
  - mitm thinking_readable.txt（路线层和证明层判定）

用法：
  python3 contrast_calculator_phase1.py --output eight-system/runs/phase1/contrast_results.json
"""

import argparse
import json
import re
from pathlib import Path

TRAJECTORY_DIR = Path("/data/math-agent-glm5.2-tmux-agents-trajectory")

# ============================================================
# 判定函数
# ============================================================

def check_route_layer_1843(text):
    """1843: 检查是否使用了mod 4分组方向。"""
    patterns = [
        r"mod\s*4", r"pmod\{4\}", r"\\equiv.*4",
        r"k\s*\\equiv\s*0.*1.*mod.*4",
    ]
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False

def check_route_layer_1709(text):
    """1709: 检查是否使用了2-adic赋值方向。"""
    patterns = [
        r"2-adic", r"v_2", r"v2\(", r"valuation",
        r"odd part", r"largest odd", r"t\(k\)",
    ]
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False

def check_route_layer_1962(text):
    """1962: 检查是否使用了2-adic赋值+case分析方向。"""
    v2_patterns = [r"2-adic", r"v_2", r"v2\(", r"valuation"]
    case_patterns = [r"a\s*\\leq\s*b\s*\\leq\s*c", r"a < b < c", r"symmetr", r"case.*a.*b.*c"]
    has_v2 = any(re.search(p, text, re.IGNORECASE) for p in v2_patterns)
    has_case = any(re.search(p, text, re.IGNORECASE) for p in case_patterns)
    return has_v2 or has_case

def check_proof_layer(text):
    """检查proof是否完成（PROOF COMPLETE标记 + 数学正确性）。"""
    return "### PROOF COMPLETE" in text

def check_thinking_completed(text):
    """检查thinking中是否完成了证明（搜索完成信号）。"""
    signals = [
        r"write.*complete.*proof", r"write.*clean.*proof",
        r"answer is.*\\boxed", r"answer is.*\{1.*3.*5\}",
        r"answer is.*2016", r"thus.*no.*real.*root",
        r"therefore.*no.*real.*root", r"Q\.E\.D",
    ]
    for s in signals:
        if re.search(s, text, re.IGNORECASE):
            return True
    return False

# ============================================================
# 数据提取
# ============================================================

def get_tmux_output(exp_id):
    """从tmux pipe log获取输出。"""
    log_path = TRAJECTORY_DIR / exp_id / "tmux" / "tmux_pipe.log"
    if log_path.exists():
        return log_path.read_text(errors='replace')
    return ""

def get_thinking(exp_id):
    """从mitm thinking_readable.txt获取thinking内容。"""
    thinking_path = TRAJECTORY_DIR / exp_id / "mitm" / "thinking_readable.txt"
    if thinking_path.exists():
        return thinking_path.read_text(errors='replace')
    return ""

def get_exit_code(exp_id):
    """从tmux pipe log获取exit code。"""
    output = get_tmux_output(exp_id)
    match = re.search(r"DEVIN_CLI_EXITED code=(\d+)", output)
    return int(match.group(1)) if match else None

# ============================================================
# 主逻辑
# ============================================================

PROBLEMS = ["1843", "1709", "1962"]
ARMS = ["R", "L", "D", "LD"]

def judge_arm(problem, arm):
    """判定一个arm的结果。"""
    exp_id = f"eight-p1-{problem}-{arm}"
    output = get_tmux_output(exp_id)
    thinking = get_thinking(exp_id)
    exit_code = get_exit_code(exp_id)
    combined = output + "\n" + thinking

    # Route layer
    if problem == "1843":
        route_ok = check_route_layer_1843(combined)
    elif problem == "1709":
        route_ok = check_route_layer_1709(combined)
    elif problem == "1962":
        route_ok = check_route_layer_1962(combined)
    else:
        route_ok = False

    # Proof layer (output)
    proof_output = check_proof_layer(output)

    # Thinking completed
    thinking_completed = check_thinking_completed(thinking)

    # Token limit
    token_limited = exit_code == 1 or "truncated" in output.lower() or "max output token" in output.lower()

    # Verdict
    if proof_output and exit_code == 0:
        verdict = "SUCCESS"
    elif route_ok and not proof_output:
        verdict = "ROUTE_ONLY"
    elif not route_ok:
        verdict = "FAILED"
    else:
        verdict = "UNKNOWN"

    return {
        "exp_id": exp_id,
        "exit_code": exit_code,
        "token_limited": token_limited,
        "route_layer": route_ok,
        "proof_output": proof_output,
        "thinking_completed": thinking_completed,
        "thinking_length": len(thinking),
        "verdict": verdict,
    }

def judge_continue(problem, arm):
    """判定continue实验的结果。"""
    exp_id = f"eight-p1-{problem}-{arm}-continue"
    output = get_tmux_output(exp_id)
    exit_code = get_exit_code(exp_id)

    # Check for actual PROOF COMPLETE (not from message text)
    # The continue message contains "### PROOF COMPLETE" so we need to exclude it
    after_msg = re.split(r"请继续完成证明", output, maxsplit=1)
    after_content = after_msg[1] if len(after_msg) > 1 else ""
    # Remove the message line itself
    lines = after_content.split("\n")
    # Skip first few lines that might contain the message
    real_proof = False
    for line in lines[1:]:
        if "### PROOF COMPLETE" in line and "结尾" not in line:
            real_proof = True
            break

    token_limited = "truncated" in output.lower() or "max output token" in output.lower() or exit_code == 1

    return {
        "exp_id": exp_id,
        "exit_code": exit_code,
        "token_limited": token_limited,
        "proof_output": real_proof,
        "verdict": "SUCCESS" if real_proof else "FAILED",
    }

def compute_contrasts(arms_data):
    """计算3个contrast，分proof-level和route-level。"""
    def proof_success(arm):
        return 1 if arms_data[arm]["verdict"] == "SUCCESS" else 0

    def route_success(arm):
        return 1 if arms_data[arm]["route_layer"] else 0

    R_p, L_p, D_p, LD_p = (proof_success(a) for a in ARMS)
    R_r, L_r, D_r, LD_r = (route_success(a) for a in ARMS)

    return {
        "proof_level": {
            "C1_LD_minus_L": {"value": LD_p - L_p, "LD": LD_p, "L": L_p},
            "C2_interaction": {"value": (LD_p - L_p) - (D_p - R_p), "LD_L": LD_p - L_p, "D_R": D_p - R_p},
            "C3_LD_minus_R": {"value": LD_p - R_p, "LD": LD_p, "R": R_p},
        },
        "route_level": {
            "C1_LD_minus_L": {"value": LD_r - L_r, "LD": LD_r, "L": L_r},
            "C2_interaction": {"value": (LD_r - L_r) - (D_r - R_r), "LD_L": LD_r - L_r, "D_R": D_r - R_r},
            "C3_LD_minus_R": {"value": LD_r - R_r, "LD": LD_r, "R": R_r},
        },
    }

def main():
    parser = argparse.ArgumentParser(description="Phase 1 contrast计算")
    parser.add_argument("--output", default="eight-system/runs/phase1/contrast_results.json")
    args = parser.parse_args()

    all_results = {}
    all_contrasts = {}

    for problem in PROBLEMS:
        print(f"\n=== Problem {problem} ===")
        arms_data = {}
        for arm in ARMS:
            result = judge_arm(problem, arm)
            arms_data[arm] = result
            print(f"  {arm}: verdict={result['verdict']} route={result['route_layer']} "
                  f"proof={result['proof_output']} thinking_done={result['thinking_completed']} "
                  f"exit={result['exit_code']} thinking_len={result['thinking_length']}")

        contrasts = compute_contrasts(arms_data)
        all_contrasts[problem] = contrasts
        all_results[problem] = arms_data

        print(f"\n  Contrasts (Proof Level):")
        for name, c in contrasts["proof_level"].items():
            print(f"    {name}: {c['value']}")
        print(f"  Contrasts (Route Level):")
        for name, c in contrasts["route_level"].items():
            print(f"    {name}: {c['value']}")

    # Continue experiments
    print("\n=== Continue Experiments ===")
    continue_results = {}
    for problem in PROBLEMS:
        continue_results[problem] = {}
        for arm in ARMS:
            # Skip arms that succeeded in original run
            if all_results[problem][arm]["verdict"] == "SUCCESS":
                continue
            result = judge_continue(problem, arm)
            continue_results[problem][arm] = result
            print(f"  {problem}-{arm}-continue: verdict={result['verdict']} "
                  f"token_limited={result['token_limited']}")

    # Cross-problem contrasts
    print("\n=== Cross-Problem Contrasts ===")
    # C4: L_continue success rate
    l_continue_successes = 0
    l_continue_total = 0
    for problem in PROBLEMS:
        if "L" in continue_results[problem]:
            l_continue_total += 1
            if continue_results[problem]["L"]["verdict"] == "SUCCESS":
                l_continue_successes += 1
    c4 = l_continue_successes / l_continue_total if l_continue_total > 0 else None
    print(f"  C4 (L_continue success rate): {c4} ({l_continue_successes}/{l_continue_total})")

    # C5: 1962 LD - 1631 LD (Phase 0)
    # Phase 0: 1631 LD = SUCCESS (1)
    # Phase 1: 1962 LD = ?
    ld_1962 = 1 if all_results["1962"]["LD"]["verdict"] == "SUCCESS" else 0
    c5 = ld_1962 - 1  # 1631 LD was SUCCESS
    print(f"  C5 (1962 LD - 1631 LD): {c5} (1962={ld_1962}, 1631=1)")

    # Output JSON
    output = {
        "problems": all_results,
        "contrasts": all_contrasts,
        "continue_results": continue_results,
        "cross_problem_contrasts": {
            "C4_L_continue_success_rate": {"value": c4, "successes": l_continue_successes, "total": l_continue_total},
            "C5_1962_LD_minus_1631_LD": {"value": c5, "1962_LD": ld_1962, "1631_LD": 1},
        },
    }
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2))
    print(f"\nResults saved to: {output_path}")

if __name__ == "__main__":
    main()
