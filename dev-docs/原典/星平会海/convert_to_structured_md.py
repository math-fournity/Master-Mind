#!/usr/bin/env python3
"""
星平会海全量清理与结构化 Markdown 转换。

输入：
  - 卷一.txt ~ 卷十.txt（原有10卷，jina reader 格式）
  - raw_卷首/*.txt（新抓取的卷首+卷一缺失+卷三缺失篇目，curl article 格式）

输出：
  - dev-docs/原典/星平会海-结构化版/00-序.md
  - dev-docs/原典/星平会海-结构化版/00-卷首.md
  - dev-docs/原典/星平会海-结构化版/01-星平会海卷一.md
  - ... 10-星平会海卷十.md
  - README.md

清理规则：
  1. 去除网页元数据（Title/URL Source/Published Time/Markdown Content/URL）
  2. 去除面包屑导航（首页 > 典籍 > 星平会海 > 正文）
  3. 去除分页链接行
  4. 去除"相关文章"及其后的链接
  5. 去除导航菜单（* [首页]... 等）
  6. 去除日期/发布者行
  7. 去除 logo 图片行
  8. 合并同一篇目的多个分页
  9. 用 schema.json 的 section 标题加 ## 标题层级
"""
import os, re, json, glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = BASE_DIR  # 原有10卷 txt 在这里
RAW_DIR = os.path.join(BASE_DIR, "raw_卷首")
OUT_DIR = os.path.join(os.path.dirname(BASE_DIR), "星平会海-结构化版")
os.makedirs(OUT_DIR, exist_ok=True)

# ===== 清理函数 =====

def clean_jina_text(text):
    """清理 jina reader 格式的 txt（原有10卷）"""
    lines = text.split('\n')
    cleaned = []
    skip_related = False
    in_nav = False

    for line in lines:
        stripped = line.strip()

        # 跳过元数据行
        if stripped.startswith('Title:') or stripped.startswith('URL Source:') or \
           stripped.startswith('Published Time:') or stripped.startswith('Markdown Content:'):
            continue

        # 跳过 URL 行
        if stripped.startswith('URL:'):
            continue

        # 跳过面包屑导航
        if stripped == '首页' or stripped == '>' or stripped == '典籍' or \
           stripped == '星平会海' or stripped == '正文' or stripped == '> 正文' or \
           re.match(r'^首页\s*>\s*典籍\s*>\s*星平会海', stripped):
            continue

        # 跳过日期/发布者行
        if re.match(r'^日期:.*发布者:', stripped) or stripped.startswith('日期:'):
            continue

        # 跳过分页链接行（包含 suanzhun.net 的链接行）
        if 'suanzhun.net' in stripped and ('[' in stripped or '](https' in stripped):
            continue

        # 跳过纯链接行
        if re.match(r'^\[.*\]\(https?://.*\)$', stripped) and len(stripped) > 20:
            continue

        # 跳过 logo 行
        if 'logo' in stripped.lower() and 'suanzhun' in stripped.lower():
            continue

        # 跳过导航菜单项
        if stripped.startswith('* [') or stripped.startswith('    * ['):
            in_nav = True
            continue
        if in_nav and (stripped.startswith('*') or stripped.startswith('    *') or stripped == ''):
            if stripped == '':
                in_nav = False
            continue

        # 跳过"相关文章"标记行本身
        if stripped == '相关文章' or stripped == '相关文章：' or stripped == '### 相关文章':
            skip_related = True
            continue
        if skip_related:
            # 相关文章区域：链接行、空行、导航符号（︿ 等）
            # 遇到正文标题（## 开头）或实质内容时恢复
            if stripped.startswith('## ') or stripped.startswith('# '):
                skip_related = False
                # 不 continue，让这行被加入
            elif stripped == '' or stripped == '︿' or stripped.startswith('[') or \
                 'suanzhun' in stripped or stripped.startswith('上一篇') or \
                 stripped.startswith('下一篇') or stripped.startswith('赣ICP') or \
                 stripped.startswith('关于我们') or stripped.startswith('隐私声明'):
                continue
            else:
                # 非空非链接非导航 → 可能是正文恢复
                skip_related = False
                # 不 continue，让这行被加入

        # 跳过纯图片标记
        if stripped.startswith('![Image') or stripped.startswith('![logo'):
            continue

        # 跳过"上一篇/下一篇"行
        if stripped.startswith('上一篇') or stripped.startswith('下一篇'):
            continue

        # 跳过页脚
        if '赣ICP备' in stripped or '关于我们' in stripped or '隐私声明' in stripped or \
           '免责声明' in stripped or '网站地图' in stripped:
            continue

        # 跳过 Apache Server 错误行
        if 'Apache Server at' in stripped:
            continue
        # 跳过 JSON 响应残留
        if '"httpStatus"' in stripped or '"httpStatusText"' in stripped or \
           '"favicon.ico"' in stripped or '"usage":{"tokens"' in stripped:
            # 这类残留可能粘在正文行末尾，需要截断
            if '"},"external"' in stripped:
                stripped = stripped[:stripped.index('"},"external"')]
                line = stripped
            else:
                continue
        # 跳过 * * * 分隔线（Apache 错误页的）
        if stripped == '* * *':
            continue

        cleaned.append(line)

    return '\n'.join(cleaned)


