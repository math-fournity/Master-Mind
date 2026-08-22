# POC.md · 非特化研究 POC 测试总索引

> **所有 POC 测试的统一索引**——方案文档、数据资产、数据库数据、运行状态。
> **项目 rule 要求**：凡有新的测试出现，必须更新本文件（见 `.devin/rules/poc-registry-update.md`）。

---

## 总览

| POC | 名称 | 状态 | 方案文档 | 数据资产 | 数据库 | 证据文档 |
|---|---|---|---|---|---|---|
| POC-0 | CasePack冻结 | ✅完成 | 399号 | `poc_assets/poc_0/` | — | — |
| POC-0.5 | 变形关系声明 | ✅完成 | 400号 | `poc_assets/poc_0.5/` | — | — |
| POC-1 | 因果取商增强版 | ✅完成——重审产出候选v0.2已采纳(2026-08-22) | 401号+419号 | `poc_assets/poc_1/`(旧归档)+`poc_1/candidates_v0.2.yaml`(正式) | `poc_2.7.5/poc1rev/` | — |
| POC-2 | 可选择 | 待执行 | 402号 | `poc_assets/poc_2/` | — | — |
| POC-2.5 | 基础因果效应验证 | ⚠️执行中 | 398号 | `poc_assets/poc_2.5_round1/` + `poc_2.6/` | sessions.db | 2份(见下) |
| POC-2.6 | 续传机制验证 | ✅完成 | 399号(2.6) | `poc_assets/poc_2.6/` | sessions.db | 2份(见下) |
| POC-2.7 | 截断vs思维错误 | ⚠️执行中 | 415号 | `poc_assets/poc_2.7/` | ArangoDB | — |
| POC-2.7.5 | 续传发现对前置POC的影响评估 | ✅完成——1962终版判定：截断可救 | 416号 | `poc_assets/poc_2.7.5/` | — | — |
| POC-2.5c | 基础因果效应验证·弱因果版 | ⚠️Batch-1完成待裁决(2026-08-22)——T4/12vsC4/12配对对称零净效应+C组33%解出触发池污染条款，详见`poc_25c/batch1_EvidenceRecord.md` | 418号+`poc_2.7.5/v2/poc25c_experiment_design.md` | `poc_assets/poc_25c/`(全)+运行现场D盘poc25c-batch1 | ArangoDB(p27_continuation_runs选题池) | batch1_EvidenceRecord.md |
| POC-3.5 | Hint非特化程度验证 | 待执行 | 403号 | `poc_assets/poc_3.5/` | — | — |
| POC-3 | 可执行 | 待执行 | 404号 | — | — | — |
| POC-4 | 可终止 | 待执行 | 405号 | — | — | — |
| POC-6 | 可归责 | 待执行 | 406号 | — | — | — |
| POC-7 | 可持续学习简化版 | 待执行 | 407号 | — | — | — |
| POC-8 | 端到端闭环 | 待执行 | 408号 | — | — | — |
| POC-9 | 识别端验证 | 待执行 | 409号 | `poc_assets/poc_9/` | — | — |

**执行编排**：413号（`Tell分类学研究过程文档/413-v0-2026-08-17-非特化研究执行编排-*.md`）

---

## 历史VMS实验（POC系列的前身）

| VMS | 名称 | 状态 | 方案文档 | 数据资产 | 数据库 |
|---|---|---|---|---|---|
| VMS-8 | 脉络继承+方向注入 | ✅完成 | 281/282号 | `runs/vms_poc_0/` | ArangoDB |
| VMS-9 | tell端去特化+形式化过滤 | ✅完成 | 287/288号 | `runs/vms_poc_0/` | ArangoDB |
| VMS-10 | 拓扑相同且距离极近的tell区分 | ✅完成 | 289号 | `runs/vms_poc_0/` | ArangoDB |

**VMS实验结果文档**：
- 283号：POC-VMS-8实验结果（bare 0% → tree 67%）
- 288号：POC-VMS-9实验结果（tell端去特化验证）
- 289号：POC-VMS-10实验结果（小概念标记分辨）

