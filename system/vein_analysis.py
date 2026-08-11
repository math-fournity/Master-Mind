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

本模块实现absorb模式的4并发方案——V5/V7/V8/V10四个提示词版本并发跑同一道题，
取trace并集。

4个版本各有所长，不是简单的子集关系：
- V5独有"归纳递降三种方式"（自由直觉发现）
- V7独有"预防性vs修复性避障"+"Case间递进"（结构化约束让注意力分布不同）
- V8独有"x贯穿"+"aₙ作为工具"（跨闭元素元模式引导）
- V10独有"WLOG闭环"+"r的生命周期"（元反思步骤）+ "先写文件后做验证"执行顺序
- V10 = V9改进版——伪元模式过滤和贯穿性验证移到程序中（verify_lattice_completeness.py已实现），
  AI只做关键实体列举和元反思；加"先写文件后做验证"防止token超限

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
1. 准备阶段（代码自动执行）：创建工作目录、从assets目录复制AGENTS.md和prompt.md、写入input.md
2. 数据库记录阶段（代码自动执行）：创建session记录、problem_entry记录（抓手）、4个ai_instance记录
3. 启动阶段（代码自动执行）：用subprocess启动4个tmux session
4. 等待阶段（代码自动执行）：轮询output.json是否出现，等待4个AI完成
5. 收集阶段（代码自动执行）：读取4个AI的产出JSON、运行程序验证、合并trace、更新数据库记录
6. 返回AnalysisOutput

数据库记录——题目录入信息抓手：
- problem_entries集合——每道题入题一条记录，是查找该题目所有录入信息的抓手
- 从这条记录可以找到：工作目录、会话ID、4个AI实例ID、产出路径、程序验证报告路径、合并trace路径
- 查找方法：db.find_problem_entries_by_problem_id(problem_id)

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
import subprocess
import sys
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
PROMPT_VERSIONS = ["V5", "V7", "V8", "V10"]

# 提示词文件的相对路径（相对repo根目录）
PROMPT_DIR = "第六代系统提示词积累目录/pipe_1_parser/step_2_grid_vein/set_A_fca_hassee"
PROMPT_FILES = {
    "V5": os.path.join(PROMPT_DIR, "v5.md"),
    "V7": os.path.join(PROMPT_DIR, "v7.md"),
    "V8": os.path.join(PROMPT_DIR, "v8.md"),
    "V10": os.path.join(PROMPT_DIR, "v10.md"),
}

# 提示词中解答文本的占位符——替换为实际解答文本
SOLUTION_PLACEHOLDER = "[解答文本插入位置]"

# AGENTS.md模板文件路径（相对system/目录）
AGENTS_TEMPLATES = {
    "V5": "assets/vein_analysis/AGENTS_V5.md",
    "V7": "assets/vein_analysis/AGENTS_V7.md",
    "V8": "assets/vein_analysis/AGENTS_V8.md",
    "V10": "assets/vein_analysis/AGENTS_V10.md",
}

# 程序验证脚本路径（相对repo根目录）
VERIFY_SCRIPT = "six/verify_lattice_completeness.py"

# ============================================================================
# 三阶段架构常量
# ============================================================================

# 格化提示词（阶段1）——只含段划分+形式上下文构造
GRADING_PROMPT_FILES = {
    "V5": os.path.join(PROMPT_DIR, "v5_grading.md"),
    "V7": os.path.join(PROMPT_DIR, "v7_grading.md"),
    "V8": os.path.join(PROMPT_DIR, "v8_grading.md"),
    "V10": os.path.join(PROMPT_DIR, "v10_grading.md"),
}

# 综合分析提示词（阶段2）
SYNTHESIS_PROMPT_FILE = os.path.join(PROMPT_DIR, "synthesis.md")

# 综合分析AGENTS.md模板
SYNTHESIS_AGENTS_TEMPLATE = "assets/vein_analysis/AGENTS_synthesis.md"

# ============================================================================
# 运行模式开关——tmux交互模式 vs 非交互模式
# ============================================================================

# True = tmux交互模式（detached session，可attach查看进度）
# False = 非交互模式（subprocess直接启动，-p/--print，跑完自动退出，trajectory完整导出）
# 默认非交互模式——devin cli处理完prompt后自动退出，--export在退出前导出完整trajectory
# tmux模式有trajectory导出不完整的问题（kill session时devin cli可能还在做导出）
USE_TMUX = False


