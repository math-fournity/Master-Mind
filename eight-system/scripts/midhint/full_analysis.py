#!/usr/bin/env python3
"""
完整的失败题梳理脚本——从所有题库获取标准解答，从trajectory获取thinking，做对照分析

支持的数据源：
- PolyMath: parquet, solution字段, id映射 polymath_{id:05d} -> id
- DeepMath: parquet, r1_solution_1字段, id映射 deepmath_103k_{id:08d} -> 行索引
- ODA-Math: parquet, response字段, id映射 oda_math_460k_{id:08d} -> id
- Omni-MATH-2: jsonl, solution字段, id映射 omni_math_{id:06d} -> id
- OlympiadBench: json, solution字段, id映射 mathnet_{id:06d} -> id
- compfiles: lean文件, id映射 compfiles_{xxx} -> 文件名
- aime: jsonl, solution字段
- AMO-Bench: parquet, solution字段
- fate: json, formal_statement（Lean，无人类解答）

用法：
  python3 eight-system/scripts/midhint/full_analysis.py --phase map    # 建立映射
  python3 eight-system/scripts/midhint/full_analysis.py --phase analyze # 执行分析
  python3 eight-system/scripts/midhint/full_analysis.py --phase all     # 全部
"""

import argparse
import json
import os
import re
import sys
import collections
from pathlib import Path

# === 路径常量 ===
TRAJECTORY_BASE = "/data/math-agent-glm5.2-tmux-agents-trajectory"
SOLVER_DIR_BASE = "/data/math-agent-glm5.2-tmux-agents-dir"
POLYMATH_PARQUET = "/data/math-manify/raw_downloads/PolyMath/data/train-00000-of-00001.parquet"
POLYMATH_NORMAL = "/data/math-manify/raw_downloads/PolyMath/normal/train-00000-of-00001.parquet"
POLYMATH_REVISED = "/data/math-manify/raw_downloads/PolyMath/revised/train-00000-of-00001.parquet"
DEEPMATH_PARQUET_DIR = "/data/math-manify/raw_downloads/DeepMath-103K/data/"
ODA_MATH_PARQUET_DIR = "/data/math-manify/raw_downloads/ODA-Math-460k/data/"
OMNI_MATH_JSONL = "/data/math-manify/raw_downloads/Omni-MATH-2/Omni-Math-2.jsonl"
OLYMPIADBENCH_JSON = "knowledge/problem_banks/aops_instruct/eval/data/olympiadbench/test.json"
AIME_JSONL = "knowledge/problem_banks/aops_instruct/eval/data/aime24/test.jsonl"
AMO_BENCH_PARQUET = "/data/math-manify/raw_downloads/AMO-Bench/data/test-00000-of-00001.parquet"
COMPFILES_DIR = "knowledge/problem_banks/compfiles/Compfiles/"
OUTPUT_DIR = "eight-system/runs/midhint"

# === TellCore v0 关键词 ===
TELLCORE_KEYWORDS = [
    "quadratic residue", "Euler criterion", "Legendre", "quadratic character",
    "mod 4", "mod 8", "mod p", "modulo 4", "modulo 8", "modulo p", "congruen",
    "p-adic", "2-adic", "valuation",
    "local representation", "local-global", "local structure", "lift", "hensel",
]

NON_TARGET_KEYWORDS = [
    "covering system", "case analysis", "enumerate", "Cunningham",
    "Mersenne prime", "gcd", "divisibility",
]


def get_failed_problems():
    """从DB获取所有失败题，去重取runtime最长的"""
    os.environ['ARANGO_DB'] = 'xishujuzhen_math_glm52'
    from arango import ArangoClient
    client = ArangoClient(hosts='http://localhost:8529')
    db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
    aql = '''FOR r IN devin_problem_runs 
      FILTER r.status IN ["failed_no_proof","failed_token_limit","failed_tool_stall"]
      RETURN {problem_id: r.problem_id, exp_id: r.exp_id, status: r.status, runtime: r.runtime_seconds}'''
    all_runs = list(db.aql.execute(aql))
    best = {}
    for r in all_runs:
        pid = r['problem_id']
        rt = r.get('runtime') or 0
        if pid not in best or rt > (best[pid].get('runtime') or 0):
            best[pid] = r
    return best


