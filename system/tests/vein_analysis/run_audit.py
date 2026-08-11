#!/usr/bin/env python3
"""
脉络分析审计脚本——和所有历史运行结果对比分析，确保改进是完全正向的。

用法：
    python3 system/tests/vein_analysis/run_audit.py [current_run_id]

    current_run_id: 当前要审计的运行ID（如0006）。如果不提供，自动找最新的。

产出：
    system/tests/vein_analysis/runs/{run_id}/audit_report.md
    system/tests/vein_analysis/runs/{run_id}/audit_comparison.json

审计逻辑：
    1. 加载baseline（当初4套POC的output.json）
    2. 加载所有历史运行（runs/0004/, runs/0005/, ...）
    3. 加载当前运行
    4. 对每个历史运行+baseline做逐维度对比
    5. 判定是否完全正向（无退化+有进步+adv_3不丢）

判定标准：
    完全正向 = 无退化（任何维度不得比任何历史运行退化）+ 有进步 + adv_3不丢
    部分正向 = 有进步但有退化
    退化 = 某维度比所有历史运行都差
"""

import json
import os
import sys
from collections import Counter
from datetime import datetime

# 确保在repo根目录
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(repo_root)
sys.path.insert(0, repo_root)

TEST_DIR = os.path.join(repo_root, "system", "tests", "vein_analysis")
BASELINE_DIR = os.path.join(TEST_DIR, "baseline")
RUNS_DIR = os.path.join(TEST_DIR, "runs")


# ============================================================================
# 加载产出
# ============================================================================

