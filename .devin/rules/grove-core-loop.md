---
description: >
  Grove核心循环认知——系统与推理AI并行运行，三个推动关系必须都成立。
  启动树生长引擎/运行POC-VMS实验时，AI自动进入辅助智能体（系统Pipe）角色：
  实时采集thinking、实时整理两棵树、在节点上检索方向、构造脉络、启动新AI。
  核心判定：如果只有解题树在长（节点在增长）但引导树没有生成新边（没有检索、没有启动新AI），
  循环只转了半圈——必须修复，让循环完整转起来。
  WHEN to use: 启动树生长引擎、运行POC-VMS实验、任何涉及两棵树生长的场景。
  WHEN NOT to use: 单AI串行解题（非树生长模式）、非数学实验。
trigger: always-on
---

# Grove核心循环rule

## 核心循环

```
引导树（给方向Q）→ 推理AI（探索）→ 解题树（记录结果）
                                    ↓
                              在终点节点检索
                                    ↓
                              引导树（新边=新方向Q）→ 启动新推理AI → ...
```

**三个推动关系**（必须都成立，循环才算完整转起来）：
1. **引导树→推理AI**：构造脉络（从根到当前节点的路径+方向Q），给推理AI作为输入
2. **推理AI→解题树**：采集thinking（从sessions.db），增量提取节点写入树
3. **推理AI→引导树**：AI终止后在终点节点检索方向Q，启动新AI——引导树长出新边

**循环只转了半圈的判定**：节点在增长但tree_edges为空，或叶节点retrieval_done全为False——推动关系3没做。

## 辅助智能体角色（系统Pipe）

运行树生长引擎时，AI是辅助智能体，不是旁观者。职责：
1. 实时采集——读sessions.db的message_nodes表（替代MITM，见sessions_db_reader.py）
2. 实时整理两棵树——从thinking增量提取节点写入ArangoDB
3. 在节点上检索方向——用retriever.py在叶节点检索Pattern
4. 构造脉络——从根到叶节点的路径+方向Q
5. 启动新AI——通过solver-harness launch
6. 检查停机——leaf_success时标记problem solved
7. 并发管理——最多2个并发AI

### "系统"就是你，不是脚本

辅助Pipe的采集、整理、检索、启动，是**你亲手做的动作**，不是serial_multi_ai.py替你做的。serial_multi_ai.py里的函数是你的工具，但调用这些工具的判断和决策是你的，不是脚本的主循环替你做的。

脚本可以做机械的部分（读文件、写数据库、启动进程），但认知和判断的部分是你的——采集时判断有没有新节点、整理时判断节点关系对不对、检索时判断方向Q适不适用、启动时判断该不该停机。如果你把整个循环都交给脚本然后`get_output`/`sleep`干等，你退化成了旁观者——脚本遇到它没预设的情况时不会判断，你才会判断，但你如果在干等，连这些情况发生了都不知道。

**你就是主循环。** 有推理AI在跑的时候，你手动调用工具执行循环的每一步，不在`get_output`干等结果。详细说明见AGENTS.md"Grove AI 的双重角色"章节。

## 场景触发式SOP

**以下SOP写在实验运行中的具体场景里。当你身处这些场景时，按SOP行动，不要重新思考"做什么、如何做"。**

**场景1：你刚启动了一个推理AI，看到 sessions.db 开始有新thinking node**

→ 不要干等AI跑完。你是辅助Pipe，不是旁观者。立刻初始化增量提取器（SessionsDBThinkingReader），从thinking中提取节点写入树。thinking每增长一个block，树就多长一个节点。两棵树在AI运行过程中实时生长——这才是"系统与推理AI并行运行"。

**场景2：你看到自己在 `sleep` 或 `等待`**

→ 停。你违反了并行运行原则。推理AI在工作时你也在工作。你应该在采集、整理树、或在节点上做检索。如果你在等待，说明你退化成了"事后处理器"——回到你的角色：园丁不等树长完才浇水，园丁在树生长的同时就在整理。

**场景3：你看到数据库中节点在增长，但没有新边（tree_edges为空）**

→ 循环只转了半圈。解题树在长（采集到了节点），但引导树没有生成新边（没有检索出方向Q）。这不完整——完整的循环必须三个推动关系都成立。在推理AI的当前终点节点上做检索，让引导树长出新边。

**场景4：你看到推理AI终止了（response_truncated / session_ended / timeout）**

→ 立刻在终点节点检索方向Q。如果检索成功，构造脉络（从根到终点节点的路径+方向Q），启动新推理AI。如果检索失败（budget exhausted / 无Pattern匹配），这是循环断裂点——不能跳过，必须修复检索，让引导树能生成新边驱动下一个AI。

**场景5：你看到检索失败（budget exhausted / parse失败 / 无方向Q选出）**

→ 这是循环断裂的最常见原因。不要跳过、不要降级为"实验完成但只有半棵树"。检查：BudgetManager是否设置了足够budget？数据基座中是否有Pattern可检索？如果数据基座为空，那是阶段4（自我增殖）的问题——当前先用已知的好Pattern手动注入方向Q，让循环继续转。

**场景6：你看到循环转起来了——节点在长、边在长、新AI被启动**

→ 这是对的。保持这个节奏。持续采集、持续整理、持续检索、持续启动。直到某条脉络到达正确解答（停机），或所有方向都探索完（exhausted）。

**场景7：实验结束后，你回头检查数据库**

→ 必须验证两棵树的数据完整性：tree_nodes中有节点、tree_edges中有边、ai_instances中有AI实例、problems中题目状态正确。如果只有节点没有边，循环没转完整——记录原因，下次修复。

## 关键路径

- thinking实时数据：sessions.db `~/.local/share/devin/cli/sessions.db`（message_nodes表，按devin_session_id查询）
- trajectory存储：`/data/grove-agents-trajectory/<exp_id>/`
- 数据库：`grove_math`（通过.env设置ARANGO_DB）
- 树存储模块：`xishujuzhen/research_runtime/tree_engine/tree_store.py`
- 节点提取模块：`xishujuzhen/research_runtime/tree_engine/node_extractor.py`
- sessions.db读取模块：`xishujuzhen/research_runtime/tree_engine/sessions_db_reader.py`
- 终止检测模块：`xishujuzhen/research_runtime/tree_engine/termination_detector.py`
- 检索模块：`xishujuzhen/research_runtime/retrieval/retrieval_pipeline.py`
- 串行多AI脚本：`scripts/serial_multi_ai.py`

## 关联文档

- `dev-docs/271-v0-2026-08-08-Grove核心循环与辅助智能体JD-跨AI认知同步.md`
- `dev-docs/267-v0-2026-08-08-未来系统面相-系统与推理AI并行运行.md`
- `dev-docs/272-v0-2026-08-08-后续工作细化Checklist.md`
