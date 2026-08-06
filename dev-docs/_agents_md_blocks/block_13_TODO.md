## TODO

> 本节记录跨 Session 需要保持的待办事项。

- [ ] 制定数学大师制造项目的建设计划（Phase 划分 + Check List）——80号提供启动认知，122号v1/v2/v3建立总体架构与证据复核，**123号v1已给出Phase 0—7建设计划基线**；后续按123号DYN阶梯和Phase入口门推进，不再单独冻结Phase计划
- [x] **数学大师系统总体架构v1调查**：确认三平面（知识/研究运行/控制）、八组件、三闭环；实测当前主链未闭合、全图拓扑验证失败、规范知识与上下文编译器缺失
- [x] **数学大师系统总体架构v2修订**：确立思维形状公理、动态题目Q_t、K/T/H三图模型、Agent M闭环和“模式→激活包”的高阶时序启发关系
- [x] **数学大师系统总体架构v3完整复核**：同轮通读80—99号，回答当前机制、有效性、改进、Master答案泄漏、费马大定理五问；确认旧POC只对静态完整路线有局部信号，动态P→X矫正完全未验证。见122号v3
- [x] **第一性原理重构计划v1**：以`系统探讨.md`全文为母本，严格化目标系统为类型化任务/工作区、事件溯源、表示变换、时序规则、证据状态和受约束最小干预；给出DYN-0—7、Phase 0—7、角色权限、数据crosswalk、停止条件及Ramsey/费马案例。见123号v1
- [x] **Phase 0：冻结legacy与统一语义**——按123号第十部分和124号Check List：标记七步骤为legacy-static、冻结dg_*现状和模式统计、定义8类schema、建立Truth Vault与角色隔离矩阵、取消L1/L2/L3=v1/v2/v3映射、建立candidate/validated/published/retired生命周期。**Phase 0出口门全部通过**（P0-EXIT-1/2/3），证据见126/127/128号文档
- [ ] **Phase 1：只观察，不提示**——按123号第四十六节和124号：完成DYN-0（事件捕获真实性），创建运行manifest、捕获公开文本和工具事件、建立不可变原始事件和语义事件抽取
- [ ] **Phase 2：类型化状态与研究义务**——按123号第四十七节和124号：完成DYN-1（状态重建一致性）和DYN-2（卡点检测校准），实现V/F/O/R/D/E工作区、AND/OR研究义务、多观察者一致性测试
- [ ] **架构调查A：统一词汇与系统边界**——消除多套L1/L2/L3、“三层”“七步骤”和图概念碰撞；纳入数学知识图K、外显思维图T、启发激活图H。**由Phase 0接管**
- [ ] **架构调查B：规范数学知识与三图模式**——分别统一K/T/H的节点、边、tag、证据、版本和端点规则；制定POC旧模式与题库模式的非破坏性迁移方案。**由Phase 1接管**
- [ ] **架构调查C：最小端到端研究主链**——用一个小问题闭合"独立尝试→T图建模→停滞检测→H图匹配→最小启发→工具验证→审计→候选关系回写"。**由Phase 1—2/DYN-0—DYN-2接管**
- [ ] **最小启发因果POC**——从多次失败A/成功B轨迹差分提取候选P→X，用Hint-0至Hint-2提示做有对照的重复干预和跨题迁移；未通过前不建设大规模启发库。**对应DYN-3—DYN-5**
- [ ] 设计数学领域的依赖图初始结构（数学领域/工具/问题类型如何组织为节点和边）——由架构调查B接管
- [ ] 选型数学计算工具（SymPy / SageMath / Lean / Coq / ...）——81号已提出SymPy→SageMath→Lean 4；122号确认工具已部分安装但尚未接入研究运行主链
- [ ] 建立第一个数学知识系统骨架（`math-notes/` 目录结构）——122号确认目录当前不存在，需先决定其与规范知识层及ArangoDB的权威关系
- [x] 设计数学版 POC 验证方案（参考星学 POC1-8 实验设计）——大师-POC-1 正式方案已落盘到 84 号文档；题库难度梯度与 POC 阶梯的对应关系见 82 号文档第七节
- [x] 确定第一个数学研究场景作为 POC 实验场——矩条件极差题（84号文档）
- [x] **大师-POC-1 执行完成**：B组显著优于A组（边际增益+1.75/5分制），核心信念在数学领域成立。结果见 85 号文档
- [x] 题库建设：Phase A 标杆题库（Proofs from THE BOOK + MathLib 100 Theorems，手工结构化 20-50 道）——见 82 号文档第六节。**Phase A完成**：15道题42个解法已导入ArangoDB，依赖图452节点393边(含69条跨领域映射边)，认知图57个认知单元。见 107 号文档
- [x] **三层提取 POC**：验证 L1/L2/L3 三层提取的跨题复用增益（A=仅L1 / B=L1+L2 / C=L1+L2+L3 三组对照）——见 83 号文档第六节。**POC-3完成**：题3远迁移C vs B L3增量+2.6≥+1.5成功。结果见 106 号文档
- [x] **部署 ArangoDB 基础设施**：共用星学项目 ArangoDB 实例（端口8529），创建 `xishujuzhen_math` 数据库，运行 `arangodb_init.py`（已复制到数学项目 `xishujuzhen/`）——见 86 号文档
- [x] **大师-POC-2 采用七步骤工作流**：矩条件极差题第二问完整证明，使用 ArangoDB + G'_topo + TopologyVerifier，从文字对照升级为拓扑确定性验证。B组显著优于A组（+3.27/10分制）和B'组（+2.34/10分制），H1-H5全部验证通过。结果见 88 号文档
- [x] **P0知识搜集——arXiv穷尽式**（109号方案第⑤来源）：239472篇元数据（44分类，2023-2026，323.8MB JSON）+ 1305篇HTML全文（145分类，972008行114MB）。技术路线：arXiv API submittedDate日期范围查询 + 200条/页 + 3秒间隔 + 429重试退避。大分类达10000 API上限。见`knowledge/arxiv/`
- [ ] **P1知识搜集**（109号方案十三大来源中剩余来源）：①MathLib 100000+定理导入 ②OEIS 37万序列 ③THE BOOK完整版 ④关键数学家全集（Euler 80卷/Ramanujan笔记+Berndt注解）⑤教材与专著~200本 ⑥竞赛题全集（含Schweitzer研究级）⑦形式化数学库（Coq/Mizar/Metamath）⑧数学杂志问题栏（AMM 1894-/Crux/Kvant）⑨Bourbaki Seminar/ICM Proceedings ⑩Gardner 25年专栏/Conway全部 ⑪历史与哲学（Kline通史/Stillwell/Neugebauer/Heath）。按111号"难妙新"优先级排序
- [x] **arXiv元数据导入ArangoDB**：239K篇元数据导入ArangoDB建立论文索引，支持按分类/日期/作者/关键词查询，为依赖图节点提供论文出处定位——**已完成**：239472篇导入`arxiv_papers` collection，4个persistent索引，SDK新增`search_arxiv()`/`get_arxiv_paper()`/`promote_arxiv_paper()`/`get_arxiv_stats()`方法。四级映射规则（L1定理级/L2方法级/L3意识级/L4索引级）。详见112号方案
- [x] **POC-4代数拓扑泛化性验证**：Klein瓶同调群计算。A/B两组满分15/15，增量0。问题选择不当（标准教材内容在AI"会"区）。详见113-114号文档
- [x] **POC-5数论最新论文验证+隔离测试方案**：arXiv:2608.02381 orientation-rigidity定理。独立目录+AGENTS.md软限制+tmux监督隔离测试方案验证有效。A/B两组满分15/15，增量0。B组使用了反证法+螺旋交叉验证（依赖图影响结构不影响正确性）。详见115-117号文档
- [ ] **POC-6修正版证据闭环**：原始B组依赖图存在答案泄漏，119号原`+4.0/10`已降级为低可信历史结果。修正版A组猜k^{k/6}(错误)，B组运行中断。按121号方案先完成B组恢复性重跑，再做至少3对同配置A/B配对复跑、完整过程审计和盲评，之后才能给正式判定
- [ ] **POC-7方向**：依赖POC-6修正版证据闭环。在更多领域验证"发现型"问题的增量（如分析/几何/逻辑领域），或扩展到"构造型"问题（让AI构造反例/构造证明）
- [ ] **运行6个诊断测试**（97号测试方案）：T14 A/B对照待执行（需真实任务场景），T11b未执行（topo_generator已覆盖meta AI版）

