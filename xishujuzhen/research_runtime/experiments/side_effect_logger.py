"""
SideEffectLogger：负效应+无效规则记录

对应134号P4-8。

123号§23 Agent依赖代理3种（§530）：
1. 撤掉Hint后的独立继续率
2. 同类后续状态再次求助率
3. 单位已验证进展所需帮助量

P4-8.1：记录Agent依赖代理3种
P4-8.2：记录副作用（错误方向/误导/破坏自然探索）
P4-8.3：记录无效规则（效果不可复现的candidate规则）

复用Phase 3的AgentDependencyProxy（149号修正）。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

from ..heuristics.leakage_audit import AgentDependencyProxy


@dataclass
class SideEffectRecord:
    """副作用记录"""
    run_id: str
    treatment_group: str
    # P4-8.2：副作用类型
    wrong_direction: bool = False       # 错误方向
    misleading: bool = False            # 误导
    disrupts_exploration: bool = False  # 破坏自然探索
    detail: str = ""

    def to_dict(self) -> dict:
        return {
            "run_id": self.run_id,
            "treatment_group": self.treatment_group,
            "wrong_direction": self.wrong_direction,
            "misleading": self.misleading,
            "disrupts_exploration": self.disrupts_exploration,
            "detail": self.detail,
        }


@dataclass
class InvalidRuleRecord:
    """无效规则记录——P4-8.3"""
    rule_id: str
    reason: str = ""  # 效果不可复现/反例发现/模型漂移
    original_effect: float = 0.0
    replication_effect: float = 0.0

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "reason": self.reason,
            "original_effect": self.original_effect,
            "replication_effect": self.replication_effect,
        }


class SideEffectLogger:
    """
    P4-8：记录负效应和无效规则。

    P4-8.1：记录Agent依赖代理3种（123号§530）
    P4-8.2：记录副作用
    P4-8.3：记录无效规则
    P4-8.COMP2：副作用低于预注册阈值（P4-EXIT-3出口门）
    """

    def __init__(self):
        self._dependency_proxy = AgentDependencyProxy()
        self._side_effects: List[SideEffectRecord] = []
        self._invalid_rules: List[InvalidRuleRecord] = []

    def measure_dependency_proxies(
        self,
        runs_with_hint: Optional[List[Dict[str, Any]]] = None,
        runs_without_hint: Optional[List[Dict[str, Any]]] = None,
        subsequent_states: Optional[List[Dict[str, Any]]] = None,
        hints_given: int = 0,
        verified_progress: int = 0,
    ) -> Dict[str, Any]:
        """
        P4-8.1：记录Agent依赖代理3种。

        P4-8.COMP：Agent依赖代理3种全部记录。
        复用Phase 3的AgentDependencyProxy（149号修正）。

        F6防线：全部是代理分数，不是真实依赖度。
        """
        return self._dependency_proxy.measure_all_proxies(
            runs_with_hint=runs_with_hint,
            runs_without_hint=runs_without_hint,
            subsequent_states=subsequent_states,
            hints_given=hints_given,
            verified_progress=verified_progress,
        )

    def record_side_effect(self, record: SideEffectRecord):
        """P4-8.2：记录副作用"""
        self._side_effects.append(record)

    def record_invalid_rule(self, record: InvalidRuleRecord):
        """P4-8.3：记录无效规则"""
        self._invalid_rules.append(record)

    def verify_side_effects_below_threshold(
        self, threshold: float = 0.3
    ) -> Dict[str, Any]:
        """
        P4-8.COMP2：副作用低于预注册阈值（P4-EXIT-3出口门）。

        边界情况：
        - 副作用率超过阈值 → 不通过
        - 无副作用记录 → 通过
        """
        if not self._side_effects:
            return {
                "passes_exit_gate": True,
                "side_effect_rate": 0.0,
                "threshold": threshold,
                "n_records": 0,
            }

        n_negative = sum(
            1 for r in self._side_effects
            if r.wrong_direction or r.misleading or r.disrupts_exploration
        )
        rate = n_negative / len(self._side_effects)

        return {
            "passes_exit_gate": rate < threshold,
            "side_effect_rate": rate,
            "threshold": threshold,
            "n_records": len(self._side_effects),
            "n_negative": n_negative,
        }

    def get_all_records(self) -> Dict[str, Any]:
        return {
            "side_effects": [r.to_dict() for r in self._side_effects],
            "invalid_rules": [r.to_dict() for r in self._invalid_rules],
        }