def _launch_devin(session_name: str, workdir: str, prompt: str) -> bool:
    """启动devin cli实例——根据USE_TMUX开关选择tmux交互模式或非交互模式

    两种模式都带--export导出ATIF v1.7格式trajectory到工作目录下的trajectory.json。
    trajectory.json包含完整推理过程（thinking + tool_calls + tool_results + token usage），
    用于审计、调试和trajectory提取。

    Args:
        session_name: tmux session名（tmux模式时用）
        workdir: 工作目录
        prompt: 启动提示词

    Returns:
        True=启动成功, False=启动失败
    """
    trajectory_path = os.path.join(workdir, "trajectory.json")

    if USE_TMUX:
        # tmux交互模式——detached session，可attach查看进度
        cmd = [
            "tmux", "new-session", "-d", "-s", session_name,
            f"cd {workdir} && devin --permission-mode dangerous --respect-workspace-trust false --export {trajectory_path} -- '{prompt}'"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode != 0:
            print(f"  ⚠️ tmux启动失败: {result.stderr}")
            return False
        return True
    else:
        # 非交互模式——subprocess后台启动，-p/--print，跑完自动退出
        # stdout输出AI响应文本，--export导出完整trajectory
        # 用Popen不等待——后台运行，轮询DONE.md判断完成
        log_path = os.path.join(workdir, "devin_cli.log")
        log_f = open(log_path, "w")
        proc = subprocess.Popen(
            ["devin", "--permission-mode", "dangerous",
             "--respect-workspace-trust", "false",
             "--export", trajectory_path,
             "-p", prompt],
            stdout=log_f, stderr=subprocess.STDOUT,
            cwd=workdir,
        )
        # 记录PID到文件——方便后续检查进程是否还活着
        with open(os.path.join(workdir, "devin_pid.txt"), "w") as f:
            f.write(str(proc.pid))
        return True

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

    absorb模式采用4并发方案——V5/V7/V8/V10四个提示词版本并发跑同一道题，
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

    # 创建工作目录——每次入题分配唯一递增序号
    workdir_base, run_id = _create_workdir_base("absorb", problem_id)

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

    # 创建数据库记录——会话+题目录入（抓手）
    from system import db
    session_key = db.create_session(
        session_type="absorb",
        problem_id=problem_id,
        working_directory=workdir_base,
    )
    entry_key = db.create_problem_entry(
        problem_id=problem_id,
        process="absorb",
        working_directory=workdir_base,
        run_id=run_id,
        record_id=record.record_id,
        versions=list(PROMPT_VERSIONS),
        version_workdirs={v: str(d) for v, d in prepared_dirs.items()},
        has_orphan_traces=input.orphan_traces is not None and len(input.orphan_traces) > 0,
        session_id=session_key,
    )
    meta["session_key"] = session_key
    meta["entry_key"] = entry_key
    _write_json(meta_path, meta)

    # 启动4个tmux session
    session_names = {}
    ai_instance_ids = {}
    for version in PROMPT_VERSIONS:
        vdir = prepared_dirs[version]
        session_name = f"absorb-{run_id:04d}-{version}"
        session_names[version] = session_name

        # 创建AI实例记录
        ai_key = db.create_ai_instance(
            session_id=session_key,
            ai_role="parser",
            working_directory=str(vdir),
            problem_id=problem_id,
            tmux_session=session_name,
            version=version,
        )
        ai_instance_ids[version] = ai_key

        # 短启动提示词——让AI加载AGENTS.md和prompt.md，从input.md读取解答文本
        launch_prompt = (
            f"先加载 {vdir}/AGENTS.md 了解你的角色和约束，"
            f"然后加载 {vdir}/prompt.md 中的提示词，"
            f"读取 {vdir}/input.md 中的解答文本作为分析对象，"
            f"按提示词要求工作，完成后把产出写入 {vdir}/output.json 和 {vdir}/output.md。"
            f"全部产出写完后，在 {vdir}/ 下创建一个空的 DONE.md 文件作为完成信号——"
            f"DONE.md是空文件，只是表示你确认所有工作已完成。"
        )

        # 用_launch_devin启动devin cli——根据USE_TMUX开关选择tmux或非交互模式
        print(f"启动 {version}: session={session_name}")
        success = _launch_devin(session_name, vdir, launch_prompt)
        if not success:
            db.update_ai_instance(ai_key, status="failed", end_reason="devin cli启动失败")
        else:
            print(f"✅ {version} tmux启动成功")

    # 更新数据库——记录session_names和ai_instance_ids
    db.update_problem_entry(
        entry_key,
        session_names=session_names,
        ai_instance_ids=ai_instance_ids,
    )

    # 更新meta状态
    meta["status"] = "running"
    meta["session_names"] = session_names
    meta["ai_instance_ids"] = ai_instance_ids
    _write_json(meta_path, meta)

    print()
    print(f"4个AI Agent已启动，等待完成...")
    print(f"工作目录: {workdir_base}")
    print(f"检查状态: tmux list-sessions | grep absorb-vein_analysis-{problem_id}")
    print()

    # 等待4个AI完成——轮询output.json是否出现
    output = _wait_and_collect(workdir_base, prepared_dirs, meta, meta_path)
    return output


def _cleanup_tmux_sessions(prepared_dirs: dict):
    """清理已完成的devin cli实例——自动回收

    根据USE_TMUX开关选择清理方式：
    - tmux模式：kill对应的tmux session
    - 非交互模式：kill对应的进程（从devin_pid.txt读PID）

    Args:
        prepared_dirs: {version: workdir_path}
    """
    for version, vdir in prepared_dirs.items():
        done_path = os.path.join(vdir, "DONE.md")
        if not os.path.exists(done_path):
            continue
        if USE_TMUX:
            # tmux模式——kill session
            # 目录名格式：{4位数字}_{problem_id}，提取数字部分构造session名
            dir_name = os.path.basename(os.path.dirname(vdir))
            run_id_str = dir_name.split("_")[0]
            session_name = f"absorb-{run_id_str}-{version}"
            try:
                result = subprocess.run(
                    ["tmux", "kill-session", "-t", session_name],
                    capture_output=True, text=True, timeout=5,
                )
                if result.returncode == 0:
                    print(f"🧹 已清理 {version} 的tmux session: {session_name}")
            except Exception as e:
                print(f"⚠️ 清理 {version} 的tmux session失败: {e}")
        else:
            # 非交互模式——kill进程
            pid_path = os.path.join(vdir, "devin_pid.txt")
            if os.path.exists(pid_path):
                try:
                    with open(pid_path) as f:
                        pid = int(f.read().strip())
                    os.kill(pid, 15)  # SIGTERM
                    print(f"🧹 已清理 {version} 的devin cli进程: PID={pid}")
                except ProcessLookupError:
                    pass  # 进程已退出
                except Exception as e:
                    print(f"⚠️ 清理 {version} 的devin cli进程失败: {e}")


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
            done_path = os.path.join(vdir, "DONE.md")
            done = os.path.exists(done_path)
            status.append(f"{version}: {'✅' if done else '⏳'}")
            if not done:
                all_done = False

        print(f"[{int(elapsed)}s] {' '.join(status)}")

        if all_done:
            print("✅ 4个AI全部完成")
            break

        time.sleep(poll_interval)

    # 收集产出
    output = collect_vein_analysis_output(workdir_base)

    # 清理已完成的tmux session——自动回收devin cli实例
    _cleanup_tmux_sessions(prepared_dirs)

    return output


def collect_vein_analysis_output(workdir_base: str) -> AnalysisOutput:
    """收集4并发脉络分析的产出——在4个AI Agent都完成后调用

    流程：
    1. 读取4个版本的output.json
    2. 对V10的output.json运行verify_lattice_completeness.py
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

    # 2. 对V10的产出运行程序验证
    v10_audit_report = None
    if "V10" in version_outputs:
        v10_output_path = os.path.join(version_workdirs["V10"], "output.json")
        audit_report_path = os.path.join(version_workdirs["V10"], "audit_report.json")
        v10_audit_report = _run_lattice_completeness_verify(v10_output_path, audit_report_path)
        if v10_audit_report:
            score = v10_audit_report.get("completeness_score", 0)
            print(f"✅ V10程序验证完成: 闭元素完备性得分={score:.1%}")
        else:
            print("⚠️ V10程序验证失败——verify_lattice_completeness.py运行出错")

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
    if v10_audit_report:
        meta["v10_completeness_score"] = v10_audit_report.get("completeness_score", 0)
    _write_json(meta_path, meta)

    # 6. 更新数据库记录——题目录入记录（抓手）和会话记录
    entry_key = meta.get("entry_key")
    session_key = meta.get("session_key")
    if entry_key:
        from system import db
        # 收集各版本产出路径
        output_paths = {}
        for version in versions:
            vdir = version_workdirs[version]
            output_paths[version] = {
                "json": os.path.join(vdir, "output.json") if os.path.exists(os.path.join(vdir, "output.json")) else None,
                "md": os.path.join(vdir, "output.md") if os.path.exists(os.path.join(vdir, "output.md")) else None,
            }
        db.update_problem_entry(
            entry_key,
            status="completed",
            output_paths=output_paths,
            audit_report_path=os.path.join(version_workdirs["V10"], "audit_report.json") if "V10" in version_outputs else None,
            merged_traces_path=merged_path,
            trace_count=len(merged_traces),
        )
        # 更新各AI实例状态
        ai_instance_ids = meta.get("ai_instance_ids", {})
        for version, ai_key in ai_instance_ids.items():
            trace_count = len(version_outputs.get(version, {}).get("traces", []))
            db.update_ai_instance(
                ai_key,
                status="completed",
                end_reason="output.json已生成",
                output_summary=f"{trace_count}个trace",
            )
    if session_key:
        from system import db
        db.update_session(
            session_key,
            status="completed",
            result_summary=f"脉络分析完成，{len(merged_traces)}个trace",
        )

    # 7. 返回AnalysisOutput
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
    solve模式的提示词尚未设计（TODO-1）——V5-V10都是absorb模式提示词。
    """
    raise NotImplementedError(
        "solve模式的脉络分析尚未实现——solve模式提示词未设计（TODO-1）。"
        "V5-V10都是absorb模式提示词（分析完整解答文本，线性脉络）。"
        "solve模式需要从推理AI的thinking分析脉络，可能有分叉（树/DAG结构），"
        "需要设计新的提示词变体并POC验证。"
    )


# ============================================================================
# 工作目录准备
# ============================================================================

def _create_workdir_base(process: str, problem_id: str, run_id: Optional[int] = None) -> tuple:
    """创建工作目录基路径——每次入题用唯一递增序号

    结构：palyground/{process}/vein_analysis/{4位数字序号}_{problem_id}/

    每次入题（无论是新题还是同一道题再次入题）都分配一个唯一的、递增的数字序号。
    这是可审计性的保障——通过序号可以追溯每一次入题的完整记录，且不会覆盖之前的产出。

    Args:
        process: "absorb"或"solve"
        problem_id: 题目标识（如imo2009p6）
        run_id: 入题序号——如果未提供，自动从数据库获取下一个递增序号

    Returns:
        (workdir_base, run_id) ——工作目录绝对路径和入题序号
    """
    from .db import get_next_run_id, format_run_id
    if run_id is None:
        run_id = get_next_run_id()
    dir_name = format_run_id(run_id, problem_id)
    repo_root = _load_repo_root()
    workdir_base = os.path.join(repo_root, "palyground", process, "vein_analysis", dir_name)
    os.makedirs(workdir_base, exist_ok=True)
    return workdir_base, run_id


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
        version: 版本名（V5/V7/V8/V10）
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
    """对V10的产出运行verify_lattice_completeness.py

    Args:
        v9_output_path: V10的output.json路径
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
    V7/V8/V10有闭元素，可以构造LevelView。V5没有闭元素，跳过。
    """
    level_views = []

    # V7/V8/V10的闭元素可以构造LevelView
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


def _build_solution_block(input: AnalysisInput) -> str:
    """构造解答文本块——题目+解答文本"""
    record = input.solution_record
    solution_text = record.solution_text
    problem_text = record.problem.problem_text

    solution_block = f"""**题目**：

{problem_text}

**解答**：

{solution_text}"""

    if input.orphan_traces:
        orphan_block = _format_orphan_traces(input.orphan_traces)
        solution_block += f"\n\n**孤悬trace启发信号**（来自解题引导，请重点关注这些模式在外部解答中的体现）：\n\n{orphan_block}"

    return solution_block


# ============================================================================
# 三阶段架构——格化→程序枚举→综合分析
# ============================================================================

def _md5_of_file(path: str) -> str:
    """计算文件的md5（前8位）"""
    import hashlib
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()[:8]


def _git_commit_hash() -> str:
    """获取当前git commit hash（前7位）"""
    import subprocess
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short=7", "HEAD"],
            capture_output=True, text=True, cwd=_load_repo_root()
        )
        return result.stdout.strip() if result.returncode == 0 else "unknown"
    except Exception:
        return "unknown"


