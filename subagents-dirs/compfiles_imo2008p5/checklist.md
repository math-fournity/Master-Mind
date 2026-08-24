# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2008p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2008P5.lean
- **来源**: IMO 2008 P5
- **ArangoDB progress记录_key**: 329207（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2008P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let n and k be positive integers with k ≥ n and k - n even. 2n lamps labelled 1..2n, each on/off, initially all off. At each step one lamp is switched. N = number of k-step sequences resulting in lamps 1..n on, lamps n+1..2n off. M = number of k-step sequences with same final state but where none of lamps n+1..2n is ever switched on. Determine N/M.
- 解答核心思路（1-2句话）：构造从N-序列到M-序列的模n归约映射ψ，证明每个M-序列的纤维大小恰好为2^(k-n)，从而N = M·2^(k-n)。
- 解答关键步骤列表：
  1. 定义映射ψ：将N-序列中≥n的灯标号归约为mod n（映射到[0,n)），得到M-序列
  2. 证明ψ的像确实是M-序列：低灯的切换次数=原低灯(奇)+原高灯(偶)=奇，高灯从不被切换
  3. 关键引理claim：对每个M-序列f，|ψ^{-1}(f)| = 2^(k-n)
  4. 纤维计数：对每个低灯i，其在M-序列中被切换c_i次(奇数)，需决定哪些次切换"真正"指向i vs n+i。选择偶数个子集→2^(c_i-1)种方式
  5. 乘积：∏2^(c_i-1) = 2^(∑(c_i-1)) = 2^(k-n)，因为∑c_i = k且共n个灯
  6. 引理even_subsets_card：c元集合的偶数大小子集个数为2^(c-1)（通过对称差{a}的双射证明）
  7. 引理lemma1（计数引理）：若每个纤维大小为n，则|B|·n = |A|
  8. 最终：N = M · 2^(k-n)，即N/M = 2^(k-n)

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
| 1 | 纯元认知观察 | 0.3 | 请描述这道题的结构：N和M分别计数什么对象？它们之间的差异是什么？最终要求什么？ | N计数所有k步切换序列，最终状态为灯1..n开、灯n+1..2n关。M计数同样的序列但附加约束：灯n+1..2n从未被打开。差异在于M禁止切换高编号灯。最终要求N/M的比值。 |
| 2 | 自由列举 | 0.5 | 列出所有可能用来计算N/M的方法方向 | 1)分别直接计数N和M再求比；2)生成函数/母函数方法；3)构造N到M的映射并数纤维；4)容斥原理；5)递推/动态规划；6)对称性论证 |
| 3 | 小尝试 | 0.4 | 尝试直接分别计算N和M。N需要计数什么？状态空间有多大？ | N需要计数所有k步序列使得每个低灯被切换奇数次、每个高灯被切换偶数次。状态空间巨大：2n个灯，k步，每步2n种选择。直接计数需要处理复杂的奇偶约束，似乎很难得到闭式。M稍简单（只涉及n个灯）但也不容易。 |
| 4 | 思维操作引导 | 0.7 | 既然直接计数困难，考虑构造一个从N-序列到M-序列的映射。关键操作：如何把可能涉及高灯的N-序列"归约"为只涉及低灯的M-序列？ | 自然想法：将高灯标号n+i映射为低灯标号i（模n归约）。定义ψ(f)(j) = f(j) if f(j)<n, else f(j)-n。这样N-序列中切换高灯n+i的操作变成切换低灯i。需要验证：归约后低灯i的切换次数=原低灯i次数(奇)+原高灯n+i次数(偶)=奇数，满足M-序列条件。 |
| 5 | 思维操作引导 | 0.6 | ψ是满射。对每个M-序列f，ψ的纤维|ψ^{-1}(f)|有多大？关键：M-序列中低灯i被切换c_i次(奇数)，哪些次"真正"指向i vs n+i？ | 对每个低灯i，c_i次切换中需选一个奇数子集"真正"指向i，其余偶数子集指向n+i。等价于选一个偶数子集指向n+i。c_i元集合的偶数大小子集个数为2^(c_i-1)。所以纤维大小=∏2^(c_i-1)=2^(∑(c_i-1))=2^(k-n)，因为∑c_i=k且有n个灯。 |
| 6 | 推进 | 0.5 | 验证关键引理：c元集合的偶数大小子集个数为什么是2^(c-1)？ | 取一个元素a，对称差s△{a}将偶子集双射到奇子集。所以偶子集=奇子集=2^c/2=2^(c-1)。这是经典的对合论证。 |
| 7 | 能量传递引导 | 0.2 | 现在把所有部分组合起来：ψ是满射，每个纤维大小2^(k-n)，由计数引理N=M·2^(k-n)。写出最终答案。 | N/M = 2^(k-n)。完整论证：ψ将N-序列满射到M-序列，每个M-序列恰好有2^(k-n)个原像（由偶子集计数和奇偶约束），因此N = M·2^(k-n)。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

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
- problem_type: discrete_combinatorial
- structure_features: 两个集合的序列计数问题，带奇偶约束（低灯切换奇数次，高灯切换偶数次），求比值N/M。关键结构：N-序列允许切换高灯，M-序列禁止。模n归约将前者映射到后者。
- key_objects: ["lamp switching sequences", "parity constraints (odd/even switching counts)", "mod-n reduction map ψ", "fiber cardinality", "even subset counting 2^(c-1)", "counting lemma (uniform fiber implies |A|=|B|·n)"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["structural_mapping", "parity_argument", "fiber_counting", "power_of_2_counting", "involution_bijection"]
- primary_pattern: structural_mapping
- knowledge_required: ["parity of integers (odd+even=odd)", "even subset counting (2^(n-1) via symmetric difference involution)", "fiber/surjection counting lemma", "modular arithmetic reduction", "product-to-power-of-sum identity"]
- key_insight: 将N-序列通过模n归约映射到M-序列，每个M-序列的纤维大小恰好为2^(k-n)，因为对每个低灯i（切换c_i次，奇数），选择偶数子集指向高灯的方式数为2^(c_i-1)，乘积得2^(k-n)。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接分别计数N和M（枚举/生成函数方法）
- translation_to: 构造满射+均匀纤维计数（通过模n归约映射）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"}
- tell_small_concepts: ["parity constraint", "mod-n reduction", "fiber cardinality", "even subset counting", "2^(c-1)", "uniform fiber size", "ratio via surjection"]
- expected_ai_method: 尝试分别直接计数N和M，用生成函数或容斥处理奇偶约束，陷入巨大状态空间
- correct_method: 构造模n归约满射ψ从N-序列到M-序列，用偶子集计数证明均匀纤维大小2^(k-n)，由计数引理得N=M·2^(k-n)

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
- [x] 当前拓扑分类是否够用——这道题的problem_type(discrete_combinatorial)/ai_method_type(enumeration_brute_force)/gap_type(method_translation)都能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——标注值和已有值粒度统一，都是中等偏抽象的粒度。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。discrete_combinatorial + enumeration_brute_force + method_translation的组合能准确描述"直接枚举失败→需要翻译为纤维计数方法"的gap。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs**:

1. path_feature型：
   - scope: "从R3直接计数失败到R4-R7构造映射+纤维计数的完整路径"
   - tell: "题目要求比值N/M，暗示不需要分别计算N和M，而应构造映射利用均匀纤维"
   - hint: "构造从N-序列到M-序列的满射，证明纤维大小均匀，由计数引理直接得比值"
   - hint_level: 0.8
   - generalizability: "high — 比值问题→满射+均匀纤维计数的策略适用于大量组合计数比值问题"
   - why_not_visible_locally: "从任何单一步骤看，'构造映射而非分别计数'的策略不可见——它需要看到从'比值问题'到'纤维计数'的完整路径，包括直接计数为何失败、模n归约为何可行、纤维为何均匀三个洞察的组合"
   - tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"}
   - tell_small_concepts: ["ratio problem", "surjection construction", "uniform fiber", "counting lemma"]

2. implicit型：
   - observation_point: "R5"
   - tell: "奇偶约束（低灯奇数次、高灯偶数次）隐含编码了纤维大小2^(c-1)"
   - hint: "奇数次切换c_i中选偶数子集指向高灯→2^(c_i-1)种；偶子集计数由对称差对合证明"
   - hint_level: 0.7
   - generalizability: "medium — 奇偶约束到2^(c-1)分裂计数的映射适用于奇偶约束组合问题"
   - why_not_visible_locally: "奇偶约束与2^(c-1)分裂计数之间的联系在任何单一步骤中不可见——它需要同时认识到：(1)奇数次可分解为奇+偶，(2)偶子集个数为2^(c-1)，(3)乘积简化为2^(k-n)。这三步的连接是隐含的。"
   - tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "algebraic_identity", gap_type: "knowledge_gap"}
   - tell_small_concepts: ["parity constraint", "odd-even split", "even subset counting", "2^(c-1)", "symmetric difference involution"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试分别直接计数N和M，用生成函数或容斥原理处理2n个灯的奇偶约束，陷入巨大状态空间。即使想到构造映射，也不太可能独立发现模n归约+偶子集计数的组合，更难将奇偶约束与2^(c-1)分裂计数联系起来。"
- suitable_for_poc: ["tell_identification", "hint_injection", "method_translation"]
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
- [x] answer（=2^(k-n)）
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

**将完整JSON写入工作目录的 `profile.json` 文件**：已写入 `subagents-dirs/compfiles_imo2008p5/profile.json`

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: compfiles_imo2008p5, 7 local pairs, 2 global pairs, answer=2^(k-n), knowledge_bottleneck=R5, thinking_bottleneck=R4

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo2008p5
- solution_method_type: fiber_counting_via_reduction_map
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系完全覆盖本题。discrete_combinatorial + enumeration_brute_force + method_translation的组合准确描述了"直接枚举失败→需要翻译为纤维计数方法"的gap。
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
