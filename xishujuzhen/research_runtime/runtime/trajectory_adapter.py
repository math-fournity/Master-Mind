"""
TrajectoryAdapter: 从solver-harness的sessions_db/trajectory.jsonl中
提取每轮agent_output，构造ParseRequest供实时解析管线使用。

数据流：
  solver-harness → sessions_db/trajectory.jsonl（step级，每行一个node）
  → TrajectoryAdapter.poll_new_turns()
  → List[ParseRequest]（每轮一个ParseRequest）

每个trajectory.jsonl行的格式（由trajectory_monitor.py输出）：
  {
    "type": "step",
    "node_id": 23,
    "parent_node_id": 22,
    "role": "assistant",       # assistant/user/system
    "content": "AI输出的文本",
    "thinking": "AI的完整thinking",
    "tool_calls": [...],
    "created_at": 1799697600
  }

只处理role=assistant的node，把content+thinking拼接为agent_output。
"""

import json
import os
import time
from typing import List, Optional
from pathlib import Path

from ..parser.models import ParseRequest, TurnRecord, SixTuple


class TrajectoryAdapter:
    """从solver-harness的trajectory数据中提取每轮agent_output，构造ParseRequest。"""

    def __init__(
        self,
        trajectory_jsonl_path: str,
        problem_text: str,
        run_id: str = "realtime",
        model_version: str = "glm-5-2",
    ):
        self.trajectory_jsonl_path = trajectory_jsonl_path
        self.problem_text = problem_text
        self.run_id = run_id
        self.model_version = model_version

        # 增量读取状态
        self.last_position = 0  # 上次读到的文件位置
        self.round_index = 0     # 当前轮次
        self.history: List[TurnRecord] = []
        self.current_six_tuple: Optional[SixTuple] = None

    def poll_new_turns(self) -> List[ParseRequest]:
        """轮询trajectory.jsonl，返回自上次调用以来新增的ParseRequest列表。

        返回空列表表示没有新数据（调用方应sleep后重试）。
        """
        if not os.path.exists(self.trajectory_jsonl_path):
            return []

        requests = []

        with open(self.trajectory_jsonl_path, "r") as f:
            f.seek(self.last_position)
            new_lines = f.readlines()
            self.last_position = f.tell()

        for line in new_lines:
            line = line.strip()
            if not line:
                continue

            try:
                node = json.loads(line)
            except json.JSONDecodeError:
                continue

            # 只处理assistant角色的node
            if node.get("role") != "assistant":
                continue

            # 提取agent_output：content + thinking
            content = node.get("content", "")
            thinking = node.get("thinking", "")
            tool_calls = node.get("tool_calls", [])

            # 拼接为agent_output
            # thinking是AI的内部推理，content是AI的输出文本
            # parser需要看到完整的推理过程
            agent_output = self._build_agent_output(content, thinking, tool_calls)

            if not agent_output.strip():
                continue

            # 构造ParseRequest
            request = ParseRequest(
                agent_output=agent_output,
                round_index=self.round_index,
                problem_text=self.problem_text,
                history=list(self.history),
                current_six_tuple=self.current_six_tuple,
                run_id=self.run_id,
                model_version=self.model_version,
                timestamp=str(node.get("created_at", "")),
            )

            requests.append(request)
            self.round_index += 1

            # 更新history（把本轮作为TurnRecord加入历史）
            turn_record = TurnRecord(
                q_text="",  # 实时模式下没有Q（除非注入了提示）
                a_text=agent_output,
                round_index=self.round_index - 1,
            )
            self.history.append(turn_record)

        return requests

    def update_six_tuple(self, six_tuple: SixTuple):
        """更新当前六元组状态（由RealtimePipeline在每次parse后调用）。"""
        self.current_six_tuple = six_tuple

    def _build_agent_output(
        self,
        content: str,
        thinking: str,
        tool_calls: list,
    ) -> str:
        """把content+thinking+tool_calls拼接为parser可解析的agent_output文本。

        parser期望接收自然语言推理输出，需要把thinking和content都包含进去。
        tool_calls也需要包含，因为parser需要解析工具调用事件。
        """
        parts = []

        if thinking:
            parts.append(f"[Thinking]\n{thinking}")

        if content:
            parts.append(f"[Output]\n{content}")

        if tool_calls:
            tool_parts = []
            for tc in tool_calls:
                if isinstance(tc, dict):
                    name = tc.get("name", tc.get("function", {}).get("name", "unknown"))
                    args = tc.get("arguments", tc.get("function", {}).get("arguments", ""))
                    tool_parts.append(f"  {name}({args})")
                elif isinstance(tc, str):
                    tool_parts.append(f"  {tc}")
            if tool_parts:
                parts.append(f"[Tool Calls]\n" + "\n".join(tool_parts))

        return "\n\n".join(parts)

    def get_last_node_id(self) -> Optional[int]:
        """获取最后处理的node_id（用于调试和状态检查）。"""
        return self._last_node_id if hasattr(self, "_last_node_id") else None