def load_polymath():
    """加载PolyMath，返回{id: {problem, solution, answer}}"""
    import pyarrow.parquet as pq
    result = {}
    for path in [POLYMATH_PARQUET, POLYMATH_NORMAL, POLYMATH_REVISED]:
        if not os.path.exists(path):
            continue
        t = pq.read_table(path)
        for row in t.to_pylist():
            rid = row['id']
            result[rid] = {
                'problem': row.get('problem', ''),
                'solution': row.get('solution', ''),
                'answer': row.get('answer', ''),
            }
    return result


def load_deepmath():
    """加载DeepMath，返回{index: {problem, solution, answer}}"""
    import pyarrow.parquet as pq
    result = {}
    idx = 0
    for fname in sorted(os.listdir(DEEPMATH_PARQUET_DIR)):
        if not fname.endswith('.parquet'):
            continue
        t = pq.read_table(os.path.join(DEEPMATH_PARQUET_DIR, fname))
        for row in t.to_pylist():
            result[idx] = {
                'problem': row.get('question', ''),
                'solution': row.get('r1_solution_1', ''),
                'answer': row.get('final_answer', ''),
            }
            idx += 1
    return result


def load_oda_math():
    """加载ODA-Math，返回{id: {problem, solution, answer}}"""
    import pyarrow.parquet as pq
    result = {}
    for fname in sorted(os.listdir(ODA_MATH_PARQUET_DIR)):
        if not fname.endswith('.parquet'):
            continue
        t = pq.read_table(os.path.join(ODA_MATH_PARQUET_DIR, fname))
        for row in t.to_pylist():
            rid = row['id']
            result[rid] = {
                'problem': row.get('question', ''),
                'solution': row.get('response', ''),
                'answer': row.get('expected_answer', ''),
            }
    return result


def load_omni_math():
    """加载Omni-MATH-2，返回{id: {problem, solution, answer}}"""
    result = {}
    with open(OMNI_MATH_JSONL) as f:
        for line in f:
            d = json.loads(line)
            result[d['id']] = {
                'problem': d.get('problem', ''),
                'solution': d.get('solution', ''),
                'answer': d.get('answer', ''),
            }
    return result


def load_olympiadbench():
    """加载OlympiadBench，返回{id: {problem, solution, answer}}"""
    result = {}
    with open(OLYMPIADBENCH_JSON) as f:
        data = json.load(f)
    for item in data:
        sol = item.get('solution', '')
        if isinstance(sol, list):
            sol = ' '.join(sol)
        result[item['id']] = {
            'problem': item.get('question', ''),
            'solution': sol,
            'answer': item.get('final_answer', ''),
        }
    return result


def load_aime():
    """加载AIME，返回{index: {problem, solution, answer}}"""
    result = {}
    with open(AIME_JSONL) as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            result[i] = {
                'problem': d.get('problem', ''),
                'solution': d.get('solution', ''),
                'answer': d.get('answer', ''),
            }
    return result


def load_amo_bench():
    """加载AMO-Bench，返回{question_id: {problem, solution, answer}}"""
    import pyarrow.parquet as pq
    result = {}
    t = pq.read_table(AMO_BENCH_PARQUET)
    for row in t.to_pylist():
        result[row['question_id']] = {
            'problem': row.get('prompt', ''),
            'solution': row.get('solution', ''),
            'answer': row.get('answer', ''),
        }
    return result


