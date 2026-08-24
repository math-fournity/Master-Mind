# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2010p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2010P6.lean
- **来源**: USA 2010 P6
- **ArangoDB progress记录_key**: 329441（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2010P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：黑板上有68个非零整数的有序对（不必不同），满足不存在整数k使得(k,k)和(-k,-k)同时出现。学生擦除136个整数中的一些，使得没有两个被擦除的数之和为零，每有一个有序对至少一个元素被擦除就得1分。求学生能保证的最大分数。
- 解答核心思路（1-2句话）：下界用概率方法——对每个绝对值k随机选择擦除+k或-k（概率q=(√5-1)/2），证明每对期望得分≥q，总期望≥68q>42故存在策略得≥43；上界用极值构造——8个绝对值各5个环(i,i)共40对+C(8,2)=28条负边(-i,-j)，证明任何合法擦除得分≤43。
- 解答关键步骤列表：
  1. 结构化简：每个绝对值k只能选擦+k或-k（不能同时），化为二元选择问题
  2. 概率方法：对n个绝对值，每个独立以概率q选+a_i，1-q选-a_i
  3. 逐对期望分析：利用棋盘条件排除(-a,-a)最坏情况，最坏每对期望≥q
  4. 最优q：q²+q≤1给出q=(√5-1)/2≈0.618，68q>42故≥43
  5. 极值构造：8个值，5个环+K₈负边，得分≤5a+28-C(a,2)≤43

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
| 1 | 纯元认知观察 | 0.3 | 描述题目结构：已知什么、未知什么、约束条件是什么？"没有两个被擦除的数之和为零"对擦除策略意味着什么？ | 68个有序对，每个对有两个非零整数。约束意味着如果擦了x就不能擦-x，所以对每个绝对值k，只能选+k或-k之一（或都不选）。目标是最大化保证得分。 |
| 2 | 自由列举 | 0.5 | 列出所有可能的方法：贪心、分类讨论、概率方法、极值构造、代数优化等 | 贪心（擦所有正数）、分类讨论（按对类型分析）、概率方法（随机策略+期望分析）、极值构造（构造最坏棋盘）、代数优化（建模为优化问题） |
| 3 | 小尝试 | 0.2 | 试贪心策略：擦所有正整数。这能保证多少分？对手能否构造一个棋盘使贪心表现差？ | 擦所有正数：对(k,k)型对得分，但对(-k,-k)型对不得分（因为擦的是+k不是-k）。如果棋盘全是(-k,-k)型对，贪心得0分。所以贪心不能保证好分数。 |
| 4 | 思维操作引导 | 0.6 | 观察关键结构：对每个出现的绝对值k，你必须选择擦+k或-k（不能同时）。这把问题化为了什么结构？每个有序对被得分的条件是什么？ | 化为n个二元选择问题（n=不同绝对值个数）。对(a,b)型对，得分当且仅当选了+a或选了-b（取决于a,b的符号和选择）。关键是分析不同对类型在不同选择下的得分概率。 |
| 5 | 思维操作引导 | 0.7 | 用概率方法：对每个绝对值k，以概率q独立随机选择擦+a_k或-a_k。计算每种对类型的期望得分。棋盘条件"不存在(k,k)和(-k,-k)同时出现"在这里起什么作用？ | 对类型分析：(a,a)环→期望q；(a,-a)→期望1；(a,b)异值→期望1-(1-q)²。棋盘条件排除了(-a,-a)型对（其期望仅q²，比q更差），使最坏期望≥q。 |
| 6 | 推进 | 0.4 | 计算最优q：要求最坏对类型期望≥q，即q²+q≤1。求q并验证68q>42。 | q²+q=1给出q=(√5-1)/2≈0.618。68×0.618≈42.02>42，所以存在策略得分≥43（因为得分是整数且>42）。 |
| 7 | 思维操作引导 | 0.6 | 构造极值棋盘证明上界：用8个绝对值，每个5个环(i,i)共40对，加C(8,2)=28条负边(-i,-j)。证明任何合法擦除得分≤43。 | 设选了a个正值，环贡献5a分。负边中，选了正值的a个索引对应的负边(-i,-j)中j也在A的那些不得分，至少C(a,2)条不得分。得分≤5a+28-C(a,2)≤43（a≤8时二次函数最大值在a=5附近取43）。 |
| 8 | 能量传递引导 | 0.3 | 组合上下界：下界≥43，上界≤43，答案是多少？ | 答案是43。下界由概率方法保证，上界由极值构造封顶，两者精确匹配。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"
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
- structure_features: 68个非零整数有序对，擦除约束（不能同时擦x和-x），棋盘条件（不存在(k,k)和(-k,-k)同时出现），保证得分最大化（min-max结构）
- key_objects: ["有序对", "绝对值", "擦除集合", "得分函数", "概率策略", "极值棋盘"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["结构化简（二元选择）", "概率方法", "逐类型期望分析", "极值构造", "二次函数优化"]
- primary_pattern: 概率方法
- knowledge_required: ["概率方法（随机策略+期望论证）", "期望值计算", "组合计数（C(n,2)）", "二次函数极值", "极值构造技巧"]
- key_insight: 问题化为每个绝对值的二元选择，用概率方法以q=(√5-1)/2随机选择，棋盘条件恰好排除最坏对类型使期望≥q，68q>42得下界43；极值构造8值5环+K₈负边精确匹配上界43。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 贪心/直接枚举（逐对分析确定性策略）
- translation_to: 概率方法+极值构造（随机策略期望论证+匹配构造）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: enumeration_brute_force, gap_type: method_problem_mismatch}
- tell_small_concepts: ["二元选择", "概率方法", "期望论证", "黄金比例q", "极值构造", "棋盘条件排除最坏情况", "匹配上下界"]
- expected_ai_method: 贪心策略（擦所有正数）或逐情况枚举，无法处理"保证"层面的min-max结构
- correct_method: 概率方法（随机策略+期望论证）证明下界+极值构造证明上界

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 可以。discrete_combinatorial + enumeration_brute_force + method_problem_mismatch 完全覆盖。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 一致。三个值都是抽象粒度。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。不同轮次的per-pair拓扑能区分不同阶段的方法-问题失配。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化。已有分类体系完全适用。

**拓扑进化建议**（如有）：无。已有拓扑分类体系完全覆盖本题。

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
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 2 个，implicit型: 1 个

**局部pairs详见profile.json中的tell_hint_pairs字段**

**全局pairs详见profile.json中的global_tell_hint_pairs字段**：
1. (path_feature) 完整解法路径：二元选择→概率方法→最优q→极值构造，三步连接在局部不可见
2. (implicit) 棋盘条件"不存在(k,k)和(-k,-k)同时出现"是概率方法可行的关键——排除最坏对类型(-a,-a)期望q²<q
3. (path_feature) 极值构造参数（8值、5环）非任意——使二次函数5a+28-C(a,2)峰值恰为43，与下界精确匹配

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会尝试贪心策略（擦所有正数）或逐情况枚举，无法处理"保证"层面的min-max结构。不会想到用概率方法建立下界，也不会构造匹配的极值棋盘证明上界。可能给出一个不正确的猜测答案而无法证明。
- suitable_for_poc: ["tell_identification", "hint_injection", "probabilistic_method_translation", "extremal_construction_guidance"]
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
2. 更新`problem_extraction_progress`集合中`_key="329441"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2010p6"
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
    '_key': '329441',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2010p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2010p6')
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
- problem_id: compfiles_usa2010p6
- solution_method_type: probabilistic_method
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 3（2个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类体系完全覆盖
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
