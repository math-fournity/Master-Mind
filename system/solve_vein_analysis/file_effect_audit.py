"""Structured file-effect audit for solve-side cognitive-worker attempts.

Pre/post inventories prove residual state changes.  Provider file-operation
events prove transient actions such as create-then-delete and attempts outside
the workspace.  Neither evidence plane substitutes for the other: incomplete
event observability can never yield PASS even when the two inventories match.

The module is read-only.  It never creates, modifies, deletes, renames or
chmods a filesystem object and performs no model, Solver, database or network
operation.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
from typing import Any, Iterable, Mapping, Sequence

from .models import canonical_json_bytes


INVENTORY_SCHEMA_VERSION = "solve-vein/workspace-inventory/v1"
FILE_EVENT_SCHEMA_VERSION = "solve-vein/file-operation-event/v1"
FILE_EFFECT_SCHEMA_VERSION = "solve-vein/file-effect-evaluation/v1"
IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class FileEffectAuditError(ValueError):
    """Fail-closed inventory, event or policy validation error."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


class EntryType(StrEnum):
    REGULAR_FILE = "regular_file"
    DIRECTORY = "directory"
    SYMLINK = "symlink"
    OTHER = "other"


class FileOperation(StrEnum):
    CREATE = "create"
    WRITE = "write"
    APPEND = "append"
    RENAME = "rename"
    DELETE = "delete"
    CHMOD = "chmod"
    SYMLINK = "symlink"
    OTHER = "other"


class PathScope(StrEnum):
    WORKSPACE = "workspace"
    APPROVED_OUTPUT = "approved_output"
    OUTSIDE_WORKSPACE = "outside_workspace"
    UNKNOWN = "unknown"


class EventObservability(StrEnum):
    COMPLETE = "complete"
    PARTIAL = "partial"
    UNKNOWN = "unknown"


class FileEffectVerdict(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    PARTIAL_OBSERVABILITY = "PARTIAL_OBSERVABILITY"
    INCONCLUSIVE_PROTOCOL = "INCONCLUSIVE_PROTOCOL"
    INVALID = "INVALID"


@dataclass(frozen=True, slots=True)
class FileEntry:
    relative_path: str
    entry_type: EntryType
    size: int
    mode: int
    sha256: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "relative_path": self.relative_path,
            "entry_type": self.entry_type.value,
            "size": self.size,
            "mode": self.mode,
            "sha256": self.sha256,
        }


@dataclass(frozen=True, slots=True)
class WorkspaceInventory:
    inventory_id: str
    workspace_id: str
    entries: tuple[FileEntry, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": INVENTORY_SCHEMA_VERSION,
            "inventory_id": self.inventory_id,
            "workspace_id": self.workspace_id,
            "entries": [entry.to_dict() for entry in self.entries],
        }

    @property
    def canonical_sha256(self) -> str:
        return hashlib.sha256(canonical_json_bytes(self.to_dict())).hexdigest()


@dataclass(frozen=True, slots=True)
class FileOperationEvent:
    event_id: str
    operation: FileOperation
    observed_path: str
    normalized_path: str | None
    path_scope: PathScope
    provider_event_ref: str
    provider_event_sha256: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": FILE_EVENT_SCHEMA_VERSION,
            "event_id": self.event_id,
            "operation": self.operation.value,
            "observed_path": self.observed_path,
            "normalized_path": self.normalized_path,
            "path_scope": self.path_scope.value,
            "provider_event_ref": self.provider_event_ref,
            "provider_event_sha256": self.provider_event_sha256,
        }


