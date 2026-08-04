# 实对称矩阵谱定理的完整证明

## 定理陈述

**谱定理（实对称矩阵）**：设 $A$ 是 $n \times n$ 实对称矩阵（即 $A^T = A$，且 $A$ 的元素均为实数），则：

1. **（实谱性）** $A$ 的所有特征值都是实数。
2. **（正交对角化）** $A$ 可对角化：存在正交矩阵 $Q$（即 $Q^T Q = I$），使得
$$Q^T A Q = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n),$$
其中 $\lambda_1, \lambda_2, \ldots, \lambda_n$ 是 $A$ 的特征值（均为实数）。

等价地，$A = Q \operatorname{diag}(\lambda_1, \ldots, \lambda_n) Q^T$，即 $A$ 可以被一组标准正交的特征向量表示。

---

## 证明的整体结构

本证明分为两大阶段：

- **第一阶段**：证明 $A$ 的所有特征值都是实数（定理第 1 部分）。
- **第二阶段**：证明 $A$ 可被正交矩阵对角化（定理第 2 部分），采用数学归纳法。

在第二阶段中，关键步骤是：**先用代数方法证明实对称矩阵至少存在一个实特征值和对应的实特征向量**，然后利用正交分解将问题从 $n$ 维降到 $n-1$ 维，对 $n$ 作数学归纳法。

> **思维模式调用说明**：本证明综合调用了材料中提取的若干 L2 层思维模式：
> - **L2-4（不变量思维）**：特征多项式是不变量，我们通过其复根与实系数的关系来锁定实特征值的存在性；迹和行列式作为不变量贯穿验证。
> - **L2-2（局部-全局思维）**：将 $n$ 维问题分解为"一个特征方向"（局部）与"其正交补空间"（局部），在局部上对 $n-1$ 维子问题求解，再粘合（直和）推出全局对角化。
> - **L2-3（恒等式构造）**：构造 $v^T A v = \lambda v^T v$ 这一恒等式，代入后"实谱性"自然得出。
> - **L2-1（多项式恒等式检验）**：利用实系数多项式的复根成对出现这一代数事实，以及特征多项式次数为奇数时必有实根的论证。

---

## 第一阶段：证明 $A$ 的所有特征值都是实数

### 步骤 1：将问题提升到复数域

虽然 $A$ 是实矩阵，但其特征值是特征多项式 $p(\lambda) = \det(\lambda I - A)$ 的根，而实系数多项式的根可能是复数。因此我们需要在复数域 $\mathbb{C}$ 上讨论特征值。

设 $\lambda \in \mathbb{C}$ 是 $A$ 的一个特征值，$v \in \mathbb{C}^n$ 是对应的特征向量（$v \neq 0$），即
$$A v = \lambda v. \quad (\star)$$

### 步骤 2：构造关键恒等式（调用 L2-3：恒等式构造）

对 $(\star)$ 两边左乘 $v^*$（$v^*$ 表示 $v$ 的共轭转置，即 $v^* = \bar{v}^{\,T}$），得：
$$v^* A v = \lambda \, v^* v. \quad (\star\star)$$

这是一个关键的恒等式。我们分别分析等式两边的性质。

### 步骤 3：分析左端 $v^* A v$ 的实数性

利用 $A$ 是实对称矩阵的性质（$A^T = A$ 且 $A$ 的元素为实数，故 $\bar{A} = A$，从而 $A^* = \bar{A}^{\,T} = A^T = A$，即 $A$ 也是 Hermite 矩阵），考虑 $v^* A v$ 的共轭：

$$\overline{v^* A v} = (v^* A v)^* = v^* A^* v = v^* A v.$$

这里第一个等号是因为 $v^* A v$ 是一个标量（$1 \times 1$ 矩阵），其共轭等于其 Hermite 转置；第二个等号利用了 $A^* = A$（$A$ 是 Hermite 的）。

因此 $v^* A v$ 是实数。

### 步骤 4：分析右端 $\lambda \, v^* v$ 并得出结论

$v^* v = \sum_{i=1}^{n} \bar{v}_i v_i = \sum_{i=1}^{n} |v_i|^2$ 是实数，且由于 $v \neq 0$，有 $v^* v > 0$。

由 $(\star\star)$，$\lambda \, v^* v = v^* A v$，左端为实数，右端 $v^* v > 0$ 为实数，因此
$$\lambda = \frac{v^* A v}{v^* v}$$
是实数。

### 步骤 5：结论

由于 $\lambda$ 是 $A$ 的任意一个特征值，我们证明了 $A$ 的所有特征值都是实数。

