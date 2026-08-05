"""
SideEffectLogger：负效应+无效规则记录+gaming检测

对应134号P4-8 + 系统探讨.md§15.4。

123号§23 Agent依赖代理3种（§530）：
1. 撤掉Hint后的独立继续率
2. 同类后续状态再次求助率
3. 单位已验证进展所需帮助量

系统探讨.md§15.4 gaming检测：
- Agent可能输出"停滞词"以触发更多帮助
- 需要工具证据和结构进展，而不是只相信自报

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


@dataclass
class GamingDetectionRecord:
    """
    gaming检测记录——系统探讨.md§15.4。

    Agent可能输出"停滞词"以触发更多帮助。
    需要工具证据和结构进展，而不是只相信自报。
    """
    run_id: str
    has_stall_words: bool = False       # 是否包含停滞词
    has_tool_evidence: bool = False     # 是否有工具证据
    has_structural_progress: bool = False  # 是否有结构进展
    is_gaming: bool = False             # 是否判定为gaming
    stall_words_detected: List[str] = field(default_factory=list)
    detail: str = ""

    def to_dict(self) -> dict:
        return {
            "run_id": self.run_id,
            "has_stall_words": self.has_stall_words,
            "has_tool_evidence": self.has_tool_evidence,
            "has_structural_progress": self.has_structural_progress,
            "is_gaming": self.is_gaming,
            "stall_words_detected": self.stall_words_detected,
            "detail": self.detail,
        }


# 系统探讨.md§15.4：Agent可能输出的"停滞词"
# 这些词如果出现但没有工具证据和结构进展，可能是gaming
STALL_WORDS = [
    "卡住了", "不知道", "无法继续", "需要帮助", "想不出来",
    "stuck", "don't know", "cannot continue", "need help",
    "no idea", "confused", "lost",
]


class SideEffectLogger:
    """
    P4-8：记录负效应和无效规则。

    P4-8.1：记录Agent依赖代理3种（123号§530）
    P4-8.2：记录副作用
    P4-8.3：记录无效规则
    P4-8.4：gaming检测（系统探讨.md§15.4）
    P4-8.COMP2：副作用低于预注册阈值（P4-EXIT-3出口门）
    """

    def __init__(self):
        self._dependency_proxy = AgentDependencyProxy()
        self._side_effects: List[SideEffectRecord] = []
        self._invalid_rules: List[InvalidRuleRecord] = []
        self._gaming_records: List[GamingDetectionRecord] = []

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

    def detect_gaming(
        self,
        run_id: str,
        response: str,
        has_tool_evidence: bool = False,
        has_structural_progress: bool = False,
    ) -> GamingDetectionRecord:
        """
        P4-8.4：gaming检测——系统探讨.md§15.4。

        Agent可能输出"停滞词"以触发更多帮助。
        需要工具证据和结构进展，而不是只相信自报。

        判定逻辑：
        - 如果包含停滞词但没有工具证据和结构进展 → is_gaming=True
        - 如果包含停滞词但有工具证据或结构进展 → is_gaming=False（真实停滞）
        - 如果不包含停滞词 → is_gaming=False
        """
        response_lower = response.lower()
        detected_words = [w for w in STALL_WORDS if w in response_lower]

        has_stall_words = len(detected_words) > 0
        # 系统探讨.md§15.4：有停滞词但无工具证据和结构进展 → gaming
        is_gaming = has_stall_words and not has_tool_evidence and not has_structural_progress

        record = GamingDetectionRecord(
            run_id=run_id,
            has_stall_words=has_stall_words,
            has_tool_evidence=has_tool_evidence,
            has_structural_progress=has_structural_progress,
            is_gaming=is_gaming,
            stall_words_detected=detected_words,
            detail=f"停滞词={detected_words}, 工具证据={has_tool_evidence}, 结构进展={has_structural_progress}",
        )
        self._gaming_records.append(record)
        return record

    def verify_gaming_rate_below_threshold(
        self, threshold: float = 0.3
    ) -> Dict[str, Any]:
        """
        验证gaming率低于阈值——系统探讨.md§15.4风险控制。
        """
        if not self._gaming_records:
            return {
                "passes": True,
                "gaming_rate": 0.0,
                "threshold": threshold,
                "n_records": 0,
            }
        n_gaming = sum(1 for r in self._gaming_records if r.is_gaming)
        rate = n_gaming / len(self._gaming_records)
        return {
            "passes": rate < threshold,
            "gaming_rate": rate,
            "threshold": threshold,
            "n_records": len(self._gaming_records),
            "n_gaming": n_gaming,
        }

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
            "gaming_records": [r.to_dict() for r in self._gaming_records],
        }
