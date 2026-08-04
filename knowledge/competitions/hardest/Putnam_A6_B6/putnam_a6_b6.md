# Putnam竞赛 A6 与 B6 题目汇编

> 本文件收录Putnam数学竞赛中A6和B6（每场考试最难的两道题）的题目。
> 题目来源为MAA官方发布及Kedlaya Putnam Archive等公开资源。
> 部分题面经多源核对，标注了领域和难度（1-5，5为最难）。

---

## 2024

### Putnam 2024 A6
**题目**：Let $c_0, c_1, c_2, \ldots$ be the sequence defined so that $\frac{1-3x-\sqrt{1-14x+9x^2}}{4} = \sum_{k=0}^{\infty} c_k x^k$ for sufficiently small $x$. For a positive integer $n$, let $A$ be the $n \times n$ matrix with $(i,j)$-entry $c_{i+j-1}$ for $i,j \in \{1,\ldots,n\}$. Find the determinant of $A$.
**领域**：代数（矩阵/组合）
**难度**：4

### Putnam 2024 B6
**题目**：For a real number $a$, let $F_a(x) = \sum_{n \geq 1} \frac{n^a e^{2nx}}{n^2}$ for $0 \leq x < 1$. Find a real number $c$ such that $\lim_{x \to 1^-} F_a(x) e^{-1/(1-x)} = 0$ for all $a < c$, and $\lim_{x \to 1^-} F_a(x) e^{-1/(1-x)} = \infty$ for all $a > c$.
**领域**：分析
**难度**：5

---

## 2023

### Putnam 2023 A6
**题目**：Alice and Bob play a game in which they take turns choosing integers from 1 to $n$. Before any integers are chosen, Bob selects a goal of "odd" or "even". On the first turn, Alice chooses one of the $n$ integers. On the second turn, Bob chooses one of the remaining integers. They continue alternately choosing one of the integers that has not yet been chosen, until the $n$th turn, which is forced and ends the game. Bob wins if the parity of $|\{k : \text{the number } k \text{ was chosen on the } k\text{th turn}\}|$ matches his goal. For which values of $n$ does Bob have a winning strategy?
**领域**：组合（博弈）
**难度**：4

### Putnam 2023 B6
**题目**：Let $n$ be a positive integer. For $i$ and $j$ in $\{1, 2, \ldots, n\}$, let $s(i, j)$ be the number of pairs $(a, b)$ of nonnegative integers satisfying $ai + bj = n$. Let $S$ be the $n \times n$ matrix whose $(i, j)$ entry is $s(i, j)$. Compute the determinant of $S$.
**领域**：代数（矩阵/数论）
**难度**：5

---

## 2022

### Putnam 2022 A6
**题目**：Let $n$ be a positive integer. Determine, in terms of $n$, the largest integer $m$ with the following property: There exist real numbers $x_1, \ldots, x_{2n}$ with $-1 < x_1 < x_2 < \cdots < x_{2n} < 1$ such that the sum of the lengths of the $n$ intervals $[x_1^{2k-1}, x_2^{2k-1}], [x_3^{2k-1}, x_4^{2k-1}], \ldots, [x_{2n-1}^{2k-1}, x_{2n}^{2k-1}]$ is equal to 1 for all integers $k$ with $1 \leq k \leq m$.
**领域**：分析/代数
**难度**：5

### Putnam 2022 B6
**题目**：Find all continuous functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ such that $f(xf(y)) + f(yf(x)) = 1 + f(x+y)$ for all $x, y > 0$.
**领域**：分析（函数方程）
**难度**：4

---

## 2021

### Putnam 2021 A6
**题目**：Let $P(x)$ be a polynomial whose coefficients are all either 0 or 1. Suppose that $P(x)$ can be written as a product of two nonconstant polynomials with integer coefficients. Does it follow that $P(2)$ is a composite integer?
**领域**：代数（多项式/数论）
**难度**：4

### Putnam 2021 B6
**题目**：Given an ordered list of $3N$ real numbers, we can trim it to form a list of $N$ numbers as follows: We divide the list into $N$ groups of 3 consecutive numbers, and within each group, discard the highest and lowest numbers, keeping only the median. Consider generating a random number $X$ by the following procedure: Start with a list of $3^{2021}$ numbers, drawn independently and uniformly at random between 0 and 1. Then trim this list as defined above, leaving a list of $3^{2020}$ numbers. Then trim again repeatedly until just one number remains; let $X$ be this number. Let $\mu$ be the expected value of $|X - \frac{1}{2}|$. Show that $\mu \geq \frac{1}{4}\left(\frac{2}{3}\right)^{2021}$.
**领域**：分析/概率
**难度**：5

---

## 2020

### Putnam 2020 A6
**题目**：For a positive integer $N$, let $f_N(x)$ be the function defined by $f_N(x) = \sum_{n=0}^{N} \frac{N+1/2-n}{(N+1)(2n+1)} \sin((2n+1)x)$. Determine the smallest constant $M$ such that $f_N(x) \leq M$ for all $N$ and all real $x$.
**领域**：分析
**难度**：4

