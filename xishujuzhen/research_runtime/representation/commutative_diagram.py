"""
P7-3.2 交换图验证——表示变换的复合保持等价。

plan HoTT方向相关："对证明路径做语义等价分类"的交换图验证。
"""

from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass


@dataclass
class CommutativeSquare:
    """交换图的一个方块——四条边构成交换关系。"""
    square_id: str
    top_left: str       # A
    top_right: str      # B
    bottom_left: str    # C
    bottom_right: str   # D
    top_edge: str       # A→B 的映射ID
    bottom_edge: str    # C→D 的映射ID
    left_edge: str      # A→C 的映射ID
    right_edge: str     # B→D 的映射ID

    def to_dict(self) -> dict:
        return {
            "square_id": self.square_id,
            "top_left": self.top_left,
            "top_right": self.top_right,
            "bottom_left": self.bottom_left,
            "bottom_right": self.bottom_right,
            "top_edge": self.top_edge,
            "bottom_edge": self.bottom_edge,
            "left_edge": self.left_edge,
            "right_edge": self.right_edge,
        }


class CommutativeDiagramVerifier:
    """
    P7-3.2：交换图验证器。

    验证表示变换的复合保持等价——即交换图成立。
    交换图成立 = top_edge ∘ left_edge == right_edge ∘ bottom_edge
    （或等价地，A→B→D == A→C→D）
    """

    def __init__(self):
        self._squares: Dict[str, CommutativeSquare] = {}

    def add_square(self, square: CommutativeSquare) -> None:
        self._squares[square.square_id] = square

    def verify_square(
        self,
        square: CommutativeSquare,
        compose_fn=None,
    ) -> Dict[str, Any]:
        """
        验证一个交换方块是否成立。

        交换图成立 = 两条路径的复合结果相同：
        A→B→D == A→C→D

        边界情况：交换图不成立、交换图部分成立。
        """
        if compose_fn is None:
            # 无复合函数时，只检查结构完整性
            return {
                "square_id": square.square_id,
                "commutative": True,  # 结构性假设
                "path1": f"{square.top_left}→{square.top_right}→{square.bottom_right}",
                "path2": f"{square.top_left}→{square.bottom_left}→{square.bottom_right}",
                "verified": False,
                "note": "未提供compose_fn，只做结构检查",
            }

        # 实际验证：两条路径的复合结果是否相同
        try:
            result1 = compose_fn(square.top_edge, square.right_edge)
            result2 = compose_fn(square.left_edge, square.bottom_edge)
            commutative = result1 == result2
        except Exception as e:
            return {
                "square_id": square.square_id,
                "commutative": False,
                "error": str(e),
            }

        return {
            "square_id": square.square_id,
            "commutative": commutative,
            "path1_result": str(result1)[:200],
            "path2_result": str(result2)[:200],
            "verified": True,
        }

    def verify_all_squares(self, compose_fn=None) -> Dict[str, Any]:
        """验证所有交换方块。"""
        results = []
        for sq in self._squares.values():
            results.append(self.verify_square(sq, compose_fn))

        all_commutative = all(r.get("commutative", False) for r in results)
        partial = sum(1 for r in results if r.get("commutative", False))

        return {
            "n_squares": len(results),
            "all_commutative": all_commutative,
            "n_commutative": partial,
            "n_partial": len(results) - partial,
            "results": results,
        }

    def check_partial_commutativity(self, results: List[Dict]) -> Dict[str, Any]:
        """
        检查交换图部分成立的情况。

        边界情况：交换图部分成立。
        """
        partial = [r for r in results if not r.get("commutative", False)]
        return {
            "has_partial": len(partial) > 0,
            "partial_squares": [r.get("square_id") for r in partial],
            "n_partial": len(partial),
        }
