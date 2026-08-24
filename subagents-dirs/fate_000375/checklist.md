# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000375
- **文件路径**: subagents-dirs/fate_000375/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396485（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000375/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 R → S 是形式上非分歧（formally unramified）环映射。证明存在一个 R-代数满射 S' → S，其核是平方为零的理想，且满足泛性质：对任意交换图 S → A/I, R → A（其中 I ⊂ A 是平方为零的理想），存在唯一的 R-代数映射 α': S' → A 使得 S' → A → A/I = S' → S → A/I。这是"泛一阶加厚"（universal first-order thickening）的存在性定理。
- 解答核心思路（1-2句话）：通过多项式呈现 S = P/J（P 为多项式环），构造 S' = P/J²，利用 P 的自由性获得提升存在性，利用形式非分歧性获得提升唯一性。
- 解答关键步骤列表：
  1. 选择多项式环 P = R[x_i] 和满射 P → S，令 J = ker(P → S)
  2. 构造 S' = P/J²，自然满射 f: S' → S，核为 J/J²，满足 (J/J²)² = 0
  3. 存在性：给定 g: S → A/I（I²=0），将 g 提升到 P → A（因 P 自由，只需选变量像），g(J) ⊂ I 蕴含 g(J²) ⊂ I² = 0，故 P → A 通过 S' = P/J² 分解，得到 α': S' → A
  4. 唯一性：若 α₁', α₂': S' → A 均满足条件，利用形式非分歧性（Hom(S,A) → Hom(S,A/I) 单射）证明 α₁' = α₂'
  5. Lean 证明为 sorry（仅有定理陈述，无实际证明）

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
| 1 | 纯元认知观察 | 0.8 | 这道题的数学结构是什么？已知条件R→S formally unramified意味着什么？需要构造的S'需要满足哪些条件？ | 题目要求构造一个R-代数满射S'→S，核平方为零，且满足泛性质。formally unramified意味着对任意平方为零理想I，Hom(S,A)→Hom(S,A/I)是单射（提升唯一性）。需要满足的条件：(1) S'是R-代数；(2) f:S'→S满射；(3) ker(f)²=0；(4) 泛性质：对任意g:S→A/I有唯一提升α':S'→A。 |
| 2 | 自由列举 | 0.7 | 构造一个环S'使其满射到S且核平方为零，有哪些可能的构造方法？列出所有你能想到的方向。 | 方向1：S'=S⊗_R S / I²（I=ker(μ)），利用对角理想；方向2：通过多项式呈现S=P/J，取S'=P/J²；方向3：S'=S[ε]/(ε²)（平凡加厚），但泛性质可能不满足；方向4：利用Ω_{S/R}=0（形式非分歧）的信息，因为Ω=I/I²=0意味着I=I²。 |
| 3 | 小尝试 | 0.4 | 试试方向1：S'=S⊗_R S / I²，其中I=ker(μ:S⊗_R S→S)。这个构造能工作吗？验证泛性质时需要什么条件？ | S'=S⊗_R S/I²，核为I/I²。由于formally unramified ⟹ Ω_{S/R}=I/I²=0 ⟹ I=I²，所以S'=S⊗_R S/I≅S，核为0。泛性质变为：对任意g:S→A/I存在唯一提升S→A，这需要formally étale而非仅unramified。所以方向1在formally unramified情形下退化为S'=S，泛性质的存在性部分不成立。方向1失败。 |
| 4 | 思维操作引导 | 0.5 | 方向1失败是因为S⊗_R S/I²在formally unramified时退化。现在换一个思路：用多项式呈现S=P/J（P=R[x_i]自由），考虑S'=P/J²。分析：(a)核是什么？(b)为什么P的自由性能帮助解决存在性？ | (a) 核ker(P/J²→P/J)=J/J²，且(J/J²)²=J²/J²=0，满足平方为零。(b) P是多项式环（自由R-代数），给定g:S→A/I，可以先选A中元素提升g(x_i)的像，定义P→A（自由选择变量像）。由于g(J)=0 in A/I，所以J的像在I中，J²的像在I²=0中。因此P→A杀死J²，通过S'=P/J²分解，得到α':S'→A。存在性由P的自由性保证。 |
| 5 | 推进 | 0.6 | 存在性已解决。现在处理唯一性：给定两个α₁',α₂':S'→A都满足mk∘αᵢ'=g∘f，如何用formally unramified证明α₁'=α₂'？ | α₁'和α₂'都是S'→A的R-代数映射，且mod I_A相等。考虑它们通过f:S'→S的"限制"——但f方向不对。正确做法：α₁',α₂'给出两个R-代数映射S'→A，它们mod I_A相等。考虑A×_{A/I}A（纤维积），它有平方为零核。两个映射S'→A给出一个映射S'→A×_{A/I}A。或者更直接：α₁'-α₂'取值在I_A中，定义一个导子S'→I_A。利用formally unramified（Ω_{S/R}=0）可以证明这个导子必须为零。具体地，导子S→I_A为零（因为Ω_{S/R}=0），而S'→S的核平方为零，导子通过核的分解也必须为零。 |
| 6 | 思维操作引导 | 0.5 | 唯一性论证需要更精确：formally unramified给出的是Hom(S,A)→Hom(S,A/I)单射。如何将S'→A的唯一性问题转化为S→A的单射问题？关键操作是什么？ | 关键操作：考虑两个提升α₁',α₂':S'→A。它们mod I_A相等意味着差值取值在I_A中。构造环B=A[ε]/(ε²)，其中ε对应I_A的方向。或者更直接：利用formally unramified对S的定义——如果两个R-代数映射φ,ψ:S→A在mod I_A后相等，则φ=ψ。但我们的映射是S'→A不是S→A。需要利用S'→S的满射性和核平方为零来转化。具体地：α₁',α₂'诱导两个映射S→A（如果S'→S有截面），或者利用S'=P/J²中P的自由性直接比较两个P→A的提升。最终：两个P→A的提升在mod I_A后相等（都提升g），而formally unramified的等价条件（通过P的自由性）给出唯一性。 |
| 7 | 能量传递引导 | 0.8 | 现在把所有部分整合：S'=P/J²的构造、存在性（P自由）、唯一性（formally unramified）。你能完整陈述证明了吗？ | 完整证明：(1)选多项式环P=R[x_i]满射到S，J=ker。(2)S'=P/J²，f:S'→S自然满射，ker=J/J²，(J/J²)²=0。(3)存在性：g:S→A/I，选A中提升g(x_i)定义φ:P→A。g(J)=0 in A/I ⟹ φ(J)⊂I ⟹ φ(J²)⊂I²=0。故φ通过S'分解得α':S'→A，满足mk∘α'=g∘f。(4)唯一性：若α₁',α₂'均满足，则mod I_A相等。由formally unramified（Hom(S,A)→Hom(S,A/I)单射），通过P的自由性和J²⊂I²=0的条件，两个提升必须相等。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4 (R1, R2, R5, R7)
- knowledge_rounds（思维操作引导的轮数）: 2 (R4, R6)
- level_sum: 0.8+0.7+0.4+0.5+0.6+0.5+0.8 = 4.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

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
- problem_type: structural_existence（构造一个满足泛性质的数学对象并证明其存在性）
- structure_features: 存在性证明+泛性质验证。需要构造环S'并证明其满足四个条件：(1)R-代数结构，(2)满射到S，(3)核平方为零，(4)泛性质（存在性+唯一性）。关键结构特征是"自由对象的商"构造——用多项式环P的自由性解决存在性，用formally unramified解决唯一性。
- key_objects: ["formally unramified ring map R→S", "surjection S'→S with square-zero kernel", "universal property of first-order thickening", "polynomial presentation P/J", "ideal J/J² with square zero", "R-algebra homomorphism lifting"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["构造法——通过多项式呈现构造S'=P/J²", "试错-排除——先试S⊗_R S/I²发现退化再换方向", "自由性利用——利用多项式环的自由性解决提升存在性", "条件分离——将泛性质拆分为存在性（P自由）和唯一性（formally unramified）两个独立子问题", "泛性质验证——构造后逐一验证四个条件"]
- primary_pattern: 构造法（通过自由对象的商构造满足泛性质的对象）
- knowledge_required: ["formally unramified的定义（Hom单射）", "Ω_{S/R}=I/I²与formally unramified的等价", "多项式环作为自由R-代数的泛性质", "理想平方为零的商环性质", "泛性质中存在性与唯一性的分离"]
- key_insight: S⊗_R S/I²在formally unramified时退化为S（因I=I²），必须改用多项式呈现S=P/J构造S'=P/J²——P的自由性解决存在性，formally unramified解决唯一性。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 张量积构造（S⊗_R S/I²，对角理想方法）
- translation_to: 自由对象商构造（P/J²，多项式呈现方法）
- translation_type: method_translation（从"内在"张量积构造翻译到"外在"自由呈现构造，因为内在构造在formally unramified条件下退化）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "structural_existence", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["formally unramified", "square-zero ideal", "universal property", "polynomial presentation", "tensor product diagonal", "module of differentials", "free algebra lifting", "kernel square zero"]
- expected_ai_method: bare AI会尝试用S⊗_R S/I²构造（对角理想/张量积方法），这是处理加厚问题的"标准"直觉，但在formally unramified条件下退化（I=I²导致S'=S），无法满足泛性质的存在性要求。
- correct_method: 通过多项式呈现S=P/J构造S'=P/J²，利用P的自由性解决存在性，formally unramified解决唯一性。

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。structural_existence（构造+存在性）、direct_manipulation（直接操作张量积/理想）、method_translation（从张量积方法翻译到自由呈现方法）都能归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。problem_type是抽象级，ai_method_type是抽象级，gap_type是中等级，与已有值粒度匹配。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的核心tell是"AI用了内在构造（张量积）但需要外在构造（自由呈现）"，method_translation准确捕捉了这个翻译需求。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。现有拓扑分类体系足够。

**拓扑进化建议**（如有）：无。现有三维度（problem_type, ai_method_type, gap_type）足以区分此题的tell。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

### 局部tell_hint_pairs详情：

**R1** (纯元认知观察, level=0.8): AI面对形式化环论题目尚未识别"泛一阶加厚"概念 / 描述题目结构识别四个条件 / topology: (structural_existence, direct_manipulation, structural_transformation) / concepts: [formally unramified, surjection, square-zero kernel, universal property]

**R2** (自由列举, level=0.7): AI列出多方向但不确定正确方向 / 列出所有构造方法 / topology: (structural_existence, direct_manipulation, search_space_estimation) / concepts: [tensor product diagonal, polynomial presentation, trivial thickening, module of differentials]

**R3** (小尝试, level=0.4): AI选S⊗_R S/I²但未意识到formally unramified导致退化 / 试张量积方向并检查退化 / is_knowledge_bottleneck: true / topology: (structural_existence, direct_manipulation, knowledge_gap) / concepts: [tensor product diagonal, I=I² degeneration, module of differentials zero, construction collapses to S]

**R4** (思维操作引导, level=0.5): AI发现张量积失败后需知多项式呈现策略 / 用P/J²构造分析核和自由性 / is_knowledge_bottleneck: true / topology: (structural_existence, direct_manipulation, knowledge_gap) / concepts: [polynomial presentation, P/J² construction, free algebra lifting, J/J² square zero]

**R5** (推进, level=0.6): AI理解构造但卡在唯一性论证 / 推进唯一性用导子或纤维积 / topology: (structural_existence, logical_deduction, structural_transformation) / concepts: [uniqueness argument, derivation to I_A, fiber product, formally unramified injectivity]

**R6** (思维操作引导, level=0.5): AI唯一性论证思维受阻需转化问题 / 精确化唯一性用P自由性转化 / topology: (structural_existence, logical_deduction, method_translation) / concepts: [Hom injectivity, S'→A to S→A reduction, free presentation comparison, uniqueness via unramified]

**R7** (能量传递引导, level=0.8): AI掌握所有组件需整合信心 / 整合完整陈述证明 / topology: (structural_existence, logical_deduction, method_translation) / concepts: [complete proof assembly, existence by freeness, uniqueness by unramified, QED]

### 全局tell_hint_pairs详情：

**Global 1** (path_feature型): scope="完整证明路径——从试错到正确构造的转换", observation_point=null, tell="AI推理路径中最关键的分叉点是从S⊗_R S/I²转向P/J²，这个转换在R3看到退化前不可预见", hint="当内在构造因形式非分歧退化时转向外在自由呈现构造", hint_level=0.6, generalizability="high——内在退化为外在的模式在交换代数中普遍出现", why_not_visible_locally="在R3局部视角中AI只看到张量积退化为S，但无法推断应用多项式呈现——后者需要知道P/J²构造和P自由性解决存在性，这是全局构造策略选择不是局部步骤能推出", topology: (structural_existence, direct_manipulation, method_translation), concepts: [tensor product degeneration, polynomial presentation switch, free algebra lifting, inner to outer construction]

**Global 2** (implicit型): scope="泛性质的存在性与唯一性分离", observation_point="R4", tell="泛性质要求存在性AND唯一性但formally unramified只给唯一性，存在性须来自构造的自由性", hint="将泛性质拆分为存在性（构造保证）和唯一性（unramified保证）两个独立子问题", hint_level=0.7, generalizability="high——存在性/唯一性分离是泛性质证明的通用模式", why_not_visible_locally="在局部步骤中AI分别处理存在性和唯一性，但'unramified只给唯一性不给存在性，存在性须来自构造自由性'这个洞察需同时看到两方面——单看定义或单看构造都无法发现此分离", topology: (structural_existence, logical_deduction, knowledge_gap), concepts: [existence vs uniqueness separation, formally unramified gives uniqueness only, free algebra gives existence, universal property decomposition]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会用S⊗_R S/I²构造（对角理想方法），这是处理加厚问题的标准直觉。但不会意识到formally unramified导致I=I²使构造退化为S，从而无法满足泛性质的存在性要求。即使发现退化，也大概率不知道应转向多项式呈现构造P/J²。在唯一性论证中，可能混淆formally unramified（单射）和formally étale（双射），错误地认为formally unramified直接给出存在性。
- suitable_for_poc: ["POC-VMS-8 hint端验证——此题需要关键的方法翻译提示（从张量积到多项式呈现），适合验证hint注入能否引导AI走正确方向", "POC-VMS-9/10 tell端验证——此题的tell信号明确（AI选了张量积方向但需要多项式呈现方向），适合验证形式化过滤能否命中"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/fate_000375/profile.json`。

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

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="396485"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000375"
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
    '_key': '396485',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000375',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000375')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [ ] 成功 / [ ] 失败
- 验证结果: [ ] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: fate_000375
- solution_method_type: construction_via_free_presentation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，现有三维度足够
- 是否遇到异常: 否

**操作**：向Master Agent报告

**汇报内容**：
- problem_id:
- solution_method_type:
- 局部(tell,hint)对数量:
- 全局(tell,hint)对数量:
- 是否发现新维度:
- **拓扑分类是否有进化建议**:
- 是否遇到异常:

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