@dataclass(frozen=True, slots=True)
class FileEffectPolicy:
    policy_id: str
    allowed_created_paths: tuple[str, ...]
    allowed_modified_paths: tuple[str, ...]
    allowed_deleted_paths: tuple[str, ...]
    allowed_operation_paths: Mapping[FileOperation, tuple[str, ...]]
    allow_preexisting_symlinks: bool = False

    @classmethod
    def create(
        cls,
        *,
        policy_id: str,
        allowed_created_paths: Sequence[str] = (),
        allowed_modified_paths: Sequence[str] = (),
        allowed_deleted_paths: Sequence[str] = (),
        allowed_operation_paths: Mapping[FileOperation | str, Sequence[str]] | None = None,
        allow_preexisting_symlinks: bool = False,
    ) -> "FileEffectPolicy":
        operation_paths: dict[FileOperation, tuple[str, ...]] = {}
        for raw_operation, paths in (allowed_operation_paths or {}).items():
            try:
                operation = (
                    raw_operation
                    if isinstance(raw_operation, FileOperation)
                    else FileOperation(raw_operation)
                )
            except ValueError as exc:
                raise FileEffectAuditError(
                    "POLICY_OPERATION_INVALID", repr(raw_operation)
                ) from exc
            operation_paths[operation] = _normalized_relative_paths(
                paths, f"allowed_operation_paths.{operation.value}"
            )
        return cls(
            policy_id=_identifier(policy_id, "policy_id"),
            allowed_created_paths=_normalized_relative_paths(
                allowed_created_paths, "allowed_created_paths"
            ),
            allowed_modified_paths=_normalized_relative_paths(
                allowed_modified_paths, "allowed_modified_paths"
            ),
            allowed_deleted_paths=_normalized_relative_paths(
                allowed_deleted_paths, "allowed_deleted_paths"
            ),
            allowed_operation_paths=dict(sorted(operation_paths.items())),
            allow_preexisting_symlinks=_boolean(
                allow_preexisting_symlinks, "allow_preexisting_symlinks"
            ),
        )


@dataclass(frozen=True, slots=True)
class FileEffectEvaluation:
    policy_id: str
    before_inventory_sha256: str
    after_inventory_sha256: str
    event_observability: EventObservability
    observability_evidence_ref: str
    observability_evidence_sha256: str
    created: tuple[str, ...]
    modified: tuple[str, ...]
    deleted: tuple[str, ...]
    type_changed: tuple[str, ...]
    symlink_paths: tuple[str, ...]
    event_count: int
    transient_event_paths: tuple[str, ...]
    unexplained_residual_changes: tuple[str, ...]
    verdict: FileEffectVerdict
    errors: tuple[Mapping[str, str], ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": FILE_EFFECT_SCHEMA_VERSION,
            "policy_id": self.policy_id,
            "before_inventory_sha256": self.before_inventory_sha256,
            "after_inventory_sha256": self.after_inventory_sha256,
            "event_observability": self.event_observability.value,
            "observability_evidence_ref": self.observability_evidence_ref,
            "observability_evidence_sha256": self.observability_evidence_sha256,
            "created": list(self.created),
            "modified": list(self.modified),
            "deleted": list(self.deleted),
            "type_changed": list(self.type_changed),
            "symlink_paths": list(self.symlink_paths),
            "event_count": self.event_count,
            "transient_event_paths": list(self.transient_event_paths),
            "unexplained_residual_changes": list(self.unexplained_residual_changes),
            "verdict": self.verdict.value,
            "errors": list(self.errors),
        }


