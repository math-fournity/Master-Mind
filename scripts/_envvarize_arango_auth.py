#!/usr/bin/env python3
"""一次性脚本：把 xishujuzhen/ 下所有 ArangoDB 用户名/密码硬编码环境变量化。

改动模式（保持默认值不变，只允许环境变量覆盖）：
  DB_USER = "root"        → DB_USER = os.environ.get("ARANGO_USER", "root")
  DB_PASS = "REDACTED-DB-PASSWORD"    → DB_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")
  ARANGO_USER = "root"    → ARANGO_USER = os.environ.get("ARANGO_USER", "root")
  ARANGO_PASS = "REDACTED-DB-PASSWORD"→ ARANGO_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")
  username="root"         → username=os.environ.get("ARANGO_USER", "root")
  password="REDACTED-DB-PASSWORD"     → password=os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")

不改动：
  username=username / password=password  （参数传递，用的是已环境变量化的变量）
  client.db("_system", ...)  中的 _system 是系统库固定名，不改

同时确保每个改动过的文件有 import os。
"""
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..", "xishujuzhen")
ROOT = os.path.normpath(ROOT)

REPLACEMENTS = [
    # 变量赋值
    ('DB_USER = "root"', 'DB_USER = os.environ.get("ARANGO_USER", "root")'),
    ('DB_PASS = "REDACTED-DB-PASSWORD"', 'DB_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")'),
    ('ARANGO_USER = "root"', 'ARANGO_USER = os.environ.get("ARANGO_USER", "root")'),
    ('ARANGO_PASS = "REDACTED-DB-PASSWORD"', 'ARANGO_PASS = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")'),
    # inline 调用参数
    ('username="root"', 'username=os.environ.get("ARANGO_USER", "root")'),
    ('password="REDACTED-DB-PASSWORD"', 'password=os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")'),
]


def ensure_import_os(content: str) -> str:
    if re.search(r"^import os\b", content, re.MULTILINE):
        return content
    match = re.search(r"^(import |from \S+ import )", content, re.MULTILINE)
    if match:
        pos = match.start()
        return content[:pos] + "import os\n" + content[pos:]
    return "import os\n" + content


def process_file(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    content = original
    changes = []

    for pattern, replacement in REPLACEMENTS:
        count = content.count(pattern)
        if count > 0:
            content = content.replace(pattern, replacement)
            changes.append(f"  {count}x: {pattern[:50]}")

    if content == original:
        return []

    content = ensure_import_os(content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return changes


def main():
    changed_files = []
    skipped = []

    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        for fname in filenames:
            if not fname.endswith(".py"):
                continue
            fpath = os.path.join(dirpath, fname)
            changes = process_file(fpath)
            if changes:
                changed_files.append((os.path.relpath(fpath), changes))
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
