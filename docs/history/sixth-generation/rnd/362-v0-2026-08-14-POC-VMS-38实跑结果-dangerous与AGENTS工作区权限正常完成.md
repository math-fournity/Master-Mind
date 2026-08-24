# POC-VMS-38实跑结果：dangerous与AGENTS工作区权限正常完成

**日期**：2026-08-14  
**协议**：361号  
**最终判定**：`SUPPORTED_WITHIN_DEBUG_CANARY`  
**执行合同**：`SUPPORTED`  
**角色资格**：`NOT_SUPPORTED / NOT_TESTED`  
**事后探索性组件判定**：`PARTIAL`（不得用于资格化）  
**证据用途**：`DEVELOPMENT_ONLY`  
**已知缺陷**：历史final receipt的ATIF计数摘要错误，原始export仍完整可审计  

---

## 1. 结论

VMS-38验证了用户指定的解题侧Devin调试运行方式：

1. Devin CLI以`glm-5-2`（GLM-5.2 High）、no-sandbox、`dangerous`/bypass模式运行；
2. 权限边界由本次workspace内冻结的`AGENTS.md`和`TASK.md`规定；
3. Devin只读取本workspace内的AGENTS、题目和raw trajectory，只在同一workspace内运行Python、写目标JSON和DONE；
4. 运行过程可在private tmux中实时观察，输出和DONE出现后只发送一次有记录的`/exit`+`Enter`；
5. 进程exit 0，完整bundle原子封存到批准的D盘专属根；
6. 没有访问repo、入题侧资产、workspace外文件、网络、Git、其他AI或破坏性命令。

因此，VMS-36/37暴露的“Devin被配置拒绝读取自己的workspace”问题已经解除。`dangerous`在这里不等于没有边界：它取消逐工具人工确认，而角色边界由冻结输入、物理工作区隔离、一次性attempt合同和运行后原始tool-event审计共同约束。

这个结果只支持**交互式调试Canary的执行合同**。它不资格化Event Extractor，不证明AGENTS等同OS sandbox，也不证明生产数学质量或完整解题侧脉络管线已完成。

---

## 2. 冻结运行事实

| 字段 | 实际值 |
|---|---|
| `poc_id` | `POC-VMS-38` |
| attempt | `poc-vms-38-extractor-tmux-a1` |
| run | `poc-vms-38-dangerous-agents-tmux-20260814` |
| start | `2026-08-14T14:50:02.567362Z` |
| sealed | `2026-08-14T14:53:35.993847Z` |
| Devin | `3000.4.25 (7e8e528a)` |
| requested/effective model | `glm-5-2` / `GLM-5.2 High` |
| effort encoding | `high` by model UID |
| sandbox | `false` |
| permission | `dangerous`，TUI显示`bypass permissions on` |
| attempt / retry | `1 / 0` |
| freeze manifest SHA-256 | `2e0bda072c111b66725a101363adf63e5b973fa7e2fda10847bfc6cc22141eeb` |
| session ID | `thoracic-heron` |
| output SHA-256 | `dc50645114407e8efbb8b92d0e9bde73df614015fa0fc6fbc9bdc1c315b32f79` |
| DONE SHA-256 | `1a4c27856d108e742039a733e59738f301c86df41a2b017ed1963790193063eb` |
| export SHA-256 | `649ef8a126fd1ee1ff86d7a3aff33a23039836fa4c158a179807f4863208d73f` |
| final receipt SHA-256 | `0cf5be7e3df34507656f250cac3fe0557e4aee3fedf16d4d85eacbea0a60ac5f` |
| pane exit | `0` |
| final evidence dir | `/data/master-mind-solve-vein-data/poc-results/poc-vms-38-dangerous-agents-tmux-20260814/` |

启动前freeze的10个文件全部hash匹配，48项解题侧回归和入题侧保护基线均PASS。保护基线聚合SHA-256在本轮前后均为：

```text
9bb4fd2551d13f196610ddf8e203ad96b0855f3337f6c4e6502f6c764eafd6b3
```

---

## 3. 状态机与人工干预

关键snapshot按预注册状态机前进：

```text
STARTING
  → RUNNING
  → DONE_WAITING_EXIT
  → PROCESS_EXITED
  → FINALIZED
```

`health-snapshots/000005.json`在`2026-08-14T14:52:56.290802Z`首次同时观察到output、DONE和合法export，状态为`DONE_WAITING_EXIT`。此前没有向pane输入。

随后只执行了一次预注册干预：

```text
2026-08-14T14:53:04.822405Z
/exit
Enter
```

干预记录为`interventions/000000.json`，两个tmux send-keys调用均exit 0。snapshot 000006观察到pane dead且status 0，000007复核状态未反转，之后才finalize。没有第二次输入、第二个attempt或retry。

---

## 4. 输出合同

Devin生成：

```text
workspace/reasoning-trajectory.json
workspace/DONE.md
workspace/devin-export.json
```

`reasoning-trajectory.json`通过严格`ReasoningTrajectory`解析，包含10个按序事件；source artifact SHA-256与冻结raw trajectory一致，10个source span逐一重新计算后全部匹配。DONE正文为：

```text
reasoning-trajectory.json SHA256=dc50645114407e8efbb8b92d0e9bde73df614015fa0fc6fbc9bdc1c315b32f79
```

文件末尾有一个正常换行；运行器按冻结规则对正文做`.strip()`后精确比较，因此final receipt中的`done_marker_content_valid=true`成立。

