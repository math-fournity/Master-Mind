# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1992p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1992P5.lean
- **来源**: USA 1992 P5
- **ArangoDB progress记录_key**: 329368（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1992P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：A complex polynomial has degree 1992 and distinct zeros. Show that we can find complex numbers z_n, such that if p_1(z) = z - z_1 and p_n(z) = p_{n-1}(z)^2 - z_n, then the polynomial divides p_{1992}(z).
- 解答核心思路（1-2句话）：通过对集合大小做归纳，每步选两个根的中点作为z_k，利用(a-m)^2=(b-m)^2将集合大小减1，递归直到单元素集，最后用互素线性因子论证整除性。
- 解答关键步骤列表：
  1. 识别q | p_{1992}等价于p_{1992}在q的所有根上为零
  2. 发现求值复合结构：p_n(x) = p_{n-1}((x - z_1)^2)
  3. 关键洞察：选z_1 = (a+b)/2为中点，使(a-z_1)^2 = (b-z_1)^2，集合大小减1
  4. 对集合大小做归纳：基例|S|=1取z_1=唯一元素；归纳步选两元素中点缩减集合
  5. |S| < n时用尾部补零填充
  6. 用互素线性因子论证：q有不同根，q = c·∏(X-a_i)，各(X-a_i)互素，故乘积整除p_{1992}

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
| 1 | 纯元认知观察 | 0.8 | q | p_{1992}在根的意义是什么？p_{1992}的次数和根的个数是多少？ | q的每个根都是p_{1992}的根。p_{1992}次数为2^{1991}，远大于1992，关键是能否选z使1992个根都在p_{1992}的根中 |
| 2 | 自由列举 | 0.7 | 列出使p_{1992}在q所有根上为零的所有可能方法，包括正向和反向策略 | 正向：按序选z_1,z_2,...控制根；反向：从根集合S出发逐步缩减|S|；直接代数操作递推式 |
| 3 | 小尝试 | 0.5 | 试正向构造：设z_1为q的一个根，选z_2使p_2在另一个根上为零，困难在哪？ | p_2(b)=(b-a)^2-z_2需z_2=(b-a)^2，但p_2(a)=-z_2≠0，正向分支结构难以同时控制多个根 |
| 4 | 思维操作引导 | 0.6 | 检查求值复合结构：p_n(x) = p_{n-1}((x-z_1)^2)，这个复合结构如何帮助？ | p_n(x)=0 iff p_{n-1}((x-z_1)^2)=0，即(x-z_1)^2是p_{n-1}的根。若p_{n-1}在T上为零，则p_n在{x:(x-z_1)^2∈T}上为零 |
| 5 | 思维操作引导 | 0.5 | 给定p_n(x)=p_{n-1}((x-z_1)^2)，如何选z_1使|T|<|S|？何时(a-z_1)^2=(b-z_1)^2？ | (a-z_1)^2=(b-z_1)^2当a-z_1=-(b-z_1)即z_1=(a+b)/2中点时。选z_1为中点使两元素坍缩为一个，|T|≤|S|-1 |
| 6 | 推进 | 0.6 | 形式化归纳：对任意非空集S（|S|≤n）存在长n的zs使p_n在S上为零。处理基例和|S|<n的情况 | 基例|S|=1取z_1=唯一元素；归纳步选两元素中点缩减集合用归纳假设；|S|<n时尾部补零 |
| 7 | 能量传递引导 | 0.7 | 应用到q：|S|=1992，p_{1992}在所有根上为零。用互素线性因子论证q | p_{1992} | q=c·∏(X-a_i)各因子互素，p_{1992}被每个(X-a_i)整除，故乘积整除p_{1992}，q整除p_{1992} |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.4
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
- problem_type: structural_existence
- structure_features: 迭代多项式构造p_n(z)=p_{n-1}(z)^2-z_n（次数倍增）；求值复合结构p_n(x)=p_{n-1}((x-z_1)^2)允许反向缩减；中点碰撞(a-m)^2=(b-m)^2将两元素坍缩为一个；对集合大小归纳每步减1；互素线性因子论证将vanishing转为整除
- key_objects: 1992次复多项式q（有不同根）；迭代多项式序列p_n；根集合S；中点m=(a+b)/2；缩减集T={(s-m)^2:s∈S}

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [backward_reasoning, structural_reduction, induction_on_cardinality, composition_decomposition]
- primary_pattern: backward_reasoning
- knowledge_required: [polynomial composition and evaluation, coprime linear factors and divisibility, mathematical induction, midpoint of complex numbers and quadratic folding]
- key_insight: 选z_1为两根a,b的中点使(a-z_1)^2=(b-z_1)^2，通过求值复合p_n(x)=p_{n-1}((x-z_1)^2)将目标集大小减1

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: forward construction of z values（正向构造z值）
- translation_to: backward reduction of root set via quadratic folding（通过二次折叠反向缩减根集合）
- translation_type: method_translation（方法翻译——从正向构造翻译到反向缩减）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [evaluation composition, midpoint collision, set reduction via quadratic folding, backward induction on cardinality, coprime linear factor divisibility]
- expected_ai_method: 正向构造——设z_1为q的一个根，然后试图依次选择z_2,z_3,...使p_n在剩余根上为零，但在平方根分支结构中迷失
- correct_method: 反向归纳——从1992个根的集合出发，每步选两元素中点作为z_k通过(s-m)^2坍缩，缩减集合大小1，递归到单元素集后补零，最后用互素线性因子论证整除

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？
- [x] 如果发现拓扑分类需要进化，在此写出建议：

**拓扑进化建议**（如有）：无需进化。structural_existence/direct_calculation/structural_transformation三个维度足够区分此题。不同轮次的pair-level拓扑有变化（R4/R7用knowledge_gap，R5/R6用structural_transformation），能精确区分知识瓶颈和思维瓶颈。

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
- bare_ai_error_prediction: Bare AI会尝试正向构造——设z_1为q的一个根，然后试图依次选择z_n使p_n在剩余根上为零，但在平方根分支结构（每步根数翻倍）中迷失，无法认识到反向缩减策略。可能也无法将vanishing on roots连接到polynomial divisibility via coprime factors。
- suitable_for_poc: [POC-VMS-hint-injection, POC-VMS-tell-detection, POC-VMS-method-translation]
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
- [x] answer（proof类型填要证明的结论）
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

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

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
2. 更新`problem_extraction_progress`集合中`_key="329368"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1992p5"
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
    '_key': '329368',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1992p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1992p5')
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
- problem_id: compfiles_usa1992p5
- solution_method_type: backward_induction_with_set_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无需进化。structural_existence/direct_calculation/structural_transformation三个维度足够。不同轮次pair-level拓扑有变化（R4/R7用knowledge_gap，R5/R6用structural_transformation），能精确区分知识瓶颈和思维瓶颈。
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
