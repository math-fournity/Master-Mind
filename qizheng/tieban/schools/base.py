"""铁板神数学派抽象基类。"""
from abc import ABC, abstractmethod
from typing import List, Optional


class TiebanSchool(ABC):
    """铁板神数学派抽象基类。

    所有学派（南派/北派/江南派/中州派）实现此接口。
    """

    @abstractmethod
    def name(self) -> str:
        """学派名称。"""
        ...

    @abstractmethod
    def compute_base(self, year_gz: str, month_gz: str, day_gz: str, hour_gz: str,
                     gender: str, yuan: str) -> dict:
        """计算基本数。

        Args:
            year_gz: 年柱
            month_gz: 月柱
            day_gz: 日柱
            hour_gz: 时柱
            gender: '男'/'女'
            yuan: '上元'/'中元'/'下元'

        Returns:
            {
                'base_num': 基本数,
                'method': 算法名称,
                'detail': 详细计算过程,
            }
        """
        ...

    @abstractmethod
    def expand(self, base_num: int, gender: str) -> List[int]:
        """展开为数序集合。

        Args:
            base_num: 基本数
            gender: '男'/'女'

        Returns:
            数序列表（8个数）
        """
        ...

    @abstractmethod
    def kaoke(self, base_num: int, father_zhi: str, mother_zhi: str) -> int:
        """考刻叠加。

        Args:
            base_num: 基本数
            father_zhi: 父亲生肖
            mother_zhi: 母亲生肖

        Returns:
            考刻后的数
        """
        ...

    def deduce(self, year_gz: str, month_gz: str, day_gz: str, hour_gz: str,
               gender: str, yuan: str, ke: int = 1,
               father_zhi: Optional[str] = None, mother_zhi: Optional[str] = None) -> dict:
        """完整推演流程（模板方法，子类可覆盖）。"""
        base_result = self.compute_base(year_gz, month_gz, day_gz, hour_gz, gender, yuan)
        base_num = base_result['base_num']
        expanded = self.expand(base_num, gender)

        kaoke_num = None
        if father_zhi and mother_zhi:
            kaoke_num = self.kaoke(base_num, father_zhi, mother_zhi)

        return {
            'school': self.name(),
            'four_poles': {'year': year_gz, 'month': month_gz, 'day': day_gz, 'hour': hour_gz},
            'gender': gender,
            'yuan': yuan,
            'ke': ke,
            'base': base_result,
            'expanded': expanded,
            'kaoke_base': kaoke_num,
        }
