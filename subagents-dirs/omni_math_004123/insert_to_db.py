#!/usr/bin/env python3
"""Insert profile.json into ArangoDB and update progress record."""
import json
import sys
from datetime import datetime, timezone

from arango import ArangoClient

WORK_DIR = "~/master-mind-glm5.2-worktree/subagents-dirs/omni_math_004123"
PROFILE_PATH = f"{WORK_DIR}/profile.json"
PROGRESS_KEY = "334002"
PROBLEM_KEY = "omni_math_004123"

# Connect to ArangoDB
client = ArangoClient(hosts="http://localhost:8529")
db = client.db("xishujuzhen_math_glm52", username="root", password="REDACTED-DB-PASSWORD")

# Read profile.json
with open(PROFILE_PATH, "r") as f:
    profile = json.load(f)

# Write to problem_profiles collection (overwrite=True)
result = db.collection("problem_profiles").insert(profile, overwrite=True)
print(f"Inserted into problem_profiles: {result}")

# Update problem_extraction_progress
now = datetime.now(timezone.utc).isoformat()
db.collection("problem_extraction_progress").update(
    {
        "_key": PROGRESS_KEY,
        "extraction_status": "completed",
        "schema_version": 3,
        "extracted_at": now,
        "profile_doc_id": f"problem_profiles/{PROBLEM_KEY}",
        "extracted_by": "subagent",
    }
)
print(f"Updated problem_extraction_progress: _key={PROGRESS_KEY}")

# Verify insertion
p = db.collection("problem_profiles").get(PROBLEM_KEY)
assert p is not None, "Failed to retrieve profile from problem_profiles"
assert "tell_topology" in p["tell_hint_pairs"][0], "Per-pair tell_topology missing"
assert "tell_small_concepts" in p["tell_hint_pairs"][0], "Per-pair tell_small_concepts missing"
assert "tell_topology" in p["global_tell_hint_pairs"][0], "Global pair tell_topology missing"
assert "tell_small_concepts" in p["global_tell_hint_pairs"][0], "Global pair tell_small_concepts missing"
assert "why_not_visible_locally" in p["global_tell_hint_pairs"][0], "Global pair why_not_visible_locally missing"
assert "why_not_visible_locally" in p["global_tell_hint_pairs"][1], "Global pair why_not_visible_locally missing"
assert p.get("answer") is not None, "answer field is missing or None"
print(
    f"Verification passed: {p['_key']}, "
    f"{len(p['tell_hint_pairs'])} local pairs, "
    f"{len(p['global_tell_hint_pairs'])} global pairs, "
    f"answer={p['answer']}"
)

# Verify progress record
prog = db.collection("problem_extraction_progress").get(PROGRESS_KEY)
assert prog is not None, "Failed to retrieve progress record"
assert prog["extraction_status"] == "completed", f"extraction_status not updated: {prog['extraction_status']}"
print(f"Progress record verified: extraction_status={prog['extraction_status']}")

print("\n=== All verification passed ===")
