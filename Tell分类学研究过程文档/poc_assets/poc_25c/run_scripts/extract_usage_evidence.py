#!/usr/bin/env python3
"""extract_usage_evidence.py — 方向使用度标注A轮的证据抽取支持

从T组12个run的agent thinking中抽取实例检验行为的候选证据片段（协议U1/U2/U3锚），
落盘到poc_25c/annotation_A_evidence.md供标注者逐条判读。抽取是过生成——宁滥勿缺，
标注人负责剔除误报。
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent  # poc_25c/
RUN_BASE = Path("/data/math-agent-glm5.2-tmux-agents-dir/poc25c-batch1")

PATTERNS = [
    (r"U1", r"(?:let me (?:check|test|try|verify)|check.{0,20}with|test.{0,15}n\s*=|take.{0,25}(?:case|instance|example)|for example,.{0,40}=|consider the case)"),
    (r"U2", r"(?:substitu(?:t|ting)|(?:plug|plugg)ing.{0,30}(?:in|back)|consistent with|agrees with|matches the|checks out)"),
    (r"U3", r"(?:discrepanc|inconsisten|something is wrong|sign error|must be wrong|let me recheck|re-?examin|contradiction.{0,40}(?:means|suggests)|too good|too easy|suspicious)"),
]


def main():
    out_lines = ["# 方向使用度·候选证据抽取（A轮支持材料）\n",
                 "来源：T组12run的agent reasoning_content。模式匹配过生成，标注者判读去伪。\n"]
    for rd in sorted(RUN_BASE.glob("*__T")):
        exp = rd / "exports" / "conversation.json"
        if not exp.is_file():
            continue
        conv = json.load(open(exp))
        think = "\n".join(
            str(s.get("reasoning_content") or "")
            for s in conv.get("steps", []) if s.get("source") == "agent"
        )
        out_lines.append(f"\n---\n\n## {rd.name} (thinking {len(think)//1024}K)\n")
        hits = 0
        seen_spans = []
        for tag, pat in PATTERNS:
            for m in re.finditer(pat, think, re.I):
                # 邻接去重：同一位置不同tag都保留（跨U类共现正是要找的）
                start = max(0, m.start() - 120)
                end = min(len(think), m.end() + 180)
                span = (start // 200, end // 200)
                if any(abs(span[0] - s[0]) < 1 and abs(span[1] - s[1]) < 1 for s in seen_spans):
                    continue
                seen_spans.append(span)
                snippet = think[start:end].replace("\n", " ¶ ")
                out_lines.append(f"- **[{tag}]** …{snippet}…\n")
                hits += 1
                if hits > 25:
                    break
            if hits > 25:
                out_lines.append("- (截断：该run命中过多，仅显示前25条)\n")
                break
        if hits == 0:
            out_lines.append("- (无模式命中)\n")
    out = HERE / "annotation_A_evidence.md"
    out.write_text("\n".join(out_lines))
    print(f"written: {out} ({out.stat().st_size//1024}K)")


if __name__ == "__main__":
    main()