### 数据丢失修复（事件2026-08-05-A）

> 详见"数据丢失事件记录"节。ArangoDB cognition_units中130个awareness单元被truncate清空，不可恢复。

- [x] **改`cognition_import_math.py`为merge/upsert模式**——不truncate，对每条JSON记录upsert；对ArangoDB有但JSON没有的记录保留不动或标记orphan待人工确认。**已完成（P0-8.1）**，脚本用 `insert(doc, overwrite=True)` 实现 upsert，检测 orphan
- [x] **新增`cognition_export_math.py`**——ArangoDB→JSON双向同步，定期把ArangoDB当前状态回写到`cognition_units_math.json`。**已完成（P0-8.2）**，支持 `--dry-run` 和 `--diff` 模式
- [x] **在`cognition_sdk_math.py`的`add_unit()`中增加JSON回写或审计日志**——每次add_unit时至少写一条审计记录到单独collection，记录cog_id/title/category/key_cognition/source_docs，防止再次出现"ArangoDB有但JSON没有且无记录"的情况。**已完成（P0-8.3）**，`_audit_log()` 方法写入 `cognition_audit_log` collection
- [x] **配置arangodump定期备份**——`arangodump` + cron定时任务，备份到`/data/master-mind/backups/arango/$(date +%Y%m%d)`，保留最近7天。**已完成（2026-08-06）**，`scripts/backup_arango.sh` 通过 `docker exec` 在容器内执行 arangodump，cron 每天凌晨 3 点运行

