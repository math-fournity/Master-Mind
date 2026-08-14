"""SecurityContractVerifier — GV0 唯一拥有的安全合同验证器。

检查签名、有效期、撤销、root/roster/policy 一致性、
Assignment scope、EEA→Permit 不可扩权、ordinal 唯一和额度守恒。

SecurityContractVerifier 的原子预留接口由 GV0 冻结（ReservationBackendPort）。
WP-DB1I 只实现 SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER 后端，
WP-RT1 只实现 canonical DB expected-revision transaction 后端。
任一后端不得复制、放宽或跳过 GV0 的验证顺序。
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from .errors import (
    ALLOWANCE_FIELDS,
    AUTHORIZATION_MODES,
    CONSUMPTION_STATUSES,
    VerificationErrorCode as EC,
)
from .completion_contract import VerificationResult


# canonical UTC timestamp pattern
_CANONICAL_UTC_RE = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
    r"(\.[0-9]{1,9})?Z$"
)


def _check_canonical_utc(value: str) -> bool:
    return bool(_CANONICAL_UTC_RE.match(value))


def _allowance_from_dict(d: dict[str, Any]) -> dict[str, int]:
    """提取额度字段为纯整数字典。"""
    return {f: int(d.get(f, 0)) for f in ALLOWANCE_FIELDS}


def _allowance_le(a: dict[str, int], b: dict[str, int]) -> bool:
    """检查 a 的每个字段 <= b 的对应字段。"""
    return all(a.get(f, 0) <= b.get(f, 0) for f in ALLOWANCE_FIELDS)


def _allowance_add(
    a: dict[str, int], b: dict[str, int]
) -> dict[str, int]:
    """额度相加。"""
    return {f: a.get(f, 0) + b.get(f, 0) for f in ALLOWANCE_FIELDS}


def _allowance_is_zero(a: dict[str, int]) -> bool:
    return all(a.get(f, 0) == 0 for f in ALLOWANCE_FIELDS)


def verify_signature_envelope(
    envelope: dict[str, Any],
    *,
    expected_domain: str,
    signed_bytes_hash: str,
) -> list[tuple[EC, str]]:
    """验证签名 envelope 的结构合法性。

    本方法只做结构检查（算法、hash 匹配）。
    domain separator 在父对象层（EEA/Permit 的 signature_domain 字段），
    不在 envelope 内，由调用方在对象层检查。
    真实 Ed25519 验签由 HumanGateService 的 AttestationSignerPort 执行，
    GV0 不拥有密钥验证能力。
    """
    errors: list[tuple[EC, str]] = []

    algorithm = envelope.get("algorithm", "")
    if algorithm != "Ed25519":
        errors.append((EC.SIGNATURE_ALGORITHM_INVALID, f"algorithm must be Ed25519, got {algorithm}"))

    env_signed_hash = envelope.get("signed_bytes_hash", "")
    if env_signed_hash != signed_bytes_hash:
        errors.append((EC.SIGNATURE_INVALID, f"signed_bytes_hash mismatch: envelope has {env_signed_hash}, expected {signed_bytes_hash}"))

    sig_b64 = envelope.get("signature_b64", "")
    if not re.match(r"^[A-Za-z0-9+/]{86}==$", sig_b64):
        errors.append((EC.SIGNATURE_INVALID, "signature_b64 is not valid Ed25519 base64 (86 chars + ==)"))

    return errors


def verify_eea(
    eea: dict[str, Any],
    *,
    expected_eea_hash: str | None = None,
) -> VerificationResult:
    """验证 ExternalExecutionAuthorization 的结构合法性。

    检查：
    - authorization_mode 合法
    - AUDITED_ACTIVATION 必须有 activation_audit_record_refs
    - UNAUDITED_AUTHORIZED_CANARY 必须有 unaudited_dependency_bundle_refs
    - 至少一项预算为正（EC.EEA_ZERO_BUDGET）
    - 时间戳为 canonical UTC
    - 签名 envelope 结构合法
    - authorization_hash 正确
    """
    errors: list[VerificationErrorCode] = []
    details: list[str] = []

    mode = eea.get("authorization_mode", "")
    if mode not in AUTHORIZATION_MODES:
        errors.append(EC.EEA_MODE_BINDING_INVALID)
        details.append(f"unknown authorization_mode: {mode}")

    if mode == "AUDITED_ACTIVATION":
        if not eea.get("activation_audit_record_refs_and_hashes"):
            errors.append(EC.EEA_MODE_BINDING_INVALID)
            details.append("AUDITED_ACTIVATION requires activation_audit_record_refs_and_hashes")
        if eea.get("unaudited_dependency_bundle_refs_and_hashes"):
            errors.append(EC.EEA_MODE_BINDING_INVALID)
            details.append("AUDITED_ACTIVATION must not have unaudited_dependency_bundle_refs_and_hashes")

    if mode in ("UNAUDITED_AUTHORIZED_CANARY", "TRUST_ROOT_OR_SCHEMA_BOOTSTRAP"):
        if not eea.get("unaudited_dependency_bundle_refs_and_hashes"):
            errors.append(EC.EEA_MODE_BINDING_INVALID)
            details.append(f"{mode} requires unaudited_dependency_bundle_refs_and_hashes")

    # 检查 action_scopes 至少有一个正预算
    action_scopes = eea.get("action_scopes", [])
    has_positive_budget = False
    for scope in action_scopes:
        budget = scope.get("budget", {})
        for f in ALLOWANCE_FIELDS:
            budget_field = f"max_{f}" if f != "cost_microunits" else "max_cost_microunits"
            if budget.get(budget_field, 0) > 0:
                has_positive_budget = True
                break
        # also check max_tokens, max_cost_microunits
        if budget.get("max_tokens", 0) > 0 or budget.get("max_cost_microunits", 0) > 0:
            has_positive_budget = True

    if not has_positive_budget:
        errors.append(EC.EEA_ZERO_BUDGET)
        details.append("EEA must have at least one positive budget item")

    # 时间戳检查
    for ts_field in ("issued_at", "not_before", "expires_at"):
        ts = eea.get(ts_field, "")
        if not _check_canonical_utc(ts):
            errors.append(EC.TIME_NOT_CANONICAL_UTC)
            details.append(f"{ts_field} is not canonical UTC: {ts!r}")

    # authorization_hash 验证
    eea_hash_algo = eea.get("authorization_hash_algorithm", "")
    if eea_hash_algo != "sha256(RFC8785-JCS-object-with-authorization_hash-null)":
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected authorization_hash_algorithm: {eea_hash_algo}")

    # signature_domain 验证（对象层）
    eea_domain = eea.get("signature_domain", "")
    if eea_domain != "seven-external-execution-authorization/v1\0":
        errors.append(EC.SIGNATURE_DOMAIN_INVALID)
        details.append(
            f"signature_domain mismatch: expected "
            f"'seven-external-execution-authorization/v1\\x00', got {eea_domain!r}"
        )

    # 计算 hash 并验证
    obj_for_hash = dict(eea)
    obj_for_hash["authorization_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if eea.get("authorization_hash") != computed_hash:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"authorization_hash mismatch: expected {computed_hash}, "
            f"got {eea.get('authorization_hash')}"
        )

    if expected_eea_hash is not None and eea.get("authorization_hash") != expected_eea_hash:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"EEA hash does not match expected {expected_eea_hash}")

    # 签名 envelope
    sig_errors = verify_signature_envelope(
        eea.get("signature_envelope", {}),
        expected_domain="seven-external-execution-authorization/v1\0",
        signed_bytes_hash=eea.get("signed_bytes_hash", ""),
    )
    for code, detail in sig_errors:
        errors.append(code)
        details.append(detail)

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )


def verify_permit_does_not_escalate_parent(
    permit: dict[str, Any],
    eea: dict[str, Any],
) -> VerificationResult:
    """验证 LiveRunPermit 是 EEA 的不可扩权子集。

    检查：
    - permit 的 parent_authorization_id == eea.authorization_id
    - permit 的 parent_authorization_ref_and_hash.sha256 == eea.authorization_hash
    - permit 的每个 action_unit 的 budget <= 对应 parent action_scope 的 budget
    - permit 的 authorization_mode == eea.authorization_mode
    - permit 的时间窗在 EEA 时间窗内
    - permit 的 trust_root/roster/policy hash 与 EEA 一致
    """
    errors: list[VerificationErrorCode] = []
    details: list[str] = []

    # parent ID 匹配
    if permit.get("parent_authorization_id") != eea.get("authorization_id"):
        errors.append(EC.PERMIT_PARENT_HASH_MISMATCH)
        details.append(
            f"parent_authorization_id mismatch: "
            f"permit has {permit.get('parent_authorization_id')}, "
            f"EEA has {eea.get('authorization_id')}"
        )

    # parent hash 匹配
    parent_ref = permit.get("parent_authorization_ref_and_hash", {})
    if parent_ref.get("sha256") != eea.get("authorization_hash"):
        errors.append(EC.PERMIT_PARENT_HASH_MISMATCH)
        details.append(
            f"parent_authorization_ref hash mismatch: "
            f"permit has {parent_ref.get('sha256')}, "
            f"EEA has {eea.get('authorization_hash')}"
        )

    # mode 匹配
    if permit.get("authorization_mode") != eea.get("authorization_mode"):
        errors.append(EC.PERMIT_ESCALATES_PARENT)
        details.append(
            f"authorization_mode mismatch: "
            f"permit has {permit.get('authorization_mode')}, "
            f"EEA has {eea.get('authorization_mode')}"
        )

    # 时间窗检查
    permit_not_before = permit.get("not_before", "")
    permit_expires = permit.get("expires_at", "")
    eea_not_before = eea.get("not_before", "")
    eea_expires = eea.get("expires_at", "")
    if permit_not_before < eea_not_before:
        errors.append(EC.PERMIT_ESCALATES_PARENT)
        details.append(f"permit not_before {permit_not_before} < EEA not_before {eea_not_before}")
    if permit_expires > eea_expires:
        errors.append(EC.PERMIT_ESCALATES_PARENT)
        details.append(f"permit expires_at {permit_expires} > EEA expires_at {eea_expires}")

    # trust_root / roster / policy hash 一致
    for ref_field in (
        "actor_roster_ref_and_hash",
        "human_gate_policy_ref_and_hash",
        "signature_algorithm_registry_ref_and_hash",
        "revocation_policy_ref_and_hash",
    ):
        permit_ref = permit.get(ref_field, {}).get("sha256", "")
        eea_ref = eea.get(ref_field, {}).get("sha256", "")
        if permit_ref != eea_ref:
            errors.append(EC.PERMIT_ESCALATES_PARENT)
            details.append(f"{ref_field} hash mismatch: permit {permit_ref} vs EEA {eea_ref}")

    permit_trust = permit.get("externally_pinned_trust_root", {}).get("sha256", "")
    eea_trust = eea.get("externally_pinned_trust_root", {}).get("sha256", "")
    if permit_trust != eea_trust:
        errors.append(EC.PERMIT_ESCALATES_PARENT)
        details.append(f"trust_root hash mismatch: permit {permit_trust} vs EEA {eea_trust}")

    # action_unit budget <= parent action_scope budget
    eea_scopes: dict[str, dict[str, Any]] = {}
    for scope in eea.get("action_scopes", []):
        eea_scopes[scope.get("scope_id", "")] = scope

    for unit in permit.get("action_units", []):
        scope_id = unit.get("parent_action_scope_id", "")
        scope_hash = unit.get("parent_action_scope_hash", "")
        parent_scope = eea_scopes.get(scope_id)
        if parent_scope is None:
            errors.append(EC.PERMIT_ESCALATES_PARENT)
            details.append(f"action_unit references unknown scope {scope_id}")
            continue
        if scope_hash != parent_scope.get("scope_hash", ""):
            errors.append(EC.PERMIT_ESCALATES_PARENT)
            details.append(f"action_unit scope_hash mismatch for {scope_id}")
            continue

        parent_budget = parent_scope.get("budget", {})
        unit_budget = unit.get("unit_budget", {})
        for f in ALLOWANCE_FIELDS:
            budget_field = f"max_{f}" if f != "cost_microunits" else "max_cost_microunits"
            parent_val = parent_budget.get(budget_field, 0)
            unit_val = unit_budget.get(budget_field, 0)
            if unit_val > parent_val:
                errors.append(EC.PERMIT_ESCALATES_PARENT)
                details.append(
                    f"unit budget {budget_field}={unit_val} exceeds "
                    f"parent {parent_val} for scope {scope_id}"
                )

    # permit_hash 验证
    permit_hash_algo = permit.get("permit_hash_algorithm", "")
    if permit_hash_algo != "sha256(RFC8785-JCS-object-with-permit_hash-null)":
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected permit_hash_algorithm: {permit_hash_algo}")

    # signature_domain 验证（对象层）
    permit_domain = permit.get("signature_domain", "")
    if permit_domain != "seven-live-run-permit/v1\0":
        errors.append(EC.SIGNATURE_DOMAIN_INVALID)
        details.append(
            f"permit signature_domain mismatch: expected "
            f"'seven-live-run-permit/v1\\x00', got {permit_domain!r}"
        )

    obj_for_hash = dict(permit)
    obj_for_hash["permit_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if permit.get("permit_hash") != computed_hash:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"permit_hash mismatch: expected {computed_hash}, "
            f"got {permit.get('permit_hash')}"
        )

    # 签名 envelope
    sig_errors = verify_signature_envelope(
        permit.get("signature_envelope", {}),
        expected_domain="seven-live-run-permit/v1\0",
        signed_bytes_hash=permit.get("signed_bytes_hash", ""),
    )
    for code, detail in sig_errors:
        errors.append(code)
        details.append(detail)

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )


def verify_consumption_receipt(
    receipt: dict[str, Any],
    *,
    permit: dict[str, Any],
    previous_receipt: dict[str, Any] | None = None,
) -> VerificationResult:
    """验证 AuthorizationConsumptionReceipt。

    检查：
    - status 合法
    - RESERVED: actual=0, held>0, released=0, no terminal
    - CONSUMED: actual>0, held=0, terminal set, start observed
    - RELEASED_UNUSED: actual=0, held=0, released>0, proof_not_started
    - UNKNOWN_START_HELD: held>0, no terminal, start unknown
    - QUARANTINED: terminal set, recovery decision
    - fence_token 匹配
    - 额度守恒: initial = remaining + consumed + held
    - receipt_hash 正确
    - append-only: state_revision 递增
    """
    errors: list[VerificationErrorCode] = []
    details: list[str] = []

    status = receipt.get("status", "")
    if status not in CONSUMPTION_STATUSES:
        errors.append(EC.STATE_COMMAND_REJECTED)
        details.append(f"unknown consumption status: {status}")

    # fence_token 检查
    permit_ordinals = {
        u.get("consumption_ordinal"): u.get("fence_token")
        for u in permit.get("action_units", [])
    }
    ordinal = receipt.get("consumption_ordinal", -1)
    expected_fence = permit_ordinals.get(ordinal)
    if expected_fence is not None and receipt.get("fence_token") != expected_fence:
        errors.append(EC.STALE_FENCE)
        details.append(
            f"fence_token mismatch for ordinal {ordinal}: "
            f"receipt has {receipt.get('fence_token')}, "
            f"permit has {expected_fence}"
        )

    # reservation_backend 检查
    backend = receipt.get("reservation_backend", "")
    if backend not in (
        "DB_V2_OR_EQUIVALENT_TRANSACTIONAL_LEDGER",
        "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
    ):
        errors.append(EC.RESERVATION_BACKEND_INVALID)
        details.append(f"unknown reservation_backend: {backend}")

    # 状态相关检查
    actual = _allowance_from_dict(receipt.get("actual_side_effects", {}))
    held = _allowance_from_dict(receipt.get("held_allowance", {}))
    released = _allowance_from_dict(receipt.get("released_allowance", {}))
    remaining = _allowance_from_dict(receipt.get("remaining_allowance", {}))
    reserved = _allowance_from_dict(receipt.get("reserved_unit_budget", {}))

    if status == "RESERVED":
        if not _allowance_is_zero(actual):
            errors.append(EC.APPEND_ONLY_VIOLATION)
            details.append("RESERVED must have zero actual_side_effects")
        if _allowance_is_zero(held):
            errors.append(EC.ALLOWANCE_NOT_CONSERVED)
            details.append("RESERVED must have nonzero held_allowance")
        if not _allowance_is_zero(released):
            errors.append(EC.APPEND_ONLY_VIOLATION)
            details.append("RESERVED must have zero released_allowance")
        if receipt.get("terminal_at_if_any") is not None:
            errors.append(EC.APPEND_ONLY_VIOLATION)
            details.append("RESERVED must not have terminal_at")
        if receipt.get("external_start_observation") != "NOT_OBSERVED":
            errors.append(EC.STATE_COMMAND_REJECTED)
            details.append("RESERVED must have external_start_observation=NOT_OBSERVED")

    elif status == "CONSUMED":
        if _allowance_is_zero(actual):
            errors.append(EC.ALLOWANCE_NOT_CONSERVED)
            details.append("CONSUMED must have nonzero actual_side_effects")
        if not _allowance_is_zero(held):
            errors.append(EC.APPEND_ONLY_VIOLATION)
            details.append("CONSUMED must have zero held_allowance")
        if receipt.get("terminal_at_if_any") is None:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("CONSUMED must have terminal_at_if_any")
        if receipt.get("external_start_observation") != "CONFIRMED_ACCEPTED_OR_STARTED":
            errors.append(EC.STATE_COMMAND_REJECTED)
            details.append("CONSUMED must have CONFIRMED_ACCEPTED_OR_STARTED")
        if not receipt.get("start_observation_evidence_refs"):
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("CONSUMED must have start_observation_evidence_refs")

    elif status == "RELEASED_UNUSED":
        if not _allowance_is_zero(actual):
            errors.append(EC.APPEND_ONLY_VIOLATION)
            details.append("RELEASED_UNUSED must have zero actual_side_effects")
        if not _allowance_is_zero(held):
            errors.append(EC.APPEND_ONLY_VIOLATION)
            details.append("RELEASED_UNUSED must have zero held_allowance")
        if _allowance_is_zero(released):
            errors.append(EC.ALLOWANCE_NOT_CONSERVED)
            details.append("RELEASED_UNUSED must have nonzero released_allowance")
        if not receipt.get("proof_not_started_refs"):
            errors.append(EC.RELEASE_WITHOUT_PROOF)
            details.append("RELEASED_UNUSED requires proof_not_started_refs")
        if receipt.get("external_start_observation") != "PROVEN_NOT_STARTED":
            errors.append(EC.STATE_COMMAND_REJECTED)
            details.append("RELEASED_UNUSED must have PROVEN_NOT_STARTED")

    elif status == "UNKNOWN_START_HELD":
        if not _allowance_is_zero(actual):
            errors.append(EC.APPEND_ONLY_VIOLATION)
            details.append("UNKNOWN_START_HELD must have zero actual_side_effects")
        if _allowance_is_zero(held):
            errors.append(EC.ALLOWANCE_NOT_CONSERVED)
            details.append("UNKNOWN_START_HELD must have nonzero held_allowance")
        if receipt.get("terminal_at_if_any") is not None:
            errors.append(EC.UNKNOWN_START_MUST_HOLD)
            details.append("UNKNOWN_START_HELD must not have terminal_at")
        if receipt.get("external_start_observation") != "UNKNOWN":
            errors.append(EC.STATE_COMMAND_REJECTED)
            details.append("UNKNOWN_START_HELD must have external_start_observation=UNKNOWN")

    elif status == "QUARANTINED":
        if receipt.get("terminal_at_if_any") is None:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("QUARANTINED must have terminal_at_if_any")
        if not receipt.get("recovery_decision_ref_and_hash_if_any"):
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("QUARANTINED requires recovery_decision_ref_and_hash")

    # 额度守恒: reserved = actual + held + released + remaining
    # (对于 RESERVED: reserved = held + remaining, actual=0, released=0)
    # (对于 CONSUMED: reserved = actual + remaining, held=0, released=0)
    # (对于 RELEASED_UNUSED: reserved = released + remaining, actual=0, held=0)
    # 通用公式: reserved = actual + held + released + remaining
    computed_reserved = _allowance_add(
        _allowance_add(actual, held),
        _allowance_add(released, remaining),
    )
    for f in ALLOWANCE_FIELDS:
        if computed_reserved.get(f, 0) != reserved.get(f, 0):
            errors.append(EC.ALLOWANCE_NOT_CONSERVED)
            details.append(
                f"allowance not conserved for {f}: "
                f"actual({actual.get(f, 0)}) + held({held.get(f, 0)}) + "
                f"released({released.get(f, 0)}) + "
                f"remaining({remaining.get(f, 0)}) = "
                f"{computed_reserved.get(f, 0)} != "
                f"reserved({reserved.get(f, 0)})"
            )
            break

    # append-only: state_revision 递增
    if previous_receipt is not None:
        if receipt.get("state_revision", 0) <= previous_receipt.get("state_revision", 0):
            errors.append(EC.APPEND_ONLY_VIOLATION)
            details.append(
                f"state_revision must increase: "
                f"{receipt.get('state_revision')} <= "
                f"{previous_receipt.get('state_revision')}"
            )

    # receipt_hash 验证
    hash_algo = receipt.get("receipt_hash_algorithm", "")
    if hash_algo != "sha256(RFC8785-JCS-object-with-receipt_hash-null)":
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected receipt_hash_algorithm: {hash_algo}")

    obj_for_hash = dict(receipt)
    obj_for_hash["receipt_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if receipt.get("receipt_hash") != computed_hash:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"receipt_hash mismatch: expected {computed_hash}, "
            f"got {receipt.get('receipt_hash')}"
        )

    # 时间戳检查
    for ts_field in ("reserved_at", "status_recorded_at"):
        ts = receipt.get(ts_field, "")
        if not _check_canonical_utc(ts):
            errors.append(EC.TIME_NOT_CANONICAL_UTC)
            details.append(f"{ts_field} is not canonical UTC: {ts!r}")

    terminal = receipt.get("terminal_at_if_any")
    if terminal is not None and not _check_canonical_utc(terminal):
        errors.append(EC.TIME_NOT_CANONICAL_UTC)
        details.append(f"terminal_at_if_any is not canonical UTC: {terminal!r}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )


def verify_authorization_chain(
    *,
    eea: dict[str, Any],
    permit: dict[str, Any],
    receipt: dict[str, Any],
    previous_receipt: dict[str, Any] | None = None,
) -> VerificationResult:
    """验证完整授权链: EEA → LiveRunPermit → AuthorizationConsumptionReceipt。

    这是 GV0 SecurityContractVerifier 的主入口。
    1. 验证 EEA 结构和签名
    2. 验证 Permit 是 EEA 的不可扩权子集
    3. 验证 Receipt 的状态、额度和 fence
    """
    errors: list[VerificationErrorCode] = []
    details: list[str] = []

    # Step 1: EEA
    eea_result = verify_eea(eea)
    errors.extend(eea_result.error_codes)
    details.extend(eea_result.details)

    # Step 2: Permit 不扩权
    permit_result = verify_permit_does_not_escalate_parent(permit, eea)
    errors.extend(permit_result.error_codes)
    details.extend(permit_result.details)

    # Step 3: Receipt
    receipt_result = verify_consumption_receipt(
        receipt, permit=permit, previous_receipt=previous_receipt
    )
    errors.extend(receipt_result.error_codes)
    details.extend(receipt_result.details)

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )
