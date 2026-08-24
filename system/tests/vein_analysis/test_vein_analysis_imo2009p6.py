"""
测试脚本——用IMO 2009 P6测试vein_analysis的数据库记录和工作目录准备。

本脚本只测试：
1. 数据库记录创建（problem_entries + sessions + ai_instances）
2. 工作目录准备（AGENTS.md/prompt.md/input.md）
3. 数据库记录查询（find_problem_entries_by_problem_id）

不实际启动tmux和devin cli——避免消耗API额度。
"""

import os
import sys
import json
from pathlib import Path

# 确保在repo根目录
repo_root = str(Path(__file__).resolve().parents[3])
os.chdir(repo_root)
sys.path.insert(0, repo_root)

# 加载环境变量（手动读取.env文件）
env_path = os.path.join(repo_root, ".env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                os.environ.setdefault(key, value)

from system import db
from system.schema import AnalysisInput, SolutionRecord, Problem
from system.vein_analysis import (
    _create_workdir_base,
    _prepare_version_workdir,
    PROMPT_VERSIONS,
)


PROFILE_PATH = (
    Path(__file__).resolve().parent / "fixtures" / "imo2009p6_profile.json"
)


def main():
    # 1. 从profile.json读取IMO 2009 P6的题目和解答
    with PROFILE_PATH.open("r", encoding="utf-8") as f:
        profile = json.load(f)

    problem_text = profile["problem_text"]
    solution_text = profile["solution_text"]
    problem_id = "imo2009p6"

    print(f"题目ID: {problem_id}")
    print(f"题目长度: {len(problem_text)}字符")
    print(f"解答长度: {len(solution_text)}字符")
    print()

    # 2. 构造AnalysisInput
    problem = Problem(
        problem_id=problem_id,
        problem_text=problem_text,
        domain=profile.get("domain", "combinatorics"),
    )
    record = SolutionRecord(
        record_id=f"test_{problem_id}",
        problem=problem,
        solution_text=solution_text,
        is_verified=True,
    )
    input = AnalysisInput(
        process="absorb",
        thinking=None,
        solution_record=record,
        orphan_traces=None,
    )

    # 3. 准备工作目录（不启动tmux）
    solution_block = f"""**题目**：

{problem_text}

**解答**：

{solution_text}"""

    workdir_base = _create_workdir_base("absorb", problem_id)
    print(f"工作目录: {workdir_base}")

    prepared_dirs = {}
    for version in PROMPT_VERSIONS:
        vdir = _prepare_version_workdir(workdir_base, version, solution_block, problem_id)
        prepared_dirs[version] = vdir
        # 验证文件
        files = os.listdir(vdir)
        assert "AGENTS.md" in files, f"{version}缺少AGENTS.md"
        assert "prompt.md" in files, f"{version}缺少prompt.md"
        assert "input.md" in files, f"{version}缺少input.md"
        print(f"  {version}: ✅ AGENTS.md + prompt.md + input.md")

    print()

    # 4. 创建数据库记录
    session_key = db.create_session(
        session_type="absorb",
        problem_id=problem_id,
        working_directory=workdir_base,
    )
    print(f"会话记录: {session_key}")

    entry_key = db.create_problem_entry(
        problem_id=problem_id,
        process="absorb",
        working_directory=workdir_base,
        record_id=record.record_id,
        versions=list(PROMPT_VERSIONS),
        version_workdirs={v: str(d) for v, d in prepared_dirs.items()},
        has_orphan_traces=False,
        session_id=session_key,
    )
    print(f"题目录入记录: {entry_key}")

    # 创建4个AI实例记录
    ai_instance_ids = {}
    session_names = {}
    for version in PROMPT_VERSIONS:
        vdir = prepared_dirs[version]
        session_name = f"absorb-vein_analysis-{problem_id}-{version}"
        session_names[version] = session_name
        ai_key = db.create_ai_instance(
            session_id=session_key,
            ai_role="parser",
            working_directory=str(vdir),
            problem_id=problem_id,
            tmux_session=session_name,
            version=version,
        )
        ai_instance_ids[version] = ai_key
        print(f"  {version} AI实例: {ai_key}")

    # 更新题目录入记录
    db.update_problem_entry(
        entry_key,
        session_names=session_names,
        ai_instance_ids=ai_instance_ids,
    )
    print()

    # 5. 验证数据库记录——查找题目的所有录入记录
    print("=== 验证：查找题目录入记录 ===")
    entries = db.find_problem_entries_by_problem_id(problem_id)
    print(f"找到{len(entries)}条录入记录:")
    for e in entries:
        print(f"  _key: {e['_key']}")
        print(f"  problem_id: {e['problem_id']}")
        print(f"  process: {e['process']}")
        print(f"  status: {e['status']}")
        print(f"  working_directory: {e['working_directory']}")
        print(f"  versions: {e['versions']}")
        print(f"  session_names: {e.get('session_names', {})}")
        print(f"  ai_instance_ids: {e.get('ai_instance_ids', {})}")
        print(f"  started_at: {e['started_at']}")
        print()

    # 6. 验证读取单条记录
    print("=== 验证：读取单条录入记录 ===")
    entry = db.get_problem_entry(entry_key)
    assert entry is not None, "录入记录不存在"
    assert entry["problem_id"] == problem_id
    assert entry["process"] == "absorb"
    assert entry["status"] == "running"
    print(f"✅ 录入记录读取成功: {entry_key}")

    # 7. 清理——标记为completed（测试完成）
    db.update_problem_entry(
        entry_key,
        status="completed",
        trace_count=0,  # 测试模式没有实际跑AI
    )
    db.update_session(session_key, status="completed", result_summary="测试完成")
    for ai_key in ai_instance_ids.values():
        db.update_ai_instance(ai_key, status="completed", end_reason="测试完成")

    print()
    print("=== 测试完成 ===")
    print(f"题目录入记录ID: {entry_key}")
    print(f"未来查找这道题的录入信息: db.find_problem_entries_by_problem_id('{problem_id}')")


if __name__ == "__main__":
    main()
