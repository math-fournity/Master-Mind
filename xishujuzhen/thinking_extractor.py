#!/usr/bin/env python3
"""
Devin CLI Thinking Extractor SDK
从 sessions.db 提取 devin cli 的完整推理过程（thinking + content + tool_calls + tool_results）。

数据位置：
- sessions.db → message_nodes.chat_message JSON 的 thinking.thinking 字段（GLM-5.2 的推理过程）
- sessions.db → message_nodes.chat_message JSON 的 content 字段（AI 输出给用户的内容）
- sessions.db → message_nodes.chat_message JSON 的 tool_calls 字段（AI 调用的工具）
- sessions.db → tool_call_state.tool_call_update_json 字段（工具返回的结果）

用法：
  # 按 session_id 提取
  python3 thinking_extractor.py --session-id nova-authority --output thinking.json

  # 按工作目录提取（找最近的 session）
  python3 thinking_extractor.py --work-dir /data/grove-agents-dir/258-challenge-analysis-test1 --output thinking.json

  # 提取并打印摘要
  python3 thinking_extractor.py --session-id nova-authority --summary

  # 提取为可读的 Markdown
  python3 thinking_extractor.py --session-id nova-authority --format markdown --output thinking.md
"""

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone


SESSIONS_DB = os.path.expanduser("~/.local/share/devin/cli/sessions.db")


def find_session_by_work_dir(conn, work_dir):
    """按工作目录找最近的 session_id。"""
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, working_directory, created_at FROM sessions "
        "WHERE working_directory = ? ORDER BY created_at DESC LIMIT 1",
        (work_dir,),
    )
    row = cur.fetchone()
    if row:
        return {"id": row[0], "title": row[1], "work_dir": row[2], "created_at": row[3]}
    return None


def find_sessions_by_work_dir_prefix(conn, prefix):
    """按工作目录前缀找所有匹配的 session（按时间倒序）。"""
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, working_directory, created_at FROM sessions "
        "WHERE working_directory LIKE ? ORDER BY created_at DESC",
        (f"{prefix}%",),
    )
    rows = cur.fetchall()
    return [
        {"id": r[0], "title": r[1], "work_dir": r[2], "created_at": r[3]}
        for r in rows
    ]


def get_session_info(conn, session_id):
    """获取 session 元信息。"""
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, working_directory, model, created_at, last_activity_at "
        "FROM sessions WHERE id = ?",
        (session_id,),
    )
    row = cur.fetchone()
    if not row:
        return None
    return {
        "id": row[0],
        "title": row[1],
        "work_dir": row[2],
        "model": row[3],
        "created_at": row[4],
        "last_activity_at": row[5],
    }


