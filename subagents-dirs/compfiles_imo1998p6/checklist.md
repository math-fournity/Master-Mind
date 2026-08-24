# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1998p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1998P6.lean
- **来源**: IMO 1998 P6
- **ArangoDB progress记录_key**: 329166（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1998P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Determine the least possible value of f(1998), where f: ℕ+ → ℕ+ satisfies f(n²·f(m)) = m·f(n)² for all m, n ∈ ℕ+.
- 解答核心思路（1-2句话）：通过代换推导出f的乘法结构，定义归一化函数g(n)=f(n)/f(1)证明g是完全乘性对合（permutation of primes），将问题归结为在素数排列下最小化g(2)·g(3)³·g(37)，最小值为120。
- 解答关键步骤列表：
  1. 令n=1得f(f(m))=m·f(1)²，证明f单射
  2. 推导乘法关系f(a)·f(b)=f(1)·f(a·b)，证明f(1)|f(n)对所有n
  3. 定义g(n)=f(n)/f(1)，证明g完全乘性、g(g(n))=n（对合）、g将素数映到素数
  4. 分解1998=2·3³·37，得f(1998)=f(1)·g(2)·g(3)³·g(37)
  5. g(2),g(3),g(37)为互异素数，最小化p·q³·r≥120（取p=3,q=2,r=5）
  6. 构造：素数排列2↔3, 5↔37，g(1998)=3·2³·5=120，验证满足函数方程

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
| 1 | 纯元认知观察 | 0.8 | 观察这个函数方程f(n²·f(m))=m·f(n)²的结构。它定义在什么域上？有哪些自由变量？f(1)扮演什么角色？ | f: ℕ+→ℕ+，方程有两个自由变量m和n。方程将f在复合参数n²·f(m)处的值与f在简单参数n处的值联系起来。f(1)是一个未知常数，可能起归一化作用。目标是找f(1998)的最小值。 |
| 2 | 自由列举 | 0.6 | 列出所有可以尝试的特殊代换：哪些值 of m 和 n 能从方程中提取最多信息？ | 令n=1得f(f(m))=m·f(1)²；令m=1得f(n²·f(1))=f(n)²；令m=n得f(n²·f(n))=n·f(n)²；尝试用f(f(n))关系推导单射性。f(1)的值是关键未知量。 |
| 3 | 小尝试 | 0.3 | 试令n=1，你得到f(f(m))=m·f(1)²。这告诉你什么？能从这里推出f的单射性吗？ | f(f(m))=m·f(1)²说明f∘f是线性函数（乘以常数f(1)²）。若f(a)=f(b)则f(f(a))=f(f(b))即a·f(1)²=b·f(1)²，故a=b，f单射。但还不知道f(1)的值和f的乘法结构。 |
| 4 | 思维操作引导 | 0.4 | 从f(f(n))=n·f(1)²和原方程出发，推导乘法关系f(a)·f(b)=f(1)·f(a·b)，并证明f(1)整除f(n)对所有n成立。 | 利用f(n²·f(1))=f(n)²和f(f(n))=n·f(1)²，通过巧妙组合方程中的参数可推出f(a)·f(b)=f(1)·f(a·b)。由此f(1)·f(n)=f(1)·f(n)，用素因子分析可证f(1)|f(n)。这为归一化铺路。 |
| 5 | 思维操作引导 | 0.5 | 既然f(1)|f(n)，定义g(n)=f(n)/f(1)。证明g是完全乘性的（g(ab)=g(a)g(b)），g(g(n))=n（对合），且g将素数映到素数。 | g(ab)=f(ab)/f(1)=(f(a)f(b)/f(1))/f(1)=g(a)g(b)，故完全乘性。g(g(n))=g(f(n)/f(1))需要用f(f(n))=n·f(1)²推出g(g(n))=n。若p素数且g(p)=ab（a,b>1），则g(a)g(b)=p，由g对合得矛盾，故g(p)素数。 |
| 6 | 推进 | 0.3 | 分解1998=2·3³·37，用g的完全乘性写出f(1998)=f(1)·g(2)·g(3)³·g(37)。g(2),g(3),g(37)是互异素数，求p·q³·r的最小值。 | g(2),g(3),g(37)互异（因g对合且2,3,37互异）。最小化p·q³·r（p,q,r互异素数）：取q=2（最小素数给最高幂），p=3,r=5，得3·8·5=120。故f(1998)≥f(1)·120≥120。 |
| 7 | 能量传递引导 | 0.2 | 构造一个达到f(1998)=120的函数。提示：定义素数排列2↔3, 5↔37，其余素数不动，g(n)为n的素因子在此排列下的像之积。验证g(1998)=120且g满足函数方程。 | 定义primeSwap: 2→3,3→2,5→37,37→5,其余不动。g(n)=∏primeSwap(p_i)^{e_i}。g是完全乘性的（素因子分解的像），g(g(n))=n（primeSwap是对合），故g(n²·g(m))=g(n)²·g(g(m))=g(n)²·m。g(1998)=g(2·3³·37)=3·2³·5=120。取f=g即得f(1)=1,f(1998)=120。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.1
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5（定义g并证明完全乘性+对合+素数保持，是核心知识转折）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6（在互异素数约束下最小化p·q³·r需要组合优化思维）

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
- problem_type: characterization（刻画满足函数方程的f的结构，再在此基础上优化）
- structure_features: 正整数上的函数方程，含未知常数f(1)，通过归一化转化为完全乘性对合，最终归结为素数排列上的极值优化
- key_objects: [f: ℕ+→ℕ+, 函数方程f(n²·f(m))=m·f(n)², f(1)未知常数, g(n)=f(n)/f(1)归一化函数, 完全乘性对合, 素数排列, 1998=2·3³·37]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [substitution_strategy, injectivity_deduction, normalization, structural_decomposition, completely_multiplicative_structure, involution_property, prime_preservation, prime_factorization, extremal_optimization, construction_verification]
- primary_pattern: normalization（通过定义g=f/f(1)归一化，将含未知常数f(1)的问题转化为f(1)=1的标准情形）
- knowledge_required: [函数方程代换技巧, 单射性证明, 完全乘性函数, 对合(involutions), 素数因子分解, 整除性与素因子分析, 素数排列, 极值论证]
- key_insight: 定义g(n)=f(n)/f(1)归一化后，g成为完全乘性对合，其作用由素数排列决定，问题归结为在互异素数约束下最小化p·q³·r=120

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 含未知常数f(1)的原始函数方程（代数操作层面）
- translation_to: 归一化后的完全乘性对合在素数排列上的极值优化（数论结构层面）
- translation_type: structural_transformation（通过归一化+结构分解，将函数方程翻译为素数排列优化问题）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [normalization, completely_multiplicative, involution, prime_permutation, prime_factorization, f1_divides_fn, extremal_optimization, construction_verification]
- expected_ai_method: direct_calculation（bare AI预期会直接代换计算f(1998)，不归一化，看不到乘法结构）
- correct_method: normalization + structural decomposition（归一化定义g，证明完全乘性对合，归结为素数排列优化）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。characterization覆盖"刻画f的结构再优化"，direct_calculation覆盖bare AI的直接代换倾向，structural_transformation覆盖归一化这个关键gap。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。三个维度都是中等偏抽象的粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的核心gap是"需要归一化才能看到乘法结构"，structural_transformation精确描述了这个gap。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类足够。

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

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到函数方程但不知道从哪里入手——未识别代换策略 | 描述方程结构：定义域、自由变量、f(1)的角色 | 0.8 | 纯元认知观察 | false | {characterization, direct_calculation, method_problem_mismatch} | [functional_equation_structure, free_variables, f_of_1] |
| 2 | AI未列举出可尝试的特殊代换 | 列出所有特殊代换：n=1, m=1, m=n等 | 0.6 | 自由列举 | false | {characterization, enumeration_brute_force, search_space_estimation} | [special_substitution, parameter_elimination, f_of_1] |
| 3 | AI试了n=1得到f(f(m))=m·f(1)²但不知道下一步 | 从f(f(n))=n·f(1)²推出f单射，探索乘法结构 | 0.3 | 小尝试 | false | {characterization, direct_calculation, structural_transformation} | [injectivity, f_f_involution, multiplicative_relation] |
| 4 | AI有单射性但未推导乘法关系f(a)f(b)=f(1)f(ab)和f(1)|f(n) | 推导乘法关系并证明f(1)整除f(n) | 0.4 | 思维操作引导 | true | {characterization, direct_calculation, knowledge_gap} | [multiplicative_relation, divisibility, f1_divides_fn] |
| 5 | AI有乘法关系但未归一化定义g(n)=f(n)/f(1) | 定义g，证明完全乘性、对合、素数保持 | 0.5 | 思维操作引导 | true | {characterization, direct_calculation, knowledge_gap} | [normalization, completely_multiplicative, involution, prime_preservation] |
| 6 | AI知道g是乘性对合但未分解1998并优化 | 分解1998=2·3³·37，最小化p·q³·r≥120 | 0.3 | 推进 | false | {characterization, direct_calculation, search_space_estimation} | [prime_factorization, distinct_primes, extremal_optimization, pqr_minimization] |
| 7 | AI有下界120但未构造达到函数 | 构造素数排列2↔3,5↔37，验证g(1998)=120 | 0.2 | 能量传递引导 | false | {characterization, direct_manipulation, method_problem_mismatch} | [prime_permutation, construction_verification, achieving_function] |

