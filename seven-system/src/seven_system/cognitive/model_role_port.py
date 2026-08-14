"""ModelRolePort — provider-neutral 认知角色端口协议。

来自 docs/implementation/05-execution-ports-and-carriers.md：

    class ModelRolePort(Protocol):
        def prepare(self, job): ...
        def submit(self, prepared_job): ...
        def observe(self, ticket): ...
        def collect(self, ticket): ...
        def reattach(self, attempt_id, fence_token): ...
        def cancel(self, ticket, fence_token): ...
        def reconcile(self, attempt_id, fence_token): ...

本模块冻结协议接口和数据结构。具体 adapter 实现（DevinCliModelRoleAdapter、
CodexExecModelRoleAdapter）是独立未来工作包（WP-CW-D1, WP-CW-C1）。
本工作包只实现 FakeModelRoleAdapter。

硬约束（AGENTS.md rule 4）：
- Devin CLI 不专属于 Solver；认知角色统一经 provider-neutral ModelRolePort
- DevinCliModelRoleAdapter 不得复用 Solver 的 port、workspace、session、AGENTS、
  能力报告、收据或资源池
- 人工复核/人门分别走未来 HumanTaskPort/HumanGateService；禁止阶段代码旁路调用任何 CLI
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable

from .role_execution_contract import RoleExecutionContract
from .attempt import Attempt, AttemptReceipt


@dataclass(frozen=True)
class DispatchRequest:
    """dispatch 请求：将 RoleExecutionContract + 输入提交给 adapter。

    输入是派生后的 view bytes（opaque view_id/sink_id + derived bytes），
    不含 raw Vault 路径或 CAS locator。
    """

    contract: RoleExecutionContract
    input_view_bytes: bytes
    input_view_id: str
    sink_id: str
    fence_token: str
    timeout_seconds: float = 0.0  # 0 = 无超时

    def to_summary(self) -> dict[str, Any]:
        return {
            "role_job_id": self.contract.role_job_id,
            "role_type_id": self.contract.role_type_id,
            "adapter_kind": self.contract.adapter_kind,
            "input_view_id": self.input_view_id,
            "sink_id": self.sink_id,
            "input_bytes_len": len(self.input_view_bytes),
            "timeout_seconds": self.timeout_seconds,
        }


@dataclass(frozen=True)
class DispatchResult:
    """dispatch 结果：包含 attempt 和初始 receipt。"""

    attempt: Attempt
    receipt: AttemptReceipt
    accepted: bool = False

    @property
    def attempt_id(self) -> str:
        return self.attempt.attempt_id


@runtime_checkable
class ModelRolePort(Protocol):
    """Provider-neutral 认知角色端口协议。

    所有 adapter（fake / Devin CLI / Codex exec / OpenAI Responses）必须实现此协议。
    协议方法：

    - dispatch(request) → DispatchResult：提交角色 job，返回 attempt + receipt
    - reattach(attempt_id, fence_token) → AttemptReceipt：重新附加到已有 attempt
    - cancel(attempt_id, fence_token) → AttemptReceipt：取消 attempt
    - get_receipt(attempt_id) → AttemptReceipt：获取当前 receipt
    """

    def dispatch(self, request: DispatchRequest) -> DispatchResult:
        """提交角色 job 到 adapter。

        执行 attempt 状态机：CREATED → ACCEPTED → STARTED → COMPLETED
        返回 DispatchResult，包含 attempt 和最终 receipt。
        """
        ...

    def reattach(self, attempt_id: str, fence_token: str) -> AttemptReceipt:
        """重新附加到已有 attempt。

        仅在稳定 thread/session/response ID 和该 backend 的 CapabilityReport
        证明可行时允许。否则在 profile 中预声明 UNSUPPORTED。
        """
        ...

    def cancel(self, attempt_id: str, fence_token: str) -> AttemptReceipt:
        """取消 attempt。

        携带 fence token 并记录发送、provider 确认和终态。
        cancel 超时不能假定未生成。
        """
        ...

    def get_receipt(self, attempt_id: str) -> AttemptReceipt:
        """获取 attempt 的当前 receipt。"""
        ...