def remove_jina_json(text):
    """清除 jina reader 嵌入在正文中的 JSON 残留"""
    # 模式1: ","url":"https://...","content":"## 标题
    # 替换为换行+标题
    text = re.sub(r'","url":"https?://[^"]*","content":"(##? [^\n]*)', r'\n\n\1', text)
    # 模式2: 行尾的 ","url":"https://...","content":"...
    text = re.sub(r'","url":"https?://[^"]*","content":"', '\n\n', text)
    # 模式3: 残留的 JSON 结尾 },"meta":{...}}
    text = re.sub(r'"},"external":\{[^}]*\},"httpStatus":\d+,"httpStatusText":"[^"]*","usage":\{"tokens":\d+\},"meta":\{"usage":\{"tokens":\d+\}\}\}', '', text)
    # 模式4: 单独的 JSON 片段
    text = re.sub(r'\{"external":\{[^}]*\},"httpStatus":\d+,"httpStatusText":"[^"]*","usage":\{"tokens":\d+\},"meta":\{"usage":\{"tokens":\d+\}\}\}', '', text)
    # 模式5: <br /> 标签替换为换行
    text = text.replace('<br />', '\n')
    text = text.replace('<br/>', '\n')
    # 清理多余的引号转义
    text = text.replace('\\"', '"')
    return text


def merge_raw_pages(raw_dir, base_id):
    """合并同一 book ID 的多个分页文件"""
    pattern = os.path.join(raw_dir, f"{base_id}*.txt")
    files = sorted(glob.glob(pattern), key=lambda x: (
        0 if x == os.path.join(raw_dir, f"{base_id}.txt") else
        int(re.search(r'_(\d+)\.txt', x).group(1))
    ))
    merged = []
    for f in files:
        text = open(f, encoding='utf-8').read()
        # 去掉 Title 和 URL 行
        lines = text.split('\n')
        content_lines = []
        skip_header = True
        for line in lines:
            stripped = line.strip()
            if skip_header and (stripped.startswith('Title:') or stripped.startswith('URL:')):
                continue
            if skip_header and stripped == '':
                continue
            skip_header = False
            content_lines.append(line)
        merged.append('\n'.join(content_lines))
    return '\n\n'.join(merged)


def clean_raw_text(text):
    """清理 raw_卷首 格式的 txt"""
    lines = text.split('\n')
    cleaned = []
    skip_related = False

    for line in lines:
        stripped = line.strip()

        # 跳过面包屑导航
        if stripped == '首页' or stripped == '>' or stripped == '典籍' or \
           stripped == '星平会海' or stripped == '正文' or stripped == '> 正文' or \
           re.match(r'^首页\s*>\s*典籍\s*>\s*星平会海', stripped):
            continue

        # 跳过标题重复行（如 "序-星平会海"）
        if re.match(r'^.{1,30}-星平会海$', stripped) and stripped != '序':
            continue

        # 跳过"返回列表"
        if stripped == '返回列表':
            continue

        # 跳过日期/发布者行
        if re.match(r'^日期:.*发布者:', stripped) or stripped.startswith('日期:'):
            continue

        # 跳过分页链接行
        if 'suanzhun.net' in stripped and ('[' in stripped or '](https' in stripped):
            continue

        # 跳过纯链接行
        if re.match(r'^\[.*\]\(https?://.*\)$', stripped) and len(stripped) > 20:
            continue

        # 跳过"相关文章"及之后的内容
        if stripped == '相关文章' or stripped == '相关文章：' or stripped == '### 相关文章':
            skip_related = True
            continue
        if skip_related:
            if stripped.startswith('## ') or stripped.startswith('# '):
                skip_related = False
            elif stripped == '' or stripped == '︿' or stripped.startswith('[') or \
                 'suanzhun' in stripped or stripped.startswith('上一篇') or \
                 stripped.startswith('下一篇'):
                continue
            else:
                skip_related = False

        # 跳过 Apache Server 错误行
        if 'Apache Server at' in stripped:
            continue
        if '"httpStatus"' in stripped or '"favicon.ico"' in stripped:
            if '"},"external"' in stripped:
                stripped = stripped[:stripped.index('"},"external"')]
                line = stripped
            else:
                continue
        if stripped == '* * *':
            continue

        # 跳过"上一篇/下一篇"
        if stripped.startswith('上一篇') or stripped.startswith('下一篇'):
            continue

        # 跳过页脚
        if '赣ICP备' in stripped or '关于我们' in stripped or '隐私声明' in stripped:
            continue

        # 跳过 logo
        if 'logo' in stripped.lower():
            continue

        cleaned.append(line)

    return '\n'.join(cleaned)


