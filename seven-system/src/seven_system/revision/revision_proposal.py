"""RevisionProposal — 受控修订提案。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P8 节：

Need revision → RevisionProposal, fit/regression, candidate freeze, one-time
prospective, two HumanGate.

关键约束（blocker）：
- RevisionProposal 必须签名 → RV_REVISION_PROPOSAL_NOT_SIGNED
- 需要两个 HumanGate 批准 → RV_REVISION_WITHOUT_TWO_GATES / RV_REVISION_GATE_COUNT_INSUFFICIENT
- 引用 EvidenceIndex → RV_REVISION_REFERENCES_EVIDENCE_INDEX
- state 不在 RV_REVISION_PROPOSAL_STATES → RV_REVISION_PROPOSAL_STATE_INVALID
- content_hash 不匹配 → RV_REVISION_PROPOSAL_HASH_MISMATCH

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    RV_REVISION_PROPOSAL_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/revision-proposal"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class RevisionProposal:
    """受控修订提案。

    字段：
        proposal_id: 唯一标识
        provenance_snapshot_hash: 引用的 ProvenanceSnapshot content_hash
        localization_hash: 引用的 FailureLocalization content_hash
        what_to_change: 修订内容描述
        fit_regression_plan: fit/regression 计划
        candidate_freeze_ref: candidate freeze 引用 {candidate_id, content_hash}
        prospective_ref: 一次性 prospective 引用 {prospective_id, content_hash}
        state: 状态（RV_REVISION_PROPOSAL_STATES）
        signed: 是否已签名（HumanGate）
        gate_decision_refs: HumanGate GateDecision 引用列表（需两个）
        proposed_at: 提案时间
        hash_algorithm: 哈希算法
        content_hash: 内容哈希
    """

    proposal_id: str
    provenance_snapshot_hash: str = ""
    localization_hash: str = ""
    what_to_change: str = ""
    fit_regression_plan: str = ""
    candidate_freeze_ref: dict[str, str] = field(default_factory=dict)
    prospective_ref: dict[str, str] = field(default_factory=dict)
    state: str = "DRAFT"
    signed: bool = False
    gate_decision_refs: tuple[dict[str, str], ...] = ()
    proposed_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "proposal_id": self.proposal_id,
            "provenance_snapshot_hash": self.provenance_snapshot_hash,
            "localization_hash": self.localization_hash,
            "what_to_change": self.what_to_change,
            "fit_regression_plan": self.fit_regression_plan,
            "candidate_freeze_ref": dict(self.candidate_freeze_ref),
            "prospective_ref": dict(self.prospective_ref),
            "state": self.state,
            "signed": self.signed,
            "gate_decision_refs": [dict(ref) for ref in self.gate_decision_refs],
            "proposed_at": self.proposed_at,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()

    @property
    def gate_count(self) -> int:
        return len(self.gate_decision_refs)


def make_revision_proposal(
    *,
    proposal_id: str,
    provenance_snapshot_hash: str,
    localization_hash: str,
    what_to_change: str = "",
    fit_regression_plan: str = "",
    candidate_freeze_ref: dict[str, str] | None = None,
    prospective_ref: dict[str, str] | None = None,
    signed: bool = False,
    gate_decision_refs: list[dict[str, str]] | None = None,
    proposed_at: str | None = None,
) -> RevisionProposal:
    """构建 RevisionProposal。

    state 根据 gate 数量派生：0→DRAFT/PROPOSED，1→ONE_GATE_APPROVED，>=2→TWO_GATE_APPROVED。
    """
    proposed_at = proposed_at or datetime.now(timezone.utc).isoformat()
    gates = list(gate_decision_refs or [])
    if not signed:
        state = "DRAFT" if not gates else "PROPOSED"
    elif len(gates) >= 2:
        state = "TWO_GATE_APPROVED"
    elif len(gates) == 1:
        state = "ONE_GATE_APPROVED"
    else:
        state = "PROPOSED"

    prop = RevisionProposal(
        proposal_id=proposal_id,
        provenance_snapshot_hash=provenance_snapshot_hash,
        localization_hash=localization_hash,
        what_to_change=what_to_change,
        fit_regression_plan=fit_regression_plan,
        candidate_freeze_ref=dict(candidate_freeze_ref or {}),
        prospective_ref=dict(prospective_ref or {}),
        state=state,
        signed=signed,
        gate_decision_refs=tuple(dict(g) for g in gates),
        proposed_at=proposed_at,
    )
    return dataclasses.replace(prop, content_hash=prop.compute_content_hash())


def verify_revision_proposal(
    prop: RevisionProposal,
) -> RevisionProposalVerificationResult:
    """验证 RevisionProposal。

    blocker：
    - 未签名 → RV_REVISION_PROPOSAL_NOT_SIGNED
    - 无两个 HumanGate 批准 → RV_REVISION_WITHOUT_TWO_GATES / RV_REVISION_GATE_COUNT_INSUFFICIENT
    - 引用 EvidenceIndex → RV_REVISION_REFERENCES_EVIDENCE_INDEX
    - state 不合法 → RV_REVISION_PROPOSAL_STATE_INVALID
    - content_hash 不匹配 → RV_REVISION_PROPOSAL_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = prop.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not prop.proposal_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("proposal_id is empty")

    if not prop.provenance_snapshot_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("provenance_snapshot_hash is empty")

    if not prop.localization_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("localization_hash is empty")

    # state 合法性
    if prop.state not in RV_REVISION_PROPOSAL_STATES:
        errors.append(EC.RV_REVISION_PROPOSAL_STATE_INVALID)
        details.append(f"state {prop.state!r} not in RV_REVISION_PROPOSAL_STATES")

    # 签名约束
    if not prop.signed:
        errors.append(EC.RV_REVISION_PROPOSAL_NOT_SIGNED)
        details.append("RevisionProposal must be signed (HumanGate)")

    # 两个 HumanGate 批准约束
    if prop.gate_count < 2:
        errors.append(EC.RV_REVISION_WITHOUT_TWO_GATES)
        details.append(
            f"RevisionProposal requires two HumanGate approvals, got {prop.gate_count}"
        )
        errors.append(EC.RV_REVISION_GATE_COUNT_INSUFFICIENT)
        details.append(f"gate count {prop.gate_count} < 2")

    # 不得引用 EvidenceIndex
    blob = canonical_json_bytes(d)
    if b"EvidenceIndex" in blob:
        errors.append(EC.RV_REVISION_REFERENCES_EVIDENCE_INDEX)
        details.append("RevisionProposal references EvidenceIndex — P8 must not read final EvidenceIndex")

    # content_hash
    if not prop.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif prop.content_hash != prop.compute_content_hash():
        errors.append(EC.RV_REVISION_PROPOSAL_HASH_MISMATCH)
        details.append("RevisionProposal content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return RevisionProposalVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        proposal_id=prop.proposal_id,
    )


@dataclass(frozen=True)
class RevisionProposalVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    proposal_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def check_revision_two_human_gates(prop: RevisionProposal) -> VerificationResult:
    """检查 RevisionProposal 需要两个 HumanGate 批准。"""
    errors: list[EC] = []
    details: list[str] = []
    if prop.gate_count < 2:
        errors.append(EC.RV_REVISION_WITHOUT_TWO_GATES)
        details.append(f"RevisionProposal requires two HumanGate approvals, got {prop.gate_count}")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
