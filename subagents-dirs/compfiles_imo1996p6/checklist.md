# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1996p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1996P6.lean
- **来源**: IMO 1996 P6
- **ArangoDB progress记录_key**: 329158（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1996P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：设 p, q, n 为正整数且 p + q < n。设 (x₀, x₁, ..., xₙ) 为满足以下条件的 (n+1) 元整数组：(a) x₀ = xₙ = 0；(b) 对每个 1 ≤ i ≤ n，要么 xᵢ - xᵢ₋₁ = p，要么 xᵢ - xᵢ₋₁ = -q。证明存在索引 i < j 且 (i,j) ≠ (0,n)，使得 xᵢ = xⱼ。
- 解答核心思路（1-2句话）：先归约到 gcd(p,q)=1 的情形，再通过计数得到 n = k(p+q)（k>1），定义辅助函数 d(i) = x(i+h) - x(i)（h=p+q），证明所有 d(i) 是 h 的倍数且相邻差 ∈ {0,±h}，若无 d(i)=0 则所有 d(i) 同号，但望远镜求和为 0，矛盾。
- 解答关键步骤列表：
  1. 归约：若 gcd(p,q) = d > 1，将 p, q, xᵢ 都除以 d，递归到更小问题
  2. 计数：设 r 个 +p 步、s 个 -q 步，则 r·p = s·q 且 r+s = n
  3. 互素推导：gcd(p,q)=1 时 p|s, q|r，故 s=kp, r=kq, n=k(p+q)，k>1（因 p+q<n）
  4. 定义辅助函数：h = p+q, d(i) = x(i+h) - x(i)，证明 h | d(i)
  5. 相邻差性质：d(i+1) - d(i) ∈ {0, h, -h}
  6. 若某 d(i) = 0，则 x(i) = x(i+h)，直接完成
  7. 若所有 d(i) ≠ 0，则所有 d(i) 同号（变号需 |d(i+1)-d(i)| ≥ 2h，矛盾）
  8. 望远镜求和 ∑d(i·h) = x(n) - x(0) = 0，但同号非零项之和不可能为 0，矛盾

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
| 1 | 纯元认知观察 | 0.8 | 描述这个问题的结构：已知条件是什么？需要证明什么？这是一个什么类型的数学对象？ | 我们有一个整数序列 x₀,...,xₙ，从0出发回到0，每步要么+ p要么-q。需要证明某个中间值重复出现（xᵢ=xⱼ，(i,j)≠(0,n)）。这是一个离散整数值上的随机游走型问题，本质是鸽巢原理的变体——但要找到正确的"盒子"。 |
| 2 | 自由列举 | 0.7 | 列出所有可能的方法来证明某个 xᵢ = xⱼ（(i,j)≠(0,n)）。 | 1. 直接鸽巢原理：值域有限则必有重复。2. 模运算：看 xᵢ mod m。3. 分析步态模式。4. 利用总步和为0的约束。5. 寻找周期结构。6. 对n归纳。7. 图论解释（路径必自交）。8. 连续化/解析方法。 |
| 3 | 小尝试 | 0.3 | 试直接用鸽巢原理：xᵢ 的值域有多大？索引有多少个？鸽巢能用吗？ | xᵢ 的值域在最坏情况下可达 O(n·max(p,q))，即 O(n²) 量级，而索引只有 n+1 个。鸽巢原理不能直接使用，因为值域远大于索引数。需要更精细的结构分析。 |
| 4 | 思维操作引导 | 0.3 | 设 r 为 +p 步数、s 为 -q 步数。利用 x₀=xₙ=0 推导 r,s,p,q 之间的关系。 | 因 xₙ-x₀=0，总步和为0：r·p - s·q = 0，即 r·p = s·q。又 r+s = n。这是连接步数与 p,q 的关键约束。 |
| 5 | 思维操作引导 | 0.4 | 先归约到 gcd(p,q)=1 的情形（除以 gcd 即可递归）。然后在互素条件下，从 r·p=s·q 推导 n 的结构。 | 若 gcd(p,q)=d>1，将 p,q,xᵢ 都除以 d 归约。当 gcd(p,q)=1 时，p|s 且 q|r，故 s=kp, r=kq, n=k(p+q)。因 p+q<n 故 k>1。令 h=p+q，则 n=kh。 |
| 6 | 思维操作引导 | 0.2 | 定义 d(i)=x(i+h)-x(i)（h=p+q）。证明：(1) h|d(i)；(2) d(i+1)-d(i) ∈ {0,h,-h}。 | (1) d(i) 是 h 个连续步之和，设 t 个为+p、h-t 个为-q，则 d(i)=t·p-(h-t)·q=(t-q)·h，故 h|d(i)。(2) d(i+1)-d(i)=g(i+h)-g(i)，其中 g(j)∈{p,-q}，四种组合给出 0, p+q=h, -(p+q)=-h, 0。 |
| 7 | 推进 | 0.4 | 若所有 d(i)≠0，证明所有 d(i) 同号（提示：变号会怎样？）。然后看望远镜求和 ∑d(i·h)。 | 若 d(i),d(i+1) 异号，两者都是 h 的非零倍数，故 |d(i)|≥h, |d(i+1)|≥h 且异号，|d(i+1)-d(i)|≥2h。但 d(i+1)-d(i)∈{0,±h}，矛盾。故所有 d(i) 同号。而 ∑d(i·h)=x(n)-x(0)=0，同号非零项之和不可能为0，矛盾！ |
| 8 | 能量传递引导 | 0.5 | 你已经到达矛盾了！把完整证明结构总结一下。 | 1. 归约到互素情形。2. 计数得 n=k(p+q), k>1。3. 定义 d(i)=x(i+h)-x(i)，证 h|d(i) 且相邻差∈{0,±h}。4. 若某 d(i)=0 则 x(i)=x(i+h) 完成。5. 否则所有 d(i) 同号。6. 望远镜求和=0 但同号非零矛盾。QED。 |

