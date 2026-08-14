"""ProcessAudit — Process Auditor 输出。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P6 节：

Process Auditor：trigger→binding→action→progress→termination 与 first divergence。

单 episode 只陈述观察事实。引用 blinded view by hash。分别 seal。

关键约束（blocker）：
- 复述观察不得当作 action（AU_RESTATE_AS_ACTION）
- 引用 blinded view by hash（AU_VIEW_HASH_MISMATCH）
- 必须 sealed separately（AU_AUDIT_NOT_SEALED_SEPARATELY）
- 单 episode 只陈述观察事实（AU_OBSERVATION_NOT_FACT）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import VerificationErrorCode as EC


_SCHEMA_ID = "seven/process-audit"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class ProcessAudit:
    """Process Auditor 输出——trigger→binding→action→progress→termination 分析。

    字段：
        audit_id: 唯一标识
        plan_id: 对应的 AuditPlan ID
        view_ref: 引用的 blinded view {view_id, view_hash}
        trigger_analysis: trigger 分析（观察事实）
        binding_analysis: binding 分析（观察事实）
        action_analysis: action 分析（观察事实；复述不算 action）
        progress_analysis: progress 分析（观察事实）
        termination_analysis: termination 分析（观察事实）
        first_divergence: 首次分歧分析
        observed_facts: 观察事实列表（单 episode，只陈述事实）
        lane_status: lane 终端状态
        sealed: 是否已 seal
        content_hash: 内容哈希
    """

    audit_id: str
    plan_id: str
    view_ref: dict[str, str] = field(default_factory=dict)
    trigger_analysis: dict[str, Any] = field(default_factory=dict)
    binding_analysis: dict[str, Any] = field(default_factory=dict)
    action_analysis: dict[str, Any] = field(default_factory=dict)
    progress_analysis: dict[str, Any] = field(default_factory=dict)
    termination_analysis: dict[str, Any] = field(default_factory=dict)
    first_divergence: dict[str, Any] = field(default_factory=dict)
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
            "trigger_analysis": dict(self.trigger_analysis),
            "binding_analysis": dict(self.binding_analysis),
            "action_analysis": dict(self.action_analysis),
            "progress_analysis": dict(self.progress_analysis),
            "termination_analysis": dict(self.termination_analysis),
            "first_divergence": dict(self.first_divergence),
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


def make_process_audit(
    *,
    audit_id: str,
    plan_id: str,
    view_ref: dict[str, str],
    trigger_analysis: dict[str, Any] | None = None,
    binding_analysis: dict[str, Any] | None = None,
    action_analysis: dict[str, Any] | None = None,
    progress_analysis: dict[str, Any] | None = None,
    termination_analysis: dict[str, Any] | None = None,
    first_divergence: dict[str, Any] | None = None,
    observed_facts: list[dict[str, Any]] | None = None,
    lane_status: str = "VALID",
    sealed: bool = True,
) -> ProcessAudit:
    audit = ProcessAudit(
        audit_id=audit_id,
        plan_id=plan_id,
        view_ref=view_ref,
        trigger_analysis=trigger_analysis or {},
        binding_analysis=binding_analysis or {},
        action_analysis=action_analysis or {},
        progress_analysis=progress_analysis or {},
        termination_analysis=termination_analysis or {},
        first_divergence=first_divergence or {},
        observed_facts=observed_facts or [],
        lane_status=lane_status,
        sealed=sealed,
    )
    return dataclasses.replace(audit, content_hash=audit.compute_content_hash())


@dataclass(frozen=True)
class ProcessAuditVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    audit_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def _check_restate_as_action(action_analysis: dict[str, Any]) -> bool:
    """检查 action_analysis 中是否把复述观察当作 action。

    复述（restate）= 重复 trajectory 中已有的观察内容，不是新的 action。
    如果 action_analysis 中有 action 标记为 "restate" 或 is_restate=True，
    但又被计为有效 action，则违规。
    """
    actions = action_analysis.get("actions", [])
    if not isinstance(actions, list):
        return False
    for act in actions:
        if not isinstance(act, dict):
            continue
        is_restate = act.get("is_restate", False) or act.get("kind") == "restate"
        counted_as_action = act.get("counted_as_action", True)
        if is_restate and counted_as_action:
            return True
    return False


def _check_observed_facts(facts: list[dict[str, Any]]) -> bool:
    """检查 observed_facts 是否都是观察事实（不含推断/因果 claim）。"""
    for fact in facts:
        if not isinstance(fact, dict):
            return False
        # 观察事实必须有 "observed" 标记为 True，且不含 "causal_claim" 或 "inference"
        if not fact.get("observed", False):
            return False
        if "causal_claim" in fact or "inference" in fact:
            return False
    return True


def verify_process_audit(
    audit: ProcessAudit,
    *,
    expected_view_hash: str | None = None,
) -> ProcessAuditVerificationResult:
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

    # view_hash 一致性
    if expected_view_hash is not None:
        if audit.view_ref.get("view_hash") != expected_view_hash:
            errors.append(EC.AU_VIEW_HASH_MISMATCH)
            details.append(
                f"view_ref.view_hash {audit.view_ref.get('view_hash')} != "
                f"expected {expected_view_hash}"
            )

    # 复述不得当作 action
    if _check_restate_as_action(audit.action_analysis):
        errors.append(EC.AU_RESTATE_AS_ACTION)
        details.append("restate observation counted as action")

    # observed_facts 必须是观察事实
    if audit.observed_facts and not _check_observed_facts(audit.observed_facts):
        errors.append(EC.AU_OBSERVATION_NOT_FACT)
        details.append("observed_facts contains non-observed or causal claim")

    # 必须 sealed
    if not audit.sealed:
        errors.append(EC.AU_AUDIT_NOT_SEALED_SEPARATELY)
        details.append("process audit must be sealed separately")

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
    return ProcessAuditVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        audit_id=audit.audit_id,
    )