def extract_thinking(conn, session_id):
    """
    从 sessions.db 提取指定 session 的完整推理过程。

    返回一个列表，每个元素是一个 step：
    - role: system/user/assistant/tool
    - content: 输出内容
    - thinking: 推理过程（仅 assistant 有）
    - tool_calls: 工具调用（仅 assistant 有）
    - tool_results: 工具返回结果（tool role 或从 tool_call_state 提取）
    - timestamp: 时间戳
    """
    cur = conn.cursor()

    # 1. 提取所有 message_nodes
    cur.execute(
        "SELECT node_id, parent_node_id, chat_message, created_at, metadata "
        "FROM message_nodes WHERE session_id = ? ORDER BY node_id",
        (session_id,),
    )
    nodes = cur.fetchall()

    # 2. 提取 tool_call_state（工具结果）
    cur.execute(
        "SELECT tool_call_id, tool_call_json, tool_call_update_json "
        "FROM tool_call_state WHERE session_id = ?",
        (session_id,),
    )
    tool_state = {}
    for tc_id, tc_json, tc_update in cur.fetchall():
        tc = json.loads(tc_json) if tc_json else {}
        update = json.loads(tc_update) if tc_update else {}
        tool_state[tc_id] = {
            "tool_call": tc,
            "tool_result": update,
        }

    # 3. 组装 steps（去重——sessions.db 中每个 node 出现两次，用 node_id 去重）
    seen_node_ids = set()
    steps = []

    for node_id, parent_id, chat_msg, created_at, metadata in nodes:
        if node_id in seen_node_ids:
            continue
        seen_node_ids.add(node_id)

        msg = json.loads(chat_msg)
        role = msg.get("role", "")
        content = msg.get("content", "")
        thinking_obj = msg.get("thinking", {})
        thinking_text = ""
        if isinstance(thinking_obj, dict):
            thinking_text = thinking_obj.get("thinking", "")
        elif isinstance(thinking_obj, str):
            thinking_text = thinking_obj

        tool_calls = msg.get("tool_calls", [])

        # 附加 tool 结果
        tool_results = []
        for tc in tool_calls:
            tc_id = tc.get("id", "")
            if tc_id in tool_state:
                result = tool_state[tc_id]["tool_result"]
                # 提取 output text
                output = result.get("output", "")
                if isinstance(output, list):
                    texts = []
                    for item in output:
                        if isinstance(item, dict):
                            c = item.get("content", {})
                            if isinstance(c, dict):
                                texts.append(c.get("text", ""))
                            elif isinstance(c, str):
                                texts.append(c)
                        elif isinstance(item, str):
                            texts.append(item)
                    output = "\n".join(texts)
                tool_results.append({
                    "tool_call_id": tc_id,
                    "tool_name": tc.get("name", tc.get("function", {}).get("name", "?")),
                    "result": str(output)[:5000],  # 截断长结果
                })

        # 跳过 system 消息（太长且无推理价值）
        if role == "system":
            continue

        steps.append({
            "node_id": node_id,
            "parent_node_id": parent_id,
            "role": role,
            "content": content,
            "thinking": thinking_text,
            "tool_calls": [
                {
                    "id": tc.get("id", ""),
                    "name": tc.get("name", tc.get("function", {}).get("name", "?")),
                    "arguments": tc.get("arguments", tc.get("function", {}).get("arguments", "")),
                }
                for tc in tool_calls
            ],
            "tool_results": tool_results,
            "created_at": created_at,
        })

    return steps


def compute_stats(steps):
    """计算统计信息。"""
    stats = {
        "total_steps": len(steps),
        "assistant_steps": 0,
        "user_steps": 0,
        "tool_steps": 0,
        "has_thinking": 0,
        "has_content": 0,
        "has_tool_calls": 0,
        "total_thinking_chars": 0,
        "total_content_chars": 0,
        "total_tool_calls": 0,
    }
    for s in steps:
        role = s["role"]
        if role == "assistant":
            stats["assistant_steps"] += 1
            if s["thinking"]:
                stats["has_thinking"] += 1
                stats["total_thinking_chars"] += len(s["thinking"])
            if s["content"]:
                stats["has_content"] += 1
                stats["total_content_chars"] += len(s["content"])
            if s["tool_calls"]:
                stats["has_tool_calls"] += 1
                stats["total_tool_calls"] += len(s["tool_calls"])
        elif role == "user":
            stats["user_steps"] += 1
        elif role == "tool":
            stats["tool_steps"] += 1
    return stats


