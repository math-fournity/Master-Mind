"""
parser: 自然语言→结构化表示的解析器（260号攻关方案）

LLM粗解析 + SymPy精确验证的混合解析器。
从工作智能体的自然语言推理输出中，解析出结构化语义表示：
- 语义事件序列（供给event-sourcing）
- 思维轨迹图节点和边（供给thinking-trajectory-graph）
- 六元组状态（供给dynamic-workspace）

对应260号§5.1的模块划分。
"""

from .models import (
    ParseRequest,
    ParseResult,
    MathObject,
    TrajectoryNode,
    TrajectoryEdge,
    SixTuple,
    VerifiedProp,
    Conjecture,
    Obligation,
    Representation,
    Evidence,
    UnsolvedProblem,
    TurnRecord,
)
from .llm_parser import LLMParser
from .sympy_verifier import SympyVerifier
from .consistency_checker import ConsistencyChecker
from .parser import MathParser

__all__ = [
    # 数据结构
    "ParseRequest", "ParseResult",
    "MathObject", "TrajectoryNode", "TrajectoryEdge",
    "SixTuple", "VerifiedProp", "Conjecture", "Obligation",
    "Representation", "Evidence", "UnsolvedProblem",
    "TurnRecord",
    # 模块
    "LLMParser", "SympyVerifier", "ConsistencyChecker", "MathParser",
]
