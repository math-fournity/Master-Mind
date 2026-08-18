# POC-9 资产 · 失败trace选题

**日期**：2026-08-17
**用途**：POC-9（识别端验证）的失败trace测试样本选取
**来源**：409号§4.1的选取标准 + 382号4道source trace题 + 387号错题分析系统DIRECTION_ERROR题
**目标**：选取10-20道失败trace作为POC-9的测试样本

---

## 1. 选取标准（409号§4.1）

POC-9需要两类失败trace：

1. **有完整的bare AI thinking**（不是截断的/解析失败的）
2. **有标准解答**（用于参照"AI本应该走什么方向"）
3. **覆盖不同的d2子类型**（mod_p_grouping / quadratic_residue_euler / crt / p_adic_valuation等），以测试系统能否识别不同类型的分叉

---

## 2. 来源1：CasePack v1的4道source trace题（CC-001~004，直接纳入）

这4道题（1631/1843/1709/1962）已有完整的bare失败记录和bare AI thinking。它们是000号tell端定义的原始POC例子。v1保留了v0的source trace题不变。

| 序号 | problem_id | d2子类型 | bare失败记录状态 | 标准解答状态 | thinking完整性状态 | 分叉类型 |
|---|---|---|---|---|---|---|
| 1 | 1631 | quadratic_residue_euler | ✅完整——VMS-7g-v3/VMS-8/VMS-9三次bare失败，无proof.md | ✅verified——k=2，Euler准则证明 | ✅完整——bare thinking有完整记录 | 根节点分叉：AI选了covering system/枚举，本应选二次剩余 |
| 2 | 1843 | mod_p_grouping | ✅完整——VMS-7g-v3/VMS-8/VMS-9三次bare失败 | ✅verified——2016，模4符号配对证明 | ✅完整——bare thinking有完整记录 | 根节点分叉：AI选了多项式符号分析，本应选模4分组 |
| 3 | 1709 | p_adic_valuation | ✅完整——VMS-10 bare失败，无proof.md | ✅verified——a是2的幂，2-adic赋值证明 | ✅完整——bare thinking约66037字符，有完整记录 | 根节点分叉：AI选了枚举/函数分析，本应选2-adic赋值 |
| 4 | 1962 | p_adic_valuation | ✅完整——VMS-7g-v3/VMS-8 bare失败，VMS-8 tree组仍失败 | ⚠️partial——v_2分析思路完整但一般情形需完整验证 | ✅完整——bare thinking和tree组thinking都有完整记录 | line上分叉：AI方向正确（p-adic）但展开方式走错，本应拐向分case简化 |

**4道题的分叉类型覆盖**：
- 根节点分叉（Root Branch）：1631, 1843, 1709（3道）
- line上分叉（Point Branch）：1962（1道）
- 翻译类型分叉：1631（穷举→结构）, 1843（连续→离散）
- 操作路径分叉：1962（展开方式→分case）

---

## 3. 来源2：387号错题分析系统DIRECTION_ERROR题（选取10-16道）

### 3.1 数据背景（387号§2.2）

387号错题分析系统现有结果1982条，其中：
- **DIRECTION_ERROR**：1071条（54%）——AI方向出错，适合作为失败trace
- CONNECTION_ERROR：360条（18%）——技术失败，不适合
- TOKEN_LIMIT：331条（17%）——AI方向对了，不适合
- PARTIAL_PROGRESS：152条（8%）——不纳入选题（原始选题理念中没有中间地带）
- None：68条（3%）——解析失败，无法判断

**DIRECTION_ERROR + 有d2分类的题：70条**（核心选题池）：

| d2子类型 | 数量 | Mid-Hint批次 | 本POC-9计划选取数 |
|---|---|---|---|
| mod_p_grouping | 28 | 批次1（低难度） | 3道 |
| finite_field_structure | 13 | 可扩展 | 2道 |
| crt | 11 | 批次3（高难度） | 2道 |
| multi_step_mod_p | 8 | 批次2（中难度） | 2道 |
| quadratic_residue_euler | 4 | 批次3（高难度） | 2道 |
| mod_p_non_obvious | 3 | 批次2（中难度） | 1道 |
| p_adic_valuation | 2 | 批次2（中难度） | 1道 |
| permutation_polynomial | 1 | 可扩展 | 1道 |
| **合计** | **70** | | **14道** |

