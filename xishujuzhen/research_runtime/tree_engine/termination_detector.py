"""TerminationDetector: 检测推理AI是否自然终止。

与stall_detector的区别：
  stall_detector（阶段1）：检测AI卡住→触发提示注入
  termination_detector（阶段2）：检测AI终止→触发节点提取+检索+启动新AI

终止检测逻辑：
  1. session_ended: tmux has-session返回false→AI进程已退出
  2. crash: pane含"Connection failed"/"Error"→进程崩溃
  3. response_truncated: pane最后8行含"Response truncated"→AI token用尽
  4. timeout: sessions.db无新node超过timeout秒→可能卡死

优先级：session_ended > crash > response_truncated > timeout

注意：不再依赖thinking_readable.txt（MITM不可靠），
改为检查sessions.db的message_nodes表是否有新node。
"""

import os
import subprocess
import sqlite3
import time
from dataclasses import dataclass
from typing import Optional


@dataclass
class TerminationEvent:
    """检测到的AI终止事件。"""
    detected_at: float
    reason: str          # session_ended/crash/response_truncated/timeout
    tmux_session: str
    details: str = ""    # 额外信息


# 终止检测的默认超时（秒）——比stall_detector的30秒更长
# 阶段2中AI不需要被中断，给它更多时间自然终止
# 注意：AI的thinking block可能持续2-5分钟，所以timeout要足够长
DEFAULT_TERMINATION_TIMEOUT = 180.0

# 崩溃关键词
CRASH_KEYWORDS = [
    "Connection failed",
    "Connection error",
    "Error:",
    "Fatal error",
    "Process crashed",
]

# 截断关键词
TRUNCATED_KEYWORDS = [
    "Response truncated",
    "Send a message to continue",
]

# sessions.db路径
SESSIONS_DB_PATH = os.path.expanduser("~/.local/share/devin/cli/sessions.db")


class TerminationDetector:
    """
    AI终止检测器。

    用法：
        detector = TerminationDetector(timeout=180.0, devin_session_id="bird-sodalite")
        event = detector.check_terminated("harness-exp1", "exp1")
        if event:
            print(f"AI终止: {event.reason}")
            # 触发节点提取+检索+启动新AI...
    """

    def __init__(self, timeout: float = DEFAULT_TERMINATION_TIMEOUT,
                 devin_session_id: str = ""):
        """
        Args:
            timeout: 超时阈值（秒），sessions.db无新node超过此值视为终止
            devin_session_id: devin cli的session ID（用于检查sessions.db活动）
        """
        self.timeout = timeout
        self.devin_session_id = devin_session_id
        self._last_node_count = 0
        self._last_activity_time = time.time()

    def set_session_id(self, devin_session_id: str):
        """设置devin session ID（在AI启动后回填时调用）。"""
        self.devin_session_id = devin_session_id
        self._last_node_count = self._get_node_count()
        self._last_activity_time = time.time()

    def check_terminated(
        self,
        tmux_session: str,
        exp_id: str,
        trajectory_base: str = "/data/grove-agents-trajectory",
    ) -> Optional[TerminationEvent]:
        """
        检测AI是否终止。

        Args:
            tmux_session: tmux session名
            exp_id: 实验ID（未使用，保留兼容）
            trajectory_base: trajectory存储根目录（未使用，保留兼容）

        Returns:
            TerminationEvent（如已终止）或None（仍在运行）
        """
        now = time.time()

        # 1. 检查tmux session是否还存在
        if not self._tmux_session_exists(tmux_session):
            return TerminationEvent(
                detected_at=now,
                reason="session_ended",
                tmux_session=tmux_session,
                details="tmux session已退出，AI进程结束",
            )

        # 2. 检查pane内容是否有崩溃/截断标志
        pane = self._capture_pane(tmux_session, lines=15)
        if pane:
            # 检查崩溃
            for kw in CRASH_KEYWORDS:
                if kw in pane:
                    return TerminationEvent(
                        detected_at=now,
                        reason="crash",
                        tmux_session=tmux_session,
                        details=f"检测到崩溃关键词: {kw}",
                    )

            # 检查截断（最后8行）
            lines_list = pane.strip().split("\n")
            last_8 = "\n".join(lines_list[-8:]) if len(lines_list) >= 8 else pane
            for kw in TRUNCATED_KEYWORDS:
                if kw in last_8:
                    return TerminationEvent(
                        detected_at=now,
                        reason="response_truncated",
                        tmux_session=tmux_session,
                        details=f"检测到截断标志: {kw}",
                    )

        # 3. 检查sessions.db是否有新node（替代thinking_readable.txt）
        if self.devin_session_id:
            current_count = self._get_node_count()
            if current_count > self._last_node_count:
                # 有新node→AI还在活动
                self._last_node_count = current_count
                self._last_activity_time = now
            elif (now - self._last_activity_time) > self.timeout:
                return TerminationEvent(
                    detected_at=now,
                    reason="timeout",
                    tmux_session=tmux_session,
                    details=f"sessions.db {self.timeout:.0f}秒无新node",
                )
        else:
            # 没有devin_session_id——只靠tmux session检测
            pass

        return None

    def _get_node_count(self) -> int:
        """获取当前session的node数量。"""
        if not self.devin_session_id:
            return 0
        try:
            conn = sqlite3.connect(SESSIONS_DB_PATH)
            c = conn.cursor()
            c.execute(
                "SELECT count(*) FROM message_nodes WHERE session_id=?",
                (self.devin_session_id,),
            )
            count = c.fetchone()[0]
            conn.close()
            return count
        except Exception:
            return 0

    def _tmux_session_exists(self, session_name: str) -> bool:
        """检查tmux session是否存在。"""
        result = subprocess.run(
            ["tmux", "has-session", "-t", session_name],
            capture_output=True,
        )
        return result.returncode == 0

    def _capture_pane(self, session_name: str, lines: int = 15) -> str:
        """捕获tmux pane内容。"""
        try:
            result = subprocess.run(
                ["tmux", "capture-pane", "-t", session_name, "-p", "-S", f"-{lines}"],
                capture_output=True, text=True,
            )
            return result.stdout
        except Exception:
            return ""

    def reset(self):
        """重置状态（用于监控新的AI实例）。"""
        self._last_node_count = 0
        self._last_activity_time = time.time()
        self.devin_session_id = ""
