# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1991p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1991P5.lean
- **来源**: IMO 1991 P5
- **ArangoDB progress记录_key**: 329136（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1991P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let ABC be a triangle and P be an interior point of ABC. Show that at least one of the angles ∠PAB, ∠PBC, ∠PCA is less than or equal to 30°.
- 解答核心思路（1-2句话）：利用三角形式的Ceva定理得到两组角的正弦积相等，结合六角之和为π，用反证法：假设三个目标角都>30°，则正弦积>(1/2)³；而另一组由AM-GM和sin的凹性得正弦积<(1/2)³，矛盾。
- 解答关键步骤列表：
  1. 三角Ceva定理：sin(∠PAB)·sin(∠PBC)·sin(∠PCA) = sin(∠ABP)·sin(∠BCP)·sin(∠CAP)
  2. P在三角形内部 → 六个角之和 = π
  3. 解析引理（反证法）：若a₁+a₂+a₃+b₁+b₂+b₃=π且sin积相等，则某个aᵢ≤π/6
  4. 反证假设：所有aᵢ>π/6 → sin(aᵢ)>1/2 → 左积>(1/2)³
  5. AM-GM + sin凹性：sin(b₁)sin(b₂)sin(b₃) ≤ (sin((b₁+b₂+b₃)/3))³ < (sin(π/6))³ = (1/2)³
  6. 矛盾：左积>(1/2)³>右积，与Ceva等式矛盾

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
| 1 | 纯元认知观察 | 0.8 | 观察这道题的结构：三角形ABC内有一点P，要证∠PAB、∠PBC、∠PCA中至少一个≤30°。这三个角有什么共同特征？已知条件和目标之间有什么gap？ | 三个角∠PAB、∠PBC、∠PCA是"循环"的——每个角涉及P和两个相邻顶点，形成PAB→PBC→PCA的循环模式。已知条件是P在三角形内部，目标是证明至少一个角有上界30°。gap在于：仅凭"P在内部"这个条件，如何得到具体的角度上界？ |
| 2 | 自由列举 | 0.7 | 列出你能想到的所有可能方法来处理这个"至少一个≤30°"的类型问题。 | 可能方法：①直接角度追踪（六个角之和=π）；②反证法（假设都>30°）；③三角恒等式/Ceva定理；④面积法；⑤坐标几何计算；⑥极值原理；⑦利用正弦定理转化 |
| 3 | 小尝试 | 0.4 | 试试直接角度追踪：P在内部将每个顶角分成两部分，六个角之和是多少？如果三个目标角都>30°能推出什么？ | 六个角之和=π。若∠PAB+∠PBC+∠PCA>90°，则∠ABP+∠BCP+∠CAP<90°。但这本身不产生矛盾——两组角可以分别>90°和<90°，没有额外的等式约束将它们联系起来。角度追踪alone不够。 |
| 4 | 思维操作引导 | 0.5 | 角度追踪只给了和的约束，但缺少将两组角联系起来的等式。思考：P在三角形内部这个条件，除了角度和之外，还给出了什么约束？想想Ceva定理的各种形式。 | P在内部意味着三条线AP、BP、CP共点于P。三角形式Ceva定理给出：sin(∠PAB)·sin(∠PBC)·sin(∠PCA) = sin(∠ABP)·sin(∠BCP)·sin(∠CAP)。这正是将两组角联系起来的等式约束！ |
| 5 | 推进 | 0.3 | 现在有了两个约束：sin积相等 + 六角和=π。设a₁=∠PAB, a₂=∠PBC, a₃=∠PCA, b₁=∠ABP, b₂=∠BCP, b₃=∠CAP。用反证法：假设所有aᵢ>π/6，推导矛盾。先看左边sin(a₁)sin(a₂)sin(a₃)的范围。 | 若所有aᵢ>π/6，则sin(aᵢ)>sin(π/6)=1/2，所以sin(a₁)sin(a₂)sin(a₃)>(1/2)³=1/8。 |
| 6 | 思维操作引导 | 0.4 | 左边>1/8。现在需要证明右边sin(b₁)sin(b₂)sin(b₃)<1/8。想想用什么不等式工具可以估计正弦乘积的上界。提示：AM-GM和sin的凹性。 | 由AM-GM：sin(b₁)sin(b₂)sin(b₃) ≤ ((sin(b₁)+sin(b₂)+sin(b₃))/3)³。由sin在[0,π]上的凹性（Jensen）：(sin(b₁)+sin(b₂)+sin(b₃))/3 ≤ sin((b₁+b₂+b₃)/3)。而b₁+b₂+b₃ = π-(a₁+a₂+a₃) < π-π/2 = π/2，所以(b₁+b₂+b₃)/3 < π/6，sin((b₁+b₂+b₃)/3) < sin(π/6) = 1/2。因此右边<(1/2)³=1/8<左边，与Ceva等式矛盾！ |
| 7 | 能量传递引导 | 0.6 | 矛盾已经完成！回顾整个证明脉络：从几何到三角到分析，三步翻译最终汇聚成一个干净的反证法。请总结关键转折点。 | 关键转折点是识别三角Ceva定理作为几何到分析的桥梁。证明脉络：①几何（P在内部）→②三角（Ceva正弦积等式）→③分析（AM-GM+凹性→不等式矛盾）。30°=π/6的阈值自然来自sin(π/6)=1/2，是AM-GM上界的临界点。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4（需要知道三角形式Ceva定理）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6（需要将AM-GM和sin凹性组合使用）

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
- structure_features: 三角形内点问题，三个循环角的上界证明，需要将几何约束翻译为三角等式再翻译为分析不等式，反证法结构
- key_objects: 三角形ABC、内点P、六个角（∠PAB,∠PBC,∠PCA,∠ABP,∠BCP,∠CAP）、正弦乘积等式、AM-GM不等式、sin凹性

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [proof_by_contradiction, trigonometric_translation, inequality_chaining, angle_sum_constraint, concavity_exploitation]
- primary_pattern: proof_by_contradiction_via_trigonometric_translation
- knowledge_required: [三角形式Ceva定理, AM-GM不等式（三元版本）, sin在[0,π]上的凹性/Jensen不等式, 三角形内点角度分解]
- key_insight: 识别三角Ceva定理作为几何到分析的桥梁——将角度上界问题翻译为正弦乘积不等式，30°=π/6的阈值自然来自sin(π/6)=1/2是AM-GM上界的临界点

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 几何角度约束（三角形内点+角度上界）
- translation_to: 三角乘积等式（Ceva）→ 分析不等式（AM-GM+凹性）→ 反证矛盾
- translation_type: method_translation（三步翻译链：几何→三角→分析）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: [三角Ceva定理, 正弦乘积等式, AM-GM不等式, sin凹性, 角度和约束, 反证法, 30度阈值, sin(π/6)=1/2]
- expected_ai_method: bare AI会尝试直接角度追踪或坐标几何计算，看不到三角Ceva定理这个翻译桥梁，缺少将两组角联系起来的等式约束
- correct_method: 三角Ceva定理将几何翻译为正弦乘积等式，再结合AM-GM和sin凹性用反证法推导矛盾

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？
- [x] 如果发现拓扑分类需要进化，在此写出建议：

