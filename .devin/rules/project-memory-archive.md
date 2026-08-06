---
description: >
  项目历史决策、架构基线、POC实验结论、知识搜集状态的按需参考档案。
  WHEN to use: 回顾项目演进历史、理解架构决策背景、查阅 POC 实验结论、
  了解 122/123 号架构基线、查阅证据裁决、了解知识搜集状态和 arXiv 操作化状态。
  WHEN NOT to use: 日常开发、当前待办（在 AGENTS.md TODO 节中）。
trigger: model_decision
---

# project-memory-archive rule

当任务涉及以下场景时，加载 `project-memory-archive` skill：

- 回顾项目演进历史、理解架构决策背景
- 查阅 122号v2 架构基线（13条工程直觉）或 123号v1 第一性原理重构基线（10条严格化基线）
- 查阅 80-99号完整复核后的证据裁决
- 查阅 POC 隔离测试标准流程（116号方案）
- 查阅四次 POC 核心洞察（POC-1/4/5/6）
- 了解 Subagent 写文件能力与 /yolo 模式
- 了解知识搜集状态和 arXiv 论文操作化状态

skill 中包含：122号v2基线、123号v1基线、证据裁决、POC隔离测试流程、POC核心洞察、知识搜集状态、arXiv操作化状态。

注意：明确不做清单（8项硬约束）和工作系统纪律（7条）在 AGENTS.md 中 always-on，本 rule 只负责历史背景和详细基线。
