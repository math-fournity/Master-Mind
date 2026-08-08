# POC-VMS-1 验证报告：预演模式+Pattern生成

**编号**：271-v0
**日期**：2026-08-08
**状态**：✅ 通过
**关联**：257号（POC-VMS进度追踪）、269号（POC-VMS-0报告）、270号（POC-VMS-0扩展）、267号（未来系统面相）

---

## 1. 验证目标

验证从虚拟QA序列中提炼Pattern的可行性（缺口4：Pattern生成闭环）。

**267号面相注入后的定位调整**：预演模式从"运行时引导AI解题"调整为"离线数据生成"——为树生长引擎的数据基座生成初始Pattern。Pattern就是树生长引擎在节点上检索出的"方向Q"。

## 2. 验证步骤与结果

### 2.1 Trajectory分析 ✅

**数据源**：20道虚拟群论题的完整trajectory（10道4阶群+10道24/12阶群）

**Trajectory结构**：
- `exports/conversation.json`：10个step，含message/reasoning_content/tool_calls/observation
- `mitm/thinking_readable.txt`：token级thinking，按round分割，含AI内部推理
- `sessions_db/trajectory.jsonl`：DB监控的step级记录

**Thinking数据质量**：
- 20/20道题有thinking数据
- 每道题2-7个thinking round
- thinking内容包含AI的完整推理过程（元素阶计算、群结构识别、Lagrange定理应用等）

### 2.2 Pattern提炼 ✅

**提炼器**：`xishujuzhen/vms/pattern_extractor.py`

**提炼方法**：
1. 从thinking_readable.txt提取每个thinking round的内容
2. 用关键词匹配识别AI使用了哪些思维操作
3. 把思维操作抽象为Pattern（"在什么处境下应该往什么方向探索"）
4. 从题目元数据提取deterministic字段（task_type/group_order/group_type）
5. 从thinking内容提取non_deterministic字段（reasoning_state描述）

**提炼结果**：
- 68个Pattern实例（含重复）
- 去重后22个Pattern
- 8个基础Pattern类型

### 2.3 8个基础Pattern ✅

| 基础Pattern | Level | 非特定性 | 实例数 | AI使用过 | 在树生长引擎中的角色 |
|---|---|---|---|---|---|
| 元素阶计算 | 0.3 | 0.9 | 3 | 3 | 在节点上提示"计算每个元素的阶" |
| Lagrange定理应用 | 0.4 | 0.8 | 3 | 1 | 在节点上提示"用Lagrange定理约束子群阶" |
| 循环群识别 | 0.5 | 0.8 | 3 | 3 | 在节点上提示"寻找阶等于群阶的生成元" |
| 共轭类计算 | 0.6 | 0.7 | 3 | 3 | 在节点上提示"对每个元素计算所有共轭" |
| 中心计算 | 0.3 | 0.9 | 2 | 2 | 在节点上提示"检查每个元素是否与所有元素可交换" |
| 正规子群判定 | 0.5 | 0.7 | 3 | 3 | 在节点上提示"验证gHg⁻¹=H" |
| Python验证 | 0.1 | 0.5 | 2 | 2 | 在节点上提示"用Python暴力枚举验证" |
| 群结构识别 | 0.7 | 0.6 | 3 | 3 | 在节点上提示"通过元素阶分布识别同构类型" |

**Level分布**：0.1-0.7，覆盖从纯知识（Python验证0.1）到接近思维模式（群结构识别0.7）的范围。

**AI使用率**：8个基础Pattern中7个被AI实际使用过（只有Lagrange定理在24阶群上AI选择直接用Python暴力枚举而非Lagrange定理）。

### 2.4 Pattern结构完整性 ✅

**验证结果**：22/22 Pattern结构完整

每个Pattern包含：
- `pattern_id`：唯一标识
- `domain`：virtual_group_theory
- `trigger_conditions.deterministic`：task_type/group_order/group_type/has_multiplication_table
- `trigger_conditions.non_deterministic`：reasoning_state描述
- `Q`：方向提示（从此节点应往什么方向探索）
- `Level`：0-1之间的知识/思维模式定位
- `non_specificity`：0-1之间的非特定性
- `situation_type`：情境类型
- `source`：来源题号和thinking round

**deterministic/non_deterministic拆分** ✅：
- deterministic字段可被形式化方法查询（task_type/group_order/group_type）
- non_deterministic字段需要AI判断（reasoning_state描述AI当前的推理状态）

## 3. 通过条件检查