**拓扑进化建议**：无需进化。problem_type=inequality_proof、ai_method_type=direct_calculation、gap_type=method_translation均可归入已有拓扑类别，粒度一致。这道题的核心特征（几何→三角→分析的三步翻译链）已被method_translation充分捕获。

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
| 1 | AI看到三角形内点+角度上界问题，但未识别三个角的循环结构 | 观察三个角的循环模式PAB→PBC→PCA，识别已知与目标的gap | 0.8 | 纯元认知观察 | false | {inequality_proof, direct_calculation, method_problem_mismatch} | [triangle, interior_point, angle_bound, cyclic_angles] |
| 2 | AI面对"至少一个≤30°"类型问题，未列举出三角Ceva方向 | 列出所有可能方法包括三角恒等式/Ceva | 0.7 | 自由列举 | false | {inequality_proof, enumeration_brute_force, search_space_estimation} | [angle_chasing, trigonometric_Ceva, area_method, contradiction] |
| 3 | AI尝试直接角度追踪，发现六角和=π但缺少联系两组角的等式 | 角度和约束alone不够，需要额外等式约束 | 0.4 | 小尝试 | false | {inequality_proof, direct_calculation, method_problem_mismatch} | [angle_sum, six_angles, π_total, missing_constraint] |
| 4 | AI不知道三角形式Ceva定理，缺少将两组角联系起来的等式 | P在内部→共点→三角Ceva给出正弦积等式 | 0.5 | 思维操作引导 | true | {inequality_proof, direct_calculation, knowledge_gap} | [trigonometric_Ceva, sine_product_equality, Ceva_theorem] |
| 5 | AI有了Ceva等式+角和=π两个约束，未启动反证法 | 设aᵢ,bᵢ，反证假设所有aᵢ>π/6，推导左边>1/8 | 0.3 | 推进 | false | {inequality_proof, algebraic_identity, method_translation} | [sin_product, contradiction_setup, π/6_threshold, 1/2³] |
| 6 | AI需要估计右边正弦积上界，未想到AM-GM+凹性组合 | AM-GM+sin凹性→右边<(1/2)³<左边，矛盾 | 0.4 | 思维操作引导 | true | {inequality_proof, continuous_analytic, structural_transformation} | [AM-GM, concavity_of_sin, Jensen, (1/2)³, contradiction] |
| 7 | AI完成矛盾推导，未总结翻译链脉络 | 回顾三步翻译：几何→三角→分析，30°阈值来自sin(π/6)=1/2 | 0.6 | 能量传递引导 | false | {inequality_proof, logical_deduction, method_problem_mismatch} | [contradiction_complete, translation_chain, sin(π/6)=1/2] |

