"""Canonical Ed25519 verification for every Seven signed object.

The object type determines the domain separator, signature location, signed-hash
location and self-hash field. Callers cannot supply those values. This avoids
silently reusing GateDecision's shape for EEA, Permit and the service-attested
consumption receipt.

SIDE_EFFECT_FREE: reads only the versioned JSON Schemas shipped with Seven.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..hashing import canonical_json_bytes
from .signature_verifier import SignatureVerificationReceipt, verify_signature


@dataclass(frozen=True)
class SignedObjectProfile:
    schema_id: str
    domain: str
    signature_field_path: str
    envelope_hash_field_path: str
    top_hash_field: str | None
    self_hash_field: str | None
    signer_field_path: str
    key_id_field_path: str
    declared_domain_field: str | None
    schema_file: str | None
    top_signer_field: str | None = None
    top_key_id_field: str | None = None


_PROFILES: dict[str, SignedObjectProfile] = {
    "seven/human-gate-decision": SignedObjectProfile(
        schema_id="seven/human-gate-decision",
        domain="seven-human-gate-decision/v1\0",
        signature_field_path="signature_envelope.signature_b64",
        envelope_hash_field_path="signature_envelope.signed_bytes_hash",
        top_hash_field="signed_bytes_hash",
        self_hash_field="decision_hash",
        signer_field_path="signature_envelope.signer_principal_id",
        key_id_field_path="signature_envelope.key_id",
        declared_domain_field="signature_domain",
        schema_file=None,
        top_signer_field="actor_id",
        top_key_id_field="key_id",
    ),
    "seven/audit-assignment": SignedObjectProfile(
        schema_id="seven/audit-assignment",
        domain="seven-audit-assignment/v1\0",
        signature_field_path="signature_envelope.signature_b64",
        envelope_hash_field_path="signature_envelope.signed_bytes_hash",
        top_hash_field="signed_bytes_hash",
        self_hash_field="assignment_hash",
        signer_field_path="signature_envelope.signer_actor_id",
        key_id_field_path="signature_envelope.key_id",
        declared_domain_field="signature_domain",
        schema_file="audit-assignment.v1.schema.json",
        top_signer_field="owner_actor_id",
    ),
    "seven/audit-record": SignedObjectProfile(
        schema_id="seven/audit-record",
        domain="seven-audit-record/v1\0",
        signature_field_path="signature_envelope.signature_b64",
        envelope_hash_field_path="signature_envelope.signed_bytes_hash",
        top_hash_field="signed_bytes_hash",
        self_hash_field="audit_record_hash",
        signer_field_path="signature_envelope.signer_principal_id",
        key_id_field_path="signature_envelope.key_id",
        declared_domain_field="signature_domain",
        schema_file="audit-record.v1.schema.json",
        top_signer_field="auditor_principal_id",
        top_key_id_field="auditor_attestation_key_id",
    ),
    "seven/external-execution-authorization": SignedObjectProfile(
        schema_id="seven/external-execution-authorization",
        domain="seven-external-execution-authorization/v1\0",
        signature_field_path="signature_envelope.signature_b64",
        envelope_hash_field_path="signature_envelope.signed_bytes_hash",
        top_hash_field="signed_bytes_hash",
        self_hash_field="authorization_hash",
        signer_field_path="signature_envelope.signer_actor_id",
        key_id_field_path="signature_envelope.key_id",
        declared_domain_field="signature_domain",
        schema_file="external-execution-authorization.v1.schema.json",
        top_signer_field="issuer_actor_id",
        top_key_id_field="issuer_key_id",
    ),
    "seven/live-run-permit": SignedObjectProfile(
        schema_id="seven/live-run-permit",
        domain="seven-live-run-permit/v1\0",
        signature_field_path="signature_envelope.signature_b64",
        envelope_hash_field_path="signature_envelope.signed_bytes_hash",
        top_hash_field="signed_bytes_hash",
        self_hash_field="permit_hash",
        signer_field_path="signature_envelope.signer_actor_id",
        key_id_field_path="signature_envelope.key_id",
        declared_domain_field="signature_domain",
        schema_file="live-run-permit.v1.schema.json",
        top_signer_field="issuer_actor_id",
        top_key_id_field="issuer_key_id",
    ),
    "seven/authorization-consumption-receipt": SignedObjectProfile(
        schema_id="seven/authorization-consumption-receipt",
        domain="seven-authorization-consumption-receipt/v1\0",
        signature_field_path="service_attestation.signature_b64",
        envelope_hash_field_path="service_attestation.attested_bytes_hash",
        top_hash_field="attested_bytes_hash",
        self_hash_field="receipt_hash",
        signer_field_path="service_attestation.service_principal_id",
        key_id_field_path="service_attestation.key_id",
        declared_domain_field="attestation_domain",
        schema_file="authorization-consumption-receipt.v1.schema.json",
    ),
    # This v1 review object predates the unified envelope shape. Its profile is
    # nevertheless explicit and Schema-bound; it cannot be mistaken for EEA.
    "seven/docs/normative-requirement-review-record": SignedObjectProfile(
        schema_id="seven/docs/normative-requirement-review-record",
        domain="seven.normative-requirement-review-record.v1",
        signature_field_path="signature_envelope.signature_base64",
        envelope_hash_field_path="signature_envelope.signed_payload_sha256",
        top_hash_field=None,
        self_hash_field=None,
        signer_field_path="signature_envelope.signer_actor_id",
        key_id_field_path="signature_envelope.key_id",
        declared_domain_field="signature_envelope.domain_separator",
        schema_file="normative-requirement-review-record.v1.schema.json",
        top_signer_field="reviewer_actor_id",
    ),
}

# Public compatibility view, now derived from the canonical profiles.
SIGNED_OBJECT_DOMAINS: dict[str, str] = {
    schema_id: profile.domain for schema_id, profile in _PROFILES.items()
}


@dataclass(frozen=True)
class SignedObjectVerificationResult:
    verdict: str
    object_type: str
    receipt: SignatureVerificationReceipt
    error_codes: list[str]
    details: list[str]


def _get_path(obj: dict[str, Any], path: str) -> Any:
    current: Any = obj
    for part in path.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(part)
    return current


def _schema_errors(obj: dict[str, Any], profile: SignedObjectProfile) -> list[str]:
    if profile.schema_file is None:
        return []
    schema_path = (
        Path(__file__).resolve().parents[3]
        / "docs"
        / "implementation"
        / profile.schema_file
    )
    try:
        from jsonschema import Draft202012Validator, FormatChecker

        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [
            f"{'.'.join(map(str, error.absolute_path)) or '(root)'}: {error.message}"
            for error in sorted(
                validator.iter_errors(obj), key=lambda item: list(item.absolute_path)
            )
        ]
    except Exception as exc:  # missing validator/schema is a hard failure
        return [f"cannot execute canonical Schema {schema_path}: {exc}"]


def _self_hash(obj: dict[str, Any], field: str) -> str:
    unsigned = copy.deepcopy(obj)
    unsigned[field] = None
    return hashlib.sha256(canonical_json_bytes(unsigned)).hexdigest()


def _failed_receipt(detail: str) -> SignatureVerificationReceipt:
    return SignatureVerificationReceipt(
        verified=False,
        algorithm="Ed25519",
        key_id="",
        signer_principal_id="",
        signed_bytes_hash="",
        verification_error=detail,
    )


def verify_signed_object(
    signed_object: dict[str, Any],
    *,
    public_key_bytes: bytes,
    expected_schema_id: str | None = None,
) -> SignedObjectVerificationResult:
    """Schema-validate, reconstruct, hash-check and verify one signed object."""
    errors: list[str] = []
    details: list[str] = []
    schema_id = signed_object.get("schema_id", "")
    if expected_schema_id is not None and schema_id != expected_schema_id:
        errors.append("SCHEMA_ID_MISMATCH")
        details.append(f"expected {expected_schema_id}, got {schema_id}")

    profile = _PROFILES.get(schema_id)
    if profile is None:
        errors.append("UNKNOWN_SIGNED_OBJECT_TYPE")
        details.append(f"unknown schema_id: {schema_id}")
        return SignedObjectVerificationResult(
            verdict="FAIL",
            object_type=str(schema_id),
            receipt=_failed_receipt("unknown signed object profile"),
            error_codes=errors,
            details=details,
        )

    schema_errors = _schema_errors(signed_object, profile)
    if schema_errors:
        errors.append("SCHEMA_VALIDATION_FAILED")
        details.extend(schema_errors[:20])

    if profile.declared_domain_field is not None:
        declared = _get_path(signed_object, profile.declared_domain_field)
        if declared != profile.domain:
            errors.append("SIGNATURE_DOMAIN_INVALID")
            details.append(f"declared domain {declared!r} != canonical {profile.domain!r}")

    if profile.top_signer_field is not None:
        top_signer = _get_path(signed_object, profile.top_signer_field)
        envelope_signer = _get_path(signed_object, profile.signer_field_path)
        if top_signer != envelope_signer:
            errors.append("SIGNER_BINDING_MISMATCH")
            details.append(
                f"top signer {top_signer!r} != envelope signer {envelope_signer!r}"
            )
    if profile.top_key_id_field is not None:
        top_key = _get_path(signed_object, profile.top_key_id_field)
        envelope_key = _get_path(signed_object, profile.key_id_field_path)
        if top_key != envelope_key:
            errors.append("KEY_BINDING_MISMATCH")
            details.append(f"top key {top_key!r} != envelope key {envelope_key!r}")

    receipt = verify_signature(
        signed_object=signed_object,
        public_key_bytes=public_key_bytes,
        signature_domain=profile.domain.encode("utf-8"),
        signature_field_path=profile.signature_field_path,
        envelope_hash_field_path=profile.envelope_hash_field_path,
        top_hash_field=profile.top_hash_field,
        self_hash_field=profile.self_hash_field,
        signer_field_path=profile.signer_field_path,
        key_id_field_path=profile.key_id_field_path,
    )
    if not receipt.verified:
        errors.append("SIGNATURE_INVALID")
        details.append(receipt.verification_error or "signature verification failed")
    else:
        envelope_hash = _get_path(signed_object, profile.envelope_hash_field_path)
        if envelope_hash != receipt.signed_bytes_hash:
            errors.append("SIGNED_BYTES_HASH_MISMATCH")
            details.append(
                f"envelope signed hash {envelope_hash!r} != computed "
                f"{receipt.signed_bytes_hash}"
            )
        if profile.top_hash_field is not None:
            top_hash = signed_object.get(profile.top_hash_field)
            if top_hash != receipt.signed_bytes_hash:
                errors.append("SIGNED_BYTES_HASH_MISMATCH")
                details.append(
                    f"top signed hash {top_hash!r} != computed "
                    f"{receipt.signed_bytes_hash}"
                )

    if profile.self_hash_field is not None and profile.self_hash_field in signed_object:
        computed_self_hash = _self_hash(signed_object, profile.self_hash_field)
        if signed_object.get(profile.self_hash_field) != computed_self_hash:
            errors.append("OBJECT_HASH_MISMATCH")
            details.append(
                f"{profile.self_hash_field} mismatch: expected {computed_self_hash}, "
                f"got {signed_object.get(profile.self_hash_field)}"
            )

    return SignedObjectVerificationResult(
        verdict="PASS" if not errors else "FAIL",
        object_type=str(schema_id),
        receipt=receipt,
        error_codes=errors,
        details=details,
    )


def verify_audit_assignment(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    return verify_signed_object(
        obj, public_key_bytes=public_key_bytes, expected_schema_id="seven/audit-assignment"
    )


def verify_audit_record(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    return verify_signed_object(
        obj, public_key_bytes=public_key_bytes, expected_schema_id="seven/audit-record"
    )


def verify_eea(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    return verify_signed_object(
        obj,
        public_key_bytes=public_key_bytes,
        expected_schema_id="seven/external-execution-authorization",
    )


def verify_live_run_permit(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    return verify_signed_object(
        obj, public_key_bytes=public_key_bytes, expected_schema_id="seven/live-run-permit"
    )


def verify_authorization_consumption_receipt(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    return verify_signed_object(
        obj,
        public_key_bytes=public_key_bytes,
        expected_schema_id="seven/authorization-consumption-receipt",
    )


def verify_normative_requirement_review_record(
    obj: dict[str, Any], *, public_key_bytes: bytes
) -> SignedObjectVerificationResult:
    return verify_signed_object(
        obj,
        public_key_bytes=public_key_bytes,
        expected_schema_id="seven/docs/normative-requirement-review-record",
    )
