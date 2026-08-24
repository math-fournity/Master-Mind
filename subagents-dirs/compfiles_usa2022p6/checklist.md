# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2022p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2022P6.lean
- **来源**: USA 2022 P6
- **ArangoDB progress记录_key**: 329497（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2022P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：有2022个用户的社交网络Mathbook，友谊是双向且永久的。从现在起，只有当两个用户至少有2个共同好友时才允许建立新友谊。问：最少需要多少条初始友谊，才能使所有用户最终都能互相成为好友？
- 解答核心思路（1-2句话）：下界通过维护clique cover不变量（每个clique K拥有至少3|K|/2-2条原始边），merge算法终止后所有4-环边共享同一标签，单一大clique给出3n≤2e+4即e≥3031；上界通过构造共享hub边0-1的1010个4-环（1+1010×3=3031条边），两阶段完成。
- 解答关键步骤列表：
  1. 定义合法操作CanAdd：两个非邻接顶点有≥2个共同好友时可加边
  2. 定义Reachable和Completable：图G可通过合法操作序列到达完全图
  3. 下界-定义Cover结构：clique集合C+标签函数ℓ，每个clique K满足theta_bound: 3|K|≤2·(属于K的原始边数)+4
  4. 下界-初始cover：每条边一个K₂，满足theta_bound
  5. 下界-merge引理：4-环abcd的4条边标签不全相同时，合并这些标签对应的clique，新cover仍有效且clique数严格减少
  6. 下界-终止cover：反复merge直到所有4-环边共享同一标签（clique数有限，必然终止）
  7. 下界-终止态分析：Completable意味着G'=⊤（完全图），无合法操作；所有边共享标签K*=全集；theta_bound给出3n≤2e+4
  8. 下界-数值：3×2022≤2e+4 → e≥3031
  9. 上界-构造：边0-1 + 1010个4-环0-1-x_i-y_i-0，共1+1010×3=3031条边
  10. 上界-Phase1：对每个i，加边0-x_i（共同好友1和y_i）和1-y_i（共同好友0和x_i）
  11. 上界-Phase2：Phase1后所有非{0,1}顶点都与0和1相邻，用0和1作为共同好友将2020个顶点连成clique
  12. 答案：3031

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
| 1 | 纯元认知观察 | 0.2 | 描述这道题的结构：有哪些数学对象？约束条件是什么？目标是什么？ | 这是一个图论问题。2022个顶点的简单图，合法操作是在两个非邻接且有≥2个共同邻居的顶点间加边。目标是找到最少的初始边数使得图能通过合法操作序列到达完全图。 |
| 2 | 自由列举 | 0.3 | 列出所有可能用于建立下界的方法 | 直接度数分析、势函数/不变量、归纳法、clique cover、谱方法、极值图论、计数论证... |
| 3 | 小尝试 | 0.4 | 试一个简单的度数论证：如果边太少，能否证明图无法完成？ | 简单度数论证给出弱下界：每个顶点至少需要度数≥2才能获得第一条新边（需要2个共同好友），这给出至少2022条边，远不够紧。问题在于完成过程会增加度数，度数论证无法捕捉动态过程。 |
| 4 | 思维操作引导 | 0.5 | 不要追踪度数，思考完成过程中什么不变量被保持。考虑维护一个clique cover，每个clique K"拥有"原图的一些边，满足3|K|≤2·(拥有的边数)+4 | 可以维护一个cover：clique集合C+标签函数ℓ，每条边属于一个clique，每个clique K满足theta_bound: 3|K|≤2·(属于K的原始边数)+4。初始时每条边一个K₂，满足3×2≤2×1+4=6。当4-环的边标签不同时，可以合并这些clique，新clique仍满足theta_bound。 |
| 5 | 推进 | 0.6 | 发展这个clique cover论证。当完成过程终止时会发生什么？ | merge算法终止时（clique数有限），所有4-环的4条边共享同一标签。如果图可完成，终止态G'=⊤（完全图），无合法操作。所有边共享标签K*=全集，theta_bound给出3n≤2e+4，即e≥(3×2022-4)/2=3031。 |
| 6 | 思维操作引导 | 0.5 | 现在构造一个达到这个下界的图。思考什么结构允许高效完成 | 需要一个图使得完成过程高效。关键想法：用一条共享hub边0-1，每个i创建4-环0-1-x_i-y_i-0。共1+1010×3=3031条边。共享边0-1为Phase 1提供所需的两个共同好友。 |
| 7 | 推进 | 0.6 | 证明这个构造是可完成的。完成的阶段是什么？ | Phase 1：对每个i，加边0-x_i（共同好友1和y_i）和1-y_i（共同好友0和x_i）。Phase 1后所有非{0,1}顶点都与0和1相邻。Phase 2：用0和1作为两个共同好友，将剩余2020个顶点两两连接成clique，完成完全图。 |
| 8 | 能量传递引导 | 0.7 | 验证答案并总结论证 | 下界3n≤2e+4给出e≥3031，构造恰好达到3031条边。答案为3031。核心是clique cover不变量+merge算法终止分析，配合hub边构造的两阶段完成。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
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
- problem_type: discrete_combinatorial
- structure_features: 图完成过程（局部规则：加边需≥2个共同邻居），最小化初始边数使图可完成到完全图。下界用clique cover不变量+merge算法终止分析，上界用hub边构造+两阶段完成。
- key_objects: 简单图(2022顶点), 合法操作CanAdd, Reachable关系, Completable性质, clique cover(Cover结构), theta_bound(3|K|≤2e_K+4), 4-环, merge算法, 终止cover, hub边0-1, 4-环族0-1-x_i-y_i-0

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["potential_function_invariant", "clique_cover_decomposition", "merge_algorithm_termination", "extremal_construction", "phase_based_completion", "hub_edge_design"]
- primary_pattern: potential_function_invariant（clique cover的theta bound是核心不变量）
- knowledge_required: ["图论基础", "clique cover", "势函数/不变量", "4-环结构", "组合计数", "图完成过程", "merge算法"]
- key_insight: 维护clique cover使得每个clique K满足3|K|≤2·(拥有的原始边数)+4；merge算法终止后所有4-环边共享标签，单一大clique=全集，直接给出3n≤2e+4

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_edge_counting（直接计数边数/度数的朴素方法）
- translation_to: clique_cover_invariant（维护clique cover结构+theta bound不变量）
- translation_type: structural_transformation（从直接的边计数转化为结构化的cover维护+merge算法终止分析）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["clique_cover", "theta_bound", "4_cycle_label", "merge_algorithm", "terminal_cover", "potential_invariant", "shared_edge_hub", "phase_completion"]
- expected_ai_method: direct_calculation（bare AI会用直接计数边数/度数的方法，得到弱下界~2022）
- correct_method: clique_cover_invariant（实际方法用clique cover的theta bound不变量+merge算法终止分析）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。discrete_combinatorial/direct_calculation/structural_transformation均已存在且粒度匹配。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。三个维度都是中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。clique cover不变量是structural_transformation的典型实例。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。当前拓扑分类充分覆盖本题。

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
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会用直接度数/边数计数，得到弱下界~2022（每个顶点至少度数2）。不会发现clique cover不变量或theta bound。对上界构造也可能尝试不共享hub边的方案，导致边数过多或无法完成。
- suitable_for_poc: ["tell_detection", "hint_injection", "topology_matching"]
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
2. 更新`problem_extraction_progress`集合中`_key="329497"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2022p6"
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
    '_key': '329497',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2022p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2022p6')
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
- problem_id: compfiles_usa2022p6
- solution_method_type: clique_cover_invariant
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。discrete_combinatorial/direct_calculation/structural_transformation均已存在且粒度匹配，无需进化。
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
