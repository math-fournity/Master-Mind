# work-system-language

## Description

指向项目 AGENTS.md「工作系统语言（元组 rule）」节；工作系统基础设施与表达语言参考。Think in 工作系统、设计工作系统新机制、盘点 hook/认知图/CP 检查点能力时按需加载。

---

## 一、Devin Hooks（3 个，均为纯提醒，无硬门禁）

| hook | 触发时机 | 脚本 | 表达能力 |
|---|---|---|---|
| SessionStart | 新 session / 压缩后 | `xishujuzhen/session_start_hook_math.py` | 注入认知图统计 + 工作纪律提醒（`additionalContext`） |
| PostCompaction | 上下文压缩后 | 同上 | 同上（让 AI 压缩后不丢"我在工作系统中"的认知） |
| UserPromptSubmit | 每次用户提问 | `xishujuzhen/user_prompt_submit_hook_math.py` | 从 `UserPromptSubmit.txt` 读取提醒注入 |

**语言**：`additionalContext` 字段注入文本到 AI 上下文。不能 block，只能提醒。

**动态配置**：`UserPromptSubmit.txt` 改文本即改提醒，不用改代码。

---

## 二、Git Hooks（2 个）

| hook | 触发时机 | 脚本 | 表达能力 |
|---|---|---|---|
| pre-commit | commit 前 | `xishujuzhen/githooks/pre-commit` | 硬性检查（AGENTS.md 引用的文件不存在 → **阻止 commit**） |
| post-commit | commit 后 | `xishujuzhen/githooks/post-commit` | 打印 CP4 检查清单（从认知图 `stop_hook` 的 depends_on 动态查询）+ AGENTS.md 对齐检查 |

**语言**：
- pre-commit：`exit 1` 阻止 commit（硬门禁）
- post-commit：`print()` 输出到终端（纯提醒，不阻止）

**动态查询**：CP4 检查清单不硬编码，从认知图 `stop_hook` 认知单元的 depends_on 边动态查询。改认知图的依赖关系 → CP4 检查清单内容自动变化。

---

## 三、认知图（ArangoDB）

### Collections

| collection | 当前数量 | 表达能力 |
|---|---|---|
| `cognition_units` | 35 | 认知单元：`cog_id`/`title`/`category`/`key_cognition`/`source_docs`/`current_version`/`status` |
| `cog_edges` | 51 | 依赖边：`_from`/`_to`/`edge_type`（depends_on 等） |
| `cog_versions` | 51 | 版本记录：`cog_id`/`version`/`version_order`/`doc`/`summary` |
| `cognition_audit_log` | 0 | 审计日志：`operation`/`cog_id`/`details`/`timestamp` |
| `cognition_tasks` | 0 | 任务记录：`task_description`/`seed_cog_ids`/`loaded_cog_ids` |

### 认知单元的 category 分类

| category | 含义 | 数量 |
|---|---|---|
| core | 核心方法论 | 19 |
| support | 支撑性认知 | 7 |
| awareness | 数学意识节点 | 5 |
| process | 过程记录 | 4 |

### 认知单元的 status 状态

| status | 含义 |
|---|---|
| active | 当前有效 |
| legacy | 历史保留，不再承担主运行时 |

**语言**：节点 + 边 + 版本链 + 审计日志 + 任务记录。可以表达"什么认知依赖什么认知"、"什么认知从哪些文档来"、"这个认知迭代了哪些版本"、"这个认知是 active 还是 legacy"。

### 数学大师系统 collections（第二层）

| collection | 表达能力 |
|---|---|
| `dg_nodes` / `dg_edges` | 数学知识依赖图（K 图） |
| `uf_nodes` / `uf_edges` | 展开图 |
| `ut_nodes` / `ut_edges` | 展开全图 |
| `raw_events` / `semantic_events` | 事件溯源（T 图） |
| `heuristic_rules` | 启发规则（H 图） |
| `evidence` | 证据 |
| `workspaces` / `obligations` / `obligation_edges` / `obligation_relations` | 工作区与义务 |
| `loops` / `stall_annotations` | 环路与停滞标注 |
| `run_manifests` / `activation_packets` | 运行清单与激活包 |
| `kcs` / `analyses` / `audits` / `checkpoints` / `prompts` / `subjects` | KC/分析/审计/检查点/提示/主体 |

---

## 四、CP1-CP6 工作流（`cognition_checkpoint_math.py`）

| CP | 时机 | 内容 | 表达能力 |
|---|---|---|---|
| CP1 | 工作开始前 | 种子选择 | `--seeds cog1,cog2` |
| CP2 | 工作开始前 | 认知加载（AQL 图遍历） | 自动执行，沿 depends_on 边遍历 |
| CP3 | 工作开始前 | 缺口检查 | 自动执行，验证覆盖 |
| CP4 | 工作结束时 | 认知捕获 | git post-commit hook 自动打印 |
| CP5 | 工作结束时 | 认知图更新 | `add_unit`/`add_edge`/`add_version` |
| CP6 | 工作结束时 | 任务-认知映射 | `record_task` |

**语言**：命令行参数 + AQL 图遍历 + SDK 方法调用。

**关键参数**：`max_depth=7`（数学项目路径比星学长，星学用 5）

---

## 五、SDK（`cognition_sdk_math.py`）公开方法

