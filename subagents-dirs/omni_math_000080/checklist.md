# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000080
- **文件路径**: subagents-dirs/omni_math_000080/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 329951（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000080/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：给定正整数n和素数p，求最小正整数m，使得对任意多项式f(x)=(x+a₁)(x+a₂)...(x+aₙ)（aᵢ为正整数），及任意非负整数k，存在非负整数k'使得v_p(f(k)) < v_p(f(k')) ≤ v_p(f(k))+m。
- 解答核心思路（1-2句话）：答案为n + v_p(n!)。上界用p-adic平移k'=k+p^s控制赋值增长，下界用f(x)=(x+1)...(x+n)和k=p^s-n构造极值例子证明紧性。
- 解答关键步骤列表：
  1. 分析v_p(f(k)) = Σ v_p(k+aᵢ)的结构
  2. 用p-adic平移k'=k+p^s分析赋值变化：v_p(k+aᵢ)<s时不变，=s时增加，>s时减少
  3. 上界：选择合适的s使得至少一个因子赋值增加，总增长≤n+v_p(n!)
  4. 用Legendre公式v_p(n!)=Σ⌊n/p^j⌋解释结构项
  5. 下界：取f(x)=(x+1)...(x+n)，k=p^s-n，计算v_p(f(k))=s+v_p((n-1)!)
  6. 证明下一个更高赋值的跳跃恰好为n+v_p(n!)

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述题目结构：v_p(f(k))是什么，条件要求什么，量词结构如何？ | v_p(f(k))=Σv_p(k+aᵢ)，要求对所有f和k存在k'使赋值增长但不超过m |
| 2 | 自由列举 | 0.4 | 列出分析v_p乘积的所有可能方法 | 直接计算、p-adic平移、CRT、归纳、极值构造 |
| 3 | 小尝试 | 0.2 | 计算n=2,p=2,a₁=1,a₂=2的小例子 | f(k)=(k+1)(k+2)，观察赋值跳跃模式，答案应为3 |
| 4 | 思维操作引导 | 0.7 | 考虑k'=k+p^s，v_p(k'+aᵢ)与v_p(k+aᵢ)的关系 | v_p<s不变，=s增加，>s减少；选择s使至少一个因子增加 |
| 5 | 推进 | 0.6 | n个整数中p,p²,...的整除计数与v_p(n!)的关系 | Legendre公式v_p(n!)=Σ⌊n/p^j⌋控制结构项 |
| 6 | 思维操作引导 | 0.8 | 下界构造：取f(x)=(x+1)...(x+n)，k=p^s-n | v_p(f(k))=s+v_p((n-1)!)，跳跃恰为n+v_p(n!) |
| 7 | 能量传递引导 | 0.5 | 验证n+v_p(n!)与小例一致，结论 | n=2,p=2→m=3；n=3,p=2→m=4；答案n+v_p(n!) |

**统计**：
- total_rounds: 7
- metacognitive_rounds: 4（R1纯元认知观察+R2自由列举+R5推进+R7能量传递引导）
- knowledge_rounds: 2（R4+R6思维操作引导）
- level_sum: 3.5
- knowledge_bottleneck: R4（p-adic平移技术是纯知识瓶颈）
- thinking_bottleneck: R6（下界极值构造是思维瓶颈）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: constraint_satisfaction（求满足全称约束的最小参数m）
- structure_features: 全称量词覆盖多项式f和整数k；p-adic赋值乘积的极值优化；上界+下界双向证明
- key_objects: p-adic赋值v_p、线性因子乘积f(x)=(x+a₁)...(x+aₙ)、v_p(n!)、p-adic平移k'=k+p^s

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [small_case_exploration, p_adic_shifting, structural_decomposition, extremal_construction]
- primary_pattern: p_adic_shifting
- knowledge_required: [p-adic valuation properties, Legendre's formula for v_p(n!), p-adic behavior of shifted integers, extremal construction technique]
- key_insight: 答案n+v_p(n!)分解为逐因子贡献(n)和结构贡献(v_p(n!))，p-adic平移控制上界，极值构造证明下界紧性

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct computation of small cases（小例直接计算）
- translation_to: p-adic structural analysis with extremal construction（p-adic结构分析+极值构造）
- translation_type: method_translation（从计算方法翻译到结构分析方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: constraint_satisfaction, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [p-adic valuation, product of linear factors, v_p(n!), p-adic shift, extremal construction]
- expected_ai_method: 直接计算小例并猜测模式，缺乏p-adic结构分析
- correct_method: p-adic平移证上界+极值构造证下界，答案分解为逐因子项和结构项

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——constraint_satisfaction/direct_calculation/structural_transformation能归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [ ] 不需要新拓扑维度

**拓扑进化建议**：无。已有拓扑分类体系足够覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对（每轮一个，含per-pair拓扑和小概念）
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

全局pair详情：
1. path_feature型：完整路径特征——n+v_p(n!)的分解（逐因子+结构）需上下界同时建立才可见
2. implicit型：乘积(x+1)...(x+n)与n!的隐含联系——仅在极值构造时浮现

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: Bare AI会计算小例并尝试猜测模式，但会错过与v_p(n!)的联系及p-adic平移技术。无p-adic平移无法推导上界，无极值构造无法建立下界。
- suitable_for_poc: [tell_extraction_poc, hint_injection_poc, knowledge_bottleneck_poc]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，已写入 `subagents-dirs/omni_math_000080/profile.json`

**字段清单逐项检查**：
- [x] _key=omni_math_000080
- [x] source_id, source_dataset, schema_version=3
- [x] problem_text, solution_text, solution_summary
- [x] domain=number_theory, subfield=p_adic_valuation
- [x] answer_type=numerical, answer="n + v_p(n!)"
- [x] problem_type, solution_method_type, structure_features, key_objects
- [x] thinking_patterns, primary_pattern, knowledge_required, key_insight
- [x] translation_from, translation_to, translation_type
- [x] tell_topology（profile级）, tell_small_concepts（profile级）
- [x] expected_ai_method, correct_method
- [x] tell_hint_pairs（7个局部pair，每个含per-pair拓扑和小概念）
- [x] global_tell_hint_pairs（2个全局pair，含why_not_visible_locally）
- [x] bare_ai_expected, bare_ai_error_prediction, suitable_for_poc, discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象，knowledge_bottleneck="R4", thinking_bottleneck="R6"）
- [x] analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功
- 验证结果: [x] 通过（7 local pairs, 2 global pairs, per-pair拓扑存在, why_not_visible_locally存在, answer非None, knowledge_bottleneck="R4", thinking_bottleneck="R6"）

---

## Step 11: 汇报 [x]

- problem_id: omni_math_000080
- solution_method_type: p_adic_structural_analysis
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类体系足够覆盖
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
