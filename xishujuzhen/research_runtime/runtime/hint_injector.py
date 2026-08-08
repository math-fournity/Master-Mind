"""
HintInjector: 把选中的提示通过tmux send-keys注入到Solver session。

基于264号§6.1验证结果：devin cli交互模式支持运行时输入。
注入需要两步send-keys：
  步骤1：tmux send-keys -t <session> "提示文本" Enter  → 排队消息
  步骤2：tmux send-keys -t <session> Enter              → 发送排队消息

前提条件：solver-harness的launch命令必须用--interactive模式启动，
否则devin cli在单轮模式（-p）下不接受运行时输入。
"""

import subprocess
import time
from typing import Optional


class HintInjector:
    """通过tmux send-keys把提示注入到Solver的devin cli交互session。"""

    def __init__(self, exp_id: str):
        self.exp_id = exp_id
        self.tmux_session = f"harness-{exp_id}"
        self.injected_hints: list = []  # 记录已注入的提示（用于审计）

    def inject(self, hint_text: str) -> bool:
        """把提示注入到Solver session。

        Args:
            hint_text: 提示文本（自然语言，引导AI思考而非给答案）

        Returns:
            True if injection succeeded, False otherwise
        """
        # 检查tmux session是否存在
        if not self._session_exists():
            print(f"ERROR: tmux session {self.tmux_session} not found")
            return False

        # 步骤1：排队消息
        # 注意：send-keys的Enter是tmux的key name，不是字符串
        result1 = subprocess.run(
            ["tmux", "send-keys", "-t", self.tmux_session, hint_text, "Enter"],
            capture_output=True, text=True
        )
        if result1.returncode != 0:
            print(f"ERROR: send-keys step 1 failed: {result1.stderr}")
            return False

        # 短暂等待，让devin cli处理排队
        time.sleep(0.5)

        # 步骤2：发送排队消息（在空输入行按Enter）
        result2 = subprocess.run(
            ["tmux", "send-keys", "-t", self.tmux_session, "Enter"],
            capture_output=True, text=True
        )
        if result2.returncode != 0:
            print(f"ERROR: send-keys step 2 failed: {result2.stderr}")
            return False

        # 记录注入（审计用）
        self.injected_hints.append({
            "timestamp": time.time(),
            "hint_text": hint_text,
        })

        print(f"Hint injected to {self.tmux_session}: {hint_text[:100]}...")
        return True

    def _session_exists(self) -> bool:
        """检查tmux session是否存在。"""
        result = subprocess.run(
            ["tmux", "has-session", "-t", self.tmux_session],
            capture_output=True
        )
        return result.returncode == 0

    def get_injection_log(self) -> list:
        """获取注入历史（用于审计和A/B对照分析）。"""
        return list(self.injected_hints)
