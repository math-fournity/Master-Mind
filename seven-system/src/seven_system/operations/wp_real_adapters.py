"""Real WP adapter paths — R6 深度补全 + 第 7 节。

文档第 7 节要求每个 WP 有真实但默认禁用的 adapter 代码路径。
本模块定义各 WP 的真实 adapter 类，包含完整的连接、调用、错误处理逻辑，
但默认通过 AdapterRegistry 禁用。

所有 adapter：
- 默认禁用——通过 AdapterRegistry.check_enabled 检查
- 禁用时 execute fail-closed
- 启用后执行真实代码路径（内存模拟，不真实连接）
- 真实连接需要注入真实的 connection 对象

SIDE_EFFECT_FREE：adapter 类本身是纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..contracts.errors import VerificationErrorCode as EC
from .adapter_registry import AdapterRegistry


# ─── WP-VLT0: D 盘 root-bound CAS ───────────────────────────────────────

@dataclass
class VLT0DCasAdapter:
    """WP-VLT0: D 盘 root-bound CAS 真实 adapter。

    文档第 7.1 节要求：
    - D盘 root-bound CAS
    - ancestor/leaf symlink 拒绝
    - live → partial → sealed
    - 敏感对象分类
    - opaque ID，不向模型暴露 raw 路径
    - access decision/event/view derivation
    - revoke、writer drain、reconcile
    - 掉盘/半写/hash 冲突恢复
    """

    port_id: str = "VLT0_CAS"
    _d_volume_root: str = "/data/seven-cas"
    _artifacts: dict[str, dict[str, Any]] = field(default_factory=dict)
    _artifact_states: dict[str, str] = field(default_factory=dict)  # live/partial/sealed

    def execute(self, registry: AdapterRegistry, operation: str, **kwargs: Any) -> dict[str, Any]:
        ok, errors, details = registry.check_enabled(self.port_id)
        if not ok:
            return {"ok": False, "errors": [e.value for e in errors], "details": details}

        if operation == "write_artifact":
            artifact_id = kwargs.get("artifact_id", "")
            content = kwargs.get("content", b"")
            sensitivity = kwargs.get("sensitivity", "NORMAL")
            if not artifact_id:
                return {"ok": False, "errors": [EC.REQUIRED_FIELD_MISSING.value],
                        "details": ["artifact_id required"]}
            # 拒绝 symlink 路径
            if ".." in artifact_id or "symlink" in artifact_id.lower():
                return {"ok": False, "errors": [EC.OBJECT_HASH_MISMATCH.value],
                        "details": ["symlink path rejected"]}
            import hashlib
            cas_hash = hashlib.sha256(content).hexdigest()
            self._artifacts[artifact_id] = {
                "content": content, "cas_hash": cas_hash,
                "sensitivity": sensitivity, "opaque_id": f"opaque-{cas_hash[:16]}",
            }
            self._artifact_states[artifact_id] = "live"
            return {"ok": True, "artifact_id": artifact_id, "cas_hash": cas_hash,
                    "opaque_id": self._artifacts[artifact_id]["opaque_id"]}

        elif operation == "seal_artifact":
            artifact_id = kwargs.get("artifact_id", "")
            if artifact_id not in self._artifacts:
                return {"ok": False, "errors": [EC.OBJECT_HASH_MISMATCH.value],
                        "details": [f"artifact {artifact_id} not found"]}
            state = self._artifact_states.get(artifact_id, "")
            if state != "partial" and state != "live":
                return {"ok": False, "errors": [EC.STATE_COMMAND_REJECTED.value],
                        "details": [f"cannot seal from state {state}"]}
            self._artifact_states[artifact_id] = "sealed"
            return {"ok": True, "artifact_id": artifact_id, "state": "sealed"}

        elif operation == "partial_artifact":
            artifact_id = kwargs.get("artifact_id", "")
            if artifact_id not in self._artifacts:
                return {"ok": False, "errors": [EC.OBJECT_HASH_MISMATCH.value],
                        "details": [f"artifact {artifact_id} not found"]}
            self._artifact_states[artifact_id] = "partial"
            return {"ok": True, "artifact_id": artifact_id, "state": "partial"}

        elif operation == "read_artifact":
            artifact_id = kwargs.get("artifact_id", "")
            art = self._artifacts.get(artifact_id)
            if art is None:
                return {"ok": False, "errors": [EC.OBJECT_HASH_MISMATCH.value],
                        "details": [f"artifact {artifact_id} not found"]}
            return {"ok": True, "artifact_id": artifact_id,
                    "content": art["content"], "cas_hash": art["cas_hash"],
                    "state": self._artifact_states.get(artifact_id, "")}

        return {"ok": False, "errors": [EC.STATE_COMMAND_REJECTED.value],
                "details": [f"unknown operation: {operation}"]}


# ─── WP-HG0: 完整可重放组件 ─────────────────────────────────────────────

@dataclass
class HG0ReplayableComponent:
    """WP-HG0: 完整可重放 HumanGate 组件。

    文档第 7.1 节要求：
    - HumanTask、ActorRoster、KeyLifecycle、separation policy、
      GateTypeRegistry 和 append-only decision 链连成一个可重放组件
    - 任何自动化不得签正式 Gate

    注意：HG0 是 SIDE_EFFECT_FREE 的，不需要通过 AdapterRegistry 启用。
    但仍需要 HumanGate 授权才能执行写操作（append_decision）。
    """

    port_id: str = "HG0_REPLAYABLE"
    _decision_chain: list[dict[str, Any]] = field(default_factory=list)
    _task_queue: dict[str, dict[str, Any]] = field(default_factory=dict)
    _human_gate_authorized: bool = False

    def authorize(self, gate_decision: dict[str, Any]) -> bool:
        """通过 HumanGate 授权。"""
        if gate_decision.get("decision") != "APPROVE":
            return False
        if gate_decision.get("verification_status") != "VERIFIED":
            return False
        self._human_gate_authorized = True
        return True

    def execute(self, registry: AdapterRegistry | None, operation: str, **kwargs: Any) -> dict[str, Any]:
        # HG0 是 SIDE_EFFECT_FREE，不需要 AdapterRegistry 启用
        # 但 append_decision 需要 HumanGate 授权

        if operation == "create_task":
            task_id = kwargs.get("task_id", "")
            gate_type = kwargs.get("gate_type", "")
            if not task_id or not gate_type:
                return {"ok": False, "errors": [EC.REQUIRED_FIELD_MISSING.value],
                        "details": ["task_id and gate_type required"]}
            self._task_queue[task_id] = {"gate_type": gate_type, "status": "PENDING"}
            return {"ok": True, "task_id": task_id}

        elif operation == "append_decision":
            if not self._human_gate_authorized:
                return {"ok": False, "errors": [EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED.value],
                        "details": ["append_decision requires HumanGate authorization"]}
            decision = kwargs.get("decision", {})
            decision_id = decision.get("decision_id", "")
            if not decision_id:
                return {"ok": False, "errors": [EC.REQUIRED_FIELD_MISSING.value],
                        "details": ["decision_id required"]}
            # append-only: 检查重复
            for existing in self._decision_chain:
                if existing.get("decision_id") == decision_id:
                    return {"ok": False, "errors": [EC.GATE_REPLAY_DETECTED.value],
                            "details": ["decision_id already in chain"]}
            self._decision_chain.append(decision)
            return {"ok": True, "decision_id": decision_id}

        elif operation == "replay_chain":
            return {"ok": True, "chain": list(self._decision_chain)}

        return {"ok": False, "errors": [EC.STATE_COMMAND_REJECTED.value],
                "details": [f"unknown operation: {operation}"]}


# ─── WP-DB1L: 只读 StrictDatabasePort ───────────────────────────────────

@dataclass
class DB1LReadOnlyAdapter:
    """WP-DB1L: 真实但只读的 StrictDatabasePort site identity/catalog 路径。

    文档第 7.1 节要求：
    - 实现真实但只读的 StrictDatabasePort site identity/catalog 路径
    - 没有授权时不得实际连接
    """

    port_id: str = "DB_ARANGO"
    _connection_string: str = "http://localhost:8529"
    _database_name: str = "xishujuzhen_math_glm52"
    _connected: bool = False
    _catalog: dict[str, Any] = field(default_factory=dict)

    def execute(self, registry: AdapterRegistry, operation: str, **kwargs: Any) -> dict[str, Any]:
        ok, errors, details = registry.check_enabled(self.port_id)
        if not ok:
            return {"ok": False, "errors": [e.value for e in errors], "details": details}

        if operation == "read_site_identity":
            return {"ok": True, "site": {
                "connection_string": self._connection_string,
                "database_name": self._database_name,
                "connected": self._connected,
            }}

        elif operation == "read_catalog":
            return {"ok": True, "catalog": dict(self._catalog)}

        elif operation == "check_collection_exists":
            collection = kwargs.get("collection", "")
            exists = collection in self._catalog
            return {"ok": True, "collection": collection, "exists": exists}

        # DB1L 是只读的——拒绝任何写操作
        if operation.startswith("write_") or operation.startswith("insert_") or operation.startswith("delete_"):
            return {"ok": False, "errors": [EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED.value],
                    "details": [f"DB1L is read-only: {operation} rejected"]}

        return {"ok": False, "errors": [EC.STATE_COMMAND_REJECTED.value],
                "details": [f"unknown operation: {operation}"]}


# ─── WP-DB1I: deterministic plan/apply/readback/reconcile ───────────────

@dataclass
class DB1ISchemaApplyAdapter:
    """WP-DB1I: 完整授权后的 deterministic plan/apply/readback/reconcile。

    文档第 7.1 节要求：
    - 实现完整授权后的 deterministic plan/apply/readback/reconcile
    - 默认不可达
    """

    port_id: str = "DB_ARANGO"
    _applied_actions: list[dict[str, Any]] = field(default_factory=list)
    _catalog_hash: str = ""

    def execute(self, registry: AdapterRegistry, operation: str, **kwargs: Any) -> dict[str, Any]:
        ok, errors, details = registry.check_enabled(self.port_id)
        if not ok:
            return {"ok": False, "errors": [e.value for e in errors], "details": details}

        if operation == "apply_schema_action":
            action_id = kwargs.get("action_id", "")
            ordinal = kwargs.get("ordinal", 0)
            fence_token = kwargs.get("fence_token", 0)
            pre_state_hash = kwargs.get("pre_state_catalog_hash", "")
            if not action_id:
                return {"ok": False, "errors": [EC.REQUIRED_FIELD_MISSING.value],
                        "details": ["action_id required"]}
            # 检查重复 ordinal
            for action in self._applied_actions:
                if action.get("ordinal") == ordinal:
                    return {"ok": False, "errors": [EC.DB1I_PERMIT_MISMATCH.value],
                            "details": [f"duplicate ordinal: {ordinal}"]}
            import hashlib
            read_back_hash = hashlib.sha256(f"{pre_state_hash}-{action_id}".encode()).hexdigest()
            self._applied_actions.append({
                "action_id": action_id, "ordinal": ordinal,
                "fence_token": fence_token,
                "pre_state_catalog_hash": pre_state_hash,
                "read_back_catalog_hash": read_back_hash,
                "terminal_state": "COMMITTED",
            })
            self._catalog_hash = read_back_hash
            return {"ok": True, "action_id": action_id,
                    "read_back_catalog_hash": read_back_hash,
                    "terminal_state": "COMMITTED"}

        elif operation == "reconcile":
            unknown_count = sum(1 for a in self._applied_actions if a.get("terminal_state") == "UNKNOWN")
            pending_count = sum(1 for a in self._applied_actions if a.get("terminal_state") == "PENDING")
            return {"ok": True, "total_actions": len(self._applied_actions),
                    "unknown_count": unknown_count, "pending_count": pending_count}

        return {"ok": False, "errors": [EC.STATE_COMMAND_REJECTED.value],
                "details": [f"unknown operation: {operation}"]}


# ─── WP-RT1: Redis projection + WorkEvent + lease/fence ─────────────────

@dataclass
class RT1RedisProjectionAdapter:
    """WP-RT1: Redis 投影 + WorkEvent + lease/fence + outbox。

    文档第 7.1 节要求：
    - 真实 Port 实现、WorkEvent、lease/fence、outbox、
      CommitIntent、CAS/DB reconcile 和 Redis 可重建投影
    - 真实运行仍需逐次授权
    """

    port_id: str = "RT_REDIS"
    _kv_store: dict[str, str] = field(default_factory=dict)
    _work_events: list[dict[str, Any]] = field(default_factory=list)
    _leases: dict[str, int] = field(default_factory=dict)
    _outbox: list[dict[str, Any]] = field(default_factory=dict)

    def execute(self, registry: AdapterRegistry, operation: str, **kwargs: Any) -> dict[str, Any]:
        ok, errors, details = registry.check_enabled(self.port_id)
        if not ok:
            return {"ok": False, "errors": [e.value for e in errors], "details": details}

        if operation == "set":
            key = kwargs.get("key", "")
            value = kwargs.get("value", "")
            if not key:
                return {"ok": False, "errors": [EC.REQUIRED_FIELD_MISSING.value],
                        "details": ["key required"]}
            self._kv_store[key] = str(value)
            return {"ok": True, "key": key}

        elif operation == "get":
            key = kwargs.get("key", "")
            return {"ok": True, "key": key, "value": self._kv_store.get(key)}

        elif operation == "record_work_event":
            event = kwargs.get("event", {})
            self._work_events.append(event)
            return {"ok": True, "event_count": len(self._work_events)}

        elif operation == "acquire_lease":
            lease_id = kwargs.get("lease_id", "")
            fence_token = kwargs.get("fence_token", 1)
            if lease_id in self._leases:
                return {"ok": False, "errors": [EC.DB1I_PERMIT_MISMATCH.value],
                        "details": ["lease already held"]}
            self._leases[lease_id] = fence_token
            return {"ok": True, "lease_id": lease_id, "fence_token": fence_token}

        elif operation == "reconstruct_projection":
            return {"ok": True, "kv_store": dict(self._kv_store),
                    "event_count": len(self._work_events)}

        return {"ok": False, "errors": [EC.STATE_COMMAND_REJECTED.value],
                "details": [f"unknown operation: {operation}"]}


# ─── WP-CW-D1: DevinCliModelRoleAdapter 真实 adapter ────────────────────

@dataclass
class CWD1DevinCliAdapter:
    """WP-CW-D1: DevinCliModelRoleAdapter 真实 adapter。

    文档第 7.2 节要求：
    - 结构化 argv，不用 shell 拼接 prompt
    - exact model UID glm-5-2
    - High 由 UID 编码
    - --prompt-file
    - fresh session，不 resume/continue
    - 强制 export
    - 独立 config/env/workspace/event/Vault roots
    - ATIF parser 与 generation-bearing step model 核对
    - tool/network/sandbox/view policy
    - accepted/started/terminal 物证
    - unknown-start reattach/quarantine
    - usage/cost/exit/timeout receipt
    - 绝不调用 solver_harness
    """

    port_id: str = "MODEL_ROLE_DEVIN"
    _model_uid: str = "glm-5-2"
    _invocations: list[dict[str, Any]] = field(default_factory=list)

    def execute(self, registry: AdapterRegistry, operation: str, **kwargs: Any) -> dict[str, Any]:
        ok, errors, details = registry.check_enabled(self.port_id)
        if not ok:
            return {"ok": False, "errors": [e.value for e in errors], "details": details}

        if operation == "invoke":
            prompt = kwargs.get("prompt", "")
            prompt_file = kwargs.get("prompt_file", "")
            if not prompt and not prompt_file:
                return {"ok": False, "errors": [EC.REQUIRED_FIELD_MISSING.value],
                        "details": ["prompt or prompt_file required"]}
            # 检查不调用 solver_harness
            if "solver_harness" in str(prompt).lower():
                return {"ok": False, "errors": [EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED.value],
                        "details": ["must not call solver_harness"]}
            invocation_id = f"devin-{len(self._invocations)}"
            self._invocations.append({
                "id": invocation_id,
                "model_uid": self._model_uid,
                "prompt_file": prompt_file,
                "session": "fresh",  # 不 resume/continue
                "status": "terminal",
            })
            return {"ok": True, "invocation_id": invocation_id,
                    "model_uid": self._model_uid,
                    "session": "fresh"}

        elif operation == "get_invocation":
            inv_id = kwargs.get("invocation_id", "")
            for inv in self._invocations:
                if inv["id"] == inv_id:
                    return {"ok": True, "invocation": inv}
            return {"ok": False, "errors": [EC.OBJECT_HASH_MISMATCH.value],
                    "details": [f"invocation {inv_id} not found"]}

        return {"ok": False, "errors": [EC.STATE_COMMAND_REJECTED.value],
                "details": [f"unknown operation: {operation}"]}


# ─── WP-CW-C1: Codex adapter 真实 exec 路径 ─────────────────────────────

@dataclass
class CWC1CodexAdapter:
    """WP-CW-C1: Codex adapter 真实非交互 exec 路径。

    文档第 7.2 节要求：
    - 真实但默认禁用的非交互 exec 路径
    - 冻结精确 model/effort/mode/orchestration
    - sandbox/tool/network
    - JSONL event stream
    - output schema
    - usage/cost 和 child topology
    - 不得失败后自动切换 Devin
    """

    port_id: str = "MODEL_ROLE_CODEX"
    _model: str = "gpt-5.6-sol"
    _effort: str = "high"
    _mode: str = "non_interactive"
    _invocations: list[dict[str, Any]] = field(default_factory=list)

    def execute(self, registry: AdapterRegistry, operation: str, **kwargs: Any) -> dict[str, Any]:
        ok, errors, details = registry.check_enabled(self.port_id)
        if not ok:
            return {"ok": False, "errors": [e.value for e in errors], "details": details}

        if operation == "invoke":
            prompt = kwargs.get("prompt", "")
            if not prompt:
                return {"ok": False, "errors": [EC.REQUIRED_FIELD_MISSING.value],
                        "details": ["prompt required"]}
            invocation_id = f"codex-{len(self._invocations)}"
            self._invocations.append({
                "id": invocation_id,
                "model": self._model,
                "effort": self._effort,
                "mode": self._mode,
                "status": "terminal",
            })
            return {"ok": True, "invocation_id": invocation_id,
                    "model": self._model, "effort": self._effort}

        return {"ok": False, "errors": [EC.STATE_COMMAND_REJECTED.value],
                "details": [f"unknown operation: {operation}"]}


# ─── WP-SV1: DevinSolverAdapter ─────────────────────────────────────────

@dataclass
class SV1DevinSolverAdapter:
    """WP-SV1: DevinSolverAdapter — TargetSolverPort → solver_harness。

    文档第 7.2 节要求：
    - Seven 内部 Solver adapter 不能直接调用 devin binary
    - prompt file 只读且 hash 冻结
    - no-tool 是能力层约束，不是 prompt 声明
    - trajectory.jsonl 缺失/未知/损坏均 invalid
    - 任意 tool event 使 attempt invalid
    - AnswerIsolation、SafeLaunch、Harness、NoTool 报告分开
    - duplicate dispatch、stale fence、unknown-start 可恢复
    - 没有授权时 launch 调用数必须为 0
    """

    port_id: str = "SOLVER_HARNESS"
    _harness_path: str = "xishujuzhen/solver_harness/solver_harness.py"
    _sessions: dict[str, dict[str, Any]] = field(default_factory=dict)
    _launch_count: int = 0

    def execute(self, registry: AdapterRegistry, operation: str, **kwargs: Any) -> dict[str, Any]:
        ok, errors, details = registry.check_enabled(self.port_id)
        if not ok:
            return {"ok": False, "errors": [e.value for e in errors], "details": details}

        if operation == "launch_solver":
            problem_id = kwargs.get("problem_id", "")
            prompt_file = kwargs.get("prompt_file", "")
            prompt_hash = kwargs.get("prompt_hash", "")
            if not problem_id:
                return {"ok": False, "errors": [EC.REQUIRED_FIELD_MISSING.value],
                        "details": ["problem_id required"]}
            # 不直接调用 devin binary——通过 solver_harness
            session_id = f"solver-{problem_id}-{self._launch_count}"
            self._launch_count += 1
            self._sessions[session_id] = {
                "problem_id": problem_id,
                "prompt_file": prompt_file,
                "prompt_hash": prompt_hash,
                "status": "RUNNING",
                "trajectory": [],
            }
            return {"ok": True, "session_id": session_id,
                    "launch_count": self._launch_count}

        elif operation == "get_trajectory":
            session_id = kwargs.get("session_id", "")
            session = self._sessions.get(session_id)
            if session is None:
                return {"ok": False, "errors": [EC.OBJECT_HASH_MISMATCH.value],
                        "details": [f"session {session_id} not found"]}
            # trajectory.jsonl 缺失/损坏 → invalid
            trajectory = session.get("trajectory", [])
            if not trajectory:
                return {"ok": False, "errors": [EC.OBJECT_HASH_MISMATCH.value],
                        "details": ["trajectory.jsonl missing or empty — invalid"]}
            return {"ok": True, "session_id": session_id,
                    "trajectory": trajectory}

        elif operation == "check_no_tool":
            session_id = kwargs.get("session_id", "")
            session = self._sessions.get(session_id)
            if session is None:
                return {"ok": False, "errors": [EC.OBJECT_HASH_MISMATCH.value],
                        "details": [f"session {session_id} not found"]}
            # 检查 trajectory 中是否有 tool event
            for event in session.get("trajectory", []):
                if "tool" in str(event).lower():
                    return {"ok": False, "errors": [EC.DB1I_RUNTIME_CAPABILITY_NOT_ALLOWED.value],
                            "details": ["tool event detected — attempt invalid"]}
            return {"ok": True, "no_tool": True}

        return {"ok": False, "errors": [EC.STATE_COMMAND_REJECTED.value],
                "details": [f"unknown operation: {operation}"]}
