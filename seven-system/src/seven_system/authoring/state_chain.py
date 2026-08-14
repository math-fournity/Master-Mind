"""AuthoringStateChain — P3A 状态机。

来自 docs/implementation/09-phase-pipeline-p0-p9.md：

P3A 出题链状态机：
  brief→architect→draft→adversarial_editor→math_verifier→gate→release

每个状态转换被记录。Fake/stub 实现证明状态链工作，不需要真实模型调用。

硬约束：
- 非法状态转换 = QA_STATE_TRANSITION_ILLEGAL
- 缺少任一 canonical report = QA_CANONICAL_REPORT_MISSING
- retry-until-desired = QA_RETRY_UNTIL_DESIRED（同一 brief + draft 重新生成直到得到期望结果）

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable

from ..contracts.errors import (
    QA_P3A_STATES,
    QA_P3A_TRANSITIONS,
    QA_P3A_TERMINAL_STATES,
    VerificationErrorCode as EC,
)
from ..contracts.completion_contract import VerificationResult


@runtime_checkable
class AuthoringRoleExecutor(Protocol):
    """角色执行器协议——fake/stub adapter 实现此协议。"""

    def execute(
        self,
        role_type_id: str,
        brief_ref_and_hash: dict[str, str],
        draft_ref_and_hash: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """执行角色 job，返回结果 dict。

        结果必须包含：
        - verdict: PASS / FAIL / REQUEST_CHANGES
        - output: 角色输出内容
        - content_hash: 输出的 content hash
        """
        ...


@dataclass
class AuthoringStateChain:
    """AuthoringStateChain — P3A 状态机编排器。

    记录每个状态转换。验证状态转换合法性。
    检测 retry-until-desired（同一 brief 重复生成 draft 直到得到期望 verdict）。
    """

    current_state: str = "BRIEF_FROZEN"
    transitions: list[dict[str, Any]] = field(default_factory=list)
    canonical_reports: dict[str, dict[str, Any]] = field(default_factory=dict)
    _brief_ref: dict[str, str] = field(default_factory=dict)
    _draft_attempts: list[dict[str, Any]] = field(default_factory=list)
    _max_draft_attempts: int = 1
    _brief_recorded: bool = False

    def record_brief(self, brief_ref_and_hash: dict[str, str]) -> VerificationResult:
        """记录 brief 冻结。"""
        if self.current_state != "BRIEF_FROZEN":
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_STATE_TRANSITION_ILLEGAL],
                details=[f"cannot record brief in state {self.current_state}"],
            )
        self._brief_ref = dict(brief_ref_and_hash)
        self._brief_recorded = True
        self.canonical_reports["AuthoringBrief"] = {"ref_and_hash": dict(brief_ref_and_hash)}
        return VerificationResult(verdict="PASS")

    def route_architect(
        self,
        executor: AuthoringRoleExecutor,
        role_type_id: str = "question_architect",
    ) -> VerificationResult:
        """路由到 question_architect，产生 draft。"""
        if self.current_state != "BRIEF_FROZEN" or not self._brief_recorded:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_STATE_TRANSITION_ILLEGAL],
                details=[f"cannot route architect in state {self.current_state} (brief recorded: {self._brief_recorded})"],
            )
        if role_type_id != "question_architect":
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_UNQUALIFIED_ROLE_ROUTED],
                details=[f"expected question_architect, got {role_type_id}"],
            )
        result = executor.execute(role_type_id, self._brief_ref)
        if result.get("verdict") != "PASS":
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_CANONICAL_REPORT_MISSING],
                details=[f"architect execution failed: {result.get('verdict')}"],
            )
        self.canonical_reports["ArchitectOutput"] = result
        self._transition("ARCHITECT_ROUTED")
        return VerificationResult(verdict="PASS")

    def produce_draft(
        self,
        executor: AuthoringRoleExecutor,
        draft_ref_and_hash: dict[str, str],
        public_statement: str,
    ) -> VerificationResult:
        """产生 QuestionDraftVersion。"""
        if self.current_state != "ARCHITECT_ROUTED":
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_STATE_TRANSITION_ILLEGAL],
                details=[f"cannot produce draft in state {self.current_state}"],
            )
        # retry-until-desired 检测
        attempt = {
            "brief_ref": dict(self._brief_ref),
            "public_statement": public_statement,
        }
        self._draft_attempts.append(attempt)
        if len(self._draft_attempts) > self._max_draft_attempts:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_RETRY_UNTIL_DESIRED],
                details=[
                    f"retry-until-desired detected: {len(self._draft_attempts)} "
                    f"draft attempts for same brief"
                ],
            )
        self.canonical_reports["QuestionDraftVersion"] = {
            "ref_and_hash": dict(draft_ref_and_hash),
            "public_statement": public_statement,
        }
        self._transition("DRAFT_PRODUCED")
        return VerificationResult(verdict="PASS")

    def adversarial_review(
        self,
        executor: AuthoringRoleExecutor,
        review_ref_and_hash: dict[str, str],
    ) -> VerificationResult:
        """执行对抗性审查。"""
        if self.current_state != "DRAFT_PRODUCED":
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_STATE_TRANSITION_ILLEGAL],
                details=[f"cannot do adversarial review in state {self.current_state}"],
            )
        draft_ref = self.canonical_reports.get("QuestionDraftVersion", {}).get("ref_and_hash", {})
        result = executor.execute("adversarial_editor", self._brief_ref, draft_ref)
        if result.get("verdict") not in ("PASS", "REQUEST_CHANGES"):
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_CANONICAL_REPORT_MISSING],
                details=[f"adversarial review failed: {result.get('verdict')}"],
            )
        self.canonical_reports["AdversarialReview"] = {
            "ref_and_hash": dict(review_ref_and_hash),
            "result": result,
        }
        self._transition("ADVERSARIAL_REVIEW_DONE")
        return VerificationResult(verdict="PASS")

    def math_verification(
        self,
        executor: AuthoringRoleExecutor,
        dossier_ref_and_hash: dict[str, str],
    ) -> VerificationResult:
        """执行数学验证。"""
        if self.current_state != "ADVERSARIAL_REVIEW_DONE":
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_STATE_TRANSITION_ILLEGAL],
                details=[f"cannot do math verification in state {self.current_state}"],
            )
        draft_ref = self.canonical_reports.get("QuestionDraftVersion", {}).get("ref_and_hash", {})
        result = executor.execute("math_verifier", self._brief_ref, draft_ref)
        if result.get("verdict") not in ("PASS", "REQUEST_CHANGES"):
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_CANONICAL_REPORT_MISSING],
                details=[f"math verification failed: {result.get('verdict')}"],
            )
        self.canonical_reports["VerificationDossier"] = {
            "ref_and_hash": dict(dossier_ref_and_hash),
            "result": result,
        }
        self._transition("MATH_VERIFICATION_DONE")
        return VerificationResult(verdict="PASS")

    def sign_gate(
        self,
        gate_decision_ref_and_hash: dict[str, str],
    ) -> VerificationResult:
        """签署 G-Q-RELEASE gate。"""
        if self.current_state != "MATH_VERIFICATION_DONE":
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_STATE_TRANSITION_ILLEGAL],
                details=[f"cannot sign gate in state {self.current_state}"],
            )
        # 检查两种审查都存在
        if "AdversarialReview" not in self.canonical_reports:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_RELEASE_WITHOUT_BOTH_REVIEWS],
                details=["AdversarialReview missing before gate sign"],
            )
        if "VerificationDossier" not in self.canonical_reports:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_RELEASE_WITHOUT_BOTH_REVIEWS],
                details=["VerificationDossier missing before gate sign"],
            )
        self.canonical_reports["GateDecision"] = {
            "ref_and_hash": dict(gate_decision_ref_and_hash),
        }
        self._transition("GATE_RELEASE_SIGNED")
        return VerificationResult(verdict="PASS")

    def release(
        self,
        release_ref_and_hash: dict[str, str],
    ) -> VerificationResult:
        """发布 QuestionRelease。"""
        if self.current_state != "GATE_RELEASE_SIGNED":
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_STATE_TRANSITION_ILLEGAL],
                details=[f"cannot release in state {self.current_state}"],
            )
        # 检查所有 canonical report 存在
        required = (
            "AuthoringBrief",
            "ArchitectOutput",
            "QuestionDraftVersion",
            "AdversarialReview",
            "VerificationDossier",
            "GateDecision",
        )
        for r in required:
            if r not in self.canonical_reports:
                return VerificationResult(
                    verdict="FAIL",
                    error_codes=[EC.QA_CANONICAL_REPORT_MISSING],
                    details=[f"canonical report missing: {r}"],
                )
        self.canonical_reports["QuestionRelease"] = {
            "ref_and_hash": dict(release_ref_and_hash),
        }
        self._transition("QUESTION_RELEASED")
        return VerificationResult(verdict="PASS")

    def _transition(self, to_state: str) -> None:
        allowed = QA_P3A_TRANSITIONS.get(self.current_state, frozenset())
        if to_state not in allowed:
            raise ValueError(
                f"illegal transition {self.current_state} -> {to_state}"
            )
        self.transitions.append({
            "from": self.current_state,
            "to": to_state,
            "action": to_state,
        })
        self.current_state = to_state

    def verify_canonical_reports(self) -> VerificationResult:
        """验证所有 canonical report 存在。"""
        required = (
            "AuthoringBrief",
            "ArchitectOutput",
            "QuestionDraftVersion",
            "AdversarialReview",
            "VerificationDossier",
            "GateDecision",
            "QuestionRelease",
        )
        missing = [r for r in required if r not in self.canonical_reports]
        if missing:
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA_CANONICAL_REPORT_MISSING],
                details=[f"missing canonical reports: {missing}"],
            )
        return VerificationResult(verdict="PASS")

    @property
    def is_terminal(self) -> bool:
        return self.current_state in QA_P3A_TERMINAL_STATES

    @property
    def state_sequence(self) -> list[str]:
        return [t["to"] for t in self.transitions]
