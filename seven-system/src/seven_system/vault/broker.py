"""VaultBroker — 编排 deny-by-default 访问链。

VaultBroker 是 Vault 的可信控制面。它编排完整访问链：
  VaultAccessCapability → AccessDecision → ViewDerivation → AccessEvent

硬约束：
- deny-by-default：没有有效 capability + ALLOW decision → 不派生 view
- 不暴露 raw Vault 路径：worker 只得到 opaque view_id/sink_id + derived bytes
- READ_RAW_OBJECT 操作不存在
- 复用 GV0 CompletionArtifactStore CAS 核心，不另造第二套 store

SIDE_EFFECT_FREE：纯内存实现，不接触真实 D 盘或 DB。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    FORBIDDEN_OPERATIONS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from ..storage.artifact_store import CompletionArtifactStore, ArtifactRef
from .sensitivity import SensitivityRegistry, SensitivityLevel
from .access_capability import verify_vault_access_capability
from .access_decision import verify_access_decision
from .view_derivation import verify_view_derivation
from .access_event import AccessEventLedger, verify_access_event


@dataclass
class VaultBroker:
    """Vault 访问链编排器。

    持有：
    - sensitivity_registry: Vault 对象敏感度注册表
    - artifact_store: 复用的 GV0 CompletionArtifactStore（CAS 核心）
    - ledger: AccessEvent append-only ledger
    - seen_nonces: 全局 nonce 去重集
    - revoked_handles: 已撤销的 revocation_handle 集合
    """

    sensitivity_registry: SensitivityRegistry
    artifact_store: CompletionArtifactStore
    ledger: AccessEventLedger
    seen_nonces: set[str] = field(default_factory=set)
    revoked_handles: set[str] = field(default_factory=set)
    _raw_vault_paths: dict[str, str] = field(default_factory=dict, repr=False)

    def register_vault_object(
        self,
        object_id: str,
        content: bytes,
        sensitivity: str,
        *,
        source_artifact_ref: str = "",
        allowed_roles: list[str] | None = None,
    ) -> str:
        """注册一个 Vault 对象。

        将内容写入 CAS（复用 GV0 CompletionArtifactStore），
        记录敏感度到 registry，并保留 raw path（只在 broker 内部，不暴露给 worker）。
        返回 object_sha256。
        """
        if not SensitivityLevel.is_valid(sensitivity):
            raise _BrokerError(EC.VAULT_OBJECT_HASH_MISMATCH, f"invalid sensitivity: {sensitivity}")

        # 写入 CAS — 复用 GV0 核心
        ref = self.artifact_store.put_bytes(content)
        sha256 = ref.sha256

        # 注册敏感度
        from .sensitivity import VaultObjectRecord
        record = VaultObjectRecord(
            object_id=object_id,
            object_sha256=sha256,
            sensitivity=sensitivity,
            size_bytes=len(content),
            source_artifact_ref=source_artifact_ref,
            allowed_roles=allowed_roles or [],
        )
        self.sensitivity_registry.register(record)

        # raw path 只在 broker 内部，永远不暴露给 worker
        self._raw_vault_paths[object_id] = sha256

        return sha256

    def revoke_capability(self, revocation_handle: str) -> None:
        """撤销一个 capability。"""
        self.revoked_handles.add(revocation_handle)

    def process_access_request(
        self,
        *,
        capability: dict[str, Any],
        access_request_id: str,
        evaluation_time: str,
        derived_view_bytes: bytes | None = None,
        derivation_rule_ref: dict[str, str] | None = None,
        generator_ref: dict[str, str] | None = None,
        redaction_manifest_ref: dict[str, str] | None = None,
        view_policy_ref: dict[str, str] | None = None,
        sink_write_receipt_ref: dict[str, str] | None = None,
    ) -> tuple[VerificationResult, dict[str, Any] | None, dict[str, Any] | None, dict[str, Any] | None]:
        """处理一次完整的访问请求。

        执行 deny-by-default 访问链：
        1. 验证 VaultAccessCapability
        2. 检查撤销
        3. 检查 nonce replay
        4. 检查时间窗
        5. 检查敏感度约束
        6. 生成 AccessDecision (ALLOW 或 DENY)
        7. 如果 ALLOW 且有 derived_view_bytes：生成 ViewDerivation
        8. 生成 AccessEvent 并追加到 ledger

        返回 (overall_result, decision_dict, derivation_dict, event_dict)。
        如果任何步骤失败，后续对象为 None。
        """
        errors: list[EC] = []
        details: list[str] = []

        # ─── Step 1: 验证 capability ───
        cap_result = verify_vault_access_capability(capability)
        if not cap_result.passed:
            errors.extend(cap_result.error_codes)
            details.extend(cap_result.details)
            return self._deny_and_record(
                capability=capability,
                access_request_id=access_request_id,
                errors=errors,
                details=details,
                reason_codes=["CAPABILITY_INVALID"],
                evaluation_time=evaluation_time,
            )

        # ─── Step 2: 检查撤销 ───
        revocation_handle = capability.get("revocation", {}).get("revocation_handle", "")
        if revocation_handle in self.revoked_handles:
            errors.append(EC.VAULT_CAPABILITY_REVOKED)
            details.append(f"capability revoked: {revocation_handle}")
            return self._deny_and_record(
                capability=capability,
                access_request_id=access_request_id,
                errors=errors,
                details=details,
                reason_codes=["REVOKED"],
                evaluation_time=evaluation_time,
                revocation_status="REVOKED",
            )

        # ─── Step 3: nonce replay ───
        nonce = capability.get("nonce", "")
        if nonce in self.seen_nonces:
            errors.append(EC.VAULT_NONCE_REPLAY)
            details.append(f"nonce replay: {nonce}")
            return self._deny_and_record(
                capability=capability,
                access_request_id=access_request_id,
                errors=errors,
                details=details,
                reason_codes=["NONCE_REPLAY"],
                evaluation_time=evaluation_time,
            )

        # ─── Step 4: 时间窗 ───
        not_before = capability.get("not_before", "")
        expires_at = capability.get("expires_at", "")
        if evaluation_time < not_before:
            errors.append(EC.VAULT_CAPABILITY_NOT_YET_VALID)
            details.append(f"evaluation_time {evaluation_time} < not_before {not_before}")
            return self._deny_and_record(
                capability=capability,
                access_request_id=access_request_id,
                errors=errors,
                details=details,
                reason_codes=["OUTSIDE_TIME_WINDOW"],
                evaluation_time=evaluation_time,
            )
        if evaluation_time >= expires_at:
            errors.append(EC.VAULT_CAPABILITY_EXPIRED)
            details.append(f"evaluation_time {evaluation_time} >= expires_at {expires_at}")
            return self._deny_and_record(
                capability=capability,
                access_request_id=access_request_id,
                errors=errors,
                details=details,
                reason_codes=["OUTSIDE_TIME_WINDOW"],
                evaluation_time=evaluation_time,
            )

        # ─── Step 5: 敏感度约束 ───
        object_binding = capability.get("object_binding", {})
        object_id = object_binding.get("object_id", "")
        sensitivity = object_binding.get("sensitivity", "")
        principal = capability.get("principal", {})
        ptype = principal.get("principal_type", "")
        operation = capability.get("operation", "")

        # TARGET_SOLVER 只能访问 PUBLIC/RESTRICTED
        if ptype == "TARGET_SOLVER" and operation in ("READ_DERIVED_VIEW", "DERIVE_VIEW"):
            if not SensitivityLevel.solver_accessible(sensitivity):
                errors.append(EC.VAULT_OBJECT_HASH_MISMATCH)
                details.append(f"TARGET_SOLVER cannot access {sensitivity}")
                return self._deny_and_record(
                    capability=capability,
                    access_request_id=access_request_id,
                    errors=errors,
                    details=details,
                    reason_codes=["OBJECT_HASH_MISMATCH"],
                    evaluation_time=evaluation_time,
                )

        # 检查 registry 中对象的敏感度
        registry_record = self.sensitivity_registry.get(object_id)
        if registry_record is not None:
            if registry_record.sensitivity != sensitivity:
                errors.append(EC.VAULT_OBJECT_HASH_MISMATCH)
                details.append(f"sensitivity mismatch: capability says {sensitivity}, registry says {registry_record.sensitivity}")
                return self._deny_and_record(
                    capability=capability,
                    access_request_id=access_request_id,
                    errors=errors,
                    details=details,
                    reason_codes=["OBJECT_HASH_MISMATCH"],
                    evaluation_time=evaluation_time,
                )

        # ─── Step 6: 生成 AccessDecision (ALLOW) ───
        decision = self._build_decision(
            capability=capability,
            access_request_id=access_request_id,
            decision="ALLOW",
            reason_codes=["POLICY_ALLOW"],
            checks_pass=True,
            revocation_status="ACTIVE",
            evaluation_time=evaluation_time,
        )

        dec_result = verify_access_decision(
            decision,
            capability=capability,
            seen_nonces=self.seen_nonces,
            evaluation_time=evaluation_time,
        )
        if not dec_result.passed:
            errors.extend(dec_result.error_codes)
            details.extend(dec_result.details)
            return self._deny_and_record(
                capability=capability,
                access_request_id=access_request_id,
                errors=errors,
                details=details,
                reason_codes=["CAPABILITY_INVALID"],
                evaluation_time=evaluation_time,
            )

        # 记录 nonce
        self.seen_nonces.add(nonce)

        # ─── Step 7: 生成 ViewDerivation (如果 ALLOW 且有 derived bytes) ───
        derivation = None
        if derived_view_bytes is not None and operation in ("READ_DERIVED_VIEW", "DERIVE_VIEW"):
            derivation = self._build_derivation(
                capability=capability,
                decision=decision,
                derived_view_bytes=derived_view_bytes,
                derivation_rule_ref=derivation_rule_ref,
                generator_ref=generator_ref,
                redaction_manifest_ref=redaction_manifest_ref,
                view_policy_ref=view_policy_ref,
                sink_write_receipt_ref=sink_write_receipt_ref,
                evaluation_time=evaluation_time,
            )

            deriv_result = verify_view_derivation(
                derivation,
                capability=capability,
                access_decision=decision,
            )
            if not deriv_result.passed:
                # derivation 失败 → 记录 DERIVATION_FAILED event
                errors.extend(deriv_result.error_codes)
                details.extend(deriv_result.details)
                event = self._build_event(
                    capability=capability,
                    decision=decision,
                    derivation=None,
                    access_request_id=access_request_id,
                    result="DERIVATION_FAILED",
                    evaluation_time=evaluation_time,
                )
                event_result = self.ledger.append(event)
                return VerificationResult(
                    verdict="FAIL",
                    error_codes=errors + event_result.error_codes,
                    details=details + event_result.details,
                ), decision, None, event if event_result.passed else None

        # ─── Step 8: 生成 AccessEvent 并追加到 ledger ───
        event = self._build_event(
            capability=capability,
            decision=decision,
            derivation=derivation,
            access_request_id=access_request_id,
            result="ACCESS_GRANTED" if derivation is not None else "ACCESS_GRANTED",
            evaluation_time=evaluation_time,
            sink_write_receipt_ref=sink_write_receipt_ref,
        )

        event_result = self.ledger.append(event)
        if not event_result.passed:
            errors.extend(event_result.error_codes)
            details.extend(event_result.details)
            return VerificationResult(
                verdict="FAIL",
                error_codes=errors,
                details=details,
            ), decision, derivation, event

        return VerificationResult(verdict="PASS"), decision, derivation, event

    def _deny_and_record(
        self,
        *,
        capability: dict[str, Any],
        access_request_id: str,
        errors: list[EC],
        details: list[str],
        reason_codes: list[str],
        evaluation_time: str,
        revocation_status: str = "ACTIVE",
    ) -> tuple[VerificationResult, dict[str, Any] | None, dict[str, Any] | None, dict[str, Any] | None]:
        """生成 DENY decision + AccessEvent 并返回失败结果。"""
        decision = self._build_decision(
            capability=capability,
            access_request_id=access_request_id,
            decision="DENY",
            reason_codes=reason_codes,
            checks_pass=False,
            revocation_status=revocation_status,
            evaluation_time=evaluation_time,
        )

        event = self._build_event(
            capability=capability,
            decision=decision,
            derivation=None,
            access_request_id=access_request_id,
            result="ACCESS_DENIED",
            evaluation_time=evaluation_time,
        )

        # 尝试追加到 ledger（即使 DENY 也要记录）
        self.ledger.append(event)

        return VerificationResult(
            verdict="FAIL",
            error_codes=errors,
            details=details,
        ), decision, None, event

    def _build_decision(
        self,
        *,
        capability: dict[str, Any],
        access_request_id: str,
        decision: str,
        reason_codes: list[str],
        checks_pass: bool,
        revocation_status: str,
        evaluation_time: str,
    ) -> dict[str, Any]:
        """构建 AccessDecision dict。"""
        check_value = "PASS" if checks_pass else "FAIL"
        checks = {
            "capability_signature": check_value,
            "issuer_trust": check_value,
            "time_window": check_value,
            "principal": check_value,
            "operation": check_value,
            "object_hash": check_value,
            "view_hash": check_value,
            "sink": check_value,
            "nonce_replay": check_value,
            "access_policy": check_value,
        }

        revocation_handle = capability.get("revocation", {}).get("revocation_handle", "")
        registry_ref = capability.get("revocation", {}).get("registry_ref_and_hash", {})

        decision_dict = {
            "schema_id": "seven/access-decision",
            "schema_version": 1,
            "object_type": "AccessDecision",
            "decision_id": f"dec-{access_request_id}",
            "access_request_id": access_request_id,
            "capability_ref_and_hash": {
                "ref_id": capability.get("capability_id", ""),
                "sha256": capability.get("capability_hash", ""),
            },
            "principal": capability.get("principal", {}),
            "operation": capability.get("operation", ""),
            "object_binding": capability.get("object_binding", {}),
            "view_binding": capability.get("view_binding", {}),
            "sink_binding": capability.get("sink_binding", {}),
            "nonce": capability.get("nonce", ""),
            "access_policy_ref_and_hash": capability.get("access_policy_ref_and_hash", {}),
            "deny_by_default": True,
            "raw_vault_path_disclosed": False,
            "checks": checks,
            "revocation_check": {
                "revocation_handle": revocation_handle,
                "status": revocation_status,
                "registry_ref_and_hash": registry_ref,
                "checked_at": evaluation_time,
                "revocation_record_ref_and_hash": None if revocation_status == "ACTIVE" else {
                    "ref_id": f"rev-{revocation_handle}",
                    "sha256": "0" * 64,
                },
            },
            "decision": decision,
            "reason_codes": reason_codes,
            "evaluated_at": evaluation_time,
            "issuer": capability.get("issuer", {}),
            "externally_pinned_trust_root": capability.get("externally_pinned_trust_root", {}),
            "issuer_key_registry_ref_and_hash": capability.get("issuer_key_registry_ref_and_hash", {}),
            "canonicalizer_profile": "RFC8785_JCS_UTF8",
            "signature_domain": "seven-access-decision/v1\0",
            "signed_bytes_hash": capability.get("signed_bytes_hash", ""),
            "signature_envelope": capability.get("signature_envelope", {}),
            "decision_hash_algorithm": "sha256(RFC8785-JCS-object-with-decision_hash-null)",
            "decision_hash": None,
        }

        # 计算 decision_hash
        obj_for_hash = dict(decision_dict)
        obj_for_hash["decision_hash"] = None
        decision_dict["decision_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()

        return decision_dict

    def _build_derivation(
        self,
        *,
        capability: dict[str, Any],
        decision: dict[str, Any],
        derived_view_bytes: bytes,
        derivation_rule_ref: dict[str, str] | None,
        generator_ref: dict[str, str] | None,
        redaction_manifest_ref: dict[str, str] | None,
        view_policy_ref: dict[str, str] | None,
        sink_write_receipt_ref: dict[str, str] | None,
        evaluation_time: str,
    ) -> dict[str, Any]:
        """构建 ViewDerivation dict。"""
        # 计算 derived view hash
        view_sha256 = hashlib.sha256(derived_view_bytes).hexdigest()

        # 使用 capability 中的 view_binding 作为基础，但更新 view_sha256
        view_binding = dict(capability.get("view_binding", {}))
        view_binding["view_sha256"] = view_sha256

        _zero_hash = "0" * 64
        _ref = lambda d: d if d is not None else {"ref_id": "placeholder", "sha256": _zero_hash}

        derivation_dict = {
            "schema_id": "seven/view-derivation",
            "schema_version": 1,
            "object_type": "ViewDerivation",
            "derivation_id": f"deriv-{capability.get('capability_id', '')}",
            "capability_ref_and_hash": {
                "ref_id": capability.get("capability_id", ""),
                "sha256": capability.get("capability_hash", ""),
            },
            "access_decision_ref_and_hash": {
                "ref_id": decision.get("decision_id", ""),
                "sha256": decision.get("decision_hash", ""),
            },
            "principal": capability.get("principal", {}),
            "operation": capability.get("operation", ""),
            "source_object": capability.get("object_binding", {}),
            "derived_view": view_binding,
            "sink_binding": capability.get("sink_binding", {}),
            "view_policy_ref_and_hash": _ref(view_policy_ref),
            "derivation_rule_ref_and_hash": _ref(derivation_rule_ref),
            "generator_ref_and_hash": _ref(generator_ref),
            "redaction_manifest_ref_and_hash": _ref(redaction_manifest_ref),
            "sink_write_receipt_ref_and_hash": _ref(sink_write_receipt_ref),
            "revocation_check": {
                "revocation_handle": capability.get("revocation", {}).get("revocation_handle", ""),
                "status": "ACTIVE",
                "registry_ref_and_hash": capability.get("revocation", {}).get("registry_ref_and_hash", {}),
                "checked_at": evaluation_time,
                "revocation_record_ref_and_hash": None,
            },
            "nonce": capability.get("nonce", ""),
            "deny_by_default": True,
            "raw_vault_path_disclosed": False,
            "model_delivery": {
                "delivery_mode": "OPAQUE_HANDLE_AND_DERIVED_BYTES",
                "delivered_view_binding_source": "TOP_LEVEL_DERIVED_VIEW",
                "raw_vault_locator_exposed": False,
                "capability_token_exposed": False,
            },
            "derived_at": evaluation_time,
            "issuer": capability.get("issuer", {}),
            "externally_pinned_trust_root": capability.get("externally_pinned_trust_root", {}),
            "issuer_key_registry_ref_and_hash": capability.get("issuer_key_registry_ref_and_hash", {}),
            "canonicalizer_profile": "RFC8785_JCS_UTF8",
            "signature_domain": "seven-view-derivation/v1\0",
            "signed_bytes_hash": capability.get("signed_bytes_hash", ""),
            "signature_envelope": capability.get("signature_envelope", {}),
            "derivation_hash_algorithm": "sha256(RFC8785-JCS-object-with-derivation_hash-null)",
            "derivation_hash": None,
        }

        obj_for_hash = dict(derivation_dict)
        obj_for_hash["derivation_hash"] = None
        derivation_dict["derivation_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()

        return derivation_dict

    def _build_event(
        self,
        *,
        capability: dict[str, Any],
        decision: dict[str, Any],
        derivation: dict[str, Any] | None,
        access_request_id: str,
        result: str,
        evaluation_time: str,
        sink_write_receipt_ref: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """构建 AccessEvent dict。"""
        seq = self.ledger.next_sequence
        prev_hash = self.ledger.last_event_hash

        _zero_hash = "0" * 64
        _ref = lambda d: d if d is not None else {"ref_id": "placeholder", "sha256": _zero_hash}

        event_dict = {
            "schema_id": "seven/access-event",
            "schema_version": 1,
            "object_type": "AccessEvent",
            "event_id": f"evt-{self.ledger.ledger_id}-{seq}",
            "ledger_id": self.ledger.ledger_id,
            "sequence": seq,
            "previous_event_hash": prev_hash,
            "access_request_id": access_request_id,
            "capability_ref_and_hash": {
                "ref_id": capability.get("capability_id", ""),
                "sha256": capability.get("capability_hash", ""),
            },
            "decision_ref_and_hash": {
                "ref_id": decision.get("decision_id", ""),
                "sha256": decision.get("decision_hash", ""),
            },
            "view_derivation_ref_and_hash": (
                {
                    "ref_id": derivation.get("derivation_id", ""),
                    "sha256": derivation.get("derivation_hash", ""),
                }
                if derivation is not None
                else None
            ),
            "sink_write_receipt_ref_and_hash": (
                _ref(sink_write_receipt_ref) if derivation is not None else None
            ),
            "principal": capability.get("principal", {}),
            "operation": capability.get("operation", ""),
            "object_binding": capability.get("object_binding", {}),
            "view_binding": capability.get("view_binding", {}),
            "sink_binding": capability.get("sink_binding", {}),
            "nonce": capability.get("nonce", ""),
            "revocation_check": decision.get("revocation_check", {}),
            "deny_by_default": True,
            "raw_vault_path_disclosed": False,
            "result": result,
            "occurred_at": evaluation_time,
            "issuer": capability.get("issuer", {}),
            "externally_pinned_trust_root": capability.get("externally_pinned_trust_root", {}),
            "issuer_key_registry_ref_and_hash": capability.get("issuer_key_registry_ref_and_hash", {}),
            "canonicalizer_profile": "RFC8785_JCS_UTF8",
            "signature_domain": "seven-access-event/v1\0",
            "signed_bytes_hash": capability.get("signed_bytes_hash", ""),
            "signature_envelope": capability.get("signature_envelope", {}),
            "event_hash_algorithm": "sha256(RFC8785-JCS-object-with-event_hash-null)",
            "event_hash": None,
        }

        obj_for_hash = dict(event_dict)
        obj_for_hash["event_hash"] = None
        event_dict["event_hash"] = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()

        return event_dict

    def get_raw_vault_path(self, object_id: str) -> str | None:
        """获取 raw Vault path（只在 broker 内部使用，不暴露给 worker）。

        这个方法的存在是为了测试：测试可以验证 worker 永远拿不到这个值。
        """
        return self._raw_vault_paths.get(object_id)


class _BrokerError(Exception):
    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)
