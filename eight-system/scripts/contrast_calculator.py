#!/usr/bin/env python3
"""contrast_calculator.py: Phase 0 contrast计算脚本。

从4组Solver实验结果中计算3个contrast，分proof-level和route-level：
  C1: LD−L  (direction的增量效果)
  C2: (LD−L)−(D−R)  (direction是否依赖lineage)
  C3: LD−R  (总效果)

每组的判定（三层）：
  路线层: thinking中是否使用了目标方向（模p/二次剩余/Euler准则）
  证明层: proof是否包含5个关键步骤（mod8/QR/Euler/index/divide）
  落盘层: 是否输出了 ### PROOF COMPLETE

数据源：
  - tmux pipe log（落盘层判定）
  - sessions.db的assistant thinking（路线层和证明层判定）
    通过working_directory匹配session，提取chat_message中的thinking字段

用法：
  python3 contrast_calculator.py --output eight-system/runs/phase0/contrast_results.json
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# ============================================================
# 判定函数
# ============================================================

TARGET_KEYWORDS = [
    "二次剩余", "quadratic residue", "Euler准则", "Euler criterion",
    "Legendre", "勒让德", "互反律", "reciprocity",
    r"\\pmod{8}", r"\\equiv.*7.*\\pmod{8}", r"\\equiv.*-1.*\\pmod{8}",
]

PROOF_COMPLETE_MARKER = "### PROOF COMPLETE"
ANSWER_LEAK_MARKER = "### ANSWER LEAK DETECTED"
EXIT_MARKER = "DEVIN_CLI_EXITED"

def check_route_layer(text):
    """检查thinking/proof中是否使用了目标方向。"""
    for kw in TARGET_KEYWORDS:
        if re.search(kw, text, re.IGNORECASE):
            return True, kw
    return False, None

def check_proof_layer(text):
    """检查proof是否数学正确（简化版：检查关键步骤）。"""
    # 必须包含的关键步骤：
    # 1. x₃ ≡ 7 (mod 8) 或 -1 (mod 8)
    # 2. 2是x₃的二次剩余 / (2/x₃) = 1
    # 3. Euler准则: 2^((x₃-1)/2) ≡ 1 (mod x₃)
    # 4. (x₃-1)/2 = x₂
    # 5. x₃ | y₂ (矛盾)
    has_mod8 = bool(re.search(r"(7|\\-1).*\\pmod{8}|\\equiv.*7.*mod.*8", text, re.IGNORECASE))
    has_qr = bool(re.search(r"二次剩余|quadratic residue|Legendre|勒让德|\\frac\{2\}", text, re.IGNORECASE))
    has_euler = bool(re.search(r"Euler|2\^\{?\(.*x_3.*-1\).*2|2\^\{?\(.*p.*-1\).*2", text, re.IGNORECASE))
    has_index = bool(re.search(r"x_2|2a\+1|\(x_3-1\)/2|\(4a\+2\)/2", text, re.IGNORECASE))
    has_divide = bool(re.search(r"x_3.*\\mid.*y_2|x_3.* divides .*y_2|x_3.*\\mid.*2\^", text, re.IGNORECASE))

    steps_found = sum([has_mod8, has_qr, has_euler, has_index, has_divide])
    return steps_found >= 3, {"mod8": has_mod8, "qr": has_qr, "euler": has_euler, "index": has_index, "divide": has_divide}

def check_output_layer(text):
    """检查是否输出了 ### PROOF COMPLETE。"""
    return PROOF_COMPLETE_MARKER in text

def check_answer_leak(text):
    """检查是否触发了answer leak检测。"""
    return ANSWER_LEAK_MARKER in text

def check_exit(text):
    """检查devin cli是否已退出。"""
    return EXIT_MARKER in text

# ============================================================
# 数据提取
# ============================================================

def get_tmux_output(exp_id):
    """从tmux pipe log获取输出。"""
    log_path = Path(f"/data/math-agent-glm5.2-tmux-agents-trajectory/{exp_id}/tmux/tmux_pipe.log")
    if log_path.exists():
        return log_path.read_text(errors='replace')
    return ""

