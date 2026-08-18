# POC.md · 非特化研究 POC 测试总索引

> **所有 POC 测试的统一索引**——方案文档、数据资产、数据库数据、运行状态。
> **项目 rule 要求**：凡有新的测试出现，必须更新本文件（见 `.devin/rules/poc-registry-update.md`）。

---

## 总览

| POC | 名称 | 状态 | 方案文档 | 数据资产 | 数据库 | 证据文档 |
|---|---|---|---|---|---|---|
| POC-0 | CasePack冻结 | ✅完成 | 399号 | `poc_assets/poc_0/` | — | — |
| POC-0.5 | 变形关系声明 | ✅完成 | 400号 | `poc_assets/poc_0.5/` | — | — |
| POC-1 | 因果取商增强版 | ✅完成(有条件) | 401号 | `poc_assets/poc_1/` | — | — |
| POC-2 | 可选择 | 待执行 | 402号 | `poc_assets/poc_2/` | — | — |
| POC-2.5 | 基础因果效应验证 | ⚠️执行中 | 398号 | `poc_assets/poc_2.5_round1/` + `poc_2.6/` | sessions.db | 2份(见下) |
| POC-2.6 | 续传机制验证 | ✅完成 | 399号(2.6) | `poc_assets/poc_2.6/` | sessions.db | 2份(见下) |
| POC-2.7 | 截断vs思维错误 | ⚠️执行中 | 415号 | `poc_assets/poc_2.6/` | sessions.db | — |
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

### 运行状态（2026-08-18）

| 题目 | bare | vein | vein_hint | hint |
|---|---|---|---|---|
| CC-101 | ✅完成(boxed{4}) | ✅完成(boxed{4}) | v2续传中 | ✅完成(boxed{4}) |
| CC-103 | ✅完成(boxed{3}) | v2续传中 | ✅完成(boxed{3}) | v1运行中 |
| CC-104 | v1运行中 | 待启动 | 待启动 | 待启动 |
| CC-105 | 待启动 | 待启动 | 待启动 | 待启动 |

**运行方式**：5并发，每个在独立tmux session中，不受对话窗口影响
**定位方法**：见AGENTS.md"POC-2.5批量续传实例"节

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
| 续传规范文档 | `续传规范文档.md`（项目根目录） | 交接文档标准 |
