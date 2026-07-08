"""
郑氏星案40例 - 结构化数据
从《张果星宗》卷十八郑氏星案提取（tianyugong.com）
用于Phase 24端到端验证。

每例含：四柱(年月日时干支) + 性别 + 命格等级 + 星格
"""

# 从原始文本提取的40例数据
ZHENG_40_CASES = [
    {"id": 1, "grade": "三品命", "gz": "庚寅 己卯 庚子 丙戌", "gender": "男"},
    {"id": 2, "grade": "三品命", "gz": "丙子 庚寅 癸丑 壬子", "gender": "男"},
    {"id": 3, "grade": "四品命", "gz": "甲子 丁丑 甲戌 庚午", "gender": "男"},
    {"id": 4, "grade": "五品命", "gz": "壬申 庚戌 壬辰 辛丑", "gender": "男"},
    {"id": 5, "grade": "五品命", "gz": "丁卯 己酉 庚辰 丁丑", "gender": "男"},
    {"id": 6, "grade": "黄堂命", "gz": "乙丑 辛巳 甲午 丁卯", "gender": "男"},
    {"id": 7, "grade": "五品命", "gz": "戊寅 丙辰 甲寅 乙亥", "gender": "男"},
    {"id": 8, "grade": "科第命", "gz": "丙辰 庚寅 丁卯 癸卯", "gender": "男"},
    {"id": 9, "grade": "监司命", "gz": "丙戌 辛卯 丙辰 戊戌", "gender": "男"},
    {"id": 10, "grade": "府官命", "gz": "壬辰 癸卯 癸丑 甲寅", "gender": "男"},
    {"id": 11, "grade": "州邑命", "gz": "壬申 癸卯 癸丑 戊午", "gender": "男"},
    {"id": 12, "grade": "邑长命", "gz": "庚申 癸未 丁卯 癸卯", "gender": "男"},
    {"id": 13, "grade": "案牍命", "gz": "己丑 癸酉 壬寅 庚戌", "gender": "男"},
    {"id": 14, "grade": "案牍命", "gz": "己丑 癸酉 壬寅 庚戌", "gender": "男"},
    {"id": 15, "grade": "武职命", "gz": "辛未 甲午 癸酉 壬戌", "gender": "男"},
    {"id": 16, "grade": "官卑命", "gz": "辛巳 庚寅 丙戌 壬辰", "gender": "男"},
    {"id": 17, "grade": "官卑命", "gz": "辛巳 庚寅 丙戌 壬辰", "gender": "男"},
    {"id": 18, "grade": "杂流命", "gz": "戊子 壬戌 乙巳 丙戌", "gender": "男"},
    {"id": 19, "grade": "功名命", "gz": "辛未 乙未 甲寅 乙丑", "gender": "男"},
    {"id": 20, "grade": "利名图成命", "gz": "癸卯 庚申 己巳 辛未", "gender": "男"},
    {"id": 21, "grade": "迟贵命", "gz": "丁卯 己酉 癸巳 壬子", "gender": "男"},
    {"id": 22, "grade": "掾曹命", "gz": "癸亥 戊午 辛丑 己丑", "gender": "男"},
    {"id": 23, "grade": "贵而带疾命", "gz": "戊子 辛酉 丙戌 辛卯", "gender": "男"},
    {"id": 24, "grade": "上达命", "gz": "丁酉 庚戌 己丑 乙亥", "gender": "男"},
    {"id": 25, "grade": "创业命", "gz": "癸未 丁巳 庚午 丙子", "gender": "男"},
    {"id": 26, "grade": "寻常命", "gz": "癸巳 癸亥 甲寅 甲戌", "gender": "男"},
    {"id": 27, "grade": "安常命", "gz": "庚午 癸未 戊申 辛酉", "gender": "男"},
    {"id": 28, "grade": "寻常命", "gz": "壬午 丁未 甲寅 壬申", "gender": "男"},
    {"id": 29, "grade": "寻常命", "gz": "庚寅 乙酉 丙午 戊戌", "gender": "男"},
    {"id": 30, "grade": "中平命", "gz": "甲申 庚午 壬寅 庚戌", "gender": "男"},
    {"id": 31, "grade": "名利破相命", "gz": "丙辰 乙未 丁酉 辛亥", "gender": "男"},
    {"id": 32, "grade": "带疾延寿命", "gz": "壬子 壬子 庚申 乙酉", "gender": "男"},
    {"id": 33, "grade": "身婴微疾命", "gz": "丁亥 辛亥 丙寅 庚寅", "gender": "男"},
    {"id": 34, "grade": "常人带疾命", "gz": "丁亥 壬子 丁巳 辛亥", "gender": "男"},
    {"id": 35, "grade": "起倒命", "gz": "壬申 己酉 壬申 甲辰", "gender": "男"},
    {"id": 36, "grade": "封诰命", "gz": "癸巳 庚申 丙寅 壬辰", "gender": "女"},
    {"id": 37, "grade": "受封命", "gz": "癸未 癸亥 乙丑 壬午", "gender": "女"},
    {"id": 38, "grade": "安常命", "gz": "丁酉 己酉 己巳 戊辰", "gender": "女"},
    {"id": 39, "grade": "无子带疾命", "gz": "庚辰 甲申 乙酉 辛巳", "gender": "女"},
    {"id": 40, "grade": "中平命", "gz": "甲午 丙子 甲午 甲戌", "gender": "女"},
]