---

## POC-2.6 续传机制验证（✅完成）

**方案文档**：`Tell分类学研究过程文档/399-v0-2026-08-18-POC-2.6-续传机制验证-completion_tokens限制应对方案.md`
**数据资产目录**：`Tell分类学研究过程文档/poc_assets/poc_2.6/`
**续传脚本**：`poc_assets/poc_2.6/continue_solver.py`
**交接文档标准**：`续传规范文档.md`（项目根目录）
**数据库**：devin cli sessions.db（`~/.local/share/devin/cli/sessions.db`），每个run的session可通过cwd关联

### 续传方案演进

| 版本 | 方案 | 验证结果 | 问题 |
|---|---|---|---|
| v1 | 机械拼接reasoning_content | CC-101_bare/vein/hint成功，CC-103_vein_hint成功 | CC-103_bare失败——6个agent step只传了最后一个的reasoning(30%)，丢失了web search结果和前5步thinking。CC-103_vein更严重——5轮全部失败 |
| v2 | 交接文档(HANDOFF.md) | CC-103_bare成功——AI 2分钟写出z3验证脚本，7分钟跑出关键结果，32分钟完成证明 | 交接文档整理目前手动做，后续可自动化 |

### 成功运行记录

| Run | 条件 | 答案 | 耗时 | 续传方案 | Round详情 | 证据文档 |
|---|---|---|---|---|---|---|
| CC-101_bare | bare | $\boxed{4}$ ✅ | ~13min | v1 | R1截断→R2完成(19步) | `EVIDENCE-CC-101_bare-续传机制验证.md` |
| CC-101_vein | vein | $\boxed{4}$ ✅ | ~45min | v1 | R1截断→R2完成(30步) | `EVIDENCE-CC-101_vein-vein策略验证.md` |
| CC-101_hint | hint | $\boxed{4}$ ✅ | ~9min | v1 | R1截断→R2完成 | — |
| CC-103_bare | bare | $\boxed{3}$ ✅ | ~32min | v2交接文档 | R1截断(6步)+R2截断→R3交接文档续传完成(10个脚本) | — |
| CC-103_vein_hint | vein_hint | $\boxed{3}$ ✅ | ~18min | v1 | R1-3截断→R4完成 | — |

### v1方案失败的run（需v2交接文档续传）

| Run | 条件 | v1轮次 | 失败原因 | v2续传状态 |
|---|---|---|---|---|
| CC-101_vein_hint | vein_hint | 2轮 | R2最后一步截断(54K thinking)，丢失了前11步的tool calls和SAT solver结果 | v2续传中 |
| CC-103_vein | vein | 5轮 | 5轮全部纯thinking spin，v1只传最后一个step的reasoning(30%)，丢失了R2的18步web search结果 | v2续传中 |

### 资产清单（每个run）

**CC-101_bare**：
- Round 1 export: `trajectories/p26-CC-101_bare/round1/exports/conversation.json`（154KB）
- Round 2 export: `trajectories/p26-CC-101_bare/round2/exports/conversation.json`（286KB）
- 续传prompt: `workdirs/p26-CC-101_bare/round2_prompt.txt`（55KB）
- 最终证明: `workdirs/p26-CC-101_bare/proof.md`（10KB）
- AI写的脚本: `workdirs/p26-CC-101_bare/`下7个Python脚本

**CC-101_vein**：
- Round 1 export: `trajectories/p26-CC-101_vein/round1/exports/conversation.json`（148KB）
- Round 2 export: `trajectories/p26-CC-101_vein/round2/exports/conversation.json`（344KB）
- 续传prompt: `workdirs/p26-CC-101_vein/round2_prompt.txt`（49KB）
- 最终证明: `workdirs/p26-CC-101_vein/proof.md`（7KB）
- AI写的脚本: `workdirs/p26-CC-101_vein/`下7个Python脚本

