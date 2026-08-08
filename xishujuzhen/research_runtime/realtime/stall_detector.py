"""StallDetector: 检测Solver卡点。

两种卡点检测方式：
1. 超时检测：N秒内没有新的trajectory节点（Solver停止输出）
2. 语义检测：thinking/content中出现卡点关键词（"我不知道"、"做不出来"等）

卡点检测是触发实时检索的信号——检测到卡点后，立即对当前累积的
agent_output跑parser→retrieval→policy，选出提示并注入。
"""

import time
from dataclasses import dataclass
from typing import Optional, List

from .trajectory_watcher import Round


# 卡点关键词（Solver表达"我做不出来"的信号）
STALL_KEYWORDS = [
    "我不知道",
    "我不会做",
    "做不出来",
    "无法继续",
    "没有思路",
    "I don't know",
    "I'm stuck",
    "I am stuck",
    "I can't solve",
    "I cannot solve",
    "not sure how",
    "no idea",
    "stuck",
    "give up",
]

# 超时阈值（秒）——N秒无新节点视为卡点
DEFAULT_STALL_TIMEOUT = 30.0


@dataclass
class StallEvent:
    """检测到的卡点事件。"""
    detected_at: float           # 检测时间戳
    reason: str                  # "timeout" 或 "semantic"
    keyword: str = ""            # 语义检测时匹配的关键词
    round_index: int = 0         # 卡点发生在第几轮
    agent_output_preview: str = ""  # agent_output预览


class StallDetector:
    """
    卡点检测器。

    用法：
        detector = StallDetector(timeout=30.0)
        # 每次轮询后调用
        event = detector.check(last_node_timestamp, current_round)
        if event:
            # 触发检索...
    """

    def __init__(
        self,
        timeout: float = DEFAULT_STALL_TIMEOUT,
        keywords: Optional[List[str]] = None,
    ):
        """
        Args:
            timeout: 超时阈值（秒），无新节点超过此值视为卡点
            keywords: 语义检测关键词列表
        """
        self.timeout = timeout
        self.keywords = keywords or STALL_KEYWORDS
        self._last_check_time = time.time()

    def check_timeout(
        self,
        last_node_timestamp: float,
        current_time: Optional[float] = None,
    ) -> Optional[StallEvent]:
        """
        超时检测：如果last_node_timestamp距今超过timeout，返回StallEvent。

        Args:
            last_node_timestamp: 最后一个节点的created_at时间戳
            current_time: 当前时间（默认time.time()）

        Returns:
            StallEvent或None
        """
        now = current_time or time.time()
        elapsed = now - last_node_timestamp
        if elapsed >= self.timeout:
            return StallEvent(
                detected_at=now,
                reason="timeout",
                round_index=0,
                agent_output_preview=f"(no new nodes for {elapsed:.1f}s)",
            )
        return None

    def check_semantic(self, round_data: Round) -> Optional[StallEvent]:
        """
        语义检测：检查agent_output中是否出现卡点关键词。

        Args:
            round_data: 当前轮次数据

        Returns:
            StallEvent或None
        """
        text = round_data.agent_output
        text_lower = text.lower()
        for kw in self.keywords:
            if kw.lower() in text_lower:
                return StallEvent(
                    detected_at=time.time(),
                    reason="semantic",
                    keyword=kw,
                    round_index=round_data.round_index,
                    agent_output_preview=text[:200],
                )
        return None

    def check(
        self,
        last_node_timestamp: float,
        round_data: Optional[Round] = None,
        current_time: Optional[float] = None,
    ) -> Optional[StallEvent]:
        """
        综合检测：先语义检测，再超时检测。

        Args:
            last_node_timestamp: 最后一个节点的时间戳
            round_data: 当前轮次数据（可选，用于语义检测）
            current_time: 当前时间

        Returns:
            StallEvent或None
        """
        # 优先语义检测（更快触发）
        if round_data is not None:
            event = self.check_semantic(round_data)
            if event:
                return event

        # 超时检测
        event = self.check_timeout(last_node_timestamp, current_time)
        return event
