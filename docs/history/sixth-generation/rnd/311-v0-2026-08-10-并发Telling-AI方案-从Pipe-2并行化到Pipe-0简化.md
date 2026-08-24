# 并发Telling AI方案——从Pipe 2并行化到Pipe 0简化

**文档编号**：311-v0
**日期**：2026-08-10
**作者**：worktree侧 AI（GLM-5.2 High）
**触发**：用户提出"暴力并发Telling AI解决tell识别问题"的构想，并表达对Pipe 0/1拓扑阶段失败的担心
**前置文档**：310号（worktree侧对grove侧303-309号文档的评审）、309号（trace-tell-hint统一命名）、305号（非局部tell的识别价值）、第五代系统技术说明书（50个文件）
**性质**：架构方案——第六代tell识别的并发化设计，修正第五代Pipe 0/1/2串行架构
**关键词**：并发Telling AI、Pipe 2并行化、Pipe 0简化、粗domain分类、trace识别、分区、汇总AI

---

## 0. 为什么记录本文档

用户在310号评审之后提出了两个关键问题：

1. **"tell分析不能并发吗？多个sub agent并发？"**——提出把tell数据基座分区，每个Telling AI实例负责一个区，并行对同一份推理AI上下文做trace识别。

2. **"我很担心我们的拓扑那个阶段是失败的，我在考虑是不是要暴力并发Telling AI解决tell识别问题？"**——表达对Pipe 0/1形式化拓扑阶段的失败担心，考虑用暴力并发替代。

本文档完整记录这两个问题的分析过程和得出的方案。方案的核心判断是：**不是"放弃Pipe 0/1用暴力并发"或"坚持Pipe 0/1不用并发"——是"Pipe 0简化+Pipe 2并发"的混合方案。**

---

## 1. 用户担心的"拓扑阶段失败"具体指什么

Pipe 0/1的形式化拓扑阶段有两个层面的失败风险：

### 1.1 层面1：拓扑化方法本身太粗糙

Pipe 0当前实现（第五代 `07-工程规格/02-Pipe-0接口定义.md`）是信号词频次统计，3个维度各2个取值：

| 维度 | 取值 |
|---|---|
| problem_type | discrete_combinatorial / structural_existence |
| ai_method_type | continuous_analytic / enumeration_brute_force |
| gap_type | method_problem_mismatch / other |

总共 **2×2×2=8种拓扑组合**。

当前数据基座有4164个tell（据另一个AI的统计：局部tell 3192 + 全局tell 972）。平均每个拓扑组合有 **4164/8 ≈ 520个tell**。Pipe 1形式化过滤只能从4164缩小到~520——缩小8倍，但520个tell仍然太多，放不进单个辅助AI的上下文。

而且信号词是手工设计的（`SIGNAL_WORDS`字典），第五代 `08-验证状态/04-验证总结与待验证项.md` 明确列出的局限是"只有2个tell——无法验证10万级规模"和"Pipe 0的信号词是手工设计的"。

**结论**：8种拓扑组合在4164个tell的规模下已经不够细——每区520个tell，Pipe 1的缩小效果不足以让Pipe 2的单AI上下文可控。

### 1.2 层面2：拓扑化能不能捕捉非局部tell

303/305号引入了非局部tell——"模分析无尽追逐"这种段特征。Pipe 0的信号词频次统计捕捉的是"thinking里出现了哪些关键词"，不是"thinking的结构模式是什么"。

非局部tell的识别需要理解段的结构（追逐/桥接/构造-分析-排除），这不是信号词频次能捕捉的。

**结论**：Pipe 0的信号词频次方法在非局部tell场景下失败——它只能捕捉"thinking里出现了mod/prime/divisibility等词"，不能捕捉"AI从a5到a11一直在做模分析追逐"这个段结构。

### 1.3 用户的担心是合理的

