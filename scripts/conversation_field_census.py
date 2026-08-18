#!/usr/bin/env python3
"""
conversation.json 完整字段普查（不假设schema）
================================================
递归遍历整个JSON，记录所有出现过的字段路径、类型、值样例。
用于发现schema文档可能遗漏的字段和结构变种。

用法：
    python3 conversation_field_census.py <conversation.json路径...>
    python3 conversation_field_census.py --dir <目录>  # 遍历目录下所有conversation.json
"""

import json
import sys
import os
from collections import defaultdict
from pathlib import Path


def classify_value(v):
    """对值做粗粒度分类。"""
    if v is None:
        return "null"
    if isinstance(v, bool):
        return f"bool={v}"
    if isinstance(v, int):
        return "int"
    if isinstance(v, float):
        return "float"
    if isinstance(v, str):
        if len(v) == 0:
            return "str(empty)"
        if len(v) > 10000:
            return f"str({len(v)}c,very_long)"
        return f"str({len(v)}c)"
    if isinstance(v, list):
        if len(v) == 0:
            return "list(empty)"
        return f"list[{len(v)}]"
    if isinstance(v, dict):
        return f"dict[{len(v)}keys]"
    return f"unknown:{type(v).__name__}"


def recursive_census(obj, path, field_stats, path_samples, depth=0, max_depth=20):
    """递归遍历JSON，记录每个路径的字段统计。"""
    if depth > max_depth:
        return

    if isinstance(obj, dict):
        for k, v in obj.items():
            child_path = f"{path}.{k}" if path else k
            vtype = classify_value(v)
            field_stats[child_path][vtype] += 1

            # 保存短值的样例
            if isinstance(v, (str, int, float, bool)) and len(str(v)) < 200:
                if child_path not in path_samples or len(path_samples[child_path]) < 3:
                    sample = str(v)[:150]
                    if sample not in path_samples[child_path]:
                        path_samples[child_path].append(sample)
            elif isinstance(v, list) and len(v) > 0:
                # 对list，记录第一个元素的类型
                first_type = classify_value(v[0])
                if child_path not in path_samples or len(path_samples[child_path]) < 3:
                    path_samples[child_path].append(f"[first_elem: {first_type}]")
                # 递归进list的所有元素（但限制总数避免爆炸）
                # steps[]要全部遍历（因为system/user/agent step结构不同）
                # tool_calls[]和observation.results[]只看前3个
                if "steps" in child_path or "tool_definitions" not in child_path:
                    max_items = len(v) if "steps" in child_path else min(3, len(v))
                    for i in range(max_items):
                        recursive_census(v[i], f"{child_path}[]", field_stats, path_samples, depth + 1, max_depth)
                    # 检查是否有混合类型
                    if len(v) > 1:
                        types_seen = set()
                        for item in v[:max_items]:
                            types_seen.add(classify_value(item))
                        if len(types_seen) > 1 and f"[MIXED: {','.join(types_seen)}]" not in path_samples[child_path]:
                            path_samples[child_path].append(f"[MIXED: {','.join(types_seen)}]")
                else:
                    # tool_definitions等只看前2个
                    recursive_census(v[0], f"{child_path}[]", field_stats, path_samples, depth + 1, max_depth)
                    if len(v) > 1:
                        recursive_census(v[1], f"{child_path}[]", field_stats, path_samples, depth + 1, max_depth)
            elif isinstance(v, dict):
                recursive_census(v, child_path, field_stats, path_samples, depth + 1, max_depth)

    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            # 只递归前2个元素（避免重复）
            if i < 2:
                recursive_census(item, path, field_stats, path_samples, depth + 1, max_depth)


def census_file(filepath):
    """对单个conversation.json做字段普查。"""
    with open(filepath) as f:
        data = json.load(f)

    field_stats = defaultdict(lambda: defaultdict(int))
    path_samples = defaultdict(list)

    recursive_census(data, "", field_stats, path_samples)

    return field_stats, path_samples


