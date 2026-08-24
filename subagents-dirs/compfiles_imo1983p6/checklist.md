# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1983p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1983P6.lean
- **来源**: IMO 1983 P6
- **ArangoDB progress记录_key**: 329104（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1983P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设a,b,c为三角形的三边长，证明 a²b(a-b) + b²c(b-c) + c²a(c-a) ≥ 0，并确定等号成立的条件。
- 解答核心思路（1-2句话）：通过Ravi替换 x=(-a+b+c)/2, y=(a-b+c)/2, z=(a+b-c)/2 将三角形约束转化为正数约束，再用Cauchy-Schwarz不等式证明 xyz(x+y+z) ≤ xy³+yz³+zx³，等号当且仅当x=y=z即a=b=c时成立。
- 解答关键步骤列表：
  1. 利用三角形不等式得到 a<b+c, b<a+c, c<a+b
  2. Ravi替换：x=(-a+b+c)/2, y=(a-b+c)/2, z=(a+b-c)/2，则x,y,z>0且a=y+z, b=z+x, c=x+y
  3. 将原不等式转化为 xyz(x+y+z) ≤ xy³+yz³+zx³
  4. 构造Cauchy-Schwarz向量 f=[√x·√(y³), √y·√(z³), √z·√(x³)], g=[√z, √x, √y]
  5. 由Cauchy-Schwarz: (∑f·g)² ≤ (∑f²)(∑g²)，即 (√xyz·(x+y+z))² ≤ (xy³+yz³+zx³)(x+y+z)
  6. 两边除以(x+y+z)>0得 xyz(x+y+z) ≤ xy³+yz³+zx³
  7. 等号条件：Cauchy-Schwarz等号⟺f与g成比例⟺x=y=z⟺a=b=c（等边三角形）

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**每轮必须标注**：
- **question**：给AI的提示/问题（Q）
- **expected_answer**：预期回复（A）
- **situation_type**：**⚠️ 只能取以下6个值之一，禁止自创**：
  - `纯元认知观察`——让AI描述题目结构、识别已知/未知
  - `自由列举`——让AI列出所有可能方向
  - `小尝试`——让AI试一个方向（可能走错的）
  - `思维操作引导`——给AI具体的思维操作指令
  - `推进`——让AI继续推进当前方向
  - `能量传递引导`——给AI信心/能量，收尾
- **level**：**⚠️ 必须是0-1之间的浮点数**（0=完全具体，1=完全抽象。禁止用1-4整数）

