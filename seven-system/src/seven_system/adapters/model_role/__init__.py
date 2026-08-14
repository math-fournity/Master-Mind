"""model_role adapters — Devin CLI / Codex exec 认知角色适配器。

本子包实现 ModelRolePort 协议的具体 provider adapter：

- DevinCliModelRoleAdapter（WP-CW-D1）：
  - model UID = glm-5-2（GLM-5.2 High），effort 编码在 UID 中
  - ATIF parser：解析 trajectory export 格式
  - ProfileCapabilityReport builder

- CodexExecModelRoleAdapter（WP-CW-C1）：
  - model / effort / mode / orchestration 分别冻结
  - JSONL parser：解析 Codex response event stream
  - ProfileCapabilityReport builder

- ProfileCapabilityReport（共享）：
  - requested / effective / unobservable profile fields
  - verifier：检查 profile 一致性、无 tool events、无 solver_harness 使用

- BypassTests（共享）：
  - direct-devin bypass test（adapter 不得使用 solver_harness）
  - tool event test（output 中不得有 tool events）
  - repo workspace test（不得使用 repo workspace）

SIDE_EFFECT_FREE：纯内存实现，不调用任何真实 CLI / DB / D-volume。
"""

from .profile_capability import (
    ProfileCapabilityReport,
    build_profile_capability_report,
    verify_profile_capability_report,
)
from .bypass_tests import (
    BypassTestResult,
    BypassTestSuite,
    run_bypass_tests,
)
from .devin_adapter import (
    DevinCliModelRoleAdapter,
    DevinProfile,
    parse_devin_profile,
    AtifParser,
    AtifParseResult,
    parse_atif_trajectory,
)
from .codex_adapter import (
    CodexExecModelRoleAdapter,
    CodexProfile,
    parse_codex_profile,
    JsonlParser,
    JsonlParseResult,
    parse_codex_jsonl,
)

__all__ = [
    "ProfileCapabilityReport",
    "build_profile_capability_report",
    "verify_profile_capability_report",
    "BypassTestResult",
    "BypassTestSuite",
    "run_bypass_tests",
    "DevinCliModelRoleAdapter",
    "DevinProfile",
    "parse_devin_profile",
    "AtifParser",
    "AtifParseResult",
    "parse_atif_trajectory",
    "CodexExecModelRoleAdapter",
    "CodexProfile",
    "parse_codex_profile",
    "JsonlParser",
    "JsonlParseResult",
    "parse_codex_jsonl",
]
