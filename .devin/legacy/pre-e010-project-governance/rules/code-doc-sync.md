# 代码修改后同步更新文档

> **触发条件**：当你修改了错题分析系统（`analysis-devin-failure-system/`）或解题系统（`xishujuzhen/solver_harness/`）的代码逻辑后——包括但不限于：新增/修改函数、修改数据结构、修改路径逻辑、修改DB字段、修改检查逻辑、修复bug。

## 铁律

**代码修改和文档更新必须在同一个commit中完成。** 不允许"先提交代码，文档以后再补"——以后永远不会补。

## 需要同步更新的文档清单

### 错题分析系统（`analysis-devin-failure-system/`）

| 修改类型 | 需要更新的文档 | 位置 |
|---|---|---|
| 新增/修改Pipe组件 | `AnalysisSystemDesign.md` §4 代码资产索引 | 项目repo根目录 |
| 修改设计原则或关键设计决策 | `AnalysisSystemDesign.md` §5/§6 | 项目repo根目录 |
| 修改Monitor Pipe检查项 | `MonitorPipe.md` 检查项目分类表 | 项目repo根目录 |
| 修改架构/目录结构 | `docs/architecture.md` | `analysis-devin-failure-system/docs/` |
| 修改框架检查清单相关逻辑 | `docs/framework-checklist.md` | `analysis-devin-failure-system/docs/` |
| 修改优雅停止/watchdog逻辑 | `docs/graceful-shutdown.md` | `analysis-devin-failure-system/docs/` |
| 修改动态并发逻辑 | `docs/dynamic-concurrency.md` | `analysis-devin-failure-system/docs/` |
| 修改运维关注点（stall/rate_limit/zombie） | `docs/operational-concerns.md` | `analysis-devin-failure-system/docs/` |
| 修改Monitor Pipe设计范式 | `docs/monitor-pipe-pattern.md` | `analysis-devin-failure-system/docs/` |
| 修改检查规范 | `specs/{name}_monitor_spec.md` | `analysis-devin-failure-system/specs/` |
| 修改POC运行状态 | `AGENTS.md` 对应POC章节 | 项目repo根目录 |

### 解题系统（`xishujuzhen/solver_harness/`）

| 修改类型 | 需要更新的文档 |
|---|---|
| 修改pipe组件 | 对应的README或设计文档 |
| 修改运行状态 | `AGENTS.md` 对应章节 |

## 判断流程

修改代码后，问自己：

1. **这次修改改变了什么行为？**（新增功能/修复bug/修改路径/修改数据结构）
2. **哪些文档描述了这个行为？**（按上表查找）
3. **这些文档是否还准确？**（如果不准确，更新它们）
4. **是否有新的设计决策需要记录？**（如果有，加入`AnalysisSystemDesign.md` §6）

## 反模式

- **"文档以后再补"**——以后永远不会补。代码和文档必须在同一个commit中。
- **"只改代码不改文档"**——下一个AI读文档时会按照旧的（错误的）逻辑理解系统，导致重复踩坑。
- **"文档太长不想更新"**——文档长是因为系统复杂。不更新文档会导致系统更难维护。
