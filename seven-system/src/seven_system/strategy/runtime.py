"""StrategyRuntime — WP-ST1 编排 Selector→Renderer→Binding→Injection→Critic 链。

关键约束（blocker）：
- 所有步骤产出 receipts
- 纯程序重放：从冻结 TellStrategyRelease 确定性重放
- 链式依赖：injection 必须有 binding，critic 必须有 injection
- 组件版本必须一致（ST_COMPONENT_DRIFT）
- 没有 TellStrategyRelease ref → BLOCK

SIDE_EFFECT_FREE：纯内存实现，不启动 Solver、不调用 live model。
"""

from __future__ import annotations

import dataclasses
import hashlib
from dataclasses import dataclass, field
from typing import Any

from ..hashing import canonical_json_bytes
from ..contracts.errors import (
    ST_STRATEGY_STATES,
    VerificationErrorCode as EC,
)
from .selector import Selector, SelectorReceipt, make_selector_receipt
from .renderer import Renderer, RendererReceipt, make_renderer_receipt
from .binding import Binder, BindingReceipt, make_binding_receipt
from .injection import Injector, InjectionReceipt, make_injection_receipt
from .critic import Critic, CriticDecision, make_critic_decision
from .fixture_pre_state import FixturePreState


_RUNTIME_SCHEMA_ID = "seven/strategy-run-receipt"
_RUNTIME_SCHEMA_VERSION = 1
_HASH_ALGORITHM = "sha256(canonical-json-with-content_hash-null)"


@dataclass(frozen=True)
class StrategyRunReceipt:
    """完整策略运行收据——包含所有子 receipt。

    字段：
        run_id: 唯一标识
        release_ref: TellStrategyRelease 引用
        fixture_id: FixturePreState ID
        state: 运行状态（ST_STRATEGY_STATES）
        selector_receipt: Selector receipt
        renderer_receipt: Renderer receipt（abstain 时为 None）
        binding_receipt: Binding receipt（abstain 时为 None）
        injection_receipt: Injection receipt（abstain 时为 None）
        critic_decision: Critic decision（abstain 时为 None）
        component_versions: 各组件版本
        content_hash: 内容哈希
    """

    run_id: str
    release_ref: dict[str, str] = field(default_factory=dict)
    fixture_id: str = ""
    state: str = "IDLE"
    selector_receipt: SelectorReceipt | None = None
    renderer_receipt: RendererReceipt | None = None
    binding_receipt: BindingReceipt | None = None
    injection_receipt: InjectionReceipt | None = None
    critic_decision: CriticDecision | None = None
    component_versions: dict[str, str] = field(default_factory=dict)
    frozen_at: str = ""
    hash_algorithm: str = _HASH_ALGORITHM
    content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_id": _RUNTIME_SCHEMA_ID,
            "schema_version": _RUNTIME_SCHEMA_VERSION,
            "run_id": self.run_id,
            "release_ref": dict(self.release_ref),
            "fixture_id": self.fixture_id,
            "state": self.state,
            "selector_receipt": (
                self.selector_receipt.to_dict()
                if self.selector_receipt
                else None
            ),
            "renderer_receipt": (
                self.renderer_receipt.to_dict()
                if self.renderer_receipt
                else None
            ),
            "binding_receipt": (
                self.binding_receipt.to_dict()
                if self.binding_receipt
                else None
            ),
            "injection_receipt": (
                self.injection_receipt.to_dict()
                if self.injection_receipt
                else None
            ),
            "critic_decision": (
                self.critic_decision.to_dict()
                if self.critic_decision
                else None
            ),
            "component_versions": dict(self.component_versions),
            "frozen_at": self.frozen_at,
            "hash_algorithm": self.hash_algorithm,
            "content_hash": self.content_hash,
        }

    def compute_content_hash(self) -> str:
        d = self.to_dict()
        d["content_hash"] = None
        return hashlib.sha256(canonical_json_bytes(d)).hexdigest()

    @property
    def is_hash_valid(self) -> bool:
        return self.content_hash == self.compute_content_hash()

    @property
    def is_abstain(self) -> bool:
        return self.state == "ABSTAINED"


