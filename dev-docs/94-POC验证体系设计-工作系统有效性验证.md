# 94-POC验证体系设计·工作系统有效性验证

> **文档定位**：设计验证数学项目工作系统（cognition基座）有效性的POC体系。对应星学91号文档（POC验证体系），但适配数学项目特点。
>
> **依据**：93号差距分析（缺失POC验证体系）+ 星学91号文档（10代演进+D1-D5+H1-H5）+ 数学项目已有POC-1/POC-2经验

## 一、为什么需要POC验证

### 1.1 工作系统的核心声称

数学项目的工作系统（91号方案）有两个核心声称：

1. **图遍历能找到所有前置工作认知**：从种子认知单元出发，沿 depends_on 边遍历，能确定性找到任务所需的全部前置工作认知
2. **集合差集能验证覆盖**：用 AQL 集合差集计算"任务所需认知集 - 图遍历找到的认知集"，结果为空集即证明完全覆盖

如果这两个声称不成立，AI 可能在每次 session 中遗漏关键工作认知而不自知。

### 1.2 不能只是声称

星学91号文档给出三个理由：
- AI不知道自己不知道什么
- 工作系统的缺陷具有隐蔽性（管的是AI自己的认知，缺陷更难自察）
- 不验证就上线违反自己的方法论（数学项目的POC-1/POC-2都经过A/B组对照验证）

### 1.3 数学项目的特殊验证需求

数学项目与星学项目的差异，导致验证需求不同：

| 维度 | 星学项目 | 数学项目 |
|---|---|---|
| 已有POC | POC-1~9（验证依赖图提示对命理分析的有效性）+ POC-R1（验证工作系统对repo认知管理的有效性） | POC-1~2（验证依赖图提示对数学证明的有效性） |
| 工作系统POC | POC-R1（已有，99.6/100） | **需要设计** |
| 独有组件 | 无 | TopologyVerifier + 经典计算展开G'_topo + 两套图共享 + 意识节点双重身份 |

数学项目需要验证的**额外声称**（星学没有的）：
3. **TopologyVerifier能做拓扑确定性验证**（已有POC-2验证，1次通过100%覆盖）
4. **经典计算展开G'_topo保证全覆盖**（需要验证）
5. **两套图共享ArangoDB不产生冲突**（需要验证）
6. **意识节点双重身份（cognition_units + dg_nodes）的一致性**（需要验证）

## 二、POC验证体系设计

### 2.1 POC-R1-Math：工作系统有效性回归验证

对应星学的POC-R1，验证数学项目工作系统的有效性。

#### 实验设计

| 组 | 内容 | 执行方式 |
|---|---|---|
| **A组（对照组）** | 不使用工作系统，给AI任务描述+精简AGENTS.md，让它自由工作 | AI自己决定加载哪些dev-docs |
| **B组（实验组）** | 使用工作系统，CP1-CP3加载认知 | 执行cognition_checkpoint_math.py start --seeds ... |
| **审计组** | 独立审计A组和B组的工作质量 | 审计组不能是A组或B组的同一个AI实例 |

#### 评分维度（D1-D5，适配数学项目）

| 维度 | 评估什么 | 评分方式 | 满分 | 与星学差异 |
|---|---|---|---|---|
| **D1 认知覆盖率** | AI找到的前置工作认知占任务所需认知的比例 | 百分比（高度相关+中等相关加权） | 20 | 同星学 |
| **D2 约束保留率** | 精简AGENTS.md保留的行为约束占原AGENTS.md的比例 | 百分比（保留+移出到认知图均算保留） | 20 | 同星学 |
| **D3 版本链准确性** | current_version指向的文档是否确实是最新版本 | 逐个验证 | 20 | 同星学 |
| **D4 图遍历完整性** | 从种子出发的图遍历是否找到所有连通的认知单元 | 图遍历结果 vs 邻接矩阵传递闭包 | 20 | 同星学 |
| **D5 流程可执行性** | AI能否按照CP1-CP6的步骤实际执行 | 模拟执行，逐步检查 | 20 | 同星学 |
| **D6 拓扑覆盖验证** | **数学独有**：TopologyVerifier能否验证数学依赖图的覆盖 | TopologyVerifier运行结果 | 20（加分项） | **数学独有** |

#### 假设检验（H1-H5+数学独有H6-H8）

