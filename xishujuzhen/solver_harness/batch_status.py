#!/usr/bin/env python3
"""批次状态查询脚本——封装所有常用查询，避免每次现写脚本。

用法：
  python batch_status.py status [--batch-id ID]          # 批次总状态
  python batch_status.py active [--batch-id ID]          # running attempt活跃度详情
  python batch_status.py errors [--batch-id ID]          # 连接错误/token_limit/异常统计
  python batch_status.py solved [--batch-id ID]          # candidate_solved列表
  python batch_status.py feed [--batch-id ID]            # feed事件历史
  python batch_status.py leak [--batch-id ID]            # 答案泄漏检查（DB marker + tmux_pipe扫描）
  python batch_status.py dead [--batch-id ID]            # 僵尸session检测（tmux pane空白+Devin CLI已退出）
  python batch_status.py all [--batch-id ID]             # 上述全部

不指定--batch-id时，自动选最新的running批次。
"""
import argparse
import os
import subprocess
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
        status = "ACTIVE" if (a["idle"] or 0) < 120 else "STALLED"
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


def cmd_leak(db, batch_id):
    """答案泄漏检查：DB marker + tmux_pipe/export文件扫描。

    检查三个层面：
    1. DB中answer_leak marker（Solver输出### ANSWER LEAK DETECTED时monitor设的）
    2. tmux_pipe.log中的### ANSWER LEAK DETECTED（直接扫描，不依赖marker）
    3. export/conversation.json中的ANSWER LEAK DETECTED（区分指令文本 vs 真报错）
    """
    print(f"=== Answer leak check: {batch_id} ===")

    # 1. DB marker
    cnt = db.aql.execute(
        'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
        'FILTER a.observability.markers.answer_leak == true '
        'COLLECT WITH COUNT INTO n RETURN n',
        bind_vars={"bid": batch_id},
    ).next()
    print(f"  DB answer_leak marker: {cnt}")

    if cnt > 0:
        for a in db.aql.execute(
            'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
            'FILTER a.observability.markers.answer_leak == true '
            'RETURN {pid:a.problem_id, status:a.status, paths:a.paths}',
            bind_vars={"bid": batch_id},
        ):
            print(f"    {a['pid']}: status={a['status']}")

    # 2. 扫描tmux_pipe.log中的真实报错（排除AGENTS.md指令文本）
    print(f"\n  --- tmux_pipe.log scan (real reports only) ---")
    real_leaks = 0
    instruction_matches = 0
    for a in db.aql.execute(
        'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
        'RETURN {pid:a.problem_id, paths:a.paths}',
        bind_vars={"bid": batch_id},
    ):
        pipe_path = Path(a["paths"]["tmux_pipe_path"])
        if not pipe_path.exists():
            continue
        content = pipe_path.read_text()
        if "ANSWER LEAK DETECTED" not in content:
            continue
        # 区分：指令文本中是"### ANSWER LEAK DETECTED: <brief description>"
        # 真报错是"### ANSWER LEAK DETECTED: <具体描述>"（没有<brief>占位符）
        for line in content.split("\n"):
            if "ANSWER LEAK DETECTED" in line:
                if "<brief description>" in line or "Instead output exactly" in line:
                    instruction_matches += 1
                else:
                    real_leaks += 1
                    print(f"    REAL LEAK: {a['pid']} -> {line.strip()[:100]}")

    print(f"    instruction_text_matches: {instruction_matches} (AGENTS.md指令被记录，正常)")
    print(f"    real_leak_reports: {real_leaks}")

    # 3. 全局grep export文件（跨批次，检查是否有遗漏）
    print(f"\n  --- global export scan (all batches) ---")
    result = subprocess.run(
        ["grep", "-r", "-l", "ANSWER LEAK DETECTED",
         "/data/math-agent-glm5.2-tmux-agents-trajectory/"],
        capture_output=True, text=True, timeout=60,
    )
    export_files = [f for f in result.stdout.strip().split("\n") if f]
    print(f"    files containing 'ANSWER LEAK DETECTED': {len(export_files)}")
    for f in export_files[:5]:
        # 检查是指令文本还是真报错
        try:
            import json as _json
            d = _json.load(open(f))
            found_real = False
            def _scan(obj):
                nonlocal found_real
                if isinstance(obj, str) and "ANSWER LEAK DETECTED" in obj:
                    if "<brief description>" not in obj and "Instead output exactly" not in obj:
                        found_real = True
                elif isinstance(obj, dict):
                    for v in obj.values():
                        _scan(v)
                elif isinstance(obj, list):
                    for v in obj:
                        _scan(v)
            _scan(d)
            tag = "REAL" if found_real else "instruction_only"
        except Exception:
            tag = "?"
        print(f"    [{tag}] {Path(f).parent.name}")

    if real_leaks == 0 and cnt == 0:
        print(f"\n  RESULT: No answer leaks detected.")


