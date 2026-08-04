# 79 · xishujuzhen 下一代工作流技术选型：超大规模知识体系的数据库架构

## 一、需求分析

### 1.1 数据规模估算

| 数据类型 | 当前规模（POC-8） | 超大规模预估 | 增长因子 |
|---|---|---|---|
| 依赖图节点 | 71 | 数千~数万 | 100× |
| 依赖图边 | 106 | 数万~数十万 | 1000× |
| 跨宫边 | 10 | 数百~数千 | 100× |
| 螺旋环路 | 2 | 数十 | 10× |
| 知识内容KC | 24 | 数千 | 100× |
| 展开图G'_topo | 与G同构 | 与G同构 | 100× |
| 展开图G'（文字） | 300行 | 数万行 | 100× |
| 审计报告 | 每次分析1份 | 累积数千份 | N× |
| 多命主依赖图 | 1 | N个命主×规模 | N× |

### 1.2 操作需求

| 操作 | 数学本质 | 频率 | 延迟要求 |
|---|---|---|---|
| 图遍历（依赖路径） | BFS/DFS | 高 | 毫秒级 |
| 环路检测 | 强连通分量 | 中 | 秒级 |
| 跨宫边查找 | 边过滤 | 高 | 毫秒级 |
| 图同构验证 | G'_topo ≅ G | 每次转译1次 | 秒级 |
| 拓扑覆盖验证 | 集合差集 | 每次审计1次 | 秒级 |
| KC检索 | 文档查询 | 高 | 毫秒级 |
| KC忠实度检查 | 文本比对 | 每次审计1次 | 秒级 |
| 邻接矩阵运算 | 稀疏矩阵乘法 | 中 | 秒级 |
| 传递闭包计算 | 矩阵幂 | 低 | 秒级~分钟级 |
| 多命主图管理 | 子图提取 | 中 | 秒级 |

### 1.3 约束

- **开源顶级精品**：必须是真正的开源（OSI批准的许可证）
- **Python生态**：必须有成熟的Python驱动
- **本地部署**：支持本地部署（不依赖云服务）
- **与现有栈兼容**：现有栈是Python 3.14 + SQLite + JSON文件

## 二、技术选型分析

### 2.1 图数据库选型

#### 候选1：ArangoDB（多模型）

| 维度 | 评价 |
|---|---|
| 数据模型 | **多模型**：图+文档+键值，一个数据库三种模型 |
| 查询语言 | AQL（ArangoDB Query Language），支持图遍历+文档查询 |
| 许可证 | **Apache 2.0**（真正的开源） |
| 规模 | 支持分片，可处理数千万文档/节点 |
| Python驱动 | python-arango（成熟） |
| 向量搜索 | 原生支持向量索引（为未来AI集成预留） |
| 部署 | Docker一键部署，支持本地 |
| 社区 | 活跃，GitHub 13k+ stars |

**优势**：
- 一个数据库同时处理图（依赖图、展开图）和文档（KC、审计报告、分析结果），不需要多个数据库
- AQL可以同时做图遍历和文档查询，例如"查找某个节点的所有下游依赖，并返回它们的KC"
- Apache 2.0许可证，无商业限制
- 原生向量索引，为未来GraphRAG预留

**劣势**：
- 多模型意味着每个模型都不是最优的——图遍历性能不如Neo4j，文档查询性能不如MongoDB
- 社区比Neo4j小
- 分布式部署需要ArangoDB集群（ArangoDB SmartGraph）

#### 候选2：Neo4j Community Edition

| 维度 | 评价 |
|---|---|
| 数据模型 | 纯图（属性图模型） |
| 查询语言 | Cypher（最成熟的图查询语言） |
| 许可证 | **GPLv3**（社区版开源，但企业版收费） |
| 规模 | 社区版单机，数亿节点/边 |
| Python驱动 | neo4j-python（成熟） |
| 向量搜索 | 5.x支持原生向量索引 |
| 部署 | Docker一键部署 |
| 社区 | 最活跃，GitHub 10k+ stars |

