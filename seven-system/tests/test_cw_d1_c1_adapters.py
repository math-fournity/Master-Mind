"""WP-CW-D1 / WP-CW-C1 adapter 测试。

测试层级：Golden → Negative → Fault injection
覆盖：
- DevinCliModelRoleAdapter profile 解析（glm-5-2 → GLM-5.2 High）
- CodexExecModelRoleAdapter profile 解析（model/effort/mode/orchestration）
- ProfileCapabilityReport with requested/effective/unobservable fields
- ATIF parser 解析 valid trajectory format
- JSONL parser 解析 valid Codex response format
- Bypass tests：solver_harness / tool events / repo workspace
- Negative：wrong model UID, wrong effort, wrong mode, profile mismatch
- Fault：profile drift, unobservable fields handling

所有 blocker test 失败 → 工作包 FAIL。
"""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import (
    BYPASS_TEST_NAMES,
    BYPASS_TEST_RESULTS,
    CODEX_FROZEN_EFFORT,
    CODEX_FROZEN_MODE,
    CODEX_FROZEN_MODEL,
    CODEX_FROZEN_ORCHESTRATION,
    DEVIN_EFFORT_ENCODING,
    DEVIN_FROZEN_EFFORT,
    DEVIN_FROZEN_MODEL_DISPLAY,
    DEVIN_FROZEN_MODEL_UID,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.cognitive.role_registry import ROLE_REGISTRY_FROZEN_V1
from seven_system.cognitive.role_execution_contract import (
    build_role_execution_contract,
)
from seven_system.cognitive.model_role_port import (
    DispatchRequest,
    DispatchResult,
    ModelRolePort,
)
from seven_system.cognitive.attempt import AttemptState
from seven_system.adapters.model_role.devin_adapter import (
    DevinCliModelRoleAdapter,
    DevinProfile,
    parse_devin_profile,
    AtifParser,
    parse_atif_trajectory,
)
from seven_system.adapters.model_role.codex_adapter import (
    CodexExecModelRoleAdapter,
    CodexProfile,
    parse_codex_profile,
    JsonlParser,
    parse_codex_jsonl,
)
from seven_system.adapters.model_role.profile_capability import (
    ProfileCapabilityReport,
    build_profile_capability_report,
    verify_profile_capability_report,
)
from seven_system.adapters.model_role.bypass_tests import (
    BypassTestResult,
    BypassTestSuite,
    run_bypass_tests,
    verify_bypass_test_suite,
)


# ─── helpers ───────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64


def _policy_hash(kind: str, kind_field: str = "view_policy_kind") -> str:
    return hashlib.sha256(canonical_json_bytes({kind_field: kind})).hexdigest()


def _make_ref(ref_id: str, sha256: str = _ZERO_HASH) -> dict[str, str]:
    return {"ref_id": ref_id, "sha256": sha256}


def _make_contract(
    *,
    role_type_id: str = "question_architect",
    adapter_kind: str = "DEVIN_CLI",
    role_job_id: str = "job-001",
) -> "object":
    """构建一个合法的 RoleExecutionContract。"""
    registry = ROLE_REGISTRY_FROZEN_V1
    role_def = registry.get_role(role_type_id)
    vp_kind = role_def.view_policy_kind if role_def else "PUBLIC_ONLY"
    tp_kind = role_def.tool_policy_kind if role_def else "NO_TOOLS"

    return build_role_execution_contract(
        role_job_id=role_job_id,
        epoch_id="epoch-001",
        role_type_registry_ref_and_hash=registry.ref_and_hash,
        role_type_id=role_type_id,
        carrier_profile_ref_and_hash=_make_ref("profile-001"),
        view_policy_ref_and_hash=_make_ref("view-policy-001", _policy_hash(vp_kind, "view_policy_kind")),
        tool_policy_ref_and_hash=_make_ref("tool-policy-001", _policy_hash(tp_kind, "tool_policy_kind")),
        adapter_kind=adapter_kind,
        vault_access_capability_ref_and_hash=_make_ref("vault-cap-001"),
        output_schema_ref_and_hash=_make_ref("output-schema-001"),
        budget_contract_ref_and_hash=_make_ref("budget-001"),
        prompt_release_ref_and_hash=_make_ref("prompt-001"),
        idempotency_key="idem-001",
    )


def _make_dispatch_request(
    *,
    contract=None,
    adapter_kind: str = "DEVIN_CLI",
    input_view_bytes: bytes = b"test input view",
    input_view_id: str = "view-001",
    sink_id: str = "sink-001",
    fence_token: str = "fence-001",
) -> DispatchRequest:
    return DispatchRequest(
        contract=contract or _make_contract(adapter_kind=adapter_kind),
        input_view_bytes=input_view_bytes,
        input_view_id=input_view_id,
        sink_id=sink_id,
        fence_token=fence_token,
    )


def _make_devin_profile_raw(
    *,
    model_uid: str = DEVIN_FROZEN_MODEL_UID,
    effort: str = DEVIN_FROZEN_EFFORT,
    effort_encoding: str = DEVIN_EFFORT_ENCODING,
    carrier: str = "devin_cli",
) -> dict:
    return {
        "carrier": carrier,
        "requested_cli_model_arg": model_uid,
        "normalized_reasoning_effort": effort,
        "effort_encoding": effort_encoding,
        "reasoning_mode_request_semantics": "not_configurable_by_cli",
        "orchestration_request_semantics": "fresh_single_top_level_session",
        "model_catalog_snapshot_ref_and_hash": _make_ref("devin-catalog-001"),
    }


def _make_codex_profile_raw(
    *,
    model: str = CODEX_FROZEN_MODEL,
    effort: str = CODEX_FROZEN_EFFORT,
    mode: str = CODEX_FROZEN_MODE,
    orchestration: str = CODEX_FROZEN_ORCHESTRATION,
    carrier: str = "codex_exec_cli",
    backend_kind: str = "local_noninteractive_exec",
) -> dict:
    return {
        "carrier": carrier,
        "backend_kind": backend_kind,
        "requested_model": model,
        "model_alias_resolution_policy": "exact_uid_required",
        "requested_reasoning_effort": effort,
        "requested_reasoning_mode": mode,
        "requested_orchestration_mode": orchestration,
        "requested_service_tier": "default",
        "sandbox_policy_ref_and_hash": _make_ref("sandbox-001"),
        "tool_policy_ref_and_hash": _make_ref("tool-policy-001"),
        "network_policy_ref_and_hash": _make_ref("network-001"),
        "output_schema_ref_and_hash": _make_ref("output-schema-001"),
        "cli_argument_mapping_ref_and_hash": _make_ref("arg-mapping-001"),
        "model_release_or_catalog_snapshot_ref_and_hash": _make_ref("catalog-001"),
    }


def _make_valid_atif() -> str:
    """构建一个合法的 ATIF trajectory JSON。"""
    return json.dumps({
        "session_id": "devin-session-001",
        "steps": [
            {"step_type": "user", "content": "solve this problem"},
            {"step_type": "assistant", "generation_model": "glm-5-2", "content": "thinking..."},
            {"step_type": "assistant", "generation_model": "glm-5-2", "content": "answer..."},
            {"step_type": "terminal", "event": "completed"},
        ],
    })


def _make_valid_jsonl() -> str:
    """构建一个合法的 Codex JSONL event stream。"""
    lines = [
        json.dumps({"sequence": 0, "timestamp": "2026-08-14T12:00:00Z", "event_type": "generation", "provider_id": "codex-001", "payload": {"text": "thinking"}}),
        json.dumps({"sequence": 1, "timestamp": "2026-08-14T12:00:01Z", "event_type": "generation", "provider_id": "codex-001", "payload": {"text": "answer"}}),
        json.dumps({"sequence": 2, "timestamp": "2026-08-14T12:00:02Z", "event_type": "terminal", "provider_id": "codex-001", "payload": {"reason": "completed"}}),
    ]
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════
# Golden: DevinCliModelRoleAdapter profile parsing
# ═══════════════════════════════════════════════════════════════════════


class TestDevinProfileGolden(unittest.TestCase):
    """Golden: DevinCliModelRoleAdapter profile 解析。"""

    def test_parse_valid_devin_profile(self):
        """合法 Devin profile 解析成功。"""
        raw = _make_devin_profile_raw()
        profile, result = parse_devin_profile(raw)
        self.assertTrue(result.passed, f"parse failed: {result.details}")
        self.assertIsNotNone(profile)
        self.assertEqual(profile.carrier, "devin_cli")
        self.assertEqual(profile.requested_cli_model_arg, DEVIN_FROZEN_MODEL_UID)
        self.assertEqual(profile.normalized_reasoning_effort, DEVIN_FROZEN_EFFORT)
        self.assertEqual(profile.effort_encoding, DEVIN_EFFORT_ENCODING)

    def test_model_uid_is_glm_5_2(self):
        """model UID 是 glm-5-2（GLM-5.2 High）。"""
        raw = _make_devin_profile_raw()
        profile, result = parse_devin_profile(raw)
        self.assertTrue(result.passed)
        self.assertEqual(profile.requested_cli_model_arg, "glm-5-2")

    def test_effort_encoded_in_uid(self):
        """effort 编码在 model UID 中，不是独立 --effort 参数。"""
        raw = _make_devin_profile_raw()
        profile, result = parse_devin_profile(raw)
        self.assertTrue(result.passed)
        self.assertEqual(profile.effort_encoding, "model_uid")
        self.assertEqual(profile.normalized_reasoning_effort, "high")

    def test_default_adapter_profile(self):
        """DevinCliModelRoleAdapter 默认 profile 是 glm-5-2 / high。"""
        adapter = DevinCliModelRoleAdapter()
        self.assertIsNotNone(adapter.profile)
        self.assertEqual(adapter.profile.requested_cli_model_arg, DEVIN_FROZEN_MODEL_UID)
        self.assertEqual(adapter.profile.normalized_reasoning_effort, DEVIN_FROZEN_EFFORT)

    def test_profile_to_dict(self):
        """DevinProfile.to_dict() 返回完整字段。"""
        raw = _make_devin_profile_raw()
        profile, result = parse_devin_profile(raw)
        self.assertTrue(result.passed)
        d = profile.to_dict()
        self.assertEqual(d["carrier"], "devin_cli")
        self.assertEqual(d["requested_cli_model_arg"], "glm-5-2")
        self.assertIn("model_catalog_snapshot_ref_and_hash", d)


# ═══════════════════════════════════════════════════════════════════════
# Golden: CodexExecModelRoleAdapter profile parsing
# ═══════════════════════════════════════════════════════════════════════


class TestCodexProfileGolden(unittest.TestCase):
    """Golden: CodexExecModelRoleAdapter profile 解析。"""

    def test_parse_valid_codex_profile(self):
        """合法 Codex profile 解析成功。"""
        raw = _make_codex_profile_raw()
        profile, result = parse_codex_profile(raw)
        self.assertTrue(result.passed, f"parse failed: {result.details}")
        self.assertIsNotNone(profile)
        self.assertEqual(profile.carrier, "codex_exec_cli")
        self.assertEqual(profile.backend_kind, "local_noninteractive_exec")

    def test_model_effort_mode_orchestration_separately_frozen(self):
        """model / effort / mode / orchestration 分别冻结。"""
        raw = _make_codex_profile_raw()
        profile, result = parse_codex_profile(raw)
        self.assertTrue(result.passed)
        self.assertEqual(profile.requested_model, CODEX_FROZEN_MODEL)
        self.assertEqual(profile.requested_reasoning_effort, CODEX_FROZEN_EFFORT)
        self.assertEqual(profile.requested_reasoning_mode, CODEX_FROZEN_MODE)
        self.assertEqual(profile.requested_orchestration_mode, CODEX_FROZEN_ORCHESTRATION)

    def test_default_adapter_profile(self):
        """CodexExecModelRoleAdapter 默认 profile 是 gpt-5.6-sol / xhigh / standard / single_agent。"""
        adapter = CodexExecModelRoleAdapter()
        self.assertIsNotNone(adapter.profile)
        self.assertEqual(adapter.profile.requested_model, CODEX_FROZEN_MODEL)
        self.assertEqual(adapter.profile.requested_reasoning_effort, CODEX_FROZEN_EFFORT)
        self.assertEqual(adapter.profile.requested_reasoning_mode, CODEX_FROZEN_MODE)
        self.assertEqual(adapter.profile.requested_orchestration_mode, CODEX_FROZEN_ORCHESTRATION)

    def test_profile_to_dict(self):
        """CodexProfile.to_dict() 返回完整字段。"""
        raw = _make_codex_profile_raw()
        profile, result = parse_codex_profile(raw)
        self.assertTrue(result.passed)
        d = profile.to_dict()
        self.assertEqual(d["carrier"], "codex_exec_cli")
        self.assertEqual(d["requested_model"], CODEX_FROZEN_MODEL)
        self.assertIn("cli_argument_mapping_ref_and_hash", d)


# ═══════════════════════════════════════════════════════════════════════
# Golden: ProfileCapabilityReport
# ═══════════════════════════════════════════════════════════════════════


class TestProfileCapabilityReportGolden(unittest.TestCase):
    """Golden: ProfileCapabilityReport with requested/effective/unobservable fields。"""

    def test_build_report_with_all_fields(self):
        """构建包含 requested/effective/unobservable 的完整报告。"""
        report = build_profile_capability_report(
            adapter_kind="DEVIN_CLI",
            requested_profile={"carrier": "devin_cli", "model": "glm-5-2"},
            effective_profile={"carrier": "devin_cli", "model": "glm-5-2"},
            unobservable_fields=["effective_reasoning_mode"],
            tool_policy_ref_and_hash=_make_ref("tool-policy-001"),
            view_policy_ref_and_hash=_make_ref("view-policy-001"),
            bypass_test_results=[
                {"test_name": "direct_devin_bypass", "result": "PASS", "detail": "ok"},
                {"test_name": "tool_event_test", "result": "PASS", "detail": "ok"},
                {"test_name": "repo_workspace_test", "result": "PASS", "detail": "ok"},
            ],
        )
        self.assertEqual(report.adapter_kind, "DEVIN_CLI")
        self.assertEqual(report.requested_profile["model"], "glm-5-2")
        self.assertEqual(report.effective_profile["model"], "glm-5-2")
        self.assertIn("effective_reasoning_mode", report.unobservable_fields)
        self.assertTrue(report.report_hash)

    def test_verify_valid_report(self):
        """合法报告通过验证。"""
        report = build_profile_capability_report(
            adapter_kind="CODEX_EXEC",
            requested_profile={"carrier": "codex_exec_cli", "model": "gpt-5.6-sol"},
            effective_profile={"carrier": "codex_exec_cli", "model": "gpt-5.6-sol"},
            unobservable_fields=["effective_reasoning_mode", "effective_effort"],
            tool_policy_ref_and_hash=_make_ref("tool-policy-001"),
            view_policy_ref_and_hash=_make_ref("view-policy-001"),
            bypass_test_results=[
                {"test_name": "direct_devin_bypass", "result": "PASS", "detail": "ok"},
            ],
        )
        result = verify_profile_capability_report(report)
        self.assertTrue(result.passed, f"verify failed: {result.details}")

    def test_report_hash_is_deterministic(self):
        """相同输入产生相同 report_hash。"""
        kwargs = dict(
            adapter_kind="DEVIN_CLI",
            requested_profile={"model": "glm-5-2"},
            effective_profile={"model": "glm-5-2"},
            unobservable_fields=["effective_reasoning_mode"],
            tool_policy_ref_and_hash=_make_ref("tp-001"),
            view_policy_ref_and_hash=_make_ref("vp-001"),
            bypass_test_results=[{"test_name": "direct_devin_bypass", "result": "PASS", "detail": ""}],
        )
        r1 = build_profile_capability_report(**kwargs)
        r2 = build_profile_capability_report(**kwargs)
        self.assertEqual(r1.report_hash, r2.report_hash)

    def test_devin_adapter_capability_report(self):
        """DevinCliModelRoleAdapter.build_capability_report() 返回合法报告。"""
        adapter = DevinCliModelRoleAdapter()
        report = adapter.build_capability_report()
        self.assertEqual(report.adapter_kind, "DEVIN_CLI")
        result = verify_profile_capability_report(report)
        self.assertTrue(result.passed, f"verify failed: {result.details}")

    def test_codex_adapter_capability_report(self):
        """CodexExecModelRoleAdapter.build_capability_report() 返回合法报告。"""
        adapter = CodexExecModelRoleAdapter()
        report = adapter.build_capability_report()
        self.assertEqual(report.adapter_kind, "CODEX_EXEC")
        result = verify_profile_capability_report(report)
        self.assertTrue(result.passed, f"verify failed: {result.details}")


# ═══════════════════════════════════════════════════════════════════════
# Golden: ATIF parser
# ═══════════════════════════════════════════════════════════════════════


class TestAtifParserGolden(unittest.TestCase):
    """Golden: ATIF parser 解析 valid trajectory format。"""

    def test_parse_valid_trajectory(self):
        """合法 ATIF trajectory 解析成功。"""
        result = parse_atif_trajectory(_make_valid_atif())
        self.assertEqual(len(result.steps), 4)
        self.assertEqual(len(result.generation_model_uids), 2)
        self.assertTrue(result.all_generation_models_match)
        self.assertFalse(result.has_tool_events)
        self.assertEqual(result.terminal_event, "completed")
        self.assertEqual(result.session_id, "devin-session-001")

    def test_atif_parser_verify_pass(self):
        """合法 ATIF 通过 verify。"""
        result = parse_atif_trajectory(_make_valid_atif())
        parser = AtifParser()
        vresult = parser.verify(result)
        self.assertTrue(vresult.passed, f"verify failed: {vresult.details}")

    def test_atif_generation_models_match_glm_5_2(self):
        """所有 generation-bearing step 的 generation_model 匹配 glm-5-2。"""
        result = parse_atif_trajectory(_make_valid_atif())
        for uid in result.generation_model_uids:
            self.assertEqual(uid, DEVIN_FROZEN_MODEL_UID)

    def test_atif_parse_bytes(self):
        """ATIF parser 接受 bytes 输入。"""
        result = parse_atif_trajectory(_make_valid_atif().encode("utf-8"))
        self.assertEqual(len(result.steps), 4)
        self.assertTrue(result.all_generation_models_match)

    def test_atif_no_tool_events(self):
        """合法 ATIF trajectory 无 tool events。"""
        result = parse_atif_trajectory(_make_valid_atif())
        self.assertFalse(result.has_tool_events)


# ═══════════════════════════════════════════════════════════════════════
# Golden: JSONL parser
# ═══════════════════════════════════════════════════════════════════════


class TestJsonlParserGolden(unittest.TestCase):
    """Golden: JSONL parser 解析 valid Codex response format。"""

    def test_parse_valid_jsonl(self):
        """合法 JSONL event stream 解析成功。"""
        result = parse_codex_jsonl(_make_valid_jsonl())
        self.assertEqual(len(result.events), 3)
        self.assertEqual(result.sequences, [0, 1, 2])
        self.assertFalse(result.has_sequence_gap)
        self.assertTrue(result.has_terminal)
        self.assertFalse(result.has_tool_events)
        self.assertEqual(result.provider_id, "codex-001")

    def test_jsonl_parser_verify_pass(self):
        """合法 JSONL 通过 verify。"""
        result = parse_codex_jsonl(_make_valid_jsonl())
        parser = JsonlParser()
        vresult = parser.verify(result)
        self.assertTrue(vresult.passed, f"verify failed: {vresult.details}")

    def test_jsonl_parse_bytes(self):
        """JSONL parser 接受 bytes 输入。"""
        result = parse_codex_jsonl(_make_valid_jsonl().encode("utf-8"))
        self.assertEqual(len(result.events), 3)

    def test_jsonl_no_tool_events(self):
        """合法 JSONL stream 无 tool events。"""
        result = parse_codex_jsonl(_make_valid_jsonl())
        self.assertFalse(result.has_tool_events)

    def test_jsonl_sequences_contiguous(self):
        """JSONL sequence 连续无缺口。"""
        result = parse_codex_jsonl(_make_valid_jsonl())
        self.assertFalse(result.has_sequence_gap)


# ═══════════════════════════════════════════════════════════════════════
# Golden: ModelRolePort protocol implementation
# ═══════════════════════════════════════════════════════════════════════


class TestAdapterProtocolGolden(unittest.TestCase):
    """Golden: adapter 实现 ModelRolePort 协议。"""

    def test_devin_adapter_implements_model_role_port(self):
        """DevinCliModelRoleAdapter 实现 ModelRolePort 协议。"""
        adapter = DevinCliModelRoleAdapter()
        self.assertIsInstance(adapter, ModelRolePort)

    def test_codex_adapter_implements_model_role_port(self):
        """CodexExecModelRoleAdapter 实现 ModelRolePort 协议。"""
        adapter = CodexExecModelRoleAdapter()
        self.assertIsInstance(adapter, ModelRolePort)

    def test_devin_dispatch_completes(self):
        """Devin adapter dispatch 完成 CREATED → COMPLETED。"""
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        result = adapter.dispatch(request)
        self.assertTrue(result.accepted)
        self.assertEqual(result.attempt.state, AttemptState.COMPLETED)
        self.assertEqual(result.receipt.requested_model_uid, DEVIN_FROZEN_MODEL_UID)
        self.assertEqual(result.receipt.effective_model_uid, DEVIN_FROZEN_MODEL_UID)

    def test_codex_dispatch_completes(self):
        """Codex adapter dispatch 完成 CREATED → COMPLETED。"""
        adapter = CodexExecModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="CODEX_EXEC")
        result = adapter.dispatch(request)
        self.assertTrue(result.accepted)
        self.assertEqual(result.attempt.state, AttemptState.COMPLETED)
        self.assertEqual(result.receipt.requested_model_uid, CODEX_FROZEN_MODEL)

    def test_devin_cancel(self):
        """Devin adapter cancel 已终态 attempt → ALREADY_TERMINATED（dispatch 同步完成到 COMPLETED）。"""
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        result = adapter.dispatch(request)
        # dispatch 同步完成到 COMPLETED（终态），cancel 应返回 ALREADY_TERMINATED
        cancel_receipt = adapter.cancel(result.attempt_id, "fence-001")
        self.assertIn("ALREADY_TERMINATED", cancel_receipt.failure_or_quarantine_state)

    def test_codex_cancel(self):
        """Codex adapter cancel 已终态 attempt → ALREADY_TERMINATED（dispatch 同步完成到 COMPLETED）。"""
        adapter = CodexExecModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="CODEX_EXEC")
        result = adapter.dispatch(request)
        # dispatch 同步完成到 COMPLETED（终态），cancel 应返回 ALREADY_TERMINATED
        cancel_receipt = adapter.cancel(result.attempt_id, "fence-001")
        self.assertIn("ALREADY_TERMINATED", cancel_receipt.failure_or_quarantine_state)

    def test_devin_reattach(self):
        """Devin adapter reattach 返回 receipt。"""
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        result = adapter.dispatch(request)
        receipt = adapter.reattach(result.attempt_id, "fence-001")
        self.assertEqual(receipt.attempt_id, result.attempt_id)

    def test_devin_get_receipt(self):
        """Devin adapter get_receipt 返回 receipt。"""
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        result = adapter.dispatch(request)
        receipt = adapter.get_receipt(result.attempt_id)
        self.assertEqual(receipt.attempt_id, result.attempt_id)

    def test_devin_deterministic_output(self):
        """Devin adapter 相同输入产生相同输出（确定性）。"""
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        r1 = adapter.dispatch(request)
        adapter2 = DevinCliModelRoleAdapter()
        r2 = adapter2.dispatch(request)
        self.assertEqual(r1.attempt.output_artifact_hashes, r2.attempt.output_artifact_hashes)