def load_baseline():
    """加载baseline——当初4套POC的output.json"""
    baseline = {}
    for version in ["V5", "V7", "V8", "V10"]:
        path = os.path.join(BASELINE_DIR, f"{version}_output.json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                baseline[version] = json.load(f)
    return baseline


def load_historical_runs():
    """加载所有历史运行——runs/下的每次运行"""
    runs = {}
    if not os.path.exists(RUNS_DIR):
        return runs
    for run_id in sorted(os.listdir(RUNS_DIR)):
        run_dir = os.path.join(RUNS_DIR, run_id)
        output_path = os.path.join(run_dir, "output.json")
        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8") as f:
                runs[run_id] = json.load(f)
    return runs


def load_current_run(run_id):
    """加载当前运行——从palyground目录读取"""
    run_dir = os.path.join(repo_root, "palyground", "absorb", "vein_analysis", f"{run_id}_imo2009p6")
    output_path = os.path.join(run_dir, "phase2_synthesis", "output.json")
    if not os.path.exists(output_path):
        print(f"❌ 当前运行产出不存在: {output_path}")
        sys.exit(1)
    with open(output_path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_latest_run_id():
    """自动找最新的运行ID"""
    base_dir = os.path.join(repo_root, "palyground", "absorb", "vein_analysis")
    if not os.path.exists(base_dir):
        return None
    run_ids = []
    for d in os.listdir(base_dir):
        if d.endswith("_imo2009p6"):
            run_id = d.replace("_imo2009p6", "")
            run_ids.append(run_id)
    if not run_ids:
        return None
    return sorted(run_ids)[-1]


# ============================================================================
# 提取指标
# ============================================================================

def extract_metrics(data):
    """从output.json提取审计指标"""
    traces = data.get("traces", [])
    ce = data.get("closed_elements", [])
    adv = data.get("ai_advantage_elements", [])
    ke = data.get("key_entities", [])
    mrt = data.get("meta_reflection_traces", [])

    # trace类型分布
    type_counter = Counter()
    for t in traces:
        t_type = t.get("type", "unknown")
        # 归一化类型名
        if t_type in ("局部",):
            t_type = "local"
        elif t_type in ("非局部", "nonlocal"):
            t_type = "nonlocal"
        elif t_type in ("全局",):
            t_type = "global"
        type_counter[t_type] += 1

    # adv_3检查——aₙ跳过障碍
    has_adv3 = False
    for a in adv:
        desc = a.get("description", "")
        if "跳过障碍" in desc or "跳过" in desc and "aₙ" in desc:
            has_adv3 = True
            break

    return {
        "trace_count": len(traces),
        "trace_types": dict(type_counter),
        "closed_elements_count": len(ce),
        "ai_advantage_count": len(adv),
        "key_entities_count": len(ke),
        "meta_reflection_count": len(mrt),
        "has_adv3": has_adv3,
        "ai_advantage_descriptions": [a.get("description", "") for a in adv],
        "meta_reflection_descriptions": [m.get("description", "") for m in mrt],
        "key_entity_names": [k.get("name", k.get("id", "")) for k in ke],
    }


def extract_baseline_metrics(baseline):
    """从baseline提取指标——4个版本取并集"""
    all_traces = []
    all_ce = []
    all_adv = []
    all_ke = []
    all_mrt = []

    for version, data in baseline.items():
        all_traces.extend(data.get("traces", []))
        all_ce.extend(data.get("closed_elements", []))
        all_adv.extend(data.get("ai_advantage_elements", []))
        all_ke.extend(data.get("key_entities", []))
        all_mrt.extend(data.get("meta_reflection_traces", []))

    # 去重
    def dedup_by_id(items, id_field="id"):
        seen = {}
        for item in items:
            iid = item.get(id_field, "")
            if iid and iid not in seen:
                seen[iid] = item
        return list(seen.values())

    traces_dedup = dedup_by_id(all_traces)
    ce_dedup = dedup_by_id(all_ce, "ce_id" if all_ce and "ce_id" in all_ce[0] else "id")
    adv_dedup = dedup_by_id(all_adv)
    ke_dedup = dedup_by_id(all_ke, "name" if all_ke and "name" in all_ke[0] else "id")
    mrt_dedup = dedup_by_id(all_mrt)

    # trace类型分布
    type_counter = Counter()
    for t in traces_dedup:
        t_type = t.get("type", "unknown")
        if t_type in ("局部",):
            t_type = "local"
        elif t_type in ("非局部", "nonlocal"):
            t_type = "nonlocal"
        elif t_type in ("全局",):
            t_type = "global"
        type_counter[t_type] += 1

    # adv_3检查
    has_adv3 = False
    for a in adv_dedup:
        desc = a.get("description", "")
        if "跳过障碍" in desc or "跳过" in desc and "aₙ" in desc:
            has_adv3 = True
            break

    return {
        "trace_count": len(traces_dedup),
        "trace_types": dict(type_counter),
        "closed_elements_count": len(ce_dedup),
        "ai_advantage_count": len(adv_dedup),
        "key_entities_count": len(ke_dedup),
        "meta_reflection_count": len(mrt_dedup),
        "has_adv3": has_adv3,
        "ai_advantage_descriptions": [a.get("description", "") for a in adv_dedup],
        "meta_reflection_descriptions": [m.get("description", "") for m in mrt_dedup],
        "key_entity_names": [k.get("name", k.get("id", "")) for k in ke_dedup],
    }


# ============================================================================
# 对比分析
# ============================================================================

def compare(current_metrics, historical_metrics, historical_name):
    """对比当前运行和历史运行的指标"""
    result = {
        "comparison_with": historical_name,
        "dimensions": {},
        "regressions": [],
        "improvements": [],
    }

    # 维度1: trace数量
    curr = current_metrics["trace_count"]
    hist = historical_metrics["trace_count"]
    dim = {"current": curr, "historical": hist, "ratio": curr / hist if hist > 0 else 0}
    if curr < hist * 0.8:
        dim["status"] = "退化"
        result["regressions"].append(f"trace数量: {curr} vs {hist}（<80%）")
    elif curr > hist:
        dim["status"] = "进步"
        result["improvements"].append(f"trace数量: {curr} > {hist}")
    else:
        dim["status"] = "持平"
    result["dimensions"]["trace_count"] = dim

    # 维度2: trace类型分布
    curr_types = current_metrics["trace_types"]
    hist_types = historical_metrics["trace_types"]
    all_types = set(list(curr_types.keys()) + list(hist_types.keys()))
    type_result = {}
    for t in all_types:
        c = curr_types.get(t, 0)
        h = hist_types.get(t, 0)
        status = "持平"
        if h > 0 and c < h * 0.7:
            status = "退化"
            result["regressions"].append(f"trace类型{t}: {c} vs {h}（<70%）")
        elif c > h:
            status = "进步"
            result["improvements"].append(f"trace类型{t}: {c} > {h}")
        type_result[t] = {"current": c, "historical": h, "status": status}
    result["dimensions"]["trace_types"] = type_result

    # 维度3: 闭元素完备性
    curr = current_metrics["closed_elements_count"]
    hist = historical_metrics["closed_elements_count"]
    dim = {"current": curr, "historical": hist}
    if curr < hist * 0.8:
        dim["status"] = "退化"
        result["regressions"].append(f"闭元素: {curr} vs {hist}（<80%）")
    elif curr > hist:
        dim["status"] = "进步"
        result["improvements"].append(f"闭元素: {curr} > {hist}")
    else:
        dim["status"] = "持平"
    result["dimensions"]["closed_elements"] = dim

    # 维度4: AI优势元素
    curr = current_metrics["ai_advantage_count"]
    hist = historical_metrics["ai_advantage_count"]
    dim = {"current": curr, "historical": hist}
    if curr < hist * 0.7:
        dim["status"] = "退化"
        result["regressions"].append(f"AI优势元素: {curr} vs {hist}（<70%）")
    elif curr > hist:
        dim["status"] = "进步"
        result["improvements"].append(f"AI优势元素: {curr} > {hist}")
    else:
        dim["status"] = "持平"
    result["dimensions"]["ai_advantage"] = dim

    # 维度5: 关键实体
    curr = current_metrics["key_entities_count"]
    hist = historical_metrics["key_entities_count"]
    dim = {"current": curr, "historical": hist}
    if curr < hist * 0.7:
        dim["status"] = "退化"
        result["regressions"].append(f"关键实体: {curr} vs {hist}（<70%）")
    elif curr > hist:
        dim["status"] = "进步"
        result["improvements"].append(f"关键实体: {curr} > {hist}")
    else:
        dim["status"] = "持平"
    result["dimensions"]["key_entities"] = dim

    # 维度6: 元反思trace
    curr = current_metrics["meta_reflection_count"]
    hist = historical_metrics["meta_reflection_count"]
    dim = {"current": curr, "historical": hist}
    if curr < hist:
        dim["status"] = "退化"
        result["regressions"].append(f"元反思trace: {curr} vs {hist}")
    elif curr > hist:
        dim["status"] = "进步"
        result["improvements"].append(f"元反思trace: {curr} > {hist}")
    else:
        dim["status"] = "持平"
    result["dimensions"]["meta_reflection"] = dim

    # 维度7: adv_3语义层面元模式
    dim = {"current": current_metrics["has_adv3"], "historical": historical_metrics["has_adv3"]}
    if current_metrics["has_adv3"] and not historical_metrics["has_adv3"]:
        dim["status"] = "进步"
        result["improvements"].append("adv_3: 识别出aₙ跳过障碍（历史没有）")
    elif not current_metrics["has_adv3"] and historical_metrics["has_adv3"]:
        dim["status"] = "退化"
        result["regressions"].append("adv_3: 未识别出aₙ跳过障碍（历史有）")
    else:
        dim["status"] = "持平"
    result["dimensions"]["adv3"] = dim

    return result


# ============================================================================
# 生成报告
# ============================================================================

def generate_report(run_id, current_metrics, baseline_metrics, historical_runs_metrics, comparisons):
    """生成审计报告"""
    lines = []
    lines.append(f"# 审计报告——run_id={run_id}")
    lines.append(f"\n**生成时间**：{datetime.now().isoformat()}")
    lines.append(f"\n---\n")

    # 当前运行指标
    lines.append("## 当前运行指标\n")
    lines.append(f"| 维度 | 值 |")
    lines.append(f"|---|---|")
    lines.append(f"| trace数量 | {current_metrics['trace_count']} |")
    lines.append(f"| trace类型分布 | {current_metrics['trace_types']} |")
    lines.append(f"| 闭元素数量 | {current_metrics['closed_elements_count']} |")
    lines.append(f"| AI优势元素 | {current_metrics['ai_advantage_count']} |")
    lines.append(f"| 关键实体 | {current_metrics['key_entities_count']} |")
    lines.append(f"| 元反思trace | {current_metrics['meta_reflection_count']} |")
    lines.append(f"| adv_3(aₙ跳过障碍) | {'✅' if current_metrics['has_adv3'] else '❌'} |")
    lines.append("")

    # 对比结果
    lines.append("## 逐对比结果\n")
    for comp in comparisons:
        name = comp["comparison_with"]
        lines.append(f"### vs {name}\n")
        lines.append(f"| 维度 | 当前 | 历史 | 状态 |")
        lines.append(f"|---|---|---|---|")
        for dim_name, dim_data in comp["dimensions"].items():
            if dim_name == "trace_types":
                for t, td in dim_data.items():
                    lines.append(f"| trace类型-{t} | {td['current']} | {td['historical']} | {td['status']} |")
            else:
                lines.append(f"| {dim_name} | {dim_data.get('current', '')} | {dim_data.get('historical', '')} | {dim_data.get('status', '')} |")
        if comp["regressions"]:
            lines.append(f"\n**退化点**：")
            for r in comp["regressions"]:
                lines.append(f"- {r}")
        if comp["improvements"]:
            lines.append(f"\n**进步点**：")
            for i in comp["improvements"]:
                lines.append(f"- {i}")
        lines.append("")

    # 总体判定
    all_regressions = []
    for comp in comparisons:
        for r in comp["regressions"]:
            all_regressions.append(f"[vs {comp['comparison_with']}] {r}")

    lines.append("## 总体判定\n")
    if not all_regressions and current_metrics["has_adv3"]:
        lines.append("**✅ 完全正向**——无退化，adv_3识别出\n")
    elif not all_regressions and not current_metrics["has_adv3"]:
        lines.append("**⚠️ 部分正向**——无退化但adv_3未识别出\n")
    else:
        lines.append("**❌ 有退化**——以下维度退化：\n")
        for r in all_regressions:
            lines.append(f"- {r}")
        lines.append(f"\n需要继续改进，直到和所有历史运行对比无退化。\n")

    return "\n".join(lines)


# ============================================================================
# 主函数
# ============================================================================

def main():
    # 确定当前运行ID
    if len(sys.argv) > 1:
        run_id = sys.argv[1]
    else:
        run_id = find_latest_run_id()
        if run_id is None:
            print("❌ 未找到任何运行。用法: python3 run_audit.py [run_id]")
            sys.exit(1)

    print(f"=" * 70)
    print(f"脉络分析审计——run_id={run_id}")
    print(f"=" * 70)

    # 1. 加载baseline
    print(f"\n1. 加载baseline（当初4套POC）...")
    baseline = load_baseline()
    baseline_metrics = extract_baseline_metrics(baseline)
    print(f"  baseline并集: {baseline_metrics['trace_count']}个trace, {baseline_metrics['closed_elements_count']}个闭元素")

    # 2. 加载历史运行
    print(f"\n2. 加载历史运行...")
    historical_runs = load_historical_runs()
    historical_metrics = {}
    for rid, data in historical_runs.items():
        historical_metrics[rid] = extract_metrics(data)
        print(f"  {rid}: {historical_metrics[rid]['trace_count']}个trace")

    # 3. 加载当前运行
    print(f"\n3. 加载当前运行({run_id})...")
    current_data = load_current_run(run_id)
    current_metrics = extract_metrics(current_data)
    print(f"  {run_id}: {current_metrics['trace_count']}个trace, 类型分布: {current_metrics['trace_types']}")

    # 4. 逐对比
    print(f"\n4. 逐对比分析...")
    comparisons = []

    # vs baseline
    comp = compare(current_metrics, baseline_metrics, "baseline")
    comparisons.append(comp)
    print(f"  vs baseline: {'退化' if comp['regressions'] else '无退化'}")

    # vs 每个历史运行
    for rid, metrics in historical_metrics.items():
        comp = compare(current_metrics, metrics, rid)
        comparisons.append(comp)
        print(f"  vs {rid}: {'退化' if comp['regressions'] else '无退化'}")

    # 5. 生成报告
    print(f"\n5. 生成审计报告...")
    report = generate_report(run_id, current_metrics, baseline_metrics, historical_metrics, comparisons)

    # 存档到runs/{run_id}/
    run_archive_dir = os.path.join(RUNS_DIR, run_id)
    os.makedirs(run_archive_dir, exist_ok=True)
    report_path = os.path.join(run_archive_dir, "audit_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"  报告已写入: {report_path}")

    # 存档comparison.json
    comparison_path = os.path.join(run_archive_dir, "audit_comparison.json")
    with open(comparison_path, "w", encoding="utf-8") as f:
        json.dump({
            "run_id": run_id,
            "current_metrics": current_metrics,
            "comparisons": comparisons,
        }, f, ensure_ascii=False, indent=2)
    print(f"  对比数据已写入: {comparison_path}")

    # 6. 判定
    print(f"\n6. 判定结果...")
    all_regressions = []
    for comp in comparisons:
        for r in comp["regressions"]:
            all_regressions.append(f"[vs {comp['comparison_with']}] {r}")

    if not all_regressions and current_metrics["has_adv3"]:
        print(f"  ✅ 完全正向——无退化，adv_3识别出")
    elif not all_regressions and not current_metrics["has_adv3"]:
        print(f"  ⚠️ 部分正向——无退化但adv_3未识别出")
    else:
        print(f"  ❌ 有退化——{len(all_regressions)}个退化点：")
        for r in all_regressions:
            print(f"    - {r}")


if __name__ == "__main__":
    main()
