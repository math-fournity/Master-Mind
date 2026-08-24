# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000309
- **文件路径**: subagents-dirs/fate_000309/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396419（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000309/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设R是Noetherian domain，且对R的每个极大理想P，局部环R_P是UFD（factorial）。设I⊂R是理想。证明：I是可逆理想当且仅当I具有纯余维数1（即I的每个相伴素理想余维数为1；当I=R时无相伴素理想，也视为满足条件）。Lean形式化中，Invertible定义为I≠⊥且存在非零理想N使得N·I是主理想；纯余维数1形式化为∀(p : associatedPrimes R I), ringKrullDim(R ⧸ p.1)=1。
- 解答核心思路（1-2句话）：通过局部化将问题归结到局部UFD上，利用"可逆理想=局部主理想"和"UFD中高度1素理想是主理想"两个关键性质，在两个方向上分别建立等价。
- 解答关键步骤列表：
  1. 正向（可逆→纯余维数1）：I可逆→在每个R_P中I_P是主理想；p是I的相伴素理想→pR_p是I_p的相伴素理想；在UFD R_p中，非零主理想的相伴素理想高度为1→ht(p)=1。
  2. 反向（纯余维数1→可逆）：I的每个相伴素理想ht=1；对任意极大理想P局部化到R_P（UFD）；I_P的相伴素理想在R_P中高度为1→在UFD中是主理想→I_P是主理想；Noetherian环中有限生成+局部主理想→可逆理想。
  3. 核心桥梁：UFD中高度1素理想是主理想（Kaplansky定理的推论）。

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
| 1 | 纯元认知观察 | 0.7 | 请描述这道题的结构：已知条件是什么？要证明什么？这是一个什么类型的命题？ | 这是一个充要条件命题。已知R是Noetherian domain且每个极大理想处的局部化R_P是UFD，要证明理想I可逆当且仅当I具有纯余维数1（I的每个相伴素理想余维数为1）。两个方向需要分别证明。 |
| 2 | 自由列举 | 0.8 | 要证明这个充要条件，可以列出哪些可能的证明方向和工具？ | 方向1：直接用可逆理想定义证明两个方向。方向2：利用局部化将问题归结到局部环。方向3：利用Noetherian环中相伴素理想的性质。方向4：利用UFD中高度1素理想是主理想。方向5：利用局部主理想与可逆理想的等价关系。方向6：利用理想的局部-全局原则。 |
| 3 | 小尝试 | 0.5 | 尝试直接用可逆理想的定义证明正向（I可逆→纯余维数1），不使用局部化。I可逆意味着存在N使得NI是主理想。这能直接推出相伴素理想的余维数吗？ | 直接用定义比较困难。NI是主理想只能说明I和N在某种意义上互逆，但无法直接控制I的相伴素理想的余维数。需要更精细的工具来分析相伴素理想的结构，可能需要局部化。 |
| 4 | 思维操作引导 | 0.4 | 考虑在相伴素理想p处做局部化。I可逆意味着什么局部性质？在UFD中，主理想和高度1素理想有什么关系？ | I可逆意味着在每个局部环R_P中I_P是主理想（可逆理想局部化后是主理想）。在UFD中，高度1的素理想是主理想。如果p是I的相伴素理想，则pR_p是I_p的相伴素理想。由于I_p是非零主理想，在UFD中其相伴素理想高度为1，因此ht(p)=1。 |
| 5 | 推进 | 0.6 | 继续推进正向证明：如何严格论证在R_p中，I_p是主理想蕴含p的余维数为1？请写出完整论证链。 | 1) I可逆→I在每个R_P中是主理想（可逆理想的基本性质）。2) p是I的相伴素理想→pR_p是I_p的相伴素理想（局部化保持相伴素理想）。3) I_p=(a)是非零主理想。4) 在UFD R_p中，a有唯一因子分解，a的素因子对应高度1素理想。5) pR_p是(a)的相伴素理想→pR_p是a的某个素因子对应的素理想→ht(pR_p)=1。6) ht(p)=ht(pR_p)=1，即codim(p)=1。 |
| 6 | 思维操作引导 | 0.4 | 现在考虑反向（纯余维数1→I可逆）。如何利用"每个相伴素理想余维数为1"和"局部UFD"条件？关键定理是什么？ | 反向证明：1) I的每个相伴素理想p满足ht(p)=1。2) 对任意极大理想P，局部化到R_P（UFD）。3) 在R_P中，I_P的相伴素理想都是高度1的素理想。4) 在UFD中高度1素理想是主理想，因此I_P可分解为主理想的乘积→I_P是主理想。5) I在Noetherian环中有限生成，且在每个极大理想处局部化后是主理想→I是可逆理想（局部主理想等价于可逆，这是关键定理）。 |
| 7 | 能量传递引导 | 0.7 | 总结整个证明的核心脉络。为什么"局部UFD+纯余维数1"恰好等价于"可逆"？这个等价的本质是什么？ | 本质在于：可逆理想=局部主理想（在Noetherian环中）。而局部UFD条件下，局部主理想恰好对应于相伴素理想高度为1的理想。因此"可逆"和"纯余维数1"在局部UFD的Noetherian domain中是同一回事。两个方向都通过局部化归结到UFD中主理想与高度1素理想的对应关系。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 4.1
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

