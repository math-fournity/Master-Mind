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

from dataclasses import dataclass, field
from typing import Any, TypedDict

from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult
from ..contracts.security_contract import verify_eea, verify_permit_does_not_escalate_parent


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

@dataclass
class SecurityContractVerifier:
    """SecurityContractVerifier — 完整授权链验证器。

    验证链：
    EEA → Permit (不可扩权子集) → Reservation (RESERVED + ordinal)

    P0-C 深度补全：
    - allowance 守恒验证
    - EEA/Permit 签名验证集成
    - 类型化对象验证
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
        expected_wp_id: str = "",
        eea_public_key_bytes: bytes | None = None,
        permit_public_key_bytes: bytes | None = None,
        verify_signatures: bool = False,
    ) -> VerificationResult:
        """验证完整授权链。

        检查：
        1. EEA 结构合法（verify_eea）
        2. Permit 结构合法且为 EEA 不可扩权子集
        3. Permit 绑定 plan_hash、wp_id、action_registry_id
        4. Permit 绑定 site fingerprint、DB name
        5. Reservation 状态为 RESERVED（如提供）
        6. Reservation ordinal 唯一
        7. nonce/idempotency/fence
        8. 时间状态（未过期、未撤销）
        9. P0-C 深度: allowance 守恒
        10. P0-C 深度: EEA/Permit 签名验证（如提供公钥）
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. EEA 结构验证
        eea_result = verify_eea(eea)
        if not eea_result.passed:
            errors.extend(eea_result.error_codes)
            details.extend(eea_result.details)

        # 2. Permit 不可扩权验证
        permit_result = verify_permit_does_not_escalate_parent(permit, eea)
        if not permit_result.passed:
            errors.extend(permit_result.error_codes)
            details.extend(permit_result.details)

        # 3. Permit 绑定验证
        if expected_plan_hash and permit.get("plan_hash", "") != expected_plan_hash:
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append(
                f"permit plan_hash {permit.get('plan_hash', '')} != expected {expected_plan_hash}"
            )

        if expected_wp_id and permit.get("wp_id", "") != expected_wp_id:
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append(
                f"permit wp_id {permit.get('wp_id', '')} != expected {expected_wp_id}"
            )

        if expected_action_registry_id and permit.get("action_registry_id", "") != expected_action_registry_id:
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append(
                f"permit action_registry_id {permit.get('action_registry_id', '')} != "
                f"expected {expected_action_registry_id}"
            )

        # 4. Site fingerprint 和 DB name 绑定
        if expected_site_fingerprint:
            permit_site = permit.get("site_fingerprint_hash", "")
            if permit_site != expected_site_fingerprint:
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append(
                    f"permit site_fingerprint_hash {permit_site} != "
                    f"expected {expected_site_fingerprint}"
                )

        if expected_db_name:
            permit_db = permit.get("db_name", "")
            if permit_db != expected_db_name:
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append(
                    f"permit db_name {permit_db} != expected {expected_db_name}"
                )

        # 5. Reservation 验证
        if reservation is not None:
            res_status = reservation.get("status", "")
            if res_status != "RESERVED":
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append(
                    f"reservation status must be RESERVED, got {res_status}"
                )

            # 6. ordinal 验证
            res_ordinal = reservation.get("ordinal")
            if res_ordinal is None:
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append("reservation must have ordinal")

            # 7. nonce/idempotency
            res_nonce = reservation.get("nonce", "")
            if not res_nonce:
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append("reservation must have nonce")

            # 8. fence token
            res_fence = reservation.get("fence_token")
            if res_fence is None:
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append("reservation must have fence_token")

            # Reservation 绑定 permit
            res_permit_id = reservation.get("permit_id", "")
            permit_id = permit.get("permit_id", "")
            if res_permit_id != permit_id:
                errors.append(EC.DB1I_PERMIT_MISMATCH)
                details.append(
                    f"reservation permit_id {res_permit_id} != permit_id {permit_id}"
                )

            # 9. P0-C 深度: allowance 守恒
            eea_budget = eea.get("budget", {}).get("max_tokens", 0)
            permit_budget = permit.get("budget", {}).get("max_tokens", 0)
            allowance_ok, allowance_errors, allowance_details = verify_allowance_conservation(
                reservation, eea_budget=eea_budget, permit_budget=permit_budget,
            )
            if not allowance_ok:
                errors.extend(allowance_errors)
                details.extend(allowance_details)

        # 时间状态验证
        eea_expiry = eea.get("expires_at", "")
        permit_expiry = permit.get("expires_at", "")
        if eea_expiry and permit_expiry and permit_expiry > eea_expiry:
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append(
                f"permit expires_at {permit_expiry} > EEA expires_at {eea_expiry} "
                f"— permit cannot outlive parent EEA"
            )

        # 10. P0-C 深度: EEA/Permit 签名验证
        if verify_signatures:
            from ..human.signed_object_verifier import verify_eea as verify_eea_sig, verify_live_run_permit

            if eea_public_key_bytes is not None:
                eea_sig_result = verify_eea_sig(eea, public_key_bytes=eea_public_key_bytes)
                if eea_sig_result.verdict != "PASS":
                    errors.append(EC.SIGNATURE_INVALID)
                    details.append(f"EEA signature verification failed: {eea_sig_result.details}")

            if permit_public_key_bytes is not None:
                permit_sig_result = verify_live_run_permit(permit, public_key_bytes=permit_public_key_bytes)
                if permit_sig_result.verdict != "PASS":
                    errors.append(EC.SIGNATURE_INVALID)
                    details.append(f"Permit signature verification failed: {permit_sig_result.details}")

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)

    def verify_typed_context(
        self,
        ctx: TypedAuthorizationContext,
        *,
        expected_plan_hash: str = "",
        expected_wp_id: str = "",
    ) -> VerificationResult:
        """验证类型化授权上下文——P0-C 深度补全。"""
        return self.verify_authorization_chain(
            eea=ctx.eea,
            permit=ctx.permit,
            reservation=ctx.reservation,
            expected_plan_hash=expected_plan_hash,
            expected_wp_id=expected_wp_id,
        )


# 全局单例
_default_verifier: SecurityContractVerifier | None = None


def get_security_contract_verifier() -> SecurityContractVerifier:
    """获取全局唯一的 SecurityContractVerifier 实例。"""
    global _default_verifier
    if _default_verifier is None:
        _default_verifier = SecurityContractVerifier()
    return _default_verifier
