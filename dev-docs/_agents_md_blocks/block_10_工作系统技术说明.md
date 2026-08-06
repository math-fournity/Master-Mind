## 工作系统技术说明

> 本节是工作系统（AI自己的工作认知管理）的操作级技术说明。跨session/压缩后AI通过本节恢复"怎么用工作系统"的认知。完整方案见依赖文档。

### 工作系统语言（元组 rule）

**当需要 Think in 工作系统、设计工作系统新机制、盘点 hook/认知图/CP 检查点能力、或讨论"用什么语言表达工作系统思想"时，加载 `work-system-language` skill。**

工作系统有一套基础设施（Devin hooks、git hooks、认知图 ArangoDB、CP1-CP6、SDK），每件基础设施提供一种"表达能力"。`work-system-language` skill 是这些表达能力的活文档：能向 AI 传递什么信息、能持久化什么结构、能触发什么动作、当前缺失什么能力。

触发场景：
- 用户说"工作系统"、"我们的语言"、"用什么表达"、"Think in 工作系统"
- 需要设计工作系统新机制（如动态埋点、批量反思等）
- 需要盘点工作系统有什么基础设施
- 需要分析"这个需求能用现有语言表达吗"
- 工作系统新增了基础设施后，需要更新语言参考

### CP1-CP6工作流

工作系统的核心是CP1-CP6六个检查点，通过`cognition_checkpoint_math.py`执行：

| CP | 时机 | 内容 | 命令 |
|---|---|---|---|
| CP1 | 工作开始前 | 种子选择：确定本次任务需要哪些种子认知单元 | `cognition_checkpoint_math.py start --seeds <cog_id1>,<cog_id2>` |
| CP2 | 工作开始前 | 认知加载：AQL图遍历，从种子出发沿depends_on边找到所有前置认知 | CP1命令自动执行 |
| CP3 | 工作开始前 | 缺口检查：验证已加载的认知是否覆盖任务所需 | CP1命令自动执行 |
| CP4 | 工作结束时 | 认知捕获：检查本次工作是否产生新方法论/新依赖/新版本/新术语/临场脚本 | git post-commit hook自动打印 |
| CP5 | 工作结束时 | 认知图更新：新版本/新边写入ArangoDB | `cognition_sdk_math.py`的add_version/add_edge |
| CP6 | 工作结束时 | 任务-认知映射：记录"这个任务用了哪些种子" | `cognition_sdk_math.py`的record_task |

**关键参数**：max_depth=7（数学项目路径比星学长，星学用5）

### 种子推荐表

`xishujuzhen/seed_recommendation_table.json`——数学问题类型→推荐意识种子映射：

| 问题类型 | 推荐种子 |
|---|---|
| 极值/上下界问题 | numerical_check, extreme_testing, invariant_thinking, approximation_thinking |
| 证明构造问题 | invariant_thinking, local_global_thinking, seven_step_workflow |
| 跨领域问题 | local_global_thinking, invariant_thinking, spiral_cognition, three_layer_extraction |
| 逼近/误差分析 | approximation_thinking, numerical_check, extreme_testing |
| 一般证明问题 | seven_step_workflow, math_awareness_nodes |

**用法**：AI接到数学问题后，先查此表确定种子，再执行CP1-CP3。

### 认知图查询与审计

```bash
# 查统计
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); print(sdk.get_stats())"

# 图遍历（从种子出发）
.venv/bin/python3 -c "from cognition_sdk_math import CognitionSDK; sdk=CognitionSDK(); print(sdk.traverse(['seven_step_workflow'], max_depth=7))"

# 全量审计
.venv/bin/python3 xishujuzhen/cognition_audit_math.py all

# POC回归验证
.venv/bin/python3 xishujuzhen/cognition_audit_math.py poc-regression --seeds <seeds> --ground-truth <cog_ids>
```

### 回归验证

每次认知图变更（新增/修改/删除认知单元或依赖边）后，运行回归验证：
- D1覆盖率：图遍历是否覆盖ground truth
- D3版本链：current_version是否指向latest
- D4图遍历完整性：depth=7 vs depth=9是否一致
- 满分100，低于95需排查

### Hook机制

三个hook的分工（均为纯提醒，无硬门禁）：

| hook | 触发时机 | 脚本 | 作用 |
|---|---|---|---|
| SessionStart | 新session/压缩后 | `session_start_hook_math.py` | 注入认知图统计+工作纪律 |
| UserPromptSubmit | 每次用户提问 | `user_prompt_submit_hook_math.py` | 从`UserPromptSubmit.txt`读取提醒注入 |
| git post-commit | 每次commit后 | `githooks/post-commit` | 打印CP4检查清单（从稀疏矩阵动态查询） |

**改提醒内容**：直接编辑`xishujuzhen/UserPromptSubmit.txt`，不用改代码，下次提问立即生效。

**不要用Stop hook**：Stop hook会影响subagent（星学项目实测证实）。用 git post-commit hook 代替。

### 依赖维护

本节的依赖关系存储在认知图稀疏矩阵中（认知单元 `agents_tech_worksystem`）：
- source_docs: [91, 94, 97, 100, 101]
- depends_on: sdk_maintenance, work_system_upgrade, math_awareness_nodes, stop_hook

**查依赖**：`cognition_sdk_math.py traverse(['agents_tech_worksystem'])`
**反向查询**（当某个dev-docs更新时，查哪些技术说明节需要同步）：
```bash
.venv/bin/python3 -c "import sys; sys.path.insert(0,'xishujuzhen'); from cognition_sdk_math import CognitionSDK; [print(u['cog_id'],u['title']) for u in CognitionSDK().find_dependents_by_doc(91)]"
```

