"""AdmissionDecision — HumanGate 签名的 case 入实验决定（WP-CS1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 78-82：

HumanGate signs AdmissionDecision and CasePackVersion, freezing
positive/false-friend/boundary/unrelated 角色。

AdmissionDecision 是 HumanGate 签名的决定，将 case 接入实验。
冻结 positive/false-friend/boundary/unrelated 角色。
必须由人类签名，不是模型。

admitted_for_process_only 标记的 case 不得进入 result-layer confirmatory claim。

硬约束（blocker）：
- 必须由人类签名（unsigned → BLOCK）
- model 不能签 G-CASE-ROLE（model self-signing → BLOCK）
- admitted_for_process_only 不得进入 result layer
- 角色冻结必须覆盖所有 CS_CASE_ROLES
- gate_type == G-CASE-ROLE

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    CS_ADMISSION_STATUSES,
    CS_CASE_ROLES,
    CS_GATE_TYPE_CASE_ROLE,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/admission-decision"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "AdmissionDecision"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class AdmissionDecision:
    """AdmissionDecision — HumanGate 签名的 case 入实验决定。不可变。

    字段：
    - decision_id：决定唯一标识
    - case_pack_ref_and_hash：CasePack 引用 {ref_id, sha256}
    - gate_type：门控类型（固定 G-CASE-ROLE）
    - admission_status：准入状态（CS_ADMISSION_STATUSES）
    - frozen_roles：已冻结的角色列表（CS_CASE_ROLES 的子集，必须全覆盖）
    - signed_by_human：是否由人类签名
    - signed_by_model：是否由模型签名（必须为 False）
    - admitted_for_process_only：是否仅用于流程（不进入 result layer）
    - gate_decision_ref_and_hash：HumanGate GateDecision 引用
    - actor_id：签名者 actor ID
    - actor_role：签名者角色
    - nonce：唯一 nonce
    - issued_at：签发时间
    """

    decision_id: str
    case_pack_ref_and_hash: dict[str, str]
    gate_type: str
    admission_status: str
    frozen_roles: list[str]
    signed_by_human: bool
    signed_by_model: bool
    admitted_for_process_only: bool
    gate_decision_ref_and_hash: dict[str, str]
    actor_id: str
    actor_role: str
    nonce: str
    issued_at: str
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    content_hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "decision_id": self.decision_id,
            "case_pack_ref_and_hash": dict(self.case_pack_ref_and_hash),
            "gate_type": self.gate_type,
            "admission_status": self.admission_status,
            "frozen_roles": list(self.frozen_roles),
            "signed_by_human": self.signed_by_human,
            "signed_by_model": self.signed_by_model,
            "admitted_for_process_only": self.admitted_for_process_only,
            "gate_decision_ref_and_hash": dict(self.gate_decision_ref_and_hash),
            "actor_id": self.actor_id,
            "actor_role": self.actor_role,
            "nonce": self.nonce,
            "issued_at": self.issued_at,
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }


def _compute_content_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["content_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def _check_ref_hash(obj: Any, field_name: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not an object")]
    if set(obj.keys()) != {"ref_id", "sha256"}:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must have exactly ref_id and sha256"))
        return errors
    if not obj.get("ref_id"):
        errors.append((EC.CS_EVIDENCE_REF_MISSING, f"{field_name}.ref_id is empty"))
    sha = obj.get("sha256", "")
    if not isinstance(sha, str) or not _HASH_RE.match(sha):
        errors.append((EC.OBJECT_HASH_MISMATCH, f"{field_name}.sha256 is not valid sha256"))
    return errors


def build_admission_decision(
    *,
    decision_id: str,
    case_pack_ref_and_hash: dict[str, str],
    admission_status: str,
    frozen_roles: list[str],
    signed_by_human: bool,
    admitted_for_process_only: bool,
    gate_decision_ref_and_hash: dict[str, str],
    actor_id: str,
    actor_role: str,
    nonce: str,
    issued_at: str,
    signed_by_model: bool = False,
) -> AdmissionDecision:
    """构建 AdmissionDecision，自动计算 content_hash。

    gate_type 固定为 G-CASE-ROLE。
    signed_by_model 默认 False（model 不能签 G-CASE-ROLE）。
    """
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "decision_id": decision_id,
        "case_pack_ref_and_hash": dict(case_pack_ref_and_hash),
        "gate_type": CS_GATE_TYPE_CASE_ROLE,
        "admission_status": admission_status,
        "frozen_roles": list(frozen_roles),
        "signed_by_human": signed_by_human,
        "signed_by_model": signed_by_model,
        "admitted_for_process_only": admitted_for_process_only,
        "gate_decision_ref_and_hash": dict(gate_decision_ref_and_hash),
        "actor_id": actor_id,
        "actor_role": actor_role,
        "nonce": nonce,
        "issued_at": issued_at,
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return AdmissionDecision(
        decision_id=decision_id,
        case_pack_ref_and_hash=dict(case_pack_ref_and_hash),
        gate_type=CS_GATE_TYPE_CASE_ROLE,
        admission_status=admission_status,
        frozen_roles=list(frozen_roles),
        signed_by_human=signed_by_human,
        signed_by_model=signed_by_model,
        admitted_for_process_only=admitted_for_process_only,
        gate_decision_ref_and_hash=dict(gate_decision_ref_and_hash),
        actor_id=actor_id,
        actor_role=actor_role,
        nonce=nonce,
        issued_at=issued_at,
        content_hash=content_hash,
    )


def verify_admission_decision(
    decision_obj: dict[str, Any] | AdmissionDecision,
) -> VerificationResult:
    """验证 AdmissionDecision 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. decision_id 非空
    3. case_pack_ref_and_hash 结构合法
    4. gate_type == G-CASE-ROLE
    5. admission_status 在 CS_ADMISSION_STATUSES 中
    6. frozen_roles 覆盖所有 CS_CASE_ROLES
    7. signed_by_human == True（unsigned → BLOCK）
    8. signed_by_model == False（model self-signing → BLOCK）
    9. gate_decision_ref_and_hash 结构合法
    10. actor_id / actor_role / nonce / issued_at 非空
    11. content_hash 正确
    """
    if isinstance(decision_obj, AdmissionDecision):
        decision_obj = decision_obj.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if decision_obj.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if decision_obj.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if decision_obj.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not decision_obj.get("decision_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("decision_id must not be empty")

    for code, detail in _check_ref_hash(
        decision_obj.get("case_pack_ref_and_hash", {}), "case_pack_ref_and_hash"
    ):
        errors.append(code)
        details.append(detail)

    if decision_obj.get("gate_type") != CS_GATE_TYPE_CASE_ROLE:
        errors.append(EC.CS_ADMISSION_ROLE_UNKNOWN)
        details.append(f"gate_type must be {CS_GATE_TYPE_CASE_ROLE}, got {decision_obj.get('gate_type')!r}")

    admission_status = decision_obj.get("admission_status", "")
    if admission_status not in CS_ADMISSION_STATUSES:
        errors.append(EC.CS_ADMISSION_STATE_INVALID)
        details.append(
            f"admission_status {admission_status!r} not in CS_ADMISSION_STATUSES "
            f"{sorted(CS_ADMISSION_STATUSES)}"
        )

    # frozen_roles must cover all CS_CASE_ROLES
    frozen_roles = decision_obj.get("frozen_roles", [])
    if not isinstance(frozen_roles, list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("frozen_roles must be a list")
    else:
        frozen_set = set(frozen_roles)
        for required_role in CS_CASE_ROLES:
            if required_role not in frozen_set:
                errors.append(EC.CS_ROLE_NOT_FROZEN)
                details.append(f"role {required_role!r} not in frozen_roles (must freeze all roles)")
        # Check for unknown roles
        unknown_roles = frozen_set - CS_CASE_ROLES
        if unknown_roles:
            errors.append(EC.CS_ADMISSION_ROLE_UNKNOWN)
            details.append(f"unknown roles in frozen_roles: {unknown_roles}")

    # signed_by_human (blocker: unsigned admission)
    if decision_obj.get("signed_by_human") is not True:
        errors.append(EC.CS_ADMISSION_DECISION_UNSIGNED)
        details.append("signed_by_human must be True (unsigned AdmissionDecision → BLOCK)")

    # signed_by_model (blocker: model self-signing role)
    if decision_obj.get("signed_by_model") is True:
        errors.append(EC.CS_MODEL_SELF_SIGNED_ROLE)
        details.append("signed_by_model must be False (model cannot sign G-CASE-ROLE)")

    for code, detail in _check_ref_hash(
        decision_obj.get("gate_decision_ref_and_hash", {}),
        "gate_decision_ref_and_hash",
    ):
        errors.append(code)
        details.append(detail)

    for field_name in ("actor_id", "actor_role", "nonce", "issued_at"):
        if not decision_obj.get(field_name):
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"{field_name} must not be empty")

    if decision_obj.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {decision_obj.get('content_hash_algorithm')}")

    computed = _compute_content_hash(decision_obj)
    if decision_obj.get("content_hash") != computed:
        errors.append(EC.CS_CASE_PACK_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {decision_obj.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_process_only_not_in_result_layer(
    decision: dict[str, Any] | AdmissionDecision,
    *,
    result_layer_claim: dict[str, Any] | None = None,
) -> VerificationResult:
    """检查 admitted_for_process_only 不进入 result layer。

    blocker: process-only entering result layer → BLOCK

    如果 decision.admitted_for_process_only == True 且
    result_layer_claim 引用了该 decision/case_pack，则 BLOCK。
    """
    if isinstance(decision, AdmissionDecision):
        decision = decision.to_dict()

    if not decision.get("admitted_for_process_only"):
        return VerificationResult(verdict="PASS")

    if result_layer_claim is None:
        return VerificationResult(verdict="PASS")

    # Check if result_layer_claim references this case_pack or decision
    case_pack_ref = decision.get("case_pack_ref_and_hash", {}).get("ref_id", "")
    decision_id = decision.get("decision_id", "")

    claim_str = str(result_layer_claim)
    if case_pack_ref and case_pack_ref in claim_str:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.CS_PROCESS_ONLY_IN_RESULT_LAYER],
            details=[
                f"admitted_for_process_only case_pack {case_pack_ref!r} "
                f"found in result-layer confirmatory claim"
            ],
        )
    if decision_id and decision_id in claim_str:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.CS_PROCESS_ONLY_IN_RESULT_LAYER],
            details=[
                f"admitted_for_process_only decision {decision_id!r} "
                f"found in result-layer confirmatory claim"
            ],
        )

    return VerificationResult(verdict="PASS")