def make_strategy_run_receipt(
    *,
    run_id: str,
    release_ref: dict[str, str] | None = None,
    fixture_id: str = "",
    state: str = "IDLE",
    selector_receipt: SelectorReceipt | None = None,
    renderer_receipt: RendererReceipt | None = None,
    binding_receipt: BindingReceipt | None = None,
    injection_receipt: InjectionReceipt | None = None,
    critic_decision: CriticDecision | None = None,
    component_versions: dict[str, str] | None = None,
    frozen_at: str = "",
) -> StrategyRunReceipt:
    r = StrategyRunReceipt(
        run_id=run_id,
        release_ref=release_ref or {},
        fixture_id=fixture_id,
        state=state,
        selector_receipt=selector_receipt,
        renderer_receipt=renderer_receipt,
        binding_receipt=binding_receipt,
        injection_receipt=injection_receipt,
        critic_decision=critic_decision,
        component_versions=component_versions or {},
        frozen_at=frozen_at,
    )
    return dataclasses.replace(r, content_hash=r.compute_content_hash())


@dataclass(frozen=True)
class StrategyRunVerificationResult:
    verdict: str
    error_codes: list[EC] = field(default_factory=list)
    details: list[str] = field(default_factory=list)
    run_id: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "PASS"


def verify_strategy_run_receipt(
    receipt: StrategyRunReceipt,
    *,
    expected_release_hash: str | None = None,
) -> StrategyRunVerificationResult:
    errors: list[EC] = []
    details: list[str] = []

    d = receipt.to_dict()
    if d.get("schema_id") != _RUNTIME_SCHEMA_ID:
        errors.append(EC.SCHEMA_ID_MISMATCH)
        details.append(f"schema_id mismatch: expected {_RUNTIME_SCHEMA_ID}")

    # state valid
    if receipt.state not in ST_STRATEGY_STATES:
        errors.append(EC.ST_STRATEGY_STATE_INVALID)
        details.append(
            f"state '{receipt.state}' not in {sorted(ST_STRATEGY_STATES)}"
        )

    # release_ref required
    if not receipt.release_ref.get("release_id"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain release_id")
    if not receipt.release_ref.get("content_hash"):
        errors.append(EC.ST_TELL_STRATEGY_RELEASE_REF_MISSING)
        details.append("release_ref must contain content_hash")

    if expected_release_hash is not None:
        if receipt.release_ref.get("content_hash") != expected_release_hash:
            errors.append(EC.ST_COMPONENT_DRIFT)
            details.append(
                f"release_ref content_hash mismatch: claims "
                f"{receipt.release_ref.get('content_hash')}, "
                f"expected {expected_release_hash}"
            )

    # selector_receipt required
    if receipt.selector_receipt is None:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("selector_receipt is missing")

    # abstain path: if selector abstained, downstream receipts are None
    if receipt.selector_receipt is not None and receipt.selector_receipt.is_abstain:
        if receipt.state != "ABSTAINED":
            errors.append(EC.ST_SELECTOR_ABSTAIN_NOT_RESPECTED)
            details.append(
                "selector abstained but state is not ABSTAINED — "
                "abstain must be respected"
            )
        # downstream should be None
        if receipt.renderer_receipt is not None:
            errors.append(EC.ST_SELECTOR_ABSTAIN_NOT_RESPECTED)
            details.append(
                "selector abstained but renderer_receipt is not None"
            )
    else:
        # non-abstain path: all downstream receipts required
        if receipt.renderer_receipt is None:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("renderer_receipt is missing (non-abstain path)")
        if receipt.binding_receipt is None:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("binding_receipt is missing (non-abstain path)")
        if receipt.injection_receipt is None:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("injection_receipt is missing (non-abstain path)")
        if receipt.critic_decision is None:
            errors.append(EC.REQUIRED_FIELD_MISSING)
            details.append("critic_decision is missing (non-abstain path)")

        # chain integrity: renderer must reference selector
        if receipt.renderer_receipt is not None and receipt.selector_receipt is not None:
            if receipt.renderer_receipt.selector_receipt_id != receipt.selector_receipt.receipt_id:
                errors.append(EC.ST_COMPONENT_DRIFT)
                details.append(
                    "renderer_receipt.selector_receipt_id != "
                    "selector_receipt.receipt_id — chain broken"
                )

        # binding must reference renderer
        if receipt.binding_receipt is not None and receipt.renderer_receipt is not None:
            if receipt.binding_receipt.renderer_receipt_id != receipt.renderer_receipt.receipt_id:
                errors.append(EC.ST_COMPONENT_DRIFT)
                details.append(
                    "binding_receipt.renderer_receipt_id != "
                    "renderer_receipt.receipt_id — chain broken"
                )

        # injection must reference binding
        if receipt.injection_receipt is not None and receipt.binding_receipt is not None:
            if receipt.injection_receipt.binding_receipt_id != receipt.binding_receipt.receipt_id:
                errors.append(EC.ST_INJECTION_WITHOUT_BINDING)
                details.append(
                    "injection_receipt.binding_receipt_id != "
                    "binding_receipt.receipt_id — injection without binding"
                )

        # critic must reference injection
        if receipt.critic_decision is not None and receipt.injection_receipt is not None:
            if receipt.critic_decision.injection_receipt_id != receipt.injection_receipt.receipt_id:
                errors.append(EC.ST_CRITIC_WITHOUT_INJECTION)
                details.append(
                    "critic_decision.injection_receipt_id != "
                    "injection_receipt.receipt_id — critic without injection"
                )

    # content_hash
    if not receipt.content_hash:
        errors.append(EC.REQUIRED_FIELD_MISSING)
        details.append("content_hash is empty")
    elif receipt.content_hash != receipt.compute_content_hash():
        errors.append(EC.OBJECT_HASH_MISMATCH)
        details.append(
            f"content_hash mismatch: claims {receipt.content_hash}, "
            f"computed {receipt.compute_content_hash()}"
        )

    verdict = "PASS" if not errors else "FAIL"
    return StrategyRunVerificationResult(
        verdict=verdict,
        error_codes=errors,
        details=details,
        run_id=receipt.run_id,
    )


class StrategyRuntime:
    """StrategyRuntime — 编排 Selector→Renderer→Binding→Injection→Critic 链。

    纯程序重放：从冻结 TellStrategyRelease + FixturePreState 确定性运行。
    所有步骤产出 receipts。不启动 Solver、不调用 live model。
    """

    def __init__(
        self,
        *,
        selector: Selector | None = None,
        renderer: Renderer | None = None,
        binder: Binder | None = None,
        injector: Injector | None = None,
        critic: Critic | None = None,
    ) -> None:
        self.selector = selector or Selector()
        self.renderer = renderer or Renderer()
        self.binder = binder or Binder()
        self.injector = injector or Injector()
        self.critic = critic or Critic()

    def run(
        self,
        *,
        run_id: str,
        fixture: FixturePreState,
        candidate_core_ids: tuple[str, ...],
        renderer_ref: dict[str, str],
        injection_policy_ref: dict[str, str],
        critic_contract_ref: dict[str, str],
        rendered_payload: dict[str, Any] | None = None,
        critic_verdict: str = "NEUTRAL",
        critic_evidence: tuple[dict[str, Any], ...] = (),
        frozen_at: str = "",
    ) -> StrategyRunReceipt:
        """执行完整 Selector→Renderer→Binding→Injection→Critic 链。

        如果 selector abstain，则下游步骤跳过，state=ABSTAINED。
        """
        release_ref = fixture.release_ref
        component_versions = {
            "selector": self.selector.component_version,
            "renderer": self.renderer.component_version,
            "binding": self.binder.component_version,
            "injection": self.injector.component_version,
            "critic": self.critic.component_version,
        }

        # Step 1: Selector
        selector_receipt = self.selector.select(
            receipt_id=f"{run_id}-selector",
            release_ref=release_ref,
            candidate_core_ids=candidate_core_ids,
            reasoning="selector selected candidates from frozen release",
            frozen_at=frozen_at,
        )

        # abstain path
        if selector_receipt.is_abstain:
            return make_strategy_run_receipt(
                run_id=run_id,
                release_ref=release_ref,
                fixture_id=fixture.fixture_id,
                state="ABSTAINED",
                selector_receipt=selector_receipt,
                component_versions=component_versions,
                frozen_at=frozen_at,
            )

        # Step 2: Renderer
        renderer_receipt = self.renderer.render(
            receipt_id=f"{run_id}-renderer",
            release_ref=release_ref,
            selector_receipt_id=selector_receipt.receipt_id,
            renderer_ref=renderer_ref,
            payload=rendered_payload or {"hint": "guidance"},
            frozen_at=frozen_at,
        )

        # Step 3: Binding
        binding_receipt = self.binder.bind(
            receipt_id=f"{run_id}-binding",
            release_ref=release_ref,
            renderer_receipt_id=renderer_receipt.receipt_id,
            hint_instance_id=(
                renderer_receipt.hint_instance.instance_id
                if renderer_receipt.hint_instance
                else ""
            ),
            frozen_at=frozen_at,
        )

        # Step 4: Injection
        injection_receipt = self.injector.inject(
            receipt_id=f"{run_id}-injection",
            release_ref=release_ref,
            binding_receipt_id=binding_receipt.receipt_id,
            injection_policy_ref=injection_policy_ref,
            injection_position=binding_receipt.position,
            before_state_hash="0" * 64,
            after_state_hash="1" * 64,
            injected_payload_hash=(
                renderer_receipt.hint_instance.payload_hash
                if renderer_receipt.hint_instance
                else ""
            ),
            frozen_at=frozen_at,
        )

        # Step 5: Critic
        critic_decision = self.critic.evaluate(
            critic_id=f"{run_id}-critic",
            release_ref=release_ref,
            injection_receipt_id=injection_receipt.receipt_id,
            critic_contract_ref=critic_contract_ref,
            verdict=critic_verdict,
            evidence=critic_evidence,
            reasoning="critic evaluated injection outcome",
            frozen_at=frozen_at,
        )

        return make_strategy_run_receipt(
            run_id=run_id,
            release_ref=release_ref,
            fixture_id=fixture.fixture_id,
            state="CRITIQUED",
            selector_receipt=selector_receipt,
            renderer_receipt=renderer_receipt,
            binding_receipt=binding_receipt,
            injection_receipt=injection_receipt,
            critic_decision=critic_decision,
            component_versions=component_versions,
            frozen_at=frozen_at,
        )

    def run_abstain(
        self,
        *,
        run_id: str,
        fixture: FixturePreState,
        abstain_reason: str,
        frozen_at: str = "",
    ) -> StrategyRunReceipt:
        """执行 abstain 路径——selector 弃权，下游跳过。"""
        release_ref = fixture.release_ref
        component_versions = {
            "selector": self.selector.component_version,
            "renderer": self.renderer.component_version,
            "binding": self.binder.component_version,
            "injection": self.injector.component_version,
            "critic": self.critic.component_version,
        }

        selector_receipt = self.selector.abstain(
            receipt_id=f"{run_id}-selector",
            release_ref=release_ref,
            abstain_reason=abstain_reason,
            reasoning="selector abstained — no suitable Tell candidates",
            frozen_at=frozen_at,
        )

        return make_strategy_run_receipt(
            run_id=run_id,
            release_ref=release_ref,
            fixture_id=fixture.fixture_id,
            state="ABSTAINED",
            selector_receipt=selector_receipt,
            component_versions=component_versions,
            frozen_at=frozen_at,
        )
