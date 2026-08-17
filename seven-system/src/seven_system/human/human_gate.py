"""HumanGateService — 门控决定编排与验证。

HumanGateService 是 HumanGate 的可信控制面。它编排完整门控链：
  GateDecision 验证 → ActorRoster 检查 → KeyRegistry 检查 →
  replay 防护 → 职责分离检查 → GV0 CompletionContractVerifier 消费

硬约束：
- Gate 决定必须签名（结构检查，与 SecurityContractVerifier 一致）
- ModelRole 不能自我批准（职责分离）
- 消费 GV0 CompletionContractVerifier 做状态命令验证，不复制
- replay 防护：decision_id + task_id + gate_type + payload_hash + actor_id + nonce 去重
- 撤销检查：key 撤销后签名拒绝
- 过期检查：key/task/payload 有效期同时检查
- payload 改写检测：签名覆盖完整 payload hash，不签摘要

SIDE_EFFECT_FREE：纯内存实现，不接触真实 DB/D 盘/模型。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..contracts.errors import (
    GATE_DECISIONS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import (
    VerificationResult,
    verify_completion_contract,
)
from .actor_roster import ActorRoster
from .gate_type_registry import GateTypeRegistry
from .key_lifecycle import KeyRegistry
from .gate_decision import verify_gate_decision
from .human_task import HumanTaskPort


@dataclass
class HumanGateService:
    """HumanGateService — 门控决定编排器。

    持有：
    - actor_roster: ActorRoster
    - gate_type_registry: GateTypeRegistry
    - key_registry: KeyRegistry
    - task_port: HumanTaskPort
    - seen_replay_keys: replay 去重集
    - seen_decision_ids: decision_id 去重集
    - accepted_decisions: 已接受的 decision 列表
    """

    actor_roster: ActorRoster
    gate_type_registry: GateTypeRegistry
    key_registry: KeyRegistry
    task_port: HumanTaskPort
    seen_replay_keys: set[str] = field(default_factory=set)
    seen_decision_ids: set[str] = field(default_factory=set)
    accepted_decisions: list[dict[str, Any]] = field(default_factory=list)

    # ─── 核心方法：验证并接受 GateDecision ───

    def accept_gate_decision(
        self,
        decision: dict[str, Any],
        *,
        evaluation_time: str,
        creator_actor_id: str | None = None,
    ) -> VerificationResult:
        """验证并接受一个 GateDecision。

        执行固定顺序检查（任一步失败都不降级为"仅告警"）：
        1. GateDecision 结构验证（verify_gate_decision）
        2. gate_type 存在（GateTypeRegistry）
        3. actor 存在、活跃、持有 required_roles（ActorRoster）
        4. ModelRole 不能自我批准（职责分离硬约束）
        5. key 有效（KeyRegistry：状态、时间窗、actor 绑定、角色资格）
        6. replay 防护（decision_id + replay_key 去重）
        7. 职责分离（CREATOR_CANNOT_APPROVE：creator != approver）
        8. decision 在合法枚举中
        9. 记录已接受的 decision
        """
        errors: list[EC] = []
        details: list[str] = []

        # ─── Step 1: 结构验证 + P0-B 真实 Ed25519 验签 ───
        # 先提取 key_id 用于公钥查找
        key_id = decision.get("key_id", "")
        # P0-B: HumanGate 是产生状态效力的边界，公钥不是可选增强。
        # 结构合法但没有已注册公钥的对象必须 fail-closed，不能退化为
        # “Base64 看起来像签名”就通过。
        public_key_bytes = self.key_registry.get_public_key(key_id) if key_id else None
        struct_result = verify_gate_decision(
            decision,
            public_key_bytes=public_key_bytes,
        )
        if not struct_result.passed:
            errors.extend(struct_result.error_codes)
            details.extend(struct_result.details)
            return VerificationResult(
                verdict="FAIL", error_codes=errors, details=details
            )
        if public_key_bytes is None:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.SIGNATURE_INVALID],
                details=[
                    f"no registered Ed25519 public key bytes for key_id={key_id!r}; "
                    "HumanGate cannot accept a structurally-only signature"
                ],
            )

        decision_id = decision.get("decision_id", "")
        task_id = decision.get("task_id", "")
        gate_type = decision.get("gate_type", "")
        payload_hash = decision.get("payload_hash", "")
        actor_id = decision.get("actor_id", "")
        actor_role = decision.get("actor_role", "")
        nonce = decision.get("nonce", "")
        key_id = decision.get("key_id", "")
        dec_value = decision.get("decision", "")

        # ─── Step 2: gate_type 存在 ───
        gate_spec = self.gate_type_registry.get(gate_type)
        if gate_spec is None:
            errors.append(EC.GATE_TYPE_UNKNOWN)
            details.append(f"unknown gate_type: {gate_type}")
            return VerificationResult(
                verdict="FAIL", error_codes=errors, details=details
            )

        # ─── Step 3: actor 检查 ───
        actor_result = self.actor_roster.check_actor(
            actor_id,
            required_roles=gate_spec.required_roles,
        )
        if not actor_result.passed:
            errors.extend(actor_result.error_codes)
            details.extend(actor_result.details)

        # ─── Step 4: ModelRole 不能自我批准 ───
        if self.actor_roster.is_model_role(actor_id):
            if dec_value == "APPROVE":
                errors.append(EC.GATE_SELF_APPROVAL_REJECTED)
                details.append(
                    f"ModelRole actor {actor_id} cannot self-approve "
                    f"gate {gate_type}"
                )
            if not gate_spec.allow_model_role:
                errors.append(EC.GATE_SELF_APPROVAL_REJECTED)
                details.append(
                    f"gate_type {gate_type} does not allow ModelRole"
                )

        # ─── Step 5: key 有效性 ───
        key_result = self.key_registry.check_key(
            key_id,
            expected_actor_id=actor_id,
            required_role=actor_role,
            evaluation_time=evaluation_time,
        )
        if not key_result.passed:
            errors.extend(key_result.error_codes)
            details.extend(key_result.details)

        # ─── Step 6: replay 防护 ───
        replay_key = f"{decision_id}|{task_id}|{gate_type}|{payload_hash}|{actor_id}|{nonce}"
        if decision_id in self.seen_decision_ids:
            errors.append(EC.GATE_REPLAY_DETECTED)
            details.append(f"decision_id {decision_id} already seen")
        if replay_key in self.seen_replay_keys:
            errors.append(EC.GATE_REPLAY_DETECTED)
            details.append(f"replay key already seen: {replay_key}")

        # ─── Step 7: 职责分离 ───
        if gate_spec.separation_policy == "CREATOR_CANNOT_APPROVE":
            task = self.task_port.get_task(task_id)
            if task is not None:
                if task.creator_actor_id == actor_id:
                    errors.append(EC.GATE_DUTY_CONFLICT)
                    details.append(
                        f"actor {actor_id} created task {task_id} "
                        f"and cannot approve it (CREATOR_CANNOT_APPROVE)"
                    )
            elif creator_actor_id is not None and creator_actor_id == actor_id:
                errors.append(EC.GATE_DUTY_CONFLICT)
                details.append(
                    f"actor {actor_id} created the payload "
                    f"and cannot approve it (CREATOR_CANNOT_APPROVE)"
                )

        # ─── Step 8: decision 合法性 ───
        if dec_value not in GATE_DECISIONS:
            errors.append(EC.STATE_COMMAND_REJECTED)
            details.append(f"unknown decision: {dec_value}")

        if errors:
            return VerificationResult(
                verdict="FAIL", error_codes=errors, details=details
            )

        # ─── Step 9: 记录 ───
        self.seen_decision_ids.add(decision_id)
        self.seen_replay_keys.add(replay_key)
        self.accepted_decisions.append(dict(decision))

        return VerificationResult(verdict="PASS")

    # ─── GV0 消费：状态命令验证 ───

    def verify_state_command(
        self,
        *,
        dag_path: Path,
        expected_dag_sha256: str,
        wp_id: str,
        submitted_object: dict[str, Any],
        actor_type: str,
        state_command: str,
    ) -> VerificationResult:
        """验证状态命令——消费 GV0 CompletionContractVerifier。

        HumanGateService 不复制 GV0 的验证逻辑。
        它直接调用 verify_completion_contract，将结果返回给调用方。
        这是 HG0 "消费 GV0 验证器而不复制" 的核心约束。
        """
        return verify_completion_contract(
            dag_path=dag_path,
            expected_dag_sha256=expected_dag_sha256,
            wp_id=wp_id,
            submitted_object=submitted_object,
            actor_type=actor_type,
            state_command=state_command,
        )

    # ─── 辅助方法 ───

    def revoke_key(self, key_id: str, *, revocation_ref: str) -> VerificationResult:
        """撤销一个签名密钥。"""
        return self.key_registry.revoke(key_id, revocation_ref=revocation_ref)

    @property
    def accepted_count(self) -> int:
        return len(self.accepted_decisions)

    def list_accepted(self) -> list[dict[str, Any]]:
        return list(self.accepted_decisions)
