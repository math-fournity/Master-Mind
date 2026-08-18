# POC-2.7 截断vs思维错误 · 完整进度报告

> **文档编号**：POC-2.7-001
> **创建日期**：2026-08-18
> **方案文档**：`Tell分类学研究过程文档/415-v0-2026-08-18-POC-2.7-截断vs思维错误.md`
> **数据资产目录**：`Tell分类学研究过程文档/poc_assets/poc_2.7/`
> **批量续传脚本**：`Tell分类学研究过程文档/poc_assets/poc_2.7/batch_continue_948.py`
> **数据库**：ArangoDB（`analysis_results` + `devin_problem_runs`）

---

## §1 核心问题

Pipe 1（错题分析系统）判定948道题为DIRECTION_ERROR（方向错误）。但POC-2.5的16个原始run中13个有export的**全部被截断**（comp=25000, msg=0, tc=0）——AI的thinking spin撞上了completion_tokens上限，从未进入working阶段（没有message输出，没有tool_call）。

**核心问题**：这948道DIRECTION_ERROR题中，有多少是真正的思维错误（AI想错了方向），有多少只是截断错误（AI还没来得及输出就被截断了）？

**验证方法**：对每道题启动续传机制——把截断的thinking作为新prompt注入，让AI继续思考。如果续传后能完成（输出proof.md含boxed答案），说明是截断错误；如果续传5轮仍然截断，说明可能是真正的思维错误。

---

## §2 已完成内容总览

| 内容 | 状态 | 说明 |
|---|---|---|
| 阶段1：5道题手工验证 | ✅完成 | 5/5成功，0/5是真正的思维错误 |
| 阶段2数据准备：919题导出 | ✅完成 | 从ArangoDB导出919道有export的题 |
| 阶段2 v1方案小批量测试 | ✅完成 | 10题/并发5，9 COMPLETED / 1 TRUNCATED |
| POC-2.7.6：面包屑地图方案 | ✅完成 | 不假设schema的conversation.json遍历方案 |
| POC-2.7.6：conversation_mapper.py | ✅完成 | 遍历程序实现+5项验证全部通过 |
| POC-2.7.6：HANDOVER.md质量验证 | ✅完成 | 5个关键数据点与原文一致 |
| 阶段2 v2方案集成 | ✅完成 | batch_continue_948.py支持`--method v2` |
| 阶段2 v2单题测试 | ⚠️部分 | omni_math_004104 round2截断（真思维错误候选） |
| 阶段2 v2全量续传 | ⏳待启动 | 919题，等用户指示 |
| 阶段3 | 待定 | 6400道failed_token_limit全量续传 |
| 阶段4 | 待定 | POC-2.5b Hint因果效应 |

---

## §3 阶段1：5道题手工验证（✅完成）

### 3.1 验证结果

| 题目 | 答案 | 轮次 | 说明 |
|---|---|---|---|
| CC-101_bare | boxed{4} | 2轮 | R1截断→R2完成 |
| CC-103_bare | boxed{3} | 3轮 | v2交接文档 |
| CC-104_bare | boxed{200} | 2轮 | R1截断→R2完成 |
| CC-105_bare | boxed{793} | 2轮 | R1截断→R2完成 |
| mathnet_001631 | boxed{k=2} | 3轮 | R1截断→R2截断→R3完成 |

**结论：5/5成功，0/5是真正的思维错误。**

### 3.2 意义

这5道题原本被Pipe 1判定为DIRECTION_ERROR（方向错误），但通过续传机制全部完成。证明Pipe 1的DIRECTION_ERROR判定中存在大量假阳性——这些题不是AI想错了方向，而是AI的thinking spin被completion_tokens上限截断了。

---

## §4 阶段2数据准备：919题导出（✅完成）

### 4.1 数据来源

从ArangoDB的`analysis_results`表（d1=DIRECTION_ERROR的948题）和`devin_problem_runs`表（原始做题的export路径）导出。

### 4.2 数据分布

- **919道有export的题**（29道无export，无法续传）
- 前缀分布：

| 前缀 | 题数 | 说明 |
|---|---|---|
| deepmath | 382 | DeepMath数据集 |
| oda | 304 | ODA数据集 |
| polymath | 207 | PolyMath数据集 |
| omni | 23 | OmniMath数据集 |
| amo | 2 | AMO数据集 |
| mathnet | 1 | MathNet数据集 |

### 4.3 原始prompt限制

