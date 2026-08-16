from __future__ import annotations

import json
from pathlib import Path
import stat
import tempfile
import time
import unittest

from system.solve_vein_analysis.agents_limit import (
    AgentsLimitError,
    CELL_SIZES,
    fixture_manifest,
    generate_agents_fixture,
    grade_agents_visibility,
    parse_sentinels,
    sentinel_offsets,
)
from system.solve_vein_analysis.role_runtime import RoleRuntimeError
from system.solve_vein_analysis.tmux_runtime import (
    send_tmux_debug_keys,
    snapshot_tmux_debug_role,
    start_tmux_debug_role,
)
from system.tests.solve_vein_analysis.run_agents_limit_poc import (
    build_spec,
    expected_attempt_id,
    finalize_agents_limit_attempt,
    task_text,
    validate_attempt_id,
)


class AgentsFixtureTests(unittest.TestCase):
    def test_every_cell_has_exact_deterministic_ascii_size(self) -> None:
        for cell_id, size in CELL_SIZES.items():
            first = generate_agents_fixture(cell_id)
            second = generate_agents_fixture(cell_id)
            self.assertEqual(first, second)
            self.assertEqual(len(first), size)
            self.assertTrue(first.isascii())
            self.assertEqual(len(parse_sentinels(first)), len(sentinel_offsets(size)))

    def test_boundary_cells_place_sentinels_around_16_kib(self) -> None:
        rows = parse_sentinels(generate_agents_fixture("A32"))
        offsets = {row["offset"] for row in rows}
        self.assertIn(15_872, offsets)
        self.assertIn(16_896, offsets)

    def test_manifest_binds_all_cells_and_sentinels(self) -> None:
        manifest = fixture_manifest()
        self.assertEqual(manifest["poc_id"], "POC-VMS-39")
        self.assertEqual([row["cell_id"] for row in manifest["cells"]], list(CELL_SIZES))
        self.assertTrue(all(len(row["sha256"]) == 64 for row in manifest["cells"]))


