#!/usr/bin/env python3
"""
题海梳理进度入库脚本——扫描所有已下载的文本化数据集，
为每道题在 problem_extraction_progress 集合中建立记录，
含难度分级和优先级排序信息。

难度分级方案（difficulty_tier，1=最难，5=最易）：
  Tier 1 (最难): IMO P5/P6, USAMO P5/P6, Putnam, FATE-X, MathArena hard (diff_score>=130)
  Tier 2 (难):   IMO P3/P4, USA TST, HMMT/CMIMC/SMT 最后几题, FATE-M, omni_math difficulty>=8
  Tier 3 (中):   IMO P1/P2, USA P1-P4, AIME #13-15, olympiadbench, numina olympiads, mathnet proof
  Tier 4 (中易): AIME #1-12, AMC, hendrycks Level 5, aops_1224
  Tier 5 (易):   hendrycks Level 1-4, mathd_algebra/numbertheory, K12

优先级 = difficulty_tier（1最先处理，5最后处理）
"""

import json
import os
import re
import sys
from pathlib import Path

from arango import ArangoClient

# ---- 配置 ----
ARANGO_HOST = 'http://localhost:8529'
ARANGO_DB = 'xishujuzhen_math_glm52'
ARANGO_USER = 'root'
ARANGO_PASS = 'REDACTED-DB-PASSWORD'

PROBLEM_BANKS = Path(__file__).parent.parent / 'knowledge' / 'problem_banks'

# ---- 难度分级函数 ----

def compfiles_tier(filename: str) -> int:
    """compfiles: IMO P5/P6=1, P3/P4=2, P1/P2=3"""
    m = re.match(r'(Imo|Usa)(\d+)P(\d)', filename)
    if not m:
        return 2  # 其他竞赛默认Tier 2
    comp, year, pnum = m.group(1), int(m.group(2)), int(m.group(3))
    if comp == 'Imo':
        if pnum in (5, 6): return 1
        if pnum in (3, 4): return 2
        return 3
    else:  # Usa
        if pnum in (5, 6): return 1
        if pnum in (3, 4): return 2
        return 3

def matharena_tier(dataset: str, problem_idx: int, hard_info: dict = None) -> int:
    """MathArena: hard_problems中diff_score>=130=1, >=100=2, AIME #13-15=2, 其他=3"""
    if hard_info and hard_info.get('diff_score', 0) >= 130:
        return 1
    if hard_info and hard_info.get('diff_score', 0) >= 100:
        return 2
    # AIME #13-15
    if 'aime' in dataset.lower() and problem_idx >= 13:
        return 2
    # IMO/USAMO/Putnam/IMC
    if any(x in dataset.lower() for x in ['imo', 'usamo', 'putnam', 'imc']):
        return 2
    return 3

def omni_math_tier(difficulty: float) -> int:
    """omni_math: difficulty>=9=1, >=7=2, >=5=3, >=3=4, else=5"""
    if difficulty >= 9: return 1
    if difficulty >= 7: return 2
    if difficulty >= 5: return 3
    if difficulty >= 3: return 4
    return 5

def hendrycks_tier(level: str) -> int:
    """hendrycks MATH: Level 5=4, Level ?=3, Level 4=4, Level 3=5, Level 2=5, Level 1=5"""
    if level == 'Level 5': return 4
    if level == 'Level ?': return 3
    if level == 'Level 4': return 4
    return 5

def numina_tier(problem_type: str, solution_valid: str) -> int:
    """numina: olympiad proof题，按领域分Tier"""
    if solution_valid != 'Yes':
        return 5  # 解答不完整的跳过或低优先
    # olympiad proof题默认Tier 3
    return 3

def mathnet_tier(problem_type: str, competition: str) -> int:
    """mathnet: proof题=3, IMO/HMMT/RMM等顶级竞赛=2, Berkeley Math Circle=4"""
    comp = (competition or '').lower()
    if any(x in comp for x in ['imo', 'putnam', 'rmm', 'romanian master']):
        return 2
    if 'berkeley math circle' in comp:
        return 4
    if problem_type and 'proof' in problem_type:
        return 3
    return 4

def fate_tier(level: str) -> int:
    """FATE: FATE-X=1, FATE-M=2"""
    if level == 'FATE-X': return 1
    if level == 'FATE-M': return 2
    return 3

