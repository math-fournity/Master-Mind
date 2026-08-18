---
description: >
  元组群：guided-math-solving（引导式数学解题）。需要用最小知识传递引导AI做数学题时——
  即通过连续启发式提问（而非知识堆砌）引导做题AI完成解题。包含5个Skill的元组群。
  WHEN to use: 需要用最小知识传递引导AI做数学题时。
  WHEN NOT to use: 直接解题（非引导模式）、非数学题。
trigger: model_decision
---

# 元组群：guided-math-solving（引导式数学解题）

## 触发条件

需要用最小知识传递引导AI做数学题时——即通过连续启发式提问（而非知识堆砌）引导做题AI完成解题。

## 核心认知（always-on）

### 路线B：思维模式优先

提示干预走路线B（思维模式）而非路线A（知识堆砌）。寻找最深的、最通用的、最高抽象度的思维模式——跨知识范围的元认知策略，而非限于同一知识范围的具体定理/技巧。详细论证见 `dev-docs/214-v1-2026-08-06-提示策略路线选择与Level连续谱.md` 第1章。

### Level连续谱

依赖图中每个元素带Level标签（0到1实数）：→0纯知识（Vieta跳跃），→1纯思维模式（反证法），中间是灰色地带。Level是经验的、模糊的、相对的——不是被赋值的，而是被AI通过相对比较感知的。详见214号第2章。

### 最小知识传递

$$\arg\max_{H} \sum_{i=1}^{n} \text{Level}(h_i) \quad \text{s.t.} \quad \text{AI在} H \text{引导下完成解题}$$

在"AI能完成解题"的约束下，最大化所有提示的Level之和。每条提示尽可能用高Level（纯思维模式），避免低Level（具体知识）。详见214号第7章。

### DFS树结构

- **节点** = 做题AI的一个状态（一个A）
- **边** = 引导者发送的一个Q
- **根节点** = 题目本身
- **叶节点** = 成功叶（证毕）/ 死路叶（卡死）/ 截断叶（超限）
- **子边** = 引导者在该节点的所有候选Q

### 回溯铁律

**禁止在同一个Session中让AI回溯到思路岔口。** DFS路径失败后必须启动新Session。原因：压缩边界风险、context污染、context不可逆性。正确做法：新Session + 重放Q序列到岔口 + 在岔口换方向。详见214号8.9节。

### 节点同一性

路径同一性为主：node_id由Q路径决定（确定性），A内容是概率性的。Q相同但A有细微差异时，不判断同一性而判断适用性——"下一个Q对A'还有效吗？"有效则继续，无效则调整Q。详见214号8.10-8.12节。

## 与树生长引擎的关系

**guided-math-solving是串行单AI引导模式，树生长引擎是它的并行多AI演进版。**

| 维度 | guided-math-solving（串行） | 树生长引擎（并行） |
|---|---|---|
| AI数量 | 1个 | 最多2个并发 |
| 引导方式 | 在同一session中注入提示Q | 启动新AI+给脉络（从根到当前节点的路径+方向Q） |
| 树结构 | DFS树（单路径，失败则回溯） | 引导展开树（多路径并发分叉） |
| 回溯 | 启动新session重放Q序列 | 不需要回溯——每条路径独立探索 |
| 停机 | AI证毕 | 任一脉络到达正确解答 |

**复用的认知**：
- DFS树结构的节点/边/叶概念 → 引导展开树的节点/边/叶
- Level连续谱和最小知识传递 → 检索时选择高Level方向Q
- 节点同一性（Q路径决定） → path_from_root字段
- 回溯铁律（不在同一session回溯） → 树生长引擎天然遵守（每条路径是独立AI）

**演进路径**：guided-math-solving（阶段1串行）→ 脉络注入（阶段2串行多AI）→ 树生长引擎（阶段3并行多AI）→ 自我增殖（阶段4树→Pattern→树）

## 元组群目录（Skill有序列表）

**整体目标**：通过连续启发式提问，以最大Level SUM引导AI完成解题

**Skill目录**（按执行顺序）：

1. **Skill `guided-rehearsal`**：预演——给定题目，生成模拟QA序列和极致提示集合
   - 产出落盘到 `runs/<run_id>/rehearsal.md`
   - 完成后加载 Skill 2

2. **Skill `guided-session-launch`**：启动session——准备work_dir+problem.txt+tmux+devin+--export
   - 读取 rehearsal.md 确认题目
   - 产出：session_id, export_path, work_dir
   - 完成后加载 Skill 3

3. **Skill `guided-interaction`**：交互引导——连续发问框架执行（核心Skill）
   - 读取 rehearsal.md 获取候选提示
   - 产出：`runs/<run_id>/dfs_tree.json` 持续更新
   - 执行中遇到死路 → 加载 Skill 4 → 回溯后回到 Skill 3
   - 每轮交互后 → 调用 Skill 5 持久化
   - AI给出正确解答或确认无法推进 → 调用 Skill 5 做最终持久化

4. **Skill `guided-backtrack`**：回溯——新session+重放Q序列+在岔口换方向
   - 读取 dfs_tree.json 获取回溯点和Q序列
   - 产出：新session + dfs_tree.json更新
   - 完成后回到 Skill 3 继续引导

5. **Skill `guided-data-persist`**：数据持久化——记录到ArangoDB+文件系统归档
   - 读取 dfs_tree.json + export文件
   - 产出：ArangoDB完整记录 + 文件系统归档
   - 在 Skill 3 每轮交互后调用，也在实验结束时调用

**阶段间传递**：
- 1→2：rehearsal.md
- 2→3：session信息（session_id, export_path, work_dir）
- 3↔4：dfs_tree.json（当前树状态+回溯点）
- 3↔5：dfs_tree.json + export文件 → ArangoDB

**何时进入下一阶段**：前一个Skill完成并落盘后，AI检查本目录，自然加载下一个Skill。规则始终可见，即使Session压缩，AI仍能看到全貌。
