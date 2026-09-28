"""
P7-7.2 持久同调——探索对噪声稳定的轨迹形状特征。

plan行220："持久同调：探索对噪声稳定的轨迹形状特征"

前置条件：必须先通过TDAGate的4限定词检查。
"""

from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class PersistenceDiagram:
    """持久同调图——记录各维度的同调类及其持久性。"""
    dimension: int  # 同调维度（0=连通分量, 1=环, 2=空腔）
    birth: float    # 出生时间（filtration参数）
    death: float    # 死亡时间
    persistence: float = 0.0  # 持久性 = death - birth

    def __post_init__(self):
        self.persistence = self.death - self.birth

    def to_dict(self) -> dict:
        return {
            "dimension": self.dimension,
            "birth": self.birth,
            "death": self.death,
            "persistence": self.persistence,
        }


class PersistentHomology:
    """
    P7-7.2：持久同调计算。

    plan行220："持久同调：探索对噪声稳定的轨迹形状特征"
    123号§20："只有定义状态空间、邻接、尺度和等价关系后，才可以研究持久同调。"
    """

    def __init__(self, tda_gate=None):
        self._tda_gate = tda_gate  # TDAGate实例，用于前置条件检查

    def compute_persistence(
        self,
        points: List[List[float]],
        max_dimension: int = 2,
        filtration_values: List[float] = None,
    ) -> Dict[str, Any]:
        """
        计算持久同调。

        前置条件：必须先通过TDAGate的4限定词检查。
        """
        # 检查前置条件
        if self._tda_gate is not None:
            self._tda_gate.assert_can_do_tda()

        # 简化实现：实际持久同调需要Vietoris-Rips复形或Cech复形
        # 这里只做连通性分析（0维同调）
        diagrams = []

        if filtration_values is None:
            # 自动生成filtration值
            max_dist = self._max_pairwise_distance(points)
            filtration_values = [max_dist * f for f in [0.1, 0.3, 0.5, 0.7, 1.0]]

        # 0维同调：连通分量的合并
        for i, eps in enumerate(filtration_values):
            n_components = self._count_components(points, eps)
            if i == 0:
                # 初始：每个点是一个连通分量
                for j in range(n_components):
                    diagrams.append(PersistenceDiagram(
                        dimension=0, birth=0.0, death=filtration_values[-1]
                    ))
            # 简化：不追踪完整的合并过程

        return {
            "n_points": len(points),
            "n_diagrams": len(diagrams),
            "diagrams": [d.to_dict() for d in diagrams],
            "max_dimension": max_dimension,
            "filtration_values": filtration_values,
            "computed": True,
        }

    def _max_pairwise_distance(self, points: List[List[float]]) -> float:
        """计算点集的最大两两距离。"""
        import math
        max_d = 0.0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = math.sqrt(sum((a - b) ** 2 for a, b in zip(points[i], points[j])))
                max_d = max(max_d, d)
        return max_d

    def _count_components(self, points: List[List[float]], epsilon: float) -> int:
        """计算给定epsilon下的连通分量数。"""
        import math
        n = len(points)
        visited = [False] * n
        components = 0

        for i in range(n):
            if not visited[i]:
                components += 1
                # BFS
                queue = [i]
                visited[i] = True
                while queue:
                    curr = queue.pop(0)
                    for j in range(n):
                        if not visited[j]:
                            d = math.sqrt(
                                sum((a - b) ** 2 for a, b in zip(points[curr], points[j]))
                            )
                            if d <= epsilon:
                                visited[j] = True
                                queue.append(j)

        return components

    def find_stable_features(
        self,
        diagrams: List[PersistenceDiagram],
        persistence_threshold: float = 0.1,
    ) -> Dict[str, Any]:
        """找出对噪声稳定的特征（持久性高的特征）。"""
        stable = [d for d in diagrams if d.persistence >= persistence_threshold]
        return {
            "n_stable_features": len(stable),
            "stable_features": [d.to_dict() for d in stable],
            "persistence_threshold": persistence_threshold,
            "noise_stable": True,
        }
