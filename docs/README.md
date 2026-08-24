# docs - Stable Knowledge Index

`docs/` contains stable, governed knowledge. It does not replace root `feature-list.md`, `MEMORY.md`, or
`rulings.md`, and it does not prove implementation by itself. Use it to route to the right evidence.

| Topic | Entry | Role |
|---|---|---|
| Product and scope | `product/README.md` | What this super repo is and is not |
| Domain and terms | `domain/README.md` | Concept families and glossary routes |
| System design | `design/system/README.md` | System-island topology and boundaries |
| Detailed design | `design/detailed/README.md` | Exact contracts that are stable enough to rely on |
| Decisions | `decisions/README.md` | Adopted decisions and links to rulings |
| Interfaces | `interfaces/README.md` | CLI/API/schema/cross-repo interface routes |
| Data | `data/README.md` | D disk data, DB boundaries, file data policy |
| Quality | `quality/README.md` | Verification, tests, audit evidence |
| Security | `security/README.md` | Secrets, sensitive docs, permissions |
| Operations | `operations/README.md` | Runbooks, external systems, no-write boundaries |
| Development | `development/README.md` | Git and development workflow |
| Releases | `releases/README.md` | Tags, branches, release notes |
| AI contracts | `ai/README.md` | AI roles, prompts, trajectories, leakage controls |
| History | `history/README.md` | Lineage, legacy assets, migrations |
| Reference | `reference/README.md` | Reference materials and off-repo pointers |

For historical claims, read `docs/history/` and then verify against Git log, old files, or migration manifests.
For current implementation claims, read the relevant island code, tests, and run evidence.
