#!/usr/bin/env python3
"""从星平会海卷一提取交会歌/照宫歌/守宫歌规则 - 处理多行文本"""
import re, json, os

BASE = os.path.dirname(os.path.abspath(__file__))

STARS = ["木", "火", "土", "金", "水", "日", "月", "气", "孛", "罗", "计"]
STAR_ALIAS = {"金星": "金", "李": "孛", "紫气": "气", "月李": "孛",
              "天首": "罗", "天尾": "计", "搀枪": "孛", "辰星": "水",
              "太白": "金", "太阳": "日", "太阴": "月", "荧惑": "火",
              "荣惑": "火", "岁星": "木", "镇星": "土", "字": "孛"}

def normalize_star(raw):
    raw = raw.strip()
    if raw in STAR_ALIAS:
        return STAR_ALIAS[raw]
    if len(raw) == 1 and raw in STARS:
        return raw
    for alias, norm in STAR_ALIAS.items():
        if alias in raw:
            return norm
    return raw

def parse_jiaohui_ge(filepath):
    """解析交会歌：星+星组合"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rules = []
    
    # Split by star sections
    sections = re.split(r'(木星郊会|火星郊会|土星郊会|金星郊会|水星郊会|日星郊会|月星郊会|气星郊会|李星郊会)', content)
    
    i = 1
    while i < len(sections) - 1:
        header = sections[i]
        body = sections[i + 1]
        star1_raw = header.replace('郊会', '').replace('星', '')
        star1 = normalize_star(star1_raw)
        
        # Find all star+star combinations in this section
        # Each line can contain multiple rules separated by 。or multiple verses
        # Split body into individual verse segments
        segments = re.split(r'[。\n]', body)
        
        found_pairs = set()
        for seg in segments:
            seg = seg.strip()
            if not seg:
                continue
            
            # Pattern: X星[会/同/相逢/相照/宜与/最喜遇/不喜会/不要会/专恶会]Y星
            m = re.search(
                rf'(木|火|土|金|水|日|月|气|孛|罗|计|太阳|太阴|紫气|月孛|天首|天尾|搀枪|荧惑|荣惑|太白|辰星|岁星|镇星|字)\S{{0,4}}(?:会|同|相逢|相照|宜与|喜遇|最喜遇|不喜会|不要会|专恶会|不欲相郊|设若逢|最忌与?|与|逢)\S{{0,4}}(木|火|土|金|水|日|月|气|孛|罗|计|紫气|月孛|天首|天尾|搀枪)',
                seg
            )
            if m:
                raw1, raw2 = m.group(1), m.group(2)
                s1 = normalize_star(raw1)
                s2 = normalize_star(raw2)
                if s1 != s2 and (s1, s2) not in found_pairs:
                    rule_id = f"卷一/交会歌/{s1}会{s2}"
                    rules.append({
                        "id": rule_id,
                        "star1": s1,
                        "star2": s2,
                        "text": seg.strip()[:80]
                    })
                    found_pairs.add((s1, s2))
        
        i += 2
    
    return rules

def parse_zhaogong_ge(filepath):
    """解析照宫歌：星+宫组合"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rules = []
    
    # Split by palace sections
    palace_map = {
        '命宫星曜': '命宫', '二宫星曜': '财帛宫', '三宫星曜': '兄弟宫',
        '四宫星曜': '田宅宫', '五宫星曜': '男女宫', '六宫星曜': '奴仆宫',
        '七宫星曜': '妻妾宫', '八宫星曜': '疾厄宫', '九宫星曜': '迁移宫',
        '十宫星曜': '官禄宫', '十一宫星曜': '福德宫', '十二宫星曜': '相貌宫',
    }
    
    sections = re.split(r'(命宫星曜|二宫星曜|三宫星曜|四宫星曜|五宫星曜|六宫星曜|七宫星曜|八宫星曜|九宫星曜|十宫星曜|十一宫星曜|十二宫星曜)', content)
    
    i = 1
    while i < len(sections) - 1:
        header = sections[i]
        body = sections[i + 1]
        palace = palace_map.get(header, header)
        
        # Split body into segments
        segments = re.split(r'[。\n]', body)
        
        found = set()
        for seg in segments:
            seg = seg.strip()
            if not seg:
                continue
            
            # Pattern: X[照/入/临/居/守/在]Y宫
            m = re.search(
                r'(木|火|土|金|水|日|月|气|孛|罗|计|紫气|月孛|太阳|太阴)\S{0,3}(?:照|入|临|居|守|在)(命宫|财帛|兄弟|田宅|男女|奴仆|妻妾|疾厄|迁移|官禄|福德|相貌)',
                seg
            )
            if m:
                raw_star, palace_name = m.group(1), m.group(2)
                star = normalize_star(raw_star)
                if (star, palace_name) not in found:
                    rule_id = f"卷一/照宫歌/{star}照{palace_name}"
                    rules.append({
                        "id": rule_id,
                        "star": star,
                        "palace": palace_name,
                        "text": seg.strip()[:80]
                    })
                    found.add((star, palace_name))
        
        i += 2
    
    return rules

