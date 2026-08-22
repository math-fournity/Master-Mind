# POC-2.5c 方向使用度标注协议（冻结·2026-08-22）

依据：poc25c_experiment_design.md §3（"方向使用度判定标准将在实验启动前细化并冻结"）+ hintinstance_v02_I_mid_frozen.md判定锚。

## 标注对象

仅T组12个run的thinking（reasoning_content）与最终消息。C组不标（无Hint可"使用"）。

## 盲化（§4.4）

标注者只看脱敏后的thinking文本（文件名替换为样本编号T-01..T-12），不知晓题名与机械判定结果。

## 记分项（每run三个二值位）

| 位 | 定义 | 证据形态 |
|---|---|---|
| U1 实例构造 | 显式构造了具体实例/特例数值 | "let me check p=7"、"test n=3"、"take the case x=1"类语句 |
| U2 代入核对 | 把实例代回某中间公式/结论做一致性检查 | "substituting back… consistent"、"plugging in gives…"类行为 |
| U3 不一致处置 | 发现不一致后定位修复而非丢弃 | "discrepancy… let me recheck step 2"、"sign error found, fixed"类序列 |

**方向使用度成立 = U1∧U2 至少同时出现**（U3为加强证据非必要条件）。只计文本中可指认的显式行为，推断性、笼统的不计。

## 汇总口径

- 双人标注（主控=A，复核=B），**分歧仲裁：只计入双方一致的证据**（§3原文）。
- 弱因果贡献工程门槛（判据口径修正案版）：T组≥8/12 COMPLETED 且 C组0/12 COMPLETED 且 T组COMPLETED题中≥6题有方向使用度证据。
- 成本指标：T组completion_tokens vs 历史R1截断tokens+R2成功tokens总和（历史值从p27_continuation_runs.rounds_log提取）。

## 流程

1. 机械收取（collect_poc25c.py）→ batch1_mechanical_results.json
2. 主控生成脱敏thinking包（T-01..T-12）
3. 标注A（本session主控）→ annotation_A.yaml
4. 标注B（独立复核者，另开干净上下文）→ annotation_B.yaml
5. 汇总一致项 → batch1_EvidenceRecord.yaml
