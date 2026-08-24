# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo2001p5
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo2001P5.lean
- **来源**: IMO 2001 P5
- **ArangoDB progress记录_key**: 329179（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo2001P5.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let ABC be a triangle. Let AP bisect ∠BAC and let BQ bisect ∠ABC, with P on BC and Q on AC. If AB + BP = AQ + QB and ∠BAC = 60°, what are the angles of the triangle?
- 解答核心思路（1-2句话）：设 x = ∠ABQ = ∠QBC（B角的一半），用正弦定理将 BP、AQ、QB 都用 AB 表示，代入条件 AB + BP = AQ + QB 得到关于 x 的三角方程，解方程得 x = 40°，从而 ∠ABC = 80°，∠ACB = 40°。
- 解答关键步骤列表：
  1. 设 x = ∠ABQ = ∠QBC，则 ∠ABC = 2x，∠ACB = 120° - 2x，x ∈ (0°, 60°)
  2. 角度追踪：∠APB = 150° - 2x，∠AQB = 120° - x
  3. 用正弦定理在 △ABP 中表达 BP = sin30°/sin(150°-2x) · AB
  4. 用正弦定理在 △ABQ 中表达 AQ = sin x/sin(120°-x) · AB
  5. 用正弦定理在 △ABQ 中表达 QB = sin60°/sin(120°-x) · AB
  6. 代入 AB + BP = AQ + QB，消去 AB，得到关键三角方程：1 + sin30°/sin(150°-2x) = (sin x + sin60°)/sin(120°-x)
  7. 通过一系列三角恒等变换（和差化积、倍角公式等）化简方程
  8. 最终解出 x = 2π/9 = 40°，得 ∠ABC = 80°，∠ACB = 40°

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
| 1 | 纯元认知观察 | 0.8 | 仔细阅读这道题：三角形ABC中，AP平分∠BAC，BQ平分∠ABC，P在BC上，Q在AC上，AB+BP=AQ+QB，∠BAC=60°，求三角形各角。请描述这道题的结构——已知条件有哪些？未知量是什么？各条件之间有什么关联？ | 已知：∠BAC=60°，AP是角平分线，BQ是角平分线，AB+BP=AQ+QB。未知：三角形ABC的三个角。关联：角平分线给出角度等分关系，长度条件AB+BP=AQ+QB连接了不同边段。由于∠BAC=60°已知，实际只需再求一个角即可确定三角形。 |
| 2 | 自由列举 | 0.7 | 这道题涉及角平分线和长度等式条件。请列出所有你可能用来攻克这道题的数学工具和方向，不需要判断哪个最好，先穷举。 | 方向列举：①坐标法/解析几何——设坐标系用距离公式；②正弦定理——在子三角形中用正弦定理表达各边段；③余弦定理——用余弦定理建立边角关系；④角平分线定理——利用角平分线分对边比例性质；⑤设未知角x=∠ABQ，用角度追踪把所有角用x表示；⑥三角恒等变换——把长度条件转化为三角方程；⑦纯几何方法——构造辅助线寻找几何关系。 |
| 3 | 小尝试 | 0.4 | 试试用角平分线定理来处理这个问题。AP平分∠BAC，BQ平分∠ABC，角平分线定理能给出什么比例关系？看看能不能直接用这些比例关系配合AB+BP=AQ+QB求出角度。 | 角平分线定理：BP/PC = AB/AC，AQ/QC = AB/BC。但这些比例涉及AC和BC，它们本身也依赖于未知角度。设∠ABC=2x，则AC/AB = sin2x/sin(120°-2x)，BC/AB = sin60°/sin(120°-2x)。代入角平分线定理得到BP和AQ的表达式，但仍然涉及多个未知量，直接用角平分线定理难以简化AB+BP=AQ+QB这个条件——因为条件中还有QB这个不在角平分线定理直接覆盖范围内的量。这条路似乎不够直接。 |
| 4 | 思维操作引导 | 0.3 | 角平分线定理这条路不够直接，因为条件AB+BP=AQ+QB中QB不在角平分线定理的直接覆盖范围内。换一个思路：设x=∠ABQ=∠QBC（B角的一半），用角度追踪把所有相关角用x表示出来，然后用正弦定理在各个子三角形中把BP、AQ、QB都用AB表示。请执行这个操作。 | 设x=∠ABQ=∠QBC，则∠ABC=2x，∠ACB=120°-2x。角度追踪：在△ABP中，∠BAP=30°（AP平分60°），∠ABP=2x，所以∠APB=150°-2x。在△ABQ中，∠BAQ=60°（即∠BAC），∠ABQ=x，所以∠AQB=120°-x。用正弦定理：BP/sin30° = AB/sin(150°-2x)，所以BP = sin30°/sin(150°-2x)·AB。AQ/sinx = AB/sin(120°-x)，所以AQ = sinx/sin(120°-x)·AB。QB/sin60° = AB/sin(120°-x)，所以QB = sin60°/sin(120°-x)·AB。 |
| 5 | 思维操作引导 | 0.2 | 现在你已经把BP、AQ、QB都用AB表示了。把这三个表达式代入条件AB+BP=AQ+QB，消去AB，得到关于x的方程。请写出这个方程。 | 代入：AB + sin30°/sin(150°-2x)·AB = sinx/sin(120°-x)·AB + sin60°/sin(120°-x)·AB。两边除以AB：1 + sin30°/sin(150°-2x) = (sinx + sin60°)/sin(120°-x)。这就是关于x的关键三角方程。 |
| 6 | 推进 | 0.5 | 你现在有了方程 1 + sin30°/sin(150°-2x) = (sinx + sin60°)/sin(120°-x)，x∈(0°,60°)。请尝试用三角恒等变换化简并求解这个方程。提示：可以尝试和差化积、倍角公式，把方程化简到能直接判断x值的形式。 | 化简过程：右边分子sinx+sin60°用和差化积=2sin((x+60°)/2)cos((x-60°)/2)。分母sin(120°-x)=sin(60°+x)。进一步化简后，设y=x/2，利用cos的和差化积公式，最终方程化简为cos(3y+30°)=0或一个可排除的分支。由cos(3y+30°)=0且y的范围约束，得3y+30°=90°，y=20°，x=40°。验证：x=40°代入原方程成立。所以∠ABC=80°，∠ACB=40°。 |
| 7 | 能量传递引导 | 0.6 | 你已经解出了x=40°，得到了∠ABC=80°，∠ACB=40°。请总结这道题的解题路径，确认答案的正确性和完整性。 | 答案确认：∠BAC=60°（已知），∠ABC=80°，∠ACB=40°。三角和=180°✓。解题路径总结：①设半角x，角度追踪→②正弦定理表达所有边段→③代入长度条件得三角方程→④三角恒等变换化简→⑤解出x=40°。关键转折在于选择正弦定理而非角平分线定理，因为条件中QB需要正弦定理在△ABQ中表达。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.5
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: 6（三角恒等变换化简需要熟练的三角技巧知识）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: 4（从角平分线定理转向正弦定理+角度追踪的思维转换）

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
- problem_type: constraint_satisfaction
- structure_features: 三角形几何配置中，角平分线给出角度等分约束，长度等式AB+BP=AQ+QB给出边段约束，已知一个角∠BAC=60°，需确定所有角度。本质是在几何约束下求解唯一满足条件的三角形。
- key_objects: 三角形ABC、角平分线AP和BQ、半角x=∠ABQ、正弦定理、三角方程

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["角度参数化——设半角x将所有角度统一表达", "正弦定理归约——将几何长度条件转化为三角方程", "试错排除——先试角平分线定理发现不可行后转向正弦定理", "三角恒等变换——和差化积、倍角公式化简方程", "范围约束求解——利用x的范围排除多余解"]
- primary_pattern: 正弦定理归约——将几何长度条件转化为三角方程
- knowledge_required: ["正弦定理", "角平分线定理", "三角恒等变换（和差化积、倍角公式）", "三角形角度和定理", "角度追踪"]
- key_insight: 选择正弦定理而非角平分线定理，因为条件AB+BP=AQ+QB中的QB需要用正弦定理在△ABQ中表达，角平分线定理无法直接覆盖QB。

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 几何长度条件（AB+BP=AQ+QB）
- translation_to: 三角方程（1 + sin30°/sin(150°-2x) = (sinx + sin60°)/sin(120°-x)）
- translation_type: method_translation（通过正弦定理将几何边段关系翻译为三角函数方程，再通过三角恒等变换求解）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