class AgentsVisibilityGraderTests(unittest.TestCase):
    def _paths(self, root: Path, cell_id: str = "A16") -> tuple[Path, Path, Path]:
        agents = root / "AGENTS.md"
        export = root / "devin-export.json"
        output = root / "agents-visibility-report.json"
        agents.write_bytes(generate_agents_fixture(cell_id))
        return agents, export, output

    @staticmethod
    def _export(messages: list[str]) -> dict[str, object]:
        return {
            "schema_version": "ATIF-v1.7",
            "session_id": "synthetic-session",
            "agent": {"name": "synthetic", "model_name": "GLM-5.2"},
            "steps": [
                {
                    "step_id": f"step-{index}",
                    "source": "system",
                    "message": message,
                    "extra": {},
                    "timestamp": "2026-08-14T00:00:00Z",
                }
                for index, message in enumerate(messages)
            ],
            "final_metrics": {},
        }

    def test_full_exact_system_message_is_primary_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            agents, export, output = self._paths(root)
            payload = agents.read_text()
            export.write_text(json.dumps(self._export(["prefix\n" + payload + "suffix"])))
            expected = [
                {"name": row["name"], "value": row["value"]}
                for row in parse_sentinels(agents.read_bytes())
            ]
            output.write_text(json.dumps({"sentinels": expected}))
            report = grade_agents_visibility(agents, export, output)
            self.assertEqual(report["primary_status"], "FULL_EXACT_SINGLE_MESSAGE")
            self.assertEqual(report["longest_exact_prefix_bytes"], CELL_SIZES["A16"])
            self.assertEqual(report["model_report"]["recall"], 1.0)

    def test_prefix_truncation_reports_exact_byte_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            agents, export, _ = self._paths(root, "A32")
            payload = agents.read_text()
            export.write_text(json.dumps(self._export([payload[:16_384]])))
            report = grade_agents_visibility(agents, export)
            self.assertEqual(report["primary_status"], "PREFIX_TRUNCATED_AT_16384")
            self.assertEqual(report["longest_exact_prefix_bytes"], 16_384)

    def test_partial_sentinel_without_prefix_is_not_full(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            agents, export, _ = self._paths(root, "A32")
            row = parse_sentinels(agents.read_bytes())[-1]
            export.write_text(json.dumps(self._export([f"{row['name']}={row['value']}"])))
            report = grade_agents_visibility(agents, export)
            self.assertEqual(report["primary_status"], "TRANSFORMED_OR_PARTIAL")

    def test_consecutive_system_messages_can_form_one_exact_rule_payload(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            agents, export, _ = self._paths(root, "A16")
            payload = agents.read_text()
            split = 8_000
            export.write_text(
                json.dumps(self._export(["prefix\n" + payload[:split], payload[split:] + "suffix"]))
            )
            report = grade_agents_visibility(agents, export)
            self.assertEqual(report["primary_status"], "FULL_EXACT_MULTI_MESSAGE")
            self.assertEqual(report["full_exact_multi_message_span"], [0, 1])

    def test_suffix_only_reports_exact_start_offset(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            agents, export, _ = self._paths(root, "A32")
            payload = agents.read_text()
            start = 16_384
            export.write_text(json.dumps(self._export([payload[start:]])))
            report = grade_agents_visibility(agents, export)
            self.assertEqual(report["primary_status"], f"SUFFIX_ONLY_FROM_{start}")
            self.assertEqual(report["longest_exact_suffix_bytes"], len(payload) - start)

    def test_invalid_export_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            agents, export, _ = self._paths(root)
            export.write_text("[]")
            with self.assertRaises(AgentsLimitError):
                grade_agents_visibility(agents, export)


class AgentsLimitRunnerTests(unittest.TestCase):
    def test_attempt_identity_is_cell_specific_and_exact(self) -> None:
        self.assertEqual(
            expected_attempt_id("A16"), "poc-vms-39-a16-tmux-a1"
        )
        validate_attempt_id("A16", "poc-vms-39-a16-tmux-a1")
        with self.assertRaisesRegex(RuntimeError, "bind the POC cell exactly"):
            validate_attempt_id("A16", "poc-vms-39-a32-tmux-a1")

    def test_task_contains_protocol_but_no_deterministic_sentinel_value(self) -> None:
        task = task_text("A16")
        first = parse_sentinels(generate_agents_fixture("A16"))[0]
        self.assertIn("Do NOT open, read, grep, list, inspect, or execute AGENTS.md", task)
        self.assertIn("solve-vein/agents-visibility-report/v1", task)
        self.assertNotIn(first["value"], task)

    def test_build_spec_rejects_wrong_fixture_size(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = root / "AGENTS.md"
            fixture.write_bytes(b"short\n")
            with self.assertRaisesRegex(RuntimeError, "byte size"):
                build_spec(
                    cell_id="A16",
                    attempt_id="poc-vms-39-a16-tmux-a1",
                    fixture_path=fixture,
                    output_bundle=root / "output",
                )

    @staticmethod
    def _fake_devin(path: Path) -> Path:
        fake = path / "devin"
        fake.write_text(
            """#!/usr/bin/env python3
import hashlib, json, os, pathlib, re, sys
args=sys.argv[1:]
if '--version' in args:
    print('devin 3000.4.25 (fake-vms39)')
    raise SystemExit(0)
if args[:2] == ['models','list']:
    print('glm-5-2 GLM-5.2 High [200K context, Free]')
    raise SystemExit(0)
assert '--sandbox' not in args
assert '-p' not in args
assert os.environ['DEVIN_SANDBOX'] == 'false'
agents=pathlib.Path('AGENTS.md').read_text()
rows=[{'name':m.group(1),'value':m.group(2)} for m in re.finditer(r'^(AGENTS_SENTINEL_[A-Z0-9]+_[0-9]+)=([0-9a-f]{32})$', agents, re.M)]
cell=rows[0]['name'].split('_')[2]
output=pathlib.Path('agents-visibility-report.json')
output.write_text(json.dumps({'schema_version':'solve-vein/agents-visibility-report/v1','cell_id':cell,'sentinels':rows}))
digest=hashlib.sha256(output.read_bytes()).hexdigest()
pathlib.Path('DONE.md').write_text('agents-visibility-report.json SHA256=' + digest)
export=pathlib.Path(args[args.index('--export')+1])
export.write_text(json.dumps({'schema_version':'ATIF-v1.7','session_id':'fake-vms39','agent':{'model_name':'GLM-5.2'},'steps':[{'step_id':'s0','source':'system','message':'PREFIX\\n'+agents+'SUFFIX','extra':{'generation_model':'glm-5-2'},'timestamp':'2026-08-14T00:00:00Z'}],'final_metrics':{}}))
print('FAKE VMS39 THINKING COMPLETE', flush=True)
for line in sys.stdin:
    if line.strip() in {'/exit','/quit','EXIT'}:
        raise SystemExit(0)
"""
        )
        fake.chmod(fake.stat().st_mode | stat.S_IXUSR)
        return fake

    def test_fake_tmux_attempt_grades_before_atomic_seal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake = self._fake_devin(root)
            fixture = root / "AGENTS.md"
            fixture.write_bytes(generate_agents_fixture("A16"))
            output = root / "sealed"
            spec = build_spec(
                cell_id="A16",
                attempt_id="poc-vms-39-a16-tmux-a1",
                fixture_path=fixture,
                output_bundle=output,
            )
            handle = start_tmux_debug_role(spec, explicit_devin_binary=fake)
            snapshot = None
            for _ in range(50):
                snapshot = snapshot_tmux_debug_role(handle)
                if snapshot["done_candidate_present"]:
                    break
                time.sleep(0.05)
            self.assertIsNotNone(snapshot)
            self.assertEqual(snapshot["state"], "DONE_WAITING_EXIT")
            send_tmux_debug_keys(
                handle,
                ("/exit", "Enter"),
                actor="unit-test",
                reason="exercise the VMS-39 graceful-exit path",
            )
            for _ in range(50):
                snapshot = snapshot_tmux_debug_role(handle)
                if snapshot["pane_dead"]:
                    break
                time.sleep(0.05)
            self.assertTrue(snapshot["pane_dead"])
            result = finalize_agents_limit_attempt(handle)
            self.assertEqual(result["primary_status"], "FULL_EXACT_SINGLE_MESSAGE")
            self.assertEqual(result["model_report"]["recall"], 1.0)
            self.assertEqual(
                result["runtime_receipt"]["model_observability_verdict"], "MATCH"
            )
            grader = output / "workspace" / "agents-visibility-grader-report.json"
            self.assertTrue(grader.is_file())
            self.assertEqual(
                json.loads(grader.read_text())["primary_status"],
                "FULL_EXACT_SINGLE_MESSAGE",
            )
            with self.assertRaisesRegex(RoleRuntimeError, "VMS39_GRADER_REPORT_EXISTS"):
                # The sealed handle no longer points at a live workspace; this
                # also proves the report itself is append-once and not replaced.
                from system.tests.solve_vein_analysis.run_agents_limit_poc import (
                    write_grader_report_before_seal,
                )

                write_grader_report_before_seal(
                    type(handle)(
                        attempt_id=handle.attempt_id,
                        live_bundle=output,
                        output_bundle=output,
                        workspace=output / "workspace",
                        socket_name=handle.socket_name,
                        session_name=handle.session_name,
                    )
                )


if __name__ == "__main__":
    unittest.main()