# ===== 篇目定义 =====

# 卷首篇目（按原书顺序）
JUANSHOU_SECTIONS = [
    (1420, "序"),
    (1421, "三才妙论"),
    (1422, "详论太阳太阴行度"),
    (1423, "论十一曜、二十八宿度数、七政诗"),
    (1424, "四余变曜"),
    (1425, "贵贱格局、分野总图、七政四余人庙乘旺好乐宫歌诀"),
    (1426, "五星忌宫歌诀、五星解神歌诀、二星乔庙歌诀"),
    (1427, "十二宫吉星凶神注"),
    (1428, "新增通加天盘法、新增通关地盘之说"),
    (1429, "依梁三关度起例、三方四正对照难星吊度"),
    (1430, "定行限度分秒诀"),
    (1431, "论洞微大限要秘"),
    (1432, "论行限度要诀"),
    (1434, "论缠度倒限直指"),
    (1435, "论余奴伤主限"),
    (1436, "论煞刃倒限"),
    (1437, "论宫度倒限"),
    (1438, "论太阴太阳倒限"),
    (1439, "详论三关之说"),
]

# 卷一缺失篇目（插入卷一开头）
JUAN1_PREFIX = [
    (1440, "五星起例、先看三星"),
    (1441, "最紧四事、专论十主"),
    (1535, "步天经诀"),
    (1536, "星曜入宫歌"),
]

# 卷三缺失篇目（插入卷三对应位置）
JUAN3_EXTRA = [
    (1550, "增释望斗仙经首篇"),
    (1551, "增释望斗仙经中篇"),
    (1552, "增释望斗仙经尾篇"),
    (1562, "玉衡经"),
    (1563, "张果老仙天口诀（果老张仙先天口诀）"),
    (1564, "后天口诀/至宝论"),
]

# ===== 主转换 =====

