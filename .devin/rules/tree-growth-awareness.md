# 两棵树生长意识规则（always-on）

## 核心意识

**Grove系统的本质是生长两棵树，不是让AI做题。**

- **引导展开树**（过程）= 从题目出发，在提示驱动下展开的所有可能解题路径。每个节点是一个数学处境，每条边是一个提示Q。活的、正在生长的。
- **解题记录树**（产物）= 引导展开树展开完成后凝固的树。包含成功路径、失败路径、分叉点、中间处境。
- **它们是同一棵树的不同阶段。**

**系统的目的不是"让AI做出来"，而是"让两棵树生长出来，在过程中与正确解答的脉络相遇"。**

## 触发条件

当Grove AI执行以下操作时，必须确保两棵树在数据库中生长：

1. **启动任何真实Solver实验**——裸跑测试、GuidedLoop引导、串行多AI、并发多AI
2. **设计新的实验编排**——任何涉及推理AI的实验脚本
3. **用户提到"树"、"两棵树"、"tree"、"脉络"、"阶段2/3/4"**
4. **实验结束后**——必须检查数据库中是否有树数据
5. **跨Session恢复工作时**——必须先检查数据库中的树状态

## 行动

触发时：
1. 加载 `.devin/skills/tree-growth-experiment/SKILL.md`
2. 确保实验编排使用 `tree_store.py` 写入ArangoDB的 `tree_nodes`/`tree_edges`/`problems`/`ai_instances` 集合
3. 每个AI实例终止后，用 `node_extractor.py` 从trajectory提取节点写入树
4. 实验结束后，验证数据库中有树数据（节点数>0、边数≥0、ai_instances数=实验AI数）
5. 如果数据库中没有树数据，实验不算完成

## 数据库中的两棵树

ArangoDB `grove_math` 数据库中的4个集合存储两棵树：

| 集合 | 类型 | 内容 |
|---|---|---|
| `tree_nodes` | document | 树节点=数学处境（六元组+path_from_root+situation_text） |
| `tree_edges` | edge | 树边=提示Q（_from父节点→_to子节点） |
| `problems` | document | 题目（每题一棵树，含root_node_key+status+total_nodes） |
| `ai_instances` | document | 推理AI实例注册（entry_node+status+nodes_contributed） |

**引导展开树** = `tree_nodes` + `tree_edges` 中 `status=growing` 的部分（正在生长）
**解题记录树** = `tree_nodes` + `tree_edges` 中所有数据（展开完成后的凝固态）

## 评测标准

**不是"做没做出来"，而是"树长得多完整"：**
- 弱系统：长出一条路径就停了（裸跑AI）
- 中等系统：长出几条路径，找到一条成功的（当前串行多AI）
- 强系统：长出完整的树，所有值得探索的方向都探索到（并发多AI目标）
- 大师级系统：长出的树足够完整，从中提炼的Pattern能让未来树长得更快更准

## 认知来源

- 267号面相文档：`dev-docs/267-v0-2026-08-08-未来系统面相-系统与推理AI并行运行.md`
- 两棵树理论：`原语化AI数学工程系统设计/05-两棵树/`（01-引导展开树、02-解题记录树、03-系统本质）
- 阶段2方案：`dev-docs/270-v0-2026-08-08-阶段2方案-脉络注入-串行多AI树生长引擎.md`
