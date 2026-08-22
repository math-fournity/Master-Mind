#!/usr/bin/env python3
"""collect_poc25c.py — POC-2.5c首批机械收取与判定

判定标准（poc25c_experiment_design.md §2，指纹经2026-08-22对历史round1截断样本校准）：
  COMPLETED —— 消息中出现"### PROOF COMPLETE"标记且消息含\\boxed答案
  TRUNCATED —— total_completion_tokens≥24000 且无PROOF COMPLETE（25000为cap，
                历史截断样本6253-R1实测：comp=25000/8steps/0tool_calls/78K thinking）
  GAVE_UP   —— 消息中出现"### I CANNOT SOLVE THIS"
  LEAK_FLAG —— 消息中出现"### ANSWER LEAK DETECTED"
  OTHER     —— 其余

输出：batch1_mechanical_results.json（同目录）+ 控制台汇总表。
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent  # poc_25c/
RUN_BASE = Path("/data/math-agent-glm5.2-tmux-agents-dir/poc25c-batch1")

PROOF_MARKER = "PROOF COMPLETE"
GIVEUP_MARKER = "I CANNOT SOLVE THIS"
LEAK_MARKER = "ANSWER LEAK DETECTED"


def classify(conv):
    fm = conv.get("final_metrics", {})
    comp = fm.get("total_completion_tokens", 0)
    steps = conv.get("steps", [])
    n_tc = sum(1 for s in steps if s.get("tool_calls"))
    messages = "\n".join(str(s.get("message") or "") for s in steps)
    boxed = []
    import re
    for m in re.finditer(r"\\boxed\{", messages):
        depth, i = 1, m.end()
        while i < len(messages) and depth > 0:
            if messages[i] == "{":
                depth += 1
            elif messages[i] == "}":
                depth -= 1
            i += 1
        if depth == 0:
            boxed.append(messages[m.end():i - 1].strip()[:120])
    if PROOF_MARKER in messages:
        verdict = "COMPLETED" if boxed else "COMPLETE_NO_BOXED"
    elif GIVEUP_MARKER in messages:
        verdict = "GAVE_UP"
    elif LEAK_MARKER in messages:
        verdict = "LEAK_FLAG"
    elif comp >= 24000:
        verdict = "TRUNCATED"
    else:
        verdict = "OTHER"
    return {
        "verdict": verdict,
        "completion_tokens": comp,
        "prompt_tokens": fm.get("total_prompt_tokens"),
        "steps": len(steps),
        "tool_call_steps": n_tc,
        "boxed": boxed,
        "message_bytes": len(messages),
    }


def main():
    results = {}
    for rd in sorted(RUN_BASE.glob("*__*")):
        name = rd.name
        pid, arm = name.rsplit("__", 1)
        exp = rd / "exports" / "conversation.json"
        rec = {"problem_id": pid, "arm": arm}
        done = rd / "DONE"
        meta_f = rd / "meta.json"
        if meta_f.is_file():
            rec["meta"] = json.loads(meta_f.read_text())
        if not exp.is_file():
            rec["status"] = "NO_EXPORT_YET"
            results[name] = rec
            continue
        try:
            conv = json.load(open(exp))
        except Exception as e:
            rec["status"] = f"EXPORT_PARSE_ERROR: {e}"
            results[name] = rec
            continue
        rec.update(classify(conv))
        rec["export_complete"] = bool(done.is_file())
        results[name] = rec

    out = HERE / "batch1_mechanical_results.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=1))

    # 汇总表
    print(f"{'run':42s} {'verdict':18s} {'comp_tok':>9s} boxed")
    for name, r in sorted(results.items()):
        if "verdict" not in r:
            print(f"{name:42s} {r.get('status', '?'):18s}")
            continue
        bx = "; ".join(r["boxed"][:2])[:50]
        print(f"{name:42s} {r['verdict']:18s} {r['completion_tokens']:>9d} {bx}")
    # 双臂计数
    arms = {"T": [0, 0], "C": [0, 0]}  # [completed, truncated]
    for r in results.values():
        if r.get("arm") in arms and r.get("verdict") == "COMPLETED":
            arms[r["arm"]][0] += 1
        elif r.get("arm") in arms and r.get("verdict") == "TRUNCATED":
            arms[r["arm"]][1] += 1
    print(f"\nT: completed={arms['T'][0]}/12 truncated={arms['T'][1]}/12")
    print(f"C: completed={arms['C'][0]}/12 truncated={arms['C'][1]}/12")
    print(f"\nwritten: {out}")


if __name__ == "__main__":
    main()
