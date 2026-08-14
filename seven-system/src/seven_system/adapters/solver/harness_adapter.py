"""HarnessAdapter — solver_harness 适配器（WP-SV1）。

这是唯一允许调用 solver_harness 的模块（docs/implementation/05-execution-ports-and-carriers.md
line 406-414）。

SIDE_EFFECT_FREE：实现为 protocol + fake/stub 实现，产生确定性 LaunchReceipts，
不调用真实 subprocess。真实 subprocess call 是 activation-gated。

FakeHarnessAdapter 实现 TargetSolverPort 协议：
- prepare：验证 SolverJob，返回 PreparedSolverJob
- launch：返回 LaunchTicket
- observe：返回 observability snapshot
- collect：返回 LaunchReceipt（确定性，trajectory + answer 分离）
- cancel：在 terminal 前取消
- reconcile：验证 attempt 一致性

可配置 fault injection：
- force_tool_events：模拟 tool events（blocker test FAIL）
- force_missing_trajectory：模拟缺 trajectory（blocker test FAIL）
- force_repo_workspace_not_isolated：模拟 repo workspace 未隔离
- force_answer_not_isolated：模拟 answer 与 trajectory 未分离
- force_direct_devin_bypass：模拟直接调用 devin binary（bypass）
- force_budget_exceeded：模拟预算超限
- force_cancel_after_terminal：模拟 terminal 后 cancel
- force_fence_mismatch：模拟 fence token 不匹配
- force_profile_hash_mismatch：模拟 profile hash 不匹配
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    SV_LAUNCH_STATES,
    SV_TERMINAL_REASONS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult
from .port import (
    LaunchReceipt,
    LaunchTicket,
    PreparedSolverJob,
    SolverJob,
    SolverJobError,
    build_launch_receipt,
    prepare_solver_job,
    verify_launch_receipt,
    verify_launch_ticket,
    verify_prepared_solver_job,
    verify_solver_job,
)
from .harness_profile import HarnessProfile, verify_harness_profile
from .notool_policy import NoToolPolicy, check_trajectory_for_tool_events


class HarnessAdapterError(Exception):
    """HarnessAdapter 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


@dataclass
class HarnessAdapter:
    """HarnessAdapter — solver_harness 适配器基类/协议。

    这是唯一允许调用 solver_harness 的模块。
    真实 subprocess call 是 activation-gated，SIDE_EFFECT_FREE 模式下不调用。

    子类（FakeHarnessAdapter）提供确定性 fake 实现。
    """

    harness_profile: HarnessProfile | None = None
    notool_policy: NoToolPolicy | None = None

    def prepare(self, job: SolverJob) -> PreparedSolverJob:
        raise NotImplementedError

    def launch(self, prepared_job: PreparedSolverJob) -> LaunchTicket:
        raise NotImplementedError

    def observe(self, ticket: LaunchTicket) -> dict[str, Any]:
        raise NotImplementedError

    def collect(self, ticket: LaunchTicket) -> LaunchReceipt:
        raise NotImplementedError

    def cancel(self, ticket: LaunchTicket, fence_token: str) -> LaunchReceipt:
        raise NotImplementedError

    def reconcile(self, attempt_id: str, fence_token: str) -> VerificationResult:
        raise NotImplementedError