**优势**：
- 图遍历性能最优（原生图引擎）
- Cypher是最成熟最直观的图查询语言
- 社区最大，文档最全
- 原生向量索引（GraphRAG）

**劣势**：
- 社区版**单机部署**，无集群——超大规模时受限于单机内存
- 企业版收费（$50k+/年）
- GPLv3许可证有传染性（如果修改源码必须开源）
- **纯图数据库**——文档存储需要另一个数据库（MongoDB等）

#### 候选3：Apache AGE（PostgreSQL扩展）

| 维度 | 评价 |
|---|---|
| 数据模型 | PostgreSQL + 图扩展（关系型+图+JSONB） |
| 查询语言 | SQL + openCypher |
| 许可证 | **Apache 2.0** |
| 规模 | PostgreSQL级别（TB级） |
| Python驱动 | psycopg2/asyncpg（成熟） |
| 部署 | PostgreSQL + AGE扩展 |
| 社区 | Apache顶级项目，4.7k stars，但仍在成熟中 |

**优势**：
- 基于PostgreSQL——最成熟的关系数据库
- SQL + Cypher混合查询
- JSONB支持文档存储
- Apache 2.0
- 继承PostgreSQL的所有运维能力（备份、复制、HA）

**劣势**：
- **仍在成熟中**——2026路线图显示openCypher覆盖、性能改进仍在进行
- 变长路径查询有性能问题（需要迭代固定深度遍历绕过）
- 图查询性能不如原生图数据库
- PG17/PG18支持仍在开发中

#### 候选4：JanusGraph

| 维度 | 评价 |
|---|---|
| 数据模型 | 分布式属性图 |
| 查询语言 | Gremlin |
| 许可证 | **Apache 2.0**（Linux基金会项目） |
| 规模 | **数十亿节点/边**（分布式） |
| Python驱动 | gremlin-python |
| 部署 | 复杂——需要存储后端（Cassandra/HBase/ScyllaDB）+ 索引后端（ElasticSearch） |
| 社区 | 活跃但小众 |

**优势**：
- 真正的超大规模（数十亿节点/边）
- Apache 2.0
- 模块化架构（存储和索引可替换）

**劣势**：
- **部署极其复杂**——需要至少3个组件（JanusGraph + 存储后端 + 索引后端）
- Gremlin查询语言学习曲线陡
- 文档存储需要另一个数据库
- 对本项目来说**过度设计**

#### 候选5：FalkorDB（Redis模块）

| 维度 | 评价 |
|---|---|
| 数据模型 | 属性图，**使用稀疏邻接矩阵（GraphBLAS）** |
| 查询语言 | openCypher |
| 许可证 | **SSPLv1**（争议性——不被OSI批准） |
| 规模 | 内存级（受限于Redis内存） |
| Python驱动 | falkordb-python |
| 部署 | Docker（需要Redis 8.0+） |
| 社区 | 新兴，482 stars |

**优势**：
- **使用稀疏邻接矩阵表示**——与用户的稀疏矩阵需求直接对应
- GraphBLAS线性代数查询——数学上优雅
- 极低延迟（内存级）
- 原生GraphRAG支持

**劣势**：
- **SSPLv1许可证**——不被OSI批准为开源，有争议
- 内存级——受限于Redis内存大小，超大规模时成本高
- 社区小，项目新
- 文档存储需要另一个数据库

### 2.2 文档数据库选型

#### 候选1：ArangoDB的文档模型
（已在图数据库候选1中分析）

#### 候选2：MongoDB Community Edition

| 维度 | 评价 |
|---|---|
| 数据模型 | 文档（BSON） |
| 查询语言 | MongoDB Query Language |
| 许可证 | **SSPLv1**（争议性） |
| 规模 | 支持分片，TB级 |
| Python驱动 | pymongo（成熟） |

**优势**：最成熟的文档数据库
**劣势**：SSPLv1许可证有争议；需要配合图数据库使用

