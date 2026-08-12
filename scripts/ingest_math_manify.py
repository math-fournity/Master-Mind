#!/usr/bin/env python3
"""
math-manify 题库入库脚本——扫描 /data/math-manify/raw_downloads/ 中已下载的数据集，
为每道题在 problem_extraction_progress 集合中建立记录。

支持的数据集：
  - NuminaMath-1.5 (parquet, 896K)
  - NuminaMath-CoT-Small-Hard-200k (parquet, 199K)
  - NuminaMath-LEAN (parquet, 104K)
  - DeepMath-103K (parquet, 103K)
  - FineProofs-RL (parquet, 5227)
  - Lean-Workbook (parquet, 25K)
  - AMO-Bench (parquet, 50)
  - math-contests-2026 (jsonl, 197)
  - ucmo (jsonl, ~300)
  - BlueMO (json, ~1800)
  - MathArena (parquet×10, 325)
  - anti-guessing-olympiad (json, 268)

用法:
  .venv/bin/python3 scripts/ingest_math_manify.py                    # 入库所有已完成的数据集
  .venv/bin/python3 scripts/ingest_math_manify.py --dry-run           # 只统计不入库
  .venv/bin/python3 scripts/ingest_math_manify.py --dataset NuminaMath-1.5  # 只入库指定数据集
  .venv/bin/python3 scripts/ingest_math_manify.py --stats             # 只显示DB统计
"""

import argparse
import glob
import hashlib
import json
import os
import sys
from pathlib import Path

import pyarrow.parquet as pq
from arango import ArangoClient

# ---- 配置 ----
ARANGO_HOST = 'http://localhost:8529'
ARANGO_DB = 'xishujuzhen_math_glm52'
ARANGO_USER = 'root'
ARANGO_PASS = 'REDACTED-DB-PASSWORD'

MATH_MANIFY = Path('/data/math-manify/raw_downloads')


# ---- 工具函数 ----

def make_key(source_dataset, idx):
    """生成唯一_key"""
    return f"{source_dataset}_{idx:08d}"

def problem_hash(text):
    """题目文本的hash，用于去重"""
    normalized = text.strip().lower()[:500]
    return hashlib.md5(normalized.encode()).hexdigest()

def source_to_tier(source):
    """NuminaMath source字段 → difficulty_tier，非竞赛来源返回None表示不入库"""
    s = source.lower()
    if s in ('olympiads', 'olympiads_ref'):
        return 2
    if s in ('amc_aime', 'competition'):
        return 3
    # 以下来源不入库——不是竞赛题
    if s in ('cn_k12', 'orca_math', 'gsm8k', 'synthetic_math', 'synthetic_amc',
             'secondary_math', 'math_test', 'math_train', 'synthetic', 'unknown'):
        return None
    return 3  # 默认竞赛级

def difficulty_rating_to_tier(rating):
    """difficulty_rating (1-10) → difficulty_tier"""
    if rating >= 9: return 1
    if rating >= 7: return 2
    if rating >= 5: return 3
    if rating >= 3: return 4
    return 5

def deepmath_difficulty_to_tier(diff):
    """DeepMath difficulty (5-9) → difficulty_tier，<7不入库"""
    if diff >= 8: return 1
    if diff >= 7: return 2
    return None  # difficulty 5-6不入库


# ---- 各数据集入库函数 ----

