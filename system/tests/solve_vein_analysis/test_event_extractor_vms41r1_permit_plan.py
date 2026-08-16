from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from system.tests.solve_vein_analysis import build_vms41r1_live_permit_review_plan as plan


class VMS41R1PermitPlanTests(unittest.TestCase):
    def test_default_plan_is_not_a_live_permit(self) -> None:
        receipt = plan.build_plan()

        self.assertEqual(
            receipt["schema_version"],
            "solve-vein/vms41r1-live-permit-review-plan/v1",
        )
        self.assertEqual(receipt["runner_preflight_status"], "READY_FOR_AUTHORIZATION")
        self.assertEqual(receipt["runner_live_authorization_status"], "NOT_AUTHORIZED")
        self.assertFalse(receipt["live_run_permit"]["permit_consumable"])
        self.assertEqual(receipt["live_run_permit"]["authorized_live_attempts"], 0)
        self.assertIsNone(receipt["live_run_permit"]["required_human_authorization_ref"])
        self.assertEqual(receipt["blind_review_plan"]["case_count"], 6)
        self.assertTrue(
            receipt["blind_review_plan"][
                "sealed_manual_judgment_required_before_hidden_join"
            ]
        )
        self.assertTrue(all(value == 0 for value in receipt["side_effects"].values()))

    def test_hidden_grader_files_are_not_reviewer_visible(self) -> None:
        receipt = plan.build_plan()
        hidden = {
            "acceptable-sets.json",
            "reference-candidates.json",
            "negative-checks.json",
            "thresholds.json",
            "blind-review-rubric.md",
        }
        for case_plan in receipt["blind_review_plan"]["case_plans"]:
            visible = set(case_plan["blind_review_visible_files_after_live"])
            self.assertFalse(hidden.intersection(visible), case_plan["case_id"])
            self.assertEqual(set(case_plan["blind_review_forbidden_files"]), hidden)
            self.assertEqual(case_plan["mechanical_grading_before_manual_seal"], "FORBIDDEN")

    def test_canonical_cli_output_is_valid_json(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/tests/solve_vein_analysis/build_vms41r1_live_permit_review_plan.py",
                "--canonical",
            ],
            cwd=plan.REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        value = json.loads(completed.stdout)
        self.assertFalse(value["live_run_permit"]["permit_consumable"])
        self.assertEqual(value["blind_review_plan"]["case_count"], 6)
        self.assertEqual(value["side_effects"]["devin_sessions"], 0)

    def test_rejects_occupied_output_root(self) -> None:
        fake = plan.build_plan()
        # Keep the shape from a real plan but simulate the runner refusing to
        # proceed because the future result root is no longer clear.
        fake_preflight = {
            "overall_status": "READY_FOR_AUTHORIZATION",
            "live_authorization_status": "NOT_AUTHORIZED",
            "output_root_status": "OCCUPIED_OR_REQUIRES_RECONCILIATION",
            "attempt_plan": [
                {
                    "case_id": row["case_id"],
                    "attempt_id": row["attempt_id"],
                }
                for row in fake["blind_review_plan"]["case_plans"]
            ],
            "freeze_path": fake["freeze_path"],
            "freeze_sha256": fake["freeze_sha256"],
        }
        with mock.patch.object(plan, "build_preflight_receipt", return_value=fake_preflight):
            with self.assertRaisesRegex(plan.VMS41R1PlanError, "OUTPUT_ROOT_NOT_CLEAR"):
                plan.build_plan()

    def test_rejects_hidden_file_in_visible_plan(self) -> None:
        with self.assertRaisesRegex(plan.VMS41R1PlanError, "ATTEMPT_PLAN_INVALID"):
            plan._case_plan({"case_id": "CASE_WITHOUT_ATTEMPT"})

        original = plan.HIDDEN_FORBIDDEN_FILES
        try:
            with mock.patch.object(plan, "HIDDEN_FORBIDDEN_FILES", ("DONE.md",)):
                with self.assertRaisesRegex(plan.VMS41R1PlanError, "HIDDEN_FILE_VISIBLE"):
                    plan._case_plan({"case_id": "C", "attempt_id": "A"})
        finally:
            self.assertIs(plan.HIDDEN_FORBIDDEN_FILES, original)

    def test_tampered_freeze_path_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.freeze.json"
            bad.write_text("{}")
            completed = subprocess.run(
                [
                    sys.executable,
                    "system/tests/solve_vein_analysis/build_vms41r1_live_permit_review_plan.py",
                    "--freeze",
                    str(bad),
                ],
                cwd=plan.REPO_ROOT,
                text=True,
                capture_output=True,
            )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("VMS41R1_PLAN_ERROR", completed.stderr)


if __name__ == "__main__":
    unittest.main()
