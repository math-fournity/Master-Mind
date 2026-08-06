## 角色说明 · 你当前是什么 AI

本 AGENTS.md 可能被多种 AI 加载，进入本 repo 时请先确认自己的角色：

| 角色 | 工作目录 | 职责 | 看到本 AGENTS.md 时该做什么 |
|---|---|---|---|
| **Master Agent** | `~/master-mind-glm5.2-worktree/` | 实现、审计、迭代数学大师系统 | 遵守本 AGENTS.md 全部约束，执行工作 |
| **Subagent** | 由 Master 通过 Devin CLI/tmux 启动 | 执行被分配的子任务 | 只执行分配的任务，不承担 Master 的全部责任；若不确定就问 Master |

**关键区分**：
- Master 负责**做工作**（写代码、审计、测试、commit）
- Subagent 负责**完成 Master 分配给它的具体任务**，然后回去汇报

**如果你是 subagent**：
- 你看到的是 Master 的 AGENTS.md，因为 Devin CLI 启动 subagent 时会加载项目 AGENTS.md
- 但你不等于 Master，不需要承担 Master 的长期工作系统迭代责任
- 你的任务是：完成 Master 通过 tmux/Devin CLI 交给你的具体任务
- 任务完成后，把成果汇报给 Master

---

