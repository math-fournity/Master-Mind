"""TargetSolverPort — 目标解题器端口协议与数据对象（WP-SV1）。

来自 docs/implementation/05-execution-ports-and-carriers.md：

```python
class TargetSolverPort(Protocol):
    def prepare(self, job): ...
    def launch(self, prepared_job): ...
    def observe(self, ticket): ...
    def collect(self, ticket): ...
    def cancel(self, ticket, fence_token): ...
    def reconcile(self, attempt_id, fence_token): ...
```

TargetSolver 与认知角色（ModelRolePort）是两个不同端口，物理隔离。
Solver 通过 HarnessAdapter 调用 solver_harness，不直接调用 devin binary。

数据对象：
- SolverJob：冻结 job specification（problem_ref+hash, view_ref+hash,
  budget_contract, tool_policy, idempotency_key, fence_token, attempt_id,
  repo_workspace_spec）
- PreparedSolverJob：prepare() 返回的冻结 prepared job，所有 hash 已绑定
- LaunchTicket：launch() 返回的 ticket（attempt_id, fence_token,
  launch_timestamp, observability refs）
- LaunchReceipt：collect() 返回的最终收据（trajectory_ref+hash,
  answer_ref+hash, exit_and_terminal_reason, wallclock, cost_observability,
  capability_report_refs, retry_replay_lineage, failure_or_quarantine_state）

硬约束：
- trajectory MUST be present（缺 trajectory = FAIL，blocker）
- answer_ref 与 trajectory_ref 分离（answer isolation）
- v1 只允许 NoTool policy

SIDE_EFFECT_FREE：纯内存实现，不调用真实 solver_harness / CLI / DB。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    SV_ALLOWED_OUTPUT_KINDS,
    SV_ANSWER_KINDS,
    SV_FORBIDDEN_OUTPUT_KINDS,
    SV_LAUNCH_STATES,
    SV_TERMINAL_REASONS,
    SV_TOOL_POLICY_KINDS,
    SV_TRAJECTORY_KINDS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_REPORT_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-hash-null)"


class SolverJobError(Exception):
    """SolverJob / PreparedSolverJob / LaunchTicket / LaunchReceipt 错误。"""

    def __init__(self, code: EC, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


def _sha256_hex(value: str) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(c in "0123456789abcdef" for c in value)
    )


def _ref_and_hash(obj: dict[str, Any]) -> bool:
    return (
        isinstance(obj, dict)
        and set(obj.keys()) == {"ref_id", "sha256"}
        and isinstance(obj.get("ref_id"), str)
        and _sha256_hex(obj.get("sha256", ""))
    )


# ─── TargetSolverPort 协议 ───────────────────────────────────────────────


@runtime_checkable
class TargetSolverPort(Protocol):
    """TargetSolverPort — 目标解题器端口协议。

    prepare → launch → observe → collect → reconcile 完整 lifecycle。
    cancel 可在 launch 后、terminal 前调用。
    """

    def prepare(self, job: SolverJob) -> PreparedSolverJob: ...
    def launch(self, prepared_job: PreparedSolverJob) -> LaunchTicket: ...
    def observe(self, ticket: LaunchTicket) -> dict[str, Any]: ...
    def collect(self, ticket: LaunchTicket) -> LaunchReceipt: ...
    def cancel(self, ticket: LaunchTicket, fence_token: str) -> LaunchReceipt: ...
    def reconcile(self, attempt_id: str, fence_token: str) -> VerificationResult: ...


# ─── SolverJob ───────────────────────────────────────────────────────────


@dataclass(frozen=True)
class SolverJob:
    """SolverJob — 冻结 job specification。

    字段：
    - problem_ref_and_hash：题目引用 + sha256
    - view_ref_and_hash：输入 view 引用 + sha256
    - budget_contract：预算合同（wallclock_seconds, max_tokens, max_cost_microunits）
    - tool_policy_kind：工具策略（v1 只允许 NO_TOOL）
    - idempotency_key：幂等键
    - fence_token：fence token
    - attempt_id：attempt 唯一标识
    - repo_workspace_spec：repo workspace 隔离规格
    - harness_profile_ref_and_hash：harness profile 引用 + sha256
    """

    problem_ref_and_hash: dict[str, str]
    view_ref_and_hash: dict[str, str]
    budget_contract: dict[str, Any]
    tool_policy_kind: str
    idempotency_key: str
    fence_token: str
    attempt_id: str
    repo_workspace_spec: dict[str, Any]
    harness_profile_ref_and_hash: dict[str, str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "problem_ref_and_hash": dict(self.problem_ref_and_hash),
            "view_ref_and_hash": dict(self.view_ref_and_hash),
            "budget_contract": dict(self.budget_contract),
            "tool_policy_kind": self.tool_policy_kind,
            "idempotency_key": self.idempotency_key,
            "fence_token": self.fence_token,
            "attempt_id": self.attempt_id,
            "repo_workspace_spec": dict(self.repo_workspace_spec),
            "harness_profile_ref_and_hash": dict(self.harness_profile_ref_and_hash),
        }

    @property
    def job_hash(self) -> str:
        """计算 SolverJob 的确定性 hash（不含 attempt_id/fence_token/idempotency_key
        之外的可变部分——这些字段本身是冻结的，全部纳入 hash）。"""
        obj = self.to_dict()
        obj["job_hash"] = None
        return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()


def build_solver_job(
    *,
    problem_ref_id: str,
    problem_sha256: str,
    view_ref_id: str,
    view_sha256: str,
    budget_contract: dict[str, Any],
    tool_policy_kind: str = "NO_TOOL",
    idempotency_key: str,
    fence_token: str,
    attempt_id: str,
    repo_workspace_spec: dict[str, Any] | None = None,
    harness_profile_ref_id: str,
    harness_profile_sha256: str,
) -> SolverJob:
    """构建 SolverJob。"""
    return SolverJob(
        problem_ref_and_hash={"ref_id": problem_ref_id, "sha256": problem_sha256},
        view_ref_and_hash={"ref_id": view_ref_id, "sha256": view_sha256},
        budget_contract=dict(budget_contract),
        tool_policy_kind=tool_policy_kind,
        idempotency_key=idempotency_key,
        fence_token=fence_token,
        attempt_id=attempt_id,
        repo_workspace_spec=dict(repo_workspace_spec) if repo_workspace_spec else {},
        harness_profile_ref_and_hash={
            "ref_id": harness_profile_ref_id,
            "sha256": harness_profile_sha256,
        },
    )


def verify_solver_job(job: SolverJob | dict[str, Any]) -> VerificationResult:
    """验证 SolverJob 的 schema + semantic 合法性。

    检查：
    1. problem_ref_and_hash 结构合法
    2. view_ref_and_hash 结构合法
    3. budget_contract 结构合法（wallclock_seconds, max_tokens, max_cost_microunits）
    4. tool_policy_kind 在 SV_TOOL_POLICY_KINDS 中
    5. idempotency_key 非空
    6. fence_token 非空
    7. attempt_id 非空
    8. repo_workspace_spec 结构合法（isolation_kind）
    9. harness_profile_ref_and_hash 结构合法
    10. job_hash 正确
    """
    if isinstance(job, SolverJob):
        job_dict = job.to_dict()
    else:
        job_dict = job

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. problem_ref_and_hash
    problem_ref = job_dict.get("problem_ref_and_hash", {})
    if not _ref_and_hash(problem_ref):
        _err(EC.SV_PROBLEM_REF_HASH_MISMATCH,
             "problem_ref_and_hash must have ref_id and sha256")

    # 2. view_ref_and_hash
    view_ref = job_dict.get("view_ref_and_hash", {})
    if not _ref_and_hash(view_ref):
        _err(EC.SV_VIEW_REF_HASH_MISMATCH,
             "view_ref_and_hash must have ref_id and sha256")

    # 3. budget_contract
    budget = job_dict.get("budget_contract", {})
    if not isinstance(budget, dict):
        _err(EC.SV_BUDGET_CONTRACT_INVALID, "budget_contract is not a dict")
    else:
        for req_field in ("wallclock_seconds", "max_tokens", "max_cost_microunits"):
            val = budget.get(req_field)
            if not isinstance(val, int) or val < 0:
                _err(EC.SV_BUDGET_CONTRACT_INVALID,
                     f"budget_contract.{req_field} must be a non-negative int")

    # 4. tool_policy_kind
    tp_kind = job_dict.get("tool_policy_kind", "")
    if tp_kind not in SV_TOOL_POLICY_KINDS:
        _err(EC.SV_TOOL_POLICY_KIND_INVALID,
             f"tool_policy_kind {tp_kind!r} not in SV_TOOL_POLICY_KINDS")

    # 5. idempotency_key
    if not job_dict.get("idempotency_key"):
        _err(EC.REQUIRED_FIELD_MISSING, "idempotency_key is empty")

    # 6. fence_token
    if not job_dict.get("fence_token"):
        _err(EC.SV_FENCE_TOKEN_INVALID, "fence_token is empty")

    # 7. attempt_id
    if not job_dict.get("attempt_id"):
        _err(EC.REQUIRED_FIELD_MISSING, "attempt_id is empty")

    # 8. repo_workspace_spec
    workspace = job_dict.get("repo_workspace_spec", {})
    if not isinstance(workspace, dict):
        _err(EC.SV_REPO_WORKSPACE_NOT_ISOLATED,
             "repo_workspace_spec is not a dict")
    else:
        isolation = workspace.get("isolation_kind", "")
        if isolation not in ("ISOLATED", "EPHEMERAL_SANDBOX"):
            _err(EC.SV_REPO_WORKSPACE_NOT_ISOLATED,
                 f"repo_workspace_spec.isolation_kind must be ISOLATED or "
                 f"EPHEMERAL_SANDBOX, got {isolation!r}")

    # 9. harness_profile_ref_and_hash
    profile_ref = job_dict.get("harness_profile_ref_and_hash", {})
    if not _ref_and_hash(profile_ref):
        _err(EC.SV_HARNESS_PROFILE_HASH_MISMATCH,
             "harness_profile_ref_and_hash must have ref_id and sha256")

    # 10. job_hash
    if "job_hash" in job_dict and job_dict.get("job_hash") is not None:
        obj_for_hash = dict(job_dict)
        obj_for_hash["job_hash"] = None
        computed = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
        if job_dict.get("job_hash") != computed:
            _err(EC.SV_PREPARED_JOB_HASH_DRIFT,
                 f"job_hash mismatch: expected {computed}, "
                 f"got {job_dict.get('job_hash')}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# ─── PreparedSolverJob ───────────────────────────────────────────────────


@dataclass(frozen=True)
class PreparedSolverJob:
    """PreparedSolverJob — prepare() 返回的冻结 prepared job。

    所有 hash 已绑定。包含原始 job_hash 和 prepared_hash。
    prepare() 验证 job 合法性后返回 prepared job。
    """

    job: SolverJob
    job_hash: str
    prepared_hash: str
    prepared_at: str
    harness_profile_verified: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "job": self.job.to_dict(),
            "job_hash": self.job_hash,
            "prepared_hash": self.prepared_hash,
            "prepared_at": self.prepared_at,
            "harness_profile_verified": self.harness_profile_verified,
        }


def prepare_solver_job(
    job: SolverJob,
    *,
    prepared_at: str = "2026-08-14T12:00:00Z",
    harness_profile_verified: bool = True,
) -> tuple[PreparedSolverJob | None, VerificationResult]:
    """验证 SolverJob 并返回 PreparedSolverJob。

    如果验证失败，返回 (None, VerificationResult(FAIL))。
    """
    result = verify_solver_job(job)
    if not result.passed:
        return None, result

    job_hash = job.job_hash
    prepared_obj = {
        "job_hash": job_hash,
        "prepared_at": prepared_at,
        "harness_profile_verified": harness_profile_verified,
        "prepared_hash": None,
    }
    prepared_hash = hashlib.sha256(canonical_json_bytes(prepared_obj)).hexdigest()

    prepared = PreparedSolverJob(
        job=job,
        job_hash=job_hash,
        prepared_hash=prepared_hash,
        prepared_at=prepared_at,
        harness_profile_verified=harness_profile_verified,
    )
    return prepared, VerificationResult(verdict="PASS")


def verify_prepared_solver_job(
    prepared: PreparedSolverJob | dict[str, Any],
) -> VerificationResult:
    """验证 PreparedSolverJob 的 schema + hash 一致性。

    检查：
    1. job_hash 正确（与 job.job_hash 一致）
    2. prepared_hash 正确
    3. harness_profile_verified 为 True
    4. 内部 job 合法
    """
    if isinstance(prepared, PreparedSolverJob):
        prepared_dict = prepared.to_dict()
        job_obj = prepared.job
    else:
        prepared_dict = prepared
        job_obj = None

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 验证内部 job
    job_dict = prepared_dict.get("job", {})
    job_result = verify_solver_job(job_dict)
    if not job_result.passed:
        errors.extend(job_result.error_codes)
        details.extend(job_result.details)

    # job_hash
    expected_job_hash = hashlib.sha256(
        canonical_json_bytes({**job_dict, "job_hash": None})
    ).hexdigest()
    if prepared_dict.get("job_hash") != expected_job_hash:
        _err(EC.SV_PREPARED_JOB_HASH_DRIFT,
             f"job_hash mismatch: expected {expected_job_hash}, "
             f"got {prepared_dict.get('job_hash')}")

    # prepared_hash
    prepared_obj_for_hash = {
        "job_hash": prepared_dict.get("job_hash", ""),
        "prepared_at": prepared_dict.get("prepared_at", ""),
        "harness_profile_verified": prepared_dict.get("harness_profile_verified", False),
        "prepared_hash": None,
    }
    expected_prepared_hash = hashlib.sha256(
        canonical_json_bytes(prepared_obj_for_hash)
    ).hexdigest()
    if prepared_dict.get("prepared_hash") != expected_prepared_hash:
        _err(EC.SV_PREPARED_JOB_HASH_DRIFT,
             f"prepared_hash mismatch: expected {expected_prepared_hash}, "
             f"got {prepared_dict.get('prepared_hash')}")

    # harness_profile_verified
    if not prepared_dict.get("harness_profile_verified"):
        _err(EC.SV_HARNESS_PROFILE_HASH_MISMATCH,
             "harness_profile_verified must be True")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# ─── LaunchTicket ────────────────────────────────────────────────────────


@dataclass(frozen=True)
class LaunchTicket:
    """LaunchTicket — launch() 返回的 ticket。

    包含 attempt_id, fence_token, launch_timestamp, observability refs。
    """

    attempt_id: str
    fence_token: str
    launch_timestamp: str
    launch_state: str
    prepared_hash: str
    observability_refs: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_id": self.attempt_id,
            "fence_token": self.fence_token,
            "launch_timestamp": self.launch_timestamp,
            "launch_state": self.launch_state,
            "prepared_hash": self.prepared_hash,
            "observability_refs": dict(self.observability_refs),
        }


def verify_launch_ticket(
    ticket: LaunchTicket | dict[str, Any],
) -> VerificationResult:
    """验证 LaunchTicket 的 schema 合法性。

    检查：
    1. attempt_id 非空
    2. fence_token 非空
    3. launch_timestamp 非空
    4. launch_state 在 SV_LAUNCH_STATES 中
    5. prepared_hash 是合法 sha256
    """
    if isinstance(ticket, LaunchTicket):
        ticket_dict = ticket.to_dict()
    else:
        ticket_dict = ticket

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    if not ticket_dict.get("attempt_id"):
        _err(EC.SV_LAUNCH_TICKET_INVALID, "attempt_id is empty")

    if not ticket_dict.get("fence_token"):
        _err(EC.SV_FENCE_TOKEN_INVALID, "fence_token is empty")

    if not ticket_dict.get("launch_timestamp"):
        _err(EC.SV_LAUNCH_TICKET_INVALID, "launch_timestamp is empty")

    launch_state = ticket_dict.get("launch_state", "")
    if launch_state not in SV_LAUNCH_STATES:
        _err(EC.SV_LAUNCH_STATE_INVALID,
             f"launch_state {launch_state!r} not in SV_LAUNCH_STATES")

    if not _sha256_hex(ticket_dict.get("prepared_hash", "")):
        _err(EC.SV_LAUNCH_TICKET_INVALID,
             "prepared_hash must be a lowercase sha256 hex")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# ─── LaunchReceipt ───────────────────────────────────────────────────────


@dataclass(frozen=True)
class LaunchReceipt:
    """LaunchReceipt — collect() 返回的最终收据。

    字段：
    - attempt_id：attempt 唯一标识
    - fence_token：fence token
    - trajectory_ref_and_hash：trajectory 引用 + sha256（MUST be present）
    - trajectory_kind：trajectory 种类（FULL/PARTIAL/EMPTY）
    - answer_ref_and_hash：answer 引用 + sha256（与 trajectory 分离）
    - answer_kind：answer 种类（FINAL/PARTIAL/NO_ANSWER）
    - exit_code：退出码
    - terminal_reason：终止原因（在 SV_TERMINAL_REASONS 中）
    - wallclock_seconds：实际墙钟耗时
    - cost_observability：成本可观察性（tokens, cost_microunits）
    - capability_report_refs：能力报告引用列表
    - retry_replay_lineage：重试/重放血缘
    - failure_or_quarantine_state：失败或隔离状态（空字符串表示成功）
    - report_hash_algorithm / report_hash：收据 hash
    """

    attempt_id: str
    fence_token: str
    trajectory_ref_and_hash: dict[str, str]
    trajectory_kind: str
    answer_ref_and_hash: dict[str, str]
    answer_kind: str
    exit_code: int
    terminal_reason: str
    wallclock_seconds: int
    cost_observability: dict[str, Any]
    capability_report_refs: list[dict[str, str]]
    retry_replay_lineage: list[dict[str, Any]]
    failure_or_quarantine_state: str
    report_hash_algorithm: str
    report_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_id": self.attempt_id,
            "fence_token": self.fence_token,
            "trajectory_ref_and_hash": dict(self.trajectory_ref_and_hash),
            "trajectory_kind": self.trajectory_kind,
            "answer_ref_and_hash": dict(self.answer_ref_and_hash),
            "answer_kind": self.answer_kind,
            "exit_code": self.exit_code,
            "terminal_reason": self.terminal_reason,
            "wallclock_seconds": self.wallclock_seconds,
            "cost_observability": dict(self.cost_observability),
            "capability_report_refs": [dict(r) for r in self.capability_report_refs],
            "retry_replay_lineage": [dict(r) for r in self.retry_replay_lineage],
            "failure_or_quarantine_state": self.failure_or_quarantine_state,
            "report_hash_algorithm": self.report_hash_algorithm,
            "report_hash": self.report_hash,
        }


def build_launch_receipt(
    *,
    attempt_id: str,
    fence_token: str,
    trajectory_ref_id: str,
    trajectory_sha256: str,
    trajectory_kind: str = "FULL_TRAJECTORY",
    answer_ref_id: str,
    answer_sha256: str,
    answer_kind: str = "FINAL_ANSWER",
    exit_code: int = 0,
    terminal_reason: str = "COMPLETED",
    wallclock_seconds: int = 0,
    cost_observability: dict[str, Any] | None = None,
    capability_report_refs: list[dict[str, str]] | None = None,
    retry_replay_lineage: list[dict[str, Any]] | None = None,
    failure_or_quarantine_state: str = "",
) -> LaunchReceipt:
    """构建 LaunchReceipt，自动计算 report_hash。"""
    cost = dict(cost_observability) if cost_observability else {
        "input_tokens": 0,
        "output_tokens": 0,
        "cost_microunits": 0,
        "usage_completeness": "COMPLETE",
    }
    cap_refs = [dict(r) for r in capability_report_refs] if capability_report_refs else []
    lineage = [dict(r) for r in retry_replay_lineage] if retry_replay_lineage else []

    obj = {
        "attempt_id": attempt_id,
        "fence_token": fence_token,
        "trajectory_ref_and_hash": {
            "ref_id": trajectory_ref_id,
            "sha256": trajectory_sha256,
        },
        "trajectory_kind": trajectory_kind,
        "answer_ref_and_hash": {
            "ref_id": answer_ref_id,
            "sha256": answer_sha256,
        },
        "answer_kind": answer_kind,
        "exit_code": exit_code,
        "terminal_reason": terminal_reason,
        "wallclock_seconds": wallclock_seconds,
        "cost_observability": cost,
        "capability_report_refs": cap_refs,
        "retry_replay_lineage": lineage,
        "failure_or_quarantine_state": failure_or_quarantine_state,
        "report_hash_algorithm": _REPORT_HASH_ALGORITHM,
        "report_hash": None,
    }
    report_hash = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

    return LaunchReceipt(
        attempt_id=attempt_id,
        fence_token=fence_token,
        trajectory_ref_and_hash={
            "ref_id": trajectory_ref_id,
            "sha256": trajectory_sha256,
        },
        trajectory_kind=trajectory_kind,
        answer_ref_and_hash={
            "ref_id": answer_ref_id,
            "sha256": answer_sha256,
        },
        answer_kind=answer_kind,
        exit_code=exit_code,
        terminal_reason=terminal_reason,
        wallclock_seconds=wallclock_seconds,
        cost_observability=cost,
        capability_report_refs=cap_refs,
        retry_replay_lineage=lineage,
        failure_or_quarantine_state=failure_or_quarantine_state,
        report_hash_algorithm=_REPORT_HASH_ALGORITHM,
        report_hash=report_hash,
    )


def verify_launch_receipt(
    receipt: LaunchReceipt | dict[str, Any],
) -> VerificationResult:
    """验证 LaunchReceipt 的 schema + semantic 合法性。

    检查（blocker tests）：
    1. trajectory_ref_and_hash 存在且结构合法（缺 trajectory = FAIL）
    2. trajectory_kind 在 SV_TRAJECTORY_KINDS 中
    3. answer_ref_and_hash 存在且结构合法
    4. answer_kind 在 SV_ANSWER_KINDS 中
    5. answer_ref 与 trajectory_ref 分离（answer isolation）
    6. terminal_reason 在 SV_TERMINAL_REASONS 中
    7. cost_observability 结构合法
    8. report_hash 正确
    9. exit_code 合法
    """
    if isinstance(receipt, LaunchReceipt):
        receipt_dict = receipt.to_dict()
    else:
        receipt_dict = receipt

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # attempt_id / fence_token
    if not receipt_dict.get("attempt_id"):
        _err(EC.SV_LAUNCH_RECEIPT_INCOMPLETE, "attempt_id is empty")
    if not receipt_dict.get("fence_token"):
        _err(EC.SV_FENCE_TOKEN_INVALID, "fence_token is empty")

    # 1. trajectory MUST be present (blocker: missing trajectory = FAIL)
    traj_ref = receipt_dict.get("trajectory_ref_and_hash", {})
    if not _ref_and_hash(traj_ref):
        _err(EC.SV_TRAJECTORY_MISSING,
             "trajectory_ref_and_hash must be present with ref_id and sha256")

    # 2. trajectory_kind
    traj_kind = receipt_dict.get("trajectory_kind", "")
    if traj_kind not in SV_TRAJECTORY_KINDS:
        _err(EC.SV_TRAJECTORY_KIND_INVALID,
             f"trajectory_kind {traj_kind!r} not in SV_TRAJECTORY_KINDS")

    # 3. answer_ref_and_hash
    answer_ref = receipt_dict.get("answer_ref_and_hash", {})
    if not _ref_and_hash(answer_ref):
        _err(EC.SV_ANSWER_NOT_ISOLATED,
             "answer_ref_and_hash must be present with ref_id and sha256")

    # 4. answer_kind
    answer_kind = receipt_dict.get("answer_kind", "")
    if answer_kind not in SV_ANSWER_KINDS:
        _err(EC.SV_ANSWER_KIND_INVALID,
             f"answer_kind {answer_kind!r} not in SV_ANSWER_KINDS")

    # 5. answer isolation — answer_ref must differ from trajectory_ref
    if (
        _ref_and_hash(traj_ref)
        and _ref_and_hash(answer_ref)
        and traj_ref.get("ref_id") == answer_ref.get("ref_id")
    ):
        _err(EC.SV_ANSWER_NOT_ISOLATED,
             f"answer_ref_id {answer_ref.get('ref_id')!r} must differ from "
             f"trajectory_ref_id {traj_ref.get('ref_id')!r}")

    # 6. terminal_reason
    terminal_reason = receipt_dict.get("terminal_reason", "")
    if terminal_reason not in SV_TERMINAL_REASONS:
        _err(EC.SV_TERMINAL_REASON_INVALID,
             f"terminal_reason {terminal_reason!r} not in SV_TERMINAL_REASONS")

    # 7. cost_observability
    cost = receipt_dict.get("cost_observability", {})
    if not isinstance(cost, dict):
        _err(EC.SV_LAUNCH_RECEIPT_INCOMPLETE,
             "cost_observability is not a dict")
    else:
        for req_field in ("input_tokens", "output_tokens", "cost_microunits"):
            val = cost.get(req_field)
            if not isinstance(val, int) or val < 0:
                _err(EC.SV_LAUNCH_RECEIPT_INCOMPLETE,
                     f"cost_observability.{req_field} must be a non-negative int")

    # 8. report_hash
    if receipt_dict.get("report_hash_algorithm") != _REPORT_HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"unexpected report_hash_algorithm: "
             f"{receipt_dict.get('report_hash_algorithm')}")
    obj_for_hash = dict(receipt_dict)
    obj_for_hash["report_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if receipt_dict.get("report_hash") != computed_hash:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"report_hash mismatch: expected {computed_hash}, "
             f"got {receipt_dict.get('report_hash')}")

    # 9. exit_code
    exit_code = receipt_dict.get("exit_code")
    if not isinstance(exit_code, int):
        _err(EC.SV_LAUNCH_RECEIPT_INCOMPLETE,
             "exit_code must be an int")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
