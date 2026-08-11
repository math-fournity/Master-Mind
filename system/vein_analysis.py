"""
脉络分析——分析推理内容，格化脉络，识别trace。

三个步骤：
1. 分析脉络——从Thinking或SolutionRecord中分析出思维脉络
2. 格化脉络——把脉络分成段，考虑段的不同合并方式，形成所有Level视图
3. 识别trace——在各Level视图下识别可泛化的思维模式

通过 input.process 区分解题引导（"solve"）和解答吸收（"absorb"）：
- solve：从Thinking分析，可能有分叉，分叉位置本身可能是trace
- absorb：从SolutionRecord分析，通常线性，接收孤悬trace作为启发信号

═══════════════════════════════════════════════════════════════════════
实现说明
═══════════════════════════════════════════════════════════════════════

本模块实现absorb模式的4并发方案——V5/V7/V8/V9四个提示词版本并发跑同一道题，
取trace并集。

4个版本各有所长，不是简单的子集关系：
- V5独有"归纳递降三种方式"（自由直觉发现）
- V7独有"预防性vs修复性避障"+"Case间递进"（结构化约束让注意力分布不同）
- V8独有"x贯穿"+"aₙ作为工具"（跨闭元素元模式引导）
- V9独有"WLOG闭环"+"r的生命周期"（元反思步骤）

每个版本的结构化约束既是引导也是盲区，4并发取并集覆盖所有优势区。

solve模式（从推理AI的thinking分析，可能有分叉）的提示词尚未设计（TODO-1），
当前留NotImplementedError。

═══════════════════════════════════════════════════════════════════════
执行方式——脚本自动执行
═══════════════════════════════════════════════════════════════════════

本模块的vein_analysis()函数自动执行全部流程——准备工作目录、启动4个tmux
session、等待AI完成、收集产出、合并trace。

系统就是脚本（2026-08-11认知转变）。系统的运行逻辑由代码自动执行，
Master Agent的职责是开发系统代码和检查系统运行——不是在系统运行时
亲手执行循环。

vein_analysis()被调用时：
1. 准备阶段（代码自动执行）：创建工作目录、准备提示词文件和输入文件
2. 启动阶段（代码自动执行）：用subprocess启动4个tmux session
3. 等待阶段（代码自动执行）：轮询output.json是否出现，等待4个AI完成
4. 收集阶段（代码自动执行）：读取4个AI的产出JSON、运行程序验证、合并trace
5. 返回AnalysisOutput

Master Agent在系统运行时是检查者——检查tmux session状态、检查AI Agent产出、
按.ai-check checklist审计产出质量。

详细设计见：
- 技术说明书06-五代继承/02-第六代的独特贡献.md "4并发方案"节
- 技术说明书07-工程规格/01-系统架构总图.md §7 AI Agent启动规范
- 332号§8.13 4并发方案决定
"""

import os
import json
import shutil
import uuid
from datetime import datetime, timezone
from typing import Optional

from .schema import (
    AnalysisInput, AnalysisOutput,
    Trace, Vein, Segment, Branch, LevelView,
    Thinking, SolutionRecord, Problem,
)


# ============================================================================
# 常量——4并发的4个提示词版本
# ============================================================================

# 4个提示词版本，按提示词积累目录的相对路径
# 每个版本的特点见模块docstring
PROMPT_VERSIONS = ["V5", "V7", "V8", "V9"]

# 提示词文件的相对路径（相对repo根目录）
PROMPT_DIR = "第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee"
PROMPT_FILES = {
    "V5": os.path.join(PROMPT_DIR, "v5.md"),
    "V7": os.path.join(PROMPT_DIR, "v7.md"),
    "V8": os.path.join(PROMPT_DIR, "v8.md"),
    "V9": os.path.join(PROMPT_DIR, "v9.md"),
}

# 提示词中解答文本的占位符——替换为实际解答文本
SOLUTION_PLACEHOLDER = "[解答文本插入位置]"

# AGENTS.md模板文件路径（相对system/目录）
AGENTS_TEMPLATES = {
    "V5": "assets/vein_analysis/AGENTS_V5.md",
    "V7": "assets/vein_analysis/AGENTS_V7.md",
    "V8": "assets/vein_analysis/AGENTS_V8.md",
    "V9": "assets/vein_analysis/AGENTS_V9.md",
}

