"""铁板神数计算包。

包含多学派算法、条文语料库、枚举引擎、并行推演框架。
"""
from .core import (
    TIAN_GAN, DI_ZHI, JIAZI_60, GAN_INDEX, ZHI_INDEX,
    TAIXUAN_GAN, TAIXUAN_ZHI,
    XIANTIAN_GUA, XIANTIAN_NUM, HOUTIAN_GUA, HOUTIAN_NUM,
    STEM_TO_GUA, BRANCH_TO_GUA,
    GUA_WUXING, GAN_WUXING, ZHI_WUXING, WUXING_SHENGCHU,
    KE_WUXING,
    gan_yinyang, taixuan_pillar, taixuan_gan, taixuan_zhi,
    get_yuan, yuan_ganzhi_num,
    wuhu_month_gan, wushu_hour_gan,
    algorithm_a, algorithm_b_xiantian, algorithm_b_houtian,
    bagua_gun, expand_48, expand_96,
    gender_secret, kaoke_base,
    tieban_deduction,
)
