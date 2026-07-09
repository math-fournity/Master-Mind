#!/usr/bin/env python3
"""
铁板神数全组合枚举引擎
枚举 八字(年干支×月支×日干支×时支) × 刻(1..8) 的全部命运配置，
对每种配置计算：
  - 算法A基数（太玄数直接合数）
  - 算法B先天/后天基本数
  - 性别秘数叠加
  - ±48 展开（北派）与 ±96 展开（江南派）的数序集合
  - 可达条文数序的统计

参考：dev-docs/raw_tieban_algorithm.md
"""

import json
import sys
import itertools
from pathlib import Path
from collections import Counter

# ── 查找表 ────────────────────────────────────────────────

# 表1：太玄数（干支→个位数）
TAIXUAN_STEM = {  # 甲己子午九，乙庚丑未八，丙辛寅申七，丁壬卯酉六，戊癸辰戌五
    '甲': 9, '乙': 8, '丙': 7, '丁': 6, '戊': 5,
    '己': 9, '庚': 8, '辛': 7, '壬': 6, '癸': 5,
}
TAIXUAN_BRANCH = {  # 子午9, 丑未8, 寅申7, 卯酉6, 辰戌5, 巳亥4
    '子': 9, '丑': 8, '寅': 7, '卯': 6, '辰': 5, '巳': 4,
    '午': 9, '未': 8, '申': 7, '酉': 6, '戌': 5, '亥': 4,
}

# 表2：先天八卦数
XIANTIAN_GUA = {1: '乾', 2: '兑', 3: '离', 4: '震', 5: '巽', 6: '坎', 7: '艮', 8: '坤'}
XIANTIAN_GUA_NUM = {v: k for k, v in XIANTIAN_GUA.items()}  # 乾1..坤8

# 表3：后天八卦数（洛书）
HOUTIAN_GUA = {1: '坎', 2: '坤', 3: '震', 4: '巽', 5: '中', 6: '乾', 7: '兑', 8: '艮', 9: '离'}
HOUTIAN_GUA_NUM = {v: k for k, v in HOUTIAN_GUA.items()}  # 坎1..离9

# 表4：天干配卦（天干→先天八卦）
STEM_TO_GUA = {
    '壬': '乾', '甲': '乾', '乙': '坤', '癸': '坤',
    '丙': '艮', '丁': '兑', '戊': '坎', '己': '离',
    '庚': '震', '辛': '巽',
}

# 表6：地支配卦（地支→八卦，后天视角）
BRANCH_TO_GUA = {
    '子': '坎', '亥': '坎',
    '寅': '震', '卯': '震',
    '巳': '离', '午': '离',
    '未': '坤',
    '申': '兑', '酉': '兑',
    '戌': '乾',
    '丑': '艮', '辰': '巽',
}

# 表9：八刻分配（刻→五行/地支组）
KE_WUXING = {
    1: '水(亥子)', 2: '火(巳午)', 3: '木(寅卯)', 4: '金(申酉)',
    5: '土(辰)', 6: '土(未)', 7: '土(戌)', 8: '土(丑)',
}

# ── 干支排列 ──────────────────────────────────────────────

TIAN_GAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
DI_ZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# 六十甲子
JIAZI_60 = [f"{TIAN_GAN[i % 10]}{DI_ZHI[i % 12]}" for i in range(60)]


# ── 核心算法 ──────────────────────────────────────────────

def taixuan_pillar(stem: str, branch: str) -> int:
    """一柱太玄数：干太玄×100 + 支太玄×10"""
    return TAIXUAN_STEM[stem] * 100 + TAIXUAN_BRANCH[branch] * 10