def aops_1224_tier() -> int:
    """aops_1224: 2024年AoPS社区题，默认Tier 4"""
    return 4

def olympiadbench_tier(subfield: str, answer_type: str) -> int:
    """olympiadbench: 奥赛题默认Tier 3"""
    return 3

def aime_tier(problem_idx: int) -> int:
    """AIME: #13-15=2, #10-12=3, #7-9=4, else=5"""
    if problem_idx >= 13: return 2
    if problem_idx >= 10: return 3
    if problem_idx >= 7: return 4
    return 5

def minif2f_tier(name: str) -> int:
    """miniF2F: imo=2, aime=3, amc=4, mathd=5"""
    name_lower = name.lower()
    if name_lower.startswith('imo_'): return 2
    if name_lower.startswith('aime_'): return 3
    if name_lower.startswith('amc'): return 4
    if 'mathd' in name_lower: return 5
    return 4

# ---- 数据集扫描函数 ----

def scan_compfiles() -> list:
    """扫描compfiles，每道题一条记录"""
    records = []
    compfiles_dir = PROBLEM_BANKS / 'compfiles' / 'Compfiles'
    if not compfiles_dir.exists():
        return records
    for f in sorted(compfiles_dir.iterdir()):
        if not f.name.endswith('.lean'):
            continue
        # 解析文件名：Imo2006P3.lean → IMO 2006 P3
        m = re.match(r'([A-Za-z]+?)(\d+)P(\d)\.lean', f.name)
        if not m:
            continue
        comp_code, year, pnum = m.group(1), int(m.group(2)), int(m.group(3))
        comp_map = {'Imo': 'IMO', 'Usa': 'USA', 'Bulgaria': 'Bulgaria', 'Singapore': 'Singapore',
                    'UK': 'UK', 'Russia': 'Russia', 'Poland': 'Poland', 'Iran': 'Iran',
                    'Canada': 'Canada', 'India': 'India', 'Hungary': 'Hungary',
                    'Romania': 'Romania', 'Egmo': 'EGMO', 'CIIM': 'CIIM'}
        comp_name = comp_map.get(comp_code, comp_code)
        problem_id = f"compfiles_{f.stem.lower()}"
        records.append({
            'problem_id': problem_id,
            'source_dataset': 'compfiles',
            'extraction_status': 'pending',
            'skip_reason': None,
            'external_ref': {
                'local_path': str(f.relative_to(PROBLEM_BANKS.parent.parent)),
                'original_index': len(records),
                'original_id_in_source': f.stem,
            },
            'metadata': {
                'domain': 'mathematics',
                'subfield': None,  # 需要从文件内容中提取
                'difficulty_source': 'competition',
                'competition_tier': f"{comp_name} P{pnum}",
                'answer_type': 'Proof',
                'has_solution': True,
                'question_length': None,
                'source_year': year,
                'source_competition': f"{comp_name} {year} P{pnum}",
            },
            'difficulty_tier': compfiles_tier(f.name),
            'priority': compfiles_tier(f.name),  # 1=最先处理
        })
    return records

def scan_matharena() -> list:
    """扫描MathArena all_problems_raw.json + hard_problems.json"""
    records = []
    raw_path = PROBLEM_BANKS / 'matharena' / 'all_problems_raw.json'
    hard_path = PROBLEM_BANKS / 'matharena' / 'hard_problems.json'
    if not raw_path.exists():
        return records
    raw = json.load(open(raw_path))
    hard_map = {}
    if hard_path.exists():
        hard = json.load(open(hard_path))
        for h in hard:
            key = (h['dataset'], h['idx'])
            hard_map[key] = h
    for item in raw:
        dataset = item['dataset']
        idx = item['idx']
        cols = item.get('columns', {})
        problem_idx = int(cols.get('problem_idx', 0))
        hard_info = hard_map.get((dataset, idx))
        problem_id = f"matharena_{dataset}_{idx:04d}"
        records.append({
            'problem_id': problem_id,
            'source_dataset': 'matharena',
            'extraction_status': 'pending',
            'skip_reason': None,
            'external_ref': {
                'local_path': str(raw_path.relative_to(PROBLEM_BANKS.parent.parent)),
                'original_index': idx,
                'original_id_in_source': f"{dataset}_{idx}",
            },
            'metadata': {
                'domain': 'mathematics',
                'subfield': cols.get('problem_type', ''),
                'difficulty_source': 'competition',
                'competition_tier': dataset,
                'answer_type': 'Numerical' if cols.get('answer') else 'Proof',
                'has_solution': bool(cols.get('answer')),
                'question_length': len(cols.get('problem', '')),
                'source_year': int(dataset.split('_')[-1]) if dataset.split('_')[-1].isdigit() else None,
                'source_competition': dataset.replace('MathArena_', ''),
            },
            'difficulty_tier': matharena_tier(dataset, problem_idx, hard_info),
            'priority': matharena_tier(dataset, problem_idx, hard_info),
            'hard_diff_score': hard_info.get('diff_score') if hard_info else None,
        })
    return records

