# Pipe3SelectionSOP.md — Pipe 3扩展运行SOP

> **来源**：从 AGENTS.md 第550-633行外移（2026-08-19瘦身工程三期，392号方案）。
> **定位**：Pipe 3扩展后的永久性运行SOP。5题分组+检查标准的规模化选题操作流程。
> **加载时机**：当你要运行Pipe 3规模化选题（5题分组/5并发/检查6字段填写率/渐进放量）时，必须用read工具全文加载本文件。不涉及Pipe 3运行时不需要读。
> **AGENTS.md索引**：AGENTS.md "外部文档索引"节有指向本文件的索引行。

---

### Pipe 3扩展运行SOP（5题分组+检查标准·2026-08-17建立）

> 本小节是Pipe 3扩展后的**永久性运行SOP**。任何Session的AI运行Pipe 3规模化选题时，必须按本SOP执行。

#### 运行思想

**不直接全量并发，而是5题一组、5并发处理、每组完成后检查。** 原因：

1. **早发现质量问题**——如果6个新字段的填写率或值分布有系统性问题（如全部填unclear、全部填hard），5题就能发现，不需要跑完726题再发现
2. **早发现rate limit问题**——5并发是小规模验证，确认rate limit安全后再继续
3. **渐进式放量**——前几组用5并发验证稳定性，后续可以根据rate limit情况调整并发数

#### 操作步骤

```
# 1. collect 5题
python3 analysis-devin-failure-system/run_selection_pipeline.py \
  --batch-id selection-batchN --source-batch-id audit-full1 \
  --step collect --limit 5

# 2. launch 5题（5并发）
python3 analysis-devin-failure-system/run_selection_pipeline.py \
  --batch-id selection-batchN --step launch --concurrency 5

# 3. collect-results
python3 analysis-devin-failure-system/run_selection_pipeline.py \
  --batch-id selection-batchN --step collect-results

# 4. 检查（AI执行，见下方检查标准）
```

#### 检查标准（每组完成后AI必须执行）

**A. 基础完整性检查**

| 检查项 | 标准 | 不通过时的处理 |
|---|---|---|
| 完成率 | 5/5完成，0失败 | 失败题重跑（--step launch会自动入队未完成的） |
| XML解析率 | 0 failed_parse | 检查tmux pane输出，看XML格式是否正确 |
| 6字段填写率 | ≥95%（允许少量unclear，但不应该大量为空或MISSING） | 如果大量MISSING，检查模板是否正确注入 |

**B. 值分布合理性检查**

| 字段 | 合理分布 | 异常信号 |
|---|---|---|
| suitable | YES和NO都有，NO占多数（AIME题大部分不涉及局部-全局切换） | 全YES（标准过松）或全NO（标准过严） |
| false_friend_candidate | 大部分no，少量yes或unclear | 全yes（假朋友识别过松）或全no且suitable=NO题多（可能没认真识别） |
| boundary_case_candidate | 大部分no，少量yes或unclear | 全yes（边界识别过松） |
| process_signal_observability | suitable=YES题应为high/medium，suitable=NO题unclear合理 | suitable=YES题全low（过程信号不可观察，POC-3用不了） |
| leakage_risk | 大部分low/medium，少量high | 全high（泄漏风险预评过严） |
| difficulty_estimate | 应有easy/medium/hard分布，与batch对应 | 全hard（没有区分度）或全easy（过松） |
| branch_position_hint | root和line都应出现 | 全root或全line（没有区分度） |

**C. 字段间逻辑一致性检查**

- suitable=YES的题：batch不应为N/A，d2_reclassified应有具体子类型
- suitable=NO的题：batch应为N/A
- suitable=YES且process_signal_observability=low：标记为POC-0精筛时的降优先级题
- suitable=YES且leakage_risk=high：标记为POC-0精筛时的降优先级题
- false_friend_candidate=yes仅应出现在suitable=NO的题中（YES题不可能是假朋友）

**D. 跨组趋势检查（从第2组开始）**

- 累计suitable=YES的题数是否在合理范围（每5题约0-2道YES）
- 6个字段的累计分布是否稳定（不是第1组全hard、第2组全easy这种突变）
- 是否出现rate limit（如果有failed=rate_limited，降低并发数）

#### 检查不通过时的处理

| 问题 | 处理 |
|---|---|
| 6字段大量MISSING | 检查模板是否正确注入（grep 6个字段名在生成的AGENTS.md中） |
| 6字段大量unclear | 可接受——Pipe 3是二阶判断，信息不足时unclear是诚实回答。但如果suitable=YES题的process_signal_observability全是unclear，说明d2_exp质量不够 |
| suitable全NO | 检查这5题的d1是否都是TOKEN_LIMIT/CONNECTION_ERROR（如果是，说明collect读到了不该读的审计结果） |
| suitable全YES | 检查选题标准是否过松（d1是否真的都是DIRECTION_ERROR） |
| difficulty全hard | 412号模板中difficulty判定指引偏粗，AI可能对不涉及局部-全局切换的题默认标hard。这是低价值字段（410号§2说"低价值"），不影响POC-0精筛，可接受 |
| rate limit | 降低并发到1，暂停20分钟后重试（388号§4.1机制） |

#### 通过检查后继续下一组

检查通过后，collect下一组5题继续运行。累计suitable=YES的题达到30-50道时可以停止（412号§7.1的完成标准）。

---

