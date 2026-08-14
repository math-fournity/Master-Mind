"""DAG-aware CompletionContractVerifier。

在接受任何完成对象或状态命令前，加载冻结 canonical DAG hash，
然后检查 owner_type + completion_contract + submitted schema + actor authority。
状态是独立维度，不能用 AUDITOR_OWNED_* 之类自造状态替代 owner 校验。

GV0 是本验证器的唯一代码所有者。状态服务、HumanGateService 和 P9/GA1
只消费本实现，不得各写局部放宽版。

P0-A 整改：verifier 必须执行完整 Draft 2020-12 Schema 验证，
不再只比较 schema_id 字符串。空壳对象、缺字段、additional property、
错类型、非法 RFC3339、self-hash 不符、WP ID 不符全部必须 FAIL。
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..hashing import canonical_json_bytes, file_sha256
from .errors import (
    COMPLETION_CONTRACT_TO_SCHEMA_ID,
    COMPLETION_SELF_HASH_ALGORITHM,
    COMPLETION_SCHEMA_FORMAT_POLICY,
    COMPLETION_SCHEMA_VALIDATOR_VERSION,
    IMPLEMENTER_CONTRACTS,
    IMPLEMENTER_FORBIDDEN_STATES,
    VALID_STATES,
    VerificationErrorCode as EC,
    _COMPLETION_SCHEMA_FILES,
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
    schema_file_sha256: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


class _DagLoadError(Exception):
    pass


def _load_dag(dag_path: Path) -> tuple[dict[str, Any], str]:
    """加载 canonical DAG 并计算其 SHA-256 hash。"""
    try:
        raw = dag_path.read_bytes()
        dag = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        raise _DagLoadError(str(exc)) from exc
    canonical = json.dumps(
        json.loads(raw), ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    dag_hash = hashlib.sha256(canonical).hexdigest()
    return dag, dag_hash


def load_dag_index(dag_path: Path) -> dict[str, dict[str, Any]]:
    """加载 DAG 并返回 wp_id -> node 索引。"""
    dag, _ = _load_dag(dag_path)
    index: dict[str, dict[str, Any]] = {}
    for wp in dag.get("work_packages", []):
        wp_id = wp["wp_id"]
        index[wp_id] = wp
    return index


# ─── P0-A: Schema registry and validation ──────────────────────────────

def _resolve_schema_path(dag_path: Path, completion_contract: str) -> Path | None:
    """根据 completion_contract 解析 Schema 文件路径。"""
    schema_file = _COMPLETION_SCHEMA_FILES.get(completion_contract)
    if not schema_file:
        return None
    # Schema files are in the same directory as the DAG
    return dag_path.parent / schema_file


def _validate_full_schema(
    submitted_object: dict[str, Any],
    schema_path: Path,
    errors: list[VerificationErrorCode],
    details: list[str],
) -> str:
    """执行完整 Draft 2020-12 Schema 验证，返回 Schema 文件 hash。"""
    # 1. 检查 Schema 文件存在
    if not schema_path.exists():
        errors.append(EC.SCHEMA_FILE_NOT_FOUND)
        details.append(f"schema file not found: {schema_path}")
        return ""

    # 2. 重算 Schema 文件 hash（verifier 不可信任调用者传入的 hash）
    schema_bytes = schema_path.read_bytes()
    schema_sha256 = hashlib.sha256(schema_bytes).hexdigest()

    # 3. 加载 Schema
    try:
        schema = json.loads(schema_bytes)
    except json.JSONDecodeError as exc:
        errors.append(EC.SCHEMA_FILE_LOAD_FAILED)
        details.append(f"schema file JSON parse error: {exc}")
        return schema_sha256

    # 4. 执行 Draft 2020-12 验证
    try:
        from jsonschema import Draft202012Validator
        from jsonschema.exceptions import ValidationError as JSValidationError
    except ImportError:
        errors.append(EC.SCHEMA_FILE_LOAD_FAILED)
        details.append("jsonschema library not available — fail-closed")
        return schema_sha256

    validator = Draft202012Validator(schema)
    schema_errors = sorted(validator.iter_errors(submitted_object), key=lambda e: e.path)

    if schema_errors:
        errors.append(EC.SCHEMA_VALIDATION_FAILED)
        for err in schema_errors[:10]:  # limit details
            path = ".".join(str(p) for p in err.absolute_path) or "(root)"
            details.append(f"schema validation error at {path}: {err.message}")

    # 5. 严格 RFC3339 date-time 验证
    _validate_rfc3339_fields(submitted_object, schema, errors, details)

    return schema_sha256


def _validate_rfc3339_fields(
    obj: dict[str, Any],
    schema: dict[str, Any],
    errors: list[VerificationErrorCode],
    details: list[str],
) -> None:
    """严格验证 RFC3339 date-time 字段，拒绝非法日期和非 canonical 时间。"""
    import re
    from datetime import datetime

    # Canonical RFC3339 UTC: YYYY-MM-DDTHH:MM:SS(.ssssss)?Z
    _CANONICAL_RFC3339_RE = re.compile(
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$"
    )

    def _check_rfc3339(value: Any, field_path: str) -> None:
        if not isinstance(value, str):
            return
        if not _CANONICAL_RFC3339_RE.match(value):
            errors.append(EC.RFC3339_INVALID)
            details.append(
                f"RFC3339 invalid at {field_path}: '{value}' — "
                f"must be canonical UTC (YYYY-MM-DDTHH:MM:SSZ)"
            )
            return
        # Verify it's a real date
        try:
            datetime.strptime(value.replace("Z", "+00:00"), "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            errors.append(EC.RFC3339_INVALID)
            details.append(f"RFC3339 invalid date at {field_path}: '{value}'")

    # Find all date-time fields in schema
    properties = schema.get("properties", {})
    for field_name, field_schema in properties.items():
        if isinstance(field_schema, dict) and field_schema.get("format") == "date-time":
            if field_name in obj:
                _check_rfc3339(obj[field_name], field_name)


def _validate_self_hash(
    submitted_object: dict[str, Any],
    errors: list[VerificationErrorCode],
    details: list[str],
) -> None:
    """验证对象的 self-hash（bundle_hash 或 receipt_hash）按规定算法重算。"""
    # Find the self-hash field
    self_hash_field = None
    for candidate in ("bundle_hash", "receipt_hash"):
        if candidate in submitted_object:
            self_hash_field = candidate
            break

    if self_hash_field is None:
        return  # No self-hash field to validate (e.g., DOC0 bootstrap)

    submitted_hash = submitted_object.get(self_hash_field)
    if not isinstance(submitted_hash, str) or not submitted_hash:
        return  # Schema validation already catches this

    # Recompute: set self_hash to null, canonical JSON, sha256
    tmp = dict(submitted_object)
    tmp[self_hash_field] = None
    canonical = json.dumps(
        tmp, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    expected_hash = hashlib.sha256(canonical).hexdigest()

    if submitted_hash != expected_hash:
        errors.append(EC.SELF_HASH_MISMATCH)
        details.append(
            f"{self_hash_field} mismatch: expected {expected_hash[:16]}..., "
            f"got {submitted_hash[:16]}..."
        )


def _validate_cross_object_binding(
    submitted_object: dict[str, Any],
    wp_id: str,
    state_command: str | None,
    errors: list[VerificationErrorCode],
    details: list[str],
    *,
    expected_subject_commit: str | None = None,
    expected_subject_tree: str | None = None,
) -> None:
    """验证 WP ID、status、subject commit/tree 等跨字段绑定。"""
    # WP ID must match request
    obj_wp_id = submitted_object.get("wp_id")
    if isinstance(obj_wp_id, str) and obj_wp_id != wp_id:
        errors.append(EC.WP_ID_MISMATCH)
        details.append(f"wp_id mismatch: request={wp_id}, bundle={obj_wp_id}")

    # Bundle status must match state command (if both present)
    obj_status = submitted_object.get("status")
    if state_command is not None and isinstance(obj_status, str):
        if obj_status != state_command:
            errors.append(EC.BUNDLE_STATUS_MISMATCH)
            details.append(
                f"bundle status mismatch: state_command={state_command}, "
                f"bundle.status={obj_status}"
            )

    # P0-A 补全: implementation subject commit/tree 必须与冻结 subject 一致
    if expected_subject_commit is not None or expected_subject_tree is not None:
        impl_subject = submitted_object.get("implementation_subject", {})
        if isinstance(impl_subject, dict):
            obj_commit = impl_subject.get("commit", "")
            obj_tree = impl_subject.get("tree", "")
            if expected_subject_commit is not None and obj_commit != expected_subject_commit:
                errors.append(EC.SUBJECT_HASH_MISMATCH)
                details.append(
                    f"implementation_subject.commit mismatch: "
                    f"expected {expected_subject_commit}, got {obj_commit}"
                )
            if expected_subject_tree is not None and obj_tree != expected_subject_tree:
                errors.append(EC.SUBJECT_HASH_MISMATCH)
                details.append(
                    f"implementation_subject.tree mismatch: "
                    f"expected {expected_subject_tree}, got {obj_tree}"
                )


def verify_completion_contract(
    *,
    dag_path: Path,
    expected_dag_sha256: str,
    wp_id: str,
    submitted_object: dict[str, Any],
    actor_type: str,  # "IMPLEMENTER" | "AUDITOR" | "SYSTEM"
    state_command: str | None = None,
    expected_subject_commit: str | None = None,
    expected_subject_tree: str | None = None,
) -> VerificationResult:
    """验证完成合同。

    执行步骤（1-10 固定顺序，不得跳过）：
    1. 加载 DAG 并验证 hash
    2. 查找 wp_id 对应的 DAG 节点
    3. 根据 completion_contract 查找期望 schema_id
    4. 验证 submitted_object.schema_id == expected_schema_id
    5. 加载并执行完整 Draft 2020-12 Schema 验证
    6. 验证 RFC3339 date-time 字段
    7. 验证 self-hash
    8. 验证跨字段绑定（WP ID、status）
    9. 根据 owner_type 验证 actor 权限和状态命令
    10. 返回结构化结果
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

    # Step 5: 加载并执行完整 Schema 验证
    schema_file_sha256 = ""
    if expected_schema_id:
        schema_path = _resolve_schema_path(dag_path, completion_contract)
        if schema_path:
            schema_file_sha256 = _validate_full_schema(
                submitted_object, schema_path, errors, details
            )
        else:
            errors.append(EC.SCHEMA_FILE_NOT_FOUND)
            details.append(f"no schema file registered for {completion_contract}")

    # Step 6: RFC3339 验证已在 _validate_full_schema 中执行

    # Step 7: 验证 self-hash
    _validate_self_hash(submitted_object, errors, details)

    # Step 8: 验证跨字段绑定
    _validate_cross_object_binding(
        submitted_object, wp_id, state_command, errors, details,
        expected_subject_commit=expected_subject_commit,
        expected_subject_tree=expected_subject_tree,
    )

    # Step 9: 验证 actor 权限和状态命令
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
    else:
        errors.append(EC.COMPLETION_CONTRACT_MISMATCH)
        details.append(f"unknown owner_type {owner_type} for {wp_id}")

    # 状态命令验证
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
        schema_file_sha256=schema_file_sha256,
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
