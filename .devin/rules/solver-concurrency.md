# Solver AI 并发约束

**硬约束**：批量测试时同时运行的 Solver AI（devin cli 实例）**10-30个**，不超过30。树生长引擎实验时最多2个。

## 规则

1. **批量测试并发上限30**——通过 `batch_problem_runner.py` 启动的批量测试，concurrency参数设10-30。
2. **树生长引擎并发上限2**——`tree_engine.py` 中的并发AI管理用 `MAX_CONCURRENT = 2`。
3. **检查并发数**——`tmux list-sessions | grep "harness-" | grep -v dbmon | wc -l`
4. **并发调整**——`batch_problem_runner.py set-concurrency --batch-id <id> --concurrency <N>`

## 并发上限经验（2026-08-12实测）

| 并发 | 连接错误率 | 性质 | 结论 |
|---|---|---|---|
| 10 | ~0% | 稳定 | 最安全 |
| 30 | ~6.7% | 偶发瞬时断连，Solver可恢复 | 可接受 |
| 60 | 51% | 致命雪崩，session直接死 | 禁止 |

详见 `.devin/rules/solver-batch-health-check.md`。

## 循环驱动下的动态分配（树生长引擎）

**静态编排**（当前实现）：30个任务预先排好，用2并发批次完成。这是POC-VMS-2的模式——循环只转了半圈。

**动态编排**（目标实现）：AI终止后在叶节点检索出新方向，新方向动态加入task_queue。任务数不固定——循环每转一圈，task_queue可能增长。2并发额度在动态任务间分配：
- AI-1终止 → 叶节点检索出3个方向 → 3个新任务加入queue
- 2并发额度中空出1个 → 从queue取1个启动
- AI-2终止 → 叶节点检索出2个方向 → 2个新任务加入queue
- ...循环直到所有problem solved或queue空且无running AI

**动态编排下2并发仍然成立**——任何时刻最多2个AI同时运行，只是任务来源从静态变为动态（循环驱动）。

## 适用于

- 所有通过 `solver-harness launch` 启动的 Solver AI
- 树生长引擎（tree_engine.py）——静态编排和动态编排都适用
- 批量测试脚本
- A/B 对照实验
