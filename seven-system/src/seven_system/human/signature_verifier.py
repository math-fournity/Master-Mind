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
import copy
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
        envelope_hash_field_path: str = "signature_envelope.signed_bytes_hash",
        top_hash_field: str | None = "signed_bytes_hash",
        self_hash_field: str | None = None,
        signer_field_path: str = "signature_envelope.signer_principal_id",
        key_id_field_path: str = "signature_envelope.key_id",
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
        envelope_hash_field_path: str = "signature_envelope.signed_bytes_hash",
        top_hash_field: str | None = "signed_bytes_hash",
        self_hash_field: str | None = None,
        signer_field_path: str = "signature_envelope.signer_principal_id",
        key_id_field_path: str = "signature_envelope.key_id",
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
        try:
            signed_bytes = compute_signed_bytes(
                signed_object,
                signature_domain,
                signature_field_path=signature_field_path,
                envelope_hash_field_path=envelope_hash_field_path,
                top_hash_field=top_hash_field,
                self_hash_field=self_hash_field,
            )
        except (KeyError, TypeError, ValueError) as exc:
            return SignatureVerificationReceipt(
                verified=False,
                algorithm="Ed25519",
                key_id="",
                signer_principal_id="",
                signed_bytes_hash="",
                verification_error=f"signed object profile mismatch: {exc}",
            )
        signed_bytes_hash = hashlib.sha256(signed_bytes).hexdigest()

        # 提取 key_id 和 signer
        key_id = str(_extract_field(signed_object, key_id_field_path) or "")
        signer = str(_extract_field(signed_object, signer_field_path) or "")

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


def _set_path(obj: dict[str, Any], path: str, value: Any) -> None:
    """在已存在的嵌套对象路径上写值；路径缺失时 fail-closed。"""
    parts = path.split(".")
    current: Any = obj
    for part in parts[:-1]:
        if not isinstance(current, dict) or part not in current:
            raise KeyError(path)
        current = current[part]
    if not isinstance(current, dict) or parts[-1] not in current:
        raise KeyError(path)
    current[parts[-1]] = value


def compute_signed_bytes(
    signed_object: dict[str, Any],
    signature_domain: bytes,
    *,
    signature_field_path: str = "signature_envelope.signature_b64",
    envelope_hash_field_path: str = "signature_envelope.signed_bytes_hash",
    top_hash_field: str | None = "signed_bytes_hash",
    self_hash_field: str | None = None,
) -> bytes:
    """按对象 profile 重建唯一的签名字节。

    规范要求把签名、envelope hash、顶层 signed/attested hash 和对象自引用
    hash 置为 ``null``，而不是删除字段。不同安全对象使用不同字段名；调用者
    必须显式提供 profile，不能把 GateDecision 的形状套到 EEA/Receipt 上。
    """
    unsigned = copy.deepcopy(signed_object)
    _set_path(unsigned, signature_field_path, None)
    _set_path(unsigned, envelope_hash_field_path, None)
    if top_hash_field is not None:
        if top_hash_field not in unsigned:
            raise KeyError(top_hash_field)
        unsigned[top_hash_field] = None

    if self_hash_field is None:
        for candidate in ("decision_hash", "self_hash"):
            if candidate in unsigned:
                unsigned[candidate] = None
                break
    else:
        if self_hash_field not in unsigned:
            raise KeyError(self_hash_field)
        unsigned[self_hash_field] = None

    # GateDecision 的 verification_status 是验签结果，不属于签名输入；其他
    # 对象没有该字段，绝不能凭空添加一个 null 字段改变payload。
    if "verification_status" in unsigned:
        unsigned["verification_status"] = None

    return signature_domain + canonical_json_bytes(unsigned)


# 旧内部名称保留给现有调用者；语义现在使用按字段存在性自动选择的 profile。
def _compute_signed_bytes(signed_object: dict[str, Any], signature_domain: bytes) -> bytes:
    return compute_signed_bytes(signed_object, signature_domain)


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
    envelope_hash_field_path: str = "signature_envelope.signed_bytes_hash",
    top_hash_field: str | None = "signed_bytes_hash",
    self_hash_field: str | None = None,
    signer_field_path: str = "signature_envelope.signer_principal_id",
    key_id_field_path: str = "signature_envelope.key_id",
) -> SignatureVerificationReceipt:
    """便捷函数——通过全局唯一 verifier 验证签名。"""
    return get_signature_verifier().verify(
        signed_object=signed_object,
        public_key_bytes=public_key_bytes,
        signature_domain=signature_domain,
        signature_field_path=signature_field_path,
        envelope_hash_field_path=envelope_hash_field_path,
        top_hash_field=top_hash_field,
        self_hash_field=self_hash_field,
        signer_field_path=signer_field_path,
        key_id_field_path=key_id_field_path,
    )
