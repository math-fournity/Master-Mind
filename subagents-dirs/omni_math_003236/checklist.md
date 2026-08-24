# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003236
- **文件路径**: subagents-dirs/omni_math_003236/problem.lean
- **来源**: AoPS omni_math (putnam)
- **ArangoDB progress记录_key**: 333114（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003236/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let n be a positive integer. What is the largest k for which there exist n×n matrices M_1,...,M_k and N_1,...,N_k with real entries such that for all i and j, the matrix product M_i N_j has a zero entry somewhere on its diagonal if and only if i ≠ j?
- 解答核心思路（1-2句话）：构造用标准基向量给出n^n对矩阵；上界通过将矩阵行/列的张量积内积等于对角线元素乘积，转化为n^n维张量空间中的线性无关性论证。
- 解答关键步骤列表：
  1. 构造（下界）：对每个(i_1,...,i_n)∈{1,...,n}^n，令M为行向量为e_{i_1},...,e_{i_n}的矩阵，N=M^T。则M_i N_j的第k个对角元为e_{i_k}·e_{j_k}，为零当且仅当i_k≠j_k，故对角线有零元当且仅当元组不同，得k=n^n。
  2. 上界：令V为R^n的n重张量积空间（维数n^n）。令m_i为M_i各行向量的张量积，n_j为N_j各列向量的张量积。则m_i·n_j等于M_i N_j对角线元素的乘积，故为零当且仅当i≠j。
  3. 若Σc_i m_i=0，对每个j取与n_j的内积得c_j=0，故m_1,...,m_k线性无关，k≤dim(V)=n^n。

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.8 | 描述这个问题的结构。我们在求什么？需要哪两个部分？ | 这是一个关于矩阵族优化的问题。求最大的k使得存在n×n矩阵对(M_i,N_i)满足M_iN_j对角线有零元当且仅当i≠j。需要两部分：构造（下界）证明k可以达到某个值，和上界证明k不能超过某个值。 |
| 2 | 自由列举 | 0.7 | 列出构造这样的矩阵族和证明上界的所有可能方法 | 构造：可用标准基向量、排列矩阵、对角矩阵等。上界：可用计数论证、维数论证、秩界、线性代数技巧如线性无关性等。 |
| 3 | 小尝试 | 0.5 | 尝试用标准基向量构造。能做出多少个不同的矩阵？ | 对每个(i_1,...,i_n)∈{1,...,n}^n，令M的行向量为e_{i_1},...,e_{i_n}，N=M^T。则M_iN_j第k个对角元为e_{i_k}·e_{j_k}，为零当且仅当i_k≠j_k。故对角线有零元当且仅当元组不同，得k=n^n。 |
| 4 | 思维操作引导 | 0.6 | 对上界，思考M_iN_j所有对角线元素的乘积代表什么。能否在某个更大的空间中表达为单个内积？ | 对角线元素乘积∏_l(row_l(M_i)·col_l(N_j))看起来像张量积的内积：若m_i=row_1(M_i)⊗...⊗row_n(M_i)，n_j=col_1(N_j)⊗...⊗col_n(N_j)，则m_i·n_j=∏_l(row_l(M_i)·col_l(N_j))=对角线元素乘积。 |
| 5 | 推进 | 0.5 | 现在用这个张量积结构证明上界。消失条件告诉你什么？ | 条件说m_i·n_j=0当且仅当i≠j，且m_i·n_i≠0。V=R^n的n重张量积空间维数为n^n。若Σc_i m_i=0，对每个j取与n_j的内积得c_j(m_j·n_j)=0，故c_j=0。因此m_1,...,m_k线性无关，k≤dim(V)=n^n。 |
| 6 | 推进 | 0.4 | 验证这个线性无关论证的每一步是否严谨 | 张量积内积公式m_i·n_j=∏(row_l·col_l)是标准性质。消失条件直接来自题目：i≠j时M_iN_j有零对角元故乘积为零，i=j时所有对角元非零故乘积非零。线性无关论证：Σc_i m_i=0→对每个j取内积→只有c_j项非零→c_j=0。严谨。 |
| 7 | 能量传递引导 | 0.3 | 将构造和上界合并，得出最终结论 | 构造给出k≥n^n，上界给出k≤n^n，因此最大的k=n^n。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 5
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R5"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: structural_existence
- structure_features: 求最大k使矩阵族满足对角线零元条件；需要构造（下界）+上界两部分；上界通过张量积提升到高维空间用线性无关性论证
- key_objects: ["n×n实矩阵", "矩阵乘积的对角线", "标准基向量", "张量积空间", "线性无关性"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["explicit_construction", "tensor_product_embedding", "linear_independence_argument", "duality_via_inner_product", "construction_upper_bound_duality"]
- primary_pattern: tensor_product_embedding
- knowledge_required: ["矩阵乘法", "对角线元素", "张量积", "张量积内积公式", "线性无关性", "维数论证", "标准基向量"]
- key_insight: 对角线元素的乘积等于各行向量张量积与各列向量张量积的内积，从而将矩阵对角线条件转化为n^n维张量空间中的线性无关性论证

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 矩阵乘积对角线零元条件（矩阵语言）
- translation_to: 张量积空间中的内积消失条件+线性无关性（张量代数语言）
- translation_type: structural_transformation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: ["tensor product lifting", "diagonal product identity", "linear independence dimension bound", "standard basis construction", "construction-upper bound duality"]
- expected_ai_method: direct_calculation（bare AI预期会尝试直接矩阵分析或计数论证，无法发现张量积提升技巧）
- correct_method: tensor_product_embedding（将矩阵条件提升到张量积空间用线性无关性论证）

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=structural_existence, ai_method_type=direct_calculation, gap_type=structural_transformation均可归入已有拓扑类别
- [x] 粒度一致——标注值与已有值粒度统一
- [x] 三个维度足够区分这道题的tell
- [x] 无需新的拓扑维度

**拓扑进化建议**：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json中tell_hint_pairs字段。
全局pairs详见profile.json中global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会找到用标准基向量的构造（下界k≥n^n），但在上界证明中卡住——会尝试直接矩阵计数或秩论证，无法发现张量积提升技巧将矩阵对角线条件转化为n^n维空间的线性无关性"
- suitable_for_poc: ["tell_extraction", "hint_injection", "knowledge_bottleneck_detection"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_003236/profile.json`。

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

- problem_id: omni_math_003236
- solution_method_type: tensor_product_embedding
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无
- 是否遇到异常: 否（problem.lean中solution被截断，通过web搜索获取完整解答）

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
