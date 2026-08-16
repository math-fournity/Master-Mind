from __future__ import annotations

import json
import subprocess
import sys
import unittest

from system.tests.solve_vein_analysis import vms41r1_hidden_join_simulator as simulator
from system.tests.solve_vein_analysis import vms41r1_manual_judgment_contract as contract


class VMS41R1HiddenJoinSimulatorTests(unittest.TestCase):
    def test_reference_candidates_join_pass_development_only(self) -> None:
        receipt = simulator.simulate_hidden_join()
        self.assertEqual(
            receipt["schema_version"],
            "solve-vein/vms41r1-hidden-join-simulator/v1",
        )
        self.assertEqual(receipt["simulator_status"], "DEVELOPMENT_ONLY")
        self.assertEqual(receipt["case_count"], 6)
        self.assertEqual(receipt["overall_join_verdict"], "PASS_DEVELOPMENT_SIMULATION_ONLY")
        self.assertTrue(all(value == 0 for value in receipt["side_effects"].values()))
        self.assertTrue(
            all(row["manual_judgment_validated_before_hidden_eval"] for row in receipt["join_rows"])
        )

    def test_invalid_manual_judgment_blocks_hidden_join(self) -> None:
        attempt_map = contract.expected_attempt_map()
        case_id = sorted(attempt_map)[0]
        bad = simulator._fake_manual_judgment(case_id, attempt_map[case_id])
        bad["reviewer_blinding_attestation"]["hidden_acceptable_set_seen"] = True
        with self.assertRaisesRegex(
            simulator.VMS41R1HiddenJoinError,
            "MANUAL_JUDGMENT_INVALID_BEFORE_HIDDEN_JOIN",
        ):
            simulator.simulate_hidden_join(manual_judgment_overrides={case_id: bad})

    def test_attempt_mismatch_blocks_hidden_join(self) -> None:
        attempt_map = contract.expected_attempt_map()
        case_id = sorted(attempt_map)[0]
        bad = simulator._fake_manual_judgment(case_id, attempt_map[case_id])
        bad["attempt_id"] = "wrong-attempt"
        with self.assertRaisesRegex(simulator.VMS41R1HiddenJoinError, "attempt_id_mismatch"):
            simulator.simulate_hidden_join(manual_judgment_overrides={case_id: bad})

    def test_mutated_candidate_fails_join(self) -> None:
        case_id = "V41R1-SYN-TEMPORAL-CORRECTION"
        mutated = simulator.mutated_reference_candidate(case_id)
        receipt = simulator.simulate_hidden_join(candidate_overrides={case_id: mutated})
        row = next(row for row in receipt["join_rows"] if row["case_id"] == case_id)
        self.assertEqual(row["join_verdict"], "JOIN_FAIL_OR_INCONCLUSIVE_DEVELOPMENT_ONLY")
        self.assertEqual(
            receipt["overall_join_verdict"],
            "FAIL_OR_INCONCLUSIVE_DEVELOPMENT_SIMULATION_ONLY",
        )

    def test_cli_outputs_zero_side_effect_json(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "system/tests/solve_vein_analysis/vms41r1_hidden_join_simulator.py",
            ],
            cwd=simulator.REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        receipt = json.loads(completed.stdout)
        self.assertEqual(receipt["case_count"], 6)
        self.assertEqual(receipt["side_effects"]["devin_sessions"], 0)
        self.assertIn("does_not_use_real_candidate_output", receipt["explicit_nonclaims"])


if __name__ == "__main__":
    unittest.main()
