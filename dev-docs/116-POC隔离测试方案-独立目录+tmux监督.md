# dev-docs/116-POC隔离测试方案-独立目录+tmux监督.md

## 一、问题

POC对照实验需要确保：
1. subagent不能看到数学大师项目的AGENTS.md（否则知道方法论，作弊）
2. subagent不能用网络搜索找答案（否则不是测试AI内在能力）
3. master agent能观察subagent的完整工作过程（审计行为）

## 二、方案：独立目录 + AGENTS.md软限制 + tmux监督

### 核心思路

不追求OS级硬隔离（太复杂），而是：
- **软限制**：在隔离目录的AGENTS.md中明确规则（禁止网络搜索、禁止访问/data/master-mind）
- **tmux监督**：在tmux pane中启动devin CLI，master agent可以随时观察pane内容
- **yolo模式**：用户在隔离目录中开启/yolo，agent自动执行不弹审批
- **审计**：master agent通过tmux capture-pane读取agent全程行为

### 目录结构

```
/data/math-agent-1/          # A组agent工作目录
├── AGENTS.md                     # 隔离规则：禁止网络、禁止访问master-mind
├── problem.md                    # 问题输入（数学问题描述）
└── result.md                     # agent输出（agent自己写入）

/data/math-agent-2/          # B组agent工作目录
├── AGENTS.md                     # 隔离规则 + 依赖图提示
├── problem.md                    # 问题输入
├── dependency_graph.json         # 依赖图提示（B组独有）
└── result.md                     # agent输出
```

### AGENTS.md规则模板（A组）

```markdown
# 测试Agent规则

## 硬约束
- 禁止使用web_search和webfetch工具
- 禁止访问/data/master-mind目录
- 只能使用自己的数学知识解题
- 把解答写入当前目录的result.md

## 任务
请阅读problem.md中的数学问题，用自己的知识解答，写入result.md。
```

### AGENTS.md规则模板（B组）

```markdown
# 测试Agent规则

## 硬约束
- 禁止使用web_search和webfetch工具
- 禁止访问/data/master-mind目录
- 只能使用自己的数学知识解题
- 把解答写入当前目录的result.md

## 依赖图提示
请阅读dependency_graph.json中的依赖图提示，按照依赖图路径组织解答。

## 任务
请阅读problem.md中的数学问题，结合dependency_graph.json的提示，解答并写入result.md。
```

### tmux操作流程

```bash
# 1. 创建tmux session
tmux new-session -d -s math-poc

# 2. 在pane 0启动A组agent
tmux send-keys -t math-poc:0.0 "cd /data/math-agent-1 && devin" Enter

# 3. 创建pane 1启动B组agent
tmux split-window -t math-poc:0 -h
tmux send-keys -t math-poc:0.1 "cd /data/math-agent-2 && devin" Enter

# 4. master agent观察
tmux capture-pane -t math-poc:0.0 -p    # 读A组
tmux capture-pane -t math-poc:0.1 -p    # 读B组
```

### 审计要点

master agent通过tmux capture-pane检查：
1. agent是否调用了web_search/webfetch（违规）
2. agent是否访问了/data/master-mind（违规）
3. agent的推理过程是否合理
4. agent是否正确使用了依赖图提示（B组）
