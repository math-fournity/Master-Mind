#!/usr/bin/env python3
"""从 devin cli 的 conversation.json (export) 中提取所有 agent step 的 reasoning_content。

用法：
    python3 extract_reasoning.py <export.json> [--out <output.txt>] [--step <index>]

不指定 --out 时打印到 stdout。不指定 --step 时输出所有 agent step 的 reasoning。
每个 step 的输出带 header 标注 step index、字符数、tool_calls 数。
"""
import argparse
import json
import sys
from pathlib import Path


def load_export(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("export", help="conversation.json 路径")
    ap.add_argument("--out", help="输出文件路径（默认 stdout）")
    ap.add_argument("--step", type=int, help="只输出指定 step index（agent step 的全局 index）")
    args = ap.parse_args()

    data = load_export(args.export)
    steps = data.get("steps", []) or []

    chunks: list[str] = []
    for i, st in enumerate(steps):
        if st.get("source") != "agent":
            continue
        if args.step is not None and i != args.step:
            continue
        rc = st.get("reasoning_content", "") or ""
        msg = st.get("message", "") or ""
        tc = st.get("tool_calls", []) or []
        metrics = st.get("metrics", {}) or {}
        comp = metrics.get("completion_tokens", 0)
        header = (
            f"=== step[{i}] source=agent "
            f"rc={len(rc)}c msg={len(msg)}c tc={len(tc)} comp={comp} ===\n"
        )
        chunks.append(header)
        chunks.append(rc)
        chunks.append("\n")
        # 同时附上 tool_calls 摘要
        if tc:
            chunks.append(f"--- tool_calls ({len(tc)}) ---\n")
            for j, call in enumerate(tc):
                name = (call.get("function") or {}).get("name", "?")
                args_str = (call.get("function") or {}).get("arguments", "")
                chunks.append(f"[tc {j}] {name}: {args_str}\n")
            chunks.append("\n")
        # 附上 message（TUI 输出）
        if msg:
            chunks.append(f"--- message ({len(msg)}c) ---\n")
            chunks.append(msg)
            chunks.append("\n")

    text = "".join(chunks)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {len(text)} chars to {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
