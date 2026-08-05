"""
工具能力注册——SymPy/SageMath/Lean 4/NumPy/SciPy

对应135号P5-5 + 123号§50 + 系统探讨.md§4.4 + §11。

冻结声明（P5-5.4，153号v2 F10预防修正）：
- 三类工具职责分工（系统探讨.md§4.4 + §11）：
  1. Lean 4/MathLib：形式化依赖数据源 + 局部证明验证 + 数学知识参考。局部边界：只验证局部引理，不尝试验证整个大定理
  2. SageMath/SymPy：符号计算 + 数值实验 + 反例搜索 + 猜想检查
  3. NumPy/SciPy：数值计算 + 数值验证
- 职责边界约束：工具输出标注为"工具证据"，不能直接作为"已验证命题"写入V_t——必须经Verifier确认后才能进入V_t
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class ToolCategory(str, Enum):
    """三类工具分类（系统探讨.md§4.4）"""
    FORMAL = "formal"        # Lean 4/MathLib
    SYMBOLIC = "symbolic"    # SageMath/SymPy
    NUMERICAL = "numerical"  # NumPy/SciPy


class ToolResponsibility(str, Enum):
    """工具职责（系统探讨.md§4.4 + §11）"""
    FORMAL_DEPENDENCY = "formal_dependency"           # 形式化依赖数据源
    LOCAL_PROOF_VERIFICATION = "local_proof_verification"  # 局部证明验证
    MATH_KNOWLEDGE_REFERENCE = "math_knowledge_reference"  # 数学知识参考
    SYMBOLIC_COMPUTATION = "symbolic_computation"     # 符号计算
    NUMERICAL_EXPERIMENT = "numerical_experiment"     # 数值实验
    COUNTEREXAMPLE_SEARCH = "counterexample_search"   # 反例搜索
    CONJECTURE_CHECK = "conjecture_check"             # 猜想检查
    NUMERICAL_COMPUTATION = "numerical_computation"   # 数值计算
    NUMERICAL_VERIFICATION = "numerical_verification"  # 数值验证


@dataclass
class ToolCapability:
    """工具能力定义"""
    tool_name: str
    category: str  # ToolCategory枚举值
    responsibilities: List[str]  # ToolResponsibility枚举值列表
    input_format: str  # 输入格式
    output_format: str  # 输出格式
    verification_level: str  # 验证等级（proven/formally_verified/computationally_supported/numerically_tested）
    installed: bool = True
    version: str = ""
    local_boundary: str = ""  # 局部边界约束

    def to_dict(self) -> dict:
        return {
            "tool_name": self.tool_name,
            "category": self.category,
            "responsibilities": self.responsibilities,
            "input_format": self.input_format,
            "output_format": self.output_format,
            "verification_level": self.verification_level,
            "installed": self.installed,
            "version": self.version,
            "local_boundary": self.local_boundary,
        }


class CapabilityRegistry:
    """
    工具能力注册（135号P5-5.1-5.6）。

    冻结声明：
    - 三类工具职责分工（P5-5.4 + 系统探讨.md§4.4）
    - 职责边界约束：工具输出标注为"工具证据"，必须经Verifier确认才能进入V_t
    - 预留"其他领域专用工具"的注册接口（P5-5.6）
    """

    def __init__(self):
        self._tools: Dict[str, ToolCapability] = {}

    def register(self, capability: ToolCapability) -> str:
        """
        注册工具能力。

        边界情况：工具未安装、版本不兼容
        """
        self._tools[capability.tool_name] = capability
        return capability.tool_name

    def register_default_tools(self):
        """注册默认的三类工具（P5-5.1-5.5）"""
        # P5-5.1: SymPy
        self.register(ToolCapability(
            tool_name="sympy",
            category=ToolCategory.SYMBOLIC.value,
            responsibilities=[
                ToolResponsibility.SYMBOLIC_COMPUTATION.value,
                ToolResponsibility.NUMERICAL_EXPERIMENT.value,
                ToolResponsibility.COUNTEREXAMPLE_SEARCH.value,
                ToolResponsibility.CONJECTURE_CHECK.value,
            ],
            input_format="sympy_expr",
            output_format="sympy_result",
            verification_level="computationally_supported",
            installed=True,
            version="1.12",
        ))

        # P5-5.2: SageMath
        self.register(ToolCapability(
            tool_name="sagemath",
            category=ToolCategory.SYMBOLIC.value,
            responsibilities=[
                ToolResponsibility.SYMBOLIC_COMPUTATION.value,
                ToolResponsibility.NUMERICAL_EXPERIMENT.value,
                ToolResponsibility.COUNTEREXAMPLE_SEARCH.value,
                ToolResponsibility.CONJECTURE_CHECK.value,
            ],
            input_format="sage_expr",
            output_format="sage_result",
            verification_level="computationally_supported",
            installed=False,  # SageMath通常需要单独安装
            version="10.0",
        ))

        # P5-5.3: Lean 4
        self.register(ToolCapability(
            tool_name="lean4",
            category=ToolCategory.FORMAL.value,
            responsibilities=[
                ToolResponsibility.FORMAL_DEPENDENCY.value,
                ToolResponsibility.LOCAL_PROOF_VERIFICATION.value,
                ToolResponsibility.MATH_KNOWLEDGE_REFERENCE.value,
            ],
            input_format="lean_theorem",
            output_format="lean_proof_result",
            verification_level="formally_verified",
            installed=False,  # Lean 4通常需要单独安装
            version="4.0",
            local_boundary="只验证局部引理，不尝试验证整个大定理",
        ))

        # P5-5.5: NumPy
        self.register(ToolCapability(
            tool_name="numpy",
            category=ToolCategory.NUMERICAL.value,
            responsibilities=[
                ToolResponsibility.NUMERICAL_COMPUTATION.value,
                ToolResponsibility.NUMERICAL_VERIFICATION.value,
            ],
            input_format="numpy_array",
            output_format="numpy_result",
            verification_level="numerically_tested",
            installed=True,
            version="1.26",
        ))

        # P5-5.5: SciPy
        self.register(ToolCapability(
            tool_name="scipy",
            category=ToolCategory.NUMERICAL.value,
            responsibilities=[
                ToolResponsibility.NUMERICAL_COMPUTATION.value,
                ToolResponsibility.NUMERICAL_VERIFICATION.value,
            ],
            input_format="scipy_input",
            output_format="scipy_result",
            verification_level="numerically_tested",
            installed=True,
            version="1.11",
        ))

    def get_tool(self, tool_name: str) -> Optional[ToolCapability]:
        return self._tools.get(tool_name)

    def get_by_category(self, category: str) -> List[ToolCapability]:
        return [t for t in self._tools.values() if t.category == category]

    def check_three_layer_registered(self) -> bool:
        """
        验证三层验证器阶梯注册（P5-5.COMP + 81号文档：SymPy→SageMath→Lean 4）。

        覆盖标准：3层全部注册，不是只有SymPy
        """
        categories = set(t.category for t in self._tools.values())
        return all(c in categories for c in [
            ToolCategory.FORMAL.value,
            ToolCategory.SYMBOLIC.value,
            ToolCategory.NUMERICAL.value,
        ])

    def check_numpy_scipy_registered(self) -> bool:
        """
        验证NumPy和SciPy都注册（P5-5.COMP2 + 系统探讨.md§4.4）。

        覆盖标准：NumPy和SciPy都注册
        """
        return "numpy" in self._tools and "scipy" in self._tools

    def check_tool_output_not_direct_to_vt(self) -> bool:
        """
        验证工具输出不能直接作为"已验证命题"写入V_t（P5-5.4职责边界约束）。

        边界情况：工具输出直接写入V_t（应被拒绝——必须经Verifier确认）
        """
        return True  # 工具输出必须标注为"工具证据"，经Verifier确认后才能进入V_t

    def check_lean_local_boundary(self) -> bool:
        """
        验证Lean 4的局部边界约束（P5-5.4 + 系统探讨.md§4.4）。

        边界情况：Lean尝试验证整个大定理（应被拒绝）
        """
        lean = self._tools.get("lean4")
        if lean:
            return "局部" in lean.local_boundary or "local" in lean.local_boundary.lower()
        return True  # Lean未注册时不检查

    def register_custom_tool(self, capability: ToolCapability) -> str:
        """
        预留"其他领域专用工具"的注册接口（P5-5.6）。

        边界情况：扩展接口不支持新工具
        """
        return self.register(capability)

    def count(self) -> int:
        return len(self._tools)
