"""Injection — WP-ST1 将 bound hint 注入 Solver job。

关键约束（blocker）：
- Injection 使用 TX1 的 InjectionPolicy 控制注入规则
- 注入必须有 binding（ST_INJECTION_WITHOUT_BINDING）
- Injection receipt 记录 before/after state hash
- 注入位置由 InjectionPolicy 控制
- 组件版本必须与 release 锁定的版本一致（ST_COMPONENT_DRIFT）

SIDE_EFFECT_FREE：纯内存实现，不启动真实 Solver。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ST_INJECTION_POSITIONS,
    VerificationErrorCode as EC,
)


_INJECTION_RECEIPT_SCHEMA_ID = "seven/injection-receipt"
_INJECTION_RECEIPT_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class InjectionReceipt:
    """Injection 运行收据——记录 hint 注入 Solver job 的结果。

    字段：
        receipt_id: 唯一标识
        release_ref: TellStrategyRelease 引用
        binding_receipt_id: 上游 BindingReceipt ID（必须非空）
        injection_policy_ref: InjectionPolicy 引用 {policy_id, version, content_hash}
        injection_position: 注入位置（ST_INJECTION_POSITIONS）
        before_state_hash: 注入前 state hash
        after_state_hash: 注入后 state hash
        injected_payload_hash: 注入的 payload hash
        component_version: injection 组件版本
        content_hash: 内容哈希
    """

    receipt_id: str
    release_ref: dict[str, str] = field(default_factory=dict)
    binding_receipt_id: str = ""
    injection_policy_ref: dict[str, str] = field(default_factory=dict)
    injection_position: str = "PRE_TRACE"
    before_state_hash: str = ""
    after_state_hash: str = ""
    injected_payload_hash: str = ""
    component_version: str = ""
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _INJECTION_RECEIPT_SCHEMA_ID,
            "schema_version": _INJECTION_RECEIPT_SCHEMA_VERSION,
            "receipt_id": self.receipt_id,
            "release_ref": dict(self.release_ref),
            "binding_receipt_id": self.binding_receipt_id,
            "injection_policy_ref": dict(self.injection_policy_ref),
            "injection_position": self.injection_position,
            "before_state_hash": self.before_state_hash,
            "after_state_hash": self.after_state_hash,
            "injected_payload_hash": self.injected_payload_hash,
            "component_version": self.component_version,
            "frozen_at": self.frozen_at,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()


def make_injection_receipt(
    *,
    receipt_id: str,
    release_ref: dict[str, str] | None = None,
    binding_receipt_id: str = "",
    injection_policy_ref: dict[str, str] | None = None,
    injection_position: str = "PRE_TRACE",
    before_state_hash: str = "",
    after_state_hash: str = "",
    injected_payload_hash: str = "",
    component_version: str = "",
    frozen_at: str = "",
) -> InjectionReceipt:
    r = InjectionReceipt(
        receipt_id=receipt_id,
        release_ref=release_ref or {},
        binding_receipt_id=binding_receipt_id,
        injection_policy_ref=injection_policy_ref or {},
        injection_position=injection_position,
        before_state_hash=before_state_hash,
        after_state_hash=after_state_hash,
        injected_payload_hash=injected_payload_hash,
        component_version=component_version,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(r, content_hash=r.compute_content_hash())


@dataclass(frozen=True)
class InjectionReceiptVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    receipt_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_injection_receipt(
    receipt: InjectionReceipt,
    *,
    expected_release_hash: str | None = None,
    expected_component_version: str | None = None,
    expected_policy_hash: str | None = None,
) -> InjectionReceiptVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = receipt.to_dict()
    if d.get("schema_id") != _INJECTION_RECEIPT_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_INJECTION_RECEIPT_SCHEMA_ID}")

    # release_ref required
    if not receipt.release_ref.get("release_id"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain release_id")
    if not receipt.release_ref.get("content_hash"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain content_hash")

    if expected_release_hash is not None:
        if receipt.release_ref.get("content_hash") != expected_release_hash:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"release_ref content_hash mismatch: claims "
                f"{receipt.release_ref.get('content_hash')}, "
                f"expected {expected_release_hash}"
            )

    # blocker: injection without binding
    if not receipt.binding_receipt_id:
        errors.append(EC.ST_INJECTION_WITHOUT_BINDING)
        details.append(
            "binding_receipt_id is empty — injection requires a binding"
        )

    # injection_policy_ref required
    if not receipt.injection_policy_ref.get("policy_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("injection_policy_ref must contain policy_id")
    if not receipt.injection_policy_ref.get("content_hash"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("injection_policy_ref must contain content_hash")

    if expected_policy_hash is not None:
        if receipt.injection_policy_ref.get("content_hash") != expected_policy_hash:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"injection_policy_ref content_hash mismatch: claims "
                f"{receipt.injection_policy_ref.get('content_hash')}, "
                f"expected {expected_policy_hash}"
            )

    # position valid
    if receipt.injection_position not in ST_INJECTION_POSITIONS:
        errors.append(EC.ST_POSITION_INVALID)
        details.append(
            f"injection_position '{receipt.injection_position}' not in "
            f"{sorted(ST_INJECTION_POSITIONS)}"
        )

    # before/after state hashes required
    if not receipt.before_state_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("before_state_hash is empty")
    if not receipt.after_state_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("after_state_hash is empty")

    # component version drift
    if expected_component_version is not None:
        if receipt.component_version != expected_component_version:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"component_version drift: claims "
                f"{receipt.component_version}, expected "
                f"{expected_component_version}"
            )

    # content_hash
    if not receipt.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif receipt.content_hash != receipt.compute_content_hash():
        errors.append(EC.ST_INJECTION_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {receipt.content_hash}, "
            f"computed {receipt.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return InjectionReceiptVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        receipt_id=receipt.receipt_id,
    )


class Injector:
    """Injector — 将 bound hint 注入 Solver job。

    纯程序实现：给定 binding + injection_policy，产出 InjectionReceipt。
    不启动真实 Solver——只记录 before/after state hash。
    """

    def __init__(self, *, component_version: str = "st1-injection-v1") -> None:
        self.component_version = component_version

    def inject(
        self,
        *,
        receipt_id: str,
        release_ref: dict[str, str],
        binding_receipt_id: str,
        injection_policy_ref: dict[str, str],
        injection_position: str = "PRE_TRACE",
        before_state_hash: str = "",
        after_state_hash: str = "",
        injected_payload_hash: str = "",
        frozen_at: str = "",
    ) -> InjectionReceipt:
        return make_injection_receipt(
            receipt_id=receipt_id,
            release_ref=release_ref,
            binding_receipt_id=binding_receipt_id,
            injection_policy_ref=injection_policy_ref,
            injection_position=injection_position,
            before_state_hash=before_state_hash,
            after_state_hash=after_state_hash,
            injected_payload_hash=injected_payload_hash,
            component_version=self.component_version,
            frozen_at=frozen_at,
        )
