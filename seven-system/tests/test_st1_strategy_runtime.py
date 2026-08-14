"""WP-ST1 Strategy Runtime 测试。

测试层级：Golden → Negative → Fault injection
覆盖：
- FixturePreState (development/activation, fixture masquerade blocker)
- Selector (select/rank/abstain, abstain-not-respected blocker)
- Renderer (bound payload, answer leakage blocker, core/text confusion blocker)
- Binding (position/timing/scope, invalid position/timing blocker)
- Injection (requires binding blocker, before/after state hash)
- Critic (requires injection blocker, HELPED/HURT/NEUTRAL)
- StrategyRuntime (full chain, abstain path, chain integrity)
- ArmPayload (all 7 arms, deterministic replay, distractor equivalence blocker)
- StrategyCapabilityReport
- Blocker tests:
  - fixture masquerading as live Case → FAIL
  - answer bound to hint → FAIL
  - core/text confusion → FAIL
  - distractor not equivalent → FAIL
  - component drift → FAIL
  - no TellStrategyRelease ref → FAIL
  - injection without binding → FAIL
  - critic without injection → FAIL
  - selector abstain not respected → FAIL
- Deterministic hash tests
- Pure program replay verification
- ST1 boundary tests (allowed/forbidden output kinds)
- All constants verified

SIDE_EFFECT_FREE：不接触真实 CLI / DB / D-volume / Solver。
"""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import (
    ST_ALLOWED_OUTPUT_KINDS,
    ST_ARM_KINDS,
    ST_BINDING_KINDS,
    ST_CRITIC_DECISIONS,
    ST_FORBIDDEN_OUTPUT_KINDS,
    ST_FIXTURE_MODES,
    ST_INJECTION_POSITIONS,
    ST_RENDERER_KINDS,
    ST_SELECTOR_DECISIONS,
    ST_SIDE_EFFECT_KEYS,
    ST_STRATEGY_STATES,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.strategy.fixture_pre_state import (
    FixturePreState,
    make_fixture_pre_state,
    verify_fixture_pre_state,
)
from seven_system.strategy.selector import (
    Selector,
    SelectorReceipt,
    make_selector_receipt,
    verify_selector_receipt,
)
from seven_system.strategy.renderer import (
    Renderer,
    RendererReceipt,
    make_renderer_receipt,
    verify_renderer_receipt,
)
from seven_system.strategy.binding import (
    Binder,
    BindingReceipt,
    make_binding_receipt,
    verify_binding_receipt,
    ST_TIMING_KINDS,
)
from seven_system.strategy.injection import (
    Injector,
    InjectionReceipt,
    make_injection_receipt,
    verify_injection_receipt,
)
from seven_system.strategy.critic import (
    Critic,
    CriticDecision,
    make_critic_decision,
    verify_critic_decision,
)
from seven_system.strategy.runtime import (
    StrategyRuntime,
    StrategyRunReceipt,
    make_strategy_run_receipt,
    verify_strategy_run_receipt,
)
from seven_system.strategy.arm_payload import (
    ArmPayload,
    make_arm_payload,
    verify_arm_payload,
    build_arm_payload_set,
)
from seven_system.strategy.capability_report import (
    StrategyCapabilityReport,
    build_strategy_capability_report,
    verify_strategy_capability_report,
    StrategyCapabilityReportError,
    STRATEGY_REPORT_SCHEMA_VERSION,
    STRATEGY_CHECK_IDS,
    STRATEGY_CLAIMS,
    STRATEGY_NONCLAIMS,
)


# ─── helpers ────────────────────────────────────────────────────────────

_ZERO_HASH = "0" * 64
_FAKE_HASH_A = "a" * 64
_FAKE_HASH_B = "b" * 64
_FAKE_HASH_C = "c" * 64

_RELEASE_REF = {"release_id": "rel-tx1-001", "content_hash": _FAKE_HASH_A}
_RENDERER_REF = {"renderer_id": "rdr-001", "version": "v1", "content_hash": _FAKE_HASH_B}
_INJECTION_POLICY_REF = {"policy_id": "inj-pol-001", "version": "v1", "content_hash": _FAKE_HASH_C}
_CRITIC_CONTRACT_REF = {"contract_id": "crt-001", "content_hash": _FAKE_HASH_A}


def _make_valid_fixture(fixture_id: str = "fix-dev-001") -> FixturePreState:
    return make_fixture_pre_state(
        fixture_id=fixture_id,
        mode="DEVELOPMENT",
        is_live_case=False,
        release_ref=_RELEASE_REF,
        problem_context={"problem_ref": "prob-001", "source": "fixture"},
        frozen_at="2026-08-20T12:00:00Z",
    )


# ─── Constants tests ───────────────────────────────────────────────────


class TestST1Constants(unittest.TestCase):
    """验证所有 ST1 常量集合。"""

    def test_arm_kinds_contains_all_arms(self):
        expected = {
            "PROBLEM_ONLY", "LINEAGE", "DIRECTION", "LINEAGE_DIRECTION",
            "DISTRACTOR", "OPERATION_CRITIC", "POSITION_NEUTRAL",
        }
        self.assertEqual(ST_ARM_KINDS, expected)

    def test_selector_decisions(self):
        self.assertEqual(ST_SELECTOR_DECISIONS, {"SELECT", "RANK", "ABSTAIN", "FALLBACK"})

    def test_renderer_kinds(self):
        self.assertEqual(
            ST_RENDERER_KINDS,
            {"HINT_INSTANCE", "LINEAGE_RENDER", "DIRECTION_RENDER", "DISTRACTOR_RENDER"},
        )

    def test_binding_kinds(self):
        self.assertEqual(
            ST_BINDING_KINDS,
            {"POSITION_BINDING", "TIMING_BINDING", "SCOPE_BINDING", "FULL_BINDING"},
        )

    def test_injection_positions(self):
        self.assertEqual(
            ST_INJECTION_POSITIONS,
            {"PRE_TRACE", "AT_BRANCH_POINT", "MID_TRACE", "POST_TRACE"},
        )

    def test_critic_decisions(self):
        self.assertEqual(ST_CRITIC_DECISIONS, {"HELPED", "HURT", "NEUTRAL"})

    def test_strategy_states(self):
        expected = {
            "IDLE", "SELECTED", "RENDERED", "BOUND",
            "INJECTED", "CRITIQUED", "ABSTAINED",
        }
        self.assertEqual(ST_STRATEGY_STATES, expected)

    def test_allowed_output_kinds(self):
        expected = {
            "SelectorReceipt", "RendererReceipt", "BindingReceipt",
            "InjectionReceipt", "CriticDecision", "StrategyRunReceipt",
            "ArmPayload", "FixturePreState", "StrategyCapabilityReport",
        }
        self.assertEqual(ST_ALLOWED_OUTPUT_KINDS, expected)

    def test_forbidden_output_kinds(self):
        # must not overlap with allowed
        self.assertEqual(ST_ALLOWED_OUTPUT_KINDS & ST_FORBIDDEN_OUTPUT_KINDS, set())
        # must contain other WP's outputs
        self.assertIn("DatabaseSchemaStateReport", ST_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("SolverLaunchReceipt", ST_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("TellStrategyRelease", ST_FORBIDDEN_OUTPUT_KINDS)

    def test_side_effect_keys(self):
        expected = (
            "database_writes", "redis_writes", "d_volume_writes",
            "solver_launches", "model_live_calls", "human_gate_commits",
        )
        self.assertEqual(ST_SIDE_EFFECT_KEYS, expected)

    def test_fixture_modes(self):
        self.assertEqual(ST_FIXTURE_MODES, {"DEVELOPMENT", "ACTIVATION"})

    def test_error_codes_exist(self):
        """所有 ST1 错误码必须存在于 VerificationErrorCode 枚举中。"""
        codes = [
            EC.ST_FIXTURE_MASQUERADE_LIVE_CASE,
            EC.ST_ANSWER_BOUND_TO_HINT,
            EC.ST_CORE_TEXT_CONFUSION,
            EC.ST_DISTRACTOR_NOT_EQUIVALENT,
            EC.ST_COMPONENT_DRIFT,
            EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING,
            EC.ST_INJECTION_WITHOUT_BINDING,
            EC.ST_CRITIC_WITHOUT_INJECTION,
            EC.ST_SELECTOR_ABSTAIN_NOT_RESPECTED,
            EC.ST_RENDERER_HASH_MISMATCH,
            EC.ST_BINDING_HASH_MISMATCH,
            EC.ST_INJECTION_HASH_MISMATCH,
            EC.ST_CRITIC_HASH_MISMATCH,
            EC.ST_ARM_PAYLOAD_NOT_REPLAYABLE,
            EC.ST_POSITION_INVALID,
            EC.ST_TIMING_INVALID,
            EC.ST_SELECTOR_KIND_INVALID,
            EC.ST_RENDERER_KIND_INVALID,
            EC.ST_BINDING_KIND_INVALID,
            EC.ST_CRITIC_VERDICT_INVALID,
            EC.ST_ARM_KIND_INVALID,
            EC.ST_STRATEGY_STATE_INVALID,
            EC.ST_OUTPUT_KIND_FORBIDDEN,
        ]
        for code in codes:
            self.assertIsInstance(code, EC)
            self.assertTrue(code.value.startswith("ST_"))


# ─── FixturePreState tests ─────────────────────────────────────────────


class TestFixturePreState(unittest.TestCase):

    def test_valid_development_fixture(self):
        fps = _make_valid_fixture()
        self.assertTrue(fps.is_hash_valid)
        result = verify_fixture_pre_state(fps)
        self.assertTrue(result.passed)
        self.assertEqual(result.fixture_id, "fix-dev-001")

    def test_valid_activation_fixture(self):
        fps = make_fixture_pre_state(
            fixture_id="fix-act-001",
            mode="ACTIVATION",
            is_live_case=False,
            release_ref=_RELEASE_REF,
            branch_snapshot_ref={"case_id": "case-001", "branch_hash": _FAKE_HASH_B},
            frozen_at="2026-08-20T12:00:00Z",
        )
        result = verify_fixture_pre_state(fps)
        self.assertTrue(result.passed)

    def test_blocker_fixture_masquerade_live_case(self):
        """Fixture 冒充 live Case → BLOCK。"""
        fps = make_fixture_pre_state(
            fixture_id="fix-bad-001",
            mode="DEVELOPMENT",
            is_live_case=True,  # blocker!
            release_ref=_RELEASE_REF,
        )
        result = verify_fixture_pre_state(fps)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_FIXTURE_MASQUERADE_LIVE_CASE, result.error_codes)

    def test_blocker_missing_release_ref(self):
        """没有 TellStrategyRelease ref → BLOCK。"""
        fps = make_fixture_pre_state(
            fixture_id="fix-bad-002",
            mode="DEVELOPMENT",
            release_ref={},  # missing!
        )
        result = verify_fixture_pre_state(fps)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING, result.error_codes)

    def test_activation_without_branch_snapshot(self):
        fps = make_fixture_pre_state(
            fixture_id="fix-bad-003",
            mode="ACTIVATION",
            release_ref=_RELEASE_REF,
            branch_snapshot_ref={},  # missing!
        )
        result = verify_fixture_pre_state(fps)
        self.assertFalse(result.passed)

    def test_invalid_mode(self):
        fps = make_fixture_pre_state(
            fixture_id="fix-bad-004",
            mode="INVALID",
            release_ref=_RELEASE_REF,
        )
        result = verify_fixture_pre_state(fps)
        self.assertFalse(result.passed)

    def test_deterministic_hash(self):
        fps1 = _make_valid_fixture("fix-det-001")
        fps2 = _make_valid_fixture("fix-det-001")
        self.assertEqual(fps1.content_hash, fps2.content_hash)

    def test_different_id_different_hash(self):
        fps1 = _make_valid_fixture("fix-a")
        fps2 = _make_valid_fixture("fix-b")
        self.assertNotEqual(fps1.content_hash, fps2.content_hash)


# ─── Selector tests ────────────────────────────────────────────────────


class TestSelector(unittest.TestCase):

    def test_select_golden(self):
        sel = Selector()
        receipt = sel.select(
            receipt_id="sel-001",
            release_ref=_RELEASE_REF,
            candidate_core_ids=("core-1", "core-2"),
            reasoning="selected top candidates",
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(receipt.kind, "SELECT")
        self.assertEqual(receipt.selected_core_ids, ("core-1", "core-2"))
        self.assertTrue(receipt.is_hash_valid)
        result = verify_selector_receipt(
            receipt,
            expected_release_hash=_FAKE_HASH_A,
            expected_component_version=sel.component_version,
        )
        self.assertTrue(result.passed)

    def test_rank_golden(self):
        sel = Selector()
        receipt = sel.rank(
            receipt_id="sel-002",
            release_ref=_RELEASE_REF,
            ranking=("core-2", "core-1"),
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(receipt.kind, "RANK")
        self.assertEqual(receipt.ranking, ("core-2", "core-1"))
        result = verify_selector_receipt(receipt)
        self.assertTrue(result.passed)

    def test_abstain_golden(self):
        sel = Selector()
        receipt = sel.abstain(
            receipt_id="sel-003",
            release_ref=_RELEASE_REF,
            abstain_reason="no suitable candidates",
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(receipt.kind, "ABSTAIN")
        self.assertTrue(receipt.is_abstain)
        self.assertEqual(receipt.selected_core_ids, ())
        result = verify_selector_receipt(receipt)
        self.assertTrue(result.passed)

    def test_blocker_abstain_with_selection(self):
        """abstain 但同时 select → BLOCK。"""
        receipt = make_selector_receipt(
            receipt_id="sel-bad-001",
            release_ref=_RELEASE_REF,
            kind="ABSTAIN",
            selected_core_ids=("core-1",),  # blocker!
            abstain_reason="reason",
        )
        result = verify_selector_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_SELECTOR_ABSTAIN_NOT_RESPECTED, result.error_codes)

    def test_blocker_abstain_without_reason(self):
        receipt = make_selector_receipt(
            receipt_id="sel-bad-002",
            release_ref=_RELEASE_REF,
            kind="ABSTAIN",
            abstain_reason="",  # blocker!
        )
        result = verify_selector_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_SELECTOR_ABSTAIN_NOT_RESPECTED, result.error_codes)

    def test_blocker_missing_release_ref(self):
        receipt = make_selector_receipt(
            receipt_id="sel-bad-003",
            release_ref={},
            kind="SELECT",
            selected_core_ids=("core-1",),
        )
        result = verify_selector_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING, result.error_codes)

    def test_blocker_component_drift(self):
        sel = Selector(component_version="v1")
        receipt = sel.select(
            receipt_id="sel-004",
            release_ref=_RELEASE_REF,
            candidate_core_ids=("core-1",),
        )
        result = verify_selector_receipt(
            receipt,
            expected_component_version="v2",  # mismatch!
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_COMPONENT_DRIFT, result.error_codes)

    def test_blocker_release_hash_drift(self):
        receipt = make_selector_receipt(
            receipt_id="sel-005",
            release_ref=_RELEASE_REF,
            kind="SELECT",
            selected_core_ids=("core-1",),
        )
        result = verify_selector_receipt(
            receipt,
            expected_release_hash=_FAKE_HASH_B,  # mismatch!
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_COMPONENT_DRIFT, result.error_codes)

    def test_invalid_kind(self):
        receipt = make_selector_receipt(
            receipt_id="sel-bad-004",
            release_ref=_RELEASE_REF,
            kind="INVALID",
            selected_core_ids=("core-1",),
        )
        result = verify_selector_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_SELECTOR_KIND_INVALID, result.error_codes)

    def test_select_empty_candidates(self):
        receipt = make_selector_receipt(
            receipt_id="sel-bad-005",
            release_ref=_RELEASE_REF,
            kind="SELECT",
            selected_core_ids=(),  # empty!
        )
        result = verify_selector_receipt(receipt)
        self.assertFalse(result.passed)

    def test_deterministic_hash(self):
        r1 = make_selector_receipt(
            receipt_id="sel-det",
            release_ref=_RELEASE_REF,
            kind="SELECT",
            selected_core_ids=("core-1",),
        )
        r2 = make_selector_receipt(
            receipt_id="sel-det",
            release_ref=_RELEASE_REF,
            kind="SELECT",
            selected_core_ids=("core-1",),
        )
        self.assertEqual(r1.content_hash, r2.content_hash)


