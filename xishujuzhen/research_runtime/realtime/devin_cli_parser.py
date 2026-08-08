"""DevinCliParserProvider: 用devin cli作为parser的LLM。

替代外部LLM API（OpenAI兼容接口），直接用`devin -p`调用devin cli
来执行260号§3.1的LLM粗解析任务。

工作方式：
  1. 接收ParseRequest
  2. 构建260号§3.1.2的system prompt + user prompt
  3. 通过`devin -p`发送给devin cli（在独立的parser工作目录中运行）
  4. 捕获devin cli的stdout（应为JSON格式）
  5. 解析JSON，返回dict

与LLMParser的接口兼容：
  LLMParser(mock_response_provider=DevinCliParserProvider())
  → provider(request) → dict

设计决策：
- parser的devin cli在独立工作目录运行（不复用Solver的工作目录）
- parser的devin cli用`-p`单轮模式（不需要交互）
- parser的devin cli不需要MITM（不采集trajectory）
- parser的devin cli用`--permission-mode dangerous`（需要exec权限做SymPy验证）
"""

import json
import os
import re
import subprocess
import time
from typing import Optional, Dict, Any

from ..parser.llm_parser import build_user_prompt, SYSTEM_PROMPT
from ..parser.models import ParseRequest


# Parser专用的devin cli工作目录（独立于Solver工作目录）
PARSER_WORK_DIRS = [
    "/data/grove-parser-1",
    "/data/grove-parser-2",
    "/data/grove-parser-3",
]


