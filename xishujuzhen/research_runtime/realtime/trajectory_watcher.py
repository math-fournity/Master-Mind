"""TrajectoryWatcher: 监控sessions.db，产出Round数据。

轮询Devin CLI的sessions.db，当检测到新的assistant节点时，
累积thinking+content+tool_calls，组装成一个"轮次"（Round）。

一个Round = 从上一个user消息（或hint注入）之后，到下一个user消息之前的
所有assistant节点的集合。对应离线解析中的A_i。

数据流：
  sessions.db → poll_new_nodes → 累积assistant节点 → Round边界检测 → Round对象

Round对象包含：
  - round_index: 轮次序号
  - agent_output: 拼接的文本（thinking + content + tool_calls描述）
  - thinking: 原始thinking文本
  - content: 原始content文本
  - tool_calls: tool_call列表
  - node_ids: 包含的node_id列表
  - timestamp: 轮次结束时间
"""

import json
import os
import sqlite3
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional, Dict, Any


SESSIONS_DB_PATH = "~/.local/share/devin/cli/sessions.db"


@dataclass
class TrajectoryNode:
    """从sessions.db提取的一个节点。"""
    node_id: int
    parent_node_id: Optional[int]
    role: str
    content: str
    thinking: str
    created_at: float  # unix timestamp
    tool_calls: List[dict] = field(default_factory=list)
    tool_call_id: str = ""


@dataclass
class Round:
    """一个完整的Solver输出轮次（对应离线的A_i）。"""
    round_index: int
    agent_output: str           # 拼接的文本，供parser使用
    thinking: str               # 原始thinking
    content: str                # 原始content（final output）
    tool_calls: List[dict]      # tool_call列表
    node_ids: List[int]         # 包含的node_id列表
    start_timestamp: float      # 轮次开始时间
    end_timestamp: float        # 轮次结束时间
    is_complete: bool = False   # 是否检测到轮次结束


