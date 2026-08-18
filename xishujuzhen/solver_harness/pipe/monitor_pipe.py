#!/usr/bin/env python3
"""monitor_pipe.py — 解题系统Monitor Pipe（持续监控+alert+AI review抽样）

参考错题分析系统的monitor_pipe.py架构，适配解题系统（pipe/5服务）的已知问题。

两类检查：
  A. 自动检查（脚本判定对错，写alert到ArangoDB）：
     - session_health: harness-p session数 vs Redis running vs 设定并发
     - queue_progress: pending是否在减少，completed是否在增加（stall检测）
     - rate_limit_detection: 最近N分钟是否有rate_limited（解题系统核心问题）
     - zombie_sessions: 空pane僵尸session（解题系统已知问题）
     - export_landing: 最近completed的题是否有export文件
     - solve_time_credibility: solve_time > runtime的比例
     - failure_rate: 失败率（按status分类）
     - throughput_trend: 吞吐趋势（对比前后轮次）

  B. AI review抽样（标记需AI判断的）：
     - 每3轮抽样2条candidate_solved，标记为needs_ai_review
     - AI检查：proof是否正确、是否有幻觉、是否答案泄漏

alert结构：
  {
    _key: "pmon-{timestamp}-{type}",
    alert_type: "session_health" | "queue_progress" | ...,
    severity: "critical" | "warning" | "info",
    details: {...},
    status: "new" | "reviewing" | "fixed" | "wontfix",
    created_at: timestamp,
    resolved_at: null
  }

用法：
  python monitor_pipe.py --interval 300                   # 启动监控循环（5分钟一轮）
  python monitor_pipe.py --check-alerts                   # 查看新alerts
  python monitor_pipe.py --resolve-alert <alert_key>      # 标记alert已解决
  python monitor_pipe.py --once                           # 只跑一轮（不循环）
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))

from redis_queue import get_redis, pending_count, running_count, completed_count, failed_count
from shared_logger import get_logger
from collector import find_ai_proof_marker

logger = get_logger("monitor")

MONITOR_ALERTS_COLLECTION = "pipe_monitor_alerts"
ATTEMPT_COLLECTION = "devin_problem_runs"

TRAJ_BASE = Path("/data/math-agent-glm5.2-tmux-agents-trajectory")

# 检查阈值
RATE_LIMIT_THRESHOLD = 3          # 最近interval内rate_limited>=3个 alert
FAILURE_RATE_THRESHOLD = 0.15     # 失败率>15% alert（解题系统容忍度比审计系统高）
STALL_THRESHOLD_SECONDS = 900     # 15分钟无进度 alert（解题系统单题耗时更长）
SOLVE_TIME_ANOMALY_THRESHOLD = 0.10  # solve_time>runtime比例>10% alert
ZOMBIE_THRESHOLD = 2              # 僵尸session>=2个 alert
EXPORT_MISSING_THRESHOLD = 0.10   # export缺失率>10% alert
SAMPLE_SIZE = 2                   # 每轮抽样2条需AI review


def _utc_now():
    return datetime.now(timezone.utc).isoformat()


def _ts():
    return int(time.time())


def _connect_db():
    from arango import ArangoClient
    host = os.environ.get("ARANGO_HOST", "http://localhost:8529")
    client = ArangoClient(hosts=host, request_timeout=300)
    db_name = os.environ.get("ARANGO_DB", "xishujuzhen_math_glm52")
    db = client.db(db_name, username=os.environ.get("ARANGO_USER", "root"),
                   password=os.environ.get("ARANGO_PASS", ""))
    return db


# ============================================================
# Alert管理
# ============================================================

def ensure_monitor_collections(db):
    if not db.has_collection(MONITOR_ALERTS_COLLECTION):
        db.create_collection(MONITOR_ALERTS_COLLECTION)


def create_alert(db, alert_type, severity, details):
    now = _utc_now()
    ts = int(time.time() * 1000)
    alert_key = f"pmon-{ts}-{alert_type}"
    doc = {
        "_key": alert_key,
        "alert_type": alert_type,
        "severity": severity,
        "details": details,
        "status": "new",
        "created_at": now,
        "resolved_at": None,
    }
    try:
        db.collection(MONITOR_ALERTS_COLLECTION).insert(doc)
        print(f"  [ALERT {severity}] {alert_type}: {details.get('summary', '')}")
        return alert_key
    except Exception as e:
        logger.error(f"创建alert失败: {e}")
        return None


def get_new_alerts(db):
    aql = f"FOR a IN {MONITOR_ALERTS_COLLECTION} FILTER a.status == 'new' SORT a.created_at DESC RETURN a"
    return list(db.aql.execute(aql, ttl=60))


def resolve_alert(db, alert_key, resolution="fixed"):
    db.collection(MONITOR_ALERTS_COLLECTION).update({
        "_key": alert_key,
        "status": resolution,
        "resolved_at": _utc_now(),
    })


# ============================================================
# 自动检查A：session健康（harness-p vs Redis running vs 设定并发）
# ============================================================

def check_session_health(db, expected_concurrency):
    """检查harness-p session数是否与并发设定匹配"""
    result = subprocess.run(
        ["tmux", "list-sessions"], capture_output=True, text=True, timeout=5
    )
    harness_p = [l for l in result.stdout.split("\n") if "harness-p" in l and "harness-dbmon" not in l]
    actual = len(harness_p)

    r = get_redis()
    redis_running = r.hlen("math:running")

    alerts = []
    if actual == 0 and redis_running > 0:
        alerts.append(("session_health", "critical", {
            "summary": f"Redis有{redis_running}个running但tmux无harness-p session，runner可能挂了",
            "redis_running": redis_running,
            "tmux_sessions": actual,
        }))
    elif actual == 0 and expected_concurrency > 0 and redis_running == 0:
        # pending有题但没有任何session——可能runner挂了或feeder没feed
        pending = r.zcard("math:pending")
        if pending > 0:
            alerts.append(("session_health", "critical", {
                "summary": f"pending有{pending}题但无harness-p session，runner可能挂了",
                "pending": pending,
                "tmux_sessions": actual,
                "expected": expected_concurrency,
            }))

    return alerts


# ============================================================
# 自动检查B：队列推进（stall检测）
# ============================================================

def check_queue_progress(last_state):
    """检查Redis队列是否在推进"""
    try:
        r = get_redis()
        pending = r.zcard("math:pending")
        completed = r.llen("math:completed")
        failed = r.llen("math:failed")
        running = r.hlen("math:running")
    except Exception as e:
        return [("redis_connection", "critical", {"summary": f"Redis连接失败: {e}"})], last_state

    current_state = {"pending": pending, "completed": completed, "failed": failed,
                     "running": running, "ts": _ts()}
    alerts = []

    if last_state:
        # pending没变且running>0——可能stall
        if pending == last_state["pending"] and pending > 0 and running > 0:
            elapsed = _ts() - last_state["ts"]
            if elapsed > STALL_THRESHOLD_SECONDS:
                alerts.append(("queue_stalled", "critical", {
                    "summary": f"队列{elapsed}秒无变化，pending={pending} running={running}",
                    "pending": pending,
                    "running": running,
                    "stall_seconds": elapsed,
                }))
        # completed没增加且running>0——可能collector挂了
        if completed == last_state["completed"] and running > 0:
            elapsed = _ts() - last_state["ts"]
            if elapsed > STALL_THRESHOLD_SECONDS:
                alerts.append(("no_completions", "warning", {
                    "summary": f"队列{elapsed}秒无新完成，collector可能挂了",
                    "completed": completed,
                    "running": running,
                    "stall_seconds": elapsed,
                }))

    return alerts, current_state


# ============================================================
# 自动检查C：rate limit检测（解题系统核心问题）
# ============================================================

def check_rate_limit(db, interval_seconds):
    """检查最近interval内是否有rate_limited"""
    now = datetime.now(timezone.utc)
    start = now - timedelta(seconds=interval_seconds)
    aql = (
        f"FOR r IN {ATTEMPT_COLLECTION} "
        f"FILTER r.ended_at >= @s "
        f"FILTER r.status == 'rate_limited' "
        f"FILTER r.fixed_by == null "
        f"COLLECT WITH COUNT INTO c RETURN c"
    )
    cursor = db.aql.execute(aql, bind_vars={"s": start.strftime('%Y-%m-%dT%H:%M')}, ttl=60)
    count = list(cursor)[0] if cursor.batch else 0

    alerts = []
    if count >= RATE_LIMIT_THRESHOLD:
        alerts.append(("rate_limit", "critical", {
            "summary": f"最近{interval_seconds//60}分钟{count}个rate_limited（阈值{RATE_LIMIT_THRESHOLD}），需降并发",
            "count": count,
            "threshold": RATE_LIMIT_THRESHOLD,
            "interval_seconds": interval_seconds,
        }))
    elif count > 0:
        alerts.append(("rate_limit", "warning", {
            "summary": f"最近{interval_seconds//60}分钟{count}个rate_limited（零星，观察中）",
            "count": count,
        }))

    return alerts


# ============================================================
# 自动检查D：僵尸session（空pane）
# ============================================================

def check_zombie_sessions(db):
    """检查空pane僵尸session"""
    r = get_redis()
    running = r.hgetall("math:running")

    zombies = []
    for k, v in running.items():
        data = json.loads(v)
        eid = data.get("exp_id", "")
        tmux_sess = f"harness-{eid}"
        res = subprocess.run(["tmux", "capture-pane", "-t", tmux_sess, "-p", "-S", "-50"],
                             capture_output=True, text=True, timeout=5)
        pane = res.stdout
        # 空pane = 僵尸（devin cli已退出但tmux session残留）
        if not pane.strip():
            zombies.append({"exp_id": eid, "problem_key": data.get("problem_key", "")})

    alerts = []
    if len(zombies) >= ZOMBIE_THRESHOLD:
        alerts.append(("zombie_sessions", "warning", {
            "summary": f"{len(zombies)}个空pane僵尸session（阈值{ZOMBIE_THRESHOLD}）",
            "zombies": zombies[:5],
            "count": len(zombies),
        }))

    return alerts


# ============================================================
# 自动检查E：export落盘率
# ============================================================

def check_export_landing(db):
    """抽查最近completed的题是否有export文件"""
    aql = (
        f"FOR a IN {ATTEMPT_COLLECTION} "
        f"FILTER a.status == 'candidate_solved' "
        f"SORT a.ended_at DESC LIMIT 10 RETURN a"
    )
    cursor = db.aql.execute(aql, ttl=60)
    records = list(cursor)

    if not records:
        return []

    missing = []
    for rec in records:
        eid = rec.get("exp_id", "")
        if not eid:
            continue
        export_path = TRAJ_BASE / eid / "exports" / "conversation.json"
        if not export_path.exists():
            missing.append({"exp_id": eid, "problem_id": rec.get("problem_id", "")})

    rate = len(missing) / len(records) if records else 0
    alerts = []
    if rate > EXPORT_MISSING_THRESHOLD:
        alerts.append(("export_missing", "critical", {
            "summary": f"export缺失率{rate:.0%}（{len(missing)}/{len(records)}），阈值{EXPORT_MISSING_THRESHOLD:.0%}",
            "missing": missing[:5],
            "missing_count": len(missing),
            "sampled": len(records),
        }))

    return alerts


# ============================================================
# 自动检查F：solve_time可信度
# ============================================================

def check_solve_time_credibility(db):
    """检查solve_time > runtime的比例"""
    aql = (
        f"FOR a IN {ATTEMPT_COLLECTION} "
        f"FILTER a.status == 'candidate_solved' "
        f"SORT a.ended_at DESC LIMIT 20 RETURN a"
    )
    cursor = db.aql.execute(aql, ttl=60)
    records = list(cursor)

    if not records:
        return []

    st_gt = sum(1 for rec in records
                if rec.get("solve_time_seconds", 0) > rec.get("runtime_seconds", 0))
    st_zero = sum(1 for rec in records if rec.get("solve_time_seconds", 0) == 0)
    rate = st_gt / len(records)

    alerts = []
    if rate > SOLVE_TIME_ANOMALY_THRESHOLD:
        alerts.append(("solve_time_anomaly", "warning", {
            "summary": f"solve_time>runtime比例{rate:.0%}（{st_gt}/{len(records)}），阈值{SOLVE_TIME_ANOMALY_THRESHOLD:.0%}",
            "anomaly_count": st_gt,
            "zero_count": st_zero,
            "sampled": len(records),
        }))

    return alerts


# ============================================================
# 自动检查G：失败率
# ============================================================

def check_failure_rate(db, interval_seconds):
    """检查最近interval内的失败率"""
    now = datetime.now(timezone.utc)
    start = now - timedelta(seconds=interval_seconds)
    aql = (
        f"FOR r IN {ATTEMPT_COLLECTION} "
        f"FILTER r.ended_at >= @s "
        f"FILTER r.fixed_by == null "
        f"COLLECT status = r.status WITH COUNT INTO c "
        f"RETURN {{status, count: c}}"
    )
    cursor = db.aql.execute(aql, bind_vars={"s": start.strftime('%Y-%m-%dT%H:%M')}, ttl=60)
    status_counts = {r["status"]: r["count"] for r in cursor}

    total = sum(status_counts.values())
    if total == 0:
        return []

    failed_statuses = ["failed_token_limit", "failed_no_proof", "failed_tool_stall",
                       "dead_session", "rate_limited", "failed_connection",
                       "failed_network_stuck", "launch_error", "answer_leak_in_input",
                       "crash_recovered", "failed_thinking_spin", "ai_gave_up",
                       "failed_timeout", "failed_stall"]
    failed = sum(status_counts.get(s, 0) for s in failed_statuses)
    solved = status_counts.get("candidate_solved", 0)
    finished = failed + solved

    if finished == 0:
        return []

    rate = failed / finished
    alerts = []
    if rate > FAILURE_RATE_THRESHOLD:
        alerts.append(("failure_rate", "warning", {
            "summary": f"最近{interval_seconds//60}分钟失败率{rate:.0%}（{failed}/{finished}），阈值{FAILURE_RATE_THRESHOLD:.0%}",
            "failed": failed,
            "solved": solved,
            "finished": finished,
            "failure_breakdown": {s: status_counts.get(s, 0) for s in failed_statuses
                                  if status_counts.get(s, 0) > 0},
        }))

    return alerts


# ============================================================
# 自动检查H：吞吐趋势
# ============================================================

def check_throughput_trend(db, last_state, interval_seconds):
    """对比前后轮次的吞吐，检测吞吐下降"""
    now = datetime.now(timezone.utc)
    start = now - timedelta(seconds=interval_seconds)
    aql = (
        f"FOR r IN {ATTEMPT_COLLECTION} "
        f"FILTER r.ended_at >= @s "
        f"FILTER r.fixed_by == null "
        f"FILTER r.status == 'candidate_solved' "
        f"COLLECT WITH COUNT INTO c RETURN c"
    )
    cursor = db.aql.execute(aql, bind_vars={"s": start.strftime('%Y-%m-%dT%H:%M')}, ttl=60)
    current_solved = list(cursor)[0] if cursor.batch else 0

    alerts = []
    if last_state and last_state.get("solved_in_interval", 0) > 0:
        prev = last_state["solved_in_interval"]
        drop_ratio = 1 - (current_solved / prev) if prev > 0 else 0
        if drop_ratio > 0.5 and current_solved < 5:
            alerts.append(("throughput_drop", "warning", {
                "summary": f"吞吐下降{drop_ratio:.0%}（上轮{prev}→本轮{current_solved}题/{interval_seconds//60}分钟）",
                "previous": prev,
                "current": current_solved,
                "interval_seconds": interval_seconds,
            }))

    return alerts, {"solved_in_interval": current_solved}


# ============================================================
# AI review抽样
# ============================================================

def flag_for_ai_review(db, sample_size=SAMPLE_SIZE):
    """抽样几条candidate_solved，标记为需AI review

    AI需要检查：
    - proof是否数学正确（不是幻觉/编造）
    - 是否有答案泄漏（proof中直接引用了答案）
    - proof的完整度（是否有跳步过多）
    """
    aql = (
        f"FOR a IN {ATTEMPT_COLLECTION} "
        f"FILTER a.status == 'candidate_solved' "
        f"FILTER a.ai_reviewed == null "
        f"SORT a.ended_at DESC LIMIT @n RETURN a"
    )
    cursor = db.aql.execute(aql, bind_vars={"n": sample_size}, ttl=60)
    runs = list(cursor)

    flagged = []
    for run in runs:
        eid = run.get("exp_id", "")
        export_path = TRAJ_BASE / eid / "exports" / "conversation.json"
        proof_snippet = ""
        if export_path.exists():
            try:
                content = export_path.read_text(encoding="utf-8", errors="ignore")
                # 提取最后2000字符作为proof snippet
                proof_snippet = content[-2000:] if len(content) > 2000 else content
            except Exception:
                pass

        flagged.append({
            "exp_id": eid,
            "problem_id": run.get("problem_id", ""),
            "solve_time_seconds": run.get("solve_time_seconds", 0),
            "proof_snippet": proof_snippet[:500],
        })

        # 标记为已reviewed（避免重复抽样）
        db.collection(ATTEMPT_COLLECTION).update({
            "_key": run["_key"],
            "ai_reviewed": "flagged",
            "ai_reviewed_at": _utc_now(),
        })

    if flagged:
        create_alert(db, "ai_review_sample", "info", {
            "summary": f"抽样{len(flagged)}条candidate_solved需AI review（proof质量检查）",
            "samples": flagged,
        })

    return flagged


# ============================================================
# 主监控循环
# ============================================================

def run_monitor_loop(interval=300, expected_concurrency=20, once=False):
    """运行监控循环"""
    logger.info(f"Monitor Pipe启动 interval={interval}s concurrency={expected_concurrency}")
    print(f"=== Monitor Pipe启动 interval={interval}s concurrency={expected_concurrency} ===")

    db = _connect_db()
    ensure_monitor_collections(db)

    last_queue_state = None
    last_throughput_state = None
    check_count = 0

    while True:
        check_count += 1
        now = _utc_now()
        print(f"\n--- 监控轮次 #{check_count} @ {now} ---")

        all_alerts = []

        # A. session健康
        try:
            alerts = check_session_health(db, expected_concurrency)
            all_alerts.extend(alerts)
        except Exception as e:
            logger.error(f"check_session_health失败: {e}")

        # B. 队列推进
        try:
            alerts, last_queue_state = check_queue_progress(last_queue_state)
            all_alerts.extend(alerts)
        except Exception as e:
            logger.error(f"check_queue_progress失败: {e}")

        # C. rate limit检测
        try:
            alerts = check_rate_limit(db, interval)
            all_alerts.extend(alerts)
        except Exception as e:
            logger.error(f"check_rate_limit失败: {e}")

        # D. 僵尸session
        try:
            alerts = check_zombie_sessions(db)
            all_alerts.extend(alerts)
        except Exception as e:
            logger.error(f"check_zombie_sessions失败: {e}")

        # E. export落盘
        try:
            alerts = check_export_landing(db)
            all_alerts.extend(alerts)
        except Exception as e:
            logger.error(f"check_export_landing失败: {e}")

        # F. solve_time可信度
        try:
            alerts = check_solve_time_credibility(db)
            all_alerts.extend(alerts)
        except Exception as e:
            logger.error(f"check_solve_time_credibility失败: {e}")

        # G. 失败率
        try:
            alerts = check_failure_rate(db, interval)
            all_alerts.extend(alerts)
        except Exception as e:
            logger.error(f"check_failure_rate失败: {e}")

        # H. 吞吐趋势
        try:
            alerts, last_throughput_state = check_throughput_trend(db, last_throughput_state, interval)
            all_alerts.extend(alerts)
        except Exception as e:
            logger.error(f"check_throughput_trend失败: {e}")

        # 创建alerts
        for alert_type, severity, details in all_alerts:
            create_alert(db, alert_type, severity, details)

        # AI review抽样（每3轮一次）
        if check_count % 3 == 0:
            try:
                flagged = flag_for_ai_review(db)
                if flagged:
                    print(f"  [AI_REVIEW] 抽样{len(flagged)}条需AI review:")
                    for f in flagged:
                        print(f"    {f['problem_id']}: solve_time={f['solve_time_seconds']}s")
            except Exception as e:
                logger.error(f"flag_for_ai_review失败: {e}")

        # 状态报告
        try:
            r = get_redis()
            pending = r.zcard("math:pending")
            running = r.hlen("math:running")
            completed = r.llen("math:completed")
            failed = r.llen("math:failed")
            print(f"  [queue] pending={pending} running={running} completed={completed} failed={failed}")

            # 最近interval吞吐
            now_dt = datetime.now(timezone.utc)
            start_dt = now_dt - timedelta(seconds=interval)
            aql = (
                f"FOR r IN {ATTEMPT_COLLECTION} "
                f"FILTER r.ended_at >= @s "
                f"FILTER r.fixed_by == null "
                f"COLLECT status = r.status WITH COUNT INTO c "
                f"SORT c DESC RETURN {{status, count: c}}"
            )
            cursor = db.aql.execute(aql, bind_vars={"s": start_dt.strftime('%Y-%m-%dT%H:%M')}, ttl=60)
            status_counts = {r["status"]: r["count"] for r in cursor}
            total_recent = sum(status_counts.values())
            solved_recent = status_counts.get("candidate_solved", 0)
            print(f"  [throughput] 最近{interval//60}分钟: {total_recent}题 "
                  f"({total_recent*3600//interval if interval else 0}题/时) "
                  f"solved={solved_recent}")
            print(f"  [status] {json.dumps(status_counts)}")
        except Exception as e:
            logger.error(f"状态报告失败: {e}")

        # 检查新alerts
        new_alerts = get_new_alerts(db)
        if new_alerts:
            print(f"  [alerts] {len(new_alerts)}个新alert:")
            for a in new_alerts[:5]:
                print(f"    [{a['severity']}] {a['alert_type']}: {a['details'].get('summary', '')}")

        if once:
            print("\n=== 单轮检查完成（--once模式）===")
            break

        # 检查pipe服务是否还在运行
        result = subprocess.run(["tmux", "has-session", "-t", "pipe-runner"],
                                capture_output=True, timeout=5)
        if result.returncode != 0:
            create_alert(db, "pipe_service_dead", "critical", {
                "summary": "pipe-runner tmux session不存在，解题系统可能已停止",
            })
            print("  [CRITICAL] pipe-runner已停止，Monitor Pipe再等1轮后退出")
            time.sleep(interval)
            # 再检查一次
            result = subprocess.run(["tmux", "has-session", "-t", "pipe-runner"],
                                    capture_output=True, timeout=5)
            if result.returncode != 0:
                print("  pipe-runner仍未恢复，Monitor Pipe退出")
                break
            print("  pipe-runner已恢复，继续监控")

        time.sleep(interval)


def check_alerts():
    """查看所有新alerts"""
    db = _connect_db()
    ensure_monitor_collections(db)
    alerts = get_new_alerts(db)
    print(f"=== 新alerts: {len(alerts)}个 ===")
    for a in alerts:
        print(f"\n  [{a['severity']}] {a['alert_type']} (key={a['_key']})")
        print(f"    {a['details'].get('summary', '')}")
        for k, v in a['details'].items():
            if k != 'summary':
                val_str = str(v)
                if len(val_str) > 200:
                    val_str = val_str[:200] + "..."
                print(f"    {k}: {val_str}")
    return alerts


def main():
    parser = argparse.ArgumentParser(description="解题系统Monitor Pipe")
    parser.add_argument("--interval", type=int, default=300, help="检查间隔（秒），默认300")
    parser.add_argument("--concurrency", type=int, default=20, help="预期并发数")
    parser.add_argument("--check-alerts", action="store_true", help="查看新alerts")
    parser.add_argument("--resolve-alert", help="标记alert为已解决")
    parser.add_argument("--once", action="store_true", help="只跑一轮（不循环）")
    args = parser.parse_args()

    if args.check_alerts:
        check_alerts()
    elif args.resolve_alert:
        db = _connect_db()
        resolve_alert(db, args.resolve_alert)
        print(f"已解决alert: {args.resolve_alert}")
    else:
        run_monitor_loop(interval=args.interval, expected_concurrency=args.concurrency, once=args.once)


if __name__ == "__main__":
    main()
