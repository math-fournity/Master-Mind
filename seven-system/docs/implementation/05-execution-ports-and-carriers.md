# 执行端口、模型载体与调用收据

## 一句话结论

阶段代码只提交冻结job，不直接调用任何CLI。Target Solver和机器认知角色是两个不同端口；Devin CLI可以同时有Solver adapter和认知adapter，但两条执行链必须物理隔离。

## canonical端口

```python
class TargetSolverPort(Protocol):
    def prepare(self, job): ...
    def launch(self, prepared_job): ...
    def observe(self, ticket): ...
    def collect(self, ticket): ...
    def cancel(self, ticket, fence_token): ...
    def reconcile(self, attempt_id, fence_token): ...

class ModelRolePort(Protocol):
    def prepare(self, job): ...
    def submit(self, prepared_job): ...
    def observe(self, ticket): ...
    def collect(self, ticket): ...
    def reattach(self, attempt_id, fence_token): ...
    def cancel(self, ticket, fence_token): ...
    def reconcile(self, attempt_id, fence_token): ...

class HumanTaskPort(Protocol):
    def create_task(self, frozen_view): ...
    def collect_response(self, task_id): ...

class HumanGateService(Protocol):
    def decide(self, signed_decision): ...
    def verify(self, decision_id): ...
```

HumanTask只收集人工意见，不能签Gate；HumanGate不调用模型。

## RoleTypeRegistry

`ModelRolePort`不接受自由字符串角色。当前机器认知角色全集由append-only、带hash的`RoleTypeRegistry`冻结：

```yaml
registry_id: seven_model_role_types
registry_version: 1.0.0
schema_version: role_type_registry.v1
status: FROZEN
implementation_status: NOT_IMPLEMENTED
role_types:
  - question_architect
  - adversarial_editor
  - math_verifier
  - trace_analyst
  - solution_analyst
  - adjudicator
  - process_auditor
  - proof_judge
  - leakage_auditor
  - selector
  - hint_renderer
supersedes_ref: null
content_hash:
```

这些role type按职责分为：P3A出题链的Architect/Editor/Verifier，P3N的Trace/Solution Analyst与Adjudicator，P6的Process/Proof/Leakage三审，以及可能由模型承担的Selector/Hint Renderer。`CaseLab reviewer`不是可调度的兜底角色名，必须映射为上述精确职责；确需新职责时先发布新registry版本。

Target Solver、HumanTask、HumanGate、Blinding Broker、Schema validator、hash/seal/reconcile等纯程序角色不在本registry中。Target Solver只能走`TargetSolverPort`；人工与纯程序工作也不能伪装成`ModelRolePort`角色。

注册表规则：

1. 新增、删除、重命名或改变角色语义必须生成新`registry_version + content_hash`，不得覆盖旧版本；
2. `RoleExecutionContract`必须同时引用registry及精确`role_type_id`；未知role、已退役role、hash不一致或使用`...`/自定义字符串都在`prepare`前BLOCK；
3. 旧receipt继续绑定历史registry，不因新版本发布而改写；新registry不会自动继承旧资格矩阵；
4. `selector`或`hint_renderer`若由确定性程序执行，不产生ModelRole job；只有RuntimeManifest明确选择模型实现时才需要对应资格单元。

## RoleExecutionContract

每个机器角色job必须冻结：

```yaml
role_job_id:
epoch_id:
role_type_registry_ref_and_hash:
role_type_id:
input_view_ref_and_hash:
input_acl_capability_hash:
vault_access_capability_ref_and_hash:
carrier_profile_id_and_hash:
role_qualification_cell_ref_and_hash:
requested:
  carrier:
  model_uid:
  normalized_effort:
  reasoning_mode:
  orchestration_mode:
prompt_release_ref_and_hash:
tool_network_sandbox_policy_ref_and_hash:
output_schema_ref_and_hash:
budget_contract_ref_and_hash:
required_capability_reports: []
idempotency_key:
retry_contract:
independence_requirements:
sensitivity_and_sink:
```