def get_session_name_from_db(exp_id):
    """从sessions.db通过working_directory查找session name。"""
    db_path = os.path.expanduser("~/.local/share/devin/cli/sessions.db")
    dir_pattern = f"%{exp_id}"
    result = subprocess.run(
        ["sqlite3", db_path, f"SELECT id FROM sessions WHERE working_directory LIKE '{dir_pattern}' ORDER BY created_at DESC LIMIT 1"],
        capture_output=True, text=True
    )
    return result.stdout.strip()

def get_thinking_from_db(session_name):
    """从sessions.db获取assistant thinking内容。"""
    db_path = os.path.expanduser("~/.local/share/devin/cli/sessions.db")
    result = subprocess.run(
        ["sqlite3", db_path, f"SELECT chat_message FROM message_nodes WHERE session_id = '{session_name}' ORDER BY node_id"],
        capture_output=True, text=True
    )
    # 解析JSON，提取thinking和content（只从assistant节点）
    thinking_text = ""
    for line in result.stdout.strip().split("\n"):
        if not line.strip():
            continue
        try:
            d = json.loads(line)
            # 只提取assistant角色的内容
            if d.get("role") != "assistant":
                continue
            t = d.get("thinking", {})
            if isinstance(t, dict):
                thinking_text += t.get("thinking", "")
            elif isinstance(t, str):
                thinking_text += t
            # 也提取content
            thinking_text += d.get("content", "")
        except json.JSONDecodeError:
            pass
    return thinking_text

# ============================================================
# 主逻辑
# ============================================================

def judge_arm(exp_id, session_name=None):
    """判定一个arm的结果。"""
    output = get_tmux_output(exp_id)

    # 如果tmux log为空，尝试从tmux capture-pane获取
    if not output:
        tmux_session = f"harness-{exp_id}"
        result = subprocess.run(
            ["tmux", "capture-pane", "-t", tmux_session, "-p"],
            capture_output=True, text=True
        )
        output = result.stdout

    # 从sessions.db获取thinking内容
    session_name = get_session_name_from_db(exp_id)
    thinking = get_thinking_from_db(session_name) if session_name else ""

    # 合并tmux output和thinking用于判定
    combined = output + "\n" + thinking

    result = {
        "exp_id": exp_id,
        "session_name": session_name,
        "has_output": len(output) > 0,
        "has_thinking": len(thinking) > 0,
        "thinking_length": len(thinking),
        "exited": check_exit(output),
        "answer_leak": check_answer_leak(combined),
        "output_layer": check_output_layer(output),
        "route_layer": False,
        "route_keyword": None,
        "proof_layer": False,
        "proof_steps": {},
        "output_preview": output[-500:] if output else "",
        "thinking_preview": thinking[-500:] if thinking else "",
    }

    if combined:
        route_ok, kw = check_route_layer(combined)
        result["route_layer"] = route_ok
        result["route_keyword"] = kw

        proof_ok, steps = check_proof_layer(combined)
        result["proof_layer"] = proof_ok
        result["proof_steps"] = steps

    # 综合判定
    if result["answer_leak"]:
        result["verdict"] = "ANSWER_LEAK"
    elif not result["has_output"] and not result["has_thinking"]:
        result["verdict"] = "NO_OUTPUT"
    elif not result["exited"] and not result["output_layer"]:
        result["verdict"] = "RUNNING"
    elif result["output_layer"] and result["proof_layer"]:
        result["verdict"] = "SUCCESS"
    elif result["route_layer"] and not result["output_layer"]:
        result["verdict"] = "ROUTE_ONLY"  # 找到路线但未完成证明（如token limit）
    elif result["output_layer"] and result["route_layer"]:
        result["verdict"] = "PARTIAL_SUCCESS"
    elif result["output_layer"]:
        result["verdict"] = "OUTPUT_ONLY"
    elif result["exited"]:
        result["verdict"] = "FAILED"
    else:
        result["verdict"] = "UNKNOWN"

    return result

