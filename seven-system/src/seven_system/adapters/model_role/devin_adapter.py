"""DevinCliModelRoleAdapter — Devin CLI 认知角色适配器（WP-CW-D1）。

来自 docs/implementation/05-execution-ports-and-carriers.md DevinCliModelRoleAdapter 节：

精确候选 profile（2026-08-14 本机只读观察）：
- resolved CLI：devin 3000.4.25 (7e8e528a)
- devin models list 中精确 UID glm-5-2 显示为 GLM-5.2 High
- CLI 没有独立 --effort 参数，High 编码在 model UID 中

冻结 profile：
    carrier: devin_cli
    requested_cli_model_arg: glm-5-2
    normalized_reasoning_effort: high
    effort_encoding: model_uid
    reasoning_mode_request_semantics: not_configurable_by_cli
    orchestration_request_semantics: fresh_single_top_level_session
    model_catalog_snapshot_ref_and_hash: required

ATIF parser：
- 对每个 generation-bearing assistant/model step 记录 generation_model 并核对 glm-5-2
- user/tool/telemetry step 不要求该字段
- 任一 generation-bearing step 缺字段即 UNOBSERVABLE/BLOCK

硬约束（AGENTS.md rule 4）：
- Devin CLI 不专属于 Solver；认知角色统一经 provider-neutral ModelRolePort
- 不得复用 Solver 的 port、workspace、session、AGENTS、能力报告、收据或资源池
- 不得使用 solver_harness 或 Solver workspace

当前状态：SIDE_EFFECT_FREE / IMPLEMENTED_PENDING_EVIDENCE
- 协议 stub、profile 解析、ATIF parser、capability report builder 已实现
- live canary 被 DB1I SchemaState / RT1 Runtime/Reconcile / VLT0 / HG0 激活依赖阻塞
- dispatch/reattach/cancel/get_receipt 是 SIDE_EFFECT_FREE stub，不调用真实 CLI
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    DEVIN_EFFORT_ENCODING,
    DEVIN_FROZEN_EFFORT,
    DEVIN_FROZEN_MODEL_DISPLAY,
    DEVIN_FROZEN_MODEL_UID,
    DEVIN_PROFILE_FIELDS,
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


# ─── Devin profile 解析 ──────────────────────────────────────────────────


@dataclass(frozen=True)
class DevinProfile:
    """Devin CLI 冻结 profile。

    model UID = glm-5-2（GLM-5.2 High），effort 编码在 UID 中。
    """

    carrier: str
    requested_cli_model_arg: str
    normalized_reasoning_effort: str
    effort_encoding: str
    reasoning_mode_request_semantics: str
    orchestration_request_semantics: str
    model_catalog_snapshot_ref_and_hash: dict[str, str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "carrier": self.carrier,
            "requested_cli_model_arg": self.requested_cli_model_arg,
            "normalized_reasoning_effort": self.normalized_reasoning_effort,
            "effort_encoding": self.effort_encoding,
            "reasoning_mode_request_semantics": self.reasoning_mode_request_semantics,
            "orchestration_request_semantics": self.orchestration_request_semantics,
            "model_catalog_snapshot_ref_and_hash": dict(self.model_catalog_snapshot_ref_and_hash),
        }


def parse_devin_profile(raw: dict[str, Any]) -> tuple[DevinProfile | None, VerificationResult]:
    """解析 Devin CLI profile。

    检查：
    1. 所有 DEVIN_PROFILE_FIELDS 存在
    2. carrier == "devin_cli"
    3. requested_cli_model_arg == "glm-5-2"
    4. normalized_reasoning_effort == "high"
    5. effort_encoding == "model_uid"
    6. model_catalog_snapshot_ref_and_hash 结构合法
    """
    errors: list[EC] = []
    details: list[str] = []

    # 1. 所有字段存在
    for field_name in DEVIN_PROFILE_FIELDS:
        if field_name not in raw:
            errors.append(EC.PROFILE_REQUIRED_FIELD_MISSING)
            details.append(f"missing required profile field: {field_name}")

    if errors:
        return None, VerificationResult(
            verdict="FAIL", error_codes=errors, details=details,
        )

    # 2. carrier
    carrier = raw.get("carrier", "")
    if carrier != "devin_cli":
        errors.append(EC.PROFILE_ADAPTER_KIND_MISMATCH)
        details.append(f"carrier must be 'devin_cli', got {carrier!r}")

    # 3. model UID
    model_uid = raw.get("requested_cli_model_arg", "")
    if model_uid != DEVIN_FROZEN_MODEL_UID:
        errors.append(EC.CWD1_MODEL_UID_MISMATCH)
        details.append(
            f"requested_cli_model_arg must be {DEVIN_FROZEN_MODEL_UID!r}, got {model_uid!r}"
        )

    # 4. effort
    effort = raw.get("normalized_reasoning_effort", "")
    if effort != DEVIN_FROZEN_EFFORT:
        errors.append(EC.CWD1_EFFORT_MISMATCH)
        details.append(
            f"normalized_reasoning_effort must be {DEVIN_FROZEN_EFFORT!r}, got {effort!r}"
        )

    # 5. effort_encoding
    effort_encoding = raw.get("effort_encoding", "")
    if effort_encoding != DEVIN_EFFORT_ENCODING:
        errors.append(EC.CWD1_EFFORT_ENCODING_INVALID)
        details.append(
            f"effort_encoding must be {DEVIN_EFFORT_ENCODING!r}, got {effort_encoding!r}"
        )

    # 6. catalog snapshot ref
    catalog_ref = raw.get("model_catalog_snapshot_ref_and_hash", {})
    if not isinstance(catalog_ref, dict):
        errors.append(EC.CWD1_CATALOG_SNAPSHOT_MISSING)
        details.append("model_catalog_snapshot_ref_and_hash is not a dict")
    elif set(catalog_ref.keys()) != {"ref_id", "sha256"}:
        errors.append(EC.CWD1_CATALOG_SNAPSHOT_MISSING)
        details.append("model_catalog_snapshot_ref_and_hash must have ref_id and sha256")

    if errors:
        return None, VerificationResult(
            verdict="FAIL", error_codes=errors, details=details,
        )

    profile = DevinProfile(
        carrier=carrier,
        requested_cli_model_arg=model_uid,
        normalized_reasoning_effort=effort,
        effort_encoding=effort_encoding,
        reasoning_mode_request_semantics=raw.get("reasoning_mode_request_semantics", ""),
        orchestration_request_semantics=raw.get("orchestration_request_semantics", ""),
        model_catalog_snapshot_ref_and_hash=dict(catalog_ref),
    )
    return profile, VerificationResult(verdict="PASS")


# ─── ATIF parser ─────────────────────────────────────────────────────────


@dataclass(frozen=True)
class AtifParseResult:
    """ATIF trajectory 解析结果。"""

    steps: list[dict[str, Any]]
    generation_model_uids: list[str]
    has_tool_events: bool
    session_id: str
    terminal_event: str
    parse_errors: list[str] = field(default_factory=list)

    @property
    def all_generation_models_match(self) -> bool:
        """所有 generation-bearing step 的 generation_model 都匹配 glm-5-2。"""
        return all(uid == DEVIN_FROZEN_MODEL_UID for uid in self.generation_model_uids)

    @property
    def has_missing_generation_model(self) -> bool:
        """是否有 generation-bearing step 缺少 generation_model 字段。"""
        return any(not uid for uid in self.generation_model_uids)


def parse_atif_trajectory(raw: str | bytes) -> AtifParseResult:
    """解析 ATIF trajectory export 格式。

    ATIF 格式是 JSON，包含 steps 数组。每个 step 有：
    - step_type: "assistant" | "user" | "tool" | "telemetry" | "terminal"
    - generation_model: 仅 generation-bearing step（assistant/model）需要
    - content: step 内容

    检查：
    1. JSON 合法
    2. 有 steps 数组
    3. 每个 generation-bearing step 有 generation_model
    4. generation_model 匹配 glm-5-2
    5. 无 tool events（认知角色 NO_TOOLS）
    6. 有 terminal event
    """
    import json

    parse_errors: list[str] = []

    if isinstance(raw, bytes):
        try:
            raw_str = raw.decode("utf-8")
        except UnicodeDecodeError:
            return AtifParseResult(
                steps=[], generation_model_uids=[], has_tool_events=False,
                session_id="", terminal_event="",
                parse_errors=["ATIF raw bytes are not valid UTF-8"],
            )
    else:
        raw_str = raw

    try:
        data = json.loads(raw_str)
    except json.JSONDecodeError as exc:
        return AtifParseResult(
            steps=[], generation_model_uids=[], has_tool_events=False,
            session_id="", terminal_event="",
            parse_errors=[f"ATIF JSON parse failed: {exc}"],
        )

    if not isinstance(data, dict):
        return AtifParseResult(
            steps=[], generation_model_uids=[], has_tool_events=False,
            session_id="", terminal_event="",
            parse_errors=["ATIF top-level is not a JSON object"],
        )

    steps = data.get("steps", [])
    if not isinstance(steps, list):
        return AtifParseResult(
            steps=[], generation_model_uids=[], has_tool_events=False,
            session_id="", terminal_event="",
            parse_errors=["ATIF 'steps' is not a list"],
        )

    session_id = data.get("session_id", "")
    if not isinstance(session_id, str):
        parse_errors.append("ATIF session_id is not a string")
        session_id = ""

    generation_model_uids: list[str] = []
    has_tool_events = False
    terminal_event = ""

    for i, step in enumerate(steps):
        if not isinstance(step, dict):
            parse_errors.append(f"step {i} is not a dict")
            continue

        step_type = step.get("step_type", "")

        # generation-bearing step: assistant / model
        if step_type in ("assistant", "model"):
            gen_model = step.get("generation_model", "")
            generation_model_uids.append(gen_model)
            if not gen_model:
                parse_errors.append(
                    f"step {i} (generation-bearing {step_type}) missing generation_model"
                )

        # tool events 检测
        if step_type == "tool":
            has_tool_events = True

        # terminal event
        if step_type == "terminal":
            terminal_event = step.get("event", "")

    if not terminal_event:
        parse_errors.append("ATIF trajectory has no terminal event")

    return AtifParseResult(
        steps=steps,
        generation_model_uids=generation_model_uids,
        has_tool_events=has_tool_events,
        session_id=session_id,
        terminal_event=terminal_event,
        parse_errors=parse_errors,
    )


class AtifParser:
    """ATIF parser 封装类。"""

    def parse(self, raw: str | bytes) -> AtifParseResult:
        return parse_atif_trajectory(raw)

    def verify(self, result: AtifParseResult) -> VerificationResult:
        """验证 ATIF 解析结果。"""
        errors: list[EC] = []
        details: list[str] = []

        for err in result.parse_errors:
            if "missing generation_model" in err:
                errors.append(EC.CWD1_ATIF_GENERATION_MODEL_MISSING)
            else:
                errors.append(EC.CWD1_ATIF_PARSE_FAILED)
            details.append(err)

        if result.has_tool_events:
            errors.append(EC.CWD1_ATIF_TOOL_EVENT_DETECTED)
            details.append("ATIF trajectory contains tool events")

        if not result.terminal_event:
            errors.append(EC.CWD1_ATIF_PARSE_FAILED)
            details.append("ATIF trajectory has no terminal event")

        if not result.all_generation_models_match and not result.has_missing_generation_model:
            errors.append(EC.CWD1_MODEL_UID_MISMATCH)
            mismatched = [uid for uid in result.generation_model_uids
                          if uid != DEVIN_FROZEN_MODEL_UID]
            details.append(
                f"generation_model mismatch: expected {DEVIN_FROZEN_MODEL_UID}, "
                f"got {mismatched}"
            )

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(
            verdict=verdict, error_codes=errors, details=details,
        )


# ─── DevinCliModelRoleAdapter ────────────────────────────────────────────


@dataclass
class DevinCliModelRoleAdapter:
    """DevinCliModelRoleAdapter — Devin CLI 认知角色适配器。

    实现 ModelRolePort 协议。

    SIDE_EFFECT_FREE：dispatch/reattach/cancel/get_receipt 是 stub，
    不调用真实 Devin CLI。纯内存实现。

    可配置行为：
    - registry：用于验证 contract 中的 role_type_id
    - profile：DevinProfile 冻结 profile
    - force_profile_drift：模拟 profile drift（effective ≠ requested）
    - force_tool_events：模拟 tool events（bypass test FAIL）
    - force_solver_harness：模拟使用 solver_harness（bypass test FAIL）
    - force_repo_workspace：模拟使用 repo workspace（bypass test FAIL）
    """

    registry: RoleRegistry = field(default_factory=lambda: ROLE_REGISTRY_FROZEN_V1)
    profile: DevinProfile | None = None
    force_profile_drift: bool = False
    force_tool_events: bool = False
    force_solver_harness: bool = False
    force_repo_workspace: bool = False
    _attempts: dict[str, Attempt] = field(default_factory=dict, repr=False)
    _receipts: dict[str, AttemptReceipt] = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        if self.profile is None:
            # 默认冻结 profile
            self.profile = DevinProfile(
                carrier="devin_cli",
                requested_cli_model_arg=DEVIN_FROZEN_MODEL_UID,
                normalized_reasoning_effort=DEVIN_FROZEN_EFFORT,
                effort_encoding=DEVIN_EFFORT_ENCODING,
                reasoning_mode_request_semantics="not_configurable_by_cli",
                orchestration_request_semantics="fresh_single_top_level_session",
                model_catalog_snapshot_ref_and_hash={
                    "ref_id": "devin-catalog-snapshot-001",
                    "sha256": "0" * 64,
                },
            )

    # ─── ModelRolePort 协议实现 ───────────────────────────────────────

    def dispatch(self, request: DispatchRequest) -> DispatchResult:
        """提交角色 job（SIDE_EFFECT_FREE stub）。

        状态机：CREATED → ACCEPTED → STARTED → COMPLETED
        不调用真实 Devin CLI。确定性输出。
        """
        # 验证 contract
        contract_result = verify_role_execution_contract(
            request.contract,
            registry=self.registry,
        )
        if not contract_result.passed:
            attempt = Attempt(
                attempt_id=f"devin-attempt-{request.contract.role_job_id}",
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

        attempt_id = f"devin-attempt-{request.contract.role_job_id}"
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
        requested_model = DEVIN_FROZEN_MODEL_UID
        effective_model = DEVIN_FROZEN_MODEL_UID
        if self.force_profile_drift:
            effective_model = "wrong-model-uid"

        receipt = build_attempt_receipt(
            attempt=attempt,
            requested_model_uid=requested_model,
            effective_model_uid=effective_model,
            normalized_effort=DEVIN_FROZEN_EFFORT,
            effort_observation="derived_from_uid",
            reasoning_mode="UNOBSERVABLE",
            usage={"input_tokens": 200, "output_tokens": 100},
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
                adapter_kind="DEVIN_CLI",
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
                adapter_kind="DEVIN_CLI",
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
            requested_model_uid=DEVIN_FROZEN_MODEL_UID,
            effective_model_uid=DEVIN_FROZEN_MODEL_UID,
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
                adapter_kind="DEVIN_CLI",
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
        """构建 Devin adapter 的 ProfileCapabilityReport。"""
        requested_profile = self.profile.to_dict() if self.profile else {}

        # effective profile：SIDE_EFFECT_FREE stub，effective = requested
        # 除非 force_profile_drift
        effective_profile = dict(requested_profile)
        if self.force_profile_drift:
            effective_profile["requested_cli_model_arg"] = "wrong-model-uid"

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
            adapter_kind="DEVIN_CLI",
            requested_profile=requested_profile,
            effective_profile=effective_profile,
            unobservable_fields=["effective_reasoning_mode"],
            tool_policy_ref_and_hash={"ref_id": "tool-policy-no-tools", "sha256": "0" * 64},
            view_policy_ref_and_hash={"ref_id": "view-policy-public", "sha256": "0" * 64},
            bypass_test_results=bypass_suite.to_list(),
        )

    # ─── 内部方法 ─────────────────────────────────────────────────────

    def _generate_output(self, request: DispatchRequest) -> bytes:
        """生成确定性输出（SIDE_EFFECT_FREE，不调用 CLI）。

        output = sha256(canonical_json({
            "adapter_kind": "DEVIN_CLI",
            "input_view_bytes_hash": sha256(input_view_bytes),
            "carrier_profile_hash": carrier_profile_hash,
            "role_type_id": role_type_id,
            "model_uid": glm-5-2,
        }))
        """
        input_hash = hashlib.sha256(request.input_view_bytes).hexdigest()
        output_payload = {
            "adapter_kind": "DEVIN_CLI",
            "input_view_bytes_hash": input_hash,
            "carrier_profile_hash": request.contract.carrier_profile_ref_and_hash.get("sha256", ""),
            "role_type_id": request.contract.role_type_id,
            "model_uid": DEVIN_FROZEN_MODEL_UID,
        }
        output_hash = hashlib.sha256(canonical_json_bytes(output_payload)).hexdigest()
        return output_hash.encode("utf-8")

    def get_output(self, attempt_id: str) -> bytes | None:
        """获取 attempt 的输出 bytes（仅用于测试验证确定性）。"""
        attempt = self._attempts.get(attempt_id)
        if attempt is None or not attempt.output_artifact_hashes:
            return None
        # SIDE_EFFECT_FREE：输出是确定性 hash，不是真实 CLI 输出
        return attempt.output_artifact_hashes[0].encode("utf-8")
