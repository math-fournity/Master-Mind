# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000364
- **文件路径**: subagents-dirs/fate_000364/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396474（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000364/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let R be a Noetherian domain, and suppose that for every maximal ideal P of R the ring R_P is factorial. Let I ⊂ R be an ideal. Prove that I is an invertible module iff I has pure codimension 1. (Pure codimension 1 = every associated prime of I has codimension 1; includes I=R with no associated primes.)
- 解答核心思路（1-2句话）：利用"可逆理想等价于局部主理想"这一桥梁，将全局可逆性翻译为局部主理想性质，再利用UFD中高度1素理想是主理想的事实，建立局部主理想与相伴素理想余维数1之间的等价。
- 解答关键步骤列表：
  1. 正向（可逆→纯余维1）：I可逆→I在每个极大理想P处局部化I_P是R_P中主理想→R_P是UFD，主理想的相伴素理想余维数1（或I_P=R_P无相伴素理想）→通过相伴素理想局部化行为回到I的相伴素理想余维数1
  2. 反向（纯余维1→可逆）：I纯余维1→I_P的相伴素理想在R_P中余维数1→R_P是UFD，高度1素理想是主理想→I_P的准素分解各分量是主理想幂→I_P本身是主理想→I局部主理想→I可逆
  3. 关键桥梁：可逆=局部主理想（Noetherian环中有限生成理想的基本性质）
  4. 关键定理：UFD中高度1素理想是主理想（由素元生成）

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
| 1 | 纯元认知观察 | 0.3 | 观察这道题的结构：要证明什么等价关系？已知条件是什么？关键数学对象有哪些？ | 要证明I可逆当且仅当I有纯余维数1。已知R是Noetherian整环，且每个极大理想P处R_P是factorial的。关键对象：可逆理想、相伴素理想、余维数、局部化、UFD。 |
| 2 | 自由列举 | 0.5 | 列出证明这个等价关系所有可能的方向和工具。 | 1)直接用可逆定义证明；2)利用局部化把全局化为局部；3)利用UFD性质（高度1素理想是主理想）；4)利用相伴素理想在局部化下的行为；5)利用Noetherian环中局部主理想等价于可逆。 |
| 3 | 小尝试 | 0.4 | 尝试直接用可逆理想的定义（存在N使NI主理想）证明正向方向，会遇到什么困难？ | 直接用定义：I可逆意味着存在N使NI主理想且N≠0。但定义中N是全局的，而余维数是关于素理想的局部性质。直接从定义出发缺乏局部-全局的桥梁，无法将全局乘积结构与相伴素理想的余维数联系起来。 |
| 4 | 思维操作引导 | 0.6 | 执行思维操作：将"可逆"翻译为"局部主理想"。在Noetherian环中，有限生成理想可逆当且仅当它在每个极大理想处局部化后是主理想。用这个翻译重新审视正向方向。 | 如果I可逆，则对每个极大理想P，I_P是R_P中的主理想。R_P是UFD。在UFD中，主理想(a)的相伴素理想要么为空（a是单位），要么是高度1素理想（a的非单位因子生成的）。因此I_P的相伴素理想都有余维数1。 |
| 5 | 推进 | 0.5 | 继续推进：从I_P的相伴素理想有余维数1，如何回到I的相伴素理想的余维数？ | 相伴素理想在局部化下的行为：Ass(I_P)={q_P : q∈Ass(I), q⊆P}。若I_P的相伴素理想在R_P中余维数1，则对每个q∈Ass(I)且q⊆P，q_P在R_P中余维数1。由于q⊆P时q的余维数等于q_P在R_P中的余维数，所以q在R中余维数1。 |
| 6 | 思维操作引导 | 0.7 | 现在处理反向：纯余维1→可逆。执行思维操作——在UFD中，所有相伴素理想高度为1的理想有什么特殊性质？ | 在UFD中，高度1素理想是主理想（由素元生成）。若I_P的所有相伴素理想高度1，则I_P的准素分解中每个分量是主理想幂。在UFD中，高度1素理想幂的乘积是主理想，所以I_P本身是主理想。因此I局部主理想，故I可逆。 |
| 7 | 能量传递引导 | 0.3 | 把两个方向合在一起，完整叙述证明。你已经掌握了所有关键步骤。 | 正向：I可逆→I局部主理想→I_P在UFD中是主理想→I_P相伴素理想余维数1→I的相伴素理想余维数1。反向：I纯余维1→I_P相伴素理想余维数1→UFD中I_P是主理想→I局部主理想→I可逆。等价得证。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.3
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 双向等价证明（iff），需要同时证明正向和反向；核心桥梁是"局部主理想"概念；涉及局部-全局转换
- key_objects: ["Noetherian整环R", "极大理想P", "局部化R_P", "factorial/UFD", "理想I", "可逆理想", "相伴素理想", "余维数/codimension", "主理想", "准素分解"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["localization_reduction", "equivalence_biproof", "property_translation", "global_local_bridge"]
- primary_pattern: localization_reduction
- knowledge_required: ["Noetherian环理论", "局部化", "UFD/因子分解", "相伴素理想", "可逆理想", "Krull维数/余维数", "准素分解", "局部主理想等价于可逆"]
- key_insight: 可逆理想等价于局部主理想，而在UFD中局部主理想恰好对应于相伴素理想余维数1——"局部主理想"是连接可逆性和余维数的桥梁概念

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 全局可逆性定义（存在N使NI主理想）
- translation_to: 局部主理想性质（每个极大理想处局部化后是主理想）
- translation_type: localization_translation（局部化翻译——将全局代数性质翻译为局部环上的性质）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: method_translation}
- tell_small_concepts: ["局部主理想", "局部化", "UFD高度1素理想", "相伴素理想余维数", "可逆=局部主理想", "准素分解"]
- expected_ai_method: bare AI会尝试直接用可逆理想的定义（存在N使NI主理想）进行逻辑推导，但无法建立全局乘积结构与相伴素理想余维数之间的联系
- correct_method: 通过局部化将可逆性翻译为局部主理想性质，利用UFD中高度1素理想是主理想的定理，建立局部主理想与相伴素理想余维数1的等价

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type(characterization)/ai_method_type(direct_manipulation)/gap_type(method_translation)均能归入已有拓扑类别
- [x] 粒度是否一致——标注值与已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无。已有拓扑分类体系足够覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs摘要**：
- R1: tell=AI看到等价关系但可能忽略局部factorial条件的作用, hint=观察题目结构识别局部化条件, level=0.3, 纯元认知观察, topology=(characterization, logical_deduction, knowledge_gap), concepts=[等价关系, 局部化条件, Noetherian整环]
- R2: tell=AI可能列举方向但不一定想到局部-全局桥梁, hint=列出所有方向特别关注局部化方法, level=0.5, 自由列举, topology=(characterization, enumeration_brute_force, method_problem_mismatch), concepts=[局部化, UFD性质, 相伴素理想]
- R3: tell=AI直接用定义会卡在全局-局部桥梁缺失, hint=尝试直接用定义发现困难, level=0.4, 小尝试, topology=(characterization, direct_manipulation, method_problem_mismatch), concepts=[可逆定义, 主理想, 全局-局部]
- R4: tell=AI需要将可逆翻译为局部主理想这个关键思维操作, hint=执行翻译操作可逆↔局部主理想, level=0.6, 思维操作引导, topology=(characterization, direct_manipulation, method_translation), concepts=[局部主理想, Noetherian环, 极大理想局部化]
- R5: tell=AI需要理解相伴素理想在局部化下的行为, hint=从局部相伴素理想回到全局, level=0.5, 推进, topology=(characterization, logical_deduction, knowledge_gap), concepts=[相伴素理想局部化, 余维数, 素理想包含关系]
- R6: tell=AI需要知道UFD中高度1素理想是主理想这一关键定理, hint=在UFD中高度1素理想的性质, level=0.7, 思维操作引导, is_knowledge_bottleneck=true, topology=(characterization, logical_deduction, knowledge_gap), concepts=[UFD高度1素理想, 主理想, 准素分解]
- R7: tell=AI需要整合两个方向完成证明, hint=收尾整合, level=0.3, 能量传递引导, topology=(characterization, logical_deduction, structural_transformation), concepts=[正向方向, 反向方向, 局部主理想桥梁]

