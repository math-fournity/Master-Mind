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
print('Written to problem_profiles')

# Update problem_extraction_progress
db.collection('problem_extraction_progress').update({
    '_key': '333721',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003842',
    'extracted_by': 'subagent',
})
print('Updated problem_extraction_progress')

# Verify
p = db.collection('problem_profiles').get('omni_math_003842')
assert p is not None
assert 'tell_topology' in p['tell_hint_pairs'][0]
assert 'tell_topology' in p['global_tell_hint_pairs'][0]
assert 'tell_small_concepts' in p['tell_hint_pairs'][0]
assert 'tell_small_concepts' in p['global_tell_hint_pairs'][0]
assert 'why_not_visible_locally' in p['global_tell_hint_pairs'][0]
assert p['answer'] is not None
print(f'Verification passed: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
print(f'Answer: {p["answer"]}')
print(f'Solution method type: {p["solution_method_type"]}')
print(f'Knowledge bottleneck: {p["qa_sequence"]["stats"]["knowledge_bottleneck"]}')
print(f'Thinking bottleneck: {p["qa_sequence"]["stats"]["thinking_bottleneck"]}')
print(f'Bare AI expected: {p["bare_ai_expected"]}')