def scan_omni_math() -> list:
    """扫描omni_math"""
    records = []
    path = PROBLEM_BANKS / 'aops_instruct' / 'eval' / 'data' / 'omni_math' / 'test.jsonl'
    if not path.exists():
        return records
    with open(path) as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            diff = d.get('difficulty', 5.0) or 5.0
            problem_id = f"omni_math_{i:06d}"
            records.append({
                'problem_id': problem_id,
                'source_dataset': 'omni_math',
                'extraction_status': 'pending',
                'skip_reason': None,
                'external_ref': {
                    'local_path': str(path.relative_to(PROBLEM_BANKS.parent.parent)),
                    'original_index': i,
                    'original_id_in_source': str(i),
                },
                'metadata': {
                    'domain': d.get('domain', [''])[0] if d.get('domain') else '',
                    'subfield': '',
                    'difficulty_source': 'competition',
                    'competition_tier': d.get('source', ''),
                    'answer_type': 'Expression',
                    'has_solution': bool(d.get('solution')),
                    'question_length': len(d.get('problem', '')),
                    'source_year': None,
                    'source_competition': d.get('source', ''),
                },
                'difficulty_tier': omni_math_tier(diff),
                'priority': omni_math_tier(diff),
                'omni_difficulty': diff,
            })
    return records

def scan_hendrycks_math() -> list:
    """扫描hendrycks MATH"""
    records = []
    base = PROBLEM_BANKS / 'hendrycks_math' / 'hf_data'
    if not base.exists():
        return records
    idx = 0
    for sub in sorted(base.iterdir()):
        if not sub.is_dir():
            continue
        for f in sorted(sub.iterdir()):
            if not f.name.endswith('.parquet'):
                continue
            import pyarrow.parquet as pq
            t = pq.read_table(str(f))
            for row in t.to_pylist():
                problem_id = f"hendrycks_math_{idx:06d}"
                records.append({
                    'problem_id': problem_id,
                    'source_dataset': 'hendrycks_math',
                    'extraction_status': 'pending',
                    'skip_reason': None,
                    'external_ref': {
                        'local_path': str(f.relative_to(PROBLEM_BANKS.parent.parent)),
                        'original_index': idx,
                        'original_id_in_source': row.get('unique_id', ''),
                    },
                    'metadata': {
                        'domain': 'mathematics',
                        'subfield': row.get('type', ''),
                        'difficulty_source': 'textbook',
                        'competition_tier': row.get('level', ''),
                        'answer_type': 'Expression',
                        'has_solution': bool(row.get('solution')),
                        'question_length': len(row.get('problem', '')),
                        'source_year': None,
                        'source_competition': 'Hendrycks MATH',
                    },
                    'difficulty_tier': hendrycks_tier(row.get('level', 'Level 3')),
                    'priority': hendrycks_tier(row.get('level', 'Level 3')),
                })
                idx += 1
    return records

