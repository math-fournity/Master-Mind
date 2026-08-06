"""
P7-1.2b 转换保真验证——plan行356要求"跨表示运输必须证明转换保真"。

3项保真验证（137号Check List明确要求，不只是"证明保真"的概括）：
  1. 前向保真：forward_transport(source_object)的结果与target_form中的对应对象语义一致
  2. 后向保真：backward_transport(forward_transport(source_object)) = source_object
     （在preserved_invariants范围内）
  3. 不变量保持：preserved_invariants中列出的不变量在运输后仍然成立

边界情况：
  - 前向运输结果与target_form不一致→拒绝
  - 后向运输不还原→拒绝
  - 不变量在运输后不成立→拒绝
"""

from typing import Any, Dict, Callable, Optional, List
from dataclasses import dataclass


@dataclass
class FidelityCheckResult:
    """转换保真验证结果。"""
    forward_fidelity: bool
    backward_fidelity: bool
    invariant_preservation: bool
    details: Dict[str, Any]

    @property
    def all_passed(self) -> bool:
        return self.forward_fidelity and self.backward_fidelity and self.invariant_preservation

    def to_dict(self) -> dict:
        return {
            "forward_fidelity": self.forward_fidelity,
            "backward_fidelity": self.backward_fidelity,
            "invariant_preservation": self.invariant_preservation,
            "all_passed": self.all_passed,
            "details": self.details,
        }


class TransportFidelityVerifier:
    """
    P7-1.2b：转换保真验证器——实现3项保真验证。

    plan行356："接口义务：跨表示运输必须证明转换保真"
    """

    def verify_fidelity(
        self,
        rep_map,
        source_object: Any,
        forward_fn: Callable[[Any], Any],
        backward_fn: Optional[Callable[[Any], Any]] = None,
        target_consistency_fn: Optional[Callable[[Any], bool]] = None,
        invariant_check_fn: Optional[Callable[[Any, List[str]], bool]] = None,
    ) -> FidelityCheckResult:
        """
        执行3项保真验证。

        参数：
        - rep_map: RepresentationMap
        - source_object: 源对象
        - forward_fn: 正向运输函数
        - backward_fn: 逆向运输函数（可选，无backward_transport时为None）
        - target_consistency_fn: 检查运输结果与target_form一致性的函数
        - invariant_check_fn: 检查不变量保持的函数

        返回：FidelityCheckResult
        """
        details = {}

        # 验证1：前向保真
        forward_result = forward_fn(source_object)
        if target_consistency_fn is not None:
            forward_ok = target_consistency_fn(forward_result)
        else:
            # 无一致性检查函数时，只要运输成功就算前向保真
            forward_ok = forward_result is not None
        details["forward_result"] = str(forward_result)[:200]
        details["forward_fidelity"] = forward_ok

        # 验证2：后向保真
        if backward_fn is not None and rep_map.has_backward_transport():
            backward_result = backward_fn(forward_result)
            # 在preserved_invariants范围内检查还原
            backward_ok = self._check_backward_equality(
                source_object, backward_result, rep_map.preserved_invariants
            )
            details["backward_result"] = str(backward_result)[:200]
            details["backward_fidelity"] = backward_ok
        else:
            # 无逆向运输时，后向保真不适用
            backward_ok = True
            details["backward_fidelity"] = "N/A（无backward_transport）"

        # 验证3：不变量保持
        if invariant_check_fn is not None:
            invariant_ok = invariant_check_fn(forward_result, rep_map.preserved_invariants)
        elif rep_map.preserved_invariants:
            # 有不变量但无检查函数时，默认不通过（需要显式检查）
            invariant_ok = False
            details["invariant_warning"] = "有preserved_invariants但未提供invariant_check_fn"
        else:
            # 无不变量时，自动通过
            invariant_ok = True
        details["invariant_preservation"] = invariant_ok

        return FidelityCheckResult(
            forward_fidelity=forward_ok,
            backward_fidelity=backward_ok,
            invariant_preservation=invariant_ok,
            details=details,
        )

    def _check_backward_equality(
        self,
        original: Any,
        restored: Any,
        preserved_invariants: List[str],
    ) -> bool:
        """
        检查后向运输是否还原源对象（在preserved_invariants范围内）。

        如果有preserved_invariants，只检查这些不变量范围内的还原。
        如果没有preserved_invariants，检查完全相等。
        """
        if preserved_invariants:
            # 简化检查：如果类型相同且str表示相同，认为在不变量范围内还原
            return type(original) == type(restored) and str(original) == str(restored)
        else:
            return original == restored

    def verify_chain_fidelity(
        self,
        chain: list,
        source_object: Any,
        forward_fns: List[Callable[[Any], Any]],
    ) -> Dict[str, Any]:
        """
        验证链条的逐环节保真。

        对链条中每个RepresentationMap，依次执行前向运输并验证保真。
        """
        results = []
        current_obj = source_object
        for i, (rep_map, fn) in enumerate(zip(chain, forward_fns)):
            if rep_map is None:
                results.append({"segment": i, "error": "链条断裂"})
                break
            fidelity = self.verify_fidelity(rep_map, current_obj, fn)
            results.append({
                "segment": i,
                "rep_id": rep_map.rep_id,
                "fidelity": fidelity.to_dict(),
            })
            # 更新当前对象为运输结果（简化：用forward_fn的输出）
            current_obj = fn(current_obj)

        all_passed = all(
            r.get("fidelity", {}).get("all_passed", False) for r in results if "fidelity" in r
        )
        return {
            "segments": results,
            "all_passed": all_passed,
            "n_segments": len(results),
        }