### Putnam 2020 B6
**题目**：Let $n$ be a positive integer. Prove that $\sum_{k=1}^{n} (-1)^{\lfloor k(\sqrt{2}-1)\rfloor} \geq 0$. (As usual, $\lfloor x \rfloor$ denotes the greatest integer less than or equal to $x$.)
**领域**：数论/组合
**难度**：5

---

## 2019

### Putnam 2019 A6
**题目**：Let $g$ be a real-valued function that is continuous on the closed interval $[0,1]$ and twice differentiable on the open interval $(0,1)$. Suppose that for some real number $r > 1$, $\lim_{x \to 0^+} g(x)/x^r = 0$. Prove that either $\lim_{x \to 0^+} g'(x) = 0$ or $\limsup_{x \to 0^+} x^r |g''(x)| = \infty$.
**领域**：分析
**难度**：5

### Putnam 2019 B6
**题目**：Let $\mathbb{Z}^n$ be the integer lattice in $\mathbb{R}^n$. Two points in $\mathbb{Z}^n$ are called neighbors if they differ by exactly 1 in one coordinate and are equal in all other coordinates. For which integers $n \geq 1$ does there exist a set of points $S \subset \mathbb{Z}^n$ satisfying the following two conditions? (1) If $p$ is in $S$, then none of the neighbors of $p$ is in $S$. (2) If $p \in \mathbb{Z}^n$ is not in $S$, then exactly one of the neighbors of $p$ is in $S$.
**领域**：组合/代数
**难度**：4

---

## 2018

### Putnam 2018 A6
**题目**：Suppose that $A, B, C$, and $D$ are distinct points, no three of which lie on a line, in the Euclidean plane. Show that if the squares of the lengths of the line segments $AB, AC, AD, BC, BD$, and $CD$ are rational numbers, then the quotient $\frac{\text{area}(\triangle ABC)}{\text{area}(\triangle ABD)}$ is a rational number.
**领域**：几何/代数
**难度**：4

### Putnam 2018 B6
**题目**：Let $S$ be the set of sequences of length 2018 whose terms are in the set $\{1, 2, 3, 4, 5, 6, 10\}$ and sum to 3860. Prove that the cardinality of $S$ is at most $\binom{3860}{20}$.
**领域**：组合
**难度**：5

---

## 2017

### Putnam 2017 A6
**题目**：The 30 edges of a regular icosahedron are distinguished by labeling them $1, 2, \ldots, 30$. How many different ways are there to paint each edge red, white, or blue such that each of the 20 triangular faces of the icosahedron has two edges of the same color and a third edge of a different color?
**领域**：组合
**难度**：4

### Putnam 2017 B6
**题目**：Find the number of ordered 64-tuples $(x_0, x_1, \ldots, x_{63})$ such that $x_0, x_1, \ldots, x_{63}$ are distinct elements of $\{1, 2, \ldots, 2017\}$ and $x_0 + x_1 + 2x_2 + 3x_3 + \cdots + 63x_{63}$ is divisible by 2017.
**领域**：组合/数论
**难度**：5

---

## 2016

### Putnam 2016 A6
**题目**：Find the smallest constant $C$ such that for every real polynomial $P(x)$ of degree 3 that has a root in the interval $[0,1]$, $\int_0^1 |P(x)|\,dx \leq C \max_{x \in [0,1]} |P(x)|$.
**领域**：分析
**难度**：4

### Putnam 2016 B6
**题目**：Evaluate $\sum_{k=1}^{\infty} \frac{(-1)^{k-1}}{k} \sum_{n=0}^{\infty} \frac{1}{k^{2n}+1}$.
**领域**：分析
**难度**：5

---

## 2015

### Putnam 2015 A6
**题目**：Let $n$ be a positive integer. Suppose that $A, B$, and $M$ are $n \times n$ matrices with real entries such that $AM = MB$, and such that $A$ and $B$ have the same characteristic polynomial. Prove that $\det(A - MX) = \det(B - XM)$ for every $n \times n$ matrix $X$ with real entries.
**领域**：代数（线性代数）
**难度**：4

### Putnam 2015 B6
**题目**：For each positive integer $k$, let $A(k)$ be the number of odd divisors of $k$ in the interval $[1, \sqrt{2k})$. Evaluate $\sum_{k=1}^{\infty} \frac{(-1)^{k-1} A(k)}{k}$.
**领域**：数论/分析
**难度**：5

---

## 2014

### Putnam 2014 A6
**题目**：Let $n$ be a positive integer. What is the largest $k$ for which there exist $n \times n$ matrices $M_1, \ldots, M_k$ and $N_1, \ldots, N_k$ with real entries such that for all $i$ and $j$, the matrix product $M_i N_j$ has a zero entry somewhere on its diagonal if and only if $i \neq j$?
**领域**：代数（线性代数/组合）
**难度**：5