def parse_shougong_ge(filepath):
    """解析守宫歌：宫主入命规则"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rules = []
    
    # Split into segments
    segments = re.split(r'[。\n]', content)
    
    found = set()
    for seg in segments:
        seg = seg.strip()
        if not seg:
            continue
        
        # Pattern: X主，入Y宫 / X主入Y宫 / X主，守Y宫
        m = re.search(r'(\S+主)\S{0,2}(?:入|守)(\S+?宫)', seg)
        if m:
            ruler = m.group(1)
            palace = m.group(2)
            
            if (ruler, palace) not in found:
                rule_id = f"卷一/守宫歌/{ruler}入{palace}"
                rules.append({
                    "id": rule_id,
                    "ruler": ruler,
                    "palace": palace,
                    "text": seg.strip()[:80]
                })
                found.add((ruler, palace))
    
    return rules

PALACES = ["命宫", "财帛宫", "兄弟宫", "田宅宫", "男女宫", "奴仆宫",
           "妻妾宫", "疾厄宫", "迁移宫", "官禄宫", "福德宫", "相貌宫"]

def update_schema(jiaohui_rules, zhaogong_rules, shougong_rules):
    schema_path = os.path.join(BASE, 'schema.json')
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    
    for vol in schema['volumes']:
        if vol['id'] == '卷一':
            for section in vol['sections']:
                if section['id'] == '卷一/交会歌':
                    section['rules'] = jiaohui_rules
                    print(f"  ✅ 交会歌: {len(jiaohui_rules)} 条规则")
                elif section['id'] == '卷一/照宫歌':
                    section['rules'] = zhaogong_rules
                    print(f"  ✅ 照宫歌: {len(zhaogong_rules)} 条规则")
                elif section['id'] == '卷一/守宫歌':
                    section['rules'] = shougong_rules
                    print(f"  ✅ 守宫歌: {len(shougong_rules)} 条规则")
    
    total_chandu = sum(
        len(sub.get('rules', []))
        for vol in schema['volumes'] if vol['id'] == '卷一'
        for section in vol['sections'] if section['id'] == '卷一/星曜躔度歌'
        for sub in section.get('subsections', [])
    )
    total_jiaohui = len(jiaohui_rules)
    total_zhaogong = len(zhaogong_rules)
    total_shougong = len(shougong_rules)
    
    print(f"\n总计: 躔度歌 {total_chandu} + 交会歌 {total_jiaohui} + 照宫歌 {total_zhaogong} + 守宫歌 {total_shougong} = {total_chandu+total_jiaohui+total_zhaogong+total_shougong} 条")
    
    with open(schema_path, 'w', encoding='utf-8') as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)
    
    print(f"已更新 schema.json")

if __name__ == '__main__':
    print("=== 解析交会歌 ===")
    jiaohui_rules = parse_jiaohui_ge(os.path.join(BASE, 'raw/1538.txt'))
    for r in jiaohui_rules:
        print(f"  {r['id']}: {r['text'][:50]}")
    print(f"  共 {len(jiaohui_rules)} 条\n")
    
    print("=== 解析照宫歌 ===")
    zhaogong_rules = parse_zhaogong_ge(os.path.join(BASE, 'raw/1539.txt'))
    for r in zhaogong_rules:
        print(f"  {r['id']}: {r['text'][:50]}")
    print(f"  共 {len(zhaogong_rules)} 条\n")
    
    print("=== 解析守宫歌 ===")
    shougong_rules = parse_shougong_ge(os.path.join(BASE, 'raw/1540.txt'))
    for r in shougong_rules:
        print(f"  {r['id']}: {r['text'][:50]}")
    print(f"  共 {len(shougong_rules)} 条\n")
    
    print("=== 更新schema.json ===")
    update_schema(jiaohui_rules, zhaogong_rules, shougong_rules)
