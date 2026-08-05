"""
VisibilityLabelChecker：visibility label检查函数

对应134号P4-4.6 + 123号§607。

123号§607：角色边界必须落实为collection、visibility label和能力令牌，
而不是只写在角色prompt里。

127号§10.3可见性矩阵——8角色×14 collection的可见性标记。
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Set
from enum import Enum


class VisibilityLevel(str, Enum):
    """127号§10.3可见性标记"""
    READ_ONLY = "R"
    READ_WRITE = "R/W"
    INVISIBLE = "—"
    CONDITIONAL = "R(限定)"


# 127号§10.3可见性矩阵——8角色×14 collection
# 来源：127号§10.3逐字提取（subagent 8681b7de返回）
VISIBILITY_MATRIX: Dict[str, Dict[str, str]] = {
    "solver": {
        "tasks": "R", "workspaces": "R/W", "raw_events": "—",
        "semantic_events": "R", "obligations": "R/W", "evidence": "R",
        "representations": "R", "heuristic_rules": "—",
        "activation_packets": "R", "truth_vault": "—",
        "manifests": "—", "audit_verdicts": "—",
        "dg_nodes": "R", "dg_edges": "R",
    },
    "event_capture": {
        "tasks": "R", "workspaces": "R", "raw_events": "R/W",
        "semantic_events": "R/W", "obligations": "—", "evidence": "—",
        "representations": "—", "heuristic_rules": "—",
        "activation_packets": "—", "truth_vault": "—",
        "manifests": "—", "audit_verdicts": "—",
        "dg_nodes": "—", "dg_edges": "—",
    },
    "state_reducer": {
        "tasks": "R", "workspaces": "R/W", "raw_events": "R",
        "semantic_events": "R", "obligations": "R/W", "evidence": "R",
        "representations": "R", "heuristic_rules": "—",
        "activation_packets": "—", "truth_vault": "—",
        "manifests": "—", "audit_verdicts": "—",
        "dg_nodes": "R", "dg_edges": "R",
    },
    "retriever": {
        "tasks": "R", "workspaces": "R", "raw_events": "—",
        "semantic_events": "R", "obligations": "R", "evidence": "R",
        "representations": "R", "heuristic_rules": "R",
        "activation_packets": "—", "truth_vault": "—",
        "manifests": "—", "audit_verdicts": "—",
        "dg_nodes": "R", "dg_edges": "R",
    },
    "heuristic_matcher": {
        "tasks": "R", "workspaces": "R", "raw_events": "R",
        "semantic_events": "R", "obligations": "R", "evidence": "R",
        "representations": "R", "heuristic_rules": "R",
        "activation_packets": "R/W", "truth_vault": "—",
        "manifests": "R", "audit_verdicts": "—",
        "dg_nodes": "R", "dg_edges": "R",
    },
    "verifier": {
        "tasks": "R", "workspaces": "R", "raw_events": "R",
        "semantic_events": "R", "obligations": "R", "evidence": "R/W",
        "representations": "R", "heuristic_rules": "—",
        "activation_packets": "—", "truth_vault": "—",
        "manifests": "—", "audit_verdicts": "—",
        "dg_nodes": "R", "dg_edges": "R",
    },
    "auditor": {
        "tasks": "R", "workspaces": "R", "raw_events": "R",
        "semantic_events": "R", "obligations": "R", "evidence": "R",
        "representations": "R", "heuristic_rules": "R",
        "activation_packets": "R", "truth_vault": "R",
        "manifests": "R", "audit_verdicts": "R/W",
        "dg_nodes": "R", "dg_edges": "R",
    },
    "orchestrator": {
        "tasks": "R", "workspaces": "R", "raw_events": "R",
        "semantic_events": "R", "obligations": "R", "evidence": "R",
        "representations": "R", "heuristic_rules": "R",
        "activation_packets": "R", "truth_vault": "—",
        "manifests": "R/W", "audit_verdicts": "R",
        "dg_nodes": "R", "dg_edges": "R",
    },
}


class VisibilityLabelChecker:
    """
    visibility label检查——123号§607落实。

    P4-4.6：角色边界落实为collection、visibility label和能力令牌。
    P4-4.COMP：Truth Vault对Solver/HeuristicMatcher不可见。
    """

    def __init__(self):
        self.matrix = VISIBILITY_MATRIX

    def check_access(
        self, role: str, collection: str, access_type: str = "R"
    ) -> Dict[str, Any]:
        """
        检查角色对collection的访问权限。

        Args:
            role: 角色名（8种之一）
            collection: collection名（14种之一）
            access_type: "R"（读）或 "W"（写）

        Returns:
            检查结果
        """
        if role not in self.matrix:
            return {"allowed": False, "reason": f"未知角色: {role}"}

        role_perms = self.matrix[role]
        if collection not in role_perms:
            return {"allowed": False, "reason": f"未知collection: {collection}"}

        perm = role_perms[collection]
        allowed = False
        if access_type == "R":
            allowed = perm in ["R", "R/W", "R(限定)"]
        elif access_type == "W":
            allowed = perm == "R/W"

        return {
            "allowed": allowed,
            "role": role,
            "collection": collection,
            "access_type": access_type,
            "permission": perm,
        }

    def verify_truth_vault_isolation(self) -> Dict[str, Any]:
        """
        P4-4.COMP：Truth Vault对Solver/HeuristicMatcher不可见。

        127号§10.1：truth_vault仅auditor可读。
        """
        violations = []
        for role in ["solver", "heuristic_matcher", "event_capture",
                      "state_reducer", "retriever", "verifier", "orchestrator"]:
            check = self.check_access(role, "truth_vault", "R")
            if check["allowed"]:
                violations.append({
                    "role": role,
                    "collection": "truth_vault",
                    "permission": check["permission"],
                })

        return {
            "isolation_verified": len(violations) == 0,
            "violations": violations,
            "auditor_can_read": self.check_access("auditor", "truth_vault", "R")["allowed"],
        }

    def verify_auditor_visibility(self) -> Dict[str, Any]:
        """
        验证Auditor的可见性矩阵——127号§10.3。

        Auditor应可见全部14个collection（R），可写audit_verdicts。
        truth_vault仅auditor可读。
        """
        auditor_perms = self.matrix.get("auditor", {})
        readable = [c for c, p in auditor_perms.items() if p in ["R", "R/W", "R(限定)"]]
        writable = [c for c, p in auditor_perms.items() if p == "R/W"]

        return {
            "readable_collections": readable,
            "writable_collections": writable,
            "n_readable": len(readable),
            "n_writable": len(writable),
            "truth_vault_readable": "truth_vault" in readable,
            "audit_verdicts_writable": "audit_verdicts" in writable,
        }

    def get_role_collections(self, role: str) -> Dict[str, str]:
        """获取角色的完整可见性矩阵"""
        return self.matrix.get(role, {})
