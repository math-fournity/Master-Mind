"""Offline orchestration tests for the sealed POC-VMS-41 runner.

The end-to-end test uses a local fake executable and temporary HOME/result
roots.  It exercises four one-shot attempts, hidden-gold grading after all
calls terminate, tool-event auditing, append-once sealing, and the deliberate
manual-audit ceiling without contacting Devin, a model, a database, Redis, or
the Target Solver.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest import mock

from system.solve_vein_analysis.event_extraction_qualification import (
    EventExtractionAcceptableSetPack,
)
from system.solve_vein_analysis.role_runtime import canonical_json_bytes, sha256_file
from system.tests.solve_vein_analysis.run_event_extractor_qualification import (
    CASE_DIRS,
    DEFAULT_FINAL_ROOT,
    EXPECTED_CASE_IDS,
    QualificationRunError,
    audit_tool_boundary,
    execute_qualification,
    render_task,
    test_source_tree_sha256 as source_tree_sha256,
    validate_freeze_manifest,
)
from system.tests.solve_vein_analysis.test_event_extraction_qualification import (
    ACCEPTABLE_SET_PATH,
    FIXTURE_ROOT,
    build_passing_candidate,
)
from system.tests.solve_vein_analysis.verify_event_extractor_qualification import (
    verify_live_bundle,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
PROTOCOL = (
    REPO_ROOT
    / "docs/history/sixth-generation/rnd"
    / "368-v0-2026-08-14-POC-VMS-41-Event-Extractor未见样本资格化协议.md"
)
ASSET_ROOT = REPO_ROOT / "system/assets/solve_vein_analysis/releases/0.4.0"
CATALOG_TEXT = "glm-5-2 GLM-5.2 High [200K context, Free]\n"
CLI_VERSION = "devin 3000.4.25 (fake)"


def _candidate_map() -> dict[str, object]:
    pack = EventExtractionAcceptableSetPack.from_json_text(
        ACCEPTABLE_SET_PATH.read_text()
    )
    result: dict[str, object] = {}
    for acceptable in pack.cases:
        raw = (
            FIXTURE_ROOT
            / CASE_DIRS[acceptable.case_id]
            / "raw_solver_trajectory.txt"
        ).read_bytes()
        result[acceptable.case_id] = build_passing_candidate(acceptable, raw)
    return result


def _write_fake_devin(path: Path) -> None:
    encoded_candidates = repr(json.dumps(_candidate_map(), ensure_ascii=True))
    path.write_text(
        f"""#!/usr/bin/env python3
import hashlib, json, pathlib, re, sys
args = sys.argv[1:]
if '--version' in args:
    print({CLI_VERSION!r})
    raise SystemExit(0)
if args[:2] == ['models', 'list']:
    print({CATALOG_TEXT.rstrip()!r})
    raise SystemExit(0)
candidates = json.loads({encoded_candidates})
cwd = pathlib.Path.cwd()
task = (cwd / 'TASK.md').read_text()
match = re.search(r"Case ID: `([^`]+)`", task)
if not match:
    raise SystemExit(4)
case_id = match.group(1)
output = cwd / 'reasoning-trajectory.json'
output.write_text(json.dumps(candidates[case_id], ensure_ascii=False, sort_keys=True))
digest = hashlib.sha256(output.read_bytes()).hexdigest()
done = cwd / 'DONE.md'
done.write_text('reasoning-trajectory.json SHA256=' + digest + '\\n')
export = pathlib.Path(args[args.index('--export') + 1])
tool_calls = []
for index, name in enumerate(('problem.md', 'raw_solver_trajectory.txt', 'reasoning-trajectory-v1.md')):
    tool_calls.append({{
        'tool_call_id': 'read-' + str(index),
        'function_name': 'read',
        'arguments': {{'file_path': str(cwd / name)}},
    }})
