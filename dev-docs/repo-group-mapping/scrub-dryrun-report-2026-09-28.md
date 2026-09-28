# Scrub Dry-Run Report — Wave 0（2026-09-28）

> 性质：上传前历史改写的 **scratch 演练报告**。生产三仓全程零写入（只读）；全部改写发生在
> `/tmp/mm-scrub-20260928/` 的一次性镜像克隆（`--no-local` 克隆，无硬链接回生产仓）。生产仓
> 均为 clean 已提交状态，任何演练结果不可接受时直接丢弃 scratch 即可——**可修复性由构造保证**。
> 报告本身不含任何敏感字面量（token/口令/JWT 值一律以代称出现）。

## 1. 演练配置

- 工具：`git-filter-repo`（本机 `~/.local/bin`）。
- 镜像：ORIGIN/GROVE/HOME 三个 `git clone --mirror --no-local`。
- Pass 1：`--replace-text` + `--replace-message`，四条字面量替换规则（敏感token→master-mind、
  DB明文口令→REDACTED 占位、用户主目录前缀→`~`、数据卷前缀→`/data`；规则文件仅存 /tmp）。
- Pass 2：`--invert-paths --path xishujuzhen/mitm_thinking_intercept/sample_capture`（二进制凭证
  载体目录整体移除，见 §3）。
- 验证：commit 数守恒、tag 名保全、`git cat-file --batch-all-objects --batch` 全对象存储流式
  复扫四模式（单一 Python 解析器逐对象计数，含二进制）。

## 2. 结果矩阵

| 检查 | ORIGIN | GROVE | HOME |
|---|---|---|---|
| glm5.2/main commit 数（改写后=源） | 302=302 | 601=601（pass2 前后均 601） | 1404=1404（pass2 前后均 1404） |
| codex 分支数守恒 | - | - | 1401/1409 均守恒 |
| tag 名保全 | 3/3 | 4/4 | 10/10 |
| 全存储·敏感token | 0 | 0 | 0 |
| 全存储·DB口令 | 0 | 0 | 0 |
| 全存储·用户主目录前缀 | 0 | 0 | 0 |
| 全存储·数据卷前缀 | 0 | 0 | 0 |
| tip 抽样语义 | - | AGENTS 路径已相对化 | AGENTS 首行已为 `~/master-mind-…` |

## 3. 过程发现（重要，超出机械验证）

1. **`--replace-text` 跳过二进制 blob**：Pass 1 后 GROVE/HOME 各残留同一 86KB 二进制 blob
   （两仓同对象、49+2 处私有路径）。定位（Python 逐对象计数）后确认载体是
   `xishujuzhen/mitm_thinking_intercept/sample_capture/`（5 个 `.bin`，HOME/GROVE 各 5、
   ORIGIN 0，由共享线单提交 `7bd106f` 引入）。
2. **该目录内含真实凭证**：MITM 抓包捕获了 Devin CLI 会话材料，其中包含一枚 session JWT
   （值不落盘、不展示）。这把"二进制凭证"从假想风险变成已证实风险：
   - Gate 新增必做项：**Devin session 凭证轮换/失效确认**（与 DB 口令轮换并列）；
   - 上传处置建议：该目录从上传历史整体移除（Pass 2 已按此演练，commit 数守恒无副作用）；
   - Gate 新增必做项：**全库二进制凭证专项扫描**（本演练只扫四个文本模式；JWT/API key 的
     模式与熵扫描需单独跑）。
3. **`refs/codex/turn-diffs/checkpoints/*`（HOME 4 条工具检查点 ref）默认不被 filter-repo 处理**
   且快照未清洗内容。处置：scratch 中删除（上传范围本就只含 heads+tags，不含工具命名空间）。
   该 ref 类目已列入 Wave 1 推送清单的显式排除项。
4. annotated tag message 在本三仓中未携带目标模式（无需重造 tag 对象；若未来发现携带，
   应使用 `--tag-callback` 保持 tagger 身份，避免用 `git tag -f` 造成身份漂移）。

## 4. 验证深度声明

- 全对象存储复扫 = 覆盖所有 blob/commit/tag/tree（含二进制），非仅 tip 级。
- commit message 复扫包含在全存储扫描内。
- 未覆盖：邮箱模式（按待裁定项 4 暂不动）；四个文本模式之外的凭证形态（见 §3.2 专项）。

## 5. 结论与剩余门槛

- **Wave 0 = PASS**：改写配方（replace-text + replace-message + sample_capture 移除 +
  codex 检查点 ref 排除）在三仓全量归零且结构守恒。
- 真实上传前仍需：用户逐 wave 授权；343MB 级大文件处置决策（见 topology-findings §6）；
  邮箱裁定；两项凭证轮换；二进制凭证专项扫描；`filter-repo` 最终运行时的 SHA 映射落盘。
- 演练产物位于 /tmp，重启即失；本报告为唯一持久收据。
