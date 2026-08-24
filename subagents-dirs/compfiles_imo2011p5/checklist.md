# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2011p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2011P5.lean
- **来源**: IMO 2011 P5
- **ArangoDB progress记录_key**: 329219（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2011P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let f be a function from the set of integers to the set of positive integers. Suppose that, for any two integers m and n, the difference f(m) - f(n) is divisible by f(m-n). Prove that, for all integers m and n with f(m) ≤ f(n), the number f(n) is divisible by f(m).
- 解答核心思路（1-2句话）：先证明所有f(n)整除f(0)，再利用此证明f(-n)=f(n)（偶函数性），然后反证法假设f(m)<f(n)且f(m)∤f(n)，通过分析f(m+n)的整除关系导出矛盾。
- 解答关键步骤列表：
  1. 证明 f(n) | f(0) 对所有n成立：取h中m=n,n=0，得f(n-0)=f(n) | f(n)-f(0)，再用dvd_iff_dvd_of_dvd_sub推出f(n)|f(0)
  2. 证明 f(-n) = f(n)（偶函数）：由f(-n)|f(0)和f(n)|f(0)分别推出f(-n)|f(n)和f(n)|f(-n)，再用正整数上的整除反对称性得f(-n)=f(n)
  3. 反证法：假设存在m,n使f(m)<f(n)且f(m)∤f(n)
  4. 证明 f(m+n) ≤ f(n)-f(m)：利用f(m+n)=f(m-(-n)) | f(m)-f(-n) = f(m)-f(n) = -(f(n)-f(m))，所以f(m+n)|f(n)-f(m)，且f(n)-f(m)>0，故f(m+n)≤f(n)-f(m)
  5. 证明 f(m) ∤ f(m+n)：因为f(m)=f((n+m)-n) | f(n+m)-f(n)，若f(m)|f(n+m)则f(m)|f(n)，矛盾
  6. 证明 f(n) ≤ |f(m+n)-f(m)|：因为f(n)=f((n+m)-m) | f(n+m)-f(m)，所以f(n)≤|f(n+m)-f(m)|
  7. 分情况讨论|f(n+m)-f(m)|的两个方向，均导出矛盾（结合h1的f(m+n)≤f(n)-f(m)和h2的f(m)∤f(m+n)）

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
| 1 | 纯元认知观察 | 0.7 | 请描述这道题的结构：已知条件是什么？要证明什么？条件中涉及哪些数学对象和关系？ | 已知：f: ℤ→ℤ⁺，且∀m,n, f(m-n) | f(m)-f(n)。要证：∀m,n, f(m)≤f(n) ⟹ f(m)|f(n)。核心对象是整函数f，核心关系是整除关系f(m-n)整除差值f(m)-f(n)。目标是从整除差值条件推出整除本身。 |
| 2 | 自由列举 | 0.6 | 给定条件f(m-n)|f(m)-f(n)，你能想到哪些特殊赋值来提取信息？列出所有你能想到的m,n取值组合。 | 可以尝试：(1) m=n,n=0 → f(n)|f(n)-f(0)；(2) m=0,n=n → f(-n)|f(0)-f(n)；(3) m=n,n=n → f(0)|0（平凡）；(4) m=2n,n=n → f(n)|f(2n)-f(n)；(5) m=n+m,n=m → f(n)|f(n+m)-f(m)；(6) m=n,n=-n → f(2n)|f(n)-f(-n) |
| 3 | 小尝试 | 0.5 | 试试m=n,n=0这个赋值，你能从中提取什么结论？ | 取m=n,n=0：f(n-0)=f(n) | f(n)-f(0)。这意味着f(n)整除f(n)-f(0)。如果f(n)|f(n)-f(0)且f(n)|f(n)（自整除），那么f(n)|f(0)。即所有f(n)都整除f(0)。 |
| 4 | 思维操作引导 | 0.4 | 你已经知道f(n)|f(0)对所有n成立。现在请利用m=0,n=n和m=0,n=-n这两个赋值，结合f(n)|f(0)的结论，推导f(-n)和f(n)之间的关系。 | 取m=0,n=n：f(-n)|f(0)-f(n)，又f(-n)|f(0)，所以f(-n)|f(n)。取m=0,n=-n：f(n)|f(0)-f(-n)，又f(n)|f(0)，所以f(n)|f(-n)。两者都是正整数，由整除反对称性得f(-n)=f(n)。f是偶函数。 |
| 5 | 思维操作引导 | 0.4 | 现在用反证法。假设存在m,n使f(m)<f(n)且f(m)∤f(n)。请分析f(m+n)的整除关系：f(m+n)能整除什么？f(m)和f(n)分别能整除什么与f(m+n)相关的量？ | (1) f(m+n)=f(m-(-n)) | f(m)-f(-n)=f(m)-f(n)=-(f(n)-f(m))，所以f(m+n)|f(n)-f(m)，且f(n)-f(m)>0，故f(m+n)≤f(n)-f(m)。(2) f(m)=f((n+m)-n) | f(n+m)-f(n)，若f(m)|f(n+m)则结合f(m)|f(n+m)-f(n)得f(m)|f(n)，矛盾，故f(m)∤f(n+m)。(3) f(n)=f((n+m)-m) | f(n+m)-f(m)，故f(n)≤|f(n+m)-f(m)|。 |
| 6 | 推进 | 0.5 | 你得到了三个不等式：f(m+n)≤f(n)-f(m)、f(m)∤f(m+n)、f(n)≤|f(m+n)-f(m)|。请分情况讨论|f(m+n)-f(m)|的两个方向，导出矛盾。 | 情况1：f(n)≤f(m+n)-f(m)，即f(n)+f(m)≤f(m+n)，但f(m+n)≤f(n)-f(m)，矛盾。情况2：f(n)≤f(m)-f(m+n)，即f(m+n)≤f(m)-f(n)<0，但f(m+n)是正整数，矛盾。两种情况都矛盾，故假设不成立。 |
| 7 | 能量传递引导 | 0.7 | 回顾整个证明的结构：先建立f(n)|f(0)的"锚点"，再推出偶函数性，最后反证法用f(m+n)作为"桥梁"导出矛盾。请总结这个证明的关键洞察。 | 关键洞察是：f(0)是所有f(n)的公倍数（锚点），偶函数性让f(m+n)可以表示为f(m-(-n))从而利用条件，而f(m+n)同时被f(m)、f(n)、f(n)-f(m)三个量约束，三重约束导致矛盾。证明的核心是找到f(m+n)这个"桥梁"变量，它同时连接了f(m)和f(n)的整除关系。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

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
- problem_type: constraint_satisfaction
- structure_features: 函数f: ℤ→ℤ⁺满足整除条件f(m-n)|f(m)-f(n)，需证明整除关系在值序约束下传递。条件是"差被整除"型约束，目标是"值本身被整除"。核心结构是通过特殊赋值从条件提取信息，再通过反证法导出矛盾。
- key_objects: ["整函数f: ℤ→ℤ⁺", "整除关系f(m-n)|f(m)-f(n)", "f(0)作为公倍数锚点", "偶函数性f(-n)=f(n)", "桥梁变量f(m+n)"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["特殊赋值提取信息", "锚点建立（f(0)作为公倍数）", "对称性推导（偶函数性）", "反证法", "桥梁变量构造（f(m+n)）", "多重约束交叉导出矛盾"]
- primary_pattern: 特殊赋值提取信息+反证法
- knowledge_required: ["整除的基本性质（传递性、反对称性）", "dvd_iff_dvd_of_dvd_sub（a|b-a且a|a则a|b）", "正整数上整除的反对称性", "le_of_dvd（整除蕴含不等式）", "绝对值与整除的关系"]
- key_insight: f(0)是所有f(n)的公倍数这一"锚点"性质，加上偶函数性f(-n)=f(n)，使得f(m+n)可以表示为f(m-(-n))从而利用条件，而f(m+n)同时被f(m)、f(n)、f(n)-f(m)三重约束导致矛盾。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接整除关系验证（尝试直接从f(m-n)|f(m)-f(n)推出f(m)|f(n)）
- translation_to: 锚点-对称性-反证法框架（先建立f(0)锚点，再推导偶函数性，最后用桥梁变量f(m+n)反证）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["特殊赋值", "f(0)锚点", "偶函数性", "整除反对称性", "桥梁变量f(m+n)", "反证法", "三重约束矛盾"]
- expected_ai_method: 直接尝试从条件f(m-n)|f(m)-f(n)通过代数变形推出f(m)|f(n)，不建立中间锚点
- correct_method: 先用特殊赋值建立f(n)|f(0)锚点，再推导偶函数性f(-n)=f(n)，然后用反证法通过桥梁变量f(m+n)的三重整除约束导出矛盾

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。constraint_satisfaction/direct_manipulation/method_translation都能归入已有值。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。都是中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心gap是"需要从直接验证翻译到锚点-对称性-反证法框架"，method_translation准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。当前拓扑分类足够。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对函数整除条件题目，尚未识别出条件中"差被整除"和目标"值被整除"之间的结构gap | 描述题目结构，识别已知/未知和核心关系 | 0.7 | 纯元认知观察 | false | {problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "method_problem_mismatch"} | ["函数整除条件", "差被整除vs值被整除"] |
| 2 | AI已识别条件结构但未系统列出特殊赋值方向 | 列出所有可能的m,n特殊赋值组合 | 0.6 | 自由列举 | false | {problem_type: "constraint_satisfaction", ai_method_type: "enumeration_brute_force", gap_type: "search_space_estimation"} | ["特殊赋值", "m=n,n=0", "m=0,n=n"] |
| 3 | AI尝试直接处理但未发现f(0)锚点 | 试m=n,n=0赋值，提取f(n)|f(0) | 0.5 | 小尝试 | false | {problem_type: "constraint_satisfaction", ai_method_type: "direct_calculation", gap_type: "structural_transformation"} | ["f(0)锚点", "dvd_iff_dvd_of_dvd_sub"] |
| 4 | AI知道f(n)|f(0)但不知道如何利用它推导对称性 | 利用m=0赋值结合f(n)|f(0)推导f(-n)=f(n) | 0.4 | 思维操作引导 | true | {problem_type: "constraint_satisfaction", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"} | ["偶函数性", "整除反对称性", "f(-n)=f(n)"] |
| 5 | AI有锚点和偶函数性但不知道如何构造桥梁变量 | 用反证法分析f(m+n)的三重整除关系 | 0.4 | 思维操作引导 | false | {problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "method_translation"} | ["桥梁变量f(m+n)", "反证法", "三重整除约束"] |
| 6 | AI有三重约束但未分情况导出矛盾 | 分情况讨论绝对值两个方向导出矛盾 | 0.5 | 推进 | false | {problem_type: "constraint_satisfaction", ai_method_type: "case_by_case", gap_type: "method_problem_mismatch"} | ["绝对值分情况", "矛盾推导", "le_of_dvd"] |
| 7 | AI完成证明但未总结关键洞察 | 总结证明的锚点-对称性-反证法结构 | 0.7 | 能量传递引导 | false | {problem_type: "constraint_satisfaction", ai_method_type: "logical_deduction", gap_type: "method_translation"} | ["锚点-对称性-反证法", "桥梁变量", "三重约束"] |

**全局tell_hint_pairs详情**：

1. path_feature型：
   - scope: 完整证明路径
   - observation_point: null
   - tell: 证明路径需要三个阶段——锚点建立(f(n)|f(0))→对称性推导(f(-n)=f(n))→反证法桥梁(f(m+n)三重约束矛盾)。bare AI倾向于直接验证，跳过锚点和对称性阶段。
   - hint: 先建立f(0)锚点，再推导偶函数性，最后用f(m+n)作为桥梁变量反证
   - hint_level: 0.6
   - generalizability: "high — 锚点-对称性-反证法框架适用于整除条件类函数问题"
   - why_not_visible_locally: "在局部视角中，AI看到的是单步整除关系，无法看到'先建锚点再推导对称性最后反证'这个三阶段路径结构。锚点的选择（f(0)）和桥梁变量的选择（f(m+n)）都是从全局路径回溯才能确定的，局部步骤中看不到为什么选这些特定值。"
   - tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
   - tell_small_concepts: ["f(0)锚点", "偶函数性", "桥梁变量f(m+n)", "三阶段路径"]

2. implicit型：
   - scope: f(m+n)的桥梁角色
   - observation_point: "R5"
   - tell: f(m+n)同时被三个量约束：f(m+n)|f(n)-f(m)、f(m)|f(n+m)-f(n)（推出f(m)∤f(n+m)）、f(n)|f(n+m)-f(m)。这三重约束隐含在条件f(m-n)|f(m)-f(n)的不同赋值中，但需要偶函数性才能将f(m+n)表示为f(m-(-n))。
   - hint: 对f(m+n)用三个不同赋值提取三重整除约束，结合偶函数性将f(m+n)表示为f(m-(-n))
   - hint_level: 0.5
   - generalizability: "medium — 桥梁变量的三重约束模式适用于需要交叉验证的整除问题"
   - why_not_visible_locally: "在R5的局部视角中，AI看到的是对f(m+n)的三个独立赋值，但'三重约束导致矛盾'这个蕴含信息需要同时持有三个不等式并交叉比较才能看到。每个赋值单独看只是普通的整除关系，只有将三个赋值的结果放在一起才暴露出矛盾结构。"
   - tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "structural_transformation"}
   - tell_small_concepts: ["桥梁变量f(m+n)", "三重整除约束", "偶函数性转换", "交叉矛盾"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接从条件f(m-n)|f(m)-f(n)通过代数变形推出f(m)|f(n)，不会想到先建立f(0)锚点和偶函数性。即使尝试特殊赋值，也未必能系统性地将f(m+n)作为桥梁变量并提取三重约束。最可能卡在"如何从差整除推出值整除"这一步，缺乏中间锚点。
- suitable_for_poc: ["POC-VMS-hint注入验证——测试锚点提示能否引导AI发现f(0)公倍数性质", "POC-VMS-tell识别验证——测试系统能否从AI thinking中识别'跳过锚点直接验证'的分叉信号", "POC-VMS-脉络继承验证——测试三阶段路径脉络能否引导AI完成完整证明"]
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
2. 更新`problem_extraction_progress`集合中`_key="329219"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2011p5"
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
    '_key': '329219',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2011p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2011p5')
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
- problem_id: compfiles_imo2011p5
- solution_method_type: anchor_symmetry_contradiction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。当前拓扑分类（constraint_satisfaction/direct_manipulation/method_translation）足够覆盖这道题。
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
