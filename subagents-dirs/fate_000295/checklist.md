# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000295
- **文件路径**: subagents-dirs/fate_000295/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396405（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000295/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设M是R-模。M是平坦的当且仅当以下条件成立：若P是有限展示R-模，f: P → M是R-线性映射，则存在有限自由R-模F及模映射h: P → F, g: F → M使得f = g∘h。
- 解答核心思路（1-2句话）：利用Lazard定理（平坦模=自由模的滤余极限）结合有限展示模到滤余极限的映射必通过某一项分解的性质，双向证明。
- 解答关键步骤列表：
  1. 正向（平坦→分解性质）：M平坦 ⟹ M = lim→ F_i（Lazard定理，F_i为有限自由模）；P有限展示 ⟹ Hom(P, -)与滤余极限交换 ⟹ f: P→M通过某个F_i分解
  2. 反向（分解性质→平坦）：分解性质 ⟹ M可表为自由模的滤余极限（所有P→M的分解给出滤系统）⟹ M平坦（Lazard逆定理：自由模滤余极限=平坦模）
  3. 关键引理：有限展示模P满足Hom(P, -)与滤余极限交换——这是连接"有限展示"与"滤余极限分解"的桥梁

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
| 1 | 纯元认知观察 | 0.8 | 请描述这道题的结构：它在断言什么？等价式的两边分别是什么条件？关键的数学对象有哪些？ | 这是一个iff命题。左边：M是平坦R-模（即-⊗_R M保持正合性）。右边：每个从有限展示模P到M的线性映射f都可通过有限自由模F分解（f = g∘h）。关键对象：R-模M、有限展示模P、有限自由模F、R-线性映射f、分解映射h和g。 |
| 2 | 自由列举 | 0.7 | 列举你所知道的所有平坦模的等价刻画或相关定理，特别是涉及自由模、滤余极限、理想等方向的。 | (1) M平坦 ⟺ 对所有有限生成理想I，I⊗M→M单射；(2) Lazard定理：M平坦 ⟺ M是自由模的滤余极限；(3) M平坦 ⟺ -⊗M保持正合；(4) 平坦模是挠自由的；(5) 有限展示模P满足Hom(P,-)与滤余极限交换。 |
| 3 | 小尝试 | 0.4 | 尝试直接用平坦模的定义（-⊗M保持正合）来证明正向（平坦→分解性质）。看看能否直接从正合性推出分解。 | 直接用定义难以推出分解。正合性给出的是关于tensor product的信息，而我们需要的是关于Hom的信息。定义方向似乎无法直接给出"通过自由模分解"的结论。需要寻找其他刻画。 |
| 4 | 思维操作引导 | 0.3 | 使用Lazard定理：M平坦当且仅当M是有限自由模的滤余极限。结合"有限展示模P满足Hom(P, -)与滤余极限交换"这一性质，证明正向方向。 | 正向：M平坦 ⟹ M = lim→ F_i（Lazard定理，F_i为有限自由模）。给定f: P→M，P有限展示，由Hom(P, -)与滤余极限交换，f通过某个F_i分解：f = g_i ∘ h_i，其中h_i: P→F_i是自然映射的分量，g_i: F_i→M是余极限结构映射。取F = F_i即得。 |
| 5 | 推进 | 0.5 | 正向已完成。现在处理反向：假设分解性质成立，如何推出M平坦？提示——能否从分解性质构造一个自由模的滤系统，使M为其余极限？ | 反向思路：对所有有限展示模P和映射f: P→M，分解性质给出F_f和分解f = g_f ∘ h_f。考虑所有这样的分解构成的范畴，以F_f为对象，自然定义态射使M成为其滤余极限。若能证明这是一个滤系统且余极限为M，则由Lazard逆定理得M平坦。 |
| 6 | 思维操作引导 | 0.3 | 具体构造滤系统：对象为所有三元组(P, f, F, h, g)其中f=g∘h，态射为使图表交换的映射。验证这是滤范畴且余极限为M。然后引用Lazard逆定理。 | 构造：指标范畴I的对象为分解(P→F→M)，态射(P₁→F₁→M)→(P₂→F₂→M)为映射u:P₁→P₂和v:F₁→F₂使图表交换。这是滤范畴（任意两个对象有公共上界——取直和）。余极限映射lim→F→M满（因为每个f都分解），且由自由模的平坦性，lim→F平坦。由Lazard逆定理，M平坦。 |
| 7 | 能量传递引导 | 0.6 | 两个方向都已建立。正向用Lazard定理+有限展示模的余极限交换性，反向用分解性质构造滤系统再引用Lazard逆定理。请将两个方向整合为完整证明。 | 完整证明：正向——M平坦⟹M=lim→F_i(Lazard)⟹f通过F_i分解(Hom(P,-)与滤余极限交换)。反向——分解性质⟹M=lim→F(构造滤系统)⟹M平坦(Lazard逆定理)。QED。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.6
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
- problem_type: characterization（等价刻画——证明一个代数性质等价于一个分解性质）
- structure_features: 双向蕴含证明（iff）；正向用已知定理降维+函子性质；反向用构造性方法建立滤系统再引用逆定理
- key_objects: R-模M、平坦模、有限展示模P、有限自由模F、R-线性映射、滤余极限、Lazard定理

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [定理引用降维, 函子性质利用, 构造性证明, 滤系统构造, 双向蕴含]
- primary_pattern: 定理引用降维（用Lazard定理将"平坦性"翻译为"滤余极限"语言，再用函子性质连接）
- knowledge_required: [平坦模定义, Lazard定理, 有限展示模, 滤余极限, Hom函子与滤余极限交换性, 自由模的平坦性]
- key_insight: 平坦性⟺滤余极限（Lazard定理）是桥梁——将"通过自由模分解"这个看似关于Hom的条件翻译为"M是自由模的滤余极限"这个关于余极限的条件

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 平坦模的张量积定义语言（-⊗M保持正合）
- translation_to: 滤余极限与Hom函子语言（M=lim→F_i, Hom(P,-)与滤余极限交换）
- translation_type: 结构翻译（将代数性质翻译为范畴论语言，通过Lazard定理作为翻译桥梁）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: logical_deduction, gap_type: knowledge_gap}
- tell_small_concepts: [平坦模, 有限展示模, 滤余极限, Lazard定理, Hom函子交换性, 自由模分解, 滤系统构造]
- expected_ai_method: 直接用平坦模定义（张量积保持正合）尝试推导分解性质，缺乏Lazard定理这一关键知识桥梁
- correct_method: 通过Lazard定理将平坦性翻译为滤余极限语言，正向用Hom(P,-)与滤余极限交换性，反向构造滤系统

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ 可以。problem_type=characterization已有；ai_method_type=logical_deduction已有；gap_type=knowledge_gap已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ 一致，都是抽象级别。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ 足够。这道题的核心gap是知识缺失（Lazard定理），knowledge_gap能准确描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议： 无需进化，现有分类体系足够。