for index, name in enumerate(('reasoning-trajectory.json', 'DONE.md')):
    tool_calls.append({{
        'tool_call_id': 'write-' + str(index),
        'function_name': 'write',
        'arguments': {{'file_path': str(cwd / name), 'content': 'omitted-from-test-export'}},
    }})
export.write_text(json.dumps({{
    'schema_version': 'ATIF-v1.7',
    'session_id': 'fake-' + case_id,
    'agent': {{'model_name': 'GLM-5.2 High'}},
    'steps': [{{
        'step_id': 'assistant-1',
        'source': 'agent',
        'extra': {{'generation_model': 'glm-5-2'}},
        'tool_calls': tool_calls,
    }}],
}}))
print('fake event extraction complete')
"""
    )
    path.chmod(path.stat().st_mode | stat.S_IXUSR)


def _write_freeze(
    path: Path,
    *,
    fake_binary: Path,
    global_agents: Path,
) -> None:
    frozen_paths = (
        PROTOCOL,
        ACCEPTABLE_SET_PATH,
        ASSET_ROOT / "AGENTS_event_extractor.md",
        ASSET_ROOT / "TASK_event_extractor.template.md",
        ASSET_ROOT / "reasoning-trajectory-v1.md",
        REPO_ROOT / "system/solve_vein_analysis/event_extraction_qualification.py",
        REPO_ROOT
        / "system/tests/solve_vein_analysis/run_event_extractor_qualification.py",
    )
    baseline = (
        REPO_ROOT
        / "system/tests/solve_vein_analysis/protected_absorb_baseline.sha256"
    )
    python_binary = Path(os.path.realpath(os.sys.executable))
    pack = EventExtractionAcceptableSetPack.from_json_text(
        ACCEPTABLE_SET_PATH.read_text()
    )
    case_specs = []
    for acceptable in pack.cases:
        fixture_dir = FIXTURE_ROOT / CASE_DIRS[acceptable.case_id]
        source_receipt = fixture_dir / "source-receipt.json"
        case_specs.append(
            {
                "case_id": acceptable.case_id,
                "fixture_dir": CASE_DIRS[acceptable.case_id],
                "acceptable_set_id": acceptable.acceptable_set_id,
                "problem_path": (fixture_dir / "problem.md")
                .relative_to(REPO_ROOT)
                .as_posix(),
                "problem_sha256": sha256_file(fixture_dir / "problem.md"),
                "raw_path": (fixture_dir / "raw_solver_trajectory.txt")
                .relative_to(REPO_ROOT)
                .as_posix(),
                "raw_sha256": sha256_file(
                    fixture_dir / "raw_solver_trajectory.txt"
                ),
                "source_receipt_path": (
                    source_receipt.relative_to(REPO_ROOT).as_posix()
                    if source_receipt.is_file()
                    else None
                ),
                "source_receipt_sha256": (
                    sha256_file(source_receipt) if source_receipt.is_file() else None
                ),
            }
        )
    test_ids = [f"test-fixture-{index:03d}" for index in range(1, 101)]
    manifest = {
        "schema_version": "solve-vein/vms41-preexecution-freeze/v1",
        "poc_id": "POC-VMS-41",
        "run_id": "poc-vms-41-event-extractor-qualification-20260814",
        "protocol": {
            "path": PROTOCOL.relative_to(REPO_ROOT).as_posix(),
            "sha256": sha256_file(PROTOCOL),
        },
        "acceptable_set_pack": {
            "path": ACCEPTABLE_SET_PATH.relative_to(REPO_ROOT).as_posix(),
            "sha256": sha256_file(ACCEPTABLE_SET_PATH),
        },
        "frozen_files": [
            {
                "path": item.relative_to(REPO_ROOT).as_posix(),
                "sha256": sha256_file(item),
            }
            for item in frozen_paths
        ],
        "case_specs": case_specs,
        "runtime_profile": {
            "carrier": "devin_cli",
            "role": "REASONING_EVENT_EXTRACTOR",
            "model_uid": "glm-5-2",
            "normalized_effort": "high",
            "effort_encoding": "model_uid",
            "orchestration_mode": "fresh_single_agent_one_shot",
            "fresh_session": True,
            "resume_allowed": False,
            "sandbox_requested": False,
            "permission_mode": "dangerous",
            "asset_release_path": ASSET_ROOT.relative_to(REPO_ROOT).as_posix(),
            "resolved_binary_path": str(fake_binary.resolve(strict=True)),
            "resolved_binary_sha256": sha256_file(fake_binary.resolve(strict=True)),
            "cli_version": CLI_VERSION,
            "catalog_snapshot_sha256": hashlib.sha256(
                CATALOG_TEXT.encode()
            ).hexdigest(),
            "global_agents_path": "~/.config/devin/AGENTS.md",
            "global_agents_sha256": sha256_file(global_agents),
            "global_agents_size_bytes": global_agents.stat().st_size,
        },
        "resource_contract": {
            "case_attempts": 1,
            "concurrency": 1,
            "infrastructure_retries": 0,
            "scientific_retries": 0,
            "timeout_seconds_per_case": 900,
        },
        "attempt_ids": {
            case_id: f"poc-vms-41-{case_id.lower()}-a1"
            for case_id in EXPECTED_CASE_IDS
        },
        "output_root": str(DEFAULT_FINAL_ROOT),
        "test_gate": {
            "runner": "python_unittest_in_process",
            "python_executable": str(python_binary),
            "python_executable_sha256": sha256_file(python_binary),
            "python_version": os.sys.version,
            "test_ids": test_ids,
            "tests_run": len(test_ids),
            "failures": 0,
            "errors": 0,
            "skipped": 0,
            "successful": True,
            "test_source_tree_sha256": source_tree_sha256(),
            "protected_absorb_baseline_path": baseline.relative_to(
                REPO_ROOT
            ).as_posix(),
            "protected_absorb_baseline_sha256": sha256_file(baseline),
            "protected_absorb_file_count": len(baseline.read_text().splitlines()),
            "verdict": "PASS",
        },
        "side_effect_authorization": {
            "devin_role_attempts_authorized": 4,
            "database_connections": 0,
            "network_calls_by_candidate": 0,
            "redis_connections": 0,
            "solver_calls": 0,
            "subagent_calls": 0,
        },
    }
    path.write_bytes(canonical_json_bytes(manifest))


class RunnerContractTests(unittest.TestCase):
    def test_task_renderer_requires_exact_placeholder_set(self) -> None:
        with self.assertRaisesRegex(QualificationRunError, "placeholders mismatch"):
            render_task("{{A}} {{EXTRA}}", {"A": "one"})

    def test_tool_audit_marks_zero_events_unobservable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            bundle = root / "attempt"
            bundle.mkdir()
            export = bundle / "devin-export.json"
            export.write_text(json.dumps({"steps": []}))
            report = audit_tool_boundary(export, bundle, "attempt-1")
            self.assertEqual(report["verdict"], "UNOBSERVABLE")

    def test_tool_audit_rejects_external_absolute_read(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            bundle = root / "attempt"
            bundle.mkdir()
            export = bundle / "devin-export.json"
            export.write_text(
                json.dumps(
                    {
                        "steps": [
                            {
                                "tool_calls": [
                                    {
                                        "function_name": "read",
                                        "arguments": {"file_path": "/etc/passwd"},
                                    }
                                ]
                            }
                        ]
                    }
                )
            )
            report = audit_tool_boundary(export, bundle, "attempt-1")
            self.assertEqual(report["verdict"], "FAIL")
            self.assertTrue(report["errors"])

    def test_four_case_fake_runtime_seals_pending_manual_audit(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake = root / "devin"
            _write_fake_devin(fake)
            home = root / "home"
            global_agents = home / ".config/devin/AGENTS.md"
            global_agents.parent.mkdir(parents=True)
            global_agents.write_text("# frozen test-only global control surface\n")
            freeze = root / "freeze.json"
            _write_freeze(
                freeze, fake_binary=fake, global_agents=global_agents
            )
            with mock.patch.dict(os.environ, {"HOME": str(home)}, clear=False):
                validate_freeze_manifest(freeze)
            final_root = root / "final"
            partial_root = root / ".final.partial"
            with mock.patch.dict(os.environ, {"HOME": str(home)}, clear=False):
                sealed = execute_qualification(
                    freeze,
                    final_root=final_root,
                    partial_root=partial_root,
                    explicit_binary=fake,
                    enforce_production_site=False,
                )
            self.assertEqual(sealed, final_root)
            self.assertFalse(partial_root.exists())
            aggregate = json.loads((final_root / "live-aggregate.json").read_text())
            self.assertEqual(aggregate["terminal_case_ids"], list(EXPECTED_CASE_IDS))
            self.assertEqual(
                aggregate["overall_status"], "PENDING_MANUAL_AUDIT", aggregate
            )
            self.assertEqual(
                aggregate["component_qualification"], "NOT_YET_DECIDABLE"
            )
            self.assertTrue((final_root / "COMMITTED").is_file())
            with mock.patch.dict(os.environ, {"HOME": str(home)}, clear=False):
                verification = verify_live_bundle(final_root, freeze)
            self.assertEqual(
                verification["artifact_integrity"], "PASS", verification
            )
            self.assertEqual(
                verification["live_attempt_status"], "PENDING_MANUAL_AUDIT"
            )
            self.assertEqual(
                verification["component_qualification"], "NOT_YET_DECIDABLE"
            )
            attempts = list((final_root / "attempts").iterdir())
            self.assertEqual(len(attempts), 4)
            for attempt in attempts:
                receipt = json.loads(
                    (attempt / "invocation-receipt.json").read_text()
                )
                self.assertEqual(receipt["model_observability_verdict"], "MATCH")
                self.assertEqual(
                    receipt["global_control_surface"]["sha256"],
                    sha256_file(global_agents),
                )
            with self.assertRaisesRegex(QualificationRunError, "already exists"):
                with mock.patch.dict(os.environ, {"HOME": str(home)}, clear=False):
                    execute_qualification(
                        freeze,
                        final_root=final_root,
                        partial_root=partial_root,
                        explicit_binary=fake,
                        enforce_production_site=False,
                    )

    def test_verifier_rejects_post_seal_candidate_tamper(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake = root / "devin"
            _write_fake_devin(fake)
            home = root / "home"
            global_agents = home / ".config/devin/AGENTS.md"
            global_agents.parent.mkdir(parents=True)
            global_agents.write_text("# frozen test-only global control surface\n")
            freeze = root / "freeze.json"
            _write_freeze(freeze, fake_binary=fake, global_agents=global_agents)
            final_root = root / "final"
            with mock.patch.dict(os.environ, {"HOME": str(home)}, clear=False):
                execute_qualification(
                    freeze,
                    final_root=final_root,
                    partial_root=root / ".final.partial",
                    explicit_binary=fake,
                    enforce_production_site=False,
                )
            attempt_id = json.loads(freeze.read_text())["attempt_ids"][
                EXPECTED_CASE_IDS[0]
            ]
            candidate = final_root / "attempts" / attempt_id / "reasoning-trajectory.json"
            candidate.write_bytes(candidate.read_bytes() + b" ")
            with mock.patch.dict(os.environ, {"HOME": str(home)}, clear=False):
                verification = verify_live_bundle(final_root, freeze)
            self.assertEqual(verification["artifact_integrity"], "FAIL")
            self.assertTrue(verification["errors"])


if __name__ == "__main__":
    unittest.main()
