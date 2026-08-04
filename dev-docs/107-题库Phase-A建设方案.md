# 107-题库Phase A建设方案

> **文档定位**：82号文档定义了题库方法论，POC-3验证了三层提取方法（L1/L2/L3）的有效性。本文档是题库Phase A的执行方案——从标杆题源中手工结构化第一批20-50道题，用POC-3验证的方法提取L1/L2/L3，导入ArangoDB。

## 一、目标

### 1.1 Phase A的核心目标

**不是数量，而是建立结构化标准**——什么样的题库记录是好的，L2/L3怎么提取，跨领域边怎么标注，卡点怎么描述。

### 1.2 具体指标

| 指标 | 目标 |
|---|---|
| 题目数量 | 20-50道 |
| 题目来源 | Proofs from THE BOOK + MathLib 100 Theorems + 经典教材 |
| 结构化格式 | 82号文档第五节定义的格式 + 83号文档7.1节的L2/L3扩展 |
| 三层提取 | 每道题提取L1（解法路径）+ L2（思维模式）+ L3（范式思维，如有） |
| 依赖图贡献 | 每道题的解法路径作为依赖图的实证边导入ArangoDB |
| 跨领域映射 | 标注跨领域映射边（一题多解中不同领域间的结构对应） |

## 二、题目来源

### 2.1 三个题源

| 题源 | 特点 | 选取数量 | 选取标准 |
|---|---|---|---|
| **Proofs from THE BOOK** | Erdős的"天书证明"，大师级思维路径标杆 | 10-15道 | 覆盖数论/组合/几何/分析/图论等多个领域 |
| **MathLib 100 Theorems** | Freek Wiedijk的100个经典定理形式化 | 10-20道 | 已在Lean 4中形式化，可做验证基准 |
| **经典教材习题** | 覆盖面广、有难度梯度 | 5-15道 | 选跨领域映射丰富的题 |

### 2.2 选取原则

1. **跨领域映射优先**：一题多解且涉及不同领域的题优先（如Cayley-Hamilton：代数/模论/行列式）
2. **难度梯度**：从基础题（3-5节点）到中等题（10-20节点）到竞赛级（20-50节点）
3. **领域覆盖**：代数/几何/分析/拓扑/数论/组合/逻辑至少各1道
4. **L3提取潜力**：优先选有范式级思维的题（如范畴论视角、对偶思维、不变量思维）

### 2.3 第一批10道题（优先级排序）

| 序号 | 定理/题目 | 领域 | 跨领域映射 | L3潜力 | 来源 |
|---|---|---|---|---|---|
| 1 | Cayley-Hamilton定理 | 线性代数 | 矩阵↔模论 | 矩阵=模等价 | POC-3已完成 |
| 2 | Euler公式 V-E+F=2 | 拓扑/组合 | 组合↔拓扑 | 组合=拓扑不变量 | POC-3已完成 |
| 3 | 谱定理（实对称矩阵） | 线性代数 | 矩阵↔算子 | 自伴随=实特征值 | POC-3已完成 |
| 4 | 费马小定理 | 数论 | 数论↔群论 | 群作用=模运算 | MathLib 100 |
| 5 | 二项式定理 | 组合/代数 | 组合↔分析（生成函数） | 计数=系数提取 | MathLib 100 |
| 6 | Cauchy-Schwarz不等式 | 分析/代数 | 内积↔不等式 | 几何=代数不等式 | MathLib 100 |
| 7 | 中国剩余定理 | 数论 | 数论↔环论 | 局部=全局（环的直积） | MathLib 100 |
| 8 | Bezout定理 | 代数几何/数论 | 几何↔数论 | 几何相交=代数GCD | MathLib 100 |
| 9 | Wilson定理 | 数论 | 数论↔群论 | 群论=模运算 | MathLib 100 |
| 10 | Pythagoras定理 | 几何 | 几何↔代数 | 几何=代数恒等式 | Proofs from THE BOOK |

**前3道已由POC-3完成三层提取**——可以直接作为Phase A的第一批数据。

## 三、结构化格式

### 3.1 题目记录结构（82号+83号合并）