def algorithm_a(year: str, month: str, day: str, hour: str) -> int:
    """
    算法A：太玄数直接合数法
    四柱太玄数相加，舍弃十位个位（取整百）
    """
    total = (taixuan_pillar(year[0], year[1]) +
             taixuan_pillar(month[0], month[1]) +
             taixuan_pillar(day[0], day[1]) +
             taixuan_pillar(hour[0], hour[1]))
    return (total // 100) * 100


def get_yinyang(stem: str) -> str:
    """天干阴阳"""
    return '阳' if TIAN_GAN.index(stem) % 2 == 0 else '阴'


def algorithm_b_xiantian(year: str, month: str, gender: str) -> int:
    """
    算法B1：先天基本数
    阳男阴女：上卦=年柱, 下卦=月柱
    阴男阳女：上卦=月柱, 下卦=年柱
    先天基本数 = 上卦先天数×1000 + 下卦先天数×100
    （十位个位按留0处理——缺口G2，取主流约定）
    """
    yinyang = get_yinyang(year[0])
    is_male = (gender == '男')
    order_normal = (yinyang == '阳' and is_male) or (yinyang == '阴' and not is_male)

    year_sum = TAIXUAN_STEM[year[0]] + TAIXUAN_BRANCH[year[1]]
    month_sum = TAIXUAN_STEM[month[0]] + TAIXUAN_BRANCH[month[1]]

    if order_normal:
        upper_mod = year_sum % 8 or 8  # 余数0当8
        lower_mod = month_sum % 8 or 8
    else:
        upper_mod = month_sum % 8 or 8
        lower_mod = year_sum % 8 or 8

    upper_xt = XIANTIAN_GUA[upper_mod]
    lower_xt = XIANTIAN_GUA[lower_mod]

    return XIANTIAN_GUA_NUM[upper_xt] * 1000 + XIANTIAN_GUA_NUM[lower_xt] * 100


def algorithm_b_houtian(day: str, hour: str) -> int:
    """
    算法B2：后天基本数
    上卦 = (日干太玄 + 日支太玄 − 10) 查后天八卦数
    下卦 = (时干太玄 + 时支太玄 − 10) 查后天八卦数
    互卦 = 基本卦的二至四爻为下卦、三至五爻为上卦
    后天基本数 = 上卦后天×1000 + 下卦后天×100 + 互上后天×10 + 互下后天
    """
    day_sum = TAIXUAN_STEM[day[0]] + TAIXUAN_BRANCH[day[1]] - 10
    hour_sum = TAIXUAN_STEM[hour[0]] + TAIXUAN_BRANCH[hour[1]] - 10

    upper_ht_num = day_sum  # 后天数直接等于和-10（和范围10~18，-10后=0~8，但实际和≥11所以≥1）
    lower_ht_num = hour_sum

    # 映射到后天卦名
    upper_ht_name = HOUTIAN_GUA.get(upper_ht_num, '?')
    lower_ht_name = HOUTIAN_GUA.get(lower_ht_num, '?')

    # 互卦：用六爻卦的中间四爻
    # 1-8 的六爻表示：八卦 × 重复=六爻
    def gua_to_liuyao(ht_num):
        """后天数→八卦→六爻（三爻重复两次）"""
        name = HOUTIAN_GUA.get(ht_num, '坤')
        return [name] * 6  # 简化：互卦取2-3-4和3-4-5

    upper_liuyao = gua_to_liuyao(upper_ht_num)
    lower_liuyao = gua_to_liuyao(lower_ht_num)

    # 互卦上卦 = 爻3,4,5 → 与上卦同名（简化处理）
    # 互卦下卦 = 爻2,3,4 → 与下卦同名（简化处理）
    # 注：完整六爻互卦需要重卦(64卦)的精确爻位，这里用简化近似
    # 对于单卦重复的情况，互卦=本卦
    hu_upper_name = upper_ht_name
    hu_lower_name = lower_ht_name

    hu_upper_ht = HOUTIAN_GUA_NUM.get(hu_upper_name, 0)
    hu_lower_ht = HOUTIAN_GUA_NUM.get(hu_lower_name, 0)

    return upper_ht_num * 1000 + lower_ht_num * 100 + hu_upper_ht * 10 + hu_lower_ht


def expand_48(base: int) -> list:
    """展开法1：±48×{2,4,8,16}，北派"""
    return [
        base + 96, base + 192, base + 384, base + 768,
        base - 96, base - 192, base - 384, base - 768,
    ]


def expand_96(base: int) -> list:
    """展开法2：±96×{1,2,3,4}，江南派"""
    return [
        base + 96, base + 192, base + 288, base + 384,
        base - 96, base - 192, base - 288, base - 384,
    ]


def gender_secret(base: int, gender: str) -> int:
    """性别秘数叠加（占位，取主流 +7130/+7600）"""
    addend = 7130 if gender == '男' else 7600
    return (base + addend) % 10000


def kaoke_base(father_zhi: str, mother_zhi: str) -> int:
    """
    父母生肖考刻表（占位生成）
    已知：范围 9024–10454，步长 10，共 144 组合
    这里用线性映射占位，实际值需从秘本填充
    """
    fi = DI_ZHI.index(father_zhi)
    mi = DI_ZHI.index(mother_zhi)
    idx = fi * 12 + mi  # 0..143
    return 9024 + idx * 10  # 占位：9024, 9034, ..., 10454


# ── 枚举主循环 ────────────────────────────────────────────

def enumerate_all(max_configs: int = 0):
    """
    枚举 六十甲子年 × 月支 × 六十甲子日 × 时支 × 刻 的全部配置。
    max_configs > 0 时限制最大枚举量（调试用）。
    """
    stats = {
        'total': 0,
        'base_a_values': Counter(),
        'base_b_ht_values': Counter(),
        'base_b_xt_values': Counter(),
        'reachable_ids': set(),   # 所有可达的数序编号（百位级）
        'expansion_stats': {
            'method1_count': 0,  # ±48 展开
            'method2_count': 0,  # ±96 展开
            'unique_numbers': set(),
        },
        'gender_stats': {'男': 0, '女': 0},
        'ke_stats': Counter(),   # 刻分布
    }

    count = 0
    for year in JIAZI_60:
        for month_br in DI_ZHI:
            for day in JIAZI_60:
                for hour_br in DI_ZHI:
                    for ke in range(1, 9):
                        if max_configs > 0 and count >= max_configs:
                            return stats, count

                        count += 1
                        month = f"甲{month_br}"  # 月柱天干按年干推算（简化：固定甲）
                        hour = f"甲{hour_br}"    # 时柱天干按日干推算（简化：固定甲）

                        # 算法A
                        base_a = algorithm_a(year, month, day, hour)
                        stats['base_a_values'][base_a] += 1

                        # 算法B
                        for gender in ['男', '女']:
                            base_b_xt = algorithm_b_xiantian(year, month, gender)
                            base_b_ht = algorithm_b_houtian(day, hour)

                            stats['base_b_xt_values'][base_b_xt] += 1
                            stats['base_b_ht_values'][base_b_ht] += 1
                            stats['gender_stats'][gender] += 1

                            # 性别秘数叠加
                            ht_gender = gender_secret(base_b_ht, gender)

                            # ±48 展开
                            seq_48 = expand_48(base_a)
                            stats['expansion_stats']['method1_count'] += 1
                            stats['expansion_stats']['unique_numbers'].update(seq_48)
                            stats['reachable_ids'].update(seq_48)

                            # ±96 展开
                            seq_96 = expand_96(ht_gender)
                            stats['expansion_stats']['method2_count'] += 1
                            stats['expansion_stats']['unique_numbers'].update(seq_96)
                            stats['reachable_ids'].update(seq_96)

                            # 考刻占位
                            for father_zhi in DI_ZHI:
                                for mother_zhi in DI_ZHI:
                                    z = kaoke_base(father_zhi, mother_zhi)
                                    seq_kaoke = expand_96(z)
                                    stats['reachable_ids'].update(seq_kaoke)

                        stats['ke_stats'][ke] += 1
                        stats['total'] = count

                        if count % 500000 == 0:
                            print(f"  ... 已枚举 {count:,} 种配置", file=sys.stderr)

    return stats, count


def write_report(stats, count, output_dir: Path):
    """生成统计报告"""
    report = {
        'total_configs': count,
        'base_a_unique': len(stats['base_a_values']),
        'base_b_xt_unique': len(stats['base_b_xt_values']),
        'base_b_ht_unique': len(stats['base_b_ht_values']),
        'reachable_ids_count': len(stats['reachable_ids']),
        'reachable_ids_min': min(stats['reachable_ids']) if stats['reachable_ids'] else 0,
        'reachable_ids_max': max(stats['reachable_ids']) if stats['reachable_ids'] else 0,
        'expansion': {
            'method1_48x_count': stats['expansion_stats']['method1_count'],
            'method2_96x_count': stats['expansion_stats']['method2_count'],
            'unique_expanded_numbers': len(stats['expansion_stats']['unique_numbers']),
        },
        'gender_split': stats['gender_stats'],
        'base_a_top20': stats['base_a_values'].most_common(20),
        'ke_distribution': dict(stats['ke_stats']),
    }

    report_path = output_dir / 'tieban_enum_report.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2, default=str)
    print(f"报告已写入: {report_path}")

    # 可达数序集合（只存百位级摘要，全集太大）
    reachable_summary = sorted(stats['reachable_ids'])
    reachable_path = output_dir / 'tieban_reachable_ids.json'
    with open(reachable_path, 'w', encoding='utf-8') as f:
        json.dump({
            'count': len(reachable_summary),
            'min': min(reachable_summary) if reachable_summary else 0,
            'max': max(reachable_summary) if reachable_summary else 0,
            'sample_first_100': reachable_summary[:100],
            'sample_last_100': reachable_summary[-100:],
        }, f, ensure_ascii=False, indent=2)
    print(f"可达数序已写入: {reachable_path}")

    return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description='铁板神数全组合枚举引擎')
    parser.add_argument('--max', type=int, default=0, help='最大枚举量（0=不限）')
    parser.add_argument('--test', action='store_true', help='测试模式（8222+2900验证）')
    parser.add_argument('--output', type=str, default='dev-docs', help='输出目录')
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.test:
        print("=== 测试模式 ===")
        # 测试案例1：8222
        # 日甲(9)+午(9)-10=8→艮(8)；时乙(8)+亥(4)-10=2→坤(2)；互卦=坤为地(2,2)
        ht = algorithm_b_houtian('甲午', '乙亥')
        print(f"后天基本数（甲午/乙亥）= {ht}  （预期 8222）")
        assert ht == 8222, f"FAIL: got {ht}"

        # 测试案例2：2900
        a = algorithm_a('戊寅', '辛酉', '丁卯', '甲辰')
        print(f"算法A基数（戊寅+辛酉+丁卯+甲辰）= {a}  （预期 2900）")
        assert a == 2900, f"FAIL: got {a}"

        # 展开验证
        seq = expand_48(8222)
        expected = [8318, 8414, 8606, 8990, 8126, 8030, 7838, 7454]
        print(f"±48展开（8222）= {seq}")
        assert seq == expected, f"FAIL: got {seq}"

        print("✅ 全部测试通过")
        return

    print(f"=== 开始枚举 ===")
    if args.max > 0:
        print(f"限制最大枚举量: {args.max:,}")
    else:
        print("全量枚举（可能需要较长时间）")

    stats, count = enumerate_all(max_configs=args.max)
    report = write_report(stats, count, output_dir)

    print(f"\n=== 枚举完成 ===")
    print(f"总配置数: {count:,}")
    print(f"算法A不重复基数: {report['base_a_unique']:,}")
    print(f"算法B先天不重复数: {report['base_b_xt_unique']:,}")
    print(f"算法B后天不重复数: {report['base_b_ht_unique']:,}")
    print(f"可达条文数序（含展开）: {report['reachable_ids_count']:,}")
    print(f"数序范围: {report['reachable_ids_min']} ~ {report['reachable_ids_max']}")


if __name__ == '__main__':
    main()