918/919题的原始prompt是"直接在TUI中输出证明，不要写任何文件"——**强制AI不调工具**。这导致原始conversation.json里几乎没有tool_calls/observation，AI只做纯thinking spin。

续传prompt改为"把证明写到proof.md文件中"（不禁止工具调用），续传后的AI正常使用工具。

---

## §5 阶段2 v1方案小批量测试（✅完成）

### 5.1 v1方案说明

**v1方案（机械拼接）**：
1. `extract_reasoning(export)` → 提取所有agent step的reasoning_content拼接
2. `build_continue_prompt(题目, reasoning)` → 用拼接的reasoning作为续传prompt
3. `devin -p --prompt-file prompt.txt` → 启动AI继续解题

**v1方案缺陷**：只提取reasoning_content（thinking），丢失tool_calls和observation。对915道纯thinking spin的题够用，但对4道有工具调用的题丢失了observation。

### 5.2 测试结果

10题/并发5，v1方案：

| 状态 | 题数 | 占比 |
|---|---|---|
| COMPLETED | 9 | 90% |
| TRUNCATED_AT_MAX | 1 | 10% |
| ERROR | 0 | 0% |

### 5.3 9道完成题详情

| 题目 | 轮次 | proof.md大小 | boxed答案 |
|---|---|---|---|
| omni_math_004100 | 2轮 | 4675c | f(n) = c·v_p(n) |
| omni_math_004123 | 2轮 | 15862c | ⌈n/2⌉ |
| omni_math_004127 | 2轮 | 6009c | n²−n−1 |
| omni_math_004105 | 2轮 | 6095c | k+4 |
| omni_math_004116 | 3轮 | 7525c | P(x) = c(qx−p)^d |
| omni_math_004128 | 3轮 | 8030c | a_n = cn+d |
| omni_math_004133 | 2轮 | 4284c | No |
| omni_math_004146 | 4轮 | 10320c | m ≡ 3 (mod 4) |
| mathnet_001631 | 5轮 | 3650c | k=2 |

### 5.4 1道截断题详情

**omni_math_004104**：5轮全部纯thinking spin截断（comp=25000, msg=0, tc=0）。

| 轮次 | reasoning大小 | comp | 状态 |
|---|---|---|---|
| Round 1 | 57487c | 25000 | 截断 |
| Round 2 | 56740c | 25000 | 截断 |
| Round 3 | 65886c | 25000 | 截断 |
| Round 4 | 57639c | 25000 | 截断 |
| Round 5 | 52401c | 25000 | 截断 |

这道题是IMO 2010第5题（6盒子硬币问题），AI在5轮中都停留在thinking spin阶段，反复探索不变量和策略但未能突破。**很可能是真正的思维错误**。

### 5.5 关键结论

**90%的DIRECTION_ERROR是截断错误**，续传后可完成。只有10%（1/10）可能是真正的思维错误。

---

## §6 POC-2.7.6：面包屑地图方案（✅全部通过）

### 6.1 方案背景

v1方案基于先验schema的conversation.json提取方式有根本缺陷——919道题的原始prompt禁止工具调用，导致conversation.json结构单一，基于此建立的schema不能代表AI正常使用工具时的真实结构。

需要一个**不假设schema的遍历方案**：递归遍历conversation.json生成面包屑地图（带JSON path的导航索引），交给编写HANDOVER.md的AI按地图逐条遍历，不依赖先验schema。

### 6.2 方案文档和程序

| 文件 | 位置 | 用途 |
|---|---|---|
| `conversation-map.md` | 项目根目录 | 方案文档（7节） |
| `scripts/conversation_mapper.py` | scripts/ | 遍历程序（生成面包屑地图） |
| `scripts/conversation_field_census.py` | scripts/ | 字段普查程序（验证schema完备性） |
| `scripts/extract_conversation_fields.py` | scripts/ | conversation.json字段提取脚本 |

### 6.3 验证结果（5项全部通过）

| 验证项 | 结果 | 证据 |
|---|---|---|
| 遍历完备性 | ✅ | 3个测试样本，所有叶子节点都在地图中，0遗漏 |
| 结构适应性 | ✅ | 受限prompt/不受限prompt/中间截断三种结构都正确处理 |
| 截断检测 | ✅ | 中间截断和最后截断都正确识别 |
| 地图可用性 | ✅ | AI根据地图成功编写253行HANDOVER.md，8章节完整 |
| HANDOVER.md质量 | ✅ | 5个关键数据点与conversation.json原文全部一致 |

### 6.4 v1 vs v2对比

