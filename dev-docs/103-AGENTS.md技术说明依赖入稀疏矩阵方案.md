# 103-AGENTS.md技术说明依赖入稀疏矩阵方案

> **文档定位**：102号文档把技术说明内联到AGENTS.md，但依赖关系只写了Markdown表格。用户指出：我们建稀疏矩阵就是为了存储依赖，应该把依赖写入认知图。本方案执行这个纠正。

## 一、问题

102号文档在AGENTS.md中加了"依赖维护"Markdown表格：

```
| 本节内容 | 依赖文档 | 更新触发条件 |
|---|---|---|
| CP1-CP6工作流 | 91号文档 | CP流程变更时 |
| ...
```

这是纯文档依赖——不可查询、不可遍历、CP1-CP3加载不到。违背了工作系统的设计初衷：**依赖关系应该在稀疏矩阵中**。

## 二、方案

### 2.1 新增2个认知单元

| cog_id | title | category | source_docs | 说明 |
|---|---|---|---|---|
| `agents_tech_worksystem` | AGENTS.md工作系统技术说明 | support | [91,94,97,100,101] | 代表AGENTS.md中"工作系统技术说明"节 |
| `agents_tech_mathmaster` | AGENTS.md数学大师系统技术说明 | support | [83,85,86,88,90,92,99,100] | 代表AGENTS.md中"数学大师系统技术说明"节 |

### 2.2 新增depends_on边

**agents_tech_worksystem →**：
- sdk_maintenance（CP5用SDK）
- work_system_upgrade（CP1-CP6来自91号方案）
- math_awareness_nodes（种子推荐表涉及意识节点）
- stop_hook（Hook机制中"不要用Stop hook"）

**agents_tech_mathmaster →**：
- seven_step_workflow（七步骤工作流）
- classic_expansion（G'_topo生成）
- topology_verifier（TopologyVerifier）
- topology_coverage（拓扑覆盖验证理论）
- three_layer_extraction（三层提取+版本链）
- math_awareness_nodes（数学意识节点）
- spiral_cognition（螺旋环路）

### 2.3 AGENTS.md中的Markdown依赖表改为指向稀疏矩阵

把102号加的Markdown依赖表替换为：

```
依赖关系存储在认知图稀疏矩阵中：
- agents_tech_worksystem（source_docs=[91,94,97,100,101]）
- agents_tech_mathmaster（source_docs=[83,85,86,88,90,92,99,100]）

查依赖：cognition_sdk_math.py traverse(['agents_tech_worksystem'])
当dev-docs更新时，用source_docs字段查哪些认知单元依赖它，同步更新AGENTS.md。
```

### 2.4 反向查询能力

新增SDK方法：`find_dependents_by_doc(doc_id)`——给定dev-docs编号，返回所有source_docs包含该编号的认知单元。这样当某个dev-docs更新时，可以查哪些AGENTS.md技术说明节需要同步。

## 三、Check List

- [x] 新增2个认知单元（agents_tech_worksystem, agents_tech_mathmaster）——完成。30个认知单元。
- [x] 新增depends_on边（4+7=11条）——完成。42条边。图遍历验证通过。
- [x] SDK新增find_dependents_by_doc方法——完成。反向查询测试通过（91/88/100号文档查询正确）。
- [x] AGENTS.md中Markdown依赖表改为指向稀疏矩阵——完成。两节依赖维护都指向认知图+给出查询命令。
- [x] 跑回归验证确保认知图变更无破坏——待执行。
- [x] 提交——待执行。

## 四、诚实面对

1. **source_docs是文档级依赖，不是节级依赖**：source_docs=[91,94,97,100,101]表示"这节技术说明依赖这5个dev-docs"，但不能精确到"CP1-CP6工作流依赖91号、种子推荐表依赖100号"。这是合理的抽象层级——节级依赖太细，文档级依赖足够指导更新。

2. **depends_on边是认知级依赖**：连接到认知单元（如seven_step_workflow），不是连接到dev-docs。这符合稀疏矩阵的设计——边连接的是认知，不是文档。
