# Repo 群后续工作方案（文件级 checklist 版）

> 生成：2026-09-28，依据当日 first-pass 结论与用户四条指令（多代系统线聚焦、先调查后分批提交、
> 多分支不丢内容、上传社区可恢复 + token 绝迹）。
> 性质：**执行计划，不是授权凭证**——凡涉及写外部仓、历史改写、push/上传的 wave，仍需用户当轮
> 明确授权。本文件不改变冻结快照 1,399 分母与 second-pass next item。

## 0. 配套清单资产（本方案引用的文件级数据）

| 资产 | 内容 |
|---|---|
| `grove-unique-commits.tsv` | GROVE 独有 37 commits 全列（`83c18ef` 迁移 → `460ce36` 封存，含日期与 subject） |
| `grove-docs-home-matrix.tsv` | GROVE/ORIGIN 独有内容在 HOME 的存在性矩阵（26 行：18 份文档 + 4 份 ORIGIN 文档 + backups + 3 个 runtime 模块） |
| `preupload-inventory/inventory-*.tsv` | 敏感内容逐文件基线（token/口令/私有路径/邮箱，三仓合计约 3,500 行） |
| `paths.local.md` | 成员真实路径（gitignored，永不入库） |

## W1 GROVE↔HOME/ORIGIN 内容级对账（并入 second-pass 执行）

- [ ] **W1.1 37 个 GROVE 独有 commits 逐个对账**。输入：`grove-unique-commits.tsv`。方法：对每行
  `git -C <GROVE> show --stat <sha>`，逐变更路径在 HOME 查同内容/同主题提交。输出新增
  `grove-home-reconciliation.tsv`，schema：
  `sha_short | 变更概要 | home对应commit或NONE | 判定依据(diff抽样) | 置信(high/med/low)`。
  已知锚点：`0e229a0`（04工作线P0：三 runtime 模块）为 GROVE-only 实现；`243dc19`（DB 二次隔离
  grove_math）为 GROVE-only 环境变更；五个封存 commit（`5e0fea7`/`09c2f9d`/`f86e13f`/`2979464`/
  `460ce36`）为 2026-09-28 封存动作本身。
- [ ] **W1.2 存在性矩阵收尾**。输入：`grove-docs-home-matrix.tsv`（当前 yes=17 / no=9）。任务：对
  9 个 `no` 行做主题级模糊匹配（同日期窗口 + 关键词），把 note 从
  `W1.2-fuzzy-match-needed` 升级为 `异号重复 / 改写 / 真缺失` 三值之一；真缺失项回填
  `poc-registry.tsv` / `research-registry.tsv`（若属 POC/研究线）。
- [ ] **W1.3 版本 drift 核对（文件对清单）**：
  - ORIGIN `dev-docs/146-v4-2026-08-05-审计方法论手册-*.md`（`19ca14d` 封存版）↔ HOME 同名文件：
    `diff` 定性（等价 / HOME 更新 / ORIGIN 独有修改）；
  - ORIGIN `dev-docs/147-v1-2026-08-05-Phase实现启动SOP-*.md` ↔ HOME 同名文件：同上；
  - ORIGIN `AGENTS.md` / `ChangeLog.md`（`56508a7` 封存版）↔ HOME 对应期版本；
  - ORIGIN `用户需求.md` ↔ HOME `用户需求.md`：逐字 diff。
- [ ] **W1.4 对账结论写回**：`repo-group-registry.tsv`（GROVE/ORIGIN 行 notes）、
  `topology-findings.md` §3、`grove-docs-home-matrix.tsv`（note 列）、必要时
  `dev-docs/git-history-reconstruction/` 各 registry。
- [ ] **W1.5 已闭合事实登记**（本轮已查明，直接写入对账 TSV 作首行结论）：HOME 从未有过三个
  runtime 模块（grove-only 实现 + grove 内删除，父提交可恢复）；ORIGIN 封存内容除 `backups/` 外
  均与 HOME 内容级重复（representation/ 24 文件、163-166 号、183/184 号、用户需求.md 均在 HOME
  tracked）；`backups/arango/20260806` 为 ORIGIN 独有。

## W2 上传前 Gate 执行准备（生产仓只读为原则；改写只在 scratch clone 演练）

- [ ] **W2.0 重扫基线**：按 `preupload-inventory/README.md` 固定命令重跑四份 inventory，替换基线；
  同时复扫 untracked/ignored 新增内容。
- [ ] **W2.1 token 清除（文件级顺序）**：按 `inventory-token.tsv` 的 HOME 目录优先级逐目录清零——
  `runs/`(82 文件) → `Tell分类学研究过程文档/`(72) → `dev-docs/`(51) → `xishujuzhen/`(36) →
  `system/`(31) → `palyground/`(29) → `subagent-docs/`(16) → `第六代系统研发过程文档/`(14) → 其余；
  每目录完成后即时复扫归零并在本项打勾。ORIGIN(33)/GROVE(190) 同法。
