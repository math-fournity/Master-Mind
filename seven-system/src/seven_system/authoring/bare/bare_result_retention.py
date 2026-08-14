"""BareResultRetention — bare 结果保留策略（WP-QA1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 72-76：

Success/failure both retained, forbidden to modify question or continue
generating until failure.

来自 docs/implementation/15-work-package-implementation-contracts.md line 89：

blocker与故障验收: Tell/Hint偷入、改题、过滤成功、retry-until-fail

BareResultRetention 确保所有 bare 结果（成功 AND 失败）都被保留。
禁止：
- 修改 question（bare results 后）
- 选择性删除成功题
- retry-until-fail
- bare 结果回流改 draft

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    QA1_BARE_STATUSES,
    QA1_RETENTION_POLICIES,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult
from .bare_baseline import BareAttemptResult


_SCHEMA_ID = "seven/bare-result-retention-record"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "BareResultRetentionRecord"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-record_hash-null)"


@dataclass(frozen=True)
class BareResultRetentionRecord:
    """BareResultRetentionRecord — bare 结果保留记录。不可变。

    记录所有 bare 结果的保留状态。
    """

    record_id: str
    bare_baseline_ref_and_hash: dict[str, str]
    total_results: int
    pass_count: int
    fail_count: int
    timeout_count: int
    quarantine_count: int
    all_retained: bool
    no_question_modification: bool
    no_successful_deletion: bool
    no_retry_until_fail: bool
    no_draft_flowback: bool
    applied_policies: list[str]
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    record_hash_algorithm: str = _HASH_ALGORITHM
    record_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "record_id": self.record_id,
            "bare_baseline_ref_and_hash": dict(self.bare_baseline_ref_and_hash),
            "total_results": self.total_results,
            "pass_count": self.pass_count,
            "fail_count": self.fail_count,
            "timeout_count": self.timeout_count,
            "quarantine_count": self.quarantine_count,
            "all_retained": self.all_retained,
            "no_question_modification": self.no_question_modification,
            "no_successful_deletion": self.no_successful_deletion,
            "no_retry_until_fail": self.no_retry_until_fail,
            "no_draft_flowback": self.no_draft_flowback,
            "applied_policies": list(self.applied_policies),
            "record_hash_algorithm": self.record_hash_algorithm,
            "record_hash": self.record_hash,
        }


def _compute_record_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["record_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


class BareResultRetention:
    """BareResultRetention — bare 结果保留器。

    确保所有 bare 结果（成功 AND 失败）都被保留。
    检查 retention policies 是否被遵守。

    硬约束：
    - 所有结果保留（成功和失败）
    - 禁止改题
    - 禁止删除成功题
    - 禁止 retry-until-fail
    - 禁止 bare 结果回流改 draft
    """

    def __init__(self) -> None:
        self._results: list[BareAttemptResult] = []
        self._question_hash_before: str = ""
        self._question_hash_after: str = ""
        self._draft_hash_before: str = ""
        self._draft_hash_after: str = ""
        self._original_problem_refs: list[str] = []
        self._current_problem_refs: list[str] = []
        self._attempts_per_problem: dict[str, int] = {}

    def register_results(
        self,
        results: list[BareAttemptResult],
    ) -> VerificationResult:
        """注册 bare 结果列表。"""
        errors: list[EC] = []
        details: list[str] = []

        for result in results:
            if result.bare_status not in QA1_BARE_STATUSES:
                errors.append(EC.QA1_BARE_STATUS_INVALID)
                details.append(
                    f"bare_status {result.bare_status!r} not in QA1_BARE_STATUSES"
                )
            self._results.append(result)
            # Track attempts per problem for retry-until-fail check
            pid = result.problem_ref_id
            self._attempts_per_problem[pid] = self._attempts_per_problem.get(pid, 0) + 1

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)
        return VerificationResult(verdict="PASS")

    def set_question_hash_before(self, hash_val: str) -> None:
        """记录 bare 前的 question release hash。"""
        self._question_hash_before = hash_val

    def set_question_hash_after(self, hash_val: str) -> None:
        """记录 bare 后的 question release hash。"""
        self._question_hash_after = hash_val

    def set_draft_hash_before(self, hash_val: str) -> None:
        """记录 bare 前的 draft hash。"""
        self._draft_hash_before = hash_val

    def set_draft_hash_after(self, hash_val: str) -> None:
        """记录 bare 后的 draft hash。"""
        self._draft_hash_after = hash_val

    def set_original_problem_refs(self, refs: list[str]) -> None:
        """记录原始 problem refs。"""
        self._original_problem_refs = list(refs)

    def set_current_problem_refs(self, refs: list[str]) -> None:
        """记录当前 problem refs（用于检测删除）。"""
        self._current_problem_refs = list(refs)

    def verify_retention(self) -> VerificationResult:
        """验证所有 retention policies 是否被遵守。

        检查（blocker tests）：
        1. 所有结果保留（成功和失败）
        2. question 未被修改
        3. 成功题未被删除
        4. 没有 retry-until-fail
        5. bare 结果未回流改 draft
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. All results retained
        if not self._results:
            errors.append(EC.QA1_BARE_RESULT_NOT_RETAINED)
            details.append("no bare results registered")

        pass_count = sum(1 for r in self._results if r.bare_status == "PASS")
        fail_count = sum(1 for r in self._results if r.bare_status == "FAIL")
        timeout_count = sum(1 for r in self._results if r.bare_status == "TIMEOUT")
        quarantine_count = sum(1 for r in self._results if r.bare_status == "QUARANTINE")

        # 2. Question not modified after bare
        if (
            self._question_hash_before
            and self._question_hash_after
            and self._question_hash_before != self._question_hash_after
        ):
            errors.append(EC.QA1_QUESTION_MODIFIED_AFTER_BARE)
            details.append(
                f"question release hash changed after bare: "
                f"{self._question_hash_before[:8]}... → "
                f"{self._question_hash_after[:8]}..."
            )

        # 3. No successful question deletion
        if self._original_problem_refs and self._current_problem_refs:
            original_set = set(self._original_problem_refs)
            current_set = set(self._current_problem_refs)
            passed_problems = {
                r.problem_ref_id for r in self._results if r.bare_status == "PASS"
            }
            deleted = original_set - current_set
            deleted_passed = deleted & passed_problems
            if deleted_passed:
                errors.append(EC.QA1_SUCCESSFUL_QUESTION_DELETED)
                details.append(
                    f"successful questions deleted: {deleted_passed}"
                )

        # 4. No retry-until-fail
        retry_problems = {
            pid: count for pid, count in self._attempts_per_problem.items()
            if count > 1
        }
        if retry_problems:
            errors.append(EC.QA1_RETRY_UNTIL_FAIL)
            details.append(
                f"retry-until-fail detected: {retry_problems}"
            )

        # 5. No bare result flowback to draft
        if (
            self._draft_hash_before
            and self._draft_hash_after
            and self._draft_hash_before != self._draft_hash_after
        ):
            errors.append(EC.QA1_BARE_RESULT_FLOWS_BACK_TO_DRAFT)
            details.append(
                f"draft hash changed after bare results: "
                f"{self._draft_hash_before[:8]}... → "
                f"{self._draft_hash_after[:8]}..."
            )

        if errors:
            return VerificationResult(verdict="FAIL", error_codes=errors, details=details)
        return VerificationResult(verdict="PASS")

    def build_record(
        self,
        *,
        record_id: str,
        bare_baseline_ref_id: str,
        bare_baseline_sha256: str,
    ) -> BareResultRetentionRecord:
        """构建 BareResultRetentionRecord。"""
        pass_count = sum(1 for r in self._results if r.bare_status == "PASS")
        fail_count = sum(1 for r in self._results if r.bare_status == "FAIL")
        timeout_count = sum(1 for r in self._results if r.bare_status == "TIMEOUT")
        quarantine_count = sum(1 for r in self._results if r.bare_status == "QUARANTINE")

        obj = {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "object_type": _OBJECT_TYPE,
            "record_id": record_id,
            "bare_baseline_ref_and_hash": {
                "ref_id": bare_baseline_ref_id,
                "sha256": bare_baseline_sha256,
            },
            "total_results": len(self._results),
            "pass_count": pass_count,
            "fail_count": fail_count,
            "timeout_count": timeout_count,
            "quarantine_count": quarantine_count,
            "all_retained": True,
            "no_question_modification": True,
            "no_successful_deletion": True,
            "no_retry_until_fail": True,
            "no_draft_flowback": True,
            "applied_policies": sorted(QA1_RETENTION_POLICIES),
            "record_hash_algorithm": _HASH_ALGORITHM,
            "record_hash": None,
        }
        record_hash = _compute_record_hash(obj)
        return BareResultRetentionRecord(
            record_id=record_id,
            bare_baseline_ref_and_hash={
                "ref_id": bare_baseline_ref_id,
                "sha256": bare_baseline_sha256,
            },
            total_results=len(self._results),
            pass_count=pass_count,
            fail_count=fail_count,
            timeout_count=timeout_count,
            quarantine_count=quarantine_count,
            all_retained=True,
            no_question_modification=True,
            no_successful_deletion=True,
            no_retry_until_fail=True,
            no_draft_flowback=True,
            applied_policies=sorted(QA1_RETENTION_POLICIES),
            record_hash=record_hash,
        )

    @property
    def results(self) -> list[BareAttemptResult]:
        return list(self._results)


