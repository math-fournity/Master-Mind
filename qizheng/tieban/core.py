"""铁板神数核心算法层。

包含：
- 天干地支常量与太玄数查表
- 先天/后天八卦查表
- 天干配卦、地支配卦
- 五行属性与生成数
- 八刻分配
- 三元甲子判定（上元/中元/下元）
- 五虎遁元（年干→月干）/ 五鼠遁元（日干→时干）
- 算法A（太玄数直接合数）
- 算法B1（先天基本卦）
- 算法B2（后天基本卦+互卦）
- 八卦滚法（变爻+变卦）
"""

from typing import List, Tuple, Optional

# ============================================================
# 一、天干地支常量
# ============================================================

TIAN_GAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
DI_ZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

GAN_INDEX = {g: i for i, g in enumerate(TIAN_GAN)}
ZHI_INDEX = {z: i for i, z in enumerate(DI_ZHI)}

# 六十甲子
JIAZI_60 = [f"{TIAN_GAN[i % 10]}{DI_ZHI[i % 12]}" for i in range(60)]
JIAZI_INDEX = {jz: i for i, jz in enumerate(JIAZI_60)}


def gan_yinyang(gan: str) -> str:
    """天干阴阳：甲丙戊庚壬=阳，乙丁己辛癸=阴。"""
    return '阳' if GAN_INDEX[gan] % 2 == 0 else '阴'


# ============================================================
# 二、太玄数查表
# ============================================================

# 天干太玄数：甲己9, 乙庚8, 丙辛7, 丁壬6, 戊癸5
TAIXUAN_GAN = {
    '甲': 9, '乙': 8, '丙': 7, '丁': 6, '戊': 5,
    '己': 9, '庚': 8, '辛': 7, '壬': 6, '癸': 5,
}

# 地支太玄数：子午9, 丑未8, 寅申7, 卯酉6, 辰戌5, 巳亥4
TAIXUAN_ZHI = {
    '子': 9, '丑': 8, '寅': 7, '卯': 6, '辰': 5, '巳': 4,
    '午': 9, '未': 8, '申': 7, '酉': 6, '戌': 5, '亥': 4,
}


def taixuan_pillar(gan: str, zhi: str) -> int:
    """一柱太玄数：干太玄×100 + 支太玄×10。

    例：甲子 → 9×100 + 9×10 = 990
    """
    return TAIXUAN_GAN[gan] * 100 + TAIXUAN_ZHI[zhi] * 10


def taixuan_gan(gan: str) -> int:
    """天干太玄数（单独）。"""
    return TAIXUAN_GAN[gan]


def taixuan_zhi(zhi: str) -> int:
    """地支太玄数（单独）。"""
    return TAIXUAN_ZHI[zhi]


# ============================================================
# 三、八卦查表（先天/后天）
# ============================================================

# 先天八卦数：乾1兑2离3震4巽5坎6艮7坤8
XIANTIAN_GUA = {1: '乾', 2: '兑', 3: '离', 4: '震', 5: '巽', 6: '坎', 7: '艮', 8: '坤'}
XIANTIAN_NUM = {v: k for k, v in XIANTIAN_GUA.items()}

# 后天八卦数（洛书）：坎1坤2震3巽4中5乾6兑7艮8离9
HOUTIAN_GUA = {1: '坎', 2: '坤', 3: '震', 4: '巽', 5: '中', 6: '乾', 7: '兑', 8: '艮', 9: '离'}
HOUTIAN_NUM = {v: k for k, v in HOUTIAN_GUA.items()}

# 八卦名称列表
GUA_NAMES = ['乾', '兑', '离', '震', '巽', '坎', '艮', '坤']


# ============================================================
# 四、天干配卦（天干→先天八卦）
# ============================================================

STEM_TO_GUA = {
    '壬': '乾', '甲': '乾',
    '乙': '坤', '癸': '坤',
    '丙': '艮', '丁': '兑',
    '戊': '坎', '己': '离',
    '庚': '震', '辛': '巽',
}


# ============================================================
# 五、地支配卦（地支→八卦，后天视角）
# ============================================================

