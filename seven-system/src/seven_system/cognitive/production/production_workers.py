"""P3NWorkers / P6Workers / DBLeaseReconcileIntegration — 生产认知工人。

来自 docs/implementation/09-phase-pipeline-p0-p9.md：

P3N Natural Case Review：
- 独立 Trace/Solution 视角形成 MechanismContract、RelationMapping、
  数学核验和对抗捷径审查
- trace_analyst / solution_analyst / adjudicator 三个角色
- 每个使用 DB lease/reconcile（RT1），独立 session 强制

P6 Independent Audits：
- 三个独立审计（Process Auditor / Proof Judge / Leakage Auditor）
- Blinding enforced（每个获得独立 view）
- 同会话审稿 = blocker
- Judge 读越权 view = blocker
- 分别 seal 后组装 RunAudit；单 episode 只陈述观察事实

DBLeaseReconcileIntegration：
- Workers 使用 RT1 的 lease/fence 进行 DB 访问
- Reconcile on crash recovery
- WorkEvent logging for all state transitions

SIDE_EFFECT_FREE：纯内存实现，使用 RT1 的 LeaseFenceManager / WorkEventLog。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    CW_P3N_ROLES,
    CW_P6_ROLES,
    CW_ALLOWED_OUTPUT_KINDS,
    CW_FORBIDDEN_OUTPUT_KINDS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult
from ...runtime.lease_fence import LeaseFenceManager, LeaseError
from ...runtime.work_event import WorkEvent, WorkEventLog, WorkEventError
from .independence_enforcer import IndependenceEnforcer, WorkerSession
from .production_role_router import ProductionRoleRouter, RouterDecision


# ─── Worker output kinds ────────────────────────────────────────────────

# P3N 各角色的输出种类
_P3N_OUTPUT_KINDS: dict[str, str] = {
    "trace_analyst": "MechanismContract",
    "solution_analyst": "RelationMapping",
    "adjudicator": "NaturalCaseReviewBundle",
}

# P6 各角色的输出种类
_P6_OUTPUT_KINDS: dict[str, str] = {
    "process_auditor": "ProcessAuditRecord",
    "proof_judge": "ProofJudgmentRecord",
    "leakage_auditor": "LeakageAuditRecord",
}


# ─── WorkerState ────────────────────────────────────────────────────────


@dataclass
class WorkerState:
    """单个 worker 的运行状态。"""

    worker_id: str
    role_type_id: str
    session_id: str
    model_uid: str
    carrier_id: str
    view_id: str
    lease_id: str = ""
    fence_token: int = 0
    state: str = "PENDING"  # PENDING → LEASED → DISPATCHED → COMPLETED / FAILED
    output_kind: str = ""
    output_hash: str = ""
    sealed: bool = False
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "worker_id": self.worker_id,
            "role_type_id": self.role_type_id,
            "session_id": self.session_id,
            "model_uid": self.model_uid,
            "carrier_id": self.carrier_id,
            "view_id": self.view_id,
            "lease_id": self.lease_id,
            "fence_token": self.fence_token,
            "state": self.state,
            "output_kind": self.output_kind,
            "output_hash": self.output_hash,
            "sealed": self.sealed,
            "error_codes": [ec.value for ec in self.error_codes],
            "details": list(self.details),
        }


# ─── DBLeaseReconcileIntegration ────────────────────────────────────────


@dataclass
class DBLeaseReconcileIntegration:
    """DB lease/reconcile 集成 — 使用 RT1 的 lease/fence 和 WorkEvent。

    Workers 通过此对象获取 DB lease、记录 WorkEvent、执行 reconcile。
    所有状态在内存中模拟，不接触真实 DB。
    """

    lease_manager: LeaseFenceManager = field(default_factory=LeaseFenceManager)
    event_log: WorkEventLog = field(default_factory=WorkEventLog)
    # aggregate_id → last sequence（用于 event 追加）
    _aggregate_seq: dict[str, int] = field(default_factory=dict)

    def acquire_lease(
        self,
        *,
        worker_id: str,
        aggregate_id: str,
        ttl_seconds: int = 300,
        current_time: str = "2026-08-14T12:00:00Z",
    ) -> tuple[int, str, list[EC]]:
        """获取 DB lease。

        返回 (fence_token, lease_id, errors)。
        失败时 errors 非空，fence_token=0。
        """
        lease_id = f"lease-{worker_id}"
        try:
            lease = self.lease_manager.acquire(
                lease_id=lease_id,
                aggregate_id=aggregate_id,
                holder=worker_id,
                ttl_seconds=ttl_seconds,
                current_time=current_time,
            )
            # 记录 LEASE_ACQUIRED event
            self._append_event(
                aggregate_id=aggregate_id,
                event_type="LEASE_ACQUIRED",
                fence_token=lease.fence_token,
                actor_or_rule=worker_id,
                payload={"lease_id": lease.lease_id, "holder": worker_id},
            )
            return lease.fence_token, lease.lease_id, []
        except LeaseError as e:
            return 0, "", [e.code]

    def release_lease(
        self,
        *,
        lease_id: str,
        fence_token: int,
        aggregate_id: str,
        worker_id: str,
    ) -> list[EC]:
        """释放 DB lease。"""
        try:
            self.lease_manager.release(
                lease_id=lease_id,
                fence_token=fence_token,
            )
            self._append_event(
                aggregate_id=aggregate_id,
                event_type="LEASE_RELEASED",
                fence_token=fence_token,
                actor_or_rule=worker_id,
                payload={"lease_id": lease_id},
            )
            return []
        except LeaseError as e:
            return [e.code]

    def reconcile_worker(
        self,
        *,
        worker_state: WorkerState,
        expected_fence_token: int,
        aggregate_id: str,
    ) -> list[EC]:
        """Reconcile on crash recovery — 检查 fence 一致性。

        如果 worker 的 fence_token 与当前有效 fence 不匹配，
        说明 worker 在崩溃后 fence 已被新 worker 取代。
        """
        errors: list[EC] = []
        current_fence = self.lease_manager.get_current_fence(aggregate_id)

        if worker_state.fence_token != expected_fence_token:
            errors.append(EC.CW_RECONCILE_FENCE_MISMATCH)
            return errors

        if self.lease_manager.is_stale_fence(aggregate_id, worker_state.fence_token):
            errors.append(EC.CW_RECONCILE_FENCE_MISMATCH)
            return errors

        # 记录 RECONCILE_COMPLETED event
        self._append_event(
            aggregate_id=aggregate_id,
            event_type="RECONCILE_COMPLETED",
            fence_token=worker_state.fence_token,
            actor_or_rule=worker_state.worker_id,
            payload={
                "worker_id": worker_state.worker_id,
                "state": worker_state.state,
                "consistent": len(errors) == 0,
            },
        )
        return errors

    def log_state_change(
        self,
        *,
        aggregate_id: str,
        worker_id: str,
        fence_token: int,
        old_state: str,
        new_state: str,
    ) -> list[EC]:
        """记录 worker 状态转换的 WorkEvent。"""
        try:
            self._append_event(
                aggregate_id=aggregate_id,
                event_type="WORK_ITEM_STATE_CHANGED",
                fence_token=fence_token,
                actor_or_rule=worker_id,
                payload={
                    "worker_id": worker_id,
                    "old_state": old_state,
                    "new_state": new_state,
                },
            )
            return []
        except WorkEventError as e:
            return [e.code]

    def _append_event(
        self,
        *,
        aggregate_id: str,
        event_type: str,
        fence_token: int,
        actor_or_rule: str,
        payload: dict[str, Any],
    ) -> None:
        """追加 WorkEvent。"""
        seq = self._aggregate_seq.get(aggregate_id, -1) + 1
        event_id = f"evt-{aggregate_id}-{seq}"
        event = WorkEvent.build(
            event_id=event_id,
            aggregate_id=aggregate_id,
            sequence=seq,
            event_type=event_type,
            fence_token=fence_token,
            actor_or_rule=actor_or_rule,
            payload=payload,
        )
        self.event_log.append(event)
        self._aggregate_seq[aggregate_id] = seq

    @property
    def events(self) -> list[WorkEvent]:
        return self.event_log.events


# ─── P3NWorkers ─────────────────────────────────────────────────────────


@dataclass
class P3NWorkers:
    """P3N 自然题审查工人。

    三个角色：trace_analyst / solution_analyst / adjudicator。
    每个使用 DB lease/reconcile，独立 session 强制。
    独立 Trace/Solution 视角形成 MechanismContract、RelationMapping、
    数学核验和对抗捷径审查。
    """

    router: ProductionRoleRouter
    db_integration: DBLeaseReconcileIntegration
    independence: IndependenceEnforcer = field(default_factory=IndependenceEnforcer)
    workers: dict[str, WorkerState] = field(default_factory=dict)
    # aggregate_id 前缀
    aggregate_prefix: str = "p3n"

    def dispatch_worker(
        self,
        *,
        role_type_id: str,
        worker_id: str,
        session_id: str,
        model_uid: str,
        carrier_id: str,
        carrier_profile_hash: str,
        view_id: str,
        current_time: str = "2026-08-14T12:00:00Z",
    ) -> WorkerState:
        """dispatch 一个 P3N worker。

        流程：
        1. 验证 role_type_id 在 P3N 角色集中
        2. 通过 ProductionRoleRouter 路由
        3. 获取 DB lease
        4. 注册独立 session
        5. 生成确定性输出
        6. seal 输出
        """
        errors: list[EC] = []
        details: list[str] = []

        state = WorkerState(
            worker_id=worker_id,
            role_type_id=role_type_id,
            session_id=session_id,
            model_uid=model_uid,
            carrier_id=carrier_id,
            view_id=view_id,
        )
        self.workers[worker_id] = state

        # 1. 验证角色
        if role_type_id not in CW_P3N_ROLES:
            errors.append(EC.CW_ROLE_TYPE_UNKNOWN)
            details.append(f"role {role_type_id} not in P3N roles {sorted(CW_P3N_ROLES)}")
            state.state = "FAILED"
            state.error_codes = errors
            state.details = details
            return state

        # 2. 路由
        decision = self.router.route(
            role_type_id=role_type_id,
            carrier_id=carrier_id,
            model_id=model_uid,
            carrier_profile_hash=carrier_profile_hash,
        )
        if not decision.is_dispatch:
            errors.extend(decision.error_codes)
            details.extend(decision.details)
            state.state = "FAILED"
            state.error_codes = errors
            state.details = details
            return state

        # 3. 获取 DB lease
        aggregate_id = f"{self.aggregate_prefix}-{worker_id}"
        fence_token, lease_id, lease_errors = self.db_integration.acquire_lease(
            worker_id=worker_id,
            aggregate_id=aggregate_id,
            current_time=current_time,
        )
        if lease_errors:
            errors.extend(lease_errors)
            details.append(f"lease acquire failed for {worker_id}")
            state.state = "FAILED"
            state.error_codes = errors
            state.details = details
            return state

        state.lease_id = lease_id
        state.fence_token = fence_token
        state.state = "LEASED"

        # 记录状态转换
        self.db_integration.log_state_change(
            aggregate_id=aggregate_id,
            worker_id=worker_id,
            fence_token=fence_token,
            old_state="PENDING",
            new_state="LEASED",
        )

        # 4. 注册独立 session
        session = WorkerSession(
            worker_id=worker_id,
            role_type_id=role_type_id,
            model_uid=model_uid,
            session_id=session_id,
            carrier_id=carrier_id,
            view_id=view_id,
        )
        self.independence.register_session(session)

        # 5. 生成确定性输出
        state.state = "DISPATCHED"
        self.db_integration.log_state_change(
            aggregate_id=aggregate_id,
            worker_id=worker_id,
            fence_token=fence_token,
            old_state="LEASED",
            new_state="DISPATCHED",
        )

        output_kind = _P3N_OUTPUT_KINDS.get(role_type_id, "")
        if output_kind in CW_FORBIDDEN_OUTPUT_KINDS:
            errors.append(EC.CW_OUTPUT_KIND_FORBIDDEN)
            details.append(f"output kind {output_kind} is forbidden")
            state.state = "FAILED"
            state.error_codes = errors
            state.details = details
            return state

        output_payload = {
            "worker_id": worker_id,
            "role_type_id": role_type_id,
            "session_id": session_id,
            "view_id": view_id,
            "output_kind": output_kind,
        }
        output_hash = hashlib.sha256(canonical_json_bytes(output_payload)).hexdigest()
        state.output_kind = output_kind
        state.output_hash = output_hash

        # 6. seal
        state.state = "COMPLETED"
        state.sealed = True
        self.db_integration.log_state_change(
            aggregate_id=aggregate_id,
            worker_id=worker_id,
            fence_token=fence_token,
            old_state="DISPATCHED",
            new_state="COMPLETED",
        )

        # 释放 lease
        self.db_integration.release_lease(
            lease_id=lease_id,
            fence_token=fence_token,
            aggregate_id=aggregate_id,
            worker_id=worker_id,
        )

        return state

    def verify_independence(self) -> VerificationResult:
        """验证 P3N workers 的独立性。"""
        return self.independence.verify_independence()

    def reconcile_worker(
        self,
        worker_id: str,
        expected_fence_token: int,
    ) -> list[EC]:
        """reconcile 一个 worker（crash recovery）。"""
        state = self.workers.get(worker_id)
        if state is None:
            return [EC.REQUIRED_FIELD_MISSING]
        aggregate_id = f"{self.aggregate_prefix}-{worker_id}"
        return self.db_integration.reconcile_worker(
            worker_state=state,
            expected_fence_token=expected_fence_token,
            aggregate_id=aggregate_id,
        )


# ─── P6Workers ──────────────────────────────────────────────────────────


@dataclass
class P6Workers:
    """P6 独立三审工人。

    三个角色：process_auditor / proof_judge / leakage_auditor。
    Blinding enforced（每个获得独立 view）。
    同会话审稿 = blocker。
    Judge 读越权 view = blocker。
    分别 seal 后组装 RunAudit；单 episode 只陈述观察事实。
    """

    router: ProductionRoleRouter
    db_integration: DBLeaseReconcileIntegration
    independence: IndependenceEnforcer = field(default_factory=IndependenceEnforcer)
    workers: dict[str, WorkerState] = field(default_factory=dict)
    # view_id → 授权的 worker_id 集合（blinding broker 分配）
    view_assignments: dict[str, set[str]] = field(default_factory=dict)
    aggregate_prefix: str = "p6"
    # 组装的 RunAudit
    run_audit_hash: str = ""
    run_audit_assembled: bool = False

    def dispatch_auditor(
        self,
        *,
        role_type_id: str,
        worker_id: str,
        session_id: str,
        model_uid: str,
        carrier_id: str,
        carrier_profile_hash: str,
        view_id: str,
        current_time: str = "2026-08-14T12:00:00Z",
    ) -> WorkerState:
        """dispatch 一个 P6 审计 worker。

        流程：
        1. 验证 role_type_id 在 P6 角色集中
        2. 通过 ProductionRoleRouter 路由
        3. 获取 DB lease
        4. 注册独立 session + blinding view
        5. 生成确定性输出（seal）
        """
        errors: list[EC] = []
        details: list[str] = []

        state = WorkerState(
            worker_id=worker_id,
            role_type_id=role_type_id,
            session_id=session_id,
            model_uid=model_uid,
            carrier_id=carrier_id,
            view_id=view_id,
        )
        self.workers[worker_id] = state

        # 1. 验证角色
        if role_type_id not in CW_P6_ROLES:
            errors.append(EC.CW_ROLE_TYPE_UNKNOWN)
            details.append(f"role {role_type_id} not in P6 roles {sorted(CW_P6_ROLES)}")
            state.state = "FAILED"
            state.error_codes = errors
            state.details = details
            return state

        # 2. 路由
        decision = self.router.route(
            role_type_id=role_type_id,
            carrier_id=carrier_id,
            model_id=model_uid,
            carrier_profile_hash=carrier_profile_hash,
        )
        if not decision.is_dispatch:
            errors.extend(decision.error_codes)
            details.extend(decision.details)
            state.state = "FAILED"
            state.error_codes = errors
            state.details = details
            return state

        # 3. 获取 DB lease
        aggregate_id = f"{self.aggregate_prefix}-{worker_id}"
        fence_token, lease_id, lease_errors = self.db_integration.acquire_lease(
            worker_id=worker_id,
            aggregate_id=aggregate_id,
            current_time=current_time,
        )
        if lease_errors:
            errors.extend(lease_errors)
            details.append(f"lease acquire failed for {worker_id}")
            state.state = "FAILED"
            state.error_codes = errors
            state.details = details
            return state

        state.lease_id = lease_id
        state.fence_token = fence_token
        state.state = "LEASED"

        self.db_integration.log_state_change(
            aggregate_id=aggregate_id,
            worker_id=worker_id,
            fence_token=fence_token,
            old_state="PENDING",
            new_state="LEASED",
        )

        # 4. 注册独立 session + blinding view
        session = WorkerSession(
            worker_id=worker_id,
            role_type_id=role_type_id,
            model_uid=model_uid,
            session_id=session_id,
            carrier_id=carrier_id,
            view_id=view_id,
        )
        self.independence.register_session(session)
        # blinding: view 只授权给该 worker
        self.view_assignments.setdefault(view_id, set()).add(worker_id)

        # 5. 生成确定性输出
        state.state = "DISPATCHED"
        self.db_integration.log_state_change(
            aggregate_id=aggregate_id,
            worker_id=worker_id,
            fence_token=fence_token,
            old_state="LEASED",
            new_state="DISPATCHED",
        )

        output_kind = _P6_OUTPUT_KINDS.get(role_type_id, "")
        if output_kind in CW_FORBIDDEN_OUTPUT_KINDS:
            errors.append(EC.CW_OUTPUT_KIND_FORBIDDEN)
            details.append(f"output kind {output_kind} is forbidden")
            state.state = "FAILED"
            state.error_codes = errors
            state.details = details
            return state

        output_payload = {
            "worker_id": worker_id,
            "role_type_id": role_type_id,
            "session_id": session_id,
            "view_id": view_id,
            "output_kind": output_kind,
            "episode": "single",  # 单 episode 只陈述观察事实
        }
        output_hash = hashlib.sha256(canonical_json_bytes(output_payload)).hexdigest()
        state.output_kind = output_kind
        state.output_hash = output_hash

        # seal
        state.state = "COMPLETED"
        state.sealed = True
        self.db_integration.log_state_change(
            aggregate_id=aggregate_id,
            worker_id=worker_id,
            fence_token=fence_token,
            old_state="DISPATCHED",
            new_state="COMPLETED",
        )

        # 释放 lease
        self.db_integration.release_lease(
            lease_id=lease_id,
            fence_token=fence_token,
            aggregate_id=aggregate_id,
            worker_id=worker_id,
        )

        return state

    def check_judge_view_access(
        self,
        judge_worker_id: str,
        requested_view_id: str,
    ) -> list[EC]:
        """检查 judge 是否试图读取越权 view。"""
        state = self.workers.get(judge_worker_id)
        if state is None:
            return [EC.REQUIRED_FIELD_MISSING]

        session_map = {s.worker_id: s for s in self.independence.sessions}
        judge_session = session_map.get(judge_worker_id)
        if judge_session is None:
            return [EC.REQUIRED_FIELD_MISSING]

        violations = self.independence.check_judge_view_isolation(
            judge_session, requested_view_id
        )
        return [v.error_code for v in violations]

    def assemble_run_audit(self) -> tuple[str, list[EC]]:
        """组装 RunAudit — 三个审计分别 seal 后组装。

        返回 (run_audit_hash, errors)。
        单 episode 只陈述观察事实。
        """
        errors: list[EC] = []

        # 检查所有 P6 worker 是否都 sealed
        sealed_workers: list[WorkerState] = []
        for wid, state in self.workers.items():
            if state.role_type_id not in CW_P6_ROLES:
                continue
            if not state.sealed:
                errors.append(EC.REQUIRED_FIELD_MISSING)
                errors.append(EC.CW_CELL_CONCLUSION_MISSING)
                break
            else:
                sealed_workers.append(state)
        else:
            # 检查独立性
            indep_result = self.verify_independence()
            if not indep_result.passed:
                errors.extend(indep_result.error_codes)

            if not errors and len(sealed_workers) >= 1:
                # 组装 RunAudit
                audit_payload = {
                    "kind": "RunAudit",
                    "audits": [
                        {
                            "worker_id": w.worker_id,
                            "role_type_id": w.role_type_id,
                            "output_kind": w.output_kind,
                            "output_hash": w.output_hash,
                        }
                        for w in sealed_workers
                    ],
                    "episode": "single",
                }
                self.run_audit_hash = hashlib.sha256(
                    canonical_json_bytes(audit_payload)
                ).hexdigest()
                self.run_audit_assembled = True
                return self.run_audit_hash, []

        return "", errors

    def verify_independence(self) -> VerificationResult:
        """验证 P6 workers 的独立性。"""
        return self.independence.verify_independence()

    def reconcile_worker(
        self,
        worker_id: str,
        expected_fence_token: int,
    ) -> list[EC]:
        """reconcile 一个 worker（crash recovery）。"""
        state = self.workers.get(worker_id)
        if state is None:
            return [EC.REQUIRED_FIELD_MISSING]
        aggregate_id = f"{self.aggregate_prefix}-{worker_id}"
        return self.db_integration.reconcile_worker(
            worker_state=state,
            expected_fence_token=expected_fence_token,
            aggregate_id=aggregate_id,
        )
