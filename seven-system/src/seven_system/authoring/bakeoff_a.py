"""BakeoffAScoring — Bakeoff-A 盲评评分。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 155-161：

- 同一 MechanismContract, CoverageCell, AuthoringBrief 和 budget
- Devin glm-5-2 High, Codex candidate 和可选其他 profile 分别生成
- 作者身份隐去（blinded）
- 只评估：math correct, mechanism faithful, orthogonal distance,
  shortcut/leakage, diversity, human revision amount, cost
- 无 Target Solver launch, 无 bare results

硬约束（blocker）：
- 作者身份泄漏 = QA_AUTHOR_IDENTITY_LEAKED
- bare 指标偷入 = QA_BARE_METRIC_SNEAKED / QA_BAKEOFF_A_USING_BARE
- 无 Solver, 无 Redis

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    QA_BAKEOFF_A_METRICS,
    QA_BAKEOFF_A_FORBIDDEN_METRICS,
    QA_BAKEOFF_A_CARRIER_LABELS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/bakeoff-a-scoring-report"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "BakeoffAScoringReport"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-report_hash-null)"


@dataclass(frozen=True)
class BakeoffASubmission:
    """单个 Bakeoff-A 提交。作者身份隐去。"""

    blinded_label: str  # devin_glm_5_2_high / codex_candidate / other_profile
    draft_ref_and_hash: dict[str, str]
    scores: dict[str, float]  # metric_name -> score

    def to_dict(self) -> dict[str, Any]:
        return {
            "blinded_label": self.blinded_label,
            "draft_ref_and_hash": dict(self.draft_ref_and_hash),
            "scores": dict(self.scores),
        }


@dataclass(frozen=True)
class BakeoffAScoringReport:
    """BakeoffAScoringReport — Bakeoff-A 盲评评分报告。不可变。"""

    report_id: str
    brief_ref_and_hash: dict[str, str]
    evaluation_pack_ref_and_hash: dict[str, str]
    submissions: list[dict[str, Any]]
    author_identity_hidden: bool
    no_solver_launched: bool
    no_bare_results: bool
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
            "brief_ref_and_hash": dict(self.brief_ref_and_hash),
            "evaluation_pack_ref_and_hash": dict(self.evaluation_pack_ref_and_hash),
            "submissions": [dict(s) for s in self.submissions],
            "author_identity_hidden": self.author_identity_hidden,
            "no_solver_launched": self.no_solver_launched,
            "no_bare_results": self.no_bare_results,
            "report_hash_algorithm": self.report_hash_algorithm,
            "report_hash": self.report_hash,
        }


def _compute_report_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["report_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


class BakeoffAScoring:
    """BakeoffAScoring — Bakeoff-A 盲评评分器。

    验证提交的评分：
    1. 作者身份隐去（blinded_label 不含真实作者身份）
    2. 指标只在 QA_BAKEOFF_A_METRICS 中
    3. 不含 QA_BAKEOFF_A_FORBIDDEN_METRICS 中的任何指标
    4. 无 Solver launch
    5. 无 bare results
    """

    def score(
        self,
        *,
        report_id: str,
        brief_ref_and_hash: dict[str, str],
        evaluation_pack_ref_and_hash: dict[str, str],
        submissions: list[BakeoffASubmission],
    ) -> VerificationResult:
        """评分并验证 Bakeoff-A 提交。

        返回 VerificationResult。如果 PASS，可以通过 build_report 获取报告。
        """
        errors: list[EC] = []
        details: list[str] = []

        if not submissions:
            errors.append(EC.QA_CANONICAL_REPORT_MISSING)
            details.append("no submissions provided")

        for i, sub in enumerate(submissions):
            # blinded_label 检查
            if sub.blinded_label not in QA_BAKEOFF_A_CARRIER_LABELS:
                errors.append(EC.QA_AUTHOR_IDENTITY_LEAKED)
                details.append(
                    f"submission {i}: blinded_label {sub.blinded_label!r} "
                    f"not in allowed labels {QA_BAKEOFF_A_CARRIER_LABELS}"
                )

            # 检查 scores 中是否有作者身份泄漏信息
            for key in sub.scores:
                key_lower = key.lower()
                if any(word in key_lower for word in ("author", "devin", "codex", "identity")):
                    if key not in QA_BAKEOFF_A_METRICS:
                        errors.append(EC.QA_AUTHOR_IDENTITY_LEAKED)
                        details.append(
                            f"submission {i}: score key {key!r} may leak author identity"
                        )

            # 检查指标合法性
            for metric in sub.scores:
                if metric in QA_BAKEOFF_A_FORBIDDEN_METRICS:
                    errors.append(EC.QA_BARE_METRIC_SNEAKED)
                    details.append(
                        f"submission {i}: bare metric sneaked in: {metric!r}"
                    )
                elif metric not in QA_BAKEOFF_A_METRICS:
                    errors.append(EC.QA_BAKEOFF_A_METRIC_NOT_ALLOWED)
                    details.append(
                        f"submission {i}: metric {metric!r} not in allowed set"
                    )

            # 检查 draft_ref_and_hash 中是否泄漏作者
            ref_id = sub.draft_ref_and_hash.get("ref_id", "")
            for word in ("devin", "codex", "author"):
                if word in ref_id.lower():
                    errors.append(EC.QA_AUTHOR_IDENTITY_LEAKED)
                    details.append(
                        f"submission {i}: draft ref_id {ref_id!r} leaks author identity"
                    )

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)
        return VerificationResult(verdict="PASS")

    def build_report(
        self,
        *,
        report_id: str,
        brief_ref_and_hash: dict[str, str],
        evaluation_pack_ref_and_hash: dict[str, str],
        submissions: list[BakeoffASubmission],
    ) -> BakeoffAScoringReport:
        """构建 BakeoffAScoringReport。调用前应先通过 score() 验证。"""
        sub_dicts = [s.to_dict() for s in submissions]
        obj = {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "object_type": _OBJECT_TYPE,
            "report_id": report_id,
            "brief_ref_and_hash": dict(brief_ref_and_hash),
            "evaluation_pack_ref_and_hash": dict(evaluation_pack_ref_and_hash),
            "submissions": sub_dicts,
            "author_identity_hidden": True,
            "no_solver_launched": True,
            "no_bare_results": True,
            "report_hash_algorithm": _HASH_ALGORITHM,
            "report_hash": None,
        }
        report_hash = _compute_report_hash(obj)
        return BakeoffAScoringReport(
            report_id=report_id,
            brief_ref_and_hash=dict(brief_ref_and_hash),
            evaluation_pack_ref_and_hash=dict(evaluation_pack_ref_and_hash),
            submissions=sub_dicts,
            author_identity_hidden=True,
            no_solver_launched=True,
            no_bare_results=True,
            report_hash=report_hash,
        )


def verify_bakeoff_a_scoring_report(
    report: dict[str, Any] | BakeoffAScoringReport,
) -> VerificationResult:
    """验证 BakeoffAScoringReport 的结构合法性。

    检查：
    1. schema 常量
    2. report_id 非空
    3. author_identity_hidden == True
    4. no_solver_launched == True
    5. no_bare_results == True
    6. submissions 中无 forbidden metrics
    7. submissions 中无作者身份泄漏
    8. report_hash 正确
    """
    if isinstance(report, BakeoffAScoringReport):
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

    if report.get("author_identity_hidden") is not True:
        errors.append(EC.QA_AUTHOR_IDENTITY_LEAKED)
        details.append("author_identity_hidden must be True")

    if report.get("no_solver_launched") is not True:
        errors.append(EC.QA_NO_SOLVER_ALLOWED)
        details.append("no_solver_launched must be True")

    if report.get("no_bare_results") is not True:
        errors.append(EC.QA_BAKEOFF_A_USING_BARE)
        details.append("no_bare_results must be True")

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
                if metric in QA_BAKEOFF_A_FORBIDDEN_METRICS:
                    errors.append(EC.QA_BARE_METRIC_SNEAKED)
                    details.append(f"submission {i}: bare metric sneaked in: {metric!r}")
                elif metric not in QA_BAKEOFF_A_METRICS:
                    errors.append(EC.QA_BAKEOFF_A_METRIC_NOT_ALLOWED)
                    details.append(f"submission {i}: metric {metric!r} not allowed")

            blinded_label = sub.get("blinded_label", "")
            if blinded_label not in QA_BAKEOFF_A_CARRIER_LABELS:
                errors.append(EC.QA_AUTHOR_IDENTITY_LEAKED)
                details.append(f"submission {i}: invalid blinded_label {blinded_label!r}")

    if report.get("report_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected report_hash_algorithm: {report.get('report_hash_algorithm')}")

    computed = _compute_report_hash(report)
    if report.get("report_hash") != computed:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"report_hash mismatch: expected {computed}, got {report.get('report_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
