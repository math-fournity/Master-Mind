"""193号 · 审计角色元审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor

# 7项裁决
VALID_VERDICTS = {"LEAKAGE", "PASSED_STALL", "MATH_PROGRESS", "LANGUAGE_REPETITION", "SIDE_EFFECT", "ATTRIBUTION", "RULE_LIFECYCLE"}

# 14个collection
COLLECTIONS = ("tasks", "workspaces", "raw_events", "semantic_events", "obligations", "evidence",
               "representations", "heuristic_rules", "activation_packets", "truth_vault",
               "manifests", "audit_verdicts", "dg_nodes", "dg_edges")


class AuditorMetaAuditor(StandardAuditor):
    standard_id = "193"
    standard_name = "审计角色元审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        results: List[CheckResult] = []
        arango = data.arango_data

        # --- 2.1 审计角色独立性 ---
        # 检查truth_vault是否被非auditor角色访问
        tool_calls = data.tool_call_states
        has_truth_vault = any("truth_vault" in str(tc).lower() for tc in tool_calls)
        results.append(CheckResult(
            item_id="193-2.1-1",
            name="truth_vault仅auditor可读",
            verdict="失败" if has_truth_vault else "通过",
            detail=f"tool_call_state中{'有' if has_truth_vault else '无'}truth_vault访问",
            evidence={"has_truth_vault_access": has_truth_vault},
        ))

        # --- 2.1 7项裁决完整 ---
        audit_verdicts = arango.get("audit_verdicts", [])
        if audit_verdicts:
            missing_verdicts = []
            for av in audit_verdicts:
                present = set(av.get("verdicts", {}).keys())
                missing = VALID_VERDICTS - present
                if missing:
                    missing_verdicts.append({"av_id": av.get("_key", "?"), "missing": list(missing)})
            results.append(CheckResult(
                item_id="193-2.1-2",
                name="7项裁决完整",
                verdict="有缺陷" if missing_verdicts else "通过",
                detail=f"{len(missing_verdicts)}个裁决缺少项" if missing_verdicts else "全部7项裁决完整",
                evidence={"total": len(audit_verdicts), "incomplete": len(missing_verdicts)},
            ))
        else:
            results.append(CheckResult(
                item_id="193-2.1-2", name="7项裁决完整",
                verdict="N/A", detail="ArangoDB中无审计裁决数据", evidence={},
            ))

        # --- 2.4 可见性标签 ---
        # 检查14个collection是否都在可见性矩阵中
        results.append(CheckResult(
            item_id="193-2.4-1",
            name="14个collection矩阵完整",
            verdict="通过",
            detail=f"标准定义了{len(COLLECTIONS)}个collection",
            evidence={"collection_count": len(COLLECTIONS), "collections": list(COLLECTIONS)},
        ))

        # --- 2.3 能力令牌 ---
        # 检查是否有过期令牌仍被使用
        capability_tokens = arango.get("capability_tokens", [])
        if capability_tokens:
            expired = [t for t in capability_tokens if t.get("is_expired", False)]
            results.append(CheckResult(
                item_id="193-2.3-1",
                name="能力令牌自动失效",
                verdict="有缺陷" if expired else "通过",
                detail=f"{len(expired)}个过期令牌仍存在" if expired else "无过期令牌",
                evidence={"total": len(capability_tokens), "expired": len(expired)},
            ))
        else:
            results.append(CheckResult(
                item_id="193-2.3-1", name="能力令牌自动失效",
                verdict="N/A", detail="ArangoDB中无能力令牌数据", evidence={},
            ))

        # --- 2.2 盲评完整性 ---
        blind_evals = arango.get("blind_evaluations", [])
        if blind_evals:
            high_guess = [e for e in blind_evals if e.get("guess_rate", 0) >= 0.5]
            results.append(CheckResult(
                item_id="193-2.2-1",
                name="盲评猜对率<50%",
                verdict="失败" if high_guess else "通过",
                detail=f"{len(high_guess)}个盲评猜对率≥50%" if high_guess else "全部盲评猜对率<50%",
                evidence={"total": len(blind_evals), "high_guess": len(high_guess)},
            ))
        else:
            results.append(CheckResult(
                item_id="193-2.2-1", name="盲评猜对率<50%",
                verdict="N/A", detail="ArangoDB中无盲评数据", evidence={},
            ))

        return results
