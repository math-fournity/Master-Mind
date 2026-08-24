# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003825
- **文件路径**: subagents-dirs/omni_math_003825/problem.lean
- **来源**: AoPS omni_math (imo_shortlist)
- **ArangoDB progress记录_key**: 333704（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003825/problem.lean`

**产出**：
- 题目原文（数学描述）：IMO队长选正整数n和k（n>k），宣布给副队长和队员。队长秘密告诉副队长一个n位二进制串，副队长写下所有与队长串恰好k位不同的n位二进制串。队员看这些串后猜队长串。最少需要几次猜测保证正确？
- 解答核心思路（1-2句话）：当n=2k时，一个串和它的补串有相同的k-邻域，需要2次猜测；否则k-邻域唯一确定原串，只需1次。
- 解答关键步骤列表：
  1. 识别副队长写下的集合为Hamming距离k的邻域S_k(x)
  2. 设d(x,y)=d，参数化z与x在d个不同位上的重合数a，得d(y,z)=d+k-2a
  3. S_k(x)=S_k(y)要求所有z的a=d/2，用Vandermonde恒等式推出d=2k且n=2k
  4. n=2k时补串x̄满足d(x,z)=k iff d(x̄,z)=n-k=k，故S_k(x)=S_k(x̄)，需2次
  5. n≠2k时条件d=2k=n不可能，唯一确定，需1次

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
| 1 | 纯元认知观察 | 0.8 | 描述题目结构，队员有什么信息，需要确定什么？ | 队员看到Hamming距离k的邻域S_k(x)，需从中确定队长串x |
| 2 | 自由列举 | 0.7 | 列出所有可能的数学框架 | Hamming距离、编码理论、球填充、组合集合论、超立方体图论 |
| 3 | 小尝试 | 0.5 | 试n=3,k=1; n=4,k=1; n=4,k=2，注意是否有两个不同串产生相同集合 | n=4,k=2时0000和1111的distance-2邻域相同！这是n=2k的情况 |
| 4 | 思维操作引导 | 0.4 | 设d(x,y)=d，参数化z与x在d个不同位上的重合数a，建立代数条件 | d(y,z)=d+k-2a，S_k(x)=S_k(y)要求所有z的a=d/2 |
| 5 | 推进 | 0.6 | 用Vandermonde恒等式推导d和n的约束 | 只有a=d/2项非零，推出d=2k且n=2k，即d=n（补串） |
| 6 | 思维操作引导 | 0.3 | 形式化：n=2k时补串邻域相同，n≠2k时唯一性 | d(x,z)+d(x̄,z)=n，n=2k时k=n-k故邻域相同；n≠2k时d=2k=n不可能 |
| 7 | 能量传递引导 | 0.7 | 清晰陈述最终答案 | n=2k时2次（补串歧义），否则1次（唯一确定） |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.0
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: discrete_combinatorial
- structure_features: n位二进制串的Hamming距离k邻域，从邻域集合反推中心的唯一性问题
- key_objects: n位二进制串、Hamming距离k邻域、二进制串补串、Vandermonde恒等式

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
- problem_type:
- structure_features:
- key_objects:

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [small_case_analysis, algebraic_condition_setting, symmetry_recognition, uniqueness_proof]
- primary_pattern: symmetry_recognition
- knowledge_required: [Hamming距离、二进制串、Vandermonde恒等式/组合计数、补串概念]
- key_insight: 当n=2k时，串x和补串x̄的k-邻域相同（因d(x,z)=k iff d(x̄,z)=n-k=k）；n≠2k时Vandermonde推出唯一性

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [列表]
- primary_pattern: （主导思维模式）
- knowledge_required: [前置知识列表]
- key_insight: （一句话关键转折点——"啊哈时刻"）

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: case_by_case枚举小例子
- translation_to: Hamming距离参数的代数条件（Vandermonde恒等式）
- translation_type: method_translation

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: （从什么方法/语言翻译）
- translation_to: （翻译到什么方法/语言）
- translation_type: （翻译类型分类）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: case_by_case, gap_type: structural_transformation}
- tell_small_concepts: [Hamming distance, binary string complement, Vandermonde identity, neighborhood uniqueness, n=2k threshold]
- expected_ai_method: bare AI会试小例子观察到1次通常够用，但可能错误推广为总是1次，遗漏n=2k时补串共享邻域的特殊情况
- correct_method: 建立两个串共享k-邻域的代数条件，用Vandermonde推出需n=2k且d=n（补串），得n=2k时2次否则1次

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——discrete_combinatorial/case_by_case/structural_transformation能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有分类体系足够。

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: __, ai_method_type: __, gap_type: __}
- tell_small_concepts: [关键概念词列表]
- expected_ai_method: （bare AI预期会用的方法——可能走错的路）
- correct_method: （正确方法——解答实际用的方法）

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
- [ ] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？
- [ ] 粒度是否一致——你标注的值和已有值的粒度是否统一？
- [ ] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？
- [ ] 如果发现拓扑分类需要进化，在此写出建议：

**拓扑进化建议**（如有）：

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

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
- 局部tell_hint_pairs数量: __ 对
- 全局tell_hint_pairs数量: __ 对
- 全局pair中path_feature型: __ 个，implicit型: __ 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: marginal
- bare_ai_error_prediction: bare AI会试小例子正确观察到1次通常够用，但可能遗漏n=2k时补串共享邻域的特殊情况，错误推广为总是1次
- suitable_for_poc: [tell_detection, hint_injection, symmetry_recognition]
- discriminates_levels: true

**产出**：
- bare_ai_expected: "pass" | "fail" | "marginal"
- bare_ai_error_prediction: （bare AI会犯什么错的具体描述）
- suitable_for_poc: [适合哪些POC实验]
- discriminates_levels: boolean

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_003825/profile.json`。所有字段已逐项检查。

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

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, per-pair拓扑存在, answer非None, bottleneck为字符串类型）

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="333704"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003825"
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
    '_key': '333704',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003825',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003825')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [ ] 成功 / [ ] 失败
- 验证结果: [ ] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: omni_math_003825
- solution_method_type: structural_argument
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有分类体系足够
- 是否遇到异常: 无

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
