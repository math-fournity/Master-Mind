# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1995p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1995P5.lean
- **来源**: USA 1995 P5
- **ArangoDB progress记录_key**: 329380（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1995P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：一个有n个顶点和k条边的图没有三角形。证明存在一个顶点P，使得不与P相邻的顶点之间至多有k(1 - 4k/n²)条边。
- 解答核心思路（1-2句话）：利用三角形-free性质将边分为"近边"（至少一个端点在P的邻居中）和"远边"（无端点在P的邻居中），近边数=∑_{Q∈N(P)} deg(Q)。对所有顶点P求和得∑deg(Q)²，用Cauchy-Schwarz和握手定理得到下界4k²/n，再用平均论证找到某个P使近边数≥4k²/n²，从而远边数≤k(1-4k/n²)。
- 解答关键步骤列表：
  1. 三角形-free性质：P的邻居集中任两个顶点不相邻（否则与P成三角形），故每条边至多有一个端点在N(P)中
  2. 边的划分：远边 + ∑_{Q∈N(P)} deg(Q) = k（近边=邻居度数之和，因为每条近边唯一对应一个邻居端点）
  3. 双重计数：∑_P ∑_{Q∈N(P)} deg(Q) = ∑_Q deg(Q)²（每个Q被计算deg(Q)次，每次贡献deg(Q)）
  4. Cauchy-Schwarz不等式：(∑deg(Q))² ≤ n·∑deg(Q)²
  5. 握手定理：∑deg(Q) = 2k
  6. 结合4和5：∑deg(Q)² ≥ 4k²/n
  7. 平均论证：存在P使∑_{Q∈N(P)} deg(Q) ≥ 4k²/n²
  8. 代数化简：远边 = k - ∑_{Q∈N(P)} deg(Q) ≤ k - 4k²/n² = k(1 - 4k/n²)

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
| 1 | 纯元认知观察 | 0.8 | 这个问题的结构是什么？我们有哪些已知条件，需要证明什么？ | 已知：无三角形的图G，n个顶点，k条边。需要证明：存在顶点P，使得不与P相邻的顶点之间的边数至多为k(1-4k/n²)。这是一个存在性证明，关键在于三角形-free条件如何被利用。 |
| 2 | 自由列举 | 0.7 | 对于这个图论存在性问题，你能想到哪些可能的证明方向？ | 1) 直接对每个顶点计算远边数；2) 归纳法；3) 概率方法（随机选P）；4) 双重计数+平均论证；5) 用Turán型定理的结论；6) 对邻居集的结构分析。 |
| 3 | 小尝试 | 0.5 | 试着直接计算某个顶点P的远边数。三角形-free条件对P的邻居集有什么约束？ | 三角形-free意味着P的邻居N(P)中任两个顶点不相邻（否则与P成三角形）。所以每条边至多有一个端点在N(P)中。远边=没有端点在N(P)中的边，近边=恰有一个端点在N(P)中的边。近边数=∑_{Q∈N(P)} deg(Q)（因为每条近边唯一对应一个邻居端点）。所以远边 = k - ∑_{Q∈N(P)} deg(Q)。 |
| 4 | 思维操作引导 | 0.6 | 现在需要证明存在P使∑_{Q∈N(P)} deg(Q) ≥ 4k²/n²。考虑对所有顶点P求和∑_P ∑_{Q∈N(P)} deg(Q)，这个双重和等于什么？ | 交换求和顺序：∑_P ∑_{Q∈N(P)} deg(Q) = ∑_Q deg(Q)·#{P : Q∈N(P)} = ∑_Q deg(Q)·deg(Q) = ∑_Q deg(Q)²。因为Q的邻居数=deg(Q)，每个邻居P都会把deg(Q)计入一次。 |
| 5 | 推进 | 0.5 | 我们得到了∑_P ∑_{Q∈N(P)} deg(Q) = ∑_Q deg(Q)²。现在需要下界，能用到什么不等式？ | Cauchy-Schwarz不等式：(∑_Q deg(Q))² ≤ n·∑_Q deg(Q)²。由握手定理∑_Q deg(Q) = 2k，所以∑_Q deg(Q)² ≥ (2k)²/n = 4k²/n。 |
| 6 | 思维操作引导 | 0.4 | 我们有∑_P ∑_{Q∈N(P)} deg(Q) ≥ 4k²/n。如何从中得出存在某个P满足我们需要的下界？ | 平均论证：∑_P ∑_{Q∈N(P)} deg(Q) ≥ 4k²/n，共有n个顶点，所以存在P使∑_{Q∈N(P)} deg(Q) ≥ 4k²/(n·n) = 4k²/n²。 |
| 7 | 能量传递引导 | 0.3 | 现在把所有部分组装起来，完成证明。 | 对这个P：远边 = k - ∑_{Q∈N(P)} deg(Q) ≤ k - 4k²/n² = k(1 - 4k/n²)。这正是要证明的结论。□ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4（R1+R2+R5+R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4+R6）
- level_sum: 0.8+0.7+0.5+0.6+0.5+0.4+0.3 = 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R5"（Cauchy-Schwarz不等式的应用是纯知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"（将存在性问题转化为对所有顶点求和的双重计数是核心思维瓶颈）

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
- problem_type: structural_existence（存在性证明：证明存在满足某条件的顶点）
- structure_features: 三角形-free图，需要证明存在顶点P使得"远边"数有上界。核心结构是边的二分划分（近边/远边），以及三角形-free条件保证每条边至多一个端点在邻居集中。
- key_objects: ["triangle-free graph", "neighbor set N(P)", "degree sequence", "far edges (edges not incident to N(P))", "near edges (edges incident to N(P))", "sum of squared degrees"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["double_counting", "averaging_argument", "structural_decomposition", "inequality_application", "sum_manipulation"]
- primary_pattern: double_counting_averaging（双重计数+平均论证是主导思维模式）
- knowledge_required: ["triangle-free graph properties", "double counting technique", "Cauchy-Schwarz inequality", "handshaking lemma", "averaging/pigeonhole principle", "edge partition by neighbor set"]
- key_insight: 将存在性问题转化为对所有顶点求和的双重计数——∑_P ∑_{Q∈N(P)} deg(Q) = ∑_Q deg(Q)²，然后用Cauchy-Schwarz和握手定理由全局下界推出个体存在性

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 存在性证明（寻找单个满足条件的顶点P）
- translation_to: 全局求和+不等式+平均论证（对所有顶点求和，用Cauchy-Schwarz建立下界，再用平均论证回推个体存在性）
- translation_type: existence_to_averaging（从局部存在性翻译到全局平均论证）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["triangle-free", "double counting", "Cauchy-Schwarz", "averaging", "edge partition", "sum of squared degrees", "handshaking lemma"]
- expected_ai_method: bare AI会尝试直接对每个顶点计算远边数，试图找到满足条件的特定顶点，但无法建立全局下界
- correct_method: 双重计数（∑_P ∑_{Q∈N(P)} deg(Q) = ∑deg(Q)²）+ Cauchy-Schwarz不等式 + 握手定理 + 平均论证

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？是。structural_existence、direct_calculation、method_translation均已存在且适用。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？是。三个值的抽象程度与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够。这道题的核心tell是"从存在性到平均论证的翻译"，method_translation准确捕捉了这一点。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全适用。

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

**局部tell_hint_pairs详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到图论存在性问题但未识别三角形-free条件的关键结构性作用 | 描述问题结构：三角形-free图，需要找到顶点P使远边数有上界 | 0.8 | 纯元认知观察 | false | {structural_existence, direct_calculation, method_problem_mismatch} | ["triangle-free", "existence", "edge counting"] |
| 2 | AI列举方向但未看到双重计数+平均论证的组合策略 | 列出所有可能方向，特别关注双重计数和平均论证 | 0.7 | 自由列举 | false | {structural_existence, enumeration_brute_force, search_space_estimation} | ["double counting", "averaging", "extremal graph theory"] |
| 3 | AI尝试直接计算但未利用三角形-free条件对邻居集的约束 | 试直接计算远边数，利用三角形-free条件：每条边至多一个端点在N(P)中 | 0.5 | 小尝试 | false | {structural_existence, direct_calculation, structural_transformation} | ["triangle-free", "neighbor set", "edge partition", "near/far edges"] |
| 4 | AI得到远边=k-∑deg(Q)公式但未想到对所有顶点求和 | 对所有顶点P求和∑_P ∑_{Q∈N(P)} deg(Q)，交换求和顺序 | 0.6 | 思维操作引导 | false | {structural_existence, direct_calculation, method_translation} | ["sum over vertices", "double counting", "sum of squared degrees"] |
| 5 | AI得到∑deg(Q)²但不知道如何建立下界 | 应用Cauchy-Schwarz不等式和握手定理 | 0.5 | 推进 | true | {structural_existence, direct_calculation, knowledge_gap} | ["Cauchy-Schwarz", "handshaking lemma", "sum of squares", "lower bound"] |
| 6 | AI有全局下界4k²/n但未连接到个体存在性 | 用平均论证：n个顶点的和≥4k²/n，故存在P≥4k²/n² | 0.4 | 思维操作引导 | false | {structural_existence, direct_calculation, method_translation} | ["averaging", "pigeonhole", "existence from global bound"] |
| 7 | AI有所有组件但未组装最终不等式 | 组装：远边≤k-4k²/n²=k(1-4k/n²) | 0.3 | 能量传递引导 | false | {structural_existence, direct_calculation, method_translation} | ["algebraic simplification", "final assembly", "target bound"] |

**全局tell_hint_pairs详情**：

1. path_feature型：
- scope_type: path_feature
- scope: 整个证明路径（R1→R7）
- observation_point: null
- tell: 问题是存在性证明（找单个顶点P），但解答路径要求从局部存在性翻译到全局求和+不等式+平均论证，这条完整路径无法从任何单一步骤中看到
- hint: 将存在性问题转化为全局求和，用Cauchy-Schwarz建立下界，再用平均论证回推个体存在性
- hint_level: 0.7
- generalizability: high——"存在性→平均论证"的翻译模式在极值图论中广泛适用（如Turán定理、Ramsey理论的许多存在性证明）
- why_not_visible_locally: 完整路径要求同时看到三个不相关的技术（双重计数、Cauchy-Schwarz、平均论证）的组合，从任何单一步骤看，只能看到局部计算，无法预见全局策略是将存在性翻译为平均论证
- tell_topology: {structural_existence, direct_calculation, method_translation}
- tell_small_concepts: ["existence to averaging", "double counting", "Cauchy-Schwarz", "global to local"]

2. implicit型：
- scope_type: implicit
- scope: 三角形-free条件在整个证明中的隐含作用
- observation_point: R3
- tell: 三角形-free条件不仅用于排除三角形，更关键的是它保证了每条边至多有一个端点在N(P)中，从而使得近边数=∑_{Q∈N(P)} deg(Q)这一精确等式成立，这是整个双重计数的基石
- hint: 三角形-free条件是边划分精确性的保证：它使近边=邻居度数之和成为精确等式而非不等式
- hint_level: 0.6
- generalizability: medium——"图的结构条件保证计数精确性"的模式在图论中常见，但三角形-free→边划分精确性这一具体蕴含需要领域知识
- why_not_visible_locally: 在R3的局部步骤中，三角形-free条件看起来只是排除了三角形，但其作为"每条边至多一个端点在邻居集中"的保证——从而使近边计数精确等于邻居度数之和——这一蕴含在局部步骤中不可见，需要理解整个双重计数论证才能看到
- tell_topology: {structural_existence, direct_calculation, structural_transformation}
- tell_small_concepts: ["triangle-free", "edge partition precision", "unique endpoint property", "double counting foundation"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接对每个顶点计算远边数，试图找到满足条件的特定顶点，但无法建立全局下界。具体错误：1) 不会想到对所有顶点求和的双重计数策略；2) 即使得到∑deg(Q)²也不会想到用Cauchy-Schwarz；3) 不会将存在性问题转化为平均论证。AI可能在局部计算上花费大量时间而无法突破到全局视角。
- suitable_for_poc: ["tell_hint_injection", "path_comparison", "method_translation_poc", "knowledge_bottleneck_detection"]
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
- [x] answer（**⚠️ 必填，不能为None**。proof类型填要证明的结论，如"sum >= ..."；existence_construction类型填构造的存在性结论；numerical类型填数值答案）
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
2. 更新`problem_extraction_progress`集合中`_key="329380"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa1995p5"
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
    '_key': '329380',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa1995p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa1995p5')
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
- problem_id: compfiles_usa1995p5
- solution_method_type: double_counting_averaging
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型，1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否。现有拓扑分类体系（structural_existence / direct_calculation / method_translation等）完全适用，粒度一致。
- 是否遇到异常: 否。入库和验证均一次通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
