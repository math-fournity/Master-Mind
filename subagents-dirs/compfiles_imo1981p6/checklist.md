# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1981p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1981P6.lean
- **来源**: IMO 1981 P6
- **ArangoDB progress记录_key**: 329097（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1981P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Suppose f: ℕ × ℕ → ℕ satisfies: (1) f(0, y) = y+1; (2) f(x+1, 0) = f(x, 1); (3) f(x+1, y+1) = f(x, f(x+1, y)). Determine f(4, 1981).
- 解答核心思路（1-2句话）：这是Ackermann函数。逐层计算f在固定第一个参数时的闭式表达式，发现f(1,y)=y+2, f(2,y)=2y+3, f(3,y)=2^(y+3)-3, f(4,y)是迭代幂塔(2^·)^[y+3]1 - 3。最终f(4,1981) = (2^·)^[1984]1 - 3。
- 解答关键步骤列表：
  1. 用强归纳证明 f(1, y) = y + 2（基础层）
  2. 用归纳证明 f(2, y) = 2y + 3（线性层）
  3. 用归纳证明 f(3, y) + 3 = 2^(y+3)，即 f(3, y) = 2^(y+3) - 3（指数层）
  4. 用归纳证明 f(4, y+1) + 3 = 2^(f(4,y) + 3)（递推关系）
  5. 用归纳证明 f(4, y) + 3 = (2^·)^[y+3] 1（迭代幂塔层）
  6. 代入 y=1981，得 f(4, 1981) = (2^·)^[1984] 1 - 3

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
| 1 | 纯元认知观察 | 0.3 | 看看这道题：f: ℕ×ℕ→ℕ 满足三条递归规则，求f(4,1981)。先描述一下这个函数的结构——三条规则分别定义了什么？已知什么、未知什么？ | 三条规则定义了一个二元递归函数：规则1是基础情形f(0,y)=y+1；规则2是第一个参数递增且第二个参数为0时的边界；规则3是双重递归——f(x+1,y+1)要用f(x, ·)和f(x+1, y)来定义。已知是三条递归关系，未知是f(4,1981)的具体值。函数的递归结构使得直接计算f(4,1981)不可行，因为值会极其巨大。 |
| 2 | 自由列举 | 0.5 | 这个函数的递归结构让你想到了什么？列出你能想到的所有可能方向来求解f(4,1981)。 | 可能方向：(1)直接按定义展开计算（但f(4,1981)太大）；(2)先计算低层f(0,y), f(1,y), f(2,y)等，看是否有规律；(3)识别这个函数是否是某个已知函数（如Ackermann函数）；(4)对第二个参数y做归纳，固定第一个参数x，求f(x,y)的闭式；(5)寻找f(x+1,·)和f(x,·)之间的关系模式。 |
| 3 | 小尝试 | 0.4 | 试试直接展开f(4,1981)的前几步，看看会发生什么。 | 直接展开：f(4,1981) = f(3, f(4,1980)) = f(3, f(3, f(4,1979))) = ... 这会无限展开下去，因为f(4,y)总是需要f(4,y-1)，而每次展开又引入f(3,·)。直接展开行不通——需要先理解f(3,·)的行为，才能处理f(4,·)。 |
| 4 | 思维操作引导 | 0.35 | 既然直接展开行不通，换一个思维操作：固定x=0,1,2,3，分别对y做归纳，求出f(x,y)的闭式表达式。先从x=0和x=1开始。 | x=0: f(0,y)=y+1（已知）。x=1: f(1,0)=f(0,1)=2; f(1,y+1)=f(0,f(1,y))=f(1,y)+1。由归纳得f(1,y)=y+2。x=2: f(2,0)=f(1,1)=3; f(2,y+1)=f(1,f(2,y))=f(2,y)+2。由归纳得f(2,y)=2y+3。 |
| 5 | 思维操作引导 | 0.4 | 继续这个方向，现在求f(3,y)的闭式。注意观察f(3,y)和f(2,·)之间的关系——f(3,y+1)=f(2,f(3,y))，而f(2,z)=2z+3。这能告诉你什么？ | f(3,0)=f(2,1)=5。f(3,y+1)=f(2,f(3,y))=2·f(3,y)+3。令g(y)=f(3,y)+3，则g(y+1)=2·f(3,y)+3+3=2·(f(3,y)+3)=2·g(y)。g(0)=5+3=8=2^3。所以g(y)=2^(y+3)，即f(3,y)=2^(y+3)-3。 |
| 6 | 推进 | 0.45 | 现在到了关键一步：求f(4,y)。你已经知道f(3,z)=2^(z+3)-3，而f(4,y+1)=f(3,f(4,y))=2^(f(4,y)+3)-3。令h(y)=f(4,y)+3，写出h的递推关系，看看能否识别出这个序列。 | h(y)=f(4,y)+3。h(y+1)=f(4,y+1)+3=2^(f(4,y)+3)=2^h(y)。h(0)=f(4,0)+3=f(3,1)+3=2^4=16。所以h(y+1)=2^h(y)，h(0)=2^4。这就是迭代幂塔：h(y)=(2^·)^[y+3]1，即连续取2的幂(y+3)次从1开始。因此f(4,y)=(2^·)^[y+3]1-3。 |
| 7 | 能量传递引导 | 0.3 | 最后一步了！你已经有了f(4,y)的完整表达式，代入y=1981就得到答案。写出最终结果。 | f(4,1981) = (2^·)^[1981+3] 1 - 3 = (2^·)^[1984] 1 - 3。这是一个2的幂塔，高度为1984，减去3。这个数极其巨大，无法用十进制写出，但表达式(2^·)^[1984]1 - 3就是精确答案。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.3+0.5+0.4+0.35+0.4+0.45+0.3 = 2.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: null
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 5（关键转折：识别h(y)=f(4,y)+3的递推关系是迭代幂塔）

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
- problem_type: characterization（函数被递归关系定义，需要刻画/确定其在特定点的值）
- structure_features: 二元递归定义的函数，三层递归结构（基础情形、边界情形、双重递归），需要逐层求闭式表达式，最终值极其巨大无法显式写出
- key_objects: ["Ackermann函数", "递归定义", "归纳法", "闭式表达式", "迭代幂塔(tetration)", "函数迭代"]

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["逐层归纳", "变量替换识别模式", "从具体到抽象的递进", "失败方向诊断", "递推关系识别"]
- primary_pattern: 逐层归纳（固定一个参数，对另一个参数做归纳，逐层求闭式）
- knowledge_required: ["Ackermann函数", "数学归纳法", "函数迭代", "迭代幂塔(tetration)", "递推关系求解"]
- key_insight: 令h(y)=f(4,y)+3，则h(y+1)=2^h(y)，这是迭代幂塔的递推关系——将看似复杂的双重递归转化为可识别的函数迭代模式

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 递归定义语言（双重递归f(x+1,y+1)=f(x,f(x+1,y))）
- translation_to: 函数迭代语言（h(y+1)=2^h(y)，即迭代幂塔(2^·)^[n]1）
- translation_type: structural_transformation（通过变量替换h(y)=f(4,y)+3将递归结构转化为迭代结构，每一层f(x,·)的闭式是对前一层函数的迭代）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["逐层归纳", "闭式表达式", "变量替换", "迭代幂塔", "函数迭代", "递推关系识别"]
- expected_ai_method: 直接展开递归定义尝试计算f(4,1981)（bare AI会试图直接展开，但值太大无法计算）
- correct_method: 逐层归纳求闭式——固定x对y做归纳，从f(0,y)到f(4,y)逐层求出闭式表达式，识别迭代幂塔模式

