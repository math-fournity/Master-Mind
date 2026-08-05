"""
HeuristicRule schema: 127号§7冻结定义

123号§21：启发先实现为类型化时序模式—动作规则
h = (p, g, a, η)
- p: LHS 匹配模式
- g: interface guard条件
- a: RHS 动作（激活包）
- η: eta 效果后验

冻结声明（127号§7）：
- 模式匹配必须返回被匹配实体、字段约束和时间窗口
- 动作只能提出候选状态扩展，真正写入V_t仍需Reducer与Verifier
- 激活包不应直接把目标结论加入V_t
- 原先的L←I→R只保留为未来DPO研究方向，首版不借用DPO记号冒充已完成形式化

生命周期状态（127号§9）：
- candidate: 离线发现，禁止在线自动提示、禁止自动写入H图
- validated: 通过DYN-3因果实验+泄漏门
- published: 通过DYN-5跨题跨模型迁移
- retired: 模型漂移/反例/更好规则替代

F4防线：HeuristicRule.status和Evidence.status是不同schema的不同字段，
在代码中用不同枚举类型隔离。
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum


class RuleLifecycleStatus(str, Enum):
    """
    127号§9 启发规则生命周期状态机。

    candidate ──(DYN-3因果实验通过+泄漏门通过)──→ validated
    validated ──(DYN-5跨3问题族+2模型版本复现)──→ published
    published ──(模型漂移/反例/更好规则替代)──→ retired
    candidate ──(反例发现/效果不可复现)──→ retired
    validated ──(反例发现/效果不可复现)──→ retired

    F4防线：这是HeuristicRule的生命周期状态，与Evidence.status
    （pending/active/superseded/retracted）是完全不同的枚举。
    """
    CANDIDATE = "candidate"
    VALIDATED = "validated"
    PUBLISHED = "published"
    RETIRED = "retired"


@dataclass
class LHS:
    """
    LHS: 匹配模式 p（127号§7）

    对当前工作区和关键事件窗口的类型化匹配模式。

    冻结声明：模式匹配必须返回被匹配实体、字段约束和时间窗口，
    不是只返回True/False（P3-3.COMP2）。
    """
    pattern: Dict[str, Any] = field(default_factory=dict)
    matched_entities: List[str] = field(default_factory=list)
    field_constraints: Dict[str, Any] = field(default_factory=dict)
    time_window: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "pattern": self.pattern,
            "matched_entities": self.matched_entities,
            "field_constraints": self.field_constraints,
            "time_window": self.time_window,
        }


@dataclass
class Interface:
    """
    interface: guard条件 g（127号§7）

    上下文、时序、模型、权限、预算和失败类型guard。
    """
    context: Dict[str, Any] = field(default_factory=dict)
    temporal: Dict[str, Any] = field(default_factory=dict)
    model_version: List[str] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)
    budget: Dict[str, Any] = field(default_factory=dict)
    failure_types: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "context": self.context,
            "temporal": self.temporal,
            "model_version": self.model_version,
            "permissions": self.permissions,
            "budget": self.budget,
            "failure_types": self.failure_types,
        }


@dataclass
class RHS:
    """
    RHS: 动作 a（激活包）（127号§7）

    123号§21激活包优先加入：
    - 一个检查问题
    - 一个研究操作
    - 一个新表示
    - 一个开放子目标
    - 一个工具调用
    - 一个反例方向
    - 一个有接口的定理候选

    冻结声明：
    - 动作只能提出候选状态扩展，真正写入V_t仍需Reducer与Verifier（P3-3.COMP3）
    - 激活包不应直接把目标结论加入V_t（P3-3.COMP4）
    """
    activation_packet: Dict[str, Any] = field(default_factory=dict)
    check_question: str = ""
    research_action: str = ""
    new_representation: str = ""
    open_subgoal: str = ""
    tool_call: str = ""
    counterexample_direction: str = ""
    theorem_candidate: str = ""

    def to_dict(self) -> dict:
        return {
            "activation_packet": self.activation_packet,
            "check_question": self.check_question,
            "research_action": self.research_action,
            "new_representation": self.new_representation,
            "open_subgoal": self.open_subgoal,
            "tool_call": self.tool_call,
            "counterexample_direction": self.counterexample_direction,
            "theorem_candidate": self.theorem_candidate,
        }


@dataclass
class Guard:
    """
    guard: 守卫条件（127号§7）

    泄漏上限、副作用上限、成本上限。
    """
    leakage_bound: float = 0.0
    side_effect_bound: float = 0.0
    cost_bound: float = 0.0

    def to_dict(self) -> dict:
        return {
            "leakage_bound": self.leakage_bound,
            "side_effect_bound": self.side_effect_bound,
            "cost_bound": self.cost_bound,
        }


@dataclass
class Eta:
    """
    η: 效果后验（127号§7）

    适用域、泄漏测量、成本测量、副作用记录。
    """
    applicability: str = ""
    leakage: float = 0.0
    cost: float = 0.0
    side_effects: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "applicability": self.applicability,
            "leakage": self.leakage,
            "cost": self.cost,
            "side_effects": self.side_effects,
        }


@dataclass
class HeuristicRule:
    """
    127号§7 HeuristicRule Schema冻结定义。

    h = (p, g, a, η) + 元数据（rule_id/status/effect_evidence/
    applicable_domains/model_versions/failure_cases）

    首版无DPO形式化（P3-3.COMP5）——文档明确声明首版无DPO形式化，
    不借用DPO记号冒充已完成形式化。
    """
    rule_id: str
    LHS: LHS = field(default_factory=LHS)
    interface: Interface = field(default_factory=Interface)
    RHS: RHS = field(default_factory=RHS)
    guard: Guard = field(default_factory=Guard)
    status: RuleLifecycleStatus = RuleLifecycleStatus.CANDIDATE
    effect_evidence: List[str] = field(default_factory=list)
    applicable_domains: List[str] = field(default_factory=list)
    model_versions: List[str] = field(default_factory=list)
    failure_cases: List[str] = field(default_factory=list)
    eta: Eta = field(default_factory=Eta)
    # 123号§44 G0-5：published通用规则至少跨3个"未参与设计"的问题族复现
    # design_participation_domains记录参与该规则设计的问题族
    # G0-5验证时：non_design_domains = applicable_domains - design_participation_domains >= 3
    design_participation_domains: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "LHS": self.LHS.to_dict(),
            "interface": self.interface.to_dict(),
            "RHS": self.RHS.to_dict(),
            "guard": self.guard.to_dict(),
            "status": self.status.value,
            "effect_evidence": self.effect_evidence,
            "applicable_domains": self.applicable_domains,
            "model_versions": self.model_versions,
            "failure_cases": self.failure_cases,
            "eta": self.eta.to_dict(),
            "design_participation_domains": self.design_participation_domains,
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "HeuristicRule":
        """从字典重建HeuristicRule（从ArangoDB读取时用）"""
        return cls(
            rule_id=d["rule_id"],
            LHS=LHS(
                pattern=d.get("LHS", {}).get("pattern", {}),
                matched_entities=d.get("LHS", {}).get("matched_entities", []),
                field_constraints=d.get("LHS", {}).get("field_constraints", {}),
                time_window=d.get("LHS", {}).get("time_window", {}),
            ),
            interface=Interface(
                context=d.get("interface", {}).get("context", {}),
                temporal=d.get("interface", {}).get("temporal", {}),
                model_version=d.get("interface", {}).get("model_version", []),
                permissions=d.get("interface", {}).get("permissions", []),
                budget=d.get("interface", {}).get("budget", {}),
                failure_types=d.get("interface", {}).get("failure_types", []),
            ),
            RHS=RHS(
                activation_packet=d.get("RHS", {}).get("activation_packet", {}),
                check_question=d.get("RHS", {}).get("check_question", ""),
                research_action=d.get("RHS", {}).get("research_action", ""),
                new_representation=d.get("RHS", {}).get("new_representation", ""),
                open_subgoal=d.get("RHS", {}).get("open_subgoal", ""),
                tool_call=d.get("RHS", {}).get("tool_call", ""),
                counterexample_direction=d.get("RHS", {}).get("counterexample_direction", ""),
                theorem_candidate=d.get("RHS", {}).get("theorem_candidate", ""),
            ),
            guard=Guard(
                leakage_bound=d.get("guard", {}).get("leakage_bound", 0.0),
                side_effect_bound=d.get("guard", {}).get("side_effect_bound", 0.0),
                cost_bound=d.get("guard", {}).get("cost_bound", 0.0),
            ),
            status=RuleLifecycleStatus(d.get("status", "candidate")),
            effect_evidence=d.get("effect_evidence", []),
            applicable_domains=d.get("applicable_domains", []),
            model_versions=d.get("model_versions", []),
            failure_cases=d.get("failure_cases", []),
            eta=Eta(
                applicability=d.get("eta", {}).get("applicability", ""),
                leakage=d.get("eta", {}).get("leakage", 0.0),
                cost=d.get("eta", {}).get("cost", 0.0),
                side_effects=d.get("eta", {}).get("side_effects", []),
            ),
            design_participation_domains=d.get("design_participation_domains", []),
        )
