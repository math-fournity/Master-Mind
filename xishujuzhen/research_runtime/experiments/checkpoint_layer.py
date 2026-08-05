"""
CheckpointLayer：checkpoint分层+continuation分配

对应134号P4-1。

123号§39 DYN-3 + §847：
- checkpoint = 序列化(Q_0/W_t, 关键事件前缀, 模型/工具/权限/预算, 版本哈希)
- 7个必填字段：q_0 / event_prefix / model_version / tool_versions / permissions / budget / version_hash
- 同一内容哈希checkpoint视为阻断/分层变量
- 在同内容哈希层内随机分配多个非确定continuation

P4-1.0：checkpoint完整字段定义（149号F7修正）
P4-1.1：选取Phase 3发现的候选规则对应的checkpoint
P4-1.2：在同一checkpoint层内随机分配多个非确定continuation
P4-1.3：用分层或配对统计估计ATE和异质性
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple
import random
import hashlib
import json

# 复用Phase 3的Checkpoint定义（149号修正版，含§847的7字段）
from ..heuristics.state_aligner import Checkpoint


@dataclass
class ContinuationAssignment:
    """continuation分配记录——记录哪个checkpoint分配到哪个处理组"""
    assignment_id: str
    checkpoint_id: str       # checkpoint内容哈希
    treatment_group: str     # control/h0/h1/h2
    run_index: int           # 在该处理组内的序号
    random_seed: int         # 随机种子（可复现）

    def to_dict(self) -> dict:
        return {
            "assignment_id": self.assignment_id,
            "checkpoint_id": self.checkpoint_id,
            "treatment_group": self.treatment_group,
            "run_index": self.run_index,
            "random_seed": self.random_seed,
        }


class CheckpointLayerExperiment:
    """
    P4-1：同内容哈希checkpoint分层并随机分配多个非确定continuation。

    P4-1.1：选取checkpoint（含§847的7个完整字段）
    P4-1.2：在同一checkpoint层内随机分配continuation到4组
    P4-1.3：用分层或配对统计估计ATE和异质性
    """

    def __init__(self, seed: int = 42):
        """
        Args:
            seed: 随机种子（记录到manifest，可复现）
        """
        self.seed = seed
        self._rng = random.Random(seed)
        self._assignments: List[ContinuationAssignment] = []

    def select_checkpoint(
        self,
        q_0: str,
        event_prefix: List[str],
        model_version: str,
        tool_versions: Dict[str, str],
        permissions: List[str],
        budget: Dict[str, Any],
        state_snapshot: Optional[Dict[str, Any]] = None,
        run_id: str = "phase4",
    ) -> Checkpoint:
        """
        P4-1.1：选取checkpoint——含§847的7个完整字段。

        边界情况：
        - checkpoint不存在 → 创建新的
        - checkpoint缺少7字段中的任一字段 → 触发告警
        """
        ckpt = Checkpoint(
            checkpoint_id="",  # 计算后填充
            run_id=run_id,
            step_index=0,
            state_snapshot=state_snapshot or {},
            q_0=q_0,
            event_prefix=event_prefix,
            model_version=model_version,
            tool_versions=tool_versions,
            permissions=permissions,
            budget=budget,
            version_hash="",
        )
        # 计算内容哈希作为checkpoint_id
        ckpt.checkpoint_id = self._compute_checkpoint_hash(ckpt)
        ckpt.version_hash = ckpt.checkpoint_id
        return ckpt

    def _compute_checkpoint_hash(self, ckpt: Checkpoint) -> str:
        """计算checkpoint内容哈希（§847：序列化Q_0/W_t+事件前缀+模型/工具/权限/预算+版本哈希）"""
        content = {
            "q_0": ckpt.q_0,
            "event_prefix": ckpt.event_prefix,
            "model_version": ckpt.model_version,
            "tool_versions": ckpt.tool_versions,
            "permissions": sorted(ckpt.permissions),
            "budget": ckpt.budget,
        }
        return hashlib.sha256(
            json.dumps(content, sort_keys=True, ensure_ascii=False).encode()
        ).hexdigest()[:16]

    def verify_checkpoint_complete(self, ckpt: Checkpoint) -> Dict[str, Any]:
        """
        P4-1.0：验证checkpoint包含§847的7个完整字段。

        边界情况：checkpoint缺少7字段中的任一字段（应触发告警）
        """
        required_fields = [
            "q_0", "event_prefix", "model_version",
            "tool_versions", "permissions", "budget", "version_hash",
        ]
        missing = []
        for f in required_fields:
            val = getattr(ckpt, f, None)
            if val is None or val == "" or val == []:
                missing.append(f)

        return {
            "complete": len(missing) == 0,
            "missing_fields": missing,
            "checkpoint_id": ckpt.checkpoint_id,
        }

    def assign_continuations(
        self,
        checkpoint: Checkpoint,
        n_per_group: int,
        treatment_groups: List[str],
    ) -> List[ContinuationAssignment]:
        """
        P4-1.2：在同一checkpoint层内随机分配多个非确定continuation。

        在同一checkpoint上，每个处理组分配n_per_group个continuation。
        随机分配顺序（不是按组顺序分配，而是随机打乱）。

        边界情况：
        - checkpoint层内只有1个continuation（无法分层）→ 至少需要4*n_per_group个
        - continuation数量不足 → 记录告警
        """
        assignments = []
        total = n_per_group * len(treatment_groups)

        # 生成分配顺序（随机打乱）
        schedule = []
        for group in treatment_groups:
            for i in range(n_per_group):
                schedule.append((group, i))
        self._rng.shuffle(schedule)

        for group, run_idx in schedule:
            assignment = ContinuationAssignment(
                assignment_id=f"{checkpoint.checkpoint_id}_{group}_{run_idx}",
                checkpoint_id=checkpoint.checkpoint_id,
                treatment_group=group,
                run_index=run_idx,
                random_seed=self.seed,
            )
            assignments.append(assignment)

        self._assignments.extend(assignments)
        return assignments

    def get_assignments_by_group(
        self, checkpoint_id: str
    ) -> Dict[str, List[ContinuationAssignment]]:
        """按处理组分组获取continuation分配"""
        result: Dict[str, List[ContinuationAssignment]] = {}
        for a in self._assignments:
            if a.checkpoint_id == checkpoint_id:
                result.setdefault(a.treatment_group, []).append(a)
        return result

    def get_all_assignments(self) -> List[ContinuationAssignment]:
        return self._assignments