# ─── Renderer tests ────────────────────────────────────────────────────


class TestRenderer(unittest.TestCase):

    def test_render_golden(self):
        rnd = Renderer()
        receipt = rnd.render(
            receipt_id="rnd-001",
            release_ref=_RELEASE_REF,
            selector_receipt_id="sel-001",
            renderer_ref=_RENDERER_REF,
            payload={"hint": "consider alternative approach"},
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(receipt.kind, "HINT_INSTANCE")
        self.assertIsNotNone(receipt.hint_instance)
        self.assertTrue(receipt.is_hash_valid)
        result = verify_renderer_receipt(
            receipt,
            expected_release_hash=_FAKE_HASH_A,
            expected_renderer_hash=_FAKE_HASH_B,
            expected_component_version=rnd.component_version,
        )
        self.assertTrue(result.passed)

    def test_blocker_answer_bound_to_hint(self):
        """Answer 泄漏到 hint payload → BLOCK。"""
        rnd = Renderer()
        receipt = rnd.render(
            receipt_id="rnd-bad-001",
            release_ref=_RELEASE_REF,
            selector_receipt_id="sel-001",
            renderer_ref=_RENDERER_REF,
            payload={"hint": "guidance", "answer": "42"},  # answer leakage!
        )
        result = verify_renderer_receipt(
            receipt,
            forbidden_answer_keys={"answer", "solution", "final_answer"},
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_ANSWER_BOUND_TO_HINT, result.error_codes)

    def test_blocker_core_text_confusion(self):
        """TellCore invariant_description 直接作为 text payload → BLOCK。"""
        rnd = Renderer()
        core_desc = "the invariant is that x > 0 for all branches"
        receipt = rnd.render(
            receipt_id="rnd-bad-002",
            release_ref=_RELEASE_REF,
            selector_receipt_id="sel-001",
            renderer_ref=_RENDERER_REF,
            payload={"text": core_desc},  # core/text confusion!
        )
        result = verify_renderer_receipt(
            receipt,
            core_invariant_description=core_desc,
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_CORE_TEXT_CONFUSION, result.error_codes)

    def test_no_core_confusion_when_different(self):
        """payload text 与 core description 不同 → PASS。"""
        rnd = Renderer()
        receipt = rnd.render(
            receipt_id="rnd-002",
            release_ref=_RELEASE_REF,
            selector_receipt_id="sel-001",
            renderer_ref=_RENDERER_REF,
            payload={"text": "consider using substitution method"},
        )
        result = verify_renderer_receipt(
            receipt,
            core_invariant_description="the invariant is that x > 0",
        )
        self.assertTrue(result.passed)

    def test_blocker_missing_release_ref(self):
        rnd = Renderer()
        receipt = rnd.render(
            receipt_id="rnd-bad-003",
            release_ref={},
            selector_receipt_id="sel-001",
            renderer_ref=_RENDERER_REF,
            payload={"hint": "guidance"},
        )
        result = verify_renderer_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING, result.error_codes)

    def test_blocker_renderer_hash_mismatch(self):
        rnd = Renderer()
        receipt = rnd.render(
            receipt_id="rnd-003",
            release_ref=_RELEASE_REF,
            selector_receipt_id="sel-001",
            renderer_ref=_RENDERER_REF,
            payload={"hint": "guidance"},
        )
        result = verify_renderer_receipt(
            receipt,
            expected_renderer_hash=_FAKE_HASH_C,  # mismatch!
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_RENDERER_HASH_MISMATCH, result.error_codes)

    def test_blocker_component_drift(self):
        rnd = Renderer(component_version="v1")
        receipt = rnd.render(
            receipt_id="rnd-004",
            release_ref=_RELEASE_REF,
            selector_receipt_id="sel-001",
            renderer_ref=_RENDERER_REF,
            payload={"hint": "guidance"},
        )
        result = verify_renderer_receipt(
            receipt,
            expected_component_version="v2",
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_COMPONENT_DRIFT, result.error_codes)

    def test_invalid_kind(self):
        receipt = make_renderer_receipt(
            receipt_id="rnd-bad-004",
            release_ref=_RELEASE_REF,
            renderer_ref=_RENDERER_REF,
            kind="INVALID",
            rendered_payload={"hint": "guidance"},
        )
        result = verify_renderer_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_RENDERER_KIND_INVALID, result.error_codes)

    def test_deterministic_hash(self):
        r1 = make_renderer_receipt(
            receipt_id="rnd-det",
            release_ref=_RELEASE_REF,
            renderer_ref=_RENDERER_REF,
            rendered_payload={"hint": "guidance"},
        )
        r2 = make_renderer_receipt(
            receipt_id="rnd-det",
            release_ref=_RELEASE_REF,
            renderer_ref=_RENDERER_REF,
            rendered_payload={"hint": "guidance"},
        )
        self.assertEqual(r1.content_hash, r2.content_hash)


