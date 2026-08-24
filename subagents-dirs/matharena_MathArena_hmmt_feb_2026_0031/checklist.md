# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: matharena_MathArena_hmmt_feb_2026_0031
- **文件路径**: subagents-dirs/matharena_MathArena_hmmt_feb_2026_0031/problem.lean
- **来源**: MathArena MathArena_hmmt_feb_2026
- **ArangoDB progress记录_key**: 329733（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/matharena_MathArena_hmmt_feb_2026_0031/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let α and β be complex numbers such that αβ + α + β + 100 = 0. Suppose that |α| = |β| = M for some nonnegative real number M. Determine, with proof, all possible values of M.
- 解答核心思路（1-2句话）：将方程因式分解为 (α+1)(β+1) = -99，令 u=α+1, v=β+1，利用 uv 为负实数推出辐角互补，再从两个模方程消元得到 M² = |uv| + 1 = 100。
- 解答关键步骤列表：
  1. 因式分解：αβ + α + β + 100 = (α+1)(β+1) + 99 = 0 → (α+1)(β+1) = -99
  2. 代换：令 u = α+1, v = β+1，则 uv = -99，|u-1| = |v-1| = M
  3. 极坐标：u = re^{iθ}, v = se^{iφ}，rs = 99，θ+φ = π（因 uv 为负实数）
  4. 辐角互补：cos φ = -cos θ
  5. 模方程展开：r² - 2r cos θ + 1 = M²，s² + 2s cos θ + 1 = M²
  6. 消元：两式相减得 (r-s)(r+s) = 2(r+s)cos θ → r - s = 2cos θ
  7. 回代：M² = r² - r(r-s) + 1 = rs + 1 = 99 + 1 = 100
  8. 结论：M = 10（M ≥ 0 唯一解）

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
| 1 | 纯元认知观察 | 0.85 | 观察方程 αβ + α + β + 100 = 0 和条件 |α| = |β| = M 的结构。已知什么？未知什么？方程有什么可利用的代数结构？ | 已知：α,β 是复数，满足 αβ+α+β+100=0 且 |α|=|β|=M。未知：M 的所有可能值。方程含 αβ, α, β 的交叉项，形似可因式分解的结构 (α+1)(β+1)。 |
| 2 | 自由列举 | 0.75 | 列出你能想到的所有处理这个方程的方向，包括可能走错的方向。 | ①直接解 α=-(β+100)/(β+1) 再代入模条件；②因式分解 (α+1)(β+1)=-99 后换元；③用三角不等式 |αβ|≤|α||β| 估计；④设极坐标 α=Me^{iθ}, β=Me^{iφ} 直接展开；⑤利用共轭复数性质。 |
| 3 | 小尝试 | 0.40 | 尝试方向①：从方程解出 α 用 β 表示，然后代入 |α|=|β|=M，看看能得到什么。 | α=-(β+100)/(β+1)，则 |α|=|β+100|/|β+1|=M=|β|，所以 |β+100|=|β|·|β+1|。展开得 |β|²+200Re(β)+10000 = |β|²(|β|²+2Re(β)+1)，式子很复杂，难以直接推出 M。这条路陷入代数泥潭。 |
| 4 | 思维操作引导 | 0.30 | 注意 αβ+α+β = (α+1)(β+1)-1。做因式分解的代换：令 u=α+1, v=β+1，重新表述条件和约束。 | (α+1)(β+1) = -99，即 uv = -99。约束变为 |u-1|=|v-1|=M。uv 是负实数，所以 |uv|=99 且 arg(u)+arg(v)=π。 |
| 5 | 推进 | 0.50 | 用极坐标表示 u=re^{iθ}, v=se^{iφ}，利用 uv 为负实数推出辐角关系，然后展开两个模方程。 | rs=99, θ+φ=π 所以 cos φ=-cos θ。|u-1|²=r²-2r cos θ+1=M²，|v-1|²=s²+2s cos θ+1=M²。 |
| 6 | 思维操作引导 | 0.25 | 两个模方程都等于 M²，相减消去 M²，提取公因式 (r+s)，然后用结果回代求 M²。 | 相减：(r²-s²)-2(r+s)cos θ=0 → (r-s)(r+s)=2(r+s)cos θ → r-s=2cos θ。回代：M²=r²-2r cos θ+1=r²-r(r-s)+1=rs+1=99+1=100。所以 M=10。 |
| 7 | 能量传递引导 | 0.70 | 验证 M=10 确实可取到（构造具体例子），并确认这是唯一解。你已经走到终点了。 | M²=100 且 M≥0 所以 M=10 唯一。可取到：取 r=s=√99, cos θ=0（即 θ=π/2），则 u=√99·i, v=-√99·i, α=√99·i-1, β=-√99·i-1，验证 |α|=|β|=√(99+1)=10，且 (α+1)(β+1)=(√99i)(-√99i)=99... 需调整符号使 uv=-99。取 u=√99i, v=√99i 则 uv=-99, α=√99i-1, β=√99i-1, |α|=|β|=10。验证完成。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.85+0.75+0.40+0.30+0.50+0.25+0.70 = 3.75
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R6"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: constraint_satisfaction
- structure_features: 复数方程约束 + 等模条件，需确定参数的所有可能值。方程 αβ+α+β+100=0 具有可因式分解的代数结构 (α+1)(β+1)=-99，等模条件 |α|=|β|=M 通过极坐标和辐角互补转化为可消元的模方程组。
- key_objects: [复数 α, β, 模 M, 因式分解后的 u=α+1 和 v=β+1, 极坐标参数 r,s,θ,φ]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: [代数因式分解识别, 变量代换简化约束, 极坐标参数化, 辐角关系利用, 对称消元, 回代求值]
- primary_pattern: 代数因式分解识别（将原始方程重构为乘积形式是解题的转折点）
- knowledge_required: [复数极坐标表示, 复数模的展开 |z-a|²=|z|²-2Re(z·ā)+|a|², 辐角加法与实数条件, 因式分解技巧]
- key_insight: 将 αβ+α+β+100=0 因式分解为 (α+1)(β+1)=-99 后换元，利用 uv 为负实数推出辐角互补，两个模方程消元后 M² 恰好等于 |uv|+1=100。

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: 直接代数运算（从原始方程解出一个变量代入模条件）
- translation_to: 结构化因式分解+极坐标消元（换元后利用辐角互补对称消元）
- translation_type: structural_transformation（通过因式分解和换元改变问题的表示结构，使隐藏的对称性显现）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: constraint_satisfaction, ai_method_type: direct_calculation, gap_type: structural_transformation}
- tell_small_concepts: [因式分解, 换元代换, 辐角互补, 模方程消元, 对称性利用]
- expected_ai_method: bare AI 会尝试直接从方程解出 α 用 β 表示，代入模条件后陷入复杂代数运算，或尝试用三角不等式估计，无法发现因式分解的结构性捷径。
- correct_method: 因式分解 (α+1)(β+1)=-99 → 换元 u,v → 极坐标参数化 → 辐角互补 → 模方程消元 → M²=|uv|+1=100。

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——constraint_satisfaction / direct_calculation / structural_transformation 均可归入已有拓扑类别。
- [x] 粒度一致——与已有值粒度统一。
- [x] 不需要新的拓扑维度——三个维度足以区分这道题的tell。
- [ ] 拓扑分类无需进化。

