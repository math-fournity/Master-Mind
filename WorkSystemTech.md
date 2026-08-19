# WorkSystemTech.md — 工作系统技术说明

> **来源**：从 AGENTS.md 第350-387行外移（2026-08-19瘦身工程三期，392号方案）。
> **定位**：工作系统（AI自己的工作认知管理）的操作级技术说明。跨session/压缩后AI通过本文件恢复"怎么用工作系统"的认知。
> **加载时机**：当你要使用工作系统（CP1-CP6检查点/cognition_checkpoint_math.py/Hook机制/认知图更新）时，必须用read工具全文加载本文件。不涉及工作系统操作时不需要读。
> **AGENTS.md索引**：AGENTS.md "外部文档索引"节有指向本文件的索引行。

---

## 工作系统技术说明

> 本节是工作系统（AI自己的工作认知管理）的操作级技术说明。跨session/压缩后AI通过本节恢复"怎么用工作系统"的认知。

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

### Hook机制

| hook | 触发时机 | 脚本 | 作用 |
|---|---|---|---|
| SessionStart | 新session/压缩后 | `session_start_hook_math.py` | 注入认知图统计+工作纪律 |
| UserPromptSubmit | 每次用户提问 | `user_prompt_submit_hook_math.py` | 从`UserPromptSubmit.txt`读取提醒注入 |
| git post-commit | 每次commit后 | `githooks/post-commit` | 打印CP4检查清单（从稀疏矩阵动态查询） |

**改提醒内容**：直接编辑`xishujuzhen/UserPromptSubmit.txt`。**不要用Stop hook**：Stop hook会影响subagent。

### 工作系统纪律

1. **新术语必须追加到词汇表**（认知单元 `glossary`）。
2. **临场脚本沉淀纪律**：现写的一次性脚本，如果操作模式可复用，结束后必须沉淀到 `cognition_sdk_math.py`。
3. **必须 commit**：commit 后 git post-commit hook 会打印 CP4 检查清单。
4. **认知图变更后跑回归验证**：运行 `cognition_audit_math.py poc-regression`。
5. **边吸收边测试**：每次往依赖图/认知图装入新内容后，必须立即跑测试验证。
6. **"检查依赖"触发词**：当用户说"检查依赖"时，AI 立即执行CP4检查清单中的第3、4项。

