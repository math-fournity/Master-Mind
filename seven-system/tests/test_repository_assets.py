from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM_ROOT / "src"))

from seven_system.config import ConfigError, load_config  # noqa: E402


class RepositoryAssetTests(unittest.TestCase):
    def test_example_config_parses(self) -> None:
        config = load_config(SYSTEM_ROOT / "config" / "runtime.example.json")
        self.assertEqual(config.system_id, "seven-system")
        self.assertEqual(config.mode, "dry_run")
        self.assertFalse(config.allow_live_solver_dispatch)

    def test_solver_asset_contains_no_tool_contract_and_no_answer_placeholder(self) -> None:
        text = (SYSTEM_ROOT / "assets" / "solver" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "不要使用任何工具",
            "### PROOF COMPLETE",
            "### I CANNOT SOLVE THIS",
            "### ANSWER LEAK DETECTED",
            "{{PROBLEM_STATEMENT}}",
            "{{INTERVENTION_TEXT}}",
        ):
            self.assertIn(phrase, text)
        self.assertNotIn("{{SOLUTION", text.upper())
        self.assertNotIn("{{ANSWER", text.upper())

    def test_all_json_schemas_are_valid_json(self) -> None:
        for path in (SYSTEM_ROOT / "schemas").glob("*.json"):
            with self.subTest(path=path.name):
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(payload["$schema"], "https://json-schema.org/draft/2020-12/schema")

    def test_config_rejects_unknown_schema_and_string_booleans(self) -> None:
        source = SYSTEM_ROOT / "config" / "runtime.example.json"
        payload = json.loads(source.read_text(encoding="utf-8"))
        payload["schema_version"] = "seven-config/v999"
        with self.assertRaises(ConfigError):
            from seven_system.config import SevenConfig

            SevenConfig.from_mapping(payload)

        payload["schema_version"] = "seven-config/v1"
        payload["database"]["allow_writes"] = "false"
        with self.assertRaises(ConfigError):
            SevenConfig.from_mapping(payload)

        payload["database"]["allow_writes"] = False
        payload["unexpected"] = "must not be ignored"
        with tempfile.TemporaryDirectory() as directory:
            config_path = Path(directory) / "runtime.json"
            config_path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaises(ConfigError):
                load_config(config_path)


if __name__ == "__main__":
    unittest.main()
