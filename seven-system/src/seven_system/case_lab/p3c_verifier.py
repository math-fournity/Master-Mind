"""P3CVerifier — P3C case role freeze 验签器（WP-CS1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 78-82：

Merge natural case P2A/[P2B]+P3N or generated case P3A+P3B evidence.
HumanGate signs AdmissionDecision and CasePackVersion, freezing
positive/false-friend/boundary/unrelated等角色。

Model can only give suggestions, cannot sign G-CASE-ROLE.
admitted_for_process_only must NOT enter result-layer confirmatory claim.

P3C 验签检查：
1. 所有角色由人类签名（不是模型）
2. admitted_for_process_only 排除在 result layer 之外
3. evidence refs 有效
4. hashes 匹配
5. AdmissionDecision 已签名
6. CasePackVersion 已冻结

硬约束（blocker）：
- model self-signing role → BLOCK
- process-only entering result layer → BLOCK
- missing evidence refs → BLOCK
- hash mismatch → BLOCK
- unsigned AdmissionDecision → BLOCK
- role without evidence → BLOCK

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    CS_P3C_STATES,
    CS_CASE_ROLES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from .case_pack import CasePack, CasePackVersion, verify_case_pack, verify_case_pack_version
from .case_role import CaseRole, verify_case_role
from .admission_decision import AdmissionDecision, verify_admission_decision


_SCHEMA_ID = "seven/p3c-verification-report"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "P3CVerificationReport"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-report_hash-null)"


@dataclass(frozen=True)
class P3CVerificationReport:
    """P3CVerificationReport — P3C 验签报告。不可变。

    字段：
    - report_id：报告唯一标识
    - case_pack_ref_and_hash：验签的 CasePack 引用
    - p3c_state：P3C 状态（CS_P3C_STATES: UNVERIFIED / VERIFIED / BLOCKED）
    - all_roles_signed_by_human：所有角色是否由人类签名
    - process_only_excluded：process-only 是否排除在 result layer 之外
    - evidence_refs_valid：证据引用是否有效
    - hashes_match：hashes 是否匹配
    - admission_signed：AdmissionDecision 是否已签名
    - roles_have_evidence：角色是否有证据
    - error_codes：错误码列表
    - details：详细信息列表
    """

    report_id: str
    case_pack_ref_and_hash: dict[str, str]
    p3c_state: str
    all_roles_signed_by_human: bool
    process_only_excluded: bool
    evidence_refs_valid: bool
    hashes_match: bool
    admission_signed: bool
    roles_have_evidence: bool
    error_codes: list[str]
    details: list[str]
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    report_hash_algorithm: str = _HASH_ALGORITHM
    report_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "report_id": self.report_id,
            "case_pack_ref_and_hash": dict(self.case_pack_ref_and_hash),
            "p3c_state": self.p3c_state,
            "all_roles_signed_by_human": self.all_roles_signed_by_human,
            "process_only_excluded": self.process_only_excluded,
            "evidence_refs_valid": self.evidence_refs_valid,
            "hashes_match": self.hashes_match,
            "admission_signed": self.admission_signed,
            "roles_have_evidence": self.roles_have_evidence,
            "error_codes": list(self.error_codes),
            "details": list(self.details),
            "report_hash_algorithm": self.report_hash_algorithm,
            "report_hash": self.report_hash,
        }


def _compute_report_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["report_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


class P3CVerifier:
    """P3CVerifier — P3C case role freeze 验签器。

    验签 P3C case role freeze 的完整性：
    1. 所有角色由人类签名（不是模型）
    2. admitted_for_process_only 排除在 result layer 之外
    3. evidence refs 有效
    4. hashes 匹配
    5. AdmissionDecision 已签名
    6. CasePackVersion 已冻结
    7. 每个角色有证据
    """

    def verify(
        self,
        *,
        case_pack: dict[str, Any] | CasePack,
        case_pack_version: dict[str, Any] | CasePackVersion,
        admission_decision: dict[str, Any] | AdmissionDecision,
        case_roles: list[dict[str, Any] | CaseRole],
        result_layer_claim: dict[str, Any] | None = None,
        report_id: str = "p3c-verify-report",
    ) -> P3CVerificationReport:
        """执行 P3C 验签。

        参数：
        - case_pack：CasePack 对象或 dict
        - case_pack_version：CasePackVersion 对象或 dict
        - admission_decision：AdmissionDecision 对象或 dict
        - case_roles：CaseRole 列表
        - result_layer_claim：result layer claim（用于检查 process-only 排除）
        - report_id：报告 ID

        返回 P3CVerificationReport。
        """
        all_errors: list[EC] = []
        all_details: list[str] = []

        all_roles_signed = True
        process_only_excluded = True
        evidence_valid = True
        hashes_match = True
        admission_signed = True
        roles_have_evidence = True

        # 1. Verify CasePack
        pack_result = verify_case_pack(case_pack)
        if not pack_result.passed:
            all_errors.extend(pack_result.error_codes)
            all_details.extend(pack_result.details)
            hashes_match = False

        # 2. Verify CasePackVersion
        version_result = verify_case_pack_version(case_pack_version)
        if not version_result.passed:
            all_errors.extend(version_result.error_codes)
            all_details.extend(version_result.details)
            hashes_match = False

        # 3. Verify AdmissionDecision
        admission_result = verify_admission_decision(admission_decision)
        if not admission_result.passed:
            all_errors.extend(admission_result.error_codes)
            all_details.extend(admission_result.details)
            admission_signed = False

        # Check admission signed_by_human
        if isinstance(admission_decision, AdmissionDecision):
            ad_dict = admission_decision.to_dict()
        else:
            ad_dict = admission_decision
        if ad_dict.get("signed_by_human") is not True:
            all_errors.append(EC.CS_ADMISSION_DECISION_UNSIGNED)
            all_details.append("AdmissionDecision signed_by_human must be True")
            admission_signed = False
        if ad_dict.get("signed_by_model") is True:
            all_errors.append(EC.CS_MODEL_SELF_SIGNED_ROLE)
            all_details.append("AdmissionDecision signed_by_model must be False (model cannot sign G-CASE-ROLE)")
            all_roles_signed = False

        # 4. Verify each CaseRole
        for i, role in enumerate(case_roles):
            role_result = verify_case_role(role)
            if not role_result.passed:
                all_errors.extend(role_result.error_codes)
                all_details.extend(role_result.details)
                if EC.CS_ROLE_WITHOUT_EVIDENCE in role_result.error_codes:
                    roles_have_evidence = False
                if EC.CS_MODEL_SELF_SIGNED_ROLE in role_result.error_codes:
                    all_roles_signed = False
                hashes_match = False

        # 5. Check all CS_CASE_ROLES are covered by case_roles
        covered_roles = set()
        for role in case_roles:
            if isinstance(role, CaseRole):
                covered_roles.add(role.role)
            else:
                covered_roles.add(role.get("role", ""))
        for required_role in CS_CASE_ROLES:
            if required_role not in covered_roles:
                all_errors.append(EC.CS_ROLE_NOT_FROZEN)
                all_details.append(f"role {required_role!r} not covered by case_roles")
                all_roles_signed = False

        # 6. Check process-only exclusion from result layer
        if ad_dict.get("admitted_for_process_only") is True:
            if result_layer_claim is not None:
                case_pack_ref = ad_dict.get("case_pack_ref_and_hash", {}).get("ref_id", "")
                decision_id = ad_dict.get("decision_id", "")
                claim_str = str(result_layer_claim)
                if (case_pack_ref and case_pack_ref in claim_str) or \
                   (decision_id and decision_id in claim_str):
                    all_errors.append(EC.CS_PROCESS_ONLY_IN_RESULT_LAYER)
                    all_details.append(
                        "admitted_for_process_only found in result-layer confirmatory claim"
                    )
                    process_only_excluded = False

        # 7. Check evidence refs validity
        for role in case_roles:
            if isinstance(role, CaseRole):
                role_dict = role.to_dict()
            else:
                role_dict = role
            ev_refs = role_dict.get("evidence_refs", [])
            if not isinstance(ev_refs, list) or len(ev_refs) == 0:
                evidence_valid = False
                if EC.CS_ROLE_WITHOUT_EVIDENCE not in all_errors:
                    all_errors.append(EC.CS_ROLE_WITHOUT_EVIDENCE)
                    all_details.append(f"role {role_dict.get('role', '')!r} has no evidence refs")

        # Determine P3C state
        if all_errors:
            p3c_state = "BLOCKED"
        else:
            p3c_state = "VERIFIED"

        # Build report
        case_pack_ref = {}
        if isinstance(case_pack, CasePack):
            case_pack_ref = {"ref_id": case_pack.pack_id, "sha256": case_pack.content_hash}
        else:
            case_pack_ref = case_pack.get("case_pack_ref_and_hash", {})
            if not case_pack_ref:
                case_pack_ref = {
                    "ref_id": case_pack.get("pack_id", ""),
                    "sha256": case_pack.get("content_hash", ""),
                }

        report_obj = {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "object_type": _OBJECT_TYPE,
            "report_id": report_id,
            "case_pack_ref_and_hash": dict(case_pack_ref),
            "p3c_state": p3c_state,
            "all_roles_signed_by_human": all_roles_signed,
            "process_only_excluded": process_only_excluded,
            "evidence_refs_valid": evidence_valid,
            "hashes_match": hashes_match,
            "admission_signed": admission_signed,
            "roles_have_evidence": roles_have_evidence,
            "error_codes": [ec.value for ec in all_errors],
            "details": list(all_details),
            "report_hash_algorithm": _HASH_ALGORITHM,
            "report_hash": None,
        }
        report_hash = _compute_report_hash(report_obj)

        return P3CVerificationReport(
            report_id=report_id,
            case_pack_ref_and_hash=dict(case_pack_ref),
            p3c_state=p3c_state,
            all_roles_signed_by_human=all_roles_signed,
            process_only_excluded=process_only_excluded,
            evidence_refs_valid=evidence_valid,
            hashes_match=hashes_match,
            admission_signed=admission_signed,
            roles_have_evidence=roles_have_evidence,
            error_codes=[ec.value for ec in all_errors],
            details=list(all_details),
            report_hash=report_hash,
        )

    def verify_report(
        self,
        report: dict[str, Any] | P3CVerificationReport,
    ) -> VerificationResult:
        """验证 P3CVerificationReport 的结构合法性。

        检查：
        1. schema 常量
        2. report_id 非空
        3. p3c_state 在 CS_P3C_STATES 中
        4. report_hash 正确
        """
        if isinstance(report, P3CVerificationReport):
            report = report.to_dict()

        errors: list[EC] = []
        details: list[str] = []

        if report.get("schema_id") != _SCHEMA_ID:
            errors.append(EC.SCHEMA_ID_MISMATCH)
            details.append(f"schema_id must be {_SCHEMA_ID}")
        if report.get("schema_version") != _SCHEMA_VERSION:
            errors.append(EC.SCHEMA_ID_MISMATCH)
            details.append(f"schema_version must be {_SCHEMA_VERSION}")
        if report.get("object_type") != _OBJECT_TYPE:
            errors.append(EC.SCHEMA_ID_MISMATCH)
            details.append(f"object_type must be {_OBJECT_TYPE}")

        if not report.get("report_id"):
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("report_id must not be empty")

        p3c_state = report.get("p3c_state", "")
        if p3c_state not in CS_P3C_STATES:
            errors.append(EC.CS_P3C_STATE_INVALID)
            details.append(f"p3c_state {p3c_state!r} not in CS_P3C_STATES {sorted(CS_P3C_STATES)}")

        if report.get("report_hash_algorithm") != _HASH_ALGORITHM:
            errors.append(EC.OBJECT_HASH_MISMATCH)
            details.append(f"unexpected report_hash_algorithm: {report.get('report_hash_algorithm')}")

        computed = _compute_report_hash(report)
        if report.get("report_hash") != computed:
            errors.append(EC.CS_CAPABILITY_HASH_MISMATCH)
            details.append(
                f"report_hash mismatch: expected {computed}, got {report.get('report_hash')}"
            )

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_natural_case_not_forged_draft(
    natural_evidence: dict[str, Any],
) -> VerificationResult:
    """检查自然题没有伪造 draft。

    blocker: natural case forged draft → BLOCK
    """
    if natural_evidence.get("draft_is_forged") is True:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.CS_NATURAL_CASE_FORGED_DRAFT],
            details=["natural case has forged QuestionDraftVersion (draft_is_forged=True)"],
        )
    return VerificationResult(verdict="PASS")


def check_model_not_self_signing_role(
    admission_decision: dict[str, Any] | AdmissionDecision,
) -> VerificationResult:
    """检查模型没有自签角色。

    blocker: model self-signing role → BLOCK
    """
    if isinstance(admission_decision, AdmissionDecision):
        admission_decision = admission_decision.to_dict()

    if admission_decision.get("signed_by_model") is True:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.CS_MODEL_SELF_SIGNED_ROLE],
            details=["model signed G-CASE-ROLE (signed_by_model=True) → BLOCK"],
        )
    if admission_decision.get("signed_by_human") is not True:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.CS_ADMISSION_DECISION_UNSIGNED],
            details=["AdmissionDecision not signed by human (signed_by_human=False)"],
        )
    return VerificationResult(verdict="PASS")


def check_process_only_excluded_from_result(
    admission_decision: dict[str, Any] | AdmissionDecision,
    result_layer_claim: dict[str, Any] | None = None,
) -> VerificationResult:
    """检查 process-only 不进入 result layer。

    blocker: process-only entering result layer → BLOCK
    """
    from .admission_decision import check_process_only_not_in_result_layer
    return check_process_only_not_in_result_layer(
        admission_decision, result_layer_claim=result_layer_claim
    )
