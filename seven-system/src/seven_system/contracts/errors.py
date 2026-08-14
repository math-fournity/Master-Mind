"""GV0 固定错误码。

所有验证器返回结构化错误，不 TypeError 崩溃或跳过检查。
错误码是稳定枚举，下游消费者和审计者按码匹配，不按文本匹配。
"""

from __future__ import annotations

from enum import Enum


class VerificationErrorCode(str, Enum):
    """CompletionContractVerifier 和 SecurityContractVerifier 的固定错误码。"""

    # CompletionContractVerifier — owner / contract / schema / actor
    COMPLETION_CONTRACT_MISMATCH = "COMPLETION_CONTRACT_MISMATCH"
    ACTOR_NOT_AUTHORIZED = "ACTOR_NOT_AUTHORIZED"
    UNKNOWN_WORK_PACKAGE = "UNKNOWN_WORK_PACKAGE"
    SCHEMA_ID_MISMATCH = "SCHEMA_ID_MISMATCH"
    DAG_HASH_MISMATCH = "DAG_HASH_MISMATCH"
    DAG_LOAD_FAILED = "DAG_LOAD_FAILED"
    STATE_COMMAND_REJECTED = "STATE_COMMAND_REJECTED"

    # SecurityContractVerifier — 签名 / 授权链 / 额度
    SIGNATURE_INVALID = "SIGNATURE_INVALID"
    SIGNATURE_ALGORITHM_INVALID = "SIGNATURE_ALGORITHM_INVALID"
    SIGNATURE_DOMAIN_INVALID = "SIGNATURE_DOMAIN_INVALID"
    TIME_WINDOW_INVALID = "TIME_WINDOW_INVALID"
    TIME_NOT_CANONICAL_UTC = "TIME_NOT_CANONICAL_UTC"

    EEA_MODE_BINDING_INVALID = "EEA_MODE_BINDING_INVALID"
    EEA_ZERO_BUDGET = "EEA_ZERO_BUDGET"
    ACTION_REGISTRY_MISMATCH = "ACTION_REGISTRY_MISMATCH"

    PERMIT_ESCALATES_PARENT = "PERMIT_ESCALATES_PARENT"
    PERMIT_PARENT_HASH_MISMATCH = "PERMIT_PARENT_HASH_MISMATCH"
    DUPLICATE_ORDINAL = "DUPLICATE_ORDINAL"
    RESERVATION_BACKEND_INVALID = "RESERVATION_BACKEND_INVALID"

    RESERVATION_NOT_ATOMIC = "RESERVATION_NOT_ATOMIC"
    RELEASE_WITHOUT_PROOF = "RELEASE_WITHOUT_PROOF"
    UNKNOWN_START_MUST_HOLD = "UNKNOWN_START_MUST_HOLD"
    STALE_FENCE = "STALE_FENCE"
    ALLOWANCE_NOT_CONSERVED = "ALLOWANCE_NOT_CONSERVED"
    APPEND_ONLY_VIOLATION = "APPEND_ONLY_VIOLATION"

    # CompletionArtifactStore
    STORE_SYMLINK_REJECTED = "STORE_SYMLINK_REJECTED"
    STORE_BOUNDARY_ESCAPED = "STORE_BOUNDARY_ESCAPED"
    STORE_FALLBACK_REJECTED = "STORE_FALLBACK_REJECTED"
    STORE_HASH_MISMATCH = "STORE_HASH_MISMATCH"
    STORE_OVERWRITE_CONFLICT = "STORE_OVERWRITE_CONFLICT"
    STORE_VOLUME_ROOT_INVALID = "STORE_VOLUME_ROOT_INVALID"

    # 通用
    OBJECT_HASH_MISMATCH = "OBJECT_HASH_MISMATCH"
    REQUIRED_FIELD_MISSING = "REQUIRED_FIELD_MISSING"


class VerificationError(Exception):
    """验证器返回的结构化错误。

    验证器不抛异常——它们返回 VerificationResult。
    本异常仅用于内部断言或 CLI 层转换。
    """

    def __init__(self, code: VerificationErrorCode, detail: str = "") -> None:
        self.code = code
        self.detail = detail
        super().__init__(f"{code.value}: {detail}" if detail else code.value)


# 完成合同到期望 schema_id 的映射
COMPLETION_CONTRACT_TO_SCHEMA_ID: dict[str, str] = {
    "DOC_BOOTSTRAP_RECORD": "seven/docs/doc-bootstrap-completion-record",
    "IMPLEMENTATION_BUNDLE": "seven/implementation-completion-bundle",
    "AUDIT_RECORD": "seven/audit-record",
}

# 实施者允许的完成合同
IMPLEMENTER_CONTRACTS: frozenset[str] = frozenset(
    {"DOC_BOOTSTRAP_RECORD", "IMPLEMENTATION_BUNDLE"}
)

# 审计者允许的完成合同
AUDITOR_CONTRACTS: frozenset[str] = frozenset({"AUDIT_RECORD"})

# 实施者不能写的状态
IMPLEMENTER_FORBIDDEN_STATES: frozenset[str] = frozenset(
    {"AUDITED_PASS", "AUDITED_PARTIAL", "AUDITED_FAIL"}
)

# 合法的工作包状态全集
VALID_STATES: frozenset[str] = frozenset(
    {
        "NOT_STARTED",
        "READY",
        "IN_PROGRESS",
        "IMPLEMENTED_PENDING_EVIDENCE",
        "READY_FOR_AUDIT",
        "AUDITED_PASS",
        "AUDITED_PARTIAL",
        "AUDITED_FAIL",
        "BLOCKED",
    }
)

# 签名算法注册表 v1
SIGNATURE_ALGORITHM_V1: str = "Ed25519"

# 预留后端枚举
RESERVATION_BACKENDS: frozenset[str] = frozenset(
    {
        "DB_V2_OR_EQUIVALENT_TRANSACTIONAL_LEDGER",
        "SCHEMA_BOOTSTRAP_D_VOLUME_LEDGER",
        "SIDE_EFFECT_FREE_REFERENCE",  # GV0 自身的 side-effect-free 参考后端
    }
)

# 授权消费状态枚举
CONSUMPTION_STATUSES: frozenset[str] = frozenset(
    {"RESERVED", "CONSUMED", "RELEASED_UNUSED", "UNKNOWN_START_HELD", "QUARANTINED"}
)

# 授权模式枚举
AUTHORIZATION_MODES: frozenset[str] = frozenset(
    {"AUDITED_ACTIVATION", "UNAUDITED_AUTHORIZED_CANARY", "TRUST_ROOT_OR_SCHEMA_BOOTSTRAP"}
)

# 额度字段全集（用于守恒检查）
ALLOWANCE_FIELDS: tuple[str, ...] = (
    "invocations",
    "solver_launches",
    "database_writes",
    "redis_writes",
    "d_volume_writes",
    "human_gate_commits",
    "active_release_changes",
    "tokens",
    "cost_microunits",
)