**全局pairs摘要**：
- G1 (path_feature): tell=证明的关键桥梁是局部主理想——可逆性通过局部化翻译为局部主理想，而UFD性质将局部主理想与余维数1联系起来, hint=识别局部主理想作为连接可逆性和余维数的桥梁概念, level=0.6, why_not_visible_locally=局部步骤中只能看到单方向的推导，桥梁概念的作用需要同时看到两个方向才能识别
- G2 (implicit): tell=反向方向隐含使用了UFD中所有相伴素理想高度为1的理想是主理想这个组合定理, hint=在UFD中高度1素理想是主理想且幂的乘积是主理想, level=0.7, observation_point=R6, why_not_visible_locally=这个定理的使用在局部步骤中被折叠为一个推理步骤，但背后的组合需要单独的知识调用

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接用可逆理想的定义（存在N使NI主理想）进行逻辑推导，但无法建立全局乘积结构与相伴素理想余维数之间的联系。关键缺失是"可逆=局部主理想"这个翻译步骤——AI不会主动将全局可逆性局部化，因此卡在定义层面无法推进。即使知道UFD性质，也无法将其与可逆性定义连接。
- suitable_for_poc: ["POC-VMS-hint-injection", "POC-VMS-tell-detection", "POC-VMS-knowledge-bottleneck"]
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
2. 更新`problem_extraction_progress`集合中`_key="396474"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000364"
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
    '_key': '396474',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000364',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000364')
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