| 维度 | v1（机械拼接） | v2（面包屑地图+HANDOVER.md） |
|---|---|---|
| observation | ❌ 丢失 | ✅ 6个exec的observation全部提取 |
| proof.md内容 | ❌ 丢失 | ✅ 4284c完整证明 |
| 续传prompt大小 | 128KB原始thinking | 12KB结构化HANDOVER.md |
| AI可理解性 | 难定位关键信息 | 8章节直接可用 |

**结论**：v2方案在observation保留、proof.md内容保留、prompt大小、可理解性四个维度全面优于v1方案。

### 6.5 POC验证流程（无头模式执行，亲自审查所有输入输出）

| Pipe | 执行方式 | 审查 |
|---|---|---|
| Pipe 1：生成地图 | `conversation_mapper.py`生成388行面包屑地图 | 亲自读取地图全文，确认包含所有节点 |
| Pipe 2：编写HANDOVER.md | `devin -p --permission-mode dangerous`无头模式 | 亲自构造prompt，审查AI的conversation.json确认工作流程 |
| 输出审查 | — | 亲自对照conversation.json原文验证5个关键数据点 |

---

## §7 阶段2 v2方案集成（✅完成）

### 7.1 v2方案流程

```
每轮续传:
  1. conversation_mapper.py export → 生成面包屑地图（Pipe A Step 1）
  2. devin -p "读地图+conversation.json，写HANDOVER.md" → Pipe A Step 2（编写交接文档）
  3. devin -p --prompt-file HANDOVER.md → Pipe B（基于交接文档继续解题）
```

### 7.2 集成实现

`batch_continue_948.py`已支持`--method v1|v2`参数切换（默认v2）：

- 新增`generate_handover()`函数——Pipe A（生成地图+编写HANDOVER.md）
- 新增`build_v2_continue_prompt()`函数——用HANDOVER.md构造续传prompt
- 修改`solve_single()`支持method参数
- v2失败时自动回退到v1

### 7.3 v2单题测试（omni_math_004104）

| 轮次 | reasoning大小 | comp | 状态 | HANDOVER.md | 地图 |
|---|---|---|---|---|---|
| Round 1 | 57487c | 25000 | 截断 | 12101c ✅ | 8383c ✅ |
| Round 2 | 53414c | 25000 | 截断 | ✅ | ✅ |

**观察**：v2方案对这道题也截断。但v2的HANDOVER.md质量极高——184行，8个章节完整，包含：
- §3.1-3.8：8个已确认的数学结论（不变量S、Type 2公式、模分析、简单策略最大值114688、循环策略失效等）
- §4：6个已尝试方向的表格
- §7：截断位置精确到thinking最后一行
- §8：4个具体的下一步建议

这道题（IMO 2010第5题）在v1和v2方案中都截断，**很可能是真正的思维错误**。

---

## §8 待完成内容

### 8.1 阶段2 v2全量续传（⏳待启动）

- 919题，使用`--method v2`全量续传
- v2方案每轮需要2个pipe（Pipe A编写HANDOVER.md + Pipe B解题），比v1慢约2倍
- 估算：919题×3轮×2 pipe×10分钟/5并发 ≈ 8天

**启动前必须确认（415号§5.5步骤0-2）**：
1. ArangoDB运行状态：`docker ps | grep arangodb || docker start arangodb`
2. D盘挂载状态：`ls /data/math-agent-glm5.2-tmux-agents-trajectory/ | head -3`
3. devin cli可用：`which devin`
4. 断点续传状态：`batch_continue_948.py status`确认9道已完成题不重复运行
5. **必须在tmux中启动**（禁止nohup——全局AGENTS.md§12 tmux优先铁律）：
   ```bash
   tmux new-session -d -s poc27-batch "cd ~/master-mind-glm5.2-worktree && .venv/bin/python3 'Tell分类学研究过程文档/poc_assets/poc_2.7/batch_continue_948.py' batch --concurrency 5 --max-rounds 5 --method v2 2>&1 | tee 'Tell分类学研究过程文档/poc_assets/poc_2.7/poc_2.7/batch_full.log'"
   ```

**运行中纪律（415号§9.6/§9.7）**：
- **不终止已启动的run**（§9.6）——如果需要调整方案，让已启动的run自然完成
- **脚本是检查者不是旁观者**（§9.7）——定期检查：tmux session是否正常、results.json是否在增长、proof.md是否在生成、log中有没有异常

### 8.2 阶段3（待定）

6400道failed_token_limit全量续传（948道之外的5452道）。

### 8.3 阶段4（待定）——POC-2.5b