**全局tell_hint_pairs详情**：

1. path_feature型：
- scope: 完整证明路径（R1-R7）
- observation_point: null
- tell: 证明需要三步翻译链：几何角度约束→三角正弦积等式(Ceva)→分析不等式(AM-GM+凹性)，反证法作为统一结构
- hint: 将三角Ceva定理作为桥梁，链式应用AM-GM和sin凹性，用反证法收束
- hint_level: 0.7
- generalizability: high——"几何→三角→分析"的翻译链模式可泛化到其他需要将几何约束转化为不等式的问题
- why_not_visible_locally: 在每个单独步骤中（角度和、Ceva、AM-GM），与最终反证矛盾的联系不可见。只有当三个翻译步骤全部链式完成后，矛盾才浮现。局部视角只能看到每一步的技术细节，看不到三步翻译链的整体结构。
- tell_topology: {inequality_proof, direct_calculation, method_translation}
- tell_small_concepts: [trigonometric_Ceva, AM-GM, concavity_of_sin, translation_chain, contradiction]

2. implicit型：
- scope: 30°=π/6阈值的来源
- observation_point: R6
- tell: 30°的阈值不是任意的——它来自sin(π/6)=1/2，是AM-GM上界的临界点。当所有aᵢ>π/6时，左边正弦积>（1/2)³；而右边由AM-GM+凹性被压缩到<(1/2)³，形成矛盾。
- hint: 识别sin(π/6)=1/2作为AM-GM上界的自然临界值，30°不是硬凑的而是从不等式结构中涌现的
- hint_level: 0.5
- generalizability: medium——"阈值从不等式结构中涌现"的模式可泛化到其他AM-GM+凹性问题，但具体的sin(π/6)=1/2联系是本题特有的
- why_not_visible_locally: 在R6的局部步骤中，AI看到的是AM-GM和凹性的机械应用。为什么恰好是π/6这个阈值？这需要同时看到Ceva等式（提供等式约束）、角和=π（提供b的和<π/2）和sin(π/6)=1/2（提供临界值）三个信息的交汇，任何单一步骤都看不到这个交汇点。
- tell_topology: {inequality_proof, continuous_analytic, structural_transformation}
- tell_small_concepts: [sin(π/6)=1/2, threshold_emergence, AM-GM_bound, critical_angle, π/6]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接角度追踪或坐标几何计算，停留在几何层面。关键错误是看不到三角Ceva定理作为翻译桥梁——没有正弦积等式，就无法将"至少一个≤30°"转化为不等式矛盾。AI可能在角度追踪上打转，发现六角和=π但无法进一步推进，因为缺少联系两组角的等式约束。
- suitable_for_poc: ["tell_hint_injection", "method_translation_poc", "knowledge_gap_detection"]
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
2. 更新`problem_extraction_progress`集合中`_key="329136"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1991p5"
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
    '_key': '329136',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1991p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1991p5')
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
- problem_id: compfiles_imo1991p5
- solution_method_type: proof_by_contradiction_via_trigonometric_translation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无需进化。problem_type=inequality_proof、ai_method_type=direct_calculation、gap_type=method_translation均可归入已有拓扑类别，粒度一致。
- 是否遇到异常: 无异常

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