def match_problem_to_solution(pid, polymath, deepmath, oda_math, omni_math, olympiadbench, aime, amo_bench):
    """根据problem_id格式匹配标准解答"""
    # polymath_06607 -> PolyMath id=6607
    m = re.match(r'^polymath_(\d+)$', pid)
    if m:
        rid = int(m.group(1))
        if rid in polymath:
            return polymath[rid], 'polymath'
        return None, 'polymath_not_found'

    # deepmath_103k_00012349 -> DeepMath index=12349
    m = re.match(r'^deepmath_103k_(\d+)$', pid)
    if m:
        idx = int(m.group(1))
        if idx in deepmath:
            return deepmath[idx], 'deepmath'
        return None, 'deepmath_not_found'

    # oda_math_460k_00013667 -> ODA-Math id=13667
    m = re.match(r'^oda_math_460k_(\d+)$', pid)
    if m:
        rid = int(m.group(1))
        if rid in oda_math:
            return oda_math[rid], 'oda_math'
        return None, 'oda_math_not_found'

    # omni_math_000007 -> Omni-MATH id=7
    m = re.match(r'^omni_math_(\d+)$', pid)
    if m:
        rid = int(m.group(1))
        if rid in omni_math:
            return omni_math[rid], 'omni_math'
        return None, 'omni_math_not_found'

    # mathnet_001631 -> OlympiadBench id=1631
    m = re.match(r'^mathnet_(\d+)$', pid)
    if m:
        oid = int(m.group(1))
        if oid in olympiadbench:
            return olympiadbench[oid], 'olympiadbench'
        return None, 'olympiadbench_not_found'

    # aime_2024_0012 -> AIME index=12
    m = re.match(r'^aime_2024_(\d+)$', pid)
    if m:
        idx = int(m.group(1)) - 1  # 0012 -> index 11
        if idx in aime:
            return aime[idx], 'aime'
        return None, 'aime_not_found'

    # amo_bench_00000006 -> AMO-Bench question_id=6
    m = re.match(r'^amo_bench_(\d+)$', pid)
    if m:
        qid = int(m.group(1))
        if qid in amo_bench:
            return amo_bench[qid], 'amo_bench'
        return None, 'amo_bench_not_found'

    # compfiles_imo1963p6 -> lean文件
    if pid.startswith('compfiles_'):
        return None, 'compfiles_lean'

    # fate_000375 -> 无人类解答
    if pid.startswith('fate_'):
        return None, 'fate_no_human_solution'

    return None, 'unknown_prefix'


def check_thinking_exists(exp_id):
    """检查trajectory目录是否有thinking数据"""
    traj_dir = os.path.join(TRAJECTORY_BASE, exp_id)
    if not os.path.exists(traj_dir):
        return False, 'no_traj_dir'
    for path in ['mitm/thinking_readable.txt', 'exports/conversation.json', 'sessions_db/trajectory.jsonl']:
        fpath = os.path.join(traj_dir, path)
        if os.path.exists(fpath) and os.path.getsize(fpath) > 100:
            return True, path
    return False, 'no_thinking_file'


def check_tellcore_keywords(text):
    """检查文本中是否包含TellCore关键词"""
    text_lower = text.lower()
    hits = {}
    for kw in TELLCORE_KEYWORDS:
        count = text_lower.count(kw)
        if count > 0:
            hits[kw] = count
    return hits


