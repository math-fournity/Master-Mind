# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000285
- **文件路径**: subagents-dirs/fate_000285/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396395（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000285/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：If \(R\) is Noetherian and \(M,N\) are finitely generated \(R\)-modules, show that \(\operatorname{Ass}\operatorname{Hom}_R(M,N)=\operatorname{Supp}M\cap\operatorname{Ass}N\), where \(\operatorname{Supp}M\) is the set of all primes containing \(\operatorname{ann}M\). Formal target: `associatedPrimes R (M →ₗ[R] N) = {p | p ∈ associatedPrimes R N ∧ Module.annihilator R M ≤ p}`.
- 解答核心思路（1-2句话）：Lean 文件中的证明体是 `sorry` 占位；数学上采用标准局部化判别。把等式在每个素理想 `p` 处局部化，化为局部环 `(A,m)` 中证明 `m ∈ Ass Hom_A(P,Q)` 当且仅当 `P ≠ 0` 且 `m ∈ Ass Q`。
- 解答关键步骤列表：
  1. 使用有限生成假设得到 `Hom_R(M,N)_p ≃ Hom_{R_p}(M_p,N_p)`，并用 associated primes 的局部判别把全局命题化为局部命题。
  2. 局部环中若 `m` 杀死一个非零同态 `f : P → Q`，则 `f(P)` 中有非零元素被 `m` 杀死，所以 `m ∈ Ass Q`，且 `P ≠ 0`。
  3. 反向若 `P ≠ 0` 且 `m ∈ Ass Q`，取嵌入 `A/m ↪ Q`；由 Nakayama 得到 `Hom_A(P,A/m) ≠ 0`，合成得到被 `m` 杀死的非零同态 `P → Q`。
  4. 将 `M_p ≠ 0` 翻译为 `p ∈ Supp M`，对有限生成模等价于 `Module.annihilator R M ≤ p`，回到题目等式。

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
| 1 | 纯元认知观察 | 0.80 | 先只观察题目结构：等式两边分别是什么对象？要证明哪种逐素理想的等价？ | 目标是集合相等。左边是 `Hom_R(M,N)` 的 associated primes，右边是 `N` 的 associated primes 中同时含 `ann M` 的素理想，即 `Supp M ∩ Ass N`。应按任意素理想 `p` 证明 `p ∈ Ass Hom` iff `p ∈ Ass N` 且 `M` 在 `p` 处非零。 |
| 2 | 自由列举 | 0.70 | 列出证明这类 associated-prime/Hom 等式的标准工具，不急着选路线。 | 可用工具包括：associated primes 的元素/嵌入定义，局部化判别 `p∈Ass X ↔ pR_p∈Ass X_p`，有限生成下 Hom 与 localization 交换，有限生成模的 support 与 annihilator containment 等价，局部环中的 residue field 与 Nakayama。 |
| 3 | 小尝试 | 0.45 | 试一下直接从一个非零同态 `f : M → N` 的 annihilator 出发，看看能走多远。 | 若 `ann(f)=p`，则 `f(M)` 中的非零元素可帮助推出 `p` 与 `N` 的 associated prime 有关；但反向要从 `p∈Ass N` 和 `ann M≤p` 构造一个 annihilator 正好为 `p` 的同态，全局上很不自然，说明直接元素追踪会卡住。 |
| 4 | 思维操作引导 | 0.25 | 把命题在一个素理想 `p` 处局部化：写出需要用的两个局部化事实，并给出局部环中的等价命题。 | 用 `p∈Ass_R X ↔ pR_p∈Ass_{R_p} X_p` 和 `(Hom_R(M,N))_p ≃ Hom_{R_p}(M_p,N_p)`。于是化为局部环 `(A,m)`、有限模 `P,Q` 中的引理：`m∈Ass_A Hom_A(P,Q)` iff `P≠0` 且 `m∈Ass_A Q`。 |
| 5 | 推进 | 0.35 | 证明局部引理的正向：若 `m` 是 `Hom_A(P,Q)` 的 associated prime，会发生什么？ | 存在非零同态 `f:P→Q` 被 `m` 杀死。取 `x` 使 `f(x)≠0`，则对所有 `a∈m`，`a f(x)=(a f)(x)=0`，所以 `Q` 有非零元素被 `m` 杀死，得到 `m∈Ass Q`；同时 `f≠0` 给出 `P≠0`。 |
| 6 | 思维操作引导 | 0.20 | 证明反向时，不要直接猜同态；利用 residue field。若 `P≠0` 且 `m∈Ass Q`，怎样构造被 `m` 杀死的非零 `P→Q`？ | `m∈Ass Q` 给出嵌入 `k=A/m ↪ Q`。由 `P` 有限且非零，Nakayama 给 `P/mP≠0`，选非零 `k`-线性泛函 `P/mP→k` 并提升为非零 `A`-线性映射 `P→k`。与 `k↪Q` 合成得到非零同态 `P→Q`，其值落在 `k` 子模中，故被 `m` 杀死，推出 `m∈Ass Hom(P,Q)`。 |
| 7 | 能量传递引导 | 0.30 | 已有局部引理，收尾：怎样回到原题形式的集合等式？ | 对任意 `p`，局部引理给出 `p∈Ass Hom_R(M,N)` iff `M_p≠0` 且 `p∈Ass_R N`。由于 `M` 有限生成，`M_p≠0` iff `ann_R M≤p`，所以得到 `{p | p∈Ass N ∧ ann M≤p}`，即所需等式。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.05
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R6
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4

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
- problem_type: characterization
- structure_features: 证明两个素理想集合相等；左侧是由 `Hom_R(M,N)` 产生的 associated primes，右侧把 `N` 的 associated primes 与 `M` 的 support/annihilator containment 交叉；有限生成和 Noetherian 假设暗示局部化、Hom-localization、support=V(ann) 三个转换层。
- key_objects: [`R` Noetherian commutative ring, finite `R`-modules `M` and `N`, `M →ₗ[R] N`, `associatedPrimes`, `Module.annihilator R M`, prime ideal `p`, localization `R_p`, local maximal ideal `pR_p`, residue field `R_p/pR_p`]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [`global_to_local_reduction`, `localization_of_invariants`, `replace_set_equality_by_membership_equivalence`, `local_ring_residue_field_construction`, `finite_module_support_translation`]
- primary_pattern: localization_to_local_lemma
- knowledge_required: [`associated primes via annihilators/submodule R/p`, `localization criterion for associated primes over Noetherian rings`, `Hom-localization isomorphism for finite source module`, `support of finite module equals V(annihilator)`, `Nakayama lemma`, `residue field of a local ring`, `finite-dimensional vector-space dual over residue field`]
- key_insight: 全局等式不要直接构造 annihilator 为 `p` 的同态，而是局部化后只需在局部环中构造一个被极大理想杀死的非零同态；这个同态来自 `P → P/mP → k ↪ Q`。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 全局 associated-prime 集合等式 / 直接 annihilator 元素追踪
- translation_to: 逐素理想局部化后的局部环命题 + residue-field 同态构造
- translation_type: global_invariant_to_local_model

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: method_translation}
- tell_small_concepts: [`associatedPrimes`, `Hom_R(M,N)`, `support`, `annihilator containment`, `localization at p`, `Hom-localization`, `local ring`, `residue field`, `Nakayama`]
- expected_ai_method: bare AI 可能尝试直接追踪 `Hom(M,N)` 中某个非零同态的 annihilator，或把 `Ass Hom` 误当成 `Ass N` 的简单子集来做元素级包含证明。
- correct_method: 先逐素理想局部化，把全局集合等式翻译成局部环引理；局部环中用 `P/mP` 和 residue field 构造/识别被极大理想杀死的非零同态。

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
- [x] 当前拓扑分类是否够用——能归入已有的 `characterization / direct_manipulation / method_translation`。
- [x] 粒度是否一致——三项都保持抽象或中等粒度，没有引入“Hom-associated-prime-specific”这种过细类别。
- [x] 是否需要新的拓扑维度——当前三个维度足以区分“集合刻画题中直接操纵失败，需要翻译到局部模型”的 tell。
- [x] 如果发现拓扑分类需要进化，在此写出建议：暂不需要新增顶层类别；可在小概念层保留 `localization`、`residue_field`、`finite_module` 来区分交换代数题。

