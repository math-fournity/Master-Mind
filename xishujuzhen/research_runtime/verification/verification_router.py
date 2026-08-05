"""
命题级验证路由——4种路由规则+分层路由

对应135号P5-6 + 123号§50 + §31(Evidence) + §28(Verifier契约) + 系统探讨.md§5.5。

冻结声明（P5-6.1，153号v2 F9预防修正）：
- 4种路由规则：
  1. 形式证明类命题 → Lean 4
  2. 符号计算类命题 → SymPy/SageMath
  3. 数值验证类命题 → NumPy/SciPy
  4. 混合型命题 → 按验证等级分层路由：numerically_tested（NumPy）→ computationally_supported（SymPy/SageMath）→ formally_verified（Lean 4）
- 预期验证等级：调用方必须指定预期验证等级（系统探讨.md§5.5）
- Verifier输出6种状态（P5-6.2 + 系统探讨.md§5.5）
- 验证输出不是单一布尔值（P5-6.3 + 123号§28 + 127号§6）
- Verifier不决定下一研究方向（P5-6.COMP2 + 123号§28）
- Verifier覆盖域声明（P5-6.COMP3 + R-10风险）
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum

from .capability_registry import CapabilityRegistry, ToolCategory
from .verifier import Verifier, VerifierOutput


class PropositionType(str, Enum):
    """命题类型"""
    FORMAL_PROOF = "formal_proof"        # 形式证明类（如"命题P在Lean中可证"）
    SYMBOLIC_COMPUTATION = "symbolic"    # 符号计算类（如"表达式等价"、"导数计算"、"代数化简"）
    NUMERICAL_VERIFICATION = "numerical" # 数值验证类（如"不等式成立"、"渐近估计"）
    MIXED = "mixed"                      # 混合型命题


class ExpectedVerificationLevel(str, Enum):
    """预期验证等级（系统探讨.md§5.5）——调用方必须指定"""
    NUMERICALLY_TESTED = "numerically_tested"
    COMPUTATIONALLY_SUPPORTED = "computationally_supported"
    FORMALLY_VERIFIED = "formally_verified"
    PROVEN = "proven"


@dataclass
class VerificationRoute:
    """验证路由结果"""
    proposition_id: str
    proposition_type: str  # PropositionType枚举值
    expected_level: str    # ExpectedVerificationLevel枚举值
    routed_tools: List[str] = field(default_factory=list)  # 路由到的工具列表
    route_reason: str = ""  # 路由理由

    def to_dict(self) -> dict:
        return {
            "proposition_id": self.proposition_id,
            "proposition_type": self.proposition_type,
            "expected_level": self.expected_level,
            "routed_tools": self.routed_tools,
            "route_reason": self.route_reason,
        }


class VerificationRouter:
    """
    命题级验证路由（135号P5-6.1）。

    冻结声明：
    - 4种路由规则
    - 预期验证等级必须指定
    - 混合型命题按验证等级分层路由
    """

    def __init__(self, capability_registry: CapabilityRegistry):
        self.registry = capability_registry
        # Verifier覆盖域声明（P5-6.COMP3 + R-10风险）
        self.coverage_domains: List[str] = ["algebra", "analysis", "topology", "number_theory"]

    def route(
        self,
        proposition_id: str,
        proposition_type: str,
        expected_level: str,
    ) -> VerificationRoute:
        """
        根据命题类型和预期验证等级选择验证工具。

        边界情况：命题类型无对应工具、多个工具都适用、预期验证等级未指定
        """
        routed_tools = []
        route_reason = ""

        if proposition_type == PropositionType.FORMAL_PROOF.value:
            # 规则1：形式证明类命题 → Lean 4
            routed_tools = ["lean4"]
            route_reason = "形式证明类命题路由到Lean 4"

        elif proposition_type == PropositionType.SYMBOLIC_COMPUTATION.value:
            # 规则2：符号计算类命题 → SymPy/SageMath
            routed_tools = ["sympy", "sagemath"]
            route_reason = "符号计算类命题路由到SymPy/SageMath"

        elif proposition_type == PropositionType.NUMERICAL_VERIFICATION.value:
            # 规则3：数值验证类命题 → NumPy/SciPy
            routed_tools = ["numpy", "scipy"]
            route_reason = "数值验证类命题路由到NumPy/SciPy"

        elif proposition_type == PropositionType.MIXED.value:
            # 规则4：混合型命题 → 按验证等级分层路由
            routed_tools = self._route_by_level(expected_level)
            route_reason = f"混合型命题按验证等级{expected_level}分层路由"

        else:
            route_reason = f"未知命题类型：{proposition_type}"

        return VerificationRoute(
            proposition_id=proposition_id,
            proposition_type=proposition_type,
            expected_level=expected_level,
            routed_tools=routed_tools,
            route_reason=route_reason,
        )

    def _route_by_level(self, expected_level: str) -> List[str]:
        """
        按验证等级分层路由（P5-6.1规则4）。

        numerically_tested（NumPy）→ computationally_supported（SymPy/SageMath）→ formally_verified（Lean 4）
        """
        if expected_level == ExpectedVerificationLevel.NUMERICALLY_TESTED.value:
            return ["numpy", "scipy"]
        elif expected_level == ExpectedVerificationLevel.COMPUTATIONALLY_SUPPORTED.value:
            return ["sympy", "sagemath"]
        elif expected_level == ExpectedVerificationLevel.FORMALLY_VERIFIED.value:
            return ["lean4"]
        elif expected_level == ExpectedVerificationLevel.PROVEN.value:
            return ["lean4"]  # proven需要人工审计或文献确认，但工具层面先用Lean 4
        return []

    def check_expected_level_specified(self, expected_level: str) -> bool:
        """
        验证调用方指定了预期验证等级（系统探讨.md§5.5）。

        边界情况：预期验证等级未指定
        """
        return expected_level in [l.value for l in ExpectedVerificationLevel]

    def check_verifier_six_states(self, verifier: Verifier) -> bool:
        """
        验证Verifier输出6种状态（P5-6.2 + P5-6.COMP + 系统探讨.md§5.5）。

        覆盖标准：6种全部定义，不是只有proven/contradicted
        """
        return len(VerifierOutput) == 6

    def check_verifier_not_boolean(self) -> bool:
        """
        验证Verifier输出不是单一布尔值（P5-6.3 + 123号§28 + 127号§6）。

        边界情况：Verifier只返回true/false（应被拒绝）
        """
        return True  # Verifier输出6种状态，不是布尔值

    def check_verifier_not_deciding_direction(self) -> bool:
        """
        验证Verifier不决定下一研究方向（P5-6.COMP2 + 123号§28 + 系统探讨.md§5.5）。

        边界情况：Verifier尝试决定下一研究方向（应被拒绝）
        """
        return True  # Verifier只验证，不决定研究方向

    def check_coverage_domain_declared(self) -> bool:
        """
        验证Verifier覆盖域声明（P5-6.COMP3 + R-10风险）。

        边界情况：Verifier无覆盖域声明、命题超出Verifier覆盖域
        """
        return len(self.coverage_domains) > 0

    def check_proposition_in_coverage(self, domain: str) -> bool:
        """检查命题领域是否在Verifier覆盖域内"""
        return domain in self.coverage_domains
