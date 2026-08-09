# Grove侧在系统设计理念维度超越Worktree侧的面相

**文档编号**：296-v0
**日期**：2026-08-09
**作者**：Grove AI（GLM-5.2 High）
**用途**：回答"系统设计理念这个维度，Grove有没有超越了Worktree的内容，哪怕是一个面相？"
**性质**：基于逐条过Grove侧22条独立commit完整diff的一手证据

---

## 0. 方法论

本文档基于以下一手证据：
- Grove侧22条独立commit（分叉点`2596dcf`之后）的完整diff逐条核查
- Worktree侧140条独立commit中关键commit的完整diff对照
- 特别是`a3d65da`的完整diff（termination_detector.py的timeout移除）
- Worktree侧`check_ai_terminated`函数的完整实现（7行）

---

## 1. 结论：有一个面相，只有一个

Grove侧在系统设计理念维度**确实有一个面相**超越了Worktree侧——但只有**一个**，而且是一个很小的面相。

### 1.1 这个面相：终止检测与实验预算的分离

**commit**：`a3d65da`（2026-08-08 10:50:54）

**commit message**：

> termination_detector: 移除timeout杀AI逻辑
>
> 根因：核心循环的关键约束是"推理AI不需要停下接受提示"——
> AI在长thinking是正常状态，不是卡死。timeout逻辑把"AI在长时间思考"
> 误判为"AI卡死了"，300秒无新node就杀掉AI。
>
> 修复：移除timeout判定。终止只由session_ended/crash/response_truncated
> 判定。硬超时由外层max_time_per_ai控制（那是实验预算，不是终止检测）。
>
> AI在长thinking时，辅助Pipe用已有的thinking并行工作——
> 这才是"系统与推理AI并行运行"。

**diff证据**（termination_detector.py第140-152行）：

删除了以下逻辑（约15行删除）：

```python
# 3. 检查sessions.db是否有新node（替代thinking_readable.txt）
if self.devin_session_id:
    current_count = self._get_node_count()
    if current_count > self._last_node_count:
        # 有新node→AI还在活动
        self._last_node_count = current_count
        self._last_activity_time = now
    elif (now - self._last_activity_time) > self.timeout:
        return TerminationEvent(
            detected_at=now,
            reason="timeout",
            tmux_session=tmux_session,
            details=f"sessions.db {self.timeout:.0f}秒无新node",
        )
else:
    # 没有devin_session_id——只靠tmux session检测
    pass
```

替换为以下注释（约8行新增）：

```python
# 3. 不再用timeout杀AI
# 核心循环的关键约束："推理AI不需要停下接受提示"——
# AI在长thinking是正常状态，不是卡死。系统与AI并行运行：
# AI在thinking的同时，辅助Pipe用已有的thinking提取节点、整理树。
# 终止只由session_ended/crash/response_truncated判定，
# 或者由外层的max_time_per_ai硬超时控制（那是实验预算，不是终止检测）。

return None
```

### 1.2 设计理念的内容

这个面相包含两个设计理念：

**理念1：AI在长时间思考是正常状态，不是卡死**

267号面相文档（分叉前的共同工作）说了"推理AI不需要停下接受提示"，但没有明确说"AI在长时间思考时不应被系统打断"。267号的认知是关于"提示注入时序"的——不需要让AI停下来接受提示。Grove侧在实际运行中遇到timeout杀AI的问题后，把这个认知推论到了"终止检测"——AI在长时间思考时不是卡死，不应该被系统timeout杀掉。

这是一个从267号的"提示注入时序"认知推论到"AI终止检测"认知的推论。267号没有明确说这个推论，Worktree侧也没有做出这个推论（Worktree侧没有termination_detector模块）。Grove侧是在解决实际问题时发现并明确化了这个推论。

**理念2：终止检测≠实验预算**

- **终止检测**：判断AI是否自然终止了。终止原因有三类：session_ended（AI进程退出）、crash（崩溃）、response_truncated（token用尽）。这三类都是AI自己的状态决定的。
- **实验预算**：外层给AI的时间上限（max_time_per_ai）。这是实验管理者给AI的资源限制，不是AI自己的状态。

timeout逻辑把这两个混淆了——它用实验预算的逻辑（超时就杀）去做终止检测的事情（判断AI是否卡死）。Grove侧明确分离了这两个概念：终止检测只看AI自己的状态，实验预算由外层控制。