BRANCH_TO_GUA = {
    '子': '坎', '亥': '坎',
    '寅': '震', '卯': '震',
    '巳': '离', '午': '离',
    '未': '坤',
    '申': '兑', '酉': '兑',
    '戌': '乾',
    '丑': '艮', '辰': '巽',
}


# ============================================================
# 六、五行属性与生成数
# ============================================================

# 八卦五行属性
GUA_WUXING = {
    '乾': '金', '兑': '金',
    '离': '火',
    '震': '木', '巽': '木',
    '坎': '水',
    '艮': '土', '坤': '土',
}

# 天干五行
GAN_WUXING = {
    '甲': '木', '乙': '木',
    '丙': '火', '丁': '火',
    '戊': '土', '己': '土',
    '庚': '金', '辛': '金',
    '壬': '水', '癸': '水',
}

# 地支五行
ZHI_WUXING = {
    '子': '水', '丑': '土',
    '寅': '木', '卯': '木',
    '辰': '土', '巳': '火',
    '午': '火', '未': '土',
    '申': '金', '酉': '金',
    '戌': '土', '亥': '水',
}

# 生成数对应：水1/火2/木3/金4/土5
WUXING_SHENGCHU = {
    '水': 1, '火': 2, '木': 3, '金': 4, '土': 5,
}


# ============================================================
# 七、八刻分配（刻→五行/地支组）
# ============================================================

KE_WUXING = {
    1: ('水', '亥子'),
    2: ('火', '巳午'),
    3: ('木', '寅卯'),
    4: ('金', '申酉'),
    5: ('土', '辰'),
    6: ('土', '未'),
    7: ('土', '戌'),
    8: ('土', '丑'),
}


# ============================================================
# 八、三元甲子判定
# ============================================================

# 三元甲子年份范围（公历）
# 上元甲子：1864-1923（60年）
# 中元甲子：1924-1983（60年）
# 下元甲子：1984-2043（60年）
YUAN_RANGES = {
    '上元': (1864, 1923),
    '中元': (1924, 1983),
    '下元': (1984, 2043),
}


def get_yuan(year: int) -> str:
    """根据公历年份判定三元甲子。

    Args:
        year: 公历年份

    Returns:
        '上元', '中元', '下元', 或 '越界'（超出1864-2043范围）
    """
    for yuan, (start, end) in YUAN_RANGES.items():
        if start <= year <= end:
            return yuan
    return '越界'


def get_yuan_from_ganzhi(gan: str, zhi: str) -> str:
    """根据年干支判定三元甲子（需要知道具体年份，此函数仅辅助）。

    注意：仅凭干支无法确定三元，因为同一干支60年出现一次，
    在不同世纪属于不同元。此函数假设1864-2043范围内。
    """
    # 甲子年=1864(上元), 1924(中元), 1984(下元)
    # 通过干支序号反推年份
    gz_idx = JIAZI_INDEX.get(f"{gan}{zhi}")
    if gz_idx is None:
        return '未知'
    # 甲子(0)对应1864/1924/1984
    # 需要知道具体年份才能判定三元
    return '需指定年份'


def yuan_ganzhi_num(gan: str, zhi: str, yuan: str, gender: str = '男') -> int:
    """三元甲子下的年干支数计算。

    上元：干×10 + 支×1
    中元（阳男阴女）：干×100 + 支×10
    中元（阴男阳女）：支×100 + 干×10
    下元：支×10 + 干×1

    Args:
        gan: 年天干
        zhi: 年地支
        yuan: '上元'/'中元'/'下元'
        gender: '男'/'女'

    Returns:
        年干支数
    """
    g = TAIXUAN_GAN[gan]
    z = TAIXUAN_ZHI[zhi]

    if yuan == '上元':
        return g * 10 + z * 1
    elif yuan == '下元':
        return z * 10 + g * 1
    elif yuan == '中元':
        yy = gan_yinyang(gan)
        is_male = (gender == '男')
        if (yy == '阳' and is_male) or (yy == '阴' and not is_male):
            # 阳男阴女
            return g * 100 + z * 10
        else:
            # 阴男阳女
            return z * 100 + g * 10
    else:
        raise ValueError(f"未知三元: {yuan}")


