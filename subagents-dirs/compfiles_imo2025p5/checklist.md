# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2025p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2025P5.lean
- **来源**: IMO 2025 P5
- **ArangoDB progress记录_key**: 329283（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2025P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Alice和Bazza玩"inekoalaty game"，参数λ > 0。第n轮：n为奇数时Alice选非负实数xₙ使∑xᵢ ≤ λn（线性预算）；n为偶数时Bazza选非负实数xₙ使∑xᵢ² ≤ n（二次预算）。无法选择则对方获胜，永远进行则平局。求所有λ使Alice/Bazza有必胜策略。
- 解答核心思路（1-2句话）：阈值λ = √2/2由Cauchy-Schwarz不等式决定——Bazza的k步二次预算≤k给出线性和≤√2·k，与Alice的线性预算λ·2k竞争。λ < √2/2时Bazza贪心策略逼死Alice；λ > √2/2时Alice蓄力（一直出0）后一击毙命Bazza；λ = √2/2时双方均能存活。
- 解答关键步骤列表：
  1. Bazza贪心策略：每步花光二次预算，使每对(a,b)满足a²+b²=2，故a+b≥√2（Cauchy-Schwarz/QM-AM），2k步后线性和≥k√2 > λ(2k+1)（当λ < √2/2）
  2. Alice蓄力策略：λ > √2/2时Alice一直出0，线性预算λ(N+1) - √2·(N/2)线性增长（Bazza贡献由Cauchy-Schwarz控制），等到超过√(N+2)后一次性花光，使∑xᵢ² > N+2，Bazza无法应对
  3. 边界λ = √2/2：Alice出0可永远存活（预算恰好匹配），Bazza贪心也可永远存活，双方均无必胜策略

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
| 1 | 纯元认知观察 | 0.8 | 这个博弈的结构是什么？Alice和Bazza各自面临什么类型的约束？两个约束之间有什么本质区别？ | Alice有线性预算（∑xᵢ ≤ λn），Bazza有二次预算（∑xᵢ² ≤ n）。线性预算是可累加的（可以不花攒着），二次预算是局部的（每步都要满足）。两人交替出牌，谁先无法满足约束谁就输。关键在于两种预算的增长速率不同。 |
| 2 | 自由列举 | 0.7 | 要确定λ的阈值，有哪些可能的分析方向？列出你能想到的所有方法。 | 可以尝试：①取特定λ值分析；②找双方的最优策略；③用不等式联系线性和二次和；④考虑连续松弛；⑤分析渐进行为；⑥找不变量；⑦考虑贪心策略；⑧考虑蓄力策略。 |
| 3 | 小尝试 | 0.4 | 试着取λ=1分析。Alice的线性预算很充裕，她能直接出大数逼死Bazza吗？ | λ=1时Alice预算充裕，但直接出大数不一定有效——因为Bazza的二次预算每步重置（只需∑xᵢ² ≤ n）。关键不是单步大小，而是累积效应。这个方向可能走错——应该关注的是累积预算的竞争，而非单步。 |
| 4 | 思维操作引导 | 0.5 | 用Cauchy-Schwarz不等式分析：如果Bazza的k步满足∑xᵢ² ≤ k，那么他的线性和∑xᵢ有什么上界？这个上界和Alice的线性预算λ·2k有什么关系？ | 由Cauchy-Schwarz，(∑xᵢ)² ≤ k·∑xᵢ² ≤ k·k = k²，故∑xᵢ ≤ k。但更精确地，如果Alice出0，Bazza的N/2步的线性和≤ √(N/2 · N) = √(N²/2) = N/√2 = √2·(N/2)。这就是阈值√2/2的来源：当λ > √2/2时，Alice的预算λN增长快于Bazza的最大线性和√2·(N/2)。 |
| 5 | 推进 | 0.4 | 当λ < √2/2时，Bazza采用贪心策略（每步花光二次预算）。验证：每对(Alice的a, Bazza的b)满足a²+b²=2，这推出a+b≥√2。为什么这能让Bazza赢？ | 贪心策略下Bazza每步使∑xᵢ²恰好等于当前步数。每对(a,b)中a²+b²=2，由QM-AM或Cauchy-Schwarz得a+b≥√2。2k步后线性和≥k√2。而Alice的预算是λ(2k+1)。当λ < √2/2时，k√2 > λ(2k+1)对大k成立，Alice无法出牌。 |
| 6 | 思维操作引导 | 0.5 | 当λ > √2/2时，Alice如何利用线性预算的可累加性？她可以一直出0，等到什么时候再出手？出手时要满足什么条件才能让Bazza无法应对？ | Alice一直出0，她的未花线性预算λ(N+1) - √2·(N/2) = (λ-√2/2)·N + λ线性增长（Bazza线性和由Cauchy-Schwarz控制≤√2·(N/2)）。等到这个预算超过√(N+2)时，Alice一次性花光，使x_N² > N+2，即∑xᵢ² > N+2，Bazza在第N+1步无法满足二次预算。 |
| 7 | 能量传递引导 | 0.6 | 最后检查边界λ = √2/2。两个策略在边界处如何退化？为什么双方都没有必胜策略？ | λ=√2/2时：Alice出0可永远存活——她的预算√2/2·(2k+1)恰好≥Bazza的最大线性和√2·k（差距为√2/2，恰好够每步出0）。Bazza贪心也可永远存活——k√2 = √2/2·(2k)恰好不超过Alice的预算。两种策略都只能保证存活，无法逼死对方，故平局。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.8+0.7+0.4+0.5+0.4+0.5+0.6 = 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"（Cauchy-Schwarz联系线性和二次和是核心知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"（蓄力策略的设计是核心思维瓶颈）

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
- problem_type: characterization（确定所有λ值使各方有必胜策略，本质是阈值刻画）
- structure_features: 双人交替博弈，非对称约束（线性预算 vs 二次预算），阈值√2/2分隔胜负区域，边界处平局
- key_objects: 线性预算约束（∑xᵢ ≤ λn）、二次预算约束（∑xᵢ² ≤ n）、Cauchy-Schwarz不等式、贪心策略、蓄力策略、阈值√2/2、不变量a²+b²=2

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["threshold_analysis", "greedy_strategy", "budget_accumulation", "invariant_analysis", "cauchy_schwarz_application", "boundary_case_analysis"]
- primary_pattern: threshold_analysis（整个问题围绕确定临界阈值√2/2展开）
- knowledge_required: ["Cauchy-Schwarz不等式", "博弈论基础（必胜策略概念）", "实分析（非负实数序列）", "渐近增长比较", "QM-AM不等式"]
- key_insight: 阈值√2/2由Cauchy-Schwarz决定——Bazza的k步二次预算≤k给出线性和≤√2·k，与Alice的线性预算λ·2k竞争，当λ > √2/2时Alice的线性预算增长更快，可蓄力一击毙命

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: game_theory_strategy（博弈论策略分析语言——谁有必胜策略）
- translation_to: inequality_analysis（不等式分析语言——线性和与二次和的渐近竞争）
- translation_type: domain_translation（将博弈论问题翻译为不等式/渐近分析问题，核心翻译操作是用Cauchy-Schwarz连接两种预算）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "case_by_case", gap_type: "structural_transformation"}
- tell_small_concepts: ["linear_budget", "quadratic_budget", "cauchy_schwarz", "greedy_strategy", "threshold", "budget_accumulation", "invariant", "pairing_structure"]
- expected_ai_method: case_by_case（bare AI会尝试对不同λ值逐案分析，不发现统一的Cauchy-Schwarz结构）
- correct_method: inequality_based_strategy_analysis（用Cauchy-Schwarz联系两种预算，设计贪心/蓄力策略，分析渐近竞争确定阈值）

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是，characterization/case_by_case/structural_transformation均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够，无需新维度
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，现有拓扑分类体系完全够用

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

局部tell_hint_pairs详情见profile.json中的tell_hint_pairs数组。
全局tell_hint_pairs详情见profile.json中的global_tell_hint_pairs数组。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试对不同λ值逐案分析或直接模拟博弈，不识别Cauchy-Schwarz作为连接线性预算和二次预算的桥梁。可能找到贪心策略但不发现蓄力策略，或反之。很可能遗漏边界λ=√2/2的平局分析。
- suitable_for_poc: ["tell_hint_injection", "topology_matching", "knowledge_bottleneck_detection", "path_feature_extraction"]
- discriminates_levels: true（这道题需要同时掌握Cauchy-Schwarz、贪心策略设计、蓄力策略设计、边界分析，能区分AI的数学推理水平）

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
2. 更新`problem_extraction_progress`集合中`_key="329283"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2025p5"
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
    '_key': '329283',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2025p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2025p5')
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
- problem_id: compfiles_imo2025p5
- solution_method_type: cauchy_schwarz_threshold_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类体系完全够用（characterization/case_by_case/structural_transformation均可归入已有类别）
- 是否遇到异常: 否，入库和验证均一次通过

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
