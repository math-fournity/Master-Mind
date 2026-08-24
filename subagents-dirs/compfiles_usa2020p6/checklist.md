# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_usa2020p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Usa2020P6.lean
- **来源**: USA 2020 P6
- **ArangoDB progress记录_key**: 329488（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Usa2020P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let n ≥ 2 be an integer. Let x₁ ≥ x₂ ≥ ⋯ ≥ xₙ and y₁ ≥ y₂ ≥ ⋯ ≥ yₙ be 2n real numbers such that 0 = ∑xᵢ = ∑yᵢ and 1 = ∑xᵢ² = ∑yᵢ². Prove that ∑_{i=1}^{n} (xᵢyᵢ − xᵢyₙ₊₁₋ᵢ) ≥ 2/√(n−1).
- 解答核心思路（1-2句话）：引入随机置换σ，定义S(σ)=∑xᵢy_{σ(i)}，计算E[S]=0和E[S²]=1/(n-1)，用方差界(Var≤(M-m)²/4)得max S - min S ≥ 2/√(n-1)，再用排序不等式识别max S=∑xᵢyᵢ和min S=∑xᵢy_{n+1-i}。
- 解答关键步骤列表：
  1. 定义S(σ)=∑xᵢy_{σ(i)}，对均匀随机置换σ
  2. 计算E[S]=0（利用置换纤维均匀性：每个yⱼ被σ(i)取到的次数相等）
  3. 计算E[S²]=1/(n-1)（展开平方，对角项贡献(n-1)!·∑yᵢ²=(n-1)!，非对角项贡献(n-2)!·∑_{a≠b}yₐy_b=-(n-2)!，合计(n-1)!+(n-2)!=n·(n-2)!，除以n!得1/(n-1)）
  4. 应用方差界：Var(S)≤(M-m)²/4，结合E[S]=0得E[S²]=Var(S)≤(M-m)²/4，故M-m≥2√(E[S²])=2/√(n-1)
  5. 排序不等式：对递减序列x,y，∑xᵢyᵢ是所有置换中最大的，∑xᵢy_{n+1-i}是最小的
  6. 因此∑(xᵢyᵢ-xᵢy_{n+1-i})=max S - min S ≥ 2/√(n-1)

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 观察这道题的结构：已知什么条件？目标表达式∑(xᵢyᵢ−xᵢyₙ₊₁₋ᵢ)中，xᵢyᵢ和xᵢyₙ₊₁₋ᵢ分别代表什么配对方式？ | 两个递减序列，零和、单位L2范数。xᵢyᵢ是同序配对（identity pairing），xᵢyₙ₊₁₋ᵢ是反序配对（reversed pairing）。目标是证明同序配对与反序配对之差≥2/√(n−1)。 |
| 2 | 自由列举 | 0.4 | 列出你能想到的所有可能证明方向，包括代数的、组合的、概率的方法。 | 直接展开求和、Cauchy-Schwarz、排序不等式直接用、归纳法、引入随机置换用期望值、凸性论证、Lagrange乘数法…… |
| 3 | 小尝试 | 0.3 | 试着直接展开∑(xᵢyᵢ−xᵢyₙ₊₁₋ᵢ)并用已知条件bound每一项，看看能否得到2/√(n−1)。 | 直接展开后每一项xᵢ(yᵢ−yₙ₊₁₋ᵢ)难以单独bound，因为xᵢ可正可负、yᵢ−yₙ₊₁₋ᵢ的符号也不固定。Cauchy-Schwarz给出∑(xᵢyᵢ−xᵢyₙ₊₁₋ᵢ)≤√(∑xᵢ²)·√(∑(yᵢ−yₙ₊₁₋ᵢ)²)但这是上界不是下界。直接方法无法得到精确常数2/√(n−1)。 |
| 4 | 思维操作引导 | 0.6 | 关键操作：引入一个均匀随机置换σ∈S_n，定义S(σ)=∑ᵢxᵢ·y_{σ(i)}。请计算E[S]。（提示：对固定的i，σ(i)均匀分布在{1,...,n}上） | E[S]=∑ᵢxᵢ·E[y_{σ(i)}]=∑ᵢxᵢ·(1/n)∑ⱼyⱼ=∑ᵢxᵢ·0=0。因为∑yⱼ=0。 |
| 5 | 推进 | 0.5 | 现在计算E[S²]。展开S²=∑ᵢ∑ⱼxᵢxⱼy_{σ(i)}y_{σ(j)}，分i=j和i≠j两种情况，利用置换纤维计数。 | i=j项：∑ᵢxᵢ²·E[y_{σ(i)}²]=(1/n)∑ᵢxᵢ²∑ⱼyⱼ²=1。i≠j项：E[y_{σ(i)}y_{σ(j)}]=(1/(n(n-1)))∑_{a≠b}yₐy_b=(1/(n(n-1)))(−1)=−1/(n(n−1))。故E[S²]=∑ᵢxᵢ²·1+∑_{i≠j}xᵢxⱼ·(−1/(n(n−1)))=1−(1/(n(n−1)))(∑ᵢxᵢ)²+∑xᵢ²...需仔细计算，最终E[S²]=1/(n−1)。 |
| 6 | 思维操作引导 | 0.7 | 现在你有E[S]=0和E[S²]=1/(n−1)。关键操作：回忆方差与值域的关系——任何取值在[m,M]中的随机变量，Var(S)≤(M−m)²/4。请用这个关系推导max S−min S的下界。 | Var(S)=E[S²]−(E[S])²=1/(n−1)−0=1/(n−1)。设M=max S, m=min S，则Var(S)≤(M−m)²/4，即1/(n−1)≤(M−m)²/4，故M−m≥2/√(n−1)。 |
| 7 | 能量传递引导 | 0.4 | 最后一步：用排序不等式识别M和m分别对应哪个置换，然后完成证明。 | 由排序不等式，对递减序列x,y：同序配对∑xᵢyᵢ=max S，反序配对∑xᵢyₙ₊₁₋ᵢ=min S。因此∑(xᵢyᵢ−xᵢyₙ₊₁₋ᵢ)=M−m≥2/√(n−1)。证毕。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.2
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: inequality_proof
- structure_features: 两个递减实数序列，零和、单位L2范数约束；目标是同序配对与反序配对之差的下界，常数2/√(n−1)与n相关
- key_objects: ["sorted_sequences", "permutations", "random_variable_S_sigma", "variance", "rearrangement_inequality"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["probabilistic_translation", "moment_computation", "variance_bound_application", "rearrangement_inequality"]
- primary_pattern: probabilistic_translation
- knowledge_required: ["rearrangement_inequality", "variance_bound_Popoviciu", "permutation_counting", "expected_value_computation"]
- key_insight: 引入随机置换σ定义S(σ)=∑xᵢy_{σ(i)}，目标表达式恰等于max S−min S，而方差界给出max S−min S≥2√(Var(S))=2/√(n−1)

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: deterministic_inequality
- translation_to: probabilistic_variance_argument
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: inequality_proof, ai_method_type: direct_manipulation, gap_type: method_translation}
- tell_small_concepts: ["random_permutation_introduction", "moment_computation", "variance_to_range", "rearrangement_inequality"]
- expected_ai_method: bare AI会尝试直接展开∑(xᵢyᵢ−xᵢyₙ₊₁₋ᵢ)用Cauchy-Schwarz或排序不等式直接bound，但无法得到精确常数2/√(n−1)
- correct_method: 引入随机置换σ定义S(σ)，计算E[S]=0和E[S²]=1/(n−1)，用方差界得max−min≥2/√(n−1)，再用排序不等式识别max和min

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——inequality_proof/direct_manipulation/method_translation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分——problem_type区分问题类型，ai_method_type区分AI走错的方法，gap_type区分差距性质
- [x] 无需新维度

