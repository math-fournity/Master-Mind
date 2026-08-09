from arango import ArangoClient
from datetime import datetime, timezone
import json

client = ArangoClient(hosts='http://localhost:8529')
db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
now = datetime.now(timezone.utc).isoformat()

# Read profile.json
with open('profile.json', 'r') as f:
    profile = json.load(f)

# Write to problem_profiles collection
db.collection('problem_profiles').insert(profile, overwrite=True)
print('Inserted into problem_profiles')

# Update problem_extraction_progress
db.collection('problem_extraction_progress').update({
    '_key': '333164',
    'extraction_status': 'completed',
    'schema_version': 3,
    'extracted_at': now,
    'profile_doc_id': 'problem_profiles/omni_math_003286',
    'extracted_by': 'subagent',
})
print('Updated problem_extraction_progress')

# Verify
p = db.collection('problem_profiles').get('omni_math_003286')
assert p is not None, 'profile not found after insert'
assert 'tell_topology' in p['tell_hint_pairs'][0], 'per-pair tell_topology missing'
assert len(p['tell_hint_pairs']) == 7, f'expected 7 local pairs, got {len(p["tell_hint_pairs"])}'
assert len(p['global_tell_hint_pairs']) == 2, f'expected 2 global pairs, got {len(p["global_tell_hint_pairs"])}'
assert p['answer'] is not None, 'answer field is None'
assert p['answer'] == 'No', f'answer should be No, got {p["answer"]}'

# Verify global pairs have required fields
for gpair in p['global_tell_hint_pairs']:
    assert 'tell_topology' in gpair, 'global pair missing tell_topology'
    assert 'tell_small_concepts' in gpair, 'global pair missing tell_small_concepts'
    assert 'why_not_visible_locally' in gpair, 'global pair missing why_not_visible_locally'

# Verify all local pairs have required fields
for lpair in p['tell_hint_pairs']:
    assert 'tell_topology' in lpair, f'local pair R{lpair["qa_round"]} missing tell_topology'
    assert 'tell_small_concepts' in lpair, f'local pair R{lpair["qa_round"]} missing tell_small_concepts'
    assert 0 <= lpair['hint_level'] <= 1, f'local pair R{lpair["qa_round"]} hint_level out of range'
    assert lpair['situation_type'] in ['纯元认知观察', '自由列举', '小尝试', '思维操作引导', '推进', '能量传递引导'], f'invalid situation_type: {lpair["situation_type"]}'

# Verify progress record
prog = db.collection('problem_extraction_progress').get('333164')
assert prog is not None, 'progress record not found'
assert prog['extraction_status'] == 'completed', f'progress status not completed: {prog["extraction_status"]}'

print(f'验证通过: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
print(f'answer: {p["answer"]}')
print(f'solution_method_type: {p["solution_method_type"]}')
print(f'knowledge_bottleneck: {p["qa_sequence"]["stats"]["knowledge_bottleneck"]}')
print(f'thinking_bottleneck: {p["qa_sequence"]["stats"]["thinking_bottleneck"]}')
print(f'bare_ai_expected: {p["bare_ai_expected"]}')