# ─── Binding tests ─────────────────────────────────────────────────────


class TestBinding(unittest.TestCase):

    def test_bind_golden(self):
        binder = Binder()
        receipt = binder.bind(
            receipt_id="bnd-001",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-001",
            hint_instance_id="rnd-001-hint",
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(receipt.kind, "FULL_BINDING")
        self.assertEqual(receipt.position, "PRE_TRACE")
        self.assertTrue(receipt.is_hash_valid)
        result = verify_binding_receipt(
            receipt,
            expected_release_hash=_FAKE_HASH_A,
            expected_component_version=binder.component_version,
        )
        self.assertTrue(result.passed)

    def test_blocker_invalid_position(self):
        receipt = make_binding_receipt(
            receipt_id="bnd-bad-001",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-001",
            hint_instance_id="hint-1",
            position="INVALID_POSITION",
        )
        result = verify_binding_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_POSITION_INVALID, result.error_codes)

    def test_blocker_invalid_timing(self):
        receipt = make_binding_receipt(
            receipt_id="bnd-bad-002",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-001",
            hint_instance_id="hint-1",
            timing="INVALID_TIMING",
        )
        result = verify_binding_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_TIMING_INVALID, result.error_codes)

    def test_blocker_missing_release_ref(self):
        receipt = make_binding_receipt(
            receipt_id="bnd-bad-003",
            release_ref={},
            renderer_receipt_id="rnd-001",
            hint_instance_id="hint-1",
        )
        result = verify_binding_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING, result.error_codes)

    def test_blocker_missing_renderer_ref(self):
        receipt = make_binding_receipt(
            receipt_id="bnd-bad-004",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="",  # missing!
            hint_instance_id="hint-1",
        )
        result = verify_binding_receipt(receipt)
        self.assertFalse(result.passed)

    def test_blocker_component_drift(self):
        binder = Binder(component_version="v1")
        receipt = binder.bind(
            receipt_id="bnd-002",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-001",
            hint_instance_id="hint-1",
        )
        result = verify_binding_receipt(receipt, expected_component_version="v2")
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_COMPONENT_DRIFT, result.error_codes)

    def test_invalid_kind(self):
        receipt = make_binding_receipt(
            receipt_id="bnd-bad-005",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-001",
            hint_instance_id="hint-1",
            kind="INVALID",
        )
        result = verify_binding_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_BINDING_KIND_INVALID, result.error_codes)

    def test_deterministic_hash(self):
        r1 = make_binding_receipt(
            receipt_id="bnd-det",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-001",
            hint_instance_id="hint-1",
        )
        r2 = make_binding_receipt(
            receipt_id="bnd-det",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-001",
            hint_instance_id="hint-1",
        )
        self.assertEqual(r1.content_hash, r2.content_hash)


