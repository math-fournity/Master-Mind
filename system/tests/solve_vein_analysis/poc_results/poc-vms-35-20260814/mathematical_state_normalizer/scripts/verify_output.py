#!/usr/bin/env python3
import hashlib, json

raw_path = "raw_solver_trajectory.txt"
with open(raw_path, "rb") as f:
    raw = f.read()

with open("normalized-reasoning-trajectory.json") as f:
    data = json.load(f)

# 1. schema/shape checks
allowed_top = {"schema_version", "trajectory_id", "problem_id", "source", "events"}
assert set(data.keys()) == allowed_top, f"top keys: {set(data.keys())}"
assert set(data["source"].keys()) == {"carrier", "source_artifact_ref", "source_artifact_sha256"}
assert data["source"]["source_artifact_sha256"] == hashlib.sha256(raw).hexdigest()

allowed_ev = {"event_id","sequence_index","event_kind","text","canonical_math_state_id",
              "attributes","status","source_span","incoming_edges"}
allowed_span = {"start","end","sha256"}
allowed_edge = {"source_event_id","relation","evidence"}
valid_kinds = {"STATE","DECISION","FAILURE","RETURN","SYNTHESIS","CONCLUSION"}
valid_status = {"ACTIVE","ABANDONED","CONTRADICTED","SOLVED","UNKNOWN"}
valid_rel = {"CONTINUE","REFINE","BRANCH_FROM","CONTRADICT","ABANDON","REVISIT","REUSE","DEPENDS_ON","MERGE","CONCLUDE"}

events = data["events"]
assert len(events) == 10, f"event count {len(events)}"

for i, ev in enumerate(events):
    assert set(ev.keys()) == allowed_ev, f"{ev['event_id']} keys {set(ev.keys())}"
    assert ev["event_id"] == f"e{i}", f"id mismatch {ev['event_id']}"
    assert ev["sequence_index"] == i
    assert ev["event_kind"] in valid_kinds, ev["event_kind"]
    assert ev["status"] in valid_status, ev["status"]
    sp = ev["source_span"]
    assert set(sp.keys()) == allowed_span, f"span keys {set(sp.keys())}"
    s,e = sp["start"], sp["end"]
    seg = raw[s:e]
    assert hashlib.sha256(seg).hexdigest() == sp["sha256"], f"{ev['event_id']} span sha mismatch"
    # no newline byte inside span
    assert b"\n" not in seg, f"{ev['event_id']} span contains newline"
    for edge in ev["incoming_edges"]:
        assert set(edge.keys()) == allowed_edge, f"edge keys {set(edge.keys())}"
        assert edge["relation"] in valid_rel, edge["relation"]
        # no edge from later to earlier
        src = int(edge["source_event_id"][1:])
        assert src < i, f"{ev['event_id']} edge from later {edge['source_event_id']}"

# 2. MERGE invariant: at least two evidence-bearing semantic parents
for i, ev in enumerate(events):
    merges = [ed for ed in ev["incoming_edges"] if ed["relation"]=="MERGE"]
    if merges:
        assert len(merges) >= 2, f"{ev['event_id']} MERGE with <2 parents"
        for m in merges:
            assert m["evidence"].strip(), f"{ev['event_id']} MERGE edge lacks evidence"

# 3. semantic revisit: occurrences sharing canonical state => check e0/e3
shared = {}
for ev in events:
    shared.setdefault(ev["canonical_math_state_id"], []).append(ev["event_id"])
print("canonical state -> events:", shared)

# 4. dump corrections summary
print("\n=== status per event ===")
for ev in events:
    print(f"  {ev['event_id']} {ev['status']:10s} {ev['canonical_math_state_id']}")

print("\n=== edges ===")
for ev in events:
    for ed in ev["incoming_edges"]:
        print(f"  {ed['source_event_id']} --{ed['relation']:11s}--> {ev['event_id']}")

print("\nALL CHECKS PASSED")
