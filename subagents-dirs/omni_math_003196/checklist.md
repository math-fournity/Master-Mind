# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003196
- **文件路径**: subagents-dirs/omni_math_003196/problem.lean
- **来源**: AoPS omni_math (putnam)
- **ArangoDB progress记录_key**: 333074（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003196/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：For a nonnegative integer k, let f(k) be the number of ones in the base 3 representation of k. Find all complex numbers z such that sum_{k=0}^{3^{1010}-1} (-2)^{f(k)} (z+k)^{2023} = 0.
- 解答核心思路（1-2句话）：利用生成函数 P_n(x) = sum (-2)^{f(k)} x^k = prod (x^{3^j}-1)^2 在 x=1 处有 2n 阶零点，使得幂和 sum (-2)^{f(k)} k^j 在 j<2n 时为零，将2023次幂的和降为z的3次多项式，再求解三次方程。
- 解答关键步骤列表：
  1. 建立生成函数恒等式：sum_{k=0}^{3^n-1} (-2)^{f(k)} x^k = prod_{j=0}^{n-1} (x^{2*3^j} - 2x^{3^j} + 1) = prod (x^{3^j}-1)^2，用归纳法证明（利用 f(3^{n-1}+k)=f(k)+1, f(2*3^{n-1}+k)=f(k)）
  2. 注意 P_n(x) = prod (x^{3^j}-1)^2 在 x=1 处有 2n 阶零点
  3. 通过 falling factorial / Stirling 数联系：sum (-2)^{f(k)} k^j = 0 for j < 2n（因为 P_n^{(i)}(1)=0 for i<2n）
  4. 用二项式定理展开 (z+k)^{2023}，只有 j>=2n=2020 的项存活，得到z的3次多项式
  5. 做中心化替换 w = z + (3^{1010}-1)/2，求解三次方程 w^3 + c*w = 0
  6. 得到三个根：w=0 和 w = ±(sqrt(9^{1010}-1)/4)i，即 z = -(3^{1010}-1)/2 和 z = -(3^{1010}-1)/2 ± (sqrt(9^{1010}-1)/4)i

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 观察这个求和式的结构：sum_{k=0}^{3^{1010}-1} (-2)^{f(k)} (z+k)^{2023} = 0。其中f(k)是k的三进制表示中1的个数。你能识别出这个表达式的哪些结构特征？已知量、未知量、关键约束分别是什么？ | 已知：f(k)定义（三进制中1的个数），求和范围0到3^{1010}-1，权重(-2)^{f(k)}，幂次2023。未知：复数z满足方程。关键约束：求和范围极大（3^{1010}项），权重与三进制表示相关，幂次2023与2*1010=2020接近。 |
| 2 | 自由列举 | 0.7 | 面对这样一个包含3^{1010}项的巨大求和，你能想到哪些可能的化简或变换方向？请列出所有你能想到的方法。 | 可能方向：1) 直接计算（不可行，项数太大）；2) 利用f(k)的三进制结构寻找递推；3) 生成函数方法 sum (-2)^{f(k)} x^k；4) 对称性分析（z的平移）；5) 二项式展开(z+k)^{2023}分离z和k；6) 数论性质分析(-2)^{f(k)}的分布。 |
| 3 | 小尝试 | 0.4 | 尝试用二项式定理展开(z+k)^{2023}，看看能否分离z和k的部分。这个方向能走多远？ | (z+k)^{2023} = sum_{j=0}^{2023} C(2023,j) z^{2023-j} k^j，所以原式 = sum_{j=0}^{2023} C(2023,j) z^{2023-j} * S_j，其中S_j = sum_{k=0}^{3^{1010}-1} (-2)^{f(k)} k^j。需要计算S_j。但S_j直接计算不可行。需要找到S_j的结构性质。 |
| 4 | 思维操作引导 | 0.3 | 考虑生成函数 P_n(x) = sum_{k=0}^{3^n-1} (-2)^{f(k)} x^k。利用f(k)的三进制递推性质 f(3^{n-1}+k)=f(k)+1 和 f(2*3^{n-1}+k)=f(k)，能否将P_n(x)分解为乘积形式？ | 将求和按k的三进制首位分组：k在[0,3^{n-1})、[3^{n-1},2*3^{n-1})、[2*3^{n-1},3^n)三段。第一段贡献P_{n-1}(x)，第二段贡献-2*x^{3^{n-1}}*P_{n-1}(x)，第三段贡献x^{2*3^{n-1}}*P_{n-1}(x)。所以P_n(x) = P_{n-1}(x)(1 - 2x^{3^{n-1}} + x^{2*3^{n-1}}) = P_{n-1}(x)(x^{3^{n-1}}-1)^2。归纳得P_n(x) = prod_{j=0}^{n-1} (x^{3^j}-1)^2。 |
| 5 | 推进 | 0.5 | P_n(x) = prod_{j=0}^{n-1} (x^{3^j}-1)^2 在x=1处的零点阶数是多少？这如何联系到幂和S_j = sum (-2)^{f(k)} k^j 的性质？ | 每个因子(x^{3^j}-1)在x=1处有1阶零点（导数为3^j≠0），平方后为2阶。n个因子共2n阶零点。所以P_n^{(i)}(1)=0 for i<2n。而P_n^{(i)}(1) = sum (-2)^{f(k)} k(k-1)...(k-i+1) = sum (-2)^{f(k)} k^{\underline{i}}。通过Stirling数，k^j是k^{\underline{0}}到k^{\underline{j}}的线性组合，所以S_j=0 for j<2n=2020。 |
| 6 | 思维操作引导 | 0.2 | 现在知道S_j=0 for j<2020。在二项式展开中只有j=2020,2021,2022,2023的项存活。做中心化替换 w = z + (3^{1010}-1)/2 后，这个关于w的多项式是什么形式？如何求根？ | 存活项给出z的3次多项式。中心化后利用对称性（sum的范围关于(3^{1010}-1)/2对称），多项式变为w^3 + c*w = 0的形式（无w^2项）。计算c需要S_{2020}和S_{2021}的值，可从P_n在x=1处的Taylor展开得到。最终c = (9^{1010}-1)/16，根为w=0和w=±sqrt(9^{1010}-1)/4 * i。 |
| 7 | 能量传递引导 | 0.6 | 你已经完成了从巨大求和到三次方程的完整降维。确认最终答案，并验证这三个复数确实满足原方程。 | 最终答案：z = -(3^{1010}-1)/2 和 z = -(3^{1010}-1)/2 ± (sqrt(9^{1010}-1)/4)i。验证：w=0对应实根，两个虚根对应w^2 = -(9^{1010}-1)/16。整个推导链条完整：生成函数分解→零点阶数→幂和消失→降次→中心化→求根。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.4+0.3+0.5+0.2+0.6 = 3.5
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
- structure_features: 巨大加权幂和（3^{1010}项），权重(-2)^{f(k)}由三进制表示决定，幂次2023与2*1010=2020接近，求复数z使和为零。核心结构是生成函数的乘积分解与高阶零点。
- key_objects: [三进制表示中1的个数f(k), 生成函数P_n(x), 乘积分解prod(x^{3^j}-1)^2, 零点阶数2n, 幂和S_j, 二项式展开, 中心化替换w=z+(3^n-1)/2, 三次方程]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [结构识别——识别(-2)^{f(k)}来自乘积结构, 生成函数方法——将求和转化为多项式, 零点分析——利用高阶零点消灭低次幂和, 降维——从2023次降到3次, 对称中心化——利用求和范围的对称性消去二次项]
- primary_pattern: 生成函数零点降维
- knowledge_required: [三进制表示与f(k)的递推性质, 生成函数与多项式乘积分解, 多项式零点阶数与导数的关系, falling factorial与Stirling数, 二项式定理, 对称性中心化]
- key_insight: 生成函数P_n(x)=prod(x^{3^j}-1)^2在x=1处有2n阶零点，使得所有j<2n的幂和S_j为零，从而将2023次幂的巨大求和降为z的3次方程。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接幂和计算（对3^{1010}项求和）
- translation_to: 生成函数零点分析（乘积分解→零点阶数→幂和消失→降次）
- translation_type: structural_transformation（将加法结构翻译为乘法结构，再利用零点性质）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [三进制表示, 生成函数, 乘积分解, 高阶零点, 幂和消失, 降维, 中心化, 三次方程]
- expected_ai_method: bare AI会尝试直接计算或寻找数值模式，无法处理3^{1010}项的求和，可能尝试小的n值归纳但难以发现生成函数的乘积分解
- correct_method: 生成函数乘积分解→零点阶数分析→幂和消失→二项式降次→中心化求根

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
- [x] 当前拓扑分类是否够用——这道题的problem_type(characterization)/ai_method_type(direct_calculation)/gap_type(structural_transformation)能归入已有的拓扑类别
- [x] 粒度是否一致——标注值与已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

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

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会尝试直接计算或对小的n值做归纳，但难以发现生成函数的乘积分解这一关键步骤。即使想到生成函数，也可能无法将零点阶数与幂和联系起来。3^{1010}的规模使得任何直接方法都不可行。
- suitable_for_poc: [tell端验证——生成函数分解是关键知识瓶颈tell, hint端验证——结构变换hint的有效性, 降维能力测试——测试AI能否从巨大求和识别降维路径]
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
2. 更新`problem_extraction_progress`集合中`_key="333074"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003196"
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
    '_key': '333074',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003196',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003196')
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
- problem_id: omni_math_003196
- solution_method_type: generating_function_zero_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类足够
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