`effective_*`不能预先填在合同中，只能由运行后的receipt记录。

## RoleQualificationMatrix

“adapter在接口上能接收某角色”和“该角色在某个真实profile上已经合格”是两个不同命题。资格以版本化`RoleQualificationMatrix`的精确cell表达：

本节冻结的是目标Schema与路由规则；matrix持久化、签名、投影和Router enforcement当前均为`NOT_IMPLEMENTED`，不能把文档中的初始表当成已生成的运行对象。

唯一机器形状是[`role-qualification-matrix.v1.schema.json`](role-qualification-matrix.v1.schema.json)。每个cell显式保存：

```text
role_type_id
× carrier_id × model_id × carrier_profile hash
× input_view hash × view policy hash × ACL policy hash × VaultAccessCapability hash
× tool/network/sandbox policy hash × output sensitivity/sink policy hash
× prompt hash × output schema hash
× adapter hash × parser hash × capability requirement hash
× CANARY|PRODUCTION
```

`cell_key`是上述字段按Schema顺序canonical化后的SHA-256；没有默认维度，也没有从profile内部“顺便推断”carrier/model的许可。Schema在所有精确字符串和ref处拒绝`*`、`?`、glob字符及`ANY/ALL/DEFAULT`哨兵。矩阵只是已签CapabilityReport的append-only索引/投影，不能靠管理员直接把空cell改成PASS。

同一对象还必须保存`completeness.required_cell_keys / pass_cell_keys / not_tested_cell_keys / failed_cell_keys / extra_cell_keys / missing_cell_keys / remainder_cell_keys / remainder_count / verdict / algorithm_ref_and_hash`。`failed_cell_keys`合并`PARTIAL/FAIL/BLOCKED/EXPIRED`；`missing`是required中根本没有cell的键；`extra`是observed中不在required的键；`remainder`是not-tested、failed、missing与extra的去重并集。只有这些集合互斥/相等关系经semantic verifier重算、`remainder_count=0`且矩阵签名有效时，completeness才可为`PASS`。

资格规则：

- Router只能选择合同中精确引用且`verdict=PASS`、未过期、scope满足本次运行的cell；禁止通配符、前缀、同provider继承或“更强profile应当兼容”的推断；
- Devin `glm-5-2` High adapter在架构上必须能接收registry中的全部机器角色，不设置硬编码三角色allowlist；这只证明公共执行面的可表达性，不证明任一cell的模型能力；
- `WP-CW-D1`首轮live canary只允许`question_architect`、`adversarial_editor`、`math_verifier`三个无敏感输入/输出cell。它们在真实CapabilityReport产生前仍是`NOT_TESTED`，CANARY PASS也不能升级成PRODUCTION PASS；
- 其余role在`WP-CW-D1`阶段保持`NOT_TESTED/NOT_IN_INITIAL_CANARY_SCOPE`。`WP-CW1`须补齐实际启用的P3N/P6角色；`PRODUCTION_SCALE_AUDITED`还须补齐RuntimeManifest中每一个已启用的完整Schema cell（role/carrier/model/profile/view/Vault capability/全部policy/adapter/parser/capability requirement），包括选择模型实现时的Selector/Hint Renderer；
- 要声称“Devin可在生产承担全部当前机器角色”，至少每个registry role都有一个精确Devin production cell PASS，且所有live plan实际使用的组合逐格PASS；Codex和未来adapter适用同一规则；
- role registry、profile/model catalog、view/ACL、tool policy、prompt、output schema、adapter/parser任一hash变化都使相关cell失效并要求新报告；历史调用收据不变。

### Vault输入交付边界

Router通过精确资格cell只说明“这个组合有资格被选择”，并不授予读取Vault的权力。每个`RoleExecutionContract`还必须引用一个[`VaultAccessCapability`](vault-access-capability.v1.schema.json)，由Vault broker在dispatch前产生[`AccessDecision`](access-decision.v1.schema.json)，再按允许的object/view hash生成[`ViewDerivation`](view-derivation.v1.schema.json)并append [`AccessEvent`](access-event.v1.schema.json)。

