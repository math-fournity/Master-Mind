# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000344
- **文件路径**: subagents-dirs/fate_000344/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396454（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000344/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 f: C[x,y]→C[x,y], x↦p(x)+ay, y↦x, 其中 a∈C, a≠0, p(x)∈C[x] 次数>1。𝔭⊂C[x,y] 是素理想，height 𝔭=1，则 f(𝔭)≠𝔭。
- 解答核心思路（1-2句话）：C[x,y]是UFD所以height-1素理想=(g)，f是自同构所以f(𝔭)=𝔭推出f(g)=cg。迭代得f^n(g)=c^n·g次数恒定，但deg(f^n(x))=d^n→∞（d=deg p>1），若g含x则次数增长矛盾，若g=g(y)则f(g)=g(x)≠c·g(y)矛盾。
- 解答关键步骤列表：
  1. C[x,y]是UFD → height-1素理想𝔭=(g)，g不可约
  2. f是自同构（a≠0，逆映射x↦y, y↦(x-p(y))/a）→ f(𝔭)=𝔭推出(f(g))=(g) → f(g)=cg, c∈C*
  3. 迭代：f^n(g)=c^n·g，次数恒定；deg(f^n(x))=d^n增长无界
  4. 情形1：g含x → deg(f^n(g))→∞，矛盾
  5. 情形2：g=g(y) → f(g)=g(x)≠c·g(y)，矛盾
  6. Lean证明为sorry（无形式化证明），数学证明已重构

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述题目结构，height-1素理想在C[x,y]中长什么样？ | 识别f是环自同构，height-1素理想有UFD特殊结构 |
| 2 | 自由列举 | 0.7 | 列出所有可能方法证明f(𝔭)≠𝔭 | 直接计算、结构理论、次数论证、迭代动力学、代数几何 |
| 3 | 小尝试 | 0.5 | 试算𝔭=(x-α)时f(𝔭)是否等于𝔭 | f(x-α)=p(x)+ay-α∉(x-α)（需a=0），但不易推广 |
| 4 | 思维操作引导 | 0.6 | C[x,y]是UFD，height-1素理想=主理想(不可约g)，f(𝔭)=𝔭推出什么？ | f(g)=cg，c∈C*（自同构+不可约+同理想→差单位） |
| 5 | 思维操作引导 | 0.5 | 迭代f(g)=cg，f^n(g)是什么？deg(f^n(x))呢？ | f^n(g)=c^n·g次数恒定；deg(f^n(x))=d^n→∞ |
| 6 | 推进 | 0.4 | 比较次数：g含x时deg(f^n(g))如何？g=g(y)时呢？ | g含x→次数增长矛盾；g=g(y)→f(g)=g(x)≠c·g(y)矛盾 |
| 7 | 能量传递引导 | 0.3 | 组装完整证明 | UFD→(g)→f(g)=cg→迭代次数矛盾+case split→QED |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.8
- knowledge_bottleneck: R4（UFD结构知识瓶颈）
- thinking_bottleneck: R6（迭代+次数比较的思维瓶颈）

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization（刻画自同构在素理想上的作用，证明无不动点）
- structure_features: 环自同构作用于素理想；height-1素理想在多项式环中的结构；多项式迭代下的次数增长；反证法+情形分裂
- key_objects: 环自同构f: x↦p(x)+ay, y↦x | height-1素理想𝔭 | 不可约多项式g | 迭代f^n和次数序列deg(f^n(x))=d^n | 标量c满足f(g)=cg

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["structural_classification", "degree_invariant_argument", "proof_by_contradiction", "iteration_dynamics", "case_split_completeness"]
- primary_pattern: degree_invariant_argument（主导思维模式：次数不变量论证）
- knowledge_required: ["C[x,y]是UFD", "UFD中height-1素理想是主理想", "环自同构保持理想格结构", "多项式复合次数增长deg(p∘q)=deg(p)·deg(q)", "a≠0时f是自同构（逆映射x↦y, y↦(x-p(y))/a）"]
- key_insight: 迭代f使deg(f^n(g))按(deg p)^n增长，但f(g)=cg强制f^n(g)=c^n·g次数恒定——矛盾。从理想等式到次数算术的翻译是关键转折。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: ideal_theory（素理想被自同构固定）
- translation_to: degree_arithmetic（多项式迭代下的次数增长）
- translation_type: structural_transformation（从理想论语言翻译到次数算术语言）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: characterization, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: ["height-1 prime", "UFD principal ideal", "ring automorphism", "degree growth", "iteration", "irreducible polynomial", "fixed point", "degree invariant"]
- expected_ai_method: direct_manipulation — bare AI会直接计算f(𝔭)并在理想论层面比较，卡住无法识别UFD结构和次数增长论证
- correct_method: 从理想等式翻译到多项式次数：UFD结构得𝔭=(g)，自同构得f(g)=cg，迭代比较次数得矛盾

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization/direct_manipulation/structural_transformation能归入已有拓扑类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [x] 无需新拓扑维度

**拓扑进化建议**：无。已有拓扑分类体系足够覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pair拓扑分布：
- R1: (characterization, direct_manipulation, structural_transformation)
- R2: (characterization, enumeration_brute_force, method_translation)
- R3: (characterization, direct_calculation, knowledge_gap)
- R4: (characterization, direct_manipulation, knowledge_gap) — 知识瓶颈
- R5: (characterization, logical_deduction, structural_transformation)
- R6: (characterization, direct_calculation, method_translation) — 思维瓶颈
- R7: (characterization, logical_deduction, structural_transformation)

全局pair：
1. path_feature型：理想论→次数算术的完整翻译路径，在局部步骤中不可见
2. implicit型：g=g(y)的边缘情形，在次数论证看似完整时隐含遗漏

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: Bare AI会在理想论层面直接计算f(𝔭)卡住，无法识别三个关键步骤：(1) C[x,y]是UFD所以height-1素理想是主理想，(2) f是自同构所以f(g)=cg，(3) 迭代次数增长提供矛盾。缺少UFD结构知识无法归约到单个生成元，缺少迭代洞察无法找到矛盾，case split（g含x vs g=g(y)）也容易被遗漏。
- suitable_for_poc: ["tell_hint_injection", "topology_matching", "knowledge_bottleneck_detection", "method_translation_detection"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**⚠️ 完整字段清单（逐项检查）**：
- [x] _key（=fate_000344）
- [x] source_id（FATE-X-95）
- [x] source_dataset（FATE-X）
- [x] schema_version（=3）
- [x] problem_text
- [x] solution_text
- [x] solution_summary
- [x] domain（algebra）
- [x] subfield（commutative_algebra）
- [x] answer_type（proof）
- [x] answer（f(𝔭)≠𝔭结论）
- [x] problem_type（characterization）
- [x] solution_method_type（degree_growth_contradiction）
- [x] structure_features
- [x] key_objects
- [x] thinking_patterns
- [x] primary_pattern
- [x] knowledge_required
- [x] key_insight
- [x] translation_from/to/type
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
- [x] qa_sequence（含rounds数组和stats子对象，stats中knowledge_bottleneck="R4", thinking_bottleneck="R6"为字符串类型）
- [x] analysis_metadata

**已写入**：`subagents-dirs/fate_000344/profile.json`

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败
- 验证详情: 7 local pairs, 2 global pairs, knowledge_bottleneck=R4, thinking_bottleneck=R6, all tell_topology/why_not_visible_locally/answer fields present

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: fate_000344
- solution_method_type: degree_growth_contradiction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类体系足够覆盖
- 是否遇到异常: 否，Lean证明为sorry但数学证明已成功重构

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
