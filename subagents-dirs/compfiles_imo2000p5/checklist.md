# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2000p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2000P5.lean
- **来源**: IMO 2000 P5
- **ArangoDB progress记录_key**: 329174（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2000P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Does there exist a positive integer n such that n has exactly 2000 distinct prime divisors and n divides 2ⁿ + 1?
- 解答核心思路（1-2句话）：通过对素因子个数k的归纳构造，从n=1出发，每步利用extend_divisibility引理（若n|2ⁿ+1且p是奇素数且p|2ⁿ+1，则np|2^(np)+1）增加1个素因子同时保持整除性，对k=2000即得结论。
- 解答关键步骤列表：
  1. 基础情形：n=1满足1|2¹+1=3，有0个素因子
  2. extend_divisibility引理：利用2^(np)+1 = (2ⁿ+1)(交替和)的因式分解，证明np|2^(np)+1
  3. quotient_not_dvd_of_ne引理：若p≠q为素数且p|2ⁿ+1，则p不整除商(2^(nq)+1)/(2ⁿ+1)（因为商≡q mod p）
  4. exists_new_prime_factor引理：当n≥3时，商Φ=(2^(nq)+1)/(2ⁿ+1)>q且只含q作为来自2ⁿ+1的素因子（重数1），故Φ/q>1必含新素数r
  5. increase_prime_factors：取q为2ⁿ+1的最小素因子（奇数）。若q∤n则m=nq；若q|n则用exists_new_prime_factor得新素数r，m=nqr
  6. 归纳2000次即得n恰有2000个素因子且n|2ⁿ+1

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
| 1 | 纯元认知观察 | 0.3 | 这个问题的结构是什么？描述已知条件和求解目标。这是一个存在性问题吗？为什么直接找到这样的n很困难？ | 这是一个存在性问题：求n恰有2000个不同素因子且n|2ⁿ+1。困难在于n同时出现在除数和指数中，且2000个素因子意味着n极大，无法直接搜索。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的解题方向。考虑：直接构造、反证法、归纳法、小情形分析。哪个方向可能利用2ⁿ+1的特殊结构？ | 可能方向：直接构造（困难，n太大）、反证法（不太适用）、归纳法（从少素因子到多素因子）、小情形分析（看n=1,3,9等）。归纳法可能利用2ⁿ+1的结构，因为如果能保持n|2ⁿ+1同时增加素因子，就能逐步构造。 |
| 3 | 小尝试 | 0.2 | 试小情形：n=1是否满足？n=3呢？n=9呢？这些值之间有什么关系？素因子个数如何变化？ | n=1: 1|3 ✓, 0个素因子。n=3: 3|9 ✓, 1个素因子。n=9: 9|513=2⁹+1 ✓, 1个素因子(3²)。n=3→9是乘以3。但9仍只有1个素因子。需要找到增加新素因子的方法。 |
| 4 | 思维操作引导 | 0.6 | 若n|2ⁿ+1且p是奇素数且p|2ⁿ+1，能否证明np|2^(np)+1？提示：利用奇数幂因式分解 a^p+b^p=(a+b)(a^(p-1)-a^(p-2)b+...+b^(p-1))。 | 是的。2^(np)+1=(2ⁿ+1)(2^(n(p-1))-2^(n(p-2))+...+1)。因为2ⁿ≡-1(mod p)，交替和≡1+1+...+1=p≡0(mod p)，所以p整除交替和。又n|2ⁿ+1整除第一因子，故np|2^(np)+1。 |
| 5 | 推进 | 0.4 | 你已证明np|2^(np)+1。现在考虑：若q是2ⁿ+1的最小素因子且q已经整除n，乘以q不增加素因子个数。如何找到额外的新素数？ | 需要在2^(nq)+1中找到不整除2ⁿ+1的新素数r。考虑商Φ=(2^(nq)+1)/(2ⁿ+1)。如果Φ含有不在2ⁿ+1中的素因子，那就是我们要找的新素数r。 |
| 6 | 思维操作引导 | 0.7 | 分析商Φ=(2^(nq)+1)/(2ⁿ+1)。证明：(1)Φ>q，(2)对2ⁿ+1的任意素因子p≠q，p不整除Φ（因为Φ≡q mod p），(3)q整除Φ的重数恰为1。因此Φ/q>1必含新素数r。 | (1)Φ>q因为(2ⁿ+1)q<2^(n+q+1)≤2^(nq)。(2)Φ≡q(mod p)因为2ⁿ≡-1(mod p)使交替和≡q(mod p)，而p≠q素数故p∤q。(3)用重数分析，q在2^(nq)+1中的重数比在2ⁿ+1中恰多1。故Φ=q·m，m>1且m与2ⁿ+1互素，m必有新素因子r。 |
| 7 | 能量传递引导 | 0.8 | 现在把所有部分组合起来：从n=1出发，应用增加步骤2000次。每步要么乘以新素数q（若q∤n），要么乘以qr（若q|n，找新素数r）。这给出恰有2000个素因子且n|2ⁿ+1的n。 | 完整归纳：基础情形n=1(0个素因子,1|3)。归纳步骤：给定n有k个素因子且n|2ⁿ+1，取q=2ⁿ+1最小素因子(奇数)。若q∤n，m=nq有k+1个素因子且m|2^m+1。若q|n，由exists_new_prime_factor得新素数r，m=nqr有k+1个素因子且m|2^m+1。归纳2000次即得答案：存在。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 6
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 4

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
- structure_features: 存在性问题，带基数约束（恰有2000个不同素因子）和自指整除条件（n|2ⁿ+1，n同时出现在除数和指数中）；2000是任意常数，构造对任意k均成立
- key_objects: 正整数n、n的素因子集合、2ⁿ+1、整除关系n|2ⁿ+1

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["inductive_construction", "divisibility_preservation", "factorization_analysis", "quotient_analysis_for_new_primes", "case_splitting_on_divisibility"]
- primary_pattern: inductive_construction
- knowledge_required: ["整除与模运算", "素因子分解", "奇数幂因式分解(a^p+b^p)", "几何级数求和", "素数重数分析", "数学归纳法"]
- key_insight: 若n|2ⁿ+1且p是奇素数且p|2ⁿ+1，则np|2^(np)+1——这允许归纳构造，每步增加1个素因子同时保持整除性

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 存在性问题（"是否存在n满足条件？"）
- translation_to: 归纳构造（"从n=1出发逐步构造，每步增加1个素因子"）
- translation_type: existence_to_construction

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: ["inductive_construction", "extend_divisibility", "odd_power_factorization", "quotient_analysis", "new_prime_factor", "prime_factor_count_increment"]
- expected_ai_method: 直接搜索或构造满足条件的n（因n极大而不可行），或尝试反证法
- correct_method: 归纳构造——从n=1出发，利用extend_divisibility引理逐步增加素因子

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是，structural_existence/enumeration_brute_force/structural_transformation均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化