def _git_branch() -> str:
    """获取当前git分支名"""
    import subprocess
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, cwd=_load_repo_root()
        )
        return result.stdout.strip() if result.returncode == 0 else "unknown"
    except Exception:
        return "unknown"


def _write_run_manifest(workdir_base: str, run_id: int, problem_id: str) -> str:
    """生成run_manifest.json——记录本次运行使用的所有资产版本（339号方案）

    回头审计时直接读run_manifest.json，不需要md5对比git历史。
    """
    repo_root = _load_repo_root()
    system_dir = os.path.join(repo_root, "system")

    def file_info(rel_path: str) -> dict:
        """返回文件的相对路径+md5"""
        abs_path = os.path.join(repo_root, rel_path) if not os.path.isabs(rel_path) else rel_path
        if os.path.exists(abs_path):
            return {"path": rel_path, "md5": _md5_of_file(abs_path)}
        return {"path": rel_path, "md5": None, "missing": True}

    manifest = {
        "run_id": run_id,
        "problem_id": problem_id,
        "started_at": datetime.now().isoformat(),
        "git_commit": _git_commit_hash(),
        "git_branch": _git_branch(),
        "phases": {
            "phase1_grading": {
                "versions": PROMPT_VERSIONS,
                "prompt_files": {
                    v: file_info(GRADING_PROMPT_FILES[v]) for v in PROMPT_VERSIONS
                },
                "agents_templates": {
                    v: file_info(os.path.join("system", AGENTS_TEMPLATES[v])) for v in PROMPT_VERSIONS
                },
                "step_files": {},
            },
            "phase1_5_enumerate": {
                "script": VERIFY_SCRIPT,
                "script_md5": _md5_of_file(os.path.join(repo_root, VERIFY_SCRIPT)) if os.path.exists(os.path.join(repo_root, VERIFY_SCRIPT)) else None,
            },
            "phase2_synthesis": {
                "prompt_file": file_info(SYNTHESIS_PROMPT_FILE),
                "agents_template": file_info(os.path.join("system", SYNTHESIS_AGENTS_TEMPLATE)),
                "step_files": {},
            },
        },
        "code_version": {
            "vein_analysis_py": _md5_of_file(os.path.abspath(__file__)),
        },
    }

    # V8的step要求文件
    for step_num in range(1, 3):
        step_path = os.path.join(PROMPT_DIR, f"v8_step{step_num}_requirements.md")
        abs_step = os.path.join(repo_root, step_path)
        if os.path.exists(abs_step):
            manifest["phases"]["phase1_grading"]["step_files"][f"v8_step{step_num}"] = file_info(step_path)

    # 综合分析的step要求文件
    for step_num in range(1, 5):
        step_path = os.path.join(PROMPT_DIR, f"synthesis_step{step_num}_requirements.md")
        abs_step = os.path.join(repo_root, step_path)
        if os.path.exists(abs_step):
            manifest["phases"]["phase2_synthesis"]["step_files"][f"step{step_num}"] = file_info(step_path)

    manifest_path = os.path.join(workdir_base, "run_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"  run_manifest.json已生成: {manifest_path}")
    return manifest_path


def _archive_run(workdir_base: str, run_id: int) -> str:
    """运行结束后自动归档到system/tests/vein_analysis/runs/{run_id}/（339号方案）

    归档内容：
    - 各V的segments.json/formal_context.json/closed_elements.json
    - 综合分析的output.json/output.md/comparison.json/closed_element_traces.json/content_based_traces.json
    - run_manifest.json
    """
    import shutil
    repo_root = _load_repo_root()
    archive_dir = os.path.join(repo_root, "system", "tests", "vein_analysis", "runs", f"{run_id:04d}")
    os.makedirs(archive_dir, exist_ok=True)

    # 归档run_manifest.json
    manifest = os.path.join(workdir_base, "run_manifest.json")
    if os.path.exists(manifest):
        shutil.copy2(manifest, os.path.join(archive_dir, "run_manifest.json"))

    # 归档各V格化结果
    grading_base = os.path.join(workdir_base, "phase1_grading")
    for v in PROMPT_VERSIONS:
        vdir = os.path.join(grading_base, v)
        if os.path.exists(vdir):
            for fname in ["segments.json", "formal_context.json", "key_entities.json"]:
                src = os.path.join(vdir, fname)
                if os.path.exists(src):
                    shutil.copy2(src, os.path.join(archive_dir, f"{v}_{fname}"))

    # 归档闭元素
    enum_dir = os.path.join(workdir_base, "phase1_5_enumerate")
    if os.path.exists(enum_dir):
        for v in PROMPT_VERSIONS:
            src = os.path.join(enum_dir, f"{v}_closed_elements.json")
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(archive_dir, f"{v}_closed_elements.json"))

    # 归档综合分析结果
    synth_dir = os.path.join(workdir_base, "phase2_synthesis")
    if os.path.exists(synth_dir):
        for fname in ["output.json", "output.md", "comparison.json",
                       "closed_element_traces.json", "content_based_traces.json"]:
            src = os.path.join(synth_dir, fname)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(archive_dir, fname))

    print(f"  归档完成: {archive_dir}")
    return archive_dir


