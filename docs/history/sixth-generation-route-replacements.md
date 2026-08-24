# 第六代系统路径与真值替代

**状态**：current history route
**恢复基线**：`pre-sixth-gen-current-repo-2026-08-24` -> `3b26684`

## 第六代形成时间线

| 时间 | 事件 | 证据 |
|---|---|---|
| 2026-08-09 至 10 | 303-309 思想链进入本 repo，形成 Trace/Tell/Hint 和查询范式 | `21e8940` |
| 2026-08-10 | 技术说明框架、四 Pipe、Prompt、FCA 和 VMS-28 系列形成 | `3624e41`、`45036e0`、`07530ff`、`6309a71` |
| 2026-08-11 | absorb 侧实现、tests/docs 和 `six/` 合并进入 `system/` | `1ce9ea6`、`224d22a`、`38d46d3` |
| 2026-08-14 | solve-side DAG、Devin/tmux、资格链、State Normalizer/Trace Auditor 方案形成 | 344-387 号；后由 `4788bab` 收入本 repo |
| 2026-08-16 | 391 取代 363；solve-side 代码、tests、assets 和 runbook 收入 `system/` | `7392235`、`cbdcd58`、`6f9e29f` |
| 2026-08-17 至 22 | Tell/Hint 非特化 POC、续传和外部 Solver 拆分继续修正证据状态 | `0f54bf4`、`d80201f`、`08ad266` 等 |
| 2026-08-24 | 治理对齐和第六代 current-repo 重建开始 | `9f7c9fe`、`3b26684`、`d84ee11` |

## 明确替代关系

| 旧入口 | 当前入口 | 证据 | 当前含义 |
|---|---|---|---|
| `six/` | `system/` | 343 号、`38d46d3` | `six/` 已删除；旧实现和设计通过 Git 恢复 |
| 363 号路线图和 route-lock | 391 号方案 | `7392235`、`534f73f`、`98bcbc4` | 363 是冻结历史物证，不再推进资格链 |
| `第六代系统技术说明书/` 作为完整现状入口 | 本组 `docs/*/sixth-generation-*` + current code/tests | 本重建分支 | 旧说明书是抽取来源，不再单独决定当前真值 |
| root `CurrentTaskAwareness.md` | `MEMORY.md` + 本文 | `e33741e` 及迁移表 | 旧文件保留历史状态，不维护第二份当前任务 |
| root `000-v0...md` | `docs/domain/sixth-generation-concepts.md` | `183f527` + 抽取账本 | Tell/Hint 当前语义进入 domain doc；原文保留来源 |
| root `DataFoundation.md` | `docs/data/sixth-generation-data-boundaries.md` | 抽取账本 | 只抽取仍与当前代码/数据边界一致的内容 |
| root `AnalysisSystem*.md` 和分析目录 | current AI/operations docs 或 history-only | `0f54bf4`、`d80201f` | 外部/历史系统不是当前第六代组件 |
| in-repo active Solver routes | 独立 Solver repos | `0f54bf4`、`d80201f`、`e318b58` | 外部 repo 受自己的 AGENTS 治理 |
| `第六代系统提示词积累目录/` | `prompts/absorb/` | path migration map | Prompt source 进入 canonical root，历史版本仍保留 |
| `第六代系统研发过程文档/` | `docs/history/sixth-generation/rnd/` | path migration map | 保留第六代 R&D 证据，退出活动根 |
| `第六代系统技术说明书/` | `docs/history/sixth-generation/legacy-spec/` | path migration map | 明确 legacy spec 身份 |
| `Tell分类学研究过程文档/` | `evidence/history/tell-research/` | path migration map | 研究/POC 进入 evidence history |

## 当前 canonical 真值顺序

1. 用户当前裁定、`feature-list.md` 和本分支治理；
2. `system/` code、`.ref`、`.ai-check` 和当前 tests；
3. 本组 stable docs；
4. 与代码一致的 `system/docs/`；
5. 已被后续证据确认的研发/POC 结论；
6. 旧技术说明、前代系统和 sibling islands；
7. Git diff 和 sealed artifacts 用于解释历史，不反向定义当前需求。

## 保留和移出规则

旧文件退出活动工作树前必须满足：其当前事实已抽取、旧 path 在 migration map 有最终 action、
replacement 或 history pointer 可达、源 commit/tag 可恢复、没有未提交内容。历史失败和 sealed evidence
不因“目录变干净”而删除；大 body 可在 D 盘保留，Git 保存 pointer/hash/receipt。

## 审计入口

- 完整 commit 逆时间索引：`dev-docs/sixth-gen-current-repo/reverse-git-log.tsv`；
- 当前路径清单：`dev-docs/sixth-gen-current-repo/source-inventory.tsv`；
- 概念主张账本：`dev-docs/sixth-gen-current-repo/concept-extraction.tsv`；
- 迁移计划：`dev-docs/sixth-gen-current-repo/path-migration-map.tsv`；
- 超级 repo 历史：`docs/history/system-lineage.md` 和 `git-log-lineage.tsv`。
