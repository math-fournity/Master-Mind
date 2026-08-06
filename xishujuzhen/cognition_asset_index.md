# 认知资产索引（活文档）

> 本文档由工作系统持续维护。每次新增认知单元、新增 dev-docs、ArangoDB 状态变更后更新。
> AGENTS.md 中的「Worktree 认知资产索引」rule 指向本文档。

## 当前隔离实施状态

**当前隔离实施状态**（截至角色说明更新 commit）：
- ✅ 文件操作边界：已建立（硬约束 1）
- ✅ Git 协调规则：已建立（硬约束 2），分支 `glm5.2`
- ✅ 数据库隔离：已实施（硬约束 3），25 个文件环境变量化，`.env` 配置 `xishujuzhen_math_glm52`
- ✅ 认证环境变量化：已实施，`REDACTED-DB-PASSWORD` 不再裸硬编码
- ✅ 上游未提交内容同步：已完成，Phase 7 实现 + 审计方法论 v4.2 已同步到本 repo
- ✅ Python venv 隔离：已实施，`.venv/`（python3.14 + python-arango 8.3.3），被 gitignore
- ✅ Devin hooks 隔离：已实施，`.devin/hooks.v1.json` 所有命令使用**绝对路径**并先 source `.env`，确保 hook 从任意 CWD 启动都执行本 repo 脚本
- ✅ ArangoDB 实例 + 数据库初始化：已完成
- ✅ 角色说明：已建立，Master/Subagent 边界清晰

**相关目录与角色**：
- **本 repo（Master）**：`~/master-mind-glm5.2-worktree/`
- **Master tmux 脚本**：`scripts/start-master.sh`（启动 tmux session `master-math` + devin CLI）、`scripts/enter-master.sh`（重新进入）、`scripts/stop-master.sh`（停止）
- **上游 repo**：`/data/master-mind/`
- **Master 职责**：实现、审计、迭代数学大师系统
- **Subagent 职责**：完成 Master 分配的具体任务

**ArangoDB 初始化状态**：
- 数据库：`xishujuzhen_math_glm52`
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
