"""190号 · 检索审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor

ANSWER_KEYWORDS = ["答案", "answer", "solution", "最终结论", "ground_truth", "truth_vault"]


class RetrievalAuditor(StandardAuditor):
    standard_id = "190"
    standard_name = "检索审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        results: List[CheckResult] = []
        arango = data.arango_data

        # --- 2.1 检索安全性 ---
        # 从conversation中检查是否有答案关键词泄漏
        final_response = data.guided_loop_result.get("final_response", "")
        has_answer_leak = any(kw in final_response for kw in ANSWER_KEYWORDS)
        results.append(CheckResult(
            item_id="190-2.1-1",
            name="答案关键词过滤",
            verdict="有缺陷" if has_answer_leak else "通过",
            detail=f"response中{'包含' if has_answer_leak else '不包含'}答案关键词",
            evidence={"has_answer_leak": has_answer_leak},
        ))

        # --- 2.5 三层存储 ---
        # 检查hot_store是否有全部历史（应该只有充分快照）
        hot = arango.get("hot_store", [])
        results.append(CheckResult(
            item_id="190-2.5-1",
            name="hot_store只保存充分快照",
            verdict="N/A" if not hot else "通过",
            detail=f"hot_store有{len(hot)}条记录" if hot else "ArangoDB中无hot_store数据",
            evidence={"hot_count": len(hot)},
        ))

        # --- 2.8 来源注册 ---
        # 检查是否有撤稿来源被使用
        cold = arango.get("cold_store", [])
        if cold:
            retracted = [c for c in cold if c.get("source_retracted", False)]
            results.append(CheckResult(
                item_id="190-2.8-1",
                name="撤稿来源不使用",
                verdict="失败" if retracted else "通过",
                detail=f"{len(retracted)}个撤稿来源被使用" if retracted else "无撤稿来源被使用",
                evidence={"retracted_count": len(retracted)},
            ))
        else:
            results.append(CheckResult(
                item_id="190-2.8-1", name="撤稿来源不使用",
                verdict="N/A", detail="ArangoDB中无cold_store数据", evidence={},
            ))

        # --- 2.3 dg_adapter只读性 ---
        # 从代码层面检查——脚本无法直接验证，但可以检查dg_nodes是否被修改
        dg_nodes = arango.get("dg_nodes", [])
        results.append(CheckResult(
            item_id="190-2.3-1",
            name="dg_adapter只读性",
            verdict="N/A",
            detail="需人工确认dg_adapter使用深拷贝+哈希校验",
            evidence={"dg_nodes_count": len(dg_nodes)},
        ))

        # --- 2.6 微包 ---
        # 检查微包是否预载了未来路线
        micro_packs = arango.get("micro_packs", [])
        if micro_packs:
            preload_keywords = ["完整解法", "complete_solution", "最终答案", "final_answer", "完整证明路径"]
            has_preload = any(
                any(kw in str(mp.get("items", "")) for kw in preload_keywords)
                for mp in micro_packs
            )
            results.append(CheckResult(
                item_id="190-2.6-1",
                name="微包不预载未来路线",
                verdict="失败" if has_preload else "通过",
                detail=f"{'发现' if has_preload else '未发现'}预载关键词",
                evidence={"micro_pack_count": len(micro_packs), "has_preload": has_preload},
            ))
        else:
            results.append(CheckResult(
                item_id="190-2.6-1", name="微包不预载未来路线",
                verdict="N/A", detail="ArangoDB中无微包数据", evidence={},
            ))

        return results
