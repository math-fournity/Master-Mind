#!/usr/bin/env python3
"""solver-harness: 在tmux中启动devin cli，自动采集完整trajectory。

v1设计（全局共享mitmproxy + 事后批量解码）：
  Solver工作目录（AI可见）:  /data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/
  Trajectory数据目录（AI不可见）: /data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/
  共享MITM raw目录: /data/math-agent-glm5.2-tmux-agents-trajectory/_shared/mitm_raw/

数据流：
  1. 全局共享mitmproxy（固定18888端口，--allow-hosts限制只拦截devin host）
  2. 每实验：创建目录 + 启动devin cli（走代理）+ pipe-pane兜底 + db轮询
  3. devin cli启动后回填devin_session_id（从sessions.db查找work_dir对应session）
  4. 实验stop时调用decode-all：扫描共享raw目录，按session_id分发到各实验

用法：
  python3 solver_harness.py launch --exp-id 258-matrix-test --problem-file problem.txt
  python3 solver_harness.py status --exp-id 258-matrix-test
  python3 solver_harness.py stop --exp-id 258-matrix-test
  python3 solver_harness.py list
  python3 solver_harness.py decode-all
  python3 solver_harness.py mitm start|stop|status
"""

import argparse
import json
import os
import shutil
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# 导入protobuf解码器（模块级，供_extract_session_id使用）
sys.path.insert(0, str(Path(__file__).parent.parent / "mitm_thinking_intercept"))
from decode_connect_proto import extract_streaming_data, parse_connect_stream, decode_protobuf

# ============================================================
# 路径常量
# ============================================================

SOLVER_BASE = "/data/math-agent-glm5.2-tmux-agents-dir"
TRAJECTORY_BASE = "/data/math-agent-glm5.2-tmux-agents-trajectory"
SHARED_RAW_DIR = os.path.join(TRAJECTORY_BASE, "_shared", "mitm_raw")
MITM_PORT = 18888
MITM_ALLOW_HOSTS = r"server\.self-serve\.windsurf\.com|api\.devin\.ai|static\.devin\.ai"
SESSIONS_DB = os.path.expanduser("~/.local/share/devin/cli/sessions.db")
SCRIPT_DIR = Path(__file__).parent.parent  # xishujuzhen/
MITM_ADDON = SCRIPT_DIR / "mitm_thinking_intercept" / "mitm_proto_capture.py"
DECODE_SCRIPT = SCRIPT_DIR / "mitm_thinking_intercept" / "decode_connect_proto.py"
TRAJECTORY_MONITOR = SCRIPT_DIR / "trajectory_monitor.py"
SOLVER_AGENTS_TEMPLATE = SCRIPT_DIR.parent / "templates" / "solver_agents_md.md"
MITM_TMUX_NAME = "harness-mitmproxy"

# ============================================================
# 工具函数
# ============================================================

def solver_dir(exp_id):
    return Path(SOLVER_BASE) / exp_id

def trajectory_dir(exp_id):
    return Path(TRAJECTORY_BASE) / exp_id

def tmux_session_name(exp_id):
    return f"harness-{exp_id}"

def ensure_dirs(exp_id):
    """创建Solver工作目录和Trajectory数据目录的完整结构。"""
    sdir = solver_dir(exp_id)
    tdir = trajectory_dir(exp_id)

    # Solver目录（AI可见）
    sdir.mkdir(parents=True, exist_ok=True)

    # Trajectory目录（AI不可见）
    (tdir / "mitm").mkdir(parents=True, exist_ok=True)
    (tdir / "sessions_db").mkdir(parents=True, exist_ok=True)
    (tdir / "tmux").mkdir(parents=True, exist_ok=True)
    (tdir / "exports").mkdir(parents=True, exist_ok=True)

    # 共享raw目录
    os.makedirs(SHARED_RAW_DIR, exist_ok=True)

    return sdir, tdir

def write_session_info(exp_id, problem_file, model, prompt, extra=None):
    """写session_info.json到trajectory目录。"""
    info = {
        "exp_id": exp_id,
        "model": model,
        "prompt": prompt,
        "problem_file": problem_file,
        "solver_dir": str(solver_dir(exp_id)),
        "trajectory_dir": str(trajectory_dir(exp_id)),
        "tmux_session": tmux_session_name(exp_id),
        "mitm_port": MITM_PORT,
        "mitm_enabled": True,
        "devin_session_id": None,
        "start_timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "launching",
    }
    if extra:
        info.update(extra)

    info_path = trajectory_dir(exp_id) / "session_info.json"
    with open(info_path, "w") as f:
        json.dump(info, f, indent=2, ensure_ascii=False)
    return info