**拓扑进化建议**：无

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

**局部pairs**：R1(纯元认知观察,0.3): tell=看到递减序列零和单位范数+同序反序配对差 / hint=描述结构识别配对含义 / topology={inequality_proof,direct_calculation,method_problem_mismatch} / concepts=[sorted_sequences,zero_sum_unit_norm,identity_vs_reversed_pairing]
R2(自由列举,0.4): tell=列举方向但可能不想到概率方法 / hint=列出所有方向含概率方法 / topology={inequality_proof,enumeration_brute_force,search_space_estimation} / concepts=[cauchy_schwarz,rearrangement_inequality,probabilistic_method,variance_bound]
R3(小尝试,0.3): tell=直接展开无法得到精确常数 / hint=试直接展开bound每项 / topology={inequality_proof,direct_manipulation,method_problem_mismatch} / concepts=[direct_expansion,term_by_term_bound,stuck_on_constant]
R4(思维操作引导,0.6,knowledge_bottleneck): tell=卡在直接方法需新框架 / hint=引入随机置换定义S(σ)计算E[S] / topology={inequality_proof,direct_manipulation,knowledge_gap} / concepts=[random_permutation,expected_value,S_sigma_definition]
R5(推进,0.5): tell=有E[S]=0需计算E[S²] / hint=展开平方分i=j和i≠j用纤维计数 / topology={inequality_proof,direct_calculation,structural_transformation} / concepts=[second_moment,fiber_counting,n_minus_2_factorial,cross_terms]
R6(思维操作引导,0.7,knowledge_bottleneck): tell=有矩需连接到值域 / hint=用方差界Var≤(M−m)²/4 / topology={inequality_proof,logical_deduction,knowledge_gap} / concepts=[popoviciu_bound,variance_range_relation,max_minus_min]
R7(能量传递引导,0.4): tell=有max−min≥2/√(n−1)需识别max和min / hint=排序不等式识别 / topology={inequality_proof,logical_deduction,method_translation} / concepts=[rearrangement_inequality,identity_maximizes,reversal_minimizes]

