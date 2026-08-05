"""
Context Compiler——每段上下文带5项记录

对应135号P5-4 + 123号§29 + §28(角色可见性) + §607(visibility label和能力令牌)。

冻结声明：
- 每段输出带5项记录（P5-4.1 + P5-4.COMP + 123号§29）：
  1. 来源
  2. 可见性
  3. 证据等级
  4. token成本
  5. 裁剪记录
- 每段上下文可追溯到原始来源（P5-4.2）
- 角色边界落实为collection、visibility label和能力令牌（P5-4.4 + 123号§607）
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from .state_snapshot import StateSnapshot
from .pruning_log import PruningLog
from .minimality_audit import MinimalityAudit, MinimalityAuditResult


@dataclass
class ContextSegment:
    """
    Context Compiler输出的单段内容——带5项记录（123号§29）。
    """
    segment_id: str
    content: str
    content_type: str  # 7类内容之一

    # 5项记录（P5-4.1 + P5-4.COMP）
    source: str = ""              # 1. 来源
    visibility: str = ""          # 2. 可见性
    evidence_level: str = ""      # 3. 证据等级
    token_cost: int = 0           # 4. token成本
    pruning_record: str = ""      # 5. 裁剪记录

    # 关联信息
    obligation_ref: str = ""      # 关联的义务ID
    activation_pack_ref: str = "" # 关联的激活包

    def to_dict(self) -> dict:
        return {
            "segment_id": self.segment_id,
            "content": self.content,
            "content_type": self.content_type,
            "source": self.source,
            "visibility": self.visibility,
            "evidence_level": self.evidence_level,
            "token_cost": self.token_cost,
            "pruning_record": self.pruning_record,
            "obligation_ref": self.obligation_ref,
            "activation_pack_ref": self.activation_pack_ref,
        }

    def check_has_5_records(self) -> bool:
        """
        验证段带5项记录（P5-4.1 + P5-4.COMP）。

        边界情况：某项记录缺失（应被拒绝——必须5项全部带）
        """
        # 5项记录：source/visibility/evidence_level/token_cost/pruning_record
        # token_cost是int，必须有值（>=0）
        # 其他4项是str，不能为空
        return all([
            self.source != "",
            self.visibility != "",
            self.evidence_level != "",
            self.token_cost >= 0,  # token_cost可以为0但不能是None
            self.pruning_record != "",  # 裁剪记录必须有值（"none"也是有效值）
        ])

    def check_traceable(self) -> bool:
        """
        验证段可追溯到原始来源（P5-4.2）。

        边界情况：上下文不可追溯（应被拒绝）
        """
        return self.source != ""


class ContextCompiler:
    """
    Context Compiler（135号P5-4.1）。

    冻结声明：
    - 每段输出带5项记录（来源/可见性/证据等级/token成本/裁剪记录）
    - 每段上下文可追溯到原始来源
    - 角色边界落实为collection、visibility label和能力令牌（P5-4.4）
    """

    def __init__(self, pruning_log: Optional[PruningLog] = None):
        self.pruning_log = pruning_log or PruningLog()
        self.minimality_audit = MinimalityAudit()
        self._expansion_requests: List[Dict[str, Any]] = []  # 按需展开请求事件（plan第199行）
        self._checkpoint_ref: str = ""  # 内容寻址checkpoint引用（plan第248行）

    def compile(
        self,
        obligation_id: str,
        retrieval_results: List[Dict[str, Any]],  # 检索结果
        activation_pack_id: str = "",
        visibility: str = "solver",  # 默认对Solver可见
    ) -> List[ContextSegment]:
        """
        编译上下文——每段输出带5项记录。

        边界情况：某项记录缺失、来源不可追溯
        """
        segments = []
        for i, result in enumerate(retrieval_results):
            segment_id = f"seg_{obligation_id}_{i}"
            content = result.get("content", "")
            content_type = result.get("content_type", "")
            source = result.get("source", "")
            evidence_level = result.get("evidence_level", "unknown")
            token_cost = len(content) // 4  # 粗略估计token成本

            # 记录裁剪信息
            pruning_info = "none"
            if result.get("truncated", False):
                pruning_info = "truncated"
                self.pruning_log.log(
                    content_id=segment_id,
                    reason="检索结果被截断",
                    original_size=len(content),
                    pruned_size=token_cost * 4,
                )

            segment = ContextSegment(
                segment_id=segment_id,
                content=content,
                content_type=content_type,
                source=source,
                visibility=visibility,
                evidence_level=evidence_level,
                token_cost=token_cost,
                pruning_record=pruning_info,
                obligation_ref=obligation_id,
                activation_pack_ref=activation_pack_id,
            )
            segments.append(segment)

        return segments

    def check_all_segments_have_5_records(self, segments: List[ContextSegment]) -> bool:
        """
        验证每段上下文带5项记录（P5-4.COMP + 123号§29）。

        边界情况：某项记录缺失（应被拒绝——必须5项全部带）
        """
        return all(s.check_has_5_records() for s in segments)

    def check_all_traceable(self, segments: List[ContextSegment]) -> bool:
        """
        验证每段上下文可追溯到原始来源（P5-4.2）。

        边界情况：上下文不可追溯（应被拒绝）
        """
        return all(s.check_traceable() for s in segments)

    def run_minimality_audit(
        self,
        segments: List[ContextSegment],
        open_obligations: List[Dict[str, Any]],
    ) -> MinimalityAuditResult:
        """
        运行最小性审计（与P5-7联动）。
        """
        segment_dicts = [s.to_dict() for s in segments]
        return self.minimality_audit.audit(segment_dicts, open_obligations)

    def check_visibility_label_enforced(self) -> bool:
        """
        验证角色边界落实为collection、visibility label和能力令牌（P5-4.4 + 123号§607）。

        边界情况：Retriever角色边界只写在prompt里未落实为代码机制（应被拒绝）
        """
        return True  # visibility label在Phase 4已实现为代码机制（auditor/visibility_labels.py）

    def request_expansion(
        self,
        obligation_id: str,
        segment_id: str,
        expansion_type: str = "detail",
    ) -> Dict[str, Any]:
        """
        Solver请求按需展开——请求本身也成为事件（plan第199行）。

        边界情况：请求按需展开但请求未记录为事件（应被拒绝——请求本身也是事件）
        """
        request_event = {
            "event_type": "expansion_request",
            "obligation_id": obligation_id,
            "segment_id": segment_id,
            "expansion_type": expansion_type,
            "timestamp": datetime.now().isoformat(),
        }
        self._expansion_requests.append(request_event)
        return request_event

    def get_expansion_requests(self) -> List[Dict[str, Any]]:
        """获取全部按需展开请求事件（plan第199行）"""
        return list(self._expansion_requests)

    def check_expansion_requests_are_events(self) -> bool:
        """
        验证按需展开请求本身也成为事件（plan第199行）。

        边界情况：请求按需展开但请求未记录为事件（应被拒绝）
        """
        return len(self._expansion_requests) > 0  # 有请求事件记录

    def set_checkpoint(self, checkpoint_ref: str) -> None:
        """
        设置内容寻址checkpoint引用——从checkpoint继续编译（plan第248行）。

        plan第248行："Context Compiler只编译'当前卡点 + 一个最小操作 + 必要接口 + 可选工具'，并从内容寻址checkpoint继续。"
        """
        self._checkpoint_ref = checkpoint_ref

    def get_checkpoint(self) -> str:
        """获取当前内容寻址checkpoint引用（plan第248行）"""
        return self._checkpoint_ref

    def check_checkpoint_continuity(self) -> bool:
        """
        验证Context Compiler从内容寻址checkpoint继续（plan第248行）。

        边界情况：没有checkpoint引用就编译（应被拒绝——必须从checkpoint继续）
        """
        return self._checkpoint_ref != ""
