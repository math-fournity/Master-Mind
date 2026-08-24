# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2023p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2023P6.lean
- **来源**: IMO 2023 P6
- **ArangoDB progress记录_key**: 329273（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2023P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**注**：Lean文件中proof为`sorry`（未形式化），从T's Lab博客和Lake Forest PDF搜索结果获取实际数学解答。

**产出**（在此填写）：
- 题目原文（数学描述）：Let ABC be an equilateral triangle. Let A₁,B₁,C₁ be interior points of ABC such that BA₁=A₁C, CB₁=B₁A, AC₁=C₁B, and ∠BA₁C + ∠CB₁A + ∠AC₁B = 480°. Let BC₁ and CB₁ meet at A₂, let CA₁ and AC₁ meet at B₂, and let AB₁ and BA₁ meet at C₂. Prove that if triangle A₁B₁C₁ is scalene, then the three circumcircles of triangles AA₁A₂, BB₁B₂ and CC₁C₂ all pass through two common points.
- 解答核心思路（1-2句话）：识别A₁,B₁,C₁分别是△BCA₂,△CAB₂,△ABC₂的外心（由角度条件480°推出），然后用等幂点/共轴圆框架找到两个不同的等幂点T₁,T₂，证明三个外接圆共轴即有两个公共点。
- 解答关键步骤列表：
  1. **外心识别(α)**：设α=∠A₁BC=∠BCA₁（因BA₁=A₁C），由480°条件得α+β+γ=30°。计算∠BA₂C=90°-α=½∠BA₁C，故A₁是△BCA₂的外心。同理B₁是△CAB₂外心，C₁是△ABC₂外心。
  2. **第一个等幂点(β)**：利用等腰三角形性质证明B₁C₁B₂C₂内接（及类似），由等幂心定理得A₁A₂,B₁B₂,C₁C₂共点T₁，T₁对三个外接圆等幂。
  3. **角度等式(γ)**：证明∠BAB₂+∠BB₁B₂=∠CAC₂+∠CC₁C₂，利用辅助点和等边三角形对称性。
  4. **第二个等幂点(ζ)**：定义A₃为外接圆(AA₁A₂)与A₁为心的圆的第二交点，类似B₃,C₃。由(γ)得BCB₃C₃内接（及类似），由等幂心定理得AA₃,BB₃,CC₃共点T₂，T₂对三个外接圆等幂。
  5. **完成**：scalene条件保证T₁≠T₂，两个不同等幂点意味着三个圆共轴，有两个公共点。

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知条件有哪些？要证明什么？"三个圆过两个公共点"在几何上意味着什么？ | ABC是等边三角形，A₁B₁C₁是内部点满足距离条件(BA₁=A₁C等，即在中垂线上)和角度条件(∠BA₁C+∠CB₁A+∠AC₁B=480°)。A₂B₂C₂由线段交点定义。要证三个外接圆(AA₁A₂),(BB₁B₂),(CC₁C₂)过两个公共点，即三个圆共轴。"两个公共点"意味着不是相切(一个公共点)而是真正相交。 |
| 2 | 自由列举 | 0.7 | 列出证明三个圆过两个公共点的所有可能方法。 | (a) 证明三圆共轴(共享等幂轴)——需找两个等幂点；(b) 直接找出两个在三个圆上的点；(c) 证明圆心共线且共享公共弦；(d) 反演变换化简；(e) 坐标/重心坐标计算；(f) 利用Miquel点性质。 |
| 3 | 小尝试 | 0.5 | 试试方法(b)：能否直接识别出两个同时在三个外接圆上的点？ | 很难。三个圆分别过A,A₁,A₂ / B,B₁,B₂ / C,C₁,C₂，涉及不同顶点，没有明显的公共点。坐标方法也困难——480°角度条件非常规，难以在坐标系中处理。此路不通。 |
| 4 | 思维操作引导 | 0.4 | BA₁=A₁C告诉你A₁在BC的什么位置？结合角度条件，计算∠BA₂C与∠BA₁C的关系。A₁相对于△BCA₂是什么？ | BA₁=A₁C意味着A₁在BC中垂线上。设α=∠A₁BC=∠BCA₁，则∠BA₁C=180°-2α。由480°=3×180°-2(α+β+γ)得α+β+γ=30°。而∠BA₂C=180°-(60°-γ)-(60°-β)=60°+β+γ=90°-α=½∠BA₁C。由圆周角定理，A₁是△BCA₂的外心！同理B₁是△CAB₂外心，C₁是△ABC₂外心。 |
| 5 | 思维操作引导 | 0.5 | 既然A₁是△BCA₂的外心（即A₁B=A₁C=A₁A₂），如何利用这个结构找到对三个外接圆等幂的点？ | A₁为外心意味着A₁B=A₁C=A₁A₂。利用等腰三角形性质：△C₁C₂A和△B₁B₂A等腰，可推出∠B₁B₂C₁=∠B₂AC₂=∠B₁C₂C₁，故B₁C₁B₂C₂内接(及类似)。由等幂心定理，A₁A₂,B₁B₂,C₁C₂三线共点T₁，T₁对三个外接圆等幂。 |
| 6 | 思维操作引导 | 0.6 | 你找到了一个等幂点T₁。但我们需要两个公共点，意味着需要第二个等幂点T₂。如何构造第二个等幂点？ | 定义A₃为外接圆(AA₁A₂)与以A₁为心的圆(即△BCA₂外接圆)的第二交点，类似B₃,C₃。需要证AA₃,BB₃,CC₃共点T₂。关键在于证明角度等式∠BAB₂+∠BB₁B₂=∠CAC₂+∠CC₁C₂（利用辅助点和等边三角形对称性），由此得BCB₃C₃内接(及类似)，再由等幂心定理得T₂等幂。 |
| 7 | 能量传递引导 | 0.7 | 你现在有两个等幂点T₁和T₂。scalene条件在这里起什么作用？这如何完成证明？ | scalene条件保证T₁≠T₂——若A₁B₁C₁等腰则两个等幂点重合，只能得到一个公共点或相切。两个不同等幂点意味着三个圆共轴，共享一条等幂轴，因此有两个公共点。证明完成！ |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 3
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 4.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 等边三角形ABC内有点A₁B₁C₁满足中垂线距离条件和480°角度条件；交点A₂B₂C₂由线段交点定义；需证三个外接圆共轴(两个公共点)。核心结构是"隐藏的外心关系"——A₁B₁C₁不是任意点而是特定三角形的外心。
- key_objects: 等边三角形ABC, 内部点A₁/B₁/C₁(在中垂线上), 交点A₂/B₂/C₂, 三个外接圆(AA₁A₂)/(BB₁B₂)/(CC₁C₂), 两个等幂点T₁/T₂, 辅助点A₃/B₃/C₃

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_recognition(识别隐藏的外心结构)", "radical_axis_method(等幂轴/共轴圆框架)", "dual_construction(构造两个等幂点而非一个)", "angle_chasing(角度等式证明共点)", "symmetry_exploitation(等边三角形对称性)"]
- primary_pattern: structural_recognition
- knowledge_required: ["外心性质与圆周角定理", "等幂轴与等幂心定理", "共轴圆", "内接四边形判定", "等边三角形中角度关系", "点到圆的幂"]
- key_insight: A₁B₁C₁不是任意中垂线上的点——由480°角度条件，它们恰好是△BCA₂/△CAB₂/△ABC₂的外心，这解锁了等幂轴框架

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接几何构造(试图直接找到圆上的公共点)或坐标计算
- translation_to: 等幂轴/共轴圆框架(通过等幂点间接证明公共点存在)
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["外心识别", "等幂轴", "共轴圆", "点到圆的幂", "角度和条件480°", "中垂线", "内接四边形", "双重等幂点构造"]
- expected_ai_method: direct_calculation——bare AI会尝试直接计算或坐标方法，被480°角度条件和复杂的交点结构困住
- correct_method: 外心识别+等幂轴框架——先识别隐藏的外心结构，再用等幂心定理构造两个等幂点证明共轴

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——structural_existence/direct_calculation/structural_transformation能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [x] 无需新的拓扑维度

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部(tell,hint)对详情**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到复杂几何题但未识别关键结构关系 | 描述题目结构：已知条件和要证明什么？"两个公共点"几何含义？ | 0.8 | 纯元认知观察 | false | {structural_existence, direct_calculation, structural_transformation} | 等边三角形, 内部点, 角度和条件, 外接圆, 公共点 |
| 2 | AI知道要证圆过公共点但未列举可能方法 | 列出证明三圆过两公共点的所有方法 | 0.7 | 自由列举 | false | {structural_existence, direct_calculation, method_problem_mismatch} | 共轴圆, 等幂轴, 直接交点, 坐标几何, 反演 |
| 3 | AI尝试直接找圆上公共点但卡住——三圆涉及不同顶点 | 试试直接识别两个同时在三圆上的点 | 0.5 | 小尝试 | false | {structural_existence, direct_calculation, method_problem_mismatch} | 直接交点, 外接圆顶点, 坐标方法 |
| 4 | AI未识别BA₁=A₁C+角度条件使A₁成为外心——关键知识缺口 | BA₁=A₁C说明A₁在哪？计算∠BA₂C与∠BA₁C关系。A₁相对于△BCA₂是什么？ | 0.4 | 思维操作引导 | true | {structural_existence, direct_calculation, knowledge_gap} | 中垂线, 外心, 角度条件480°, 圆周角定理, 半角 |
| 5 | AI已识别外心结构但未连接到等幂轴框架 | A₁是外心意味着什么？如何找到对三圆等幂的点？ | 0.5 | 思维操作引导 | false | {structural_existence, logical_deduction, structural_transformation} | 外心, 点到圆的幂, 等幂心, 共点线, 内接四边形 |
| 6 | AI找到一个等幂点但未意识到需要第二个——思维瓶颈 | 需要两个公共点意味着需要第二个等幂点T₂。如何构造？ | 0.6 | 思维操作引导 | false | {structural_existence, logical_deduction, structural_transformation} | 第二等幂点, 辅助构造, 角度等式, 共点线, 共轴圆 |
| 7 | AI有两个等幂点但未验证distinct性且未收尾 | scalene条件起什么作用？两个不同等幂点如何完成证明？ | 0.7 | 能量传递引导 | false | {structural_existence, logical_deduction, structural_transformation} | scalene条件, 不同点, 共轴圆, 两公共点, 完成证明 |

