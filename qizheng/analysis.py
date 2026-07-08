"""
分析函数封装（实战核心）
提供高层次的命理分析接口，供 AI 直接调用。
"""

from typing import Dict, Any, List
from qizheng import core


def _get_house_for_degree(cusps: List[float], degree: float) -> int:
    for i in range(12):
        start = cusps[i]
        end = cusps[(i + 1) % 12]
        if start <= end:
            if start <= degree < end:
                return i + 1
        else:
            if degree >= start or degree < end:
                return i + 1
    return 1


def _get_sign_ruler(degree: float) -> str:
    sign_index = int(degree // 30) % 12
    rulers = ["火星", "金星", "水星", "月亮", "太阳", "水星",
              "金星", "火星", "木星", "土星", "土星", "木星"]
    return rulers[sign_index]


def analyze_daxian_limit(chart: Dict[str, Any], limit_index: int) -> Dict[str, Any]:
    if not chart.get('daxian') or limit_index < 0 or limit_index >= len(chart['daxian']):
        return {"error": "invalid limit_index"}

    limit_data = chart['daxian'][limit_index]
    start_deg = limit_data['start_degree']
    end_deg = limit_data['end_degree']

    cusps = chart.get('houses', {}).get('cusps', [])
    limit_house = _get_house_for_degree(cusps, start_deg) if cusps else None

    palace_lord = _get_sign_ruler(start_deg) if limit_house else None

    bodies = chart.get('bodies', {})
    stars_in_limit = [name for name, pos in bodies.items()
                      if isinstance(pos, (int, float)) and start_deg <= pos < end_deg]

    star_signs = chart.get('star_signs', {})
    shen_sha = star_signs.get('table', {}).get(str(limit_house), []) if limit_house else []

    result = {
        "limit_index": limit_index,
        "age_range": f"{limit_data['age_start']:.1f}-{limit_data['age_end']:.1f}",
        "degree_range": f"{start_deg:.1f}°-{end_deg:.1f}°",
        "house": limit_house,
        "palace_lord": palace_lord,
        "stars_in_limit": stars_in_limit,
        "shen_sha_in_house": shen_sha,
        "triggered_rules": [],
        "overall_judgment": "待AI综合判断"
    }
    return result


def progress_daxian_years(chart: Dict[str, Any], age_start: float, age_end: float) -> List[Dict[str, Any]]:
    return [{"age": age, "note": "叠加当前大限"} for age in range(int(age_start), int(age_end) + 1)]


def analyze_liunian(chart: Dict[str, Any], age: int) -> Dict[str, Any]:
    return {"age": age, "judgment": "待AI判断"}


def rectify_multi_point(birth_year: int, birth_month: int, birth_day: int,
                        targets: Dict[str, float], lon: float = 116.4, lat: float = 39.9) -> Dict[str, Any]:
    """
    多点矫正：输入多个目标黄经，返回一致性最高的出生时间。
    targets 示例：{"sun": 30.0, "jupiter": 120.0}
    """
    results = []
    for planet, target_lon in targets.items():
        try:
            found = core.find_date_at_planet_pos(
                birth_year, birth_month, birth_day,
                planet, target_lon, lon, lat
            )
            results.append({"planet": planet, "found_ut": found, "target": target_lon})
        except Exception as e:
            results.append({"planet": planet, "error": str(e)})

    # 简单一致性评分（占位）
    success_count = sum(1 for r in results if "found_ut" in r)
    consistency = success_count / len(targets) if targets else 0

    return {
        "results": results,
        "consistency_score": round(consistency, 2),
        "recommended_ut": results[0].get("found_ut") if results and "found_ut" in results[0] else None
    }