```json
{
  "problem_id": "MATH-001",
  "title": "Cayley-Hamilton定理",
  "source": "MathLib 100 Theorems #23",
  "difficulty": "undergraduate",
  "domain": ["linear_algebra"],
  "statement": "设A是n×n矩阵，p(λ)=det(λI-A)是其特征多项式，则p(A)=0。",
  "statement_mathml": null,
  "solutions": [
    {
      "solution_id": "MATH-001-S1",
      "method": "matrix_direct",
      "domain": "linear_algebra",
      "path": [
        {"step": 1, "concept": "characteristic_polynomial", "action": "define"},
        {"step": 2, "concept": "matrix_polynomial", "action": "evaluate"},
        {"step": 3, "concept": "linear_dependence", "action": "use"},
        {"step": 4, "concept": "conclusion", "action": "derive"}
      ],
      "l2_patterns": [
        {"pattern": "多项式恒等式检验", "evidence_step": 3, "applicable_domains": ["algebra","number_theory","analysis"]},
        {"pattern": "不变量思维", "evidence_step": 1, "applicable_domains": ["algebra","topology","number_theory","geometry"]}
      ],
      "l3_paradigms": [
        {"paradigm": "矩阵=模等价", "domains_connected": ["linear_algebra","module_theory"], "graph_restructure": "增加线性代数↔模论跨领域边"}
      ],
      "cross_domain_edges": [],
      "elegant": false,
      "source": "standard"
    },
    {
      "solution_id": "MATH-001-S2",
      "method": "module_nakayama",
      "domain": "module_theory",
      "path": [...],
      "l2_patterns": [...],
      "l3_paradigms": [...],
      "cross_domain_edges": [
        {"from": "matrix", "to": "module", "type": "equivalence"}
      ],
      "elegant": true,
      "source": "standard"
    },
    {
      "solution_id": "MATH-001-S3",
      "method": "determinant_adjugate",
      "domain": "linear_algebra",
      "path": [...],
      "l2_patterns": [...],
      "l3_paradigms": [],
      "cross_domain_edges": [],
      "elegant": true,
      "source": "standard"
    }
  ],
  "stuck_points": [],
  "lean_formalized": true,
  "lean_proof": "MathLib4: Matrix.charpoly"
}
```

### 3.2 从题目记录到依赖图

```
对每道题的每个解法：
  对 path 中的每一步：
    如果 concept 不在 dg_nodes 中 → 新增节点
    如果相邻 step 之间的边不在 dg_edges 中 → 新增边（类型：solution_path）
  对 l2_patterns 中的每个思维模式：
    如果 pattern 不在 dg_nodes 中 → 新增意识节点
    新增边：problem --invokes--> awareness_node
  对 l3_paradigms 中的每个范式：
    如果 paradigm 不在 dg_nodes 中 → 新增范式节点
    新增边：domain_a --paradigm_equivalence--> domain_b
  对 cross_domain_edges 中的每条边：
    如果边不在 dg_edges 中 → 新增跨领域映射边
```

## 四、执行计划

### 4.1 阶段1：POC-3已有3道题导入

前3道题（Cayley-Hamilton、Euler公式、谱定理）的三层提取已在POC-3中完成，只需格式化为标准JSON并导入ArangoDB。

### 4.2 阶段2：MathLib 100 Theorems选取5-7道

从MathLib 100 Theorems中选取跨领域映射丰富的5-7道题：
- 费马小定理、二项式定理、Cauchy-Schwarz、中国剩余定理、Bezout定理、Wilson定理
- 每道题用subagent做三层提取（L1从标准证明提取，L2/L3用AI二次/三次分析）

### 4.3 阶段3：Proofs from THE BOOK选取3-5道

从Proofs from THE BOOK中选取最优美的3-5道证明：
- 选取有"天书级"优美证明的题
- 这些证明代表大师级思维路径的标杆

### 4.4 阶段4：导入ArangoDB + 依赖图构建

把所有结构化题目导入ArangoDB的problems/solutions集合，解法路径导入dg_nodes/dg_edges。

## 五、Check List

- [ ] 阶段1：POC-3已有3道题格式化为标准JSON
- [ ] 阶段1：导入ArangoDB（problems + solutions + dg_nodes + dg_edges）
- [ ] 阶段2：从MathLib 100 Theorems选取5-7道题
- [ ] 阶段2：每道题三层提取（subagent辅助）
- [ ] 阶段3：从Proofs from THE BOOK选取3-5道题
- [ ] 阶段3：每道题三层提取
- [ ] 阶段4：全部导入ArangoDB
- [ ] 阶段4：依赖图统计（节点数/边数/跨领域边数）
- [ ] 阶段4：更新AGENTS.md

## 六、与后续工作的关系

### 6.1 与POC-3b的关系

POC-3b（消除L3直接映射提示）仍记为TODO，但优先级降低——题库Phase A积累的真实题目会自然提供更好的L3提取材料，POC-3b可以在Phase A完成后用更大题库重新验证。

### 6.2 与MathLib导入的关系

MathLib 100 Theorems是Phase A的题源之一。Phase A中从这些定理提取的是**思维依赖**（L1/L2/L3），不是**形式化依赖**（Lean 4的declaration依赖）。后者是81号Phase 1的lean-graph-extractor工作，是另一条工作线。

### 6.3 与math-notes/的关系

Phase A提取的L2思维模式将成为math-notes/数学意识/的第一批内容来源——不是凭空写的，而是从具体解法中抽象出来的，每条都有实证来源。