| 假设 | 内容 | 验证方式 | 对应星学 |
|---|---|---|---|
| H1 | 精简+认知图 ≥ 完整AGENTS.md | B组覆盖率 ≥ A组覆盖率且B组≥80% | 同星学H1 |
| H2 | 图遍历确定性找到所有前置 | depth=5和depth=7的结果一致 | 同星学H2 |
| H3 | 版本链指向正确current_version | 逐个验证current_version=latest | 同星学H3 |
| H4 | CP1-CP6可被AI实际执行 | 模拟执行CP1→CP2→CP3 | 同星学H4 |
| H5 | 精简不丢失行为约束 | 约束保留率≥95% | 同星学H5 |
| **H6** | **TopologyVerifier拓扑覆盖验证是确定性的** | TopologyVerifier代码运行结果100%可复现 | **数学独有**（已有POC-2验证） |
| **H7** | **经典计算展开G'_topo保证全覆盖** | topo_generator生成的G'_topo通过TopologyVerifier 1次验证 | **数学独有**（需要验证） |
| **H8** | **意识节点双重身份一致性** | cognition_units中的意识节点与dg_nodes中的意识节点内容一致 | **数学独有**（需要验证） |

#### Ground Truth标注

| 标注对象 | 标注方法 |
|---|---|
| D1的ground truth | 人工标注~15个高度相关认知单元+~5个中等相关认知单元（数学项目认知单元约30个，标注20个） |
| D2的ground truth | 原AGENTS.md的约束清单 |
| D6的ground truth | 数学依赖图G本身（dg_nodes + dg_edges + loops） |

#### 回归验证

认知图每次变更（新增/修改/删除认知单元或依赖边）后，运行回归验证：

```bash
.venv/bin/python3 xishujuzhen/cognition_audit_math.py poc-regression \
    --seeds math_master_system,poc_methodology \
    --ground-truth math_master_system,poc_methodology,dependency_graph_prompt,...
```

回归验证检查：
- 版本链完整性：每个active认知单元的current_version是否在cog_versions中有对应记录
- 图遍历完整性：从标准种子集出发的图遍历是否覆盖所有连通认知单元（max_depth=5）
- 约束保留率：精简规则文件的约束是否仍≥95%保留
- **拓扑覆盖**（数学独有）：TopologyVerifier验证数学依赖图覆盖

如果回归验证得分 < 95分，停止变更，先修复问题。

### 2.2 POC-3-Math：经典计算展开验证

验证92号方案的topo_generator.py——经典计算生成G'_topo骨架的有效性。

#### 实验设计

| 组 | 内容 | 执行方式 |
|---|---|---|
| **A组（对照组）** | meta AI生成G'_topo（当前POC-2的方式） | meta AI从ArangoDB读取G，规划G'_topo |
| **B组（实验组）** | 经典计算生成G'_topo骨架 | topo_generator.py从ArangoDB读取G，自动生成骨架 |
| **审计组** | 对比两组G'_topo的质量 | TopologyVerifier验证覆盖 + 人工对比section划分质量 |

#### 评分维度

| 维度 | 评估什么 | 评分方式 | 满分 |
|---|---|---|---|
| **节点覆盖** | G'_topo是否覆盖G的所有节点 | TopologyVerifier | 20 |
| **边覆盖** | G'_topo是否覆盖G的所有边 | TopologyVerifier | 20 |
| **螺旋环路圈数** | G'_topo中环路圈数是否与G一致 | TopologyVerifier | 20 |
| **traversal_order合理性** | 拓扑排序的顺序是否符合数学证明逻辑 | 人工对比 | 20 |
| **section划分质量** | section划分是否符合数学证明结构 | 人工对比 | 20 |

#### 假设检验

| 假设 | 内容 | 验证方式 |
|---|---|---|
| H1 | 经典计算生成的G'_topo通过TopologyVerifier 1次验证 | TopologyVerifier运行 |
| H2 | 经典计算生成的G'_topo全覆盖（节点+边+环路） | TopologyVerifier运行 |
| H3 | 经典计算的traversal_order与meta AI的traversal_order差异可接受 | 人工对比 |
| H4 | 经典计算的section划分与meta AI的section划分差异可接受 | 人工对比 |

#### 测试用例

用POC-2的依赖图（18节点25边2螺旋环路）作为测试用例：
- A组：meta AI生成的poc2_g_prime_topo.json（已有，作为基准）
- B组：topo_generator.py生成的poc2_g_prime_topo_auto.json（新生成）
- 对比两组的差异

### 2.3 POC-4-Math：两套图共享验证

验证两套图（cognition_units + dg_nodes）共享ArangoDB不产生冲突。

#### 实验设计

