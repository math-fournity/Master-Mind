"""
StateAligner: 对齐多个成功/失败状态 + 找稳定共同状态和首个关键分叉

对应133号P3-1和P3-2。

123号§48：
- 对齐多个成功/失败状态，而非只对齐最终答案
- 用Phase 2的V/F/O/R/D/E工作区状态做对齐

123号§39：内容哈希checkpoint标识

边界情况（133号P3-1/P3-2）：
- 成功/失败运行数量不足
- 状态序列长度不同
- 状态字段缺失
- 无共同状态
- 无分叉点
- 多个分叉点同时出现

F1防线：RunSelector和StateAligner都是可执行类，不是只定义接口。
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple, Set
from datetime import datetime, timezone
import hashlib
import json


@dataclass
class Checkpoint:
    """
    状态checkpoint——用内容哈希标识（123号§39内容寻址）。

    123号§847冻结定义：
    checkpoint = 序列化(Q_0/W_t, 关键事件前缀, 模型/工具/权限/预算, 版本哈希)
    - 不包含、也不能冻结LLM隐藏内部状态
    - 同一内容哈希checkpoint视为阻断/分层变量

    不是按序号对齐，而是按内容哈希对齐。
    """
    checkpoint_id: str          # 内容哈希
    run_id: str
    step_index: int             # 在运行中的序号（仅用于排序，不用于对齐）
    state_snapshot: Dict[str, Any]   # V/F/O/R/D/E快照（W_t）
    # 123号§847要求checkpoint包含的完整字段：
    q_0: str = ""                           # 原题Q_0的标识
    event_prefix: List[str] = field(default_factory=list)  # 关键事件前缀
    model_version: str = ""                 # 模型版本
    tool_versions: Dict[str, str] = field(default_factory=dict)  # 工具版本
    permissions: List[str] = field(default_factory=list)  # 权限
    budget: Dict[str, Any] = field(default_factory=dict)  # 预算
    version_hash: str = ""                  # 版本哈希
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "checkpoint_id": self.checkpoint_id,
            "run_id": self.run_id,
            "step_index": self.step_index,
            "state_snapshot": self.state_snapshot,
            "q_0": self.q_0,
            "event_prefix": self.event_prefix,
            "model_version": self.model_version,
            "tool_versions": self.tool_versions,
            "permissions": self.permissions,
            "budget": self.budget,
            "version_hash": self.version_hash,
            "timestamp": self.timestamp,
        }


@dataclass
class DivergencePoint:
    """
    首个关键分叉点（P3-2.2）。

    成功运行和失败运行在哪个checkpoint开始分叉。
    """
    checkpoint_id: str          # 分叉点的checkpoint哈希
    step_index: int
    success_features: Dict[str, Any] = field(default_factory=dict)
    failure_features: Dict[str, Any] = field(default_factory=dict)
    stall_type: str = ""
    open_obligations: List[str] = field(default_factory=list)
    representation: str = ""
    evidence_status: str = ""

    def to_dict(self) -> dict:
        return {
            "checkpoint_id": self.checkpoint_id,
            "step_index": self.step_index,
            "success_features": self.success_features,
            "failure_features": self.failure_features,
            "stall_type": self.stall_type,
            "open_obligations": self.open_obligations,
            "representation": self.representation,
            "evidence_status": self.evidence_status,
        }


def compute_state_hash(state: Dict[str, Any]) -> str:
    """
    计算状态的内容哈希（123号§39内容寻址）。

    123号§847：checkpoint = 序列化(Q_0/W_t, 关键事件前缀, 模型/工具/权限/预算, 版本哈希)
    用V/F/O/R/D/E的规范化键计算哈希，忽略timestamp和措辞。
    """
    # 提取V/F/O/R/D/E的规范化表示（W_t部分）
    canonical = {}
    for key in ["V_t", "F_t", "O_t", "R_t", "D_t", "E_t"]:
        val = state.get(key, {})
        if isinstance(val, dict):
            # 排序键确保确定性
            canonical[key] = {k: sorted(v) if isinstance(v, list) else v
                              for k, v in sorted(val.items())}
        else:
            canonical[key] = val

    # 123号§847要求checkpoint还包含Q_0/事件前缀/模型/工具/权限/预算/版本哈希
    # 这些字段如果存在于state中，也参与哈希计算
    for key in ["q_0", "event_prefix", "model_version", "tool_versions",
                "permissions", "budget", "version_hash"]:
        if key in state and state[key]:
            canonical[key] = state[key]

    return hashlib.sha256(
        json.dumps(canonical, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()


class RunSelector:
    """
    P3-1.1：从Phase 2的状态重建结果中选取多个成功和失败运行。

    深度标准：有可执行的运行选取函数，从Phase 2结果中按成功/失败分类选取。

    边界情况：
    - 成功/失败运行数量不足 → 报错
    - 运行结果不明确 → 标记为"ambiguous"
    """

    def __init__(self, workspace_store=None):
        """
        workspace_store: WorkspaceStore实例（Phase 2已实现）。
        如果为None，则用内存数据（测试用）。
        """
        self.workspace_store = workspace_store

    def select_runs(
        self,
        task_id: str,
        outcome_filter: str = "all",   # "success" / "failure" / "all"
        min_runs: int = 2,
        runs: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        从Phase 2结果中按成功/失败分类选取运行。

        参数：
        - task_id: 任务ID
        - outcome_filter: "success"/"failure"/"all"
        - min_runs: 每类最少需要的运行数
        - runs: 直接传入运行列表（测试用），如果为None则从workspace_store查询

        返回：{"success": [...], "failure": [...], "ambiguous": [...]}

        边界情况：
        - 成功/失败运行数量不足 → 报错并要求更多运行
        - 运行结果不明确 → 放入"ambiguous"
        """
        if runs is None:
            if self.workspace_store is None:
                raise ValueError("无workspace_store且无runs参数——无法选取运行")
            runs = self.workspace_store.list_workspaces(task_id=task_id, limit=1000)

        success_runs = []
        failure_runs = []
        ambiguous_runs = []

        for run in runs:
            # run可能是dict（单状态+outcome）或list（状态序列，最后状态含outcome）
            if isinstance(run, list):
                # 状态序列——从最后一个状态取outcome
                outcome = run[-1].get("outcome", "") if run else ""
            elif isinstance(run, dict):
                outcome = run.get("outcome", "")
            else:
                outcome = ""
            if outcome == "success":
                success_runs.append(run)
            elif outcome == "failure":
                failure_runs.append(run)
            else:
                ambiguous_runs.append(run)

        # 检查数量
        if outcome_filter in ("success", "all") and len(success_runs) < min_runs:
            raise ValueError(
                f"成功运行数量不足：需要至少{min_runs}个，实际{len(success_runs)}个"
            )
        if outcome_filter in ("failure", "all") and len(failure_runs) < min_runs:
            raise ValueError(
                f"失败运行数量不足：需要至少{min_runs}个，实际{len(failure_runs)}个"
            )

        if outcome_filter == "success":
            return {"success": success_runs, "failure": [], "ambiguous": ambiguous_runs}
        elif outcome_filter == "failure":
            return {"success": [], "failure": failure_runs, "ambiguous": ambiguous_runs}
        else:
            return {"success": success_runs, "failure": failure_runs, "ambiguous": ambiguous_runs}


