# 101-UserPromptSubmit提醒机制方案

> **文档定位**：模仿星学项目97号文档的UserPromptSubmit提醒机制，给数学项目加一份同样的"每次用户提问时自动提醒"机制。内容适配数学项目特点。

## 一、星学项目方案要点

星学项目97号文档描述了三轮迭代后的最终方案（v3：纯提醒，无硬门禁）：

- **UserPromptSubmit hook**：每次用户提问时，从`UserPromptSubmit.txt`文件读取提醒内容，注入到AI上下文
- **提醒内容外置到txt文件**：改提醒内容只需编辑txt文件，不用改代码
- **核心信念**：提示就够了，不需要硬门禁。AI看到提醒后自行判断是否需要进入工作系统
- **subagent豁免**：subagent不需要每次都考虑进入工作系统

## 二、数学项目与星学项目的差异

| 维度 | 星学项目 | 数学项目 |
|---|---|---|
| 认知检查点命令 | `cognition_checkpoint.py start --seeds <cog_id>` | `cognition_checkpoint_math.py start --seeds <cog_id>` |
| 种子推荐表 | 无 | **有**（`seed_recommendation_table.json`，5种问题类型→推荐意识种子） |
| 七步骤工作流 | 无 | **有**（`seven_step_pipeline.py`，做数学证明时的入口） |
| 数学意识节点 | 无 | **有**（5个：不变量思维/局部-全局/逼近论/极端检验/数值检验） |
| AGENTS.md认知图索引 | 有 | 有 |

**关键差异**：数学项目的用户提问可能有两种类型——
1. **一般工作问题**（讨论方案、更新文档、看代码等）→ 和星学一样，提醒考虑是否需要加载认知
2. **数学问题**（做证明、解题、分析依赖图等）→ 额外提醒查种子推荐表+七步骤工作流

## 三、方案设计

### 3.1 新增文件

| 文件 | 用途 |
|---|---|
| `xishujuzhen/user_prompt_submit_hook_math.py` | UserPromptSubmit hook脚本，从txt文件读取提醒 |
| `xishujuzhen/UserPromptSubmit.txt` | 提醒内容文件（可随时编辑定制） |

### 3.2 修改文件

| 文件 | 修改内容 |
|---|---|
| `.devin/hooks.v1.json` | 加入UserPromptSubmit hook配置 |

### 3.3 提醒内容设计

```
[工作系统提醒] 请在回答用户问题前，考虑你是否需要先进入工作系统：
  .venv/bin/python3 xishujuzhen/cognition_checkpoint_math.py start --seeds <cog_id1>,<cog_id2>
从AGENTS.md认知图索引中选择与用户问题相关的种子认知单元，执行CP1-CP3认知加载。

如果是数学问题（证明/解题/依赖图分析），先查种子推荐表：
  cat xishujuzhen/seed_recommendation_table.json
按问题类型选意识种子，再做七步骤工作流：
  .venv/bin/python3 xishujuzhen/seven_step_pipeline.py --steps 1,2,3

如果你是subagent，请忽略此提醒，subagent不需要每次都考虑进入工作系统。
```

**设计要点**：
- 前三行：和星学一样的通用提醒（考虑是否进入工作系统+具体命令+从哪选种子）
- 第四到七行：**数学项目独有**——数学问题额外提醒（种子推荐表+七步骤工作流）
- 最后一行：subagent豁免（和星学一样）

### 3.4 hook脚本设计

和星学的`user_prompt_submit_hook.py`结构完全一样，只是文件路径指向数学项目的txt文件。从`DEVIN_PROJECT_DIR`环境变量找项目根目录，读取`xishujuzhen/UserPromptSubmit.txt`。

### 3.5 hooks配置

在`.devin/hooks.v1.json`中加入UserPromptSubmit hook：

```json
"UserPromptSubmit": [
  {
    "matcher": "",
    "hooks": [
      {
        "type": "command",
        "command": ".venv/bin/python3 xishujuzhen/user_prompt_submit_hook_math.py",
        "timeout": 5
      }
    ]
  }
]
```

## 四、Check List

- [x] 编写`user_prompt_submit_hook_math.py`（模仿星学结构）——完成。从`DEVIN_PROJECT_DIR`找项目根，读取`xishujuzhen/UserPromptSubmit.txt`，注入到AI上下文。
- [x] 编写`UserPromptSubmit.txt`（数学项目提醒内容）——完成。前三行通用提醒（和星学一样）+ 第四到七行数学问题额外提醒（种子推荐表+七步骤工作流）+ 最后一行subagent豁免。
- [x] 修改`.devin/hooks.v1.json`加入UserPromptSubmit hook——完成。timeout=5秒。
- [x] 测试hook：模拟UserPromptSubmit事件，验证提醒内容正确注入——**通过**。`echo '{"hook_event_name":"UserPromptSubmit","prompt":"测试"}' | .venv/bin/python3 xishujuzhen/user_prompt_submit_hook_math.py`正确输出JSON，additionalContext包含完整提醒内容。
- [x] 更新AGENTS.md索引——完成。

## 五、诚实面对

1. **提醒不是强制**：和星学一样，AI看到提醒后仍然可能不进入工作系统。这是设计选择，不是bug。
2. **提醒内容需要维护**：随着项目演进，提醒内容可能需要调整（如新增工具入口）。直接编辑txt文件即可。
3. **数学问题判断靠AI**：提醒中写"如果是数学问题"，但"是否是数学问题"由AI自行判断。这是合理的——AI能区分用户是在讨论方案还是在做数学证明。
