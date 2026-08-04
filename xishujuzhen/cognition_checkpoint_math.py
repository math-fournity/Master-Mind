#!/usr/bin/env python3
"""cognition_checkpoint_math.py —— CP1-CP6工作流入口

AI在工作流中通过此脚本执行CP1-CP6。

使用方式：
  # CP1+CP2+CP3: 工作开始前
  .venv/bin/python3 xishujuzhen/cognition_checkpoint_math.py start --seeds cog1,cog2

  # CP4+CP5+CP6: 工作结束时
  .venv/bin/python3 xishujuzhen/cognition_checkpoint_math.py end \
      --task "任务描述" --seeds cog1,cog2 --loaded cog1,cog2,cog3 \
      --new_version cog_id:v2:99:版本摘要 \
      --new_edge from_cog:to_cog:depends_on

  # 查询命令
  .venv/bin/python3 xishujuzhen/cognition_checkpoint_math.py stats
  .venv/bin/python3 xishujuzhen/cognition_checkpoint_math.py list --category core
  .venv/bin/python3 xishujuzhen/cognition_checkpoint_math.py versions --cog_id seven_step_workflow
  .venv/bin/python3 xishujuzhen/cognition_checkpoint_math.py deps --cog_id seven_step_workflow --reverse
"""
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from cognition_sdk_math import CognitionSDK


def cmd_start(args, sdk):
    """CP1+CP2+CP3: 工作开始前"""
    seeds = args.seeds.split(",")

    # CP1: 种子选择
    print("=" * 60)
    print("CP1: 种子选择")
    print("=" * 60)
    print(f"种子认知单元: {seeds}")

    # CP2: 认知加载（AQL图遍历）
    print("\n" + "=" * 60)
    print("CP2: 认知加载（图遍历）")
    print("=" * 60)
    task_cogs = sdk.traverse(seeds, max_depth=args.max_depth)
    for c in task_cogs:
        depth = c.get("depth", 0)
        indent = "  " * depth
        seed_mark = " [种子]" if c.get("is_seed") else ""
        print(f"{indent}[{c['cog_id']}] {c['title']}{seed_mark}")
        kc = c.get("key_cognition", "")
        if kc:
            print(f"{indent}  {kc[:80]}...")

    # CP3: 缺口检查
    print("\n" + "=" * 60)
    print("CP3: 缺口检查")
    print("=" * 60)
    loaded = set(seeds)
    discovered = [c for c in task_cogs if c.get("cog_id") not in loaded]
    print(f"图遍历发现 {len(discovered)} 个额外认知单元（种子之外的）")
    print(f"\n提醒：图遍历可能遗漏与种子无依赖边但任务相关的认知单元。")
    print(f"请自检是否有遗漏的认知。")


def cmd_end(args, sdk):
    """CP4+CP5+CP6: 工作结束时"""
    seeds = args.seeds.split(",") if args.seeds else []
    loaded = args.loaded.split(",") if args.loaded else []

    # CP4: 认知捕获
    print("=" * 60)
    print("CP4: 认知捕获")
    print("=" * 60)
    print("请检查本次工作是否产生新的工作意识：")
    print("  - 新的方法论？→ 落盘到dev-docs，创建新认知单元或新版本")
    print("  - 新的依赖关系？→ 加入cog_edges")
    print("  - 对已有认知的修正？→ 创建新版本到版本链")
    print("  - 新的术语？→ 追加到工作系统词汇表")
    print("  - 临场脚本？→ 检查是否应沉淀到cognition_sdk_math.py")

    # CP5: 认知图更新
    print("\n" + "=" * 60)
    print("CP5: 认知图更新")
    print("=" * 60)
    if args.new_version:
        for nv in args.new_version:
            parts = nv.split(":")
            if len(parts) >= 4:
                cog_id, version, doc, summary = parts[0], parts[1], parts[2], parts[3]
                sdk.add_version(cog_id, version, doc, summary)
                print(f"  ✅ 新版本: {cog_id} {version} (doc={doc})")
            else:
                print(f"  ⚠️  格式错误: {nv}（应为cog_id:version:doc:summary）")

    if args.new_edge:
        for ne in args.new_edge:
            parts = ne.split(":")
            if len(parts) == 3:
                from_cog, to_cog, edge_type = parts
                sdk.add_edge(from_cog, to_cog, edge_type)
                print(f"  ✅ 新边: {from_cog} → {to_cog} ({edge_type})")
            else:
                print(f"  ⚠️  格式错误: {ne}（应为from:to:type）")

    # CP6: 任务-认知映射
    print("\n" + "=" * 60)
    print("CP6: 任务-认知映射")
    print("=" * 60)
    if args.task and seeds:
        sdk.record_task(args.task, seeds, loaded)


