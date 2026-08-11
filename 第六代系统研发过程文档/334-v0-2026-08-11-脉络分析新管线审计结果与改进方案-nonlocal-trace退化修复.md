# 334号 · 脉络分析新管线审计结果与改进方案——nonlocal trace退化修复

**日期**：2026-08-11
**状态**：方案设计（待实现）
**来源**：333号方案实现后的第一次审计——新管线vs当初4套POC的逐维度对比
**审计对象**：run_id=0005（三阶段架构）vs baseline（V5/V7/V8/V10各自独立做完整流程的4套POC）

---

## 1. 审计背景

### 1.1 审计动机

333号方案把脉络分析从"4并发完整流程"改为"三阶段架构（格化→程序枚举→综合分析）"。改动很大——不仅是代码结构变了，AI的认知路径也变了。必须审计：新管线是让脉络分析更丰富完备了，还是因为管线设计/提示词的不当导致退化？

### 1.2 审计对象

| 数据集 | 说明 | 位置 |
|---|---|---|
| **baseline**（当初4套POC） | V5/V7/V8/V10各自独立做完整流程，取并集 | `system/tests/vein_analysis/baseline/` |
| **run_id=0004**（三阶段架构第一次运行） | 三阶段架构的第一次运行，有Trace构造bug | `palyground/absorb/vein_analysis/0004_imo2009p6/` |
| **run_id=0005**（三阶段架构第二次运行） | 修复Trace构造bug后的运行，非交互模式 | `palyground/absorb/vein_analysis/0005_imo2009p6/` |

### 1.3 审计维度（来自333号§4.4）

| 维度 | 检查内容 | 判定标准 |
|---|---|---|
| trace数量 | 新架构trace总数 vs baseline并集 | 新架构 ≥ baseline的80% |
| trace语义覆盖 | baseline每个trace在新架构中是否有语义等价 | 覆盖率 ≥ 70% |
| 闭元素完备性 | 程序枚举闭元素数 vs baseline各版本闭元素数 | 程序枚举 ≥ baseline最大值 |
| AI优势元素 | 新架构是否覆盖baseline中有价值的AI优势元素 | 覆盖基线中有价值的 |
| 关键实体 | 新架构key_entities是否覆盖baseline | 遗漏 ≤ 20% |
| 元反思trace | 新架构meta_reflection_traces是否覆盖baseline | 内容价值不亚于baseline |
| **trace类型分布** | 新架构各类型trace数量 vs baseline | **无类型显著退化**（本次审计新增） |
| **adv_3语义层面元模式** | 新架构是否识别出"aₙ跳过障碍" | **必须识别出** |

---

## 2. 审计结果

### 2.1 总体判定

**新管线在语义层面不亚于当初4套POC，在多个维度上更丰富，但有一个明确的退化点：nonlocal trace显著减少。**

### 2.2 逐维度结果

| 维度 | baseline | 新管线(0005) | 判定 |
|---|---|---|---|
| trace数量 | 49（并集去重） | 43 | ✅ 覆盖88%，>任何单个版本 |
| 闭元素完备性 | V8=20(max) | 程序枚举V8=48 | ✅ 更完备 |
| AI优势元素 | 11（并集去重） | 6（覆盖10/11） | ✅ 覆盖91%，且有2个新发现 |
| 关键实体 | 11 | 9 | ⚠️ 粒度差异，不是缺失 |
| 元反思trace | 2 | 2 | ✅ 覆盖+2个新发现 |
| **trace类型分布** | nonlocal~20 | **nonlocal=7** | **❌ 退化——少了13个** |
| adv_3语义层面元模式 | adv_5 | adv_2 | ✅ 识别出 |

### 2.3 trace类型分布详细对比

| 类型 | 新管线 | baseline并集(估) | 判定 |
|---|---|---|---|
| local | 21 | ~18 | ✅ 更丰富 |
| **nonlocal** | **7** | **~20** | **❌ 退化——少了13个** |
| global | 8 | ~6 | ✅ 更丰富 |
| **cross_case_merge** | **1** | **~3** | **⚠️ 退化——少了2个** |
| cross_element_meta_pattern | 6 | ~2 | ✅ 更丰富 |

### 2.4 AI优势元素语义对照

baseline 11个AI优势元素中，新管线覆盖10个：

