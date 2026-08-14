"""DAG-aware CompletionContractVerifier。

在接受任何完成对象或状态命令前，加载冻结 canonical DAG hash，
然后检查 owner_type + completion_contract + submitted schema + actor authority。
状态是独立维度，不能用 AUDITOR_OWNED_* 之类自造状态替代 owner 校验。

GV0 是本验证器的唯一代码所有者。状态服务、HumanGateService 和 P9/GA1
只消费本实现，不得各写局部放宽版。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..hashing import canonical_json_bytes, file_sha256
from .errors import (
    COMPLETION_CONTRACT_TO_SCHEMA_ID,
    IMPLEMENTER_CONTRACTS,
    IMPLEMENTER_FORBIDDEN_STATES,
    VALID_STATES,
    VerificationErrorCode as EC,
)


@dataclass(frozen=True)
class VerificationResult:
    """验证器返回的结构化结果，不抛异常。"""

    verdict: str  # "PASS" | "FAIL"
    error_codes: list[VerificationErrorCode] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    dag_sha256: str = ""
    wp_id: str = ""
    owner_type: str = ""
    completion_contract: str = ""
    expected_schema_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def _load_dag(dag_path: Path) -> tuple[dict[str, Any], str]:
    """加载 canonical DAG 并计算其 SHA-256 hash。"""
    try:
        raw = dag_path.read_bytes()
        dag = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        raise _DagLoadError(str(exc)) from exc
    # canonical JSON hash
    canonical = json.dumps(
        json.loads(raw), ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    import hashlib

    dag_hash = hashlib.sha256(canonical).hexdigest()
    return dag, dag_hash


class _DagLoadError(Exception):
    pass


def load_dag_index(dag_path: Path) -> dict[str, dict[str, Any]]:
    """加载 DAG 并返回 wp_id -> node 索引。"""
    dag, _ = _load_dag(dag_path)
    index: dict[str, dict[str, Any]] = {}
    for wp in dag.get("work_packages", []):
        wp_id = wp["wp_id"]
        index[wp_id] = wp
    return index


def verify_completion_contract(
    *,
    dag_path: Path,
    expected_dag_sha256: str,
    wp_id: str,
    submitted_object: dict[str, Any],
    actor_type: str,  # "IMPLEMENTER" | "AUDITOR" | "SYSTEM"
    state_command: str | None = None,
) -> VerificationResult:
    """验证完成合同。

    执行步骤（1-7 固定顺序，不得跳过）：
    1. 加载 DAG 并验证 hash
    2. 查找 wp_id 对应的 DAG 节点
    3. 根据 completion_contract 查找期望 schema_id
    4. 验证 submitted_object.schema_id == expected_schema_id
    5. 根据 owner_type 验证 actor 权限
    6. 验证状态命令（如有）
    7. 返回结构化结果
    """
    errors: list[VerificationErrorCode] = []
    details: list[str] = []

    # Step 1: 加载 DAG 并验证 hash
    try:
        dag, dag_hash = _load_dag(dag_path)
    except _DagLoadError as exc:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.DAG_LOAD_FAILED],
            details=[f"failed to load DAG: {exc}"],
            wp_id=wp_id,
        )

    if dag_hash != expected_dag_sha256:
        errors.append(EC.DAG_HASH_MISMATCH)
        details.append(
            f"DAG hash mismatch: expected {expected_dag_sha256}, got {dag_hash}"
        )

    # Step 2: 查找节点
    node: dict[str, Any] | None = None
    for wp in dag.get("work_packages", []):
        if wp.get("wp_id") == wp_id:
            node = wp
            break

    if node is None:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.UNKNOWN_WORK_PACKAGE],
            details=[f"wp_id {wp_id} not found in canonical DAG"],
            dag_sha256=dag_hash,
            wp_id=wp_id,
        )

    owner_type = node.get("owner_type", "")
    completion_contract = node.get("completion_contract", "")

    # Step 3: 查找期望 schema_id
    expected_schema_id = COMPLETION_CONTRACT_TO_SCHEMA_ID.get(completion_contract, "")
    if not expected_schema_id:
        errors.append(EC.COMPLETION_CONTRACT_MISMATCH)
        details.append(
            f"unknown completion_contract {completion_contract} for {wp_id}"
        )

    # Step 4: 验证 schema_id
    submitted_schema_id = submitted_object.get("schema_id", "")
    if expected_schema_id and submitted_schema_id != expected_schema_id:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(
            f"schema_id mismatch: expected {expected_schema_id}, "
            f"got {submitted_schema_id}"
        )

    # Step 5: 验证 actor 权限
    if owner_type == "IMPLEMENTER":
        if completion_contract not in IMPLEMENTER_CONTRACTS:
            errors.append(EC.COMPLETION_CONTRACT_MISMATCH)
            details.append(
                f"implementer-owned {wp_id} has invalid contract "
                f"{completion_contract}"
            )
        if actor_type == "AUDITOR":
            errors.append(EC.ACTOR_NOT_AUTHORIZED)
            details.append(
                f"auditor cannot submit completion object for "
                f"implementer-owned {wp_id}"
            )
    elif owner_type == "AUDITOR":
        if completion_contract != "AUDIT_RECORD":
            errors.append(EC.COMPLETION_CONTRACT_MISMATCH)
            details.append(
                f"auditor-owned {wp_id} must use AUDIT_RECORD, "
                f"got {completion_contract}"
            )
        if actor_type == "IMPLEMENTER":
            errors.append(EC.ACTOR_NOT_AUTHORIZED)
            details.append(
                f"implementer cannot submit completion object or state command "
                f"for auditor-owned {wp_id}"
            )
        # 审计者提交 AUDIT_RECORD 还需要 AuditAssignment + 签名
        # 但签名验证属于 SecurityContractVerifier，这里只检查合同层
    else:
        errors.append(EC.COMPLETION_CONTRACT_MISMATCH)
        details.append(f"unknown owner_type {owner_type} for {wp_id}")

    # Step 6: 验证状态命令
    if state_command is not None:
        if state_command not in VALID_STATES:
            errors.append(EC.STATE_COMMAND_REJECTED)
            details.append(f"unknown state {state_command}")
        elif owner_type == "IMPLEMENTER":
            if state_command in IMPLEMENTER_FORBIDDEN_STATES:
                errors.append(EC.STATE_COMMAND_REJECTED)
                details.append(
                    f"implementer cannot write {state_command} for {wp_id}"
                )
        elif owner_type == "AUDITOR":
            # 审计者可以写 AUDITED_*，但不能写实施者状态
            if state_command in (
                "NOT_STARTED",
                "READY",
                "IN_PROGRESS",
                "IMPLEMENTED_PENDING_EVIDENCE",
                "READY_FOR_AUDIT",
            ):
                errors.append(EC.STATE_COMMAND_REJECTED)
                details.append(
                    f"auditor cannot write implementer state "
                    f"{state_command} for {wp_id}"
                )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        dag_sha256=dag_hash,
        wp_id=wp_id,
        owner_type=owner_type,
        completion_contract=completion_contract,
        expected_schema_id=expected_schema_id,
    )


def verify_doc0_bootstrap_record(
    *,
    dag_path: Path,
    expected_dag_sha256: str,
    submitted_object: dict[str, Any],
    actor_type: str,
) -> VerificationResult:
    """DOC0 bootstrap record 专用验证。

    DOC0 使用 DOC_BOOTSTRAP_RECORD 而非 IMPLEMENTATION_BUNDLE。
    GV0 完成后必须先回验 DOC0 record，再接受任何普通工作包完成对象。
    """
    return verify_completion_contract(
        dag_path=dag_path,
        expected_dag_sha256=expected_dag_sha256,
        wp_id="WP-DOC0",
        submitted_object=submitted_object,
        actor_type=actor_type,
    )
