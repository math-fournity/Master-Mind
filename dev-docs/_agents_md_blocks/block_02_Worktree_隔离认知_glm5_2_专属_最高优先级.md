## Worktree 隔离认知（glm5.2 专属 · 最高优先级）

### 本 repo 是什么

本目录 `/data/master-mind-glm5.2-grove/` 是上游 repo `/data/master-mind/` 的**独立 clone**，不是 git worktree，是物理隔离的第二个 repo。

- **存在原因**：另一个 AI 正在上游 D repo 内活跃工作（有未提交改动）。为让本 AI（GLM-5.2）并发工作而不互相干扰，开辟了这个独立 clone。
- **为什么不用 git worktree**：worktree 共享 `.git`，并发 git 操作有锁冲突风险；且 D repo 的 `.git` 在 HDD 上，git 操作慢。独立 clone 把 `.git` 放到内置 SSD，既隔离又快。
- **上游 repo 路径**：`/data/master-mind/`
- **本 repo 路径**：`/data/master-mind-glm5.2-grove/`
- **origin**：`/data/master-mind`（fetch/push 都指向它）
- **本 repo 工作分支**：`glm5.2`（基于上游 main 的 `f32194f`）
- **本地 main 分支**：保留为 origin/main 的镜像，**不要在 main 上工作**。

### 硬约束 1 · 文件操作边界

**所有文件读写、代码改动、文档落盘、构建产物，只能在 `/data/master-mind-glm5.2-grove/` 内。**

- **禁止**以任何方式写入 `/data/master-mind/`（上游 repo）。那是另一个 AI 的工作目录，你的任何写入都会污染它。
- **禁止**在上游 repo 内执行 `git`、`python`、`arangodb` 等任何会改动文件的命令。
- 读取上游 repo 用于参考是可以的，但写只能写本 repo。
- 误写入上游 repo → 立即停止，告知用户，由用户决定如何处理。**不要自行回滚上游 repo 的文件**，那可能破坏另一个 AI 的未提交工作。

### 硬约束 2 · Git 协调规则

1. **只在 `glm5.2` 分支上工作**。不要 commit 到本地 `main`，不要 push 到 `main`。
2. **拿上游最新成果**：`git fetch origin` → 看 `git log origin/main` → 需要时 `git rebase origin/main` 或 `git merge origin/main` 到 `glm5.2`。注意：上游 AGENTS.md 和 dev-docs 也在被另一个 AI 改动，rebase/merge 时这些文件大概率冲突，需手动处理。
3. **送成果回上游**：`git push origin glm5.2`（**必须经用户当轮明确授权**）。另一个 AI 在上游 `git fetch` 后可见 `origin/glm5.2`。
4. **显式路径 add**：遵守全局规范，禁止 `git add -A`/`git add .`/`git add -u`，只 add 具体路径。
5. **改前清干净 + 改后立即 commit**：遵守全局 Git 管理协议。

### 硬约束 3 · 数据库完全隔离（最重要）

**本 repo 与上游 repo 共享同一台机器上的同一个 ArangoDB 实例（`localhost:8529`）。如果不做数据库隔离，两个 AI 的研究数据会互相覆盖、互相污染——这是最危险的隐性冲突。**

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

#### 数据库隔离硬规则

1. **本 repo 启动任何会连 ArangoDB 的脚本/服务前**，必须确认 `ARANGO_DB` 环境变量已设为 `xishujuzhen_math_glm52`。
2. **禁止**以 `xishujuzhen_math`（上游数据库名）连接 ArangoDB 做任何写操作。读可以（用于对比/迁移），但写绝对禁止。
3. **本 repo 首次初始化数据库时**，用 `arangodb_init.py`（环境变量化后）创建 `xishujuzhen_math_glm52`，不要复用上游的 `xishujuzhen_math`。
4. **运行 POC、研究 runtime、事件存储、启发规则存储**等所有会写库的代码前，先核对环境变量。
5. **环境变量化已实施**：运行写库脚本前，`source .env` 加载环境变量。若忘了 source，脚本会 fallback 到默认值 `xishujuzhen_math`（上游数据库）——所以 **每次运行前必须确认 `echo $ARANGO_DB` 输出 `xishujuzhen_math_glm52`**。

### 硬约束 4 · 其他共享资源意识

除 ArangoDB 外，以下资源也是共享的，使用前要意识到：

- **ArangoDB 实例** `localhost:8529`：共享，通过 DB_NAME 隔离（见上）。
- **文件系统**：本 repo 在内置 SSD，上游在 D 盘 HDD，物理隔离，无冲突。
- **网络端口**：如果本 repo 要起服务（如 ArangoDB Web、自定义 HTTP 服务），注意端口不要和上游冲突。起服务前先 `lsof -i :<port>` 检查。
- **Python 环境**：如果用同一个 Python venv/conda env，包安装会互相影响。建议本 repo 用独立 venv（见下）。

### Python 环境隔离（已实施）

本 repo 已创建独立 venv：
```bash
cd /data/master-mind-glm5.2-grove
python3 -m venv .venv          # python3.14
.venv/bin/pip install python-arango==8.3.3
```
- `.venv/` 已被 `.gitignore` 排除，不提交
- hooks 命令使用 `.venv/bin/python3`，与本 venv 一致
- 运行脚本时用 `.venv/bin/python3` 或先 `source .venv/bin/activate`

### Worktree 认知资产索引

本 section 是本 repo 的跨 Session 认知锚点。未来 AI 进入本 repo 时，从这里开始读。后续在本 repo 产生的工作认知，如果属于 worktree 隔离范畴，更新本 section；如果属于项目方法论，更新下游章节或 dev-docs。

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
- **本 repo（Master）**：`/data/master-mind-glm5.2-grove/`
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

---

