# AI Agent启动规范

**触发条件**：启动系统中任何AI Agent实例时——包括推理AI（Solver）、脉络分析AI（Parser）、trace匹配AI（Telling）、引导展开AI（Guide）等。always-on——任何涉及AI Agent启动的操作都必须遵守此规范。

## 核心约束

**系统中所有AI Agent的启动，全部使用tmux中的运行方式。首先到达指定的工作目录，然后启动devin cli实例运行。**

启动前必须在工作目录中准备好AGENTS.md、提示词文件、输入文件等。给devin cli的直接提示词应该很短——让AI去加载工作目录中的提示词文件，而不是把完整提示词塞在启动命令中。

**启动动作由脚本自动执行**（2026-08-11认知转变）。系统就是脚本——AI Agent的启动由Python代码用subprocess自动执行tmux命令，不需要Master Agent手动执行。Master Agent在系统运行时是检查者，不参与循环执行。

**yolo模式启动**：所有AI Agent的devin cli实例都用`--permission-mode dangerous`启动——自动批准所有工具操作。因为AI Agent在detached tmux session中运行，无法交互式批准文件写入和命令执行。如果不加此参数，AI Agent会在第一次需要写文件时卡住等待批准。

## 启动前的准备工作

每个AI Agent启动前，必须在其工作目录中准备好以下文件：

| 文件 | 内容 | 必需 |
|---|---|---|
| `AGENTS.md` | 给AI的指令和约束——角色定义、工作规范、产出要求 | ✅ |
| `prompt.md` | 完整提示词——V5/V7/V8/V9等提示词的完整内容（可能几十KB） | ✅ |
| `input.md` 或 `input.json` | 输入数据——题目文本、解答文本、thinking文本、孤悬trace等 | ✅ |
| 其他依赖文件 | 如verify_lattice_completeness.py的路径引用、tell库片段等 | 按需 |

**禁止**：在工作目录没准备好的情况下启动AI Agent。禁止"先启动AI，让它自己去找文件"。

## 短启动提示词原则

给devin cli的直接提示词应该很短——让AI去加载工作目录中的提示词文件，而不是把完整提示词塞在启动命令中。

```
# ❌ 错误——把完整提示词塞在启动命令中（几十KB的提示词无法放在命令行参数里）
devin "你是脉络分析AI...（30KB的完整提示词）...请分析input.md中的解答"

# ✅ 正确——短启动提示词，让AI加载提示词文件
devin "加载 {workdir}/prompt.md 中的提示词，读取 {workdir}/input.md 中的输入数据，按提示词要求工作，完成后把产出写入 {workdir}/output.json 和 {workdir}/output.md"
```

**为什么**：提示词可能几十KB（V9提示词66KB），无法放在命令行参数中。放在文件中，AI启动后读取，既支持长提示词又保持启动命令简洁。同时，提示词文件本身是痕迹保留的一部分——可以审计"这个AI当时收到了什么提示词"。

## 标准启动流程（5步）

```
步骤1：创建工作目录
  mkdir -p palyground/{process}/{stage}/{problem_id}/{version}/

步骤2：准备文件（写入工作目录）
  {workdir}/AGENTS.md      ← AI的指令和约束
  {workdir}/prompt.md      ← 完整提示词（从提示词积累目录复制+填入输入占位符）
  {workdir}/input.md       ← 输入数据（题目/解答/thinking文本）
  {workdir}/input.json     ← 结构化输入数据（如有）

步骤3：在tmux中启动devin cli实例
  tmux new-session -d -s {session_name} \
    "cd {workdir} && devin '加载 {workdir}/prompt.md，读取 {workdir}/input.md，按提示词工作，产出写入 {workdir}/output.json 和 {workdir}/output.md'"

步骤4：等待devin cli实例完成
  tmux capture-pane -t {session_name} -p  # 检查状态
  # 或轮询 {workdir}/output.json 是否出现

步骤5：收集产出
  读取 {workdir}/output.json（结构化产出）
  读取 {workdir}/output.md（人类可读产出）
  读取 {workdir}/audit_report.json（程序验证报告，如有）
```

## tmux session命名规范

```
{process}-{stage}-{problem_id}-{version}

示例：
absorb-vein_analysis-IMO2009P6-V5
absorb-vein_analysis-IMO2009P6-V7
absorb-vein_analysis-IMO2009P6-V8
absorb-vein_analysis-IMO2009P6-V9
solve-inference_explore-IMO2009P6-solver_01
solve-trace_match-IMO2009P6-telling_03
```

## tmux管理命令

```bash
# 启动
tmux new-session -d -s {session_name} "cd {workdir} && devin '...'"

# 查看所有session
tmux list-sessions

# 检查某个session的输出
tmux capture-pane -t {session_name} -p

# 进入session查看（交互模式）
tmux attach -t {session_name}

# 停止session
tmux kill-session -t {session_name}
```

## 工作目录结构

```
palyground/{process}/{stage}/{problem_id}/
├── {version}/              ← 如果是4并发，每个版本一个子目录
│   ├── AGENTS.md           ← AI的指令和约束
│   ├── prompt.md           ← 完整提示词
│   ├── input.md            ← 输入数据
│   ├── input.json          ← 结构化输入数据（如有）
│   ├── output.json         ← AI结构化产出
│   ├── output.md           ← AI人类可读产出
│   └── audit_report.json   ← 程序验证报告（如有）
├── merged_traces.json      ← 4版本trace并集（仅4并发阶段）
└── meta.json               ← 本次运行的元数据
```

## 和其他规则的关系

- 和`six-trace-preservation.md`的关系：tmux session的输出可以capture-pane查看，工作目录中的文件是痕迹保留的载体。本规则定义"怎么启动"，痕迹保留rule定义"启动后要保留什么"。
- 和`six-mechanization-reference.md`的关系：程序验证（verify_lattice_completeness.py）的审计报告是AI Agent产出的一部分，落盘到工作目录的audit_report.json。
- 和全局`~/.config/devin/AGENTS.md`中"tmux优先"规则的关系：本规则是"tmux优先"在AI Agent启动场景下的具体化——所有AI Agent必须用tmux启动，不允许用nohup等脱离终端的方式。