| 类别 | 方法 | 表达能力 |
|---|---|---|
| 查询 | `list_units`/`get_unit`/`get_versions`/`get_deps`/`get_stats`/`traverse` | 读认知图 |
| 写入 | `add_unit`/`add_edge`/`add_version`/`update_current_version` | 写认知图（带审计日志） |
| 删除 | `delete_version`/`delete_edge`/`delete_tasks_by_description` | 删认知图 |
| 审计 | `audit_version_chain`/`audit_graph_completeness`/`audit_coverage`/`audit_all`/`audit_poc_regression`/`audit_topology_coverage` | 验证认知图健康 |
| 修复 | `fix_version_order` | 修版本链 |
| 任务 | `record_task` | 记录任务-认知映射 |
| CP4 | `get_stop_checklist` | 从认知图动态查询 stop_hook 的依赖 |
| arxiv | `search_arxiv`/`get_arxiv_paper`/`promote_arxiv_paper`/`get_arxiv_stats` | arxiv 知识库 |
| 依赖查询 | `find_dependents_by_doc` | 反向查询（某文档更新时查哪些认知单元受影响） |

---

## 六、其他基础设施

| 设施 | 位置 | 表达能力 |
|---|---|---|
| 种子推荐表 | `seed_recommendation_table.json` | 问题类型 → 推荐种子映射 |
| 七步骤 pipeline | `seven_step_pipeline.py` | `--steps 1,2,3` 脚本化执行（legacy） |
| 认知图导入/导出 | `cognition_import_math.py`（merge/upsert）/ `cognition_export_math.py`（--dry-run/--diff） | JSON ↔ ArangoDB 双向同步 |
| 认知图审计 | `cognition_audit_math.py` | 全量审计 / POC 回归验证 |
| AGENTS.md 对齐检查 | `alignment_check.py` | 文件存在性 + 编号覆盖 + DYN/Phase 一致性 |
| ArangoDB 备份 | `scripts/backup_arango.sh` | docker exec arangodump + cron 每天 3 点 |
| tmux 脚本 | `start/enter/stop-master.sh` | tmux session 管理 |
| UserPromptSubmit.txt | `xishujuzhen/UserPromptSubmit.txt` | 动态提醒文本（改 txt 即改提醒） |
| dev-docs/ | `dev-docs/` | 顺序编号的工作文档 |
| AGENTS.md | 项目根 | 跨 session 认知一致性（always-on） |

---

## 七、表达能力总表

把基础设施按"表达能力"分类——这是 Think in 工作系统时的核心参考：

| 表达能力 | 机制 | 能表达什么 | 适用需求 |
|---|---|---|---|
| **注入文本到 AI 上下文** | SessionStart / PostCompaction / UserPromptSubmit hook | "你现在在工作系统中"、"你该加载认知"、"你该反思" | 启动自省、检查点提醒 |
| **阻止/允许操作** | git pre-commit hook | "AGENTS.md 引用的文件不存在 → 不许 commit" | 数据安全 |
| **输出提醒到终端** | git post-commit hook | "CP4 检查清单：你该检查工作系统是否需要更新" | 检查点反思 |
| **持久化认知（节点+边+版本）** | ArangoDB 认知图 | "这个认知依赖那个认知"、"这个认知从这些文档来"、"这个认知迭代了这些版本" | 认知不遗忘、自身可迭代 |
| **图遍历** | SDK `traverse()` + AQL | "从种子出发，找到所有前置认知" | 认知不遗忘 |
| **审计/验证** | SDK audit 方法 + `cognition_audit_math.py` | "认知图是否完整、是否一致" | 持续监控自身 |
| **动态查询依赖** | SDK `get_stop_checklist()` | "stop_hook 依赖了哪些认知 → CP4 检查清单" | 检查点反思 |
| **动态文本配置** | `UserPromptSubmit.txt` | 改 txt 即改提醒内容，不用改代码 | 检查点提醒 |
| **顺序编号文档** | `dev-docs/` | 工作痕迹和认知的有机积累 | 认知不遗忘 |
| **跨 session 认知锚点** | `AGENTS.md` | 跨压缩边界后 AI 能找回的认知 | 认知不遗忘 |

---

## 八、当前缺失的表达能力

针对用户需求.md 中的 7 条需求：

| 需求 | 现有语言 | 状态 |
|---|---|---|
| 1. 启动自省 | SessionStart hook | ✅ 已有 |
| 2. 认知不遗忘 | 认知图 + CP1-CP3 + dev-docs + AGENTS.md | ✅ 已有 |
| 3. 检查点反思 | git post-commit hook（CP4） | ✅ 已有 |
| **4. 动态埋点与批量反思** | **无** | **❌ 缺失** |
| 5. 持续监控自身 | audit + alignment_check | ✅ 已有 |
| 6. 自身可迭代 | add_unit/add_edge/add_version | ✅ 已有 |
| 7. 数据安全 | merge/upsert + arangodump + pre-commit | ✅ 已有 |

**核心缺口**：第 4 条"动态埋点与批量反思"没有对应的表达能力。需要设计：
- 埋点机制：AI 在工作中标记"这里值得反思"（记录下来，不打断连续工作）
- 批量反思机制：在合适的时间，AI 捋过所有埋点，一一反思
- 提醒机制：工作系统在合适的位置提醒 AI 做动态埋点

---

## 九、维护规则

本 skill 是工作系统"语言"的活文档。每次工作系统新增基础设施、新增表达能力、或发现新的缺失时，更新本 skill。

更新步骤：
1. 修改本 SKILL.md
2. 如果新增了 Devin hook 或 git hook，更新"一、Devin Hooks"或"二、Git Hooks"节
3. 如果新增了认知图 collection 或 SDK 方法，更新"三、认知图"或"五、SDK"节
4. 如果新增了表达能力，更新"七、表达能力总表"
5. 如果缺失被填补，更新"八、当前缺失的表达能力"
6. 同步更新项目 AGENTS.md 中对应的技术说明节
