# 脉络分析模块设计说明书

**模块**：`system/vein_analysis.py`
**架构**：三阶段架构（格化→程序枚举→综合分析）
**定义来源**：333号文档（脉络分析Pipe内细化方案）

---

## 1. 概述

脉络分析是AI数学系统的Parser AI核心功能——分析一道数学题的解答，提取"脉络"（解题路径上所有思维步骤的序列），切成最细的"段"，标注段的思维特征，构造形式上下文(G,M,I)，枚举闭元素，识别trace（有数学思维价值的模式）。

**三阶段架构**将原来一个AI session完成的完整流程拆成三个阶段：

| 阶段 | 做什么 | 谁做 | 产出 |
|---|---|---|---|
| 阶段1 格化 | 段划分+特征标注+形式上下文构造 | 4个devin cli并发（V5/V7/V8/V10） | segments.json + formal_context.json |
| 阶段1.5 程序枚举 | 闭元素枚举 | 程序自动（verify_lattice_completeness.py） | closed_elements.json |
| 阶段2 综合分析 | trace识别+审计+元反思 | 1个devin cli | output.json + output.md |

**为什么要拆**：格化和trace识别是不同的认知工作——格化是"把解答分段并标注特征"，trace识别是"从段和闭元素中识别有数学思维价值的模式"。拆分后格化可以4版本并发（不同提示词视角），程序枚举闭元素（确定性运算），综合分析做程序做不了的语义判断。

---

## 2. 入口函数

```python
def vein_analysis_three_phase(input: AnalysisInput) -> AnalysisOutput:
```

**调用方式**：`system/run_imo2009p6_three_phase.py`

**流程**：
1. 创建工作目录 `palyground/absorb/vein_analysis/{run_id:04d}_{problem_id}/`
2. 调用`_phase1_grading()` → 4并发格化
3. 调用`_phase1_5_enumerate()` → 程序枚举闭元素
4. 调用`_phase2_synthesis()` → 综合分析
5. 返回`AnalysisOutput`

---

## 3. 阶段1：格化（`_phase1_grading`）

### 3.1 4个版本

| 版本 | 提示词 | AGENTS模板 | 特色 | 产出 |
|---|---|---|---|---|
| V5 | v5_grading.md | AGENTS_V5.md | 自由直觉段划分 | segments.json |
| V7 | v7_grading.md | AGENTS_V7.md | 结构化约束（FCA+Hasse图） | segments.json + formal_context.json |
| V8 | v8_grading.md | AGENTS_V8.md | 跨闭元素元模式引导+文件拆分流程控制 | segments.json + formal_context.json |
| V10 | v10_grading.md | AGENTS_V10.md | 显式元模式编码+key_entities | segments.json + formal_context.json + key_entities.json |

### 3.2 V8的文件拆分流程控制（335号方案D）

V8使用2步文件拆分流程控制，控制thinking大小：

- **step1**：完整格化（段划分+所有特征标注）→ segments.json
  - 段划分和特征标注是同一个认知过程——不禁止标注特征
- **step2**：矩阵构造（从segments.json提取特征构造I矩阵）→ formal_context.json
  - 只做机械的矩阵构造——不做验证

**退化教训**：4步方案曾导致退化（step1禁止标注特征→改变了认知内容→段数21 vs 32）。2步方案不退化（闭元素48=48）。

**设计原则**：不改变认知内容，只改变执行顺序。

### 3.3 并发执行

4个版本并发启动（4个tmux session），轮询DONE.md检测完成。V8有900秒超时降级——超时后用V5/V7/V10继续。

### 3.4 AGENTS模板

所有版本的AGENTS模板都已更新为三阶段架构格化阶段模板：
- "只做段划分和形式上下文构造"
- "不做trace识别——trace识别由后续的综合分析阶段完成"
- "不做验证——矩阵验证由程序完成"

---

## 4. 阶段1.5：程序枚举闭元素（`_phase1_5_enumerate`）

### 4.1 程序自动完成

用`system/verify_lattice_completeness.py`的Next Closure算法枚举所有满足A''=A的子集A。

**输入**：各版本的formal_context.json（G,M,I）
**输出**：各版本的closed_elements.json

**V5不参与**——V5是自由直觉段划分，不要求形式上下文。

### 4.2 完备性保证

程序枚举是给定(G,M,I)的确定性运算——给定形式上下文，Next Closure算法枚举所有闭元素，一个不漏。这个运算是完备的。

**但(G,M,I)本身可能不完美**——阶段1的AI在做段划分和特征标注时可能遗漏。形式上下文回溯检查在阶段2的综合分析中完成。

---

## 5. 阶段2：综合分析（`_phase2_synthesis`）

