# Master-Mind（大师头脑）

> **数学大师制造系统 · 多代系统线全集**——本仓库合并保存了该系统从星学方法论继承起步、
> 经 xishujuzhen 依赖图导航、Grove 引导树核心循环、第六代系统巩固、Seven/Eight 证据工厂，到
> 2026-08 治理重建期的全部 Git 历史。任何感兴趣的人都可以在本仓库中恢复这段工作的上下文并
> 接续推进。

---

## 一、这个仓库是做什么的

本项目是一个 **AI 数学大师制造系统**的完整研发史与工作现场。系统的目标不是"会做题的解题
机器"，而是能做数学研究的 AI——提出猜想、构造证明、在复杂问题面前知道该从哪个方向切入。

核心方法论（自源头仓库继承）：

- **"知道该判断什么"的工程化**：系统不做数学判断，只做依赖计算与提示生成——经典计算负责
  确定部分（类型过滤、遍历、模式匹配、稀疏候选），AI 在提示下完成判断；
- **Grove 核心循环**（第六代定型）：引导树（给方向 Q）→ 推理 AI（探索）→ 解题树（记录结果）→
  在终点节点检索 → 引导树新边 → 启动新推理 AI。两棵树是同一棵树的两个面；
- **tell/hint 原语**：从推理 AI 的 thinking 中识别"没走的分叉"（tell），翻译成给下一个 AI 的
  方向提示（hint），存入数据基座（ArangoDB）；
- **稀疏关系视图**：K（数学语义）/ T（事件状态）/ H（启发规则）三类投影，矩阵负责候选计算，
  不负责数学真值。

本仓库（main 分支）同时承载一个进行中的**治理任务**：对多代系统线全部历史的认知重建
（见下文"如何接手"）。

## 二、历史沿革

### 时间线（七个阶段）

| 阶段 | 时间 | 主题 |
|---|---|---|
| 1 | 2026-07-07..07-10 | 星学（astro/qizheng）遗留资产起步，方法论继承起点 |
| 2 | 2026-08-02..08-05 | xishujuzhen 转向与早期 POC；Phase 0-7 证据等级线（DYN-0..7） |
| 3 | 2026-08-06..08-08 | Grove/tell-hint 认知与 VMS 形式化爆发期 |
| 4 | 2026-08-09..08-12 | 第六代系统巩固；FCA 框架对接、思维原语化 |
| 5 | 2026-08-13..08-17 | Seven/Eight 系统与非特化证据工厂 |
| 6 | 2026-08-18..08-22 | 续传/solver 分线、POC-2.5c |
| 7 | 2026-08-24 起 | 治理重建期：全历史认知重建成为项目宪法 |

### 三个源仓库与本仓库的关系

本仓库由三个本地仓库的完整历史合并保全而来（内容经机械脱敏后重写，见第八节）：

```
源头主仓库 (origin, D盘)                Grove 引擎仓库 (grove, D盘)
  main: 302 commits                      glm5.2: 601 commits
  星学继承→方法论本体→Phase 0-7           第六代 Grove 支线
        │                                      │
        └──────────── 共同基点 ────────────────┘
                  (2026-08-05, 299 commits 处)
                        │
                        ▼
       glm5.2 主线（现 main 分支, 1406+ commits）
       08-08 于 2596dcf 处与 Grove 支线分叉后持续演化：
       六代巩固 → seven/eight → 治理重建
```

- **源头主仓库**（→ `legacy/origin-main`）：整条代际线的源头，止于 2026-08-06 的 Phase 7 工作；
- **Grove 引擎仓库**（→ `legacy/grove-glm5.2`）：2026-08-08 迁移成独立仓库后走了 37 个独有
  commits（树生长引擎实现、293-307 号研究文档），止于"范式转变——从提取到查询"；
- **主线**（→ `main`）：全代际全集与当前治理重建现场。

