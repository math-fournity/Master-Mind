"""Offline contract tests for POC-VMS-32 and its one-shot role runner."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.models import ReasoningTrajectory
from system.solve_vein_analysis.pipeline import analyze_trajectory
from system.solve_vein_analysis.role_runtime import (
    DEVIN_MODEL_UID,
    DevinRoleSpec,
    RoleInput,
    RoleRuntimeError,
    dedicated_devin_config,
    inspect_export,
    run_devin_role,
)
from system.tests.solve_vein_analysis.run_live_poc import (
    FIXTURES,
    _load_preexecution_freeze_manifest,
    evaluate_auditor,
    evaluate_extractor,
    evaluate_normalizer,
)


def _write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def _passing_receipt() -> dict[str, object]:
    return {
        "exit_code": 0,
        "timed_out": False,
        "retry_count": 0,
        "model_observability_verdict": "MATCH",
        "export_sha256": "1" * 64,
        "export_observation": {"json_valid": True},
        "output_sha256": "2" * 64,
        "done_marker_sha256": "3" * 64,
        "done_marker_content_valid": True,
        "sandbox_requested": True,
        "sanitized_argv": ["devin", "--sandbox", "-p"],
    }


class FrozenLiveFixtureTests(unittest.TestCase):
    def test_preexecution_freeze_manifest_is_bound_to_poc_and_file_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "freeze.json"
            relative = "system/tests/solve_vein_analysis/live_fixtures/poc_vms_32/problem.md"
            _write_json(
                path,
                {
                    "schema_version": "solve-vein/preexecution-freeze-manifest/v1",
                    "poc_id": "POC-TEST",
                    "frozen_files": [
                        {
                            "path": relative,
                            "sha256": hashlib.sha256(
                                (REPO_ROOT / relative).read_bytes()
                            ).hexdigest(),
                        }
                    ],
                },
            )
            value = _load_preexecution_freeze_manifest(path, "POC-TEST")
            self.assertEqual(value["poc_id"], "POC-TEST")
            with self.assertRaisesRegex(RuntimeError, "POC mismatch"):
                _load_preexecution_freeze_manifest(path, "POC-OTHER")

    def test_gold_trajectory_is_strict_and_every_span_hashes_raw_bytes(self) -> None:
        raw = (FIXTURES / "raw_solver_trajectory.txt").read_bytes()
        trajectory = ReasoningTrajectory.from_json_text(
            (FIXTURES / "gold.reasoning-trajectory.json").read_text()
        )
        self.assertEqual(len(trajectory.events), 10)
        self.assertEqual(
            trajectory.source.source_artifact_sha256,
            hashlib.sha256(raw).hexdigest(),
        )
        for event in trajectory.events:
            span = event.source_span
            self.assertEqual(
                span.sha256,
                hashlib.sha256(raw[span.start : span.end]).hexdigest(),
            )

    def test_normalizer_input_has_exactly_three_preregistered_semantic_errors(self) -> None:
        candidate = ReasoningTrajectory.from_json_text(
            (FIXTURES / "normalizer-input.reasoning-trajectory.json").read_text()
        )
        gold = ReasoningTrajectory.from_json_text(
            (FIXTURES / "gold.reasoning-trajectory.json").read_text()
        )
        candidate_by_id = {event.event_id: event for event in candidate.events}
        gold_by_id = {event.event_id: event for event in gold.events}
        differences: list[str] = []
        for event_id in candidate_by_id:
            left = candidate_by_id[event_id]
            right = gold_by_id[event_id]
            if left.status != right.status:
                differences.append(f"{event_id}.status")
            if left.canonical_math_state_id != right.canonical_math_state_id:
                differences.append(f"{event_id}.canonical_math_state_id")
            left_rel = {
                (edge.source_event_id, edge.relation.value) for edge in left.incoming_edges
            }
            right_rel = {
                (edge.source_event_id, edge.relation.value) for edge in right.incoming_edges
            }
            if left_rel != right_rel:
                differences.append(f"{event_id}.incoming_relations")
        self.assertEqual(
            differences,
            ["e2.status", "e3.canonical_math_state_id", "e7.incoming_relations"],
        )

    def test_auditor_mixed_set_contains_one_real_revisit_and_one_fake_merge(self) -> None:
        trajectory = ReasoningTrajectory.from_json_text(
            (FIXTURES / "gold.reasoning-trajectory.json").read_text()
        )
        dag = analyze_trajectory(trajectory).dag
        edge_by_id = {edge.edge_id: edge for edge in dag.edges}
        candidates = json.loads(
            (FIXTURES / "auditor-candidate-traces.json").read_text()
        )["traces"]
        valid, invalid = candidates
        self.assertEqual(valid["family"], "REVISIT_WITH_NEW_INFORMATION")
        self.assertEqual(edge_by_id[valid["edge_ids"][0]].relation.value, "REVISIT")
        self.assertEqual(invalid["family"], "TRUE_MERGE")
        self.assertEqual(len(invalid["edge_ids"]), 1)
        self.assertNotEqual(edge_by_id[invalid["edge_ids"][0]].relation.value, "MERGE")


class RoleRuntimeTests(unittest.TestCase):
    def test_atif_v17_export_counts_steps_and_tool_calls_once(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            export = Path(temp) / "devin-export.json"
            _write_json(
                export,
                {
                    "schema_version": "ATIF-v1.7",
                    "session_id": "atif-session",
                    "agent": {"model_name": "GLM-5.2 High"},
                    "steps": [
                        {
                            "step_id": "s0",
                            "source": "user",
                            "message": "task",
                        },
                        {
                            "step_id": "s1",
                            "source": "agent",
                            "model_name": "GLM-5.2 High",
                            "extra": {"generation_model": "glm-5-2"},
                            "tool_calls": [
                                {
                                    "tool_call_id": "call-1",
                                    "function_name": "read",
                                    "arguments": {"file_path": "input.txt"},
                                },
                                {
                                    "tool_call_id": "call-2",
                                    "function_name": "write",
                                    "arguments": {"file_path": "output.json"},
                                },
                            ],
                        },
                    ],
                },
            )
            observation = inspect_export(export)
            self.assertTrue(observation["json_valid"])
            self.assertEqual(observation["step_count"], 2)
            self.assertEqual(observation["tool_event_count"], 2)
            self.assertEqual(
                observation["observed_generation_model_uids"], ["glm-5-2"]
            )
            self.assertEqual(
                observation["observed_agent_model_names"], ["GLM-5.2 High"]
            )
            self.assertEqual(observation["session_ids"], ["atif-session"])

    def test_dedicated_config_is_secret_free_and_disables_subagents(self) -> None:
        config = dedicated_devin_config()
        self.assertFalse(config["subagents_enabled"])
        self.assertEqual(config["agent"]["model"], DEVIN_MODEL_UID)
        self.assertNotIn("org_id", json.dumps(config))
        self.assertTrue(config["permissions"]["deny"])
        self.assertNotIn(
            "Read(/Volumes/**)", config["permissions"]["deny"]
        )
        self.assertFalse(
            any(rule.startswith("Read(") for rule in config["permissions"]["deny"])
        )
        self.assertIn("Read(**)", config["permissions"]["allow"])
        self.assertIn("Write(**)", config["permissions"]["allow"])

    def test_sandbox_environment_uses_cli_boolean_spelling(self) -> None:
        from system.solve_vein_analysis.role_runtime import _minimal_environment

        self.assertEqual(_minimal_environment()["DEVIN_SANDBOX"], "true")
        self.assertEqual(_minimal_environment(False)["DEVIN_SANDBOX"], "false")
        self.assertEqual(_minimal_environment()["DEVIN_PERMISSION_MODE"], "dangerous")

    def test_gold_named_input_is_rejected_before_any_process(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            asset = root / "asset.md"
            asset.write_text("role")
            source = root / "source"
            source.write_text("input")
            spec = DevinRoleSpec(
                attempt_id="a1",
                role="test",
                role_asset_path=asset,
                task_text="test",
                inputs=(RoleInput(source, "gold.json"),),
                expected_output_name="result.json",
                output_bundle=root / "bundle",
            )
            with self.assertRaisesRegex(RoleRuntimeError, "ROLE_INPUT_NAME_FORBIDDEN"):
                run_devin_role(spec, explicit_binary=Path("/bin/false"))

    def test_fake_devin_one_shot_seals_receipt_and_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake = root / "devin"
            fake.write_text(
                """#!/usr/bin/env python3