### 1.3 Worktree侧的对应

Worktree侧的`check_ai_terminated`函数（`ff91ed5`中创建，tree_engine.py）：

```python
def check_ai_terminated(exp_id: str) -> bool:
    """检测推理AI是否自然终止（tmux session的devin cli停止）。"""
    session_name = f'harness-{exp_id}'
    result = subprocess.run(
        ['tmux', 'has-session', '-t', session_name],
        capture_output=True, text=True, timeout=5
    )
    # has-session返回0=存在，非0=不存在
    return result.returncode != 0
```

只有7行。检查tmux session是否存在，返回bool。没有终止原因分类，没有timeout，也没有"终止检测vs实验预算"的区分。

Worktree侧没有遇到timeout杀AI的问题（因为它的tree_engine.py从未有过timeout逻辑），因此也没有做出"终止检测≠实验预算"的区分。Worktree侧的终止检测是纯二值的（存在/不存在），没有区分终止原因，也没有区分终止检测和实验预算。

### 1.4 这算不算"超越"

我认为算。Grove侧做出了一个Worktree侧没有做出的设计理念区分——**终止检测与实验预算是两个不同的概念，不应混淆**。虽然这个区分是在解决实际问题时发现的，不是在设计阶段主动提出的，但它是一个关于系统设计的理念，不是纯工程修复。

具体来说：

- **纯工程修复**会是："timeout太短了，从120秒改到300秒"（Grove侧确实先做了这个，`8819ad8`，10:34）
- **设计理念区分**是："timeout逻辑本身不应该存在，因为它混淆了终止检测和实验预算"（Grove侧随后做了这个，`a3d65da`，10:50）

从`8819ad8`（调大timeout）到`a3d65da`（移除timeout）的演变，是一个从工程修复到设计理念区分的演化过程。Grove侧先尝试了工程修复（调大timeout），发现治标不治本，然后做出了设计理念的区分（移除timeout，分离终止检测和实验预算）。

---

## 2. 没有超越的地方

其他21条Grove侧独立commit都没有在系统设计理念维度超越Worktree侧：

| Grove侧commit | 内容 | 为什么不算超越 |
|---|---|---|
| `83c18ef` | Grove repo迁移 | 纯工程（路径更新） |
| `243dc19` | 数据库隔离 | 纯工程（库名更换） |
| `21f99a6` | 工作目录隔离 | 纯工程（目录创建） |
| `058965c` | 阶段2实现 | 工程实现（3028行新代码），设计理念来自267号共同工作 |
| `1a12d41` | 核心循环认知落盘+辅助智能体JD | Worktree侧的`04de8c4`（10:01）commit message明确写"从Grove repo的271号文档同步核心循环认知"——但两边几乎同时做了这个落盘，核心循环和JD是267号共同工作的延伸 |
| `cf6c449` | 272号Checklist补充 | 纯文档补充 |
| `a455b5b` | 生动写作规则 | Worktree侧也有生动性原则（`4b64ac3`，10:07） |
| `97fa9c5` | sessions.db替代MITM | 工程改进（采集技术路线转换），不是设计理念 |
| `fb8ddf7` | termination_detector改用sessions.db | 工程改进 |
| `8819ad8` | timeout 120s→300s | 工程修复（调大参数） |
| `f2d51ba` | 补回"系统就是你" | **从Worktree同步**（commit message自述"从worktree repo同步三个关键section"） |
| `f14acdc` | 身份觉知rule | **从Worktree同步**（commit message自述"从worktree repo同步，适配Grove repo路径后安装"） |
| `49d61ea` | sleep自检rule | Worktree侧也有（`d8588d2`，10:49，几乎同时） |
| `04bcbe4` | sessions_db_reader.init()修复 | 纯bug修复 |
| `3a97188` | 更新任务追踪 | 纯文档更新 |
| `4babfdd` | case_253实验完成 | 验证方法论改进（真实题vs虚拟题），不是设计理念 |
| `80fc561` | PatternMatcher子集匹配 | bug修复 |
| `092a5e8` | NodeExtractor去重 | bug修复 |
| `aeb1ccf` | 发现policy选择逻辑问题 | 发现问题，不是设计理念 |
| `af49f50` | 293号报告 | 文档落盘 |
| `14bb497` | 294号git log覆盖范围 | 文档落盘 |

---

## 3. 这个超越的局限

