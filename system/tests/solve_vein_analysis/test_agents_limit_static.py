from __future__ import annotations

import json
from pathlib import Path
import stat
import tempfile
import unittest

from system.tests.solve_vein_analysis.run_agents_limit_static import (
    StaticLoaderError,
    run_static_loader,
    seal_static_loader_audit,
    verify_static_loader_bundle,
)


class AgentsLimitStaticRunnerTests(unittest.TestCase):
    @staticmethod
    def _fake_devin(root: Path, *, truncate_show: bool = False) -> Path:
        fake = root / "devin"
        fake.write_text(
            """#!/usr/bin/env python3
import pathlib, sys
args=sys.argv[1:]
if args == ['--version']:
    print('devin 3000.4.25 (fake-static)')
elif args == ['rules', 'paths']:
    print('Current directory:', pathlib.Path.cwd())
elif args == ['rules', 'list']:
    print('AGENTS [Standard] always-on')
elif args == ['rules', 'show', 'AGENTS']:
    data=pathlib.Path('AGENTS.md').read_bytes()
    if __TRUNCATE__:
        data=data[:16384]
    sys.stdout.buffer.write(b'Content:\\n---\\n' + data + b'---\\n')
else:
    raise SystemExit(9)
""".replace("__TRUNCATE__", "True" if truncate_show else "False")
        )
        fake.chmod(fake.stat().st_mode | stat.S_IXUSR)
        return fake

    @staticmethod
    def _protocol_and_freeze(root: Path) -> tuple[Path, Path]:
        protocol = root / "protocol.md"
        freeze = root / "freeze.json"
        protocol.write_text("frozen protocol\n")
        freeze.write_text(json.dumps({"schema_version": "test-freeze/v1"}))
        return protocol, freeze

    def test_full_exact_static_show_seals_append_once_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake = self._fake_devin(root)
            protocol, freeze = self._protocol_and_freeze(root)
            output = root / "result"
            receipt = run_static_loader(
                devin_binary=fake,
                output_bundle=output,
                protocol_path=protocol,
                freeze_path=freeze,
                cell_ids=("A16", "A32"),
            )
            self.assertEqual(receipt["overall_status"], "STATIC_SHOW_FULL_EXACT_ALL_CELLS")
            self.assertEqual(receipt["model_invocations"], 0)
            self.assertTrue((output / "static-loader-receipt.json").is_file())
            self.assertTrue(all(row["full_fixture_exact_substring_in_show"] for row in receipt["cells"]))
            self.assertTrue(all("path" not in row["fixture"] for row in receipt["cells"]))
            self.assertTrue(all(row["fixture"]["fixture_ref"] == "workspace/AGENTS.md" for row in receipt["cells"]))
            verification = verify_static_loader_bundle(output)
            self.assertEqual(verification["artifact_integrity"], "PASS")
            self.assertEqual(verification["errors"], [])

    def test_partial_show_is_preserved_but_not_promoted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake = self._fake_devin(root, truncate_show=True)
            protocol, freeze = self._protocol_and_freeze(root)
            output = root / "result"
            receipt = run_static_loader(
                devin_binary=fake,
                output_bundle=output,
                protocol_path=protocol,
                freeze_path=freeze,
                cell_ids=("A32",),
            )
            self.assertEqual(receipt["overall_status"], "STATIC_VIEW_INSUFFICIENT_OR_COMMAND_FAILURE")
            self.assertEqual(receipt["cells"][0]["primary_status"], "STATIC_VIEW_INSUFFICIENT")
            self.assertTrue(output.is_dir())

    def test_existing_output_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake = self._fake_devin(root)
            protocol, freeze = self._protocol_and_freeze(root)
            output = root / "result"
            output.mkdir()
            with self.assertRaisesRegex(StaticLoaderError, "output already exists"):
                run_static_loader(
                    devin_binary=fake,
                    output_bundle=output,
                    protocol_path=protocol,
                    freeze_path=freeze,
                    cell_ids=("A16",),
                )

    def test_duplicate_cell_list_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake = self._fake_devin(root)
            protocol, freeze = self._protocol_and_freeze(root)
            with self.assertRaisesRegex(StaticLoaderError, "non-empty and unique"):
                run_static_loader(
                    devin_binary=fake,
                    output_bundle=root / "result",
                    protocol_path=protocol,
                    freeze_path=freeze,
                    cell_ids=("A16", "A16"),
                )

    def test_integrity_verifier_rejects_modified_raw_stream(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake = self._fake_devin(root)
            protocol, freeze = self._protocol_and_freeze(root)
            output = root / "result"
            run_static_loader(
                devin_binary=fake,
                output_bundle=output,
                protocol_path=protocol,
                freeze_path=freeze,
                cell_ids=("A16",),
            )
            raw = output / "A16" / "evidence" / "rules-list.stdout"
            raw.write_text("tampered\n")
            verification = verify_static_loader_bundle(output)
            self.assertEqual(verification["artifact_integrity"], "FAIL")
            self.assertTrue(any("sha256_mismatch" in error for error in verification["errors"]))

    def test_legacy_unindexed_auxiliary_is_partial_not_primary_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake = self._fake_devin(root)
            protocol, freeze = self._protocol_and_freeze(root)
            output = root / "result"
            run_static_loader(
                devin_binary=fake,
                output_bundle=output,
                protocol_path=protocol,
                freeze_path=freeze,
                cell_ids=("A16",),
            )
            auxiliary = output / "A16" / "workspace" / "isolated-home" / "legacy.log"
            auxiliary.parent.mkdir(parents=True, exist_ok=True)
            auxiliary.write_text("legacy auxiliary\n")
            verification = verify_static_loader_bundle(output)
            self.assertEqual(verification["primary_artifact_integrity"], "PASS")
            self.assertEqual(verification["auxiliary_artifact_integrity"], "UNINDEXED")
            self.assertEqual(verification["artifact_integrity"], "PARTIAL_UNINDEXED_AUXILIARY")

    def test_separate_audit_receipt_hashes_complete_source_tree(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fake = self._fake_devin(root)
            protocol, freeze = self._protocol_and_freeze(root)
            output = root / "result"
            run_static_loader(
                devin_binary=fake,
                output_bundle=output,
                protocol_path=protocol,
                freeze_path=freeze,
                cell_ids=("A16",),
            )
            audit = root / "audit"
            receipt = seal_static_loader_audit(output, audit)
            self.assertFalse(receipt["source_bundle_modified"])
            self.assertGreater(receipt["source_file_count"], 0)
            self.assertEqual(len(receipt["source_tree_sha256"]), 64)
            self.assertTrue((audit / "static-loader-audit-receipt.json").is_file())


if __name__ == "__main__":
    unittest.main()
