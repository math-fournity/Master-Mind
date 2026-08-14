"""GateDecision — 签名后的门控决定对象。

每个 GateDecision 至少包含：
- decision_id / task_id / gate_type
- payload_ref + payload_hash（签完整 payload hash，不签摘要）
- actor_id + actor_role
- decision: APPROVE / REJECT / REQUEST_CHANGES / QUARANTINE
- reason_codes
- nonce（唯一、不可预测）
- issued_at / expires_at
- key_id / signature algorithm
- signature_domain（含实际 NUL byte）
- signed_bytes_hash
- signature_envelope
- separation_evidence_refs
- verification_status
- decision_hash

v1 签名输入固定为：
    UTF8("seven-human-gate-decision/v1\0") || canonical_json(unsigned_decision_envelope)

unsigned_decision_envelope 是完整 Decision 对象移除 signature、verification_status
和自引用 decision_hash 后的对象。

验证器做结构检查（与 SecurityContractVerifier 的 verify_signature_envelope 一致），
真实 Ed25519 验签由 HumanGateService 的外部 signer 执行。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    GATE_DECISIONS,
    GATE_VERIFICATION_STATUSES,
    HUMAN_GATE_HASH_ALGORITHM,
    HUMAN_GATE_SIGNATURE_DOMAIN,
    HUMAN_GATE_ROLES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from ..contracts.security_contract import _check_canonical_utc, verify_signature_envelope


_SCHEMA_ID = "seven/human-gate-decision"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "HumanGateDecision"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_ID_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9._:@+-]{0,254}[A-Za-z0-9])?$")
_NONCE_RE = re.compile(r"^[A-Za-z0-9._:-]{16,128}$")
_SIG_B64_RE = re.compile(r"^[A-Za-z0-9+/]{86}==$")


@dataclass(frozen=True)
class GateDecision:
    """GateDecision 数据对象。不可变。"""

    decision_id: str
    task_id: str
    gate_type: str
    payload_ref: str
    payload_hash: str
    actor_id: str
    actor_role: str
    decision: str
    reason_codes: list[str]
    nonce: str
    issued_at: str
    expires_at: str
    key_id: str
    signature_algorithm: str
    signature_domain: str
    signed_bytes_hash: str
    signature_envelope: dict[str, Any]
    separation_evidence_refs: list[str]
    verification_status: str
    decision_hash_algorithm: str
    decision_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "object_type": _OBJECT_TYPE,
            "decision_id": self.decision_id,
            "task_id": self.task_id,
            "gate_type": self.gate_type,
            "payload_ref": self.payload_ref,
            "payload_hash": self.payload_hash,
            "actor_id": self.actor_id,
            "actor_role": self.actor_role,
            "decision": self.decision,
            "reason_codes": list(self.reason_codes),
            "nonce": self.nonce,
            "issued_at": self.issued_at,
            "expires_at": self.expires_at,
            "key_id": self.key_id,
            "signature_algorithm": self.signature_algorithm,
            "signature_domain": self.signature_domain,
            "signed_bytes_hash": self.signed_bytes_hash,
            "signature_envelope": dict(self.signature_envelope),
            "separation_evidence_refs": list(self.separation_evidence_refs),
            "verification_status": self.verification_status,
            "decision_hash_algorithm": self.decision_hash_algorithm,
            "decision_hash": self.decision_hash,
        }


def _compute_signed_bytes_hash(decision: dict[str, Any]) -> str:
    """计算 signed_bytes_hash。

    signed_bytes = UTF8(domain) || canonical_json(unsigned_envelope)
    unsigned_envelope = decision 移除 signature_envelope.signature_b64、
    envelope 及顶层 signed_bytes_hash、decision_hash、verification_status 后的对象。
    signed_bytes_hash 不进入它自身的签名输入（顶层和 envelope 内都置 null）。
    """
    unsigned = dict(decision)
    # 移除自引用和签名结果字段
    envelope = dict(unsigned.get("signature_envelope", {}))
    envelope["signature_b64"] = None
    envelope["signed_bytes_hash"] = None
    unsigned["signature_envelope"] = envelope
    unsigned["signed_bytes_hash"] = None
    unsigned["decision_hash"] = None
    unsigned["verification_status"] = None

    domain_bytes = HUMAN_GATE_SIGNATURE_DOMAIN.encode("utf-8")
    payload_bytes = canonical_json_bytes(unsigned)
    return hashlib.sha256(domain_bytes + payload_bytes).hexdigest()


def _compute_decision_hash(decision: dict[str, Any]) -> str:
    """计算 decision_hash = sha256(canonical_json(decision with decision_hash=null))。"""
    obj = dict(decision)
    obj["decision_hash"] = None
    return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()


def verify_gate_decision(
    decision: dict[str, Any],
    *,
    expected_payload_hash: str | None = None,
    public_key_bytes: bytes | None = None,
) -> VerificationResult:
    """验证 GateDecision 的结构合法性。

    检查（结构层，与 SecurityContractVerifier 一致）：
    1. schema_id / schema_version / object_type 常量
    2. decision_id / task_id / gate_type 非空合法 ID
    3. payload_ref 非空、payload_hash 是合法 sha256
    4. actor_id 非空、actor_role 是合法角色
    5. decision 在合法枚举中
    6. nonce 格式合法
    7. issued_at / expires_at 为 canonical UTC 且 issued_at < expires_at
    8. key_id 非空合法 ID
    9. signature_algorithm == Ed25519
    10. signature_domain == "seven-human-gate-decision/v1\\0"
    11. signed_bytes_hash 正确（重算）
    12. signature_envelope 结构合法（algorithm/hash/b64 格式）
    13. verification_status 在合法枚举中
    14. decision_hash 正确（重算）
    15. expected_payload_hash 匹配（如提供）
    16. P0-B: 真实 Ed25519 验签（如提供 public_key_bytes）

    P0-B 整改：如果提供 public_key_bytes，执行真实 Ed25519 验签。
    如果不提供 public_key_bytes，只做结构检查（向后兼容旧调用方，
    但 HumanGateService 必须提供 public_key_bytes）。
    """
    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. schema 常量
    if decision.get("schema_id") != _SCHEMA_ID:
        _err(EC.SCHEMA_ID_MISMATCH, f"schema_id must be {_SCHEMA_ID}")
    if decision.get("schema_version") != _SCHEMA_VERSION:
        _err(EC.SCHEMA_ID_MISMATCH, f"schema_version must be {_SCHEMA_VERSION}")
    if decision.get("object_type") != _OBJECT_TYPE:
        _err(EC.SCHEMA_ID_MISMATCH, f"object_type must be {_OBJECT_TYPE}")

    # 2. IDs
    for field_name in ("decision_id", "task_id", "gate_type", "key_id", "actor_id"):
        val = decision.get(field_name, "")
        if not val or not _ID_RE.match(str(val)):
            _err(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not a valid id: {val!r}")

    # 3. payload
    payload_ref = decision.get("payload_ref", "")
    if not payload_ref:
        _err(EC.REQUIRED_FIELD_MISSING, "payload_ref must not be empty")
    payload_hash = decision.get("payload_hash", "")
    if not isinstance(payload_hash, str) or not _HASH_RE.match(payload_hash):
        _err(EC.GATE_PAYLOAD_HASH_MISMATCH, f"payload_hash is not valid sha256: {payload_hash!r}")

    # 4. actor_role
    actor_role = decision.get("actor_role", "")
    if actor_role not in HUMAN_GATE_ROLES:
        _err(EC.ACTOR_ROLE_MISSING, f"unknown actor_role: {actor_role}")

    # 5. decision
    dec_value = decision.get("decision", "")
    if dec_value not in GATE_DECISIONS:
        _err(EC.STATE_COMMAND_REJECTED, f"unknown decision: {dec_value}")

    # 6. nonce
    nonce = decision.get("nonce", "")
    if not isinstance(nonce, str) or not _NONCE_RE.match(nonce):
        _err(EC.GATE_NONCE_INVALID, f"nonce is not valid: {nonce!r}")

    # 7. timestamps
    issued_at = decision.get("issued_at", "")
    expires_at = decision.get("expires_at", "")
    if not _check_canonical_utc(issued_at):
        _err(EC.TIME_NOT_CANONICAL_UTC, f"issued_at not canonical UTC: {issued_at!r}")
    if not _check_canonical_utc(expires_at):
        _err(EC.TIME_NOT_CANONICAL_UTC, f"expires_at not canonical UTC: {expires_at!r}")
    if _check_canonical_utc(issued_at) and _check_canonical_utc(expires_at):
        if issued_at >= expires_at:
            _err(EC.TIME_WINDOW_INVALID, f"issued_at {issued_at} >= expires_at {expires_at}")

    # 8. signature_algorithm
    if decision.get("signature_algorithm") != "Ed25519":
        _err(EC.SIGNATURE_ALGORITHM_INVALID, "signature_algorithm must be Ed25519")

    # 9. signature_domain
    sig_domain = decision.get("signature_domain", "")
    if sig_domain != HUMAN_GATE_SIGNATURE_DOMAIN:
        _err(
            EC.SIGNATURE_DOMAIN_INVALID,
            f"signature_domain mismatch: expected {HUMAN_GATE_SIGNATURE_DOMAIN!r}, "
            f"got {sig_domain!r}",
        )

    # 10. signed_bytes_hash 重算
    computed_signed_hash = _compute_signed_bytes_hash(decision)
    if decision.get("signed_bytes_hash") != computed_signed_hash:
        _err(
            EC.GATE_DECISION_HASH_MISMATCH,
            f"signed_bytes_hash mismatch: expected {computed_signed_hash}, "
            f"got {decision.get('signed_bytes_hash')}",
        )

    # 11. signature_envelope 结构检查
    envelope = decision.get("signature_envelope", {})
    if not isinstance(envelope, dict):
        _err(EC.SIGNATURE_INVALID, "signature_envelope is not an object")
    else:
        env_algo = envelope.get("algorithm", "")
        if env_algo != "Ed25519":
            _err(EC.SIGNATURE_ALGORITHM_INVALID, f"envelope algorithm must be Ed25519, got {env_algo}")
        env_key_id = envelope.get("key_id", "")
        if not env_key_id or not _ID_RE.match(str(env_key_id)):
            _err(EC.REQUIRED_FIELD_MISSING, f"envelope key_id invalid: {env_key_id!r}")
        env_signer = envelope.get("signer_principal_id", "")
        if not env_signer or not _ID_RE.match(str(env_signer)):
            _err(EC.REQUIRED_FIELD_MISSING, f"envelope signer_principal_id invalid: {env_signer!r}")
        if envelope.get("signature_encoding") != "base64":
            _err(EC.SIGNATURE_INVALID, "signature_encoding must be base64")
        sig_b64 = envelope.get("signature_b64", "")
        if not isinstance(sig_b64, str) or not _SIG_B64_RE.match(sig_b64):
            _err(EC.SIGNATURE_INVALID, "signature_b64 is not valid Ed25519 base64 (86 chars + ==)")
        # envelope signed_bytes_hash 必须与顶层一致
        env_signed_hash = envelope.get("signed_bytes_hash", "")
        if env_signed_hash != computed_signed_hash:
            _err(
                EC.SIGNATURE_INVALID,
                f"envelope signed_bytes_hash mismatch: expected {computed_signed_hash}, "
                f"got {env_signed_hash}",
            )

    # 12. verification_status
    vstatus = decision.get("verification_status", "")
    if vstatus not in GATE_VERIFICATION_STATUSES:
        _err(EC.STATE_COMMAND_REJECTED, f"unknown verification_status: {vstatus}")

    # P0-B 补全: HUMAN_PENDING + APPROVE 必须拒绝
    # verification_status 不是 VERIFIED 时，不能产生 APPROVE 效果
    if dec_value == "APPROVE" and vstatus != "VERIFIED":
        _err(
            EC.GATE_VERIFICATION_STATUS_INVALID,
            f"APPROVE decision requires verification_status=VERIFIED, got {vstatus}",
        )

    # 13. decision_hash_algorithm
    hash_algo = decision.get("decision_hash_algorithm", "")
    if hash_algo != HUMAN_GATE_HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH, f"unexpected decision_hash_algorithm: {hash_algo}")

    # 14. decision_hash 重算
    computed_decision_hash = _compute_decision_hash(decision)
    if decision.get("decision_hash") != computed_decision_hash:
        _err(
            EC.GATE_DECISION_HASH_MISMATCH,
            f"decision_hash mismatch: expected {computed_decision_hash}, "
            f"got {decision.get('decision_hash')}",
        )

    # 15. expected_payload_hash
    if expected_payload_hash is not None:
        if payload_hash != expected_payload_hash:
            _err(
                EC.GATE_PAYLOAD_HASH_MISMATCH,
                f"payload_hash mismatch: expected {expected_payload_hash}, got {payload_hash}",
            )

    # 16. P0-B: 真实 Ed25519 验签（如提供 public_key_bytes）
    if public_key_bytes is not None and not errors:
        _verify_ed25519_signature(decision, public_key_bytes, errors, details)

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def _verify_ed25519_signature(
    decision: dict[str, Any],
    public_key_bytes: bytes,
    errors: list[EC],
    details: list[str],
) -> None:
    """执行真实 Ed25519 验签。

    P0-B 补全：使用 SignatureVerifierPort 唯一接口执行验签。
    不再直接调用 cryptography 库——所有验签通过 SignatureVerifierPort。
    """
    from .signature_verifier import verify_signature

    receipt = verify_signature(
        signed_object=decision,
        public_key_bytes=public_key_bytes,
        signature_domain=HUMAN_GATE_SIGNATURE_DOMAIN.encode("utf-8"),
    )
    if not receipt.verified:
        errors.append(EC.SIGNATURE_INVALID)
        details.append(receipt.verification_error or "signature verification failed")


def _get_signed_bytes_for_verification(decision: dict[str, Any]) -> bytes:
    """获取用于验签的 signed bytes（与 _compute_signed_bytes_hash 一致）。"""
    unsigned = dict(decision)
    envelope = dict(unsigned.get("signature_envelope", {}))
    envelope["signature_b64"] = None
    envelope["signed_bytes_hash"] = None
    unsigned["signature_envelope"] = envelope
    unsigned["signed_bytes_hash"] = None
    unsigned["decision_hash"] = None
    unsigned["verification_status"] = None

    domain_bytes = HUMAN_GATE_SIGNATURE_DOMAIN.encode("utf-8")
    payload_bytes = canonical_json_bytes(unsigned)
    return domain_bytes + payload_bytes


def build_gate_decision_dict(
    *,
    decision_id: str,
    task_id: str,
    gate_type: str,
    payload_ref: str,
    payload_hash: str,
    actor_id: str,
    actor_role: str,
    decision: str,
    reason_codes: list[str],
    nonce: str,
    issued_at: str,
    expires_at: str,
    key_id: str,
    signer_principal_id: str,
    signature_b64: str,
    separation_evidence_refs: list[str] | None = None,
    verification_status: str = "HUMAN_PENDING",
) -> dict[str, Any]:
    """构建一个完整的 GateDecision dict，自动计算 signed_bytes_hash 和 decision_hash。

    辅助函数：调用方提供签名结果（signature_b64），本函数计算所有 hash。
    """
    envelope = {
        "algorithm": "Ed25519",
        "key_id": key_id,
        "signer_principal_id": signer_principal_id,
        "signature_encoding": "base64",
        "signature_b64": signature_b64,
        "signed_bytes_hash": None,  # 占位，后面填
    }

    dec: dict[str, Any] = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "decision_id": decision_id,
        "task_id": task_id,
        "gate_type": gate_type,
        "payload_ref": payload_ref,
        "payload_hash": payload_hash,
        "actor_id": actor_id,
        "actor_role": actor_role,
        "decision": decision,
        "reason_codes": list(reason_codes),
        "nonce": nonce,
        "issued_at": issued_at,
        "expires_at": expires_at,
        "key_id": key_id,
        "signature_algorithm": "Ed25519",
        "signature_domain": HUMAN_GATE_SIGNATURE_DOMAIN,
        "signed_bytes_hash": None,
        "signature_envelope": envelope,
        "separation_evidence_refs": list(separation_evidence_refs or []),
        "verification_status": verification_status,
        "decision_hash_algorithm": HUMAN_GATE_HASH_ALGORITHM,
        "decision_hash": None,
    }

    # 计算 signed_bytes_hash
    signed_hash = _compute_signed_bytes_hash(dec)
    dec["signed_bytes_hash"] = signed_hash
    dec["signature_envelope"]["signed_bytes_hash"] = signed_hash

    # 计算 decision_hash
    dec["decision_hash"] = _compute_decision_hash(dec)

    return dec
