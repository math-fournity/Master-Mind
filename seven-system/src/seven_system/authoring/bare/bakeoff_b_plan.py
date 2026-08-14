"""BakeoffBPlan — Bakeoff-B 冻结计划（WP-QA1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 163-170：

- Only uses A-stage already human-released, immutable calibration QuestionRelease
- Uses problem-only Target Solver admission results to add bare dimension
- bare results must NOT flow back to modify same question draft
- A/B calibration objects must NOT enter P5/P7 confirmatory Evidence
- Default profile must also re-verify on unseen brief qualification pack
- Can get per-role defaults, not forced global single winner

BakeoffBPlan 是冻结的 Bakeoff-B 计划：哪些 QuestionReleases、哪些 profiles、
哪些 metrics、stop conditions。引用 Bakeoff-A results。

硬约束：
- 计划必须冻结（frozen == True）
- 必须引用 Bakeoff-A results
- A/B calibration objects 不得进入 P5/P7 confirmatory Evidence

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    QA1_BAKEOFF_B_METRICS,
    QA1_BAKEOFF_B_STATES,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/bakeoff-b-plan"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "BakeoffBPlan"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-plan_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class BakeoffBPlan:
    """BakeoffBPlan — Bakeoff-B 冻结计划。不可变。

    字段：
    - plan_id：计划 ID
    - bakeoff_a_ref_and_hash：Bakeoff-A results 引用 + sha256
    - question_release_refs：参与的 QuestionRelease 引用列表
    - profile_labels：参与的 profile 标签列表（per-role defaults）
    - metrics：评估指标列表（QA1_BAKEOFF_B_METRICS 子集）
    - stop_conditions：停止条件
    - frozen：是否冻结（必须为 True）
    - no_calibration_in_confirmatory_evidence：A/B 校准对象不得进入 P5/P7
    - per_role_defaults：是否 per-role defaults（不强制单一 winner）
    - reverify_on_unseen_qualification_pack：是否在未见资格包上重新验证
    """

    plan_id: str
    bakeoff_a_ref_and_hash: dict[str, str]
    question_release_refs: list[dict[str, str]]
    profile_labels: list[str]
    metrics: list[str]
    stop_conditions: dict[str, Any]
    frozen: bool
    no_calibration_in_confirmatory_evidence: bool
    per_role_defaults: bool
    reverify_on_unseen_qualification_pack: bool
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    plan_hash_algorithm: str = _HASH_ALGORITHM
    plan_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "plan_id": self.plan_id,
            "bakeoff_a_ref_and_hash": dict(self.bakeoff_a_ref_and_hash),
            "question_release_refs": [dict(r) for r in self.question_release_refs],
            "profile_labels": list(self.profile_labels),
            "metrics": list(self.metrics),
            "stop_conditions": dict(self.stop_conditions),
            "frozen": self.frozen,
            "no_calibration_in_confirmatory_evidence": self.no_calibration_in_confirmatory_evidence,
            "per_role_defaults": self.per_role_defaults,
            "reverify_on_unseen_qualification_pack": self.reverify_on_unseen_qualification_pack,
            "plan_hash_algorithm": self.plan_hash_algorithm,
            "plan_hash": self.plan_hash,
        }


def _compute_plan_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["plan_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def _ref_and_hash_valid(obj: Any) -> bool:
    return (
        isinstance(obj, dict)
        and set(obj.keys()) == {"ref_id", "sha256"}
        and isinstance(obj.get("ref_id"), str)
        and bool(obj.get("ref_id"))
        and isinstance(obj.get("sha256"), str)
        and bool(_HASH_RE.match(obj.get("sha256", "")))
    )


def build_bakeoff_b_plan(
    *,
    plan_id: str,
    bakeoff_a_ref_id: str,
    bakeoff_a_sha256: str,
    question_release_refs: list[dict[str, str]],
    profile_labels: list[str],
    metrics: list[str],
    stop_conditions: dict[str, Any] | None = None,
    per_role_defaults: bool = True,
    reverify_on_unseen_qualification_pack: bool = True,
) -> BakeoffBPlan:
    """构建 BakeoffBPlan，自动计算 plan_hash。

    frozen 固定为 True（计划必须冻结）。
    no_calibration_in_confirmatory_evidence 固定为 True。
    """
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "plan_id": plan_id,
        "bakeoff_a_ref_and_hash": {
            "ref_id": bakeoff_a_ref_id,
            "sha256": bakeoff_a_sha256,
        },
        "question_release_refs": [dict(r) for r in question_release_refs],
        "profile_labels": list(profile_labels),
        "metrics": list(metrics),
        "stop_conditions": dict(stop_conditions) if stop_conditions else {},
        "frozen": True,
        "no_calibration_in_confirmatory_evidence": True,
        "per_role_defaults": per_role_defaults,
        "reverify_on_unseen_qualification_pack": reverify_on_unseen_qualification_pack,
        "plan_hash_algorithm": _HASH_ALGORITHM,
        "plan_hash": None,
    }
    plan_hash = _compute_plan_hash(obj)
    return BakeoffBPlan(
        plan_id=plan_id,
        bakeoff_a_ref_and_hash={
            "ref_id": bakeoff_a_ref_id,
            "sha256": bakeoff_a_sha256,
        },
        question_release_refs=[dict(r) for r in question_release_refs],
        profile_labels=list(profile_labels),
        metrics=list(metrics),
        stop_conditions=dict(stop_conditions) if stop_conditions else {},
        frozen=True,
        no_calibration_in_confirmatory_evidence=True,
        per_role_defaults=per_role_defaults,
        reverify_on_unseen_qualification_pack=reverify_on_unseen_qualification_pack,
        plan_hash=plan_hash,
    )


def verify_bakeoff_b_plan(
    plan: dict[str, Any] | BakeoffBPlan,
) -> VerificationResult:
    """验证 BakeoffBPlan 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. plan_id 非空
    3. bakeoff_a_ref_and_hash 存在且结构合法
    4. frozen == True（计划必须冻结）
    5. no_calibration_in_confirmatory_evidence == True
    6. metrics 都在 QA1_BAKEOFF_B_METRICS 中
    7. question_release_refs 非空且结构合法
    8. plan_hash 正确
    """
    if isinstance(plan, BakeoffBPlan):
        plan = plan.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if plan.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if plan.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if plan.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not plan.get("plan_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("plan_id must not be empty")

    # bakeoff_a_ref_and_hash (blocker: missing ref)
    a_ref = plan.get("bakeoff_a_ref_and_hash", {})
    if not _ref_and_hash_valid(a_ref):
        errors.append(EC.QA1_BAKEOFF_A_REF_MISSING)
        details.append(
            "bakeoff_a_ref_and_hash must have ref_id and sha256"
        )

    # frozen (blocker: plan must be frozen)
    if plan.get("frozen") is not True:
        errors.append(EC.QA1_BAKEOFF_B_PLAN_NOT_FROZEN)
        details.append("frozen must be True")

    # no_calibration_in_confirmatory_evidence (blocker)
    if plan.get("no_calibration_in_confirmatory_evidence") is not True:
        errors.append(EC.QA1_CALIBRATION_ENTERING_CONFIRMATORY_EVIDENCE)
        details.append("no_calibration_in_confirmatory_evidence must be True")

    # metrics
    metrics = plan.get("metrics", [])
    if not isinstance(metrics, list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("metrics must be a list")
    else:
        for metric in metrics:
            if metric not in QA1_BAKEOFF_B_METRICS:
                errors.append(EC.QA1_BAKEOFF_B_METRIC_NOT_ALLOWED)
                details.append(f"metric {metric!r} not in QA1_BAKEOFF_B_METRICS")

    # question_release_refs
    release_refs = plan.get("question_release_refs", [])
    if not isinstance(release_refs, list) or not release_refs:
        errors.append(EC.QA1_QUESTION_RELEASE_REF_MISSING)
        details.append("question_release_refs must be a non-empty list")
    else:
        for i, ref in enumerate(release_refs):
            if not _ref_and_hash_valid(ref):
                errors.append(EC.QA1_QUESTION_RELEASE_REF_MISSING)
                details.append(
                    f"question_release_refs[{i}] must have ref_id and sha256"
                )

    # plan_hash
    if plan.get("plan_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"unexpected plan_hash_algorithm: {plan.get('plan_hash_algorithm')}"
        )
    computed = _compute_plan_hash(plan)
    if plan.get("plan_hash") != computed:
        errors.append(EC.QA1_BAKEOFF_B_PLAN_HASH_MISMATCH)
        details.append(
            f"plan_hash mismatch: expected {computed}, "
            f"got {plan.get('plan_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
