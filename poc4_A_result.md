# Klein瓶的整系数同调群计算

## 1. CW结构

Klein瓶 $K$ 由正方形将其对边按词 $w = aba^{-1}b$ 粘贴得到。由此可得极简CW结构：

| 维度 | 胞腔数量 | 具体胞腔 |
|------|---------|---------|
| 0-cell | 1 | $v$（正方形四个顶点粘贴后重合为一个点） |
| 1-cell | 2 | $a$（一对对边），$b$（另一对对边） |
| 2-cell | 1 | $e^2$（正方形内部） |

粘贴过程：
- **1-skeleton**：将两条线段 $a$、$b$ 的端点都粘贴到唯一顶点 $v$ 上，得到 wedge of two circles $S^1_a \vee S^1_b$。
- **2-cell**：将正方形 $e^2$ 的边界沿词 $w = a\, b\, a^{-1}\, b$ 映射到1-skeleton上。注意 $b$ 出现两次且方向相同（这是非定向曲面的特征），$a$ 出现一次正向、一次反向。

## 2. 胞腔链复形

胞腔链复形为：

$$
0 \longrightarrow C_2(K) \xrightarrow{\ d_2\ } C_1(K) \xrightarrow{\ d_1\ } C_0(K) \longrightarrow 0
$$

其中各链群为自由Abel群：

$$
C_2(K) \cong \mathbb{Z}\langle e^2 \rangle, \qquad C_1(K) \cong \mathbb{Z}\langle a \rangle \oplus \mathbb{Z}\langle b \rangle \cong \mathbb{Z}^2, \qquad C_0(K) \cong \mathbb{Z}\langle v \rangle \cong \mathbb{Z}
$$

完整链复形图示：

$$
0 \longrightarrow \mathbb{Z} \xrightarrow{\ d_2\ } \mathbb{Z}^2 \xrightarrow{\ d_1\ } \mathbb{Z} \longrightarrow 0
$$

## 3. 边界映射的计算

### 3.1 计算 $d_1: C_1(K) \to C_0(K)$

1-cell $a$ 的两个端点都粘贴到同一个顶点 $v$，同理 1-cell $b$ 的两个端点也粘贴到 $v$。因此：

$$
d_1(a) = v - v = 0, \qquad d_1(b) = v - v = 0
$$

$$
\boxed{d_1 = 0 \quad (\text{零映射})}
$$

### 3.2 计算 $d_2: C_2(K) \to C_1(K)$

2-cell的粘贴映射由词 $w = a\, b\, a^{-1}\, b$ 给出。胞腔边界映射的公式为：将2-cell $e^2$ 映射到其在各1-cell上出现的**代数重数**之和。

逐项分析词 $w = a\, b\, a^{-1}\, b$：

| 项 | 1-cell | 贡献符号 |
|----|--------|---------|
| $a$ | $a$ | $+a$ |
| $b$ | $b$ | $+b$ |
| $a^{-1}$ | $a$ | $-a$ |
| $b$ | $b$ | $+b$ |

求和：

$$
d_2(e^2) = (+1)\,a + (+1)\,b + (-1)\,a + (+1)\,b = (1-1)\,a + (1+1)\,b = 0 \cdot a + 2 \cdot b
$$

$$
\boxed{d_2(e^2) = 2b}
$$

即在基 $\{a, b\}$ 下，$d_2: \mathbb{Z} \to \mathbb{Z}^2$ 的矩阵表示为：

$$
d_2 = \begin{pmatrix} 0 \\ 2 \end{pmatrix}, \qquad d_2(n) = (0,\; 2n)
$$

**直观理解**：$a$ 在粘贴词中正反各出现一次，互相抵消（定向相消）；$b$ 两次同向出现，故系数为 $2$（这正是Klein瓶非定向性的代数体现）。

## 4. 同调群的计算

同调群定义为 $H_n(K) = \ker(d_n) / \operatorname{im}(d_{n+1})$。

### 4.1 $H_0(K;\mathbb{Z})$

$$
H_0(K) = \ker(d_0) / \operatorname{im}(d_1)
$$

- $d_0: C_0 \to 0$ 是到零群的映射，故 $\ker(d_0) = C_0 = \mathbb{Z}$。
- $d_1 = 0$，故 $\operatorname{im}(d_1) = 0$。

$$
H_0(K;\mathbb{Z}) = \mathbb{Z} / 0 \cong \mathbb{Z}
$$

$$
\boxed{H_0(K;\mathbb{Z}) \cong \mathbb{Z}}
$$

**意义**：Klein瓶是道路连通的，故 $H_0 \cong \mathbb{Z}$，与一般结论一致。

### 4.2 $H_1(K;\mathbb{Z})$

$$
H_1(K) = \ker(d_1) / \operatorname{im}(d_2)
$$

