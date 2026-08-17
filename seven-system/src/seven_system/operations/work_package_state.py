"""WorkPackageStateService — R5: DAG 依赖强制执行与 board 投影。

R5 整改：审计发现 22 个工作包曾被越级标为 IMPLEMENTED_PENDING_EVIDENCE，
但 development dependency 未满足（GV0 未到 READY_FOR_AUDIT）。
本服务根据 canonical DAG 强制执行：
1. 工作包只能从 NOT_STARTED → IN_PROGRESS（不能越级）
2. 进入 IN_PROGRESS 前，所有 development_dependencies 必须处于
   READY_FOR_AUDIT 或 AUDITED_PASS 状态
3. 进入 READY_FOR_AUDIT 前，工作包必须处于 IN_PROGRESS
4. 进入 AUDITED_PASS 前，工作包必须处于 READY_FOR_AUDIT 且有 AuditRecord

R5 补全：
5. complete 命令——验证 completion contract、owner、状态命令
6. activate 命令——验证 activation dependencies、Permit、Reservation
7. Plan 验证——start 前检查 Plan 存在且 schema-valid
8. audit debt 继承——记录 inherited audit debt
9. board append-only 事件源——状态变更记录为事件
10. 双向对账——board/implementation-status/capabilities 一致性

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB/D 盘/模型。
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..contracts.errors import VALID_STATES, VerificationErrorCode as EC
from ..contracts.completion_contract import verify_completion_contract
from ..contracts.work_package_plan import (
    VerifiedWorkPackagePlan,
    verify_work_package_plan_file,
)
from ..hashing import file_sha256


# 合法的状态转换
_LEGAL_TRANSITIONS: dict[str, frozenset[str]] = {
    "NOT_STARTED": frozenset({"IN_PROGRESS", "BLOCKED"}),
    "READY": frozenset({"IN_PROGRESS", "BLOCKED"}),
    "IN_PROGRESS": frozenset({"IMPLEMENTED_PENDING_EVIDENCE", "READY_FOR_AUDIT", "BLOCKED"}),
    "IMPLEMENTED_PENDING_EVIDENCE": frozenset({"READY_FOR_AUDIT", "IN_PROGRESS", "BLOCKED"}),
    "READY_FOR_AUDIT": frozenset({"AUDITED_PASS", "AUDITED_PARTIAL", "AUDITED_FAIL", "IN_PROGRESS"}),
    "AUDITED_PASS": frozenset(),  # terminal
    "AUDITED_PARTIAL": frozenset({"IN_PROGRESS", "READY_FOR_AUDIT"}),
    "AUDITED_FAIL": frozenset({"IN_PROGRESS", "READY_FOR_AUDIT"}),
    "BLOCKED": frozenset({"NOT_STARTED", "IN_PROGRESS"}),
}

# development dependency 满足的最低状态
_DEV_DEP_MIN_STATES = frozenset({"READY_FOR_AUDIT", "AUDITED_PASS"})

# activation dependency 满足的最低状态
_ACT_DEP_MIN_STATES = frozenset({"AUDITED_PASS"})

# implementer 不能写的状态
_IMPLEMENTER_FORBIDDEN_STATES = frozenset({"AUDITED_PASS", "AUDITED_PARTIAL", "AUDITED_FAIL"})


@dataclass
class StateEvent:
    """状态变更事件——append-only。"""

    event_id: str
    wp_id: str
    from_state: str
    to_state: str
    timestamp: str
    actor_type: str  # "IMPLEMENTER" | "AUDITOR" | "SYSTEM"
    command: str  # "start" | "complete" | "activate" | "transition"
    details: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "wp_id": self.wp_id,
            "from_state": self.from_state,
            "to_state": self.to_state,
            "timestamp": self.timestamp,
            "actor_type": self.actor_type,
            "command": self.command,
            "details": list(self.details),
        }


@dataclass
class WorkPackageStateService:
    """WorkPackageStateService — DAG 依赖强制执行器。

    持有：
    - dag_path: canonical DAG 路径
    - wp_states: wp_id → 当前状态
    - wp_plans: wp_id → 已执行Schema/self-hash/DAG绑定验证的冻结Plan
    - wp_audit_debt: wp_id → inherited audit debt list
    - event_log: append-only 状态变更事件
    - _dag: 加载的 DAG（lazy）
    """

    dag_path: Path
    wp_states: dict[str, str] = field(default_factory=dict)
    wp_plans: dict[str, VerifiedWorkPackagePlan] = field(default_factory=dict)
    wp_completion_objects: dict[str, dict[str, Any]] = field(default_factory=dict)
    wp_audit_objects: dict[str, dict[str, Any]] = field(default_factory=dict)
    wp_audit_debt: dict[str, list[dict[str, str]]] = field(default_factory=dict)
    event_log: list[StateEvent] = field(default_factory=list)
    _dag: dict[str, Any] | None = None
    _dag_index: dict[str, dict[str, Any]] = field(default_factory=dict)
    _event_counter: int = 0

    def _load_dag(self) -> dict[str, Any]:
        """加载 DAG（lazy）。"""
        if self._dag is None:
            with open(self.dag_path, "r", encoding="utf-8") as f:
                self._dag = json.load(f)
            for wp in self._dag.get("work_packages", []):
                self._dag_index[wp["wp_id"]] = wp
        return self._dag

    def _get_wp_spec(self, wp_id: str) -> dict[str, Any]:
        """获取 WP 的 DAG spec。"""
        self._load_dag()
        if wp_id not in self._dag_index:
            raise ValueError(f"unknown wp_id: {wp_id}")
        return self._dag_index[wp_id]

    def _record_event(
        self, wp_id: str, from_state: str, to_state: str,
        actor_type: str, command: str, details: list[str] | None = None,
    ) -> None:
        """记录状态变更事件（append-only）。"""
        self._event_counter += 1
        event = StateEvent(
            event_id=f"evt-{self._event_counter:06d}",
            wp_id=wp_id,
            from_state=from_state,
            to_state=to_state,
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            actor_type=actor_type,
            command=command,
            details=details or [],
        )
        self.event_log.append(event)

    def get_state(self, wp_id: str) -> str:
        """获取 WP 当前状态。默认 NOT_STARTED。"""
        return self.wp_states.get(wp_id, "NOT_STARTED")

    def register_plan(
        self, wp_id: str, plan_ref: str | Path, expected_file_sha256: str,
    ) -> tuple[bool, list[EC], list[str]]:
        """读取并注册一个经过完整验证的冻结Plan。

        调用者给出的path/hash pair不是证据。这里会读取实际文件、执行
        WorkPackagePlan Schema、重算plan self-hash、绑定canonical DAG，并
        保存不可变snapshot。相同WP不能静默替换为另一个Plan。
        """
        result = verify_work_package_plan_file(
            plan_path=Path(plan_ref),
            dag_path=self.dag_path,
            expected_wp_id=wp_id,
            expected_file_sha256=expected_file_sha256,
        )
        if not result.passed or result.verified_plan is None:
            return False, list(result.error_codes), list(result.details)

        existing = self.wp_plans.get(wp_id)
        if existing is not None and (
            existing.file_sha256 != result.verified_plan.file_sha256
            or existing.plan_hash != result.verified_plan.plan_hash
        ):
            return (
                False,
                [EC.SUBJECT_HASH_MISMATCH],
                [f"wp {wp_id} already has a different frozen Plan"],
            )
        self.wp_plans[wp_id] = result.verified_plan
        return True, [], []

    def has_plan(self, wp_id: str) -> bool:
        """检查 WP 是否有已验证的冻结Plan。"""
        return wp_id in self.wp_plans

    def _reverify_plan(self, wp_id: str) -> tuple[bool, list[EC], list[str]]:
        verified = self.wp_plans.get(wp_id)
        if verified is None:
            return (
                False,
                [EC.WP_DEPENDENCY_NOT_MET],
                [f"wp {wp_id} has no verified frozen Plan"],
            )
        result = verify_work_package_plan_file(
            plan_path=verified.plan_path,
            dag_path=self.dag_path,
            expected_wp_id=wp_id,
            expected_file_sha256=verified.file_sha256,
        )
        if not result.passed or result.verified_plan is None:
            return False, list(result.error_codes), list(result.details)
        if result.verified_plan.plan_hash != verified.plan_hash:
            return (
                False,
                [EC.SUBJECT_HASH_MISMATCH],
                [f"wp {wp_id} Plan changed after registration"],
            )
        return True, [], []

    @staticmethod
    def _load_frozen_json(
        path: str | Path, expected_file_sha256: str, *, label: str,
    ) -> tuple[dict[str, Any] | None, list[EC], list[str]]:
        candidate = Path(path)
        if candidate.is_symlink() or not candidate.is_file():
            return None, [EC.SCHEMA_FILE_NOT_FOUND], [f"{label} is not a regular non-symlink file: {candidate}"]
        actual_hash = file_sha256(candidate)
        if actual_hash != expected_file_sha256:
            return None, [EC.SUBJECT_HASH_MISMATCH], [
                f"{label} file hash mismatch: expected {expected_file_sha256}, got {actual_hash}"
            ]
        try:
            obj = json.loads(candidate.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            return None, [EC.SCHEMA_VALIDATION_FAILED], [f"cannot read {label}: {exc}"]
        if not isinstance(obj, dict):
            return None, [EC.SCHEMA_VALIDATION_FAILED], [f"{label} must be a JSON object"]
        return obj, [], []

    def inherit_audit_debt(self, wp_id: str, debt: list[dict[str, str]]) -> None:
        """继承 audit debt。"""
        self.wp_audit_debt[wp_id] = list(debt)

    def get_audit_debt(self, wp_id: str) -> list[dict[str, str]]:
        """获取 WP 的 inherited audit debt。"""
        return self.wp_audit_debt.get(wp_id, [])

    def can_start(self, wp_id: str) -> tuple[bool, list[EC], list[str]]:
        """检查 WP 是否可以开始（NOT_STARTED → IN_PROGRESS）。

        检查：
        1. WP 存在于 DAG
        2. 当前状态为 NOT_STARTED 或 READY
        3. 所有 development_dependencies 处于 READY_FOR_AUDIT 或 AUDITED_PASS
        4. R5 补全: Plan 存在且已注册
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. WP 存在
        try:
            spec = self._get_wp_spec(wp_id)
        except ValueError:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown wp_id: {wp_id}")
            return False, errors, details

        # 2. 当前状态
        current = self.get_state(wp_id)
        if current not in ("NOT_STARTED", "READY"):
            errors.append(EC.WP_ALREADY_STARTED)
            details.append(f"wp {wp_id} already in state {current}, cannot start")

        # 3. development dependencies
        dev_deps = spec.get("development_dependencies", [])
        for dep_id in dev_deps:
            dep_state = self.get_state(dep_id)
            if dep_state not in _DEV_DEP_MIN_STATES:
                errors.append(EC.WP_DEPENDENCY_NOT_MET)
                details.append(
                    f"wp {wp_id} dependency {dep_id} is {dep_state}, "
                    f"must be READY_FOR_AUDIT or AUDITED_PASS"
                )

        # 4. Plan必须存在，且在start时重新执行验证以捕获注册后的漂移。
        plan_ok, plan_errors, plan_details = self._reverify_plan(wp_id)
        if not plan_ok:
            errors.extend(plan_errors)
            details.extend(plan_details)

        return len(errors) == 0, errors, details

    def start(self, wp_id: str, *, actor_type: str = "IMPLEMENTER") -> tuple[bool, list[EC], list[str]]:
        """开始一个 WP（NOT_STARTED → IN_PROGRESS）。

        如果依赖不满足，拒绝并返回错误。
        """
        ok, errors, details = self.can_start(wp_id)
        if not ok:
            return False, errors, details

        from_state = self.get_state(wp_id)
        self.wp_states[wp_id] = "IN_PROGRESS"
        self._record_event(wp_id, from_state, "IN_PROGRESS", actor_type, "start", details)
        return True, [], []

    def can_complete(
        self, wp_id: str, *, actor_type: str = "IMPLEMENTER",
        target_state: str = "READY_FOR_AUDIT",
    ) -> tuple[bool, list[EC], list[str]]:
        """检查 WP 是否可以完成（IN_PROGRESS → READY_FOR_AUDIT）。

        R5 补全: complete 命令检查：
        1. WP 存在
        2. 当前状态为 IN_PROGRESS 或 IMPLEMENTED_PENDING_EVIDENCE
        3. completion contract 与 owner 匹配
        4. implementer 不能写 AUDITED_* 状态
        5. target_state 是合法的完成状态
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. WP 存在
        try:
            spec = self._get_wp_spec(wp_id)
        except ValueError:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown wp_id: {wp_id}")
            return False, errors, details

        # 2. 当前状态
        current = self.get_state(wp_id)
        if current not in ("IN_PROGRESS", "IMPLEMENTED_PENDING_EVIDENCE"):
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"wp {wp_id} in state {current}, must be IN_PROGRESS or IMPLEMENTED_PENDING_EVIDENCE to complete")

        # 3. 只有implementer-owned包走complete；auditor-owned必须走audit。
        expected_contract = spec.get("completion_contract", "")
        if spec.get("owner_type") != "IMPLEMENTER" or expected_contract not in {
            "DOC_BOOTSTRAP_RECORD", "IMPLEMENTATION_BUNDLE"
        }:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(
                f"wp {wp_id} must not use implementer complete; "
                f"owner={spec.get('owner_type')}, contract={expected_contract}"
            )

        # 4. implementer 不能写 AUDITED_* 状态
        if actor_type == "IMPLEMENTER" and target_state in _IMPLEMENTER_FORBIDDEN_STATES:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"implementer cannot write {target_state} for {wp_id}")

        # 5. 合法转换
        allowed = _LEGAL_TRANSITIONS.get(current, frozenset())
        if target_state not in allowed:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"illegal transition: {current} → {target_state}")

        return len(errors) == 0, errors, details

    def complete(
        self,
        wp_id: str,
        *,
        completion_path: str | Path | None = None,
        expected_file_sha256: str = "",
        completion_contract: str | None = None,
        actor_type: str = "IMPLEMENTER",
        target_state: str = "READY_FOR_AUDIT",
        expected_subject_commit: str | None = None,
        expected_subject_tree: str | None = None,
    ) -> tuple[bool, list[EC], list[str]]:
        """完成一个 WP（IN_PROGRESS → READY_FOR_AUDIT）。

        R5 补全: complete 命令。
        """
        ok, errors, details = self.can_complete(
            wp_id, actor_type=actor_type, target_state=target_state,
        )
        if not ok:
            return False, errors, details

        expected_contract = self._get_wp_spec(wp_id).get("completion_contract")
        if completion_contract is not None and completion_contract != expected_contract:
            return False, [EC.WP_ILLEGAL_TRANSITION], [
                f"completion contract mismatch: expected {expected_contract}, got {completion_contract}"
            ]
        if completion_path is None or not expected_file_sha256:
            return False, [EC.WP_DEPENDENCY_NOT_MET], [
                "complete requires a frozen completion object path and file sha256"
            ]

        submitted_object, load_errors, load_details = self._load_frozen_json(
            completion_path, expected_file_sha256, label="completion object"
        )
        if submitted_object is None:
            return False, load_errors, load_details

        verification = verify_completion_contract(
            dag_path=self.dag_path,
            expected_dag_sha256=file_sha256(self.dag_path),
            wp_id=wp_id,
            submitted_object=submitted_object,
            actor_type=actor_type,
            state_command=target_state,
            expected_subject_commit=expected_subject_commit,
            expected_subject_tree=expected_subject_tree,
        )
        if not verification.passed:
            return False, list(verification.error_codes), list(verification.details)

        from_state = self.get_state(wp_id)
        self.wp_states[wp_id] = target_state
        self.wp_completion_objects[wp_id] = {
            "ref": str(Path(completion_path).resolve()),
            "sha256": expected_file_sha256,
            "object": submitted_object,
        }
        self._record_event(
            wp_id,
            from_state,
            target_state,
            actor_type,
            "complete",
            [f"completion_sha256={expected_file_sha256}"],
        )
        return True, [], []

    def can_activate(
        self, wp_id: str,
    ) -> tuple[bool, list[EC], list[str]]:
        """检查 WP 是否可以激活（READY_FOR_AUDIT → live action）。

        R5 补全: activate 命令检查：
        1. WP 存在
        2. 当前状态为 AUDITED_PASS（或精确未审 canary 例外）
        3. 所有 activation_dependencies 处于 AUDITED_PASS
        授权对象本身由``activate``中的SecurityContractVerifier验证；本方法
        只计算状态与DAG依赖，不能单独授权任何副作用。
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. WP 存在
        try:
            spec = self._get_wp_spec(wp_id)
        except ValueError:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown wp_id: {wp_id}")
            return False, errors, details

        # 2. 当前状态
        current = self.get_state(wp_id)
        if current != "AUDITED_PASS":
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"wp {wp_id} in state {current}, must be AUDITED_PASS to activate")

        # 3. activation dependencies
        act_deps = spec.get("activation_dependencies", [])
        for dep_id in act_deps:
            dep_state = self.get_state(dep_id)
            if dep_state not in _ACT_DEP_MIN_STATES:
                errors.append(EC.WP_DEPENDENCY_NOT_MET)
                details.append(
                    f"wp {wp_id} activation dependency {dep_id} is {dep_state}, "
                    f"must be AUDITED_PASS"
                )

        return len(errors) == 0, errors, details

    def activate(
        self,
        wp_id: str,
        *,
        eea_path: str | Path | None = None,
        eea_file_sha256: str = "",
        permit_path: str | Path | None = None,
        permit_file_sha256: str = "",
        reservation_path: str | Path | None = None,
        reservation_file_sha256: str = "",
        security_contract_verifier: Any = None,
        eea_public_key_bytes: bytes | None = None,
        permit_public_key_bytes: bytes | None = None,
        receipt_public_key_bytes: bytes | None = None,
        evaluation_time: str = "",
        expected_plan_hash: str = "",
        expected_site_fingerprint: str = "",
        expected_db_name: str = "",
        expected_action_registry_id: str = "",
        expected_action_registry_entry_ref_and_hash: dict[str, str] | None = None,
        expected_action_kind: str = "",
        permit_ref: str | None = None,
        reservation_ref: str | None = None,
        actor_type: str = "IMPLEMENTER",
    ) -> tuple[bool, list[EC], list[str]]:
        """激活一个 WP（AUDITED_PASS → live action）。

        R5 补全: activate 命令。
        注意：activate 不改变 WP 状态（AUDITED_PASS 是 terminal），
        但记录激活事件。
        """
        ok, errors, details = self.can_activate(wp_id)
        if not ok:
            return False, errors, details

        if permit_ref is not None or reservation_ref is not None:
            return False, [EC.WP_DEPENDENCY_NOT_MET], [
                "opaque permit_ref/reservation_ref activation is forbidden"
            ]
        if any(path is None for path in (eea_path, permit_path, reservation_path)):
            return False, [EC.WP_DEPENDENCY_NOT_MET], [
                "activate requires frozen EEA, Permit and RESERVED receipt files"
            ]
        if not all(
            (
                eea_file_sha256,
                permit_file_sha256,
                reservation_file_sha256,
                evaluation_time,
                expected_plan_hash,
                expected_action_registry_id,
                expected_action_kind,
            )
        ) or expected_action_registry_entry_ref_and_hash is None:
            return False, [EC.WP_DEPENDENCY_NOT_MET], [
                "activate is missing mandatory authorization bindings"
            ]

        from ..contracts.security_contract_verifier import SecurityContractVerifier

        if not isinstance(security_contract_verifier, SecurityContractVerifier):
            return (
                False,
                [EC.WP_DEPENDENCY_NOT_MET],
                ["activate requires the canonical SecurityContractVerifier"],
            )

        frozen_inputs: list[dict[str, Any]] = []
        for path, digest, label in (
            (eea_path, eea_file_sha256, "ExternalExecutionAuthorization"),
            (permit_path, permit_file_sha256, "LiveRunPermit"),
            (reservation_path, reservation_file_sha256, "AuthorizationConsumptionReceipt"),
        ):
            obj, input_errors, input_details = self._load_frozen_json(
                path, digest, label=label
            )
            if obj is None:
                return False, input_errors, input_details
            frozen_inputs.append(obj)
        eea, permit, reservation = frozen_inputs

        authorization = security_contract_verifier.verify_authorization_chain(
            eea=eea,
            permit=permit,
            reservation=reservation,
            expected_plan_hash=expected_plan_hash,
            expected_site_fingerprint=expected_site_fingerprint,
            expected_db_name=expected_db_name,
            expected_action_registry_id=expected_action_registry_id,
            expected_action_registry_entry_ref_and_hash=(
                expected_action_registry_entry_ref_and_hash
            ),
            expected_action_kind=expected_action_kind,
            expected_wp_id=wp_id,
            evaluation_time=evaluation_time,
            eea_public_key_bytes=eea_public_key_bytes,
            permit_public_key_bytes=permit_public_key_bytes,
            receipt_public_key_bytes=receipt_public_key_bytes,
        )
        if not authorization.passed:
            return False, list(authorization.error_codes), list(authorization.details)

        self._record_event(
            wp_id,
            "AUDITED_PASS",
            "AUDITED_PASS",
            actor_type,
            "activate",
            [
                f"eea_sha256={eea_file_sha256}",
                f"permit_sha256={permit_file_sha256}",
                f"reservation_sha256={reservation_file_sha256}",
            ],
        )
        return True, [], []

    def accept_audit(
        self,
        wp_id: str,
        *,
        assignment_path: str | Path,
        assignment_file_sha256: str,
        assignment_public_key_bytes: bytes,
        audit_record_path: str | Path,
        audit_record_file_sha256: str,
        audit_record_public_key_bytes: bytes,
        human_gate_service: Any,
        gate_decision: dict[str, Any],
        evaluation_time: str,
        target_state: str,
    ) -> tuple[bool, list[EC], list[str]]:
        """Apply an independent audit only after every signed binding passes.

        This is the sole upward path into ``AUDITED_*``.  A valid signature is
        necessary but not sufficient: assignment, record, frozen completion
        object and the HumanGate payload must all bind to the same work package
        and bytes.
        """
        from ..human.human_gate import HumanGateService
        from ..human.signed_object_verifier import (
            verify_audit_assignment,
            verify_audit_record,
        )

        if target_state not in {"AUDITED_PASS", "AUDITED_PARTIAL", "AUDITED_FAIL", "BLOCKED"}:
            return False, [EC.WP_ILLEGAL_TRANSITION], [f"invalid audit target state: {target_state}"]
        if self.get_state(wp_id) != "READY_FOR_AUDIT":
            return False, [EC.WP_ILLEGAL_TRANSITION], [
                f"wp {wp_id} must be READY_FOR_AUDIT before independent audit acceptance"
            ]
        if not isinstance(human_gate_service, HumanGateService):
            return False, [EC.ACTOR_NOT_AUTHORIZED], [
                "audit acceptance requires the canonical HumanGateService"
            ]
        completion = self.wp_completion_objects.get(wp_id)
        if completion is None:
            return False, [EC.WP_DEPENDENCY_NOT_MET], [
                f"wp {wp_id} has no verified completion object"
            ]

        assignment, errors, details = self._load_frozen_json(
            assignment_path, assignment_file_sha256, label="AuditAssignment"
        )
        if assignment is None:
            return False, errors, details
        record, errors, details = self._load_frozen_json(
            audit_record_path, audit_record_file_sha256, label="AuditRecord"
        )
        if record is None:
            return False, errors, details

        assignment_result = verify_audit_assignment(
            assignment, public_key_bytes=assignment_public_key_bytes
        )
        record_result = verify_audit_record(
            record, public_key_bytes=audit_record_public_key_bytes
        )
        signed_errors: list[EC] = []
        signed_details: list[str] = []
        if assignment_result.verdict != "PASS":
            signed_errors.append(EC.SIGNATURE_INVALID)
            signed_details.extend(f"assignment: {item}" for item in assignment_result.details)
        if record_result.verdict != "PASS":
            signed_errors.append(EC.SIGNATURE_INVALID)
            signed_details.extend(f"audit record: {item}" for item in record_result.details)
        if signed_errors:
            return False, signed_errors, signed_details

        assignment_bundle = assignment.get("completion_bundle_ref_and_hash", {})
        record_assignment = record.get("audit_assignment_ref_and_hash", {})
        record_bundle = record.get("audited_bundle_ref_and_hash", {})
        binding_failures: list[str] = []
        if assignment.get("target_work_package_id") != wp_id:
            binding_failures.append("AuditAssignment target_work_package_id mismatch")
        if assignment_bundle.get("sha256") != completion["sha256"]:
            binding_failures.append("AuditAssignment completion bundle hash mismatch")
        if record.get("wp_id") != wp_id:
            binding_failures.append("AuditRecord wp_id mismatch")
        if record_assignment.get("sha256") != assignment_file_sha256:
            binding_failures.append("AuditRecord assignment hash mismatch")
        if record_bundle.get("sha256") != completion["sha256"]:
            binding_failures.append("AuditRecord audited bundle hash mismatch")
        if record.get("auditor_principal_id") != assignment.get("auditor_principal_id"):
            binding_failures.append("auditor principal mismatch")
        if gate_decision.get("payload_hash") != audit_record_file_sha256:
            binding_failures.append("HumanGate payload hash does not bind AuditRecord bytes")

        implementation_axis = record.get("axis_verdicts", {}).get("implementation", {})
        axis_verdict = implementation_axis.get("verdict")
        expected_state = {
            "AUDITED_PASS": "AUDITED_PASS",
            "AUDITED_PARTIAL": "AUDITED_PARTIAL",
            "AUDITED_FAIL": "AUDITED_FAIL",
            "BLOCKED": "BLOCKED",
        }.get(axis_verdict)
        if expected_state != target_state:
            binding_failures.append(
                f"target state {target_state} does not match implementation axis {axis_verdict}"
            )
        if binding_failures:
            return False, [EC.SUBJECT_HASH_MISMATCH], binding_failures

        gate_result = human_gate_service.accept_gate_decision(
            gate_decision, evaluation_time=evaluation_time,
            creator_actor_id=record.get("auditor_principal_id"),
        )
        if not gate_result.passed:
            return False, list(gate_result.error_codes), list(gate_result.details)

        from_state = self.get_state(wp_id)
        self.wp_states[wp_id] = target_state
        self.wp_audit_objects[wp_id] = {
            "assignment_ref": str(Path(assignment_path).resolve()),
            "assignment_sha256": assignment_file_sha256,
            "audit_record_ref": str(Path(audit_record_path).resolve()),
            "audit_record_sha256": audit_record_file_sha256,
        }
        self._record_event(
            wp_id,
            from_state,
            target_state,
            "HUMAN_GATE_SERVICE",
            "accept_audit",
            [
                f"assignment_sha256={assignment_file_sha256}",
                f"audit_record_sha256={audit_record_file_sha256}",
            ],
        )
        return True, [], []

    def transition(self, wp_id: str, new_state: str, *, actor_type: str = "IMPLEMENTER") -> tuple[bool, list[EC], list[str]]:
        """转换 WP 状态。

        检查：
        1. WP 存在
        2. new_state 是合法状态
        3. 当前状态 → new_state 是合法转换
        4. 如果是 IN_PROGRESS，检查 development dependencies
        5. R5 补全: implementer 不能写 AUDITED_*
        """
        errors: list[EC] = []
        details: list[str] = []

        # 1. WP 存在
        try:
            self._get_wp_spec(wp_id)
        except ValueError:
            errors.append(EC.WP_UNKNOWN)
            details.append(f"unknown wp_id: {wp_id}")
            return False, errors, details

        # 2. 合法状态
        if new_state not in VALID_STATES:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"invalid state: {new_state}")
            return False, errors, details

        current = self.get_state(wp_id)

        # 3. 合法转换
        allowed = _LEGAL_TRANSITIONS.get(current, frozenset())
        if new_state not in allowed:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(f"illegal transition: {current} → {new_state}")
            return False, errors, details

        # Upward privileged transitions have dedicated consumers.  A generic
        # transition must never stand in for a Plan, CompletionBundle,
        # independent AuditRecord or signed authorization chain.
        if new_state in {"IN_PROGRESS", "READY_FOR_AUDIT", "AUDITED_PASS", "AUDITED_PARTIAL", "AUDITED_FAIL"}:
            errors.append(EC.WP_ILLEGAL_TRANSITION)
            details.append(
                f"generic transition cannot enter {new_state}; use start/complete/accept_audit"
            )
            return False, errors, details

        from_state = current
        self.wp_states[wp_id] = new_state
        self._record_event(wp_id, from_state, new_state, actor_type, "transition", details)
        return True, [], []

    def project_to_board(self) -> list[dict[str, str]]:
        """生成 board 投影：wp_id → state。

        确保 board 与实际状态一致。
        """
        self._load_dag()
        board = []
        for wp in self._dag.get("work_packages", []):
            wp_id = wp["wp_id"]
            board.append({
                "wp_id": wp_id,
                "state": self.get_state(wp_id),
                "owner_type": wp.get("owner_type", ""),
                "completion_contract": wp.get("completion_contract", ""),
            })
        return board

    def verify_board_consistency(self, board: list[dict[str, str]]) -> tuple[bool, list[EC], list[str]]:
        """验证 board 投影与实际状态一致。"""
        errors: list[EC] = []
        details: list[str] = []

        actual = {row["wp_id"]: row["state"] for row in self.project_to_board()}
        for row in board:
            wp_id = row.get("wp_id", "")
            board_state = row.get("state", "")
            actual_state = actual.get(wp_id)
            if actual_state is None:
                errors.append(EC.WP_UNKNOWN)
                details.append(f"board has unknown wp_id: {wp_id}")
            elif board_state != actual_state:
                errors.append(EC.WP_ILLEGAL_TRANSITION)
                details.append(
                    f"board state mismatch for {wp_id}: "
                    f"board={board_state}, actual={actual_state}"
                )

        return len(errors) == 0, errors, details

    def get_event_log(self) -> list[dict[str, Any]]:
        """获取 append-only 事件日志。"""
        return [evt.to_dict() for evt in self.event_log]

    def verify_event_log_consistency(self) -> tuple[bool, list[EC], list[str]]:
        """验证事件日志与当前状态一致。

        从事件日志重放，检查最终状态与 wp_states 一致。
        """
        errors: list[EC] = []
        details: list[str] = []

        replayed: dict[str, str] = {}
        for evt in self.event_log:
            if evt.to_state != "AUDITED_PASS" or evt.command != "activate":
                replayed[evt.wp_id] = evt.to_state

        for wp_id, state in self.wp_states.items():
            replayed_state = replayed.get(wp_id, "NOT_STARTED")
            if replayed_state != state:
                errors.append(EC.WP_ILLEGAL_TRANSITION)
                details.append(
                    f"event log inconsistency for {wp_id}: "
                    f"replayed={replayed_state}, actual={state}"
                )

        return len(errors) == 0, errors, details
