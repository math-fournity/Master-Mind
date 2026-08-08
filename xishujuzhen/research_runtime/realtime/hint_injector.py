"""HintInjector: 提示注入机制（04工作线§2.5）。

把选中的提示通过tmux send-keys注入到Solver的devin cli session中。

注入时序控制：
1. 检测到卡点后，等待Solver完成当前输出（tmux pane空闲）
2. 在Solver的下一次输入前注入提示
3. 注入后等待Solver响应，不重复注入

注入方式：
  tmux send-keys -t <session> "<hint text>" Enter

注意：
- 提示文本可能多行，需要逐行send-keys后统一发Enter
- devin cli的输入框可能需要先按Enter进入输入模式
- 注入前检查tmux session是否存在
"""

import subprocess
import time
from typing import Optional


class HintInjector:
    """
    提示注入器：通过tmux send-keys注入提示到Solver session。

    用法：
        injector = HintInjector(tmux_session="harness-exp001")
        success = injector.inject("考虑一下稳定性方程的结构...")
    """

    def __init__(
        self,
        tmux_session: str,
        wait_idle: float = 2.0,
        verify_injection: bool = True,
    ):
        """
        Args:
            tmux_session: tmux session名（如"harness-exp001"）
            wait_idle: 注入前等待pane空闲的时间（秒）
            verify_injection: 是否验证注入成功（检查pane内容）
        """
        self.tmux_session = tmux_session
        self.wait_idle = wait_idle
        self.verify_injection = verify_injection
        self._last_injected_at: float = 0
        self._injection_count: int = 0

    def session_exists(self) -> bool:
        """检查tmux session是否存在。"""
        try:
            result = subprocess.run(
                ["tmux", "has-session", "-t", self.tmux_session],
                capture_output=True,
            )
            return result.returncode == 0
        except Exception:
            return False

    def capture_pane(self, lines: int = 20) -> str:
        """捕获tmux pane的当前内容。"""
        try:
            result = subprocess.run(
                ["tmux", "capture-pane", "-t", self.tmux_session, "-p", "-S", f"-{lines}"],
                capture_output=True,
                text=True,
            )
            return result.stdout
        except Exception:
            return ""

    def is_pane_idle(self) -> bool:
        """
        检查pane是否空闲（Solver不在输出中）。

        简化判断：捕获pane内容，检查最后一行是否是输入提示符。
        devin cli空闲时最后一行通常是空行或提示符。
        """
        pane = self.capture_pane(lines=5)
        if not pane:
            return True
        lines = pane.strip().split("\n")
        if not lines:
            return True
        # 简化判断：最后一行是空行或短行（提示符）
        last_line = lines[-1].strip()
        return len(last_line) < 50

    def inject(self, hint_text: str) -> bool:
        """
        注入提示到Solver session。

        Args:
            hint_text: 提示文本（可能多行）

        Returns:
            True if注入成功
        """
        if not self.session_exists():
            print(f"[HintInjector] tmux session '{self.tmux_session}' 不存在")
            return False

        # 等待pane空闲
        if self.wait_idle > 0:
            time.sleep(self.wait_idle)

        # 注入前捕获pane（用于验证）
        before_pane = self.capture_pane(lines=10) if self.verify_injection else ""

        # 逐行send-keys
        lines = hint_text.strip().split("\n")
        try:
            for line in lines:
                subprocess.run(
                    ["tmux", "send-keys", "-t", self.tmux_session, line],
                    check=True,
                    capture_output=True,
                )

            # 发送Enter提交
            subprocess.run(
                ["tmux", "send-keys", "-t", self.tmux_session, "Enter"],
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"[HintInjector] send-keys失败: {e}")
            return False

        self._last_injected_at = time.time()
        self._injection_count += 1

        # 验证注入
        if self.verify_injection:
            time.sleep(1.0)  # 等待1秒让pane更新
            after_pane = self.capture_pane(lines=15)
            if after_pane == before_pane:
                print("[HintInjector] 警告：注入后pane内容未变化")
                # 不返回False——可能只是渲染延迟

        print(f"[HintInjector] 注入成功 (#{self._injection_count}): {hint_text[:80]}...")
        return True

    @property
    def injection_count(self) -> int:
        """已注入次数。"""
        return self._injection_count

    @property
    def last_injected_at(self) -> float:
        """上次注入时间。"""
        return self._last_injected_at
