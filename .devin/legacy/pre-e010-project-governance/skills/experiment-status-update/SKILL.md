---
description: >
  实验后设计元素验证状态更新工作流。
  从实验run数据中识别受影响原语，更新验证状态、使用经验/架构位置、README统计。
  WHEN to use: 被 experiment-status-update rule 触发时。
  WHEN NOT to use: 新增设计元素、面相演化、定期审查（各有独立元组，部分待建）。
---

# experiment-status-update skill

## 这个skill做什么

一个实验run完成后，更新设计元素目录中受影响原语的验证状态。这是设计元素管理的高频操作——每次实验后都可能需要。

## 前置条件

- 一个实验run已完成，结果在 `runs/<run_id>/` 目录中
- 实验类型已知：guided run（有引导者决策）或 bare run（裸跑）

## 工作流

### 步骤1：识别受影响的原语

从run数据中提取信息：

**guided run**：
- 读 `runs/<run_id>/problem.txt` 了解题目
- 读 `runs/<run_id>/solutions.json` 或 `summary.json` 了解结果
- 读引导者决策（引导者发了什么Q，Q的形式是特定还是非特定）
- 识别测试了哪些原语：
  - 连续发问框架用了几层？→ continuous-questioning
  - 第一步是"描述形状"吗？→ safe-first-step
  - Q序列是特定还是非特定？→ non-specificity / implicit-filtering
  - 有回溯吗？→ backtrack-fresh-session / dfs-guidance
  - AI做了中心化/换基吗？→ base-change
  - AI用了SymPy验证吗？→ constraint-solver-engine（功能层面）
  - 引导改变了AI的路径吗？→ cognitive-activation

**bare run**：
- 读题目和结果
- 识别AI自发使用了哪些原语功能（不涉及引导类原语）

### 步骤2：判断每个受影响原语的验证状态变化

对照rule中的验证状态转换规则表：

- 这个实验是否**用了**这个原语？（用了→可能改变状态；没用→不影响）
- 用了之后**有效还是无效**？（有效→tested/保持；无效→tested_negative）
- 是否**证明了核心声称**？（证明→tested；只证明部分→partial）

**关键纪律**：
- 不要因为实验成功就把untested标成tested——要确认这个原语真的被使用了，且它的使用是成功的原因之一
- 243号修正的教训：确认实验题目的难度——如果AI裸跑就能做，引导类原语的"tested"要降级为"partial"
- 一个原语只在第一问（AI裸跑能做）上tested，不等于它在第二问（AI裸跑做不出）上tested

### 步骤3：更新原语文件

对每个验证状态有变化的原语：

1. 更新 `## 验证状态` section：
   - 改状态标签（如 `[untested]` → `[tested]`）
   - 更新具体说明（加一行：在什么实验中验证了什么）
   - 如果是重大修正（如243号），加"重大修正"子节

2. 更新 `## 使用经验`（操作原语）或 `## 架构位置`（结构原语）section：
   - 加一个子节记录这次实验中的使用情况
   - 格式：`### <run_id>中的表现` + 具体描述

### 步骤4：更新 README 统计

更新 `primitives/README.md` 中的：
- 验证状态分组索引（把原语移到新的分组）
- 验证状态分布统计表
- "一眼能看出的结论"（如果有显著变化）

### 步骤5：检查面相影响（可选）

如果实验结果改变了我们对系统的理解（不只是验证了一个原语，而是改变了面相理解）：
- 更新 `facets/` 中对应面相文件的"开放问题"或"局限"
- 这一步是可选的——大多数实验只验证原语，不改变面相

### 步骤6：commit

```bash
git add <受影响的文件路径>
git commit -m "<run_id>: 更新<原语名>验证状态 <旧状态>→<新状态>"
```

## 示例

### guided_003后的更新（历史案例）

guided_003用纯非特定Q序列成功，更新了3个原语：
- `non-specificity`: tested_negative → tested（纯非特定引导有效）
- `implicit-filtering`: tested_negative保持，但说明改为"非关键因素"（guided_003证明隐含筛选不是成功的必要条件）
- `cognitive-activation`: 保持tested（后243号降级为partial）

### 243号修正后的更新（历史案例）

243号发现guided_001/003的题目只有第一问，AI裸跑就能做：
- `cognitive-activation`: tested → partial（效应存在但未证明激活做不出来的能力）
- `continuous-questioning`: tested保持，但加注"未证明必要性——AI裸跑就能做第一问"
- `safe-first-step`: 同上

## 注意事项

1. **不要过度更新**——一次实验可能只影响1-3个原语，不是所有原语都要改
2. **保守标注**——如果不确定实验是否真的测试了某个原语，不要改它的状态
3. **记历史**——验证状态变化时，保留旧状态的说明（如"历史：曾经是tested_negative，guided_003后升级为tested"）
4. **commit粒度**——一次实验的更新可以一个commit，也可以按原语分多个commit（如果影响多个原语且变化复杂）
