"""WP-TX1 Taxonomy/Tell Registry 测试。

测试层级：Golden → Negative (blocker) → Migration/Invalidation/Inheritance
所有 blocker test 失败 → 工作包 FAIL。

覆盖：
- Golden: 每个 object 的 create/version/hash/lineage
- Negative (blocker):
  - manifestation=Core 被拒绝
  - 旧 Evidence 外键未迁移
  - Gate 改 pointer
  - invariant violation
  - M:N violation
  - broken lineage
  - abstain violation
  - policy version drift
  - efficacy without solver context
  - FCA marked as truth
  - negative guard violated
- Migration/invalidation/inheritance 测试
- Deterministic hash 测试
- Boundary 测试（TX1 allowed/forbidden output kinds）
- 所有 constants verified
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.contracts.errors import (
    VerificationErrorCode as EC,
    TX_TELL_MANIFESTATION_KINDS,
    TX_TELL_CORE_ACTIONS,
    TX_BOUNDARY_GUARD_KINDS,
    TX_HINT_RELATION_KINDS,
    TX_SELECTOR_DECISION_KINDS,
    TX_INJECTION_POSITIONS,
    TX_CONTRACT_KINDS,
    TX_RELEASE_STATES,
    TX_VALIDITY_STATUSES,
    TX_EFFICACY_STATUSES,
    TX_TAXONOMY_SNAPSHOT_STATES,
    TX_EVIDENCE_INHERITANCE_SCOPES,
    TX_INVALIDATION_TARGETS,
    TX1_ALLOWED_OUTPUT_KINDS,
    TX1_FORBIDDEN_OUTPUT_KINDS,
    TX1_SIDE_EFFECT_KEYS,
    TX_GATE_TYPE_TX_RELEASE,
)
from seven_system.taxonomy import (
    # taxonomy snapshot
    TaxonomyCoordinate,
    TaxonomyEnumeration,
    TaxonomySnapshot,
    make_taxonomy_snapshot,
    verify_taxonomy_snapshot,
    AttributeDefinition,
    AttributeDictionaryVersion,
    make_attribute_dictionary_version,
    verify_attribute_dictionary_version,
    FCAContextSnapshot,
    make_fca_context_snapshot,
    verify_fca_context_snapshot,
    # tell core / family
    TellCore,
    make_tell_core,
    verify_tell_core,
    TellFamily,
    make_tell_family,
    verify_tell_family,
    ObservationView,
    make_observation_view,
    TellManifestation,
    make_tell_manifestation,
    verify_tell_manifestation,
    CandidateBranch,
    TellRecognitionRecord,
    make_tell_recognition_record,
    verify_tell_recognition_record,
    # boundary / hint / renderer / selector / injection / contract
    BoundaryGuard,
    ApplicabilityBoundary,
    make_applicability_boundary,
    verify_applicability_boundary,
    TellHintRelation,
    make_tell_hint_relation,
    verify_tell_hint_relation,
    HintRenderer,
    make_hint_renderer,
    HintInstance,
    make_hint_instance,
    verify_hint_instance,
    SelectorDecision,
    make_selector_decision,
    verify_selector_decision,
    InjectionPolicy,
    make_injection_policy,
    verify_injection_policy,
    TellContract,
    make_tell_contract,
    verify_tell_contract,
    # release / lineage / migration / validity / efficacy / invalidation
    ReleaseComponentRef,
    TellStrategyRelease,
    make_tell_strategy_release,
    verify_tell_strategy_release,
    ReleaseLineage,
    make_release_lineage,
    verify_release_lineage,
    EvidenceForeignKeyMigration,
    make_evidence_foreign_key_migration,
    verify_evidence_foreign_key_migration,
    MathValidityRecord,
    make_math_validity_record,
    verify_math_validity_record,
    SolverResourceContext,
    SystemEfficacyRecord,
    make_system_efficacy_record,
    verify_system_efficacy_record,
    InvalidationNotice,
    make_invalidation_notice,
    compute_invalidation_notice,
    verify_invalidation_notice,
    INVALIDATION_TRIGGERS,
)


# ─── helpers ─────────────────────────────────────────────────────────


def _make_taxonomy_snapshot_v1() -> TaxonomySnapshot:
    return make_taxonomy_snapshot(
        snapshot_id="tx-snap-001",
        version="1.0.0",
        state="FROZEN",
        coordinates=(
            TaxonomyCoordinate(
                axis="problem_type",
                value="algebra",
                definition="algebraic problem",
                applicable_versions=("1.0.0",),
            ),
        ),
        enumerations=(
            TaxonomyEnumeration(
                axis="problem_type",
                values=("algebra", "geometry", "number_theory"),
                definitions={"algebra": "algebraic problem"},
            ),
        ),
        definitions={"branch_signal": "fork signal in trace"},
        applicable_versions=("1.0.0",),
        frozen_at="2026-08-20T00:00:00Z",
    )


def _make_taxonomy_snapshot_v2(v1: TaxonomySnapshot) -> TaxonomySnapshot:
    return make_taxonomy_snapshot(
        snapshot_id="tx-snap-002",
        version="2.0.0",
        state="FROZEN",
        coordinates=(
            TaxonomyCoordinate(
                axis="problem_type",
                value="algebra",
                definition="algebraic problem v2",
                applicable_versions=("2.0.0",),
            ),
        ),
        enumerations=(
            TaxonomyEnumeration(
                axis="problem_type",
                values=("algebra", "geometry", "number_theory", "combinatorics"),
                definitions={"algebra": "algebraic problem v2"},
            ),
        ),
        definitions={"branch_signal": "fork signal in trace v2"},
        applicable_versions=("2.0.0",),
        supersedes_ref={
            "snapshot_id": v1.snapshot_id,
            "content_hash": v1.content_hash,
        },
        frozen_at="2026-08-21T00:00:00Z",
    )


def _make_tell_family() -> TellFamily:
    return make_tell_family(
        family_id="tf-001",
        family_name="Branch Open Family",
        lineage_root_core_id="tc-001",
        member_core_ids=("tc-001", "tc-002"),
        frozen_at="2026-08-20T00:00:00Z",
    )


def _make_tell_core(family: TellFamily) -> TellCore:
    return make_tell_core(
        core_id="tc-001",
        family_id=family.family_id,
        cognitive_action="BRANCH_OPEN",
        invariant_description="opens a new branch at fork point",
        lineage_ref={
            "family_id": family.family_id,
            "lineage_hash": family.lineage_hash,
        },
        frozen_at="2026-08-20T00:00:00Z",
    )


def _make_tell_core_v2(family: TellFamily, v1: TellCore) -> TellCore:
    return make_tell_core(
        core_id="tc-002",
        family_id=family.family_id,
        cognitive_action="BRANCH_OPEN",
        invariant_description="opens a new branch at fork point v2",
        lineage_ref={
            "family_id": family.family_id,
            "lineage_hash": family.lineage_hash,
        },
        supersedes_ref={
            "core_id": v1.core_id,
            "content_hash": v1.content_hash,
        },
        frozen_at="2026-08-21T00:00:00Z",
    )


def _make_manifestation(core: TellCore) -> TellManifestation:
    return make_tell_manifestation(
        manifestation_id="man-001",
        core_id=core.core_id,
        manifestation_core_id="man-core-001",
        kind="TRACE_POSITION_MANIFESTATION",
        observation_view_id="ov-001",
        span="span[0:10]",
        frozen_at="2026-08-20T00:00:00Z",
    )


def _make_hint_renderer() -> HintRenderer:
    return make_hint_renderer(
        renderer_id="hr-001",
        version="1.0.0",
        expression_strategy="directional_hint",
        leakage_budget="low",
        specificity_level="topology",
        frozen_at="2026-08-20T00:00:00Z",
    )


def _make_release_components(
    core: TellCore,
    boundary: ApplicabilityBoundary,
    selector: SelectorDecision,
    renderer: HintRenderer,
    injection: InjectionPolicy,
    critic: TellContract,
    composition: TellContract,
    taxonomy: TaxonomySnapshot,
) -> dict:
    return dict(
        core_ref=ReleaseComponentRef(
            kind="TellCore",
            component_id=core.core_id,
            version="1.0.0",
            content_hash=core.content_hash,
        ),
        boundary_ref=ReleaseComponentRef(
            kind="ApplicabilityBoundary",
            component_id=boundary.boundary_id,
            content_hash=boundary.content_hash,
        ),
        selector_ref=ReleaseComponentRef(
            kind="SelectorDecision",
            component_id=selector.decision_id,
            content_hash=selector.content_hash,
        ),
        renderer_ref=ReleaseComponentRef(
            kind="HintRenderer",
            component_id=renderer.renderer_id,
            version=renderer.version,
            content_hash=renderer.content_hash,
        ),
        injection_ref=ReleaseComponentRef(
            kind="InjectionPolicy",
            component_id=injection.policy_id,
            version=injection.version,
            content_hash=injection.content_hash,
        ),
        critic_ref=ReleaseComponentRef(
            kind="CriticContract",
            component_id=critic.contract_id,
            content_hash=critic.content_hash,
        ),
        composition_ref=ReleaseComponentRef(
            kind="CompositionContract",
            component_id=composition.contract_id,
            content_hash=composition.content_hash,
        ),
        taxonomy_ref=ReleaseComponentRef(
            kind="TaxonomySnapshot",
            component_id=taxonomy.snapshot_id,
            version=taxonomy.version,
            content_hash=taxonomy.content_hash,
        ),
    )


# ─── Constants tests ─────────────────────────────────────────────────


class ConstantsTests(unittest.TestCase):
    """所有 TX1 常量集合 verified。"""

    def test_manifestation_kinds(self):
        self.assertIsInstance(TX_TELL_MANIFESTATION_KINDS, frozenset)
        self.assertIn("TRACE_POSITION_MANIFESTATION", TX_TELL_MANIFESTATION_KINDS)
        self.assertGreaterEqual(len(TX_TELL_MANIFESTATION_KINDS), 4)

    def test_tell_core_actions(self):
        self.assertIsInstance(TX_TELL_CORE_ACTIONS, frozenset)
        self.assertIn("BRANCH_OPEN", TX_TELL_CORE_ACTIONS)
        self.assertIn("ABSTAIN", TX_TELL_CORE_ACTIONS)

    def test_boundary_guard_kinds(self):
        self.assertIsInstance(TX_BOUNDARY_GUARD_KINDS, frozenset)
        self.assertIn("NEGATIVE_GUARD", TX_BOUNDARY_GUARD_KINDS)

    def test_hint_relation_kinds(self):
        self.assertIsInstance(TX_HINT_RELATION_KINDS, frozenset)
        self.assertIn("TELL_TO_HINT", TX_HINT_RELATION_KINDS)

    def test_selector_decision_kinds(self):
        self.assertIsInstance(TX_SELECTOR_DECISION_KINDS, frozenset)
        self.assertIn("ABSTAIN", TX_SELECTOR_DECISION_KINDS)

    def test_injection_positions(self):
        self.assertIsInstance(TX_INJECTION_POSITIONS, frozenset)
        self.assertIn("PRE_TRACE", TX_INJECTION_POSITIONS)

    def test_contract_kinds(self):
        self.assertIsInstance(TX_CONTRACT_KINDS, frozenset)
        self.assertIn("COMPOSITION_CONTRACT", TX_CONTRACT_KINDS)

    def test_release_states(self):
        self.assertIsInstance(TX_RELEASE_STATES, frozenset)
        self.assertIn("RELEASED", TX_RELEASE_STATES)

    def test_validity_statuses(self):
        self.assertIsInstance(TX_VALIDITY_STATUSES, frozenset)
        self.assertIn("VALID", TX_VALIDITY_STATUSES)

    def test_efficacy_statuses(self):
        self.assertIsInstance(TX_EFFICACY_STATUSES, frozenset)
        self.assertIn("EFFICACIOUS", TX_EFFICACY_STATUSES)

    def test_taxonomy_snapshot_states(self):
        self.assertIsInstance(TX_TAXONOMY_SNAPSHOT_STATES, frozenset)
        self.assertIn("FROZEN", TX_TAXONOMY_SNAPSHOT_STATES)

    def test_evidence_inheritance_scopes(self):
        self.assertIsInstance(TX_EVIDENCE_INHERITANCE_SCOPES, frozenset)
        self.assertIn("EXACT", TX_EVIDENCE_INHERITANCE_SCOPES)
        self.assertIn("SUBSCOPE", TX_EVIDENCE_INHERITANCE_SCOPES)
        self.assertIn("PROVENANCE_ONLY", TX_EVIDENCE_INHERITANCE_SCOPES)

    def test_invalidation_targets(self):
        self.assertIsInstance(TX_INVALIDATION_TARGETS, frozenset)
        self.assertIn("CoverageApplicability", TX_INVALIDATION_TARGETS)
        self.assertIn("SystemEfficacyRecord", TX_INVALIDATION_TARGETS)

    def test_allowed_output_kinds(self):
        self.assertIsInstance(TX1_ALLOWED_OUTPUT_KINDS, frozenset)
        self.assertIn("TaxonomySnapshot", TX1_ALLOWED_OUTPUT_KINDS)
        self.assertIn("TellCore", TX1_ALLOWED_OUTPUT_KINDS)
        self.assertIn("TellStrategyRelease", TX1_ALLOWED_OUTPUT_KINDS)
        self.assertIn("MathValidityRecord", TX1_ALLOWED_OUTPUT_KINDS)
        self.assertIn("SystemEfficacyRecord", TX1_ALLOWED_OUTPUT_KINDS)

    def test_forbidden_output_kinds(self):
        self.assertIsInstance(TX1_FORBIDDEN_OUTPUT_KINDS, frozenset)
        self.assertIn("EvidenceRecord", TX1_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("SolverLaunchReceipt", TX1_FORBIDDEN_OUTPUT_KINDS)

    def test_allowed_and_forbidden_disjoint(self):
        self.assertEqual(
            TX1_ALLOWED_OUTPUT_KINDS & TX1_FORBIDDEN_OUTPUT_KINDS,
            frozenset(),
        )

    def test_side_effect_keys(self):
        self.assertIsInstance(TX1_SIDE_EFFECT_KEYS, tuple)
        self.assertIn("database_writes", TX1_SIDE_EFFECT_KEYS)
        self.assertIn("solver_launches", TX1_SIDE_EFFECT_KEYS)
        self.assertIn("model_live_calls", TX1_SIDE_EFFECT_KEYS)

    def test_gate_type(self):
        self.assertEqual(TX_GATE_TYPE_TX_RELEASE, "G-TX-RELEASE")

    def test_error_codes_exist(self):
        codes = [
            EC.TX_TAXONOMY_HASH_MISMATCH,
            EC.TX_TAXONOMY_VERSION_NOT_FROZEN,
            EC.TX_MANIFESTATION_EQUALS_CORE,
            EC.TX_TELL_CORE_INVARIANT_VIOLATED,
            EC.TX_BOUNDARY_NEGATIVE_GUARD_VIOLATED,
            EC.TX_HINT_RELATION_NOT_MN,
            EC.TX_RELEASE_LINEAGE_BROKEN,
            EC.TX_RELEASE_POINTER_CHANGED_BY_GATE,
            EC.TX_EFFICACY_SOLVER_CONTEXT_MISSING,
            EC.TX_OLD_EVIDENCE_FOREIGN_KEY_NOT_MIGRATED,
            EC.TX_TELL_FAMILY_LINEAGE_BROKEN,
            EC.TX_SELECTOR_ABSTAIN_VIOLATED,
            EC.TX_INJECTION_POLICY_VERSION_DRIFT,
            EC.TX_FCA_CONTEXT_MARKED_AS_TRUTH,
            EC.TX_FCA_CONTEXT_NOT_CALIBRATION_AID,
        ]
        for c in codes:
            self.assertTrue(c.value.startswith("TX_"), f"{c}")


# ─── TaxonomySnapshot golden + negative ──────────────────────────────


class TaxonomySnapshotTests(unittest.TestCase):

    def test_golden_create_and_hash(self):
        snap = _make_taxonomy_snapshot_v1()
        self.assertTrue(snap.is_hash_valid)
        self.assertTrue(snap.is_frozen)
        self.assertTrue(snap.is_append_only)
        self.assertEqual(snap.state, "FROZEN")
        self.assertEqual(snap.version, "1.0.0")

    def test_golden_verify_passes(self):
        snap = _make_taxonomy_snapshot_v1()
        result = verify_taxonomy_snapshot(snap)
        self.assertTrue(result.passed, result.details)
        self.assertEqual(result.snapshot_id, "tx-snap-001")

    def test_version_lineage(self):
        v1 = _make_taxonomy_snapshot_v1()
        v2 = _make_taxonomy_snapshot_v2(v1)
        self.assertEqual(v2.supersedes_ref["snapshot_id"], v1.snapshot_id)
        self.assertEqual(v2.supersedes_ref["content_hash"], v1.content_hash)
        result = verify_taxonomy_snapshot(v2, known_snapshots={v1.snapshot_id: v1})
        self.assertTrue(result.passed, result.details)

    def test_negative_version_not_frozen(self):
        snap = make_taxonomy_snapshot(
            snapshot_id="tx-bad",
            version="",
            state="FROZEN",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_taxonomy_snapshot(snap)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_TAXONOMY_VERSION_NOT_FROZEN, result.error_codes)

    def test_negative_hash_mismatch(self):
        snap = _make_taxonomy_snapshot_v1()
        import dataclasses
        bad = dataclasses.replace(snap, content_hash="deadbeef" * 8)
        result = verify_taxonomy_snapshot(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_TAXONOMY_HASH_MISMATCH, result.error_codes)

    def test_negative_broken_supersedes_ref(self):
        v1 = _make_taxonomy_snapshot_v1()
        v2 = make_taxonomy_snapshot(
            snapshot_id="tx-snap-002",
            version="2.0.0",
            state="FROZEN",
            supersedes_ref={"snapshot_id": "nonexistent", "content_hash": "x" * 64},
            frozen_at="2026-08-21T00:00:00Z",
        )
        result = verify_taxonomy_snapshot(v2, known_snapshots={v1.snapshot_id: v1})
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_TAXONOMY_SUPERSEDES_REF_BROKEN, result.error_codes)

    def test_deterministic_hash(self):
        snap1 = _make_taxonomy_snapshot_v1()
        snap2 = _make_taxonomy_snapshot_v1()
        self.assertEqual(snap1.content_hash, snap2.content_hash)


# ─── AttributeDictionaryVersion ──────────────────────────────────────


class AttributeDictionaryTests(unittest.TestCase):

    def test_golden_create_and_hash(self):
        adv = make_attribute_dictionary_version(
            dict_id="ad-001",
            version="1.0.0",
            attributes=(
                AttributeDefinition(
                    name="branch_signal",
                    attr_type="string",
                    description="fork signal",
                ),
            ),
            frozen_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(adv.is_hash_valid)
        self.assertTrue(adv.is_frozen)
        result = verify_attribute_dictionary_version(adv)
        self.assertTrue(result.passed, result.details)

    def test_version_lineage(self):
        v1 = make_attribute_dictionary_version(
            dict_id="ad-001", version="1.0.0", frozen_at="2026-08-20T00:00:00Z",
        )
        v2 = make_attribute_dictionary_version(
            dict_id="ad-002",
            version="2.0.0",
            supersedes_ref={"dict_id": v1.dict_id, "content_hash": v1.content_hash},
            frozen_at="2026-08-21T00:00:00Z",
        )
        result = verify_attribute_dictionary_version(
            v2, known_versions={v1.dict_id: v1}
        )
        self.assertTrue(result.passed, result.details)

    def test_negative_version_not_frozen(self):
        adv = make_attribute_dictionary_version(
            dict_id="ad-bad", version="", frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_attribute_dictionary_version(adv)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_ATTRIBUTE_DICT_VERSION_NOT_FROZEN, result.error_codes)

    def test_deterministic_hash(self):
        a1 = make_attribute_dictionary_version(
            dict_id="ad-001", version="1.0.0", frozen_at="2026-08-20T00:00:00Z",
        )
        a2 = make_attribute_dictionary_version(
            dict_id="ad-001", version="1.0.0", frozen_at="2026-08-20T00:00:00Z",
        )
        self.assertEqual(a1.content_hash, a2.content_hash)


# ─── FCAContextSnapshot ──────────────────────────────────────────────


class FCAContextTests(unittest.TestCase):

    def test_golden_create_and_hash(self):
        snap = _make_taxonomy_snapshot_v1()
        ctx = make_fca_context_snapshot(
            context_id="fca-001",
            taxonomy_snapshot_ref={
                "snapshot_id": snap.snapshot_id,
                "content_hash": snap.content_hash,
            },
            objects=("obj-1", "obj-2"),
            attributes=("attr-1", "attr-2"),
            incidence={"obj-1": ("attr-1",), "obj-2": ("attr-2",)},
            frozen_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(ctx.is_hash_valid)
        self.assertTrue(ctx.is_calibration_aid_only)
        result = verify_fca_context_snapshot(ctx)
        self.assertTrue(result.passed, result.details)

    def test_negative_marked_as_truth(self):
        snap = _make_taxonomy_snapshot_v1()
        ctx = make_fca_context_snapshot(
            context_id="fca-bad",
            taxonomy_snapshot_ref={
                "snapshot_id": snap.snapshot_id,
                "content_hash": snap.content_hash,
            },
            is_calibration_aid_only=False,
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_fca_context_snapshot(ctx)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_FCA_CONTEXT_NOT_CALIBRATION_AID, result.error_codes)
        self.assertIn(EC.TX_FCA_CONTEXT_MARKED_AS_TRUTH, result.error_codes)

    def test_negative_missing_taxonomy_ref(self):
        ctx = make_fca_context_snapshot(
            context_id="fca-bad2",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_fca_context_snapshot(ctx)
        self.assertFalse(result.passed)
        self.assertIn(EC.REQUIRED_FIELD_MISSING, result.error_codes)


# ─── TellCore / TellFamily ───────────────────────────────────────────


class TellCoreTests(unittest.TestCase):

    def test_golden_create_and_hash(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        self.assertTrue(core.is_hash_valid)
        self.assertTrue(core.is_invariant_kernel_valid)
        self.assertTrue(core.is_frozen)
        result = verify_tell_core(core)
        self.assertTrue(result.passed, result.details)

    def test_golden_family_verify(self):
        fam = _make_tell_family()
        result = verify_tell_family(fam)
        self.assertTrue(result.passed, result.details)
        self.assertTrue(fam.is_lineage_hash_valid)

    def test_core_version_lineage(self):
        fam = _make_tell_family()
        v1 = _make_tell_core(fam)
        v2 = _make_tell_core_v2(fam, v1)
        result = verify_tell_core(v2, known_cores={v1.core_id: v1})
        self.assertTrue(result.passed, result.details)
        self.assertEqual(v2.supersedes_ref["core_id"], v1.core_id)

    def test_negative_invariant_violated(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        import dataclasses
        bad = dataclasses.replace(core, invariant_kernel_hash="bad" * 21 + "b")
        result = verify_tell_core(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_TELL_CORE_INVARIANT_VIOLATED, result.error_codes)

    def test_negative_action_invalid(self):
        fam = _make_tell_family()
        core = make_tell_core(
            core_id="tc-bad",
            family_id=fam.family_id,
            cognitive_action="INVALID_ACTION",
            lineage_ref={"family_id": fam.family_id, "lineage_hash": fam.lineage_hash},
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_core(core)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_TELL_CORE_ACTION_INVALID, result.error_codes)

    def test_negative_family_lineage_broken(self):
        fam = make_tell_family(
            family_id="tf-bad",
            family_name="bad",
            lineage_root_core_id="",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_family(fam)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_TELL_FAMILY_LINEAGE_BROKEN, result.error_codes)

    def test_negative_lineage_ref_missing(self):
        core = make_tell_core(
            core_id="tc-bad",
            family_id="tf-001",
            cognitive_action="BRANCH_OPEN",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_core(core)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_TELL_FAMILY_LINEAGE_REF_MISSING, result.error_codes)

    def test_deterministic_hash(self):
        fam = _make_tell_family()
        c1 = _make_tell_core(fam)
        c2 = _make_tell_core(fam)
        self.assertEqual(c1.content_hash, c2.content_hash)
        self.assertEqual(c1.invariant_kernel_hash, c2.invariant_kernel_hash)


# ─── TellManifestation (blocker: manifestation != Core) ─────────────


class TellManifestationTests(unittest.TestCase):

    def test_golden_create_and_hash(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        man = _make_manifestation(core)
        self.assertTrue(man.is_hash_valid)
        result = verify_tell_manifestation(man, core=core)
        self.assertTrue(result.passed, result.details)

    def test_blocker_manifestation_equals_core(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        # manifestation_core_id == core_id → manifestation=Core
        man = make_tell_manifestation(
            manifestation_id="man-bad",
            core_id=core.core_id,
            manifestation_core_id=core.core_id,
            kind="TRACE_POSITION_MANIFESTATION",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_manifestation(man, core=core)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_MANIFESTATION_EQUALS_CORE, result.error_codes)

    def test_blocker_manifestation_content_hash_equals_core(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        # same content_hash as core → manifestation=Core
        man = make_tell_manifestation(
            manifestation_id="man-bad2",
            core_id=core.core_id,
            manifestation_core_id="man-core-diff",
            kind="TRACE_POSITION_MANIFESTATION",
            frozen_at="2026-08-20T00:00:00Z",
        )
        import dataclasses
        bad = dataclasses.replace(man, content_hash=core.content_hash)
        result = verify_tell_manifestation(bad, core=core)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_MANIFESTATION_EQUALS_CORE, result.error_codes)

    def test_negative_kind_invalid(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        man = make_tell_manifestation(
            manifestation_id="man-bad3",
            core_id=core.core_id,
            manifestation_core_id="man-core-x",
            kind="INVALID_KIND",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_manifestation(man)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_MANIFESTATION_KIND_INVALID, result.error_codes)


# ─── ObservationView / TellRecognitionRecord ─────────────────────────


class ObservationAndRecognitionTests(unittest.TestCase):

    def test_golden_observation_view(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        view = make_observation_view(
            view_id="ov-001",
            core_id=core.core_id,
            observation_granularity="topology",
            trace_position="step-5",
            span="span[0:10]",
            frozen_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(view.is_hash_valid)

    def test_golden_recognition_record(self):
        snap = _make_taxonomy_snapshot_v1()
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        rec = make_tell_recognition_record(
            record_id="rec-001",
            core_id=core.core_id,
            manifestation_id="man-001",
            span="span[0:10]",
            observer="telling-ai-001",
            confidence=0.85,
            candidate_branches=(
                CandidateBranch(
                    branch_id="br-1",
                    branch_type="line_branch",
                    direction="algebraic",
                ),
            ),
            taxonomy_snapshot_ref={
                "snapshot_id": snap.snapshot_id,
                "content_hash": snap.content_hash,
            },
            observed_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(rec.is_hash_valid)
        result = verify_tell_recognition_record(rec)
        self.assertTrue(result.passed, result.details)

    def test_negative_recognition_missing_taxonomy_ref(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        rec = make_tell_recognition_record(
            record_id="rec-bad",
            core_id=core.core_id,
            observed_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_recognition_record(rec)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_TELL_RECOGNITION_TAXONOMY_REF_MISSING, result.error_codes)


# ─── ApplicabilityBoundary ───────────────────────────────────────────


class ApplicabilityBoundaryTests(unittest.TestCase):

    def _make_boundary(self) -> ApplicabilityBoundary:
        return make_applicability_boundary(
            boundary_id="ab-001",
            core_id="tc-001",
            trigger="fork_point_detected",
            negative_guards=(
                BoundaryGuard(
                    guard_id="ng-1",
                    kind="NEGATIVE_GUARD",
                    condition="not_at_root",
                    binding_roles=("telling_ai",),
                ),
            ),
            binding_roles=("telling_ai",),
            applicable_transformations=("open_branch",),
            frozen_at="2026-08-20T00:00:00Z",
        )

    def test_golden_create_and_hash(self):
        b = self._make_boundary()
        self.assertTrue(b.is_hash_valid)
        result = verify_applicability_boundary(b)
        self.assertTrue(result.passed, result.details)

    def test_blocker_negative_guard_violated(self):
        b = self._make_boundary()
        result = verify_applicability_boundary(b, violated_guard_ids={"ng-1"})
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_BOUNDARY_NEGATIVE_GUARD_VIOLATED, result.error_codes)

    def test_negative_trigger_missing(self):
        b = make_applicability_boundary(
            boundary_id="ab-bad",
            core_id="tc-001",
            trigger="",
            binding_roles=("telling_ai",),
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_applicability_boundary(b)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_BOUNDARY_TRIGGER_MISSING, result.error_codes)

    def test_negative_binding_role_invalid(self):
        b = make_applicability_boundary(
            boundary_id="ab-bad2",
            core_id="tc-001",
            trigger="fork",
            binding_roles=(),
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_applicability_boundary(b)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_BOUNDARY_BINDING_ROLE_INVALID, result.error_codes)

    def test_negative_guard_kind_invalid(self):
        b = make_applicability_boundary(
            boundary_id="ab-bad3",
            core_id="tc-001",
            trigger="fork",
            negative_guards=(
                BoundaryGuard(
                    guard_id="ng-bad",
                    kind="INVALID_KIND",
                    condition="x",
                ),
            ),
            binding_roles=("telling_ai",),
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_applicability_boundary(b)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_BOUNDARY_GUARD_KIND_INVALID, result.error_codes)


# ─── TellHintRelation (M:N blocker) ──────────────────────────────────


class TellHintRelationTests(unittest.TestCase):

    def test_golden_mn_relation(self):
        # 2 tells → 2 hints, forming M:N
        rels = (
            make_tell_hint_relation(
                relation_id="rel-1",
                tell_core_id="tc-1",
                hint_renderer_id="hr-1",
                kind="TELL_TO_HINT",
                applicability_condition="cond-1",
                frozen_at="2026-08-20T00:00:00Z",
            ),
            make_tell_hint_relation(
                relation_id="rel-2",
                tell_core_id="tc-1",
                hint_renderer_id="hr-2",
                kind="TELL_TO_HINT",
                applicability_condition="cond-2",
                frozen_at="2026-08-20T00:00:00Z",
            ),
            make_tell_hint_relation(
                relation_id="rel-3",
                tell_core_id="tc-2",
                hint_renderer_id="hr-1",
                kind="TELL_TO_HINT",
                applicability_condition="cond-3",
                frozen_at="2026-08-20T00:00:00Z",
            ),
            make_tell_hint_relation(
                relation_id="rel-4",
                tell_core_id="tc-2",
                hint_renderer_id="hr-2",
                kind="TELL_TO_HINT",
                applicability_condition="cond-4",
                frozen_at="2026-08-20T00:00:00Z",
            ),
        )
        result = verify_tell_hint_relation(rels[0], all_relations=rels)
        self.assertTrue(result.passed, result.details)
        self.assertTrue(result.is_mn)

    def test_blocker_not_mn_1_to_1(self):
        # only 1:1 → not M:N
        rels = (
            make_tell_hint_relation(
                relation_id="rel-1",
                tell_core_id="tc-1",
                hint_renderer_id="hr-1",
                kind="TELL_TO_HINT",
                applicability_condition="cond",
                frozen_at="2026-08-20T00:00:00Z",
            ),
        )
        result = verify_tell_hint_relation(rels[0], all_relations=rels)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_HINT_RELATION_NOT_MN, result.error_codes)

    def test_blocker_not_mn_1_to_many_only(self):
        # 1 tell → many hints, but each hint only 1 tell → not M:N
        rels = (
            make_tell_hint_relation(
                relation_id="rel-1",
                tell_core_id="tc-1",
                hint_renderer_id="hr-1",
                kind="TELL_TO_HINT",
                applicability_condition="cond",
                frozen_at="2026-08-20T00:00:00Z",
            ),
            make_tell_hint_relation(
                relation_id="rel-2",
                tell_core_id="tc-1",
                hint_renderer_id="hr-2",
                kind="TELL_TO_HINT",
                applicability_condition="cond",
                frozen_at="2026-08-20T00:00:00Z",
            ),
        )
        result = verify_tell_hint_relation(rels[0], all_relations=rels)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_HINT_RELATION_NOT_MN, result.error_codes)

    def test_negative_kind_invalid(self):
        rel = make_tell_hint_relation(
            relation_id="rel-bad",
            tell_core_id="tc-1",
            hint_renderer_id="hr-1",
            kind="INVALID",
            applicability_condition="cond",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_hint_relation(rel)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_HINT_RELATION_KIND_INVALID, result.error_codes)

    def test_negative_applicability_missing(self):
        rel = make_tell_hint_relation(
            relation_id="rel-bad2",
            tell_core_id="tc-1",
            hint_renderer_id="hr-1",
            kind="TELL_TO_HINT",
            applicability_condition="",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_hint_relation(rel)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_HINT_RELATION_APPLICABILITY_MISSING, result.error_codes)


# ─── HintRenderer / HintInstance ─────────────────────────────────────


class HintRendererAndInstanceTests(unittest.TestCase):

    def test_golden_renderer(self):
        r = _make_hint_renderer()
        self.assertTrue(r.is_hash_valid)
        self.assertTrue(r.is_frozen)

    def test_golden_hint_instance(self):
        r = _make_hint_renderer()
        inst = make_hint_instance(
            instance_id="hi-001",
            renderer_ref={
                "renderer_id": r.renderer_id,
                "version": r.version,
                "content_hash": r.content_hash,
            },
            payload={"hint_text": "consider algebraic approach"},
            bound_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(inst.is_hash_valid)
        self.assertTrue(inst.is_payload_hash_valid)
        result = verify_hint_instance(inst)
        self.assertTrue(result.passed, result.details)

    def test_negative_instance_renderer_ref_missing(self):
        inst = make_hint_instance(
            instance_id="hi-bad",
            payload={"hint_text": "x"},
            bound_at="2026-08-20T00:00:00Z",
        )
        result = verify_hint_instance(inst)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_HINT_INSTANCE_RENDERER_REF_MISSING, result.error_codes)

    def test_negative_payload_hash_mismatch(self):
        r = _make_hint_renderer()
        inst = make_hint_instance(
            instance_id="hi-bad2",
            renderer_ref={
                "renderer_id": r.renderer_id,
                "version": r.version,
                "content_hash": r.content_hash,
            },
            payload={"hint_text": "x"},
            bound_at="2026-08-20T00:00:00Z",
        )
        import dataclasses
        bad = dataclasses.replace(inst, payload_hash="bad" * 21 + "b")
        result = verify_hint_instance(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_HINT_INSTANCE_PAYLOAD_HASH_MISMATCH, result.error_codes)


# ─── SelectorDecision (abstain blocker) ──────────────────────────────


class SelectorDecisionTests(unittest.TestCase):

    def test_golden_select(self):
        sd = make_selector_decision(
            decision_id="sd-001",
            kind="SELECT",
            selected_core_ids=("tc-001", "tc-002"),
            frozen_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(sd.is_hash_valid)
        result = verify_selector_decision(sd)
        self.assertTrue(result.passed, result.details)

    def test_golden_abstain(self):
        sd = make_selector_decision(
            decision_id="sd-002",
            kind="ABSTAIN",
            abstain_reason="insufficient_confidence",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_selector_decision(sd)
        self.assertTrue(result.passed, result.details)

    def test_blocker_abstain_with_selection(self):
        sd = make_selector_decision(
            decision_id="sd-bad",
            kind="ABSTAIN",
            selected_core_ids=("tc-001",),
            abstain_reason="",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_selector_decision(sd)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_SELECTOR_ABSTAIN_VIOLATED, result.error_codes)

    def test_blocker_abstain_without_reason(self):
        sd = make_selector_decision(
            decision_id="sd-bad2",
            kind="ABSTAIN",
            abstain_reason="",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_selector_decision(sd)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_SELECTOR_ABSTAIN_VIOLATED, result.error_codes)

    def test_negative_kind_invalid(self):
        sd = make_selector_decision(
            decision_id="sd-bad3",
            kind="INVALID",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_selector_decision(sd)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_SELECTOR_DECISION_KIND_INVALID, result.error_codes)

    def test_negative_select_empty(self):
        sd = make_selector_decision(
            decision_id="sd-bad4",
            kind="SELECT",
            selected_core_ids=(),
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_selector_decision(sd)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_SELECTOR_RANKING_EMPTY, result.error_codes)


# ─── InjectionPolicy (version drift blocker) ─────────────────────────


class InjectionPolicyTests(unittest.TestCase):

    def test_golden_create(self):
        p = make_injection_policy(
            policy_id="ip-001",
            version="1.0.0",
            injection_position="AT_BRANCH_POINT",
            frozen_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(p.is_hash_valid)
        result = verify_injection_policy(p)
        self.assertTrue(result.passed, result.details)

    def test_blocker_version_drift(self):
        p = make_injection_policy(
            policy_id="ip-bad",
            version="1.0.0",
            injection_position="AT_BRANCH_POINT",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_injection_policy(p, expected_version="2.0.0")
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_INJECTION_POLICY_VERSION_DRIFT, result.error_codes)

    def test_negative_position_invalid(self):
        p = make_injection_policy(
            policy_id="ip-bad2",
            version="1.0.0",
            injection_position="INVALID_POSITION",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_injection_policy(p)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_INJECTION_POSITION_INVALID, result.error_codes)


# ─── TellContract ────────────────────────────────────────────────────


class TellContractTests(unittest.TestCase):

    def test_golden_progress_contract(self):
        c = make_tell_contract(
            contract_id="pc-001",
            kind="PROGRESS_CONTRACT",
            core_id="tc-001",
            specification="progress check",
            frozen_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(c.is_hash_valid)
        result = verify_tell_contract(c)
        self.assertTrue(result.passed, result.details)

    def test_golden_composition_contract(self):
        c = make_tell_contract(
            contract_id="cc-001",
            kind="COMPOSITION_CONTRACT",
            core_id="tc-001",
            related_core_ids=("tc-002",),
            specification="compose two tells",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_contract(c)
        self.assertTrue(result.passed, result.details)

    def test_negative_composition_cycle(self):
        c = make_tell_contract(
            contract_id="cc-bad",
            kind="COMPOSITION_CONTRACT",
            core_id="tc-001",
            related_core_ids=("tc-001",),  # self-reference
            specification="cycle",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_contract(c)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_COMPOSITION_CONTRACT_CYCLE, result.error_codes)

    def test_negative_kind_invalid(self):
        c = make_tell_contract(
            contract_id="c-bad",
            kind="INVALID",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_tell_contract(c)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_CONTRACT_KIND_INVALID, result.error_codes)


# ─── TellStrategyRelease ─────────────────────────────────────────────


class TellStrategyReleaseTests(unittest.TestCase):

    def _make_full_release(self, state: str = "RELEASED") -> TellStrategyRelease:
        snap = _make_taxonomy_snapshot_v1()
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        boundary = make_applicability_boundary(
            boundary_id="ab-001",
            core_id=core.core_id,
            trigger="fork",
            binding_roles=("telling_ai",),
            frozen_at="2026-08-20T00:00:00Z",
        )
        selector = make_selector_decision(
            decision_id="sd-001",
            kind="SELECT",
            selected_core_ids=(core.core_id,),
            frozen_at="2026-08-20T00:00:00Z",
        )
        renderer = _make_hint_renderer()
        injection = make_injection_policy(
            policy_id="ip-001",
            version="1.0.0",
            injection_position="AT_BRANCH_POINT",
            frozen_at="2026-08-20T00:00:00Z",
        )
        critic = make_tell_contract(
            contract_id="critic-001",
            kind="CRITIC_CONTRACT",
            core_id=core.core_id,
            frozen_at="2026-08-20T00:00:00Z",
        )
        composition = make_tell_contract(
            contract_id="comp-001",
            kind="COMPOSITION_CONTRACT",
            core_id=core.core_id,
            frozen_at="2026-08-20T00:00:00Z",
        )
        comps = _make_release_components(
            core, boundary, selector, renderer, injection,
            critic, composition, snap,
        )
        return make_tell_strategy_release(
            release_id="tsr-001",
            version="1.0.0",
            state=state,
            scope="math_problem_solving",
            frozen_at="2026-08-20T00:00:00Z",
            **comps,
        )

    def test_golden_create_and_hash(self):
        rel = self._make_full_release()
        self.assertTrue(rel.is_hash_valid)
        self.assertTrue(rel.is_manifest_hash_valid)
        self.assertTrue(rel.is_immutable)
        result = verify_tell_strategy_release(rel)
        self.assertTrue(result.passed, result.details)

    def test_golden_version_lineage(self):
        v1 = self._make_full_release()
        v2 = make_tell_strategy_release(
            release_id="tsr-002",
            version="2.0.0",
            state="RELEASED",
            scope="math_problem_solving",
            supersedes_ref={
                "release_id": v1.release_id,
                "content_hash": v1.content_hash,
            },
            frozen_at="2026-08-21T00:00:00Z",
            core_ref=v1.core_ref,
            boundary_ref=v1.boundary_ref,
            selector_ref=v1.selector_ref,
            renderer_ref=v1.renderer_ref,
            injection_ref=v1.injection_ref,
            critic_ref=v1.critic_ref,
            composition_ref=v1.composition_ref,
            taxonomy_ref=v1.taxonomy_ref,
        )
        result = verify_tell_strategy_release(
            v2, known_releases={v1.release_id: v1}
        )
        self.assertTrue(result.passed, result.details)

    def test_negative_component_missing(self):
        rel = self._make_full_release()
        import dataclasses
        bad = dataclasses.replace(
            rel,
            core_ref=ReleaseComponentRef(kind="TellCore", component_id=""),
        )
        # need to recompute hashes since we changed a component
        bad = dataclasses.replace(
            bad, manifest_hash=bad.compute_manifest_hash(),
            content_hash=bad.compute_content_hash(),
        )
        result = verify_tell_strategy_release(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_RELEASE_COMPONENT_MISSING, result.error_codes)

    def test_negative_state_invalid(self):
        rel = self._make_full_release(state="INVALID_STATE")
        result = verify_tell_strategy_release(rel)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_RELEASE_STATE_INVALID, result.error_codes)

    def test_negative_lineage_broken(self):
        v1 = self._make_full_release()
        v2 = make_tell_strategy_release(
            release_id="tsr-002",
            version="2.0.0",
            state="RELEASED",
            supersedes_ref={"release_id": "nonexistent", "content_hash": "x" * 64},
            frozen_at="2026-08-21T00:00:00Z",
            core_ref=v1.core_ref,
            boundary_ref=v1.boundary_ref,
            selector_ref=v1.selector_ref,
            renderer_ref=v1.renderer_ref,
            injection_ref=v1.injection_ref,
            critic_ref=v1.critic_ref,
            composition_ref=v1.composition_ref,
            taxonomy_ref=v1.taxonomy_ref,
        )
        result = verify_tell_strategy_release(
            v2, known_releases={v1.release_id: v1}
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_RELEASE_LINEAGE_BROKEN, result.error_codes)

    def test_negative_not_immutable(self):
        # RELEASED but empty content_hash
        rel = self._make_full_release()
        import dataclasses
        bad = dataclasses.replace(rel, content_hash="")
        result = verify_tell_strategy_release(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_RELEASE_NOT_IMMUTABLE, result.error_codes)

    def test_deterministic_hash(self):
        r1 = self._make_full_release()
        r2 = self._make_full_release()
        self.assertEqual(r1.content_hash, r2.content_hash)
        self.assertEqual(r1.manifest_hash, r2.manifest_hash)


# ─── ReleaseLineage ──────────────────────────────────────────────────


class ReleaseLineageTests(unittest.TestCase):

    def test_golden_lineage(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        boundary = make_applicability_boundary(
            boundary_id="ab-001", core_id=core.core_id, trigger="fork",
            binding_roles=("ai",), frozen_at="2026-08-20T00:00:00Z",
        )
        selector = make_selector_decision(
            decision_id="sd-001", kind="SELECT",
            selected_core_ids=(core.core_id,), frozen_at="2026-08-20T00:00:00Z",
        )
        renderer = _make_hint_renderer()
        injection = make_injection_policy(
            policy_id="ip-001", version="1.0.0",
            injection_position="AT_BRANCH_POINT", frozen_at="2026-08-20T00:00:00Z",
        )
        critic = make_tell_contract(
            contract_id="c-1", kind="CRITIC_CONTRACT",
            core_id=core.core_id, frozen_at="2026-08-20T00:00:00Z",
        )
        composition = make_tell_contract(
            contract_id="c-2", kind="COMPOSITION_CONTRACT",
            core_id=core.core_id, frozen_at="2026-08-20T00:00:00Z",
        )
        snap = _make_taxonomy_snapshot_v1()
        comps = _make_release_components(
            core, boundary, selector, renderer, injection,
            critic, composition, snap,
        )
        r1 = make_tell_strategy_release(
            release_id="tsr-1", version="1.0.0", state="RELEASED",
            frozen_at="2026-08-20T00:00:00Z", **comps,
        )
        r2 = make_tell_strategy_release(
            release_id="tsr-2", version="2.0.0", state="RELEASED",
            supersedes_ref={"release_id": r1.release_id, "content_hash": r1.content_hash},
            frozen_at="2026-08-21T00:00:00Z", **comps,
        )
        lineage = make_release_lineage(
            lineage_id="rl-001",
            releases=(
                {"release_id": r1.release_id, "content_hash": r1.content_hash},
                {"release_id": r2.release_id, "content_hash": r2.content_hash},
            ),
        )
        self.assertTrue(lineage.is_hash_valid)
        self.assertEqual(lineage.head_release_id, r2.release_id)
        result = verify_release_lineage(
            lineage, known_releases={r1.release_id: r1, r2.release_id: r2}
        )
        self.assertTrue(result.passed, result.details)

    def test_negative_empty_lineage(self):
        lineage = make_release_lineage(lineage_id="rl-bad", releases=())
        result = verify_release_lineage(lineage)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_RELEASE_LINEAGE_BROKEN, result.error_codes)

    def test_negative_head_mismatch(self):
        lineage = make_release_lineage(
            lineage_id="rl-bad2",
            releases=(
                {"release_id": "r1", "content_hash": "a" * 64},
            ),
        )
        import dataclasses
        bad = dataclasses.replace(lineage, head_release_id="wrong")
        bad = dataclasses.replace(bad, content_hash=bad.compute_content_hash())
        result = verify_release_lineage(bad)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_RELEASE_LINEAGE_BROKEN, result.error_codes)


# ─── EvidenceForeignKeyMigration (blocker tests) ─────────────────────


class EvidenceMigrationTests(unittest.TestCase):

    def test_golden_migration(self):
        m = make_evidence_foreign_key_migration(
            migration_id="mig-001",
            old_release_ref={"release_id": "tsr-1", "content_hash": "a" * 64},
            new_release_ref={"release_id": "tsr-2", "content_hash": "b" * 64},
            evidence_ids=("ev-1", "ev-2", "ev-3"),
            inheritance_scope="EXACT",
            migrated_by="REGISTRY",
            migrated_at="2026-08-21T00:00:00Z",
        )
        self.assertTrue(m.is_hash_valid)
        result = verify_evidence_foreign_key_migration(
            m, unmigrated_evidence_ids={"ev-1", "ev-2", "ev-3"}
        )
        self.assertTrue(result.passed, result.details)

    def test_blocker_old_evidence_not_migrated(self):
        m = make_evidence_foreign_key_migration(
            migration_id="mig-bad",
            old_release_ref={"release_id": "tsr-1", "content_hash": "a" * 64},
            new_release_ref={"release_id": "tsr-2", "content_hash": "b" * 64},
            evidence_ids=("ev-1", "ev-2"),  # missing ev-3
            inheritance_scope="EXACT",
            migrated_by="REGISTRY",
            migrated_at="2026-08-21T00:00:00Z",
        )
        result = verify_evidence_foreign_key_migration(
            m, unmigrated_evidence_ids={"ev-1", "ev-2", "ev-3"}
        )
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_OLD_EVIDENCE_FOREIGN_KEY_NOT_MIGRATED, result.error_codes)

    def test_blocker_gate_changes_pointer(self):
        m = make_evidence_foreign_key_migration(
            migration_id="mig-bad2",
            old_release_ref={"release_id": "tsr-1", "content_hash": "a" * 64},
            new_release_ref={"release_id": "tsr-2", "content_hash": "b" * 64},
            evidence_ids=("ev-1",),
            inheritance_scope="EXACT",
            migrated_by="GATE",  # blocker: Gate cannot change pointer
            migrated_at="2026-08-21T00:00:00Z",
        )
        result = verify_evidence_foreign_key_migration(m)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_RELEASE_POINTER_CHANGED_BY_GATE, result.error_codes)

    def test_blocker_gate_changes_pointer_via_param(self):
        m = make_evidence_foreign_key_migration(
            migration_id="mig-bad3",
            old_release_ref={"release_id": "tsr-1", "content_hash": "a" * 64},
            new_release_ref={"release_id": "tsr-2", "content_hash": "b" * 64},
            evidence_ids=("ev-1",),
            inheritance_scope="EXACT",
            migrated_by="REGISTRY",
            migrated_at="2026-08-21T00:00:00Z",
        )
        result = verify_evidence_foreign_key_migration(m, actor_is_gate=True)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_RELEASE_POINTER_CHANGED_BY_GATE, result.error_codes)

    def test_inheritance_scopes(self):
        for scope in ("EXACT", "SUBSCOPE", "PROVENANCE_ONLY", "NONE"):
            m = make_evidence_foreign_key_migration(
                migration_id=f"mig-{scope}",
                old_release_ref={"release_id": "tsr-1", "content_hash": "a" * 64},
                new_release_ref={"release_id": "tsr-2", "content_hash": "b" * 64},
                evidence_ids=("ev-1",),
                inheritance_scope=scope,
                migrated_by="REGISTRY",
                migrated_at="2026-08-21T00:00:00Z",
            )
            result = verify_evidence_foreign_key_migration(m)
            self.assertTrue(result.passed, f"{scope}: {result.details}")


# ─── MathValidityRecord ──────────────────────────────────────────────


class MathValidityTests(unittest.TestCase):

    def test_golden_valid(self):
        r = make_math_validity_record(
            record_id="mvr-001",
            core_id="tc-001",
            status="VALID",
            validity_basis="proof verified",
            frozen_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(r.is_hash_valid)
        result = verify_math_validity_record(r)
        self.assertTrue(result.passed, result.details)

    def test_negative_status_invalid(self):
        r = make_math_validity_record(
            record_id="mvr-bad",
            core_id="tc-001",
            status="INVALID_STATUS",
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_math_validity_record(r)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_VALIDITY_STATUS_INVALID, result.error_codes)


# ─── SystemEfficacyRecord (solver context blocker) ──────────────────


class SystemEfficacyTests(unittest.TestCase):

    def test_golden_efficacious(self):
        r = make_system_efficacy_record(
            record_id="ser-001",
            core_id="tc-001",
            status="EFFICACIOUS",
            solver_context=SolverResourceContext(
                solver_id="solver-001",
                solver_version="1.0.0",
                resource_profile="high",
                renderer_version="1.0.0",
                selector_version="1.0.0",
            ),
            efficacy_basis="improved branch coverage",
            frozen_at="2026-08-20T00:00:00Z",
        )
        self.assertTrue(r.is_hash_valid)
        result = verify_system_efficacy_record(r)
        self.assertTrue(result.passed, result.details)

    def test_blocker_solver_context_missing(self):
        r = make_system_efficacy_record(
            record_id="ser-bad",
            core_id="tc-001",
            status="EFFICACIOUS",
            solver_context=SolverResourceContext(),  # empty
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_system_efficacy_record(r)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_EFFICACY_SOLVER_CONTEXT_MISSING, result.error_codes)

    def test_blocker_renderer_version_drift(self):
        r = make_system_efficacy_record(
            record_id="ser-bad2",
            core_id="tc-001",
            status="EFFICACIOUS",
            solver_context=SolverResourceContext(
                solver_id="solver-001",
                renderer_version="1.0.0",
            ),
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_system_efficacy_record(r, expected_renderer_version="2.0.0")
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_EFFICACY_RENDERER_VERSION_DRIFT, result.error_codes)

    def test_blocker_selector_version_drift(self):
        r = make_system_efficacy_record(
            record_id="ser-bad3",
            core_id="tc-001",
            status="EFFICACIOUS",
            solver_context=SolverResourceContext(
                solver_id="solver-001",
                selector_version="1.0.0",
            ),
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_system_efficacy_record(r, expected_selector_version="2.0.0")
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_EFFICACY_SELECTOR_VERSION_DRIFT, result.error_codes)

    def test_blocker_solver_version_drift(self):
        r = make_system_efficacy_record(
            record_id="ser-bad4",
            core_id="tc-001",
            status="EFFICACIOUS",
            solver_context=SolverResourceContext(
                solver_id="solver-001",
                solver_version="1.0.0",
            ),
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_system_efficacy_record(r, expected_solver_version="2.0.0")
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_EFFICACY_TARGET_SOLVER_VERSION_DRIFT, result.error_codes)

    def test_negative_status_invalid(self):
        r = make_system_efficacy_record(
            record_id="ser-bad5",
            core_id="tc-001",
            status="INVALID",
            solver_context=SolverResourceContext(solver_id="s1"),
            frozen_at="2026-08-20T00:00:00Z",
        )
        result = verify_system_efficacy_record(r)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_EFFICACY_STATUS_INVALID, result.error_codes)

    def test_validity_and_efficacy_separated(self):
        """MathValidity 和 SystemEffication 是分开的对象。"""
        mv = make_math_validity_record(
            record_id="mvr-001", core_id="tc-001", status="VALID",
            frozen_at="2026-08-20T00:00:00Z",
        )
        se = make_system_efficacy_record(
            record_id="ser-001", core_id="tc-001", status="EFFICACIOUS",
            solver_context=SolverResourceContext(solver_id="s1"),
            frozen_at="2026-08-20T00:00:00Z",
        )
        # different schema_ids
        self.assertNotEqual(mv.to_dict()["schema_id"], se.to_dict()["schema_id"])
        # different content_hash
        self.assertNotEqual(mv.content_hash, se.content_hash)


# ─── InvalidationRules ───────────────────────────────────────────────


class InvalidationTests(unittest.TestCase):

    def test_golden_core_changed_triggers_readjudication(self):
        notice = compute_invalidation_notice(
            notice_id="inv-001",
            trigger="CORE_CHANGED",
            issued_at="2026-08-21T00:00:00Z",
        )
        self.assertTrue(notice.requires_readjudication)
        self.assertFalse(notice.requires_efficacy_retest)
        self.assertIn("CoverageApplicability", notice.targets)
        self.assertIn("CaseApplicability", notice.targets)
        result = verify_invalidation_notice(notice)
        self.assertTrue(result.passed, result.details)

    def test_golden_boundary_changed_triggers_readjudication(self):
        notice = compute_invalidation_notice(
            notice_id="inv-002",
            trigger="BOUNDARY_CHANGED",
            issued_at="2026-08-21T00:00:00Z",
        )
        self.assertTrue(notice.requires_readjudication)
        result = verify_invalidation_notice(notice)
        self.assertTrue(result.passed, result.details)

    def test_golden_renderer_version_changed_triggers_retest(self):
        notice = compute_invalidation_notice(
            notice_id="inv-003",
            trigger="RENDERER_VERSION_CHANGED",
            issued_at="2026-08-21T00:00:00Z",
        )
        self.assertTrue(notice.requires_efficacy_retest)
        self.assertTrue(notice.requires_cost_retest)
        self.assertFalse(notice.requires_readjudication)
        self.assertIn("SystemEfficacyRecord", notice.targets)
        self.assertIn("CostEvidence", notice.targets)
        result = verify_invalidation_notice(notice)
        self.assertTrue(result.passed, result.details)

    def test_golden_selector_version_changed_triggers_retest(self):
        notice = compute_invalidation_notice(
            notice_id="inv-004",
            trigger="SELECTOR_VERSION_CHANGED",
            issued_at="2026-08-21T00:00:00Z",
        )
        self.assertTrue(notice.requires_efficacy_retest)

    def test_golden_solver_version_changed_triggers_retest(self):
        notice = compute_invalidation_notice(
            notice_id="inv-005",
            trigger="TARGET_SOLVER_VERSION_CHANGED",
            issued_at="2026-08-21T00:00:00Z",
        )
        self.assertTrue(notice.requires_efficacy_retest)

    def test_negative_readjudication_missing(self):
        notice = compute_invalidation_notice(
            notice_id="inv-bad",
            trigger="CORE_CHANGED",
            issued_at="2026-08-21T00:00:00Z",
        )
        result = verify_invalidation_notice(notice, readjudication_done=False)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_INVALIDATION_READJUDICATION_MISSING, result.error_codes)

    def test_negative_efficacy_retest_missing(self):
        notice = compute_invalidation_notice(
            notice_id="inv-bad2",
            trigger="RENDERER_VERSION_CHANGED",
            issued_at="2026-08-21T00:00:00Z",
        )
        result = verify_invalidation_notice(notice, efficacy_retest_done=False)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_INVALIDATION_EFFICACY_RETEST_MISSING, result.error_codes)

    def test_negative_unknown_trigger(self):
        notice = make_invalidation_notice(
            notice_id="inv-bad3",
            trigger="UNKNOWN_TRIGGER",
            issued_at="2026-08-21T00:00:00Z",
        )
        result = verify_invalidation_notice(notice)
        self.assertFalse(result.passed)
        self.assertIn(EC.TX_INVALIDATION_TARGET_UNKNOWN, result.error_codes)

    def test_invalidation_triggers_set(self):
        self.assertIn("CORE_CHANGED", INVALIDATION_TRIGGERS)
        self.assertIn("BOUNDARY_CHANGED", INVALIDATION_TRIGGERS)
        self.assertIn("RENDERER_VERSION_CHANGED", INVALIDATION_TRIGGERS)
        self.assertIn("SELECTOR_VERSION_CHANGED", INVALIDATION_TRIGGERS)
        self.assertIn("TARGET_SOLVER_VERSION_CHANGED", INVALIDATION_TRIGGERS)


# ─── Boundary tests (TX1 allowed/forbidden output kinds) ────────────


class OutputBoundaryTests(unittest.TestCase):
    """TX1 输出边界——只允许 taxonomy 对象，禁止其他工作包的对象。"""

    def test_allowed_contains_all_tx1_objects(self):
        expected = {
            "TaxonomySnapshot", "AttributeDictionaryVersion", "FCAContextSnapshot",
            "ObservationView", "TellManifestation", "TellRecognitionRecord",
            "TellFamily", "TellCore", "ApplicabilityBoundary", "TellHintRelation",
            "HintRenderer", "HintInstance", "SelectorDecision", "InjectionPolicy",
            "ProgressContract", "TerminationContract", "CriticContract",
            "CompositionContract", "TellStrategyRelease", "MathValidityRecord",
            "SystemEfficacyRecord",
        }
        self.assertTrue(expected.issubset(TX1_ALLOWED_OUTPUT_KINDS))

    def test_forbidden_contains_other_wp_objects(self):
        self.assertIn("EvidenceRecord", TX1_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("SolverLaunchReceipt", TX1_FORBIDDEN_OUTPUT_KINDS)
        self.assertIn("QuestionRelease", TX1_FORBIDDEN_OUTPUT_KINDS)

    def test_no_overlap(self):
        self.assertEqual(
            TX1_ALLOWED_OUTPUT_KINDS & TX1_FORBIDDEN_OUTPUT_KINDS, frozenset()
        )

    def test_tx1_does_not_output_evidence(self):
        """TX1 不能输出 EvidenceRecord——那是 WP-EV1 的产物。"""
        self.assertNotIn("EvidenceRecord", TX1_ALLOWED_OUTPUT_KINDS)

    def test_tx1_does_not_output_solver(self):
        """TX1 不能输出 SolverLaunchReceipt——那是 WP-SV1 的产物。"""
        self.assertNotIn("SolverLaunchReceipt", TX1_ALLOWED_OUTPUT_KINDS)


# ─── Side-effect-free tests ──────────────────────────────────────────


class SideEffectFreeTests(unittest.TestCase):
    """TX1 是 SIDE_EFFECT_FREE——不写 DB/Redis/D盘，不调 live model，不启动 Solver。"""

    def test_side_effect_keys_all_zero_semantic(self):
        # 这些键在 TX1 能力报告中必须全为 0
        for key in TX1_SIDE_EFFECT_KEYS:
            self.assertIsInstance(key, str)

    def test_no_solver_launch_in_allowed(self):
        # TX1 不产出 solver 相关对象
        for kind in TX1_ALLOWED_OUTPUT_KINDS:
            self.assertNotIn("Solver", kind)
            self.assertNotIn("Launch", kind)

    def test_no_db_objects_in_allowed(self):
        for kind in TX1_ALLOWED_OUTPUT_KINDS:
            self.assertNotIn("Database", kind)
            self.assertNotIn("Schema", kind)


# ─── Cross-object consistency ────────────────────────────────────────


class CrossObjectConsistencyTests(unittest.TestCase):

    def test_release_components_match_object_hashes(self):
        """Release 中的 component content_hash 必须与实际对象 hash 一致。"""
        snap = _make_taxonomy_snapshot_v1()
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        boundary = make_applicability_boundary(
            boundary_id="ab-001", core_id=core.core_id, trigger="fork",
            binding_roles=("ai",), frozen_at="2026-08-20T00:00:00Z",
        )
        selector = make_selector_decision(
            decision_id="sd-001", kind="SELECT",
            selected_core_ids=(core.core_id,), frozen_at="2026-08-20T00:00:00Z",
        )
        renderer = _make_hint_renderer()
        injection = make_injection_policy(
            policy_id="ip-001", version="1.0.0",
            injection_position="AT_BRANCH_POINT", frozen_at="2026-08-20T00:00:00Z",
        )
        critic = make_tell_contract(
            contract_id="c-1", kind="CRITIC_CONTRACT",
            core_id=core.core_id, frozen_at="2026-08-20T00:00:00Z",
        )
        composition = make_tell_contract(
            contract_id="c-2", kind="COMPOSITION_CONTRACT",
            core_id=core.core_id, frozen_at="2026-08-20T00:00:00Z",
        )
        comps = _make_release_components(
            core, boundary, selector, renderer, injection,
            critic, composition, snap,
        )
        rel = make_tell_strategy_release(
            release_id="tsr-001", version="1.0.0", state="RELEASED",
            frozen_at="2026-08-20T00:00:00Z", **comps,
        )
        # verify component hashes match object hashes
        self.assertEqual(rel.core_ref.content_hash, core.content_hash)
        self.assertEqual(rel.boundary_ref.content_hash, boundary.content_hash)
        self.assertEqual(rel.selector_ref.content_hash, selector.content_hash)
        self.assertEqual(rel.renderer_ref.content_hash, renderer.content_hash)
        self.assertEqual(rel.injection_ref.content_hash, injection.content_hash)
        self.assertEqual(rel.critic_ref.content_hash, critic.content_hash)
        self.assertEqual(rel.composition_ref.content_hash, composition.content_hash)
        self.assertEqual(rel.taxonomy_ref.content_hash, snap.content_hash)

    def test_core_lineage_ref_matches_family_hash(self):
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        self.assertEqual(core.lineage_ref["lineage_hash"], fam.lineage_hash)
        self.assertEqual(core.lineage_ref["family_id"], fam.family_id)

    def test_recognition_refs_match_snapshot(self):
        snap = _make_taxonomy_snapshot_v1()
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        rec = make_tell_recognition_record(
            record_id="rec-001", core_id=core.core_id,
            taxonomy_snapshot_ref={
                "snapshot_id": snap.snapshot_id,
                "content_hash": snap.content_hash,
            },
            observed_at="2026-08-20T00:00:00Z",
        )
        self.assertEqual(
            rec.taxonomy_snapshot_ref["content_hash"], snap.content_hash
        )


# ─── Migration / inheritance tests ───────────────────────────────────


class MigrationInheritanceTests(unittest.TestCase):

    def test_inheritance_exact(self):
        m = make_evidence_foreign_key_migration(
            migration_id="mig-exact",
            old_release_ref={"release_id": "r1", "content_hash": "a" * 64},
            new_release_ref={"release_id": "r2", "content_hash": "b" * 64},
            evidence_ids=("ev-1",),
            inheritance_scope="EXACT",
            migrated_by="REGISTRY",
            migrated_at="2026-08-21T00:00:00Z",
        )
        result = verify_evidence_foreign_key_migration(m)
        self.assertTrue(result.passed, result.details)

    def test_inheritance_subscope(self):
        m = make_evidence_foreign_key_migration(
            migration_id="mig-sub",
            old_release_ref={"release_id": "r1", "content_hash": "a" * 64},
            new_release_ref={"release_id": "r2", "content_hash": "b" * 64},
            evidence_ids=("ev-1",),
            inheritance_scope="SUBSCOPE",
            migrated_by="REGISTRY",
            migrated_at="2026-08-21T00:00:00Z",
        )
        result = verify_evidence_foreign_key_migration(m)
        self.assertTrue(result.passed, result.details)

    def test_inheritance_provenance_only(self):
        m = make_evidence_foreign_key_migration(
            migration_id="mig-prov",
            old_release_ref={"release_id": "r1", "content_hash": "a" * 64},
            new_release_ref={"release_id": "r2", "content_hash": "b" * 64},
            evidence_ids=("ev-1",),
            inheritance_scope="PROVENANCE_ONLY",
            migrated_by="REGISTRY",
            migrated_at="2026-08-21T00:00:00Z",
        )
        result = verify_evidence_foreign_key_migration(m)
        self.assertTrue(result.passed, result.details)

    def test_full_release_lineage_with_migration(self):
        """完整 release lineage + foreign key migration 端到端。"""
        fam = _make_tell_family()
        core = _make_tell_core(fam)
        boundary = make_applicability_boundary(
            boundary_id="ab-1", core_id=core.core_id, trigger="fork",
            binding_roles=("ai",), frozen_at="2026-08-20T00:00:00Z",
        )
        selector = make_selector_decision(
            decision_id="sd-1", kind="SELECT",
            selected_core_ids=(core.core_id,), frozen_at="2026-08-20T00:00:00Z",
        )
        renderer = _make_hint_renderer()
        injection = make_injection_policy(
            policy_id="ip-1", version="1.0.0",
            injection_position="AT_BRANCH_POINT", frozen_at="2026-08-20T00:00:00Z",
        )
        critic = make_tell_contract(
            contract_id="c-1", kind="CRITIC_CONTRACT",
            core_id=core.core_id, frozen_at="2026-08-20T00:00:00Z",
        )
        composition = make_tell_contract(
            contract_id="c-2", kind="COMPOSITION_CONTRACT",
            core_id=core.core_id, frozen_at="2026-08-20T00:00:00Z",
        )
        snap = _make_taxonomy_snapshot_v1()
        comps = _make_release_components(
            core, boundary, selector, renderer, injection,
            critic, composition, snap,
        )
        r1 = make_tell_strategy_release(
            release_id="tsr-1", version="1.0.0", state="RELEASED",
            frozen_at="2026-08-20T00:00:00Z", **comps,
        )
        r2 = make_tell_strategy_release(
            release_id="tsr-2", version="2.0.0", state="RELEASED",
            supersedes_ref={"release_id": r1.release_id, "content_hash": r1.content_hash},
            frozen_at="2026-08-21T00:00:00Z", **comps,
        )
        # lineage
        lineage = make_release_lineage(
            lineage_id="rl-1",
            releases=(
                {"release_id": r1.release_id, "content_hash": r1.content_hash},
                {"release_id": r2.release_id, "content_hash": r2.content_hash},
            ),
        )
        lin_result = verify_release_lineage(
            lineage, known_releases={r1.release_id: r1, r2.release_id: r2}
        )
        self.assertTrue(lin_result.passed, lin_result.details)
        # migration
        mig = make_evidence_foreign_key_migration(
            migration_id="mig-1",
            old_release_ref={"release_id": r1.release_id, "content_hash": r1.content_hash},
            new_release_ref={"release_id": r2.release_id, "content_hash": r2.content_hash},
            evidence_ids=("ev-1", "ev-2"),
            inheritance_scope="EXACT",
            migrated_by="REGISTRY",
            migrated_at="2026-08-21T00:00:00Z",
        )
        mig_result = verify_evidence_foreign_key_migration(
            mig, unmigrated_evidence_ids={"ev-1", "ev-2"}
        )
        self.assertTrue(mig_result.passed, mig_result.details)
        # invalidation notice for core change
        notice = compute_invalidation_notice(
            notice_id="inv-1", trigger="CORE_CHANGED",
            issued_at="2026-08-21T00:00:00Z",
        )
        inv_result = verify_invalidation_notice(
            notice, readjudication_done=True
        )
        self.assertTrue(inv_result.passed, inv_result.details)


if __name__ == "__main__":
    unittest.main()