- $d_1 = 0$，故 $\ker(d_1) = C_1 = \mathbb{Z}^2$。
- $\operatorname{im}(d_2) = \langle 2b \rangle = \{(0, 2n) : n \in \mathbb{Z}\} = 0 \oplus 2\mathbb{Z} \subset \mathbb{Z} \oplus \mathbb{Z}$。

因此：

$$
H_1(K;\mathbb{Z}) = \frac{\mathbb{Z}\langle a \rangle \oplus \mathbb{Z}\langle b \rangle}{\mathbb{Z}\langle 2b \rangle} = \mathbb{Z}\langle a \rangle \oplus \frac{\mathbb{Z}\langle b \rangle}{2\mathbb{Z}} = \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}
$$

$$
\boxed{H_1(K;\mathbb{Z}) \cong \mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}}
$$

**结构分析**：
- $\mathbb{Z}$ 分量由 1-cycle $a$ 生成（$a$ 是一个"自由"的1-cycle，不被任何2-chain的边界所限制）。
- $\mathbb{Z}/2\mathbb{Z}$ 分量由 $b$ 生成（$b$ 本身是1-cycle，但 $2b = d_2(e^2)$ 是2-cell的边界，故 $b$ 的阶为2）。

**扭群 $\text{Tor} \cong \mathbb{Z}/2\mathbb{Z}$ 的存在**正是Klein瓶**非定向性**的直接代数证据。相比之下，定向曲面（如环面 $T^2$）的 $H_1$ 是自由Abel群，不含扭元素。

### 4.3 $H_2(K;\mathbb{Z})$

$$
H_2(K) = \ker(d_2) / \operatorname{im}(d_3)
$$

- 不存在3-cell，故 $C_3 = 0$，$\operatorname{im}(d_3) = 0$。
- $\ker(d_2) = \{n \in \mathbb{Z} : d_2(n) = (0, 2n) = (0,0)\} = \{n \in \mathbb{Z} : 2n = 0\} = \{0\}$。

$$
H_2(K;\mathbb{Z}) = 0 / 0 = 0
$$

$$
\boxed{H_2(K;\mathbb{Z}) = 0}
$$

**意义**：$H_2 = 0$ 意味Klein瓶上不存在"整体2-cycle"，即不存在非平凡的闭2-链。这与Klein瓶的**非定向性**一致——非定向闭曲面的整系数 $H_2$ 恒为零（不存在整体相容的定向）。

## 5. Euler特征数验证

### 5.1 由CW结构计算

$$
\chi(K) = \sum_{n=0}^{2} (-1)^n \, \text{rank}\, C_n(K) = 1 - 2 + 1 = 0
$$

### 5.2 由同调群验证

利用同调群的秩（Betti数）$\beta_n = \text{rank}\, H_n$：

$$
\beta_0 = \text{rank}(\mathbb{Z}) = 1
$$
$$
\beta_1 = \text{rank}(\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}) = 1 + 0 = 1
$$
$$
\beta_2 = \text{rank}(0) = 0
$$

$$
\chi(K) = \beta_0 - \beta_1 + \beta_2 = 1 - 1 + 0 = 0
$$

**两种方法结果一致：$\chi(K) = 0$。** ✓

> 注：Euler特征数只依赖Betti数（秩），不涉及扭群。$\mathbb{Z}/2\mathbb{Z}$ 扭项不影响Euler特征数的值，因此扭群的存在不影响此验证的成立。

## 6. 结果总结

| $n$ | $H_n(K;\mathbb{Z})$ | 说明 |
|-----|---------------------|------|
| 0 | $\mathbb{Z}$ | 道路连通 |
| 1 | $\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$ | 自由部分$\mathbb{Z}$由$a$生成，扭部分$\mathbb{Z}/2\mathbb{Z}$由$b$生成 |
| 2 | $0$ | 非定向曲面无整体定向，$H_2=0$ |
| $\geq 3$ | $0$ | 无高维胞腔 |

### 与环面 $T^2$ 的对比

| | 环面 $T^2$（定向） | Klein瓶 $K$（非定向） |
|--|-------------------|---------------------|
| 粘贴词 | $aba^{-1}b^{-1}$ | $aba^{-1}b$ |
| $d_2$ | $e^2 \mapsto a+b-a-b = 0$ | $e^2 \mapsto a+b-a+b = 2b$ |
| $H_1$ | $\mathbb{Z}^2$（无扭） | $\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$（有扭） |
| $H_2$ | $\mathbb{Z}$ | $0$ |
| $\chi$ | $0$ | $0$ |

两者的Euler特征数相同（均为0），但同调群结构截然不同：Klein瓶的 $H_1$ 含有2-扭群，$H_2$ 为零，这完全由粘贴词中 $b$ 的两次同向出现所决定。
