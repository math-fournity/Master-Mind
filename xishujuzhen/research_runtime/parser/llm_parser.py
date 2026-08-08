"""
LLM粗解析模块：260号§3.1。

按260号§3.1.2的prompt设计实现LLM粗解析。
先实现mock接口（返回预定义JSON），后续再接真实LLM API。
也实现一个真实LLM调用接口——用openai兼容的API，
从环境变量读取base_url和api_key。如果环境变量没设置，fallback到mock。
"""

import json
import os
from typing import Dict, Any, Optional, Callable

from .models import ParseRequest


# ---------------------------------------------------------------------------
# Prompt模板（260号§3.1.2）
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """你是一个数学推理过程的结构化解析器。你的任务是从工作智能体（做题AI）的自然语言推理输出中，解析出结构化的语义事件序列。

你需要识别14种语义事件类型：
1. OBSERVATION - 从题面或证据中注意到的事实
2. CLAIM - 当前认为成立的命题
3. REPRESENTATION - 引入新表示、新变量、新记号
4. SUBGOAL - 需要解决的子问题
5. CANDIDATE - 候选答案或方法
6. TEST - 正在尝试的思维动作（如数值实验、极端检验）
7. TOOL_RESULT - 工具返回结果
8. CONTRADICTION - 发现冲突
9. STALL - 停滞或重复
10. BACKTRACK - 回退或放弃方向
11. RESOLUTION - 已解决的局部结论（如导出恒等式、得到中间结果）
12. HINT_INJECTION - 系统提示注入（非工作智能体产出，通常忽略）
13. STATE_REDUCTION - 状态归约（系统内部事件，通常忽略）
14. VERIFICATION - 验证结果

你需要识别10种思维轨迹图节点类型：
observation, claim, representation, subgoal, candidate, operation, tool_result, contradiction, stall, resolution

你需要归约六元组状态：
- V_t（已验证核心）：已被逻辑确认的数学事实
- F_t（猜想前沿）：正在探索但未验证的命题
- O_t（开放义务）：待解决子目标
- R_t（表示状态）：当前使用的表示形式
- E_t（证据）：已积累的证据
- U_t（未解决问题）：已识别但未解决的问题

对于每个数学对象，提取：
- name: 名称
- latex: LaTeX表示
- sympy_expr: SymPy可解析的表达式（用Python语法，如 5*D - 3*sqrt(5)*(B_r - B_s) - 2*C）
- object_type: equation/variable/inequality/identity/definition
- variables: 涉及的变量列表
- properties: 结构特征（如 {"depends_on_integers": "k,n"}）

请只输出JSON，不要输出其他内容。"""


USER_PROMPT_TEMPLATE = """## 题目
{problem_text}

## 历史QA（简要）
{history_summary}

## 上一轮六元组状态
{previous_six_tuple_json}

## 本轮工作智能体输出（A{round_index}）
{agent_output}

## 请输出JSON
请从上面的工作智能体输出中解析出结构化语义表示，输出以下JSON格式：

{{
  "semantic_events": [
    {{
      "type": "RESOLUTION",
      "description": "导出稳定性方程(3)",
      "raw_text_span": "由Σxᵢq(xᵢ)=0 → 5D = 3√5(B_r-B_s) + 2C ... (3)",
      "math_objects": [
        {{
          "name": "稳定性方程",
          "latex": "5D = 3\\\\sqrt{{5}}(B_r - B_s) + 2C",
          "sympy_expr": "Eq(5*D, 3*sqrt(5)*(B_r - B_s) + 2*C)",
          "object_type": "equation",
          "variables": ["D", "B_r", "B_s", "C"],
          "properties": {{}}
        }}
      ],
      "depends_on": [],
      "confidence": 0.9
    }}
  ],
  "trajectory_nodes": [
    {{
      "type": "resolution",
      "content": "稳定性方程5D=3√5(B_r-B_s)+2C",
      "math_objects": ["稳定性方程"],
      "is_frontier": true,
      "confidence": 0.9
    }}
  ],
  "trajectory_edges": [
    {{
      "source_type": "representation",
      "target_type": "resolution",
      "edge_type": "infer",
      "description": "从投影表示推出稳定性方程"
    }}
  ],
  "six_tuple": {{
    "V_t": [
      {{"statement": "中心化结果", "verified_by": "logic", "verified_at_round": 1}}
    ],
    "F_t": [
      {{"statement": "稳定性方程", "status": "exploring"}}
    ],
    "O_t": [
      {{"description": "估计D的下界", "obligation_type": "prove", "status": "open"}}
    ],
    "R_t": [
      {{"name": "投影到根", "description": "ζᵢ∈{{r,s}}", "introduced_at_round": 6}}
    ],
    "E_t": [],
    "U_t": [
      {{"description": "D的量级问题", "severity": "blocking"}}
    ]
  }},
  "parse_confidence": 0.85,
  "parse_warnings": []
}}"""


