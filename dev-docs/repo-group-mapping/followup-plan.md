# Repo 群后续工作方案（文件级 checklist 版）

> 生成：2026-09-28；**执行状态更新：2026-09-28 全量执行轮**（用户指令"全部做完并自我审计，
> 危险操作前确保可修复"）。生产三仓全程零写入（只读、均已提交），一切改写只发生在 /tmp 一次性
> scratch 镜像——可修复性由构造保证。push/上传仍停在逐 wave 授权 Gate（公开曝光不可撤销）。
> 本文件不改变冻结快照 1,399 分母与 second-pass next item。

## 0. 配套清单资产（本方案引用的文件级数据）

| 资产 | 内容 | 状态 |
|---|---|---|
| `grove-unique-commits.tsv` | GROVE 独有 37 commits 全列 | 已生成并消费（W1.1） |
| `grove-home-reconciliation.tsv` | 37 commits 逐个对账结论（blob 级） | 已生成（W1.1） |
| `grove-docs-fuzzy-match.tsv` | 15 份缺失文档主题词 HOME 命中明细 | 已生成（W1.2） |
| `grove-docs-home-matrix.tsv` | 独有内容在 HOME 存在性矩阵（37 行） | 已生成并两轮更新 |
| `preupload-inventory/inventory-*.tsv` | 敏感内容逐文件基线（四类） | 已生成（W2.0 复核） |
| `scrub-dryrun-report-2026-09-28.md` | Wave 0 改写演练全记录 | 已生成（W2.6 PASS） |
| `paths.local.md` | 成员真实路径（gitignored，永不入库） | 维护中 |

## W1 GROVE↔HOME/ORIGIN 内容级对账 —— **全部完成**

- [x] **W1.1** 37 个 GROVE 独有 commits 逐个对账 → `grove-home-reconciliation.tsv`。结论：
  22 path_absent（真独有：树生长引擎实现/sessions.db 管线/devin rules/293-302 号元文档）、
  9 same_name_diff_content（迁移与隔离环境适配）、5 partial、1 blob_full（`5e0fea7` 225-253 号
  13 份与 HOME 完全相同）。
- [x] **W1.2** 存在性矩阵收尾 → `grove-docs-fuzzy-match.tsv` + 矩阵 37 行。结论：293-302 号
  主题词 HOME 零命中=真缺失；303-307 号=异号延续（Tell分类学线）；**HOME dev-docs 编号止于 292，
  两线编号在 293 分道**。
- [x] **W1.3** 版本 drift 核对：146 号两仓 blob 相同（`851b0e2`）、147 号 diff 零；AGENTS.md 差
  1043 行为代际差异（方法论本体 vs 重建宪法）；ChangeLog 176 行为 HOME 超集；用户需求.md 差 54
  行——ORIGIN 封存版为用户原话完整版，HOME 版为精简编辑版（原话版保留独立价值）。
- [x] **W1.4** 写回：topology-findings §3 重写、矩阵/registry/MEMORY 同批更新。
- [x] **W1.5** 已闭合事实登记（对账 TSV 与 §3）：HOME 从未有 3 个 runtime 模块；ORIGIN 独有
  arango 备份；runs 证据 292/293 blob 已在 HOME。

## W2 上传前 Gate 执行准备 —— 分析项全部完成；清除配方已演练验证

> 执行原则（本轮明确）：**生产仓不做内容改写**（保持本地工作真值与脚本可用性）；四模式清除
> 完整发生在上传副本（scratch 改写），由 inventory 复扫归零作通过判据。

- [x] **W2.0** 重扫基线（修正 inventory README 自指污染后四项计数回到 394/435/564+620 基线）。
- [x] **W2.1-W2.3**（token/口令/私有路径清除）：已在 scratch 三仓镜像全量执行并验证归零
  （见 `scrub-dryrun-report-2026-09-28.md` 结果矩阵）；生产仓内容不动。
- [x] **W2.4** 邮箱甄别：inventory-emails.tsv 分类——531/535 在 `knowledge/`（arxiv 论文全文，
  公开作者邮箱），仅 4 文件在 `dev-docs` 需人工甄别。保留/脱敏清单待用户裁定（待裁定项 4）。
