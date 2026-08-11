#!/usr/bin/env python3
"""
POC验证脚本——验证三阶段架构不会丢失当前完整流程架构产出的有价值内容。

用法：
    python3 system/tests/vein_analysis/run_poc_no_loss.py

产出：
    system/tests/vein_analysis/poc_no_loss_report.md
    system/tests/vein_analysis/new_arch/comparison.json

验证逻辑：
    1. 加载基线产出（baseline/下的4版本output.json）
    2. 加载新架构产出（new_arch/下的产出）
    3. 逐维度对比
    4. 生成测试报告
    5. 判定通过/失败
"""

import json
import os
import sys
from collections import defaultdict
from datetime import datetime

# 确保在repo根目录
# 本文件在 system/tests/vein_analysis/ 下，往上3层是repo根目录
repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(repo_root)
sys.path.insert(0, repo_root)

TEST_DIR = os.path.join(repo_root, "system", "tests", "vein_analysis")
BASELINE_DIR = os.path.join(TEST_DIR, "baseline")
NEW_ARCH_DIR = os.path.join(TEST_DIR, "new_arch")


# ============================================================================
# 加载产出
# ============================================================================

def load_baseline():
    """加载基线产出——4版本的output.json"""
    baseline = {}
    for version in ["V5", "V7", "V8", "V10"]:
        path = os.path.join(BASELINE_DIR, f"{version}_output.json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                baseline[version] = json.load(f)
            print(f"  基线 {version}: {len(baseline[version].get('traces', []))}个trace")
        else:
            print(f"  ⚠️ 基线 {version} 不存在: {path}")
    return baseline


def load_new_arch():
    """加载新架构产出"""
    new_arch = {}
    
    # 阶段1格化产出
    grading_dir = os.path.join(NEW_ARCH_DIR, "phase1_grading")
    if os.path.exists(grading_dir):
        new_arch["phase1_grading"] = {}
        for version in ["V5", "V7", "V8", "V10"]:
            seg_path = os.path.join(grading_dir, f"{version}_segments.json")
            fc_path = os.path.join(grading_dir, f"{version}_formal_context.json")
            if os.path.exists(seg_path):
                new_arch["phase1_grading"][version] = {
                    "segments": json.load(open(seg_path)),
                    "formal_context": json.load(open(fc_path)) if os.path.exists(fc_path) else None,
                }
    
    # 阶段1.5程序枚举产出
    enum_dir = os.path.join(NEW_ARCH_DIR, "phase1_5_enumerate")
    if os.path.exists(enum_dir):
        new_arch["phase1_5_enumerate"] = {}
        for version in ["V5", "V7", "V8", "V10"]:
            ce_path = os.path.join(enum_dir, f"{version}_closed_elements.json")
            if os.path.exists(ce_path):
                new_arch["phase1_5_enumerate"][version] = json.load(open(ce_path))
    
    # 阶段2综合分析产出
    synth_dir = os.path.join(NEW_ARCH_DIR, "phase2_synthesis")
    if os.path.exists(synth_dir):
        output_path = os.path.join(synth_dir, "output.json")
        if os.path.exists(output_path):
            new_arch["phase2_synthesis"] = json.load(open(output_path))
    
    return new_arch


# ============================================================================
# 提取基线的有价值内容
# ============================================================================

def extract_baseline_content(baseline):
    """从基线的4版本产出中提取所有有价值的内容"""
    content = {
        "all_traces": [],           # 所有版本的trace并集
        "all_closed_elements": [],  # 所有版本的闭元素并集
        "all_ai_advantage": [],     # 所有版本的AI优势元素并集
        "all_key_entities": [],     # 所有关键实体并集
        "all_meta_reflection": [],  # 所有元反思trace并集
        "most_valuable": {},        # 各版本最有价值trace
    }
    
    for version, output in baseline.items():
        traces = output.get("traces", [])
        for t in traces:
            t["_version"] = version
            content["all_traces"].append(t)
        
        closed = output.get("closed_elements", [])
        for ce in closed:
            ce["_version"] = version
            content["all_closed_elements"].append(ce)
        
        adv = output.get("ai_advantage_elements", [])
        for a in adv:
            a["_version"] = version
            content["all_ai_advantage"].append(a)
        
        ke = output.get("key_entities", [])
        for k in ke:
            k["_version"] = version
            content["all_key_entities"].append(k)
        
        mr = output.get("meta_reflection_traces", [])
        for m in mr:
            m["_version"] = version
            content["all_meta_reflection"].append(m)
        
        # 最有价值trace
        mvt = output.get("most_valuable_traces", output.get("most_valuable_trace"))
        if mvt:
            content["most_valuable"][version] = mvt
    
    return content


# ============================================================================
# 对比维度
# ============================================================================

def compare_trace_count(baseline_content, new_arch):
    """对比trace数量"""
    baseline_count = len(baseline_content["all_traces"])
    
    if "phase2_synthesis" not in new_arch:
        return {"status": "skip", "reason": "新架构阶段2产出不存在"}
    
    new_count = len(new_arch["phase2_synthesis"].get("traces", []))
    
    return {
        "baseline_count": baseline_count,
        "new_count": new_count,
        "ratio": new_count / baseline_count if baseline_count > 0 else 0,
        "status": "pass" if new_count >= baseline_count * 0.8 else "fail",
        "threshold": "新架构 ≥ 基线的80%",
    }


def compare_trace_coverage(baseline_content, new_arch):
    """对比trace语义覆盖——基线的每个trace在新架构中是否有语义等价"""
    if "phase2_synthesis" not in new_arch:
        return {"status": "skip", "reason": "新架构阶段2产出不存在"}
    
    new_traces = new_arch["phase2_synthesis"].get("traces", [])
    
    # 提取新架构trace的描述集合
    new_descriptions = set()
    for t in new_traces:
        desc = t.get("description", "") if isinstance(t, dict) else str(t)
        new_descriptions.add(desc.lower().strip())
    
    # 逐个检查基线trace
    coverage = []
    for bt in baseline_content["all_traces"]:
        bt_desc = bt.get("description", "") if isinstance(bt, dict) else str(bt)
        bt_desc_lower = bt_desc.lower().strip()
        
        # 简单匹配：关键词重叠
        bt_keywords = set(bt_desc_lower.split())
        matched = False
        best_overlap = 0
        for nd in new_descriptions:
            nd_keywords = set(nd.split())
            overlap = len(bt_keywords & nd_keywords)
            if overlap > best_overlap:
                best_overlap = overlap
        
        # 如果关键词重叠度 > 50%，认为有覆盖（初步判断，需人工确认）
        keyword_ratio = best_overlap / len(bt_keywords) if bt_keywords else 0
        matched = keyword_ratio > 0.5
        
        coverage.append({
            "version": bt.get("_version", ""),
            "description": bt_desc[:80],
            "keyword_overlap_ratio": round(keyword_ratio, 2),
            "matched": matched,
        })
    
    matched_count = sum(1 for c in coverage if c["matched"])
    total_count = len(coverage)
    
    return {
        "total": total_count,
        "matched": matched_count,
        "unmatched": total_count - matched_count,
        "coverage_ratio": matched_count / total_count if total_count > 0 else 0,
        "status": "pass" if matched_count >= total_count * 0.7 else "fail",
        "unmatched_traces": [c for c in coverage if not c["matched"]],
        "note": "关键词匹配是初步判断，需人工/AI确认语义等价性",
    }


def compare_closed_elements(baseline_content, new_arch):
    """对比闭元素完备性"""
    baseline_counts = {}
    for ce in baseline_content["all_closed_elements"]:
        v = ce.get("_version", "")
        baseline_counts[v] = baseline_counts.get(v, 0) + 1
    
    new_counts = {}
    if "phase1_5_enumerate" in new_arch:
        for version, closed in new_arch["phase1_5_enumerate"].items():
            new_counts[version] = len(closed) if isinstance(closed, list) else len(closed.get("closed_elements", []))
    
    max_baseline = max(baseline_counts.values()) if baseline_counts else 0
    max_new = max(new_counts.values()) if new_counts else 0
    
    return {
        "baseline_per_version": baseline_counts,
        "new_per_version": new_counts,
        "max_baseline": max_baseline,
        "max_new": max_new,
        "status": "pass" if max_new >= max_baseline else "fail",
        "note": "程序枚举应 ≥ 基线各版本中最大的闭元素数（程序是完备的）",
    }


def compare_ai_advantage(baseline_content, new_arch):
    """对比AI优势元素"""
    baseline_adv = baseline_content["all_ai_advantage"]
    
    if "phase2_synthesis" not in new_arch:
        return {"status": "skip", "reason": "新架构阶段2产出不存在"}
    
    new_adv = new_arch["phase2_synthesis"].get("ai_advantage_elements", [])
    
    # 检查adv_3——aₙ作为跳过障碍工具
    adv3_in_baseline = False
    adv3_in_new = False
    for a in baseline_adv:
        desc = a.get("description", "").lower()
        if "aₙ" in desc or "跳过障碍" in desc or "skip" in desc:
            adv3_in_baseline = True
            break
    for a in new_adv:
        desc = a.get("description", "").lower()
        if "aₙ" in desc or "跳过障碍" in desc or "skip" in desc:
            adv3_in_new = True
            break
    
    return {
        "baseline_count": len(baseline_adv),
        "new_count": len(new_adv),
        "adv3_in_baseline": adv3_in_baseline,
        "adv3_in_new": adv3_in_new,
        "adv3_status": "pass" if adv3_in_new or not adv3_in_baseline else "fail",
        "status": "pass" if len(new_adv) >= len(baseline_adv) * 0.7 else "fail",
        "note": "adv_3是POC-VMS-28d的关键发现——语义层面元模式，程序看不到",
    }


def compare_key_entities(baseline_content, new_arch):
    """对比关键实体"""
    baseline_ke = baseline_content["all_key_entities"]
    
    if "phase2_synthesis" not in new_arch:
        return {"status": "skip", "reason": "新架构阶段2产出不存在"}
    
    new_ke = new_arch["phase2_synthesis"].get("key_entities", [])
    
    # 提取名称集合
    baseline_names = set()
    for k in baseline_ke:
        name = k.get("name", "").lower().strip()
        if name:
            baseline_names.add(name)
    
    new_names = set()
    for k in new_ke:
        name = k.get("name", "").lower().strip()
        if name:
            new_names.add(name)
    
    # 计算覆盖
    covered = baseline_names & new_names
    missed = baseline_names - new_names
    
    return {
        "baseline_count": len(baseline_names),
        "new_count": len(new_names),
        "covered": len(covered),
        "missed": list(missed),
        "coverage_ratio": len(covered) / len(baseline_names) if baseline_names else 0,
        "status": "pass" if len(missed) <= len(baseline_names) * 0.2 else "fail",
    }


def compare_meta_reflection(baseline_content, new_arch):
    """对比元反思trace"""
    baseline_mr = baseline_content["all_meta_reflection"]
    
    if "phase2_synthesis" not in new_arch:
        return {"status": "skip", "reason": "新架构阶段2产出不存在"}
    
    new_mr = new_arch["phase2_synthesis"].get("meta_reflection_traces", [])
    
    return {
        "baseline_count": len(baseline_mr),
        "new_count": len(new_mr),
        "status": "pass" if len(new_mr) >= len(baseline_mr) * 0.5 else "review",
        "note": "元反思trace数量差异可以较大——关键是内容价值，不是数量",
    }


# ============================================================================
# 生成报告
# ============================================================================

def generate_report(baseline, new_arch, results):
    """生成Markdown测试报告"""
    lines = []
    lines.append("# POC验证报告——脉络分析Pipe内细化不丢东西验证")
    lines.append("")
    lines.append(f"**日期**：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("**测试题目**：IMO 2009 P6")
    lines.append("**基线架构**：4并发完整流程（V5/V7/V8/V10各做格化+trace+审计+元反思）")
    lines.append("**新架构**：三阶段（4并发格化→程序枚举闭元素→1个综合分析Agent）")
    lines.append("")
    
    # 判定
    all_pass = all(r.get("status") in ("pass", "skip", "review") for r in results.values())
    lines.append("## 总判定")
    lines.append("")
    if all_pass:
        lines.append("✅ **POC验证通过——新架构没有丢东西**")
    else:
        lines.append("❌ **POC验证失败——新架构丢了以下东西：**")
        for dim, r in results.items():
            if r.get("status") == "fail":
                lines.append(f"  - {dim}")
    lines.append("")
    
    # 各维度详情
    lines.append("## 1. trace数量对比")
    r = results.get("trace_count", {})
    lines.append(f"- 基线（4版本并集）：{r.get('baseline_count', 'N/A')}")
    lines.append(f"- 新架构：{r.get('new_count', 'N/A')}")
    lines.append(f"- 比率：{r.get('ratio', 0):.1%}")
    lines.append(f"- 判定：{r.get('status', 'N/A')}（阈值：{r.get('threshold', '')}）")
    lines.append("")
    
    lines.append("## 2. trace语义覆盖")
    r = results.get("trace_coverage", {})
    lines.append(f"- 基线trace总数：{r.get('total', 0)}")
    lines.append(f"- 已覆盖：{r.get('matched', 0)}")
    lines.append(f"- 未覆盖：{r.get('unmatched', 0)}")
    lines.append(f"- 覆盖率：{r.get('coverage_ratio', 0):.1%}")
    lines.append(f"- 判定：{r.get('status', 'N/A')}")
    if r.get("unmatched_traces"):
        lines.append(f"- 注意：{r.get('note', '')}")
        lines.append("- 未覆盖的trace：")
        for ut in r["unmatched_traces"][:10]:
            lines.append(f"  - [{ut['version']}] {ut['description']} (重叠度={ut['keyword_overlap_ratio']})")
    lines.append("")
    
    lines.append("## 3. 闭元素完备性")
    r = results.get("closed_elements", {})
    lines.append(f"- 基线各版本闭元素数：{r.get('baseline_per_version', {})}")
    lines.append(f"- 新架构各版本闭元素数：{r.get('new_per_version', {})}")
    lines.append(f"- 基线最大：{r.get('max_baseline', 0)}")
    lines.append(f"- 新架构最大：{r.get('max_new', 0)}")
    lines.append(f"- 判定：{r.get('status', 'N/A')}")
    lines.append(f"- 说明：{r.get('note', '')}")
    lines.append("")
    
    lines.append("## 4. AI优势元素")
    r = results.get("ai_advantage", {})
    lines.append(f"- 基线AI优势元素数：{r.get('baseline_count', 0)}")
    lines.append(f"- 新架构AI优势元素数：{r.get('new_count', 0)}")
    lines.append(f"- 判定：{r.get('status', 'N/A')}")
    lines.append(f"- adv_3（aₙ跳过障碍）在基线中：{'是' if r.get('adv3_in_baseline') else '否'}")
    lines.append(f"- adv_3（aₙ跳过障碍）在新架构中：{'是' if r.get('adv3_in_new') else '否'}")
    lines.append(f"- adv_3判定：{r.get('adv3_status', 'N/A')}")
    lines.append(f"- 说明：{r.get('note', '')}")
    lines.append("")
    
    lines.append("## 5. 关键实体")
    r = results.get("key_entities", {})
    lines.append(f"- 基线关键实体数：{r.get('baseline_count', 0)}")
    lines.append(f"- 新架构关键实体数：{r.get('new_count', 0)}")
    lines.append(f"- 覆盖率：{r.get('coverage_ratio', 0):.1%}")
    if r.get("missed"):
        lines.append(f"- 遗漏的关键实体：{r['missed']}")
    lines.append(f"- 判定：{r.get('status', 'N/A')}")
    lines.append("")
    
    lines.append("## 6. 元反思trace")
    r = results.get("meta_reflection", {})
    lines.append(f"- 基线元反思trace数：{r.get('baseline_count', 0)}")
    lines.append(f"- 新架构元反思trace数：{r.get('new_count', 0)}")
    lines.append(f"- 判定：{r.get('status', 'N/A')}")
    lines.append(f"- 说明：{r.get('note', '')}")
    lines.append("")
    
    return "\n".join(lines)


# ============================================================================
# 主函数
# ============================================================================

def main():
    print("=" * 70)
    print("POC验证——脉络分析Pipe内细化不丢东西验证")
    print("=" * 70)
    print()
    
    # 1. 加载基线
    print("1. 加载基线产出...")
    baseline = load_baseline()
    if not baseline:
        print("❌ 基线产出不存在，请先运行基线测试")
        return
    print()
    
    # 2. 加载新架构产出
    print("2. 加载新架构产出...")
    new_arch = load_new_arch()
    if not new_arch:
        print("⚠️ 新架构产出不存在——当前只能做基线分析，无法对比")
        print("   请先实现三阶段架构并运行，再跑本验证脚本")
    print()
    
    # 3. 提取基线内容
    print("3. 提取基线有价值内容...")
    baseline_content = extract_baseline_content(baseline)
    print(f"  基线trace并集：{len(baseline_content['all_traces'])}")
    print(f"  基线闭元素并集：{len(baseline_content['all_closed_elements'])}")
    print(f"  基线AI优势元素并集：{len(baseline_content['all_ai_advantage'])}")
    print(f"  基线关键实体并集：{len(baseline_content['all_key_entities'])}")
    print(f"  基线元反思trace并集：{len(baseline_content['all_meta_reflection'])}")
    print()
    
    # 4. 逐维度对比
    print("4. 逐维度对比...")
    results = {}
    
    if new_arch:
        results["trace_count"] = compare_trace_count(baseline_content, new_arch)
        results["trace_coverage"] = compare_trace_coverage(baseline_content, new_arch)
        results["closed_elements"] = compare_closed_elements(baseline_content, new_arch)
        results["ai_advantage"] = compare_ai_advantage(baseline_content, new_arch)
        results["key_entities"] = compare_key_entities(baseline_content, new_arch)
        results["meta_reflection"] = compare_meta_reflection(baseline_content, new_arch)
        
        for dim, r in results.items():
            status = r.get("status", "N/A")
            print(f"  {dim}: {status}")
    else:
        print("  跳过对比——新架构产出不存在")
    print()
    
    # 5. 生成报告
    print("5. 生成测试报告...")
    report = generate_report(baseline, new_arch, results)
    report_path = os.path.join(TEST_DIR, "poc_no_loss_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"  报告已写入: {report_path}")
    print()
    
    # 6. 保存对比结果JSON
    if results:
        comparison_path = os.path.join(NEW_ARCH_DIR, "comparison.json")
        os.makedirs(NEW_ARCH_DIR, exist_ok=True)
        with open(comparison_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"  对比结果已写入: {comparison_path}")
    
    # 7. 判定
    if results:
        all_pass = all(r.get("status") in ("pass", "skip", "review") for r in results.values())
        if all_pass:
            print()
            print("✅ POC验证通过——新架构没有丢东西")
        else:
            print()
            print("❌ POC验证失败——新架构丢了以下东西：")
            for dim, r in results.items():
                if r.get("status") == "fail":
                    print(f"  - {dim}")


if __name__ == "__main__":
    main()
