#!/usr/bin/env python3
"""从 dev-docs/06 和 dev-docs/07 的 Markdown 表格提取全部 TODO，生成 todos.json。

这是初始化脚本，只需运行一次。之后用 todo.py 管理状态。
"""

import json
import re
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent.parent
DOC_06 = BASE / "dev-docs" / "06-业务工作流SOP与后续建设规划.md"
DOC_07 = BASE / "dev-docs" / "07-文献考据总体规划.md"
OUTPUT = BASE / "dev-docs" / "todos.json"

# 搜索预置映射（从 dev-docs/07 §9.2 的审查结果）
SEARCH_PRESET_MAP = {
    # Phase 13
    "13.1": ("不需要", ""),
    "13.2": ("边做边搜索", "搜索：七政四余传统论命关注哪些人生事件（婚/禄/子/疾/迁/灾），用于定义 event_type 枚举"),
    "13.3": ("不需要", ""),
    "13.4": ("不需要", ""),
    "13.5": ("不需要", ""),
    "13.6": ("不需要", ""),
    "13.7": ("不需要", ""),
    "13.8": ("不需要", ""),
    "13.9": ("不需要", ""),
    "13.10": ("不需要", ""),
    # Phase 14
    "14.1": ("先搜索", "搜索：传统'考刻定分'方法 + 现代天文反推算法。不搜索则算法设计可能脱离传统方法论"),
    "14.2": ("不需要", "统计学，标准差/极差"),
    "14.3": ("先搜索", "搜索：传统矫正 SOP 的步骤（初盘→映射事件→反推→一致性检验→收敛）。这是领域工作流，不搜索会自己编"),
    "14.4": ("不需要", ""),
    "14.5": ("不需要", ""),
    # Phase 15
    "15.1": ("先搜索", "搜索：果老星宗/星学大成中'行限'分析方法论——看什么（宫主？限内星？神煞？），先后顺序，权重。不搜索则分析逻辑是自己编的"),
    "15.2": ("不需要", "工程封装"),
    "15.3": ("不需要", "工程计算"),
    "15.4": ("不需要", ""),
    "15.5": ("不需要", ""),
    "15.6": ("不需要", ""),
    # Phase 16
    "16.1": ("先搜索", "搜索：果老星宗/星学大成中'流年'分析方法论——太岁/神煞/大限如何叠加，先后顺序。不搜索则叠加逻辑是自己编的"),
    "16.2": ("不需要", "工程封装"),
    "16.3": ("边做边搜索", "合/冲/刑/破/害是标准知识，但应核对原文确认完整性和定义。特别是'破'和'害'的精确地支关系"),
    "16.4": ("不需要", ""),
    "16.5": ("不需要", ""),
    # Phase 17
    "17.1": ("先搜索", "TODO 本身就是研究任务。搜索获取原文"),
    "17.2": ("先搜索", "同上"),
    "17.3": ("不需要", "依赖 17.1-17.2 结果"),
    "17.4": ("先搜索", "需要读原文逐条提取"),
    "17.5": ("不需要", ""),
    "17.6": ("不需要", ""),
    # Phase 18
    "18.1": ("不需要", "基于现有代码写文档"),
    "18.2": ("不需要", "基于现有代码写文档"),
    "18.3": ("不需要", "基于现有代码写文档"),
    "18.4": ("不需要", "基于现有代码写文档"),
    # Phase 19
    "19.1": ("边做边搜索", "标准概念，但应核对果老星宗中三方四正的精确定义（三合宫+对宫，还是有更多？）"),
    "19.2": ("先搜索", "搜索：西洋占星标准相位定义（主要相位列表 + orb 默认值）。七政四余本身没有相位系统，这是引入西洋概念，必须搜索确认标准"),
    "19.3": ("先搜索", "搜索：Swiss Ephemeris transit 计算 API + 推运标准方法"),
    "19.4": ("先搜索", "搜索：Solar return 计算方法 + Swiss Ephemeris 相关 API"),
    "19.5": ("先搜索", "搜索：Swiss Ephemeris 日月食 API + 传统七政四余对日月食的定义"),
    "19.6": ("边做边搜索", "核对原文中飞限半年切换的具体规则"),
    # Phase 20
    "20.1": ("先搜索", "TODO 本身就是获取文献"),
    "20.2": ("先搜索", "TODO 本身就是获取文献"),
    "20.3": ("先搜索", "TODO 本身就是获取文献"),
    "20.4": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.5": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.6": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.7": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.8": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.9": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.10": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.11": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.12": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.13": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.14": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.15": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.16": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.17": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.18": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.19": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.20": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.21": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.22": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.23": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.24": ("先搜索", "审计的本质就是搜索原文对照"),
    "20.25": ("不需要", "汇总"),
    # Phase 21
    "21.1": ("先搜索", "搜索：NASA JPL Horizons API 用法 + 获取参考数据"),
    "21.2": ("先搜索", "搜索：NASA JPL Horizons API 用法 + 获取参考数据"),
    "21.3": ("先搜索", "搜索：Lahiri ayanamsa 在 J2000.0 等历元的官方标准值"),
    "21.4": ("先搜索", "访问 Astro.com 获取参考宫位表"),
    "21.5": ("先搜索", "访问 Astro.com 获取参考宫位表"),
    "21.6": ("先搜索", "搜索：紫金山天文台 2024-2025 节气数据"),
    "21.7": ("先搜索", "搜索：权威万年历农历数据"),
    "21.8": ("先搜索", "搜索：权威万年历农历数据"),
    "21.9": ("先搜索", "访问 timeanddate.com 获取参考数据"),
    "21.10": ("不需要", "本地执行 Java"),
    "21.11": ("不需要", "本地执行 Java"),
    "21.12": ("先搜索", "搜索：已出版的四柱/纳音/神煞参考表"),
    "21.13": ("先搜索", "搜索：已出版的四柱/纳音/神煞参考表"),
    "21.14": ("先搜索", "搜索：已出版的四柱/纳音/神煞参考表"),
    "21.15": ("先搜索", "搜索：馥灵之钥或杰赫星命参考数据"),
    "21.16": ("先搜索", "搜索：权威万年历农历数据"),
    "21.17": ("不需要", "本地执行 Java"),
    "21.18": ("边做边搜索", "主体是本地 Java 对比，JPL 部分需要搜索"),
    "21.19": ("边做边搜索", "主体是本地 Java 对比，JPL 部分需要搜索"),
    "21.20": ("不需要", "汇总"),
    # Phase 22
    "22.1": ("先搜索", "TODO 本身就是文献获取"),
    "22.2": ("先搜索", "搜索：七政四余文献谱系、流派归属、互相引用关系"),
    "22.3": ("先搜索", "搜索：果老派 vs 天官派的区别，四库提要的相关论述"),
    # Phase 23
    "23.1": ("先搜索", "每项考据的本质就是搜索原文"),
    "23.2": ("不需要", "依赖 23.1 结果"),
    "23.3": ("不需要", "汇总"),
    # Phase 24
    "24.1": ("先搜索", "搜索：郑氏星案完整数据（四柱+星图+断语），d5168.com 等网站有部分"),
    "24.2": ("边做边搜索", "主体是工程验证，但差异分析时可能需要搜索原文理解差异原因"),
    "24.3": ("不需要", "依赖 24.1 数据 + 24.2 方法"),
    "24.4": ("先搜索", "获取星命溯源全文中的自述命例"),
    # Phase 25
    "25.1": ("先搜索", "搜索：授时历/康熙壬子/乾隆甲子 二十八宿宿度表"),
    "25.2": ("边做边搜索", "主体是工程实现，但 Swiss Ephemeris 岁差 API 需要查文档"),
    "25.3": ("不需要", "依赖 25.2 函数 + 24.1 数据"),
    "25.4": ("先搜索", "搜索：清史稿历狱争议 + 四余定义变更 + 觜参顺序变更"),
    "25.5": ("不需要", "依赖 25.1-25.4 结果"),
}

