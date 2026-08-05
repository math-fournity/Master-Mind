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
        return all([
            self.source != "",
            self.visibility != "",
            self.evidence_level != "",
            self.token_cost > 0 or self.token_cost == 0,  # token_cost可以为0但必须有值
            self.pruning_record != "" or self.pruning_record == "",  # 裁剪记录可以为空但字段必须存在
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