# 程序验证脚本路径（相对repo根目录）
VERIFY_SCRIPT = "six/verify_lattice_completeness.py"

# repo根目录——vein_analysis.py在system/下，所以根目录是上一级
# 这个值在_load_repo_root()中动态计算
_REPO_ROOT: Optional[str] = None


def _load_repo_root() -> str:
    """获取repo根目录的绝对路径。

    vein_analysis.py在 {repo_root}/system/vein_analysis.py，
    所以repo_root是本文件所在目录的上一级。
    """
    global _REPO_ROOT
    if _REPO_ROOT is None:
        _REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return _REPO_ROOT


# ============================================================================
# 主函数
# ============================================================================

def vein_analysis(input: AnalysisInput) -> AnalysisOutput:
    """脉络分析——分析推理内容，格化脉络，识别trace

    三个步骤：
    1. 分析脉络——从Thinking或SolutionRecord中分析出思维脉络
    2. 格化脉络——把脉络分成段，考虑段的不同合并方式，形成所有Level视图
    3. 识别trace——在各Level视图下识别可泛化的思维模式

    通过 input.process 区分解题引导（"solve"）和解答吸收（"absorb"）：
    - solve：从Thinking分析，可能有分叉，分叉位置本身可能是trace
    - absorb：从SolutionRecord分析，通常线性，接收孤悬trace作为启发信号

    absorb模式采用4并发方案——V5/V7/V8/V9四个提示词版本并发跑同一道题，
    取trace并集。详见模块docstring和技术说明书"4并发方案"节。

    solve模式的提示词尚未设计（TODO-1），当前留NotImplementedError。
    """
    if input.process == "absorb":
        return _vein_analysis_absorb(input)
    elif input.process == "solve":
        return _vein_analysis_solve(input)
    else:
        raise ValueError(f"未知的process类型: {input.process}，必须是 'solve' 或 'absorb'")


# ============================================================================
# absorb模式——4并发方案
# ============================================================================

