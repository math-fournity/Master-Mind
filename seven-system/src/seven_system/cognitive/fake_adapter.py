"""FakeModelRoleAdapter — side-effect-free 测试适配器。

来自 docs/implementation/05-execution-ports-and-carriers.md：
"fake只证明公共状态机，stub只证明精确命令/事件协议，live canary才可能证明
本机+账号+provider能力；三者不得互相冒充。"

FakeModelRoleAdapter 实现 ModelRolePort 协议：
- dispatch：CREATED → ACCEPTED → STARTED → COMPLETED，确定性输出
- reattach：重新获取已有 attempt 的 receipt
- cancel：CANCELLED 终态
- get_receipt：获取当前 receipt

确定性保证：
- 相同 input_view_bytes + carrier_profile_hash → 相同 output
- output = sha256(canonical_json(input + profile_hash + role_type_id))
- 不调用任何外部 CLI / DB / D-volume
- 纯内存实现

SIDE_EFFECT_FREE：无任何副作用。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ATTEMPT_OUTPUT_SINK_KINDS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from .model_role_port import DispatchRequest, DispatchResult, ModelRolePort
from .attempt import (
    Attempt,
    AttemptReceipt,
    AttemptState,
    build_attempt_receipt,
)
from .role_execution_contract import verify_role_execution_contract
from .role_registry import RoleRegistry, ROLE_REGISTRY_FROZEN_V1


@dataclass
class FakeModelRoleAdapter:
    """FakeModelRoleAdapter — side-effect-free 测试适配器。

    实现 ModelRolePort 协议。纯内存，无副作用。

    可配置行为：
    - registry：用于验证 contract 中的 role_type_id
    - force_timeout：模拟超时（dispatch 后直接 TIMED_OUT）
    - force_unknown_start：模拟未知启动（ACCEPTED 后不 STARTED，进入 UNKNOWN_START_QUARANTINED）
    - force_wrong_sink：模拟敏感 sink 违规（output 写入错误 sink）
    - delay_started：模拟 dispatch 时跳过 STARTED（用于 unknown-start 测试）
    """

    registry: RoleRegistry = field(default_factory=lambda: ROLE_REGISTRY_FROZEN_V1)
    force_timeout: bool = False
    force_unknown_start: bool = False
    force_wrong_sink: bool = False
    force_skip_accepted: bool = False  # 跳过 ACCEPTED，直接 STARTED（unknown-start）
    _attempts: dict[str, Attempt] = field(default_factory=dict, repr=False)
    _receipts: dict[str, AttemptReceipt] = field(default_factory=dict, repr=False)
    _outputs: dict[str, bytes] = field(default_factory=dict, repr=False)

    # ─── ModelRolePort 协议实现 ───────────────────────────────────────

    def dispatch(self, request: DispatchRequest) -> DispatchResult:
        """提交角色 job。

        状态机：CREATED → ACCEPTED → STARTED → COMPLETED
        确定性输出：sha256(canonical_json(input + profile_hash + role_type_id))
        """
        # 验证 contract
        contract_result = verify_role_execution_contract(
            request.contract,
            registry=self.registry,
        )
        if not contract_result.passed:
            # contract 验证失败 → 创建 attempt 但不 accepted
            attempt = Attempt(
                attempt_id=f"attempt-{request.contract.role_job_id}",
                role_job_id=request.contract.role_job_id,
                role_type_id=request.contract.role_type_id,
                contract_hash=request.contract.contract_hash,
                carrier_profile_hash=request.contract.carrier_profile_ref_and_hash.get("sha256", ""),
                adapter_kind=request.contract.adapter_kind,
                fence_token=request.fence_token,
                state=AttemptState.CREATED,
                created_at="2026-08-14T12:00:00Z",
            )
            receipt = build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="CONTRACT_INVALID",
                output_schema_validation_verdict="FAIL",
            )
            self._attempts[attempt.attempt_id] = attempt
            self._receipts[attempt.attempt_id] = receipt
            return DispatchResult(attempt=attempt, receipt=receipt, accepted=False)

        attempt_id = f"attempt-{request.contract.role_job_id}"
        timestamp = "2026-08-14T12:00:00Z"

        attempt = Attempt(
            attempt_id=attempt_id,
            role_job_id=request.contract.role_job_id,
            role_type_id=request.contract.role_type_id,
            contract_hash=request.contract.contract_hash,
            carrier_profile_hash=request.contract.carrier_profile_ref_and_hash.get("sha256", ""),
            adapter_kind=request.contract.adapter_kind,
            fence_token=request.fence_token,
            state=AttemptState.CREATED,
            created_at=timestamp,
        )

        # ─── force_skip_accepted: 跳过 ACCEPTED 直接 STARTED ───
        if self.force_skip_accepted:
            # 非法：CREATED → STARTED（跳过 ACCEPTED）
            attempt.state = AttemptState.STARTED
            attempt.started_at = timestamp
            receipt = build_attempt_receipt(
                attempt=attempt,
                requested_model_uid="fake-model",
                effective_model_uid="fake-model",
                normalized_effort="high",
                effort_observation="UNOBSERVABLE",
                reasoning_mode="not_configurable",
                failure_or_quarantine_state="UNKNOWN_START",
            )
            self._attempts[attempt_id] = attempt
            self._receipts[attempt_id] = receipt
            return DispatchResult(attempt=attempt, receipt=receipt, accepted=False)

        # ─── 正常路径：CREATED → ACCEPTED ───
        result = attempt.transition_to(AttemptState.ACCEPTED, timestamp)
        if not result.passed:
            receipt = build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="STATE_TRANSITION_FAILED",
            )
            self._attempts[attempt_id] = attempt
            self._receipts[attempt_id] = receipt
            return DispatchResult(attempt=attempt, receipt=receipt, accepted=False)

        # ─── force_unknown_start: ACCEPTED 后进入 UNKNOWN_START_QUARANTINED ───
        if self.force_unknown_start:
            attempt.transition_to(AttemptState.UNKNOWN_START_QUARANTINED, timestamp)
            attempt.terminal_reason = "UNKNOWN_START_QUARANTINED"
            receipt = build_attempt_receipt(
                attempt=attempt,
                requested_model_uid="fake-model",
                effective_model_uid="UNOBSERVABLE",
                failure_or_quarantine_state="UNKNOWN_START_QUARANTINED",
            )
            self._attempts[attempt_id] = attempt
            self._receipts[attempt_id] = receipt
            return DispatchResult(attempt=attempt, receipt=receipt, accepted=True)

        # ─── force_timeout: ACCEPTED 后直接 TIMED_OUT ───
        if self.force_timeout:
            attempt.transition_to(AttemptState.TIMED_OUT, timestamp)
            attempt.terminal_reason = "TIMEOUT"
            receipt = build_attempt_receipt(
                attempt=attempt,
                requested_model_uid="fake-model",
                effective_model_uid="fake-model",
                failure_or_quarantine_state="TIMED_OUT",
            )
            self._attempts[attempt_id] = attempt
            self._receipts[attempt_id] = receipt
            return DispatchResult(attempt=attempt, receipt=receipt, accepted=True)

        # ─── 正常路径：ACCEPTED → STARTED ───
        result = attempt.transition_to(AttemptState.STARTED, timestamp)
        if not result.passed:
            receipt = build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="STATE_TRANSITION_FAILED",
            )
            self._attempts[attempt_id] = attempt
            self._receipts[attempt_id] = receipt
            return DispatchResult(attempt=attempt, receipt=receipt, accepted=True)

        # ─── 生成确定性输出 ───
        output_bytes = self._generate_output(request)

        # 计算 output artifact hash
        output_hash = hashlib.sha256(output_bytes).hexdigest()
        attempt.output_artifact_hashes = [output_hash]

        # 设置 output sink
        if self.force_wrong_sink:
            # 敏感 sink 违规：output 写入 EPHEMERAL_MODEL_OUTPUT 而非 RESTRICTED_VAULT
            attempt.output_sink_ref = "wrong-sink-001"
            attempt.output_sink_kind = "EPHEMERAL_MODEL_OUTPUT"
        else:
            attempt.output_sink_ref = request.sink_id
            attempt.output_sink_kind = "RESTRICTED_VAULT"

        # ─── 正常路径：STARTED → COMPLETED ───
        result = attempt.transition_to(AttemptState.COMPLETED, timestamp)
        if not result.passed:
            receipt = build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="STATE_TRANSITION_FAILED",
            )
            self._attempts[attempt_id] = attempt
            self._receipts[attempt_id] = receipt
            return DispatchResult(attempt=attempt, receipt=receipt, accepted=True)

        attempt.terminal_reason = "COMPLETED"
        self._outputs[attempt_id] = output_bytes

        # ─── 构建 receipt ───
        receipt = build_attempt_receipt(
            attempt=attempt,
            requested_model_uid="fake-model",
            effective_model_uid="fake-model",
            normalized_effort="high",
            effort_observation="UNOBSERVABLE",
            reasoning_mode="not_configurable",
            usage={"input_tokens": 100, "output_tokens": 50},
            usage_completeness="COMPLETE",
        )

        self._attempts[attempt_id] = attempt
        self._receipts[attempt_id] = receipt
        return DispatchResult(attempt=attempt, receipt=receipt, accepted=True)

    def reattach(self, attempt_id: str, fence_token: str) -> AttemptReceipt:
        """重新附加到已有 attempt。"""
        attempt = self._attempts.get(attempt_id)
        if attempt is None:
            # 创建一个不存在的 attempt receipt
            fake_attempt = Attempt(
                attempt_id=attempt_id,
                role_job_id="unknown",
                role_type_id="unknown",
                contract_hash="0" * 64,
                carrier_profile_hash="0" * 64,
                adapter_kind="FAKE",
                fence_token=fence_token,
                state=AttemptState.CREATED,
            )
            return build_attempt_receipt(
                attempt=fake_attempt,
                failure_or_quarantine_state="ATTEMPT_NOT_FOUND",
            )

        # fence token 验证
        if attempt.fence_token != fence_token:
            return build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="FENCE_TOKEN_MISMATCH",
            )

        # 已取消的 attempt 不能 reattach
        if attempt.state == AttemptState.CANCELLED:
            return build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="ATTEMPT_CANCELLED",
            )

        return self._receipts.get(attempt_id, build_attempt_receipt(attempt=attempt))

    def cancel(self, attempt_id: str, fence_token: str) -> AttemptReceipt:
        """取消 attempt。"""
        attempt = self._attempts.get(attempt_id)
        if attempt is None:
            fake_attempt = Attempt(
                attempt_id=attempt_id,
                role_job_id="unknown",
                role_type_id="unknown",
                contract_hash="0" * 64,
                carrier_profile_hash="0" * 64,
                adapter_kind="FAKE",
                fence_token=fence_token,
                state=AttemptState.CREATED,
            )
            return build_attempt_receipt(
                attempt=fake_attempt,
                failure_or_quarantine_state="ATTEMPT_NOT_FOUND",
            )

        # fence token 验证
        if attempt.fence_token != fence_token:
            return build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="FENCE_TOKEN_MISMATCH",
            )

        # 已终态不能 cancel
        if AttemptState.is_terminal(attempt.state):
            return build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="ALREADY_TERMINATED",
            )

        # 执行 cancel
        timestamp = "2026-08-14T12:00:01Z"
        attempt.transition_to(AttemptState.CANCELLED, timestamp)
        attempt.terminal_reason = "CANCELLED"

        receipt = build_attempt_receipt(
            attempt=attempt,
            requested_model_uid="fake-model",
            effective_model_uid="fake-model",
            failure_or_quarantine_state="CANCELLED",
        )
        self._receipts[attempt_id] = receipt
        return receipt

    def get_receipt(self, attempt_id: str) -> AttemptReceipt:
        """获取 attempt 的当前 receipt。"""
        attempt = self._attempts.get(attempt_id)
        if attempt is None:
            fake_attempt = Attempt(
                attempt_id=attempt_id,
                role_job_id="unknown",
                role_type_id="unknown",
                contract_hash="0" * 64,
                carrier_profile_hash="0" * 64,
                adapter_kind="FAKE",
                fence_token="",
                state=AttemptState.CREATED,
            )
            return build_attempt_receipt(
                attempt=fake_attempt,
                failure_or_quarantine_state="ATTEMPT_NOT_FOUND",
            )
        return self._receipts.get(attempt_id, build_attempt_receipt(attempt=attempt))

    # ─── 内部方法 ─────────────────────────────────────────────────────

    def _generate_output(self, request: DispatchRequest) -> bytes:
        """生成确定性输出。

        output = sha256(canonical_json({
            "input_view_bytes_hash": sha256(input_view_bytes),
            "carrier_profile_hash": carrier_profile_hash,
            "role_type_id": role_type_id,
        }))

        相同 input + profile → 相同 output（确定性保证）
        """
        input_hash = hashlib.sha256(request.input_view_bytes).hexdigest()
        output_payload = {
            "input_view_bytes_hash": input_hash,
            "carrier_profile_hash": request.contract.carrier_profile_ref_and_hash.get("sha256", ""),
            "role_type_id": request.contract.role_type_id,
        }
        output_hash = hashlib.sha256(canonical_json_bytes(output_payload)).hexdigest()
        return output_hash.encode("utf-8")

    def get_output(self, attempt_id: str) -> bytes | None:
        """获取 attempt 的输出 bytes（仅用于测试验证确定性）。"""
        return self._outputs.get(attempt_id)