**CC-103_bare**（v2交接文档续传）：
- Round 1 export: `trajectories/p26-CC-103_bare/round1/exports/conversation.json`（353KB，6个agent step含web search）
- Round 2 export: `trajectories/p26-CC-103_bare/round2/exports/conversation.json`（260KB，纯thinking spin被截断）
- 交接文档: `workdirs/p26-CC-103_bare/HANDOFF.md`（7.5KB，整理Round 1-2的完整探索历程）
- Round 3 export: `trajectories/p26-CC-103_bare/round3_handoff/exports/conversation.json`
- 最终证明: `workdirs/p26-CC-103_bare/proof.md`（9KB）
- AI写的脚本: `workdirs/p26-CC-103_bare/`下10个Python脚本（verify_area3.py, find_minimal.py, cross_verify.py, debug_verify.py, backtrack_fixed.py, find_small_config.py, proof_helpers.py, analyze_27.py等）

### 关键发现

1. **续传机制成功**：裸AI模型在completion_tokens限制下无法单轮完成的竞赛数学推理，通过续传机制完成了
2. **v1方案在简单情况下够用**：CC-101的bare/vein/hint条件Round 1只有1个agent step（纯thinking），v1只传reasoning_content刚好够用
3. **v1方案在复杂情况下失败**：CC-103_bare Round 1有6个agent step（web search+多轮thinking），v1只传了最后一个step的reasoning(30%)，丢失了web search结果和前5步thinking。CC-103_vein更严重——5轮全部失败
4. **v2交接文档方案显著优于v1**：CC-103_bare用v2交接文档续传，AI 2分钟内写出z3验证脚本，7分钟跑出关键结果(7×5网格UNSAT)，32分钟完成证明。对比v1方案CC-103_vein 5轮全部在thinking中打转，0个脚本
5. **vein可能增加成本**：CC-101_vein比CC-101_bare多11步、多32分钟，vein注入的p-adic方向不是最优路径（bare走Rado定理更简洁）
6. **vein与hint是同一策略的不同Level表述**：vein是展开版（四步+具体方法示范），hint是压缩版（一句话），但vein混入了特化方法引导的混淆变量（见398号§2.5）

---

## POC-2.7 截断vs思维错误（⚠️执行中）

**方案文档**：`Tell分类学研究过程文档/415-v0-2026-08-18-POC-2.7-截断vs思维错误.md`
**数据资产目录**：`Tell分类学研究过程文档/poc_assets/poc_2.7/`
**批量续传脚本**：`poc_assets/poc_2.7/batch_continue_948.py`
**数据库**：ArangoDB（`analysis_results` + `devin_problem_runs`）

### 核心发现

POC-2.5的16个原始run中13个有export的**全部被截断**（comp=25000, msg=0, tc=0）。Pipe 1判定948道题为DIRECTION_ERROR，但96%实际上是failed_token_limit——thinking被截断，AI从未进入working阶段。

### 阶段1验证结果（✅完成）

| 题目 | 答案 | 轮次 | 说明 |
|---|---|---|---|
| CC-101_bare | boxed{4} | 2轮 | R1截断→R2完成 |
| CC-103_bare | boxed{3} | 3轮 | v2交接文档 |
| CC-104_bare | boxed{200} | 2轮 | R1截断→R2完成 |
| CC-105_bare | boxed{793} | 2轮 | R1截断→R2完成 |
| mathnet_001631 | boxed{k=2} | 3轮 | R1截断→R2截断→R3完成 |

**5/5成功，0/5是真正的思维错误。**

### 阶段2：948道DIRECTION_ERROR题全量续传（⚠️v1小批量完成，v2集成完成，全量待启动）

- 919道有export的题已从ArangoDB导出
- 前缀分布：deepmath(382) + oda(304) + polymath(207) + omni(23) + amo(2) + mathnet(1)

**v1方案小批量测试结果（10题/并发5，已完成）**：

| 状态 | 题数 | 占比 |
|---|---|---|
| COMPLETED | 9 | 90% |
| TRUNCATED_AT_MAX | 1 | 10% |
| ERROR | 0 | 0% |

