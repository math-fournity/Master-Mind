"""
P7-4.3 洞识别——4种候选障碍。

123号§20："首版可以识别：已知区域与开放义务之间没有已验证接口；
多条路线在同一缺失构造前停滞；局部视图在重叠部分不一致，无法粘合；
某表示中目标不可达，但存在未知的跨表示桥梁。"

plan行228："所谓'洞'首版仅定义为未满足接口、不可达开放义务或局部视图无法粘合的**候选障碍**，
不直接宣称是同调群元素。"

强制机制（P7-4.COMP）：
  洞的类型标注必须为"候选障碍"而非"同调群元素"→抛HoleTypeError。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class HoleTypeError(Exception):
    """
    P7-4.COMP强制机制：洞直接当作同调群元素→抛HoleTypeError。

    不只是返回False声明——是运行时强制阻断。
    """


class HoleType(Enum):
    """4种候选障碍（123号§20）。"""
    NO_VERIFIED_INTERFACE = "no_verified_interface"  # 已知区域与开放义务间无接口
    MULTI_ROUTE_STALL = "multi_route_stall"  # 多条路线在同一缺失构造前停滞
    LOCAL_VIEW_INCONSISTENT = "local_view_inconsistent"  # 局部视图重叠不一致
    UNKNOWN_CROSS_REP_BRIDGE = "unknown_cross_rep_bridge"  # 某表示中目标不可达但存在未知跨表示桥梁


@dataclass
class CandidateHole:
    """候选障碍——不是同调群元素。"""
    hole_id: str
    hole_type: HoleType
    description: str
    location: str = ""  # 障碍所在位置（如哪个表示/哪个区域）
    candidate_nature: str = "candidate_obstacle"  # 必须为"candidate_obstacle"

    def to_dict(self) -> dict:
        return {
            "hole_id": self.hole_id,
            "hole_type": self.hole_type.value,
            "description": self.description,
            "location": self.location,
            "candidate_nature": self.candidate_nature,
        }


class HoleDetector:
    """
    P7-4.3：洞识别——4种候选障碍。

    plan行228："洞首版仅定义为候选障碍，不直接宣称是同调群元素。"
    """

    def detect_no_verified_interface(
        self,
        known_region: str,
        open_obligation: str,
        verified_interfaces: List[str],
    ) -> Optional[CandidateHole]:
        """
        候选障碍1：已知区域与开放义务之间没有已验证接口。

        123号§20："已知区域与开放义务之间没有已验证接口。"
        """
        interface_key = f"{known_region}->{open_obligation}"
        if interface_key not in verified_interfaces:
            return CandidateHole(
                hole_id=f"hole_{known_region}_{open_obligation}",
                hole_type=HoleType.NO_VERIFIED_INTERFACE,
                description=f"已知区域'{known_region}'与开放义务'{open_obligation}'之间无已验证接口",
                location=known_region,
            )
        return None

    def detect_multi_route_stall(
        self,
        routes: List[List[str]],
        missing_construction: str,
    ) -> Optional[CandidateHole]:
        """
        候选障碍2：多条路线在同一缺失构造前停滞。

        123号§20："多条路线在同一缺失构造前停滞。"
        """
        stalled_routes = [r for r in routes if missing_construction not in r]
        if len(stalled_routes) >= 2:
            return CandidateHole(
                hole_id=f"hole_stall_{missing_construction}",
                hole_type=HoleType.MULTI_ROUTE_STALL,
                description=f"{len(stalled_routes)}条路线在缺失构造'{missing_construction}'前停滞",
                location=missing_construction,
            )
        return None

    def detect_local_view_inconsistent(
        self,
        view_overlaps: List[Dict[str, Any]],
    ) -> Optional[CandidateHole]:
        """
        候选障碍3：局部视图在重叠部分不一致，无法粘合。

        123号§20："局部视图在重叠部分不一致，无法粘合。"
        """
        inconsistent = [o for o in view_overlaps if not o.get("consistent", True)]
        if inconsistent:
            return CandidateHole(
                hole_id="hole_view_inconsistent",
                hole_type=HoleType.LOCAL_VIEW_INCONSISTENT,
                description=f"{len(inconsistent)}个视图重叠区域不一致，无法粘合",
                location="multiple_views",
            )
        return None

    def detect_unknown_cross_rep_bridge(
        self,
        representation: str,
        target_reachable: bool,
        cross_rep_bridges: List[str],
    ) -> Optional[CandidateHole]:
        """
        候选障碍4：某表示中目标不可达，但存在未知的跨表示桥梁。

        123号§20："某表示中目标不可达，但存在未知的跨表示桥梁。"
        """
        if not target_reachable and cross_rep_bridges:
            return CandidateHole(
                hole_id=f"hole_crossrep_{representation}",
                hole_type=HoleType.UNKNOWN_CROSS_REP_BRIDGE,
                description=f"表示'{representation}'中目标不可达，但存在{len(cross_rep_bridges)}个未知跨表示桥梁",
                location=representation,
            )
        return None

    def detect_all(
        self,
        known_regions: List[str],
        open_obligations: List[str],
        verified_interfaces: List[str],
        routes: List[List[str]],
        missing_constructions: List[str],
        view_overlaps: List[Dict[str, Any]],
        representations: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """检测全部4种候选障碍。"""
        holes = []

        # 候选障碍1
        for region in known_regions:
            for ob in open_obligations:
                h = self.detect_no_verified_interface(region, ob, verified_interfaces)
                if h:
                    holes.append(h)

        # 候选障碍2
        for mc in missing_constructions:
            h = self.detect_multi_route_stall(routes, mc)
            if h:
                holes.append(h)

        # 候选障碍3
        h = self.detect_local_view_inconsistent(view_overlaps)
        if h:
            holes.append(h)

        # 候选障碍4
        for rep in representations:
            h = self.detect_unknown_cross_rep_bridge(
                rep.get("name", ""),
                rep.get("target_reachable", True),
                rep.get("cross_rep_bridges", []),
            )
            if h:
                holes.append(h)

        return {
            "n_holes": len(holes),
            "holes": [h.to_dict() for h in holes],
            "all_are_candidate_obstacles": all(
                h.candidate_nature == "candidate_obstacle" for h in holes
            ),
        }

    def assert_candidate_obstacle(self, hole: CandidateHole) -> Dict[str, Any]:
        """
        断言洞是候选障碍——不是同调群元素。

        强制机制（P7-4.COMP）：
        洞的类型标注必须为"候选障碍"而非"同调群元素"→抛HoleTypeError。
        """
        if hole.candidate_nature != "candidate_obstacle":
            raise HoleTypeError(
                f"洞的类型标注必须为'候选障碍'，当前为'{hole.candidate_nature}'。"
                f"plan行228：洞首版仅定义为候选障碍，不直接宣称是同调群元素。"
            )

        return {
            "is_candidate_obstacle": True,
            "not_homology_element": True,
            "hole_id": hole.hole_id,
        }

    def check_not_homology_element(self, hole: CandidateHole) -> Dict[str, Any]:
        """
        P7-8.COMP2：不在状态空间未定义时宣称找到同调洞。

        plan行232："未定义状态空间就声称检测'洞'或同调类。"
        """
        if hole.candidate_nature == "homology_element":
            raise HoleTypeError(
                f"洞被标注为'同调群元素'——plan行228明确禁止。"
                f"洞首版仅定义为候选障碍。"
            )

        return {
            "is_candidate_obstacle": True,
            "not_homology_element": True,
            "hole_id": hole.hole_id,
        }
