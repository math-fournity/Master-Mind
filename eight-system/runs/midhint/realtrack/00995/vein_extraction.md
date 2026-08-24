# polymath_00995 · Phase B 脉络提取记录（读tell实践）

> 日期：2026-08-16｜提取者：Master Agent（亲手通读bare thinking全文1095行/63,289字符）
> bare run：exp_id `p892ddcf48a1f47829efb`（status: failed，thinking被token截断，未输出证明/答案）
> 数据源：`/data/math-agent-glm5.2-tmux-agents-trajectory/p892ddcf48a1f47829efb/exports/conversation.json`（reasoning全文已dump到本目录 `bare_thinking.txt`）

## 一、真实地读：AI建立了什么（逐项核验过的脉络）

| # | AI建立的结论 | 我的核验 |
|---|---|---|
| 1 | **归约**：行列均值整数 ⟺ 行列和被n整除 ⟺ 只看mod n残差；问题化为"n个0..n−1各出现n次填n×n格，行列和≡0 (mod n)" | ✓正确（值的q部分贡献n的倍数） |
| 2 | 总和条件自动满足，无排除力 | ✓（n²(n²+1)/2总能被n整除） |
| 3 | n=1平凡；**n=2不可能**（行必须同残差→列必混合） | ✓（我的程序验证IMPOSSIBLE一致） |
| 4 | **奇数n构造**：循环方阵a_ij=(i+j) mod n | ✓（我的手工证明一致） |
| 5 | **n=4显式构造**（0112/0332/2110/2330） | ✓（程序验证POSSIBLE一致） |
| 6 | **配对构造**：(r, n−r)对+特殊列(0,0)/(m,m)，当且仅当m=n/2为偶（即4|n）时列和m²≡0 | ✓（代数核验一致） |
| 7 | **CRT乘积闭包**：gcd(a,b)=1且a,b可行⇒ab可行（显式乘积排列） | ✓（推导逐步核验一致） |

## 二、卡点（AI的数学处境）

- **唯一未决类：n ≡ 2 (mod 4)**。AI明确知道这一点（它写下了猜想"iff n≢2 (mod 4)"但未证明）。
- 它的尝试全部在**构造方向**：n=6行类型匹配（奇偶配对失败）、mod2与mod3必要条件分别满足但无法合并、正在检查"m×m→2m×2m倍增构造"时thinking被截断。
- **AI从头到尾没有尝试过 n ≡ 2 (mod 4) 的不可能性证明**。它甚至一度猜想"除n=2外全部可行"。
- 深层诊断：AI已经在局部表示（mod n）里工作，但**没有向更细的局部层级下沉**（行和除以n后的商的奇偶、即mod 2n/v₂层面的结构）——这正是缺失的表示切换。与1843的实测失败形态（mod-2停滞、需mod-4）同构。

## 三、真实地给：Hint匹配

- 匹配对象：TellCore v0（局部-全局表示切换）direction原文，**纯Level-3非特化**（不带1631那样的Euler准则尾巴——那是Phase 0旧版做法，违反非泄漏）。
- Hint文本（冻结）："When the problem is stuck in its current representation, try switching to a local representation (such as Z/pZ or Q_p); look for hidden algebraic structure in the local representation, and lift the local finding back to a global conclusion."
- 匹配论证：卡点的解出路（据标准分类n≢2 mod 4不可行）在于在更细局部（mod 2n / 行和的v₂ / CRT局部分解）发现障碍结构并提升为全局不可能性——direction所指的"切换局部表示找隐藏结构"正对此处。Hint不含任何题目细节（无"mod 4"、无"不可能"、无具体p）。

## 四、脉络文本

见 `00995_MH_midhint.txt`（题面+已建立的脉络7条+卡点描述+Hint）。非泄漏自查：脉络只含AI自己已建立的结果；卡点如实描述"不知可行与否"；最终分类与总和3800不出现在任何位置。

## 五、树形化记录字段（本圈循环的链式记录）

- parent_run: `p892ddcf48a1f47829efb`（bare，failed）
- 卡点节点：n ≡ 2 (mod 4) 类未决（构造尝试穷尽、无不可能性论证）
- hint边：TellCore_v0_local_global_switch direction（Level 3）
- child_run: `eight-mh-00995-MH`（待启动）
