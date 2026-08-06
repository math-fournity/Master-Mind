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

    def __init__(self, host="localhost", port=8529, db_name=os.environ.get("ARANGO_DB", "xishujuzhen_math"),
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

    # ============================================================
    # arXiv论文查询
    # ============================================================

    def search_arxiv(self, category=None, keyword=None, author=None,
                     date_from=None, date_to=None, has_fulltext=None,
                     mapping_level=None, limit=20, sort="newest"):
        """查询arXiv论文（239K篇，存储在arxiv_papers collection）。

        参数：
            category: 主分类（如"math.AG"）或None
            keyword: 关键词，在title和abstract中搜索（AQL LIKE）
            author: 作者名（部分匹配）
            date_from: 发布日期起点（如"2026-01-01"）
            date_to: 发布日期终点（如"2026-08-01"）
            has_fulltext: True/False/None（是否有HTML全文）
            mapping_level: "L1"/"L2"/"L3"/"L4"/None
            limit: 返回数量上限
            sort: "newest"（按发布日期降序）/"oldest"/"relevance"

        返回：list of dict，每条含arxiv_id/title/authors/primary_category/published/has_fulltext
        """
        filters = []
        bind_vars = {"limit": limit}

        if category:
            filters.append("p.primary_category == @category")
            bind_vars["category"] = category

        if keyword:
            filters.append("(CONTAINS(LOWER(p.title), LOWER(@keyword)) OR CONTAINS(LOWER(p.abstract), LOWER(@keyword)))")
            bind_vars["keyword"] = keyword

        if author:
            filters.append("CONTAINS(LOWER(CONCAT_SEPARATOR(' ', p.authors[*])), LOWER(@author))")
            bind_vars["author"] = author

        if date_from:
            filters.append("p.published >= @date_from")
            bind_vars["date_from"] = date_from

        if date_to:
            filters.append("p.published <= @date_to")
            bind_vars["date_to"] = date_to

        if has_fulltext is not None:
            filters.append("p.has_fulltext == @has_fulltext")
            bind_vars["has_fulltext"] = has_fulltext

        if mapping_level:
            filters.append("p.mapping_level == @mapping_level")
            bind_vars["mapping_level"] = mapping_level

        filter_clause = "FILTER " + " AND ".join(filters) if filters else ""

        if sort == "newest":
            sort_clause = "SORT p.published DESC"
        elif sort == "oldest":
            sort_clause = "SORT p.published ASC"
        else:
            sort_clause = "SORT p.published DESC"

        aql = f"""
            FOR p IN arxiv_papers
            {filter_clause}
            {sort_clause}
            LIMIT @limit
            RETURN {{
                arxiv_id: p.arxiv_id,
                title: p.title,
                authors: p.authors,
                primary_category: p.primary_category,
                all_categories: p.all_categories,
                published: p.published,
                has_fulltext: p.has_fulltext,
                mapping_level: p.mapping_level,
                html_url: p.html_url
            }}
        """
        return list(self.db.aql.execute(aql, bind_vars=bind_vars))

    def get_arxiv_paper(self, arxiv_id):
        """获取单篇论文完整信息。"""
        clean_id = arxiv_id.split("v")[0] if "v" in arxiv_id[-3:] else arxiv_id
        doc_key = clean_id.replace(".", "_")
        return self.db.collection("arxiv_papers").get(doc_key)

    def promote_arxiv_paper(self, arxiv_id, mapping_level, linked_node_id):
        """提升论文映射级别并关联到依赖图节点。

        参数：
            arxiv_id: arXiv论文ID
            mapping_level: "L1"/"L2"/"L3"（不能降为L4）
            linked_node_id: 关联的dg_nodes.node_id
        """
        clean_id = arxiv_id.split("v")[0] if "v" in arxiv_id[-3:] else arxiv_id
        doc_key = clean_id.replace(".", "_")
        col = self.db.collection("arxiv_papers")
        doc = col.get(doc_key)
        if not doc:
            return None
        linked = doc.get("linked_nodes", [])
        if linked_node_id not in linked:
            linked.append(linked_node_id)
        col.update({"_key": doc_key, "mapping_level": mapping_level, "linked_nodes": linked})
        return col.get(doc_key)

    def get_arxiv_stats(self):
        """arXiv论文统计。"""
        stats = {}
        stats["total"] = self.db.collection("arxiv_papers").count()
        stats["by_category"] = list(self.db.aql.execute("""
            FOR p IN arxiv_papers
            COLLECT cat = p.primary_category WITH COUNT INTO c
            SORT c DESC
            LIMIT 20
            RETURN {category: cat, count: c}
        """))
        stats["by_fulltext"] = list(self.db.aql.execute("""
            FOR p IN arxiv_papers
            COLLECT ft = p.has_fulltext WITH COUNT INTO c
            RETURN {has_fulltext: ft, count: c}
        """))
        stats["by_mapping"] = list(self.db.aql.execute("""
            FOR p IN arxiv_papers
            COLLECT ml = p.mapping_level WITH COUNT INTO c
            SORT c DESC
            RETURN {mapping_level: ml, count: c}
        """))
        return stats

    def find_dependents_by_doc(self, doc_id):
        """反向查询：给定dev-docs编号，返回所有source_docs包含该编号的认知单元。

        用途：当某个dev-docs更新时，查哪些认知单元（含AGENTS.md技术说明节）
        依赖它，需要同步更新。
        """
        aql = "FOR u IN cognition_units FILTER @doc IN u.source_docs RETURN {cog_id: u.cog_id, title: u.title, source_docs: u.source_docs}"
        return list(self.db.aql.execute(aql, bind_vars={"doc": doc_id}))

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
        # [P0-8.3] 审计日志：记录add_unit操作，防止"ArangoDB有但JSON没有且无记录"
        self._audit_log("add_unit", cog_id, {
            "title": title,
            "category": category,
            "key_cognition": key_cognition[:200],
            "source_docs": source_docs,
            "current_version": current_version,
            "status": status,
        })
        return result

    def _audit_log(self, operation, cog_id, details=None):
        """[P0-8.3] 写入审计日志到cognition_audit_log collection"""
        now = datetime.utcnow().isoformat() + "Z"
        audit_doc = {
            "operation": operation,
            "cog_id": cog_id,
            "details": details or {},
            "timestamp": now,
        }
        try:
            if not self.db.has_collection("cognition_audit_log"):
                self.db.create_collection("cognition_audit_log")
            self.db.collection("cognition_audit_log").insert(audit_doc)
        except Exception as e:
            print(f"  ⚠️ 审计日志写入失败: {e}")

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
        tv = TopologyVerifier(db_name=os.environ.get("ARANGO_DB", "xishujuzhen_math"))
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