两个层面的失败风险都真实存在。Pipe 0/1的精确拓扑化在当前规模（4164个tell）下已经不够用，在非局部tell场景下方法本身不适用。

---

## 2. 暴力并发Telling AI的代价分析

### 2.1 真暴力方案

不经过任何前置过滤，把4164个tell分成N个区，每个Telling AI读完整thinking+自己区的tell，并行做trace识别。

### 2.2 规模代价

假设thinking是50K tokens，4164个tell按大概念分10个区，每区~416个tell约12K tokens：

| 规模 | 分区数 | 并发Telling AI数 | 每个AI上下文 | 总token消耗 |
|---|---|---|---|---|
| 当前4164 tell | 10区×416 tell | 10 | 50K+12K+5K=67K | 670K |
| Tier 2预计5500 tell | 14区×416 tell | 14 | 67K | 938K |
| 未来10万级tell | 250区×416 tell | 250 | 67K | 16.75M |

### 2.3 三个问题

**问题1：当前规模可行，未来规模不可行**

当前10个并发、670K总token——可行。但未来10万级tell需要250个并发、16.75M总token——并发数和token消耗都爆炸。

**问题2：每个Telling AI都要读完整thinking——重复消耗**

每个Telling AI都需要完整理解thinking才能做trace识别。这部分每个Telling AI都在重复做。10个并发时重复消耗是9×50K=450K的浪费。

**但这不完全是bug，可能是feature**——每个Telling AI带着自己区的tell视角去理解thinking，可能看到不同的trace。区1的Telling AI带着"数论tell"的视角看thinking，看到的是数论相关的trace；区2的Telling AI带着"代数tell"的视角看thinking，看到的是代数相关的trace。**多视角并行理解，比单视角全局扫描可能更全面。** 这和305号的多视角理解一致。

**问题3：汇总瓶颈**

10个Telling AI各产出几个trace，汇总AI处理几十个trace还行。250个Telling AI产出几百个trace，汇总AI又回到大规模问题。

### 2.4 关键问题：不经过前置过滤，怎么知道当前thinking应该发给哪些Telling AI？

如果发给所有Telling AI——当前规模可行，未来规模不可行。

如果只发给相关区的Telling AI——那你又需要一个前置过滤来确定"哪些区相关"，这个前置过滤就是Pipe 0/1做的事。

**暴力并发绕不开前置过滤问题——只是把前置过滤从"缩小tell范围"变成了"选择Telling AI实例"。**

---

## 3. 方案：Pipe 0简化 + Pipe 2并行化

### 3.1 核心判断

**不是"放弃Pipe 0/1用暴力并发"或"坚持Pipe 0/1不用并发"——是"Pipe 0简化+Pipe 2并发"的混合方案。**

| 第五代原设计 | 第六代新设计 | 变化 |
|---|---|---|
| Pipe 0：精确拓扑化（3维度8种组合+手工信号词） | Pipe 0简化：粗domain分类（数论/代数/组合/几何/跨域） | 简化——从精确拓扑降级为粗分类 |
| Pipe 1：用拓扑匹配缩小tell范围 | Pipe 1：用domain分类选择启动哪些区的Telling AI | 角色变了——从缩小tell范围变为选择Telling AI实例 |
| Pipe 2：单AI在缩小范围内做标记分辨 | Pipe 2并行：多Telling AI并行trace识别+汇总AI精筛 | 并行化——从单AI串行变为多AI并行 |

### 3.2 Pipe 0不应该放弃，但应该简化

Pipe 0当前的失败风险在于**追求精确拓扑化但方法太粗糙**（3维度8种组合+手工信号词）。

但如果把Pipe 0的目标从"精确拓扑化"降级为"粗domain分类"——只判断"这道thinking大概属于数论/代数/组合/几何/跨域中的哪几个"——这个粗分类比精确拓扑化鲁棒得多。

