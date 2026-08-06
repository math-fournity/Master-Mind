---
description: >
  查询、下载和管理外部数学题库数据集的工作流。
  通过ArangoDB math_datasets集合查询10063个数据集的元数据（描述/题量/格式/下载状态/本地路径等），
  支持按数学门类/难度/来源类型/Tier筛选，支持下载状态更新。
  参考文档：dev-docs/212-v3-2026-08-06-数学各门类可下载题海清单.md
  WHEN to use: 被 math-datasets-trigger 规则触发时。
  WHEN NOT to use: 项目内部认知图操作、一般代码编写。
---

# math-datasets skill

## 数据库连接

```python
from arango import ArangoClient
client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
col = db.collection('math_datasets')
```

**硬约束**：必须用 `xishujuzhen_math_glm52`，禁止写 `xishujuzhen_math`（上游数据库）。

## 工作流

### WF1. 查询数据集

按需选择查询模式：

```python
# 按关键词搜索
db.aql.execute('FOR d IN math_datasets FILTER CONTAINS(LOWER(d.title), "numina") OR CONTAINS(LOWER(d.description), "numina") RETURN d')

# 按数学门类筛选
db.aql.execute('FOR d IN math_datasets FILTER "geometry" IN d.math_domain RETURN {title: d.title, desc: d.description, count: d.problem_count}')

# 按难度筛选
db.aql.execute('FOR d IN math_datasets FILTER "competition" IN d.difficulty_level RETURN d')

# 按来源类型筛选
db.aql.execute('FOR d IN math_datasets FILTER "formal" IN d.source_type RETURN {title: d.title, desc: d.description, url: d.url}')

# 按Tier筛选（1=≥1万次下载，2=1千-1万，3=100-1千，4=<100）
db.aql.execute('FOR d IN math_datasets FILTER d.tier == 1 SORT d.downloads DESC RETURN {repo_id: d.repo_id, desc: d.description, downloads: d.downloads}')

# 查下载状态
db.aql.execute('FOR d IN math_datasets FILTER d.download_status == "completed" RETURN {title: d.title, path: d.local_path, size: d.local_size}')

# 查抗污染数据集
db.aql.execute('FOR d IN math_datasets FILTER d.anti_contamination == true RETURN {title: d.title, desc: d.description}')
```

### WF2. 下载新数据集

1. 查数据库确认是否已下载：`FILTER d.repo_id == "xxx" RETURN d.download_status`
2. 确定下载路径：`/data/hf_math_datasets/<repo_id>/` 或 `knowledge/problem_banks/<name>/`
3. 在tmux中启动下载：
   - HuggingFace: `hf download <repo_id> --repo-type dataset --local-dir <path>`
   - GitHub: `git clone <url> <path>` 或 `curl -L -o <path>/repo.zip <archive_url>`
4. 下载完成后更新数据库：
   ```python
   col.update_match({"repo_id": "<repo_id>"}, {
       "download_status": "completed",
       "download_date": "2026-08-06",
       "local_path": "<path>",
       "local_size": "<size>",
       "file_count": <count>
   })
   ```

### WF3. 入库新数据集

```python
record = {
    "_key": sanitize_key(f"hf_{repo_id}"),
    "repo_id": repo_id,
    "platform": "huggingface",
    "title": title,
    "description": "数据集是什么——完整描述",
    "unique_value": "为什么重要",
    "problem_count": count,
    "format": ["parquet"],
    "source_type": ["competition"],
    "math_domain": ["algebra"],
    "difficulty_level": ["competition"],
    "has_solutions": True,
    "solution_format": ["cot"],
    "url": f"https://huggingface.co/datasets/{repo_id}",
    "download_status": "not_started",
    "ingest_source": "manual",
    "ingest_date": "2026-08-06",
    "last_updated": "2026-08-06",
}
col.insert(record)
```

### WF4. 批量自动分类

对未分类数据集（source_type含"unknown"）按名称关键词自动标注：

```python
KEYWORDS = {
    "competition": ["olympiad", "competition", "contest", "aime", "amc", "imo", "usamo"],
    "k12": ["gsm", "grade", "school", "elementary", "word_problem"],
    "formal": ["lean", "coq", "isabelle", "proof", "theorem"],
    "multimodal": ["vision", "image", "chart", "geometry", "figure", "diagram"],
    "synthetic": ["synthetic", "generated", "augmented", "evol"],
}
# 遍历未分类记录，按repo_id/title匹配关键词，更新source_type
```

## 参考文档

- **dev-docs/212-v3-2026-08-06-数学各门类可下载题海清单.md**：方法论骨架（总思路/来源分类/存储结构/分层测试策略）
- **knowledge/problem_banks/math_datasets_catalog_v2.json**：完整目录JSON快照
- **scripts/ingest_hf_math_datasets_v2.py**：批量入库脚本

## Schema速查

9类字段：标识 / 价值描述 / 内容属性 / 来源归属 / HF-GitHub元数据 / 获取 / 下载状态 / 项目相关性 / 入库管理

详见212号文档§4.1或脚本头部的schema注释。
