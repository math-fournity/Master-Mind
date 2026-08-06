# worktree-isolation-history

## Description

指向元组 rule 中的 worktree-isolation-history 条目；Worktree 隔离的实施历史记录——环境变量化过程、commit 历史、上游同步记录。按需加载用于排查隔离问题或了解实施背景。

## 内容

### 历史代码状态与隔离方案详情

#### 历史代码状态（已修复，保留作背景）

修复前，所有 Python 文件**硬编码**了 ArangoDB 连接参数（DB_NAME、ARANGO_HOST、username、password）。这是从星学项目继承基础设施时留下的——`REDACTED-DB-PASSWORD` 密码来自星学项目 MOIRA_chinese_astrology 的命名。两轮环境变量化（commit `89760a4` + `4f781d2`）已消除全部裸硬编码，27 处 `REDACTED-DB-PASSWORD` 现全部位于 `os.environ.get()` 默认值中。

#### 隔离方案（已实施 · 方案 a 环境变量化）

**本 repo 专用数据库名**：`xishujuzhen_math_glm52`

**已实施的策略**：方案 a · 环境变量化。25 个 Python 文件的硬编码已改为 `os.environ.get()`，覆盖 4 个环境变量：

| 环境变量 | 默认值（上游行为） | 本 repo .env 值（隔离） |
|---|---|---|
| `ARANGO_HOST` | `http://localhost:8529` | `http://localhost:8529` |
| `ARANGO_DB` | `xishujuzhen_math` | `xishujuzhen_math_glm52` |
| `ARANGO_USER` | `root` | `root` |
| `ARANGO_PASS` | `REDACTED-DB-PASSWORD` | `REDACTED-DB-PASSWORD` |

改动模式（共 6 种）：
- `DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")`（16 个文件）
- `ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")`（11 个文件）
- `ArangoClient(hosts=os.environ.get(...))`（11 个文件 inline）
- `client.db(os.environ.get("ARANGO_DB", ...), ...)`（7 个文件 inline）
- `db_name=os.environ.get("ARANGO_DB", ...)`（3 处 inline 调用）
- `DB_USER/DB_PASS/ARANGO_USER/ARANGO_PASS` 赋值 + inline `username=/password=`（25 个文件，含 `topology_verifier.py` 带类型注解的函数签名）

默认值保持和上游一致，所以上游代码行为不变。本 repo 通过 `.env` 文件覆盖 `ARANGO_DB` 实现数据库隔离。

**配置文件**：
- `.env`（已 gitignore，不提交）：本 repo 专用，含 4 个环境变量
- `.env.example`（提交到 repo）：模板，供未来 AI 参考
- 使用前 `source .env` 或用 dotenv 加载

**未环境变量化的部分**（已知，按需处理）：
- `cognition_sdk_math.py` 和 `topology_verifier.py` 的 `host="localhost", port=8529` 是分开参数格式（非 URL），与 `ARANGO_HOST` 格式不同，暂未改。它们的 `db_name`/`username`/`password` 已环境变量化。
- 若未来要把本 repo push 到公开远端：默认值里的 `REDACTED-DB-PASSWORD` 仍在代码中（虽不是裸硬编码），需进一步用 secrets 管理或移除默认值。

**一次性改动脚本**：`scripts/_envvarize_arango.py`（DB_NAME/HOST）、`scripts/_envvarize_arango_auth.py`（username/password），保留在 repo 中作为改动记录。

### 本 repo commit 历史（glm5.2 分支）

**本 repo commit 历史**（glm5.2 分支）：
- `2938177` 用户需求.md/AGENTS.md: Supervisor 改为 Devin Stop hook 方案
- `73e0982` 用户需求.md: 追加 Supervisor 未来启动与运行场景
- `fd7f1ef` AGENTS.md: 记录 Supervisor hook 运行方式与产物
- `f86f13f` 补同步用户需求.md + runs/manifest.json
- `8fc823b` 初始同步：representation/ + dev-docs/163-166 + 146/147 patch + AGENTS.md 索引
- `627c579` .devin/ 隔离：config.local.json + hooks.v1.json 绝对路径 + .venv
- `73e6ca7` ArangoDB 初始化 + hook 路径绝对化
- `754c450`/`06078ac` AGENTS.md 角色说明 + Supervisor 目录
- `c78f382` dev-docs/001: 上游未提交内容同步方案
- `2e33663` AGENTS.md: 更新数据库隔离状态
- `4f781d2` ArangoDB 认证环境变量化：25 个文件
- `89760a4` ArangoDB 环境变量化：25 个文件，实现数据库隔离
- `25334f2` AGENTS.md: 新增 Worktree 隔离认知章节
- `f32194f`（上游 main 基点）146号v4→v4.1

**上游同步记录**：
- 同步内容：representation/ 24个.py（Phase 7实现，无ArangoDB依赖）+ dev-docs/163-166 + 146号v4.1→v4.2 + 147号v1.3→v1.4 + AGENTS.md 4行索引 + 用户需求.md + runs/manifest.json
- 同步方式：手动复制+patch应用（因上游AI停摆，未提交内容无法通过git fetch获取）
- 注意：未来如果上游被commit并rebase，本次手动同步的commit可能与上游commit冲突，需手动处理
