# 第六代系统现状 Repo 逆向调查报告

## 调查范围与结论边界

本报告记录 `codex/sixth-gen-current-repo-2026-08-24` 分支的第一轮调查，不把“文档存在”写成“系统已经实现”，也不把旧目录位置写成当前真值。调查基线是 annotated tag `pre-sixth-gen-current-repo-2026-08-24`，指向 `3b26684`；未 push、未改写 Git 历史、未写数据库、未启动外部运行系统。

本阶段目标是把当前工作树收敛为“第六代系统现状 repo”。旧代系统不再作为活动根目录内容参与未来路由，但其仍有价值的第六代事实必须先抽取；不能证明继承关系的材料只保留 Git/tag/history 可恢复性。

## 已完成的基线动作

- 已创建并切换到 `codex/sixth-gen-current-repo-2026-08-24`。
- 已创建 `pre-sixth-gen-current-repo-2026-08-24`，tag message 明确说明这是收窄前的安全基线。
- 分支切换前工作区干净，HEAD 为 `3b2668404ce42a3bd6eacd76f0ed1a5cfe880769`。
- 当前现场初始清单覆盖 19,286 条路径：6,184 条 tracked、13,100 条 ignored，另有 2 条在清单生成过程中产生的调查清单路径（`source-inventory.tsv` 和 `path-migration-map.tsv`）。清单包含状态、大小、mtime，并为 Git 路径记录最近提交；后续调查报告、概念账本和逆时间索引不属于这次基线输入。
- 初始路径分类为：`candidate-source` 818、`governance-current` 338、`supporting-candidate` 439、`legacy-generation` 207、`sibling-or-evidence` 4,331、`exclude-local` 13,084、`unknown` 69。`unknown` 是待调查项，不是最终许可状态。

机器底账：`source-inventory.tsv`。迁移审计底账：`path-migration-map.tsv`。概念账本：`concept-extraction.tsv`。

## 第二轮路径分类结果

初始 69 个 `unknown` 已逐项读取路径、最近提交和相关内容后归零：43 个 `keep-current`、7 个
`extract-current-knowledge`、18 个 `history-only`、1 个 `exclude-local`。此外，tracked 的
`.env.example` 从过宽的 `.env*` local-secret 规则中纠正为 `keep-current`。

本轮仅修改清单和迁移计划，没有移动、删除或重写任何原文件。两张 TSV 均为 19,286 个唯一
path，字段数和 path 集合一致。由于 macOS 当前 locale 会把不同中文路径视作排序等价，所有
中文 path 分类、唯一性和集合检查统一使用 `LC_ALL=C` 的字节级比较。当前仍有 5,795 条
`retain/extract/history` 候选动作待概念证据核验，不能把 literal `unknown=0` 写成迁移已经完成。

## Final Path Decision And Canonical Move Batch

在19个概念族、canonical docs、current code/tests和Git替代关系闭合后，19,286个baseline path已全部
获得final action：799个`keep-current`、7个`extract-current-knowledge`、5,396个`history-only`、
13,084个`exclude-local`；pending和unknown均为0，target collision为0。

已执行的物理迁移共698个path：26个Prompt迁入`prompts/absorb/`，95个第六代R&D来源迁入
`docs/history/sixth-generation/rnd/`，19个旧第六代说明迁入`docs/history/sixth-generation/legacy-spec/`，
557个Tell/非特化研究与POC资产迁入`evidence/history/tell-research/`，1个仍被current absorb驱动消费的
IMO 2009 P6 profile迁入`system/tests/vein_analysis/fixtures/`。其余history-only内容不复制进目标树，由
`pre-sixth-gen-current-repo-2026-08-24`和逐path Git pointer恢复。

current `.ref` 对待移除目录的依赖已经清除；仍有效的 `.devin` 开发纪律已归一到current development
contract。冻结 manifest 的旧路径 identity 保持原值，通过 canonical current path 或 pinned Git blob
验证，未靠恢复旧根目录换取测试通过。

## Git 历史逆向结果

截至安全基线，原项目历史为 1,397 个主要开发提交；加入本轮治理提交后当前 refs 可见 1,401 个提交。历史从 2026-07-07 的星学/排盘系统开始，不能把这段早期历史伪装成第六代系统的出生点。

从最新提交向前回溯，已经确认以下第六代谱系：

| 阶段 | 关键证据 | 当前解释 |
|---|---|---|
| 2026-08-09 至 2026-08-10 | 303-309 研发文档，特别是 `21e8940` | Grove 侧思想被复制到本 repo，形成 Trace/Tell/Hint、FCA 和“从提取到查询”的第六代概念起点。 |
| 2026-08-10 | `3624e41`、`691fa60`、`07530ff`、`6309a71`、`daa90c1` 等 | 技术说明书、双轨术语、Prompt 资产、VMS-28 验证和三阶段脉络分析逐渐形成。 |
| 2026-08-11 | `1ce9ea6`、`250da22`、`224d22a`、`38d46d3` | `system/` 获得物理实现、测试资产和内部 docs；`six/` 合并进 `system/`，明确终止 `six/` 作为独立维护边界。 |
| 2026-08-12 至 2026-08-13 | Tell 分类学、非特化研究、Seven 相关提交 | 第六代概念被扩展到 Tell/Hint 研究和证据工厂，但这些并非自动等价于第六代当前实现。 |
| 2026-08-14 | 344-387 号文档，打包提交 `4788bab` | 解题侧非线性脉络、Devin/tmux、D 盘 workspace、Event Extractor、State Normalizer、Trace Auditor 和零模型资格链形成。 |
| 2026-08-16 | `7392235`、`3c38996`、`cbdcd58`、`6f9e29f` | 391 取代 363 成为解题侧路线真值；代码、fixtures、测试、冻结资格链和 runbook 进入 `system/`。 |
| 2026-08-17 至 2026-08-22 | Tell/非特化 POC、外部解题系统拆分、`08ad266` | 研究线和续传/解题系统继续改写概念与证据状态；它们需要抽取与降级，不能整岛搬入当前第六代活动面。 |

