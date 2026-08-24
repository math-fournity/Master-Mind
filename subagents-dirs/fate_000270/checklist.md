# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000270
- **文件路径**: subagents-dirs/fate_000270/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396380（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000270/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let F be a field and f(x) ∈ F[x] be irreducible. K is a splitting field for f over F. Suppose ∃α ∈ K such that both α and α+1 are roots of f. Prove ∃ intermediate field E between K and F with [K:E] = char(F).
- 解答核心思路（1-2句话）：α和α+1同为不可约多项式f的根，推出存在F-自同构σ使σ(α)=α+1；迭代σ得σⁿ(α)=α+n，由根有限推出char(F)=p>0且σ阶为p；由Galois基本定理，固定域E=K^⟨σ⟩满足[K:E]=p=char(F)。
- 解答关键步骤列表：
  1. f不可约且α是根 → f是α在F上的极小多项式
  2. α+1也是f的根 → 存在F-嵌入σ: F(α)→K使σ(α)=α+1
  3. K是分裂域 → σ延拓为Gal(K/F)中的自同构
  4. 迭代σ: σⁿ(α)=α+n，f根有限 → ∃n>0使n·1=0 → char(F)=p>0（素数）
  5. σ≠id且σᵖ=id → σ的阶恰为p
  6. 取E=K^⟨σ⟩（⟨σ⟩的固定域），由Galois基本定理[K:E]=|⟨σ⟩|=p=char(F)

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
| 1 | 纯元认知观察 | 0.7 | 描述这道题的结构：已知条件有哪些？要证明什么？关键数学对象是什么？ | 已知：F是域，f∈F[x]不可约，K是f的分裂域，∃α∈K使α和α+1都是f的根。要证：∃中间域E使[K:E]=char(F)。关键对象：不可约多项式、分裂域、根的关系α与α+1、中间域、域特征。 |
| 2 | 自由列举 | 0.6 | 列出所有可能的方法方向：Galois理论中哪些工具可以连接"根的关系"和"中间域的存在"？ | 方向：①Galois群与自同构（根的置换→自同构）②Galois基本定理（子群↔中间域）③固定域构造④域扩张次数公式⑤极小多项式与根的关系⑥特征p的性质 |
| 3 | 小尝试 | 0.4 | 试一个方向：f不可约且α和α+1都是根，这直接告诉我们什么？能否用极小多项式的性质推出什么？ | f是α在F上的极小多项式。α+1也是f的根，意味着存在F-同构F(α)→F(α+1)把α映到α+1。但可能停在这里，没有进一步构造自同构或利用分裂域延拓。 |
| 4 | 思维操作引导 | 0.3 | 构造自同构σ∈Gal(K/F)使σ(α)=α+1。然后执行一个具体操作：迭代σ，计算σⁿ(α)。当n增大时会发生什么？ | σⁿ(α)=α+n。f只有有限个根，所以∃n>0使σⁿ(α)=α，即n·1=0。因此char(F)=p>0（素数），且σ的阶为p。 |
| 5 | 推进 | 0.3 | 继续推进：现在知道char(F)=p且σ阶为p。如何把这些信息与要证明的结论[K:E]=char(F)联系起来？ | 需要找到一个中间域E使[K:E]=p。σ生成一个p阶循环群⟨σ⟩。如果能用Galois基本定理把⟨σ⟩对应到一个中间域，那个中间域的[K:E]就等于|⟨σ⟩|=p。 |
| 6 | 思维操作引导 | 0.2 | 用Galois基本定理：⟨σ⟩是Gal(K/F)的子群，它对应哪个中间域？这个中间域E满足什么性质？ | E=K^⟨σ⟩（⟨σ⟩的固定域）。由Galois基本定理，[K:E]=|⟨σ⟩|=p=char(F)。E是F和K之间的中间域，满足要求。 |
| 7 | 能量传递引导 | 0.1 | 验证完整证明链：从α和α+1是根出发，经过自同构构造、迭代、Galois对应，最终得到E=K^⟨σ⟩使[K:E]=char(F)。每一步是否都成立？ | 完整链条：①f不可约→f是α的极小多项式 ②α+1是根→∃F-嵌入σ(α)=α+1 ③K分裂域→σ延拓为自同构 ④迭代σ→char(F)=p ⑤σ阶p→⟨σ⟩是p阶子群 ⑥Galois基本定理→E=K^⟨σ⟩使[K:E]=p=char(F)。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 2.6
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
- problem_type: structural_existence
- structure_features: 不可约多项式的根之间存在平移关系(α与α+1)，需利用Galois理论将根的关系转化为自同构，再通过Galois对应转化为中间域的存在性。核心是"根关系→自同构→迭代→特征→固定域"的结构变换链。
- key_objects: 不可约多项式f、分裂域K、根α与α+1、F-自同构σ、循环群⟨σ⟩、固定域E=K^⟨σ⟩、域特征char(F)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["automorphism_construction（从根的平移关系构造自同构）", "iteration_to_periodicity（迭代自同构发现周期性→特征p）", "galois_correspondence（用Galois基本定理将子群对应到中间域）", "structural_transformation（根关系→自同构→固定域的结构变换链）"]
- primary_pattern: galois_correspondence
- knowledge_required: ["不可约多项式与极小多项式", "分裂域的定义与性质", "F-嵌入与自同构的延拓", "Galois群与Galois基本定理", "固定域与子群的对应", "域特征与素特征的性质"]
- key_insight: α和α+1同为不可约多项式的根意味着存在自同构σ(α)=α+1，迭代σ得σⁿ(α)=α+n，由根有限推出char(F)=p且σ阶为p，固定域E=K^⟨σ⟩即为所求。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 根的代数关系（α和α+1同为不可约多项式的根）
- translation_to: Galois理论语言（自同构σ(α)=α+1 → 迭代→特征p → 固定域E=K^⟨σ⟩）
- translation_type: structural_transformation（将根的平移关系结构变换为自同构群的结构，再通过Galois对应变换为中间域的存在性）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: logical_deduction, gap_type: structural_transformation}
- tell_small_concepts: ["irreducible polynomial", "splitting field", "root translation", "automorphism", "iteration to periodicity", "Galois correspondence", "fixed field", "characteristic p"]
- expected_ai_method: logical_deduction（bare AI会尝试直接推理域扩张次数或直接构造中间域，不经过自同构→迭代→Galois对应的变换链）
- correct_method: galois_correspondence（构造自同构σ(α)=α+1，迭代发现char(F)=p，用Galois基本定理取固定域E=K^⟨σ⟩）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 是。structural_existence、logical_deduction、structural_transformation均已存在，完全适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 是。problem_type是抽象级，ai_method_type是抽象级，gap_type是中等级，与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的核心特征是"根关系→自同构→迭代→Galois对应"的多步结构变换链，gap_type=structural_transformation已能捕获。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。

