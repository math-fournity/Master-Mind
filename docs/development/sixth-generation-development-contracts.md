# 第六代系统开发合同

**状态**：current
**替代来源**：旧 `.devin/rules/six-*`、`system-ref-sync.md` 和相关项目规则。
**边界**：本文只保留与当前第六代 repo、代码和测试一致的规则；旧规则通过安全 tag/Git 恢复。

## 代码三件套

`system/` 下每个受治理的 Python 模块必须有同名 `.ref` 和 `.ai-check`：

- `.py`：实际实现；
- `.ref`：建立模块认知所需的 current 文件路径，每行一个 repo-relative path；
- `.ai-check`：代码无法机械判定的语义、证据和运行审计 checklist。

修改模块职责、接口、Prompt、schema、证据或参考路径时，必须同步审查三件套。`.ref` 的非注释路径
必须存在、唯一并优先指向 current canonical docs；历史原因通过 `docs/history/` 或 Git pointer 路由，
不得依赖即将移出工作树的旧根目录。

冻结 fixture、sealed `poc_results/` 和外部工具原样副本中的 Python 文件是不可变证据成员，不因扩展名
成为 current module；不得为了补 sidecar 而改变其封存 file set。它们由上层 manifest、README、hash
和 historical binding 统一治理。三件套完整性检查应显式排除这些 immutable evidence subtrees。

## 代码检查与 AI 审计

能由代码机械判定的事项全部进入 assertions、schema、hash、exact-set、oracle、negative/fault tests。
需要语义判断的事项才进入 `.ai-check`。测试 PASS 只覆盖其断言和环境；Prompt 或 checklist 出现某个
词不证明对应行为发生。

AI 审计必须读取 `.ref`、代码、`.ai-check` 和公开运行证据，区分实现、离线验证、development
canary、manual audit、live qualification 和 runtime observed。不得索取或制造隐藏 chain-of-thought。

## Prompt 与运行资产

- canonical Prompt source：`prompts/`；
- runtime copies：`system/assets/`；
- current AI/role/isolation contract：`docs/ai/sixth-generation-runtime-and-prompt-contracts.md`；
- POC 和演进证据：`docs/history/sixth-generation/rnd/` 与 `evidence/history/`。

修改行为相关 Prompt 时必须同步 source、runtime copy、版本/manifest、受影响代码常量和验证状态。
当前 absorb active versions 是 V5/V7/V8/V10；历史 V9 不得冒充 active。

## Runtime 启动边界

legacy absorb 代码会使用 tmux/Devin、工作目录、DB 和归档写入，但默认无执行授权。`dangerous`、
no-sandbox 或 yolo 只是历史/开发执行档，不是安全隔离证明。项目 `AGENTS.md` 不得自动进入 runtime
worker context；角色、可见输入、禁止知识、tool 权限、model UID、Prompt、attempt 和 output identity
必须冻结并由原始 events/receipts 证明。

任何真实 DB、Devin、tmux live role、Solver、网络或外部系统动作都需要当前用户明确授权。

## 运行痕迹和证据

行为相关输入、输出、trajectory、tool events、Prompt/version、model/profile、时间、hash、失败类型和
receipt 必须可追溯。sealed/frozen evidence append-only；历史 attempt ID 不重跑，历史 receipt 不回写。
大 run body 在 D 盘，Git 保存 pointer、manifest、hash、小 fixture 和解释结论。

基础设施、协议/盲性、tool/orchestration、模型能力和数学正确性失败分轴记录。失败和 negative evidence
不得因迁移或追求绿色结果而删除。

## 测试和保护基线

- 测试从 current requirement/design claim 推导，不从现有测试反推完整规格；
- 代码/合同变化运行相称 unit、contract、negative、fault、replay 和 full regression；
- current solve-side 命令：`PYTHONPATH=. python3 -m pytest system/tests/solve_vein_analysis`；
- historical v1 absorb baseline 保持不可变；current baseline 版本化，不能移动球门；
- historical validator 从 pinned Git commit 复核已演进旧字节，current isolation test核 current baseline。

## Git 和迁移

文件变化前执行 baseline check；只 stage 精确 pathspec。移动或删除前源文件必须有可恢复 commit/tag，
并在 migration map 记录 old path、new path/history pointer、action、reason、recoverability 和 evidence。
不 push、不改写历史。

## 完成检查

1. 受影响 `.py/.ref/.ai-check` 同步；
2. 所有 `.ref` target 存在且无待移除根依赖；
3. Prompt/source/runtime/version/evidence 对齐；
4. secret、answer、holdout 和项目治理未泄漏进 runtime；
5. 测试、失败和残余未知准确记录；
6. governance validator、`git diff --check` 和相称测试通过。
