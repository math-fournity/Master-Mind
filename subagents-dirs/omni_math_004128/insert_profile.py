from arango import ArangoClient
from datetime import datetime, timezone
import json

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
now = datetime.now(timezone.utc).isoformat()

# Read profile.json
with open('profile.json', 'r') as f:
    profile = json.load(f)

# Write to problem_profiles
db.collection('problem_profiles').insert(profile, overwrite=True)

# Update problem_extraction_progress
db.collection('problem_extraction_progress').update({
    '_key': '334007',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_004128',
    'extracted_by': 'subagent',
})
print('入库完成')

# Verify
p = db.collection('problem_profiles').get('omni_math_004128')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]  # per-pair topology exists
assert 'tell_small_concepts' in p['tell_hint_pairs'][0]
assert 'tell_topology' in p['global_tell_hint_pairs'][0]
assert 'tell_small_concepts' in p['global_tell_hint_pairs'][0]
assert 'why_not_visible_locally' in p['global_tell_hint_pairs'][0]
assert p['answer'] is not None
assert isinstance(p['qa_sequence']['stats']['knowledge_bottleneck'], str)
assert isinstance(p['qa_sequence']['stats']['thinking_bottleneck'], str)
print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
print(f'answer: {p["answer"][:80]}')
print(f'bare_ai_expected: {p["bare_ai_expected"]}')
print(f'solution_method_type: {p["solution_method_type"]}')
