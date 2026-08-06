"""189号 · 启发匹配审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor


class HeuristicsAuditor(StandardAuditor):
    standard_id = "189"
    standard_name = "启发匹配审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        results: List[CheckResult] = []
        arango = data.arango_data

        # --- 2.2 规则生命周期管理 ---
        rules = arango.get("heuristic_rules", [])
        if rules:
            # 1. candidate规则不在线使用
            candidate_rules = [r for r in rules if r.get("status") == "candidate"]
            used_online = [r for r in candidate_rules if r.get("used_online", False)]
            results.append(CheckResult(
                item_id="189-2.2-1",
                name="candidate规则禁止在线提示",
                verdict="失败" if used_online else "通过",
                detail=f"{len(candidate_rules)}个candidate规则，{len(used_online)}个被在线使用" if candidate_rules else "无candidate规则",
                evidence={"candidate_count": len(candidate_rules), "used_online": len(used_online)},
            ))

            # 2. 字段完整性
            incomplete = []
            for r in rules:
                if r.get("status") in ("validated", "published"):
                    missing = []
                    for field in ("applicable_domains", "model_versions", "failure_cases", "effect_evidence"):
                        if not r.get(field):
                            missing.append(field)
                    if missing:
                        incomplete.append({"rule_id": r.get("rule_id", "?"), "missing": missing})
            results.append(CheckResult(
                item_id="189-2.2-2",
                name="validated/published规则字段完整",
                verdict="有缺陷" if incomplete else "通过",
                detail=f"{len(incomplete)}个规则字段不完整" if incomplete else "全部规则字段完整",
                evidence={"incomplete_count": len(incomplete), "incomplete_rules": incomplete[:5]},
            ))

            # 3. 状态转移条件
            published = [r for r in rules if r.get("status") == "published"]
            missing_evidence = [r for r in published if not r.get("effect_evidence")]
            results.append(CheckResult(
                item_id="189-2.2-3",
                name="published规则有效果证据",
                verdict="有缺陷" if missing_evidence else "通过",
                detail=f"{len(published)}个published规则，{len(missing_evidence)}个缺效果证据" if published else "无published规则",
                evidence={"published_count": len(published), "missing_evidence": len(missing_evidence)},
            ))
        else:
            for i, name in enumerate(["candidate规则禁止在线提示", "validated/published规则字段完整", "published规则有效果证据"], 1):
                results.append(CheckResult(
                    item_id=f"189-2.2-{i}", name=name,
                    verdict="N/A", detail="ArangoDB中无规则数据", evidence={},
                ))

        # --- 2.3 答案泄漏审计 ---
        leakage_audits = arango.get("leakage_audits", [])
        if leakage_audits:
            # 检查四门是否全执行
            four_door = [a for a in leakage_audits if all(
                a.get(door) is not None for door in ("literal", "equivalence", "candidate_space", "blind_recovery")
            )]
            results.append(CheckResult(
                item_id="189-2.3-1",
                name="四门全执行",
                verdict="失败" if len(four_door) < len(leakage_audits) else "通过",
                detail=f"{len(four_door)}/{len(leakage_audits)}个审计执行了全部四门",
                evidence={"total": len(leakage_audits), "four_door": len(four_door)},
            ))

            # 检查阈值
            over_threshold = [a for a in leakage_audits if any(
                a.get(door, {}).get("score", 0) > a.get(door, {}).get("threshold", 1.0)
                for door in ("literal", "equivalence", "candidate_space", "blind_recovery")
            )]
            results.append(CheckResult(
                item_id="189-2.3-2",
                name="泄漏代理分数低于阈值",
                verdict="失败" if over_threshold else "通过",
                detail=f"{len(over_threshold)}个审计有门超阈值" if over_threshold else "全部低于阈值",
                evidence={"over_threshold_count": len(over_threshold)},
            ))
        else:
            results.append(CheckResult(
                item_id="189-2.3-1", name="四门全执行",
                verdict="N/A", detail="ArangoDB中无泄漏审计数据", evidence={},
            ))
            results.append(CheckResult(
                item_id="189-2.3-2", name="泄漏代理分数低于阈值",
                verdict="N/A", detail="ArangoDB中无泄漏审计数据", evidence={},
            ))

        # --- 2.1 规则匹配正确性（从tool_call_states检查有无truth_vault访问） ---
        tool_calls = data.tool_call_states
        has_truth_vault = any("truth_vault" in str(tc).lower() for tc in tool_calls)
        results.append(CheckResult(
            item_id="189-2.1-1",
            name="matcher不可见truth_vault",
            verdict="失败" if has_truth_vault else "通过",
            detail=f"tool_call_state中{'有' if has_truth_vault else '无'}truth_vault访问",
            evidence={"has_truth_vault_access": has_truth_vault},
        ))

        return results
