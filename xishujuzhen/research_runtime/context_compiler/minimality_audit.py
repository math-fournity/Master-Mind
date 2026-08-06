"""
最小性审计——3项审计：冗余/缺失/预载

对应135号P5-7.2 + 123号§23(最小提示受约束多目标选择)。

冻结声明（153号v2 F9预防修正）：
- 3项审计方法（代码必须实现全部3项，不只是"验证上下文最小"的概括）：
  1. 冗余审计：检查每段内容是否被当前义务的推理路径直接需要。不需要的内容必须裁剪。
  2. 缺失审计：检查当前义务的推理路径是否缺少必要内容。
  3. 预载审计：检查上下文是否预载了未来答案路线（与P5-7.3联动）。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class AuditType(str, Enum):
    """3项审计类型"""
    REDUNDANCY = "redundancy"    # 冗余审计
    MISSING = "missing"          # 缺失审计
    PRELOADING = "preloading"    # 预载审计


@dataclass
class AuditFinding:
    """审计发现"""
    audit_type: str  # AuditType枚举值
    content_id: str
    severity: str  # info/warning/error
    description: str
    recommendation: str = ""  # 建议操作

    def to_dict(self) -> dict:
        return {
            "audit_type": self.audit_type,
            "content_id": self.content_id,
            "severity": self.severity,
            "description": self.description,
            "recommendation": self.recommendation,
        }


@dataclass
class MinimalityAuditResult:
    """最小性审计结果"""
    redundancy_findings: List[AuditFinding] = field(default_factory=list)
    missing_findings: List[AuditFinding] = field(default_factory=list)
    preloading_findings: List[AuditFinding] = field(default_factory=list)
    passed: bool = False

    def to_dict(self) -> dict:
        return {
            "redundancy_findings": [f.to_dict() for f in self.redundancy_findings],
            "missing_findings": [f.to_dict() for f in self.missing_findings],
            "preloading_findings": [f.to_dict() for f in self.preloading_findings],
            "passed": self.passed,
        }


class MinimalityAudit:
    """
    最小性审计（135号P5-7.2）。

    冻结声明：
    - 3项审计：冗余/缺失/预载
    - 上下文最小性审计通过（P5-7.COMP + 123号§23："以尽量少的信息达到足够进展"）
    - 不预载未来答案路线（P5-7.COMP2 + NO-2约束）
    """

    # 预载审计的答案路线关键词
    ANSWER_ROUTE_KEYWORDS = [
        "完整解法", "complete_solution", "最终答案", "final_answer",
        "ground_truth", "truth_vault", "完整证明路径", "complete_proof_path",
    ]

    def audit(
        self,
        context_segments: List[Dict[str, Any]],  # Context Compiler输出的段列表
        open_obligations: List[Dict[str, Any]],  # 当前open义务列表
    ) -> MinimalityAuditResult:
        """
        执行3项最小性审计。

        边界情况：
        - 上下文过多（有冗余——审计1触发）
        - 上下文过少（缺失关键信息——审计2触发）
        - 上下文预载未来路线（审计3触发）

        F-176-5修正：添加输入验证和异常处理。
        """
        # F-176-5：输入验证
        if not isinstance(context_segments, list):
            raise TypeError(f"context_segments必须是list，实际是{type(context_segments).__name__}")
        if not isinstance(open_obligations, list):
            raise TypeError(f"open_obligations必须是list，实际是{type(open_obligations).__name__}")

        try:
            redundancy = self._audit_redundancy(context_segments, open_obligations)
            missing = self._audit_missing(context_segments, open_obligations)
            preloading = self._audit_preloading(context_segments)
        except (KeyError, TypeError, AttributeError) as e:
            raise ValueError(f"最小性审计执行失败——输入格式错误: {e}") from e

        # 审计通过条件：无冗余error + 无缺失error + 无预载error
        passed = (
            not any(f.severity == "error" for f in redundancy) and
            not any(f.severity == "error" for f in missing) and
            not any(f.severity == "error" for f in preloading)
        )

        return MinimalityAuditResult(
            redundancy_findings=redundancy,
            missing_findings=missing,
            preloading_findings=preloading,
            passed=passed,
        )

    def _audit_redundancy(
        self,
        context_segments: List[Dict[str, Any]],
        open_obligations: List[Dict[str, Any]],
    ) -> List[AuditFinding]:
        """
        冗余审计：检查每段内容是否被当前义务的推理路径直接需要（P5-7.2审计1）。

        审计方法：对每段内容，回溯当前O_t中的open义务，确认该内容是某个义务的前提/工具/表示/证据。
        无法回溯到任何open义务的内容标记为冗余。
        """
        findings = []
        open_obligation_ids = [o.get("obligation_id", "") for o in open_obligations]

        for segment in context_segments:
            segment_id = segment.get("segment_id", segment.get("content_id", ""))
            obligation_ref = segment.get("obligation_ref", "")

            if obligation_ref and obligation_ref in open_obligation_ids:
                continue  # 可以回溯到open义务——不是冗余

            # 无法回溯到任何open义务——标记为冗余
            findings.append(AuditFinding(
                audit_type=AuditType.REDUNDANCY.value,
                content_id=segment_id,
                severity="warning",
                description=f"内容{segment_id}无法回溯到任何open义务——可能是冗余",
                recommendation="裁剪此内容",
            ))

        return findings

    def _audit_missing(
        self,
        context_segments: List[Dict[str, Any]],
        open_obligations: List[Dict[str, Any]],
    ) -> List[AuditFinding]:
        """
        缺失审计：检查当前义务的推理路径是否缺少必要内容（P5-7.2审计2）。

        审计方法：对每个open义务，检查其前提/工具/表示/证据是否全部在上下文中。
        缺少任何必要项标记为缺失。
        """
        findings = []

        for obligation in open_obligations:
            obligation_id = obligation.get("obligation_id", "")
            required_items = obligation.get("required_items", [])

            # 检查每个必要项是否在上下文中
            for required in required_items:
                found = False
                for segment in context_segments:
                    if segment.get("obligation_ref") == obligation_id and segment.get("content_type") == required:
                        found = True
                        break

                if not found:
                    findings.append(AuditFinding(
                        audit_type=AuditType.MISSING.value,
                        content_id=obligation_id,
                        severity="warning",
                        description=f"义务{obligation_id}缺少必要内容：{required}",
                        recommendation=f"补充{required}类型的内容",
                    ))

        return findings

    def _audit_preloading(self, context_segments: List[Dict[str, Any]]) -> List[AuditFinding]:
        """
        预载审计：检查上下文是否预载了未来答案路线（P5-7.2审计3 + P5-7.3联动）。

        审计方法：检查上下文中是否有超出当前义务范围的完整解题路径或答案直接材料。
        """
        findings = []

        for segment in context_segments:
            segment_id = segment.get("segment_id", segment.get("content_id", ""))
            content = segment.get("content", "").lower()

            for keyword in self.ANSWER_ROUTE_KEYWORDS:
                if keyword.lower() in content:
                    findings.append(AuditFinding(
                        audit_type=AuditType.PRELOADING.value,
                        content_id=segment_id,
                        severity="error",
                        description=f"内容{segment_id}预载了未来答案路线：检测到关键词'{keyword}'",
                        recommendation="移除此内容——不预载未来答案路线（P5-EXIT-2）",
                    ))
                    break

        return findings

    def check_no_preload(self, context_segments: List[Dict[str, Any]]) -> bool:
        """
        验证不预载未来答案路线（P5-7.3 + P5-EXIT-2 + P5-7.COMP2 + NO-2约束）。

        边界情况：上下文预载未来答案路线（应被拒绝）
        """
        preloading = self._audit_preloading(context_segments)
        return len(preloading) == 0