| baseline | 新管线 | 覆盖方式 |
|---|---|---|
| adv_1 存在性避障vs交换避障 | adv_4 预防性vs修复性避障 | ✅ 语义等价 |
| adv_2 定义辅助量刻画冲突结构 | trace_6/trace_7 | ⚠️ 作为trace覆盖，未作为adv |
| adv_3 强归纳声明跨Case贯穿 | trace_34 | ✅ 作为trace覆盖 |
| adv_4 子问题归约 | trace_30 | ✅ 作为trace覆盖 |
| adv_5 aₙ跳过障碍 | adv_2 | ✅ 语义等价 |
| adv_6 归纳-缩减-构造-验证四步曲 | adv_5 三Case并行5步结构 | ✅ 语义等价 |
| adv_7 情况分析策略连接三Case | trace_29 | ✅ 作为trace覆盖 |
| adv_8 swap避障技巧统一目的 | adv_1 | ✅ 语义等价 |
| adv_9 集合缩减M'统一目的 | trace_33 | ✅ 作为trace覆盖 |
| adv_10 鸽巢论证完整策略 | trace_22 | ✅ 作为trace覆盖 |
| adv_11 bad index完整使用链 | trace_22 | ✅ 作为trace覆盖 |

新管线独有（baseline没有的）：
- adv_3 x的多功能角色——baseline V8的adv_4有类似内容，但新管线更系统
- adv_6 s作为隐藏贯穿变量——**baseline完全没有，这是新管线的新发现**

---

## 3. 退化根因分析

### 3.1 退化点

**nonlocal trace退化（7 vs ~20）是核心问题**。nonlocal trace是跨多个段的trace——baseline的4套POC各自独立做完整流程时，每个版本都会从段内容出发识别nonlocal trace，4个版本取并集得到~20个。新管线的综合分析Agent只识别了7个。

### 3.2 根因

根因在**333号方案的§2.4设计**——综合分析Agent的工作流程：

```
第一步：形式上下文回溯检查
第二步：对每个闭元素做语义解读
第三步：识别跨闭元素元模式
第四步：审计+元反思
```

这个流程**以闭元素为中心**——对每个闭元素做语义解读。但nonlocal trace不一定对应闭元素——nonlocal trace是"跨多个段的思维模式"，可能不是任何闭元素的内涵能捕获的。

baseline的4套POC在做完整流程时，AI会从段的内容出发识别nonlocal trace（不依赖闭元素），而新管线的综合分析Agent从闭元素出发做语义解读（依赖闭元素），导致nonlocal trace减少。

**cross_case_merge退化（1 vs ~3）**也是同样根因——cross_case_merge是跨Case的非相邻段合并，不一定对应闭元素。

### 3.3 333号方案已预见但未覆盖的风险

333号方案的§2.4.2已经预见到了"程序不能完全替代AI"的风险，并要求AI做"对每个闭元素做语义解读"和"识别跨闭元素元模式"。但方案没有要求AI做"**不依赖闭元素的nonlocal trace识别**"——这是方案的一个待改进点。

---

## 4. 改进方案

### 4.1 核心改进

在综合分析Agent的工作流程中，在"对每个闭元素做语义解读"之前，加一步"**从段内容出发识别nonlocal trace**"——不依赖闭元素，直接从段的内容和段间关系出发，识别跨多个段的思维模式。

### 4.2 改进后的综合分析Agent工作流程

```
第一步：形式上下文回溯检查——质疑(G,M,I)是否完美
第二步：从段内容出发识别nonlocal trace（新增）——不依赖闭元素
第三步：对每个闭元素做语义解读——这个闭元素代表什么思维模式？是不是trace？
第四步：识别跨闭元素元模式——变量/技巧贯穿多个闭元素的统一角色
第五步：识别跨Case非相邻合并（cross_case_merge）——不依赖闭元素
第六步：审计+元反思
```

### 4.3 提示词改动

在`synthesis.md`提示词中，在"闭元素语义解读"步骤之前，加"nonlocal trace识别"步骤：

