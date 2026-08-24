# POC-VMS-41R1 hidden join simulator：零模型端到端

**日期**：2026-08-14  
**状态**：`DEVELOPMENT_SIMULATOR / NO_REAL_LIVE_OUTPUT`  
**阶段**：`SV-S2.13`  
**前置**：375号sealed manual judgment合同  
**代码入口**：`system/tests/solve_vein_analysis/vms41r1_hidden_join_simulator.py`

---

## 1. 本阶段做什么

本阶段用全假的、可复验的物件跑通未来join顺序：

1. 使用冻结reference candidates作为fake candidate outputs；
2. 生成synthetic sealed manual judgment；
3. 先验证manual judgment合同；
4. 再读取hidden acceptable set并运行机械V2 evaluator；
5. 形成development-only join verdict。

这一步证明的是**顺序和接口**，不是证明真实Devin输出有效。

---

## 2. 为什么还不能live

当前仍缺：

- 人签LiveRunPermit；
- 真实Devin candidate outputs；
- 真正的blind review package materialization；
- 真实Reviewer sealed judgment；
- live bundle与D盘append-only receipt。

因此本阶段严禁启动Devin、Solver、DB、Redis或网络。

---

## 3. 命令

```bash
.venv/bin/python \
  system/tests/solve_vein_analysis/vms41r1_hidden_join_simulator.py
```

预期：

- `schema_version = solve-vein/vms41r1-hidden-join-simulator/v1`；
- `simulator_status = DEVELOPMENT_ONLY`；
- `case_count = 6`；
- 每行`manual_judgment_validated_before_hidden_eval = true`；
- 全部reference candidate行得到`JOIN_PASS_DEVELOPMENT_ONLY`；
- 全部side effects为0。

---

## 4. 关键反例

测试必须证明：

- hidden暴露的manual judgment在hidden join前被拒绝；
- case/attempt不匹配的manual judgment被拒绝；
- 使用negative mutation后的fake candidate不会得到join PASS；
- CLI输出只是development simulator receipt，不创建live workspace。

---

## 5. 非主张

本阶段不主张：

- 有任何真实live candidate output；
- 有任何真实人工盲审；
- Event Extractor profile已资格化；
- manual judgment已经可以替代hidden grader；
- VMS-41旧attempt可重跑。

---

## 6. 下一步

如果继续零模型推进，下一步可以做：

- fake live bundle materializer；
- blind review package materializer；
- final qualification join receipt schema。

如果要进入真实VMS-41R1 live资格实验，必须先获得新的明确人签LiveRunPermit。
