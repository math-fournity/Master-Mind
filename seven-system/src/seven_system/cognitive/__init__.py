"""WP-CW0 认知角色端口：provider-neutral ModelRolePort。

本包实现：
- RoleRegistry：冻结的机器认知角色注册表（append-only, hashed）
- RoleExecutionContract：绑定 role + profile + view policy + tool policy + adapter + capability
- ModelRolePort：provider-neutral 协议接口（dispatch / reattach / cancel / get_receipt）
- Attempt / AttemptReceipt：accepted → started → completed 状态机与收据
- FakeModelRoleAdapter：side-effect-free 测试适配器，确定性输出
- AttemptReconciler：识别 unknown-start / stale-fence / sensitive-sink / illegal-state

硬约束（AGENTS.md rule 4）：
- Devin CLI 不专属于 Solver；认知角色统一经 provider-neutral ModelRolePort
- DevinCliModelRoleAdapter 和 CodexExecModelRoleAdapter 是独立未来工作包（WP-CW-D1, WP-CW-C1）
- 本包只实现 fake adapter，不调用任何真实 CLI / DB / D-volume
- SIDE_EFFECT_FREE：纯内存实现

角色全集（来自 docs/implementation/05-execution-ports-and-carriers.md RoleTypeRegistry）：
  question_architect, adversarial_editor, math_verifier,
  trace_analyst, solution_analyst, adjudicator,
  process_auditor, proof_judge, leakage_auditor,
  selector, hint_renderer
"""

from .role_registry import (
    RoleDefinition,
    RoleRegistry,
    ROLE_REGISTRY_FROZEN_V1,
)
from .role_execution_contract import (
    RoleExecutionContract,
    verify_role_execution_contract,
)
from .model_role_port import (
    ModelRolePort,
    DispatchRequest,
    DispatchResult,
)
from .attempt import (
    Attempt,
    AttemptReceipt,
    AttemptState,
    verify_attempt_receipt,
)
from .fake_adapter import FakeModelRoleAdapter
from .reconcile import (
    AttemptReconciler,
    ReconcileResult,
)

__all__ = [
    "RoleDefinition",
    "RoleRegistry",
    "ROLE_REGISTRY_FROZEN_V1",
    "RoleExecutionContract",
    "verify_role_execution_contract",
    "ModelRolePort",
    "DispatchRequest",
    "DispatchResult",
    "Attempt",
    "AttemptReceipt",
    "AttemptState",
    "verify_attempt_receipt",
    "FakeModelRoleAdapter",
    "AttemptReconciler",
    "ReconcileResult",
]
