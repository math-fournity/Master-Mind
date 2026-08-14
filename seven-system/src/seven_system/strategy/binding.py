"""Binding — WP-ST1 将渲染的 hint 绑定到具体 problem context。

关键约束（blocker）：
- Binding 包含 position、timing、scope
- Binding receipt 记录绑定结果
- position 必须在 ST_INJECTION_POSITIONS 中（ST_POSITION_INVALID）
- timing 必须合法（ST_TIMING_INVALID）
- 组件版本必须与 release 锁定的版本一致（ST_COMPONENT_DRIFT）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ST_BINDING_KINDS,
    ST_INJECTION_POSITIONS,
    VerificationErrorCode as EC,
)


_BINDING_RECEIPT_SCHEMA_ID = "seven/binding-receipt"
_BINDING_RECEIPT_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"

# 合法 timing 枚举
ST_TIMING_KINDS: frozenset[str] = frozenset(
    {"BEFORE_SOLVE", "AT_BRANCH", "MID_SOLVE", "AFTER_SOLVE"}
)


@dataclass(frozen=True)
class BindingReceipt:
    """Binding 运行收据——记录 hint 到 problem context 的绑定。

    字段：
        receipt_id: 唯一标识
        release_ref: TellStrategyRelease 引用
        renderer_receipt_id: 上游 RendererReceipt ID
        hint_instance_id: 绑定的 HintInstance ID
        kind: 绑定种类（ST_BINDING_KINDS）
        position: 注入位置（ST_INJECTION_POSITIONS）
        timing: 注入时机（ST_TIMING_KINDS）
        scope: 绑定 scope 描述
        problem_context_ref: problem context 引用
        component_version: binding 组件版本
        content_hash: 内容哈希
    """

    receipt_id: str
    release_ref: dict[str, str] = field(default_factory=dict)
    renderer_receipt_id: str = ""
    hint_instance_id: str = ""
    kind: str = "FULL_BINDING"
    position: str = "PRE_TRACE"
    timing: str = "BEFORE_SOLVE"
    scope: str = ""
    problem_context_ref: dict[str, str] = field(default_factory=dict)
    component_version: str = ""
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _BINDING_RECEIPT_SCHEMA_ID,
            "schema_version": _BINDING_RECEIPT_SCHEMA_VERSION,
            "receipt_id": self.receipt_id,
            "release_ref": dict(self.release_ref),
            "renderer_receipt_id": self.renderer_receipt_id,
            "hint_instance_id": self.hint_instance_id,
            "kind": self.kind,
            "position": self.position,
            "timing": self.timing,
            "scope": self.scope,
            "problem_context_ref": dict(self.problem_context_ref),
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


def make_binding_receipt(
    *,
    receipt_id: str,
    release_ref: dict[str, str] | None = None,
    renderer_receipt_id: str = "",
    hint_instance_id: str = "",
    kind: str = "FULL_BINDING",
    position: str = "PRE_TRACE",
    timing: str = "BEFORE_SOLVE",
    scope: str = "",
    problem_context_ref: dict[str, str] | None = None,
    component_version: str = "",
    frozen_at: str = "",
) -> BindingReceipt:
    r = BindingReceipt(
        receipt_id=receipt_id,
        release_ref=release_ref or {},
        renderer_receipt_id=renderer_receipt_id,
        hint_instance_id=hint_instance_id,
        kind=kind,
        position=position,
        timing=timing,
        scope=scope,
        problem_context_ref=problem_context_ref or {},
        component_version=component_version,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(r, content_hash=r.compute_content_hash())


@dataclass(frozen=True)
class BindingReceiptVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    receipt_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_binding_receipt(
    receipt: BindingReceipt,
    *,
    expected_release_hash: str | None = None,
    expected_component_version: str | None = None,
) -> BindingReceiptVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = receipt.to_dict()
    if d.get("schema_id") != _BINDING_RECEIPT_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_BINDING_RECEIPT_SCHEMA_ID}")

    # kind valid
    if receipt.kind not in ST_BINDING_KINDS:
        errors.append(EC.ST_BINDING_KIND_INVALID)
        details.append(
            f"kind '{receipt.kind}' not in {sorted(ST_BINDING_KINDS)}"
        )

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

    # position valid
    if receipt.position not in ST_INJECTION_POSITIONS:
        errors.append(EC.ST_POSITION_INVALID)
        details.append(
            f"position '{receipt.position}' not in "
            f"{sorted(ST_INJECTION_POSITIONS)}"
        )

    # timing valid
    if receipt.timing not in ST_TIMING_KINDS:
        errors.append(EC.ST_TIMING_INVALID)
        details.append(
            f"timing '{receipt.timing}' not in {sorted(ST_TIMING_KINDS)}"
        )

    # component version drift
    if expected_component_version is not None:
        if receipt.component_version != expected_component_version:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"component_version drift: claims "
                f"{receipt.component_version}, expected "
                f"{expected_component_version}"
            )

    # renderer_receipt_id required (must chain from renderer)
    if not receipt.renderer_receipt_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("renderer_receipt_id is empty — must chain from renderer")

    # hint_instance_id required
    if not receipt.hint_instance_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("hint_instance_id is empty")

    # content_hash
    if not receipt.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif receipt.content_hash != receipt.compute_content_hash():
        errors.append(EC.ST_BINDING_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {receipt.content_hash}, "
            f"computed {receipt.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return BindingReceiptVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        receipt_id=receipt.receipt_id,
    )


class Binder:
    """Binder — 将渲染的 hint 绑定到 problem context。

    纯程序实现：给定 position/timing/scope，产出 BindingReceipt。
    """

    def __init__(self, *, component_version: str = "st1-binding-v1") -> None:
        self.component_version = component_version

    def bind(
        self,
        *,
        receipt_id: str,
        release_ref: dict[str, str],
        renderer_receipt_id: str,
        hint_instance_id: str,
        position: str = "PRE_TRACE",
        timing: str = "BEFORE_SOLVE",
        scope: str = "",
        problem_context_ref: dict[str, str] | None = None,
        kind: str = "FULL_BINDING",
        frozen_at: str = "",
    ) -> BindingReceipt:
        return make_binding_receipt(
            receipt_id=receipt_id,
            release_ref=release_ref,
            renderer_receipt_id=renderer_receipt_id,
            hint_instance_id=hint_instance_id,
            kind=kind,
            position=position,
            timing=timing,
            scope=scope,
            problem_context_ref=problem_context_ref,
            component_version=self.component_version,
            frozen_at=frozen_at,
        )
