# 错题分析（Pipe 1）产出总结

> **生成时间**：2026-08-17 04:40 UTC
> **Pipe**：Pipe 1（分析Pipe）
> **目标**：对解题系统中运行错误的题目，用devin cli分析AI为什么做错——判定d1（失败类型）和d2（标准解答关键转折点类型）

---

## 1. 数据规模

| 指标 | 数量 | 说明 |
|---|---|---|
| analysis_results（已收集结果） | **2050条** | 含重复 |
| 唯一problem_id | **1589个** | 去重后 |
| analysis_runs总任务 | 6325个 | 含所有batch |
| 已收集（results_collected） | 2047个 | |
| 还在queued（未跑） | 4177个 | 可后续补跑 |

### 1.1 batch分布

| batch | 总任务 | 已收集 | 说明 |
|---|---|---|---|
| full-analysis-30c | 3180 | 1453 | 主批次，还有1623个queued |
| full-analysis-v2 | 3145 | 544 | 早期批次，还有2554个queued |
| polish-1~10 | 各5 | 各5 | 10轮打磨迭代改进提示词 |

### 1.2 每条结果的字段

| 字段 | 说明 |
|---|---|
| problem_id | 题目ID |
| dimension1_verdict (d1) | AI失败类型：DIRECTION_ERROR / TOKEN_LIMIT / CONNECTION_ERROR / PARTIAL_PROGRESS |
| dimension1_explanation (d1_exp) | AI为什么失败的详细解释 |
| dimension2_turning_point_type (d2) | 标准解答关键转折点类型：10种子类型 + other |
| dimension2_explanation (d2_exp) | 标准解答关键技巧的详细解释 |
| ai_direction_summary | AI实际走了什么方向 |
| standard_solution_key_technique | 标准解答用了什么具体技巧 |
| confidence | 分析AI的置信度（high/medium/low） |

---

## 2. d1分布（2050条结果）

| d1 | 数量 | 占比 | 含义 | Mid-Hint选题适用性 |
|---|---|---|---|---|
| **DIRECTION_ERROR** | **1096** | **53%** | AI走错方向 | **适合（核心选题来源）** |
| CONNECTION_ERROR | 360 | 18% | 技术失败 | 不适合 |
| TOKEN_LIMIT | 360 | 18% | 方向对了但token不够 | 不适合 |
| PARTIAL_PROGRESS | 166 | 8% | 部分进展 | 不纳入选题 |
| None | 68 | 3% | 解析失败 | 无法使用 |

---

## 3. d2分布（1096个DIRECTION_ERROR中）

| d2类型 | 数量 | Mid-Hint批次 | 说明 |
|---|---|---|---|
| **other** | **984** | **需Pipe 3语义再分类** | 未归入10种子类型——Pipe 3选题的核心工作 |
| None | 41 | — | 缺d2分类 |
| mod_p_grouping | 29 | 批次1（低难度） | mod p取模分组 |
| finite_field_structure | 13 | 可扩展 | 有限域结构 |
| crt | 11 | 批次3（高难度） | CRT多模数组合 |
| multi_step_mod_p | 8 | 批次2（中难度） | 多步mod p |
| quadratic_residue_euler | 4 | 批次3（高难度） | 二次剩余+Euler准则 |
| mod_p_non_obvious | 3 | 批次2（中难度） | 非显然mod p |
| p_adic_valuation | 2 | 批次2（中难度） | p-adic赋值 |
| permutation_polynomial | 1 | 可扩展 | 有限域置换多项式 |

### 3.1 d2=other的再分类潜力

d2=other的984条中，根据关键词预调查：

| 关键词 | 题数 | 可能归入 |
|---|---|---|
| modular | 923 | mod_p_* |
| finite field | 152 | finite_field_structure |
| residue | 140 | quadratic_residue_euler |
| LTE | 135 | lte_lemma |
| quadratic | 135 | quadratic_residue_euler |
| p-adic | 86 | p_adic_valuation |
| CRT | 68 | crt |
| valuation | 59 | p_adic_valuation |

**注意**：关键词预调查只是粗粒度估计，实际再分类由Pipe 3选题AI做语义判断。

---

## 4. 与Pipe 2审计的关系

Pipe 1的2050条结果经去重后得到1521个唯一题目，Pipe 2对这1521个题目做质量审计。

| Pipe 2审计状态 | 数量 | 说明 |
|---|---|---|
| completed | 1385 | 审计完成，结果在audit_results集合 |
| prepared（重跑中） | 135 | 原failed_stall/rate_limited，并发1重跑 |

Pipe 2审计结果中，**721个PASS_SELECTABLE**可直接用于Pipe 3选题。

详见 `audit-full1/audit_summary.md`。

---

## 5. 与Mid-Hint实验的关系

Mid-Hint实验（eight-system第五阶段）需要"标准解答用了局部-全局切换，但AI没走这个方向"的题。Pipe 1的产出正是这个需求的输入：

- d1=DIRECTION_ERROR → AI没走正确方向 ✅
- d2∈{mod_p_*, QR, p_adic, LTE, CRT, finite_field} → 标准解答用了局部-全局切换 ✅
- d2=other → 需要Pipe 3选题AI做语义再分类

**选题流程**：Pipe 1（本文件）→ Pipe 2审计（audit_summary.md）→ Pipe 3选题（待执行）→ Mid-Hint实验

---

## 6. 未完成的工作

1. **4177个queued未跑**：analysis_runs中还有4177个任务未执行。当前2050条结果覆盖1589个唯一题目，已足够开始Pipe 3选题。如需扩大选题池，可后续补跑。
2. **68个d1=null**：解析失败的题目，无法用于选题。如需修复，需要检查原始XML。
3. **461个重复**：2050条结果对应1589个唯一题目，Pipe 2审计前已去重（保留confidence=high + 字段最完整的）。

---

## 7. 相关文件

| 文件 | 说明 |
|---|---|
| `analysis-devin-failure-system/src/analysis_launcher.py` | Pipe 1启动器 |
| `analysis-devin-failure-system/src/result_collector.py` | Pipe 1结果收集器 |
| `analysis-devin-failure-system/templates/analysis_agents_md.md` | Pipe 1提示词模板 |
| `analysis-devin-failure-system/output/audit-full1/audit_summary.md` | Pipe 2审计总结 |
| `dev-docs/387号` | 错题分析系统审计与选题方案（三Pipe方案） |