def cmd_dead(db, batch_id):
    """僵尸session检测：tmux session还在但Devin CLI已退出（pane空白）。

    检测逻辑：
    1. 找所有running/stalled_warning的attempt
    2. 检查tmux pane内容——空白=Devin CLI已退出
    3. 检查tmux_pipe.log——有没有PROOF COMPLETE（已完成但monitor没判定）
    4. 检查thinking_readable_path——有没有实际产出

    输出分类：
    - DEAD: pane空白，无PROOF COMPLETE，无thinking → 僵尸session
    - PROOF_MISSED: pane空白但有PROOF COMPLETE → 已完成但monitor没判定
    - CONN_DEAD: pane空白，pipe有Connection error → 连接错误导致退出
    - ALIVE: pane有内容 → 正常运行
    """
    print(f"=== Dead session check: {batch_id} ===")

    dead = 0
    proof_missed = 0
    conn_dead = 0
    alive = 0

    for a in db.aql.execute(
        'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
        'FILTER a.status IN ["running", "stalled_warning"] '
        'RETURN {key:a._key, pid:a.problem_id, tmux:a.tmux_session, '
        'paths:a.paths, rt:a.runtime_seconds}',
        bind_vars={"bid": batch_id},
    ):
        tmux = a["tmux"]
        # 检查tmux session是否存在
        r = subprocess.run(
            ["tmux", "has-session", "-t", tmux],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
        )
        if r.returncode != 0:
            # tmux session已消失但DB还显示running——也是僵尸
            pipe = Path(a["paths"]["tmux_pipe_path"])
            pipe_text = pipe.read_text() if pipe.exists() else ""
            if "### PROOF COMPLETE" in pipe_text:
                proof_missed += 1
                print(f"  [PROOF_MISSED] {a['pid']:25s} rt={a['rt']}s (tmux gone, proof in pipe)")
            else:
                dead += 1
                print(f"  [DEAD] {a['pid']:25s} rt={a['rt']}s (tmux session gone)")
            continue

        # 捕获pane内容
        r = subprocess.run(
            ["tmux", "capture-pane", "-t", tmux, "-p"],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False, timeout=10,
        )
        content = r.stdout.decode("utf-8", errors="ignore")
        stripped = "\n".join(line.strip() for line in content.split("\n") if line.strip())

        if len(stripped) < 5:
            # pane空白——Devin CLI已退出
            pipe = Path(a["paths"]["tmux_pipe_path"])
            pipe_text = pipe.read_text() if pipe.exists() else ""
            think_size = Path(a["paths"]["thinking_readable_path"]).stat().st_size if Path(a["paths"]["thinking_readable_path"]).exists() else 0

            if "### PROOF COMPLETE" in pipe_text:
                proof_missed += 1
                print(f"  [PROOF_MISSED] {a['pid']:25s} rt={a['rt']}s think={think_size//1024}KB (pane empty, proof in pipe)")
            elif "Connection error" in pipe_text or "unavailable" in pipe_text or "cognition.ai" in pipe_text:
                conn_dead += 1
                print(f"  [CONN_DEAD] {a['pid']:25s} rt={a['rt']}s think={think_size//1024}KB (pane empty, connection error)")
            else:
                dead += 1
                print(f"  [DEAD] {a['pid']:25s} rt={a['rt']}s think={think_size//1024}KB (pane empty, no output)")
        else:
            alive += 1

    print(f"\n  DEAD={dead}  PROOF_MISSED={proof_missed}  CONN_DEAD={conn_dead}  ALIVE={alive}")

    if dead + proof_missed + conn_dead > 0:
        print(f"\n  ACTION NEEDED: {dead + proof_missed + conn_dead} zombie sessions need cleanup.")
        print(f"  Run with --cleanup to auto-fix (kill tmux + update DB status).")
    else:
        print(f"\n  RESULT: No zombie sessions.")


