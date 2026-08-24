# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: omni_math_003243
- **文件路径**: subagents-dirs/omni_math_003243/problem.lean
- **来源**: AoPS omni_math (putnam)
- **ArangoDB progress记录_key**: 333121（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `subagents-dirs/omni_math_003243/problem.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Shanille O'Keal罚球，第一个命中第二个错过，之后每次命中概率=之前命中率（已命中数/已投数）。求前100球中恰好命中50球的概率。
- 解答核心思路（1-2句话）：用归纳法证明：投n球后，命中1到n-1球中任意特定数量的概率都等于1/(n-1)（均匀分布）。n=100时恰好命中50球的概率=1/99。
- 解答关键步骤列表：
  1. 基础情形n=2：命中1球，概率=1=1/(2-1) ✓
  2. 归纳假设：投n球后，命中任意i球(1≤i≤n-1)的概率=1/(n-1)
  3. 归纳步：投n+1球后命中i球的概率 = (i-1)/n · 1/(n-1) + (n-i)/n · 1/(n-1) = [(i-1)+(n-i)]/[n(n-1)] = (n-1)/[n(n-1)] = 1/n
  4. 结论：投n球后均匀分布成立，n=100时P(恰好50球)=1/99

---

## Step 2: QA序列分析——局部视角7步 [x]

**操作**：重构"什么提示序列能引导AI从题目走到解答"，构造5-8轮Q&A对话

**产出**（在此填写每轮）：

| Round | situation_type | level | question | expected_answer |
|---|---|---|---|---|
| 1 | 纯元认知观察 | 0.3 | 描述这道题的结构：已知什么（初始条件、概率规则），未知什么（求什么），概率过程的关键特征是什么？ | 已知：第一球命中、第二球错过，之后命中概率=已命中数/已投总数。未知：前100球中恰好命中50球的概率。关键特征：概率依赖于当前状态（命中率），是一个状态依赖的随机过程。 |
| 2 | 自由列举 | 0.5 | 列出所有可能解决这个概率问题的方法方向。 | 1) 直接计算所有可能序列的概率（指数复杂度）；2) 递推/动态规划；3) 生成函数；4) 小情形枚举找规律；5) 归纳法证明一般性结论；6) 马尔可夫链分析。 |
| 3 | 小尝试 | 0.4 | 试算n=3,4,5时各命中数的概率，看看有没有规律。 | n=3: P(1球)=1/2, P(2球)=1/2。n=4: P(1)=1/3, P(2)=1/3, P(3)=1/3。n=5: P(1)=1/4,...,P(4)=1/4。规律：投n球后，命中1到n-1球中每个数的概率都等于1/(n-1)——均匀分布！ |
| 4 | 思维操作引导 | 0.6 | 你发现了均匀分布的规律。现在请将其形式化为归纳假设：投n球后，命中任意i球(1≤i≤n-1)的概率等于什么？ | 归纳假设：投n球后，对任意i∈{1,2,...,n-1}，P(恰好命中i球)=1/(n-1)。基础情形n=2：P(命中1球)=1=1/(2-1) ✓ |
| 5 | 推进 | 0.5 | 假设归纳假设对n成立，证明对n+1也成立。投n+1球后命中i球的概率由哪两种情况组成？分别计算并合并。 | 情况1：n球时命中i-1球(概率1/(n-1))，第n+1球命中(概率(i-1)/n)，贡献(i-1)/[n(n-1)]。情况2：n球时命中i球(概率1/(n-1))，第n+1球未中(概率(n-i)/n)，贡献(n-i)/[n(n-1)]。合计=[(i-1)+(n-i)]/[n(n-1)]=(n-1)/[n(n-1)]=1/n ✓ |
| 6 | 能量传递引导 | 0.3 | 归纳法已完成。现在应用结论：投100球后恰好命中50球的概率是多少？ | 由归纳结论，投n球后命中任意i球(1≤i≤n-1)的概率=1/(n-1)。n=100, i=50：P=1/(100-1)=1/99。 |

**统计**：
- total_rounds: 6
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 1
- level_sum: 2.6
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: "R4"
- thinking_bottleneck（思维瓶颈在哪轮，或null）: "R3"

---

## Step 3: 标注问题拓扑层 [x]

**产出**：
- problem_type: characterization
- structure_features: 状态依赖概率过程（转移概率=当前命中率），需证明均匀分布性质；归纳法核心
- key_objects: ["state-dependent probability process", "uniform distribution", "induction on n", "proportion-dependent transition probability"]

---

## Step 4: 标注解答思维模式层 [x]

**产出**：
- thinking_patterns: ["pattern recognition from small cases", "induction hypothesis formulation", "case analysis in inductive step", "uniform distribution recognition"]
- primary_pattern: induction hypothesis formulation
- knowledge_required: ["conditional probability", "mathematical induction", "probability distributions", "uniform distribution"]
- key_insight: 投n球后，命中1到n-1球中每个数量都等概率（1/(n-1)）——状态依赖概率过程产生均匀分布，这反直觉

---

## Step 5: 标注翻译方向层 [x]

**产出**：
- translation_from: direct probability calculation (逐序列条件概率计算)
- translation_to: induction proving uniform distribution property (归纳法证明均匀分布)
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "characterization", ai_method_type: "direct_calculation", gap_type: "method_translation"}
- tell_small_concepts: ["uniform distribution", "induction hypothesis", "state-dependent probability", "proportion of hits", "equally likely outcomes"]
- expected_ai_method: direct_calculation — bare AI会尝试逐序列追踪所有命中/未命中序列的条件概率，导致指数复杂度计算
- correct_method: 归纳法证明均匀分布——投n球后每个命中数(1到n-1)等概率1/(n-1)，n=100时答案1/99

### 6b. 反思拓扑分类

- [x] 当前拓扑分类够用——characterization + direct_calculation + method_translation能准确描述这道题的tell
- [x] 粒度一致——与已有值粒度统一
- [x] 不需要新维度——三个维度足够区分
- [ ] 无需进化建议

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 6 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

局部pairs详见profile.json中tell_hint_pairs字段。
全局pairs详见profile.json中global_tell_hint_pairs字段。

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: bare AI会尝试逐序列追踪所有命中/未命中序列的条件概率，导致指数复杂度计算。或者尝试朴素递推但不识别均匀分布性质，陷入复杂条件概率计算无法简化。关键缺口在于不会从小情形发现均匀分布规律并形式化为归纳假设。
- suitable_for_poc: ["POC-VMS-8 (hint injection)", "POC-VMS-9/10 (tell identification)"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

完整profile JSON已写入 `subagents-dirs/omni_math_003243/profile.json`

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证输出：omni_math_003243, 6 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

- problem_id: omni_math_003243
- solution_method_type: induction_uniform_distribution
- 局部(tell,hint)对数量: 6
- 全局(tell,hint)对数量: 2
- 是否发现新维度: 否
- 拓扑分类是否有进化建议: 否（已有拓扑分类characterization + direct_calculation + method_translation足够）
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
