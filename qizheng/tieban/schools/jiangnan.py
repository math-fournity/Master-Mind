"""铁板神数江南派实现。

江南派特征：
- 八卦加则：天干配卦 + 地支配卦 + 生成数
- 甲流度考刻（需进一步研究具体算法）
- 展开：±96×{1,2,3,4}
- 与北派的主要差异：八卦加则法（天干配卦+地支配卦+生成数的组合）
"""
from typing import List, Optional
from ..core import (
    algorithm_a, algorithm_b_xiantian, algorithm_b_houtian,
    expand_48, expand_96, gender_secret, kaoke_base,
    yuan_ganzhi_num, bagua_gun,
    TIAN_GAN, DI_ZHI, GAN_INDEX, ZHI_INDEX,
    STEM_TO_GUA, BRANCH_TO_GUA,
    XIANTIAN_NUM, HOUTIAN_NUM,
    GUA_WUXING, WUXING_SHENGCHU,
    taixuan_gan, taixuan_zhi,
)
from .base import TiebanSchool


class JiangnanSchool(TiebanSchool):
    """江南派（八卦加则+甲流度考刻）。"""

    def name(self) -> str:
        return '江南派'

    def _bagua_jiaze(self, year_gz: str, month_gz: str, day_gz: str, hour_gz: str) -> dict:
        """八卦加则法：天干配卦+地支配卦+生成数。

        算法：
        1. 四柱天干各自配卦（先天八卦）
        2. 四柱地支各自配卦（后天八卦）
        3. 生成数叠加（水1/火2/木3/金4/土5）
        4. 综合得出基本数
        """
        pillars = [
            ('年', year_gz[0], year_gz[1]),
            ('月', month_gz[0], month_gz[1]),
            ('日', day_gz[0], day_gz[1]),
            ('时', hour_gz[0], hour_gz[1]),
        ]

        stem_guas = []  # 天干配卦
        branch_guas = []  # 地支配卦
        shengchu_sum = 0  # 生成数之和

        for label, gan, zhi in pillars:
            sg = STEM_TO_GUA.get(gan, '乾')
            bg = BRANCH_TO_GUA.get(zhi, '乾')
            stem_guas.append((label, gan, sg))
            branch_guas.append((label, zhi, bg))

            # 生成数
            sg_wx = GUA_WUXING.get(sg, '金')
            bg_wx = GUA_WUXING.get(bg, '金')
            shengchu_sum += WUXING_SHENGCHU.get(sg_wx, 4)
            shengchu_sum += WUXING_SHENGCHU.get(bg_wx, 4)

        # 八卦加则基本数 = 天干卦先天数之和 × 100 + 地支卦后天数之和 × 10 + 生成数
        stem_xt_sum = sum(XIANTIAN_NUM.get(g, 1) for _, _, g in stem_guas)
        branch_ht_sum = sum(HOUTIAN_NUM.get(g, 1) for _, _, g in branch_guas)

        base_num = stem_xt_sum * 100 + branch_ht_sum * 10 + shengchu_sum

        return {
            'base_num': base_num,
            'stem_guas': stem_guas,
            'branch_guas': branch_guas,
            'shengchu_sum': shengchu_sum,
            'stem_xt_sum': stem_xt_sum,
            'branch_ht_sum': branch_ht_sum,
        }

    def compute_base(self, year_gz: str, month_gz: str, day_gz: str, hour_gz: str,
                     gender: str, yuan: str) -> dict:
        """江南派基本数计算。

        主算：八卦加则法
        辅算：算法A/B（用于对比）
        """
        jiaze = self._bagua_jiaze(year_gz, month_gz, day_gz, hour_gz)
        base_a = algorithm_a(year_gz, month_gz, day_gz, hour_gz)
        base_b_xt = algorithm_b_xiantian(year_gz, month_gz, gender)
        result_b_ht = algorithm_b_houtian(day_gz, hour_gz)

        return {
            'base_num': jiaze['base_num'],
            'method': '八卦加则法',
            'detail': {
                'jiaze': jiaze,
                'base_a': base_a,
                'base_b_xt': base_b_xt,
                'base_b_ht': result_b_ht['basic_num'],
            }
        }

    def expand(self, base_num: int, gender: str) -> List[int]:
        """江南派展开：±96×{1,2,3,4}。"""
        return expand_96(base_num)

    def kaoke(self, base_num: int, father_zhi: str, mother_zhi: str) -> int:
        """江南派考刻（甲流度考刻，需进一步研究）。"""
        kaoke_num = kaoke_base(father_zhi, mother_zhi)
        return expand_96(kaoke_num)
