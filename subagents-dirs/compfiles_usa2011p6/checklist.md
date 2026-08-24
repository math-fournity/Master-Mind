# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2011p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2011P6.lean
- **来源**: USA 2011 P6
- **ArangoDB progress记录_key**: 329445（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2011P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let A be a set with |A| = 225. Suppose there are eleven subsets A₁, A₂, ..., A₁₁ of A such that |Aᵢ| = 45 for 1 ≤ i ≤ 11 and |Aᵢ ∩ Aⱼ| = 9 for 1 ≤ i < j ≤ 11. Prove that |A₁ ∪ A₂ ∪ ··· ∪ A₁₁| ≥ 165, and give an example for which equality holds.
- 解答核心思路（1-2句话）：对并集中每个元素定义重数（出现在多少个Aᵢ中），用双重计数算出重数之和=495、重数平方和=1485，再用Cauchy-Schwarz得|并集|≥495²/1485=165。等号例子：用Fin 11的所有3元子集（C(11,3)=165个）作为并集元素，Aᵢ=含i的3元子集，加60个哑元素使|A|=225。
- 解答关键步骤列表：
  1. 定义元素重数 m(a) = |{i : a ∈ Aᵢ}|
  2. 双重计数：Σ m(a) = Σ|Aᵢ| = 11×45 = 495
  3. 双重计数：Σ m(a)² = Σ_{i,j} |Aᵢ∩Aⱼ| = 11×45 + 11×10×9 = 1485
  4. Cauchy-Schwarz: (Σ m(a))² ≤ |U| × Σ m(a)²，即 495² ≤ |U| × 1485
  5. 得 |U| ≥ 495²/1485 = 165
  6. 构造等号例子：U₀ = Fin 11的所有3元子集（165个），A = U₀ ∪ {60个哑元素}，Aᵢ = {T ∈ U₀ : i ∈ T}
  7. 验证：|Aᵢ| = C(10,2) = 45，|Aᵢ∩Aⱼ| = C(9,1) = 9，|∪Aᵢ| = C(11,3) = 165

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知条件是什么？要证明什么？关键数字之间有什么关系？ | 已知：225元集合A，11个子集每个45元，两两交集9元。要证：并集≥165且给出等号例子。关键数字：11×45=495，C(11,2)×9=495，两个数恰好相等。 |
| 2 | 自由列举 | 0.7 | 列出所有你能想到的估计集合并集大小的方法。 | 容斥原理、双重计数、Cauchy-Schwarz不等式、线性代数方法、概率方法、构造反例验证极值…… |
| 3 | 小尝试 | 0.3 | 试用容斥原理计算并集大小，看看能走多远。 | 容斥：|∪Aᵢ| = Σ|Aᵢ| - Σ|Aᵢ∩Aⱼ| + Σ|Aᵢ∩Aⱼ∩Aₖ| - ... = 495 - 495 + (三项交未知) - ...。前两项抵消（495-495=0），三项交集没有给出数据，容斥原理走不通。 |
| 4 | 思维操作引导 | 0.2 | 换一个视角：不要从集合层面想，从元素层面想。对并集中每个元素a，定义重数m(a)=包含a的Aᵢ个数。用双重计数算出Σm(a)和Σm(a)²。 | Σm(a) = Σ|Aᵢ| = 11×45 = 495。Σm(a)² = Σ_{i,j}|Aᵢ∩Aⱼ| = 11×45 + 11×10×9 = 495+990 = 1485。（对角线贡献11×45，非对角线贡献11×10×9） |
| 5 | 推进 | 0.3 | 你现在有Σm(a)=495和Σm(a)²=1485。如何把它们和并集大小|U|联系起来？ | 由Cauchy-Schwarz不等式：(Σm(a))² ≤ |U| × Σm(a)²，即495² ≤ |U| × 1485，所以|U| ≥ 495²/1485 = 245025/1485 = 165。 |
| 6 | 思维操作引导 | 0.2 | 现在构造等号成立的例子。Cauchy-Schwarz等号条件是什么？什么样的结构能满足？ | 等号条件：所有m(a)相等，m(a)=495/165=3。考虑Fin 11的所有3元子集（C(11,3)=165个）作为并集元素，Aᵢ={含i的3元子集}。则|Aᵢ|=C(10,2)=45，|Aᵢ∩Aⱼ|=C(9,1)=9，每个元素恰好在3个Aᵢ中。加60个哑元素使|A|=225。 |
| 7 | 能量传递引导 | 0.4 | 验证你的构造满足所有条件，完成证明。 | 验证：|A|=165+60=225 ✓，|Aᵢ|=C(10,2)=45 ✓，|Aᵢ∩Aⱼ|=C(9,1)=9 ✓，|∪Aᵢ|=C(11,3)=165 ✓。所有条件满足，等号成立。证明完成。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.8+0.7+0.3+0.2+0.3+0.2+0.4 = 2.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

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
- problem_type: inequality_proof
- structure_features: 11个子集Aᵢ⊆A（|A|=225），每个|Aᵢ|=45，两两|Aᵢ∩Aⱼ|=9，证明|∪Aᵢ|≥165并给出等号构造。关键数字关系：11×45=495=C(11,2)×9，容斥前两项恰好抵消。
- key_objects: ["有限集合A（|A|=225）", "11个子集Aᵢ（每个|Aᵢ|=45）", "两两交集Aᵢ∩Aⱼ（|Aᵢ∩Aⱼ|=9）", "并集∪Aᵢ", "元素重数m(a)=|{i:a∈Aᵢ}|"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["double_counting", "cauchy_schwarz_inequality", "multiplicity_analysis", "extremal_construction", "perspective_switch"]
- primary_pattern: double_counting
- knowledge_required: ["Cauchy-Schwarz不等式", "双重计数（combinatorial double counting）", "组合恒等式与二项系数", "容斥原理（识别其局限性）"]
- key_insight: 从集合层面切换到元素层面——定义每个元素的重数，用双重计数算出重数之和与平方和，再用Cauchy-Schwarz一步得到并集下界。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 集合层面容斥原理（set-level inclusion-exclusion）
- translation_to: 元素层面重数双重计数 + Cauchy-Schwarz不等式（element-level multiplicity double counting + Cauchy-Schwarz）
- translation_type: method_translation（从一种计数框架翻译到另一种）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["multiplicity", "double_counting", "cauchy_schwarz", "sum_of_squares", "element_level", "inclusion_exclusion_failure"]
- expected_ai_method: bare AI预期会用容斥原理直接计算并集大小，但前两项抵消（495-495=0）且三项交集未知，走不通后可能放弃或尝试错误方向。
- correct_method: 元素重数双重计数 + Cauchy-Schwarz不等式：定义m(a)，算Σm(a)=495和Σm(a)²=1485，用Cauchy-Schwarz得|U|≥165。

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type=inequality_proof、ai_method_type=direct_manipulation、gap_type=method_translation都能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——标注的值和已有值的粒度统一，没有过细或过粗。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。已有拓扑分类完全覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详情**：

| qa_round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到并集下界问题，有交集数据但不知道从何入手 | 描述题目结构：已知条件、目标、关键数字关系 | 0.8 | 纯元认知观察 | false | {inequality_proof, direct_manipulation, method_problem_mismatch} | ["union_bound", "intersection_data", "set_size_constraints"] |
| 2 | AI列出方法但未识别关键的元素层面切换 | 列出所有估计并集大小的方法 | 0.7 | 自由列举 | false | {inequality_proof, enumeration_brute_force, search_space_estimation} | ["inclusion_exclusion", "double_counting", "cauchy_schwarz", "linear_algebra_method"] |
| 3 | AI试容斥原理，前两项抵消（495-495=0），三项交集未知，走不通 | 试容斥原理，看能走多远 | 0.3 | 小尝试 | false | {inequality_proof, direct_manipulation, method_problem_mismatch} | ["inclusion_exclusion", "triple_intersection_unknown", "term_cancellation"] |
| 4 | AI卡在集合层面，需要切换到元素层面重数思维 | 换视角：定义元素重数m(a)，用双重计数算Σm(a)和Σm(a)² | 0.2 | 思维操作引导 | true | {inequality_proof, direct_manipulation, knowledge_gap} | ["multiplicity", "double_counting", "element_level", "sum_of_squares"] |
| 5 | AI算出Σm=495和Σm²=1485但未看到与|U|的联系 | 用Cauchy-Schwarz联系重数和与并集大小 | 0.3 | 推进 | false | {inequality_proof, direct_calculation, method_translation} | ["cauchy_schwarz", "power_mean", "sum_squared_bound"] |
| 6 | AI有下界但需构造等号例子，需识别均匀重数结构 | Cauchy-Schwarz等号条件=均匀重数=3，用3元子集构造 | 0.2 | 思维操作引导 | true | {structural_existence, case_by_case, knowledge_gap} | ["cauchy_schwarz_equality", "uniform_multiplicity", "three_element_subsets", "binomial_coefficient"] |
| 7 | AI有构造，需验证所有条件并收尾 | 验证构造满足所有条件，完成证明 | 0.4 | 能量传递引导 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["verification", "binomial_coefficient", "construction_check"] |

**全局tell_hint_pairs详情**：

1. path_feature型：
- scope_type: "path_feature"
- scope: "完整解题路径：从容斥失败到重数双重计数+Cauchy-Schwarz"
- observation_point: null
- tell: "解题需要从容斥原理的集合层面切换到元素层面重数计数。关键路径特征：容斥前两项抵消（495-495=0）是切换视角的信号，而非死路。"
- hint: "当容斥原理因项抵消或高阶交集未知而走不通时，切换到元素重数双重计数，再用Cauchy-Schwarz联系重数和与并集大小。"
- hint_level: 0.5
- generalizability: "high — 从集合层面到元素层面的视角切换适用于许多有交集数据的组合不等式问题"
- why_not_visible_locally: "在每个单独步骤中（试容斥、算重数），'容斥失败→元素层面→Cauchy-Schwarz'的整体路径不可见。容斥的失败在局部看起来是死路，而非切换视角的信号。重数和与Cauchy-Schwarz之间的联系需要同时看到两个计算才能发现。"
- tell_topology: {inequality_proof, direct_manipulation, method_translation}
- tell_small_concepts: ["perspective_switch", "inclusion_exclusion_failure", "multiplicity_counting", "cauchy_schwarz_connection"]

2. implicit型：
- scope_type: "implicit"
- scope: "等号构造"
- observation_point: "Q6"
- tell: "等号要求所有重数均匀（=3），对应高度对称的组合设计（11元集合的3元子集）。45=C(10,2)、9=C(9,1)、165=C(11,3)这三个数隐含指向同一组合结构。"
- hint: "当等号条件要求均匀重数时，寻找对称组合设计。45=C(10,2)、9=C(9,1)、165=C(11,3)都指向11元集合的3元子集结构。"
- hint_level: 0.4
- generalizability: "medium — 均匀重数与组合设计的联系可泛化，但具体的3元子集构造是本题特有的"
- why_not_visible_locally: "在Cauchy-Schwarz步骤中，等号条件（均匀重数）是数学细节而非构造提示。45=C(10,2)、9=C(9,1)、165=C(11,3)来自同一组合结构这一事实，在单独计算这些数时不可见——需要同时识别三个数的模式才能发现。"
- tell_topology: {structural_existence, case_by_case, structural_transformation}
- tell_small_concepts: ["uniform_multiplicity", "combinatorial_design", "binomial_coefficient_pattern", "three_element_subsets"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试容斥原理，发现前两项抵消（495-495=0）后陷入困境——三项交集未知，无法继续。之后可能放弃或尝试错误方向（如假设三项交集为0等），不会想到切换到元素层面重数计数。即使想到双重计数，也可能不知道用Cauchy-Schwarz联系重数和与并集大小。
- suitable_for_poc: ["POC-VMS-hint-injection（验证hint端：注入重数+Cauchy-Schwarz方向后AI能否完成）", "POC-VMS-tell-detection（验证tell端：从AI thinking中检测容斥失败的分叉信号）"]
- discriminates_levels: true（本题区分度高：bare AI大概率fail，有hint的AI应该能pass，适合验证hint注入效果）

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
- [x] answer（proof类型，填要证明的结论+等号构造）
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
- [x] tell_hint_pairs（7个局部pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个全局pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R5"为字符串类型）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

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
2. 更新`problem_extraction_progress`集合中`_key="329445"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2011p6"
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
    '_key': '329445',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2011p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2011p6')
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
- problem_id: compfiles_usa2011p6
- solution_method_type: double_counting
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类完全覆盖本题（inequality_proof / direct_manipulation / method_translation等已有值均适用）
- 是否遇到异常: 否，入库和验证均一次通过

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