class DevinCliParserProvider:
    """
    用devin cli作为parser的LLM provider。

    实现LLMParser的mock_response_provider接口：
    输入ParseRequest，返回JSON dict。

    用法：
        provider = DevinCliParserProvider()
        llm_parser = LLMParser(mock_response_provider=provider)
        math_parser = MathParser(llm_parser=llm_parser)
    """

    def __init__(
        self,
        model: str = "glm-5-2",
        work_dir: Optional[str] = None,
        timeout: int = 120,
        max_retries: int = 2,
    ):
        """
        Args:
            model: devin cli模型名
            work_dir: parser的devin cli工作目录
                      如果为None，自动选择或创建第一个PARSER_WORK_DIRS
            timeout: 单次devin cli调用超时（秒）
            max_retries: JSON解析失败时的重试次数
        """
        self.model = model
        self.timeout = timeout
        self.max_retries = max_retries

        # 选择工作目录
        if work_dir:
            self.work_dir = work_dir
        else:
            self.work_dir = self._ensure_work_dir()

    def _ensure_work_dir(self) -> str:
        """确保parser工作目录存在且有AGENTS.md。"""
        for d in PARSER_WORK_DIRS:
            if os.path.isdir(d):
                # 检查是否有AGENTS.md
                agents_md = os.path.join(d, "AGENTS.md")
                if os.path.exists(agents_md):
                    return d
                # 目录存在但没有AGENTS.md，创建一个
                self._write_parser_agents_md(d)
                return d

        # 都不存在，创建第一个
        d = PARSER_WORK_DIRS[0]
        os.makedirs(d, exist_ok=True)
        self._write_parser_agents_md(d)
        return d

    def _write_parser_agents_md(self, work_dir: str):
        """写parser专用的AGENTS.md。"""
        agents_md = os.path.join(work_dir, "AGENTS.md")
        with open(agents_md, "w") as f:
            f.write("""# Parser Agent AGENTS.md · 数学推理过程解析器

你是数学大师系统的 **Parser** 角色——一个结构化解析器。

## 你的职责

- 读取工作智能体（做题AI）的自然语言推理输出
- 解析出结构化的语义事件序列、思维轨迹图节点、六元组状态
- 输出严格的JSON格式

## 工作方式

- 直接解析文本，不要做数学题
- 只输出JSON，不要输出其他内容
- 严格按照给定的JSON schema输出

## 工具使用

- 不需要使用任何工具
- 直接分析文本，输出JSON
""")

    def __call__(self, request: ParseRequest) -> dict:
        """
        调用devin cli执行LLM粗解析。

        Args:
            request: ParseRequest

        Returns:
            LLM输出的JSON dict
        """
        # 构建prompt
        user_prompt = build_user_prompt(request)
        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"

        # 调用devin cli
        for attempt in range(self.max_retries + 1):
            try:
                response_text = self._call_devin_cli(full_prompt)
                # 尝试解析JSON
                result = self._extract_json(response_text)
                if result is not None:
                    return result

                # JSON解析失败，重试（加提示要求纯JSON输出）
                if attempt < self.max_retries:
                    print(f"[DevinCliParser] JSON解析失败(尝试{attempt+1}/{self.max_retries+1})，重试...")
                    full_prompt = full_prompt + "\n\n注意：请只输出JSON，不要输出其他内容。"
                    time.sleep(1)
                else:
                    # 最后一次也失败，返回降级JSON
                    print(f"[DevinCliParser] JSON解析失败，返回降级JSON")
                    return self._fallback_response(request)

            except subprocess.TimeoutExpired:
                print(f"[DevinCliParser] devin cli超时({self.timeout}s)")
                if attempt < self.max_retries:
                    time.sleep(2)
                else:
                    return self._fallback_response(request)

            except Exception as e:
                print(f"[DevinCliParser] 调用失败: {e}")
                if attempt < self.max_retries:
                    time.sleep(2)
                else:
                    return self._fallback_response(request)

        return self._fallback_response(request)

    def _call_devin_cli(self, prompt: str) -> str:
        """调用devin -p，返回stdout文本。"""
        cmd = [
            "devin", "-p", prompt,
            "--model", self.model,
            "--respect-workspace-trust", "false",
            "--permission-mode", "dangerous",
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=self.timeout,
            cwd=self.work_dir,
        )

        output = result.stdout.strip()
        if result.returncode != 0:
            stderr = result.stderr[:500]
            raise RuntimeError(f"devin cli返回码{result.returncode}: {stderr}")

        return output

    def _extract_json(self, text: str) -> Optional[dict]:
        """
        从devin cli的输出中提取JSON。

        devin cli的输出可能包含：
        1. 纯JSON（理想情况）
        2. JSON前后有markdown代码块标记（```json ... ```）
        3. JSON前后有其他文本

        尝试多种方式提取JSON。
        """
        # 尝试1: 直接解析
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # 尝试2: 从markdown代码块中提取
        json_block = re.search(r'```(?:json)?\s*\n(.*?)\n```', text, re.DOTALL)
        if json_block:
            try:
                return json.loads(json_block.group(1))
            except json.JSONDecodeError:
                pass

        # 尝试3: 找第一个{和最后一个}之间的内容
        first_brace = text.find('{')
        last_brace = text.rfind('}')
        if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
            json_str = text[first_brace:last_brace + 1]
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass

        # 尝试4: 找第一个[和最后一个]之间的内容（数组情况）
        first_bracket = text.find('[')
        last_bracket = text.rfind(']')
        if first_bracket != -1 and last_bracket != -1 and last_bracket > first_bracket:
            json_str = text[first_bracket:last_bracket + 1]
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass

        return None

    def _fallback_response(self, request: ParseRequest) -> dict:
        """
        降级响应：当devin cli调用失败或JSON解析失败时，
        返回一个最小的有效JSON。
        """
        return {
            "semantic_events": [
                {
                    "type": "OBSERVATION",
                    "description": f"轮次{request.round_index}的输出（解析降级）",
                    "raw_text_span": request.agent_output[:200],
                    "confidence": 0.3,
                    "math_objects": [],
                    "depends_on": [],
                }
            ],
            "trajectory_nodes": [
                {
                    "type": "observation",
                    "content": request.agent_output[:200],
                    "is_frontier": True,
                    "confidence": 0.3,
                    "math_objects": [],
                }
            ],
            "trajectory_edges": [],
            "six_tuple": {
                "V_t": [],
                "F_t": [],
                "O_t": [],
                "R_t": [],
                "E_t": [],
                "U_t": [
                    {
                        "description": "解析降级，无法识别具体问题",
                        "severity": "minor",
                        "identified_at_round": request.round_index,
                    }
                ],
            },
            "parse_confidence": 0.3,
            "parse_warnings": ["devin cli parser fallback: JSON解析失败或调用超时"],
        }