# ============================================================
# 九、五虎遁元（年干→月干）
# ============================================================

# 甲己年→丙寅起, 乙庚年→戊寅起, 丙辛年→庚寅起, 丁壬年→壬寅起, 戊癸年→甲寅起
WUHU_START = {
    '甲': '丙', '己': '丙',
    '乙': '戊', '庚': '戊',
    '丙': '庚', '辛': '庚',
    '丁': '壬', '壬': '壬',
    '戊': '甲', '癸': '甲',
}


def wuhu_month_gan(year_gan: str, month_zhi: str) -> str:
    """五虎遁元：年干→月干。

    Args:
        year_gan: 年天干
        month_zhi: 月地支（寅=正月, 卯=二月, ..., 丑=十二月）

    Returns:
        月天干
    """
    start_gan = WUHU_START[year_gan]
    start_idx = GAN_INDEX[start_gan]
    # 寅月(index 0)起, 月支序号从寅(2)开始
    month_offset = (ZHI_INDEX[month_zhi] - 2) % 12
    return TIAN_GAN[(start_idx + month_offset) % 10]


# ============================================================
# 十、五鼠遁元（日干→时干）
# ============================================================

# 甲己日→甲子起, 乙庚日→丙子起, 丙辛日→戊子起, 丁壬日→庚子起, 戊癸日→壬子起
WUSHU_START = {
    '甲': '甲', '己': '甲',
    '乙': '丙', '庚': '丙',
    '丙': '戊', '辛': '戊',
    '丁': '庚', '壬': '庚',
    '戊': '壬', '癸': '壬',
}


def wushu_hour_gan(day_gan: str, hour_zhi: str) -> str:
    """五鼠遁元：日干→时干。

    Args:
        day_gan: 日天干
        hour_zhi: 时地支

    Returns:
        时天干
    """
    start_gan = WUSHU_START[day_gan]
    start_idx = GAN_INDEX[start_gan]
    hour_offset = ZHI_INDEX[hour_zhi]
    return TIAN_GAN[(start_idx + hour_offset) % 10]


# ============================================================
# 十一、算法A：太玄数直接合数法
# ============================================================

