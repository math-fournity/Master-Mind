# 实对称矩阵的谱定理 · 完整证明

## 定理陈述

**谱定理（实对称矩阵）**：设 $A$ 是 $n \times n$ 实对称矩阵（即 $A = A^T$，且 $A$ 的元素均为实数），则：

1. $A$ 的所有特征值都是实数；
2. $A$ 可正交对角化：存在正交矩阵 $Q$（即 $Q^T Q = I$），使得
$$Q^T A Q = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n),$$
其中 $\lambda_1, \lambda_2, \ldots, \lambda_n$ 是 $A$ 的特征值（均为实数）。

---

## 第一部分：实对称矩阵的特征值均为实数

### 证明思路

我们要证明：若 $A$ 是实对称矩阵，$\lambda$ 是 $A$ 的特征值（按定义，特征值是特征多项式 $\det(\lambda I - A) = 0$ 的根，可能在复数域中），则 $\lambda \in \mathbb{R}$。

核心方法是：将 $A$ 视为复矩阵（实矩阵自然是复矩阵的特例），利用复数域上的特征值-特征向量关系，结合 $A$ 的对称性（$A = A^T$，注意不是 $A = \bar{A}^T$，但因为 $A$ 是实矩阵，所以 $A^T = \bar{A}^T = A^*$），通过共轭运算推出 $\lambda = \bar{\lambda}$。

### 详细证明

**步骤 1：特征值的存在性**

首先，$A$ 的特征多项式 $p(\lambda) = \det(\lambda I - A)$ 是关于 $\lambda$ 的 $n$ 次实系数多项式（因为 $A$ 的元素是实数，行列式展开后系数均为实数）。由代数基本定理（Fundamental Theorem of Algebra），$n$ 次复系数多项式在复数域 $\mathbb{C}$ 上恰有 $n$ 个根（计重数）。因此，$A$ 在复数域上至少有一个特征值 $\lambda$（实际上恰有 $n$ 个，计重数）。

设 $\lambda \in \mathbb{C}$ 是 $A$ 的一个特征值，我们需要证明 $\lambda \in \mathbb{R}$。

**步骤 2：取对应的复特征向量**

因为 $\lambda$ 是 $A$ 的特征值，所以 $\lambda I - A$ 是奇异矩阵（$\det(\lambda I - A) = 0$），从而齐次线性方程组
$$(\lambda I - A)v = 0$$
有非零解。即存在非零向量 $v \in \mathbb{C}^n$（注意：即使 $A$ 是实矩阵，当 $\lambda$ 是复数时，特征向量 $v$ 一般也是复向量），使得
$$Av = \lambda v. \quad \quad (1)$$

**步骤 3：对等式 (1) 两边取共轭**

对 $v$ 取复共轭，记 $\bar{v}$（即对 $v$ 的每个分量取复共轭）。对等式 (1) 两边取复共轭：
$$\overline{Av} = \overline{\lambda v}$$

由于 $A$ 是实矩阵（$A$ 的每个元素 $a_{ij} \in \mathbb{R}$，所以 $\bar{a}_{ij} = a_{ij}$，即 $\bar{A} = A$），有：
$$A\bar{v} = \bar{\lambda}\bar{v}. \quad \quad (2)$$

这说明 $\bar{\lambda}$ 也是 $A$ 的特征值，对应的特征向量为 $\bar{v}$。

**步骤 4：利用对称性导出关键等式**

对等式 (1) 左乘 $\bar{v}^T$（即 $\bar{v}$ 的转置，这是一个 $1 \times n$ 行向量）：
$$\bar{v}^T A v = \bar{v}^T (\lambda v) = \lambda (\bar{v}^T v). \quad \quad (3)$$

对等式 (2) 左乘 $v^T$：
$$v^T A \bar{v} = v^T (\bar{\lambda} \bar{v}) = \bar{\lambda}(v^T \bar{v}). \quad \quad (4)$$

现在观察等式 (3) 的左端 $\bar{v}^T A v$ 和等式 (4) 的左端 $v^T A \bar{v}$。因为它们都是标量（$1 \times 1$ 矩阵），所以：

$$(\bar{v}^T A v)^T = v^T A^T \bar{v}.$$

而 $A$ 是对称矩阵，$A^T = A$，所以：
$$(\bar{v}^T A v)^T = v^T A \bar{v}.$$

标量的转置等于自身，所以 $\bar{v}^T A v = (\bar{v}^T A v)^T = v^T A \bar{v}$，即：
$$\bar{v}^T A v = v^T A \bar{v}. \quad \quad (5)$$

**步骤 5：比较等式 (3) 和 (4)**

由 (3) 和 (4)：
$$\lambda(\bar{v}^T v) = \bar{v}^T A v = v^T A \bar{v} = \bar{\lambda}(v^T \bar{v}).$$

