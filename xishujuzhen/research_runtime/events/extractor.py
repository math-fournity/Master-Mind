"""
基础语义抽取器：从原始事件中识别基本的语义类型

对应131号P1-4.3 + 123号§28 Event Capture输出契约。

123号§28要求Event Capture输出分两层：
1. 不可变原始事件
2. 带置信度的语义事件

系统探讨.md§5.2定义的11种语义事件类型：
observation/claim/representation/subgoal/candidate/test/
tool_result/contradiction/stall/backtrack/resolution

本抽取器是规则-based的首版实现，后续Phase 2需要多观察者一致性测试（DYN-1）。
"""

from typing import List, Optional, Dict, Any
from ..models.event import (
    RawEvent, SemanticEvent, EventFactory,
    RawEventType, SemanticEventType,
)


class SemanticExtractor:
    """
    首版规则-based语义抽取器。

    从RawEvent的type和raw_payload中推断SemanticEvent的type。

    123号§17三层保留：语义事件可重抽，抽取失败不丢原始证据。
    """

    # RawEventType → SemanticEventType 的映射规则
    TYPE_MAPPING = {
        RawEventType.TEXT_OUTPUT.value: SemanticEventType.OBSERVATION.value,
        RawEventType.TEXT_DRAFT.value: SemanticEventType.OBSERVATION.value,
        RawEventType.REASONING_STEP.value: SemanticEventType.OBSERVATION.value,
        RawEventType.TOOL_CALL.value: SemanticEventType.TEST.value,
        RawEventType.TOOL_OUTPUT.value: SemanticEventType.TOOL_RESULT.value,
        RawEventType.CODE_EXEC.value: SemanticEventType.TEST.value,
        RawEventType.BRANCH_CHOICE.value: SemanticEventType.SUBGOAL.value,
        RawEventType.BRANCH_FORK.value: SemanticEventType.SUBGOAL.value,
        RawEventType.BACKTRACK_ACTION.value: SemanticEventType.BACKTRACK.value,
        RawEventType.CLAIM_MADE.value: SemanticEventType.CLAIM.value,
        RawEventType.CLAIM_RETRACTED.value: SemanticEventType.BACKTRACK.value,
        RawEventType.HYPOTHESIS_FORMED.value: SemanticEventType.CANDIDATE.value,
        RawEventType.GOAL_SET.value: SemanticEventType.SUBGOAL.value,
        RawEventType.GOAL_COMPLETED.value: SemanticEventType.RESOLUTION.value,
        RawEventType.GOAL_ABANDONED.value: SemanticEventType.BACKTRACK.value,
        RawEventType.STALL_DETECTED.value: SemanticEventType.STALL.value,
        RawEventType.CLAIM_CONTRADICTED.value: SemanticEventType.CONTRADICTION.value,
        RawEventType.CLAIM_REJECTED.value: SemanticEventType.BACKTRACK.value,
        RawEventType.VERIFICATION_RESULT.value: SemanticEventType.VERIFICATION.value,
        RawEventType.HINT_INJECTED.value: SemanticEventType.HINT_INJECTION.value,
        RawEventType.CHECKPOINT.value: SemanticEventType.STATE_REDUCTION.value,
    }

    def __init__(self, source_tag: str = "extractor_v1"):
        self.source_tag = source_tag

    def extract(self, raw_event: RawEvent) -> Optional[SemanticEvent]:
        """
        从单个原始事件抽取语义事件。

        返回None表示该原始事件无语义抽取（如RUN_START/RUN_END等元事件）。
        抽取失败不丢原始证据（123号§17三层保留）。
        """
        semantic_type = self.TYPE_MAPPING.get(raw_event.type)
        if semantic_type is None:
            return None  # 无语义抽取的原始事件类型

        # 从raw_payload中提取语义内容
        payload = self._extract_payload(raw_event)

        # 计算置信度（首版规则-based，后续Phase 2需要多观察者一致性测试）
        confidence = self._estimate_confidence(raw_event, semantic_type)

        return EventFactory.create_semantic_event(
            raw_event=raw_event,
            semantic_type=semantic_type,
            payload=payload,
            confidence=confidence,
            source=self.source_tag,
        )

    def extract_batch(self, raw_events: List[RawEvent]) -> List[SemanticEvent]:
        """批量抽取语义事件。跳过无语义抽取的原始事件。"""
        results = []
        for raw in raw_events:
            sem = self.extract(raw)
            if sem is not None:
                results.append(sem)
        return results

    def _extract_payload(self, raw_event: RawEvent) -> Dict[str, Any]:
        """从raw_payload中提取语义内容"""
        payload = raw_event.raw_payload.copy()

        # 根据事件类型添加语义标注
        if raw_event.type in (RawEventType.TEXT_OUTPUT.value, RawEventType.TEXT_DRAFT.value):
            payload["semantic_role"] = "agent_output"
        elif raw_event.type in (RawEventType.TOOL_CALL.value, RawEventType.TOOL_OUTPUT.value):
            payload["semantic_role"] = "tool_interaction"
        elif raw_event.type == RawEventType.BRANCH_CHOICE.value:
            payload["semantic_role"] = "decision_point"
            # 提取被拒绝的选项作为backtrack信息
            if "rejected" in payload:
                payload["abandoned_alternative"] = payload["rejected"]
        elif raw_event.type == RawEventType.CLAIM_CONTRADICTED.value:
            payload["semantic_role"] = "contradiction_evidence"
        elif raw_event.type == RawEventType.CLAIM_REJECTED.value:
            payload["semantic_role"] = "branch_rejection"

        return payload

    def _estimate_confidence(
        self, raw_event: RawEvent, semantic_type: str
    ) -> float:
        """
        首版置信度估计（规则-based）。

        后续Phase 2需要多观察者一致性测试（DYN-1）来校准。
        """
        # 工具结果和验证结果的置信度较高
        if semantic_type in (
            SemanticEventType.TOOL_RESULT.value,
            SemanticEventType.VERIFICATION.value,
        ):
            return 0.95

        # 明确的声明和目标设置置信度较高
        if semantic_type in (
            SemanticEventType.CLAIM.value,
            SemanticEventType.SUBGOAL.value,
            SemanticEventType.RESOLUTION.value,
        ):
            return 0.9

        # 观察类置信度中等
        if semantic_type == SemanticEventType.OBSERVATION.value:
            return 0.8

        # 候选和假设置信度较低
        if semantic_type in (
            SemanticEventType.CANDIDATE.value,
            SemanticEventType.REPRESENTATION.value,
        ):
            return 0.7

        # 矛盾和停滞需要进一步验证
        if semantic_type in (
            SemanticEventType.CONTRADICTION.value,
            SemanticEventType.STALL.value,
        ):
            return 0.6

        return 0.75  # 默认置信度
