# 任务追踪 · Trajectory采集与Solver-Harness系统

> **本文件是本工作线的跨Session工作追踪文档。**
> **作用**：帮助进入本工作线的AI（可能跨Session、跨压缩边界）快速恢复工作意识——之前做了什么、现在在做什么、接下来该做什么、为什么做。
>
> **维护规则**：每完成一个工作单元，立即更新对应条目状态。新增任务追加到末尾。不删除历史条目。
>
> **与主线任务追踪的关系**：`任务追踪/任务追踪.md`是主线（253号检索机制验证），本文件是另一条并行工作线（trajectory采集基础设施）。两条线独立推进，互不阻塞。

---

## 0. 当前工作焦点

**主线**：搭建solver-harness系统——一个完整的trajectory自动采集环境，在tmux中启动devin cli并自动采集所有数据。

**当前状态**：solver-harness v1实施完成，端到端测试通过。主控脚本重写完成（全局共享mitmproxy + 事后批量解码 + work_dir匹配分发）。3个设计决策已确认（CA永久信任+host白名单、全局单mitmproxy固定18888、GuidedLoop独立使用）。

**下一步**：写solver-harness的README + 更新solver-tmux-launch元组 + 更新263号方案文档实现状态。

---

## 1. 已完成的工作

### 1.1 Devin CLI trajectory数据源调查

**为什么做**：用户观察到AI有时"卡在thinking中"不产出输出。需要搞清楚thinking数据是否实时落盘、能否实时拦截、"卡在thinking"的根因是什么。这是设计trajectory采集系统的前置调查。

- [x] 确认Devin CLI通信架构：`devin cli` → `devin acp`（子进程）→ 云端API（HTTPS）
- [x] 确认thinking数据流：云端生成 → 流式传输到本地 → devin cli内存累积 → 等完整response后写入sessions.db
- [x] 确认thinking**不实时落盘**——只有step级数据在sessions.db中
- [x] 确认"卡在thinking"根因：AI hit max output token limit（59k字符thinking但0 content 0 tool_calls）
- [x] 完整映射sessions.db schema（sessions/message_nodes/tool_call_state三表+chat_message JSON结构）
- [x] 产出文档：`dev-docs/262-v0-2026-08-08-Devin-CLI-trajectory数据源调查与MITM-thinking拦截验证.md`

### 1.2 MITM代理方案验证

**为什么做**：调查确认thinking是流式传输到本地的（只是没落盘），所以可以通过MITM代理在`devin acp`和云端API之间拦截HTTPS通信，实现token级实时thinking拦截。这比sessions.db轮询（step级、~3s延迟）高一个粒度。

- [x] 确认devin cli支持`HTTPS_PROXY`环境变量（reqwest库）
- [x] 确认devin cli用`rustls-platform-verifier`验证TLS（macOS Keychain）
- [x] 将mitmproxy CA加入macOS Keychain信任
- [x] 成功拦截GetChatMessage端点（`application/connect+proto`格式）
- [x] 逆向推断Connect streaming protobuf格式：1 byte flags + 4 bytes length + protobuf message
- [x] 逆向推断protobuf字段映射：field 9=thinking chunk, field 6=tool_call chunk, field 28=token usage等
- [x] 验证成功：拦截矩条件极差题测试的第一个inference响应（5808 bytes, 43 streaming messages），提取出thinking "Let me read the problem file first." + tool_call read(problem.txt)
- [x] 产出工具：
  - `xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py`（mitmproxy addon）
  - `xishujuzhen/mitm_thinking_intercept/decode_connect_proto.py`（protobuf解码器）
  - `xishujuzhen/mitm_thinking_intercept/sample_capture/`（样本数据）
  - `xishujuzhen/mitm_thinking_intercept/README.md`（MITM方案文档）

### 1.3 Solver-Harness方案设计

**为什么做**：MITM方案验证成功后，需要一个完整的系统把所有数据采集手段（MITM token级 + sessions.db step级 + tmux兜底）整合起来，自动化运行。不能每次手动启动mitmproxy、手动设代理、手动启动tmux。

- [x] 确认核心设计决策（用户确认）：
  - 目录分离：Solver工作目录（AI可见）vs Trajectory数据目录（AI不可见，避免污染Solver行为）
  - MITM默认开启
  - 系统命名：solver-harness
- [x] 设计系统架构：4个tmux sessions（devin cli + mitmproxy + decoder daemon + db monitor）
- [x] 设计数据流：MITM raw → decoder → jsonl；sessions.db → monitor → jsonl；tmux → pipe-pane → log
- [x] 设计数据格式：session_info.json + mitm/trajectory.jsonl + sessions_db/trajectory.jsonl
- [x] 产出文档：`dev-docs/263-v0-2026-08-08-Solver-Harness系统方案-完整Trajectory自动采集环境.md`
- [x] 初版主控脚本：`xishujuzhen/solver_harness/solver_harness.py`（5命令：launch/status/stop/decode/list，待完善和测试）

