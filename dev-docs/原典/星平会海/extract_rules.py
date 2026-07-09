#!/usr/bin/env python3
"""从躔度歌原文提取308条规则并更新schema.json - 含变体句式"""
import re, json, os

BASE = os.path.dirname(os.path.abspath(__file__))

MANSIONS = ["角","亢","氐","房","心","尾","箕","斗","牛","女","虚","危","室","壁",
            "奎","娄","胃","昴","毕","觜","参","井","鬼","柳","星","张","翼","轸"]

STAR_ALIAS = {"金星": "金", "李": "孛"}

def parse_chandu_ge(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    mansions_data = {}
    interpretations = {}
    
    sections = re.split(r'===\s*(\S)度星曜\s*===', content)
    
    i = 1
    while i < len(sections) - 1:
        mansion = sections[i]
        body = sections[i + 1]
        
        rules = []
        for line in body.split('\n'):
            line = line.strip()
            if not line or line.startswith('释云') or line.startswith('==='):
                continue
            
            # 模式1: X缠Y宿号Z[，,。]...
            m = re.match(r'([木火土金水日月气孛罗计金星李]+?)缠(\S+?)(?:宿|度)?(?:号|名)(\S+?)[，,。](.+)', line)
            if m:
                raw_star = m.group(1)
                star = STAR_ALIAS.get(raw_star, raw_star)
                name = m.group(3)
                text = m.group(4).strip()
                rule_id = f"卷一/星曜躔度歌/{mansion}/{star}-{name}"
                rules.append({"id": rule_id, "star": star, "name": name, "text": text})
                continue
            
            # 模式2: X缠Y宿[号]Z[，,。]... (无号/名，直接跟描述)
            # 如 "木缠虚宿不曾安" "土缠危宿庙堂窠" "日缠壁宿水金连"
            m = re.match(r'([木火土金水日月气孛罗计金星李]+?)缠(\S+?)(?:宿|度)([^，,。]+)[，,。](.+)', line)
            if m:
                raw_star = m.group(1)
                star = STAR_ALIAS.get(raw_star, raw_star)
                desc = m.group(3).strip()
                text = m.group(4).strip()
                # 用描述前2字作为名称
                name = desc[:2] if len(desc) >= 2 else desc
                rule_id = f"卷一/星曜躔度歌/{mansion}/{star}-{name}"
                rules.append({"id": rule_id, "star": star, "name": name, "text": f"{desc}，{text}"})
                continue
        
        # 提取释云
        interp_match = re.search(r'释云[：:](.+?)(?=\n===|\n卷|$)', body, re.DOTALL)
        interpretation = ""
        if interp_match:
            interpretation = interp_match.group(1).strip().replace('\n', ' ')
            interpretation = re.sub(r'\s+', '', interpretation)
        
        mansions_data[mansion] = rules
        interpretations[mansion] = interpretation
        i += 2
    
    return mansions_data, interpretations

def update_schema(mansions_data, interpretations):
    schema_path = os.path.join(BASE, 'schema.json')
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    
    for vol in schema['volumes']:
        if vol['id'] == '卷一':
            for section in vol['sections']:
                if section['id'] == '卷一/星曜躔度歌':
                    for sub in section['subsections']:
                        sub_id = sub['id']
                        mansion = sub_id.split('/')[-1]
                        
                        if mansion in mansions_data:
                            rules = mansions_data[mansion]
                            interp = interpretations.get(mansion, '')
                            sub['rules'] = rules
                            if interp:
                                sub['interpretation'] = interp
                            print(f"  ✅ {mansion}: {len(rules)} 条规则")
                        else:
                            print(f"  ⚠️ {mansion}: 未找到数据")
                    break
    
    total = sum(len(sub.get('rules', [])) 
                for vol in schema['volumes'] if vol['id'] == '卷一'
                for section in vol['sections'] if section['id'] == '卷一/星曜躔度歌'
                for sub in section['subsections'])
    
    print(f"\n总计: {total} 条规则")
    
    with open(schema_path, 'w', encoding='utf-8') as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)
    
    print(f"已更新 schema.json")

if __name__ == '__main__':
    filepath = os.path.join(BASE, '卷一-躔度歌完整原文.txt')
    print("=== 解析躔度歌 ===")
    mansions_data, interpretations = parse_chandu_ge(filepath)
    
    for mansion in MANSIONS:
        rules = mansions_data.get(mansion, [])
        interp = interpretations.get(mansion, '')[:50] if interpretations.get(mansion) else ''
        print(f"  {mansion}: {len(rules)} 条 | {interp}...")
    
    print(f"\n=== 更新schema.json ===")
    update_schema(mansions_data, interpretations)
