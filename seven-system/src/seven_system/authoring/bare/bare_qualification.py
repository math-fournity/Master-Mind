"""BareQualificationResult — bare 资格判定结果（WP-QA1 P3B）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 72-76 和
docs/implementation/15-work-package-implementation-contracts.md line 89：

BareQualificationResult 是从 bare 结果得出的资格判定。
引用 BareBaseline by hash。包含 per-problem qualification status
（QUALIFIED/NOT_QUALIFIED/INCONCLUSIVE/QUARANTINED）。

硬约束：
- 必须引用 BareBaseline（ref_id + sha256）
- 每个 problem 的 qualification status 在 QA1_QUALIFICATION_STATUSES 中
- 不可回流修改 question draft
- 不是 P5 claim

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    QA1_QUALIFICATION_STATUSES,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/bare-qualification-result"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "BareQualificationResult"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-result_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class ProblemQualification:
    """单个 problem 的 bare 资格判定。不可变。

    字段：
    - problem_ref_id：题目引用 ID
    - qualification_status：资格状态（QUALIFIED/NOT_QUALIFIED/INCONCLUSIVE/QUARANTINED）
    - bare_status_ref：对应的 bare attempt 状态
    - not_p5_claim：明确标记不是 P5 claim（必须为 True）
    """

    problem_ref_id: str
    qualification_status: str
    bare_status_ref: str
    not_p5_claim: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "problem_ref_id": self.problem_ref_id,
            "qualification_status": self.qualification_status,
            "bare_status_ref": self.bare_status_ref,
            "not_p5_claim": self.not_p5_claim,
        }


@dataclass(frozen=True)
class BareQualificationResult:
    """BareQualificationResult — bare 资格判定结果。不可变。

    引用 BareBaseline by hash。
    包含 per-problem qualification status。
    """

    result_id: str
    bare_baseline_ref_and_hash: dict[str, str]
    problem_qualifications: list[dict[str, Any]]
    no_p5_claim: bool
    no_draft_flowback: bool
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    result_hash_algorithm: str = _HASH_ALGORITHM
    result_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "result_id": self.result_id,
            "bare_baseline_ref_and_hash": dict(self.bare_baseline_ref_and_hash),
            "problem_qualifications": [dict(q) for q in self.problem_qualifications],
            "no_p5_claim": self.no_p5_claim,
            "no_draft_flowback": self.no_draft_flowback,
            "result_hash_algorithm": self.result_hash_algorithm,
            "result_hash": self.result_hash,
        }


def _compute_result_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["result_hash"] = None
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


def build_bare_qualification_result(
    *,
    result_id: str,
    bare_baseline_ref_id: str,
    bare_baseline_sha256: str,
    problem_qualifications: list[ProblemQualification],
) -> BareQualificationResult:
    """构建 BareQualificationResult，自动计算 result_hash。

    no_p5_claim 固定为 True（bare 不是 P5 claim）。
    no_draft_flowback 固定为 True（bare 结果不回流改 draft）。
    """
    quals = [q.to_dict() for q in problem_qualifications]
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "result_id": result_id,
        "bare_baseline_ref_and_hash": {
            "ref_id": bare_baseline_ref_id,
            "sha256": bare_baseline_sha256,
        },
        "problem_qualifications": quals,
        "no_p5_claim": True,
        "no_draft_flowback": True,
        "result_hash_algorithm": _HASH_ALGORITHM,
        "result_hash": None,
    }
    result_hash = _compute_result_hash(obj)
    return BareQualificationResult(
        result_id=result_id,
        bare_baseline_ref_and_hash={
            "ref_id": bare_baseline_ref_id,
            "sha256": bare_baseline_sha256,
        },
        problem_qualifications=quals,
        no_p5_claim=True,
        no_draft_flowback=True,
        result_hash=result_hash,
    )


def verify_bare_qualification_result(
    result: dict[str, Any] | BareQualificationResult,
) -> VerificationResult:
    """验证 BareQualificationResult 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. result_id 非空
    3. bare_baseline_ref_and_hash 存在且结构合法
    4. no_p5_claim == True（bare 不是 P5 claim）
    5. no_draft_flowback == True（bare 结果不回流改 draft）
    6. 每个 problem_qualification 的 qualification_status 在 QA1_QUALIFICATION_STATUSES 中
    7. 每个 problem_qualification 的 not_p5_claim == True
    8. result_hash 正确
    """
    if isinstance(result, BareQualificationResult):
        result = result.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if result.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if result.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if result.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not result.get("result_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("result_id must not be empty")

    # bare_baseline_ref_and_hash (blocker: missing ref)
    baseline_ref = result.get("bare_baseline_ref_and_hash", {})
    if not _ref_and_hash_valid(baseline_ref):
        errors.append(EC.QA1_BARELINE_REF_MISSING)
        details.append(
            "bare_baseline_ref_and_hash must have ref_id and sha256"
        )

    # no_p5_claim (blocker: bare is not P5 claim)
    if result.get("no_p5_claim") is not True:
        errors.append(EC.QA1_P5_CLAIM_IN_BARE_REPORT)
        details.append("no_p5_claim must be True")

    # no_draft_flowback (blocker: bare results must not flow back to draft)
    if result.get("no_draft_flowback") is not True:
        errors.append(EC.QA1_BARE_RESULT_FLOWS_BACK_TO_DRAFT)
        details.append("no_draft_flowback must be True")

    # problem_qualifications
    quals = result.get("problem_qualifications", [])
    if not isinstance(quals, list):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("problem_qualifications must be a list")
    else:
        for i, qual in enumerate(quals):
            if not isinstance(qual, dict):
                errors.append(EC.REQUIRED_FIELD_MISSING)
                details.append(f"problem_qualification {i} is not a dict")
                continue
            status = qual.get("qualification_status", "")
            if status not in QA1_QUALIFICATION_STATUSES:
                errors.append(EC.QA1_QUALIFICATION_STATUS_INVALID)
                details.append(
                    f"problem_qualification {i}: qualification_status {status!r} "
                    f"not in QA1_QUALIFICATION_STATUSES"
                )
            if not qual.get("problem_ref_id"):
                errors.append(EC.REQUIRED_FIELD_MISSING)
                details.append(f"problem_qualification {i}: problem_ref_id is empty")
            # not_p5_claim must be True (blocker)
            if qual.get("not_p5_claim") is not True:
                errors.append(EC.QA1_P5_CLAIM_IN_BARE_REPORT)
                details.append(
                    f"problem_qualification {i}: not_p5_claim must be True"
                )

    # result_hash
    if result.get("result_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"unexpected result_hash_algorithm: "
            f"{result.get('result_hash_algorithm')}"
        )
    computed = _compute_result_hash(result)
    if result.get("result_hash") != computed:
        errors.append(EC.QA1_QUALIFICATION_RESULT_HASH_MISMATCH)
        details.append(
            f"result_hash mismatch: expected {computed}, "
            f"got {result.get('result_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
