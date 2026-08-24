"""Regression and adversarial tests for the isolated solve-side pipeline."""

from __future__ import annotations

import ast
from copy import deepcopy
import hashlib
import importlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from system.solve_vein_analysis.cli import (
    CliContractError,
    analyze_to_directory,
    default_assets_dir,
    validate_asset_manifest,
)
from system.solve_vein_analysis.fca import (
    enumerate_closed_intents_bruteforce,
    enumerate_closed_intents_next_closure,
)
from system.solve_vein_analysis.integrity import implementation_tree_receipt
from system.solve_vein_analysis.models import (
    ReasoningTrajectory,
    TrajectoryValidationError,
)
from system.solve_vein_analysis.pipeline import (
    analyze_incrementally,
    analyze_trajectory,
    build_reasoning_dag,
    build_state_context,
    build_transition_context,
    edge_identity_set,
    project_flattened_edges,
    project_tree_edges,
)


HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"
PACKAGE_ROOT = HERE.parents[1] / "solve_vein_analysis"
PROTECTED_BASELINE = HERE / "protected_absorb_baseline_v2.sha256"
PROTECTED_BASELINE_SHA256 = (
    "2085e1c91bac1909b01ab3dd74f0845b9d2484b77e34d0a7cb9f2357f0b5f3a7"
)


def load_raw(case_slug: str) -> dict[str, object]:
    return json.loads((FIXTURES / f"{case_slug}.trajectory.json").read_text())


def load_case(case_slug: str) -> tuple[ReasoningTrajectory, dict[str, object]]:
    trajectory = ReasoningTrajectory.from_dict(load_raw(case_slug))
    expected = json.loads((FIXTURES / f"{case_slug}.expected.json").read_text())
    return trajectory, expected


def assert_validation_code(
    testcase: unittest.TestCase,
    raw: dict[str, object],
    expected_code: str,
) -> None:
    with testcase.assertRaises(TrajectoryValidationError) as caught:
        ReasoningTrajectory.from_dict(raw)
    testcase.assertEqual(caught.exception.code, expected_code)


