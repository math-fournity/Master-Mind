#!/usr/bin/env python3
"""TODO 管理脚本：查询、更新、统计 TODO 状态。

数据源：dev-docs/todos.json（唯一真理源）
用法：
  python todo.py list                     # 列出所有 TODO
  python todo.py list --phase 13          # 列出指定 Phase
  python todo.py list --status pending    # 按状态过滤
  python todo.py list --search-preset 先搜索  # 按搜索预置过滤
  python todo.py show 13.1                # 查看单个 TODO
  python todo.py update 13.1 --status in_progress  # 更新状态
  python todo.py update 20.4 --status completed --result "PASS" --commit abc123
  python todo.py stats                    # 统计概览
  python todo.py stats --by-phase         # 按 Phase 统计
  python todo.py stats --by-search-preset # 按搜索预置统计
  python todo.py next                     # 下一个可执行的 TODO（pending + 依赖满足）
  python todo.py search-preset            # 列出所有需要搜索预置的 TODO
  python todo.py add --phase 99 --id 99.1 --title "新任务" --search-preset 先搜索
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

TODO_FILE = Path(__file__).parent / "dev-docs" / "todos.json"

VALID_STATUSES = ["pending", "in_progress", "completed", "blocked", "cancelled"]
VALID_SEARCH_PRESETS = ["先搜索", "边做边搜索", "不需要", "未评估"]


def load_todos():
    if not TODO_FILE.exists():
        print(f"错误：TODO 文件不存在：{TODO_FILE}", file=sys.stderr)
        sys.exit(1)
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(data):
    TODO_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def find_todo(data, todo_id):
    for todo in data["todos"]:
        if todo["id"] == todo_id:
            return todo
    return None


def parse_dependencies(dep_str):
    """解析依赖字符串，如 '13.1, Phase 13' → ['13.1', 'Phase 13']"""
    if not dep_str or dep_str.strip() == "—":
        return []
    return [d.strip() for d in dep_str.split(",")]


# ---------- 命令处理 ----------

def cmd_list(args):
    data = load_todos()
    todos = data["todos"]

    # 过滤
    if args.phase:
        todos = [t for t in todos if t["phase"] == args.phase]
    if args.status:
        todos = [t for t in todos if t["status"] == args.status]
    if args.search_preset:
        todos = [t for t in todos if t["search_preset"] == args.search_preset]
    if args.keyword:
        kw = args.keyword.lower()
        todos = [
            t for t in todos
            if kw in t["title"].lower() or kw in t.get("description", "").lower()
        ]

    if not todos:
        print("没有匹配的 TODO。")
        return

    # 输出
    if args.format == "json":
        print(json.dumps(todos, ensure_ascii=False, indent=2))
    else:
        print(f"共 {len(todos)} 个 TODO：\n")
        print(f"{'ID':<8} {'Phase':<6} {'状态':<12} {'搜索预置':<10} {'标题'}")
        print("-" * 100)
        for t in todos:
            status_icon = {
                "pending": "⬜",
                "in_progress": "🔄",
                "completed": "✅",
                "blocked": "🚫",
                "cancelled": "❌",
            }.get(t["status"], "?")
            print(f"{t['id']:<8} {t['phase']:<6} {status_icon} {t['status']:<10} {t['search_preset']:<10} {t['title']}")


def cmd_show(args):
    data = load_todos()
    todo = find_todo(data, args.todo_id)
    if not todo:
        print(f"错误：找不到 TODO {args.todo_id}", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(todo, ensure_ascii=False, indent=2))


def cmd_update(args):
    data = load_todos()
    todo = find_todo(data, args.todo_id)
    if not todo:
        print(f"错误：找不到 TODO {args.todo_id}", file=sys.stderr)
        sys.exit(1)

    changed = False
    if args.status:
        if args.status not in VALID_STATUSES:
            print(f"错误：无效状态 '{args.status}'，可选：{VALID_STATUSES}", file=sys.stderr)
            sys.exit(1)
        todo["status"] = args.status
        changed = True
    if args.result:
        todo["result"] = args.result
        changed = True
    if args.commit:
        todo["commit"] = args.commit
        changed = True
    if args.search_preset:
        if args.search_preset not in VALID_SEARCH_PRESETS:
            print(f"错误：无效搜索预置 '{args.search_preset}'，可选：{VALID_SEARCH_PRESETS}", file=sys.stderr)
            sys.exit(1)
        todo["search_preset"] = args.search_preset
        changed = True
    if args.note:
        todo.setdefault("notes", []).append({
            "date": datetime.now().isoformat(timespec="seconds"),
            "text": args.note,
        })
        changed = True

    if changed:
        todo["updated_at"] = datetime.now().isoformat(timespec="seconds")
        save_todos(data)
        print(f"已更新 TODO {args.todo_id}：{json.dumps({k: v for k, v in todo.items() if k in ['status', 'result', 'commit', 'search_preset', 'updated_at']}, ensure_ascii=False)}")
    else:
        print("没有指定要更新的字段。")


def cmd_stats(args):
    data = load_todos()
    todos = data["todos"]

    if args.by_phase:
        from collections import Counter
        phases = Counter()
        phase_status = {}
        for t in todos:
            p = t["phase"]
            phases[p] += 1
            phase_status.setdefault(p, Counter())[t["status"]] += 1

        print(f"{'Phase':<8} {'总数':<6} {'pending':<9} {'in_progress':<13} {'completed':<10} {'blocked':<8}")
        print("-" * 60)
        for p in sorted(phases.keys(), key=lambda x: int(x) if x.isdigit() else 999):
            s = phase_status[p]
            print(f"{p:<8} {phases[p]:<6} {s.get('pending',0):<9} {s.get('in_progress',0):<13} {s.get('completed',0):<10} {s.get('blocked',0):<8}")

    elif args.by_search_preset:
        from collections import Counter
        presets = Counter(t["search_preset"] for t in todos)
        total = len(todos)
        print(f"搜索预置统计（共 {total} 项）：\n")
        for preset in ["先搜索", "边做边搜索", "不需要", "未评估"]:
            count = presets.get(preset, 0)
            pct = count / total * 100 if total else 0
            bar = "█" * int(pct / 2)
            print(f"  {preset:<12} {count:>3}  ({pct:5.1f}%)  {bar}")

    else:
        from collections import Counter
        statuses = Counter(t["status"] for t in todos)
        total = len(todos)
        print(f"TODO 总览（共 {total} 项）：\n")
        for s in VALID_STATUSES:
            count = statuses.get(s, 0)
            pct = count / total * 100 if total else 0
            bar = "█" * int(pct / 2)
            print(f"  {s:<14} {count:>3}  ({pct:5.1f}%)  {bar}")

        # 搜索预置概要
        presets = Counter(t["search_preset"] for t in todos)
        print(f"\n搜索预置概要：")
        for preset in ["先搜索", "边做边搜索", "不需要", "未评估"]:
            count = presets.get(preset, 0)
            print(f"  {preset:<12} {count:>3}")


def cmd_next(args):
    """找下一个可执行的 TODO：pending + 依赖满足"""
    data = load_todos()
    todos = data["todos"]
    completed_ids = {t["id"] for t in todos if t["status"] == "completed"}

    candidates = []
    for t in todos:
        if t["status"] != "pending":
            continue
        deps = t.get("dependencies", [])
        # 解析依赖：支持 "13.1" 和 "Phase 13" 两种格式
        deps_met = True
        for dep in deps:
            dep = dep.strip()
            if dep.startswith("Phase "):
                phase_num = dep.replace("Phase ", "")
                # Phase 级依赖：该 Phase 所有 TODO 都 completed
                phase_todos = [x for x in todos if x["phase"] == phase_num]
                if phase_todos and not all(x["status"] == "completed" for x in phase_todos):
                    deps_met = False
                    break
            elif dep:
                # TODO 级依赖
                if dep not in completed_ids:
                    deps_met = False
                    break
        if deps_met:
            candidates.append(t)

    if not candidates:
        print("没有可执行的 TODO（所有 pending 项都有未满足的依赖）。")
        return

    # 按搜索预置排序：先搜索 > 边做边搜索 > 不需要
    priority = {"先搜索": 0, "边做边搜索": 1, "不需要": 2, "未评估": 3}
    candidates.sort(key=lambda t: (priority.get(t["search_preset"], 9), t["id"]))

    print(f"可执行的 TODO（pending + 依赖满足）共 {len(candidates)} 个：\n")
    for t in candidates[:10]:
        status_icon = "⬜"
        print(f"  {t['id']:<8} [{t['search_preset']}]  {t['title']}")
    if len(candidates) > 10:
        print(f"  ... 还有 {len(candidates) - 10} 个")


def cmd_search_preset(args):
    """列出所有需要搜索预置的 TODO"""
    data = load_todos()
    todos = data["todos"]

    if args.only == "先搜索":
        todos = [t for t in todos if t["search_preset"] == "先搜索"]
        print(f"需要先搜索的 TODO（共 {len(todos)} 项）：\n")
    elif args.only == "边做边搜索":
        todos = [t for t in todos if t["search_preset"] == "边做边搜索"]
        print(f"需要边做边搜索的 TODO（共 {len(todos)} 项）：\n")
    else:
        todos = [t for t in todos if t["search_preset"] in ("先搜索", "边做边搜索")]
        print(f"需要搜索预置的 TODO（共 {len(todos)} 项）：\n")

    for t in todos:
        icon = "🔍" if t["search_preset"] == "先搜索" else "🔄"
        sp_note = t.get("search_preset_note", "")
        print(f"  {icon} {t['id']:<8} [{t['phase']}]  {t['title']}")
        if sp_note:
            print(f"     → {sp_note}")
        print()


def cmd_add(args):
    data = load_todos()
    new_todo = {
        "id": args.id,
        "phase": str(args.phase),
        "title": args.title,
        "description": args.description or "",
        "dependencies": args.dependencies.split(",") if args.dependencies else [],
        "output": args.output or "",
        "validation": args.validation or "",
        "search_preset": args.search_preset or "未评估",
        "search_preset_note": args.search_note or "",
        "status": "pending",
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    data["todos"].append(new_todo)
    save_todos(data)
    print(f"已添加 TODO {args.id}: {args.title}")


def main():
    parser = argparse.ArgumentParser(description="TODO 管理脚本")
    sub = parser.add_subparsers(dest="command")

    # list
    p_list = sub.add_parser("list", help="列出 TODO")
    p_list.add_argument("--phase", help="按 Phase 过滤")
    p_list.add_argument("--status", help="按状态过滤")
    p_list.add_argument("--search-preset", dest="search_preset", help="按搜索预置过滤")
    p_list.add_argument("--keyword", help="关键词搜索")
    p_list.add_argument("--format", choices=["table", "json"], default="table")
    p_list.set_defaults(func=cmd_list)

    # show
    p_show = sub.add_parser("show", help="查看单个 TODO")
    p_show.add_argument("todo_id", help="TODO ID，如 13.1")
    p_show.set_defaults(func=cmd_show)

    # update
    p_update = sub.add_parser("update", help="更新 TODO 状态")
    p_update.add_argument("todo_id", help="TODO ID")
    p_update.add_argument("--status", choices=VALID_STATUSES)
    p_update.add_argument("--result", help="结果描述")
    p_update.add_argument("--commit", help="关联 commit hash")
    p_update.add_argument("--search-preset", dest="search_preset", choices=VALID_SEARCH_PRESETS)
    p_update.add_argument("--note", help="添加备注")
    p_update.set_defaults(func=cmd_update)

    # stats
    p_stats = sub.add_parser("stats", help="统计概览")
    p_stats.add_argument("--by-phase", action="store_true")
    p_stats.add_argument("--by-search-preset", action="store_true")
    p_stats.set_defaults(func=cmd_stats)

    # next
    p_next = sub.add_parser("next", help="下一个可执行的 TODO")
    p_next.set_defaults(func=cmd_next)

    # search-preset
    p_sp = sub.add_parser("search-preset", help="列出需要搜索预置的 TODO")
    p_sp.add_argument("--only", choices=["先搜索", "边做边搜索"], help="只看某一级")
    p_sp.set_defaults(func=cmd_search_preset)

    # add
    p_add = sub.add_parser("add", help="添加新 TODO")
    p_add.add_argument("--phase", type=int, required=True)
    p_add.add_argument("--id", required=True, help="TODO ID，如 99.1")
    p_add.add_argument("--title", required=True)
    p_add.add_argument("--description", default="")
    p_add.add_argument("--dependencies", default="", help="逗号分隔的依赖 ID")
    p_add.add_argument("--output", default="")
    p_add.add_argument("--validation", default="")
    p_add.add_argument("--search-preset", dest="search_preset", choices=VALID_SEARCH_PRESETS, default="未评估")
    p_add.add_argument("--search-note", default="")
    p_add.set_defaults(func=cmd_add)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
