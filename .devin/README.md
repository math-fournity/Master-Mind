# `.devin/` 治理入口

## 当前活动面

- `config.json`：只启用标准 AGENTS，关闭兼容导入和 Sub Agent，并给历史重建保留只读 Git 取证面。
- `hooks.v1.json`：不作为永久 tracked 文件维护；由
  `~/devin/harness/start-devin-harness.sh` 在启动时创建并拥有，由 stop 脚本按 hash
  精确解除。
- 当前没有项目本地 `.devin/rules/*.md` 或 `.devin/skills/*/SKILL.md`。跨项目治理由 Devin E010
  global AGENTS + 45项 Layer2 router 提供，项目事实由根 AGENTS/README/MEMORY/Feature/调查资产提供。

## 为什么退出旧自动发现面

`legacy/pre-e010-project-governance/` 保存本 repo 旧阶段的 50 条 Rules、15 个 Skills 和 Arango cognition
Hooks。它们服务过数学系统研发、POC、数据、认知图和 Sub Agent 工作线，但当前任务是对冻结历史
做完整认知重建；继续自动发现会：

- 与根 AGENTS 和全局 always-on 竞争 Devin 的实际规则注入预算；
- 把历史产品工作线、数据库操作、POC 审计或 Sub Agent 流程重新调度为当前任务；
- 让 200k context 在开工前被无关 descriptions/always-on 正文占用；
- 与 E010 的 closure/lifecycle/legacy reconstruction 形成冲突真值。

因此这些资产被 `git mv` 到 legacy，而不是删除或判定为永远错误。需要研究历史治理机制时可作为
`HISTORICAL_EVIDENCE`读取；它们默认无当前调度权，不得直接复制回活动目录。

## 启动

完整命令和首条用户指令见：

`~/devin/docs/operations/Devin-CLI超级Repo全历史重建使用说明.md`

不要手工覆盖 harness-owned `hooks.v1.json`。若 start 报配置冲突，先运行 harness status 和 Git
baseline，确认文件来源后再处理。

## 恢复

- 旧项目治理模式恢复点：annotated tag `pre-devin-governance-e010-2026-08-25`；
- 1,399-commit调查快照：annotated tag `legacy-reconstruction-snapshot-2026-08-24`；
- 恢复不得使用 `git reset --hard` 或整目录覆盖；先比较当前 baseline，再选择精确文件/目录和新 commit。