def inventory_workspace(
    workspace_root: Path,
    *,
    inventory_id: str,
    workspace_id: str,
) -> WorkspaceInventory:
    """Read a deterministic, no-follow inventory of a workspace."""

    root = Path(workspace_root)
    try:
        root_stat = root.lstat()
    except OSError as exc:
        raise FileEffectAuditError("WORKSPACE_ROOT_UNREADABLE", str(exc)) from exc
    if stat.S_ISLNK(root_stat.st_mode):
        raise FileEffectAuditError("WORKSPACE_ROOT_SYMLINK", str(root))
    if not stat.S_ISDIR(root_stat.st_mode):
        raise FileEffectAuditError("WORKSPACE_ROOT_NOT_DIRECTORY", str(root))

    entries: list[FileEntry] = []

    def walk(directory: Path, relative_prefix: PurePosixPath) -> None:
        try:
            children = sorted(os.scandir(directory), key=lambda item: item.name)
        except OSError as exc:
            raise FileEffectAuditError("WORKSPACE_DIRECTORY_UNREADABLE", str(exc)) from exc
        for child in children:
            relative = relative_prefix / child.name
            relative_text = relative.as_posix()
            try:
                metadata = child.stat(follow_symlinks=False)
            except OSError as exc:
                raise FileEffectAuditError("WORKSPACE_ENTRY_UNREADABLE", str(exc)) from exc
            file_mode = stat.S_IMODE(metadata.st_mode)
            if stat.S_ISLNK(metadata.st_mode):
                entry_type = EntryType.SYMLINK
                digest = None
            elif stat.S_ISDIR(metadata.st_mode):
                entry_type = EntryType.DIRECTORY
                digest = None
            elif stat.S_ISREG(metadata.st_mode):
                entry_type = EntryType.REGULAR_FILE
                try:
                    digest = _sha256_file(Path(child.path))
                except OSError as exc:
                    raise FileEffectAuditError(
                        "WORKSPACE_FILE_UNREADABLE", str(exc)
                    ) from exc
            else:
                entry_type = EntryType.OTHER
                digest = None
            entries.append(
                FileEntry(
                    relative_path=relative_text,
                    entry_type=entry_type,
                    size=metadata.st_size,
                    mode=file_mode,
                    sha256=digest,
                )
            )
            if entry_type is EntryType.DIRECTORY:
                walk(Path(child.path), relative)

    walk(root, PurePosixPath())
    return WorkspaceInventory(
        inventory_id=_identifier(inventory_id, "inventory_id"),
        workspace_id=_identifier(workspace_id, "workspace_id"),
        entries=tuple(entries),
    )


def parse_file_operation_event(
    value: Mapping[str, Any],
    *,
    workspace_root: Path,
    approved_output_roots: Sequence[Path] = (),
) -> FileOperationEvent:
    item = _mapping(value, "file_operation_event")
    _exact_keys(
        item,
        {
            "schema_version",
            "event_id",
            "operation",
            "observed_path",
            "provider_event_ref",
            "provider_event_sha256",
        },
        "file_operation_event",
    )
    if _string(item["schema_version"], "schema_version") != FILE_EVENT_SCHEMA_VERSION:
        raise FileEffectAuditError(
            "FILE_EVENT_SCHEMA_UNSUPPORTED", repr(item["schema_version"])
        )
    operation = _enum(FileOperation, item["operation"], "operation")
    observed_path = _nonempty_string(item["observed_path"], "observed_path")
    normalized, scope = classify_observed_path(
        observed_path,
        workspace_root=workspace_root,
        approved_output_roots=approved_output_roots,
    )
    return FileOperationEvent(
        event_id=_identifier(item["event_id"], "event_id"),
        operation=operation,
        observed_path=observed_path,
        normalized_path=normalized,
        path_scope=scope,
        provider_event_ref=_nonempty_string(
            item["provider_event_ref"], "provider_event_ref"
        ),
        provider_event_sha256=_sha256(
            item["provider_event_sha256"], "provider_event_sha256"
        ),
    )


def classify_observed_path(
    observed_path: str,
    *,
    workspace_root: Path,
    approved_output_roots: Sequence[Path] = (),
) -> tuple[str | None, PathScope]:
    """Classify an actual path structurally; never inspect arbitrary command text."""

    if "\x00" in observed_path:
        return None, PathScope.UNKNOWN
    workspace = Path(workspace_root).resolve(strict=False)
    raw = Path(observed_path)
    candidate = raw if raw.is_absolute() else workspace / raw
    try:
        resolved = candidate.resolve(strict=False)
    except (OSError, RuntimeError):
        return None, PathScope.UNKNOWN
    try:
        relative = resolved.relative_to(workspace)
    except ValueError:
        for approved_root in approved_output_roots:
            approved = Path(approved_root).resolve(strict=False)
            try:
                approved_relative = resolved.relative_to(approved)
            except ValueError:
                continue
            return approved_relative.as_posix() or ".", PathScope.APPROVED_OUTPUT
        return str(resolved), PathScope.OUTSIDE_WORKSPACE
    return relative.as_posix() or ".", PathScope.WORKSPACE


