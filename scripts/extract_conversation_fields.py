#!/usr/bin/env python3
"""从conversation.json提取指定step的指定字段，用于制作HANDOVER.md。

用法：
  python3 extract_conversation_fields.py <conversation.json> [--step N] [--field name] [--all-agent]

示例：
  # 提取step 8的message（题目）
  python3 extract_conversation_fields.py conv.json --step 8 --field message

  # 提取所有agent step的reasoning_content
  python3 extract_conversation_fields.py conv.json --all-agent --field reasoning_content

  # 提取step 14的tool_calls参数（proof.md内容）
  python3 extract_conversation_fields.py conv.json --step 14 --field tool_calls

  # 提取step 16的message（最终总结）
  python3 extract_conversation_fields.py conv.json --step 16 --field message
"""
import argparse
import json
import sys
from pathlib import Path


def load_conversation(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_step(data: dict, step_idx: int) -> dict:
    steps = data.get("steps", [])
    if step_idx < 0 or step_idx >= len(steps):
        raise IndexError(f"step index {step_idx} out of range (0..{len(steps)-1})")
    return steps[step_idx]


def extract_field(step: dict, field: str) -> object:
    if field not in step:
        return None
    return step[field]


def format_output(value, max_len: int = None) -> str:
    if value is None:
        return "<missing>"
    if isinstance(value, str):
        s = value
    else:
        s = json.dumps(value, ensure_ascii=False, indent=2)
    if max_len and len(s) > max_len:
        s = s[:max_len] + f"\n... [truncated at {max_len}c, total {len(s)}c]"
    return s


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("conversation_json", help="path to conversation.json")
    parser.add_argument("--step", type=int, help="step index (0-based)")
    parser.add_argument("--field", help="field name to extract (message, reasoning_content, tool_calls, observation, etc.)")
    parser.add_argument("--all-agent", action="store_true", help="iterate all agent steps")
    parser.add_argument("--max-len", type=int, default=None, help="max output length per field")
    parser.add_argument("--list-steps", action="store_true", help="list all steps with summary")
    args = parser.parse_args()

    data = load_conversation(args.conversation_json)

    if args.list_steps:
        for i, s in enumerate(data.get("steps", [])):
            src = s.get("source", "?")
            msg_len = len(s.get("message", "") or "")
            rc_len = len(s.get("reasoning_content", "") or "")
            tc = len(s.get("tool_calls", []) or [])
            print(f"  step[{i}] source={src} msg={msg_len}c rc={rc_len}c tool_calls={tc}")
        return

    if args.all_agent:
        for i, s in enumerate(data.get("steps", [])):
            if s.get("source") != "agent":
                continue
            val = extract_field(s, args.field) if args.field else s
            print(f"===== step[{i}] field={args.field or 'whole'} =====")
            print(format_output(val, args.max_len))
            print()
        return

    if args.step is None or args.field is None:
        parser.error("need --step and --field, or --all-agent --field, or --list-steps")

    step = get_step(data, args.step)
    val = extract_field(step, args.field)
    print(format_output(val, args.max_len))


if __name__ == "__main__":
    main()
