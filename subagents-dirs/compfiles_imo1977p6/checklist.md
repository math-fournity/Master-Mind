# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1977p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1977P6.lean
- **来源**: IMO 1977 P6
- **ArangoDB progress记录_key**: 329085（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1977P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 f: ℕ+ → ℕ+ 满足对所有 n 有 f(f(n)) < f(n+1)。证明 f(n) = n 对所有 n 成立。
- 解答核心思路（1-2句话）：先对 f: ℕ → ℕ 证明更强的引理 ∀k n, k ≤ n → k ≤ f n（对 k 归纳），由此得 f(n) ≥ n 且 f 严格单调，再用单调性从 f(f(n)) < f(n+1) "消去" 外层 f 得 f(n) < n+1，夹逼得 f(n) = n。最后将结果从 ℕ 转移到 ℕ+。
- 解答关键步骤列表：
  1. 归约：先对 f: ℕ → ℕ 证明，再转移到 ℕ+
  2. 关键引理：∀ k n, k ≤ n → k ≤ f n，对 k 做归纳
     - k=0：平凡（0 ≤ 任意自然数）
     - k+1 ≤ n 时：由 IH 得 k ≤ f(f(n-1))，再用条件 f(f(n-1)) < f(n) 得 k+1 ≤ f(n)
  3. 由引理取 k=n 得 f(n) ≥ n
  4. 严格单调性：f(n) ≤ f(f(n))（由引理 k=f(n), n=f(n)）且 f(f(n)) < f(n+1)，故 f(n) < f(n+1)，f 严格递增
  5. 消去：严格单调意味着 f(a) < f(b) ⟺ a < b，故 f(f(n)) < f(n+1) 蕴含 f(n) < n+1，即 f(n) ≤ n
  6. 结合 f(n) ≥ n 与 f(n) ≤ n 得 f(n) = n
  7. 转移到 ℕ+：用嵌入 if 0 < m then f m.toPNat' else 0

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：f 是什么类型的映射？条件 f(f(n)) < f(n+1) 说了什么？目标是什么？条件中出现了什么嵌套结构？ | f: ℕ+→ℕ+ 是正整数上的函数。条件说对每个 n，f 在 f(n) 处的值小于 f 在 n+1 处的值。目标是证明 f 是恒等映射。关键结构：条件中出现了嵌套的 f(f(n))，不是简单的 f(n) < f(n+1)。 |
| 2 | 自由列举 | 0.7 | 列出你能想到的所有可能证明方向：直接对 n 归纳？计算前几项？证明 f 单调？证明 f(n) ≥ n？证明 f(n) ≤ n？还有别的吗？ | 方向包括：①直接对 n 归纳证明 f(n)=n；②计算 f(1), f(2),... 猜测模式；③先证 f 单调递增；④先证 f(n) ≥ n（下界）；⑤先证 f(n) ≤ n（上界）；⑥反证法假设存在 n 使 f(n)≠n；⑦考虑 f 的不动点。 |
| 3 | 小尝试 | 0.4 | 试试直接对 n 归纳：基例 n=1 时 f(f(1)) < f(2)，这能推出 f(1)=1 吗？归纳步中假设 f(k)=k，能推出 f(k+1)=k+1 吗？看看卡在哪里。 | n=1 时 f(f(1)) < f(2)，无法直接得 f(1)=1。归纳步假设 f(k)=k，则条件给 f(k) < f(k+1) 即 k < f(k+1)，但无法得到 f(k+1)=k+1。卡住的原因：条件涉及 f(f(n))，直接归纳无法利用这个嵌套结构。 |
| 4 | 思维操作引导 | 0.3 | 直接归纳失败是因为假设太弱。尝试证明一个更强的命题：∀ k n, k ≤ n → k ≤ f n（即 f(n) ≥ 任意不超过 n 的数）。对 k 做归纳，想想归纳步中条件 f(f(n-1)) < f(n) 如何帮到你。 | 对 k 归纳：k=0 平凡。归纳步设 k+1 ≤ n，需证 k+1 ≤ f(n)。由 IH（k ≤ f(n-1) 的某种应用）可得 k ≤ f(f(n-1))，再用条件 f(f(n-1)) < f(n) 得 k+1 ≤ f(n)。关键：IH 要灵活应用于不同 n 值。 |
| 5 | 推进 | 0.2 | 继续完成引理的归纳证明。具体写出：k+1 ≤ n 时，如何从 IH 得到 k ≤ f(f(n-1))？提示——IH 说 k ≤ m → k ≤ f(m)，你需要选合适的 m。 | 由 k ≤ n-1（因 k+1 ≤ n），IH 给 k ≤ f(n-1)。再对 m=f(n-1) 用 IH（需 k ≤ f(n-1) 已证），得 k ≤ f(f(n-1))。由条件 f(f(n-1)) < f(n)，故 k+1 ≤ f(n)。引理证毕。取 k=n 得 f(n) ≥ n。 |
| 6 | 思维操作引导 | 0.5 | 现在你有了 f(n) ≥ n。接下来需要两步：①证明 f 严格递增；②利用严格单调性从 f(f(n)) < f(n+1) 中"消去"外层 f。想想怎么做。 | ①由引理 k=f(n), n=f(n) 得 f(n) ≤ f(f(n))，结合 f(f(n)) < f(n+1) 得 f(n) < f(n+1)，故 f 严格递增。②严格递增意味着 f(a) < f(b) ⟺ a < b，故 f(f(n)) < f(n+1) 蕴含 f(n) < n+1，即 f(n) ≤ n。 |
| 7 | 能量传递引导 | 0.5 | 现在你同时有 f(n) ≥ n 和 f(n) ≤ n。收尾吧！另外，我们最初是在 ℕ+ 上，但证明用了 ℕ（含 0），这个差异怎么处理？ | 由 f(n) ≥ n 和 f(n) ≤ n 得 f(n) = n。对于 ℕ+ 到 ℕ 的差异：将 f 嵌入为 g: ℕ→ℕ，g(0)=0, g(m)=f(m) 当 m>0，在 ℕ 上证明 g(n)=n，再限制回 ℕ+ 即可。证毕！ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.8+0.7+0.4+0.3+0.2+0.5+0.5 = 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R6（知道严格单调可以"消去"嵌套函数是一个知识事实）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4（意识到需要证明更强的引理是关键思维转折）

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
- problem_type: characterization（证明满足条件的函数必为恒等映射——刻画问题）
- structure_features: 函数 f: ℕ+→ℕ+ 满足嵌套不等式 f(f(n)) < f(n+1)，需证明 f 是恒等映射。核心结构特征是条件中的嵌套函数应用 f(f(n))，使得直接归纳失效，需要通过更强的引理间接处理。
- key_objects: [函数 f, 正整数集 ℕ+, 嵌套函数应用 f(f(n)), 不等式关系, 恒等映射]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [强化归纳假设（证明比目标更强的引理）, 辅助性质推导（先证 f(n)≥n 再证单调性）, 单调性消去（用严格单调从嵌套不等式中消去外层函数）, 域归约（先证 ℕ 再转移到 ℕ+）]
- primary_pattern: 强化归纳假设（strengthening the induction hypothesis）
- knowledge_required: [自然数归纳法, 严格单调性及其与不等式的关系, 自然数上的序结构, 强化归纳假设技巧, 域嵌入转移技巧]
- key_insight: 证明更强的引理 ∀k n, k ≤ n → k ≤ f n（对 k 归纳），由此得 f(n) ≥ n 和严格单调性，再用单调性从 f(f(n)) < f(n+1) 中"消去"外层 f 得 f(n) < n+1，夹逼得 f(n) = n。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接对 n 归纳证明 f(n)=n（朴素方法，因条件含嵌套 f(f(n)) 而失效）
- translation_to: 强化为双变量引理 ∀k n, k ≤ n → k ≤ f n 的归纳证明 + 单调性消去（间接方法）
- translation_type: structural_transformation（将单变量直接归纳转化为双变量强化引理的归纳，再通过单调性消去完成翻译）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [嵌套函数应用, 强化归纳假设, 双变量引理, 严格单调性消去, 夹逼论证]
- expected_ai_method: bare AI 会尝试直接对 n 归纳证明 f(n)=n，因条件含嵌套 f(f(n)) 而在归纳步卡住，无法利用嵌套结构
- correct_method: 证明更强的双变量引理 ∀k n, k ≤ n → k ≤ f n（对 k 归纳），由此得 f(n) ≥ n 和严格单调性，再用单调性消去外层 f 得 f(n) ≤ n，夹逼得 f(n) = n

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
- [x] 当前拓扑分类是否够用——这道题的problem_type=characterization、ai_method_type=direct_calculation、gap_type=structural_transformation 均可归入已有拓扑类别，够用。
- [x] 粒度是否一致——characterization 与已有值粒度一致（抽象级），direct_calculation 与已有值一致（抽象级），structural_transformation 与已有值一致（中等级）。统一。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的 tell。problem_type 区分问题类型，ai_method_type 区分 AI 走错的方法，gap_type 区分差距性质。不需要新维度。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无进化建议。

