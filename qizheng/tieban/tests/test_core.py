"""铁板神数核心算法测试。"""
import sys
sys.path.insert(0, '~/MOIRA_chinese_astrology-main')

from qizheng.tieban.core import (
    TIAN_GAN, DI_ZHI, JIAZI_60,
    TAIXUAN_GAN, TAIXUAN_ZHI,
    XIANTIAN_GUA, XIANTIAN_NUM, HOUTIAN_GUA, HOUTIAN_NUM,
    STEM_TO_GUA, BRANCH_TO_GUA,
    gan_yinyang, taixuan_pillar,
    get_yuan, yuan_ganzhi_num,
    wuhu_month_gan, wushu_hour_gan,
    algorithm_a, algorithm_b_xiantian, algorithm_b_houtian,
    bagua_gun, expand_48, expand_96,
    gender_secret, kaoke_base,
    calc_higua, GUA_3YAO,
)


def test_taixuan():
    """测试太玄数查表。"""
    assert TAIXUAN_GAN['甲'] == 9
    assert TAIXUAN_GAN['戊'] == 5
    assert TAIXUAN_ZHI['子'] == 9
    assert TAIXUAN_ZHI['亥'] == 4
    # 甲子 = 9×100 + 9×10 = 990
    assert taixuan_pillar('甲', '子') == 990
    # 丁卯 = 6×100 + 6×10 = 660
    assert taixuan_pillar('丁', '卯') == 660
    print("✅ 太玄数查表正确")


def test_yinyang():
    """测试天干阴阳。"""
    assert gan_yinyang('甲') == '阳'
    assert gan_yinyang('乙') == '阴'
    assert gan_yinyang('丙') == '阳'
    assert gan_yinyang('癸') == '阴'
    print("✅ 天干阴阳正确")


def test_yuan():
    """测试三元甲子判定。"""
    assert get_yuan(1864) == '上元'
    assert get_yuan(1923) == '上元'
    assert get_yuan(1924) == '中元'
    assert get_yuan(1983) == '中元'
    assert get_yuan(1984) == '下元'
    assert get_yuan(2043) == '下元'
    assert get_yuan(1863) == '越界'
    assert get_yuan(2044) == '越界'
    print("✅ 三元甲子判定正确")


def test_yuan_ganzhi_num():
    """测试三元年干支数。"""
    # 上元甲子：甲(9)×10 + 子(9)×1 = 99
    assert yuan_ganzhi_num('甲', '子', '上元') == 99
    # 下元甲子：子(9)×10 + 甲(9)×1 = 99
    assert yuan_ganzhi_num('甲', '子', '下元') == 99
    # 中元（阳男）甲子：甲(9)×100 + 子(9)×10 = 990
    assert yuan_ganzhi_num('甲', '子', '中元', '男') == 990
    # 中元（阴男）乙丑：乙(8)→阴，丑(8)→乙丑太玄和=8+8=16
    # 阴男：支×100 + 干×10 = 8×100 + 8×10 = 880
    assert yuan_ganzhi_num('乙', '丑', '中元', '男') == 880
    print("✅ 三元年干支数正确")


def test_wuhu():
    """测试五虎遁元。"""
    # 甲年正月(寅月) → 丙寅
    assert wuhu_month_gan('甲', '寅') == '丙'
    # 甲年二月(卯月) → 丁卯
    assert wuhu_month_gan('甲', '卯') == '丁'
    # 乙年正月(寅月) → 戊寅
    assert wuhu_month_gan('乙', '寅') == '戊'
    # 戊年正月(寅月) → 甲寅
    assert wuhu_month_gan('戊', '寅') == '甲'
    print("✅ 五虎遁元正确")