# ─── Injection tests ───────────────────────────────────────────────────


class TestInjection(unittest.TestCase):

    def test_inject_golden(self):
        inj = Injector()
        receipt = inj.inject(
            receipt_id="inj-001",
            release_ref=_RELEASE_REF,
            binding_receipt_id="bnd-001",
            injection_policy_ref=_INJECTION_POLICY_REF,
            injection_position="PRE_TRACE",
            before_state_hash=_ZERO_HASH,
            after_state_hash="1" * 64,
            injected_payload_hash=_FAKE_HASH_B,
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertTrue(receipt.is_hash_valid)
        result = verify_injection_receipt(
            receipt,
            expected_release_hash=_FAKE_HASH_A,
            expected_policy_hash=_FAKE_HASH_C,
            expected_component_version=inj.component_version,
        )
        self.assertTrue(result.passed)

    def test_blocker_injection_without_binding(self):
        """Injection without binding → BLOCK。"""
        receipt = make_injection_receipt(
            receipt_id="inj-bad-001",
            release_ref=_RELEASE_REF,
            binding_receipt_id="",  # missing!
            injection_policy_ref=_INJECTION_POLICY_REF,
        )
        result = verify_injection_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_INJECTION_WITHOUT_BINDING, result.error_codes)

    def test_blocker_missing_release_ref(self):
        receipt = make_injection_receipt(
            receipt_id="inj-bad-002",
            release_ref={},
            binding_receipt_id="bnd-001",
            injection_policy_ref=_INJECTION_POLICY_REF,
        )
        result = verify_injection_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING, result.error_codes)

    def test_blocker_invalid_position(self):
        receipt = make_injection_receipt(
            receipt_id="inj-bad-003",
            release_ref=_RELEASE_REF,
            binding_receipt_id="bnd-001",
            injection_policy_ref=_INJECTION_POLICY_REF,
            injection_position="INVALID",
        )
        result = verify_injection_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_POSITION_INVALID, result.error_codes)

    def test_blocker_component_drift(self):
        inj = Injector(component_version="v1")
        receipt = inj.inject(
            receipt_id="inj-002",
            release_ref=_RELEASE_REF,
            binding_receipt_id="bnd-001",
            injection_policy_ref=_INJECTION_POLICY_REF,
        )
        result = verify_injection_receipt(receipt, expected_component_version="v2")
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_COMPONENT_DRIFT, result.error_codes)

    def test_missing_state_hashes(self):
        receipt = make_injection_receipt(
            receipt_id="inj-bad-004",
            release_ref=_RELEASE_REF,
            binding_receipt_id="bnd-001",
            injection_policy_ref=_INJECTION_POLICY_REF,
            before_state_hash="",  # missing!
        )
        result = verify_injection_receipt(receipt)
        self.assertFalse(result.passed)

    def test_deterministic_hash(self):
        r1 = make_injection_receipt(
            receipt_id="inj-det",
            release_ref=_RELEASE_REF,
            binding_receipt_id="bnd-001",
            injection_policy_ref=_INJECTION_POLICY_REF,
            before_state_hash=_ZERO_HASH,
            after_state_hash="1" * 64,
        )
        r2 = make_injection_receipt(
            receipt_id="inj-det",
            release_ref=_RELEASE_REF,
            binding_receipt_id="bnd-001",
            injection_policy_ref=_INJECTION_POLICY_REF,
            before_state_hash=_ZERO_HASH,
            after_state_hash="1" * 64,
        )
        self.assertEqual(r1.content_hash, r2.content_hash)


# ─── Critic tests ──────────────────────────────────────────────────────


