# Eight System

> 对 seven-system 及其前置"非特化"研究过程的设计复杂度调查、过度设计分析，筛选后的可审计非特化方案，以及Phase 0实验验证。

## 目录结构

```
eight-system/
├── NEW_AI_ONBOARDING.md               ← 新AI入口文档（先读这个）
├── README.md                          ← 本文件（文档索引）
├── docs/                              ← 文档（调查、筛选、方案）
│   ├── 386-v0-...-seven-system设计复杂度评估.md
│   ├── 非特化研究文档体系调查.md
│   ├── 非特化研究过程的过度设计调查.md
│   ├── 筛选标准与编排方案.md
│   ├── 非特化方案-v1.md               ← 核心方案文档（8个部分）
│   ├── 总筛选审计表.md
│   ├── 实现路径建议.md                 ← [已被方案§8替代，保留为历史记录]
│   └── 筛选产出/                      ← 5个subagent的精简文档和审计表
│       ├── S1-核心理论-*.md
│       ├── S2-分类学认知-*.md
│       ├── S3-非特化定义与出题经验-*.md
│       ├── S4-TellCore与CaseCard-*.md
│       └── S5-合理设计决策-*.md
├── src/                               ← 源码
│   └── tellcores/
│       └── local_global_switch.yaml   ← TellCore v0定义
├── scripts/                           ← 脚本
│   └── contrast_calculator.py         ← contrast自动计算
└── runs/                              ← 实验运行
    └── phase0/                        ← Phase 0实验
        ├── preregistration.md         ← 预注册文档
        ├── experiment_report.md       ← Phase 0实验报告
        ├── experiment_report_step4.md ← Step 4 continue实验报告
        ├── evidence_record_001.md     ← EvidenceRecord
        ├── contrast_results.json      ← 自动计算结果
        ├── 1631_R_bare.txt            ← 4组对照prompt
        ├── 1631_L_lineage.txt
        ├── 1631_D_direction.txt
        └── 1631_LD_lineage_direction.txt
```

## 文档索引

> **交接与当前状态**：[HANDOFF.md](HANDOFF.md)——工作线全景、第一圈staged状态与重启命令、待决策事项（2026-08-16）。

### 第一阶段：调查与分析

| 文档 | 行数 | 内容 |
|---|---|---|
| [seven-system设计复杂度评估](docs/386-v0-2026-08-15-seven-system设计复杂度评估.md) | 162 | 从架构、文档、代码、测试、git历史五个维度通读 seven-system v0.1.0 后的批判性分析。判断：需求复杂度约30-40%，过度设计约60-70%。 |
| [非特化研究文档体系调查](docs/非特化研究文档体系调查.md) | 452 | 从git log和文档内容追溯seven-system构建前5天的"非特化"研究文档体系：000号根定义→277-289 POC-VMS→333-348 Tell分类学→349-373 非特化策略深化→386-389 证据工厂设计。共约34,000行。 |
| [非特化研究过程的过度设计调查](docs/非特化研究过程的过度设计调查.md) | 318 | 调查研究过程本身是否存在过度设计。结论：认知增量比仅9-19%，过早系统化和膨胀占58-81%。识别四个过度设计模式：过早全面化、重复学习、治理递归、文档膨胀。 |

### 第二阶段：筛选与方案

| 文档 | 行数 | 内容 |
|---|---|---|
| [新AI入口文档](NEW_AI_ONBOARDING.md) | 164 | 给新AI的入口文档：3句话理解全局 + "中"的guardrail + 阅读顺序 + 任务定义 + 过度设计防护 + 实现约束。**anti-351号**——同时传递理论、约束和防护。 |
| [筛选标准与编排方案](docs/筛选标准与编排方案.md) | 104 | 5个subagent的统一筛选指令：保留标准R1-R5、剔除标准D1-D6、待定标准T1-T3、编排方案。 |
| [非特化方案-v1](docs/非特化方案-v1.md) | 613 | **核心方案文档**。从34,000行研究文档中筛选整合的可审计非特化方案。8个部分：核心理论、分类学认知、非特化定义（§3已按"中"缩减）、TellCore与CaseCard、出题经验、合理工程约束、六门审计、实现路径（含Phase 0结果+§8.5"中"的定位注）。 |
| [总筛选审计表](docs/总筛选审计表.md) | 111 | 汇总5个subagent的筛选审计表。保留~144项、剔除~56项、待定~19项。含388号历史证据重新定级表和CC-013数学错误降级记录。 |
| [实现路径建议](docs/实现路径建议.md) | 224 | Phase 0之前的实现路径规划。**已被方案§8吸收并更新**，保留为历史记录。 |
| [钟形曲线到帕累托前沿的演化分析](docs/钟形曲线到帕累托前沿的演化分析.md) | 572 | 追踪"钟形曲线"（345号）到"帕累托前沿"（372号）的演化路径，识别非特化研究本身的钟形曲线峰值在345-347号，371/372号越过峰值。含345/352/371/372号原文落盘、351号委托提示词分析、Phase 0实验数据、方案缩减建议、来源文档索引。 |

