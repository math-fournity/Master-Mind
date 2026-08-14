"""WP-EX1 P4/P5 Experiment 测试。

测试层级：Golden → Negative → Fault injection
覆盖：
- ResourceContract (equal-resource, frozen, hash)
- BranchSnapshot (shared pre-treatment state, frozen, hash)
- RandomizationPlan (deterministic replay, same seed → same assignment)
- ExperimentArm (all 7 arm kinds, refs required)
- ContrastSpec (pre-registered, arms found, metric)
- ExperimentPlan (frozen, immutable, all arms, equal resource, contrasts)
- RunArtifactBundle (sealed per arm, references, termination, observability)
- P5ExperimentRunner (golden path, all arms collected, bundles sealed)
- ExperimentCapabilityReport
- Blocker tests:
  - budget exceeded → BLOCK
  - baseline truncated → BLOCK
  - plan modified after start → BLOCK
  - arms not equal-resource → BLOCK
  - negative result deleted → BLOCK
  - invalid result deleted → BLOCK
  - randomization not replayable → BLOCK
  - missing CasePack/StrategyRelease ref → BLOCK
  - contrast not pre-registered → BLOCK
- Deterministic hash tests
- EX1 boundary tests (allowed/forbidden output kinds)
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
    EX_ALLOWED_OUTPUT_KINDS,
    EX_ARM_KINDS,
    EX_CHECK_IDS,
    EX_CLAIMS,
    EX_CONTRAST_KINDS,
    EX_FORBIDDEN_OUTPUT_KINDS,
    EX_NONCLAIMS,
    EX_OBSERVABILITY_STATUSES,
    EX_PLAN_STATES,
    EX_PURPOSE_KINDS,
    EX_RUN_STATES,
    EX_SIDE_EFFECT_KEYS,
    EX_TERMINATION_REASONS,
    VerificationErrorCode as EC,
)
from seven_system.hashing import canonical_json_bytes
from seven_system.experiment.resource_contract import (
    ResourceContract,
    make_resource_contract,
    verify_resource_contract,
    contracts_equal,
)
from seven_system.experiment.branch_snapshot import (
    BranchSnapshot,
    make_branch_snapshot,
    verify_branch_snapshot,
)
from seven_system.experiment.randomization_plan import (
    RandomizationPlan,
    make_randomization_plan,
    verify_randomization_plan,
    replay_randomization,
)
from seven_system.experiment.experiment_arm import (
    ExperimentArm,
    make_experiment_arm,
    verify_experiment_arm,
)
from seven_system.experiment.contrast_spec import (
    ContrastSpec,
    make_contrast_spec,
    verify_contrast_spec,
)
from seven_system.experiment.experiment_plan import (
    ExperimentPlan,
    make_experiment_plan,
    verify_experiment_plan,
    check_plan_modified_after_start,
)
from seven_system.experiment.run_artifact_bundle import (
    RunArtifactBundle,
    make_run_artifact_bundle,
    verify_run_artifact_bundle,
)
from seven_system.experiment.p5_runner import (
    P5ExperimentRunner,
    P5ExperimentRunResult,
    verify_p5_run_result,
)
from seven_system.experiment.capability_report import (
    ExperimentCapabilityReport,
    build_experiment_capability_report,
    verify_experiment_capability_report,
    ExperimentCapabilityReportError,
    EXPERIMENT_REPORT_SCHEMA_VERSION,
)
from seven_system.strategy.arm_payload import build_arm_payload_set


# ─── Test helpers ────────────────────────────────────────────────────────

_FAKE_RELEASE_REF = {
    "release_id": "release-test-001",
    "content_hash": hashlib.sha256(b"fake-release-content").hexdigest(),
}
_FAKE_CASE_PACK_REF = {
    "pack_id": "case-pack-test-001",
    "content_hash": hashlib.sha256(b"fake-case-pack-content").hexdigest(),
}


def _make_test_resource_contract() -> ResourceContract:
    return make_resource_contract(
        contract_id="rc-test-001",
        token_budget=8192,
        wallclock_seconds=600,
        tool_budget=0,
        call_budget=1,
        cost_microunits=0,
    )


def _make_test_branch_snapshot() -> BranchSnapshot:
    return make_branch_snapshot(
        snapshot_id="bs-test-001",
        case_pack_ref=_FAKE_CASE_PACK_REF,
        pre_treatment_state={"problem_context": "test problem"},
    )


def _make_test_randomization_plan(seed: int = 42) -> RandomizationPlan:
    return make_randomization_plan(
        plan_id="rp-test-001",
        seed=seed,
        arm_kinds=sorted(EX_ARM_KINDS),
    )


def _make_test_arm(
    arm_kind: str,
    rc: ResourceContract,
    bs: BranchSnapshot,
    rp: RandomizationPlan,
    arm_payload_ref: dict[str, str] | None = None,
) -> ExperimentArm:
    assignment = rp.replay_assignment().get(arm_kind, 0)
    return make_experiment_arm(
        arm_id=f"arm-{arm_kind}",
        arm_kind=arm_kind,
        case_pack_ref=_FAKE_CASE_PACK_REF,
        strategy_release_ref=_FAKE_RELEASE_REF,
        arm_payload_ref=arm_payload_ref or {
            "arm_id": f"payload-{arm_kind}",
            "content_hash": hashlib.sha256(f"payload-{arm_kind}".encode()).hexdigest(),
        },
        resource_contract_ref={
            "contract_id": rc.contract_id,
            "content_hash": rc.content_hash,
        },
        branch_snapshot_ref={
            "snapshot_id": bs.snapshot_id,
            "content_hash": bs.content_hash,
        },
        randomization_assignment=assignment,
    )


def _make_all_test_arms(
    rc: ResourceContract,
    bs: BranchSnapshot,
    rp: RandomizationPlan,
) -> list[ExperimentArm]:
    return [
        _make_test_arm(kind, rc, bs, rp)
        for kind in sorted(EX_ARM_KINDS)
    ]


def _make_test_contrasts() -> list[ContrastSpec]:
    return [
        make_contrast_spec(
            contrast_id="contrast-001",
            contrast_kind="equal_resource_fresh_restart",
            arm_kinds=["problem_only", "lineage"],
            metric="math_correct",
            hypothesis="lineage > problem_only",
        ),
        make_contrast_spec(
            contrast_id="contrast-002",
            contrast_kind="lineage_vs_problem_only",
            arm_kinds=["problem_only", "lineage"],
            metric="math_correct",
            hypothesis="lineage > problem_only",
        ),
        make_contrast_spec(
            contrast_id="contrast-003",
            contrast_kind="direction_vs_problem_only",
            arm_kinds=["problem_only", "direction"],
            metric="math_correct",
            hypothesis="direction > problem_only",
        ),
    ]


def _make_test_plan(seed: int = 42) -> ExperimentPlan:
    rc = _make_test_resource_contract()
    bs = _make_test_branch_snapshot()
    rp = _make_test_randomization_plan(seed)
    arms = _make_all_test_arms(rc, bs, rp)
    contrasts = _make_test_contrasts()
    return make_experiment_plan(
        plan_id="plan-test-001",
        arms=arms,
        contrasts=contrasts,
        randomization_plan=rp,
        branch_snapshot=bs,
        resource_contract=rc,
        solver_spec={
            "model": "glm-5-2",
            "profile": "high",
            "tool_policy": "NO_TOOL",
        },
        repeat_stop_rules={
            "max_repeats": 1,
            "stop_on": "COMPLETED",
            "no_retry_negative": True,
        },
        blind_views={"enabled": True},
        endpoints={"primary": "math_correct"},
        cost_statistics={"track_tokens": True},
        technical_failure_handling={
            "tool_drift": "invalid",
            "unobservable": "quarantine",
            "protocol_drift": "invalid",
        },
        audit_roles={
            "independence": "DIFFERENT_SESSION",
            "auditor": "process_auditor",
        },
    )


# ─── ResourceContract tests ──────────────────────────────────────────────


class TestResourceContract(unittest.TestCase):

    def test_make_and_verify(self):
        rc = _make_test_resource_contract()
        result = verify_resource_contract(rc)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(rc.is_hash_valid)
        self.assertTrue(rc.frozen)

    def test_deterministic_hash(self):
        rc1 = _make_test_resource_contract()
        rc2 = _make_test_resource_contract()
        self.assertEqual(rc1.content_hash, rc2.content_hash)

    def test_not_frozen_blocks(self):
        rc = make_resource_contract(
            contract_id="rc-unfrozen",
            frozen=False,
        )
        result = verify_resource_contract(rc)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_RESOURCE_CONTRACT_NOT_FROZEN, result.error_codes)

    def test_hash_mismatch_blocks(self):
        rc = _make_test_resource_contract()
        import dataclasses
        bad = dataclasses.replace(rc, content_hash="0" * 64)
        result = verify_resource_contract(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_RESOURCE_CONTRACT_HASH_MISMATCH, result.error_codes)

    def test_negative_budget_blocks(self):
        rc = make_resource_contract(
            contract_id="rc-neg",
            token_budget=-1,
        )
        result = verify_resource_contract(rc)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_RESOURCE_BUDGET_INVALID, result.error_codes)

    def test_contracts_equal(self):
        rc1 = _make_test_resource_contract()
        rc2 = _make_test_resource_contract()
        self.assertTrue(contracts_equal(rc1, rc2))

    def test_contracts_not_equal(self):
        rc1 = _make_test_resource_contract()
        rc2 = make_resource_contract(
            contract_id="rc-diff",
            token_budget=16384,
        )
        self.assertFalse(contracts_equal(rc1, rc2))


# ─── BranchSnapshot tests ────────────────────────────────────────────────


class TestBranchSnapshot(unittest.TestCase):

    def test_make_and_verify(self):
        bs = _make_test_branch_snapshot()
        result = verify_branch_snapshot(bs)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(bs.is_hash_valid)
        self.assertTrue(bs.frozen)

    def test_deterministic_hash(self):
        bs1 = _make_test_branch_snapshot()
        bs2 = _make_test_branch_snapshot()
        self.assertEqual(bs1.content_hash, bs2.content_hash)

    def test_not_frozen_blocks(self):
        bs = make_branch_snapshot(
            snapshot_id="bs-unfrozen",
            case_pack_ref=_FAKE_CASE_PACK_REF,
            frozen=False,
        )
        result = verify_branch_snapshot(bs)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_BRANCH_SNAPSHOT_NOT_FROZEN, result.error_codes)

    def test_missing_case_pack_ref_blocks(self):
        bs = make_branch_snapshot(
            snapshot_id="bs-no-ref",
            case_pack_ref={},
        )
        result = verify_branch_snapshot(bs)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_CASE_PACK_REF_MISSING, result.error_codes)

    def test_hash_mismatch_blocks(self):
        bs = _make_test_branch_snapshot()
        import dataclasses
        bad = dataclasses.replace(bs, content_hash="0" * 64)
        result = verify_branch_snapshot(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_BRANCH_SNAPSHOT_HASH_MISMATCH, result.error_codes)


# ─── RandomizationPlan tests ─────────────────────────────────────────────


class TestRandomizationPlan(unittest.TestCase):

    def test_make_and_verify(self):
        rp = _make_test_randomization_plan()
        result = verify_randomization_plan(rp)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(rp.is_hash_valid)
        self.assertTrue(rp.frozen)

    def test_deterministic_replay_same_seed_same_assignment(self):
        rp1 = _make_test_randomization_plan(seed=42)
        rp2 = _make_test_randomization_plan(seed=42)
        self.assertEqual(rp1.arm_order, rp2.arm_order)
        self.assertEqual(
            rp1.replay_assignment(),
            rp2.replay_assignment(),
        )

    def test_different_seed_different_assignment(self):
        rp1 = _make_test_randomization_plan(seed=42)
        rp2 = _make_test_randomization_plan(seed=99)
        self.assertNotEqual(rp1.arm_order, rp2.arm_order)

    def test_replay_randomization_function(self):
        order1 = replay_randomization(42, sorted(EX_ARM_KINDS))
        order2 = replay_randomization(42, sorted(EX_ARM_KINDS))
        self.assertEqual(order1, order2)

    def test_deterministic_hash(self):
        rp1 = _make_test_randomization_plan(seed=42)
        rp2 = _make_test_randomization_plan(seed=42)
        self.assertEqual(rp1.content_hash, rp2.content_hash)

    def test_not_frozen_blocks(self):
        rp = make_randomization_plan(
            plan_id="rp-unfrozen",
            seed=42,
            arm_kinds=sorted(EX_ARM_KINDS),
            frozen=False,
        )
        result = verify_randomization_plan(rp)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_RANDOMIZATION_NOT_REPLAYABLE, result.error_codes)

    def test_invalid_block_size_blocks(self):
        rp = RandomizationPlan(
            plan_id="rp-bad",
            seed=42,
            block_size=0,
            arm_order=(),
            frozen=True,
        )
        result = verify_randomization_plan(rp)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_RANDOMIZATION_BLOCK_INVALID, result.error_codes)

    def test_all_arm_kinds_in_order(self):
        rp = _make_test_randomization_plan()
        self.assertEqual(set(rp.arm_order), EX_ARM_KINDS)
        self.assertEqual(rp.block_size, len(EX_ARM_KINDS))


# ─── ExperimentArm tests ─────────────────────────────────────────────────


class TestExperimentArm(unittest.TestCase):

    def test_make_and_verify_all_seven_kinds(self):
        rc = _make_test_resource_contract()
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        for kind in sorted(EX_ARM_KINDS):
            arm = _make_test_arm(kind, rc, bs, rp)
            result = verify_experiment_arm(arm)
            self.assertTrue(
                result.passed,
                msg=f"arm {kind}: {result.details}",
            )

    def test_deterministic_hash(self):
        rc = _make_test_resource_contract()
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        arm1 = _make_test_arm("lineage", rc, bs, rp)
        arm2 = _make_test_arm("lineage", rc, bs, rp)
        self.assertEqual(arm1.content_hash, arm2.content_hash)

    def test_invalid_arm_kind_blocks(self):
        rc = _make_test_resource_contract()
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        arm = make_experiment_arm(
            arm_id="arm-bad",
            arm_kind="invalid_kind",
            case_pack_ref=_FAKE_CASE_PACK_REF,
            strategy_release_ref=_FAKE_RELEASE_REF,
            resource_contract_ref={
                "contract_id": rc.contract_id,
                "content_hash": rc.content_hash,
            },
            branch_snapshot_ref={
                "snapshot_id": bs.snapshot_id,
                "content_hash": bs.content_hash,
            },
            randomization_assignment=0,
        )
        result = verify_experiment_arm(arm)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_ARM_KIND_INVALID, result.error_codes)

    def test_missing_case_pack_ref_blocks(self):
        rc = _make_test_resource_contract()
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        arm = make_experiment_arm(
            arm_id="arm-no-cp",
            arm_kind="problem_only",
            case_pack_ref={},
            strategy_release_ref=_FAKE_RELEASE_REF,
            resource_contract_ref={
                "contract_id": rc.contract_id,
                "content_hash": rc.content_hash,
            },
            branch_snapshot_ref={
                "snapshot_id": bs.snapshot_id,
                "content_hash": bs.content_hash,
            },
            randomization_assignment=0,
        )
        result = verify_experiment_arm(arm)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_CASE_PACK_REF_MISSING, result.error_codes)

    def test_missing_strategy_release_ref_blocks(self):
        rc = _make_test_resource_contract()
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        arm = make_experiment_arm(
            arm_id="arm-no-sr",
            arm_kind="problem_only",
            case_pack_ref=_FAKE_CASE_PACK_REF,
            strategy_release_ref={},
            resource_contract_ref={
                "contract_id": rc.contract_id,
                "content_hash": rc.content_hash,
            },
            branch_snapshot_ref={
                "snapshot_id": bs.snapshot_id,
                "content_hash": bs.content_hash,
            },
            randomization_assignment=0,
        )
        result = verify_experiment_arm(arm)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_STRATEGY_RELEASE_REF_MISSING, result.error_codes)

    def test_missing_arm_payload_ref_blocks(self):
        rc = _make_test_resource_contract()
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        arm = make_experiment_arm(
            arm_id="arm-no-payload",
            arm_kind="problem_only",
            case_pack_ref=_FAKE_CASE_PACK_REF,
            strategy_release_ref=_FAKE_RELEASE_REF,
            arm_payload_ref={},
            resource_contract_ref={
                "contract_id": rc.contract_id,
                "content_hash": rc.content_hash,
            },
            branch_snapshot_ref={
                "snapshot_id": bs.snapshot_id,
                "content_hash": bs.content_hash,
            },
            randomization_assignment=0,
        )
        result = verify_experiment_arm(arm)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_ARM_REF_MISSING, result.error_codes)


# ─── ContrastSpec tests ──────────────────────────────────────────────────


class TestContrastSpec(unittest.TestCase):

    def test_make_and_verify(self):
        cs = make_contrast_spec(
            contrast_id="cs-001",
            contrast_kind="lineage_vs_problem_only",
            arm_kinds=["problem_only", "lineage"],
            metric="math_correct",
            hypothesis="lineage > problem_only",
        )
        result = verify_contrast_spec(cs, available_arm_kinds=EX_ARM_KINDS)
        self.assertTrue(result.passed, msg=str(result.details))

    def test_deterministic_hash(self):
        cs1 = make_contrast_spec(
            contrast_id="cs-001",
            contrast_kind="lineage_vs_problem_only",
            arm_kinds=["problem_only", "lineage"],
        )
        cs2 = make_contrast_spec(
            contrast_id="cs-001",
            contrast_kind="lineage_vs_problem_only",
            arm_kinds=["problem_only", "lineage"],
        )
        self.assertEqual(cs1.content_hash, cs2.content_hash)

    def test_not_pre_registered_blocks(self):
        cs = make_contrast_spec(
            contrast_id="cs-not-pre",
            contrast_kind="lineage_vs_problem_only",
            arm_kinds=["problem_only", "lineage"],
            pre_registered=False,
        )
        result = verify_contrast_spec(cs)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_CONTRAST_NOT_PREREGISTERED, result.error_codes)

    def test_invalid_kind_blocks(self):
        cs = make_contrast_spec(
            contrast_id="cs-bad-kind",
            contrast_kind="invalid_contrast",
            arm_kinds=["problem_only", "lineage"],
        )
        result = verify_contrast_spec(cs)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_CONTRAST_KIND_INVALID, result.error_codes)

    def test_empty_metric_blocks(self):
        cs = make_contrast_spec(
            contrast_id="cs-no-metric",
            contrast_kind="lineage_vs_problem_only",
            arm_kinds=["problem_only", "lineage"],
            metric="",
        )
        result = verify_contrast_spec(cs)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_CONTRAST_METRIC_INVALID, result.error_codes)

    def test_arms_not_found_blocks(self):
        cs = make_contrast_spec(
            contrast_id="cs-bad-arms",
            contrast_kind="lineage_vs_problem_only",
            arm_kinds=["problem_only", "nonexistent"],
        )
        result = verify_contrast_spec(cs, available_arm_kinds={"problem_only", "lineage"})
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_CONTRAST_ARMS_NOT_FOUND, result.error_codes)


# ─── ExperimentPlan tests ────────────────────────────────────────────────


class TestExperimentPlan(unittest.TestCase):

    def test_make_and_verify_golden_path(self):
        plan = _make_test_plan()
        result = verify_experiment_plan(plan)
        self.assertTrue(result.passed, msg=str(result.details))

    def test_plan_is_frozen(self):
        plan = _make_test_plan()
        self.assertTrue(plan.is_frozen)
        self.assertEqual(plan.state, "FROZEN")

    def test_deterministic_hash(self):
        plan1 = _make_test_plan()
        plan2 = _make_test_plan()
        self.assertEqual(plan1.content_hash, plan2.content_hash)

    def test_all_seven_arm_kinds_present(self):
        plan = _make_test_plan()
        self.assertEqual(plan.arm_kinds, EX_ARM_KINDS)

    def test_all_arms_equal_resource(self):
        plan = _make_test_plan()
        rc_hash = plan.resource_contract.content_hash
        for arm in plan.arms:
            self.assertEqual(
                arm.resource_contract_ref["content_hash"],
                rc_hash,
            )

    def test_all_arms_share_branch_snapshot(self):
        plan = _make_test_plan()
        bs_hash = plan.branch_snapshot.content_hash
        for arm in plan.arms:
            self.assertEqual(
                arm.branch_snapshot_ref["content_hash"],
                bs_hash,
            )

    def test_draft_state_blocks(self):
        import dataclasses
        plan = _make_test_plan()
        draft = dataclasses.replace(plan, state="DRAFT")
        result = verify_experiment_plan(draft)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_PLAN_MODIFIED_AFTER_START, result.error_codes)

    def test_arms_not_equal_resource_blocks(self):
        rc = _make_test_resource_contract()
        rc_diff = make_resource_contract(
            contract_id="rc-diff",
            token_budget=16384,
        )
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        arms = _make_all_test_arms(rc, bs, rp)
        # replace one arm's resource_contract_ref with different contract
        import dataclasses
        bad_arm = dataclasses.replace(
            arms[0],
            resource_contract_ref={
                "contract_id": rc_diff.contract_id,
                "content_hash": rc_diff.content_hash,
            },
        )
        bad_arm = dataclasses.replace(
            bad_arm, content_hash=bad_arm.compute_content_hash()
        )
        arms[0] = bad_arm
        plan = make_experiment_plan(
            plan_id="plan-unequal",
            arms=arms,
            contrasts=_make_test_contrasts(),
            randomization_plan=rp,
            branch_snapshot=bs,
            resource_contract=rc,
            solver_spec={"model": "test"},
        )
        result = verify_experiment_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_ARMS_NOT_EQUAL_RESOURCE, result.error_codes)

    def test_missing_contrasts_blocks(self):
        rc = _make_test_resource_contract()
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        plan = make_experiment_plan(
            plan_id="plan-no-contrasts",
            arms=_make_all_test_arms(rc, bs, rp),
            contrasts=[],
            randomization_plan=rp,
            branch_snapshot=bs,
            resource_contract=rc,
            solver_spec={"model": "test"},
        )
        result = verify_experiment_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_CONTRAST_NOT_PREREGISTERED, result.error_codes)

    def test_missing_solver_spec_blocks(self):
        rc = _make_test_resource_contract()
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        plan = make_experiment_plan(
            plan_id="plan-no-solver",
            arms=_make_all_test_arms(rc, bs, rp),
            contrasts=_make_test_contrasts(),
            randomization_plan=rp,
            branch_snapshot=bs,
            resource_contract=rc,
            solver_spec={},
        )
        result = verify_experiment_plan(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)

    def test_check_plan_modified_after_start(self):
        plan = _make_test_plan()
        original_hash = plan.content_hash
        # not started → modification OK
        self.assertFalse(check_plan_modified_after_start(plan, original_hash))
        # started with same hash → not modified
        import dataclasses
        started = dataclasses.replace(plan, state="STARTED")
        self.assertFalse(check_plan_modified_after_start(started, original_hash))
        # started with different hash → modified
        started_modified = dataclasses.replace(started, content_hash="0" * 64)
        self.assertTrue(check_plan_modified_after_start(started_modified, original_hash))

    def test_hash_mismatch_blocks(self):
        plan = _make_test_plan()
        import dataclasses
        bad = dataclasses.replace(plan, content_hash="0" * 64)
        result = verify_experiment_plan(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_PLAN_HASH_MISMATCH, result.error_codes)


# ─── RunArtifactBundle tests ─────────────────────────────────────────────


class TestRunArtifactBundle(unittest.TestCase):

    def _make_test_bundle(self, **kwargs) -> RunArtifactBundle:
        defaults = dict(
            bundle_id="bundle-test-001",
            arm_id="arm-lineage",
            plan_id="plan-test-001",
            branch_snapshot_ref={
                "snapshot_id": "bs-test-001",
                "content_hash": hashlib.sha256(b"bs").hexdigest(),
            },
            resource_contract_ref={
                "contract_id": "rc-test-001",
                "content_hash": hashlib.sha256(b"rc").hexdigest(),
            },
            purpose="causal_experiment",
            run_state="COMPLETED",
            raw_artifact_ref={
                "ref_id": "raw-001",
                "sha256": hashlib.sha256(b"raw").hexdigest(),
            },
            parser_ref={
                "ref_id": "parser-001",
                "sha256": hashlib.sha256(b"parser").hexdigest(),
            },
            termination_reason="COMPLETED",
            observability_status="COMPLETE",
            trajectory_ref={
                "ref_id": "traj-001",
                "sha256": hashlib.sha256(b"traj").hexdigest(),
            },
            answer_ref={
                "ref_id": "answer-001",
                "sha256": hashlib.sha256(b"answer").hexdigest(),
            },
            cost_observability={
                "input_tokens": 200,
                "output_tokens": 100,
                "cost_microunits": 0,
                "usage_completeness": "COMPLETE",
            },
        )
        defaults.update(kwargs)
        return make_run_artifact_bundle(**defaults)

    def test_make_and_verify(self):
        bundle = self._make_test_bundle()
        result = verify_run_artifact_bundle(bundle)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(bundle.is_hash_valid)
        self.assertTrue(bundle.sealed)

    def test_deterministic_hash(self):
        b1 = self._make_test_bundle()
        b2 = self._make_test_bundle()
        self.assertEqual(b1.content_hash, b2.content_hash)

    def test_causal_experiment_requires_all_refs(self):
        bundle = self._make_test_bundle(
            branch_snapshot_ref={},
            resource_contract_ref={},
        )
        result = verify_run_artifact_bundle(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE, result.error_codes)

    def test_invalid_termination_reason_blocks(self):
        bundle = self._make_test_bundle(termination_reason="INVALID_REASON")
        result = verify_run_artifact_bundle(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_TERMINATION_INVALID, result.error_codes)

    def test_invalid_observability_status_blocks(self):
        bundle = self._make_test_bundle(observability_status="INVALID")
        result = verify_run_artifact_bundle(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_OBSERVABILITY_INCOMPLETE, result.error_codes)

    def test_not_sealed_blocks(self):
        bundle = self._make_test_bundle(sealed=False)
        result = verify_run_artifact_bundle(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE, result.error_codes)

    def test_missing_trajectory_blocks(self):
        bundle = self._make_test_bundle(trajectory_ref={})
        result = verify_run_artifact_bundle(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE, result.error_codes)

    def test_quarantine_state_valid(self):
        bundle = self._make_test_bundle(
            run_state="QUARANTINED",
            termination_reason="QUARANTINED",
            quarantine_state="PROTOCOL_DRIFT",
            is_invalid=True,
        )
        result = verify_run_artifact_bundle(bundle)
        self.assertTrue(result.passed, msg=str(result.details))

    def test_quarantine_state_invalid_run_state_blocks(self):
        bundle = self._make_test_bundle(
            run_state="COMPLETED",
            quarantine_state="SOME_QUARANTINE",
        )
        result = verify_run_artifact_bundle(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_QUARANTINE_INVALID, result.error_codes)

    def test_invalid_purpose_blocks(self):
        bundle = self._make_test_bundle(purpose="invalid_purpose")
        result = verify_run_artifact_bundle(bundle)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_RUN_ARTIFACT_BUNDLE_INCOMPLETE, result.error_codes)

    def test_negative_result_bundle(self):
        bundle = self._make_test_bundle(
            run_state="FAILED",
            termination_reason="TIMED_OUT",
            is_negative=True,
        )
        result = verify_run_artifact_bundle(bundle)
        self.assertTrue(result.passed, msg=str(result.details))
        self.assertTrue(bundle.is_negative)


# ─── P5ExperimentRunner tests ────────────────────────────────────────────


class TestP5ExperimentRunner(unittest.TestCase):

    def test_golden_path_all_arms_collected(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner()
        result = runner.run(plan)
        self.assertTrue(
            result.passed,
            msg=f"errors: {result.error_codes} details: {result.details}",
        )
        self.assertEqual(len(result.arm_results), 7)
        # all bundles present
        for r in result.arm_results:
            self.assertIsNotNone(r.bundle)
            self.assertTrue(r.retained)
        # all bundles sealed
        for bundle in result.bundles:
            self.assertTrue(bundle.sealed)

    def test_all_bundles_reference_plan_and_arm(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner()
        result = runner.run(plan)
        for r in result.arm_results:
            self.assertEqual(r.bundle.plan_id, plan.plan_id)
            self.assertEqual(r.bundle.arm_id, r.arm_id)

    def test_verify_p5_run_result(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner()
        result = runner.run(plan)
        vresult = verify_p5_run_result(result)
        self.assertTrue(vresult.passed, msg=str(vresult.details))

    def test_budget_exceeded_blocks(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner(force_budget_exceeded=True)
        result = runner.run(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_BUDGET_EXCEEDED, result.error_codes)

    def test_baseline_truncated_blocks(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner(force_baseline_truncated=True)
        result = runner.run(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_BASELINE_TRUNCATED, result.error_codes)

    def test_plan_modified_after_start_blocks(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner(force_plan_modified=True)
        result = runner.run(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_PLAN_MODIFIED_AFTER_START, result.error_codes)

    def test_negative_result_deleted_blocks(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner(force_negative_deleted=True)
        result = runner.run(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_NEGATIVE_RESULT_DELETED, result.error_codes)

    def test_invalid_result_deleted_blocks(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner(force_invalid_deleted=True)
        result = runner.run(plan)
        self.assertFalse(result.passed)
        self.assertIn(EC.EX_INVALID_RESULT_DELETED, result.error_codes)

    def test_invalid_plan_blocks(self):
        rc = _make_test_resource_contract()
        bs = _make_test_branch_snapshot()
        rp = _make_test_randomization_plan()
        plan = make_experiment_plan(
            plan_id="plan-invalid",
            arms=[],  # no arms
            contrasts=_make_test_contrasts(),
            randomization_plan=rp,
            branch_snapshot=bs,
            resource_contract=rc,
            solver_spec={"model": "test"},
        )
        runner = P5ExperimentRunner()
        result = runner.run(plan)
        self.assertFalse(result.passed)

    def test_all_arm_kinds_present_in_results(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner()
        result = runner.run(plan)
        result_kinds = {r.arm_kind for r in result.arm_results}
        self.assertEqual(result_kinds, EX_ARM_KINDS)

    def test_deterministic_run(self):
        plan = _make_test_plan()
        runner1 = P5ExperimentRunner()
        runner2 = P5ExperimentRunner()
        result1 = runner1.run(plan)
        result2 = runner2.run(plan)
        # same plan → same bundle hashes
        for r1, r2 in zip(result1.arm_results, result2.arm_results):
            self.assertEqual(r1.bundle.content_hash, r2.bundle.content_hash)


# ─── ExperimentCapabilityReport tests ────────────────────────────────────


class TestExperimentCapabilityReport(unittest.TestCase):

    def test_build_and_verify(self):
        plan = _make_test_plan()
        runner = P5ExperimentRunner()
        run_result = runner.run(plan)
        bundle_hashes = {
            r.arm_id: r.bundle.content_hash
            for r in run_result.arm_results
            if r.bundle
        }
        report = build_experiment_capability_report(
            plan_hash=plan.content_hash,
            branch_snapshot_hash=plan.branch_snapshot.content_hash,
            resource_contract_hash=plan.resource_contract.content_hash,
            randomization_seed=plan.randomization_plan.seed,
            arm_kinds_present=sorted(EX_ARM_KINDS),
            contrast_ids=[c.contrast_id for c in plan.contrasts],
            bundle_hashes=bundle_hashes,
            negative_result_count=run_result.negative_count,
            invalid_result_count=run_result.invalid_count,
            all_results_retained=True,
            randomization_replayable=True,
            verifier_identity="test-verifier",
        )
        errors = verify_experiment_capability_report(report)
        self.assertEqual(errors, (), msg=str(errors))

    def test_report_class(self):
        plan = _make_test_plan()
        report = build_experiment_capability_report(
            plan_hash=plan.content_hash,
            branch_snapshot_hash=plan.branch_snapshot.content_hash,
            resource_contract_hash=plan.resource_contract.content_hash,
            randomization_seed=42,
            arm_kinds_present=sorted(EX_ARM_KINDS),
            contrast_ids=["c1"],
            bundle_hashes={"arm1": hashlib.sha256(b"x").hexdigest()},
            negative_result_count=0,
            invalid_result_count=0,
            all_results_retained=True,
            randomization_replayable=True,
            verifier_identity="test",
        )
        r = ExperimentCapabilityReport(report)
        self.assertEqual(r.report_kind, "ExperimentCapabilityReport")
        self.assertEqual(r.verdict, "PASS")

    def test_invalid_report_kind_rejected(self):
        report = {
            "schema_version": EXPERIMENT_REPORT_SCHEMA_VERSION,
            "report_kind": "DatabaseSchemaStateReport",  # forbidden
            "scope": "EXPERIMENT_CAPABILITY_V1",
            "generated_at": "2026-08-14T12:00:00+00:00",
            "plan_hash": hashlib.sha256(b"p").hexdigest(),
            "branch_snapshot_hash": hashlib.sha256(b"b").hexdigest(),
            "resource_contract_hash": hashlib.sha256(b"r").hexdigest(),
            "randomization_seed": 42,
            "arm_kinds_present": sorted(EX_ARM_KINDS),
            "contrast_ids": [],
            "bundle_hashes": {},
            "negative_result_count": 0,
            "invalid_result_count": 0,
            "all_results_retained": True,
            "randomization_replayable": True,
            "verdict": "PASS",
            "verifier_identity": "test",
            "checks": [{"check_id": c, "verdict": "PASS", "evidence": []} for c in EX_CHECK_IDS],
            "claims": {c: True for c in EX_CLAIMS},
            "side_effects": {k: 0 for k in EX_SIDE_EFFECT_KEYS},
            "blockers": [],
            "explicit_nonclaims": list(EX_NONCLAIMS),
        }
        errors = verify_experiment_capability_report(report)
        self.assertTrue(any(e[0] == EC.EX_OUTPUT_KIND_FORBIDDEN for e in errors))

    def test_missing_arm_kinds_rejected(self):
        report = build_experiment_capability_report(
            plan_hash=hashlib.sha256(b"p").hexdigest(),
            branch_snapshot_hash=hashlib.sha256(b"b").hexdigest(),
            resource_contract_hash=hashlib.sha256(b"r").hexdigest(),
            randomization_seed=42,
            arm_kinds_present=sorted(EX_ARM_KINDS),
            contrast_ids=[],
            bundle_hashes={},
            negative_result_count=0,
            invalid_result_count=0,
            all_results_retained=True,
            randomization_replayable=True,
            verifier_identity="test",
        )
        report["arm_kinds_present"] = ["problem_only"]  # incomplete
        errors = verify_experiment_capability_report(report)
        self.assertTrue(any(e[0] == EC.EX_ARM_KIND_INVALID for e in errors))

    def test_nonzero_side_effects_rejected(self):
        report = build_experiment_capability_report(
            plan_hash=hashlib.sha256(b"p").hexdigest(),
            branch_snapshot_hash=hashlib.sha256(b"b").hexdigest(),
            resource_contract_hash=hashlib.sha256(b"r").hexdigest(),
            randomization_seed=42,
            arm_kinds_present=sorted(EX_ARM_KINDS),
            contrast_ids=[],
            bundle_hashes={},
            negative_result_count=0,
            invalid_result_count=0,
            all_results_retained=True,
            randomization_replayable=True,
            verifier_identity="test",
        )
        report["side_effects"]["database_writes"] = 1
        errors = verify_experiment_capability_report(report)
        self.assertTrue(any(e[0] == EC.EX_OUTPUT_KIND_FORBIDDEN for e in errors))

    def test_randomization_not_replayable_rejected(self):
        report = build_experiment_capability_report(
            plan_hash=hashlib.sha256(b"p").hexdigest(),
            branch_snapshot_hash=hashlib.sha256(b"b").hexdigest(),
            resource_contract_hash=hashlib.sha256(b"r").hexdigest(),
            randomization_seed=42,
            arm_kinds_present=sorted(EX_ARM_KINDS),
            contrast_ids=[],
            bundle_hashes={},
            negative_result_count=0,
            invalid_result_count=0,
            all_results_retained=True,
            randomization_replayable=True,
            verifier_identity="test",
        )
        report["randomization_replayable"] = False
        errors = verify_experiment_capability_report(report)
        self.assertTrue(any(e[0] == EC.EX_RANDOMIZATION_NOT_REPLAYABLE for e in errors))

    def test_results_not_retained_rejected(self):
        report = build_experiment_capability_report(
            plan_hash=hashlib.sha256(b"p").hexdigest(),
            branch_snapshot_hash=hashlib.sha256(b"b").hexdigest(),
            resource_contract_hash=hashlib.sha256(b"r").hexdigest(),
            randomization_seed=42,
            arm_kinds_present=sorted(EX_ARM_KINDS),
            contrast_ids=[],
            bundle_hashes={},
            negative_result_count=0,
            invalid_result_count=0,
            all_results_retained=True,
            randomization_replayable=True,
            verifier_identity="test",
        )
        report["all_results_retained"] = False
        errors = verify_experiment_capability_report(report)
        self.assertTrue(any(e[0] == EC.EX_NEGATIVE_RESULT_DELETED for e in errors))


# ─── Constants verification tests ────────────────────────────────────────


class TestConstants(unittest.TestCase):

    def test_ex_arm_kinds_has_seven(self):
        self.assertEqual(len(EX_ARM_KINDS), 7)
        for kind in (
            "problem_only", "lineage", "direction", "lineage_direction",
            "distractor", "operation_critic", "position_neutral",
        ):
            self.assertIn(kind, EX_ARM_KINDS)

    def test_ex_contrast_kinds(self):
        self.assertIn("equal_resource_fresh_restart", EX_CONTRAST_KINDS)
        self.assertIn("lineage_vs_problem_only", EX_CONTRAST_KINDS)

    def test_ex_plan_states(self):
        for state in ("DRAFT", "FROZEN", "STARTED", "COMPLETED", "SUPERSEDED"):
            self.assertIn(state, EX_PLAN_STATES)

    def test_ex_run_states(self):
        for state in ("PENDING", "COMPLETED", "FAILED", "QUARANTINED", "INVALID"):
            self.assertIn(state, EX_RUN_STATES)

    def test_ex_termination_reasons(self):
        for reason in ("COMPLETED", "CANCELLED", "TIMED_OUT", "BUDGET_EXCEEDED",
                        "TERMINATED", "FAILED_PERMANENT", "QUARANTINED"):
            self.assertIn(reason, EX_TERMINATION_REASONS)

    def test_ex_observability_statuses(self):
        for status in ("COMPLETE", "PARTIAL", "MISSING", "UNOBSERVABLE_DECLARED"):
            self.assertIn(status, EX_OBSERVABILITY_STATUSES)

    def test_ex_allowed_output_kinds(self):
        for kind in (
            "ExperimentPlan", "ResourceContract", "BranchSnapshot",
            "RandomizationPlan", "ExperimentArm", "ContrastSpec",
            "RunArtifactBundle", "ExperimentCapabilityReport",
        ):
            self.assertIn(kind, EX_ALLOWED_OUTPUT_KINDS)

    def test_ex_forbidden_output_kinds(self):
        for kind in (
            "DatabaseSchemaStateReport", "EvidenceRecord",
            "ConfirmatoryEvidenceRecord", "P5ClaimRecord", "RunAudit",
        ):
            self.assertIn(kind, EX_FORBIDDEN_OUTPUT_KINDS)

    def test_ex_purpose_kinds(self):
        for kind in ("causal_experiment", "bare_baseline", "calibration"):
            self.assertIn(kind, EX_PURPOSE_KINDS)

    def test_ex_side_effect_keys(self):
        for key in (
            "database_writes", "redis_writes", "d_volume_writes",
            "solver_launches", "model_live_calls", "human_gate_commits",
        ):
            self.assertIn(key, EX_SIDE_EFFECT_KEYS)

    def test_ex_check_ids_match_claims(self):
        self.assertEqual(len(EX_CHECK_IDS), 23)
        self.assertEqual(len(EX_CLAIMS), 23)

    def test_ex_nonclaims(self):
        self.assertIn("status_implemented_pending_evidence", EX_NONCLAIMS)
        self.assertIn("does_not_launch_real_solver", EX_NONCLAIMS)

    def test_allowed_and_forbidden_disjoint(self):
        self.assertEqual(
            EX_ALLOWED_OUTPUT_KINDS & EX_FORBIDDEN_OUTPUT_KINDS,
            set(),
        )


# ─── EX1 boundary tests ──────────────────────────────────────────────────


class TestEX1Boundary(unittest.TestCase):

    def test_allowed_output_kinds_are_ex1_objects(self):
        """EX1 allowed output kinds must all be EX1 objects."""
        for kind in EX_ALLOWED_OUTPUT_KINDS:
            self.assertIn(kind, (
                "ExperimentPlan", "ResourceContract", "BranchSnapshot",
                "RandomizationPlan", "ExperimentArm", "ContrastSpec",
                "RunArtifactBundle", "ExperimentCapabilityReport",
            ))

    def test_forbidden_output_kinds_are_other_wp(self):
        """EX1 forbidden output kinds must all belong to other WPs."""
        for kind in EX_FORBIDDEN_OUTPUT_KINDS:
            self.assertNotIn(kind, EX_ALLOWED_OUTPUT_KINDS)

    def test_experiment_objects_not_in_forbidden(self):
        """EX1's own objects must not be in its forbidden list."""
        for kind in EX_ALLOWED_OUTPUT_KINDS:
            self.assertNotIn(kind, EX_FORBIDDEN_OUTPUT_KINDS)

    def test_no_db_or_solver_reports_in_allowed(self):
        """EX1 must not produce DB or solver reports."""
        forbidden_in_allowed = EX_ALLOWED_OUTPUT_KINDS & {
            "DatabaseSchemaStateReport",
            "DatabaseRuntimeCapabilityReport",
            "SolverLaunchReceipt",
            "SolverSafeLaunchReport",
        }
        self.assertEqual(forbidden_in_allowed, set())


