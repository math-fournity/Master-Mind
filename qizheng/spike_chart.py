#!/usr/bin/env python3
"""Python spike: 输入生辰 -> 输出七政四余天体恒星黄道 JSON.
对齐 Java spike (SpikeChart.java) 的结果。
用法: spike_chart.py year month day hour_ut lon lat
"""
import sys, json
import swisseph as swe

# 天体: 七政(日月水金火木土) + 四余(罗睺=真北交点, 计都=真南交点, 紫炁=远地点, 月孛=osc apog)
BODIES = [
    (swe.SUN,    "sun"),
    (swe.MOON,   "moon"),
    (swe.MERCURY,"mercury"),
    (swe.VENUS,  "venus"),
    (swe.MARS,   "mars"),
    (swe.JUPITER,"jupiter"),
    (swe.SATURN, "saturn"),
    (swe.TRUE_NODE, "true_node_rohuo"),
    (swe.MEAN_APOG, "mean_apog_ziqi"),
    (swe.OSCU_APOG,  "oscu_apog_yuebei"),
]

def main():
    if len(sys.argv) < 6:
        sys.exit("Usage: spike_chart.py year month day hour_ut lon lat")
    y, mo, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    h_ut = float(sys.argv[4])
    lon, lat = float(sys.argv[5]), float(sys.argv[6]) if len(sys.argv) > 6 else 0.0

    swe.set_ephe_path("ephe")
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
    jd = swe.julday(y, mo, d, h_ut)

    bodies = {}
    for pid, name in BODIES:
        xx, ret = swe.calc_ut(jd, pid, flag)
        if ret >= 0:
            bodies[name] = {
                "lon": round(xx[0], 6),
                "lat": round(xx[1], 6),
                "dist": round(xx[2], 8),
                "lon_speed": round(xx[3], 6),
                "lat_speed": round(xx[4], 6),
                "dist_speed": round(xx[5], 8),
            }
        else:
            bodies[name] = {"error": f"ret={ret}"}

    out = {
        "input": {
            "date_ut": f"{y:04d}-{mo:02d}-{d:02d}T{h_ut:07.4f}",
            "jd": jd,
            "lon": lon, "lat": lat,
            "ayanamsa": "Lahiri", "frame": "sidereal",
        },
        "bodies": bodies,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    swe.close()

if __name__ == "__main__":
    main()