**统计**：
- total_rounds: 8
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 3
- level_sum: 0.8+0.7+0.3+0.3+0.4+0.2+0.4+0.5 = 3.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R6（构造辅助函数 d(i) 并证明其性质是核心知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R7（将同号性连接到望远镜求和矛盾是核心思维瓶颈）

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
- problem_type: discrete_combinatorial
- structure_features: 离散整数序列上的两步游走（+p或-q），起点终点同为0，需证明中间值重复出现。核心结构是步态约束+回归约束的组合。
- key_objects: ["整数序列 x₀,...,xₙ", "步长 p, q", "步数 r, s", "辅助函数 d(i)=x(i+h)-x(i)", "周期 h=p+q", "互素归约 gcd(p,q)"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["结构归约（除以gcd递归到互素情形）", "计数约束分析（r·p=s·q推导n的结构）", "辅助函数构造（定义d(i)=x(i+h)-x(i)）", "符号一致性论证（同号性+相邻差约束）", "望远镜求和矛盾（同号非零项之和≠0）"]
- primary_pattern: 辅助函数构造（定义d(i)并利用其性质导出矛盾是整个证明的核心转折）
- knowledge_required: ["鸽巢原理", "Bézout定理/互素性质", "整除性", "望远镜求和", "符号分析"]
- key_insight: 定义 d(i)=x(i+h)-x(i)（h=p+q），证明 d(i) 是 h 的倍数且相邻差 ∈ {0,±h}，从而所有非零 d(i) 同号，但望远镜求和为 0 导致矛盾

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接搜索重复值（在原始序列 x₀,...,xₙ 中寻找 xᵢ=xⱼ）
- translation_to: 辅助函数+符号矛盾（定义 d(i)=x(i+h)-x(i)，通过整除性、相邻差约束和符号一致性导出矛盾）
- translation_type: structural_transformation（从直接存在性搜索翻译为间接矛盾论证，需要构造全新的辅助函数视角）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "structural_transformation"}
- tell_small_concepts: ["两步游走", "回归约束", "互素归约", "计数方程rp=sq", "周期h=p+q", "辅助函数d(i)", "整除性", "相邻差约束", "符号一致性", "望远镜求和矛盾"]
- expected_ai_method: 直接鸽巢原理在xᵢ值上搜索重复值，或对步态模式做案例分析，不构造辅助函数
- correct_method: 归约到互素情形→计数得n=k(p+q)→构造辅助函数d(i)=x(i+h)-x(i)→利用整除性和相邻差约束证明符号一致性→望远镜求和矛盾

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type(discrete_combinatorial)/ai_method_type(enumeration_brute_force)/gap_type(structural_transformation)都能归入已有的拓扑类别，够用。
- [x] 粒度是否一致——标注的值和已有值的粒度统一，都是抽象级别的大概念。
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell。gap_type=structural_transformation准确描述了"从直接搜索到辅助函数+矛盾论证"的转换。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有分类体系适用。

