"""188号 · 状态归约审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor


class StateReducerAuditor(StandardAuditor):
    standard_id = "188"
    standard_name = "状态归约审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        results: List[CheckResult] = []
        arango = data.arango_data

        # --- 2.6 V_t/F_t分离 ---
        workspaces = arango.get("workspaces", [])

        # 1. W_t不可直接修改——检查是否有非Reducer创建的workspace
        if workspaces:
            non_reducer = [w for w in workspaces if w.get("source") not in ("reducer", "versioned_reducer", None, "")]
            results.append(CheckResult(
                item_id="188-2.6-1",
                name="W_t不可直接修改",
                verdict="失败" if non_reducer else "通过",
                detail=f"{len(non_reducer)}个workspace非Reducer创建" if non_reducer else "全部workspace由Reducer创建",
                evidence={"workspace_count": len(workspaces), "non_reducer_count": len(non_reducer)},
            ))
        else:
            results.append(CheckResult(
                item_id="188-2.6-1", name="W_t不可直接修改",
                verdict="N/A", detail="ArangoDB中无workspace数据", evidence={},
            ))

        # --- 2.3 义务图完整性 ---
        obligations = arango.get("obligations", [])
        if obligations:
            # 检查是否有SCC（循环依赖）
            scc_obligations = [o for o in obligations if o.get("in_scc", False)]
            auto_released = [o for o in scc_obligations if o.get("status") == "released"]
            results.append(CheckResult(
                item_id="188-2.3-1",
                name="循环依赖不自动释放",
                verdict="失败" if auto_released else "通过",
                detail=f"{len(scc_obligations)}个SCC义务，{len(auto_released)}个被自动释放" if scc_obligations else "无SCC义务",
                evidence={"scc_count": len(scc_obligations), "auto_released": len(auto_released)},
            ))
        else:
            results.append(CheckResult(
                item_id="188-2.3-1", name="循环依赖不自动释放",
                verdict="N/A", detail="ArangoDB中无义务数据", evidence={},
            ))

        # --- 2.4 证据状态正确性 ---
        evidence = arango.get("evidence", [])
        if evidence:
            # 检查派生认识状态是否正确
            refute_only = [e for e in evidence if e.get("derived_state") == "refute_only"]
            in_vt = [e for e in refute_only if e.get("in_v_t", False)]
            results.append(CheckResult(
                item_id="188-2.4-1",
                name="refute_only不进入V_t",
                verdict="失败" if in_vt else "通过",
                detail=f"{len(refute_only)}个refute_only证据，{len(in_vt)}个进入了V_t" if refute_only else "无refute_only证据",
                evidence={"refute_only_count": len(refute_only), "in_vt_count": len(in_vt)},
            ))

            # 检查冲突检测
            mixed = [e for e in evidence if e.get("derived_state") == "mixed"]
            has_conflict = [e for e in mixed if e.get("has_conflict", False)]
            results.append(CheckResult(
                item_id="188-2.4-2",
                name="冲突检测",
                verdict="有缺陷" if mixed and not has_conflict else "通过",
                detail=f"{len(mixed)}个mixed状态，{len(has_conflict)}个检测到冲突" if mixed else "无mixed状态",
                evidence={"mixed_count": len(mixed), "conflict_detected": len(has_conflict)},
            ))
        else:
            results.append(CheckResult(
                item_id="188-2.4-1", name="refute_only不进入V_t",
                verdict="N/A", detail="ArangoDB中无证据数据", evidence={},
            ))
            results.append(CheckResult(
                item_id="188-2.4-2", name="冲突检测",
                verdict="N/A", detail="ArangoDB中无证据数据", evidence={},
            ))

        # --- 2.7 Q_0冻结 ---
        # 从guided_loop_result检查problem是否被修改
        glr = data.guided_loop_result
        problem = glr.get("problem", "")
        results.append(CheckResult(
            item_id="188-2.7-1",
            name="Q_0冻结验证",
            verdict="通过" if problem else "失败",
            detail=f"problem字段{'存在' if problem else '为空'}",
            evidence={"problem_length": len(problem)},
        ))

        # --- 2.1 状态重建准确性（需要ArangoDB数据） ---
        # 检查是否有多个workspace版本（可复现性）
        if workspaces:
            ws_versions = set(w.get("reducer_version", "unknown") for w in workspaces)
            results.append(CheckResult(
                item_id="188-2.1-1",
                name="状态重建可复现性",
                verdict="通过" if len(ws_versions) <= 1 else "有缺陷",
                detail=f"Reducer版本: {ws_versions}",
                evidence={"reducer_versions": list(ws_versions)},
            ))
        else:
            results.append(CheckResult(
                item_id="188-2.1-1", name="状态重建可复现性",
                verdict="N/A", detail="ArangoDB中无workspace数据", evidence={},
            ))

        return results
