#!/usr/bin/env python3
"""solver-harness: 在tmux中启动devin cli，自动采集完整trajectory。

系统架构：
  Solver工作目录（AI可见）:  /data/math-agent-glm5.2-tmux-agents-dir/<exp-id>/
  Trajectory数据目录（AI不可见）: /data/math-agent-glm5.2-tmux-agents-trajectory/<exp-id>/

数据流：
  1. 创建两个目录 + 启动mitmdump + 启动tmux session
  2. tmux内devin cli走mitmproxy代理，--export到trajectory目录
  3. MITM addon捕获GetChatMessage raw bytes → mitm/raw/
  4. 后台解码进程：raw → mitm/trajectory.jsonl（token级）
  5. sessions.db轮询进程：→ sessions_db/trajectory.jsonl（step级）
  6. tmux pipe-pane：→ tmux/tmux_pipe.log（兜底）

用法：
  python3 solver-harness.py launch --exp-id 258-matrix-test --problem-file problem.txt
  python3 solver-harness.py status --exp-id 258-matrix-test
  python3 solver-harness.py stop --exp-id 258-matrix-test
  python3 solver-harness.py decode --exp-id 258-matrix-test
  python3 solver-harness.py list
"""

import argparse
import json
import os
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ============================================================
# 路径常量
# ============================================================

SOLVER_BASE = "/data/math-agent-glm5.2-tmux-agents-dir"
TRAJECTORY_BASE = "/data/math-agent-glm5.2-tmux-agents-trajectory"
MITM_PORT = 18888
SESSIONS_DB = os.path.expanduser("~/.local/share/devin/cli/sessions.db")
SCRIPT_DIR = Path(__file__).parent.parent  # xishujuzhen/
MITM_ADDON = SCRIPT_DIR / "mitm_thinking_intercept" / "mitm_proto_capture.py"
DECODE_SCRIPT = SCRIPT_DIR / "mitm_thinking_intercept" / "decode_connect_proto.py"
TRAJECTORY_MONITOR = SCRIPT_DIR / "trajectory_monitor.py"
SOLVER_AGENTS_TEMPLATE = SCRIPT_DIR.parent / "templates" / "solver_agents_md.md"

# ============================================================
# 工具函数
# ============================================================

def solver_dir(exp_id):
    return Path(SOLVER_BASE) / exp_id

def trajectory_dir(exp_id):
    return Path(TRAJECTORY_BASE) / exp_id

def tmux_session_name(exp_id):
    return f"harness-{exp_id}"

def mitm_tmux_name():
    return "harness-mitmproxy"

def ensure_dirs(exp_id):
    """创建Solver工作目录和Trajectory数据目录的完整结构。"""
    sdir = solver_dir(exp_id)
    tdir = trajectory_dir(exp_id)
    
    # Solver目录（AI可见）
    sdir.mkdir(parents=True, exist_ok=True)
    
    # Trajectory目录（AI不可见）
    (tdir / "mitm" / "raw").mkdir(parents=True, exist_ok=True)
    (tdir / "sessions_db").mkdir(parents=True, exist_ok=True)
    (tdir / "tmux").mkdir(parents=True, exist_ok=True)
    (tdir / "exports").mkdir(parents=True, exist_ok=True)
    
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

# ============================================================
# MITM代理管理
# ============================================================

def is_mitmproxy_running():
    """检查mitmproxy是否在运行。"""
    result = subprocess.run(
        ["pgrep", "-f", "mitmdump.*harness"],
        capture_output=True, text=True
    )
    return result.returncode == 0

def ensure_mitmproxy_ca_trusted():
    """确保mitmproxy CA证书在Keychain中信任。"""
    ca_cert = os.path.expanduser("~/.mitmproxy/mitmproxy-ca-cert.pem")
    if not os.path.exists(ca_cert):
        print("ERROR: mitmproxy CA cert not found at", ca_cert)
        print("Run mitmdump once first to generate it.")
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

def start_mitmproxy(raw_dir):
    """在tmux中启动mitmproxy（全局共享，所有实验的MITM流量都走这里）。
    
    raw_dir通过环境变量MITM_RAW_DIR传给addon。
    但因为mitmproxy是共享的，我们用一个动态addon——每次实验启动时
    用独立的mitmproxy实例更好。
    """
    # 策略：每个实验启动独立的mitmproxy实例，用不同端口
    # 但端口冲突问题复杂——简化：用全局共享mitmproxy，addon把数据写到
    # 各实验的raw目录。这需要addon知道当前活跃实验。
    # 
    # 更简单：每个实验启动自己的mitmproxy在独立端口上
    # 端口分配：18888 + hash(exp_id) % 100
    pass

