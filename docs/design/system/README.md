# System Design

## Current Sixth-Generation Architecture

The canonical current/target split is `sixth-generation-architecture.md`. It records the partial legacy Grove
skeleton, the independently verified solve-side offline core, external side effects, and missing end-to-end flow.

The stable system design fact for this repo is that it is a multi-island historical super repo.

## Island Topology

- Root governance: `AGENTS.md`, `README.md`, `feature-list.md`, `MEMORY.md`, `rulings.md`.
- Sixth-generation implementation: `system/`.
- Seven evidence factory: `seven-system/`.
- Eight refinement system: `eight-system/`.
- Tell taxonomy research: `Tell分类学研究过程文档/`.
- Analysis remnants: `analysis-devin-failure-system/` and related root analysis docs.
- Historical primitive/generation material: `primitives/`, `concepts/`, `criteria/`, `facets/`,
  `第五代系统技术说明书/`, `原语化AI数学工程系统设计/`.
- External active solvers: `~/master-mind-normal-solver/` and
  `~/master-mind-analysis-system/`.

Do not infer cross-island runtime coupling from path proximity. Verify coupling from code imports, configs,
tests, runbooks, and Git history.