- 9/10题通过续传完成，证明绝大多数DIRECTION_ERROR是截断错误而非思维错误
- omni_math_004104是v1方案中唯一5轮全截断的题（真思维错误候选）
- v1方案缺陷：只提取reasoning_content拼接，丢失tool_calls和observation

**v2方案集成完成（面包屑地图+HANDOVER.md）**：

- `batch_continue_948.py`已支持`--method v1|v2`参数切换
- v2流程：每轮续传先Pipe A（生成地图+编写HANDOVER.md），再Pipe B（用HANDOVER.md作为续传prompt）
- v2单题测试（omni_math_004104）：round2也截断（comp=25000），该题很可能是真正的思维错误
- v2方案优势：HANDOVER.md包含v1丢失的observation/proof.md内容，prompt从128KB原始thinking缩减到12KB结构化文档

### 执行路径

1. **阶段1** ✅已完成——4道bare题+1道DIRECTION_ERROR题全部成功
2. **阶段2** ⚠️执行中——v1小批量完成(9/10)，v2集成完成，全量续传待启动
3. **阶段3** 待定——6400道failed_token_limit全量续传（948道之外的5452道）
4. **阶段4** POC-2.5b——续传后仍然失败的题上测试Hint因果效应

---

## POC-2.7.6 面包屑地图方案验证（✅全部通过）

**方案文档**：`conversation-map.md`（项目根目录）
**遍历程序**：`scripts/conversation_mapper.py`（已实现）
**普查程序**：`scripts/conversation_field_census.py`（已实现）

### 核心问题

基于先验schema的conversation.json提取方式有根本缺陷——919道DIRECTION_ERROR题的原始prompt禁止工具调用，导致conversation.json结构单一，基于此建立的schema不能代表AI正常使用工具时的真实结构。续传后AI正常调工具，conversation.json中出现大量tool_calls/observation和多轮thinking spin。

需要一个不假设schema的遍历方案：递归遍历conversation.json生成面包屑地图（带JSON path的导航索引），交给编写HANDOVER.md的AI按地图逐条遍历，不依赖先验schema。

### 验证结果

**1. 遍历完备性 ✅通过**

三个测试样本，所有叶子节点都在地图中，0遗漏：

| 测试样本 | 特征 | steps叶子节点数 | 地图包含 | 遗漏 |
|---|---|---|---|---|
| omni_math_004100 round1 | 原始做题，受限prompt，单step纯thinking spin | 54 | 54 | 0 |
| omni_math_004133 round2 | 续传后，不受限prompt，7个agent step，6个有工具调用 | 175 | 175 | 0 |
| omni_math_000120 | 有中间截断，7个agent step，step0和step6都截断 | — | — | 0 |

**2. 结构适应性 ✅通过**

地图正确处理了三种不同结构的conversation.json：
- 受限prompt（无工具调用，纯thinking spin）
- 不受限prompt（多轮thinking spin + 工具调用 + observation）
- 中间截断（step0截断后devin cli内部续传，step1-5正常工具调用，step6再截断）

**3. 截断检测 ✅通过**

统计摘要正确识别了中间截断（agent step 0）和最后截断（agent step 6）。

### 待验证

- ~~**地图可用性**：编写HANDOVER.md的AI能根据地图正确定位和读取所有需要的内容~~ ✅已通过（见下）
- ~~**HANDOVER.md质量**：对比v1方案（机械拼接reasoning_content）和v2方案（面包屑地图+HANDOVER.md）的续传效果~~ ✅已通过（见下）

### 地图可用性验证结果（✅通过）

**Pipe 1**：用`conversation_mapper.py`生成omni_math_004133 round2的面包屑地图（388行）
**Pipe 2**：用`devin -p --permission-mode dangerous`无头模式启动AI，给它地图+conversation.json路径，让它编写HANDOVER.md

AI的工作流程（从conversation.json的agent steps确认）：
1. read地图（conversation_map.md）——了解conversation.json结构
2. read续传规范文档——了解HANDOVER.md的8个章节要求
3. exec python脚本（`scripts/extract_conversation_fields.py`）——从conversation.json提取大字段
4. write HANDOVER.md——按8个章节整理