**⚠️ 这一步不只是机械标注，必须同时思考以下问题**：

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["角平分线定理", "正弦定理", "角度参数化", "三角方程", "和差化积", "半角设定"]
- expected_ai_method: bare AI预期会用角平分线定理直接处理，因为题目中明确提到角平分线，AI会自然想到角平分线定理，但这条路无法覆盖条件中的QB项，导致陷入困境。
- correct_method: 设半角x，用正弦定理在子三角形中表达所有边段，代入长度条件得到三角方程，再用三角恒等变换化简求解。

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
- [x] 当前拓扑分类是否够用——这道题的problem_type/ai_method_type/gap_type能否归入已有的拓扑类别？→ 是。constraint_satisfaction已有，direct_manipulation已有，method_translation已有。
- [x] 粒度是否一致——你标注的值和已有值的粒度是否统一？→ 是，三个值都是中等粒度，与已有值一致。
- [x] 是否需要新的拓扑维度——三个维度是否足够区分这道题的tell和已有tell？→ 足够。这道题的tell核心是"方法翻译"——从几何语言翻译到三角方程语言，gap_type=method_translation精准描述。
- [x] 如果发现拓扑分类需要进化，在此写出建议：→ 无需进化，现有分类足够。

**拓扑进化建议**（如有）：无需进化。现有拓扑分类（constraint_satisfaction, direct_manipulation, method_translation）完全覆盖这道题的特征。

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

