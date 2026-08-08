#!/usr/bin/env python3
"""
Devin CLI Trajectory Extractor
从 sessions.db 提取 devin cli 的完整工作过程，重建AI从头到尾的所有工作轨迹。

一个 trajectory = 一个 session 的完整工作过程，包含：
- session 元信息
- 按时间排序的 steps（去重后的assistant nodes + tool nodes + user nodes）
- 每个 step 包含：thinking、content、tool_calls、tool_results
- step 之间的 parent-child 关系（树结构）

数据源：
  sessions.db → sessions          (session元信息)
  sessions.db → message_nodes     (消息树：thinking + content + tool_calls)
  sessions.db → tool_call_state   (工具输入和输出)

用法：
  # 按 session_id 提取完整trajectory
  python3 trajectory_extractor.py --session-id nova-authority --output trajectory.jsonl

  # 按工作目录提取
  python3 trajectory_extractor.py --work-dir /data/.../experiment-dir --output trajectory.jsonl

  # 提取并打印摘要
  python3 trajectory_extractor.py --session-id nova-authority --summary

  # 导出为可读Markdown
  python3 trajectory_extractor.py --session-id nova-authority --format markdown --output trajectory.md

  # 增量更新：只提取新增的steps（用于session还在跑时）
  python3 trajectory_extractor.py --session-id nova-authority --output trajectory.jsonl --since-node 100

Trajectory JSONL Schema（每行一个JSON对象）：

  第一行：session_meta
  {
    "type": "session_meta",
    "session_id": "nova-authority",
    "title": "...",
    "working_directory": "/data/...",
    "model": "glm-5-2",
    "created_at": 1786165442,
    "last_activity_at": 1786167094,
    "main_chain_id": 134,
    "stats": {
      "total_steps": 97,
      "assistant_steps": 61,
      "tool_steps": 36,
      "user_steps": 1,
      "has_thinking": 40,
      "total_thinking_chars": 268848,
      "total_content_chars": 5000,
      "total_tool_calls": 61
    }
  }

  后续每行：一个 step
  {
    "type": "step",
    "step_index": 0,           // 在trajectory中的序号（从0开始）
    "node_id": 23,             // sessions.db中的node_id
    "parent_node_id": 22,      // 父node_id（树结构）
    "role": "assistant",       // system/user/assistant/tool
    "created_at": 1786165450,  // 时间戳
    "content": "...",          // AI输出给用户的内容
    "thinking": "...",         // AI的完整推理过程（仅assistant有）
    "tool_calls": [            // AI调用的工具（仅assistant有）
      {
        "id": "chatcmpl-tool-xxx",
        "name": "exec",        // 工具名：exec/read/write/edit/web_search/get_output/kill_shell/...
        "kind": "execute",     // ACP kind: execute/read/write/...
        "title": "Ran command",// 人类可读标题
        "arguments": {...},    // 工具参数
        "raw_input": {...}     // 原始输入（tool_call_state中的rawInput）
      }
    ],
    "tool_results": [          // 工具返回的结果（仅当tool_calls非空时）
      {
        "tool_call_id": "chatcmpl-tool-xxx",
        "status": "completed", // completed/failed/running
        "output": "...",       // 工具输出文本
        "meta": {...}          // 工具元信息（如cwd）
      }
    ]
  }

  tool role step（工具返回的回显）：
  {
    "type": "step",
    "step_index": 1,
    "node_id": 25,
    "parent_node_id": 24,
    "role": "tool",
    "created_at": 1786165455,
    "tool_call_id": "chatcmpl-tool-xxx",
    "content": "..."           // 工具结果回显
  }
"""

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone


SESSIONS_DB = os.path.expanduser("~/.local/share/devin/cli/sessions.db")


def find_session_by_work_dir(conn, work_dir):
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM sessions WHERE working_directory = ? ORDER BY created_at DESC LIMIT 1",
        (work_dir,),
    )
    row = cur.fetchone()
    return row[0] if row else None


def find_sessions_by_work_dir_prefix(conn, prefix):
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, working_directory, created_at FROM sessions "
        "WHERE working_directory LIKE ? ORDER BY created_at DESC",
        (f"{prefix}%",),
    )
    return cur.fetchall()


def get_session_info(conn, session_id):
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, working_directory, model, created_at, last_activity_at, main_chain_id "
        "FROM sessions WHERE id = ?",
        (session_id,),
    )
    row = cur.fetchone()
    if not row:
        return None
    return {
        "id": row[0],
        "title": row[1],
        "working_directory": row[2],
        "model": row[3],
        "created_at": row[4],
        "last_activity_at": row[5],
        "main_chain_id": row[6],
    }


