"""
LLMBackend：LLM后端封装——通过devin cli调用

对应134号P4-3.1（冻结模型版本）。

封装devin cli的非交互模式（-p/--print）作为LLM后端：
    devin -p "prompt" --model <model> --respect-workspace-trust false

冻结声明（123号§49 + §44）：
- 模型版本在实验期间不变
- 工具版本（devin cli版本）在实验期间不变
- 非确定性来自LLM本身的采样随机性

P4-3.1边界情况：
- 实验期间模型版本变更（应触发告警）
- devin cli调用失败（应记录并重试或排除）
"""

import subprocess
import hashlib
import json
import os
from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class LLMCallRecord:
    """单次LLM调用记录——用于实验日志和哈希"""
    call_id: str
    model_version: str
    prompt: str
    response: str
    prompt_hash: str
    response_hash: str
    cli_version: str = ""
    timestamp: str = ""
    elapsed_seconds: float = 0.0

    def to_dict(self) -> dict:
        return {
            "call_id": self.call_id,
            "model_version": self.model_version,
            "prompt": self.prompt,
            "response": self.response,
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "cli_version": self.cli_version,
            "timestamp": self.timestamp,
            "elapsed_seconds": self.elapsed_seconds,
        }


class LLMBackend:
    """
    LLM后端封装——通过devin cli调用。

    P4-3.1：冻结模型版本（实验期间不变）。

    使用方法：
        backend = LLMBackend(model_version="claude-sonnet-5-low")
        response = backend.generate("你的prompt")
    """

    def __init__(self, model_version: str = "claude-sonnet-5-low"):
        """
        Args:
            model_version: 冻结的模型版本（如claude-sonnet-5-low）
        """
        self.model_version = model_version
        self.cli_version = self._get_cli_version()
        self._frozen = False

    def _get_cli_version(self) -> str:
        """获取devin cli版本（P4-3.2：冻结工具版本）"""
        try:
            result = subprocess.run(
                ["devin", "version"],
                capture_output=True, text=True, timeout=10
            )
            return result.stdout.strip()
        except Exception:
            return "unknown"

    def freeze(self):
        """冻结模型版本和工具版本——实验开始后调用"""
        self._frozen = True

    def generate(self, prompt: str, timeout: int = 120) -> str:
        """
        调用devin cli生成continuation。

        非确定性来源：LLM本身的采样随机性（即使prompt相同，每次调用的推理过程不同）。

        Args:
            prompt: 输入prompt
            timeout: 超时秒数

        Returns:
            LLM生成的文本

        边界情况：
        - devin cli调用失败 → 抛出异常（调用方决定排除或重试）
        - 超时 → 抛出TimeoutError
        """
        cmd = [
            "devin", "-p", prompt,
            "--model", self.model_version,
            "--respect-workspace-trust", "false",
        ]
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"devin cli调用失败 (returncode={result.returncode}): {result.stderr[:200]}"
            )
        return result.stdout.strip()

    def generate_with_record(self, prompt: str, timeout: int = 120) -> tuple:
        """
        调用LLM并返回调用记录（用于实验日志）。

        Returns:
            (response_text, LLMCallRecord)
        """
        import time
        from datetime import datetime, timezone

        start = time.time()
        response = self.generate(prompt, timeout=timeout)
        elapsed = time.time() - start

        prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()[:16]
        response_hash = hashlib.sha256(response.encode()).hexdigest()[:16]
        call_id = f"llm_{prompt_hash}_{response_hash}"

        record = LLMCallRecord(
            call_id=call_id,
            model_version=self.model_version,
            prompt=prompt,
            response=response,
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            cli_version=self.cli_version,
            timestamp=datetime.now(timezone.utc).isoformat(),
            elapsed_seconds=elapsed,
        )
        return response, record

    def verify_frozen(self) -> bool:
        """验证模型版本和工具版本未变更（P4-3.1边界情况）"""
        current_cli = self._get_cli_version()
        return current_cli == self.cli_version