class FixtureContractTests(unittest.TestCase):
    CASES = (
        "c1_linear",
        "c2_branch",
        "c3_revisit",
        "c4_merge",
        "c5_composite",
    )

    def test_all_fixtures_match_preregistered_graph_and_trace_contracts(self) -> None:
        for case_slug in self.CASES:
            with self.subTest(case=case_slug):
                trajectory, expected = load_case(case_slug)
                bundle = analyze_trajectory(trajectory)
                actual_edges = edge_identity_set(bundle.dag.edges)
                expected_edges = {tuple(edge) for edge in expected["gold_edges"]}
                self.assertEqual(actual_edges, expected_edges)

                families = {trace.family.value for trace in bundle.traces}
                self.assertTrue(
                    set(expected["required_trace_families"]).issubset(families)
                )
                self.assertTrue(
                    set(expected["forbidden_trace_families"]).isdisjoint(families)
                )
                self.assertEqual(bundle.audit["verdicts"]["live_extraction"], "NOT_TESTED")
                self.assertTrue(bundle.relational_scaling["fixed_point_reached"])

    def test_revisit_occurrences_keep_distinct_identity(self) -> None:
        for case_slug in ("c3_revisit", "c5_composite"):
            with self.subTest(case=case_slug):
                trajectory, expected = load_case(case_slug)
                by_id = {event.event_id: event for event in trajectory.events}
                for earlier_id, later_id in expected["revisit_pairs"]:
                    self.assertNotEqual(earlier_id, later_id)
                    self.assertEqual(
                        by_id[earlier_id].canonical_math_state_id,
                        by_id[later_id].canonical_math_state_id,
                    )
                    self.assertLess(
                        by_id[earlier_id].sequence_index,
                        by_id[later_id].sequence_index,
                    )

    def test_true_merges_keep_every_preregistered_parent(self) -> None:
        for case_slug in ("c4_merge", "c5_composite"):
            with self.subTest(case=case_slug):
                trajectory, expected = load_case(case_slug)
                bundle = analyze_trajectory(trajectory)
                for target_id, parents in expected["merge_parents"].items():
                    actual = {
                        edge.source_event_id
                        for edge in bundle.dag.edges
                        if edge.target_event_id == target_id and edge.relation.value == "MERGE"
                    }
                    self.assertEqual(actual, set(parents))

    def test_batch_and_incremental_reference_are_scientifically_identical(self) -> None:
        for case_slug in self.CASES:
            with self.subTest(case=case_slug):
                trajectory, _ = load_case(case_slug)
                batch = analyze_trajectory(trajectory)
                incremental, journal = analyze_incrementally(trajectory)
                self.assertEqual(
                    batch.scientific_fingerprint,
                    incremental.scientific_fingerprint,
                )
                self.assertEqual(
                    journal["final_scientific_fingerprint"],
                    batch.scientific_fingerprint,
                )
                self.assertEqual(len(journal["prefixes"]), len(trajectory.events))

    def test_next_closure_equals_independent_oracle_on_all_contexts(self) -> None:
        for case_slug in self.CASES:
            trajectory, _ = load_case(case_slug)
            dag = build_reasoning_dag(trajectory)
            for context in (build_state_context(dag), build_transition_context(dag)):
                with self.subTest(case=case_slug, context=context.context_id):
                    self.assertEqual(
                        set(enumerate_closed_intents_next_closure(context)),
                        set(enumerate_closed_intents_bruteforce(context)),
                    )

    def test_relational_attributes_have_edge_provenance(self) -> None:
        trajectory, _ = load_case("c5_composite")
        bundle = analyze_trajectory(trajectory)
        edge_ids = {edge.edge_id for edge in bundle.dag.edges}
        for round_record in bundle.relational_scaling["rounds"]:
            for provenance in round_record["provenance"]:
                self.assertIn(provenance["edge_id"], edge_ids)
                self.assertIn(
                    provenance["quantifier"],
                    {"exists_incoming", "exists_outgoing"},
                )

    def test_attribute_and_incoming_array_order_do_not_change_science(self) -> None:
        raw = load_raw("c5_composite")
        permuted = deepcopy(raw)
        for event in permuted["events"]:
            event["attributes"] = list(reversed(event["attributes"]))
            event["incoming_edges"] = list(reversed(event["incoming_edges"]))
        original = ReasoningTrajectory.from_dict(raw)
        reordered = ReasoningTrajectory.from_dict(permuted)
        self.assertEqual(original.canonical_sha256, reordered.canonical_sha256)
        self.assertEqual(
            analyze_trajectory(original).scientific_fingerprint,
            analyze_trajectory(reordered).scientific_fingerprint,
        )

    def test_trace_occurrences_preserve_temporal_order(self) -> None:
        trajectory, _ = load_case("c5_composite")
        position = {event.event_id: event.sequence_index for event in trajectory.events}
        bundle = analyze_trajectory(trajectory)
        for trace in bundle.traces:
            indexes = [position[event_id] for event_id in trace.event_ids]
            self.assertEqual(indexes, sorted(indexes))


class BaselineComparisonTests(unittest.TestCase):
    def test_flattening_destroys_non_linear_edge_identity(self) -> None:
        trajectory, _ = load_case("c5_composite")
        dag = build_reasoning_dag(trajectory)
        full = edge_identity_set(dag.edges)
        flattened = edge_identity_set(project_flattened_edges(dag))
        self.assertFalse(any(relation != "CONTINUE" for _, _, relation in flattened))
        self.assertTrue(any(relation == "REVISIT" for _, _, relation in full))
        self.assertTrue(any(relation == "MERGE" for _, _, relation in full))
        self.assertLess(len(full & flattened), len(full))

    def test_tree_projection_cannot_retain_multi_parent_merge(self) -> None:
        trajectory, expected = load_case("c5_composite")
        dag = build_reasoning_dag(trajectory)
        tree_edges = project_tree_edges(dag)
        target_id = next(iter(expected["merge_parents"]))
        incoming = [edge for edge in tree_edges if edge.target_event_id == target_id]
        self.assertEqual(len(incoming), 1)
        self.assertEqual(len(expected["merge_parents"][target_id]), 2)