def algorithm_a(year_gz: str, month_gz: str, day_gz: str, hour_gz: str) -> int:
    """算法A：四柱太玄数相加，舍弃十位个位（取整百）。

    Args:
        year_gz: 年柱（如"甲子"）
        month_gz: 月柱（如"丙寅"）
        day_gz: 日柱（如"丁卯"）
        hour_gz: 时柱（如"甲辰"）

    Returns:
        基本数（整百）
    """
    total = (taixuan_pillar(year_gz[0], year_gz[1]) +
             taixuan_pillar(month_gz[0], month_gz[1]) +
             taixuan_pillar(day_gz[0], day_gz[1]) +
             taixuan_pillar(hour_gz[0], hour_gz[1]))
    return (total // 100) * 100


# ============================================================
# 十二、算法B1：先天基本卦
# ============================================================

def algorithm_b_xiantian(year_gz: str, month_gz: str, gender: str) -> int:
    """算法B1：先天基本卦。

    阳男阴女：上卦=年柱, 下卦=月柱
    阴男阳女：上卦=月柱, 下卦=年柱

    年柱/月柱太玄数之和 ÷ 8 取余 → 先天卦数（余0当8=坤）

    Returns:
        先天基本数（上卦×1000 + 下卦×100）
    """
    year_gan, year_zhi = year_gz[0], year_gz[1]
    month_gan, month_zhi = month_gz[0], month_gz[1]

    yy = gan_yinyang(year_gan)
    is_male = (gender == '男')
    order_normal = (yy == '阳' and is_male) or (yy == '阴' and not is_male)

    year_sum = TAIXUAN_GAN[year_gan] + TAIXUAN_ZHI[year_zhi]
    month_sum = TAIXUAN_GAN[month_gan] + TAIXUAN_ZHI[month_zhi]

    if order_normal:
        upper_mod = year_sum % 8 or 8
        lower_mod = month_sum % 8 or 8
    else:
        upper_mod = month_sum % 8 or 8
        lower_mod = year_sum % 8 or 8

    upper_num = XIANTIAN_GUA[upper_mod]
    lower_num = XIANTIAN_GUA[lower_mod]

    return XIANTIAN_NUM[upper_num] * 1000 + XIANTIAN_NUM[lower_num] * 100


# ============================================================
# 十三、六爻卦（重卦）表与互卦计算
# ============================================================

# 六十四卦重卦表：上卦×下卦 → 卦名
# 上卦行（乾兑离震巽坎艮坤），下卦列（乾兑离震巽坎艮坤）
LIUYAO_64 = {
    ('乾', '乾'): '乾为天',   ('乾', '兑'): '天泽履',   ('乾', '离'): '天火同人', ('乾', '震'): '天雷无妄',
    ('乾', '巽'): '天风姤',   ('乾', '坎'): '天水讼',   ('乾', '艮'): '天山遁',   ('乾', '坤'): '天地否',
    ('兑', '乾'): '泽天夬',   ('兑', '兑'): '兑为泽',   ('兑', '离'): '泽火革',   ('兑', '震'): '泽雷随',
    ('兑', '巽'): '泽风大过', ('兑', '坎'): '泽水困',   ('兑', '艮'): '泽山咸',   ('兑', '坤'): '泽地萃',
    ('离', '乾'): '火天大有', ('离', '兑'): '火泽睽',   ('离', '离'): '离为火',   ('离', '震'): '火雷噬嗑',
    ('离', '巽'): '火风鼎',   ('离', '坎'): '火水未济', ('离', '艮'): '火山旅',   ('离', '坤'): '火地晋',
    ('震', '乾'): '雷天大壮', ('震', '兑'): '雷泽归妹', ('震', '离'): '雷火丰',   ('震', '震'): '震为雷',
    ('震', '巽'): '雷风恒',   ('震', '坎'): '雷水解',   ('震', '艮'): '雷山小过', ('震', '坤'): '雷地豫',
    ('巽', '乾'): '风天小畜', ('巽', '兑'): '风泽中孚', ('巽', '离'): '风火家人', ('巽', '震'): '风雷益',
    ('巽', '巽'): '巽为风',   ('巽', '坎'): '风水涣',   ('巽', '艮'): '风山渐',   ('巽', '坤'): '风地观',
    ('坎', '乾'): '水天需',   ('坎', '兑'): '水泽节',   ('坎', '离'): '水火既济', ('坎', '震'): '水雷屯',
    ('坎', '巽'): '水风井',   ('坎', '坎'): '坎为水',   ('坎', '艮'): '水山蹇',   ('坎', '坤'): '水地比',
    ('艮', '乾'): '山天大畜', ('艮', '兑'): '山泽损',   ('艮', '离'): '山火贲',   ('艮', '震'): '山雷颐',
    ('艮', '巽'): '山风蛊',   ('艮', '坎'): '山水蒙',   ('艮', '艮'): '艮为山',   ('艮', '坤'): '山地剥',
    ('坤', '乾'): '地天泰',   ('坤', '兑'): '地泽临',   ('坤', '离'): '地火明夷', ('坤', '震'): '地雷复',
    ('坤', '巽'): '地风升',   ('坤', '坎'): '地水师',   ('坤', '艮'): '地山谦',   ('坤', '坤'): '坤为地',
}

# 六爻爻位（从下到上：初爻=0, 二爻=1, 三爻=2, 四爻=3, 五爻=4, 上爻=5）
# 八卦三爻（从下到上）：乾=111(阳阳阳), 兑=110(阳阳阴), 离=101(阳阴阳), 震=001(阴阴阳)
#                       巽=011(阴阳阳), 坎=010(阴阳阴), 艮=001(阴阴阴), 坤=000(阴阴阴)
GUA_3YAO = {
    '乾': [1, 1, 1], '兑': [1, 1, 0], '离': [1, 0, 1], '震': [0, 0, 1],
    '巽': [0, 1, 1], '坎': [0, 1, 0], '艮': [0, 0, 0], '坤': [0, 0, 0],
}
# 注意：艮和坤的三爻都是0，需要修正。艮=100(阳阴阴)
GUA_3YAO['艮'] = [1, 0, 0]


def gua_to_liuyao(gua_name: str) -> List[int]:
    """八卦→六爻（三爻重复两次）。

    如乾(111)→[1,1,1,1,1,1]，兑(110)→[1,1,0,1,1,0]
    """
    san_yao = GUA_3YAO[gua_name]
    return san_yao + san_yao


def liuyao_to_gua(yao_list: List[int]) -> str:
    """六爻→八卦（取下三爻或上三爻，看是哪个卦）。

    六爻卦的上卦=爻3,4,5, 下卦=爻0,1,2
    """
    # 下卦（爻0,1,2）
    lower = yao_list[:3]
    # 上卦（爻3,4,5）
    upper = yao_list[3:]

    lower_gua = None
    upper_gua = None
    for name, yao in GUA_3YAO.items():
        if yao == lower:
            lower_gua = name
        if yao == upper:
            upper_gua = name

    return upper_gua, lower_gua


def calc_higua(upper_gua: str, lower_gua: str) -> Tuple[str, str]:
    """计算互卦。

    互卦：取六爻卦的爻2,3,4为下卦，爻3,4,5为上卦。
    即：重卦的中间四爻。

    Args:
        upper_gua: 上卦名
        lower_gua: 下卦名

    Returns:
        (互上卦, 互下卦)
    """
    # 构建六爻
    upper_yao = GUA_3YAO[upper_gua]
    lower_yao = GUA_3YAO[lower_gua]
    liuyao = lower_yao + upper_yao  # 爻0-2=下卦, 爻3-5=上卦

    # 互下卦 = 爻1,2,3
    hu_lower = [liuyao[1], liuyao[2], liuyao[3]]
    # 互上卦 = 爻2,3,4
    hu_upper = [liuyao[2], liuyao[3], liuyao[4]]

    # 查找对应的卦名
    hu_upper_name = None
    hu_lower_name = None
    for name, yao in GUA_3YAO.items():
        if yao == hu_upper:
            hu_upper_name = name
        if yao == hu_lower:
            hu_lower_name = name

    return hu_upper_name or '坤', hu_lower_name or '坤'


# ============================================================
# 十四、算法B2：后天基本卦
# ============================================================

def algorithm_b_houtian(day_gz: str, hour_gz: str) -> dict:
    """算法B2：后天基本卦。

    上卦 = (日干太玄 + 日支太玄 − 10) → 后天卦数
    下卦 = (时干太玄 + 时支太玄 − 10) → 后天卦数
    互卦 = 中间四爻

    Returns:
        {
            'upper_gua': 上卦名,
            'lower_gua': 下卦名,
            'hu_upper': 互上卦名,
            'hu_lower': 互下卦名,
            'upper_num': 上卦后天数,
            'lower_num': 下卦后天数,
            'hu_upper_num': 互上后天数,
            'hu_lower_num': 互下后天数,
            'basic_num': 后天基本数（上×1000+下×100+互上×10+互下）
        }
    """
    day_gan, day_zhi = day_gz[0], day_gz[1]
    hour_gan, hour_zhi = hour_gz[0], hour_gz[1]

    day_sum = TAIXUAN_GAN[day_gan] + TAIXUAN_ZHI[day_zhi] - 10
    hour_sum = TAIXUAN_GAN[hour_gan] + TAIXUAN_ZHI[hour_zhi] - 10

    # 后天卦数（和-10，范围1-8，0按8处理）
    upper_ht_num = day_sum if day_sum != 0 else 8
    lower_ht_num = hour_sum if hour_sum != 0 else 8

    upper_gua = HOUTIAN_GUA.get(upper_ht_num, '坤')
    lower_gua = HOUTIAN_GUA.get(lower_ht_num, '坤')

    # 互卦
    hu_upper, hu_lower = calc_higua(upper_gua, lower_gua)
    hu_upper_num = HOUTIAN_NUM.get(hu_upper, 2)
    hu_lower_num = HOUTIAN_NUM.get(hu_lower, 2)

    basic_num = upper_ht_num * 1000 + lower_ht_num * 100 + hu_upper_num * 10 + hu_lower_num

    return {
        'upper_gua': upper_gua,
        'lower_gua': lower_gua,
        'hu_upper': hu_upper,
        'hu_lower': hu_lower,
        'upper_num': upper_ht_num,
        'lower_num': lower_ht_num,
        'hu_upper_num': hu_upper_num,
        'hu_lower_num': hu_lower_num,
        'basic_num': basic_num,
    }


# ============================================================
# 十五、八卦滚法（变爻+变卦）
# ============================================================

def bagua_gun(base_num: int, yuan: str, gender: str = '男',
              year_gan: str = None, year_zhi: str = None) -> dict:
    """八卦滚法：在基本数基础上，通过变爻生成变卦，再展开为48条数序。

    算法：
    1. 用三元甲子年干支数作为基础
    2. ÷9取余 → 上卦变爻位置
    3. ÷6取余 → 下卦变爻位置
    4. 变爻后得到变卦
    5. 每个变卦对应一个数

    Args:
        base_num: 基本数（先天或后天）
        yuan: '上元'/'中元'/'下元'
        gender: '男'/'女'
        year_gan: 年天干（用于三元计算）
        year_zhi: 年地支（用于三元计算）

    Returns:
        {
            'yuan_num': 三元甲子年干支数,
            'div9_remainder': ÷9余数,
            'div6_remainder': ÷6余数,
            'upper_change_yao': 上卦变爻位置,
            'lower_change_yao': 下卦变爻位置,
            'original_upper': 原上卦,
            'original_lower': 原下卦,
            'changed_upper': 变后上卦,
            'changed_lower': 变后下卦,
            'gua_name': 原卦名,
            'changed_gua_name': 变卦名,
        }
    """
    # 计算三元甲子年干支数
    if year_gan and year_zhi:
        yuan_num = yuan_ganzhi_num(year_gan, year_zhi, yuan, gender)
    else:
        yuan_num = base_num

    # ÷9和÷6取余
    div9 = yuan_num % 9
    div6 = yuan_num % 6

    # 上卦变爻位置（余数0=不变，1=初爻变，...，8=上爻变）
    upper_change = div9
    # 下卦变爻位置（余数0=不变，1=初爻变，...，5=五爻变）
    lower_change = div6

    # 从基本数反推上下卦
    # 先天基本数：上×1000+下×100 → 上=base//1000, 下=(base%1000)//100
    # 后天基本数：上×1000+下×100+互上×10+互下
    upper_idx = base_num // 1000
    lower_idx = (base_num % 1000) // 100

    # 上下卦名（根据基本数类型判断是先天还是后天）
    if upper_idx >= 1 and upper_idx <= 8:
        # 先天卦数
        original_upper = XIANTIAN_GUA.get(upper_idx, '乾')
        original_lower = XIANTIAN_GUA.get(lower_idx, '乾')
    else:
        # 后天卦数
        original_upper = HOUTIAN_GUA.get(upper_idx, '乾')
        original_lower = HOUTIAN_GUA.get(lower_idx, '乾')

    # 变爻：翻转对应爻位
    def change_yao(gua_name: str, yao_pos: int) -> str:
        """对卦的指定爻位变爻（0=不变, 1-3=初二三爻）。"""
        if yao_pos == 0:
            return gua_name
        yao = GUA_3YAO[gua_name][:]
        pos = yao_pos - 1  # 转为0-indexed
        if pos < 3:
            yao[pos] = 1 - yao[pos]  # 翻转
        # 查找变后卦名
        for name, y in GUA_3YAO.items():
            if y == yao:
                return name
        return gua_name

    changed_upper = change_yao(original_upper, upper_change)
    changed_lower = change_yao(original_lower, lower_change)

    # 原卦名和变卦名
    gua_name = LIUYAO_64.get((original_upper, original_lower), '?')
    changed_gua_name = LIUYAO_64.get((changed_upper, changed_lower), '?')

    return {
        'yuan_num': yuan_num,
        'div9_remainder': div9,
        'div6_remainder': div6,
        'upper_change_yao': upper_change,
        'lower_change_yao': lower_change,
        'original_upper': original_upper,
        'original_lower': original_lower,
        'changed_upper': changed_upper,
        'changed_lower': changed_lower,
        'gua_name': gua_name,
        'changed_gua_name': changed_gua_name,
    }


# ============================================================
# 十六、展开法
# ============================================================

def expand_48(base: int) -> List[int]:
    """展开法1：±48×{2,4,8,16}，北派。"""
    return [
        base + 96, base + 192, base + 384, base + 768,
        base - 96, base - 192, base - 384, base - 768,
    ]


def expand_96(base: int) -> List[int]:
    """展开法2：±96×{1,2,3,4}，江南派。"""
    return [
        base + 96, base + 192, base + 288, base + 384,
        base - 96, base - 192, base - 288, base - 384,
    ]


# ============================================================
# 十七、性别秘数
# ============================================================

def gender_secret(base: int, gender: str) -> int:
    """性别秘数叠加（占位，取主流 +7130/+7600）。"""
    addend = 7130 if gender == '男' else 7600
    return (base + addend) % 10000


# ============================================================
# 十八、考刻（占位）
# ============================================================

def kaoke_base(father_zhi: str, mother_zhi: str) -> int:
    """父母生肖考刻表（占位生成）。

    已知：范围 9024–10454，步长 10，共 144 组合。
    实际值需从秘本填充。
    """
    fi = ZHI_INDEX[father_zhi]
    mi = ZHI_INDEX[mother_zhi]
    idx = fi * 12 + mi
    return 9024 + idx * 10


# ============================================================
# 十九、完整推演流程
# ============================================================

def tieban_deduction(year_gz: str, month_gz: str, day_gz: str, hour_gz: str,
                     gender: str, yuan: str,
                     ke: int = 1,
                     father_zhi: str = None, mother_zhi: str = None,
                     school: str = 'nanpai') -> dict:
    """铁板神数完整推演流程。

    Args:
        year_gz: 年柱（如"甲子"）
        month_gz: 月柱（如"丙寅"）
        day_gz: 日柱（如"丁卯"）
        hour_gz: 时柱（如"甲辰"）
        gender: '男'/'女'
        yuan: '上元'/'中元'/'下元'
        ke: 刻数（1-8）
        father_zhi: 父亲生肖（可选）
        mother_zhi: 母亲生肖（可选）
        school: 'nanpai'/'beipai'/'jiangnan'

    Returns:
        完整推演结果字典
    """
    year_gan = year_gz[0]
    year_zhi = year_gz[1]

    # 算法A
    base_a = algorithm_a(year_gz, month_gz, day_gz, hour_gz)

    # 算法B1（先天）
    base_b_xt = algorithm_b_xiantian(year_gz, month_gz, gender)

    # 算法B2（后天）
    result_b_ht = algorithm_b_houtian(day_gz, hour_gz)
    base_b_ht = result_b_ht['basic_num']

    # 三元甲子年干支数
    yuan_num = yuan_ganzhi_num(year_gan, year_zhi, yuan, gender)

    # 八卦滚法
    bagua = bagua_gun(base_b_xt, yuan, gender, year_gan, year_zhi)

    # 展开
    seq_48 = expand_48(base_a)
    seq_96 = expand_96(base_b_ht)

    # 性别秘数
    ht_gender = gender_secret(base_b_ht, gender)

    # 考刻
    kaoke_num = None
    if father_zhi and mother_zhi:
        kaoke_num = kaoke_base(father_zhi, mother_zhi)

    return {
        'four_poles': {'year': year_gz, 'month': month_gz, 'day': day_gz, 'hour': hour_gz},
        'gender': gender,
        'yuan': yuan,
        'ke': ke,
        'algorithm_a': {
            'base_num': base_a,
            'expanded_48': seq_48,
        },
        'algorithm_b_xt': {
            'base_num': base_b_xt,
        },
        'algorithm_b_ht': {
            'result': result_b_ht,
            'base_num': base_b_ht,
            'expanded_96': seq_96,
            'gender_secret': ht_gender,
        },
        'yuan_ganzhi_num': yuan_num,
        'bagua_gun': bagua,
        'kaoke_base': kaoke_num,
        'school': school,
    }
