# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003816
- **文件路径**: subagents-dirs/omni_math_003816/problem.lean
- **来源**: AoPS omni_math (imo)
- **ArangoDB progress记录_key**: 333695（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003816/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：求所有函数 f: ℝ→ℝ 使得 (f(x)+f(z))(f(y)+f(t)) = f(xy-zt) + f(xt+yz) 对所有实数 x,y,z,t 成立。
- 解答核心思路（1-2句话）：先代入特殊值确定 f(0)=0 或 1/2；f(0)=1/2 时推出 f≡1/2；f(0)=0 时推出 f 是积性的且偶的，再通过 x=z 代换将原方程化为平行四边形法则 f(y+t)+f(y-t)=2f(y)+2f(t)，结合积性推出 f(x)=x² 或 f≡0。
- 解答关键步骤列表：
  1. 令 x=y=z=t=0：(2f(0))²=2f(0) → f(0)=0 或 f(0)=1/2
  2. 令 z=t=0：(f(x)+f(0))(f(y)+f(0))=f(xy)+f(0)
  3. f(0)=1/2 情形：(f(x)+1/2)(f(y)+1/2)=f(xy)+1/2，令 y=0 推出 f(x)=1/2 常数
  4. f(0)=0 情形：f(x)f(y)=f(xy)（积性），令 x=y=0 推出 f(-zt)=f(zt)（偶性）
  5. 令 x=z：(2f(x))(f(y)+f(t))=f(x(y-t))+f(x(y+t))=f(x)(f(y-t)+f(y+t))，若 f≢0 则 2(f(y)+f(t))=f(y-t)+f(y+t)（平行四边形法则）
  6. 积性+平行四边形法则 → f(1)=0 或 1；f(1)=0 → f≡0；f(1)=1 → f(x)=x²
  7. 验证三个解 f≡0, f≡1/2, f(x)=x² 均满足原方程（Brahmagupta-Fibonacci恒等式）

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
| 1 | 纯元认知观察 | 0.3 | 观察这个函数方程 (f(x)+f(z))(f(y)+f(t))=f(xy-zt)+f(xt+yz)，描述它的结构特征：左边是什么形式？右边是什么形式？有哪些自由变量？ | 左边是两个关于f的线性组合的乘积，形如 (f(·)+f(·))(f(·)+f(·))；右边是 f 在两个线性组合 xy-zt 和 xt+yz 上的求和。四个自由变量 x,y,z,t。右边的 xy-zt 和 xt+yz 看起来像复数乘法 (x+zi)(y+ti) 的实部和虚部，或像行列式/二次型的结构。 |
| 2 | 自由列举 | 0.5 | 对于这种多变量函数方程，列出你能想到的所有可能入手方向。 | 1) 代入特殊值（令某些变量为0）简化方程；2) 尝试常数函数 f(x)=c；3) 尝试幂函数 f(x)=x²；4) 观察右端 xy-zt 和 xt+yz 的代数结构（复数乘法）；5) 先确定 f(0) 的值；6) 尝试证明 f 的积性或加性。 |
| 3 | 小尝试 | 0.2 | 先试试常数函数 f(x)=c 能否满足方程，看看能得到什么。 | 代入 f(x)=c：左边 (c+c)(c+c)=4c²，右边 c+c=2c。所以 4c²=2c，即 c(2c-1)=0，得 c=0 或 c=1/2。所以 f≡0 和 f≡1/2 都是解。 |
| 4 | 思维操作引导 | 0.4 | 现在执行"令所有变量为0"这个操作来确定 f(0) 的可能值，然后根据 f(0) 的值分情况讨论。 | 令 x=y=z=t=0：(2f(0))²=2f(0)，即 2f(0)(2f(0)-1)=0，所以 f(0)=0 或 f(0)=1/2。分两种情况：Case 1: f(0)=1/2；Case 2: f(0)=0。 |
| 5 | 推进 | 0.5 | 在 f(0)=0 的情况下，令 z=t=0 看看能得到什么性质，然后继续推导。 | 令 z=t=0：(f(x)+f(0))(f(y)+f(0))=f(xy)+f(0)，即 f(x)f(y)=f(xy)，所以 f 是积性的。再令 x=y=0：f(z)f(t)=f(-zt)，结合积性得 f(-zt)=f(zt)，即 f 是偶函数。 |
| 6 | 思维操作引导 | 0.6 | 现在执行一个关键代换：令 x=z。观察方程两边如何简化，看看能否得到一个关于 f 的更简单的函数方程。 | 令 x=z：左边 (f(x)+f(x))(f(y)+f(t))=2f(x)(f(y)+f(t))；右边 f(xy-xt)+f(xt+xy)=f(x(y-t))+f(x(y+t))=f(x)f(y-t)+f(x)f(y+t)（用积性）=f(x)(f(y-t)+f(y+t))。若 f≢0，两边约去 f(x)：2(f(y)+f(t))=f(y-t)+f(y+t)，即平行四边形法则 f(y+t)+f(y-t)=2f(y)+2f(t)。 |
| 7 | 推进 | 0.5 | 你已经得到了 f 是积性的、偶的，且满足平行四边形法则。现在用这些性质来确定 f 的具体形式。 | 积性 → f(1)²=f(1)，所以 f(1)=0 或 1。若 f(1)=0，则 f(x)=f(x·1)=f(x)f(1)=0，即 f≡0。若 f(1)=1，由平行四边形法则和积性可推出 f(x)=x²（先证有理数，再由积性和偶性扩展到实数）。最终三个解：f≡0, f≡1/2, f(x)=x²。 |
| 8 | 能量传递引导 | 0.7 | 你已经找到了所有候选解，最后一步是验证它们确实满足原方程。f(x)=x² 的验证用到了什么经典恒等式？完成验证收尾。 | f≡0 和 f≡1/2 已在前面验证。f(x)=x² 的验证：(x²+z²)(y²+t²)=(xy-zt)²+(xt+yz)²，这正是 Brahmagupta-Fibonacci 恒等式（复数乘法模长公式 |α|²|β|²=|αβ|²）。三个解全部验证通过。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5（R1纯元认知观察, R2自由列举, R5推进, R7推进, R8能量传递引导）
- knowledge_rounds（思维操作引导的轮数）: 2（R4, R6）
- level_sum: 0.3+0.5+0.2+0.4+0.5+0.6+0.5+0.7=3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"（平行四边形法则的识别是关键知识瓶颈——需要知道这是二次型的特征方程）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"（x=z 代换是关键思维转折——从四变量方程到二变量方程的降维操作）

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
- problem_type: `characterization`（求所有满足约束的函数——这是经典的"刻画"型问题）
- structure_features: 四变量函数方程，左端是 f 值的乘积结构 (f(x)+f(z))(f(y)+f(t))，右端是 f 在复数乘法实部/虚部上的求和。方程具有高度对称性，可通过特殊值代入逐步降维。关键代换 x=z 将四变量方程化为平行四边形法则（二次型特征方程）。
- key_objects: ["函数方程", "积性函数", "平行四边形法则（二次型特征方程）", "Brahmagupta-Fibonacci恒等式", "复数乘法结构"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["特殊值代入降维", "分情况讨论（f(0)=0 vs f(0)=1/2）", "代数恒等式识别（平行四边形法则）", "结构化约（四变量→二变量）", "积性+二次型性质综合", "验证解的完备性"]
- primary_pattern: "特殊值代入降维→结构化约→代数恒等式识别"（通过逐步代入特殊值降低方程复杂度，最终将四变量方程化约为已知的平行四边形法则）
- knowledge_required: ["函数方程基本技巧（特殊值代入）", "积性函数性质", "平行四边形法则/二次型特征方程", "Brahmagupta-Fibonacci恒等式（复数乘法模长）", "积性函数+平行四边形法则→f(x)=x²的推导"]
- key_insight: "令 x=z 是关键转折——这个代换将四变量方程化简为平行四边形法则 f(y+t)+f(y-t)=2f(y)+2f(t)，从而将问题从'解一个陌生的四变量函数方程'翻译为'识别一个已知的二次型特征方程'"

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: "陌生四变量函数方程（(f(x)+f(z))(f(y)+f(t))=f(xy-zt)+f(xt+yz)）"
- translation_to: "已知的二次型特征方程（平行四边形法则 f(y+t)+f(y-t)=2f(y)+2f(t)）+ 积性函数性质"
- translation_type: "structural_reduction"（通过特殊值代入和变量代换，将高维未知结构化约为低维已知结构——从四变量到二变量的降维翻译）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_manipulation", gap_type: "structural_transformation"}
- tell_small_concepts: ["特殊值代入", "f(0)分情况", "积性函数", "偶函数", "x=z代换", "平行四边形法则", "二次型特征方程", "Brahmagupta-Fibonacci恒等式"]
- expected_ai_method: "direct_manipulation"（bare AI预期会直接展开方程尝试代数操作，可能尝试各种代入但没有系统性的降维策略，容易在四变量的搜索空间中迷失）
- correct_method: "structural_reduction"（正确方法是通过特殊值代入逐步降维，再用关键代换 x=z 将方程化约为已知的平行四边形法则）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。characterization 已有，direct_manipulation 已有，structural_transformation 已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。三个值都是中等偏抽象的粒度，与已有体系一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心gap是"需要从四变量结构化约到二变量已知结构"，structural_transformation 准确描述了这个gap。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。现有拓扑分类体系可以很好地容纳这道题。

**拓扑进化建议**（如有）：无。现有分类体系足够。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对四变量函数方程，尚未识别关键代数结构（复数乘法） | 描述方程结构：左端什么形式？右端什么形式？有哪些自由变量？ | 0.3 | 纯元认知观察 | false | {characterization, direct_manipulation, method_problem_mismatch} | ["四变量函数方程", "乘积结构", "复数乘法实部虚部"] |
| 2 | AI列出多个方向但未优先排序，关键方向（特殊值代入降维）可能被淹没 | 列出所有可能入手方向 | 0.5 | 自由列举 | false | {characterization, enumeration_brute_force, search_space_estimation} | ["特殊值代入", "常数函数尝试", "幂函数尝试", "复数结构观察"] |
| 3 | AI尝试常数函数得到c=0或1/2，方向正确但不完整 | 试试常数函数f(x)=c | 0.2 | 小尝试 | false | {characterization, direct_calculation, method_problem_mismatch} | ["常数函数", "4c²=2c", "c=0或1/2"] |
| 4 | AI尚未系统使用特殊值代入确定f(0) | 令所有变量为0确定f(0)，然后分情况讨论 | 0.4 | 思维操作引导 | false | {characterization, direct_manipulation, structural_transformation} | ["f(0)确定", "分情况讨论", "2f(0)(2f(0)-1)=0"] |
| 5 | AI在f(0)=0情形下需要进一步代入推导性质 | 令z=t=0看能得到什么性质，继续推导 | 0.5 | 推进 | false | {characterization, direct_manipulation, structural_transformation} | ["积性函数", "偶函数", "z=t=0代入"] |
| 6 | AI有积性和偶性但未看出x=z代换能导出平行四边形法则——这是知识瓶颈（识别二次型特征方程）和思维瓶颈（选择x=z代换） | 执行关键代换x=z，观察两端如何简化 | 0.6 | 思维操作引导 | true | {characterization, algebraic_identity, knowledge_gap} | ["x=z代换", "平行四边形法则", "二次型特征方程", "降维"] |
| 7 | AI拥有积性、偶性、平行四边形法则但需综合推出f(x)=x² | 用这些性质确定f的具体形式 | 0.5 | 推进 | false | {characterization, logical_deduction, method_translation} | ["f(1)=0或1", "积性+平行四边形法则", "f(x)=x²"] |
| 8 | AI有候选解但未验证，尤其f(x)=x²需要Brahmagupta-Fibonacci恒等式 | 验证所有解，f(x)=x²用到什么经典恒等式？ | 0.7 | 能量传递引导 | true | {characterization, algebraic_identity, knowledge_gap} | ["Brahmagupta-Fibonacci恒等式", "复数乘法模长", "验证完备性"] |

**全局pairs详情**：

| # | scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | path_feature | 整个解题路径的降维策略 | null | 解题路径呈现渐进降维结构：4变量→f(0)分情况→积性+偶性→x=z代换得2变量平行四边形法则→确定f形式 | 函数方程求解中系统性的特殊值代入降维是核心策略——每步代入都应减少自由度或增加约束 | 0.6 | high - 降维策略适用于所有多变量函数方程 | 在任何单一步骤中只能看到当前的特殊值代入及其直接结果，看不到整个降维链条的累积效应——每一步看似简单的代入，其价值在于为下一步降维铺路，这种累积性只有从完整路径才能识别 | {characterization, direct_manipulation, structural_transformation} | ["渐进降维", "特殊值代入链", "自由度递减"] |
| 2 | implicit | 题目方程右端的代数结构 | R1 | 右端xy-zt和xt+yz是复数乘法(x+zi)(y+ti)的实部和虚部——这个隐含复数结构解释了为什么f(x)=x²是解 | 观察xy-zt和xt+yz的代数结构——它们是复数乘法的实部和虚部，暗示f(x)=x²的解和验证方向 | 0.7 | medium - 复数乘法结构识别适用于具有类似代数形式的函数方程 | 在局部步骤中xy-zt和xt+yz只是两个线性组合，看起来是普通代数表达式。只有联想到复数乘法(x+zi)(y+ti)=xy-zt+(xt+yz)i时才能识别隐含结构——这个联想需要跨领域知识连接，不在任何单个推导步骤中自然出现 | {characterization, algebraic_identity, knowledge_gap} | ["复数乘法结构", "Brahmagupta-Fibonacci恒等式", "实部虚部"] |
| 3 | implicit | 关键代换x=z的选择动机 | R6 | 选择x=z代换的隐含动机是它使左端变为2f(x)·(f(y)+f(t))，右端通过积性变为f(x)·(f(y-t)+f(y+t))，从而约去f(x)得到平行四边形法则 | 在选择代换时寻找能使方程两端都出现公因子的变量设置——x=z使左端出现2f(x)，右端通过积性也出现f(x)因子 | 0.65 | medium - '寻找公因子代换'策略适用于具有乘积结构的函数方程 | 在R6局部视角中'令x=z'看起来只是普通特殊值代入。但选择x=z而非其他代换的深层原因——让两端都出现可约去的公因子f(x)——这个结构性考量在局部步骤中不可见，需要同时掌握积性（来自R5）和对方程两端结构的全局分析 | {characterization, direct_manipulation, structural_transformation} | ["公因子代换", "x=z选择动机", "约去f(x)", "结构匹配"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "bare AI大概率能找到f≡0和f≡1/2（常数函数代入是直觉性的），但在f(0)=0情形下会卡住：能推出积性和偶性，但不会想到x=z这个关键代换。可能尝试其他代换（如x=y, y=t等）但无法得到平行四边形法则。也可能尝试直接猜f(x)=x²但不一定能严格证明。最终可能给出不完整的解集或无法完成证明。"
- suitable_for_poc: ["hint_injection_effectiveness", "tell_extraction_from_thinking", "knowledge_bottleneck_identification", "progressive_hint_chain"]
- discriminates_levels: true（这道题能区分：弱AI只能找到常数解；中等AI能推出积性但卡在代换；强AI能完成x=z代换并识别平行四边形法则）

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查，不能遗漏）**：
- [x] _key（=problem_id）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
- [x] problem_type
- [x] solution_method_type
- [x] structure_features
- [x] key_objects
- [x] thinking_patterns
- [x] primary_pattern
- [x] knowledge_required
- [x] key_insight
- [x] translation_from
- [x] translation_to
- [x] translation_type
- [x] tell_topology（profile级）
- [x] tell_small_concepts（profile级）
- [x] expected_ai_method
- [x] correct_method
- [x] tell_hint_pairs（每个pair含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（每个pair含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** ✅ 已写入，JSON验证通过

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
2. 更新`problem_extraction_progress`集合中`_key="333695"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003816"
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
    '_key': '333695',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003816',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003816')
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
- problem_id: omni_math_003816
- solution_method_type: structural_reduction
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 3（1 path_feature + 2 implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有分类体系（characterization / direct_manipulation / structural_transformation等）完全够用。
- 是否遇到异常: problem.lean中解答被截断（仅25行），基于数学知识完整重建了解答。其余流程正常。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