**粗domain分类不需要精确**——只需要"数论区的Telling AI应该被启动"这个判断对。即使分错了（把数论题分到代数区），代价是漏掉相关tell，不是系统崩溃。

**粗domain分类的实现方式**：
- 可以用LLM做一次轻量判断（读thinking前1000 tokens，判断domain）——不需要信号词频次统计
- 可以用题目本身的domain标签（如果题目有domain元数据）——不需要分析thinking
- 可以用thinking的开头部分做domain分类——AI通常在开头就会提到问题领域

### 3.3 Pipe 1的形式化过滤保留但角色变了

原来Pipe 1是"用拓扑匹配从10万级tell缩小到数百候选"——这是硬约束，因为单AI上下文放不下10万级tell。

现在Pipe 1的角色变成"用domain分类确定启动哪些区的Telling AI"——不再是缩小tell范围，而是**选择Telling AI实例**。这是更轻量的任务。

**Pipe 1的新接口**：
```
输入：domain分类结果（如"数论+代数"）
输出：需要启动的Telling AI实例列表（如["Telling_AI_数论", "Telling_AI_代数"]）
```

### 3.4 Pipe 2并行化——用户方案真正有价值的部分

每个区的Telling AI并行做trace识别：
- 每个Telling AI只加载自己区的tell（~416个tell约12K tokens）
- 读完整thinking（50K）
- 上下文可控（67K）
- 产出自己区视角下的trace集合

汇总AI从各Telling AI产出的trace中选最终tell——处理几十个trace，不是4164个tell。

### 3.5 完整方案

```
thinking（50K tokens）
    │
    ▼ Pipe 0简化版：粗domain分类（不是信号词频次）
    │  实现方式：LLM轻量判断 / 题目domain标签 / thinking开头分类
    │  输出："这道题大概属于数论+代数"
    │
    ▼ Pipe 1新角色：选择启动哪些区的Telling AI
    │  只启动数论区和代数区的Telling AI（2个，不是全部10个）
    │
    ▼ Pipe 2并行化
    │
    ├── Telling AI #数论
    │   [读完整thinking 50K + 416个数论tell 12K + 提示词 5K = 67K上下文]
    │   → 带着数论tell视角理解thinking
    │   → 产出数论视角的trace集合
    │
    ├── Telling AI #代数
    │   [读完整thinking 50K + 416个代数tell 12K + 提示词 5K = 67K上下文]
    │   → 带着代数tell视角理解thinking
    │   → 产出代数视角的trace集合
    │
    ▼ 汇总AI
    │  输入：数论trace集合 + 代数trace集合（共几十个trace）
    │  任务：从几十个trace中选最终tell
    │  上下文：几十个trace + 提示词 = 轻量
    │
    ▼ tell → hint
    │
    ▼ 给新推理AI
```

---

## 4. 这个方案的好处和代价

### 4.1 好处

1. **Pipe 0简化了**——粗domain分类比精确拓扑化鲁棒，不需要手工信号词。不追求8种拓扑组合的精确判定，只追求"数论vs代数vs组合"的粗分类。

2. **并发数可控**——只启动相关区的Telling AI（2-3个），不是全部N个。Pipe 0的粗domain分类决定了启动哪些区。

3. **每个Telling AI上下文可控**——67K tokens（50K thinking + 12K tell + 5K提示词），远低于上下文上限。

4. **汇总AI负担轻**——只处理几十个trace，不是4164个tell。两级过滤：第一级Telling AI并行粗筛（每个从416个tell中筛出几个trace），第二级汇总AI精筛（从几十个trace中选最终tell）。

5. **规模可扩展**——tell增长时增加分区数，但每个Telling AI的上下文不变（每区tell数控制在~416个）。

6. **多视角并行理解**——每个Telling AI带着自己区的tell视角理解thinking，可能看到不同的trace。这和305号的多视角理解一致——数论视角看到"模分析追逐"，代数视角可能看到"因式分解方向未尝试"。

