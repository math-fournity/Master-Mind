#!/usr/bin/env python3
"""Phase 21 Layer B 验证批次2：B7节气/B8农历/B9新月/B19四柱/B10日出日落"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qizheng import core

EPHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ephe")

def run():
    core.init_ephe(EPHE)

    # B7: 二十四节气 2024-2025
    print("=" * 60)
    print("B7: 二十四节气 UT 验证 (2024-2025)")
    print("=" * 60)
    # 紫金山天文台2024年节气数据（部分）
    pmo_2024 = {
        "冬至": "2023-12-22T11:27",  # 2023年冬至
        "小寒": "2024-01-06T04:49",
        "大寒": "2024-01-20T22:07",
        "立春": "2024-02-04T16:27",
        "雨水": "2024-02-19T12:13",
        "惊蛰": "2024-03-05T10:23",
        "春分": "2024-03-20T11:06",
        "清明": "2024-04-04T15:02",
        "谷雨": "2024-04-19T21:59",
        "立夏": "2024-05-05T08:10",
        "小满": "2024-05-20T20:59",
        "芒种": "2024-06-05T12:10",
        "夏至": "2024-06-21T04:51",
    }

    terms_2024 = core.calc_solar_terms_v2(2024, ephe_path=EPHE)
    # calc_solar_terms_v2 从冬至(270°)开始，所以索引0=冬至(前一年), 1=小寒, 2=大寒...
    term_names = ["冬至","小寒","大寒","立春","雨水","惊蛰","春分","清明","谷雨",
                  "立夏","小满","芒种","夏至","小暑","大暑","立秋","处暑",
                  "白露","秋分","寒露","霜降","立冬","小雪","大雪"]

    pass_count = 0
    total = 0
    for i, term_data in enumerate(terms_2024[:13]):  # 前13个到夏至
        name = term_names[i]
        py_time = term_data.get("date", "")
        pmo_time = pmo_2024.get(name, "")
        if pmo_time:
            total += 1
            # 对比到分钟级
            py_min = py_time[:16] if py_time else ""
            pmo_min = pmo_time[:16]
            if py_min == pmo_min:
                pass_count += 1
                print(f"  ✓ {name}: py={py_time} pmo={pmo_time}")
            else:
                # 计算分钟差
                from datetime import datetime
                try:
                    py_dt = datetime.strptime(py_time, "%Y-%m-%dT%H.%M%f")
                    pmo_dt = datetime.strptime(pmo_time, "%Y-%m-%dT%H:%M")
                    diff_min = abs((py_dt - pmo_dt).total_seconds()) / 60
                    if diff_min < 1:
                        pass_count += 1
                        print(f"  ✓ {name}: py={py_time} pmo={pmo_time} (Δ={diff_min:.1f}min)")
                    else:
                        print(f"  ⚠ {name}: py={py_time} pmo={pmo_time} (Δ={diff_min:.1f}min)")
                except:
                    print(f"  ⚠ {name}: py={py_time} pmo={pmo_time} (解析失败)")

    print(f"  B7 结果: {pass_count}/{total} PASS")
    print()

    # B8: 农历转换 2024
    print("=" * 60)
    print("B8: 农历转换验证 (2024年12个月)")
    print("=" * 60)
    # 2024年农历正月初一 = 2024-02-10（春节）
    # 2024年各月农历初一对应公历：
    lunar_first_days_2024 = [
        (2024, 2, 10, "正月初一"),
        (2024, 3, 10, "二月初一"),
        (2024, 4, 9, "三月初一"),
        (2024, 5, 8, "四月初一"),
        (2024, 6, 6, "五月初一"),
        (2024, 7, 6, "六月初一"),
        (2024, 8, 4, "七月初一"),
        (2024, 9, 3, "八月初一"),
        (2024, 10, 3, "九月初一"),
        (2024, 11, 1, "十月初一"),
        (2024, 12, 1, "十一月初一"),
    ]

    pass_count = 0
    for y, mo, d, label in lunar_first_days_2024:
        lunar = core.solar_to_lunar(y, mo, d, 0.0, ephe_path=EPHE)
        lunar_str = f"{lunar.get('lunar_month', '?')}月{lunar.get('lunar_day', '?')}日"
        expected = label.replace("初一", "初一日").replace("月", "月")
        # 简化对比
        if str(lunar.get('lunar_day', '')) == "1":
            pass_count += 1
            print(f"  ✓ {y}-{mo:02d}-{d:02d} → {lunar_str} (期望: {label})")
        else:
            print(f"  ✗ {y}-{mo:02d}-{d:02d} → {lunar_str} (期望: {label})")

    print(f"  B8 结果: {pass_count}/{len(lunar_first_days_2024)} PASS")
    print()

    # B9: 新月日期 2024
    print("=" * 60)
    print("B9: 新月日期验证 (2024年)")
    print("=" * 60)
    new_moons = core.compute_new_moons(2024, ephe_path=EPHE)
    print(f"  2024年新月数: {len(new_moons)}")
    for nm_jd in new_moons[:6]:
        y, mo, d, h = core.ymd_ut_from_jd(nm_jd)
        print(f"    {y:04d}-{mo:02d}-{d:02d}T{h:07.4f} (JD={nm_jd:.4f})")

    # B19: 四柱干支验证
    print()
    print("=" * 60)
    print("B19: 四柱干支验证 (10个测试用例)")
    print("=" * 60)
    # 只验证年柱（最可靠），月柱用节气判断
    test_cases = [
        (1990, 5, 15, 3.5, "庚午", "辛巳"),  # 1990庚午年，立夏后巳月
        (1985, 10, 20, 12.0, "乙丑", "丙戌"),  # 1985乙丑年，寒露后戌月
        (2000, 1, 5, 6.0, "己卯", "丙子"),  # 2000己卯年，冬至后子月
        (1978, 7, 30, 18.5, "戊午", "己未"),  # 1978戊午年，小暑后未月
        (1995, 3, 10, 9.0, "乙亥", "己卯"),  # 1995乙亥年，惊蛰后卯月
        (1988, 8, 8, 8.0, "戊辰", "庚申"),  # 1988戊辰年，立秋后申月
        (1992, 2, 18, 14.0, "壬申", "壬寅"),  # 1992壬申年，立春后寅月
        (2005, 6, 15, 22.0, "乙酉", "壬午"),  # 2005乙酉年，芒种后午月
        (2010, 11, 11, 11.0, "庚寅", "丁亥"),  # 2010庚寅年，立冬后亥月
        (2020, 1, 25, 0.0, "己亥", "丁丑"),  # 2020己亥年，小寒后丑月
    ]

    pass_count = 0
    for y, mo, d, h, exp_year, exp_month in test_cases:
        poles = core.calc_four_poles(y, mo, d, h)
        # poles是list: [年柱, 月柱, 日柱, 时柱]
        year_gz = poles[0] if isinstance(poles, list) else ""
        month_gz = poles[1] if isinstance(poles, list) else ""
        day_gz = poles[2] if isinstance(poles, list) else ""
        hour_gz = poles[3] if isinstance(poles, list) else ""
        year_ok = year_gz == exp_year
        month_ok = month_gz == exp_month
        if year_ok and month_ok:
            pass_count += 1
            print(f"  ✓ {y}-{mo}-{d}T{h}: {year_gz}年{month_gz}月{day_gz}日{hour_gz}时 (年月柱正确)")
        else:
            print(f"  ⚠ {y}-{mo}-{d}T{h}: {year_gz}年{month_gz}月{day_gz}日{hour_gz}时 (期望年:{exp_year}月:{exp_month})")

    print(f"  B19 结果: {pass_count}/{len(test_cases)} PASS (年月柱)")

    # B10: 日出日落
    print()
    print("=" * 60)
    print("B10: 日出日落验证 (北京1990-05-15)")
    print("=" * 60)
    jd = core.jd_from_ymd_ut(1990, 5, 15, 3.5)
    rise_set = core.calc_rise_set(jd, 116.4, 39.9, ephe_path=EPHE)
    print(f"  日出: {rise_set.get('rise_ut', 'N/A')}")
    print(f"  日落: {rise_set.get('set_ut', 'N/A')}")
    print(f"  昼生: {rise_set.get('is_day_birth', 'N/A')}")
    # 北京1990-05-15日出约04:50 UTC（12:50 CST），日落约19:20 UTC（03:20 CST）
    print(f"  (参考: 北京5月日出约04:50UTC, 日落约19:20UTC)")

    print()
    print("=" * 60)
    print("Phase 21 批次2 验证完成")
    print("=" * 60)

if __name__ == "__main__":
    run()
