# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003648
- **文件路径**: subagents-dirs/omni_math_003648/problem.lean
- **来源**: AoPS omni_math (balkan_mo_shortlist)
- **ArangoDB progress记录_key**: 333527（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003648/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：求所有函数 f: R⁺ → R⁺ 使得 f(xf(x+y)) = yf(x) + 1 对所有 x, y ∈ R⁺ 成立。
- 解答核心思路（1-2句话）：观察到 RHS 关于 y 线性，猜测 f(x) = c/x 使 LHS 也关于 y 线性，代入得 c=1，即 f(x)=1/x。验证后代入即成立。
- 解答关键步骤列表：
  1. 观察方程结构：RHS = yf(x)+1 关于 y 线性
  2. 猜测 f(x) = c/x（倒数形式），因为此时 xf(x+y) = xc/(x+y)，f(xc/(x+y)) = (x+y)/x = 1+y/x 也关于 y 线性
  3. 匹配系数：LHS = 1 + y/x，RHS = 1 + yc/x，得 c=1
  4. 验证 f(x) = 1/x：f(xf(x+y)) = f(x/(x+y)) = (x+y)/x = 1 + y/x = y·(1/x) + 1 = yf(x)+1 ✓
  5. 唯一性：需证明 f 是唯一解（通过内射性论证）

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
| 1 | 纯元认知观察 | 0.8 | 观察函数方程 f(xf(x+y)) = yf(x) + 1，描述其结构特征：已知什么、未知什么、方程两边各自有什么特点？ | 未知函数 f: R⁺→R⁺，方程对所有 x,y>0 成立。LHS 是 f 在复合参数 xf(x+y) 处求值，RHS 是 yf(x)+1，关于 y 是线性的。 |
| 2 | 自由列举 | 0.7 | 针对这个函数方程，你能想到哪些可能的解题方向？列出所有方向。 | 尝试特定函数形式（常数、线性、倒数）；做特殊代入（固定x让y变化）；尝试建立内射性/满射性；从RHS关于y的线性结构入手猜测f的形式。 |
| 3 | 小尝试 | 0.5 | 试试 f 是常数函数 f(x)=c 的情况，看看会发生什么。 | 若 f(x)=c，则 LHS=c，RHS=yc+1 随 y 变化而变化，矛盾。所以 f 不是常数。 |
| 4 | 思维操作引导 | 0.4 | RHS 是 yf(x)+1，关于 y 线性。什么样的 f 能让 LHS f(xf(x+y)) 也关于 y 线性？尝试 f(x)=c/x 的形式，计算 LHS。 | 若 f(x)=c/x，则 xf(x+y)=xc/(x+y)，f(xc/(x+y))=c/(xc/(x+y))=(x+y)/x=1+y/x，确实关于 y 线性。 |
| 5 | 推进 | 0.5 | 你发现 f(x)=c/x 使两边都关于 y 线性。现在代入匹配系数，确定 c 的值。 | LHS=1+y/x，RHS=1+yc/x。匹配 y 的系数：1/x=c/x，得 c=1。所以 f(x)=1/x。 |
| 6 | 思维操作引导 | 0.4 | 你找到了 f(x)=1/x 满足方程。但题目要求找"所有"函数，如何证明这是唯一解？ | 需要证明唯一性。从 P(x,y) 出发，固定 x 时 y↦yf(x)+1 是内射的，所以 f 在 {xf(x+y):y>0} 上内射。结合满射性（RHS 值域为 (1,∞)）可建立全局内射性，再推导 f(x)=1/x。 |
| 7 | 能量传递引导 | 0.6 | 你已经找到了候选函数并概述了唯一性论证。请总结完整解答。 | f(x)=1/x 是唯一解。验证：f(xf(x+y))=f(x/(x+y))=(x+y)/x=1+y/x=yf(x)+1 ✓。唯一性通过内射性论证完成。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.5+0.4+0.5+0.4+0.6 = 3.9
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R6"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R4"

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
- problem_type: characterization
- structure_features: 函数方程 f(xf(x+y))=yf(x)+1，RHS关于y线性，LHS为f在复合参数处求值。需找到所有满足条件的函数并证明唯一性。
- key_objects: ["函数 f: R⁺→R⁺", "函数方程", "复合参数 xf(x+y)", "线性结构 yf(x)+1"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["pattern_recognition", "ansatz", "coefficient_matching", "injectivity_argument", "verification"]
- primary_pattern: ansatz
- knowledge_required: ["函数方程基本技巧", "内射性证明", "满射性", "倒数函数性质", "系数匹配"]
- key_insight: RHS关于y线性这一结构特征暗示f(x)=c/x，因为倒数函数能使LHS的复合参数简化后也关于y线性

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: direct_algebraic_manipulation（直接代数操作，尝试各种代入化简）
- translation_to: ansatz_based_reasoning（基于结构特征的猜测-验证-唯一性论证）
- translation_type: method_translation（从直接操作翻译到基于ansatz的方法）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["reciprocal_ansatz", "linearity_in_y", "injectivity", "surjectivity_onto_(1,infty)", "coefficient_matching"]
- expected_ai_method: bare AI倾向于直接代入和代数操作，尝试各种特殊值代入化简方程，可能陷入繁琐计算而无法识别倒数ansatz
- correct_method: 从RHS关于y的线性结构出发，猜测f(x)=c/x使LHS也线性，匹配系数得c=1，再通过内射性证明唯一性

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type=characterization、ai_method_type=direct_manipulation、gap_type=method_translation都能归入已有的拓扑类别
- [x] 粒度是否一致——标注的值和已有值的粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [ ] 如果发现拓扑分类需要进化，在此写出建议：无

**拓扑进化建议**（如有）：无，现有拓扑分类足够

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部pairs概要**：
- R1: tell="AI面对函数方程尚未识别RHS关于y的线性结构", hint="描述方程结构，注意RHS yf(x)+1关于y线性", level=0.8, 纯元认知观察
- R2: tell="AI列出方向但未将线性结构与函数形式猜测联系", hint="从RHS线性出发思考什么f使LHS也线性", level=0.7, 自由列举
- R3: tell="AI尝试常数被排除但未尝试倒数形式", hint="常数不行，试试f(x)=c/x", level=0.5, 小尝试
- R4: tell="AI未识别RHS线性→倒数ansatz的关键转折", hint="RHS关于y线性，尝试f(x)=c/x使LHS也线性", level=0.4, 思维操作引导
- R5: tell="AI找到f(x)=c/x使两边线性但未确定c", hint="代入匹配y的系数确定c", level=0.5, 推进
- R6: tell="AI找到f(x)=1/x但未意识到需证明唯一性", hint="题目要求'所有'函数，需证明唯一性", level=0.4, 思维操作引导, is_knowledge_bottleneck=True
- R7: tell="AI已完成验证和唯一性概述需收尾", hint="总结完整解答", level=0.6, 能量传递引导

**全局pairs概要**：
- path_feature型: tell="AI在直接代数操作中无法自发识别RHS线性→倒数ansatz的翻译路径", hint="从RHS线性结构猜测f(x)=c/x", level=0.5, generalizability=high
- implicit型(R6): tell="AI验证后未意识到'find all'隐含唯一性证明", hint="需证明唯一性", level=0.4, generalizability=high

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "marginal"
- bare_ai_error_prediction: "AI可能通过试错猜到f(x)=1/x（因为这是常见函数方程解），但可能无法自发从RHS线性结构推导出倒数ansatz，且很可能在验证后忽略唯一性证明"
- suitable_for_poc: ["ansatz_recognition", "uniqueness_awareness", "structure_to_form_translation"]
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
2. 更新`problem_extraction_progress`集合中`_key="333527"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/omni_math_003648"
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
    '_key': '333527',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003648',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('omni_math_003648')
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
- problem_id: omni_math_003648
- solution_method_type: ansatz_verification
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有拓扑分类（characterization / direct_manipulation / method_translation）足够覆盖
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