这只证明输出的结构、来源绑定和封存合同成立。VMS-38没有预注册独立数学语义Judge，不能据此把Event Extractor升级为角色资格PASS。

封存后，用既有VMS-32冻结evaluator定义做了一次**事后、探索性**机械差分；它不是361号的确认性endpoint，也不改变本轮证据lane：

| 指标 | 值 |
|---|---:|
| strict schema | `true` |
| source artifact SHA exact | `true` |
| all source spans byte exact | `true` |
| occurrence recall | `1.0` |
| typed-edge recall | `9/13 = 0.692307…` |
| frozen-gold revisit identity | `false` |
| true merge two-parent recall | `1.0` |
| false merge count | `0` |

按旧evaluator规则，这一投影是`PARTIAL`。主要差异包括：候选把`e0→e3`直接标为`REVISIT`，而旧gold同时要求`e0→e3 BRANCH_FROM`和`e2→e3 REVISIT`；候选把terminal-case分支连到e3而不是e0；候选把e4→e5记为`CONTINUE`而不是`REFINE`。这些差异不能在看到结果后单方面改成PASS：它们既可能是抽取错误，也可能暴露“同一折返/分叉存在多种合法关系视图”的旧gold过窄问题。必须用预注册acceptable-set和独立审计解决。

---

## 5. 原始ATIF工具边界审计

原始`devin-export.json`为ATIF-v1.7，包含13个step，其中7次实际tool call：

| 类型 | 数量 | 目标/用途 |
|---|---:|---|
| `read` | 3 | 本次live workspace内的`AGENTS.md`、`problem.md`、`raw_solver_trajectory.txt` |
| `exec` | 2 | `cd`到同一workspace后用本地Python计算offset/hash、验证JSON/span/hash |
| `write` | 2 | 同一workspace内的`reasoning-trajectory.json`和`DONE.md` |

逐条检查arguments后：

- 所有绝对路径都在本次原始live workspace下；
- 没有访问repo、`system/assets/vein_analysis/`或`palyground/absorb/vein_analysis/`；
- 没有网络、Git、curl/wget/ssh、另一AI、resume/continue或破坏性命令；
- model-bearing steps的`generation_model`均为`glm-5-2`；
- workspace在finalize时整体rename到最终D盘bundle，原始export保留当时live路径是正确历史物证。

因此本轮tool boundary判定为`PASS`。

---

## 6. 发现的ATIF摘要解析缺陷

final receipt历史记录了：

```json
{"step_count": 0, "tool_event_count": 15}
```

但原始export的真实值是：

```text
steps = 13
actual tool calls = 7
```

根因是当时冻结的`inspect_export()`：

1. 只把含`step_type`/`event_type`的对象计为step，而ATIF-v1.7使用`step_id`+`source`；
2. 既累加`tool_calls`列表长度，又递归把每个`tool_call_id`再计一次，造成双计数。

这里必须分开裁决：

- 原始export完整、hash固定、可独立逐条审计，因此tool boundary本身可判PASS；
- 历史receipt的两个摘要计数字段不准确，判为`EXPORT_SUMMARY_COUNTER_ACCURACY=CONTRADICTED`；
- final bundle和receipt保持append-only，不得回写修正；
- 解析器修复已在VMS-38封存之后完成，新增ATIF-v1.7单测，并只在未来新run中生效。

这个缺陷不改变361号`SUPPORTED_WITHIN_DEBUG_CANARY`的显式判定条件，因为原始export合法、模型可观察且工具边界已经直接审计；但它阻止任何人把VMS-38 receipt中的0/15当成可靠统计数据。

---

## 7. 对361号逐项裁决

| 条件 | 结果 | 物证 |
|---|---|---|
| D站点与private tmux | PASS | launch receipt、D盘final bundle |
| POC/run/attempt身份一致 | PASS | `poc-vms-38-extractor-tmux-a1`贯穿全部receipt |
| 可读自身AGENTS与输入 | PASS | raw ATIF 3次read、pane capture |
| 严格输出与DONE | PASS | strict parser、span/hash复核、DONE receipt |
| exact effective model | PASS | `glm-5-2` / `GLM-5.2 High` |
| tool events无越界 | PASS | 原始13-step/7-call逐条审计 |
| 唯一退出干预后exit 0 | PASS | intervention 000000、snapshot 000006/7 |
| D盘原子封存 | PASS | final receipt与final目录 |
| 入题侧基线不变 | PASS | `9bb4fd…afd6b3` |

总判：`SUPPORTED_WITHIN_DEBUG_CANARY`。

---

## 8. 非主张与下一步

本轮不主张：

- Event Extractor已经资格化；
- AGENTS指令等同于OS sandbox；
- Devin暴露完整或忠实的内部thinking；
- 输出已通过独立数学语义审计；
- streaming、并发、故障恢复、数据库、Solver接入或全管线已完成；
- 可以把DEVELOPMENT_ONLY结果升级为确认性Evidence。

已完成的运行后工程动作：

- 修正ATIF-v1.7 step/tool计数器，现行解析结果为13/7；
- 新增精确计数回归，解题侧全量49项PASS；
- 对候选输出做旧冻结evaluator的事后投影，得到探索性`PARTIAL`，没有改gold或升级证据。

下一步顺序固定为：

1. 为事件关系建立预注册acceptable-set/多视图gold和独立审计协议；
2. 用新题/新raw trajectory运行Event Extractor资格化，而不是重跑VMS-38；
3. 再为normalizer和auditor建立各自的新资格化协议；
4. 只有三个角色都具备独立能力物证后，才讨论端到端live管线和流式增量POC。