POC-2.5b——续传后仍然失败的题上测试Hint因果效应。

**修正后的选题流程**（415号§10.7）：
```
原始做题 → 启动续传 → 续传后仍然失败的题 → Pipe 1重新分析（在完整thinking上）→ Pipe 3选题 → POC-2.5b
```

**关键改变**：Pipe 1的分析在续传后的完整thinking上做，不是在截断的thinking上做。原始选题流程中Pipe 1在截断thinking上判定DIRECTION_ERROR，判定基础本身有问题（本POC已验证）。

---

## §9 关键发现汇总

1. **90%的DIRECTION_ERROR是截断错误**——v1小批量测试9/10题通过续传完成
2. **omni_math_004104是真思维错误候选**——v1和v2方案中都5轮/2轮截断，IMO 2010第5题
3. **原始prompt限制导致schema有偏**——918/919题禁止工具调用，基于此的schema不能代表真实场景
4. **v2方案全面优于v1**——observation保留、proof.md内容保留、prompt从128KB→12KB、结构化可理解
5. **面包屑地图方案不假设schema**——递归遍历任意JSON结构，适应未来schema变化

### 9.1 对照§7.1通过标准的判定（415号§7.1）

415号§7.1定义的通过标准（针对919题全量）：
- COMPLETED≥80% → 大部分是截断错误 → POC-2.5需要重新选题，Pipe 1判定基础有严重问题
- 50%≤COMPLETED<80% → 部分截断错误，部分思维错误 → 失败的题进入POC-2.5b
- COMPLETED<50% → 大部分是真正的思维错误 → POC-2.5候选题基础基本成立

**当前判定**：
- **10题样本**：COMPLETED=90% → 落在"≥80%"区间 → **初步倾向"大部分是截断错误"**
- **但10题样本不足以做正式判定**——10题中9道是omni_math前缀（23道omni题中的9道），前缀分布严重偏斜，不能代表919题全量（deepmath 382/oda 304/polymath 207/omni 23/amo 2/mathnet 1）
- **正式判定需要919题全量结果**——特别是deepmath（382题）和oda（304题）的续传成功率，这两个前缀占919题的74%，但小批量测试中0覆盖

**结论**：10题样本的90%成功率是积极信号，但POC-2.7的正式通过/不通过判定必须等919题全量续传完成。

---

## §10 资产清单

### 10.1 代码资产

| 文件 | 位置 | 用途 |
|---|---|---|
| `batch_continue_948.py` | `poc_assets/poc_2.7/` | 批量续传脚本（支持v1/v2） |
| `conversation_mapper.py` | `scripts/` | 面包屑地图生成器 |
| `conversation_field_census.py` | `scripts/` | JSON字段普查程序 |
| `extract_conversation_fields.py` | `scripts/` | conversation.json字段提取脚本 |

### 10.2 数据资产

| 文件 | 位置 | 内容 |
|---|---|---|
| `problem_list.json` | `poc_assets/poc_2.7/poc_2.7/` | 919道题的列表 |
| `results.json` | `poc_assets/poc_2.7/poc_2.7/` | 9道完成题的结果 |
| `trajectories/` | `poc_assets/poc_2.7/poc_2.7/` | 每道题的round1-5 export |
| `workdirs/` | `poc_assets/poc_2.7/poc_2.7/` | 每道题的工作目录（含proof.md） |

### 10.3 文档资产

| 文件 | 位置 | 内容 |
|---|---|---|
| `415-v0-2026-08-18-POC-2.7-截断vs思维错误.md` | `Tell分类学研究过程文档/` | POC-2.7方案文档 |
| `conversation-map.md` | 项目根目录 | 面包屑地图方案文档 |
| `续传规范文档.md` | 项目根目录 | HANDOVER.md标准结构 |
| `devin-cli-export-conversation.md` | 项目根目录 | conversation.json Schema |
| `trajectory-schema.md` | 项目根目录 | trajectory.jsonl Schema |
| `POC-2.7/POC-2.7-001-完整进度报告.md` | `POC-2.7/` | 本文件 |

---

## §11 执行约束遵守记录（415号§9执行约束）

> **本节为事后补充记录**——小批量测试执行时未系统记录这些约束的遵守情况，本节根据git log和现有产物回溯整理。全量续传启动前应建立实时记录机制。

### 11.1 环境检查（415号§9.1/§9.2/§9.3）

