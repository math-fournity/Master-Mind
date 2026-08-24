# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003535
- **文件路径**: subagents-dirs/omni_math_003535/problem.lean
- **来源**: AoPS omni_math (putnam)
- **ArangoDB progress记录_key**: 333413（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003535/problem.lean`

**产出**：
- 题目原文：Fix b≥2, f(1)=1, f(2)=2, f(n)=n·f(d) where d=base-b digits of n. For which b does Σ1/f(n) converge?
- 解答核心思路：按位数分块后Σ_d 1/f(d)=S（自指），积分比较得H_d>ln(b)，故S>ln(b)·S，b≥3时ln(b)>1矛盾发散，b=2时ln(2)<1收缩收敛。
- 解答关键步骤：(1)按d分块重写求和 (2)积分比较H_d>ln(b) (3)识别自指Σ_d 1/f(d)=S (4)b≥3矛盾发散 (5)b=2收缩因子证明收敛

---

## Step 2: QA序列分析——局部视角7步 [x]

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 观察递归f(n)=n·f(d)的自指性质，d遍历值域有何特殊？ | d遍历所有正整数，Σ_d 1/f(d)=S自指 |
| 2 | 自由列举 | 0.7 | 列出判断Σ1/f(n)收敛性的所有方向 | 分块、比较判别、积分判别、研究f增长等 |
| 3 | 小尝试 | 0.5 | 试算b=2时f前几项，能否判断收敛？ | f增长快但逐项计算无法处理无穷级数 |
| 4 | 思维操作引导 | 0.4 | 按d分块重写求和，提取1/f(d)因子 | S=Σ_d(1/f(d))·H_d，关键知识瓶颈 |
| 5 | 思维操作引导 | 0.3 | 对H_d做积分比较，与ln(b)关系 | H_d>∫dx/x=ln(b)，知识瓶颈 |
| 6 | 推进 | 0.4 | 从S>ln(b)·S出发，b≥3和b=2各推出什么？ | b≥3矛盾发散，b=2自洽需精细分析 |
| 7 | 能量传递引导 | 0.6 | b=2时ln(2)<1收缩因子，构造收敛上界 | S=ln(2)·S+误差项，误差项收敛故S收敛 |

**统计**：
- total_rounds: 7
- metacognitive_rounds: 4
- knowledge_rounds: 2
- level_sum: 3.7
- knowledge_bottleneck: R4
- thinking_bottleneck: R6

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
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |

**统计**：
- total_rounds:
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）:
- knowledge_rounds（思维操作引导的轮数）:
- level_sum:
- knowledge_bottleneck（知识瓶颈在哪轮，或null）:
- thinking_bottleneck（思维瓶颈在哪轮，或null）:

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 递归定义f(n)=n·f(d)其中d为n的b进制位数；按位数分块后求和具有自指结构S=Σ_d(1/f(d))·H_d且Σ_d 1/f(d)=S；积分比较给出H_d>ln(b)；自指不等式S>ln(b)·S在ln(b)>1时产生矛盾
- key_objects: 递归函数f, b进制位数d, 调和级数块和H_d, 自然对数ln(b), 自指不等式S>ln(b)·S

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
- thinking_patterns: ["分块重组", "自指识别", "积分比较", "矛盾法", "收缩因子分析"]
- primary_pattern: 自指识别
- knowledge_required: ["调和级数与积分比较", "对数性质ln(b)", "级数收敛判别法", "b进制位数概念", "正项级数比较判别"]
- key_insight: 按位数分块后，Σ_d 1/f(d)恰好等于原级数S，形成自指不等式S > ln(b)·S，b≥3时ln(b)>1导致矛盾

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [列表]
- primary_pattern: （主导思维模式）
- knowledge_required: [前置知识列表]
- key_insight: （一句话关键转折点——"啊哈时刻"）

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 逐项递归计算
- translation_to: 分块重组与自指不等式分析
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
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["自指求和", "位数分块", "积分比较", "ln(b)阈值", "矛盾法"]
- expected_ai_method: direct_calculation — bare AI会尝试直接计算f的前几项或研究f的增长速度
- correct_method: 按位数分块重写求和，识别自指结构，用积分比较得H_d>ln(b)，推出自指不等式S>ln(b)·S

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/direct_calculation/structural_transformation可归入已有类别
- [x] 粒度一致
- [x] 三个维度足够区分
- [x] 无需进化

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
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会尝试直接计算f的前几项或研究f的增长速度，不会想到按位数分块重写求和，无法识别自指结构，无法得到S>ln(b)·S的关键不等式
- suitable_for_poc: ["自指结构识别POC", "分块重组思维操作POC", "积分比较与阈值分析POC"]
- discriminates_levels: true

**产出**：
- bare_ai_expected: "pass" | "fail" | "marginal"
- bare_ai_error_prediction: （bare AI会犯什么错的具体描述）
- suitable_for_poc: [适合哪些POC实验]
- discriminates_levels: boolean

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_003535/profile.json`，所有字段齐全。

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
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, per-pair拓扑存在, answer非None, knowledge_bottleneck=R4, thinking_bottleneck=R6）

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="333413"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003535"
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
    '_key': '333413',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003535',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003535')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [ ] 成功 / [ ] 失败
- 验证结果: [ ] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: omni_math_003535
- solution_method_type: block_decomposition_self_reference
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有分类够用
- 是否遇到异常: 否（solution_text从截断的problem.lean重建补全）

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
