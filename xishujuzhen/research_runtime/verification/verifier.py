"""
Verifier角色：输出6种状态而非布尔值

对应132号P2-ROLE-2 + 127号§10 + 123号§28。

123号§28 + 系统探讨.md§5.5：
- Verifier输出proven/formally_verified/computationally_supported/numerically_tested/contradicted/unknown
- 不是单一布尔值

角色隔离（127号§10）：
- 可见：明确命题、前提、证明片段、工具输入、期望证据等级
- 不能做：决定下一研究路线
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

from ..state_reducer.evidence import EvidenceStore, EvidenceKind, EvidencePolarity, EvidenceStatus, DerivedEpistemicState


class VerifierOutput(str, Enum):
    """
    Verifier的6种输出状态（123号§28 + 系统探讨.md§5.5）。

    不是单一布尔值——Verifier输出认识状态而非true/false。
    """
    PROVEN = "proven"                             # 已证明（形式证明通过）
    FORMALLY_VERIFIED = "formally_verified"       # 形式验证（Lean/Coq等验证器通过）
    COMPUTATIONALLY_SUPPORTED = "computationally_supported"  # 计算支持（符号计算支持）
    NUMERICALLY_TESTED = "numerically_tested"     # 数值检验（数值验证通过但无形式证明）
    CONTRADICTED = "contradicted"                 # 矛盾（有反例或矛盾证据）
    UNKNOWN = "unknown"                           # 未知（证据不足）


@dataclass
class VerificationResult:
    """
    验证结果——Verifier的输出。

    包含6种状态之一 + 证据引用 + 范围 + 失败原因。
    """
    output: VerifierOutput
    claim_id: str
    evidence_refs: List[str] = field(default_factory=list)
    scope: str = ""
    failure_reason: str = ""

    def to_dict(self) -> dict:
        return {
            "output": self.output.value,
            "claim_id": self.claim_id,
            "evidence_refs": self.evidence_refs,
            "scope": self.scope,
            "failure_reason": self.failure_reason,
        }


class Verifier:
    """
    Verifier角色（132号P2-ROLE-2）。

    角色隔离：
    - 可见：明确命题、前提、证明片段、工具输入、期望证据等级
    - 不能做：决定下一研究路线
    - 输出：6种状态而非布尔值

    冻结声明（P2-ROLE.COMP2）：
    - Verifier只返回6种状态之一，不返回true/false
    - Verifier不决定下一研究路线
    """

    def __init__(self, evidence_store: EvidenceStore):
        self.evidence_store = evidence_store

    def verify(
        self,
        claim_id: str,
        required_kinds: List[EvidenceKind] = None,
    ) -> VerificationResult:
        """
        验证一个命题。

        根据证据类型和状态输出6种状态之一。

        边界情况：
        - 无证据 → unknown
        - 有形式证明证据 → formally_verified
        - 有符号计算证据 → computationally_supported
        - 有数值证据 → numerically_tested
        - 有反例证据 → contradicted
        - 证据不足 → unknown
        """
        evidence_list = self.evidence_store.get_evidence_for_claim(claim_id)

        if not evidence_list:
            return VerificationResult(
                output=VerifierOutput.UNKNOWN,
                claim_id=claim_id,
                failure_reason="无证据",
            )

        # 只考虑active状态的证据
        active = [e for e in evidence_list if e["status"] == EvidenceStatus.ACTIVE.value]

        if not active:
            return VerificationResult(
                output=VerifierOutput.UNKNOWN,
                claim_id=claim_id,
                failure_reason="无active状态证据",
            )

        # 检查是否有反驳证据（反例）
        refute_evidence = [e for e in active if e["polarity"] == EvidencePolarity.REFUTE.value]
        if refute_evidence:
            return VerificationResult(
                output=VerifierOutput.CONTRADICTED,
                claim_id=claim_id,
                evidence_refs=[e["evidence_id"] for e in refute_evidence],
                failure_reason="存在反例/反驳证据",
            )

        # 检查支持证据的类型
        support = [e for e in active if e["polarity"] == EvidencePolarity.SUPPORT.value]

        if not support:
            return VerificationResult(
                output=VerifierOutput.UNKNOWN,
                claim_id=claim_id,
                failure_reason="无支持证据",
            )

        # 按证据类型确定验证等级
        support_kinds = set(e["kind"] for e in support)

        # formally_verified：有formal_proof证据
        if EvidenceKind.FORMAL_PROOF.value in support_kinds:
            return VerificationResult(
                output=VerifierOutput.FORMALLY_VERIFIED,
                claim_id=claim_id,
                evidence_refs=[e["evidence_id"] for e in support if e["kind"] == EvidenceKind.FORMAL_PROOF.value],
            )

        # computationally_supported：有symbolic证据
        if EvidenceKind.SYMBOLIC.value in support_kinds:
            return VerificationResult(
                output=VerifierOutput.COMPUTATIONALLY_SUPPORTED,
                claim_id=claim_id,
                evidence_refs=[e["evidence_id"] for e in support if e["kind"] == EvidenceKind.SYMBOLIC.value],
            )

        # numerically_tested：有numerical证据
        if EvidenceKind.NUMERICAL.value in support_kinds:
            return VerificationResult(
                output=VerifierOutput.NUMERICALLY_TESTED,
                claim_id=claim_id,
                evidence_refs=[e["evidence_id"] for e in support if e["kind"] == EvidenceKind.NUMERICAL.value],
            )

        # proven：有human_audit证据（人工审计确认）
        if EvidenceKind.HUMAN_AUDIT.value in support_kinds:
            return VerificationResult(
                output=VerifierOutput.PROVEN,
                claim_id=claim_id,
                evidence_refs=[e["evidence_id"] for e in support if e["kind"] == EvidenceKind.HUMAN_AUDIT.value],
            )

        # 其他情况（如只有literature证据）
        return VerificationResult(
            output=VerifierOutput.UNKNOWN,
            claim_id=claim_id,
            evidence_refs=[e["evidence_id"] for e in support],
            failure_reason="证据类型不足以判定验证等级",
        )

    def verify_with_gate(
        self,
        claim_id: str,
        required_kinds: List[EvidenceKind],
    ) -> VerificationResult:
        """
        按验证门验证——检查是否有required_kinds中的active支持证据。

        边界情况：
        - Verifier尝试返回布尔值（应被拒绝——必须返回6种状态之一）
        - Verifier尝试决定下一研究路线（应被拒绝）
        """
        result = self.verify(claim_id)

        # 检查验证门是否满足
        evidence_list = self.evidence_store.get_evidence_for_claim(claim_id)
        active = [e for e in evidence_list if e["status"] == EvidenceStatus.ACTIVE.value]
        has_required = any(
            e["kind"] in [k.value for k in required_kinds]
            and e["polarity"] == EvidencePolarity.SUPPORT.value
            for e in active
        )

        if not has_required and result.output not in (VerifierOutput.CONTRADICTED,):
            return VerificationResult(
                output=VerifierOutput.UNKNOWN,
                claim_id=claim_id,
                failure_reason=f"验证门未满足——需要{[k.value for k in required_kinds]}类型的active支持证据",
            )

        return result