**拓扑进化建议**（如有）：无。现有拓扑分类体系完全适用。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 8 对
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

**局部tell_hint_pairs摘要**：
- R1: tell="AI看到两步游走+回归约束但不知道如何利用", hint="描述问题结构", level=0.8, topology=(discrete_combinatorial, direct_calculation, method_problem_mismatch)
- R2: tell="AI列举了多种方法但无法判断哪个有效", hint="列出所有可能方向", level=0.7, topology=(discrete_combinatorial, enumeration_brute_force, search_space_estimation)
- R3: tell="AI尝试鸽巢但值域太大", hint="试鸽巢原理", level=0.3, topology=(discrete_combinatorial, enumeration_brute_force, search_space_estimation)
- R4: tell="AI未注意到步数约束可推导关键方程", hint="计数步数推导r·p=s·q", level=0.3, topology=(discrete_combinatorial, direct_calculation, knowledge_gap)
- R5: tell="AI未利用互素性推导n的结构", hint="归约到互素+推导n=k(p+q)", level=0.4, topology=(discrete_combinatorial, logical_deduction, structural_transformation)
- R6: tell="AI未想到构造辅助函数d(i)", hint="定义d(i)并证明性质", level=0.2, topology=(discrete_combinatorial, direct_manipulation, structural_transformation)
- R7: tell="AI未连接符号一致性到矛盾", hint="证明同号+望远镜求和", level=0.4, topology=(discrete_combinatorial, logical_deduction, method_translation)
- R8: tell="AI需要综合所有步骤", hint="总结完整证明", level=0.5, topology=(discrete_combinatorial, logical_deduction, method_translation)

**全局tell_hint_pairs摘要**：
- GP1 (path_feature): 完整证明路径"归约→计数→辅助函数→符号矛盾"的结构特征
- GP2 (implicit, R5): 计数方程r·p=s·q隐含n=k(p+q)的周期结构
- GP3 (implicit, R7): 相邻差约束{0,±h}+整除性隐含符号一致性→矛盾

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: 裸AI会尝试直接鸽巢原理在xᵢ值上找重复，但值域太大无法直接应用；或者尝试对步态模式做案例分析，但无法发现构造辅助函数d(i)和利用符号一致性导出矛盾的关键步骤。最可能卡在"如何利用p+q<n这个条件"上——不知道它意味着n=k(p+q)且k>1，从而h=p+q是自然周期。
- suitable_for_poc: ["tell_extraction", "hint_injection", "topology_classification", "difficulty_benchmark"]
- discriminates_levels: true（这是IMO 1996 P6，公认史上最难的IMO题之一，能有效区分强方法和弱方法）

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

**产出**：profile.json已写入，包含34个字段，8个局部tell_hint_pairs，3个全局tell_hint_pairs。所有pair含tell_topology和tell_small_concepts，所有global pair含why_not_visible_locally（非None），answer字段已填写。

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
2. 更新`problem_extraction_progress`集合中`_key="329158"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1996p6"
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
    '_key': '329158',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1996p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1996p6')
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
- problem_id: compfiles_imo1996p6
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 8
- 全局(tell,hint)对数量: 3（1个path_feature型，2个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有分类体系完全适用
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
