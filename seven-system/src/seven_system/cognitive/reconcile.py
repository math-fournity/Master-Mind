"""AttemptReconciler — 识别 unknown-start / stale-fence / sensitive-sink / illegal-state。

来自 docs/implementation/05-execution-ports-and-carriers.md CW0 行：
"blocker与故障验收: unknown-start、stale fence、敏感sink、非法状态"

reconcile 对 attempt 的状态、fence token、output sink 和状态转换历史逐项对账：
- unknown-start：dispatch without accepted（STARTED 但没有 ACCEPTED）
- stale-fence：fence token 过期或不匹配
- sensitive-sink：output 写入错误 sink（非 RESTRICTED_VAULT）
- illegal-state：非法状态转换（如 CREATED → COMPLETED 跳过中间状态）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import (
    ATTEMPT_RECONCILE_VERDICTS,
    ATTEMPT_TERMINAL_STATES,
    ATTEMPT_TRANSITIONS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from .attempt import Attempt, AttemptReceipt, AttemptState, verify_attempt_receipt


@dataclass(frozen=True)
class ReconcileResult:
    """reconcile 结果。

    verdict:
    - CONSISTENT：attempt 状态一致，无问题
    - UNKNOWN_START：dispatch without accepted
    - STALE_FENCE：fence token 过期或不匹配
    - SENSITIVE_SINK：output 写入错误 sink
    - ILLEGAL_STATE：非法状态转换
    """

    verdict: str
    attempt_id: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)

    @property
    def is_consistent(self) -> bool:
        return self.verdict == "CONSISTENT"

    def to_dict(self) -> dict[str, Any]:
        return {
            "verdict": self.verdict,
            "attempt_id": self.attempt_id,
            "error_codes": [ec.value for ec in self.error_codes],
            "details": list(self.details),
        }


@dataclass
class AttemptReconciler:
    """AttemptReconciler — 对账 attempt 状态一致性。

    检查项：
    1. receipt 本身合法（verify_attempt_receipt）
    2. attempt 状态与 receipt 状态一致
    3. unknown-start：attempt 状态为 STARTED 但没有 ACCEPTED 记录
    4. stale-fence：fence token 不匹配或过期
    5. sensitive-sink：output_sink_kind 不是 RESTRICTED_VAULT（对敏感输出）
    6. illegal-state：状态转换路径非法
    """

    expected_fence_tokens: dict[str, str] = field(default_factory=dict)

    def reconcile(
        self,
        attempt: Attempt,
        receipt: AttemptReceipt | dict[str, Any],
        *,
        expected_fence_token: str | None = None,
    ) -> ReconcileResult:
        """对账单个 attempt。

        返回 ReconcileResult，verdict 为 CONSISTENT 或具体问题类型。
        """
        # 统一 receipt 为 dict
        if isinstance(receipt, AttemptReceipt):
            receipt_dict = receipt.to_dict()
            receipt_state = receipt.state
            receipt_fence = receipt.fence_token
            receipt_lifecycle = receipt.lifecycle_events
        else:
            receipt_dict = receipt
            receipt_state = receipt.get("state", "")
            receipt_fence = receipt.get("fence_token", "")
            receipt_lifecycle = receipt.get("lifecycle_events", [])

        errors: list[EC] = []
        details: list[str] = []
        verdicts: list[str] = []

        # 1. receipt 验证
        receipt_result = verify_attempt_receipt(receipt_dict)
        if not receipt_result.passed:
            errors.extend(receipt_result.error_codes)
            details.extend(receipt_result.details)
            # 如果有非法状态错误，标记为 ILLEGAL_STATE
            if EC.ATTEMPT_ILLEGAL_STATE_TRANSITION in receipt_result.error_codes:
                verdicts.append("ILLEGAL_STATE")
            if EC.ATTEMPT_SENSITIVE_SINK in receipt_result.error_codes:
                verdicts.append("SENSITIVE_SINK")

        # 2. attempt 状态与 receipt 状态一致
        if attempt.state != receipt_state:
            errors.append(EC.ATTEMPT_ILLEGAL_STATE_TRANSITION)
            details.append(
                f"state mismatch: attempt={attempt.state}, receipt={receipt_state}"
            )
            verdicts.append("ILLEGAL_STATE")

        # 3. unknown-start：STARTED 但没有 ACCEPTED 记录
        # 检查 lifecycle_events 中是否有 ACCEPTED
        lifecycle_states = [e.get("state", "") for e in receipt_lifecycle]
        if attempt.state == AttemptState.STARTED or AttemptState.STARTED in lifecycle_states:
            if AttemptState.ACCEPTED not in lifecycle_states:
                errors.append(EC.ATTEMPT_UNKNOWN_START)
                details.append(
                    "STARTED without ACCEPTED: unknown-start detected"
                )
                verdicts.append("UNKNOWN_START")

        # 也检查：如果 attempt 当前状态是 STARTED 但 accepted_at 为空
        if attempt.state == AttemptState.STARTED and not attempt.accepted_at:
            errors.append(EC.ATTEMPT_UNKNOWN_START)
            details.append("STARTED state but accepted_at is empty")
            if "UNKNOWN_START" not in verdicts:
                verdicts.append("UNKNOWN_START")

        # 4. stale-fence：fence token 不匹配
        if expected_fence_token is not None:
            if attempt.fence_token != expected_fence_token:
                errors.append(EC.ATTEMPT_STALE_FENCE)
                details.append(
                    f"fence token mismatch: attempt={attempt.fence_token}, "
                    f"expected={expected_fence_token}"
                )
                verdicts.append("STALE_FENCE")
        elif receipt_fence != attempt.fence_token:
            errors.append(EC.ATTEMPT_STALE_FENCE)
            details.append(
                f"fence token mismatch: attempt={attempt.fence_token}, "
                f"receipt={receipt_fence}"
            )
            verdicts.append("STALE_FENCE")

        # 5. sensitive-sink：output 写入错误 sink
        # 敏感输出（非 PUBLIC）必须写入 RESTRICTED_VAULT
        if attempt.output_sink_kind and attempt.output_sink_kind != "RESTRICTED_VAULT":
            if attempt.output_artifact_hashes:  # 有输出但 sink 不对
                errors.append(EC.ATTEMPT_SENSITIVE_SINK)
                details.append(
                    f"output written to {attempt.output_sink_kind}, "
                    f"expected RESTRICTED_VAULT"
                )
                if "SENSITIVE_SINK" not in verdicts:
                    verdicts.append("SENSITIVE_SINK")

        # 6. illegal-state：检查状态转换路径
        # 如果 lifecycle_events 中的状态序列有非法转换
        if len(lifecycle_states) > 1:
            for i in range(1, len(lifecycle_states)):
                from_state = lifecycle_states[i - 1]
                to_state = lifecycle_states[i]
                if not AttemptState.can_transition(from_state, to_state):
                    errors.append(EC.ATTEMPT_ILLEGAL_STATE_TRANSITION)
                    details.append(
                        f"illegal transition in lifecycle: {from_state} → {to_state}"
                    )
                    if "ILLEGAL_STATE" not in verdicts:
                        verdicts.append("ILLEGAL_STATE")

        # 确定最终 verdict
        if not verdicts:
            final_verdict = "CONSISTENT"
        else:
            # 优先级：UNKNOWN_START > STALE_FENCE > SENSITIVE_SINK > ILLEGAL_STATE
            priority = ["UNKNOWN_START", "STALE_FENCE", "SENSITIVE_SINK", "ILLEGAL_STATE"]
            final_verdict = "CONSISTENT"
            for p in priority:
                if p in verdicts:
                    final_verdict = p
                    break

        if final_verdict not in ATTEMPT_RECONCILE_VERDICTS:
            final_verdict = "ILLEGAL_STATE"

        return ReconcileResult(
            verdict=final_verdict,
            attempt_id=attempt.attempt_id,
            error_codes=errors,
            details=details,
        )

    def reconcile_batch(
        self,
        attempts: list[tuple[Attempt, AttemptReceipt]],
        *,
        expected_fence_tokens: dict[str, str] | None = None,
    ) -> list[ReconcileResult]:
        """批量对账。"""
        results: list[ReconcileResult] = []
        tokens = expected_fence_tokens or self.expected_fence_tokens
        for attempt, receipt in attempts:
            token = tokens.get(attempt.attempt_id)
            results.append(self.reconcile(attempt, receipt, expected_fence_token=token))
        return results
