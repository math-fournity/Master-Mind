# 目标操作者 CLI 与控制 API 合同

> **状态**：`DESIGN_FROZEN / NOT_IMPLEMENTED`。本文定义完整系统的目标操作面，不表示当前 `seven.py` 已提供这些命令。当前已验证命令只以 [`../operations.md`](../operations.md) 为准。

## 一句话结论

操作者只通过受版本控制的 CLI/API 创建冻结对象和提交动作意图；CLI 不直接绕过 Port 调 provider、raw DB、Redis 或 HumanGate。所有有副作用命令都是 `plan → verify → permit → apply → receipt`。

## 公共调用合同

每条命令必须支持：

```text
--site-config <path>       明确站点配置，禁止默认DB/数据根
--request-id <uuid>        操作者请求幂等键
--expected-input-hash <h>  所读冻结对象的hash
--output json              机器可读结果
--dry-run                  只生成计划/预期变更，不发生外部副作用
```

命令输出统一包含 `command_id`、`request_id`、输入 hashes、结果对象/ref/hash、side-effect counts、verdict、next allowed actions 和 explicit nonclaims。重复 `request_id + identical inputs` 返回已有结果；相同 ID、不同输入立即 `CONFLICT/QUARANTINE`。

## 退出码

| 码 | 含义 |
|---:|---|
| 0 | 结构完整且命令科学/业务结果已合法封存；结果可以是科学负面 |
| 2 | 用户输入、Schema、配置或命令用法错误 |
| 3 | `BLOCKED`：能力、授权、环境或当前兼容性不满足 |
| 4 | `CONFLICT/QUARANTINED`：hash、fence、重复提交、泄漏或盲化冲突 |
| 5 | 协议有效的科学/Case/Gate拒绝；不等于基础设施故障 |
| 6 | `INCONCLUSIVE_DUE_TO_PROTOCOL`：不得推断科学PASS/FAIL |

历史命令若已使用不同退出码，实现时要通过版本化 adapter 保持兼容，不能静默重定义。

## 目标命令面

### 环境、能力与工作包

```text
seven version
seven capabilities [--kind <registry-kind>] [--profile <id>]
seven preflight --manifest <path>
seven wp plan --wp <id> --baseline <commit> --spec-hash <hash>
seven wp start|status|complete --wp <id> --attempt <id>
seven verify-bundle --bundle <ref> --subject-tree <hash>
```

`wp complete` 最高只写 `READY_FOR_AUDIT`；它不接受 `--audited-pass` 类参数。

### 存储、DB与恢复

```text
seven storage probe|verify|reconcile-plan
seven db site inspect
seven db schema plan
seven db schema apply --plan-hash <h> --permit <ref>
seven db schema verify --expected-spec-hash <h>
seven reconcile plan --scope <epoch|job|attempt>
seven reconcile apply --plan-hash <h> --permit <ref>
```

`inspect/plan/verify/reconcile plan`只读。`apply`必须接收未撤销、未过期的`LiveRunPermit`，验证它是有效`ExternalExecutionAuthorization`的不可扩权子集，并在调用外部边界前原子预留一个精确action ordinal；adapter不能直接消费EEA。结果必须落`AuthorizationConsumptionReceipt`。CLI中不存在`--yes-really-write`等布尔授权。

### Epoch、队列与停止

```text
seven epoch create --manifest <ref>
seven epoch start --epoch <id> --permit <ref>
seven epoch pause|stop --epoch <id> --expected-checkpoint <hash>
seven epoch resume --epoch <id> --expected-checkpoint <hash> --permit <ref>
seven epoch status --epoch <id>
seven epoch seal --epoch <id> --expected-remainder 0
seven queue status|drain --epoch <id>
seven queue rebuild --epoch <id> --projection-plan-hash <h> --permit <ref>
```

`pause/stop/kill-switch/quarantine`是安全优先动作：先阻止新dispatch，再drain writer、checkpoint和reconcile，不得因为缺少新permit而被阻止。`resume`会重新开放外部dispatch，必须重跑runtime compatibility与全部绑定CapabilityReport，并消费覆盖剩余动作的新鲜permit；不允许把新release/profile偷混进原Epoch。`queue rebuild`会写Redis投影，同样必须消费精确permit；只读`status`与纯drain不得借机写投影。

### 输入、出题与Case

```text
seven intake import --candidate-manifest <ref>
seven authoring plan --brief <ref> --evaluation-pack <ref>
seven authoring run --plan-hash <h> --profile <qualified-profile> --permit <ref>
seven human-task create --payload <ref> --gate-type <type>
seven human-task submit-response --task <id> --response <ref>
seven human-gate submit --signed-decision <ref>
seven case qualify-bare --question-release <ref> --plan <ref> --permit <ref>
seven case freeze --admission-task <id>
```

