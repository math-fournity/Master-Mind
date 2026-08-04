#!/usr/bin/env python3
"""cognition_sdk_math.py —— 认知图操作SDK（高层API）

封装CognitionVerifier，提供认知单元CRUD、版本链、依赖边、任务记录、
CP4检查清单、拓扑覆盖验证等高层操作。
"""
import sys
import os
from datetime import datetime

from arango import ArangoClient
from cognition_verifier_math import CognitionVerifier


class CognitionSDK:
    """认知图操作SDK"""

    def __init__(self, host="localhost", port=8529, db_name="xishujuzhen_math",
                 username="root", password="REDACTED-DB-PASSWORD"):
        self.client = ArangoClient(hosts=f"http://{host}:{port}")
        self.db = self.client.db(db_name, username=username, password=password)
        self.cv = CognitionVerifier(self.db)

    # ============================================================
    # 查询类
    # ============================================================
    def list_units(self, category=None, status="active"):
        """列出认知单元"""
        if category:
            docs = list(self.db.collection("cognition_units").find({
                "category": category,
                "status": status,
            }))
        else:
            docs = list(self.db.collection("cognition_units").find({"status": status}))
        return docs

    def get_unit(self, cog_id):
        """获取单个认知单元"""
        docs = list(self.db.collection("cognition_units").find({"cog_id": cog_id}))
        return docs[0] if docs else None

    def get_versions(self, cog_id):
        """获取版本链"""
        return self.cv.get_version_chain(cog_id)

    def get_deps(self, cog_id, reverse=False):
        """获取依赖"""
        if reverse:
            return self.cv.get_dependents(cog_id)
        return self.cv.get_dependencies(cog_id)

    def traverse(self, seeds, max_depth=7):
        """图遍历"""
        return self.cv.get_task_cognition(seeds, max_depth=max_depth)

    def verify_cognition_coverage(self, task_cogs, loaded_cog_ids):
        """覆盖验证（集合差集）"""
        return self.cv.verify_cognition_coverage(task_cogs, loaded_cog_ids)

    def get_stats(self):
        """统计"""
        return self.cv.get_cognition_stats()

    def get_stop_checklist(self, cog_id="stop_hook"):
        """获取Stop hook的CP4检查清单（从稀疏矩阵动态查询）

        查询cog_id的depends_on依赖，格式化为检查清单。
        未来加新纪律只需在ArangoDB加一条边，此方法不用改。
        """
        deps = self.get_deps(cog_id)
        checklist = []
        for d in deps:
            unit = self.get_unit(d["cog_id"])
            if unit:
                checklist.append({
                    "cog_id": unit["cog_id"],
                    "title": unit["title"],
                    "key_cognition": unit.get("key_cognition", ""),
                    "source_docs": unit.get("source_docs", []),
                })
        return checklist

    # ============================================================
    # 审计类
    # ============================================================
    def audit_version_chain(self):
        """D3：版本链审计

        每个active认知单元的current_version是否指向版本链最新版本。
        """
        units = self.list_units(status="active")
        total = len(units)
        correct = 0
        errors = []
        for u in units:
            versions = self.get_versions(u["cog_id"])
            if not versions:
                errors.append({"cog_id": u["cog_id"], "error": "无版本记录"})
                continue
            latest = versions[-1]["version"]
            if u.get("current_version") == latest:
                correct += 1
            else:
                errors.append({
                    "cog_id": u["cog_id"],
                    "current": u.get("current_version"),
                    "latest": latest,
                })
        score = 20 if total == 0 else int(20 * correct / total)
        return {"total": total, "correct": correct, "errors": errors, "score": score}

    def audit_graph_completeness(self, seeds, depth_default=7, depth_max=9):
        """D4：图遍历完整性审计

        默认深度是否覆盖更大深度。
        """
        default_result = self.traverse(seeds, max_depth=depth_default)
        max_result = self.traverse(seeds, max_depth=depth_max)
        default_ids = {c["cog_id"] for c in default_result}
        max_ids = {c["cog_id"] for c in max_result}
        missing = max_ids - default_ids
        score = 20 if not missing else int(20 * len(default_ids) / len(max_ids)) if max_ids else 20
        return {
            "seeds": seeds,
            "default_count": len(default_ids),
            "max_count": len(max_ids),
            "missing": list(missing),
            "score": score,
        }

    def audit_coverage(self, found_ids, ground_truth_ids):
        """D1：认知覆盖率审计"""
        found_set = set(found_ids)
        gt_set = set(ground_truth_ids)
        missing = gt_set - found_set
        coverage_rate = (len(gt_set) - len(missing)) / len(gt_set) if gt_set else 1.0
        score = int(20 * coverage_rate)
        return {
            "found_count": len(found_set),
            "gt_count": len(gt_set),
            "missing": list(missing),
            "coverage_rate": coverage_rate,
            "score": score,
        }

    def audit_all(self, seeds=None, ground_truth=None):
        """一键全量审计（D3+D4+可选D1）"""
        result = {}
        result["D3_version_chain"] = self.audit_version_chain()
        if seeds:
            result["D4_graph_completeness"] = self.audit_graph_completeness(seeds)
        if ground_truth:
            found = {c["cog_id"] for c in self.traverse(seeds or [])}
            result["D1_coverage"] = self.audit_coverage(list(found), ground_truth)
        return result

    def audit_poc_regression(self, seeds, ground_truth):
        """POC回归综合评分（D1-D5）"""
        d3 = self.audit_version_chain()
        d4 = self.audit_graph_completeness(seeds)
        found = {c["cog_id"] for c in self.traverse(seeds)}
        d1 = self.audit_coverage(list(found), ground_truth)
        # D2约束保留率和D5流程可执行性需要外部输入
        total = d1["score"] + d3["score"] + d4["score"] + 20 + 20  # D2/D5默认满分
        return {
            "D1_coverage": d1,
            "D3_version_chain": d3,
            "D4_graph_completeness": d4,
            "D2_constraints": {"score": 20, "note": "需外部输入"},
            "D5_executability": {"score": 20, "note": "需手动验证"},
            "total_score": total,
            "max_score": 100,
        }

    # ============================================================
    # 修复/写入类
    # ============================================================
    def fix_version_order(self):
        """修复cog_versions中version_order为None的记录"""
        docs = list(self.db.collection("cog_versions").all())
        fixed = 0
        for d in docs:
            if d.get("version_order") is None:
                v = d.get("version", "v1")
                try:
                    order = int(v.lstrip("v"))
                except ValueError:
                    order = 1
                self.db.collection("cog_versions").update(
                    {"_key": d["_key"], "version_order": order}
                )
                fixed += 1
        return {"fixed": fixed}

    def add_edge(self, from_cog, to_cog, edge_type="depends_on"):
        """添加依赖边"""
        from_unit = self.get_unit(from_cog)
        to_unit = self.get_unit(to_cog)
        if not from_unit or not to_unit:
            raise ValueError(f"认知单元不存在: from={from_cog}, to={to_cog}")
        now = datetime.utcnow().isoformat() + "Z"
        doc = {
            "_from": from_unit["_id"],
            "_to": to_unit["_id"],
            "from_cog_id": from_cog,
            "to_cog_id": to_cog,
            "edge_type": edge_type,
            "created_at": now,
        }
        return self.db.collection("cog_edges").insert(doc)

    def add_unit(self, cog_id, title, category, key_cognition, source_docs,
                 current_version="v1", status="active"):
        """创建新认知单元"""
        now = datetime.utcnow().isoformat() + "Z"
        doc = {
            "_key": cog_id,
            "cog_id": cog_id,
            "title": title,
            "category": category,
            "status": status,
            "key_cognition": key_cognition,
            "source_docs": source_docs,
            "current_version": current_version,
            "created_at": now,
        }
        result = self.db.collection("cognition_units").insert(doc, overwrite=True)
        # 补充v1版本记录
        self.add_version(cog_id, current_version,
                         str(source_docs[0]) if source_docs else "",
                         "初始版本")
        return result

    def add_version(self, cog_id, version, doc, summary, version_order=None):
        """添加版本记录，同时更新cognition_units的current_version"""
        if version_order is None:
            versions = self.get_versions(cog_id)
            version_order = len(versions) + 1
        now = datetime.utcnow().isoformat() + "Z"
        ver_doc = {
            "cog_id": cog_id,
            "version": version,
            "version_order": version_order,
            "doc": str(doc),
            "summary": summary,
            "created_at": now,
        }
        self.db.collection("cog_versions").insert(ver_doc)
        # 更新current_version
        unit = self.get_unit(cog_id)
        if unit:
            self.db.collection("cognition_units").update(
                {"_key": unit["_key"], "current_version": version}
            )

    def record_task(self, task_description, seed_cog_ids, loaded_cog_ids):
        """记录任务-认知映射（CP6）"""
        task_cogs = self.traverse(seed_cog_ids)
        gaps = self.verify_cognition_coverage(task_cogs, loaded_cog_ids)
        coverage_rate = 1.0 - (len(gaps) / len(task_cogs)) if task_cogs else 1.0
        now = datetime.utcnow().isoformat() + "Z"
        doc = {
            "task_description": task_description,
            "seed_cog_ids": seed_cog_ids,
            "loaded_cog_ids": loaded_cog_ids,
            "gaps": gaps,
            "coverage_rate": coverage_rate,
            "timestamp": now,
        }
        result = self.db.collection("cognition_tasks").insert(doc)
        print(f"覆盖率: {coverage_rate:.1%}")
        return result

    def delete_version(self, cog_id, version):
        """删除版本记录"""
        docs = list(self.db.collection("cog_versions").find({
            "cog_id": cog_id, "version": version
        }))
        for d in docs:
            self.db.collection("cog_versions").delete(d["_key"])
        return len(docs)

    def delete_edge(self, from_cog, to_cog, edge_type="depends_on"):
        """删除依赖边"""
        docs = list(self.db.collection("cog_edges").find({
            "from_cog_id": from_cog, "to_cog_id": to_cog, "edge_type": edge_type
        }))
        for d in docs:
            self.db.collection("cog_edges").delete(d["_key"])
        return len(docs)

    def delete_tasks_by_description(self, desc):
        """删除任务记录"""
        docs = list(self.db.collection("cognition_tasks").find({
            "task_description": desc
        }))
        for d in docs:
            self.db.collection("cognition_tasks").delete(d["_key"])
        return len(docs)

    def update_current_version(self, cog_id, version):
        """恢复current_version"""
        unit = self.get_unit(cog_id)
        if unit:
            self.db.collection("cognition_units").update(
                {"_key": unit["_key"], "current_version": version}
            )

    # ============================================================
    # 拓扑覆盖验证（数学项目独有，调用TopologyVerifier）
    # ============================================================
    def audit_topology_coverage(self):
        """调用TopologyVerifier做拓扑覆盖验证"""
        sys.path.insert(0, os.path.dirname(__file__))
        from topology_verifier import TopologyVerifier
        tv = TopologyVerifier(db_name="xishujuzhen_math")
        return tv.verify_all()

    def cross_reference_dg(self, cog_id):
        """查询认知单元在数学依赖图中的对应节点（意识节点双重身份）

        意识节点的cog_id（英文）和dg_nodes的node_id（中文）不同，需要映射。
        """
        # cog_id → dg_nodes.node_id 映射表
        name_map = {
            "invariant_thinking": "不变量思维",
            "local_global_thinking": "局部-全局思维",
            "approximation_thinking": "逼近论思维",
            "extreme_testing": "极端检验",
            "numerical_check": "数值检验意识",
        }
        dg_node_id = name_map.get(cog_id, cog_id)
        dg_nodes = list(self.db.collection("dg_nodes").find({"node_id": dg_node_id}))
        return dg_nodes[0] if dg_nodes else None
