#!/usr/bin/env python3
"""
构建《星平会海》完整path树

精确到行号、hash、source_file，用于 PathListGate 审计。
v2.0: 每个 path 节点都有 source_file / start_line / end_line / hash。
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).parent
DOCUMENT_DIR = ROOT / "dev-docs" / "原典" / "星平会海"
SCHEMA_FILE = DOCUMENT_DIR / "schema.json"
OUTPUT_FILE = DOCUMENT_DIR / "full_path_tree.json"


def calculate_sha256(content: str) -> str:
    """计算内容的SHA256哈希"""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def _is_web_metadata(line: str) -> bool:
    """判断是否为 web fetch 元数据行（非正文）"""
    stripped = line.strip()
    if stripped.startswith("Title:"):
        return True
    if stripped.startswith("URL Source:"):
        return True
    if stripped.startswith("Published Time:"):
        return True
    if stripped == "Markdown Content:":
        return True
    if stripped.startswith("[**"):
        return True
    if stripped.startswith("](https://"):
        return True
    if stripped.startswith("»"):
        return True
    if stripped.startswith(">"):
        return True
    if stripped.startswith("Warning:"):
        return True
    if stripped.startswith("Apache Server"):
        return True
    if stripped == "* * *":
        return True
    if stripped == "The requested URL was not found on this server.":
        return True
    # 分页标记碎片（纯数字或符号行）
    if stripped in ["«", "<", "»", ">"]:
        return True
    if stripped.isdigit() and len(stripped) <= 2:
        return True
    if stripped == "/" or stripped.startswith("/ "):
        return True
    # 导航链接
    if stripped.startswith("上一篇") or stripped.startswith("下一篇"):
        return True
    if stripped.startswith("相关文章"):
        return True
    if stripped.startswith("首页") and "典籍" in stripped:
        return True
    if stripped.startswith("日期:") and "发布者" in stripped:
        return True
    return False


def _is_404_block(lines: List[str], start_idx: int) -> bool:
    """判断从 start_idx 开始是否是一个 404 错误块"""
    # 检查前几行是否有 404 标志
    for i in range(start_idx, min(start_idx + 6, len(lines))):
        if "404" in lines[i] and "Not Found" in lines[i]:
            return True
    return False


def _extract_title_from_header(line: str) -> Optional[str]:
    """从 'Title: XXX-卷Y-星平会海-算准网' 提取 XXX"""
    stripped = line.strip()
    if not stripped.startswith("Title:"):
        return None
    rest = stripped[6:].strip()
    # 去掉 "-卷X-星平会海-算准网" 后缀
    for sep in ["-卷", "-星平会海"]:
        idx = rest.find(sep)
        if idx > 0:
            rest = rest[:idx]
            break
    # 如果有 "/" 分隔多个标题，取第一个
    if "/" in rest:
        rest = rest.split("/")[0]
    return rest.strip() if rest else None


def _find_title_line(lines: List[str], title: str, start: int, end: int) -> Optional[int]:
    """在 lines[start-1:end] 范围内查找标题行

    策略优先级：
    1. 精确匹配正文中的独立标题行
    2. 子串匹配（短行）
    3. 忽略空格匹配
    4. 从 Title: 头提取（最后才用，因为 Title 头在正文之前）
    返回 1-based 行号。
    """
    # 策略1：精确匹配
    for i in range(start - 1, min(end, len(lines))):
        if _is_web_metadata(lines[i]):
            continue
        line_text = lines[i].strip()
        if line_text == title:
            return i + 1

    # 策略2：子串匹配（标题在行首或独立出现，短行）
    for i in range(start - 1, min(end, len(lines))):
        if _is_web_metadata(lines[i]):
            continue
        line_text = lines[i].strip()
        if not line_text or len(line_text) > len(title) + 5:
            continue
        if title in line_text:
            return i + 1

    # 策略3：忽略空格匹配（如 "吊 冲 秘 诀" 匹配 "吊冲秘诀"）
    title_no_space = title.replace(" ", "")
    for i in range(start - 1, min(end, len(lines))):
        if _is_web_metadata(lines[i]):
            continue
        line_text = lines[i].strip().replace(" ", "")
        if line_text == title_no_space:
            return i + 1

    # 策略4：从 Title: 头提取（最后才用）
    for i in range(start - 1, min(end, len(lines))):
        stripped = lines[i].strip()
        if stripped.startswith("Title:"):
            header_title = _extract_title_from_header(lines[i])
            if header_title and (header_title == title or title in header_title or header_title in title):
                return i + 1

    return None


def _find_title_line_fuzzy(lines: List[str], title: str, start: int, end: int) -> Optional[int]:
    """模糊查找标题行：先精确，再尝试常见 OCR 变体"""
    result = _find_title_line(lines, title, start, end)
    if result:
        return result

    # OCR 变体替换表
    replacements = [
        ("交", "郊"),
        ("郊", "交"),
        ("缠", "躔"),
        ("躔", "缠"),
        ("曜", "暇"),
        ("暇", "曜"),
        ("曜", "缠"),
        ("缠", "曜"),
        ("曜", "眼"),
        ("眼", "曜"),
        ("僧", "憎"),
        ("憎", "僧"),
        ("宫", "官"),
        ("官", "宫"),
    ]

    variants = set()
    for old, new in replacements:
        if old in title:
            variants.add(title.replace(old, new))

    for v in variants:
        if v == title:
            continue
        result = _find_title_line(lines, v, start, end)
        if result:
            return result
    return None


def _find_rule_line(lines: List[str], rule_text: str, start: int, end: int) -> Optional[int]:
    """在 lines[start-1:end] 范围内查找规则文本所在行

    rule_text 可能跨多行，取前 10 个非空格字符做匹配。
    返回 1-based 行号。
    """
    # 取前10个非空格字符（忽略空格和换行）
    keyword = rule_text.replace(" ", "").replace("\n", "")[:10]
    if not keyword:
        return None

    # 策略1：逐行精确匹配（忽略空格）
    for i in range(start - 1, min(end, len(lines))):
        line_no_space = lines[i].replace(" ", "").replace("\n", "")
        if keyword in line_no_space:
            return i + 1

    # 策略2：跨行匹配（合并多行后搜索）
    # 把 start 到 end 范围内的所有行合并，搜索 keyword
    region_text = "".join(lines[start - 1:min(end, len(lines))])
    region_no_space = region_text.replace(" ", "").replace("\n", "")
    idx = region_no_space.find(keyword)
    if idx >= 0:
        # 找到 keyword 在合并文本中的位置，反推回行号
        # 计算到 keyword 起始位置为止的原始文本长度
        raw_pos = 0
        space_count = 0
        for i, ch in enumerate(region_text):
            if ch in " \n":
                space_count += 1
            else:
                if raw_pos == idx:
                    # 当前位置就是 keyword 起始
                    # 计算行号：从 start 开始，数换行符
                    line_num = start
                    for j in range(i):
                        if region_text[j] == '\n':
                            line_num += 1
                    return line_num
                raw_pos += 1
        # fallback: 返回 start
        return start

    return None


def build_detailed_path_tree(document_dir: Path) -> Dict:
    """构建详细的path树（精确到行号、hash、source_file）"""
    with open(document_dir / "schema.json", "r", encoding="utf-8") as f:
        schema = json.load(f)

    print(f"Schema中有 {len(schema['volumes'])} 个卷")

    volumes_data = {}
    volume_names = ["卷一", "卷二", "卷三", "卷四", "卷五",
                    "卷六", "卷七", "卷八", "卷九", "卷十"]

    for vol_name in volume_names:
        file_path = document_dir / f"{vol_name}.txt"
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            volumes_data[vol_name] = lines
            print(f"  已加载: {file_path.name} ({len(lines)} 行)")
        else:
            print(f"  警告：文件不存在 {file_path}")

    print(f"成功加载 {len(volumes_data)} 个卷")

    path_tree = {
        "document": "星平会海",
        "version": "2.0.0",
        "total_volumes": len(schema["volumes"]),
        "volumes": []
    }

    unresolved = []

    for vol_schema in schema["volumes"]:
        vol_id = vol_schema["id"]

        if vol_id not in volumes_data:
            print(f"警告：找不到 {vol_id} 的数据")
            continue

        print(f"处理 {vol_id}")

        lines = volumes_data[vol_id]
        total_lines = len(lines)
        source_file = f"{vol_id}.txt"

        content = "".join(lines)
        vol_hash = calculate_sha256(content)

        volume = {
            "id": vol_id,
            "title": vol_schema["title"],
            "source_file": source_file,
            "start_line": 1,
            "end_line": total_lines,
            "total_lines": total_lines,
            "volume_hash": vol_hash,
            "sections": []
        }

        sections_schema = vol_schema.get("sections", [])

        if not sections_schema:
            path_tree["volumes"].append(volume)
            continue

        # 定位每个 section 的行号
        section_positions = []

        for sec_idx, section in enumerate(sections_schema):
            section_title = section["title"]
            search_start = section_positions[-1][0] if section_positions else 1
            search_end = total_lines

            found_line = _find_title_line_fuzzy(lines, section_title, search_start, search_end)

            if found_line:
                section_positions.append((found_line, section))
            else:
                unresolved.append({
                    "type": "section",
                    "id": section["id"],
                    "title": section_title,
                    "volume": vol_id,
                    "reason": "title not found in text"
                })
                section_positions.append((search_start, section))

        # 计算 section 的 end_line
        for sec_idx, (start_line, section) in enumerate(section_positions):
            if sec_idx + 1 < len(section_positions):
                end_line = section_positions[sec_idx + 1][0] - 1
            else:
                end_line = total_lines

            if end_line < start_line:
                end_line = start_line

            section_lines = lines[start_line - 1:end_line]
            section_hash = calculate_sha256("".join(section_lines))

            section_data = {
                "id": section["id"],
                "title": section["title"],
                "source_file": source_file,
                "start_line": start_line,
                "end_line": end_line,
                "total_lines": len(section_lines),
                "hash": section_hash,
                "subsections": []
            }

            subsections_schema = section.get("subsections", [])

            if subsections_schema:
                sub_positions = []

                for sub_idx, subsection in enumerate(subsections_schema):
                    sub_title = subsection["title"]
                    sub_search_start = sub_positions[-1][0] if sub_positions else start_line
                    sub_search_end = end_line

                    sub_found = _find_title_line_fuzzy(lines, sub_title, sub_search_start, sub_search_end)

                    if sub_found:
                        sub_positions.append((sub_found, subsection))
                    else:
                        unresolved.append({
                            "type": "subsection",
                            "id": subsection["id"],
                            "title": sub_title,
                            "section": section["id"],
                            "reason": "title not found in section range"
                        })
                        sub_positions.append((sub_search_start, subsection))

                for sub_idx, (sub_start, subsection) in enumerate(sub_positions):
                    if sub_idx + 1 < len(sub_positions):
                        sub_end = sub_positions[sub_idx + 1][0] - 1
                    else:
                        sub_end = end_line

                    if sub_end < sub_start:
                        sub_end = sub_start

                    sub_lines = lines[sub_start - 1:sub_end]
                    sub_hash = calculate_sha256("".join(sub_lines))

                    rules = subsection.get("rules", [])
                    rules_data = []

                    for rule in rules:
                        rule_id = rule["id"]
                        rule_text = rule.get("text", "")
                        rule_start = _find_rule_line(lines, rule_text, sub_start, sub_end)

                        if rule_start:
                            rule_end = rule_start
                            rule_lines = lines[rule_start - 1:rule_end]
                            rule_hash = calculate_sha256("".join(rule_lines))
                        else:
                            unresolved.append({
                                "type": "rule",
                                "id": rule_id,
                                "subsection": subsection["id"],
                                "reason": "rule text not found in subsection range"
                            })
                            rule_start = None
                            rule_end = None
                            rule_hash = None

                        rules_data.append({
                            "id": rule_id,
                            "source_file": source_file,
                            "start_line": rule_start,
                            "end_line": rule_end,
                            "hash": rule_hash,
                            "star": rule.get("star"),
                            "name": rule.get("name"),
                            "text": rule_text
                        })

                    subsection_data = {
                        "id": subsection["id"],
                        "title": subsection["title"],
                        "source_file": source_file,
                        "start_line": sub_start,
                        "end_line": sub_end,
                        "total_lines": len(sub_lines),
                        "hash": sub_hash,
                        "rules_count": len(rules),
                        "rules": rules_data
                    }

                    section_data["subsections"].append(subsection_data)

            volume["sections"].append(section_data)

        path_tree["volumes"].append(volume)

    # 统计
    total_sections = sum(len(v["sections"]) for v in path_tree["volumes"])
    total_subsections = sum(
        len(s["subsections"])
        for v in path_tree["volumes"]
        for s in v["sections"]
    )
    total_rules = sum(
        len(s.get("rules", []))
        for v in path_tree["volumes"]
        for sec in v["sections"]
        for s in sec.get("subsections", [])
    )

    # remainder=0 验证：区分 web 元数据间隙和真实内容间隙
    coverage_gaps = []
    web_metadata_gaps = []
    for vol in path_tree["volumes"]:
        vol_id = vol["id"]
        vol_start = vol["start_line"]
        vol_end = vol["end_line"]
        vol_lines = volumes_data.get(vol_id, [])
        covered = [(sec["start_line"], sec["end_line"]) for sec in vol["sections"]]

        def _classify_gap(gap_start, gap_end, gap_desc):
            """判断间隙是 web 元数据还是真实内容缺失"""
            all_web_meta = True
            has_404 = False
            for li in range(gap_start - 1, min(gap_end, len(vol_lines))):
                line_text = vol_lines[li].strip()
                if not line_text:
                    continue
                if "404" in line_text and "Not Found" in line_text:
                    has_404 = True
                    continue
                if not _is_web_metadata(vol_lines[li]):
                    all_web_meta = False
                    break

            if all_web_meta:
                web_metadata_gaps.append({
                    "volume": vol_id,
                    "gap": f"{gap_start}-{gap_end} ({gap_desc})",
                    "has_404": has_404
                })
            else:
                coverage_gaps.append({
                    "volume": vol_id,
                    "gap": f"{gap_start}-{gap_end} ({gap_desc})"
                })

        if not covered:
            _classify_gap(vol_start, vol_end, "no sections")
        else:
            if covered[0][0] > vol_start:
                _classify_gap(vol_start, covered[0][0] - 1, "before first section")
            for i in range(len(covered) - 1):
                if covered[i][1] + 1 < covered[i+1][0]:
                    _classify_gap(covered[i][1] + 1, covered[i+1][0] - 1, "between sections")
            if covered[-1][1] < vol_end:
                _classify_gap(covered[-1][1] + 1, vol_end, "after last section")

    remainder_is_zero = len(coverage_gaps) == 0

    path_tree["statistics"] = {
        "total_volumes": len(path_tree["volumes"]),
        "total_sections": total_sections,
        "total_subsections": total_subsections,
        "total_rules": total_rules,
        "unresolved_count": len(unresolved),
        "coverage_gaps_count": len(coverage_gaps),
        "web_metadata_gaps_count": len(web_metadata_gaps),
        "remainder_is_zero": remainder_is_zero
    }

    path_tree["unresolved"] = unresolved
    path_tree["coverage_gaps"] = coverage_gaps
    path_tree["web_metadata_gaps"] = web_metadata_gaps

    return path_tree


def main():
    """主函数"""
    print("开始构建《星平会海》完整path树...")

    path_tree = build_detailed_path_tree(DOCUMENT_DIR)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(path_tree, f, ensure_ascii=False, indent=2)

    stats = path_tree["statistics"]
    print(f"\n✅ 已生成完整path树: {OUTPUT_FILE}")
    print(f"\n统计信息:")
    print(f"  卷数: {stats['total_volumes']}")
    print(f"  节数: {stats['total_sections']}")
    print(f"  子节数: {stats['total_subsections']}")
    print(f"  规则数: {stats['total_rules']}")
    print(f"  未定位: {stats['unresolved_count']}")
    print(f"  覆盖间隙: {stats['coverage_gaps_count']}")
    print(f"  web元数据间隙: {stats['web_metadata_gaps_count']}")
    print(f"  remainder=0: {stats['remainder_is_zero']}")

    if stats["unresolved_count"] > 0:
        print(f"\n⚠️ 未定位项 ({stats['unresolved_count']}):")
        for item in path_tree["unresolved"][:10]:
            print(f"  {item['type']}: {item['id']} - {item['reason']}")
        if stats["unresolved_count"] > 10:
            print(f"  ... 还有 {stats['unresolved_count'] - 10} 项")

    if stats["coverage_gaps_count"] > 0:
        print(f"\n⚠️ 真实覆盖间隙 ({stats['coverage_gaps_count']}):")
        for gap in path_tree["coverage_gaps"][:10]:
            print(f"  {gap['volume']}: {gap['gap']}")
        if stats["coverage_gaps_count"] > 10:
            print(f"  ... 还有 {stats['coverage_gaps_count'] - 10} 项")

    if stats["web_metadata_gaps_count"] > 0:
        print(f"\nℹ️ web元数据间隙 ({stats['web_metadata_gaps_count']}):")
        for gap in path_tree["web_metadata_gaps"][:10]:
            print(f"  {gap['volume']}: {gap['gap']}")
        if stats["web_metadata_gaps_count"] > 10:
            print(f"  ... 还有 {stats['web_metadata_gaps_count'] - 10} 项")


if __name__ == "__main__":
    main()
