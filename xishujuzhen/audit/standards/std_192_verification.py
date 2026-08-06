"""192号 · 验证审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor

VALID_STATES = {"proven", "formally_verified", "computationally_supported", "numerically_tested", "contradicted", "unknown"}


class VerificationAuditor(StandardAuditor):
    standard_id = "192"
    standard_name = "验证审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        results: List[CheckResult] = []
        arango = data.arango_data

        # --- 2.1 验证状态正确性 ---
        verification_results = arango.get("verification_results", [])
        if verification_results:
            # 1. 6种状态
            invalid_states = [v for v in verification_results if v.get("output") not in VALID_STATES]
            results.append(CheckResult(
                item_id="192-2.1-1",
                name="6种验证状态",
                verdict="失败" if invalid_states else "通过",
                detail=f"{len(invalid_states)}个结果状态不在6种之内" if invalid_states else "全部状态合法",
                evidence={"total": len(verification_results), "invalid": len(invalid_states)},
            ))

            # 2. 不决定研究方向——检查output中是否包含"下一步应该"等
            decides_direction = [v for v in verification_results if any(
                kw in str(v.get("output", "")) for kw in ["下一步应该", "应该继续", "next_step"]
            )]
            results.append(CheckResult(
                item_id="192-2.1-2",
                name="不决定研究方向",
                verdict="失败" if decides_direction else "通过",
                detail=f"{len(decides_direction)}个结果决定了研究方向" if decides_direction else "未决定研究方向",
                evidence={"decides_direction_count": len(decides_direction)},
            ))

            # 3. 反驳优先
            has_refute = [v for v in verification_results if v.get("output") == "contradicted"]
            has_refute_evidence = any(
                v.get("output") != "contradicted" and any(
                    e.get("polarity") == "refute" for e in v.get("evidence_refs", [])
                )
                for v in verification_results
            )
            results.append(CheckResult(
                item_id="192-2.1-3",
                name="反驳优先",
                verdict="有缺陷" if has_refute_evidence else "通过",
                detail=f"有反驳证据但未返回contradicted" if has_refute_evidence else "反驳优先正确",
                evidence={"contradicted_count": len(has_refute), "missed_refute": has_refute_evidence},
            ))
        else:
            for i, name in enumerate(["6种验证状态", "不决定研究方向", "反驳优先"], 1):
                results.append(CheckResult(
                    item_id=f"192-2.1-{i}", name=name,
                    verdict="N/A", detail="ArangoDB中无验证结果数据", evidence={},
                ))

        # --- 2.2 卡点检测准确性 ---
        stall_detections = arango.get("stall_detections", [])
        if stall_detections:
            valid_types = {"necessary_exploration", "semantic_repetition", "contradiction_unhandled",
                          "tool_blockage", "representation_mismatch", "strategy_exhausted", "budget_exhausted"}
            invalid_types = [s for s in stall_detections if s.get("stall_type") not in valid_types]
            results.append(CheckResult(
                item_id="192-2.2-1",
                name="7种卡点类型",
                verdict="失败" if invalid_types else "通过",
                detail=f"{len(invalid_types)}个卡点类型不在7种之内" if invalid_types else "全部类型合法",
                evidence={"total": len(stall_detections), "invalid": len(invalid_types)},
            ))

            # 必要探索不应提示
            necessary = [s for s in stall_detections if s.get("stall_type") == "necessary_exploration"]
            hinted = [s for s in necessary if s.get("action") == "inject_hint"]
            results.append(CheckResult(
                item_id="192-2.2-2",
                name="必要探索不提示",
                verdict="失败" if hinted else "通过",
                detail=f"{len(necessary)}个必要探索，{len(hinted)}个被提示" if necessary else "无必要探索",
                evidence={"necessary_count": len(necessary), "hinted": len(hinted)},
            ))
        else:
            results.append(CheckResult(
                item_id="192-2.2-1", name="7种卡点类型",
                verdict="N/A", detail="ArangoDB中无卡点检测数据", evidence={},
            ))
            results.append(CheckResult(
                item_id="192-2.2-2", name="必要探索不提示",
                verdict="N/A", detail="ArangoDB中无卡点检测数据", evidence={},
            ))

        return results
