#!/usr/bin/env python3
"""cognition_verifier_math.py —— 认知图遍历引擎

直接操作ArangoDB，执行AQL图遍历和覆盖验证。
适配自星学cognition_verifier.py，数据库名改为xishujuzhen_math。
"""
from typing import Optional


class CognitionVerifier:
    """认知图遍历引擎——直接操作ArangoDB"""

    def __init__(self, db):
        self.db = db

    def get_task_cognition(self, seed_cog_ids, max_depth=7):
        """步骤1：任务→认知子图

        从种子认知单元出发，沿depends_on边遍历，找到所有前置认知。
        返回认知子图列表，每个元素含cog_id/title/category/key_cognition/is_seed/depth。
        """
        # 获取种子的ArangoDB _id
        seed_ids = []
        for cog_id in seed_cog_ids:
            unit = self.db.collection("cognition_units").find({"cog_id": cog_id})
            docs = list(unit)
            if docs:
                seed_ids.append(docs[0]["_id"])
            else:
                print(f"  ⚠️  种子认知单元不存在: {cog_id}")

        if not seed_ids:
            return []

        # AQL图遍历
        aql = """
        FOR seed IN @seed_ids
          FOR v, e, p IN 0..@max_depth ANY seed cog_edges
            FILTER e == null || e.edge_type == 'depends_on'
            RETURN DISTINCT {
              cog_id: v.cog_id,
              title: v.title,
              category: v.category,
              status: v.status,
              key_cognition: v.key_cognition,
              current_version: v.current_version,
              source_docs: v.source_docs,
              is_seed: v._id == seed,
              depth: p.vertices.length - 1
            }
        """
        cursor = self.db.aql.execute(
            aql,
            bind_vars={"seed_ids": seed_ids, "max_depth": max_depth},
        )
        results = list(cursor)

        # 去重（DISTINCT在AQL中对对象不完全可靠，补充Python去重）
        seen = set()
        deduped = []
        for r in results:
            key = r["cog_id"]
            if key not in seen:
                seen.add(key)
                deduped.append(r)
        return deduped

    def verify_cognition_coverage(self, task_cogs, loaded_cog_ids):
        """步骤2：认知覆盖验证

        集合差集：task_cogs - loaded_cogs = 未覆盖的认知
        返回gaps列表（空列表=完全覆盖）
        """
        task_ids = {c["cog_id"] for c in task_cogs}
        loaded_set = set(loaded_cog_ids)
        uncovered = task_ids - loaded_set
        return list(uncovered)

    def get_version_chain(self, cog_id):
        """获取认知单元的版本链（按version_order排序）"""
        docs = list(self.db.collection("cog_versions").find({"cog_id": cog_id}))
        docs.sort(key=lambda d: d.get("version_order", 0))
        return docs

    def get_dependencies(self, cog_id):
        """获取认知单元的直接依赖（OUTBOUND depends_on + calls）"""
        unit = list(self.db.collection("cognition_units").find({"cog_id": cog_id}))
        if not unit:
            return []
        uid = unit[0]["_id"]
        aql = """
        FOR v, e IN 1..1 OUTBOUND @uid cog_edges
          RETURN {
            cog_id: v.cog_id,
            title: v.title,
            edge_type: e.edge_type
          }
        """
        cursor = self.db.aql.execute(aql, bind_vars={"uid": uid})
        return list(cursor)

    def get_dependents(self, cog_id):
        """获取反向依赖（谁依赖它）"""
        unit = list(self.db.collection("cognition_units").find({"cog_id": cog_id}))
        if not unit:
            return []
        uid = unit[0]["_id"]
        aql = """
        FOR v, e IN 1..1 INBOUND @uid cog_edges
          RETURN {
            cog_id: v.cog_id,
            title: v.title,
            edge_type: e.edge_type
          }
        """
        cursor = self.db.aql.execute(aql, bind_vars={"uid": uid})
        return list(cursor)

    def get_cognition_stats(self):
        """认知图统计"""
        units = list(self.db.collection("cognition_units").all())
        edges = self.db.collection("cog_edges").count()
        versions = self.db.collection("cog_versions").count()
        from collections import Counter
        cats = Counter(u.get("category", "?") for u in units)
        statuses = Counter(u.get("status", "?") for u in units)
        return {
            "total_units": len(units),
            "total_edges": edges,
            "total_versions": versions,
            "categories": dict(cats),
            "statuses": dict(statuses),
        }
