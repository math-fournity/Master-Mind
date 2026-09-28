# Topology Findings — 拓扑结论、封存战役与 GitHub 整备 Gate

> 证据等级：本文件结论分两级标注——[git] 为 Git 机械证据（SHA/merge-base/分支关系，可直接复验）；
> [doc] 为仓库文档自述；[stat] 为 HOME first-pass 大图（metadata/stat 级，未经逐 commit diff-review）。
> 本地绝对路径与敏感 token 不出现在本文件；路径映射见 `paths.local.md`（gitignored）。

## 1. 拓扑三问

### 1.1 ORIGIN main 与 glm5.2 线的关系

- [git] `f32194f`（2026-08-05 14:48，"146号v4→v4.1"）是 ORIGIN main 的开发终点，也是两条 glm5.2
  线的共同 merge-base：ORIGIN main 自此再无开发 commit，直到 2026-09-28 的三个封存提交。
- [git] ORIGIN 侧分支：`parallel-work` 与 main 同 tip（无独有内容）；`worker/W1/auto.220` 与
  `worker/W2/auto.221` 同指 `f2c5fa1`（2026-07-10，auto_dispatch 自动化），为 main 祖先、0 独有
  commit——**无保全风险，但可作为早期自动化工作线的历史标记选择是否推送**。
- [git] tags：`GPT-5.6启动`/`GPT-5.6结束`（模型切换时代标记）、`审计方法论手册`。
- [doc] ORIGIN 的 AGENTS.md（f32194f 版）是"数学大师制造项目"方法论本体：星学继承、K/T/H 稀疏
  视图、综述博士、依赖图三层提示。其未提交工作区（Phase 7 + 183/184 号）是 DYN-0..7 证据等级线
  的收尾，7 周未落盘，2026-09-28 已封存（§2）。

### 1.2 GROVE glm5.2 与 HOME glm5.2 的分叉

- [git] 两线共享 `f32194f` 之后的 **265 个 commits**；fork 点 `2e33663`（08-05 晚，"更新数据库隔离
  状态"）。
- [git] GROVE 首个独有 commit：`83c18ef`（2026-08-08，"Grove repo迁移：路径全部从旧worktree路径
  更新为Grove路径"）——**glm5.2 线最初在别的 worktree 目录工作，08-08 迁入 GROVE 路径后形成支线**。
- [git] 独有量：GROVE 32（历史）+5（封存）= 37；HOME 838。HOME 是 glm5.2 主线（延续至治理重建），
  GROVE 是 08-08..08-09 的研究支线（止于 `41a3cb2`"范式转变——从提取到查询"）。
- [git] HOME 不含 `41a3cb2` 对象；GROVE 不含 HOME tip 对象——两 clone 从未互相 fetch/push，且
  glm5.2 从未推回 ORIGIN（ORIGIN 无 glm5.2 分支）。

### 1.3 分支全景与保全清单（"不丢东西"核对表）

| 分支/引用 | 所在 | 状态 | 保全动作（提案） |
|---|---|---|---|
| glm5.2（HOME） | HOME | 主线，1402 commits | Gate 后作 Master-Mind 主干 |
| codex/governance-alignment-2026-08-24（`3b26684`） | HOME | **未合并**，3 独有 | 推送保全，之后择机 merge 或归档 |
| codex/sixth-gen-current-repo-2026-08-24（`b431756`） | HOME | **未合并**，11 独有 | 同上 |
| legacy-reconstruction-snapshot-2026-08-24 → f7dc625 | HOME | annotated tag | 一并推送（分母锚） |
| glm5.2（GROVE） | GROVE | 支线，37 独有 | 作 legacy 分支推送保全 |
| main + parallel-work + worker×2（ORIGIN） | ORIGIN | main=302；其余无独有 | main 作 legacy 分支推送；worker/tag 可选 |
| codex/trace-restructure-feasibility（`537412bb`） | A-FEASIBILITY | clean，SUPERVISOR 实验克隆 | 随 SUPERVISOR 线处置 |

## 2. 未提交内容封存战役（2026-09-28，用户授权）