def to_markdown(session_info, steps, stats):
    """转换为可读的 Markdown。"""
    lines = []
    lines.append(f"# Devin CLI Thinking Transcript")
    lines.append("")
    lines.append(f"**Session**: {session_info['id']}")
    lines.append(f"**Title**: {session_info.get('title', '')}")
    lines.append(f"**Work dir**: {session_info.get('work_dir', '')}")
    lines.append(f"**Model**: {session_info.get('model', '')}")
    lines.append("")
    lines.append(f"## Statistics")
    lines.append(f"- Total steps: {stats['total_steps']}")
    lines.append(f"- Assistant steps: {stats['assistant_steps']}")
    lines.append(f"- Steps with thinking: {stats['has_thinking']}")
    lines.append(f"- Total thinking chars: {stats['total_thinking_chars']}")
    lines.append(f"- Total tool calls: {stats['total_tool_calls']}")
    lines.append("")

    for s in steps:
        role = s["role"]
        node_id = s["node_id"]
        lines.append(f"---")
        lines.append(f"")
        if role == "user":
            lines.append(f"## [User] (node {node_id})")
            lines.append(f"{s['content']}")
        elif role == "assistant":
            lines.append(f"## [Assistant] (node {node_id})")
            if s["content"]:
                lines.append(f"**Output**: {s['content']}")
            if s["thinking"]:
                lines.append(f"")
                lines.append(f"<details><summary>Thinking ({len(s['thinking'])} chars)</summary>")
                lines.append("")
                lines.append(s["thinking"])
                lines.append("")
                lines.append(f"</details>")
            if s["tool_calls"]:
                for tc in s["tool_calls"]:
                    fn = tc["name"]
                    args = str(tc["arguments"])[:200]
                    lines.append(f"- Tool call: `{fn}`({args})")
            if s["tool_results"]:
                for tr in s["tool_results"]:
                    result_preview = tr["result"][:500]
                    lines.append(f"  - Result: `{result_preview}`")
        elif role == "tool":
            lines.append(f"## [Tool] (node {node_id})")
            lines.append(f"{s['content'][:500]}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="从 sessions.db 提取 devin cli 的完整推理过程（thinking + content + tool_calls + tool_results）"
    )
    parser.add_argument("--session-id", help="devin cli session ID（如 nova-authority）")
    parser.add_argument("--work-dir", help="工作目录（自动找最近的 session）")
    parser.add_argument("--output", "-o", help="输出文件路径")
    parser.add_argument("--format", choices=["json", "markdown"], default="json", help="输出格式")
    parser.add_argument("--summary", action="store_true", help="只打印摘要统计")
    parser.add_argument("--db", default=SESSIONS_DB, help="sessions.db 路径")
    args = parser.parse_args()

    if not args.session_id and not args.work_dir:
        parser.error("必须指定 --session-id 或 --work-dir")

    if not os.path.exists(args.db):
        print(f"ERROR: sessions.db not found at {args.db}", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(args.db)

    # 确定 session_id
    session_id = args.session_id
    session_info = None
    if not session_id:
        session_info = find_session_by_work_dir(conn, args.work_dir)
        if not session_info:
            print(f"ERROR: No session found for work_dir={args.work_dir}", file=sys.stderr)
            sys.exit(1)
        session_id = session_info["id"]

    session_info = get_session_info(conn, session_id)
    if not session_info:
        print(f"ERROR: Session {session_id} not found", file=sys.stderr)
        sys.exit(1)

    # 提取
    steps = extract_thinking(conn, session_id)
    stats = compute_stats(steps)

    # 输出
    if args.summary:
        print(f"Session: {session_id}")
        print(f"Title: {session_info.get('title', '')}")
        print(f"Work dir: {session_info.get('work_dir', '')}")
        print(f"Model: {session_info.get('model', '')}")
        print(f"Total steps: {stats['total_steps']}")
        print(f"Assistant steps: {stats['assistant_steps']}")
        print(f"Steps with thinking: {stats['has_thinking']}")
        print(f"Total thinking chars: {stats['total_thinking_chars']}")
        print(f"Total tool calls: {stats['total_tool_calls']}")
        conn.close()
        return

    if args.format == "markdown":
        output = to_markdown(session_info, steps, stats)
    else:
        output = json.dumps({
            "session": session_info,
            "stats": stats,
            "steps": steps,
        }, ensure_ascii=False, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Written to {args.output} ({len(output)} chars)")
        print(f"  Steps: {stats['total_steps']}, Thinking: {stats['total_thinking_chars']} chars, Tool calls: {stats['total_tool_calls']}")
    else:
        print(output)

    conn.close()


if __name__ == "__main__":
    main()