**产出文件**：
- `trajectories/p27-omni_math_004133/round2/HANDOVER.md`（253行）
- `scripts/extract_conversation_fields.py`（可复用的conversation.json字段提取脚本）

### HANDOVER.md质量验证结果（✅通过）

**审查方法**：亲自对照conversation.json原文验证HANDOVER.md中5个关键数据点的准确性

| 验证项 | HANDOVER.md内容 | conversation.json原文 | 一致 |
|---|---|---|---|
| §1 题目文本 | "For a positive integer $n$..." | steps[8].message开头完全一致 | ✅ |
| §3.3 素数列表 | 7, 13, 97, 193, 769, 12289...11个 | step10 observation包含完全相同的素数 | ✅ |
| §6.1 proof.md | boxed{No}, 4284c | step14 write arguments.content完全一致 | ✅ |
| §3.4 Match: True | sympy精确验证 | step15 observation包含"Match: True" | ✅ |
| §2 最终答案 | No | step16 message包含"No"和"否" | ✅ |

**v1 vs v2对比**：

| 维度 | v1方案（机械拼接reasoning_content） | v2方案（面包屑地图+HANDOVER.md） |
|---|---|---|
| 提取内容 | 只有thinking（reasoning_content） | thinking + tool_calls + observation + proof.md内容 |
| observation | ❌ 丢失 | ✅ 包含（6个exec的observation全部提取） |
| proof.md内容 | ❌ 丢失 | ✅ 包含（4284c完整证明） |
| 续传prompt大小 | 拼接7个reasoning_content ≈ 128KB | HANDOVER.md = 253行（约12KB），提炼后 |
| AI可理解性 | 128KB原始thinking，难定位关键信息 | 8章节结构化文档，直接可用 |

**结论**：v2方案在observation保留、proof.md内容保留、prompt大小、可理解性四个维度全面优于v1方案。

---

## POC-2.7.5 续传发现对前置POC的影响评估（✅完成——1962终版判定：截断可救，POC-1重审触发）

**方案文档**：`Tell分类学研究过程文档/416-v0-2026-08-18-POC-2.7.5-续传发现对前置POC的影响评估.md`
**影响评估报告**：`Tell分类学研究过程文档/poc_assets/poc_2.7.5/impact_assessment_report.md`（2026-08-21产出）
**1962补验证**：tmux `poc275-1962`运行中，脚本`poc_assets/poc_2.7.5/run_1962_revalidation.py`，结果落`poc_assets/poc_2.7.5/results_1962.json`

### 核心问题

续传能让裸模型解决原本被判定为"思维错误"的题。这个发现对POC-0/0.5/1/2的验证意义有什么影响？

### 影响评估结论（2026-08-21正式版，含新增实况）

| POC | 影响程度 | 结论 |
|---|---|---|
| POC-0 | 部分受影响 | 题包冻结有效，但"bare可失败"否决项需修正为"bare+续传可失败"；CC-101~106正迁移题资格需按新标准复核 |
| POC-0.5 | 不受影响 | 变形关系是数学结构层面的验证，完全有效 |
| POC-1 | 需要关键确认 | 383号消融分析有效；401号提取完备性检查需补验证1962；**波及面**：§7.6.1思维F（case分裂）裁决的证据链同样依赖1962判据 |
| POC-2 | 入场券标准需修正 | selector验证有效，但"bare失败是入场券"正式修正为"bare+续传失败是入场券" |

### 新增实况（2026-08-21）

全量续传已由续传解题系统接管（10,072题入池，152 completed全部2轮解出，TRUNCATED_AT_MAX=0）；小批量90%+大规模完成率相互印证"DIRECTION_ERROR绝大部分是截断"。强入场券候选目前仅omni_math_004104一道。

### 1962补验证

