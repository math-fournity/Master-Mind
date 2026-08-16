#!/usr/bin/env python3
import hashlib, json

raw_path = "raw_solver_trajectory.txt"
with open(raw_path, "rb") as f:
    raw = f.read()

print("total bytes:", len(raw))
print("whole sha256:", hashlib.sha256(raw).hexdigest())
print()

# Find each [NN] line boundaries (start, end-exclusive of line content excluding newline)
lines = []
i = 0
for li, line in enumerate(raw.split(b"\n")):
    start = i
    end = i + len(line)
    lines.append((start, end, line))
    i = end + 1  # +1 for the newline byte

for idx, (s, e, line) in enumerate(lines):
    seg = raw[s:e]
    print(f"[{idx:02d}] start={s} end={e} len={e-s} sha={hashlib.sha256(seg).hexdigest()}")
    print(f"     text={line.decode('utf-8')!r}")

print()
print("=== compare with reasoning-trajectory.json spans ===")
with open("reasoning-trajectory.json") as f:
    data = json.load(f)

for ev in data["events"]:
    sp = ev["source_span"]
    s, e = sp["start"], sp["end"]
    seg = raw[s:e]
    calc = hashlib.sha256(seg).hexdigest()
    given = sp["sha256"]
    match = "OK" if calc == given else "MISMATCH"
    print(f"{ev['event_id']} start={s} end={e} len={e-s} {match}")
    print(f"   given={given}")
    print(f"   calc ={calc}")
    print(f"   text={seg.decode('utf-8', 'replace')!r}")
