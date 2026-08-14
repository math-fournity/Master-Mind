"""SafeLaunchReport — 安全启动验证报告（WP-SV1）。

SafeLaunchReport 验证：
1. no direct-devin bypass（只有 harness adapter 调用 solver_harness）
2. repo workspace isolated
3. no tool events
4. trajectory present
5. answer isolation maintained

报告记录每项检查的 verdict 和 evidence。

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import VerificationErrorCode as EC
from ...contracts.completion_contract import VerificationResult
from .port import LaunchReceipt, verify_launch_receipt
from .notool_policy import check_trajectory_for_tool_events


_REPORT_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-report_hash-null)"

SAFE_LAUNCH_CHECK_IDS = (
    "sv1.safe_launch.no_direct_devin_bypass",
    "sv1.safe_launch.repo_workspace_isolated",
    "sv1.safe_launch.no_tool_events",
    "sv1.safe_launch.trajectory_present",
    "sv1.safe_launch.answer_isolation_maintained",
)


@dataclass(frozen=True)
class SafeLaunchReport:
    """SafeLaunchReport — 安全启动验证报告。"""

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


def build_safe_launch_report(
    *,
    attempt_id: str,
    receipt: LaunchReceipt | dict[str, Any],
    adapter_metadata: dict[str, Any] | None = None,
    trajectory: list[dict[str, Any]] | dict[str, Any] | None = None,
) -> SafeLaunchReport:
    """构建 SafeLaunchReport。

    检查：
    1. no direct-devin bypass（adapter_metadata 中无 direct_devin_bypass）
    2. repo workspace isolated（adapter_metadata / receipt 中 workspace 已隔离）
    3. no tool events（trajectory 中无 tool events）
    4. trajectory present（receipt 中 trajectory_ref_and_hash 存在）
    5. answer isolation maintained（answer_ref != trajectory_ref）
    """
    meta = adapter_metadata or {}
    if isinstance(receipt, LaunchReceipt):
        receipt_dict = receipt.to_dict()
    else:
        receipt_dict = receipt

    checks: list[dict[str, Any]] = []
    blockers: list[str] = []

    # 1. no direct-devin bypass
    direct_bypass = meta.get("direct_devin_bypass", False)
    uses_devin_binary = meta.get("uses_devin_binary", False)
    subprocess_to_devin = meta.get("subprocess_to_devin", False)
    bypass_detected = direct_bypass or uses_devin_binary or subprocess_to_devin
    # also check receipt failure state
    if receipt_dict.get("failure_or_quarantine_state") == "DIRECT_DEVIN_BYPASS_DETECTED":
        bypass_detected = True

    checks.append({
        "check_id": "sv1.safe_launch.no_direct_devin_bypass",
        "verdict": "FAIL" if bypass_detected else "PASS",
        "evidence": [f"direct_devin_bypass={direct_bypass}, "
                     f"uses_devin_binary={uses_devin_binary}, "
                     f"subprocess_to_devin={subprocess_to_devin}"],
    })
    if bypass_detected:
        blockers.append("SV_DIRECT_DEVIN_BYPASS")

    # 2. repo workspace isolated
    workspace_isolated = meta.get("repo_workspace_isolated", True)
    workspace_not_isolated = meta.get("repo_workspace_not_isolated", False)
    repo_leak = not workspace_isolated or workspace_not_isolated

    checks.append({
        "check_id": "sv1.safe_launch.repo_workspace_isolated",
        "verdict": "FAIL" if repo_leak else "PASS",
        "evidence": [f"repo_workspace_isolated={workspace_isolated}, "
                     f"repo_workspace_not_isolated={workspace_not_isolated}"],
    })
    if repo_leak:
        blockers.append("SV_REPO_WORKSPACE_NOT_ISOLATED")

    # 3. no tool events
    if trajectory is not None:
        tool_result = check_trajectory_for_tool_events(trajectory)
        has_tool_events = not tool_result.passed
    else:
        # if no trajectory provided, check receipt failure state
        has_tool_events = (
            receipt_dict.get("failure_or_quarantine_state") == "TOOL_EVENT_DETECTED"
        )

    checks.append({
        "check_id": "sv1.safe_launch.no_tool_events",
        "verdict": "FAIL" if has_tool_events else "PASS",
        "evidence": [f"has_tool_events={has_tool_events}"],
    })
    if has_tool_events:
        blockers.append("SV_TOOL_EVENT_DETECTED")

    # 4. trajectory present
    traj_ref = receipt_dict.get("trajectory_ref_and_hash", {})
    trajectory_present = (
        isinstance(traj_ref, dict)
        and set(traj_ref.keys()) == {"ref_id", "sha256"}
        and isinstance(traj_ref.get("ref_id"), str)
        and traj_ref.get("ref_id")
        and isinstance(traj_ref.get("sha256"), str)
        and len(traj_ref.get("sha256", "")) == 64
    )

    checks.append({
        "check_id": "sv1.safe_launch.trajectory_present",
        "verdict": "PASS" if trajectory_present else "FAIL",
        "evidence": [f"trajectory_ref_and_hash present={trajectory_present}"],
    })
    if not trajectory_present:
        blockers.append("SV_TRAJECTORY_MISSING")

    # 5. answer isolation maintained
    answer_ref = receipt_dict.get("answer_ref_and_hash", {})
    answer_isolated = (
        trajectory_present
        and isinstance(answer_ref, dict)
        and set(answer_ref.keys()) == {"ref_id", "sha256"}
        and answer_ref.get("ref_id")
        and answer_ref.get("ref_id") != traj_ref.get("ref_id")
    )
    # if trajectory not present, answer isolation can't be verified → FAIL
    if not trajectory_present:
        answer_isolated = False

    checks.append({
        "check_id": "sv1.safe_launch.answer_isolation_maintained",
        "verdict": "PASS" if answer_isolated else "FAIL",
        "evidence": [
            f"answer_ref_id={answer_ref.get('ref_id', '')!r}, "
            f"trajectory_ref_id={traj_ref.get('ref_id', '')!r}, "
            f"isolated={answer_isolated}",
        ],
    })
    if not answer_isolated:
        blockers.append("SV_ANSWER_NOT_ISOLATED")

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

    return SafeLaunchReport(
        attempt_id=attempt_id,
        checks=checks,
        verdict=verdict,
        blockers=blockers,
        report_hash_algorithm=_REPORT_HASH_ALGORITHM,
        report_hash=report_hash,
    )


def verify_safe_launch_report(
    report: SafeLaunchReport | dict[str, Any],
) -> VerificationResult:
    """验证 SafeLaunchReport 的 schema + semantic 合法性。

    检查：
    1. attempt_id 非空
    2. checks 包含全部 SAFE_LAUNCH_CHECK_IDS
    3. 所有 check verdict 为 PASS（否则 report verdict 必须为 FAIL）
    4. blockers 与 check verdict 一致
    5. report_hash 正确
    """
    if isinstance(report, SafeLaunchReport):
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
        if check_ids != list(SAFE_LAUNCH_CHECK_IDS):
            _err(EC.REQUIRED_FIELD_MISSING,
                 f"checks must exactly match SAFE_LAUNCH_CHECK_IDS, got {check_ids}")

        # 3. check verdict consistency
        failed_checks = [
            c.get("check_id", "?") for c in checks
            if isinstance(c, dict) and c.get("verdict") == "FAIL"
        ]
        report_verdict = report_dict.get("verdict", "")
        if failed_checks and report_verdict != "FAIL":
            _err(EC.SV_SAFE_LAUNCH_VERDICT_FAIL,
                 f"checks failed {failed_checks} but verdict is {report_verdict!r}")
        if not failed_checks and report_verdict != "PASS":
            _err(EC.SV_SAFE_LAUNCH_VERDICT_FAIL,
                 f"no checks failed but verdict is {report_verdict!r}")

    # 4. blockers
    blockers = report_dict.get("blockers", [])
    if not isinstance(blockers, list):
        _err(EC.REQUIRED_FIELD_MISSING, "blockers is not a list")
    else:
        if report_verdict == "PASS" and blockers:
            _err(EC.SV_SAFE_LAUNCH_VERDICT_FAIL,
                 "PASS report must have no blockers")
        if report_verdict == "FAIL" and not blockers:
            _err(EC.SV_SAFE_LAUNCH_VERDICT_FAIL,
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