### 局部tell_hint_pairs详情：

**R1**: tell="AI面对题目尚未开始分析，处于初始状态" hint="描述题目结构，识别已知/未知/关联" hint_level=0.8 situation_type=纯元认知观察 is_knowledge_bottleneck=false tell_topology={problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "method_problem_mismatch"} tell_small_concepts=["题目结构识别", "已知未知分析", "条件关联"]

**R2**: tell="AI已理解题目结构但尚未选择方向" hint="穷举所有可能的数学工具和方向" hint_level=0.7 situation_type=自由列举 is_knowledge_bottleneck=false tell_topology={problem_type: "constraint_satisfaction", ai_method_type: "enumeration_brute_force", gap_type: "search_space_estimation"} tell_small_concepts=["方向穷举", "工具列举", "正弦定理", "角平分线定理", "坐标法"]

**R3**: tell="AI选择了角平分线定理方向，但此方向无法覆盖条件中的QB" hint="试角平分线定理，发现无法处理QB" hint_level=0.4 situation_type=小尝试 is_knowledge_bottleneck=false tell_topology={problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "method_problem_mismatch"} tell_small_concepts=["角平分线定理", "BP/PC比例", "QB不可达", "方法不匹配"]

**R4**: tell="AI在角平分线定理上碰壁，需要转向正弦定理+角度参数化" hint="设半角x，用正弦定理在子三角形中表达所有边段" hint_level=0.3 situation_type=思维操作引导 is_knowledge_bottleneck=false tell_topology={problem_type: "constraint_satisfaction", ai_method_type: "direct_calculation", gap_type: "method_translation"} tell_small_concepts=["半角参数化", "正弦定理", "角度追踪", "边段表达", "△ABP", "△ABQ"]

**R5**: tell="AI已用正弦定理表达所有边段，需要代入条件得到方程" hint="代入AB+BP=AQ+QB消去AB得到三角方程" hint_level=0.2 situation_type=思维操作引导 is_knowledge_bottleneck=false tell_topology={problem_type: "constraint_satisfaction", ai_method_type: "algebraic_identity", gap_type: "method_translation"} tell_small_concepts=["代入消元", "三角方程", "AB归约", "方程建立"]

**R6**: tell="AI已得到三角方程但不会化简求解，这是知识瓶颈" hint="用和差化积、倍角公式化简方程" hint_level=0.5 situation_type=推进 is_knowledge_bottleneck=true tell_topology={problem_type: "constraint_satisfaction", ai_method_type: "algebraic_identity", gap_type: "knowledge_gap"} tell_small_concepts=["和差化积", "倍角公式", "cos方程", "范围约束求解", "y=x/2代换"]

