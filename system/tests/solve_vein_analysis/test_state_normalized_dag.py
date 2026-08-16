"""Regression tests for VMS-42 state-normalized DAG annotation sidecars."""

from __future__ import annotations

from copy import deepcopy
import json
import subprocess
import sys
from pathlib import Path
import unittest

from system.solve_vein_analysis import state_normalization as sn
from system.solve_vein_analysis import state_normalized_dag as snd


REPO_ROOT = Path(__file__).resolve().parents[3]


def _unseen_source() -> dict[str, object]:
    return json.loads(snd.UNSEEN_FIXTURE.read_text())


def _candidate_bundle(case_index: int, candidate_index: int) -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    source = _unseen_source()
    case = source["cases"][case_index]  # type: ignore[index]
    candidate = case["candidates"][candidate_index]["input"]  # type: ignore[index]
    normalized = sn.normalize_state_claims(
        candidate,
        case["dictionary"],  # type: ignore[index]
        legacy_projection_axes=sn.StateNormalizationAcceptableSet.from_dict(
            case["acceptable_set"]  # type: ignore[index]
        ).legacy_projection_axes,
    ).to_dict()
    evaluation = sn.evaluate_state_normalization_value(
        candidate,
        case["dictionary"],  # type: ignore[arg-type,index]
        case["acceptable_set"],  # type: ignore[arg-type,index]
    )
    dag = snd._demo_dag_for_occurrences(candidate["occurrence_ids"])  # type: ignore[index]
    return dag, normalized, evaluation


class VMS42StateNormalizedDagTests(unittest.TestCase):
    def test_demo_unseen_annotation_passes_in_topological_order(self) -> None:
        receipt = snd.build_demo_unseen_annotation_bundle()
        self.assertEqual(receipt["schema_version"], snd.STATE_NORMALIZED_DAG_SCHEMA_VERSION)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertEqual(receipt["annotation_count"], 3)
        self.assertEqual(receipt["topological_annotation_order"], ["s0", "s1", "s2"])
        self.assertEqual(receipt["annotated_occurrence_ids"], ["s0", "s1", "s2"])
        self.assertTrue(all(value == 0 for value in receipt["side_effects"].values()))

    def test_annotation_sidecar_does_not_mutate_reasoning_dag(self) -> None:
        dag, normalized, evaluation = _candidate_bundle(0, 0)
        before = snd.sha256_json(dag)
        receipt = snd.annotate_dag_with_normalized_state(
            dag=dag,
            normalized_bundle=normalized,
            evaluation=evaluation,
        )
        self.assertEqual(snd.sha256_json(dag), before)
        self.assertEqual(receipt["dag_sha256"], before)

    def test_normalized_occurrence_missing_from_dag_is_rejected(self) -> None:
        dag, normalized, evaluation = _candidate_bundle(0, 0)
        dag["nodes"] = dag["nodes"][:-1]  # type: ignore[index]
        dag["topological_order"] = dag["topological_order"][:-1]  # type: ignore[index]
        with self.assertRaises(snd.StateNormalizedDagError) as caught:
            snd.annotate_dag_with_normalized_state(
                dag=dag,
                normalized_bundle=normalized,
                evaluation=evaluation,
            )
        self.assertEqual(caught.exception.code, "NORMALIZED_OCCURRENCE_NOT_IN_DAG")

    def test_non_pass_state_normalization_evaluation_is_rejected(self) -> None:
        dag, normalized, evaluation = _candidate_bundle(0, 1)
        self.assertEqual(evaluation["overall_verdict"], "FAIL")
        with self.assertRaises(snd.StateNormalizedDagError) as caught:
            snd.annotate_dag_with_normalized_state(
                dag=dag,
                normalized_bundle=normalized,
                evaluation=evaluation,
            )
        self.assertEqual(caught.exception.code, "EVALUATION_NOT_PASS")

    def test_normalized_bundle_tampering_is_rejected_by_hash(self) -> None:
        dag, normalized, evaluation = _candidate_bundle(0, 0)
        tampered = deepcopy(normalized)
        tampered["state_bindings"][0]["value_id"] = "tampered-value"  # type: ignore[index]
        with self.assertRaises(snd.StateNormalizedDagError) as caught:
            snd.annotate_dag_with_normalized_state(
                dag=dag,
                normalized_bundle=tampered,
                evaluation=evaluation,
            )
        self.assertEqual(caught.exception.code, "NORMALIZED_BUNDLE_HASH_MISMATCH")

    def test_duplicate_axis_binding_is_rejected_after_hash_bound_evaluation(self) -> None:
        dag, normalized, evaluation = _candidate_bundle(0, 0)
        duplicated = deepcopy(normalized)
        duplicated["state_bindings"].append(deepcopy(duplicated["state_bindings"][0]))  # type: ignore[index]
        eval_for_duplicated = deepcopy(evaluation)
        eval_for_duplicated["canonical_input_hashes"]["normalized_bundle_sha256"] = snd.sha256_json(duplicated)  # type: ignore[index]
        with self.assertRaises(snd.StateNormalizedDagError) as caught:
            snd.annotate_dag_with_normalized_state(
                dag=dag,
                normalized_bundle=duplicated,
                evaluation=eval_for_duplicated,
            )
        self.assertEqual(caught.exception.code, "STATE_BINDING_DUPLICATE")

    def test_cli_outputs_demo_unseen_pass_receipt(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/solve_vein_analysis/state_normalized_dag.py",
                "--demo-unseen",
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        receipt = json.loads(completed.stdout)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertEqual(receipt["side_effects"]["model_calls"], 0)

    def test_state_normalized_dag_module_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        roots = snd.assert_no_forbidden_imports(Path(snd.__file__))
        self.assertNotIn("arango", roots)
        self.assertNotIn("socket", roots)
        self.assertNotIn("subprocess", roots)


if __name__ == "__main__":
    unittest.main()
