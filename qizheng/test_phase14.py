#!/usr/bin/env python3
"""Phase 14 验证脚本：用已知出生时间生成3个模拟事件→矫正→验证反推精度"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qizheng import core

def run():
    core.init_ephe("ephe")

    # 已知出生时间
    birth = {"year": 1990, "month": 5, "day": 15, "hour": 3.5, "lon": 116.4, "lat": 39.9}
    birth_jd = core.jd_from_ymd_ut(birth["year"], birth["month"], birth["day"], birth["hour"])

    # 获取出生时的行星位置作为"目标"
    bodies = core.calc_all_bodies(birth_jd)
    print("=== 出生时行星位置 ===")
    targets = {}
    for name in ["sun", "moon", "mars"]:
        lon = bodies[name]["lon"]
        targets[name] = lon
        print(f"  {name}: {lon}°")

    # 14.1 多点反推
    print("\n=== 14.1 多点反推 ===")
    # 用出生前1天的JD作为搜索起点
    search_jd = birth_jd - 1.0
    result = core.rectify_multi_point(targets, search_jd, ephe_path="ephe")
    print(f"  反推结果数: {result['jd_count']}")
    print(f"  一致性评分: {result['consistency_score']}")
    for name, r in result["results"].items():
        if "jd" in r:
            delta = abs(r["jd"] - birth_jd) * 24
            print(f"  {name}: {r['date_ut']} (Δ={delta:.4f}小时)")

    # 14.2 一致性评分
    print("\n=== 14.2 一致性评分 ===")
    score = core._consistency_score([birth_jd, birth_jd + 0.01, birth_jd - 0.01])
    print(f"  小偏差评分: {score}")
    score2 = core._consistency_score([birth_jd, birth_jd + 1.0, birth_jd - 1.0])
    print(f"  大偏差评分: {score2}")

    # 14.3 迭代矫正
    print("\n=== 14.3 迭代矫正 ===")
    life_events = [
        {"year": 1990, "event_type": "birth", "description": "出生",
         "target_planet": "sun", "target_degree": targets["sun"]},
        {"year": 1990, "event_type": "birth", "description": "出生",
         "target_planet": "moon", "target_degree": targets["moon"]},
        {"year": 1990, "event_type": "birth", "description": "出生",
         "target_planet": "mars", "target_degree": targets["mars"]},
    ]
    rect = core.iterative_rectify(birth, life_events, ephe_path="ephe")
    print(f"  原始: {rect['original_ut']}")
    print(f"  矫正: {rect['corrected_ut']}")
    print(f"  Δ小时: {rect['delta_hours']}")
    print(f"  一致性: {rect['consistency']}")

    # 验证精度
    if rect["corrected_jd"]:
        precision = abs(rect["corrected_jd"] - birth_jd) * 24
        print(f"  矫正精度: {precision:.4f}小时")
        if precision < 1.0:
            print("  ✓ 精度<1小时")
        else:
            print(f"  ⚠ 精度{precision:.2f}小时（>1小时）")

    print("\n=== Phase 14 验证完成 ===")

if __name__ == "__main__":
    run()