def _calc_grading_timeout(solution_text: str) -> int:
    """根据解答文本长度计算格化超时时间（秒）——340号方案

    经验值（基于0004-0011的历史数据）：
    - 短文本（<2000字符）：10分钟
    - 中等文本（2000-5000字符）：15分钟
    - 长文本（5000-10000字符）：20分钟
    - 超长文本（>10000字符）：30分钟

    IMO 2009 P6解答约2400字符 → 15分钟
    """
    text_len = len(solution_text)
    if text_len < 2000:
        return 600   # 10分钟
    elif text_len < 5000:
        return 900   # 15分钟
    elif text_len < 10000:
        return 1200  # 20分钟
    else:
        return 1800  # 30分钟


def vein_analysis_three_phase(input: AnalysisInput) -> AnalysisOutput:
    """三阶段脉络分析——格化与trace识别分离

    阶段1（4并发格化）：V5/V7/V8/V10各做段划分+形式上下文构造
    阶段1.5（程序枚举闭元素）：verify_lattice_completeness.py枚举所有闭元素
    阶段2（1个综合分析Agent）：读4个版本格化结果+程序枚举闭元素，做trace识别+审计+元反思

    支持两种模式：
    - absorb（解答吸收）：从SolutionRecord分析，线性脉络，接收孤悬trace启发信号
    - solve（解题引导）：从Thinking分析，可能有分叉——TODO: solve模式提示词未设计

    详见333号文档。
    """
    print("=" * 70)
    print("三阶段脉络分析——格化与trace识别分离")
    print("=" * 70)

    if input.process == "absorb":
        if input.solution_record is None:
            raise ValueError("absorb模式需要input.solution_record")
        problem_id = input.solution_record.problem.problem_id
    elif input.process == "solve":
        if input.thinking is None:
            raise ValueError("solve模式需要input.thinking")
        # solve模式从thinking中提取problem_id
        problem_id = input.thinking.problem_id
        raise NotImplementedError(
            "solve模式的三阶段架构尚未实现——solve模式提示词未设计（TODO-1）。"
            "当前只有absorb模式的三阶段架构可用。"
        )
    else:
        raise ValueError(f"未知的process类型: {input.process}，必须是 'solve' 或 'absorb'")

    workdir_base, run_id = _create_workdir_base(input.process, problem_id)
    print(f"工作目录: {workdir_base}")
    print(f"入题序号: {run_id:04d}")

    # 创建数据库记录——入题抓手
    from . import db
    session_key = db.create_session(
        session_type=input.process,
        problem_id=problem_id,
        working_directory=workdir_base,
    )
    entry_key = db.create_problem_entry(
        problem_id=problem_id,
        process=input.process,
        working_directory=workdir_base,
        run_id=run_id,
        session_id=session_key,
    )

    # 生成run_manifest.json——记录本次运行使用的所有资产版本（339号方案）
    print("\n--- 生成run_manifest.json ---")
    manifest_path = _write_run_manifest(workdir_base, run_id, problem_id)

    # 阶段1：4并发格化
    print("\n--- 阶段1：4并发格化 ---")
    grading_dirs = _phase1_grading(workdir_base, input, run_id)

    # 检查是否所有版本都失败（340号方案）
    from .log import get_logger
    logger = get_logger("vein_analysis")

    if not grading_dirs:
        logger.error("❌ 所有格化子管线失败，无法进行综合分析")
        db.update_problem_entry(entry_key, status="failed", error_detail="all_grading_failed")
        print("\n❌ 所有格化子管线失败，无法进行综合分析")
        # 返回空output
        from .schema import AnalysisOutput
        return AnalysisOutput(traces=[], veins=[], level_views=[], all_failed=True)

    # 读取phase1结果meta
    phase1_meta_path = os.path.join(workdir_base, "phase1_grading", "phase1_results.json")
    phase1_meta = {}
    if os.path.exists(phase1_meta_path):
        phase1_meta = _read_json(phase1_meta_path)
    success_versions = list(grading_dirs.keys())
    failed_versions = phase1_meta.get("failed_versions", [])
    if failed_versions:
        logger.info(f"综合分析将基于{success_versions}的格化结果，{failed_versions}因超时被舍弃")
        print(f"  ℹ️ 综合分析基于{success_versions}，{failed_versions}被舍弃")

    # 更新数据库——阶段1产出路径+成功/失败版本（340号方案）
    phase1_output_paths = {}
    for version, vdir in grading_dirs.items():
        phase1_output_paths[version] = {
            "segments": os.path.join(vdir, "segments.json"),
            "formal_context": os.path.join(vdir, "formal_context.json") if os.path.exists(os.path.join(vdir, "formal_context.json")) else None,
        }
    db.update_problem_entry(
        entry_key,
        phase1_output_paths=phase1_output_paths,
        phase1_success_versions=success_versions,
        phase1_failed_versions=failed_versions,
        phase1_results=phase1_meta.get("results", {}),
    )

    # 阶段1.5：程序枚举闭元素
    print("\n--- 阶段1.5：程序枚举闭元素 ---")
    closed_elements = _phase1_5_enumerate(workdir_base, grading_dirs)

    # 更新数据库——阶段1.5产出路径
    phase1_5_output_paths = {}
    enum_dir = os.path.join(workdir_base, "phase1_5_enumerate")
    for version in grading_dirs:
        ce_path = os.path.join(enum_dir, f"{version}_closed_elements.json")
        if os.path.exists(ce_path):
            phase1_5_output_paths[version] = ce_path
    db.update_problem_entry(entry_key, phase1_5_output_paths=phase1_5_output_paths)

    # 阶段2：综合分析
    print("\n--- 阶段2：综合分析 ---")
    output = _phase2_synthesis(workdir_base, input, grading_dirs, closed_elements, run_id)

    # 更新数据库——阶段2产出路径+完成
    synth_dir = os.path.join(workdir_base, "phase2_synthesis")
    db.update_problem_entry(
        entry_key,
        status="completed",
        phase2_output_paths={
            "output_json": os.path.join(synth_dir, "output.json"),
            "output_md": os.path.join(synth_dir, "output.md"),
        },
        trace_count=len(output.traces) if output.traces else 0,
    )

    # 自动归档到system/tests/vein_analysis/runs/{run_id}/（339号方案）
    print("\n--- 自动归档 ---")
    archive_dir = _archive_run(workdir_base, run_id)
    db.update_problem_entry(
        entry_key,
        archive_path=archive_dir,
        manifest_path=manifest_path,
    )

    print("\n✅ 三阶段脉络分析完成")
    return output