**QA序列设计原则**：
1. 第1轮通常是`纯元认知观察`——让AI描述题目结构
2. 第2轮通常是`自由列举`——让AI列出所有可能方向
3. 第3轮通常是`小尝试`——让AI试一个可能走错的方向
4. 中间几轮根据情况用`思维操作引导`或`推进`
5. 最后一轮通常是`能量传递引导`——收尾

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的结构：已知什么？要证明什么？表达式 a²b(a-b)+b²c(b-c)+c²a(c-a) 有什么结构特征？ | 已知a,b,c是三角形边长（满足三角形不等式），要证明一个循环不对称的三次多项式不等式≥0，并求等号条件。表达式是循环的但不完全对称，每项形如"边²·邻边·(边-邻边)"，结构上难以直接因式分解或配凑。 |
| 2 | 自由列举 | 0.7 | 对于三角形边长相关的不等式，你能想到哪些处理方向？ | ①直接展开因式分解；②排序假设（WLOG a≥b≥c）后分析符号；③Schur不等式或已知不等式工具；④Ravi替换（令x,y,z为半周长分量，将三角形约束转为正数约束）；⑤SOS（平方和）方法；⑥换元后用经典不等式（Cauchy-Schwarz/AM-GM等）。 |
| 3 | 小尝试 | 0.5 | 试试直接展开 a²b(a-b)+b²c(b-c)+c²a(c-a) 并尝试因式分解，看看能不能直接证明非负性。 | 展开后得到 a³b-a²b²+b³c-b²c²+c³a-c²a²，这是一个循环多项式。直接因式分解困难——尝试a=b=c时为0，但无法简单提取(a-b)类因子。排序假设也不太有效，因为表达式不是对称的，无法WLOG假设a≥b≥c。这条路走不通。 |
| 4 | 思维操作引导 | 0.4 | 三角形边长这个条件还没有被充分利用。请执行Ravi替换：令x=(-a+b+c)/2, y=(a-b+c)/2, z=(a+b-c)/2，则x,y,z>0且a=y+z, b=z+x, c=x+y。将原表达式用x,y,z表示，看看新的不等式是什么。 | 代入后，原不等式 a²b(a-b)+b²c(b-c)+c²a(c-a)≥0 转化为 xy³+yz³+zx³ ≥ xyz(x+y+z)，即 xyz(x+y+z) ≤ xy³+yz³+zx³。这个新形式更简洁，且x,y,z仅为正数（不再有三角形约束）。 |
| 5 | 思维操作引导 | 0.3 | 现在需要证明 xyz(x+y+z) ≤ xy³+yz³+zx³。观察右边xy³+yz³+zx³的结构，能否将其拆分为两个向量的内积平方形式，从而用Cauchy-Schwarz不等式？提示：考虑 f=[√x·√(y³), √y·√(z³), √z·√(x³)] 和 g=[√z, √x, √y]。 | 令f=[√x·√(y³), √y·√(z³), √z·√(x³)], g=[√z, √x, √y]。则 ∑f²=xy³+yz³+zx³, ∑g²=x+y+z, ∑f·g=√x·√(y³)·√z+√y·√(z³)·√x+√z·√(x³)·√y=√(xyz)(y+x+z)=√(xyz)(x+y+z)。由Cauchy-Schwarz: (√(xyz)(x+y+z))² ≤ (xy³+yz³+zx³)(x+y+z)，两边除以(x+y+z)即得 xyz(x+y+z) ≤ xy³+yz³+zx³。 |
| 6 | 推进 | 0.5 | 现在确定等号成立的条件。Cauchy-Schwarz等号成立的条件是什么？由此推出x,y,z满足什么关系，再推出a,b,c满足什么关系。 | Cauchy-Schwarz等号⟺f与g成比例，即存在r使得 r·√x·√(y³)=√z, r·√y·√(z³)=√x, r·√z·√(x³)=√y。平方后得 r²·xy³=z, r²·yz³=x, r²·zx³=y。三式相乘得 r⁶·x²y²z²·xyz=xyz，即r⁶=1，r=1（正数）。代入得xy³=z, yz³=x, zx³=y，联立解出x=y=z，即a=b=c（等边三角形）。 |
| 7 | 能量传递引导 | 0.6 | 回顾整个证明：Ravi替换将三角形约束转化为正数约束，Cauchy-Schwarz以精巧的向量构造一举完成证明。请总结完整证明并确认等号条件。 | 完整证明：①Ravi替换将问题转化为正数x,y,z上的 xyz(x+y+z)≤xy³+yz³+zx³；②构造Cauchy-Schwarz向量f,g，内积为√(xyz)(x+y+z)，平方后除以(x+y+z)得证；③等号当且仅当f∥g即x=y=z即a=b=c。证明完整，等号条件为等边三角形。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 5（Cauchy-Schwarz向量构造是关键知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 4（Ravi替换的动机是思维瓶颈——需要意识到三角形约束需要被"消化"）

---

## Step 3: 标注问题拓扑层 [x]

**操作**：从题目结构中提取

**要求**：
- `problem_type`：问题类型大概念。**优先使用已有值**（见下方拓扑分类体系），如需新建确保粒度一致
- `structure_features`：题目结构特征描述
- `key_objects`：核心数学对象列表

**已有problem_type值**（优先使用）：
- `structural_existence` ✅ 抽象
- `discrete_combinatorial` ✅ 抽象
- `trigonometric_identity` ✅ 中等
- `constraint_satisfaction` ✅ 中等
- `characterization` ✅ 抽象
- `inequality_proof` ✅ 中等
- `absolute_value_system` ⚠️ 偏具体
- `functional_equation_periodicity` ⚠️ 偏具体
- **❌ 不要用太具体的值**（如`word_problem_with_diophantine_constraint`是错误粒度）