import hashlib, json, pathlib, sys
args=sys.argv[1:]
if '--version' in args:
    print('devin 3000.4.25 (fake)')
    raise SystemExit(0)
if args[:2] == ['models','list']:
    print('glm-5-2 GLM-5.2 High [200K context, Free]')
    raise SystemExit(0)
export=pathlib.Path(args[args.index('--export')+1])
export.write_text(json.dumps({'session_id':'fake-s1','steps':[{'step_type':'assistant','extra':{'generation_model':'glm-5-2'}}]}))
pathlib.Path('result.json').write_text('{}')
digest=hashlib.sha256(pathlib.Path('result.json').read_bytes()).hexdigest()
pathlib.Path('DONE.md').write_text('result.json SHA256=' + digest)
print('fake complete')
"""
            )
            fake.chmod(fake.stat().st_mode | stat.S_IXUSR)
            asset = root / "asset.md"
            asset.write_text("role")
            source = root / "source.txt"
            source.write_text("input")
            bundle = root / "bundle"
            spec = DevinRoleSpec(
                attempt_id="a1",
                role="test",
                role_asset_path=asset,
                task_text="test",
                inputs=(RoleInput(source, "source.txt"),),
                expected_output_name="result.json",
                output_bundle=bundle,
            )
            receipt = run_devin_role(spec, explicit_binary=fake)
            self.assertEqual(receipt["retry_count"], 0)
            self.assertEqual(receipt["model_observability_verdict"], "MATCH")
            self.assertEqual(receipt["permission_mode"], "dangerous")
            self.assertTrue(receipt["sandbox_requested"])
            self.assertTrue((bundle / "invocation-receipt.json").is_file())
            self.assertTrue((bundle / "launch-receipt.json").is_file())
            events = [
                json.loads(line)
                for line in (bundle / "attempt-events.jsonl").read_text().splitlines()
            ]
            self.assertEqual(
                [event["event"] for event in events],
                ["PREPARED", "LOCAL_PROCESS_STARTED", "LOCAL_PROCESS_EXITED"],
            )
            self.assertEqual(receipt["request_accepted_observability"], "OBSERVED_POSTHOC")
            self.assertEqual(receipt["generation_started_observability"], "OBSERVED_POSTHOC")
            self.assertNotIn("--resume", receipt["sanitized_argv"])
            self.assertNotIn("--continue", receipt["sanitized_argv"])
            with self.assertRaisesRegex(RoleRuntimeError, "ROLE_OUTPUT_EXISTS"):
                run_devin_role(spec, explicit_binary=fake)

    def test_no_sandbox_profile_is_exactly_reflected_in_argv_env_and_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake = root / "devin"
            fake.write_text(
                """#!/usr/bin/env python3