def _phase1_grading(workdir_base: str, input: AnalysisInput, run_id: int) -> dict:
    """阶段1：4并发格化——V5/V7/V8/V10各做段划分+形式上下文构造

    Returns:
        {version: workdir_path}——4个版本的格化工作目录
    """
    repo_root = _load_repo_root()
    system_dir = os.path.join(repo_root, "system")

    # 创建格化阶段的工作目录
    grading_base = os.path.join(workdir_base, "phase1_grading")
    os.makedirs(grading_base, exist_ok=True)

    prepared_dirs = {}
    for version in PROMPT_VERSIONS:
        vdir = os.path.join(grading_base, version)
        os.makedirs(vdir, exist_ok=True)

        # 复制AGENTS.md模板
        agents_src = os.path.join(system_dir, AGENTS_TEMPLATES[version])
        with open(agents_src, "r", encoding="utf-8") as f:
            agents_content = f.read()
        with open(os.path.join(vdir, "AGENTS.md"), "w", encoding="utf-8") as f:
            f.write(agents_content)

        # 复制格化提示词
        prompt_src = os.path.join(repo_root, GRADING_PROMPT_FILES[version])
        with open(prompt_src, "r", encoding="utf-8") as f:
            prompt_content = f.read()
        with open(os.path.join(vdir, "prompt.md"), "w", encoding="utf-8") as f:
            f.write(prompt_content)

        # V8文件拆分流程控制——复制step要求文件（335号方案v1修订——2步不退化方案）
        if version == "V8":
            import shutil
            for step_num in range(1, 3):  # step1=格化, step2=矩阵构造
                step_src = os.path.join(repo_root, PROMPT_DIR, f"v8_step{step_num}_requirements.md")
                if os.path.exists(step_src):
                    shutil.copy2(step_src, os.path.join(vdir, f"step{step_num}_requirements.md"))

        # 写input.md——题目+解答文本
        solution_block = _build_solution_block(input)
        with open(os.path.join(vdir, "input.md"), "w", encoding="utf-8") as f:
            f.write(solution_block)

        prepared_dirs[version] = vdir
        print(f"  准备 {version}: {vdir}")

    # 启动4个tmux session
    for version, vdir in prepared_dirs.items():
        session_name = f"grade-{run_id:04d}-{version}"
        launch_prompt = (
            f"先加载 {vdir}/AGENTS.md 了解你的角色和约束，"
            f"然后加载 {vdir}/prompt.md 中的提示词，"
            f"读取 {vdir}/input.md 中的解答文本作为分析对象，"
            f"按提示词要求做格化（段划分+形式上下文构造），"
            f"完成后把产出写入 {vdir}/segments.json"
            + (f" 和 {vdir}/formal_context.json" if version != "V5" else "")
            + (f" 和 {vdir}/key_entities.json" if version == "V10" else "")
            + f"。全部产出写完后，在 {vdir}/ 下创建一个空的 DONE.md 文件作为完成信号。"
        )

        success = _launch_devin(session_name, vdir, launch_prompt)
        if success:
            print(f"  ✅ {version} 启动成功: {session_name}")
        else:
            print(f"  ⚠️ {version} 启动失败")

    # 等待格化session完成——每个版本独立超时，至少1个通过即可（340号方案）
    import time
    from .log import get_logger
    logger = get_logger("vein_analysis")

    # 根据解答文本长度计算超时时间（340号方案）
    solution_text = input.solution_record.solution_text if input.solution_record else ""
    grading_timeout = _calc_grading_timeout(solution_text)
    logger.info(f"格化超时设定: {grading_timeout}秒（解答文本{len(solution_text)}字符）")

    poll_interval = 20
    started = time.time()
    version_status = {}  # {version: "running"/"completed"/"timeout"}
    version_start_time = {}  # {version: start_timestamp}
    for version in prepared_dirs:
        version_status[version] = "running"
        version_start_time[version] = started

    while True:
        elapsed = time.time() - started

        # 检查每个版本的状态
        status_parts = []
        for version, vdir in prepared_dirs.items():
            if version_status[version] == "completed":
                status_parts.append(f"{version}: ✅")
                continue
            if version_status[version] == "timeout":
                status_parts.append(f"{version}: ❌超时")
                continue

            # 检查是否完成
            done = os.path.exists(os.path.join(vdir, "DONE.md"))
            if done:
                version_status[version] = "completed"
                duration = int(time.time() - version_start_time[version])
                # 读取段数
                seg_count = 0
                seg_path = os.path.join(vdir, "segments.json")
                if os.path.exists(seg_path):
                    seg_data = _read_json(seg_path)
                    seg_count = len(seg_data.get("segments", seg_data if isinstance(seg_data, list) else []))
                logger.info(f"格化版本{version}完成，耗时{duration}秒，段数={seg_count}")
                status_parts.append(f"{version}: ✅")
            elif elapsed > grading_timeout:
                # 超时——标记timeout（340号方案）
                version_status[version] = "timeout"
                duration = int(time.time() - version_start_time[version])
                logger.warning(f"格化版本{version}超时({duration}秒)，标记timeout")
                # 创建FAILED.md标记文件
                with open(os.path.join(vdir, "FAILED.md"), "w") as f:
                    f.write(f"{version}超时失败，耗时{duration}秒\n")
                # kill卡住的进程
                pid_file = os.path.join(vdir, "devin_pid.txt")
                if os.path.exists(pid_file):
                    with open(pid_file) as f:
                        pid = f.read().strip()
                    if pid:
                        try:
                            import signal
                            os.kill(int(pid), signal.SIGTERM)
                            logger.info(f"已kill版本{version}的进程(PID={pid})")
                        except Exception:
                            pass
                status_parts.append(f"{version}: ❌超时")
            else:
                status_parts.append(f"{version}: ⏳")

        print(f"  [{int(elapsed)}s] {' '.join(status_parts)}")

        # 退出条件：所有版本要么completed要么timeout
        all_settled = all(s in ("completed", "timeout") for s in version_status.values())
        if all_settled:
            success_count = sum(1 for s in version_status.values() if s == "completed")
            fail_count = sum(1 for s in version_status.values() if s == "timeout")
            if fail_count == 0:
                logger.info(f"✅ {success_count}个格化session全部完成")
            else:
                logger.info(f"✅ {success_count}个格化session完成，{fail_count}个超时降级")
            break

        # 安全兜底：总超时2倍grading_timeout
        if elapsed > grading_timeout * 2:
            logger.warning(f"⚠️ 总超时({int(elapsed)}秒)，强制停止等待")
            break

        time.sleep(poll_interval)

    # 收集成功的版本——只返回成功的（340号方案）
    success_versions = {v: d for v, d in prepared_dirs.items() if version_status[v] == "completed"}
    failed_versions = [v for v in prepared_dirs if version_status[v] == "timeout"]

    # 记录到数据库（340号方案）
    phase1_results = {}
    for version in prepared_dirs:
        vdir = prepared_dirs[version]
        seg_count = 0
        seg_path = os.path.join(vdir, "segments.json")
        if os.path.exists(seg_path):
            seg_data = _read_json(seg_path)
            seg_count = len(seg_data.get("segments", seg_data if isinstance(seg_data, list) else []))
        phase1_results[version] = {
            "status": version_status[version],
            "duration_sec": int(time.time() - version_start_time[version]) if version_status[version] == "timeout" else None,
            "segments_count": seg_count,
        }

    # 存到工作目录的meta文件中，供vein_analysis_three_phase()读取
    phase1_meta = {
        "success_versions": list(success_versions.keys()),
        "failed_versions": failed_versions,
        "results": phase1_results,
    }
    with open(os.path.join(workdir_base, "phase1_grading", "phase1_results.json"), "w", encoding="utf-8") as f:
        json.dump(phase1_meta, f, ensure_ascii=False, indent=2)

    logger.info(f"格化阶段结果: 成功={list(success_versions.keys())}, 失败={failed_versions}")

    # 清理tmux session
    _cleanup_tmux_sessions_named(prepared_dirs, f"grade-{run_id:04d}")

    return success_versions