**拓扑进化建议**（如有）：无。当前三维度拓扑分类体系完全适用。

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
| 1 | AI看到不可约多项式、分裂域、两个根α和α+1，但未识别Galois理论结构 | 描述题目结构：已知条件、目标、关键数学对象 | 0.7 | 纯元认知观察 | false | {structural_existence, logical_deduction, structural_transformation} | ["irreducible polynomial", "splitting field", "root relation"] |
| 2 | AI列举方向但可能未识别自同构/Galois对应为关键 | 列出Galois理论中连接根关系与中间域的所有工具 | 0.6 | 自由列举 | false | {structural_existence, enumeration_brute_force, knowledge_gap} | ["Galois group", "automorphism", "intermediate field", "fixed field"] |
| 3 | AI尝试用极小多项式性质但未进一步构造自同构 | f不可约且α,α+1都是根，这直接告诉我们什么？ | 0.4 | 小尝试 | false | {structural_existence, direct_calculation, method_translation} | ["minimal polynomial", "F-isomorphism", "root mapping"] |
| 4 | AI识别F-同构但未想到迭代自同构 | 构造σ(α)=α+1并迭代，计算σⁿ(α) | 0.3 | 思维操作引导 | true | {structural_existence, logical_deduction, knowledge_gap} | ["automorphism iteration", "characteristic", "finite roots"] |
| 5 | AI已知char(F)=p且σ阶p，但未联系到结论 | 如何把这些信息与[K:E]=char(F)联系起来？ | 0.3 | 推进 | false | {structural_existence, logical_deduction, structural_transformation} | ["order of automorphism", "prime characteristic", "cyclic group"] |
| 6 | AI知道σ阶p但未想到用Galois基本定理 | 用Galois基本定理：⟨σ⟩对应哪个中间域？ | 0.2 | 思维操作引导 | true | {structural_existence, logical_deduction, knowledge_gap} | ["fixed field", "Galois correspondence", "fundamental theorem"] |
| 7 | AI已识别固定域E=K^⟨σ⟩，需验证完整链条 | 验证完整证明链每一步是否成立 | 0.1 | 能量传递引导 | false | {structural_existence, logical_deduction, structural_transformation} | ["fixed field verification", "degree equality", "Galois correspondence"] |

