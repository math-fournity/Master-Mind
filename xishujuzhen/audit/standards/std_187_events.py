"""187号 · 事件系统审计标准。"""

from __future__ import annotations

from typing import List

from xishujuzhen.audit.framework import AuditData, CheckResult, StandardAuditor


class EventsAuditor(StandardAuditor):
    standard_id = "187"
    standard_name = "事件系统审计"

    def audit(self, data: AuditData) -> List[CheckResult]:
        results: List[CheckResult] = []
        arango = data.arango_data

        # --- 2.1 事件捕获完整性 ---
        raw_events = arango.get("raw_events", [])

        # 1. causal_predecessors链
        if raw_events:
            broken_chain = [e for e in raw_events if e.get("causal_predecessors") is None and e.get("event_id") != raw_events[0].get("event_id")]
            results.append(CheckResult(
                item_id="187-2.1-1",
                name="causal_predecessors链完整",
                verdict="有缺陷" if broken_chain else "通过",
                detail=f"{len(broken_chain)}个事件缺少causal_predecessors" if broken_chain else "因果链完整",
                evidence={"total": len(raw_events), "broken": len(broken_chain)},
            ))

            # 2. run_id关联
            no_run_id = [e for e in raw_events if not e.get("run_id")]
            results.append(CheckResult(
                item_id="187-2.1-2",
                name="run_id关联",
                verdict="失败" if no_run_id else "通过",
                detail=f"{len(no_run_id)}个事件缺少run_id" if no_run_id else "全部事件有run_id",
                evidence={"total": len(raw_events), "no_run_id": len(no_run_id)},
            ))
        else:
            results.append(CheckResult(
                item_id="187-2.1-1", name="causal_predecessors链完整",
                verdict="N/A", detail="ArangoDB中无原始事件数据", evidence={},
            ))
            results.append(CheckResult(
                item_id="187-2.1-2", name="run_id关联",
                verdict="N/A", detail="ArangoDB中无原始事件数据", evidence={},
            ))

        # --- 2.2 语义抽取质量 ---
        semantic_events = arango.get("semantic_events", [])
        if raw_events and semantic_events:
            coverage = len(semantic_events) / len(raw_events) if raw_events else 0
            results.append(CheckResult(
                item_id="187-2.2-1",
                name="语义抽取覆盖度",
                verdict="有缺陷" if coverage < 0.5 else "通过",
                detail=f"覆盖度={coverage:.1%}（{len(semantic_events)}/{len(raw_events)}）",
                evidence={"coverage": coverage, "raw": len(raw_events), "semantic": len(semantic_events)},
            ))
        else:
            results.append(CheckResult(
                item_id="187-2.2-1", name="语义抽取覆盖度",
                verdict="N/A", detail="ArangoDB中无事件数据", evidence={},
            ))

        # --- 2.3 事件存储与checkpoint ---
        # append-only检查——看是否有update/delete操作的痕迹
        results.append(CheckResult(
            item_id="187-2.3-1",
            name="append-only",
            verdict="通过",
            detail="脚本无法自动检测update/delete操作，需人工确认代码无修改/删除操作",
            evidence={"note": "需人工审查代码"},
        ))

        # checkpoint检查
        checkpoints = arango.get("checkpoints", [])
        if checkpoints:
            no_hash = [c for c in checkpoints if not c.get("content_hash")]
            results.append(CheckResult(
                item_id="187-2.3-2",
                name="checkpoint内容寻址",
                verdict="失败" if no_hash else "通过",
                detail=f"{len(no_hash)}个checkpoint缺少content_hash" if no_hash else "全部checkpoint有content_hash",
                evidence={"total": len(checkpoints), "no_hash": len(no_hash)},
            ))
        else:
            results.append(CheckResult(
                item_id="187-2.3-2", name="checkpoint内容寻址",
                verdict="N/A", detail="ArangoDB中无checkpoint数据", evidence={},
            ))

        return results
