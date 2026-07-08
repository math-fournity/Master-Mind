"""
Phase 24: 郑氏星案端到端验证
干支四柱 → 公历 → 排盘 → 命格判断 → 与郑希诚原判对比

关键挑战：
1. 干支纪日→公历：需要基准日 + 60日循环
2. 年柱→公历年：需考虑立春分年（果老星宗用立春分年）
3. 月柱→公历月：需考虑节气分月
4. 时柱→UT：需考虑真太阳时+经度
5. 地点：郑希诚是浙江瑞安人，默认瑞安(120.65E, 27.78N)
"""

import sys
sys.path.insert(0, ".")
from qizheng import core, chart
from qizheng.zheng_cases import ZHENG_40_CASES, SKY, EARTH, gz_year_offset
from datetime import datetime, timedelta

# 干支纪日→公历转换
# 已知基准：1900年1月1日 = 甲戌日 (干支序号10)
# 实际：1900-01-31 = 甲戌日，需要验证
# 更可靠：2000年1月1日 = 戊午日 (干支序号54)
# 2000-01-07 = 甲子日 (干支序号0)

# 甲子=0, 乙丑=1, ..., 癸亥=59
def gz_to_index(gz):
    """单个干支→序号(0-59)"""
    t = SKY.index(gz[0])
    d = EARTH.index(gz[1])
    for i in range(60):
        if i % 10 == t and i % 12 == d:
            return i
    return -1

def index_to_gz(idx):
    """序号→干支"""
    return SKY[idx % 10] + EARTH[idx % 12]

# 日柱→公历日
# 基准：2000-01-07 = 甲子日(序号0)
DAY_BASE = datetime(2000, 1, 7)
DAY_BASE_IDX = 0  # 甲子

def day_gz_to_dates(day_gz, year_range=(1280, 1400)):
    """日柱干支→可能的公历日期列表（在year_range范围内）
    干支日60天循环，所以一个干支日每60天出现一次
    """
    target_idx = gz_to_index(day_gz)
    if target_idx < 0:
        return []

    # 从基准日往前推算到year_range
    # 基准2000-01-07=甲子, 序号0
    # 目标序号=target_idx
    # 基准到目标的偏移 = target_idx - 0 = target_idx (正向)
    # 或 = target_idx - 60 (负向)
    # 每60天循环一次

    # 先找到year_range开始时的干支序号
    start_date = datetime(year_range[0], 1, 1)
    end_date = datetime(year_range[1], 12, 31)

    # 从基准日到start_date的天数
    days_from_base = (start_date - DAY_BASE).days
    # start_date的干支序号
    start_idx = (DAY_BASE_IDX + days_from_base) % 60

    # 找到第一个目标日
    offset = (target_idx - start_idx) % 60
    first_target = start_date + timedelta(days=offset)

    # 每60天一个目标日
    dates = []
    d = first_target
    while d <= end_date:
        if d >= start_date:
            dates.append(d)
        d += timedelta(days=60)

    return dates

# 时柱→UT小时
# 时柱地支: 子=23-1, 丑=1-3, 寅=3-5, 卯=5-7, 辰=7-9, 巳=9-11,
#           午=11-13, 未=13-15, 申=15-17, 酉=17-19, 戌=19-21, 亥=21-23
HOUR_RANGES = {
    "子": (23, 1), "丑": (1, 3), "寅": (3, 5), "卯": (5, 7),
    "辰": (7, 9), "巳": (9, 11), "午": (11, 13), "未": (13, 15),
    "申": (15, 17), "酉": (17, 19), "戌": (19, 21), "亥": (21, 23),
}

def hour_gz_to_ut_range(hour_gz, lon=120.65):
    """时柱→UT小时范围
    lon: 经度（默认瑞安120.65E）
    返回(ut_start, ut_end, cross_day)
    cross_day: True表示UT跨日（需要用前一日）
    """
    earth_branch = hour_gz[1]
    local_start, local_end = HOUR_RANGES[earth_branch]

    # UT = 北京时间 - 8h
    if earth_branch == "子":
        # 子时=23-1CST, UT=15-17, 不跨UT日
        ut_start = 15.0  # 23CST
        ut_end = 17.0    # 1CST(次日) = 17UT(当日)
        return (ut_start, ut_end, False)
    else:
        ut_start = local_start - 8.0
        ut_end = local_end - 8.0
        if ut_start < 0:
            # UT为负，跨UT日（用前一日）
            ut_start += 24
            ut_end += 24
            return (ut_start, ut_end, True)
        return (ut_start, ut_end, False)

# 瑞安经纬度（郑希诚故乡）
RUIAN_LON = 120.65
RUIAN_LAT = 27.78

