---
name: audit-module
description: >
  按dev-docs/183-195号审计标准对数学大师系统模块执行审计。
  从ArangoDB/sessions.db/run目录提取数据，按检查项逐项验证，输出审计报告。
  WHEN to use: run结束后审计、模块代码变更后审计、定期回归审计。
  WHEN NOT to use: 一般代码编写、非审计相关的任务。
---

# audit-module skill

## 用途

按审计标准文档（dev-docs/183-195号）对数学大师系统的模块执行审计。

## 输入

- **审计范围**：要审计哪些模块（如"184+195"或"全部"）
- **数据源**：
  - ArangoDB（`$ARANGO_DB`，默认`grove_math`）
  - sessions.db（`~/.local/share/devin/cli/sessions.db`）
  - run目录（`runs/<run_id>/`）
- **审计标准文档**：dev-docs/183-195号

## 工作流

### 步骤1：确定审计范围

根据触发条件确定要审计的模块：
- run结束后：184（循环）+ 195（数学正确性）
- 模块代码变更：对应模块的审计文档
- 定期回归：全部模块

### 步骤2：读取审计标准

读取对应的审计标准文档，提取检查项清单。

### 步骤3：提取数据

根据审计模块从对应数据源提取数据：

```python
# 从ArangoDB提取
from arango import ArangoClient
client = ArangoClient(hosts="http://localhost:8529")
db = client.db(os.environ.get("ARANGO_DB", "grove_math"), username="root", password="")

# 从sessions.db提取
import sqlite3
conn = sqlite3.connect(os.path.expanduser("~/.local/share/devin/cli/sessions.db"))

# 从run目录提取
import json
with open(f"runs/{run_id}/guided_loop_result.json") as f:
    result = json.load(f)
```

### 步骤4：逐项检查

按审计标准文档中的检查项表逐项检查，每项判定为通过/有缺陷/失败。

### 步骤5：输出审计报告

```markdown
## <模块名>审计报告

### 审计时间
<timestamp>

### 审计范围
<哪些检查项组>

### 检查结果
| 检查项 | 结果 | 说明 |
|---|---|---|
| ... | [通过/有缺陷/失败] | [具体说明] |

### 判定
[通过 / 有缺陷 / 失败]

### 缺陷详情（如果有）
[具体描述和修复建议]
```

### 步骤6：记录审计结果

- 审计报告保存到run目录（`runs/<run_id>/audit_report.md`）
- 或保存到dev-docs/（定期回归审计）
- 更新AGENTS.md当前任务节记录审计结果

## 审计标准文档索引

参见 `.devin/rules/audit-trigger.md` 中的文档索引表。

## 注意事项

1. **审计AI与Solver隔离**：审计AI不能看到Solver的thinking（避免确认偏差）
2. **truth_vault权限**：只有Auditor角色可读truth_vault
3. **不修改被审计对象**：审计是只读操作，不修改代码或数据
4. **记录审计元数据**：审计时间、审计者、审计范围、数据源版本
