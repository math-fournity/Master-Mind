# Problem Banks Download Manifest

> 生成日期：2026-09-28（repo 群梳理调查期间建立）。
> 策略：**原始外部题库语料不进入 Git**（体积与再获取成本考虑）；Git 内保留：本清单、
> `download_*.log` 下载日志、`math_datasets_catalog*.json` 数据集目录、以及 `matharena/`
> 下由实验精选出的 `hard_batch_*` / `retry_batch_*` / `failed_problems.json` 等工作产物。
> 任何人在新机器上恢复工作时，按本清单 + 下载日志 + 目录文件重新获取原始语料即可。

## 原始语料清单（不提交，按 .gitignore 忽略）

| 目录 | 体积 | 文件数 | 来源类别 |
|---|---|---|---|
| aops_instruct | 39M | 133 | GitHub（AoPS instruct 语料） |
| awesome_math | 200K | 32 | GitHub（awesome-math-project 类） |
| compfiles | 11M | 595 | GitHub（竞赛题文件集） |
| conjecture_bench | 37M | 5602 | 研究基准数据集 |
| demidovich | 1.1G | 36 | Demidovich 习题集扫描/数据（体积最大） |
| evan_chen | 48M | 289 | Evan Chen 竞赛材料 |
| fate | 6.9M | 516 | FATE 基准 |
| hendrycks_math | 4.8M | 51 | HuggingFace（MATH 数据集） |
| mathnet | 484M | 1990 | HuggingFace（math.net 语料，见 download_hf.log） |
| miniF2F | 5.3M | 1314 | GitHub（miniF2F 形式化基准） |
| moscow_olympiad | 100K | 1 | 莫斯科奥林匹克题集 |
| numina_math | 55M | 1 | HuggingFace（NuminaMath，单文件打包） |
| russian_546 | 136K | 1 | 俄罗斯 546 题集 |
| sasabe | 12K | 1 | Sasabe 题集 |
| springer_pbm | 5.0M | 4 | Springer Problem Book in Mathematics |
| taichili | 1.8M | 43 | 太池里题集 |
| we_math | 28K | 11 | WeMath 数据集 |
| yau_contest | 8.1M | 5 | 丘成桐中学生数学竞赛 |
| matharena/MathArena_* （19 个比赛目录） | 各40-72K | 各12-15 | MathArena 各赛事原始题面 |
| matharena/math-ai_* （3 个目录） | 各44-64K | 各12-15 | math.ai 赛事原始题面 |
| matharena/all_problems_raw.json | 148K | 1 | MathArena 全量原始汇总 |

## 再获取途径

- HuggingFace 数据集（mathnet、numina_math、hendrycks_math 等）：见 `download_hf.log`
  与 `math_datasets_catalog_v2.json`（两份 catalog 已在 Git 内，含数据集标识）。
- GitHub 语料（aops_instruct、awesome_math、compfiles、evan_chen、miniF2F 等）：见
  `download_cn_github.log` 与 `download_numina.log`。
- MathArena 原始题面：matharena 官方公开仓库/站点；本地精选批次
  （`matharena/hard_batch_*.json`、`retry_batch_*.json`、`failed_problems.json`）已在 Git 内，
  可作为对照基线。
- 其余（demidovich、springer_pbm、russian_546、sasabe、taichili、moscow_olympiad 等）：
  见 `math_datasets_catalog*.json` 中的条目标识。

## 与实验的关系

`runs/` 下 fate、matharena、bare_q2、ab_test_253、vms_test_1 等实验直接消费的输入是
Git 内已跟踪的精选批次文件；本清单所列原始语料是精选批次的上一级来源。