# 已完成的 TODO（Phase 1-12 + A3 审计）
COMPLETED_PHASES = {
    # Phase 1-12 全部完成
    "1.1": "排盘引擎补全（农历/二十八宿/升落/身宫/长生/逆顺）",
    "2.1": "命理参数表提取（庙旺/纳音/化曜/天干星曜）",
    "3.1": "格局规则引擎（134条规则 + 求值器 + 流年）",
    "4.1": "限运系统 + 升落昼夜 + 行星状态",
    "5.1": "文本渲染 + JSON 格式化",
    "6.1": "Java 对比验证 + 排序 + 端到端",
    "7.1": "CLI + 方位标记 + 模板展开",
    "8.1": "API 文档 + 回归测试",
    "11.1": "测试扩展 + 规则验证 + Web API",
    "12.1": "SVG + 大限增强 + 回归 + 文档冻结",
}

# A3 审计已完成
A3_RESULT = {
    "status": "completed",
    "result": "❌ 发现数据错误：庚辛壬癸四干化曜全部错位。根因：天嗣（天贵别名）被误当作独立化曜。已修复。",
    "commit": "ae1d865",
}


def parse_todo_table(filepath, phase_pattern):
    """从 Markdown 表格解析 TODO 行。

    phase_pattern: 匹配 Phase 编号的正则，如 r"(\d+\.\d+)"
    返回 [{id, title, dependencies, output, validation}, ...]
    """
    content = filepath.read_text(encoding="utf-8")
    todos = []
    for line in content.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        # 匹配 TODO 行：| 13.1 | 内容 | 依赖 | 产出 | 验证 |
        # 用 split 分割更可靠，因为 title 中可能含特殊字符
        parts = [p.strip() for p in line.split("|")]
        # parts[0] = "" (line starts with |), parts[-1] = "" (line ends with |)
        if len(parts) < 6:
            continue
        todo_id = parts[1]
        if not re.match(r"^\d+\.\d+$", todo_id):
            continue
        title = parts[2]
        deps = parts[3]
        output = parts[4]
        validation = parts[5] if len(parts) > 6 else ""

        # 跳过非 TODO 行（如变更记录中的年份）
        if not re.match(r"^\d+\.\d+$", todo_id):
            continue

        # 清理 title 中的 markdown 格式
        title = title.replace("`", "").strip()

        # 解析依赖
        dep_list = []
        if deps and deps != "—":
            for d in deps.split(","):
                d = d.strip()
                if d:
                    dep_list.append(d)

        todos.append({
            "id": todo_id,
            "title": title,
            "dependencies": dep_list,
            "output": output,
            "validation": validation,
        })
    return todos


