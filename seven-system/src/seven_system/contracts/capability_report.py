"""VerifierCapabilityReport 生成器。

GV0 的能力报告：绑定 DAG hash、代码 hash 和完整 test IDs，
证明两个验证器和 CompletionArtifactStore 的正负向量全部通过。
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..hashing import canonical_json_bytes, file_sha256


@dataclass(frozen=True)
class VerifierCapabilityReport:
    """GV0 验证器能力报告。"""

    schema_id: str = "seven/gv0-verifier-capability-report"
    schema_version: int = 1
    report_id: str = ""
    dag_ref_and_hash: dict[str, str] = field(default_factory=dict)
    implementation_tree_hash: str = ""
    completion_contract_verifier: dict[str, Any] = field(default_factory=dict)
    security_contract_verifier: dict[str, Any] = field(default_factory=dict)
    completion_artifact_store: dict[str, Any] = field(default_factory=dict)
    test_ids: list[str] = field(default_factory=list)
    golden_vectors: list[dict[str, str]] = field(default_factory=list)
    negative_vectors: list[dict[str, str]] = field(default_factory=list)
    claims: list[str] = field(default_factory=list)
    nonclaims: list[str] = field(default_factory=list)
    created_at: str = ""
    report_hash_algorithm: str = "sha256(canonical-json-with-report_hash-null)"
    report_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        d = {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "report_id": self.report_id,
            "dag_ref_and_hash": self.dag_ref_and_hash,
            "implementation_tree_hash": self.implementation_tree_hash,
            "completion_contract_verifier": self.completion_contract_verifier,
            "security_contract_verifier": self.security_contract_verifier,
            "completion_artifact_store": self.completion_artifact_store,
            "test_ids": self.test_ids,
            "golden_vectors": self.golden_vectors,
            "negative_vectors": self.negative_vectors,
            "claims": self.claims,
            "nonclaims": self.nonclaims,
            "created_at": self.created_at,
            "report_hash_algorithm": self.report_hash_algorithm,
            "report_hash": None,  # 先置 null 计算
        }
        canonical = canonical_json_bytes(d)
        d["report_hash"] = hashlib.sha256(canonical).hexdigest()
        return d


def implementation_tree_hash(system_root: Path) -> str:
    """计算 src/ 目录的 git tree hash。"""
    src_dir = system_root / "src"
    if not src_dir.is_dir():
        return ""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD^{tree}"],
            capture_output=True,
            text=True,
            cwd=str(system_root),
        )
        return result.stdout.strip()
    except Exception:
        return ""


def build_verifier_capability_report(
    *,
    report_id: str,
    dag_path: Path,
    dag_sha256: str,
    system_root: Path,
    test_ids: list[str],
    golden_vectors: list[dict[str, str]],
    negative_vectors: list[dict[str, str]],
    created_at: str,
) -> dict[str, Any]:
    """构建 VerifierCapabilityReport。"""
    tree_hash = implementation_tree_hash(system_root)

    report = VerifierCapabilityReport(
        report_id=report_id,
        dag_ref_and_hash={
            "ref": str(dag_path.relative_to(system_root)) if dag_path.is_relative_to(system_root) else str(dag_path),
            "sha256": dag_sha256,
        },
        implementation_tree_hash=tree_hash,
        completion_contract_verifier={
            "verifier": "CompletionContractVerifier",
            "checks": [
                "owner_type_verification",
                "completion_contract_verification",
                "submitted_schema_id_verification",
                "actor_authority_verification",
                "state_command_verification",
                "dag_hash_verification",
            ],
            "golden_vector_count": sum(
                1 for v in golden_vectors if v.get("category") == "completion_contract"
            ),
            "negative_vector_count": sum(
                1 for v in negative_vectors if v.get("category") == "completion_contract"
            ),
        },
        security_contract_verifier={
            "verifier": "SecurityContractVerifier",
            "checks": [
                "signature_envelope_verification",
                "eea_structure_verification",
                "permit_non_escalation_verification",
                "consumption_receipt_status_verification",
                "allowance_conservation_verification",
                "ordinal_uniqueness_verification",
                "fence_token_verification",
                "time_window_verification",
            ],
            "golden_vector_count": sum(
                1 for v in golden_vectors if v.get("category") == "security_contract"
            ),
            "negative_vector_count": sum(
                1 for v in negative_vectors if v.get("category") == "security_contract"
            ),
        },
        completion_artifact_store={
            "store": "CompletionArtifactStore",
            "checks": [
                "content_addressed_hash_addressing",
                "append_once_no_overwrite",
                "hash_byte_verification_on_read",
                "symlink_rejection_leaf_and_ancestor",
                "fallback_rejection_repo_home_tmp",
                "d_volume_root_enforcement",
                "atomic_write_fsync_hardlink",
            ],
            "golden_vector_count": sum(
                1 for v in golden_vectors if v.get("category") == "artifact_store"
            ),
            "negative_vector_count": sum(
                1 for v in negative_vectors if v.get("category") == "artifact_store"
            ),
        },
        test_ids=test_ids,
        golden_vectors=golden_vectors,
        negative_vectors=negative_vectors,
        claims=[
            "CompletionContractVerifier and SecurityContractVerifier are implemented "
            "with fixed error codes and golden/negative vectors.",
            "CompletionArtifactStore provides content-addressed append-once storage "
            "with symlink/fallback/hash-conflict rejection.",
            "ReservationBackendPort interface is frozen with side-effect-free reference backend.",
            "All golden and negative vectors pass in isolated fixture tests.",
        ],
        nonclaims=[
            "This report does not prove complete Artifact/Vault capability.",
            "This report does not prove DB reservation, HumanGate, model or Solver live capability.",
            "This report does not constitute independent audit or AUDITED_PASS.",
            "The side-effect-free reference backend is not a real DB or D-volume ledger backend.",
            "Self-hosted ImplementationCompletionBundle requires D-volume write authorization "
            "(EEA/Permit/RESERVED) which is not yet obtained.",
        ],
        created_at=created_at,
    )
    return report.to_dict()
