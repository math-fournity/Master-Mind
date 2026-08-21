# HANDOVER · 1962 · Round 4 → Round 5

## 0. 唯一任务（先读这个）

前三块（全偶/恰一偶/两偶一奇）已三轮闭环，**禁止触碰**。你只做两件事：

1. **证明全奇情形中 α≥3 不可能**（α 定义见 §2；α=1 分支 R4 已完整解决，勿重做）。
2. 完成 α≥3 矛盾后，**立即组装 proof.md**（结构见 §5）。

输出预算随时耗尽（前四轮均死于32000 tokens）——每完成一小块立即写入 proof.md。

## 1. 题目

Determine all triples $(a, b, c)$ of positive integers for which $ab-c$, $bc-a$, and $ca-b$ are powers of $2$.

Explanation: A power of $2$ is an integer of the form $2^n$, where $n$ denotes some nonnegative integer.

## 2. 全奇情形已知结构（r4_thinking.md 为准，行号标注）

记号：$ab-c=2^x,\ bc-a=2^y,\ ca-b=2^z$，WLOG $a\le b\le c$，全奇 ⟹ 严格 $a<b<c$、严格 $x<z<y$、$x,y,z\ge1$、pairwise gcd = 1（r4 L479-483 新引理：任何解的两两 gcd 是 2 的幂）。

### 2.1 核心参数与关系 [R3/R4 建立，直接用]

- $v_2(a^2-1)=x,\quad v_2(b^2-1)=x,\quad v_2(c^2-1)=z$。
- 奇参数：$\alpha=\frac{a^2-1}{2^x},\ \beta=\frac{b^2-1}{2^x},\ \gamma=\frac{c^2-1}{2^z}$（正奇数），满足：
  $$\text{(A)}\ 2^{z-x}=b\alpha-a,\qquad \text{(B)}\ 2^{y-x}=a\beta-b,\qquad \text{(C)}\ 2^{y-z}=a\gamma-c.$$
- 记 $s=z-x\ge1,\ t=y-z\ge1$（故 $y=x+s+t$）。则 (A)(B) 可重写为：
  $$\text{(D)}\quad a(\beta+2^t)=b(2^t\alpha+1),$$
  且 $b=\frac{a+2^s}{\alpha}$（由 (A)：$\alpha b = a+2^s$）。
- 恒等式 (E)：$a\alpha\beta=a+2^s(1+2^t\alpha)$（R4 已独立验算，r4 尾部）。
- $v_2(n^2-1)=x \iff n\equiv\pm(1+2^{x-1})\pmod{2^x}$（$x\ge2$）（r4 L613）。
- $\beta>\alpha$（因 $b>a$）且均为奇 ⟹ $\beta\ge\alpha+2$。
- R4 归约成果（L638）：全奇解必须满足条件组 (P1)–(P4)（详见 r4_thinking.md 尾部），其中 P2 即 $b=(a+2^s)/\alpha$、$\alpha\mid a+2^s$。

### 2.2 α=1 分支 [R4 已完整解决——你的对照模板]

$\alpha=1\iff a^2-1=2^x\iff(a-1)(a+1)=2^x$，连续偶数同为2幂只有2和4 ⟹ $a=3,x=3$。继而 $c=3b-8$，$2^z=8(b-3)$ ⟹ $b=3+2^t$；$b\equiv5\bmod8$ 支给 $t=1,b=5,z=4,c=7$ 即 $(3,5,7)$✓；$t\ge3$ 支因 $v_2(c^2-1)=t+1\ne z=3+t$ 矛盾。（r4 L279-285）

## 3. 你的主攻点：α≥3 的矛盾

R4 在此方向已有素材（均未完成）：

- (D) 是主战场：$a(\beta+2^t)=b(2^t\alpha+1)$，代入 $b=(a+2^s)/\alpha$ 可得关于 $a,\alpha,\beta,s,t$ 的约束。
- r4 L505 曾猜 $b\mid 2^{y-x}-1$ 但**已被自我证伪**（$(3,5,7)$ 上 $5\nmid3$，r4 L543）——不要复活这条。
- r4 L427 起的多条大小估计（G1/G2 等）方向正确但未收敛。
- 可考虑的角度：
  1. (D) 移项后做 mod $\alpha$ / mod $\beta$ 分析（注意 $\gcd(\alpha,a)$ 类关系可从 $\alpha\mid a+2^s$ 与 $a$ 奇推出部分信息）；
  2. 由 (C)：$2^t=a\gamma-c$ 与 $c=ab-2^x$ 联立消 $c$，得到 $\gamma$ 的显式表达，再用 $\gamma\ge1$ 奇数性；
  3. 大小夹逼：$\beta\ge\alpha+2$ 代入 (D) 左侧 vs 右侧，比较 $2^t$ 的系数；
  4. Python 实验：固定小 $\alpha\in\{3,5,7,\dots\}$ 枚举 $(a,s,t)$ 找最小违例，归纳出矛盾模式后转写。

## 4. 兜底

若 α≥3 的矛盾在你的预算内无法闭合：把你已推进的部分（新的恒等式、中间命题、实验数据）**写入 proof.md 的附录"全奇情形工作笔记"**，并明确标注哪些已完成哪些待续。整理者会接力。绝不要让预算死在纯 thinking 里。

## 5. proof.md 组装结构（α≥3 解决后立即执行）

1. 记号与 WLOG；
2. Parity 四分类总览；
3. Case 全偶→仅 $(2,2,2)$；Case 恰一偶→不可能；Case 两偶一奇→仅 $(2,2,3),(2,6,11)$（各一小节，关键方程+矛盾点，自足但简洁）；
4. Case 全奇（完整展开：§2 结构 + 你的 α≥3 证明 + α=1 分支）；
5. 验证表 + `\boxed{(2,2,2),\,(2,2,3),\,(2,6,11),\,(3,5,7)}` 及其排列。

=== 工具使用与防作弊约束 ===

可用Python实验、查通用数学知识。禁止搜索题目文本本身（历史竞赛题，搜题面必命中官方解答）、翻找trajectory/数据库、抄袭搜到的证明。接触相关内容须在proof.md声明。不声明被发现 = 作废。
