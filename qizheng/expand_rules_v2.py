"""
第二批规则扩充：覆盖剩余31种未覆盖星格。
8种喜格 + 23种忌格。

可用神煞变量：
- ?阳刃, ?飞刃, ?的杀, ?劫杀, ?天雄, ?血刃, @血刃
- @长生, @岁驾, @岁殿, @帝旺, @斗杓, @天贵, @玉贵, @禄勋, @卦气
- @命宫, @夫妻, @官禄, @福德, @田宅, @财帛, @男女, @奴仆, @疾厄, @迁移, @相貌, @兄弟
- ?昼, ?夜, ?春, ?夏, ?秋, ?冬
"""

# 第二批忌格（sign="-"）
NEW_BAD_RULES_V2 = [
    # === 刃类（需要神煞变量）===
    {"id": 260, "sign": "-", "name": "命坐刃乡", "priority": "2.0.1",
     "condition": "@命=@血刃 | @命[0]=@血刃[0]",
     "excludes": [], "comment": "命宫坐血刃地"},
    {"id": 261, "sign": "-", "name": "刃逢的劫", "priority": "2.0.1",
     "condition": "?阳刃 & ?的杀 & ?劫杀",
     "excludes": [], "comment": "刃逢的杀劫杀"},
    {"id": 262, "sign": "-", "name": "刃雄守命", "priority": "2.0.1",
     "condition": "?阳刃 & ?天雄 & @命[0]=@血刃[0]",
     "excludes": [], "comment": "刃雄守命宫"},
    {"id": 263, "sign": "-", "name": "日月拱刃", "priority": "2.0.1",
     "condition": "(@日=@血刃+4 & @月=@血刃-4) | (@日=@血刃-4 & @月=@血刃+4)",
     "excludes": [], "comment": "日月拱血刃"},
    {"id": 264, "sign": "-", "name": "的刃妻位", "priority": "2.0.1",
     "condition": "@{夫妻}[0]=@血刃[0]",
     "excludes": [], "comment": "的刃在妻宫"},
    {"id": 265, "sign": "-", "name": "计刃儿位", "priority": "2.0.1",
     "condition": "@计[0]=@{男女}[0] & @{男女}[0]=@血刃[0]",
     "excludes": [], "comment": "计都+刃在男女宫"},

    # === 日月无光/失位类 ===
    {"id": 270, "sign": "-", "name": "日月无光", "priority": "2.0.1",
     "condition": "?昼 & (@月[0]=午 | @月[0]=巳) | ?夜 & (@日[0]=子 | @日[0]=亥)",
     "excludes": [], "comment": "昼月近日/夜日入地，日月无光"},
    {"id": 271, "sign": "-", "name": "阴阳背行", "priority": "2.0.1",
     "condition": "?{日东} & ?{月西} & !?{日月会}",
     "excludes": [], "comment": "阴阳东西背行"},
    {"id": 272, "sign": "-", "name": "日居奴位", "priority": "2.0.1",
     "condition": "@日[0]=@{奴仆}[0]",
     "excludes": [], "comment": "太阳居奴仆宫"},
    {"id": 273, "sign": "-", "name": "日陷奴宫", "priority": "2.0.1",
     "condition": "@日[0]=@{奴仆}[0] & !?{日垣}",
     "excludes": [], "comment": "太阳陷在奴仆宫"},
    {"id": 274, "sign": "-", "name": "孤日临奴", "priority": "2.0.1",
     "condition": "@日[0]=@{奴仆}[0] & !?{日月会} & !?{日金会} & !?{日木会} & !?{日水会} & !?{日火会} & !?{日土会}",
     "excludes": [], "comment": "孤日临奴仆宫"},
    {"id": 275, "sign": "-", "name": "孤阳无辅", "priority": "2.0.1",
     "condition": "!?{日月会} & !?{日金会} & !?{日木会} & !?{日水会} & !?{日火会} & !?{日土会} & !?{日计会} & !?{日罗会} & !?{日炁会} & !?{日孛会}",
     "excludes": [], "comment": "孤阳无星辅"},

    # === 孛星/躔度类 ===
    {"id": 280, "sign": "-", "name": "孛星守命", "priority": "2.0.1",
     "condition": "@孛[0]=@命[0]",
     "excludes": [], "comment": "月孛守命宫"},
    {"id": 281, "sign": "-", "name": "月躔土度", "priority": "2.0.1",
     "condition": "?{月土会}",
     "excludes": [], "comment": "月躔土星之度（土月同宫）"},

    # === 失宫/失位类 ===
    {"id": 285, "sign": "-", "name": "木入金宫", "priority": "2.0.1",
     "condition": "(@木[0]=辰 | @木[0]=酉) & !?{木垣}",
     "excludes": [], "comment": "木星入金宫（辰酉）克木"},
    {"id": 286, "sign": "-", "name": "水土失宫", "priority": "2.0.1",
     "condition": "?{水土会} & !?{水垣} & !?{土垣}",
     "excludes": [], "comment": "水土同宫且均失垣"},
    {"id": 287, "sign": "-", "name": "水泛白羊", "priority": "2.0.1",
     "condition": "@水[0]=戌 & !?{水垣}",
     "excludes": [], "comment": "水星在戌宫（白羊）失地"},
    {"id": 288, "sign": "-", "name": "火木失位", "priority": "2.0.1",
     "condition": "?{火木会} & !?{火垣} & !?{木垣}",
     "excludes": [], "comment": "火木同宫且均失垣"},
    {"id": 289, "sign": "-", "name": "火金失躔", "priority": "2.0.1",
     "condition": "?{火金会} & !?{火垣} & !?{金垣}",
     "excludes": [], "comment": "火金同宫且均失躔"},
    {"id": 290, "sign": "-", "name": "田财临福", "priority": "2.0.1",
     "condition": "@{@{田宅}[1]}=@{福德} & @{@{财帛}[1]}=@{福德}",
     "excludes": [], "comment": "田财二主临福德（反为忌）"},
    {"id": 291, "sign": "-", "name": "雄罗居官", "priority": "2.0.1",
     "condition": "?天雄 & @罗[0]=@{官禄}[0]",
     "excludes": [], "comment": "天雄+罗睺居官禄宫"},
]

