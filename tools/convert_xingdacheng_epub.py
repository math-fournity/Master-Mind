#!/usr/bin/env python3
"""
星学大成 EPUB → 结构化 Markdown 转换脚本 v2

epub 结构：每个卷的 h1 标题在一个 xhtml 文件中，
卷内容（h2/h3/h4）在后续的 xhtml 文件中。
遇到 h1 开始新卷，后续无 h1 的文件归入当前卷。

用法：
    python3 tools/convert_xingdacheng_epub.py
"""
import os
import re
from html.parser import HTMLParser

EPUB_EXTRACT = "/tmp/epub_extract"
TEXT_DIR = os.path.join(EPUB_EXTRACT, "OEBPS", "Text")
OUTPUT_DIR = "~/MOIRA_chinese_astrology-main/dev-docs/原典/星学大成-epub版"

NUM_MAP = {'一': '01', '二': '02', '三': '03', '四': '04',
           '五': '05', '六': '06', '七': '07', '八': '08',
           '九': '09', '十': '10', '十一': '11', '十二': '12',
           '十三': '13', '十四': '14', '十五': '15', '十六': '16',
           '十七': '17', '十八': '18', '十九': '19', '二十': '20',
           '二十一': '21', '二十二': '22', '二十三': '23', '二十四': '24',
           '二十五': '25', '二十六': '26', '二十七': '27', '二十八': '28',
           '二十九': '29', '三十': '30'}


class MarkdownExtractor(HTMLParser):
    """从 xhtml 提取 Markdown，保留标题层级和段落"""

    def __init__(self):
        super().__init__()
        self.result = []
        self.skip = False
        self.heading_level = 0
        self.heading_text = ""
        self.in_heading = False
        self.p_text = ""
        self.in_p = False

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'head'):
            self.skip = True
            return
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.in_heading = True
            self.heading_level = int(tag[1])
            self.heading_text = ""
        elif tag == 'p':
            self.in_p = True
            self.p_text = ""
        elif tag == 'br':
            if self.in_p:
                self.p_text += '\n'
            else:
                self.result.append('\n')
        elif tag == 'img':
            # 跳过图片，记录占位
            self.result.append('\n\n[图]\n')
        elif tag == 'div':
            if self.result and self.result[-1] and not self.result[-1].endswith('\n'):
                self.result.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'head'):
            self.skip = False
            return
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6') and self.in_heading:
            text = self.heading_text.strip()
            if text:
                # h1→#, h2→##, h3→###, h4→####
                level = self.heading_level
                self.result.append(f'\n\n{"#" * level} {text}\n')
            self.in_heading = False
            self.heading_level = 0
            self.heading_text = ""
        elif tag == 'p' and self.in_p:
            text = self.p_text.strip()
            if text:
                self.result.append(f'\n\n{text}\n')
            self.in_p = False
            self.p_text = ""
        elif tag == 'div':
            if self.result and self.result[-1] and not self.result[-1].endswith('\n\n'):
                self.result.append('\n')

    def handle_data(self, data):
        if self.skip:
            return
        if self.in_heading:
            self.heading_text += data
        elif self.in_p:
            self.p_text += data
        else:
            text = data.strip()
            if text:
                self.result.append(text)

    def get_markdown(self):
        text = ''.join(self.result)
        text = re.sub(r'\n{4,}', '\n\n\n', text)
        return text.strip()


def extract_xhtml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    extractor = MarkdownExtractor()
    extractor.feed(content)
    return extractor.get_markdown()


def get_h1_title(filepath):
    """提取文件的 h1 标题，没有则返回 None"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if match:
        return match.group(1).strip()
    return None


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 获取所有 part 文件（按顺序）
    files = sorted(
        f for f in os.listdir(TEXT_DIR)
        if f.startswith('part') and f.endswith('.xhtml')
    )

    # 按 h1 分组：遇到 h1 开始新组，后续无 h1 的文件归入当前组
    groups = []  # [(h1_title, [filepaths])]
    current_title = None
    current_files = []

    for fname in files:
        filepath = os.path.join(TEXT_DIR, fname)
        h1 = get_h1_title(filepath)

        if h1:
            # 保存上一组
            if current_title is not None:
                groups.append((current_title, current_files))
            current_title = h1
            current_files = [filepath]
        else:
            if current_title is not None:
                current_files.append(filepath)
            else:
                # h1 之前的前置内容（cover_page, TOC 等）
                # 跳过 cover 和 TOC
                if 'cover' in fname or 'part0000' in fname or 'part0001' in fname:
                    continue
                # part0005 是上册扉页，也跳过
                if 'part0005' in fname:
                    continue
                # 其他归入"前置内容"组
                if not groups or groups[-1][0] != '__front_matter__':
                    groups.append(('__front_matter__', []))
                groups[-1][1].append(filepath)

    # 保存最后一组
    if current_title is not None:
        groups.append((current_title, current_files))

    print(f"共 {len(groups)} 组")

    # 生成文件
    for title, filepaths in groups:
        # 合并该组所有文件的 Markdown
        md_parts = []
        for fp in filepaths:
            md = extract_xhtml(fp)
            if md:
                md_parts.append(md)

        if not md_parts:
            continue

        full_md = '\n\n---\n\n'.join(md_parts)

        if title == '__front_matter__':
            out_name = "00-提要序凡例.md"
        else:
            # "星学大成卷一" → 提取卷号
            juan_match = re.search(r'卷([一二三四五六七八九十]+)', title)
            if juan_match:
                juan_str = juan_match.group(1)
                num = NUM_MAP.get(juan_str, juan_str)
                out_name = f"{num}-{title}.md"
            else:
                # 提要、原序、凡例
                out_name = f"00-{title}.md"

        out_path = os.path.join(OUTPUT_DIR, out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full_md)
            f.write('\n')

        size_kb = os.path.getsize(out_path) / 1024
        n_files = len(filepaths)
        print(f"  {out_name} ({size_kb:.1f} KB, {n_files} 源文件)")

    # 生成索引
    index_path = os.path.join(OUTPUT_DIR, "README.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# 星学大成 · epub 版\n\n")
        f.write("**来源**：星学大成(套装共2册) epub，万民英著\n\n")
        f.write("**转换方式**：epub xhtml → Markdown，保留 h1-h4 标题层级\n\n")
        f.write("**校勘对照**：kanripo 四库全书文渊阁本在 `外部系统/星学大成/`（繁体无标点）\n\n")
        f.write("---\n\n## 目录\n\n")

        for title, _ in groups:
            if title == '__front_matter__':
                f.write("- [00-提要序凡例.md](00-提要序凡例.md)\n")
            else:
                juan_match = re.search(r'卷([一二三四五六七八九十]+)', title)
                if juan_match:
                    juan_str = juan_match.group(1)
                    num = NUM_MAP.get(juan_str, juan_str)
                    f.write(f"- [{num}-{title}.md]({num}-{title}.md)\n")
                else:
                    f.write(f"- [00-{title}.md](00-{title}.md)\n")

    print(f"\n索引：{index_path}")
    print("完成。")


if __name__ == "__main__":
    main()