**全局pairs**：
G1(path_feature,scope=完整路径,obs=null): tell=确定性不等式需翻译为概率论证 / hint=路径：随机置换→矩→方差界→排序不等式 / level=0.7 / generalizability=high / why_not_visible_locally=在任何单步中确定性目标与概率框架的联系不可见，只有看到完整路径才能理解翻译 / topology={inequality_proof,direct_manipulation,method_translation} / concepts=[probabilistic_translation,moment_computation,variance_to_range,rearrangement_identification]
G2(implicit,scope=E[S²]与最终常数连接,obs=R6): tell=二阶矩1/(n−1)通过方差界决定常数2/√(n−1) / hint=E[S²]=Var(S)因E[S]=0，Var≤(M−m)²/4 / level=0.6 / generalizability=medium / why_not_visible_locally=计算E[S²]时与最终常数的联系不可见，阶乘算术掩盖了化简到1/(n−1)的过程，只有结合方差界后2/√(n−1)才浮现 / topology={inequality_proof,direct_calculation,structural_transformation} / concepts=[variance_equals_second_moment,popoviciu_inequality,factorial_simplification,bound_emergence]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试直接展开∑(xᵢyᵢ−xᵢyₙ₊₁₋ᵢ)用Cauchy-Schwarz或排序不等式直接bound，但无法得到精确常数2/√(n−1)。关键缺失是想不到引入随机置换将确定性不等式翻译为概率论证。
- suitable_for_poc: ["tell_extraction_poc", "hint_injection_poc", "method_translation_poc"]
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
2. 更新`problem_extraction_progress`集合中`_key="329488"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_usa2020p6"
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
    '_key': '329488',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_usa2020p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_usa2020p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_usa2020p6
- solution_method_type: probabilistic_method
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，已有拓扑分类(inequality_proof/direct_manipulation/method_translation等)完全够用
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
