#!/usr/bin/env python3
"""rebuild_selection_pool.py — POC-2.5c选题池重建脚本

背景：2026-08-21预筛的45道清单只写在/tmp/p275-1962-v2/poc25c_selection_pool.txt，
未落盘repo即丢失（文件存在但内容为空）。本脚本从数据源（ArangoDB p27_continuation_runs
+ D盘产物）按poc25c_experiment_design.md §1的四道过滤标准重建选题池。

过滤标准（按序）：
1. status=completed 且 current_round=2（bare截断+1轮续传解出——弱因果池定义）
2. round2/exports/conversation.json 存在且完整（>10KB且可解析）
3. proof.md 存在且含 \\boxed
4. 泄漏初筛：problem_text不含解答性文字标记

用法：source ~/master-mind-analysis-system/.env 后运行本脚本。
输出：selection_pool_2026-08-22.md + selection_pool_2026-08-22.json（同目录）。
"""

import json
import os
import re
from collections import Counter
from datetime import date
from pathlib import Path

from arango import ArangoClient

ANALYSIS_ENV = "~/master-mind-analysis-system/.env"
OUT_DIR = Path(__file__).resolve().parent
TODAY = date.today().isoformat()

# 泄漏初筛标记：题面出现这些模式即标flag（人工复核后决定去留）
LEAK_PATTERNS = [
    (r"\\boxed\{", "题面含boxed答案"),
    (r"[Aa]nswer\s*[:=]", "题面含Answer字段"),
    (r"^#+\s*Solution", "题面含Solution节"),
    (r"答案[是为：:]", "题面含中文答案字段"),
]


def load_env(path):
    for line in open(path):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k, v)


def extract_boxed(proof_text):
    """提取proof.md中全部\\boxed{...}内容（嵌套花括号感知）。"""
    answers = []
    for m in re.finditer(r"\\boxed\{", proof_text):
        depth, i = 1, m.end()
        while i < len(proof_text) and depth > 0:
            if proof_text[i] == "{":
                depth += 1
            elif proof_text[i] == "}":
                depth -= 1
            i += 1
        if depth == 0:
            answers.append(proof_text[m.end() : i - 1].strip())
    return answers


def main():
    load_env(ANALYSIS_ENV)
    db_name = os.environ.get("ARANGO_DB", "xishujuzhen_math_glm52")
    client = ArangoClient(hosts=os.environ.get("ARANGO_HOST", "http://localhost:8529"))
    db = client.db(db_name, username="root", password="REDACTED-DB-PASSWORD")

    runs = list(
        db.aql.execute(
            'FOR d IN p27_continuation_runs '
            'FILTER d.status=="completed" AND d.current_round==2 '
            'SORT d.problem_id RETURN d'
        )
    )
    print(f"completed r2 runs: {len(runs)}")

    pool, rejected = [], []
    for d in runs:
        pid = d["problem_id"]
        source = pid.split("_")[0]
        exp = os.path.join(d.get("trajectory_dir", ""), "round2/exports/conversation.json")
        proof_path = os.path.join(d.get("work_dir", ""), "proof.md")
        problem_text = d.get("problem_text", "")

        rec = {
            "problem_id": pid,
            "source": source,
            "run_key": d["_key"],
            "work_dir": d.get("work_dir"),
            "trajectory_dir": d.get("trajectory_dir"),
        }

        # 过滤1：export存在且完整
        e_ok = False
        if os.path.isfile(exp):
            size = os.path.getsize(exp)
            rec["export_size"] = size
            if size > 10000:
                try:
                    json.load(open(exp))
                    e_ok = True
                    rec["export_valid_json"] = True
                except Exception:
                    rec["export_valid_json"] = False
        if not e_ok:
            rejected.append({**rec, "reject_reason": "export缺失或不完整"})
            continue

        # 过滤2：proof.md含boxed
        if not os.path.isfile(proof_path):
            rejected.append({**rec, "reject_reason": "proof.md缺失"})
            continue
        proof_text = open(proof_path, errors="ignore").read()
        rec["proof_size"] = len(proof_text)
        answers = extract_boxed(proof_text)
        rec["boxed_answers"] = answers
        if not answers:
            rejected.append({**rec, "reject_reason": "proof.md无boxed"})
            continue

        # 过滤3：泄漏初筛
        flags = [desc for pat, desc in LEAK_PATTERNS if re.search(pat, problem_text, re.M)]
        rec["leak_flags"] = flags

        pool.append(rec)

    src_dist = Counter(r["source"] for r in pool)
    print(f"pool candidates: {len(pool)}  by source: {dict(src_dist)}")
    flagged = [r["problem_id"] for r in pool if r["leak_flags"]]
    print(f"leak-flagged: {len(flagged)} {flagged}")

    # 落盘 JSON
    out_json = OUT_DIR / f"selection_pool_{TODAY}.json"
    meta = {
        "date": TODAY,
        "db": db_name,
        "collection": "p27_continuation_runs",
        "filter": "completed+round2+export完整+proof含boxed+泄漏初筛",
        "total_completed_r2": len(runs),
        "pool_size": len(pool),
        "rejected": len(rejected),
        "source_distribution": dict(src_dist),
        "quota_note": "实验设计§1要求deepmath为主+polymath/oda各保底2道；当前completed池仅含deepmath与amo，polymath/oda配额不可满足，如实记录为池限制。",
        "candidates": pool,
    }
    out_json.write_text(json.dumps(meta, ensure_ascii=False, indent=1))

    # 落盘 Markdown
    lines = [
        f"# POC-2.5c 选题池重建清单（{TODAY}）",
        "",
        f"- 数据源：`{db_name}.p27_continuation_runs`（completed+current_round=2 共{len(runs)}条）",
        f"- 硬过滤通过：**{len(pool)}道**（export完整+proof含boxed）；泄漏初筛flag {len(flagged)}道",
        f"- 来源分布：{dict(src_dist)}",
        "- 配额说明：设计§1的polymath/oda各保底2道在当前completed池中无供给（池仅deepmath+amo），如实记录。",
        "- 本清单替代已丢失的/tmp/p275-1962-v2/poc25c_selection_pool.txt（45道版，2026-08-21）。",
        "",
        "| # | problem_id | 来源 | boxed答案 | export大小 | proof大小 | 泄漏flag |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(pool, 1):
        ans = "; ".join(a[:40] for a in r["boxed_answers"]) or "—"
        lines.append(
            f"| {i} | {r['problem_id']} | {r['source']} | {ans} "
            f"| {r.get('export_size', 0)//1024}KB | {r.get('proof_size', 0)//1024}KB "
            f"| {'; '.join(r['leak_flags']) or '—'} |"
        )
    out_md = OUT_DIR / f"selection_pool_{TODAY}.md"
    out_md.write_text("\n".join(lines) + "\n")

    print(f"written: {out_md}")
    print(f"written: {out_json}")


if __name__ == "__main__":
    main()