**拓扑进化建议**（如有）：无。已有拓扑分类完全适用。

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
| 1 | AI识别出存在性问题但未看到归纳结构 | 描述问题结构：已知条件和求解目标，为什么直接找n困难 | 0.3 | 纯元认知观察 | false | {structural_existence, enumeration_brute_force, method_problem_mismatch} | ["existence_question", "prime_divisor_count", "self_referential_divisibility"] |
| 2 | AI列出方向但未识别"保持n\|2ⁿ+1同时增长n"为可行方向 | 列出所有方向：直接构造、反证、归纳、小情形，哪个利用2ⁿ+1结构 | 0.5 | 自由列举 | false | {structural_existence, direct_calculation, search_space_estimation} | ["approach_enumeration", "divisibility_preservation", "induction_potential"] |
| 3 | AI验证小情形但未看到素因子个数增长的系统模式 | 试n=1,3,9，观察素因子个数变化 | 0.2 | 小尝试 | false | {structural_existence, case_by_case, structural_transformation} | ["small_cases", "pattern_recognition", "prime_factor_growth"] |
| 4 | AI考虑扩展n但未看到2^(np)+1的因式分解 | 若n\|2ⁿ+1且p奇素数p\|2ⁿ+1，证明np\|2^(np)+1，利用奇数幂因式分解 | 0.6 | 思维操作引导 | true | {structural_existence, algebraic_identity, knowledge_gap} | ["odd_power_factorization", "geometric_series", "modular_arithmetic", "extend_divisibility"] |
| 5 | AI看到因式分解但未处理q已整除n的情况 | 若q是2ⁿ+1最小素因子且q\|n，乘q不增素因子个数，如何找新素数 | 0.4 | 推进 | false | {structural_existence, algebraic_identity, structural_transformation} | ["prime_factor_count", "smallest_prime_factor", "new_prime_needed"] |
| 6 | AI认识到需要新素数但未分析商Φ的结构 | 分析商Φ=(2^(nq)+1)/(2ⁿ+1)：Φ>q，Φ≡q mod p，q重数恰1，故Φ/q>1含新素数r | 0.7 | 思维操作引导 | true | {structural_existence, logical_deduction, knowledge_gap} | ["quotient_analysis", "congruence_mod_p", "multiplicity_tracking", "new_prime_existence"] |
| 7 | AI有所有部件但需形式化完整归纳 | 组合：从n=1出发应用增加步骤2000次，每步增1个素因子 | 0.8 | 能量传递引导 | false | {structural_existence, logical_deduction, method_translation} | ["induction_formalization", "base_case", "2000_steps", "existence_conclusion"] |

