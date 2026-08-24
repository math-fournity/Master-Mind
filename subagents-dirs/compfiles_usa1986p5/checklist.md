# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1986p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1986P5.lean
- **来源**: USA 1986 P5
- **ArangoDB progress记录_key**: 329345（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1986P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：n的划分（partition）是一个递增整数序列，和为n。f(p)=p中1的个数，g(p)=p中不同整数的个数。证明对所有n的划分p，∑f(p)=∑g(p)。
- 解答核心思路（1-2句话）：两个和都等于π(0)+π(1)+...+π(n-1)（π(k)为k的划分数），通过双计数法分别证明。
- 解答关键步骤列表：
  1. **∑f(p)的递推**：建立F(n+1)=F(n)+π(n)。含1的n+1的划分擦去一个1与n的划分双射，不含1的划分贡献0。归纳得∑f(p)=∑_{k=0}^{n-1}π(k)。
  2. **∑g(p)的双计数**：g(p)=p中不同部分的个数=∑_{m=1}^{n} [m∈p]。交换求和顺序，对固定m，含m的n的划分数=π(n-m)（擦去一个m的双射）。得∑g(p)=∑_{m=1}^{n}π(n-m)=∑_{k=0}^{n-1}π(k)。
  3. **结论**：两个和都等于∑_{k=0}^{n-1}π(k)，故相等。

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
| 1 | 纯元认知观察 | 0.2 | 描述这道题的结构：我们要证明什么？f(p)和g(p)分别是什么？求和的范围是什么？ | 我们需要对n的所有划分p证明∑f(p)=∑g(p)。f(p)是划分p中1的个数，g(p)是p中不同整数的个数。求和遍历n的所有划分。这是一个关于划分的恒等式证明。 |
| 2 | 自由列举 | 0.5 | 列出所有可能证明两个和相等的方法方向。 | 可能方向：(1)直接对每个划分计算f和g再比较；(2)对n做归纳；(3)生成函数方法；(4)双计数法——把两个和重新解释为计数同一事物；(5)建立递推关系分别计算两个和；(6)构造双射。 |
| 3 | 小尝试 | 0.3 | 试n=3,4,5，分别计算∑f(p)和∑g(p)，看看有没有规律。 | n=3: 划分为(1,1,1),(1,2),(3)。∑f=3+1+0=4, ∑g=1+2+1=4。n=4: ∑f=4+2+1+0+0=7(?需仔细算), ∑g也=7。似乎都相等，且可能等于π(0)+π(1)+...+π(n-1)。 |
| 4 | 思维操作引导 | 0.6 | 把两个和重新解释：∑f(p)是在计数所有"（划分p, p中某个1的位置）"的配对数；∑g(p)是在计数所有"（划分p, p中某个不同部分m）"的配对数。两者都在计数"（划分, 特定部分）"的配对。能否用这个统一视角？ | 是的！∑f(p)=#{(p,i): p是n的划分, p的第i个部分是1}，∑g(p)=#{(p,m): p是n的划分, m是p的一个不同部分}。两者都是计数"划分-部分"配对，只是选取部分的规则不同。 |
| 5 | 推进 | 0.5 | 对∑f(p)，擦去一个1得到n-1的划分，这是双射。更一般地，能否建立递推F(n+1)=F(n)+π(n)？并归纳得∑f(p)=∑_{k=0}^{n-1}π(k)？ | 含1的n+1的划分擦去一个1↔n的划分（双射），贡献∑f(含1的划分)=F(n)+π(n)（每个n的划分加一个1，f增加1）。不含1的划分贡献0。故F(n+1)=F(n)+π(n)。归纳得F(n)=∑_{k=0}^{n-1}π(k)。 |
| 6 | 思维操作引导 | 0.4 | 对∑g(p)，交换求和顺序：对固定部分m，含m的n的划分数等于多少？（提示：擦去一个m） | 对固定m（1≤m≤n），含m的n的划分擦去一个m↔n-m的划分（双射），所以含m的划分数=π(n-m)。因此∑g(p)=∑_{m=1}^{n}π(n-m)=∑_{k=0}^{n-1}π(k)。 |
| 7 | 能量传递引导 | 0.7 | 现在两个和都表示为∑_{k=0}^{n-1}π(k)，完成证明。 | ∑f(p)=∑_{k=0}^{n-1}π(k)=∑g(p)，故∑f(p)=∑g(p)。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.2+0.5+0.3+0.6+0.5+0.4+0.7=3.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

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
- structure_features: 两个关于整数划分的求和恒等式，需要证明∑f(p)=∑g(p)。f(p)计数1的个数，g(p)计数不同部分的个数。核心结构是"两个不同的划分统计量在所有划分上求和后相等"。
- key_objects: ["整数划分(partition of n)", "f(p)=p中1的个数", "g(p)=p中不同整数的个数", "划分计数函数π(k)", "双计数配对(partition, part)"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["double_counting", "bijection", "recursive_decomposition", "sum_exchange"]
- primary_pattern: double_counting
- knowledge_required: ["整数划分的基本概念", "划分计数函数π(k)", "双射原理", "双计数法", "求和顺序交换"]
- key_insight: 把两个和都重新解释为计数"（划分, 特定部分）"配对，然后利用"擦去一个部分m"的双射将含m的n的划分数化为π(n-m)，最终两个和都等于∑_{k=0}^{n-1}π(k)。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 逐划分求和的统计量（sum of per-partition quantities f(p) and g(p)）
- translation_to: 双计数配对计数（counting pairs (partition, specific part) in two ways, both yielding ∑π(k)）
- translation_type: reinterpretation_to_double_counting（将表面不同的两个求和重新解释为同一双计数问题的两个面）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "direct_calculation", gap_type: "method_translation"}
- tell_small_concepts: ["double_counting", "bijection_partition_n-m", "counting_pairs", "distinct_parts", "partition_function_pi", "erase_one_part"]
- expected_ai_method: direct_calculation——bare AI预期会尝试直接对每个划分计算f和g再比较，或尝试对n做归纳但找不到统一的双计数解释，陷入复杂案例分析。
- correct_method: double_counting——将两个和重新解释为计数"（划分, 特定部分）"配对，利用擦去一个部分的双射将含m的划分数化为π(n-m)，两个和都等于∑π(k)。

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。discrete_combinatorial + direct_calculation + method_translation 完全覆盖。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。三个维度都用抽象级别值。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类完全适用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部(tell, hint)对详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到两个关于划分的求和等式，但未识别出双计数结构 | 描述题目结构：f(p)和g(p)分别是什么？求和范围是什么？ | 0.2 | 纯元认知观察 | false | {discrete_combinatorial, direct_calculation, method_problem_mismatch} | ["partition_structure", "f_count_ones", "g_count_distinct"] |
| 2 | AI列出方法但可能未识别双计数为关键方向 | 列出所有可能证明方法：直接计算、归纳、生成函数、双计数、双射 | 0.5 | 自由列举 | false | {discrete_combinatorial, enumeration_brute_force, method_problem_mismatch} | ["approach_enumeration", "double_counting_candidate", "induction_candidate"] |
| 3 | AI试小例子但可能未发现π(0)+...+π(n-1)规律 | 试n=3,4,5计算两个和，观察规律 | 0.3 | 小尝试 | false | {discrete_combinatorial, direct_calculation, search_space_estimation} | ["small_cases", "pattern_pi_sum", "numerical_verification"] |
| 4 | AI计算了小例子但未将求和重新解释为配对计数 | 把两个和重新解释为计数"（划分, 特定部分）"配对 | 0.6 | 思维操作引导 | false | {discrete_combinatorial, direct_calculation, method_translation} | ["pair_counting", "reinterpret_sum", "partition_part_pairs"] |
| 5 | AI看到配对计数解释但未连接到划分函数递推 | 对∑f(p)建立递推F(n+1)=F(n)+π(n)，归纳得∑π(k) | 0.5 | 推进 | false | {discrete_combinatorial, logical_deduction, method_translation} | ["erase_one_bijection", "recursive_decomposition", "partition_recurrence"] |
| 6 | AI需要关键双射知识：含m的划分↔n-m的划分 | 对固定m，含m的n的划分数=π(n-m)（擦去一个m的双射） | 0.4 | 思维操作引导 | true | {discrete_combinatorial, logical_deduction, knowledge_gap} | ["bijection_partition_n-m", "fixed_part_count", "erase_one_part"] |
| 7 | AI已将两个和都表示为∑π(k)，需收尾 | 两个和都等于∑_{k=0}^{n-1}π(k)，故相等，证毕 | 0.7 | 能量传递引导 | false | {discrete_combinatorial, logical_deduction, method_translation} | ["common_expression", "pi_sum_equality", "conclusion"] |