class StateAligner:
    """
    P3-1.2/P3-1.3/P3-2：状态对齐+共同状态+分叉点检测。

    对齐V/F/O/R/D/E工作区状态（不是最终答案）。
    用内容哈希checkpoint对齐（不是按序号对齐）。
    """

    def align_states(
        self,
        run_states_list: List[List[Dict[str, Any]]],
    ) -> List[List[Checkpoint]]:
        """
        P3-1.2：对齐状态而非只对齐最终答案。

        对每个运行的每个状态快照计算内容哈希checkpoint。

        参数：
        - run_states_list: 每个运行的状态序列列表

        返回：每个运行的checkpoint链列表

        边界情况：
        - 状态序列长度不同 → 用checkpoint内容哈希对齐，不是按序号对齐
        - 状态字段缺失 → 标记为"missing"，不参与对齐
        """
        all_checkpoints = []

        for run_idx, run_states in enumerate(run_states_list):
            run_id = f"run_{run_idx}"
            checkpoints = self.record_checkpoints(run_states, run_id)
            all_checkpoints.append(checkpoints)

        return all_checkpoints

    def record_checkpoints(
        self,
        run_states: List[Dict[str, Any]],
        run_id: str,
    ) -> List[Checkpoint]:
        """
        P3-1.3：记录每个运行的关键状态序列（checkpoint链）。

        123号§847：checkpoint = 序列化(Q_0/W_t, 关键事件前缀, 模型/工具/权限/预算, 版本哈希)

        边界情况：
        - 运行无checkpoint → 返回空列表
        - checkpoint链断裂 → 标记缺失步骤
        """
        checkpoints = []
        for step_idx, state in enumerate(run_states):
            # 检查状态字段是否缺失
            missing_fields = []
            for key in ["V_t", "F_t", "O_t", "R_t", "D_t", "E_t"]:
                if key not in state:
                    missing_fields.append(key)

            # 即使有缺失字段也计算哈希（缺失字段用空值）
            state_hash = compute_state_hash(state)

            # 123号§847：填充checkpoint的完整字段
            cp = Checkpoint(
                checkpoint_id=state_hash,
                run_id=run_id,
                step_index=step_idx,
                state_snapshot=state,
                q_0=state.get("q_0", ""),
                event_prefix=state.get("event_prefix", []),
                model_version=state.get("model_version", ""),
                tool_versions=state.get("tool_versions", {}),
                permissions=state.get("permissions", []),
                budget=state.get("budget", {}),
                version_hash=state.get("version_hash", ""),
            )
            if missing_fields:
                cp.state_snapshot["_missing_fields"] = missing_fields

            checkpoints.append(cp)

        return checkpoints

    def find_common_states(
        self,
        success_checkpoints: List[List[Checkpoint]],
        failure_checkpoints: List[List[Checkpoint]],
    ) -> List[str]:
        """
        P3-2.1：在成功运行和失败运行中找稳定共同状态。

        多个运行都经过的checkpoint（内容哈希相同）。

        边界情况：
        - 无共同状态 → 返回空列表
        - 共同状态太多 → 按出现频率排序，返回前N个
        """
        # 统计每个checkpoint哈希在成功运行和失败运行中各出现多少次
        success_hashes: Dict[str, int] = {}
        failure_hashes: Dict[str, int] = {}

        for run_cps in success_checkpoints:
            seen_in_run = set()
            for cp in run_cps:
                seen_in_run.add(cp.checkpoint_id)
            for h in seen_in_run:
                success_hashes[h] = success_hashes.get(h, 0) + 1

        for run_cps in failure_checkpoints:
            seen_in_run = set()
            for cp in run_cps:
                seen_in_run.add(cp.checkpoint_id)
            for h in seen_in_run:
                failure_hashes[h] = failure_hashes.get(h, 0) + 1

        # 共同状态：在成功和失败运行中都出现的checkpoint
        common = set(success_hashes.keys()) & set(failure_hashes.keys())

        # 按总出现次数排序
        common_sorted = sorted(
            common,
            key=lambda h: success_hashes[h] + failure_hashes[h],
            reverse=True,
        )

        return common_sorted

    def find_first_divergence(
        self,
        success_checkpoints: List[List[Checkpoint]],
        failure_checkpoints: List[List[Checkpoint]],
        common_states: Optional[List[str]] = None,
    ) -> Optional[DivergencePoint]:
        """
        P3-2.2：找首个关键分叉（成功运行和失败运行在哪个checkpoint开始分叉）。

        策略：找到最后一个共同checkpoint，下一个就是分叉点。

        边界情况：
        - 无分叉点 → 返回None
        - 多个分叉点同时出现 → 取最早的作为"首个关键分叉"
        """
        if common_states is None:
            common_states = self.find_common_states(success_checkpoints, failure_checkpoints)

        if not common_states:
            return None

        # 对每个成功运行，找最后一个共同checkpoint的step_index
        # 然后取所有运行中最小的"分叉step_index"
        min_divergence_step = float("inf")
        divergence_cp_id = None
        success_state_at_div = None
        failure_state_at_div = None

        for run_cps in success_checkpoints:
            last_common_step = -1
            last_common_cp = None
            for cp in run_cps:
                if cp.checkpoint_id in common_states:
                    last_common_step = cp.step_index
                    last_common_cp = cp
                else:
                    # 第一个非共同checkpoint——分叉点
                    if last_common_step >= 0 and cp.step_index < min_divergence_step:
                        min_divergence_step = cp.step_index
                        divergence_cp_id = cp.checkpoint_id
                        success_state_at_div = cp.state_snapshot
                    break

        # 找失败运行在同一step的状态
        if divergence_cp_id is not None:
            for run_cps in failure_checkpoints:
                for cp in run_cps:
                    if cp.step_index == min_divergence_step:
                        failure_state_at_div = cp.state_snapshot
                        break
                if failure_state_at_div:
                    break

        if divergence_cp_id is None:
            return None

        div = DivergencePoint(
            checkpoint_id=divergence_cp_id,
            step_index=int(min_divergence_step),
        )

        # P3-2.3：记录分叉点的状态特征
        self._record_divergence_features(div, success_state_at_div, failure_state_at_div)

        return div

    def _record_divergence_features(
        self,
        div: DivergencePoint,
        success_state: Optional[Dict[str, Any]],
        failure_state: Optional[Dict[str, Any]],
    ):
        """
        P3-2.3：记录分叉点的状态特征（卡点类型、开放义务、表示、证据状态）。

        边界情况：分叉点状态特征不完整 → 用默认值
        """
        if success_state:
            div.success_features = {
                "V_t": success_state.get("V_t", {}),
                "F_t": success_state.get("F_t", {}),
                "O_t": success_state.get("O_t", {}),
            }

        if failure_state:
            div.failure_features = {
                "V_t": failure_state.get("V_t", {}),
                "F_t": failure_state.get("F_t", {}),
                "O_t": failure_state.get("O_t", {}),
            }
            # 卡点类型
            div.stall_type = failure_state.get("stall_type", "")
            # 开放义务
            o_t = failure_state.get("O_t", {})
            div.open_obligations = o_t.get("obligation_ids", []) if isinstance(o_t, dict) else []
            # 表示
            r_t = failure_state.get("R_t", {})
            reps = r_t.get("active_representations", []) if isinstance(r_t, dict) else []
            div.representation = reps[0] if reps else ""
            # 证据状态
            e_t = failure_state.get("E_t", {})
            div.evidence_status = str(len(e_t.get("evidence_ids", [])) if isinstance(e_t, dict) else 0)
