# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1975p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1975P5.lean
- **来源**: USA 1975 P5
- **ArangoDB progress记录_key**: 329308（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1975P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：A pack of n cards, including three aces, is well shuffled. Cards are turned over in turn. Show that the expected number of cards that must be turned over to reach the second ace is (n+1)/2.
- 解答核心思路（1-2句话）：将三张A的位置建模为{1,...,n}的3元子集，第二张A的位置即中间元素(mid)。利用反射变换 x→n+1-x 将每个配置映射为其镜像，mid(S)+mid(reflect(S))=n+1。由于反射是样本空间上的对合双射，mid的平均值等于(n+1)/2。
- 解答关键步骤列表：
  1. 将洗牌后的牌堆建模为{1,...,n}的3元子集（三张A的位置），均匀分布
  2. 定义反射变换 reflect(n,x) = n+1-x，将位置关于中心翻转
  3. 证明反射将mid(S)映射为n+1-mid(S)（核心引理 mid_image_reflect）
  4. 证明反射是样本空间上的对合（involution），即反射两次回到原集
  5. 证明反射是样本空间上的双射（permutation）
  6. 利用双射性质：sum(mid) = sum(mid(reflect(S))) = sum(n+1-mid(S))，故2*sum = C(n,3)*(n+1)
  7. 平均值 = sum/C(n,3) = (n+1)/2

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
| 1 | 纯元认知观察 | 0.2 | 描述这道题的结构：已知什么？求什么？关键数学对象是什么？ | 已知n张牌中有3张A，洗匀后依次翻牌。求翻到第2张A时翻过的牌数的期望。关键对象：3张A的位置是{1,...,n}的3元子集，第二张A的位置是这三个位置的中间值（第二顺序统计量）。需要证明期望=(n+1)/2。 |
| 2 | 自由列举 | 0.5 | 列出所有可能用来计算这个期望的方法。 | 1) 直接计算：求P(第2张A在位置k)，然后求和k*P(k)；2) 指示变量法：用线性期望分解；3) 对称性论证：利用某种对称变换；4) 枚举所有3元子集求mid的平均值；5) 连续类比/积分近似。 |
| 3 | 小尝试 | 0.3 | 试试直接计算法：写出P(第2张A在位置k)的公式，看看能否求和。 | P(第2张A在位置k) = C(k-1,1)*C(n-k,1)/C(n,3) = (k-1)(n-k)/C(n,3)。期望 = sum_{k=2}^{n-1} k*(k-1)(n-k)/C(n,3)。这个求和可以展开但很繁琐，需要计算sum k(k-1)(n-k)，涉及三阶矩，容易出错。 |
| 4 | 思维操作引导 | 0.7 | 不要做繁琐求和。观察答案(n+1)/2是{1,...,n}的中点。执行以下思维操作：寻找一个将样本空间映射到自身的变换T，使得T把mid(S)映射为n+1-mid(S)。什么样的变换能做到这一点？ | 考虑反射变换：x→n+1-x。如果S={a,b,c}（a<b<c），则reflect(S)={n+1-c, n+1-b, n+1-a}，mid(reflect(S))=n+1-b=n+1-mid(S)。反射把最小变最大、最大变最小、中间变n+1-中间。这正是我们需要的变换！ |
| 5 | 推进 | 0.5 | 验证反射变换是样本空间上的对合双射，然后利用mid(S)+mid(reflect(S))=n+1推导期望。 | 反射x→n+1-x是{1,...,n}上的对合（反射两次回到原位），因此它把3元子集映射为3元子集，且是样本空间上的双射。由于mid(S)+mid(reflect(S))=n+1对所有S成立，且反射是双射，所以sum(mid)=sum(mid(reflect(S)))=sum(n+1-mid)。因此2*sum=C(n,3)*(n+1)，期望=(n+1)/2。 |
| 6 | 能量传递引导 | 0.2 | 把以上推理整理成完整证明。你已经有了所有关键部件：反射变换、对合性质、mid互补关系、双射求和。写出干净的证明。 | 完整证明：设三张A的位置为{1,...,n}的3元子集S，mid(S)为第二张A的位置。定义反射T(x)=n+1-x。T是{1,...,n}上的对合，诱导样本空间上的双射。mid(T(S))=n+1-mid(S)。因此E[mid]=E[mid(T(S))]=E[n+1-mid(S)]=n+1-E[mid]，解得E[mid]=(n+1)/2。 |

