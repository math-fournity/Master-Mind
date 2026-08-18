# POC资产中央索引

**日期**：2026-08-17
**来源**：411号§2"现在就可以准备的7项资产"
**状态**：7项资产全部准备完成，审计通过（详见411号§4 + 本索引§3审计结论）

---

## §1 资产清单

| 序号 | 资产编号 | 资产名称 | 服务的POC | 文件路径 | 行数 | 状态 |
|---|---|---|---|---|---|---|
| 1 | POC-0-Asset-1 | CasePack v0简化版（10字段+5否决项审查） | POC-0 | `poc_0/casepack_simplified.md` | 955 | ✅就绪 |
| 2 | POC-0.5-Asset-1 | 变形关系声明表（6允许+5禁止+3边界） | POC-0.5 | `poc_0.5/metamorphic_relation_declaration.yaml` | 66 | ✅就绪 |
| 3 | POC-1-Asset-1 | 3个候选TellCore（A精简/B baseline/C扩展）+8维度Pareto评分表 | POC-1 | `poc_1/tellcore_candidates.yaml` | 153 | ✅就绪 |
| 4 | POC-1-Asset-2 | 独立审查者解题思维提取指南 | POC-1 | `poc_1/independent_reviewer_guide.md` | 254 | ✅就绪 |
| 5 | POC-2-Asset-1 | 小型Tell库（1目标+3近邻+2错配+1通用反思） | POC-2 | `poc_2/small_tell_library.yaml` | 324 | ✅就绪 |
| 6 | POC-3.5-Asset-1 | 5个HintInstance完整文本（L1极低→L5极高） | POC-3.5 | `poc_3.5/hint_instances_l1_l5.yaml` | 151 | ✅就绪 |
| 7 | POC-9-Asset-1 | 失败trace选题（382号4道+387号14道按d2子类型分布） | POC-9 | `poc_9/failure_trace_selection.md` | 317 | ✅就绪（有限制） |

---

## §2 资产→POC方案文档§8引用映射

每个资产文件已在对应POC方案文档的§8"被索引文档全文加载清单"中以"已就绪资产"子节引用：

| 资产 | 引用位置（POC方案文档§8） |
|---|---|
| POC-0-Asset-1 | 399号§8.0 |
| POC-0.5-Asset-1 | 400号§8.0 |
| POC-1-Asset-1 + POC-1-Asset-2 | 401号§8.0 |
| POC-2-Asset-1 | 402号§8.0 |
| POC-3.5-Asset-1 | 403号§8.0 |
| POC-9-Asset-1 | 409号§8.0 |

---

## §3 审计结论（2026-08-17）

**7项资产全部审计通过，不需要重写。**

### 3.1 逐项审计

| 资产 | 审计结论 | 关键质量点 |
|---|---|---|
| POC-0-Asset-1 | ✅合格 | 22道题全部有简化CaseCard（10字段）+5否决项审查；汇总表标注6道5否决项全通过题（CC-001/002/003/007 + CC-013/017） |
| POC-0.5-Asset-1 | ✅合格 | 6允许+5禁止+3边界变换声明完整；基于383号TellCore v0候选C的7字段 |
| POC-1-Asset-1 | ✅合格 | 3个候选（A精简/B baseline/C扩展）结构完整；8维度Pareto评分表清晰 |
| POC-1-Asset-2 | ✅合格 | 4层提取结构正确（困境识别/方向切换/新方向操作/提升回全局）；独立性约束明确（不加载383号）；关键区分写到（"什么认知动作导致了成功" vs "成功解答里有什么"） |
| POC-2-Asset-1 | ✅合格 | 7个TellCore结构完整（1目标+3近邻+2错配+1通用反思）；目标TellCore（TGT-001）完整7字段；3近邻（p-adic/CRT/QR）正确；2错配（构造-分析-排除/极值原理）正确；近邻和错配标注"待POC-2执行时补充"其他字段——合理 |
| POC-3.5-Asset-1 | ✅合格 | L1极低→L5极高5个HintInstance完整文本；固定TellCore不变只改变HintRenderer渲染参数 |
| POC-9-Asset-1 | ✅合格但有限制 | 382号4道source trace题直接纳入（信息完整）；387号14道按d2子类型分布选取（覆盖所有8种d2子类型）；**限制**：387号的14道题problem_id标注"需从ArangoDB查询"——387号文档只有数量分布无具体problem_id，subagent正确标注了需要查询并附带查询伪代码 |

### 3.2 限制项的后续处理

- **POC-9-Asset-1的problem_id查询**：执行POC-9前需从ArangoDB的`analysis_results`集合查询387号14道题的具体problem_id（查询伪代码已在资产文件中附带）

---

## §4 资产依赖关系

```
382号CasePack v0（✅已冻结）
  ├─→ POC-0-Asset-1（简化CaseCard）
  ├─→ POC-0.5-Asset-1（变形关系声明）
  ├─→ POC-1-Asset-2（独立审查者指南的source trace题）
  └─→ POC-9-Asset-1（失败trace选题的382号4道）

383号TellCore v0候选C（✅已完成）
  ├─→ POC-0.5-Asset-1（变形关系声明的TellCore字段）
  ├─→ POC-1-Asset-1（候选B=baseline）
  ├─→ POC-2-Asset-1（目标TellCore TGT-001）
  └─→ POC-3.5-Asset-1（5个HintInstance的TellCore来源）

403号POC-3.5方案文档（✅已设计5个HintInstance）
  └─→ POC-3.5-Asset-1（5个HintInstance文本）

387号错题分析系统（✅已有1071条DIRECTION_ERROR题）
  └─→ POC-9-Asset-1（失败trace选题的387号14道）
```

---

## §5 执行就绪状态（来自411号§3）

```
Phase A：策略对象成形 ← 7项资产就绪后可立即执行
  POC-0 CasePack冻结 ← 资产1就绪 ✅
  POC-0.5 变形关系声明 ← 资产2就绪 ✅
  POC-1 因果取商增强版 ← 资产3+4就绪 ✅

Phase B：基础验证 ← 部分资产就绪，部分需等Phase A完成
  POC-2 可选择 ← 资产5就绪 ✅，需POC-0完成精筛后才有12道题
  POC-2.5 基础因果效应验证 ← 资产6部分就绪（Hint-L3文本），脉络需等POC-1
  POC-3.5 Hint非特化程度验证 ← 资产6就绪 ✅，需POC-0完成精筛后有4道正迁移题
  POC-3 可执行 ← ❌等POC-3.5
  POC-4 可终止 ← ❌等POC-3

Phase C：归责与学习 ← ❌全部需等Phase B完成
  POC-6 可归责 ← 等POC-2+3.5
  POC-7 可持续学习 ← 等POC-2~6

Phase D：端到端 ← ❌需等Phase C完成
  POC-8 端到端闭环 ← 等POC-0~7
  POC-9 识别端验证 ← 资产7就绪 ✅，可并行执行
```

**结论**：7项资产就绪后，Phase A的3个POC可以立即执行，POC-9可以并行执行。Phase B~D需等前置POC完成。

---

## §6 来源文档

| 文档 | 对本索引的贡献 |
|---|---|
| 411号 | 资产准备分析——7项资产的定义、依赖、存放位置 |
| 382号 | CasePack v0（资产1/2/4/7的来源） |
| 383号 | TellCore v0候选C（资产2/3/5/6的来源） |
| 403号 | POC-3.5方案（资产6的5个HintInstance设计来源） |
| 387号dev-docs目录 | DIRECTION_ERROR题（资产7的来源） |
| 399-409号 | 6个POC方案文档（资产引用位置） |
