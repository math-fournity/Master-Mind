# Eight System · 工作交接文档

> **更新**：2026-08-17｜**交接者**：Master Agent（非特化研究线）
> **用法**：接手AI先读 `NEW_AI_ONBOARDING.md`（认知与约束），再读本文件（当前状态与下一步）。本文件自包含到"不需要读对话历史即可继续"。

## 一、三句话当前状态

1. 非特化研究已进入 **Mid-Hint 实验阶段**，真实失败题轨道为先行轨道（用错题分析系统的真实bare失败题做测试题）。
2. **devin配额已恢复**（2026-08-17验证：audit-full1在并发1下正常跑了数十个session）。真实题轨道**2圈已staged**（00995+00128），全套资产就绪，可直接启动。错题分析系统审计**Pipe 2已完成90%**（1424/1521），产出**721个PASS_SELECTABLE**可选题。
3. **选题数据已就绪**：721个PASS_SELECTABLE中，**51个已有明确d2子类型**（覆盖全部8种局部-全局切换类型），脚本直接选题，不需要Pipe 3。667个d2=other需Pipe 3语义再分类（可选扩展）。

## 二、工作线全景

| 线 | 状态 | 关键资产 | 下一步 |
|---|---|---|---|
| **Mid-Hint实验·真实题轨道**（active） | 2圈staged（00995+00128），配额已恢复 | `runs/midhint/realtrack/00995/`与`00128/`全套 | **启动00995的MH运行**→三层判定→对照报告 |
| **Mid-Hint实验·选题池扩展** | 51道已分类d2可直接选题；667道d2=other需Pipe 3 | `analysis-devin-failure-system/output/audit-full1/audit_summary.md` | 用51道扩展实验批次（7种卡点类型全覆盖） |
| 错题分析系统·Pipe 2审计 | 1424/1521完成，96个prepared重跑中 | `audit-full1/audit_summary.md` | 等剩余96个跑完，再次运行collector |
| 错题分析系统·Pipe 3选题 | **未开始**，但51个已分类d2不需要Pipe 3 | — | 需要扩展667个d2=other时再启动 |
| 构造轨道（后台） | 批次1未收敛 | `runs/midhint/problems/` | 参考真实圈的卡点形态再迭代 |
| 决策治理 | 已落盘 | `docs/两棵树实现时机与基本实践方式.md` | 无待办 |

## 三、第一圈（00995）精确状态与重启

- **重启命令**：见 `runs/midhint/realtrack/00995/experiment_report.md` 头部（solver_harness launch，exp-id `eight-mh-00995-MH`）。
- **启动后立即做**：扫 `/data/math-agent-glm5.2-tmux-agents-trajectory/eight-mh-00995-MH/tmux/tmux_pipe.log` 的错误模式（quota/rate limit/connection）——首圈启动因只查"session存活"漏判配额错误，此为检查者教训。
- **运行中**：按AGENTS.md检查者SOP监控；**运行后**：收集thinking（conversation.json），按`preregistration.md`三层判定填`experiment_report.md`。
- **判定要点**：路线层成功=AI用局部表示分析（mod 2n/v₂等）正确解决n≡2 mod 4类；标准答案3800（分类：n可行⟺n奇数或4|n）。

## 四、选题数据来源与并发约束

### 4.1 选题数据链

```
Pipe 1（分析）→ 2050条结果，1589个唯一题目，1096个DIRECTION_ERROR
    ↓ 去重
Pipe 2（审计）→ 1521个题目审计，1424完成，721个PASS_SELECTABLE
    ↓ 选题
Mid-Hint实验 → 51个已分类d2（脚本直接选题）+ 667个d2=other（需Pipe 3）
```

产出文件：
- `analysis-devin-failure-system/output/analysis_summary.md`（Pipe 1产出统计）
- `analysis-devin-failure-system/output/audit-full1/audit_summary.md`（Pipe 2审计总结）

### 4.2 721个PASS_SELECTABLE的d2分布

| d2类型 | 数量 | Mid-Hint批次 | 需要devin cli选题吗 |
|---|---|---|---|
| **other** | **667** | 需再分类 | **需要**（Pipe 3） |
| mod_p_grouping | 16 | 批次1（低难度） | 不需要 |
| finite_field_structure | 13 | 可扩展 | 不需要 |
| crt | 7 | 批次3（高难度） | 不需要 |
| p_adic_valuation | 5 | 批次2（中难度） | 不需要 |
| multi_step_mod_p | 4 | 批次2 | 不需要 |
| mod_p_non_obvious | 3 | 批次2 | 不需要 |
| quadratic_residue_euler | 2 | 批次3 | 不需要 |
| permutation_polynomial | 1 | 可扩展 | 不需要 |
| **已分类合计** | **51** | **7种类型全覆盖** | **不需要** |

### 4.3 并发约束

**Rate limit是账户级的，跨所有devin cli实例共享。** 运行任何devin cli pipeline前必须检查当前进程数（见`.devin/rules/audit-pipeline-rate-limit.md`）。

