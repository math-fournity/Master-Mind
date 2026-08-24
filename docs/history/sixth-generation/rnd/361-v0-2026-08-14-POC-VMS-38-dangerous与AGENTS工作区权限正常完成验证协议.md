# POC-VMS-38：dangerous + AGENTS工作区权限的正常完成验证协议

**日期**：2026-08-14  
**状态**：`PREREGISTERED_NOT_STARTED`  
**用户裁决**：Devin CLI使用YOLO/`dangerous`模式，权限要求写入其workspace `AGENTS.md`  
**前序反例**：358号（VMS-36）、360号（VMS-37）  
**证据用途**：`DEVELOPMENT_ONLY`  

---

## 1. 本轮只修什么

VMS-37已经证明D卷、专属根、private tmux、no-sandbox、dangerous/bypass、`glm-5-2`和exact export可用。它没有完成角色任务，是因为同一份config显式禁止了`Read(/Volumes/**)`。

本轮仅引入三项预注册修订：

1. 删除`dedicated_devin_config()`中会阻断自身workspace的repo/Volumes广泛Read deny；
2. 把“只读本workspace允许输入、只写指定输出、不访问外部路径/网络/git/其他AI/破坏性命令”写入冻结角色`AGENTS.md`；
3. runner强制`--attempt-id=poc-vms-38-extractor-tmux-a1`，启动前机械验证它与POC ID精确一致。

不改task、题目、raw trajectory、事件Schema、tmux状态机、D盘落点、模型、退出协议、attempt数或科学评分。

---

## 2. 冻结权限档

| 字段 | 值 |
|---|---|
| carrier | Devin CLI interactive TUI in private tmux |
| model argument | `glm-5-2` |
| normalized effort | `high` by model UID |
| sandbox | `false` |
| permission mode | `dangerous` / expected effective `Bypass` |
| workspace | `/data/master-mind-solve-vein-data/poc-results/.<run>.tmux-live-<nonce>/workspace` |
| asset set | `solve-vein-assets-0.3.0` |
| role | `reasoning_event_extractor` |
| allowed reads | `AGENTS.md`, `TASK.md`, `problem.md`, `raw_solver_trajectory.txt`，以及运行器生成的本workspace配置/清单 |
| allowed writes | `reasoning-trajectory.json`, `DONE.md`, Devin export/runtime物证 |
| local execution | 仅允许Python/`shasum`用于offset、JSON验证和哈希 |
| forbidden | workspace外路径、网络、git、另一AI/agent、破坏性命令、参考解答、入题侧资产 |

`dangerous`/bypass只消除逐工具人工确认。本协议不把AGENTS说明冒充为OS sandbox；它要求运行后核对export中的tool events，若模型试图越过角色边界，则即使输出数学上正确也不能PASS。

---

## 3. 冻结身份与资源

| 字段 | 值 |
|---|---|
| `poc_id` | `POC-VMS-38` |
| `attempt_id` | `poc-vms-38-extractor-tmux-a1` |
| run ID | `poc-vms-38-dangerous-agents-tmux-20260814` |
| attempt / retry | `1 / 0` |
| allowed exit intervention | DONE后最多一次`/exit` + `Enter` |
| evidence lane | `DEVELOPMENT_ONLY` |
| DB / Redis / Solver | 不连接、不启动 |
| absorb-side | 冻结基线前后必须一致 |

VMS-38是新资产与新运行ID，不是VMS-36/37的retry。两个历史bundle不得移动、覆盖或重新裁决。

---

## 4. 运行时SOP

1. 执行48项解题侧回归，其中包含入题侧保护基线、资产hash、config不自拒绝和attempt ID精确绑定；
2. 验证freeze manifest的每个文件hash与D盘站点信息；
3. 仅启动一个Devin attempt；
4. 启动后立即snapshot，不在前台空等；继续处理未冻结文档，每个工作段结束后追加snapshot；
5. 未见DONE前不得向pane输入；
6. 见`DONE_WAITING_EXIT`时只允许一次记账的`/exit`+`Enter`；
7. pane dead后才finalize；未到DONE却idle、越界或出现新协议阻断时显式abort；
8. 不重试、不更换prompt、不开第二个model call。

---

## 5. 判定规则

### `SUPPORTED_WITHIN_DEBUG_CANARY`

必须全部成立：

- D站点preflight和private tmux PASS；
- receipt中POC/run/attempt身份一致；
- pane显示Devin成功读取自身AGENTS与输入，不再出现路径deny；
- 生成严格`reasoning-trajectory.json`与exact `DONE.md`；
- export合法，effective generation model仅含`glm-5-2`；
- tool events不包含workspace外路径、网络、git、另一AI或破坏性命令；
- 自然退出或唯一记账`/exit`+`Enter`后exit 0；
- D盘final bundle原子封存，且入题侧基线不变。

### `INCONCLUSIVE_PROTOCOL`

模型/载体/输出/export/退出链任一缺失，但没有越界或覆盖物证。

### `FAILED_DEBUG_CONTRACT`

出现任一以下情况：越出workspace、访问禁止信息、未记账pane输入、重试/第二attempt、身份不一致、覆盖历史run、D盘失效后fallback，或触碰入题侧。

---

## 6. 非主张

- 不资格化Event Extractor；
- 不评估生产数学质量；
- 不证明AGENTS指令等同OS sandbox；
- 不证明完整或忠实thinking可见；
- 不进入确认性证据；
- 不证明streaming、并发、崩溃恢复、DB、Solver或全管线已实现；
- 不授权修改入题侧代码、运行资产或历史实例。
