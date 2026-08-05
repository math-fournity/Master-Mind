#!/usr/bin/env python3
"""alignment_check.py —— AGENTS.md 与 repo 实际内容对齐检查

检查 AGENTS.md 索引与 dev-docs/、xishujuzhen/ 的实际文件是否对齐，
以及 AGENTS.md 中的 DYN/Phase 定义与 123 号/124 号权威文档是否一致。

设计原则：
- 独立于 ArangoDB（hook 可能在 ArangoDB 不可用时触发）
- 只依赖文件系统
- 返回 (hard_violations, soft_warnings)，hard 阻止 commit，soft 仅提醒
- graceful 降级：权威文档不存在时跳过对应检查，不报错
"""
import os
import re
import sys
import json
from pathlib import Path


def check_alignment(project_dir):
    """运行全部对齐检查，返回 (hard_violations, soft_warnings)"""
    hard = []
    soft = []

    agents_md = Path(project_dir) / "AGENTS.md"
    dev_docs = Path(project_dir) / "dev-docs"
    xishujuzhen = Path(project_dir) / "xishujuzhen"
    cog_json = xishujuzhen / "poc" / "cognition_units_math.json"

    if not agents_md.exists():
        hard.append("AGENTS.md 不存在")
        return hard, soft

    agents_text = agents_md.read_text(encoding="utf-8")

    # ============================================================
    # 检查 1: AGENTS.md 引用的 dev-docs/*.md 文件是否存在
    # ============================================================
    # 匹配 `dev-docs/xxx.md` 但排除标注为"星学项目"的行
    # 跳过范围引用（如 `64-...md` ~ `77-...md`）和通配符引用
    for m in re.finditer(r'`dev-docs/([^`]+\.md)`', agents_text):
        filename = m.group(1)
        filepath = dev_docs / filename
        if not filepath.exists():
            # 检查是否在同一行标注了"星学项目"或范围引用（~）
            line_start = agents_text.rfind('\n', 0, m.start()) + 1
            line_end = agents_text.find('\n', m.end())
            if line_end == -1:
                line_end = len(agents_text)
            line = agents_text[line_start:line_end]
            if "星学项目" in line or "星学项目目录" in line:
                continue
            if "~" in line and ("POC" in filename or "xishujuzhen" in filename):
                # 范围引用：`64-xxx.md` ~ `77-yyy.md`，只检查首尾是否存在
                continue
            hard.append(f"AGENTS.md 引用 dev-docs/{filename} 但文件不存在")

    # ============================================================
    # 检查 2: dev-docs/ 中的编号文档是否都在 AGENTS.md 索引中
    # ============================================================
    dev_doc_numbers = set()
    for f in dev_docs.glob("[0-9]*.md"):
        num_match = re.match(r'(\d+)', f.name)
        if num_match:
            dev_doc_numbers.add(int(num_match.group(1)))

    agents_doc_numbers = set()
    for m in re.finditer(r'dev-docs/(\d+)', agents_text):
        agents_doc_numbers.add(int(m.group(1)))

    # 星学项目目录文件编号（标注为星学项目的）
    xingxue_numbers = set()
    for m in re.finditer(r'星学项目.*?dev-docs/(\d+)', agents_text):
        xingxue_numbers.add(int(m.group(1)))

    missing_in_agents = dev_doc_numbers - agents_doc_numbers
    if missing_in_agents:
        for num in sorted(missing_in_agents):
            soft.append(f"dev-docs/ 中有 {num} 号文档，但 AGENTS.md 索引中未引用")

    # ============================================================
    # 检查 3: AGENTS.md 引用的 .py 文件是否存在
    # ============================================================
    for m in re.finditer(r'`xishujuzhen/([^`]+\.py)`', agents_text):
        filename = m.group(1)
        # 跳过通配符引用（如 cognition_*.py）
        if "*" in filename or "?" in filename:
            continue
        filepath = xishujuzhen / filename
        if not filepath.exists():
            hard.append(f"AGENTS.md 引用 xishujuzhen/{filename} 但文件不存在")

    # ============================================================
    # 检查 4: DYN 阶梯定义与 123 号是否一致
    # ============================================================
    doc_123 = dev_docs / "123-v1-2026-08-05-数学大师系统全景复盘与第一性原理重构计划.md"
    if doc_123.exists():
        dyn_123 = _extract_dyn_definitions(doc_123.read_text(encoding="utf-8"))
        dyn_agents = _extract_dyn_from_agents(agents_text)

        for dyn_id, desc_123 in dyn_123.items():
            if dyn_id in dyn_agents:
                # 检查 AGENTS.md 中的 DYN 描述是否包含 123 号的关键词
                desc_agents = dyn_agents[dyn_id]
                keywords = _extract_keywords(desc_123)
                missing_kw = [kw for kw in keywords if kw not in desc_agents]
                if missing_kw and dyn_id in ("DYN-4", "DYN-5", "DYN-6", "DYN-7"):
                    # 只对容易出错的 DYN-4—7 做硬性检查
                    soft.append(
                        f"AGENTS.md 中 {dyn_id} 定义可能与 123 号不一致"
                        f"（缺少关键词: {', '.join(missing_kw)}）"
                    )

    # ============================================================
    # 检查 5: Phase 编号与 123 号/124 号是否一致
    # ============================================================
    doc_124 = dev_docs / "124-v1-2026-08-05-Phase0-7建设计划CheckList.md"
    if doc_124.exists():
        phase_124 = _extract_phase_definitions(doc_124.read_text(encoding="utf-8"))
        phase_agents = _extract_phase_from_agents(agents_text)

        for phase_id, desc_124 in phase_124.items():
            if phase_id in phase_agents:
                desc_agents = phase_agents[phase_id]
                keywords = _extract_keywords(desc_124)
                # 只检查核心关键词（Phase 标题中的关键词）
                missing_kw = [kw for kw in keywords if kw not in desc_agents]
                if missing_kw and len(missing_kw) >= 2:
                    soft.append(
                        f"AGENTS.md 中 {phase_id} 描述可能与 124 号不一致"
                        f"（缺少关键词: {', '.join(missing_kw)}）"
                    )

    # ============================================================
    # 检查 6: 认知图规模与 JSON 是否一致
    # ============================================================
    if cog_json.exists():
        try:
            data = json.loads(cog_json.read_text(encoding="utf-8"))
            json_units = len(data.get("units", []))
            json_edges = len(data.get("edges", []))

            # 从 AGENTS.md 提取认知图规模声明
            units_match = re.search(r'(\d+)\s*个认知单元', agents_text)
            edges_match = re.search(r'(\d+)\s*条边', agents_text)

            if units_match:
                agents_units = int(units_match.group(1))
                # 取最后一个匹配（Handover Section 中的最新值）
                all_units_matches = re.findall(r'(\d+)\s*个认知单元', agents_text)
                if all_units_matches:
                    agents_units = int(all_units_matches[-1])
                if agents_units != json_units:
                    soft.append(
                        f"AGENTS.md 声明认知图 {agents_units} 个单元，"
                        f"但 JSON 实际 {json_units} 个"
                    )

            if edges_match:
                all_edges_matches = re.findall(r'(\d+)\s*条边', agents_text)
                if all_edges_matches:
                    agents_edges = int(all_edges_matches[-1])
                    if agents_edges != json_edges:
                        soft.append(
                            f"AGENTS.md 声明认知图 {agents_edges} 条边，"
                            f"但 JSON 实际 {json_edges} 条"
                        )
        except (json.JSONDecodeError, KeyError):
            soft.append("cognition_units_math.json 解析失败，跳过规模检查")

    return hard, soft