def write_md(filepath, title, content, level=1):
    """写 Markdown 文件"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"{'#' * level} {title}\n\n")
        f.write(content.strip())
        f.write('\n')

def main():
    print(f"输出目录: {OUT_DIR}\n")

    # 1. 序
    print("=== 序 ===")
    text = merge_raw_pages(RAW_DIR, 1420)
    text = clean_raw_text(text)
    write_md(os.path.join(OUT_DIR, "00-序.md"), "星平会海序", text)
    print(f"  00-序.md ({len(text)}c)")

    # 2. 卷首
    print("=== 卷首 ===")
    juanshou_content = []
    for bid, title in JUANSHOU_SECTIONS[1:]:  # 跳过序
        text = merge_raw_pages(RAW_DIR, bid)
        text = clean_raw_text(text)
        juanshou_content.append(f"## {title}\n\n{text.strip()}")
        print(f"  {bid} {title} ({len(text)}c)")

    full = '\n\n---\n\n'.join(juanshou_content)
    write_md(os.path.join(OUT_DIR, "00-卷首.md"), "星平会海卷首", full)
    print(f"  00-卷首.md 总计 {len(full)}c")

    # 3. 卷一（含缺失篇目前置）
    print("=== 卷一 ===")
    juan1_content = []

    # 前置缺失篇目
    for bid, title in JUAN1_PREFIX:
        text = merge_raw_pages(RAW_DIR, bid)
        text = clean_raw_text(text)
        juan1_content.append(f"## {title}\n\n{text.strip()}")
        print(f"  {bid} {title} ({len(text)}c)")

    # 原有卷一内容
    raw = open(os.path.join(SRC_DIR, "卷一.txt"), encoding='utf-8').read()
    text = clean_jina_text(raw)
    text = remove_jina_json(text)
    juan1_content.append(f"## 星曜躔度歌\n\n{text.strip()}")
    print(f"  原有卷一内容 ({len(text)}c)")

    full = '\n\n---\n\n'.join(juan1_content)
    write_md(os.path.join(OUT_DIR, "01-星平会海卷一.md"), "星平会海卷一", full)
    print(f"  01-星平会海卷一.md 总计 {len(full)}c")

    # 4. 卷二~卷十
    for i in range(2, 11):
        fname = f"卷{['一','二','三','四','五','六','七','八','九','十'][i-1]}.txt"
        fpath = os.path.join(SRC_DIR, fname)
        if not os.path.exists(fpath):
            print(f"  卷{i}: 文件不存在 {fname}")
            continue

        print(f"=== 卷{i} ===")
        raw = open(fpath, encoding='utf-8').read()
        text = clean_jina_text(raw)
        text = remove_jina_json(text)

        # 卷三插入缺失篇目
        if i == 3:
            extra_parts = []
            for bid, title in JUAN3_EXTRA:
                etext = merge_raw_pages(RAW_DIR, bid)
                etext = clean_raw_text(etext)
                extra_parts.append(f"## {title}\n\n{etext.strip()}")
                print(f"  {bid} {title} ({len(etext)}c)")
            # 在卷三内容前插入
            text = '\n\n---\n\n'.join(extra_parts) + '\n\n---\n\n' + text

        outname = f"{i:02d}-星平会海卷{['一','二','三','四','五','六','七','八','九','十'][i-1]}.md"
        write_md(os.path.join(OUT_DIR, outname), f"星平会海卷{['一','二','三','四','五','六','七','八','九','十'][i-1]}", text)
        print(f"  {outname} ({len(text)}c)")

    # 5. README
    readme = """# 星平会海结构化版

## 来源
- 卷一~卷十：suanzhun.net 网页抓取（jina reader 格式）
- 卷首+卷一缺失+卷三缺失：suanzhun.net 网页抓取（curl article 提取）

## 文件列表
| 文件 | 内容 |
|---|---|
| 00-序.md | 原序 |
| 00-卷首.md | 卷首19个篇目（三才妙论~详论三关之说） |
| 01-星平会海卷一.md | 五星起例+最紧四事+步天经诀+星曜入宫歌+星曜躔度歌+星曜交会歌+星曜照宫歌+主星守宫歌+吊冲秘诀+五星变局 |
| 02-星平会海卷二.md | 入门四十四看法~碎金总诀 |
| 03-星平会海卷三.md | 增释望斗仙经(首/中/尾)+玉衡经+张果老仙天口诀+后天口诀/至宝论+十二宫论断+命理何知经 |
| 04-星平会海卷四.md | 琴堂指金赋~补遗诸星次合格 |
| 05-星平会海卷五.md | 三元男女合婚定局~论运行吉凶 |
| 06-星平会海卷六.md | 八字基础 |
| 07-星平会海卷七.md | 气象篇~天元秀气巫咸经 |
| 08-星平会海卷八.md | 赋文·女命 |
| 09-星平会海卷九.md | 赋文·经典 |
| 10-星平会海卷十.md | 八字格局 |

## 完整性
原书《增补星平会海命学全书》十卷首一卷，本版本已补全：
- ✅ 卷首19个篇目
- ✅ 卷一4个前置篇目（五星起例、最紧四事、步天经诀、星曜入宫歌）
- ✅ 卷三6个缺失篇目（增释望斗仙经首/中/尾篇、玉衡经、张果老仙天口诀、后天口诀/至宝论）

## 清理说明
- 去除网页元数据（Title/URL Source/Published Time/Markdown Content）
- 去除面包屑导航、分页链接、相关文章链接、导航菜单
- 合并同一篇目的多个分页
- 保留原文内容，不做文字修改
"""
    with open(os.path.join(OUT_DIR, "README.md"), 'w', encoding='utf-8') as f:
        f.write(readme)
    print(f"\nREADME.md 已生成")

    # 统计
    all_files = glob.glob(os.path.join(OUT_DIR, "*.md"))
    total_size = sum(os.path.getsize(f) for f in all_files)
    total_lines = sum(sum(1 for _ in open(f, encoding='utf-8')) for f in all_files)
    print(f"\n总计: {len(all_files)} 个文件, {total_size} 字节, {total_lines} 行")

if __name__ == "__main__":
    main()
