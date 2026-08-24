# 第六代系统证据与资格边界

**状态**：current
**最近验证**：2026-08-24，commit 基线 `8940e92`

## 当前实际测试结果

命令：

```bash
PYTHONPATH=. python3 -m pytest system/tests/solve_vein_analysis
```

环境：darwin、Python 3.14.6、pytest 9.1.1、pluggy 1.6.0。
结果：294 collected，294 passed，1 warning，13.29 秒。

警告来自 `test_event_extraction_qualification_runtime.py::test_source_tree_sha256`：测试函数返回字符串
而不是 `None`。这不改变本次 294 PASS，但属于测试质量债务；现有 293 计数文档均已过时。

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
294 项离线测试和相称的负向/fault 检查。任何 live、DB 或外部系统证据均需单独授权。