def cmd_stats(args, sdk):
    stats = sdk.get_stats()
    print(f"认知单元: {stats['total_units']}个")
    print(f"  分类: {stats['categories']}")
    print(f"  状态: {stats['statuses']}")
    print(f"边: {stats['total_edges']}条")
    print(f"版本: {stats['total_versions']}条")


def cmd_list(args, sdk):
    units = sdk.list_units(category=args.category)
    for u in units:
        print(f"[{u['cog_id']}] {u['title']} ({u['category']}, {u['current_version']})")
        print(f"  {u.get('key_cognition', '')[:80]}")


def cmd_versions(args, sdk):
    versions = sdk.get_versions(args.cog_id)
    for v in versions:
        print(f"  {v['version']} (order={v.get('version_order')}, doc={v.get('doc')}): {v.get('summary', '')}")


def cmd_deps(args, sdk):
    deps = sdk.get_deps(args.cog_id, reverse=args.reverse)
    direction = "反向依赖（谁依赖它）" if args.reverse else "直接依赖"
    print(f"{args.cog_id} 的{direction}:")
    for d in deps:
        print(f"  [{d['edge_type']}] → {d['cog_id']}: {d['title']}")


def main():
    parser = argparse.ArgumentParser(description="认知检查点工具（CP1-CP6）")
    sub = parser.add_subparsers(dest="command")

    p_start = sub.add_parser("start", help="CP1+CP2+CP3: 工作开始前")
    p_start.add_argument("--seeds", required=True, help="种子认知单元ID，逗号分隔")
    p_start.add_argument("--max_depth", type=int, default=7)

    p_end = sub.add_parser("end", help="CP4+CP5+CP6: 工作结束时")
    p_end.add_argument("--task", help="任务描述")
    p_end.add_argument("--seeds", help="种子认知单元ID，逗号分隔")
    p_end.add_argument("--loaded", help="实际加载的认知单元ID，逗号分隔")
    p_end.add_argument("--new_version", action="append", help="新版本，格式cog_id:version:doc:summary")
    p_end.add_argument("--new_edge", action="append", help="新边，格式from:to:type")

    sub.add_parser("stats", help="认知图统计")
    p_list = sub.add_parser("list", help="列出认知单元")
    p_list.add_argument("--category", choices=["core", "process", "support", "awareness"])
    p_versions = sub.add_parser("versions", help="版本链")
    p_versions.add_argument("--cog_id", required=True)
    p_deps = sub.add_parser("deps", help="依赖")
    p_deps.add_argument("--cog_id", required=True)
    p_deps.add_argument("--reverse", action="store_true")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    sdk = CognitionSDK()

    if args.command == "start":
        cmd_start(args, sdk)
    elif args.command == "end":
        cmd_end(args, sdk)
    elif args.command == "stats":
        cmd_stats(args, sdk)
    elif args.command == "list":
        cmd_list(args, sdk)
    elif args.command == "versions":
        cmd_versions(args, sdk)
    elif args.command == "deps":
        cmd_deps(args, sdk)


if __name__ == "__main__":
    main()