注意 $\bar{v}^T v = v^T \bar{v}$（都是 $\sum_{i=1}^n |v_i|^2$，是同一个标量），因此：
$$\lambda(\bar{v}^T v) = \bar{\lambda}(\bar{v}^T v).$$

**步骤 6：得出结论**

因为 $v \neq 0$（$v$ 是特征向量，非零），所以
$$\bar{v}^T v = \sum_{i=1}^n \bar{v}_i v_i = \sum_{i=1}^n |v_i|^2 > 0.$$

因此可以从等式两边约去 $\bar{v}^T v \neq 0$，得到：
$$\lambda = \bar{\lambda}.$$

一个复数等于其共轭，当且仅当它是实数。因此 $\lambda \in \mathbb{R}$。

**结论**：$A$ 的每一个特征值都是实数。$\blacksquare$

---

## 第二部分：实对称矩阵可正交对角化

### 证明思路

我们需要证明存在正交矩阵 $Q$ 使得 $Q^T A Q$ 为对角矩阵。证明采用**数学归纳法**，对矩阵的阶数 $n$ 进行归纳。核心步骤是：

1. **基例**：$n = 1$ 时显然成立。
2. **归纳步骤**：假设结论对所有 $k \times k$（$k < n$）实对称矩阵成立。对 $n \times n$ 实对称矩阵 $A$：
   - 由第一部分，$A$ 有实特征值 $\lambda_1$ 和对应的实特征向量 $v_1$；
   - 将 $v_1$ 单位化，并扩充为一组标准正交基 $\{v_1, w_2, \ldots, w_n\}$；
   - 在这组基下，$A$ 变为准对角形式 $\begin{pmatrix} \lambda_1 & 0 \\ 0 & A_1 \end{pmatrix}$，其中 $A_1$ 是 $(n-1) \times (n-1)$ 实对称矩阵；
   - 对 $A_1$ 应用归纳假设，完成证明。

### 详细证明

**对 $n$ 进行数学归纳法。**

#### 基例：$n = 1$

当 $n = 1$ 时，$A = (a)$ 是 $1 \times 1$ 实对称矩阵（$a \in \mathbb{R}$）。取 $Q = (1)$（$1 \times 1$ 单位矩阵，显然是正交矩阵），则 $Q^T A Q = (a) = \operatorname{diag}(a)$，结论成立。

#### 归纳假设

假设对于所有 $k \times k$（$1 \leq k < n$）实对称矩阵，结论成立，即存在 $k \times k$ 正交矩阵 $P$ 使得 $P^T B P = \operatorname{diag}(\mu_1, \ldots, \mu_k)$。

#### 归纳步骤：证明 $n \times n$ 实对称矩阵的情形

设 $A$ 是 $n \times n$ 实对称矩阵。

**步骤 1：取一个实特征值和对应的实特征向量**

由第一部分已证，$A$ 的所有特征值都是实数。设 $\lambda_1$ 是 $A$ 的一个特征值（$\lambda_1 \in \mathbb{R}$），对应的特征向量 $u \in \mathbb{C}^n$ 满足 $Au = \lambda_1 u$。

我们需要说明可以取到**实**特征向量。因为 $\lambda_1 \in \mathbb{R}$ 且 $A$ 是实矩阵，方程组 $(\lambda_1 I - A)x = 0$ 是实系数齐次线性方程组。该方程组有非零复解 $u$，将 $u$ 写成 $u = u_R + i u_I$（$u_R, u_I \in \mathbb{R}^n$ 分别为实部和虚部），代入方程：
$$(\lambda_1 I - A)(u_R + i u_I) = 0,$$
分开实部和虚部：
$$(\lambda_1 I - A)u_R = 0, \quad (\lambda_1 I - A)u_I = 0.$$
因为 $u \neq 0$，所以 $u_R$ 和 $u_I$ 不全为零。取其中非零者，即得到 $\lambda_1$ 的非零实特征向量。记其为 $v_1 \in \mathbb{R}^n$，则
$$Av_1 = \lambda_1 v_1, \quad v_1 \neq 0, \quad v_1 \in \mathbb{R}^n.$$

**步骤 2：将 $v_1$ 单位化**

令 $q_1 = \dfrac{v_1}{\|v_1\|}$，则 $\|q_1\| = 1$，且 $Aq_1 = \lambda_1 q_1$。

**步骤 3：将 $q_1$ 扩充为 $\mathbb{R}^n$ 的一组标准正交基**

由 Gram-Schmidt 正交化过程（或直接引用线性代数基本定理：任意非零向量可扩充为一组标准正交基），存在向量 $q_2, q_3, \ldots, q_n \in \mathbb{R}^n$，使得 $\{q_1, q_2, \ldots, q_n\}$ 构成 $\mathbb{R}^n$ 的一组标准正交基，即
$$q_i^T q_j = \delta_{ij} = \begin{cases} 1, & i = j, \\ 0, & i \neq j. \end{cases}$$