### 筛选产出（5个subagent的精简文档和审计表）

| 模块 | 精简文档 | 审计表 |
|---|---|---|
| S1 核心理论（000+277-289） | [精简文档](docs/筛选产出/S1-核心理论-精简文档.md)（423行） | [审计表](docs/筛选产出/S1-核心理论-筛选审计表.md)（55行） |
| S2 分类学认知（333-348） | [精简文档](docs/筛选产出/S2-分类学认知-精简文档.md)（544行） | [审计表](docs/筛选产出/S2-分类学认知-筛选审计表.md)（64行） |
| S3 非特化定义+出题（349-373） | [精简文档](docs/筛选产出/S3-非特化定义与出题经验-精简文档.md)（777行） | [审计表](docs/筛选产出/S3-非特化定义与出题经验-筛选审计表.md)（68行） |
| S4 TellCore+CaseCard（382+383+388） | [精简文档](docs/筛选产出/S4-TellCore与CaseCard-精简文档.md)（1103行） | [审计表](docs/筛选产出/S4-TellCore与CaseCard-筛选审计表.md)（55行） |
| S5 合理设计决策（387+389） | [精简文档](docs/筛选产出/S5-合理设计决策-精简文档.md)（357行） | [审计表](docs/筛选产出/S5-合理设计决策-筛选审计表.md)（49行） |

### 决策记录（治理决策，持续追加）

| 文档 | 行数 | 内容 |
|---|---|---|
| [两棵树实现时机与基本实践方式](docs/两棵树实现时机与基本实践方式.md) | 130 | 2026-08-16两次问答完整落盘：①非特化研究阶段不实现两棵树（树缓建+记录树形化可回填+四条毕业条件）；②每轮研究必须是核心循环的一次真实旋转（五个真实动作亲手完整执行）。用户确认，新AI必读。 |

### 第三阶段：Phase 0 实验验证

| 文档/文件 | 行数 | 内容 |
|---|---|---|
| [预注册文档](runs/phase0/preregistration.md) | 78 | R/L/D/LD四组对照的预注册文档（冻结于结果前） |
| [Phase 0实验报告](runs/phase0/experiment_report.md) | 117 | 完整实验报告：4组结果、contrast计算、关键发现（含Step 4修正说明） |
| [Step 4实验报告](runs/phase0/experiment_report_step4.md) | 164 | Continue实验 + 钟形曲线实证补充：L在continue后立即输出proof，D/R失败；指导力需分层测量（认知维度vs执行维度） |
| [EvidenceRecord 001](runs/phase0/evidence_record_001.md) | 99 | 第一条contrast级EvidenceRecord（含Step 4更新） |
| [contrast_results.json](runs/phase0/contrast_results.json) | 137 | 自动计算的contrast结果（JSON） |
| [TellCore v0 YAML](src/tellcores/local_global_switch.yaml) | 48 | TellCore v0定义（局部-全局表示切换，7字段最小充分集） |
| [contrast_calculator.py](scripts/contrast_calculator.py) | 297 | contrast自动计算脚本（从sessions.db提取thinking判定路线层/证明层） |

### 第四阶段：POC预注册（Step 5-7）

| 文档/文件 | 行数 | 内容 |
|---|---|---|
| [Phase 1预注册](runs/phase1/preregistration.md) | 123 | 跨题泛化验证（1843/1709/1962的R/L/D/LD+continue）。验证"认知支架"假说跨题成立，1962是关键测试（操作路径瓶颈） |
| [Lineage分解预注册](runs/lineage_decomp/preregistration.md) | 108 | Lineage分解实验（L1结论/L2推导过程/L3完整）。验证认知支架的核心是结论锚点还是过程锚点 |
| [Phase 2预注册](runs/phase2/preregistration.md) | 146 | Selector验证（false_friend/boundary题）。验证误触发率和Selector预测准确率 |

### 第五阶段：Mid-Hint实验（Step 5修正版——半路提示）

| 文档/文件 | 行数 | 内容 |
|---|---|---|
| [Mid-Hint行动方案](runs/midhint/preregistration.md) | 446 | **完备的行动方案文档**。从Phase 0/1的"前缀Hint"修正为"半路Hint注入"——AI先跑到出错→系统识别中间节点→给非特化Hint→AI从中间继续。理念部分完整记录：核心命题、用户设计意图、与283号tree组的关系、277号"99%不相识"命题、非特化Hint层次结构、与第五代三个推动关系的对应、正交出题核心理念、bare失败题来源。 |

#### 选题数据来源（Mid-Hint实验输入）

Mid-Hint实验需要"标准解答用了局部-全局切换，但AI没走这个方向"的题。选题数据来自错题分析系统的三Pipe流程：

| Pipe | 产出文件 | 状态 | 说明 |
|---|---|---|---|
| Pipe 1（分析） | [analysis_summary.md](../analysis-devin-failure-system/output/analysis_summary.md) | ✅ 完成 | 2050条分析结果，1589个唯一题目，1096个DIRECTION_ERROR |
| Pipe 2（审计） | [audit_summary.md](../analysis-devin-failure-system/output/audit-full1/audit_summary.md) | ✅ 90%完成 | 1385个审计完成，721个PASS_SELECTABLE可选题，135个重跑中 |
| Pipe 3（选题） | — | ⏳ 未开始 | 从721个PASS_SELECTABLE中按Mid-Hint标准选题，对d2=other做语义再分类 |

