"""NoChangeDecision — 签名决定无需修订，不解封 holdout。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P8 节：

No revision needed → signed NoChangeDecision, do not unseal holdout.

关键约束（blocker）：
- NoChangeDecision 必须签名（HumanGate）→ RV_NOCHANGE_NOT_SIGNED
- NoChangeDecision 不解封 holdout → RV_NOCHANGE_UNSEALS_HOLDOUT
- 引用 EvidenceIndex → RV_NOCHANGE_REFERENCES_EVIDENCE_INDEX
- state 不在 RV_NOCHANGE_STATES → RV_NOCHANGE_STATE_INVALID
- content_hash 不匹配 → RV_NOCHANGE_HASH_MISMATCH

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
    RV_NOCHANGE_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/no-change-decision"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class NoChangeDecision:
    """签名决定无需修订。不解封 holdout。

    字段：
        decision_id: 唯一标识
        provenance_snapshot_hash: 引用的 ProvenanceSnapshot content_hash
        localization_hash: 引用的 FailureLocalization content_hash
        state: 状态（RV_NOCHANGE_STATES）
        rationale: 决定理由
        signed: 是否已签名（HumanGate）
        gate_decision_ref: HumanGate GateDecision 引用 {decision_id, decision_hash}
        holdout_unsealed: 是否解封 holdout（必须 False）
        decided_at: 决定时间
        hash_algorithm: 哈希算法
        content_hash: 内容哈希
    """

    decision_id: str
    provenance_snapshot_hash: str = ""
    localization_hash: str = ""
    state: str = "DRAFT"
    rationale: str = ""
    signed: bool = False
    gate_decision_ref: dict[str, str] = field(default_factory=dict)
    holdout_unsealed: bool = False
    decided_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "decision_id": self.decision_id,
            "provenance_snapshot_hash": self.provenance_snapshot_hash,
            "localization_hash": self.localization_hash,
            "state": self.state,
            "rationale": self.rationale,
            "signed": self.signed,
            "gate_decision_ref": dict(self.gate_decision_ref),
            "holdout_unsealed": self.holdout_unsealed,
            "decided_at": self.decided_at,
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


@dataclass(frozen=True)
class NoChangeDecisionVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    decision_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def make_no_change_decision(
    *,
    decision_id: str,
    provenance_snapshot_hash: str,
    localization_hash: str,
    rationale: str = "",
    signed: bool = False,
    gate_decision_ref: dict[str, str] | None = None,
    decided_at: str | None = None,
) -> NoChangeDecision:
    """构建 NoChangeDecision。

    holdout_unsealed 强制为 False（NoChangeDecision 不解封 holdout）。
    """
    decided_at = decided_at or datetime.now(timezone.utc).isoformat()
    state = "SIGNED" if signed else "DRAFT"
    dec = NoChangeDecision(
        decision_id=decision_id,
        provenance_snapshot_hash=provenance_snapshot_hash,
        localization_hash=localization_hash,
        state=state,
        rationale=rationale,
        signed=signed,
        gate_decision_ref=dict(gate_decision_ref or {}),
        holdout_unsealed=False,
        decided_at=decided_at,
    )
    return dataclasses.replace(dec, content_hash=dec.compute_content_hash())


def verify_no_change_decision(
    dec: NoChangeDecision,
) -> NoChangeDecisionVerificationResult:
    """验证 NoChangeDecision。

    blocker：
    - 未签名 → RV_NOCHANGE_NOT_SIGNED
- 解封 holdout → RV_NOCHANGE_UNSEALS_HOLDOUT
    - 引用 EvidenceIndex → RV_NOCHANGE_REFERENCES_EVIDENCE_INDEX
    - state 不在 RV_NOCHANGE_STATES → RV_NOCHANGE_STATE_INVALID
    - content_hash 不匹配 → RV_NOCHANGE_HASH_MISMATCH
    """
    errors: list[EC] = []
    details: list[str] = []

    d = dec.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not dec.decision_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("decision_id is empty")

    if not dec.provenance_snapshot_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("provenance_snapshot_hash is empty")

    if not dec.localization_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("localization_hash is empty")

    # state 合法性
    if dec.state not in RV_NOCHANGE_STATES:
        errors.append(EC.RV_NOCHANGE_STATE_INVALID)
        details.append(f"state {dec.state!r} not in RV_NOCHANGE_STATES")

    # 签名约束
    if not dec.signed:
        errors.append(EC.RV_NOCHANGE_NOT_SIGNED)
        details.append("NoChangeDecision must be signed (HumanGate)")
    if dec.signed and not dec.gate_decision_ref:
        errors.append(EC.RV_NOCHANGE_NOT_SIGNED)
        details.append("signed NoChangeDecision must reference a GateDecision")

    # 不解封 holdout
    if dec.holdout_unsealed:
        errors.append(EC.RV_NOCHANGE_UNSEALS_HOLDOUT)
        details.append("NoChangeDecision must not unseal holdout")

    # 不得引用 EvidenceIndex
    blob = canonical_json_bytes(d)
    if b"EvidenceIndex" in blob:
        errors.append(EC.RV_NOCHANGE_REFERENCES_EVIDENCE_INDEX)
        details.append("NoChangeDecision references EvidenceIndex — P8 must not read final EvidenceIndex")

    # content_hash
    if not dec.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif dec.content_hash != dec.compute_content_hash():
        errors.append(EC.RV_NOCHANGE_HASH_MISMATCH)
        details.append("NoChangeDecision content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return NoChangeDecisionVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        decision_id=dec.decision_id,
    )


def check_nochange_does_not_unseal_holdout(dec: NoChangeDecision) -> VerificationResult:
    """检查 NoChangeDecision 不解封 holdout。"""
    errors: list[EC] = []
    details: list[str] = []
    if dec.holdout_unsealed:
        errors.append(EC.RV_NOCHANGE_UNSEALS_HOLDOUT)
        details.append("NoChangeDecision must not unseal holdout")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
