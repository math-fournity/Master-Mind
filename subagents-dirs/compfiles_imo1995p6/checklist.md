# Subagent Analysis Checklist

> **这是你的工作清单。一上来全文读完，每完成一步把 `[ ]` 改为 `[x]` 并填写产出说明。全部完成后汇报。**

## 你的任务信息

- **problem_id**: compfiles_imo1995p6
- **文件路径**: knowledge/problem_banks/compfiles/Compfiles/Imo1995P6.lean
- **来源**: IMO 1995 P6
- **ArangoDB progress记录_key**: 329154（入库时用这个key更新progress记录）
- **Schema版本**: v3

---

## Step 1: 读取题目和解答 [x]

**操作**：用read工具读取 `knowledge/problem_banks/compfiles/Compfiles/Imo1995P6.lean`

**要求**：
- 从Lean注释块 `/-! ... -/` 中提取题目描述
- 从 `problem` / `theorem` 块中提取解答
- 将Lean解答翻译为数学语言理解
- 如果文件很长，分段读完

**产出**（在此填写）：
- 题目原文（数学描述）：Let p be an odd prime number. How many p-element subsets A of {1, 2, ..., 2p} are there, the sum of whose elements is divisible by p?
- 解答核心思路（1-2句话）：定义{1,...,p}上的循环移位σ（x→x+1 mod p, p→1），{p+1,...,2p}上为恒等映射。利用Z/pZ群作用，每个轨道中恰好一个子集的元素和被p整除，加上两个特殊子集{1,...,p}和{p+1,...,2p}，总数为2+(C(2p,p)-2)/p。
- 解答关键步骤列表：
  1. 定义shift函数：在{1,...,p}上做循环移位（x%p+1），其余位置恒等
  2. 证明shift是双射，迭代p次回到自身（Z/pZ作用）
  3. 关键引理：sum(σA) ≡ sum(A) + |A∩{1,...,p}| (mod p)，迭代i次后sum(σ^i A) ≡ sum(A) + i·|A∩{1,...,p}| (mod p)
  4. 对非特殊子集A（≠{1,...,p}, ≠{p+1,...,2p}），|A∩{1,...,p}| ∈ {1,...,p-1}，故非零mod p
  5. 当|A∩{1,...,p}| ≠ 0 mod p时，线性函数sum(A)+i·|A∩{1,...,p}|在i∈Z/pZ中恰好一次取0，即每个轨道恰好一个好子集
  6. 双重计数：C(2p,p)-2个非特殊子集分成大小为p的轨道，每个轨道贡献1个好子集，故好子集数=(C(2p,p)-2)/p
  7. 两个特殊子集{1,...,p}和{p+1,...,2p}的和都被p整除（利用p为奇数，sum=p(p+1)/2）
  8. 总数 = 2 + (C(2p,p)-2)/p

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
| 1 | 纯元认知观察 | 0.8 | 描述这道题的结构：已知什么、求什么、有哪些关键数学对象？ | 已知奇素数p，求{1,...,2p}的p元子集中元素和被p整除的子集个数。总共有C(2p,p)个p元子集，需要筛选和≡0 mod p的。关键对象：奇素数p、p元子集、模p整除条件。 |
| 2 | 自由列举 | 0.7 | 列出你能想到的所有方法来计数满足模条件的子集。 | 直接枚举、生成函数、Burnside引理/群作用、模算术、双重计数、归纳法、容斥原理... |
| 3 | 小尝试 | 0.5 | 试试p=3的情况，计算{1,...,6}的3元子集中和被3整除的有多少个？C(6,3)-2是否被3整除？ | C(6,3)=20，答案=2+(20-2)/3=2+6=8。可以验证C(6,3)-2=18确实被3整除。但这个数值规律的原因不明确。 |
| 4 | 思维操作引导 | 0.4 | 考虑定义一个循环群作用在子集上。在{1,...,p}上定义什么自然的循环作用？{p+1,...,2p}呢？ | 在{1,...,p}上定义循环移位σ(x)=x%p+1（即1→2→...→p→1），在{p+1,...,2p}上保持恒等。这给出Z/pZ在{1,...,2p}上的作用，进而作用在p元子集上。 |
| 5 | 推进 | 0.5 | 在这个移位作用下，子集A的元素和如何变化？用|A∩{1,...,p}|表示。 | sum(σA) ≡ sum(A) + |A∩{1,...,p}| (mod p)，因为{1,...,p}中的每个元素加1，其余不变。迭代i次：sum(σ^i A) ≡ sum(A) + i·|A∩{1,...,p}| (mod p)。 |
| 6 | 思维操作引导 | 0.3 | 当|A∩{1,...,p}| ≠ 0 mod p时，i从0到p-1中恰好几个使sum(σ^i A) ≡ 0？哪些子集是例外？ | 线性函数sum(A)+i·|A∩{1,...,p}|在Z/pZ上恰好一个零点（因为系数非零），所以每个轨道恰好一个好子集。例外是|A∩{1,...,p}|=0或p的子集，即{p+1,...,2p}和{1,...,p}，它们的和都被p整除（p为奇数时sum=p(p+1)/2）。 |
| 7 | 能量传递引导 | 0.6 | 你已经有了所有要素。组装最终答案：非特殊子集的轨道贡献+特殊子集。 | C(2p,p)-2个非特殊子集分成大小p的轨道，每个轨道1个好子集，共(C(2p,p)-2)/p个。加上2个特殊子集，总数=2+(C(2p,p)-2)/p。 |