**步骤 4：构造正交矩阵 $Q_1$ 并考察 $Q_1^T A Q_1$ 的结构**

令 $Q_1 = (q_1 \mid q_2 \mid \cdots \mid q_n)$，即以 $q_1, q_2, \ldots, q_n$ 为列向量构成的 $n \times n$ 矩阵。由于列向量标准正交，$Q_1$ 是正交矩阵：$Q_1^T Q_1 = I$，从而 $Q_1^{-1} = Q_1^T$。

考察 $Q_1^T A Q_1$。其第 $(i, j)$ 元素为 $q_i^T A q_j$。

- **第 1 列**：$Q_1^T A Q_1$ 的第 1 列为 $Q_1^T A q_1 = Q_1^T (\lambda_1 q_1) = \lambda_1 Q_1^T q_1$。

  而 $Q_1^T q_1$ 的第 $i$ 个分量为 $q_i^T q_1 = \delta_{i1}$，所以 $Q_1^T q_1 = e_1 = (1, 0, \ldots, 0)^T$。

  因此 $Q_1^T A Q_1$ 的第 1 列为 $\lambda_1 e_1 = (\lambda_1, 0, \ldots, 0)^T$。

- **第 1 行**：$Q_1^T A Q_1$ 的第 $(1, j)$ 元素为 $q_1^T A q_j$。由于 $A$ 是对称矩阵：
  $$q_1^T A q_j = (Aq_1)^T q_j = (\lambda_1 q_1)^T q_j = \lambda_1 q_1^T q_j = \lambda_1 \delta_{1j}.$$
  所以第 1 行为 $(\lambda_1, 0, \ldots, 0)$。

综合以上，$Q_1^T A Q_1$ 具有以下分块形式：
$$Q_1^T A Q_1 = \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 \end{pmatrix},$$

其中 $\mathbf{0}$ 是 $(n-1) \times 1$ 零向量，$A_1$ 是 $(n-1) \times (n-1)$ 矩阵。

**步骤 5：验证 $A_1$ 是实对称矩阵**

$A_1$ 是实矩阵（因为 $Q_1$ 和 $A$ 都是实矩阵，$Q_1^T A Q_1$ 是实矩阵，其右下角子块 $A_1$ 也是实矩阵）。

$A_1$ 的对称性：因为 $Q_1^T A Q_1$ 是对称矩阵（$(Q_1^T A Q_1)^T = Q_1^T A^T (Q_1^T)^T = Q_1^T A Q_1$，用到 $A^T = A$），所以其右下角子块 $A_1$ 也是对称矩阵：$A_1^T = A_1$。

**步骤 6：对 $A_1$ 应用归纳假设**

$A_1$ 是 $(n-1) \times (n-1)$ 实对称矩阵。由归纳假设，存在 $(n-1) \times (n-1)$ 正交矩阵 $P$，使得
$$P^T A_1 P = \operatorname{diag}(\lambda_2, \lambda_3, \ldots, \lambda_n).$$

**步骤 7：构造 $n \times n$ 正交矩阵完成对角化**

定义 $n \times n$ 矩阵：
$$Q_2 = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & P \end{pmatrix},$$

其中左上角是 $1 \times 1$ 单位矩阵，$\mathbf{0}$ 是适当维度的零向量或零矩阵。

验证 $Q_2$ 是正交矩阵：
$$Q_2^T Q_2 = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & P^T \end{pmatrix} \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & P \end{pmatrix} = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & P^T P \end{pmatrix} = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & I_{n-1} \end{pmatrix} = I_n.$$

**步骤 8：计算 $Q_2^T (Q_1^T A Q_1) Q_2$**

令 $Q = Q_1 Q_2$（两个正交矩阵的乘积仍是正交矩阵：$Q^T Q = Q_2^T Q_1^T Q_1 Q_2 = Q_2^T I Q_2 = I$），则：

$$Q^T A Q = (Q_1 Q_2)^T A (Q_1 Q_2) = Q_2^T (Q_1^T A Q_1) Q_2.$$

代入 $Q_1^T A Q_1 = \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 \end{pmatrix}$ 和 $Q_2 = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & P \end{pmatrix}$：

$$Q^T A Q = \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & P^T \end{pmatrix} \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 \end{pmatrix} \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & P \end{pmatrix}.$$

先计算后两个矩阵的乘积：
$$\begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 \end{pmatrix} \begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & P \end{pmatrix} = \begin{pmatrix} \lambda_1 \cdot 1 + \mathbf{0}^T \cdot \mathbf{0} & \lambda_1 \cdot \mathbf{0}^T + \mathbf{0}^T \cdot P \\ \mathbf{0} \cdot 1 + A_1 \cdot \mathbf{0} & \mathbf{0} \cdot \mathbf{0}^T + A_1 P \end{pmatrix} = \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 P \end{pmatrix}.$$