#### 候选3：PostgreSQL JSONB

| 维度 | 评价 |
|---|---|
| 数据模型 | 关系型 + JSONB |
| 查询语言 | SQL（含JSON操作符） |
| 许可证 | **PostgreSQL License**（BSD-like，真正开源） |
| 规模 | TB级 |
| Python驱动 | psycopg2/asyncpg |

**优势**：最成熟，JSONB功能强大，可以同时处理关系型和文档型
**劣势**：不是纯文档数据库，JSON查询语法不如MongoDB直观

### 2.3 稀疏矩阵数据库选型

#### 候选1：TileDB

| 维度 | 评价 |
|---|---|
| 数据模型 | 多维数组（dense + sparse） |
| 许可证 | **MIT**（最宽松） |
| 规模 | 支持云存储（S3/GCS/Azure），本地文件系统 |
| Python驱动 | tiledb-python（成熟） |
| 部署 | 嵌入式库（无需服务端） |
| 社区 | 活跃，学术出身 |

**优势**：
- **MIT许可证**——最宽松
- 嵌入式库——无需部署服务端
- 原生支持稀疏数组
- 支持数据版本控制（time traveling）
- 与NumPy/SciPy/Pandas集成

**劣势**：
- 不是图数据库——无法做图遍历
- 主要面向科学计算，不是通用数据库
- 社区相对小

#### 候选2：FalkorDB的GraphBLAS
（已在图数据库候选5中分析——使用稀疏邻接矩阵）

#### 候选3：SciPy稀疏矩阵 + Parquet文件

| 维度 | 评价 |
|---|---|
| 数据模型 | 内存稀疏矩阵（CSR/CSC/COO） |
| 持久化 | Parquet文件（列式存储） |
| 许可证 | SciPy: BSD; Parquet: Apache 2.0 |
| 规模 | 内存级（计算）+ 磁盘级（存储） |
| Python驱动 | 原生Python |

**优势**：
- 最简单——不需要额外数据库
- SciPy稀疏矩阵是科学计算标准
- Parquet是高效的列式存储格式
- 与现有Python栈无缝集成

**劣势**：
- 不是数据库——没有查询语言、没有事务、没有并发控制
- 图遍历需要手动实现（用矩阵乘法）
- 不适合多用户并发

### 2.4 综合评估矩阵

| 方案 | 图存储 | 文档存储 | 稀疏矩阵 | 许可证 | 部署复杂度 | 推荐度 |
|---|---|---|---|---|---|---|
| **A: ArangoDB单数据库** | ✅ 原生图 | ✅ 原生文档 | △ 边列表（可提取为矩阵） | Apache 2.0 | 低 | **★★★★★** |
| B: Neo4j + MongoDB | ✅ 最优图 | ✅ 最优文档 | △ 边列表 | GPLv3 + SSPLv1 | 中 | ★★★★ |
| C: PostgreSQL + AGE + JSONB | ✅ 图扩展 | ✅ JSONB | △ 边列表 | Apache 2.0 | 中 | ★★★☆ |
| D: JanusGraph + MongoDB | ✅ 超大规模图 | ✅ 文档 | △ 边列表 | Apache 2.0 + SSPLv1 | **高** | ★★★ |
| E: ArangoDB + TileDB | ✅ 原生图 | ✅ 原生文档 | ✅ 原生稀疏数组 | Apache 2.0 + MIT | 中 | ★★★★☆ |
| F: FalkorDB + MongoDB | ✅ GraphBLAS图 | ✅ 文档 | ✅ 稀疏邻接矩阵 | SSPLv1（争议） | 中 | ★★★ |

## 三、推荐方案

### 3.1 主推荐：方案A — ArangoDB单数据库

**推荐理由**：

1. **多模型统一**：一个数据库同时处理图（依赖图G、展开图G'_topo、展开图G'）和文档（KC、审计报告、分析结果、大师提示词）。这直接对应了78号文档中的下一代工作流的数据需求。

