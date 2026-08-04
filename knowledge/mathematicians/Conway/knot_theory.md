# Conway 的纽结理论工作

> John Conway 对纽结理论（knot theory）做出了奠基性贡献。他发明的**Conway 纽结记法（tangle notation）**和**Conway 多项式**至今仍是纽结理论的核心工具。此外，Conway-Gordon 定理是图论与纽结理论交叉的重要结果。

---

## 1. Conway 纽结记法（Tangle Notation）

### 1.1 背景

纽结理论中，一个核心挑战是**如何系统地描述和分类纽结**。在 Conway 之前，纽结的描述主要依赖 Reidemeister 的纽结表（通过移动操作分类），缺乏代数化的系统方法。

### 1.2 Tangle 的概念

**Tangle（缠结）**：纽结图的一部分，包含在一个球内，球面上有4个标记点（NW, NE, SW, SE），弦从这些点进入球内并相互缠绕。

Conway 的核心创新：将纽结分解为**tangle 的组合**，用代数运算描述 tangle 的拼接。

### 1.3 基本 tangle

Conway 定义了以下基本 tangle：

| 记号 | 名称 | 描述 |
|------|------|------|
| $0$ | 零 tangle | 两条不相交的水平弦（无缠绕） |
| $1$ | 一 tangle | 两条交叉的弦（正向交叉） |
| $-1$ | 负一 tangle | 两条交叉的弦（负向交叉） |
| $\infty$ | 无穷 tangle | 两条不相交的竖直弦 |

### 1.4 Tangle 运算

Conway 定义了三种 tangle 运算：

1. **和（Sum, $+$）**：将两个 tangle $A$ 和 $B$ 水平拼接（$A$ 在左，$B$ 在右），连接相邻的端点。
   $$A + B$$

2. **积（Product, $\cdot$）**：将两个 tangle 竖直拼接（$A$ 在上，$B$ 在下）。
   $$A \cdot B \quad \text{（等价于 } A + \infty + B \text{ 的某种变体）}$$

3. **括号（Parenthesis, $,$）**：将 tangle 的对角端点连接（NW-SE 和 NE-SW），形成一个新的 tangle 或闭曲线。
   $$A, B \quad \text{（连接 } A \text{ 和 } B \text{ 的对角端点）}$$

### 1.5 Conway 记法的表示力

**关键洞察**：所有（有理）tangle 都可以通过基本 tangle $0, 1, -1, \infty$ 和运算 $+, \cdot, ,$ 递归构造。

**有理 tangle（Rational Tangle）**：通过 $0, 1, -1$ 和 $+, \cdot$ 构造的 tangle。每个有理 tangle 对应一个**有理数** $p/q$（其 fraction），且两个有理 tangle 等价当且仅当它们的 fraction 相等（Conway 的有理 tangle 定理，后被 Goldman 严格证明）。

**有理纽结（Rational Knot / 2-bridge knot）**：通过闭合有理 tangle 得到的纽结。Conway 记法给出了 2-bridge 纽结的完整分类。

### 1.6 例子

- $3$ = $1 + 1 + 1$（三个正交叉）→ fraction $3/1$ → 三叶结（trefoil）的某种表示；
- $2\,2$ = $(1+1),(1+1)$ → fraction $2/2 = 1/1$ → 与 $1$ 等价（Hopf 链的某种表示）；
- $2\,1\,2$ → 对应更复杂的 2-bridge 纽结。

### 1.7 Conway 的纽结表

Conway 利用 tangle 记法系统编制了**纽结表**，将纽结按交叉数排列。他的表（发表于1970年）纠正了之前 Reidemeister 和 Alexander-Briggs 表中的若干错误，并扩展到更高交叉数。

特别地，Conway 发现了**11个交叉数11的纽结**（之前未被列出），其中著名的 **Conway 纽结（Conway knot）**——交叉数11的纽结 $11n34$——后来成为纽结理论中的重要测试案例。

---

## 2. Conway 多项式

### 2.1 定义

**Conway 多项式** $\nabla_K(z)$（也称 Conway-Alexander 多项式）是纽结 $K$ 的一个**纽结不变量**，满足以下公理：

1. **规范性**：$\nabla_{\text{unknot}}(z) = 1$；
2. **Conway 关系（skein relation）**：对于在同一交叉点处仅交叉方向不同的三个链环 $L_+, L_-, L_0$：
   $$\nabla_{L_+}(z) - \nabla_{L_-}(z) = z \cdot \nabla_{L_0}(z).$$

### 2.2 与 Alexander 多项式的关系

Conway 多项式是 **Alexander 多项式** $\Delta_K(t)$ 的规范化形式。具体关系：
$$\nabla_K(z) = \Delta_K(t), \quad \text{其中 } z = t^{1/2} - t^{-1/2}.$$

即 $\nabla_K(t^{1/2} - t^{-1/2}) = \Delta_K(t)$。

**Conway 的贡献**：Conway 将 Alexander 多项式重新表述为满足 skein relation 的形式，这大大简化了计算，并揭示了多项式的**局部性质**（通过改变一个交叉点来递归计算）。

### 2.3 Skein 关系的意义

Conway 的 skein relation 是纽结理论中最重要的工具之一：

$$\nabla_{L_+} - \nabla_{L_-} = z \cdot \nabla_{L_0}$$

其中：
- $L_+$：交叉点为正向；
- $L_-$：交叉点为负向；
- $L_0$：交叉点被"解开"（smoothed）。

