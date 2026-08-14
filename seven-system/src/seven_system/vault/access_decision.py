"""AccessDecision — 逐请求重新验签和查撤销。

必须重验 capability 签名与 issuer trust，并逐字段比较
principal/operation/object/view/sink，检查时窗、nonce replay 和最新 revocation registry。
只有全部检查 PASS、revocation=ACTIVE 才能 ALLOW；撤销状态未知也必须 DENY。

deny_by_default 只能为 true，raw_vault_path_disclosed 只能为 false。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ACCESS_DECISIONS,
    ACCESS_REASON_CODES,
    CHECK_RESULTS,
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
    verify_vault_access_capability,
)


_SCHEMA_ID = "seven/access-decision"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "AccessDecision"
_SIGNATURE_DOMAIN = "seven-access-decision/v1\0"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-decision_hash-null)"

_CHECK_FIELDS = (
    "capability_signature", "issuer_trust", "time_window",
    "principal", "operation", "object_hash", "view_hash",
    "sink", "nonce_replay", "access_policy",
)


@dataclass(frozen=True)
class AccessDecision:
    """AccessDecision 数据对象。"""

    decision_id: str
    access_request_id: str
    capability_ref_and_hash: dict[str, str]
    principal: dict[str, Any]
    operation: str
    object_binding: dict[str, Any]
    view_binding: dict[str, Any]
    sink_binding: dict[str, Any]
    nonce: str
    access_policy_ref_and_hash: dict[str, str]
    deny_by_default: bool
    raw_vault_path_disclosed: bool
    checks: dict[str, str]
    revocation_check: dict[str, Any]
    decision: str
    reason_codes: list[str]
    evaluated_at: str
    issuer: dict[str, Any]
    externally_pinned_trust_root: dict[str, str]
    issuer_key_registry_ref_and_hash: dict[str, str]
    canonicalizer_profile: str
    signature_domain: str
    signed_bytes_hash: str
    signature_envelope: dict[str, Any]
    decision_hash_algorithm: str
    decision_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "object_type": _OBJECT_TYPE,
            "decision_id": self.decision_id,
            "access_request_id": self.access_request_id,
            "capability_ref_and_hash": dict(self.capability_ref_and_hash),
            "principal": dict(self.principal),
            "operation": self.operation,
            "object_binding": dict(self.object_binding),
            "view_binding": dict(self.view_binding),
            "sink_binding": dict(self.sink_binding),
            "nonce": self.nonce,
            "access_policy_ref_and_hash": dict(self.access_policy_ref_and_hash),
            "deny_by_default": self.deny_by_default,
            "raw_vault_path_disclosed": self.raw_vault_path_disclosed,
            "checks": dict(self.checks),
            "revocation_check": dict(self.revocation_check),
            "decision": self.decision,
            "reason_codes": list(self.reason_codes),
            "evaluated_at": self.evaluated_at,
            "issuer": dict(self.issuer),
            "externally_pinned_trust_root": dict(self.externally_pinned_trust_root),
            "issuer_key_registry_ref_and_hash": dict(self.issuer_key_registry_ref_and_hash),
            "canonicalizer_profile": self.canonicalizer_profile,
            "signature_domain": self.signature_domain,
            "signed_bytes_hash": self.signed_bytes_hash,
            "signature_envelope": dict(self.signature_envelope),
            "decision_hash_algorithm": self.decision_hash_algorithm,
            "decision_hash": self.decision_hash,
        }


def _check_revocation_check(revocation_check: dict[str, Any]) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(revocation_check, dict):
        return [(EC.REQUIRED_FIELD_MISSING, "revocation_check is not an object")]
    required = {"revocation_handle", "status", "registry_ref_and_hash",
                "checked_at", "revocation_record_ref_and_hash"}
    missing = required - set(revocation_check.keys())
    if missing:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"revocation_check missing: {missing}"))
        return errors
    errors.extend(_check_exact_id(revocation_check.get("revocation_handle", ""), "revocation_check.revocation_handle"))
    status = revocation_check.get("status", "")
    if status not in REVOCATION_STATUSES:
        errors.append((EC.VAULT_REVOCATION_UNKNOWN, f"invalid revocation status: {status}"))
    errors.extend(_check_opaque_ref_hash(revocation_check.get("registry_ref_and_hash", {}), "revocation_check.registry_ref_and_hash"))
    if not _check_canonical_utc(revocation_check.get("checked_at", "")):
        errors.append((EC.TIME_NOT_CANONICAL_UTC, "revocation_check.checked_at is not canonical UTC"))
    rec_ref = revocation_check.get("revocation_record_ref_and_hash")
    if rec_ref is not None:
        errors.extend(_check_opaque_ref_hash(rec_ref, "revocation_check.revocation_record_ref_and_hash"))
    return errors


def verify_access_decision(
    decision: dict[str, Any],
    *,
    capability: dict[str, Any] | None = None,
    seen_nonces: set[str] | None = None,
    evaluation_time: str | None = None,
    expected_decision_hash: str | None = None,
) -> VerificationResult:
    """验证 AccessDecision 的 schema + semantic 合法性。

    如果提供 capability，则逐字段比较 decision 与 capability 的
    principal/operation/object/view/sink/nonce 是否一致。

    检查：
    1. schema 常量
    2. deny_by_default == true, raw_vault_path_disclosed == false
    3. decision 在 ALLOW/DENY 中
    4. checks 结构合法
    5. revocation_check 结构合法
    6. reason_codes 合法
    7. ALLOW → 所有 checks PASS, revocation ACTIVE, reason_codes == ["POLICY_ALLOW"]
    8. DENY → reason_codes 至少一个非 POLICY_ALLOW
    9. 如果提供 capability：逐字段比较
    10. nonce replay 检查
    11. 时间窗检查
    12. decision_hash 正确
    13. signature_envelope 合法
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

    # 2. deny_by_default / raw_vault_path_disclosed
    if decision.get("deny_by_default") is not True:
        _err(EC.VAULT_DENY_BY_DEFAULT_FALSE, "deny_by_default must be true")
    if decision.get("raw_vault_path_disclosed") is not False:
        _err(EC.VAULT_RAW_PATH_DISCLOSED, "raw_vault_path_disclosed must be false")

    # 3. decision
    dec = decision.get("decision", "")
    if dec not in ACCESS_DECISIONS:
        _err(EC.VAULT_ACCESS_DENIED, f"invalid decision: {dec}")

    # 4. IDs
    for code, detail in _check_exact_id(decision.get("decision_id", ""), "decision_id"):
        _err(code, detail)
    for code, detail in _check_exact_id(decision.get("access_request_id", ""), "access_request_id"):
        _err(code, detail)

    # 5. capability_ref_and_hash
    for code, detail in _check_opaque_ref_hash(decision.get("capability_ref_and_hash", {}), "capability_ref_and_hash"):
        _err(code, detail)

    # 6. principal / operation / object / view / sink
    for code, detail in _check_principal(decision.get("principal", {})):
        _err(code, detail)
    operation = decision.get("operation", "")
    if operation in FORBIDDEN_OPERATIONS:
        _err(EC.VAULT_READ_RAW_OBJECT_REJECTED, f"operation {operation} is forbidden")
    elif operation not in VAULT_OPERATIONS:
        _err(EC.VAULT_OPERATION_MISMATCH, f"unknown operation: {operation}")
    for code, detail in _check_object_binding(decision.get("object_binding", {})):
        _err(code, detail)
    for code, detail in _check_view_binding(decision.get("view_binding", {})):
        _err(code, detail)
    for code, detail in _check_sink_binding(decision.get("sink_binding", {})):
        _err(code, detail)

    # 7. nonce
    for code, detail in _check_nonce(decision.get("nonce", "")):
        _err(code, detail)

    # 8. access_policy_ref_and_hash
    for code, detail in _check_opaque_ref_hash(decision.get("access_policy_ref_and_hash", {}), "access_policy_ref_and_hash"):
        _err(code, detail)

    # 9. checks
    checks = decision.get("checks", {})
    if not isinstance(checks, dict):
        _err(EC.REQUIRED_FIELD_MISSING, "checks is not an object")
    else:
        for field_name in _CHECK_FIELDS:
            if field_name not in checks:
                _err(EC.REQUIRED_FIELD_MISSING, f"checks missing: {field_name}")
            elif checks[field_name] not in CHECK_RESULTS:
                _err(EC.REQUIRED_FIELD_MISSING, f"checks.{field_name} invalid: {checks[field_name]}")

    # 10. revocation_check
    for code, detail in _check_revocation_check(decision.get("revocation_check", {})):
        _err(code, detail)

    # 11. reason_codes
    reason_codes = decision.get("reason_codes", [])
    if not isinstance(reason_codes, list):
        _err(EC.REQUIRED_FIELD_MISSING, "reason_codes is not an array")
    else:
        for rc in reason_codes:
            if rc not in ACCESS_REASON_CODES:
                _err(EC.REQUIRED_FIELD_MISSING, f"invalid reason_code: {rc}")
        if len(reason_codes) != len(set(reason_codes)):
            _err(EC.REQUIRED_FIELD_MISSING, "reason_codes has duplicates")

    # 12. evaluated_at
    if not _check_canonical_utc(decision.get("evaluated_at", "")):
        _err(EC.TIME_NOT_CANONICAL_UTC, "evaluated_at is not canonical UTC")

    # 13. issuer / trust_root / key_registry
    for code, detail in _check_issuer(decision.get("issuer", {})):
        _err(code, detail)
    for code, detail in _check_named_hash(decision.get("externally_pinned_trust_root", {}), "externally_pinned_trust_root"):
        _err(code, detail)
    for code, detail in _check_opaque_ref_hash(decision.get("issuer_key_registry_ref_and_hash", {}), "issuer_key_registry_ref_and_hash"):
        _err(code, detail)

    # 14. canonicalizer_profile / signature_domain
    if decision.get("canonicalizer_profile") != "RFC8785_JCS_UTF8":
        _err(EC.SCHEMA_ID_MISMATCH, "canonicalizer_profile must be RFC8785_JCS_UTF8")
    sig_domain = decision.get("signature_domain", "")
    if sig_domain != _SIGNATURE_DOMAIN:
        _err(EC.SIGNATURE_DOMAIN_INVALID, f"signature_domain mismatch")

    # 15. signed_bytes_hash
    for code, detail in _check_hash(decision.get("signed_bytes_hash", ""), "signed_bytes_hash"):
        _err(code, detail)

    # 16. signature_envelope
    for code, detail in _check_signature_envelope(
        decision.get("signature_envelope", {}),
        decision.get("signed_bytes_hash", ""),
    ):
        _err(code, detail)

    # 17. decision_hash_algorithm
    hash_algo = decision.get("decision_hash_algorithm", "")
    if hash_algo != _HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH, f"unexpected decision_hash_algorithm: {hash_algo}")

    # 18. decision_hash 验证
    obj_for_hash = dict(decision)
    obj_for_hash["decision_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if decision.get("decision_hash") != computed_hash:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"decision_hash mismatch: expected {computed_hash}, got {decision.get('decision_hash')}")

    if expected_decision_hash is not None and decision.get("decision_hash") != expected_decision_hash:
        _err(EC.OBJECT_HASH_MISMATCH, f"decision_hash does not match expected")

    # 19. ALLOW 语义约束
    if dec == "ALLOW":
        for field_name in _CHECK_FIELDS:
            if checks.get(field_name) != "PASS":
                _err(EC.VAULT_ACCESS_DENIED, f"ALLOW requires all checks PASS, {field_name}={checks.get(field_name)}")
        rev_status = decision.get("revocation_check", {}).get("status", "")
        if rev_status != "ACTIVE":
            _err(EC.VAULT_CAPABILITY_REVOKED, f"ALLOW requires revocation ACTIVE, got {rev_status}")
        if reason_codes != ["POLICY_ALLOW"]:
            _err(EC.VAULT_ACCESS_DENIED, f"ALLOW requires reason_codes == ['POLICY_ALLOW'], got {reason_codes}")

    # 20. DENY 语义约束
    if dec == "DENY":
        if not reason_codes or all(rc == "POLICY_ALLOW" for rc in reason_codes):
            _err(EC.VAULT_ACCESS_DENIED, "DENY requires at least one non-POLICY_ALLOW reason_code")

    # 21. 如果提供 capability，逐字段比较
    if capability is not None:
        cap_result = verify_vault_access_capability(capability)
        if not cap_result.passed:
            _err(EC.VAULT_CAPABILITY_HASH_MISMATCH, "capability itself is invalid")
        else:
            # 比较 capability_ref_and_hash.sha256 == capability.capability_hash
            cap_ref = decision.get("capability_ref_and_hash", {})
            if cap_ref.get("sha256") != capability.get("capability_hash"):
                _err(EC.VAULT_CAPABILITY_HASH_MISMATCH,
                     f"capability_ref sha256 mismatch: decision has {cap_ref.get('sha256')}, "
                     f"capability has {capability.get('capability_hash')}")

            # 逐字段比较
            for field_name in ("principal", "operation", "object_binding", "view_binding", "sink_binding", "nonce"):
                if decision.get(field_name) != capability.get(field_name):
                    _err(EC.VAULT_PRINCIPAL_MISMATCH if field_name == "principal"
                         else EC.VAULT_OPERATION_MISMATCH if field_name == "operation"
                         else EC.VAULT_OBJECT_HASH_MISMATCH if field_name == "object_binding"
                         else EC.VAULT_VIEW_HASH_MISMATCH if field_name == "view_binding"
                         else EC.VAULT_SINK_MISMATCH if field_name == "sink_binding"
                         else EC.VAULT_NONCE_REPLAY,
                         f"field {field_name} mismatch between decision and capability")

            # access_policy_ref_and_hash
            if decision.get("access_policy_ref_and_hash") != capability.get("access_policy_ref_and_hash"):
                _err(EC.VAULT_ACCESS_DENIED, "access_policy_ref_and_hash mismatch")

            # issuer
            if decision.get("issuer") != capability.get("issuer"):
                _err(EC.VAULT_ACCESS_DENIED, "issuer mismatch")

            # externally_pinned_trust_root
            if decision.get("externally_pinned_trust_root") != capability.get("externally_pinned_trust_root"):
                _err(EC.VAULT_ACCESS_DENIED, "externally_pinned_trust_root mismatch")

    # 22. nonce replay 检查
    if seen_nonces is not None:
        nonce = decision.get("nonce", "")
        if nonce in seen_nonces:
            _err(EC.VAULT_NONCE_REPLAY, f"nonce replay detected: {nonce}")
            if checks.get("nonce_replay") != "FAIL":
                _err(EC.VAULT_NONCE_REPLAY, "nonce_replay check should be FAIL for replayed nonce")

    # 23. 时间窗检查
    if evaluation_time is not None and capability is not None:
        not_before = capability.get("not_before", "")
        expires_at = capability.get("expires_at", "")
        if evaluation_time < not_before:
            _err(EC.VAULT_CAPABILITY_NOT_YET_VALID, f"evaluation_time {evaluation_time} < not_before {not_before}")
        if evaluation_time >= expires_at:
            _err(EC.VAULT_CAPABILITY_EXPIRED, f"evaluation_time {evaluation_time} >= expires_at {expires_at}")

    # 24. semantic: TARGET_SOLVER + READ_DERIVED_VIEW/DERIVE_VIEW → sensitivity PUBLIC/RESTRICTED
    principal = decision.get("principal", {})
    ptype = principal.get("principal_type", "")
    if ptype == "TARGET_SOLVER" and operation in ("READ_DERIVED_VIEW", "DERIVE_VIEW"):
        sensitivity = decision.get("object_binding", {}).get("sensitivity", "")
        if sensitivity not in ("PUBLIC", "RESTRICTED"):
            _err(EC.VAULT_OBJECT_HASH_MISMATCH,
                 f"TARGET_SOLVER can only access PUBLIC/RESTRICTED, got {sensitivity}")

    # 25. semantic: WRITE/SEAL → sink_kind RESTRICTED_VAULT/RESTRICTED_CAS
    if operation in ("WRITE_RESTRICTED_OBJECT", "SEAL_RESTRICTED_OBJECT"):
        sink_kind = decision.get("sink_binding", {}).get("sink_kind", "")
        if sink_kind not in ("RESTRICTED_VAULT", "RESTRICTED_CAS"):
            _err(EC.VAULT_SINK_MISMATCH,
                 f"WRITE/SEAL requires RESTRICTED sink, got {sink_kind}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )
