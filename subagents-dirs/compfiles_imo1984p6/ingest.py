import sys
sys.path.insert(0, '~/master-mind-glm5.2-worktree/.venv/lib/python3.14/site-packages')

from arango import ArangoClient
from datetime import datetime, timezone
import json

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
now = datetime.now(timezone.utc).isoformat()

with open('~/master-mind-glm5.2-worktree/subagents-dirs/compfiles_imo1984p6/profile.json', 'r') as f:
    profile = json.load(f)

# Write to problem_profiles
db.collection('problem_profiles').insert(profile, overwrite=True)
print('Written to problem_profiles')

# Update problem_extraction_progress
db.collection('problem_extraction_progress').update({
    '_key': '329108',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/compfiles_imo1984p6',
    'extracted_by': 'subagent',
})
print('Updated progress record')

# Verify
p = db.collection('problem_profiles').get('compfiles_imo1984p6')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]
print(f'Verification passed: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