> 注：上图及本 README 引用的形如 `2596dcf` 的编号是**内部原始 SHA**（合并前的各源仓库内可复
> 核）；脱敏重写后库内 SHA 已全部变化，与原始编号不一一对应。

## 三、分支索引（统一 `legacy/` 前缀）

除主线外，所有历史线一律使用 `legacy/` 前缀命名：

| 分支 | 来源 | 规模 | 说明 |
|---|---|---|---|
| `main` | 主线 worktree 仓库 glm5.2 | 1406+ commits | 全代际全集；进行中的历史认知重建现场 |
| `legacy/origin-main` | 源头主仓库 main | 302 commits | 星学继承与方法论本体；Phase 0-7 证据等级线 |
| `legacy/grove-glm5.2` | Grove 引擎仓库 glm5.2 | 601 commits | 第六代引擎支线；37 个独有 commits（树生长引擎、293-307 号文档） |
| `legacy/codex/governance-alignment-2026-08-24` | 主线并行分支 | 3 独有 commits | 2026-08-24 治理对齐工作线；其成果已被当时的基线封存吸收（保全性推送） |
| `legacy/codex/sixth-gen-current-repo-2026-08-24` | 主线并行分支 | 11 独有 commits（含上一分支） | 第六代现状盘点与退役预检线；同上，内容已并入主线，推送为叙事保全 |

**tag 说明**：`legacy-reconstruction-snapshot-2026-08-24`（1399-commit 冻结重建快照锚）、
`GPT-5.6启动/结束`（模型切换时代标记）、`审计方法论手册`、`调整AGENTS.md之前`、
`pre-*`/`devin-*`（治理节点备份锚）、`入题侧脉络分析全管线完成1.0`（管线里程碑）。

## 四、仓库组织架构（main 分支顶层导读）

**治理层**（接手工作先读这些）：

| 文件 | 职责 |
|---|---|
| `AGENTS.md` | 项目宪法：恢复路由、五方向完成门、安全边界 |
| `MEMORY.md` | 当前态与续做记录（current queue 在顶部） |
| `feature-list.md` / `rulings.md` | 当前要求与验收 / 用户原始裁定 |
| `README.md` | 历史资产导航地图（本文件之外的旧地图仍在 git 历史中） |
| `dev-docs/git-history-reconstruction/` | **当前主任务**：1399-commit 认知重建的 ledger/registries/合同 |
| `dev-docs/repo-group-mapping/` | repo 群梳理：三源仓库拓扑、对账结论、上传 Gate 与本 README 的源文件 |

**认知与文档层**：`GroveCoreCognition.md`（核心循环认知，最高优先级）、
`000-v0-*-引导树闭环-识别端结构定义.md`（tell/hint 根定义）、`Glossary.md`、`WorkPrinciples.md`、
`RulePointers.md`、`SystemAssets.md`、`ChangeLog.md`。

**研究过程文档群**（有日期的历史证据，非当前真值）：`Tell分类学研究过程文档/`（编号文档至
400+）、`第六代系统研发过程文档/`、`seven-system非特化证据工厂研发过程文档/`、
`devin大规模高并发题目测试系统技术说明书/`、`FCA学习笔记/`、`FCA知识点/`、`dev-docs/`
（编号过程文档+两个 active 调查目录）。

**系统与代码层**：`xishujuzhen/`（方法论本体实现：research_runtime、githooks 等）、`system/`
（第六代三层结构）、`seven-system/`、`eight-system/`、`analysis-devin-failure-system/`（错题
分析）、`solver-harness/`、`scripts/`、`tools/`、`master.py`。

**知识基座层**：`knowledge/`（arxiv 全文/元数据、problem_banks 精选批次）、`primitives/`
（原语目录）、`concepts/`、`facets/`、`criteria/`。

**运行与产物层**：`runs/`（实验运行现场，如 vms_test_1、fate/matharena 批次）、`POC-2.7/`、
`poc4_*`、`subagents-dirs/`、`subagent-docs/`、`palyground/`、`任务追踪/`、
`.devin/legacy/`（pre-E010 项目治理的 rules/skills 存档）。

