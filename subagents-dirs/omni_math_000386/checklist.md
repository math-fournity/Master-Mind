# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_000386
- **文件路径**: subagents-dirs/omni_math_000386/problem.lean
- **来源**: AoPS omni_math (china_team_selection_test)
- **ArangoDB progress记录_key**: 330258（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_000386/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设k为固定偶正整数，N=p_1...p_k为k个不同素数之积，a,b为正整数且a,b≤N。S_1={d|d|N, a≤d≤b, d有偶数个素因子}，S_2={d|d|N, a≤d≤b, d有奇数个素因子}。证明|S_1|-|S_2|≤C(k,k/2)。
- 解答核心思路（1-2句话）：将|S_1|-|S_2|表示为生成多项式P(x)=∏(1-x^{p_i})的连续系数之和，对k归纳，利用P=Q(1-x^{p_k})将和分解为Q的两个连续系数和之差，再用Pascal恒等式2·C(k-1,⌊(k-1)/2⌋)≤C(k,⌊k/2⌋)完成归纳。
- 解答关键步骤列表：
  1. 重构：|S_1|-|S_2| = Σ_{d|N, a≤d≤b} (-1)^{ω(d)} = P(x)=∏(1-x^{p_i})在[a,b]上的连续系数和
  2. 归纳奠基：k=0时P(x)=1，任意连续系数和≤1=C(0,0)
  3. 归纳递推：P=Q(1-x^{p_k})，连续系数和 = (Q的连续系数和) - (Q的平移连续系数和)
  4. 归纳假设：每个Q的连续系数和≤C(k-1,⌊(k-1)/2⌋)
  5. Pascal恒等式：2·C(k-1,⌊(k-1)/2⌋)≤C(k,⌊k/2⌋)，k为偶时取等

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.7 | 描述这道题的结构：N的约数与[1,k]的子集有什么对应关系？|S_1|-|S_2|在代数上是什么？ | N的每个约数d对应子集S⊆[k]，ω(d)=|S|。|S_1|-|S_2|=Σ_{d|N,a≤d≤b}(-1)^{ω(d)}是一个带符号交替的求和，区间[a,b]选取了部分约数。目标是证明这个和≤C(k,k/2)。 |
| 2 | 自由列举 | 0.8 | 列出所有你能想到的逼近这个问题的方法 | 直接计数法、Möbius函数、生成函数/多项式方法、归纳法、Sperner定理、对称链分解、Bonferroni不等式、组合恒等式等 |
| 3 | 小尝试 | 0.5 | 试用直接计数法：按素因子个数j分组，n_j=[a,b]中恰有j个素因子的约数个数，能否得到C(k,k/2)的界？ | 直接计数给出|S_1|-|S_2|≤Σn_j≤2^k，远大于C(k,k/2)≈2^k/√(πk/2)。问题在于没有利用交替符号的抵消结构和区间约束。 |
| 4 | 思维操作引导 | 0.3 | 构造一个生成多项式P(x)，使其系数恰好为(-1)^{ω(d)}。什么样的多项式满足这个性质？ | P(x)=∏_{i=1}^k(1-x^{p_i})。展开后x^d的系数恰为(-1)^{|S|}，其中d=∏_{i∈S}p_i。因此|S_1|-|S_2|=Σ_{n=a}^b [x^n]P(x)，即P(x)在[a,b]上的连续系数和。 |
| 5 | 推进 | 0.4 | 现在你有P(x)=∏(1-x^{p_i})，如何利用其乘积结构对连续系数和进行归纳？ | 设Q(x)=∏_{i<k}(1-x^{p_i})，则P=Q(1-x^{p_k})。[x^n]P=[x^n]Q-[x^{n-p_k}]Q。因此Σ_{n=a}^b[x^n]P = Σ_{n=a}^b[x^n]Q - Σ_{n=a-p_k}^{b-p_k}[x^n]Q，即Q的两个连续系数和之差。 |
| 6 | 思维操作引导 | 0.3 | 对Q应用归纳假设，每个连续系数和≤C(k-1,⌊(k-1)/2⌋)。如何用Pascal恒等式得到C(k,k/2)？ | 差的绝对值≤2·C(k-1,⌊(k-1)/2⌋)。当k为偶时，⌊(k-1)/2⌋=k/2-1，且C(k-1,k/2-1)=C(k-1,k/2)，所以2·C(k-1,k/2-1)=C(k-1,k/2-1)+C(k-1,k/2)=C(k,k/2)（Pascal恒等式）。归纳完成。 |
| 7 | 能量传递引导 | 0.6 | 验证奠基情形(k=0)，检查等号成立的条件，完成证明 | k=0: P(x)=1，连续系数和≤1=C(0,0)✓。k为偶时Pascal恒等式取等，界是紧的。完整证明：重构→归纳→Pascal恒等式，三步完成。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 约数与子集的对应关系；交替符号求和在数值区间上的界；生成多项式的连续系数和
- key_objects: ["N=p_1...p_k（k个不同素数之积）", "约数d↔子集S⊆[k]", "(-1)^{ω(d)}交替符号", "生成多项式P(x)=∏(1-x^{p_i})", "C(k,k/2)中心二项系数"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["generating_function_reformulation", "induction_on_structure", "algebraic_factorization", "pascal_identity_application"]
- primary_pattern: generating_function_reformulation
- knowledge_required: ["约数与子集的对应关系", "生成多项式/形式幂级数", "多项式系数与求和的关系", "数学归纳法", "Pascal恒等式/二项式系数性质"]
- key_insight: 将|S_1|-|S_2|重构为P(x)=∏(1-x^{p_i})的连续系数和，利用P=Q(1-x^{p_k})的因式分解做归纳，Pascal恒等式在k为偶时精确闭合。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接计数法（按素因子个数分组计数约数）
- translation_to: 生成多项式系数分析（多项式连续系数和的归纳界）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_calculation, gap_type: method_translation}
- tell_small_concepts: ["约数-子集对应", "交替符号求和", "生成多项式∏(1-x^p)", "连续系数和", "Pascal恒等式", "归纳因式分解"]
- expected_ai_method: 直接计数法——按素因子个数分组，用n_j≤C(k,j)求和，得到2^k的平凡界，无法利用交替符号的抵消结构
- correct_method: 生成多项式重构+归纳法——将交替和重构为∏(1-x^{p_i})的连续系数和，利用乘积结构做归纳，Pascal恒等式闭合

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=inequality_proof, ai_method_type=direct_calculation, gap_type=method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分——这道题的tell（直接计数→多项式重构）与已有tell可区分
- [ ] 不需要新的拓扑维度

