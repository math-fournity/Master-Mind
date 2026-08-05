"""
Event schema: 123号§17 + 127号§3

原始事件 L_≤t = (E_≤t, ≼, #, λ)
- ≼: 自反/反对称/传递的可观测先后偏序（causal_predecessors实现DAG边）
- #: 对称、非自反的显式分支冲突关系（conflict_with实现）

三层保留（127号§3冻结声明）：
1. 原始事件（不可变）
2. 语义抽取（可重抽）
3. 状态快照（可重建）

冻结声明：
- 原始事件append-only，不允许修改或删除
- 事件因果图是DAG（时间不倒流）
- "又回到同一想法"是两个不同时刻事件投影到相同语义状态，不是事件循环
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import hashlib
import json
import uuid
from datetime import datetime, timezone


class SemanticEventType(str, Enum):
    """
    127号§3定义的14种语义事件类型。
    系统探讨.md§5.2的11种 + 123号§17新增的3种。
    """
    OBSERVATION = "observation"
    CLAIM = "claim"
    REPRESENTATION = "representation"
    SUBGOAL = "subgoal"
    CANDIDATE = "candidate"
    TEST = "test"
    TOOL_RESULT = "tool_result"
    CONTRADICTION = "contradiction"
    STALL = "stall"
    BACKTRACK = "backtrack"
    RESOLUTION = "resolution"
    HINT_INJECTION = "hint_injection"       # 123号§17新增
    STATE_REDUCTION = "state_reduction"      # 123号§17新增
    VERIFICATION = "verification"            # 123号§17新增


class RawEventType(str, Enum):
    """
    128号G0-1定义的原始事件类型（5类27种中的主要类型）。
    原始事件是未加工的捕获内容，语义事件是从中抽取的类型化事件。
    """
    # 工具调用类
    TOOL_CALL = "tool_call"
    TOOL_OUTPUT = "tool_output"
    CODE_EXEC = "code_exec"
    FILE_WRITE = "file_write"
    FILE_READ = "file_read"
    API_CALL = "api_call"
    SEARCH = "search"
    # 文本段落类
    TEXT_OUTPUT = "text_output"
    TEXT_DRAFT = "text_draft"
    REASONING_STEP = "reasoning_step"
    # 分支点类
    BRANCH_CHOICE = "branch_choice"
    BRANCH_FORK = "branch_fork"
    BRANCH_MERGE = "branch_merge"
    BACKTRACK_ACTION = "backtrack_action"
    # 状态变更类
    CLAIM_MADE = "claim_made"
    CLAIM_RETRACTED = "claim_retracted"
    HYPOTHESIS_FORMED = "hypothesis_formed"
    GOAL_SET = "goal_set"
    GOAL_COMPLETED = "goal_completed"
    GOAL_ABANDONED = "goal_abandoned"
    # 其他
    STALL_DETECTED = "stall_detected"
    RESUMED = "resumed"
    RUN_START = "run_start"
    RUN_END = "run_end"
    CHECKPOINT = "checkpoint"
    HINT_INJECTED = "hint_injected"
    VERIFICATION_RESULT = "verification_result"


def _compute_hash(payload: Any) -> str:
    """计算内容的SHA-256哈希"""
    if isinstance(payload, str):
        content = payload.encode("utf-8")
    else:
        content = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(content).hexdigest()


def _now_iso() -> str:
    """当前UTC时间的ISO 8601时间戳"""
    return datetime.now(timezone.utc).isoformat()


def _gen_id(prefix: str = "evt") -> str:
    """生成唯一事件ID"""
    return f"{prefix}_{uuid.uuid4().hex[:16]}"


@dataclass
class RawEvent:
    """
    127号§3 RawEvent Schema冻结定义。
    原始事件append-only，不允许修改或删除。
    """
    event_id: str
    type: str                             # RawEventType枚举值
    timestamp: str                        # ISO 8601
    run_id: str                           # 关联运行manifest
    raw_payload: Dict[str, Any]           # 原始未加工内容
    content_hash: str                     # SHA-256内容哈希
    causal_predecessors: List[str] = field(default_factory=list)  # DAG边
    workspace_ref: Optional[str] = None   # 关联工作区（可选，语义层填充）

    def to_dict(self) -> dict:
        return {
            "event_id": self.event_id,
            "type": self.type,
            "timestamp": self.timestamp,
            "run_id": self.run_id,
            "workspace_ref": self.workspace_ref,
            "raw_payload": self.raw_payload,
            "content_hash": self.content_hash,
            "causal_predecessors": self.causal_predecessors,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "RawEvent":
        return cls(
            event_id=d["event_id"],
            type=d["type"],
            timestamp=d["timestamp"],
            run_id=d["run_id"],
            raw_payload=d["raw_payload"],
            content_hash=d["content_hash"],
            causal_predecessors=d.get("causal_predecessors", []),
            workspace_ref=d.get("workspace_ref"),
        )


@dataclass
class SemanticEvent:
    """
    127号§3 SemanticEvent Schema冻结定义。
    语义事件可重抽（三层保留的第2层）。
    """
    event_id: str
    raw_event_id: str                     # 指向原始事件
    type: str                             # SemanticEventType枚举值
    timestamp: str
    run_id: str
    payload: Dict[str, Any]               # 抽取后的语义内容
    content_hash: str                     # 语义内容哈希
    causal_predecessors: List[str] = field(default_factory=list)
    conflict_with: List[str] = field(default_factory=list)  # #关系
    confidence: float = 1.0               # 置信度 [0,1]
    source: str = "extractor_v1"          # 来源标注（抽取器版本）
    workspace_ref: Optional[str] = None
    obligation_ref: Optional[str] = None
    evidence_ref: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "event_id": self.event_id,
            "raw_event_id": self.raw_event_id,
            "type": self.type,
            "timestamp": self.timestamp,
            "run_id": self.run_id,
            "workspace_ref": self.workspace_ref,
            "obligation_ref": self.obligation_ref,
            "evidence_ref": self.evidence_ref,
            "payload": self.payload,
            "content_hash": self.content_hash,
            "causal_predecessors": self.causal_predecessors,
            "conflict_with": self.conflict_with,
            "confidence": self.confidence,
            "source": self.source,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "SemanticEvent":
        return cls(
            event_id=d["event_id"],
            raw_event_id=d["raw_event_id"],
            type=d["type"],
            timestamp=d["timestamp"],
            run_id=d["run_id"],
            payload=d["payload"],
            content_hash=d["content_hash"],
            causal_predecessors=d.get("causal_predecessors", []),
            conflict_with=d.get("conflict_with", []),
            confidence=d.get("confidence", 1.0),
            source=d.get("source", "extractor_v1"),
            workspace_ref=d.get("workspace_ref"),
            obligation_ref=d.get("obligation_ref"),
            evidence_ref=d.get("evidence_ref"),
        )


class EventFactory:
    """
    事件工厂：创建RawEvent和SemanticEvent的辅助方法。
    自动生成event_id、timestamp和content_hash。
    """

    @staticmethod
    def create_raw_event(
        run_id: str,
        event_type: str,
        raw_payload: Dict[str, Any],
        causal_predecessors: Optional[List[str]] = None,
        workspace_ref: Optional[str] = None,
    ) -> RawEvent:
        """创建原始事件（自动生成event_id/timestamp/content_hash）"""
        return RawEvent(
            event_id=_gen_id("raw"),
            type=event_type,
            timestamp=_now_iso(),
            run_id=run_id,
            raw_payload=raw_payload,
            content_hash=_compute_hash(raw_payload),
            causal_predecessors=causal_predecessors or [],
            workspace_ref=workspace_ref,
        )

    @staticmethod
    def create_semantic_event(
        raw_event: RawEvent,
        semantic_type: str,
        payload: Dict[str, Any],
        causal_predecessors: Optional[List[str]] = None,
        conflict_with: Optional[List[str]] = None,
        confidence: float = 1.0,
        source: str = "extractor_v1",
        workspace_ref: Optional[str] = None,
        obligation_ref: Optional[str] = None,
        evidence_ref: Optional[str] = None,
    ) -> SemanticEvent:
        """创建语义事件（继承run_id/timestamp，自动生成content_hash）"""
        return SemanticEvent(
            event_id=_gen_id("sem"),
            raw_event_id=raw_event.event_id,
            type=semantic_type,
            timestamp=raw_event.timestamp,
            run_id=raw_event.run_id,
            payload=payload,
            content_hash=_compute_hash(payload),
            causal_predecessors=causal_predecessors or [],
            conflict_with=conflict_with or [],
            confidence=confidence,
            source=source,
            workspace_ref=workspace_ref or raw_event.workspace_ref,
            obligation_ref=obligation_ref,
            evidence_ref=evidence_ref,
        )