**拓扑进化建议**（如有）：无；若后续大量交换代数题出现，可考虑在非必填扩展字段记录 `domain_bridge = global_to_local`，但不建议升级为当前三维拓扑的新值。

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
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

**局部pairs摘要**：
1. R1 tell: AI 未把集合等式拆成逐 `p` 的 membership equivalence；hint: 先对任意素理想 `p` 写出左右条件。topology=`(characterization, logical_deduction, structural_transformation)`; small_concepts=[`set ext`, `associatedPrimes`, `annihilator containment`].
2. R2 tell: AI 没有召回 associated primes 与 finite Hom 的标准工具箱；hint: 列出 localization、Hom-localization、support=V(ann)、Nakayama。topology=`(characterization, logical_deduction, knowledge_gap)`; small_concepts=[`localization criterion`, `Hom localization`, `Nakayama`].
3. R3 tell: AI 正在直接追踪 `ann(f)`，反向构造全局同态会变硬；hint: 记录直接法障碍并切向局部化。topology=`(characterization, direct_manipulation, method_problem_mismatch)`; small_concepts=[`ann(f)`, `nonzero hom`, `reverse construction`].
4. R4 tell: AI 尚未把全局素理想问题翻译成局部环问题；hint: 局部化到 `R_p` 并陈述局部引理。topology=`(characterization, direct_manipulation, method_translation)`; small_concepts=[`R_p`, `pR_p`, `Hom-localization`, `local lemma`].
5. R5 tell: AI 已有局部引理但正向不知如何从 `m` 杀同态转到 `Q`；hint: 取 `x` 使 `f(x)≠0` 并评价 `a f`。topology=`(characterization, logical_deduction, structural_transformation)`; small_concepts=[`m-torsion`, `image of f`, `evaluation`].
6. R6 tell: AI 不知道由 `P≠0` 和 `m∈Ass Q` 构造非零 `P→Q`；hint: 用 Nakayama 得到 `P/mP≠0`，选 `P/mP→k`，再合成 `k↪Q`。topology=`(characterization, logical_deduction, knowledge_gap)`; small_concepts=[`Nakayama`, `P/mP`, `residue field`, `linear functional`].
7. R7 tell: AI 有局部结论但没把 `M_p≠0` 转成题面里的 `ann M≤p`；hint: 用有限生成模 `Supp M = V(ann M)` 收尾。topology=`(characterization, logical_deduction, method_translation)`; small_concepts=[`support`, `annihilator`, `finite module`, `set equality`].