def main():
    all_todos = []

    # Phase 13-21 从 dev-docs/06（只取 Phase 13-21 的 TODO，跳过其他表格行）
    todos_06 = parse_todo_table(DOC_06, r"")
    seen_ids = set()
    for t in todos_06:
        phase = t["id"].split(".")[0]
        # 只取 Phase 13-21
        if not phase.isdigit() or int(phase) < 13 or int(phase) > 21:
            continue
        if t["id"] in seen_ids:
            continue
        seen_ids.add(t["id"])

        sp, sp_note = SEARCH_PRESET_MAP.get(t["id"], ("未评估", ""))

        # A3 审计已完成
        if t["id"] == "20.4":
            status = A3_RESULT["status"]
            result = A3_RESULT["result"]
            commit = A3_RESULT["commit"]
        else:
            status = "pending"
            result = None
            commit = None

        all_todos.append({
            "id": t["id"],
            "phase": phase,
            "title": t["title"],
            "description": "",
            "dependencies": t["dependencies"],
            "output": t["output"],
            "validation": t["validation"],
            "search_preset": sp,
            "search_preset_note": sp_note,
            "status": status,
            "result": result,
            "commit": commit,
            "source": "dev-docs/06",
            "created_at": "2026-07-16",
            "updated_at": datetime.now().isoformat(timespec="seconds"),
        })

    # Phase 22-25 从 dev-docs/07（只取 Phase 22-25 的 TODO，跳过 §9.2 审查表）
    todos_07 = parse_todo_table(DOC_07, r"")
    for t in todos_07:
        phase = t["id"].split(".")[0]
        # 只取 Phase 22-25
        if not phase.isdigit() or int(phase) < 22 or int(phase) > 25:
            continue
        if t["id"] in seen_ids:
            continue
        seen_ids.add(t["id"])

        sp, sp_note = SEARCH_PRESET_MAP.get(t["id"], ("未评估", ""))
        all_todos.append({
            "id": t["id"],
            "phase": phase,
            "title": t["title"],
            "description": "",
            "dependencies": t["dependencies"],
            "output": t["output"],
            "validation": t["validation"],
            "search_preset": sp,
            "search_preset_note": sp_note,
            "status": "pending",
            "result": None,
            "commit": None,
            "source": "dev-docs/07",
            "created_at": "2026-07-16",
            "updated_at": datetime.now().isoformat(timespec="seconds"),
        })

    # 添加已完成的 Phase 1-12 概要条目
    for pid, title in COMPLETED_PHASES.items():
        phase = pid.split(".")[0]
        all_todos.append({
            "id": pid,
            "phase": phase,
            "title": title,
            "description": f"Phase {phase} 已完成，详见 dev-docs/05",
            "dependencies": [],
            "output": "代码 + 完成报告",
            "validation": "20/20 回归测试 PASS",
            "search_preset": "不需要",
            "search_preset_note": "已完成（回溯审查：Phase 1-3 应该搜索原文但没有搜）",
            "status": "completed",
            "result": "20/20 回归测试 PASS",
            "commit": None,
            "source": "dev-docs/05",
            "created_at": "2026-07-16",
            "updated_at": "2026-07-16",
        })

    # 按 ID 排序
    def sort_key(t):
        parts = t["id"].split(".")
        try:
            return (int(parts[0]), int(parts[1]))
        except (ValueError, IndexError):
            return (999, 999)

    all_todos.sort(key=sort_key)

    data = {
        "version": "1.0",
        "description": "七政四余推命系统 TODO 列表。由 dev-docs/generate_todos.py 生成，用 todo.py 管理状态。",
        "source_docs": [
            "dev-docs/06-业务工作流SOP与后续建设规划.md (Phase 13-21)",
            "dev-docs/07-文献考据总体规划.md (Phase 22-25)",
        ],
        "search_preset_legend": {
            "先搜索": "必须先搜索外部信息源才能动手。不搜索 = 必然幻觉或用错数据",
            "边做边搜索": "主体是工程任务，过程中有特定细节需要核对",
            "不需要": "纯工程任务，不需要搜索",
            "未评估": "尚未评估搜索需求",
        },
        "status_legend": {
            "pending": "待执行",
            "in_progress": "进行中",
            "completed": "已完成",
            "blocked": "被阻塞",
            "cancelled": "已取消",
        },
        "todos": all_todos,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"已生成 {OUTPUT}")
    print(f"共 {len(all_todos)} 个 TODO")
    # 统计
    from collections import Counter
    statuses = Counter(t["status"] for t in all_todos)
    presets = Counter(t["search_preset"] for t in all_todos)
    print(f"状态：{dict(statuses)}")
    print(f"搜索预置：{dict(presets)}")


if __name__ == "__main__":
    main()