class FailClosedTrajectoryTests(unittest.TestCase):
    def test_duplicate_event_id_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["event_id"] = raw["events"][0]["event_id"]
        assert_validation_code(self, raw, "EVENT_ID_DUPLICATE")

    def test_bool_sequence_index_is_not_an_integer(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["sequence_index"] = True
        assert_validation_code(self, raw, "TYPE_INTEGER_REQUIRED")

    def test_duplicate_sequence_index_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][2]["sequence_index"] = 1
        assert_validation_code(self, raw, "SEQUENCE_INDEX_INVALID")

    def test_missing_parent_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["incoming_edges"][0]["source_event_id"] = "absent"
        assert_validation_code(self, raw, "PARENT_EVENT_MISSING")

    def test_backward_edge_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["incoming_edges"][0]["source_event_id"] = "e2"
        assert_validation_code(self, raw, "NON_FORWARD_EDGE")

    def test_root_with_incoming_edge_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][0]["incoming_edges"] = [
            {"source_event_id": "e1", "relation": "CONTINUE", "evidence": "invalid"}
        ]
        assert_validation_code(self, raw, "ROOT_HAS_INCOMING_EDGE")

    def test_non_root_without_parent_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["incoming_edges"] = []
        assert_validation_code(self, raw, "NON_ROOT_WITHOUT_PARENT")

    def test_unknown_enum_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["event_kind"] = "WISHFUL_THINKING"
        assert_validation_code(self, raw, "ENUM_VALUE_INVALID")

    def test_unknown_edge_relation_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["incoming_edges"][0]["relation"] = "TELEPORT"
        assert_validation_code(self, raw, "ENUM_VALUE_INVALID")

    def test_unknown_status_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["status"] = "MAYBE_SOLVED"
        assert_validation_code(self, raw, "ENUM_VALUE_INVALID")

    def test_empty_canonical_state_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["canonical_math_state_id"] = ""
        assert_validation_code(self, raw, "TYPE_NONEMPTY_STRING_REQUIRED")

    def test_unknown_key_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["hidden_answer"] = "forbidden"
        assert_validation_code(self, raw, "OBJECT_KEY_UNKNOWN")

    def test_nonfinite_json_is_rejected(self) -> None:
        text = (FIXTURES / "c1_linear.trajectory.json").read_text()
        text = text.replace('"sequence_index": 1', '"sequence_index": NaN', 1)
        with self.assertRaises(TrajectoryValidationError) as caught:
            ReasoningTrajectory.from_json_text(text)
        self.assertEqual(caught.exception.code, "JSON_NONFINITE_NUMBER")

    def test_merge_with_only_one_semantic_parent_is_rejected(self) -> None:
        raw = load_raw("c1_linear")
        raw["events"][1]["incoming_edges"][0]["relation"] = "MERGE"
        trajectory = ReasoningTrajectory.from_dict(raw)
        with self.assertRaises(TrajectoryValidationError) as caught:
            analyze_trajectory(trajectory)
        self.assertEqual(caught.exception.code, "MERGE_PARENT_INSUFFICIENT")


