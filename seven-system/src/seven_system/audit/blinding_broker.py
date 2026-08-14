"""BlindingBroker — 从 sealed P5 RunArtifactBundle 生成三个盲化 view。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P6 节：

Blinding Broker 生成三个 view；每个 view 有不同的 redaction/scope。
真实 arm 身份不得泄漏到 view 中。

三个 view：
1. process_auditor_view: trigger→binding→action→progress→termination 与 first divergence
   - 包含：trajectory 事件序列、trigger/binding/action/progress/termination 元数据
   - redact: arm_id、arm_kind、answer、solution information atoms
2. proof_judge_view: 数学正确性与完备性
   - 包含：problem statement、solution/proof 文本、trajectory 中的数学步骤
   - redact: arm_id、arm_kind、trigger/binding 元数据、cost
3. leakage_auditor_view: 完整 Solver payload 与 solution information atoms
   - 包含：完整 Solver payload、solution information atoms、leakage budget
   - redact: arm_id、arm_kind（但保留 payload 内容用于 leakage 分析）

关键约束（blocker）：
- 真实 arm 身份泄漏到 view → AU_ARM_LEAKED_INTO_VIEW
- view hash 必须与 broker 声称的一致 → AU_VIEW_HASH_MISMATCH
- 三个 view 必须独立、各自不同 → AU_BLINDING_INVALID

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    AU_VIEW_KINDS,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


_SCHEMA_ID = "seven/blinded-view"
_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-view_hash-null)"

# arm 身份相关字段——这些字段不得出现在任何 blinded view 中
_ARM_IDENTITY_FIELDS = frozenset(
    {"arm_id", "arm_kind", "arm_label", "arm_description"}
)


@dataclass(frozen=True)
class BlindedView:
    """单个审计角色的盲化 view。

    字段：
        view_id: 唯一标识
        view_kind: view 种类（AU_VIEW_KINDS）
        role_type_id: 对应的审计角色
        source_bundle_ref: 源 RunArtifactBundle 引用 {bundle_id, content_hash}
        redacted_payload: 盲化后的 payload（已 redact arm 身份）
        view_hash: view 内容哈希
        source_hash: 源 bundle content_hash（用于完整性校验）
        redaction_manifest: redaction 规则清单
    """

    view_id: str
    view_kind: str
    role_type_id: str
    source_bundle_ref: dict[str, str] = field(default_factory=dict)
    redacted_payload: dict[str, Any] = field(default_factory=dict)
    view_hash: str = ""
    source_hash: str = ""
    redaction_manifest: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _SCHEMA_ID,
            "schema_version": _SCHEMA_VERSION,
            "view_id": self.view_id,
            "view_kind": self.view_kind,
            "role_type_id": self.role_type_id,
            "source_bundle_ref": dict(self.source_bundle_ref),
            "redacted_payload": dict(self.redacted_payload),
            "view_hash": self.view_hash,
            "source_hash": self.source_hash,
            "redaction_manifest": dict(self.redaction_manifest),
            "hash_algorithm": _HASH_ALGORITHM,
        }

    def compute_view_hash(self) -> str:
        d = self.to_dict()
        d["view_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.view_hash == self.compute_view_hash()


def _contains_arm_identity(payload: Any, *, _depth: int = 0) -> bool:
    """递归检查 payload 中是否包含 arm 身份字段。"""
    if _depth > 20:
        return False
    if isinstance(payload, dict):
        for key in payload:
            if key in _ARM_IDENTITY_FIELDS:
                val = payload[key]
                if isinstance(val, str) and val:
                    return True
        for val in payload.values():
            if _contains_arm_identity(val, _depth=_depth + 1):
                return True
    elif isinstance(payload, list):
        for item in payload:
            if _contains_arm_identity(item, _depth=_depth + 1):
                return True
    return False


def _redact_arm_identity(payload: Any) -> Any:
    """递归 redact arm 身份字段——替换为 "__REDACTED__"。"""
    if isinstance(payload, dict):
        result: dict[str, Any] = {}
        for key, val in payload.items():
            if key in _ARM_IDENTITY_FIELDS:
                result[key] = "__REDACTED__"
            else:
                result[key] = _redact_arm_identity(val)
        return result
    if isinstance(payload, list):
        return [_redact_arm_identity(item) for item in payload]
    return payload


def _build_process_auditor_view(
    bundle_dict: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    """构建 process_auditor_view 的 payload 和 redaction_manifest。

    包含：trajectory 事件序列、trigger/binding/action/progress/termination 元数据
    redact: arm_id、arm_kind、answer、solution information atoms
    """
    raw_payload = {
        "trajectory_ref": bundle_dict.get("trajectory_ref", {}),
        "termination_reason": bundle_dict.get("termination_reason", ""),
        "observability_status": bundle_dict.get("observability_status", ""),
        "observability_state": bundle_dict.get("observability_state", {}),
        "run_state": bundle_dict.get("run_state", ""),
        "cost_observability": bundle_dict.get("cost_observability", {}),
        "process_events": bundle_dict.get("process_events", []),
    }
    redacted = _redact_arm_identity(raw_payload)
    manifest = {
        "redacted_fields": sorted(_ARM_IDENTITY_FIELDS),
        "removed_fields": ["answer_ref", "solution_information_atoms"],
        "scope": "trigger_binding_action_progress_termination_first_divergence",
    }
    return redacted, manifest


def _build_proof_judge_view(
    bundle_dict: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    """构建 proof_judge_view 的 payload 和 redaction_manifest。

    包含：problem statement、solution/proof 文本、trajectory 中的数学步骤
    redact: arm_id、arm_kind、trigger/binding 元数据、cost
    """
    raw_payload = {
        "problem_ref": bundle_dict.get("problem_ref", {}),
        "solution_ref": bundle_dict.get("solution_ref", {}),
        "trajectory_math_steps": bundle_dict.get("trajectory_math_steps", []),
        "termination_reason": bundle_dict.get("termination_reason", ""),
    }
    redacted = _redact_arm_identity(raw_payload)
    manifest = {
        "redacted_fields": sorted(_ARM_IDENTITY_FIELDS),
        "removed_fields": ["cost_observability", "trigger_ref", "binding_ref"],
        "scope": "math_correctness_and_completeness",
    }
    return redacted, manifest


def _build_leakage_auditor_view(
    bundle_dict: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    """构建 leakage_auditor_view 的 payload 和 redaction_manifest。

    包含：完整 Solver payload、solution information atoms、leakage budget
    redact: arm_id、arm_kind（但保留 payload 内容用于 leakage 分析）
    """
    raw_payload = {
        "raw_artifact_ref": bundle_dict.get("raw_artifact_ref", {}),
        "parser_ref": bundle_dict.get("parser_ref", {}),
        "trajectory_ref": bundle_dict.get("trajectory_ref", {}),
        "answer_ref": bundle_dict.get("answer_ref", {}),
        "solution_information_atoms": bundle_dict.get("solution_information_atoms", []),
        "solver_payload": bundle_dict.get("solver_payload", {}),
        "termination_reason": bundle_dict.get("termination_reason", ""),
    }
    redacted = _redact_arm_identity(raw_payload)
    manifest = {
        "redacted_fields": sorted(_ARM_IDENTITY_FIELDS),
        "removed_fields": [],
        "scope": "complete_solver_payload_and_solution_information_atoms",
    }
    return redacted, manifest


_VIEW_BUILDERS = {
    "process_auditor_view": _build_process_auditor_view,
    "proof_judge_view": _build_proof_judge_view,
    "leakage_auditor_view": _build_leakage_auditor_view,
}

_VIEW_KIND_TO_ROLE = {
    "process_auditor_view": "process_auditor",
    "proof_judge_view": "proof_judge",
    "leakage_auditor_view": "leakage_auditor",
}


@dataclass
class BlindingBroker:
    """BlindingBroker — 盲化 Broker，从 sealed P5 bundle 生成三个盲化 view。

    硬约束：
    - 真实 arm 身份不得泄漏到任何 view
    - 三个 view 必须独立、各自不同
    - 每个 view 的 view_hash 必须与 broker 声称的一致
    - 源 bundle 必须已 sealed
    """

    # 已生成的 view（view_id → BlindedView）
    views: dict[str, BlindedView] = field(default_factory=dict)

    def generate_views(
        self,
        *,
        bundle_id: str,
        bundle_content_hash: str,
        bundle_dict: dict[str, Any],
        sealed: bool = True,
        plan_id: str = "",
    ) -> tuple[VerificationResult, dict[str, BlindedView] | None]:
        """从 sealed P5 RunArtifactBundle 生成三个盲化 view。

        返回 (result, views_dict)。
        views_dict: view_kind → BlindedView
        """
        errors: list[EC] = []
        details: list[str] = []

        # 源 bundle 必须 sealed
        if not sealed:
            errors.append(EC.AU_BUNDLE_REF_MISSING)
            details.append("source bundle must be sealed before blinding")

        # 源 bundle content_hash 必须非空
        if not bundle_content_hash:
            errors.append(EC.AU_BUNDLE_REF_MISSING)
            details.append("source bundle content_hash is empty")

        if errors:
            return VerificationResult(
                verdict="FAIL", error_codes=errors, details=details
            ), None

        source_ref = {
            "bundle_id": bundle_id,
            "content_hash": bundle_content_hash,
        }

        generated: dict[str, BlindedView] = {}
        for view_kind in AU_VIEW_KINDS:
            builder = _VIEW_BUILDERS[view_kind]
            payload, manifest = builder(bundle_dict)

            # 检查 arm 身份是否泄漏
            if _contains_arm_identity(payload):
                errors.append(EC.AU_ARM_LEAKED_INTO_VIEW)
                details.append(
                    f"arm identity leaked into {view_kind} payload"
                )
                continue

            role_type_id = _VIEW_KIND_TO_ROLE[view_kind]
            view_id = f"view-{bundle_id}-{view_kind}"

            view = BlindedView(
                view_id=view_id,
                view_kind=view_kind,
                role_type_id=role_type_id,
                source_bundle_ref=source_ref,
                redacted_payload=payload,
                source_hash=bundle_content_hash,
                redaction_manifest=manifest,
            )
            # 计算 view_hash
            view_hash = view.compute_view_hash()
            # 用 dataclasses.replace 不可行（frozen + field），直接构造
            view = BlindedView(
                view_id=view.view_id,
                view_kind=view.view_kind,
                role_type_id=view.role_type_id,
                source_bundle_ref=view.source_bundle_ref,
                redacted_payload=view.redacted_payload,
                view_hash=view_hash,
                source_hash=view.source_hash,
                redaction_manifest=view.redaction_manifest,
            )
            generated[view_kind] = view
            self.views[view_id] = view

        if errors:
            return VerificationResult(
                verdict="FAIL", error_codes=errors, details=details
            ), None

        # 三个 view 必须各自不同（view_hash 互异）
        view_hashes = [v.view_hash for v in generated.values()]
        if len(set(view_hashes)) != len(view_hashes):
            errors.append(EC.AU_BLINDING_INVALID)
            details.append("three views must have distinct view_hashes")

        if errors:
            return VerificationResult(
                verdict="FAIL", error_codes=errors, details=details
            ), None

        return VerificationResult(verdict="PASS"), generated


def verify_blinded_view(view: BlindedView) -> VerificationResult:
    """验证单个 BlindedView 的合法性。"""
    errors: list[EC] = []
    details: list[str] = []

    d = view.to_dict()
    if d.get("schema_id") != _SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_SCHEMA_ID}")

    if view.view_kind not in AU_VIEW_KINDS:
        errors.append(EC.AU_BLINDING_INVALID)
        details.append(f"view_kind {view.view_kind} not in AU_VIEW_KINDS")

    if not view.view_id:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("view_id is empty")

    if not view.source_bundle_ref.get("bundle_id"):
        errors.append(EC.AU_BUNDLE_REF_MISSING)
        details.append("source_bundle_ref missing bundle_id")
    if not view.source_bundle_ref.get("content_hash"):
        errors.append(EC.AU_BUNDLE_REF_MISSING)
        details.append("source_bundle_ref missing content_hash")

    # arm 身份不得泄漏
    if _contains_arm_identity(view.redacted_payload):
        errors.append(EC.AU_ARM_LEAKED_INTO_VIEW)
        details.append("arm identity leaked into redacted_payload")

    # view_hash 校验
    if not view.view_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("view_hash is empty")
    elif view.view_hash != view.compute_view_hash():
        errors.append(EC.AU_VIEW_HASH_MISMATCH)
        details.append(
            f"view_hash mismatch: claims {view.view_hash}, "
            f"computed {view.compute_view_hash()}"
        )

    # source_hash 必须与 source_bundle_ref.content_hash 一致
    if view.source_hash and view.source_bundle_ref.get("content_hash"):
        if view.source_hash != view.source_bundle_ref["content_hash"]:
            errors.append(EC.AU_VIEW_HASH_MISMATCH)
            details.append("source_hash != source_bundle_ref.content_hash")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(
        verdict=verdict, error_codes=errors, details=details
    )


def check_arm_leakage(view: BlindedView) -> bool:
    """检查 view 中是否泄漏了 arm 身份。返回 True 表示泄漏（blocker）。"""
    return _contains_arm_identity(view.redacted_payload)
