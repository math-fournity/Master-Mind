# 题目侧写Profile提取完整方案 — 从最难到最简单

> **创建时间**：2025-01-24
> **状态**：活文档，随进度更新
> **关联**：AGENTS.md第300-372行"题目侧写Profile提取工作"章节

---

## §0 当前焦点

Tier 2进行中（IMO Shortlist 3/606已完成）。

---

## §1 总览

| 层级 | 难度 | 来源数 | 题数 | 约批次 | 状态 |
|---|---|---|---|---|---|
| **Tier 1** | 最高（IMO P5/P6 + Putnam + FATE-X + IMO SL已做部分） | — | 452 | — | ✅全部完成 |
| **Tier 2** | 国际顶级竞赛+TST | 11 | 603 | ~201批 | 进行中(3/603) |
| **Tier 3** | 国家级竞赛+顶级邀请赛 | 1711 | 11894 | ~3965批 | 待处理 |
| **Tier 4** | 中等难度基准 | 2 | 830 | ~277批 | 待处理 |
| **Tier 5** | 初等竞赛+教材题库 | 5 | 13442 | ~4481批 | 待处理 |
| **Tier 6** | 大规模题库 | 2 | 40481 | ~13494批 | 暂不规划 |
| 其他 | source_competition为空 | 2 | 133 | ~44批 | 待分类 |
| **合计** | | | **67383** | | |

**每批3题，并发3个subagent。**

---

## §2 Tier 2 — 国际顶级竞赛+TST（603题，~201批）

> 难度最高，与Tier 1同级别。优先处理。

| 优先级 | 来源 | 题数 | 约批次 | 起始seq | 状态 |
|---|---|---|---|---|---|
| 1 | imo_shortlist | 93 | ~31批 | 1955 | 进行中(3/93) |
| 2 | imo | 89 | ~30批 | 1403 | 待处理 |
| 3 | putnam | 88 | ~29批 | 1756 | 待处理 |
| 4 | china_team_selection_test | 80 | ~27批 | 1443 | 待处理 |
| 5 | imc | 67 | ~22批 | 1627 | 待处理 |
| 6 | ToT (Tournament of Towns) | 54 | ~18批 | 1956 | 待处理 |
| 7 | imo_longlists | 39 | ~13批 | 1994 | 待处理 |
| 8 | china_national_olympiad | 35 | ~12批 | 1446 | 待处理 |
| 9 | balkan_mo_shortlist | 31 | ~10批 | 1862 | 待处理 |
| 10 | alibaba_global_contest | 21 | ~7批 | 1597 | 待处理 |
| 11 | yau_contest | 6 | ~2批 | 1630 | 待处理 |

---

## §3 Tier 3 — 国家级竞赛+顶级邀请赛（11894题，~3965批）

> 1711个来源，各国数学奥林匹亚+邀请赛。按规模分组。

### Tier 3a — 大规模来源（>100题，~5463题）

| 来源 | 题数 | 性质 |
|---|---|---|
| HMMT_2 | 1385 | HMMT 2月赛 |
| HMMT_11 | 896 | HMMT 11月赛 |
| Harvard-MIT Mathematics Tournament | 228 | HMMT综合 |
| Brazilian Mathematical Olympiad | 145 | 巴西MO |
| usamo | 133 | USAMO |
| FATE-H | 110 | FATE高难度 |
| Iranian Mathematical Olympiad | 81 | 伊朗MO |
| Baltic Way | 73 | Baltic Way |
| Mathematica competitions in Croatia | 66 | 克罗地亚竞赛 |
| HMMT February | 65 | HMMT 2月 |
| Harvard-MIT Math Tournament | 63 | HMMT |
| apmoapmo_sol | 61 | APMO解答 |
| Canadian Mathematical Olympiad | 61 | 加拿大MO |
| Berkeley Math Circle | 55 | 伯克利数学圈 |
| amc12a | 55 | AMC 12A |
| SAUDI ARABIAN MATHEMATICAL COMPETITIONS | 55 | 沙特MO |
| PRÉPARATION OLYMPIQUE FRANÇAISE DE MATHÉMATIQUES | 55 | 法国MO预备 |
| Harvard-MIT November Tournament | 55 | HMMT 11月 |
| ASU | 53 | ASU竞赛 |
| Mongolian Mathematical Olympiad | 52 | 蒙古MO |
| smt_2025 | 51 | SMT 2025 |
| baltic_way | 47 | Baltic Way |
| Belarusian Mathematical Olympiad | 42 | 白俄罗斯MO |
| IMO HK TST | 42 | 香港IMO TST |
| China Mathematical Competition | 41 | 中国数学竞赛 |
| AMC 2023 | 40 | AMC 2023 |
| Bulgarian Mathematical Competitions | 40 | 保加利亚MO |
| usajmo | 39 | USAJMO |
| cmimc_2025 | 38 | CMIMC 2025 |
| Estonian Math Competitions | 37 | 爱沙尼亚MO |
| Japan Mathematical Olympiad | 37 | 日本MO |
| algebra | 36 | 代数题集 |
| Préparation Olympique Française de Mathématiques | 36 | 法国MO预备 |
| Olympiades Françaises de Mathématiques | 36 | 法国MO |
| HMMT November | 36 | HMMT 11月 |
| china_national_olympiad (已在Tier 2) | — | — |