`authoring run` 不能直接发布题面；只有验签 `G-Q-RELEASE` 能产生 QuestionRelease。`case qualify-bare` 不接受 Tell/Hint 字段，不得 retry-until-failure。

### 实验、审计、证据与版本

```text
seven experiment preregister --plan <ref>
seven experiment run --plan-hash <h> --permit <ref>
seven audit dispatch --run <ref> --audit-plan <ref> --permit <ref>
seven audit join --sealed-audits <refs>
seven evidence aggregate --plan-hash <h>
seven revision diagnose --evidence-record-set <ref> --provenance-snapshot <ref>
seven revision propose --proposal <ref>
seven revision evaluate --proposal-hash <h> --permit <ref>
seven release activate --release <ref> --signed-gate-decision <ref> --permit <ref>
seven verdict build --epoch <id>
seven replay --verdict <ref> --check-remainder
```

`evidence aggregate`仅消费预注册contrast和已sealed RunAudit；不接受人工直接传`supports=true`。`revision evaluate`不能由proposal生成者自批，不得重用已消耗prospective pack。`release activate`必须同时验证独立promotion Gate和覆盖该精确release/pointer的LiveRunPermit；Gate批准不等于外部执行授权。

## OperatorCommandRegistry

命令列表不能只存在于帮助文本。实现必须按[`operator-command-registry.v1.schema.json`](operator-command-registry.v1.schema.json)生成版本化、可哈希的`OperatorCommandRegistry`，并由CLI、未来HTTP API、worker API、operations文档和Capability机器列表共同消费。每个entry至少包含：

```yaml
command_id:
surface_bindings: []          # CLI argv / HTTP operation / worker message type
command_schema_ref_and_hash:
application_service_and_method:
final_ports: []
effect_class: READ_ONLY | SAFETY_ONLY | EXTERNAL_SIDE_EFFECT
authorization_contract:
  requires_external_execution_authorization:
  requires_live_run_permit:
  required_action_kind:
  authorization_action_registry_entry_ref_and_hash:
  requires_human_gate_decision:
idempotency_and_fence_contract:
  request_id_required: true
  expected_input_hash_required: true
  expected_revision_or_fence_required:
  reservation_and_dispatch_atomic:
  duplicate_identical_behavior: RETURN_EXISTING_RESULT
  duplicate_conflicting_behavior: CONFLICT_OR_QUARANTINE
  unknown_start_behavior: NOT_APPLICABLE | UNKNOWN_START_HELD_OR_QUARANTINE
safety_semantics_if_any:
receipt_types: []
allowed_exit_codes: []
introduced_in / deprecated_in:
```

`READ_ONLY`必须用零写入/零provider调用测试证明；它的EEA、permit、action entry和HumanGate字段在Schema中都固定为false/null。`SAFETY_ONLY`只能收窄或停止活动，必须携带`narrows_activity_only=true / can_resume_or_activate=false / can_increase_external_work=false`，不能暗中重启、重建或切pointer。`EXTERNAL_SIDE_EFFECT`在Schema层固定要求EEA、LiveRunPermit、非空canonical action registry entry、fence以及`reservation_and_dispatch_atomic=true`；不能靠semantic verifier事后把一个fail-open entry补成安全。新增任一CLI/API/worker入口都必须先进入新registry version，未知operation fail-closed。

Registry自身使用RFC 8785 JCS，并把`registry_hash`视为`null`计算SHA-256。跨entry semantic verifier还必须拒绝重复`command_id`、同一surface binding指向多个command、command/action registry hash不一致、未知Port/receipt/exit code，以及`effect_class`与真实调用图不一致。每个真实外部副作用entry最终消费[`external-execution-authorization.v1.schema.json`](external-execution-authorization.v1.schema.json)、[`live-run-permit.v1.schema.json`](live-run-permit.v1.schema.json)和[`authorization-consumption-receipt.v1.schema.json`](authorization-consumption-receipt.v1.schema.json)；Registry里的布尔值不是授权本身。

## API和CLI的唯一业务层

CLI 是薄 adapter：参数解析后调用同一个应用服务层，不在 CLI 里复制业务规则。若未来增加 HTTP/worker API，必须重用同一命令对象、授权、幂等键、fence 和 receipt；禁止出现“CLI 会验 Gate，worker API 不会”的旁路。

## 实现与审计硬要求

1. parser 只组装类型化 Command，不直接 `subprocess`、ArangoClient 或 Redis client；
2. 每条命令都有 fake/in-memory happy path、blocker、重复请求、stale fence 和 crash test；
3. 命令帮助、Schema、operations、Capability机器列表和`OperatorCommandRegistry`双向同步；
4. `NOT_IMPLEMENTED` 命令必须在发生副作用前 fail-closed，不能默默返回0；
5. 独立审计从registry枚举CLI/API/worker全部入口，验证每个入口到应用服务、Gate/permit、Port和receipt的调用图；未登记入口、登记但不可达entry、分类漂移及旁路搜索的remainder必须为0。