**拓扑进化建议**（如有）：无

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

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对iff命题，识别出两边条件但未识别关键定理桥梁 | 描述题目结构，识别已知/未知 | 0.8 | 纯元认知观察 | false | {characterization, logical_deduction, method_problem_mismatch} | [iff命题, 平坦模, 分解性质, 有限展示模] |
| 2 | AI列出平坦模刻画但可能遗漏Lazard定理 | 列举所有已知平坦模等价刻画 | 0.7 | 自由列举 | false | {characterization, logical_deduction, knowledge_gap} | [平坦模刻画, Lazard定理, 滤余极限, 理想准则] |
| 3 | AI尝试用张量积定义直接推导但无法连接到Hom/分解 | 尝试直接用定义证明正向 | 0.4 | 小尝试 | false | {characterization, direct_manipulation, method_problem_mismatch} | [张量积正合性, Hom, 分解, 方法不匹配] |
| 4 | AI不知道Lazard定理（平坦=自由模滤余极限），知识瓶颈 | 引入Lazard定理+Hom(P,-)与滤余极限交换性 | 0.3 | 思维操作引导 | true | {characterization, logical_deduction, knowledge_gap} | [Lazard定理, 滤余极限, 有限展示模, Hom交换性] |
| 5 | AI需要将有限展示与滤余极限分解连接，需方法翻译 | 推进正向方向，连接有限展示与余极限 | 0.5 | 推进 | false | {characterization, logical_deduction, method_translation} | [有限展示, 滤余极限, Hom交换, 分解映射] |
| 6 | AI需要从分解性质构造滤系统，思维瓶颈——构造性步骤 | 具体构造滤系统并验证滤范畴性质 | 0.3 | 思维操作引导 | false | {characterization, logical_deduction, structural_transformation} | [滤系统构造, 滤范畴, 直和上界, 余极限映射] |
| 7 | AI已有两个方向，需整合为完整证明 | 整合两个方向完成证明 | 0.6 | 能量传递引导 | false | {characterization, logical_deduction, method_translation} | [正向证明, 反向证明, Lazard定理, 完整整合] |