def phase_map():
    """阶段1：建立problem_id → 标准解答 + thinking数据的映射"""
    print("=== 阶段1：建立完整映射 ===")

    # 获取失败题
    print("  获取失败题列表...")
    failed = get_failed_problems()
    print(f"  失败题总数: {len(failed)}")

    # 加载所有题库
    print("  加载题库...")
    polymath = load_polymath()
    print(f"    PolyMath: {len(polymath)}")
    deepmath = load_deepmath()
    print(f"    DeepMath: {len(deepmath)}")
    oda_math = load_oda_math()
    print(f"    ODA-Math: {len(oda_math)}")
    omni_math = load_omni_math()
    print(f"    Omni-MATH: {len(omni_math)}")
    olympiadbench = load_olympiadbench()
    print(f"    OlympiadBench: {len(olympiadbench)}")
    aime = load_aime()
    print(f"    AIME: {len(aime)}")
    amo_bench = load_amo_bench()
    print(f"    AMO-Bench: {len(amo_bench)}")

    # 匹配
    print("  匹配标准解答...")
    mapping = []
    stats = collections.Counter()
    for pid, run_info in failed.items():
        sol_data, source = match_problem_to_solution(
            pid, polymath, deepmath, oda_math, omni_math, olympiadbench, aime, amo_bench
        )
        has_thinking, thinking_source = check_thinking_exists(run_info['exp_id'])

        entry = {
            'problem_id': pid,
            'exp_id': run_info['exp_id'],
            'status': run_info['status'],
            'runtime': run_info.get('runtime', 0),
            'solution_source': source,
            'has_solution': sol_data is not None,
            'has_thinking': has_thinking,
            'thinking_source': thinking_source,
        }

        if sol_data:
            entry['solution_length'] = len(sol_data.get('solution', ''))
            # 检查标准解答中的TellCore关键词
            sol_tellcore = check_tellcore_keywords(sol_data.get('solution', ''))
            entry['tellcore_in_solution'] = sol_tellcore
            entry['has_tellcore_in_solution'] = len(sol_tellcore) > 0

        mapping.append(entry)
        stats[source] += 1

    print(f"\n  匹配统计:")
    for s, c in stats.most_common():
        print(f"    {s}: {c}")

    # 汇总
    has_solution = sum(1 for e in mapping if e['has_solution'])
    has_thinking = sum(1 for e in mapping if e['has_thinking'])
    has_both = sum(1 for e in mapping if e['has_solution'] and e['has_thinking'])
    has_tellcore = sum(1 for e in mapping if e.get('has_tellcore_in_solution', False))
    has_tellcore_and_thinking = sum(1 for e in mapping if e.get('has_tellcore_in_solution', False) and e['has_thinking'])

    print(f"\n  汇总:")
    print(f"    有标准解答: {has_solution}")
    print(f"    有thinking数据: {has_thinking}")
    print(f"    有both: {has_both}")
    print(f"    标准解答含TellCore关键词: {has_tellcore}")
    print(f"    含TellCore + 有thinking: {has_tellcore_and_thinking}")

    # 保存映射
    output_path = os.path.join(OUTPUT_DIR, 'full_mapping.json')
    with open(output_path, 'w') as f:
        json.dump({
            'total': len(mapping),
            'has_solution': has_solution,
            'has_thinking': has_thinking,
            'has_both': has_both,
            'has_tellcore': has_tellcore,
            'has_tellcore_and_thinking': has_tellcore_and_thinking,
            'stats': dict(stats),
            'mapping': mapping,
        }, f, ensure_ascii=False, indent=2)
    print(f"\n  映射已保存到: {output_path}")

    return mapping


def phase_analyze(mapping):
    """阶段2：对有TellCore关键词+有thinking的题做对照分析"""
    print("=== 阶段2：对照分析 ===")

    # 筛选：有标准解答 + 有thinking + 标准解答含TellCore关键词
    candidates = [e for e in mapping if e.get('has_tellcore_in_solution', False) and e['has_thinking']]
    print(f"  候选题（有TellCore关键词+有thinking）: {len(candidates)}")

    # 对每道题做对照分析
    results = []
    for i, entry in enumerate(candidates):
        pid = entry['problem_id']
        exp_id = entry['exp_id']
        if (i + 1) % 50 == 0:
            print(f"  进度: {i+1}/{len(candidates)}")

        # 获取thinking文本
        thinking_text = get_thinking_text(exp_id)
        if not thinking_text:
            results.append({
                'problem_id': pid,
                'exp_id': exp_id,
                'verdict': 'NO_THINKING',
                'error': '无法获取thinking文本',
            })
            continue

        # 检查thinking中的TellCore关键词
        thinking_tellcore = check_tellcore_keywords(thinking_text)
        thinking_non_target = {}
        for kw in NON_TARGET_KEYWORDS:
            count = thinking_text.lower().count(kw)
            if count > 0:
                thinking_non_target[kw] = count

        # 判定
        sol_has_tellcore = entry.get('has_tellcore_in_solution', False)
        thinking_has_tellcore = len(thinking_tellcore) > 0

        if sol_has_tellcore and not thinking_has_tellcore:
            verdict = 'DIRECTION_ERROR'
        elif sol_has_tellcore and thinking_has_tellcore:
            verdict = 'TOKEN_LIMIT'
        else:
            verdict = 'NO_TARGET_IN_SOLUTION'

        results.append({
            'problem_id': pid,
            'exp_id': exp_id,
            'solution_source': entry['solution_source'],
            'verdict': verdict,
            'tellcore_in_thinking': thinking_tellcore,
            'non_target_in_thinking': thinking_non_target,
            'tellcore_in_solution': entry.get('tellcore_in_solution', {}),
            'thinking_length': len(thinking_text),
        })

    # 汇总
    verdicts = collections.Counter(r['verdict'] for r in results)
    print(f"\n  判定统计:")
    for v, c in verdicts.most_common():
        print(f"    {v}: {c}")

    # 保存结果
    output_path = os.path.join(OUTPUT_DIR, 'full_analysis_results.json')
    with open(output_path, 'w') as f:
        json.dump({
            'total_candidates': len(candidates),
            'verdicts': dict(verdicts),
            'results': results,
        }, f, ensure_ascii=False, indent=2)
    print(f"\n  结果已保存到: {output_path}")

    return results