def scan_numina() -> list:
    """扫描numina_math proof题"""
    records = []
    path = PROBLEM_BANKS / 'numina_math' / 'numina_proofs.jsonl'
    if not path.exists():
        return records
    with open(path) as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            valid = d.get('solution_is_valid', 'Yes')
            problem_id = f"numina_math_{i:06d}"
            tier = numina_tier(d.get('problem_type', ''), valid)
            skip = None if valid == 'Yes' else 'incomplete_solution'
            records.append({
                'problem_id': problem_id,
                'source_dataset': 'numina_math',
                'extraction_status': 'pending' if valid == 'Yes' else 'skipped',
                'skip_reason': skip,
                'external_ref': {
                    'local_path': str(path.relative_to(PROBLEM_BANKS.parent.parent)),
                    'original_index': i,
                    'original_id_in_source': str(i),
                },
                'metadata': {
                    'domain': 'mathematics',
                    'subfield': d.get('problem_type', ''),
                    'difficulty_source': 'competition',
                    'competition_tier': 'olympiad',
                    'answer_type': 'Proof',
                    'has_solution': valid == 'Yes',
                    'question_length': len(d.get('problem', '')),
                    'source_year': None,
                    'source_competition': d.get('source', 'olympiads'),
                },
                'difficulty_tier': tier,
                'priority': tier,
            })
    return records

def scan_mathnet() -> list:
    """扫描mathnet"""
    records = []
    base = PROBLEM_BANKS / 'mathnet' / 'hf_data' / 'data' / 'all'
    if not base.exists():
        return records
    import pyarrow.parquet as pq
    idx = 0
    for f in sorted(base.iterdir()):
        if not f.name.endswith('.parquet'):
            continue
        t = pq.read_table(str(f))
        for row in t.to_pylist():
            sols = row.get('solutions_markdown')
            has_sol = bool(sols and len(sols) > 0)
            problem_id = f"mathnet_{idx:06d}"
            comp = row.get('competition', '')
            ptype = row.get('problem_type', '')
            tier = mathnet_tier(ptype, comp)
            records.append({
                'problem_id': problem_id,
                'source_dataset': 'mathnet',
                'extraction_status': 'pending' if has_sol else 'skipped',
                'skip_reason': None if has_sol else 'no_solution',
                'external_ref': {
                    'local_path': str(f.relative_to(PROBLEM_BANKS.parent.parent)),
                    'original_index': idx,
                    'original_id_in_source': row.get('id', ''),
                },
                'metadata': {
                    'domain': 'mathematics',
                    'subfield': ', '.join(row.get('topics_flat', []) or []),
                    'difficulty_source': 'competition',
                    'competition_tier': comp or '',
                    'answer_type': ptype or '',
                    'has_solution': has_sol,
                    'question_length': len(row.get('problem_markdown', '')),
                    'source_year': None,
                    'source_competition': comp or '',
                    'country': row.get('country', ''),
                },
                'difficulty_tier': tier,
                'priority': tier,
            })
            idx += 1
    return records

def scan_aops_1224() -> list:
    """扫描aops_1224"""
    records = []
    path = PROBLEM_BANKS / 'aops_instruct' / 'eval' / 'data' / 'aops_1224' / 'test.jsonl'
    if not path.exists():
        return records
    with open(path) as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            problem_id = f"aops_1224_{i:06d}"
            records.append({
                'problem_id': problem_id,
                'source_dataset': 'aops_1224',
                'extraction_status': 'pending',
                'skip_reason': None,
                'external_ref': {
                    'local_path': str(path.relative_to(PROBLEM_BANKS.parent.parent)),
                    'original_index': i,
                    'original_id_in_source': str(d.get('idx', i)),
                },
                'metadata': {
                    'domain': 'mathematics',
                    'subfield': '',
                    'difficulty_source': 'community',
                    'competition_tier': 'AoPS community',
                    'answer_type': 'Expression',
                    'has_solution': bool(d.get('solution')),
                    'question_length': len(d.get('question', '')),
                    'source_year': 2024,
                    'source_competition': 'AoPS 2024',
                },
                'difficulty_tier': aops_1224_tier(),
                'priority': aops_1224_tier(),
            })
    return records