@dataclass
class FakeHarnessAdapter(HarnessAdapter):
    """FakeHarnessAdapter — 确定性 fake 实现 TargetSolverPort。

    SIDE_EFFECT_FREE：不调用真实 solver_harness / subprocess。
    产生确定性 LaunchReceipts。

    可配置 fault injection 用于 blocker tests。
    """

    force_tool_events: bool = False
    force_missing_trajectory: bool = False
    force_repo_workspace_not_isolated: bool = False
    force_answer_not_isolated: bool = False
    force_direct_devin_bypass: bool = False
    force_budget_exceeded: bool = False
    force_cancel_after_terminal: bool = False
    force_fence_mismatch: bool = False
    force_profile_hash_mismatch: bool = False
    _prepared: dict[str, PreparedSolverJob] = field(default_factory=dict, repr=False)
    _tickets: dict[str, LaunchTicket] = field(default_factory=dict, repr=False)
    _receipts: dict[str, LaunchReceipt] = field(default_factory=dict, repr=False)
    _terminal: dict[str, bool] = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        if self.notool_policy is None:
            from .notool_policy import build_notool_policy
            self.notool_policy = build_notool_policy()
        if self.harness_profile is None:
            from .harness_profile import build_harness_profile
            content = hashlib.sha256(b"fake-harness-content-v1").hexdigest()
            self.harness_profile = build_harness_profile(
                version="fake-harness-v1",
                content_hash=content,
                harness_kind="FAKE_HARNESS",
                tool_policy_kind="NO_TOOL",
            )

    # ─── TargetSolverPort 协议实现 ───────────────────────────────────

    def prepare(self, job: SolverJob) -> PreparedSolverJob:
        """验证 SolverJob 并返回 PreparedSolverJob。"""
        # 验证 job
        job_result = verify_solver_job(job)
        if not job_result.passed:
            raise SolverJobError(
                job_result.error_codes[0],
                "; ".join(job_result.details),
            )

        # 验证 harness profile hash（如果 job 中引用的 hash 与 adapter profile 不匹配）
        if self.harness_profile is not None and not self.force_profile_hash_mismatch:
            job_profile_hash = job.harness_profile_ref_and_hash.get("sha256", "")
            if job_profile_hash and job_profile_hash != self.harness_profile.profile_hash:
                raise SolverJobError(
                    EC.SV_HARNESS_PROFILE_HASH_MISMATCH,
                    f"job harness_profile_hash {job_profile_hash} != "
                    f"adapter profile_hash {self.harness_profile.profile_hash}",
                )

        if self.force_profile_hash_mismatch:
            raise SolverJobError(
                EC.SV_HARNESS_PROFILE_HASH_MISMATCH,
                "forced profile hash mismatch",
            )

        # repo workspace isolation check (blocker)
        if self.force_repo_workspace_not_isolated:
            raise SolverJobError(
                EC.SV_REPO_WORKSPACE_NOT_ISOLATED,
                "forced repo workspace not isolated",
            )

        prepared, result = prepare_solver_job(job)
        if prepared is None:
            raise SolverJobError(
                result.error_codes[0],
                "; ".join(result.details),
            )

        self._prepared[prepared.prepared_hash] = prepared
        return prepared

    def launch(self, prepared_job: PreparedSolverJob) -> LaunchTicket:
        """返回 LaunchTicket。"""
        # 验证 prepared job
        prepared_result = verify_prepared_solver_job(prepared_job)
        if not prepared_result.passed:
            raise SolverJobError(
                prepared_result.error_codes[0],
                "; ".join(prepared_result.details),
            )

        # budget check (blocker)
        if self.force_budget_exceeded:
            raise SolverJobError(
                EC.SV_BUDGET_EXCEEDED,
                "forced budget exceeded",
            )

        ticket = LaunchTicket(
            attempt_id=prepared_job.job.attempt_id,
            fence_token=prepared_job.job.fence_token,
            launch_timestamp="2026-08-14T12:00:00Z",
            launch_state="LAUNCHED",
            prepared_hash=prepared_job.prepared_hash,
            observability_refs={
                "harness_session_ref": f"harness-session-{prepared_job.job.attempt_id}",
                "trajectory_stream_ref": f"trajectory-stream-{prepared_job.job.attempt_id}",
            },
        )

        ticket_result = verify_launch_ticket(ticket)
        if not ticket_result.passed:
            raise SolverJobError(
                ticket_result.error_codes[0],
                "; ".join(ticket_result.details),
            )

        self._tickets[ticket.attempt_id] = ticket
        self._terminal[ticket.attempt_id] = False
        return ticket

    def observe(self, ticket: LaunchTicket) -> dict[str, Any]:
        """返回 observability snapshot。"""
        if ticket.attempt_id not in self._tickets:
            raise SolverJobError(
                EC.SV_OBSERVE_TICKET_UNKNOWN,
                f"unknown ticket for attempt {ticket.attempt_id}",
            )

        return {
            "attempt_id": ticket.attempt_id,
            "launch_state": "LAUNCHED",
            "wallclock_seconds_so_far": 0,
            "tokens_so_far": 0,
            "is_terminal": self._terminal.get(ticket.attempt_id, False),
            "observability_refs": dict(ticket.observability_refs),
        }

    def collect(self, ticket: LaunchTicket) -> LaunchReceipt:
        """返回确定性 LaunchReceipt。"""
        if ticket.attempt_id not in self._tickets:
            raise SolverJobError(
                EC.SV_COLLECT_TICKET_UNKNOWN,
                f"unknown ticket for attempt {ticket.attempt_id}",
            )

        # fence token check
        if self.force_fence_mismatch or ticket.fence_token != self._tickets[ticket.attempt_id].fence_token:
            raise SolverJobError(
                EC.SV_FENCE_TOKEN_INVALID,
                "fence token mismatch",
            )

        attempt_id = ticket.attempt_id
        prepared = self._prepared.get(ticket.prepared_hash)
        job = prepared.job if prepared else None

        # blocker: missing trajectory = FAIL
        if self.force_missing_trajectory:
            receipt = LaunchReceipt(
                attempt_id=attempt_id,
                fence_token=ticket.fence_token,
                trajectory_ref_and_hash={},
                trajectory_kind="EMPTY_TRAJECTORY",
                answer_ref_and_hash={
                    "ref_id": f"answer-{attempt_id}",
                    "sha256": hashlib.sha256(b"fake-answer").hexdigest(),
                },
                answer_kind="FINAL_ANSWER",
                exit_code=1,
                terminal_reason="FAILED_PERMANENT",
                wallclock_seconds=0,
                cost_observability={
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "cost_microunits": 0,
                    "usage_completeness": "COMPLETE",
                },
                capability_report_refs=[],
                retry_replay_lineage=[],
                failure_or_quarantine_state="TRAJECTORY_MISSING",
                report_hash_algorithm="sha256(RFC8785-JCS-object-with-hash-null)",
                report_hash="0" * 64,
            )
            self._receipts[attempt_id] = receipt
            self._terminal[attempt_id] = True
            return receipt

        # generate deterministic trajectory
        traj_content = canonical_json_bytes({
            "attempt_id": attempt_id,
            "steps": [
                {"step_type": "assistant", "content": "deterministic reasoning step 1"},
                {"step_type": "assistant", "content": "deterministic reasoning step 2"},
                {"step_type": "terminal", "event": "COMPLETED"},
            ],
        })
        traj_hash = hashlib.sha256(traj_content).hexdigest()

        # blocker: tool event detected
        if self.force_tool_events:
            traj_content_with_tools = canonical_json_bytes({
                "attempt_id": attempt_id,
                "steps": [
                    {"step_type": "assistant", "content": "reasoning"},
                    {"step_type": "tool", "tool_name": "shell", "content": "ls"},
                    {"step_type": "terminal", "event": "COMPLETED"},
                ],
            })
            traj_hash = hashlib.sha256(traj_content_with_tools).hexdigest()

        # answer content (separate from trajectory)
        answer_content = canonical_json_bytes({
            "attempt_id": attempt_id,
            "answer": "42",
        })
        answer_hash = hashlib.sha256(answer_content).hexdigest()

        # blocker: answer not isolated
        answer_ref_id = f"answer-{attempt_id}"
        traj_ref_id = f"trajectory-{attempt_id}"
        if self.force_answer_not_isolated:
            answer_ref_id = traj_ref_id  # same ref = not isolated

        # blocker: direct devin bypass
        failure_state = ""
        terminal_reason = "COMPLETED"
        exit_code = 0
        if self.force_direct_devin_bypass:
            failure_state = "DIRECT_DEVIN_BYPASS_DETECTED"
            terminal_reason = "FAILED_PERMANENT"
            exit_code = 1

        receipt = build_launch_receipt(
            attempt_id=attempt_id,
            fence_token=ticket.fence_token,
            trajectory_ref_id=traj_ref_id,
            trajectory_sha256=traj_hash,
            trajectory_kind="FULL_TRAJECTORY",
            answer_ref_id=answer_ref_id,
            answer_sha256=answer_hash,
            answer_kind="FINAL_ANSWER",
            exit_code=exit_code,
            terminal_reason=terminal_reason,
            wallclock_seconds=0,
            cost_observability={
                "input_tokens": 200,
                "output_tokens": 100,
                "cost_microunits": 0,
                "usage_completeness": "COMPLETE",
            },
            capability_report_refs=[],
            retry_replay_lineage=[],
            failure_or_quarantine_state=failure_state,
        )

        self._receipts[attempt_id] = receipt
        self._terminal[attempt_id] = True
        return receipt

    def cancel(self, ticket: LaunchTicket, fence_token: str) -> LaunchReceipt:
        """在 terminal 前取消。"""
        if ticket.attempt_id not in self._tickets:
            raise SolverJobError(
                EC.SV_COLLECT_TICKET_UNKNOWN,
                f"unknown ticket for attempt {ticket.attempt_id}",
            )

        # blocker: cancel after terminal
        if self._terminal.get(ticket.attempt_id, False) or self.force_cancel_after_terminal:
            raise SolverJobError(
                EC.SV_CANCEL_AFTER_TERMINAL,
                f"attempt {ticket.attempt_id} already terminal, cannot cancel",
            )

        if fence_token != ticket.fence_token:
            raise SolverJobError(
                EC.SV_FENCE_TOKEN_INVALID,
                "fence token mismatch on cancel",
            )

        receipt = build_launch_receipt(
            attempt_id=ticket.attempt_id,
            fence_token=fence_token,
            trajectory_ref_id=f"trajectory-{ticket.attempt_id}",
            trajectory_sha256=hashlib.sha256(b"cancelled-trajectory").hexdigest(),
            trajectory_kind="PARTIAL_TRAJECTORY",
            answer_ref_id=f"answer-{ticket.attempt_id}",
            answer_sha256=hashlib.sha256(b"no-answer").hexdigest(),
            answer_kind="NO_ANSWER",
            exit_code=130,
            terminal_reason="CANCELLED",
            wallclock_seconds=0,
            cost_observability={
                "input_tokens": 0,
                "output_tokens": 0,
                "cost_microunits": 0,
                "usage_completeness": "COMPLETE",
            },
            failure_or_quarantine_state="CANCELLED",
        )

        self._receipts[ticket.attempt_id] = receipt
        self._terminal[ticket.attempt_id] = True
        return receipt

    def reconcile(self, attempt_id: str, fence_token: str) -> VerificationResult:
        """验证 attempt 一致性。"""
        receipt = self._receipts.get(attempt_id)
        ticket = self._tickets.get(attempt_id)

        if receipt is None or ticket is None:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.SV_RECONCILE_UNKNOWN_ATTEMPT],
                details=[f"unknown attempt {attempt_id}"],
            )

        # fence mismatch check
        if fence_token != ticket.fence_token:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.SV_RECONCILE_FENCE_MISMATCH],
                details=[
                    f"fence mismatch: reconcile has {fence_token}, "
                    f"ticket has {ticket.fence_token}"
                ],
            )

        # verify receipt
        receipt_result = verify_launch_receipt(receipt)
        if not receipt_result.passed:
            return receipt_result

        return VerificationResult(verdict="PASS")