对1962（VMS-8中唯一bare和tree都失败的题）启动bare+续传，确认其bare失败是截断还是真正的思维错误：
- 续传后成功 → 1962是截断错误 → POC-1因果取商结论需重新审视
- 续传后失败 → 1962是真正的思维错误 → POC-1结论仍然有效
- 反向证据：1962-tree也失败了（给了方向也失败），更像真正的思维错误

### 修正后的铁律

"bare+续传失败是入场券"——替代原始的"bare失败是入场券"（373号§3）

### TellCore因果贡献的测量基线修正

| 维度 | 之前的基线 | 续传后的基线 |
|---|---|---|
| bare失败的定义 | bare单轮失败 | bare+续传5轮失败 |
| TellCore的因果贡献 | 从失败到成功 | 从续传5轮失败到成功，或减少续传轮次/时间 |
| 正迁移题的筛选标准 | DIRECTION_ERROR | 续传后仍然失败 |

### 后续序列调整（2026-08-21晚·终版）

1962补验证完成：v2编排六轮接力产出完整proof.md（16解boxed，COMPLETED）。终版判定=**截断可救**（verdict_1962.md），覆盖第三类判定。POC-1重审触发（401号头部回执）；POC-2.5b选题前提细化（TRUNCATED_AT_MAX vs BUDGET_STARVED区分，见047号修正6）；POC-2.5c处理组资产待POC-1重审后定。

---

## POC-2.5 基础因果效应验证（⚠️执行中）

**方案文档**：`Tell分类学研究过程文档/398-v0-2026-08-17-POC-2.5-基础因果效应验证-自包含方案文档.md`
**第一轮原始数据**：`poc_assets/poc_2.5_round1/`（16个problem文件+13个export+3个多轮tool call的work_dir）
**续传数据**：`poc_assets/poc_2.6/`（续传运行的数据存在这里）
**数据库**：devin cli sessions.db

### 4条件对照矩阵

| 条件 | 给AI什么 | 策略表述Level | 是否混入特化方法 |
|---|---|---|---|
| bare | 只有题目 | 无策略 | — |
| vein | 题目+参考路径 | 展开（四步+示范） | 是 |
| vein_hint | 题目+参考路径+Hint | 展开+抽象 | 是 |
| hint | 题目+Hint | 抽象（一句话） | 否 |

### 运行状态（2026-08-18更新）

| 题目 | bare | vein | vein_hint | hint |
|---|---|---|---|---|
| CC-101 | ✅boxed{4} | ✅boxed{4} | ✅boxed{n=4} | ✅boxed{4} |
| CC-103 | ✅boxed{3} | v2续传中 | ✅boxed{3} | v1运行中 |
| CC-104 | ✅boxed{200} | ✅boxed{200} | ✅boxed{200} | v1运行中 |
| CC-105 | ✅boxed{793} | 待启动 | 待启动 | 待启动 |

**运行方式**：5并发，每个在独立tmux session中，不受对话窗口影响
**定位方法**：见AGENTS.md"POC-2.5批量续传实例"节

**POC-2.7发现**：4道bare题续传全部成功 → 这些题是截断错误不是思维错误 → POC-2.5的Hint因果实验需要重新选题（在续传后仍然失败的题上做）。详见415号POC-2.7方案。

### 判定逻辑（398号§5.3）

- 场景1：bare失败+vein_hint成功，但vein也成功 → vein够，Hint无因果作用
- 场景2：bare失败+vein失败+vein_hint成功 → Hint有因果作用（最理想）
- 场景3：全失败 → Hint无效
- 场景4：bare成功 → 题目不是真正的bare失败

---

## 数据库数据定位

| 数据库 | 位置 | 内容 | 查询方式 |
|---|---|---|---|
| devin cli sessions.db | `~/.local/share/devin/cli/sessions.db` | 所有devin cli session的trajectory | 按cwd关联到具体run |
| ArangoDB (xishujuzhen_math_glm52) | ArangoDB服务 | VMS历史实验数据、数学题库 | `echo $ARANGO_DB` 确认库名 |

---

## 方案文档索引