**全局tell_hint_pairs详情**：

| # | scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | path_feature | 整个证明路径从根条件到结论 | null | 证明需要非显然的路径：根关系→自同构→迭代→特征→Galois对应→固定域。没有任何单步能揭示完整路径 | 关键结构变换：将根的平移关系翻译为自同构，迭代发现特征，再用Galois对应得到中间域 | 0.5 | high - "根关系→自同构→迭代→Galois对应"的模式可泛化到许多Galois理论问题 | 完整路径从根条件到固定域的变换链在任何单步中都不可见。每步局部看似不同的子问题，但变换链只作为整体才有意义 | {structural_existence, logical_deduction, structural_transformation} | ["automorphism construction", "iteration to periodicity", "Galois correspondence", "fixed field"] |
| 2 | implicit | char(F)>0不是给定条件而是需要推导的 | "Q4" | 题目未声明char(F)>0，但这隐含必需且必须从根条件推导。特征从迭代自同构中涌现 | 迭代σ得σⁿ(α)=α+n，f根有限→∃n使n·1=0→char(F)=p>0 | 0.4 | medium - "从自同构周期性推导域特征"的模式专涉及根平移的问题 | char(F)必须为正这一事实在题目中未声明，只有在构造并迭代自同构后才涌现。在读题的局部视角中，这一要求不可见 | {structural_existence, logical_deduction, knowledge_gap} | ["positive characteristic", "automorphism periodicity", "finite roots constraint"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI大概率会尝试直接构造中间域E或直接计算[K:E]，不经过"根关系→自同构→迭代→特征→Galois对应"的变换链。可能犯的具体错误：①只利用极小多项式性质但不构造自同构 ②不知道迭代自同构来发现char(F)>0 ③不知道用Galois基本定理的固定域构造 ④试图用域扩张次数公式直接计算而非通过Galois对应
- suitable_for_poc: ["POC-VMS-hint-injection（验证hint端：注入自同构构造+迭代+Galois对应的脉络能否引导AI完成证明）", "POC-VMS-tell-detection（验证tell端：能否从AI的thinking中检测到'未想到迭代自同构'和'未想到Galois对应'的分叉信号）"]
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
- [x] answer（**⚠ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
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
2. 更新`problem_extraction_progress`集合中`_key="396380"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000270"
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
    '_key': '396380',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000270',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000270')
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
- problem_id: fate_000270
- solution_method_type: galois_correspondence
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。当前三维度拓扑分类体系（problem_type/ai_method_type/gap_type）完全适用，已有值structural_existence/logical_deduction/structural_transformation/knowledge_gap等均能准确描述此题。
- 是否遇到异常: 否。Lean文件中proof为sorry（无解答），但数学证明已从题目条件完整推导。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
