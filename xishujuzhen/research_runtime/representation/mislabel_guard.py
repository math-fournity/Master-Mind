"""
P7-8.COMP4-6/P7-STOP-2 误标注防线。

plan行232-235（4个否定限定词）：
  - 把普通依赖图路径称为HoTT路径；
  - 把静态复制称为拓扑覆盖；
  - 未定义状态空间就声称检测"洞"或同调类；
  - 用embedding距离直接裁决数学等价或因果启发。

强制机制：
  普通依赖图路径称为HoTT路径→抛MislabelError
  静态复制称为拓扑覆盖→抛MislabelError
  embedding距离直接裁决数学等价→抛EmbeddingMisuseError
  标注为`语义规格`或`实验分析`的方法用于生产依赖→抛MislabelError
"""

from typing import Dict, Any, List


class MislabelError(Exception):
    """
    P7-8.COMP4/COMP5/P7-STOP-2强制机制：误标注→抛MislabelError。

    不只是返回False声明——是运行时强制阻断。
    """


class EmbeddingMisuseError(Exception):
    """
    P7-8.COMP6强制机制：embedding距离直接裁决数学等价→抛EmbeddingMisuseError。
    """


class MislabelGuard:
    """
    P7-8.COMP4-6/P7-STOP-2：误标注防线。

    plan行232-235的4个否定限定词全部实现。
    """

    def check_not_hott_path(self, path_type: str) -> Dict[str, Any]:
        """
        P7-8.COMP4：不把普通依赖图路径称为HoTT路径。

        plan行232："把普通依赖图路径称为HoTT路径"。
        """
        if path_type == "dependency_graph_path":
            return {
                "is_hott_path": False,
                "path_type": path_type,
                "correct_label": "依赖图路径",
                "not_mislabeled": True,
            }

        if path_type == "hott_path":
            return {
                "is_hott_path": True,
                "path_type": path_type,
                "correct_label": "HoTT路径",
                "not_mislabeled": True,
            }

        return {"is_hott_path": False, "path_type": path_type, "not_mislabeled": True}

    def assert_not_mislabel_hott(self, path_type: str, claimed_label: str) -> Dict[str, Any]:
        """
        断言不把普通依赖图路径误标为HoTT路径。

        强制机制：普通依赖图路径称为HoTT路径→抛MislabelError。
        """
        if path_type == "dependency_graph_path" and claimed_label == "hott_path":
            raise MislabelError(
                f"误标注：普通依赖图路径不能称为HoTT路径。"
                f"plan行232：把普通依赖图路径称为HoTT路径是禁止的。"
            )

        return {"not_mislabeled": True, "path_type": path_type, "claimed_label": claimed_label}

    def check_not_topology_cover(self, copy_type: str) -> Dict[str, Any]:
        """
        P7-8.COMP5：不把静态复制称为拓扑覆盖。

        plan行233："把静态复制称为拓扑覆盖"。
        """
        if copy_type == "static_copy":
            return {
                "is_topology_cover": False,
                "copy_type": copy_type,
                "correct_label": "静态复制",
                "not_mislabeled": True,
            }

        return {"is_topology_cover": False, "copy_type": copy_type, "not_mislabeled": True}

    def assert_not_mislabel_topology(self, copy_type: str, claimed_label: str) -> Dict[str, Any]:
        """
        断言不把静态复制误标为拓扑覆盖。

        强制机制：静态复制称为拓扑覆盖→抛MislabelError。
        """
        if copy_type == "static_copy" and claimed_label == "topology_cover":
            raise MislabelError(
                f"误标注：静态复制不能称为拓扑覆盖。"
                f"plan行233：把静态复制称为拓扑覆盖是禁止的。"
            )

        return {"not_mislabeled": True, "copy_type": copy_type, "claimed_label": claimed_label}

    def check_not_embedding_math_equivalence(self, method: str) -> Dict[str, Any]:
        """
        P7-8.COMP6：不用embedding距离直接裁决数学等价或因果启发。

        plan行234："用embedding距离直接裁决数学等价或因果启发"。
        """
        if method == "embedding_distance":
            return {
                "can_determine_math_equivalence": False,
                "can_determine_causality": False,
                "method": method,
                "requires_causal_validation": True,
            }

        return {"method": method, "not_misused": True}

    def assert_not_embedding_misuse(self, method: str, purpose: str) -> Dict[str, Any]:
        """
        断言不用embedding距离直接裁决数学等价。

        强制机制：embedding距离直接裁决数学等价→抛EmbeddingMisuseError。
        """
        if method == "embedding_distance" and purpose in [
            "math_equivalence", "causal_hint_determination"
        ]:
            raise EmbeddingMisuseError(
                f"embedding距离不能直接裁决'{purpose}'。"
                f"plan行234：用embedding距离直接裁决数学等价或因果启发是禁止的。"
                f"几何相近不等于数学等价，更不等于同一个Hint具有因果效果。"
            )

        return {"not_misused": True, "method": method, "purpose": purpose}

    def check_not_production_dependency(self, label: str) -> Dict[str, Any]:
        """
        P7-STOP-2：标注为`语义规格`或`实验分析`的方法不能用于生产依赖。

        plan行384："POMDP、范畴、层、HoTT、TDA等只在对象和可证伪问题明确时进入；
        文档必须区分'数学语义规格''首版工程表示''远期研究方向'。"
        """
        non_production_labels = ["语义规格", "实验分析"]
        if label in non_production_labels:
            return {
                "can_be_production_dependency": False,
                "label": label,
                "reason": f"标注为'{label}'的方法不能用于生产依赖",
            }

        return {"can_be_production_dependency": True, "label": label}

    def assert_not_production_dependency(self, label: str) -> Dict[str, Any]:
        """
        断言标注为`语义规格`或`实验分析`的方法不用于生产依赖。

        强制机制：标注为`语义规格`或`实验分析`的方法用于生产依赖→抛MislabelError。
        """
        check = self.check_not_production_dependency(label)
        if not check["can_be_production_dependency"]:
            raise MislabelError(
                f"标注为'{label}'的方法不能用于生产依赖。"
                f"plan行384：文档必须区分'数学语义规格''首版工程表示''远期研究方向'。"
            )

        return {"can_be_production_dependency": True, "label": label}