**全局tell_hint_pairs详情**：

| scope_type | scope | observation_point | tell | hint | hint_level | generalizability | why_not_visible_locally | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|---|---|
| path_feature | 从n=1到2000个素因子的完整归纳构造路径 | null | 问题要求存在n有2000素因子且n\|2ⁿ+1，但解答需要从n=1归纳构造，每步增1个素因子 | 从平凡基础情形出发，归纳地增加素因子个数同时保持整除性 | 0.7 | high——归纳构造模式适用于数论中许多存在性问题 | 从构造的任何单步只能看到如何增加1个素因子，但"从n=1重复2000次"的全局路径结构在局部视角完全不可见 | {structural_existence, enumeration_brute_force, structural_transformation} | ["inductive_construction", "base_case_to_target", "prime_factor_count_increment"] |
| implicit | 商Φ=(2^(nq)+1)/(2ⁿ+1)在n≥3时总含新素因子 | R6 | 当q已整除n时，简单乘q不增素因子个数。商Φ>q且只含q作为来自2ⁿ+1的素因子(重数1)，故Φ/q>1必含新素数r | 分析商Φ的大小、模p同余、重数，证明Φ/q>1与2ⁿ+1互素故含新素数 | 0.6 | medium——"商分析找新因子"技术适用于此类整除问题但模式更广泛 | 在q\|n的步骤中，需要在商中找新素数的需求不显眼。Φ>q且现有素数(除q外)不能整除Φ需要全局的商结构知识和Φ≡q(mod p)同余 | {structural_existence, direct_calculation, knowledge_gap} | ["quotient_analysis", "new_prime_factor", "congruence_mod_p", "multiplicity_tracking"] |

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接构造或搜索满足条件的n（因n极大而不可行），或尝试反证法（不适用）。即使试小情形发现了n=1,3,9的模式，也难以识别出extend_divisibility引理和商分析找新素数的技术，无法完成归纳构造。
- suitable_for_poc: ["tell_hint_injection", "inductive_structure_recognition", "existence_to_construction_translation"]
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
2. 更新`problem_extraction_progress`集合中`_key="329174"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2000p5"
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
    '_key': '329174',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2000p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2000p5')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 2 global pairs, answer非None, per-pair拓扑存在, why_not_visible_locally存在

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: compfiles_imo2000p5
- solution_method_type: inductive_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类完全适用
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
