#!/usr/bin/env python3
"""
全管线非退化审计脚本——各V各阶段历史对比

用法：
    python3 system/tests/vein_analysis/run_full_pipeline_audit.py [run_id]

产出：
    system/tests/vein_analysis/runs/{run_id}/full_pipeline_audit_report.md
    system/tests/vein_analysis/runs/{run_id}/full_pipeline_audit_data.json

3层审计结构：
    第1层：阶段1格化——各V的段数/特征数/闭元素数 vs 历史
    第2层：阶段1.5程序枚举——闭元素数和段数/特征数关系分析
    第3层：阶段2综合分析——trace/类型分布/AI优势/元反思 vs 历史
"""

import json
import os
import sys
from collections import Counter
from datetime import datetime

repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(repo_root)
sys.path.insert(0, repo_root)

TEST_DIR = os.path.join(repo_root, "system", "tests", "vein_analysis")
BASELINE_DIR = os.path.join(TEST_DIR, "baseline")
RUNS_DIR = os.path.join(TEST_DIR, "runs")
PLAYGROUND_DIR = os.path.join(repo_root, "palyground", "absorb", "vein_analysis")

VERSIONS = ["V5", "V7", "V8", "V10"]


# ============================================================================
# 数据加载
# ============================================================================

def load_baseline_grading():
    """加载baseline各V的格化数据（从output.json中提取）"""
    result = {}
    for v in VERSIONS:
        path = os.path.join(BASELINE_DIR, f"{v}_output.json")
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        segs = d.get("segments", [])
        ce = d.get("closed_elements", [])
        fc = d.get("formal_context", {})
        if isinstance(fc, dict):
            M = fc.get("M", fc.get("attributes", []))
            feat_count = len(M) if isinstance(M, list) else 0
        else:
            feat_count = 0
        result[v] = {
            "segments": len(segs),
            "features": feat_count,
            "closed_elements": len(ce),
        }
    return result


def load_historical_grading(run_id):
    """加载某次历史运行的各V格化数据"""
    result = {}
    run_dir = os.path.join(RUNS_DIR, run_id)
    for v in VERSIONS:
        data = {"segments": None, "features": None, "closed_elements": None}
        # segments
        seg_path = os.path.join(run_dir, f"{v}_segments.json")
        if os.path.exists(seg_path):
            with open(seg_path, "r", encoding="utf-8") as f:
                d = json.load(f)
            segs = d.get("segments", d if isinstance(d, list) else [])
            data["segments"] = len(segs)
        # formal_context
        fc_path = os.path.join(run_dir, f"{v}_formal_context.json")
        if os.path.exists(fc_path):
            with open(fc_path, "r", encoding="utf-8") as f:
                d = json.load(f)
            fc = d.get("formal_context", d)
            if isinstance(fc, dict):
                M = fc.get("M", fc.get("attributes", []))
                data["features"] = len(M) if isinstance(M, list) else None
        # closed_elements
        ce_path = os.path.join(run_dir, f"{v}_closed_elements.json")
        if os.path.exists(ce_path):
            with open(ce_path, "r", encoding="utf-8") as f:
                d = json.load(f)
            ce = d.get("closed_elements", d if isinstance(d, list) else [])
            data["closed_elements"] = len(ce)
        if any(v2 is not None for v2 in data.values()):
            result[v] = data
    return result


def load_historical_synthesis(run_id):
    """加载某次历史运行的综合分析结果"""
    # 先从runs目录找
    run_dir = os.path.join(RUNS_DIR, run_id)
    output_path = os.path.join(run_dir, "output.json")
    if os.path.exists(output_path):
        with open(output_path, "r", encoding="utf-8") as f:
            return json.load(f)
    # 再从palyground找
    for prefix in [f"{run_id}_imo2009p6", f"{run_id}_imo2009p6_synthtest"]:
        p = os.path.join(PLAYGROUND_DIR, prefix, "phase2_synthesis", "output.json")
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
    return None


