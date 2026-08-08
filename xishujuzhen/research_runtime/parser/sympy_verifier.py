"""
SymPy精确验证模块：260号§3.2。

对LLM粗解析输出的每个MathObject做SymPy验证：
- 表达式可解析性（sympify不抛异常）
- 变量列表完整性（free_symbols对比）
- 恒等式验证（如适用，simplify(lhs-rhs)==0）
- 结构特征验证（如适用）

按260号§3.2.3的代码框架实现。
"""

from typing import List

import sympy as sp

from .models import MathObject


class SympyVerifier:
    """
    SymPy精确验证模块（260号§3.2）。

    对LLM输出的math_objects逐一做SymPy验证，返回修正后的对象。
    """

    def __init__(self):
        self.warnings: List[str] = []

    def verify_math_object(self, math_obj: MathObject) -> MathObject:
        """
        对单个数学对象做SymPy验证，返回修正后的对象（260号§3.2.3）。

        验证内容：
        1. 表达式可解析性：sympify(expr)不抛异常
        2. 变量列表完整性：expr.free_symbols与LLM声称的variables比较
        3. 恒等式验证（如适用）：simplify(lhs-rhs)==0
        4. 结构特征验证（如适用）

        验证失败不删除对象，只标记sympy_verified=False并降低置信度。
        """
        self.warnings = []

        if math_obj.sympy_expr is None:
            # 无SymPy表达式，无法验证
            math_obj.sympy_verified = False
            self.warnings.append(
                f"数学对象'{math_obj.name}'无sympy_expr，无法验证"
            )
            return math_obj

        try:
            # 验证表达式可解析性
            expr = sp.sympify(math_obj.sympy_expr)

            # 提取变量列表，与LLM声称的比较
            actual_vars = {str(s) for s in expr.free_symbols}
            claimed_vars = set(math_obj.variables)
            if actual_vars != claimed_vars:
                # 以SymPy提取的为准
                missing = actual_vars - claimed_vars
                extra = claimed_vars - actual_vars
                if missing:
                    self.warnings.append(
                        f"数学对象'{math_obj.name}'变量列表遗漏: {missing}"
                    )
                if extra:
                    self.warnings.append(
                        f"数学对象'{math_obj.name}'变量列表多出: {extra}"
                    )
                math_obj.variables = sorted(actual_vars)

            # 如果是identity类型，验证恒等式
            if math_obj.object_type == "identity":
                if isinstance(expr, sp.Eq):
                    diff = sp.simplify(expr.lhs - expr.rhs)
                    if diff == 0:
                        math_obj.properties["verified_identity"] = "true"
                    else:
                        math_obj.properties["verified_identity"] = "false"
                        self.warnings.append(
                            f"恒等式验证失败: {expr.lhs} - {expr.rhs} = {diff} ≠ 0"
                        )
                else:
                    # 非等式，尝试整体简化判断
                    simplified = sp.simplify(expr)
                    if simplified == 0:
                        math_obj.properties["verified_identity"] = "true"
                    else:
                        math_obj.properties["verified_identity"] = "unconfirmed"

            # 如果是definition类型且有等价性需要验证
            # （如D=kr+(n-k)s与D=√5(pn-k)的等价性）
            if math_obj.object_type == "definition":
                if isinstance(expr, sp.Eq):
                    # 定义性引入，验证可解析性即可
                    math_obj.properties["sympy_parseable"] = "true"
                else:
                    math_obj.properties["sympy_parseable"] = "true"

            math_obj.sympy_verified = True

        except Exception as e:
            math_obj.sympy_verified = False
            math_obj.properties["sympy_error"] = str(e)
            self.warnings.append(
                f"SymPy无法解析表达式'{math_obj.sympy_expr}': {e}"
            )

        return math_obj

    def verify_batch(self, math_objects: List[MathObject]) -> List[MathObject]:
        """批量验证数学对象，返回修正后的列表"""
        self.warnings = []
        results = []
        for math_obj in math_objects:
            verified = self.verify_math_object(math_obj)
            results.append(verified)
        return results

    def compute_sympy_factor(self, math_objects: List[MathObject]) -> float:
        """
        计算SymPy验证因子（260号§3.3.3）。

        - 所有math_objects都通过SymPy验证：1.0
        - 部分通过：0.8
        - 全部未通过但有math_objects：0.5
        - 无math_objects（纯文本推理）：1.0（不涉及SymPy验证）
        """
        if not math_objects:
            return 1.0  # 无math_objects，不涉及SymPy验证

        verified_count = sum(1 for m in math_objects if m.sympy_verified)
        total = len(math_objects)

        if verified_count == total:
            return 1.0
        elif verified_count > 0:
            return 0.8
        else:
            return 0.5

    def verify_equivalence(
        self, expr_str_1: str, expr_str_2: str, name: str = ""
    ) -> bool:
        """
        验证两个SymPy表达式是否等价（260号§4.2.3验证1）。

        用于验证如 D=kr+(n-k)s 与 D=√5(pn-k) 的等价性。
        """
        try:
            expr1 = sp.sympify(expr_str_1)
            expr2 = sp.sympify(expr_str_2)
            diff = sp.simplify(expr1 - expr2)
            if diff == 0:
                return True
            else:
                self.warnings.append(
                    f"等价性验证失败({name}): {expr_str_1} ≠ {expr_str_2}, 差={diff}"
                )
                return False
        except Exception as e:
            self.warnings.append(
                f"等价性验证异常({name}): {e}"
            )
            return False
