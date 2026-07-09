#!/usr/bin/env python3
"""
《星平会海》Y=F(X) 模式提取器
从卷一的星曜照宫歌/星曜躔度歌/星曜交会歌中提取规则
"""

import re
import json
from pathlib import Path

# 星曜名称映射（古名→标准名）
STAR_MAP = {
    "木": "木星", "火": "火星", "土": "土星", "金": "金星", "水": "水星",
    "日": "太阳", "太阳": "太阳", "月": "太阴", "太阴": "太阴",
    "气": "紫炁", "紫气": "紫炁", "孛": "月孛", "月孛": "月孛",
    "罗": "罗睺", "罗喉": "罗睺", "计": "计都", "计都": "计都",
    "木星": "木星", "火星": "火星", "土星": "土星", "金星": "金星", "水星": "水星",
    "荧惑": "火星", "太白": "金星", "辰星": "水星",
    "搀枪": "月孛", "天首": "罗睺", "天尾": "计都",
}

# 宫位名称映射
PALACE_MAP = {
    "命": "命宫", "命宫": "命宫",
    "财": "财帛宫", "财帛": "财帛宫", "财帛宫": "财帛宫", "二宫": "财帛宫",
    "兄": "兄弟宫", "兄弟": "兄弟宫", "兄弟宫": "兄弟宫", "三宫": "兄弟宫",
    "田": "田宅宫", "田宅": "田宅宫", "田宅宫": "田宅宫", "四宫": "田宅宫",
    "男": "男女宫", "男女": "男女宫", "男女宫": "男女宫", "五宫": "男女宫", "子宫": "男女宫",
    "奴": "奴仆宫", "奴仆": "奴仆宫", "奴仆宫": "奴仆宫", "六宫": "奴仆宫",
    "妻": "妻妾宫", "妻妾": "妻妾宫", "妻妾宫": "妻妾宫", "七宫": "妻妾宫",
    "疾": "疾厄宫", "疾厄": "疾厄宫", "疾厄宫": "疾厄宫", "八宫": "疾厄宫", "八煞": "疾厄宫",
    "迁": "迁移宫", "迁移": "迁移宫", "迁移宫": "迁移宫", "九宫": "迁移宫",
    "官": "官禄宫", "官禄": "官禄宫", "官禄宫": "官禄宫", "十宫": "官禄宫",
    "福": "福德宫", "福德": "福德宫", "福德宫": "福德宫", "十一宫": "福德宫",
    "相": "相貌宫", "相貌": "相貌宫", "相貌宫": "相貌宫", "十二宫": "相貌宫",
}

# 宿度名称
MANSIONS = [
    "角", "亢", "氐", "房", "心", "尾", "箕",
    "斗", "牛", "女", "虚", "危", "室", "壁",
    "奎", "娄", "胃", "昴", "毕", "觜", "参",
    "井", "鬼", "柳", "星", "张", "翼", "轸",
]


def normalize_star(name: str) -> str:
    """标准化星曜名称"""
    name = name.strip()
    return STAR_MAP.get(name, name)


def normalize_palace(name: str) -> str:
    """标准化宫位名称"""
    name = name.strip()
    return PALACE_MAP.get(name, name)


def extract_from_zhaogong(text: str) -> list:
    """从星曜照宫歌提取规则"""
    rules = []
    
    # 匹配模式：星名 + (照/临/入/守/居) + 宫位名 + ，/。 + 结果描述
    # 例如："木照人聪敏" 或 "火星入命最为宜"
    patterns = [
        # 模式1：X照/临/入/守/居 + 宫位 + 结果
        r'([木火土金水日月气孛罗计]{1,2})\s*(?:照|临|入|守|居)\s*(?:人)?命\s*[，,]\s*(.+?)(?=[。]|$)',
        # 模式2：X星 + 入命/在命/居命 + 结果
        r'([木火土金水日月气孛罗计]{1,2})\s*(?:星)?\s*(?:入|在|居)\s*命\s*[，,]\s*(.+?)(?=[。]|$)',
        # 模式3：X + 照 + 宫位
        r'([木火土金水日月气孛罗计]{1,2})\s*照\s*(\S{1,4}?)\s*[中宫]',
        # 模式4：X + 临 + 宫位
        r'([木火土金水日月气孛罗计]{1,2})\s*临\s*(\S{1,4}?)\s*[中宫]',
        # 模式5：X + 居 + 宫位
        r'([木火土金水日月气孛罗计]{1,2})\s*居\s*(\S{1,4}?)\s*[中宫]',
    ]
    
    return rules


