# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1976p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1976P6.lean
- **来源**: IMO 1976 P6
- **ArangoDB progress记录_key**: 329080（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1976P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：数列 u_0, u_1, u_2, ... 定义为 u_0 = 2, u_1 = 5/2, u_{n+1} = u_n(u_{n-1}^2 - 2) - u_1 (n ≥ 1)。证明对所有正整数 n，⌊u_n⌋ = 2^((2^n - (-1)^n)/3)，其中 ⌊x⌋ 为下取整函数。
- 解答核心思路（1-2句话）：猜测闭式 u_n = 2^α + 2^(-α)（α = (2^n - (-1)^n)/3），用二步归纳法验证递推关系，再证明 α 为整数且 2^(-α) ∈ (0,1) 从而取整后恰好等于 2^α。
- 解答关键步骤列表：
  1. 构造闭式假设：u_n = 2^((2^n - (-1)^n)/3) + 2^((-2^n + (-1)^n)/3)，即 a + a^(-1) 形式，其中 a = 2^α
  2. 用 Nat.twoStepInduction（二步归纳）验证闭式满足递推关系：利用恒等式 (x + x^(-1))^2 - 2 = x^2 + x^(-2) 化简递推
  3. 分奇偶讨论（Nat.even_or_odd）完成归纳步骤的代数验证
  4. 证明 (2^n - (-1)^n)/3 为整数：利用 sub_dvd_pow_sub_pow（3 | 2^n - (-1)^n）
  5. 证明 2^(-α) ∈ (0,1)（对正 n），因此 ⌊u_n⌋ = ⌊2^α + 2^(-α)⌋ = 2^α（因为 2^α 是整数且 0 < 2^(-α) < 1）

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
| 1 | 纯元认知观察 | 0.7 | 观察这道题的结构：已知什么（递推定义、初始值），要证什么（下取整等于2的幂），递推关系有什么特点（非线性、含u_n和u_{n-1}的交叉项）？ | 题目给出二阶非线性递推 u_{n+1} = u_n(u_{n-1}^2 - 2) - u_1，初始值 u_0=2, u_1=5/2。要证 ⌊u_n⌋ = 2^((2^n - (-1)^n)/3)。递推是非线性的，目标公式涉及2的幂和(-1)^n的奇偶交替，结构上像是一个闭式公式。 |
| 2 | 自由列举 | 0.8 | 列出你能想到的所有可能攻克方向：直接对floor做归纳？找闭式？计算前几项猜模式？变换递推？利用a+1/a型恒等式？ | 方向包括：(a)直接对⌊u_n⌋公式做归纳；(b)先求u_n的闭式再取整；(c)计算u_0,u_1,u_2,u_3猜模式；(d)观察递推中u_{n-1}^2-2的结构联想到x^2+x^{-2}；(e)设u_n = a_n + a_n^{-1}尝试分离变量；(f)利用生成函数或其他变换。 |
| 3 | 小尝试 | 0.3 | 试着直接对⌊u_n⌋ = 2^((2^n-(-1)^n)/3)做归纳——从u_n和u_{n-1}的floor能推出u_{n+1}的floor吗？ | 直接对floor归纳行不通：递推是非线性的 u_{n+1} = u_n(u_{n-1}^2 - 2) - u_1，从⌊u_n⌋和⌊u_{n-1}⌋无法还原u_n和u_{n-1}的小数部分，非线性运算后取整的关系无法控制。需要先找到u_n本身的闭式。 |
| 4 | 思维操作引导 | 0.2 | 计算前几项：u_0=2, u_1=5/2, u_2=?, u_3=?，然后对照目标公式 2^((2^n-(-1)^n)/3) 的值，看u_n和目标之间差多少。 | u_2 = (5/2)(4-2) - 5/2 = 5/2 - 5/2... 等等，u_2 = u_1(u_0^2-2) - u_1 = (5/2)(4-2) - 5/2 = 5 - 5/2 = 5/2。目标2^((4-1)/3)=2^1=2。⌊5/2⌋=2✓。u_3 = u_2(u_1^2-2) - u_1 = (5/2)(25/4-2) - 5/2 = (5/2)(17/4) - 5/2 = 85/8 - 20/8 = 65/8。目标2^((8+1)/3)=2^3=8。⌊65/8⌋=8✓。注意u_n - 2^α = 5/2-2=1/2, 65/8-8=1/8，小数部分恰好是2^(-α)。 |
| 5 | 思维操作引导 | 0.4 | 注意u_n = 2^α + (小数部分)，且小数部分 = 2^(-α)。这提示u_n = 2^α + 2^(-α) = a + 1/a形式。请验证：设α_n = (2^n-(-1)^n)/3，u_n = 2^{α_n} + 2^{-α_n}，检查初始值是否满足，然后思考递推为什么成立。 | u_0 = 2^0 + 2^0 = 2 ✓（α_0=(1-1)/3=0）。u_1 = 2^{1/3} + 2^{-1/3}... 等等，α_1=(2+1)/3=1，所以u_1 = 2^1 + 2^{-1} = 2 + 1/2 = 5/2 ✓。闭式 u_n = 2^{α_n} + 2^{-α_n} 对初始值成立。递推方面，关键是(x+x^{-1})^2 - 2 = x^2 + x^{-2}，所以u_{n-1}^2 - 2 = 2^{2α_{n-1}} + 2^{-2α_{n-1}}，然后u_n(u_{n-1}^2-2) = (2^{α_n}+2^{-α_n})(2^{2α_{n-1}}+2^{-2α_{n-1}})，需要验证这减去u_1后等于2^{α_{n+1}}+2^{-α_{n+1}}。 |
| 6 | 推进 | 0.5 | 继续验证递推：展开u_n(u_{n-1}^2-2) = (2^{α_n}+2^{-α_n})(2^{2α_{n-1}}+2^{-2α_{n-1}})，利用α_n + 2α_{n-1} = α_{n+1} + α_1（需要验证这个指数关系），完成归纳步骤。 | 展开得4项：2^{α_n+2α_{n-1}} + 2^{α_n-2α_{n-1}} + 2^{-α_n+2α_{n-1}} + 2^{-α_n-2α_{n-1}}。需要验证指数关系：α_{n+1} = α_n + 2α_{n-1} - α_1（因为要减去u_1 = 2^{α_1}+2^{-α_1}）。验证：α_n + 2α_{n-1} = (2^n-(-1)^n)/3 + 2(2^{n-1}-(-1)^{n-1})/3 = (2^n + 2^n - (-1)^n - 2(-1)^{n-1})/3 = (2^{n+1} - (-1)^n + 2(-1)^n)/3 = (2^{n+1} + (-1)^n)/3 = (2^{n+1} - (-1)^{n+1})/3 = α_{n+1}。所以α_n + 2α_{n-1} = α_{n+1}，减去α_1后主项为2^{α_{n+1}}，交叉项配对为2^{-α_{n+1}}。归纳成立。 |
| 7 | 能量传递引导 | 0.6 | 闭式已验证。最后一步：证明⌊u_n⌋ = 2^{α_n}。需要两件事：(1) α_n是整数（这样2^{α_n}是整数），(2) 2^{-α_n} ∈ (0,1)（这样小数部分不影响取整）。这两步都不难，你有信心完成。 | (1) α_n = (2^n - (-1)^n)/3是整数：因为2 ≡ -1 (mod 3)，所以2^n ≡ (-1)^n (mod 3)，即3 | (2^n - (-1)^n)。(2) 对正n，α_n > 0（因为2^n > 1 ≥ (-1)^n），所以-α_n < 0，2^{-α_n} ∈ (0,1)。因此⌊u_n⌋ = ⌊2^{α_n} + 2^{-α_n}⌋ = 2^{α_n}（整数加一个(0,1)的小数，取整后为整数部分）。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R6+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R5）
- level_sum: 0.7+0.8+0.3+0.2+0.4+0.5+0.6 = 3.5
- knowledge_bottleneck: R5（关键的a+1/a闭式猜测是知识瓶颈——需要知道x+x^{-1}型序列的恒等式）
- thinking_bottleneck: R6（指数关系的验证是思维瓶颈——需要正确展开和配对指数项）

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
- problem_type: characterization（证明递推数列的下取整等于特定闭式公式，本质是刻画数列的整数部分）
- structure_features: 二阶非线性递推关系（u_{n+1} = u_n(u_{n-1}^2 - 2) - u_1），目标为下取整等于2的幂次闭式。递推中u_{n-1}^2 - 2的结构暗示x^2 + x^{-2}恒等式。目标公式中(2^n - (-1)^n)/3的奇偶交替模式是关键结构特征。
- key_objects: ["递推数列 u_n", "下取整函数 ⌊·⌋", "闭式 2^((2^n-(-1)^n)/3)", "a + 1/a 型恒等式 (x+x^{-1})^2 - 2 = x^2 + x^{-2}", "指数关系 α_n + 2α_{n-1} = α_{n+1}"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["pattern_recognition（计算前几项识别模式）", "ansatz_construction（猜测a+1/a型闭式）", "algebraic_identity_verification（用恒等式验证递推）", "bounding_argument（证明修正项在(0,1)内完成取整）"]
- primary_pattern: ansatz_construction（主导思维模式是构造闭式假设——从计算前几项到猜测a+1/a形式，这是整个证明的核心转折）
- knowledge_required: ["二阶递推数列", "下取整函数性质", "数学归纳法（二步归纳）", "a + 1/a型代数恒等式 (x+x^{-1})^2 - 2 = x^2 + x^{-2}", "模运算与整除性（3 | 2^n - (-1)^n）", "指数运算与幂的性质"]
- key_insight: 猜测u_n = 2^α + 2^(-α)（a + 1/a形式），将非线性递推验证转化为指数关系的代数恒等式验证，其中(x+x^{-1})^2 - 2 = x^2 + x^{-2}是使递推成立的关键恒等式

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 非线性递推+下取整的直接归纳（对floor公式直接做归纳，受困于非线性递推和取整的不可交换性）
- translation_to: 闭式ansatz a + 1/a + 代数恒等式验证 + 修正项界定（先求u_n的精确闭式，验证递推，再利用修正项的界完成取整）
- translation_type: structural_transformation（将"对floor直接归纳"的结构转化为"先求闭式再取整"的结构，问题被完全重构）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["非线性递推", "下取整", "闭式公式", "a + 1/a 恒等式", "二步归纳", "指数关系验证", "整除性 3 | 2^n - (-1)^n"]
- expected_ai_method: bare AI预期会尝试直接对floor公式做归纳，或计算前几项后无法识别a+1/a模式，卡在非线性递推的复杂性上
- correct_method: 猜测闭式u_n = 2^α + 2^(-α)，利用(x+x^{-1})^2-2 = x^2+x^{-2}恒等式将递推验证转化为指数关系验证，再证明α为整数且2^(-α)∈(0,1)完成取整

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。problem_type=characterization（已有），ai_method_type=direct_calculation（已有，bare AI会尝试直接计算/归纳），gap_type=structural_transformation（已有，需要从直接归纳重构为闭式ansatz）
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。三个维度都用了已有值，粒度匹配。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。per-pair拓扑可以用不同的ai_method_type和gap_type区分不同轮次的tell。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，已有分类体系足够。

**拓扑进化建议**（如有）：无。已有拓扑分类体系完全够用。

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
- `why_not_visible_locally`: 蕴含型专用——为什么在局部不可见
- `tell_topology`: object（**⚠️ 每个全局pair也要有**）
- `tell_small_concepts`: array[string]（**⚠️ 每个全局pair也要有**）

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

### 局部tell_hint_pairs详情：

**R1** (纯元认知观察, level=0.7):
- tell: "AI面对非线性递推+下取整的混合结构，识别出递推和目标但未识别出a+1/a模式"
- hint: "描述题目结构：递推是非线性的，目标是2的幂次闭式，思考闭式可能的形式"
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["非线性递推", "下取整", "2的幂次闭式"]

**R2** (自由列举, level=0.8):
- tell: "AI列举了多个方向但未将a+1/a恒等式方向优先级排高"
- hint: "列出所有可能方向，特别注意递推中u_{n-1}^2-2的结构"
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: "characterization", ai_method_type: "enumeration_brute_force", gap_type: "search_space_estimation"}
- tell_small_concepts: ["方向列举", "u_{n-1}^2-2结构", "a+1/a恒等式方向"]