### Putnam 2014 B6
**题目**：Let $f: [0,1] \to \mathbb{R}$ be a function for which there exists a constant $K > 0$ such that $|f(x) - f(y)| \leq K|x - y|$ for all $x, y \in [0,1]$. Suppose also that for each rational number $r \in [0,1]$, there exist integers $a$ and $b$ such that $f(r) = a + br\sqrt{2}$. Prove that there exist finitely many intervals $I_1, \ldots, I_n$ such that $f$ is a linear function on each $I_i$ and $[0,1] = \bigcup_{i=1}^n I_i$.
**领域**：分析
**难度**：5

---

## 2013

### Putnam 2013 B6
**题目**：Let $n \geq 1$ be an odd integer. Alice and Bob play the following game, taking alternating turns, with Alice playing first. The playing area consists of $n$ spaces, arranged in a line. Initially all spaces are empty. At each turn, a player either places a stone in an empty space, or removes a stone from a nonempty space $s$, places a stone in the nearest empty space to the left of $s$ (if such a space exists), and places a stone in the nearest empty space to the right of $s$ (if such a space exists). Furthermore, a move is permitted only if the resulting position has not occurred previously in the game. A player loses if he or she is unable to move. Assuming that both players play optimally throughout the game, what moves may Alice make on her first turn?
**领域**：组合（博弈）
**难度**：5

---

## 2012

### Putnam 2012 A6
**题目**：Let $f(x, y)$ be a continuous, real-valued function on $\mathbb{R}^2$. Suppose that, for every rectangular region $R$ of area 1, the double integral of $f(x, y)$ over $R$ equals 0. Must $f(x, y)$ be identically 0?
**领域**：分析
**难度**：4

### Putnam 2012 B6
**题目**：Let $p$ be an odd prime number such that $p \equiv 2 \pmod{3}$. Define a permutation $\pi$ of the residue classes modulo $p$ by $\pi(x) \equiv x^3 \pmod{p}$. Show that $\pi$ is an even permutation if and only if $p \equiv 3 \pmod{4}$.
**领域**：数论/代数
**难度**：5

---

## 2011

### Putnam 2011 A6
**题目**：Let $G$ be an abelian group with $n$ elements, and let $\{g_1 = e, g_2, \ldots, g_k\} \subset G$ be a (not necessarily minimal) set of distinct generators of $G$. A special die, which randomly selects one of the elements $g_1, g_2, \ldots, g_k$ with equal probability, is rolled $m$ times and the selected elements are multiplied to produce an element $g \in G$. Prove that there exists a real number $b \in (0, 1)$ such that $\lim_{m \to \infty} \frac{1}{b^{2m}} \sum_{x \in G} \left|\text{Prob}(g = x) - \frac{1}{n}\right|$ is positive and finite.
**领域**：代数/概率
**难度**：5

### Putnam 2011 B6
**题目**：Let $p$ be an odd prime. Show that for at least $(p+1)/2$ values of $n$ in $\{0, 1, 2, \ldots, p-1\}$, $\sum_{k=0}^{p-1} k! n^k$ is not divisible by $p$.
**领域**：数论
**难度**：5

---

## 2010

### Putnam 2010 A6
**题目**：Let $f: [0, \infty) \to \mathbb{R}$ be a strictly decreasing continuous function such that $\lim_{x \to \infty} f(x) = 0$. Prove that $\int_0^{\infty} \frac{f(x) - f(x+1)}{f(x)}\,dx$ diverges.
**领域**：分析
**难度**：4

### Putnam 2010 B6
**题目**：Let $A$ be an $n \times n$ matrix of real numbers for some $n \geq 1$. For each positive integer $k$, let $A^{[k]}$ be the matrix obtained by raising each entry to the $k$th power. Show that if $A^k = A^{[k]}$ for $k = 1, 2, \ldots, n+1$, then $A^k = A^{[k]}$ for all $k \geq 1$.
**领域**：代数（线性代数）
**难度**：5

---

## 2009

### Putnam 2009 A6
**题目**：Let $f: [0,1]^2 \to \mathbb{R}$ be a continuous function on the closed unit square such that $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ exist and are continuous on the interior $(0,1)^2$. Let $a = \int_0^1 f(0, y)\,dy$, $b = \int_0^1 f(1, y)\,dy$, $c = \int_0^1 f(x, 0)\,dx$, $d = \int_0^1 f(x, 1)\,dx$. Prove or disprove: There must be a point $(x_0, y_0)$ in $(0,1)^2$ such that $\frac{\partial f}{\partial x}(x_0, y_0) = b - a$ and $\frac{\partial f}{\partial y}(x_0, y_0) = d - c$.
**领域**：分析
**难度**：4

### Putnam 2009 B6
**题目**：Prove that for every positive integer $n$, there is a sequence of integers $a_0, a_1, \ldots, a_{2009}$ with $a_0 = 0$ and $a_{2009} = n$ such that each term after $a_0$ is either an earlier term plus $2^k$ for some nonnegative integer $k$, or of the form $b \bmod c$ for some earlier positive terms $b$ and $c$. [Here $b \bmod c$ denotes the remainder when $b$ is divided by $c$, so $0 \leq (b \bmod c) < c$.]
**领域**：组合/数论
**难度**：5