### 1.4 trajectory提取工具（前期工作，本工作线复用）

**为什么做**：在MITM方案之前，已有基于sessions.db的trajectory提取工具。solver-harness需要复用这些工具作为step级数据源和兜底。

- [x] `xishujuzhen/trajectory_extractor.py`（完整trajectory提取，post-analysis）
- [x] `xishujuzhen/trajectory_monitor.py`（实时监控sessions.db，step级）
- [x] `xishujuzhen/thinking_extractor.py`（简化版thinking提取）
- [x] 对应元组：trajectory-extraction、thinking-extraction、solver-tmux-launch

### 1.5 solver-harness v1实施（主控脚本重写 + 端到端测试）

**为什么做**：263号方案v1确认了设计决策（全局共享mitmproxy + CA永久信任 + host白名单 + 事后批量解码 + GuidedLoop独立使用），需要根据v1方案重写初版主控脚本（初版是每实验独立mitmproxy的旧设计），并端到端验证。

- [x] 重写`solver_harness.py`：全局共享mitmproxy（固定18888 + `--allow-hosts`限制3个devin host）
- [x] 实现`cmd_mitm`（start/stop/status管理共享mitmproxy生命周期）
- [x] 实现`cmd_launch`：确保mitmproxy运行 → 创建目录 → 复制模板 → 写session_info → 启动db轮询 → 启动devin cli（走代理）→ 启动pipe-pane → 回填devin_session_id
- [x] 实现`cmd_stop`：停止该实验的tmux sessions（不影响共享mitmproxy）+ 自动调用decode-all
- [x] 实现`cmd_decode_all`：扫描共享raw目录 → 通过_req文件中的work_dir匹配实验 → 解码分发到各实验mitm/trajectory.jsonl
- [x] 实现`devin_session_id`回填（从sessions.db查找work_dir对应session_id，最多等30秒）
- [x] 实现`_extract_session_id`（从protobuf field 17提取云端UUID）
- [x] 发现并修复session_id匹配问题：MITM的UUID和sessions.db的本地名称是两个ID系统，改用_req文件中的work_dir路径匹配
- [x] 端到端测试通过：用简单题（n²+n恒偶）测试完整launch→stop→decode-all流程
  - 4个raw文件，3个matched（含work_dir），1个unmatched（session token请求，无work_dir）
  - 解码结果正确：Entry 0读取problem.txt，Entry 1用Python验证，Entry 2输出证明
  - 所有3个response正确匹配到harness-test-001实验

---

## 2. 待办清单（按优先级排序）

### P0-高优先级（solver-harness实施）—— ✅ 已完成

#### 2.1 完善solver-harness主控脚本 ✅

**为什么做**：初版脚本已写但未测试。需要根据263号方案v1完善各命令的实现，确保端到端流程能跑通。

- [x] 重写`cmd_launch`：目录创建 + 确保共享mitmproxy + db轮询 + devin cli + pipe-pane + 回填devin_session_id
- [x] 重写`cmd_status`：session_info + tmux状态 + 数据统计
- [x] 重写`cmd_stop`：停止该实验的tmux sessions（不影响共享mitmproxy）+ 自动decode-all
- [x] 实现`cmd_decode_all`：通过_req文件work_dir匹配实验，解码分发
- [x] 实现`cmd_list`：列出所有实验
- [x] 实现`cmd_mitm`：管理共享mitmproxy

#### 2.2 实现解码daemon ✅（改为事后批量解码）

**为什么做**：MITM捕获的raw .bin文件需要解码为jsonl。v1方案改为事后批量解码（共享raw目录混合多实验数据，实时分发复杂易错）。

- [x] 实现`cmd_decode_all`：扫描共享raw目录，通过_req文件work_dir匹配实验，解码分发
- [x] 未匹配的数据写入`_shared/unmatched/`
- [x] 解码失败时记录error到`_shared/unmatched/decode_errors.jsonl`

#### 2.3 端到端测试 ✅

- [x] 用简单题（n²+n恒偶）测试完整launch流程
- [x] 验证MITM数据：3个response正确匹配，解码出thinking+tool_calls
- [x] 验证兜底记录：tmux_pipe.log有AI完整证明输出
- [x] 验证conversation.json：60KB，含完整对话

### P1-中优先级（完善和集成）

#### 2.4 solver-harness文档和元组

**为什么做**：solver-harness作为基础设施，需要有README和元组（rule+skill），让其他AI知道何时使用它。

- [ ] 写solver-harness的README
- [ ] 更新solver-tmux-launch元组，指向solver-harness
- [ ] 考虑是否需要独立的solver-harness元组

#### 2.5 GuidedLoop集成（已确认独立使用）

**为什么做**：已确认solver-harness和GuidedLoop独立使用，先解耦后集成。裸跑测试的trajectory采集验证可靠后，再考虑集成。

