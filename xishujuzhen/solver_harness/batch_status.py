#!/usr/bin/env python3
"""批次状态查询脚本——封装所有常用查询，避免每次现写脚本。

用法：
  python batch_status.py status [--batch-id ID]          # 批次总状态
  python batch_status.py active [--batch-id ID]          # running attempt活跃度详情
  python batch_status.py errors [--batch-id ID]          # 连接错误/token_limit/异常统计
  python batch_status.py solved [--batch-id ID]          # candidate_solved列表
  python batch_status.py feed [--batch-id ID]            # feed事件历史
  python batch_status.py all [--batch-id ID]             # 上述全部

不指定--batch-id时，自动选最新的running批次。
"""
import argparse
import os
import sys
from pathlib import Path

from arango import ArangoClient


def connect_db():
    host = os.environ.get("ARANGO_HOST", "http://localhost:8529")
    db_name = os.environ["ARANGO_DB"]
    user = os.environ.get("ARANGO_USER", "root")
    pwd = os.environ.get("ARANGO_PASS", "")
    c = ArangoClient(hosts=host)
    return c.db(db_name, username=user, password=pwd)


def latest_batch_id(db):
    """选最新的非completed批次。"""
    for b in db.aql.execute(
        'FOR b IN devin_batch_runs FILTER b.status != "completed" '
        'SORT b.created_at DESC LIMIT 1 RETURN b._key'
    ):
        return b
    # fallback: 最新的任意批次
    for b in db.aql.execute(
        'FOR b IN devin_batch_runs SORT b.created_at DESC LIMIT 1 RETURN b._key'
    ):
        return b
    return None


def cmd_status(db, batch_id):
    """批次总状态：按status分组计数 + 并发 + feed剩余。"""
    print(f"=== Batch: {batch_id} ===")
    batch = db.collection("devin_batch_runs").get(batch_id)
    if not batch:
        print(f"  NOT FOUND")
        return
    print(f"  concurrency: {batch.get('concurrency')}")
    print(f"  status: {batch.get('status')}")
    print(f"  created: {batch.get('created_at')}")

    print(f"\n  --- Attempt counts ---")
    total = 0
    for r in db.aql.execute(
        'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
        'COLLECT status=a.status WITH COUNT INTO cnt SORT cnt DESC '
        'RETURN {status, cnt}',
        bind_vars={"bid": batch_id},
    ):
        print(f"    {r['status']:25s}: {r['cnt']}")
        total += r["cnt"]
    print(f"    {'TOTAL':25s}: {total}")

    # feed剩余
    tier = (batch.get("selection") or {}).get("feed_tier", 1)
    remaining = db.aql.execute(
        'FOR p IN problem_extraction_progress FILTER p.difficulty_tier == @tier '
        'FILTER LENGTH(FOR r IN devin_problem_runs FILTER r.progress_key == p._key LIMIT 1 RETURN 1) == 0 '
        'COLLECT WITH COUNT INTO n RETURN n',
        bind_vars={"tier": tier},
    ).next()
    print(f"\n  --- Feed (tier={tier}) ---")
    print(f"    remaining unprocessed: {remaining}")


def cmd_active(db, batch_id):
    """running attempt活跃度详情：runtime/idle/thinking大小/markers。"""
    print(f"=== Active attempts: {batch_id} ===")
    active = 0
    stalled = 0
    for a in db.aql.execute(
        'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
        'FILTER a.status IN ["running", "stalled_warning"] '
        'SORT a.idle_seconds ASC '
        'RETURN {pid:a.problem_id, rt:a.runtime_seconds, idle:a.idle_seconds, '
        'sizes:a.observability.file_sizes, markers:a.observability.markers}',
        bind_vars={"bid": batch_id},
    ):
        s = a["sizes"]
        think_kb = s.get("thinking_readable_path", 0) // 1024
        pipe_kb = s.get("tmux_pipe_path", 0) // 1024
        export_kb = s.get("export_path", 0) // 1024
        markers = [k for k, v in a["markers"].items() if v]
        m_str = ",".join(markers) if markers else "-"
        status = "ACTIVE" if a["idle"] < 120 else "STALLED"
        if status == "ACTIVE":
            active += 1
        else:
            stalled += 1
        print(
            f"  {a['pid']:30s} rt={a['rt']:5d}s idle={a['idle']:4d}s "
            f"think={think_kb:5d}KB pipe={pipe_kb:3d}KB exp={export_kb:4d}KB "
            f"[{status}] {m_str}"
        )
    print(f"\n  active={active}, stalled={stalled}")