class TestCritic(unittest.TestCase):

    def test_evaluate_helped(self):
        crt = Critic()
        decision = crt.evaluate(
            critic_id="crt-001",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-001",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            verdict="HELPED",
            evidence=({"metric": "correctness", "delta": 0.3},),
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(decision.verdict, "HELPED")
        self.assertTrue(decision.is_hash_valid)
        result = verify_critic_decision(
            decision,
            expected_release_hash=_FAKE_HASH_A,
            expected_contract_hash=_FAKE_HASH_A,
            expected_component_version=crt.component_version,
        )
        self.assertTrue(result.passed)

    def test_evaluate_hurt(self):
        crt = Critic()
        decision = crt.evaluate(
            critic_id="crt-002",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-001",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            verdict="HURT",
        )
        result = verify_critic_decision(decision)
        self.assertTrue(result.passed)

    def test_evaluate_neutral(self):
        crt = Critic()
        decision = crt.evaluate(
            critic_id="crt-003",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-001",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            verdict="NEUTRAL",
        )
        result = verify_critic_decision(decision)
        self.assertTrue(result.passed)

    def test_blocker_critic_without_injection(self):
        """Critic without injection → BLOCK。"""
        decision = make_critic_decision(
            critic_id="crt-bad-001",
            release_ref=_RELEASE_REF,
            injection_receipt_id="",  # missing!
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            verdict="NEUTRAL",
        )
        result = verify_critic_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_CRITIC_WITHOUT_INJECTION, result.error_codes)

    def test_blocker_missing_release_ref(self):
        decision = make_critic_decision(
            critic_id="crt-bad-002",
            release_ref={},
            injection_receipt_id="inj-001",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
        )
        result = verify_critic_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING, result.error_codes)

    def test_invalid_verdict(self):
        decision = make_critic_decision(
            critic_id="crt-bad-003",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-001",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            verdict="INVALID",
        )
        result = verify_critic_decision(decision)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_CRITIC_VERDICT_INVALID, result.error_codes)

    def test_blocker_component_drift(self):
        crt = Critic(component_version="v1")
        decision = crt.evaluate(
            critic_id="crt-004",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-001",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
        )
        result = verify_critic_decision(decision, expected_component_version="v2")
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_COMPONENT_DRIFT, result.error_codes)

    def test_deterministic_hash(self):
        d1 = make_critic_decision(
            critic_id="crt-det",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-001",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            verdict="NEUTRAL",
        )
        d2 = make_critic_decision(
            critic_id="crt-det",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-001",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            verdict="NEUTRAL",
        )
        self.assertEqual(d1.content_hash, d2.content_hash)


# ─── StrategyRuntime tests ─────────────────────────────────────────────