import hashlib, json, os, pathlib, sys
args=sys.argv[1:]
if '--version' in args:
    print('devin 3000.4.25 (fake)')
    raise SystemExit(0)
if args[:2] == ['models','list']:
    print('glm-5-2 GLM-5.2 High [200K context, Free]')
    raise SystemExit(0)
assert '--sandbox' not in args
assert os.environ['DEVIN_SANDBOX'] == 'false'
export=pathlib.Path(args[args.index('--export')+1])
export.write_text(json.dumps({'session_id':'fake-s2','steps':[{'step_type':'assistant','extra':{'generation_model':'glm-5-2'}}]}))
pathlib.Path('result.json').write_text('{}')
digest=hashlib.sha256(pathlib.Path('result.json').read_bytes()).hexdigest()
pathlib.Path('DONE.md').write_text('result.json SHA256=' + digest)
"""
            )
            fake.chmod(fake.stat().st_mode | stat.S_IXUSR)
            asset = root / "asset.md"
            asset.write_text("role")
            source = root / "source.txt"
            source.write_text("input")
            spec = DevinRoleSpec(
                attempt_id="a2",
                role="test",
                role_asset_path=asset,
                task_text="test",
                inputs=(RoleInput(source, "source.txt"),),
                expected_output_name="result.json",
                output_bundle=root / "bundle",
                sandbox_requested=False,
            )
            receipt = run_devin_role(spec, explicit_binary=fake)
            self.assertFalse(receipt["sandbox_requested"])
            self.assertNotIn("--sandbox", receipt["sanitized_argv"])
            self.assertEqual(receipt["permission_mode"], "dangerous")
            self.assertNotIn("--resume", receipt["sanitized_argv"])
            self.assertNotIn("--continue", receipt["sanitized_argv"])

    def test_process_start_failure_persists_quarantine_and_blocks_relaunch(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            asset = root / "asset.md"
            asset.write_text("role")
            source = root / "source.txt"
            source.write_text("input")
            bundle = root / "bundle"
            spec = DevinRoleSpec(
                attempt_id="a3",
                role="test",
                role_asset_path=asset,
                task_text="test",
                inputs=(RoleInput(source, "source.txt"),),
                expected_output_name="result.json",
                output_bundle=bundle,
            )
            preflight = [
                subprocess.CompletedProcess(["devin", "--version"], 0, "devin fake", ""),
                subprocess.CompletedProcess(
                    ["devin", "models", "list"],
                    0,
                    "glm-5-2 GLM-5.2 High [200K context, Free]",
                    "",
                ),
            ]
            with mock.patch(
                "system.solve_vein_analysis.role_runtime._run_preflight_command",
                side_effect=preflight,
            ), mock.patch(
                "system.solve_vein_analysis.role_runtime.subprocess.Popen",
                side_effect=OSError("synthetic start failure"),
            ):
                with self.assertRaisesRegex(
                    RoleRuntimeError, "DEVIN_PROCESS_START_FAILED"
                ):
                    run_devin_role(spec, explicit_binary=Path(sys.executable))
            partial = root / ".bundle.partial-a3"
            self.assertTrue((partial / "launch-receipt.json").is_file())
            self.assertTrue((partial / "quarantine-receipt.json").is_file())
            events = [
                json.loads(line)
                for line in (partial / "attempt-events.jsonl").read_text().splitlines()
            ]
            self.assertEqual(
                [event["event"] for event in events],
                ["PREPARED", "LOCAL_PROCESS_START_FAILED"],
            )
            with self.assertRaisesRegex(
                RoleRuntimeError, "ROLE_RECONCILIATION_REQUIRED"
            ):
                run_devin_role(spec, explicit_binary=Path("/bin/false"))


class EvaluatorGoldenTests(unittest.TestCase):
    def _bundle(self, root: Path, output_name: str, output: object) -> Path:
        bundle = root / output_name.replace(".json", "")
        bundle.mkdir()
        _write_json(bundle / "invocation-receipt.json", _passing_receipt())
        _write_json(bundle / output_name, output)
        return bundle

    def test_extractor_evaluator_passes_frozen_gold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            gold = json.loads(
                (FIXTURES / "gold.reasoning-trajectory.json").read_text()
            )
            bundle = self._bundle(Path(temp), "reasoning-trajectory.json", gold)
            result = evaluate_extractor(bundle)
            self.assertEqual(result["component_verdict"], "PASS")

    def test_normalizer_evaluator_passes_exact_correction(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            gold = json.loads(
                (FIXTURES / "gold.reasoning-trajectory.json").read_text()
            )
            bundle = self._bundle(
                Path(temp), "normalized-reasoning-trajectory.json", gold
            )
            result = evaluate_normalizer(bundle)
            self.assertEqual(result["component_verdict"], "PASS")

    def test_auditor_evaluator_requires_rejection_of_fake_merge(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = {
                "schema_version": "solve-vein/trace-audit/v1",
                "artifact_hashes": {},
                "trace_verdicts": [
                    {
                        "trace_id": "candidate-valid-revisit",
                        "verdict": "PASS",
                        "reasons": ["same canonical state and revisit edge"],
                        "evidence_refs": ["e0", "e3", "edge_f75db69bda8f4387"],
                    },
                    {
                        "trace_id": "candidate-invalid-single-parent-merge",
                        "verdict": "FAIL",
                        "reasons": ["only one non-MERGE edge"],
                        "evidence_refs": ["edge_30e90287411de9e1"],
                    },
                ],
                "protocol_violations": [],
                "overall_verdict": "FAIL",
            }
            bundle = self._bundle(Path(temp), "trace-audit.json", output)
            result = evaluate_auditor(bundle)
            self.assertEqual(result["component_verdict"], "PASS")

    def test_auditor_evaluator_rejects_false_positive_merge(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = {
                "schema_version": "solve-vein/trace-audit/v1",
                "artifact_hashes": {},
                "trace_verdicts": [
                    {
                        "trace_id": "candidate-valid-revisit",
                        "verdict": "PASS",
                        "reasons": [],
                        "evidence_refs": [],
                    },
                    {
                        "trace_id": "candidate-invalid-single-parent-merge",
                        "verdict": "PASS",
                        "reasons": [],
                        "evidence_refs": [],
                    },
                ],
                "protocol_violations": [],
                "overall_verdict": "PASS",
            }
            bundle = self._bundle(Path(temp), "trace-audit.json", output)
            result = evaluate_auditor(bundle)
            self.assertEqual(result["component_verdict"], "FAIL")


if __name__ == "__main__":
    unittest.main()
