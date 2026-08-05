"""
控制器信念建模 b_t + 9种动作

对应132号P2-8。

123号§22冻结声明：
- 系统看不到LLM完整内部状态，只看到公开产物和工具事件
- 控制器维护的是对"当前策略、卡点类型、是否真的停滞"的不确定估计，而不是假装读心
- 动作集合包括9种（123号§22）

边界情况：
- 信念不确定（多种卡点类型概率相近）
- 信念与自报不一致（gaming检测）
- 预算不足时动作受限
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone

from ..verification.stall_detector import StallDetector, StallType, StallDetection


class ActionType(str, Enum):
    """
    123号§22定义的9种动作。
    """
    CONTINUE_OBSERVING = "continue_observing"           # 继续观察
    ASK_DIAGNOSTIC_QUESTION = "ask_diagnostic_question" # 诊断提问
    REQUEST_TOOL_CHECK = "request_tool_check"           # 工具检查
    RETRIEVE_MINIMAL_INTERFACE = "retrieve_minimal_interface"  # 检索最小接口
    INJECT_HINT_0 = "inject_hint_0"                     # 注入H0元检查
    INJECT_HINT_1 = "inject_hint_1"                     # 注入H1思维操作
    INJECT_HINT_2 = "inject_hint_2"                     # 注入H2概念/工具候选
    ABSTAIN = "abstain"                                 # 弃权/不提示
    STOP_OR_ESCALATE = "stop_or_escalate"               # 停止或升级


@dataclass
class ControllerBelief:
    """
    控制器信念 b_t（123号§15 + §22）。

    控制器对当前卡点、策略和缺失信息的带不确定性信念。
    不是假装读心——只基于公开产物和工具事件做估计。
    """
    stall_type_probs: Dict[str, float] = field(default_factory=dict)  # 各卡点类型的概率
    is_stall_prob: float = 0.0                  # 是否真的停滞的概率
    strategy_confidence: float = 0.5            # 当前策略的置信度
    missing_info_estimate: List[str] = field(default_factory=list)  # 估计缺失的信息
    gaming_prob: float = 0.0                    # gaming概率（Agent迎合触发器）
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "stall_type_probs": self.stall_type_probs,
            "is_stall_prob": self.is_stall_prob,
            "strategy_confidence": self.strategy_confidence,
            "missing_info_estimate": self.missing_info_estimate,
            "gaming_prob": self.gaming_prob,
            "timestamp": self.timestamp,
        }


class BeliefEstimator:
    """
    信念估计器（P2-8）。

    冻结声明：
    - 只基于公开产物和工具事件做估计（P2-8.COMP）
    - 不假装读心（P2-8.COMP）
    """

    def __init__(self, stall_detector: StallDetector):
        self.stall_detector = stall_detector

    def estimate(
        self,
        progress_history: List[Dict[str, Any]],
        budget: Dict[str, Any],
        obligations: Dict[str, Any],
        self_reported_stall: bool = False,
    ) -> ControllerBelief:
        """
        从公开产物和工具事件估计控制器信念。

        不读取LLM内部状态——只基于可观测的事件和状态。
        """
        # 1. 检测卡点
        detections = self.stall_detector.detect(
            progress_history, budget, obligations, self_reported_stall,
        )

        # 2. 计算各卡点类型的概率
        stall_type_probs: Dict[str, float] = {}
        total_confidence = sum(d.confidence for d in detections)

        if total_confidence > 0:
            for d in detections:
                stall_type_probs[d.stall_type.value] = d.confidence / total_confidence

        # 3. 是否真的停滞——排除必要探索（不是真正卡点）
        real_stalls = [d for d in detections if d.stall_type != StallType.NECESSARY_EXPLORATION]
        is_stall_prob = min(1.0, sum(d.confidence for d in real_stalls))

        # 4. gaming概率——必要探索被误判为停滞
        necessary_exploration = [d for d in detections if d.stall_type == StallType.NECESSARY_EXPLORATION]
        gaming_prob = max(d.confidence for d in necessary_exploration) if necessary_exploration else 0.0

        # 5. 策略置信度
        if progress_history:
            recent_improve = sum(1 for p in progress_history[-3:] if p.get("relation") == "improved")
            strategy_confidence = recent_improve / min(3, len(progress_history))
        else:
            strategy_confidence = 0.5

        # 6. 估计缺失的信息（按123号§38的7类卡点）
        missing_info = []
        if stall_type_probs.get(StallType.UNRESOLVED_CONTRADICTION.value, 0) > 0:
            missing_info.append("冲突澄清")
        if stall_type_probs.get(StallType.REPRESENTATION_UNSUITABLE.value, 0) > 0:
            missing_info.append("替代表示")
        if stall_type_probs.get(StallType.TOOL_BLOCKED.value, 0) > 0:
            missing_info.append("工具修复")

        return ControllerBelief(
            stall_type_probs=stall_type_probs,
            is_stall_prob=is_stall_prob,
            strategy_confidence=strategy_confidence,
            missing_info_estimate=missing_info,
            gaming_prob=gaming_prob,
        )

    def select_action(
        self,
        belief: ControllerBelief,
        budget: Dict[str, Any],
        hint_budget_remaining: int = 3,
    ) -> Dict[str, Any]:
        """
        根据信念选择动作（123号§32步骤7+步骤9）。

        不把所有停滞都视为应提示。
        受预算约束——hint预算不足时不能注入Hint。
        """
        # 1. gaming概率高——弃权（优先检查，即使is_stall_prob低）
        if belief.gaming_prob > 0.7:
            return {
                "action": ActionType.ABSTAIN.value,
                "reason": f"gaming概率高({belief.gaming_prob:.2f})——不提示",
                "belief": belief.to_dict(),
            }

        # 2. 无停滞——继续观察
        if belief.is_stall_prob < 0.3:
            return {
                "action": ActionType.CONTINUE_OBSERVING.value,
                "reason": f"停滞概率低({belief.is_stall_prob:.2f})",
                "belief": belief.to_dict(),
            }

        # 3. 预算耗尽——停止
        for budget_type, values in budget.items():
            if values.get("remaining", 0) <= 0:
                return {
                    "action": ActionType.STOP_OR_ESCALATE.value,
                    "reason": f"{budget_type}预算耗尽",
                    "belief": belief.to_dict(),
                }

        # 4. 矛盾未处理——请求工具检查
        if belief.stall_type_probs.get(StallType.UNRESOLVED_CONTRADICTION.value, 0) > 0.3:
            return {
                "action": ActionType.REQUEST_TOOL_CHECK.value,
                "reason": "矛盾未处理——请求工具检查",
                "belief": belief.to_dict(),
            }

        # 5. 工具阻塞——请求工具检查
        if belief.stall_type_probs.get(StallType.TOOL_BLOCKED.value, 0) > 0.3:
            return {
                "action": ActionType.REQUEST_TOOL_CHECK.value,
                "reason": "工具阻塞——请求工具检查",
                "belief": belief.to_dict(),
            }

        # 6. 表示不合适——检索最小接口
        if belief.stall_type_probs.get(StallType.REPRESENTATION_UNSUITABLE.value, 0) > 0.3:
            return {
                "action": ActionType.RETRIEVE_MINIMAL_INTERFACE.value,
                "reason": "表示不合适——检索最小接口",
                "belief": belief.to_dict(),
            }

        # 6. 策略耗尽——诊断提问或注入Hint
        if belief.stall_type_probs.get(StallType.STRATEGY_EXHAUSTION.value, 0) > 0.3:
            if hint_budget_remaining > 0:
                # 按H0→H1→H2顺序选择Hint级别
                if hint_budget_remaining >= 3:
                    action = ActionType.INJECT_HINT_0.value
                    reason = "策略耗尽——注入H0元检查（最低级别Hint）"
                elif hint_budget_remaining >= 2:
                    action = ActionType.INJECT_HINT_1.value
                    reason = "策略耗尽——注入H1思维操作"
                else:
                    action = ActionType.INJECT_HINT_2.value
                    reason = "策略耗尽——注入H2概念/工具候选"
                return {
                    "action": action,
                    "reason": reason,
                    "belief": belief.to_dict(),
                    "hint_budget_remaining": hint_budget_remaining,
                }
            else:
                return {
                    "action": ActionType.ASK_DIAGNOSTIC_QUESTION.value,
                    "reason": "策略耗尽但Hint预算不足——诊断提问",
                    "belief": belief.to_dict(),
                }

        # 7. 默认——诊断提问
        return {
            "action": ActionType.ASK_DIAGNOSTIC_QUESTION.value,
            "reason": "停滞检测但无特定类型——诊断提问",
            "belief": belief.to_dict(),
        }