def audit_file_effects(
    *,
    before: WorkspaceInventory,
    after: WorkspaceInventory,
    events: Sequence[FileOperationEvent],
    event_observability: EventObservability | str,
    observability_evidence_ref: str,
    observability_evidence_sha256: str,
    policy: FileEffectPolicy,
) -> FileEffectEvaluation:
    """Reconcile residual inventory changes with structured provider events."""

    if before.workspace_id != after.workspace_id:
        raise FileEffectAuditError(
            "WORKSPACE_ID_MISMATCH",
            f"{before.workspace_id!r} != {after.workspace_id!r}",
        )
    observability = (
        event_observability
        if isinstance(event_observability, EventObservability)
        else _enum(EventObservability, event_observability, "event_observability")
    )
    evidence_ref = _nonempty_string(
        observability_evidence_ref, "observability_evidence_ref"
    )
    evidence_sha = _sha256(
        observability_evidence_sha256, "observability_evidence_sha256"
    )
    event_ids = [event.event_id for event in events]
    if len(event_ids) != len(set(event_ids)):
        raise FileEffectAuditError("FILE_EVENT_ID_DUPLICATE", repr(event_ids))

    before_by_path = {entry.relative_path: entry for entry in before.entries}
    after_by_path = {entry.relative_path: entry for entry in after.entries}
    before_paths = set(before_by_path)
    after_paths = set(after_by_path)
    created = tuple(sorted(after_paths - before_paths))
    deleted = tuple(sorted(before_paths - after_paths))
    type_changed: list[str] = []
    modified: list[str] = []
    for path in sorted(before_paths & after_paths):
        old = before_by_path[path]
        new = after_by_path[path]
        if old.entry_type is not new.entry_type:
            type_changed.append(path)
        elif (old.size, old.mode, old.sha256) != (new.size, new.mode, new.sha256):
            modified.append(path)

    before_symlinks = {
        entry.relative_path
        for entry in before.entries
        if entry.entry_type is EntryType.SYMLINK
    }
    after_symlinks = {
        entry.relative_path
        for entry in after.entries
        if entry.entry_type is EntryType.SYMLINK
    }
    symlinks = tuple(sorted(before_symlinks | after_symlinks))
    errors: list[dict[str, str]] = []
    new_symlinks = tuple(sorted(after_symlinks - before_symlinks))
    if new_symlinks:
        errors.append(_error("NEW_SYMLINK_FORBIDDEN", repr(new_symlinks)))
    unchanged_preexisting_symlinks = before_symlinks & after_symlinks
    if unchanged_preexisting_symlinks and not policy.allow_preexisting_symlinks:
        errors.append(
            _error(
                "PREEXISTING_SYMLINK_FORBIDDEN",
                repr(sorted(unchanged_preexisting_symlinks)),
            )
        )
    removed_symlinks = before_symlinks - after_symlinks
    if removed_symlinks:
        errors.append(
            _error("REMOVED_SYMLINK_FORBIDDEN", repr(sorted(removed_symlinks)))
        )

    _check_residual_paths(
        created,
        set(policy.allowed_created_paths),
        "CREATED_PATH_NOT_ALLOWED",
        errors,
    )
    _check_residual_paths(
        modified,
        set(policy.allowed_modified_paths),
        "MODIFIED_PATH_NOT_ALLOWED",
        errors,
    )
    _check_residual_paths(
        deleted,
        set(policy.allowed_deleted_paths),
        "DELETED_PATH_NOT_ALLOWED",
        errors,
    )
    for path in type_changed:
        errors.append(_error("TYPE_CHANGE_NOT_ALLOWED", path))

    operations_by_path: dict[str, set[FileOperation]] = {}
    transient_paths: set[str] = set()
    for event in events:
        if event.path_scope is PathScope.UNKNOWN:
            errors.append(_error("FILE_EVENT_PATH_UNKNOWN", event.event_id))
            continue
        if event.path_scope is PathScope.OUTSIDE_WORKSPACE:
            errors.append(
                _error(
                    "FILE_EVENT_OUTSIDE_WORKSPACE",
                    f"{event.event_id}:{event.observed_path}",
                )
            )
            continue
        if event.path_scope is PathScope.APPROVED_OUTPUT:
            errors.append(
                _error(
                    "MODEL_EVENT_IN_APPROVED_OUTPUT_ROOT",
                    f"{event.event_id}:{event.observed_path}",
                )
            )
            continue
        assert event.normalized_path is not None
        normalized = event.normalized_path
        operations_by_path.setdefault(normalized, set()).add(event.operation)
        allowed = set(policy.allowed_operation_paths.get(event.operation, ()))
        if normalized not in allowed:
            errors.append(
                _error(
                    "FILE_OPERATION_NOT_ALLOWED",
                    f"{event.operation.value}:{normalized}",
                )
            )
        if normalized not in before_paths and normalized not in after_paths:
            transient_paths.add(normalized)

    expected_operations: dict[str, set[FileOperation]] = {}
    for path in created:
        expected_operations[path] = {
            FileOperation.CREATE,
            FileOperation.WRITE,
            FileOperation.APPEND,
            FileOperation.RENAME,
            FileOperation.SYMLINK,
        }
    for path in modified:
        expected_operations[path] = {
            FileOperation.WRITE,
            FileOperation.APPEND,
            FileOperation.CHMOD,
            FileOperation.RENAME,
        }
    for path in deleted:
        expected_operations[path] = {FileOperation.DELETE, FileOperation.RENAME}
    for path in type_changed:
        expected_operations[path] = {
            FileOperation.CREATE,
            FileOperation.WRITE,
            FileOperation.RENAME,
            FileOperation.DELETE,
            FileOperation.SYMLINK,
        }
    unexplained = tuple(
        sorted(
            path
            for path, compatible in expected_operations.items()
            if not (operations_by_path.get(path, set()) & compatible)
        )
    )
    if observability is EventObservability.COMPLETE:
        for path in unexplained:
            errors.append(_error("UNEXPLAINED_RESIDUAL_CHANGE", path))

    if errors:
        verdict = FileEffectVerdict.FAIL
    elif observability is EventObservability.COMPLETE:
        verdict = FileEffectVerdict.PASS
    elif observability is EventObservability.PARTIAL:
        verdict = FileEffectVerdict.PARTIAL_OBSERVABILITY
    else:
        verdict = FileEffectVerdict.INCONCLUSIVE_PROTOCOL

    return FileEffectEvaluation(
        policy_id=policy.policy_id,
        before_inventory_sha256=before.canonical_sha256,
        after_inventory_sha256=after.canonical_sha256,
        event_observability=observability,
        observability_evidence_ref=evidence_ref,
        observability_evidence_sha256=evidence_sha,
        created=created,
        modified=tuple(modified),
        deleted=deleted,
        type_changed=tuple(type_changed),
        symlink_paths=symlinks,
        event_count=len(events),
        transient_event_paths=tuple(sorted(transient_paths)),
        unexplained_residual_changes=unexplained,
        verdict=verdict,
        errors=tuple(errors),
    )


