"""EvidenceImmutability — 旧证据不得修改。

来自 docs/implementation/15-work-package-implementation-contracts.md WP-RV1：

READY_FOR_AUDIT最低产物: NO_CHANGE或受控revision纵切，旧证据不改

关键约束（blocker）：
- 旧证据修改 → RV_OLD_EVIDENCE_MODIFIED
- ProvenanceSnapshot 非只读 → RV_PROVENANCE_SNAPSHOT_NOT_READONLY

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC
from ..contracts.completion_contract import VerificationResult


def check_old_evidence_not_modified(
    original_record_hashes: list[str],
    current_record_hashes: list[str],
) -> VerificationResult:
    """检查旧证据未被修改。

    比较 original 和 current 的 EvidenceRecord content_hash 集合。
    任何修改（增删改）都视为旧证据被修改。
    """
    errors: list[EC] = []
    details: list[str] = []
    original_set = set(original_record_hashes)
    current_set = set(current_record_hashes)
    if original_set != current_set:
        errors.append(EC.RV_OLD_EVIDENCE_MODIFIED)
        added = current_set - original_set
        removed = original_set - current_set
        if added:
            details.append(f"records added to sealed evidence: {sorted(added)}")
        if removed:
            details.append(f"records removed from sealed evidence: {sorted(removed)}")
    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_evidence_immutability(
    *,
    provenance_readonly: bool,
    original_record_hashes: list[str],
    current_record_hashes: list[str],
) -> VerificationResult:
    """综合证据不可变性检查。

    blocker：
    - ProvenanceSnapshot 非只读 → RV_PROVENANCE_SNAPSHOT_NOT_READONLY
    - 旧证据修改 → RV_OLD_EVIDENCE_MODIFIED
    """
    errors: list[EC] = []
    details: list[str] = []

    if not provenance_readonly:
        errors.append(EC.RV_PROVENANCE_SNAPSHOT_NOT_READONLY)
        details.append("ProvenanceSnapshot must be readonly — sealed evidence cannot be modified")

    original_set = set(original_record_hashes)
    current_set = set(current_record_hashes)
    if original_set != current_set:
        errors.append(EC.RV_OLD_EVIDENCE_MODIFIED)
        details.append("sealed EvidenceRecord hashes changed — old evidence modified")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
