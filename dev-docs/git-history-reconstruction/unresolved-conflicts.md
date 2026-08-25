# Unresolved Conflicts

> 本文件记录历史重建过程中的来源冲突、unknown、已查范围和阻塞影响。

## Open Conflicts

暂无已由 diff-review 确认的来源冲突。第一轮只完成 metadata/stat，总账中的候选分类可能存在
false positive/false negative，不能作为语义冲突裁决依据。

## Unknowns

- `glm5.2` 全部 1399 commits 已进入 first-pass ledger，但尚未逐 commit diff-review。
- `docs/README.md` 当前不存在；这与完整治理骨架要求存在差距，但 `AGENTS.md` 明确当前阶段先做历史认知重建，故本轮只记录缺口，不扩展 bootstrap。
- 系统群、代码群、POC 群和研究线群均为 first-pass 候选；后续可能拆分、合并或改名。
- `c1b934ab56d6f0554c7a7e9d89bb8b5d66b6baaa` 是大规模 baseline 封存提交，新增 2207 个 changed paths；它会放大当前路径资产可见性，不能替代这些资产的来源 commit。
- POC verdict、PASS/FAIL、qualification、live observed、proof correctness 等都尚未回到原始 artifact。
- 当前 active research 的最终集合未知；提交时间新和“交接/当前”标题都只能作为候选信号。

## Classification Limits

- `commit-ledger.tsv` 的五方向 impact 字段由 subject/path/numstat first-pass 规则标记，含义是 `candidate` 或 `none`。
- `candidate` 不等于事实存在，`none` 不等于事实不存在。
- 第二轮必须用 exact diff、当前代码、测试和运行实物校准这些字段。