def update_session_info(exp_id, updates):
    """更新session_info.json。"""
    info_path = trajectory_dir(exp_id) / "session_info.json"
    if not info_path.exists():
        return
    with open(info_path) as f:
        info = json.load(f)
    info.update(updates)
    info["updated_at"] = datetime.now(timezone.utc).isoformat()
    with open(info_path, "w") as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

def tmux_has_session(name):
    """检查tmux session是否存在。"""
    result = subprocess.run(
        ["tmux", "has-session", "-t", name],
        capture_output=True
    )
    return result.returncode == 0

# ============================================================
# 共享mitmproxy管理
# ============================================================

def is_mitmproxy_running():
    """检查共享mitmproxy是否在运行。"""
    return tmux_has_session(MITM_TMUX_NAME)

def ensure_mitmproxy_ca_trusted():
    """确保mitmproxy CA证书在Keychain中信任。"""
    ca_cert = os.path.expanduser("~/.mitmproxy/mitmproxy-ca-cert.pem")
    if not os.path.exists(ca_cert):
        print("ERROR: mitmproxy CA cert not found at", ca_cert)
        print("Run 'mitmdump' once first to generate it.")
        return False

    # 检查是否已信任
    result = subprocess.run(
        ["security", "find-certificate", "-c", "mitmproxy",
         os.path.expanduser("~/Library/Keychains/login.keychain-db")],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        return True  # 已信任

    # 添加信任
    print("Adding mitmproxy CA to Keychain (requires password)...")
    result = subprocess.run(
        ["security", "add-trusted-cert", "-d", "-r", "trustRoot",
         "-k", os.path.expanduser("~/Library/Keychains/login.keychain-db"),
         ca_cert],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("ERROR: Failed to add CA cert:", result.stderr)
        return False
    return True

def start_shared_mitmproxy():
    """启动全局共享mitmproxy实例（固定18888端口，--allow-hosts限制只拦截devin host）。"""
    if is_mitmproxy_running():
        print(f"mitmproxy already running (tmux: {MITM_TMUX_NAME})")
        return True

    if not ensure_mitmproxy_ca_trusted():
        return False

    # 确保共享raw目录存在
    os.makedirs(SHARED_RAW_DIR, exist_ok=True)

    stderr_log = os.path.join(TRAJECTORY_BASE, "_shared", "mitm_stderr.log")
    os.makedirs(os.path.dirname(stderr_log), exist_ok=True)

    cmd = (
        f"MITM_RAW_DIR={SHARED_RAW_DIR} "
        f"mitmdump --listen-port {MITM_PORT} "
        f"--allow-hosts \"{MITM_ALLOW_HOSTS}\" "
        f"-s {MITM_ADDON} --set ssl_insecure=true "
        f"2>{stderr_log}"
    )

    subprocess.run(
        ["tmux", "new-session", "-d", "-s", MITM_TMUX_NAME, cmd],
        capture_output=True
    )

    # 等mitmproxy启动
    time.sleep(3)

    if is_mitmproxy_running():
        print(f"mitmproxy started on port {MITM_PORT} (tmux: {MITM_TMUX_NAME})")
        print(f"  raw dir: {SHARED_RAW_DIR}")
        print(f"  allow-hosts: {MITM_ALLOW_HOSTS}")
        return True
    else:
        print("ERROR: mitmproxy failed to start")
        print(f"  check stderr: {stderr_log}")
        return False

def stop_shared_mitmproxy():
    """停止全局共享mitmproxy实例。"""
    subprocess.run(["tmux", "kill-session", "-t", MITM_TMUX_NAME], capture_output=True)
    print(f"mitmproxy stopped (tmux: {MITM_TMUX_NAME})")

# ============================================================
# sessions.db轮询 + devin_session_id回填
# ============================================================

def find_session_id_by_work_dir(work_dir):
    """从sessions.db中查找work_dir对应的最新session_id。"""
    if not os.path.exists(SESSIONS_DB):
        return None
    conn = sqlite3.connect(SESSIONS_DB)
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT id FROM sessions WHERE working_directory = ? ORDER BY created_at DESC LIMIT 1",
            (str(work_dir),),
        )
        row = cur.fetchone()
        return row[0] if row else None
    finally:
        conn.close()

def backfill_devin_session_id(exp_id, max_wait=30):
    """等待devin cli在sessions.db中出现，回填devin_session_id到session_info.json。

    devin cli启动后需要几秒才在sessions.db中创建session记录。
    最多等max_wait秒。
    """
    sdir = solver_dir(exp_id)
    print(f"Waiting for devin session to appear in sessions.db (max {max_wait}s)...")

    waited = 0
    while waited < max_wait:
        session_id = find_session_id_by_work_dir(sdir)
        if session_id:
            update_session_info(exp_id, {"devin_session_id": session_id})
            print(f"  Found devin_session_id: {session_id}")
            return session_id
        time.sleep(2)
        waited += 2

    print(f"  WARN: devin session not found in sessions.db after {max_wait}s")
    print(f"  (session_info.json devin_session_id will remain null)")
    return None

def start_db_monitor(exp_id):
    """启动sessions.db轮询进程：step级trajectory。"""
    tdir = trajectory_dir(exp_id)
    sdir = solver_dir(exp_id)
    jsonl_path = tdir / "sessions_db" / "trajectory.jsonl"

    tname = f"harness-dbmon-{exp_id}"
    subprocess.run(
        ["tmux", "new-session", "-d", "-s", tname,
         f"{sys.executable} {TRAJECTORY_MONITOR} "
         f"--work-dir {sdir} --interval 3 --max-wait 7200 "
         f"-o {jsonl_path}"],
        capture_output=True
    )
    return tname

def stop_db_monitor(exp_id):
    tname = f"harness-dbmon-{exp_id}"
    subprocess.run(["tmux", "kill-session", "-t", tname], capture_output=True)

# ============================================================
# decode-all：按session_id分发
# ============================================================

def build_session_id_to_exp_mapping():
    """构建session_id → exp_id映射表（读所有实验的session_info.json）。"""
    mapping = {}
    tbase = Path(TRAJECTORY_BASE)
    if not tbase.exists():
        return mapping

    for d in tbase.iterdir():
        if not d.is_dir() or d.name == "_shared":
            continue
        info_path = d / "session_info.json"
        if not info_path.exists():
            continue
        try:
            with open(info_path) as f:
                info = json.load(f)
            sid = info.get("devin_session_id")
            if sid:
                mapping[sid] = d.name
        except (json.JSONDecodeError, KeyError):
            continue

    return mapping

def cmd_decode_all(args):
    """扫描共享raw目录，解码每个.bin，按session_id分发到各实验的mitm/trajectory.jsonl。"""
    if not os.path.exists(SHARED_RAW_DIR):
        print(f"Shared raw dir not found: {SHARED_RAW_DIR}")
        return 1

    # 构建映射表
    mapping = build_session_id_to_exp_mapping()
    if not mapping:
        print("No devin_session_id mapping found (no experiments with backfilled session_id)")
        print("Will decode all to _shared/unmatched/")
    else:
        print(f"Session mapping ({len(mapping)} experiments):")
        for sid, exp_id in mapping.items():
            print(f"  {sid[:8]}... → {exp_id}")

    # 扫描所有.bin文件（排除_req文件）
    raw_files = sorted([
        f for f in os.listdir(SHARED_RAW_DIR)
        if f.endswith(".bin") and "_req" not in f
    ])

    if not raw_files:
        print(f"No .bin files in {SHARED_RAW_DIR}")
        return 0

    print(f"\nDecoding {len(raw_files)} files...")

    unmatched_dir = os.path.join(TRAJECTORY_BASE, "_shared", "unmatched")
    os.makedirs(unmatched_dir, exist_ok=True)

    stats = {"matched": 0, "unmatched": 0, "errors": 0}

    for fname in raw_files:
        fpath = os.path.join(SHARED_RAW_DIR, fname)
        try:
            result = extract_streaming_data(fpath)

            # 提取session_id（field 17）——需要从原始protobuf中找
            session_id = _extract_session_id(fpath)

            # 确定目标实验
            exp_id = mapping.get(session_id) if session_id else None

            if exp_id:
                target_jsonl = trajectory_dir(exp_id) / "mitm" / "trajectory.jsonl"
                os.makedirs(os.path.dirname(target_jsonl), exist_ok=True)
                stats["matched"] += 1
            else:
                target_jsonl = Path(unmatched_dir) / "trajectory.jsonl"
                stats["unmatched"] += 1

            entry = {
                "source_file": fname,
                "session_id": session_id,
                "decoded_at": time.time(),
                "total_messages": result["total_messages"],
                "content_thinking": result["content_thinking"],
                "content_chunks_count": result["content_chunks_count"],
                "tool_calls": result["tool_calls"],
            }

            with open(target_jsonl, "a") as out:
                out.write(json.dumps(entry, ensure_ascii=False) + "\n")

        except Exception as e:
            stats["errors"] += 1
            error_log = os.path.join(unmatched_dir, "decode_errors.jsonl")
            with open(error_log, "a") as out:
                out.write(json.dumps({"error": str(e), "file": fname}, ensure_ascii=False) + "\n")

    print(f"\nDone: {stats['matched']} matched, {stats['unmatched']} unmatched, {stats['errors']} errors")
    if stats["unmatched"] > 0:
        print(f"  unmatched → {unmatched_dir}/trajectory.jsonl")
    if stats["errors"] > 0:
        print(f"  errors → {unmatched_dir}/decode_errors.jsonl")

    return 0

def _extract_session_id(filepath):
    """从GetChatMessage响应中提取session_id（protobuf field 17）。"""
    with open(filepath, "rb") as f:
        data = f.read()

    messages = parse_connect_stream(data)

    for flags, msg_data in messages:
        decoded = decode_protobuf(msg_data)
        for field_num, type_name, value in decoded:
            if field_num == 17 and type_name == "string":
                return value
            # session_id也可能在嵌套message中
            if field_num == 17 and type_name == "message":
                for fn, ft, fv in value:
                    if ft == "string":
                        return fv

    return None

# ============================================================
# 主命令：launch
# ============================================================

def cmd_launch(args):
    exp_id = args.exp_id
    problem_file = args.problem_file
    model = args.model
    prompt = args.prompt or "请读取当前目录下的problem.txt文件，解答其中的数学题。"
    no_mitm = args.no_mitm

    print(f"=== Launching solver-harness for {exp_id} ===")

    # 1. 创建目录
    sdir, tdir = ensure_dirs(exp_id)
    print(f"Solver dir:     {sdir}")
    print(f"Trajectory dir: {tdir}")

    # 2. 复制AGENTS.md模板
    agents_md = sdir / "AGENTS.md"
    if not agents_md.exists():
        if SOLVER_AGENTS_TEMPLATE.exists():
            shutil.copy(SOLVER_AGENTS_TEMPLATE, agents_md)
            print(f"Copied AGENTS.md template")
        else:
            print(f"WARN: template not found at {SOLVER_AGENTS_TEMPLATE}")

    # 3. 复制题目文件
    if problem_file and os.path.exists(problem_file):
        shutil.copy(problem_file, sdir / "problem.txt")
        print(f"Copied problem.txt from {problem_file}")
    elif problem_file:
        print(f"ERROR: problem file not found: {problem_file}")
        return 1

    # 4. 写session_info
    write_session_info(exp_id, problem_file, model, prompt)

    # 5. 确保共享mitmproxy运行
    mitm_enabled = not no_mitm
    if not no_mitm:
        if not is_mitmproxy_running():
            if not start_shared_mitmproxy():
                print("WARN: mitmproxy failed to start, continuing without MITM")
                mitm_enabled = False
        else:
            print(f"mitmproxy already running on port {MITM_PORT}")
    else:
        print("MITM disabled (--no-mitm)")

    update_session_info(exp_id, {"mitm_enabled": mitm_enabled})

    # 6. 启动sessions.db轮询
    start_db_monitor(exp_id)
    print(f"DB monitor started (step-level trajectory)")

    # 7. 启动devin cli in tmux
    tname = tmux_session_name(exp_id)
    export_path = tdir / "exports" / "conversation.json"
    tmux_pipe_path = tdir / "tmux" / "tmux_pipe.log"
    tmux_log_path = tdir / "tmux" / "tmux.log"

    # 构建devin cli命令
    devin_cmd = f"devin -p '{prompt}' --model {model} --respect-workspace-trust false --permission-mode dangerous --export {export_path}"

    if mitm_enabled:
        # 走mitmproxy代理
        env_prefix = f"HTTPS_PROXY=http://localhost:{MITM_PORT} HTTP_PROXY=http://localhost:{MITM_PORT} "
        full_cmd = f"cd {sdir} && {env_prefix}{devin_cmd} 2>&1 | tee {tmux_log_path}"
    else:
        full_cmd = f"cd {sdir} && {devin_cmd} 2>&1 | tee {tmux_log_path}"

    subprocess.run(
        ["tmux", "new-session", "-d", "-s", tname, full_cmd],
        capture_output=True
    )

    # 8. 启动pipe-pane兜底
    time.sleep(1)
    subprocess.run(
        ["tmux", "pipe-pane", "-t", tname, f"cat >> {tmux_pipe_path}"],
        capture_output=True
    )

    update_session_info(exp_id, {"status": "running"})

    # 9. 回填devin_session_id（异步，不阻塞launch返回）
    print(f"\nBackfilling devin_session_id...")
    backfill_devin_session_id(exp_id, max_wait=30)

    print(f"\n=== Launched ===")
    print(f"tmux session: {tname}")
    print(f"Observe:      tmux attach -t {tname}")
    print(f"Stop:         python3 solver_harness.py stop --exp-id {exp_id}")
    print(f"Status:       python3 solver_harness.py status --exp-id {exp_id}")

    return 0

# ============================================================
# 主命令：status
# ============================================================

def cmd_status(args):
    exp_id = args.exp_id
    tdir = trajectory_dir(exp_id)

    if not tdir.exists():
        print(f"Experiment {exp_id} not found (no trajectory dir)")
        return 1

    # session_info
    info_path = tdir / "session_info.json"
    if info_path.exists():
        with open(info_path) as f:
            info = json.load(f)
        print(f"=== Session Info ===")
        for k, v in info.items():
            print(f"  {k}: {v}")

    # tmux sessions（只查该实验的，不查共享mitmproxy）
    print(f"\n=== tmux sessions ===")
    for tname, label in [
        (tmux_session_name(exp_id), "devin cli"),
        (f"harness-dbmon-{exp_id}", "db monitor"),
    ]:
        status = "running" if tmux_has_session(tname) else "stopped"
        print(f"  {label} ({tname}): {status}")

    # 共享mitmproxy状态
    mitm_status = "running" if is_mitmproxy_running() else "stopped"
    print(f"  shared mitmproxy ({MITM_TMUX_NAME}): {mitm_status}")

    # 数据统计
    print(f"\n=== Data ===")
    mitm_jsonl = tdir / "mitm" / "trajectory.jsonl"
    if mitm_jsonl.exists():
        with open(mitm_jsonl) as f:
            lines = f.readlines()
        print(f"  MITM trajectory.jsonl: {len(lines)} entries")
    else:
        print(f"  MITM trajectory.jsonl: not yet decoded (run 'decode-all' after stop)")

    db_jsonl = tdir / "sessions_db" / "trajectory.jsonl"
    if db_jsonl.exists():
        with open(db_jsonl) as f:
            lines = f.readlines()
        print(f"  DB trajectory.jsonl: {len(lines)} entries")

    tmux_pipe = tdir / "tmux" / "tmux_pipe.log"
    if tmux_pipe.exists():
        print(f"  tmux_pipe.log: {tmux_pipe.stat().st_size} bytes")

    export = tdir / "exports" / "conversation.json"
    if export.exists():
        print(f"  conversation.json: {export.stat().st_size} bytes")

    # 共享raw目录统计
    if os.path.exists(SHARED_RAW_DIR):
        raw_files = [f for f in os.listdir(SHARED_RAW_DIR)
                     if f.endswith(".bin") and "_req" not in f]
        print(f"  shared raw files: {len(raw_files)} (all experiments)")

    return 0

# ============================================================
# 主命令：stop
# ============================================================

def cmd_stop(args):
    exp_id = args.exp_id
    decode = not args.no_decode  # 默认stop时自动decode

    print(f"=== Stopping {exp_id} ===")

    # 停止该实验的tmux sessions（不影响共享mitmproxy）
    for tname, label in [
        (tmux_session_name(exp_id), "devin cli"),
        (f"harness-dbmon-{exp_id}", "db monitor"),
    ]:
        if tmux_has_session(tname):
            subprocess.run(["tmux", "kill-session", "-t", tname], capture_output=True)
            print(f"Stopped {label} ({tname})")
        else:
            print(f"{label} ({tname}) not running")

    update_session_info(exp_id, {"status": "stopped"})

    # 自动调用decode-all
    if decode:
        print(f"\nDecoding MITM raw data...")
        cmd_decode_all(args)

    print(f"\nExperiment {exp_id} stopped.")
    print(f"  (shared mitmproxy is still running — use 'mitm stop' to stop it)")
    return 0

# ============================================================
# 主命令：list
# ============================================================

def cmd_list(args):
    print(f"=== Solver experiments ===")
    sbase = Path(SOLVER_BASE)
    if sbase.exists():
        for d in sorted(sbase.iterdir()):
            if d.is_dir():
                print(f"  {d.name}")

    print(f"\n=== Trajectory data ===")
    tbase = Path(TRAJECTORY_BASE)
    if tbase.exists():
        for d in sorted(tbase.iterdir()):
            if d.is_dir():
                if d.name == "_shared":
                    # 共享目录显示raw文件数
                    raw_files = [f for f in d.iterdir()
                                 if f.name.endswith(".bin") and "_req" not in f.name] if (d / "mitm_raw").exists() else []
                    raw_count = len(list((d / "mitm_raw").glob("chatmsg_*.bin"))) if (d / "mitm_raw").exists() else 0
                    print(f"  _shared [mitmproxy raw: {raw_count} files]")
                    continue
                info_path = d / "session_info.json"
                status = "?"
                if info_path.exists():
                    try:
                        with open(info_path) as f:
                            info = json.load(f)
                        status = info.get("status", "?")
                    except json.JSONDecodeError:
                        pass
                print(f"  {d.name} [{status}]")

    print(f"\n=== Running tmux sessions ===")
    result = subprocess.run(["tmux", "list-sessions"], capture_output=True, text=True)
    if result.returncode == 0:
        for line in result.stdout.strip().split("\n"):
            if "harness-" in line:
                print(f"  {line}")
    else:
        print("  (no tmux sessions)")

    return 0

# ============================================================
# 主命令：mitm
# ============================================================

def cmd_mitm(args):
    sub = args.subcommand

    if sub == "start":
        start_shared_mitmproxy()
        return 0
    elif sub == "stop":
        stop_shared_mitmproxy()
        return 0
    elif sub == "status":
        if is_mitmproxy_running():
            print(f"mitmproxy: RUNNING (tmux: {MITM_TMUX_NAME}, port: {MITM_PORT})")
            print(f"  raw dir: {SHARED_RAW_DIR}")
            print(f"  allow-hosts: {MITM_ALLOW_HOSTS}")
            if os.path.exists(SHARED_RAW_DIR):
                raw_files = [f for f in os.listdir(SHARED_RAW_DIR)
                             if f.endswith(".bin") and "_req" not in f]
                print(f"  raw files captured: {len(raw_files)}")
        else:
            print(f"mitmproxy: STOPPED")
            print(f"  start with: python3 solver_harness.py mitm start")
        return 0
    else:
        print("Usage: mitm start|stop|status")
        return 1

# ============================================================
# main
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="solver-harness: 启动devin cli并自动采集完整trajectory (v1)"
    )
    sub = parser.add_subparsers(dest="command")

    # launch
    p_launch = sub.add_parser("launch", help="启动一个实验")
    p_launch.add_argument("--exp-id", required=True, help="实验ID（如 258-matrix-test）")
    p_launch.add_argument("--problem-file", help="题目文件路径")
    p_launch.add_argument("--model", default="glm-5-2", help="模型名")
    p_launch.add_argument("--prompt", help="自定义prompt（默认读problem.txt）")
    p_launch.add_argument("--no-mitm", action="store_true", help="不启用MITM代理")

    # status
    p_status = sub.add_parser("status", help="查看实验状态")
    p_status.add_argument("--exp-id", required=True)

    # stop
    p_stop = sub.add_parser("stop", help="停止实验（不影响共享mitmproxy）")
    p_stop.add_argument("--exp-id", required=True)
    p_stop.add_argument("--no-decode", action="store_true", help="stop时不自动decode")

    # list
    sub.add_parser("list", help="列出所有实验")

    # decode-all
    sub.add_parser("decode-all", help="解码共享raw目录，按session_id分发到各实验")

    # mitm
    p_mitm = sub.add_parser("mitm", help="管理共享mitmproxy")
    p_mitm.add_argument("subcommand", choices=["start", "stop", "status"], help="start/stop/status")

    args = parser.parse_args()

    if args.command == "launch":
        return cmd_launch(args)
    elif args.command == "status":
        return cmd_status(args)
    elif args.command == "stop":
        return cmd_stop(args)
    elif args.command == "list":
        return cmd_list(args)
    elif args.command == "decode-all":
        return cmd_decode_all(args)
    elif args.command == "mitm":
        return cmd_mitm(args)
    else:
        parser.print_help()
        return 1

if __name__ == "__main__":
    sys.exit(main() or 0)
