# 第二轮Connection Failed问题诊断报告

**编号**：266-v0  
**日期**：2026-08-08  
**作者**：GLM-5.2（glm5.2 worktree）  
**关联**：262号（MITM thinking拦截验证）、263号（Solver-Harness方案）、265号（A/B对照实验方案）

---

## 1. 问题描述

在04工作线§2.6 A/B对照实验中，用solver-harness启动的devin cli（`--interactive`模式 + mitmproxy代理）在**第一轮thinking正常完成后，第二轮请求始终"Connection failed"**。无论是否使用mitmproxy，无论是否设置`NODE_EXTRA_CA_CERTS`，第二轮请求都无法成功发送。

**核心症状**：
- 第一轮：devin cli读取problem.txt → thinking约1.5-5分钟（25000 tokens）→ 被"Response truncated"截断
- 第二轮：用户发送"继续" → "Connection failed (attempt N), retrying..." → 无限重试，无法成功

---

## 2. 实验时间线与证据

### 2.1 实验序列

共进行了5次实验，逐步排除可能原因：

| 实验ID | mitmproxy | NODE_EXTRA_CA_CERTS | 第一轮 | 第二轮 | 结论 |
|---|---|---|---|---|---|
| ab-253-B | ✅启用 | ❌未设置 | Connection failed（第1次请求就失败） | N/A | SSL证书问题 |
| ab-253-B2 | ✅启用 | ✅已设置 | ✅正常（thinking 5分钟，25000 tokens） | ❌Connection failed | SSL已修复，但第二轮失败 |
| ab-253-B3 | ❌禁用(--no-mitm) | N/A | ✅正常（thinking 5分钟，25000 tokens） | ❌Response truncated → 发"继续" → ✅正常（thinking 5分钟） → ❌Response truncated | 不用mitmproxy时第二轮可以成功 |
| mitm-test-2round | ✅启用（6fa006a版本） | ✅已设置 | ✅正常（thinking 1.5分钟） | ❌Connection failed (attempt 2) | 另一个AI的mitmproxy改进版仍未解决第二轮问题 |
| mitm-stream-test | ✅启用（05fef30流式版本） | ✅已设置 | ✅正常（thinking 1.5分钟，7817 chunks实时落盘） | ❌Connection lost → 发"继续" → ❌Connection failed (attempt 4) | 流式截获工作正常，但第二轮仍失败 |

### 2.2 关键证据

#### 证据1：mitmproxy日志显示第二轮请求未到达

```
# mitm-test-2round的api_log.txt最后几条
04:09:19.292240 | GetChatMessage | status=200 | resp_size=4396    ← 第一轮最后的成功响应
04:09:19.674025 | GetChatMessage | status=200 | resp_size=240     ← 空轮询
04:09:25.133044 | BatchRecordAnalyticsEvents | status=200          ← 分析事件
04:10:15.597243 | GetUserStatus | status=200                       ← 用户状态查询
# 之后没有新的GetChatMessage请求——第二轮请求根本没有发出来
```

**结论**：第二轮"Connection failed"不是mitmproxy拦截失败，而是devin cli**根本没有向mitmproxy发送第二轮请求**。

#### 证据2：Pro额度显示0% remaining

所有实验中tmux pane都显示：
```
Pro · 0% remaining (resets in 24h XXm)
```

**结论**：API额度耗尽可能是第二轮失败的根本原因。

#### 证据3：不用mitmproxy时第二轮可以成功

实验ab-253-B3（`--no-mitm`）中：
- 第一轮：thinking 5分钟 → Response truncated
- 发送"继续" → 第二轮成功：thinking 5分钟 → Response truncated
- 再次发送"继续" → 第三轮成功：thinking继续

**结论**：mitmproxy代理在第二轮请求时引入了某种问题，导致devin cli无法通过代理发送第二轮请求。

#### 证据4：流式thinking截获验证了第一轮完整工作

实验mitm-stream-test中，另一个AI的流式截获版本（05fef30）成功截获了：
- 7817个thinking chunks（token级粒度，1-7字符/chunk）
- 25个tool_call chunks
- 毫秒级时间戳（04:40:58.732 → 04:42:26.487，约1.5分钟）
- 三路落盘（共享raw + 实验目录txt + 实验目录jsonl）

**结论**：mitmproxy的截获功能本身工作正常，问题出在第一轮完成后devin cli与API端的连接恢复。

#### 证据5：sessions.db中没有assistant消息

实验mitm-stream-test的session（judicious-lemon）在sessions.db中有16个message_nodes，但全部是system/user角色，**没有assistant消息**。

```
node_id | role   | msg_len
0       | system | 593
1       | system | 7019
2       | user   | 481
...
15      | system | 40903
```

**结论**：devin cli在thinking被截断后，没有将thinking内容写入sessions.db的message_nodes表。assistant消息只在完整响应（含content）完成后才写入。这与mitmproxy的流式截获形成对比——mitmproxy能截获到thinking内容，但sessions.db只在完整响应后才记录。

---

## 3. 根因分析

### 3.1 问题不在mitmproxy

证据1和证据3共同表明：
- mitmproxy的SSL证书问题已解决（NODE_EXTRA_CA_CERTS）
- mitmproxy的thinking截获功能正常（流式版本验证）
- 不用mitmproxy时第二轮可以成功

