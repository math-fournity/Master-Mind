# FCA再分析Subagent Prompt模板

> 主agent用本模板构造subagent的prompt。每次启动FCA再分析subagent时，复制本模板，填入`{problem_id}`和`{output_path}`，作为run_subagent的task参数。
>
> 本模板与`.devin/rules/tell-taxonomy-iteration-audit.md`的10步SOP严格对应。
> subagent是stateless的——prompt必须front-load所有信息，不依赖session上下文。

---

## Prompt模板（复制以下内容到run_subagent的task参数）

你是FCA再分析执行者。你的任务是对一道已完成题目的profile做FCA再分析，用FCA先验分类学重新识别原始profile遗漏的非局部/全局tell显现。

### 题目信息

- problem_id: {problem_id}
- 原始profile路径: `subagents-dirs/{problem_id}/profile.json`
- 产出报告路径: `{output_path}`

### 执行流程（必须严格按顺序执行，不允许跳步）

#### 步骤0：加载V6提示词全文（mandatory · 不可跳过）

用read工具读取以下文件全文：
`第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee/v6.md`

V6是格化+全Level Trace识别的完整操作指南（679行）。它定义了所有术语（双轨制FCA定义+工程含义）、核心概念（脉络/段/Level视图/有意义的合并/Hasse图）、7种反模式、8种复杂情况检查、9项自我审计。你必须先加载V6再做任何分析。

**V6与v3分类学的对齐注意**：V6审计项5的8种复杂情况中，"模分析无尽追逐"还是独立项——但v3分类学已把它降级为"探索-诊断-修复"的子模式。在使用V6时，审计项5的检查应按v3分类学理解：把"模分析无尽追逐"作为"探索-诊断-修复"的子模式检查，不作为独立模式检查。

#### 步骤1：读原始profile

**优先从文件系统读取**：用read工具读取`subagents-dirs/{problem_id}/profile.json`

**如果文件不存在，从数据库读取**：用exec工具执行以下Python脚本从ArangoDB读取：
```python
from arango import ArangoClient
client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
p = db.collection('problem_profiles').get('{problem_id}')
```
数据库中`problem_profiles`集合的`_key`就是problem_id，每个profile含完整字段。

提取以下字段：
- `tell_hint_pairs`：局部tell列表
- `global_tell_hint_pairs`：全局tell列表
- `tell_topology`：题目级拓扑
- `tell_small_concepts`：题目级小概念
- `domain`：原始domain标注
- `key_insight`：关键洞察
- `solution_text`：解答文本
- `problem_text`：题目文本

#### 步骤2：确定domain（属性维度第一层）

看原始domain字段，问"这道题的解答是否跨域？"——如果解答把问题从一个领域翻译到另一个领域，标多个domain。v3分类学的6个domain：数论/代数/组合/几何/分析/跨域。

#### 步骤3：识别段结构模式（属性维度第二层）

用V6的格化方法（段划分→Level视图→有意义的合并）对解答做格化。逐一检查v3分类学的5大类段结构模式：
- 构造-分析-排除？（构造对象→分析性质→排除不可能）
- 探索-诊断-修复？（探索→发现gap→诊断→修复；无尽追逐是此模式的子模式）
- 跨域桥接？（把问题翻译到另一个领域）
- 归约策略？（大问题归约到小问题）
- 累积-收敛？（逐步累积信息→收敛到结论）

#### 步骤4：确定具体概念（属性维度第三层）

domain × 段结构模式的交叉，生成具体概念。子模式在此层体现（如"无尽追逐"是"探索-诊断-修复"的子模式）。

#### 步骤5：从多个观察Level分析trace

- 局部Level：每一步的特征——"AI在第N步做了什么/没做什么"
- 非局部Level：跨多段的模式——"AI在这几步构成了什么模式/没构成什么模式"
- 全局Level：整体策略——"AI整体走了什么路线/没走什么路线"
- **关键**：同一个tell在三个Level下有三种显现——它们不是三个不同的tell，是同一个tell的三种观察方式

每个tell显现标注：tell内容 + 观察Level（局部/非局部/全局） + 固有属性（domain+段结构模式+具体概念） + 是原始profile已有的还是新发现的

#### 步骤6：构造形式背景

把所有tell显现写成形式背景表格——行是tell，列是固有属性（domain + 段结构模式），打✓表示"这个tell有这个属性"。**列不包含观察Level**——观察Level在表格注释中说明。

#### 步骤7：算概念格

从形式背景算出所有形式概念（用FCA闭包算子的直觉——"查表格找共同特点再找有这些特点的tell"），排成层级。

