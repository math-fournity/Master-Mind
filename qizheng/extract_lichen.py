#!/usr/bin/env python3
"""
从 MinerU OCR 结果中提取立成表数据，生成校对底稿和 JSON 结构。

输入：dev-docs/原典/七政推步-MinerU-OCR/卷N-full.md
输出：
  - dev-docs/原典/七政推步-MinerU-OCR/校对底稿/卷N-表格M.md
  - qizheng/data/lichen_tables/*.json
"""
import json
import os
import re
from html.parser import HTMLParser

BASE = os.path.dirname(os.path.abspath(__file__))
OCR_DIR = os.path.join(BASE, "..", "dev-docs", "原典", "七政推步-MinerU-OCR")
PROOF_DIR = os.path.join(OCR_DIR, "校对底稿")
JSON_DIR = os.path.join(BASE, "..", "qizheng", "data", "lichen_tables")


class TableParser(HTMLParser):
    """解析 HTML 表格为结构化数据"""

    def __init__(self):
        super().__init__()
        self.tables = []
        self._table = None
        self._row = None
        self._cell = None
        self._attrs = {}

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "table":
            self._table = []
        elif tag == "tr" and self._table is not None:
            self._row = []
        elif tag in ("td", "th") and self._row is not None:
            self._cell = ""
            self._attrs = d

    def handle_endtag(self, tag):
        if tag == "table":
            if self._table:
                self.tables.append(self._table)
            self._table = None
        elif tag == "tr" and self._row is not None:
            self._table.append(self._row)
            self._row = None
        elif tag in ("td", "th") and self._cell is not None:
            cs = int(self._attrs.get("colspan", 1))
            rs = int(self._attrs.get("rowspan", 1))
            self._row.append({
                "text": self._cell.strip(),
                "colspan": cs,
                "rowspan": rs,
            })
            self._cell = None

    def handle_data(self, data):
        if self._cell is not None:
            self._cell += data


# OCR 常见误认修复
OCR_FIXES = {
    "三千秒": "三十秒",
    "五千秒": "五十秒",
    "五千分": "五十分",
    "三千分": "三十分",
    "比敷": "比數",
    "目分": "日分",
    "目+": "日+",
    "廿十": "二十",
    "廿十一": "二十一",
    "廿十二": "二十二",
    "廿十三": "二十三",
    "廿十四": "二十四",
    "廿十五": "二十五",
    "廿十六": "二十六",
    "廿十七": "二十七",
    "廿十八": "二十八",
    "廿十九": "二十九",
    "卅+": "三十",
}


def apply_ocr_fixes(text):
    """应用 OCR 误认修复"""
    for wrong, right in OCR_FIXES.items():
        text = text.replace(wrong, right)
    return text


def extract_tables(md_content):
    """从 Markdown 内容中提取所有 HTML 表格"""
    parser = TableParser()
    parser.feed(md_content)
    return parser.tables


def table_to_proof_markdown(table, table_idx, source_file):
    """将表格转为校对底稿 Markdown"""
    lines = []
    lines.append(f"## 表格 {table_idx}")
    lines.append(f"**来源**: {source_file}")
    lines.append(f"**行数**: {len(table)}")
    lines.append("")
    lines.append("| 行号 | 列内容 |")
    lines.append("|---|---|")

    for row_idx, row in enumerate(table):
        cells = []
        for cell in row:
            text = cell["text"]
            fixed = apply_ocr_fixes(text)
            if fixed != text:
                cells.append(f"~~{text}~~ → **{fixed}**")
            else:
                cells.append(text)
        lines.append(f"| {row_idx} | {' | '.join(cells)} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def table_to_json(table, table_idx, source_file, vol):
    """将表格转为 JSON 结构"""
    # 应用 OCR 修复
    fixed_table = []
    for row in table:
        fixed_row = []
        for cell in row:
            fixed_row.append({
                "text": apply_ocr_fixes(cell["text"]),
                "colspan": cell["colspan"],
                "rowspan": cell["rowspan"],
            })
        fixed_table.append(fixed_row)

    return {
        "id": f"vol{vol}-table{table_idx}",
        "volume": vol,
        "source": source_file,
        "ocr_status": "未校对",
        "rows": len(fixed_table),
        "data": fixed_table,
    }


def find_lichen_table_titles(md_content):
    """从文本中找立成表标题"""
    titles = []
    for line in md_content.split("\n"):
        if "立成" in line and "<table>" not in line:
            # 去掉多余空白
            title = line.strip()
            if title and len(title) < 100:
                titles.append(title)
    return titles


def main():
    os.makedirs(PROOF_DIR, exist_ok=True)
    os.makedirs(JSON_DIR, exist_ok=True)

    all_tables_json = []
    all_titles = {}

    for vol in range(1, 6):
        md_path = os.path.join(OCR_DIR, f"卷{vol}-full.md")
        if not os.path.exists(md_path):
            print(f"  跳过卷{vol}: 文件不存在")
            continue

        with open(md_path, encoding="utf-8") as f:
            content = f.read()

        tables = extract_tables(content)
        titles = find_lichen_table_titles(content)
        all_titles[f"卷{vol}"] = titles

        print(f"卷{vol}: {len(tables)} 个表格, {len(titles)} 个立成表标题")

        # 生成校对底稿
        proof_path = os.path.join(PROOF_DIR, f"卷{vol}-校对底稿.md")
        with open(proof_path, "w", encoding="utf-8") as f:
            f.write(f"# 卷{vol} 立成表校对底稿\n\n")
            f.write(f"**来源**: {md_path}\n")
            f.write(f"**表格数**: {len(tables)}\n")
            f.write(f"**立成表标题**:\n")
            for t in titles:
                f.write(f"- {t}\n")
            f.write(f"\n---\n\n")
            for i, table in enumerate(tables):
                f.write(table_to_proof_markdown(table, i + 1, f"卷{vol}-full.md"))

        # 生成 JSON
        for i, table in enumerate(tables):
            j = table_to_json(table, i + 1, f"卷{vol}-full.md", vol)
            json_path = os.path.join(JSON_DIR, f"vol{vol}_table{i+1:02d}.json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(j, f, ensure_ascii=False, indent=2)
            all_tables_json.append(j)

    # 生成总索引
    index_path = os.path.join(JSON_DIR, "_index.json")
    index = {
        "description": "七政推步立成表数据（从 MinerU OCR 提取，未校对）",
        "source": "dev-docs/原典/七政推步-MinerU-OCR/卷1-5-full.md",
        "ocr_tool": "MinerU 3.4.0",
        "ocr_status": "未校对",
        "total_tables": len(all_tables_json),
        "volumes": {
            f"卷{v}": {
                "tables": len([t for t in all_tables_json if t["volume"] == v]),
                "titles": all_titles.get(f"卷{v}", []),
            }
            for v in range(1, 6)
        },
        "known_ocr_issues": [
            "三千秒→三十秒",
            "比敷/比數混用",
            "竖排阅读顺序部分错乱",
            "部分数值有误",
        ],
        "tables": [t["id"] for t in all_tables_json],
    }
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"\n总计: {len(all_tables_json)} 个表格")
    print(f"校对底稿: {PROOF_DIR}/")
    print(f"JSON数据: {JSON_DIR}/")


if __name__ == "__main__":
    main()
