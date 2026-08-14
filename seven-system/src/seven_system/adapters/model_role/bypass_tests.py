"""BypassTests — adapter 旁路测试定义。

来自 docs/implementation/05-execution-ports-and-carriers.md 和 AGENTS.md rule 4：

- direct-devin bypass test：adapter 不得使用 solver_harness
- tool event test：output 中不得有 tool events（认知角色默认 NO_TOOLS）
- repo workspace test：adapter 不得使用 repo workspace

这些测试验证 adapter 不绕过 ModelRolePort 协议、不复用 Solver 资源池。

SIDE_EFFECT_FREE：纯内存实现，测试输入是 adapter 的元数据/输出描述，
不调用任何真实 CLI / DB / D-volume。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ...contracts.errors import (
    BYPASS_TEST_NAMES,
    BYPASS_TEST_RESULTS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


@dataclass(frozen=True)
class BypassTestResult:
    """单个 bypass test 的结果。"""

    test_name: str
    result: str  # "PASS" | "FAIL" | "NOT_APPLICABLE"
    detail: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "test_name": self.test_name,
            "result": self.result,
            "detail": self.detail,
        }


@dataclass
class BypassTestSuite:
    """bypass test 套件：收集所有 bypass test 结果。"""

    results: list[BypassTestResult] = field(default_factory=list)

    def add(self, result: BypassTestResult) -> None:
        self.results.append(result)

    def all_pass(self) -> bool:
        return all(r.result == "PASS" for r in self.results)

    def to_list(self) -> list[dict[str, str]]:
        return [r.to_dict() for r in self.results]


def _test_direct_devin_bypass(adapter_metadata: dict[str, Any]) -> BypassTestResult:
    """direct-devin bypass test：adapter 不得使用 solver_harness。

    检查 adapter_metadata 中是否引用了 solver_harness。
    如果引用了 solver_harness → FAIL（BYPASS_SOLVER_HARNESS_USED）。
    """
    uses_solver_harness = adapter_metadata.get("uses_solver_harness", False)
    solver_harness_ref = adapter_metadata.get("solver_harness_ref", "")

    if uses_solver_harness or solver_harness_ref:
        return BypassTestResult(
            test_name="direct_devin_bypass",
            result="FAIL",
            detail=f"adapter uses solver_harness: uses_solver_harness={uses_solver_harness}, "
                   f"solver_harness_ref={solver_harness_ref!r}",
        )
    return BypassTestResult(
        test_name="direct_devin_bypass",
        result="PASS",
        detail="adapter does not use solver_harness",
    )


def _test_tool_events(adapter_metadata: dict[str, Any]) -> BypassTestResult:
    """tool event test：output 中不得有 tool events。

    认知角色默认 NO_TOOLS。如果 output 中包含 tool events → FAIL。
    """
    tool_events = adapter_metadata.get("tool_events", [])
    has_tool_events = adapter_metadata.get("has_tool_events", False)

    if has_tool_events or (isinstance(tool_events, list) and len(tool_events) > 0):
        return BypassTestResult(
            test_name="tool_event_test",
            result="FAIL",
            detail=f"tool events detected: {len(tool_events) if isinstance(tool_events, list) else '?'} events, "
                   f"has_tool_events={has_tool_events}",
        )
    return BypassTestResult(
        test_name="tool_event_test",
        result="PASS",
        detail="no tool events in output",
    )


def _test_repo_workspace(adapter_metadata: dict[str, Any]) -> BypassTestResult:
    """repo workspace test：adapter 不得使用 repo workspace。

    检查 adapter_metadata 中是否使用了 repo workspace。
    角色 workspace 不在 repo、不在 Solver root。
    """
    uses_repo_workspace = adapter_metadata.get("uses_repo_workspace", False)
    workspace_path = adapter_metadata.get("workspace_path", "")

    repo_indicators = ["solver_harness", "solver_root", "/repo", "repo_root"]
    is_repo = (
        uses_repo_workspace
        or any(ind in workspace_path for ind in repo_indicators if workspace_path)
    )

    if is_repo:
        return BypassTestResult(
            test_name="repo_workspace_test",
            result="FAIL",
            detail=f"adapter uses repo workspace: uses_repo_workspace={uses_repo_workspace}, "
                   f"workspace_path={workspace_path!r}",
        )
    return BypassTestResult(
        test_name="repo_workspace_test",
        result="PASS",
        detail="adapter does not use repo workspace",
    )


def run_bypass_tests(adapter_metadata: dict[str, Any]) -> BypassTestSuite:
    """运行全部 bypass test，返回 BypassTestSuite。

    adapter_metadata 是 adapter 的元数据/输出描述，包含：
    - uses_solver_harness: bool
    - solver_harness_ref: str
    - tool_events: list
    - has_tool_events: bool
    - uses_repo_workspace: bool
    - workspace_path: str
    """
    suite = BypassTestSuite()
    suite.add(_test_direct_devin_bypass(adapter_metadata))
    suite.add(_test_tool_events(adapter_metadata))
    suite.add(_test_repo_workspace(adapter_metadata))
    return suite


def verify_bypass_test_suite(suite: BypassTestSuite) -> VerificationResult:
    """验证 BypassTestSuite 的结果。

    所有 test 必须 PASS（NOT_APPLICABLE 也接受，但 FAIL 不接受）。
    """
    errors: list[EC] = []
    details: list[str] = []

    for result in suite.results:
        if result.test_name not in BYPASS_TEST_NAMES:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"unknown bypass test: {result.test_name}")
        if result.result not in BYPASS_TEST_RESULTS:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append(f"invalid bypass test result: {result.result}")
        if result.result == "FAIL":
            if result.test_name == "direct_devin_bypass":
                errors.append(EC.BYPASS_SOLVER_HARNESS_USED)
            elif result.test_name == "tool_event_test":
                errors.append(EC.BYPASS_TOOL_EVENT_DETECTED)
            elif result.test_name == "repo_workspace_test":
                errors.append(EC.BYPASS_REPO_WORKSPACE_USED)
            details.append(f"bypass test {result.test_name} FAILED: {result.detail}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
    )