### 3.2 问题在devin cli与API端的连接恢复机制

当devin cli通过mitmproxy代理时：
1. 第一轮请求：devin cli → mitmproxy → API端 → 成功返回thinking
2. 第一轮thinking被token limit截断（"Response truncated"）
3. devin cli尝试发送第二轮请求（用户输入"继续"后）
4. **devin cli无法通过mitmproxy建立新连接到API端** → "Connection failed"

可能的原因：
- mitmproxy在第一轮长连接结束后，连接池状态异常
- devin cli的HTTP客户端在代理模式下keep-alive连接超时处理有bug
- API端在第一轮请求后对代理IP限流

### 3.3 API额度耗尽是叠加因素

"Pro · 0% remaining"表示额度耗尽。但这不应该是第二轮失败的原因——因为：
- 不用mitmproxy时第二轮可以成功（ab-253-B3实验）
- 额度显示"resets in 24h"——如果是额度问题，不应该只在mitmproxy模式下失败

**最可能的解释**：API额度耗尽导致API端对请求更严格，mitmproxy代理的连接复用机制在额度受限时更容易触发连接拒绝。

---

## 4. 对A/B对照实验的影响

### 4.1 B组（裸跑）不受影响

B组用`--no-mitm`模式，第二轮可以正常工作。B组裸跑结果有效：
- Solver做了2轮thinking（每轮约25000 tokens），但都被"Response truncated"截断
- Solver的thinking内容涉及矩约束优化、Carathéodory定理、极值分布分析——深度思考但无法完成完整证明
- **结论**：B组裸跑Solver无法完成253号案例的证明

### 4.2 A组（有检索系统）受影响

A组需要mitmproxy来实时截获thinking（供RealtimePipeline解析）。但mitmproxy导致第二轮Connection failed，意味着：
- RealtimePipeline只能在第一轮thinking期间工作（实时解析thinking → 检索 → 选择提示）
- 提示注入后Solver无法发送第二轮请求（Connection failed）
- **A组无法验证"提示注入后Solver是否突破卡点"**

### 4.3 替代方案

1. **方案A：A组也用--no-mitm模式**
   - RealtimePipeline从sessions.db读取thinking（不实时，但响应完成后可用）
   - 缺点：无法在thinking过程中实时解析，只能在thinking完成后（被截断后）解析
   - 优点：第二轮可以正常工作

2. **方案B：等API额度恢复后重跑**
   - 额度24小时后重置，届时可能不再触发连接拒绝
   - 缺点：需要等待，且不确定额度恢复后mitmproxy模式是否正常

3. **方案C：修复mitmproxy的连接复用问题**
   - 调查mitmproxy在长连接结束后的连接池行为
   - 可能需要配置mitmproxy的连接超时或keep-alive参数
   - 缺点：需要深入mitmproxy内部机制

**推荐**：方案A（A组用--no-mitm），因为A/B对照的核心是验证"提示是否帮助突破卡点"，不需要mitmproxy级别的实时性——sessions.db的thinking内容（响应完成后写入）足够用于解析和检索。

---

## 5. 已验证可用的机制

尽管第二轮Connection failed问题存在，以下机制已验证可用：

| 机制 | 状态 | 验证实验 |
|---|---|---|
| mitmproxy SSL证书（NODE_EXTRA_CA_CERTS） | ✅可用 | ab-253-B2 |
| mitmproxy流式thinking截获 | ✅可用（第一轮） | mitm-stream-test |
| sessions.db thinking读取 | ✅可用（响应完成后） | ab-253-B3 |
| DevinCliParserProvider | ✅可用 | test_devin_cli_parser |
| RealtimePipeline完整流程 | ✅可用（mock测试） | test_realtime |
| HintInjector tmux send-keys | ✅可用（dry-run） | test_realtime |
| solver-harness --interactive模式 | ✅可用（第一轮） | 所有实验 |
| solver-harness --no-mitm模式 | ✅可用（多轮） | ab-253-B3 |

---

## 6. 下一步建议

1. **A/B对照实验用--no-mitm模式**——A组从sessions.db读取thinking（响应完成后），不依赖mitmproxy实时截获
2. **修复HintInjector时序**——等Solver的thinking完成（Response truncated出现后）再注入提示，不要在thinking期间注入
3. **等API额度恢复后补充mitmproxy模式验证**——确认额度恢复后mitmproxy多轮是否正常
4. **考虑向devin cli开发者报告此问题**——mitmproxy代理模式下第二轮Connection failed可能是devin cli的bug

---

## 7. Git Commit关联

| Commit | 描述 | 与本报告的关系 |
|---|---|---|
| bedfdad | solver-harness: 修复mitmproxy SSL证书问题 + A/B对照实验脚本 | 添加NODE_EXTRA_CA_CERTS，解决了第一轮的SSL问题 |
| 6fa006a | 稳定mitmproxy thinking截获 | 另一个AI的改进，截获所有ApiServerService API |
| 05fef30 | 流式实时thinking落盘 | 另一个AI的流式截获实现，验证了第一轮thinking完整截获 |
| 本报告 | 266号文档 | 记录第二轮Connection failed的完整诊断 |