2. **Apache 2.0**：真正的开源，无商业限制，无传染性。

3. **AQL统一查询**：一个查询语言同时做图遍历和文档查询。例如：
   ```aql
   // 查找某个节点的所有下游依赖，并返回它们的KC
   FOR v, e, p IN 1..10 OUTBOUND 'nodes/命宫分析' edges
     RETURN {node: v.id, kc: v.knowledge_content, path: p.vertices[*].id}
   ```

4. **拓扑覆盖验证可以代码化**：
   ```aql
   // 验证G'_topo覆盖G的所有节点
   FOR v IN graph_G_nodes
     FILTER v._id NOT IN (
       FOR n IN graph_G_prime_topo_nodes
         RETURN n._id
     )
     RETURN v  // 返回未覆盖的节点
   ```
   这是**确定性查询**，不是"文字随机匹配"。

5. **部署简单**：Docker一行命令，本地部署，无需多组件。

6. **向量索引预留**：为未来GraphRAG（知识图谱+向量检索）预留能力。

7. **Python驱动成熟**：python-arango，与现有Python 3.14栈兼容。

### 3.2 备选：方案E — ArangoDB + TileDB

如果稀疏矩阵运算成为性能瓶颈（例如需要计算传递闭包、可达性矩阵），可以增加TileDB作为稀疏矩阵持久化层：

- ArangoDB：图存储 + 文档存储（主数据库）
- TileDB：稀疏矩阵持久化（邻接矩阵、覆盖矩阵、传递闭包矩阵）
- SciPy：内存稀疏矩阵运算（从TileDB加载到内存计算）

**何时需要TileDB**：
- 邻接矩阵需要频繁矩阵运算（传递闭包、可达性）
- 矩阵规模超过内存（需要磁盘级稀疏矩阵存储）
- 需要矩阵版本控制（不同版本的依赖图对比）

**当前不需要TileDB的理由**：
- 当前规模（71节点106边）的邻接矩阵很小，SciPy内存计算足够
- 图遍历可以通过ArangoDB的AQL完成，不需要矩阵运算
- TileDB增加了系统复杂度

### 3.3 不推荐的方案

| 方案 | 不推荐原因 |
|---|---|
| Neo4j + MongoDB | 需要两个数据库，运维复杂；Neo4j社区版单机；GPLv3传染性 |
| JanusGraph | 部署极其复杂（3+组件），对本项目过度设计 |
| FalkorDB | SSPLv1许可证争议；内存级限制；社区小 |
| PostgreSQL + AGE | AGE仍在成熟中，变长路径查询有性能问题 |

## 四、架构设计

### 4.1 数据模型

#### ArangoDB Collections（集合）设计

```
数据库: xishujuzhen

├── 图集合（Graph）
│   ├── dependency_graph（依赖图G）
│   │   ├── vertex_collection: dg_nodes（节点集合）
│   │   │   └── 文档结构: {_id, _key, node_id, type, knowledge_content, section, ...}
│   │   └── edge_collection: dg_edges（边集合）
│   │       └── 文档结构: {_id, _key, _from, _to, edge_type, reason, ...}
│   │
│   ├── unfold_topo（展开图拓扑骨架G'_topo）
│   │   ├── vertex_collection: ut_nodes
│   │   │   └── 文档结构: {_id, _key, node_id, section, position, ...}
│   │   └── edge_collection: ut_edges
│   │       └── 文档结构: {_id, _key, _from, _to, edge_type, section, ...}
│   │
│   └── unfold_full（展开图G'，含文字）
│       ├── vertex_collection: uf_nodes
│       │   └── 文档结构: {_id, _key, node_id, text_content, kc_fidelity, ...}
│       └── edge_collection: uf_edges
│           └── 文档结构: {_id, _key, _from, _to, text_content, ...}

├── 文档集合（Documents）
│   ├── kcs（知识内容库）
│   │   └── 文档结构: {_id, _key, node_id, knowledge_content, source, version, ...}
│   ├── audits（审计报告）
│   │   └── 文档结构: {_id, _key, poc_id, round, type, report, score, ...}
│   ├── analyses（分析结果）
│   │   └── 文档结构: {_id, _key, poc_id, group, version, content, ...}
│   ├── prompts（大师提示词）
│   │   └── 文档结构: {_id, _key, poc_id, version, content, ...}
│   └── subjects（命主档案）
│       └── 文档结构: {_id, _key, name, birth_info, chart_data, ...}

└── 环路定义（存为文档）
    └── loops（螺旋环路）
        └── 文档结构: {_id, _key, loop_id, nodes, circles, type, ...}
```

