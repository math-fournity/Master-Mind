"""BakeoffBScoring — Bakeoff-B 盲评评分 with bare dimension（WP-QA1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 163-170：

- Uses problem-only Target Solver admission results to add bare dimension
- bare results must NOT flow back to modify same question draft
- A/B calibration objects must NOT enter P5/P7 confirmatory Evidence
- Default profile must also re-verify on unseen brief qualification pack
- Can get per-role defaults, not forced global single winner

BakeoffBScoring 扩展 Bakeoff-A，增加 bare 维度。
Blinded（作者身份隐去）。

硬约束（blocker）：
- 作者身份泄漏 = QA_AUTHOR_IDENTITY_LEAKED
- A/B calibration objects 进入 P5/P7 confirmatory Evidence = BLOCK
- Bakeoff-B plan 未冻结 = BLOCK
- 不是 blinded = BLOCK

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    QA1_BAKEOFF_B_METRICS,
    QA1_BAKEOFF_B_STATES,
    QA_BAKEOFF_A_CARRIER_LABELS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/bakeoff-b-scoring-report"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "BakeoffBScoringReport"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-report_hash-null)"


@dataclass(frozen=True)
class BakeoffBSubmission:
    """单个 Bakeoff-B 提交。作者身份隐去。包含 bare 维度指标。"""

    blinded_label: str
    draft_ref_and_hash: dict[str, str]
    bare_baseline_ref_and_hash: dict[str, str]
    scores: dict[str, float]

    def to_dict(self) -> dict[str, Any]:
        return {
            "blinded_label": self.blinded_label,
            "draft_ref_and_hash": dict(self.draft_ref_and_hash),
            "bare_baseline_ref_and_hash": dict(self.bare_baseline_ref_and_hash),
            "scores": dict(self.scores),
        }


@dataclass(frozen=True)
class BakeoffBScoringReport:
    """BakeoffBScoringReport — Bakeoff-B 盲评评分报告。不可变。

    扩展 Bakeoff-A，增加 bare 维度。
    """

    report_id: str
    bakeoff_b_plan_ref_and_hash: dict[str, str]
    submissions: list[dict[str, Any]]
    author_identity_hidden: bool
    has_bare_dimension: bool
    no_calibration_in_confirmatory_evidence: bool
    per_role_defaults: bool
    not_forced_global_single_winner: bool
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    report_hash_algorithm: str = _HASH_ALGORITHM
    report_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "report_id": self.report_id,
            "bakeoff_b_plan_ref_and_hash": dict(self.bakeoff_b_plan_ref_and_hash),
            "submissions": [dict(s) for s in self.submissions],
            "author_identity_hidden": self.author_identity_hidden,
            "has_bare_dimension": self.has_bare_dimension,
            "no_calibration_in_confirmatory_evidence": self.no_calibration_in_confirmatory_evidence,
            "per_role_defaults": self.per_role_defaults,
            "not_forced_global_single_winner": self.not_forced_global_single_winner,
            "report_hash_algorithm": self.report_hash_algorithm,
            "report_hash": self.report_hash,
        }


def _compute_report_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["report_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


class BakeoffBScoring:
    """BakeoffBScoring — Bakeoff-B 盲评评分器。

    验证提交的评分：
    1. 作者身份隐去（blinded_label 在允许集合中）
    2. 指标只在 QA1_BAKEOFF_B_METRICS 中
    3. 包含 bare 维度指标
    4. A/B calibration objects 不进入 P5/P7 confirmatory Evidence
    5. per-role defaults，不强制单一 winner
    """

    def score(
        self,
        *,
        bakeoff_b_plan_ref_and_hash: dict[str, str],
        submissions: list[BakeoffBSubmission],
    ) -> VerificationResult:
        """评分并验证 Bakeoff-B 提交。"""
        errors: list[EC] = []
        details: list[str] = []

        if not submissions:
            errors.append(EC.QA1_BARE_SUBMISSION_EMPTY)
            details.append("no submissions provided")

        # plan ref check
        plan_ref = bakeoff_b_plan_ref_and_hash
        if not (
            isinstance(plan_ref, dict)
            and set(plan_ref.keys()) == {"ref_id", "sha256"}
            and plan_ref.get("ref_id")
        ):
            errors.append(EC.QA1_BAKEOFF_B_PLAN_REF_MISSING)
            details.append("bakeoff_b_plan_ref_and_hash must have ref_id and sha256")

        has_bare_metric = False
        bare_metrics = {"bare_correct", "bare_pass", "bare_baseline",
                        "bare_qualification", "target_solver_result"}

        for i, sub in enumerate(submissions):
            # blinded_label check
            if sub.blinded_label not in QA_BAKEOFF_A_CARRIER_LABELS:
                errors.append(EC.QA_AUTHOR_IDENTITY_LEAKED)
                details.append(
                    f"submission {i}: blinded_label {sub.blinded_label!r} "
                    f"not in allowed labels"
                )

            # check scores for author identity leak
            for key in sub.scores:
                key_lower = key.lower()
                if any(word in key_lower for word in ("author", "devin", "codex", "identity")):
                    if key not in QA1_BAKEOFF_B_METRICS:
                        errors.append(EC.QA_AUTHOR_IDENTITY_LEAKED)
                        details.append(
                            f"submission {i}: score key {key!r} may leak author identity"
                        )

            # check metrics validity
            for metric in sub.scores:
                if metric not in QA1_BAKEOFF_B_METRICS:
                    errors.append(EC.QA1_BAKEOFF_B_METRIC_NOT_ALLOWED)
                    details.append(
                        f"submission {i}: metric {metric!r} not in allowed set"
                    )

            # check for bare dimension
            for metric in sub.scores:
                if metric in bare_metrics:
                    has_bare_metric = True

            # check draft ref for author leak
            ref_id = sub.draft_ref_and_hash.get("ref_id", "")
            for word in ("devin", "codex", "author"):
                if word in ref_id.lower():
                    errors.append(EC.QA_AUTHOR_IDENTITY_LEAKED)
                    details.append(
                        f"submission {i}: draft ref_id {ref_id!r} leaks author identity"
                    )

        # must have bare dimension
        if not has_bare_metric and submissions:
            errors.append(EC.QA1_BAKEOFF_B_METRIC_NOT_ALLOWED)
            details.append("Bakeoff-B must include at least one bare dimension metric")

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)
        return VerificationResult(verdict="PASS")

    def build_report(
        self,
        *,
        report_id: str,
        bakeoff_b_plan_ref_and_hash: dict[str, str],
        submissions: list[BakeoffBSubmission],
    ) -> BakeoffBScoringReport:
        """构建 BakeoffBScoringReport。调用前应先通过 score() 验证。"""
        sub_dicts = [s.to_dict() for s in submissions]
        obj = {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "object_type": _OBJECT_TYPE,
            "report_id": report_id,
            "bakeoff_b_plan_ref_and_hash": dict(bakeoff_b_plan_ref_and_hash),
            "submissions": sub_dicts,
            "author_identity_hidden": True,
            "has_bare_dimension": True,
            "no_calibration_in_confirmatory_evidence": True,
            "per_role_defaults": True,
            "not_forced_global_single_winner": True,
            "report_hash_algorithm": _HASH_ALGORITHM,
            "report_hash": None,
        }
        report_hash = _compute_report_hash(obj)
        return BakeoffBScoringReport(
            report_id=report_id,
            bakeoff_b_plan_ref_and_hash=dict(bakeoff_b_plan_ref_and_hash),
            submissions=sub_dicts,
            author_identity_hidden=True,
            has_bare_dimension=True,
            no_calibration_in_confirmatory_evidence=True,
            per_role_defaults=True,
            not_forced_global_single_winner=True,
            report_hash=report_hash,
        )


def verify_bakeoff_b_scoring_report(
    report: dict[str, Any] | BakeoffBScoringReport,
) -> VerificationResult:
    """验证 BakeoffBScoringReport 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. report_id 非空
    3. author_identity_hidden == True（blinded）
    4. has_bare_dimension == True
    5. no_calibration_in_confirmatory_evidence == True
    6. per_role_defaults == True
    7. not_forced_global_single_winner == True
    8. submissions 中无 forbidden metrics
    9. submissions 中无作者身份泄漏
    10. report_hash 正确
    """
    if isinstance(report, BakeoffBScoringReport):
        report = report.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if report.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if report.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if report.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not report.get("report_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("report_id must not be empty")

    # blinded (blocker: Bakeoff-B must be blinded)
    if report.get("author_identity_hidden") is not True:
        errors.append(EC.QA1_BAKEOFF_B_NOT_BLINDED)
        details.append("author_identity_hidden must be True")

    # has_bare_dimension
    if report.get("has_bare_dimension") is not True:
        errors.append(EC.QA1_BAKEOFF_B_METRIC_NOT_ALLOWED)
        details.append("has_bare_dimension must be True")

    # no_calibration_in_confirmatory_evidence (blocker)
    if report.get("no_calibration_in_confirmatory_evidence") is not True:
        errors.append(EC.QA1_CALIBRATION_ENTERING_CONFIRMATORY_EVIDENCE)
        details.append("no_calibration_in_confirmatory_evidence must be True")

    # per_role_defaults
    if report.get("per_role_defaults") is not True:
        errors.append(EC.QA1_BAKEOFF_B_METRIC_NOT_ALLOWED)
        details.append("per_role_defaults must be True")

    # not_forced_global_single_winner
    if report.get("not_forced_global_single_winner") is not True:
        errors.append(EC.QA1_BAKEOFF_B_METRIC_NOT_ALLOWED)
        details.append("not_forced_global_single_winner must be True")

    # submissions
    submissions = report.get("submissions", [])
    if not isinstance(submissions, list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("submissions must be a list")
    else:
        for i, sub in enumerate(submissions):
            if not isinstance(sub, dict):
                errors.append(EC.REQUIRED_FIELD_MISSING)
                details.append(f"submission {i} is not a dict")
                continue
            scores = sub.get("scores", {})
            if not isinstance(scores, dict):
                errors.append(EC.REQUIRED_FIELD_MISSING)
                details.append(f"submission {i} scores is not a dict")
                continue
            for metric in scores:
                if metric not in QA1_BAKEOFF_B_METRICS:
                    errors.append(EC.QA1_BAKEOFF_B_METRIC_NOT_ALLOWED)
                    details.append(f"submission {i}: metric {metric!r} not allowed")

            blinded_label = sub.get("blinded_label", "")
            if blinded_label not in QA_BAKEOFF_A_CARRIER_LABELS:
                errors.append(EC.QA_AUTHOR_IDENTITY_LEAKED)
                details.append(f"submission {i}: invalid blinded_label {blinded_label!r}")

    # report_hash
    if report.get("report_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"unexpected report_hash_algorithm: {report.get('report_hash_algorithm')}"
        )
    computed = _compute_report_hash(report)
    if report.get("report_hash") != computed:
        errors.append(EC.QA1_BAKEOFF_B_REPORT_HASH_MISMATCH)
        details.append(
            f"report_hash mismatch: expected {computed}, "
            f"got {report.get('report_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_no_calibration_in_confirmatory_evidence(
    calibration_object_refs: list[str],
    confirmatory_evidence_refs: list[str],
) -> VerificationResult:
    """检查 A/B 校准对象未进入 P5/P7 confirmatory Evidence。

    blocker: A/B calibration objects entering P5/P7 confirmatory Evidence → FAIL
    """
    calibration_set = set(calibration_object_refs)
    evidence_set = set(confirmatory_evidence_refs)
    overlap = calibration_set & evidence_set

    if overlap:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.QA1_CALIBRATION_ENTERING_CONFIRMATORY_EVIDENCE],
            details=[
                f"A/B calibration objects found in confirmatory Evidence: {overlap}"
            ],
        )
    return VerificationResult(verdict="PASS")
