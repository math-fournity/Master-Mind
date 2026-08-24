# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: fate_000286
- **文件路径**: subagents-dirs/fate_000286/problem.lean
- **来源**: FATE FATE-X
- **ArangoDB progress记录_key**: 396396（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/fate_000286/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let $R=\mathbb{C}[x_{11},x_{12},\dots,x_{nn}]/(\det(x_{ij})-1)$, show that $R$ is a unique factorization domain.
- 解答核心思路（1-2句话）：Lean文件中 theorem 的证明体是 `sorry`，没有正式解答；数学上可用 Nagata 判别法证明：把坐标环看作 SL_n 的坐标环，先在某个矩阵坐标（如 $x_{nn}$）处局部化，利用 Schur complement/初等行列变换把局部化环化为 $GL_{n-1}$ 的坐标环乘一个多项式环，从而是UFD；再验证该坐标函数给出的余环是整环，降回原环。
- 解答关键步骤列表：1) $n=1$ 时商环同构于 $\mathbb C$；2) 对 $n\ge2$，证明 $A=\mathbb C[x_{ij}]/(\det-1)$ 是Noether整环；3) 证明坐标函数 $x_{nn}$ 在 $A$ 中为素元，即 $A/(x_{nn})$ 是整环；4) 局部化 $A[x_{nn}^{-1}]$，用 Schur complement 得到 $A[x_{nn}^{-1}]\cong \mathbb C[x_{nn}^{\pm1},\text{last row/column variables},Y_{ij}]/(x_{nn}\det Y-1)\cong \mathbb C[Y_{ij},\det(Y)^{-1},\text{free variables}]$；5) 由多项式环局部化保持UFD和归纳/直接事实得局部化是UFD；6) 用 Nagata 引理从 $A[x_{nn}^{-1}]$ 是UFD且 $x_{nn}$ 是素元推出 $A$ 是UFD。

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
| 1 | 纯元认知观察 | 0.85 | 先不要证明，描述这个Lean定理中的环、关系式和目标性质分别是什么。 | 这是矩阵坐标多项式环对单个关系 $\det(X)-1$ 的商环，即 $SL_n$ 的坐标环；目标是给出整环结构并证明它是唯一分解整环。 |
| 2 | 自由列举 | 0.80 | 对这类“多项式环商环是UFD”的命题，列出可能路线，并指出每条路线的风险。 | 可尝试直接用不可约超曲面、代数群坐标环定理、Class group、或Nagata局部化；直接“不可约即UFD”不成立，高阶代数群定理太重，Nagata+局部化最可控。 |
| 3 | 小尝试 | 0.55 | 试一下最直接路线：证明 $\det(X)-1$ 不可约/素，然后看是否足够推出UFD。 | 只能说明商环是整环或超曲面坐标环；UFD不从“UFD模掉一个素元”自动推出，所以这条路会卡在错误推理上。 |
| 4 | 思维操作引导 | 0.35 | 改用UFD下降思路：找一个元素 $s$，使得 $A_s$ 是UFD且 $s$ 在 $A$ 中是素元。你会选哪个元素、用什么定理？ | 选一个矩阵坐标如 $s=x_{nn}$；准备用Nagata引理：Noether整环 $A$ 中若 $s$ 是素元且 $A_s$ 是UFD，则 $A$ 是UFD。 |
| 5 | 思维操作引导 | 0.25 | 在 $x_{nn}$ 可逆的局部环里，把矩阵写成块矩阵并做Schur complement，关系式会变成什么？ | 写 $X=\begin{pmatrix}B&c\\ r& a\end{pmatrix}$，$a=x_{nn}$；令 $Y=B-ca^{-1}r$，则 $\det X=a\det Y$，所以 $A_a\cong \mathbb C[Y_{ij},\det(Y)^{-1},r,c]$，这是 $GL_{n-1}$ 坐标环加自由变量。 |
| 6 | 推进 | 0.45 | 现在补齐Nagata的两个剩余假设：基例、整环性和 $x_{nn}$ 的素性应该怎样验证？ | $n=1$ 时商环是 $\mathbb C$；一般情形可由 $\det-1$ 的素性得整环；$A/(x_{nn})$ 是不可约除子/整环（等价于 $(\det-1,x_{nn})$ 为素理想），所以 $x_{nn}$ 是素元。 |
| 7 | 能量传递引导 | 0.40 | 把这些组件组织成最终证明，不要再展开计算细节，只给出逻辑闭环。 | 基例成立；对 $n\ge2$，$A_{x_{nn}}$ 由Schur complement同构到 $GL_{n-1}$ 坐标环的多项式扩张，是UFD；$x_{nn}$ 为素元；由Nagata引理推出 $A$ 是UFD，同时已知它是整环。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.65
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R5
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R4

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
- problem_type: structural_existence
- structure_features: 目标是给一个由单个行列式方程定义的商环建立整环和UFD结构；表面是“UFD模一个关系”，实质需要把全局商环转到一个可计算的局部开图，再通过素除子和Nagata判别法下降。
- key_objects: [`MvPolynomial ((Fin n) × (Fin n)) ℂ`, generic matrix `X`, determinant polynomial `det(X)`, ideal `(det(X)-1)`, quotient ring `QuotDetSubOne n`, coordinate ring of `SL_n`, coordinate function `x_nn`, localization, Schur complement, coordinate ring of `GL_{n-1}`, prime divisor, Nagata lemma]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [`识别几何对象`, `排除直接商环误推`, `选择可逆坐标开图`, `Schur complement变量替换`, `局部UFD验证`, `Nagata下降`, `基例与素除子补齐`]
- primary_pattern: localization_descent_after_structural_transformation
- knowledge_required: [`多项式环是UFD`, `UFD在多项式扩张和局部化下保持`, `商环为整环与素理想的关系`, `Nagata UFD criterion`, `块矩阵行列式/Schur complement`, `GL_n坐标环是多项式环按det局部化`, `坐标超曲面除子的素性/不可约性`]
- key_insight: 不要试图从“$\det-1$素”直接推出UFD；先把一个矩阵坐标反演，使 $\det=1$ 变成 $GL_{n-1}$ 的局部图，然后用Nagata从这个局部UFD降回全局。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 全局超曲面商环/“UFD对素关系取商”的直接代数语言
- translation_to: 局部化开图 + 块矩阵变量替换 + Nagata UFD下降的交换代数语言
- translation_type: global_quotient_to_localization_descent

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: structural_existence, ai_method_type: direct_manipulation, gap_type: structural_transformation}
- tell_small_concepts: [`SL_n坐标环`, `det-1商环`, `UFD`, `局部化`, `x_nn`, `Schur complement`, `GL_{n-1}`, `Nagata引理`, `素除子`]
- expected_ai_method: bare AI 很可能直接证明 $\det-1$ 不可约/素后误以为商环继承UFD，或直接引用“SL_n坐标环是UFD”的高阶定理但不补形式化可用的局部化下降细节。
- correct_method: 采用Nagata判别法：证明 $x_{nn}$ 是素元，局部化 $A_{x_{nn}}$ 后用Schur complement同构到 $GL_{n-1}$ 坐标环的多项式扩张，从局部UFD下降到全局UFD。

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
- [x] 当前拓扑分类是否够用——够用。问题是结构性质存在/实例证明，AI方法是直接操纵商环，缺口是需要结构变换到局部化图。
- [x] 粒度是否一致——一致。`structural_existence`、`direct_manipulation`、`structural_transformation` 都是抽象到中等粒度，没有引入“SL_n_UFD”这种过细类型。
- [x] 是否需要新的拓扑维度——暂不需要。每轮差异可由小概念词区分，例如Nagata、Schur complement、素除子。
- [x] 如果发现拓扑分类需要进化，在此写出建议：不建议新增硬拓扑；若后续大量交换代数题都出现类似模式，可在小概念或二级标签中记录 `localization_descent`，但不必升级为顶层分类。