class TrajectoryWatcher:
    """
    监控sessions.db，产出Round数据。

    用法：
        watcher = TrajectoryWatcher(session_id="xxx")
        for round_data in watcher.watch():
            print(f"Round {round_data.round_index}: {len(round_data.agent_output)} chars")
            # 喂给parser...

    或手动轮询：
        watcher = TrajectoryWatcher(session_id="xxx")
        rounds = watcher.poll()
        if rounds:
            latest = rounds[-1]
            # 处理latest...
    """

    def __init__(
        self,
        session_id: str,
        sessions_db: str = SESSIONS_DB_PATH,
        poll_interval: float = 2.0,
    ):
        """
        Args:
            session_id: Devin CLI session ID
            sessions_db: sessions.db路径
            poll_interval: 轮询间隔（秒）
        """
        self.session_id = session_id
        self.sessions_db = os.path.expanduser(sessions_db)
        self.poll_interval = poll_interval
        self._last_node_id: int = 0
        self._round_index: int = 0
        self._current_nodes: List[TrajectoryNode] = []
        self._current_start_ts: Optional[float] = None

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.sessions_db)
        conn.row_factory = sqlite3.Row
        return conn

    def _fetch_new_nodes(self, conn: sqlite3.Connection) -> List[TrajectoryNode]:
        """获取node_id > _last_node_id的所有新节点。"""
        cur = conn.cursor()
        cur.execute(
            "SELECT node_id, parent_node_id, chat_message, created_at "
            "FROM message_nodes "
            "WHERE session_id = ? AND node_id > ? "
            "ORDER BY node_id",
            (self.session_id, self._last_node_id),
        )
        nodes = []
        for row in cur.fetchall():
            node_id = row["node_id"]
            self._last_node_id = max(self._last_node_id, node_id)

            msg = json.loads(row["chat_message"])
            role = msg.get("role", "")
            if role == "system":
                continue

            thinking = ""
            if isinstance(msg.get("thinking"), dict):
                thinking = msg["thinking"].get("thinking", "")

            nodes.append(TrajectoryNode(
                node_id=node_id,
                parent_node_id=row["parent_node_id"],
                role=role,
                content=msg.get("content", ""),
                thinking=thinking,
                tool_calls=msg.get("tool_calls", []),
                tool_call_id=msg.get("tool_call_id", ""),
                created_at=row["created_at"],
            ))
        return nodes

    def _fetch_tool_results(
        self, conn: sqlite3.Connection, tool_call_ids: List[str]
    ) -> Dict[str, dict]:
        """获取tool_call的结果。"""
        if not tool_call_ids:
            return {}
        cur = conn.cursor()
        placeholders = ",".join("?" * len(tool_call_ids))
        cur.execute(
            f"SELECT tool_call_id, tool_call_update_json FROM tool_call_state "
            f"WHERE session_id = ? AND tool_call_id IN ({placeholders})",
            [self.session_id] + tool_call_ids,
        )
        results = {}
        for row in cur.fetchall():
            tc_id = row["tool_call_id"]
            update = json.loads(row["tool_call_update_json"]) if row["tool_call_update_json"] else {}
            output = ""
            for item in update.get("content", []):
                if isinstance(item, dict):
                    c = item.get("content", {})
                    if isinstance(c, dict):
                        output += c.get("text", "")
            results[tc_id] = {
                "status": update.get("status", ""),
                "output": output,
            }
        return results

    def _nodes_to_agent_output(
        self,
        nodes: List[TrajectoryNode],
        tool_results: Dict[str, dict],
    ) -> str:
        """
        把assistant节点拼接成parser可用的agent_output文本。

        格式：
        [Thinking] <thinking文本>
        [Tool Call: exec] <command>
        [Tool Result] <output>
        [Output] <content文本>
        """
        parts = []
        for node in nodes:
            if node.role == "assistant":
                if node.thinking:
                    parts.append(f"[Thinking]\n{node.thinking}")
                if node.tool_calls:
                    for tc in node.tool_calls:
                        tc_id = tc.get("id", "")
                        tc_name = tc.get("name", tc.get("function", {}).get("name", "?"))
                        args = tc.get("arguments", tc.get("function", {}).get("arguments", ""))
                        if isinstance(args, str):
                            args_preview = args[:500]
                        else:
                            args_preview = json.dumps(args, ensure_ascii=False)[:500]
                        parts.append(f"[Tool Call: {tc_name}]\n{args_preview}")
                        if tc_id and tc_id in tool_results:
                            result = tool_results[tc_id]
                            parts.append(f"[Tool Result ({result['status']})]\n{result['output'][:2000]}")
                if node.content:
                    parts.append(f"[Output]\n{node.content}")
            elif node.role == "tool":
                if node.content:
                    parts.append(f"[Tool Echo]\n{node.content[:1000]}")
        return "\n\n".join(parts)

    def _collect_tool_call_ids(self, nodes: List[TrajectoryNode]) -> List[str]:
        """收集所有tool_call的ID。"""
        ids = []
        for node in nodes:
            if node.role == "assistant":
                for tc in node.tool_calls:
                    tc_id = tc.get("id", "")
                    if tc_id:
                        ids.append(tc_id)
        return ids

    def poll(self) -> List[Round]:
        """
        轮询一次sessions.db，返回新完成的Round列表。

        如果没有新的已完成轮次，返回空列表。
        如果有新的assistant节点但轮次未结束，累积到_current_nodes，返回空列表。
        如果检测到轮次边界（新的user节点），把累积的assistant节点组装成Round返回。

        Returns:
            新完成的Round列表（可能为空、一个或多个）
        """
        conn = self._connect()
        try:
            new_nodes = self._fetch_new_nodes(conn)
            if not new_nodes:
                return []

            completed_rounds = []

            for node in new_nodes:
                if node.role == "user":
                    # user消息 = 轮次边界
                    # 如果有累积的assistant节点，组装成Round
                    if self._current_nodes:
                        round_data = self._build_round()
                        completed_rounds.append(round_data)
                        self._current_nodes = []
                        self._current_start_ts = None
                elif node.role == "assistant":
                    if self._current_start_ts is None:
                        self._current_start_ts = node.created_at
                    self._current_nodes.append(node)
                elif node.role == "tool":
                    # tool echo节点也累积（属于当前轮次）
                    self._current_nodes.append(node)

            return completed_rounds
        finally:
            conn.close()

    def _build_round(self) -> Round:
        """把_current_nodes组装成一个Round对象。"""
        self._round_index += 1

        # 获取tool结果
        conn = self._connect()
        try:
            tool_call_ids = self._collect_tool_call_ids(self._current_nodes)
            tool_results = self._fetch_tool_results(conn, tool_call_ids)
        finally:
            conn.close()

        # 拼接agent_output
        agent_output = self._nodes_to_agent_output(
            self._current_nodes, tool_results
        )

        # 提取thinking和content
        thinking_parts = [n.thinking for n in self._current_nodes if n.thinking]
        content_parts = [n.content for n in self._current_nodes if n.content]
        all_tool_calls = []
        for n in self._current_nodes:
            if n.role == "assistant":
                all_tool_calls.extend(n.tool_calls)

        node_ids = [n.node_id for n in self._current_nodes]
        end_ts = self._current_nodes[-1].created_at if self._current_nodes else 0

        return Round(
            round_index=self._round_index,
            agent_output=agent_output,
            thinking="\n".join(thinking_parts),
            content="\n".join(content_parts),
            tool_calls=all_tool_calls,
            node_ids=node_ids,
            start_timestamp=self._current_start_ts or end_ts,
            end_timestamp=end_ts,
            is_complete=True,
        )

    def get_current_partial(self) -> Optional[Round]:
        """
        获取当前未完成的轮次（正在进行的assistant输出）。

        用于stall检测——即使轮次未结束，也可以解析当前累积的内容。

        Returns:
            未完成的Round（is_complete=False），或None
        """
        if not self._current_nodes:
            return None
        round_data = self._build_round()
        round_data.is_complete = False
        # 不递增round_index（这是预览）
        self._round_index -= 1
        return round_data

    def watch(self, max_rounds: int = 100):
        """
        生成器：持续监控sessions.db，yield完成的Round。

        Args:
            max_rounds: 最大轮次数（防止无限循环）
        """
        rounds_yielded = 0
        while rounds_yielded < max_rounds:
            new_rounds = self.poll()
            for r in new_rounds:
                yield r
                rounds_yielded += 1
                if rounds_yielded >= max_rounds:
                    return
            time.sleep(self.poll_interval)
