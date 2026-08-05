"""
证据状态模型和冲突状态

对应132号P2-5。

123号§31定义：
- 证据条目至少是(claim_id, kind, polarity, scope, assumptions, artifact_hash, verifier, verifier_version, status)
- kind：6种枚举（literature/numerical/symbolic/formal_proof/counterexample/human_audit）
- polarity：support/refute
- 派生认识状态：no_decisive/support_only/refute_only/mixed

冻结声明：
- 首版不宣称已有数学意义上的"证据格"（P2-5.COMP5）
- 证据集合不把数值支持与形式证明排成伪造的总序（P2-5.COMP）
- 冲突不自动爆炸到整个知识库，生成范围/前提澄清义务（P2-5.COMP3）
- 只有满足该命题类型预先指定的验证门，命题才进入V_t（P2-5.COMP4）

边界情况：
- 同一命题有支持也有反驳证据（mixed状态）
- 证据scope/assumptions冲突
- 证据artifact_hash缺失
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from arango import ArangoClient

DB_NAME = "xishujuzhen_math"
DB_USER = "root"
DB_PASS = "REDACTED-DB-PASSWORD"
ARANGO_HOST = "http://localhost:8529"


class EvidenceKind(str, Enum):
    """
    123号§31定义的6种证据类型。
    """
    LITERATURE = "literature"             # 文献
    NUMERICAL = "numerical"               # 数值
    SYMBOLIC = "symbolic"                 # 符号
    FORMAL_PROOF = "formal_proof"         # 形式证明
    COUNTEREXAMPLE = "counterexample"     # 反例
    HUMAN_AUDIT = "human_audit"           # 人工审计


class EvidencePolarity(str, Enum):
    """
    123号§31定义的极性。
    """
    SUPPORT = "support"       # 支持
    REFUTE = "refute"         # 反驳


class EvidenceStatus(str, Enum):
    """
    证据状态（127号§6权威定义）。
    """
    PENDING = "pending"           # 待验证
    ACTIVE = "active"             # 活跃——已验证且当前有效
    SUPERSEDED = "superseded"     # 被更好的证据替代
    RETRACTED = "retracted"       # 撤回


class DerivedEpistemicState(str, Enum):
    """
    123号§31定义的派生认识状态。
    """
    NO_DECISIVE = "no_decisive"       # 无决定性证据
    SUPPORT_ONLY = "support_only"     # 仅支持
    REFUTE_ONLY = "refute_only"       # 仅反驳
    MIXED = "mixed"                   # 支持与反驳并存


@dataclass
class Evidence:
    """
    证据条目（123号§31 + 127号§6权威定义）。

    127号§6的12个字段：evidence_id/claim_id/kind/polarity/status/scope/
    assumptions/artifact_hash/source_event/verifier/verifier_version/confidence/conflicts
    """
    evidence_id: str
    claim_id: str                              # 关联的命题ID
    kind: EvidenceKind                         # 证据类型
    polarity: EvidencePolarity                 # 极性
    status: EvidenceStatus = EvidenceStatus.PENDING
    scope: str = ""                            # 证据在哪些前提和参数范围有效
    assumptions: List[str] = field(default_factory=list)  # 假设
    artifact_hash: str = ""                    # 可重放工具产物或来源的内容哈希
    source_event: str = ""                     # 来源事件ID（127号§6）
    verifier: str = ""                         # 验证者
    verifier_version: str = ""                 # 验证者版本
    confidence: float = 0.0                    # 置信度[0,1]（127号§6）
    conflicts: List[str] = field(default_factory=list)  # 冲突证据ID列表（127号§6）
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "evidence_id": self.evidence_id,
            "claim_id": self.claim_id,
            "kind": self.kind.value,
            "polarity": self.polarity.value,
            "status": self.status.value,
            "scope": self.scope,
            "assumptions": self.assumptions,
            "artifact_hash": self.artifact_hash,
            "source_event": self.source_event,
            "verifier": self.verifier,
            "verifier_version": self.verifier_version,
            "confidence": self.confidence,
            "conflicts": self.conflicts,
            "created_at": self.created_at,
        }


class EvidenceStore:
    """
    证据ArangoDB存储 + 派生认识状态计算 + 冲突检测。

    冻结声明：
    - 证据集合不把数值支持与形式证明排成伪造的总序（P2-5.COMP）
    - 冲突不自动爆炸到整个知识库，生成范围/前提澄清义务（P2-5.COMP3）
    - 首版不宣称已有数学意义上的"证据格"（P2-5.COMP5）
    """

    def __init__(
        self,
        db_name: str = DB_NAME,
        username: str = DB_USER,
        password: str = DB_PASS,
        host: str = ARANGO_HOST,
    ):
        client = ArangoClient(hosts=host)
        self.db = client.db(db_name, username=username, password=password)
        self.col = self.db.collection("evidence")

    def insert_evidence(self, ev: Evidence) -> str:
        """插入证据条目。"""
        doc = ev.to_dict()
        doc["_key"] = ev.evidence_id
        result = self.col.insert(doc)
        return result["_key"]

    def get_evidence(self, evidence_id: str) -> Optional[Dict[str, Any]]:
        """读取证据条目。"""
        doc = self.col.get(evidence_id)
        if doc is None:
            return None
        doc.pop("_id", None)
        doc.pop("_rev", None)
        return doc

    def update_status(self, evidence_id: str, status: EvidenceStatus) -> bool:
        """更新证据状态。"""
        doc = self.col.get(evidence_id)
        if doc is None:
            return False
        doc["status"] = status.value
        self.col.replace(doc)
        return True

    def get_evidence_for_claim(self, claim_id: str) -> List[Dict[str, Any]]:
        """获取一个命题的所有证据。"""
        aql = "FOR e IN evidence FILTER e.claim_id == @claim_id RETURN e"
        cursor = self.db.aql.execute(aql, bind_vars={"claim_id": claim_id})
        results = []
        for doc in cursor:
            doc.pop("_id", None)
            doc.pop("_rev", None)
            results.append(doc)
        return results

    def compute_derived_state(self, claim_id: str) -> Dict[str, Any]:
        """
        计算派生认识状态（123号§31）。

        至少区分：
        - no_decisive：无决定性证据
        - support_only：仅支持
        - refute_only：仅反驳
        - mixed：支持与反驳并存

        证据集合不把数值支持与形式证明排成伪造的总序（P2-5.COMP）。
        只统计polarity，不对kind排序。
        """
        evidence_list = self.get_evidence_for_claim(claim_id)

        # 只考虑status=verified或pending的证据（withdrawn的不算）
        active = [e for e in evidence_list if e["status"] in (
            EvidenceStatus.ACTIVE.value,
            EvidenceStatus.PENDING.value,
        )]

        support_count = sum(1 for e in active if e["polarity"] == EvidencePolarity.SUPPORT.value)
        refute_count = sum(1 for e in active if e["polarity"] == EvidencePolarity.REFUTE.value)

        if support_count == 0 and refute_count == 0:
            state = DerivedEpistemicState.NO_DECISIVE
        elif support_count > 0 and refute_count == 0:
            state = DerivedEpistemicState.SUPPORT_ONLY
        elif support_count == 0 and refute_count > 0:
            state = DerivedEpistemicState.REFUTE_ONLY
        else:
            state = DerivedEpistemicState.MIXED

        return {
            "claim_id": claim_id,
            "derived_state": state.value,
            "support_count": support_count,
            "refute_count": refute_count,
            "total_active": len(active),
            # P2-5.COMP: 不对kind排序，只按polarity统计
            "support_kinds": list(set(e["kind"] for e in active if e["polarity"] == EvidencePolarity.SUPPORT.value)),
            "refute_kinds": list(set(e["kind"] for e in active if e["polarity"] == EvidencePolarity.REFUTE.value)),
        }

    def detect_conflicts(self, claim_id: str) -> Dict[str, Any]:
        """
        检测冲突（123号§31）。

        冲突不自动爆炸到整个知识库（P2-5.COMP3）。
        冲突生成范围/前提澄清义务。
        """
        state = self.compute_derived_state(claim_id)

        has_conflict = state["derived_state"] == DerivedEpistemicState.MIXED.value

        if not has_conflict:
            return {
                "claim_id": claim_id,
                "has_conflict": False,
                "clarification_obligation_needed": False,
            }

        # 冲突存在——生成范围/前提澄清义务
        evidence_list = self.get_evidence_for_claim(claim_id)
        active = [e for e in evidence_list if e["status"] in (
            EvidenceStatus.ACTIVE.value,
            EvidenceStatus.PENDING.value,
        )]

        support = [e for e in active if e["polarity"] == EvidencePolarity.SUPPORT.value]
        refute = [e for e in active if e["polarity"] == EvidencePolarity.REFUTE.value]

        # 检查scope/assumptions是否冲突
        support_scopes = set(e["scope"] for e in support if e["scope"])
        refute_scopes = set(e["scope"] for e in refute if e["scope"])
        scope_overlap = support_scopes & refute_scopes

        return {
            "claim_id": claim_id,
            "has_conflict": True,
            "clarification_obligation_needed": True,
            # P2-5.COMP3: 冲突不自动爆炸到整个知识库
            "conflict_scope": "claim_only",  # 只影响该命题，不爆炸
            "support_count": len(support),
            "refute_count": len(refute),
            "scope_overlap": list(scope_overlap),
            # 建议生成的澄清义务
            "suggested_obligation": {
                "type": "clarification",
                "description": f"命题{claim_id}存在支持与反驳证据并存，需澄清范围/前提",
                "claim_id": claim_id,
            },
        }

    def check_verification_gate(
        self,
        claim_id: str,
        required_kinds: List[EvidenceKind],
        required_polarity: EvidencePolarity = EvidencePolarity.SUPPORT,
    ) -> Dict[str, Any]:
        """
        检查命题是否满足验证门（P2-5.COMP4）。

        只有满足该命题类型预先指定的验证门，命题才进入V_t。
        """
        evidence_list = self.get_evidence_for_claim(claim_id)
        active = [e for e in evidence_list if e["status"] == EvidenceStatus.ACTIVE.value]

        # 检查是否有required_kinds中的证据
        has_required = any(e["kind"] in [k.value for k in required_kinds] for e in active)
        has_correct_polarity = any(
            e["polarity"] == required_polarity.value for e in active
        )

        gate_passed = has_required and has_correct_polarity

        return {
            "claim_id": claim_id,
            "gate_passed": gate_passed,
            "required_kinds": [k.value for k in required_kinds],
            "required_polarity": required_polarity.value,
            "has_required_kind": has_required,
            "has_correct_polarity": has_correct_polarity,
            "can_enter_v_t": gate_passed,  # P2-5.COMP4
        }
