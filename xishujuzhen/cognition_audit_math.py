#!/usr/bin/env python3
"""cognition_audit_math.py —— 审计CLI

一键执行认知图的各项审计和修复。

命令：
  all                 一键全量审计
  version-chain       D3版本链审计
  graph-completeness  D4图遍历完整性审计
  coverage            D1覆盖率审计
  poc-regression      POC回归综合评分（D1-D5）
  topology            拓扑覆盖验证（调用TopologyVerifier）
  fix-version-order   修复version_order
  stats               统计
  list                列出认知单元
  versions            版本链
  deps                依赖
"""
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from cognition_sdk_math import CognitionSDK


def cmd_all(args, sdk):
    result = sdk.audit_all(
        seeds=args.seeds.split(",") if args.seeds else None,
        ground_truth=args.ground_truth.split(",") if args.ground_truth else None,
    )
    for key, val in result.items():
        print(f"\n{key}:")
        if isinstance(val, dict):
            for k, v in val.items():
                print(f"  {k}: {v}")


def cmd_version_chain(args, sdk):
    r = sdk.audit_version_chain()
    print(f"版本链审计: {r['correct']}/{r['total']} 正确, 得分={r['score']}/20")
    for e in r["errors"]:
        print(f"  ❌ {e['cog_id']}: current={e.get('current')}, latest={e.get('latest')}")


def cmd_graph_completeness(args, sdk):
    seeds = args.seeds.split(",")
    r = sdk.audit_graph_completeness(seeds)
    print(f"图遍历完整性: depth=5找到{r['default_count']}个, depth=7找到{r['max_count']}个, 得分={r['score']}/20")
    if r["missing"]:
        print(f"  遗漏: {r['missing']}")


def cmd_coverage(args, sdk):
    seeds = args.seeds.split(",")
    gt = args.ground_truth.split(",")
    found = {c["cog_id"] for c in sdk.traverse(seeds)}
    r = sdk.audit_coverage(list(found), gt)
    print(f"覆盖率: {r['found_count']}/{r['gt_count']} = {r['coverage_rate']:.1%}, 得分={r['score']}/20")
    if r["missing"]:
        print(f"  遗漏: {r['missing']}")


def cmd_poc_regression(args, sdk):
    seeds = args.seeds.split(",")
    gt = args.ground_truth.split(",")
    r = sdk.audit_poc_regression(seeds, gt)
    print(f"POC回归综合评分: {r['total_score']}/{r['max_score']}")
    for key in ["D1_coverage", "D3_version_chain", "D4_graph_completeness",
                "D2_constraints", "D5_executability"]:
        v = r[key]
        print(f"  {key}: score={v['score']}")


def cmd_topology(args, sdk):
    report = sdk.audit_topology_coverage()
    print(report.summary())


def cmd_fix_version_order(args, sdk):
    r = sdk.fix_version_order()
    print(f"修复 {r['fixed']} 条版本记录的version_order")


def cmd_stats(args, sdk):
    stats = sdk.get_stats()
    print(f"认知单元: {stats['total_units']}个")
    print(f"  分类: {stats['categories']}")
    print(f"边: {stats['total_edges']}条")
    print(f"版本: {stats['total_versions']}条")


def cmd_list(args, sdk):
    units = sdk.list_units(category=args.category)
    for u in units:
        print(f"[{u['cog_id']}] {u['title']} ({u['category']}, {u['current_version']})")


def cmd_versions(args, sdk):
    versions = sdk.get_versions(args.cog_id)
    for v in versions:
        print(f"  {v['version']} (order={v.get('version_order')}, doc={v.get('doc')}): {v.get('summary', '')}")


def cmd_deps(args, sdk):
    deps = sdk.get_deps(args.cog_id, reverse=args.reverse)
    direction = "反向依赖" if args.reverse else "直接依赖"
    print(f"{args.cog_id} 的{direction}:")
    for d in deps:
        print(f"  [{d['edge_type']}] → {d['cog_id']}: {d['title']}")


def main():
    parser = argparse.ArgumentParser(description="认知图审计CLI")
    sub = parser.add_subparsers(dest="command")

    p_all = sub.add_parser("all", help="一键全量审计")
    p_all.add_argument("--seeds")
    p_all.add_argument("--ground-truth")

    sub.add_parser("version-chain", help="D3版本链审计")

    p_gc = sub.add_parser("graph-completeness", help="D4图遍历完整性")
    p_gc.add_argument("--seeds", required=True)

    p_cov = sub.add_parser("coverage", help="D1覆盖率")
    p_cov.add_argument("--seeds", required=True)
    p_cov.add_argument("--ground-truth", required=True)

    p_pr = sub.add_parser("poc-regression", help="POC回归综合评分")
    p_pr.add_argument("--seeds", required=True)
    p_pr.add_argument("--ground-truth", required=True)

    sub.add_parser("topology", help="拓扑覆盖验证（TopologyVerifier）")
    sub.add_parser("fix-version-order", help="修复version_order")
    sub.add_parser("stats", help="统计")

    p_list = sub.add_parser("list", help="列出认知单元")
    p_list.add_argument("--category", choices=["core", "process", "support", "awareness"])

    p_ver = sub.add_parser("versions", help="版本链")
    p_ver.add_argument("--cog_id", required=True)

    p_deps = sub.add_parser("deps", help="依赖")
    p_deps.add_argument("--cog_id", required=True)
    p_deps.add_argument("--reverse", action="store_true")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    sdk = CognitionSDK()

    commands = {
        "all": cmd_all,
        "version-chain": cmd_version_chain,
        "graph-completeness": cmd_graph_completeness,
        "coverage": cmd_coverage,
        "poc-regression": cmd_poc_regression,
        "topology": cmd_topology,
        "fix-version-order": cmd_fix_version_order,
        "stats": cmd_stats,
        "list": cmd_list,
        "versions": cmd_versions,
        "deps": cmd_deps,
    }
    commands[args.command](args, sdk)


if __name__ == "__main__":
    main()
