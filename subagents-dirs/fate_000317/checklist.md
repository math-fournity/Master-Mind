# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000317
- **文件路径**: subagents-dirs/fate_000317/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396427（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000317/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let A be a Noetherian local ring with maximal ideal m. For any f ∈ m such that f is not nilpotent, A_f is Jacobson.
- 解答核心思路（1-2句话）：用Jacobson环等价刻画（R是Jacobson iff对每个素理想P，R/P的Jacobson根=幂零根）归约到整环情形，再证明Noetherian整环R中f≠0时R_f的Jacobson根为(0)，关键在于Noetherian性保证不含f的极大素理想的交=所有不含f的素理想的交=(0):f^∞=(0)。
- 解答关键步骤列表：
  1. 用等价刻画归约：R是Jacobson iff对每个素P，J(R/P)=nil(R/P)
  2. 对A_f的素理想P（对应A中不含f的素理想p），A_f/P ≅ (A/p)_f̄，其中A/p是Noetherian整环，f̄≠0
  3. 关键引理：Noetherian整环R中f≠0，R_f的Jacobson根=(0)
  4. 引理证明：∩{不含f的极大素理想}=∩{所有不含f的素理想}（Noetherian性保证每个不含f的素理想含于某个极大的）=(0):f^∞=(0)（整环中f≠0）
  5. 结论：A_f的每个素商都是Jacobson，故A_f是Jacobson

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
| 1 | 纯元认知观察 | 0.8 | 这个问题的已知条件和目标是什么？涉及哪些核心代数对象？它们之间有什么关系？ | 已知：Noetherian局部环(A,m)，f∈m且f非幂零。目标：证明A_f是Jacobson环。核心对象：Noetherian局部环、极大理想、局部化Localization.Away、Jacobson环。关键关系：f∈m意味着反转f会移除m对应的素理想。 |
| 2 | 自由列举 | 0.7 | 证明一个环是Jacobson环有哪些可能的途径？列出你能想到的所有方法。 | (a)直接用定义：每个素理想=极大理想的交；(b)等价刻画：对每个素P，R/P的Jacobson根=幂零根；(c)Noetherian归纳法；(d)利用维数下降dim(A_f)<dim(A)做归纳；(e)利用Stacks Project已知引理；(f)利用Jacobson环在局部化下封闭的性质。 |
| 3 | 小尝试 | 0.4 | 试用定义直接证明：取A_f的任一素理想P，证明P是A_f中包含P的极大理想的交。这个方向可行吗？ | A_f的素理想对应A中不含f的素理想。因f∈m，这些素理想都严格包含于m。A_f的极大理想对应A中不含f的极大素理想。需要证明p=∩{q:q在不含f的素理想中极大,q⊇p}。这个方向不太直接——需要利用Noetherian性来连接极大素理想和所有素理想，但直接操作比较困难。 |
| 4 | 思维操作引导 | 0.5 | 换一个角度：用Jacobson环的等价刻画——R是Jacobson当且仅当对每个素理想P，R/P的Jacobson根等于幂零根。这能把问题简化到什么情况？ | 对A_f的每个素理想P（对应A中不含f的素理想p），A_f/P≅(A/p)_f̄，其中f̄是f在A/p中的像。因p是素理想且f∉p，A/p是Noetherian整环且f̄≠0。所以问题归约为：Noetherian整环R中非零元素f，R_f的Jacobson根为(0)。 |
| 5 | 推进 | 0.6 | 现在需要证明：Noetherian整环R中f≠0，R_f的Jacobson根为(0)。即R_f中所有极大理想的交为(0)。这等价于什么关于R中素理想的陈述？ | R_f的极大理想对应R中不含f的极大素理想（在不含f的素理想中极大的）。需要证明这些素理想的交为(0)。即∩{q:q在不含f的素理想中极大}=(0)。 |
| 6 | 思维操作引导 | 0.4 | 关键步骤：在Noetherian环中，"不含f的素理想中极大的那些"的交，和"所有不含f的素理想"的交，有什么关系？后者又等于什么？ | 由Noetherian性，每个不含f的素理想都包含在某个不含f的极大素理想中。因此∩{极大不含f的素理想}=∩{所有不含f的素理想}。后者={g:∃n,f^n·g=0}=(0):f^∞。在整环中f≠0，所以(0):f^∞=(0)。 |
| 7 | 能量传递引导 | 0.3 | 把所有步骤串起来，完成证明。 | 1)用Jacobson环等价刻画归约到整环情形；2)对Noetherian整环R和f≠0，R_f的极大理想的交=∩{不含f的极大素理想}=∩{所有不含f的素理想}=(0):f^∞=(0)；3)所以R_f的Jacobson根=(0)=幂零根，R_f是Jacobson环；4)回到原问题：A_f的每个素商都是Jacobson，故A_f是Jacobson。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

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
- structure_features: 给定Noetherian局部环和极大理想中非幂零元素，证明其局部化具有Jacobson性质。结构上是"在特定条件下构造的对象满足某性质"的表征型问题。
- key_objects: Noetherian局部环、极大理想m、非幂零元素f、局部化A_f、Jacobson环、素谱Spec(A)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["equivalent_characterization_reduction", "structural_reduction_to_domain", "Noetherian_maximality_argument", "colon_ideal_technique", "prime_spectrum_intersection"]
- primary_pattern: equivalent_characterization_reduction
- knowledge_required: ["Noetherian局部环", "环的局部化", "Jacobson环定义与等价刻画", "素谱与素理想对应", "Krull维数", "colon理想(0):f^∞", "Noetherian性与极大元存在性"]
- key_insight: 用Jacobson环等价刻画（R是Jacobson iff对每个素P，R/P的J=nil）归约到整环情形，再利用Noetherian性保证∩{不含f的极大素理想}=∩{所有不含f的素理想}=(0):f^∞=(0)

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接定义验证（直接检查每个素理想=极大理想的交）
- translation_to: 等价刻画归约 + colon理想技术（用R/P的Jacobson根=幂零根刻画，归约到整环，再用(0):f^∞计算素理想交集）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_calculation, gap_type: knowledge_gap}
- tell_small_concepts: ["Jacobson ring characterization", "localization primes correspondence", "Noetherian maximal prime existence", "colon ideal (0):f^infinity", "Jacobson radical equals nilradical"]
- expected_ai_method: bare AI会尝试直接用Jacobson环定义验证（取素理想，试图直接表达为极大理想的交），在Noetherian性连接极大素理想与所有素理想的步骤上卡住
- correct_method: 用等价刻画归约到整环情形，再用Noetherian性证明∩{不含f的极大素理想}=∩{所有不含f的素理想}=(0):f^∞=(0)

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=characterization, ai_method_type=direct_calculation, gap_type=knowledge_gap均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类足以覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接用Jacobson环定义验证（取素理想P，试图直接表达为极大理想的交），在需要利用Noetherian性连接"不含f的极大素理想"与"所有不含f的素理想"的步骤上卡住，不知道等价刻画归约和colon理想技术
- suitable_for_poc: ["tell_detection_poc", "knowledge_bottleneck_poc", "method_translation_poc"]
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
2. 更新`problem_extraction_progress`集合中`_key="396427"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000317"
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
    '_key': '396427',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000317',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000317')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000317
- solution_method_type: logical_deduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有拓扑分类足以覆盖
- 是否遇到异常: 无

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
