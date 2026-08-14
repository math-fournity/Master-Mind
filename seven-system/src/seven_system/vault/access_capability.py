"""VaultAccessCapability — issuer 签发的最小访问能力。

精确绑定 principal、单一 operation、object ID/hash、view ID/hash/policy hash、
sink ID/kind/policy hash、时窗、nonce、issuer 和 revocation handle。

硬约束：
- deny_by_default 只能为 true
- raw_vault_path_disclosure 只能为 false
- 没有 READ_RAW_OBJECT 操作
- capability_hash = sha256(canonical_json(object with capability_hash=null))

验证器做 schema + semantic 双重检查，返回 VerificationResult。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ACCESS_REASON_CODES,
    FORBIDDEN_OPERATIONS,
    SENSITIVITY_LEVELS,
    SINK_KINDS,
    VAULT_OPERATIONS,
    VAULT_PRINCIPAL_TYPES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from ..contracts.security_contract import (
    _check_canonical_utc,
    verify_signature_envelope,
)


# VaultAccessCapability v1 schema 常量
_SCHEMA_ID = "seven/vault-access-capability"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "VaultAccessCapability"
_SIGNATURE_DOMAIN = "seven-vault-access-capability/v1\0"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-capability_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_EXACT_ID_RE = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._:@+-]{0,254}[A-Za-z0-9])?$"
)
_NONCE_RE = re.compile(r"^[A-Za-z0-9._:-]{16,128}$")
_SIG_B64_RE = re.compile(r"^[A-Za-z0-9+/]{86}==$")


@dataclass(frozen=True)
class VaultAccessCapability:
    """VaultAccessCapability 数据对象。

    不可变。通过 verify_vault_access_capability 验证后使用。
    """

    capability_id: str
    principal: dict[str, Any]
    operation: str
    object_binding: dict[str, Any]
    view_binding: dict[str, Any]
    sink_binding: dict[str, Any]
    access_policy_ref_and_hash: dict[str, str]
    deny_by_default: bool
    raw_vault_path_disclosure: bool
    issued_at: str
    not_before: str
    expires_at: str
    nonce: str
    issuer: dict[str, Any]
    revocation: dict[str, Any]
    externally_pinned_trust_root: dict[str, str]
    issuer_key_registry_ref_and_hash: dict[str, str]
    canonicalizer_profile: str
    signature_domain: str
    signed_bytes_hash: str
    signature_envelope: dict[str, Any]
    capability_hash_algorithm: str
    capability_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "object_type": _OBJECT_TYPE,
            "capability_id": self.capability_id,
            "principal": dict(self.principal),
            "operation": self.operation,
            "object_binding": dict(self.object_binding),
            "view_binding": dict(self.view_binding),
            "sink_binding": dict(self.sink_binding),
            "access_policy_ref_and_hash": dict(self.access_policy_ref_and_hash),
            "deny_by_default": self.deny_by_default,
            "raw_vault_path_disclosure": self.raw_vault_path_disclosure,
            "issued_at": self.issued_at,
            "not_before": self.not_before,
            "expires_at": self.expires_at,
            "nonce": self.nonce,
            "issuer": dict(self.issuer),
            "revocation": dict(self.revocation),
            "externally_pinned_trust_root": dict(self.externally_pinned_trust_root),
            "issuer_key_registry_ref_and_hash": dict(self.issuer_key_registry_ref_and_hash),
            "canonicalizer_profile": self.canonicalizer_profile,
            "signature_domain": self.signature_domain,
            "signed_bytes_hash": self.signed_bytes_hash,
            "signature_envelope": dict(self.signature_envelope),
            "capability_hash_algorithm": self.capability_hash_algorithm,
            "capability_hash": self.capability_hash,
        }


def _check_hash(value: str, field_name: str) -> list[tuple[EC, str]]:
    if not isinstance(value, str) or not _HASH_RE.match(value):
        return [(EC.OBJECT_HASH_MISMATCH, f"{field_name} is not a valid sha256 hash: {value!r}")]
    return []


def _check_exact_id(value: str, field_name: str) -> list[tuple[EC, str]]:
    if not isinstance(value, str) or not _EXACT_ID_RE.match(value):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not a valid exact_id: {value!r}")]
    if value in ("ANY", "ALL", "DEFAULT", "any", "all", "default"):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is a reserved word: {value!r}")]
    return []


def _check_nonce(value: str) -> list[tuple[EC, str]]:
    if not isinstance(value, str) or not _NONCE_RE.match(value):
        return [(EC.VAULT_NONCE_REPLAY, f"nonce is not valid: {value!r}")]
    return []


def _check_opaque_ref_hash(obj: dict[str, Any], field_name: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not an object")]
    if set(obj.keys()) != {"ref_id", "sha256"}:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must have exactly ref_id and sha256"))
        return errors
    errors.extend(_check_exact_id(obj.get("ref_id", ""), f"{field_name}.ref_id"))
    errors.extend(_check_hash(obj.get("sha256", ""), f"{field_name}.sha256"))
    return errors


def _check_named_hash(obj: dict[str, Any], field_name: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not an object")]
    if set(obj.keys()) != {"object_id", "sha256"}:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must have exactly object_id and sha256"))
        return errors
    errors.extend(_check_exact_id(obj.get("object_id", ""), f"{field_name}.object_id"))
    errors.extend(_check_hash(obj.get("sha256", ""), f"{field_name}.sha256"))
    return errors


def _check_principal(principal: dict[str, Any]) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(principal, dict):
        return [(EC.VAULT_PRINCIPAL_MISMATCH, "principal is not an object")]
    required = {"principal_id", "principal_type", "role_type_id",
                "carrier_profile_sha256", "target_solver_contract_sha256",
                "execution_attempt_id"}
    missing = required - set(principal.keys())
    if missing:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"principal missing fields: {missing}"))
        return errors

    ptype = principal.get("principal_type", "")
    if ptype not in VAULT_PRINCIPAL_TYPES:
        errors.append((EC.VAULT_PRINCIPAL_MISMATCH, f"unknown principal_type: {ptype}"))

    errors.extend(_check_exact_id(principal.get("principal_id", ""), "principal.principal_id"))

    # MODEL_ROLE: role_type_id + carrier_profile_sha256 required, target_solver_contract_sha256=null
    if ptype == "MODEL_ROLE":
        if principal.get("role_type_id") is None or not _EXACT_ID_RE.match(str(principal.get("role_type_id", ""))):
            errors.append((EC.VAULT_PRINCIPAL_MISMATCH, "MODEL_ROLE requires role_type_id"))
        if principal.get("carrier_profile_sha256") is None or not _HASH_RE.match(str(principal.get("carrier_profile_sha256", ""))):
            errors.append((EC.VAULT_PRINCIPAL_MISMATCH, "MODEL_ROLE requires carrier_profile_sha256"))
        if principal.get("target_solver_contract_sha256") is not None:
            errors.append((EC.VAULT_PRINCIPAL_MISMATCH, "MODEL_ROLE must have target_solver_contract_sha256=null"))
        if principal.get("execution_attempt_id") is None:
            errors.append((EC.VAULT_PRINCIPAL_MISMATCH, "MODEL_ROLE requires execution_attempt_id"))

    # TARGET_SOLVER: target_solver_contract_sha256 required, role_type_id=null, carrier=null
    if ptype == "TARGET_SOLVER":
        if principal.get("role_type_id") is not None:
            errors.append((EC.VAULT_PRINCIPAL_MISMATCH, "TARGET_SOLVER must have role_type_id=null"))
        if principal.get("carrier_profile_sha256") is not None:
            errors.append((EC.VAULT_PRINCIPAL_MISMATCH, "TARGET_SOLVER must have carrier_profile_sha256=null"))
        if principal.get("target_solver_contract_sha256") is None or not _HASH_RE.match(str(principal.get("target_solver_contract_sha256", ""))):
            errors.append((EC.VAULT_PRINCIPAL_MISMATCH, "TARGET_SOLVER requires target_solver_contract_sha256"))
        if principal.get("execution_attempt_id") is None:
            errors.append((EC.VAULT_PRINCIPAL_MISMATCH, "TARGET_SOLVER requires execution_attempt_id"))

    return errors


def _check_object_binding(obj: dict[str, Any]) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.VAULT_OBJECT_HASH_MISMATCH, "object_binding is not an object")]
    required = {"object_id", "object_sha256", "sensitivity"}
    missing = required - set(obj.keys())
    if missing:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"object_binding missing: {missing}"))
        return errors
    errors.extend(_check_exact_id(obj.get("object_id", ""), "object_binding.object_id"))
    errors.extend(_check_hash(obj.get("object_sha256", ""), "object_binding.object_sha256"))
    sensitivity = obj.get("sensitivity", "")
    if sensitivity not in SENSITIVITY_LEVELS:
        errors.append((EC.VAULT_OBJECT_HASH_MISMATCH, f"invalid sensitivity: {sensitivity}"))
    return errors


def _check_view_binding(obj: dict[str, Any]) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.VAULT_VIEW_HASH_MISMATCH, "view_binding is not an object")]
    required = {"view_id", "view_sha256", "view_policy_sha256"}
    missing = required - set(obj.keys())
    if missing:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"view_binding missing: {missing}"))
        return errors
    errors.extend(_check_exact_id(obj.get("view_id", ""), "view_binding.view_id"))
    errors.extend(_check_hash(obj.get("view_sha256", ""), "view_binding.view_sha256"))
    errors.extend(_check_hash(obj.get("view_policy_sha256", ""), "view_binding.view_policy_sha256"))
    return errors


def _check_sink_binding(obj: dict[str, Any]) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.VAULT_SINK_MISMATCH, "sink_binding is not an object")]
    required = {"sink_id", "sink_kind", "sink_policy_sha256"}
    missing = required - set(obj.keys())
    if missing:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"sink_binding missing: {missing}"))
        return errors
    errors.extend(_check_exact_id(obj.get("sink_id", ""), "sink_binding.sink_id"))
    sink_kind = obj.get("sink_kind", "")
    if sink_kind not in SINK_KINDS:
        errors.append((EC.VAULT_SINK_MISMATCH, f"invalid sink_kind: {sink_kind}"))
    errors.extend(_check_hash(obj.get("sink_policy_sha256", ""), "sink_binding.sink_policy_sha256"))
    return errors


def _check_issuer(issuer: dict[str, Any]) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(issuer, dict):
        return [(EC.REQUIRED_FIELD_MISSING, "issuer is not an object")]
    required = {"issuer_principal_id", "issuer_key_id", "issuer_public_key_sha256"}
    missing = required - set(issuer.keys())
    if missing:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"issuer missing: {missing}"))
        return errors
    errors.extend(_check_exact_id(issuer.get("issuer_principal_id", ""), "issuer.issuer_principal_id"))
    errors.extend(_check_exact_id(issuer.get("issuer_key_id", ""), "issuer.issuer_key_id"))
    errors.extend(_check_hash(issuer.get("issuer_public_key_sha256", ""), "issuer.issuer_public_key_sha256"))
    return errors


def _check_revocation(revocation: dict[str, Any]) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(revocation, dict):
        return [(EC.REQUIRED_FIELD_MISSING, "revocation is not an object")]
    required = {"revocable", "revocation_handle", "status_at_issue", "registry_ref_and_hash"}
    missing = required - set(revocation.keys())
    if missing:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"revocation missing: {missing}"))
        return errors
    if revocation.get("revocable") is not True:
        errors.append((EC.VAULT_CAPABILITY_REVOKED, "revocation.revocable must be true"))
    errors.extend(_check_exact_id(revocation.get("revocation_handle", ""), "revocation.revocation_handle"))
    if revocation.get("status_at_issue") != "ACTIVE":
        errors.append((EC.VAULT_CAPABILITY_REVOKED, f"status_at_issue must be ACTIVE, got {revocation.get('status_at_issue')}"))
    errors.extend(_check_opaque_ref_hash(revocation.get("registry_ref_and_hash", {}), "revocation.registry_ref_and_hash"))
    return errors


def _check_signature_envelope(envelope: dict[str, Any], signed_bytes_hash: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(envelope, dict):
        return [(EC.SIGNATURE_INVALID, "signature_envelope is not an object")]
    required = {"algorithm", "key_id", "signer_principal_id", "signature_encoding",
                "signature_b64", "signed_bytes_hash", "trust_root_hash",
                "issuer_key_registry_hash"}
    missing = required - set(envelope.keys())
    if missing:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"signature_envelope missing: {missing}"))
        return errors
    if envelope.get("algorithm") != "Ed25519":
        errors.append((EC.SIGNATURE_ALGORITHM_INVALID, "algorithm must be Ed25519"))
    errors.extend(_check_exact_id(envelope.get("key_id", ""), "signature_envelope.key_id"))
    errors.extend(_check_exact_id(envelope.get("signer_principal_id", ""), "signature_envelope.signer_principal_id"))
    if envelope.get("signature_encoding") != "base64":
        errors.append((EC.SIGNATURE_INVALID, "signature_encoding must be base64"))
    sig_b64 = envelope.get("signature_b64", "")
    if not isinstance(sig_b64, str) or not _SIG_B64_RE.match(sig_b64):
        errors.append((EC.SIGNATURE_INVALID, "signature_b64 is not valid Ed25519 base64"))
    if envelope.get("signed_bytes_hash") != signed_bytes_hash:
        errors.append((EC.SIGNATURE_INVALID, "signed_bytes_hash mismatch in envelope"))
    errors.extend(_check_hash(envelope.get("trust_root_hash", ""), "signature_envelope.trust_root_hash"))
    errors.extend(_check_hash(envelope.get("issuer_key_registry_hash", ""), "signature_envelope.issuer_key_registry_hash"))
    return errors


def verify_vault_access_capability(
    capability: dict[str, Any],
    *,
    expected_capability_hash: str | None = None,
) -> VerificationResult:
    """验证 VaultAccessCapability 的 schema + semantic 合法性。

    检查：
    1. schema_id / schema_version / object_type 常量
    2. deny_by_default == true（硬约束）
    3. raw_vault_path_disclosure == false（硬约束）
    4. operation 在允许列表中（READ_RAW_OBJECT 被拒绝）
    5. principal 结构合法
    6. object_binding / view_binding / sink_binding 结构合法
    7. 时间戳为 canonical UTC
    8. nonce 格式合法
    9. issuer / revocation 结构合法
    10. signature_domain / canonicalizer_profile 常量
    11. signature_envelope 结构合法
    12. capability_hash 正确（sha256 of canonical JSON with capability_hash=null）
    13. TARGET_SOLVER + READ_DERIVED_VIEW/DERIVE_VIEW → sensitivity 只能是 PUBLIC/RESTRICTED
    14. WRITE_RESTRICTED_OBJECT/SEAL_RESTRICTED_OBJECT → sink_kind 只能是 RESTRICTED_VAULT/RESTRICTED_CAS
    """
    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. schema 常量
    if capability.get("schema_id") != _SCHEMA_ID:
        _err(EC.SCHEMA_ID_MISMATCH, f"schema_id must be {_SCHEMA_ID}, got {capability.get('schema_id')}")
    if capability.get("schema_version") != _SCHEMA_VERSION:
        _err(EC.SCHEMA_ID_MISMATCH, f"schema_version must be {_SCHEMA_VERSION}")
    if capability.get("object_type") != _OBJECT_TYPE:
        _err(EC.SCHEMA_ID_MISMATCH, f"object_type must be {_OBJECT_TYPE}")

    # 2. deny_by_default
    if capability.get("deny_by_default") is not True:
        _err(EC.VAULT_DENY_BY_DEFAULT_FALSE, "deny_by_default must be true")

    # 3. raw_vault_path_disclosure
    if capability.get("raw_vault_path_disclosure") is not False:
        _err(EC.VAULT_RAW_PATH_DISCLOSED, "raw_vault_path_disclosure must be false")

    # 4. operation
    operation = capability.get("operation", "")
    if operation in FORBIDDEN_OPERATIONS:
        _err(EC.VAULT_READ_RAW_OBJECT_REJECTED, f"operation {operation} is forbidden")
    elif operation not in VAULT_OPERATIONS:
        _err(EC.VAULT_OPERATION_MISMATCH, f"unknown operation: {operation}")

    # 5. capability_id
    for code, detail in _check_exact_id(capability.get("capability_id", ""), "capability_id"):
        _err(code, detail)

    # 6. principal
    for code, detail in _check_principal(capability.get("principal", {})):
        _err(code, detail)

    # 7. object_binding
    for code, detail in _check_object_binding(capability.get("object_binding", {})):
        _err(code, detail)

    # 8. view_binding
    for code, detail in _check_view_binding(capability.get("view_binding", {})):
        _err(code, detail)

    # 9. sink_binding
    for code, detail in _check_sink_binding(capability.get("sink_binding", {})):
        _err(code, detail)

    # 10. access_policy_ref_and_hash
    for code, detail in _check_opaque_ref_hash(capability.get("access_policy_ref_and_hash", {}), "access_policy_ref_and_hash"):
        _err(code, detail)

    # 11. 时间戳
    for ts_field in ("issued_at", "not_before", "expires_at"):
        ts = capability.get(ts_field, "")
        if not _check_canonical_utc(ts):
            _err(EC.TIME_NOT_CANONICAL_UTC, f"{ts_field} is not canonical UTC: {ts!r}")

    # 12. nonce
    for code, detail in _check_nonce(capability.get("nonce", "")):
        _err(code, detail)

    # 13. issuer
    for code, detail in _check_issuer(capability.get("issuer", {})):
        _err(code, detail)

    # 14. revocation
    for code, detail in _check_revocation(capability.get("revocation", {})):
        _err(code, detail)

    # 15. externally_pinned_trust_root
    for code, detail in _check_named_hash(capability.get("externally_pinned_trust_root", {}), "externally_pinned_trust_root"):
        _err(code, detail)

    # 16. issuer_key_registry_ref_and_hash
    for code, detail in _check_opaque_ref_hash(capability.get("issuer_key_registry_ref_and_hash", {}), "issuer_key_registry_ref_and_hash"):
        _err(code, detail)

    # 17. canonicalizer_profile
    if capability.get("canonicalizer_profile") != "RFC8785_JCS_UTF8":
        _err(EC.SCHEMA_ID_MISMATCH, "canonicalizer_profile must be RFC8785_JCS_UTF8")

    # 18. signature_domain
    sig_domain = capability.get("signature_domain", "")
    if sig_domain != _SIGNATURE_DOMAIN:
        _err(EC.SIGNATURE_DOMAIN_INVALID, f"signature_domain mismatch: expected {_SIGNATURE_DOMAIN!r}, got {sig_domain!r}")

    # 19. signed_bytes_hash
    for code, detail in _check_hash(capability.get("signed_bytes_hash", ""), "signed_bytes_hash"):
        _err(code, detail)

    # 20. signature_envelope
    for code, detail in _check_signature_envelope(
        capability.get("signature_envelope", {}),
        capability.get("signed_bytes_hash", ""),
    ):
        _err(code, detail)

    # 21. capability_hash_algorithm
    hash_algo = capability.get("capability_hash_algorithm", "")
    if hash_algo != _HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH, f"unexpected capability_hash_algorithm: {hash_algo}")

    # 22. capability_hash 验证
    obj_for_hash = dict(capability)
    obj_for_hash["capability_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if capability.get("capability_hash") != computed_hash:
        _err(EC.VAULT_CAPABILITY_HASH_MISMATCH,
             f"capability_hash mismatch: expected {computed_hash}, got {capability.get('capability_hash')}")

    if expected_capability_hash is not None and capability.get("capability_hash") != expected_capability_hash:
        _err(EC.VAULT_CAPABILITY_HASH_MISMATCH, f"capability_hash does not match expected {expected_capability_hash}")

    # 23. semantic: TARGET_SOLVER + READ_DERIVED_VIEW/DERIVE_VIEW → sensitivity PUBLIC/RESTRICTED
    principal = capability.get("principal", {})
    ptype = principal.get("principal_type", "")
    if ptype == "TARGET_SOLVER" and operation in ("READ_DERIVED_VIEW", "DERIVE_VIEW"):
        sensitivity = capability.get("object_binding", {}).get("sensitivity", "")
        if sensitivity not in ("PUBLIC", "RESTRICTED"):
            _err(EC.VAULT_OBJECT_HASH_MISMATCH,
                 f"TARGET_SOLVER can only access PUBLIC/RESTRICTED, got {sensitivity}")

    # 24. semantic: WRITE_RESTRICTED_OBJECT/SEAL_RESTRICTED_OBJECT → sink_kind RESTRICTED_VAULT/RESTRICTED_CAS
    if operation in ("WRITE_RESTRICTED_OBJECT", "SEAL_RESTRICTED_OBJECT"):
        sink_kind = capability.get("sink_binding", {}).get("sink_kind", "")
        if sink_kind not in ("RESTRICTED_VAULT", "RESTRICTED_CAS"):
            _err(EC.VAULT_SINK_MISMATCH,
                 f"WRITE/SEAL requires RESTRICTED_VAULT/RESTRICTED_CAS sink, got {sink_kind}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )
