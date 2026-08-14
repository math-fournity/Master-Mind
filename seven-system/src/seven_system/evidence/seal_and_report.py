"""EvidenceSeal + EvidenceCapabilityReport — P7 seal 与能力报告。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P7 节：

P7 唯一阶段输出是 sealed EvidenceRecord 集合及其 seal/root hash；
它不生成 EvidenceIndex 或 ProvenanceSnapshot。P8 开始时才对该 sealed 集合
冻结只读 ProvenanceSnapshot，最终 EvidenceIndex 仅由 P9 生成。

关键约束（blocker）：
- EvidenceIndex 在 P7 生成 → BLOCK（EV_EVIDENCE_INDEX_GENERATED_IN_P7）
- ProvenanceSnapshot 在 P7 生成 → BLOCK（EV_PROVENANCE_SNAPSHOT_GENERATED_IN_P7）
- seal hash 不匹配 → BLOCK（EV_EVIDENCE_SEAL_HASH_MISMATCH）
- seal 不完整 → BLOCK（EV_SEAL_INCOMPLETE）
- missing/multiplicity/cost 不完整 → BLOCK

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    EV_ALLOWED_OUTPUT_KINDS,
    EV_CHECK_IDS,
    EV_CLAIMS,
    EV_FORBIDDEN_OUTPUT_KINDS,
    EV_NONCLAIMS,
    EV_SIDE_EFFECT_KEYS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult
from .evidence_record import EvidenceRecord, verify_evidence_record


_SCHEMA_ID = "seven/evidence-seal"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


# ─── EvidenceSeal ───────────────────────────────────────────────────────


@dataclass(frozen=True)
class EvidenceSeal:
    """P7 seal over EvidenceRecord 集合——root hash + seal hash。

    P7 唯一阶段输出。不生成 EvidenceIndex 或 ProvenanceSnapshot。

    字段：
        seal_id: 唯一标识
        plan_id: 对应的 ExperimentPlan ID
        record_hashes: 所有 EvidenceRecord 的 content_hash 列表（有序）
        root_hash: root hash（所有 record hash 的 merkle/排序哈希）
        seal_hash: seal hash（对 seal 元数据 + root_hash 的哈希）
        record_count: record 数量
        sealed_at: seal 时间
        hash_algorithm: 哈希算法
        content_hash: seal 自身内容哈希
    """

    seal_id: str
    plan_id: str
    record_hashes: tuple[str, ...] = ()
    root_hash: str = ""
    seal_hash: str = ""
    record_count: int = 0
    sealed_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "seal_id": self.seal_id,
            "plan_id": self.plan_id,
            "record_hashes": list(self.record_hashes),
            "root_hash": self.root_hash,
            "seal_hash": self.seal_hash,
            "record_count": self.record_count,
            "sealed_at": self.sealed_at,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


def compute_root_hash(record_hashes: list[str]) -> str:
    """计算 root hash——所有 record hash 的排序哈希。"""
    sorted_hashes = sorted(record_hashes)
    return hashlib.sha256(canonical_json_bytes(sorted_hashes)).hexdigest()


def compute_seal_hash(seal_id: str, plan_id: str, root_hash: str, sealed_at: str) -> str:
    """计算 seal hash——对 seal 元数据 + root_hash 的哈希。"""
    payload = {
        "seal_id": seal_id,
        "plan_id": plan_id,
        "root_hash": root_hash,
        "sealed_at": sealed_at,
    }
    return hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def make_evidence_seal(
    *,
    seal_id: str,
    plan_id: str,
    records: list[EvidenceRecord],
    sealed_at: str | None = None,
) -> EvidenceSeal:
    """构建 EvidenceSeal——对 EvidenceRecord 集合 seal。

    计算 root hash（所有 record hash 排序哈希）和 seal hash。
    """
    sealed_at = sealed_at or datetime.now(timezone.utc).isoformat()
    record_hashes = tuple(sorted(r.content_hash for r in records))
    root_hash = compute_root_hash(list(record_hashes))
    seal_hash = compute_seal_hash(seal_id, plan_id, root_hash, sealed_at)

    seal = EvidenceSeal(
        seal_id=seal_id,
        plan_id=plan_id,
        record_hashes=record_hashes,
        root_hash=root_hash,
        seal_hash=seal_hash,
        record_count=len(records),
        sealed_at=sealed_at,
    )
    return dataclasses.replace(seal, content_hash=seal.compute_content_hash())


@dataclass(frozen=True)
class EvidenceSealVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    seal_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_evidence_seal(
    seal: EvidenceSeal,
    *,
    records: list[EvidenceRecord] | None = None,
) -> EvidenceSealVerificationResult:
    """验证 EvidenceSeal。

    blocker：
    - seal hash 不匹配 → EV_EVIDENCE_SEAL_HASH_MISMATCH
    - root hash 不匹配 → EV_SEAL_ROOT_HASH_MISMATCH
    - seal 不完整（无 records）→ EV_SEAL_INCOMPLETE
    - record hash 不在 seal 中 → EV_SEAL_INCOMPLETE
    """
    errors: list[EC] = []
    details: list[str] = []

    d = seal.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not seal.seal_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("seal_id is empty")

    if not seal.plan_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("plan_id is empty")

    # seal 不完整
    if seal.record_count == 0 or not seal.record_hashes:
        errors.append(EC.EV_SEAL_INCOMPLETE)
        details.append("EvidenceSeal has no records — incomplete")

    # root hash 验证
    expected_root = compute_root_hash(list(seal.record_hashes))
    if seal.root_hash != expected_root:
        errors.append(EC.EV_SEAL_ROOT_HASH_MISMATCH)
        details.append(
            f"root_hash mismatch: claims {seal.root_hash}, computed {expected_root}"
        )

    # seal hash 验证
    expected_seal = compute_seal_hash(
        seal.seal_id, seal.plan_id, seal.root_hash, seal.sealed_at
    )
    if seal.seal_hash != expected_seal:
        errors.append(EC.EV_EVIDENCE_SEAL_HASH_MISMATCH)
        details.append(
            f"seal_hash mismatch: claims {seal.seal_hash}, computed {expected_seal}"
        )

    # record count 一致
    if seal.record_count != len(seal.record_hashes):
        errors.append(EC.EV_SEAL_INCOMPLETE)
        details.append(
            f"record_count {seal.record_count} != len(record_hashes) {len(seal.record_hashes)}"
        )

    # 如果提供了 records，检查所有 record hash 都在 seal 中
    if records is not None:
        seal_hash_set = set(seal.record_hashes)
        for r in records:
            if r.content_hash not in seal_hash_set:
                errors.append(EC.EV_SEAL_INCOMPLETE)
                details.append(
                    f"record {r.record_id} hash {r.content_hash} not in seal"
                )

    # content_hash
    if not seal.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif seal.content_hash != seal.compute_content_hash():
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append("EvidenceSeal content_hash mismatch")

    verdict = "PASS" if not errors else "FAIL"
    return EvidenceSealVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        seal_id=seal.seal_id,
    )


# ─── P7 边界检查 ────────────────────────────────────────────────────────


def check_no_evidence_index_in_p7(outputs: dict[str, Any]) -> VerificationResult:
    """检查 P7 输出中不含 EvidenceIndex。"""
    errors: list[EC] = []
    details: list[str] = []

    for key, value in outputs.items():
        kind = value.get("report_kind", value.get("schema_id", "")) if isinstance(value, dict) else ""
        if kind == "EvidenceIndex" or key == "EvidenceIndex":
            errors.append(EC.EV_EVIDENCE_INDEX_GENERATED_IN_P7)
            details.append("EvidenceIndex generated in P7 — only P9 generates it")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_no_provenance_snapshot_in_p7(outputs: dict[str, Any]) -> VerificationResult:
    """检查 P7 输出中不含 ProvenanceSnapshot。"""
    errors: list[EC] = []
    details: list[str] = []

    for key, value in outputs.items():
        kind = value.get("report_kind", value.get("schema_id", "")) if isinstance(value, dict) else ""
        if kind == "ProvenanceSnapshot" or key == "ProvenanceSnapshot":
            errors.append(EC.EV_PROVENANCE_SNAPSHOT_GENERATED_IN_P7)
            details.append("ProvenanceSnapshot generated in P7 — only P8 freezes it")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_p7_output_boundary(outputs: dict[str, Any]) -> VerificationResult:
    """检查 P7 输出边界——只允许 EV_ALLOWED_OUTPUT_KINDS。"""
    errors: list[EC] = []
    details: list[str] = []

    for key, value in outputs.items():
        kind = ""
        if isinstance(value, dict):
            kind = value.get("report_kind", value.get("schema_id", ""))
        if not kind:
            kind = key
        # 去掉 schema_id 前缀
        if kind.startswith("seven/"):
            kind = kind.split("/")[-1]
        if kind in EV_FORBIDDEN_OUTPUT_KINDS:
            errors.append(EC.EV_OUTPUT_KIND_FORBIDDEN)
            details.append(f"P7 must not produce {kind}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


# ─── EvidenceCapabilityReport ───────────────────────────────────────────


EVIDENCE_REPORT_SCHEMA_VERSION = "ev1-evidence-capability-report/v1"
EVIDENCE_REPORT_SCOPE = "EVIDENCE_CAPABILITY_V1"


class EvidenceCapabilityReportError(ValueError):
    """报告输入或语义验证不满足 WP-EV1。"""


def _valid_generated_at(value: object) -> bool:
    if not isinstance(value, str) or any(c in value for c in "\r\n\x00"):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _sha256_hex(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(c in "0123456789abcdef" for c in value)
    )


def build_evidence_capability_report(
    *,
    plan_hash: str,
    analysis_registry_hash: str,
    multiplicity_registry_hash: str,
    stopping_registry_hash: str,
    status_registry_hash: str,
    contrast_count: int,
    evidence_record_count: int,
    evidence_seal_hash: str,
    evidence_seal_root_hash: str,
    missingness_complete: bool,
    multiplicity_complete: bool,
    cost_complete: bool,
    randomized_contrast_replay: bool,
    all_records_sealed: bool,
    no_evidence_index: bool,
    no_provenance_snapshot: bool,
    verifier_identity: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """构造 EvidenceCapabilityReport。

    READY_FOR_AUDIT 最低产物：随机对照重放、missing/multiplicity/cost 完整。
    """
    report: dict[str, Any] = {
        "schema_version": EVIDENCE_REPORT_SCHEMA_VERSION,
        "report_kind": "EvidenceCapabilityReport",
        "scope": EVIDENCE_REPORT_SCOPE,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "plan_hash": plan_hash,
        "analysis_registry_hash": analysis_registry_hash,
        "multiplicity_registry_hash": multiplicity_registry_hash,
        "stopping_registry_hash": stopping_registry_hash,
        "status_registry_hash": status_registry_hash,
        "contrast_count": contrast_count,
        "evidence_record_count": evidence_record_count,
        "evidence_seal_hash": evidence_seal_hash,
        "evidence_seal_root_hash": evidence_seal_root_hash,
        "missingness_complete": missingness_complete,
        "multiplicity_complete": multiplicity_complete,
        "cost_complete": cost_complete,
        "randomized_contrast_replay": randomized_contrast_replay,
        "all_records_sealed": all_records_sealed,
        "no_evidence_index_in_p7": no_evidence_index,
        "no_provenance_snapshot_in_p7": no_provenance_snapshot,
        "verdict": "PASS",
        "verifier_identity": verifier_identity,
        "checks": [
            {"check_id": cid, "verdict": "PASS", "evidence": []}
            for cid in EV_CHECK_IDS
        ],
        "claims": {claim: True for claim in EV_CLAIMS},
        "side_effects": {key: 0 for key in EV_SIDE_EFFECT_KEYS},
        "blockers": [],
        "explicit_nonclaims": list(EV_NONCLAIMS),
    }

    errors = verify_evidence_capability_report(report)
    if errors:
        raise EvidenceCapabilityReportError(
            "generated report failed verification: "
            + "; ".join(f"{e[0]}:{e[1]}" for e in errors)
        )
    return report


def verify_evidence_capability_report(
    report: object,
) -> tuple[tuple[EC, str], ...]:
    """语义验证 EvidenceCapabilityReport。"""
    errors: list[tuple[EC, str]] = []

    if not isinstance(report, dict):
        return ((EC.REQUIRED_FIELD_MISSING, "report root must be an object"),)

    # schema_version
    if report.get("schema_version") != EVIDENCE_REPORT_SCHEMA_VERSION:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"schema_version must be {EVIDENCE_REPORT_SCHEMA_VERSION}",
        ))

    # report_kind
    rk = report.get("report_kind", "")
    if rk != "EvidenceCapabilityReport":
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "report_kind must be EvidenceCapabilityReport",
        ))

    # boundary check: must not be other WP's output
    if rk in EV_FORBIDDEN_OUTPUT_KINDS:
        errors.append((
            EC.EV_OUTPUT_KIND_FORBIDDEN,
            f"EV1 must not produce {rk}",
        ))

    # scope
    if report.get("scope") != EVIDENCE_REPORT_SCOPE:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            f"scope must be {EVIDENCE_REPORT_SCOPE}",
        ))

    # generated_at
    if not _valid_generated_at(report.get("generated_at")):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "generated_at is not a timezone-aware ISO-8601 timestamp",
        ))

    # hashes
    for field_name in (
        "plan_hash", "analysis_registry_hash", "multiplicity_registry_hash",
        "stopping_registry_hash", "status_registry_hash",
        "evidence_seal_hash", "evidence_seal_root_hash",
    ):
        val = report.get(field_name)
        if not _sha256_hex(val):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a lowercase sha256 hex",
            ))

    # counts must be non-negative integers
    for field_name in ("contrast_count", "evidence_record_count"):
        val = report.get(field_name)
        if not isinstance(val, int) or val < 0:
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                f"{field_name} must be a non-negative integer",
            ))

    # completeness flags
    if report.get("missingness_complete") is not True:
        errors.append((EC.EV_MISSINGNESS_INCOMPLETE, "missingness_complete must be True"))
    if report.get("multiplicity_complete") is not True:
        errors.append((EC.EV_MULTIPLICITY_INCOMPLETE, "multiplicity_complete must be True"))
    if report.get("cost_complete") is not True:
        errors.append((EC.EV_COST_INCOMPLETE, "cost_complete must be True"))

    # randomized contrast replay
    if report.get("randomized_contrast_replay") is not True:
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "randomized_contrast_replay must be True",
        ))

    # all records sealed
    if report.get("all_records_sealed") is not True:
        errors.append((EC.EV_EVIDENCE_RECORD_NOT_SEALED, "all_records_sealed must be True"))

    # boundary flags
    if report.get("no_evidence_index_in_p7") is not True:
        errors.append((
            EC.EV_EVIDENCE_INDEX_GENERATED_IN_P7,
            "no_evidence_index_in_p7 must be True",
        ))
    if report.get("no_provenance_snapshot_in_p7") is not True:
        errors.append((
            EC.EV_PROVENANCE_SNAPSHOT_GENERATED_IN_P7,
            "no_provenance_snapshot_in_p7 must be True",
        ))

    # checks
    checks = report.get("checks")
    if not isinstance(checks, list):
        errors.append((EC.REQUIRED_FIELD_MISSING, "checks must be an array"))
    else:
        check_ids = [c.get("check_id") if isinstance(c, dict) else None for c in checks]
        if not all(isinstance(cid, str) for cid in check_ids):
            errors.append((EC.REQUIRED_FIELD_MISSING, "every check ID must be a string"))
        elif len(check_ids) != len(set(check_ids)):
            errors.append((EC.REQUIRED_FIELD_MISSING, "check IDs must not contain duplicates"))
        elif check_ids != list(EV_CHECK_IDS):
            errors.append((
                EC.REQUIRED_FIELD_MISSING,
                "checks must exactly match canonical IDs and order",
            ))
        for c in checks:
            if isinstance(c, dict) and c.get("verdict") != "PASS":
                errors.append((EC.REQUIRED_FIELD_MISSING, "every EV1 check must be PASS"))

    # claims
    claims = report.get("claims")
    if not isinstance(claims, dict) or set(claims) != set(EV_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "claim set does not exactly match EV1 claims"))
    elif any(claims[c] is not True for c in EV_CLAIMS):
        errors.append((EC.REQUIRED_FIELD_MISSING, "all EV1 claims must be true"))

    # side_effects
    side_effects = report.get("side_effects")
    if not isinstance(side_effects, dict) or set(side_effects) != set(EV_SIDE_EFFECT_KEYS):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "side-effect set does not match the EV1 report scope",
        ))
    elif any(side_effects[k] != 0 for k in EV_SIDE_EFFECT_KEYS):
        errors.append((EC.EV_OUTPUT_KIND_FORBIDDEN, "all EV1 report side effects must be zero"))

    # verdict
    if report.get("verdict") != "PASS":
        errors.append((EC.REQUIRED_FIELD_MISSING, "EV1 report verdict must be PASS"))

    # blockers
    if report.get("blockers") != []:
        errors.append((EC.REQUIRED_FIELD_MISSING, "PASS EV1 report must have no blockers"))

    # explicit_nonclaims
    nonclaims = report.get("explicit_nonclaims")
    if (
        not isinstance(nonclaims, list)
        or not all(isinstance(item, str) for item in nonclaims)
        or len(nonclaims) != len(set(nonclaims))
        or set(nonclaims) != set(EV_NONCLAIMS)
    ):
        errors.append((
            EC.REQUIRED_FIELD_MISSING,
            "explicit nonclaims must preserve the EV1 boundary",
        ))

    return tuple(dict.fromkeys(errors))
