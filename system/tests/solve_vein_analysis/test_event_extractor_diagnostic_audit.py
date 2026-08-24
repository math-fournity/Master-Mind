from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch

from system.tests.solve_vein_analysis import seal_event_extractor_diagnostic_audit as audit


class EventExtractorDiagnosticAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.review = json.loads(audit.DEFAULT_REVIEW.read_text())
        self.binding = {
            "schema_version": "solve-vein/vms41-posthoc-source-binding/v1",
            "source_poc_id": "POC-VMS-41",
            "source_run_id": "poc-vms-41-event-extractor-qualification-20260814",
            "source_bundle": "/frozen/live/bundle",
            "source_final_receipt_file_sha256": self.review[
                "source_final_receipt_file_sha256"
            ],
            "source_artifact_tree_sha256": self.review[
                "source_artifact_tree_sha256"
            ],
            "freeze_manifest_sha256": "a" * 64,
            "cases": [
                {
                    "case_id": case["case_id"],
                    "attempt_id": case["attempt_id"],
                    "candidate_sha256": "b" * 64,
                    "export_sha256": "c" * 64,
                    "invocation_receipt_sha256": "d" * 64,
                    "evaluation_sha256": "e" * 64,
                }
                for case in self.review["case_audits"]
            ],
        }
        self.replay = {
            "schema_version": "solve-vein/vms41-historical-membership-replay/v1",
            "replay_policy": (
                "VERIFY_EVERY_FROZEN_MEMBER_IGNORE_DECLARED_POSTFREEZE_ADDITIONS"
            ),
            "artifact_integrity": "PASS",
            "mechanical_replay": "PASS",
            "live_attempt_status": "INCONCLUSIVE_PROTOCOL",
            "manual_semantic_audit": "PENDING",
            "component_qualification": "NOT_YET_DECIDABLE",
            "postfreeze_source_additions": [],
            "errors": [],
        }

    def _write_review(self, root: Path, review: dict | None = None) -> Path:
        path = root / "review.json"
        path.write_text(json.dumps(review or self.review, ensure_ascii=False))
        return path

    def _seal(self, root: Path, review: dict | None = None) -> tuple[Path, dict]:
        final = root / "audit-final"
        partial = root / ".audit-final.partial"
        review_path = self._write_review(root, review)
        with patch.object(
            audit,
            "_build_source_binding",
            return_value=(deepcopy(self.binding), deepcopy(self.replay)),
        ):
            result = audit.seal_diagnostic_audit(
                review_path=review_path,
                live_bundle=root / "unused-live",
                freeze_path=root / "unused-freeze",
                final_root=final,
                partial_root=partial,
            )
        return final, result

    def test_repository_review_is_strict_and_nonconfirmatory(self) -> None:
        validated = audit.validate_manual_review(deepcopy(self.review))
        self.assertFalse(validated["confirmation_eligible"])
        self.assertEqual(validated["component_qualification"], "NOT_QUALIFIED")
        self.assertEqual(len(validated["case_audits"]), 4)

    def test_historical_freeze_checks_members_without_rejecting_postfreeze_test(self) -> None:
        frozen = audit._validate_historical_freeze(audit.DEFAULT_FREEZE)
        self.assertEqual(len(frozen["frozen_files"]), 90)
        current = {
            path.relative_to(audit.REPO_ROOT).as_posix()
            for path in audit.qualification_test_source_files()
        }
        historical = {
            row["path"] for row in audit._historical_test_source_rows(frozen)
        }
        self.assertIn(
            "system/tests/solve_vein_analysis/test_event_extractor_diagnostic_audit.py",
            current - historical,
        )
        self.assertEqual(historical - current, set())

    def test_historical_git_fallback_rejects_wrong_blob(self) -> None:
        freeze = json.loads(audit.DEFAULT_FREEZE.read_text())
        binding = next(
            row
            for row in freeze["frozen_files"]
            if row["path"]
            == "system/tests/solve_vein_analysis/test_pipeline.ai-check"
        )
        with patch.object(audit, "_historical_git_blob", return_value=b"wrong"):
            with self.assertRaises(audit.DiagnosticAuditError):
                audit._validate_current_or_historical_binding(
                    binding["path"],
                    binding["sha256"],
                    "negative fallback test",
                )

    def test_review_cannot_restore_blindness_or_qualification(self) -> None:
        for field, bad_value in (
            ("blindness", "BLIND"),
            ("purpose", "CONFIRMATORY"),
            ("confirmation_eligible", True),
            ("component_qualification", "PASS"),
        ):
            with self.subTest(field=field):
                changed = deepcopy(self.review)
                changed[field] = bad_value
                with self.assertRaises(audit.DiagnosticAuditError):
                    audit.validate_manual_review(changed)

    def test_review_requires_exact_frozen_case_set_and_order(self) -> None:
        changed = deepcopy(self.review)
        changed["case_audits"][1]["case_id"] = changed["case_audits"][0]["case_id"]
        with self.assertRaises(audit.DiagnosticAuditError):
            audit.validate_manual_review(changed)

    def test_seal_verify_and_idempotent_reopen(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            final, result = self._seal(root)
            self.assertEqual(result["artifact_integrity"], "PASS")
            self.assertEqual(result["commit_status"], "COMMITTED")
            self.assertEqual(stat.S_IMODE(final.stat().st_mode), 0o700)
            self.assertEqual(
                {path.name for path in final.iterdir()},
                {
                    "source-binding.json",
                    "verifier-replay.json",
                    "manual-diagnostic.json",
                    "diagnostic-summary.json",
                    "final-receipt.json",
                    "COMMITTED",
                },
            )
            with patch.object(
                audit,
                "_build_source_binding",
                return_value=(deepcopy(self.binding), deepcopy(self.replay)),
            ):
                reopened = audit.seal_diagnostic_audit(
                    review_path=root / "review.json",
                    live_bundle=root / "unused-live",
                    freeze_path=root / "unused-freeze",
                    final_root=final,
                    partial_root=root / ".audit-final.partial",
                )
            self.assertEqual(reopened["commit_status"], "ALREADY_COMMITTED")

    def test_tampered_sealed_review_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            final, _ = self._seal(root)
            review_path = final / "manual-diagnostic.json"
            changed = json.loads(review_path.read_text())
            changed["case_audits"][0]["notes"] = "tampered"
            review_path.write_text(json.dumps(changed))
            with patch.object(
                audit,
                "_build_source_binding",
                return_value=(deepcopy(self.binding), deepcopy(self.replay)),
            ):
                result = audit.verify_diagnostic_audit(
                    audit_root=final,
                    live_bundle=root / "unused-live",
                    freeze_path=root / "unused-freeze",
                )
            self.assertEqual(result["artifact_integrity"], "FAIL")
            self.assertTrue(result["errors"])

    def test_symlink_artifact_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            final, _ = self._seal(root)
            target = root / "outside.json"
            target.write_text("{}")
            path = final / "diagnostic-summary.json"
            path.unlink()
            path.symlink_to(target)
            with patch.object(
                audit,
                "_build_source_binding",
                return_value=(deepcopy(self.binding), deepcopy(self.replay)),
            ):
                result = audit.verify_diagnostic_audit(
                    audit_root=final,
                    live_bundle=root / "unused-live",
                    freeze_path=root / "unused-freeze",
                )
            self.assertEqual(result["artifact_integrity"], "FAIL")
            self.assertIn("audit contains a symlink", result["errors"])

    def test_source_receipt_binding_mismatch_refuses_seal(self) -> None:
        changed = deepcopy(self.review)
        changed["source_final_receipt_file_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            review_path = self._write_review(root, changed)
            with patch.object(
                audit,
                "_build_source_binding",
                return_value=(deepcopy(self.binding), deepcopy(self.replay)),
            ):
                with self.assertRaises(audit.DiagnosticAuditError):
                    audit.seal_diagnostic_audit(
                        review_path=review_path,
                        live_bundle=root / "unused-live",
                        freeze_path=root / "unused-freeze",
                        final_root=root / "final",
                        partial_root=root / ".partial",
                    )

    def test_existing_partial_is_never_deleted_or_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            partial = root / ".partial"
            partial.mkdir()
            sentinel = partial / "evidence.txt"
            sentinel.write_text("preserve me")
            review_path = self._write_review(root)
            with patch.object(
                audit,
                "_build_source_binding",
                return_value=(deepcopy(self.binding), deepcopy(self.replay)),
            ):
                with self.assertRaises(audit.DiagnosticAuditError):
                    audit.seal_diagnostic_audit(
                        review_path=review_path,
                        live_bundle=root / "unused-live",
                        freeze_path=root / "unused-freeze",
                        final_root=root / "final",
                        partial_root=partial,
                    )
            self.assertEqual(sentinel.read_text(), "preserve me")


if __name__ == "__main__":
    unittest.main()
