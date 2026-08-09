#!/usr/bin/env python3
"""Insert profile.json into ArangoDB and update progress record."""
import json
import sys
from datetime import datetime, timezone

# Load environment variables from .env
import os
env_path = "~/master-mind-glm5.2-worktree/.env"
with open(env_path, "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#") or not line or "=" not in line:
            continue
        key, _, val = line.partition("=")
        val = val.strip().strip('"').strip("'")
        os.environ.setdefault(key.strip(), val)

from arango import ArangoClient

# Connection info
host = os.environ.get("ARANGO_HOST", "http://localhost:8529")
db_name = os.environ.get("ARANGO_DB", "xishujuzhen_math_glm52")
username = os.environ.get("ARANGO_USER", "root")
password = os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")

print(f"Connecting to {host}, database: {db_name}")

client = ArangoClient(hosts=host)
db = client.db(db_name, username=username, password=password)

# Read profile.json
profile_path = "~/master-mind-glm5.2-worktree/subagents-dirs/omni_math_004108/profile.json"
with open(profile_path, "r") as f:
    profile = json.load(f)

# Update analyzed_at to current time
profile["analysis_metadata"]["analyzed_at"] = datetime.now(timezone.utc).isoformat()

# Write to problem_profiles collection (overwrite=True, _key=omni_math_004108)
result = db.collection("problem_profiles").insert(profile, overwrite=True)
print(f"Inserted profile: {result}")

# Update problem_extraction_progress record _key=333987
now = datetime.now(timezone.utc).isoformat()
update_result = db.collection("problem_extraction_progress").update({
    "_key": "333987",
    "extraction_status": "completed",
    "schema_version": 3,
    "extracted_at": now,
    "profile_doc_id": "problem_profiles/omni_math_004108",
    "extracted_by": "subagent",
})
print(f"Updated progress record: {update_result}")

# Verification
p = db.collection("problem_profiles").get("omni_math_004108")
assert p is not None, "Profile not found after insert!"
assert "tell_topology" in p["tell_hint_pairs"][0], "Per-pair topology missing!"
assert len(p["tell_hint_pairs"]) == 8, f"Expected 8 local pairs, got {len(p['tell_hint_pairs'])}"
assert len(p["global_tell_hint_pairs"]) == 2, f"Expected 2 global pairs, got {len(p['global_tell_hint_pairs'])}"
assert p.get("answer") is not None, "Answer field is missing!"

# Verify all global pairs have why_not_visible_locally
for g in p["global_tell_hint_pairs"]:
    assert g.get("why_not_visible_locally") is not None, "why_not_visible_locally missing in global pair!"
    assert "tell_topology" in g, "tell_topology missing in global pair!"
    assert "tell_small_concepts" in g, "tell_small_concepts missing in global pair!"

# Verify all local pairs have tell_topology and tell_small_concepts
for pair in p["tell_hint_pairs"]:
    assert "tell_topology" in pair, f"tell_topology missing in pair round {pair['qa_round']}"
    assert "tell_small_concepts" in pair, f"tell_small_concepts missing in pair round {pair['qa_round']}"
    assert 0 <= pair["hint_level"] <= 1, f"hint_level out of range in pair round {pair['qa_round']}"

# Verify situation_type values
valid_types = {"纯元认知观察", "自由列举", "小尝试", "思维操作引导", "推进", "能量传递引导"}
for pair in p["tell_hint_pairs"]:
    assert pair["situation_type"] in valid_types, f"Invalid situation_type: {pair['situation_type']}"

# Verify knowledge_bottleneck and thinking_bottleneck are strings
stats = p["qa_sequence"]["stats"]
assert isinstance(stats["knowledge_bottleneck"], str), "knowledge_bottleneck must be string"
assert isinstance(stats["thinking_bottleneck"], str), "thinking_bottleneck must be string"

# Verify progress record
prog = db.collection("problem_extraction_progress").get("333987")
assert prog is not None, "Progress record not found!"
assert prog["extraction_status"] == "completed", f"Status not completed: {prog['extraction_status']}"

print(f"\nVerification PASSED:")
print(f"  _key: {p['_key']}")
print(f"  answer: {p['answer']}")
print(f"  local pairs: {len(p['tell_hint_pairs'])}")
print(f"  global pairs: {len(p['global_tell_hint_pairs'])}")
print(f"  knowledge_bottleneck: {stats['knowledge_bottleneck']}")
print(f"  thinking_bottleneck: {stats['thinking_bottleneck']}")
print(f"  bare_ai_expected: {p['bare_ai_expected']}")
print(f"  progress status: {prog['extraction_status']}")
print(f"\nAll checks passed. Database insertion complete.")
