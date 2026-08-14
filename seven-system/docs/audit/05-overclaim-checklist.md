# 过度主张检查表

审计结束前逐项确认没有把左侧偷换成右侧：

- Schema存在 ≠ runtime已实现；
- unit test PASS ≠ live能力PASS；
- CLI存在 ≠ 指定model/effort真实生效；
- `devin models list`显示`glm-5-2` ≠ 认知adapter能力PASS；
- requested profile ≠ effective/observed profile；
- 两个adapter可import ≠ 两个adapter已资格通过；
- 同一Devin binary有两个adapter ≠ 两执行面已隔离；
- dry-run PASS ≠ canonical P1完成；
- D-backing PASS ≠逻辑DB/Schema PASS；
- 离线DB contract PASS ≠真实site/apply PASS；
- QuestionRelease数学正确 ≠ Devin bare失败；
- Devin bare失败 ≠ 认知机制失败；
- bare准入 ≠ P5因果实验；
- 单次guided成功 ≠ Tell有效；
- 单题contrast ≠ 非特化泛化；
- 同模型fresh session ≠ 异模型独立；
- Devin/Codex不同carrier ≠ 不同基础模型；
- 跨载体fallback成功 ≠ 同一实验条件；
- 日志没看到tool ≠ 工具被物理禁止；
- proof正确 ≠ 采用目标题机制；
- 方向词出现 ≠ action执行；
- calibration胜出 ≠ qualification通过；
- regression通过 ≠ prospective通过；
- 一次修订循环 ≠ 长期持续学习；
- Factory PASS ≠ Scientific SUPPORTS；
- Golden Slice runnable ≠ Production Scale Ready；
- 实施者READY_FOR_AUDIT ≠ AUDITED_PASS；
- 文档“已批准方向” ≠ 用户授权本次付费调用/写库/生产运行。

任一过度主张进入机器Verdict、CapabilityReport或实现状态，至少是P1；涉及泄漏、DB、Gate、证据覆盖或科学伪PASS时是P0。
