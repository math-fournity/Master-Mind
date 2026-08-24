# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa1977p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa1977P5.lean
- **来源**: USA 1977 P5
- **ArangoDB progress记录_key**: 329314（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa1977P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：正实数 v, w, x, y, z 满足 0 < h ≤ v, w, x, y, z ≤ k。证明 (v+w+x+y+z)(1/v+1/w+1/x+1/y+1/z) ≤ 25 + 6(√(h/k) - √(k/h))²。何时取等？
- 解答核心思路（1-2句话）：利用 (r+x)(s+1/x) 作为 x 的函数是凸函数（线性项 sx 加凸项 r/x），最大值在区间端点取到，归纳地将 5 变量的连续优化归约为检查 2^5=32 个"角点"，再由对称性压缩为 6 个不同值，逐一验证不超过 13+6(h/k+k/h) = 25+6(√(h/k)-√(k/h))²。
- 解答关键步骤列表：
  1. 证明引理 le_max_endpoint：对 r≥0, 0<a≤x≤b，(r+x)(s+1/x) ≤ max{(r+a)(s+1/a), (r+b)(s+1/b)}，因为该函数是凸函数，最大值在端点取到。用凸组合 x=λa+μb 和精确恒等式验证。
  2. 定义 cornerMax：递归地计算所有变量取 h 或 k 的 2^n 个角点值的最大值。
  3. 证明 le_cornerMax：对 n 个变量归纳，每次用 le_max_endpoint 将一个变量归约到端点，得到 (r+Σf_i)(s+Σ1/f_i) ≤ cornerMax。
  4. 将 5 变量问题用 le_cornerMax 归约为角点最大值。
  5. 恒等式：(√(h/k)-√(k/h))² = h/k + k/h - 2，故 25+6(√(h/k)-√(k/h))² = 13+6(h/k+k/h)。
  6. 6 个不同角点值（m 个变量取 k）：((5-m)h+mk)((5-m)/h+m/k) = 13+6(h/k+k/h) - (m-2)(m-3)(h-k)²/(hk) ≤ 13+6(h/k+k/h)，因为 (m-2)(m-3)≥0 对 m=0,...,5 成立。
  7. 等号成立条件：所有变量取 h 或 k，且 (m-2)(m-3)(h-k)²=0，即 m=2 或 m=3（或 h=k）。

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构。已知什么？要求什么？这个不等式和标准的不等式有什么不同？ | 已知5个正实数 v,w,x,y,z 都在 [h,k] 内，要证明 (sum)(sum of reciprocals) ≤ 含 h/k 比率的上界。与标准不等式不同之处：通常 Cauchy-Schwarz 给出 (sum)(sum 1/x) ≥ n² 的下界，这里需要上界，且上界依赖变量范围的比率 h/k。 |
| 2 | 自由列举 | 0.7 | 列出所有可能用于证明这个上界不等式的方法，包括利用变量有界性 [h,k] 的方法。 | Cauchy-Schwarz, AM-GM, 拉格朗日乘数法, 凸性分析, 逐变量端点归约, 归纳法, 直接展开, 变量替换 t=x/h 等。 |
| 3 | 小尝试 | 0.4 | 试着用 Cauchy-Schwarz 或 AM-GM 直接处理这个不等式，看看能得到什么。 | Cauchy-Schwarz 给 (sum)(sum 1/x) ≥ 25，是下界不是上界。AM-GM 给 sum ≥ 5h, sum 1/x ≥ 5/k，乘积 ≥ 25h/k 也是下界。标准不等式工具都给出下界方向，无法直接得到上界。这条路走不通。 |
| 4 | 思维操作引导 | 0.5 | 考虑单个变量 x∈[h,k]，函数 f(x)=(r+x)(s+1/x) 是什么类型的函数？它在 [h,k] 上的最大值在哪里取到？ | f(x) = rs + 1 + sx + r/x。sx 是线性函数，r/x 是凸函数（r≥0），所以 f 是凸函数。凸函数在闭区间上的最大值在端点取到，即 max{f(h), f(k)}。 |
| 5 | 推进 | 0.6 | 利用这个单变量凸性结论，如何推广到5个变量的情况？ | 对5个变量逐一应用端点归约：固定其余4个变量，对当前变量用凸性结论，最大值在 h 或 k 取到。归纳地，整体最大值在所有变量都取 h 或 k 的"角点"取到，共 2^5=32 个角点。 |
| 6 | 思维操作引导 | 0.4 | 32个角点太多，但由对称性只有6个不同值（取决于多少个变量取k）。计算这6个值并证明每个 ≤ 13+6(h/k+k/h)。 | 设 m 个变量取 k，角点值为 ((5-m)h+mk)((5-m)/h+m/k) = 13+6(h/k+k/h) - (m-2)(m-3)(h-k)²/(hk)。因为 (m-2)(m-3)≥0 对 m=0,...,5 成立，所以每个角点值 ≤ 13+6(h/k+k/h)。 |
| 7 | 能量传递引导 | 0.5 | 验证恒等式 25+6(√(h/k)-√(k/h))² = 13+6(h/k+k/h)，并确定等号成立条件。 | (√(h/k)-√(k/h))² = h/k+k/h-2，故 25+6(h/k+k/h-2) = 13+6(h/k+k/h)。等号成立当所有变量取 h 或 k，且 (m-2)(m-3)(h-k)²=0，即 m=2 或 m=3（恰2个或3个变量取k），或 h=k（所有变量相等）。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5（R1,R2,R3,R5,R7）
- knowledge_rounds（思维操作引导的轮数）: 2（R4,R6）
- level_sum: 0.8+0.7+0.4+0.5+0.6+0.4+0.5 = 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 5个正实数有界于[h,k]，需证明(sum)(sum of reciprocals)的上界，上界依赖h/k比率，含根号表达式
- key_objects: [正实数 v,w,x,y,z, 界 h,k, 求和, 倒数求和, 凸函数, 角点值, 比率 h/k]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [convexity_maximization, endpoint_reduction, symmetry_compression, algebraic_identity_verification, induction_on_variables]
- primary_pattern: convexity_maximization
- knowledge_required: [凸函数在闭区间端点取最大值, Cauchy-Schwarz不等式, 根号代数恒等式, 归纳法, 对称性压缩]
- key_insight: (r+x)(s+1/x)作为x的函数是凸函数（线性项加凸项r/x），最大值在端点取到，从而将连续优化归约为离散角点检查

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: continuous_optimization（在连续域[h,k]^5上优化乘积）
- translation_to: discrete_case_checking（检查有限个角点值）
- translation_type: structural_transformation（通过凸性将连续优化结构性转化为离散角点检查）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [convexity_at_endpoints, sum_reciprocal_product, corner_reduction, popcount_symmetry, sqrt_ratio_identity]
- expected_ai_method: direct_calculation（bare AI会用Cauchy-Schwarz/AM-GM直接计算，得到下界而非上界）
- correct_method: convexity_endpoint_reduction（用凸性将连续优化归约到角点，再检查有限个情况）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=inequality_proof, ai_method_type=direct_calculation, gap_type=structural_transformation 均可归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类足够覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs详见profile.json中的tell_hint_pairs字段**

