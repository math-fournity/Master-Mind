# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000337
- **文件路径**: subagents-dirs/fate_000337/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396447（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000337/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：证明 R = C[x,y,z]/(x²+y³+z⁷) 是UFD。Lean定理名`quotient_not_UFD`有误导性——形式化语句实际断言R是UFD（∃ h : IsDomain R, UniqueFactorizationMonoid R）。Lean证明为sorry（未完成）。
- 解答核心思路（1-2句话）：通过Mumford定理将UFD问题转化为link的同调球判定，再用Brieskorn准则验证(2,3,7)两两互素→link是同调球→局部环是UFD，最后用quasi-homogeneous分次性将局部Cl(R_m)≅Cl(R)推出全局UFD。
- 解答关键步骤列表：
  1. R是2维normal domain，孤立奇点在原点
  2. f=x²+y³+z⁷是quasi-homogeneous（权21,14,6，次数42）
  3. 分次normal domain有Cl(R)≅Cl(R_m)
  4. Mumford定理：Cl(R_m)≅H₁(link,Z)，R_m是UFD ⟺ link是同调3球
  5. Brieskorn准则：x^a+y^b+z^c的link是同调球 ⟺ (a,b,c)两两互素
  6. (2,3,7)两两互素 → link是同调球 → R_m是UFD → Cl(R)=0 → R是UFD

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
| 1 | 纯元认知观察 | 0.8 | 描述R=C[x,y,z]/(x²+y³+z⁷)的环结构和几何对象 | R是超曲面x²+y³+z⁷=0的坐标环，2维C-代数，多项式是quasi-homogeneous |
| 2 | 自由列举 | 0.7 | 列出证明商环是UFD的所有方法（代数+几何+拓扑） | 代数法：直接分解、Nagata准则、类群计算；几何法：奇点理论、link拓扑 |
| 3 | 小尝试 | 0.4 | 尝试用C[x,y,z]是UFD来证明R是UFD | 不行——UFD的商环不一定是UFD，需要利用奇点的具体结构 |
| 4 | 思维操作引导 | 0.5 | 分析R的奇点轨迹，R是否normal？维数？ | 2维，孤立奇点在原点，hypersurface+孤立奇点→normal（Serre准则） |
| 5 | 思维操作引导 | 0.6 | 2维normal local ring的UFD由什么拓扑不变量决定？（Mumford定理） | Cl(R_m)≅H₁(link,Z)，R_m是UFD ⟺ link是同调3球 |
| 6 | 推进 | 0.3 | 用Brieskorn准则验证(2,3,7)：link是同调球⟺两两互素 | gcd(2,3)=gcd(2,7)=gcd(3,7)=1，两两互素→link是同调球→R_m是UFD |
| 7 | 能量传递引导 | 0.4 | 用quasi-homogeneous分次性连接局部和全局，得出结论 | Cl(R)≅Cl(R_m)=0，所以R是UFD |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5
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
- structure_features: 2维normal domain，hypersurface商环，孤立奇点在原点，quasi-homogeneous（权21,14,6），Brieskorn-Pham奇点(2,3,7)，两两互素指数
- key_objects: R=C[x,y,z]/(x²+y³+z⁷)，极大理想m=(x,y,z)，link Σ(2,3,7)，divisor class group Cl(R)

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [structural_translation, criterion_application, local_global_connection, singularity_analysis]
- primary_pattern: structural_translation
- knowledge_required: [UFD和divisor class group理论, normal domain和Serre准则, 超曲面孤立奇点, Mumford定理Cl(R_m)≅H₁(link,Z), Brieskorn准则(两两互素→同调球), quasi-homogeneous分次性和Cl(R)≅Cl(R_m)]
- key_insight: UFD性质等价于H₁(link,Z)=0（Mumford定理），对Brieskorn-Pham奇点x^a+y^b+z^c归结为(a,b,c)两两互素——而(2,3,7)两两互素。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 纯代数（商环的UFD性质）
- translation_to: 代数拓扑（奇点link的同调群）
- translation_type: domain_translation（跨领域翻译：代数→奇点理论→拓扑）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: knowledge_gap}
- tell_small_concepts: [UFD, hypersurface_singularity, link_homology_sphere, Brieskorn_criterion, pairwise_coprime, class_group, Mumford_theorem]
- expected_ai_method: 直接代数操作——尝试逐元素验证唯一分解，或用Nagata准则，或从C[x,y,z]是UFD出发论证
- correct_method: 通过奇点理论的结构翻译——用Mumford定理(Cl(R_m)≅H₁(link,Z))和Brieskorn准则(两两互素→同调球)计算divisor class group，再用quasi-homogeneous分次性连接局部和全局

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。characterization/direct_manipulation/knowledge_gap均可归入已有类别。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是。characterization是抽象级，direct_manipulation是抽象级，knowledge_gap是抽象级。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 够用。这道题的核心特征（跨领域翻译）由gap_type=knowledge_gap和translation_type=domain_translation共同刻画。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无进化建议。现有拓扑分类足够。

**拓扑进化建议**（如有）：无。现有分类体系可覆盖此题。

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
- bare_ai_expected: fail
- bare_ai_error_prediction: Bare AI会尝试直接代数操作——逐元素验证唯一分解、用Nagata准则、或从C[x,y,z]是UFD出发论证——这些方法都无法触及所需的拓扑判据。关键insight需要Mumford定理和Brieskorn准则的奇点理论知识，标准交换代数工具箱中无法获得。
- suitable_for_poc: [tell_extraction, knowledge_bottleneck_detection, cross_domain_translation]
- discriminates_levels: true

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
- [x] answer
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

**将完整JSON写入工作目录的 `profile.json` 文件** → 已写入 subagents-dirs/fate_000337/profile.json

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
2. 更新`problem_extraction_progress`集合中`_key="396447"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000337"
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
    '_key': '396447',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000337',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000337')
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
- problem_id: fate_000337
- solution_method_type: structural_translation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有分类体系(characterization/direct_manipulation/knowledge_gap)可覆盖此题。
- 是否遇到异常: 否。Lean定理名`quotient_not_UFD`有误导性（实际断言R是UFD），已在profile notes中标注。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
