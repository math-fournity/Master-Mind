"""SessionsDBThinkingReader: 从sessions.db实时读取推理AI的thinking内容。

替代MITM proxy的thinking_readable.txt——直接从sessions.db的message_nodes表
读取assistant节点的thinking字段。

优势：
  - 不依赖HTTPS_PROXY环境变量（MITM的脆弱点）
  - 实时写入（AI思考时node就出现在sessions.db中）
  - 每个node有完整的thinking块（不需要从流式chunks拼接）
  - 有node_id和parent_node_id（天然的轮次结构）

用法：
    reader = SessionsDBThinkingReader(devin_session_id="busy-appliance")
    reader.init()
    # AI运行中周期性调用
    new_thinking = reader.poll_new_thinking()
    for chunk in new_thinking:
        print(f"node {chunk['node_id']}: {len(chunk['thinking'])} chars")
    # AI终止后
    remaining = reader.flush()
"""

import sqlite3
import json
import os
from typing import List, Dict, Optional


class ThinkingChunk:
    """一个thinking块，对应sessions.db中一个assistant message_node。"""
    def __init__(self, node_id: int, thinking: str, content: str = "",
                 tool_calls: list = None, created_at: int = 0):
        self.node_id = node_id
        self.thinking = thinking
        self.content = content
        self.tool_calls = tool_calls or []
        self.created_at = created_at

    def __repr__(self):
        return f"ThinkingChunk(node_id={self.node_id}, thinking_len={len(self.thinking)}, content_len={len(self.content)})"

    def to_dict(self):
        return {
            "node_id": self.node_id,
            "thinking": self.thinking,
            "content": self.content,
            "tool_calls": self.tool_calls,
            "created_at": self.created_at,
        }


class SessionsDBThinkingReader:
    """从sessions.db实时读取thinking内容。"""

    def __init__(self, devin_session_id: str, db_path: str = ""):
        """
        Args:
            devin_session_id: devin cli的session ID（如"busy-appliance"）
            db_path: sessions.db路径（默认~/.local/share/devin/cli/sessions.db）
        """
        self.session_id = devin_session_id
        self.db_path = db_path or os.path.expanduser(
            "~/.local/share/devin/cli/sessions.db"
        )
        self._last_node_id: int = -1  # 已处理到的node_id
        self._all_chunks: List[ThinkingChunk] = []

    def init(self):
        """初始化：从session开头开始读取。

        不跳过已有node——因为AI启动后第一个thinking block可能在
        init_sessions_db()调用之前就写入sessions.db了（launch_solver
        等待devin session出现需要时间，期间AI可能已完成第一个thinking block）。

        短thinking（如"Let me read the problem file first"，39字符）
        会被extract_from_sessions_db()中的len < 50过滤掉。
        """
        self._last_node_id = -1
        self._all_chunks = []

    def read_all(self) -> List[ThinkingChunk]:
        """读取session中所有thinking块（从头开始）。

        用于已完成session的批量读取。
        """
        self._last_node_id = -1
        self._all_chunks = []
        return self.poll_new_thinking()

    def poll_new_thinking(self) -> List[ThinkingChunk]:
        """
        轮询：返回自上次调用以来新出现的thinking块。

        只返回assistant角色的node，且thinking字段非空。
        跳过content非空的node（那些是最终输出，不是thinking过程）。
        """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute(
            "SELECT node_id, chat_message, created_at "
            "FROM message_nodes "
            "WHERE session_id=? AND node_id > ? "
            "ORDER BY node_id",
            (self.session_id, self._last_node_id),
        )
        rows = c.fetchall()
        conn.close()

        new_chunks = []
        for row in rows:
            node_id = row[0]
            chat_msg_json = row[1]
            created_at = row[2]

            self._last_node_id = max(self._last_node_id, node_id)

            try:
                msg = json.loads(chat_msg_json)
            except (json.JSONDecodeError, TypeError):
                continue

            role = msg.get("role", "")
            if role != "assistant":
                continue

            thinking_obj = msg.get("thinking", {})
            thinking_text = ""
            if isinstance(thinking_obj, dict):
                thinking_text = thinking_obj.get("thinking", "")
            elif isinstance(thinking_obj, str):
                thinking_text = thinking_obj

            content = msg.get("content", "")
            tool_calls = msg.get("tool_calls", [])

            # 只返回有thinking内容的node
            if thinking_text and len(thinking_text.strip()) > 0:
                chunk = ThinkingChunk(
                    node_id=node_id,
                    thinking=thinking_text,
                    content=content,
                    tool_calls=tool_calls,
                    created_at=created_at,
                )
                new_chunks.append(chunk)
                self._all_chunks.append(chunk)

        return new_chunks

    def flush(self) -> List[ThinkingChunk]:
        """AI终止后调用：获取最后一批未处理的thinking块。"""
        return self.poll_new_thinking()

    def get_all_chunks(self) -> List[ThinkingChunk]:
        """获取所有已采集的thinking块。"""
        return list(self._all_chunks)

    def get_all_thinking_text(self) -> str:
        """获取所有thinking拼成的完整文本。"""
        return "\n\n".join(c.thinking for c in self._all_chunks)

    def get_total_thinking_length(self) -> int:
        """获取所有thinking的总字符数。"""
        return sum(len(c.thinking) for c in self._all_chunks)
