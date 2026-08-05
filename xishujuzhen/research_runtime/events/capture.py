"""
基础事件捕获器：从Solver输出和工具调用中创建原始事件

对应131号P1-2 + 123号§28 Event Capture输入契约。

123号§28要求Event Capture输入：
Solver公开产物、草稿中被明确允许保存的研究文本、工具调用、提示、分支/回退和时间

123号§32步骤4（事件捕获）：
保存公开文本、命题、工具、分支、回退和失败

R-1风险防线：不捕获隐藏CoT，只处理公开研究产物与工具事件
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, timezone

from ..models.event import (
    RawEvent, EventFactory, RawEventType,
)


class EventCapture:
    """
    基础事件捕获器。

    从Solver的公开输出、工具调用、分支选择等中创建原始事件。
    不捕获隐藏CoT（R-1风险防线）。
    """

    def __init__(self, run_id: str):
        self.run_id = run_id
        self._last_event_id: Optional[str] = None  # 用于自动设置causal_predecessors

    def capture_text_output(self, text: str, metadata: Optional[Dict] = None) -> RawEvent:
        """捕获Solver的公开文本输出"""
        payload = {"text": text, "char_count": len(text)}
        if metadata:
            payload["metadata"] = metadata
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.TEXT_OUTPUT.value,
            raw_payload=payload,
            causal_predecessors=self._predecessors(),
        )
        self._last_event_id = event.event_id
        return event

    def capture_text_draft(self, text: str, metadata: Optional[Dict] = None) -> RawEvent:
        """捕获Solver的草稿文本（被明确允许保存的研究文本）"""
        payload = {"text": text, "char_count": len(text)}
        if metadata:
            payload["metadata"] = metadata
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.TEXT_DRAFT.value,
            raw_payload=payload,
            causal_predecessors=self._predecessors(),
        )
        self._last_event_id = event.event_id
        return event

    def capture_tool_call(
        self, tool_name: str, tool_input: Any,
        metadata: Optional[Dict] = None,
    ) -> RawEvent:
        """捕获工具调用"""
        payload = {"tool": tool_name, "input": tool_input}
        if metadata:
            payload["metadata"] = metadata
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.TOOL_CALL.value,
            raw_payload=payload,
            causal_predecessors=self._predecessors(),
        )
        self._last_event_id = event.event_id
        return event

    def capture_tool_output(
        self, tool_name: str, tool_output: Any,
        call_event_id: Optional[str] = None,
        metadata: Optional[Dict] = None,
    ) -> RawEvent:
        """捕获工具输出"""
        payload = {"tool": tool_name, "output": tool_output}
        if metadata:
            payload["metadata"] = metadata
        preds = [call_event_id] if call_event_id else self._predecessors()
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.TOOL_OUTPUT.value,
            raw_payload=payload,
            causal_predecessors=preds,
        )
        self._last_event_id = event.event_id
        return event

    def capture_code_exec(
        self, code: str, result: Optional[Any] = None,
        metadata: Optional[Dict] = None,
    ) -> RawEvent:
        """捕获代码执行"""
        payload = {"code": code, "result": result}
        if metadata:
            payload["metadata"] = metadata
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.CODE_EXEC.value,
            raw_payload=payload,
            causal_predecessors=self._predecessors(),
        )
        self._last_event_id = event.event_id
        return event

    def capture_branch_choice(
        self, chosen: str, rejected: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> RawEvent:
        """捕获分支选择"""
        payload = {"chosen": chosen}
        if rejected:
            payload["rejected"] = rejected
        if reason:
            payload["reason"] = reason
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.BRANCH_CHOICE.value,
            raw_payload=payload,
            causal_predecessors=self._predecessors(),
        )
        self._last_event_id = event.event_id
        return event

    def capture_backtrack(
        self, abandoned_target: str, reason: str = "",
    ) -> RawEvent:
        """捕获回退行为"""
        payload = {"abandoned": abandoned_target, "reason": reason}
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.BACKTRACK_ACTION.value,
            raw_payload=payload,
            causal_predecessors=self._predecessors(),
        )
        self._last_event_id = event.event_id
        return event

    def capture_claim(self, claim_text: str, claim_type: str = "lemma") -> RawEvent:
        """捕获Agent提出的命题/声明"""
        payload = {"claim": claim_text, "claim_type": claim_type}
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.CLAIM_MADE.value,
            raw_payload=payload,
            causal_predecessors=self._predecessors(),
        )
        self._last_event_id = event.event_id
        return event

    def capture_stall(self, stall_type: str, details: str = "") -> RawEvent:
        """捕获停滞检测"""
        payload = {"stall_type": stall_type, "details": details}
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.STALL_DETECTED.value,
            raw_payload=payload,
            causal_predecessors=self._predecessors(),
        )
        self._last_event_id = event.event_id
        return event

    def capture_run_start(self, task_id: str) -> RawEvent:
        """捕获运行开始"""
        payload = {"action": "run_start", "task_id": task_id}
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.RUN_START.value,
            raw_payload=payload,
        )
        self._last_event_id = event.event_id
        return event

    def capture_run_end(self, outcome: str = "completed") -> RawEvent:
        """捕获运行结束"""
        payload = {"action": "run_end", "outcome": outcome}
        event = EventFactory.create_raw_event(
            run_id=self.run_id,
            event_type=RawEventType.RUN_END.value,
            raw_payload=payload,
            causal_predecessors=self._predecessors(),
        )
        self._last_event_id = event.event_id
        return event

    def _predecessors(self) -> List[str]:
        """获取前驱事件ID列表（自动链接到上一个事件）"""
        return [self._last_event_id] if self._last_event_id else []