**R3** (小尝试, level=0.3):
- tell: "AI尝试直接对floor做归纳，发现非线性递推使小数部分不可控"
- hint: "试直接对floor公式做归纳，观察为什么行不通"
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["直接归纳", "floor不可交换", "小数部分不可控"]

**R4** (思维操作引导, level=0.2):
- tell: "AI计算前几项后发现u_n与目标之差恰好是2^(-α)，但未主动形成a+1/a假设"
- hint: "计算u_0到u_3，对照目标公式，观察差值的模式"
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: "characterization", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["前几项计算", "差值模式", "2^(-α)小数部分"]

**R5** (思维操作引导, level=0.4):
- tell: "AI看到差值=2^(-α)但未联想到a+1/a型闭式，缺少(x+x^{-1})^2-2=x^2+x^{-2}的恒等式知识"
- hint: "注意差值恰好是2^(-α)，提示u_n = 2^α + 2^(-α) = a + 1/a形式，验证初始值"
- is_knowledge_bottleneck: true
- tell_topology: {problem_type: "characterization", ai_method_type: "algebraic_identity", gap_type: "knowledge_gap"}
- tell_small_concepts: ["a+1/a闭式", "x^2+x^{-2}恒等式", "初始值验证"]

**R6** (推进, level=0.5):
- tell: "AI有闭式假设但展开递推后无法正确配对指数项，卡在指数关系的验证"
- hint: "展开u_n(u_{n-1}^2-2)的4项，验证α_n + 2α_{n-1} = α_{n+1}的指数关系"
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: "characterization", ai_method_type: "algebraic_identity", gap_type: "method_translation"}
- tell_small_concepts: ["指数展开", "4项配对", "α_n + 2α_{n-1} = α_{n+1}"]