7. **和非局部tell兼容**——Telling AI读完整thinking，能识别段结构（追逐/桥接/构造-分析-排除），不局限于信号词频次。Pipe 0的粗domain分类不试图捕捉非局部tell，非局部tell的识别交给Telling AI的语义理解。

### 4.2 代价

1. **Pipe 0的粗domain分类可能分错**——漏掉相关区的Telling AI。
   - 缓解：允许"跨域"分类，启动跨域区的Telling AI作为兜底。
   - 缓解：允许Telling AI返回"这个trace不属于我的区"的信号，汇总AI据此判断是否需要启动其他区的Telling AI。

2. **每个Telling AI都要读完整thinking——重复消耗**。
   - 10个并发时重复消耗是9×50K=450K的浪费。
   - 但这是多视角理解的代价，可能是feature不是bug（305号的多视角并行理解）。
   - 如果thinking很长（100K+），可以考虑只给Telling AI读thinking的摘要+关键段，不是完整thinking。但这会损失非局部tell的识别能力（非局部tell需要看整段结构）。

3. **domain分类的粒度需要实验确定**——太粗（4个domain）则每区tell太多，太细则分区数爆炸。
   - 当前4164个tell / 4个domain = 1041 tell/domain——每区仍然太多。
   - 当前4164个tell / 10个区 = 416 tell/区——可控。
   - 需要实验确定分区粒度：按domain分（4区）太粗，按domain×problem_type分（8-16区）可能合适，按大概念拓扑分（第五代原8种组合）可能太细且方法有失败风险。

4. **汇总AI的判断标准需要定义**——
   - 如果是"所有Telling AI找到的trace取并集"——简单，但可能有冲突（不同区找到的trace矛盾）。
   - 如果是"汇总AI再做一次判断"——又回到单AI，但这次单AI只需要处理几十个trace（已经被Telling AI过滤过），不需要处理4164个tell。
   - 第二种更合理——两级过滤。

---

## 5. 与第五代架构的关系

### 5.1 这不是范式转变，是Pipe 2并行化

310号评审中对309号的判断需要修正：

| 主张 | 判断 |
|---|---|
| 309号原主张："辅助AI直接分析thinking，Pipe 0/1/2融合成一次分析" | 仍然跑偏——大规模下不能融合，Pipe 0/1的前置过滤是分区的前置 |
| 用户后续提出的"分区后并发Telling AI" | **不跑偏——这是Pipe 2并行化，和Pipe 0/1兼容** |

用户的并发Telling AI方案回答了309号没回答的问题："如果辅助AI是智能的，怎么处理大规模tell？"309号说"直接分析"——大规模下不行。用户说"分区后并行"——大规模下可行，因为每个Telling AI只需要加载一个区的tell。

### 5.2 和概念树的兼容性

第五代 `04-概念树/03-概念树的按需加载.md` 的概念文件按需加载机制和本方案完全兼容——每个区的tell就是一个大概念下的概念文件，Telling AI加载的就是概念文件。

区别是：第五代原设计是"单AI加载1个概念文件做标记分辨"，本方案是"多AI并行各加载1个概念文件做trace识别"。

### 5.3 和trace/tell/hint命名的兼容性

309号的trace/tell/hint命名在本方案中完整成立：
- 每个Telling AI产出的是**trace**（对当前thinking的识别结果，具体的、和当前题目绑定的）
- 汇总AI从trace中匹配**tell**（数据库中标准化的trace描述）
- tell关联的**hint**被取出给新推理AI

### 5.4 和非局部tell的兼容性

305号的非局部tell在本方案中得到更好的支持——
- 第五代原设计中Pipe 0/1的信号词频次方法不能捕捉非局部tell
- 本方案中Telling AI读完整thinking，能理解段结构，能识别非局部tell
- 每个Telling AI带着自己区的tell视角去理解thinking，可能识别出自己区视角下的非局部tell

---

