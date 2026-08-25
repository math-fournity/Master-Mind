---
name: guided-interaction
description: >
  引导式数学解题元组群·Skill 3：交互引导（核心Skill）。
  连续发问框架执行，从L1观察到L5推进，包括提示注入。
  WHEN to use: 元组群guided-math-solving的第三步，session启动后开始引导做题AI时。
  WHEN NOT to use: 非引导模式、session未启动、预演未完成。
---

# guided-interaction skill

## 用途

元组群 `guided-math-solving` 的 Skill 3（核心）。在session启动后，通过连续发问框架引导做题AI从观察走向解题。

## 前置条件

- Skill 1 `guided-rehearsal` 已完成，`runs/<run_id>/rehearsal.md` 可读
- Skill 2 `guided-session-launch` 已完成，session已启动
- `runs/<run_id>/dfs_tree.json` 已初始化

## 连续发问框架（六层）

### L1：观察（必然安全）

发送：
> "请读取当前目录下的problem.txt文件。不要解题。请描述这道题的结构形状：结论是什么类型？已知条件是什么类型？条件和结论之间的距离有多远？"

AI必然可以回答——只要求读题并分类，不要求解题。

记录到dfs_tree：创建根节点，Q_level=1.0，q_category="元认知指令"

### L2：联想（几乎安全）

发送：
> "这些条件让你想到了什么方向？不要求正确，不要求完整，只要列出你脑中浮现的任何方向。"

AI必然可以回答——只要求列举方向，不要求方向正确。

记录到dfs_tree：添加子节点，Q_level=1.0，q_category="元认知指令"

### L3：描述方向（仍然安全）

发送：
> "对每个方向，如果走这个方向，第一步会做什么？不要求真的做，只描述。"

AI必然可以回答——只要求描述，不要求执行。

记录到dfs_tree：添加子节点，Q_level=1.0，q_category="元认知指令"

### L4：小尝试（可控风险）

发送：
> "选你觉得最有希望的方向，试着做第一步。做多少算多少，做不出来也没关系。"

AI可能开始有产出，也可能卡住。

- 有产出 → 进入L5
- 卡住 → 给提示（从rehearsal.md的极致提示集合中选Level最高的匹配提示）

记录到dfs_tree：添加子节点，Q_level=1.0，q_category="元认知指令"

### L5：推进 + 提示注入循环

**如果AI推进了**：
> "你得到了什么？这个结果和你要证明的结论之间还有什么差距？下一步你想怎么走？"

**如果AI卡住了**——从rehearsal.md的极致提示集合中选择匹配的提示注入：
1. 读rehearsal.md，找到和当前卡点形状匹配的提示
2. 按Level降序选择——先给Level最高的提示
3. 发送提示
4. 等待AI回复
5. 如果AI推进了→继续L5；如果AI仍卡住→给Level次高的提示
6. 如果所有高Level提示都失败→降Level走向知识端（记录降Level原因）

**提示注入的Level评估**：
- Level≈0.9：反证法、归一化（纯思维模式）
- Level≈0.85：寻找统一编码、结构对应、极值构型探测
- Level≈0.7-0.8：恒等式挖掘、投影分解、扰动分析
- Level≈0.5-0.6：量级感知、能量传递（开始暗示具体知识方向）
- Level<0.3：具体知识（"用q(x)=x²+x-1"、"用badly approximable"）——最后手段

循环直到AI完成证明或确认无法推进。

### L6：卡点处理（如果卡住）

发送：
> "你卡在哪里了？是不知道下一步该做什么，还是知道方向但做不下去？如果是前者，我们换个方向；如果是后者，你缺的是什么——是一个具体技巧，还是一个思路？"

根据AI回答：
- "不知道下一步" → 回到L3换方向，或加载Skill 4回溯
- "知道方向但做不下去" → 判断缺的是技巧（降Level给知识）还是思路（给更高Level的思维模式提示）

## 每轮交互的操作流程

1. **记录发送前的pane状态**（用于捕获增量输出）
2. **通过tmux send-keys发送Q**
3. **等待AI回复**（sleep 30-60秒，或观察pane变化）
4. **通过tmux capture-pane捕获A**
5. **判断A的状态**：progressing / stuck / success / dead_end
6. **更新dfs_tree.json**：添加节点，记录Q/A/Level/status
7. **调用Skill 5持久化**：本轮数据存入ArangoDB+文件系统
8. **决定下一步**：继续L5 / 给提示 / 回溯（Skill 4）/ 完成

## A的状态判断标准

| 状态 | 判断标准 |
|---|---|
| progressing | A长度>200字符，有数学内容，在推进 |
| stuck | A长度<100字符，或明确说"不知道/无法/卡住" |
| success | A包含"证毕/QED"且给出了正确结论 |
| dead_end | A走入错误方向且无法挽回 |

## 何时调用Skill 4（回溯）

- AI在L4/L5连续2-3轮stuck，且提示注入无效
- AI走入错误方向，且L6卡点处理无法纠正
- 当前路径的所有候选Q都已试过且都失败

## 何时结束

- **成功**：AI给出正确解答（A状态=success）→ 调用Skill 5做最终持久化
- **失败**：所有路径都走不通，或超过20轮/深度限制 → 调用Skill 5做最终持久化
- **截断**：context即将压缩 → 调用Skill 4回溯（新session）

## 注意事项

1. **每轮交互后必须更新dfs_tree.json**——这是跨压缩边界的状态恢复手段
2. **每轮交互后调用Skill 5持久化**——数据不可复现，不存就没了
3. **提示从rehearsal.md读取**——不依赖Session上下文记忆提示内容
4. **状态从dfs_tree.json读取**——不依赖Session上下文记忆当前进度
5. **本Skill只含框架**——具体提示文本在rehearsal.md中，状态在dfs_tree.json中
