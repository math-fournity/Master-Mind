"""Attempt / AttemptReceipt — accepted → started → completed 状态机与收据。

来自 docs/implementation/05-execution-ports-and-carriers.md：

submit 只有在获得 provider/CLI 可验证的接受物证后才能写 REQUEST_ACCEPTED；
GENERATION_STARTED 至少需要可归属本 attempt 的首个 generation/reasoning/output 事件
或 provider usage 正证据。两者未知时进入 UNKNOWN_START_QUARANTINED。

Attempt 状态机：
  CREATED → ACCEPTED → STARTED → COMPLETED
                     ↘ CANCELLED
                       ↘ TIMED_OUT
           ↘ CANCELLED
  STARTED → TERMINATED
  CREATED → ACCEPTED → UNKNOWN_START_QUARANTINED → TERMINATED / CANCELLED

非法状态转换 → ATTEMPT_ILLEGAL_STATE_TRANSITION
dispatch without accepted → ATTEMPT_UNKNOWN_START (reconcile: RECONCILE_UNKNOWN_START)
stale fence → ATTEMPT_STALE_FENCE
output to wrong sink → ATTEMPT_SENSITIVE_SINK

收据（AttemptReceipt）至少包含：
- attempt_id, role_job_id, role_type_id
- contract_hash, carrier_profile_hash, adapter_kind
- state (lifecycle), fence_token
- requested/effective model, effort, reasoning_mode
- output_artifact_hashes, output_sink_ref
- usage (tokens), terminal_reason
- receipt_hash
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ATTEMPT_STATES,
    ATTEMPT_TERMINAL_STATES,
    ATTEMPT_TRANSITIONS,
    ATTEMPT_OUTPUT_SINK_KINDS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_EXACT_ID_RE = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._:@+-]{0,254}[A-Za-z0-9])?$"
)

_RECEIPT_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-receipt_hash-null)"


class AttemptState:
    """Attempt 状态常量。"""

    CREATED = "CREATED"
    ACCEPTED = "ACCEPTED"
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
    TERMINATED = "TERMINATED"
    CANCELLED = "CANCELLED"
    TIMED_OUT = "TIMED_OUT"
    UNKNOWN_START_QUARANTINED = "UNKNOWN_START_QUARANTINED"

    @staticmethod
    def is_terminal(state: str) -> bool:
        return state in ATTEMPT_TERMINAL_STATES

    @staticmethod
    def is_valid(state: str) -> bool:
        return state in ATTEMPT_STATES

    @staticmethod
    def can_transition(from_state: str, to_state: str) -> bool:
        allowed = ATTEMPT_TRANSITIONS.get(from_state, frozenset())
        return to_state in allowed


@dataclass
class Attempt:
    """Attempt — 一次角色 job 的执行实例。

    可变对象：状态在生命周期中推进。
    """

    attempt_id: str
    role_job_id: str
    role_type_id: str
    contract_hash: str
    carrier_profile_hash: str
    adapter_kind: str
    fence_token: str
    state: str = AttemptState.CREATED
    created_at: str = ""
    accepted_at: str = ""
    started_at: str = ""
    completed_at: str = ""
    terminated_at: str = ""
    output_artifact_hashes: list[str] = field(default_factory=list)
    output_sink_ref: str = ""
    output_sink_kind: str = ""
    terminal_reason: str = ""

    def transition_to(self, new_state: str, timestamp: str = "") -> VerificationResult:
        """执行状态转换。返回 VerificationResult。"""
        errors: list[EC] = []
        details: list[str] = []

        if not AttemptState.is_valid(new_state):
            errors.append(EC.ATTEMPT_ILLEGAL_STATE_TRANSITION)
            details.append(f"unknown state: {new_state}")
        elif self.state == new_state:
            # 幂等：相同状态不做转换
            pass
        elif AttemptState.is_terminal(self.state):
            errors.append(EC.ATTEMPT_ALREADY_TERMINATED)
            details.append(f"attempt already in terminal state {self.state}")
        elif not AttemptState.can_transition(self.state, new_state):
            errors.append(EC.ATTEMPT_ILLEGAL_STATE_TRANSITION)
            details.append(
                f"illegal transition: {self.state} → {new_state} "
                f"(allowed: {ATTEMPT_TRANSITIONS.get(self.state, frozenset())})"
            )
        else:
            self.state = new_state
            if new_state == AttemptState.ACCEPTED:
                self.accepted_at = timestamp
            elif new_state == AttemptState.STARTED:
                self.started_at = timestamp
            elif new_state == AttemptState.COMPLETED:
                self.completed_at = timestamp
            elif new_state == AttemptState.TERMINATED:
                self.terminated_at = timestamp

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(
            verdict=verdict,
            error_codes=errors,
            details=details,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_id": self.attempt_id,
            "role_job_id": self.role_job_id,
            "role_type_id": self.role_type_id,
            "contract_hash": self.contract_hash,
            "carrier_profile_hash": self.carrier_profile_hash,
            "adapter_kind": self.adapter_kind,
            "fence_token": self.fence_token,
            "state": self.state,
            "created_at": self.created_at,
            "accepted_at": self.accepted_at,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "terminated_at": self.terminated_at,
            "output_artifact_hashes": list(self.output_artifact_hashes),
            "output_sink_ref": self.output_sink_ref,
            "output_sink_kind": self.output_sink_kind,
            "terminal_reason": self.terminal_reason,
        }


@dataclass(frozen=True)
class AttemptReceipt:
    """AttemptReceipt — attempt 的收据。

    记录 attempt 的生命周期事件、requested/effective 字段、
    输出 artifact hashes、usage 和 terminal reason。
    """

    receipt_id: str
    attempt_id: str
    role_job_id: str
    role_type_id: str
    contract_hash: str
    carrier_profile_hash: str
    adapter_kind: str
    state: str
    fence_token: str
    lifecycle_events: list[dict[str, str]]
    requested_model_uid: str
    effective_model_uid: str
    normalized_effort: str
    effort_observation: str
    reasoning_mode: str
    output_artifact_hashes: list[str]
    output_sink_ref: str
    output_sink_kind: str
    output_schema_validation_verdict: str
    usage: dict[str, int]
    usage_completeness: str
    terminal_reason: str
    failure_or_quarantine_state: str
    receipt_hash_algorithm: str
    receipt_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "receipt_id": self.receipt_id,
            "attempt_id": self.attempt_id,
            "role_job_id": self.role_job_id,
            "role_type_id": self.role_type_id,
            "contract_hash": self.contract_hash,
            "carrier_profile_hash": self.carrier_profile_hash,
            "adapter_kind": self.adapter_kind,
            "state": self.state,
            "fence_token": self.fence_token,
            "lifecycle_events": [dict(e) for e in self.lifecycle_events],
            "requested_model_uid": self.requested_model_uid,
            "effective_model_uid": self.effective_model_uid,
            "normalized_effort": self.normalized_effort,
            "effort_observation": self.effort_observation,
            "reasoning_mode": self.reasoning_mode,
            "output_artifact_hashes": list(self.output_artifact_hashes),
            "output_sink_ref": self.output_sink_ref,
            "output_sink_kind": self.output_sink_kind,
            "output_schema_validation_verdict": self.output_schema_validation_verdict,
            "usage": dict(self.usage),
            "usage_completeness": self.usage_completeness,
            "terminal_reason": self.terminal_reason,
            "failure_or_quarantine_state": self.failure_or_quarantine_state,
            "receipt_hash_algorithm": self.receipt_hash_algorithm,
            "receipt_hash": self.receipt_hash,
        }

    @property
    def is_terminal(self) -> bool:
        return AttemptState.is_terminal(self.state)

    @property
    def is_completed(self) -> bool:
        return self.state == AttemptState.COMPLETED


def build_attempt_receipt(
    *,
    attempt: Attempt,
    requested_model_uid: str = "",
    effective_model_uid: str = "",
    normalized_effort: str = "",
    effort_observation: str = "UNOBSERVABLE",
    reasoning_mode: str = "",
    output_schema_validation_verdict: str = "PASS",
    usage: dict[str, int] | None = None,
    usage_completeness: str = "COMPLETE",
    failure_or_quarantine_state: str = "",
) -> AttemptReceipt:
    """从 Attempt 构建 AttemptReceipt，自动计算 receipt_hash。"""
    # 构建生命周期事件
    lifecycle_events: list[dict[str, str]] = []
    if attempt.created_at:
        lifecycle_events.append({"state": AttemptState.CREATED, "timestamp": attempt.created_at})
    if attempt.accepted_at:
        lifecycle_events.append({"state": AttemptState.ACCEPTED, "timestamp": attempt.accepted_at})
    if attempt.started_at:
        lifecycle_events.append({"state": AttemptState.STARTED, "timestamp": attempt.started_at})
    if attempt.completed_at:
        lifecycle_events.append({"state": AttemptState.COMPLETED, "timestamp": attempt.completed_at})
    if attempt.terminated_at:
        lifecycle_events.append({"state": AttemptState.TERMINATED, "timestamp": attempt.terminated_at})
    # CANCELLED / TIMED_OUT / UNKNOWN_START 没有单独的 timestamp 字段
    if attempt.state in (AttemptState.CANCELLED, AttemptState.TIMED_OUT, AttemptState.UNKNOWN_START_QUARANTINED):
        lifecycle_events.append({"state": attempt.state, "timestamp": attempt.terminated_at or attempt.completed_at})

    receipt_id = f"receipt-{attempt.attempt_id}"

    obj = {
        "receipt_id": receipt_id,
        "attempt_id": attempt.attempt_id,
        "role_job_id": attempt.role_job_id,
        "role_type_id": attempt.role_type_id,
        "contract_hash": attempt.contract_hash,
        "carrier_profile_hash": attempt.carrier_profile_hash,
        "adapter_kind": attempt.adapter_kind,
        "state": attempt.state,
        "fence_token": attempt.fence_token,
        "lifecycle_events": lifecycle_events,
        "requested_model_uid": requested_model_uid,
        "effective_model_uid": effective_model_uid,
        "normalized_effort": normalized_effort,
        "effort_observation": effort_observation,
        "reasoning_mode": reasoning_mode,
        "output_artifact_hashes": list(attempt.output_artifact_hashes),
        "output_sink_ref": attempt.output_sink_ref,
        "output_sink_kind": attempt.output_sink_kind,
        "output_schema_validation_verdict": output_schema_validation_verdict,
        "usage": dict(usage) if usage else {},
        "usage_completeness": usage_completeness,
        "terminal_reason": attempt.terminal_reason,
        "failure_or_quarantine_state": failure_or_quarantine_state,
        "receipt_hash_algorithm": _RECEIPT_HASH_ALGORITHM,
        "receipt_hash": None,
    }
    receipt_hash = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

    return AttemptReceipt(
        receipt_id=receipt_id,
        attempt_id=attempt.attempt_id,
        role_job_id=attempt.role_job_id,
        role_type_id=attempt.role_type_id,
        contract_hash=attempt.contract_hash,
        carrier_profile_hash=attempt.carrier_profile_hash,
        adapter_kind=attempt.adapter_kind,
        state=attempt.state,
        fence_token=attempt.fence_token,
        lifecycle_events=lifecycle_events,
        requested_model_uid=requested_model_uid,
        effective_model_uid=effective_model_uid,
        normalized_effort=normalized_effort,
        effort_observation=effort_observation,
        reasoning_mode=reasoning_mode,
        output_artifact_hashes=list(attempt.output_artifact_hashes),
        output_sink_ref=attempt.output_sink_ref,
        output_sink_kind=attempt.output_sink_kind,
        output_schema_validation_verdict=output_schema_validation_verdict,
        usage=dict(usage) if usage else {},
        usage_completeness=usage_completeness,
        terminal_reason=attempt.terminal_reason,
        failure_or_quarantine_state=failure_or_quarantine_state,
        receipt_hash_algorithm=_RECEIPT_HASH_ALGORITHM,
        receipt_hash=receipt_hash,
    )


def verify_attempt_receipt(
    receipt: dict[str, Any] | AttemptReceipt,
    *,
    expected_receipt_hash: str | None = None,
) -> VerificationResult:
    """验证 AttemptReceipt 的 schema + semantic 合法性。

    检查：
    1. state 在合法枚举中
    2. output_sink_kind 在合法枚举中
    3. receipt_hash 正确
    4. 终态 → terminal_reason 非空
    5. COMPLETED → output_artifact_hashes 非空
    6. output_schema_validation_verdict
    """
    if isinstance(receipt, AttemptReceipt):
        receipt = receipt.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. state
    state = receipt.get("state", "")
    if state not in ATTEMPT_STATES:
        _err(EC.ATTEMPT_ILLEGAL_STATE_TRANSITION, f"invalid state: {state}")

    # 2. output_sink_kind
    sink_kind = receipt.get("output_sink_kind", "")
    if sink_kind and sink_kind not in ATTEMPT_OUTPUT_SINK_KINDS:
        _err(EC.ATTEMPT_SENSITIVE_SINK, f"invalid output_sink_kind: {sink_kind}")

    # 3. receipt_hash_algorithm
    if receipt.get("receipt_hash_algorithm") != _RECEIPT_HASH_ALGORITHM:
        _err(EC.ATTEMPT_RECEIPT_HASH_MISMATCH,
             f"unexpected receipt_hash_algorithm: {receipt.get('receipt_hash_algorithm')}")

    # 4. receipt_hash
    obj_for_hash = dict(receipt)
    obj_for_hash["receipt_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if receipt.get("receipt_hash") != computed_hash:
        _err(EC.ATTEMPT_RECEIPT_HASH_MISMATCH,
             f"receipt_hash mismatch: expected {computed_hash}, got {receipt.get('receipt_hash')}")

    if expected_receipt_hash is not None and receipt.get("receipt_hash") != expected_receipt_hash:
        _err(EC.ATTEMPT_RECEIPT_HASH_MISMATCH, "receipt_hash does not match expected")

    # 5. 终态 → terminal_reason
    if AttemptState.is_terminal(state):
        if not receipt.get("terminal_reason"):
            _err(EC.REQUIRED_FIELD_MISSING, f"terminal state {state} requires terminal_reason")

    # 6. COMPLETED → output_artifact_hashes 非空
    if state == AttemptState.COMPLETED:
        if not receipt.get("output_artifact_hashes"):
            _err(EC.REQUIRED_FIELD_MISSING, "COMPLETED state requires non-empty output_artifact_hashes")

    # 7. IDs
    for id_field in ("receipt_id", "attempt_id", "role_job_id", "role_type_id"):
        val = receipt.get(id_field, "")
        if not isinstance(val, str) or not _EXACT_ID_RE.match(val):
            _err(EC.REQUIRED_FIELD_MISSING, f"{id_field} is not valid: {val!r}")

    # 8. contract_hash / carrier_profile_hash
    for hash_field in ("contract_hash", "carrier_profile_hash"):
        val = receipt.get(hash_field, "")
        if not isinstance(val, str) or not _HASH_RE.match(val):
            _err(EC.OBJECT_HASH_MISMATCH, f"{hash_field} is not a valid hash: {val!r}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )
