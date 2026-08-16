"""Offline regressions for the VMS-41R1 structured file-effect auditor."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from system.solve_vein_analysis.file_effect_audit import (
    EventObservability,
    FileEffectAuditError,
    FileEffectPolicy,
    FileEffectVerdict,
    FileOperation,
    PathScope,
    audit_file_effects,
    classify_observed_path,
    inventory_workspace,
    parse_file_operation_event,
    parse_file_operation_events_jsonl,
)


EVIDENCE_SHA = hashlib.sha256(b"provider-file-event-ledger").hexdigest()


def event_value(
    event_id: str,
    operation: str,
    observed_path: str,
) -> dict[str, str]:
    return {
        "schema_version": "solve-vein/file-operation-event/v1",
        "event_id": event_id,
        "operation": operation,
        "observed_path": observed_path,
        "provider_event_ref": f"fixture://events/{event_id}",
        "provider_event_sha256": hashlib.sha256(event_id.encode()).hexdigest(),
    }


def policy() -> FileEffectPolicy:
    return FileEffectPolicy.create(
        policy_id="v41r1-candidate-only",
        allowed_created_paths=("candidate.json",),
        allowed_operation_paths={
            FileOperation.CREATE: ("candidate.json",),
            FileOperation.WRITE: ("candidate.json",),
        },
    )


class FileEffectAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "workspace"
        self.root.mkdir()

    def snapshot(self, suffix: str):
        return inventory_workspace(
            self.root,
            inventory_id=f"inventory-{suffix}",
            workspace_id="workspace-v41r1",
        )

    def parse(self, value: dict[str, str]):
        return parse_file_operation_event(value, workspace_root=self.root)

    def audit(self, before, after, events, observability="complete"):
        return audit_file_effects(
            before=before,
            after=after,
            events=events,
            event_observability=observability,
            observability_evidence_ref="fixture://provider-event-ledger",
            observability_evidence_sha256=EVIDENCE_SHA,
            policy=policy(),
        )

    def test_allowed_candidate_creation_with_complete_event_passes(self) -> None:
        before = self.snapshot("before")
        (self.root / "candidate.json").write_text("{}")
        after = self.snapshot("after")
        event = self.parse(event_value("event-1", "create", "candidate.json"))
        result = self.audit(before, after, [event])
        self.assertEqual(result.verdict, FileEffectVerdict.PASS)
        self.assertEqual(result.created, ("candidate.json",))
        self.assertEqual(result.unexplained_residual_changes, ())

    def test_transient_helper_create_delete_fails_with_equal_inventories(self) -> None:
        before = self.snapshot("before")
        after = self.snapshot("after")
        events = [
            self.parse(event_value("event-1", "create", "helper.py")),
            self.parse(event_value("event-2", "delete", "helper.py")),
        ]
        result = self.audit(before, after, events)
        self.assertEqual(result.verdict, FileEffectVerdict.FAIL)
        self.assertEqual(result.transient_event_paths, ("helper.py",))
        self.assertIn(
            "FILE_OPERATION_NOT_ALLOWED", {error["code"] for error in result.errors}
        )

    def test_outside_workspace_event_fails(self) -> None:
        before = self.snapshot("before")
        after = self.snapshot("after")
        event = self.parse(event_value("event-1", "write", "/tmp/helper.py"))
        self.assertEqual(event.path_scope, PathScope.OUTSIDE_WORKSPACE)
        result = self.audit(before, after, [event])
        self.assertEqual(result.verdict, FileEffectVerdict.FAIL)
        self.assertIn(
            "FILE_EVENT_OUTSIDE_WORKSPACE",
            {error["code"] for error in result.errors},
        )

    def test_parent_traversal_is_structurally_outside(self) -> None:
        normalized, scope = classify_observed_path(
            "../escape.py", workspace_root=self.root
        )
        self.assertEqual(scope, PathScope.OUTSIDE_WORKSPACE)
        self.assertTrue(normalized.endswith("escape.py"))

    def test_complete_event_stream_cannot_omit_residual_change(self) -> None:
        before = self.snapshot("before")
        (self.root / "candidate.json").write_text("{}")
        after = self.snapshot("after")
        result = self.audit(before, after, [])
        self.assertEqual(result.verdict, FileEffectVerdict.FAIL)
        self.assertEqual(result.unexplained_residual_changes, ("candidate.json",))
        self.assertIn(
            "UNEXPLAINED_RESIDUAL_CHANGE",
            {error["code"] for error in result.errors},
        )

    def test_partial_observability_never_passes(self) -> None:
        before = self.snapshot("before")
        after = self.snapshot("after")
        result = self.audit(before, after, [], observability="partial")
        self.assertEqual(result.verdict, FileEffectVerdict.PARTIAL_OBSERVABILITY)

    def test_unknown_observability_is_inconclusive(self) -> None:
        before = self.snapshot("before")
        after = self.snapshot("after")
        result = self.audit(before, after, [], observability="unknown")
        self.assertEqual(result.verdict, FileEffectVerdict.INCONCLUSIVE_PROTOCOL)

    def test_symlink_is_recorded_without_following_and_fails(self) -> None:
        outside = Path(self.temporary.name) / "outside.txt"
        outside.write_text("secret")
        (self.root / "link").symlink_to(outside)
        before = self.snapshot("before")
        after = self.snapshot("after")
        result = self.audit(before, after, [])
        self.assertEqual(result.verdict, FileEffectVerdict.FAIL)
        self.assertEqual(result.symlink_paths, ("link",))
        entry = next(item for item in before.entries if item.relative_path == "link")
        self.assertEqual(entry.entry_type.value, "symlink")
        self.assertIsNone(entry.sha256)

    def test_new_symlink_fails_even_if_preexisting_symlinks_are_allowed(self) -> None:
        before = self.snapshot("before")
        outside = Path(self.temporary.name) / "outside.txt"
        outside.write_text("secret")
        (self.root / "candidate.json").symlink_to(outside)
        after = self.snapshot("after")
        permissive_for_old_only = FileEffectPolicy.create(
            policy_id="old-links-only",
            allowed_created_paths=("candidate.json",),
            allowed_operation_paths={FileOperation.SYMLINK: ("candidate.json",)},
            allow_preexisting_symlinks=True,
        )
        event = self.parse(event_value("event-1", "symlink", "candidate.json"))
        result = audit_file_effects(
            before=before,
            after=after,
            events=[event],
            event_observability=EventObservability.COMPLETE,
            observability_evidence_ref="fixture://provider-event-ledger",
            observability_evidence_sha256=EVIDENCE_SHA,
            policy=permissive_for_old_only,
        )
        self.assertEqual(result.verdict, FileEffectVerdict.FAIL)
        self.assertIn(
            "NEW_SYMLINK_FORBIDDEN", {item["code"] for item in result.errors}
        )

    def test_wrong_event_operation_does_not_explain_created_file(self) -> None:
        before = self.snapshot("before")
        (self.root / "candidate.json").write_text("{}")
        after = self.snapshot("after")
        misleading_policy = FileEffectPolicy.create(
            policy_id="misleading-operation",
            allowed_created_paths=("candidate.json",),
            allowed_operation_paths={FileOperation.CHMOD: ("candidate.json",)},
        )
        event = self.parse(event_value("event-1", "chmod", "candidate.json"))
        result = audit_file_effects(
            before=before,
            after=after,
            events=[event],
            event_observability="complete",
            observability_evidence_ref="fixture://provider-event-ledger",
            observability_evidence_sha256=EVIDENCE_SHA,
            policy=misleading_policy,
        )
        self.assertEqual(result.verdict, FileEffectVerdict.FAIL)
        self.assertEqual(result.unexplained_residual_changes, ("candidate.json",))

    def test_root_symlink_is_rejected(self) -> None:
        real = Path(self.temporary.name) / "real"
        real.mkdir()
        alias = Path(self.temporary.name) / "alias"
        alias.symlink_to(real, target_is_directory=True)
        with self.assertRaises(FileEffectAuditError) as caught:
            inventory_workspace(alias, inventory_id="inventory-link", workspace_id="ws")
        self.assertEqual(caught.exception.code, "WORKSPACE_ROOT_SYMLINK")

    def test_unknown_event_field_is_rejected(self) -> None:
        value = event_value("event-1", "create", "candidate.json")
        value["self_verdict"] = "PASS"
        with self.assertRaises(FileEffectAuditError) as caught:
            self.parse(value)
        self.assertEqual(caught.exception.code, "OBJECT_KEYS_INVALID")

    def test_duplicate_event_ids_are_rejected(self) -> None:
        before = self.snapshot("before")
        after = self.snapshot("after")
        one = self.parse(event_value("event-1", "create", "candidate.json"))
        with self.assertRaises(FileEffectAuditError) as caught:
            self.audit(before, after, [one, one])
        self.assertEqual(caught.exception.code, "FILE_EVENT_ID_DUPLICATE")

    def test_jsonl_blank_line_and_nonfinite_values_fail_closed(self) -> None:
        valid = json.dumps(event_value("event-1", "create", "candidate.json"))
        with self.assertRaises(FileEffectAuditError) as blank:
            parse_file_operation_events_jsonl(
                valid + "\n\n", workspace_root=self.root
            )
        self.assertEqual(blank.exception.code, "FILE_EVENT_JSONL_BLANK_LINE")
        invalid = valid.replace('"event_id": "event-1"', '"event_id": NaN')
        with self.assertRaises(FileEffectAuditError) as nonfinite:
            parse_file_operation_events_jsonl(invalid, workspace_root=self.root)
        self.assertEqual(nonfinite.exception.code, "JSON_NONFINITE_NUMBER")

    def test_math_text_with_slashes_is_not_a_path_event(self) -> None:
        before = self.snapshot("before")
        after = self.snapshot("after")
        mathematical_output = "Use x/2 and /liminf in the proof."
        self.assertIn("/", mathematical_output)
        result = self.audit(before, after, [])
        self.assertEqual(result.verdict, FileEffectVerdict.PASS)


if __name__ == "__main__":
    unittest.main()
