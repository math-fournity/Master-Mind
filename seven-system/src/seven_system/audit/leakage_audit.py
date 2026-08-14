"""LeakageAudit — Leakage Auditor 输出。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P6 节：

Leakage Auditor：完整 Solver payload 与 solution information atoms。

单 episode 只陈述观察事实。引用 blinded view by hash。分别 seal。

关键约束（blocker）：
- 引用 blinded view by hash（AU_VIEW_HASH_MISMATCH）
- 必须 sealed separately（AU_AUDIT_NOT_SEALED_SEPARATELY）
- 污染必须被标记（AU_CONTAMINATION_NOT_FLAGGED）
- 超预注册 leakage budget 必须被标记（AU_LEAKAGE_BUDGET_EXCEEDED）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


_SCHEMA_ID = "seven/leakage-audit"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class LeakageAudit:
    """Leakage Auditor 输出——完整 Solver payload 与 solution information atoms 分析。

    字段：
        audit_id: 唯一标识
        plan_id: 对应的 AuditPlan ID
        view_ref: 引用的 blinded view {view_id, view_hash}
        solver_payload_analysis: Solver payload 分析
        solution_information_atoms: solution information atoms 分析
        leakage_budget_check: leakage budget 检查
        contamination_flagged: 是否标记污染
        observed_facts: 观察事实列表（单 episode，只陈述事实）
        lane_status: lane 终端状态
        sealed: 是否已 seal
        content_hash: 内容哈希
    """

    audit_id: str
    plan_id: str
    view_ref: dict[str, str] = field(default_factory=dict)
    solver_payload_analysis: dict[str, Any] = field(default_factory=dict)
    solution_information_atoms: list[dict[str, Any]] = field(default_factory=list)
    leakage_budget_check: dict[str, Any] = field(default_factory=dict)
    contamination_flagged: bool = False
    observed_facts: list[dict[str, Any]] = field(default_factory=list)
    lane_status: str = "VALID"
    sealed: bool = False
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "audit_id": self.audit_id,
            "plan_id": self.plan_id,
            "view_ref": dict(self.view_ref),
            "solver_payload_analysis": dict(self.solver_payload_analysis),
            "solution_information_atoms": [dict(a) for a in self.solution_information_atoms],
            "leakage_budget_check": dict(self.leakage_budget_check),
            "contamination_flagged": self.contamination_flagged,
            "observed_facts": [dict(f) for f in self.observed_facts],
            "lane_status": self.lane_status,
            "sealed": self.sealed,
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


def make_leakage_audit(
    *,
    audit_id: str,
    plan_id: str,
    view_ref: dict[str, str],
    solver_payload_analysis: dict[str, Any] | None = None,
    solution_information_atoms: list[dict[str, Any]] | None = None,
    leakage_budget_check: dict[str, Any] | None = None,
    contamination_flagged: bool = False,
    observed_facts: list[dict[str, Any]] | None = None,
    lane_status: str = "VALID",
    sealed: bool = True,
) -> LeakageAudit:
    audit = LeakageAudit(
        audit_id=audit_id,
        plan_id=plan_id,
        view_ref=view_ref,
        solver_payload_analysis=solver_payload_analysis or {},
        solution_information_atoms=solution_information_atoms or [],
        leakage_budget_check=leakage_budget_check or {},
        contamination_flagged=contamination_flagged,
        observed_facts=observed_facts or [],
        lane_status=lane_status,
        sealed=sealed,
    )
    return dataclasses.replace(audit, content_hash=audit.compute_content_hash())


@dataclass(frozen=True)
class LeakageAuditVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    audit_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_leakage_audit(
    audit: LeakageAudit,
    *,
    expected_view_hash: str | None = None,
    leakage_budget_limit: int | None = None,
) -> LeakageAuditVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = audit.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if not audit.audit_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("audit_id is empty")

    if not audit.plan_id:
        errors.append(EC.AU_AUDIT_PLAN_REF_MISSING)
        details.append("plan_id is empty")

    # view_ref required
    if not audit.view_ref.get("view_id"):
        errors.append(EC.AU_VIEW_REF_MISSING)
        details.append("view_ref missing view_id")
    if not audit.view_ref.get("view_hash"):
        errors.append(EC.AU_VIEW_REF_MISSING)
        details.append("view_ref missing view_hash")

    if expected_view_hash is not None:
        if audit.view_ref.get("view_hash") != expected_view_hash:
            errors.append(EC.AU_VIEW_HASH_MISMATCH)
            details.append(
                f"view_ref.view_hash {audit.view_ref.get('view_hash')} != "
                f"expected {expected_view_hash}"
            )

    # 污染必须被标记
    contamination_detected = audit.solver_payload_analysis.get("contamination_detected", False)
    if contamination_detected and not audit.contamination_flagged:
        errors.append(EC.AU_CONTAMINATION_NOT_FLAGGED)
        details.append("contamination detected but not flagged")

    # leakage budget 检查
    if leakage_budget_limit is not None:
        atoms_count = len(audit.solution_information_atoms)
        if atoms_count > leakage_budget_limit:
            if not audit.leakage_budget_check.get("exceeded", False):
                errors.append(EC.AU_LEAKAGE_BUDGET_EXCEEDED)
                details.append(
                    f"leakage atoms {atoms_count} > budget {leakage_budget_limit} "
                    f"but not flagged as exceeded"
                )

    # observed_facts 必须是观察事实
    for fact in audit.observed_facts:
        if not isinstance(fact, dict) or not fact.get("observed", False):
            errors.append(EC.AU_OBSERVATION_NOT_FACT)
            details.append("observed_facts contains non-observed fact")
            break

    # 必须 sealed
    if not audit.sealed:
        errors.append(EC.AU_AUDIT_NOT_SEALED_SEPARATELY)
        details.append("leakage audit must be sealed separately")

    # content_hash
    if not audit.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif audit.content_hash != audit.compute_content_hash():
        errors.append(EC.AU_SEAL_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {audit.content_hash}, "
            f"computed {audit.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return LeakageAuditVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        audit_id=audit.audit_id,
    )
