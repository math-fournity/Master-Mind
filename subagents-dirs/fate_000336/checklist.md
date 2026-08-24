# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000336
- **文件路径**: subagents-dirs/fate_000336/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396446（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000336/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：存在交换环R,S使得R[x]≅S[x]但R⇏S。Lean形式化：∃ (R S : Type) (_ : CommRing R) (_ : CommRing S), Nonempty ((Polynomial R) ≃+* (Polynomial S)) ∧ IsEmpty (R ≃+* S)
- 解答核心思路（1-2句话）：Lean证明为sorry（未填写）。数学解答：将R[x]≅S[x]翻译为几何问题X×A¹≅Y×A¹（Zariski消去问题），用Danielewski曲面W_n={x^n·y=z²-1}作为反例——W_n⇏W_m但W_n×A¹≅W_m×A¹。
- 解答关键步骤列表：
  1. 识别问题为多项式环消去问题的反例构造
  2. 尝试Artinian环失败（幂零结构在多项式扩张下保持）
  3. 几何翻译：R[x]≅S[x] ↔ Spec(R)×A¹≅Spec(S)×A¹
  4. 回忆Danielewski曲面：W_n={x^n·y=z²-1}，W_n⇏W_m（无穷远点数不同）但W_n×A¹≅W_m×A¹
  5. 构造R=k[x,y,z]/(xy-z²+1), S=k[x,y,z]/(x²y-z²+1)，验证R⇏S且R[t]≅S[t]

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
| 1 | 纯元认知观察 | 0.3 | 描述问题结构：需要证明什么？涉及什么数学对象？ | 存在交换环R,S使R[x]≅S[x]但R⇏S，是存在性/构造性问题 |
| 2 | 自由列举 | 0.5 | 列出所有可能的方法：有限环、仿射代数、monoid环、几何方法 | (a)Artinian环 (b)仿射k-代数 (c)monoid环 (d)几何方法via Spec (e)文献检索 |
| 3 | 小尝试 | 0.4 | 尝试用Artinian局部环构造R,S，检查幂零结构是否在多项式扩张下保持 | 失败：幂零结构在多项式扩张下保持，Artinian环无法提供反例 |
| 4 | 思维操作引导 | 0.6 | 转向仿射k-代数，几何思考：R[x]≅S[x]在几何上意味着什么？ | R[x]≅S[x] ↔ Spec(R)×A¹≅Spec(S)×A¹，即Zariski消去问题 |
| 5 | 推进 | 0.5 | 搜索已知的X⇏Y但X×A¹≅Y×A¹的例子，什么是Danielewski曲面？ | W_n={x^n·y=z²-1}，W_n⇏W_m（无穷远点数不同）但W_n×A¹≅W_m×A¹ |
| 6 | 思维操作引导 | 0.4 | 从Danielewski曲面构造具体环R,S并验证 | R=k[x,y,z]/(xy-z²+1), S=k[x,y,z]/(x²y-z²+1)，R⇏S且R[t]≅S[t] |
| 7 | 能量传递引导 | 0.7 | 总结完整证明策略，为什么这个反例有效？ | 几何翻译+Danielewski曲面，A¹吸收了无穷远点的拓扑差异 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.4
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4

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
- structure_features: 多项式环消去问题的反例构造；需要构造具体环R,S；关键难点在于识别从纯代数到代数几何的领域翻译需求；反例使用正维数仿射簇（Danielewski曲面）而非有限/Artinian环
- key_objects: 交换环R,S, 多项式环R[x], 环同构R[x]≅S[x], 非同构R⇏S, Danielewski曲面W_n={x^n·y=z²-1}, 仿射直线A¹, 簇的积X×A¹, 仿射簇的坐标环, Zariski消去问题

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [geometric_translation, counterexample_construction, failed_approach_diagnosis, literature_recall, structural_invariant_analysis]
- primary_pattern: geometric_translation
- knowledge_required: [polynomial ring isomorphism, Zariski cancellation problem, Danielewski surfaces, affine algebraic geometry, coordinate rings of affine varieties, nilradical structure of Artinian rings, points at infinity of affine varieties]
- key_insight: R[x]≅S[x]几何翻译为X×A¹≅Y×A¹，Danielewski曲面提供非同构簇在乘以仿射直线后同构的显式反例

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 代数环同构问题（algebraic ring isomorphism problem）
- translation_to: 几何簇×仿射直线同构问题（geometric variety × affine line isomorphism problem）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: method_translation}
- tell_small_concepts: [cancellation problem, polynomial ring extension, Danielewski surface, affine line product, Zariski cancellation, points at infinity, geometric translation]
- expected_ai_method: direct_manipulation — bare AI会尝试直接代数构造R,S，可能尝试有限/Artinian环或简单商环，无法识别几何翻译的需求
- correct_method: geometric_translation via Danielewski surfaces — 将R[x]≅S[x]翻译为X×A¹≅Y×A¹，使用代数几何中的已知反例

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是，structural_existence + direct_manipulation + method_translation均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？是，三个维度足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，当前拓扑分类足够覆盖此题

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
- bare_ai_error_prediction: bare AI会尝试用有限/Artinian环构造R,S（如k[x]/(x^n) vs k[x,y]/(x^a,y^b)），失败于幂零结构在多项式扩张下保持。不会知道Danielewski曲面或几何翻译到Zariski消去问题。即使考虑几何方法，也缺乏W_n×A¹≅W_m×A¹的具体知识。
- suitable_for_poc: [POC-VMS-8 (hint injection — R4的几何翻译提示是强方向性提示), POC-VMS-9/10 (tell detection — R3失败的Artinian方法是可检测的分叉信号)]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/fate_000336/profile.json`。所有字段均已填写，包括tell_hint_pairs（7个局部pair，每个含tell_topology和tell_small_concepts）、global_tell_hint_pairs（2个全局pair，含why_not_visible_locally）、qa_sequence（7轮+stats）。

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
2. 更新`problem_extraction_progress`集合中`_key="396446"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000336"
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
    '_key': '396446',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000336',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000336')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: fate_000336
- solution_method_type: geometric_translation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，当前拓扑分类足够
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