模型进程只能接收派生后的bytes和opaque `view_id/sink_id`。raw Vault filesystem路径、CAS/Vault locator、源object locator、bearer capability、签名材料和revocation registry handle一律留在可信控制面，不能进入prompt、argv、env、workspace、stdout/stderr或模型可调用工具。decision的任一检查为`FAIL/UNKNOWN`、nonce重放、issuer不可信、capability过期/撤销，或principal/operation/object/view/sink任一不相等时，必须在创建provider请求前`DENY/BLOCK`；不得fallback到更宽view或普通文件路径。

首轮Devin矩阵应初始化为下面的状态，而不是预填PASS：

| role集合 | WP阶段 | 初始scope | 初始verdict |
|---|---|---|---|
| `question_architect`、`adversarial_editor`、`math_verifier` | WP-CW-D1 | CANARY、无敏感输入/输出 | `NOT_TESTED` |
| `trace_analyst`、`solution_analyst`、`adjudicator`、三审 | WP-CW1 | 待冻结精确view/policy | `NOT_TESTED` |
| `selector`、`hint_renderer` | WP-ST1/PRODUCTION，且仅限模型实现 | 待冻结精确view/policy | `NOT_TESTED` |

## DevinCliModelRoleAdapter

### 精确候选profile

2026-08-14本机只读观察：

- resolved CLI：`devin 3000.4.25 (7e8e528a)`；
- `devin models list`中精确UID `glm-5-2`显示为`GLM-5.2 High`；
- CLI没有独立`--effort`参数，High编码在model UID中。

上述仅为静态discovery artifact，不是live capability test。本机二进制可执行性、账号权限、模型可调用性、角色质量、工具/网络/沙箱有效性和usage/cost可观察性一律仍为`NOT_TESTED`。

因此首个候选合同写：

```yaml
carrier: devin_cli
requested_cli_model_arg: glm-5-2
normalized_reasoning_effort: high
effort_encoding: model_uid
reasoning_mode_request_semantics: not_configurable_by_cli
orchestration_request_semantics: fresh_single_top_level_session
model_catalog_snapshot_ref_and_hash: required
```

历史代码中的`glm-5.2-high`不是当前catalog列出的精确UID，Seven不得照抄。未来catalog变化时必须新建CarrierProfile和CapabilityReport。`not_configurable_by_cli`不等于已知effective reasoning mode；receipt必须写`UNOBSERVABLE`。系统能观察的只是每次fresh顶层CLI session；如果某项科学主张依赖模型内部编排模式，而provider/export不能证明，则该profile对该主张必须BLOCK。

### 启动要求

- 使用argv数组，禁止`shell=True`或字符串拼接；
- 完整prompt通过受限`--prompt-file`，不得暴露在进程列表；
- 每attempt全新print session，禁止`--continue/--resume`；
- 强制`--export`到该attempt的受限raw-event目录；
- 使用专用`--config`、环境allowlist和D盘角色workspace；
- 角色workspace不在repo、不在Solver root，不继承Solver AGENTS；
- stdout/stderr若可能含解答，直接进入Vault，不回显普通控制台；
- 角色级permission/tool/network/sandbox策略由合同决定；`dangerous`不是能力证明；
- ATIF/export解析器版本化，对每个generation-bearing assistant/model step记录`generation_model`并核对`glm-5-2`；user/tool/telemetry step不要求该字段，但任一generation-bearing step缺字段即`UNOBSERVABLE/BLOCK`；
- 若effective effort只能由UID+catalog快照解析，receipt必须写明`effort_observation=derived_from_uid`；
- provider是否接受/开始生成不明确时进入`UNKNOWN_START_QUARANTINED`，不得盲重呼。

### 能力探针

每个角色+profile分别验证：

