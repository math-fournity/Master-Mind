#!/usr/bin/env python3
"""retry_infrastructure.py — 基础设施失败自动重试

扫描failed队列中的基础设施失败（failed_connection/rate_limited/launch_error/dead_session），
将它们重新入pending队列，让Runner重新启动。

模型能力失败（failed_token_limit/ai_gave_up/failed_thinking_spin等）不重试——
它们是Profile数据。

用法:
  python retry_infrastructure.py [--max-retries 3] [--dry-run]
  python retry_infrastructure.py --once  # 执行一次后退出
"""
import sys
import os
import time
import json
import argparse

sys.path.insert(0, os.path.dirname(__file__))

from redis_queue import get_redis, ping
from arango import ArangoClient

DB_HOST = "http://localhost:8529"
DB_NAME = "xishujuzhen_math_glm52"
DB_USER = "root"
DB_PASS = "REDACTED-DB-PASSWORD"
ATTEMPT_COLLECTION = "devin_problem_runs"
COLLECTION = "problem_extraction_progress"

# 基础设施失败——重试
INFRA_FAILURES = {"failed_connection", "rate_limited", "launch_error", "dead_session"}

# 模型能力失败——不重试，是Profile数据
MODEL_FAILURES = {
    "failed_token_limit", "failed_output_limit", "ai_gave_up",
    "failed_thinking_spin", "failed_no_proof", "failed_stall",
    "invalid_tool_use",
}


def get_retry_count(db, problem_key: str) -> int:
    """查DB中该题目已有的基础设施失败重试次数"""
    aql = (
        f"FOR a IN {ATTEMPT_COLLECTION} "
        f"FILTER a.problem_id == '{problem_key}' "
        f"FILTER a.verdict IN {list(INFRA_FAILURES)!r} "
        f"COLLECT WITH COUNT INTO c RETURN c"
    )
    cursor = db.aql.execute(aql, ttl=60)
    return cursor.next()


def retry_failed(r, db, max_retries: int, dry_run: bool = False) -> dict:
    """扫描failed队列，重试基础设施失败"""
    failed_items = r.lrange("math:failed", 0, -1)
    infra_count = 0
    model_count = 0
    retried = 0
    skipped_max_retries = 0

    for item in failed_items:
        data = json.loads(item)
        verdict = data.get("verdict", "")
        problem_key = data.get("problem_key", "")

        if verdict in INFRA_FAILURES:
            infra_count += 1
            # 检查重试次数
            retry_count = get_retry_count(db, problem_key)
            if retry_count >= max_retries:
                skipped_max_retries += 1
                print(f"  ⏭️ {problem_key}: 已重试{retry_count}次, 达到上限{max_retries}", flush=True)
                continue

            if dry_run:
                print(f"  [DRY-RUN] 重试 {problem_key}: {verdict} (第{retry_count+1}次)", flush=True)
                retried += 1
            else:
                # 重新入pending队列
                priority = data.get("priority", 100)
                r.zadd("math:pending", {problem_key: priority})
                # 更新DB中problem状态为pending
                try:
                    db.collection(COLLECTION).update({"_key": problem_key, "extraction_status": "pending"})
                except Exception:
                    pass
                print(f"  ✅ 重试 {problem_key}: {verdict} → pending (第{retry_count+1}次)", flush=True)
                retried += 1
        else:
            model_count += 1

    # 从failed队列中移除已重试的项（保留模型能力失败和达到上限的）
    if not dry_run and retried > 0:
        # 重建failed队列——只保留模型能力失败和达到上限的基础设施失败
        remaining = []
        for item in failed_items:
            data = json.loads(item)
            verdict = data.get("verdict", "")
            problem_key = data.get("problem_key", "")
            if verdict in INFRA_FAILURES:
                retry_count = get_retry_count(db, problem_key)
                if retry_count < max_retries:
                    continue  # 已重试，移除
            remaining.append(item)
        r.delete("math:failed")
        if remaining:
            r.rpush("math:failed", *remaining)

    return {
        "total_failed": len(failed_items),
        "infra_failures": infra_count,
        "model_failures": model_count,
        "retried": retried,
        "skipped_max_retries": skipped_max_retries,
    }


def main():
    parser = argparse.ArgumentParser(description="基础设施失败自动重试")
    parser.add_argument("--max-retries", type=int, default=3, help="最大重试次数")
    parser.add_argument("--dry-run", action="store_true", help="只看不执行")
    parser.add_argument("--once", action="store_true", help="执行一次后退出（默认循环）")
    parser.add_argument("--interval", type=int, default=60, help="循环模式间隔秒数")
    args = parser.parse_args()

    if not ping():
        print("❌ Redis连接失败", flush=True)
        sys.exit(1)

    client = ArangoClient(hosts=DB_HOST, request_timeout=300)
    db = client.db(DB_NAME, username=DB_USER, password=DB_PASS)
    r = get_redis()

    def run_once():
        print(f"=== 扫描failed队列 ===", flush=True)
        result = retry_failed(r, db, args.max_retries, args.dry_run)
        print(f"  总failed:        {result['total_failed']}", flush=True)
        print(f"  基础设施失败:    {result['infra_failures']}", flush=True)
        print(f"  模型能力失败:    {result['model_failures']} (不重试, Profile数据)", flush=True)
        print(f"  已重试:          {result['retried']}", flush=True)
        print(f"  达到上限跳过:    {result['skipped_max_retries']}", flush=True)
        return result

    if args.once:
        run_once()
        return

    # 循环模式
    while True:
        run_once()
        print(f"\n等待 {args.interval}s 后再次扫描...\n", flush=True)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
