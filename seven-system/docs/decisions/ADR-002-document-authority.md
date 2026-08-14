# ADR-002：实现规范与审计规范留在Seven内部

- **状态**：ACCEPTED
- **日期**：2026-08-14

## 决策

稳定、规定性的完整实现和审计文档统一放在：

- `seven-system/docs/implementation/`
- `seven-system/docs/audit/`
- `seven-system/docs/decisions/`

外部研发过程目录只可保存探索史、委托记录和被替代方案，不得成为运行时唯一真值源。这样Seven未来迁成独立repo时不会丢失实现和审计认知。

## 文档职责

- `implementation/`：完整目标和实施方法；
- `audit/`：未来独立审计程序；
- `decisions/`：重大裁决与取代关系；
- `implementation-status.md`：当前真实能力；
- `operations.md`：当前已经验证可运行的命令；
- 387/389及外部研究文档：设计来源与历史。

任何实现AI都必须从`implementation/README.md`进入。发生冲突时必须形成冲突记录并停止，不得自行选择最宽松解释。