# 干支→索引
SKY = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
EARTH = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

def gz_to_indices(gz_str):
    """干支字符串→(年天干/年地支/月天干/月地支/日天干/日地支/时天干/时地支索引)"""
    parts = gz_str.split()
    result = []
    for p in parts:
        if len(p) >= 2:
            t = SKY.index(p[0]) if p[0] in SKY else -1
            d = EARTH.index(p[1]) if p[1] in EARTH else -1
            result.extend([t, d])
    return result

def gz_year_offset(gz_str):
    """从年柱干支推算可能的公历年份范围
    郑希诚是元代人(约1280-1360)，星案大约在此期间
    """
    parts = gz_str.split()
    year_gz = parts[0]
    t = SKY.index(year_gz[0])
    d = EARTH.index(year_gz[1])
    # 干支年: 天干10循环, 地支12循环, 组合60循环
    # 甲子=0, 乙丑=1, ..., 癸亥=59
    gz_index = (d - t) % 12 + t * 6  # 简化计算
    # 实际: 干支序号 = (天干索引 - 地支索引) % 12 是判断同余的
    # 甲子: t=0,d=0 → 0; 乙丑: t=1,d=1 → 1; ...; 癸亥: t=9,d=11 → 59
    # 公式: 序号 = (d - t) % 12 * 5 + t  (不对)
    # 正确: 序号满足 序号%10=t 且 序号%12=d
    # 用CRT: 序号 = t + 10*k, 且 (t+10*k)%12 = d → k = (d-t)*inv(10,12)
    # 10和12不互质，需要特殊处理
    # 简单方法：遍历60甲子找匹配
    for i in range(60):
        if i % 10 == t and i % 12 == d:
            gz_index = i
            break
    # 甲子年对应的公历年: 1984是甲子年, 1924也是, 1864也是...
    # 元代约1300-1360, 找最近的甲子=1984-60*11=1324
    # 1324是甲子年, 所以元代甲子=1324
    base_years = [1324, 1384]  # 元代两个甲子年
    possible_years = []
    for base in base_years:
        y = base + gz_index
        if 1280 <= y <= 1400:
            possible_years.append(y)
    return possible_years, gz_index

if __name__ == "__main__":
    print(f"郑氏星案共{len(ZHENG_40_CASES)}例\n")

    # 命格等级分布
    grades = {}
    for c in ZHENG_40_CASES:
        g = c["grade"]
        grades[g] = grades.get(g, 0) + 1
    print("命格等级分布:")
    for g, n in sorted(grades.items(), key=lambda x: -x[1]):
        print(f"  {g}: {n}例")

    # 性别分布
    males = sum(1 for c in ZHENG_40_CASES if c["gender"] == "男")
    females = sum(1 for c in ZHENG_40_CASES if c["gender"] == "女")
    print(f"\n性别: 男{males}例, 女{females}例")

    # 推算年份
    print("\n年份推算（元代约1280-1400）:")
    for c in ZHENG_40_CASES[:5]:
        years, idx = gz_year_offset(c["gz"])
        print(f"  星案{c['id']}({c['grade']}): {c['gz']} → 干支序号{idx} → 可能年份{years}")

    # 检查重复
    print("\n重复四柱检查:")
    gz_set = {}
    for c in ZHENG_40_CASES:
        gz = c["gz"]
        if gz in gz_set:
            print(f"  重复: 星案{gz_set[gz]}和星案{c['id']}都是{gz}")
        else:
            gz_set[gz] = c["id"]