---

## 2008

### Putnam 2008 A6
**题目**：Prove that there exists a constant $c > 0$ such that in every nontrivial finite group $G$ there exists a sequence of length at most $c \log|G|$ with the property that each element of $G$ equals the product of some subsequence. (The elements of $G$ in the sequence are not required to be distinct. A subsequence is obtained by selecting some of the terms, not necessarily consecutive, without reordering them.)
**领域**：代数（群论/组合）
**难度**：5

### Putnam 2008 B6
**题目**：Let $n$ and $k$ be positive integers. Say that a permutation $\sigma$ of $\{1, 2, \ldots, n\}$ is $k$-limited if $|\sigma(i) - i| \leq k$ for all $i$. Prove that the number of $k$-limited permutations of $\{1, 2, \ldots, n\}$ is odd if and only if $n \equiv 0$ or $1 \pmod{2k+1}$.
**领域**：组合
**难度**：5

---

## 2007

### Putnam 2007 A6
**题目**：A triangulation $T$ of a polygon $P$ is a finite collection of triangles whose union is $P$, and such that the intersection of any two triangles is either empty, or a shared vertex, or a shared side. Moreover, each side of $P$ is a side of exactly one triangle in $T$. Say that $T$ is admissible if every internal vertex is shared by 6 or more triangles. Prove that there is an integer $M_n$, depending only on $n$, such that any admissible triangulation of a polygon $P$ with $n$ sides has at most $M_n$ triangles.
**领域**：几何/组合
**难度**：5

### Putnam 2007 B6
**题目**：For each positive integer $n$, let $f(n)$ be the number of ways to make $n!$ cents using an unordered collection of coins, each worth $k!$ cents for some $k$, $1 \leq k \leq n$. Prove that for some constant $C$, independent of $n$, $n^{n^2/2 - Cn} e^{-n^2/4} \leq f(n) \leq n^{n^2/2 + Cn} e^{-n^2/4}$.
**领域**：组合/分析
**难度**：5

---

## 2006

### Putnam 2006 A6
**题目**：Four points are chosen uniformly and independently at random in the interior of a given circle. Find the probability that they are the vertices of a convex quadrilateral.
**领域**：几何/概率
**难度**：4

### Putnam 2006 B6
**题目**：Let $k$ be an integer greater than 1. Suppose $a_0 > 0$, and define $a_{n+1} = a_n + \frac{1}{\sqrt[k]{a_n}}$ for $n \geq 0$. Evaluate $\lim_{n \to \infty} \frac{a_n^{k+1}}{n^k}$.
**领域**：分析
**难度**：4

---

## 2005

### Putnam 2005 A6
**题目**：Let $n$ be given, $n \geq 4$, and suppose that $P_1, P_2, \ldots, P_n$ are $n$ randomly, independently and uniformly, chosen points on a circle. Consider the convex $n$-gon whose vertices are the $P_i$. What is the probability that at least one of the vertex angles of this polygon is acute?
**领域**：几何/概率
**难度**：4

### Putnam 2005 B6
**题目**：Let $S_n$ denote the set of all permutations of the numbers $1, 2, \ldots, n$. For $\pi \in S_n$, let $\sigma(\pi) = 1$ if $\pi$ is an even permutation and $\sigma(\pi) = -1$ if $\pi$ is an odd permutation. Also, let $\nu(\pi)$ denote the number of fixed points of $\pi$. Show that $\sum_{\pi \in S_n} \frac{\sigma(\pi)}{\nu(\pi) + 1} = (-1)^{n+1} \frac{n}{n+1}$.
**领域**：组合
**难度**：5

---

## 2004

### Putnam 2004 A6
**题目**：Suppose that $f(x, y)$ is a continuous real-valued function on the unit square $0 \leq x \leq 1$, $0 \leq y \leq 1$. Show that $\int_0^1 \left(\int_0^1 f(x,y)\,dx\right)^2 dy + \int_0^1 \left(\int_0^1 f(x,y)\,dy\right)^2 dx \leq \left(\int_0^1 \int_0^1 f(x,y)\,dx\,dy\right)^2 + \int_0^1 \int_0^1 (f(x,y))^2\,dx\,dy$.
**领域**：分析（不等式）
**难度**：4

### Putnam 2004 B6
**题目**：Let $A$ be a non-empty set of positive integers, and let $N(x)$ denote the number of elements of $A$ not exceeding $x$. Let $B$ denote the set of positive integers $b$ that can be written in the form $b = a - a'$ with $a \in A$ and $a' \in A$. Let $b_1 < b_2 < \cdots$ be the members of $B$, listed in increasing order. Show that if the sequence $b_{i+1} - b_i$ is unbounded, then $\lim_{x \to \infty} N(x)/x = 0$.
**领域**：数论/分析
**难度**：5

---

## 2003