def parse_file_operation_events_jsonl(
    text: str,
    *,
    workspace_root: Path,
    approved_output_roots: Sequence[Path] = (),
) -> tuple[FileOperationEvent, ...]:
    events: list[FileOperationEvent] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        if not raw_line.strip():
            raise FileEffectAuditError(
                "FILE_EVENT_JSONL_BLANK_LINE", str(line_number)
            )
        try:
            value = json.loads(raw_line, parse_constant=_reject_nonfinite_json)
        except json.JSONDecodeError as exc:
            raise FileEffectAuditError(
                "FILE_EVENT_JSON_INVALID", f"line {line_number}: {exc}"
            ) from exc
        events.append(
            parse_file_operation_event(
                value,
                workspace_root=workspace_root,
                approved_output_roots=approved_output_roots,
            )
        )
    return tuple(events)


def _check_residual_paths(
    observed: Iterable[str],
    allowed: set[str],
    code: str,
    errors: list[dict[str, str]],
) -> None:
    for path in observed:
        if path not in allowed:
            errors.append(_error(code, path))


def _normalized_relative_paths(values: Sequence[str], path: str) -> tuple[str, ...]:
    normalized: list[str] = []
    for index, value in enumerate(values):
        raw = _nonempty_string(value, f"{path}[{index}]")
        pure = PurePosixPath(raw)
        if pure.is_absolute() or raw == "." or ".." in pure.parts:
            raise FileEffectAuditError(
                "POLICY_RELATIVE_PATH_INVALID", f"{path}[{index}]: {raw!r}"
            )
        canonical = pure.as_posix()
        if canonical != raw:
            raise FileEffectAuditError(
                "POLICY_RELATIVE_PATH_NONCANONICAL", f"{path}[{index}]: {raw!r}"
            )
        normalized.append(canonical)
    if len(normalized) != len(set(normalized)):
        raise FileEffectAuditError("POLICY_PATH_DUPLICATE", path)
    return tuple(sorted(normalized))


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _mapping(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise FileEffectAuditError("TYPE_OBJECT_REQUIRED", path)
    if not all(isinstance(key, str) for key in value):
        raise FileEffectAuditError("OBJECT_KEY_TYPE_INVALID", path)
    return value


def _exact_keys(value: Mapping[str, Any], expected: set[str], path: str) -> None:
    actual = set(value)
    if actual != expected:
        raise FileEffectAuditError(
            "OBJECT_KEYS_INVALID",
            f"{path}: missing={sorted(expected - actual)!r}, unknown={sorted(actual - expected)!r}",
        )


def _string(value: Any, path: str) -> str:
    if not isinstance(value, str):
        raise FileEffectAuditError("TYPE_STRING_REQUIRED", path)
    return value


def _nonempty_string(value: Any, path: str) -> str:
    result = _string(value, path)
    if not result.strip():
        raise FileEffectAuditError("STRING_EMPTY", path)
    return result


def _identifier(value: Any, path: str) -> str:
    result = _nonempty_string(value, path)
    if IDENTIFIER_RE.fullmatch(result) is None:
        raise FileEffectAuditError("IDENTIFIER_INVALID", f"{path}: {result!r}")
    return result


def _sha256(value: Any, path: str) -> str:
    result = _string(value, path)
    if SHA256_RE.fullmatch(result) is None:
        raise FileEffectAuditError("SHA256_INVALID", path)
    return result


def _boolean(value: Any, path: str) -> bool:
    if not isinstance(value, bool):
        raise FileEffectAuditError("TYPE_BOOLEAN_REQUIRED", path)
    return value


def _enum(enum_type: type[StrEnum], value: Any, path: str) -> Any:
    raw = _string(value, path)
    try:
        return enum_type(raw)
    except ValueError as exc:
        raise FileEffectAuditError("ENUM_VALUE_INVALID", f"{path}: {raw!r}") from exc


def _reject_nonfinite_json(value: str) -> None:
    raise FileEffectAuditError("JSON_NONFINITE_NUMBER", value)


def _error(code: str, message: str) -> dict[str, str]:
    return {"code": code, "message": message}


__all__ = [
    "FILE_EFFECT_SCHEMA_VERSION",
    "FILE_EVENT_SCHEMA_VERSION",
    "INVENTORY_SCHEMA_VERSION",
    "EntryType",
    "EventObservability",
    "FileEffectAuditError",
    "FileEffectEvaluation",
    "FileEffectPolicy",
    "FileEffectVerdict",
    "FileOperation",
    "FileOperationEvent",
    "PathScope",
    "WorkspaceInventory",
    "audit_file_effects",
    "classify_observed_path",
    "inventory_workspace",
    "parse_file_operation_event",
    "parse_file_operation_events_jsonl",
]