class TestStrategyRuntime(unittest.TestCase):

    def test_full_chain_golden(self):
        """Golden path: full Selector→Renderer→Binding→Injection→Critic chain."""
        fixture = _make_valid_fixture()
        runtime = StrategyRuntime()
        receipt = runtime.run(
            run_id="run-001",
            fixture=fixture,
            candidate_core_ids=("core-1", "core-2"),
            renderer_ref=_RENDERER_REF,
            injection_policy_ref=_INJECTION_POLICY_REF,
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            rendered_payload={"hint": "consider substitution method"},
            critic_verdict="HELPED",
            critic_evidence=({"metric": "correctness", "delta": 0.2},),
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(receipt.state, "CRITIQUED")
        self.assertIsNotNone(receipt.selector_receipt)
        self.assertIsNotNone(receipt.renderer_receipt)
        self.assertIsNotNone(receipt.binding_receipt)
        self.assertIsNotNone(receipt.injection_receipt)
        self.assertIsNotNone(receipt.critic_decision)
        self.assertTrue(receipt.is_hash_valid)

        result = verify_strategy_run_receipt(
            receipt, expected_release_hash=_FAKE_HASH_A
        )
        self.assertTrue(result.passed)
        self.assertEqual(result.error_codes, [])

    def test_abstain_path(self):
        """Selector abstain path — downstream skipped."""
        fixture = _make_valid_fixture()
        runtime = StrategyRuntime()
        receipt = runtime.run_abstain(
            run_id="run-002",
            fixture=fixture,
            abstain_reason="no suitable Tell candidates in release",
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(receipt.state, "ABSTAINED")
        self.assertTrue(receipt.is_abstain)
        self.assertIsNotNone(receipt.selector_receipt)
        self.assertIsNone(receipt.renderer_receipt)
        self.assertIsNone(receipt.binding_receipt)
        self.assertIsNone(receipt.injection_receipt)
        self.assertIsNone(receipt.critic_decision)

        result = verify_strategy_run_receipt(receipt)
        self.assertTrue(result.passed)

    def test_blocker_abstain_not_respected_in_run(self):
        """abstain but state not ABSTAINED → BLOCK。"""
        sel_receipt = make_selector_receipt(
            receipt_id="run-bad-001-selector",
            release_ref=_RELEASE_REF,
            kind="ABSTAIN",
            abstain_reason="no candidates",
        )
        # state is CRITIQUED but selector abstained
        receipt = make_strategy_run_receipt(
            run_id="run-bad-001",
            release_ref=_RELEASE_REF,
            fixture_id="fix-001",
            state="CRITIQUED",  # should be ABSTAINED!
            selector_receipt=sel_receipt,
        )
        result = verify_strategy_run_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_SELECTOR_ABSTAIN_NOT_RESPECTED, result.error_codes)

    def test_blocker_abstain_with_renderer(self):
        """abstain but renderer_receipt present → BLOCK。"""
        sel_receipt = make_selector_receipt(
            receipt_id="run-bad-002-selector",
            release_ref=_RELEASE_REF,
            kind="ABSTAIN",
            abstain_reason="no candidates",
        )
        rnd_receipt = make_renderer_receipt(
            receipt_id="run-bad-002-renderer",
            release_ref=_RELEASE_REF,
            renderer_ref=_RENDERER_REF,
            rendered_payload={"hint": "guidance"},
        )
        receipt = make_strategy_run_receipt(
            run_id="run-bad-002",
            release_ref=_RELEASE_REF,
            fixture_id="fix-001",
            state="ABSTAINED",
            selector_receipt=sel_receipt,
            renderer_receipt=rnd_receipt,  # should be None!
        )
        result = verify_strategy_run_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_SELECTOR_ABSTAIN_NOT_RESPECTED, result.error_codes)

    def test_blocker_missing_release_ref_in_run(self):
        sel_receipt = make_selector_receipt(
            receipt_id="run-bad-003-selector",
            release_ref={},
            kind="SELECT",
            selected_core_ids=("core-1",),
        )
        receipt = make_strategy_run_receipt(
            run_id="run-bad-003",
            release_ref={},
            fixture_id="fix-001",
            state="CRITIQUED",
            selector_receipt=sel_receipt,
        )
        result = verify_strategy_run_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING, result.error_codes)

    def test_blocker_chain_broken_selector_renderer(self):
        """renderer doesn't reference selector → chain broken."""
        sel_receipt = make_selector_receipt(
            receipt_id="sel-A",
            release_ref=_RELEASE_REF,
            kind="SELECT",
            selected_core_ids=("core-1",),
        )
        rnd_receipt = make_renderer_receipt(
            receipt_id="rnd-A",
            release_ref=_RELEASE_REF,
            selector_receipt_id="sel-B",  # wrong!
            renderer_ref=_RENDERER_REF,
            rendered_payload={"hint": "guidance"},
        )
        bnd_receipt = make_binding_receipt(
            receipt_id="bnd-A",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-A",
            hint_instance_id="hint-A",
        )
        inj_receipt = make_injection_receipt(
            receipt_id="inj-A",
            release_ref=_RELEASE_REF,
            binding_receipt_id="bnd-A",
            injection_policy_ref=_INJECTION_POLICY_REF,
            before_state_hash=_ZERO_HASH,
            after_state_hash="1" * 64,
        )
        crt_decision = make_critic_decision(
            critic_id="crt-A",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-A",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
        )
        receipt = make_strategy_run_receipt(
            run_id="run-bad-004",
            release_ref=_RELEASE_REF,
            fixture_id="fix-001",
            state="CRITIQUED",
            selector_receipt=sel_receipt,
            renderer_receipt=rnd_receipt,
            binding_receipt=bnd_receipt,
            injection_receipt=inj_receipt,
            critic_decision=crt_decision,
        )
        result = verify_strategy_run_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_COMPONENT_DRIFT, result.error_codes)

    def test_blocker_chain_broken_injection_without_binding(self):
        """injection doesn't reference binding → injection without binding."""
        sel_receipt = make_selector_receipt(
            receipt_id="sel-B",
            release_ref=_RELEASE_REF,
            kind="SELECT",
            selected_core_ids=("core-1",),
        )
        rnd_receipt = make_renderer_receipt(
            receipt_id="rnd-B",
            release_ref=_RELEASE_REF,
            selector_receipt_id="sel-B",
            renderer_ref=_RENDERER_REF,
            rendered_payload={"hint": "guidance"},
        )
        bnd_receipt = make_binding_receipt(
            receipt_id="bnd-B",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-B",
            hint_instance_id="hint-B",
        )
        inj_receipt = make_injection_receipt(
            receipt_id="inj-B",
            release_ref=_RELEASE_REF,
            binding_receipt_id="bnd-C",  # wrong!
            injection_policy_ref=_INJECTION_POLICY_REF,
            before_state_hash=_ZERO_HASH,
            after_state_hash="1" * 64,
        )
        crt_decision = make_critic_decision(
            critic_id="crt-B",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-B",
            critic_contract_ref=_CRITIC_CONTRACT_REF,
        )
        receipt = make_strategy_run_receipt(
            run_id="run-bad-005",
            release_ref=_RELEASE_REF,
            fixture_id="fix-001",
            state="CRITIQUED",
            selector_receipt=sel_receipt,
            renderer_receipt=rnd_receipt,
            binding_receipt=bnd_receipt,
            injection_receipt=inj_receipt,
            critic_decision=crt_decision,
        )
        result = verify_strategy_run_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_INJECTION_WITHOUT_BINDING, result.error_codes)

    def test_blocker_chain_broken_critic_without_injection(self):
        """critic doesn't reference injection → critic without injection."""
        sel_receipt = make_selector_receipt(
            receipt_id="sel-C",
            release_ref=_RELEASE_REF,
            kind="SELECT",
            selected_core_ids=("core-1",),
        )
        rnd_receipt = make_renderer_receipt(
            receipt_id="rnd-C",
            release_ref=_RELEASE_REF,
            selector_receipt_id="sel-C",
            renderer_ref=_RENDERER_REF,
            rendered_payload={"hint": "guidance"},
        )
        bnd_receipt = make_binding_receipt(
            receipt_id="bnd-C",
            release_ref=_RELEASE_REF,
            renderer_receipt_id="rnd-C",
            hint_instance_id="hint-C",
        )
        inj_receipt = make_injection_receipt(
            receipt_id="inj-C",
            release_ref=_RELEASE_REF,
            binding_receipt_id="bnd-C",
            injection_policy_ref=_INJECTION_POLICY_REF,
            before_state_hash=_ZERO_HASH,
            after_state_hash="1" * 64,
        )
        crt_decision = make_critic_decision(
            critic_id="crt-C",
            release_ref=_RELEASE_REF,
            injection_receipt_id="inj-D",  # wrong!
            critic_contract_ref=_CRITIC_CONTRACT_REF,
        )
        receipt = make_strategy_run_receipt(
            run_id="run-bad-006",
            release_ref=_RELEASE_REF,
            fixture_id="fix-001",
            state="CRITIQUED",
            selector_receipt=sel_receipt,
            renderer_receipt=rnd_receipt,
            binding_receipt=bnd_receipt,
            injection_receipt=inj_receipt,
            critic_decision=crt_decision,
        )
        result = verify_strategy_run_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_CRITIC_WITHOUT_INJECTION, result.error_codes)

    def test_invalid_state(self):
        receipt = make_strategy_run_receipt(
            run_id="run-bad-007",
            release_ref=_RELEASE_REF,
            state="INVALID",
        )
        result = verify_strategy_run_receipt(receipt)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_STRATEGY_STATE_INVALID, result.error_codes)

    def test_deterministic_replay(self):
        """Pure program replay: same input → same output."""
        fixture = _make_valid_fixture()
        runtime = StrategyRuntime()
        r1 = runtime.run(
            run_id="run-det",
            fixture=fixture,
            candidate_core_ids=("core-1",),
            renderer_ref=_RENDERER_REF,
            injection_policy_ref=_INJECTION_POLICY_REF,
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            rendered_payload={"hint": "guidance"},
            frozen_at="2026-08-20T12:00:00Z",
        )
        r2 = runtime.run(
            run_id="run-det",
            fixture=fixture,
            candidate_core_ids=("core-1",),
            renderer_ref=_RENDERER_REF,
            injection_policy_ref=_INJECTION_POLICY_REF,
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            rendered_payload={"hint": "guidance"},
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(r1.content_hash, r2.content_hash)
        self.assertEqual(
            r1.selector_receipt.content_hash,
            r2.selector_receipt.content_hash,
        )
        self.assertEqual(
            r1.renderer_receipt.content_hash,
            r2.renderer_receipt.content_hash,
        )


# ─── ArmPayload tests ──────────────────────────────────────────────────


class TestArmPayload(unittest.TestCase):

    def test_problem_only_arm(self):
        arm = make_arm_payload(
            arm_id="arm-po",
            arm_kind="PROBLEM_ONLY",
            release_ref=_RELEASE_REF,
            hint_enabled=False,
        )
        self.assertFalse(arm.hint_enabled)
        self.assertTrue(arm.is_hash_valid)
        self.assertTrue(arm.is_replay_hash_valid)
        result = verify_arm_payload(arm, expected_release_hash=_FAKE_HASH_A)
        self.assertTrue(result.passed)

    def test_lineage_arm(self):
        arm = make_arm_payload(
            arm_id="arm-lin",
            arm_kind="LINEAGE",
            release_ref=_RELEASE_REF,
            hint_enabled=True,
            selector_spec={"kind": "SELECT", "hint_type": "lineage"},
        )
        result = verify_arm_payload(arm)
        self.assertTrue(result.passed)

    def test_all_arms_via_build_set(self):
        """All 7 arm payloads deterministic replay."""
        arms = build_arm_payload_set(release_ref=_RELEASE_REF)
        self.assertEqual(set(arms.keys()), ST_ARM_KINDS)
        for arm_kind, arm in arms.items():
            self.assertTrue(arm.is_hash_valid, f"{arm_kind} hash invalid")
            self.assertTrue(arm.is_replay_hash_valid, f"{arm_kind} replay hash invalid")
            result = verify_arm_payload(arm, expected_release_hash=_FAKE_HASH_A)
            self.assertTrue(result.passed, f"{arm_kind} verify failed: {result.details}")

    def test_all_arms_deterministic_replay(self):
        """Same release + same arm spec → same payload."""
        arms1 = build_arm_payload_set(release_ref=_RELEASE_REF)
        arms2 = build_arm_payload_set(release_ref=_RELEASE_REF)
        for arm_kind in ST_ARM_KINDS:
            self.assertEqual(
                arms1[arm_kind].content_hash,
                arms2[arm_kind].content_hash,
                f"{arm_kind} not deterministic",
            )
            self.assertEqual(
                arms1[arm_kind].replay_hash,
                arms2[arm_kind].replay_hash,
                f"{arm_kind} replay not deterministic",
            )

    def test_blocker_distractor_not_equivalent(self):
        """Distractor arm with different budget → BLOCK。"""
        arm = make_arm_payload(
            arm_id="arm-dist-bad",
            arm_kind="DISTRACTOR",
            release_ref=_RELEASE_REF,
            budget_contract={"wallclock_seconds": 300, "max_tokens": 4096, "max_cost_microunits": 0},
            hint_enabled=True,
            selector_spec={"kind": "SELECT"},
        )
        reference = {"wallclock_seconds": 600, "max_tokens": 8192, "max_cost_microunits": 0}
        result = verify_arm_payload(arm, reference_budget=reference)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_DISTRACTOR_NOT_EQUIVALENT, result.error_codes)

    def test_distractor_equivalent_passes(self):
        """Distractor arm with equal budget → PASS。"""
        budget = {"wallclock_seconds": 600, "max_tokens": 8192, "max_cost_microunits": 0}
        arm = make_arm_payload(
            arm_id="arm-dist-ok",
            arm_kind="DISTRACTOR",
            release_ref=_RELEASE_REF,
            budget_contract=budget,
            hint_enabled=True,
            selector_spec={"kind": "SELECT"},
        )
        result = verify_arm_payload(arm, reference_budget=budget)
        self.assertTrue(result.passed)

    def test_blocker_missing_release_ref(self):
        arm = make_arm_payload(
            arm_id="arm-bad-001",
            arm_kind="LINEAGE",
            release_ref={},
            hint_enabled=True,
            selector_spec={"kind": "SELECT"},
        )
        result = verify_arm_payload(arm)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING, result.error_codes)

    def test_blocker_invalid_arm_kind(self):
        arm = make_arm_payload(
            arm_id="arm-bad-002",
            arm_kind="INVALID",
            release_ref=_RELEASE_REF,
            hint_enabled=True,
            selector_spec={"kind": "SELECT"},
        )
        result = verify_arm_payload(arm)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_ARM_KIND_INVALID, result.error_codes)

    def test_blocker_problem_only_with_hint(self):
        """PROBLEM_ONLY with hint_enabled=True → FAIL。"""
        arm = make_arm_payload(
            arm_id="arm-bad-003",
            arm_kind="PROBLEM_ONLY",
            release_ref=_RELEASE_REF,
            hint_enabled=True,  # should be False!
            selector_spec={"kind": "SELECT"},
        )
        result = verify_arm_payload(arm)
        self.assertFalse(result.passed)

    def test_blocker_arm_not_replayable(self):
        """Tampered replay_hash → BLOCK。"""
        arm = make_arm_payload(
            arm_id="arm-bad-004",
            arm_kind="LINEAGE",
            release_ref=_RELEASE_REF,
            hint_enabled=True,
            selector_spec={"kind": "SELECT"},
        )
        # tamper replay_hash
        import dataclasses as dc
        tampered = dc.replace(arm, replay_hash="0" * 64)
        result = verify_arm_payload(tampered)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_ARM_PAYLOAD_NOT_REPLAYABLE, result.error_codes)

    def test_blocker_component_drift(self):
        arm = make_arm_payload(
            arm_id="arm-bad-005",
            arm_kind="LINEAGE",
            release_ref=_RELEASE_REF,
            hint_enabled=True,
            selector_spec={"kind": "SELECT"},
        )
        result = verify_arm_payload(arm, expected_release_hash=_FAKE_HASH_B)
        self.assertFalse(result.passed)
        self.assertIn(EC.ST_COMPONENT_DRIFT, result.error_codes)

    def test_all_arms_share_equal_budget(self):
        """All arms from build_arm_payload_set share equal budget (distractor equivalence)."""
        arms = build_arm_payload_set(release_ref=_RELEASE_REF)
        budgets = [arm.budget_contract for arm in arms.values()]
        for b in budgets:
            self.assertEqual(b, budgets[0])


