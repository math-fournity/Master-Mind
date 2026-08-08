"""
解析器数据结构：260号§2的输入输出规格。

按260号§2.1定义ParseRequest（解析器输入），
按260号§2.2定义ParseResult（解析器输出），
以及其中各组件的详细格式（§2.3）。

复用已有的 models/event.py 中的 SemanticEvent 和 EventFactory，
不重新定义语义事件类型。
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

from ..models.event import SemanticEvent


# ---------------------------------------------------------------------------
# 数学对象
# ---------------------------------------------------------------------------

@dataclass
class MathObject:
    """
    数学对象的统一表示（260号§2.3.1）。

    包含名称、LaTeX、SymPy表达式、类型、变量列表、结构特征。
    SymPy验证后填充 sympy_verified 字段。
    """
    name: str                                   # 名称（如"稳定性方程"）
    latex: str                                  # LaTeX表示
    sympy_expr: Optional[str] = None            # SymPy可解析的表达式
    object_type: str = "equation"               # equation/variable/inequality/identity/definition
    variables: List[str] = field(default_factory=list)
    properties: Dict[str, str] = field(default_factory=dict)
    sympy_verified: bool = False                # 是否经过SymPy验证

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "latex": self.latex,
            "sympy_expr": self.sympy_expr,
            "object_type": self.object_type,
            "variables": list(self.variables),
            "properties": dict(self.properties),
            "sympy_verified": self.sympy_verified,
        }

    @classmethod
    def from_dict(cls, d) -> "MathObject":
        # 容错：devin cli可能返回字符串而非dict（如"方程(1)"）
        if isinstance(d, str):
            return cls(name=d, latex="", sympy_expr=None)
        return cls(
            name=d["name"],
            latex=d.get("latex", ""),
            sympy_expr=d.get("sympy_expr"),
            object_type=d.get("object_type", "equation"),
            variables=list(d.get("variables", [])),
            properties=dict(d.get("properties", {})),
            sympy_verified=d.get("sympy_verified", False),
        )


# ---------------------------------------------------------------------------
# 思维轨迹图节点和边
# ---------------------------------------------------------------------------

@dataclass
class TrajectoryNode:
    """
    思维轨迹图节点（260号§2.3.2）。

    10种节点类型：observation/claim/representation/subgoal/candidate/
    operation/tool_result/contradiction/stall/resolution。
    """
    node_id: str
    type: str                                   # 10种之一
    round_index: int
    content: str
    math_objects: List[MathObject] = field(default_factory=list)
    is_frontier: bool = False
    confidence: float = 1.0

    def to_dict(self) -> dict:
        return {
            "node_id": self.node_id,
            "type": self.type,
            "round_index": self.round_index,
            "content": self.content,
            "math_objects": [m.to_dict() for m in self.math_objects],
            "is_frontier": self.is_frontier,
            "confidence": self.confidence,
        }


@dataclass
class TrajectoryEdge:
    """
    思维轨迹图边（260号§2.3.2）。

    13种边类型：notice/infer/recall/transform/decompose/compare/test/
    reject/backtrack/generalize/analogize/ask_for_hint/activate。
    """
    source_id: str
    target_id: str
    edge_type: str
    description: str = ""

    def to_dict(self) -> dict:
        return {
            "source_id": self.source_id,
            "target_id": self.target_id,
            "edge_type": self.edge_type,
            "description": self.description,
        }


# ---------------------------------------------------------------------------
# 六元组状态
# ---------------------------------------------------------------------------

@dataclass
class VerifiedProp:
    """V_t条目：已验证核心命题"""
    statement: str
    math_objects: List[MathObject] = field(default_factory=list)
    verified_by: str = "logic"                  # logic/sympy/given
    verified_at_round: int = 0

    def to_dict(self) -> dict:
        return {
            "statement": self.statement,
            "math_objects": [m.to_dict() for m in self.math_objects],
            "verified_by": self.verified_by,
            "verified_at_round": self.verified_at_round,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "VerifiedProp":
        return cls(
            statement=d["statement"],
            math_objects=[MathObject.from_dict(m) for m in d.get("math_objects", [])],
            verified_by=d.get("verified_by", "logic"),
            verified_at_round=d.get("verified_at_round", 0),
        )


@dataclass
class Conjecture:
    """F_t条目：猜想前沿"""
    statement: str
    math_objects: List[MathObject] = field(default_factory=list)
    status: str = "exploring"                   # exploring/promising/weak

    def to_dict(self) -> dict:
        return {
            "statement": self.statement,
            "math_objects": [m.to_dict() for m in self.math_objects],
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Conjecture":
        return cls(
            statement=d["statement"],
            math_objects=[MathObject.from_dict(m) for m in d.get("math_objects", [])],
            status=d.get("status", "exploring"),
        )


@dataclass
class Obligation:
    """O_t条目：开放研究义务"""
    description: str
    obligation_type: str = "prove"              # prove/refute/construct/compute/compare/evaluate
    status: str = "open"                        # open/in_progress/solved/denied
    depends_on: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "obligation_type": self.obligation_type,
            "status": self.status,
            "depends_on": list(self.depends_on),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Obligation":
        return cls(
            description=d["description"],
            obligation_type=d.get("obligation_type", "prove"),
            status=d.get("status", "open"),
            depends_on=list(d.get("depends_on", [])),
        )


@dataclass
class Representation:
    """R_t条目：当前使用的表示形式"""
    name: str
    description: str = ""
    introduced_at_round: int = 0

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "introduced_at_round": self.introduced_at_round,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Representation":
        return cls(
            name=d["name"],
            description=d.get("description", ""),
            introduced_at_round=d.get("introduced_at_round", 0),
        )


@dataclass
class Evidence:
    """E_t条目：已积累的证据"""
    kind: str                                   # literature/numerical/symbolic/formal_proof/counterexample/human_audit
    content: str
    supports: str = ""

    def to_dict(self) -> dict:
        return {
            "kind": self.kind,
            "content": self.content,
            "supports": self.supports,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Evidence":
        # 容错：devin cli可能用不同的字段名
        if isinstance(d, str):
            return cls(kind="numerical", content=d)
        return cls(
            kind=d.get("kind", d.get("source", "numerical")),
            content=d.get("content", d.get("description", "")),
            supports=d.get("supports", ""),
        )


@dataclass
class UnsolvedProblem:
    """U_t条目：已识别但未解决的问题"""
    description: str
    severity: str = "minor"                     # blocking/minor/potential
    identified_at_round: int = 0

    def to_dict(self) -> dict:
        return {
            "description": self.description,
            "severity": self.severity,
            "identified_at_round": self.identified_at_round,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "UnsolvedProblem":
        return cls(
            description=d["description"],
            severity=d.get("severity", "minor"),
            identified_at_round=d.get("identified_at_round", 0),
        )


@dataclass
class SixTuple:
    """
    六元组状态（260号§2.3.3）：(V_t, F_t, O_t, R_t, E_t, U_t)。

    各字段用dataclass，支持增量更新。
    """
    V_t: List[VerifiedProp] = field(default_factory=list)
    F_t: List[Conjecture] = field(default_factory=list)
    O_t: List[Obligation] = field(default_factory=list)
    R_t: List[Representation] = field(default_factory=list)
    E_t: List[Evidence] = field(default_factory=list)
    U_t: List[UnsolvedProblem] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "V_t": [v.to_dict() for v in self.V_t],
            "F_t": [f.to_dict() for f in self.F_t],
            "O_t": [o.to_dict() for o in self.O_t],
            "R_t": [r.to_dict() for r in self.R_t],
            "E_t": [e.to_dict() for e in self.E_t],
            "U_t": [u.to_dict() for u in self.U_t],
        }

    @classmethod
    def from_dict(cls, d: dict) -> "SixTuple":
        return cls(
            V_t=[VerifiedProp.from_dict(v) for v in d.get("V_t", [])],
            F_t=[Conjecture.from_dict(v) for v in d.get("F_t", [])],
            O_t=[Obligation.from_dict(v) for v in d.get("O_t", [])],
            R_t=[Representation.from_dict(v) for v in d.get("R_t", [])],
            E_t=[Evidence.from_dict(v) for v in d.get("E_t", [])],
            U_t=[UnsolvedProblem.from_dict(v) for v in d.get("U_t", [])],
        )

    @classmethod
    def empty(cls) -> "SixTuple":
        """创建空六元组"""
        return cls()


# ---------------------------------------------------------------------------
# 单轮QA记录
# ---------------------------------------------------------------------------

@dataclass
class TurnRecord:
    """
    单轮QA记录（260号§2.1）。
    """
    q_text: str
    a_text: str
    q_level: float = 1.0
    q_non_specificity: float = 0.0
    parsed_events: List[SemanticEvent] = field(default_factory=list)
    round_index: int = 0

    def to_dict(self) -> dict:
        return {
            "q_text": self.q_text,
            "a_text": self.a_text,
            "q_level": self.q_level,
            "q_non_specificity": self.q_non_specificity,
            "round_index": self.round_index,
            "parsed_events": [e.to_dict() for e in self.parsed_events],
        }


# ---------------------------------------------------------------------------
# 解析器输入和输出
# ---------------------------------------------------------------------------

@dataclass
class ParseRequest:
    """
    解析器输入（260号§2.1）。
    """
    agent_output: str                           # 工作智能体本轮的自然语言推理输出
    round_index: int                            # 当前轮次
    problem_text: str                           # 题目原文
    history: List[TurnRecord] = field(default_factory=list)
    current_six_tuple: Optional[SixTuple] = None
    run_id: str = "test_run"
    model_version: str = "mock"
    timestamp: str = ""


@dataclass
class ParseResult:
    """
    解析器输出（260号§2.2）。

    核心输出：
    1. semantic_events —— 供给event-sourcing
    2. trajectory_nodes + trajectory_edges —— 供给thinking-trajectory-graph
    3. six_tuple —— 供给dynamic-workspace

    解析质量信息：
    - parse_confidence：整体解析置信度（0-1）
    - per_event_confidence：每个事件的解析置信度
    - sympy_verified：每个事件是否经过SymPy验证
    - parse_warnings：解析过程中的警告信息
    """
    semantic_events: List[SemanticEvent] = field(default_factory=list)
    trajectory_nodes: List[TrajectoryNode] = field(default_factory=list)
    trajectory_edges: List[TrajectoryEdge] = field(default_factory=list)
    six_tuple: SixTuple = field(default_factory=SixTuple)
    parse_confidence: float = 0.0
    per_event_confidence: List[float] = field(default_factory=list)
    sympy_verified: List[bool] = field(default_factory=list)
    parse_warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "semantic_events": [e.to_dict() for e in self.semantic_events],
            "trajectory_nodes": [n.to_dict() for n in self.trajectory_nodes],
            "trajectory_edges": [e.to_dict() for e in self.trajectory_edges],
            "six_tuple": self.six_tuple.to_dict(),
            "parse_confidence": self.parse_confidence,
            "per_event_confidence": list(self.per_event_confidence),
            "sympy_verified": list(self.sympy_verified),
            "parse_warnings": list(self.parse_warnings),
        }
