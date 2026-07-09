"""铁板神数条文查找函数。

条文格式：编号：[虚岁/刻数：]条文内容
例：
  1001：47：一樹殘花，有枝複茂。
  1002：寄人廊廟，何如自立門戶。
  1004：21、22：苦雨連宵，行人泥滑。
"""
import re
import json
from pathlib import Path
from typing import List, Optional, Dict

_CORPUS_CACHE = None
_RAW_PATH = Path(__file__).parent.parent.parent.parent / 'dev-docs' / 'raw_tieban_text.md'


def _parse_entry(line: str) -> Optional[Dict]:
    """解析单条条文。

    Returns:
        {'id': int, 'ages': list|None, 'text': str} 或 None
    """
    line = line.strip()
    if not line:
        return None

    # 匹配：编号：[可选虚岁：]条文内容
    # 格式1：1001：47：一樹殘花...
    # 格式2：1002：寄人廊廟...
    # 格式3：1004：21、22：苦雨連宵...
    m = re.match(r'^(\d+)：(.+)$', line)
    if not m:
        return None

    entry_id = int(m.group(1))
    rest = m.group(2)

    # 检查是否有虚岁前缀（数字+、+数字：）
    ages = None
    age_match = re.match(r'^([\d、]+)：(.+)$', rest)
    if age_match:
        age_str = age_match.group(1)
        text = age_match.group(2)
        # 解析虚岁（可能有多个，用、分隔）
        try:
            ages = [int(a.strip()) for a in age_str.split('、')]
        except ValueError:
            # 不是虚岁，可能是其他格式（如"乙亥金榜提名方合此刻"）
            ages = None
            text = rest
    else:
        text = rest

    # 清理文本（去除末尾空白和标点）
    text = text.strip()

    return {'id': entry_id, 'ages': ages, 'text': text}


def load_corpus(raw_path: str = None) -> Dict[int, Dict]:
    """加载条文语料库。

    Args:
        raw_path: raw_tieban_text.md 路径（默认自动查找）

    Returns:
        {id: {'id': int, 'ages': list|None, 'text': str}}
    """
    global _CORPUS_CACHE
    if _CORPUS_CACHE is not None:
        return _CORPUS_CACHE

    path = Path(raw_path) if raw_path else _RAW_PATH
    if not path.exists():
        raise FileNotFoundError(f"条文库文件不存在: {path}")

    corpus = {}
    in_section = False

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            # 定位到"第五节 全文库条文 1001-13000"
            if '全文库条文' in line or '1001-13000' in line:
                in_section = True
                continue

            if in_section:
                # 跳过空行和注释
                stripped = line.strip()
                if not stripped or stripped.startswith('#') or stripped.startswith('>'):
                    continue

                # 停止条件：遇到新的大章节
                if stripped.startswith('## ') and '全文库' not in stripped:
                    break

                entry = _parse_entry(stripped)
                if entry:
                    corpus[entry['id']] = entry

    _CORPUS_CACHE = corpus
    return corpus


def get_entry(entry_id: int) -> Optional[Dict]:
    """按编号查找单条条文。"""
    corpus = load_corpus()
    return corpus.get(entry_id)


def get_entries_by_ids(ids: List[int]) -> List[Dict]:
    """按编号列表批量查找条文。"""
    corpus = load_corpus()
    return [corpus[i] for i in ids if i in corpus]


def get_entries_by_age(age: int) -> List[Dict]:
    """按虚岁查找条文（返回所有标注该虚岁的条文）。"""
    corpus = load_corpus()
    return [e for e in corpus.values() if e['ages'] and age in e['ages']]


def get_entries_by_ids_text(ids: List[int]) -> str:
    """按编号列表查找条文，返回格式化文本。"""
    entries = get_entries_by_ids(ids)
    lines = []
    for e in entries:
        age_str = f"（虚岁{'、'.join(str(a) for a in e['ages'])}）" if e['ages'] else ""
        lines.append(f"  {e['id']}：{age_str}{e['text']}")
    return '\n'.join(lines)


def get_category_entries(category: str) -> List[Dict]:
    """按分类查找条文（需要分类索引文件）。

    分类索引格式：{category: [id1, id2, ...]}
    """
    index_path = Path(__file__).parent / 'category_index.json'
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            index = json.load(f)
        ids = index.get(category, [])
        return get_entries_by_ids(ids)
    return []


def corpus_stats() -> Dict:
    """条文库统计信息。"""
    corpus = load_corpus()
    total = len(corpus)
    with_ages = sum(1 for e in corpus.values() if e['ages'])
    age_counter = {}
    for e in corpus.values():
        if e['ages']:
            for a in e['ages']:
                age_counter[a] = age_counter.get(a, 0) + 1

    return {
        'total': total,
        'with_ages': with_ages,
        'without_ages': total - with_ages,
        'min_id': min(corpus.keys()) if corpus else 0,
        'max_id': max(corpus.keys()) if corpus else 0,
        'age_distribution': dict(sorted(age_counter.items())),
    }
