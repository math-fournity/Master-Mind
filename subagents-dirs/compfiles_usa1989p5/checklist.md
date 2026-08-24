# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1989p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1989P5.lean
- **来源**: USA 1989 P5
- **ArangoDB progress记录_key**: 329357（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1989P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let u and v be real numbers such that (u + u² + u³ + ⋯ + u⁸) + 10u⁹ = (v + v² + v³ + ⋯ + v¹⁰) + 10v¹¹ = 8. Determine, with proof, which of the two numbers, u or v, is larger.
- 解答核心思路（1-2句话）：定义 U(x)=x+x²+...+x⁸+10x⁹ 和 V(x)=x+x²+...+x¹⁰+10x¹¹。通过证明 u,v>0、u<9/10、V(u)-U(u)=u⁹(10u-9)(u+1)<0 得到 V(u)<U(u)=8=V(v)，再由 V 在正实数上单调递增推出 u<v。
- 解答关键步骤列表：
  1. 定义 U(x) 和 V(x)，将条件重写为 U(u)=8, V(v)=8
  2. 证明 x≤0 时 U(x)≤0 且 V(x)≤0，从而 u>0, v>0
  3. 计算 U(9/10)=9>8，由 U 在正实数上递增得 u<9/10
  4. 计算 V(u)-U(u) = 10u¹¹+u¹⁰-9u⁹ = u⁹(10u-9)(u+1)
  5. 由 0<u<9/10 得 u⁹>0, 10u-9<0, u+1>0，故 V(u)-U(u)<0，即 V(u)<U(u)=8
  6. V(u)<8=V(v)，且 V 在正实数上递增，故 u<v
  7. 结论：v 更大（u<v）

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.2 | 描述这道题的结构：已知条件是什么？要求什么？定义 U(x)=x+x²+...+x⁸+10x⁹, V(x)=x+x²+...+x¹⁰+10x¹¹ 后条件是什么？ | 已知 U(u)=8, V(v)=8，要求比较 u 和 v 的大小。U 是9次多项式，V 是11次多项式，两者结构相似但次数不同，最高次项系数都是10。 |
| 2 | 自由列举 | 0.3 | 列出所有可能的比较 u 和 v 大小的方法方向 | ①直接解方程 U(u)=8, V(v)=8 求 u,v（但次数太高）；②研究 U,V 的单调性；③在特定点评估 U 和 V；④比较 U 和 V 在同一点的值；⑤利用 U,V 的结构差异。 |
| 3 | 小尝试 | 0.4 | 试试计算 U(9/10) 的值——系数10和9次方暗示 9/10 可能是特殊点 | U(9/10) = 9(1-(9/10)⁸) + 10(9/10)⁹ = 9 - 9(9/10)⁸ + 9(9/10)⁸ = 9 > 8。因为 U 在正实数上递增，所以 u < 9/10。这给出了 u 的上界！ |
| 4 | 思维操作引导 | 0.5 | 既然 0 < u < 9/10，现在计算 V(u) - U(u) 并因式分解 | V(u)-U(u) = (u⁹+u¹⁰+10u¹¹) - (9u⁹) = 10u¹¹+u¹⁰-9u⁹ = u⁹(10u²+u-9) = u⁹(10u-9)(u+1)。因式 10u-9 与上界 u<9/10 直接相关！ |
| 5 | 推进 | 0.6 | 利用 0 < u < 9/10 判断 V(u)-U(u) = u⁹(10u-9)(u+1) 的符号 | u⁹ > 0（因 u>0），10u-9 < 0（因 u<9/10），u+1 > 0（因 u>0）。所以 V(u)-U(u) < 0，即 V(u) < U(u) = 8。 |
| 6 | 推进 | 0.7 | 现在 V(u) < 8 = V(v)，如何从 V 的性质推出 u 和 v 的关系？ | V(x) = x+x²+...+x¹⁰+10x¹¹ 在 x>0 时每一项都递增，所以 V 在正实数上严格递增。V(u) < V(v) 且 u,v > 0，故 u < v。 |
| 7 | 能量传递引导 | 0.8 | 将所有步骤组装成完整证明 | 证明链：①u,v>0（因 x≤0 时 U,V≤0）；②u<9/10（因 U(9/10)=9>8 且 U 递增）；③V(u)-U(u)=u⁹(10u-9)(u+1)<0（符号分析）；④V(u)<8=V(v)；⑤V 递增 ⟹ u<v。结论：v 更大。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5（R1+R2+R5+R6+R7）
- knowledge_rounds（思维操作引导的轮数）: 1（R4）
- level_sum: 0.2+0.3+0.4+0.5+0.6+0.7+0.8 = 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 两个结构相似但次数不同的多项式方程共享同一函数值8；最高次项系数为10；需要比较两个方程的根的大小而非求解
- key_objects: ["U(x) = x + x² + ... + x⁸ + 10x⁹", "V(x) = x + x² + ... + x¹⁰ + 10x¹¹", "实数 u, v 满足 U(u) = V(v) = 8"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["bounding（通过特定点评估建立上界）", "function_difference（计算同一点处两个函数的差）", "sign_analysis（因式分解后逐因子判断符号）", "monotonicity_transfer（利用单调性将函数值不等式 transferred 到自变量不等式）"]
- primary_pattern: indirect_comparison_via_function_difference
- knowledge_required: ["多项式在正实数上的单调性", "几何级数求和公式", "代数因式分解", "符号分析", "特定点评估技巧"]
- key_insight: 计算 V(u)-U(u) = u⁹(10u-9)(u+1)，其中因子 10u-9 与上界 u<9/10 直接关联，从而 V(u)<U(u)=8=V(v)，再由 V 递增推出 u<v

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接方程求解（试图解 U(u)=8 和 V(v)=8 这两个高次多项式方程）
- translation_to: 间接比较（通过函数差 V(u)-U(u) 的因式分解和符号分析，结合单调性传递比较 u 和 v）
- translation_type: method_translation（从"分别求解再比较"翻译为"在同一点比较函数差再利用单调性传递"）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "inequality_proof", ai_method_type: "equation_solving", gap_type: "method_translation"}
- tell_small_concepts: ["polynomial_root_comparison", "function_difference", "specific_point_evaluation", "factor_sign_analysis", "monotonicity_transfer", "bound_factor_link"]
- expected_ai_method: bare AI 会尝试直接解 U(u)=8 和 V(v)=8 这两个高次多项式方程，或尝试数值方法，无法找到闭式解
- correct_method: 通过特定点评估建立 u 的上界，计算 V(u)-U(u) 并因式分解，利用符号分析和单调性间接比较

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的 problem_type=inequality_proof, ai_method_type=equation_solving, gap_type=method_translation 均可归入已有拓扑类别
- [x] 粒度是否一致——标注值与已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的 tell 和已有 tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化