def scan_olympiadbench() -> list:
    """扫描olympiadbench"""
    records = []
    path = PROBLEM_BANKS / 'aops_instruct' / 'eval' / 'data' / 'olympiadbench' / 'test.jsonl'
    if not path.exists():
        return records
    with open(path) as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            problem_id = f"olympiadbench_{d.get('id', i):06d}"
            records.append({
                'problem_id': problem_id,
                'source_dataset': 'olympiadbench',
                'extraction_status': 'pending',
                'skip_reason': None,
                'external_ref': {
                    'local_path': str(path.relative_to(PROBLEM_BANKS.parent.parent)),
                    'original_index': i,
                    'original_id_in_source': str(d.get('id', '')),
                },
                'metadata': {
                    'domain': 'mathematics',
                    'subfield': d.get('subfield', ''),
                    'difficulty_source': 'competition',
                    'competition_tier': 'olympiad',
                    'answer_type': d.get('answer_type', ''),
                    'has_solution': bool(d.get('solution')),
                    'question_length': len(d.get('question', '')),
                    'source_year': None,
                    'source_competition': 'OlympiadBench',
                },
                'difficulty_tier': olympiadbench_tier(d.get('subfield', ''), d.get('answer_type', '')),
                'priority': olympiadbench_tier(d.get('subfield', ''), d.get('answer_type', '')),
            })
    return records

def scan_aime() -> list:
    """扫描AIME (aops_instruct eval data)"""
    records = []
    for year_dir in [(PROBLEM_BANKS / 'aops_instruct' / 'eval' / 'data' / 'aime24' / 'test.jsonl', 2024),
                     (PROBLEM_BANKS / 'aops_instruct' / 'eval' / 'data' / 'amc23' / 'test.jsonl', 2023)]:
        path, year = year_dir
        if not path.exists():
            continue
        with open(path) as f:
            for i, line in enumerate(f):
                d = json.loads(line)
                pidx = int(d.get('problem_idx', i + 1)) if 'problem_idx' in d else i + 1
                is_aime = 'aime' in str(path)
                problem_id = f"{'aime' if is_aime else 'amc'}_{year}_{i:04d}"
                tier = aime_tier(pidx) if is_aime else 5
                records.append({
                    'problem_id': problem_id,
                    'source_dataset': 'aime' if is_aime else 'amc',
                    'extraction_status': 'pending',
                    'skip_reason': None,
                    'external_ref': {
                        'local_path': str(path.relative_to(PROBLEM_BANKS.parent.parent)),
                        'original_index': i,
                        'original_id_in_source': str(pidx),
                    },
                    'metadata': {
                        'domain': 'mathematics',
                        'subfield': '',
                        'difficulty_source': 'competition',
                        'competition_tier': f"AIME {year}" if is_aime else f"AMC {year}",
                        'answer_type': 'Numerical',
                        'has_solution': bool(d.get('solution')),
                        'question_length': len(d.get('problem', '')),
                        'source_year': year,
                        'source_competition': f"AIME {year}" if is_aime else f"AMC {year}",
                    },
                    'difficulty_tier': tier,
                    'priority': tier,
                })
    return records

def scan_fate() -> list:
    """扫描FATE"""
    records = []
    base = PROBLEM_BANKS / 'fate'
    if not base.exists():
        return records
    idx = 0
    for f in sorted(base.iterdir()):
        if not (f.name.startswith('fate_batch') or f.name.startswith('fate_hard_batch')):
            continue
        if not f.name.endswith('.json'):
            continue
        data = json.load(open(f))
        for d in data:
            problem_id = f"fate_{idx:06d}"
            level = d.get('level', 'FATE-M')
            records.append({
                'problem_id': problem_id,
                'source_dataset': 'fate',
                'extraction_status': 'pending',
                'skip_reason': None,
                'external_ref': {
                    'local_path': str(f.relative_to(PROBLEM_BANKS.parent.parent)),
                    'original_index': idx,
                    'original_id_in_source': str(d.get('id', '')),
                },
                'metadata': {
                    'domain': 'mathematics',
                    'subfield': ', '.join(d.get('tag', []) or []),
                    'difficulty_source': 'research',
                    'competition_tier': level,
                    'answer_type': 'Formal Proof',
                    'has_solution': True,
                    'question_length': len(d.get('informal_statement', '')),
                    'source_year': None,
                    'source_competition': d.get('source', 'FATE'),
                },
                'difficulty_tier': fate_tier(level),
                'priority': fate_tier(level),
            })
            idx += 1
    return records

