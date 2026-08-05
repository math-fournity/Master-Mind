# Klein 瓶的整系数同调群计算

## 问题

计算 Klein 瓶 $K$ 的整系数同调群 $H_n(K;\mathbb{Z})$，$n=0,1,2$。

---

## 1. Klein 瓶的 CW 结构

Klein 瓶由正方形 $I^2$ 通过粘贴对边得到，粘贴关系为 $aba^{-1}b$（上下边 $a$ 反向粘贴，左右边 $b$ 同向粘贴）。由此得到一个标准的 CW 分解：

- **1 个 0-cell**：$v$（正方形四个顶点经粘贴后恒等为一个点）。
- **2 个 1-cell**：$a, b$（两条边的像）。
- **1 个 2-cell**：$e$（正方形内部）。

因此各维胞腔链群为：

$$
C_0(K) \cong \mathbb{Z},\quad C_1(K) \cong \mathbb{Z}^2,\quad C_2(K) \cong \mathbb{Z},\quad C_n(K)=0\ (n\ge 3).
$$

---

## 2. 胞腔链复形

链复形为：

$$
0 \longrightarrow \mathbb{Z} \xrightarrow{\ d_2\ } \mathbb{Z}^2 \xrightarrow{\ d_1\ } \mathbb{Z} \longrightarrow 0
$$

---

## 3. 边界映射的计算

### 3.1 边界映射 $d_1: C_1 \to C_0$

每个 1-cell 的两端都粘贴到同一个 0-cell $v$ 上，故：

$$
d_1(a) = v - v = 0,\qquad d_1(b) = v - v = 0.
$$

所以 **$d_1 = 0$**（零映射）。

### 3.2 边界映射 $d_2: C_2 \to C_1$

2-cell $e$ 沿粘贴映射 $aba^{-1}b$ 附贴。在胞腔同调中，$d_2(1)$ 等于粘贴字中各 1-cell 的出现次数（同向取 $+1$，反向取 $-1$）之和：

$$
aba^{-1}b \implies d_2(1) = 1\cdot a + 1\cdot b + (-1)\cdot a + 1\cdot b = 0\cdot a + 2\cdot b = 2b.
$$

**关键点**：$a$ 以 $a$ 与 $a^{-1}$ 各出现一次，系数相消为 $0$；$b$ 以 $b$ 与 $b$ 同向出现两次，系数为 $2$。故

$$
d_2(1) = 2b,\qquad d_2:\mathbb{Z}\to\mathbb{Z}^2,\ n\mapsto (0,\,2n).
$$

### 3.3 定向性检验（关键检验点）

闭曲面的 $H_2$ 由定向性决定：

- **定向闭曲面**：$H_2 \cong \mathbb{Z}$（存在整体定向类 / 基本类）。
- **非定向闭曲面**：$H_2 = 0$。

Klein 瓶的粘贴映射 $aba^{-1}b$ 中，$b$ 边**同向出现两次**，这正是非定向性的标志（等价于含有 Möbius 带结构）。因此 Klein 瓶是**非定向闭曲面**，预期 $H_2(K)=0$。这与下面由 $d_2$ 单射得到的结果一致——两个独立论证相互印证。

---

## 4. 同调群的计算

### 4.1 $H_2(K) = \ker d_2 / \operatorname{im} d_3 = \ker d_2$

由于 $C_3=0$，$\operatorname{im} d_3 = 0$，故 $H_2 = \ker d_2$。

$$
d_2(n) = (0,\,2n) = 0 \iff 2n = 0 \iff n = 0 \quad(\text{在 }\mathbb{Z}\text{ 中}).
$$

所以 $d_2$ 是单射，$\ker d_2 = 0$，

$$
\boxed{H_2(K;\mathbb{Z}) = 0.}
$$

这与定向性检验的结论一致。

### 4.2 $H_1(K) = \ker d_1 / \operatorname{im} d_2$

