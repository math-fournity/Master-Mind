# Solver AI 并发约束

**硬约束**：同时运行的 Solver AI（devin cli 实例）最多 **2 个**。

## 规则

1. **任何时刻最多 2 个并发 AI**——通过 `solver-harness launch` 启动的 devin cli 实例，同时运行数不得超过 2。
2. **有 N 个任务时用 2 个 AI 编排完成**——如果有 30 个 AI 任务要做，不能同时启动 30 个，而是用 2 个并发额度，串行批次完成：
   - 批次1：启动 AI-1 + AI-2
   - 等 AI-1 完成 → 启动 AI-3（保持 2 个并发）
   - 等 AI-2 完成 → 启动 AI-4
   - ...直到所有任务完成
3. **检查并发数**——启动新 AI 前必须检查当前运行的 AI 数：
   ```bash
   tmux list-sessions | grep "harness-vms" | grep -v dbmon | wc -l
   ```
   如果结果 >= 2，等待其中一个完成后再启动新的。
4. **树生长引擎必须遵守此约束**——`tree_engine.py` 中的并发 AI 管理必须用 `MAX_CONCURRENT = 2`，不能用 30。

## 为什么

- 每个 devin cli 实例消耗大量 API token 和系统资源
- 30 个并发会导致 API 限速、连接失败、系统资源耗尽
- 2 个并发是经过验证的稳定配置

## 适用于

- 所有通过 `solver-harness launch` 启动的 Solver AI
- 树生长引擎（tree_engine.py）
- 批量测试脚本
- A/B 对照实验
