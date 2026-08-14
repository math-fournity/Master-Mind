"""IndependenceEnforcer — 作者/审稿独立性、judge 视图隔离、伪独立性检测。

来自 docs/implementation/09-phase-pipeline-p0-p9.md P6 节和
docs/implementation/05-execution-ports-and-carriers.md：

独立性硬约束：
- 作者和审稿者不能是同一 session（同会话审稿 = blocker）
- Judge 不能读取其他 judge 的 view（judge 读越权 view = blocker）
- 同模型 fresh session ≠ 不同模型独立性（伪独立性 = blocker）
- P6 三个独立审计各自 blinding，分别 seal 后组装

SIDE_EFFECT_FREE：纯内存实现。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ...contracts.errors import (
    CW_INDEPENDENCE_KINDS,
    VerificationErrorCode as EC,
)
from ...contracts.completion_contract import VerificationResult


@dataclass(frozen=True)
class WorkerSession:
    """单个 worker 的 session 标识。

    model_uid + session_id 唯一标识一次独立执行。
    carrier_id 标识执行载体（devin / codex / ...）。
    """

    worker_id: str
    role_type_id: str
    model_uid: str
    session_id: str
    carrier_id: str
    view_id: str  # 该 worker 被授予的 view（P6 blinding）

    def to_dict(self) -> dict[str, Any]:
        return {
            "worker_id": self.worker_id,
            "role_type_id": self.role_type_id,
            "model_uid": self.model_uid,
            "session_id": self.session_id,
            "carrier_id": self.carrier_id,
            "view_id": self.view_id,
        }


@dataclass(frozen=True)
class IndependenceViolation:
    """独立性违规记录。"""

    error_code: EC
    detail: str
    worker_a: str  # worker_id
    worker_b: str  # worker_id（如果是配对违规）
    independence_kind: str  # CW_INDEPENDENCE_KINDS 中的种类

    def to_dict(self) -> dict[str, Any]:
        return {
            "error_code": self.error_code.value,
            "detail": self.detail,
            "worker_a": self.worker_a,
            "worker_b": self.worker_b,
            "independence_kind": self.independence_kind,
        }


@dataclass
class IndependenceEnforcer:
    """IndependenceEnforcer — 独立性强制器。

    检查：
    1. 作者和审稿者不能是同一 session（CW_SAME_SESSION_AUTHOR_REVIEWER）
    2. Judge 不能读取其他 judge 的 view（CW_JUDGE_READ_UNAUTHORIZED_VIEW）
    3. 同模型 fresh session ≠ 不同模型独立性（CW_FAKE_INDEPENDENCE_SAME_MODEL）
    4. P6 三个审计各自独立 session + blinding
    """

    # 已注册的 worker sessions
    sessions: list[WorkerSession] = field(default_factory=list)
    # worker_id → 授权读取的 view_id 集合
    authorized_views: dict[str, set[str]] = field(default_factory=dict)
    # 记录作者-审稿者配对关系
    author_reviewer_pairs: list[tuple[str, str]] = field(default_factory=list)

    def register_session(self, session: WorkerSession) -> None:
        """注册一个 worker session。"""
        self.sessions.append(session)
        if session.worker_id not in self.authorized_views:
            self.authorized_views[session.worker_id] = {session.view_id}

    def authorize_view(self, worker_id: str, view_id: str) -> None:
        """授权 worker 读取某个 view。"""
        self.authorized_views.setdefault(worker_id, set()).add(view_id)

    def record_author_reviewer(self, author_id: str, reviewer_id: str) -> None:
        """记录作者-审稿者配对。"""
        self.author_reviewer_pairs.append((author_id, reviewer_id))

    def check_author_reviewer_independence(
        self,
        author: WorkerSession,
        reviewer: WorkerSession,
    ) -> list[IndependenceViolation]:
        """检查作者和审稿者的独立性。

        违规：
        1. 同 session → CW_SAME_SESSION_AUTHOR_REVIEWER
        2. 同模型 fresh session 声称不同模型独立性 → CW_FAKE_INDEPENDENCE_SAME_MODEL
        """
        violations: list[IndependenceViolation] = []

        # 1. 同 session
        if author.session_id == reviewer.session_id:
            violations.append(
                IndependenceViolation(
                    error_code=EC.CW_SAME_SESSION_AUTHOR_REVIEWER,
                    detail=(
                        f"author {author.worker_id} and reviewer {reviewer.worker_id} "
                        f"share session {author.session_id}"
                    ),
                    worker_a=author.worker_id,
                    worker_b=reviewer.worker_id,
                    independence_kind="DIFFERENT_SESSION",
                )
            )

        # 2. 同模型 fresh session 声称不同模型独立性
        # 如果两个 worker 声称是不同模型但 model_uid 相同，是伪独立性
        # （这里检查的是：如果声称 DIFFERENT_MODEL 但实际 model_uid 相同）
        # 这个检查由 check_fake_independence 单独处理

        return violations

    def check_judge_view_isolation(
        self,
        judge: WorkerSession,
        requested_view_id: str,
    ) -> list[IndependenceViolation]:
        """检查 judge 是否只读取授权的 view。

        P6 三个审计各自 blinding，judge 不能读取其他 judge 的 view。
        """
        violations: list[IndependenceViolation] = []
        authorized = self.authorized_views.get(judge.worker_id, set())

        if requested_view_id not in authorized:
            violations.append(
                IndependenceViolation(
                    error_code=EC.CW_JUDGE_READ_UNAUTHORIZED_VIEW,
                    detail=(
                        f"judge {judge.worker_id} (role={judge.role_type_id}) "
                        f"attempted to read view {requested_view_id}, "
                        f"authorized views: {sorted(authorized)}"
                    ),
                    worker_a=judge.worker_id,
                    worker_b="",
                    independence_kind="BLINDED_VIEW",
                )
            )

        return violations

    def check_fake_independence(
        self,
        worker_a: WorkerSession,
        worker_b: WorkerSession,
        *,
        claimed_kind: str = "DIFFERENT_MODEL",
    ) -> list[IndependenceViolation]:
        """检查伪独立性。

        同模型 fresh session ≠ 不同模型独立性。
        如果声称 DIFFERENT_MODEL 但 model_uid 相同 → 伪独立性。
        """
        violations: list[IndependenceViolation] = []

        if claimed_kind == "DIFFERENT_MODEL":
            if worker_a.model_uid == worker_b.model_uid:
                violations.append(
                    IndependenceViolation(
                        error_code=EC.CW_FAKE_INDEPENDENCE_SAME_MODEL,
                        detail=(
                            f"workers {worker_a.worker_id} and {worker_b.worker_id} "
                            f"claim DIFFERENT_MODEL independence but share model_uid "
                            f"{worker_a.model_uid}; same model fresh session != "
                            f"different model independence"
                        ),
                        worker_a=worker_a.worker_id,
                        worker_b=worker_b.worker_id,
                        independence_kind="SAME_MODEL_FRESH_SESSION",
                    )
                )

        return violations

    def check_p6_independence(
        self,
        auditors: list[WorkerSession],
    ) -> list[IndependenceViolation]:
        """检查 P6 三个独立审计的独立性。

        每个审计必须有独立 session、独立 view（blinding）。
        三个审计之间不能共享 session。
        """
        violations: list[IndependenceViolation] = []

        if len(auditors) < 2:
            return violations

        # 检查两两之间
        for i in range(len(auditors)):
            for j in range(i + 1, len(auditors)):
                a = auditors[i]
                b = auditors[j]

                # 同 session
                if a.session_id == b.session_id:
                    violations.append(
                        IndependenceViolation(
                            error_code=EC.CW_WORKER_NOT_INDEPENDENT,
                            detail=(
                                f"P6 auditors {a.worker_id} and {b.worker_id} "
                                f"share session {a.session_id}"
                            ),
                            worker_a=a.worker_id,
                            worker_b=b.worker_id,
                            independence_kind="DIFFERENT_SESSION",
                        )
                    )

                # 同 view（blinding 违规）
                if a.view_id == b.view_id:
                    violations.append(
                        IndependenceViolation(
                            error_code=EC.CW_BLINDING_VIOLATED,
                            detail=(
                                f"P6 auditors {a.worker_id} and {b.worker_id} "
                                f"share view {a.view_id}; blinding violated"
                            ),
                            worker_a=a.worker_id,
                            worker_b=b.worker_id,
                            independence_kind="BLINDED_VIEW",
                        )
                    )

        return violations

    def check_all(self) -> list[IndependenceViolation]:
        """检查所有已注册的约束。"""
        violations: list[IndependenceViolation] = []

        # 检查所有作者-审稿者配对
        session_map = {s.worker_id: s for s in self.sessions}
        for author_id, reviewer_id in self.author_reviewer_pairs:
            author = session_map.get(author_id)
            reviewer = session_map.get(reviewer_id)
            if author and reviewer:
                violations.extend(
                    self.check_author_reviewer_independence(author, reviewer)
                )

        # 检查 P6 审计独立性（同 role_type_id 的 P6 角色）
        p6_roles = {"process_auditor", "proof_judge", "leakage_auditor"}
        p6_sessions = [s for s in self.sessions if s.role_type_id in p6_roles]
        if len(p6_sessions) >= 2:
            violations.extend(self.check_p6_independence(p6_sessions))

        return violations

    def verify_independence(self) -> VerificationResult:
        """验证独立性，返回 VerificationResult。"""
        violations = self.check_all()
        errors = [v.error_code for v in violations]
        details = [v.detail for v in violations]
        verdict = "PASS" if not errors else "FAIL"
        return VerificationResult(verdict=verdict, error_codes=errors, details=details)