**拓扑进化建议**（如有）：无。当前三维度拓扑分类体系足以处理此题。

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
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到函数不等式 f(f(n))<f(n+1) 和目标 f=id，但未识别嵌套结构导致的归纳困难 | 描述问题结构：f 的类型、条件的含义、嵌套应用 f(f(n)) | 0.8 | 纯元认知观察 | false | {characterization, direct_calculation, method_problem_mismatch} | [嵌套函数应用, 恒等映射目标, 函数不等式] |
| 2 | AI列举方向但可能未列出"强化引理"这一关键方向 | 列出所有可能方向：直接归纳、计算值、证单调、证上下界、反证 | 0.7 | 自由列举 | false | {characterization, enumeration_brute_force, search_space_estimation} | [直接归纳, 值计算, 单调性, 上下界, 反证法] |
| 3 | AI尝试直接归纳但在归纳步卡住——条件含 f(f(n)) 无法利用 | 试直接归纳，观察卡在归纳步的嵌套应用 | 0.4 | 小尝试 | false | {characterization, direct_calculation, method_problem_mismatch} | [直接归纳, 归纳步失效, 嵌套应用障碍] |
| 4 | AI卡在直接归纳，需要被引导到更强的双变量引理 | 证明更强命题 ∀k n, k≤n→k≤f n，对 k 归纳 | 0.3 | 思维操作引导 | false | {characterization, logical_deduction, structural_transformation} | [强化引理, 双变量归纳, 归纳假设强化] |
| 5 | AI需要完成引理归纳证明，在归纳步中灵活应用 IH | 完成归纳步：由 IH 得 k≤f(f(n-1))，再用条件推 k+1≤f(n) | 0.2 | 推进 | false | {characterization, logical_deduction, structural_transformation} | [归纳步, 条件应用, 不等式链] |
| 6 | AI有 f(n)≥n 但未看到如何得单调性并消去 f | 从 f(n)≥n 推严格单调，再用单调性消去外层 f | 0.5 | 思维操作引导 | true | {characterization, algebraic_identity, knowledge_gap} | [严格单调性, 函数消去, 不等式简化] |
| 7 | AI有 f(n)≥n 和 f(n)≤n，需要收尾并处理域差异 | 结合上下界得 f(n)=n，处理 ℕ 到 ℕ+ 的转移 | 0.5 | 能量传递引导 | false | {characterization, logical_deduction, knowledge_gap} | [夹逼论证, 域转移, 等式结论] |