### 3.2 选取策略

从70条有d2分类的DIRECTION_ERROR题中，按d2子类型各选1-3道，覆盖所有8种d2子类型，共14道。

选取数量按各子类型的题量加权：
- 题量≥10的子类型选2-3道（mod_p_grouping 3道, finite_field_structure 2道, crt 2道, multi_step_mod_p 2道）
- 题量4-9的子类型选2道（quadratic_residue_euler 2道）
- 题量1-3的子类型选1道（mod_p_non_obvious 1道, p_adic_valuation 1道, permutation_polynomial 1道）

### 3.3 选取的14道题

**重要**：387号文档中没有列出具体的problem_id——387号§2.2只给出了d2子类型的数量分布，没有列出每道题的problem_id。因此以下14道题的problem_id需要从ArangoDB analysis_results集合查询。

**查询方法**：从ArangoDB的analysis_results集合中，查询d1=DIRECTION_ERROR且d2为以下子类型的题，按上述数量选取。查询条件：
- d1 = "DIRECTION_ERROR"
- d2 ∈ 指定子类型
- 审计状态 = 通过-可选题（Pipe 2审计通过且可选题）
- thinking完整性 = 完整（不是截断的/解析失败的）

```yaml
failure_traces_from_387:
  # 从387号DIRECTION_ERROR + 有d2分类的70条中选取14道
  # 需从ArangoDB analysis_results集合查询具体problem_id
  # 查询条件：d1=DIRECTION_ERROR, d2=指定子类型, audit_status=通过-可选题

  # --- mod_p_grouping（3道）---
  - problem_id: "需从ArangoDB查询——d2=mod_p_grouping的第1道"
    d2_subtype: mod_p_grouping
    bare_failure_record_status: "需确认——DIRECTION_ERROR题应有完整bare thinking"
    standard_solution_status: "需确认——应从OlympiadBench获取标准解答"
    thinking_completeness: "需确认——筛选条件要求完整非截断"
    selection_note: "批次1低难度，mod p取模分组型"

  - problem_id: "需从ArangoDB查询——d2=mod_p_grouping的第2道"
    d2_subtype: mod_p_grouping
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次1低难度，mod p取模分组型"

  - problem_id: "需从ArangoDB查询——d2=mod_p_grouping的第3道"
    d2_subtype: mod_p_grouping
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次1低难度，mod p取模分组型"

  # --- finite_field_structure（2道）---
  - problem_id: "需从ArangoDB查询——d2=finite_field_structure的第1道"
    d2_subtype: finite_field_structure
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "可扩展，有限域结构型"

  - problem_id: "需从ArangoDB查询——d2=finite_field_structure的第2道"
    d2_subtype: finite_field_structure
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "可扩展，有限域结构型"

  # --- crt（2道）---
  - problem_id: "需从ArangoDB查询——d2=crt的第1道"
    d2_subtype: crt
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次3高难度，中国剩余定理多模数组合型"

  - problem_id: "需从ArangoDB查询——d2=crt的第2道"
    d2_subtype: crt
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次3高难度，中国剩余定理多模数组合型"

  # --- multi_step_mod_p（2道）---
  - problem_id: "需从ArangoDB查询——d2=multi_step_mod_p的第1道"
    d2_subtype: multi_step_mod_p
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次2中难度，多步mod p分析型"

  - problem_id: "需从ArangoDB查询——d2=multi_step_mod_p的第2道"
    d2_subtype: multi_step_mod_p
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次2中难度，多步mod p分析型"

  # --- quadratic_residue_euler（2道）---
  - problem_id: "需从ArangoDB查询——d2=quadratic_residue_euler的第1道"
    d2_subtype: quadratic_residue_euler
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次3高难度，二次剩余+Euler准则型"

  - problem_id: "需从ArangoDB查询——d2=quadratic_residue_euler的第2道"
    d2_subtype: quadratic_residue_euler
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次3高难度，二次剩余+Euler准则型"

  # --- mod_p_non_obvious（1道）---
  - problem_id: "需从ArangoDB查询——d2=mod_p_non_obvious的第1道"
    d2_subtype: mod_p_non_obvious
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次2中难度，非显然的mod p分析型"

  # --- p_adic_valuation（1道）---
  - problem_id: "需从ArangoDB查询——d2=p_adic_valuation的第1道"
    d2_subtype: p_adic_valuation
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "批次2中难度，p-adic赋值型"

  # --- permutation_polynomial（1道）---
  - problem_id: "需从ArangoDB查询——d2=permutation_polynomial的第1道"
    d2_subtype: permutation_polynomial
    bare_failure_record_status: "需确认"
    standard_solution_status: "需确认"
    thinking_completeness: "需确认"
    selection_note: "可扩展，有限域上的置换多项式型"
```