**全局tell_hint_pairs详情**：

1. path_feature型：
- scope_type: path_feature
- scope: 从原始函数方程到素数排列优化的完整解答路径
- observation_point: null
- tell: 解答需要归一化步骤（定义g=f/f(1)）将含未知常数f(1)的问题转化为完全乘性对合。这个归一化不是任何单步可见的——它是路径级的结构洞察。
- hint: 面对含未知常数的函数方程时，尝试除掉常数归一化到标准情形，再研究归一化函数的代数性质。
- hint_level: 0.7
- generalizability: high——归一化是函数方程中的通用技术
- why_not_visible_locally: 归一化g=f/f(1)只有在证明f(1)|f(n)对所有n成立后才有意义，而证明f(1)|f(n)本身需要先推导乘法关系f(a)f(b)=f(1)f(ab)——这是一个多步链条。没有任何单步能揭示归一化将导致完全乘性对合。
- tell_topology: {characterization, direct_calculation, structural_transformation}
- tell_small_concepts: [normalization, completely_multiplicative, involution, f1_divides_fn]

2. implicit型：
- scope_type: implicit
- scope: 函数方程与素数排列之间的隐藏联系
- observation_point: R5
- tell: 函数方程f(n²·f(m))=m·f(n)²归一化后强制g为完全乘性对合，其作用由素数排列决定。这意味着问题归结为素数排列上的优化——这个联系隐含在代数结构中。
- hint: 完全乘性对合由其在素数上的作用决定，素数上的作用必须是素数排列（自逆）。这将优化问题归结为选择素数排列。
- hint_level: 0.6
- generalizability: high——乘性函数与素数排列的对应是数论基本原理
- why_not_visible_locally: 从"ℕ+上的乘性对合"到"素数排列"的归结需要知道完全乘性函数由素数上的值决定、且素数上的对合延拓为ℕ+上的对合。这个推理链条在任何单步代数操作中都不可见。
- tell_topology: {characterization, direct_calculation, structural_transformation}
- tell_small_concepts: [completely_multiplicative, prime_permutation, involution, multiplicative_determined_by_primes]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会直接代换计算f(1998)，可能得到f(f(n))=n·f(1)²和单射性，但不会想到归一化定义g=f/f(1)。没有归一化，乘法结构隐藏在f(1)中不可见，AI无法将问题归结为素数排列优化。AI可能也无法证明f(1)|f(n)，这是归一化的前提。最终AI可能猜测f(1998)的值但无法给出严格下界证明和构造。
- suitable_for_poc: ["tell_hint_injection", "normalization_hint", "structural_transformation_hint", "knowledge_bottleneck_detection"]
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
2. 更新`problem_extraction_progress`集合中`_key="329166"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1998p6"
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
    '_key': '329166',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1998p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1998p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: compfiles_imo1998p6, 7 local pairs, 2 global pairs, answer=120, why_not_visible_locally均非None

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo1998p6
- solution_method_type: normalization + structural decomposition + extremal argument + construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类（characterization / direct_calculation / structural_transformation等）足够覆盖此题。
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