**R7** (能量传递引导, level=0.6):
- tell: "AI有闭式但需要完成取整论证——需要证明α是整数和2^(-α)∈(0,1)"
- hint: "证明α_n是整数（3 | 2^n - (-1)^n）和2^(-α)∈(0,1)，完成取整"
- is_knowledge_bottleneck: false
- tell_topology: {problem_type: "characterization", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"}
- tell_small_concepts: ["整除性", "3 | 2^n - (-1)^n", "取整论证"]

### 全局tell_hint_pairs详情：

**G1** (path_feature):
- scope: "从题目到闭式猜测的完整路径"
- observation_point: null
- tell: "非线性递推u_{n+1}=u_n(u_{n-1}^2-2)-u_1的结构中隐藏了a+1/a型闭式，bare AI不会主动联想到"
- hint: "观察u_{n-1}^2-2的结构，联想(x+x^{-1})^2-2=x^2+x^{-2}，猜测u_n=a_n+a_n^{-1}型闭式"
- hint_level: 0.7
- generalizability: "high — a+1/a型闭式是非线性递推的通用技巧，适用于类似结构的递推问题"
- why_not_visible_locally: null
- tell_topology: {problem_type: "characterization", ai_method_type: "algebraic_identity", gap_type: "structural_transformation"}
- tell_small_concepts: ["a+1/a闭式", "x^2+x^{-2}恒等式", "非线性递推结构"]

**G2** (implicit):
- scope: "取整论证中的整除性"
- observation_point: "R7"
- tell: "取整论证需要α_n=(2^n-(-1)^n)/3是整数，这个整除性隐藏在公式中"
- hint: "利用2≡-1 (mod 3)证明3 | (2^n-(-1)^n)，这是标准数论工具"
- hint_level: 0.5
- generalizability: "medium — 模幂的整除性是标准数论工具，但需要在此处主动调用"
- why_not_visible_locally: "整除性在闭式验证阶段不可见，只有在取整阶段才需要α为整数，是跨步骤的蕴含关系"
- tell_topology: {problem_type: "characterization", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"}
- tell_small_concepts: ["整除性", "2≡-1 (mod 3)", "取整论证"]

**G3** (path_feature):
- scope: "归纳验证步骤中的指数关系"
- observation_point: null
- tell: "展开递推后4个指数项需要配对，关键关系α_n + 2α_{n-1} = α_{n+1}不是显然的"
- hint: "验证α_n + 2α_{n-1} = (2^n-(-1)^n)/3 + 2(2^{n-1}-(-1)^{n-1})/3 = (2^{n+1}-(-1)^{n+1})/3 = α_{n+1}"
- hint_level: 0.4
- generalizability: "high — 指数关系的代数验证是递推闭式证明的通用步骤"
- why_not_visible_locally: null
- tell_topology: {problem_type: "characterization", ai_method_type: "algebraic_identity", gap_type: "method_translation"}
- tell_small_concepts: ["指数关系", "α_n + 2α_{n-1} = α_{n+1}", "4项配对"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "bare AI会尝试直接对floor公式做归纳，受困于非线性递推和取整的不可交换性。即使计算前几项，也大概率无法识别a+1/a模式——这需要知道(x+x^{-1})^2-2=x^2+x^{-2}这个特定恒等式。AI可能在计算前几项后给出部分正确但无法推广的观察，或尝试错误的闭式形式。"
- suitable_for_poc: ["tell_detection_poc（R5的a+1/a知识瓶颈是典型tell检测场景）", "hint_injection_poc（注入a+1/a方向后验证AI能否完成剩余步骤）", "level_discrimination_poc（R3小尝试vs R5知识瓶颈区分不同能力层级）"]
- discriminates_levels: true

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
- [x] answer
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

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 `subagents-dirs/compfiles_imo1976p6/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="329080"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1976p6"
   - extracted_by改为"subagent"

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: Verification passed: compfiles_imo1976p6, 7 local pairs, 3 global pairs

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1976p6
- solution_method_type: closed_form_ansatz_with_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3（2个path_feature + 1个implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类体系完全够用。problem_type=characterization、ai_method_type用了direct_calculation/enumeration_brute_force/algebraic_identity/logical_deduction、gap_type用了method_problem_mismatch/search_space_estimation/structural_transformation/knowledge_gap/method_translation，全部为已有值，粒度一致。
- 是否遇到异常: 否，全流程顺利完成

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