**拓扑进化建议**（如有）：无顶层进化建议；保留 `localization_descent` 作为方法小概念即可。

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
- 局部tell_hint_pairs数量: 7 对（R1识别对象；R2路线列举；R3排除“素商即UFD”；R4引入Nagata；R5Schur complement；R6补素性/基例；R7组装结论）
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个
- 约束核查：每个局部和全局pair均在 `profile.json` 中包含 `tell_topology` 与 `tell_small_concepts`；全局pair均填写非空 `why_not_visible_locally`。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI 很可能把“$\det-1$不可约/素”误当成“商环是UFD”的充分条件；或者只引用“$SL_n$坐标环是UFD”的外部定理而没有构造Lean/交换代数可落地的局部化、素除子和Nagata下降链条。
- suitable_for_poc: [`quotient_UFD_false_shortcut_detection`, `localization_descent_hint_injection`, `formal_commutative_algebra_theorem_selection`, `global_path_feature_tell_extraction`]
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

产出文件：`subagents-dirs/fate_000286/profile.json`；已用Python校验JSON可解析、必填字段完整、hint_level为0-1浮点数、situation_type合法、知识瓶颈pair使用knowledge_gap、全局why_not_visible_locally非空、qa_sequence.stats瓶颈字段为字符串。

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
2. 更新`problem_extraction_progress`集合中`_key="396396"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/fate_000286"
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
    '_key': '396396',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/fate_000286',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('fate_000286')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair拓扑存在
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
```

**产出**：
- 入库结果: [x] 成功 / [ ] 失败（已写入 `problem_profiles/fate_000286`，并更新 progress `_key=396396` 为 completed）
- 验证结果: [x] 通过 / [ ] 失败（查询确认profile存在、per-pair拓扑存在、answer非空、global why_not_visible_locally非空、瓶颈字段为字符串；输出 `入库完成并验证通过: fate_000286, 7 local pairs, 3 global pairs`）

---

## Step 11: 汇报 [x]

**操作**：向Master Agent报告

**汇报内容**：
- problem_id: fate_000286
- solution_method_type: localization_descent_nagata
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无顶层进化建议；可把 `localization_descent` 作为方法小概念保留。
- 是否遇到异常: Lean题目中证明体是 `sorry`，因此profile中的solution是重构的标准数学证明；数据库入库成功并验证通过。

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