### 3.4 ArangoDB查询脚本要求

执行POC-9前，需要从ArangoDB analysis_results集合查询上述14道题的具体problem_id。查询脚本要求：

```python
# 查询伪代码（不是可执行脚本，是查询需求说明）
# ArangoDB连接：echo $ARANGO_DB 应输出 xishujuzhen_math_glm52
# 集合：analysis_results

# 查询条件：
# FOR doc IN analysis_results
#   FILTER doc.d1 == "DIRECTION_ERROR"
#   FILTER doc.d2 IN [
#     "mod_p_grouping", "finite_field_structure", "crt",
#     "multi_step_mod_p", "quadratic_residue_euler",
#     "mod_p_non_obvious", "p_adic_valuation", "permutation_polynomial"
#   ]
#   FILTER doc.audit_status == "通过-可选题"  # Pipe 2审计通过
#   SORT doc.d2, doc.confidence DESC
#   RETURN {
#     problem_id: doc.problem_id,
#     d1: doc.d1,
#     d2: doc.d2,
#     d1_exp: doc.d1_exp,
#     d2_exp: doc.d2_exp,
#     ai_direction_summary: doc.ai_direction_summary,
#     standard_solution_key_technique: doc.standard_solution_key_technique,
#     confidence: doc.confidence
#   }

# 然后按d2子类型分组，各取前N道：
# mod_p_grouping: 取前3道
# finite_field_structure: 取前2道
# crt: 取前2道
# multi_step_mod_p: 取前2道
# quadratic_residue_euler: 取前2道
# mod_p_non_obvious: 取前1道
# p_adic_valuation: 取前1道
# permutation_polynomial: 取前1道（仅1条可用）
```

---

## 4. 最终测试样本汇总

| 序号 | problem_id | 来源 | d2子类型 | 分叉类型 | bare失败记录 | 标准解答 | thinking完整性 |
|---|---|---|---|---|---|---|---|
| 1 | 1631 | 382号 | quadratic_residue_euler | 根节点分叉 | ✅完整 | ✅verified | ✅完整 |
| 2 | 1843 | 382号 | mod_p_grouping | 根节点分叉 | ✅完整 | ✅verified | ✅完整 |
| 3 | 1709 | 382号 | p_adic_valuation | 根节点分叉 | ✅完整 | ✅verified | ✅完整 |
| 4 | 1962 | 382号 | p_adic_valuation | line上分叉 | ✅完整 | ⚠️partial | ✅完整 |
| 5 | 需查询 | 387号 | mod_p_grouping | 待识别 | 需确认 | 需确认 | 需确认 |
| 6 | 需查询 | 387号 | mod_p_grouping | 待识别 | 需确认 | 需确认 | 需确认 |
| 7 | 需查询 | 387号 | mod_p_grouping | 待识别 | 需确认 | 需确认 | 需确认 |
| 8 | 需查询 | 387号 | finite_field_structure | 待识别 | 需确认 | 需确认 | 需确认 |
| 9 | 需查询 | 387号 | finite_field_structure | 待识别 | 需确认 | 需确认 | 需确认 |
| 10 | 需查询 | 387号 | crt | 待识别 | 需确认 | 需确认 | 需确认 |
| 11 | 需查询 | 387号 | crt | 待识别 | 需确认 | 需确认 | 需确认 |
| 12 | 需查询 | 387号 | multi_step_mod_p | 待识别 | 需确认 | 需确认 | 需确认 |
| 13 | 需查询 | 387号 | multi_step_mod_p | 待识别 | 需确认 | 需确认 | 需确认 |
| 14 | 需查询 | 387号 | quadratic_residue_euler | 待识别 | 需确认 | 需确认 | 需确认 |
| 15 | 需查询 | 387号 | quadratic_residue_euler | 待识别 | 需确认 | 需确认 | 需确认 |
| 16 | 需查询 | 387号 | mod_p_non_obvious | 待识别 | 需确认 | 需确认 | 需确认 |
| 17 | 需查询 | 387号 | p_adic_valuation | 待识别 | 需确认 | 需确认 | 需确认 |
| 18 | 需查询 | 387号 | permutation_polynomial | 待识别 | 需确认 | 需确认 | 需确认 |

