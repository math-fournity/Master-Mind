"""
Q_0任务实例化：128号§3冻结的Ramsey案例

对应132号P2-1。

冻结声明（128号§3.4）：
- Ramsey修正版材料冻结为只读实验基底
- 这是新protocol的候选题族（NI-5），不是继续POC-6
- 不能反向把119号结论升级

Q_0在运行时保持冻结（127号§1冻结声明）。
"""

import copy
from ..models.task import Task, TaskType


# 冻结标记——用于运行时检查Q_0未被修改
_Q0_FROZEN_HASH = None


def create_q0_ramsey() -> Task:
    """
    创建Q_0：Ramsey C_5下界猜测任务。

    来源：128号§3.1案例描述。
    任务类型：conjecture（猜测R_k(C_5)下界）。
    成功条件：按123号§23的conjecture类型——非重复、可证伪、通过初筛且未被反例否定的候选。
    """
    return Task(
        task_id="Q_0_ramsey_c5",
        type=TaskType.CONJECTURE,
        domain="combinatorics/ramsey_theory",
        objects=[
            "R_k(C_5)",       # 目标：猜测R_k(C_5)下界
            "C_5",            # 奇环C_5
            "C_3",            # 三角形C_3（已知下界参照）
            "k",              # 参数k
            "迭代对数",        # 上界相关工具
        ],
        premises=[
            "R_k(C_3) ≥ k^{k/3-o(k)}",       # 已知C_3下界
            "C_5比C_3更难避免",                # 结构观察
            "上界与迭代对数定义",              # 已知上界
        ],
        goal="猜测R_k(C_5)下界",
        success_conditions=[
            # 123号§23 conjecture类型的进展定义：
            "候选是非重复的（与已知R_k(C_3)下界形式不同）",
            "候选是可证伪的（有明确的数学陈述，可被反例否定）",
            "候选通过初筛（结构合理性检查）",
            "候选未被反例否定",
        ],
        stop_conditions=[
            "预算耗尽",
            "反复改变指数无进展（平面环路）",
            "策略耗尽",
        ],
        failure_conditions=[
            "只改指数不分析底数（128号§3.1失败轨迹）",
            "给出答案等价内容（128号§3.2禁止级别）",
        ],
    )


def _compute_task_hash(task: Task) -> str:
    """计算Task的内容哈希，用于冻结检查"""
    import hashlib
    import json
    d = task.to_dict()
    # 排序键确保确定性
    return hashlib.sha256(
        json.dumps(d, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()


# 冻结的Q_0实例（运行时保持冻结）
Q0_RAMSEY = create_q0_ramsey()
_Q0_FROZEN_HASH = _compute_task_hash(Q0_RAMSEY)


def verify_q0_frozen(task: Task = None) -> bool:
    """
    验证Q_0在运行时保持冻结（P2-1.COMP3）。

    检查传入的task（默认Q0_RAMSEY）的内容哈希是否与冻结时一致。
    """
    if task is None:
        task = Q0_RAMSEY
    return _compute_task_hash(task) == _Q0_FROZEN_HASH