def load_baseline_synthesis():
    """加载baseline的综合分析结果（4套POC并集）"""
    all_traces = []
    all_ce = []
    all_adv = []
    all_mrt = []
    for v in VERSIONS:
        path = os.path.join(BASELINE_DIR, f"{v}_output.json")
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        all_traces.extend(d.get("traces", []))
        all_ce.extend(d.get("closed_elements", []))
        all_adv.extend(d.get("ai_advantage_elements", []))
        all_mrt.extend(d.get("meta_reflection_traces", []))

    # 去重
    def dedup(items, id_field="id"):
        seen = set()
        result = []
        for item in items:
            key = item.get(id_field, "")
            if key and key not in seen:
                seen.add(key)
                result.append(item)
        return result

    return {
        "traces": dedup(all_traces),
        "closed_elements": dedup(all_ce),
        "ai_advantage_elements": dedup(all_adv),
        "meta_reflection_traces": dedup(all_mrt),
    }


def find_historical_run_ids():
    """找到所有历史运行ID"""
    run_ids = []
    if os.path.exists(RUNS_DIR):
        for rid in sorted(os.listdir(RUNS_DIR)):
            if rid == "baseline":
                continue
            run_dir = os.path.join(RUNS_DIR, rid)
            if os.path.isdir(run_dir) and os.path.exists(os.path.join(run_dir, "output.json")):
                run_ids.append(rid)
    return run_ids


# ============================================================================
# 指标提取
# ============================================================================

def extract_synthesis_metrics(data):
    """从综合分析output.json提取指标"""
    traces = data.get("traces", [])
    ce = data.get("closed_elements", [])
    adv = data.get("ai_advantage_elements", [])
    mrt = data.get("meta_reflection_traces", [])

    # 类型标准化——baseline用了中文类型，统一映射为英文
    TYPE_MAP = {
        "全局": "global",
        "局部": "local",
        "非局部": "nonlocal",
        "跨Case合并": "cross_case_merge",
        "跨闭元素元模式": "cross_element_meta_pattern",
    }
    type_counter = Counter()
    for t in traces:
        t_type = t.get("type", "unknown")
        t_type = TYPE_MAP.get(t_type, t_type)
        type_counter[t_type] += 1

    return {
        "trace_count": len(traces),
        "trace_types": dict(type_counter),
        "closed_elements_count": len(ce),
        "ai_advantage_count": len(adv),
        "meta_reflection_count": len(mrt),
    }


# ============================================================================
# 退化判定
# ============================================================================

def check_regression_layer1(current, historical_all, run_id):
    """第1层：格化阶段各V历史对比"""
    regressions = []
    improvements = []
    details = {}

    for v in VERSIONS:
        v_details = {}
        for metric in ["segments", "features", "closed_elements"]:
            curr_val = current.get(v, {}).get(metric)
            if curr_val is None:
                continue

            # 收集历史值
            hist_vals = []
            for h_run, h_data in historical_all.items():
                h_val = h_data.get(v, {}).get(metric)
                if h_val is not None:
                    hist_vals.append((h_run, h_val))

            if not hist_vals:
                continue

            hist_min = min(h[1] for h in hist_vals)
            hist_max = max(h[1] for h in hist_vals)
            threshold = hist_min * 0.8

            dim = {
                "current": curr_val,
                "hist_min": hist_min,
                "hist_max": hist_max,
                "threshold_80pct": threshold,
                "status": "ok",
            }

            if curr_val < threshold:
                dim["status"] = "regression"
                regressions.append(f"[{v}] {metric}: {curr_val} vs 历史最低{hist_min}（<80%）")
            elif curr_val > hist_max:
                dim["status"] = "improvement"
                improvements.append(f"[{v}] {metric}: {curr_val} > 历史最高{hist_max}")

            v_details[metric] = dim
        if v_details:
            details[v] = v_details

    return {
        "layer": "阶段1格化——各V历史对比",
        "regressions": regressions,
        "improvements": improvements,
        "details": details,
    }


