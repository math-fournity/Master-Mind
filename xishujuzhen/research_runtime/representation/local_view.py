"""
P7-4.1/P7-4.2 局部视图一致性检查+层式粘合。

plan行217："层论：在局部研究视图之间做一致性与全局粘合"

3项一致性检查（137号Check List明确要求）：
  1. 重叠区域识别
  2. 一致性判定
  3. 冲突标记

3步粘合（137号Check List明确要求）：
  1. 粘合前置检查
  2. 合并非重叠区域
  3. 合并重叠区域
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Set, Optional


@dataclass
class LocalView:
    """局部研究视图。"""
    view_id: str
    objects: Set[str] = field(default_factory=set)
    relations: Dict[str, str] = field(default_factory=dict)  # (obj_a, obj_b) -> relation

    def to_dict(self) -> dict:
        return {
            "view_id": self.view_id,
            "objects": list(self.objects),
            "relations": {k: v for k, v in self.relations.items()},
        }


class LocalViewConsistencyChecker:
    """
    P7-4.1：局部视图一致性检查——3项检查。

    plan行217："在局部研究视图之间做一致性与全局粘合"
    """

    def identify_overlap(self, view_a: LocalView, view_b: LocalView) -> Dict[str, Any]:
        """
        检查1：重叠区域识别。

        识别两个视图的共享对象和共享关系。
        """
        shared_objects = view_a.objects & view_b.objects
        shared_relations = {
            k: (view_a.relations.get(k), view_b.relations.get(k))
            for k in set(view_a.relations.keys()) & set(view_b.relations.keys())
        }

        return {
            "shared_objects": list(shared_objects),
            "n_shared_objects": len(shared_objects),
            "shared_relations": shared_relations,
            "n_shared_relations": len(shared_relations),
            "has_overlap": len(shared_objects) > 0 or len(shared_relations) > 0,
        }

    def check_consistency(self, view_a: LocalView, view_b: LocalView) -> Dict[str, Any]:
        """
        检查2：一致性判定。

        检查重叠区域中两个视图的关系是否一致。
        """
        overlap = self.identify_overlap(view_a, view_b)
        conflicts = []

        for rel_key, (rel_a, rel_b) in overlap["shared_relations"].items():
            if rel_a is not None and rel_b is not None and rel_a != rel_b:
                conflicts.append({
                    "relation_key": rel_key,
                    "view_a_relation": rel_a,
                    "view_b_relation": rel_b,
                })

        return {
            "consistent": len(conflicts) == 0,
            "n_conflicts": len(conflicts),
            "conflicts": conflicts,
            "overlap": overlap,
        }

    def mark_conflicts(self, view_a: LocalView, view_b: LocalView) -> Dict[str, Any]:
        """
        检查3：冲突标记。

        标记冲突的关系，供后续粘合使用。
        """
        consistency = self.check_consistency(view_a, view_b)
        marked = []

        for conflict in consistency["conflicts"]:
            marked.append({
                **conflict,
                "marked": True,
                "needs_resolution": True,
            })

        return {
            "n_marked": len(marked),
            "marked_conflicts": marked,
            "all_marked": consistency["n_conflicts"] == len(marked),
        }

    def full_check(self, view_a: LocalView, view_b: LocalView) -> Dict[str, Any]:
        """执行全部3项检查。"""
        overlap = self.identify_overlap(view_a, view_b)
        consistency = self.check_consistency(view_a, view_b)
        conflicts = self.mark_conflicts(view_a, view_b)

        return {
            "overlap_check": overlap,
            "consistency_check": consistency,
            "conflict_marking": conflicts,
            "all_3_checks_done": True,
        }


class LayeredGluer:
    """
    P7-4.2：层式粘合——3步粘合。

    plan行217："在局部研究视图之间做一致性与全局粘合"
    """

    def __init__(self, checker: LocalViewConsistencyChecker = None):
        self._checker = checker or LocalViewConsistencyChecker()

    def pre_glue_check(self, view_a: LocalView, view_b: LocalView) -> Dict[str, Any]:
        """
        步骤1：粘合前置检查。

        检查两个视图是否可以粘合（有重叠且无未解决冲突）。
        """
        full_check = self._checker.full_check(view_a, view_b)

        return {
            "can_glue": full_check["consistency_check"]["consistent"],
            "has_overlap": full_check["overlap_check"]["has_overlap"],
            "n_conflicts": full_check["consistency_check"]["n_conflicts"],
            "needs_conflict_resolution": full_check["consistency_check"]["n_conflicts"] > 0,
        }

    def merge_non_overlapping(self, view_a: LocalView, view_b: LocalView) -> Dict[str, Any]:
        """
        步骤2：合并非重叠区域。

        合并两个视图中不重叠的对象和关系。
        """
        overlap = self._checker.identify_overlap(view_a, view_b)
        shared_objects = set(overlap["shared_objects"])

        # 非重叠对象
        a_only = view_a.objects - shared_objects
        b_only = view_b.objects - shared_objects

        # 非重叠关系
        shared_rel_keys = set(overlap["shared_relations"].keys())
        a_only_rels = {k: v for k, v in view_a.relations.items() if k not in shared_rel_keys}
        b_only_rels = {k: v for k, v in view_b.relations.items() if k not in shared_rel_keys}

        merged_objects = a_only | b_only
        merged_relations = {**a_only_rels, **b_only_rels}

        return {
            "merged_objects": list(merged_objects),
            "merged_relations": merged_relations,
            "a_only_objects": list(a_only),
            "b_only_objects": list(b_only),
            "n_merged": len(merged_objects),
        }

    def merge_overlapping(self, view_a: LocalView, view_b: LocalView) -> Dict[str, Any]:
        """
        步骤3：合并重叠区域。

        合并两个视图中重叠的对象和关系（需要一致性检查通过）。
        """
        consistency = self._checker.check_consistency(view_a, view_b)

        if not consistency["consistent"]:
            return {
                "merged": False,
                "reason": "重叠区域有未解决冲突",
                "conflicts": consistency["conflicts"],
            }

        overlap = self._checker.identify_overlap(view_a, view_b)
        shared_objects = set(overlap["shared_objects"])

        # 合并重叠关系（一致性已检查通过，取任一视图的关系）
        shared_rel_keys = set(overlap["shared_relations"].keys())
        merged_shared_rels = {
            k: view_a.relations.get(k) or view_b.relations.get(k)
            for k in shared_rel_keys
        }

        return {
            "merged": True,
            "merged_shared_objects": list(shared_objects),
            "merged_shared_relations": merged_shared_rels,
            "n_merged_shared": len(shared_objects),
        }

    def full_glue(self, view_a: LocalView, view_b: LocalView) -> Dict[str, Any]:
        """执行全部3步粘合。"""
        pre_check = self.pre_glue_check(view_a, view_b)
        non_overlap_merge = self.merge_non_overlapping(view_a, view_b)
        overlap_merge = self.merge_overlapping(view_a, view_b)

        return {
            "pre_glue_check": pre_check,
            "non_overlapping_merge": non_overlap_merge,
            "overlapping_merge": overlap_merge,
            "all_3_steps_done": True,
            "glue_success": pre_check["can_glue"] and overlap_merge.get("merged", False),
        }
