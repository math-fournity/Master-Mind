#!/usr/bin/env python3
"""launch_poc25c.py — POC-2.5c首批T/C双臂tmux批量驱动器

设计依据：poc25c_experiment_design.md §2/§4/§5 + first_batch_12_selection.md判据口径修正案。
  - 每题两臂各1次devin cli调用（glm-5-2, dangerous, 与续传管线同参数）
  - 顺序效应控制（§4.3）：奇数题先T后C，偶数题先C后T
  - 环境同一性（§4.2）：同日运行、同模型同参数；并发上限4
  - 每run隔离目录：prompt.txt + exports/conversation.json + meta.json

用法：
  python3 launch_poc25c.py launch   # 启动全部24个run（阻塞至全部完成/超时）
  python3 launch_poc25c.py status   # 打印当前进度
"""

import json
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent / "batch1_prompts"
# 隔离现场：D盘实验目录（无AGENTS.md无.git，devin cli不会加载任何规则文件——环境同一性）
RUN_BASE = Path("/data/math-agent-glm5.2-tmux-agents-dir/poc25c-batch1")
MODEL = "glm-5-2"
PERMISSION = "dangerous"
CONCURRENCY = 4
RUN_TIMEOUT_S = 120 * 60  # 单run上限120分钟
POLL_S = 30


def now():
    return datetime.now(timezone.utc).isoformat()


def run_dir(pid, arm):
    return RUN_BASE / f"{pid}__{arm}"


def tmux_session(pid, arm):
    return f"poc25c-{pid[-8:]}-{arm.lower()}"


def launch_one(pid, arm):
    rd = run_dir(pid, arm)
    rd.mkdir(parents=True, exist_ok=True)
    (rd / "exports").mkdir(exist_ok=True)
    # 同步repo内可审计副本prompt到隔离现场
    src_prompt = HERE / f"{pid}__{arm}" / "prompt.txt"
    dst_prompt = rd / "prompt.txt"
    if not dst_prompt.exists() or dst_prompt.read_bytes() != src_prompt.read_bytes():
        shutil.copyfile(src_prompt, dst_prompt)
    sess = tmux_session(pid, arm)
    export = rd / "exports" / "conversation.json"
    subprocess.run(["tmux", "kill-session", "-t", sess], capture_output=True)
    cmd = (
        f"cd {rd} && devin -p --prompt-file {rd/'prompt.txt'} "
        f"--model {MODEL} --respect-workspace-trust false "
        f"--permission-mode {PERMISSION} --export {export} ; "
        f"echo $? > DONE"
    )
    r = subprocess.run(["tmux", "new-session", "-d", "-s", sess, cmd], capture_output=True, text=True)
    ok = r.returncode == 0
    meta_path = rd / "meta.json"
    meta = json.loads(meta_path.read_text()) if meta_path.is_file() else {}
    meta.update({"problem_id": pid, "arm": arm, "session": sess,
                 "model": MODEL, "permission_mode": PERMISSION,
                 "launched_at": now(), "launch_ok": ok})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
    print(f"[{now()}] launched {pid} {arm} ({sess})")
    return ok


def wait_one(pid, arm):
    rd = run_dir(pid, arm)
    done = rd / "DONE"
    t0 = time.time()
    while time.time() - t0 < RUN_TIMEOUT_S:
        if done.is_file():
            code = done.read_text().strip()
            finish("done", pid, arm, exit_code=code)
            return True
        time.sleep(POLL_S)
    subprocess.run(["tmux", "kill-session", "-t", tmux_session(pid, arm)], capture_output=True)
    finish("timeout_killed", pid, arm)
    return False


def finish(state, pid, arm, **kw):
    meta_path = run_dir(pid, arm) / "meta.json"
    meta = json.loads(meta_path.read_text())
    meta["finished_at"] = now()
    meta["state"] = state
    meta.update(kw)
    if export_exists(pid, arm):
        meta["export_size"] = (run_dir(pid, arm) / "exports/conversation.json").stat().st_size
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
    print(f"[{now()}] finished {pid} {arm}: {state} {kw.get('exit_code','')}")


def export_exists(pid, arm):
    e = run_dir(pid, arm) / "exports" / "conversation.json"
    try:
        return e.is_file() and e.stat().st_size > 0
    except OSError:
        return False


def build_queue():
    """顺序交错（§4.3）：奇数题T先C后，偶数题C先T后。"""
    pids = sorted({p.parent.name.rsplit("__", 1)[0]
                   for p in HERE.glob("*__*/prompt.txt")})
    q = []
    for i, pid in enumerate(pids, start=1):
        pair = ("T", "C") if i % 2 == 1 else ("C", "T")
        q.append((i, pid, pair[0]))
        q.append((i, pid, pair[1]))
    return q


def status():
    for d in sorted(HERE.glob("*__*/")):
        meta_f = d / "meta.json"
        if not meta_f.is_file():
            print(f"{d.name:45s} NO_META")
            continue
        m = json.loads(meta_f.read_text())
        print(f"{d.name:45s} state={m.get('state','-'):15s} export={m.get('export_size','-')}")


def main():
    if len(sys.argv) < 2 or sys.argv[1] == "status":
        status()
        return
    q = build_queue()
    assert len(q) == 24, f"期望24个run，实际{len(q)}——先跑gen_prompts.py"
    print(f"queue: {len(q)} runs, concurrency={CONCURRENCY}, order={[x[2] for x in q]}")
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futures = []
        for i, pid, arm in q:
            futures.append(ex.submit(_one, pid, arm))
            time.sleep(5)  # 错峰启动
        for f in futures:
            f.result()
    print("ALL RUNS FINISHED")


def _one(pid, arm):
    if not launch_one(pid, arm):
        finish("launch_failed", pid, arm)
        return
    wait_one(pid, arm)


if __name__ == "__main__":
    main()
