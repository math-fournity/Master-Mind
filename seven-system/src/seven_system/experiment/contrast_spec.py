"""ContrastSpec — WP-EX1 冻结对比规格。

关键约束（blocker）：
- 对比必须在 P4 预注册（EX_CONTRAST_NOT_PREREGISTERED）
- 对比引用的 arm 必须存在于 plan 中（EX_CONTRAST_ARMS_NOT_FOUND）
- contrast_kind 在 EX_CONTRAST_KINDS 中（EX_CONTRAST_KIND_INVALID）
- metric 非空（EX_CONTRAST_METRIC_INVALID）
- 对比级证据只引用预注册对比

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    EX_CONTRAST_KINDS,
    VerificationErrorCode as EC,
)


_SCHEMA_ID = "seven/contrast-spec"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class ContrastSpec:
    """冻结对比规格——P4 预注册。

    字段：
        contrast_id: 唯一标识
        contrast_kind: 对比种类（EX_CONTRAST_KINDS）
        arm_kinds: 参与对比的 arm kind 列表
        metric: 评估指标
        hypothesis: 假设声明
        pre_registered: 是否已预注册
        content_hash: 内容哈希
    """

    contrast_id: str
    contrast_kind: str
    arm_kinds: tuple[str, ...] = ()
    metric: str = ""
    hypothesis: str = ""
    pre_registered: bool = True
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "contrast_id": self.contrast_id,
            "contrast_kind": self.contrast_kind,
            "arm_kinds": list(self.arm_kinds),
            "metric": self.metric,
            "hypothesis": self.hypothesis,
            "pre_registered": self.pre_registered,
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


def make_contrast_spec(
    *,
    contrast_id: str,
    contrast_kind: str,
    arm_kinds: list[str] | tuple[str, ...] = (),
    metric: str = "math_correct",
    hypothesis: str = "",
    pre_registered: bool = True,
) -> ContrastSpec:
    cs = ContrastSpec(
        contrast_id=contrast_id,
        contrast_kind=contrast_kind,
        arm_kinds=tuple(arm_kinds),
        metric=metric,
        hypothesis=hypothesis,
        pre_registered=pre_registered,
    )
    return dataclasses.replace(cs, content_hash=cs.compute_content_hash())


@dataclass(frozen=True)
class ContrastSpecVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    contrast_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_contrast_spec(
    contrast: ContrastSpec,
    *,
    available_arm_kinds: set[str] | None = None,
) -> ContrastSpecVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = contrast.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    # contrast_kind valid
    if contrast.contrast_kind not in EX_CONTRAST_KINDS:
        errors.append(EC.EX_CONTRAST_KIND_INVALID)
        details.append(
            f"contrast_kind '{contrast.contrast_kind}' not in {sorted(EX_CONTRAST_KINDS)}"
        )

    # arm_kinds non-empty
    if not contrast.arm_kinds:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("arm_kinds must not be empty")

    # metric non-empty
    if not contrast.metric:
        errors.append(EC.EX_CONTRAST_METRIC_INVALID)
        details.append("metric must not be empty")

    # pre_registered
    if not contrast.pre_registered:
        errors.append(EC.EX_CONTRAST_NOT_PREREGISTERED)
        details.append("contrast must be pre-registered in P4 plan")

    # arms must exist in available arm_kinds
    if available_arm_kinds is not None and contrast.arm_kinds:
        for ak in contrast.arm_kinds:
            if ak not in available_arm_kinds:
                errors.append(EC.EX_CONTRAST_ARMS_NOT_FOUND)
                details.append(
                    f"arm_kind '{ak}' not found in available arms "
                    f"{sorted(available_arm_kinds)}"
                )

    # content_hash
    if not contrast.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif contrast.content_hash != contrast.compute_content_hash():
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {contrast.content_hash}, "
            f"computed {contrast.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return ContrastSpecVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        contrast_id=contrast.contrast_id,
    )
