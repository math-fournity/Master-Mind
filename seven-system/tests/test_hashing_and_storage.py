from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.hashing import canonical_json_bytes, object_hash  # noqa: E402
from seven_system.storage import (  # noqa: E402
    ContentConflictError,
    commit_json_once,
)


class HashingAndStorageTests(unittest.TestCase):
    def test_canonical_hash_ignores_mapping_order_and_normalizes_newlines(self) -> None:
        left = {"b": "x\r\ny", "a": 1}
        right = {"a": 1, "b": "x\ny"}
        self.assertEqual(canonical_json_bytes(left), canonical_json_bytes(right))
        self.assertEqual(
            object_hash("Thing", "v1", left), object_hash("Thing", "v1", right)
        )

    def test_commit_is_idempotent_and_never_overwrites_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            self.assertEqual(commit_json_once(path, {"value": 1}), "COMMITTED")
            self.assertEqual(
                commit_json_once(path, {"value": 1}), "ALREADY_COMMITTED"
            )
            with self.assertRaises(ContentConflictError):
                commit_json_once(path, {"value": 2})
            self.assertIn(b'"value":1', path.read_bytes())


if __name__ == "__main__":
    unittest.main()
