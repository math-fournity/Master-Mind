#!/usr/bin/env python3
"""
Devin CLI Trajectory Real-time Monitor
实时监控sessions.db，当新的thinking step出现时立即提取并打印。

用法：
  python3 trajectory_monitor.py --session-id <session_id>
  python3 trajectory_monitor.py --work-dir <work_dir>
  python3 trajectory_monitor.py --session-id <session_id> --interval 3 --output trajectory.jsonl
"""

import argparse
import json
import os
import sqlite3
import sys
import time
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


def get_latest_nodes(conn, session_id, since_node_id):
    """获取node_id > since_node_id的所有新node（去重）。"""
    cur = conn.cursor()
    cur.execute(
        "SELECT node_id, parent_node_id, chat_message, created_at "
        "FROM message_nodes WHERE session_id = ? AND node_id > ? ORDER BY node_id",
        (session_id, since_node_id),
    )
    
    seen = set()
    nodes = []
    for node_id, parent_id, chat_msg, created_at in cur.fetchall():
        if node_id in seen:
            continue
        seen.add(node_id)
        msg = json.loads(chat_msg)
        role = msg.get("role", "")
        if role == "system":
            continue
        nodes.append({
            "node_id": node_id,
            "parent_node_id": parent_id,
            "role": role,
            "content": msg.get("content", ""),
            "thinking": msg.get("thinking", {}).get("thinking", "") if isinstance(msg.get("thinking"), dict) else "",
            "tool_calls": msg.get("tool_calls", []),
            "tool_call_id": msg.get("tool_call_id", ""),
            "created_at": created_at,
        })
    return nodes


def get_tool_results(conn, session_id, tool_call_ids):
    """获取tool_call_ids对应的工具结果。"""
    if not tool_call_ids:
        return {}
    cur = conn.cursor()
    placeholders = ",".join("?" * len(tool_call_ids))
    cur.execute(
        f"SELECT tool_call_id, tool_call_update_json FROM tool_call_state "
        f"WHERE session_id = ? AND tool_call_id IN ({placeholders})",
        [session_id] + tool_call_ids,
    )
    results = {}
    for tc_id, update_json in cur.fetchall():
        update = json.loads(update_json) if update_json else {}
        output = ""
        for item in update.get("content", []):
            if isinstance(item, dict):
                c = item.get("content", {})
                if isinstance(c, dict):
                    output += c.get("text", "")
        results[tc_id] = {
            "status": update.get("status", ""),
            "output": output[:2000],
        }
    return results


def format_step(node, tool_results=None):
    """格式化一个step为可读字符串。"""
    role = node["role"]
    node_id = node["node_id"]
    ts = datetime.fromtimestamp(node["created_at"], tz=timezone.utc).strftime("%H:%M:%S")
    
    lines = []
    
    if role == "user":
        lines.append(f"[{ts}] === USER (node {node_id}) ===")
        lines.append(f"  {node['content'][:200]}")
    
    elif role == "assistant":
        thinking = node["thinking"]
        content = node["content"]
        tool_calls = node["tool_calls"]
        
        lines.append(f"[{ts}] === ASSISTANT (node {node_id}) ===")
        if content:
            lines.append(f"  OUTPUT: {content[:200]}")
        if thinking:
            lines.append(f"  THINKING ({len(thinking)} chars):")
            # 显示thinking的前300和后300字符
            if len(thinking) <= 600:
                lines.append(f"    {thinking}")
            else:
                lines.append(f"    [START] {thinking[:300]}")
                lines.append(f"    [...{len(thinking)-600} chars omitted...]")
                lines.append(f"    [END] {thinking[-300:]}")
        if tool_calls:
            for tc in tool_calls:
                tc_id = tc.get("id", "")
                tc_name = tc.get("name", tc.get("function", {}).get("name", "?"))
                args = str(tc.get("arguments", tc.get("function", {}).get("arguments", "")))[:100]
                lines.append(f"  TOOL: {tc_name}({args})")
                
                if tool_results and tc_id in tool_results:
                    result = tool_results[tc_id]
                    lines.append(f"    RESULT [{result['status']}]: {result['output'][:200]}")
        
        if not thinking and not content and not tool_calls:
            lines.append(f"  (empty)")
    
    elif role == "tool":
        content = node["content"]
        lines.append(f"[{ts}] === TOOL ECHO (node {node_id}) ===")
        lines.append(f"  {content[:200]}")
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="实时监控devin cli的trajectory")
    parser.add_argument("--session-id", help="session ID")
    parser.add_argument("--work-dir", help="工作目录（自动找session）")
    parser.add_argument("--interval", type=float, default=3.0, help="轮询间隔（秒）")
    parser.add_argument("--output", "-o", help="同时追加到JSONL文件")
    parser.add_argument("--max-wait", type=int, default=600, help="最大等待时间（秒）")
    parser.add_argument("--db", default=SESSIONS_DB, help="sessions.db路径")
    args = parser.parse_args()

    if not args.session_id and not args.work_dir:
        parser.error("必须指定 --session-id 或 --work-dir")

    conn = sqlite3.connect(args.db)
    
    session_id = args.session_id
    if not session_id:
        session_id = find_session_by_work_dir(conn, args.work_dir)
        if not session_id:
            print(f"ERROR: No session found for work_dir={args.work_dir}", file=sys.stderr)
            sys.exit(1)

    print(f"Monitoring session: {session_id}")
    print(f"Poll interval: {args.interval}s")
    print(f"Max wait: {args.max_wait}s")
    print(f"Waiting for new steps...")
    print()

    last_node_id = 0
    start_time = time.time()
    
    # 如果session已有数据，从最后一个node开始
    cur = conn.cursor()
    cur.execute("SELECT MAX(node_id) FROM message_nodes WHERE session_id=?", (session_id,))
    row = cur.fetchone()
    if row and row[0]:
        last_node_id = row[0]
        print(f"Starting from node {last_node_id} (existing data)")
        print()

    while True:
        elapsed = time.time() - start_time
        if elapsed > args.max_wait:
            print(f"\nMax wait ({args.max_wait}s) reached. Stopping.")
            break

        # 检查session是否还在活跃
        cur.execute("SELECT last_activity_at FROM sessions WHERE id=?", (session_id,))
        row = cur.fetchone()
        if not row:
            print(f"Session {session_id} not found. Stopping.")
            break
        
        # 获取新nodes
        new_nodes = get_latest_nodes(conn, session_id, last_node_id)
        
        if new_nodes:
            # 收集所有tool_call_ids
            tc_ids = []
            for node in new_nodes:
                for tc in node["tool_calls"]:
                    tc_id = tc.get("id", "")
                    if tc_id:
                        tc_ids.append(tc_id)
            
            tool_results = get_tool_results(conn, session_id, tc_ids)
            
            for node in new_nodes:
                step_str = format_step(node, tool_results)
                print(step_str)
                print()
                sys.stdout.flush()
                
                last_node_id = max(last_node_id, node["node_id"])
                
                # 追加到JSONL
                if args.output:
                    with open(args.output, "a") as f:
                        f.write(json.dumps({
                            "type": "step",
                            "node_id": node["node_id"],
                            "parent_node_id": node["parent_node_id"],
                            "role": node["role"],
                            "content": node["content"],
                            "thinking": node["thinking"],
                            "tool_calls": node["tool_calls"],
                            "created_at": node["created_at"],
                        }, ensure_ascii=False) + "\n")
        
        time.sleep(args.interval)

    conn.close()


if __name__ == "__main__":
    main()