def check_regression_layer3(current_metrics, historical_metrics_all):
    """第3层：综合分析历史对比"""
    regressions = []
    improvements = []
    details = {}

    # trace数量
    curr = current_metrics["trace_count"]
    hist_vals = [(name, m["trace_count"]) for name, m in historical_metrics_all.items()]
    hist_min = min(h[1] for h in hist_vals)
    threshold = hist_min * 0.8
    details["trace_count"] = {
        "current": curr, "hist_min": hist_min, "threshold_80pct": threshold,
        "status": "regression" if curr < threshold else ("improvement" if curr > max(h[1] for h in hist_vals) else "ok"),
    }
    if curr < threshold:
        regressions.append(f"trace数量: {curr} vs 历史最低{hist_min}（<80%）")
    elif curr > max(h[1] for h in hist_vals):
        improvements.append(f"trace数量: {curr} > 历史最高{max(h[1] for h in hist_vals)}")

    # trace类型分布
    type_result = {}
    curr_types = current_metrics["trace_types"]
    all_hist_types = {}
    for name, m in historical_metrics_all.items():
        for t, c in m["trace_types"].items():
            if t not in all_hist_types:
                all_hist_types[t] = []
            all_hist_types[t].append((name, c))

    for t, curr_count in curr_types.items():
        hist = all_hist_types.get(t, [])
        if hist:
            hist_min_t = min(h[1] for h in hist)
            threshold_t = hist_min_t * 0.7
            status = "regression" if curr_count < threshold_t else ("improvement" if curr_count > max(h[1] for h in hist) else "ok")
            type_result[t] = {"current": curr_count, "hist_min": hist_min_t, "threshold_70pct": threshold_t, "status": status}
            if status == "regression":
                regressions.append(f"trace类型{t}: {curr_count} vs 历史最低{hist_min_t}（<70%）")
            elif status == "improvement":
                improvements.append(f"trace类型{t}: {curr_count} > 历史最高{max(h[1] for h in hist)}")
    details["trace_types"] = type_result

    # 闭元素/AI优势/元反思
    for metric_name, threshold_pct in [("closed_elements_count", 0.8), ("ai_advantage_count", 0.7), ("meta_reflection_count", 0.7)]:
        curr = current_metrics[metric_name]
        hist_vals = [(name, m[metric_name]) for name, m in historical_metrics_all.items()]
        hist_min = min(h[1] for h in hist_vals)
        threshold = hist_min * threshold_pct
        status = "regression" if curr < threshold else ("improvement" if curr > max(h[1] for h in hist_vals) else "ok")
        details[metric_name] = {"current": curr, "hist_min": hist_min, "threshold": threshold, "status": status}
        if status == "regression":
            regressions.append(f"{metric_name}: {curr} vs 历史最低{hist_min}（<{threshold_pct*100:.0f}%）")
        elif status == "improvement":
            improvements.append(f"{metric_name}: {curr} > 历史最高{max(h[1] for h in hist_vals)}")

    return {
        "layer": "阶段2综合分析——最终结果历史对比",
        "regressions": regressions,
        "improvements": improvements,
        "details": details,
    }


# ============================================================================
# 报告生成
# ============================================================================

