# POC-VMS-36：Devin tmux 交互可观测与正常退出 Canary 协议

**日期**：2026-08-14  
**状态**：`PREREGISTERED_NOT_STARTED`  
**证据用途**：`DEVELOPMENT_ONLY`  
**实现对象**：`system/solve_vein_analysis/tmux_runtime.py`  
**理论与运行档来源**：353、355号文档  

---

## 1. 要回答的唯一问题

入题侧已经证明 tmux 交互运行便于观察 Devin 的 TUI、thinking spin 和文件生成，但其旧实现把 prompt 插入 shell 字符串，并可能在看到 `DONE.md` 后过早终止、丢失 export。

本 Canary 只回答：解题侧独立的 `INTERACTIVE_TMUX_DEBUG` 运行档，能否在不修改入题侧任何对象的前提下：

1. 用私有 tmux socket/session 直接启动 Devin CLI；
2. 在进程仍运行时封存可读 pane capture 与健康 snapshot；
3. 观察候选输出和 `DONE.md`，但不以 DONE 触发 kill；
4. 通过自然退出，或一次已记账的 `/exit` + `Enter`，使进程正常结束；
5. 在进程结束后保留可解析 export、exact model UID 和完整工作目录。

它不评估抽取数学质量，不资格化 Event Extractor，也不进入任何确认性 EvidenceRecord。

---

## 2. 冻结运行单元

| 字段 | 冻结值 |
|---|---|
| `poc_id` | `POC-VMS-36` |
| `run_id` | `poc-vms-36-tmux-canary-20260814` |
| 角色 | `reasoning_event_extractor` |
| 角色资产 | 当前 `AGENTS_event_extractor.md`，其字节与0.1.0相同 |
| 输入 | VMS-32的 `problem.md` 与 `raw_solver_trajectory.txt` |
| 输出 | `reasoning-trajectory.json` + exact `DONE.md` |
| carrier | Devin CLI interactive TUI in tmux |
| requested model | `glm-5-2` |
| normalized effort | `high`，由 model UID 编码 |
| sandbox | `false` |
| permission mode | `dangerous` |
| attempt | 1 |
| scientific retry | 0 |
| infrastructure retry | 0 |
| evidence lane | `DEVELOPMENT_ONLY` |

启动前必须生成 `poc_vms_36.freeze.json`，逐文件冻结本协议、runner、两个 runtime、角色资产和两份输入。freeze 只在首次启动前生成；模型调用后不得更新。

---

## 3. 观察与退出协议

1. `start` 后立即记录 launch receipt 和第一份 snapshot；
2. 不用前台 sleep 空等。运行期间继续修订不影响冻结输入的技术文档；每完成一个实际工作段，再追加 snapshot；
3. 至少保留一份进程活着时的非空 pane capture；
4. 若 Devin 自然退出，直接进入 finalize；
5. 若出现 `DONE_WAITING_EXIT`，允许且只允许一次 intervention：按顺序发送 literal `/exit` 与 `Enter`；
6. intervention 后最多观察 60 秒，不发送第二种退出命令；
7. 若仍未退出，追加最终 snapshot，执行一次显式、归因的 private tmux server abort；不得删除目录，不得再开第二个 Devin attempt。

任何人工 attach 都只能观察。若在 attach pane 中输入了未通过 API 记账的字符，本次协议立即为 `INCONCLUSIVE_PROTOCOL`。

---

## 4. 预注册判据

### 4.1 `SUPPORTED_WITHIN_DEBUG_CANARY`

同时满足：

- launch exit 0，且 launch receipt 证明没有 shell interpolation；
- private socket/session 可被机器 snapshot 定位；
- 至少一份 live pane capture 非空并能看出 Devin 正在运行；
- 输出、DONE、export 均存在；
- DONE 精确等于 `reasoning-trajectory.json SHA256=<actual>`；
- export 是合法 JSON，所有 generation-bearing step 的 model UID 可观察为 `glm-5-2`；
- pane 最终 dead，exit status 为 0；
- 若发生 intervention，恰好一条记录，keys 恰好为 `[/exit, Enter]`；
- final receipt 在进程退出后生成，bundle 原子封存。

### 4.2 `INCONCLUSIVE_PROTOCOL`

任一关键物证缺失、model 不可观察/不匹配、DONE 非精确、export 缺失/不可解析、未记账输入、正常退出失败或只能 abort。

### 4.3 `FAILED_DEBUG_CONTRACT`

实现使用 shell 插值、触碰入题侧对象、覆盖既有 bundle、看到 DONE 后未经协议直接 kill，或开启第二个 model attempt。

数学内容无论好坏都不改变本 Canary 的 verdict；内容只能作为后续 gold/角色协议设计素材。

---

## 5. 明确非主张

- 不证明 thinking spin 是完整 chain-of-thought；
- 不证明 pane capture 等于 ATIF/export；
- 不证明 no-sandbox + dangerous 的安全隔离；
- 不证明 Event Extractor 数学正确或可泛化；
- 不证明可用于确认性实验；
- 不证明 streaming、reattach、并发、数据库或真实 Solver 已实现；
- 不改变 POC-VMS-35 的 `INCONCLUSIVE_PROTOCOL` 结论。

---

## 6. 保护边界

下列对象在本实验前后必须逐哈希不变：

- `system/vein_analysis.py`；
- `system/process_absorb.py`；
- `system/assets/vein_analysis/`；
- `palyground/absorb/vein_analysis/`；
- `.devin/rules/`。

本实验不连接 ArangoDB/Redis，不启动目标 Solver，不写 Seven System，不改入题侧管线使用的任何 `AGENTS.md`。