**第一阶段证毕。** $\blacksquare$

> **不变量思维（L2-4）的体现**：$v^* A v$ 和 $v^* v$ 都是在共轭转置下保持实数性的不变量。无论选择哪个特征向量 $v$，这个实数性都成立，这保证了特征值的实数性是一个与基选择无关的内蕴性质。

---

## 第二阶段：证明 $A$ 可被正交矩阵对角化

我们将对矩阵的阶数 $n$ 作数学归纳法。为此，需要先建立一个关键前提：**实对称矩阵至少存在一个实特征值和对应的实特征向量。**

### 前置引理：实对称矩阵至少存在一个实特征值和对应的实特征向量

**证明**：

由第一阶段，$A$ 的所有特征值都是实数。现在需要确认 $A$ 确实有特征值（即特征多项式在 $\mathbb{C}$ 上有根），并且对应的特征向量可以取为实向量。

**特征值的存在性**：$A$ 的特征多项式 $p(\lambda) = \det(\lambda I - A)$ 是 $n$ 次实系数多项式。由代数基本定理，$p(\lambda)$ 在 $\mathbb{C}$ 上恰有 $n$ 个根（计重数），因此 $A$ 至少有一个复特征值 $\lambda$。由第一阶段，$\lambda$ 是实数。

（此处也可给出一个纯实数域的论证：实系数奇数次多项式必有实根。当 $n$ 为奇数时，$p(\lambda)$ 是奇次多项式，故有实根。当 $n$ 为偶数时，可先通过其他方法降阶——但利用复数域和代数基本定理是最简洁的路径，且第一阶段的结论已经保证了所有复根都是实数。）

**实特征向量的存在性**：设 $\lambda$ 是 $A$ 的一个（实）特征值。方程 $(\lambda I - A) v = 0$ 是一个实系数齐次线性方程组，且 $\det(\lambda I - A) = 0$（因为 $\lambda$ 是特征值），故方程组有非零解。由于系数矩阵 $\lambda I - A$ 是实矩阵，其非零解可以取为**实向量** $v \in \mathbb{R}^n$。

**前置引理证毕。** $\blacksquare$

> **局部-全局思维（L2-2）的体现**：前置引理解决了"局部"问题——找到一个特征方向。归纳法的核心就是把全局问题分解为这一个方向和它的正交补，在正交补（局部）上对低维问题求解，再粘合为全局结论。

---

### 归纳法主体

**归纳命题 $P(n)$**：对任意 $n \times n$ 实对称矩阵 $A$，存在正交矩阵 $Q \in O(n)$，使得 $Q^T A Q$ 为对角矩阵。

#### 基础步骤：$n = 1$

$1 \times 1$ 矩阵 $A = [a]$（$a \in \mathbb{R}$）已经是对角矩阵。取 $Q = [1]$（$1 \times 1$ 单位矩阵，显然正交），则 $Q^T A Q = [a]$ 为对角矩阵。

$P(1)$ 成立。$\blacksquare$

#### 归纳步骤：假设 $P(1), P(2), \ldots, P(n-1)$ 成立，证明 $P(n)$

设 $A$ 是 $n \times n$ 实对称矩阵。

**步骤 A：取一个实特征向量并单位化**

由前置引理，$A$ 有一个实特征值 $\lambda_1$ 和对应的实特征向量 $u \in \mathbb{R}^n$（$u \neq 0$），满足
$$A u = \lambda_1 u.$$

将 $u$ 单位化：令 $q_1 = \dfrac{u}{\|u\|}$，则 $\|q_1\| = 1$，且
$$A q_1 = \lambda_1 q_1.$$

**步骤 B：扩充为正交基并构造正交矩阵**

以 $q_1$ 为第一个向量，利用 Gram-Schmidt 正交化过程，将 $q_1$ 扩充为 $\mathbb{R}^n$ 的一组标准正交基 $\{q_1, q_2, \ldots, q_n\}$。

令 $Q_0 = [q_1 \mid q_2 \mid \cdots \mid q_n]$（以 $q_i$ 为列的 $n \times n$ 矩阵），则 $Q_0$ 是正交矩阵：$Q_0^T Q_0 = I$。

**步骤 C：计算 $Q_0^T A Q_0$ 的结构**

考察 $Q_0^T A Q_0$ 的第一列。$Q_0^T A Q_0$ 的第 $j$ 行第 $1$ 列元素为 $q_j^T A q_1$。

