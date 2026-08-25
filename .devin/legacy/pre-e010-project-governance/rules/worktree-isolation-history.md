---
description: >
  Worktree 隔离的实施历史记录。
  WHEN to use: 排查 ArangoDB 隔离问题、了解环境变量化过程、查看 commit 历史、
  了解上游同步记录、排查数据库连接问题。
  WHEN NOT to use: 日常文件操作和 git 操作（这些规则在 AGENTS.md 硬约束中）。
trigger: model_decision
---

# worktree-isolation-history rule

当任务涉及以下场景时，加载 `worktree-isolation-history` skill：

- 排查 ArangoDB 数据库隔离问题（为什么连错了数据库、环境变量化细节）
- 了解环境变量化过程（25个文件、6种改动模式、配置文件说明）
- 查看本 repo commit 历史（glm5.2 分支）
- 了解上游同步记录（同步内容、方式、注意事项）

skill 中包含：历史代码状态、隔离方案详情（环境变量化过程）、commit 历史、上游同步记录。

注意：日常的文件操作边界、git 协调规则、数据库隔离硬规则在 AGENTS.md 的硬约束 1-4 中，本 rule 只负责历史背景。