def test_wushu():
    """测试五鼠遁元。"""
    # 甲日子时 → 甲子
    assert wushu_hour_gan('甲', '子') == '甲'
    # 甲日丑时 → 乙丑
    assert wushu_hour_gan('甲', '丑') == '乙'
    # 乙日子时 → 丙子
    assert wushu_hour_gan('乙', '子') == '丙'
    # 戊癸日子时 → 壬子
    assert wushu_hour_gan('戊', '子') == '壬'
    assert wushu_hour_gan('癸', '子') == '壬'
    print("✅ 五鼠遁元正确")


def test_algorithm_a():
    """测试算法A（已有验证案例）。"""
    # 测试案例：戊寅+辛酉+丁卯+甲辰 = 2900
    a = algorithm_a('戊寅', '辛酉', '丁卯', '甲辰')
    assert a == 2900, f"FAIL: got {a}"
    print("✅ 算法A正确")


def test_algorithm_b_houtian():
    """测试算法B2后天基本卦。

    测试案例：甲午/乙亥
    甲午: 甲太玄9+午太玄9-10=8→艮
    乙亥: 乙太玄8+亥太玄4-10=2→坤
    互卦（正确六爻）: 艮/坤→坎/震 → 8213
    注：原 tieban_enum.py 用简化近似（互卦=本卦）得到8222，此为已知bug。
    """
    result = algorithm_b_houtian('甲午', '乙亥')
    assert result['basic_num'] == 8213, f"FAIL: got {result['basic_num']}"
    assert result['upper_gua'] == '艮'
    assert result['upper_num'] == 8
    assert result['lower_gua'] == '坤'
    assert result['lower_num'] == 2
    assert result['hu_upper'] == '坎'
    assert result['hu_lower'] == '震'
    print("✅ 算法B2后天基本卦正确（互卦用正确六爻计算）")


def test_higua():
    """测试互卦计算。"""
    # 乾为天(乾/乾)：六爻[1,1,1,1,1,1]，互卦=乾/乾
    hu_u, hu_l = calc_higua('乾', '乾')
    assert hu_u == '乾' and hu_l == '乾'

    # 坤为地(坤/坤)：六爻[0,0,0,0,0,0]，互卦=坤/坤
    hu_u, hu_l = calc_higua('坤', '坤')
    assert hu_u == '坤' and hu_l == '坤'

    # 天地否(乾/坤)：六爻[0,0,0,1,1,1]
    # 互下卦=爻1,2,3=[0,0,1]=震
    # 互上卦=爻2,3,4=[0,1,1]=巽
    hu_u, hu_l = calc_higua('乾', '坤')
    assert hu_l == '震', f"FAIL: got {hu_l}"
    assert hu_u == '巽', f"FAIL: got {hu_u}"

    print("✅ 互卦计算正确")


def test_expand():
    """测试展开法。"""
    seq48 = expand_48(1000)
    assert seq48 == [1096, 1192, 1384, 1768, 904, 808, 616, 232]

    seq96 = expand_96(1000)
    assert seq96 == [1096, 1192, 1288, 1384, 904, 808, 712, 616]

    print("✅ 展开法正确")


def test_bagua_gun():
    """测试八卦滚法。"""
    result = bagua_gun(2100, '上元', '男', '甲', '子')
    # 上元甲子：甲(9)×10+子(9)×1=99
    assert result['yuan_num'] == 99
    # 99÷9=11余0 → 不变
    assert result['div9_remainder'] == 0
    # 99÷6=16余3 → 三爻变
    assert result['div6_remainder'] == 3
    print("✅ 八卦滚法正确")


def test_gender_secret():
    """测试性别秘数。"""
    assert gender_secret(1000, '男') == (1000 + 7130) % 10000
    assert gender_secret(1000, '女') == (1000 + 7600) % 10000
    print("✅ 性别秘数正确")


if __name__ == '__main__':
    test_taixuan()
    test_yinyang()
    test_yuan()
    test_yuan_ganzhi_num()
    test_wuhu()
    test_wushu()
    test_algorithm_a()
    test_algorithm_b_houtian()
    test_higua()
    test_expand()
    test_bagua_gun()
    test_gender_secret()
    print("\n🎉 全部测试通过")
