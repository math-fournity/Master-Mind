from __future__ import annotations

import json
import subprocess
import sys
import unittest

from system.tests.solve_vein_analysis import vms41r1_fake_live_bundle_materializer as materializer
from system.tests.solve_vein_analysis import vms41r1_final_qualification_join_receipt as final_join
from system.tests.solve_vein_analysis import vms41r1_hidden_join_simulator as simulator


class VMS41R1FinalQualificationJoinReceiptTests(unittest.TestCase):
    def test_reference_chain_builds_development_only_final_receipt(self) -> None:
        receipt = final_join.build_final_qualification_join_receipt()
        self.assertEqual(
            receipt["schema_version"],
            "solve-vein/vms41r1-final-qualification-join-receipt/v1",
        )
        self.assertEqual(receipt["receipt_status"], "FINAL_JOIN_RECEIPT_DEVELOPMENT_ONLY")
        self.assertEqual(receipt["case_count"], 6)
        self.assertEqual(receipt["final_join_verdict"], "PASS_DEVELOPMENT_SIMULATION_ONLY")
        self.assertEqual(
            receipt["profile_qualification_verdict"],
            "NOT_QUALIFIED_LIVE_NOT_AUTHORIZED",
        )
        self.assertTrue(all(value == 0 for value in receipt["side_effects"].values()))

    def test_mutated_candidate_propagates_fail_without_profile_qualification(self) -> None:
        case_id = "V41R1-SYN-TEMPORAL-CORRECTION"
        mutated = simulator.mutated_reference_candidate(case_id)
        receipt = final_join.build_final_qualification_join_receipt(
            materializer_candidate_overrides={case_id: mutated},
            hidden_join_candidate_overrides={case_id: mutated},
        )
        row = next(row for row in receipt["case_rows"] if row["case_id"] == case_id)
        self.assertEqual(row["join_verdict"], "JOIN_FAIL_OR_INCONCLUSIVE_DEVELOPMENT_ONLY")
        self.assertEqual(
            receipt["final_join_verdict"],
            "FAIL_OR_INCONCLUSIVE_DEVELOPMENT_SIMULATION_ONLY",
        )
        self.assertEqual(
            receipt["profile_qualification_verdict"],
            "NOT_QUALIFIED_LIVE_NOT_AUTHORIZED",
        )

    def test_candidate_hash_mismatch_blocks_final_join(self) -> None:
        case_id = "V41R1-SYN-TEMPORAL-CORRECTION"
        mutated = simulator.mutated_reference_candidate(case_id)
        with self.assertRaisesRegex(
            final_join.VMS41R1FinalJoinReceiptError,
            "CANDIDATE_HASH_MISMATCH",
        ):
            final_join.build_final_qualification_join_receipt(
                hidden_join_candidate_overrides={case_id: mutated}
            )

    def test_nonzero_materializer_side_effect_blocks_assembly(self) -> None:
        materializer_receipt = materializer.build_fake_materialization_plan()
        hidden_join_receipt = simulator.simulate_hidden_join()
        materializer_receipt["side_effects"]["files_written"] = 1
        with self.assertRaisesRegex(
            final_join.VMS41R1FinalJoinReceiptError,
            "side_effect_nonzero",
        ):
            final_join.assemble_final_qualification_join_receipt(
                materializer_receipt=materializer_receipt,
                hidden_join_receipt=hidden_join_receipt,
            )

    def test_cli_outputs_zero_side_effect_json(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/tests/solve_vein_analysis/vms41r1_final_qualification_join_receipt.py",
            ],
            cwd=final_join.REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        receipt = json.loads(completed.stdout)
        self.assertEqual(receipt["case_count"], 6)
        self.assertEqual(receipt["side_effects"]["devin_sessions"], 0)
        self.assertIn("does_not_qualify_event_extractor_profile", receipt["explicit_nonclaims"])


if __name__ == "__main__":
    unittest.main()