### 5.1 文件拆分流程控制（336号方案）

综合分析使用4阶段文件拆分流程控制：

| 阶段 | 做什么 | 输入 | 输出 |
|---|---|---|---|
| 阶段1 | 对比4版本格化+回溯检查 | grading/ + closed_elements/ | comparison.json |
| 阶段2 | 闭元素解读+跨闭元素元模式 | closed_elements/ + comparison.json | closed_element_traces.json |
| 阶段3 | nonlocal+ccm+global trace | input.md + comparison.json | content_based_traces.json |
| 阶段4 | 审计+合并+AI优势+关键实体+元反思 | 前3个json | output.json + output.md |

### 5.2 为什么4阶段拆分不退化

**和V8的关键区别**：
- V8退化根因：段划分和特征标注是"同一个认知过程"——拆分后step1禁止标注特征→改变了认知内容→退化
- 综合分析不退化：6步之间是"不同的认知工作"——nonlocal trace识别"不依赖闭元素"，闭元素解读"依赖闭元素"，它们本来就是不同的认知过程，拆分不改变认知内容

**验证结果**：不仅没有退化，还大幅提升——trace从43提升到88，AI优势从7提升到20。原因是4阶段拆分让每个阶段的thinking更专注，每步更细致→更多trace。

### 5.3 5类trace

| 类型 | 来源 | 说明 |
|---|---|---|
| local | 闭元素语义解读 | 几个段共享某特征构成的闭元素 |
| nonlocal | 段内容分析 | 跨多个段的思维模式，不依赖闭元素 |
| global | 全证明视角 | 贯穿全证明的结构骨架（如强归纳框架、核心变量贯穿） |
| cross_case_merge | 跨Case对比 | 跨Case的非相邻段合并——本质相同但在不同Case中 |
| cross_element_meta_pattern | 跨闭元素 | 变量/技巧贯穿多个闭元素的统一角色 |

**不同类型不合并**——它们是5个不同的抽象视角，同一个模式从不同视角看会得到不同类型的trace，各自有泛化价值。

### 5.4 AI优势元素

程序做不了的语义判断——如"aₙ作为跳过障碍的工具"（程序看到特征共现，看不到功能统一性）、"预防性避障vs修复性避障"（程序看到相同特征，看不到策略差异）。

---

## 6. 数据流

```
input.md（题目+解答）
    ↓
阶段1 格化（4并发）
    V5 → segments.json
    V7 → segments.json + formal_context.json
    V8 → segments.json + formal_context.json（2步文件拆分）
    V10 → segments.json + formal_context.json + key_entities.json
    ↓
阶段1.5 程序枚举
    V7 formal_context.json → V7_closed_elements.json
    V8 formal_context.json → V8_closed_elements.json
    V10 formal_context.json → V10_closed_elements.json
    ↓
阶段2 综合分析（4阶段文件拆分）
    grading/ + closed_elements/ → comparison.json
    closed_elements/ + comparison.json → closed_element_traces.json
    input.md + comparison.json → content_based_traces.json
    前3个json → output.json + output.md
```

---

## 7. 关键常量

```python
PROMPT_DIR = "prompts/absorb/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee"
PROMPT_VERSIONS = ["V5", "V7", "V8", "V10"]
GRADING_PROMPT_FILES = {v: f"{PROMPT_DIR}/v{v.lower()}_grading.md"}
SYNTHESIS_PROMPT_FILE = f"{PROMPT_DIR}/synthesis.md"
AGENTS_TEMPLATES = {v: f"assets/vein_analysis/AGENTS_{v}.md"}
SYNTHESIS_AGENTS_TEMPLATE = "assets/vein_analysis/AGENTS_synthesis.md"
VERIFY_SCRIPT = "system/verify_lattice_completeness.py"
```

---

## 8. 审计

**审计脚本**：`system/tests/vein_analysis/run_audit.py`
**审计维度**：trace数量、trace类型分布、闭元素数量、AI优势数量、元反思数量
**退化判定**：trace数量<80%或trace类型<70%为退化
**历史运行**：0004-0013（见`system/docs/references.md` §8 脉络分析审计）

---

## 9. 研发文档索引

| 文档 | 内容 |
|---|---|
| 333号 | 脉络分析Pipe内细化方案——格化与trace识别分离（三阶段架构定义） |
| 334号 | 脉络分析新管线审计结果与改进方案——nonlocal trace退化修复 |
| 335号 | V8格化thinking过大问题分析——方案D 2步文件拆分（不退化） |
| 336号 | 综合分析4阶段文件拆分——不会退化且大幅提升（trace 43→88） |

**代码映射**：见`system/docs/references.md`中的§6三阶段架构、§7文件拆分流程控制、§8脉络分析审计