def generate_report(run_id, layer1_result, layer3_result, all_grading_data, all_synthesis_metrics):
    """生成全管线审计报告"""
    lines = []
    lines.append(f"# 全管线非退化审计报告——run_id={run_id}\n")
    lines.append(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # ===== 第1层 =====
    lines.append("\n## 第1层：阶段1格化——各V历史对比\n")
    lines.append("退化判定：每个指标 < 历史最低值的80% → 退化\n")

    for v in VERSIONS:
        lines.append(f"\n### {v}\n")
        v_data = all_grading_data.get(v, {})
        if not v_data:
            lines.append("（无数据）\n")
            continue

        # 表头
        run_ids = sorted(v_data.keys())
        metrics = ["segments", "features", "closed_elements"]
        metric_names = {"segments": "段数", "features": "特征数", "closed_elements": "闭元素数"}

        header = "| 指标 | " + " | ".join(run_ids) + " | 退化? |"
        separator = "|---|" + "|".join(["---"] * len(run_ids)) + "|---|"
        lines.append(header)
        lines.append(separator)

        for metric in metrics:
            row = f"| {metric_names[metric]} |"
            vals = []
            for rid in run_ids:
                val = v_data.get(rid, {}).get(metric)
                vals.append(str(val) if val is not None else "-")
            row += " | ".join(vals) + " |"

            # 退化判定
            curr_val = v_data.get(run_id, {}).get(metric)
            hist_vals = [v_data[r][metric] for r in run_ids if r != run_id and v_data.get(r, {}).get(metric) is not None]
            if curr_val is not None and hist_vals:
                hist_min = min(hist_vals)
                if curr_val < hist_min * 0.8:
                    row += " ❌退化 |"
                elif curr_val > max(hist_vals):
                    row += " ✅提升 |"
                else:
                    row += " ✅ |"
            else:
                row += " - |"
            lines.append(row)

        # 退化分析
        v_regressions = [r for r in layer1_result["regressions"] if f"[{v}]" in r]
        v_improvements = [r for r in layer1_result["improvements"] if f"[{v}]" in r]
        if v_regressions:
            lines.append(f"\n**退化点**：\n")
            for r in v_regressions:
                lines.append(f"- ❌ {r}\n")
        if v_improvements:
            lines.append(f"\n**提升点**：\n")
            for r in v_improvements:
                lines.append(f"- ✅ {r}\n")
        if not v_regressions and not v_improvements:
            lines.append(f"\n**无退化无提升**——各指标在历史范围内\n")

    # ===== 第2层 =====
    lines.append("\n## 第2层：阶段1.5程序枚举——闭元素合理性分析\n")
    lines.append("检查闭元素数和段数/特征数的关系是否合理\n")
    for v in ["V7", "V8", "V10"]:  # V5没有闭元素
        curr = all_grading_data.get(v, {}).get(run_id, {})
        seg = curr.get("segments")
        feat = curr.get("features")
        ce = curr.get("closed_elements")
        if seg and feat and ce:
            ratio = ce / (seg * feat) if seg * feat > 0 else 0
            lines.append(f"- {v}: 段{seg}×特征{feat}={seg*feat} → 闭元素{ce}（密度{ratio:.3f}）\n")
    lines.append("\n（闭元素数取决于段和特征的组合关系，密度在0.02-0.15之间为正常）\n")

    # ===== 第3层 =====
    lines.append("\n## 第3层：阶段2综合分析——最终结果历史对比\n")
    lines.append("退化判定：trace数量<80%为退化，trace类型<70%为退化\n")

    # 总表
    run_ids = sorted(all_synthesis_metrics.keys())
    lines.append("\n| 指标 | " + " | ".join(run_ids) + " |")
    lines.append("|---|" + "|".join(["---"] * len(run_ids)) + "|")

    for metric_name, display_name in [("trace_count", "trace总数"), ("closed_elements_count", "闭元素"), ("ai_advantage_count", "AI优势"), ("meta_reflection_count", "元反思")]:
        row = f"| {display_name} |"
        for rid in run_ids:
            row += f" {all_synthesis_metrics[rid][metric_name]} |"
        lines.append(row)

    # trace类型分布
    lines.append("\n**trace类型分布**：\n")
    all_types = set()
    for m in all_synthesis_metrics.values():
        all_types.update(m["trace_types"].keys())
    all_types = sorted(all_types)

    header = "| 类型 | " + " | ".join(run_ids) + " |"
    separator = "|---|" + "|".join(["---"] * len(run_ids)) + "|"
    lines.append(header)
    lines.append(separator)
    for t in all_types:
        row = f"| {t} |"
        for rid in run_ids:
            row += f" {all_synthesis_metrics[rid]['trace_types'].get(t, 0)} |"
        lines.append(row)

    # 退化/提升
    if layer3_result["regressions"]:
        lines.append(f"\n**退化点**（{len(layer3_result['regressions'])}个）：\n")
        for r in layer3_result["regressions"]:
            lines.append(f"- ❌ {r}\n")
    else:
        lines.append("\n**无退化点**\n")

    if layer3_result["improvements"]:
        lines.append(f"\n**提升点**（{len(layer3_result['improvements'])}个）：\n")
        for r in layer3_result["improvements"]:
            lines.append(f"- ✅ {r}\n")

    # ===== 综合判定 =====
    lines.append("\n## 综合判定\n")
    total_reg = len(layer1_result["regressions"]) + len(layer3_result["regressions"])
    total_imp = len(layer1_result["improvements"]) + len(layer3_result["improvements"])
    lines.append(f"- 第1层退化点：{len(layer1_result['regressions'])}个\n")
    lines.append(f"- 第1层提升点：{len(layer1_result['improvements'])}个\n")
    lines.append(f"- 第3层退化点：{len(layer3_result['regressions'])}个\n")
    lines.append(f"- 第3层提升点：{len(layer3_result['improvements'])}个\n")
    lines.append(f"- 总退化点：{total_reg}个\n")
    lines.append(f"- 总提升点：{total_imp}个\n")

    if total_reg == 0:
        lines.append("\n**✅ 验证通过——全管线无退化**\n")
    elif total_reg <= 2:
        lines.append(f"\n**⚠️ 有{total_reg}个退化点——需要分析是否为真正退化**\n")
    else:
        lines.append(f"\n**❌ 有{total_reg}个退化点——需要修复后重跑**\n")

    return "\n".join(lines)


# ============================================================================
# 主函数
# ============================================================================

def main():
    # 确定run_id
    if len(sys.argv) > 1:
        run_id = sys.argv[1]
    else:
        # 自动找最新
        run_ids = find_historical_run_ids()
        if not run_ids:
            print("❌ 没有找到任何历史运行")
            sys.exit(1)
        run_id = run_ids[-1]
        print(f"自动选择最新运行：{run_id}")

    print(f"{'='*70}")
    print(f"全管线非退化审计——run_id={run_id}")
    print(f"{'='*70}\n")

    # 1. 加载baseline格化数据
    print("1. 加载baseline格化数据...")
    baseline_grading = load_baseline_grading()
    for v in VERSIONS:
        if v in baseline_grading:
            print(f"  {v}: {baseline_grading[v]}")

    # 2. 加载历史运行格化数据
    print("\n2. 加载历史运行格化数据...")
    hist_run_ids = find_historical_run_ids()
    historical_grading = {}
    for rid in hist_run_ids:
        g = load_historical_grading(rid)
        if g:
            historical_grading[rid] = g
            print(f"  {rid}: {len(g)}个版本有数据")

    # 3. 加载当前运行格化数据
    print(f"\n3. 加载当前运行({run_id})格化数据...")
    current_grading = load_historical_grading(run_id)
    if not current_grading:
        # 尝试从palyground加载
        for prefix in [f"{run_id}_imo2009p6", f"{run_id}_imo2009p6_synthtest"]:
            base = os.path.join(PLAYGROUND_DIR, prefix)
            if os.path.exists(base):
                current_grading = {}
                for v in VERSIONS:
                    data = {"segments": None, "features": None, "closed_elements": None}
                    seg_p = os.path.join(base, "phase1_grading", v, "segments.json")
                    if os.path.exists(seg_p):
                        with open(seg_p) as f:
                            d = json.load(f)
                        data["segments"] = len(d.get("segments", d if isinstance(d, list) else []))
                    fc_p = os.path.join(base, "phase1_grading", v, "formal_context.json")
                    if os.path.exists(fc_p):
                        with open(fc_p) as f:
                            d = json.load(f)
                        fc = d.get("formal_context", d)
                        if isinstance(fc, dict):
                            M = fc.get("M", fc.get("attributes", []))
                            data["features"] = len(M) if isinstance(M, list) else None
                    ce_p = os.path.join(base, "phase1_5_enumerate", f"{v}_closed_elements.json")
                    if os.path.exists(ce_p):
                        with open(ce_p) as f:
                            d = json.load(f)
                        data["closed_elements"] = len(d.get("closed_elements", d if isinstance(d, list) else []))
                    if any(x is not None for x in data.values()):
                        current_grading[v] = data
                if current_grading:
                    break

    if current_grading:
        for v in VERSIONS:
            if v in current_grading:
                print(f"  {v}: {current_grading[v]}")
    else:
        print(f"  ⚠️ 未找到{run_id}的格化数据")

    # 4. 合并所有格化数据
    all_grading = {}
    all_grading["baseline"] = baseline_grading
    for rid, g in historical_grading.items():
        all_grading[rid] = g
    if current_grading:
        all_grading[run_id] = current_grading

    # 5. 第1层审计
    print("\n4. 第1层审计——格化阶段各V历史对比...")
    # 构建按V组织的格化数据
    grading_by_v = {}
    for rid, g in all_grading.items():
        for v in VERSIONS:
            if v in g:
                if v not in grading_by_v:
                    grading_by_v[v] = {}
                grading_by_v[v][rid] = g[v]

    layer1_result = check_regression_layer1(current_grading, {k: v for k, v in all_grading.items() if k != "baseline" and k != run_id}, run_id)
    print(f"  退化点：{len(layer1_result['regressions'])}个")
    print(f"  提升点：{len(layer1_result['improvements'])}个")

    # 6. 加载综合分析数据
    print("\n5. 加载综合分析数据...")
    baseline_synth = load_baseline_synthesis()
    all_synth = {"baseline": extract_synthesis_metrics(baseline_synth)}
    for rid in hist_run_ids:
        d = load_historical_synthesis(rid)
        if d:
            all_synth[rid] = extract_synthesis_metrics(d)
            print(f"  {rid}: trace={all_synth[rid]['trace_count']}")

    # 当前运行
    current_synth = load_historical_synthesis(run_id)
    if not current_synth:
        for prefix in [f"{run_id}_imo2009p6", f"{run_id}_imo2009p6_synthtest"]:
            p = os.path.join(PLAYGROUND_DIR, prefix, "phase2_synthesis", "output.json")
            if os.path.exists(p):
                with open(p) as f:
                    current_synth = json.load(f)
                break

    if current_synth:
        current_metrics = extract_synthesis_metrics(current_synth)
        all_synth[run_id] = current_metrics
        print(f"  {run_id}: trace={current_metrics['trace_count']}")
    else:
        print(f"  ⚠️ 未找到{run_id}的综合分析结果")

    # 7. 第3层审计
    print("\n6. 第3层审计——综合分析历史对比...")
    hist_synth_metrics = {k: v for k, v in all_synth.items() if k != "baseline" and k != run_id}
    layer3_result = check_regression_layer3(current_metrics, hist_synth_metrics)
    print(f"  退化点：{len(layer3_result['regressions'])}个")
    print(f"  提升点：{len(layer3_result['improvements'])}个")

    # 8. 生成报告
    print("\n7. 生成审计报告...")
    report = generate_report(run_id, layer1_result, layer3_result, grading_by_v, all_synth)

    # 保存
    out_dir = os.path.join(RUNS_DIR, run_id)
    os.makedirs(out_dir, exist_ok=True)
    report_path = os.path.join(out_dir, "full_pipeline_audit_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"  报告已写入：{report_path}")

    # 保存结构化数据
    data_path = os.path.join(out_dir, "full_pipeline_audit_data.json")
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump({
            "run_id": run_id,
            "timestamp": datetime.now().isoformat(),
            "layer1": layer1_result,
            "layer3": layer3_result,
            "all_grading": grading_by_v,
            "all_synthesis": all_synth,
        }, f, ensure_ascii=False, indent=2)
    print(f"  数据已写入：{data_path}")

    # 9. 判定
    print(f"\n{'='*70}")
    total_reg = len(layer1_result["regressions"]) + len(layer3_result["regressions"])
    if total_reg == 0:
        print(f"✅ 验证通过——全管线无退化")
    elif total_reg <= 2:
        print(f"⚠️ 有{total_reg}个退化点——需要分析是否为真正退化")
    else:
        print(f"❌ 有{total_reg}个退化点——需要修复后重跑")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