def get_thinking_text(exp_id):
    """从trajectory目录获取thinking文本（4级优先级）"""
    traj_dir = os.path.join(TRAJECTORY_BASE, exp_id)
    if not os.path.exists(traj_dir):
        return None

    # 优先级1：mitm/thinking_readable.txt
    path = os.path.join(traj_dir, "mitm", "thinking_readable.txt")
    if os.path.exists(path) and os.path.getsize(path) > 100:
        with open(path) as f:
            content = f.read()
        if content.strip():
            return content

    # 优先级2：sessions_db/trajectory.jsonl
    path = os.path.join(traj_dir, "sessions_db", "trajectory.jsonl")
    if os.path.exists(path):
        parts = []
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    thinking = obj.get("thinking", "")
                    if isinstance(thinking, str) and thinking.strip():
                        parts.append(thinking)
                except json.JSONDecodeError:
                    continue
        if parts:
            seen = set()
            unique = []
            for p in parts:
                if p not in seen:
                    seen.add(p)
                    unique.append(p)
            return "\n".join(unique)

    # 优先级3：exports/conversation.json
    path = os.path.join(traj_dir, "exports", "conversation.json")
    if os.path.exists(path):
        with open(path) as f:
            conv = json.load(f)
        parts = []
        if isinstance(conv, dict):
            steps = conv.get("steps", [])
            for step in steps:
                if not isinstance(step, dict):
                    continue
                rc = step.get("reasoning_content", "")
                if isinstance(rc, str) and rc.strip():
                    parts.append(rc)
                if step.get("source") == "agent":
                    msg = step.get("message", "")
                    if isinstance(msg, str) and msg.strip():
                        parts.append(msg)
        if parts:
            return "\n".join(parts)

    # 优先级4：collector/pane_snapshot_clean.txt
    path = os.path.join(traj_dir, "collector", "pane_snapshot_clean.txt")
    if os.path.exists(path) and os.path.getsize(path) > 100:
        with open(path) as f:
            return f.read()

    return None


def main():
    parser = argparse.ArgumentParser(description="完整失败题梳理——从所有题库获取标准解答+thinking做对照分析")
    parser.add_argument("--phase", choices=['map', 'analyze', 'all'], default='all', help="执行阶段")
    args = parser.parse_args()

    if args.phase in ['map', 'all']:
        mapping = phase_map()
    else:
        # 加载已有映射
        mapping_path = os.path.join(OUTPUT_DIR, 'full_mapping.json')
        if not os.path.exists(mapping_path):
            print(f"ERROR: 需要先执行 --phase map")
            sys.exit(1)
        with open(mapping_path) as f:
            mapping = json.load(f)['mapping']

    if args.phase in ['analyze', 'all']:
        phase_analyze(mapping)


if __name__ == "__main__":
    main()
