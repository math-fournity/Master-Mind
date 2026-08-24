# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003864
- **文件路径**: subagents-dirs/omni_math_003864/problem.lean
- **来源**: AoPS omni_math (imo)
- **ArangoDB progress记录_key**: 333743（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003864/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：n²个站点在山坡上不同海拔，两个缆车公司A和B各运营k辆车，每辆从低到高，k个不同起点k个不同终点且起点高终点也高。linked = 可经一辆或多辆车到达。求最小k保证有两站被两公司都linked。
- 解答核心思路（1-2句话）：每公司缆车图是顶点不相交有向路径集合（入度≤1出度≤1无环），k辆车→n²-k条路径。k=n²-n+1时每公司n-1条路径，两划分各n-1部分，(n-1)²<n²故必有交集≥2。下界用n×n网格构造。
- 解答关键步骤列表：
  1. 下界构造：n×n网格，A行内连接B列内连接，k=n²-n，行link和列link不交
  2. 图结构分析：入度≤1（终点不同），出度≤1（起点不同），无环（低→高）→有向路径集合
  3. 路径计数：路径数 = 顶点数 - 边数 = n² - k
  4. 上界：k=n²-n+1 → 每公司n-1条路径 → (n-1)²个交集格 < n² → 矛盾
  5. 答案：n² - n + 1

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
| 1 | 纯元认知观察 | 0.8 | 描述题目结构：关键对象、约束、优化目标 | n²站点全序，两公司各k辆保序匹配，linked=传递闭包，求最小k保证两公司有公共linked对 |
| 2 | 自由列举 | 0.7 | 列出所有可能方法，哪些最有前景？ | 小案例、图结构、计数/鸽巢、构造反例、传递闭包分析。图结构和构造最有前景 |
| 3 | 小尝试 | 0.5 | 试n=2, k=2=n²-n，能否构造无公共linked对的配置？ | 2×2网格，A行内连接B列内连接，行link和列link不交，k=2不够 |
| 4 | 思维操作引导 | 0.4 | 分析缆车图的入度和出度，什么结构？ | 入度≤1出度≤1无环→顶点不相交有向路径，linked=同路径 |
| 5 | 思维操作引导 | 0.3 | k条边n²个顶点，多少条路径？ | 路径数=n²-k（每条边减少一个连通分量） |
| 6 | 推进 | 0.4 | k=n²-n+1→每公司n-1条路径，用计数论证两划分必有交集≥2 | (n-1)²个交集格≤(n-1)²<n²，矛盾 |
| 7 | 能量传递引导 | 0.6 | 总结完整解答 | 下界网格构造+上界路径鸽巢，答案n²-n+1 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 3.7
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: R4
- thinking_bottleneck（思维瓶颈在哪轮，或null）: R6

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
- structure_features: n²站点全序，两公司各定义保序匹配，linked=传递闭包，图结构约束（入度≤1出度≤1无环）→路径分解，阈值k处两路径划分必非平凡相交
- key_objects: 全序n²站点集合, 保序匹配(缆车), 有向无环图(度约束), 路径分解/划分, 传递闭包(linked关系), 划分交集计数

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: [小案例分析, 图结构分析, 路径分解, 鸽巢计数, 构造与证明]
- primary_pattern: 图结构分析（路径分解是核心转折）
- knowledge_required: [图论基础(入度出度有向路径), 鸽巢原理, 传递闭包, 划分交集计数]
- key_insight: 每公司缆车图是顶点不相交有向路径集合(n²-k条路径)，问题归约为两划分各n-1部分必有交集≥2元素的鸽巢论证

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接推理linked对和缆车连接
- translation_to: 图路径分解 + 划分交集鸽巢计数
- translation_type: 结构变换（structural_transformation）

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: discrete_combinatorial, ai_method_type: enumeration_brute_force, gap_type: structural_transformation}
- tell_small_concepts: [路径分解, 入度出度约束, 划分交集鸽巢, 保序匹配, 传递闭包, 有向无环图]
- expected_ai_method: bare AI会直接推理哪些站点对被两公司都linked，尝试案例分析或枚举缆车配置，不识别路径分解结构
- correct_method: 识别缆车图为有向路径集合（度约束+无环），路径数=n²-k，鸽巢论证划分交集得下界，网格构造得上界

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——problem_type=discrete_combinatorial, ai_method_type=enumeration_brute_force, gap_type=structural_transformation均可归入已有类别
- [x] 粒度一致——与已有值粒度统一
- [x] 三个维度足够区分这道题的tell和已有tell
- [ ] 无需新拓扑维度

**拓扑进化建议**：无。已有分类体系足够覆盖此题。

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
- 全局tell_hint_pairs数量: 3 对
- 全局pair中path_feature型: 1 个，implicit型: 2 个

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: fail
- bare_ai_error_prediction: bare AI会直接推理哪些站点对被两公司都linked，尝试案例分析或枚举配置，错过路径分解的关键结构洞察，无法找到阈值k
- suitable_for_poc: [tell_identification, hint_injection_effectiveness, structural_transformation_gap]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON

**将完整JSON写入工作目录的 `profile.json` 文件** — 已完成，JSON验证通过。

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: omni_math_003864
- solution_method_type: graph_decomposition_pigeonhole
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 3
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 无，已有分类体系足够覆盖
- 是否遇到异常: problem.lean中Solution文本被截断，已根据题目结构和答案重构完整解答

---

## 约束提醒

- **你只处理这一道题**，不要自行领取下一道题
- **不要更新AGENTS.md或Schema文件**，发现新维度或拓扑问题在profile中标注并在汇报中提出
- **不要做Master Agent的工作**——不管理并发，不建集合，不写任务追踪文档
- **situation_type只能取6个规范值**：纯元认知观察|自由列举|小尝试|思维操作引导|推进|能量传递引导
- **hint_level必须是0-1浮点数**
- **每个tell_hint_pair和global_tell_hint_pair都必须包含tell_topology和tell_small_concepts**
- **拓扑标注优先用已有值**，新建时检查粒度，太具体的值不要用