三个仓库的工作区在封存后全部 clean；每批均为调查后按语义分组、精确 pathspec stage：

| 仓库 | commit | 内容 | 备注 |
|---|---|---|---|
| ORIGIN | `19ca14d` | Phase 7：representation/ 24 模块 + 163-166 号 + 146→v4.2.1 + 147→v1.4.1 + runs 清单 | py_compile 24 模块全过；对应 GROVE 线 001 号方案所记录的"上游未提交内容" |
| ORIGIN | `56508a7` | 183/184 号（用户需求总执行方案、Phase0-7 证据等级审计）+ 用户需求.md + AGENTS/ChangeLog 索引 | AGENTS diff 含 163-166 与 183/184 两组索引行，随本批落盘 |
| ORIGIN | `36d5e85` | backups/arango/20260806 数据库 dump（244K） | runtime 数据备份，上传前需隐私复核 |
| GROVE | `5e0fea7` | 08-07 批研究文档 225-253 号 13 份 | 其中 225-241 号的 ChangeLog 索引在此前提交已存在但文件从未 add |
| GROVE | `09c2f9d` | 08-09 批研究文档 303-307 号 + ChangeLog 同步（+183 行） | 非局部 tell / FCA 对应 / 思维拓扑 / 原语化 |
| GROVE | `f86e13f` | 移除提取侧 runtime 三模块（trajectory_adapter/hint_injector/realtime_pipeline） | **删除意图为推断**（与 41a3cb2 范式转变一致，无书面记录）；父提交 `0e229a0` 可恢复 |
| GROVE | `2979464` | knowledge 原始语料治理：DOWNLOAD-MANIFEST + 下载日志入库 + 2.7G 原始题库按 .gitignore 排除 | 另归档"来自另一个AI/1.md"（225→226 号数学化路线外部 AI 来函） |
| GROVE | `460ce36` | 实验产物 runs 约 65M（ab_test_253、fate×10、matharena×30、vms_test_1、mitm_verify 等） | 含 31M tmux 管道原始捕获；与已提交的 cb3d044 等 commit 证据对应 |
| FEITEHUA | `84ff468` | 角色目录初始保全提交（非特化 POC AI 工作说明） | 订正事实：该目录原为零提交状态，其 AGENTS 自述"与主 worktree 共享 git 仓库"与 Git 事实不符 |

## 3. 内容级对账（开放项）

- [git] ORIGIN 今日封存的内容大部分在 HOME 线已有对应提交（HOME tracked：representation/ 24 文件、
  183/184 号、用户需求.md 均存在）；**ORIGIN 真正独有的是 arango 备份**（HOME 无 backups/）。差异
  以 ORIGIN 自己的工作区封存为准，是否与 HOME 版本 drift 留待核对（146/147 版本号）。
- [git] GROVE 303-307 号文档在 HOME 的 dev-docs 无同号文件；GROVE 37 个独有 commits 与 HOME 的
  内容对应（异号重复/改写/缺失）**未做内容级对账**——列入 second-pass 的对账事项，不在本轮伪造结论。
- [doc] 下载日志中出现过 HOME 路径的 hf 锁记录，说明部分题库下载最初以 HOME 为目标目录，后落在
  GROVE——数据落位史以日志为准。

## 4. 世代覆盖映射（[stat]+[doc]，待 second-pass 校准）

| 成员 | 覆盖世代/时间窗 | 角色 |
|---|---|---|
| ORIGIN | 星学继承→xishujuzhen 方法论→Phase 0-7（≈2026-07-07..08-06） | 源头/最早代际载体 |
| GROVE | 第六代 Grove 核心（≈2026-08-05..08-09，含 VMS/FCA/原语化研究支线） | 引擎支线 |
| HOME | 全代际（2026-07-07..今：astro/qizheng→…→seven/eight→治理重建） | 主线/全集 |
| FEITEHUA | 非特化研究线（2026-08-12 前后，产出写入 HOME） | 角色目录 |
| SUPERVISOR | 非代际本体（2026-08-25 起，重整控制面） | 治理外围 |

## 5. GitHub 整备对位（2026-09-28 探测）