**选题方案**：详见 [dev-docs/387号](../dev-docs/387-v0-2026-08-16-错题分析系统审计与选题方案.md)（三Pipe方案，FROZEN）

## 文档关系

```
第一阶段：调查与分析
  seven-system设计复杂度评估        ← seven-system 代码/文档/测试的过度设计分析
      ↑ 溯源
  非特化研究文档体系调查             ← seven-system 构建前的完整研究脉络梳理
      ↑ 深入
  非特化研究过程的过度设计调查        ← 研究过程本身的过度设计分析

第二阶段：筛选与方案
  筛选标准与编排方案                 ← 5个subagent的统一筛选指令
      ↓ 执行
  5个subagent并行筛选                ← 34,000行 → 3,204行精简内容（~9.4%）
      ↓ 整合
  非特化方案-v1                      ← 可审计的非特化方案（8个部分，含Phase 0结果）
  总筛选审计表                       ← 完整的筛选追溯（保留/剔除/待定）
  实现路径建议                       ← [已被方案§8替代，历史记录]

第三阶段：Phase 0 实验验证
  预注册文档                         ← R/L/D/LD四组对照的预注册
      ↓ 执行
  Phase 0实验报告                    ← 4组结果 + contrast计算
      ↓ 深入
  Step 4实验报告                     ← continue实验，假说修正
  EvidenceRecord 001                 ← 第一条contrast级证据
      ↓ 反馈
  非特化方案-v1 §8                   ← 实现路径更新（Step 1-4完成，Step 5-8规划）

元层次分析
  钟形曲线到帕累托前沿的演化分析      ← 识别非特化研究本身的钟形曲线峰值
      ↓ 反馈
  非特化方案-v1 §3缩减               ← 九个可→三个可，8维向量→T1/T2例子
  非特化方案-v1 §8.5定位注           ← 每个Step标注验证的峰值维度

第四阶段：POC预注册（Step 5-7）
  Phase 1预注册                      ← 1843/1709/1962跨题泛化验证
  Lineage分解预注册                  ← L1结论/L2推导过程/L3完整
  Phase 2预注册                      ← false_friend/boundary题Selector验证
```

## 核心发现

### 调查阶段发现

seven-system 的过度设计不是工程化阶段引入的，而是从研究过程直接继承的。治理递归的种子在 372号（24项契约+六门审计），在 387号完全展开（74个Gate），在 seven-system 工程化（561个错误码+638条规范）。研究过程本身的过度设计比例（58-81%）甚至高于 seven-system（60-70%）。

### 筛选阶段发现

从34,000行研究文档中筛选出3,204行精简内容（~9.4%），与调查文档识别的9-19%认知增量比一致。保留~144项（R1认知推进/R2实验证据/R3可复用工件/R4合理工程约束/R5负证据），剔除~56项（D1过早全面化/D2重复学习/D3治理递归/D4文档膨胀/D5无关工具/D6过早POC框架），待定~19项（T1未验证理论/T2过早框架/T3过早工件）。

### Phase 0 实验发现

1. **Lineage alone足以引导route finding** — L（只有脉络）自己发现了QR/Euler方向（thinking中8处"quadratic residue"）
2. **Route finding ≠ Proof completion** — L和D都找到路线但hit token limit，只有LD完成proof
3. **TellCore v0的价值在于认知支架（cognitive scaffold）** — Step 4 continue实验修正了原"token efficiency"假说：L在thinking中已完成证明（continue后立即输出），D未完成（continue后从头开始再次失败）。L和D的thinking长度相似（105K chars），差异在于lineage提供了推理锚点
4. **Proof-level C2=1** — lineage和direction在proof completion上有正向交互效应

## 当前状态与下一步

**已完成**：
- Phase 0（Step 1-4）— 1631题的R/L/D/LD四组对照 + continue实验
- Phase 1 — 1843/1709/1962跨题泛化验证（前缀Hint对照，认知支架有难度阈值）

**当前**：Mid-Hint实验（Step 5修正版——半路提示）
- 从Phase 0/1的"前缀Hint"修正为"半路Hint注入"——回到第五代系统核心设计
- 完备行动方案已落盘：[runs/midhint/preregistration.md](runs/midhint/preregistration.md)（446行，理念+设计+SOP完整记录）
- 下一步：构造正交新题（从1631/1843的TellCore机制派生，Level 3-4正交）→ bare跑正交新题 → 从thinking提取脉络到卡点 → 注入非特化Hint → 测试半路提示有效性

**关键修正**：Phase 0/1偏离了用户设计意图——做的是"前缀Hint对照"（预先写在prompt开头），不是"半路Hint注入"（AI先跑到出错后从中间节点注入）。Mid-Hint实验回到用户设计意图和第五代核心循环。
