"""AuthoringBootstrapInputPack — HumanGate 批准的 QA0 启动包。

来自 docs/implementation/04-object-and-schema-catalog.md：

AuthoringBootstrapInputPack 是 HumanGate-approved QA0 startup pack。
冻结 MechanismContract, CoverageCell 和 evaluation pack source。
不依赖尚未存在的生产 CasePack。

硬约束：
- 必须签名（unsigned bootstrap input = blocker）
- 不依赖 CasePack（QA_BOOTSTRAP_DEPENDS_ON_CASEPACK）
- 状态：UNSIGNED → SIGNED → CONSUMED / REVOKED

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    QA_BOOTSTRAP_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/authoring-bootstrap-input-pack"
_SCHEMA_VERSION = 1
_OBJECT_TYPE = "AuthoringBootstrapInputPack"
_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-content_hash-null)"

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class AuthoringBootstrapInputPack:
    """AuthoringBootstrapInputPack — HumanGate 批准的启动包。不可变。

    冻结 MechanismContract + CoverageCell + evaluation pack source。
    不依赖 CasePack。
    """

    pack_id: str
    mechanism_contract_ref_and_hash: dict[str, str]
    coverage_cell_ref_and_hash: dict[str, str]
    evaluation_pack_ref_and_hash: dict[str, str]
    gate_decision_ref_and_hash: dict[str, str]
    state: str  # UNSIGNED / SIGNED / CONSUMED / REVOKED
    depends_on_casepack: bool
    schema_id: str = _SCHEMA_ID
    schema_version: int = _SCHEMA_VERSION
    object_type: str = _OBJECT_TYPE
    content_hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "object_type": self.object_type,
            "pack_id": self.pack_id,
            "mechanism_contract_ref_and_hash": dict(self.mechanism_contract_ref_and_hash),
            "coverage_cell_ref_and_hash": dict(self.coverage_cell_ref_and_hash),
            "evaluation_pack_ref_and_hash": dict(self.evaluation_pack_ref_and_hash),
            "gate_decision_ref_and_hash": dict(self.gate_decision_ref_and_hash),
            "state": self.state,
            "depends_on_casepack": self.depends_on_casepack,
            "content_hash_algorithm": self.content_hash_algorithm,
            "content_hash": self.content_hash,
        }


def _compute_content_hash(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o["content_hash"] = None
    return hashlib.sha256(canonical_json_bytes(o)).hexdigest()


def _check_ref_hash(obj: Any, field_name: str) -> list[tuple[EC, str]]:
    errors: list[tuple[EC, str]] = []
    if not isinstance(obj, dict):
        return [(EC.REQUIRED_FIELD_MISSING, f"{field_name} is not an object")]
    if set(obj.keys()) != {"ref_id", "sha256"}:
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name} must have exactly ref_id and sha256"))
        return errors
    if not obj.get("ref_id"):
        errors.append((EC.REQUIRED_FIELD_MISSING, f"{field_name}.ref_id is empty"))
    sha = obj.get("sha256", "")
    if not isinstance(sha, str) or not _HASH_RE.match(sha):
        errors.append((EC.OBJECT_HASH_MISMATCH, f"{field_name}.sha256 is not valid sha256"))
    return errors


def build_authoring_bootstrap_input_pack(
    *,
    pack_id: str,
    mechanism_contract_ref_and_hash: dict[str, str],
    coverage_cell_ref_and_hash: dict[str, str],
    evaluation_pack_ref_and_hash: dict[str, str],
    gate_decision_ref_and_hash: dict[str, str],
    state: str = "UNSIGNED",
    depends_on_casepack: bool = False,
) -> AuthoringBootstrapInputPack:
    """构建 AuthoringBootstrapInputPack，自动计算 content_hash。"""
    obj = {
        "schema_id": _SCHEMA_ID,
        "schema_version": _SCHEMA_VERSION,
        "object_type": _OBJECT_TYPE,
        "pack_id": pack_id,
        "mechanism_contract_ref_and_hash": dict(mechanism_contract_ref_and_hash),
        "coverage_cell_ref_and_hash": dict(coverage_cell_ref_and_hash),
        "evaluation_pack_ref_and_hash": dict(evaluation_pack_ref_and_hash),
        "gate_decision_ref_and_hash": dict(gate_decision_ref_and_hash),
        "state": state,
        "depends_on_casepack": depends_on_casepack,
        "content_hash_algorithm": _HASH_ALGORITHM,
        "content_hash": None,
    }
    content_hash = _compute_content_hash(obj)
    return AuthoringBootstrapInputPack(
        pack_id=pack_id,
        mechanism_contract_ref_and_hash=dict(mechanism_contract_ref_and_hash),
        coverage_cell_ref_and_hash=dict(coverage_cell_ref_and_hash),
        evaluation_pack_ref_and_hash=dict(evaluation_pack_ref_and_hash),
        gate_decision_ref_and_hash=dict(gate_decision_ref_and_hash),
        state=state,
        depends_on_casepack=depends_on_casepack,
        content_hash=content_hash,
    )


def verify_authoring_bootstrap_input_pack(
    pack: dict[str, Any] | AuthoringBootstrapInputPack,
) -> VerificationResult:
    """验证 AuthoringBootstrapInputPack 的结构合法性。

    检查：
    1. schema 常量
    2. pack_id 非空
    3. mechanism_contract / coverage_cell / evaluation_pack ref 结构合法
    4. gate_decision ref 结构合法
    5. state 在 QA_BOOTSTRAP_STATES 中
    6. depends_on_casepack 必须为 False（blocker: 依赖 CasePack）
    7. state != UNSIGNED（unsigned bootstrap = blocker）
    8. content_hash 正确
    """
    if isinstance(pack, AuthoringBootstrapInputPack):
        pack = pack.to_dict()

    errors: list[EC] = []
    details: list[str] = []

    if pack.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id must be {_SCHEMA_ID}")
    if pack.get("schema_version") != _SCHEMA_VERSION:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_version must be {_SCHEMA_VERSION}")
    if pack.get("object_type") != _OBJECT_TYPE:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"object_type must be {_OBJECT_TYPE}")

    if not pack.get("pack_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("pack_id must not be empty")

    for fname in (
        "mechanism_contract_ref_and_hash",
        "coverage_cell_ref_and_hash",
        "evaluation_pack_ref_and_hash",
        "gate_decision_ref_and_hash",
    ):
        for code, detail in _check_ref_hash(pack.get(fname, {}), fname):
            errors.append(code)
            details.append(detail)

    state = pack.get("state", "")
    if state not in QA_BOOTSTRAP_STATES:
        errors.append(EC.STATE_COMMAND_REJECTED)
        details.append(f"state must be in {QA_BOOTSTRAP_STATES}, got {state!r}")

    if pack.get("depends_on_casepack") is True:
        errors.append(EC.QA_BOOTSTRAP_DEPENDS_ON_CASEPACK)
        details.append("bootstrap input pack must not depend on not-yet-existing CasePack")

    if state == "UNSIGNED":
        errors.append(EC.QA_BOOTSTRAP_INPUT_UNSIGNED)
        details.append("bootstrap input pack must be signed (state != UNSIGNED)")

    if pack.get("content_hash_algorithm") != _HASH_ALGORITHM:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(f"unexpected content_hash_algorithm: {pack.get('content_hash_algorithm')}")

    computed = _compute_content_hash(pack)
    if pack.get("content_hash") != computed:
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: expected {computed}, got {pack.get('content_hash')}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
