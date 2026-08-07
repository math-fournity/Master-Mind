---
name: guided-session-launch
description: >
  引导式数学解题元组群·Skill 2：启动session。
  准备work_dir、problem.txt，启动tmux+devin cli+--export。
  WHEN to use: 元组群guided-math-solving的第二步，预演完成后需要启动做题AI时。
  WHEN NOT to use: 非引导模式、session已在运行中。
---

# guided-session-launch skill

## 用途

元组群 `guided-math-solving` 的 Skill 2。预演完成后，准备做题AI的运行环境并启动交互式session。

## 前置条件

- Skill 1 `guided-rehearsal` 已完成，`runs/<run_id>/rehearsal.md` 已落盘
- 从rehearsal.md中获取题目文本

## 工作流

### 步骤1：准备run目录

```bash
RUN_ID="guided_<编号>"
RUN_DIR="runs/${RUN_ID}"
EXPORT_DIR="${RUN_DIR}/exports"
mkdir -p ${EXPORT_DIR}
```

### 步骤2：选择Solver工作目录

三个可用目录，选一个未被占用的：
- `/data/math-agent-glm5.2-1`
- `/data/math-agent-glm5.2-2`
- `/data/math-agent-glm5.2-3`

检查占用：`tmux list-sessions | grep guided`

### 步骤3：清理work_dir并写入problem.txt

**session隔离铁律**：清理work_dir下的所有文件（problem.txt、hint.txt、之前的产物），只保留AGENTS.md。

```bash
WORK_DIR="/data/math-agent-glm5.2-<n>"
# 清理（保留AGENTS.md）
find ${WORK_DIR} -maxdepth 1 -type f ! -name "AGENTS.md" -delete
```

写入problem.txt（完整题目文本，LaTeX格式）。

### 步骤4：启动tmux + devin cli + --export

```bash
EXPORT_PATH="${EXPORT_DIR}/session_$(date +%s).json"
SESSION_NAME="guided-exp-<n>"

tmux new-session -d -s ${SESSION_NAME} \
  "cd ${WORK_DIR} && devin --model glm-5-2 --export ${EXPORT_PATH}"
```

### 步骤5：处理trust prompt

```bash
sleep 5
tmux capture-pane -t ${SESSION_NAME} -p
# 如果看到trust prompt，发送"1"选择Yes
tmux send-keys -t ${SESSION_NAME} "1" Enter
sleep 8
```

### 步骤6：启动pipe-pane兜底记录

```bash
tmux pipe-pane -t ${SESSION_NAME} "cat >> ${RUN_DIR}/tmux_pipe.log"
```

### 步骤7：初始化DFS树

```python
from scripts.dfs_tree import DFSTree
tree = DFSTree("${RUN_DIR}/dfs_tree.json")
# 根节点将在Skill 3的第一轮交互时创建
```

### 步骤8：记录session信息

将以下信息记录到 `${RUN_DIR}/session_info.json`：
- run_id, session_name, work_dir, export_path, model, devin_cli_version
- agents_md_snapshot（work_dir/AGENTS.md的内容）
- problem_txt_snapshot（problem.txt的内容）
- start_timestamp

## 完成后

加载 Skill 3 `guided-interaction` 开始交互引导。

## 注意事项

1. **--export必须带**：每轮对话自动导出JSON，是trajectory记录的核心
2. **pipe-pane必须启动**：terminal兜底记录
3. **work_dir必须清理**：session隔离铁律
4. **AGENTS.md必须保留**：做题AI需要加载Solver角色定义
5. **不要用exec后台**：tmux优先（全局铁律）