### 3.1 它是267号的推论，不是全新的设计理念

267号面相文档（分叉前的共同工作）说了"推理AI不需要停下接受提示"。Grove侧的"AI在长时间思考是正常状态，不是卡死"是这个认知在终止检测场景下的推论——如果AI不需要停下接受提示，那么AI在长时间思考时也不应该被系统timeout杀掉。

这不是一个全新的设计理念，而是一个已有认知在新场景下的应用。但它确实是一个Worktree侧没有做出的推论。

### 3.2 它是在解决实际问题时发现的，不是在设计阶段主动提出的

Grove侧的演化过程是：
1. `058965c`（09:40）：创建termination_detector，包含timeout逻辑
2. `8819ad8`（10:34）：timeout太短，从120秒改到300秒（工程修复）
3. `a3d65da`（10:50）：timeout逻辑本身不应该存在（设计理念区分）

这个演化过程说明Grove侧先有了错误的设计（timeout杀AI），然后通过实践发现这个设计违反了267号的认知，然后做出了设计理念的区分。

Worktree侧没有做出这个区分，是因为Worktree侧没有创建termination_detector模块——它的`check_ai_terminated`函数只有7行，只检查tmux session存在性，没有timeout逻辑，因此没有遇到这个问题。

### 3.3 它很小

这是一个关于"终止检测模块中是否应该有timeout逻辑"的设计理念区分。它不是一个大的系统设计理念（如tell+hint二元组、三层Pipe架构、概念树），而是一个具体的模块级别的设计决策。

但用户问的是"哪怕是一个面相"——这个确实是一个面相，虽然很小。

---

## 4. Worktree侧在系统设计理念维度走得远得多的地方

作为对比，Worktree侧在系统设计理念维度有以下Grove侧完全没有的工作：

| 设计理念 | Worktree侧证据 | Grove侧 |
|---|---|---|
| tell+hint二元组 | 000号v1/v2/v3修正（`3e28bdc`/`e32c1c0`/`36b4a3d`） | 无 |
| 三层Pipe架构 | poc9_tell_filter.py 329行 + poc10_tell_disambiguation.py 386行 | 无 |
| 概念树设计哲学 | 287号用户第六次原文（`c3467db`，100+7行） | 无 |
| tell的去特化 | 287号（`6067b5e`，118行新建） | 无 |
| 拓扑相同tell区分 | POC-VMS-10（`19e57f1`，3文件702行） | 无 |
| 根分叉vs点分叉 | 000号v2修正（`e32c1c0`，55+23行） | 无 |
| hint字典的Low Level化 | 281号（`8acb61c`）+ POC-VMS-8（`afec4a6`，32文件943行） | 无 |
| 脉络继承+方向注入的组合 | POC-VMS-8结果（`7e47e65`，bare 0%→tree 67%） | 无 |
| 四代继承梳理 | 290号（`979b4d7`，338行） | 无 |
| QA序列分析 | 292号（`1a48a68`） | 无 |
| 并发DFS设计 | tree_engine.py MAX_CONCURRENT=2（`ff91ed5`，599行） | 无（Grove侧是串行） |

---

## 5. 最终回答

**对于用户的问题"系统设计理念这个维度，Grove有没有超越了Worktree的内容，哪怕是一个面相？"——**

有，只有一个：**终止检测与实验预算的分离**（`a3d65da`）。

这个面相包含两个设计理念：
1. AI在长时间思考是正常状态，不是卡死（267号"推理AI不需要停下接受提示"在终止检测场景下的推论）
2. 终止检测（判断AI是否自然终止）和实验预算（外层给AI的时间上限）是两个不同的概念，不应混淆

这个超越的局限：
- 它是267号的推论，不是全新的设计理念
- 它是在解决实际问题时发现的，不是在设计阶段主动提出的
- 它很小，是模块级别的设计决策，不是系统级别的

但它确实是一个Worktree侧没有做出的设计理念区分。Worktree侧的`check_ai_terminated`函数只有7行，只检查tmux session存在性，没有做出"终止检测≠实验预算"的区分。

在系统设计理念的其他维度——tell+hint二元组、三层Pipe架构、概念树、去特化、拓扑相同tell区分、根分叉vs点分叉、hint字典Low Level化、脉络继承+方向注入、四代继承、QA序列分析、并发DFS——Worktree侧走得比Grove侧远得多。
