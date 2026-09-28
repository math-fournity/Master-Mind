# Repo Group Mapping — 多代系统 repo 群梳理入口

> 职责边界：本目录登记"多代系统线"相关的本地 repo 群（核心 Git 实体、外围成员、排除项、负结论与
> 相邻发现），固化 Git 拓扑结论、2026-09-28 未提交内容封存战役的收据，以及 GitHub 整备（Master-Mind）
> 的处置提案与上传前 Gate。它与 `dev-docs/git-history-reconstruction/` 平级：**不改变冻结快照 1,399
> 分母，不改变 second-pass next item（ordinal 2 path-group）**。

## 本轮用户裁定（2026-09-28 会话）

1. 本轮只关注**与多代系统有关**的 repo 群；**续传解题系统、简单解题系统不在本轮范围**（两者在
   GitHub 侧已有独立公开仓，见 `topology-findings.md` §5 对位表）。
2. 外围成员裁定：FEITEHUA 与 SUPERVISOR **均纳入**登记（外围身份，不改变核心三仓地位）。
3. 探测不到内容的路径按**不存在**处理，登记为负结论。
4. GitHub 目标：主 repo 暂定 `math-fournity/Master-Mind`（账号 `math-fournity@proton.me`；已探测为
   public 空仓）。repo 群在 GitHub 侧可合为一个 repo。
5. **上传硬约束：上传内容中绝不允许出现本项目本地目录名所用的敏感 token（无论前缀/中缀/后缀）。**
   因此本目录所有入库文件用匿名 ID 指代各成员；真实本地路径只记录在 gitignored 的
   `paths.local.md`。
6. 上传目标 = **社区任何人在任何机器上都能恢复工作**（不是仅本地可恢复）：原始外部语料不入 Git、
   以清单+日志+精选产物形态保全；治理文档按陌生人可接手标准书写。
7. 未提交内容必须**先调查、再分批提交**；多分支工作不得丢失任何分支的独有内容（含未合并分支、
   worker 分支、脏工作区）。

## 成员一览

| ID | 类别 | 一句话身份 |
|---|---|---|
| ORIGIN | 核心 | D 盘源头主仓库：数学大师制造项目本体（星学继承→xishujuzhen 方法论→Phase 0-7） |
| GROVE | 核心 | ORIGIN 的 clone：第六代 Grove 树生长引擎线（225-307 号研究+题库+实验） |
| HOME | 核心 | ORIGIN 的 clone：glm5.2 主线（全代际史+当前治理重建，即本 repo） |
| FEITEHUA | 外围 | 非特化 POC 设计验证 AI 的角色目录（零历史，2026-09-28 建立保全提交） |
| SUPERVISOR | 外围 | Trace 驱动全 repo 重整的 AI 控制面（独立 Git，不存业务代码） |
| X-AISTUDIO-MATH / X-PROOFS | 排除 | 外部语料数学发现库 / 证明证据库（语料线，与多代无关且隐私风险高） |
| X-CODEX-PATH | 负结论 | 用户清单中的路径探测无任何内容，按不存在处理 |
| A-AISTUDIO-SOURCE / A-FEASIBILITY | 相邻发现 | 语料源树 / supervisor 实验用非浅 clone（登记不纳入） |

明细（Git 身份、分支、世代覆盖、GitHub 处置提案、风险、证据等级）：`repo-group-registry.tsv`。
拓扑结论、封存战役收据、GitHub 生态对位与上传前 Gate：`topology-findings.md`。
**后续工作方案（文件级 checklist 版）**：`followup-plan.md`（W1 内容对账 / W2 Gate 执行准备 /
W3 上传 wave 化 / W4 / 待裁定项）。
清单资产：`grove-unique-commits.tsv`（GROVE 独有 37 commits）、`grove-docs-home-matrix.tsv`
（独有内容在 HOME 的存在性矩阵）、`preupload-inventory/`（敏感内容逐文件基线，重生成命令见其
README）。
本地绝对路径映射：`paths.local.md`（**已 gitignore，不入库**）。

## 进度

- first-pass 完成（2026-09-28 单会话）：范围裁定、机械勘察、拓扑三问、未提交内容封存（ORIGIN 3
  commits / GROVE 5 commits / FEITEHUA 1 commit，三仓工作区均 clean）、敏感内容量化扫描、GitHub
  目标与既有生态对位、Gate 清单落盘。
- 同日补做：后续工作方案 checklist 化（`followup-plan.md` + 三类清单资产）；fork 点复核修正——
  GROVE↔HOME 真实 fork commit 为 `2596dcf`（2026-08-08 07:53），first-pass 曾误读为 `2e33663`
  （实为共享段早期 commit），修正详情见 `topology-findings.md` §1.2。
- 开放项：GROVE 独有 commits 与 HOME 的内容级对账、ORIGIN/GROVE 方法论文档版本 drift、分支与
  tag 的上传保全决策、LFS 决策——均不阻塞 second-pass，留待相应阶段。

## 边界

- 本目录是调查资产，不是当前系统真值；稳定结论定型后再按治理框架沉淀到 README/Feature/MEMORY。
- 本轮未对任何 GitHub 账号执行写操作；上传是需要用户逐 wave 明确授权的未来动作。
- 对 ORIGIN/GROVE/FEITEHUA 等外部仓的写入仅限 2026-09-28 封存战役本身（用户当轮授权），此后恢复
  只读。
