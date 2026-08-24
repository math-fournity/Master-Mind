# 第六代系统 AI 运行与 Prompt 合同

**状态**：current
**事实边界**：Prompt 和角色文件证明配置存在；只有 trajectory、tool events、receipts 和测试能证明行为。

## 角色分离

| 角色 | 可见输入 | 责任 | 当前状态 |
|---|---|---|---|
| 开发/Master AI | repo 治理、代码、测试和公开证据 | 设计、实现、审计和治理 | 受根 `AGENTS.md` 约束 |
| absorb Parser AI | 解答文本和对应运行资产 | 格化、形式上下文、Trace 识别 | 历史实现；当前未 live 复验 |
| solve-side Event Extractor | 冻结 raw/source 输入和角色资产 | 候选事件抽取 | VMS-41 NOT_QUALIFIED；R1 live 未授权 |
| State Normalizer | 候选事件和公开字典/合同 | 多轴状态归一化 | 离线合同已验证，模型角色未资格化 |
| Trace Auditor | 已结构化 DAG 和可选 sidecar | 结构 trace family 审计 | 离线合同已验证，模型角色未资格化 |
| 人工 Reviewer | 盲审包，不可见 hidden acceptable set | 独立语义判断 | 合同/模拟已实现，无真实当前 review |
| hidden evaluator | candidate、hidden set、冻结 hash | 机械合并和 fail-closed 判定 | 离线实现，不代表模型能力 |

## Prompt 资产

absorb 侧当前代码使用 `V5/V7/V8/V10` 和 synthesis Prompt：

- 完整演进文本：`prompts/absorb/`；
- 运行模板：`system/assets/vein_analysis/`；
- 历史 POC 与设计理由：`docs/history/sixth-generation/rnd/`。

三处必须保持 source/version/evidence 对齐。V9 文本和 `AGENTS_V9.md` 是历史资产；当前代码常量和
active template 指向 V10。Prompt 内容不能代替实际 Devin 调用、输出、export 或质量审计。

solve-side 角色资产位于 `system/assets/solve_vein_analysis/`，并有 0.2.0 至 0.4.1 release。当前
Event Extractor 候选资产是 0.4.1；不同 release 不得在一个资格 attempt 中混用。

根 `prompts/README.md` 只是当前入口。在迁移表闭合前不复制 Prompt body，以免形成第二份当前真值。

## 隔离和权限

- 项目治理 `AGENTS.md` 不得自动进入 runtime worker context。
- 每次资格 attempt 使用独立 workspace、config、export、attempt ID 和冻结资产 hash。
- `dangerous` 或 no-sandbox 只描述执行档，不是安全或文件系统隔离证明。
- runtime 仍必须禁止网络、嵌套 AI、Git 和破坏性命令，并用 tool events 和 file-effect audit 证明。
- gold、expected、hidden rubric、答案和测试 oracle 不得进入 candidate workspace。
- 用户级 Devin `AGENTS.md` 若属于冻结可见控制面，必须记录 sanitized path、size 和 SHA；不得复制 secret。

## Trajectory 和完成语义

- ATIF/trajectory 需要版本、顺序、tool call/result、source 和完整性证据。
- DONE 文本必须绑定实际输出 SHA，额外 prose 不能被静默接受。
- timeout、预算/上下文截断、provider/auth/rate/connection、tool、orchestration、模型能力和数学错误
  是不同失败类型。
- candidate 自报 verdict 不能进入机械真值。
- raw thinking 或 hidden chain-of-thought 不是治理交付物；只保留合法可公开的 trajectory 和 artifacts。

## 资格与 Eval 边界

VMS-38 只支持冻结 debug canary，VMS-39 只支持冻结 profile 的控制面上限，VMS-40 只支持确定性
离线合同。VMS-41 的冻结机械结果是 0/4、`INCONCLUSIVE_PROTOCOL / NOT_QUALIFIED`；事后审计
只可用于 failure localization。

VMS-41R1、VMS-42 和 VMS-43 的零模型包、合同、hidden join 和模拟收据不资格化模型。当前没有
可消费 LiveRunPermit，`authorized_live_attempts=0`。任何真实模型执行必须取得新的明确用户授权。
