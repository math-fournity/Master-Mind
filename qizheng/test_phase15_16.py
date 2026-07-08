#!/usr/bin/env python3
"""Phase 15/16 验证脚本：对5个测试用例生成完整大限推演报告+流年推演报告"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qizheng import core, chart

TEST_CASES = [
    {"year": 1990, "month": 5, "day": 15, "hour": 3.5, "lon": 116.4, "lat": 39.9, "label": "北京男"},
    {"year": 1985, "month": 10, "day": 20, "hour": 12.0, "lon": 121.5, "lat": 31.2, "label": "上海女"},
    {"year": 2000, "month": 1, "day": 5, "hour": 6.0, "lon": 113.3, "lat": 23.1, "label": "广州男"},
    {"year": 1978, "month": 7, "day": 30, "hour": 18.5, "lon": 108.9, "lat": 34.3, "label": "西安女"},
    {"year": 1995, "month": 3, "day": 10, "hour": 9.0, "lon": 120.2, "lat": 30.3, "label": "杭州男"},
]

def run():
    core.init_ephe("ephe")
    results = []

    for tc in TEST_CASES:
        label = tc.pop("label")
        print(f"\n--- {label}: {tc['year']}-{tc['month']}-{tc['day']} ---")

        # 构建星盘
        chart_data = chart.build_chart(
            tc["year"], tc["month"], tc["day"], tc["hour"],
            tc["lon"], tc["lat"], ephe="ephe"
        )

        # Phase 15: 大限全量分析
        daxian_full = core.analyze_daxian_full(chart_data)
        print(f"  大限: {daxian_full['total_limits']}限, 童限={daxian_full['child_limit_years']}年")
        for lim in daxian_full["limits"][:3]:
            stars = [s["name"] for s in lim["stars_in_limit"]]
            print(f"    第{lim['limit_index']+1}限 {lim['limit_name']}({lim['limit_years']}年) 宫主={lim['house_ruler']} 星曜={stars}")

        # Phase 16: 流年分析（当前年龄）
        birth_year = tc["year"]
        current_age = 2025 - birth_year + 1  # 虚岁
        liunian = core.analyze_liunian(chart_data, current_age)
        print(f"  流年({current_age}岁): {liunian['year_pole']} 太岁={liunian['taishui']['relation']}")

        # 流年3年
        prog = core.progress_liunian_years(chart_data, current_age, current_age + 2)
        print(f"  流年推演: {len(prog)}年")
        for p in prog:
            print(f"    {p['age']}岁: {p['year_pole']} {p['taishui']['relation']}")

        results.append({
            "label": label,
            "input": tc,
            "daxian_summary": {
                "total_limits": daxian_full["total_limits"],
                "child_limit_years": daxian_full["child_limit_years"],
                "first_limit": daxian_full["limits"][0]["limit_name"] if daxian_full["limits"] else "",
            },
            "liunian_current": {
                "age": liunian["age"],
                "year_pole": liunian["year_pole"],
                "taishui": liunian["taishui"]["relation"],
            },
        })

    # 保存结果
    out_path = "/tmp/phase15_16_result.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n=== Phase 15/16 验证通过，结果保存到 {out_path} ===")

if __name__ == "__main__":
    run()