**R7**: tell="AI已解出x=40°，需要确认和总结" hint="总结解题路径，确认答案正确性" hint_level=0.6 situation_type=能量传递引导 is_knowledge_bottleneck=false tell_topology={problem_type: "constraint_satisfaction", ai_method_type: "logical_deduction", gap_type: "method_translation"} tell_small_concepts=["答案确认", "路径总结", "80°-40°-60°三角形", "正弦定理选择"]

### 全局tell_hint_pairs详情：

**G1 (path_feature型)**:
- scope_type: "path_feature"
- scope: "完整解题路径：角平分线定理试错→正弦定理转向→三角方程建立→三角恒等变换求解"
- observation_point: null
- tell: "完整路径特征是'试错后转向'——先试角平分线定理（因题目明示角平分线），碰壁后转向正弦定理+角度参数化。这个转向不是任意的，而是由条件中QB项的结构决定的。"
- hint: "当几何条件中包含不在角平分线定理覆盖范围内的边段时，应转向正弦定理进行统一参数化表达"
- hint_level: 0.6
- generalizability: "high——'试错后转向'模式和'正弦定理统一参数化'策略可泛化到所有包含角平分线+长度条件的几何题"
- why_not_visible_locally: "在局部视角中，AI只能看到当前步骤的困难（角平分线定理无法处理QB），但看不到'转向正弦定理后整个路径会通畅'这个完整路径特征。只有回顾完整路径才能识别出'角平分线定理是诱饵方向，正弦定理才是正确方向'这个模式。"
- tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "method_translation"}
- tell_small_concepts: ["角平分线定理试错", "正弦定理转向", "路径特征", "QB不可达信号"]

**G2 (implicit型)**:
- scope_type: "implicit"
- scope: "条件AB+BP=AQ+QB中QB的隐含信息"
- observation_point: "R3"
- tell: "条件AB+BP=AQ+QB中QB这一项隐含了'必须用正弦定理而非角平分线定理'的信号——QB是B到Q的距离，Q在AC上，QB不在任何角平分线定理的比例关系中，但可以用正弦定理在△ABQ中表达。这个隐含信息决定了方法选择。"
- hint: "检查长度条件中的每一项是否都能被所选方法覆盖，QB不在角平分线定理覆盖范围内是转向正弦定理的关键信号"
- hint_level: 0.5
- generalizability: "medium——'检查条件中每项的方法覆盖性'策略可泛化，但具体的QB信号是本题特有的"
- why_not_visible_locally: "在R3的局部视角中，AI只看到角平分线定理给出了BP和AQ的比例，但不会注意到QB这个项'恰好不在角平分线定理覆盖范围内'这个隐含信息。只有当AI明确检查'条件中每一项是否都能被当前方法表达'时，才能发现QB的不可达性是方法选择的关键信号。"
- tell_topology: {problem_type: "constraint_satisfaction", ai_method_type: "direct_manipulation", gap_type: "method_problem_mismatch"}
- tell_small_concepts: ["QB不可达", "方法覆盖性检查", "隐含方法选择信号", "条件项分析"]

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会被题目中明示的角平分线条件诱导，优先使用角平分线定理，但无法处理条件中的QB项。即使转向正弦定理，在三角方程化简阶段（和差化积、倍角公式、y=x/2代换）也极可能卡住，因为化简路径非常复杂且非标准。bare AI大概率无法独立完成从三角方程到x=40°的求解。
- suitable_for_poc: ["tell端验证——QB不可达信号作为方法选择tell的形式化过滤测试", "hint端验证——正弦定理转向提示的有效性测试", "知识瓶颈测试——三角恒等变换作为knowledge_gap的POC"]
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
2. 更新`problem_extraction_progress`集合中`_key="329179"`的记录：
   - extraction_status改为"completed"
   - schema_version改为3
   - extracted_at改为当前ISO时间
   - profile_doc_id改为"problem_profiles/compfiles_imo2001p5"
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
    '_key': '329179',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo2001p5',
    'extracted_by': 'subagent',
})
print('入库完成')
```

**验证**：入库后查询确认
```python
p = db.collection('problem_profiles').get('compfiles_imo2001p5')
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
- problem_id: compfiles_imo2001p5
- solution_method_type: trigonometric_reduction
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2（1个path_feature型 + 1个implicit型）
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 否，现有拓扑分类（constraint_satisfaction, direct_manipulation, method_translation）完全覆盖
- 是否遇到异常: 否，入库和验证均一次通过

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