# ─── StrategyCapabilityReport tests ────────────────────────────────────


class TestStrategyCapabilityReport(unittest.TestCase):

    def _build_report(self) -> dict:
        arms = build_arm_payload_set(release_ref=_RELEASE_REF)
        arm_hashes = {k: v.content_hash for k, v in arms.items()}
        return build_strategy_capability_report(
            release_hash=_FAKE_HASH_A,
            fixture_hash=_FAKE_HASH_B,
            dag_hash=_FAKE_HASH_C,
            arm_payload_hashes=arm_hashes,
            probe_results=[
                {"probe_id": "st1.probe.full_chain", "verdict": "PASS"},
                {"probe_id": "st1.probe.abstain", "verdict": "PASS"},
            ],
            positive_evidence_refs=["ev-st1-001"],
            negative_evidence_refs=["ev-st1-neg-001"],
            residual_risks=["live solver not tested"],
            verifier_identity="st1-impl",
            generated_at="2026-08-20T12:00:00Z",
        )

    def test_build_and_verify_report(self):
        report = self._build_report()
        self.assertEqual(report["report_kind"], "StrategyCapabilityReport")
        self.assertEqual(report["verdict"], "PASS")
        errors = verify_strategy_capability_report(report)
        self.assertEqual(errors, ())

    def test_report_class_wrapper(self):
        report = self._build_report()
        wrapped = StrategyCapabilityReport(report)
        self.assertEqual(wrapped.report_kind, "StrategyCapabilityReport")
        self.assertEqual(wrapped.verdict, "PASS")

    def test_report_invalid_schema_version(self):
        report = self._build_report()
        report["schema_version"] = "wrong"
        errors = verify_strategy_capability_report(report)
        self.assertTrue(any(e[0] == EC.REQUIRED_FIELD_MISSING for e in errors))

    def test_report_forbidden_output_kind(self):
        report = self._build_report()
        report["report_kind"] = "DatabaseSchemaStateReport"
        errors = verify_strategy_capability_report(report)
        self.assertTrue(any(e[0] == EC.ST_OUTPUT_KIND_FORBIDDEN for e in errors))

    def test_report_side_effects_not_zero(self):
        report = self._build_report()
        report["side_effects"]["database_writes"] = 1
        errors = verify_strategy_capability_report(report)
        self.assertTrue(len(errors) > 0)

    def test_report_missing_arm_kind(self):
        report = self._build_report()
        report["arm_kinds"] = ["PROBLEM_ONLY"]  # incomplete
        errors = verify_strategy_capability_report(report)
        self.assertTrue(any(e[0] == EC.ST_ARM_KIND_INVALID for e in errors))

    def test_report_invalid_arm_hash(self):
        report = self._build_report()
        report["arm_payload_hashes"]["LINEAGE"] = "not-a-hash"
        errors = verify_strategy_capability_report(report)
        self.assertTrue(any(e[0] == EC.ST_ARM_PAYLOAD_NOT_REPLAYABLE for e in errors))

    def test_report_check_ids_match(self):
        report = self._build_report()
        check_ids = [c["check_id"] for c in report["checks"]]
        self.assertEqual(check_ids, list(STRATEGY_CHECK_IDS))

    def test_report_claims_match(self):
        report = self._build_report()
        self.assertEqual(set(report["claims"].keys()), set(STRATEGY_CLAIMS))

    def test_report_nonclaims_match(self):
        report = self._build_report()
        self.assertEqual(set(report["explicit_nonclaims"]), set(STRATEGY_NONCLAIMS))

    def test_report_build_raises_on_invalid(self):
        """build should raise if generated report fails verification."""
        with self.assertRaises(StrategyCapabilityReportError):
            build_strategy_capability_report(
                release_hash="not-a-hash",  # invalid
                fixture_hash=_FAKE_HASH_B,
                dag_hash=_FAKE_HASH_C,
                arm_payload_hashes={},
                probe_results=[],
                positive_evidence_refs=[],
                negative_evidence_refs=[],
                residual_risks=[],
                verifier_identity="st1-impl",
            )

    def test_report_schema_version_constant(self):
        self.assertEqual(STRATEGY_REPORT_SCHEMA_VERSION, "st1-strategy-capability-report/v1")