| 场景 | 需要devin cli数 | 并发建议 |
|---|---|---|
| Mid-Hint实验（00995+00128） | 2次（bare复用已有数据） | 并发1，半小时内完成 |
| Pipe 3选题（667个d2=other） | 667次 | 并发1-3，配合自动暂停，约2-6小时 |
| Pipe 3选题（关键词预筛后） | ~150-300次 | 并发1-3，约1-2小时 |

**建议**：先用51个已分类的推进Mid-Hint实验。需要扩展选题池时再启动Pipe 3，且可只跑关键词预筛后的子集。

## 五、待用户决定的事项

1. **执行顺序**：先跑00995的MH（1次devin cli）还是等audit-full1剩余96个跑完？建议MH先行——1个session解锁第一圈，audit继续在后台跑。
2. **Pipe 3选题范围**：51个已分类的够用吗？还是需要对667个d2=other做系统选题扩大选题池？
3. （低优先）11道构造轨道源题中9道未入错题分析池，可请分析系统补跑AI级分析。

## 六、与错题分析系统的协调状态

- 本轨道消费其产出：analysis_results的d1/d2判定 + audit_results的审计状态。
- **选题两道闸门**见`runs/midhint/realtrack/pool_screening.md`（闸门A真做了本题；闸门B解答亲自核验）。
- 交叉验证发现：源题1843的AI级判定为PARTIAL_PROGRESS（非关键词脚本的DIRECTION_ERROR）——bare当时已到mod 2配对停滞，需mod 4升级；此精化判据已传入构造轨道要求。
- audit-full1当前状态：1424 completed / 96 prepared（重跑中）/ 1 running。Rate limit根因分析见`dev-docs/388号`。

## 七、资产索引（按交接重要性）

| 文档 | 内容 |
|---|---|
| `runs/midhint/realtrack/00995/preregistration.md` | 第一圈冻结预注册（Arms/判定/预测/停止规则） |
| `runs/midhint/realtrack/00995/vein_extraction.md` | Phase B记录：7条脉络+卡点+Hint匹配+树形化字段 |
| `runs/midhint/realtrack/00995/00995_MH_midhint.txt` | MH输入文件（重启即用） |
| `runs/midhint/realtrack/00995/verification/` | 标准答案程序核验（n=2/6不可行穷举等） |
| `runs/midhint/realtrack/00995/experiment_report.md` | 报告骨架（含重启命令+待填判定表） |
| `runs/midhint/realtrack/pool_screening.md` | 32→13选题池筛选记录+两道闸门+第2圈候选 |
| `analysis-devin-failure-system/output/analysis_summary.md` | Pipe 1产出统计（2050条结果，d1/d2分布） |
| `analysis-devin-failure-system/output/audit-full1/audit_summary.md` | Pipe 2审计总结（721个PASS_SELECTABLE） |
| `dev-docs/387号` | 三Pipe方案（FROZEN） |
| `dev-docs/388号` | Rate limit根因分析与处理记录 |
| `.devin/rules/audit-pipeline-rate-limit.md` | Rate limit防护规则 |
| `runs/midhint/problems/master_track_notes.md` | 构造轨道：5陷阱+否决候选全图+7条审查清单 |
| `docs/两棵树实现时机与基本实践方式.md` | 树缓建决策+基本实践方式（用户确认，新AI必读） |

## 八、历史事件记录（防重复踩坑）

- 2026-08-16：两个构造subagent均空返回失败（模型无输出），无产出；此后构造工作由master亲手做。
- 2026-08-16：MH首启撞devin每日配额耗尽（`resource_exhausted`）；健康检查教训=启动后必扫错误模式。
- 2026-08-16：n=6不可行性穷举验证完成（1.71亿节点，脚本在verification/）。
- 2026-08-16：**ZCode subagent载具判定：受模型并发限制，当前不可用**——5/5失败。subagent应在主会话空闲、且一次只跑1个时重试。
- 2026-08-16：devin配额二次探测仍耗尽（重启用即拒），Phase C持续阻塞。
- 2026-08-17：**devin配额恢复**——audit-full1在并发1下正常跑了数十个session，MH可启动。
- 2026-08-17：**Rate limit根因确认**——账户级overall message rate limit，跨所有CLI实例共享。24个进程+并发3=触发，并发1=不触发。详见`dev-docs/388号`。
- 2026-08-17：**选题数据链澄清**——721个PASS_SELECTABLE中51个已有明确d2子类型（不需要Pipe 3），667个d2=other需Pipe 3（可选扩展）。
- **方法论说明（为何MH的solver必须是devin cli）**：bare run是GLM-5.2 High跑的，MH臂必须同模型同载体，否则R vs MH对照被模型差异污染；整条证据链（283号、Phase 0/1、卡点分析）均在该模型上校准；且AGENTS.md硬约束4规定devin cli Solver必须走solver_harness。换载具只允许以"双臂平行线"形式，不允许替换主冻结线的载体。