**统计**：
- total_rounds: 6
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 0.2+0.5+0.3+0.7+0.5+0.2 = 2.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

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
- structure_features: 3元子集上的期望值计算，第二顺序统计量，反射对称性论证
- key_objects: ["3-element subsets of {1,...,n}", "second order statistic (mid)", "reflection involution x→n+1-x", "expected value", "sample space bijection"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["symmetry_exploitation", "reflection_principle", "pairing_argument", "involution_bijection", "order_statistic_recognition"]
- primary_pattern: symmetry_exploitation
- knowledge_required: ["order statistics", "expected value over uniform distribution", "involution and bijection on finite sets", "reflection symmetry in combinatorics"]
- key_insight: 答案(n+1)/2是{1,...,n}的中点，暗示存在反射对称——将每个3元子集关于中心翻转，mid(S)变为n+1-mid(S)，由于反射是双射，平均值恰为中点(n+1)/2。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_calculation（直接计算第二顺序统计量的分布并求和）
- translation_to: symmetry_reflection（利用反射对称性将求和问题转化为配对论证）
- translation_type: method_translation（从分析法到对称性论证的方法转换）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["expected_value", "order_statistic", "midpoint_symmetry", "reflection_involution", "pairing_argument", "sample_space_bijection"]
- expected_ai_method: 直接计算第二顺序统计量的分布P(第2张A在位置k)=(k-1)(n-k)/C(n,3)，然后求和k*P(k)得到期望值。这个方法可行但计算繁琐，涉及三阶多项式求和。
- correct_method: 反射对称性论证：定义反射变换x→n+1-x，证明它是样本空间上的对合双射，且mid(S)+mid(reflect(S))=n+1，由此2*E[mid]=n+1，即E[mid]=(n+1)/2。

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是。discrete_combinatorial、direct_calculation、method_problem_mismatch均已存在且粒度合适。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是。三个维度都是抽象级别，与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够。这道题的核心gap是"直接计算可行但繁琐，对称性论证优雅"——method_problem_mismatch准确描述了这一gap。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。现有拓扑分类体系完全覆盖。

**拓扑进化建议**（如有）：无。现有分类体系充分。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 6 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI描述了题目结构（3张A的位置、第二顺序统计量、期望值），但未识别答案(n+1)/2的对称性含义 | 观察答案(n+1)/2是{1,...,n}的中点，思考这个中点形式暗示了什么对称性 | 0.2 | 纯元认知观察 | false | {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"} | ["expected_value", "order_statistic", "midpoint_form"] |
| 2 | AI列举了多种方法（直接计算、指示变量、对称性、枚举），但对称性只是众多选项之一，未被识别为关键路径 | 在列举的方法中，哪个方法能避免繁琐计算？关注"对称性论证"这一选项 | 0.5 | 自由列举 | false | {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "search_space_estimation"} | ["direct_calculation", "indicator_variables", "symmetry", "enumeration"] |
| 3 | AI尝试直接计算，得到P(k)=(k-1)(n-k)/C(n,3)，面临三阶多项式求和，计算路径正确但繁琐 | 停止直接计算。答案的中点形式暗示存在更优雅的对称性方法 | 0.3 | 小尝试 | false | {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"} | ["binomial_coefficients", "polynomial_sum", "third_order_moment"] |
| 4 | AI被引导寻找反射变换，识别出x→n+1-x将mid映射为n+1-mid——这是知识瓶颈，需要知道反射对称性技巧 | 寻找样本空间上的变换T，使得T(mid(S))=n+1-mid(S)。考虑位置关于中心的反射 | 0.7 | 思维操作引导 | true | {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "knowledge_gap"} | ["reflection", "involution", "midpoint_complement", "center_symmetry"] |
| 5 | AI验证了反射是对合双射，并推导出2*sum=C(n,3)*(n+1)，逻辑链条即将闭合 | 利用双射性质完成求和等式，推导期望=(n+1)/2 | 0.5 | 推进 | false | {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "method_translation"} | ["involution_bijection", "sum_pairing", "double_counting"] |
| 6 | AI将所有部件组装成完整证明，逻辑清晰 | 整理完整证明，确认所有步骤：反射定义→对合性质→mid互补→双射求和→结论 | 0.2 | 能量传递引导 | false | {problem_type: "discrete_combinatorial", ai_method_type: "logical_deduction", gap_type: "method_translation"} | ["complete_proof", "symmetry_argument", "expectation_conclusion"] |

**全局pairs详情**：

1. path_feature型：
- scope: "从直接计算尝试到反射对称性论证的完整路径转换"
- observation_point: null
- tell: "解题路径需要从'计算分布求和'转换到'寻找对称变换配对'。这一转换是路径级特征——它不是任何单步推理的产物，而是需要看到'答案形式(中点)+问题结构(均匀分布)'的组合才能触发的方法论跳跃。"
- hint: "当期望值等于可能范围的中点时，寻找样本空间上的对合变换（如反射），使得该量在变换下取互补值（range - value），然后利用双射性得出平均值=中点。"
- hint_level: 0.7
- generalizability: "high - 反射/中点对称性原理广泛适用于期望值等于范围中点的离散概率问题"
- why_not_visible_locally: "反射对称性洞察是整个解题路径的全局特征——没有任何单步计算能揭示'答案为中点→存在反射对称'这一跨步骤的元模式。在局部视角中，AI看到的是P(k)=(k-1)(n-k)/C(n,3)这样的具体公式，无法从中读出'应该放弃计算转而寻找对称变换'的路径级判断。"
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "method_translation"}
- tell_small_concepts: ["midpoint_symmetry", "reflection_principle", "involution_pairing", "method_switch"]

2. implicit型：
- scope: "答案形式(n+1)/2与反射对称性之间的蕴含关系"
- observation_point: "R1"
- tell: "答案(n+1)/2恰好是{1,...,n}的中点。这一形式隐含编码了反射对称性——如果一个量在均匀分布下的期望等于其取值范围的中点，那么样本空间上很可能存在一个对合变换将该量映射为其互补值。"
- hint: "看到期望值=范围中点时，立即检查是否存在样本空间上的对合T使得quantity(T(x))=range-quantity(x)。这是'中点答案→反射对称'的元模式识别。"
- hint_level: 0.8
- generalizability: "high - '中点答案暗示反射对称'这一元模式适用于大量概率和组合期望问题"
- why_not_visible_locally: "答案形式与对称性论证之间的蕴含关系在任何单步计算中都不可见——它是一种元层面的模式识别，需要同时看到'答案是什么形式'和'问题有什么对称结构'才能触发。局部步骤中的公式推导（如P(k)的计算）完全不会暴露这一蕴含信息。"
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["midpoint_answer", "involution_complement", "range_symmetry", "meta_pattern"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "marginal"
- bare_ai_error_prediction: "bare AI可能通过直接计算得到正确答案——P(第2张A在位置k)=(k-1)(n-k)/C(n,3)的求和虽繁琐但可行。但bare AI很可能不会发现反射对称性论证，因为'答案为中点→存在反射对称'这一元模式识别不是自然推理路径。bare AI可能卡在三阶多项式求和的代数运算中，或虽然算对但无法给出优雅证明。"
- suitable_for_poc: ["POC-VMS-tell-detection: 测试系统能否从AI的thinking中识别'AI在做直接计算而未考虑对称性'这一tell", "POC-VMS-hint-injection: 测试注入'寻找反射对称变换'这一hint后AI是否能完成证明", "POC-VMS-method-translation: 测试从direct_calculation到symmetry_reflection的方法翻译是否有效"]
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
- [x] answer（proof类型填要证明的结论）
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

---

## Step 10: 入库ArangoDB [x]

**操作**：用exec工具执行Python脚本入库

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证详情：6 local pairs, 2 global pairs, per-pair tell_topology存在, why_not_visible_locally非None, answer非None, knowledge_bottleneck="R4", thinking_bottleneck="R3"

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_usa1975p5
- solution_method_type: symmetry_reflection
- 局部(tell,hint)对数量: 6
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系（discrete_combinatorial / direct_calculation / method_problem_mismatch等）完全覆盖此题。
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
