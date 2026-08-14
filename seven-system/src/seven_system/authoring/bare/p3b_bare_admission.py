"""P3BBareAdmission — P3B problem-only bare admission pipeline（WP-QA1）。

来自 docs/implementation/09-phase-pipeline-p0-p9.md lines 72-76：

Only give QuestionRelease public statement to TargetSolverPort for problem-only
bare. No Tell/Hint, not part of P5. Success/failure both retained, forbidden to
modify question or continue generating until failure.

Output: RunArtifactBundle, BareBaseline, BareQualificationResult.

P3B pipeline:
1. take immutable QuestionRelease
2. submit to TargetSolverPort (problem-only, no Tell/Hint)
3. collect bare results
4. produce BareBaseline + BareQualificationResult

使用 FakeHarnessAdapter for SIDE_EFFECT_FREE。

硬约束（blocker）：
- Tell/Hint sneaked into bare submission → BLOCK
- Question modified after bare results → BLOCK
- Successful questions selectively deleted → BLOCK
- Retry-until-fail → BLOCK
- bare results flow back to modify question draft → BLOCK
- Missing QuestionRelease ref → BLOCK

SIDE_EFFECT_FREE：纯内存实现，不调用真实 solver_harness / DB / model。
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from ...contracts.errors import (
    QA1_P3B_STATES,
    QA1_P3B_TRANSITIONS,
    QA1_P3B_TERMINAL_STATES,
    QA1_BARE_STATUSES,
    QA1_QUALIFICATION_STATUSES,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult
from ..question_release import QuestionRelease
from .bare_baseline import (
    BareAttemptResult,
    BareBaseline,
    build_bare_baseline,
    verify_bare_baseline,
)
from .bare_qualification import (
    ProblemQualification,
    BareQualificationResult,
    build_bare_qualification_result,
    verify_bare_qualification_result,
)


# Tell/Hint 关键词——bare submission 中不得出现这些
_TELL_HINT_KEYWORDS: frozenset[str] = frozenset(
    {"tell", "hint", "guidance", "scaffolding", "scaffold", "prompt_hint"}
)


@dataclass(frozen=True)
class RunArtifactBundle:
    """RunArtifactBundle — P3B 运行资产包。不可变。

    包含 bare admission 运行产生的所有资产引用。
    """

    bundle_id: str
    question_release_ref_and_hash: dict[str, str]
    bare_baseline_ref_and_hash: dict[str, str]
    qualification_result_ref_and_hash: dict[str, str]
    attempt_receipt_refs: list[dict[str, str]]
    problem_only: bool
    no_tell_hint: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "bundle_id": self.bundle_id,
            "question_release_ref_and_hash": dict(self.question_release_ref_and_hash),
            "bare_baseline_ref_and_hash": dict(self.bare_baseline_ref_and_hash),
            "qualification_result_ref_and_hash": dict(
                self.qualification_result_ref_and_hash
            ),
            "attempt_receipt_refs": [dict(r) for r in self.attempt_receipt_refs],
            "problem_only": self.problem_only,
            "no_tell_hint": self.no_tell_hint,
        }


class P3BBareAdmission:
    """P3BBareAdmission — P3B problem-only bare admission pipeline。

    流程：
    1. 接收 immutable QuestionRelease
    2. 构造 problem-only SolverJob（只给 public_statement，无 Tell/Hint）
    3. 通过 TargetSolverPort（FakeHarnessAdapter）提交 → collect
    4. 收集 bare results（成功和失败都保留）
    5. 构建 BareBaseline
    6. 从 bare results 判定 BareQualificationResult
    7. 产出 RunArtifactBundle

    硬约束：
    - bare submission 只含 public_statement，不含 Tell/Hint
    - 成功和失败都保留
    - 不可修改 question
    - 不可 retry-until-fail
    - bare 结果不回流改 draft
    """

    def __init__(self, solver_port: Any) -> None:
        """初始化 P3B bare admission pipeline。

        solver_port 必须实现 TargetSolverPort 协议（FakeHarnessAdapter）。
        """
        self._solver_port = solver_port
        self._state: str = "RELEASE_FROZEN"
        self._attempts_made: int = 0
        self._question_release: QuestionRelease | None = None
        self._bare_results: list[BareAttemptResult] = []
        self._receipts: list[dict[str, str]] = []
        self._baseline: BareBaseline | None = None
        self._qualification: BareQualificationResult | None = None
        self._bundle: RunArtifactBundle | None = None

    @property
    def state(self) -> str:
        return self._state

    def _transition(self, target: str) -> VerificationResult:
        if target not in QA1_P3B_TRANSITIONS.get(self._state, frozenset()):
            return VerificationResult(
                verdict="FAIL",
                error_codes=[EC.QA1_BARE_ADMISSION_STATE_INVALID],
                details=[
                    f"illegal state transition: {self._state} → {target}"
                ],
            )
        self._state = target
        return VerificationResult(verdict="PASS")

    def admit(
        self,
        *,
        question_release: QuestionRelease,
        baseline_id: str,
        result_id: str,
        bundle_id: str,
        bare_submission_payload: dict[str, Any] | None = None,
    ) -> tuple[RunArtifactBundle | None, VerificationResult]:
        """执行 P3B bare admission pipeline。

        参数：
        - question_release：不可变的 QuestionRelease
        - baseline_id：BareBaseline ID
        - result_id：BareQualificationResult ID
        - bundle_id：RunArtifactBundle ID
        - bare_submission_payload：可选的自定义 submission payload
          （用于 blocker test：注入 Tell/Hint）

        返回 (RunArtifactBundle | None, VerificationResult)。
        如果验证失败，返回 (None, VerificationResult(FAIL))。
        """
        errors: list[EC] = []
        details: list[str] = []

        # ─── 1. 验证 QuestionRelease ─────────────────────────────────
        self._question_release = question_release
        release_ref = {
            "ref_id": question_release.release_id,
            "sha256": question_release.content_hash,
        }

        # blocker: missing QuestionRelease ref
        if not question_release.release_id or not question_release.content_hash:
            errors.append(EC.QA1_QUESTION_RELEASE_REF_MISSING)
            details.append("QuestionRelease ref_id or content_hash is empty")
            return None, VerificationResult(
                verdict="FAIL", error_codes=errors, details=details
            )

        # ─── 2. 检查 bare submission 是否 problem-only（无 Tell/Hint） ──
        submission = bare_submission_payload or {}
        submission_str = str(submission).lower()
        for keyword in _TELL_HINT_KEYWORDS:
            if keyword in submission_str:
                errors.append(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE)
                details.append(
                    f"Tell/Hint keyword {keyword!r} sneaked into bare submission"
                )

        # problem_only check: submission must only contain public_statement
        if submission:
            allowed_keys = {"public_statement", "problem_ref_id"}
            extra_keys = set(submission.keys()) - allowed_keys
            if extra_keys:
                # Check if extra keys contain tell/hint
                for key in extra_keys:
                    key_lower = key.lower()
                    if any(kw in key_lower for kw in _TELL_HINT_KEYWORDS):
                        if EC.QA1_TELL_HINT_SNEAKED_INTO_BARE not in errors:
                            errors.append(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE)
                            details.append(
                                f"bare submission contains forbidden key {key!r}"
                            )

        if errors:
            return None, VerificationResult(
                verdict="FAIL", error_codes=errors, details=details
            )

        # ─── 3. 提交到 TargetSolverPort（problem-only） ───────────────
        # transition: RELEASE_FROZEN → BARE_SUBMITTED
        trans = self._transition("BARE_SUBMITTED")
        if not trans.passed:
            return None, trans

        # Build SolverJob for problem-only bare
        from ...adapters.solver.port import build_solver_job
        from ...adapters.solver.harness_profile import build_harness_profile

        profile = self._solver_port.harness_profile
        if profile is None:
            # fallback: build a fake profile
            content = hashlib.sha256(b"fake-harness-content-v1").hexdigest()
            profile = build_harness_profile(
                version="fake-harness-v1",
                content_hash=content,
                harness_kind="FAKE_HARNESS",
                tool_policy_kind="NO_TOOL",
            )

        attempt_id = f"bare-{question_release.release_id}-{self._attempts_made}"
        self._attempts_made += 1

        job = build_solver_job(
            problem_ref_id=question_release.release_id,
            problem_sha256=question_release.content_hash,
            view_ref_id=f"public-statement-{question_release.release_id}",
            view_sha256=hashlib.sha256(
                question_release.public_statement.encode("utf-8")
            ).hexdigest(),
            budget_contract={
                "wallclock_seconds": 300,
                "max_tokens": 10000,
                "max_cost_microunits": 0,
            },
            tool_policy_kind="NO_TOOL",
            idempotency_key=f"bare-idempotent-{attempt_id}",
            fence_token=f"bare-fence-{attempt_id}",
            attempt_id=attempt_id,
            repo_workspace_spec={"isolation_kind": "EPHEMERAL_SANDBOX"},
            harness_profile_ref_id=profile.version,
            harness_profile_sha256=profile.profile_hash,
        )

        # prepare → launch → collect
        try:
            prepared = self._solver_port.prepare(job)
            ticket = self._solver_port.launch(prepared)
            receipt = self._solver_port.collect(ticket)
        except Exception as exc:
            # If solver fails, treat as QUARANTINE
            bare_result = BareAttemptResult(
                problem_ref_id=question_release.release_id,
                bare_status="QUARANTINE",
                attempt_ref_id=attempt_id,
                terminal_reason="SOLVER_ERROR",
                tell_hint_included=False,
            )
            self._bare_results.append(bare_result)
            self._receipts.append({
                "ref_id": attempt_id,
                "sha256": "0" * 64,
            })
        else:
            # Determine bare status from receipt
            bare_status = self._determine_bare_status(receipt)
            bare_result = BareAttemptResult(
                problem_ref_id=question_release.release_id,
                bare_status=bare_status,
                attempt_ref_id=attempt_id,
                terminal_reason=receipt.terminal_reason,
                tell_hint_included=False,
            )
            self._bare_results.append(bare_result)
            self._receipts.append({
                "ref_id": attempt_id,
                "sha256": receipt.report_hash,
            })

        # transition: BARE_SUBMITTED → BARE_COLLECTED
        trans = self._transition("BARE_COLLECTED")
        if not trans.passed:
            return None, trans

        # ─── 4. 构建 BareBaseline ─────────────────────────────────────
        baseline = build_bare_baseline(
            baseline_id=baseline_id,
            question_release_ref_id=question_release.release_id,
            question_release_sha256=question_release.content_hash,
            bare_attempt_results=list(self._bare_results),
        )
        baseline_result = verify_bare_baseline(baseline)
        if not baseline_result.passed:
            return None, baseline_result
        self._baseline = baseline

        # transition: BARE_COLLECTED → BASELINE_BUILT
        trans = self._transition("BASELINE_BUILT")
        if not trans.passed:
            return None, trans

        # ─── 5. 判定 BareQualificationResult ──────────────────────────
        quals = [
            self._judge_qualification(r) for r in self._bare_results
        ]
        qualification = build_bare_qualification_result(
            result_id=result_id,
            bare_baseline_ref_id=baseline.baseline_id,
            bare_baseline_sha256=baseline.baseline_hash,
            problem_qualifications=quals,
        )
        qual_result = verify_bare_qualification_result(qualification)
        if not qual_result.passed:
            return None, qual_result
        self._qualification = qualification

        # transition: BASELINE_BUILT → QUALIFICATION_JUDGED
        trans = self._transition("QUALIFICATION_JUDGED")
        if not trans.passed:
            return None, trans

        # ─── 6. 产出 RunArtifactBundle ────────────────────────────────
        bundle = RunArtifactBundle(
            bundle_id=bundle_id,
            question_release_ref_and_hash=release_ref,
            bare_baseline_ref_and_hash={
                "ref_id": baseline.baseline_id,
                "sha256": baseline.baseline_hash,
            },
            qualification_result_ref_and_hash={
                "ref_id": qualification.result_id,
                "sha256": qualification.result_hash,
            },
            attempt_receipt_refs=list(self._receipts),
            problem_only=True,
            no_tell_hint=True,
        )
        self._bundle = bundle

        return bundle, VerificationResult(verdict="PASS")

    def _determine_bare_status(self, receipt: Any) -> str:
        """从 LaunchReceipt 判定 bare status。"""
        if receipt.failure_or_quarantine_state:
            if "QUARANTINE" in receipt.failure_or_quarantine_state.upper():
                return "QUARANTINE"
        if receipt.terminal_reason == "COMPLETED" and receipt.exit_code == 0:
            return "PASS"
        if receipt.terminal_reason == "TIMED_OUT":
            return "TIMEOUT"
        if receipt.terminal_reason in ("FAILED_PERMANENT", "CANCELLED", "TERMINATED"):
            return "FAIL"
        if receipt.terminal_reason == "BUDGET_EXCEEDED":
            return "TIMEOUT"
        return "FAIL"

    def _judge_qualification(self, bare_result: BareAttemptResult) -> ProblemQualification:
        """从 bare result 判定 qualification status。"""
        if bare_result.bare_status == "PASS":
            status = "QUALIFIED"
        elif bare_result.bare_status == "FAIL":
            status = "NOT_QUALIFIED"
        elif bare_result.bare_status == "TIMEOUT":
            status = "INCONCLUSIVE"
        else:  # QUARANTINE
            status = "QUARANTINED"
        return ProblemQualification(
            problem_ref_id=bare_result.problem_ref_id,
            qualification_status=status,
            bare_status_ref=bare_result.bare_status,
            not_p5_claim=True,
        )

    @property
    def bare_results(self) -> list[BareAttemptResult]:
        return list(self._bare_results)

    @property
    def baseline(self) -> BareBaseline | None:
        return self._baseline

    @property
    def qualification(self) -> BareQualificationResult | None:
        return self._qualification

    @property
    def bundle(self) -> RunArtifactBundle | None:
        return self._bundle


# ─── Blocker validators ─────────────────────────────────────────────────


def check_no_tell_hint_in_submission(
    submission: dict[str, Any],
) -> VerificationResult:
    """检查 bare submission 不含 Tell/Hint。

    blocker: Tell/Hint sneaked into bare submission → FAIL
    """
    errors: list[EC] = []
    details: list[str] = []

    submission_str = str(submission).lower()
    for keyword in _TELL_HINT_KEYWORDS:
        if keyword in submission_str:
            errors.append(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE)
            details.append(
                f"Tell/Hint keyword {keyword!r} found in bare submission"
            )

    # Check for tell/hint keys
    for key in submission:
        key_lower = key.lower()
        if any(kw in key_lower for kw in _TELL_HINT_KEYWORDS):
            errors.append(EC.QA1_TELL_HINT_SNEAKED_INTO_BARE)
            details.append(f"bare submission key {key!r} contains tell/hint")

    verdict = "PASS" if not errors else "FAIL"
    return VerificationResult(verdict=verdict, error_codes=errors, details=details)


def check_question_not_modified_after_bare(
    original_release_hash: str,
    current_release_hash: str,
) -> VerificationResult:
    """检查 question 在 bare results 后未被修改。

    blocker: Question modified after bare results → FAIL
    """
    if original_release_hash != current_release_hash:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.QA1_QUESTION_MODIFIED_AFTER_BARE],
            details=[
                f"question release hash changed after bare: "
                f"{original_release_hash[:8]}... → {current_release_hash[:8]}..."
            ],
        )
    return VerificationResult(verdict="PASS")


def check_no_successful_question_deleted(
    original_problem_refs: list[str],
    current_problem_refs: list[str],
    bare_results: list[BareAttemptResult],
) -> VerificationResult:
    """检查成功题未被选择性删除。

    blocker: Successful questions selectively deleted → FAIL
    """
    original_set = set(original_problem_refs)
    current_set = set(current_problem_refs)

    # Find problems that passed bare
    passed_problems = {
        r.problem_ref_id for r in bare_results if r.bare_status == "PASS"
    }

    # Check if any passed problem was deleted
    deleted = original_set - current_set
    deleted_passed = deleted & passed_problems

    if deleted_passed:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.QA1_SUCCESSFUL_QUESTION_DELETED],
            details=[
                f"successful questions deleted after bare: {deleted_passed}"
            ],
        )
    return VerificationResult(verdict="PASS")


def check_no_retry_until_fail(
    attempts_per_problem: dict[str, int],
) -> VerificationResult:
    """检查没有 retry-until-fail（对同一题重复生成直到得到 fail 结果）。

    blocker: Retry-until-fail → FAIL
    """
    retry_problems = {
        pid: count for pid, count in attempts_per_problem.items() if count > 1
    }
    if retry_problems:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.QA1_RETRY_UNTIL_FAIL],
            details=[
                f"retry-until-fail detected: {retry_problems} "
                f"(each problem should only have 1 bare attempt)"
            ],
        )
    return VerificationResult(verdict="PASS")


def check_no_bare_result_flowback_to_draft(
    draft_hash_before: str,
    draft_hash_after: str,
) -> VerificationResult:
    """检查 bare 结果未回流修改 question draft。

    blocker: bare results flow back to modify question draft → FAIL
    """
    if draft_hash_before != draft_hash_after:
        return VerificationResult(
            verdict="FAIL",
            error_codes=[EC.QA1_BARE_RESULT_FLOWS_BACK_TO_DRAFT],
            details=[
                f"draft hash changed after bare results: "
                f"{draft_hash_before[:8]}... → {draft_hash_after[:8]}... "
                f"(bare results must not flow back to modify draft)"
            ],
        )
    return VerificationResult(verdict="PASS")