- 当 $j = 1$ 时：$q_1^T A q_1 = q_1^T (\lambda_1 q_1) = \lambda_1 q_1^T q_1 = \lambda_1$。
- 当 $j \geq 2$ 时：$q_j^T A q_1 = q_j^T (\lambda_1 q_1) = \lambda_1 q_j^T q_1 = 0$（因为 $q_j \perp q_1$）。

因此 $Q_0^T A Q_0$ 的第一列为 $(\lambda_1, 0, \ldots, 0)^T$。

又因为 $A$ 是对称矩阵，$Q_0^T A Q_0$ 也是对称的（$(Q_0^T A Q_0)^T = Q_0^T A^T (Q_0^T)^T = Q_0^T A Q_0$）。对称矩阵的第一行等于第一列的转置，因此第一行也是 $(\lambda_1, 0, \ldots, 0)$。

于是 $Q_0^T A Q_0$ 具有如下分块形式：

$$Q_0^T A Q_0 = \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 \end{pmatrix},$$

其中 $\mathbf{0}$ 是 $(n-1) \times 1$ 零向量，$A_1$ 是 $(n-1) \times (n-1)$ 矩阵。

**步骤 D：验证 $A_1$ 是实对称矩阵**

$Q_0^T A Q_0$ 是实矩阵（$Q_0$ 和 $A$ 都是实矩阵），且是对称矩阵。由上述分块结构，$A_1$ 是 $Q_0^T A Q_0$ 的右下 $(n-1) \times (n-1)$ 子矩阵。

- **$A_1$ 是实矩阵**：因为 $Q_0^T A Q_0$ 是实矩阵，其子矩阵 $A_1$ 也是实矩阵。
- **$A_1$ 是对称矩阵**：由 $Q_0^T A Q_0$ 的对称性，
$$\begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 \end{pmatrix} = \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1^T \end{pmatrix},$$
比较右下分块得 $A_1 = A_1^T$，即 $A_1$ 对称。

因此 $A_1$ 是 $(n-1) \times (n-1)$ 实对称矩阵。

**步骤 E：对 $A_1$ 应用归纳假设**

由归纳假设 $P(n-1)$，存在 $(n-1) \times (n-1)$ 正交矩阵 $\tilde{Q}$，使得
$$\tilde{Q}^T A_1 \tilde{Q} = \operatorname{diag}(\lambda_2, \lambda_3, \ldots, \lambda_n).$$

**步骤 F：构造最终的正交矩阵 $Q$ 并完成对角化**

定义 $n \times n$ 矩阵
$$\hat{Q} = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & \tilde{Q} \end{pmatrix}.$$

验证 $\hat{Q}$ 是正交矩阵：

$$\hat{Q}^T \hat{Q} = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & \tilde{Q}^T \end{pmatrix} \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & \tilde{Q} \end{pmatrix} = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & \tilde{Q}^T \tilde{Q} \end{pmatrix} = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & I_{n-1} \end{pmatrix} = I_n.$$

令 $Q = Q_0 \hat{Q}$。由于 $Q_0$ 和 $\hat{Q}$ 都是正交矩阵，$Q$ 也是正交矩阵（正交矩阵的乘积仍是正交矩阵）。

现在计算 $Q^T A Q$：

$$Q^T A Q = (Q_0 \hat{Q})^T A (Q_0 \hat{Q}) = \hat{Q}^T (Q_0^T A Q_0) \hat{Q}.$$

代入 $Q_0^T A Q_0 = \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 \end{pmatrix}$：

$$Q^T A Q = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & \tilde{Q}^T \end{pmatrix} \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 \end{pmatrix} \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & \tilde{Q} \end{pmatrix}.$$

逐项相乘：

$$= \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & \tilde{Q}^T \end{pmatrix} \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 \tilde{Q} \end{pmatrix} = \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & \tilde{Q}^T A_1 \tilde{Q} \end{pmatrix} = \begin{pmatrix} \lambda_1 & & \\ & \lambda_2 & \\ & & \ddots & \\ & & & \lambda_n \end{pmatrix} = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n).$$

这正是我们需要的对角化形式。

#### 归纳步骤的几何解释

上述过程的几何含义是：

1. 找到 $A$ 的一个特征方向 $q_1$（步骤 A）。
2. 将全空间 $\mathbb{R}^n$ 分解为 $q_1$ 张成的一维子空间 $V_1$ 与其正交补 $V_1^\perp$（步骤 B）。
3. 在正交补 $V_1^\perp \cong \mathbb{R}^{n-1}$ 上，$A$ 的限制是一个 $(n-1) \times (n-1)$ 实对称矩阵 $A_1$（步骤 C-D）。
4. 对 $A_1$ 递归地对角化（步骤 E），最终把所有特征方向粘合起来（步骤 F）。