**拓扑进化建议**（如有）：无，现有拓扑分类足够

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI看到两个多项式方程但不知道如何比较u和v | 描述题目结构：定义U和V后条件是什么，要求什么 | 0.2 | 纯元认知观察 | false | {inequality_proof, direct_calculation, method_problem_mismatch} | ["polynomial_equation", "comparison", "real_numbers"] |
| 2 | AI列出方向但不会想到比较V(u)与U(u) | 列出所有方向包括特定点评估和同一点函数比较 | 0.3 | 自由列举 | false | {inequality_proof, enumeration_brute_force, method_problem_mismatch} | ["approach_enumeration", "function_comparison", "specific_point_evaluation"] |
| 3 | AI不知道9/10是特殊点 | 试试计算U(9/10)——系数10和9次方暗示9/10 | 0.4 | 小尝试 | false | {inequality_proof, direct_calculation, knowledge_gap} | ["specific_evaluation", "upper_bound", "telescoping_cancellation"] |
| 4 | AI有u的上界但不知道如何连接U和V | 计算V(u)-U(u)并因式分解 | 0.5 | 思维操作引导 | true | {inequality_proof, algebraic_identity, structural_transformation} | ["difference_factoring", "polynomial_identity", "u9_factor"] |
| 5 | AI有因式分解结果但需要判断符号 | 利用0<u<9/10判断每个因子的符号 | 0.6 | 推进 | false | {inequality_proof, logical_deduction, method_translation} | ["sign_analysis", "factor_sign", "inequality_chain"] |
| 6 | AI知道V(u)<8=V(v)但没联系到u vs v | V在正实数上递增，V(u)<V(v)推出u<v | 0.7 | 推进 | false | {inequality_proof, logical_deduction, method_translation} | ["monotonicity", "function_increasing", "comparison_transfer"] |
| 7 | AI有所有片段但需要组装完整证明 | 组装：u,v>0 → u<9/10 → V(u)<8=V(v) → V递增 ⟹ u<v | 0.8 | 能量传递引导 | false | {inequality_proof, logical_deduction, method_translation} | ["proof_synthesis", "inequality_chain", "conclusion"] |