# ─── Integration: full P4→P5 flow ────────────────────────────────────────


class TestFullP4P5Flow(unittest.TestCase):

    def test_p4_freeze_to_p5_run_to_bundle_sealed(self):
        """Golden path: P4 plan freeze → P5 experiment run → all arm results collected → bundles sealed."""
        # P4 freeze
        plan = _make_test_plan()
        plan_result = verify_experiment_plan(plan)
        self.assertTrue(plan_result.passed, msg=str(plan_result.details))

        # P5 run
        runner = P5ExperimentRunner()
        run_result = runner.run(plan)
        self.assertTrue(run_result.passed, msg=str(run_result.details))

        # all arm results collected
        self.assertEqual(len(run_result.arm_results), 7)

        # all bundles sealed
        for r in run_result.arm_results:
            self.assertIsNotNone(r.bundle)
            self.assertTrue(r.bundle.sealed)
            bundle_result = verify_run_artifact_bundle(r.bundle)
            self.assertTrue(
                bundle_result.passed,
                msg=f"arm {r.arm_id}: {bundle_result.details}",
            )

        # verify run result
        vresult = verify_p5_run_result(run_result)
        self.assertTrue(vresult.passed, msg=str(vresult.details))

    def test_randomization_replay_in_full_flow(self):
        """Same seed → same randomization assignment in full flow."""
        plan1 = _make_test_plan(seed=42)
        plan2 = _make_test_plan(seed=42)
        self.assertEqual(
            plan1.randomization_plan.arm_order,
            plan2.randomization_plan.arm_order,
        )
        self.assertEqual(
            plan1.randomization_plan.replay_assignment(),
            plan2.randomization_plan.replay_assignment(),
        )

    def test_capability_report_from_full_flow(self):
        """Build capability report from full P4→P5 flow."""
        plan = _make_test_plan()
        runner = P5ExperimentRunner()
        run_result = runner.run(plan)
        self.assertTrue(run_result.passed)

        bundle_hashes = {
            r.arm_id: r.bundle.content_hash
            for r in run_result.arm_results
            if r.bundle
        }
        report = build_experiment_capability_report(
            plan_hash=plan.content_hash,
            branch_snapshot_hash=plan.branch_snapshot.content_hash,
            resource_contract_hash=plan.resource_contract.content_hash,
            randomization_seed=plan.randomization_plan.seed,
            arm_kinds_present=sorted(EX_ARM_KINDS),
            contrast_ids=[c.contrast_id for c in plan.contrasts],
            bundle_hashes=bundle_hashes,
            negative_result_count=run_result.negative_count,
            invalid_result_count=run_result.invalid_count,
            all_results_retained=True,
            randomization_replayable=True,
            verifier_identity="integration-test",
        )
        errors = verify_experiment_capability_report(report)
        self.assertEqual(errors, (), msg=str(errors))


if __name__ == "__main__":
    unittest.main()