def start_mitmproxy_for_exp(exp_id, raw_dir, port):
    """为单个实验启动mitmproxy实例。"""
    tname = f"harness-mitm-{exp_id}"
    
    # 检查是否已在运行
    result = subprocess.run(
        ["tmux", "has-session", "-t", tname],
        capture_output=True
    )
    if result.returncode == 0:
        # 已在运行，kill后重启
        subprocess.run(["tmux", "kill-session", "-t", tname], capture_output=True)
    
    env = os.environ.copy()
    env["MITM_RAW_DIR"] = str(raw_dir)
    
    cmd = (
        f"MITM_RAW_DIR={raw_dir} "
        f"mitmdump --listen-port {port} -s {MITM_ADDON} --set ssl_insecure=true "
        f"2>{trajectory_dir(exp_id) / 'mitm' / 'mitm_stderr.log'}"
    )
    
    subprocess.run(
        ["tmux", "new-session", "-d", "-s", tname, cmd],
        capture_output=True
    )
    
    # 等mitmproxy启动
    time.sleep(2)
    
    # 验证
    result = subprocess.run(
        ["tmux", "has-session", "-t", tname],
        capture_output=True
    )
    return result.returncode == 0

def stop_mitmproxy_for_exp(exp_id):
    """停止实验的mitmproxy实例。"""
    tname = f"harness-mitm-{exp_id}"
    subprocess.run(["tmux", "kill-session", "-t", tname], capture_output=True)

# ============================================================
# 后台解码进程
# ============================================================

def start_decoder(exp_id):
    """启动后台解码进程：监控raw目录，有新.bin文件时自动解码追加到trajectory.jsonl。
    
    用一个简单的轮询脚本实现。
    """
    tdir = trajectory_dir(exp_id)
    raw_dir = tdir / "mitm" / "raw"
    jsonl_path = tdir / "mitm" / "trajectory.jsonl"
    
    # 写一个解码daemon脚本
    daemon_script = f"""
import sys, os, time, json, glob
sys.path.insert(0, "{SCRIPT_DIR}")
sys.path.insert(0, "{SCRIPT_DIR / 'mitm_thinking_intercept'}")
from decode_connect_proto import extract_streaming_data

raw_dir = "{raw_dir}"
jsonl_path = "{jsonl_path}"
seen = set()

while True:
    files = sorted(glob.glob(os.path.join(raw_dir, "chatmsg_*.bin")))
    new_files = [f for f in files if f not in seen and "_req" not in f]
    for f in new_files:
        seen.add(f)
        try:
            result = extract_streaming_data(f)
            entry = {{
                "source_file": os.path.basename(f),
                "decoded_at": time.time(),
                "total_messages": result["total_messages"],
                "content_thinking": result["content_thinking"],
                "content_chunks_count": result["content_chunks_count"],
                "tool_calls": result["tool_calls"],
            }}
            with open(jsonl_path, "a") as out:
                out.write(json.dumps(entry, ensure_ascii=False) + "\\n")
        except Exception as e:
            with open(jsonl_path, "a") as out:
                out.write(json.dumps({{"error": str(e), "file": f}}, ensure_ascii=False) + "\\n")
    time.sleep(2)
"""
    
    daemon_path = tdir / "mitm" / "_decoder_daemon.py"
    with open(daemon_path, "w") as f:
        f.write(daemon_script)
    
    tname = f"harness-decoder-{exp_id}"
    subprocess.run(
        ["tmux", "new-session", "-d", "-s", tname,
         f"{sys.executable} {daemon_path}"],
        capture_output=True
    )
    return tname

def stop_decoder(exp_id):
    tname = f"harness-decoder-{exp_id}"
    subprocess.run(["tmux", "kill-session", "-t", tname], capture_output=True)