def _phase1_5_enumerate(workdir_base: str, grading_dirs: dict) -> dict:
    """阶段1.5：程序枚举闭元素——对每个版本的形式上下文运行Next Closure算法

    Returns:
        {version: closed_elements_list}——每个版本的闭元素列表
    """
    # 创建闭元素输出目录
    enum_dir = os.path.join(workdir_base, "phase1_5_enumerate")
    os.makedirs(enum_dir, exist_ok=True)

    closed_elements = {}

    for version, vdir in grading_dirs.items():
        fc_path = os.path.join(vdir, "formal_context.json")
        if not os.path.exists(fc_path):
            print(f"  ⚠️ {version} 无formal_context.json（V5不要求形式上下文），跳过")
            continue

        fc_data = _read_json(fc_path)
        G = fc_data.get("G", [])
        M = fc_data.get("M", [])
        I = fc_data.get("I", [])

        if not G or not M or not I:
            print(f"  ⚠️ {version} 形式上下文不完整，跳过")
            continue

        # 用verify_lattice_completeness.py的FormalContext枚举闭元素
        sys.path.insert(0, os.path.join(_load_repo_root(), "six"))
        from verify_lattice_completeness import FormalContext

        fc = FormalContext(G, M, I)
        all_closed = fc.enumerate_all_closed_elements()

        # 转成可序列化的格式
        closed_list = []
        for i, (extent, intent) in enumerate(all_closed):
            closed_list.append({
                "id": f"ce_{version}_{i}",
                "extent": sorted(list(extent)),
                "intent": sorted(list(intent)),
                "source_version": version,
            })

        closed_elements[version] = closed_list

        # 写入文件
        output_path = os.path.join(enum_dir, f"{version}_closed_elements.json")
        _write_json(output_path, {
            "version": version,
            "phase": "enumerate",
            "formal_context": {"G": G, "M": M, "I_count": len(I)},
            "closed_elements": closed_list,
        })

        print(f"  ✅ {version}: {len(closed_list)}个闭元素 → {output_path}")

    return closed_elements