这条时间线说明：`第六代系统技术说明书/` 是重要历史设计入口，但它不是完整的当前第六代认知。当前认知还分布在 `system/`、`system/docs/`、`system/tests/`、344-392 研发/POC 文档、Prompt 资产、Tell 研究和后续验证收据中。

## 当前系统边界的初步判断

目前可以作为第六代候选活动面的物理核心是：

- `system/`：入题侧 `vein_analysis.py`、解题侧 `solve_vein_analysis/`、schema/DB 封装、assets、tests 和模块 docs。
- Prompt 与角色资产：`system/assets/`、`第六代系统提示词积累目录/` 以及经证实影响运行行为的 `.devin/rules/` 子集。
- 当前证据：`system/tests/`、冻结 fixtures、qualification packs、audit receipts，以及经过状态标注的 D 盘 run 指针。
- 当前认知入口：根治理骨架、`docs/`、`dev-docs/sixth-gen-current-repo/` 和 `认知闭包/`。
- 数据边界：`knowledge/` 中的指针与 D 盘大数据策略；数据库代码是实现证据，不能替代当前 live DB 观察。

下列内容目前不能直接作为第六代活动面：第五代说明书、原语系统、Seven、Eight、分析系统、星学遗留、Tell 研究全目录、运行输出大岛和旧根文档。它们只在某一条概念经过代码/测试/用户裁定或明确替代关系证明后，进入“抽取当前知识”或“历史证据”路径。

## 第一轮概念调查结论

`concept-extraction.tsv` 已登记 19 个概念族。当前最重要的结论不是把它们全部写进新文档，而是保留它们不同的状态：

- Trace、入口侧 vein analysis、FCA/lattice、Pipe 架构已有代码和测试支撑，但语义仍分散，需要 canonical docs 统一。
- Tell、Hint、Trace/Tell/Hint 链是第六代核心词汇，但后来 TellCore/非特化 POC 对候选含义做过修正；必须区分用户裁定、研究候选、实现和实验结果。
- 解题侧 `solve_vein_analysis/`、State Normalizer、Trace Auditor 已有物理实现和零模型/离线证据；这不等于模型 live qualification 通过。
- Devin/tmux 与 D 盘 workspace 是 development-only 证据路径；`LiveRunPermit`、盲审、qualification pack 是独立的授权/质量门。
- `Grove` 和 `VMS` 仍然是理解历史的高价值概念，但是否作为当前第六代公开架构的一部分，要由抽取结果和当前代码边界决定，不能只因旧文档使用了这些词而保留为当前事实。

## 目前已发现的冲突与未知

1. 第六代技术说明书、研发过程文档、`system/docs/` 和后期 POC 对 Pipe、Tell、Hint、资格链的叙述粒度不同；尚未形成一份唯一当前规范。
2. `system/README.md` 已记录 391 替代 363，但旧 363 文件和 route-lock 仍必须保留为历史物证；迁移时不能把“替代”误做成物理删除。
3. `.devin/rules/` 中既有第六代开发纪律，也有后来解题/续传系统的规则；必须按运行时可见性和消费者逐文件划分，不能整目录复制到未来 runtime context。
4. `Tell分类学研究过程文档/`、`runs/`、`subagents-dirs/`、`palyground/` 含大量证据和生成物；它们的保留方式需要按“当前证据、历史证据、D 盘外置、local/cache”四类逐项核对。
5. Final path action 已归零 pending；剩余风险是迁移执行期间的 ref/import/link 完整性和历史恢复验证。
6. 当前没有授权使用数据库或外部运行系统补足 live 事实，因此所有 live/资格化结论必须保持证据准确的降级状态。

## 下一步执行顺序

1. 建立current development contract，清除`.ref`对`.devin`、旧代和待移除根目录的依赖。
2. 按迁移表执行四组`git mv`，同步Prompt代码路径和历史索引。
3. 从活动树移除其余history-only tracked paths；不触碰local/secret/cache内容。
4. 重写根README、dev-docs/history索引，使旧岛只通过Git/history入口可达。
5. 生成最终文件对账，要求pending/unknown/missing/duplicate均为0；运行治理、链接、compile和system tests。

## 当前判定

本报告是第一轮调查产物，状态为 `investigation-in-progress`。新分支和安全基线已经完成，逆向谱系和三张底账已经开始建立；第六代 canonical repo 尚未完成，当前不能声称已经不存在文档/代码不一致，也不能声称旧系统内容已经安全移出活动面。