**总计：18道**（4道来自382号 + 14道来自387号）

---

## 5. d2子类型覆盖检查

| d2子类型 | 来自382号 | 来自387号 | 合计 | 覆盖 |
|---|---|---|---|---|
| mod_p_grouping | 1（1843） | 3 | 4 | ✅ |
| finite_field_structure | 0 | 2 | 2 | ✅ |
| crt | 0 | 2 | 2 | ✅ |
| multi_step_mod_p | 0 | 2 | 2 | ✅ |
| quadratic_residue_euler | 1（1631） | 2 | 3 | ✅ |
| mod_p_non_obvious | 0 | 1 | 1 | ✅ |
| p_adic_valuation | 2（1709, 1962） | 1 | 3 | ✅ |
| permutation_polynomial | 0 | 1 | 1 | ✅ |
| **合计** | **4** | **14** | **18** | **8种全覆盖** |

所有8种d2子类型均有覆盖。最多的是mod_p_grouping（4道）和p_adic_valuation（3道），最少的是mod_p_non_obvious和permutation_polynomial（各1道）。

---

## 6. 分叉类型覆盖检查

| 分叉类型 | 来自382号 | 来自387号 | 说明 |
|---|---|---|---|
| 根节点分叉（Root Branch） | 3（1631, 1843, 1709） | 待识别 | 387号的题需要在系统识别后才能确定分叉类型 |
| line上分叉（Point Branch） | 1（1962） | 待识别 | 同上 |
| 翻译类型分叉 | 2（1631穷举→结构, 1843连续→离散） | 待识别 | 同上 |
| 操作路径分叉 | 1（1962展开方式→分case） | 待识别 | 同上 |

**注**：387号的14道题的分叉类型需要在POC-9执行时由系统识别和人类专家独立识别后才能确定。选取时只保证d2子类型覆盖，不保证分叉类型覆盖——分叉类型的覆盖是POC-9的验证目标之一。

---

## 7. 后续行动

### 7.1 立即需要做的

1. **从ArangoDB查询14道题的problem_id**——执行§3.4的查询，获取具体的problem_id列表
2. **确认14道题的bare失败记录和thinking完整性**——查询后逐一检查
3. **获取14道题的标准解答**——从OlympiadBench或其他来源获取

### 7.2 POC-9执行时需要做的

1. 对18道失败trace执行系统识别（识别端分析器从bare AI thinking中读出000号tell端四个成分）
2. 对18道失败trace执行人类专家独立识别（双盲——专家不看到系统识别结果）
3. 对照系统识别和人类专家识别的四个成分，计算一致率/遗漏率/误报率
4. 分析系统能识别多少种不同类型的分叉

### 7.3 如果387号的70条中某些d2子类型没有足够的题

如果ArangoDB查询后发现某个d2子类型的可用题不足（如permutation_polynomial仅1条，如果该条不满足完整性/可选题条件则无可用题），则：
- 从d2=other中按Pipe 3的再分类结果选取补充题（387号§4.3）
- 或从382号CasePack的其他题中选取补充（如正迁移题CC-007/1681的bare失败记录）
- 不足的d2子类型标注为"覆盖不足"，在POC-9结果中记录