**统计**：
- total_rounds: 7
- metacognitive_rounds（纯元认知观察+自由列举+推进+能量传递引导的轮数）: 4
- knowledge_rounds（思维操作引导的轮数）: 2
- level_sum: 0.8+0.7+0.5+0.4+0.5+0.3+0.6=3.8
- knowledge_bottleneck（知识瓶颈在哪轮，或null）: round 4（群作用/循环移位的识别是纯知识瓶颈）
- thinking_bottleneck（思维瓶颈在哪轮，或null）: round 6（将线性公式与轨道计数和例外情况分析连接是思维瓶颈）

---

## Step 3: 标注问题拓扑层 [x]

**操作**：从题目结构中提取

**产出**：
- problem_type: discrete_combinatorial
- structure_features: 计数{1,...,2p}的p元子集中满足元素和被p整除的子集个数；涉及Z/pZ群作用和轨道计数；将全集分成{1,...,p}和{p+1,...,2p}两半，循环移位只作用在前半
- key_objects: 奇素数p, p元子集, Z/pZ循环群作用, shift移位映射, 轨道, 两个特殊区间子集{1,...,p}和{p+1,...,2p}

---

## Step 4: 标注解答思维模式层 [x]

**操作**：从QA序列中提取

**产出**：
- thinking_patterns: ["group_action_orbit_counting", "double_counting", "modular_arithmetic", "exceptional_case_isolation", "linear_function_over_finite_field"]
- primary_pattern: group_action_orbit_counting
- knowledge_required: ["循环群在集合上的作用", "Burnside型轨道计数", "模算术", "素数性质", "二项式系数", "有限域上的线性函数"]
- key_insight: 在{1,...,p}上定义循环移位而{p+1,...,2p}保持恒等，和的变化是|A∩{1,...,p}|的线性函数，非零系数意味着每个轨道恰好一个好子集

---

## Step 5: 标注翻译方向层 [x]

**操作**：从QA序列中识别翻译操作

**产出**：
- translation_from: 直接计数/枚举（逐个检查子集和的模p值）
- translation_to: 群作用轨道分析（用Z/pZ作用将子集分轨道，每轨道恰好一个好子集）
- translation_type: method_translation

---

## Step 6: 标注tell拓扑层 + 反思拓扑分类是否需要进化 [x]

**操作**：从QA序列中提取tell_topology/small_concepts/expected_ai_method/correct_method

### 6a. 标注profile级拓扑

