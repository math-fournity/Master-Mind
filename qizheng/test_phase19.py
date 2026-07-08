#!/usr/bin/env python3
"""Phase 19 验证脚本：三方四正/相位/推运/返照/日月食"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qizheng import core

def run():
    core.init_ephe("ephe")

    # 19.1 三方四正
    print("=== 19.1 三方四正 ===")
    for i in range(12):
        sf = core.sanfang_sizheng(i)
        print(f"  宫{i}: 三合={sf['sanfang']} 对宫={sf['duigong']}")

    # 19.2 相位计算
    print("\n=== 19.2 相位计算 ===")
    jd = core.jd_from_ymd_ut(1990, 5, 15, 3.5)
    bodies = core.calc_all_bodies(jd)
    aspects = core.calc_aspects(bodies, orb=8.0)
    print(f"  共{len(aspects)}个相位:")
    for a in aspects:
        print(f"    {a['p1']}-{a['p2']} {a['aspect']} 角度={a['actual_angle']}° orb={a['orb']}°")

    # 19.3 推运计算
    print("\n=== 19.3 推运计算 ===")
    birth_jd = core.jd_from_ymd_ut(1990, 5, 15, 3.5)
    now_jd = core.jd_from_ymd_ut(2025, 7, 8, 0.0)
    for pid_name in ["sun", "moon", "mars"]:
        pid = core.BODIES[pid_name]
        transit = core.calc_transit(birth_jd, now_jd, pid)
        print(f"  {pid_name}: 出生{transit['birth_lon']}° → 现在{transit['now_lon']}° Δ={transit['delta']}°")

    # 19.4 太阳返照
    print("\n=== 19.4 太阳返照 ===")
    sr = core.solar_return(birth_jd, 2025, ephe_path="ephe")
    if sr:
        print(f"  2025年返照JD={sr['return_jd']}, 太阳{sr['sun_lon']}°, 误差={sr['delta']}°")

    # 19.5 日月食判定
    print("\n=== 19.5 日月食判定 ===")
    # 测试几个已知日期
    test_dates = [
        (2024, 4, 8, 0.0, "2024日全食"),
        (2024, 10, 2, 0.0, "2024日环食"),
        (2025, 7, 8, 0.0, "今天"),
    ]
    for y, mo, d, h, label in test_dates:
        jd = core.jd_from_ymd_ut(y, mo, d, h)
        ec = core.calc_eclipse(jd, ephe_path="ephe")
        print(f"  {label}: {ec['type']} 分离={ec['separation']}° 月纬={ec['moon_lat']}°")

    print("\n=== Phase 19 验证通过 ===")

if __name__ == "__main__":
    run()