### Tier 3b — 中等规模来源（20-99题，~3500题）

约100个来源，包括：
- 各国TST（Saudi/Ireland/Belarus/Bulgaria/Croatia/Czech-Slovak/Estonia/Greece/Hungary/Latvia/Lithuania/Macedonia/Moldova/Poland/Romania/Russia/Serbia/Slovenia/South Africa/Turkey/Ukraine等）
- 各国NMO（同上）
- APMO/Baltic Way/JBMO/BMO/EGMO/Iberoamerican/MEMO/Mediterranean/Caucasus/Danube/Silk Road等区域竞赛
- Berkeley Math Circle系列
- AMC/AIME/USAMO/USAJMO系列
- Bay Area MO/Tuymaada/Stars of Mathematics/Romanian Master of Mathematics等邀请赛

### Tier 3c — 小规模来源（1-19题，~2900题）

约1500个来源，每个1-19题。大部分是各国MO的单届比赛、各TST的单日考试等。这些来源名称高度碎片化（如"IMO 1972 P1"、"USA 2018 P4"、"二〇一九數學奧林匹亞競賽第二階段選訓營，獨立研究（一）"等）。

**处理策略**：按global_sequence顺序批量处理，不按来源分组。

---

## §4 Tier 4 — 中等难度基准（830题，~277批）

| 来源 | 题数 | 性质 |
|---|---|---|
| OlympiadBench | 675 | 奥林匹亚基准测试集 |
| FATE-M | 155 | FATE中等难度 |

---

## §5 Tier 5 — 初等竞赛+教材题库（13442题，~4481批）

| 来源 | 题数 | 性质 |
|---|---|---|
| Hendrycks MATH | 12500 | MATH数据集（初等-中等） |
| mathd | 260 | Math数据集 |
| pascal | 249 | 加拿大Pascal竞赛 |
| fermat | 232 | 加拿大Fermat竞赛 |
| cayley | 201 | 加拿大Cayley竞赛 |

---

## §6 Tier 6 — 大规模题库（40481题，暂不规划）

| 来源 | 题数 | 性质 |
|---|---|---|
| olympiads | 35153 | 各国奥林匹亚题库（最大来源） |
| AoPS 2024 | 5328 | AoPS社区2024年题目 |

---

## §7 其他（133题，source_competition为空）

需人工分类后归入相应Tier。

---

## §8 工作流程（每批3题）

1. **领取题目**：从ArangoDB按global_sequence取3题，提取problem_id/progress_key/题目内容
2. **准备目录**：为每题创建`subagents-dirs/<problem_id>/`，写入problem.lean和checklist.md
3. **并发启动**：3个subagent并发执行11步分析
4. **等待完成**：3个subagent完成后，逐个格式检查
5. **数学审查**：Master Agent审查题目理解/解答理解/key_insight/瓶颈标注
6. **落盘审计**：写audit-checklist.md，更新review-log.md
7. **git commit**：提交本批产出

---

## §9 预估

| 层级 | 题数 | 约批次 | 预估时间（每批10分钟） |
|---|---|---|---|
| Tier 2 | 603 | ~201批 | ~33小时 |
| Tier 3 | 11894 | ~3965批 | ~661小时 |
| Tier 4 | 830 | ~277批 | ~46小时 |
| Tier 5 | 13442 | ~4481批 | ~747小时 |
| Tier 6 | 40481 | ~13494批 | ~2249小时 |
| **合计** | **67383** | **~22419批** | ~3736小时 |

**实际节奏**：每批约10-15分钟（含subagent运行+审计+commit）。Tier 2可在约1周内完成。Tier 3-5需要数月连续运行。Tier 6暂不规划。

---

## §10 关键文件

- `subagents-dirs/review-log.md`：完整审计日志
- `subagents-dirs/<problem_id>/`：每题工作目录
- `subagents-dirs/audit-checklist-template.md`：审计模板
- `subagents-dirs/checklist-template.md`：subagent工作模板
- `scripts/prepare_subagent_dir.py`：目录准备脚本
- `AGENTS.md`第300-372行：AGENTS.md中的进度章节
