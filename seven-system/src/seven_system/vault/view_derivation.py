"""ViewDerivation — sealed source → 精确 view → 精确 sink。

冻结 source hash、规则/生成器/redaction manifest hash、derived view hash、
sink write receipt 和仍有效的 revocation 检查。

模型交付模式只能是 OPAQUE_HANDLE_AND_DERIVED_BYTES，
且声明 raw locator 与 capability token 均未暴露。

deny_by_default 只能为 true，raw_vault_path_disclosed 只能为 false。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    FORBIDDEN_OPERATIONS,
    REVOCATION_STATUSES,
    SENSITIVITY_LEVELS,
    SINK_KINDS,
    VAULT_OPERATIONS,
    VAULT_PRINCIPAL_TYPES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from ..contracts.security_contract import _check_canonical_utc
from .access_capability import (
    _check_exact_id,
    _check_hash,
    _check_nonce,
    _check_opaque_ref_hash,
    _check_named_hash,
    _check_principal,
    _check_object_binding,
    _check_view_binding,
    _check_sink_binding,
    _check_issuer,
    _check_signature_envelope,
)
from .access_decision import _check_revocation_check


_SCHEMA_ID = "seven/view-derivation"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "ViewDerivation"
_SIGNATURE_DOMAIN = "seven-view-derivation/v1\0"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-derivation_hash-null)"


@dataclass(frozen=True)
class ViewDerivation:
    """ViewDerivation 数据对象。"""

    derivation_id: str
    capability_ref_and_hash: dict[str, str]
    access_decision_ref_and_hash: dict[str, str]
    principal: dict[str, Any]
    operation: str
    source_object: dict[str, Any]
    derived_view: dict[str, Any]
    sink_binding: dict[str, Any]
    view_policy_ref_and_hash: dict[str, str]
    derivation_rule_ref_and_hash: dict[str, str]
    generator_ref_and_hash: dict[str, str]
    redaction_manifest_ref_and_hash: dict[str, str]
    sink_write_receipt_ref_and_hash: dict[str, str]
    revocation_check: dict[str, Any]
    nonce: str
    deny_by_default: bool
    raw_vault_path_disclosed: bool
    model_delivery: dict[str, Any]
    derived_at: str
    issuer: dict[str, Any]
    externally_pinned_trust_root: dict[str, str]
    issuer_key_registry_ref_and_hash: dict[str, str]
    canonicalizer_profile: str
    signature_domain: str
    signed_bytes_hash: str
    signature_envelope: dict[str, Any]
    derivation_hash_algorithm: str
    derivation_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "object_type": _OBJECT_TYPE,
            "derivation_id": self.derivation_id,
            "capability_ref_and_hash": dict(self.capability_ref_and_hash),
            "access_decision_ref_and_hash": dict(self.access_decision_ref_and_hash),
            "principal": dict(self.principal),
            "operation": self.operation,
            "source_object": dict(self.source_object),
            "derived_view": dict(self.derived_view),
            "sink_binding": dict(self.sink_binding),
            "view_policy_ref_and_hash": dict(self.view_policy_ref_and_hash),
            "derivation_rule_ref_and_hash": dict(self.derivation_rule_ref_and_hash),
            "generator_ref_and_hash": dict(self.generator_ref_and_hash),
            "redaction_manifest_ref_and_hash": dict(self.redaction_manifest_ref_and_hash),
            "sink_write_receipt_ref_and_hash": dict(self.sink_write_receipt_ref_and_hash),
            "revocation_check": dict(self.revocation_check),
            "nonce": self.nonce,
            "deny_by_default": self.deny_by_default,
            "raw_vault_path_disclosed": self.raw_vault_path_disclosed,
            "model_delivery": dict(self.model_delivery),
            "derived_at": self.derived_at,
            "issuer": dict(self.issuer),
            "externally_pinned_trust_root": dict(self.externally_pinned_trust_root),
            "issuer_key_registry_ref_and_hash": dict(self.issuer_key_registry_ref_and_hash),
            "canonicalizer_profile": self.canonicalizer_profile,
            "signature_domain": self.signature_domain,
            "signed_bytes_hash": self.signed_bytes_hash,
            "signature_envelope": dict(self.signature_envelope),
            "derivation_hash_algorithm": self.derivation_hash_algorithm,
            "derivation_hash": self.derivation_hash,
        }


def _check_model_delivery(model_delivery: dict[str, Any]) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(model_delivery, dict):
        return [(EC.VIEW_DELIVERY_MODE_INVALID, "model_delivery is not an object")]
    required = {"delivery_mode", "delivered_view_binding_source",
                "raw_vault_locator_exposed", "capability_token_exposed"}
    missing = required - set(model_delivery.keys())
    if missing:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"model_delivery missing: {missing}"))
        return errors
    if model_delivery.get("delivery_mode") != "OPAQUE_HANDLE_AND_DERIVED_BYTES":
        errors.append((EC.VIEW_DELIVERY_MODE_INVALID,
                       f"delivery_mode must be OPAQUE_HANDLE_AND_DERIVED_BYTES, got {model_delivery.get('delivery_mode')}"))
    if model_delivery.get("delivered_view_binding_source") != "TOP_LEVEL_DERIVED_VIEW":
        errors.append((EC.VIEW_DELIVERY_MODE_INVALID,
                       f"delivered_view_binding_source must be TOP_LEVEL_DERIVED_VIEW"))
    if model_delivery.get("raw_vault_locator_exposed") is not False:
        errors.append((EC.VIEW_RAW_LOCATOR_EXPOSED, "raw_vault_locator_exposed must be false"))
    if model_delivery.get("capability_token_exposed") is not False:
        errors.append((EC.VIEW_CAPABILITY_TOKEN_EXPOSED, "capability_token_exposed must be false"))
    return errors


def verify_view_derivation(
    derivation: dict[str, Any],
    *,
    capability: dict[str, Any] | None = None,
    access_decision: dict[str, Any] | None = None,
    expected_derivation_hash: str | None = None,
) -> VerificationResult:
    """验证 ViewDerivation 的 schema + semantic 合法性。

    检查：
    1. schema 常量
    2. deny_by_default == true, raw_vault_path_disclosed == false
    3. model_delivery: OPAQUE_HANDLE_AND_DERIVED_BYTES, raw locator / capability token 未暴露
    4. revocation_check: status 必须为 ACTIVE, revocation_record_ref_and_hash 必须为 null
    5. source_object / derived_view / sink_binding 结构合法
    6. 所有 ref_and_hash 结构合法
    7. derivation_hash 正确
    8. 如果提供 capability / access_decision：逐字段比较
    9. semantic: TARGET_SOLVER → sensitivity PUBLIC/RESTRICTED
    10. semantic: WRITE/SEAL → sink_kind RESTRICTED
    """
    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. schema 常量
    if derivation.get("schema_id") != _SCHEMA_ID:
        _err(EC.SCHEMA_ID_MISMATCH, f"schema_id must be {_SCHEMA_ID}")
    if derivation.get("schema_version") != _SCHEMA_VERSION:
        _err(EC.SCHEMA_ID_MISMATCH, f"schema_version must be {_SCHEMA_VERSION}")
    if derivation.get("object_type") != _OBJECT_TYPE:
        _err(EC.SCHEMA_ID_MISMATCH, f"object_type must be {_OBJECT_TYPE}")

    # 2. deny_by_default / raw_vault_path_disclosed
    if derivation.get("deny_by_default") is not True:
        _err(EC.VAULT_DENY_BY_DEFAULT_FALSE, "deny_by_default must be true")
    if derivation.get("raw_vault_path_disclosed") is not False:
        _err(EC.VAULT_RAW_PATH_DISCLOSED, "raw_vault_path_disclosed must be false")

    # 3. derivation_id
    for code, detail in _check_exact_id(derivation.get("derivation_id", ""), "derivation_id"):
        _err(code, detail)

    # 4. capability_ref_and_hash / access_decision_ref_and_hash
    for code, detail in _check_opaque_ref_hash(derivation.get("capability_ref_and_hash", {}), "capability_ref_and_hash"):
        _err(code, detail)
    for code, detail in _check_opaque_ref_hash(derivation.get("access_decision_ref_and_hash", {}), "access_decision_ref_and_hash"):
        _err(code, detail)

    # 5. principal / operation
    for code, detail in _check_principal(derivation.get("principal", {})):
        _err(code, detail)
    operation = derivation.get("operation", "")
    if operation in FORBIDDEN_OPERATIONS:
        _err(EC.VAULT_READ_RAW_OBJECT_REJECTED, f"operation {operation} is forbidden")
    elif operation not in VAULT_OPERATIONS:
        _err(EC.VAULT_OPERATION_MISMATCH, f"unknown operation: {operation}")

    # 6. source_object / derived_view / sink_binding
    for code, detail in _check_object_binding(derivation.get("source_object", {})):
        _err(code, detail)
    for code, detail in _check_view_binding(derivation.get("derived_view", {})):
        _err(code, detail)
    for code, detail in _check_sink_binding(derivation.get("sink_binding", {})):
        _err(code, detail)

    # 7. ref_and_hash fields
    for field_name in ("view_policy_ref_and_hash", "derivation_rule_ref_and_hash",
                       "generator_ref_and_hash", "redaction_manifest_ref_and_hash",
                       "sink_write_receipt_ref_and_hash"):
        for code, detail in _check_opaque_ref_hash(derivation.get(field_name, {}), field_name):
            _err(code, detail)

    # 8. revocation_check — ViewDerivation 中 status 必须为 ACTIVE, record_ref 必须为 null
    revocation_check = derivation.get("revocation_check", {})
    for code, detail in _check_revocation_check(revocation_check):
        _err(code, detail)
    if isinstance(revocation_check, dict):
        if revocation_check.get("status") != "ACTIVE":
            _err(EC.VAULT_CAPABILITY_REVOKED,
                 f"ViewDerivation revocation_check.status must be ACTIVE, got {revocation_check.get('status')}")
        if revocation_check.get("revocation_record_ref_and_hash") is not None:
            _err(EC.VAULT_CAPABILITY_REVOKED,
                 "ViewDerivation revocation_record_ref_and_hash must be null")

    # 9. nonce
    for code, detail in _check_nonce(derivation.get("nonce", "")):
        _err(code, detail)

    # 10. model_delivery
    for code, detail in _check_model_delivery(derivation.get("model_delivery", {})):
        _err(code, detail)

    # 11. derived_at
    if not _check_canonical_utc(derivation.get("derived_at", "")):
        _err(EC.TIME_NOT_CANONICAL_UTC, "derived_at is not canonical UTC")

    # 12. issuer / trust_root / key_registry
    for code, detail in _check_issuer(derivation.get("issuer", {})):
        _err(code, detail)
    for code, detail in _check_named_hash(derivation.get("externally_pinned_trust_root", {}), "externally_pinned_trust_root"):
        _err(code, detail)
    for code, detail in _check_opaque_ref_hash(derivation.get("issuer_key_registry_ref_and_hash", {}), "issuer_key_registry_ref_and_hash"):
        _err(code, detail)

    # 13. canonicalizer_profile / signature_domain
    if derivation.get("canonicalizer_profile") != "RFC8785_JCS_UTF8":
        _err(EC.SCHEMA_ID_MISMATCH, "canonicalizer_profile must be RFC8785_JCS_UTF8")
    sig_domain = derivation.get("signature_domain", "")
    if sig_domain != _SIGNATURE_DOMAIN:
        _err(EC.SIGNATURE_DOMAIN_INVALID, f"signature_domain mismatch")

    # 14. signed_bytes_hash
    for code, detail in _check_hash(derivation.get("signed_bytes_hash", ""), "signed_bytes_hash"):
        _err(code, detail)

    # 15. signature_envelope
    for code, detail in _check_signature_envelope(
        derivation.get("signature_envelope", {}),
        derivation.get("signed_bytes_hash", ""),
    ):
        _err(code, detail)

    # 16. derivation_hash_algorithm
    hash_algo = derivation.get("derivation_hash_algorithm", "")
    if hash_algo != _HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH, f"unexpected derivation_hash_algorithm: {hash_algo}")

    # 17. derivation_hash 验证
    obj_for_hash = dict(derivation)
    obj_for_hash["derivation_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if derivation.get("derivation_hash") != computed_hash:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"derivation_hash mismatch: expected {computed_hash}, got {derivation.get('derivation_hash')}")

    if expected_derivation_hash is not None and derivation.get("derivation_hash") != expected_derivation_hash:
        _err(EC.OBJECT_HASH_MISMATCH, "derivation_hash does not match expected")

    # 18. 如果提供 capability：逐字段比较
    if capability is not None:
        cap_ref = derivation.get("capability_ref_and_hash", {})
        if cap_ref.get("sha256") != capability.get("capability_hash"):
            _err(EC.VAULT_CAPABILITY_HASH_MISMATCH,
                 f"capability_ref sha256 mismatch: derivation has {cap_ref.get('sha256')}, "
                 f"capability has {capability.get('capability_hash')}")

        for field_name in ("principal", "operation", "nonce"):
            if derivation.get(field_name) != capability.get(field_name):
                _err(EC.VAULT_PRINCIPAL_MISMATCH if field_name == "principal"
                     else EC.VAULT_OPERATION_MISMATCH if field_name == "operation"
                     else EC.VAULT_NONCE_REPLAY,
                     f"field {field_name} mismatch between derivation and capability")

        # source_object should match capability.object_binding
        if derivation.get("source_object") != capability.get("object_binding"):
            _err(EC.VIEW_SOURCE_HASH_MISMATCH, "source_object mismatch with capability.object_binding")
        # derived_view: view_id and view_policy_sha256 must match capability;
        # view_sha256 is the actual derived hash (may differ from capability's expected hash)
        deriv_view = derivation.get("derived_view", {})
        cap_view = capability.get("view_binding", {})
        if deriv_view.get("view_id") != cap_view.get("view_id"):
            _err(EC.VAULT_VIEW_HASH_MISMATCH, "derived_view.view_id mismatch with capability.view_binding")
        if deriv_view.get("view_policy_sha256") != cap_view.get("view_policy_sha256"):
            _err(EC.VAULT_VIEW_HASH_MISMATCH, "derived_view.view_policy_sha256 mismatch with capability.view_binding")
        if derivation.get("sink_binding") != capability.get("sink_binding"):
            _err(EC.VAULT_SINK_MISMATCH, "sink_binding mismatch with capability.sink_binding")

    # 19. 如果提供 access_decision：比较 refs
    if access_decision is not None:
        dec_ref = derivation.get("access_decision_ref_and_hash", {})
        if dec_ref.get("sha256") != access_decision.get("decision_hash"):
            _err(EC.OBJECT_HASH_MISMATCH,
                 f"access_decision_ref sha256 mismatch: derivation has {dec_ref.get('sha256')}, "
                 f"decision has {access_decision.get('decision_hash')}")

        for field_name in ("principal", "operation", "nonce"):
            if derivation.get(field_name) != access_decision.get(field_name):
                _err(EC.VAULT_PRINCIPAL_MISMATCH if field_name == "principal"
                     else EC.VAULT_OPERATION_MISMATCH if field_name == "operation"
                     else EC.VAULT_NONCE_REPLAY,
                     f"field {field_name} mismatch between derivation and access_decision")

    # 20. semantic: TARGET_SOLVER → sensitivity PUBLIC/RESTRICTED
    principal = derivation.get("principal", {})
    ptype = principal.get("principal_type", "")
    if ptype == "TARGET_SOLVER" and operation in ("READ_DERIVED_VIEW", "DERIVE_VIEW"):
        sensitivity = derivation.get("source_object", {}).get("sensitivity", "")
        if sensitivity not in ("PUBLIC", "RESTRICTED"):
            _err(EC.VAULT_OBJECT_HASH_MISMATCH,
                 f"TARGET_SOLVER can only access PUBLIC/RESTRICTED, got {sensitivity}")

    # 21. semantic: WRITE/SEAL → sink_kind RESTRICTED
    if operation in ("WRITE_RESTRICTED_OBJECT", "SEAL_RESTRICTED_OBJECT"):
        sink_kind = derivation.get("sink_binding", {}).get("sink_kind", "")
        if sink_kind not in ("RESTRICTED_VAULT", "RESTRICTED_CAS"):
            _err(EC.VAULT_SINK_MISMATCH,
                 f"WRITE/SEAL requires RESTRICTED sink, got {sink_kind}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )
