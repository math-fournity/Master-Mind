"""WP-ST1 Strategy Runtime — Selector/Renderer/Binding/Injection/Critic Runtime.

本包实现 ST1 工作包：
- FixturePreState: 开发/激活模式的显式前置状态
- Selector: 从冻结 TellStrategyRelease 检索/排序/弃权 Tell 候选
- Renderer: 将选中的 Tell 渲染为 model-facing HintInstance
- Binding: 将渲染的 hint 绑定到 problem context
- Injection: 将 bound hint 注入 Solver job
- Critic: 评估注入结果
- StrategyRuntime: 编排完整链
- ArmPayload: 冻结的实验对比臂
- StrategyCapabilityReport: 能力报告

关键约束：
- SIDE_EFFECT_FREE：不写 DB、不写 Redis、不写 D 盘、不调用 live model、不启动 Solver
- Fixture 冒充 live Case → BLOCK
- Answer 绑定到 hint → BLOCK
- Core/text 混淆 → BLOCK
- Distractor 不对等 → BLOCK
- 组件漂移 → BLOCK
- 没有 TellStrategyRelease ref → BLOCK
- Injection without binding → BLOCK
- Critic without injection → BLOCK
- Selector abstain not respected → BLOCK
- 所有 arm payload 是纯程序重放
"""

from .fixture_pre_state import (
    FixturePreState,
    make_fixture_pre_state,
    FixturePreStateVerificationResult,
    verify_fixture_pre_state,
)
from .selector import (
    Selector,
    SelectorReceipt,
    make_selector_receipt,
    SelectorReceiptVerificationResult,
    verify_selector_receipt,
)
from .renderer import (
    Renderer,
    RendererReceipt,
    make_renderer_receipt,
    RendererReceiptVerificationResult,
    verify_renderer_receipt,
)
from .binding import (
    Binder,
    BindingReceipt,
    make_binding_receipt,
    BindingReceiptVerificationResult,
    verify_binding_receipt,
    ST_TIMING_KINDS,
)
from .injection import (
    Injector,
    InjectionReceipt,
    make_injection_receipt,
    InjectionReceiptVerificationResult,
    verify_injection_receipt,
)
from .critic import (
    Critic,
    CriticDecision,
    make_critic_decision,
    CriticDecisionVerificationResult,
    verify_critic_decision,
)
from .runtime import (
    StrategyRuntime,
    StrategyRunReceipt,
    make_strategy_run_receipt,
    StrategyRunVerificationResult,
    verify_strategy_run_receipt,
)
from .arm_payload import (
    ArmPayload,
    make_arm_payload,
    ArmPayloadVerificationResult,
    verify_arm_payload,
    build_arm_payload_set,
)
from .capability_report import (
    StrategyCapabilityReport,
    build_strategy_capability_report,
    verify_strategy_capability_report,
    StrategyCapabilityReportError,
    STRATEGY_REPORT_SCHEMA_VERSION,
    STRATEGY_CHECK_IDS,
    STRATEGY_CLAIMS,
    STRATEGY_NONCLAIMS,
)

__all__ = [
    # fixture pre state
    "FixturePreState",
    "make_fixture_pre_state",
    "FixturePreStateVerificationResult",
    "verify_fixture_pre_state",
    # selector
    "Selector",
    "SelectorReceipt",
    "make_selector_receipt",
    "SelectorReceiptVerificationResult",
    "verify_selector_receipt",
    # renderer
    "Renderer",
    "RendererReceipt",
    "make_renderer_receipt",
    "RendererReceiptVerificationResult",
    "verify_renderer_receipt",
    # binding
    "Binder",
    "BindingReceipt",
    "make_binding_receipt",
    "BindingReceiptVerificationResult",
    "verify_binding_receipt",
    "ST_TIMING_KINDS",
    # injection
    "Injector",
    "InjectionReceipt",
    "make_injection_receipt",
    "InjectionReceiptVerificationResult",
    "verify_injection_receipt",
    # critic
    "Critic",
    "CriticDecision",
    "make_critic_decision",
    "CriticDecisionVerificationResult",
    "verify_critic_decision",
    # runtime
    "StrategyRuntime",
    "StrategyRunReceipt",
    "make_strategy_run_receipt",
    "StrategyRunVerificationResult",
    "verify_strategy_run_receipt",
    # arm payload
    "ArmPayload",
    "make_arm_payload",
    "ArmPayloadVerificationResult",
    "verify_arm_payload",
    "build_arm_payload_set",
    # capability report
    "StrategyCapabilityReport",
    "build_strategy_capability_report",
    "verify_strategy_capability_report",
    "StrategyCapabilityReportError",
    "STRATEGY_REPORT_SCHEMA_VERSION",
    "STRATEGY_CHECK_IDS",
    "STRATEGY_CLAIMS",
    "STRATEGY_NONCLAIMS",
]
