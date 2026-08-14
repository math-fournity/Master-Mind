"""solver adapters — TargetSolverPort / Harness adapter (WP-SV1).

本子包实现 TargetSolverPort 协议的具体 provider adapter：

- HarnessAdapter（WP-SV1）：
  - 唯一允许调用 solver_harness 的模块
  - v1 只允许 NoTool policy
  - LaunchReceipt 必须包含 trajectory_ref+hash（缺 trajectory = FAIL）
  - answer_ref 与 trajectory_ref 分离（answer isolation）

- 数据对象：
  - SolverJob / PreparedSolverJob / LaunchTicket / LaunchReceipt
  - HarnessProfile / NoToolPolicy
  - SafeLaunchReport / AnswerIsolationReport / SolverCapabilityReport

硬约束（docs/implementation/05-execution-ports-and-carriers.md line 406-414）：
- 只有 adapters/solver/devin_solver.py 可调用 solver_harness
- 其他模块出现 subprocess 调用这些 CLI = bypass

当前状态：SIDE_EFFECT_FREE / IMPLEMENTED_PENDING_EVIDENCE
- 协议 stub、fake adapter、profile 解析、capability report builder 已实现
- live solver launch 被 activation-gated，不调用真实 solver_harness
- 不调用任何真实 CLI / DB / D-volume
"""

from .port import (
    TargetSolverPort,
    SolverJob,
    PreparedSolverJob,
    LaunchTicket,
    LaunchReceipt,
    SolverJobError,
    build_solver_job,
    prepare_solver_job,
    verify_solver_job,
    verify_prepared_solver_job,
    verify_launch_ticket,
    verify_launch_receipt,
)
from .harness_profile import (
    HarnessProfile,
    build_harness_profile,
    verify_harness_profile,
)
from .notool_policy import (
    NoToolPolicy,
    build_notool_policy,
    verify_notool_policy,
    check_trajectory_for_tool_events,
)
from .harness_adapter import (
    HarnessAdapter,
    FakeHarnessAdapter,
    HarnessAdapterError,
)
from .safe_launch_report import (
    SafeLaunchReport,
    build_safe_launch_report,
    verify_safe_launch_report,
)
from .answer_isolation_report import (
    AnswerIsolationReport,
    build_answer_isolation_report,
    verify_answer_isolation_report,
)
from .solver_capability_report import (
    SolverCapabilityReport,
    build_solver_capability_report,
    verify_solver_capability_report,
    SOLVER_REPORT_SCHEMA_VERSION,
    SOLVER_CHECK_IDS,
    SOLVER_CLAIMS,
    SOLVER_NONCLAIMS,
    SOLVER_SIDE_EFFECT_KEYS,
)

__all__ = [
    "TargetSolverPort",
    "SolverJob",
    "PreparedSolverJob",
    "LaunchTicket",
    "LaunchReceipt",
    "SolverJobError",
    "build_solver_job",
    "prepare_solver_job",
    "verify_solver_job",
    "verify_prepared_solver_job",
    "verify_launch_ticket",
    "verify_launch_receipt",
    "HarnessProfile",
    "build_harness_profile",
    "verify_harness_profile",
    "NoToolPolicy",
    "build_notool_policy",
    "verify_notool_policy",
    "check_trajectory_for_tool_events",
    "HarnessAdapter",
    "FakeHarnessAdapter",
    "HarnessAdapterError",
    "SafeLaunchReport",
    "build_safe_launch_report",
    "verify_safe_launch_report",
    "AnswerIsolationReport",
    "build_answer_isolation_report",
    "verify_answer_isolation_report",
    "SolverCapabilityReport",
    "build_solver_capability_report",
    "verify_solver_capability_report",
    "SOLVER_REPORT_SCHEMA_VERSION",
    "SOLVER_CHECK_IDS",
    "SOLVER_CLAIMS",
    "SOLVER_NONCLAIMS",
    "SOLVER_SIDE_EFFECT_KEYS",
]