def verify_bare_result_retention_record(
    record: dict[str, Any] | BareResultRetentionRecord,
) -> VerificationResult:
    """验证 BareResultRetentionRecord 的结构合法性。

    检查（blocker tests）：
    1. schema 常量
    2. record_id 非空
    3. all_retained == True
    4. no_question_modification == True
    5. no_successful_deletion == True
    6. no_retry_until_fail == True
    7. no_draft_flowback == True
    8. applied_policies == QA1_RETENTION_POLICIES
    9. record_hash 正确
    """
    if isinstance(record, BareResultRetentionRecord):
        record = record.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if record.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if record.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if record.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not record.get("record_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("record_id must not be empty")

    if record.get("all_retained") is not True:
        errors.append(EC.QA1_BARE_RESULT_NOT_RETAINED)
        details.append("all_retained must be True")

    if record.get("no_question_modification") is not True:
        errors.append(EC.QA1_QUESTION_MODIFIED_AFTER_BARE)
        details.append("no_question_modification must be True")

    if record.get("no_successful_deletion") is not True:
        errors.append(EC.QA1_SUCCESSFUL_QUESTION_DELETED)
        details.append("no_successful_deletion must be True")

    if record.get("no_retry_until_fail") is not True:
        errors.append(EC.QA1_RETRY_UNTIL_FAIL)
        details.append("no_retry_until_fail must be True")

    if record.get("no_draft_flowback") is not True:
        errors.append(EC.QA1_BARE_RESULT_FLOWS_BACK_TO_DRAFT)
        details.append("no_draft_flowback must be True")

    applied = set(record.get("applied_policies", []))
    if applied != set(QA1_RETENTION_POLICIES):
        errors.append(EC.QA1_BARE_RESULT_NOT_RETAINED)
        details.append(
            f"applied_policies mismatch: expected {sorted(QA1_RETENTION_POLICIES)}, "
            f"got {sorted(applied)}"
        )

    if record.get("record_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"unexpected record_hash_algorithm: {record.get('record_hash_algorithm')}"
        )
    computed = _compute_record_hash(record)
    if record.get("record_hash") != computed:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"record_hash mismatch: expected {computed}, "
            f"got {record.get('record_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
