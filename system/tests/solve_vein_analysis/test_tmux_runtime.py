"""Contract tests for the independent interactive tmux debug profile."""

from __future__ import annotations

from contextlib import redirect_stderr
import io
import json
from pathlib import Path
import stat
import sys
import tempfile
import time
import unittest

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from system.solve_vein_analysis.role_runtime import DevinRoleSpec, RoleInput, RoleRuntimeError
from system.solve_vein_analysis.tmux_runtime import (
    abort_tmux_debug_role,
    finalize_tmux_debug_role,
    load_tmux_debug_handle,
    send_tmux_debug_keys,
    snapshot_tmux_debug_role,
    start_tmux_debug_role,
)
from system.tests.solve_vein_analysis.run_tmux_canary import (
    _validate_attempt_id,
    parser as tmux_canary_parser,
)


class TmuxDebugRuntimeTests(unittest.TestCase):
    def test_canary_attempt_identity_is_required_and_exact(self) -> None:
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                tmux_canary_parser().parse_args(
                    [
                        "start",
                        "--poc-id",
                        "POC-VMS-38",
                        "--freeze",
                        "freeze.json",
                        "--output",
                        "/data/example",
                    ]
                )
        _validate_attempt_id(
            "POC-VMS-38", "poc-vms-38-extractor-tmux-a1"
        )
        with self.assertRaisesRegex(RuntimeError, "bind the POC identity"):
            _validate_attempt_id(
                "POC-VMS-38", "poc-vms-37-extractor-tmux-a1"
            )

    def _fixture(self, root: Path) -> tuple[Path, Path]:
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
assert '-p' not in args
assert os.environ['DEVIN_SANDBOX'] == 'false'
export=pathlib.Path(args[args.index('--export')+1])
export.write_text(json.dumps({'session_id':'fake-tmux','steps':[{'step_type':'assistant','extra':{'generation_model':'glm-5-2'}}]}))
pathlib.Path('result.json').write_text('{}')
digest=hashlib.sha256(pathlib.Path('result.json').read_bytes()).hexdigest()
pathlib.Path('DONE.md').write_text('result.json SHA256=' + digest)
print('FAKE THINKING SPIN COMPLETE', flush=True)
for line in sys.stdin:
    if line.strip() in {'/exit','/quit','EXIT'}:
        raise SystemExit(0)
"""
        )
        fake.chmod(fake.stat().st_mode | stat.S_IXUSR)
        asset = root / "asset.md"
        asset.write_text("# fake role\n")
        source = root / "source.txt"
        source.write_text("input\n")
        return fake, asset

    def test_interactive_tmux_is_observable_intervention_logged_and_sealed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake, asset = self._fixture(root)
            source = root / "source.txt"
            source.write_text("input\n")
            output = root / "sealed"
            spec = DevinRoleSpec(
                attempt_id="tmux-contract-a1",
                role="tmux_contract_test",
                role_asset_path=asset,
                task_text="write the frozen result",
                inputs=(RoleInput(source, "source.txt"),),
                expected_output_name="result.json",
                output_bundle=output,
                sandbox_requested=False,
            )
            handle = start_tmux_debug_role(spec, explicit_devin_binary=fake)
            handle = load_tmux_debug_handle(handle.live_bundle)
            self.assertFalse(output.exists())
            snapshot = None
            for _ in range(50):
                snapshot = snapshot_tmux_debug_role(handle)
                if snapshot["done_candidate_present"]:
                    break
                time.sleep(0.05)
            self.assertIsNotNone(snapshot)
            self.assertTrue(snapshot["session_present"])
            self.assertEqual(snapshot["state"], "DONE_WAITING_EXIT")
            capture = handle.live_bundle / str(snapshot["capture_ref"])
            self.assertIn("FAKE THINKING SPIN COMPLETE", capture.read_text())
            with self.assertRaisesRegex(RoleRuntimeError, "TMUX_DEBUG_STILL_RUNNING"):
                finalize_tmux_debug_role(handle)
            send_tmux_debug_keys(
                handle,
                ("/exit", "Enter"),
                actor="unit-test",
                reason="exercise the recorded graceful-exit path",
            )
            for _ in range(50):
                snapshot = snapshot_tmux_debug_role(handle)
                if snapshot["pane_dead"]:
                    break
                time.sleep(0.05)
            self.assertTrue(snapshot["pane_dead"])
            receipt = finalize_tmux_debug_role(handle)
            self.assertTrue(output.is_dir())
            self.assertEqual(receipt["execution_mode"], "INTERACTIVE_TMUX_DEBUG")
            self.assertEqual(receipt["evidence_lane"], "DEVELOPMENT_ONLY")
            self.assertEqual(receipt["model_observability_verdict"], "MATCH")
            self.assertTrue(receipt["done_marker_content_valid"])
            self.assertEqual(receipt["intervention_count"], 1)
            self.assertEqual(receipt["human_intervention"], "INPUT_SENT")
            launch = json.loads(
                (output / "tmux-debug-launch-receipt.json").read_text()
            )
            self.assertFalse(launch["shell_interpolation_used"])
            self.assertNotIn("write the frozen result", launch["sanitized_devin_argv"])

    def test_abort_preserves_failed_debug_attempt_as_development_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake, asset = self._fixture(root)
            source = root / "source.txt"
            output = root / "aborted"
            spec = DevinRoleSpec(
                attempt_id="tmux-contract-abort-a1",
                role="tmux_contract_test",
                role_asset_path=asset,
                task_text="write then remain interactive",
                inputs=(RoleInput(source, "source.txt"),),
                expected_output_name="result.json",
                output_bundle=output,
                sandbox_requested=False,
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
            receipt = abort_tmux_debug_role(
                handle,
                actor="unit-test",
                reason="exercise fail-closed cleanup",
            )
            self.assertEqual(receipt["terminal_status"], "ABORTED")
            self.assertEqual(receipt["evidence_lane"], "DEVELOPMENT_ONLY")
            self.assertTrue((output / "workspace" / "result.json").is_file())
            self.assertTrue((output / "tmux-debug-abort-receipt.json").is_file())

    def test_sandbox_profile_and_unrecordable_keys_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake, asset = self._fixture(root)
            source = root / "source.txt"
            source.write_text("input\n")
            spec = DevinRoleSpec(
                attempt_id="tmux-contract-a2",
                role="tmux_contract_test",
                role_asset_path=asset,
                task_text="test",
                inputs=(RoleInput(source, "source.txt"),),
                expected_output_name="result.json",
                output_bundle=root / "sealed",
                sandbox_requested=True,
            )
            with self.assertRaisesRegex(RoleRuntimeError, "TMUX_DEBUG_PROFILE_MISMATCH"):
                start_tmux_debug_role(spec, explicit_devin_binary=fake)


if __name__ == "__main__":
    unittest.main()