| 通过条件 | 状态 | 证据 |
|---|---|---|
| 预演QA序列成功引导AI解出虚拟题 | ✅ | 20/20题AI全部解出（269/270号报告） |
| 提炼的Pattern有完整的trigger_conditions/Q/Level/非特定性 | ✅ | 22/22 Pattern结构完整 |
| Pattern的trigger_conditions可以拆分为deterministic和non_deterministic字段 | ✅ | 所有Pattern都有deterministic（task_type/group_order等）和non_deterministic（reasoning_state） |

**POC-VMS-1 通过。**

## 4. 关键发现

### 4.1 Pattern提炼不需要"引导AI解题"

267号面相注入后的重要认知：预演模式不需要"让AI停下来接受提示"。AI自己就能解出来（20/20全对），Pattern的提炼来自AI的**自然推理过程**，不是来自"系统提示后AI的反应"。

这意味着Pattern生成可以**完全自动化**——让AI解题，记录trajectory，从trajectory中提炼Pattern。不需要人工引导。

### 4.2 Thinking数据是Pattern提炼的核心

Pattern的提炼质量直接取决于thinking数据的质量。MITM拦截的token级thinking包含了AI的完整推理过程，是Pattern提炼的核心数据源。

没有thinking数据，Pattern提炼只能靠AI的最终输出（message），会丢失大量中间推理步骤。

### 4.3 8个基础Pattern覆盖了虚拟群论的核心思维操作

8个基础Pattern覆盖了虚拟群论解题的核心思维链：
1. 元素阶计算（基础操作）
2. Lagrange定理应用（定理应用）
3. 群结构识别（模式识别）
4. 循环群识别（概念判定）
5. 共轭类计算（计算方法）
6. 中心计算（概念应用）
7. 正规子群判定（概念判定）
8. Python验证（工具使用）

这8个Pattern构成了虚拟群论的"思维操作库"，对应树生长引擎中数据基座的初始内容。

### 4.4 AI使用率验证了Pattern的有效性

8个基础Pattern中7个被AI实际使用过（87.5%），说明这些Pattern不是人为编造的，而是AI真实推理过程中使用的思维操作。这验证了Pattern提炼方法的有效性。

唯一没有被AI在所有题中使用的Pattern是Lagrange定理应用——在24阶群上AI选择直接用Python暴力枚举而非Lagrange定理。这本身是一个有价值的Pattern：**当群阶较大时，AI倾向于用计算工具而非定理推理**。

### 4.5 Pattern的Level分布合理

8个基础Pattern的Level从0.1（Python验证，纯工具使用）到0.7（群结构识别，接近思维模式），覆盖了知识-思维模式连续谱的完整范围。这说明虚拟群论的Pattern不是单一层次的，而是包含了从具体操作到抽象模式识别的完整层次。

## 5. 对树生长引擎的意义

这22个Pattern是树生长引擎数据基座的**初始种子**。在树生长引擎中：

1. **节点上的检索**：当推理AI在某个节点上卡住时，系统检索数据基座中的Pattern。例如，当AI在"找子群"的节点上卡住时，检索到`VG-lagrange-theorem-application`，提示"用Lagrange定理约束子群阶"。

2. **方向Q驱动分叉**：每个Pattern的Q字段就是树生长引擎中的"方向Q"——从此节点应往什么方向探索。多个Pattern可以同时被检索到，驱动树的不同分叉。

3. **deterministic字段做粗筛**：形式化方法用task_type/group_order等deterministic字段做粗筛，缩小候选Pattern集。

4. **non_deterministic字段做精筛**：AI用reasoning_state等non_deterministic字段做精筛，从候选Pattern中选出最相关的。

## 6. 下一步

### POC-VMS-2：小规模检索验证（10个Pattern）

用POC-VMS-1生成的22个Pattern构建小规模虚拟数据基座，让AI解新的虚拟题（不在预演集中的题），测试：
1. 形式化方法能否从context中提取出结构化状态
2. 形式化粗筛能否缩小候选集
3. AI精筛能否从候选集中找到正确Pattern
4. 检索到的Pattern能否引导AI解出新虚拟题

## 7. 产出资产

| 资产 | 路径 | 说明 |
|---|---|---|
| Pattern提炼器 | `xishujuzhen/vms/pattern_extractor.py` | 从trajectory自动提炼Pattern |
| Pattern数据 | `runs/vms_poc_0/patterns.json` | 22个Pattern实例 |
| 基础Pattern | `runs/vms_poc_0/base_patterns.json` | 8个基础Pattern模板 |