> **局部-全局思维（L2-2）的体现**：这正是"把问题分解到局部，在局部解决，再用粘合原理推出全局"的经典模式。$n$ 维问题被分解为一个特征方向（一维局部）和正交补（$n-1$ 维局部），归纳法把所有局部结果粘合为全局的正交对角化。

#### 归纳完成

由数学归纳法，$P(n)$ 对所有正整数 $n$ 成立。

**第二阶段证毕。** $\blacksquare$

---

## 补充：不同特征值对应的特征向量的正交性

作为谱定理的一个直接推论，我们补充证明一个重要性质，它在上述归纳法中隐含地被使用，也具有独立的价值。

**命题**：设 $A$ 是实对称矩阵，$\lambda_i \neq \lambda_j$ 是 $A$ 的两个不同特征值，$v_i$ 和 $v_j$ 分别是对应的特征向量，则 $v_i \perp v_j$。

**证明**：

由 $A v_i = \lambda_i v_i$ 和 $A v_j = \lambda_j v_j$，且 $A^T = A$：

$$\lambda_i \, v_i^T v_j = (\lambda_i v_i)^T v_j = (A v_i)^T v_j = v_i^T A^T v_j = v_i^T A v_j = v_i^T (\lambda_j v_j) = \lambda_j \, v_i^T v_j.$$

因此
$$(\lambda_i - \lambda_j) \, v_i^T v_j = 0.$$

由于 $\lambda_i \neq \lambda_j$，故 $\lambda_i - \lambda_j \neq 0$，从而 $v_i^T v_j = 0$，即 $v_i \perp v_j$。$\blacksquare$

> **不变量思维（L2-4）的体现**：这里 $v_i^T A v_j$ 可以通过两种方式计算——先左乘 $A$ 得 $\lambda_i v_i^T v_j$，或先右乘 $A$ 得 $\lambda_j v_i^T v_j$——两种方式必须给出同一个值（不变量），由此推出正交性。

---

## 完整证明的总结

### 证明结构一览

| 阶段 | 内容 | 关键工具 | 调用的 L2 思维模式 |
|------|------|---------|-------------------|
| 第一阶段 | 所有特征值为实数 | 共轭转置 + Hermite 性质 | L2-3（恒等式构造）、L2-4（不变量） |
| 前置引理 | 实特征值和实特征向量存在 | 代数基本定理 + 实系数方程组 | L2-1（多项式根的检验） |
| 归纳基础 | $n=1$ 平凡 | — | — |
| 归纳步骤 | 降维 + 粘合 | 正交分解 + 归纳假设 | L2-2（局部-全局） |
| 正交性推论 | 不同特征值特征向量正交 | 对称性 + 双重计算 | L2-4（不变量） |

### 关键数学事实链条

1. **$A$ 是实对称 $\Rightarrow$ $A$ 是 Hermite**（$A^* = A$）：因为 $A$ 的元素为实数（$\bar{A} = A$）且 $A^T = A$，所以 $A^* = \bar{A}^{\,T} = A^T = A$。

2. **Hermite 矩阵的 Rayleigh 商为实数**：$v^* A v / v^* v \in \mathbb{R}$，因为 $v^* A v = \overline{v^* A v}$（由 $A^* = A$）。

3. **实特征值对应实特征向量**：$\lambda I - A$ 是实矩阵且奇异，其零空间有实基。

4. **正交补上的限制仍对称**：$Q_0^T A Q_0$ 对称 $\Rightarrow$ 其右下子块 $A_1$ 对称。

5. **正交矩阵的乘积正交**：$Q_0, \hat{Q} \in O(n) \Rightarrow Q = Q_0 \hat{Q} \in O(n)$。

6. **归纳降维**：$n$ 维问题 $\to$ $1$ 维 + $(n-1)$ 维问题 $\to$ 对 $(n-1)$ 维递归。

### 最终结论

综上所述，对任意 $n \times n$ 实对称矩阵 $A$：

1. $A$ 的所有特征值都是实数。
2. 存在正交矩阵 $Q$，使得 $Q^T A Q = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$，其中 $\lambda_1, \ldots, \lambda_n$ 是 $A$ 的特征值（均为实数），$Q$ 的列向量是 $A$ 的一组标准正交的特征向量。

**谱定理证毕。** $\blacksquare$