- [ ] **W2.2 口令清除 + 轮换**：`inventory-secret.tsv` 逐文件（HOME 重灾区 `subagents-dirs/`
  358、`xishujuzhen/` 30、`scripts/` 19）；**同时轮换 ArangoDB 该口令本身**（历史上曾大量暴露）。
- [ ] **W2.3 私有路径相对化**：`inventory-privatepaths.tsv`（HOME 564+620 文件）；策略=绝对路径改
  相对/匿名 ID + 本地附录（沿用本目录既有模式）。
- [ ] **W2.4 邮箱甄别**：`inventory-emails.tsv` 抽样 30 文件分类（arxiv 论文作者 / 项目身份 /
  偶然命中），产出保留/脱敏两清单待用户裁定。
- [ ] **W2.5 大文件决策**：清单化 >5M 文件（已知：GROVE `runs/guided_002/tmux_pipe.log` 31M、
  `guided_003` 4.7M、`bare_q2` 4.0M；GROVE .git 已 450M）；逐文件定 LFS / 排除 / 保留。
- [ ] **W2.6 历史改写 dry-run（scratch clone，不动生产仓）**：对 HOME/ORIGIN/GROVE 各建 scratch
  clone，`git filter-repo` 替换（token + 口令 + 私有路径）。验证 checklist：
  commit 总数守恒（HOME 1402 / ORIGIN 302 / GROVE 601）；SHA 重写映射落盘；四份 inventory 复扫
  归零；`git log --all --format=%B` 复扫归零；关键 tag（`legacy-reconstruction-snapshot-*`、
  GPT-5.6 两 tag、审计方法论手册、调整AGENTS.md之前）重打且指向语义等价位；tree diff 仅预期
  变更。
- [ ] **W2.7 许可证**：对齐生态 MIT；Master-Mind 首 wave 携带 LICENSE。
- [ ] **W2.8 Gate 通过判据**：三仓 token/口令/私有路径（内容+历史 message）复扫全部归零；大文件
  决策闭合；邮箱裁定完成；scratch 演练全部 PASS。

## W3 上传 wave 化（每个 wave 需用户当轮明确授权）

- **Wave 0（演练）**：W2.6 的 scratch 改写与验证，不触碰生产仓与 GitHub。
- **Wave 1（主容器初始化）**：Master-Mind 接收 HOME glm5.2 改写后史为主干；同批推送分支
  `codex/governance-alignment-2026-08-24`（3 独有）、`codex/sixth-gen-current-repo-2026-08-24`
  （11 独有）与重打后的 snapshot tag。DoD（文件级）：远端 refs 与 §1.3 保全清单一致；GitHub 页面
  抽查 token=0；全新临时目录 clone 后按 README/治理入口/数据 manifest 可恢复工作（社区可恢复
  判据）。
- **Wave 2（源头分支）**：ORIGIN main（`36d5e85`，302 commits）作 `legacy-origin-main` 分支推送，
  或将其 3 个封存 commits merge 入主干——二选一，**待用户裁定**。
- **Wave 3（引擎支线）**：GROVE glm5.2（`460ce36`，601 commits）作 `legacy-grove-glm5.2` 分支推送；
  是否 merge 其 37 独有 commits 待 W1 对账结论后裁定。
- **Wave 4（可选历史标记）**：ORIGIN `parallel-work` + `worker/W1/auto.220` + `worker/W2/auto.221`
  分支、ORIGIN/GROVE 全部 tags——**是否保全待用户裁定**。

## W4 SUPERVISOR / feasibility 线（其自身治理，低优先）

- [ ] A-FEASIBILITY（experiment 克隆，`codex/trace-restructure-feasibility`@`537412bb`）与 HOME 的
  Trace generation 对账——结论写入 SUPERVISOR 自身资产，不进本 repo。

## 待用户裁定项（阻塞 W2.6 之后所有动作）

1. ORIGIN 3 个封存 commits：merge 入主线，还是分支保全？
2. worker 分支与各仓 tags 是否上传？
3. ArangoDB 口令轮换的执行窗口。
4. W2.4 邮箱保留/脱敏清单。
5. 各 wave 的授权节奏（可一次性预授权 Wave 0 演练，其余逐 wave）。

## 与 second-pass 的关系

W1 全部任务在 `devin-execution-contract.md` 的 second-pass 框架内执行（复用其批次/恢复/写回合同）；
本方案只新增对账对象与输出 schema，不改变其 ledger/分母/next item。GROVE/HOME 内容对账结论最终
回流 `system-architecture.md` 与各 registry。