### 4.2 拓扑覆盖验证（代码化）

```python
from arango import ArangoClient

class TopologyVerifier:
    def __init__(self, db):
        self.db = db
    
    def verify_node_coverage(self, graph_name, topo_name):
        """验证G'_topo覆盖G的所有节点"""
        query = """
        FOR v IN @@graph_nodes
          FILTER v._id NOT IN (
            FOR n IN @@topo_nodes
              RETURN n._id
          )
          RETURN {node_id: v.node_id, type: v.type}
        """
        cursor = self.db.aql.execute(query, bind_vars={
            '@graph_nodes': f'{graph_name}_nodes',
            '@topo_nodes': f'{topo_name}_nodes'
        })
        uncovered = list(cursor)
        return {
            'total': self.db.collection(f'{graph_name}_nodes').count(),
            'covered': self.db.collection(f'{graph_name}_nodes').count() - len(uncovered),
            'uncovered': uncovered,
            'coverage_rate': 1 - len(uncovered) / self.db.collection(f'{graph_name}_nodes').count()
        }
    
    def verify_edge_coverage(self, graph_name, topo_name):
        """验证G'_topo覆盖G的所有边"""
        query = """
        FOR e IN @@graph_edges
          FILTER e._from NOT IN (
            FOR n IN @@topo_nodes RETURN n._id
          ) OR e._to NOT IN (
            FOR n IN @@topo_nodes RETURN n._id
          )
          RETURN {from: e._from, to: e._to, type: e.edge_type}
        """
        cursor = self.db.aql.execute(query, bind_vars={
            '@graph_edges': f'{graph_name}_edges',
            '@topo_nodes': f'{topo_name}_nodes'
        })
        uncovered = list(cursor)
        return {
            'total': self.db.collection(f'{graph_name}_edges').count(),
            'covered': self.db.collection(f'{graph_name}_edges').count() - len(uncovered),
            'uncovered': uncovered,
            'coverage_rate': 1 - len(uncovered) / self.db.collection(f'{graph_name}_edges').count()
        }
    
    def verify_loop_coverage(self, graph_name, topo_name):
        """验证螺旋环路圈数保持"""
        loops = list(self.db.collection('loops').find({'graph': graph_name}))
        results = []
        for loop in loops:
            topo_loop = self.db.collection('loops').find({
                'graph': topo_name, 
                'loop_id': loop['loop_id']
            }).next()
            results.append({
                'loop_id': loop['loop_id'],
                'expected_circles': loop['circles'],
                'topo_circles': topo_loop['circles'],
                'match': loop['circles'] == topo_loop['circles']
            })
        return results
    
    def verify_all(self, graph_name, topo_name):
        """完整拓扑覆盖验证"""
        return {
            'nodes': self.verify_node_coverage(graph_name, topo_name),
            'edges': self.verify_edge_coverage(graph_name, topo_name),
            'loops': self.verify_loop_coverage(graph_name, topo_name),
            'passed': None  # 由调用者根据结果判断
        }
```

### 4.3 下一代工作流与数据库的整合