**产出**：
- problem_type: inequality_proof
- structure_features: 循环不对称三次多项式不等式，带三角形边长约束，需确定等号条件。表达式具有循环结构但不完全对称，直接展开因式分解困难，需要通过变量替换将约束条件转化为正数约束后用经典不等式工具。
- key_objects: ["三角形边长a,b,c", "循环三次多项式 a²b(a-b)+b²c(b-c)+c²a(c-a)", "Ravi替换变量x,y,z（半周长分量）", "Cauchy-Schwarz不等式", "等号条件（等边三角形）"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["约束转化（将三角形约束通过Ravi替换转化为正数约束）", "变量替换简化（用半周长分量替换边长，消除约束）", "经典不等式应用（Cauchy-Schwarz的精巧向量构造）", "等号条件追溯（从Cauchy-Schwarz等号条件反推变量关系）", "失败诊断（直接展开因式分解走不通后及时转向）"]
- primary_pattern: 约束转化（将隐含的三角形约束通过Ravi替换显式化为正数约束，使问题从约束优化变为无约束不等式）
- knowledge_required: ["Ravi替换（三角形边长到半周长分量的标准替换）", "Cauchy-Schwarz不等式", "Cauchy-Schwarz等号条件（向量成比例）", "三角形不等式"]
- key_insight: 将三角形边长用Ravi替换转化为正数x,y,z后，原不等式变为xyz(x+y+z)≤xy³+yz³+zx³，而右边恰好可以拆成Cauchy-Schwarz的两个向量内积平方形式——关键是构造f=[√x·√(y³),√y·√(z³),√z·√(x³)]和g=[√z,√x,√y]使内积恰好为√(xyz)(x+y+z)。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接多项式不等式（在三角形边长a,b,c上的循环三次多项式）
- translation_to: Cauchy-Schwarz内积不等式（在正数x,y,z上的向量内积平方形式）
- translation_type: method_translation（通过Ravi替换将约束多项式不等式翻译为无约束的Cauchy-Schwarz内积形式）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["循环不对称多项式", "三角形边长约束", "Ravi替换", "半周长分量", "Cauchy-Schwarz向量构造", "等号条件追溯"]
- expected_ai_method: bare AI预期会尝试直接展开多项式并因式分解，或尝试排序假设后分析符号——这些方法在循环不对称结构上走不通
- correct_method: Ravi替换将三角形约束转化为正数约束，再用Cauchy-Schwarz不等式以精巧的向量构造完成证明

**已有ai_method_type值**（优先使用）：
- `enumeration_brute_force` ✅ 抽象
- `continuous_analytic` ✅ 抽象
- `direct_calculation` ✅ 抽象
- `logical_deduction` ✅ 抽象
- `case_by_case` ✅ 抽象
- `algebraic_identity` ✅ 中等
- `equation_solving` ✅ 抽象
- `direct_manipulation` ✅ 抽象
- **❌ 不要用太长太具体的值**

**已有gap_type值**（优先使用）：
- `method_problem_mismatch` ✅ 抽象
- `knowledge_gap` ✅ 抽象
- `structural_transformation` ✅ 中等
- `search_space_estimation` ✅ 中等
- `method_translation` ✅ 中等
- `global_sorting` ⚠️ 偏具体
- **❌ 不要用太具体的值**

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type(inequality_proof)/ai_method_type(direct_calculation)/gap_type(method_translation)都能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——inequality_proof是中等粒度，direct_calculation是抽象粒度，method_translation是中等粒度，与已有值粒度一致。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。这道题的核心gap是"需要将约束多项式不等式翻译为Cauchy-Schwarz内积形式"，method_translation准确描述了这个gap。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无，现有拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**⚠️ 每个tell_hint_pair必须包含以下所有字段**：
- `qa_round`: int（对应QA序列的第几轮）
- `tell`: string（AI在这个位置的状态/分叉信号）
- `hint`: string（给AI的提示方向）
- `hint_level`: float（**⚠️ 0-1浮点数，禁止1-4整数**）
- `situation_type`: string（**⚠️ 只能取6个规范值之一**）
- `is_knowledge_bottleneck`: boolean（这轮是否是纯知识瓶颈）
- `tell_topology`: object（**⚠️ 每个pair都要有，不能全用profile级拓扑**）
  - `{problem_type, ai_method_type, gap_type}`
  - **不同轮次的pair可能有不同的拓扑**——比如R1是`(inequality_proof, direct_calculation, method_problem_mismatch)`，R2是`(structural_existence, case_by_case, structural_transformation)`
  - `is_knowledge_bottleneck=True`的pair，`gap_type`应该用`knowledge_gap`
- `tell_small_concepts`: array[string]（**⚠️ 每个pair都要有**，是这个tell特有的小概念信号词）

**同时提取全局(tell, hint)对**：
- `scope_type`: "path_feature"（路径特征型）或 "implicit"（蕴含型）
- `scope`: 具体范围描述
- `observation_point`: 蕴含型填Q编号，路径特征型填null
- `tell`: 全局tell
- `hint`: 全局hint
- `hint_level`: float（0-1）
- `generalizability`: "high/medium/low + 泛化描述"
- `why_not_visible_locally`: **必填字段，不能为None**。path_feature型和implicit型都要填。path_feature型填"完整路径特征为什么在局部视角看不到"；implicit型填"这个蕴含信息为什么在局部步骤中不可见"
- `tell_topology`: object（**⚠️ 每个全局pair也要有**）
- `tell_small_concepts`: array[string]（**⚠️ 每个全局pair也要有**）

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对循环不对称三次多项式不等式，尚未识别三角形约束的作用 | 描述题目结构，识别已知/未知和表达式特征 | 0.8 | 纯元认知观察 | false | {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch} | ["循环不对称多项式", "三角形边长约束"] |
| 2 | AI已识别题目结构但尚未选择方向 | 列出所有可能方向（因式分解、排序、Schur、Ravi替换、SOS等） | 0.7 | 自由列举 | false | {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch} | ["因式分解", "排序假设", "Schur不等式", "Ravi替换", "SOS方法"] |
| 3 | AI尝试直接展开因式分解，发现循环不对称结构无法简单分解 | 试直接展开因式分解，验证走不通 | 0.5 | 小尝试 | false | {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_problem_mismatch} | ["多项式展开", "因式分解失败", "循环不对称"] |
| 4 | AI因式分解失败后卡住，未意识到三角形约束需要被消化 | 执行Ravi替换，将三角形约束转化为正数约束 | 0.4 | 思维操作引导 | false | {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: structural_transformation} | ["Ravi替换", "半周长分量", "约束转化", "正数约束"] |
| 5 | AI已完成Ravi替换得到xyz(x+y+z)≤xy³+yz³+zx³，但不知道如何用Cauchy-Schwarz | 构造Cauchy-Schwarz向量f和g，使内积为√(xyz)(x+y+z) | 0.3 | 思维操作引导 | true | {problem_type: inequality_proof, ai_method_type: algebraic_identity, gap_type: knowledge_gap} | ["Cauchy-Schwarz向量构造", "内积平方形式", "√x·√(y³)", "向量成比例"] |
| 6 | AI已用Cauchy-Schwarz完成不等式证明，需要确定等号条件 | 从Cauchy-Schwarz等号条件（向量成比例）反推x=y=z | 0.5 | 推进 | false | {problem_type: inequality_proof, ai_method_type: logical_deduction, gap_type: method_translation} | ["Cauchy-Schwarz等号条件", "向量成比例", "x=y=z", "等边三角形"] |
| 7 | AI已完成全部证明，需要总结确认 | 回顾完整证明路径，确认等号条件 | 0.6 | 能量传递引导 | false | {problem_type: inequality_proof, ai_method_type: logical_deduction, gap_type: method_translation} | ["Ravi替换", "Cauchy-Schwarz", "等边三角形", "证明总结"] |

**全局tell_hint_pairs详情**：

| # | scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | path_feature | 完整证明路径R1→R7 | null | 整个证明路径的特征是"约束转化→经典不等式应用"两步跳跃：先Ravi替换消化三角形约束，再Cauchy-Schwarz精巧构造完成不等式。这两步缺一不可，且第二步的向量构造高度非显然 | 遇到带几何约束的多项式不等式时，先考虑用变量替换将约束消化为正数约束，再在无约束框架下用经典不等式工具（Cauchy-Schwarz/AM-GM等）的精巧构造完成 | 0.7 | high——"约束转化+经典不等式精巧构造"模式适用于大量带约束的不等式问题 | 在局部视角中，R3只看到因式分解失败，R4只看到Ravi替换后的新形式，R5只看到Cauchy-Schwarz构造——每一步都看不到"为什么这两步组合在一起能work"的全局模式。只有完整路径才能看出"约束消化+经典不等式精巧构造"是统一策略 | {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_translation} | ["约束转化", "Ravi替换", "Cauchy-Schwarz精巧构造", "两步跳跃策略"] |
| 2 | implicit | Ravi替换后的不等式形式 | Q4 | Ravi替换后得到的xyz(x+y+z)≤xy³+yz³+zx³蕴含着一个隐藏的Cauchy-Schwarz结构：右边的三项xy³,yz³,zx³可以分别写成(√x·√(y³))²,(√y·√(z³))²,(√z·√(x³))²，而左边的xyz(x+y+z)可以写成(√(xyz))²·(x+y+z)，恰好是(∑f·g)²/(∑g²)的形式 | 观察右边的每一项是否可以写成某个量的平方，从而构造Cauchy-Schwarz的f向量；同时观察左边是否可以写成内积平方除以模长平方的形式 | 0.4 | high——"将多项式不等式识别为Cauchy-Schwarz的内积形式"是一个广泛适用的技巧 | 在局部视角中，AI只看到xyz(x+y+z)≤xy³+yz³+zx³这个不等式，但"右边的每一项可以写成平方"和"左边可以写成内积平方除以模长平方"这两个观察需要同时成立且相互配合，单独看任一边都看不出Cauchy-Schwarz结构。这个蕴含信息在局部步骤中不可见，因为需要同时识别两边的平方结构并匹配 | {problem_type: inequality_proof, ai_method_type: algebraic_identity, gap_type: knowledge_gap} | ["Cauchy-Schwarz内积形式识别", "平方结构", "xy³=(√x·√(y³))²", "内积平方除以模长平方"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接展开多项式因式分解或排序假设分析符号，在循环不对称结构上走不通后可能尝试Schur不等式但无法直接匹配。关键瓶颈在于：(1)不一定想到Ravi替换来消化三角形约束；(2)即使做了Ravi替换，也很难发现xy³+yz³+zx³可以拆成Cauchy-Schwarz的向量内积平方形式——这个构造高度非显然。
- suitable_for_poc: ["POC-VMS-8（hint端验证：脉络继承+方向注入）", "POC-VMS-9/10（tell端验证：去特化+形式化过滤+小概念标记分辨）", "约束转化型tell的识别实验", "知识瓶颈型tell（Cauchy-Schwarz构造）的识别实验"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [ ] _key（=problem_id）
- [ ] source_id
- [ ] source_dataset
- [ ] schema_version（=3）
- [ ] problem_text
- [ ] solution_text
- [ ] solution_summary
- [ ] domain
- [ ] subfield
- [ ] answer_type
- [ ] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
- [ ] problem_type
- [ ] solution_method_type
- [ ] structure_features
- [ ] key_objects
- [ ] thinking_patterns
- [ ] primary_pattern
- [ ] knowledge_required
- [ ] key_insight
- [ ] translation_from
- [ ] translation_to
- [ ] translation_type
- [ ] tell_topology（profile级）
- [ ] tell_small_concepts（profile级）
- [ ] expected_ai_method
- [ ] correct_method
- [ ] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [ ] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [ ] bare_ai_expected
- [ ] bare_ai_error_prediction
- [ ] suitable_for_poc
- [ ] discriminates_levels
- [ ] qa_sequence（含rounds数组和stats子对象）
- [ ] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件**

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329104"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1983p6"
   - extracted_by改为"subagent"

**示例代码**：
```python
from arango import ArangoClient
from datetime import datetime, timezone
import json

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
now = datetime.now(timezone.utc).isoformat()

# 读取profile.json
with open('profile.json', 'r') as f:
    profile = json.load(f)

# 写入problem_profiles
db.collection('problem_profiles').insert(profile, overwrite=True)

# 更新problem_extraction_progress
db.collection('problem_extraction_progress').update({
    '_key': '329104',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1983p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1983p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1983p6
- solution_method_type: method_translation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有拓扑分类（inequality_proof/direct_calculation/method_translation等）足够覆盖本题
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
