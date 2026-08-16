Read AGENTS.md first and obey it. Audit candidate-traces.json against
the sealed graph/context/concept/relational files in this workspace. Do not solve
the problem and do not infer process from a final answer. Produce trace-audit.json
with exactly the top-level keys required by AGENTS.md. Each trace_verdicts item must
have exactly:
{
  "trace_id": "<candidate trace id>",
  "verdict": "PASS|FAIL|INCONCLUSIVE",
  "reasons": ["<specific structural reason>"],
  "evidence_refs": ["<event or edge id>"]
}
Every candidate trace must receive exactly one verdict. Then write DONE.md as:
trace-audit.json SHA256=<lowercase-64hex>
Do not inspect any path outside this workspace.