**全局pairs详情**：

Global pair 1 (path_feature):
- scope_type: path_feature
- scope: 整个证明路径——从平坦模定义到Lazard定理翻译到双向证明
- observation_point: null
- tell: 证明路径的关键特征是"通过Lazard定理进行语言翻译"——将张量积语言翻译为滤余极限语言，这个翻译桥接了iff的两边
- hint: 识别到平坦模问题时应首先考虑Lazard定理作为翻译桥梁，而非直接用定义
- hint_level: 0.4
- generalizability: "high — 适用于所有涉及平坦模刻证的题目，Lazard定理是标准桥梁"
- why_not_visible_locally: "在局部步骤中，AI看到的是iff的两边各自需要证明，无法从单个方向看出需要Lazard定理作为翻译桥梁。只有从完整路径视角才能看到'张量积语言→滤余极限语言'的翻译是贯穿两边的核心操作。"
- tell_topology: {characterization, logical_deduction, method_translation}
- tell_small_concepts: [Lazard定理, 语言翻译, 张量积到滤余极限, 桥梁定理]

Global pair 2 (implicit):
- scope_type: implicit
- scope: 分解性质与滤余极限之间的隐含等价
- observation_point: Q5
- tell: 分解性质隐含地等价于"M是自由模的滤余极限"——这个等价不是显然的，需要通过构造滤系统来揭示
- hint: 分解性质不仅仅是关于Hom的条件，它实际上等价于M是自由模的滤余极限，这是Lazard定理的另一面
- hint_level: 0.3
- generalizability: "medium — 适用于涉及Lazard定理变体的题目，但构造滤系统的具体方法因题而异"
- why_not_visible_locally: "在R5的局部步骤中，AI看到的是'分解性质→构造滤系统→M平坦'的线性推理，但'分解性质等价于M是自由模滤余极限'这个隐含等价关系不是任何单步推理的直接结论，而是整个反向证明的结构性洞察。"
- tell_topology: {characterization, logical_deduction, structural_transformation}
- tell_small_concepts: [分解性质, 滤余极限等价, 隐含等价, 滤系统构造]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI很可能不知道Lazard定理，会尝试直接用平坦模的张量积定义推导分解性质，在正向方向卡住。即使知道Lazard定理，反向方向构造滤系统也需要创造性思维，AI可能无法自行想到构造方法。
- suitable_for_poc: ["POC-VMS-8 hint端验证——测试注入Lazard定理hint后AI能否完成证明", "POC-VMS-9 tell端验证——测试AI在R3走错路（直接用定义）后系统能否识别knowledge_gap并注入Lazard定理", "知识瓶颈识别实验——测试系统在R2自由列举阶段能否检测AI遗漏Lazard定理"]
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
2. 更新`problem_extraction_progress`集合中`_key="396405"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000295"
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
    '_key': '396405',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000295',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000295')
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
- problem_id: fate_000295
- solution_method_type: logical_deduction（通过Lazard定理进行语言翻译的双向证明）
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature + 1个implicit）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有分类体系（characterization/logical_deduction/knowledge_gap等）足够覆盖
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
