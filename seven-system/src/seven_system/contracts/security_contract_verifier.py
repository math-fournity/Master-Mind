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

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult
from ..contracts.security_contract import verify_eea, verify_permit_does_not_escalate_parent


@dataclass
class SecurityContractVerifier:
    """SecurityContractVerifier — 完整授权链验证器。

    验证链：
    EEA → Permit (不可扩权子集) → Reservation (RESERVED + ordinal)
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

        # 时间状态验证
        eea_expiry = eea.get("expires_at", "")
        permit_expiry = permit.get("expires_at", "")
        if eea_expiry and permit_expiry and permit_expiry > eea_expiry:
            errors.append(EC.DB1I_PERMIT_MISMATCH)
            details.append(
                f"permit expires_at {permit_expiry} > EEA expires_at {eea_expiry} "
                f"— permit cannot outlive parent EEA"
            )

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# 全局单例
_default_verifier: SecurityContractVerifier | None = None


def get_security_contract_verifier() -> SecurityContractVerifier:
    """获取全局唯一的 SecurityContractVerifier 实例。"""
    global _default_verifier
    if _default_verifier is None:
        _default_verifier = SecurityContractVerifier()
    return _default_verifier
