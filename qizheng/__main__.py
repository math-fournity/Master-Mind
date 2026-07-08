"""七政四余推命系统 CLI 主入口。

用法:
    python -m qizheng 1990 5 15 3.5 116.4 39.9
    python -m qizheng 1990 5 15 3.5 116.4 39.9 --json
    python -m qizheng 1990 5 15 3.5 116.4 39.9 --verbose
    python -m qizheng 1990 5 15 3.5 116.4 39.9 --json --output chart.json

参数:
    year month day hour_ut longitude latitude
    hour_ut: UT 小时（如 3.5 = 3:30 UT）
    longitude/latitude: 地理经纬度（东经北纬为正）

选项:
    --json          输出 JSON 格式
    --verbose       显示神煞明细
    --output FILE   输出到文件
    --quiet         只输出匹配格局（不显示命盘）
"""
import argparse
import sys

from qizheng.chart import build_chart
from qizheng.render import render_chart, export_json


def main():
    parser = argparse.ArgumentParser(
        prog="qizheng",
        description="七政四余推命系统 — 排盘/神煞/格局/限运/流年",
    )
    parser.add_argument("year", type=int, help="出生年（公历）")
    parser.add_argument("month", type=int, help="出生月（公历，1-12）")
    parser.add_argument("day", type=int, help="出生日（公历）")
    parser.add_argument("hour", type=float, help="出生时间（UT 小时，如 3.5=3:30）")
    parser.add_argument("longitude", type=float, help="地理经度（东经为正）")
    parser.add_argument("latitude", type=float, help="地理纬度（北纬为正）")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式")
    parser.add_argument("--svg", action="store_true", help="输出 SVG 图形命盘")
    parser.add_argument("--verbose", action="store_true", help="显示神煞明细")
    parser.add_argument("--output", "-o", type=str, help="输出到文件")
    parser.add_argument("--quiet", action="store_true", help="只输出匹配格局")

    args = parser.parse_args()

    # 构建命盘
    try:
        chart = build_chart(
            args.year, args.month, args.day, args.hour,
            args.longitude, args.latitude,
        )
    except Exception as e:
        print(f"排盘失败: {e}", file=sys.stderr)
        sys.exit(1)

    # 输出
    if args.json:
        output = export_json(chart, pretty=True)
    elif args.svg:
        from qizheng.svg_chart import render_svg
        output = render_svg(chart)
    elif args.quiet:
        rules = chart.get("rules", {})
        matched = rules.get("matched", []) if isinstance(rules, dict) else []
        lines = []
        for r in matched:
            lines.append(f"[{r['id']}] {r['name']}")
            if r.get("comment"):
                lines.append(f"    {r['comment']}")
        output = "\n".join(lines) if lines else "（无匹配格局）"
    else:
        output = render_chart(chart, verbose=args.verbose)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"已输出到 {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