**全局tell_hint_pairs**：

1. path_feature型：
- scope: "完整推理链：从界定u到比较V(u)与V(v)再到结论u<v"
- observation_point: null
- tell: "证明需要多步链式推理：界定u → 计算V(u)-U(u) → 符号分析 → 单调性传递。没有任何单一步骤能揭示完整策略。"
- hint: "策略是：(1)证明u,v>0，(2)通过U(9/10)=9界定u<9/10，(3)计算V(u)-U(u)并证明为负，(4)用V单调性推出u<v"
- hint_level: 0.7
- generalizability: "high — '先界定再比较函数差再利用单调性传递'的策略可泛化到许多比较问题"
- why_not_visible_locally: "完整策略——界定u、再用界定结果因式分解V(u)-U(u)并符号分析、再通过单调性传递——是路径级特征。在任何单一步骤中，该步骤的动机只有从下游步骤才能看清。例如，界定u<9/10在不知道10u-9是V(u)-U(u)的因子时看起来毫无动机。"
- tell_topology: {inequality_proof, logical_deduction, method_translation}
- tell_small_concepts: ["multi_step_strategy", "bound_then_compare", "monotonicity_transfer"]

2. implicit型：
- scope: "V(u)-U(u)的代数结构"
- observation_point: "R4"
- tell: "V(u)-U(u) = 10u¹¹+u¹⁰-9u⁹ 因式分解为 u⁹(10u-9)(u+1)，其中因子10u-9与上界u<9/10直接关联。这种因式分解和关联从U和V的单独定义中不可见。"
- hint: "当有两个函数在同一点求值时，计算它们的差并因式分解——因式分解往往揭示与已知上界的隐藏联系"
- hint_level: 0.6
- generalizability: "high — 计算函数差并因式分解以揭示与已知界联系的技巧广泛适用"
- why_not_visible_locally: "因式分解V(u)-U(u)=u⁹(10u-9)(u+1)及其与上界u<9/10的联系，在分别观察U和V时不可见。只有当计算差并因式分解后才浮现，这是一种跨步骤综合，在任何单一步骤中都不明显。"
- tell_topology: {inequality_proof, algebraic_identity, structural_transformation}
- tell_small_concepts: ["difference_factoring", "hidden_connection", "bound_factor_link"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI 会尝试直接解 U(u)=8（9次方程）和 V(v)=8（11次方程），这两个高次多项式方程没有闭式解。AI 可能尝试数值方法但不一定能可靠地比较精度。AI 不会想到计算 V(u)-U(u) 并因式分解，也不会想到评估 U(9/10) 来建立上界。关键的非显然步骤——在同一点比较两个不同函数的值差——是 bare AI 最可能遗漏的。"
- suitable_for_poc: ["tell_hint_injection", "path_feature_retrieval", "method_translation_poc"]
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
- [x] answer（"u < v (v is larger)"）
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
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R3"为字符串类型）
- [x] analysis_metadata（analyzed_by/analyzed_at/analysis_duration/notes）

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa1989p5
- solution_method_type: indirect_comparison_via_function_difference
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类（inequality_proof / equation_solving / method_translation等）足够覆盖
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
