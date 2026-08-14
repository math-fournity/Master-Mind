"""SignatureVerifierPort — P0-B 补全：唯一签名验证接口。

文档 4.2 节"必须实现"第 1 条：
> 定义 SignatureVerifierPort 或等价唯一接口，禁止各模块自行写"Base64看起来像签名"的判断。

本模块定义唯一的 Ed25519 签名验证接口，所有签名对象（GateDecision、
AuditAssignment、AuditRecord、EEA、LiveRunPermit、AuthorizationConsumptionReceipt、
NormativeRequirementReviewRecord）必须通过此接口验证签名。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import base64 as _b64
import hashlib
from dataclasses import dataclass
from typing import Any, Protocol

from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult
from ..hashing import canonical_json_bytes


# 签名验证结果
@dataclass(frozen=True)
class SignatureVerificationReceipt:
    """签名验证收据——由 verifier 生成，不能由调用者传入。"""

    verified: bool
    algorithm: str  # "Ed25519"
    key_id: str
    signer_principal_id: str
    signed_bytes_hash: str
    verification_error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "verified": self.verified,
            "algorithm": self.algorithm,
            "key_id": self.key_id,
            "signer_principal_id": self.signer_principal_id,
            "signed_bytes_hash": self.signed_bytes_hash,
            "verification_error": self.verification_error,
        }


class SignatureVerifierPort(Protocol):
    """唯一签名验证接口——所有签名对象必须通过此接口验证。"""

    def verify(
        self,
        *,
        signed_object: dict[str, Any],
        public_key_bytes: bytes,
        signature_domain: bytes,
        signature_field_path: str = "signature_envelope.signature_b64",
    ) -> SignatureVerificationReceipt:
        """验证签名对象的 Ed25519 签名。

        参数：
        - signed_object: 包含签名的完整对象
        - public_key_bytes: Ed25519 公钥 raw bytes (32 bytes)
        - signature_domain: domain separator bytes (含 NUL byte)
        - signature_field_path: 签名在对象中的路径

        返回 SignatureVerificationReceipt——verified=True 表示验签通过。
        """
        ...


class Ed25519SignatureVerifier:
    """Ed25519SignatureVerifier — 真实 Ed25519 验签实现。

    使用 cryptography 库执行真实 Ed25519 验签。
    伪签名（全A、全0、随机）全部 FAIL。

    这是唯一的签名验证实现——所有签名对象都通过此 verifier 验证。
    """

    def verify(
        self,
        *,
        signed_object: dict[str, Any],
        public_key_bytes: bytes,
        signature_domain: bytes,
        signature_field_path: str = "signature_envelope.signature_b64",
    ) -> SignatureVerificationReceipt:
        """执行真实 Ed25519 验签。"""
        try:
            from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
            from cryptography.exceptions import InvalidSignature
        except ImportError:
            return SignatureVerificationReceipt(
                verified=False,
                algorithm="Ed25519",
                key_id="",
                signer_principal_id="",
                signed_bytes_hash="",
                verification_error="cryptography library not available — fail-closed",
            )

        # 提取签名
        sig_b64 = _extract_field(signed_object, signature_field_path)
        if not isinstance(sig_b64, str):
            return SignatureVerificationReceipt(
                verified=False,
                algorithm="Ed25519",
                key_id=str(signed_object.get("key_id", "")),
                signer_principal_id="",
                signed_bytes_hash="",
                verification_error="signature field not found or not a string",
            )

        try:
            signature = _b64.b64decode(sig_b64)
        except Exception:
            return SignatureVerificationReceipt(
                verified=False,
                algorithm="Ed25519",
                key_id=str(signed_object.get("key_id", "")),
                signer_principal_id="",
                signed_bytes_hash="",
                verification_error="signature_b64 decode failed",
            )

        # 计算 signed bytes
        signed_bytes = _compute_signed_bytes(signed_object, signature_domain)
        signed_bytes_hash = hashlib.sha256(signed_bytes).hexdigest()

        # 提取 key_id 和 signer
        key_id = str(signed_object.get("key_id", ""))
        envelope = signed_object.get("signature_envelope", {})
        signer = str(envelope.get("signer_principal_id", "")) if isinstance(envelope, dict) else ""

        # 执行真实验签
        try:
            public_key = Ed25519PublicKey.from_public_bytes(public_key_bytes)
            public_key.verify(signature, signed_bytes)
            return SignatureVerificationReceipt(
                verified=True,
                algorithm="Ed25519",
                key_id=key_id,
                signer_principal_id=signer,
                signed_bytes_hash=signed_bytes_hash,
            )
        except InvalidSignature:
            return SignatureVerificationReceipt(
                verified=False,
                algorithm="Ed25519",
                key_id=key_id,
                signer_principal_id=signer,
                signed_bytes_hash=signed_bytes_hash,
                verification_error="Ed25519 signature verification failed — fake or forged signature",
            )
        except Exception as exc:
            return SignatureVerificationReceipt(
                verified=False,
                algorithm="Ed25519",
                key_id=key_id,
                signer_principal_id=signer,
                signed_bytes_hash=signed_bytes_hash,
                verification_error=f"Ed25519 verification error: {exc}",
            )


def _extract_field(obj: dict[str, Any], path: str) -> Any:
    """从嵌套 dict 中按路径提取字段。"""
    parts = path.split(".")
    current: Any = obj
    for part in parts:
        if isinstance(current, dict):
            current = current.get(part)
        else:
            return None
    return current


def _compute_signed_bytes(signed_object: dict[str, Any], signature_domain: bytes) -> bytes:
    """计算 signed bytes = domain || canonical_json(unsigned_object)。

    unsigned_object = signed_object 移除 signature_envelope.signature_b64、
    signature_envelope.signed_bytes_hash、顶层 signed_bytes_hash、
    顶层 decision_hash（或对应自引用 hash）、顶层 verification_status。

    注意：字段设为 None（不是 pop），与 gate_decision._compute_signed_bytes_hash 一致，
    确保 canonical_json 中字段顺序和值完全一致。
    """
    unsigned = dict(signed_object)
    envelope = dict(unsigned.get("signature_envelope", {}))
    envelope["signature_b64"] = None
    envelope["signed_bytes_hash"] = None
    unsigned["signature_envelope"] = envelope
    # 设为 None（与 gate_decision 一致，不是 pop）
    unsigned["signed_bytes_hash"] = None
    unsigned["decision_hash"] = None
    unsigned["verification_status"] = None

    payload_bytes = canonical_json_bytes(unsigned)
    return signature_domain + payload_bytes


# 全局单例——所有模块共享同一个 verifier 实例
_default_verifier: Ed25519SignatureVerifier | None = None


def get_signature_verifier() -> Ed25519SignatureVerifier:
    """获取全局唯一的签名验证器实例。"""
    global _default_verifier
    if _default_verifier is None:
        _default_verifier = Ed25519SignatureVerifier()
    return _default_verifier


def verify_signature(
    *,
    signed_object: dict[str, Any],
    public_key_bytes: bytes,
    signature_domain: bytes,
    signature_field_path: str = "signature_envelope.signature_b64",
) -> SignatureVerificationReceipt:
    """便捷函数——通过全局唯一 verifier 验证签名。"""
    return get_signature_verifier().verify(
        signed_object=signed_object,
        public_key_bytes=public_key_bytes,
        signature_domain=signature_domain,
        signature_field_path=signature_field_path,
    )