```
步骤1：依赖图解析（代码）
  输入：JSON依赖图文件
  输出：ArangoDB中的dependency_graph
  操作：代码解析JSON，写入ArangoDB的dg_nodes和dg_edges集合

步骤2：展开图拓扑规划（meta AI）
  输入：ArangoDB中的dependency_graph
  输出：ArangoDB中的unfold_topo
  操作：meta AI读取dependency_graph，生成G'_topo，写入ut_nodes和ut_edges

步骤3：拓扑覆盖验证（代码）
  输入：ArangoDB中的dependency_graph和unfold_topo
  输出：覆盖验证报告
  操作：TopologyVerifier.verify_all()，确定性验证
  如果验证通过 → 进入步骤4
  如果验证不通过 → 回到步骤2

步骤4：转译（normal AI）
  输入：ArangoDB中的dependency_graph和unfold_topo
  输出：ArangoDB中的unfold_full + prompts文档
  操作：normal AI按G'_topo结构填充文字，写入uf_nodes和uf_edges

步骤5：KC忠实审计（meta AI）
  输入：ArangoDB中的dependency_graph和unfold_full
  输出：审计报告文档
  操作：meta AI验证每个uf_node的text_content忠实于kc

步骤6：分析（normal AI）
  输入：ArangoDB中的dependency_graph和unfold_full
  输出：ArangoDB中的analyses文档
  操作：normal AI按G'结构进行分析

步骤7：分析覆盖审计（meta AI）
  输入：ArangoDB中的dependency_graph和analyses
  输出：审计报告文档
  操作：meta AI验证分析结果覆盖G的所有节点和边
```

### 4.4 稀疏矩阵的整合

虽然ArangoDB的图存储本质上就是稀疏邻接矩阵的边列表表示，但某些操作需要矩阵运算：

```python
import scipy.sparse as sp
from arango import ArangoClient

class GraphMatrixOps:
    def __init__(self, db, graph_name):
        self.db = db
        self.graph_name = graph_name
    
    def build_adjacency_matrix(self):
        """从ArangoDB图构建稀疏邻接矩阵"""
        # 获取所有节点
        nodes = list(self.db.collection(f'{self.graph_name}_nodes').all())
        node_ids = [n['_id'] for n in nodes]
        id_to_idx = {nid: i for i, nid in enumerate(node_ids)}
        
        # 获取所有边
        edges = list(self.db.collection(f'{self.graph_name}_edges').all())
        
        # 构建稀疏矩阵（COO格式）
        rows = [id_to_idx[e['_from']] for e in edges]
        cols = [id_to_idx[e['_to']] for e in edges]
        data = [1] * len(edges)
        
        n = len(node_ids)
        return sp.coo_matrix((data, (rows, cols)), shape=(n, n)).tocsr()
    
    def transitive_closure(self):
        """计算传递闭包（可达性矩阵）"""
        adj = self.build_adjacency_matrix()
        n = adj.shape[0]
        # Warshall算法或矩阵幂
        closure = adj.copy()
        for k in range(n):
            closure = closure + closure @ adj
            closure.data[:] = 1  # 二值化
        return closure
    
    def reachability(self, source_idx, target_idx):
        """检查从source到target是否可达"""
        adj = self.build_adjacency_matrix()
        # BFS或矩阵幂
        reachable = adj[source_idx]
        for _ in range(adj.shape[0]):
            if reachable[target_idx] > 0:
                return True
            reachable = reachable @ adj
        return False
```

## 五、实施路径

### 5.1 Phase 1：ArangoDB部署+数据迁移

- [ ] Docker部署ArangoDB
- [ ] 创建数据库xishujuzhen
- [ ] 创建collections（dg_nodes, dg_edges, ut_nodes, ut_edges, uf_nodes, uf_edges, kcs, audits, analyses, prompts, subjects, loops）
- [ ] 创建graphs（dependency_graph, unfold_topo, unfold_full）
- [ ] 将POC-7/POC-8的JSON依赖图导入ArangoDB
- [ ] 将POC-7/POC-8的大师提示词、审计报告、分析结果导入ArangoDB

### 5.2 Phase 2：拓扑覆盖验证代码化

