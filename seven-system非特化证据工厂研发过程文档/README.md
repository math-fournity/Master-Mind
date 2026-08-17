# Seven System 研发过程文档目录说明

Seven已经在自身目录内建立了自包含的正式文档体系。本目录不再复制规定性正文：

- 完整文档总入口与实施者入口：[`../seven-system/docs/implementation/README.md`](../seven-system/docs/implementation/README.md)
- 未来独立审计者入口：[`../seven-system/docs/audit/README.md`](../seven-system/docs/audit/README.md)

本目录只保留未来可能产生的探索记录、阶段委托和被替代方案。这里的文档不得覆盖`seven-system/docs/implementation/`的规定性契约，也不得证明代码已经实现。

## 当前阶段委托

| 编号 | 文件 | 用途 |
|---:|---|---|
| 001 | [`001-v0-2026-08-14-首轮完整实现声明审计后的整改实施技术说明.md`](001-v0-2026-08-14-首轮完整实现声明审计后的整改实施技术说明.md) | 把commit `783d4be...`首轮实现声明的诊断性审计结果转成下一位实施AI可执行、未来审计AI可复验的整改顺序、P0修复规格、测试向量、物证合同和停止门 |
| 002 | [`002-v0-2026-08-14-R1整改后再次复核记录-文档合同恢复但全量实现仍未闭合.md`](002-v0-2026-08-14-R1整改后再次复核记录-文档合同恢复但全量实现仍未闭合.md) | 记录R1当时亲自复核的历史事实：DOC0文档合同、P0-B、P0-C局部PASS，但全量测试仍为2325 tests / 9 failures / 26 errors；该失败快照已被003号R2记录取代 |
| 003 | [`003-v0-2026-08-14-R2亲自整改复核记录-全量测试闭合但未进入独立审计.md`](003-v0-2026-08-14-R2亲自整改复核记录-全量测试闭合但未进入独立审计.md) | 记录R2亲自整改后的事实：DB1I已迁到真实HumanGate+EEA/LiveRunPermit/RESERVED授权链，R5已迁到WorkPackagePlan+CompletionRecord路径，DOC0 bootstrap evidence、普通WorkPackagePlan/ImplementationBundle候选物证、NormativeReviewRecord语义验证器、GA1审计输入包机械预检/覆盖报告与DB1L只读逻辑站点报告预检已有受控组装/验证器；文档合同、targeted 282 tests、全量2385 tests与diff-check均PASS，但仍未进入GA1独立审计、live副作用或科学Evidence |

使用顺序：下一位实施AI先读根/Seven `AGENTS.md`，再读001号整改委托、002号失败复核记录和003号闭合复核记录，随后回到canonical implementation入口按DAG整理候选CompletionBundle并准备GA1独立审计。001/002/003号不得被用来绕过canonical Plan、依赖、签名、授权、CompletionBundle或GA1。