- 目标主容器：`math-fournity/Master-Mind`——**public、空仓（quick-setup）**，描述"大师头脑"。
- 同账号已有 15 个公开仓，与用户排除项对位：**平凡/简单解题系统 = AI-Math-Normal-Solver**；
  **持续/续传解题系统 = AI-Math-Competition-Problem-Solving-System**；另有 AI-Math-Solving-
  Trajectories（当前世代运行现场）、AI-Math-Solving-Trajectories-Archive（早期世代归档）、
  AI-Math-Solving-Databases（ArangoDB 导出+题库目录）及多个数学元理论仓（HoTT-Paradoxy、
  MATH-FOURNITY、Gödel/Church 扩展、NavierStokesAndEuler、vibe-mathing 系、prove2me_manual）。
- 命名风格：英文意译名，均不含敏感 token——与上传硬约束一致；生态现用 MIT 许可证居多。
- **处置提案（草案，待用户裁定）**：Master-Mind 承载多代线——HOME glm5.2 史为主干，ORIGIN main
  与 GROVE glm5.2 作 legacy 分支，HOME 两个 codex 分支与 snapshot tag 一并保全；FEITEHUA 内容已
  在 HOME 主线中，本体不单独上传；SUPERVISOR 保持本地或独立小仓；原始题库沿用 GROVE 已建立的
  manifest 模式不入 Git（数据导出类内容可参考既有 Databases 仓的做法）。

## 6. 上传前 Gate 清单（量化基线，2026-09-28 扫描）

> 扫描方法：`git grep`（工作树 tracked 内容）与 `git log --all`（commit message / 历史文件路径）。
> 只记录计数与文件路径，不落任何凭证值。**历史文件路径三仓均为 0 命中——改写面集中在内容与
> commit message，不涉及路径重写。**

| # | Gate 项 | HOME | ORIGIN | GROVE | 必做动作 |
|---|---|---|---|---|---|
| 1 | 敏感 token（本地目录名） | 394 文件/3,581 处 + 7 条 msg | 33/162 + 1 | 190/514 + 5 | 内容替换 + commit message 历史改写（filter-repo 级），改写后全量复扫归零 |
| 2 | ArangoDB 明文口令 | 435 文件 + 3 条 msg（重灾区 subagents-dirs 358、xishujuzhen 30、scripts 19） | 29 文件 | 49 文件 + 3 条 msg | 同上；优先轮换该口令本身（历史上曾暴露于多处） |
| 3 | 私有路径（/Users/*、/Volumes/*） | 564 + 620 文件 | 7 + 33 | 278 + 429 | 内容级替换或相对化；治理文档改用匿名 ID + 本地附录模式 |
| 4 | 邮箱样串 | 180 文件 | 177 | 177 | 多为 arxiv 全文/语料内的公开邮箱，需甄别；作者身份类邮箱按用户意愿保留或脱敏 |
| 5 | sk- 样式串 | 2 文件 | 2 | 2 | **已判定假阳性**：arxiv 全文（cs_MA_2607_16764、cs_SE_2607_25647）中的偶然字符串，非凭证 |
| 6 | 大文件 | runs 若入史需评估 | arango 备份 244K | 31M tmux log；.git 已 450M | 单文件 100M 硬限核查；LFS/裁剪决策 |
| 7 | 语料隐私 | - | - | - | aistudio 系排除项不进入；arxiv 全文许可证合规复核 |
| 8 | 分支/tag/授权 | - | - | - | §1.3 保全清单逐项决策；每个上传 wave 单独用户授权 |

## 7. 开放项与后续

1. GROVE 37 独有 commits ↔ HOME 内容级对账（second-pass 事项）。
2. ORIGIN 146/147 封存版本与 HOME 对应文档的版本 drift 核对。
3. worker 分支、ORIGIN/GROVE tags 是否随上传保全——待用户裁定。
4. A-FEASIBILITY 克隆与 HOME 的 Trace generation 对账（属 SUPERVISOR 线）。
5. 上传 wave 化方案（分支顺序、改写工具链、改写后验证脚本、复扫归零判据）——需专项设计文档，
   本清单只固定量化基线。