### Putnam 2003 A6
**题目**：For a set $S$ of nonnegative integers, let $r_S(n)$ denote the number of ordered pairs $(s_1, s_2)$ such that $s_1 \in S$, $s_2 \in S$, $s_1 \neq s_2$, and $s_1 + s_2 = n$. Is it possible to partition the nonnegative integers into two sets $A$ and $B$ in such a way that $r_A(n) = r_B(n)$ for all $n$?
**领域**：组合/数论
**难度**：4

### Putnam 2003 B6
**题目**：Let $f(x)$ be a continuous real-valued function defined on the interval $[0,1]$. Show that $\int_0^1 \int_0^1 |f(x) + f(y)|\,dx\,dy \geq \int_0^1 |f(x)|\,dx$.
**领域**：分析（不等式）
**难度**：4

---

## 2002

### Putnam 2002 A6
**题目**：Fix an integer $b \geq 2$. Let $f(1) = 1$, $f(2) = 2$, and for each $n \geq 3$, define $f(n) = n^{f(d)}$, where $d$ is the number of base-$b$ digits of $n$. For which values of $b$ does $\sum_{n=1}^{\infty} \frac{1}{f(n)}$ converge?
**领域**：分析/数论
**难度**：4

### Putnam 2002 B6
**题目**：Let $p$ be a prime number. Prove that the determinant of the matrix $\begin{pmatrix} x & y & z \\ x^p & y^p & z^p \\ x^{p^2} & y^{p^2} & z^{p^2} \end{pmatrix}$ is congruent modulo $p$ to a product of polynomials of the form $ax + by + cz$, where $a, b, c$ are integers. (We say two integer polynomials are congruent modulo $p$ if corresponding coefficients are congruent modulo $p$.)
**领域**：代数/数论
**难度**：5

---

## 2001

### Putnam 2001 A6
**题目**：Can an arc of a parabola inside a circle of radius 1 have a length greater than 4?
**领域**：几何/分析
**难度**：4

### Putnam 2001 B6
**题目**：Assume that $(a_n)_{n \geq 1}$ is an increasing sequence of positive real numbers such that $\lim a_n/n = 0$. Must there exist infinitely many positive integers $n$ such that $a_{n-i} + a_{n+i} < 2a_n$ for $i = 1, 2, \ldots, n-1$?
**领域**：分析
**难度**：5

---

## 2000

### Putnam 2000 A6
**题目**：Let $f(x)$ be a polynomial with integer coefficients. Define a sequence $a_0, a_1, \ldots$ of integers such that $a_0 = 0$ and $a_{n+1} = f(a_n)$ for $n \geq 0$. Prove that if there exists a positive integer $m$ for which $a_m = 0$, then either $a_1 = 0$ or $a_2 = 0$.
**领域**：代数/数论
**难度**：4

### Putnam 2000 B6
**题目**：Let $B$ be a set of more than $2^{n+1}/n$ distinct points with coordinates of the form $(\pm 1, \pm 1, \ldots, \pm 1)$ in $n$-dimensional space, with $n \geq 3$. Show that there are three distinct points in $B$ which are the vertices of an equilateral triangle.
**领域**：组合/几何
**难度**：5

---

## 1999

### Putnam 1999 A6
**题目**：The sequence $(a_n)_{n \geq 1}$ is defined by $a_1 = 1$, $a_2 = 2$, $a_3 = 24$, and, for $n \geq 4$, $a_n = \frac{6a_{n-1}^2 a_{n-3} - 8a_{n-1} a_{n-2}^2}{a_{n-2} a_{n-3}}$. Show that, for all $n$, $a_n$ is an integer multiple of $n$.
**领域**：代数/数论
**难度**：5

### Putnam 1999 B6
**题目**：Let $S$ be a finite set of integers, each greater than 1. Suppose that for each integer $n$ there is some $s \in S$ such that $\gcd(s, n) = 1$ or $\gcd(s, n) = s$. Show that there exist $s, t \in S$ such that $\gcd(s, t)$ is prime.
**领域**：数论
**难度**：5

---

## 1998

### Putnam 1998 A6
**题目**：Let $A, B, C$ denote distinct points with integer coordinates in $\mathbb{R}^2$. Prove that if $(|AB| + |BC|)^2 < 8 \cdot [ABC] + 1$, then $A, B, C$ are three vertices of a square. Here $|XY|$ is the length of segment $XY$ and $[ABC]$ is the area of triangle $ABC$.
**领域**：几何/数论
**难度**：4

### Putnam 1998 B6
**题目**：Prove that, for any integers $a, b, c$, there exists a positive integer $n$ such that $\sqrt{n^3 + an^2 + bn + c}$ is not an integer.
**领域**：数论
**难度**：4

---

## 1997

### Putnam 1997 A6
**题目**：For a positive integer $n$ and any real number $c$, define $x_k$ recursively by $x_0 = 0$, $x_1 = 1$, and for $k \geq 0$, $x_{k+2} = \frac{cx_{k+1} - (n-k)x_k}{k+1}$. Fix $n$ and then take $c$ to be the largest value for which $x_{n+1} = 0$. Find $x_k$ in terms of $n$ and $k$, $1 \leq k \leq n$.
**领域**：代数/分析
**难度**：4