- [x] **W2.5** 大文件清单：三仓共同 tracked `knowledge/arxiv/metadata_all_2023plus.json` **343MB
  （超 GitHub 单文件 100MB 硬限）**、8 个 26-36MB `meta_*.json`、HOME `runs/guided_002/tmux_pipe.log`
  81MB。建议：metadata 系移出 Git 改 manifest 模式（同题库先例）或 LFS——待用户裁定（新增
  待裁定项 8）。
- [x] **W2.6** 历史改写 dry-run：**PASS**。三仓镜像（`--no-local` 无硬链接）Pass1（replace-text
  +replace-message）+ Pass2（sample_capture 目录移除）+ codex 检查点 ref 排除后，**全对象存储四
  模式归零**；commit 数守恒（302/601/1404；codex 分支 1401/1409）；tag 名保全 3/4/10。过程发现：
  replace-text 跳过二进制 blob——sample_capture 5 个 `.bin` 内含**真实 Devin session JWT**
  （凭证暴露，须轮换），已按整目录移除演练。
- [x] **W2.7** 许可证决策记录：对齐生态 MIT；LICENSE 随 Wave 1 落地。
- [ ] **W2.8** Gate 通过判据：四模式归零已证 ✅；二进制凭证专项扫描已做 ✅（结论：真实凭证仅
  sample_capture 两枚 Devin JWT，移除配方已全覆盖；catalog 的 hf_ 形态串为 Arango `_key` 假阳性）；
  **仍开**：邮箱裁定（项 4）、大文件处置（项 8）、两项凭证轮换（项 3/7）。

## W3 上传 wave 化（每个 wave 需用户当轮明确授权；本轮零执行——by design）

- Wave 0（演练）：✅ 已完成（W2.6）。
- Wave 1（主容器初始化）：Master-Mind 接收 HOME glm5.2 改写后史；同批推送两个 codex 分支与
  重打 snapshot tag；**显式排除 `refs/codex/turn-diffs/checkpoints/*` 工具检查点命名空间**。
- Wave 2（源头分支）：ORIGIN main 302 commits 作 `legacy-origin-main` 或 merge 封存 3 commits
  ——待裁定项 1。
- Wave 3（引擎支线）：GROVE glm5.2 作 `legacy-grove-glm5.2`；对账已完成（W1），merge 与否转为
  可决策状态。
- Wave 4（可选）：worker 分支与全部 tags——待裁定项 2。

## W4 SUPERVISOR / feasibility 线 —— 完成（分析部分）

- [x] A-FEASIBILITY lineage：HOME 的 clone（origin=HOME），HOME tip 为其祖先，+15 个 trace
  实验 commits，HEAD `537412bb`（2026-08-25）。写入 SUPERVISOR 自身资产的结论由其治理线执行
  （本 repo 已在 topology-findings §3 记录同样事实）。

## 待用户裁定项（阻塞 W2.8 收口与 W3 全部动作）

1. ORIGIN 3 个封存 commits：merge 入主线，还是分支保全？
2. worker 分支与各仓 tags 是否上传？
3. ArangoDB 口令轮换的执行窗口。
4. 邮箱保留/脱敏清单（4 个 dev-docs 文件 + 项目身份类邮箱策略）。
5. 各 wave 的授权节奏（可先授权 Wave 1）。
6. **新增**：`sample_capture` 目录从上传历史整体移除的正式确认（演练已按此执行，commit 数无
   副作用）。
7. **新增**：两枚 Devin session JWT 轮换/失效确认（sample_capture 的 chatmsg_001/002，历史内
   已暴露；移除配方已覆盖上传侧，轮换覆盖暴露侧）。
8. **新增**：343MB metadata 大文件处置（LFS vs manifest 外置）。

## 与 second-pass 的关系

W1 对账已闭合本方案范围；second-pass 仍按 `devin-execution-contract.md` 原计划推进（ordinal 2
path-group），293-302/303-307 的缺失文档如需纳入重建注册表，由 second-pass 在到达相应 ordinal 时
按既有合同处理。本方案不改变其 ledger/分母/next item。