```markdown
## 第二步：从段内容出发识别nonlocal trace（不依赖闭元素）

**为什么需要这一步**：闭元素枚举是段集合层面的完备运算，但nonlocal trace
不一定对应任何闭元素——nonlocal trace是"跨多个段的思维模式"，可能不是任何
闭元素的内涵能捕获的。

**怎么做**：从段的内容和段间关系出发，识别跨多个段的思维模式：
- 哪些段在思维上属于同一个"论证链"？（比如"定义bad index→构造注入映射→
  鸽巢论证得好指标r"是一个3段的论证链）
- 哪些段在思维上构成"对比"或"呼应"？（比如"段1 WLOG排序"和"段21一般情形
  归约"是首尾呼应）
- 哪些段共享同一个"关键变量的使用"？（比如x在多个段中作为分类标准/边界量/
  验证依据）

**产出**：列出所有识别到的nonlocal trace，每个给出trace描述和涉及的段编号。
这些trace可能不是任何闭元素的内涵能捕获的——这正是它们的价值所在。
```

同时在"跨闭元素元模式"步骤之后，加"cross_case_merge识别"步骤：

```markdown
## 第五步：识别跨Case非相邻合并（cross_case_merge）

**为什么需要这一步**：cross_case_merge是跨Case的非相邻段合并——这些段在
不同Case中但本质相同，它们的合并不一定对应任何闭元素。

**怎么做**：对比三个Case的段，找出"本质相同但在不同Case中"的段集合：
- Case 1的验证段、Case 2的验证段、Case 3的验证段——本质都是"前缀和验证
  避开M"
- Case 1的M'构造段、Case 2的M'构造段、Case 3的M'构造段——本质都是
  "缩减M为归纳创造条件"

**产出**：列出所有cross_case_merge trace，每个给出trace描述和涉及的段编号。
```

---

## 5. 后续审计方案

### 5.1 审计原则

**所有改进必须和所有历史运行结果对比分析，确保改进是完全正向的。**

不只和baseline（当初4套POC）对比，还要和之前的每次新管线运行结果对比——确保改进不会修复一个问题却引入另一个问题。

### 5.2 历史运行结果清单

每次运行结果必须永久存档，作为未来审计的对比基线：

| 运行 | 说明 | 位置 | 存档位置 |
|---|---|---|---|
| baseline V5/V7/V8/V10 | 当初4套POC | `palyground/absorb/vein_analysis/imo2009p6/V{5,7,8,10}/` | `system/tests/vein_analysis/baseline/` ✅已存档 |
| run_id=0004 | 三阶段架构第一次运行（有Trace构造bug） | `palyground/absorb/vein_analysis/0004_imo2009p6/` | 待存档到`system/tests/vein_analysis/runs/0004/` |
| run_id=0005 | 三阶段架构第二次运行（修复Trace构造bug+非交互模式） | `palyground/absorb/vein_analysis/0005_imo2009p6/` | 待存档到`system/tests/vein_analysis/runs/0005/` |
| run_id=0006+ | 改进后的运行 | 待运行 | 存档到`system/tests/vein_analysis/runs/0006/` |

### 5.3 存档规范

每次运行结果存档到`system/tests/vein_analysis/runs/{run_id}/`，包含：
- `phase2_synthesis/output.json`——综合分析产出
- `phase2_synthesis/output.md`——人类可读报告
- `phase1_grading/V{5,7,8,10}/segments.json`——格化产出
- `phase1_grading/V{5,7,8,10}/formal_context.json`——形式上下文（V5无）
- `phase1_5_enumerate/V{7,8,10}_closed_elements.json`——程序枚举闭元素
- `audit_report.md`——本次运行的审计报告（见§5.4）

### 5.4 审计流程

每次改进后运行新管线，然后执行以下审计流程：

**第一步：收集所有历史运行结果**
- baseline（4套POC的output.json）
- 之前每次新管线运行的output.json（0004, 0005, 0006, ...）

**第二步：逐维度对比**

对每次历史运行，做以下维度对比：

| 维度 | 对比方式 |
|---|---|
| trace数量 | 新运行 vs 每次历史运行 |
| trace类型分布 | 新运行 vs 每次历史运行——**无类型显著退化** |
| 闭元素完备性 | 新运行程序枚举 vs 每次历史运行 |
| AI优势元素 | 新运行 vs 每次历史运行——语义对照 |
| 关键实体 | 新运行 vs 每次历史运行 |
| 元反思trace | 新运行 vs 每次历史运行 |
| adv_3语义层面元模式 | 新运行是否识别出"aₙ跳过障碍" |

