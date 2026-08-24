# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1988p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1988P5.lean
- **来源**: USA 1988 P5
- **ArangoDB progress记录_key**: 329353（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1988P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let p(x) = (1-x)^a (1-x²)^b (1-x³)^c ... (1-x^32)^k, where a, b, ..., k are integers. When expanded in powers of x, the coefficient of x¹ is -2 and the coefficients of x², x³, ..., x³² are all zero. Find k.
- 解答核心思路（1-2句话）：利用"倍增变换"p(x)→p(x)p(-x)，该变换保持乘积结构∏(1-x^i)^(a'(i))，同时将线性系数平方（取负）并将消失系数范围减半。重复4次后从-2/范围32变为-65536/范围2，提取指数后追溯得k=2^27-2^11。
- 解答关键步骤列表：
  1. 由x¹系数=-2推出a(1)=2（只有(1-x)^a影响x¹系数）
  2. 定义倍增变换：p(x)·p(-x) = q(x²)，其中q=∏(1-x^i)^(nextA(a,i))，nextA(a,j) = (if odd j then a(j) else 0) + 2·a(2j)
  3. 奇数因子：(1-x^i)(1-(-x)^i) = (1-x^i)(1+x^i) = 1-x^(2i)；偶数因子：(1-x^i)(1-(-x)^i) = (1-x^i)²
  4. 每次倍增：线性系数c→-c²，消失范围m→m/2
  5. 4次变换：-2/32 → -4/16 → -16/8 → -256/4 → -65536/2
  6. 提取：变换后(1-x)指数=65536，(1-x²)指数=C(65536,2)=65536·65535/2
  7. 追溯：(1-x²)的指数经4次变换=16·a(32)=16·k
  8. 解方程：16k = 65536·65535/2 → k = 2^27 - 2^11 = 134215680

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
| 1 | 纯元认知观察 | 0.8 | 观察这个问题的结构：p(x)是32个因子(1-x^i)的幂的乘积，x¹系数为-2，x²到x³²系数全为0。你能描述这个问题的结构特征吗？特别地，哪些因子影响低次系数？ | 只有(1-x)^a影响x¹系数，所以a=2。x²系数由(1-x)^a和(1-x²)^b共同贡献。x²到x³²系数全为0意味着32个未知指数满足31个约束方程，是一个高度约束的系统。 |
| 2 | 自由列举 | 0.7 | 已知a=2，x²到x³²系数全为0，你能列出可能的方法来确定所有指数（特别是k=a(32)）吗？ | 可能方法：1)直接逐个计算系数建立方程组；2)利用生成函数理论；3)寻找某种代换或变换简化问题；4)递归/归纳方法；5)利用多项式的特殊结构。 |
| 3 | 小尝试 | 0.5 | 尝试直接计算前几个系数。已知a=2，(1-x)²=1-2x+x²。要使x²系数为0，(1-x²)^b需要贡献什么？继续算x³会怎样？ | x²系数：C(2,2)+(-b)=1-b=0，所以b=1。但x³系数涉及(1-x)²、(1-x²)¹、(1-x³)^c三项的交叉贡献，方程迅速复杂化。到x³²时方程组几乎不可解。 |
| 4 | 思维操作引导 | 0.6 | 直接计算太复杂了。考虑一个变换操作：计算p(x)·p(-x)。对每个因子(1-x^i)，(1-x^i)·(1-(-x)^i)会变成什么？注意区分i为奇数和偶数的情况。 | 奇数i：(1-x^i)(1+x^i)=1-x^(2i)。偶数i：(1-x^i)(1-(-x)^i)=(1-x^i)²。因此p(x)·p(-x)=q(x²)，其中q=∏(1-x^i)^(a'(i))保持相同的乘积结构，指数按nextA规则更新。 |
| 5 | 推进 | 0.7 | p(x)·p(-x)=q(x²)保持了乘积结构。这个变换对线性系数和消失范围有什么效果？如果我们从-2/范围32开始，重复4次会怎样？ | 每次倍增：线性系数c→-c²，消失范围m→m/2。4次变换：-2/32→-4/16→-16/8→-256/4→-65536/2。最终得到一个乘积形式，x¹系数为-65536，x²系数为0。 |
| 6 | 思维操作引导 | 0.6 | 4次变换后，新乘积的x¹系数为-65536，x²系数为0。你能从中提取出变换后(1-x)和(1-x²)的指数吗？然后如何追溯到原始的k=a(32)？ | (1-x)的指数=65536（由x¹系数=-指数）。(1-x²)的指数=C(65536,2)=65536·65535/2（由x²系数=0的条件）。追溯：(1-x²)的指数经4次nextA变换=16·a(32)=16·k。 |
| 7 | 能量传递引导 | 0.8 | 现在你有了所有关键信息：16k = C(65536,2) = 65536·65535/2。完成最后计算，求k的值。 | k = 65536·65535/(2·16) = 2^16·(2^16-1)/2^5 = 2^11·(2^16-1) = 2^27 - 2^11 = 134215680。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.7
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
- problem_type: constraint_satisfaction
- structure_features: 32个因子的幂乘积多项式，31个系数消失条件约束32个未知指数，需要发现代数变换将约束系统降维
- key_objects: 多项式乘积∏(1-x^i)^(a(i)), 指数序列a(i), 系数条件, 倍增变换p(x)→p(x)p(-x), nextA递推关系

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["structural_transformation", "iterative_reduction", "coefficient_tracking", "algebraic_identity_exploitation", "exponent_recursion_tracing"]
- primary_pattern: structural_transformation
- knowledge_required: ["多项式乘积展开", "二项式系数", "生成函数", "p(x)p(-x)倍增变换技巧", "乘积形式保持性", "nextA递推关系"]
- key_insight: 倍增变换p(x)→p(x)p(-x)保持乘积结构同时平方线性系数、减半消失范围，使32维约束系统经4次迭代降为2维可直接求解

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_coefficient_computation（直接逐个计算系数建立方程组）
- translation_to: iterative_structural_transformation（通过倍增变换迭代降维）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: constraint_satisfaction, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["doubling transformation", "p(x)p(-x)", "product form preservation", "coefficient squaring", "vanishing range halving", "exponent tracking", "binomial coefficient extraction", "nextA recurrence"]
- expected_ai_method: direct_calculation（bare AI预期会逐个计算系数建立方程组，在32维系统中迷失）
- correct_method: iterative_structural_transformation（通过倍增变换p(x)p(-x)迭代降维求解）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。constraint_satisfaction + direct_calculation + method_translation 完全适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。都是中等抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的tell特征是"需要发现一个非显然的代数变换来降维"，method_translation已能捕获。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。现有拓扑分类体系完全适用。

**拓扑进化建议**（如有）：无。现有分类体系足够。

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
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试直接逐个计算系数建立方程组，从x¹系数推出a=2，从x²系数推出b=1，但随着阶数升高方程交叉项指数级增长，在32维约束系统中迷失。AI不会发现p(x)p(-x)倍增变换这个非显然的代数技巧，因此无法将问题降维。
- suitable_for_poc: ["tell_hint_injection", "knowledge_bottleneck_detection", "method_translation_verification"]
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
2. 更新`problem_extraction_progress`集合中`_key="329353"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1988p5"
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
    '_key': '329353',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1988p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1988p5')
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
- problem_id: compfiles_usa1988p5
- solution_method_type: iterative_structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系（constraint_satisfaction + direct_calculation + method_translation）完全适用。
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
