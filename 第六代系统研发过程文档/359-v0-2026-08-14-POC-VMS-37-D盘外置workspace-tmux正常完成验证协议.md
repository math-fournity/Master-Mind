# POC-VMS-37：D盘外置workspace的tmux正常完成验证协议

**日期**：2026-08-14  
**状态**：`PREREGISTERED_NOT_STARTED`  
**前序反例**：358号 / POC-VMS-36  
**证据用途**：`DEVELOPMENT_ONLY`  

---

## 1. 单一修订假设

VMS-36已经支持tmux实时可观测，但repo内workspace被专用config的repo deny规则拒绝。本轮只修订物理落点：

```text
VMS-36: <repo>/system/tests/.../poc_results/.<run>.tmux-live/workspace
VMS-37: /data/master-mind-solve-vein-data/poc-results/.<run>.tmux-live/workspace
```

角色prompt、题目、raw trajectory、Devin model、permission、sandbox、tmux runtime语义、一次attempt和退出协议保持不变。若D盘外置workspace使角色完成，则支持“VMS-36失败定位在路径/权限组合”，而不是支持全部角色能力。

---

## 2. D盘站点冻结

启动前已按D卷README同步规则确认：

- 挂载点：`/data`；
- 文件系统：APFS；
- Volume UUID：`C293C841-DD80-4EFF-9AE4-EA7D826FBE20`；
- 设备：本次观测`disk7s1`，但设备号不作为持久身份；
- 可用空间：约780GiB；
- `/data/README.md` SHA-256：`fee07273d29357edf9b3f46c05ea6f9b8651d2180e8c6593345f85621347820a`；
- 专属根README SHA-256：`43730e88ad9715ff7f584227b0bf8ca0c923dd6b888c041c744ff01ce8fce473`；
- `poc-results/`与D卷的`st_dev`相同；
- 专属根、`poc-results/`均不是symlink，权限意图为`0700`。

这个物理根不提供强安全证明，但可防止模型自身workspace落入主repo deny范围，并使live bundle到final bundle保持同一文件系统。

---

## 3. 冻结运行单元

| 字段 | 冻结值 |
|---|---|
| `poc_id` | `POC-VMS-37` |
| `run_id` | `poc-vms-37-d-volume-tmux-20260814` |
| 输出根 | `/data/master-mind-solve-vein-data/poc-results/` |
| 角色 | `reasoning_event_extractor` |
| 资产/输入 | 与VMS-36相同 |
| task | 与VMS-36相同 |
| carrier | Devin CLI interactive TUI in private tmux |
| model | `glm-5-2` / High by UID |
| sandbox | `false` |
| permission | `dangerous` |
| attempt/retry | 1 / 0 |
| evidence lane | `DEVELOPMENT_ONLY` |

VMS-37使用新的freeze manifest和新的run ID，不是VMS-36 retry。VMS-36 bundle不移动、不覆盖、不重新裁决。

---

## 4. 运行时动作

1. runner先验证repo内freeze，再验证D盘mount、两份README哈希、专属根非symlink、同一`st_dev`和output范围；
2. 启动后立即snapshot；
3. 不在前台空等，继续完善非冻结文档；每个工作段后追加snapshot；
4. 看到DONE前不得输入；
5. 若自然退出，直接finalize；若`DONE_WAITING_EXIT`，只发送一次已记账`/exit` + `Enter`；
6. 若没有DONE且任务已停在idle，或唯一退出动作后60秒仍不退出，显式abort；
7. 不重试、不换prompt、不补第二个model调用。

---

## 5. PASS / INCONCLUSIVE / FAIL

### `SUPPORTED_WITHIN_DEBUG_CANARY`

- D站点preflight全部PASS；
- private tmux launch与至少一份live capture PASS；
- 模型能读取自身AGENTS/inputs，不再出现repo deny；
- 生成`reasoning-trajectory.json`与exact DONE；
- export合法，effective generation model只含`glm-5-2`；
- 自然退出或唯一一次已记账`/exit`后exit 0；
- final bundle在D盘同设备原子rename完成。

### `INCONCLUSIVE_PROTOCOL`

模型/载体/权限/输出/export/退出任一关键链缺失，但实现未违反硬边界。

### `FAILED_DEBUG_CONTRACT`

输出逃出批准D根、D掉线后fallback、shell插值、未记账输入、覆盖历史run、触碰入题侧或开启第二attempt。

---

## 6. 非主张

- 不资格化Event Extractor；
- 不评估数学质量；
- 不证明no-sandbox安全；
- 不证明完整thinking可见；
- 不进入确认性证据；
- 不证明streaming、并发、恢复、DB或Solver接入；
- 不证明未来生产workspace必须使用这个具体目录名。

---

## 7. 保护边界

沿用VMS-36的入题侧保护清单。实验前后必须通过`protected_absorb_baseline.sha256`逐文件验证。本轮不修改入题侧代码、运行资产、历史实例或任何入题侧`AGENTS.md`。
