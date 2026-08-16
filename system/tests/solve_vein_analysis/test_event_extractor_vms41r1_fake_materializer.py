from __future__ import annotations

import json
import subprocess
import sys
import unittest

from system.tests.solve_vein_analysis import vms41r1_fake_live_bundle_materializer as materializer
from system.tests.solve_vein_analysis.build_vms41r1_qualification_pack import CASE_ORDER


class VMS41R1FakeMaterializerTests(unittest.TestCase):
    def test_materializer_builds_one_plan_per_case_without_side_effects(self) -> None:
        receipt = materializer.build_fake_materialization_plan()
        self.assertEqual(
            receipt["schema_version"],
            "solve-vein/vms41r1-fake-live-bundle-materializer/v1",
        )
        self.assertEqual(receipt["materializer_status"], "PLAN_ONLY_NO_FILES_WRITTEN")
        self.assertEqual(receipt["case_count"], 6)
        self.assertEqual(receipt["fake_live_output_count"], 6)
        self.assertEqual(receipt["blind_review_package_count"], 6)
        self.assertEqual(receipt["hidden_public_split_verdict"], "PASS")
        self.assertTrue(all(value == 0 for value in receipt["side_effects"].values()))
        self.assertEqual(
            [row["case_id"] for row in receipt["case_rows"]],
            list(CASE_ORDER),
        )

    def test_reviewer_visible_files_are_exact_and_hide_hidden_inputs(self) -> None:
        receipt = materializer.build_fake_materialization_plan()
        expected = set(materializer.VISIBLE_REVIEW_FILES)
        forbidden = set(materializer.FORBIDDEN_HIDDEN_FILES)
        for row in receipt["case_rows"]:
            self.assertEqual(set(row["reviewer_visible_files"]), expected)
            self.assertEqual(set(row["forbidden_hidden_files"]), forbidden)
            self.assertEqual(row["hidden_files_exposed"], [])
            self.assertEqual(
                row["candidate_output_source"],
                "HIDDEN_REFERENCE_CANDIDATE_AS_FAKE_LIVE_OUTPUT",
            )

    def test_cli_outputs_zero_side_effect_json(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/tests/solve_vein_analysis/vms41r1_fake_live_bundle_materializer.py",
            ],
            cwd=materializer.REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        receipt = json.loads(completed.stdout)
        self.assertEqual(receipt["case_count"], 6)
        self.assertEqual(receipt["side_effects"]["files_written"], 0)
        self.assertIn("does_not_use_real_devin_output", receipt["explicit_nonclaims"])

    def test_candidate_override_changes_only_target_candidate_hash(self) -> None:
        baseline = materializer.build_fake_materialization_plan()
        case_id = "V41R1-SYN-TRUE-MERGE"
        override = {"schema_version": "fake", "events": [], "relations": []}
        changed = materializer.build_fake_materialization_plan(
            candidate_overrides={case_id: override}
        )
        baseline_by_case = {row["case_id"]: row for row in baseline["case_rows"]}
        changed_by_case = {row["case_id"]: row for row in changed["case_rows"]}
        for current_case in CASE_ORDER:
            same = (
                baseline_by_case[current_case]["candidate_output_sha256"]
                == changed_by_case[current_case]["candidate_output_sha256"]
            )
            self.assertEqual(same, current_case != case_id)


if __name__ == "__main__":
    unittest.main()
