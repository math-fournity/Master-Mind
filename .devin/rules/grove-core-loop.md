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
2. **推理AI→解题树**：采集thinking，增量提取节点写入树
3. **推理AI→引导树**：AI终止后在终点节点检索方向Q，启动新AI——引导树长出新边

**循环只转了半圈的判定**：节点在增长但tree_edges为空，或叶节点retrieval_done全为False——推动关系3没做。

## 辅助智能体角色（系统Pipe）

运行树生长引擎时，AI是辅助智能体，不是旁观者。职责：
1. 实时采集——读thinking_live.txt/jsonl
2. 实时整理两棵树——从thinking增量提取节点写入ArangoDB
3. 在节点上检索方向——用retriever.py在叶节点检索Pattern
4. 构造脉络——从根到叶节点的路径+方向Q
5. 启动新AI——通过solver-harness launch
6. 检查停机——leaf_success时标记problem solved
7. 并发管理——最多2个并发AI

## 场景触发式SOP

**场景1：AI启动后thinking_live.txt开始有内容**
→ 不要干等AI跑完。立刻轮询thinking_live.txt，提取节点写入树。

**场景2：你看到自己在sleep或等待**
→ 停。你违反了并行运行原则。回到采集/整理/检索。

**场景3：节点在增长但tree_edges为空**
→ 循环只转了半圈。在叶节点做检索，让引导树长出新边。

**场景4：推理AI终止了**
→ 立刻在终点节点检索方向Q。检索成功→构造脉络→启动新AI。检索失败→修复检索，不能跳过。

**场景5：检索失败（无Pattern匹配）**
→ 不能跳过、不能降级为"只有半棵树"。检查数据基座是否有Pattern。空则手动注入方向Q。

**场景6：循环转起来了——节点在长、边在长、新AI被启动**
→ 保持节奏。持续到停机或exhausted。

**场景7：实验结束后检查数据库**
→ 验证tree_nodes有节点、tree_edges有边、叶节点retrieval_done=True、有从叶节点启动的新AI。

## 关键路径

- thinking实时数据：`/data/math-agent-glm5.2-tmux-agents-trajectory/<exp_id>/mitm/thinking_live.txt`
- thinking共享流：`/data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/thinking_live.txt`
- 数据库：`xishujuzhen_math_glm52`（通过.env设置ARANGO_DB）
- 树存储模块：`xishujuzhen/vms/tree_store.py`
- 节点提取模块：`xishujuzhen/vms/node_extractor.py`
- 检索模块：`xishujuzhen/vms/retriever.py`
- 树生长引擎：`xishujuzhen/vms/tree_engine.py`

## 关联文档

- `dev-docs/273-v0-2026-08-08-Grove核心循环与辅助智能体JD-跨AI认知同步.md`
- `dev-docs/267-v0-2026-08-08-未来系统面相-系统与推理AI并行运行.md`
- `dev-docs/274-v0-2026-08-08-后续工作Checklist-让核心循环完整转起来.md`
