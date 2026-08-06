## Handover Section

> 本节在压缩前更新，确保压缩后不丢认知。

### 工作系统实现状态（2026-08-05）

**已实现并测试通过**：
- `xishujuzhen/cognition_init_math.py`：ArangoDB初始化（5个新collections + 索引 + graph）
- `xishujuzhen/cognition_import_math.py`：认知单元导入
- `xishujuzhen/cognition_verifier_math.py`：认知图遍历引擎（AQL图遍历 + 集合差集覆盖验证）
- `xishujuzhen/cognition_sdk_math.py`：认知图SDK（CRUD + 审计 + 拓扑覆盖验证 + 交叉引用）
- `xishujuzhen/cognition_checkpoint_math.py`：CP1-CP6工作流入口
- `xishujuzhen/cognition_audit_math.py`：审计CLI（全量审计 + POC回归评分 + 拓扑覆盖验证）
- `xishujuzhen/topo_generator.py`：经典计算展开G'_topo（L0+L1+L2，1次通过100%覆盖）
- `xishujuzhen/seven_step_pipeline.py`：七步骤工作流集成脚本（步骤2调用topo_generator）
- `xishujuzhen/seed_recommendation_table.json`：种子推荐表（5种问题类型→推荐意识种子）
- `xishujuzhen/session_start_hook_math.py`：SessionStart + PostCompaction hook
- `xishujuzhen/user_prompt_submit_hook_math.py`：UserPromptSubmit hook（从txt读取提醒注入）
- `xishujuzhen/UserPromptSubmit.txt`：提醒内容文件（可随时编辑定制）
- `xishujuzhen/githooks/post-commit`：git post-commit hook（CP4检查清单 + AGENTS.md对齐检查）
- `xishujuzhen/githooks/pre-commit`：git pre-commit hook（AGENTS.md对齐硬性检查，阻止引用不存在文件的commit）
- `xishujuzhen/alignment_check.py`：AGENTS.md与repo内容对齐检查脚本（文件存在性+编号覆盖+DYN/Phase定义一致性+认知图规模一致性）
- `xishujuzhen/poc/cognition_units_math.json`：认知单元定义
- `.devin/hooks.v1.json`：Devin hooks配置（SessionStart + PostCompaction + UserPromptSubmit，不含Stop）

**测试结果**：
- 工作系统测试：14/16通过（98号报告）。T11b未执行，T14待真实任务场景。
- 反哺方案测试：10/10通过（100号报告）。R1-1~R6-1全部通过。

**关键参数**：
- max_depth默认值：7（数学项目路径比星学长，星学用5）
- git hook shebang：`#!/data/master-mind/.venv/bin/python3`（绝对路径）
- 意识节点名称映射：英文cog_id ↔ 中文node_id（cross_reference_dg方法中）

**ArangoDB状态**：
- 数据库：xishujuzhen_math
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
- **arXiv全文**：1305篇972008行114MB——`knowledge/arxiv/fulltext/*.md`
  - 145个分类各10篇最新论文HTML全文
  - math.* 325篇 / cs.* 302篇 / physics.* 182篇 / quant-ph 7篇 / math-ph 8篇 / hep-th 9篇 / stat.* 45篇 / nlin.* 45篇
  - 216篇失败（主要是旧论文无HTML版本）
- **arXiv技术路线**（全部免费匿名无key）：
  - 元数据：arXiv API `export.arxiv.org/api/query` + submittedDate日期范围查询（2025-2026 + 2023-2024两批） + 200条/页（API最大值） + 3秒间隔 + 429重试退避（60s/120s/180s...）
  - 全文：`arxiv.org/html/<id>`抓取HTML转Markdown + 3秒间隔 + 429重试退避
  - 脚本：`scripts/arxiv_search_v3.py`（元数据）+ `scripts/arxiv_fetch_html_v2.py`（全文）
- **P1待搜集**（109号方案十三大来源中剩余来源）：MathLib 100000+定理 / OEIS 37万序列 / THE BOOK / 数学家全集 / 教材~200本 / 竞赛题全集 / Coq/Mizar/Metamath / AMM问题栏 / Bourbaki Seminar / Gardner/Conway / Kline通史等

**arXiv论文ArangoDB操作化状态（2026-08-04）**：
- `arxiv_papers` collection：239472篇论文元数据已导入ArangoDB（22.9秒，10466篇/秒）
- 4个persistent索引：primary_category / published / mapping_level / has_fulltext
- 四级映射规则（112号方案）：L1定理级（论文中的定理成为dg_nodes concept节点）/ L2方法级 / L3意识级 / L4索引级（默认，仅在arxiv_papers中可搜索）
- SDK新增4个方法：`search_arxiv()`（按分类/关键词/作者/日期/全文/映射级别查询）/ `get_arxiv_paper()`（单篇获取）/ `promote_arxiv_paper()`（提升映射级别+关联dg_nodes）/ `get_arxiv_stats()`（统计）
- 所有239472篇初始为L4索引级，可按需提升为L1/L2/L3并关联到dg_nodes——这是"大师的一次在场"的体现
- 查询性能：按分类+日期排序查询~毫秒级（persistent索引生效）
- 脚本：`xishujuzhen/arxiv_to_arangodb.py`（导入+索引创建+验证）

