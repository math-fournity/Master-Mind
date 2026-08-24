"""Mechanical GA1 audit input-pack verifier.

This module is intentionally read-only and side-effect-free.  It verifies that
an input pack points to completion objects that are mechanically acceptable for
handoff to a future independent GA1 auditor.  It does not create an
AuditAssignment, does not create an AuditRecord, and does not change any work
package state.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
from typing import Any

from ..contracts.completion_contract import load_dag_index, verify_completion_contract
from ..hashing import canonical_json_bytes, file_sha256


SCHEMA_ID = "seven/audit-input-pack"
SCHEMA_VERSION = 1
SELF_HASH_FIELD = "input_pack_hash"
READINESS_REPORT_SCHEMA_ID = "seven/audit-readiness-report"


class AuditInputPackError(ValueError):
    """Raised when an audit input pack cannot be mechanically accepted."""


@dataclass(frozen=True)
class AuditInputPackValidation:
    """Structured validation result for CLI and tests."""

    verdict: str
    errors: list[str] = field(default_factory=list)
    checked_work_package_ids: list[str] = field(default_factory=list)
    independent_audit_verdict: str = "NOT_STARTED"
    state_effect: str = "NONE"

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"

    def to_dict(self) -> dict[str, Any]:
        return {
            "verdict": self.verdict,
            "errors": list(self.errors),
            "checked_work_package_ids": list(self.checked_work_package_ids),
            "independent_audit_verdict": self.independent_audit_verdict,
            "state_effect": self.state_effect,
        }


def audit_input_pack_hash(pack: dict[str, Any]) -> str:
    """Return the canonical self-hash for an audit input pack."""

    candidate = deepcopy(pack)
    candidate[SELF_HASH_FIELD] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def audit_readiness_report_hash(report: dict[str, Any]) -> str:
    """Return the canonical self-hash for an audit readiness report."""

    candidate = deepcopy(report)
    candidate["report_hash"] = None
    return hashlib.sha256(canonical_json_bytes(candidate)).hexdigest()


def _resolve_ref(base_dir: Path, ref: str) -> Path:
    path = Path(ref)
    if not path.is_absolute():
        path = base_dir / path
    return path


def _load_json_file(path: Path) -> dict[str, Any]:
    if path.is_symlink():
        raise AuditInputPackError(f"ref is a symlink: {path}")
    payload = json.loads(path.read_text())
    if not isinstance(payload, dict):
        raise AuditInputPackError(f"ref is not a JSON object: {path}")
    return payload


def _schema_errors(pack: dict[str, Any], schema_path: Path) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        return ["jsonschema is not available"]
    schema = json.loads(schema_path.read_text())
    validator = jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    )
    return [
        f"schema:{'/'.join(map(str, err.absolute_path)) or '(root)'}:{err.message}"
        for err in sorted(validator.iter_errors(pack), key=lambda item: list(item.path))
    ]


def _contains_audit_overclaim(value: Any) -> bool:
    """Return true when a claim field tries to smuggle an audit verdict."""

    if isinstance(value, str):
        upper = value.upper()
        return any(token in upper for token in ("AUDITED_PASS", "AUDITED_PARTIAL", "AUDITED_FAIL", "INDEPENDENT AUDIT PASS"))
    if isinstance(value, list):
        return any(_contains_audit_overclaim(item) for item in value)
    return False


def _development_closure(dag_index: dict[str, dict[str, Any]], target_wp_id: str) -> list[str]:
    """Return sorted transitive development dependencies for one WP."""

    seen: set[str] = set()

    def visit(wp_id: str) -> None:
        node = dag_index.get(wp_id)
        if not isinstance(node, dict):
            return
        for dep in node.get("development_dependencies", []):
            if isinstance(dep, str) and dep not in seen:
                seen.add(dep)
                visit(dep)

    visit(target_wp_id)
    return sorted(seen)


def _completion_contract_from_schema_id(schema_id: Any) -> str:
    if schema_id == "seven/docs/doc-bootstrap-completion-record":
        return "DOC_BOOTSTRAP_RECORD"
    if schema_id == "seven/implementation-completion-bundle":
        return "IMPLEMENTATION_BUNDLE"
    raise AuditInputPackError(f"unsupported completion object schema_id: {schema_id!r}")


def build_audit_input_pack_from_refs(
    *,
    pack_input: dict[str, Any],
    pack_base_dir: Path,
    schema_path: Path,
    dag_path: Path,
) -> dict[str, Any]:
    """Build and self-check a mechanical GA1 audit input pack.

    ``pack_input`` is intentionally small: a caller supplies only pack metadata
    and already sealed completion-object refs.  The builder loads every object,
    derives ``wp_id``/contract/subject from the object itself, computes the pack
    self-hash, then runs the same validator used by the CLI precheck.
    """

    if not isinstance(pack_input, dict):
        raise AuditInputPackError("pack_input must be a JSON object")
    allowed = {"pack_id", "completion_object_refs", "created_at", "creator", "claims", "nonclaims"}
    unknown = sorted(set(pack_input) - allowed)
    if unknown:
        raise AuditInputPackError(f"unknown pack_input fields: {unknown}")
    for required in ("pack_id", "completion_object_refs", "created_at", "creator"):
        if required not in pack_input:
            raise AuditInputPackError(f"missing pack_input field: {required}")

    refs = pack_input["completion_object_refs"]
    if not isinstance(refs, list) or not refs:
        raise AuditInputPackError("completion_object_refs must be a non-empty array")

    completion_objects: list[dict[str, Any]] = []
    target_ids: list[str] = []
    seen: set[str] = set()
    for ref_hash in refs:
        if not isinstance(ref_hash, dict) or not isinstance(ref_hash.get("ref"), str):
            raise AuditInputPackError("completion_object_refs item is malformed")
        object_path = _resolve_ref(pack_base_dir, ref_hash["ref"])
        if file_sha256(object_path) != ref_hash.get("sha256"):
            raise AuditInputPackError(f"completion object file hash mismatch: {ref_hash['ref']}")
        obj = _load_json_file(object_path)
        wp_id = obj.get("wp_id")
        if not isinstance(wp_id, str):
            raise AuditInputPackError(f"completion object missing wp_id: {ref_hash['ref']}")
        if wp_id in seen:
            raise AuditInputPackError(f"duplicate completion object wp_id: {wp_id}")
        seen.add(wp_id)
        if wp_id == "WP-GA1":
            raise AuditInputPackError("WP-GA1 cannot be listed as an implementation completion object")
        contract = _completion_contract_from_schema_id(obj.get("schema_id"))
        subject = obj.get("implementation_subject")
        if not isinstance(subject, dict):
            raise AuditInputPackError(f"completion object missing implementation_subject: {wp_id}")
        completion_objects.append(
            {
                "wp_id": wp_id,
                "completion_contract": contract,
                "object_ref_and_hash": deepcopy(ref_hash),
                "implementation_subject": {
                    "commit": subject.get("commit"),
                    "tree": subject.get("tree"),
                },
                "expected_state_after_consume": "READY_FOR_AUDIT",
            }
        )
        target_ids.append(wp_id)

    claims = deepcopy(pack_input.get("claims", []))
    if not isinstance(claims, list):
        raise AuditInputPackError("claims must be an array")
    if not claims:
        claims = ["This pack mechanically references candidate completion objects for future GA1 review."]
    nonclaims = deepcopy(pack_input.get("nonclaims", []))
    if not isinstance(nonclaims, list):
        raise AuditInputPackError("nonclaims must be an array")
    nonclaims.extend(
        [
            "This pack is not an AuditAssignment.",
            "This pack is not an AuditRecord.",
            "This pack does not change any work-package state.",
            "This pack does not claim AUDITED_PASS.",
        ]
    )

    pack: dict[str, Any] = {
        "schema_id": SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "pack_id": pack_input["pack_id"],
        "purpose": "GA1_MECHANICAL_INPUT_CANDIDATE",
        "canonical_dag_ref_and_hash": {
            "ref": str(dag_path),
            "sha256": file_sha256(dag_path),
        },
        "target_work_package_ids": target_ids,
        "completion_objects": completion_objects,
        "audit_assignment_status": "NOT_REQUESTED",
        "audit_record_status": "NOT_CREATED",
        "state_effect": "NONE",
        "claims": claims,
        "nonclaims": nonclaims,
        "created_at": pack_input["created_at"],
        "creator": pack_input["creator"],
        "input_pack_hash_algorithm": "sha256(canonical-json-with-input_pack_hash-null)",
        "input_pack_hash": None,
    }
    pack["input_pack_hash"] = audit_input_pack_hash(pack)

    validation = validate_audit_input_pack(
        pack=pack,
        pack_base_dir=pack_base_dir,
        schema_path=schema_path,
        dag_path=dag_path,
    )
    if not validation.passed:
        raise AuditInputPackError("; ".join(validation.errors))
    return pack


def validate_audit_input_pack(
    *,
    pack: dict[str, Any],
    pack_base_dir: Path,
    schema_path: Path,
    dag_path: Path,
) -> AuditInputPackValidation:
    """Validate a GA1 mechanical input candidate.

    The function deliberately returns a report rather than raising for ordinary
    validation failures, making it suitable for audit preflight and CLI use.
    """

    errors: list[str] = []
    checked: list[str] = []

    if not isinstance(pack, dict):
        return AuditInputPackValidation(verdict="FAIL", errors=["pack is not a JSON object"])

    errors.extend(_schema_errors(pack, schema_path))

    if pack.get("schema_id") == SCHEMA_ID and pack.get("schema_version") == SCHEMA_VERSION:
        expected_hash = audit_input_pack_hash(pack)
        if pack.get(SELF_HASH_FIELD) != expected_hash:
            errors.append("input_pack_hash mismatch")

    dag_ref = pack.get("canonical_dag_ref_and_hash", {})
    if isinstance(dag_ref, dict):
        if dag_ref.get("sha256") != file_sha256(dag_path):
            errors.append("canonical DAG hash mismatch")

    try:
        dag_index = load_dag_index(dag_path)
    except Exception as exc:  # fail closed; exact exception is not the contract
        errors.append(f"failed to load canonical DAG: {type(exc).__name__}: {exc}")
        dag_index = {}

    target_ids = pack.get("target_work_package_ids", [])
    completion_objects = pack.get("completion_objects", [])
    if not isinstance(target_ids, list):
        target_ids = []
    if not isinstance(completion_objects, list):
        completion_objects = []

    object_ids = [item.get("wp_id") for item in completion_objects if isinstance(item, dict)]
    if sorted(target_ids) != sorted(object_ids):
        errors.append("target_work_package_ids and completion_objects wp_id set differ")
    if len(object_ids) != len(set(object_ids)):
        errors.append("duplicate completion object wp_id")

    for item in completion_objects:
        if not isinstance(item, dict):
            errors.append("completion object entry is not an object")
            continue
        wp_id = item.get("wp_id")
        if not isinstance(wp_id, str):
            errors.append("completion object missing wp_id")
            continue
        checked.append(wp_id)
        if wp_id == "WP-GA1":
            errors.append("WP-GA1 cannot be listed as an implementation completion object")
            continue

        node = dag_index.get(wp_id)
        if not isinstance(node, dict):
            errors.append(f"unknown work package: {wp_id}")
            continue
        expected_contract = node.get("completion_contract")
        if item.get("completion_contract") != expected_contract:
            errors.append(
                f"{wp_id} completion_contract mismatch: expected {expected_contract}, got {item.get('completion_contract')}"
            )
            continue
        if expected_contract not in {"DOC_BOOTSTRAP_RECORD", "IMPLEMENTATION_BUNDLE"}:
            errors.append(f"{wp_id} is not an implementer completion object")
            continue

        ref_hash = item.get("object_ref_and_hash", {})
        if not isinstance(ref_hash, dict) or not isinstance(ref_hash.get("ref"), str):
            errors.append(f"{wp_id} object_ref_and_hash is malformed")
            continue
        object_path = _resolve_ref(pack_base_dir, ref_hash["ref"])
        try:
            if file_sha256(object_path) != ref_hash.get("sha256"):
                errors.append(f"{wp_id} object file hash mismatch")
                continue
            submitted = _load_json_file(object_path)
        except (OSError, json.JSONDecodeError, AuditInputPackError) as exc:
            errors.append(f"{wp_id} object load failed: {type(exc).__name__}: {exc}")
            continue

        if _contains_audit_overclaim(submitted.get("claims", [])):
            errors.append(f"{wp_id} completion object claims an audit verdict")

        subject = item.get("implementation_subject", {})
        expected_commit = subject.get("commit") if isinstance(subject, dict) else None
        expected_tree = subject.get("tree") if isinstance(subject, dict) else None
        verification = verify_completion_contract(
            dag_path=dag_path,
            expected_dag_sha256=file_sha256(dag_path),
            wp_id=wp_id,
            submitted_object=submitted,
            actor_type="IMPLEMENTER",
            state_command="READY_FOR_AUDIT",
            expected_subject_commit=expected_commit,
            expected_subject_tree=expected_tree,
        )
        if not verification.passed:
            errors.append(
                f"{wp_id} completion contract failed: "
                f"{','.join(code.value for code in verification.error_codes)}"
            )

    return AuditInputPackValidation(
        verdict="PASS" if not errors else "FAIL",
        errors=errors,
        checked_work_package_ids=sorted(set(checked)),
    )


def load_and_validate_audit_input_pack(
    *,
    pack_path: Path,
    schema_path: Path,
    dag_path: Path,
) -> AuditInputPackValidation:
    """Load an audit input pack file and validate it."""

    try:
        pack = _load_json_file(pack_path)
    except (OSError, json.JSONDecodeError, AuditInputPackError) as exc:
        return AuditInputPackValidation(
            verdict="FAIL",
            errors=[f"pack load failed: {type(exc).__name__}: {exc}"],
        )
    return validate_audit_input_pack(
        pack=pack,
        pack_base_dir=pack_path.parent,
        schema_path=schema_path,
        dag_path=dag_path,
    )


def build_audit_readiness_report(
    *,
    report_id: str,
    pack_path: Path,
    input_pack_schema_path: Path,
    dag_path: Path,
    expected_scope: str,
    created_at: str,
    creator: str,
) -> dict[str, Any]:
    """Build a read-only readiness report for a mechanical GA1 input pack."""

    if expected_scope not in {"PACK_TARGETS_ONLY", "GA1_DEVELOPMENT_CLOSURE"}:
        raise AuditInputPackError(f"unknown expected_scope: {expected_scope}")
    pack = _load_json_file(pack_path)
    validation = validate_audit_input_pack(
        pack=pack,
        pack_base_dir=pack_path.parent,
        schema_path=input_pack_schema_path,
        dag_path=dag_path,
    )
    dag_index = load_dag_index(dag_path)
    covered = sorted(
        wp_id
        for wp_id in pack.get("target_work_package_ids", [])
        if isinstance(wp_id, str)
    )
    if expected_scope == "PACK_TARGETS_ONLY":
        expected = list(covered)
    else:
        expected = [
            wp_id
            for wp_id in _development_closure(dag_index, "WP-GA1")
            if wp_id != "WP-GA1"
        ]

    missing = sorted(set(expected) - set(covered))
    unexpected = sorted(set(covered) - set(expected))
    invalid = list(validation.checked_work_package_ids if not validation.passed else [])
    if not validation.passed:
        status = "INVALID_INPUT"
    elif missing or unexpected:
        status = "INCOMPLETE"
    else:
        status = "COMPLETE"

    report: dict[str, Any] = {
        "schema_id": READINESS_REPORT_SCHEMA_ID,
        "schema_version": 1,
        "report_id": report_id,
        "input_pack_ref_and_hash": {
            "ref": str(pack_path),
            "sha256": file_sha256(pack_path),
        },
        "canonical_dag_ref_and_hash": {
            "ref": str(dag_path),
            "sha256": file_sha256(dag_path),
        },
        "expected_scope": expected_scope,
        "expected_work_package_ids": expected,
        "covered_work_package_ids": covered,
        "missing_work_package_ids": missing,
        "unexpected_work_package_ids": unexpected,
        "invalid_work_package_ids": sorted(set(invalid)),
        "audit_input_validation": {
            "verdict": validation.verdict,
            "errors": validation.errors,
        },
        "mechanical_handoff_status": status,
        "independent_audit_verdict": "NOT_STARTED",
        "state_effect": "NONE",
        "claims": [
            "This report mechanically compares an AuditInputPack against a declared expected scope.",
        ],
        "nonclaims": [
            "This report is not an AuditAssignment.",
            "This report is not an AuditRecord.",
            "This report does not change any work-package state.",
            "COMPLETE only means mechanical handoff input coverage; it is not AUDITED_PASS.",
        ],
        "created_at": created_at,
        "creator": creator,
        "report_hash_algorithm": "sha256(canonical-json-with-report_hash-null)",
        "report_hash": None,
    }
    report["report_hash"] = audit_readiness_report_hash(report)
    return report


__all__ = [
    "AuditInputPackError",
    "AuditInputPackValidation",
    "audit_input_pack_hash",
    "audit_readiness_report_hash",
    "build_audit_input_pack_from_refs",
    "build_audit_readiness_report",
    "load_and_validate_audit_input_pack",
    "validate_audit_input_pack",
]