# ─── Boundary tests ────────────────────────────────────────────────────


class TestST1Boundary(unittest.TestCase):

    def test_allowed_output_kinds_disjoint_from_forbidden(self):
        self.assertEqual(ST_ALLOWED_OUTPUT_KINDS & ST_FORBIDDEN_OUTPUT_KINDS, set())

    def test_strategy_report_is_allowed(self):
        self.assertIn("StrategyCapabilityReport", ST_ALLOWED_OUTPUT_KINDS)

    def test_other_wp_reports_are_forbidden(self):
        for kind in (
            "DatabaseSchemaStateReport",
            "SolverLaunchReceipt",
            "QuestionRelease",
            "TaxonomySnapshot",
            "TellStrategyRelease",
        ):
            self.assertIn(kind, ST_FORBIDDEN_OUTPUT_KINDS)

    def test_all_st1_receipts_are_allowed(self):
        for kind in (
            "SelectorReceipt",
            "RendererReceipt",
            "BindingReceipt",
            "InjectionReceipt",
            "CriticDecision",
            "StrategyRunReceipt",
            "ArmPayload",
            "FixturePreState",
        ):
            self.assertIn(kind, ST_ALLOWED_OUTPUT_KINDS)


# ─── Pure program replay verification ──────────────────────────────────


class TestPureProgramReplay(unittest.TestCase):

    def test_full_chain_deterministic_replay(self):
        """Same frozen release + same fixture → same run receipt."""
        fixture = _make_valid_fixture()
        runtime = StrategyRuntime()
        kwargs = dict(
            run_id="run-replay",
            fixture=fixture,
            candidate_core_ids=("core-1", "core-2"),
            renderer_ref=_RENDERER_REF,
            injection_policy_ref=_INJECTION_POLICY_REF,
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            rendered_payload={"hint": "consider substitution"},
            critic_verdict="HELPED",
            critic_evidence=({"metric": "correctness", "delta": 0.2},),
            frozen_at="2026-08-20T12:00:00Z",
        )
        r1 = runtime.run(**kwargs)
        r2 = runtime.run(**kwargs)
        self.assertEqual(r1.content_hash, r2.content_hash)

    def test_abstain_deterministic_replay(self):
        fixture = _make_valid_fixture()
        runtime = StrategyRuntime()
        r1 = runtime.run_abstain(
            run_id="run-abstain-replay",
            fixture=fixture,
            abstain_reason="no candidates",
            frozen_at="2026-08-20T12:00:00Z",
        )
        r2 = runtime.run_abstain(
            run_id="run-abstain-replay",
            fixture=fixture,
            abstain_reason="no candidates",
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertEqual(r1.content_hash, r2.content_hash)

    def test_arm_set_deterministic_replay(self):
        arms1 = build_arm_payload_set(release_ref=_RELEASE_REF)
        arms2 = build_arm_payload_set(release_ref=_RELEASE_REF)
        for arm_kind in ST_ARM_KINDS:
            self.assertEqual(
                arms1[arm_kind].replay_hash,
                arms2[arm_kind].replay_hash,
            )

    def test_different_input_different_output(self):
        fixture = _make_valid_fixture()
        runtime = StrategyRuntime()
        r1 = runtime.run(
            run_id="run-diff",
            fixture=fixture,
            candidate_core_ids=("core-1",),
            renderer_ref=_RENDERER_REF,
            injection_policy_ref=_INJECTION_POLICY_REF,
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            rendered_payload={"hint": "approach A"},
            frozen_at="2026-08-20T12:00:00Z",
        )
        r2 = runtime.run(
            run_id="run-diff",
            fixture=fixture,
            candidate_core_ids=("core-1",),
            renderer_ref=_RENDERER_REF,
            injection_policy_ref=_INJECTION_POLICY_REF,
            critic_contract_ref=_CRITIC_CONTRACT_REF,
            rendered_payload={"hint": "approach B"},  # different!
            frozen_at="2026-08-20T12:00:00Z",
        )
        self.assertNotEqual(r1.content_hash, r2.content_hash)


if __name__ == "__main__":
    unittest.main()