class IsolationAndCliTests(unittest.TestCase):
    def test_protected_absorb_baseline_is_unchanged(self) -> None:
        baseline_bytes = PROTECTED_BASELINE.read_bytes()
        self.assertEqual(
            hashlib.sha256(baseline_bytes).hexdigest(),
            PROTECTED_BASELINE_SHA256,
        )
        entries = []
        for line in baseline_bytes.decode("utf-8").splitlines():
            digest, relative = line.split("  ", 1)
            entries.append((digest, relative))
        self.assertEqual(len(entries), 161)
        self.assertEqual(len({relative for _, relative in entries}), 161)
        repo_root = HERE.parents[2]
        for expected, relative in entries:
            path = repo_root / relative
            self.assertTrue(path.is_file(), relative)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected)

    def test_package_has_no_absorb_side_imports(self) -> None:
        forbidden = (
            "system.vein_analysis",
            "system.process_absorb",
            "system.schema",
        )
        for source in PACKAGE_ROOT.glob("*.py"):
            tree = ast.parse(source.read_text(), filename=str(source))
            imported: set[str] = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imported.update(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    imported.add(module)
                    imported.update(f"{module}.{alias.name}" for alias in node.names)
            for marker in forbidden:
                self.assertFalse(
                    any(name == marker or name.startswith(f"{marker}.") for name in imported),
                    f"{source} imports protected marker {marker}",
                )

    def test_public_import_has_no_db_model_or_solver_side_effect(self) -> None:
        module = importlib.import_module("system.solve_vein_analysis")
        self.assertEqual(module.__version__, "0.1.0")

    def test_runtime_assets_validate(self) -> None:
        report = validate_asset_manifest(default_assets_dir())
        self.assertEqual(report["verdict"], "PASS")
        self.assertEqual(report["live_execution"], "NOT_TESTED")
        self.assertEqual(report["asset_count"], 4)

    def test_asset_tampering_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "assets"
            shutil.copytree(default_assets_dir(), copied)
            target = copied / "AGENTS_event_extractor.md"
            target.write_text(target.read_text() + "\ntampered\n")
            with self.assertRaises(CliContractError):
                validate_asset_manifest(copied)

    def test_asset_leaf_symlink_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "assets"
            shutil.copytree(default_assets_dir(), copied)
            target = copied / "AGENTS_event_extractor.md"
            target.unlink()
            target.symlink_to(default_assets_dir() / "AGENTS_event_extractor.md")
            with self.assertRaises(CliContractError):
                validate_asset_manifest(copied)

    def test_cli_seals_complete_output_and_rejects_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "result"
            manifest = analyze_to_directory(
                FIXTURES / "c5_composite.trajectory.json",
                output,
                default_assets_dir(),
                relational_max_iterations=8,
                check_incremental_equivalence=True,
            )
            self.assertEqual(manifest["verdict"], "PASS")
            self.assertEqual(manifest["live_model_calls"], 0)
            self.assertEqual(manifest["database_connections"], 0)
            self.assertEqual(manifest["solver_launches"], 0)
            self.assertTrue(manifest["incremental_equivalence"])
            receipt = manifest["implementation_tree_receipt"]
            self.assertEqual(receipt, implementation_tree_receipt())
            aggregate_lines = []
            for entry in receipt["files"]:
                path = HERE.parents[2] / entry["path"]
                self.assertTrue(path.is_file())
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                self.assertEqual(actual, entry["sha256"])
                aggregate_lines.append(f"{actual}  {entry['path']}\n")
            self.assertEqual(
                hashlib.sha256("".join(aggregate_lines).encode()).hexdigest(),
                receipt["aggregate_sha256"],
            )
            expected_files = {
                "reasoning-dag.json",
                "state-context.json",
                "transition-context.json",
                "state-concepts.json",
                "transition-concepts.json",
                "relational-scaling.json",
                "traces.json",
                "audit-report.json",
                "incremental-replay.json",
                "output.md",
                "run-manifest.json",
            }
            self.assertEqual({path.name for path in output.iterdir()}, expected_files)
            with self.assertRaises(CliContractError):
                analyze_to_directory(
                    FIXTURES / "c5_composite.trajectory.json",
                    output,
                    default_assets_dir(),
                    relational_max_iterations=8,
                    check_incremental_equivalence=True,
                )


if __name__ == "__main__":
    unittest.main()
