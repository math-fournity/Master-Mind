"""铁板神数南派实现。

南派特征：
- 主算：日干支太玄数 + 时干支太玄数
- 算法A：太玄数直接合数（四柱太玄数相加→舍十位个位）
- 展开：±48×{2,4,8,16}（北派也用此法，南派具体展开方式需进一步考据）
- 性别秘数：男+7130，女+7600（占位值）
"""
from typing import List, Optional
from ..core import (
    algorithm_a, algorithm_b_xiantian, algorithm_b_houtian,
    expand_48, expand_96, gender_secret, kaoke_base,
    yuan_ganzhi_num, bagua_gun,
)
from .base import TiebanSchool


class NanpaiSchool(TiebanSchool):
    """南派（日干支+时干支主算）。"""

    def name(self) -> str:
        return '南派'

    def compute_base(self, year_gz: str, month_gz: str, day_gz: str, hour_gz: str,
                     gender: str, yuan: str) -> dict:
        """南派基本数计算。

        主算：算法A（太玄数直接合数）
        辅算：算法B（先天/后天基本卦）
        """
        base_a = algorithm_a(year_gz, month_gz, day_gz, hour_gz)
        base_b_xt = algorithm_b_xiantian(year_gz, month_gz, gender)
        result_b_ht = algorithm_b_houtian(day_gz, hour_gz)
        base_b_ht = result_b_ht['basic_num']

        year_gan = year_gz[0]
        year_zhi = year_gz[1]
        yuan_num = yuan_ganzhi_num(year_gan, year_zhi, yuan, gender)

        return {
            'base_num': base_a,
            'method': '算法A（太玄数直接合数）',
            'detail': {
                'base_a': base_a,
                'base_b_xt': base_b_xt,
                'base_b_ht': base_b_ht,
                'yuan_ganzhi_num': yuan_num,
            }
        }

    def expand(self, base_num: int, gender: str) -> List[int]:
        """南派展开：±48×{2,4,8,16}。"""
        return expand_48(base_num)

    def kaoke(self, base_num: int, father_zhi: str, mother_zhi: str) -> int:
        """南派考刻。"""
        kaoke_num = kaoke_base(father_zhi, mother_zhi)
        return expand_96(kaoke_num)