**全局(tell,hint)对详情**：

1. path_feature型：
- scope: 完整解答路径从题目到两公共点证明
- tell: 解答需要识别隐藏的外心结构(A₁为△BCA₂外心)然后用等幂轴框架两次构造两个不同等幂点——双重等幂点构造是路径级特征
- hint: 关键路径特征：外心识别→等幂轴框架→找两个等幂点(非一个)→scalene保证distinct
- hint_level: 0.8
- generalizability: "high——识别隐藏结构后用框架两次获得两个见证的模式可泛化到多种存在性问题"
- why_not_visible_locally: 从任何单步看，解题者只能看到外心识别或一个等幂点构造，无法看到完整路径需要两个等幂点——第二个等幂点的需求只有在第一个找到后才显现，两者之间的联系需要理解完整证明结构

2. implicit型：
- scope: 角度条件480°隐含编码α+β+γ=30°，这是外心识别的关键
- observation_point: R4
- tell: 480°角度条件不只是约束——它隐含决定了A₁B₁C₁是外心，这是整道题的关键
- hint: 将480°改写为α+β+γ=30°，用它证明∠BA₂C=½∠BA₁C，揭示外心结构
- hint_level: 0.5
- generalizability: "medium——将非常规角度和改写以揭示隐藏结构的模式在奥数几何中常见，但480°→外心的具体联系是本题特有的"
- why_not_visible_locally: 在R4步中，解题者看到角度条件作为需满足的约束，而非结构信号。480°=3×180°-2×30°使A₁成为外心这一事实，只有在计算∠BA₂C并与∠BA₁C比较时才可见——这种比较需要同时审视多个几何关系

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试坐标几何或直接构造，被480°角度条件的非常规性困住。即使偶然识别出外心结构，也大概率只找到一个等幂点而不意识到需要构造第二个。双重等幂点构造超出bare AI的典型生成能力。
- suitable_for_poc: ["tell端验证：外心识别作为知识瓶颈(R4)", "hint端验证：等幂轴框架注入的有效性", "path feature验证：双重等幂点构造作为路径级特征"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，已写入 `profile.json`

**字段清单逐项检查**：
- [x] _key（=compfiles_imo2023p6）
- [x] source_id
- [x] source_dataset
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain
- [x] subfield
- [x] answer_type
- [x] answer（proof类型填要证明的结论）
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
- [x] tell_hint_pairs（7个pair，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个pair，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R6"为字符串）
- [x] analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: compfiles_imo2023p6, 7 local pairs, 2 global pairs, knowledge_bottleneck="R4"(str), thinking_bottleneck="R6"(str), answer非None, why_not_visible_locally非None, per-pair tell_topology存在

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo2023p6
- solution_method_type: radical_axis_construction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，已有拓扑分类(structural_existence/direct_calculation/structural_transformation)足够覆盖
- 是否遇到异常: Lean文件proof为sorry(未形式化)，从外部来源(T's Lab博客)获取实际数学解答

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
