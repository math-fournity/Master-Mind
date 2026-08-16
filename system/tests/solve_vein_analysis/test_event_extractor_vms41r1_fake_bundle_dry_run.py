from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from system.tests.solve_vein_analysis import vms41r1_fake_bundle_append_only_dry_run as dry_run
from system.tests.solve_vein_analysis import vms41r1_fake_live_bundle_materializer as materializer


class VMS41R1FakeBundleAppendOnlyDryRunTests(unittest.TestCase):
    def test_writes_expected_visible_files_to_empty_temp_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "bundle"
            receipt = dry_run.write_fake_bundle_append_only_dry_run(root)
            self.assertEqual(
                receipt["schema_version"],
                "solve-vein/vms41r1-fake-bundle-append-only-dry-run/v1",
            )
            self.assertEqual(receipt["dry_run_status"], "APPEND_ONLY_FAKE_BUNDLE_WRITTEN")
            self.assertEqual(receipt["case_count"], 6)
            self.assertEqual(receipt["side_effects"]["local_files_written"], 31)
            for row in receipt["case_rows"]:
                case_dir = root / row["case_dir_name"]
                self.assertEqual(
                    {path.name for path in case_dir.iterdir()},
                    set(materializer.VISIBLE_REVIEW_FILES),
                )
                self.assertTrue(all(not (case_dir / name).exists() for name in materializer.FORBIDDEN_HIDDEN_FILES))

    def test_second_write_to_same_root_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "bundle"
            dry_run.write_fake_bundle_append_only_dry_run(root)
            with self.assertRaisesRegex(dry_run.VMS41R1FakeBundleDryRunError, "OUTPUT_ROOT_NOT_EMPTY"):
                dry_run.write_fake_bundle_append_only_dry_run(root)

    def test_repo_output_root_is_rejected_without_writing(self) -> None:
        root = dry_run.REPO_ROOT / "vms41r1-forbidden-output-root"
        with self.assertRaisesRegex(dry_run.VMS41R1FakeBundleDryRunError, "REPO_OUTPUT_ROOT_REJECTED"):
            dry_run.write_fake_bundle_append_only_dry_run(root)
        self.assertFalse(root.exists())

    def test_symlink_output_root_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "target"
            link = Path(tmp) / "link"
            target.mkdir()
            link.symlink_to(target)
            with self.assertRaisesRegex(dry_run.VMS41R1FakeBundleDryRunError, "SYMLINK_PATH_REJECTED"):
                dry_run.write_fake_bundle_append_only_dry_run(link)

    def test_cli_writes_temp_bundle_and_reports_no_model_side_effects(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "cli-bundle"
            completed = subprocess.run(
                [
                    sys.executable,
                    "system/tests/solve_vein_analysis/vms41r1_fake_bundle_append_only_dry_run.py",
                    "--output-root",
                    str(root),
                ],
                cwd=dry_run.REPO_ROOT,
                text=True,
                capture_output=True,
                check=True,
            )
            receipt = json.loads(completed.stdout)
            self.assertEqual(receipt["case_count"], 6)
            self.assertEqual(receipt["side_effects"]["devin_sessions"], 0)
            self.assertEqual(receipt["side_effects"]["database_connections"], 0)
            self.assertTrue((root / dry_run.BUNDLE_MANIFEST).is_file())


if __name__ == "__main__":
    unittest.main()