**第三步：判定标准**

改进被判定为"完全正向"的条件：
1. **无退化**——任何维度不得比任何历史运行退化（允许持平，不允许退化）
2. **有进步**——至少一个维度比所有历史运行都有进步
3. **adv_3不丢**——必须识别出"aₙ跳过障碍"语义层面元模式

如果改进在某个维度比某个历史运行退化——即使比baseline好——也不算完全正向，需要继续改进。

**第四步：写审计报告**

每次审计写报告到`system/tests/vein_analysis/runs/{run_id}/audit_report.md`，包含：
- 和baseline的对比
- 和每次历史运行的对比
- 逐维度判定结果
- 总体判定（完全正向/部分正向/退化）
- 如果有退化：退化点分析+下一步改进方向

### 5.5 审计脚本

改进`run_poc_no_loss.py`为`run_audit.py`——不只和baseline对比，和所有历史运行对比：

```python
# run_audit.py的对比逻辑
baseline = load_baseline()  # baseline/V{5,7,8,10}_output.json
historical_runs = load_all_runs()  # runs/0004/, runs/0005/, runs/0006/, ...
new_run = load_current_run()  # 当前运行的output.json

# 对每个历史运行+baseline做逐维度对比
for run in [baseline] + historical_runs:
    comparison = compare(new_run, run)
    # 检查是否有退化
    if comparison.has_regression():
        print(f"⚠️ 相比{run.name}退化: {comparison.regression_details}")
```

### 5.6 迭代终止条件

**迭代改进直到满足以下所有条件**：
1. 和baseline对比：所有维度无退化（nonlocal trace ≥ baseline的80%）
2. 和所有历史运行对比：所有维度无退化
3. adv_3语义层面元模式识别出
4. trace类型分布无显著退化（任何类型不得比任何历史运行少30%以上）

---

## 6. 实现计划

### 6.1 改进步骤

| 步骤 | 内容 | 产出 |
|---|---|---|
| 1 | 改synthesis.md提示词——加nonlocal trace识别步骤 | `system/assets/vein_analysis/synthesis.md`更新 |
| 2 | 改synthesis.md提示词——加cross_case_merge识别步骤 | 同上 |
| 3 | 存档0004和0005的运行结果到`system/tests/vein_analysis/runs/` | 历史运行存档 |
| 4 | 用IMO 2009 P6跑改进后的新管线（run_id=0006） | `palyground/absorb/vein_analysis/0006_imo2009p6/` |
| 5 | 运行审计脚本——和baseline+0004+0005对比 | `audit_report.md` |
| 6 | 检查审计结果——无退化则完成，有退化则继续改进 | |

### 6.2 审计脚本改进

| 步骤 | 内容 | 产出 |
|---|---|---|
| 1 | 改`run_poc_no_loss.py`为`run_audit.py`——支持多历史运行对比 | `system/tests/vein_analysis/run_audit.py` |
| 2 | 加trace类型分布维度 | 同上 |
| 3 | 加语义对照维度（不只是关键词匹配） | 同上 |
| 4 | 加"和所有历史运行对比"的逻辑 | 同上 |

---

## 7. 和333号方案的关系

本方案是333号方案的改进——不是替代。333号方案的三阶段架构（格化→程序枚举→综合分析）是正确的，问题出在综合分析Agent的工作流程缺了一步"从段内容出发识别nonlocal trace"。

333号方案的§2.4.2已经预见到"程序不能完全替代AI"的风险，并要求AI做"对每个闭元素做语义解读"和"识别跨闭元素元模式"。本方案在此基础上加一步"从段内容出发识别nonlocal trace"——这是333号方案没有覆盖的，是本次审计发现的待改进点。

---

## 8. 待决策的问题

1. **nonlocal trace识别步骤应该放在回溯检查之前还是之后**：放在之前可能不受闭元素影响，放在之后可以借助闭元素信息。建议放在之前——先从段内容出发，再看闭元素。

2. **cross_case_merge是否应该和nonlocal trace合并为一步**：cross_case_merge是nonlocal trace的子集（跨Case的nonlocal trace），可以合并。建议合并——减少步骤数，让AI更自然地识别。

3. **审计脚本是否应该自动化语义对照**：当前语义对照是人工做的，自动化需要语义匹配算法。建议先人工，等改进稳定后再自动化。
