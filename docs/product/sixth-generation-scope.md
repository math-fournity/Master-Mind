# 第六代系统当前范围

**状态**：current
**适用分支**：`codex/sixth-gen-current-repo-2026-08-24`
**需求来源**：`feature-list.md` GOV-010，`rulings.md` R-008
**事实边界**：本文描述当前产品范围和交付状态；实现由代码决定，验证由测试和运行证据决定。

## 产品身份

本分支的目标是成为第六代 AI 数学系统的当前状态 repo。历史超级 repo 中的前代系统、Seven、
Eight、错题分析系统、外部 Solver 和星学遗留只作为抽取来源或历史证据，不再作为当前产品组件。

第六代系统的目标能力仍是让推理树和引导树通过 Trace、Tell、Hint 的循环持续生长，但当前 repo
尚未实现完整闭环。不能把目标架构、历史 POC 或类型定义冒充为可运行产品。

## 当前交付面

| 能力 | 当前状态 | 决定性证据 |
|---|---|---|
| 共享领域类型 | 已实现，未形成完整端到端验证 | `system/schema.py` |
| absorb 侧三阶段脉络分析 | 代码已实现，当前分支未进行 live 运行验证 | `system/vein_analysis.py`、`system/docs/vein_analysis.md` |
| ArangoDB 适配器 | 代码存在，当前 live schema 和数据未核验 | `system/db.py`、`system/db_schema.py` |
| solve-side 结构化轨迹离线分析 | 已实现并在当前环境验证 | `system/solve_vein_analysis/`；295 tests PASS |
| Event Extractor/State Normalizer/Trace Auditor 资格工具 | 离线和零模型合同已验证；模型角色未资格化 | `system/tests/solve_vein_analysis/README.md` |
| `enter.py` 入题入口 | 未实现 | `load_solution_records()` 抛 `NotImplementedError` |
| `solve.py` 解题入口 | 未实现 | `load_problem()`、`inference_explore()` 等抛 `NotImplementedError` |
| Trace 到 Tell 匹配和 Tell 沉淀 | 未实现 | `process_absorb.py`、`process_solve.py` |
| Guide 展开、两棵树和 Grove 闭环 | 目标架构，未实现 | `process_solve.py`、`system/docs/architecture.md` |
| live 模型资格实验 | 未授权、未验证 | R-007、冻结 `LiveRunPermit` 计划和测试索引 |

## 当前非目标

- 不把历史目录原样搬成“第六代模块”。
- 不在本轮实现缺失的 Grove/Tree/Tell runtime，只先建立准确当前认知。
- 不启动 Devin、tmux live qualification、外部 Solver、ArangoDB 写入或远程 push。
- 不把 295 个离线测试解释成模型能力、Tell 有效性或端到端闭环证明。
- 不复制大语料和大 run body 回 Git。

## 目标活动面

最终活动工作树只路由到：根治理文件、`system/`、`docs/`、`prompts/`、`evidence/`、`knowledge/`、
`dev-docs/` 和 `认知闭包/`。历史来源只有在当前事实已抽取、迁移表有恢复指针后才退出活动面。

## 完成标准

1. 根治理入口把 repo 明确识别为第六代当前状态，而不是历史超级 repo。
2. 当前范围、概念、架构、合同、AI、数据、质量、运行和历史替代均有唯一 canonical 路由。
3. 所有原路径都有最终分类；pending 和 unknown 均为零。
4. 当前代码事实和验证状态不被文档抬高。
5. 非第六代活动目录退出当前工作树，但可从安全 tag、Git commit 和迁移表恢复。