def build_history_summary(history, max_rounds: int = 3) -> str:
    """
    构建历史QA的简要摘要（260号§5.4.2）。

    只传入最近max_rounds轮的Q和A的摘要，控制token用量。
    """
    if not history:
        return "（无历史）"
    recent = history[-max_rounds:]
    lines = []
    for turn in recent:
        q_preview = turn.q_text[:100].replace("\n", " ")
        a_preview = turn.a_text[:200].replace("\n", " ")
        lines.append(
            f"Q{turn.round_index}(L{turn.q_level}): {q_preview}..."
        )
        lines.append(
            f"A{turn.round_index}: {a_preview}..."
        )
    return "\n".join(lines)


def build_user_prompt(request: ParseRequest) -> str:
    """构建用户提示词"""
    history_summary = build_history_summary(request.history)
    if request.current_six_tuple is not None:
        six_tuple_json = json.dumps(
            request.current_six_tuple.to_dict(), ensure_ascii=False, indent=2
        )
    else:
        six_tuple_json = "（无上一轮六元组，首轮解析）"

    return USER_PROMPT_TEMPLATE.format(
        problem_text=request.problem_text,
        history_summary=history_summary,
        previous_six_tuple_json=six_tuple_json,
        round_index=request.round_index,
        agent_output=request.agent_output,
    )


# ---------------------------------------------------------------------------
# LLM解析器
# ---------------------------------------------------------------------------

class LLMParser:
    """
    LLM粗解析模块（260号§3.1）。

    调用LLM，返回JSON。先实现mock接口，后续接真实LLM API。
    如果环境变量PARSER_LLM_BASE_URL和PARSER_LLM_API_KEY设置了，
    用openai兼容的API调用真实LLM；否则fallback到mock。
    """

    def __init__(
        self,
        mock_response_provider: Optional[Callable[[ParseRequest], dict]] = None,
        model: str = "glm-5.2",
    ):
        """
        Args:
            mock_response_provider: mock响应提供函数。
                输入ParseRequest，返回预定义的JSON dict。
                如果为None，则尝试用真实LLM；真实LLM也不可用则返回降级JSON。
            model: LLM模型名。
        """
        self.mock_response_provider = mock_response_provider
        self.model = model
        self.base_url = os.environ.get("PARSER_LLM_BASE_URL")
        self.api_key = os.environ.get("PARSER_LLM_API_KEY")

    def parse(self, request: ParseRequest) -> dict:
        """
        调用LLM做粗解析，返回JSON dict（260号§3.1）。

        优先级：
        1. 如果设置了mock_response_provider，用mock（用于测试）
        2. 否则如果环境变量设置了base_url和api_key，用真实LLM
        3. 否则fallback到mock（降级为纯OBSERVATION事件）

        Returns:
            LLM输出的JSON dict，包含semantic_events/trajectory_nodes/
            trajectory_edges/six_tuple/parse_confidence/parse_warnings。
        """
        # 优先用mock_response_provider（测试用）
        if self.mock_response_provider is not None:
            return self.mock_response_provider(request)

        # 尝试用真实LLM
        if self.base_url and self.api_key:
            try:
                return self._call_real_llm(request)
            except Exception as e:
                # LLM调用失败，降级处理（260号§5.3）
                return self._fallback_response(
                    request, f"LLM调用失败: {e}"
                )

        # 无mock也无真实LLM，降级处理
        return self._fallback_response(
            request, "无LLM可用（mock_response_provider未设置，环境变量未配置），降级为纯OBSERVATION事件"
        )

    def _call_real_llm(self, request: ParseRequest) -> dict:
        """
        用openai兼容的API调用真实LLM。

        从环境变量读取base_url和api_key。
        温度0.0-0.1（解析是确定性任务）。
        """
        try:
            from openai import OpenAI
        except ImportError:
            raise RuntimeError("openai库未安装，无法调用真实LLM")

        client = OpenAI(base_url=self.base_url, api_key=self.api_key)
        user_prompt = build_user_prompt(request)

        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content
        return json.loads(content)

    def _fallback_response(self, request: ParseRequest, warning: str) -> dict:
        """
        降级处理（260号§5.3）。

        LLM不可用时，把整段输出作为单个OBSERVATION事件，
        parse_confidence=0.3。
        """
        return {
            "semantic_events": [
                {
                    "type": "OBSERVATION",
                    "description": f"A{request.round_index}的完整输出（降级处理）",
                    "raw_text_span": request.agent_output[:200],
                    "math_objects": [],
                    "depends_on": [],
                    "confidence": 0.3,
                }
            ],
            "trajectory_nodes": [
                {
                    "type": "observation",
                    "content": f"A{request.round_index}的完整输出",
                    "math_objects": [],
                    "is_frontier": True,
                    "confidence": 0.3,
                }
            ],
            "trajectory_edges": [],
            "six_tuple": (
                request.current_six_tuple.to_dict()
                if request.current_six_tuple is not None
                else SixTuple.empty().to_dict()
            ),
            "parse_confidence": 0.3,
            "parse_warnings": [warning],
        }


# 延迟导入，避免循环引用
from .models import SixTuple  # noqa: E402