**全局pairs详见profile.json中的global_tell_hint_pairs字段**

全局pair 1 (path_feature):
- scope_type: path_feature
- scope: 从连续优化到离散角点检查的完整路径
- tell: 整个解题路径需要识别凸性将连续优化转化为离散角点检查——这是一个从任何单步都看不到的结构性转化
- hint: 用凸性将连续域上的乘积优化归约到检查有限个角点配置
- hint_level: 0.7
- generalizability: high — 凸性端点归约模式适用于任何有界变量乘积优化
- why_not_visible_locally: 从任何单步看，凸性观察、归纳推广、对称性压缩都是独立的技术。只有完整路径才揭示凸性是使所有后续步骤成为可能的结构性转化。
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [convexity_endpoint_reduction, continuous_to_discrete, corner_optimization]

全局pair 2 (implicit):
- scope_type: implicit
- scope: 题目中的根号形式上界与证明所需的有理形式之间的隐藏恒等式
- observation_point: Q7
- tell: 题目上界写作 √(h/k)-√(k/h) 的平方形式，但证明自然需要 13+6(h/k+k/h) 的有理形式。这个恒等式隐含在题目表述中。
- hint: 展开 (√(h/k)-√(k/h))² 揭示 h/k+k/h-2，连接题目上界与证明所需的代数形式
- hint_level: 0.6
- generalizability: medium — 将根号形式重写为有理形式的技巧适用于类似的比率依赖不等式
- why_not_visible_locally: 根号形式与有理形式之间的联系在凸性论证的任何中间步骤中都不可见。只有在比较最终角点上界表达式与题目表述形式时才显现。
- tell_topology: {problem_type: inequality_proof, ai_method_type: algebraic_identity, gap_type: method_translation}
- tell_small_concepts: [sqrt_expansion, rational_form_conversion, hidden_identity]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会用Cauchy-Schwarz或AM-GM直接处理，但这些工具给出的是下界（(sum)(sum 1/x) ≥ 25），而非所需的上界。AI不会识别(r+x)(s+1/x)的凸性结构，因此无法找到将连续优化归约到角点检查的方法路径。
- suitable_for_poc: ["tell_hint_injection", "convexity_recognition", "structural_transformation_detection"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入 `profile.json`

**已完成**：profile.json 已写入 `subagents-dirs/compfiles_usa1977p5/profile.json`

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证输出: compfiles_usa1977p5, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa1977p5
- solution_method_type: convexity_endpoint_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有拓扑分类（inequality_proof / direct_calculation / structural_transformation等）足够覆盖此题
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
