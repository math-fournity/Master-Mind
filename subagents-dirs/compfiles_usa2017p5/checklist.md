# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2017p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2017P5.lean
- **来源**: USA 2017 P5
- **ArangoDB progress记录_key**: 329472（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2017P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Determine the set of positive real numbers c such that there exists a labeling of the lattice points in ℤ² with positive integers for which: (1) only finitely many distinct labels occur, and (2) for each label i, the distance between any two points labeled i is at least cⁱ.
- 解答核心思路（1-2句话）：答案是 (0, √2)。上界用squeeze argument证明 c ≥ √2 时不可能（2^n×2^n方格中必然出现超过任意固定上界的标签），下界用递归奇偶标号构造证明 c < √2 时可行。
- 解答关键步骤列表：
  1. 识别 √2 为格点最小非零距离（单位正方形对角线），是临界阈值
  2. 上界（c = √2 不可能）：square_squeeze' 引理——对 2^n×2^n 方格归纳，证明存在标签 > 2n；归纳中分两种情况（两个大标签点的相对位置），用排除原理（exclusion lemma：靠近某标签的点不能共享该标签）
  3. 上界推广（c > √2）：c > √2 时 cⁱ > √2ⁱ，√2 的反例直接适用
  4. 下界（c < √2 构造）：递归奇偶标号——坐标和为奇数→标签1，两坐标均奇→标签2，两坐标均偶→递归到 (a/2, b/2) 标签为 2+递归值
  5. 构造验证：标签数有限（≤ 2*limit+1），距离条件满足（c < √2 蕴含 cⁱ < √2ⁱ，而构造保证 √2ⁱ ≤ dist）

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
| 1 | 纯元认知观察 | 0.3 | 请描述这道题的结构：我们要确定什么？已知条件是什么？约束是什么？ | 我们要确定所有正实数c的集合，使得存在ℤ²上用正整数的标号，满足：(1)只有有限个不同标签，(2)同一标签i的任意两点距离≥cⁱ。这是一个参数刻画问题——找到使某种组合结构存在的参数范围。 |
| 2 | 自由列举 | 0.5 | 列出所有可能帮助确定c范围的方向和思路。特别地，格点之间的距离有什么特殊性质？ | 方向包括：尝试具体c值看是否可行；分析格点最小距离（相邻格点距离为1，对角为√2）；考虑鸽巢原理在有限标签中的作用；尝试构造显式标号；考虑c很大或很小时的极端情况。格点距离的最小非零值是1（水平/垂直相邻）和√2（对角相邻）。 |
| 3 | 小尝试 | 0.4 | 试一下：c=1时能否构造一个满足条件的标号？c=√2呢？ | c=1时，可以用棋盘染色（坐标和奇偶性）给标签1，距离≥√2>1=1¹，但需要多个标签。c=√2时，棋盘染色给标签1恰好满足距离≥√2=√2¹，但更高标签的要求√2ⁱ增长很快，可能难以在有限标签内满足所有点。直觉上√2可能是临界值。 |
| 4 | 思维操作引导 | 0.6 | 关键操作：将注意力集中到√2作为格点最小非零距离的几何意义。为什么√2是自然的临界值？如果c=√2，标签i要求同标签点距离≥√2ⁱ，这意味着什么？ | √2是格点中"对角相邻"的距离，也是棋盘上同色格之间的最小距离。c=√2时，标签1要求距离≥√2（恰好是棋盘同色最小距离），标签2要求≥2，标签3要求≥2√2。关键洞察：标签越大要求间距越大，但有限标签意味着有限个距离要求，而ℤ²是无限的——如果标签数有限，某些标签必须覆盖无限多点，但大标签的距离要求可能无法满足。 |
| 5 | 推进 | 0.5 | 推进上界方向：对于c=√2，尝试证明任何有限标号都不可能。提示——考虑2^n×2^n的方格，用归纳法证明其中必然存在标签超过2n的点。 | 核心思路（squeeze argument）：在2^n×2^n方格中归纳。基础n=0：1个点标签>0。归纳步：在2^(n+1)×2^(n+1)方格中找到两个大标签点（标签≥2n+1和≥2(n+1)），利用排除原理（靠近大标签的点不能共享该标签），在剩余区域用归纳假设找到标签>2(n+1)的点。排除原理：如果点q在点p的√2^(l p)范围内且q≠p，则l(q)≠l(p)。 |
| 6 | 思维操作引导 | 0.6 | 现在处理下界：对于c<√2，构造一个显式标号。提示——利用坐标的奇偶性递归分解格点。 | 构造递归标号：坐标和为奇数→标签1（棋盘染色，同标签最小距离=√2，c<√2所以c¹<√2≤dist✓）；两坐标均奇→标签2（1/4稀疏格，同标签最小距离=2，c²<2✓）；两坐标均偶→递归到(a/2,b/2)，标签=2+递归值。标签数≤2*limit+1有限。距离验证：归纳证明同标签点距离≥√2^(标签值)>c^(标签值)。 |
| 7 | 能量传递引导 | 0.7 | 综合以上两个方向，写出完整结论。上界证明c≥√2不可能，下界构造证明c<√2可行，答案是什么？ | 答案是(0,√2)。上界：c=√2时squeeze argument证明任何有限标号在足够大的方格中必然出现超过标签上界的标签，矛盾；c>√2时√2的反例直接适用。下界：c<√2时递归奇偶标号给出有限标签且距离条件满足。因此解集为(0,√2)。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 3.6
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
- problem_type: characterization
- structure_features: 参数刻画问题——确定使某种组合结构（有限标号+距离约束）存在的参数c的范围。双向证明：上界用不可能性论证（squeeze argument），下界用显式构造。关键阈值√2来自格点几何（最小非零距离）。
- key_objects: ["格点 ℤ²", "正整数标号 labeling", "距离函数 dist", "参数 c", "解集 (0,√2)", "2^n×2^n 方格", "递归奇偶标号"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["参数阈值识别", "几何-组合连接（格点最小距离→临界值）", "squeeze argument（归纳+鸽巢）", "排除原理", "递归构造", "奇偶分解", "双向证明（上界+下界）"]
- primary_pattern: 几何-组合连接（从格点几何性质识别临界阈值，再用组合论证和构造分别处理两个方向）
- knowledge_required: ["格点距离性质", "鸽巢原理", "数学归纳法", "棋盘染色", "递归构造", "√2的几何意义"]
- key_insight: √2是格点最小非零距离（对角相邻），这自然成为标号距离约束的临界阈值——c=√2时squeeze argument迫使标签无界增长，c<√2时递归奇偶标号恰好满足条件

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 参数枚举（逐个测试c值是否可行）
- translation_to: 几何-组合结构论证（从格点几何识别临界阈值，用squeeze argument和递归构造处理两个方向）
- translation_type: method_translation（从枚举试错翻译到结构化论证：识别几何阈值→不可能性论证+显式构造）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["lattice_minimum_distance", "sqrt2_threshold", "squeeze_argument", "exclusion_principle", "recursive_parity_labeling", "pigeonhole_on_squares"]
- expected_ai_method: 逐个测试c值（枚举brute force），尝试构造或否定具体c值，不识别√2的几何意义
- correct_method: 从格点几何识别√2为临界阈值，上界用squeeze argument（归纳+排除原理），下界用递归奇偶标号构造

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 可以。characterization已有，enumeration_brute_force已有，structural_transformation已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 一致。都是中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 足够。这道题的独特性在于"几何-组合连接"作为key_insight，但这通过small_concepts和thinking_patterns已经能区分，不需要新拓扑维度。
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类完全够用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到参数刻画问题但未识别格点几何的特殊角色 | 描述题目结构，识别已知/未知 | 0.3 | 纯元认知观察 | false | {characterization, direct_calculation, method_problem_mismatch} | ["parameter_set_determination", "lattice_labeling", "distance_constraint"] |
| 2 | AI列举方向但未连接格点最小距离到临界阈值 | 列出所有可能方向，特别关注格点距离性质 | 0.5 | 自由列举 | false | {characterization, enumeration_brute_force, search_space_estimation} | ["approach_enumeration", "lattice_geometry", "distance_threshold"] |
| 3 | AI试具体c值但未识别√2的结构性角色 | 试c=1和c=√2，感受临界值 | 0.4 | 小尝试 | false | {characterization, case_by_case, method_problem_mismatch} | ["specific_value_testing", "minimum_lattice_distance", "parity_structure"] |
| 4 | AI需要连接√2作为格点最小距离到标号约束 | 将注意力集中到√2的几何意义 | 0.6 | 思维操作引导 | true | {characterization, direct_calculation, knowledge_gap} | ["lattice_minimum_distance", "sqrt2_threshold", "geometric_constraint"] |
| 5 | AI需要构造squeeze argument的归纳证明 | 推进上界方向，用2^n×2^n方格归纳 | 0.5 | 推进 | false | {characterization, logical_deduction, structural_transformation} | ["squeeze_argument", "pigeonhole_principle", "induction_on_squares", "exclusion_principle"] |
| 6 | AI需要构造递归奇偶标号 | 利用坐标奇偶性递归分解格点 | 0.6 | 思维操作引导 | false | {characterization, direct_manipulation, method_translation} | ["recursive_labeling", "parity_decomposition", "coordinate_scaling", "distance_verification"] |
| 7 | AI需要综合两个方向得出完整结论 | 综合上界和下界，写出答案 | 0.7 | 能量传递引导 | false | {characterization, logical_deduction, method_translation} | ["bidirectional_proof", "threshold_characterization", "solution_set"] |

**全局tell_hint_pairs**：

Global 1 (path_feature):
- scope_type: "path_feature"
- scope: "整个证明路径——从识别√2为临界阈值到双向证明"
- observation_point: null
- tell: "答案(0,√2)的完整证明路径需要同时看到：(1)√2是格点最小非零距离的几何事实，(2)这个几何事实如何转化为squeeze argument的上界论证，(3)递归奇偶标号如何利用c<√2的间隙构造下界。三个部分缺一不可。"
- hint: "先从格点几何识别√2为临界阈值，然后分别用squeeze argument（上界）和递归奇偶标号（下界）处理两个方向"
- hint_level: 0.7
- generalizability: "high——参数刻画问题中'从几何/结构性质识别临界阈值'的模式可泛化到许多组合存在性问题"
- why_not_visible_locally: "在局部视角中，AI可能分别看到格点距离性质、鸽巢原理、递归构造等组件，但无法看到它们如何组合成完整的双向证明——特别是√2同时作为上界论证的核心参数和下界构造的间隙边界，这个双重角色只有在完整路径中才可见"
- tell_topology: {problem_type: "characterization", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["lattice_minimum_distance", "sqrt2_threshold", "squeeze_argument", "recursive_parity_labeling", "bidirectional_proof"]

Global 2 (implicit):
- scope_type: "implicit"
- scope: "squeeze argument的归纳结构中蕴含的不可能性"
- observation_point: "R5"
- tell: "squeeze argument的归纳结构蕴含一个深层信息：在2^n×2^n方格中，标签必须超过2n——这不仅仅是一个引理，而是'有限标签无法覆盖无限格点'这一根本张力的具体化。排除原理（靠近大标签的点不能共享该标签）是这个张力释放的机制。"
- hint: "在归纳的每一步，利用排除原理将大标签点周围的区域'排除'，迫使剩余区域中出现更大的标签——这就是'挤压'的本质"
- hint_level: 0.6
- generalizability: "medium——squeeze argument模式可泛化到其他'有限资源覆盖无限空间'的不可能性证明，但排除原理的具体形式依赖于距离约束的结构"
- why_not_visible_locally: "在R5的局部视角中，AI看到的是归纳步骤的机械操作（找两个大标签点、用排除原理、在剩余区域归纳），但看不到的是'挤压'的动态——每一步归纳都在缩小可用区域同时迫使标签增长，这个动态只有在追踪整个归纳链时才可见"
- tell_topology: {problem_type: "characterization", ai_method_type: "logical_deduction", gap_type: "structural_transformation"}
- tell_small_concepts: ["squeeze_argument", "exclusion_principle", "induction_on_squares", "finite_vs_infinite_tension"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI大概率会尝试枚举具体c值或直接构造标号，但不会识别√2作为格点最小非零距离的几何意义。即使猜到√2是临界值，也难以独立构造squeeze argument的归纳证明（需要在2^n×2^n方格中找两个大标签点并用排除原理）和递归奇偶标号构造。最可能的错误是：给出不完整的答案（如只证明一个方向），或构造的标号不满足距离条件。"
- suitable_for_poc: ["tell_hint_injection", "path_feature_retrieval", "knowledge_bottleneck_identification", "structural_transformation_detection"]
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

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329472"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2017p5"
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
    '_key': '329472',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2017p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2017p5')
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
- problem_id: compfiles_usa2017p5
- solution_method_type: bidirectional_proof
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类（characterization / enumeration_brute_force / structural_transformation等）完全够用，粒度一致。
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
