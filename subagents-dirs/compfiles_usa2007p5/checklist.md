# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2007p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2007P5.lean
- **来源**: USA 2007 P5
- **ArangoDB progress记录_key**: 329430（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2007P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Prove that for every nonnegative integer n, the number 7^(7^n) + 1 is the product of at least 2n + 3 (not necessarily distinct) primes.
- 解答核心思路（1-2句话）：对n归纳。利用 t^7+1 = (t+1)(t^6-t^5+t^4-t^3+t^2-t+1) 分解，归纳假设给出 x+1 有 ≥2d+3 个素因子；关键是将第二因子 p 改写为 (x+1)^6 - 7x(x^2+x+1)^2，因 7^d 为奇数故 7x = 7^(7^d+1) 是完全平方，从而 p = (a-c)(a+c) 差平方分解，两因子均>1，贡献≥2个素因子。
- 解答关键步骤列表：
  1. 基例 n=0：7^1+1=8=2^3，3个素因子=2·0+3 ✓
  2. 归纳步：令 x=7^(7^d)，则 7^(7^(d+1))+1 = x^7+1 = (x+1)·p
  3. 多项式分解 t^7+1 = (t+1)(t^6-t^5+t^4-t^3+t^2-t+1)
  4. 改写第二因子 p = (x+1)^6 - 7x(x^2+x+1)^2（factor_poly_bn）
  5. 关键观察：7x = 7·7^(7^d) = 7^(7^d+1) = (7^((7^d+1)/2))^2，因7^d为奇数→7^d+1为偶数
  6. 差平方分解：p = ((x+1)^3)^2 - (7^((7^d+1)/2)·(x^2+x+1))^2 = (a₀-c₀)(a₀+c₀)
  7. 验证 a₀-c₀ > 1：因 7^((7^d+1)/2) ≤ x=7^(7^d)，故 a₀-c₀ ≥ (x+1)^3 - x(x^2+x+1) = 2x^2+2x+1 > 1
  8. 两因子均>1→p有≥2个素因子，总计 (2d+3)+2 = 2(d+1)+3 ✓

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
| 1 | 纯元认知观察 | 0.7 | 观察这道题的结构：要证的是对每个非负整数n，7^(7^n)+1至少有2n+3个素因子。2n+3这个界与n的关系是什么？这暗示了什么方法？ | 2n+3随n线性增长，每增加1个n就多2个素因子。这强烈暗示数学归纳法——每步归纳增加恰好2个素因子。 |
| 2 | 自由列举 | 0.8 | 列出所有可能分解7^(7^n)+1的方法。考虑：直接因式分解、分圆多项式、Aurifeuillean分解、归纳+递归结构。 | 可列举：①直接对7^(7^n)+1做数值分解；②利用t^7+1的多项式分解；③分圆多项式φ_14(t)；④Aurifeuillean因子分解；⑤归纳法利用递归结构7^(7^(n+1))+1=(7^(7^n))^7+1。 |
| 3 | 小尝试 | 0.3 | 试一个方向：对多项式 t^7+1 做因式分解，得到什么？然后令 t=7^(7^d) 看看归纳步会发生什么。 | t^7+1=(t+1)(t^6-t^5+t^4-t^3+t^2-t+1)。令x=7^(7^d)，则x^7+1=(x+1)·p，其中p=x^6-x^5+x^4-x^3+x^2-x+1。归纳假设给出x+1有≥2d+3个素因子，但p的素因子数未知。 |
| 4 | 思维操作引导 | 0.4 | 关键操作：将第二因子p改写为 (x+1)^6 - 7x(x^2+x+1)^2。现在观察 7x=7·7^(7^d)=7^(7^d+1)。因为7^d是奇数，7^d+1是偶数，所以7x是完全平方。将p表达为差平方形式。 | 7x=(7^((7^d+1)/2))^2，所以p=((x+1)^3)^2-(7^((7^d+1)/2)·(x^2+x+1))^2=(a₀-c₀)(a₀+c₀)，其中a₀=(x+1)^3, c₀=7^((7^d+1)/2)·(x^2+x+1)。这是Aurifeuillean型差平方分解。 |
| 5 | 推进 | 0.5 | 继续推进：验证a₀-c₀和a₀+c₀都大于1。利用7^((7^d+1)/2) ≤ 7^(7^d)=x来建立不等式。 | a₀+c₀>1显然。对a₀-c₀：因(7^d+1)/2 ≤ 7^d，故c₀ ≤ x·(x^2+x+1)=b₀，于是a₀-c₀ ≥ a₀-b₀=(x+1)^3-x(x^2+x+1)=2x^2+2x+1>1。两因子均>1，各贡献≥1个素因子，p有≥2个素因子。 |
| 6 | 推进 | 0.6 | 组装归纳：归纳假设给出x+1有≥2d+3个素因子，p有≥2个素因子，总计多少？ | (2d+3)+2=2d+5=2(d+1)+3。归纳步完成。 |
| 7 | 能量传递引导 | 0.7 | 验证基例n=0并收尾：7^1+1=8=2^3，有3个素因子=2·0+3。归纳法完整。 | 基例成立，归纳步成立，由数学归纳法对一切非负整数n，7^(7^n)+1至少有2n+3个素因子。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5（R1+R2+R5+R6+R7）
- knowledge_rounds（思维操作引导的轮数）: 1（R4）
- level_sum: 0.7+0.8+0.3+0.4+0.5+0.6+0.7 = 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 归纳结构+代数因式分解；7^(7^n)+1的递归结构7^(7^(n+1))+1=(7^(7^n))^7+1允许每步归纳用t^7+1分解获得2个新素因子；关键在于第二因子的Aurifeuillean型差平方分解
- key_objects: ["7^(7^n)+1", "t^7+1多项式分解", "差平方分解", "素因子计数", "归纳法", "7^d奇偶性"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["mathematical_induction", "algebraic_factorization", "difference_of_squares", "recursive_structure_exploitation", "parity_argument"]
- primary_pattern: algebraic_factorization
- knowledge_required: ["t^7+1多项式分解", "差平方公式a²-c²=(a-c)(a+c)", "素因子分解基本性质", "数学归纳法", "7^d奇偶性（奇数的幂仍为奇数）", "Aurifeuillean因子分解概念"]
- key_insight: 第二因子p=(x+1)^6-7x(x²+x+1)²可做差平方分解，因为7x=7^(7^d+1)是完全平方——7^d为奇数使7^d+1为偶数，这是隐藏在底数7的奇偶性中的关键。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接素因子计数（试图直接对7^(7^n)+1做数值分解并数素因子）
- translation_to: 代数因式分解+归纳法（将计数问题转化为递归分解结构，每步用多项式分解和差平方获得2个新素因子）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["t^7+1_factorization", "difference_of_squares", "Aurifeuillean", "7^d_parity", "induction_2_per_step", "perfect_square_hidden"]
- expected_ai_method: direct_calculation——bare AI会尝试直接计算或数值分解7^(7^n)+1的素因子，无法处理指数增长的大数
- correct_method: algebraic_factorization_induction——用t^7+1多项式分解+归纳法，关键步骤是第二因子的Aurifeuillean型差平方分解

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=inequality_proof, ai_method_type=direct_calculation, gap_type=structural_transformation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新的拓扑维度——三个维度足以区分这道题的tell
- 拓扑进化建议：无。已有分类体系完全覆盖。

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
| 1 | AI面对一个关于素因子计数下界的命题，界2n+3随n线性增长，但AI尚未识别归纳结构 | 观察2n+3与n的关系，线性增长暗示归纳法，每步增加2个素因子 | 0.7 | 纯元认知观察 | false | {inequality_proof, direct_calculation, structural_transformation} | ["growth_rate_2n+3", "prime_factor_count", "induction_hint"] |
| 2 | AI识别出归纳可能但不确定如何分解7^(7^n)+1，列举方向时可能遗漏Aurifeuillean | 列出所有分解方法：直接分解、分圆多项式、Aurifeuillean、归纳+递归结构 | 0.8 | 自由列举 | false | {inequality_proof, enumeration_brute_force, search_space_estimation} | ["factorization_approaches", "cyclotomic", "Aurifeuillean", "induction_structure"] |
| 3 | AI尝试直接数值分解但数太大无法处理，或尝试多项式分解但卡在第二因子 | 试多项式分解t^7+1=(t+1)(t^6-...+1)，令t=7^(7^d)看归纳步 | 0.3 | 小尝试 | false | {inequality_proof, algebraic_identity, method_translation} | ["t^7+1_factorization", "polynomial_identity", "substitution"] |
| 4 | AI已分解出(x+1)·p但不知道p有≥2个素因子，缺乏Aurifeuillean差平方分解的知识 | 将p改写为(x+1)^6-7x(x²+x+1)²，观察7x=7^(7^d+1)是完全平方（7^d奇→7^d+1偶），做差平方分解 | 0.4 | 思维操作引导 | true | {inequality_proof, algebraic_identity, knowledge_gap} | ["difference_of_squares", "perfect_square_7t", "parity_7^d_odd", "Aurifeuillean"] |
| 5 | AI已得到p=(a₀-c₀)(a₀+c₀)但需验证两因子>1，不等式验证方向不明 | 利用(7^d+1)/2≤7^d建立c₀≤b₀，得a₀-c₀≥2x²+2x+1>1 | 0.5 | 推进 | false | {inequality_proof, direct_manipulation, method_problem_mismatch} | ["factor_greater_than_1", "inequality_verification", "a_minus_c_positive"] |
| 6 | AI已证p有≥2素因子但未组装归纳结论 | 组装：归纳假设2d+3 + p的2个 = 2d+5 = 2(d+1)+3 | 0.6 | 推进 | false | {inequality_proof, logical_deduction, method_problem_mismatch} | ["induction_assembly", "counting_prime_factors", "base_case_verification"] |
| 7 | AI有所有部件但需验证基例收尾 | 验证n=0：7^1+1=8=2³，3=2·0+3。归纳完整，证毕 | 0.7 | 能量传递引导 | false | {inequality_proof, logical_deduction, method_problem_mismatch} | ["base_case", "8_equals_2_cubed", "induction_complete"] |

**全局pairs详情**：

1. path_feature型：
- scope: "整个归纳链从n=0到一般n"
- observation_point: null
- tell: 递归结构7^(7^(n+1))+1=(7^(7^n))^7+1允许每步归纳用t^7+1分解+差平方分解恰好获得2个新素因子
- hint: 用归纳法，每步分解t^7+1并将第二因子做差平方分解，获得2个素因子
- hint_level: 0.6
- generalizability: "high——此递归分解+差平方模式适用于任意a^(a^n)+1其中a为奇数>1"
- why_not_visible_locally: "完整递归链——每步一致地通过同一代数恒等式增加恰好2个因子——只有在看到整个归纳结构时才可见。在任意单步中只看到一个分解，看不到它重复并累积的模式。"
- tell_topology: {inequality_proof, algebraic_identity, structural_transformation}
- tell_small_concepts: ["recursive_factorization", "2_primes_per_step", "induction_accumulation"]

2. implicit型：
- scope: "R4中的差平方分解关键步骤"
- observation_point: "R4"
- tell: 恒等式7·7^(7^d)=(7^((7^d+1)/2))²成立因为7^d总为奇数使7^d+1为偶数——这是隐藏的完全平方使差平方成为可能
- hint: 识别7t其中t=7^(7^d)是完全平方，因为7^(7^d+1)=(7^((7^d+1)/2))²，利用7^d的奇偶性
- hint_level: 0.4
- generalizability: "medium——具体适用于a^(a^n)+1形式其中a为奇数，因奇偶论证依赖于a为奇数"
- why_not_visible_locally: "在R4中AI看到表达式(x+1)^6-7x(x²+x+1)²但7x是完全平方这一事实隐藏在代入x=7^(7^d)和7^d的奇偶性之后。需要将代数形式与底数7的数论性质连接起来，这在局部步骤中不可见。"
- tell_topology: {inequality_proof, algebraic_identity, knowledge_gap}
- tell_small_concepts: ["perfect_square_hidden", "parity_7^d_odd", "7t_square_identity"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI很可能正确分解t^7+1=(t+1)(t^6-...+1)并建立归纳框架，但在第二因子p处卡住——不会想到将p改写为(x+1)^6-7x(x²+x+1)²并利用7x是完全平方来做差平方分解。AI可能尝试直接证明p是合数或寻找p的具体素因子，但无法建立一般性的≥2素因子论证。"
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_detection", "structural_transformation_recognition", "aurifeuillean_factorization_hint"]
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
2. 更新`problem_extraction_progress`集合中`_key="329430"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2007p5"
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
    '_key': '329430',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2007p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2007p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2007p5
- solution_method_type: algebraic_factorization_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有分类体系完全覆盖
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