def cmd_errors(db, batch_id):
    """连接错误/token_limit/异常统计 + 抽样tmux_pipe内容。"""
    print(f"=== Error analysis: {batch_id} ===")

    # marker统计
    for marker in ["connection_error", "token_limited", "rate_limited", "answer_leak"]:
        cnt = db.aql.execute(
            'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
            'FILTER a.observability.markers.@marker == true '
            'COLLECT WITH COUNT INTO n RETURN n',
            bind_vars={"bid": batch_id, "marker": marker},
        ).next()
        if cnt > 0:
            print(f"  {marker}: {cnt} attempts")

    # failed_no_proof中实际是连接错误的
    print(f"\n  --- failed_no_proof breakdown (sampling tmux_pipe) ---")
    conn_err = 0
    token_lim = 0
    real_fail = 0
    other = 0
    for a in db.aql.execute(
        'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
        'FILTER a.status == "failed_no_proof" '
        'RETURN {pid:a.problem_id, paths:a.paths}',
        bind_vars={"bid": batch_id},
    ):
        pipe = Path(a["paths"]["tmux_pipe_path"])
        if not pipe.exists():
            other += 1
            continue
        content = pipe.read_text()
        if "Connection error" in content or "cognition.ai/errorKind" in content or "unavailable" in content:
            conn_err += 1
        elif "token limit" in content.lower() or "truncated" in content.lower():
            token_lim += 1
        elif len(content.strip()) > 100:
            real_fail += 1
        else:
            other += 1
    print(f"    connection_error: {conn_err}")
    print(f"    token_limit: {token_lim}")
    print(f"    real_no_proof (has thinking but no proof): {real_fail}")
    print(f"    other (empty/missing): {other}")


def cmd_solved(db, batch_id):
    """candidate_solved列表。"""
    print(f"=== Solved: {batch_id} ===")
    count = 0
    for a in db.aql.execute(
        'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
        'FILTER a.status == "candidate_solved" '
        'SORT a.runtime_seconds ASC '
        'RETURN {pid:a.problem_id, rt:a.runtime_seconds, think:a.observability.file_sizes.thinking_readable_path}',
        bind_vars={"bid": batch_id},
    ):
        think_kb = (a["think"] or 0) // 1024
        print(f"  {a['pid']:30s} rt={a['rt']:5d}s think={think_kb:5d}KB")
        count += 1
    print(f"  total solved: {count}")


def cmd_feed(db, batch_id):
    """feed事件历史。"""
    print(f"=== Feed events: {batch_id} ===")
    for e in db.aql.execute(
        'FOR e IN devin_run_events FILTER e.batch_id == @bid '
        'FILTER e.event_type IN ["cases_added", "concurrency_changed", "feed_exhausted"] '
        'SORT e.timestamp ASC RETURN e',
        bind_vars={"bid": batch_id},
    ):
        print(f"  {e['timestamp']}: {e['event_type']} {e.get('details', {})}")


def main():
    parser = argparse.ArgumentParser(description="Batch status query tool")
    parser.add_argument("cmd", choices=["status", "active", "errors", "solved", "feed", "all"])
    parser.add_argument("--batch-id", help="batch id (default: latest running)")
    args = parser.parse_args()

    db = connect_db()
    batch_id = args.batch_id or latest_batch_id(db)
    if not batch_id:
        print("No batch found", file=sys.stderr)
        sys.exit(1)
    if not args.batch_id:
        print(f"(auto-selected batch: {batch_id})\n")

    if args.cmd in ("status", "all"):
        cmd_status(db, batch_id)
        print()
    if args.cmd in ("active", "all"):
        cmd_active(db, batch_id)
        print()
    if args.cmd in ("errors", "all"):
        cmd_errors(db, batch_id)
        print()
    if args.cmd in ("solved", "all"):
        cmd_solved(db, batch_id)
        print()
    if args.cmd in ("feed", "all"):
        cmd_feed(db, batch_id)
        print()


if __name__ == "__main__":
    main()