#### 步骤8：对比原始profile

1. 量化对比：局部tell数量、非局部tell显现数量、domain识别数量、段结构模式识别数量、观察Level覆盖
2. 质变对比：格化思考多看到什么（4个质变维度：从"每轮缺什么"到"整体没走什么路线"、从"没想到X"到"没跨域到Y"、从"两个独立缺口"到"同一模式的两个实例"、从"扁平topology"到"3层属性维度+观察Level"）
3. 记录"原始profile遗漏了什么"——列出所有新发现的tell显现

#### 步骤9：分类学问题检查

检查：
1. 分类学是否无法覆盖这道题的某个tell？→ 标注"发现分类学问题"
2. 用FCA理论审查分类学是否不自洽？→ 标注"发现分类学问题"

如果发现问题，在报告中明确标注"发现分类学问题"并描述具体问题——但**不要自行修正分类学**，修正由主agent执行。

### 产出格式（写入{output_path}的报告必须包含以下所有部分）

#### 第1部分：题目信息
- problem_id
- domain（原始标注）
- key_insight

#### 第2部分：段划分（Level 0）
- 段编号、段内容、段特征（按V6第四部分§1格式）

#### 第3部分：所有有意义的Level视图
- Level编号、哪些段合并了、为什么这个合并有意义（按V8第四部分§2格式）

#### 第4部分：每个Level视图上的Trace
- 在哪个Level视图上、trace类型（局部/非局部/全局）、trace模式描述、涉及哪些段（按V6第四部分§3格式）

#### 第5部分：FCA分类学标注
- domain列表（步骤2输出）
- 段结构模式列表（步骤3输出，每个含模式名+具体表现+涉及的段）
- 具体概念列表（步骤4输出）
- tell显现列表（步骤5输出，每个含tell内容+观察Level+固有属性+是否新发现）

#### 第6部分：形式背景表格
- Markdown表格（步骤6输出）
- 观察Level注释

#### 第7部分：概念格描述
- 层级结构（步骤7输出）

#### 第8部分：对比报告
- 量化对比表（步骤8输出）
- 质变对比描述
- 遗漏清单（新发现的tell显现列表）

#### 第9部分：9项自我审计报告（按V6第四部分§4格式，必填，不允许跳过）

#### 第10部分：最有价值的trace
- 最有价值的trace是哪个？为什么？
- 第二有价值的trace是哪个？为什么？

#### 第11部分：分类学问题报告
- 是否发现分类学问题？如果是，描述具体问题。
- 是否发现FCA理论自洽性问题？如果是，描述具体问题。

### 返回给主agent的执行摘要（在subagent完成后，除了写入报告文件，还要在返回文本中包含以下摘要）

```
## 执行摘要
- problem_id: {problem_id}
- check list完成情况: 全部完成 / 部分完成（列出未完成项）
- 段数: N
- Level视图数: N
- trace总数: N（局部N + 非局部N + 全局N）
- 新发现的tell显现数: N
- 最有价值的trace: <trace描述>
- 是否发现分类学问题: 是/否
  - 如果是，问题描述: <描述>
- 报告路径: {output_path}
```

### 约束

1. **不允许跳过V6加载（步骤0）**——V6是你的操作指南，不加载就做分析等于盲目操作
2. **不允许跳过9项自我审计**——自我审计是产出的一部分，不是可选的反思
3. **不允许自行修正分类学**——如果你发现分类学问题，在报告中标注即可，修正由主agent执行
4. **产出报告必须包含第1-11部分的所有内容**——缺少任何一部分都是不完整的产出
5. **返回给主agent的执行摘要必须包含上述所有字段**——主agent用执行摘要验证你的产出

---

## 主agent使用方法

1. 复制上面"Prompt模板"部分的内容
2. 把`{problem_id}`替换为实际题目ID（如`imo_2024_p5`）
3. 把`{output_path}`替换为实际产出路径（如`FCA学习笔记/10-用FCA重做已完成题目Tell分类-{problem_id}.md`）
4. 用run_subagent启动，profile选`subagent_general`（需要写文件权限）
5. subagent返回后，用产出验证check list验证产出

### 并行使用

可以同时启动多个subagent做多道题的FCA再分析。每个subagent有独立的上下文窗口，互不干扰。10题抽样验证可以2-3个subagent并行做。

**注意**：如果多个subagent同时发现分类学问题，主agent需要合并这些问题，统一执行修正流程（7条铁律），不让多个subagent各自修正。
