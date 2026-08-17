"""SecurityContractVerifier — P0-C 补全：完整 EEA/Permit/Reservation 授权链验证。

文档 4.3 节"必须实现"第 3 条：
> SecurityContractVerifier 必须验证完整：
> - EEA真实签名、scope、budget、expiry、target
> - Permit真实签名且为EEA不可扩权子集
> - action registry ID、plan hash、site fingerprint、DB名
> - RESERVED receipt与精确ordinal
> - allowance守恒
> - nonce/idempotency/fence
> - 撤销和时间状态

本模块整合所有授权链验证，提供唯一的 SecurityContractVerifier 入口。

P0-C 深度补全：
- allowance 守恒验证（reserved = actual + held + released + remaining）
- EEA/Permit 签名验证集成（通过 SignedObjectVerifier）
- 类型化对象包装（TypedAuthorizationContext）
- DDL action catalog hash 跟踪

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, TypedDict

from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult
from ..hashing import canonical_json_bytes
from ..contracts.security_contract import verify_authorization_chain as verify_chain_semantics


# ─── 类型化对象 ─────────────────────────────────────────────────────────

class TypedEEA(TypedDict, total=False):
    """类型化 EEA 对象——P0-C 深度补全：不再接受任意 dict。"""
    schema_id: str
    authorization_mode: str
    unaudited_dependency_bundle_refs_and_hashes: list[dict[str, str]]
    action_scopes: list[dict[str, Any]]
    expires_at: str
    target_site_fingerprint: str
    target_db_name: str
    budget: dict[str, int]
    signature_envelope: dict[str, Any]


class TypedPermit(TypedDict, total=False):
    """类型化 Permit 对象。"""
    schema_id: str
    permit_id: str
    plan_hash: str
    wp_id: str
    action_registry_id: str
    site_fingerprint_hash: str
    db_name: str
    expires_at: str
    budget: dict[str, int]
    parent_eea_ref: str
    parent_eea_hash: str
    signature_envelope: dict[str, Any]


class TypedReservation(TypedDict, total=False):
    """类型化 Reservation 对象。"""
    permit_id: str
    status: str  # RESERVED / CONSUMED / RELEASED
    ordinal: int
    nonce: str
    fence_token: int
    reserved_amount: int
    actual_amount: int
    held_amount: int
    released_amount: int
    remaining_amount: int


@dataclass
class TypedAuthorizationContext:
    """类型化授权上下文——P0-C 深度补全。

    不再接受任意 dict 作为 Gate 或 Permit；
    只接受验证后对象/receipt 引用及其 hash。
    """
    eea: TypedEEA
    permit: TypedPermit
    reservation: TypedReservation | None = None
    eea_hash: str = ""
    permit_hash: str = ""
    reservation_hash: str = ""
    verified: bool = False


# ─── Allowance 守恒 ─────────────────────────────────────────────────────

def verify_allowance_conservation(
    reservation: dict[str, Any],
    *,
    eea_budget: int = 0,
    permit_budget: int = 0,
) -> tuple[bool, list[EC], list[str]]:
    """验证 allowance 守恒。

    文档要求：reserved = actual + held + released + remaining
    且 reserved <= permit_budget <= eea_budget
    """
    errors: list[EC] = []
    details: list[str] = []

    reserved = reservation.get("reserved_amount", 0)
    actual = reservation.get("actual_amount", 0)
    held = reservation.get("held_amount", 0)
    released = reservation.get("released_amount", 0)
    remaining = reservation.get("remaining_amount", 0)

    # 守恒检查：reserved = actual + held + released + remaining
    total = actual + held + released + remaining
    if total != reserved:
        errors.append(EC.DB1I_PERMIT_MISMATCH)
        details.append(
            f"allowance not conserved: reserved={reserved} != "
            f"actual({actual}) + held({held}) + released({released}) + remaining({remaining}) = {total}"
        )

    # reserved 不能超过 permit budget
    if permit_budget > 0 and reserved > permit_budget:
        errors.append(EC.DB1I_PERMIT_MISMATCH)
        details.append(f"reserved {reserved} > permit_budget {permit_budget}")

    # permit budget 不能超过 EEA budget
    if eea_budget > 0 and permit_budget > eea_budget:
        errors.append(EC.DB1I_PERMIT_MISMATCH)
        details.append(f"permit_budget {permit_budget} > eea_budget {eea_budget}")

    ok = len(errors) == 0
    return ok, errors, details


# ─── DDL Action Catalog Hash ────────────────────────────────────────────

@dataclass
class DDLActionRecord:
    """DDL action 记录——P0-C 深度补全。

    每个 DDL action 都要有：
    - pre-state catalog hash
    - action ID / ordinal
    - fence token
    - apply 结果
    - read-back catalog hash
    - terminal state
    - previous receipt hash
    """
    action_id: str
    ordinal: int
    fence_token: int
    pre_state_catalog_hash: str
    apply_result: str  # "SUCCESS" / "FAILURE" / "UNKNOWN"
    read_back_catalog_hash: str = ""
    terminal_state: str = ""  # "COMMITTED" / "ROLLED_BACK" / "PENDING"
    previous_receipt_hash: str = ""


@dataclass
class DDLActionReconciler:
    """DDL action reconcile——P0-C 深度补全。

    crash 前/后、重复 apply、旧 fence、部分索引、未知结果都必须进入 reconcile。
    """
    _actions: list[DDLActionRecord] = field(default_factory=list)
    _applied_ordinals: set[int] = field(default_factory=set)

    def record_action(self, action: DDLActionRecord) -> tuple[bool, list[EC], list[str]]:
        """记录一个 DDL action，检查重复 ordinal。"""
        errors: list[EC] = []
        details: list[str] = []

        if action.ordinal in self._applied_ordinals:
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append(f"duplicate ordinal: {action.ordinal}")
            return False, errors, details

        self._applied_ordinals.add(action.ordinal)
        self._actions.append(action)
        return True, [], []

    def reconcile(self) -> tuple[bool, list[EC], list[str]]:
        """reconcile 所有 actions——检查 crash 恢复。"""
        errors: list[EC] = []
        details: list[str] = []

        for action in self._actions:
            if action.apply_result == "UNKNOWN":
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append(f"action {action.action_id} has UNKNOWN result — needs reconcile")
            if action.terminal_state == "PENDING":
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append(f"action {action.action_id} is PENDING — needs reconcile")
            if action.pre_state_catalog_hash == action.read_back_catalog_hash and action.apply_result == "SUCCESS":
                # catalog 没变但 apply 成功——可能 no-op 或 hash 漂移
                details.append(f"action {action.action_id}: catalog unchanged after apply")

        ok = len(errors) == 0
        return ok, errors, details

    def get_actions(self) -> list[DDLActionRecord]:
        return list(self._actions)


# ─── SecurityContractVerifier ───────────────────────────────────────────

DB_SCHEMA_APPLY_ACTION_KIND = "DB_SCHEMA_APPLY"
DB_SCHEMA_APPLY_WP_ID = "WP-DB1I"

_SCHEMA_FILES = {
    "seven/external-execution-authorization": "external-execution-authorization.v1.schema.json",
    "seven/live-run-permit": "live-run-permit.v1.schema.json",
    "seven/authorization-consumption-receipt": "authorization-consumption-receipt.v1.schema.json",
}


def database_identity_hash(database_name: str) -> str:
    """Canonical target hash used by an EEA action scope."""
    return hashlib.sha256(
        canonical_json_bytes({"database_name": database_name})
    ).hexdigest()


def schema_bootstrap_target_binding_hash(
    *, plan_hash: str, site_fingerprint_hash: str, database_name: str
) -> str:
    """Bind a permit unit to exactly one bootstrap plan and logical site."""
    return hashlib.sha256(
        canonical_json_bytes(
            {
                "database_name": database_name,
                "plan_hash": plan_hash,
                "site_fingerprint_hash": site_fingerprint_hash,
            }
        )
    ).hexdigest()


def action_scope_hash(scope: dict[str, Any]) -> str:
    candidate = dict(scope)
    candidate["scope_hash"] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def _validate_security_schema(obj: dict[str, Any]) -> list[str]:
    schema_id = obj.get("schema_id", "")
    schema_file = _SCHEMA_FILES.get(schema_id)
    if schema_file is None:
        return [f"unknown security schema_id: {schema_id!r}"]
    schema_path = (
        Path(__file__).resolve().parents[3]
        / "docs"
        / "implementation"
        / schema_file
    )
    try:
        from jsonschema import Draft202012Validator, FormatChecker

        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [
            f"{'.'.join(map(str, error.absolute_path)) or '(root)'}: {error.message}"
            for error in sorted(
                validator.iter_errors(obj), key=lambda item: list(item.absolute_path)
            )
        ]
    except Exception as exc:
        return [f"cannot execute canonical Schema {schema_path}: {exc}"]


def _parse_utc(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def _binding_mismatch(
    errors: list[EC], details: list[str], label: str, actual: Any, expected: Any
) -> None:
    if actual != expected:
        errors.append(EC.DB1I_PERMIT_MISMATCH)
        details.append(f"{label} mismatch: expected {expected!r}, got {actual!r}")


@dataclass
class SecurityContractVerifier:
    """Fail-closed verifier for EEA → Permit → RESERVED receipt.

    The canonical entry point always executes all three JSON Schemas, all three
    Ed25519 verifications and exact action-unit binding. There is no structural-
    only mode and no optional reservation path.
    """

    def verify_authorization_chain(
        self,
        *,
        eea: dict[str, Any],
        permit: dict[str, Any],
        reservation: dict[str, Any] | None = None,
        expected_plan_hash: str = "",
        expected_site_fingerprint: str = "",
        expected_db_name: str = "",
        expected_action_registry_id: str = "",
        expected_action_registry_entry_ref_and_hash: dict[str, str] | None = None,
        expected_action_kind: str = "",
        expected_wp_id: str = "",
        evaluation_time: str = "",
        eea_public_key_bytes: bytes | None = None,
        permit_public_key_bytes: bytes | None = None,
        receipt_public_key_bytes: bytes | None = None,
        verify_signatures: bool = True,
    ) -> VerificationResult:
        errors: list[EC] = []
        details: list[str] = []

        if reservation is None:
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append("authorization consumption receipt is mandatory")
        if not verify_signatures:
            errors.append(EC.SIGNATURE_INVALID)
            details.append("canonical authorization verification cannot disable signatures")
        missing_keys = [
            name
            for name, value in (
                ("EEA", eea_public_key_bytes),
                ("Permit", permit_public_key_bytes),
                ("Receipt", receipt_public_key_bytes),
            )
            if value is None
        ]
        if missing_keys:
            errors.append(EC.SIGNATURE_INVALID)
            details.append(f"missing public keys for: {', '.join(missing_keys)}")
        if not evaluation_time:
            errors.append(EC.TIME_WINDOW_INVALID)
            details.append("trusted evaluation_time is mandatory")

        for label, obj in (("EEA", eea), ("Permit", permit)):
            schema_errors = _validate_security_schema(obj)
            if schema_errors:
                errors.append(EC.SCHEMA_VALIDATION_FAILED)
                details.extend(f"{label} schema: {item}" for item in schema_errors[:20])
        if reservation is not None:
            schema_errors = _validate_security_schema(reservation)
            if schema_errors:
                errors.append(EC.SCHEMA_VALIDATION_FAILED)
                details.extend(f"Receipt schema: {item}" for item in schema_errors[:20])

        if reservation is not None:
            semantic = verify_chain_semantics(
                eea=eea, permit=permit, receipt=reservation
            )
            errors.extend(semantic.error_codes)
            details.extend(semantic.details)

        if not missing_keys and verify_signatures:
            from ..human.signed_object_verifier import (
                verify_authorization_consumption_receipt,
                verify_eea as verify_eea_signature,
                verify_live_run_permit,
            )

            signature_results = [
                ("EEA", verify_eea_signature(eea, public_key_bytes=eea_public_key_bytes or b"")),
                ("Permit", verify_live_run_permit(permit, public_key_bytes=permit_public_key_bytes or b"")),
            ]
            if reservation is not None:
                signature_results.append(
                    (
                        "Receipt",
                        verify_authorization_consumption_receipt(
                            reservation,
                            public_key_bytes=receipt_public_key_bytes or b"",
                        ),
                    )
                )
            for label, result in signature_results:
                if result.verdict != "PASS":
                    errors.append(EC.SIGNATURE_INVALID)
                    details.append(f"{label} signature verification failed: {result.details}")

        evaluation = _parse_utc(evaluation_time)
        for label, obj in (("EEA", eea), ("Permit", permit)):
            issued = _parse_utc(str(obj.get("issued_at", "")))
            not_before = _parse_utc(str(obj.get("not_before", "")))
            expires = _parse_utc(str(obj.get("expires_at", "")))
            if None in (issued, not_before, expires):
                errors.append(EC.TIME_NOT_CANONICAL_UTC)
                details.append(f"{label} contains an invalid UTC time")
            elif not (issued <= not_before < expires):
                errors.append(EC.TIME_WINDOW_INVALID)
                details.append(f"{label} must satisfy issued_at <= not_before < expires_at")
            if evaluation is not None and not_before is not None and expires is not None:
                if not (not_before <= evaluation < expires):
                    errors.append(EC.TIME_WINDOW_INVALID)
                    details.append(f"{label} is not valid at evaluation_time")

        scope_ids: set[str] = set()
        scope_hashes: set[str] = set()
        for scope in eea.get("action_scopes", []):
            scope_id = scope.get("scope_id", "")
            scope_hash_value = scope.get("scope_hash", "")
            if scope_id in scope_ids or scope_hash_value in scope_hashes:
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append("EEA action scope IDs and hashes must be unique")
            scope_ids.add(scope_id)
            scope_hashes.add(scope_hash_value)
            _binding_mismatch(
                errors,
                details,
                f"scope {scope_id} hash",
                scope_hash_value,
                action_scope_hash(scope),
            )

        ordinals = [unit.get("consumption_ordinal") for unit in permit.get("action_units", [])]
        if len(ordinals) != len(set(ordinals)):
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append("permit consumption ordinals must be unique")

        expected_wp = expected_wp_id or DB_SCHEMA_APPLY_WP_ID
        expected_kind = expected_action_kind or DB_SCHEMA_APPLY_ACTION_KIND
        _binding_mismatch(errors, details, "permit wp_id", permit.get("wp_id"), expected_wp)
        if expected_wp not in eea.get("subject_work_package_ids", []):
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append(f"EEA does not authorize work package {expected_wp}")

        receipt_ordinal = reservation.get("consumption_ordinal") if reservation else None
        matching_units = [
            unit
            for unit in permit.get("action_units", [])
            if unit.get("consumption_ordinal") == receipt_ordinal
        ]
        if len(matching_units) != 1:
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append("receipt ordinal must select exactly one permit action unit")
            unit: dict[str, Any] = {}
        else:
            unit = matching_units[0]

        if unit:
            _binding_mismatch(errors, details, "action kind", unit.get("action_kind"), expected_kind)
            if expected_plan_hash:
                _binding_mismatch(errors, details, "plan input hash", unit.get("input_hash"), expected_plan_hash)
            if expected_site_fingerprint and expected_db_name:
                expected_target = schema_bootstrap_target_binding_hash(
                    plan_hash=expected_plan_hash,
                    site_fingerprint_hash=expected_site_fingerprint,
                    database_name=expected_db_name,
                )
                _binding_mismatch(
                    errors, details, "target binding", unit.get("target_binding_hash"), expected_target
                )
            if expected_action_registry_entry_ref_and_hash is not None:
                _binding_mismatch(
                    errors,
                    details,
                    "action registry entry",
                    unit.get("authorization_action_registry_entry_ref_and_hash"),
                    expected_action_registry_entry_ref_and_hash,
                )

            scopes = [
                scope
                for scope in eea.get("action_scopes", [])
                if scope.get("scope_id") == unit.get("parent_action_scope_id")
                and scope.get("scope_hash") == unit.get("parent_action_scope_hash")
            ]
            if len(scopes) != 1:
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append("permit unit must match exactly one EEA action scope")
            else:
                scope = scopes[0]
                _binding_mismatch(errors, details, "scope action kind", scope.get("action_kind"), expected_kind)
                if expected_site_fingerprint:
                    _binding_mismatch(
                        errors,
                        details,
                        "scope target site",
                        scope.get("target_site_hash_if_any"),
                        expected_site_fingerprint,
                    )
                if expected_db_name:
                    _binding_mismatch(
                        errors,
                        details,
                        "scope database identity",
                        scope.get("target_database_identity_hash_if_any"),
                        database_identity_hash(expected_db_name),
                    )
                _binding_mismatch(
                    errors,
                    details,
                    "scope/unit action registry entry",
                    unit.get("authorization_action_registry_entry_ref_and_hash"),
                    scope.get("authorization_action_registry_entry_ref_and_hash"),
                )

        if expected_action_registry_id:
            registry = eea.get("authorization_action_registry_ref_and_hash", {})
            _binding_mismatch(errors, details, "action registry ref", registry.get("ref"), expected_action_registry_id)

        if reservation is not None and unit:
            exact_fields = (
                "parent_action_scope_id",
                "parent_action_scope_hash",
                "action_kind",
                "authorization_action_registry_entry_ref_and_hash",
                "job_id",
                "attempt_id",
                "input_hash",
                "carrier_profile_or_solver_contract_hash_if_any",
                "target_binding_hash",
                "required_output_sink_and_acl_hash_if_any",
                "idempotency_key",
            )
            for field_name in exact_fields:
                _binding_mismatch(
                    errors,
                    details,
                    f"receipt {field_name}",
                    reservation.get(field_name),
                    unit.get(field_name),
                )
            _binding_mismatch(errors, details, "receipt status", reservation.get("status"), "RESERVED")
            _binding_mismatch(
                errors,
                details,
                "receipt reservation backend",
                reservation.get("reservation_backend"),
                permit.get("required_reservation_backend"),
            )
            _binding_mismatch(
                errors,
                details,
                "receipt parent authorization id",
                reservation.get("parent_authorization_id"),
                eea.get("authorization_id"),
            )
            _binding_mismatch(
                errors,
                details,
                "receipt parent authorization hash",
                reservation.get("parent_authorization_ref_and_hash", {}).get("sha256"),
                eea.get("authorization_hash"),
            )
            _binding_mismatch(
                errors,
                details,
                "receipt permit hash",
                reservation.get("permit_ref_and_hash", {}).get("sha256"),
                permit.get("permit_hash"),
            )

        return VerificationResult(
            verdict="PASS" if not errors else "FAIL",
            error_codes=errors,
            details=details,
        )

    def verify_typed_context(
        self,
        ctx: TypedAuthorizationContext,
        **kwargs: Any,
    ) -> VerificationResult:
        return self.verify_authorization_chain(
            eea=ctx.eea,
            permit=ctx.permit,
            reservation=ctx.reservation,
            **kwargs,
        )


# 全局单例
_default_verifier: SecurityContractVerifier | None = None


def get_security_contract_verifier() -> SecurityContractVerifier:
    """获取全局唯一的 SecurityContractVerifier 实例。"""
    global _default_verifier
    if _default_verifier is None:
        _default_verifier = SecurityContractVerifier()
    return _default_verifier