def scan_minif2f() -> list:
    """扫描miniF2F"""
    records = []
    base = PROBLEM_BANKS / 'miniF2F' / 'lean' / 'src'
    if not base.exists():
        return records
    idx = 0
    for split_file in ['test.lean', 'valid.lean']:
        path = base / split_file
        if not path.exists():
            continue
        content = path.read_text()
        for m in re.finditer(r'^theorem\s+(\S+)', content, re.MULTILINE):
            name = m.group(1)
            problem_id = f"minif2f_{idx:06d}"
            records.append({
                'problem_id': problem_id,
                'source_dataset': 'minif2f',
                'extraction_status': 'pending',
                'skip_reason': None,
                'external_ref': {
                    'local_path': str(path.relative_to(PROBLEM_BANKS.parent.parent)),
                    'original_index': idx,
                    'original_id_in_source': name,
                },
                'metadata': {
                    'domain': 'mathematics',
                    'subfield': '',
                    'difficulty_source': 'competition',
                    'competition_tier': name.split('_')[0],
                    'answer_type': 'Formal Proof',
                    'has_solution': True,
                    'question_length': None,
                    'source_year': None,
                    'source_competition': name.split('_')[0],
                    'split': split_file.replace('.lean', ''),
                },
                'difficulty_tier': minif2f_tier(name),
                'priority': minif2f_tier(name),
            })
            idx += 1
    return records

# ---- 主函数 ----

def main():
    client = ArangoClient(hosts=ARANGO_HOST)
    db = client.db(ARANGO_DB, username=ARANGO_USER, password=ARANGO_PASS)

    # 创建集合
    if 'problem_extraction_progress' not in [c['name'] for c in db.collections() if not c['name'].startswith('_')]:
        db.create_collection('problem_extraction_progress')
        print('创建集合 problem_extraction_progress')
    if 'problem_profiles' not in [c['name'] for c in db.collections() if not c['name'].startswith('_')]:
        db.create_collection('problem_profiles')
        print('创建集合 problem_profiles')

    progress = db.collection('problem_extraction_progress')

    # 清空已有记录（重新入库）
    progress.truncate()

    # 扫描所有数据集
    all_records = []
    scanners = [
        ('compfiles', scan_compfiles),
        ('matharena', scan_matharena),
        ('omni_math', scan_omni_math),
        ('hendrycks_math', scan_hendrycks_math),
        ('numina_math', scan_numina),
        ('mathnet', scan_mathnet),
        ('aops_1224', scan_aops_1224),
        ('olympiadbench', scan_olympiadbench),
        ('aime/amc', scan_aime),
        ('fate', scan_fate),
        ('minif2f', scan_minif2f),
    ]

    for name, scanner in scanners:
        print(f'扫描 {name}...', end=' ')
        try:
            recs = scanner()
            print(f'{len(recs)} 题')
            all_records.extend(recs)
        except Exception as e:
            print(f'ERROR: {e}')

    print(f'\n总计 {len(all_records)} 题')

    # 统计难度分布
    from collections import Counter
    tier_dist = Counter(r['difficulty_tier'] for r in all_records)
    status_dist = Counter(r['extraction_status'] for r in all_records)
    dataset_dist = Counter(r['source_dataset'] for r in all_records)

    print('\n难度分布:')
    for t in sorted(tier_dist.keys()):
        print(f'  Tier {t}: {tier_dist[t]} 题')
    print('\n状态分布:')
    for s, c in status_dist.most_common():
        print(f'  {s}: {c}')
    print('\n数据集分布:')
    for ds, c in dataset_dist.most_common():
        print(f'  {ds}: {c}')

    # 批量入库
    print(f'\n入库 {len(all_records)} 条记录...')
    batch_size = 500
    for i in range(0, len(all_records), batch_size):
        batch = all_records[i:i+batch_size]
        progress.import_bulk(batch)
        print(f'  入库 {i+len(batch)}/{len(all_records)}')

    # 创建索引
    print('\n创建索引...')
    try:
        db.create_index('problem_extraction_progress', ['source_dataset'], type_='persistent')
        print('  索引: source_dataset')
    except: pass
    try:
        db.create_index('problem_extraction_progress', ['extraction_status'], type_='persistent')
        print('  索引: extraction_status')
    except: pass
    try:
        db.create_index('problem_extraction_progress', ['difficulty_tier'], type_='persistent')
        print('  索引: difficulty_tier')
    except: pass
    try:
        db.create_index('problem_extraction_progress', ['priority'], type_='persistent')
        print('  索引: priority')
    except: pass

    print('\n完成！')

if __name__ == '__main__':
    main()
