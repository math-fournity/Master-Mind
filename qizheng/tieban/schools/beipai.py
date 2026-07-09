"""铁板神数北派实现。

北派特征：
- 主算：月干支太玄数 + 时干支太玄数
- 算法B1：先天基本卦（年柱+月柱→上卦下卦→先天数）
- 算法B2：后天基本卦（日柱+时柱→上卦下卦→后天数+互卦）
- 展开：±96×{1,2,3,4}
- 八卦滚法：基本数÷9和÷6的余数→变爻位置→变卦
"""
from typing import List, Optional
from ..core import (
    algorithm_a, algorithm_b_xiantian, algorithm_b_houtian,
    expand_48, expand_96, gender_secret, kaoke_base,
    yuan_ganzhi_num, bagua_gun,
)
from .base import TiebanSchool


class BeipaiSchool(TiebanSchool):
    """北派（月干支+时干支主算，含八卦滚法）。"""

    def name(self) -> str:
        return '北派'

    def compute_base(self, year_gz: str, month_gz: str, day_gz: str, hour_gz: str,
                     gender: str, yuan: str) -> dict:
        """北派基本数计算。

        主算：算法B1（先天基本卦）+ 算法B2（后天基本卦）
        八卦滚法：在基本数基础上变爻展开
        """
        base_a = algorithm_a(year_gz, month_gz, day_gz, hour_gz)
        base_b_xt = algorithm_b_xiantian(year_gz, month_gz, gender)
        result_b_ht = algorithm_b_houtian(day_gz, hour_gz)
        base_b_ht = result_b_ht['basic_num']

        year_gan = year_gz[0]
        year_zhi = year_gz[1]
        yuan_num = yuan_ganzhi_num(year_gan, year_zhi, yuan, gender)

        # 八卦滚法（在先天基本数上）
        bagua = bagua_gun(base_b_xt, yuan, gender, year_gan, year_zhi)

        return {
            'base_num': base_b_xt,
            'method': '算法B1（先天基本卦）+ 八卦滚法',
            'detail': {
                'base_a': base_a,
                'base_b_xt': base_b_xt,
                'base_b_ht': base_b_ht,
                'yuan_ganzhi_num': yuan_num,
                'bagua_gun': bagua,
            }
        }

    def expand(self, base_num: int, gender: str) -> List[int]:
        """北派展开：±96×{1,2,3,4}。"""
        return expand_96(base_num)

    def kaoke(self, base_num: int, father_zhi: str, mother_zhi: str) -> int:
        """北派考刻。"""
        kaoke_num = kaoke_base(father_zhi, mother_zhi)
        return expand_96(kaoke_num)