def case_to_chart(case):
    """郑氏星案→排盘
    返回chart或None
    """
    gz_parts = case["gz"].split()
    year_gz, month_gz, day_gz, hour_gz = gz_parts

    # 1. 年柱→公历年
    possible_years, gz_idx = gz_year_offset(case["gz"])
    if not possible_years:
        return None, "无法推算年份"

    # 2. 日柱→公历日（在元代明初范围内）
    possible_dates = day_gz_to_dates(day_gz, year_range=(1260, 1420))
    if not possible_dates:
        return None, "无法推算日期"

    # 3. 时柱→UT范围
    ut_start, ut_end, cross_day = hour_gz_to_ut_range(hour_gz, RUIAN_LON)

    # 4. 月柱地支→节气月范围
    # 寅=315-345(立春-惊蛰), 卯=345-15(惊蛰-清明), 辰=15-45, 巳=45-75,
    # 午=75-105, 未=105-135, 申=135-165, 酉=165-195, 戌=195-225,
    # 亥=225-255, 子=255-285, 丑=285-315
    month_branch = month_gz[1]
    branch_idx = EARTH.index(month_branch)
    # 寅=2对应立春(315°), 每月30°
    month_start = (315 + (branch_idx - 2) * 30) % 360
    month_end = (month_start + 30) % 360

    # 5. 组合：对每个可能日期，检查年份+月柱是否匹配
    for date in possible_dates:
        # 年份过滤放宽：允许date.year和可能的solar_year匹配
        # (立春前solar_year=date.year-1, 立春后solar_year=date.year)
        year_ok = (date.year in possible_years or
                   (date.year - 1) in possible_years or
                   (date.year + 1) in possible_years)
        if not year_ok:
            continue

        # 时柱→UT：北京时间→UT需要-8h，可能跨日
        # 子时特殊：用前半段(23:30CST=15.5UT)避免跨日
        if hour_gz[1] == "子":
            ut_mid = 15.5  # 23:30CST, 不跨日
        else:
            ut_mid = (ut_start + ut_end) / 2
        chart_date = date
        if cross_day:
            # UT跨日（子时以外的时柱UT为负时），用前一日
            chart_date = date - timedelta(days=1)

        try:
            # 直接用calc_four_poles验证（它内部处理跨日和节气分月）
            poles = core.calc_four_poles(chart_date.year, chart_date.month, chart_date.day, ut_mid,
                                         use_solar_terms=True)

            # 检查全部四柱
            year_match = poles[0] == year_gz
            month_match = poles[1] == month_gz
            day_match = poles[2] == day_gz
            hour_match = poles[3] == hour_gz

            if year_match and month_match and day_match and hour_match:
                c = chart.build_chart(chart_date.year, chart_date.month, chart_date.day,
                                     ut_mid, RUIAN_LON, RUIAN_LAT, ephe="ephe")
                return c, f"匹配: {chart_date.year}-{chart_date.month:02d}-{chart_date.day:02d}T{ut_mid:.2f}UT"
        except Exception as e:
            continue

    return None, "无匹配日期"

def run_phase24():
    """Phase 24: 郑氏星案端到端验证"""
    EPHE = "ephe"
    core.init_ephe(EPHE)

    print("=" * 70)
    print("Phase 24: 郑氏星案40例端到端验证")
    print("=" * 70)

    success = 0
    fail = 0
    no_match = 0

    for case in ZHENG_40_CASES:  # 全部40例
        print(f"\n--- 星案{case['id']}: {case['grade']} ({case['gender']}) ---")
        print(f"  四柱: {case['gz']}")

        c, msg = case_to_chart(case)
        if c:
            print(f"  ✓ {msg}")
            # 输出关键信息
            life_sign = c.get("life_sign")
            self_sign = c.get("self_sign")
            houses = c.get("houses", {})
            asc = houses.get("asc")
            print(f"  命宫: {life_sign:.2f}°" if life_sign else "  命宫: N/A")
            print(f"  身宫: {self_sign:.2f}°" if self_sign else "  身宫: N/A")
            print(f"  ASC: {asc:.2f}°" if asc else "  ASC: N/A")

            # 输出七政四余位置
            bodies = c.get("bodies", {})
            for name in ["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn"]:
                if name in bodies:
                    lon = bodies[name].get("lon", 0)
                    print(f"  {name}: {lon:.2f}°")

            success += 1
        else:
            print(f"  ✗ {msg}")
            no_match += 1

    print(f"\n{'=' * 70}")
    print(f"Phase 24 初步结果: {success}成功, {no_match}无匹配, {fail}失败")
    print(f"{'=' * 70}")

if __name__ == "__main__":
    run_phase24()
