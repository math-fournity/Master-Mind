# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000147
- **文件路径**: subagents-dirs/omni_math_000147/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 330019（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000147/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：n is interesting if 2018 | d(n). Find all positive integers k such that there exists an infinite AP with common difference k whose terms are all interesting.
- 解答核心思路（1-2句话）：Factor 2018 = 2 × 1009 (1009 prime), decompose 2018|d(n) into two structural cases on prime exponents, construct APs by locking p-adic valuations, prove necessity by obstruction.
- 解答关键步骤列表：
  1. Factor 2018 = 2 × 1009, note 1009 is prime
  2. d(n) = (a1+1)...(at+1), so 2018|d(n) iff either one (ai+1) ≡ 0 mod 2018, or one (ai+1) ≡ 0 mod 1009 and another (aj+1) ≡ 0 mod 2
  3. Sufficiency case (a): v_p(k) ≥ 2018 → set a = p^2017, v_p(a+nk) = 2017 for all n
  4. Sufficiency case (b): v_q(k) ≥ 1009 and v_r(k) ≥ 2 → set a = q^1008 · r, valuations locked
  5. Necessity: if neither condition holds, some AP term is not interesting
  6. Answer: all k with v_p(k) ≥ 2018 for some prime p, or v_q(k) ≥ 1009 and v_r(k) ≥ 2 for distinct primes q, r

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
| 1 | 纯元认知观察 | 0.8 | Describe the problem structure: what is d(n) in terms of prime factorization? What does 2018 \| d(n) require? | d(n) = (a1+1)...(at+1) for n = p1^a1...pt^at. So 2018 \| d(n) means 2018 divides this product. |
| 2 | 自由列举 | 0.7 | List all possible ways 2018 can divide a product of integers. What is the prime factorization of 2018? How does this constrain the factors of d(n)? | 2018 = 2 * 1009, 1009 is prime. So 2018 \| product means either one factor divisible by 2018, or one factor divisible by 1009 and another by 2. |
| 3 | 小尝试 | 0.4 | Try k = p^2018 for a prime p. Can you find a starting point a such that every term a + nk is interesting? Think about what v_p(a+nk) is for all n. | Set a = p^2017. Then a+nk = p^2017(1+nk/p^2017). Since v_p(k) >= 2018, k/p^2017 is divisible by p, so 1+nk/p^2017 ≡ 1 mod p. Thus v_p(a+nk) = 2017 for all n. |
| 4 | 思维操作引导 | 0.3 | 2018 = 2 * 1009. What if no single (ai+1) is divisible by 2018, but the product of two different factors gives 2018? What condition on k does this lead to? | If some (ai+1) divisible by 1009 (ai >= 1008) and another (aj+1) divisible by 2 (aj >= 1), then 2018 \| d(n). For AP: v_q(k) >= 1009 and v_r(k) >= 2 for distinct primes q, r. Set a = q^1008 * r. |
| 5 | 推进 | 0.5 | For necessity, assume neither condition holds. For any starting point a, can you find n such that a + nk is not interesting? | If neither condition holds, the p-adic structure of k is insufficient to lock in required exponents across all terms. Some term will have divisor count not divisible by 2018. |
| 6 | 能量传递引导 | 0.6 | Combine both cases: the answer is all k with v_p(k) >= 2018 for some prime p, OR v_q(k) >= 1009 and v_r(k) >= 2 for distinct primes q, r. Verify this matches your constructions. | Yes, the two conditions exactly correspond to the two structural cases from 2018 = 2 * 1009. Sufficiency by explicit AP construction, necessity by obstruction. |

**统计**：
- total_rounds: 6
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5

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
- structure_features: characterize_all_k_with_existence_property, divisor_function_divisibility_condition, infinite_AP_existence, two_structural_cases_from_prime_factorization_of_2018
- key_objects: d(n) divisor function, 2018=2*1009 (1009 prime), p-adic valuation v_p(k), AP with common difference k, prime factorization exponents

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [structural_decomposition_of_divisibility_condition, case_splitting_based_on_prime_factorization, constructive_sufficiency_via_p_adic_locking, necessity_via_obstruction_argument, chinese_remainder_theorem_implicit_use]
- primary_pattern: structural_decomposition_with_constructive_verification
- knowledge_required: [divisor function d(n)=product of (exponent+1), p-adic valuation, prime factorization of 2018=2*1009, arithmetic progressions, CRT/coprimality arguments, constructive vs necessity proof structure]
- key_insight: Factor 2018 = 2 * 1009 with 1009 prime, splitting 2018|d(n) into two cases: one exponent >= 2017, or one exponent >= 1008 and another >= 1. The AP construction locks in these valuations by choosing the right starting point so that the common difference's p-adic structure preserves them.

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_case_by_case_checking_of_individual_k_values
- translation_to: structural_analysis_via_p_adic_valuations_and_divisor_function_factorization
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: [divisor function, 2018 factorization, p-adic valuation, arithmetic progression, prime exponent structure, 1009 primality]
- expected_ai_method: Bare AI would try to check small k values or attempt direct construction without first decomposing 2018 into prime factors, missing the two-case structure.
- correct_method: Factor 2018 = 2 * 1009, decompose 2018|d(n) into two structural cases on exponents, construct APs by locking p-adic valuations, prove necessity by obstruction.

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？ → 是，characterization + enumeration_brute_force + structural_transformation 均为已有值
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？ → 是，粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？ → 是，三个维度足够
- [x] 如果发现拓扑分类需要进化，在此写出建议： → 无需进化

**拓扑进化建议**（如有）：无，现有拓扑分类完全够用。

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
- 局部tell_hint_pairs数量: 6 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: Bare AI will likely fail to factor 2018 and decompose the divisibility condition into two structural cases. It may attempt direct construction for specific k values without recognizing the p-adic valuation locking mechanism, and will almost certainly miss the necessity argument.
- suitable_for_poc: [tell_identification_structural_decomposition, hint_injection_p_adic_locking, knowledge_bottleneck_primality_recognition]
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
- [x] answer（**⚠️ 必填，不能为None**）
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

完整JSON已写入 `subagents-dirs/omni_math_000147/profile.json`

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
2. 更新`problem_extraction_progress`集合中`_key="330019"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_000147"
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
    '_key': '330019',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_000147',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_000147')
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