- [ ] 实现TopologyVerifier类
- [ ] 实现GraphMatrixOps类
- [ ] 对POC-7/POC-8的依赖图运行拓扑覆盖验证
- [ ] 验证结果与文字审计结果对比（应该一致）

### 5.3 Phase 3：下一代工作流集成

- [ ] 实现步骤1（依赖图解析→ArangoDB）
- [ ] 实现步骤2（meta AI读取ArangoDB→生成G'_topo→写入ArangoDB）
- [ ] 实现步骤3（代码验证G'_topo≅G）
- [ ] 实现步骤4（normal AI按G'_topo转译→写入ArangoDB）
- [ ] 实现步骤5（meta AI KC忠实审计→写入ArangoDB）
- [ ] 实现步骤6-7（分析+分析覆盖审计）

### 5.4 Phase 4：POC-9验证

- [ ] 用下一代工作流+ArangoDB执行POC-9
- [ ] 验证拓扑覆盖验证是确定性的（只做一次）
- [ ] 验证meta/normal分离有效
- [ ] 与POC-8对比效率

## 六、与现有系统的兼容性

### 6.1 现有SQLite数据库（qizheng.db）

现有qizheng.db（4表：命主档案、排盘记录、矫正历史、大限存档）保持不变。ArangoDB是新增的，不是替换。

| 数据 | 存储位置 | 说明 |
|---|---|---|
| 命主档案、排盘记录、矫正历史、大限存档 | SQLite（现有） | 保持不变 |
| 依赖图、展开图、KC、审计报告、分析结果 | ArangoDB（新增） | xishujuzhen专用 |

### 6.2 现有JSON文件

| JSON文件 | 处理方式 |
|---|---|
| rules_library.json | 保持不变（规则库） |
| constants.json | 保持不变（命理常量） |
| shen_sha_complete.json | 保持不变（神煞数据） |
| POC的prompt JSON | 导入ArangoDB（依赖图） |

### 6.3 现有Python栈

| 组件 | 兼容性 |
|---|---|
| Python 3.14 | ✅ python-arango兼容 |
| .venv | ✅ 安装python-arango到.venv |
| qizheng模块 | ✅ 不受影响 |
| CS41.py | ✅ 不受影响 |

## 七、成本分析

### 7.1 开发成本

| 组件 | 复杂度 | 说明 |
|---|---|---|
| ArangoDB部署 | 低 | Docker一行命令 |
| 数据模型设计 | 中 | Collections + Graphs设计 |
| 数据迁移 | 中 | POC-7/8数据导入 |
| TopologyVerifier | 中 | AQL查询 + Python代码 |
| GraphMatrixOps | 中 | SciPy稀疏矩阵 + ArangoDB交互 |
| 工作流集成 | 高 | 7个步骤的端到端集成 |

### 7.2 运维成本

| 组件 | 成本 |
|---|---|
| ArangoDB单机 | 低（Docker容器，本地部署） |
| ArangoDB集群 | 高（需要3+节点，但本项目暂不需要） |
| 备份 | 低（ArangoDB支持dump/restore） |

## 八、风险与缓解

### 风险1：ArangoDB图遍历性能

**风险**：ArangoDB的图遍历性能不如Neo4j（原生图引擎）。
**缓解**：当前规模（数千节点数万边）在ArangoDB的性能范围内。如果未来需要超大规模（数百万节点），可以迁移到JanusGraph。

### 风险2：多模型数据库的复杂性

**风险**：ArangoDB的多模型特性意味着每个模型都不是最优的。
**缓解**：对本项目来说，"一个数据库处理所有数据"的简化优势大于"每个模型最优"的性能优势。

### 风险3：AQL学习曲线

**风险**：AQL是新查询语言，需要学习。
**缓解**：AQL语法类似SQL，学习曲线不高。核心查询模式（图遍历、集合差集）可以模板化。

### 风险4：从SQLite/JSON到ArangoDB的迁移

**风险**：迁移过程中可能丢失数据。
**缓解**：现有SQLite和JSON文件保持不变，ArangoDB是新增。迁移是导入，不是移动。