# ═══════════════════════════════════════════════════════════════════════
# Golden: Bypass tests
# ═══════════════════════════════════════════════════════════════════════


class TestBypassTestsGolden(unittest.TestCase):
    """Golden: bypass test 正常通过。"""

    def test_clean_adapter_bypass_tests_pass(self):
        """干净的 adapter metadata 通过全部 bypass test。"""
        metadata = {
            "uses_solver_harness": False,
            "solver_harness_ref": "",
            "tool_events": [],
            "has_tool_events": False,
            "uses_repo_workspace": False,
            "workspace_path": "",
        }
        suite = run_bypass_tests(metadata)
        self.assertTrue(suite.all_pass())
        vresult = verify_bypass_test_suite(suite)
        self.assertTrue(vresult.passed)

    def test_bypass_test_names(self):
        """bypass test 名称在合法枚举中。"""
        metadata = {
            "uses_solver_harness": False,
            "tool_events": [],
            "uses_repo_workspace": False,
        }
        suite = run_bypass_tests(metadata)
        for result in suite.results:
            self.assertIn(result.test_name, BYPASS_TEST_NAMES)

    def test_bypass_test_results_in_enum(self):
        """bypass test 结果在合法枚举中。"""
        metadata = {
            "uses_solver_harness": False,
            "tool_events": [],
            "uses_repo_workspace": False,
        }
        suite = run_bypass_tests(metadata)
        for result in suite.results:
            self.assertIn(result.result, BYPASS_TEST_RESULTS)