**全局(tell, hint)对详情**：

1. **path_feature型**：
   - scope: "整个解答路径"
   - observation_point: null
   - tell: 解答需要识别两个和都是同一双计数恒等式的两个面——都等于∑π(k)
   - hint: 寻找两个和的共同表达式，而非直接证明相等
   - hint_level: 0.7
   - generalizability: "high——双计数技术适用于许多划分恒等式"
   - why_not_visible_locally: 从任何单一步骤看，共同结构（两个和都=∑π(k)）不可见。局部步骤（小例子、配对计数、双射）对f和g看起来不同，只有走完整条路径后才在终点发现两个表达式收敛到同一个∑π(k)。
   - tell_topology: {discrete_combinatorial, direct_calculation, method_translation}
   - tell_small_concepts: ["double_counting", "common_expression_pi_sum", "convergence_of_two_paths"]

2. **implicit型**：
   - scope: "擦去一个部分m的双射原理"
   - observation_point: "R6"
   - tell: "擦去一个m"的双射是驱动两个和成立的隐藏引擎——在f和中以"擦去1"出现在递推中，在g和中以"擦去m"出现在直接计数中
   - hint: 计数含特定性质的划分时，寻找擦去该特定元素的双射，将问题归约为更小的划分问题
   - hint_level: 0.6
   - generalizability: "high——擦去一个部分的双射是划分理论的基本技术"
   - why_not_visible_locally: 在f和中，双射以"擦去1"出现在递推中；在g和中，以"擦去m"出现在直接计数中。局部看是不同操作，但本质是同一双射原理。只有看到两个应用才能发现共享技术。
   - tell_topology: {discrete_combinatorial, logical_deduction, knowledge_gap}
   - tell_small_concepts: ["erase_one_part_bijection", "partition_reduction", "shared_technique"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "marginal"
- bare_ai_error_prediction: bare AI可能尝试对n做归纳直接证明两个和相等，但无法找到统一的双计数解释，陷入复杂案例分析。或计算小例子后猜测相等但不证明双射。或只处理∑f(p)的递推但无法处理∑g(p)的求和顺序交换。
- suitable_for_poc: ["hint_injection_effectiveness", "tell_identification_at_branch_point", "double_counting_translation"]
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
2. 更新`problem_extraction_progress`集合中`_key="329345"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1986p5"
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
    '_key': '329345',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1986p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1986p5')
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
- problem_id: compfiles_usa1986p5
- solution_method_type: double_counting
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类（discrete_combinatorial + direct_calculation/method_translation + knowledge_gap）完全适用。
- 是否遇到异常: 无。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