**全局pairs摘要**：
1. path_feature: 连续走“直接 annihilator 追踪”路径时，局部每步都像合理元素法，但整条路径暴露反向构造不自然；hint: 从根部换成“逐 `p` 局部化 + 局部环引理”。
2. implicit(Q2/Q4): 有限生成假设并非装饰，它隐含 Hom-localization 与 `Supp=V(ann)`；hint: 主动问“有限生成在哪里使用”。
3. implicit(Q6): `P≠0` 在局部有限模中隐含 `Hom(P,k)≠0`，这需要 Nakayama + residue-field dual；hint: 从 `P/mP` 找非零线性泛函。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: marginal
- bare_ai_error_prediction: bare AI 若熟悉交换代数标准定理可能直接给出局部化证明；否则容易停留在全局元素/annihilator 追踪，尤其在反向从 `p∈Ass N` 与 `ann M≤p` 构造 `Hom(M,N)` 的 associated element 时卡住，或漏用 finite generation 导致 Hom-localization 与 support 翻译不严谨。
- suitable_for_poc: [`tell_detection_global_to_local`, `knowledge_bottleneck_localization`, `implicit_assumption_finite_generation`, `residue_field_construction_hint`, `formal_math_commutative_algebra`]
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
- [x] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
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
- 已写入：`subagents-dirs/fate_000285/profile.json`
- 本地字段校验：通过；7 个局部 pair、3 个全局 pair；`answer` 非空；`knowledge_bottleneck="R6"`、`thinking_bottleneck="R4"` 为字符串；所有全局 pair 的 `why_not_visible_locally` 非空。

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
2. 更新`problem_extraction_progress`集合中`_key="396395"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000285"
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
    '_key': '396395',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000285',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000285')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 写入集合：`problem_profiles/fate_000285`
- 更新progress：`problem_extraction_progress/396395`，`extraction_status=completed`，`schema_version=3`，`profile_doc_id=problem_profiles/fate_000285`，`extracted_by=subagent`
- 验证输出：`入库完成并验证通过: fate_000285, 7 local pairs, 3 global pairs, progress=completed`

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: fate_000285
- solution_method_type: localization_to_local_lemma
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无；现有 `characterization / direct_manipulation / method_translation` 足够，交换代数特征保留在 small concepts。
- 是否遇到异常: Lean 文件证明体为 `sorry`，未提供正式解答；已基于标准交换代数证明重构 profile。入库与验证均成功。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