# ═══════════════════════════════════════════════════════════════════════
# Negative: Devin profile parsing
# ═══════════════════════════════════════════════════════════════════════


class TestDevinProfileNegative(unittest.TestCase):
    """Negative: Devin profile 解析错误。"""

    def test_wrong_model_uid(self):
        """错误的 model UID → CWD1_MODEL_UID_MISMATCH。"""
        raw = _make_devin_profile_raw(model_uid="wrong-model")
        profile, result = parse_devin_profile(raw)
        self.assertFalse(result.passed)
        self.assertIsNone(profile)
        self.assertIn(EC.CWD1_MODEL_UID_MISMATCH, result.error_codes)

    def test_wrong_effort(self):
        """错误的 effort → CWD1_EFFORT_MISMATCH。"""
        raw = _make_devin_profile_raw(effort="low")
        profile, result = parse_devin_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.CWD1_EFFORT_MISMATCH, result.error_codes)

    def test_wrong_effort_encoding(self):
        """错误的 effort_encoding → CWD1_EFFORT_ENCODING_INVALID。"""
        raw = _make_devin_profile_raw(effort_encoding="separate_param")
        profile, result = parse_devin_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.CWD1_EFFORT_ENCODING_INVALID, result.error_codes)

    def test_wrong_carrier(self):
        """错误的 carrier → PROFILE_ADAPTER_KIND_MISMATCH。"""
        raw = _make_devin_profile_raw(carrier="wrong_carrier")
        profile, result = parse_devin_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.PROFILE_ADAPTER_KIND_MISMATCH, result.error_codes)

    def test_missing_field(self):
        """缺少必需字段 → PROFILE_REQUIRED_FIELD_MISSING。"""
        raw = _make_devin_profile_raw()
        del raw["requested_cli_model_arg"]
        profile, result = parse_devin_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.PROFILE_REQUIRED_FIELD_MISSING, result.error_codes)

    def test_missing_catalog_snapshot(self):
        """缺少 catalog snapshot → CWD1_CATALOG_SNAPSHOT_MISSING。"""
        raw = _make_devin_profile_raw()
        raw["model_catalog_snapshot_ref_and_hash"] = {}
        profile, result = parse_devin_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.CWD1_CATALOG_SNAPSHOT_MISSING, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# Negative: Codex profile parsing