def extract_zhaogong_patterns(text: str) -> list:
    """从星曜照宫歌提取模式 - 使用更灵活的方法"""
    rules = []
    
    # 按宫位分段
    palace_sections = {
        "命宫": r'命宫星曜(.*?)二宫星曜',
        "财帛宫": r'二宫星曜(.*?)三宫星曜',
        "兄弟宫": r'三宫星曜(.*?)四宫星曜',
        "田宅宫": r'四宫星曜(.*?)五宫星曜',
        "男女宫": r'五宫星曜(.*?)六宫星曜',
        "奴仆宫": r'六宫星曜(.*?)七宫星曜',
        "妻妾宫": r'七宫星曜(.*?)八宫星曜',
        "疾厄宫": r'八宫星曜(.*?)九宫星曜',
        "迁移宫": r'九宫星曜(.*?)十宫',
        "官禄宫": r'十宫(?:墨|星)曜(.*?)十一宫',
        "福德宫": r'十一宫星曜(.*?)十二宫',
        "相貌宫": r'十二宫星曜(.*?)(?=$)',
    }
    
    # 星曜名称列表
    star_names = ["木", "火", "土", "金", "水", "日", "月", "气", "孛", "罗", "计"]
    star_full = ["木星", "火星", "土星", "金星", "水星", "太阳", "太阴", "紫炁", "月孛", "罗睺", "计都"]
    
    for palace_name, pattern in palace_sections.items():
        match = re.search(pattern, text, re.DOTALL)
        if not match:
            continue
        
        section = match.group(1)
        
        # 提取该宫位下每个星曜的描述
        for star_short, star_full_name in zip(star_names, star_full):
            # 匹配模式：X + (各种动词) + 结果
            star_patterns = [
                f'{star_short}\\s*(?:照|临|入|守|居|到|在|会|见|遇)\\s*.*?[，,]\\s*(.+?)(?=[。]|$)',
                f'{star_full_name}\\s*(?:照|临|入|守|居|到|在|会|见|遇)\\s*.*?[，,]\\s*(.+?)(?=[。]|$)',
            ]
            
            for sp in star_patterns:
                matches = re.findall(sp, section)
                for m in matches:
                    desc = m.strip()
                    if len(desc) > 5:  # 过滤太短的描述
                        rules.append({
                            "id": f"ZG-{palace_name[:2]}-{star_short}",
                            "source": "星平会海/卷一/星曜照宫歌",
                            "x_condition": {
                                "element_a": star_full_name,
                                "element_b": palace_name,
                                "relationship": "照临"
                            },
                            "y_outcome": desc,
                            "confidence": "medium",
                            "notes": ""
                        })
    
    return rules


def extract_chandu_patterns(text: str) -> list:
    """从星曜躔度歌提取模式"""
    rules = []
    
    # 星曜名称
    star_names = ["木", "火", "土", "金", "水", "日", "月", "气", "孛", "罗", "计"]
    star_full = ["木星", "火星", "土星", "金星", "水星", "太阳", "太阴", "紫炁", "月孛", "罗睺", "计都"]
    
    # 宿度名称
    mansions = ["角", "亢", "氐", "房", "心", "尾", "箕", "斗", "牛", "女", "虚", "危", "室", "壁",
                "奎", "娄", "胃", "昴", "毕", "觜", "参", "井", "鬼", "柳", "星", "张", "翼", "轸"]
    
    # 匹配模式：X缠Y宿号/名/为 + 名称 + ， + 描述
    pattern = r'([木火土金水日月气孛罗计]{1,2})\s*缠\s*([\u4e00-\u9fff]{1,2})\s*宿?\s*(?:号|名|为)\s*([\u4e00-\u9fff]{2,4})\s*[，,]\s*(.+?)(?=[。]|$)'
    
    matches = re.findall(pattern, text)
    for star_short, mansion, title, desc in matches:
        star_full_name = star_full[star_names.index(star_short)] if star_short in star_names else star_short
        rules.append({
            "id": f"CD-{mansion}-{star_short}",
            "source": "星平会海/卷一/星曜躔度歌",
            "x_condition": {
                "element_a": star_full_name,
                "element_b": f"{mansion}宿",
                "relationship": "躔"
            },
            "y_outcome": f"{title}。{desc.strip()}",
            "confidence": "high",
            "notes": f"号{title}"
        })
    
    return rules


def extract_jiaohui_patterns(text: str) -> list:
    """从星曜交会歌提取模式"""
    rules = []
    
    # 星曜名称
    star_names = ["木", "火", "土", "金", "水", "日", "月", "气", "孛", "罗", "计"]
    star_full = ["木星", "火星", "土星", "金星", "水星", "太阳", "太阴", "紫炁", "月孛", "罗睺", "计都"]
    
    # 匹配模式：X星 + 会/同/逢/遇 + Y星 + 结果
    pattern = r'([木火土金水日月气孛罗计]{1,2})\s*(?:星)?\s*(?:会|同|逢|遇|与|和)\s*([\u4e00-\u9fff]{1,2})\s*(?:星)?\s*[，,]\s*(.+?)(?=[。]|$)'
    
    matches = re.findall(pattern, text)
    for star1, star2, desc in matches:
        star1_full = star_full[star_names.index(star1)] if star1 in star_names else star1
        star2_full = star_full[star_names.index(star2)] if star2 in star_names else star2
        rules.append({
            "id": f"JH-{star1}-{star2}",
            "source": "星平会海/卷一/星曜交会歌",
            "x_condition": {
                "element_a": star1_full,
                "element_b": star2_full,
                "relationship": "交会"
            },
            "y_outcome": desc.strip(),
            "confidence": "high",
            "notes": ""
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
    zhaogong_rules = extract_zhaogong_patterns(vol1_text)
    print(f"  提取到 {len(zhaogong_rules)} 条规则")
    all_rules.extend(zhaogong_rules)
    
    # 2. 星曜躔度歌
    print("=== 提取星曜躔度歌 ===")
    chandu_rules = extract_chandu_patterns(vol1_text)
    print(f"  提取到 {len(chandu_rules)} 条规则")
    all_rules.extend(chandu_rules)
    
    # 3. 星曜交会歌
    print("=== 提取星曜交会歌 ===")
    jiaohui_rules = extract_jiaohui_patterns(vol1_text)
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


if __name__ == "__main__":
    main()