1. binary真实路径、SHA、版本；
2. catalog raw artifact与hash；
3. requested UID和所有generation UID一致；
4. 专用config和global rules污染检查；
5. fresh session、无resume；
6. input view和sibling workspace拒读canary；
7. 工具定义、工具事件、网络和sandbox观察；
8. output JSON解析与Schema验证；
9. export完整性、session ID、token metrics和终止原因；
10. timeout/cancel/partial/seal/reattach；
11. usage/cost可观察性和carrier-global quota；
12. 敏感输出确实进入Vault。

CLI帮助和models list只证明静态候选，不能单独产生PASS。

## CodexExecModelRoleAdapter

### 产品边界与当前状态

`CodexExecModelRoleAdapter`只表示**本地Codex CLI的非交互exec载体**。OpenAI Responses API必须由独立的`OpenAIResponsesModelRoleAdapter`实现，不能把API request、Codex CLI命令和当前交互式Codex任务混成同一adapter。OpenAI正式维度必须分开记录：

- exact model/model snapshot或alias解析状态；
- `reasoning.effort`；
- `reasoning.mode`（如standard/pro，只有provider与账号实际支持时才可请求）；
- orchestration topology（single-agent与Responses multi-agent beta分开）；
- sandbox、tools、network；
- output schema；
- raw event、thread/response ID、usage和cost。

“Ultra-like”只能是对multi-agent编排的非规范描述，不能写入profile枚举、receipt effective field或能力结论；它不等于正式产品中的Codex ultra mode。`gpt-5.6-sol`、`xhigh/max`、standard/pro和Responses multi-agent beta目前都只是待探测候选。本机Codex CLI、账号模型访问、精确flag/config映射、reasoning字段生效、multi-agent能力、子调用可见性、usage/cost与cancel/reattach能力均为`NOT_TESTED`；adapter本身为`NOT_IMPLEMENTED`。

### 冻结profile与结构化请求

Codex CLI profile必须逐项冻结，不能用“high/ultra”一个字符串代替：

```yaml
carrier: codex_exec_cli
backend_kind: local_noninteractive_exec
requested_model:
model_alias_resolution_policy:
requested_reasoning_effort:
requested_reasoning_mode:
requested_orchestration_mode: single_agent
requested_service_tier:
sandbox_policy_ref_and_hash:
tool_policy_ref_and_hash:
network_policy_ref_and_hash:
output_schema_ref_and_hash:
cli_argument_mapping_ref_and_hash:
model_release_or_catalog_snapshot_ref_and_hash:
```

`requested_reasoning_mode`或其他字段若当前CLI没有经CapabilityReport确认的精确映射，`prepare`必须BLOCK，不得静默省略、降级或用环境默认值。single-agent CLI profile不能继承Responses multi-agent beta的PASS，反之亦然。

公共层先生成不可变`CodexExecPreparedRequest`，adapter再以版本化argument mapping物化命令：

```yaml
prepared_request_schema: codex_exec_prepared_request.v1
attempt_id:
role_contract_ref_and_hash:
role_qualification_cell_ref_and_hash:
resolved_executable_path_and_hash:
exact_argv: []              # 完整token数组；seal后不得含占位符
stdin_or_prompt_file_ref_and_hash:
project_doc_ref_and_hash:
isolated_workdir_ref_and_hash:
config_home_ref_and_hash:
environment_allowlist_ref_and_hash:
credential_handle_ref_and_policy_hash:
requested_model_fields:
requested_reasoning_fields:
requested_orchestration_fields:
tool_network_sandbox_fields:
output_schema_ref_and_hash:
raw_event_sink_ref:
provider_native_export_sink_ref:
stdout_stderr_sink_refs:
timeout_cancel_and_fence_contract:
```

命令必须是`[resolved_codex_binary, "exec", ...]`形态的argv数组，由`cli_argument_mapping_ref_and_hash`把每个requested字段一对一映射成该精确CLI版本已验证的flag/config token；禁止shell、字符串拼接、调用者自带任意extra args和运行时补默认值。物化后的`exact_argv`、受限输入、mapping和CLI hash同时seal。尚未通过本机help/schema stub与live capability canary确认的具体flag不得写成“已支持”；缺映射即BLOCK，这正是当前`NOT_TESTED`边界。

