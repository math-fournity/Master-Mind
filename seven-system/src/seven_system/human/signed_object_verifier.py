"""SignedObjectVerifier — P0-B 深度补全：统一签名验证核心接入所有签名对象。

文档 4.2 节"必须实现"第 9 条：
> 相同的真实验签核心还必须被以下签名对象复用或等价覆盖：
> - AuditAssignment
> - AuditRecord
> - ExternalExecutionAuthorization (EEA)
> - LiveRunPermit
> - AuthorizationConsumptionReceipt
> - NormativeRequirementReviewRecord

本模块定义所有签名对象的 domain separator 和统一验证入口，
确保所有签名对象都通过 SignatureVerifierPort 验证。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .signature_verifier import (
    SignatureVerificationReceipt,
    verify_signature,
)


# ─── Domain Separators ─────────────────────────────────────────────────

# 每个签名对象有唯一的 domain separator（含 NUL byte）
SIGNED_OBJECT_DOMAINS: dict[str, str] = {
    "seven/human-gate-decision": "seven-human-gate-decision/v1\0",
    "seven/audit-assignment": "seven-audit-assignment/v1\0",
    "seven/audit-record": "seven-audit-record/v1\0",
    "seven/external-execution-authorization": "seven-eea/v1\0",
    "seven/live-run-permit": "seven-live-run-permit/v1\0",
    "seven/authorization-consumption-receipt": "seven-auth-consumption-receipt/v1\0",
    "seven/normative-requirement-review-record": "seven-normative-review/v1\0",
}


@dataclass(frozen=True)
class SignedObjectVerificationResult:
    """签名对象验证结果。"""

    verdict: str  # "PASS" or "FAIL"
    object_type: str
    receipt: SignatureVerificationReceipt
    error_codes: list[str]
    details: list[str]


def verify_signed_object(
    signed_object: dict[str, Any],
    *,
    public_key_bytes: bytes,
    expected_schema_id: str | None = None,
) -> SignedObjectVerificationResult:
    """验证任意签名对象的 Ed25519 签名。

    P0-B 深度补全：统一签名验证入口。
    所有签名对象（GateDecision、AuditAssignment、AuditRecord、EEA、
    LiveRunPermit、AuthorizationConsumptionReceipt、NormativeRequirementReviewRecord）
    都通过此函数验证签名。

    参数：
    - signed_object: 包含 schema_id 和 signature_envelope 的签名对象
    - public_key_bytes: Ed25519 公钥 raw bytes (32 bytes)
    - expected_schema_id: 期望的 schema_id（如提供则验证匹配）

    返回 SignedObjectVerificationResult。
    """
    errors: list[str] = []
    details: list[str] = []

    # 确定 schema_id 和 domain
    schema_id = signed_object.get("schema_id", "")
    if expected_schema_id is not None and schema_id != expected_schema_id:
        errors.append("SCHEMA_ID_MISMATCH")
        details.append(f"expected {expected_schema_id}, got {schema_id}")

    domain_str = SIGNED_OBJECT_DOMAINS.get(schema_id, "")
    if not domain_str:
        errors.append("UNKNOWN_SIGNED_OBJECT_TYPE")
        details.append(f"unknown schema_id: {schema_id}")

    # 如果有结构错误，返回 FAIL 但不执行验签
    if errors:
        return SignedObjectVerificationResult(
            verdict="FAIL",
            object_type=schema_id,
            receipt=SignatureVerificationReceipt(
                verified=False,
                algorithm="Ed25519",
                key_id=str(signed_object.get("key_id", "")),
                signer_principal_id="",
                signed_bytes_hash="",
                verification_error="structure check failed before signature verification",
            ),
            error_codes=errors,
            details=details,
        )

    # 执行真实 Ed25519 验签
    receipt = verify_signature(
        signed_object=signed_object,
        public_key_bytes=public_key_bytes,
        signature_domain=domain_str.encode("utf-8"),
    )

    if not receipt.verified:
        errors.append("SIGNATURE_INVALID")
        details.append(receipt.verification_error or "signature verification failed")

    verdict = "PASS" if not errors else "FAIL"
    return SignedObjectVerificationResult(
        verdict=verdict,
        object_type=schema_id,
        receipt=receipt,
        error_codes=errors,
        details=details,
    )


def verify_audit_assignment(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    """验证 AuditAssignment 签名。"""
    return verify_signed_object(
        obj, public_key_bytes=public_key_bytes,
        expected_schema_id="seven/audit-assignment",
    )


def verify_audit_record(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    """验证 AuditRecord 签名。"""
    return verify_signed_object(
        obj, public_key_bytes=public_key_bytes,
        expected_schema_id="seven/audit-record",
    )


def verify_eea(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    """验证 ExternalExecutionAuthorization (EEA) 签名。"""
    return verify_signed_object(
        obj, public_key_bytes=public_key_bytes,
        expected_schema_id="seven/external-execution-authorization",
    )


def verify_live_run_permit(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    """验证 LiveRunPermit 签名。"""
    return verify_signed_object(
        obj, public_key_bytes=public_key_bytes,
        expected_schema_id="seven/live-run-permit",
    )


def verify_authorization_consumption_receipt(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    """验证 AuthorizationConsumptionReceipt 签名。"""
    return verify_signed_object(
        obj, public_key_bytes=public_key_bytes,
        expected_schema_id="seven/authorization-consumption-receipt",
    )


def verify_normative_requirement_review_record(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    """验证 NormativeRequirementReviewRecord 签名。"""
    return verify_signed_object(
        obj, public_key_bytes=public_key_bytes,
        expected_schema_id="seven/normative-requirement-review-record",
    )