## 6. 需要进一步想清楚的问题

### 6.1 分区依据是什么

按domain分（数论/代数/组合/几何/跨域）？按大概念拓扑分（第五代原8种组合）？按其他依据分？

- 按domain分：粗但鲁棒，每区~1000个tell（当前规模），需要二次分区
- 按大概念拓扑分：细但方法有失败风险（§1.1-1.2），每区~520个tell
- 按 domain × problem_type 分：中等粒度，每区~250-500个tell

**建议**：先用domain分（最鲁棒），如果某区tell太多（>500），在该区内再用problem_type二次分区。这是"层次分区"——和第五代概念树的层次结构一致。

### 6.2 Telling AI的提示词是什么

Telling AI需要被告知：
- 你的区里有哪些tell（完整列表）
- 当前推理AI的thinking（完整文本）
- 你的任务：识别thinking中和你区的tell相关的trace

提示词模板需要设计——这是工程问题，不是架构问题。

### 6.3 汇总AI的判断标准是什么

汇总AI面对几十个trace，需要：
- 去重（不同Telling AI可能找到相同的trace）
- 排序（哪些trace更值得给出hint）
- 冲突解决（不同Telling AI找到的trace矛盾时怎么办）

判断标准需要设计——可能和第五代Pipe 2的combined_score类似，但作用于trace而不是tell。

### 6.4 规模增长的应对

| 规模 | 分区数 | 每区tell数 | 并发Telling AI数 | 可行性 |
|---|---|---|---|---|
| 当前4164 | 10 | 416 | 2-3（只启动相关区） | ✅ 可行 |
| Tier 2预计5500 | 14 | 416 | 2-3 | ✅ 可行 |
| 未来1万 | 25 | 400 | 2-3 | ✅ 可行 |
| 未来10万 | 250 | 400 | 2-3（如果domain分类足够精确） | ⚠️ 需要更精确的domain分类 |

关键：**并发Telling AI数不随tell总数增长——只随"当前thinking相关的domain数"增长**。一道数学题通常涉及1-3个domain，所以并发数通常2-3个，无论tell总数是4164还是10万。

但前提是domain分类足够精确——如果domain分类分错了，需要启动更多区的Telling AI作为兜底，并发数会上升。

---

## 7. 对310号评审的修正

本文档修正310号评审中对309号的判断：

| 310号原判断 | 修正后判断 |
|---|---|
| 309号"范式转变"跑偏——绕过了10万级规模硬约束 | 309号原主张（Pipe 0/1/2融合成一次分析）仍然跑偏，但用户后续提出的"分区后并发Telling AI"是Pipe 2并行化，不跑偏 |

同时修正对Pipe 0/1的判断：

| 310号原判断 | 修正后判断 |
|---|---|
| Pipe 0/1的形式化过滤在大规模下是硬约束 | Pipe 0/1的形式化过滤仍然需要，但角色变了——Pipe 0从精确拓扑化简化为粗domain分类，Pipe 1从缩小tell范围变为选择Telling AI实例。Pipe 2从单AI标记分辨变为多AI并行trace识别+汇总 |

---

## 8. 来源

- 用户提问："tell分析不能并发吗？多个sub agent并发？" + "我很担心我们的拓扑那个阶段是失败的，我在考虑是不是要暴力并发Telling AI解决tell识别问题？"
- 前置文档：310号（worktree侧评审）、309号（trace-tell-hint命名）、305号（非局部tell识别价值）
- 第五代参照：`07-工程规格/02-Pipe-0接口定义.md`（Pipe 0当前实现）、`02-tell端/04-Pipe-1-形式化过滤.md`（Pipe 1硬约束）、`08-验证状态/04-验证总结与待验证项.md`（Pipe 0局限）、`04-概念树/03-概念树的按需加载.md`（概念文件按需加载）
- 数据基座统计：4164个tell（局部3192+全局972），122K tokens，455个profile