def _vein_analysis_absorb(input: AnalysisInput) -> AnalysisOutput:
    """absorb模式的脉络分析——4并发方案

    流程（全部由代码自动执行）：
    1. 准备阶段——创建4个工作目录，准备提示词文件和输入文件
    2. 启动阶段——用subprocess启动4个tmux session（devin cli实例）
    3. 等待阶段——轮询4个output.json是否出现，等待4个AI完成
    4. 收集阶段——读取4个AI的产出JSON、运行程序验证、合并trace
    5. 返回AnalysisOutput

    系统就是脚本——启动、等待、收集全部由代码自动执行。
    Master Agent在系统运行时是检查者，不参与循环执行。
    """
    # 验证输入
    if input.solution_record is None:
        raise ValueError("absorb模式需要input.solution_record")

    record = input.solution_record
    problem_id = record.problem.problem_id
    solution_text = record.solution_text
    problem_text = record.problem.problem_text

    # 构造解答文本块——插入到提示词中
    solution_block = f"""**题目**：

{problem_text}

**解答**：

{solution_text}"""

    # 如果有孤悬trace启发信号，附加到解答文本块后面
    if input.orphan_traces:
        orphan_block = _format_orphan_traces(input.orphan_traces)
        solution_block += f"\n\n**孤悬trace启发信号**（来自解题引导，请重点关注这些模式在外部解答中的体现）：\n\n{orphan_block}"

    # 创建工作目录
    workdir_base = _create_workdir_base("absorb", problem_id)

    # 准备4个版本的工作目录
    prepared_dirs = {}
    for version in PROMPT_VERSIONS:
        version_dir = _prepare_version_workdir(
            workdir_base, version, solution_block, problem_id
        )
        prepared_dirs[version] = version_dir

    # 写meta.json——记录本次脉络分析的元数据
    meta = {
        "process": "absorb",
        "problem_id": problem_id,
        "record_id": record.record_id,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "versions": PROMPT_VERSIONS,
        "version_workdirs": {v: str(d) for v, d in prepared_dirs.items()},
        "has_orphan_traces": input.orphan_traces is not None and len(input.orphan_traces) > 0,
        "status": "prepared",  # prepared → running → completed
    }
    meta_path = os.path.join(workdir_base, "meta.json")
    _write_json(meta_path, meta)

    # 启动4个tmux session
    session_names = {}
    for version in PROMPT_VERSIONS:
        vdir = prepared_dirs[version]
        session_name = f"absorb-vein_analysis-{problem_id}-{version}"
        session_names[version] = session_name

        # 短启动提示词——让AI加载AGENTS.md和prompt.md，从input.md读取解答文本
        launch_prompt = (
            f"先加载 {vdir}/AGENTS.md 了解你的角色和约束，"
            f"然后加载 {vdir}/prompt.md 中的提示词，"
            f"读取 {vdir}/input.md 中的解答文本作为分析对象，"
            f"按提示词要求工作，完成后把产出写入 {vdir}/output.json 和 {vdir}/output.md"
        )

        # 用subprocess启动tmux session
        import subprocess
        cmd = [
            "tmux", "new-session", "-d", "-s", session_name,
            f"cd {vdir} && devin '{launch_prompt}'"
        ]
        print(f"启动 {version}: tmux session={session_name}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"⚠️ {version} tmux启动失败: {result.stderr}")
        else:
            print(f"✅ {version} tmux启动成功")

    # 更新meta状态
    meta["status"] = "running"
    meta["session_names"] = session_names
    _write_json(meta_path, meta)

    print()
    print(f"4个AI Agent已启动，等待完成...")
    print(f"工作目录: {workdir_base}")
    print(f"检查状态: tmux list-sessions | grep absorb-vein_analysis-{problem_id}")
    print()

    # 等待4个AI完成——轮询output.json是否出现
    output = _wait_and_collect(workdir_base, prepared_dirs, meta, meta_path)
    return output


def _wait_and_collect(workdir_base: str, prepared_dirs: dict,
                       meta: dict, meta_path: str) -> AnalysisOutput:
    """等待4个AI完成并收集产出

    轮询4个版本的output.json是否出现。全部出现后调用collect_vein_analysis_output。
    设置超时——如果超过timeout秒还没全部完成，返回已完成的版本的产出。
    """
    import time

    timeout = 3600  # 60分钟超时
    poll_interval = 30  # 每30秒检查一次
    started = time.time()

    while True:
        elapsed = time.time() - started
        if elapsed > timeout:
            print(f"⚠️ 超时({timeout}秒)，停止等待，收集已完成的版本")
            break

        all_done = True
        status = []
        for version, vdir in prepared_dirs.items():
            output_path = os.path.join(vdir, "output.json")
            done = os.path.exists(output_path)
            status.append(f"{version}: {'✅' if done else '⏳'}")
            if not done:
                all_done = False

        print(f"[{int(elapsed)}s] {' '.join(status)}")

        if all_done:
            print("✅ 4个AI全部完成")
            break

        time.sleep(poll_interval)

    # 收集产出
    return collect_vein_analysis_output(workdir_base)


def collect_vein_analysis_output(workdir_base: str) -> AnalysisOutput:
    """收集4并发脉络分析的产出——在4个AI Agent都完成后调用

    流程：
    1. 读取4个版本的output.json
    2. 对V9的output.json运行verify_lattice_completeness.py
    3. 合并4个版本的trace（取并集）
    4. 解析成AnalysisOutput返回

    Args:
        workdir_base: 工作目录基路径（_vein_analysis_absorb创建的workdir_base）

    Returns:
        AnalysisOutput——包含4并发并集后的traces/veins/level_views
    """
    workdir_base = os.path.abspath(workdir_base)
    meta_path = os.path.join(workdir_base, "meta.json")

    # 读取meta
    meta = _read_json(meta_path)
    problem_id = meta["problem_id"]
    versions = meta["versions"]
    version_workdirs = {v: os.path.abspath(p) for v, p in meta["version_workdirs"].items()}

    # 1. 读取4个版本的产出
    version_outputs = {}
    for version in versions:
        vdir = version_workdirs[version]
        output_json_path = os.path.join(vdir, "output.json")

        if not os.path.exists(output_json_path):
            print(f"⚠️ {version}的output.json不存在: {output_json_path}")
            # 检查是否有output.md（V5可能只有md没有json）
            output_md_path = os.path.join(vdir, "output.md")
            if os.path.exists(output_md_path):
                print(f"  {version}有output.md但没有output.json——V5可能需要手动解析")
            continue

        version_outputs[version] = _read_json(output_json_path)
        print(f"✅ {version}产出已读取: {len(version_outputs[version].get('traces', []))}个trace")

    if not version_outputs:
        raise RuntimeError(f"没有找到任何版本的产出——请检查4个AI Agent是否都已完成。工作目录: {workdir_base}")

    # 2. 对V9的产出运行程序验证
    v9_audit_report = None
    if "V9" in version_outputs:
        v9_output_path = os.path.join(version_workdirs["V9"], "output.json")
        audit_report_path = os.path.join(version_workdirs["V9"], "audit_report.json")
        v9_audit_report = _run_lattice_completeness_verify(v9_output_path, audit_report_path)
        if v9_audit_report:
            score = v9_audit_report.get("completeness_score", 0)
            print(f"✅ V9程序验证完成: 闭元素完备性得分={score:.1%}")
        else:
            print("⚠️ V9程序验证失败——verify_lattice_completeness.py运行出错")

    # 3. 合并4个版本的trace（取并集，按语义去重）
    merged_traces, merged_veins, merged_level_views = _merge_version_outputs(
        version_outputs, problem_id
    )

    # 4. 写merged_traces.json
    merged_path = os.path.join(workdir_base, "merged_traces.json")
    merged_data = {
        "traces": [t.__dict__ if hasattr(t, '__dict__') else t for t in merged_traces],
        "veins": [v.__dict__ if hasattr(v, '__dict__') else v for v in merged_veins],
        "level_views": [lv.__dict__ if hasattr(lv, '__dict__') else lv for lv in merged_level_views],
        "version_trace_counts": {
            v: len(output.get("traces", [])) for v, output in version_outputs.items()
        },
        "merged_trace_count": len(merged_traces),
    }
    _write_json(merged_path, merged_data)
    print(f"✅ 合并完成: {len(merged_traces)}个trace（并集去重后）")

    # 5. 更新meta
    meta["status"] = "completed"
    meta["completed_at"] = datetime.now(timezone.utc).isoformat()
    meta["version_trace_counts"] = merged_data["version_trace_counts"]
    meta["merged_trace_count"] = len(merged_traces)
    if v9_audit_report:
        meta["v9_completeness_score"] = v9_audit_report.get("completeness_score", 0)
    _write_json(meta_path, meta)

    # 6. 返回AnalysisOutput
    return AnalysisOutput(
        traces=merged_traces,
        veins=merged_veins,
        level_views=merged_level_views,
        process="absorb",
    )


# ============================================================================
# solve模式——提示词未设计，留NotImplementedError
# ============================================================================

def _vein_analysis_solve(input: AnalysisInput) -> AnalysisOutput:
    """solve模式的脉络分析

    solve模式从推理AI的thinking分析脉络，可能有分叉（树/DAG结构）。
    solve模式的提示词尚未设计（TODO-1）——V5-V9都是absorb模式提示词。
    """
    raise NotImplementedError(
        "solve模式的脉络分析尚未实现——solve模式提示词未设计（TODO-1）。"
        "V5-V9都是absorb模式提示词（分析完整解答文本，线性脉络）。"
        "solve模式需要从推理AI的thinking分析脉络，可能有分叉（树/DAG结构），"
        "需要设计新的提示词变体并POC验证。"
    )


# ============================================================================
# 工作目录准备
# ============================================================================

def _create_workdir_base(process: str, problem_id: str) -> str:
    """创建工作目录基路径

    结构：palyground/{process}/vein_analysis/{problem_id}/
    """
    repo_root = _load_repo_root()
    workdir_base = os.path.join(repo_root, "palyground", process, "vein_analysis", problem_id)
    os.makedirs(workdir_base, exist_ok=True)
    return workdir_base


def _prepare_version_workdir(workdir_base: str, version: str,
                              solution_block: str, problem_id: str) -> str:
    """准备单个版本的工作目录

    在workdir_base/{version}/下创建：
    - AGENTS.md——AI的指令和约束（从assets目录复制固定模板）
    - prompt.md——完整提示词（从提示词积累目录复制，不替换占位符）
    - input.md——输入数据（解答文本块）

    固定内容（AGENTS.md、提示词）从积累目录复制，不动态生成。
    动态内容（解答文本）写入input.md，AI启动后从input.md读取。

    Args:
        workdir_base: 工作目录基路径
        version: 版本名（V5/V7/V8/V9）
        solution_block: 解答文本块（题目+解答+孤悬trace启发信号）
        problem_id: 题目ID

    Returns:
        版本工作目录的绝对路径
    """
    version_dir = os.path.join(workdir_base, version)
    os.makedirs(version_dir, exist_ok=True)

    # 1. 复制AGENTS.md——从assets目录复制固定模板
    system_dir = os.path.dirname(os.path.abspath(__file__))
    agents_src = os.path.join(system_dir, AGENTS_TEMPLATES[version])
    if not os.path.exists(agents_src):
        raise FileNotFoundError(f"AGENTS.md模板不存在: {agents_src}")
    agents_path = os.path.join(version_dir, "AGENTS.md")
    shutil.copy(agents_src, agents_path)

    # 2. 复制prompt.md——从提示词积累目录复制，不替换占位符
    #    提示词中的[解答文本插入位置]占位符保留，AI启动后从input.md读取解答文本
    #    prompt.md中会说"读取input.md中的解答文本，分析以下解答：[解答文本插入位置]"
    #    AI看到占位符后知道要从input.md读取
    repo_root = _load_repo_root()
    prompt_src = os.path.join(repo_root, PROMPT_FILES[version])
    if not os.path.exists(prompt_src):
        raise FileNotFoundError(f"提示词文件不存在: {prompt_src}")
    prompt_path = os.path.join(version_dir, "prompt.md")
    shutil.copy(prompt_src, prompt_path)

    # 3. 写input.md——解答文本块（动态内容）
    input_path = os.path.join(version_dir, "input.md")
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(solution_block)

    return version_dir


def _generate_agents_md(version: str, problem_id: str) -> str:
    """生成为脉络分析AI定制的AGENTS.md

    已废弃——AGENTS.md现在从assets目录复制固定模板，不再动态生成。
    保留此函数仅为向后兼容。
    """
    raise DeprecationWarning(
        "_generate_agents_md已废弃——AGENTS.md现在从system/assets/vein_analysis/复制固定模板。"
        "如需修改AGENTS.md内容，修改assets目录下的模板文件。"
    )


# ============================================================================
# 产出收集和合并
# ============================================================================

def _run_lattice_completeness_verify(v9_output_path: str,
                                      audit_report_path: str) -> Optional[dict]:
    """对V9的产出运行verify_lattice_completeness.py

    Args:
        v9_output_path: V9的output.json路径
        audit_report_path: 审计报告输出路径

    Returns:
        审计报告dict，如果验证脚本运行出错则返回None
    """
    repo_root = _load_repo_root()
    verify_script = os.path.join(repo_root, VERIFY_SCRIPT)

    if not os.path.exists(verify_script):
        print(f"⚠️ 程序验证脚本不存在: {verify_script}")
        return None

    # 用subprocess运行验证脚本
    import subprocess
    cmd = [
        "python3", verify_script, v9_output_path,
        "--report", audit_report_path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            # 读取审计报告
            if os.path.exists(audit_report_path):
                return _read_json(audit_report_path)
            else:
                print(f"⚠️ 验证脚本运行成功但审计报告未生成: {audit_report_path}")
                return None
        else:
            print(f"⚠️ 验证脚本运行失败: {result.stderr}")
            return None
    except subprocess.TimeoutExpired:
        print("⚠️ 验证脚本运行超时（60秒）")
        return None
    except Exception as e:
        print(f"⚠️ 验证脚本运行异常: {e}")
        return None


def _merge_version_outputs(version_outputs: dict, problem_id: str) -> tuple:
    """合并4个版本的产出——取trace并集

    当前实现：不做自动去重（TODO-5），4版本trace全部保留。
    理由：去重需要语义判断（成本高且可能出错），让trace_match阶段自然处理重复
    （多个trace匹配同一个tell只取一次匹配结果）。

    Args:
        version_outputs: {version: output_json_dict}
        problem_id: 题目ID

    Returns:
        (merged_traces, merged_veins, merged_level_views)
    """
    merged_traces = []
    merged_veins = []
    merged_level_views = []

    # 用于生成唯一trace_id
    trace_counter = 0

    for version, output in version_outputs.items():
        # 解析trace
        version_traces = output.get("traces", [])
        for t in version_traces:
            trace_counter += 1
            # 生成唯一trace_id——带版本前缀，方便追溯来源
            original_id = t.get("id", t.get("trace_id", f"t{trace_counter}"))
            trace_id = f"{version}_{original_id}"

            # 解析source_segment_ids
            seg_ids = t.get("source_segment_ids", t.get("segments", t.get("segment", [])))
            if isinstance(seg_ids, str):
                seg_ids = [seg_ids]

            # 解析trace_type
            trace_type = t.get("trace_type", t.get("type", "non_local"))
            if trace_type not in ("local", "non_local", "global"):
                # 尝试从level推断
                level = t.get("level", 0)
                if level == 0:
                    trace_type = "local"
                elif "global" in str(trace_type).lower() or "meta_reflection" in str(t.get("level", "")).lower():
                    trace_type = "global"
                else:
                    trace_type = "non_local"

            trace = Trace(
                trace_id=trace_id,
                level=t.get("level", 0),
                trace_type=trace_type,
                pattern_description=t.get("description", t.get("pattern_description", "")),
                source_segment_ids=seg_ids,
                is_branch_position=False,  # absorb模式没有分叉位置
            )
            merged_traces.append(trace)

        # 解析vein（每个版本产出一个vein）
        version_vein = _parse_vein_from_output(output, version, problem_id)
        if version_vein:
            merged_veins.append(version_vein)

        # 解析level_views
        version_level_views = _parse_level_views_from_output(output, version, problem_id)
        merged_level_views.extend(version_level_views)

    return merged_traces, merged_veins, merged_level_views


def _parse_vein_from_output(output: dict, version: str, problem_id: str) -> Optional[Vein]:
    """从版本产出中解析Vein

    absorb模式是线性脉络。段划分从output的segments字段获取。
    """
    segments_data = output.get("segments", [])
    if not segments_data:
        return None

    segments = []
    for i, seg in enumerate(segments_data):
        seg_id = seg.get("id", seg.get("segment_id", f"seg_{i+1}"))
        segments.append(Segment(
            segment_id=seg_id,
            segment_text=seg.get("content", seg.get("segment_text", "")),
            segment_features=seg.get("features", seg.get("segment_features", {})),
            order=seg.get("order", i),
        ))

    vein_id = f"vein_{version}_{problem_id}"
    return Vein(
        vein_id=vein_id,
        source_id=f"{version}_{problem_id}",
        source_type="solution_record",
        structure="linear",  # absorb模式是线性脉络
        segments=segments,
        branches=None,  # absorb模式没有分叉
    )


def _parse_level_views_from_output(output: dict, version: str,
                                     problem_id: str) -> list:
    """从版本产出中解析LevelView列表

    LevelView从output的closed_elements或level_views字段获取。
    V7/V8/V9有闭元素，可以构造LevelView。V5没有闭元素，跳过。
    """
    level_views = []

    # V7/V8/V9的闭元素可以构造LevelView
    closed_elements = output.get("closed_elements", [])
    for i, ce in enumerate(closed_elements):
        extent = ce.get("extent", [])
        view_id = f"lv_{version}_{problem_id}_{i}"
        level_views.append(LevelView(
            view_id=view_id,
            vein_id=f"vein_{version}_{problem_id}",
            level=ce.get("level", i),
            merged_segments=[extent] if isinstance(extent, list) else [[str(extent)]],
            view_features={
                "intent": ce.get("intent", []),
                "is_closed": ce.get("is_closed", True),
                "trace_judgment": ce.get("trace_judgment", ""),
                "is_ai_advantage": ce.get("is_ai_advantage", False),
            },
        ))

    return level_views


# ============================================================================
# 辅助函数
# ============================================================================

def _format_orphan_traces(traces: list) -> str:
    """格式化孤悬trace启发信号——附加到解答文本块后面"""
    lines = []
    for t in traces:
        lines.append(f"- [{t.trace_type}] {t.pattern_description}")
    return "\n".join(lines)


def _write_json(path: str, data: dict) -> None:
    """写JSON文件"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _read_json(path: str) -> dict:
    """读JSON文件"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
