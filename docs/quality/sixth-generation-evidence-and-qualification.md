# 第六代系统证据与资格边界

**状态**：current
**最近验证**：2026-08-24，当前目录迁移与历史绑定解析 diff

## 当前实际测试结果

命令：

```bash
PYTHONPATH=. python3 -m pytest system/tests/solve_vein_analysis
```

环境：darwin、Python 3.14.6、pytest 9.1.1、pluggy 1.6.0。
结果：297 passed，62 subtests passed，0 warning，16.93 秒。

原 warning 来自把辅助函数 `test_source_tree_sha256` 直接导入测试模块后被 pytest 误收集；现在使用
非 `test_` 别名，辅助函数不再冒充测试。新增 3 个历史绑定负向/迁移测试，净测试数由 295 变为 297。

## Protected absorb baseline 版本

- historical v1 digest=`9bb4fd2551d13f196610ddf8e203ad96b0855f3337f6c4e6502f6c764eafd6b3`，
  继续由冻结 VMS receipts 引用，文件和 receipts 均不修改；
- current v2 digest=`2085e1c91bac1909b01ab3dd74f0845b9d2484b77e34d0a7cb9f2357f0b5f3a7`，
  仍覆盖同一 161 path，只更新 13 个经审计的 current docs/ref/ai-check/V10 schema 描述；
- current v3 digest=`3789a3137aa5bcd31514f63d8f34c7bd17996f728c5ee9b2e2517a57394787c1`，
  仍覆盖同一 161 path，记录 Prompt/R&D/spec 迁移引起的 9 个受保护路径变化；
- historical validator 对已演进的 frozen path 从固定 commit `3b26684` 读取旧 blob，93 个绑定预核
  0 mismatch；错误 blob 的新增负向测试 fail-closed。

冻结 manifest 的旧 path identity 不改写。解析器先核 canonical current path 的同字节文件，再核固定
Git blob；symlink、缺失 blob、错误 hash/size 均 fail-closed。这使 current isolation protection 可以
演进，同时保持 historical freeze 可逐字节复核；不得用 v2/v3 替换历史 receipt 中的 v1 identity。

## PASS 支持什么

- strict structured trajectory 和 Reasoning DAG 合同；
- state/transition FCA、Next Closure 与 brute-force oracle 对照；
- RCA-style relational scaling 和 deterministic TraceRecord；
- batch/incremental scientific fingerprint 等价；
- CLI asset 校验、保护路径、append/atomic output 和失败清理；
- Event Extractor V1/V2 的离线 parser/evaluator、file-effect audit 和冻结包；
- State Normalizer、hidden join、reviewer object、final receipt、unseen pack 和 DAG sidecar；
- Trace Auditor 的结构 family 和 fail-closed 边界；
- tmux/role runtime 的模拟、preflight 和不可消费 permit 合同。

## PASS 不支持什么

- raw natural-language thinking 能被可靠抽取为 structured events；
- 远程模型、Devin、Solver、ArangoDB 或 Redis 当前可运行；
- Event Extractor、State Normalizer 或 Trace Auditor 模型角色已资格化；
- Tell/Hint 具有因果效果；
- Trace 两类合同已经统一；
- 推理树、引导树或 Grove 闭环已实现；
- streaming、恢复、规模性能、成本或生产部署已验证。

## VMS 证据分层

| 范围 | 当前 verdict | 可支持主张 |
|---|---|---|
| VMS-28 系列 | 历史 POC success/partial | absorb 侧 Prompt 和格化方法的历史选择依据 |
| VMS-31 | PASS within frozen structured cases | DAG/FCA/RCA-style 离线结构 |
| VMS-32 至 37 | 多数 INCONCLUSIVE/ABORTED | 权限、workspace、tmux 和载体失败定位 |
| VMS-38 | SUPPORTED_WITHIN_DEBUG_CANARY / DEVELOPMENT_ONLY | 冻结 debug canary，不是角色资格 |
| VMS-39 | 冻结 profile 下控制面边界 | 不能把 AGENTS 当知识库 |
| VMS-40 | deterministic offline PASS | 多视图/多轴 acceptable-set 机械合同 |
| VMS-41 | 0/4，INCONCLUSIVE_PROTOCOL / NOT_QUALIFIED | artifact/replay 和失败定位；不支持确认性 PASS |
| VMS-41R1 | zero-model chain PASS / LIVE_NOT_AUTHORIZED | V2 包和合并合同；不资格化模型 |
| VMS-42 | zero-model State Normalizer chain PASS | 离线多轴归一化合同 |
| VMS-43 | structural zero-model PASS | 已结构化 DAG 的 Trace family 审计 |

## 资格门

实现、离线验证、development canary、blind manual audit、hidden join、模型资格和生产接入是不同门。
当前 `authorized_live_attempts=0`，LiveRunPermit 不可消费。只有新的明确用户授权、全新 attempt ID、
冻结角色/模型/Prompt/tool/context、public/hidden 隔离、独立盲审和 final receipt 全部闭合后，才可进行
真实资格实验。

## 保留失败

VMS-41 失败、协议中断、旧 parser 计数错误和所有 sealed negative evidence 必须保留。历史 receipt
不可为修正文档而回写；修正只能进入新代码、新测试和 replacement note。

## 重建验收

文档批次至少运行 governance validator、`git diff --check` 和链接/path 检查。代码或合同变化再运行
297 项离线测试和相称的负向/fault 检查。任何 live、DB 或外部系统证据均需单独授权。
