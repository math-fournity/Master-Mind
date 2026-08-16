"""Regression tests for the zero-model solve-side Trace Auditor."""

from __future__ import annotations

from copy import deepcopy
import json
import subprocess
import sys
from pathlib import Path
import unittest

from system.solve_vein_analysis import state_normalized_dag as snd
from system.solve_vein_analysis import trace_auditor as ta


REPO_ROOT = Path(__file__).resolve().parents[3]


class SolveSideTraceAuditorTests(unittest.TestCase):
    def test_demo_complex_trace_audit_passes_required_families(self) -> None:
        receipt = ta.build_demo_complex_trace_audit()
        self.assertEqual(receipt["schema_version"], ta.TRACE_AUDIT_SCHEMA_VERSION)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertEqual(receipt["branch_point_count"], 1)
        self.assertEqual(receipt["revisit_event_count"], 1)
        self.assertEqual(receipt["explicit_merge_event_count"], 1)
        self.assertEqual(receipt["required_trace_family_verdict"]["status"], "PASS")
        self.assertIn("TRUE_MERGE", receipt["observed_trace_families"])
        self.assertTrue(all(value == 0 for value in receipt["side_effects"].values()))

    def test_missing_required_trace_family_is_scientific_fail_not_protocol_exception(self) -> None:
        receipt = ta.audit_reasoning_trace(
            dag=ta._demo_complex_dag(),
            required_trace_families=("CROSS_BRANCH_REUSE",),
        )
        self.assertEqual(receipt["overall_verdict"], "FAIL")
        self.assertEqual(receipt["required_trace_family_verdict"]["missing_trace_families"], ["CROSS_BRANCH_REUSE"])

    def test_unknown_required_trace_family_is_rejected(self) -> None:
        with self.assertRaises(ta.TraceAuditError) as caught:
            ta.audit_reasoning_trace(
                dag=ta._demo_complex_dag(),
                required_trace_families=("NOT_A_FAMILY",),
            )
        self.assertEqual(caught.exception.code, "REQUIRED_TRACE_FAMILY_UNKNOWN")

    def test_state_sidecar_matching_dag_hash_and_order_passes(self) -> None:
        dag = ta._demo_complex_dag()
        sidecar = {
            "schema_version": snd.STATE_NORMALIZED_DAG_SCHEMA_VERSION,
            "overall_verdict": "PASS",
            "dag_sha256": ta.sha256_json(dag),
            "annotated_occurrence_ids": ["a0", "e3"],
            "topological_annotation_order": ["a0", "e3"],
        }
        receipt = ta.audit_reasoning_trace(dag=dag, state_annotation_bundle=sidecar)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertEqual(receipt["state_sidecar_verdict"]["status"], "PASS")
        self.assertEqual(receipt["state_sidecar_verdict"]["annotated_occurrence_count"], 2)

    def test_state_sidecar_dag_hash_mismatch_is_rejected(self) -> None:
        dag = ta._demo_complex_dag()
        sidecar = {
            "schema_version": snd.STATE_NORMALIZED_DAG_SCHEMA_VERSION,
            "overall_verdict": "PASS",
            "dag_sha256": "0" * 64,
            "annotated_occurrence_ids": ["a0"],
            "topological_annotation_order": ["a0"],
        }
        with self.assertRaises(ta.TraceAuditError) as caught:
            ta.audit_reasoning_trace(dag=dag, state_annotation_bundle=sidecar)
        self.assertEqual(caught.exception.code, "STATE_SIDECAR_DAG_HASH_MISMATCH")

    def test_state_sidecar_order_mismatch_is_rejected(self) -> None:
        dag = ta._demo_complex_dag()
        sidecar = {
            "schema_version": snd.STATE_NORMALIZED_DAG_SCHEMA_VERSION,
            "overall_verdict": "PASS",
            "dag_sha256": ta.sha256_json(dag),
            "annotated_occurrence_ids": ["a0", "e3"],
            "topological_annotation_order": ["e3", "a0"],
        }
        with self.assertRaises(ta.TraceAuditError) as caught:
            ta.audit_reasoning_trace(dag=dag, state_annotation_bundle=sidecar)
        self.assertEqual(caught.exception.code, "STATE_SIDECAR_ORDER_MISMATCH")

    def test_unknown_edge_endpoint_is_rejected(self) -> None:
        dag = ta._demo_complex_dag()
        dag["edges"][0]["target_event_id"] = "missing"  # type: ignore[index]
        with self.assertRaises(ta.TraceAuditError) as caught:
            ta.audit_reasoning_trace(dag=dag)
        self.assertEqual(caught.exception.code, "DAG_EDGE_ENDPOINT_UNKNOWN")

    def test_duplicate_edge_id_is_rejected(self) -> None:
        dag = ta._demo_complex_dag()
        dag["edges"].append(deepcopy(dag["edges"][0]))  # type: ignore[index]
        with self.assertRaises(ta.TraceAuditError) as caught:
            ta.audit_reasoning_trace(dag=dag)
        self.assertEqual(caught.exception.code, "DAG_EDGE_ID_DUPLICATE")

    def test_cli_outputs_demo_complex_trace_audit_receipt(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/solve_vein_analysis/trace_auditor.py",
                "--demo-complex",
            ],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        receipt = json.loads(completed.stdout)
        self.assertEqual(receipt["overall_verdict"], "PASS")
        self.assertEqual(receipt["side_effects"]["model_calls"], 0)

    def test_trace_auditor_module_has_no_model_solver_database_network_or_subprocess_import(self) -> None:
        roots = ta.assert_no_forbidden_imports(Path(ta.__file__))
        self.assertNotIn("arango", roots)
        self.assertNotIn("socket", roots)
        self.assertNotIn("subprocess", roots)


if __name__ == "__main__":
    unittest.main()