## 五、未随库内容与数据基座说明

为保证"任何人 clone 即可恢复工作"且不超出托管平台限制，以下内容**有意不在库内**，均以
清单+再获取说明保全：

| 内容 | 规模 | 位置与恢复方式 |
|---|---|---|
| 原始外部题库语料（demidovich/mathnet/numina_math 等） | ~2.7GB | 见 `legacy/grove-glm5.2` 分支 `knowledge/problem_banks/DOWNLOAD-MANIFEST.md`（含来源与下载日志） |
| arxiv 汇总元数据 `metadata_all_2023plus.json` | 343MB | 超单文件托管上限，已从上传历史移除；分片元数据（`meta_*.json`）在库内 |
| ArangoDB 数据库本体 | 三库 | 不随库；导出与恢复方式见同账号 `AI-Math-Solving-Databases` 仓库 |
| AI 解题运行现场（当前世代/早期世代归档） | 5 万+ | 见同账号 `AI-Math-Solving-Trajectories` 与 `-Archive` 仓库 |
| 解题管线代码（平凡/竞赛续传系统） | - | 见同账号 `AI-Math-Normal-Solver`、`AI-Math-Competition-Problem-Solving-System` |

## 六、如何接手这项工作

1. 按 `AGENTS.md` 的恢复路由建立认知闭包（读 `MEMORY.md` 顶部 current queue →
   `feature-list.md`/`rulings.md` → 调查入口文档）；
2. **当前主任务**是历史认知重建：`dev-docs/git-history-reconstruction/README.md` 是调查入口，
   `devin-execution-contract.md` 是执行合同（批次、证据、恢复、完成门）；重建完成门通过前，
   不得做目录重塑/批量删除；
3. 重建的下一步已登记在该目录的 Progress/next item 中，从已提交 coverage 恢复，不重复已闭
   合批次；
4. 历史文档（研究过程文档群）是**有日期的证据**，未经 exact diff 与当前实物核对不得当作当
   前真值；
5. 2026-09-28 repo 群梳理与本次发布的完整自包含交接记录：
   `dev-docs/repo-group-mapping/session-record-2026-09-28.md`（裁定链、拓扑结论、封存与对账
   明细、脱敏配方、全部提交清单与剩余事项）。

## 七、相关仓库（同账号生态）

- `AI-Math-Solving-Trajectories` / `AI-Math-Solving-Trajectories-Archive`：解题运行现场（当前
  世代 / 早期世代 5 万+ 归档）；
- `AI-Math-Solving-Databases`：ArangoDB 数据表导出与题库目录；
- `AI-Math-Normal-Solver`：平凡解题系统（早期世代解题管线）；
- `AI-Math-Competition-Problem-Solving-System`：竞赛题持续解题系统（多轮续传管线）；
- 数学元理论线：`HoTT-Paradoxy`、`MATH-FOURNITY`、`Extensions-of-Some-Theorems-of-Goedel-and-Church`、`prove2me_manual`。

## 八、历史保真与脱敏声明

本仓库的历史在合并时经过了**机械脱敏重写**（Git SHA 已全部变化）：

- 本地绝对路径（用户目录/数据卷前缀）替换为 `~` 与 `/data` 相对形式；
- 项目内部代号统一替换；曾硬编码于历史中的数据库口令替换为 `REDACTED-DB-PASSWORD` 占位；
- 含真实会话凭证的 MITM 抓包目录与超过托管平台单文件体积上限的 343MB 元数据文件从上传
  历史中移除（本地原件保留）；
- 工具检查点 ref（`refs/codex/turn-diffs/*`）不上传。

commit 数量、分支结构、tag 语义在重写前后逐项核对守恒；重写配方与验证记录见源仓库治理
文档（`dev-docs/repo-group-mapping/scrub-dryrun-report`）。

## 九、许可证

MIT（见 `LICENSE`）。