若未来实现Responses API，必须生成独立的`OpenAIResponsesPreparedRequest`和adapter receipt，按官方request schema保存`model`、`reasoning.effort`、`reasoning.mode`、tools、input、metadata及任何multi-agent配置；不得由Codex CLI adapter代发，也不得把CLI session ID冒充response ID。

### 隔离、凭据与敏感sink

- 每attempt创建D盘独立role workspace、独立config home和最小project doc；不得在repo、Solver root或其他role workspace运行，也不得继承repo/用户级AGENTS或历史conversation；
- 默认fresh top-level task。除非合同明确要求且能力报告覆盖，不得使用resume、历史thread、`previous_response_id`或共享memory；
- 环境变量只取allowlist。凭据由supervisor以opaque credential handle注入，长期secret不复制到workspace、prompt、argv、普通receipt或普通日志；receipt只留credential pool/policy的非秘密hash；
- project doc只能包含该role所需规则和ACL，不得暴露其他角色、arm、答案或holdout；input file/stdin/API body按`input_view_ref_and_hash`物化并只读挂载；
- sandbox、tool definitions和network策略必须同时记录requested与observed。无法证明实际生效时cell为`BLOCKED/UNOBSERVABLE`；
- request、JSONL/raw events、stdout/stderr和output一旦可能含solution/holdout，必须从创建时直接写受限Vault；禁止先落普通日志再搬运或在控制台回显。

### 生命周期、事件与恢复

`submit`只有在获得provider/CLI可验证的接受物证后才能写`REQUEST_ACCEPTED`；进程fork、PID存在或命令返回0本身都不等于provider accepted。`GENERATION_STARTED`至少需要可归属本attempt的首个generation/reasoning/output事件或provider usage正证据。两者未知时进入`UNKNOWN_START_QUARANTINED`，禁止自动重呼或转Devin。

CLI必须启用该精确版本已资格化的结构化事件模式。原始JSONL/event stream逐字节写append-only sink，保留sequence/timestamp/event type/provider ID；若精确CLI版本提供provider-native export，也必须保存完整export及hash。版本化parser只消费已知Schema。未知event、序号缺口、截断、EOF前无terminal、只剩final文本、所需export缺失或parser版本不匹配均fail-closed。派生output不得替代raw event/export物证；profile若声明export不受支持，必须由CapabilityReport证明raw event链足以覆盖规定字段，不能在运行时临时降级。

adapter必须完整实现`submit/observe/collect/reattach/cancel/reconcile`：

- reattach仅在稳定thread/session/response ID和该backend的CapabilityReport证明可行时允许；否则在profile中预声明`UNSUPPORTED`，恢复时隔离而不是重跑；
- cancel携带fence token并记录发送、provider确认和终态；cancel超时不能假定未生成；
- reconcile对request ID、raw event尾部、partial artifact、usage、terminal state和seal marker逐项对账；未知启动、孤儿进程/response或重复terminal必须隔离；
- fallback、retry或换profile只能创建新attempt，并满足预注册retry contract；不得在同一receipt内改载体。

### 能力探针与测试入口

每个`role × carrier × model × Codex profile × actual view/Vault capability × 全部policy × adapter/parser × capability requirement`精确cell分别验证：

1. executable真实路径、SHA、版本与argument mapping；
2. exact model/alias解析和requested/effective model；
3. effort、reasoning mode、orchestration分别requested/observed，不能相互推断；
4. fresh task、project doc、config、env、credential和历史context隔离；
5. sibling workspace、Solver root与Vault拒读canary；
6. sandbox、tool definitions/events和network观察；
7. accepted与generation-started正证据；
8. JSONL/raw event完整性、provider ID、parser和output Schema；
9. timeout、cancel、partial、reattach/reconcile及未知启动；
10. solution-bearing request/event/output直接进入Vault；
11. tokens、reasoning/child usage、parent-child reconciliation、rate/quota和cost可观察性；
12. fake、protocol stub、经逐次授权的live canary及fault injection全部有测试收据。

