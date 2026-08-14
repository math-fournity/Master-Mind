"""WP-OP1 Operations/Scale — multi-worker, Redis projection, multi-Epoch,
active learning, soak, cross-Epoch budget, active release pointer,
cross-Epoch duplicate assessment, longitudinal learning verdict.

来自 docs/implementation/15-work-package-implementation-contracts.md WP-OP1：

冻结输入: VR1候选系统、资源policy；activation另需GA1 AUDITED_PASS
必需实现/对象: multi-worker、Redis投影、多Epoch/active learning/soak
blocker与故障验收: 未审即live、饥饿、队列丢失、中途换版本、holdout重用
READY_FOR_AUDIT最低产物: soak、Redis重建、create→seal→next Epoch、跨Epoch remainder=0

SIDE_EFFECT_FREE：纯内存模拟，不部署真实 multi-worker、不写真实 Redis、
不启动 Solver、不调真实模型。真实 scaling 需要 GA1 AUDITED_PASS（auditor-owned，
当前 blocked）。
"""

from __future__ import annotations
