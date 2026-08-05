"""
Workspace schema: 123号§15 + 127号§2

工作区 W_t = (V_t, F_t, O_t, R_t, D_t, E_t)
完整运行状态 S_t = (Q_0, W_t, L_≤t, b_t, B_t, M_t)

冻结声明（127号§2）：
- Q_0保持冻结，不混入临时假设
- 临时假设进入F_t，不进入V_t
- 被拒绝路线进入D_t，不与representation共用R
- W_t只能由版本化Reducer按明确字段规则派生，不能被直接修改
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class VerifiedCore:
    """V_t: 已验证核心（原则上单调增长）"""
    verified_premises: List[str] = field(default_factory=list)
    verified_lemmas: List[str] = field(default_factory=list)
    verified_tool_results: List[str] = field(default_factory=list)


@dataclass
class Frontier:
    """F_t: 猜想前沿（非单调）"""
    candidates: List[str] = field(default_factory=list)
    temporary_assumptions: List[str] = field(default_factory=list)
    unverified_bridges: List[str] = field(default_factory=list)


@dataclass
class OpenObligations:
    """O_t: 开放研究义务（AND/OR超图引用）"""
    obligation_ids: List[str] = field(default_factory=list)


@dataclass
class ActiveRepresentations:
    """R_t: 当前表示及其转换"""
    active_representations: List[str] = field(default_factory=list)
    pending_transforms: List[str] = field(default_factory=list)


@dataclass
class DiscardedBranches:
    """D_t: 被证伪/拒绝/暂停/可恢复分支"""
    rejected_branches: List[str] = field(default_factory=list)
    suspended_branches: List[str] = field(default_factory=list)
    recoverable_branches: List[str] = field(default_factory=list)


@dataclass
class EvidenceRefs:
    """E_t: 每个命题与动作的证据"""
    evidence_ids: List[str] = field(default_factory=list)


@dataclass
class Workspace:
    """
    127号§2 Workspace Schema冻结定义。
    W_t只能由版本化Reducer按明确字段规则派生，不能被直接修改。
    """
    workspace_id: str
    task_id: str
    timestamp: str                        # ISO 8601

    V_t: VerifiedCore = field(default_factory=VerifiedCore)
    F_t: Frontier = field(default_factory=Frontier)
    O_t: OpenObligations = field(default_factory=OpenObligations)
    R_t: ActiveRepresentations = field(default_factory=ActiveRepresentations)
    D_t: DiscardedBranches = field(default_factory=DiscardedBranches)
    E_t: EvidenceRefs = field(default_factory=EvidenceRefs)

    def to_dict(self) -> dict:
        return {
            "workspace_id": self.workspace_id,
            "task_id": self.task_id,
            "timestamp": self.timestamp,
            "V_t": {
                "verified_premises": self.V_t.verified_premises,
                "verified_lemmas": self.V_t.verified_lemmas,
                "verified_tool_results": self.V_t.verified_tool_results,
            },
            "F_t": {
                "candidates": self.F_t.candidates,
                "temporary_assumptions": self.F_t.temporary_assumptions,
                "unverified_bridges": self.F_t.unverified_bridges,
            },
            "O_t": {
                "obligation_ids": self.O_t.obligation_ids,
            },
            "R_t": {
                "active_representations": self.R_t.active_representations,
                "pending_transforms": self.R_t.pending_transforms,
            },
            "D_t": {
                "rejected_branches": self.D_t.rejected_branches,
                "suspended_branches": self.D_t.suspended_branches,
                "recoverable_branches": self.D_t.recoverable_branches,
            },
            "E_t": {
                "evidence_ids": self.E_t.evidence_ids,
            },
        }


@dataclass
class RunState:
    """
    127号§2 完整运行状态 S_t = (Q_0, W_t, L_≤t, b_t, B_t, M_t)

    - Q_0: 冻结的初始任务
    - W_t: 当前工作区
    - L_≤t: 不可变事件历史
    - b_t: 控制器对卡点/策略/缺失信息的带不确定性信念
    - B_t: token/计算/工具/分支/Hint预算
    - M_t: 模型版本/推理配置/权限/工具能力
    """
    task: dict                           # Q_0 (frozen)
    workspace: dict                      # W_t
    event_history_ref: str               # L_≤t (reference to event chain)
    controller_belief: Dict[str, Any]    # b_t
    budget: Dict[str, float]             # B_t
    model_config: Dict[str, Any]         # M_t