def ingest_numina_math_15(col, dry_run=False):
    """NuminaMath-1.5: 896K题，parquet格式"""
    data_dir = MATH_MANIFY / "NuminaMath-1.5" / "data"
    if not data_dir.exists():
        print("  NuminaMath-1.5: 目录不存在，跳过")
        return 0

    count = 0
    existing_hashes = set()

    # 先加载已有numina_math的hash用于去重
    if not dry_run:
        cursor = col.db.aql.execute(
            'FOR p IN problem_extraction_progress FILTER p.source_dataset == "numina_math" RETURN p.problem_hash'
        )
        existing_hashes = set(cursor)

    for pf in sorted(data_dir.glob("*.parquet")):
        print(f"  处理 {pf.name}...")
        table = pq.read_table(pf)
        data = table.to_pylist()
        for row in data:
            if not row.get('problem_is_valid') or row['problem_is_valid'] != 'Yes':
                continue
            ph = problem_hash(row['problem'])
            if ph in existing_hashes:
                continue
            existing_hashes.add(ph)

            tier = source_to_tier(row.get('source', ''))
            if tier is None:
                continue  # 非竞赛来源，跳过
            record = {
                "_key": make_key("numina_math_15", count),
                "problem_text": row['problem'],
                "solution_text": row.get('solution', ''),
                "answer": row.get('answer', ''),
                "problem_type": row.get('problem_type', ''),
                "question_type": row.get('question_type', ''),
                "source_dataset": "numina_math_15",
                "source_subset": row.get('source', ''),
                "difficulty_tier": tier,
                "priority": tier,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "synthetic": row.get('synthetic', False),
                "local_path": str(pf),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1
            if count % 50000 == 0:
                print(f"    已处理 {count} 题...")

    print(f"  NuminaMath-1.5: {count} 题入库")
    return count


def ingest_numina_math_hard200k(col, dry_run=False):
    """NuminaMath-CoT-Small-Hard-200k: 199K题，parquet格式"""
    data_dir = MATH_MANIFY / "NuminaMath-CoT-Small-Hard-200k" / "data"
    if not data_dir.exists():
        print("  NuminaMath-CoT-Small-Hard-200k: 目录不存在，跳过")
        return 0

    count = 0
    existing_hashes = set()
    if not dry_run:
        cursor = col.db.aql.execute(
            'FOR p IN problem_extraction_progress RETURN p.problem_hash'
        )
        existing_hashes = set(cursor)

    for pf in sorted(data_dir.glob("*.parquet")):
        print(f"  处理 {pf.name}...")
        table = pq.read_table(pf)
        data = table.to_pylist()
        for row in data:
            ph = problem_hash(row['problem'])
            if ph in existing_hashes:
                continue
            existing_hashes.add(ph)

            tier = source_to_tier(row.get('source', ''))
            if tier is None:
                continue  # 非竞赛来源，跳过
            record = {
                "_key": make_key("numina_hard200k", count),
                "problem_text": row['problem'],
                "solution_text": row.get('solution', ''),
                "source_dataset": "numina_hard200k",
                "source_subset": row.get('source', ''),
                "difficulty_tier": tier,
                "priority": tier,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "local_path": str(pf),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1
            if count % 20000 == 0:
                print(f"    已处理 {count} 题...")

    print(f"  NuminaMath-CoT-Small-Hard-200k: {count} 题入库")
    return count


def ingest_numina_math_lean(col, dry_run=False):
    """NuminaMath-LEAN: 104K题，parquet格式"""
    data_dir = MATH_MANIFY / "NuminaMath-LEAN" / "data"
    if not data_dir.exists():
        print("  NuminaMath-LEAN: 目录不存在，跳过")
        return 0

    count = 0
    for pf in sorted(data_dir.glob("*.parquet")):
        print(f"  处理 {pf.name}...")
        table = pq.read_table(pf)
        data = table.to_pylist()
        for row in data:
            problem = row.get('problem') or ''
            if not problem.strip():
                continue
            ph = problem_hash(problem)
            formal_proof = row.get('formal_proof') or ''
            source = row.get('source') or ''
            tier = source_to_tier(source)
            if tier is None:
                continue  # 非竞赛来源，跳过
            record = {
                "_key": make_key("numina_lean", count),
                "problem_text": problem,
                "solution_text": formal_proof,
                "formal_statement": row.get('formal_statement') or '',
                "formal_ground_truth": row.get('formal_ground_truth', ''),
                "answer": row.get('answer', ''),
                "problem_type": row.get('problem_type', ''),
                "source_dataset": "numina_math_lean",
                "source_subset": source,
                "difficulty_tier": tier,
                "priority": tier,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "has_formal_proof": bool(formal_proof.strip()),
                "local_path": str(pf),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1
            if count % 20000 == 0:
                print(f"    已处理 {count} 题...")

    print(f"  NuminaMath-LEAN: {count} 题入库")
    return count


def ingest_deepmath_103k(col, dry_run=False):
    """DeepMath-103K: 103K题，parquet格式"""
    data_dir = MATH_MANIFY / "DeepMath-103K" / "data"
    if not data_dir.exists():
        print("  DeepMath-103K: 目录不存在，跳过")
        return 0

    count = 0
    for pf in sorted(data_dir.glob("*.parquet")):
        print(f"  处理 {pf.name}...")
        table = pq.read_table(pf)
        data = table.to_pylist()
        for row in data:
            ph = problem_hash(row.get('question', ''))
            diff = row.get('difficulty', 5)
            tier = deepmath_difficulty_to_tier(diff)
            if tier is None:
                continue  # difficulty<7，跳过
            record = {
                "_key": make_key("deepmath_103k", count),
                "problem_text": row.get('question', ''),
                "solution_text": row.get('r1_solution_1', ''),
                "answer": row.get('final_answer', ''),
                "difficulty_score": diff,
                "topic": row.get('topic', ''),
                "source_dataset": "deepmath_103k",
                "source_subset": "deepmath",
                "difficulty_tier": tier,
                "priority": tier,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "local_path": str(pf),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1
            if count % 20000 == 0:
                print(f"    已处理 {count} 题...")

    print(f"  DeepMath-103K: {count} 题入库")
    return count


def ingest_fineproofs_rl(col, dry_run=False):
    """FineProofs-RL: 5227题，parquet格式"""
    data_dir = MATH_MANIFY / "FineProofs-RL" / "data"
    if not data_dir.exists():
        print("  FineProofs-RL: 目录不存在，跳过")
        return 0

    count = 0
    for pf in sorted(data_dir.glob("*.parquet")):
        print(f"  处理 {pf.name}...")
        table = pq.read_table(pf)
        data = table.to_pylist()
        for row in data:
            ph = problem_hash(row.get('problem', ''))
            reward_mean = row.get('reward_mean', 0)
            # 难度由reward_mean反推：越低越难
            if reward_mean < 0.05: tier = 1
            elif reward_mean < 0.15: tier = 2
            else: tier = 2
            record = {
                "_key": make_key("fineproofs_rl", count),
                "problem_text": row.get('problem', ''),
                "solution_text": row.get('rubrics', ''),
                "source_dataset": "fineproofs_rl",
                "source_subset": row.get('source', ''),
                "difficulty_tier": tier,
                "priority": tier,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "reward_mean": reward_mean,
                "reward_std": row.get('reward_std', 0),
                "num_rewards": row.get('num_rewards', 0),
                "local_path": str(pf),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1

    print(f"  FineProofs-RL: {count} 题入库")
    return count


def ingest_lean_workbook(col, dry_run=False):
    """Lean-Workbook: 25K题，parquet格式"""
    base = MATH_MANIFY / "Lean-Workbook"
    if not base.exists():
        print("  Lean-Workbook: 目录不存在，跳过")
        return 0

    count = 0
    for pf in sorted(base.glob("*.parquet")):
        print(f"  处理 {pf.name}...")
        table = pq.read_table(pf)
        data = table.to_pylist()
        for row in data:
            stmt = row.get('natural_language_statement', '')
            if not stmt.strip():
                continue
            ph = problem_hash(stmt)
            record = {
                "_key": make_key("lean_workbook", count),
                "problem_text": stmt,
                "solution_text": row.get('tactic', ''),
                "answer": row.get('answer', ''),
                "formal_statement": row.get('formal_statement', ''),
                "source_dataset": "lean_workbook",
                "source_subset": row.get('id', ''),
                "difficulty_tier": 3,
                "priority": 3,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "status": row.get('status', ''),
                "local_path": str(pf),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1

    print(f"  Lean-Workbook: {count} 题入库")
    return count


def ingest_amo_bench(col, dry_run=False):
    """AMO-Bench: 50题，parquet格式"""
    data_dir = MATH_MANIFY / "AMO-Bench" / "data"
    if not data_dir.exists():
        print("  AMO-Bench: 目录不存在，跳过")
        return 0

    count = 0
    for pf in sorted(data_dir.glob("*.parquet")):
        table = pq.read_table(pf)
        data = table.to_pylist()
        for row in data:
            ph = problem_hash(row.get('prompt', ''))
            record = {
                "_key": make_key("amo_bench", count),
                "problem_text": row.get('prompt', ''),
                "solution_text": row.get('solution', ''),
                "answer": row.get('answer', ''),
                "answer_type": row.get('answer_type', ''),
                "source_dataset": "amo_bench",
                "source_subset": "amo_bench",
                "difficulty_tier": 1,  # IMO级+
                "priority": 1,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "local_path": str(pf),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1

    print(f"  AMO-Bench: {count} 题入库")
    return count


def ingest_math_contests_2026(col, dry_run=False):
    """math-contests-2026: 197题，jsonl格式"""
    base = MATH_MANIFY / "math-contests-2026"
    if not base.exists():
        print("  math-contests-2026: 目录不存在，跳过")
        return 0

    problems_file = base / "problems.jsonl"
    solutions_file = base / "solutions.jsonl"
    if not problems_file.exists():
        print("  math-contests-2026: problems.jsonl不存在，跳过")
        return 0

    # 加载solutions
    solutions = {}
    if solutions_file.exists():
        with open(solutions_file) as f:
            for line in f:
                d = json.loads(line)
                pid = d.get('problem_id', '')
                solutions[pid] = d

    count = 0
    with open(problems_file) as f:
        for line in f:
            d = json.loads(line)
            ph = problem_hash(d.get('statement', ''))
            rating = int(d.get('difficulty_rating', 5))
            tier = difficulty_rating_to_tier(rating)
            sol = solutions.get(d.get('problem_id', ''), {})
            record = {
                "_key": make_key("math_contests_2026", count),
                "problem_text": d.get('statement', ''),
                "solution_text": sol.get('solution', ''),
                "source_dataset": "math_contests_2026",
                "source_subset": d.get('source', ''),
                "country": d.get('country', ''),
                "domain": d.get('domain', ''),
                "difficulty_rating": rating,
                "difficulty_level": d.get('difficulty_level', ''),
                "difficulty_tier": tier,
                "priority": tier,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "answer_type": d.get('answer_type', ''),
                "task": d.get('task', ''),
                "url": d.get('url', ''),
                "local_path": str(problems_file),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1

    print(f"  math-contests-2026: {count} 题入库")
    return count


def ingest_ucmo(col, dry_run=False):
    """ucmo: ~300题，jsonl格式"""
    base = MATH_MANIFY / "ucmo"
    if not base.exists():
        print("  ucmo: 目录不存在，跳过")
        return 0

    tasks_file = base / "tasks.jsonl"
    if not tasks_file.exists():
        print("  ucmo: tasks.jsonl不存在，跳过")
        return 0

    count = 0
    with open(tasks_file) as f:
        for line in f:
            d = json.loads(line)
            ph = problem_hash(d.get('problem', ''))
            diff = float(d.get('difficulty', 5))
            tier = difficulty_rating_to_tier(diff)
            record = {
                "_key": make_key("ucmo", count),
                "problem_text": d.get('problem', ''),
                "solution_text": d.get('solution', ''),
                "answer": d.get('answer', ''),
                "answer_type": d.get('answer_type', ''),
                "source_dataset": "ucmo",
                "source_subset": d.get('source', ''),
                "difficulty_score": diff,
                "difficulty_tier": tier,
                "priority": tier,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "contest_date": d.get('contest_date', ''),
                "url": d.get('link', ''),
                "local_path": str(tasks_file),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1

    print(f"  ucmo: {count} 题入库")
    return count


def ingest_bluemo(col, dry_run=False):
    """BlueMO: ~1800题，json格式（小蓝书奥赛）"""
    base = MATH_MANIFY / "BlueMO"
    if not base.exists():
        print("  BlueMO: 目录不存在，跳过")
        return 0

    count = 0
    for subdir in ['proof', 'calculation']:
        dir_path = base / subdir
        if not dir_path.exists():
            continue
        for jf in sorted(dir_path.glob("*.json")):
            with open(jf) as f:
                d = json.load(f)
            problem = d.get('problem', '')
            if not problem.strip():
                continue
            ph = problem_hash(problem)
            record = {
                "_key": make_key("bluemo", count),
                "problem_text": problem,
                "solution_text": d.get('solution', ''),
                "problem_type": d.get('problem_type', ''),
                "source_dataset": "bluemo",
                "source_subset": subdir,
                "difficulty_tier": 2,  # 奥赛级
                "priority": 2,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "source_file": d.get('source_file', ''),
                "local_path": str(jf),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1

    print(f"  BlueMO: {count} 题入库")
    return count


def ingest_matharena_new(col, dry_run=False):
    """MathArena新竞赛: 325题，parquet格式×10竞赛"""
    base = MATH_MANIFY / "MathArena"
    if not base.exists():
        print("  MathArena: 目录不存在，跳过")
        return 0

    count = 0
    for comp_dir in sorted(base.iterdir()):
        if not comp_dir.is_dir():
            continue
        comp_name = comp_dir.name
        parquets = list((comp_dir / "data").glob("*.parquet")) if (comp_dir / "data").exists() else []
        if not parquets:
            continue
        table = pq.read_table(parquets[0])
        data = table.to_pylist()
        for row in data:
            problem = row.get('problem', '')
            if not problem.strip():
                continue
            ph = problem_hash(problem)
            # 难度分级
            if comp_name in ('imo_2025', 'putnam_2025', 'usamo_2025', 'usamo_2026', 'imc_2025'):
                tier = 1
            elif 'aime' in comp_name:
                idx = row.get('problem_idx', 0)
                tier = 2 if idx >= 13 else 3
            else:
                tier = 2
            record = {
                "_key": make_key("matharena_new", count),
                "problem_text": problem,
                "solution_text": row.get('sample_solution', ''),
                "answer": str(row.get('answer', '')),
                "problem_type": str(row.get('problem_type', '')),
                "source_dataset": "matharena_new",
                "source_subset": comp_name,
                "difficulty_tier": tier,
                "priority": tier,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "problem_idx": row.get('problem_idx', 0),
                "local_path": str(parquets[0]),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1

    print(f"  MathArena(新): {count} 题入库")
    return count


def ingest_anti_guessing(col, dry_run=False):
    """anti-guessing-olympiad: 134题HARD认证，json格式"""
    base = MATH_MANIFY / "anti-guessing-olympiad" / "data"
    if not base.exists():
        print("  anti-guessing-olympiad: 目录不存在，跳过")
        return 0

    # 关键文件是FINAL_HARD_134.json
    hard_file = base / "FINAL_HARD_134.json"
    if not hard_file.exists():
        print("  anti-guessing-olympiad: FINAL_HARD_134.json不存在，跳过")
        return 0

    count = 0
    with open(hard_file) as f:
        data = json.load(f)
    for item in data:
        problem = item.get('problem', '')
        if not problem.strip():
            continue
        ph = problem_hash(problem)
        record = {
            "_key": make_key("anti_guessing", count),
            "problem_text": problem,
            "solution_text": item.get('solution', ''),
            "answer": item.get('answer', ''),
            "answer_type": item.get('answer_type', ''),
            "problem_type": item.get('problem_type', ''),
            "question_type": item.get('question_type', ''),
            "source_dataset": "anti_guessing_olympiad",
            "source_subset": "certified_hard",
            "difficulty_tier": 1,
            "priority": 1,
            "extraction_status": "pending",
            "skip_reason": None,
            "problem_hash": ph,
            "guessability": item.get('guessability', ''),
            "local_path": str(hard_file),
            "ingest_date": "2026-08-12",
        }
        if not dry_run:
            col.insert(record)
        count += 1

    print(f"  anti-guessing-olympiad: {count} 题入库")
    return count


def ingest_oda_math_460k(col, dry_run=False):
    """ODA-Math-460k: 460K题，parquet格式，只入库difficulty>=7"""
    data_dir = MATH_MANIFY / "ODA-Math-460k" / "data"
    if not data_dir.exists():
        print("  ODA-Math-460k: 目录不存在，跳过")
        return 0

    count = 0
    for pf in sorted(data_dir.glob("*.parquet")):
        print(f"  处理 {pf.name}...")
        table = pq.read_table(pf)
        data = table.to_pylist()
        for row in data:
            diff = row.get('difficulty', 0)
            if diff < 7:
                continue  # 只入库difficulty>=7
            ph = problem_hash(row.get('question', ''))
            if diff >= 9: tier = 1
            elif diff >= 8: tier = 2
            else: tier = 3
            record = {
                "_key": make_key("oda_math_460k", count),
                "problem_text": row.get('question', ''),
                "solution_text": row.get('response', ''),
                "answer": row.get('expected_answer', ''),
                "subject": row.get('subject', ''),
                "difficulty_score": diff,
                "pass_rate": row.get('pass_rate', 0),
                "source_dataset": "oda_math_460k",
                "source_subset": row.get('source', ''),
                "difficulty_tier": tier,
                "priority": tier,
                "extraction_status": "pending",
                "skip_reason": None,
                "problem_hash": ph,
                "local_path": str(pf),
                "ingest_date": "2026-08-12",
            }
            if not dry_run:
                col.insert(record)
            count += 1
            if count % 20000 == 0:
                print(f"    已处理 {count} 题...")

    print(f"  ODA-Math-460k: {count} 题入库（difficulty>=7）")
    return count


def ingest_olympiadbench(col, dry_run=False):
    """OlympiadBench-official: 只入库subject=Math的题"""
    base = MATH_MANIFY / "OlympiadBench-official" / "OlympiadBench"
    if not base.exists():
        print("  OlympiadBench-official: 目录不存在，跳过")
        return 0

    count = 0
    for root, dirs, files in os.walk(base):
        for f in files:
            if not f.endswith('.parquet'):
                continue
            pf = os.path.join(root, f)
            try:
                table = pq.read_table(pf)
                data = table.to_pylist()
            except Exception:
                continue
            for row in data:
                if row.get('subject', '') != 'Math':
                    continue  # 只入库数学题
                question = row.get('question', '')
                if not question.strip():
                    continue
                ph = problem_hash(question)
                diff = row.get('difficulty', '')
                if diff == 'Competition':
                    tier = 2
                elif diff == 'Easy':
                    tier = 3
                else:
                    tier = 2
                record = {
                    "_key": make_key("olympiadbench_official", count),
                    "problem_text": question,
                    "solution_text": str(row.get('solution', '')),
                    "answer": str(row.get('final_answer', '')),
                    "source_dataset": "olympiadbench_official",
                    "source_subset": os.path.basename(os.path.dirname(pf)),
                    "difficulty_tier": tier,
                    "priority": tier,
                    "extraction_status": "pending",
                    "skip_reason": None,
                    "problem_hash": ph,
                    "modality": row.get('modality', ''),
                    "is_multiple_answer": row.get('is_multiple_answer', False),
                    "answer_type": row.get('answer_type', ''),
                    "question_type": row.get('question_type', ''),
                    "subfield": row.get('subfield', ''),
                    "language": row.get('language', ''),
                    "local_path": pf,
                    "ingest_date": "2026-08-12",
                }
                if not dry_run:
                    col.insert(record)
                count += 1

    print(f"  OlympiadBench-official: {count} 题入库（Math only）")
    return count


# ---- 主函数 ----

DATASET_FUNCS = {
    'NuminaMath-1.5': ingest_numina_math_15,
    'NuminaMath-CoT-Small-Hard-200k': ingest_numina_math_hard200k,
    'NuminaMath-LEAN': ingest_numina_math_lean,
    'DeepMath-103K': ingest_deepmath_103k,
    'FineProofs-RL': ingest_fineproofs_rl,
    'Lean-Workbook': ingest_lean_workbook,
    'AMO-Bench': ingest_amo_bench,
    'math-contests-2026': ingest_math_contests_2026,
    'ucmo': ingest_ucmo,
    'BlueMO': ingest_bluemo,
    'MathArena': ingest_matharena_new,
    'anti-guessing-olympiad': ingest_anti_guessing,
    'ODA-Math-460k': ingest_oda_math_460k,
    'OlympiadBench-official': ingest_olympiadbench,
}

def show_stats(col):
    """显示DB统计"""
    total = col.db.aql.execute('RETURN LENGTH(problem_extraction_progress)').next()
    print(f"\nDB problem_extraction_progress 总量: {total}")

    # 按source_dataset统计
    cursor = col.db.aql.execute('''
        FOR p IN problem_extraction_progress
            COLLECT source = p.source_dataset WITH COUNT INTO cnt
            SORT cnt DESC
            RETURN {source: source, count: cnt}
    ''')
    print("\n按来源统计:")
    for r in cursor:
        print(f"  {r['source']}: {r['count']}")

    # 按difficulty_tier统计
    cursor = col.db.aql.execute('''
        FOR p IN problem_extraction_progress
            COLLECT tier = p.difficulty_tier WITH COUNT INTO cnt
            SORT tier ASC
            RETURN {tier: tier, count: cnt}
    ''')
    print("\n按难度统计:")
    for r in cursor:
        print(f"  Tier {r['tier']}: {r['count']}")

    # 按extraction_status统计
    cursor = col.db.aql.execute('''
        FOR p IN problem_extraction_progress
            COLLECT status = p.extraction_status WITH COUNT INTO cnt
            SORT cnt DESC
            RETURN {status: status, count: cnt}
    ''')
    print("\n按状态统计:")
    for r in cursor:
        print(f"  {r['status']}: {r['count']}")


def main():
    parser = argparse.ArgumentParser(description='math-manify题库入库脚本')
    parser.add_argument('--dry-run', action='store_true', help='只统计不入库')
    parser.add_argument('--dataset', type=str, help='只入库指定数据集')
    parser.add_argument('--stats', action='store_true', help='只显示DB统计')
    args = parser.parse_args()

    # 连接ArangoDB
    client = ArangoClient(hosts=ARANGO_HOST)
    db = client.db(ARANGO_DB, username=ARANGO_USER, password=ARANGO_PASS)
    col = db.collection('problem_extraction_progress')
    col.db = db  # 给col附加db引用

    if args.stats:
        show_stats(col)
        return

    print(f"\n{'='*60}")
    print(f"math-manify 题库入库 {'(dry-run)' if args.dry_run else ''}")
    print(f"{'='*60}\n")

    total = 0
    if args.dataset:
        if args.dataset in DATASET_FUNCS:
            total = DATASET_FUNCS[args.dataset](col, dry_run=args.dry_run)
        else:
            print(f"未知数据集: {args.dataset}")
            print(f"可用: {list(DATASET_FUNCS.keys())}")
            sys.exit(1)
    else:
        for name, func in DATASET_FUNCS.items():
            print(f"\n--- {name} ---")
            try:
                total += func(col, dry_run=args.dry_run)
            except Exception as e:
                print(f"  ❌ 错误: {e}")

    print(f"\n{'='*60}")
    print(f"总计入库: {total} 题")
    print(f"{'='*60}")

    show_stats(col)


if __name__ == '__main__':
    main()