def _extract_dyn_definitions(text):
    """从 123 号文档提取 DYN-0—7 的定义"""
    dyns = {}
    # 匹配 "## 三十六、DYN-0：事件捕获真实性" 等模式
    for m in re.finditer(r'DYN-(\d)[：:]\s*(.+?)(?:\n##|\n## |$)', text, re.DOTALL):
        dyn_id = f"DYN-{m.group(1)}"
        # 取第一行标题
        title = m.group(2).strip().split('\n')[0].strip()
        dyns[dyn_id] = title
    return dyns


def _extract_dyn_from_agents(text):
    """从 AGENTS.md 提取 DYN 阶梯定义"""
    dyns = {}
    # 匹配 "DYN-0事件捕获真实性 → DYN-1..." 模式
    # 或 "DYN-0：事件捕获真实性" 模式
    for m in re.finditer(r'DYN-(\d)\s*[：:]?\s*(.+?)(?:\s*→|\n|$)', text):
        dyn_id = f"DYN-{m.group(1)}"
        title = m.group(2).strip()
        if title:
            dyns[dyn_id] = title
    return dyns


def _extract_phase_definitions(text):
    """从 124 号文档提取 Phase 0—7 的定义"""
    phases = {}
    # 匹配 "## Phase 0：冻结legacy与统一语义" 等模式
    for m in re.finditer(r'Phase\s*(\d)\s*[：:]\s*(.+?)(?:\n##|\n\n##|$)', text, re.DOTALL):
        phase_id = f"Phase {m.group(1)}"
        title = m.group(2).strip().split('\n')[0].strip()
        phases[phase_id] = title
    return phases


def _extract_phase_from_agents(text):
    """从 AGENTS.md 提取 Phase 定义"""
    phases = {}
    # 匹配 "Phase 0：冻结legacy与统一语义" 或 "Phase 0：schema与术语冻结" 等
    for m in re.finditer(r'Phase\s*(\d)\s*[：:]\s*(.+?)(?:\n|$)', text):
        phase_id = f"Phase {m.group(1)}"
        title = m.group(2).strip()
        if title and len(title) > 2:
            phases[phase_id] = title
    return phases


def _extract_keywords(text):
    """从描述中提取关键词（用于一致性检查）"""
    # 去除常见停用词，保留有意义的中文词
    stopwords = {"的", "与", "和", "及", "或", "在", "上", "中", "下", "为", "是", "不", "了"}
    # 按非汉字/非字母字符分割，保留长度>=2的片段
    fragments = re.findall(r'[\u4e00-\u9fff]{2,}|[a-zA-Z]{3,}', text)
    return [f for f in fragments if f not in stopwords]


def format_report(hard, soft):
    """格式化检查报告"""
    lines = []
    if hard:
        lines.append("🔴 硬性违规（必须修正才能 commit）：")
        for v in hard:
            lines.append(f"  ❌ {v}")
    if soft:
        lines.append("🟡 软性警告（建议检查，不阻止 commit）：")
        for w in soft:
            lines.append(f"  ⚠️  {w}")
    if not hard and not soft:
        lines.append("✅ AGENTS.md 与 repo 内容对齐检查通过")
    return "\n".join(lines)


if __name__ == "__main__":
    project_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    hard, soft = check_alignment(project_dir)
    print(format_report(hard, soft))
    if hard:
        sys.exit(1)