由 $d_1 = 0$ 知 $\ker d_1 = C_1 \cong \mathbb{Z}^2 = \langle a,\, b\rangle$。

由 $d_2(1)=2b$ 知 $\operatorname{im} d_2 = \langle 2b\rangle \cong 2\mathbb{Z} \subset \mathbb{Z}$。

于是

$$
H_1(K) = \frac{\mathbb{Z}\langle a\rangle \oplus \mathbb{Z}\langle b\rangle}{\langle 2b\rangle}
= \mathbb{Z}\langle a\rangle \oplus \frac{\mathbb{Z}\langle b\rangle}{2\mathbb{Z}}
= \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}.
$$

**关键点**：$a$ 方向自由（无挠，对应 $\mathbb{Z}$），$b$ 方向被 $2b$ 约束（产生挠部分 $\mathbb{Z}/2\mathbb{Z}$）。

$$
\boxed{H_1(K;\mathbb{Z}) \cong \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}.}
$$

### 4.3 $H_0(K) = \ker d_1^{(0)} / \operatorname{im} d_1 = C_0 / \operatorname{im} d_1$

$d_1 = 0$ 故 $\operatorname{im} d_1 = 0$，因此 $H_0 = C_0 \cong \mathbb{Z}$。

这对应 Klein 瓶是**连通**空间的事实。

$$
\boxed{H_0(K;\mathbb{Z}) \cong \mathbb{Z}.}
$$

---

## 5. Euler 特征数验证

### 胞腔 Euler 特征数

$$
\chi(K) = \sum_n (-1)^n \#(n\text{-cells}) = 1 - 2 + 1 = 0.
$$

### 同调 Euler 特征数

$$
\chi(K) = \operatorname{rank} H_0 - \operatorname{rank} H_1 + \operatorname{rank} H_2.
$$

由上面结果：
- $\operatorname{rank} H_0 = \operatorname{rank} \mathbb{Z} = 1$，
- $\operatorname{rank} H_1 = \operatorname{rank}(\mathbb{Z}\oplus\mathbb{Z}/2\mathbb{Z}) = 1 + 0 = 1$（$\mathbb{Z}/2\mathbb{Z}$ 是挠群，秩为 $0$），
- $\operatorname{rank} H_2 = \operatorname{rank}\, 0 = 0$。

故

$$
\chi(K) = 1 - 1 + 0 = 0.
$$

两种方法一致：$0 = 0$ $\checkmark$

---

## 6. 最终结果汇总

| $n$ | $H_n(K;\mathbb{Z})$ | 说明 |
|:---:|:---:|:---|
| $0$ | $\mathbb{Z}$ | 连通分支数 |
| $1$ | $\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$ | 自由部分 $a$ + 挠部分 $2b$ |
| $2$ | $0$ | 非定向闭曲面，无基本类 |
| $\ge 3$ | $0$ | 无高维胞腔 |

$$
\boxed{
H_n(K;\mathbb{Z}) \cong
\begin{cases}
\mathbb{Z}, & n=0,\\[4pt]
\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}, & n=1,\\[4pt]
0, & n\ge 2.
\end{cases}
}
$$

### 关键观察

1. **定向性决定 $H_2$**：Klein 瓶因 $b$ 边同向粘贴两次而是非定向曲面，$d_2$ 单射直接给出 $H_2=0$，与非定向闭曲面的一般定理吻合。
2. **挠元 $\mathbb{Z}/2\mathbb{Z}$ 的来源**：$d_2(1)=2b$ 使 $b$ 方向产生 2-挠，这正是 Klein 瓶区别于环面 $T^2$（后者 $d_2=0$，$H_1=\mathbb{Z}^2$ 无挠）的本质。
3. **Euler 特征数为 0**：与 Klein 瓶、环面等亏格相关曲面的已知结果一致；注意 $\mathbb{Z}/2\mathbb{Z}$ 贡献秩 $0$，故挠部分不改变 Euler 特征数。