再左乘 $Q_2^T$：
$$\begin{pmatrix} 1 & \mathbf{0}^T \\ \mathbf{0} & P^T \end{pmatrix} \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & A_1 P \end{pmatrix} = \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & P^T A_1 P \end{pmatrix} = \begin{pmatrix} \lambda_1 & \mathbf{0}^T \\ \mathbf{0} & \operatorname{diag}(\lambda_2, \ldots, \lambda_n) \end{pmatrix}.$$

因此：
$$Q^T A Q = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n).$$

**步骤 9：归纳完成**

由数学归纳法原理，对所有 $n \geq 1$，任意 $n \times n$ 实对称矩阵 $A$ 都存在正交矩阵 $Q$ 使得 $Q^T A Q = \operatorname{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$。$\blacksquare$

---

## 补充说明

### 1. 特征值的几何意义

谱定理告诉我们，实对称矩阵 $A$ 的作用可以分解为：在正交矩阵 $Q$ 的列向量 $\{q_1, q_2, \ldots, q_n\}$ 张成的方向上，$A$ 仅仅是伸缩变换——沿 $q_i$ 方向伸缩 $\lambda_i$ 倍。即：
$$A = Q \operatorname{diag}(\lambda_1, \ldots, \lambda_n) Q^T = \sum_{i=1}^n \lambda_i q_i q_i^T.$$

这称为 $A$ 的**谱分解**（spectral decomposition）。每个 $q_i q_i^T$ 是到 $q_i$ 方向的正交投影矩阵。

### 2. 为什么对称性是关键

在证明中，对称性 $A = A^T$ 在两处起到了决定性作用：

- **第一部分（特征值为实数）**：步骤 4 中，$\bar{v}^T A v = v^T A^T \bar{v} = v^T A \bar{v}$ 用到了 $A^T = A$。若 $A$ 不对称，则 $\bar{v}^T A v \neq v^T A \bar{v}$，无法推出 $\lambda = \bar{\lambda}$。例如，实矩阵 $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ 的特征值为 $\pm i$，不是实数——它不是对称矩阵。

- **第二部分（正交对角化）**：步骤 4 中，$Q_1^T A Q_1$ 的对称性（从而 $A_1$ 的对称性）依赖于 $A^T = A$。若 $A$ 不对称，$A_1$ 也不对称，归纳假设无法应用。例如，$\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ 虽然特征值为实数 1 和 2，但它不可对角化为正交矩阵的对角形式——它不是对称矩阵。

### 3. 正交对角化与一般对角化的区别

一般地，一个 $n \times n$ 矩阵可对角化（存在可逆矩阵 $P$ 使 $P^{-1}AP$ 为对角矩阵）当且仅当它有 $n$ 个线性无关的特征向量。而谱定理保证的是更强的结论：对于实对称矩阵，不仅可对角化，而且可**正交**对角化——变换矩阵 $Q$ 可以取为正交矩阵（$Q^{-1} = Q^T$），这意味着特征向量不仅线性无关，而且可以选为**标准正交**的。

### 4. 不同特征值对应特征向量的正交性

作为谱定理的推论，若 $\lambda_i \neq \lambda_j$ 是 $A$ 的两个不同特征值，对应的特征向量 $q_i, q_j$ 必正交。证明如下：

$$\lambda_i (q_i^T q_j) = (\lambda_i q_i)^T q_j = (Aq_i)^T q_j = q_i^T A^T q_j = q_i^T A q_j = q_i^T (\lambda_j q_j) = \lambda_j (q_i^T q_j).$$

因此 $(\lambda_i - \lambda_j)(q_i^T q_j) = 0$。若 $\lambda_i \neq \lambda_j$，则 $q_i^T q_j = 0$，即 $q_i \perp q_j$。

对于重特征值，其特征空间中可以选取标准正交基（因为同一特征空间中的特征向量加上其他特征空间的特征向量，总可以通过 Gram-Schmidt 正交化），这正是归纳证明中步骤 3 所保证的。

---

## 证毕

综上，我们完整证明了实对称矩阵的谱定理：

1. **特征值为实数**：通过复共轭运算与对称性，证明 $\lambda = \bar{\lambda}$，即所有特征值均为实数。

2. **正交对角化**：通过对矩阵阶数 $n$ 的数学归纳法，利用"实特征值 → 实特征向量 → 扩充为标准正交基 → 分块降阶 → 归纳假设"的递推路径，证明存在正交矩阵 $Q$ 使 $Q^T A Q$ 为对角矩阵。$\blacksquare$