| 检查项 | 要求 | 回溯记录 |
|---|---|---|
| ArangoDB运行 | `docker ps \| grep arangodb` | 阶段2数据导出（919题）成功 → ArangoDB当时在运行（commit b75b5c2） |
| D盘挂载 | `ls /data/math-agent-glm5.2-tmux-agents-trajectory/ \| head -3` | 919题export路径验证通过 → D盘当时已挂载（commit b75b5c2） |
| devin cli可用 | `which devin` | 10题续传run成功启动 → devin cli当时可用 |

**不足**：没有在文档中记录检查的具体时间和输出。全量续传启动前必须实时记录环境检查结果。

### 11.2 监控纪律（415号§9.7）

415号§9.7要求："脚本运行时，你不是旁观者——你在检查脚本的健康状态：1.检查tmux session是否正常 2.检查results.json是否在增长 3.检查proof.md是否在生成 4.检查log中有没有异常信息"

**小批量测试期间的监控记录**：未系统记录。从结果反推：
- 10题/并发5的run全部正常完成（9 COMPLETED + 1 TRUNCATED_AT_MAX）→ 没有异常退出的tmux session
- results.json保存了9道完成题 → results.json正常增长
- 9道完成题都有proof.md → proof.md正常生成
- 0道ERROR → 无脚本异常

**不足**：没有记录运行过程中是否做过中途检查、检查频率、是否发现过stall。全量续传期间必须建立定期监控记录（建议每30分钟检查一次）。

### 11.3 Git commit记录（415号§9.5）

415号§9.5："续传结果提交到git，415号文档和POC.md随进展更新"

**POC-2.7相关commit历史**（从git log回溯）：

| commit | 内容 | 涉及文件 |
|---|---|---|
| d014ffc | POC-2.7方案初版 | 415号文档 |
| 9e74635 | 方案扩展：6400道截断题视角 | 415号文档 |
| be71220 | 调查结果修正：948题具体数据 | 415号文档 |
| b75b5c2 | 批量续传基础设施 | batch_continue_948.py + problem_list.json + mathnet_001631数据 |
| 88833a8 | 阶段1完成+阶段2执行中 | 415号文档 |
| dfea8a5 | POC.md更新 | POC.md |
| 50f9515 | 方案文档重构为自包含格式 | 415号文档 |
| 195f6f4 | 398号+399号文档更新 | 398号/399号文档 |
| 84dfaa3 | trajectory Schema文档 | devin-cli-export-conversation.md + trajectory-schema.md |
| c764d01 | POC-2.7.5影响评估 | 416号文档 + POC.md |
| 99560b7 | 面包屑地图方案 | conversation-map.md + conversation_field_census.py |
| 7b7bd0f | POC.md新增POC-2.7.6 | POC.md |
| 80428de | conversation_mapper.py实现 | scripts/conversation_mapper.py |
| 2a5da23 | POC-2.7.6遍历完备性验证 | POC.md |
| 77d3f85 | POC-2.7.6全部通过 | POC.md + HANDOVER.md + conversation_map.md + extract_conversation_fields.py |
| 422bb37 | batch_continue_948.py v2集成 | batch_continue_948.py + POC.md |
| 9fe19ff | 方案文档更新：小批量测试结果 | 415号文档 |
| 4bd88da | POC-2.7-001完整进度报告 | 本文件 |

**不足**：commit历史完整，但小批量测试的续传结果数据（results.json + trajectories + workdirs）是否已commit需要确认。从commit b75b5c2的stat看，只commit了mathnet_001631的数据，其余9道题的续传结果可能未commit。

### 11.4 "不终止已启动的run"纪律（415号§9.6）

415号§9.6："已启动的续传run不应该终止。如果需要调整方案，让已启动的run自然完成。"

**小批量测试期间**：10题/并发5的run全部自然完成，没有中途终止任何run。符合§9.6纪律。

**全量续传期间**：必须严格遵守——如果发现方案问题需要调整，不能终止已启动的run，只能让它们自然完成，调整后的方案只应用于未启动的题。

### 11.5 全量续传启动前的检查清单

- [ ] ArangoDB运行状态确认（`docker ps | grep arangodb`）
- [ ] D盘挂载状态确认（`ls /data/math-agent-glm5.2-tmux-agents-trajectory/ | head -3`）
- [ ] devin cli可用确认（`which devin`）
- [ ] 断点续传状态确认（`batch_continue_948.py status`显示9道已完成题）
- [ ] 用tmux启动（不用nohup）
- [ ] 建立定期监控记录机制（每30分钟检查一次）
- [ ] 确认"不终止已启动的run"纪律在工作记忆中