**意义**：skein relation 将纽结不变量的计算**局部化**——只需改变一个交叉点，就能递归地计算整个纽结的不变量。这一思想后来被推广到：
- **Jones 多项式**（1984）：$V_{L_+} - V_{L_-} = t \cdot V_{L_0}$（不同变量）；
- **HOMFLY 多项式**（1985）：$a \cdot P_{L_+} - a^{-1} \cdot P_{L_-} = z \cdot P_{L_0}$（统一了 Conway 和 Jones）；
- **Kauffman 多项式**。

**Conway 的 skein relation 是所有后续纽结多项式不变量的范式**。

### 2.4 性质

- **Conway 多项式的系数是整数**；
- **符号交替性**：对于纽结（非链环），$\nabla_K(z) = a_0 + a_2 z^2 + a_4 z^4 + \cdots$（只有偶数次项）；
- **Conway 多项式是 genus 的下界**：$|\nabla_K(z)|$ 的 $z$ 的次数 $\leq 2 \cdot \text{genus}(K)$；
- **符号差（signature）**：Conway 多项式在 $z = i$ 处的值给出纽结的符号差。

---

## 3. Conway-Gordon 定理

### 3.1 背景

Conway-Gordon 定理（1970年代）是**图论与纽结理论交叉**的里程碑结果，属于**空间图（spatial graph）**理论。

### 3.2 定理陈述

**Conway-Gordon 定理**：

> 对于 $K_7$（7个顶点的完全图）的任何**空间嵌入**（将顶点映射到 $\mathbb{R}^3$ 中的点，边映射为不相交的弧），其所有 Hamiltonian 圈的 linking number 的平方和满足：
> $$\sum_{\text{Hamiltonian cycles } C} \text{lk}(C)^2 \equiv 1 \pmod{2}.$$
>
> 特别地，$K_7$ 的任何空间嵌入中，至少有一对 Hamiltonian 圈的 linking number 为奇数（即它们非平凡地链接）。

类似地，对于 $K_6$：

> $K_6$ 的任何空间嵌入中，至少有一对不相交的三角形（3-圈）形成非平凡链接。

### 3.3 意义

1. **内在纽结性（Intrinsic Knotting）**：Conway-Gordon 定理证明了 $K_7$ 是**内在纽结的（intrinsically knotted）**——无论怎样嵌入 $\mathbb{R}^3$，总有一个 Hamiltonian 圈形成非平凡纽结。类似地，$K_6$ 是**内在链接的（intrinsically linked）**。

2. **图论与纽结理论的桥梁**：这是首次将纯图论性质（完全图的嵌入）与纽结/链接的拓扑性质（非平凡性）联系起来。

3. **后续发展**：
   - **Robertson-Seymour-Thomas（1995）**：分类了所有内在链接的图（与 Petersen 族图相关）；
   - 内在纽结图的研究成为活跃领域。

### 3.4 证明思路

Conway-Gordon 定理的证明基于：
1. 计算 $K_7$ 中 Hamiltonian 圈的数量（$7!/2 = 2520$ 个，但模 2 后简化）；
2. 利用 linking number 在 crossing change 下的变化性质；
3. 从标准嵌入（所有边为直线段）出发，通过连续变形论证不变性。

---

## 4. Conway 在纽结理论中的其他贡献

### 4.1 Conway 的 tangle 与 DNA 重组

Conway 的 tangle 理论后来被应用于**DNA 重组拓扑**：
- DNA 重组酶的作用可以建模为 tangle 操作；
- **Ernst-Sumners（1990）** 利用 tangle 理论分析了 DNA 重组的拓扑机制；
- Conway 的 tangle 运算恰好对应于 DNA 重组的"位点特异性重组"操作。

### 4.2 Conway 与纽结的幻灯片

Conway 制作了著名的**纽结幻灯片（knot slides）**，用直观的视觉方式展示纽结理论的核心概念。这些幻灯片在数学教育中广泛使用，极大地推广了纽结理论。

### 4.3 Conway 对纽结表的影响

Conway 的纽结表（1970）是20世纪最重要的纽结分类工作之一：
- 纠正了之前表中的错误；
- 引入了 tangle 记法作为系统工具；
- 扩展了纽结表到更高交叉数；
- 发现了新的纽结类型（如 Conway 纽结）。

---

## 5. Conway 纽结（Conway Knot）的故事

**Conway 纽结**（$11n34$）是交叉数11的纽结，由 Conway 在编制纽结表时发现。

**Slice 性问题**：Conway 纽结是否是 slice 的（即是否是某个 $\mathbb{R}^4$ 中圆盘的边界）？这个问题长期未解决。

**2020年突破**：**Lisa Piccirillo**（当时是UT Austin的博士生）在论文"The Conway knot is not slice"中证明了 Conway 纽结**不是 slice 的**。这一结果引起了广泛关注，Piccirillo 因此获得了2021年的 NSF Career Award等多个荣誉，并成为MIT的助理教授。

Piccirillo 的证明使用了 **Rasmussen s-不变量**和**trace surgery**技术，展示了现代纽结理论的强大工具。

---

## 参考文献

- Conway. *An Enumeration of Knots and Links, and Some of Their Algebraic Properties*. Computational Problems in Abstract Algebra, 1970.
- Conway, Gordon. *Knots and Links in Spatial Graphs*. J. Graph Theory, 1983.
- Goldman, Kauffman. *Rational tangles*. 1997.
- Ernst, Sumners. *A calculus for rational tangles: applications to DNA recombination*. Math. Proc. Camb. Phil. Soc., 1990.
- Piccirillo. *The Conway knot is not slice*. Annals of Mathematics, 2020.
- Robertson, Seymour, Thomas. *Sachs' linkless embedding conjecture*. J. Combin. Theory Ser. B, 1995.
