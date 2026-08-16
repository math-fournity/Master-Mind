Read AGENTS.md first and obey it. Review problem.md,
raw_solver_trajectory.txt, and reasoning-trajectory.json. Produce only
normalized-reasoning-trajectory.json plus DONE.md. Preserve the event history and
correct only evidence-supported normalization mistakes. Do not inspect any path
outside this workspace.

The output must obey this same exact contract:
The exact JSON object has only these fields and shapes:
{
  "schema_version": "solve-vein/reasoning-trajectory/v1",
  "trajectory_id": "poc-vms-32-calibration",
  "problem_id": "poc-vms-32-fibonacci-gcd",
  "source": {
    "carrier": "fixture",
    "source_artifact_ref": "raw_solver_trajectory.txt",
    "source_artifact_sha256": "<sha256 of the complete raw file>"
  },
  "events": [
    {
      "event_id": "e0",
      "sequence_index": 0,
      "event_kind": "STATE|DECISION|FAILURE|RETURN|SYNTHESIS|CONCLUSION",
      "text": "<concise faithful description>",
      "canonical_math_state_id": "state:<stable-slug>",
      "attributes": ["namespace:value"],
      "status": "ACTIVE|ABANDONED|CONTRADICTED|SOLVED|UNKNOWN",
      "source_span": {"start": 0, "end": 1, "sha256": "<sha256>"},
      "incoming_edges": [
        {
          "source_event_id": "e0",
          "relation": "CONTINUE|REFINE|BRANCH_FROM|CONTRADICT|ABANDON|REVISIT|REUSE|DEPENDS_ON|MERGE|CONCLUDE",
          "evidence": "<raw-grounded reason>"
        }
      ]
    }
  ]
}
Unknown keys are forbidden. start/end are zero-based UTF-8 byte offsets into the
raw file, end-exclusive and excluding the line-ending byte. source_span.sha256 is
SHA-256 of exactly raw_bytes[start:end]. Every [NN] line is one occurrence and
must map in order to e0..e9; this fixes occurrence boundaries but does not tell
you the relations or canonical state identities.