fake只证明公共状态机，stub只证明精确命令/事件协议，live canary才可能证明本机+账号+provider能力；三者不得互相冒充。任何profile PASS都不能解锁另一model、effort、reasoning mode、orchestration、role或policy cell。

## AIInvocationReceipt

至少包含：

```yaml
invocation_id:
role_job_id:
attempt_id:
role_type_registry_ref_and_hash:
role_type_id:
role_qualification_cell_ref_and_hash:
role_contract_hash:
carrier_profile_hash:
backend_kind:
binary_or_adapter_version_and_hash:
resolved_executable_path_and_hash:
provider_request_thread_or_session_id:
sanitized_effective_request_ref_and_hash:
restricted_effective_request_vault_ref_and_hash:
sanitized_exact_argv:
restricted_full_argv_vault_ref_and_hash:
config_env_workspace_manifest_hashes: []
requested_and_observed_permission_sandbox_flags:
model_catalog_or_release_snapshot_ref_and_hash:
requested_model_uid:
effective_or_observed_model_uids: []
normalized_effort:
effort_observation:
reasoning_and_orchestration_observation:
input_artifact_hashes: []
output_artifact_hashes: []
raw_event_log_ref_and_hash:
raw_event_schema_and_parser_version:
stdout_ref_and_hash:
stderr_ref_and_hash:
provider_export_ref_and_hash:
request_lifecycle_events:
  - state: REQUEST_ACCEPTED | GENERATION_STARTED | ...
    evidence_ref_and_hash:
tool_definitions_ref_and_hash:
tool_events_ref_and_hash:
tool_network_sandbox_verdict:
output_schema_validation_verdict:
security_classification:
storage_sink_ref:
acl_capability_hash:
usage:
  input_tokens:
  output_tokens:
  cached_tokens:
  cache_write_tokens:
  reasoning_tokens:
  tool_tokens:
  scope_and_child_refs:
usage_completeness:
parent_child_reconciliation_verdict:
provider_billed_amount:
currency:
cost_observability:
pricing_snapshot_ref_and_hash:
wallclock_and_timestamps:
exit_and_terminal_reason:
capability_report_refs: []
retry_replay_lineage:
failure_or_quarantine_state:
```

当前catalog显示GLM profile为Free时，只能把历史catalog价格快照用于derived cost；`provider_billed_amount`不可观察就写`UNOBSERVABLE`，不得把derived amount回填为provider bill。`usage_completeness != COMPLETE`、parent/child未对账或缺pricing snapshot时，正式成本指标必须BLOCK；仍需原样保留可观察的tokens、wallclock、rate limit、quota和人工分钟。

## 路由与Bakeoff

Role Router按`registry role + sensitivity + required independence + exact qualified cell + budget`选择profile。没有精确PRODUCTION PASS cell时生产dispatch必须BLOCK，不得回落到另一个carrier或通用profile。Bakeoff可以得到“Architect默认Devin、Verifier默认Codex”等分角色结论；它只改变未来RuntimeManifest的预注册默认路由，不改写既有receipt，也不把胜者资格传播给未测cell。

严禁：

- 运行失败后自动换模型并把结果算同一attempt；
- 作者与审稿者复用session；
- 同模型fresh session冒充异模型独立；
- 用Target Solver的NoTool报告解锁Devin认知角色；
- 用Devin认知能力报告解锁Target Solver；
- 把外部模型调用隐藏在phase、parser或审计代码中。

## 静态旁路审计

只有以下模块可出现对应外部执行：

- `adapters/solver/devin_solver.py` → 只能调用solver_harness，不得直接调用devin binary；
- `adapters/model_role/devin_cli.py` → Seven内唯一允许直接调用devin binary的模块；
- `adapters/model_role/codex_exec.py` → 只能调用codex binary；
- `adapters/model_role/openai_responses.py` → 若未来实现，只能调用OpenAI Responses API；
- fake/test adapters → 无外部调用。

其他模块出现`subprocess`调用这些CLI、SDK client或shell命令，一律视为绕过端口。