def cmd_dead_cleanup(db, batch_id):
    """僵尸session自动清理：kill tmux + 更新DB状态。"""
    from datetime import datetime, timezone
    print(f"=== Dead session cleanup: {batch_id} ===")
    now = datetime.now(timezone.utc).isoformat()
    cleaned = 0

    for a in db.aql.execute(
        'FOR a IN devin_problem_runs FILTER a.batch_id == @bid '
        'FILTER a.status IN ["running", "stalled_warning"] '
        'RETURN {key:a._key, pid:a.problem_id, tmux:a.tmux_session, paths:a.paths}',
        bind_vars={"bid": batch_id},
    ):
        tmux = a["tmux"]
        r = subprocess.run(
            ["tmux", "has-session", "-t", tmux],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
        )
        if r.returncode != 0:
            # tmux已消失
            pipe = Path(a["paths"]["tmux_pipe_path"])
            pipe_text = pipe.read_text() if pipe.exists() else ""
            if "### PROOF COMPLETE" in pipe_text:
                status = "candidate_solved"
            elif "Connection error" in pipe_text or "unavailable" in pipe_text:
                status = "failed_connection"
            else:
                status = "dead_session"
            db.collection("devin_problem_runs").update({
                "_key": a["key"], "status": status,
                "ended_at": now, "end_reason": "auto_cleanup_zombie",
            })
            print(f"  [{status}] {a['pid']}")
            cleaned += 1
            continue

        r = subprocess.run(
            ["tmux", "capture-pane", "-t", tmux, "-p"],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False, timeout=10,
        )
        content = r.stdout.decode("utf-8", errors="ignore")
        stripped = "\n".join(line.strip() for line in content.split("\n") if line.strip())

        if len(stripped) < 5:
            subprocess.run(["tmux", "kill-session", "-t", tmux],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
            pipe = Path(a["paths"]["tmux_pipe_path"])
            pipe_text = pipe.read_text() if pipe.exists() else ""
            if "### PROOF COMPLETE" in pipe_text:
                status = "candidate_solved"
            elif "Connection error" in pipe_text or "unavailable" in pipe_text:
                status = "failed_connection"
            else:
                status = "dead_session"
            db.collection("devin_problem_runs").update({
                "_key": a["key"], "status": status,
                "ended_at": now, "end_reason": "auto_cleanup_zombie",
            })
            print(f"  [{status}] {a['pid']}")
            cleaned += 1

    print(f"\n  cleaned: {cleaned}")


def main():
    parser = argparse.ArgumentParser(description="Batch status query tool")
    parser.add_argument("cmd", choices=["status", "active", "errors", "solved", "feed", "leak", "dead", "all"])
    parser.add_argument("--batch-id", help="batch id (default: latest running)")
    parser.add_argument("--cleanup", action="store_true", help="auto-fix zombie sessions (for dead command)")
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
    if args.cmd in ("leak", "all"):
        cmd_leak(db, batch_id)
        print()
    if args.cmd == "dead":
        if args.cleanup:
            cmd_dead_cleanup(db, batch_id)
        else:
            cmd_dead(db, batch_id)
        print()


if __name__ == "__main__":
    main()
