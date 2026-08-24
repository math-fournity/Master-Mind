# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1999p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1999P6.lean
- **来源**: IMO 1999 P6
- **ArangoDB progress记录_key**: 329170（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1999P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Determine all functions f : ℝ → ℝ such that f(x - f(y)) = f(f(y)) + x·f(y) + f(x) - 1 for all x, y ∈ ℝ.
- 解答核心思路（1-2句话）：令 c = f(0)，A = range(f)。对 A 中元素代入特殊值得到 f 在 A 上的二次表达式，再证明 c≠0 使得 f(x-c)-f(x) 可取任意值，从而任意实数是 A 中两元素之差，最终推出 f(x) = c - x²/2 并比较得 c=1。
- 解答关键步骤列表：
  1. 令 c = f(0)，A = Set.range f
  2. 对 a ∈ A（a = f(y)），令 x = a 代入：f(a - a) = f(a) + a² + f(a) - 1 → f(a) = (1+c)/2 - a²/2  （h1）
  3. 证明 c ≠ 0：若 c=0，令 y=0 得 f(x) = f(0) + 0 + f(x) - 1 → f(0) = 1，与 c=0 矛盾
  4. 由 y=0 得 f(x-c) - f(x) = xc + (f(c) - 1)，因 c≠0，xc + (f(c)-1) 可取任意实数值
  5. 故对任意 x，存在 x' 使 x'·c + (f(c)-1) = x，取 a = f(x'-c), b = f(x') ∈ A，则 x = a - b  （h2）
  6. 由 x = a - b 代入原方程：f(a-b) = f(b) + ab + f(a) - 1，结合 h1 得 f(x) = c - x²/2  （h11）
  7. 比较 h1（a=c 时）和 h11（x=c 时）：(1+c)/2 - c²/2 = c - c²/2 → c = 1
  8. 结论：f(x) = 1 - x²/2

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
| 1 | 纯元认知观察 | 0.8 | 观察这个函数方程 f(x - f(y)) = f(f(y)) + x·f(y) + f(x) - 1 的结构。方程中 f 出现在哪些位置？哪些变量是自由的，哪些被嵌套在 f 的内部？方程的左边和右边在结构上有什么不对称性？ | 方程中 f 出现在5个位置：f(x-f(y))、f(f(y))、f(y)（两次）、f(x)。x 是完全自由的，y 通过 f(y) 嵌套。左边是 f 在复合表达式 x-f(y) 处取值，右边是 f(f(y)) + x·f(y) + f(x) - 1 的线性组合。结构不对称性：左边只有一个 f 的求值（在复合点），右边有三个 f 的求值（在 f(y)、x、f(y) 处）加一个线性项 x·f(y)。 |
| 2 | 自由列举 | 0.7 | 对于这个函数方程，你能想到哪些可能的代入策略来提取信息？列出所有你能想到的特殊代入方式。 | 1) 令 y=0，利用 f(0)=c 简化；2) 令 x=0，得到 f(-f(y)) = f(f(y)) + f(0) - 1；3) 令 x=f(y)，使左边变成 f(0)；4) 令 x=f(y)+某值，使左边变成 f(某值)；5) 考虑 f 的值域 A=range(f)，对 a∈A 做代入；6) 假设 f 是多项式，尝试 f(x)=ax²+bx+c 的形式；7) 令 y 使得 f(y)=0（如果存在）。 |
| 3 | 小尝试 | 0.5 | 试试假设 f 是二次多项式 f(x) = ax² + bx + c，代入方程看看能否确定系数。这个方向可能走通也可能走不通。 | 代入 f(x)=ax²+bx+c：左边 = a(x-ay²-by-c)² + b(x-ay²-by-c) + c，右边 = a(ay²+by+c)² + b(ay²+by+c) + c + x(ay²+by+c) + ax²+bx+c - 1。比较 x² 项：左边 a，右边 a，一致。比较 x 的一次项（不含 y）：左边 -2a(ay²+by+c)x + bx，右边 (ay²+by+c)x + bx。需要 -2a = 1，即 a = -1/2。进一步比较常数项可得 b=0, c=1。所以 f(x) = 1 - x²/2 是候选解，但还需要证明这是唯一的解。 |
| 4 | 思维操作引导 | 0.4 | 多项式假设给出了候选解 f(x)=1-x²/2，但需要证明唯一性。执行以下操作：令 c=f(0)，A=range(f)。对任意 a∈A（即 a=f(y) 对某个 y），在原方程中令 x=a，推导 f(a) 用 c 和 a 表示的公式。 | 令 x=a=f(y)，则左边 f(a-a)=f(0)=c，右边 f(a)+a·a+f(a)-1 = 2f(a)+a²-1。所以 c = 2f(a)+a²-1，即 f(a) = (c+1-a²)/2 = (1+c)/2 - a²/2。这给出了 f 在值域 A 上的显式表达式。 |
| 5 | 思维操作引导 | 0.4 | 现在你有了 f 在 A 上的表达式。下一步需要把结论推广到所有实数。先证明 c≠0（用反证法：若 c=0 会怎样？），然后利用 y=0 时的方程分析 f(x-c)-f(x) 的结构。 | 若 c=0，令 y=0：f(x-0)=f(0)+x·0+f(x)-1 → f(x)=0+0+f(x)-1 → 0=-1，矛盾。故 c≠0。令 y=0：f(x-c)=f(c)+xc+f(x)-1，即 f(x-c)-f(x)=xc+(f(c)-1)。因 c≠0，当 x 遍历 ℝ 时，xc+(f(c)-1) 遍历 ℝ。 |
| 6 | 推进 | 0.5 | 既然 f(x-c)-f(x) 可以取任意实数值，利用这一点证明：对任意实数 t，存在 a,b∈A 使得 t=a-b。然后利用 x=a-b 的代入和步骤4的公式，推导 f 在所有实数上的表达式。 | 对任意 t，选 x' 使 x'c+(f(c)-1)=t，即 x'=(t-(f(c)-1))/c。令 a=f(x'-c)∈A, b=f(x')∈A，则 a-b = f(x'-c)-f(x') = x'c+(f(c)-1) = t。现在对 x=a-b 代入原方程：f(a-b)=f(b)+ab+f(a)-1。用 h1: f(a)=(1+c)/2-a²/2, f(b)=(1+c)/2-b²/2。代入计算：f(x)=(1+c)/2-b²/2+ab+(1+c)/2-a²/2-1 = c-(a-b)²/2 = c-x²/2。所以 f(x)=c-x²/2 对所有 x 成立。 |
| 7 | 推进 | 0.4 | 你已经得到 f(x)=c-x²/2 对所有实数成立。现在需要确定 c 的值。利用步骤4中 f 在 A 上的公式，取 a=c（因为 c=f(0)∈A），与 f(x)=c-x²/2 在 x=c 处比较。 | c=f(0)∈A，由 h1：f(c)=(1+c)/2-c²/2。由 f(x)=c-x²/2 在 x=c：f(c)=c-c²/2。比较：(1+c)/2-c²/2 = c-c²/2 → (1+c)/2 = c → 1+c = 2c → c=1。因此 f(x)=1-x²/2。验证：代入原方程可确认满足。 |
| 8 | 能量传递引导 | 0.7 | 回顾整个证明路径：从特殊代入提取信息 → 值域上的二次表达式 → c≠0 保证覆盖性 → 差分解覆盖全实数 → 比较确定 c=1。每一步都是前一步的自然延伸。现在用一句话总结这个函数方程的唯一解，并确认验证无误。 | f(x) = 1 - x²/2 是唯一满足 f(x-f(y))=f(f(y))+xf(y)+f(x)-1 的函数。验证：f(x-f(y))=1-(x-(1-y²/2))²/2，展开后等于 f(f(y))+xf(y)+f(x)-1。证明完整，逻辑链从特殊代入到全局覆盖再到参数确定，环环相扣。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 6（R1纯元认知观察, R2自由列举, R6推进, R7推进, R8能量传递引导, R3小尝试也算偏元认知但归小尝试）
- knowledge_rounds（思维操作引导的轮数）: 2（R4, R5）
- level_sum: 0.8+0.7+0.5+0.4+0.4+0.5+0.4+0.7 = 4.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4（需要知道对值域元素做特殊代入的技巧）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6（需要将"c≠0→f(x-c)-f(x)可取任意值→任意实数是A中两元素之差"这条逻辑链串联起来）

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
- problem_type: characterization（确定所有满足给定约束的函数，即刻画满足函数方程的全部函数）
- structure_features: 函数方程 f(x-f(y)) = f(f(y)) + x·f(y) + f(x) - 1，涉及 f 的多重嵌套（f(f(y))）、f 在复合点取值（f(x-f(y))）、以及线性项 x·f(y)。方程对 x 是线性的（x 只以一次出现），对 f(y) 也是线性的。核心结构是 f 在"自由变量减去值域元素"处的取值与 f 在值域元素处的取值之间的关系。
- key_objects: [函数 f: ℝ→ℝ, 值域 A=range(f), 常数 c=f(0), 二次函数 1-x²/2, 差分关系 f(x-c)-f(x)]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [特殊代入法（对值域元素和零点做代入）, 值域分析（利用range(f)的结构）, 反证法（证明c≠0）, 覆盖性论证（从局部到全局的推广）, 系数比较法（多项式假设）, 差分技巧（f(x-c)-f(x)的结构利用）]
- primary_pattern: 值域分析+覆盖性论证（从值域上的局部信息推广到全实数，是整个证明的主导思维模式）
- knowledge_required: [函数方程的基本代入技巧, 值域(range)的概念, 二次函数的性质, 反证法, 差分方程的概念]
- key_insight: 令 x=a（a∈range(f)）使左边变成 f(0)=c，从而在值域上得到 f 的二次表达式；再利用 c≠0 使 f(x-c)-f(x) 可取任意值，证明任意实数是值域中两元素之差，将局部结论推广到全局。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 多项式假设/系数比较（连续解析方法，假设f是多项式）
- translation_to: 值域分析+覆盖性论证（离散结构方法，利用range(f)的代数结构）
- translation_type: method_translation（从"假设函数形式直接求解"翻译到"利用值域结构间接推导"——前者只能给出候选解，后者才能证明唯一性）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: [值域代入, f(0)常数化, c≠0反证, 差分覆盖, 二次表达式比较]
- expected_ai_method: bare AI预期会尝试多项式假设或直接代入特殊值（如x=0, y=0），但停留在候选解阶段，无法证明唯一性——缺少从值域局部信息到全局覆盖的结构性转化
- correct_method: 值域分析+覆盖性论证——对range(f)中元素做特殊代入得到局部二次表达式，利用c≠0的差分结构证明任意实数是值域中两元素之差，从而推广到全局

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是。characterization已有，direct_manipulation已有，structural_transformation已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是。三个维度都在抽象/中等粒度上。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够。这道题的核心gap是从"局部值域信息"到"全局覆盖"的结构转化，structural_transformation准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。现有拓扑分类足够。

**拓扑进化建议**（如有）：无。现有分类体系完全适用。

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
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对复杂函数方程，尚未识别结构特征，不知道从哪里入手 | 观察方程结构，识别f的出现位置和变量自由度 | 0.8 | 纯元认知观察 | false | {characterization, direct_manipulation, method_problem_mismatch} | [f的多重嵌套, 变量自由度, 结构不对称性] |
| 2 | AI已识别结构但未列举代入策略，可能只想到一两种代入 | 列出所有可能的特殊代入方式 | 0.7 | 自由列举 | false | {characterization, enumeration_brute_force, search_space_estimation} | [y=0代入, x=0代入, x=f(y)代入, 值域元素代入, 多项式假设] |
| 3 | AI尝试多项式假设，得到候选解但卡在唯一性证明 | 假设f是二次多项式，代入方程确定系数 | 0.5 | 小尝试 | false | {characterization, algebraic_identity, method_problem_mismatch} | [二次多项式假设, 系数比较, 候选解, 唯一性缺口] |
| 4 | AI有候选解但不知道如何证明唯一性——缺少值域分析的知识 | 令c=f(0), A=range(f)，对a∈A令x=a代入，推导f在值域上的表达式 | 0.4 | 思维操作引导 | true | {characterization, direct_manipulation, knowledge_gap} | [值域定义, x=a代入, f(0)=c, 值域上二次表达式] |
| 5 | AI有值域上的局部表达式但不知道如何推广到全局——缺少c≠0和差分结构的知识 | 证明c≠0（反证法），利用y=0分析f(x-c)-f(x)的可取值范围 | 0.4 | 思维操作引导 | true | {characterization, direct_manipulation, knowledge_gap} | [c≠0反证, y=0代入, 差分结构f(x-c)-f(x), 线性覆盖] |
| 6 | AI知道c≠0和差分结构但未串联成覆盖性论证——思维瓶颈 | 利用差分可取任意值证明任意实数是A中两元素之差，再代入推导全局表达式 | 0.5 | 推进 | false | {characterization, logical_deduction, structural_transformation} | [差分覆盖, a-b分解, 全局推广, 二次表达式代入] |
| 7 | AI有f(x)=c-x²/2但未确定c的值 | 比较值域公式和全局公式在x=c处的值，解出c=1 | 0.4 | 推进 | false | {characterization, direct_calculation, method_problem_mismatch} | [c=f(0)∈A, 公式比较, 解方程c=1] |
| 8 | AI完成推导，需要确认和总结 | 回顾完整证明路径，总结唯一解并验证 | 0.7 | 能量传递引导 | false | {characterization, logical_deduction, method_problem_mismatch} | [证明路径回顾, 唯一解确认, 验证] |

**全局pairs详情**：

1. path_feature型：
- scope: "完整证明路径R1→R8"
- observation_point: null
- tell: 整个证明的核心路径特征是"局部→全局"的推广结构：先在值域A上得到f的二次表达式（局部），再通过c≠0的差分覆盖性证明任意实数是A中两元素之差（桥梁），最后将局部公式推广到全实数并确定参数c=1（全局）。这条路径的关键转折在于识别"值域元素的特殊代入"和"差分覆盖"两个操作。
- hint: 在处理函数方程唯一性证明时，优先考虑值域结构分析：先在range(f)上建立局部公式，再寻找从局部到全局的覆盖性桥梁
- hint_level: 0.6
- generalizability: "high——适用于所有涉及值域结构的函数方程唯一性证明，特别是当直接代入只能给出候选解时"
- why_not_visible_locally: "在局部视角中，每一步看起来都是独立的代入和推导——R4的值域代入、R5的c≠0证明、R6的覆盖论证各自独立。只有从完整路径回看，才能看到'局部值域信息→覆盖桥梁→全局推广'这个三段式结构是一个统一的证明范式。局部视角下AI不会意识到R4的值域表达式和R5的差分结构是为了R6的覆盖论证做准备的。"
- tell_topology: {characterization, direct_manipulation, structural_transformation}
- tell_small_concepts: [值域局部公式, 差分覆盖桥梁, 全局推广, 三段式证明范式]

2. implicit型：
- scope: "R3多项式假设与R4-R7严格证明之间的关系"
- observation_point: "R3"
- tell: R3的多项式假设虽然给出了正确候选解f(x)=1-x²/2，但这只是一个"猜对答案"的步骤——它隐含了一个更深层的信号：二次函数的结构暗示了f在值域上的二次行为，但多项式假设本身无法证明唯一性。真正的证明需要放弃"假设函数形式"的路线，转而"从方程结构推导函数形式"。这个蕴含信息在R3局部是不可见的。
- hint: 多项式假设是发现候选解的工具，但不是证明工具。当多项式假设给出候选解后，需要切换到值域分析来证明唯一性——从"假设形式"到"推导形式"的方法论转换
- hint_level: 0.7
- generalizability: "medium——适用于所有'先猜后证'的函数方程问题，但具体切换点取决于问题结构"
- why_not_visible_locally: "在R3局部，AI只看到'多项式假设成功给出了候选解'，会自然认为这条路可以走到底。AI不会意识到多项式假设的真正价值是提供候选解的方向指引，而非证明工具。只有当AI在R3之后尝试用多项式假设证明唯一性并失败时，才会隐约感到需要换方法——但这个'失败'信号在R3局部尚未出现。"
- tell_topology: {characterization, algebraic_identity, method_translation}
- tell_small_concepts: [多项式假设, 候选解vs唯一性, 方法论转换, 猜后证范式]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI大概率能通过多项式假设猜出f(x)=1-x²/2作为候选解，但会卡在唯一性证明上。AI可能尝试：1) 直接验证候选解满足方程后声称完成（遗漏唯一性）；2) 尝试更多特殊代入但无法串联成覆盖性论证；3) 尝试假设f是连续/可微来缩小范围，但题目无此条件。核心错误是缺少"值域分析+差分覆盖"这条从局部到全局的结构性转化路径。
- suitable_for_poc: ["POC-VMS-8脉络继承验证（hint端：给AI值域分析的脉络提示，看能否从候选解推进到完整证明）", "POC-VMS-9/10 tell端验证（从AI的thinking中识别'卡在唯一性证明'的tell信号）", "bare vs tree对照实验（bare AI只能猜答案，tree AI通过脉络注入值域分析方法完成完整证明）"]
- discriminates_levels: true（这道题能清晰区分"会猜答案"和"会证明唯一性"两个能力层级）

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

**产出**：profile.json已写入 `subagents-dirs/compfiles_imo1999p6/profile.json`，包含全部字段（_key, source_id, source_dataset, schema_version, problem_text, solution_text, solution_summary, domain, subfield, answer_type, answer, problem_type, solution_method_type, structure_features, key_objects, thinking_patterns, primary_pattern, knowledge_required, key_insight, translation_from, translation_to, translation_type, tell_topology, tell_small_concepts, expected_ai_method, correct_method, tell_hint_pairs(8个), global_tell_hint_pairs(2个), bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels, qa_sequence, analysis_metadata）。

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
2. 更新`problem_extraction_progress`集合中`_key="329170"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1999p6"
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
    '_key': '329170',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1999p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1999p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
  - problem_profiles/compfiles_imo1999p6 已写入
  - 8 local pairs, 2 global pairs 验证通过
  - per-pair tell_topology 存在
  - global pairs why_not_visible_locally 非None
  - answer 字段非None
  - progress记录 _key=329170 已更新为 completed

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1999p6
- solution_method_type: range_analysis_and_coverage_argument
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有分类体系（characterization / direct_manipulation / structural_transformation等）完全适用，粒度一致。
- 是否遇到异常: 否。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
