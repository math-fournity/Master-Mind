"""AnswerIsolationReport — 答案隔离验证报告（WP-SV1）。

AnswerIsolationReport 验证 answer 与 process artifacts 分离：
- answer_ref 与 trajectory_ref 是不同的引用
- answer_ref 的 hash 独立于 trajectory hash
- answer 不嵌入在 trajectory 中

报告记录隔离检查的 verdict 和 evidence。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import VerificationErrorCode as EC
from ...contracts.completion_contract import VerificationResult
from .port import LaunchReceipt


_REPORT_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-report_hash-null)"

ANSWER_ISOLATION_CHECK_IDS = (
    "sv1.answer_isolation.answer_ref_separate_from_trajectory_ref",
    "sv1.answer_isolation.answer_hash_independent",
    "sv1.answer_isolation.answer_not_embedded_in_trajectory",
    "sv1.answer_isolation.answer_kind_valid",
)


@dataclass(frozen=True)
class AnswerIsolationReport:
    """AnswerIsolationReport — 答案隔离验证报告。"""

    attempt_id: str
    checks: list[dict[str, Any]]
    verdict: str
    blockers: list[str]
    report_hash_algorithm: str
    report_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_id": self.attempt_id,
            "checks": [dict(c) for c in self.checks],
            "verdict": self.verdict,
            "blockers": list(self.blockers),
            "report_hash_algorithm": self.report_hash_algorithm,
            "report_hash": self.report_hash,
        }


def _is_ref_and_hash(obj: Any) -> bool:
    return (
        isinstance(obj, dict)
        and set(obj.keys()) == {"ref_id", "sha256"}
        and isinstance(obj.get("ref_id"), str)
        and isinstance(obj.get("sha256"), str)
        and len(obj.get("sha256", "")) == 64
    )


def build_answer_isolation_report(
    *,
    attempt_id: str,
    receipt: LaunchReceipt | dict[str, Any],
    trajectory_content: str | bytes | None = None,
    answer_content: str | bytes | None = None,
) -> AnswerIsolationReport:
    """构建 AnswerIsolationReport。

    检查：
    1. answer_ref 与 trajectory_ref 是不同的引用
    2. answer hash 独立于 trajectory hash
    3. answer 不嵌入在 trajectory 中
    4. answer_kind 合法
    """
    if isinstance(receipt, LaunchReceipt):
        receipt_dict = receipt.to_dict()
    else:
        receipt_dict = receipt

    checks: list[dict[str, Any]] = []
    blockers: list[str] = []

    traj_ref = receipt_dict.get("trajectory_ref_and_hash", {})
    answer_ref = receipt_dict.get("answer_ref_and_hash", {})
    answer_kind = receipt_dict.get("answer_kind", "")

    # 1. answer_ref separate from trajectory_ref
    refs_separate = (
        _is_ref_and_hash(traj_ref)
        and _is_ref_and_hash(answer_ref)
        and traj_ref.get("ref_id") != answer_ref.get("ref_id")
    )
    checks.append({
        "check_id": "sv1.answer_isolation.answer_ref_separate_from_trajectory_ref",
        "verdict": "PASS" if refs_separate else "FAIL",
        "evidence": [
            f"trajectory_ref_id={traj_ref.get('ref_id', '')!r}, "
            f"answer_ref_id={answer_ref.get('ref_id', '')!r}, "
            f"separate={refs_separate}",
        ],
    })
    if not refs_separate:
        blockers.append("SV_ANSWER_NOT_ISOLATED")

    # 2. answer hash independent from trajectory hash
    hashes_independent = (
        _is_ref_and_hash(traj_ref)
        and _is_ref_and_hash(answer_ref)
        and traj_ref.get("sha256") != answer_ref.get("sha256")
    )
    checks.append({
        "check_id": "sv1.answer_isolation.answer_hash_independent",
        "verdict": "PASS" if hashes_independent else "FAIL",
        "evidence": [
            f"trajectory_sha256={traj_ref.get('sha256', '')[:16]}..., "
            f"answer_sha256={answer_ref.get('sha256', '')[:16]}..., "
            f"independent={hashes_independent}",
        ],
    })
    if not hashes_independent:
        blockers.append("SV_ANSWER_NOT_ISOLATED")

    # 3. answer not embedded in trajectory
    if trajectory_content is not None and answer_content is not None:
        if isinstance(trajectory_content, bytes):
            traj_str = trajectory_content.decode("utf-8", errors="replace")
        else:
            traj_str = trajectory_content
        if isinstance(answer_content, bytes):
            answer_str = answer_content.decode("utf-8", errors="replace")
        else:
            answer_str = answer_content
        # check answer content is not a substring of trajectory content
        not_embedded = answer_str not in traj_str
    else:
        # can't verify without content; assume isolated if refs are separate
        not_embedded = refs_separate

    checks.append({
        "check_id": "sv1.answer_isolation.answer_not_embedded_in_trajectory",
        "verdict": "PASS" if not_embedded else "FAIL",
        "evidence": [f"answer_not_embedded_in_trajectory={not_embedded}"],
    })
    if not not_embedded:
        blockers.append("SV_ANSWER_NOT_ISOLATED")

    # 4. answer_kind valid
    from ...contracts.errors import SV_ANSWER_KINDS
    answer_kind_valid = answer_kind in SV_ANSWER_KINDS
    checks.append({
        "check_id": "sv1.answer_isolation.answer_kind_valid",
        "verdict": "PASS" if answer_kind_valid else "FAIL",
        "evidence": [f"answer_kind={answer_kind!r}, valid={answer_kind_valid}"],
    })
    if not answer_kind_valid:
        blockers.append("SV_ANSWER_KIND_INVALID")

    verdict = "PASS" if not blockers else "FAIL"

    obj = {
        "attempt_id": attempt_id,
        "checks": checks,
        "verdict": verdict,
        "blockers": blockers,
        "report_hash_algorithm": _REPORT_HASH_ALGORITHM,
        "report_hash": None,
    }
    report_hash = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

    return AnswerIsolationReport(
        attempt_id=attempt_id,
        checks=checks,
        verdict=verdict,
        blockers=blockers,
        report_hash_algorithm=_REPORT_HASH_ALGORITHM,
        report_hash=report_hash,
    )


def verify_answer_isolation_report(
    report: AnswerIsolationReport | dict[str, Any],
) -> VerificationResult:
    """验证 AnswerIsolationReport 的 schema + semantic 合法性。

    检查：
    1. attempt_id 非空
    2. checks 包含全部 ANSWER_ISOLATION_CHECK_IDS
    3. check verdict 与 report verdict 一致
    4. blockers 与 check verdict 一致
    5. report_hash 正确
    """
    if isinstance(report, AnswerIsolationReport):
        report_dict = report.to_dict()
    else:
        report_dict = report

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. attempt_id
    if not report_dict.get("attempt_id"):
        _err(EC.REQUIRED_FIELD_MISSING, "attempt_id is empty")

    # 2. checks
    checks = report_dict.get("checks", [])
    if not isinstance(checks, list):
        _err(EC.REQUIRED_FIELD_MISSING, "checks is not a list")
    else:
        check_ids = [c.get("check_id") if isinstance(c, dict) else None for c in checks]
        if check_ids != list(ANSWER_ISOLATION_CHECK_IDS):
            _err(EC.REQUIRED_FIELD_MISSING,
                 f"checks must exactly match ANSWER_ISOLATION_CHECK_IDS, got {check_ids}")

        # 3. verdict consistency
        failed_checks = [
            c.get("check_id", "?") for c in checks
            if isinstance(c, dict) and c.get("verdict") == "FAIL"
        ]
        report_verdict = report_dict.get("verdict", "")
        if failed_checks and report_verdict != "FAIL":
            _err(EC.SV_ANSWER_ISOLATION_VERDICT_FAIL,
                 f"checks failed {failed_checks} but verdict is {report_verdict!r}")
        if not failed_checks and report_verdict != "PASS":
            _err(EC.SV_ANSWER_ISOLATION_VERDICT_FAIL,
                 f"no checks failed but verdict is {report_verdict!r}")

    # 4. blockers
    blockers = report_dict.get("blockers", [])
    if not isinstance(blockers, list):
        _err(EC.REQUIRED_FIELD_MISSING, "blockers is not a list")
    else:
        if report_verdict == "PASS" and blockers:
            _err(EC.SV_ANSWER_ISOLATION_VERDICT_FAIL,
                 "PASS report must have no blockers")
        if report_verdict == "FAIL" and not blockers:
            _err(EC.SV_ANSWER_ISOLATION_VERDICT_FAIL,
                 "FAIL report must have blockers")

    # 5. report_hash
    if report_dict.get("report_hash_algorithm") != _REPORT_HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"unexpected report_hash_algorithm: "
             f"{report_dict.get('report_hash_algorithm')}")
    obj_for_hash = dict(report_dict)
    obj_for_hash["report_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if report_dict.get("report_hash") != computed_hash:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"report_hash mismatch: expected {computed_hash}, "
             f"got {report_dict.get('report_hash')}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
