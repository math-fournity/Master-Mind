---
description: >
  sleep前自检——调用sleep或get_output等待前，问自己一句：
  此刻有推理AI在跑吗？如果有，你是辅助Pipe，不是旁观者。
  你该做的事在AGENTS.md的"辅助智能体SOP"和grove-core-loop.md里有描述。
  WHEN to use: 任何sleep、get_output等待、timeout>0的后台命令之前。
  WHEN NOT to use: 无例外——每次都要自检。
trigger: always
---

# sleep前自检

## 调用sleep之前，问自己一句：

> **此刻有推理AI在跑吗？**

- **有** → 你是辅助Pipe。不要sleep。你有该做的事：
  - 采集thinking（读sessions.db）
  - 提取节点写入树
  - 在叶节点检索方向Q
  - 构造脉络、启动新AI
  - 检查循环完整性
  
  这些事在AGENTS.md"辅助智能体SOP"和`.devin/rules/grove-core-loop.md`里有描述。去读，去执行，不要干等。

- **没有** → 可以sleep或等待。但确认一下：你是在等一个非实验的命令（编译、下载、测试）吗？如果是，等没问题。

## 判定"有推理AI在跑"的方法

- 有tmux session名包含`harness-`且存在？
- sessions.db中有该session的新node在增长？
- 实验脚本（serial_multi_ai.py等）在后台运行？

任一为是 → 有推理AI在跑 → 你是辅助Pipe → 不要sleep。

## 违反时的纠正

**如果你已经sleep了，然后读到这条rule——停。**

立刻回到辅助Pipe角色。看AGENTS.md的SOP，找到你现在该做的事。园丁不等树长完才浇水。
