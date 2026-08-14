"""HarnessProfile — 冻结 harness profile（WP-SV1）。

HarnessProfile 记录 solver_harness 的冻结配置：
- version：profile 版本
- content_hash：profile 内容 hash
- supersedes_ref：被此 profile 取代的旧 profile 引用
- harness_kind：harness 种类（DEVIN_HARNESS / FAKE_HARNESS）
- tool_policy_kind：工具策略（v1 只允许 NO_TOOL）

验证器检查：
1. version 非空
2. content_hash 是合法 sha256
3. harness_kind 在允许集合中
4. tool_policy_kind 在 SV_TOOL_POLICY_KINDS 中
5. profile_hash 正确

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from ...hashing import canonical_json_bytes
from ...contracts.errors import (
    SV_TOOL_POLICY_KINDS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


_PROFILE_HASH_ALGORITHM = "sha256(RFC8785-JCS-object-with-profile_hash-null)"

HARNESS_KINDS: frozenset[str] = frozenset(
    {"DEVIN_HARNESS", "FAKE_HARNESS"}
)


@dataclass(frozen=True)
class HarnessProfile:
    """HarnessProfile — 冻结 harness profile。"""

    version: str
    content_hash: str
    harness_kind: str
    tool_policy_kind: str
    supersedes_ref: str
    profile_hash_algorithm: str
    profile_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": self.version,
            "content_hash": self.content_hash,
            "harness_kind": self.harness_kind,
            "tool_policy_kind": self.tool_policy_kind,
            "supersedes_ref": self.supersedes_ref,
            "profile_hash_algorithm": self.profile_hash_algorithm,
            "profile_hash": self.profile_hash,
        }


def build_harness_profile(
    *,
    version: str,
    content_hash: str,
    harness_kind: str = "DEVIN_HARNESS",
    tool_policy_kind: str = "NO_TOOL",
    supersedes_ref: str = "",
) -> HarnessProfile:
    """构建 HarnessProfile，自动计算 profile_hash。"""
    obj = {
        "version": version,
        "content_hash": content_hash,
        "harness_kind": harness_kind,
        "tool_policy_kind": tool_policy_kind,
        "supersedes_ref": supersedes_ref,
        "profile_hash_algorithm": _PROFILE_HASH_ALGORITHM,
        "profile_hash": None,
    }
    profile_hash = hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

    return HarnessProfile(
        version=version,
        content_hash=content_hash,
        harness_kind=harness_kind,
        tool_policy_kind=tool_policy_kind,
        supersedes_ref=supersedes_ref,
        profile_hash_algorithm=_PROFILE_HASH_ALGORITHM,
        profile_hash=profile_hash,
    )


def verify_harness_profile(
    profile: HarnessProfile | dict[str, Any],
) -> VerificationResult:
    """验证 HarnessProfile 的 schema + semantic 合法性。

    检查：
    1. version 非空
    2. content_hash 是合法 sha256
    3. harness_kind 在 HARNESS_KINDS 中
    4. tool_policy_kind 在 SV_TOOL_POLICY_KINDS 中
    5. profile_hash 正确
    """
    if isinstance(profile, HarnessProfile):
        profile_dict = profile.to_dict()
    else:
        profile_dict = profile

    errors: list[EC] = []
    details: list[str] = []

    def _err(code: EC, detail: str) -> None:
        errors.append(code)
        details.append(detail)

    # 1. version
    if not profile_dict.get("version"):
        _err(EC.SV_HARNESS_PROFILE_HASH_MISMATCH, "version is empty")

    # 2. content_hash
    content_hash = profile_dict.get("content_hash", "")
    if not (
        isinstance(content_hash, str)
        and len(content_hash) == 64
        and all(c in "0123456789abcdef" for c in content_hash)
    ):
        _err(EC.SV_HARNESS_PROFILE_HASH_MISMATCH,
             "content_hash must be a lowercase sha256 hex")

    # 3. harness_kind
    harness_kind = profile_dict.get("harness_kind", "")
    if harness_kind not in HARNESS_KINDS:
        _err(EC.SV_HARNESS_PROFILE_HASH_MISMATCH,
             f"harness_kind {harness_kind!r} not in HARNESS_KINDS")

    # 4. tool_policy_kind
    tp_kind = profile_dict.get("tool_policy_kind", "")
    if tp_kind not in SV_TOOL_POLICY_KINDS:
        _err(EC.SV_TOOL_POLICY_KIND_INVALID,
             f"tool_policy_kind {tp_kind!r} not in SV_TOOL_POLICY_KINDS")

    # 5. profile_hash
    if profile_dict.get("profile_hash_algorithm") != _PROFILE_HASH_ALGORITHM:
        _err(EC.OBJECT_HASH_MISMATCH,
             f"unexpected profile_hash_algorithm: "
             f"{profile_dict.get('profile_hash_algorithm')}")
    obj_for_hash = dict(profile_dict)
    obj_for_hash["profile_hash"] = None
    computed_hash = hashlib.sha256(canonical_json_bytes(obj_for_hash)).hexdigest()
    if profile_dict.get("profile_hash") != computed_hash:
        _err(EC.SV_HARNESS_PROFILE_HASH_MISMATCH,
             f"profile_hash mismatch: expected {computed_hash}, "
             f"got {profile_dict.get('profile_hash')}")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)