# ═══════════════════════════════════════════════════════════════════════


class TestCodexProfileNegative(unittest.TestCase):
    """Negative: Codex profile 解析错误。"""

    def test_wrong_model(self):
        """错误的 model → CWC1_MODEL_MISMATCH。"""
        raw = _make_codex_profile_raw(model="wrong-model")
        profile, result = parse_codex_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.CWC1_MODEL_MISMATCH, result.error_codes)

    def test_wrong_effort(self):
        """错误的 effort → CWC1_EFFORT_MISMATCH。"""
        raw = _make_codex_profile_raw(effort="low")
        profile, result = parse_codex_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.CWC1_EFFORT_MISMATCH, result.error_codes)

    def test_wrong_mode(self):
        """错误的 mode → CWC1_MODE_MISMATCH。"""
        raw = _make_codex_profile_raw(mode="pro")
        profile, result = parse_codex_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.CWC1_MODE_MISMATCH, result.error_codes)

    def test_wrong_orchestration(self):
        """错误的 orchestration → CWC1_ORCHESTRATION_MISMATCH。"""
        raw = _make_codex_profile_raw(orchestration="multi_agent")
        profile, result = parse_codex_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.CWC1_ORCHESTRATION_MISMATCH, result.error_codes)

    def test_wrong_carrier(self):
        """错误的 carrier → PROFILE_ADAPTER_KIND_MISMATCH。"""
        raw = _make_codex_profile_raw(carrier="wrong_carrier")
        profile, result = parse_codex_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.PROFILE_ADAPTER_KIND_MISMATCH, result.error_codes)

    def test_missing_field(self):
        """缺少必需字段 → PROFILE_REQUIRED_FIELD_MISSING。"""
        raw = _make_codex_profile_raw()
        del raw["requested_model"]
        profile, result = parse_codex_profile(raw)
        self.assertFalse(result.passed)
        self.assertIn(EC.PROFILE_REQUIRED_FIELD_MISSING, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# Negative: Bypass tests must fail
# ═══════════════════════════════════════════════════════════════════════


class TestBypassTestsNegative(unittest.TestCase):
    """Negative: bypass test 必须在违规时 fail。"""

    def test_solver_harness_used_bypass_fails(self):
        """adapter 使用 solver_harness → direct_devin_bypass FAIL。"""
        metadata = {
            "uses_solver_harness": True,
            "solver_harness_ref": "solver_harness/solver_harness.py",
            "tool_events": [],
            "has_tool_events": False,
            "uses_repo_workspace": False,
            "workspace_path": "",
        }
        suite = run_bypass_tests(metadata)
        self.assertFalse(suite.all_pass())
        vresult = verify_bypass_test_suite(suite)
        self.assertFalse(vresult.passed)
        self.assertIn(EC.BYPASS_SOLVER_HARNESS_USED, vresult.error_codes)

    def test_tool_events_bypass_fails(self):
        """output 中有 tool events → tool_event_test FAIL。"""
        metadata = {
            "uses_solver_harness": False,
            "solver_harness_ref": "",
            "tool_events": [{"type": "tool_call", "name": "read_file"}],
            "has_tool_events": True,
            "uses_repo_workspace": False,
            "workspace_path": "",
        }
        suite = run_bypass_tests(metadata)
        self.assertFalse(suite.all_pass())
        vresult = verify_bypass_test_suite(suite)
        self.assertFalse(vresult.passed)
        self.assertIn(EC.BYPASS_TOOL_EVENT_DETECTED, vresult.error_codes)

    def test_repo_workspace_bypass_fails(self):
        """adapter 使用 repo workspace → repo_workspace_test FAIL。"""
        metadata = {
            "uses_solver_harness": False,
            "solver_harness_ref": "",
            "tool_events": [],
            "has_tool_events": False,
            "uses_repo_workspace": True,
            "workspace_path": "solver_harness/workspace",
        }
        suite = run_bypass_tests(metadata)
        self.assertFalse(suite.all_pass())
        vresult = verify_bypass_test_suite(suite)
        self.assertFalse(vresult.passed)
        self.assertIn(EC.BYPASS_REPO_WORKSPACE_USED, vresult.error_codes)

    def test_devin_adapter_force_solver_harness(self):
        """Devin adapter force_solver_harness → capability report bypass FAIL。"""
        adapter = DevinCliModelRoleAdapter(force_solver_harness=True)
        report = adapter.build_capability_report()
        result = verify_profile_capability_report(report)
        self.assertFalse(result.passed)
        self.assertIn(EC.BYPASS_SOLVER_HARNESS_USED, result.error_codes)

    def test_devin_adapter_force_tool_events(self):
        """Devin adapter force_tool_events → capability report bypass FAIL。"""
        adapter = DevinCliModelRoleAdapter(force_tool_events=True)
        report = adapter.build_capability_report()
        result = verify_profile_capability_report(report)
        self.assertFalse(result.passed)
        self.assertIn(EC.BYPASS_TOOL_EVENT_DETECTED, result.error_codes)

    def test_devin_adapter_force_repo_workspace(self):
        """Devin adapter force_repo_workspace → capability report bypass FAIL。"""
        adapter = DevinCliModelRoleAdapter(force_repo_workspace=True)
        report = adapter.build_capability_report()
        result = verify_profile_capability_report(report)
        self.assertFalse(result.passed)
        self.assertIn(EC.BYPASS_REPO_WORKSPACE_USED, result.error_codes)

    def test_codex_adapter_force_solver_harness(self):
        """Codex adapter force_solver_harness → capability report bypass FAIL。"""
        adapter = CodexExecModelRoleAdapter(force_solver_harness=True)
        report = adapter.build_capability_report()
        result = verify_profile_capability_report(report)
        self.assertFalse(result.passed)
        self.assertIn(EC.BYPASS_SOLVER_HARNESS_USED, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# Negative: ATIF / JSONL parser errors
# ═══════════════════════════════════════════════════════════════════════


class TestParserNegative(unittest.TestCase):
    """Negative: parser 错误检测。"""

    def test_atif_tool_events_detected(self):
        """ATIF trajectory 包含 tool events → CWD1_ATIF_TOOL_EVENT_DETECTED。"""
        atif = json.dumps({
            "session_id": "s1",
            "steps": [
                {"step_type": "assistant", "generation_model": "glm-5-2", "content": "ok"},
                {"step_type": "tool", "content": "tool call"},
                {"step_type": "terminal", "event": "completed"},
            ],
        })
        result = parse_atif_trajectory(atif)
        self.assertTrue(result.has_tool_events)
        parser = AtifParser()
        vresult = parser.verify(result)
        self.assertFalse(vresult.passed)
        self.assertIn(EC.CWD1_ATIF_TOOL_EVENT_DETECTED, vresult.error_codes)

    def test_atif_missing_generation_model(self):
        """ATIF generation-bearing step 缺少 generation_model → CWD1_ATIF_GENERATION_MODEL_MISSING。"""
        atif = json.dumps({
            "session_id": "s1",
            "steps": [
                {"step_type": "assistant", "content": "ok"},  # 缺少 generation_model
                {"step_type": "terminal", "event": "completed"},
            ],
        })
        result = parse_atif_trajectory(atif)
        self.assertTrue(result.has_missing_generation_model)
        parser = AtifParser()
        vresult = parser.verify(result)
        self.assertFalse(vresult.passed)
        self.assertIn(EC.CWD1_ATIF_GENERATION_MODEL_MISSING, vresult.error_codes)

    def test_atif_wrong_generation_model(self):
        """ATIF generation_model 不匹配 glm-5-2 → CWD1_MODEL_UID_MISMATCH。"""
        atif = json.dumps({
            "session_id": "s1",
            "steps": [
                {"step_type": "assistant", "generation_model": "wrong-model", "content": "ok"},
                {"step_type": "terminal", "event": "completed"},
            ],
        })
        result = parse_atif_trajectory(atif)
        self.assertFalse(result.all_generation_models_match)
        parser = AtifParser()
        vresult = parser.verify(result)
        self.assertFalse(vresult.passed)
        self.assertIn(EC.CWD1_MODEL_UID_MISMATCH, vresult.error_codes)

    def test_atif_no_terminal(self):
        """ATIF 无 terminal event → CWD1_ATIF_PARSE_FAILED。"""
        atif = json.dumps({
            "session_id": "s1",
            "steps": [
                {"step_type": "assistant", "generation_model": "glm-5-2", "content": "ok"},
            ],
        })
        result = parse_atif_trajectory(atif)
        self.assertFalse(result.terminal_event)
        parser = AtifParser()
        vresult = parser.verify(result)
        self.assertFalse(vresult.passed)

    def test_atif_invalid_json(self):
        """ATIF 非法 JSON → parse 失败。"""
        result = parse_atif_trajectory("not valid json {{{")
        self.assertEqual(len(result.steps), 0)
        self.assertTrue(len(result.parse_errors) > 0)

    def test_jsonl_tool_events_detected(self):
        """JSONL stream 包含 tool events → CWC1_JSONL_TOOL_EVENT_DETECTED。"""
        lines = [
            json.dumps({"sequence": 0, "event_type": "generation", "provider_id": "c1"}),
            json.dumps({"sequence": 1, "event_type": "tool", "provider_id": "c1"}),
            json.dumps({"sequence": 2, "event_type": "terminal", "provider_id": "c1"}),
        ]
        result = parse_codex_jsonl("\n".join(lines))
        self.assertTrue(result.has_tool_events)
        parser = JsonlParser()
        vresult = parser.verify(result)
        self.assertFalse(vresult.passed)
        self.assertIn(EC.CWC1_JSONL_TOOL_EVENT_DETECTED, vresult.error_codes)

    def test_jsonl_sequence_gap(self):
        """JSONL 序号缺口 → CWC1_JSONL_EVENT_GAP。"""
        lines = [
            json.dumps({"sequence": 0, "event_type": "generation", "provider_id": "c1"}),
            json.dumps({"sequence": 2, "event_type": "terminal", "provider_id": "c1"}),  # 跳过 1
        ]
        result = parse_codex_jsonl("\n".join(lines))
        self.assertTrue(result.has_sequence_gap)
        parser = JsonlParser()
        vresult = parser.verify(result)
        self.assertFalse(vresult.passed)
        self.assertIn(EC.CWC1_JSONL_EVENT_GAP, vresult.error_codes)

    def test_jsonl_no_terminal(self):
        """JSONL 无 terminal event → CWC1_JSONL_NO_TERMINAL。"""
        lines = [
            json.dumps({"sequence": 0, "event_type": "generation", "provider_id": "c1"}),
            json.dumps({"sequence": 1, "event_type": "generation", "provider_id": "c1"}),
        ]
        result = parse_codex_jsonl("\n".join(lines))
        self.assertFalse(result.has_terminal)
        parser = JsonlParser()
        vresult = parser.verify(result)
        self.assertFalse(vresult.passed)
        self.assertIn(EC.CWC1_JSONL_NO_TERMINAL, vresult.error_codes)

    def test_jsonl_invalid_line(self):
        """JSONL 包含非法 JSON 行 → parse 失败。"""
        lines = [
            json.dumps({"sequence": 0, "event_type": "generation", "provider_id": "c1"}),
            "not valid json {{{",
            json.dumps({"sequence": 2, "event_type": "terminal", "provider_id": "c1"}),
        ]
        result = parse_codex_jsonl("\n".join(lines))
        self.assertTrue(len(result.parse_errors) > 0)


# ═══════════════════════════════════════════════════════════════════════
# Negative: Profile mismatch
# ═══════════════════════════════════════════════════════════════════════


class TestProfileMismatchNegative(unittest.TestCase):
    """Negative: requested 与 effective profile 不一致。"""

    def test_profile_drift_detected(self):
        """requested ≠ effective → PROFILE_REQUESTED_EFFECTIVE_MISMATCH。"""
        report = build_profile_capability_report(
            adapter_kind="DEVIN_CLI",
            requested_profile={"model": "glm-5-2"},
            effective_profile={"model": "wrong-model"},
            unobservable_fields=[],
            tool_policy_ref_and_hash=_make_ref("tp-001"),
            view_policy_ref_and_hash=_make_ref("vp-001"),
            bypass_test_results=[{"test_name": "direct_devin_bypass", "result": "PASS", "detail": ""}],
        )
        result = verify_profile_capability_report(report)
        self.assertFalse(result.passed)
        self.assertIn(EC.PROFILE_REQUESTED_EFFECTIVE_MISMATCH, result.error_codes)

    def test_unobservable_field_not_in_allowed_set(self):
        """unobservable 字段不在允许列表中 → PROFILE_UNOBSERVABLE_FIELD_NOT_DECLARED。"""
        report = build_profile_capability_report(
            adapter_kind="DEVIN_CLI",
            requested_profile={"model": "glm-5-2"},
            effective_profile={"model": "glm-5-2"},
            unobservable_fields=["some_random_field"],
            tool_policy_ref_and_hash=_make_ref("tp-001"),
            view_policy_ref_and_hash=_make_ref("vp-001"),
            bypass_test_results=[{"test_name": "direct_devin_bypass", "result": "PASS", "detail": ""}],
        )
        result = verify_profile_capability_report(report)
        self.assertFalse(result.passed)
        self.assertIn(EC.PROFILE_UNOBSERVABLE_FIELD_NOT_DECLARED, result.error_codes)

    def test_bypass_fail_in_report(self):
        """capability report 中 bypass test FAIL → 验证失败。"""
        report = build_profile_capability_report(
            adapter_kind="DEVIN_CLI",
            requested_profile={"model": "glm-5-2"},
            effective_profile={"model": "glm-5-2"},
            unobservable_fields=[],
            tool_policy_ref_and_hash=_make_ref("tp-001"),
            view_policy_ref_and_hash=_make_ref("vp-001"),
            bypass_test_results=[
                {"test_name": "direct_devin_bypass", "result": "FAIL", "detail": "uses solver_harness"},
            ],
        )
        result = verify_profile_capability_report(report)
        self.assertFalse(result.passed)

    def test_report_hash_mismatch(self):
        """report_hash 不匹配 → OBJECT_HASH_MISMATCH。"""
        report = build_profile_capability_report(
            adapter_kind="DEVIN_CLI",
            requested_profile={"model": "glm-5-2"},
            effective_profile={"model": "glm-5-2"},
            unobservable_fields=[],
            bypass_test_results=[],
        )
        d = report.to_dict()
        d["report_hash"] = "0" * 64  # 篡改 hash
        result = verify_profile_capability_report(d)
        self.assertFalse(result.passed)
        self.assertIn(EC.OBJECT_HASH_MISMATCH, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# Fault injection: profile drift
# ═══════════════════════════════════════════════════════════════════════


class TestProfileDriftFault(unittest.TestCase):
    """Fault: profile drift (requested ≠ effective)。"""

    def test_devin_force_profile_drift(self):
        """Devin adapter force_profile_drift → receipt effective_model ≠ requested。"""
        adapter = DevinCliModelRoleAdapter(force_profile_drift=True)
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        result = adapter.dispatch(request)
        self.assertTrue(result.accepted)
        self.assertEqual(result.receipt.requested_model_uid, DEVIN_FROZEN_MODEL_UID)
        self.assertNotEqual(result.receipt.effective_model_uid, DEVIN_FROZEN_MODEL_UID)

    def test_devin_force_profile_drift_capability_report(self):
        """Devin adapter force_profile_drift → capability report 验证失败。"""
        adapter = DevinCliModelRoleAdapter(force_profile_drift=True)
        report = adapter.build_capability_report()
        result = verify_profile_capability_report(report)
        self.assertFalse(result.passed)
        self.assertIn(EC.PROFILE_REQUESTED_EFFECTIVE_MISMATCH, result.error_codes)

    def test_codex_force_profile_drift(self):
        """Codex adapter force_profile_drift → receipt effective_model ≠ requested。"""
        adapter = CodexExecModelRoleAdapter(force_profile_drift=True)
        request = _make_dispatch_request(adapter_kind="CODEX_EXEC")
        result = adapter.dispatch(request)
        self.assertTrue(result.accepted)
        self.assertNotEqual(result.receipt.requested_model_uid, result.receipt.effective_model_uid)

    def test_codex_force_profile_drift_capability_report(self):
        """Codex adapter force_profile_drift → capability report 验证失败。"""
        adapter = CodexExecModelRoleAdapter(force_profile_drift=True)
        report = adapter.build_capability_report()
        result = verify_profile_capability_report(report)
        self.assertFalse(result.passed)
        self.assertIn(EC.PROFILE_REQUESTED_EFFECTIVE_MISMATCH, result.error_codes)


# ═══════════════════════════════════════════════════════════════════════
# Fault injection: unobservable fields handling
# ═══════════════════════════════════════════════════════════════════════


class TestUnobservableFieldsFault(unittest.TestCase):
    """Fault: unobservable fields handling。"""

    def test_devin_reasoning_mode_unobservable(self):
        """Devin adapter reasoning_mode 是 UNOBSERVABLE。"""
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        result = adapter.dispatch(request)
        self.assertEqual(result.receipt.reasoning_mode, "UNOBSERVABLE")

    def test_devin_effort_observation_derived_from_uid(self):
        """Devin adapter effort_observation = derived_from_uid。"""
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        result = adapter.dispatch(request)
        self.assertEqual(result.receipt.effort_observation, "derived_from_uid")

    def test_devin_capability_report_declares_unobservable(self):
        """Devin capability report 声明 effective_reasoning_mode 为 unobservable。"""
        adapter = DevinCliModelRoleAdapter()
        report = adapter.build_capability_report()
        self.assertIn("effective_reasoning_mode", report.unobservable_fields)

    def test_codex_capability_report_declares_unobservable(self):
        """Codex capability report 声明多个 unobservable 字段。"""
        adapter = CodexExecModelRoleAdapter()
        report = adapter.build_capability_report()
        self.assertIn("effective_reasoning_mode", report.unobservable_fields)
        self.assertIn("effective_orchestration_mode", report.unobservable_fields)
        self.assertIn("effective_effort", report.unobservable_fields)

    def test_unobservable_field_skipped_in_drift_check(self):
        """unobservable 字段不参与 profile drift 检查。"""
        report = build_profile_capability_report(
            adapter_kind="DEVIN_CLI",
            requested_profile={"effective_reasoning_mode": "requested_mode"},
            effective_profile={"effective_reasoning_mode": "different_mode"},
            unobservable_fields=["effective_reasoning_mode"],
            bypass_test_results=[{"test_name": "direct_devin_bypass", "result": "PASS", "detail": ""}],
        )
        result = verify_profile_capability_report(report)
        # unobservable 字段不检查 drift，所以应该 PASS
        self.assertTrue(result.passed, f"unexpected fail: {result.details}")


# ═══════════════════════════════════════════════════════════════════════
# Fault injection: adapter edge cases
# ═══════════════════════════════════════════════════════════════════════


class TestAdapterEdgeCasesFault(unittest.TestCase):
    """Fault: adapter 边缘情况。"""

    def test_devin_dispatch_not_found_reattach(self):
        """Devin adapter reattach 不存在的 attempt → ATTEMPT_NOT_FOUND。"""
        adapter = DevinCliModelRoleAdapter()
        receipt = adapter.reattach("nonexistent", "fence")
        self.assertIn("ATTEMPT_NOT_FOUND", receipt.failure_or_quarantine_state)

    def test_devin_dispatch_not_found_cancel(self):
        """Devin adapter cancel 不存在的 attempt → ATTEMPT_NOT_FOUND。"""
        adapter = DevinCliModelRoleAdapter()
        receipt = adapter.cancel("nonexistent", "fence")
        self.assertIn("ATTEMPT_NOT_FOUND", receipt.failure_or_quarantine_state)

    def test_devin_dispatch_not_found_get_receipt(self):
        """Devin adapter get_receipt 不存在的 attempt → ATTEMPT_NOT_FOUND。"""
        adapter = DevinCliModelRoleAdapter()
        receipt = adapter.get_receipt("nonexistent")
        self.assertIn("ATTEMPT_NOT_FOUND", receipt.failure_or_quarantine_state)

    def test_devin_fence_token_mismatch_reattach(self):
        """Devin adapter reattach fence token 不匹配 → FENCE_TOKEN_MISMATCH。"""
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI", fence_token="fence-001")
        result = adapter.dispatch(request)
        receipt = adapter.reattach(result.attempt_id, "wrong-fence")
        self.assertIn("FENCE_TOKEN_MISMATCH", receipt.failure_or_quarantine_state)

    def test_devin_cancel_already_terminated(self):
        """Devin adapter cancel 已终态 attempt → ALREADY_TERMINATED。"""
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        result = adapter.dispatch(request)
        # dispatch 后已 COMPLETED，再次 cancel 应 ALREADY_TERMINATED
        receipt = adapter.cancel(result.attempt_id, "fence-001")
        self.assertIn("ALREADY_TERMINATED", receipt.failure_or_quarantine_state)

    def test_codex_dispatch_not_found_reattach(self):
        """Codex adapter reattach 不存在的 attempt → ATTEMPT_NOT_FOUND。"""
        adapter = CodexExecModelRoleAdapter()
        receipt = adapter.reattach("nonexistent", "fence")
        self.assertIn("ATTEMPT_NOT_FOUND", receipt.failure_or_quarantine_state)

    def test_codex_fence_token_mismatch_cancel(self):
        """Codex adapter cancel fence token 不匹配 → FENCE_TOKEN_MISMATCH。"""
        adapter = CodexExecModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="CODEX_EXEC", fence_token="fence-001")
        result = adapter.dispatch(request)
        receipt = adapter.cancel(result.attempt_id, "wrong-fence")
        self.assertIn("FENCE_TOKEN_MISMATCH", receipt.failure_or_quarantine_state)

    def test_devin_contract_invalid(self):
        """Devin adapter contract 验证失败 → CONTRACT_INVALID。"""
        adapter = DevinCliModelRoleAdapter()
        # 使用不存在的 role_type_id
        contract = _make_contract(role_type_id="nonexistent_role", adapter_kind="DEVIN_CLI")
        request = _make_dispatch_request(contract=contract, adapter_kind="DEVIN_CLI")
        result = adapter.dispatch(request)
        self.assertFalse(result.accepted)
        self.assertIn("CONTRACT_INVALID", result.receipt.failure_or_quarantine_state)


# ═══════════════════════════════════════════════════════════════════════
# SIDE_EFFECT_FREE verification
# ═══════════════════════════════════════════════════════════════════════


class TestSideEffectFree(unittest.TestCase):
    """验证 adapter 是 SIDE_EFFECT_FREE。"""

    def test_devin_adapter_no_solver_harness(self):
        """Devin adapter 默认不使用 solver_harness。"""
        adapter = DevinCliModelRoleAdapter()
        report = adapter.build_capability_report()
        for br in report.bypass_test_results:
            if br["test_name"] == "direct_devin_bypass":
                self.assertEqual(br["result"], "PASS")

    def test_codex_adapter_no_solver_harness(self):
        """Codex adapter 默认不使用 solver_harness。"""
        adapter = CodexExecModelRoleAdapter()
        report = adapter.build_capability_report()
        for br in report.bypass_test_results:
            if br["test_name"] == "direct_devin_bypass":
                self.assertEqual(br["result"], "PASS")

    def test_devin_adapter_no_tool_events(self):
        """Devin adapter 默认无 tool events。"""
        adapter = DevinCliModelRoleAdapter()
        report = adapter.build_capability_report()
        for br in report.bypass_test_results:
            if br["test_name"] == "tool_event_test":
                self.assertEqual(br["result"], "PASS")

    def test_devin_adapter_no_repo_workspace(self):
        """Devin adapter 默认不使用 repo workspace。"""
        adapter = DevinCliModelRoleAdapter()
        report = adapter.build_capability_report()
        for br in report.bypass_test_results:
            if br["test_name"] == "repo_workspace_test":
                self.assertEqual(br["result"], "PASS")

    def test_devin_adapter_status_side_effect_free(self):
        """Devin adapter 是 SIDE_EFFECT_FREE（不调用真实 CLI）。"""
        # dispatch 两次相同输入，输出确定性
        adapter = DevinCliModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="DEVIN_CLI")
        r1 = adapter.dispatch(request)
        # 清空后重新 dispatch
        adapter2 = DevinCliModelRoleAdapter()
        r2 = adapter2.dispatch(request)
        self.assertEqual(
            r1.attempt.output_artifact_hashes,
            r2.attempt.output_artifact_hashes,
            "SIDE_EFFECT_FREE: same input must produce same output",
        )

    def test_codex_adapter_deterministic_output(self):
        """Codex adapter 相同输入产生相同输出（确定性）。"""
        adapter1 = CodexExecModelRoleAdapter()
        adapter2 = CodexExecModelRoleAdapter()
        request = _make_dispatch_request(adapter_kind="CODEX_EXEC")
        r1 = adapter1.dispatch(request)
        r2 = adapter2.dispatch(request)
        self.assertEqual(r1.attempt.output_artifact_hashes, r2.attempt.output_artifact_hashes)


if __name__ == "__main__":
    unittest.main()
