# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000273
- **文件路径**: subagents-dirs/fate_000273/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396383（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000273/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let p_1, ..., p_r be r different prime numbers. Prove that the Galois group of K = Q(sqrt(p_1), ..., sqrt(p_r)) over Q is (Z/2Z)^r, where Z/2Z is the cyclic group of order 2.
- 解答核心思路（1-2句话）：通过对r归纳，先用关键引理（sqrt(p_i)不在之前域中，用符号变换自同构隔离基系数证明）得到[K:Q]=2^r，再利用Galois对应|Gal|=[K:Q]和符号向量构造显式同构。
- 解答关键步骤列表：
  1. 关键引理：sqrt(p_r)不在K'=Q(sqrt(p_1),...,sqrt(p_{r-1}))中——用K'的Q基{prod sqrt(p_i)}和符号变换自同构sigma_j隔离系数，推出sqrt(p_r)∈Q矛盾
  2. 归纳证明[K:Q]=2^r（塔律+引理保证每步扩张度为2）
  3. K是(x^2-p_1)...(x^2-p_r)的分裂域，故K/Q Galois，|Gal|=2^r
  4. 每个自同构将sqrt(p_i)映到±sqrt(p_i)，共2^r个选择，全部有效
  5. 构造符号向量同构phi: Gal→(Z/2Z)^r，验证是群同构

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
| 1 | 纯元认知观察 | 0.8 | 描述K的结构：Q(sqrt(p_i))/Q是什么扩张？sqrt(p_i)的极小多项式？目标群(Z/2Z)^r的结构？ | 每个Q(sqrt(p_i))/Q是二次扩张，极小多项式x^2-p_i。K是r个二次扩张的复合。(Z/2Z)^r是2^r阶初等交换2-群，暗示每个自同构独立翻转sqrt(p_i)的符号。 |
| 2 | 自由列举 | 0.7 | 确定Galois群需要哪些信息？列出所有可能方法：计算[K:Q]、直接枚举自同构、Galois对应、基本定理。哪个应先建立？ | 关键方法：归纳用塔律计算[K:Q]；通过生成元作用枚举自同构；Galois扩张有|Gal|=[K:Q]；构造显式同构。度数计算应优先，因为它给出群阶。 |
| 3 | 小尝试 | 0.5 | 试归纳计算[K:Q]。归纳步需要[K:K']=2，即x^2-p_r在K'上不可约，即sqrt(p_r)不在K'中。如何证明？ | 尝试：假设sqrt(p_r)∈K'，则x^2-p_r在K'上可约。需推出矛盾。关键认识：K'有Q基{prod sqrt(p_i)}，可用符号变换自同构隔离系数。 |
| 4 | 思维操作引导 | 0.3 | 用K'的Q基写出sqrt(p_r)=sum a_S prod sqrt(p_i)，施以sigma_j翻转sqrt(p_j)符号，两式相加隔离含j的系数。j任意取，结论是什么？ | 施sigma_j后：-sqrt(p_r)=sum (-1)^{[j∈S]} a_S prod sqrt(p_i)。相加得0=2*sum_{S:j∈S} a_S prod，故a_S=0对所有含j的S。j任意，故所有非空S的a_S=0，sqrt(p_r)=a_∅∈Q，矛盾。引理得证。 |
| 5 | 推进 | 0.4 | [K:Q]=2^r已知。K是分裂域故Galois，|Gal|=2^r。每个自同构将sqrt(p_i)映到±sqrt(p_i)，至多2^r个选择，全部有效。继续——还需证明什么？ | 有2^r个自同构，每个由符号向量(eps_1,...,eps_r)决定。还需构造显式同构phi:Gal→(Z/2Z)^r并验证是群同态、单射、满射。 |
| 6 | 思维操作引导 | 0.2 | 定义phi(sigma)=(eps_1,...,eps_r)其中sigma(sqrt(p_i))=(-1)^eps_i sqrt(p_i)。验证：(1)同态(2)单射(3)满射。 | (1)同态：复合对应符号加法。(2)单射：phi(sigma)=0则sigma固定所有sqrt(p_i)，故固定K，sigma=id。(3)满射：两群均2^r阶，单射即满射。 |
| 7 | 能量传递引导 | 0.6 | 所有部件齐备。组装完整证明：(1)关键引理(2)归纳得[K:Q]=2^r(3)Galois故|Gal|=2^r(4)符号向量同构。证明完成！ | 完整证明组装：归纳+关键引理得[K:Q]=2^r；K是分裂域故Galois，|Gal|=2^r；符号向量映射phi是同构。因此Gal(Q(sqrt(p_1),...,sqrt(p_r))/Q)≅(Z/2Z)^r。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R3

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
- structure_features: 归纳结构（对素数个数归纳）、关键引理（平方根线性无关性）、度数计算（塔律）、Galois对应（|Gal|=[K:Q]）、显式同构构造（符号向量映射）
- key_objects: K=Q(sqrt(p_1),...,sqrt(p_r))、Galois群Gal(K/Q)、(Z/2Z)^r、极小多项式x^2-p_i、多重二次扩张的Q基（平方根乘积）、符号变换自同构sigma_j

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [归纳结构识别, 关键引理识别, 自同构作用反证法, 度数-群阶连接, 显式同构构造]
- primary_pattern: 归纳结构识别（inductive_structure_recognition）
- knowledge_required: [Galois理论：Galois群/Galois扩张/分裂域, 域扩张度数与塔律, 极小多项式与不可约性, 自同构对生成元的作用, 二次扩张Q(sqrt(d)), 多重二次扩张的基, 基本定理|Gal(K/Q)|=[K:Q]对Galois扩张]
- key_insight: 符号变换自同构可以用来隔离基的个别系数，从而证明sqrt(p_r)不在K'中——这是让归纳成立的关键引理

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接Galois群计算（直接枚举自同构）
- translation_to: 度数计算（归纳+关键引理）+ Galois对应 + 显式同构构造
- translation_type: method_translation（方法翻译：从直接群枚举翻译为先算度数再用Galois对应）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: [多重二次扩张的Galois群, 平方根线性无关, 符号变换自同构, 塔律归纳, 符号向量同构]
- expected_ai_method: 直接枚举自同构（注意到每个sqrt(p_i)映到±sqrt(p_i)得2^r个选择），但不先证明[K:Q]=2^r和关键引理，无法证明所有选择都有效
- correct_method: 归纳法：先证关键引理（sqrt(p_i)不在之前域中，用符号变换自同构隔离基系数），再算度数=2^r，用Galois对应得|Gal|=2^r，构造显式符号向量同构

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是，characterization/direct_calculation/knowledge_gap均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是，粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？是，三个维度足够
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无。已有拓扑分类体系完全覆盖此题。

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

详见profile.json中的tell_hint_pairs和global_tell_hint_pairs字段。每个pair均包含tell_topology和tell_small_concepts。全局pair均包含why_not_visible_locally（非None）。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: Bare AI会直接枚举自同构（注意到每个sqrt(p_i)映到±sqrt(p_i)得2^r个选择），但跳过度数计算和关键引理，无法证明所有2^r个符号选择都是有效自同构。没有[K:Q]=2^r的证明，就不能用|Gal|=[K:Q]来确认所有选择有效。也可能无法构造显式群同构并验证。
- suitable_for_poc: [POC-VMS-hint: 测试度数优先策略提示能否将AI从直接枚举重定向到归纳度数计算, POC-VMS-tell: 测试能否从AI的thinking轨迹中检测到缺失关键引理（平方根线性无关性）的tell, POC-VMS-knowledge: 测试符号变换自同构技术是否是需要显式提示的知识瓶颈]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/fate_000273/profile.json`。所有字段均已填写：
- _key=fate_000273, source_id=FATE-X-24, source_dataset=FATE-X, schema_version=3
- problem_text, solution_text, solution_summary, domain, subfield, answer_type=proof, answer="Gal(Q(sqrt(p_1),...,sqrt(p_r))/Q) is isomorphic to (Z/2Z)^r"
- problem_type=characterization, solution_method_type=structural_induction
- structure_features, key_objects, thinking_patterns, primary_pattern, knowledge_required, key_insight
- translation_from/to/type, tell_topology(profile级), tell_small_concepts(profile级), expected_ai_method, correct_method
- tell_hint_pairs(7个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts)
- global_tell_hint_pairs(2个全局pair：1个path_feature型+1个implicit型，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts)
- bare_ai_expected=fail, bare_ai_error_prediction, suitable_for_poc, discriminates_levels=true
- qa_sequence(7轮rounds + stats子对象，knowledge_bottleneck="R4", thinking_bottleneck="R3")
- analysis_metadata(analyzed_by/analyzed_at/analysis_duration/notes)

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
2. 更新`problem_extraction_progress`集合中`_key="396383"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000273"
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
    '_key': '396383',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000273',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000273')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证输出：fate_000273, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: fate_000273
- solution_method_type: structural_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类体系完全覆盖此题
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