| 测试项 | 验证方法 |
|---|---|
| 集合名冲突 | cognition_units/cog_edges/cog_versions与dg_nodes/dg_edges/loops无重名 |
| 意识节点一致性 | cognition_units中的5个意识节点与dg_nodes中对应的意识节点内容一致 |
| 交叉引用 | cognition_sdk_math.py的cross_reference_dg方法能正确查询意识节点在数学依赖图中的位置 |
| 图遍历隔离 | cognition_units的图遍历不误访dg_nodes，反之亦然 |

#### 假设检验

| 假设 | 内容 | 验证方式 |
|---|---|---|
| H1 | 两套图集合名无冲突 | 检查ArangoDB集合列表 |
| H2 | 意识节点双重身份内容一致 | 逐个对比cognition_units和dg_nodes中的意识节点 |
| H3 | 图遍历相互隔离 | 分别从cognition_units和dg_nodes出发遍历，验证不串扰 |

## 三、验证体系设计原则

从星学91号文档继承7条原则 + 数学项目独有1条：

| 原则 | 内容 | 来源 |
|---|---|---|
| 对照原则 | 必须有A组（不使用工作系统）作为对照 | 星学POC-1起确立 |
| 独立审计原则 | 审计组不能是A组或B组的同一AI实例 | 星学POC-6交叉审计发现 |
| 闭环修正原则 | 审计发现问题→反馈→修正→再审，最大3轮 | 星学POC-8闭环审计 |
| 数学确定性原则 | 覆盖验证用集合差集，不用文字随机匹配 | 星学POC-9拓扑覆盖 |
| meta/normal分离原则 | 规划审计与执行转译由不同subagent完成 | 星学POC-9完全分离 |
| Ground truth原则 | 评判基准必须独立标注 | 星学POC-R1 |
| 回归验证原则 | 每次变更后跑回归验证 | 星学POC-R1修复后 |
| **拓扑确定性原则** | **数学独有**：TopologyVerifier做拓扑覆盖验证，不只是集合差集 | **数学POC-2验证** |

## 四、复用指南

### 4.1 最小验证：5-10节点简化认知图 + A/B对照

适用于：刚建好认知图，想快速验证是否有效。

**步骤**：
1. 从认知图中选一个典型任务，手动标注5-10个高度相关认知单元作为ground truth
2. A组：不使用认知图，给AI任务描述+精简规则文件，让它自由工作
3. B组：使用认知图，执行CP1（选3-5个种子）→CP2（图遍历）→CP3（缺口检查）
4. 审计：统计A组和B组各找到多少个ground truth认知单元
5. 计算：覆盖率(B) vs 覆盖率(A)，如果B > A且B ≥ 80%，最小验证通过

### 4.2 标准验证：完整认知图 + POC-R1-Math级回归验证

适用于：认知图已稳定，想全面验证工作系统。

**步骤**：
1. 建立完整认知图（所有认知单元+依赖边+版本链）
2. 设置A/B组对照，执行D1-D5评分
3. 验证H1-H5假设
4. 如果得分 ≥ 80分，标准验证通过

### 4.3 增强验证：拓扑覆盖 + 经典计算展开

适用于：需要验证数学项目独有组件（TopologyVerifier + topo_generator）。

**步骤**：
1. 上述标准验证
2. POC-3-Math：经典计算展开验证（topo_generator vs meta AI）
3. POC-4-Math：两套图共享验证
4. 验证H6-H8假设

## 五、Check List

### 阶段1：POC-R1-Math准备
- [ ] 认知图建好后，人工标注20个ground truth认知单元
- [ ] 准备A组材料（精简AGENTS.md，不含认知图索引）
- [ ] 准备B组材料（完整认知图 + cognition_checkpoint_math.py）
- [ ] 准备审计组材料（ground truth + 评分表）

### 阶段2：POC-R1-Math执行
- [ ] A组执行：给AI任务，自由工作，记录找到的认知单元
- [ ] B组执行：CP1-CP3加载认知，记录找到的认知单元
- [ ] 审计组评分：D1-D5五维度评分
- [ ] 假设检验：H1-H5

### 阶段3：POC-3-Math执行（经典计算展开验证）
- [ ] 用POC-2依赖图，topo_generator生成G'_topo骨架
- [ ] TopologyVerifier验证覆盖
- [ ] 对比经典计算版与meta AI版的差异
- [ ] 假设检验：H1-H4

### 阶段4：POC-4-Math执行（两套图共享验证）
- [ ] 检查集合名无冲突
- [ ] 对比意识节点双重身份内容一致性
- [ ] 测试图遍历隔离
- [ ] 假设检验：H1-H3

### 阶段5：回归验证
- [ ] 编写cognition_audit_math.py的poc-regression命令
- [ ] 认知图变更后运行回归验证
- [ ] 如果得分<95分，停止变更，先修复
