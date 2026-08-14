"""CodexExecModelRoleAdapter — Codex CLI exec 认知角色适配器（WP-CW-C1）。

来自 docs/implementation/05-execution-ports-and-carriers.md CodexExecModelRoleAdapter 节：

Codex CLI profile 必须逐项冻结，不能用 "high/ultra" 一个字符串代替：
    carrier: codex_exec_cli
    backend_kind: local_noninteractive_exec
    requested_model: gpt-5.6-sol
    requested_reasoning_effort: xhigh
    requested_reasoning_mode: standard
    requested_orchestration_mode: single_agent
    ...

JSONL parser：
- 原始 JSONL/event stream 逐字节写 append-only sink
- 保留 sequence/timestamp/event type/provider ID
- 未知 event、序号缺口、截断、EOF 前无 terminal 均 fail-closed

硬约束（AGENTS.md rule 4）：
- CodexExecModelRoleAdapter 只表示本地 Codex CLI 的非交互 exec 载体
- OpenAI Responses API 必须由独立的 OpenAIResponsesModelRoleAdapter 实现
- 不得复用 Solver 的 port、workspace、session、AGENTS、能力报告、收据或资源池
- 不得使用 solver_harness 或 Solver workspace

当前状态：SIDE_EFFECT_FREE / IMPLEMENTED_PENDING_EVIDENCE
- 协议 stub、profile 解析、JSONL parser、capability report builder 已实现
- live canary 被 DB1I SchemaState / RT1 Runtime/Reconcile / VLT0 / HG0 激活依赖阻塞
- dispatch/reattach/cancel/get_receipt 是 SIDE_EFFECT_FREE stub，不调用真实 CLI
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    CODEX_FROZEN_EFFORT,
    CODEX_FROZEN_MODE,
    CODEX_FROZEN_MODEL,
    CODEX_FROZEN_ORCHESTRATION,
    CODEX_PROFILE_FIELDS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult
from ...cognitive.model_role_port import DispatchRequest, DispatchResult, ModelRolePort
from ...cognitive.attempt import (
    Attempt,
    AttemptReceipt,
    AttemptState,
    build_attempt_receipt,
)
from ...cognitive.role_execution_contract import verify_role_execution_contract
from ...cognitive.role_registry import RoleRegistry, ROLE_REGISTRY_FROZEN_V1
from .profile_capability import (
    ProfileCapabilityReport,
    build_profile_capability_report,
)
from .bypass_tests import run_bypass_tests


# ─── Codex profile 解析 ──────────────────────────────────────────────────


@dataclass(frozen=True)
class CodexProfile:
    """Codex CLI 冻结 profile。

    model / effort / mode / orchestration 分别冻结。
    """

    carrier: str
    backend_kind: str
    requested_model: str
    model_alias_resolution_policy: str
    requested_reasoning_effort: str
    requested_reasoning_mode: str
    requested_orchestration_mode: str
    requested_service_tier: str
    sandbox_policy_ref_and_hash: dict[str, str]
    tool_policy_ref_and_hash: dict[str, str]
    network_policy_ref_and_hash: dict[str, str]
    output_schema_ref_and_hash: dict[str, str]
    cli_argument_mapping_ref_and_hash: dict[str, str]
    model_release_or_catalog_snapshot_ref_and_hash: dict[str, str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "carrier": self.carrier,
            "backend_kind": self.backend_kind,
            "requested_model": self.requested_model,
            "model_alias_resolution_policy": self.model_alias_resolution_policy,
            "requested_reasoning_effort": self.requested_reasoning_effort,
            "requested_reasoning_mode": self.requested_reasoning_mode,
            "requested_orchestration_mode": self.requested_orchestration_mode,
            "requested_service_tier": self.requested_service_tier,
            "sandbox_policy_ref_and_hash": dict(self.sandbox_policy_ref_and_hash),
            "tool_policy_ref_and_hash": dict(self.tool_policy_ref_and_hash),
            "network_policy_ref_and_hash": dict(self.network_policy_ref_and_hash),
            "output_schema_ref_and_hash": dict(self.output_schema_ref_and_hash),
            "cli_argument_mapping_ref_and_hash": dict(self.cli_argument_mapping_ref_and_hash),
            "model_release_or_catalog_snapshot_ref_and_hash": dict(
                self.model_release_or_catalog_snapshot_ref_and_hash
            ),
        }


def parse_codex_profile(raw: dict[str, Any]) -> tuple[CodexProfile | None, VerificationResult]:
    """解析 Codex CLI profile。

    检查：
    1. 所有 CODEX_PROFILE_FIELDS 存在
    2. carrier == "codex_exec_cli"
    3. backend_kind == "local_noninteractive_exec"
    4. requested_model == "gpt-5.6-sol"
    5. requested_reasoning_effort == "xhigh"
    6. requested_reasoning_mode == "standard"
    7. requested_orchestration_mode == "single_agent"
    8. 所有 ref_and_hash 字段结构合法
    """
    errors: list[EC] = []
    details: list[str] = []

    # 1. 所有字段存在
    for field_name in CODEX_PROFILE_FIELDS:
        if field_name not in raw:
            errors.append(EC.PROFILE_REQUIRED_FIELD_MISSING)
            details.append(f"missing required profile field: {field_name}")

    if errors:
        return None, VerificationResult(
            verdict="FAIL", error_codes=errors, details=details,
        )

    # 2. carrier
    carrier = raw.get("carrier", "")
    if carrier != "codex_exec_cli":
        errors.append(EC.PROFILE_ADAPTER_KIND_MISMATCH)
        details.append(f"carrier must be 'codex_exec_cli', got {carrier!r}")

    # 3. backend_kind
    backend_kind = raw.get("backend_kind", "")
    if backend_kind != "local_noninteractive_exec":
        errors.append(EC.PROFILE_ADAPTER_KIND_MISMATCH)
        details.append(f"backend_kind must be 'local_noninteractive_exec', got {backend_kind!r}")

    # 4. requested_model
    model = raw.get("requested_model", "")
    if model != CODEX_FROZEN_MODEL:
        errors.append(EC.CWC1_MODEL_MISMATCH)
        details.append(f"requested_model must be {CODEX_FROZEN_MODEL!r}, got {model!r}")

    # 5. effort
    effort = raw.get("requested_reasoning_effort", "")
    if effort != CODEX_FROZEN_EFFORT:
        errors.append(EC.CWC1_EFFORT_MISMATCH)
        details.append(
            f"requested_reasoning_effort must be {CODEX_FROZEN_EFFORT!r}, got {effort!r}"
        )

    # 6. mode
    mode = raw.get("requested_reasoning_mode", "")
    if mode != CODEX_FROZEN_MODE:
        errors.append(EC.CWC1_MODE_MISMATCH)
        details.append(
            f"requested_reasoning_mode must be {CODEX_FROZEN_MODE!r}, got {mode!r}"
        )

    # 7. orchestration
    orchestration = raw.get("requested_orchestration_mode", "")
    if orchestration != CODEX_FROZEN_ORCHESTRATION:
        errors.append(EC.CWC1_ORCHESTRATION_MISMATCH)
        details.append(
            f"requested_orchestration_mode must be {CODEX_FROZEN_ORCHESTRATION!r}, "
            f"got {orchestration!r}"
        )

    # 8. ref_and_hash 字段
    ref_fields = [
        "sandbox_policy_ref_and_hash",
        "tool_policy_ref_and_hash",
        "network_policy_ref_and_hash",
        "output_schema_ref_and_hash",
        "cli_argument_mapping_ref_and_hash",
        "model_release_or_catalog_snapshot_ref_and_hash",
    ]
    for ref_field in ref_fields:
        ref_val = raw.get(ref_field, {})
        if not isinstance(ref_val, dict):
            errors.append(EC.PROFILE_REQUIRED_FIELD_MISSING)
            details.append(f"{ref_field} is not a dict")
        elif set(ref_val.keys()) != {"ref_id", "sha256"}:
            errors.append(EC.PROFILE_REQUIRED_FIELD_MISSING)
            details.append(f"{ref_field} must have ref_id and sha256")

    if errors:
        return None, VerificationResult(
            verdict="FAIL", error_codes=errors, details=details,
        )

    profile = CodexProfile(
        carrier=carrier,
        backend_kind=backend_kind,
        requested_model=model,
        model_alias_resolution_policy=raw.get("model_alias_resolution_policy", ""),
        requested_reasoning_effort=effort,
        requested_reasoning_mode=mode,
        requested_orchestration_mode=orchestration,
        requested_service_tier=raw.get("requested_service_tier", ""),
        sandbox_policy_ref_and_hash=dict(raw.get("sandbox_policy_ref_and_hash", {})),
        tool_policy_ref_and_hash=dict(raw.get("tool_policy_ref_and_hash", {})),
        network_policy_ref_and_hash=dict(raw.get("network_policy_ref_and_hash", {})),
        output_schema_ref_and_hash=dict(raw.get("output_schema_ref_and_hash", {})),
        cli_argument_mapping_ref_and_hash=dict(raw.get("cli_argument_mapping_ref_and_hash", {})),
        model_release_or_catalog_snapshot_ref_and_hash=dict(
            raw.get("model_release_or_catalog_snapshot_ref_and_hash", {})
        ),
    )
    return profile, VerificationResult(verdict="PASS")


# ─── JSONL parser ────────────────────────────────────────────────────────


@dataclass(frozen=True)
class JsonlParseResult:
    """Codex JSONL event stream 解析结果。"""

    events: list[dict[str, Any]]
    sequences: list[int]
    has_tool_events: bool
    has_terminal: bool
    provider_id: str
    parse_errors: list[str] = field(default_factory=list)

    @property
    def has_sequence_gap(self) -> bool:
        """检查是否有序号缺口。"""
        if not self.sequences:
            return False
        expected = list(range(self.sequences[0], self.sequences[-1] + 1))
        return self.sequences != expected


def parse_codex_jsonl(raw: str | bytes) -> JsonlParseResult:
    """解析 Codex JSONL event stream 格式。

    JSONL 格式：每行一个 JSON 对象，包含：
    - sequence: int（序号，必须连续）
    - timestamp: str
    - event_type: str（"generation" | "tool" | "terminal" | "usage" | ...）
    - provider_id: str
    - payload: dict

    检查：
    1. 每行是合法 JSON
    2. 有 sequence 字段且连续
    3. 无 tool events（认知角色 NO_TOOLS）
    4. 有 terminal event
    5. 有 provider_id
    """
    parse_errors: list[str] = []

    if isinstance(raw, bytes):
        try:
            raw_str = raw.decode("utf-8")
        except UnicodeDecodeError:
            return JsonlParseResult(
                events=[], sequences=[], has_tool_events=False,
                has_terminal=False, provider_id="",
                parse_errors=["JSONL raw bytes are not valid UTF-8"],
            )
    else:
        raw_str = raw

    lines = raw_str.strip().split("\n") if raw_str.strip() else []
    events: list[dict[str, Any]] = []
    sequences: list[int] = []
    has_tool_events = False
    has_terminal = False
    provider_id = ""

    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            parse_errors.append(f"line {i} JSON parse failed: {exc}")
            continue

        if not isinstance(event, dict):
            parse_errors.append(f"line {i} is not a JSON object")
            continue

        events.append(event)

        seq = event.get("sequence", -1)
        if isinstance(seq, int):
            sequences.append(seq)
        else:
            parse_errors.append(f"line {i} missing or invalid sequence: {seq!r}")

        event_type = event.get("event_type", "")
        if event_type == "tool":
            has_tool_events = True
        if event_type == "terminal":
            has_terminal = True

        if not provider_id:
            provider_id = event.get("provider_id", "")

    if not events:
        parse_errors.append("JSONL stream has no events")

    if not has_terminal:
        parse_errors.append("JSONL stream has no terminal event")

    if sequences and sequences != list(range(sequences[0], sequences[-1] + 1)):
        parse_errors.append("JSONL stream has sequence gap")

    if not provider_id:
        parse_errors.append("JSONL stream has no provider_id")

    return JsonlParseResult(
        events=events,
        sequences=sequences,
        has_tool_events=has_tool_events,
        has_terminal=has_terminal,
        provider_id=provider_id,
        parse_errors=parse_errors,
    )


class JsonlParser:
    """JSONL parser 封装类。"""

    def parse(self, raw: str | bytes) -> JsonlParseResult:
        return parse_codex_jsonl(raw)

    def verify(self, result: JsonlParseResult) -> VerificationResult:
        """验证 JSONL 解析结果。"""
        errors: list[EC] = []
        details: list[str] = []

        for err in result.parse_errors:
            if "sequence gap" in err:
                errors.append(EC.CWC1_JSONL_EVENT_GAP)
            elif "no terminal" in err:
                errors.append(EC.CWC1_JSONL_NO_TERMINAL)
            else:
                errors.append(EC.CWC1_JSONL_PARSE_FAILED)
            details.append(err)

        if result.has_tool_events:
            errors.append(EC.CWC1_JSONL_TOOL_EVENT_DETECTED)
            details.append("JSONL stream contains tool events")

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(
            verdict=verdict, error_codes=errors, details=details,
        )


# ─── CodexExecModelRoleAdapter ───────────────────────────────────────────


@dataclass
class CodexExecModelRoleAdapter:
    """CodexExecModelRoleAdapter — Codex CLI exec 认知角色适配器。

    实现 ModelRolePort 协议。

    SIDE_EFFECT_FREE：dispatch/reattach/cancel/get_receipt 是 stub，
    不调用真实 Codex CLI。纯内存实现。

    可配置行为：
    - registry：用于验证 contract 中的 role_type_id
    - profile：CodexProfile 冻结 profile
    - force_profile_drift：模拟 profile drift（effective ≠ requested）
    - force_tool_events：模拟 tool events（bypass test FAIL）
    - force_solver_harness：模拟使用 solver_harness（bypass test FAIL）
    - force_repo_workspace：模拟使用 repo workspace（bypass test FAIL）
    """

    registry: RoleRegistry = field(default_factory=lambda: ROLE_REGISTRY_FROZEN_V1)
    profile: CodexProfile | None = None
    force_profile_drift: bool = False
    force_tool_events: bool = False
    force_solver_harness: bool = False
    force_repo_workspace: bool = False
    _attempts: dict[str, Attempt] = field(default_factory=dict, repr=False)
    _receipts: dict[str, AttemptReceipt] = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        if self.profile is None:
            zero_ref = {"ref_id": "ref-001", "sha256": "0" * 64}
            self.profile = CodexProfile(
                carrier="codex_exec_cli",
                backend_kind="local_noninteractive_exec",
                requested_model=CODEX_FROZEN_MODEL,
                model_alias_resolution_policy="exact_uid_required",
                requested_reasoning_effort=CODEX_FROZEN_EFFORT,
                requested_reasoning_mode=CODEX_FROZEN_MODE,
                requested_orchestration_mode=CODEX_FROZEN_ORCHESTRATION,
                requested_service_tier="default",
                sandbox_policy_ref_and_hash=dict(zero_ref),
                tool_policy_ref_and_hash=dict(zero_ref),
                network_policy_ref_and_hash=dict(zero_ref),
                output_schema_ref_and_hash=dict(zero_ref),
                cli_argument_mapping_ref_and_hash=dict(zero_ref),
                model_release_or_catalog_snapshot_ref_and_hash=dict(zero_ref),
            )

    # ─── ModelRolePort 协议实现 ───────────────────────────────────────

    def dispatch(self, request: DispatchRequest) -> DispatchResult:
        """提交角色 job（SIDE_EFFECT_FREE stub）。

        状态机：CREATED → ACCEPTED → STARTED → COMPLETED
        不调用真实 Codex CLI。确定性输出。
        """
        # 验证 contract
        contract_result = verify_role_execution_contract(
            request.contract,
            registry=self.registry,
        )
        if not contract_result.passed:
            attempt = Attempt(
                attempt_id=f"codex-attempt-{request.contract.role_job_id}",
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

        attempt_id = f"codex-attempt-{request.contract.role_job_id}"
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

        # CREATED → ACCEPTED
        result = attempt.transition_to(AttemptState.ACCEPTED, timestamp)
        if not result.passed:
            receipt = build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="STATE_TRANSITION_FAILED",
            )
            self._attempts[attempt_id] = attempt
            self._receipts[attempt_id] = receipt
            return DispatchResult(attempt=attempt, receipt=receipt, accepted=False)

        # ACCEPTED → STARTED
        result = attempt.transition_to(AttemptState.STARTED, timestamp)
        if not result.passed:
            receipt = build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="STATE_TRANSITION_FAILED",
            )
            self._attempts[attempt_id] = attempt
            self._receipts[attempt_id] = receipt
            return DispatchResult(attempt=attempt, receipt=receipt, accepted=True)

        # 生成确定性输出（SIDE_EFFECT_FREE，不调用 CLI）
        output_bytes = self._generate_output(request)
        output_hash = hashlib.sha256(output_bytes).hexdigest()
        attempt.output_artifact_hashes = [output_hash]
        attempt.output_sink_ref = request.sink_id
        attempt.output_sink_kind = "RESTRICTED_VAULT"

        # STARTED → COMPLETED
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

        # 构建 receipt — requested/effective model
        requested_model = CODEX_FROZEN_MODEL
        effective_model = CODEX_FROZEN_MODEL
        if self.force_profile_drift:
            effective_model = "wrong-model"

        receipt = build_attempt_receipt(
            attempt=attempt,
            requested_model_uid=requested_model,
            effective_model_uid=effective_model,
            normalized_effort=CODEX_FROZEN_EFFORT,
            effort_observation="UNOBSERVABLE",
            reasoning_mode=CODEX_FROZEN_MODE,
            usage={"input_tokens": 300, "output_tokens": 150},
            usage_completeness="COMPLETE",
        )

        self._attempts[attempt_id] = attempt
        self._receipts[attempt_id] = receipt
        return DispatchResult(attempt=attempt, receipt=receipt, accepted=True)

    def reattach(self, attempt_id: str, fence_token: str) -> AttemptReceipt:
        """重新附加到已有 attempt（SIDE_EFFECT_FREE stub）。"""
        attempt = self._attempts.get(attempt_id)
        if attempt is None:
            fake_attempt = Attempt(
                attempt_id=attempt_id,
                role_job_id="unknown",
                role_type_id="unknown",
                contract_hash="0" * 64,
                carrier_profile_hash="0" * 64,
                adapter_kind="CODEX_EXEC",
                fence_token=fence_token,
                state=AttemptState.CREATED,
            )
            return build_attempt_receipt(
                attempt=fake_attempt,
                failure_or_quarantine_state="ATTEMPT_NOT_FOUND",
            )

        if attempt.fence_token != fence_token:
            return build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="FENCE_TOKEN_MISMATCH",
            )

        if attempt.state == AttemptState.CANCELLED:
            return build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="ATTEMPT_CANCELLED",
            )

        return self._receipts.get(attempt_id, build_attempt_receipt(attempt=attempt))

    def cancel(self, attempt_id: str, fence_token: str) -> AttemptReceipt:
        """取消 attempt（SIDE_EFFECT_FREE stub）。"""
        attempt = self._attempts.get(attempt_id)
        if attempt is None:
            fake_attempt = Attempt(
                attempt_id=attempt_id,
                role_job_id="unknown",
                role_type_id="unknown",
                contract_hash="0" * 64,
                carrier_profile_hash="0" * 64,
                adapter_kind="CODEX_EXEC",
                fence_token=fence_token,
                state=AttemptState.CREATED,
            )
            return build_attempt_receipt(
                attempt=fake_attempt,
                failure_or_quarantine_state="ATTEMPT_NOT_FOUND",
            )

        if attempt.fence_token != fence_token:
            return build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="FENCE_TOKEN_MISMATCH",
            )

        if AttemptState.is_terminal(attempt.state):
            return build_attempt_receipt(
                attempt=attempt,
                failure_or_quarantine_state="ALREADY_TERMINATED",
            )

        timestamp = "2026-08-14T12:00:01Z"
        attempt.transition_to(AttemptState.CANCELLED, timestamp)
        attempt.terminal_reason = "CANCELLED"

        receipt = build_attempt_receipt(
            attempt=attempt,
            requested_model_uid=CODEX_FROZEN_MODEL,
            effective_model_uid=CODEX_FROZEN_MODEL,
            failure_or_quarantine_state="CANCELLED",
        )
        self._receipts[attempt_id] = receipt
        return receipt

    def get_receipt(self, attempt_id: str) -> AttemptReceipt:
        """获取 attempt 的当前 receipt（SIDE_EFFECT_FREE stub）。"""
        attempt = self._attempts.get(attempt_id)
        if attempt is None:
            fake_attempt = Attempt(
                attempt_id=attempt_id,
                role_job_id="unknown",
                role_type_id="unknown",
                contract_hash="0" * 64,
                carrier_profile_hash="0" * 64,
                adapter_kind="CODEX_EXEC",
                fence_token="",
                state=AttemptState.CREATED,
            )
            return build_attempt_receipt(
                attempt=fake_attempt,
                failure_or_quarantine_state="ATTEMPT_NOT_FOUND",
            )
        return self._receipts.get(attempt_id, build_attempt_receipt(attempt=attempt))

    # ─── Capability report ────────────────────────────────────────────

    def build_capability_report(self) -> ProfileCapabilityReport:
        """构建 Codex adapter 的 ProfileCapabilityReport。"""
        requested_profile = self.profile.to_dict() if self.profile else {}

        # effective profile：SIDE_EFFECT_FREE stub，effective = requested
        # 除非 force_profile_drift
        effective_profile = dict(requested_profile)
        if self.force_profile_drift:
            effective_profile["requested_model"] = "wrong-model"
            effective_profile["requested_reasoning_effort"] = "wrong-effort"
            effective_profile["requested_reasoning_mode"] = "wrong-mode"
            effective_profile["requested_orchestration_mode"] = "wrong-orchestration"

        # bypass test metadata
        bypass_metadata = {
            "uses_solver_harness": self.force_solver_harness,
            "solver_harness_ref": "solver_harness" if self.force_solver_harness else "",
            "tool_events": ["tool_call_1"] if self.force_tool_events else [],
            "has_tool_events": self.force_tool_events,
            "uses_repo_workspace": self.force_repo_workspace,
            "workspace_path": "solver_harness/workspace" if self.force_repo_workspace else "",
        }
        bypass_suite = run_bypass_tests(bypass_metadata)

        return build_profile_capability_report(
            adapter_kind="CODEX_EXEC",
            requested_profile=requested_profile,
            effective_profile=effective_profile,
            unobservable_fields=[
                "effective_reasoning_mode",
                "effective_orchestration_mode",
                "effective_effort",
            ],
            tool_policy_ref_and_hash={"ref_id": "tool-policy-no-tools", "sha256": "0" * 64},
            view_policy_ref_and_hash={"ref_id": "view-policy-public", "sha256": "0" * 64},
            bypass_test_results=bypass_suite.to_list(),
        )

    # ─── 内部方法 ─────────────────────────────────────────────────────

    def _generate_output(self, request: DispatchRequest) -> bytes:
        """生成确定性输出（SIDE_EFFECT_FREE，不调用 CLI）。

        output = sha256(canonical_json({
            "adapter_kind": "CODEX_EXEC",
            "input_view_bytes_hash": sha256(input_view_bytes),
            "carrier_profile_hash": carrier_profile_hash,
            "role_type_id": role_type_id,
            "model": gpt-5.6-sol,
        }))
        """
        input_hash = hashlib.sha256(request.input_view_bytes).hexdigest()
        output_payload = {
            "adapter_kind": "CODEX_EXEC",
            "input_view_bytes_hash": input_hash,
            "carrier_profile_hash": request.contract.carrier_profile_ref_and_hash.get("sha256", ""),
            "role_type_id": request.contract.role_type_id,
            "model": CODEX_FROZEN_MODEL,
        }
        output_hash = hashlib.sha256(canonical_json_bytes(output_payload)).hexdigest()
        return output_hash.encode("utf-8")

    def get_output(self, attempt_id: str) -> bytes | None:
        """获取 attempt 的输出 bytes（仅用于测试验证确定性）。"""
        attempt = self._attempts.get(attempt_id)
        if attempt is None or not attempt.output_artifact_hashes:
            return None
        return attempt.output_artifact_hashes[0].encode("utf-8")
