#!/usr/bin/env python3
"""洞微大限小工具: 输入命主信息 -> 输出大限/小限/飞限 JSON。
用法:
  daxian.py --year 1990 --month 5 --day 15 --hour 3.5 --age 35
  daxian.py --json '{"year":1990,"month":5,"day":15,"hour":3.5,"age":35}'
"""
import sys, json, argparse
from . import core

def main():
    ap = argparse.ArgumentParser(description="洞微大限分析")
    ap.add_argument("--json", help="JSON 输入")
    ap.add_argument("--year", type=int)
    ap.add_argument("--month", type=int)
    ap.add_argument("--day", type=int)
    ap.add_argument("--hour", type=float, help="UT 小数")
    ap.add_argument("--age", type=int, required=True)
    ap.add_argument("--lon", type=float, default=116.4)
    ap.add_argument("--lat", type=float, default=39.9)
    ap.add_argument("--ephe", default="ephe")
    args = ap.parse_args()

    if args.json:
        inp = json.loads(args.json)
    else:
        inp = {k: getattr(args, k) for k in ["year","month","day","hour","lon","lat"]}
    y, mo, d, h = inp["year"], inp["month"], inp["day"], inp["hour"]
    core.init_ephe(args.ephe)
    jd = core.jd_from_ymd_ut(y, mo, d, h)
    bodies = core.calc_all_bodies(jd)
    sun_pos = bodies["sun"]["lon"]
    cusps, ascmc = core.calc_houses(jd, inp.get("lat",39.9), inp.get("lon",116.4))
    life_sign = core.calc_life_sign([y,mo,d,int(h),int((h%1)*60)], sun_pos, cusps)
    child_yr = core.calc_child_limit_years(life_sign)

    out = {
        "input": {"birth": f"{y:04d}-{mo:02d}-{d:02d}T{h:07.4f}", "age": args.age},
        "life_sign": round(life_sign, 6),
        "child_limit_years": child_yr,
        "daxian_current": core.calc_daxian(life_sign, args.age, child_yr),
        "daxian_all": core.daxian_full(life_sign, child_yr),
        "small_limit": round(core.small_limit(life_sign, args.age), 6),
        "child_limit_pos": round(core.child_limit_pos(life_sign, args.age), 6) if args.age < len(core._c()["limits"]["child_seq"]) else None,
        "fly_limit": round(core.fly_limit(life_sign, args.age, child_yr), 6) if core.fly_limit(life_sign, args.age, child_yr) else None,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