def load_tool_call_state(conn, session_id):
    """加载所有 tool_call_state，返回 {tool_call_id: {call, update}} 字典。"""
    cur = conn.cursor()
    cur.execute(
        "SELECT tool_call_id, tool_call_json, tool_call_update_json "
        "FROM tool_call_state WHERE session_id = ?",
        (session_id,),
    )
    state = {}
    for tc_id, tc_json, tc_update in cur.fetchall():
        tc = json.loads(tc_json) if tc_json else {}
        update = json.loads(tc_update) if tc_update else {}

        # 从 tc 中提取工具名和参数
        raw_input = tc.get("rawInput", {})
        kind = tc.get("kind", "")
        title = tc.get("title", "")

        # 推断工具名
        if "command" in raw_input:
            tool_name = "exec"
        elif "file_path" in raw_input and kind == "read":
            tool_name = "read"
        elif "file_path" in raw_input and kind == "write":
            tool_name = "write"
        elif "shell_id" in raw_input and "Read" in title:
            tool_name = "get_output"
        elif "shell_id" in raw_input and "Kill" in title:
            tool_name = "kill_shell"
        elif "query" in raw_input:
            tool_name = "web_search"
        elif "url" in raw_input:
            tool_name = "webfetch"
        elif "prompt" in raw_input:
            tool_name = "ask_user_question"
        elif "path" in raw_input:
            tool_name = "browser_preview"
        else:
            tool_name = kind or title or "unknown"

        # 提取输出文本
        output_text = ""
        update_content = update.get("content", [])
        if isinstance(update_content, list):
            texts = []
            for item in update_content:
                if isinstance(item, dict):
                    c = item.get("content", {})
                    if isinstance(c, dict):
                        t = c.get("text", "")
                        if t:
                            texts.append(t)
                    elif isinstance(c, str):
                        texts.append(c)
                elif isinstance(item, str):
                    texts.append(item)
            output_text = "\n".join(texts)

        state[tc_id] = {
            "tool_name": tool_name,
            "kind": kind,
            "title": title,
            "raw_input": raw_input,
            "status": update.get("status", ""),
            "output": output_text,
            "meta": update.get("_meta", {}),
        }
    return state


def extract_trajectory(conn, session_id, since_node=0):
    """
    从 sessions.db 提取指定 session 的完整 trajectory。

    返回 (session_info, steps) 元组。
    steps 是去重后的、按 node_id 排序的 step 列表。
    """
    session_info = get_session_info(conn, session_id)
    if not session_info:
        return None, []

    tool_state = load_tool_call_state(conn, session_id)

    # 提取所有 message_nodes
    cur = conn.cursor()
    cur.execute(
        "SELECT node_id, parent_node_id, chat_message, created_at, metadata "
        "FROM message_nodes WHERE session_id = ? AND node_id >= ? ORDER BY node_id",
        (session_id, since_node),
    )
    raw_nodes = cur.fetchall()

    # 去重：assistant nodes 出现两次，保留第一个
    seen_node_ids = set()
    steps = []

    for node_id, parent_id, chat_msg, created_at, metadata in raw_nodes:
        if node_id in seen_node_ids:
            continue
        seen_node_ids.add(node_id)

        msg = json.loads(chat_msg)
        role = msg.get("role", "")

        # 跳过 system 消息（太长且无推理价值）
        if role == "system":
            continue

        content = msg.get("content", "")
        thinking_obj = msg.get("thinking", {})
        thinking_text = ""
        if isinstance(thinking_obj, dict):
            thinking_text = thinking_obj.get("thinking", "")
        elif isinstance(thinking_obj, str):
            thinking_text = thinking_obj

        tool_calls_raw = msg.get("tool_calls", [])
        tool_call_id = msg.get("tool_call_id", "")  # tool role 的回显

        # 构建 tool_calls 和 tool_results
        tool_calls = []
        tool_results = []
        for tc in tool_calls_raw:
            tc_id = tc.get("id", "")
            tc_name = tc.get("name", tc.get("function", {}).get("name", "?"))
            tc_args = tc.get("arguments", tc.get("function", {}).get("arguments", {}))

            # 从 tool_call_state 获取更详细的信息
            state_entry = tool_state.get(tc_id, {})
            kind = state_entry.get("kind", "")
            title = state_entry.get("title", "")
            raw_input = state_entry.get("raw_input", {})
            # 如果 state 中有更准确的 tool_name，用它
            state_tool_name = state_entry.get("tool_name", "")
            final_name = state_tool_name if state_tool_name != "unknown" else tc_name

            tool_calls.append({
                "id": tc_id,
                "name": final_name,
                "kind": kind,
                "title": title,
                "arguments": tc_args,
                "raw_input": raw_input,
            })

            # 工具结果
            output = state_entry.get("output", "")
            status = state_entry.get("status", "")
            result_meta = state_entry.get("meta", {})
            tool_results.append({
                "tool_call_id": tc_id,
                "status": status,
                "output": output[:10000],  # 截断超长结果
                "meta": result_meta,
            })

        step = {
            "type": "step",
            "node_id": node_id,
            "parent_node_id": parent_id,
            "role": role,
            "created_at": created_at,
            "content": content,
            "thinking": thinking_text,
            "tool_calls": tool_calls,
            "tool_results": tool_results,
        }

        # tool role 的回显
        if role == "tool" and tool_call_id:
            step["tool_call_id"] = tool_call_id

        steps.append(step)

    # 添加 step_index
    for i, step in enumerate(steps):
        step["step_index"] = i

    return session_info, steps