# ============================================================
# sessions.db轮询进程
# ============================================================

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
    print(f"Solver dir:    {sdir}")
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
    info = write_session_info(exp_id, problem_file, model, prompt)
    
    # 5. MITM代理
    mitm_port = None
    if not no_mitm:
        if not ensure_mitmproxy_ca_trusted():
            print("WARN: mitmproxy CA not trusted, disabling MITM")
            no_mitm = True
        else:
            # 端口分配：18888 + hash(exp_id) % 100
            mitm_port = MITM_PORT + (hash(exp_id) % 100)
            raw_dir = tdir / "mitm" / "raw"
            if start_mitmproxy_for_exp(exp_id, raw_dir, mitm_port):
                print(f"MITM proxy started on port {mitm_port}")
                update_session_info(exp_id, {"mitm_port": mitm_port, "mitm_enabled": True})
                # 启动解码daemon
                start_decoder(exp_id)
                print(f"Decoder daemon started")
            else:
                print("WARN: MITM proxy failed to start, continuing without MITM")
                no_mitm = True
    
    if no_mitm:
        update_session_info(exp_id, {"mitm_enabled": False})
    
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
    
    if not no_mitm and mitm_port:
        # 走mitmproxy代理
        env_prefix = f"HTTPS_PROXY=http://localhost:{mitm_port} HTTP_PROXY=http://localhost:{mitm_port} "
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
    
    print(f"\n=== Launched ===")
    print(f"tmux session: {tname}")
    print(f"Observe:      tmux attach -t {tname}")
    print(f"Stop:         python3 solver-harness.py stop --exp-id {exp_id}")
    print(f"Status:       python3 solver-harness.py status --exp-id {exp_id}")
    
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
    
    # tmux sessions
    print(f"\n=== tmux sessions ===")
    for prefix in ["harness-", f"harness-mitm-{exp_id}", f"harness-decoder-{exp_id}", f"harness-dbmon-{exp_id}"]:
        result = subprocess.run(
            ["tmux", "has-session", "-t", f"harness-{exp_id}" if prefix == "harness-" else prefix],
            capture_output=True
        )
        status = "running" if result.returncode == 0 else "stopped"
        print(f"  {prefix}: {status}")
    
    # 数据统计
    print(f"\n=== Data ===")
    raw_dir = tdir / "mitm" / "raw"
    if raw_dir.exists():
        bins = list(raw_dir.glob("chatmsg_*.bin"))
        bins = [b for b in bins if "_req" not in b.name]
        print(f"  MITM raw files: {len(bins)}")
    
    mitm_jsonl = tdir / "mitm" / "trajectory.jsonl"
    if mitm_jsonl.exists():
        with open(mitm_jsonl) as f:
            lines = f.readlines()
        print(f"  MITM trajectory.jsonl: {len(lines)} entries")
    
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
    
    return 0

# ============================================================
# 主命令：stop
# ============================================================

def cmd_stop(args):
    exp_id = args.exp_id
    
    # 停止所有相关tmux session
    for tname in [
        tmux_session_name(exp_id),
        f"harness-mitm-{exp_id}",
        f"harness-decoder-{exp_id}",
        f"harness-dbmon-{exp_id}",
    ]:
        subprocess.run(["tmux", "kill-session", "-t", tname], capture_output=True)
        print(f"Stopped {tname}")
    
    update_session_info(exp_id, {"status": "stopped"})
    print(f"Experiment {exp_id} stopped.")
    return 0

# ============================================================
# 主命令：decode
# ============================================================

def cmd_decode(args):
    exp_id = args.exp_id
    tdir = trajectory_dir(exp_id)
    raw_dir = tdir / "mitm" / "raw"
    
    if not raw_dir.exists():
        print(f"No MITM raw data for {exp_id}")
        return 1
    
    result = subprocess.run(
        [sys.executable, str(DECODE_SCRIPT), str(raw_dir), "--stream"],
        cwd=str(SCRIPT_DIR.parent)
    )
    return result.returncode

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
                info_path = d / "session_info.json"
                status = "?"
                if info_path.exists():
                    with open(info_path) as f:
                        info = json.load(f)
                    status = info.get("status", "?")
                print(f"  {d.name} [{status}]")
    
    print(f"\n=== Running tmux sessions ===")
    result = subprocess.run(["tmux", "list-sessions"], capture_output=True, text=True)
    if result.returncode == 0:
        for line in result.stdout.strip().split("\n"):
            if "harness-" in line:
                print(f"  {line}")
    
    return 0

# ============================================================
# main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="solver-harness: 启动devin cli并自动采集完整trajectory")
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
    p_stop = sub.add_parser("stop", help="停止实验")
    p_stop.add_argument("--exp-id", required=True)
    
    # decode
    p_decode = sub.add_parser("decode", help="解码MITM raw数据")
    p_decode.add_argument("--exp-id", required=True)
    
    # list
    sub.add_parser("list", help="列出所有实验")
    
    args = parser.parse_args()
    
    if args.command == "launch":
        return cmd_launch(args)
    elif args.command == "status":
        return cmd_status(args)
    elif args.command == "stop":
        return cmd_stop(args)
    elif args.command == "decode":
        return cmd_decode(args)
    elif args.command == "list":
        return cmd_list(args)
    else:
        parser.print_help()
        return 1

if __name__ == "__main__":
    sys.exit(main() or 0)