**产出**：
- tell_topology: {problem_type: "discrete_combinatorial", ai_method_type: "enumeration_brute_force", gap_type: "method_translation"}
- tell_small_concepts: ["cyclic_shift", "orbit_counting", "modular_sum", "group_action", "exceptional_subsets", "Z/pZ_action", "linear_sum_change"]
- expected_ai_method: 直接枚举或生成函数方法逐个计数和被p整除的子集
- correct_method: 定义循环群作用（前半移位），利用轨道结构和线性求和公式，每个轨道恰好一个好子集

### 6b. 反思拓扑分类

- [x] 当前拓扑分类是否够用——这道题的problem_type=discrete_combinatorial、ai_method_type=enumeration_brute_force、gap_type=method_translation都能归入已有拓扑类别
- [x] 粒度是否一致——标注值和已有值粒度统一
- [x] 是否需要新的拓扑维度——三个维度足够区分这道题的tell和已有tell
- [x] 如果发现拓扑分类需要进化，在此写出建议：无需进化，现有分类体系足够

**拓扑进化建议**（如有）：无

---

## Step 7: 提取(tell, hint)对 [x]

**产出**：
- 局部tell_hint_pairs数量: 7 对
- 全局tell_hint_pairs数量: 2 对
- 全局pair中path_feature型: 1 个，implicit型: 1 个

**局部tell_hint_pairs详见profile.json**

**全局tell_hint_pairs**：

1. path_feature型：
- scope: "完整解题路径：循环移位定义→和变化公式→轨道结构→计数"
- tell: "关键insight是在{1,...,p}上定义循环移位使和的变化成为线性函数，从而用轨道计数"
- hint: "定义前半循环移位，计算和变化，用轨道结构计数"
- why_not_visible_locally: "完整路径——移位定义→和变化公式→轨道结构→计数——需要看到所有环节如何连接。在任一单步中，只在前半定义移位看似任意；只有完整路径才揭示为什么这个特定作用使计数成立。"

2. implicit型：
- scope: "C(2p,p)-2被p整除这一隐含事实"
- observation_point: Q3
- tell: "C(2p,p)-2必须被p整除，这不显然但由轨道结构保证"
- hint: "C(2p,p)-2被p整除本身暗示有一个p阶群作用在C(2p,p)-2个非特殊子集上"
- why_not_visible_locally: "在Q3计算小案例时可能注意到C(2p,p)-2被p整除，但原因（p阶群的轨道结构）从数值规律本身不可见——需要群作用框架来解释。"

---

## Step 8: 标注实验适用性层 [x]

**产出**：
- bare_ai_expected: "fail"
- bare_ai_error_prediction: "Bare AI会尝试直接枚举、生成函数或归纳法。可能正确计算小案例但无法找到一般公式。关键insight——在前半{1,...,p}上定义循环移位并利用轨道计数——非显然，需要识别群作用结构。AI可能尝试在整个{1,...,2p}上做循环移位，但这不会给出正确的轨道大小（因为2p不是p的倍数时轨道结构不同）。"
- suitable_for_poc: ["tell_hint_injection", "group_action_recognition", "orbit_counting_guidance"]
- discriminates_levels: true

---

## Step 9: 输出完整profile JSON [x]

**操作**：将以上所有产出组装成完整profile JSON，写入profile.json

**完整字段清单核对**：
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
- [x] answer
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
- [x] tell_hint_pairs
- [x] global_tell_hint_pairs
- [x] bare_ai_expected
- [x] bare_ai_error_prediction
- [x] suitable_for_poc
- [x] discriminates_levels
- [x] qa_sequence
- [x] analysis_metadata

---

## Step 10: 入库ArangoDB [x]

**产出**：
- 入库结果: [x] 成功 / [ ] 失败
- 验证结果: [x] 通过 / [ ] 失败

验证输出: compfiles_imo1995p6, 7 local pairs, 2 global pairs

---

## Step 11: 汇报 [x]

**汇报内容**：
- problem_id: compfiles_imo1995p6
- solution_method_type: group_action_orbit_counting
- 局部(tell,hint)对数量: 7
- 全局(tell,hint)对数量: 2 (1 path_feature + 1 implicit)
- 是否发现新维度: 否
- **拓扑分类是否有进化建议**: 无，现有分类体系足够
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