def compute_contrasts(arms):
    """计算3个contrast，分proof-level和route-level。"""
    # Proof-level success = SUCCESS (proof correct + route correct + output complete)
    def proof_success(arm):
        return 1 if arms[arm]["verdict"] == "SUCCESS" else 0

    # Route-level success = found the target direction (SUCCESS or ROUTE_ONLY)
    def route_success(arm):
        return 1 if arms[arm]["route_layer"] else 0

    R_p, L_p, D_p, LD_p = proof_success("R"), proof_success("L"), proof_success("D"), proof_success("LD")
    R_r, L_r, D_r, LD_r = route_success("R"), route_success("L"), route_success("D"), route_success("LD")

    contrasts = {
        "proof_level": {
            "C1_LD_minus_L": {
                "value": LD_p - L_p,
                "meaning": "direction的增量效果（在lineage基础上，proof完成）",
                "LD": LD_p, "L": L_p,
            },
            "C2_interaction": {
                "value": (LD_p - L_p) - (D_p - R_p),
                "meaning": "direction是否依赖lineage（proof完成层面）",
                "LD_L": LD_p - L_p, "D_R": D_p - R_p,
            },
            "C3_LD_minus_R": {
                "value": LD_p - R_p,
                "meaning": "总效果（完整干预包 vs bare，proof完成）",
                "LD": LD_p, "R": R_p,
            },
        },
        "route_level": {
            "C1_LD_minus_L": {
                "value": LD_r - L_r,
                "meaning": "direction的增量效果（在lineage基础上，找到路线）",
                "LD": LD_r, "L": L_r,
            },
            "C2_interaction": {
                "value": (LD_r - L_r) - (D_r - R_r),
                "meaning": "direction是否依赖lineage（找到路线层面）",
                "LD_L": LD_r - L_r, "D_R": D_r - R_r,
            },
            "C3_LD_minus_R": {
                "value": LD_r - R_r,
                "meaning": "总效果（完整干预包 vs bare，找到路线）",
                "LD": LD_r, "R": R_r,
            },
        },
    }

    return contrasts

def main():
    parser = argparse.ArgumentParser(description="Phase 0 contrast计算")
    parser.add_argument("--results-dir", default="eight-system/runs/phase0",
                        help="结果目录")
    parser.add_argument("--output", default=None, help="输出JSON路径")
    args = parser.parse_args()

    # 判定4个arm
    arms = {}
    for arm_name, exp_id in [
        ("R", "eight-p0-1631-R"),
        ("L", "eight-p0-1631-L"),
        ("D", "eight-p0-1631-D"),
        ("LD", "eight-p0-1631-LD"),
    ]:
        print(f"\n=== Judging {arm_name} ({exp_id}) ===")
        result = judge_arm(exp_id)
        arms[arm_name] = result
        print(f"  verdict: {result['verdict']}")
        print(f"  exited: {result['exited']}")
        print(f"  output_layer: {result['output_layer']}")
        print(f"  route_layer: {result['route_layer']} (kw: {result['route_keyword']})")
        print(f"  proof_layer: {result['proof_layer']} (steps: {result['proof_steps']})")

    # 计算contrast
    contrasts = compute_contrasts(arms)
    print("\n=== Contrasts (Proof Level) ===")
    for name, c in contrasts["proof_level"].items():
        print(f"  {name}: {c['value']} ({c['meaning']})")
    print("\n=== Contrasts (Route Level) ===")
    for name, c in contrasts["route_level"].items():
        print(f"  {name}: {c['value']} ({c['meaning']})")

    # 输出JSON
    output = {
        "arms": arms,
        "contrasts": contrasts,
    }
    output_path = args.output or str(Path(args.results_dir) / "contrast_results.json")
    Path(output_path).write_text(json.dumps(output, ensure_ascii=False, indent=2))
    print(f"\nResults saved to: {output_path}")

if __name__ == "__main__":
    main()