### Putnam 1997 B6
**题目**：The dissection of the 3-4-5 triangle into four congruent right triangles similar to the original has diameter 5/2. Find the least diameter of a dissection of this triangle into four parts. (The diameter of a dissection is the least upper bound of the distances between pairs of points belonging to the same part.)
**领域**：几何
**难度**：5

---

## 1996

### Putnam 1996 A6
**题目**：Let $\mathbb{R}$ be the reals and $k$ a non-negative real. Find all continuous functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(x) = f(x^2 + k)$ for all $x$.
**领域**：分析（函数方程）
**难度**：4

### Putnam 1996 B6
**题目**：Let $(a_1, b_1), (a_2, b_2), \ldots, (a_n, b_n)$ be the vertices of a convex polygon which contains the origin in its interior. Prove that there exist positive real numbers $x$ and $y$ such that $\sum_{i=1}^{n} (a_i, b_i) x^{a_i} y^{b_i} = (0, 0)$.
**领域**：分析/代数
**难度**：5

---

## 1995

### Putnam 1995 A6
**题目**：Suppose that each of $n$ people writes down the numbers 1, 2, 3 in random order in one column of a $3 \times n$ matrix, with all orders equally likely and with the orders for different columns independent of each other. Let the row sums $a, b, c$ of the resulting matrix be rearranged (if necessary) so that $a \leq b \leq c$. Show that for some $n \geq 1995$, it is at least four times as likely that both $b = a+1$ and $c = a+2$ as that $a = b = c$.
**领域**：组合/概率
**难度**：5

### Putnam 1995 B6
**题目**：For a positive real number $\alpha$, define $S(\alpha) = \{\lfloor n\alpha \rfloor : n = 1, 2, 3, \ldots\}$. Prove that $\{1, 2, 3, \ldots\}$ cannot be expressed as the disjoint union of $S(\alpha)$, $S(\beta)$, and $S(\gamma)$ for any positive real numbers $\alpha, \beta, \gamma$.
**领域**：数论/组合
**难度**：5

---

## 1994

### Putnam 1994 A6
**题目**：Let $f_1, \ldots, f_{10}$ be bijections of the set of integers such that for each integer $n$, there is some composition $f_{i_1} \circ f_{i_2} \circ \cdots \circ f_{i_m}$ of these functions (allowing repetitions) which maps 0 to $n$. Consider the set of 1024 functions $F = \{f_1^{e_1} \circ f_2^{e_2} \circ \cdots \circ f_{10}^{e_{10}}\}$, $e_i = 0$ or 1 for $1 \leq i \leq 10$. ($f_i^0$ is the identity function and $f_i^1 = f_i$.) Show that if $A$ is any nonempty finite set of integers, then at most 512 of the functions in $F$ map $A$ to itself.
**领域**：代数/组合
**难度**：5

### Putnam 1994 B6
**题目**：For any integer $a$, set $n_a = 101^a - 100 \cdot 2^a$. Show that for $0 \leq a, b, c, d \leq 99$, $n_a + n_b \equiv n_c + n_d \pmod{10100}$ implies $\{a, b\} = \{c, d\}$.
**领域**：数论
**难度**：5

---

## 1993

### Putnam 1993 A6
**题目**：The infinite sequence of 2's and 3's $2, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 2, \ldots$ has the property that, if one forms a second sequence that records the number of 3's between successive 2's, the result is identical to the given sequence. Show that there exists a real number $r$ such that, for any $n$, the $n$th term of the sequence is 2 if and only if $n = 1 + \lfloor rm \rfloor$ for some nonnegative integer $m$.
**领域**：组合/数论
**难度**：5

### Putnam 1993 B6
**题目**：Let $S$ be a set of three, not necessarily distinct, positive integers. Show that one can transform $S$ into a set containing 0 by a finite number of applications of the following rule: Select two of the three integers, say $x$ and $y$, where $x \leq y$, and replace them with $2x$ and $y - x$.
**领域**：数论/组合
**难度**：5

---

## 1992

### Putnam 1992 A6
**题目**：Four points are chosen at random on the surface of a sphere. What is the probability that the center of the sphere lies inside the tetrahedron whose vertices are at the four points? (It is understood that each point is independently chosen relative to a uniform distribution on the sphere.)
**领域**：几何/概率
**难度**：3

### Putnam 1992 B6
**题目**：Let $M$ be a set of real $n \times n$ matrices such that (i) $I \in M$, where $I$ is the $n \times n$ identity matrix; (ii) if $A \in M$ and $B \in M$, then either $AB \in M$ or $-AB \in M$, but not both; (iii) if $A \in M$ and $B \in M$, then either $AB = BA$ or $AB = -BA$; (iv) if $A \in M$ and $A \neq I$, there is at least one $B \in M$ such that $AB = -BA$. Prove that $M$ contains at most $n^2$ matrices.
**领域**：代数（线性代数）
**难度**：5

---

## 1991

