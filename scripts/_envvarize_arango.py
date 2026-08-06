#!/usr/bin/env python3
"""一次性脚本：把 xishujuzhen/ 下所有 ArangoDB 硬编码环境变量化。

改动模式（保持默认值不变，只允许环境变量覆盖）：
  DB_NAME = "xishujuzhen_math"
    → DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")
  ARANGO_HOST = "http://localhost:8529"
    → ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")
  ArangoClient(hosts="http://localhost:8529")
    → ArangoClient(hosts=os.environ.get("ARANGO_HOST", "http://localhost:8529"))
  client.db("xishujuzhen_math", ...)
    → client.db(os.environ.get("ARANGO_DB", "xishujuzhen_math"), ...)
  client.db("xishujuzhen", ...)
    → client.db(os.environ.get("ARANGO_DB", "xishujuzhen"), ...)
  db_name="xishujuzhen_math"
    → db_name=os.environ.get("ARANGO_DB", "xishujuzhen_math")

同时确保每个改动过的文件有 import os。
"""
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..", "xishujuzhen")
ROOT = os.path.normpath(ROOT)

# (pattern, replacement) — 顺序敏感
REPLACEMENTS = [
    # DB_NAME 赋值
    (
        'DB_NAME = "xishujuzhen_math"',
        'DB_NAME = os.environ.get("ARANGO_DB", "xishujuzhen_math")',
    ),
    # ARANGO_HOST 赋值
    (
        'ARANGO_HOST = "http://localhost:8529"',
        'ARANGO_HOST = os.environ.get("ARANGO_HOST", "http://localhost:8529")',
    ),
    # inline ArangoClient(hosts=...)
    (
        'ArangoClient(hosts="http://localhost:8529")',
        'ArangoClient(hosts=os.environ.get("ARANGO_HOST", "http://localhost:8529"))',
    ),
    # inline client.db("xishujuzhen_math", ...)
    (
        'client.db("xishujuzhen_math",',
        'client.db(os.environ.get("ARANGO_DB", "xishujuzhen_math"),',
    ),
    # inline client.db("xishujuzhen", ...)  — 星学遗留，保持默认值
    (
        'client.db("xishujuzhen",',
        'client.db(os.environ.get("ARANGO_DB", "xishujuzhen"),',
    ),
    # inline db_name="xishujuzhen_math" in function calls/defaults
    (
        'db_name="xishujuzhen_math"',
        'db_name=os.environ.get("ARANGO_DB", "xishujuzhen_math")',
    ),
]


def ensure_import_os(content: str) -> str:
    """如果文件没有 import os，在第一个 import/from 行前插入。"""
    if re.search(r"^import os\b", content, re.MULTILINE):
        return content
    # 找第一个 import 或 from ... import 行
    match = re.search(r"^(import |from \S+ import )", content, re.MULTILINE)
    if match:
        pos = match.start()
        return content[:pos] + "import os\n" + content[pos:]
    # 没有 import 行：在 shebang + docstring 之后插入
    # 简单 fallback：文件开头插入
    return "import os\n" + content


def process_file(path: str) -> list[str]:
    """处理单个文件，返回应用的改动描述列表。"""
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    content = original
    changes = []

    for pattern, replacement in REPLACEMENTS:
        count = content.count(pattern)
        if count > 0:
            content = content.replace(pattern, replacement)
            changes.append(f"  {count}x: {pattern[:50]}...")

    if content == original:
        return []  # 无改动

    # 确保 import os
    content = ensure_import_os(content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return changes


def main():
    changed_files = []
    skipped = []

    for dirpath, dirnames, filenames in os.walk(ROOT):
        # 跳过 __pycache__
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        for fname in filenames:
            if not fname.endswith(".py"):
                continue
            fpath = os.path.join(dirpath, fname)
            changes = process_file(fpath)
            if changes:
                rel = os.path.relpath(fpath)
                changed_files.append((rel, changes))
            else:
                skipped.append(os.path.relpath(fpath))

    print(f"=== 改动文件 ({len(changed_files)}) ===")
    for rel, changes in sorted(changed_files):
        print(f"\n{rel}:")
        for c in changes:
            print(c)

    print(f"\n=== 跳过文件 ({len(skipped)}) ===")
    for rel in sorted(skipped):
        print(f"  {rel}")


if __name__ == "__main__":
    main()