---

## Step 3: 标注问题拓扑层 [x]

**操作**：从题目结构中提取

**产出**：
- problem_type: characterization
- structure_features: 充要条件命题（iff），需要两个方向分别证明；通过局部化将全局性质归结为局部性质；涉及相伴素理想、余维数、可逆理想三个概念的等价刻画
- key_objects: Noetherian domain, locally UFD (R_P factorial for all maximal P), invertible ideal, associated primes, pure codimension 1, localization at primes, height-1 primes in UFD

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["localization_reduction", "biconditional_decomposition", "property_transport_under_localization", "UFD_height_one_prime_principal", "local_global_principle"]
- primary_pattern: localization_reduction
- knowledge_required: ["invertible ideals and their local properties", "associated primes and localization", "UFD: height-1 primes are principal", "locally principal ideals are invertible in Noetherian rings", "codimension/height of prime ideals", "Noetherian ring theory"]
- key_insight: 在局部UFD的Noetherian domain中，可逆理想=局部主理想，而局部主理想恰好对应相伴素理想高度为1的理想，因此"可逆"与"纯余维数1"是同一回事

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 全环上的理想性质（可逆、相伴素理想、余维数）的全局刻画
- translation_to: 局部环R_P上的主理想性质和UFD中高度1素理想性质的局部刻画
- translation_type: local_global_reduction（局部-全局归结：将全局充要条件通过局部化翻译为局部环上的主理想性质）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "logical_deduction", gap_type: "knowledge_gap"}
- tell_small_concepts: ["invertible ideal", "associated prime", "pure codimension 1", "locally UFD", "localization at prime", "height-1 prime principal in UFD", "locally principal ideal"]
- expected_ai_method: 直接逻辑推演——尝试用可逆理想定义和相伴素理想定义直接推导，不使用局部化将问题归结到局部UFD上
- correct_method: 局部化归结——在每个相伴素理想/极大理想处局部化，利用UFD中高度1素理想是主理想的性质，以及局部主理想等价于可逆理想

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type=characterization、ai_method_type=logical_deduction、gap_type=knowledge_gap均能归入已有拓扑类别，够用。
- [x] 粒度是否一致——characterization是已有抽象值，logical_deduction是已有抽象值，knowledge_gap是已有抽象值，粒度一致。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell。gap_type=knowledge_gap准确反映了bare AI缺乏"局部化归结+UFD高度1素理想性质"这一关键知识。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有拓扑分类体系可覆盖。

