#!/usr/bin/env python3
"""
《星平会海》Y=F(X) 模式提取器 v2
改进：处理单行文本，更灵活的模式匹配
"""

import re
import json
from pathlib import Path


def extract_zhaogong_v2(text: str) -> list:
    """从星曜照宫歌提取规则 - v2"""
    rules = []
    
    # 找到星曜照宫歌部分
    start = text.find("星曜照宫歌 命宫星曜")
    if start == -1:
        start = text.find("星曜照宫歌")
    end = text.find("上一篇：", start)
    if end == -1:
        end = len(text)
    
    section = text[start:end]
    
    # 宫位标记
    palace_markers = [
        ("命宫星曜", "命宫"), ("二宫星曜", "财帛宫"), ("三宫星曜", "兄弟宫"),
        ("四宫星曜", "田宅宫"), ("五宫星曜", "男女宫"), ("六宫星曜", "奴仆宫"),
        ("七宫星曜", "妻妾宫"), ("八宫星曜", "疾厄宫"), ("九宫星曜", "迁移宫"),
        ("十宫", "官禄宫"), ("十一宫星曜", "福德宫"), ("十二宫星曜", "相貌宫"),
    ]
    
    # 星曜名称
    star_short = ["木", "火", "土", "金", "水", "日", "月", "气", "孛", "罗", "计"]
    star_full = ["木星", "火星", "土星", "金星", "水星", "太阳", "太阴", "紫炁", "月孛", "罗睺", "计都"]
    
    # 按宫位分割
    current_palace = "命宫"
    palace_start = 0
    
    for marker, palace_name in palace_markers:
        pos = section.find(marker)
        if pos != -1:
            palace_start = pos + len(marker)
    
    # 对每个宫位段落提取规则
    for i, (marker, palace_name) in enumerate(palace_markers):
        # 找到当前宫位的开始和结束
        start_pos = section.find(marker)
        if start_pos == -1:
            continue
        
        # 找下一个宫位的开始
        end_pos = len(section)
        for next_marker, _ in palace_markers[i+1:]:
            next_pos = section.find(next_marker, start_pos + len(marker))
            if next_pos != -1:
                end_pos = next_pos
                break
        
        palace_text = section[start_pos:end_pos]
        
        # 对每个星曜提取规则
        for star_s, star_f in zip(star_short, star_full):
            # 匹配模式：X + (各种动词) + 结果
            patterns = [
                f'{star_s}\\s*照.*?[，,]\\s*(.+?)(?=[。]|$)',
                f'{star_s}\\s*临.*?[，,]\\s*(.+?)(?=[。]|$)',
                f'{star_s}\\s*入.*?[，,]\\s*(.+?)(?=[。]|$)',
                f'{star_s}\\s*守.*?[，,]\\s*(.+?)(?=[。]|$)',
                f'{star_s}\\s*居.*?[，,]\\s*(.+?)(?=[。]|$)',
                f'{star_f}\\s*(?:照|临|入|守|居).*?[，,]\\s*(.+?)(?=[。]|$)',
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, palace_text)
                for m in matches:
                    desc = m.strip()
                    if len(desc) > 3 and not desc.startswith("主人"):
                        rules.append({
                            "id": f"ZG-{palace_name[:2]}-{star_s}",
                            "source": "星平会海/卷一/星曜照宫歌",
                            "x": {
                                "a": star_f,
                                "b": palace_name,
                                "rel": "照临入守居"
                            },
                            "y": desc,
                            "src": "high"
                        })
                        break  # 每个星曜每个宫位只取第一条
    
    return rules


def extract_chandu_v2(text: str) -> list:
    """从星曜躔度歌提取规则 - v2"""
    rules = []
    
    # 星曜名称
    star_short = ["木", "火", "土", "金", "水", "日", "月", "气", "孛", "罗", "计"]
    star_full = ["木星", "火星", "土星", "金星", "水星", "太阳", "太阴", "紫炁", "月孛", "罗睺", "计都"]
    
    # 宿度名称
    mansions = ["角", "亢", "氐", "房", "心", "尾", "箕", "斗", "牛", "女", "虚", "危", "室", "壁",
                "奎", "娄", "胃", "昴", "毕", "觜", "参", "井", "鬼", "柳", "星", "张", "翼", "轸"]
    
    # 匹配模式：X缠Y宿号/名 + 名称 + ， + 描述
    pattern = r'([木火土金水日月气孛罗计]{1,2})\s*缠\s*([\u4e00-\u9fff]{1,2})\s*宿?\s*(?:号|名)\s*([\u4e00-\u9fff]{2,4})\s*[，,]\s*(.+?)(?=[。]|$)'
    
    matches = re.findall(pattern, text)
    for star_s, mansion, title, desc in matches:
        star_f = star_full[star_short.index(star_s)] if star_s in star_short else star_s
        rules.append({
            "id": f"CD-{mansion}-{star_s}",
            "source": "星平会海/卷一/星曜躔度歌",
            "x": {
                "a": star_f,
                "b": f"{mansion}宿",
                "rel": "躔"
            },
            "y": f"号{title}。{desc.strip()}",
            "src": "high"
        })
    
    return rules


