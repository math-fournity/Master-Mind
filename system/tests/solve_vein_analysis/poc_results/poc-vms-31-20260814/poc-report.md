# POC-VMS-31 machine result

Overall verdict: **PASS**

| Case | DAG | traces | batch=incremental | tree recall | flat recall |
|---|---:|---:|---:|---:|---:|
| C1_LINEAR | PASS | PASS | PASS | 1.000 | 0.333 |
| C2_BRANCH | PASS | PASS | PASS | 1.000 | 0.250 |
| C3_REVISIT | PASS | PASS | PASS | 0.800 | 0.200 |
| C4_TRUE_MERGE | PASS | PASS | PASS | 0.750 | 0.250 |
| C5_COMPOSITE | PASS | PASS | PASS | 0.750 | 0.250 |

This POC starts from frozen structured event trajectories. Raw Solver-thinking
extraction, live model execution, database integration, and large-scale
performance remain NOT_TESTED.
