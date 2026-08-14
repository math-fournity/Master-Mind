"""Renderer — WP-ST1 将选中的 Tell 渲染为 model-facing 表达（HintInstance）。

关键约束（blocker）：
- Renderer 使用 TX1 的 HintRenderer 渲染
- 输出是 bound payload（HintInstance），不是 raw Tell
- Core/text 混淆：TellCore 的 invariant_description 不得直接作为 text payload
  （ST_CORE_TEXT_CONFUSION）
- Answer 不得绑定到 hint（ST_ANSWER_BOUND_TO_HINT）
- Renderer 引用 HintRenderer by hash
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
    ST_RENDERER_KINDS,
    VerificationErrorCode as EC,
)
from ..taxonomy.boundary import HintInstance, make_hint_instance


_RENDERER_RECEIPT_SCHEMA_ID = "seven/renderer-receipt"
_RENDERER_RECEIPT_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class RendererReceipt:
    """Renderer 运行收据——记录渲染结果。

    字段：
        receipt_id: 唯一标识
        release_ref: TellStrategyRelease 引用
        selector_receipt_id: 上游 SelectorReceipt ID
        renderer_ref: HintRenderer 引用 {renderer_id, version, content_hash}
        hint_instance: 渲染产出的 HintInstance（来自 TX1）
        kind: renderer 输出种类（ST_RENDERER_KINDS）
        rendered_payload: 绑定的 payload（不是 raw Tell）
        component_version: renderer 组件版本
        content_hash: 内容哈希
    """

    receipt_id: str
    release_ref: dict[str, str] = field(default_factory=dict)
    selector_receipt_id: str = ""
    renderer_ref: dict[str, str] = field(default_factory=dict)
    hint_instance: HintInstance | None = None
    kind: str = "HINT_INSTANCE"
    rendered_payload: dict[str, Any] = field(default_factory=dict)
    component_version: str = ""
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _RENDERER_RECEIPT_SCHEMA_ID,
            "schema_version": _RENDERER_RECEIPT_SCHEMA_VERSION,
            "receipt_id": self.receipt_id,
            "release_ref": dict(self.release_ref),
            "selector_receipt_id": self.selector_receipt_id,
            "renderer_ref": dict(self.renderer_ref),
            "hint_instance": (
                self.hint_instance.to_dict() if self.hint_instance else None
            ),
            "kind": self.kind,
            "rendered_payload": dict(self.rendered_payload),
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


def make_renderer_receipt(
    *,
    receipt_id: str,
    release_ref: dict[str, str] | None = None,
    selector_receipt_id: str = "",
    renderer_ref: dict[str, str] | None = None,
    kind: str = "HINT_INSTANCE",
    rendered_payload: dict[str, Any] | None = None,
    component_version: str = "",
    frozen_at: str = "",
) -> RendererReceipt:
    """构建 RendererReceipt，内部自动构建 HintInstance。"""
    payload = rendered_payload or {}
    instance = make_hint_instance(
        instance_id=f"{receipt_id}-hint",
        renderer_ref=renderer_ref or {},
        payload=payload,
        bound_at=frozen_at,
    )
    r = RendererReceipt(
        receipt_id=receipt_id,
        release_ref=release_ref or {},
        selector_receipt_id=selector_receipt_id,
        renderer_ref=renderer_ref or {},
        hint_instance=instance,
        kind=kind,
        rendered_payload=payload,
        component_version=component_version,
        frozen_at=frozen_at,
    )
    return dataclasses.replace(r, content_hash=r.compute_content_hash())


@dataclass(frozen=True)
class RendererReceiptVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    receipt_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_renderer_receipt(
    receipt: RendererReceipt,
    *,
    expected_release_hash: str | None = None,
    expected_component_version: str | None = None,
    expected_renderer_hash: str | None = None,
    forbidden_answer_keys: set[str] | None = None,
    core_invariant_description: str = "",
) -> RendererReceiptVerificationResult:
    """验证 RendererReceipt。

    参数：
        expected_release_hash: TellStrategyRelease content_hash
        expected_component_version: 期望的 renderer 组件版本
        expected_renderer_hash: HintRenderer content_hash
        forbidden_answer_keys: payload 中不得出现的 answer 泄漏键
        core_invariant_description: TellCore 的 invariant_description
            （用于 core/text confusion 检查）
    """
    errors: list[EC] = []
    details: list[str] = []

    d = receipt.to_dict()
    if d.get("schema_id") != _RENDERER_RECEIPT_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_RENDERER_RECEIPT_SCHEMA_ID}")

    # kind valid
    if receipt.kind not in ST_RENDERER_KINDS:
        errors.append(EC.ST_RENDERER_KIND_INVALID)
        details.append(
            f"kind '{receipt.kind}' not in {sorted(ST_RENDERER_KINDS)}"
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

    # renderer_ref required — must reference HintRenderer by hash
    if not receipt.renderer_ref.get("renderer_id"):
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("renderer_ref must contain renderer_id")
    if not receipt.renderer_ref.get("content_hash"):
        errors.append(EC.ST_RENDERER_HASH_MISMATCH)
        details.append("renderer_ref must contain content_hash")

    if expected_renderer_hash is not None:
        if receipt.renderer_ref.get("content_hash") != expected_renderer_hash:
            errors.append(EC.ST_RENDERER_HASH_MISMATCH)
            details.append(
                f"renderer_ref content_hash mismatch: claims "
                f"{receipt.renderer_ref.get('content_hash')}, "
                f"expected {expected_renderer_hash}"
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

    # blocker: answer bound to hint — payload must not contain answer keys
    if forbidden_answer_keys:
        payload_keys = set(receipt.rendered_payload.keys())
        leaked = payload_keys & forbidden_answer_keys
        if leaked:
            errors.append(EC.ST_ANSWER_BOUND_TO_HINT)
            details.append(
                f"rendered_payload contains answer-leakage keys: "
                f"{sorted(leaked)} — answer must not be bound to hint"
            )

    # blocker: core/text confusion — TellCore invariant_description must
    # not appear as raw text payload
    if core_invariant_description and core_invariant_description.strip():
        payload_text = str(receipt.rendered_payload.get("text", ""))
        if payload_text == core_invariant_description:
            errors.append(EC.ST_CORE_TEXT_CONFUSION)
            details.append(
                "rendered_payload.text equals TellCore invariant_description "
                "— Core content must not be confused with text payload"
            )
        # also check if any payload value equals the invariant description
        for k, v in receipt.rendered_payload.items():
            if isinstance(v, str) and v == core_invariant_description:
                errors.append(EC.ST_CORE_TEXT_CONFUSION)
                details.append(
                    f"rendered_payload.{k} equals TellCore "
                    f"invariant_description — Core/text confusion"
                )
                break

    # hint_instance must be present
    if receipt.hint_instance is None:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("hint_instance is missing")

    # content_hash
    if not receipt.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif receipt.content_hash != receipt.compute_content_hash():
        errors.append(EC.ST_RENDERER_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {receipt.content_hash}, "
            f"computed {receipt.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return RendererReceiptVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        receipt_id=receipt.receipt_id,
    )


class Renderer:
    """Renderer — 将选中的 Tell 渲染为 model-facing HintInstance。

    纯程序实现：给定 renderer_ref + payload，产出 RendererReceipt。
    输出是 bound payload，不是 raw Tell。
    """

    def __init__(self, *, component_version: str = "st1-renderer-v1") -> None:
        self.component_version = component_version

    def render(
        self,
        *,
        receipt_id: str,
        release_ref: dict[str, str],
        selector_receipt_id: str,
        renderer_ref: dict[str, str],
        payload: dict[str, Any],
        kind: str = "HINT_INSTANCE",
        frozen_at: str = "",
    ) -> RendererReceipt:
        """执行渲染——产出 bound payload HintInstance。"""
        return make_renderer_receipt(
            receipt_id=receipt_id,
            release_ref=release_ref,
            selector_receipt_id=selector_receipt_id,
            renderer_ref=renderer_ref,
            kind=kind,
            rendered_payload=payload,
            component_version=self.component_version,
            frozen_at=frozen_at,
        )