def compute_stats(steps):
    stats = {
        "total_steps": len(steps),
        "assistant_steps": 0,
        "tool_steps": 0,
        "user_steps": 0,
        "has_thinking": 0,
        "has_content": 0,
        "has_tool_calls": 0,
        "total_thinking_chars": 0,
        "total_content_chars": 0,
        "total_tool_calls": 0,
        "tool_names": {},
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
                for tc in s["tool_calls"]:
                    name = tc["name"]
                    stats["tool_names"][name] = stats["tool_names"].get(name, 0) + 1
        elif role == "user":
            stats["user_steps"] += 1
        elif role == "tool":
            stats["tool_steps"] += 1
    return stats


def to_jsonl(session_info, steps, stats):
    """转换为 JSONL 格式：第一行 session_meta，后续每行一个 step。"""
    lines = []

    # 第一行：session_meta
    meta = {
        "type": "session_meta",
        "session_id": session_info["id"],
        "title": session_info.get("title", ""),
        "working_directory": session_info.get("working_directory", ""),
        "model": session_info.get("model", ""),
        "created_at": session_info.get("created_at", 0),
        "last_activity_at": session_info.get("last_activity_at", 0),
        "main_chain_id": session_info.get("main_chain_id", 0),
        "stats": stats,
    }
    lines.append(json.dumps(meta, ensure_ascii=False))

    # 后续每行：一个 step
    for step in steps:
        lines.append(json.dumps(step, ensure_ascii=False))

    return "\n".join(lines)


def to_markdown(session_info, steps, stats):
    """转换为可读的 Markdown。"""
    lines = []
    lines.append(f"# Devin CLI Trajectory")
    lines.append("")
    lines.append(f"**Session**: {session_info['id']}")
    lines.append(f"**Title**: {session_info.get('title', '')}")
    lines.append(f"**Work dir**: {session_info.get('working_directory', '')}")
    lines.append(f"**Model**: {session_info.get('model', '')}")
    lines.append(f"**Created**: {datetime.fromtimestamp(session_info.get('created_at', 0), tz=timezone.utc).isoformat()}")
    lines.append("")
    lines.append(f"## Statistics")
    lines.append(f"- Total steps: {stats['total_steps']}")
    lines.append(f"- Assistant steps: {stats['assistant_steps']} (with thinking: {stats['has_thinking']})")
    lines.append(f"- Tool steps: {stats['tool_steps']}")
    lines.append(f"- User steps: {stats['user_steps']}")
    lines.append(f"- Total thinking: {stats['total_thinking_chars']} chars")
    lines.append(f"- Total tool calls: {stats['total_tool_calls']}")
    lines.append(f"- Tool usage: {json.dumps(stats['tool_names'], ensure_ascii=False)}")
    lines.append("")

    for s in steps:
        role = s["role"]
        idx = s["step_index"]
        node_id = s["node_id"]
        lines.append("---")
        lines.append("")

        if role == "user":
            lines.append(f"## [{idx}] User (node {node_id})")
            lines.append(f"{s['content']}")
        elif role == "assistant":
            lines.append(f"## [{idx}] Assistant (node {node_id})")
            if s["content"]:
                lines.append(f"**Output**: {s['content']}")
            if s["thinking"]:
                lines.append("")
                lines.append(f"<details><summary>Thinking ({len(s['thinking'])} chars)</summary>")
                lines.append("")
                lines.append(s["thinking"])
                lines.append("")
                lines.append(f"</details>")
            if s["tool_calls"]:
                lines.append("")
                lines.append("**Tool calls:**")
                for tc in s["tool_calls"]:
                    args_str = json.dumps(tc["arguments"], ensure_ascii=False)[:200]
                    lines.append(f"- `{tc['name']}` ({tc['kind']}, {tc['title']}): {args_str}")
            if s["tool_results"]:
                lines.append("")
                lines.append("**Tool results:**")
                for tr in s["tool_results"]:
                    result_preview = tr["output"][:500]
                    lines.append(f"- [{tr['status']}] {result_preview}")
        elif role == "tool":
            lines.append(f"## [{idx}] Tool echo (node {node_id})")
            lines.append(f"{s['content'][:500]}")
        lines.append("")

    return "\n".join(lines)


def incremental_update(conn, session_id, existing_jsonl_path):
    """增量更新：读取已有的 JSONL，找到最后一个 node_id，只提取新增的 steps。"""
    if not os.path.exists(existing_jsonl_path):
        return 0, []

    last_node_id = 0
    with open(existing_jsonl_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if obj.get("type") == "step":
                nid = obj.get("node_id", 0)
                if nid > last_node_id:
                    last_node_id = nid
    return last_node_id, []


def main():
    parser = argparse.ArgumentParser(
        description="从 sessions.db 提取 devin cli 的完整 trajectory（thinking + content + tool_calls + tool_results）"
    )
    parser.add_argument("--session-id", help="devin cli session ID")
    parser.add_argument("--work-dir", help="工作目录（自动找最近的 session）")
    parser.add_argument("--output", "-o", help="输出文件路径")
    parser.add_argument("--format", choices=["jsonl", "markdown", "json"], default="jsonl", help="输出格式")
    parser.add_argument("--summary", action="store_true", help="只打印摘要统计")
    parser.add_argument("--since-node", type=int, default=0, help="只提取 node_id >= 此值的 steps（增量更新）")
    parser.add_argument("--incremental", action="store_true", help="增量更新模式：读取已有 JSONL，只追加新 steps")
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
    if not session_id:
        session_id = find_session_by_work_dir(conn, args.work_dir)
        if not session_id:
            print(f"ERROR: No session found for work_dir={args.work_dir}", file=sys.stderr)
            sys.exit(1)

    # 增量更新模式
    since_node = args.since_node
    if args.incremental and args.output and os.path.exists(args.output):
        since_node, _ = incremental_update(conn, session_id, args.output)
        if since_node > 0:
            print(f"Incremental: extracting nodes >= {since_node}", file=sys.stderr)

    # 提取
    session_info, steps = extract_trajectory(conn, session_id, since_node=since_node)
    if not session_info:
        print(f"ERROR: Session {session_id} not found", file=sys.stderr)
        sys.exit(1)

    stats = compute_stats(steps)

    # 输出
    if args.summary:
        print(f"Session: {session_id}")
        print(f"Title: {session_info.get('title', '')}")
        print(f"Work dir: {session_info.get('working_directory', '')}")
        print(f"Model: {session_info.get('model', '')}")
        print(f"Total steps: {stats['total_steps']}")
        print(f"Assistant steps: {stats['assistant_steps']} (with thinking: {stats['has_thinking']})")
        print(f"Tool steps: {stats['tool_steps']}")
        print(f"Total thinking: {stats['total_thinking_chars']} chars")
        print(f"Total tool calls: {stats['total_tool_calls']}")
        print(f"Tool usage: {json.dumps(stats['tool_names'], ensure_ascii=False)}")
        conn.close()
        return

    if args.format == "markdown":
        output = to_markdown(session_info, steps, stats)
    elif args.format == "json":
        output = json.dumps({
            "session": session_info,
            "stats": stats,
            "steps": steps,
        }, ensure_ascii=False, indent=2)
    else:  # jsonl
        output = to_jsonl(session_info, steps, stats)

    if args.output:
        if args.incremental and args.format == "jsonl" and os.path.exists(args.output):
            # 追加模式：只追加 step 行，不重复 session_meta
            with open(args.output, "a") as f:
                for step in steps:
                    f.write(json.dumps(step, ensure_ascii=False) + "\n")
            print(f"Appended {len(steps)} steps to {args.output}")
        else:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"Written to {args.output} ({len(output)} chars)")
        print(f"  Steps: {stats['total_steps']}, Thinking: {stats['total_thinking_chars']} chars, Tool calls: {stats['total_tool_calls']}")
    else:
        print(output)

    conn.close()


if __name__ == "__main__":
    main()