**拓扑进化建议**（如有）：无。

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

**局部pairs概要**：
- R1: tell=AI看到方程但未识别因式分解结构, hint=观察方程结构识别已知/未知, topology=(constraint_satisfaction, direct_calculation, method_problem_mismatch)
- R2: tell=AI列出方向但未排序优先级, hint=列出所有可能方向, topology=(constraint_satisfaction, enumeration_brute_force, search_space_estimation)
- R3: tell=AI选择直接解出α代入模条件陷入代数泥潭, hint=尝试直接代入方向, topology=(constraint_satisfaction, direct_calculation, method_problem_mismatch)
- R4: tell=AI未注意到αβ+α+β可因式分解, hint=因式分解代换, topology=(constraint_satisfaction, algebraic_identity, knowledge_gap), is_knowledge_bottleneck=True
- R5: tell=AI已换元但未利用辐角互补, hint=极坐标参数化利用辐角关系, topology=(constraint_satisfaction, direct_calculation, structural_transformation)
- R6: tell=AI有两个模方程但未想到相减消元, hint=相减消元回代求M², topology=(constraint_satisfaction, direct_calculation, structural_transformation)
- R7: tell=AI得到M=10但未验证可取性, hint=验证并确认唯一解, topology=(constraint_satisfaction, logical_deduction, method_problem_mismatch)

**全局pairs概要**：
- GP1 (path_feature): tell=完整路径"因式分解→换元→辐角互补→消元→M²=|uv|+1"是不可分割的结构性洞察, hint=识别方程的因式分解结构是整个解题路径的入口, why_not_visible_locally=局部步骤中每一步看起来都是独立的代数操作，但"M²恰好等于|uv|+1"这个不变量只有在完成全部消元后才能看到，任何中间步骤都无法预见到这个简洁结果。
- GP2 (implicit): tell=uv为负实数隐含辐角互补(cos φ=-cos θ)是消元成功的关键, hint=利用乘积为实数推出辐角关系, why_not_visible_locally=在单独看任一模方程时，辐角关系隐含在uv=-99这个全局条件中，不展开极坐标并利用乘积辐角就无法发现两个方程间的对称消元结构。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI 大概率会尝试直接从方程解出 α=-(β+100)/(β+1) 代入模条件，得到 |β+100|=|β|·|β+1| 后展开成复杂的多项式方程，无法简化。或者尝试用三角不等式 |αβ|≤M² 估计，得到 M²≥99 但无法确定精确值。关键障碍是不会想到因式分解 (α+1)(β+1)=-99 这一结构性变换。
- suitable_for_poc: ["hint_injection_effectiveness", "tell_detection_from_thinking", "structural_transformation_gap"]
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

## Step 10: 入库ArangoDB [ ]

**操作**：用exec工具执行Python脚本入库

**数据库连接**：
- host: http://localhost:8529
- database: xishujuzhen_math_glm52
- username: root
- password: REDACTED-DB-PASSWORD

**入库步骤**：
1. 将profile JSON写入`problem_profiles`集合（overwrite=True，_key=problem_id）
2. 更新`problem_extraction_progress`集合中`_key="329733"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/matharena_MathArena_hmmt_feb_2026_0031"
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
    '_key': '329733',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/matharena_MathArena_hmmt_feb_2026_0031',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('matharena_MathArena_hmmt_feb_2026_0031')
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
- problem_id: matharena_MathArena_hmmt_feb_2026_0031
- solution_method_type: structural_transformation
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否，已有拓扑分类够用
- 是否遇到异常: 否

**操作**：向Master Agent报告

**汇报内容**：
- problem_id:
- solution_method_type:
- 局部(tell,hint)对数量:
- 全局(tell,hint)对数量:
- 是否发现新维度:
- **拓扑分类是否有进化建议**:
- 是否遇到异常:

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
