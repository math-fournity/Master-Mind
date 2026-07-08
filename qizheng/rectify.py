#!/usr/bin/env python3
"""星盘矫正小工具: 给定已知天体目标位置, 反推出生时间。
用法:
  rectify.py --year 1990 --month 5 --day 15 --hour 3.5 --target '{"sun":30.0}'
  rectify.py --json '{"year":1990,"month":5,"day":15,"hour":3.5,"target":{"sun":30.0}}'
"""
import sys, json, argparse
from . import core

def main():
    ap = argparse.ArgumentParser(description="星盘时间矫正")
    ap.add_argument("--json", help="JSON 输入")
    ap.add_argument("--year", type=int)
    ap.add_argument("--month", type=int)
    ap.add_argument("--day", type=int)
    ap.add_argument("--hour", type=float, help="初始 UT 小数")
    ap.add_argument("--target", help="目标黄经 JSON, 如 {\"sun\":30.0}")
    ap.add_argument("--ephe", default="ephe")
    args = ap.parse_args()

    if args.json:
        inp = json.loads(args.json)
    else:
        inp = {"year":args.year,"month":args.month,"day":args.day,"hour":args.hour,
               "target":json.loads(args.target) if args.target else {}}

    y, mo, d, h = inp["year"], inp["month"], inp["day"], inp["hour"]
    target = inp["target"]
    core.init_ephe(args.ephe)
    start_jd = core.jd_from_ymd_ut(y, mo, d, h)

    results = {}
    for name, deg in target.items():
        if name == "sun":
            jd_found = core.find_date_at_sun_pos(deg, start_jd)
        else:
            pid = core.BODIES.get(name)
            if pid is None:
                results[name] = {"error": f"unknown body {name}"}
                continue
            jd_found = core.find_date_at_planet_pos(pid, deg, start_jd)
        if jd_found is None:
            results[name] = {"error": "no solution"}
        else:
            fy, fmo, fd, fh = core.ymd_ut_from_jd(jd_found)
            results[name] = {
                "jd": round(jd_found, 8),
                "date_ut": f"{fy:04d}-{fmo:02d}-{fd:02d}T{fh:07.4f}",
                "delta_hours": round((jd_found - start_jd) * 24, 4),
            }

    out = {
        "input": {"start": f"{y:04d}-{mo:02d}-{d:02d}T{h:07.4f}", "jd": start_jd, "target": target},
        "results": results,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
