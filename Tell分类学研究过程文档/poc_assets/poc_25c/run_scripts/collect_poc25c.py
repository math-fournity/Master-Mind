#!/usr/bin/env python3
"""collect_poc25c.py — POC-2.5c首批机械收取与判定

判定标准（poc25c_experiment_design.md §2+v2修正2026-08-22）：
  COMPLETED —— agent消息含"### PROOF COMPLETE"且内容≥500B（boxed降为属性记录；
               本实验环境禁用工具无proof.md，deepmath题面无boxed格式要求）
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
    # 只扫agent消息——user prompt含PROOF COMPLETE/boxed格式说明，扫全部steps会误判
    # （2026-08-22首4run事故教训：模板回显假COMPLETED）
    agent_msgs = "\n".join(
        str(s.get("message") or "") for s in steps if s.get("source") == "agent"
    )
    agent_reason_lens = [
        len(str(s.get("reasoning_content") or "")) for s in steps if s.get("source") == "agent"
    ]
    boxed = []
    import re
    for m in re.finditer(r"\\boxed\{", agent_msgs):
        depth, i = 1, m.end()
        while i < len(agent_msgs) and depth > 0:
            if agent_msgs[i] == "{":
                depth += 1
            elif agent_msgs[i] == "}":
                depth -= 1
            i += 1
        if depth == 0:
            boxed.append(agent_msgs[m.end():i - 1].strip()[:120])
    # 判定标准v2（2026-08-22）：本实验环境禁用工具→无proof.md可判，判定落在agent消息上。
    # COMPLETED=agent消息含PROOF COMPLETE且内容实质(≥500B)。boxed降为属性——
    # deepmath题面无boxed格式要求（那是amo模板），强制boxed会把真完成误判为NO_BOXED
    # （首例：2077__T正确证明|z|<1收尾PROOF COMPLETE无boxed）。
    if PROOF_MARKER in agent_msgs:
        verdict = "COMPLETED" if len(agent_msgs.strip()) >= 500 else "COMPLETE_TOO_SHORT"
    elif GIVEUP_MARKER in agent_msgs:
        verdict = "GAVE_UP"
    elif LEAK_MARKER in agent_msgs:
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
        "agent_thinking_bytes": sum(agent_reason_lens),
        "agent_message_bytes": len(agent_msgs),
        "boxed": boxed,
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
        # prompt送达校验：双锚点（题面段头+约束块尾）由gen_prompts固化在anchors.json
        user_msg = "\n".join(
            str(s.get("message") or "") for s in conv.get("steps", []) if s.get("source") == "user"
        )
        anchors = json.loads((HERE / "batch1_prompts" / name / "anchors.json").read_text())
        rec["prompt_delivery_ok"] = (
            anchors["body_head"][:50] in user_msg and anchors["cons_tail"][:30] in user_msg
        )
        if arm == "T":
            rec["hint_delivery_ok"] = "策略提示" in user_msg
        rec["export_complete"] = bool(done.is_file())
        results[name] = rec

    out = HERE / "batch1_mechanical_results.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=1))

    # 汇总表
    print(f"{'run':42s} {'verdict':18s} {'comp_tok':>9s} {'bx':>3s} boxed/备注")
    for name, r in sorted(results.items()):
        if "verdict" not in r:
            print(f"{name:42s} {r.get('status', '?'):18s}")
            continue
        bx = "Y" if r["boxed"] else "-"
        note = ("; ".join(r["boxed"][:1])[:40] if r["boxed"] else
                f"think={r.get('agent_thinking_bytes', 0)//1024}K")
        print(f"{name:42s} {r['verdict']:18s} {r['completion_tokens']:>9d} {bx:>3s} {note}"
              + ("" if r.get("prompt_delivery_ok", True) else "  [DELIVERY_FAIL]")
              + ("" if r.get("hint_delivery_ok", True) else "  [HINT_MISSING]"))
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
