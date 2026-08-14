"""AccessEvent — append-only 结果账。

保存相同 principal/operation/object/view/sink/nonce 绑定、
decision/derivation/receipt refs、revocation snapshot、
sequence 和 previous-event hash。

ACCESS_GRANTED 缺任何 derivation 或 sink receipt 均不合法。
Ledger 是 append-only：sequence 递增，previous_event_hash 链接前一条。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ACCESS_EVENT_RESULTS,
    FORBIDDEN_OPERATIONS,
    REVOCATION_STATUSES,
    SENSITIVITY_LEVELS,
    SINK_KINDS,
    VAULT_OPERATIONS,
    VAULT_PRINCIPAL_TYPES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from ..contracts.security_contract import _check_canonical_utc
from .access_capability import (
    _check_exact_id,
    _check_hash,
    _check_nonce,
    _check_opaque_ref_hash,
    _check_named_hash,
    _check_principal,
    _check_object_binding,
    _check_view_binding,
    _check_sink_binding,
    _check_issuer,
    _check_signature_envelope,
)
from .access_decision import _check_revocation_check


_SCHEMA_ID = "seven/access-event"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "AccessEvent"
_SIGNATURE_DOMAIN = "seven-access-event/v1\0"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-event_hash-null)"


@dataclass(frozen=True)
class AccessEvent:
    """AccessEvent 数据对象。"""

    event_id: str
    ledger_id: str
    sequence: int
    previous_event_hash: str | None
    access_request_id: str
    capability_ref_and_hash: dict[str, str]
    decision_ref_and_hash: dict[str, str]
    view_derivation_ref_and_hash: dict[str, str] | None
    sink_write_receipt_ref_and_hash: dict[str, str] | None
    principal: dict[str, Any]
    operation: str
    object_binding: dict[str, Any]
    view_binding: dict[str, Any]
    sink_binding: dict[str, Any]
    nonce: str
    revocation_check: dict[str, Any]
    deny_by_default: bool
    raw_vault_path_disclosed: bool
    result: str
    occurred_at: str
    issuer: dict[str, Any]
    externally_pinned_trust_root: dict[str, str]
    issuer_key_registry_ref_and_hash: dict[str, str]
    canonicalizer_profile: str
    signature_domain: str
    signed_bytes_hash: str
    signature_envelope: dict[str, Any]
    event_hash_algorithm: str
    event_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "object_type": _OBJECT_TYPE,
            "event_id": self.event_id,
            "ledger_id": self.ledger_id,
            "sequence": self.sequence,
            "previous_event_hash": self.previous_event_hash,
            "access_request_id": self.access_request_id,
            "capability_ref_and_hash": dict(self.capability_ref_and_hash),
            "decision_ref_and_hash": dict(self.decision_ref_and_hash),
            "view_derivation_ref_and_hash": dict(self.view_derivation_ref_and_hash) if self.view_derivation_ref_and_hash else None,
            "sink_write_receipt_ref_and_hash": dict(self.sink_write_receipt_ref_and_hash) if self.sink_write_receipt_ref_and_hash else None,
            "principal": dict(self.principal),
            "operation": self.operation,
            "object_binding": dict(self.object_binding),
            "view_binding": dict(self.view_binding),
            "sink_binding": dict(self.sink_binding),
            "nonce": self.nonce,
            "revocation_check": dict(self.revocation_check),
            "deny_by_default": self.deny_by_default,
            "raw_vault_path_disclosed": self.raw_vault_path_disclosed,
            "result": self.result,
            "occurred_at": self.occurred_at,
            "issuer": dict(self.issuer),
            "externally_pinned_trust_root": dict(self.externally_pinned_trust_root),
            "issuer_key_registry_ref_and_hash": dict(self.issuer_key_registry_ref_and_hash),
            "canonicalizer_profile": self.canonicalizer_profile,
            "signature_domain": self.signature_domain,
            "signed_bytes_hash": self.signed_bytes_hash,
            "signature_envelope": dict(self.signature_envelope),
            "event_hash_algorithm": self.event_hash_algorithm,
            "event_hash": self.event_hash,
        }


def verify_access_event(
    event: dict[str, Any],
    *,
    expected_previous_event_hash: str | None = None,
    expected_sequence: int | None = None,
) -> VerificationResult:
    """验证单个 AccessEvent 的 schema + semantic 合法性。

    检查：
    1. schema 常量
    2. deny_by_default == true, raw_vault_path_disclosed == false
    3. sequence >= 1
    4. previous_event_hash: sequence==1 → null, sequence>1 → 64-hex
    5. result 在合法枚举中
    6. ACCESS_GRANTED → view_derivation_ref_and_hash 和 sink_write_receipt_ref_and_hash 必须存在
    7. revocation_check 结构合法
    8. event_hash 正确
    9. semantic: TARGET_SOLVER → sensitivity PUBLIC/RESTRICTED
    10. semantic: WRITE/SEAL → sink_kind RESTRICTED
    11. 如果提供 expected_previous_event_hash：比较
    12. 如果提供 expected_sequence：比较
    """
    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. schema 常量
    if event.get("schema_id") != _SCHEMA_ID:
        _err(EC.SCHEMA_ID_MISMATCH, f"schema_id must be {_SCHEMA_ID}")
    if event.get("schema_version") != _SCHEMA_VERSION:
        _err(EC.SCHEMA_ID_MISMATCH, f"schema_version must be {_SCHEMA_VERSION}")
    if event.get("object_type") != _OBJECT_TYPE:
        _err(EC.SCHEMA_ID_MISMATCH, f"object_type must be {_OBJECT_TYPE}")

    # 2. deny_by_default / raw_vault_path_disclosed
    if event.get("deny_by_default") is not True:
        _err(EC.VAULT_DENY_BY_DEFAULT_FALSE, "deny_by_default must be true")
    if event.get("raw_vault_path_disclosed") is not False:
        _err(EC.VAULT_RAW_PATH_DISCLOSED, "raw_vault_path_disclosed must be false")

    # 3. IDs
    for code, detail in _check_exact_id(event.get("event_id", ""), "event_id"):
        _err(code, detail)
    for code, detail in _check_exact_id(event.get("ledger_id", ""), "ledger_id"):
        _err(code, detail)
    for code, detail in _check_exact_id(event.get("access_request_id", ""), "access_request_id"):
        _err(code, detail)

    # 4. sequence
    sequence = event.get("sequence", 0)
    if not isinstance(sequence, int) or isinstance(sequence, bool) or sequence < 1:
        _err(EC.ACCESS_LEDGER_SEQUENCE_CONFLICT, f"sequence must be integer >= 1, got {sequence}")

    # 5. previous_event_hash
    prev_hash = event.get("previous_event_hash")
    if sequence == 1:
        if prev_hash is not None:
            _err(EC.ACCESS_LEDGER_PREVIOUS_HASH_MISMATCH,
                 "first event (sequence=1) must have previous_event_hash=null")
    else:
        if prev_hash is None:
            _err(EC.ACCESS_LEDGER_PREVIOUS_HASH_MISMATCH,
                 f"event sequence={sequence} must have non-null previous_event_hash")
        else:
            for code, detail in _check_hash(prev_hash, "previous_event_hash"):
                _err(code, detail)

    # 6. refs
    for code, detail in _check_opaque_ref_hash(event.get("capability_ref_and_hash", {}), "capability_ref_and_hash"):
        _err(code, detail)
    for code, detail in _check_opaque_ref_hash(event.get("decision_ref_and_hash", {}), "decision_ref_and_hash"):
        _err(code, detail)

    view_deriv_ref = event.get("view_derivation_ref_and_hash")
    if view_deriv_ref is not None:
        for code, detail in _check_opaque_ref_hash(view_deriv_ref, "view_derivation_ref_and_hash"):
            _err(code, detail)

    sink_receipt_ref = event.get("sink_write_receipt_ref_and_hash")
    if sink_receipt_ref is not None:
        for code, detail in _check_opaque_ref_hash(sink_receipt_ref, "sink_write_receipt_ref_and_hash"):
            _err(code, detail)

    # 7. principal / operation / object / view / sink
    for code, detail in _check_principal(event.get("principal", {})):
        _err(code, detail)
    operation = event.get("operation", "")
    if operation in FORBIDDEN_OPERATIONS:
        _err(EC.VAULT_READ_RAW_OBJECT_REJECTED, f"operation {operation} is forbidden")
    elif operation not in VAULT_OPERATIONS:
        _err(EC.VAULT_OPERATION_MISMATCH, f"unknown operation: {operation}")
    for code, detail in _check_object_binding(event.get("object_binding", {})):
        _err(code, detail)
    for code, detail in _check_view_binding(event.get("view_binding", {})):
        _err(code, detail)
    for code, detail in _check_sink_binding(event.get("sink_binding", {})):
        _err(code, detail)

    # 8. nonce
    for code, detail in _check_nonce(event.get("nonce", "")):
        _err(code, detail)

    # 9. revocation_check
    for code, detail in _check_revocation_check(event.get("revocation_check", {})):
        _err(code, detail)

    # 10. result
    result = event.get("result", "")
    if result not in ACCESS_EVENT_RESULTS:
        _err(EC.VAULT_ACCESS_DENIED, f"invalid result: {result}")

    # 11. ACCESS_GRANTED → derivation + sink receipt 必须存在
    if result == "ACCESS_GRANTED":
        if view_deriv_ref is None:
            _err(EC.VIEW_SINK_RECEIPT_MISSING,
                 "ACCESS_GRANTED requires view_derivation_ref_and_hash")
        if sink_receipt_ref is None:
            _err(EC.VIEW_SINK_RECEIPT_MISSING,
                 "ACCESS_GRANTED requires sink_write_receipt_ref_and_hash")
        rev_status = event.get("revocation_check", {}).get("status", "")
        if rev_status != "ACTIVE":
            _err(EC.VAULT_CAPABILITY_REVOKED,
                 f"ACCESS_GRANTED requires revocation ACTIVE, got {rev_status}")

    # 12. occurred_at
    if not _check_canonical_utc(event.get("occurred_at", "")):
        _err(EC.TIME_NOT_CANONICAL_UTC, "occurred_at is not canonical UTC")

    # 13. issuer / trust_root / key_registry
    for code, detail in _check_issuer(event.get("issuer", {})):
        _err(code, detail)
    for code, detail in _check_named_hash(event.get("externally_pinned_trust_root", {}), "externally_pinned_trust_root"):
        _err(code, detail)
    for code, detail in _check_opaque_ref_hash(event.get("issuer_key_registry_ref_and_hash", {}), "issuer_key_registry_ref_and_hash"):
        _err(code, detail)

    # 14. canonicalizer_profile / signature_domain
    if event.get("canonicalizer_profile") != "RFC8785_JCS_UTF8":
        _err(EC.SCHEMA_ID_MISMATCH, "canonicalizer_profile must be RFC8785_JCS_UTF8")
    sig_domain = event.get("signature_domain", "")
    if sig_domain != _SIGNATURE_DOMAIN:
        _err(EC.SIGNATURE_DOMAIN_INVALID, f"signature_domain mismatch")

    # 15. signed_bytes_hash
    for code, detail in _check_hash(event.get("signed_bytes_hash", ""), "signed_bytes_hash"):
        _err(code, detail)

    # 16. signature_envelope
    for code, detail in _check_signature_envelope(
        event.get("signature_envelope", {}),
        event.get("signed_bytes_hash", ""),
    ):
        _err(code, detail)

    # 17. event_hash_algorithm
    hash_algo = event.get("event_hash_algorithm", "")
    if hash_algo != _HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH, f"unexpected event_hash_algorithm: {hash_algo}")

    # 18. event_hash 验证
    obj_for_hash = dict(event)
    obj_for_hash["event_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if event.get("event_hash") != computed_hash:
        _err(EC.ACCESS_EVENT_HASH_MISMATCH,
             f"event_hash mismatch: expected {computed_hash}, got {event.get('event_hash')}")

    # 19. expected_previous_event_hash
    if expected_previous_event_hash is not None:
        if prev_hash != expected_previous_event_hash:
            _err(EC.ACCESS_LEDGER_PREVIOUS_HASH_MISMATCH,
                 f"previous_event_hash mismatch: expected {expected_previous_event_hash}, got {prev_hash}")

    # 20. expected_sequence
    if expected_sequence is not None:
        if sequence != expected_sequence:
            _err(EC.ACCESS_LEDGER_SEQUENCE_CONFLICT,
                 f"sequence mismatch: expected {expected_sequence}, got {sequence}")

    # 21. semantic: TARGET_SOLVER → sensitivity PUBLIC/RESTRICTED
    principal = event.get("principal", {})
    ptype = principal.get("principal_type", "")
    if ptype == "TARGET_SOLVER" and operation in ("READ_DERIVED_VIEW", "DERIVE_VIEW"):
        sensitivity = event.get("object_binding", {}).get("sensitivity", "")
        if sensitivity not in ("PUBLIC", "RESTRICTED"):
            _err(EC.VAULT_OBJECT_HASH_MISMATCH,
                 f"TARGET_SOLVER can only access PUBLIC/RESTRICTED, got {sensitivity}")

    # 22. semantic: WRITE/SEAL → sink_kind RESTRICTED
    if operation in ("WRITE_RESTRICTED_OBJECT", "SEAL_RESTRICTED_OBJECT"):
        sink_kind = event.get("sink_binding", {}).get("sink_kind", "")
        if sink_kind not in ("RESTRICTED_VAULT", "RESTRICTED_CAS"):
            _err(EC.VAULT_SINK_MISMATCH,
                 f"WRITE/SEAL requires RESTRICTED sink, got {sink_kind}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )


class AccessEventLedger:
    """AccessEvent append-only ledger。

    SIDE_EFFECT_FREE：纯内存实现。
    维护 sequence 递增、previous_event_hash 链接、nonce 去重。
    任何篡改、sequence 冲突、previous-hash 不匹配都会被检测。
    """

    def __init__(self, ledger_id: str) -> None:
        self._ledger_id = ledger_id
        self._events: list[dict[str, Any]] = []
        self._seen_nonces: set[str] = set()
        self._seen_sequences: set[int] = set()

    @property
    def ledger_id(self) -> str:
        return self._ledger_id

    @property
    def length(self) -> int:
        return len(self._events)

    @property
    def last_event_hash(self) -> str | None:
        if not self._events:
            return None
        return self._events[-1].get("event_hash")

    @property
    def next_sequence(self) -> int:
        return len(self._events) + 1

    def append(self, event: dict[str, Any]) -> VerificationResult:
        """追加一个 AccessEvent 到 ledger。

        验证：
        1. event 本身合法（verify_access_event）
        2. sequence == next_sequence
        3. previous_event_hash == last_event_hash
        4. nonce 未在 ledger 中出现过（nonce replay 防护）
        5. ledger_id 匹配
        """
        errors: list[EC] = []
        details: list[str] = []

        # ledger_id 匹配
        if event.get("ledger_id") != self._ledger_id:
            errors.append(EC.ACCESS_LEDGER_TAMPERED)
            details.append(f"ledger_id mismatch: expected {self._ledger_id}, got {event.get('ledger_id')}")

        # sequence 检查
        expected_seq = self.next_sequence
        if event.get("sequence") != expected_seq:
            errors.append(EC.ACCESS_LEDGER_SEQUENCE_CONFLICT)
            details.append(f"sequence must be {expected_seq}, got {event.get('sequence')}")

        # previous_event_hash 检查
        expected_prev = self.last_event_hash
        if event.get("previous_event_hash") != expected_prev:
            errors.append(EC.ACCESS_LEDGER_PREVIOUS_HASH_MISMATCH)
            details.append(f"previous_event_hash must be {expected_prev}, got {event.get('previous_event_hash')}")

        # nonce replay 检查
        nonce = event.get("nonce", "")
        if nonce in self._seen_nonces:
            errors.append(EC.VAULT_NONCE_REPLAY)
            details.append(f"nonce already used in this ledger: {nonce}")

        # event 本身验证
        event_result = verify_access_event(
            event,
            expected_previous_event_hash=expected_prev,
            expected_sequence=expected_seq,
        )
        if not event_result.passed:
            errors.extend(event_result.error_codes)
            details.extend(event_result.details)

        if errors:
            return VerificationResult(
                verdict="FAIL",
                error_codes=errors,
                details=details,
            )

        # 追加
        self._events.append(dict(event))
        self._seen_nonces.add(nonce)
        self._seen_sequences.add(event["sequence"])

        return VerificationResult(verdict="PASS")

    def verify_integrity(self) -> VerificationResult:
        """验证整个 ledger 的完整性。

        检查每条 event 的 hash、sequence 递增、previous_event_hash 链接。
        """
        errors: list[EC] = []
        details: list[str] = []

        prev_hash: str | None = None
        for i, event in enumerate(self._events):
            expected_seq = i + 1
            result = verify_access_event(
                event,
                expected_previous_event_hash=prev_hash,
                expected_sequence=expected_seq,
            )
            if not result.passed:
                errors.extend(result.error_codes)
                details.extend([f"event[{i}]: {d}" for d in result.details])
            prev_hash = event.get("event_hash")

        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(
            verdict=verdict,
            error_codes=errors,
            details=details,
        )

    def get_event(self, sequence: int) -> dict[str, Any] | None:
        """按 sequence 获取 event。"""
        for event in self._events:
            if event.get("sequence") == sequence:
                return event
        return None

    def list_events(self) -> list[dict[str, Any]]:
        return list(self._events)