# 第二批喜格（sign="+"）
NEW_GOOD_RULES_V2 = [
    {"id": 450, "sign": "+", "name": "单罗守命", "priority": "2.0.1",
     "condition": "@罗[0]=@命[0] & !?{日月会}",
     "excludes": [], "comment": "罗睺单独守命宫"},
    {"id": 451, "sign": "+", "name": "单罗独计", "priority": "2.0.1",
     "condition": "@罗[0]=@命[0] & @计[0]=@{夫妻}[0]",
     "excludes": [], "comment": "罗守命计守妻"},
    {"id": 452, "sign": "+", "name": "日月得位", "priority": "2.0.1",
     "condition": "(?{日东} & ?{月西}) | (?{日南} & ?{月北}) | (@日[0]=午 & @月[0]=未) | (@日[0]=巳 & @月[0]=申)",
     "excludes": [], "comment": "日月得位"},
    {"id": 453, "sign": "+", "name": "日月得体", "priority": "2.0.1",
     "condition": "?{日垣} & ?{月垣}",
     "excludes": [], "comment": "日月均入垣得体"},
    {"id": 454, "sign": "+", "name": "田财垣殿", "priority": "2.0.1",
     "condition": "?{@{田宅}[1]}_垣 & ?{@{财帛}[1]}_垣",
     "excludes": [], "comment": "田宅财帛二主均入垣"},
    {"id": 455, "sign": "+", "name": "福财得地", "priority": "2.0.1",
     "condition": "?{@{福德}[1]}_垣 | ?{@{财帛}[1]}_垣",
     "excludes": [], "comment": "福德或财帛主得地"},
    {"id": 456, "sign": "+", "name": "群星西北夜生合格", "priority": "2.0.1",
     "condition": "?夜 & ?{日西} & ?{月西} & ?{金西} & ?{木西}",
     "excludes": [], "comment": "群星西北夜生合格"},
    {"id": 457, "sign": "+", "name": "计罗截断", "priority": "2.0.1",
     "condition": "@罗[0]=午 & @计[0]=子 | @罗[0]=子 & @计[0]=午",
     "excludes": [], "comment": "罗计截断（子在午对宫）"},
]

def merge_rules_v2():
    """合并第二批新规则到规则库"""
    import json
    with open("qizheng/rules_library.json", encoding="utf-8") as f:
        existing = json.load(f)

    all_new = NEW_BAD_RULES_V2 + NEW_GOOD_RULES_V2

    existing_ids = set(r["id"] for r in existing)
    for r in all_new:
        assert r["id"] not in existing_ids, f"ID冲突: {r['id']}"

    merged = existing + all_new
    with open("qizheng/rules_library.json", "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    print(f"原有规则: {len(existing)}")
    print(f"新增忌格v2: {len(NEW_BAD_RULES_V2)}")
    print(f"新增喜格v2: {len(NEW_GOOD_RULES_V2)}")
    print(f"合并后总数: {len(merged)}")

if __name__ == "__main__":
    merge_rules_v2()
