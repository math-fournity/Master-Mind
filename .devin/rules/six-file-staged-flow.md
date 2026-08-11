# 文件拆分流程控制规则

**触发条件**：always-on——设计提示词时，当一个AI session的工作流程有多个阶段且thinking可能过大时。

## 核心问题

单个AI session的工作流程有多个阶段时，AI会在一个thinking中想所有阶段的问题——thinking内容爆炸，导致：
- output token超限truncated
- thinking时间过长
- 某些阶段的thinking质量下降（因为上下文被其他阶段占满）

## 核心秘诀：文件拆分流程控制

**不是拆成多个session（那会引入认知过程断裂风险——见335号V8拆分分析），而是在同一个session内用文件拆分控制thinking。**

### 三步法

**第一步：先创建文件**

AI一上来就先创建所有输出文件（空文件或带骨架结构的占位文件）。这一步的目的是：
- 让AI明确知道有哪些输出要完成
- 每个文件的存在是一个"待完成"的提醒
- 避免AI在thinking中"规划所有输出"——文件已经规划好了

**第二步：要求文件拆分**

把工作阶段的要求拆分成多个独立的要求文件，每个要求文件对应一个输出文件：
- `step1_requirements.md` → `segments.json`
- `step2_requirements.md` → `features.json`
- `step3_requirements.md` → `formal_context.json`

每个要求文件只包含该阶段的要求，不包含其他阶段的要求。

**第三步：一次一个要求+一个输出**

AI按顺序执行：
1. 完整读取`step1_requirements.md` → 填充`segments.json` → 创建`step1_done.md`标记
2. 完整读取`step2_requirements.md` → 填充`features.json` → 创建`step2_done.md`标记
3. 完整读取`step3_requirements.md` → 填充`formal_context.json` → 创建`step3_done.md`标记
4. 所有步骤完成 → 创建`DONE.md`

**关键约束**：AI每次只读一个要求文件，只填充一个输出文件。不要在读取step2要求时回头修改step1的产出。不要在thinking中同时考虑多个阶段。

## 为什么有效

1. **分批进入上下文**——每个阶段的要求只在需要时进入AI的上下文，不是一开始就全部加载。AI的thinking空间只关注当前阶段。

2. **文件的存在是流程控制**——`step1_done.md`的存在告诉AI"step1已完成，进入step2"。不需要AI在thinking中记住"我做到哪一步了"——文件系统替它记。

3. **不引入认知过程断裂**——和拆成多个session不同，文件拆分流程控制在同一个session内完成。AI仍然能看到所有阶段的产出文件（因为都在同一个工作目录），只是不被要求在一个thinking中同时处理所有阶段。

## 实例：V8格化session的改进（335号方案）

V8的原始设计：一个提示词文件包含所有要求（段划分+常规特征标注+角色特征标注+矩阵构造），AI在一个thinking中做所有事情——thinking爆炸。

V8的文件拆分流程控制设计：

```
工作目录：
├── AGENTS.md                    ← 角色和约束
├── input.md                     ← 解答文本
├── step1_requirements.md        ← 段划分要求
├── step2_requirements.md        ← 常规思维特征标注要求
├── step3_requirements.md        ← 关键实体角色特征标注要求
├── step4_requirements.md        ← 形式上下文矩阵构造要求
├── segments.json                ← step1产出（AI先创建空文件）
├── features_conventional.json   ← step2产出（AI先创建空文件）
├── features_role.json           ← step3产出（AI先创建空文件）
├── formal_context.json          ← step4产出（AI先创建空文件）
└── DONE.md                      ← 完成信号
```

AI的执行流程：
1. 先创建segments.json/features_conventional.json/features_role.json/formal_context.json（空文件）
2. 读step1_requirements.md → 划段 → 填充segments.json → 创建step1_done.md
3. 读step2_requirements.md → 读segments.json → 标注常规特征 → 填充features_conventional.json → 创建step2_done.md
4. 读step3_requirements.md → 读segments.json → 识别关键实体角色 → 填充features_role.json → 创建step3_done.md
5. 读step4_requirements.md → 读features_conventional.json+features_role.json → 构造矩阵 → 填充formal_context.json → 创建step4_done.md
6. 创建DONE.md

## 和333号三阶段架构的关系

333号的三阶段架构是**session间拆分**——格化session→程序枚举→综合分析session，session间通过文件传递。

文件拆分流程控制是**session内拆分**——同一个session内用文件拆分控制thinking。

两者可以叠加使用：333号的三阶段架构中，格化session（阶段1）内部可以用文件拆分流程控制（V8的4步），综合分析session（阶段2）内部也可以用文件拆分流程控制（7步工作流程的每一步对应一个要求文件+一个输出文件）。

## 和335号V8拆分分析的关系

335号分析了V8拆成V8a+V8b两个session的风险——认知过程断裂。结论是不拆分。

文件拆分流程控制是335号分析的替代方案——不拆session（保留认知过程的统一性），但用文件拆分控制thinking（解决thinking过大的工程问题）。这正是335号需要的"其他方式解决"。
