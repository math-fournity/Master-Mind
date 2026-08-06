"""191号 · 上下文编译审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor

REQUIRED_FIELDS = ("source", "visibility", "evidence_level", "token_cost", "pruning_record")
PRELOAD_KEYWORDS = ["完整解法", "complete_solution", "最终答案", "final_answer", "ground_truth", "truth_vault", "完整证明路径", "complete_proof_path"]


class ContextCompilerAuditor(StandardAuditor):
    standard_id = "191"
    standard_name = "上下文编译审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        results: List[CheckResult] = []
        arango = data.arango_data

        # --- 2.2 最小性审计 ---
        # 检查response中是否有预载关键词
        final_response = data.guided_loop_result.get("final_response", "")
        has_preload = any(kw in final_response for kw in PRELOAD_KEYWORDS)
        results.append(CheckResult(
            item_id="191-2.2-1",
            name="无预载答案路线",
            verdict="失败" if has_preload else "通过",
            detail=f"response中{'包含' if has_preload else '不包含'}预载关键词",
            evidence={"has_preload": has_preload},
        ))

        # --- 2.4 状态快照 ---
        workspaces = arango.get("workspaces", [])
        if workspaces:
            # 检查8字段完整性
            snapshot_fields = ("q0", "accepted_propositions", "open_goals", "current_representation",
                             "recent_key_path", "rejected_routes_summary", "tool_evidence", "current_hint")
            incomplete = []
            for w in workspaces:
                ws_data = w.get("state_snapshot", w)
                missing = [f for f in snapshot_fields if f not in ws_data]
                if missing:
                    incomplete.append({"ws_id": w.get("_key", "?"), "missing": missing})
            results.append(CheckResult(
                item_id="191-2.4-1",
                name="状态快照8字段完整",
                verdict="有缺陷" if incomplete else "通过",
                detail=f"{len(incomplete)}个快照字段不完整" if incomplete else "全部快照8字段完整",
                evidence={"total": len(workspaces), "incomplete": len(incomplete)},
            ))
        else:
            results.append(CheckResult(
                item_id="191-2.4-1", name="状态快照8字段完整",
                verdict="N/A", detail="ArangoDB中无workspace数据", evidence={},
            ))

        # --- 2.1 上下文编译质量 ---
        # 5项记录检查——需要ArangoDB中的context_segments数据
        context_segments = arango.get("context_segments", [])
        if context_segments:
            missing_records = []
            for seg in context_segments:
                missing = [f for f in REQUIRED_FIELDS if f not in seg]
                if missing:
                    missing_records.append({"seg_id": seg.get("_key", "?"), "missing": missing})
            results.append(CheckResult(
                item_id="191-2.1-1",
                name="5项记录完整",
                verdict="有缺陷" if missing_records else "通过",
                detail=f"{len(missing_records)}个段缺少记录字段" if missing_records else "全部段5项记录完整",
                evidence={"total": len(context_segments), "missing_records": len(missing_records)},
            ))
        else:
            results.append(CheckResult(
                item_id="191-2.1-1", name="5项记录完整",
                verdict="N/A", detail="ArangoDB中无context_segments数据", evidence={},
            ))

        # --- 2.3 裁剪记录 ---
        pruning_logs = arango.get("pruning_logs", [])
        if pruning_logs:
            no_reason = [p for p in pruning_logs if not p.get("reason")]
            results.append(CheckResult(
                item_id="191-2.3-1",
                name="裁剪原因明确",
                verdict="失败" if no_reason else "通过",
                detail=f"{len(no_reason)}条裁剪记录缺少原因" if no_reason else "全部裁剪记录有原因",
                evidence={"total": len(pruning_logs), "no_reason": len(no_reason)},
            ))
        else:
            results.append(CheckResult(
                item_id="191-2.3-1", name="裁剪原因明确",
                verdict="N/A", detail="ArangoDB中无裁剪记录", evidence={},
            ))

        return results
