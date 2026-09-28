# Preupload Inventory — 敏感内容文件级清单（2026-09-28 基线）

> 性质：上传前 Gate 执行用的逐文件量化基线；**只含路径与命中计数，不含任何敏感值**。
> 真实路径映射见上级目录 `paths.local.md`（gitignored）。

## 文件

| 文件 | 内容 | 行数（含表头） |
|---|---|---|
| `inventory-token.tsv` | 敏感 token 逐文件命中（HOME 394 / ORIGIN 33 / GROVE 190） | 618 |
| `inventory-secret.tsv` | ArangoDB 明文口令逐文件命中（HOME 435 / ORIGIN 29 / GROVE 49） | 514 |
| `inventory-privatepaths.tsv` | 私有路径逐文件命中，kind 区分 users_path/dvol_path（HOME 564+620 / ORIGIN 7+33 / GROVE 278+429） | 1932 |
| `inventory-emails.tsv` | 邮箱样串逐文件命中（HOME 180 / ORIGIN 177 / GROVE 177，多为 arxiv 全文） | 536 |

## 重生成方法（Gate 执行当日必须重跑并以新结果为权威）

```bash
# 对每个成员仓（HOME/ORIGIN/GROVE，路径见 paths.local.md）：
# 四个待扫模式的字面量均不落盘（口头/本地补全）：敏感token（成员目录名中的词）、DB明文口令、
# 用户主目录前缀、数据卷前缀。下文以 $TOKEN/$DB_SECRET/$USER_HOME/$DATA_VOL 代指。
cd <成员仓>
git grep -c "$TOKEN"       # → inventory-token.tsv（补 repo 列）
git grep -c "$DB_SECRET"   # → inventory-secret.tsv
git grep -c "$USER_HOME" && git grep -c "$DATA_VOL"   # → inventory-privatepaths.tsv（kind 列区分）
git grep -cE '[a-zA-Z0-9._%+-]+@(proton|gmail|qq|163)\.'  # → inventory-emails.tsv
```

## 边界与注意事项

- `git grep` 只覆盖 tracked 文件；Gate 时还需对新 untracked/ignored 内容单独复扫。
- 模式按 `path:count` 切分，路径若含 `:` 会错位（2026-09-28 基线三仓无此情况）。
- 历史侧（commit message）命中另见 `topology-findings.md` §6；历史文件路径三仓均为 0。
- **归零判据**：清除完成后，本目录四份 TSV 重生成均为仅表头，且 `git log --all --format=%B |
  grep` 对 token/口令归零，方视为 Gate 1/2 项通过。
- 本基线入库后内容会随治理工作漂移，仅作起点与量级参照；执行以当日重扫为准。
