# 任务追踪 · 端到端效果验证-接真实Solver

> **本文件是跨Session的工作追踪文档。新Session的AI进入本工作线后，先读本文件，了解"之前做了什么、现在在做什么、接下来该做什么"。**
>
> **维护规则**：每完成一个工作单元，立即更新对应条目的状态。新增任务时追加到末尾。不删除历史条目——它们是工作积累的记录。

---

## 0. 当前工作焦点

**主线**：接真实Solver跑端到端效果验证——验证"检索机制选出提示后，AI是否真的能突破卡点"。

**当前状态**：实时管线（§2.3-2.5）实现完成，mock测试通过——253号A7→Q8与离线test_e2e_253结果一致。下一步是§2.6端到端效果验证A/B对照实验（需用solver-harness启动真实Solver）。

**下一步**：用solver-harness启动真实Solver跑253号案例，连接RealtimePipeline到真实sessions.db，验证实时解析+检索+注入的完整流程。

---

## 1. 已完成的工作

### 1.1 端到端效果验证方案设计

**为什么做**：01工作线验证了"检索机制能选出正确的Q"（253号A7→Q8），但这只是"选出了正确提示"，没有验证"选出提示后AI是否真的突破卡点"。从"原型验证"到"效果验证"是性质不同的阶段——原型验证用的是已生成的QA记录（离线），效果验证需要实时解析+实时检索+实时提示注入（在线）。不验证效果，检索机制可能只是"理论上正确"但实际无效。

- [x] 分析效果验证的复杂度——涉及多模块实时集成
- [x] 确定本工作线是01工作线和02工作线的交汇点
- [x] 创建本任务追踪文档

### 1.2 实时解析管线实现（§2.3-2.5）

**为什么做**：01工作线的parser是离线的——解析预先生成的A_i文本。效果验证需要在线实时解析——Solver每输出一段，立即解析为ParseResult，检索Pattern，选择提示，注入到Solver。不搭建实时管线，检索机制无法接入实时Solver。

**实现的模块**（`xishujuzhen/research_runtime/realtime/`）：
- `trajectory_watcher.py`：监控sessions.db，从Devin CLI trajectory提取Round（一个Round = Solver一轮完整输出，对应离线的A_i）
- `stall_detector.py`：卡点检测（语义检测"我不知道"等关键词 + 超时检测N秒无新节点）
- `pipeline.py`：RealtimePipeline整合watcher + stall_detector + MathParser + RetrievalPipeline + ConstrainedPolicy
- `hint_injector.py`：通过tmux send-keys注入提示到Solver session
- `test_realtime.py`：mock测试——用253号A7数据验证完整流程

**测试结果**：
- StallDetector：语义检测✅（匹配"我不知道"）、超时检测✅
- RealtimePipeline：解析✅（4事件4节点）、六元组✅（V_t=6/F_t=2/O_t=7/U_t=1）、检索✅（5条匹配规则）、策略选择✅（选中Q8）
- HintInjector：dry-run✅（不存在的session正确返回False）
- TrajectoryWatcher：mock Round构建✅
- **关键验证**：选中Q8与离线test_e2e_253结果一致——实时管线正确复现了离线检索流程

---

## 2. 待办清单（按优先级排序）

### P0-前置条件（必须先完成） ✅

#### 2.1 等待01工作线P1原语升级tested ✅

**为什么做**：本工作线要用完整的检索机制（P0+P1全部模块），如果P1原语还是partial（只在253号单一案例上验证），在新案例上跑可能出问题。先在01工作线完成P1升级tested，确保检索机制本身可靠。

- [x] 01工作线P1原语升级tested完成（tested 35/72，8个P1原语在数论和组合2个新案例上全部通过）

#### 2.2 等待02工作线solver-harness实施完成 ✅

**为什么做**：本工作线需要实时采集Solver的trajectory（thinking+tool_calls+results），这是02工作线solver-harness的核心能力。没有solver-harness，无法实时获取Solver的推理过程，也就无法实时解析和检索。

- [x] 02工作线solver-harness v1实施完成（全局共享mitmproxy + 事后批量解码 + 端到端测试通过）
- [x] 所有场景统一用solver-harness（rule+skill+AGENTS.md硬约束已写入）

### P1-核心实施

#### 2.3 实时解析管线搭建 ✅

**为什么做**：01工作线的parser模块是离线的——解析预先生成的A_i文本。效果验证需要在线实时解析——Solver每输出一段，立即解析为语义事件+T_t节点+六元组。不搭建实时管线，检索机制无法接入实时Solver。

- [x] 设计实时解析管线架构（TrajectoryWatcher监控sessions.db → 提取Round → MathParser解析）
- [x] 实现trajectory数据到ParseRequest的适配器（`_nodes_to_agent_output`：thinking+content+tool_calls → agent_output文本）
- [x] mock测试通过（253号A7解析出4事件4节点，六元组V_t=6/F_t=2/O_t=7/U_t=1）
- [x] 验证实时解析结果与离线解析结果一致（mock数据下一致）

#### 2.4 实时检索管线搭建 ✅

**为什么做**：01工作线的retrieval-pipeline是离线的——对单个ParseResult跑一次检索。效果验证需要在线实时检索——每解析出一个新的ParseResult，立即检索Pattern并选择提示。不搭建实时检索，无法在Solver卡住时及时给出提示。