**拓扑进化建议**：无。已有拓扑分类体系完全覆盖本题。

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pair概要**：
| Round | tell | hint | hint_level | situation_type | is_kb | gap_type |
|---|---|---|---|---|---|---|
| 1 | AI看到题目结构但未识别关键重构 | 描述约数-子集对应和交替求和 | 0.7 | 纯元认知观察 | False | method_problem_mismatch |
| 2 | AI列举方法但可能遗漏多项式方法 | 列出所有可能方向 | 0.8 | 自由列举 | False | search_space_estimation |
| 3 | AI尝试直接计数得到2^k的弱界 | 试直接计数法 | 0.5 | 小尝试 | False | method_problem_mismatch |
| 4 | AI需要发现多项式重构（知识瓶颈） | 构造P(x)=∏(1-x^{p_i}) | 0.3 | 思维操作引导 | True | knowledge_gap |
| 5 | AI有多项式但需利用乘积结构做归纳 | 用P=Q(1-x^{p_k})分解 | 0.4 | 推进 | False | structural_transformation |
| 6 | AI需用Pascal恒等式闭合归纳（知识瓶颈） | 应用Pascal恒等式 | 0.3 | 思维操作引导 | True | knowledge_gap |
| 7 | AI有所有部件需验证组装 | 验证奠基和紧性 | 0.6 | 能量传递引导 | False | method_problem_mismatch |

**全局pair概要**：
1. path_feature型：完整证明路径特征（重构→归纳→Pascal闭合），局部步骤中看不到全局路径
2. implicit型（R4）：区间[a,b]约束与连续多项式系数和的隐含对应关系

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: Bare AI会尝试直接计数法，按素因子个数j分组用n_j≤C(k,j)求和，得到2^k的平凡界。无法识别交替符号的抵消结构需要生成多项式重构，也不会想到利用∏(1-x^{p_i})的乘积结构做归纳。关键瓶颈在于从"计数"语言翻译到"多项式系数"语言的方法转换。
- suitable_for_poc: ["tell_extraction_poc", "hint_injection_poc", "method_translation_poc"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入 `profile.json`

**字段清单检查**：
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
- [x] answer（=\\binom{k}{k/2}）
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
- [x] tell_hint_pairs（7个，每个含qa_round/tell/hint/hint_level/situation_type/is_knowledge_bottleneck/tell_topology/tell_small_concepts）
- [x] global_tell_hint_pairs（2个，每个含scope_type/scope/observation_point/tell/hint/hint_level/generalizability/why_not_visible_locally/tell_topology/tell_small_concepts）
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence（含rounds数组和stats子对象）
- [x] analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_000386
- solution_method_type: generating_function_induction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1 path_feature + 1 implicit）
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类体系完全覆盖
- 是否遇到异常: problem.lean中solution被截断（仅到`\bi`），根据数学内容重构完整解答

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
