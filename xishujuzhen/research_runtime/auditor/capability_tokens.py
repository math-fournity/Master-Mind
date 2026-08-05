"""
CapabilityToken：能力令牌——127号§10.6

对应134号P4-4.6 + 123号§607。

127号§10.6 CapabilityToken schema（8字段）：
- token_id, role, granted_collections, write_collections,
  granted_fields, expires_at, issued_by, run_id

强制机制（127号§10.6）：
1. collection级访问控制
2. 字段级访问控制
3. 写入控制
4. 运行隔离（token绑定run_id）
5. 自动失效
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Set
from datetime import datetime, timezone


@dataclass
class CapabilityToken:
    """
    127号§10.6 CapabilityToken schema——8字段。

    123号§607：角色边界必须落实为能力令牌，而不是只写在prompt里。
    """
    token_id: str                           # 唯一标识
    role: str                               # 角色名（8种之一）
    granted_collections: List[str]          # 可读collection列表
    write_collections: List[str]            # 可写collection列表
    granted_fields: Dict[str, List[str]] = field(default_factory=dict)  # 字段级权限
    expires_at: str = ""                    # 过期时间
    issued_by: str = "orchestrator"         # 签发者
    run_id: str = ""                        # 运行ID（运行隔离）

    def to_dict(self) -> dict:
        return {
            "token_id": self.token_id,
            "role": self.role,
            "granted_collections": self.granted_collections,
            "write_collections": self.write_collections,
            "granted_fields": self.granted_fields,
            "expires_at": self.expires_at,
            "issued_by": self.issued_by,
            "run_id": self.run_id,
        }

    def is_expired(self) -> bool:
        """检查token是否过期——127号§10.6强制机制5：自动失效"""
        if not self.expires_at:
            return False
        now = datetime.now(timezone.utc).isoformat()
        return now > self.expires_at

    def can_read(self, collection: str) -> bool:
        """127号§10.6强制机制1：collection级访问控制"""
        if self.is_expired():
            return False
        return collection in self.granted_collections

    def can_write(self, collection: str) -> bool:
        """127号§10.6强制机制3：写入控制"""
        if self.is_expired():
            return False
        return collection in self.write_collections

    def can_read_field(self, collection: str, field_name: str) -> bool:
        """127号§10.6强制机制2：字段级访问控制"""
        if not self.can_read(collection):
            return False
        if collection not in self.granted_fields:
            return True  # 无字段级限制→全部可读
        return field_name in self.granted_fields[collection]

    def is_same_run(self, run_id: str) -> bool:
        """127号§10.6强制机制4：运行隔离"""
        return self.run_id == run_id


class CapabilityTokenVerifier:
    """
    能力令牌验证器——运行时强制CapabilityToken检查。

    123号§607：角色边界必须落实为能力令牌，而不是只写在prompt里。
    """

    def __init__(self):
        self._tokens: Dict[str, CapabilityToken] = {}

    def issue_token(
        self,
        role: str,
        granted_collections: List[str],
        write_collections: List[str],
        run_id: str,
        granted_fields: Optional[Dict[str, List[str]]] = None,
        expires_at: str = "",
    ) -> CapabilityToken:
        """签发CapabilityToken"""
        import hashlib
        token_id = hashlib.sha256(
            f"{role}:{run_id}:{datetime.now(timezone.utc).isoformat()}".encode()
        ).hexdigest()[:16]

        token = CapabilityToken(
            token_id=token_id,
            role=role,
            granted_collections=granted_collections,
            write_collections=write_collections,
            granted_fields=granted_fields or {},
            expires_at=expires_at,
            run_id=run_id,
        )
        self._tokens[token_id] = token
        return token

    def issue_auditor_token(self, run_id: str = "phase4") -> CapabilityToken:
        """
        签发Auditor的CapabilityToken——127号§10.3+§10.6。

        Auditor可见14个collection，可写audit_verdicts。
        truth_vault仅auditor可读（granted_fields包含全部字段）。
        """
        return self.issue_token(
            role="auditor",
            granted_collections=[
                "tasks", "workspaces", "raw_events", "semantic_events",
                "obligations", "evidence", "representations", "heuristic_rules",
                "activation_packets", "truth_vault", "manifests",
                "audit_verdicts", "dg_nodes", "dg_edges",
            ],
            write_collections=["audit_verdicts"],
            run_id=run_id,
            granted_fields={
                "truth_vault": ["ground_truth", "answer_equivalent_content", "scoring_rubrics"],
            },
        )

    def verify_access(
        self, token: CapabilityToken, collection: str, access_type: str = "R"
    ) -> Dict[str, Any]:
        """
        验证token对collection的访问权限。

        123号§607：运行时强制检查。
        """
        if token.is_expired():
            return {"allowed": False, "reason": "token已过期"}

        if access_type == "R":
            allowed = token.can_read(collection)
        elif access_type == "W":
            allowed = token.can_write(collection)
        else:
            allowed = False

        return {
            "allowed": allowed,
            "token_id": token.token_id,
            "role": token.role,
            "collection": collection,
            "access_type": access_type,
            "run_isolated": token.run_id,
        }

    def verify_truth_vault_access(
        self, token: CapabilityToken
    ) -> Dict[str, Any]:
        """
        验证truth_vault访问——127号§10.1。

        truth_vault仅auditor可读。其他角色的token不应有truth_vault访问权限。
        """
        if token.role != "auditor":
            return {
                "allowed": False,
                "reason": f"truth_vault仅auditor可读，当前角色={token.role}",
                "r13_guard": True,  # R-13防线
            }

        return {
            "allowed": token.can_read("truth_vault"),
            "role": "auditor",
            "r13_guard": True,
        }
