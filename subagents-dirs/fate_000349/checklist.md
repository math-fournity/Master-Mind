# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000349
- **文件路径**: subagents-dirs/fate_000349/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396459（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000349/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let R be a Noetherian ring, P be a countably generated projective R-module such that P_m has infinite rank for all maximal ideals m of R. Then P is free.
- 解答核心思路（1-2句话）：利用局部无限rank启用Eilenberg swindle（P ≅ P ⊕ F），结合Noetherian粘贴和迭代消去证明P ≅ F^(ℵ₀)是自由模。
- 解答关键步骤列表：
  1. P projective → P ⊕ Q = F（自由模直和项）
  2. 局部化：P_m ≅ R_m^(ℵ₀)（局部环上projective=free，infinite rank）
  3. Eilenberg swindle：P_m ≅ (P ⊕ F)_m（无限rank吸收自由直和项）
  4. Noetherian粘贴：P ≅ P ⊕ F（局部→全局）
  5. 迭代：P ≅ P ⊕ F^(ℵ₀)
  6. 消去：P ⊕ F^(ℵ₀) = P ⊕ (P⊕Q)^(ℵ₀) ≅ P^(ℵ₀) ⊕ Q^(ℵ₀) = F^(ℵ₀)（自由）
  7. 结论：P ≅ F^(ℵ₀)是自由模

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
| 1 | 纯元认知观察 | 0.3 | 观察题目结构：已知条件有哪些？要证明什么？哪个条件连接局部和全局？ | 识别三条件和结论，localization是关键桥梁 |
| 2 | 自由列举 | 0.5 | 列举证明projective=free的方法，特别思考infinite rank启用什么技术 | 列举方法，关键：Eilenberg swindle |
| 3 | 小尝试 | 0.4 | 尝试直接证明P≅R^(I)，能确定I吗？ | 直接构造困难，需局部化 |
| 4 | 思维操作引导 | 0.6 | 局部化：P_m有什么结构？projective在局部环上是什么？infinite rank意味什么？ | P_m≅R_m^(ℵ₀)，吸收可数自由直和项 |
| 5 | 推进 | 0.5 | Eilenberg swindle给出P_m≅(P⊕F)_m，如何推到全局？Noetherian起什么作用？ | Noetherian粘贴局部同构为全局P≅P⊕F |
| 6 | 思维操作引导 | 0.7 | 有P≅P⊕F和P⊕Q=F，如何迭代消去证明P自由？写出完整推导 | 迭代→P≅F^(ℵ₀)，消去→P自由 |
| 7 | 能量传递引导 | 0.8 | 整合所有线索，确认逻辑链条完整 | 完整7步证明链条，证毕 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R5

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
- structure_features: 三个假设（Noetherian, 可数生成投射, 局部无限rank）组合强制全局自由性。关键结构桥梁是局部化：局部无限rank启用Eilenberg swindle，Noetherian条件启用局部到全局的粘贴。
- key_objects: Noetherian环R, 可数生成投射R-模P, 极大理想m, 局部化P_m, 无限rank, 自由模F, 补项Q, Eilenberg swindle分解

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [localization_global_patch, algebraic_cancellation, structural_decomposition, infinite_rank_absorption]
- primary_pattern: localization_global_patch
- knowledge_required: [projective模作为自由模直和项, 模在素理想/极大理想处的局部化, 局部环上projective=free, 局部化模的rank, Eilenberg swindle, Noetherian环上局部到全局粘贴, Bass大投射模定理]
- key_insight: 局部无限rank启用Eilenberg swindle P ≅ P ⊕ F，结合P ⊕ Q = F和迭代得到P ≅ F^(ℵ₀)是自由模

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 局部代数（在极大理想处局部化，局部自由性）
- translation_to: 全局代数（模的全局自由性）
- translation_type: structural_transformation（局部到全局的结构转化）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: knowledge_gap}
- tell_small_concepts: [projective module, localization at maximal ideals, infinite rank, Eilenberg swindle, Noetherian patching, countably generated, direct summand of free module]
- expected_ai_method: direct_manipulation — bare AI会尝试直接构造同构P≅R^I或用有限rank投射模技术（Serre分裂/Quillen-Suslin），错过Eilenberg swindle
- correct_method: localization_cancellation — 局部化获取局部自由性+无限rank，Eilenberg swindle吸收自由直和项，Noetherian粘贴到全局，迭代消去得P自由

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是，structural_existence + direct_manipulation + knowledge_gap 均可归入已有类别
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是，与已有值粒度一致
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够，per-pair拓扑通过不同轮次的gap_type变化（method_problem_mismatch → knowledge_gap → structural_transformation → method_translation）区分
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，现有拓扑分类体系足够覆盖此题。

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
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试用有限rank投射模技术（Serre分裂/Quillen-Suslin），不认识infinite rank启用Eilenberg swindle，卡在确定rank或构造显式同构。Noetherian粘贴步骤也大概率遗漏。
- suitable_for_poc: [POC-VMS-tell-detection: 检测AI遗漏Eilenberg swindle, POC-VMS-hint-injection: 测试infinite rank absorption提示能否重定向策略, POC-VMS-knowledge-bottleneck: Eilenberg swindle知识瓶颈检测]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

profile.json已写入 `subagents-dirs/fate_000349/profile.json`，包含所有必填字段。

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

入库成功，验证通过：fate_000349, 7 local pairs, 3 global pairs。

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="396459"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000349"
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
    '_key': '396459',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000349',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000349')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: fate_000349
- solution_method_type: localization_cancellation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3 (1 path_feature + 2 implicit)
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，现有拓扑分类体系足够
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