- [x] 确认：solver-harness独立使用，不集成GuidedLoop（裸跑测试优先）
- [ ] 未来如需集成，修改GuidedLoop调用solver-harness启动Solver

### P2-低优先级（后续优化）

#### 2.6 MITM protobuf schema精确化

**为什么做**：当前protobuf字段映射是逆向推断的，可能有误差。如需精确解析，需要正式的.proto文件。

- [ ] 尝试从devin二进制中提取更完整的proto定义
- [ ] 或通过更多样本对比验证字段映射

#### 2.7 trajectory数据分析工具

**为什么做**：采集到的trajectory数据需要分析工具——如thinking长度分布、tool_call序列模式、卡点检测等。

- [ ] 写trajectory分析脚本
- [ ] 可视化thinking流式过程

---

## 3. 关键决策记录

### 3.1 为什么目录分离（Solver工作目录 vs Trajectory数据目录）

用户明确指出：AI不能看到自己的运行数据，这会污染Solver的行为。数据必须放在Solver工作目录之外。

- Solver工作目录：`/data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/`（AI可见）
- Trajectory数据目录：`/data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/`（AI不可见）
- 同名子目录设计，一一对应，好查

### 3.2 为什么MITM默认开启

用户明确选择：每次启动Solver都自动起mitmproxy + 走代理，实现token级实时拦截。虽然需要全局Keychain信任mitmproxy CA，但token级数据的价值值得这个代价。

### 3.3 为什么三层数据采集

- MITM可能失败（CA未信任、端口冲突、protobuf解析错误）
- sessions.db轮询有~3s延迟，但数据最完整（含tool_results）
- tmux pipe-pane是最可靠的兜底，但只有终端可见内容
- 三层互为补充，任一层失败其他层仍能提供数据

### 3.4 为什么每实验独立mitmproxy实例

- 避免端口冲突
- 隔离实验数据（每个实验的raw数据在自己的目录）
- 实验结束后自动停止mitmproxy

---

## 4. Git Commit 历史（本工作线）

| Commit | 描述 | 产出路径 |
|---|---|---|
| `7bd106f` | MITM thinking拦截方案验证 | `xishujuzhen/mitm_thinking_intercept/README.md`, `xishujuzhen/mitm_thinking_intercept/decode_connect_proto.py`, `xishujuzhen/mitm_thinking_intercept/mitm_proto_capture.py`, `xishujuzhen/mitm_thinking_intercept/sample_capture/` |
| `72a0ebf` | 落盘262号调查结果+263号solver-harness方案+初版主控脚本 | `dev-docs/262-v0-2026-08-08-Devin-CLI-trajectory数据源调查与MITM-thinking拦截验证.md`, `dev-docs/263-v0-2026-08-08-Solver-Harness系统方案-完整Trajectory自动采集环境.md`, `xishujuzhen/solver_harness/solver_harness.py` |
| `cb6a51a` | 建立多AI并发任务追踪机制+为trajectory采集工作线建独立任务追踪文档 | `AGENTS.md`, `任务追踪/trajectory采集与solver-harness.md`（后重命名为`02-trajectory采集与solver-harness.md`） |
| `48ff87a` | 263号方案v1：完整技术方案（含讨论中确认的设计决策） | `dev-docs/263-v1-2026-08-08-Solver-Harness系统方案-完整Trajectory自动采集环境.md`（同时删除v0） |
| `8a2d5a2` | 新增任务追踪README.md（工作线DAG）+ 更新AGENTS.md | `任务追踪/README.md`, `AGENTS.md` |
| `47e80e6` | solver-harness v1实施：重写主控脚本（全局共享mitmproxy+事后批量解码） | `xishujuzhen/solver_harness/solver_harness.py` |
| `1e7f41c` | fix: decode-all改用_req文件中的work_dir匹配实验（不用session_id UUID） | `xishujuzhen/solver_harness/solver_harness.py` |
| `c533e3c` | 更新02任务追踪文档和263号方案文档的实现状态 | `任务追踪/02-trajectory采集与solver-harness.md`, `dev-docs/263-v1-2026-08-08-Solver-Harness系统方案-完整Trajectory自动采集环境.md` |

---

## 5. 跨Session读取指南

**新Session的AI进入本工作线后**：

1. **先读本文件**——了解本工作线的焦点、已做和待做事项
2. **读dev-docs/262号**——了解trajectory数据源调查和MITM验证的完整结论
3. **读dev-docs/263号**——了解solver-harness系统的完整方案设计
4. **读`xishujuzhen/mitm_thinking_intercept/README.md`**——了解MITM方案的技术细节
5. **看§2待办清单**——选择下一步要做的事
6. **开始工作前**——确认worktree隔离规则（AGENTS.md顶部）、数据库隔离

**工作完成后**：
- 更新本文件的对应条目状态
- 更新263号方案文档的实现状态（Check List打勾）
- commit