### Putnam 1991 A6
**题目**：Let $A(n)$ denote the number of sums of positive integers $a_1 + a_2 + \cdots + a_r$ which add up to $n$ with $a_1 > a_2 + a_3$, $a_2 > a_3 + a_4$, $\ldots$, $a_{r-2} > a_{r-1} + a_r$, $a_{r-1} > a_r$. Let $B(n)$ denote the number of $b_1 + b_2 + \cdots + b_s$ which add up to $n$, with (1) $b_1 \geq b_2 \geq \cdots \geq b_s$, (2) each $b_i$ is in the sequence $1, 2, 4, \ldots, g_j, \ldots$ defined by $g_1 = 1$, $g_2 = 2$, and $g_j = g_{j-1} + g_{j-2} + 1$, and (3) if $b_1 = g_k$ then every element in $\{1, 2, 4, \ldots, g_k\}$ appears at least once as a $b_i$. Prove that $A(n) = B(n)$ for each $n \geq 1$.
**领域**：组合
**难度**：5

### Putnam 1991 B6
**题目**：Let $a$ and $b$ be positive numbers. Find the largest number $c$, in terms of $a$ and $b$, such that $a^\alpha b^{1-\alpha} \leq a \frac{\sinh(\alpha x)}{\sinh x} + b \frac{\sinh(x(1-\alpha))}{\sinh x}$ for all $x$ with $0 < |x| \leq c$ and for all $\alpha$ with $0 < \alpha < 1$.
**领域**：分析（不等式）
**难度**：5

---

## 1990

### Putnam 1990 A6
**题目**：How many ordered pairs $(A, B)$ of subsets of $\{1, 2, \ldots, 10\}$ can we find such that each element of $A$ is larger than $|B|$ and each element of $B$ is larger than $|A|$?
**领域**：组合
**难度**：4

### Putnam 1990 B6
**题目**：Let $S$ be a nonempty closed bounded convex set in the plane. Let $K$ be a line and $t$ a positive number. Let $L_1$ and $L_2$ be support lines for $S$ parallel to $K$, and let $L$ be the line parallel to $K$ and midway between $L_1$ and $L_2$. Let $B_S(K, t)$ be the band of points whose distance from $L$ is at most $(t/2)w$, where $w$ is the distance between $L_1$ and $L_2$. What is the smallest $t$ such that $S \cap \bigcap_K B_S(K, t) \neq \emptyset$ for all $S$? ($K$ runs over all lines in the plane.)
**领域**：几何/分析
**难度**：5

---

## 1989

### Putnam 1989 A6
**题目**：Let $\alpha = 1 + a_1 x + a_2 x^2 + \cdots$ be a formal power series with coefficients in the field of two elements. Let $a_n = 1$ if every block of zeros in the binary expansion of $n$ has an even number of zeros in the block, and $a_n = 0$ otherwise. Prove that $\alpha^3 + x\alpha + 1 = 0$.
**领域**：代数/组合
**难度**：5

### Putnam 1989 B6
**题目**：Let $(x_1, x_2, \ldots, x_n)$ be a point chosen at random from the $n$-dimensional region defined by $0 < x_1 < x_2 < \cdots < x_n < 1$. Let $f$ be a continuous function on $[0,1]$ with $f(1) = 0$. Set $x_0 = 0$ and $x_{n+1} = 1$. Show that the expected value of the Riemann sum $\sum_{i=0}^{n} (x_{i+1} - x_i) f(x_{i+1})$ is $\int_0^1 f(t) P(t)\,dt$, where $P$ is a polynomial of degree $n$, independent of $f$, with $0 \leq P(t) \leq 1$ for $0 \leq t \leq 1$.
**领域**：分析/概率
**难度**：4

---

## 1988

### Putnam 1988 A6
**题目**：If a linear transformation $A$ on an $n$-dimensional vector space has $n+1$ eigenvectors such that any $n$ of them are linearly independent, does it follow that $A$ is a scalar multiple of the identity? Prove your answer.
**领域**：代数（线性代数）
**难度**：3

### Putnam 1988 B6
**题目**：Prove that there exist an infinite number of ordered pairs $(a, b)$ of integers such that for every positive integer $t$, the number $at + b$ is a triangular number if and only if $t$ is a triangular number. (The triangular numbers are the $t_n = n(n+1)/2$ with $n$ in $\{0, 1, 2, \ldots\}$.)
**领域**：数论
**难度**：5

---

## 1987

### Putnam 1987 A6
**题目**：For each positive integer $n$, let $a(n)$ be the number of zeros in the base 3 representation of $n$. For which positive real numbers $x$ does the series $\sum_{n=1}^{\infty} \frac{x^{a(n)}}{n^3}$ converge?
**领域**：分析/数论
**难度**：4

### Putnam 1987 B6
**题目**：Let $F$ be the field of $p^2$ elements, where $p$ is an odd prime. Suppose $S$ is a set of $(p^2 - 1)/2$ distinct nonzero elements of $F$ with the property that for each $a \neq 0$ in $F$, exactly one of $a$ and $-a$ is in $S$. Let $N$ be the number of elements in the intersection $S \cap \{2a : a \in S\}$. Prove that $N$ is even.
**领域**：代数（有限域）
**难度**：5

