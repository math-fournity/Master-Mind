"""
experiments模块：同可观测checkpoint分层随机实验

对应134号P4-CODE-1。

123号§49 + §39(DYN-3) + §40(DYN-4) + §41(DYN-5)：
- 同内容哈希checkpoint分层并随机分配多个非确定continuation
- 无提示/H0/H1/H2四组处理
- 测局部效应和帮助量曲线
- 新题迁移

模块文件：
- llm_backend.py：LLM后端封装（devin cli）
- checkpoint_layer.py：checkpoint分层+continuation分配
- treatment_groups.py：四组处理定义（control/H0/H1/H2）
- experiment_runner.py：实验运行器（冻结manifest+随机分配+日志）
- effect_estimator.py：局部效应+ATE+异质性估计（分层/配对统计）
- help_curve.py：帮助量响应曲线（DYN-4）
- migration_tester.py：跨题迁移验证（DYN-5）
- side_effect_logger.py：负效应+无效规则记录
- pilot_runner.py：Pilot实验运行器（G0-3/G0-4方差估计）
- test_phase4.py：集成测试
"""