def _phase2_synthesis(workdir_base: str, input: AnalysisInput,
                       grading_dirs: dict, closed_elements: dict, run_id: int) -> AnalysisOutput:
    """阶段2：综合分析——1个devin cli实例读4个版本格化结果+程序枚举闭元素"""
    repo_root = _load_repo_root()
    system_dir = os.path.join(repo_root, "system")

    # 创建综合分析工作目录
    synth_dir = os.path.join(workdir_base, "phase2_synthesis")
    os.makedirs(synth_dir, exist_ok=True)

    # 复制AGENTS.md模板
    agents_src = os.path.join(system_dir, SYNTHESIS_AGENTS_TEMPLATE)
    with open(agents_src, "r", encoding="utf-8") as f:
        agents_content = f.read()
    with open(os.path.join(synth_dir, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write(agents_content)

    # 复制综合分析提示词
    prompt_src = os.path.join(repo_root, SYNTHESIS_PROMPT_FILE)
    with open(prompt_src, "r", encoding="utf-8") as f:
        prompt_content = f.read()
    with open(os.path.join(synth_dir, "prompt.md"), "w", encoding="utf-8") as f:
        f.write(prompt_content)

    # 综合分析文件拆分流程控制——复制step要求文件（336号方案——4阶段不退化方案）
    import shutil
    for step_num in range(1, 5):  # step1=对比+回溯, step2=闭元素解读, step3=内容trace, step4=审计+合并
        step_src = os.path.join(repo_root, PROMPT_DIR, f"synthesis_step{step_num}_requirements.md")
        if os.path.exists(step_src):
            shutil.copy2(step_src, os.path.join(synth_dir, f"step{step_num}_requirements.md"))

    # 写input.md——题目+解答文本
    solution_block = _build_solution_block(input)
    with open(os.path.join(synth_dir, "input.md"), "w", encoding="utf-8") as f:
        f.write(solution_block)

    # 创建grading/目录——复制4个版本的格化产出
    grading_copy_dir = os.path.join(synth_dir, "grading")
    os.makedirs(grading_copy_dir, exist_ok=True)
    for version, vdir in grading_dirs.items():
        for fname in ["segments.json", "formal_context.json", "key_entities.json"]:
            src = os.path.join(vdir, fname)
            if os.path.exists(src):
                import shutil
                shutil.copy2(src, os.path.join(grading_copy_dir, f"{version}_{fname}"))

    # 创建closed_elements/目录——复制程序枚举的闭元素
    ce_copy_dir = os.path.join(synth_dir, "closed_elements")
    os.makedirs(ce_copy_dir, exist_ok=True)
    enum_dir = os.path.join(workdir_base, "phase1_5_enumerate")
    for version in PROMPT_VERSIONS:
        src = os.path.join(enum_dir, f"{version}_closed_elements.json")
        if os.path.exists(src):
            import shutil
            shutil.copy2(src, os.path.join(ce_copy_dir, f"{version}_closed_elements.json"))

    # 启动综合分析devin cli
    session_name = f"synth-{run_id:04d}"
    launch_prompt = (
        f"先加载 {synth_dir}/AGENTS.md 了解你的角色和约束，"
        f"然后加载 {synth_dir}/prompt.md 中的提示词，"
        f"读取 {synth_dir}/grading/ 目录下4个版本的格化结果，"
        f"读取 {synth_dir}/closed_elements/ 目录下程序枚举的闭元素，"
        f"读取 {synth_dir}/input.md 中的解答文本，"
        f"按提示词要求做综合分析，"
        f"完成后把产出写入 {synth_dir}/output.json 和 {synth_dir}/output.md。"
        f"全部产出写完后，在 {synth_dir}/ 下创建一个空的 DONE.md 文件作为完成信号。"
    )

    success = _launch_devin(session_name, synth_dir, launch_prompt)
    if success:
        print(f"  ✅ 综合分析启动成功: {session_name}")
    else:
        print(f"  ⚠️ 综合分析启动失败")

    # 等待综合分析完成——轮询DONE.md
    import time
    timeout = 3600  # 60分钟超时
    poll_interval = 30
    started = time.time()

    while True:
        elapsed = time.time() - started
        if elapsed > timeout:
            print(f"  ⚠️ 综合分析超时({timeout}秒)")
            break

        done = os.path.exists(os.path.join(synth_dir, "DONE.md"))
        print(f"  [{int(elapsed)}s] synthesis: {'✅' if done else '⏳'}")
        if done:
            print("  ✅ 综合分析完成")
            break
        time.sleep(poll_interval)

    # 清理综合分析devin cli实例
    if USE_TMUX:
        try:
            subprocess.run(["tmux", "kill-session", "-t", session_name],
                           capture_output=True, timeout=5)
            print(f"  🧹 已清理综合分析tmux session")
        except Exception:
            pass
    else:
        pid_path = os.path.join(synth_dir, "devin_pid.txt")
        if os.path.exists(pid_path):
            try:
                with open(pid_path) as f:
                    pid = int(f.read().strip())
                os.kill(pid, 15)
                print(f"  🧹 已清理综合分析devin cli进程: PID={pid}")
            except ProcessLookupError:
                pass
            except Exception:
                pass

    # 读取综合分析产出
    output_path = os.path.join(synth_dir, "output.json")
    if not os.path.exists(output_path):
        print(f"  ⚠️ 综合分析产出不存在: {output_path}")
        return AnalysisOutput(traces=[], veins=[], level_views=[], process="absorb")

    output_data = _read_json(output_path)

    # 转成AnalysisOutput
    traces = []
    for t in output_data.get("traces", []):
        # trace_type映射——AI输出用cross_case_merge/cross_element_meta_pattern等，
        # 映射到schema的local/non_local/global
        t_type = t.get("type", "local")
        if t_type in ("local",):
            mapped_type = "local"
        elif t_type in ("global",):
            mapped_type = "global"
        else:
            # non_local, cross_case_merge, cross_element_meta_pattern → non_local
            mapped_type = "non_local"
        traces.append(Trace(
            trace_id=t.get("id", ""),
            trace_type=mapped_type,
            level=t.get("level", 0) if isinstance(t.get("level"), int) else 0,
            pattern_description=t.get("description", ""),
            source_segment_ids=[str(s) for s in t.get("segments", [])],
        ))

    veins = []
    level_views = []

    return AnalysisOutput(traces=traces, veins=veins, level_views=level_views, process="absorb")


def _cleanup_tmux_sessions_named(prepared_dirs: dict, prefix: str):
    """清理指定前缀的devin cli实例——根据USE_TMUX开关选择清理方式"""
    for version, vdir in prepared_dirs.items():
        done_path = os.path.join(vdir, "DONE.md")
        if not os.path.exists(done_path):
            continue
        if USE_TMUX:
            session_name = f"{prefix}-{version}"
            try:
                result = subprocess.run(
                    ["tmux", "kill-session", "-t", session_name],
                    capture_output=True, text=True, timeout=5,
                )
                if result.returncode == 0:
                    print(f"  🧹 已清理 {version} 的tmux session: {session_name}")
            except Exception as e:
                print(f"  ⚠️ 清理 {version} 的tmux session失败: {e}")
        else:
            pid_path = os.path.join(vdir, "devin_pid.txt")
            if os.path.exists(pid_path):
                try:
                    with open(pid_path) as f:
                        pid = int(f.read().strip())
                    os.kill(pid, 15)
                    print(f"  🧹 已清理 {version} 的devin cli进程: PID={pid}")
                except ProcessLookupError:
                    pass
                except Exception as e:
                    print(f"  ⚠️ 清理 {version} 的devin cli进程失败: {e}")