| 编号 | 路径 | POC |
|---|---|---|
| 396号 | `Tell分类学研究过程文档/396-v0-2026-08-17-非特化理论综合-*.md` | 理论背景 |
| 397号 | `Tell分类学研究过程文档/397-v0-2026-08-17-GPT373号POC套装的逐个审视-*.md` | POC系列审视 |
| 398号 | `Tell分类学研究过程文档/398-v0-2026-08-17-POC-2.5-基础因果效应验证-*.md` | POC-2.5 |
| 399号 | `Tell分类学研究过程文档/399-v0-2026-08-17-POC-0-CasePack冻结简化版-*.md` | POC-0 |
| 399号(2.6) | `Tell分类学研究过程文档/399-v0-2026-08-18-POC-2.6-续传机制验证-*.md` | POC-2.6 |
| 400号 | `Tell分类学研究过程文档/400-v0-2026-08-17-POC-0.5-变形关系声明-*.md` | POC-0.5 |
| 401号 | `Tell分类学研究过程文档/401-v0-2026-08-17-POC-1-因果取商增强版-*.md` | POC-1 |
| 402号 | `Tell分类学研究过程文档/402-v0-2026-08-17-POC-2-可选择-*.md` | POC-2 |
| 403号 | `Tell分类学研究过程文档/403-v0-2026-08-17-POC-3.5-Hint非特化程度验证-*.md` | POC-3.5 |
| 404号 | `Tell分类学研究过程文档/404-v0-2026-08-17-POC-3-可执行-*.md` | POC-3 |
| 405号 | `Tell分类学研究过程文档/405-v0-2026-08-17-POC-4-可终止-*.md` | POC-4 |
| 406号 | `Tell分类学研究过程文档/406-v0-2026-08-17-POC-6-可归责-*.md` | POC-6 |
| 407号 | `Tell分类学研究过程文档/407-v0-2026-08-17-POC-7-可持续学习简化版-*.md` | POC-7 |
| 408号 | `Tell分类学研究过程文档/408-v0-2026-08-17-POC-8-端到端闭环-*.md` | POC-8 |
| 409号 | `Tell分类学研究过程文档/409-v0-2026-08-17-POC-9-识别端验证-*.md` | POC-9 |
| 413号 | `Tell分类学研究过程文档/413-v0-2026-08-17-非特化研究执行编排-*.md` | 执行编排 |
| 415号 | `Tell分类学研究过程文档/415-v0-2026-08-18-POC-2.7-截断vs思维错误.md` | POC-2.7 |
| 416号 | `Tell分类学研究过程文档/416-v0-2026-08-18-POC-2.7.5-续传发现对前置POC的影响评估.md` | POC-2.7.5 |
| 417号 | `Tell分类学研究过程文档/417-v0-2026-08-21-非特化研究POC系列-完整演进脉络与交接文档.md` | 交接文档（完整演进脉络+接手指南） |
| 418号 | `Tell分类学研究过程文档/418-v0-2026-08-21-POC-2.5c-基础因果效应验证弱因果版-自包含方案文档.md` | POC-2.5c（骨架） |
| 续传规范文档 | `续传规范文档.md`（项目根目录） | 交接文档标准 |
| 面包屑地图方案 | `conversation-map.md`（项目根目录） | POC-2.7.6 |
| conversation.json Schema | `devin-cli-export-conversation.md`（项目根目录） | POC-2.7.6 |
| trajectory.jsonl Schema | `trajectory-schema.md`（项目根目录） | POC-2.7.6 |

## POC-1重审（✅完成·方案=419号·产出已采纳）

1962终版判定（截断可救）触发401号重审：7字段结构存活，因果充分性宣称悬置，Pareto证据降级。重构路径=以v2 R4/R6 thinking为素材双审查者独立提取，产出候选TellCore v0.2四条（弱因果框架）。**2026-08-22用户拍板采纳v0.2四候选**，取代旧候选A/B/C（归档+Evidence-downgraded）。首个下游应用：POC-2.5c候选Ⅰ单臂12题T/C试点（实验矩阵冻结于`poc_assets/poc_2.7.5/v2/poc25c_experiment_design.md`）。
