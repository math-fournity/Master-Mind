# 第六代系统运行边界

**状态**：current
**默认权限**：只读调查和无外部副作用的本地验证。

## 默认允许

- 读取代码、Prompt、fixtures、manifest、Git diff 和 D 盘指针元数据；
- 运行 governance validator、`git diff --check`、安全的 `py_compile`；
- 运行 `system/tests/solve_vein_analysis` 的离线测试；
- 对全新临时目录运行明确标记为 zero-model/offline 的纯本地工具；
- 使用 explicit pathspec 进行本地 Git stage/commit。

## 默认禁止

- 连接或写入 ArangoDB/Redis；
- 启动 `system/vein_analysis.py`、Devin、tmux live role、Solver batch 或外部系统；
- 消费 LiveRunPermit、创建真实 qualification attempt 或重跑已消费 attempt ID；
- push、发布、改写 Git 历史；
- 显示 416 文档中的 credential-like 值；
- 把 repo 根 `AGENTS.md` 复制进 runtime worker workspace。

## 运行路径差异

### Legacy absorb 侧

`vein_analysis_three_phase(process="absorb")` 会创建 repo 内 `palyground/` 工作目录，启动 tmux/Devin，
写 DB 记录，并把部分产物归档到 `system/tests/vein_analysis/runs/`。它是有副作用的开发运行路径，
当前没有安全 dry-run，也不应在治理重建中启动。

### Solve-side offline CLI

`system.solve_vein_analysis.cli` 从已经结构化的轨迹开始，不调用模型、DB 或 Solver。输出必须是不存在
的新目录；成功使用 atomic rename，失败清理 partial。它仍会写本地文件，因此验证时使用显式临时
目录，不得指向 repo 根、absorb 保护路径或 symlink。

### Solve-side development runtime

`role_runtime.py` 和 `tmux_runtime.py` 能描述或启动 Devin/tmux 档位，但只有 preflight、模拟和冻结
canary 获得当前证据。真实执行必须有新的用户授权、冻结 attempt 和 D 盘 evidence root。

## 存储根

- curated Git knowledge：`knowledge/`；
- 大语料和题库：`/data/master-mind-glm5.2-worktree-external-data/2026-08-24/`；
- solve-side 大 POC 证据：`/data/master-mind-solve-vein-data/`；
- legacy ignored runtime：`palyground/`、`runs/`、`system/logs/`；
- canonical in-repo evidence 入口：`evidence/README.md` 和 `system/tests/`。

## 失败分类

运行报告必须区分：输入/schema 失败、asset drift、权限/隔离失败、provider/auth/rate/connection、
timeout/截断、tool/subprocess、orchestration、模型能力、数学正确性、协议/盲性破坏。不得把基础设施
或协议失败写成模型科学失败，也不得把 debug canary success 写成 qualification success。

## 恢复和不可变性

- sealed bundle、frozen manifest、raw export 和历史 receipt append-only；
- process-start 失败也要保留 deterministic partial/quarantine receipt；
- 历史 VMS-38 receipt 的旧计数错误不回写，现行解析器修正只影响未来产物；
- 目录迁移依靠 `pre-sixth-gen-current-repo-2026-08-24` 和 path migration map 恢复；
- 任何 destructive cleanup 必须有可恢复基线和明确用户授权。