def main():
    files = []

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    # 解析参数
    if sys.argv[1] == "--dir":
        directory = sys.argv[2]
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 20
        # 找目录下所有conversation.json
        for root, dirs, fnames in os.walk(directory):
            for fn in fnames:
                if fn == "conversation.json":
                    files.append(os.path.join(root, fn))
                    if len(files) >= limit:
                        break
            if len(files) >= limit:
                break
        print(f"在 {directory} 下找到 {len(files)} 个 conversation.json")
    else:
        files = sys.argv[1:]

    # 汇总所有文件的字段统计
    all_field_stats = defaultdict(lambda: defaultdict(int))
    all_path_samples = defaultdict(list)
    file_count = 0
    errors = []

    for fp in files:
        if not os.path.exists(fp):
            errors.append(f"不存在: {fp}")
            continue
        try:
            fs, ps = census_file(fp)
            file_count += 1
            for path, type_counts in fs.items():
                for vtype, count in type_counts.items():
                    all_field_stats[path][vtype] += count
            for path, samples in ps.items():
                for s in samples:
                    if s not in all_path_samples[path] and len(all_path_samples[path]) < 5:
                        all_path_samples[path].append(s)
        except Exception as e:
            errors.append(f"解析失败 {fp}: {e}")

    print(f"\n成功普查 {file_count} 个文件, {len(errors)} 个错误")
    if errors:
        for e in errors[:5]:
            print(f"  {e}")

    # 输出完整字段路径树
    print(f"\n{'='*80}")
    print(f"完整字段路径普查（{len(all_field_stats)}个唯一路径）")
    print(f"{'='*80}\n")

    # 按路径排序
    sorted_paths = sorted(all_field_stats.keys())

    # 按顶层字段分组输出
    current_top = None
    for path in sorted_paths:
        top = path.split(".")[0].split("[")[0]
        if top != current_top:
            current_top = top
            print(f"\n--- {top} ---")

        type_counts = all_field_stats[path]
        total = sum(type_counts.values())
        type_str = ", ".join(f"{vtype}={count}" for vtype, count in sorted(type_counts.items(), key=lambda x: -x[1]))
        samples = all_path_samples.get(path, [])

        print(f"  {path}")
        print(f"    出现{total}次: {type_str}")
        if samples:
            for s in samples[:3]:
                print(f"    样例: {s}")

    # 特别检查：有没有不在我们schema文档中的字段
    print(f"\n{'='*80}")
    print("Schema文档已记录的字段（用于对比）")
    print(f"{'='*80}\n")

    known_paths = {
        # 顶层
        "schema_version", "session_id", "agent", "steps", "final_metrics",
        # agent
        "agent.name", "agent.version", "agent.model_name", "agent.tool_definitions", "agent.extra",
        "agent.extra.backend", "agent.extra.permission_mode",
        # final_metrics
        "final_metrics.total_prompt_tokens", "final_metrics.total_completion_tokens",
        "final_metrics.total_cached_tokens", "final_metrics.total_steps",
        # step通用
        "steps[].step_id", "steps[].timestamp", "steps[].source", "steps[].message", "steps[].extra",
        "steps[].extra.telemetry", "steps[].extra.telemetry.source", "steps[].extra.telemetry.operation",
        # agent step
        "steps[].model_name", "steps[].reasoning_content", "steps[].tool_calls", "steps[].observation",
        "steps[].metrics", "steps[].metrics.prompt_tokens", "steps[].metrics.completion_tokens",
        "steps[].metrics.cached_tokens", "steps[].extra.generation_model",
        # tool_calls
        "steps[].tool_calls[].tool_call_id", "steps[].tool_calls[].function_name", "steps[].tool_calls[].arguments",
        # observation
        "steps[].observation.results", "steps[].observation.results[].source_call_id",
        "steps[].observation.results[].content",
    }

    unknown_paths = []
    for path in sorted_paths:
        # 标准化路径（把[N]变成[]）
        norm_path = path.replace("[0]", "[]").replace("[1]", "[]").replace("[2]", "[]")
        # 检查是否在已知路径中
        found = False
        for kp in known_paths:
            if norm_path == kp or norm_path.startswith(kp + ".") or norm_path.startswith(kp + "[]"):
                found = True
                break
        if not found:
            unknown_paths.append(path)

    if unknown_paths:
        print(f"❌ 发现 {len(unknown_paths)} 个不在schema文档中的字段路径：")
        for p in unknown_paths:
            type_counts = all_field_stats[p]
            total = sum(type_counts.values())
            type_str = ", ".join(f"{vtype}={count}" for vtype, count in sorted(type_counts.items(), key=lambda x: -x[1]))
            samples = all_path_samples.get(p, [])
            print(f"  {p}")
            print(f"    出现{total}次: {type_str}")
            if samples:
                for s in samples[:2]:
                    print(f"    样例: {s}")
    else:
        print("✅ 所有字段都在schema文档中已记录")


if __name__ == "__main__":
    main()