**拓扑进化建议**（如有）：无。现有分类体系充分。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对充要条件命题，需要识别两个方向和可用条件结构 | 描述题目结构，识别已知条件和证明目标 | 0.7 | 纯元认知观察 | false | {characterization, logical_deduction, method_problem_mismatch} | ["iff statement", "Noetherian domain", "locally UFD", "invertible ideal", "pure codimension 1"] |
| 2 | AI需要列举可用工具但可能遗漏局部化这一关键方向 | 列出所有可能方向，特别关注局部化和UFD性质 | 0.8 | 自由列举 | false | {characterization, logical_deduction, method_problem_mismatch} | ["localization", "UFD height-1 prime", "associated prime", "locally principal", "invertible ideal definition"] |
| 3 | AI尝试直接用定义证明但缺乏局部化视角，在全局层面卡住 | 试直接用定义，发现需要局部化工具 | 0.5 | 小尝试 | false | {characterization, direct_manipulation, method_problem_mismatch} | ["invertible ideal definition", "NI principal", "associated prime codimension", "global argument limitation"] |
| 4 | AI需要知道可逆理想局部化为主理想和UFD中高度1素理想是主理想这两个关键性质 | 在相伴素理想处做局部化，利用UFD中高度1素理想是主理想 | 0.4 | 思维操作引导 | true | {characterization, logical_deduction, knowledge_gap} | ["invertible localizes to principal", "UFD height-1 prime principal", "associated prime localization", "codimension equals height"] |
| 5 | AI需要严格论证局部化后主理想的相伴素理想高度为1的完整链条 | 推进正向证明的严格论证链 | 0.6 | 推进 | false | {characterization, logical_deduction, structural_transformation} | ["localization preserves associated primes", "UFD factorization", "prime factor height 1", "height equals codimension"] |
| 6 | AI需要知道局部主理想等价于可逆理想这一关键定理来完成反向证明 | 利用局部主理想等价于可逆理想，通过局部化归结 | 0.4 | 思维操作引导 | true | {characterization, logical_deduction, knowledge_gap} | ["locally principal equals invertible", "Noetherian finite generation", "UFD height-1 prime principal", "local-global principle"] |
| 7 | AI需要整合两个方向的理解形成统一视角 | 总结核心脉络：可逆=局部主理想=纯余维数1 | 0.7 | 能量传递引导 | false | {characterization, logical_deduction, method_translation} | ["invertible equals locally principal", "locally UFD", "pure codimension 1 equivalence", "localization bridge"] |

**全局pairs详情**：

1. path_feature型：
   - scope: 完整证明路径
   - observation_point: null
   - tell: 证明的两个方向都通过局部化归结到同一个局部性质——UFD中主理想与高度1素理想的对应关系
   - hint: 在两个方向中都使用局部化，将全局充要条件翻译为局部UFD中的主理想性质
   - hint_level: 0.6
   - generalizability: "high — 局部-全局归结策略适用于所有涉及局部环性质的交换代数充要条件证明"
   - why_not_visible_locally: "在单个步骤中只能看到局部化操作，无法看到两个方向共享同一个局部性质桥梁这一路径特征。需要完整走完两个方向后才能识别出对称结构。"
   - tell_topology: {characterization, logical_deduction, method_translation}
   - tell_small_concepts: ["localization reduction", "UFD height-1 prime principal", "locally principal", "local-global bridge", "symmetric argument structure"]

2. implicit型：
   - scope: 整个证明
   - observation_point: "R4"
   - tell: "可逆理想=局部主理想"这一等价是连接两个方向的隐藏桥梁，但题目中并未直接提及局部主理想
   - hint: 识别可逆理想在局部环中的表现是主理想，这是连接"可逆"与"纯余维数1"的中间概念
   - hint_level: 0.5
   - generalizability: "high — '可逆=局部主理想'是交换代数中的基本定理，适用于所有Noetherian环上可逆理想的刻画"
   - why_not_visible_locally: "题目只涉及'可逆'和'纯余维数1'两个概念，'局部主理想'作为中间桥梁在题目中完全不可见。只有在R4引入局部化后才隐含出现，且需要知道'可逆理想局部化为主理想'这一定理才能识别。"
   - tell_topology: {characterization, logical_deduction, knowledge_gap}
   - tell_small_concepts: ["invertible equals locally principal", "hidden bridge concept", "intermediate property", "Noetherian ring theorem"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI很可能尝试直接用可逆理想定义和相伴素理想定义进行逻辑推演，不使用局部化将问题归结到局部UFD上。即使想到局部化，也可能不知道"UFD中高度1素理想是主理想"和"局部主理想等价于可逆理想"这两个关键定理，导致无法完成两个方向的证明。对于高级交换代数定理，bare AI缺乏足够的专业知识储备。
- suitable_for_poc: ["POC-VMS-8 hint端验证——测试注入局部化方向hint后AI能否完成证明", "POC-VMS-9 tell端验证——测试从AI的thinking中识别'未使用局部化'这一分叉信号", "知识瓶颈POC——测试knowledge_gap型tell的识别和hint注入"]
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
2. 更新`problem_extraction_progress`集合中`_key="396419"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000309"
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
    '_key': '396419',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000309',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000309')
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
- problem_id: fate_000309
- solution_method_type: localization_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类体系（characterization/logical_deduction/knowledge_gap等）充分覆盖
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
