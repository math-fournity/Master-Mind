# 认知资产索引（活文档）

> 本文档由工作系统持续维护。每次新增认知单元、新增 dev-docs、ArangoDB 状态变更后更新。
> AGENTS.md 中的「Worktree 认知资产索引」rule 指向本文档。

## 当前隔离实施状态

**当前隔离实施状态**（Grove repo，2026-08-08 迁移后）：
- ✅ 文件操作边界：已建立（硬约束 1），本 repo `/data/master-mind-glm5.2-grove/` 独立工作
- ✅ Git 规则：已建立（硬约束 2），分支 `glm5.2`，不 push 到上游
- ✅ 数据库隔离：已实施（硬约束 3），25 个文件环境变量化，`.env` 配置 `grove_math`
- ✅ 认证环境变量化：已实施，`REDACTED-DB-PASSWORD` 不再裸硬编码
- ✅ Python venv 隔离：已实施，`.venv/`（python3.14 + python-arango 8.3.3），被 gitignore
- ✅ Devin hooks 隔离：已实施，`.devin/hooks.v1.json` 所有命令使用**绝对路径**（已更新为 Grove 路径）并先 source `.env`，确保 hook 从任意 CWD 启动都执行本 repo 脚本
- ✅ ArangoDB 实例 + 数据库初始化：已完成
- ✅ 角色说明：已建立，Grove AI/Subagent 边界清晰

**相关目录与角色**：
- **本 repo（Grove AI）**：`/data/master-mind-glm5.2-grove/`
- **Grove tmux 脚本**：`scripts/start-master.sh`（启动 tmux session `master-math` + devin CLI）、`scripts/enter-master.sh`（重新进入）、`scripts/stop-master.sh`（停止）
- **上游 repo**：`/data/master-mind/`（禁止写入，仅供参考）
- **旧工作目录**：`~/master-mind-glm5.2-worktree/`（已废弃，禁止触碰）
- **Grove AI 职责**：实现、迭代 Grove 树生长引擎
- **Subagent 职责**：完成 Grove AI 分配的具体任务

**ArangoDB 初始化状态**：
- 数据库：`grove_math`
- 初始化脚本：`xishujuzhen/arangodb_init.py`（基础集合+图+索引）
- `xishujuzhen/cognition_init_math.py`（cognition 集合）
- `scripts/init_research_runtime_db.py`（events/state_reducer/heuristics collections）
- 已验证：`session_start_hook_math.py` 正确连接并返回统计信息（0单元0边）

## ArangoDB 状态

- 认知图：35个认知单元（事件2026-08-05-A后；原165个中130个awareness单元已丢失，详见"数据丢失事件记录"节），51条边
- CP4检查清单6项纪律：iterative_testing(边吸收边测试), math_master_matrix_update, work_matrix_update, doc_sync_discipline, sdk_maintenance, glossary
- 5个意识节点版本链：v1(POC-1发现)→v2(POC-2深化)，current_version=v2
- cayley_hamilton三层版本链：v1(L1)→v2(L2)→v3(L3)，current_version=v3（**注意：cayley_hamilton单元在事件中丢失，需从题库重建**）
- three_layer_extraction版本链：v1(83号方案)→v2(POC-3验证L3跨领域迁移价值成立)，current_version=v2（**注意：该单元在事件中丢失，需重建**）
- AGENTS.md技术说明依赖已入稀疏矩阵：agents_tech_worksystem(source_docs=[91,94,97,100,101]) + agents_tech_mathmaster(source_docs=[83,85,86,88,90,92,99,100])（**注意：这两个单元在事件中丢失，需重建**）
- 数学依赖图（Phase 0冻结时点值，详见126号只读盘点报告）：dg_nodes=1719（concept:867, domain_concept:599, paradigm:165, problem:53, substep:27, 意识:5, step:3），dg_edges=1483（edge_type: unknown:1431/depends_on:38/calls:13/invokes:1; mapping_type: solution_path:837/invokes:259/structural_analogy:136/equivalence:87/其他:264），loops=4（dependency_graph:2, unfold_topo:2）
- 题库：60道题，159个解法（problems + solutions集合，未受事件影响）
- arxiv_papers：239472篇（未受事件影响）
- G'_topo（经典计算生成）：18节点，25边，2环路，TopologyVerifier 1次通过100%覆盖（POC-2场景）
- POC回归验证基线：POC-1=94/100，POC-2=100/100（**注意：回归基线可能因单元丢失而变化，需重新验证**）

**知识搜集状态（2026-08-04）**：
- **P0经典知识**：38文件10810行680KB（Ramanujan/Arnold/思想书/竞赛题/突破/Conway/开放问题）——`knowledge/`根目录
- **arXiv穷尽式元数据**：239472篇唯一论文，323.8MB JSON——`knowledge/arxiv/metadata_all_2023plus.json` + `knowledge/arxiv/metadata/meta_*.json`
  - 44个分类：math.* 28个 + cs.CC/LO/FL/DS/CG/GT/SC 7个 + quant-ph + math-ph + hep-th + stat.ML + nlin.CD/SI/AO/PS 4个
  - 年份分布：2023=48983 / 2024=69810 / 2025=62131 / 2026=58548
  - 大分类达10000 API上限（math.CO/AP/OC/PR/NA, quant-ph, hep-th, stat.ML）
  - math.MP和stat.TH返回0（分类名可能需要交叉列表查询）

## 最新 dev-docs（期许一/二期许方案区）

- **167**：认知图恢复与数据丢失防护方案（merge/upsert导入 + pre-commit防护 + arangodump定期备份）
- **168**：移除Supervisor需求与系统痕迹方案（删Supervisor目录 + 清AGENTS.md/用户需求.md/003/004中的Supervisor引用）
- **169**：工作系统需求实现方案（7条需求逐条映射，核心是第4条"动态埋点与批量反思"设计——SDK方法+CLI命令+提醒机制+AGENTS.md永久内容）
- **170**：AGENTS.md瘦身工程方案（元组Rule+Skill是瘦身根本手段）
- **171**：AGENTS.md瘦身整理方案（逐块决定保留/移走，1070行→396行减少63%）
- **172**：数据丢失事件记录（2026-08-05-A，130个awareness单元清空）
- **173**：审计意见交付方案（期许一方案——分4份文档审计低级别AI的Phase拆分/实现方案/代码/审计报告，新增维度23设计充分性+维度24元审计，产出174-177号审计报告）
- **174**：架构理解审计报告（3个P0+2个P1+2个P2——Phase 4→5入口门链条断裂；124号总览过时；Phase 4/6/7代码存在但CheckList说"待开始"；Phase 4用Mock LLM；Phase 5前置实现。Phase拆分忠实度✅）
- **175**：实现充分性审计报告（6份方案5份PASS+1份PARTIAL——143/148/155/160/163号无设计降级；151号方案声明devin cli但执行用Mock LLM。维度11-14全部PASS，维度23有1项gap）
- **176**：代码错漏审计报告（5个P0+6个P1——dataclass未frozen；candidate规则无运行时拦截；角色隔离未在业务逻辑调用；dg_adapter浅拷贝；无异常处理。D19/D20 PASS，D18/D21 FAIL）
- **177**：元审计报告（修正落实率78%；预防有效率0%——文档vs代码断层。低级别AI是优秀的文档审计员但不合格的代码审计员）