**全局pairs详情**：

| scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|
| implicit | 整体证明策略 | R4 | 直接归纳因嵌套 f(f(n)) 失效，需要证明更强的双变量引理——这个需要只在直接尝试失败后才显现 | 当直接归纳因嵌套函数应用失效时，强化命题为双变量引理以获得更强的归纳假设 | 0.6 | high——强化归纳假设技巧广泛适用于归纳困难的场景 | 直接尝试失败后才显现的需要，是元策略而非单步可见的操作 | {characterization, direct_calculation, structural_transformation} | [强化归纳, 嵌套应用障碍, 双变量引理] |
| path_feature | R4-R7：从强化引理到单调性到消去的完整链路 | null | 解答遵循三阶段策略：建立下界→推导单调性→用单调性消去嵌套函数 | 面对 f(f(n))<g(n) 型不等式，先建立 f 的单调性，再用单调性消去外层 f | 0.7 | high——单调性消去模式适用于多种嵌套函数不等式 | null（路径特征型） | {characterization, logical_deduction, method_translation} | [下界建立, 单调性推导, 函数消去] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI 会尝试直接对 n 归纳证明 f(n)=n，在归纳步因条件含嵌套 f(f(n)) 而无法推进。AI 不会想到证明更强的双变量引理 ∀k n, k ≤ n → k ≤ f n，也不会意识到需要先建立 f(n) ≥ n 再推导单调性再用单调性消去。AI 可能在直接归纳失败后放弃或尝试无关方向。
- suitable_for_poc: ["tell端验证——分叉信号识别（AI在R3直接归纳失败后没走强化引理这条路，系统应在此分叉）", "hint端验证——脉络继承（给AI强化引理方向后能否完成后续证明）", "知识瓶颈验证——R6的单调性消去是否为纯知识瓶颈"]
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
2. 更新`problem_extraction_progress`集合中`_key="329085"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1977p6"
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
    '_key': '329085',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1977p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1977p6')
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
- problem_id: compfiles_imo1977p6
- solution_method_type: inductive_strengthening
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 implicit + 1 path_feature）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。当前三维度拓扑分类体系（problem_type/ai_method_type/gap_type）足以处理此题，所有标注值均归入已有类别，粒度一致。
- 是否遇到异常: 否

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