- [x] 设计实时检索管线架构（ParseResult → RetrievalPipeline → ConstrainedPolicy → 提示选择）
- [x] 实现卡点检测的实时触发（StallDetector：语义检测"我不知道"等关键词 + 超时检测）
- [x] mock测试通过（检索5条匹配规则，策略选中Q8）
- [x] 验证实时检索结果与离线检索结果一致（选中Q8与test_e2e_253一致）

#### 2.5 提示注入机制 ✅

**为什么做**：01工作线验证了"constrained-policy选中Q8"，但没有实际发送Q8给Solver。效果验证需要实时提示注入——选出的提示要实际发送到Solver的session中，影响Solver的后续推理。不验证提示注入，不知道提示是否能被Solver正确接收和利用。

- [x] 设计提示注入机制（HintInjector：通过tmux send-keys注入到Solver session）
- [x] 实现提示注入的时序控制（wait_idle等待pane空闲 + 逐行send-keys + Enter提交）
- [x] dry-run测试通过（不存在的session正确返回False）
- [ ] 验证提示注入后Solver的trajectory中能看到提示（需真实Solver实验）

#### 2.6 端到端效果验证实验

**为什么做**：这是本工作线的核心目标——验证"检索机制选出提示后，AI是否真的能突破卡点"。不跑这个实验，整个检索机制的价值未经验证。

- [ ] 选择实验题目（从01工作线的3个案例中选，或选新题）
- [ ] 设计A/B对照实验：
  - A组：有检索系统（实时解析+实时检索+提示注入）
  - B组：无检索系统（Solver裸跑，无提示）
- [ ] 跑A组实验（有检索系统），记录Solver的trajectory和最终结果
- [ ] 跑B组实验（无检索系统），记录Solver的trajectory和最终结果
- [ ] 对比A/B组：
  - 成功率：A组是否比B组更高？
  - 突破卡点：A组在收到提示后是否真的突破了卡点？
  - 效率：A组是否比B组更快完成？
  - 提示质量：选出的提示是否真的帮助了AI（而非替AI做题）？

### P2-后续深化

#### 2.7 多案例效果验证

**为什么做**：单一案例的效果验证可能偶然性高。多个案例的效果验证才能确认检索机制的普遍有效性。

- [ ] 在3-5个不同领域的案例上跑A/B对照
- [ ] 统计整体成功率和突破率
- [ ] 分析失败案例——是检索选错了提示，还是提示本身无效？

#### 2.8 controlled-experiment框架化

**为什么做**：手动跑A/B对照效率低，且不可复现。框架化后可以自动跑多个案例的对照实验。

- [ ] 基于checkpoint模块实现实验快照和复现
- [ ] 实现A/B对照的自动化脚本
- [ ] 生成实验报告（成功率/突破率/效率/提示质量）

---

## 3. 关键决策记录

### 3.1 为什么需要独立的工作线

01工作线（253号检索机制验证）验证的是"检索机制能选出正确的Q"——离线、单次、用预生成数据。
本工作线验证的是"选出Q后AI是否真的突破"——在线、实时、用真实Solver。

两者性质不同：
- 01是"组件验证"——各模块是否能独立工作
- 本工作线是"系统集成验证"——各模块串起来能否在真实环境中工作

且本工作线依赖02工作线（solver-harness）的trajectory采集能力，是01和02的交汇点，不属于任何一个的简单延续。

### 3.2 为什么用A/B对照而非单组实验

单组实验（只跑有检索系统的A组）无法排除"AI本来就能做出来"的假设。A/B对照通过比较"有检索系统"和"无检索系统"的差异，才能证明检索机制的价值。

### 3.3 为什么提示质量是关键指标

如果选出的提示是"直接告诉答案"，即使A组成功率更高，也不能说明检索机制有效——那只是替AI做题。提示质量指标验证的是"提示是否引导AI自己思考"而非"提示是否替AI思考"。这是燧人代"不给火而教取火"理念的核心。

---

## 4. Git Commit历史

| Commit | 描述 | 产出资产（完整路径） |
|---|---|---|
| b5bbae3 | 04工作线§2.3-2.5：实时解析+检索+注入管线实现，mock测试通过（7文件） | **代码**: `xishujuzhen/research_runtime/realtime/__init__.py`, `xishujuzhen/research_runtime/realtime/trajectory_watcher.py`, `xishujuzhen/research_runtime/realtime/stall_detector.py`, `xishujuzhen/research_runtime/realtime/pipeline.py`, `xishujuzhen/research_runtime/realtime/hint_injector.py`, `xishujuzhen/research_runtime/realtime/test_realtime.py` **任务追踪**: `任务追踪/04-端到端效果验证-接真实Solver.md` |

---

## 5. 跨Session读取指南

**新Session的AI进入本工作线后**：

1. **先读本文件**——了解当前工作焦点和待办清单
2. **读`任务追踪/README.md`**——了解本工作线与01/02/03工作线的依赖关系
3. **读01工作线（`任务追踪/01-253号检索机制验证.md`）**——了解检索机制原型的验证状态
4. **读02工作线（`任务追踪/02-trajectory采集与solver-harness.md`）**——了解solver-harness的实施状态
5. **读dev-docs/258号**——了解检索机制设计（含实现状态回填）
6. **检查前置条件**——01工作线P1是否升级tested？02工作线solver-harness是否实施完成？
7. **如果前置条件未满足**——先去推进前置工作线
8. **如果前置条件已满足**——从§2.3开始实施

**工作完成后**：
- 更新本文件的对应条目状态
- 更新`任务追踪/README.md`中本工作线的状态
- 更新AGENTS.md任务追踪登记表的焦点列
- commit