### 6b. 反思拓扑分类

**必须回答以下问题**：
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？可以。characterization已有，direct_calculation已有，method_problem_mismatch已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？一致。characterization是抽象级，direct_calculation是抽象级，method_problem_mismatch是抽象级。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？足够。这道题的核心gap是"直接计算不可行，需要逐层归纳求闭式"，method_problem_mismatch准确描述了这个gap。
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化。现有拓扑分类可以覆盖。

**拓扑进化建议**（如有）：无。现有拓扑分类体系足够覆盖此题。

---

## Step 7: 提取(tell, hint)对 [x]

**操作**：从QA序列的每轮(状态, Q)中提取(tell, hint)对

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs**：

| Round | tell | hint | hint_level | situation_type | is_knowledge_bottleneck | tell_topology | tell_small_concepts |
|---|---|---|---|---|---|---|---|
| 1 | AI面对二元递归定义的函数，尚未识别其结构——三层递归规则的关系不清楚 | 描述函数结构，识别三条规则分别定义了什么 | 0.3 | 纯元认知观察 | false | {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"} | ["递归定义", "基础情形", "双重递归"] |
| 2 | AI识别了递归结构但不知道往哪个方向走——可能直接展开或可能逐层归纳 | 列出所有可能方向 | 0.5 | 自由列举 | false | {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"} | ["方向列举", "Ackermann函数", "逐层归纳"] |
| 3 | AI尝试直接展开f(4,1981)，发现无限递归无法终止 | 直接展开行不通，需要先理解低层行为 | 0.4 | 小尝试 | false | {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"} | ["直接展开", "无限递归", "失败诊断"] |
| 4 | AI从失败中认识到需要逐层求闭式，但尚未开始系统归纳 | 固定x对y做归纳，从x=0,1开始求闭式 | 0.35 | 思维操作引导 | false | {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "structural_transformation"} | ["逐层归纳", "闭式表达式", "基础层"] |
| 5 | AI已求出f(1,y)和f(2,y)，面对f(3,y)的递推关系需要变量替换技巧 | 观察f(3,y+1)=f(2,f(3,y))=2f(3,y)+3，令g(y)=f(3,y)+3 | 0.4 | 思维操作引导 | false | {problem_type: "characterization", ai_method_type: "algebraic_identity", gap_type: "structural_transformation"} | ["变量替换", "递推关系", "指数函数"] |
| 6 | AI已求出f(3,y)=2^(y+3)-3，面对f(4,y)的递推需要识别迭代幂塔模式 | 令h(y)=f(4,y)+3，写出h的递推关系，识别迭代幂塔 | 0.45 | 推进 | false | {problem_type: "characterization", ai_method_type: "algebraic_identity", gap_type: "method_translation"} | ["迭代幂塔", "函数迭代", "递推识别"] |
| 7 | AI已识别f(4,y)的迭代幂塔表达式，需要代入具体值完成 | 代入y=1981，写出最终结果 | 0.3 | 能量传递引导 | false | {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "method_problem_mismatch"} | ["代入计算", "幂塔高度", "最终答案"] |

**全局tell_hint_pairs**：

1. path_feature型：
- scope_type: "path_feature"
- scope: "从f(0,y)到f(4,y)的逐层归纳路径——每一层的闭式都是对前一层函数的迭代"
- observation_point: null
- tell: 整个解题路径的结构特征是"逐层递进"——f(1,y)是加法，f(2,y)是乘法，f(3,y)是指数，f(4,y)是迭代幂塔，每一层都是对前一层的迭代升级
- hint: 从最底层f(0,y)开始，逐层向上求闭式，注意每一层都是对前一层函数的迭代
- hint_level: 0.5
- generalizability: "high——这种逐层归纳求闭式的方法适用于所有类似的嵌套递归定义函数"
- why_not_visible_locally: "在任何一个单独的步骤中，只能看到当前层的归纳，看不到从加法→乘法→指数→迭代幂塔的完整升级模式。只有走完全部四层，才能识别出这个'每一层是前一层的迭代'的元模式。局部视角只能看到具体的递推关系，看不到整个函数族的迭代升级结构。"
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "structural_transformation"}
- tell_small_concepts: ["逐层归纳", "迭代升级", "加法→乘法→指数→迭代幂塔", "函数迭代"]

2. implicit型：
- scope_type: "implicit"
- scope: "R5-R6之间的关键转折：变量替换h(y)=f(4,y)+3将递推转化为迭代幂塔"
- observation_point: "R6"
- tell: f(4,y+1)+3=2^(f(4,y)+3)这个递推关系蕴含着迭代幂塔结构，但这个蕴含关系只有在做出正确的变量替换后才能被识别——h(y+1)=2^h(y)是幂塔的 defining 递推
- hint: 对递推关系做变量替换（平移），使其匹配已知函数迭代的递推形式
- hint_level: 0.6
- generalizability: "medium——变量替换识别递推模式是通用技巧，但'+3'这个具体偏移量是本题特有的"
- why_not_visible_locally: "在R6这一步，AI看到的是f(4,y+1)+3=2^(f(4,y)+3)，这是一个关于f(4,y)的递推。但'令h(y)=f(4,y)+3就能得到h(y+1)=2^h(y)'这个变量替换的洞察，在局部步骤中不可见——它需要AI同时持有两个认知：(1)当前的递推关系，(2)迭代幂塔的定义形式h(n+1)=2^h(n)。只有同时匹配这两个模式，才能发现'+3'是连接两者的桥梁。局部视角只看到递推，看不到它和幂塔定义之间的同构关系。"
- tell_topology: {problem_type: "characterization", ai_method_type: "algebraic_identity", gap_type: "method_translation"}
- tell_small_concepts: ["变量替换", "迭代幂塔识别", "递推同构", "平移变换"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "bare AI会尝试直接展开递归定义计算f(4,1981)，但发现值极其巨大无法直接计算。即使AI想到逐层归纳，也可能在f(3,y)的变量替换（令g(y)=f(3,y)+3）或f(4,y)的迭代幂塔识别上卡住——关键转折需要同时匹配递推关系和迭代幂塔定义形式，这需要跨步骤的模式识别能力。"
- suitable_for_poc: ["tell端去特化验证——path_feature型全局tell的迭代升级模式可去特化", "implicit型tell的变量替换识别验证", "思维瓶颈vs知识瓶颈区分——此题是思维瓶颈（模式识别）而非知识瓶颈"]
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

**将完整JSON写入工作目录的 `profile.json` 文件** ✅ 已写入

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
2. 更新`problem_extraction_progress`集合中`_key="329097"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo1981p6"
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
    '_key': '329097',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1981p6',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo1981p6')
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
- problem_id: compfiles_imo1981p6
- solution_method_type: inductive_layered_closed_form（逐层归纳求闭式）
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无。现有拓扑分类体系（characterization / direct_calculation / method_problem_mismatch / structural_transformation / method_translation / algebraic_identity）足够覆盖此题。
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