---

## 1986

### Putnam 1986 A6
**题目**：Let $a_1, a_2, \ldots, a_n$ be real numbers, and let $b_1, b_2, \ldots, b_n$ be distinct positive integers. Suppose that there is a polynomial $f(x)$ satisfying the identity $(1-x)^n f(x) = 1 + \sum_{i=1}^{n} a_i x^{b_i}$. Find a simple expression (not involving any sums) for $f(1)$ in terms of $b_1, b_2, \ldots, b_n$ and $n$ (but independent of $a_1, a_2, \ldots, a_n$).
**领域**：代数（多项式）
**难度**：5

### Putnam 1986 B6
**题目**：Suppose $A, B, C, D$ are $n \times n$ matrices with entries in a field $F$, satisfying the conditions that $AB^T$ and $CD^T$ are symmetric and $AD^T - BC^T = I$. Here $I$ is the $n \times n$ identity matrix, and if $M$ is an $n \times n$ matrix, $M^T$ is its transpose. Prove that $A^T D - C^T B = I$.
**领域**：代数（线性代数）
**难度**：4

---

## 1985

### Putnam 1985 A6
**题目**：If $p(x) = a_0 + a_1 x + \cdots + a_m x^m$ is a polynomial with real coefficients $a_i$, then set $\Gamma(p(x)) = a_0^2 + a_1^2 + \cdots + a_m^2$. Let $F(x) = 3x^2 + 7x + 2$. Find, with proof, a polynomial $g(x)$ with real coefficients such that (i) $g(0) = 1$, and (ii) $\Gamma(F(x)^n) = \Gamma(g(x)^n)$ for every positive integer $n$.
**领域**：代数（多项式）
**难度**：4

### Putnam 1985 B6
**题目**：Let $G$ be a finite set of real $n \times n$ matrices $\{M_i\}$, $1 \leq i \leq r$, which form a group under matrix multiplication. Suppose that $\sum_{i=1}^{r} \text{tr}(M_i) = 0$, where $\text{tr}(A)$ denotes the trace of the matrix $A$. Prove that $\sum_{i=1}^{r} M_i$ is the $n \times n$ zero matrix.
**领域**：代数（群论/线性代数）
**难度**：5

---

## 1979

### Putnam 1979 A6
**题目**：Let $0 \leq p_i \leq 1$ for $i = 1, 2, \ldots, n$. Show that $\sum_{i=1}^{n} \frac{1}{|x - p_i|} \leq 8n\left(1 + \frac{1}{3} + \frac{1}{5} + \cdots + \frac{1}{2n-1}\right)$ for some $x$ satisfying $0 \leq x \leq 1$.
**领域**：分析（不等式）
**难度**：5

---

## 1978

### Putnam 1978 A6
**题目**：Given $n$ points in the plane, prove that less than $2n^{3/2}$ pairs of points are a distance 1 apart.
**领域**：组合/几何
**难度**：4

### Putnam 1978 B6
**题目**：Let $a_{ij}$ be reals in $[0, 1]$. Show that $\left(\sum_{i=1}^{n} \sum_{j=1}^{m_i} \frac{a_{ij}}{i}\right)^2 \leq 2m \sum_{i=1}^{n} \sum_{j=1}^{m_i} a_{ij}$.
**领域**：分析（不等式）
**难度**：4

---

## 1976

### Putnam 1976 A6
**题目**：Let $f: \mathbb{R} \to [-1, 1]$ be twice differentiable and $f(0)^2 + f'(0)^2 = 4$. Show that $f(x_0) + f''(x_0) = 0$ for some $x_0$.
**领域**：分析
**难度**：4

### Putnam 1976 B6
**题目**：Let $\sigma(n)$ be the sum of all positive divisors of $n$, including 1 and $n$. Show that if $\sigma(n) = 2n + 1$, then $n$ is the square of an odd integer.
**领域**：数论
**难度**：5

---

## 1966

### Putnam 1966 A6
**题目**：Let $a_n = \sqrt{1 + 2\sqrt{1 + 3\sqrt{1 + 4\sqrt{1 + 5\sqrt{\cdots + (n-1)\sqrt{1+n}\cdots}}}}}$. Prove $\lim a_n = 3$.
**领域**：分析
**难度**：4

### Putnam 1966 B6
**题目**：$y = f(x)$ is a solution of $y'' + e^x y = 0$. Prove that $f(x)$ is bounded.
**领域**：分析（微分方程）
**难度**：4

---

## 备注

- 以上题目来自MAA官方发布及Kedlaya Putnam Archive (kskedlaya.org/putnam-archive/) 等公开资源。
- A6和B6是Putnam考试每场（A部分和B部分）的最后一题，通常为全场最难的题目。
- 据统计（1974-2016数据），前200名选手无人得到正分的题目包括1979年A6和2011年B6，被认为是历史上最难的Putnam题目之一。
- 部分年份的A6或B6因题面核对不确定而跳过（如2013年A6等）。
- 难度标注为相对估计，仅供参考。