def extract_jiaohui_v2(text: str) -> list:
    """从星曜交会歌提取规则 - v2"""
    rules = []
    
    # 星曜名称
    star_short = ["木", "火", "土", "金", "水", "日", "月", "气", "孛", "罗", "计"]
    star_full = ["木星", "火星", "土星", "金星", "水星", "太阳", "太阴", "紫炁", "月孛", "罗睺", "计都"]
    
    # 找到星曜交会歌部分
    start = text.find("星曜郊会歌")
    if start == -1:
        start = text.find("星曜交会歌")
    end = text.find("上一篇：", start)
    if end == -1:
        end = len(text)
    
    section = text[start:end]
    
    # 匹配模式：X星 + 会/同/逢/遇 + Y星 + 结果
    pattern = r'([木火土金水日月气孛罗计]{1,2})\s*(?:星)?\s*(?:会|同|逢|遇|与|和)\s*([\u4e00-\u9fff]{1,2})\s*(?:星)?\s*[，,]\s*(.+?)(?=[。]|$)'
    
    matches = re.findall(pattern, section)
    for star1, star2, desc in matches:
        star1_f = star_full[star_short.index(star1)] if star1 in star_short else star1
        star2_f = star_full[star_short.index(star2)] if star2 in star_short else star2
        rules.append({
            "id": f"JH-{star1}-{star2}",
            "source": "星平会海/卷一/星曜交会歌",
            "x": {
                "a": star1_f,
                "b": star2_f,
                "rel": "交会"
            },
            "y": desc.strip(),
            "src": "high"
        })
    
    return rules


def main():
    """主函数"""
    base_dir = Path("dev-docs/原典/星平会海")
    
    # 读取卷一
    with open(base_dir / "卷一.txt", "r", encoding="utf-8") as f:
        vol1_text = f.read()
    
    # 提取各部分的模式
    all_rules = []
    
    # 1. 星曜照宫歌
    print("=== 提取星曜照宫歌 ===")
    zhaogong_rules = extract_zhaogong_v2(vol1_text)
    print(f"  提取到 {len(zhaogong_rules)} 条规则")
    all_rules.extend(zhaogong_rules)
    
    # 2. 星曜躔度歌
    print("=== 提取星曜躔度歌 ===")
    chandu_rules = extract_chandu_v2(vol1_text)
    print(f"  提取到 {len(chandu_rules)} 条规则")
    all_rules.extend(chandu_rules)
    
    # 3. 星曜交会歌
    print("=== 提取星曜交会歌 ===")
    jiaohui_rules = extract_jiaohui_v2(vol1_text)
    print(f"  提取到 {len(jiaohui_rules)} 条规则")
    all_rules.extend(jiaohui_rules)
    
    # 保存到JSONL
    output_file = base_dir / "patterns.jsonl"
    with open(output_file, "w", encoding="utf-8") as f:
        for rule in all_rules:
            f.write(json.dumps(rule, ensure_ascii=False) + "\n")
    
    print(f"\n=== 总计提取 {len(all_rules)} 条规则 ===")
    print(f"已保存到: {output_file}")
    
    # 统计
    print("\n=== 规则分布 ===")
    source_counts = {}
    for rule in all_rules:
        source = rule["source"].split("/")[-1]
        source_counts[source] = source_counts.get(source, 0) + 1
    for source, count in sorted(source_counts.items()):
        print(f"  {source}: {count} 条")
    
    # 显示前10条规则示例
    print("\n=== 前10条规则示例 ===")
    for rule in all_rules[:10]:
        print(f"[{rule['id']}] {rule['x']['a']} {rule['x']['rel']} {rule['x']['b']} → {rule['y'][:50]}...")


if __name__ == "__main__":
    main()
