#!/usr/bin/env python3
"""Insert profile.json into ArangoDB and update progress record."""
import json
import sys
from datetime import datetime, timezone

from arango import ArangoClient

def main():
    # Connect to ArangoDB
    client = ArangoClient(hosts='http://localhost:8529')
    db = client.db('xishujuzhen_math_glm52', username='root', password='REDACTED-DB-PASSWORD')
    now = datetime.now(timezone.utc).isoformat()

    # Read profile.json
    with open('profile.json', 'r') as f:
        profile = json.load(f)

    # Write to problem_profiles collection
    db.collection('problem_profiles').insert(profile, overwrite=True)
    print(f'Written to problem_profiles: {profile["_key"]}')

    # Update problem_extraction_progress
    db.collection('problem_extraction_progress').update({
        '_key': '334046',
        'extraction_status': 'completed',
        'schema_version': 3,
        'extracted_at': now,
        'profile_doc_id': 'problem_profiles/omni_math_004166',
        'extracted_by': 'subagent',
    })
    print(f'Updated progress record: 334046 -> completed')

    # Verify
    p = db.collection('problem_profiles').get('omni_math_004166')
    assert p is not None, 'profile not found after insert'
    assert 'tell_topology' in p['tell_hint_pairs'][0], 'per-pair topology missing'
    assert 'tell_small_concepts' in p['tell_hint_pairs'][0], 'per-pair small concepts missing'
    assert 'tell_topology' in p['global_tell_hint_pairs'][0], 'global pair topology missing'
    assert 'tell_small_concepts' in p['global_tell_hint_pairs'][0], 'global pair small concepts missing'
    assert 'why_not_visible_locally' in p['global_tell_hint_pairs'][0], 'why_not_visible_locally missing'
    assert p.get('answer') is not None, 'answer field is None'
    print(f'Verification passed: {p["_key"]}, {len(p["tell_hint_pairs"])} local pairs, {len(p["global_tell_hint_pairs"])} global pairs')
    print(f'Answer: {p["answer"]}')
    print(f'Solution method type: {p["solution_method_type"]}')
    print(f'Knowledge bottleneck: {p["qa_sequence"]["stats"]["knowledge_bottleneck"]}')
    print(f'Thinking bottleneck: {p["qa_sequence"]["stats"]["thinking_bottleneck"]}')
    print(f'Bare AI expected: {p["bare_ai_expected"]}')
    print('All done.')

if __name__ == '__main__':
    main()
