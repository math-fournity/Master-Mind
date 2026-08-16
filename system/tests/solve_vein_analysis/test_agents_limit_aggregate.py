from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from system.solve_vein_analysis.role_runtime import canonical_json_bytes, sha256_file
from system.tests.solve_vein_analysis.aggregate_agents_limit_live import (
    EXECUTED_CELLS,
    LiveAggregateError,
    _derive_boundary,
    _tree_manifest,
)


class AgentsLimitAggregateTests(unittest.TestCase):
    def _row(self, cell: str, status: str, prefix: int, marker: bool) -> dict:
        return {
            "cell_id": cell,
            "primary_status": status,
            "longest_exact_prefix_bytes": prefix,
            "truncation_marker_16384_observed": marker,
            "pane_dead_status": 0,
            "intervention_count": 1,
            "effective_model_uids": ["glm-5-2"],
        }

    def test_exact_boundary_requires_full_and_truncated_cells(self) -> None:
        rows = [
            self._row("A16M1", "FULL_EXACT_SINGLE_MESSAGE", 16_383, False),
            self._row("A16", "FULL_EXACT_SINGLE_MESSAGE", 16_384, False),
            self._row("A16P1", "PREFIX_TRUNCATED_AT_16383", 16_383, True),
            self._row("A32", "PREFIX_TRUNCATED_AT_16384", 16_384, True),
        ]
        verdict = _derive_boundary(rows)
        self.assertEqual(verdict["observed_loader_cap_bytes"], 16_384)
        self.assertTrue(verdict["verdict"].startswith("SUPPORTS_EXACT_16384"))

    def test_missing_marker_is_inconclusive(self) -> None:
        rows = [
            self._row("A16M1", "FULL_EXACT_SINGLE_MESSAGE", 16_383, False),
            self._row("A16", "FULL_EXACT_SINGLE_MESSAGE", 16_384, False),
            self._row("A16P1", "PREFIX_TRUNCATED_AT_16383", 16_383, True),
            self._row("A32", "PREFIX_TRUNCATED_AT_16384", 16_384, False),
        ]
        self.assertEqual(_derive_boundary(rows)["verdict"], "INCONCLUSIVE_LIVE_BOUNDARY")

    def test_executed_cell_set_is_exact(self) -> None:
        rows = [
            self._row(cell, "FULL_EXACT_SINGLE_MESSAGE", 1, False)
            for cell in EXECUTED_CELLS[:-1]
        ]
        with self.assertRaises(LiveAggregateError):
            _derive_boundary(rows)

    def test_tree_manifest_hashes_all_regular_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "a").write_bytes(b"a")
            (root / "b").mkdir()
            (root / "b" / "c").write_bytes(b"c")
            rows, tree_hash = _tree_manifest(root)
            self.assertEqual([row["ref"] for row in rows], ["a", "b/c"])
            self.assertEqual(len(tree_hash), 64)
            self.assertEqual(rows[0]["sha256"], sha256_file(root / "a"))
            self.assertEqual(
                len(canonical_json_bytes(rows)) > 0,
                True,
            )

    def test_tree_manifest_rejects_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "source").write_text("x")
            (root / "link").symlink_to(root / "source")
            with self.assertRaises(LiveAggregateError):
                _tree_manifest(root)

    def test_receipt_hash_pattern_is_canonical(self) -> None:
        payload = {"z": 1, "a": 2}
        encoded = canonical_json_bytes(payload)
        self.assertEqual(json.loads(encoded), payload)


if __name__ == "__main__":
    unittest.main()
