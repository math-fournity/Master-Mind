"""
representation: Phase 7——表示运输、长证明和高级数学分析

对应137号Phase 7 Check List（v4版本，经162号v4维度19/20/21预防性审计修正）。

模块结构：
- representation_map: P7-1.1 类型化表示映射（127号§5的12字段+6枚举）
- soundness_obligation: P7-1.2/P7-1.COMP soundness义务验证（SoundnessViolationError强制）
- transport_fidelity: P7-1.2b 转换保真验证（3项保真验证）
- fermat_chain: P7-1.2c/P7-2 费马案例完整链条（4环节+3层阶梯+6条大师启发）
- source_version: P7-1.4 来源版本和撤稿状态监控（R-15防线）
- groupoid_check: P7-1.COMP3 groupoid条件检查（2限定词+GroupoidViolationError）
- path_equivalence: P7-3.1 证明路径等价分类（3类等价判定）
- commutative_diagram: P7-3.2 交换图验证
- transport_objects: P7-3.3 等价表示间运输5对象
- local_view: P7-4.1/P7-4.2 局部视图一致性+层式粘合
- hole_detector: P7-4.3 洞识别（4种候选障碍+HoleTypeError）
- egraph: P7-5.1/P7-5.2 e-graph+equality saturation
- trajectory_alignment: P7-6.1/P7-6.2 轨迹嵌入+4种对齐方法
- geometry_guard: P7-6.COMP 几何方法用途限制
- tda_gate: P7-7.1/P7-7.1b TDA数据充分性4限定词
- persistent_homology: P7-7.2 持久同调
- hott_gate: P7-8.1/P7-8.1b HoTT形式对象充分性3限定词
- hott_directions: P7-8.2 HoTT三个真实方向
- baseline_comparison: P7-7.3/P7-8.3/P7-EXIT-1b 3基线比较维度量化
- math_label: P7-MATH 数学主张标注3级别
- phase_gate: P7-8.4/P7-8.5 分阶段进入顺序+防止过早数学包装
- mislabel_guard: P7-8.COMP4-6/P7-STOP-2 误标注防线
"""
