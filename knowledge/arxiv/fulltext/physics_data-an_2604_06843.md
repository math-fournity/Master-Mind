# Fast and accurate noise removal by curve fitting using orthogonal polynomials

**arXiv ID**: 2604.06843v1
**Authors**: Andrea Gallo Rosso
**Published**: 2026-04-08
**Categories**: physics.data-an, math.NA
**HTML URL**: https://arxiv.org/html/2604.06843v1

## Abstract

Local polynomial smoothing is a widespread technique in data analysis, and Savitzky-Golay (SG) filters are one of its most well-known realizations. In real settings, the effectiveness of SG filtering depends critically on proper tuning of its parameters, constrained in turn by repeated polynomial fitting over large data windows and for varying polynomial degrees. Standard implementations based on monomial bases and Vandermonde matrix formulations are known to suffer from ill-conditioning and unfavorable scaling as the problem size increases. In this work, we present a fast and numerically stable method for computing polynomial fitting and differentiation matrices by reformulating the problem in terms of discrete orthogonal (Chebyshev) polynomials. Exploiting their recursive structure and the intrinsic symmetry properties of the resulting matrices, we derive two algorithms designed to reduce computational overhead. Both methods significantly reduce memory usage and improve scalability with respect to the polynomial degree and window length. A discussion of the performance demonstrates that the proposed algorithms achieve orders-of-magnitude improvements in numerical accuracy compared to standard matrix multiplication, while also providing potential gains in execution time for large-scale problems. These features make the approach particularly well suited for applications requiring repeated local polynomial fits, such as the optimization of SG filters in high-resolution spectral analyses, including axion dark matter searches and the ALPHA haloscope.

## Full Text

Fast and accurate noise removal by curve fitting using orthogonal polynomials

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2604.06843v1 [physics.data-an] 08 Apr 2026

## Fast and accurate noise removal by curve fitting using orthogonal polynomialsAndreaGallo Rossoandrea.gallo.rosso@fysik.su.se.Physics Department and Oskar Klein Centre,
Stockholm University, Stockholm, Sweden

## Abstract

Local polynomial smoothing is a widespread technique in data analysis, and Savitzky–Golay (SG) filters are one of its most well-known realizations. In real settings, the effectiveness of SG filtering depends critically on proper tuning of its parameters, constrained in turn by repeated polynomial fitting over large data windows and for varying polynomial degrees. Standard implementations based on monomial bases and Vandermonde matrix formulations are known to suffer from ill-conditioning and unfavorable scaling as the problem size increases.
In this work, we present a fast and numerically stable method for computing polynomial fitting and differentiation matrices by reformulating the problem in terms of discrete orthogonal (Chebyshev) polynomials. Exploiting their recursive structure and the intrinsic symmetry properties of the resulting matrices, we derive two algorithms designed to reduce computational overhead. Both methods significantly reduce memory usage and improve scalability with respect to the polynomial degree and window length.
A discussion of the performance demonstrates that the proposed algorithms achieve orders-of-magnitude improvements in numerical accuracy compared to standard matrix multiplication, while also providing potential gains in execution time for large-scale problems. These features make the approach particularly well suited for applications requiring repeated local polynomial fits, such as the optimization of SG filters in high-resolution spectral analyses, including axion dark matter searches and the ALPHA haloscope.

## 1Introduction

Curve fitting is a fundamental and omnipresent technique in any scientific discipline facing data analysis. Even in basic practices, parametric functions are crucial for representing observed data, extract meaningful features, and facilitate subsequent inference or prediction[[, e.g.]]bruce2020, grus2021. In many practical settings, data are contaminated by noise. Therefore, not only fitting functions can provide predictive models that summarize complex phenomena, but they can also act as filters, to remove noise from raw measurements and to reveal the underlying signal structure.

Local polynomial smoothing (or local polynomial regression) provides a powerful and flexible framework to meet this two-fold requirement. It is widely used in applications like time-series analysis and spectral estimation, where the goal is to isolate deterministic patterns from stochastic disturbances, and especially when the signal trend is too complex for a single global function[[, e.g.]]scharf1991, lyons1997, shumway2017. Unlike global regression, local polynomial smoothing fits a separate, simple model at every point of interest by defining a local neighborhood (or bandwidth), possibly applying weights via a kernel function, and then performing a least squares fit. The resulting “smoothed” value corresponds to the evaluation of this local polynomial at the target point.

Several methods have refined this approach; most notably, the locally weighted scatterplot smoothing (LOWESS) and locally estimated scatterplot smoothing (LOESS), which employ iterative weighting to ensure robustness against outliers[10,9]. These methods have been extended to complex tasks like seasonal-trend decomposition (STL)[8]. Another particularly relevant class of local polynomial models is the digital smoothing polynomial (DISPO)[60]and in particular the Savitzky–Golay (SG) filter[38], which performs local polynomial regression on equally spaced data to preserve higher-order moments of the signal while suppressing noise. The versatility of SG filters has led to their adoption across a wide variety of fields such as biomedical engineering and physiology[14,33,1,3,29,34,37],
analytical chemistry and molecular spectroscopy[38,53,40,61,26,4],
environmental science and remote sensing[18,22,57,46],
industrial systems and energy infrastructure[15,19,50,20,43],
and information and communication sciences[22,23].

This work is motivated by the application of SG filters to axion[31,30,55,56,21,44,12,59]dark-matter searches[16,5,17,42,2,25]in general and to the ALPHA experiment[27]in particular. It makes use of a resonant microwave cavity, commonly known as axion haloscope[47,48], to trigger the resonant conversion of axions into a detectable electromagnetic signal.
One of the primary challenges faced by haloscopes is the identification of an extremely weak, narrow-band signal, hidden within high-resolution power spectral densities. In this context, SG filtering is used to remove the complex, frequency-dependent background of the receiver system without artifacts that could mimic or obscure a real axion signal[[, e.g.]]Foster:2017hbq,Palken:2020wgs,GalloRosso:2022mhx. SG filtering is valued for being analytical, numerically efficient, and predictable, while not requiring any background modeling. However, a careful implementation is needed to minimize some of its known issues such as numerical artifacts, biases, and signal underestimation[39,58].

The effectiveness of these filtering techniques is critically dependent on the selection of the polynomial degree and the window length. Together, they dictate the trade-off between noise suppression and signal distortion[36,24]. Finding the optimal configuration is a non-trivial task. Many approaches can be found in the literature, ranging from manual trial-and-error approaches[32], to automated methods like grid searches[4]or noise-residual matching[54]. Statistical frameworks based on Stein’s[49]Unbiased Risk Estimator (SURE) have also been developed[41,24].

However, these optimization strategies are characterized by a significant computational burden, where a smoothing operation is turned into a heavy, iterative search problem. For instance, we mention the need for iterative numerical solvers like Newton’s method to find optimal smoothing parameters[41], the requirement for repeated evaluations across a range of candidate window lengths[61,54], and the demand for pointwise adaptive filtering where the window is tuned for every single data point[24]. Such procedures are frequently described as “time-consuming”[61], especially if the fitting function and/or its first derivative needs to be evaluated across all the points in the windows. As a result, the computational cost can become prohibitively expensive for the high-resolution, large-scale datasets typical of modern axion haloscope experiments.

Traditional computational implementations of these fits often rely on power series or Vandermonde matrix formulations[[, e.g.]]Guest,Schafer2011,NumRec2,NumRec3. However, these become numerically burdensome as the polynomial order or the number of data points increases. Such approaches are prone to numerical ill-conditioning, where small perturbations in the data are amplified, leading to unstable estimates and undermining the reliability of the model.

A long-known and well-established alternative to the Vandermonde formulation in curve fitting is the use of orthogonal polynomials[[, e.g.]]Shohat,Szego,Guest,Cadwell1961S,Peck1962,Hayes1969A,Fan1996,Brinker and specifically the so-called Chebyshev polynomials, named after Chebyshev and his work[7,52]. In the context of repeated evaluations, a fitting process based on orthogonal polynomials can benefit from their recursive properties, allowing for the recursive addition of higher-order terms without recomputing the entire model. However, and as discussed in[11], the evaluation of discrete Chebyshev polynomials via standard recurrence relations is prone to significant inaccuracies, particularly at high polynomial orders or for large data windows. These findings highlight that cumulative errors can lead to substantial deviations from the expected normalization, where the deviation can even exceed the norm itself as the interval size increases.

The goal of this work is to present a method that achieves both high numerical accuracy and improves computational efficiency. We present a recursive algorithm for the calculation of the polynomial fitting matrix that exploits its inherent bisymmetric properties to reduce memory usage and processing time. Our approach provides a fast and accurate solution for curve fitting in large-scale datasets, such as the high-resolution power spectra encountered in ALPHA. The presented algorithms are publicly available[35].

The paper is organized as follows. In Section2, we introduce the theoretical framework underlying curve fitting with orthogonal polynomials. Section3is devoted to the numerical implementation of the proposed method, where algorithmic details and practical considerations are discussed. The performance of the approach is then assessed in Section4through a series of numerical experiments designed to evaluate accuracy, robustness, and computational efficiency. Finally, Section5summarizes the main results of this work and outlines possible directions for future research.

## 2Curve fitting and orthogonal polynomials

In this section, we provide a review of the basic
concepts and formalism about curve fitting
(Section2.1), orthogonal
polynomials (Section2.2), and their
numerical properties when applied to polynomial
fitting which will be used in Section3.

## 2.1Method and formalism

Let us consider a set ofNNpoints𝒙\bm{x},𝒙=(x0,x1,…,xN−1)T,\bm{x}=(x_{0},\,x_{1},\dots,x_{N-1})^{T},(1)

and a set ofNNdata points𝒚\bm{y},𝒚=(y0,y1,…,yN−1)T.\bm{y}=(y_{0},\,y_{1},\dots,y_{N-1})^{T}.(2)

The latter can be thought of as the outcome of a
measurement at different conditions represented by
each one of thexix_{i}’s.

Given the pairs(xi,yi)(x_{i},\,y_{i}), we can define
a polynomial fitting functionfn​(x)f_{n}(x)as the
polynomial of degreennthat minimizes the
mean-squared error for the group of input samples:ℰ=∑i=1N(fn​(xi)−yi)2.\mathcal{E}=\sum_{i=1}^{N}\left(f_{n}(x_{i})-y_{i}\right)^{2}.(3)

Incidentally, we have assumed that the data points
are weighted equally. This assumption will hold
from now on.

Once the terms of the problems have been set,
the fitting function is univocally determined by
its set of coefficientsbj;nb_{j;n}. That is,fn​(x)=∑j=0nbj;n​xj.f_{n}(x)=\sum_{j=0}^{n}b_{j;n}\,x^{j}.(4)

The notationbj;nb_{j;n}highlights that
the coefficients depend both on thejj-th power
ofxxand the degreennof the fitting
polynomial.

Given expression (4), we can write
equation (3) asℰ=∑i=1N(∑j=0nbj;n​xij−yi)2,\mathcal{E}=\sum_{i=1}^{N}\left(\sum_{j=0}^{n}b_{j;n}\,x_{i}^{j}-y_{i}\right)^{2},(5)

where the only unknowns are precisely thebj;nb_{j;n}. A straightforward minimization process
yields the set ofn+1n+1equations inn+1n+1unknowns that constitute the so-called normal
equations for the coefficientsbn;jb_{n;j}:∑j=0nbn;j​∑i=1Nxij​xik=∑i=1Nyi​xik(k=0,…,n).\sum_{j=0}^{n}b_{n;j}\sum_{i=1}^{N}\,x_{i}^{j}\,x_{i}^{k}=\sum_{i=1}^{N}y_{i}\,x_{i}^{k}\quad(k=0,\dots,n).(6)

A well-established[[, e.g.]]Guest,Schafer2011,
NumRec2,NumRec3 approach for addressing this problem is to express Equation (6) in matrix
form:(𝑽T⋅𝑽)⋅𝒃\displaystyle\left(\bm{V}^{T}\cdot\bm{V}\right)\cdot\bm{b}=𝑽T⋅𝒚,\displaystyle=\bm{V}^{T}\cdot\bm{y},(7)𝒃\displaystyle\bm{b}=(𝑽T⋅𝑽)−1⋅𝑽T⋅𝒚\displaystyle=\left(\bm{V}^{T}\cdot\bm{V}\right)^{-1}\cdot\bm{V}^{T}\cdot\bm{y}(8)

where𝑽\bm{V}is known as Vandermonde’s matrix:[𝑽]i​ℓ=xiℓ.\left[\bm{V}\right]_{i\ell}=x_{i}^{\ell}.(9)

Thanks to expression (8), we can
now express equation (4) as a
matrix product:fn​(x)=𝒑​(x)⋅𝒃with𝒑​(x)=(1,x,…,xn).f_{n}(x)=\bm{p}(x)\cdot\bm{b}\quad\text{with}\quad\bm{p}(x)=(1,x,\dots,x^{n}).(10)

As it will turn out to be useful in the following,
we can also define the vector𝒇n\bm{f}_{n}composed by the fitting functionfn​(x)f_{n}(x)evaluated at the pointsxix_{i}:𝒇n=(fn​(x0),fn​(x1),…,fn​(xN−1)),\bm{f}_{n}=(f_{n}(x_{0}),\,f_{n}(x_{1}),\dots,\,f_{n}(x_{N-1})),(11)

In this case, the vector of powers for eachxix_{i}is precisely a row of the Vandermonde’s matrix.
Thus, as it is straightforward to see𝒇n=𝑽⋅𝒃=𝑽⋅(𝑽T⋅𝑽)−1⋅𝑽T⋅𝒚≡𝑨n⋅𝒚.\bm{f}_{n}=\bm{V}\cdot\bm{b}=\bm{V}\cdot\left(\bm{V}^{T}\cdot\bm{V}\right)^{-1}\cdot\bm{V}^{T}\cdot\bm{y}\equiv\bm{A}_{n}\cdot\bm{y}.(12)

Thanks to the linear nature of the problem, we
have now a function that takes the vector of
measurements and automatically performs a
polynomial fit, returning the value of the
fitting function at the measured points.

In the following, we focus on the problem of
computing matrix𝑨n\bm{A}_{n}. As definition
(12) shows, a direct evaluation of
the matrix product is not an optimal approach.
In fact, exponential growth (9) can
lead to accuracy losses, especially for largennorNN. These problems will be discussed in
Section4. Moreover, and with respect
to the use of memory, the matrix𝑨n\bm{A}_{n}has
several symmetry properties (see Section2.4). This means that the storage of
a fullN×NN\times Nmatrix is not required—two,
in fact, as multiplication (12)
shows:(𝑽T⋅𝑽)−1(\bm{V}^{T}\cdot\bm{V})^{-1}and𝑽\bm{V}.

## 2.2Orthogonal polynomials

In this section, we present an overview and some
basic properties of orthogonal polynomials, which
will be useful for the calculation of𝑨n\bm{A}_{n}and therefore for the optimization of the problem
of curve fitting. We refer to Refs.[13,45]for notation and theoretical background.

In general, given a set ofxix_{i}’s, the set of
orthogonal polynomials of degreennis defined by
the relation∑i=1Npn​(xi)​pm​(xi)=δn​m​Hn2,\sum_{i=1}^{N}p_{n}(x_{i})\,p_{m}(x_{i})=\delta_{nm}H_{n}^{2},(13)

whereδn​m\delta_{nm}is the Kronecker delta andHnH_{n}is the norm of the polynomial of degreenn:Hn=∑i=1Npn2​(xi).H_{n}=\sum_{i=1}^{N}p_{n}^{2}(x_{i}).(14)

We stress that, in general,Hn≠1H_{n}\neq 1.

The explicit expansion ofpn​(x)p_{n}(x)in powers ofxxwill be written aspn​(x)=∑j=0nβn;j​xj.p_{n}(x)=\sum_{j=0}^{n}{\beta_{n;j}\,x^{j}}.(15)

Equation (15) can also be
inverted, leading to the expansion ofxxas a
series ofpj​(x)p_{j}(x):xn=∑j=0nαn;j​pj​(x).x^{n}=\sum_{j=0}^{n}\alpha_{n;j}\,p_{j}(x).(16)

An expression forαn;j\alpha_{n;j}can be recovered
by combining relations (16) and
(13):∑i=1N(xin−∑j=0n−1αn;j​pj​(xi))​pℓ​(xi)=δℓ​n​αn;n​Hn2,\sum_{i=1}^{N}\left(x_{i}^{n}-\sum_{j=0}^{n-1}\alpha_{n;j}\,p_{j}(x_{i})\right)p_{\ell}(x_{i})=\delta_{\ell n}\alpha_{n;n}H_{n}^{2},(17)

which gives:αn;j=1Hn2​∑i=1Nxin​pj​(xi).\alpha_{n;j}=\frac{1}{H_{n}^{2}}\sum_{i=1}^{N}x_{i}^{n}\,p_{j}(x_{i}).(18)

Thanks to relations
(15–18)
we can express the normal equations
(6) in terms of the orthogonal
polynomialspn​(x)p_{n}(x). As a starting point, we
express the fitting functionfn​(x)f_{n}(x)in
(4) asfn​(x)=∑j=0naj​pj​(x).f_{n}(x)=\sum_{j=0}^{n}a_{j}\,p_{j}(x).(19)

It is worth noting that, unlike thebn;jb_{n;j}’s,
the coefficientsaja_{j}do not depend on the
specific degree of the fitting function. In fact,fn+1​(x)f_{n+1}(x)can be computed by simply adding the(n+1)(n+1)thterm to the series, while all thebn;jb_{n;j}’s would need to be substituted by newbn+1;jb_{n+1;j}’s.

A comparison between definitions (4)
and (19) leads to:fn​(x)=∑j=0nbn;j​∑ℓ=0jαj;ℓ​pℓ​(x)=∑ℓ=0n(∑j=ℓnbn;j​αj;ℓ)​pℓ​(x)≡∑ℓ=0naℓ​pℓ​(x).f_{n}(x)=\sum_{j=0}^{n}b_{n;j}\sum_{\ell=0}^{j}\alpha_{j;\ell}\,p_{\ell}(x)=\sum_{\ell=0}^{n}\left(\sum_{j=\ell}^{n}b_{n;j}\,\alpha_{j;\ell}\right)p_{\ell}(x)\equiv\sum_{\ell=0}^{n}a_{\ell}\,p_{\ell}(x).(20)

Now, we can apply relations (20) and
(18) to the l.h.s. of
(6), and relations (16)
and (18) to its r.h.s. This givesaj=1Hn2​∑i=1Nyi​pj​(xi),a_{j}=\frac{1}{H_{n}^{2}}\sum_{i=1}^{N}y_{i}\,p_{j}(x_{i}),(21)

which finally leads tofn​(x)=∑i=1Nyi​∑j=0npj​(xi)​pj​(x)Hj.f_{n}(x)=\sum_{i=1}^{N}y_{i}\sum_{j=0}^{n}\frac{p_{j}(x_{i})\,p_{j}(x)}{H_{j}}.(22)

We can easily recognize the matrix product (12) hiding in relation (22)
and, consequently, how orthogonal polynomials
link to matrix𝑨n\bm{A}_{n}. Fundamental properties
of𝑨n\bm{A}_{n}will be highlighted in Section2.4. Before that, the explicit
expression for polynomialspj​(x)p_{j}(x)will now be
discussed.

## 2.3Chebyshev polynomials

The computation of polynomialspj​(x)p_{j}(x)in
equation (22) was originally performed
by Chebyshev[7,52,45].
In addition to the assumption of equally-weighted
data (wi=1w_{i}=1) his method works under the
assumption that the series of pointsxix_{i}are
equally spaced by the same amountΔ​x\Delta x:𝒙=(x0,x0+Δ​x,…,x0+(N−1)​Δ​x).\bm{x}=(x_{0},\,x_{0}+\Delta x,\dots,x_{0}+(N-1)\,\Delta x).(23)

We stick to this assumption. We also follow
Chebyshev’s choice to rescale𝒙\bm{x}so as to
take up integer values:xℓ=ℓ∈[0,1,…,N).x_{\ell}=\ell\in[0,\,1,\,\dots,\,N).(24)

The reasons for this choice are many. First of all,
the value of orthogonal polynomials is independent
of the origin of their variable, as e.g. pointed
out in[13, Sec. 7.2.1]. Moreover,
equation (12) and the matrix𝑨n\bm{A}_{n}are independent of the equally-weighted
and equally-spaced points of applicationxix_{i}’s.
Indeed, thexix_{i}’s play no role beyond indexing,
while the construction depends solely on the valuesyiy_{i}’s and the associatedfif_{i}’s. Naming thexix_{i}’s from0toN−1N-1will automatically link
them to the indices of the matrix𝑨n\bm{A}_{n}.

In our notation, Chebyshev polynomials will be
denoted asqn​(x)q_{n}(x). Under assumptions
(23) and (24), such
polynomials can be expressed using Szegö’s
notation[51]and thenthn^{\text{th}}forward differenceΔn\Delta^{n}:qn​(ℓ)=n!​Δn​[(ℓn)​(n−Nn)].q_{n}(\ell)=n!\,\Delta^{n}\!\left[\binom{\ell}{n}\binom{n-N}{n}\right].(25)

Polynomialsqn​(ℓ)q_{n}(\ell)are not normalized, and
their normHnH_{n}(14) is given byHn=(n!)2​(2​nn)​(N+n2​n+1)=N​∏j=1n(N2−j2)2​n+1.H_{n}=(n!)^{2}\binom{2n}{n}\binom{N+n}{2n+1}=\frac{N\prod_{j=1}^{n}\left(N^{2}-j^{2}\right)}{2n+1}.(26)

The crucial property that characterizes every set
of orthogonal polynomials is the existence of a
recursive relation that gives the polynomial of
degree(n+1)(n+1)from the ones of degreennand(n−1)(n-1)[[, e.g.]]Nikiforov. In the case of
Chebyshev polynomials, the relation reads:(n+1)​qn+1​(ℓ)=(2​ℓ−N+1)​(2​n+1)​qn​(ℓ)−n​(N2−n2)​qn−1​(ℓ),(n+1)\,q_{n+1}(\ell)=\left(2\ell-N+1\right)(2n+1)\,q_{n}(\ell)-n(N^{2}-n^{2})q_{n-1}(\ell),(27)

with initial values given by:q0​(ℓ)=1andq1​(ℓ)=2​ℓ−N+1.q_{0}(\ell)=1\quad\text{and}\quad q_{1}(\ell)=2\ell-N+1.(28)

A similar relation holds also for coefficientsβn;j\beta_{n;j}in (15) as well as the
normHnH_{n}. The former satisfies:βn;j=2​(2​n−1)n​βn−1;j−1−(N−1)​(2​n−1)n​βn−1;j−n−1n​(N2−(n−1)2)​βn−2;j,\beta_{n;j}=\frac{2(2n-1)}{n}\beta_{n-1;\,j-1}-\,\frac{(N-1)(2n-1)}{n}\beta_{n-1;\,j}-\frac{n-1}{n}\left(N^{2}-(n-1)^{2}\right)\beta_{n-2;\,j},(29)

whereβn;j=0\beta_{n;\,j}=0ifj>nj>norj<0j<0.
The normHnH_{n}, on the other hand, satisfies:Hn=2​n−12​n+1​(N2−n2)​Hn−1.H_{n}=\frac{2n-1}{2n+1}(N^{2}-n^{2})H_{n-1}.(30)

Chebyshev polynomials satisfy another kind of
recursive relation, this time inℓ\ell, for fixed
values ofnn(see e.g.[11]):qn​(ℓ)=Dn​qn​(ℓ−1)+En​qn​(ℓ−2),q_{n}(\ell)=D_{n}\,q_{n}(\ell-1)+E_{n}\,q_{n}(\ell-2),(31)

assumingn<Nn<Nandℓ∈[0,N)\ell\in[0,\,N).
The coefficientsDnD_{n}andEnE_{n}are given by:Dn\displaystyle D_{n}=−n​(n+1)+(2​ℓ−1)​(ℓ−N−1)+ℓℓ​(N−ℓ);\displaystyle=-\frac{n(n+1)+(2\ell-1)(\ell-N-1)+\ell}{\ell(N-\ell)};(32)En\displaystyle E_{n}=(ℓ−1)​(ℓ−N−1)ℓ​(N−ℓ).\displaystyle=\frac{(\ell-1)(\ell-N-1)}{\ell(N-\ell)}.(33)

Among the useful properties of Chebyshev
polynomials that will be useful in the following, we
mention their symmetry inℓ∈[0,N)\ell\in[0,\,N)[28]. That is,qn​(ℓ)=(−1)n​qn​(N−1−ℓ).q_{n}(\ell)=(-1)^{n}\,q_{n}(N-1-\ell).(34)

In principle, what we have discussed so far would
be enough to determine the polynomials in equation
(22) and their coefficientsβn;j\beta_{n;j}in (15). Unfortunately,
however, their definition would remain implicit.
An explicit expression does exist, but we have to
resort to the so-called factorial notation borrowed
from[13]. Let us write:qn​(ℓ)=∑j=0nβ(j​n)​ℓ(j),q_{n}(\ell)=\sum_{j=0}^{n}\beta_{(jn)}\ell^{(j)},(35)

whereℓ(j)≡∏k=0j−1(ℓ−k)=ℓ!(ℓ−j)!\ell^{(j)}\equiv\prod_{k=0}^{j-1}(\ell-k)=\frac{\ell!}{(\ell-j)!}(36)

andβ(j​n)=(−1)n−j​(n+jn)​(nj)​(N−1)(n)(N−1)(j).\beta_{(jn)}=(-1)^{n-j}\binom{n+j}{n}\binom{n}{j}\frac{(N-1)^{(n)}}{(N-1)^{(j)}}.(37)

Interestingly, coefficientsβ(j​n)\beta_{(jn)}are
still related by a recursive relation. In fact, it
even takes a simpler form than (29):β(j​(n+1))\displaystyle\beta_{(j(n+1))}=−(N−n−1)​n+1+jn+1−j​β(j​n);\displaystyle=-\left(N-n-1\right)\,\frac{n+1+j}{n+1-j}\,\beta_{(jn)};(38)β((j+1)​n)\displaystyle\beta_{((j+1)n)}=−n−j(j+1)2​n+j+1N−j−1​β(j​n).\displaystyle=-\frac{n-j}{(j+1)^{2}}\,\frac{n+j+1}{N-j-1}\,\beta_{(jn)}.(39)

We will make good use of these two relations in
Section3, where we finally
tackle the problem of the computation of matrix𝑨n\bm{A}_{n}.

## 2.4Useful properties of𝑨n\bm{A}_{n}and its derivative

At the core of our computation is the matrix[𝑨n]i​ℓ=∑j=0nAi​ℓj=∑j=0nqj​(i)​qj​(ℓ)Hj.[\bm{A}_{n}]_{i\ell}=\sum_{j=0}^{n}A^{j}_{i\ell}=\sum_{j=0}^{n}\frac{q_{j}(i)\,q_{j}(\ell)}{H_{j}}.(40)

We remind that, in our notation, the row indexiiand the column indexℓ\ellrange from 0 toN−1N-1, whereNNis the number of fitted points
andnnthe degree of the fitting polynomial.

The first thing that emerges from definition
(40) is the fact that matrix𝑨n\bm{A}_{n}is bisymmetric. That is, and thanks to
relation (34),𝑨n\bm{A}_{n}is symmetric
about both of its main diagonals:[𝑨n]N−1−i,N−1−ℓ\displaystyle[\bm{A}_{n}]_{N-1-i,N-1-\ell}=[𝑨n]N−1−i,N−1−ℓ=\displaystyle=[\bm{A}_{n}]_{N-1-i,N-1-\ell}=(41a)=[𝑨n]ℓ,i=[𝑨n]N−1−ℓ,N−1−i,\displaystyle=[\bm{A}_{n}]_{\ell,i}=[\bm{A}_{n}]_{N-1-\ell,N-1-i},(41b)

where (41b) does not apply ifi=ℓi=\ellori+ℓ=N−1i+\ell=N-1.
This means that the algorithm presented in Section3will not have to deal with the
computation ofN×NN\times Nentries, but just with
a quarter of those. Moreover, a similar symmetry
holds for the two central axes:Ai,N−1−ℓj\displaystyle A_{i,N-1-\ell}^{j}=(−1)j​Ai​ℓj;\displaystyle=(-1)^{j}A^{j}_{i\ell};(42)[𝑨n]i,N−1−ℓ\displaystyle[\bm{A}_{n}]_{i,N-1-\ell}=∑j=0n(−1)j​Ai​ℓj.\displaystyle=\sum_{j=0}^{n}(-1)^{j}A^{j}_{i\ell}.(43)

Hence, while calculating𝑨n\bm{A}_{n}through
summation (40), it will suffice to
know the termsAi​ℓjA^{j}_{i\ell}(j=0,…,nj=0,\dots,n) for
only half of a quarter of the entries—see Figure1and2for a graphical
representation.

Finally, the rows and columns of𝑨n\bm{A}_{n}sum up
to 1, thanks to the relation (14),
at the core of the definition of orthogonal
polynomials. From a numerical perspective, dealing
with𝑨n\bm{A}_{n}as a whole helps preventing
overflows and loss of precision, in contrast with
going throughqn​(ℓ)q_{n}(\ell)(25) andHnH_{n}(26) separately, or through
the exponential terms in Vandermonde’s matrix
(9).

As a side note, this means that𝑨n\bm{A}_{n}is
idempotent, too. That is,𝑨n⋅𝑨n=𝑨n\bm{A}_{n}\cdot\bm{A}_{n}=\bm{A}_{n}. This is a straightforward conclusion
from the fact that fitting the fitted values
returns the fitted values themselves; that is,𝑨n⋅𝒇n=𝒇n\bm{A}_{n}\cdot\bm{f}_{n}=\bm{f}_{n}.

Relation (40) also allows for the
definition of the first derivative of the
polynomial fit (4), evaluated at the
fitting points:[𝒇n′]i=1Δ​x​∑ℓ=0N−1[𝑩n]i​ℓ​[𝒚]ℓ=∑ℓ=0N−1yℓΔ​x​∑j=0nqj′​(i)​qj​(ℓ)Hj,[\bm{f}_{n}^{\prime}]_{i}=\frac{1}{\Delta x}\sum_{\ell=0}^{N-1}[\bm{B}_{n}]_{i\ell}[\bm{y}]_{\ell}=\sum_{\ell=0}^{N-1}\frac{y_{\ell}}{\Delta x}\sum_{j=0}^{n}\frac{q_{j}^{\prime}(i)\,q_{j}(\ell)}{H_{j}},(44)

whereΔ​x\Delta xis the distance between the
data points. Note that, in our notation, we
preserve the subscriptnnin𝑩n\bm{B}_{n}, even if
the fitting polynomial has one lesser degree.

Matrix𝑩n\bm{B}_{n}is no more symmetrical. However,
it is anti-centrosymmetrical, as a differentiation
of relation (34) can easily show.
That is,[𝑩n]N−1−i,N−1−ℓ=−[𝑩n]i​ℓ.[\bm{B}_{n}]_{N-1-i,N-1-\ell}=-[\bm{B}_{n}]_{i\ell}.(45)

The same property holds for each of the termsBi​ℓjB_{i\ell}^{j}in the sum (44).
Moreover, it can be shown thatBN−1−i,ℓj\displaystyle B^{j}_{N-1-i,\ell}=(−1)j+1​Bi​ℓj;\displaystyle=(-1)^{j+1}B_{i\ell}^{j};(46a)Bi,N−1−ℓj\displaystyle B^{j}_{i,N-1-\ell}=(−1)j​Bi​ℓj.\displaystyle=(-1)^{j\hphantom{+1}}B_{i\ell}^{j}.(46b)

## 3Numerical implementation

In this section, we present the algorithms to
compute𝑨n\bm{A}_{n}and𝑩n\bm{B}_{n}. The computation
of𝑨n\bm{A}_{n}will follow two different approaches,
the first one being characterized by a better
numerical accuracy (Section3.1), and
the other one by a faster execution (Section3.2). A systematic discussion about the
performances is presented in Section4.

## 3.1Numerical computation of𝑨n\bm{A}_{n}

Based on definition (40), the
computation of each entry of𝑨n\bm{A}_{n}requires
the summation over the polynomial degreejj;
i.e., over the set of values:A→i​ℓ=(Ai​ℓ0,…,Ai​ℓn).\vec{A}_{i\ell}=(A^{0}_{i\ell},\dots,\,A^{n}_{i\ell}).(47)

At each step, we take advantage of the recursive
relations to getA→i​ℓ\vec{A}_{i\ell}from the values
that have already been computed.
The simplest way is to proceed by rows, as shown
in Figure1. The computation does
not need to span the whole set of columns because,
thanks to symmetries (41) matrix𝑨n\bm{A}_{n}is composed of 4 identical triangles.
In this case, we focus on the left one. Moreover,
values[𝑨n]i​ℓ[\bm{A}_{n}]_{i\ell}and[𝑨n]N−1−i,ℓ[\bm{A}_{n}]_{N-1-i,\ell}are linked by relation (43).
Hence, the number of rows to be covered explicitly
is just111Incidentally, and for clarity
purposes, we point out that the code attached to
the present paper stores the result in a
one-dimensional array of lengthNr×(⌊N/2⌋+1)N_{r}\times(\lfloor N/2\rfloor+1), where the indexkkof the array
is linked to the row indexiiand column indexℓ\ellby:k=i+ℓ​(N−ℓ)k=i+\ell(N-\ell).:Nr=⌊N/2⌋+N​mod​2N_{r}=\lfloor N/2\rfloor+N\text{mod }2.Figure 1:Graphical representation of the
computation of the matrix𝑨n\bm{A}_{n}as
described in Section3.1. Because
of symmetries (41) only a
quarter of it needs computation. And because
of (43), the sum for the entries
in the lower part of the triangle can be
recovered directly from the upper partData:NN,n<Nn<N1imax←⌊N/2⌋+(Nmod2)−1i_{\max}\leftarrow\lfloor N/2\rfloor+(N\!\mod 2)-1𝒂0←𝒂1←[0,…,0]\bm{a}_{0}\leftarrow\bm{a}_{1}\leftarrow[0,\dots,0]⊳\trianglerightA→i,ℓ−2,A→i,ℓ−1\vec{A}_{i,\ell-2},\vec{A}_{i,\ell-1}in (52)2fori←0i\leftarrow 0toimaxi_{\max}do3forℓ←0\ell\leftarrow 0toiido4ifℓ=0\ell=0then5Compute𝒂1\bm{a}_{1}from eqs. (48,49)67else ifℓ=1\ell=1then8𝒂0←𝒂1\bm{a}_{0}\leftarrow\bm{a}_{1}9Compute𝒂1\bm{a}_{1}from eq. (51)1011else12Compute𝒂2\bm{a}_{2}from eq. (52)13𝒂1←𝒂2\bm{a}_{1}\leftarrow\bm{a}_{2}14𝒂0←𝒂1\bm{a}_{0}\leftarrow\bm{a}_{1}1516end if17sum_and_update(𝐀n,𝐚1\bm{A}_{n},\bm{a}_{1})1819end for2021end for22Subroutinesum_and_update(𝐀n,𝐚1\bm{A}_{n},\bm{a}_{1})Σ,Σ′←0,0\Sigma,\Sigma^{\prime}\leftarrow 0,0⊳\trianglerightTotal of sum (40) for
elements(i,ℓ)(i,\ell)and(i,N−ℓ−1)(i,N-\ell-1)of𝑨n\bm{A}_{n}σ←+1\sigma\leftarrow+1⊳\trianglerightSign betweenAi​ℓjA^{j}_{i\ell}andAi,N−ℓ−1jA^{j}_{i,N-\ell-1}23forj←0j\leftarrow 0tonndo24Σ←Σ+𝒂1​[j]\Sigma\leftarrow\Sigma+\bm{a}_{1}[j]25Σ′←Σ+σ∗𝒂1​[j]\Sigma^{\prime}\leftarrow\Sigma+\sigma*\bm{a}_{1}[j]26σ←−σ\sigma\leftarrow-\sigma27end for28WriteΣ\Sigmaat element(i,ℓ)(i,\ell)of𝑨n\bm{A}_{n}29WriteΣ′\Sigma^{\prime}at element(N−i−1,ℓ)(N-i-1,\ell)of𝑨n\bm{A}_{n}3031Algorithm 1Computation of𝑨n\bm{A}_{n}(Section3.1)

The computation relies on the recursive properties
of the orthogonal polynomialsqn​(x)q_{n}(x)embedded in
the definition of𝑨n\bm{A}_{n}. In fact, for each
new rowii, one just needs to obtain the first
two column entries—i.e.A→i​0\vec{A}_{i0}andA→i​1\vec{A}_{i1}. Then, the recursive relation (31) will propagate them across the columns.
In turn, anyA→i​ℓ\vec{A}_{i\ell}can be obtained from
the two valuesAi​ℓ0A_{i\ell}^{0}andAi​ℓ1A_{i\ell}^{1},
corresponding to a degreej=0j=0andj=1j=1,
recursively propagated up tonnthanks to relation
(27). The calculation ofAi​ℓ0A_{i\ell}^{0}andAi​ℓ1A_{i\ell}^{1}is straightforward and
derives directly from the explicit expression
(28) for the Chebyshev polynomials
of degreej=0j=0andj=1j=1, plugged into definition
(40):Ai​ℓ0=1NandAi​ℓ1=3​(N−1−2​i)​(N−1−2​ℓ)N​(N2−1).A^{0}_{i\ell}=\frac{1}{N}\quad\text{and}\quad A^{1}_{i\ell}=\frac{3(N-1-2i)(N-1-2\ell)}{N(N^{2}-1)}.(48)

Then, the recursive relation for the subsequent
values ofA→i​0\vec{A}_{i0}is derived by combining
relations (27) and (40),
while applying relations (30,38), and keeping in mind thatqn​(0)=β(0​n)q_{n}(0)=\beta_{(0n)}. This gives:Ai​0j=2​j+1(N+j)​j​((N−1−2​i)​Ai​0j−1−(j−1)​(N−j+1)2​j−3​Ai​0j−2).A^{j}_{i0}=\frac{2j+1}{(N+j)\,j}\left((N-1-2i)A^{j-1}_{i0}\right.-\left.\frac{(j-1)(N-j+1)}{2j-3}A^{j-2}_{i0}\right).(49)

The computation of the second term in the row,A→i​1\vec{A}_{i1}, follows directly fromA→i​0\vec{A}_{i0}.
We notice:qn​(1)=β(0​n)+β(1​n)=(1−n​(n+1)N−1)​β(0​n),q_{n}(1)=\beta_{(0n)}+\beta_{(1n)}=\left(1-\frac{n(n+1)}{N-1}\right)\beta_{(0n)},(50)

and therefore:Ai​1j=(1−j​(j+1)N−1)​Ai​0j.A^{j}_{i1}=\left(1-\frac{j(j+1)}{N-1}\right)A^{j}_{i0}.(51)

For any other indexℓ>1\ell>1we can use the
recursive relation inℓ\ell, (31),
which remains valid even through definition
(40):Ai​ℓj=Dn​Ai,ℓ−1j+En​Ai,ℓ−2j.A^{j}_{i\ell}=D_{n}A^{j}_{i,\ell-1}+E_{n}A^{j}_{i,\ell-2}.(52)

We recall thatDnD_{n}andEnE_{n}are defined in
(32,33) and depend onℓ\ell. Algorithm1summarizes the
whole procedure.Figure 2:Graphical representation of the
computation of the matrix𝑨n\bm{A}_{n}as
described in Section3.2. Because
of symmetries (41) only a
quarter of it needs computation. And because
of (43), the sum for the entries
in the right part of the triangle can be
recovered directly from the left part by
a change of sign.

## 3.2Numerical computation of𝑨𝒏\bm{A_{n}}. Buffer method
Figure 3:Magnification of the upper triangle
of the right matrix in Figure2assumingN=16N=16. Each new row in the
computation process requires the recursive
termsA→i,ℓ−2\vec{A}_{i,\ell-2}andA→i,ℓ−1\vec{A}_{i,\ell-1}to start the series. A circular buffer
with indices from 0 to 4 ensures that the
values can be read from the terms already
computed; i.e.,A→ℓ−2,i\vec{A}_{\ell-2,i}andA→ℓ−1,i\vec{A}_{\ell-1,i}.

Performing the calculation ofA→i​0\vec{A}_{i0}andA→i​1\vec{A}_{i1}from scratch at the beginning of
every row gives Algorithm1a certain
a certain degree ofnumerical stability. However,
one could improve the speed of Algorithm1by noting that this is not always
necessary.

Let us change perspective and focus on the top
triangle of𝑨n\bm{A}_{n}, as shown by Figure2. In this case, the starting values
needed by each row are:
- •

A→00\vec{A}_{00}andA→01\vec{A}_{01}fori=0i=0;
- •

A→10\vec{A}_{10}andA→11\vec{A}_{11}fori=1i=1;
- •

A→i,i−2\vec{A}_{i,i-2}andA→i,i−1\vec{A}_{i,i-1}fori>1i>1.

Among them, only three need an ad-hoc calculation:A→00\vec{A}_{00}andA→01\vec{A}_{01}for the first
row, andA→11\vec{A}_{11}for the second. All the
others are in fact computed at a certain point in
the previous steps, as the symmetries (41) and Figure3make clear.
A circular buffer of only 5 entries for theA→i​ℓ\vec{A}_{i\ell}can store and read those values,
avoiding the need to pass through relation
(49) at every new iteration.Data:NN,n<Nn<N1𝐛𝐮𝐟𝐟𝐞𝐫←[0→,0→,0→,0→,0→]\bm{\mathrm{buffer}}\leftarrow[\vec{0},\vec{0},\vec{0},\vec{0},\vec{0}]𝒂0←𝒂1←[0,…,0]\bm{a}_{0}\leftarrow\bm{a}_{1}\leftarrow[0,\dots,0]⊳\trianglerightA→i,ℓ−2,A→i,ℓ−1\vec{A}_{i,\ell-2},\vec{A}_{i,\ell-1}in (52)2imax←⌊N/2⌋+(Nmod2)−1i_{\max}\leftarrow\lfloor N/2\rfloor+(N\!\mod 2)-13fori←0i\leftarrow 0toimaxi_{\max}do/*Initialize𝒂0,𝒂1\bm{a}_{0},\bm{a}_{1}*/4ifi=0i=0(first row)then5Compute𝒂0\bm{a}_{0}from eq. (48,49)6Compute𝒂1\bm{a}_{1}from eq. (51)7Write𝒂1\bm{a}_{1}tobuffer8sum_and_update(𝐀n,𝐚0\bm{A}_{n},\bm{a}_{0})9sum_and_update(𝐀n,𝐚1\bm{A}_{n},\bm{a}_{1})1011else ifi=1i=1(second row)then12Read𝒂0\bm{a}_{0}from𝐛𝐮𝐟𝐟𝐞𝐫\bm{\mathrm{buffer}}13Compute𝒂1\bm{a}_{1}from eq. (51)14sum_and_update(𝐀n,𝐚1\bm{A}_{n},\bm{a}_{1})1516else ifi>1i>1then17Read𝒂0,𝒂1\bm{a}_{0},\bm{a}_{1}from𝐛𝐮𝐟𝐟𝐞𝐫\bm{\mathrm{buffer}}18/*Propagate𝒂0,𝒂1\bm{a}_{0},\bm{a}_{1}along the row */19ℓmin←max⁡(i,2)\ell_{\min}\leftarrow\max(i,2)20ℓmax←⌊N/2⌋+(Nmod2)−1\ell_{\max}\leftarrow\lfloor N/2\rfloor+(N\!\!\mod 2)-121forℓ←ℓmin\ell\leftarrow\ell_{\min}toℓmax\ell_{\max}do22Compute𝒂2\bm{a}_{2}from eq. (52)23𝒂0,𝒂1←𝒂1,𝒂2\bm{a}_{0},\bm{a}_{1}\leftarrow\bm{a}_{1},\bm{a}_{2}24sum_and_update(𝐀n,𝐚1\bm{A}_{n},\bm{a}_{1})25ifℓ=i+1\ell=i+1orℓ=i+2\ell=i+2then26Write𝒂1\bm{a}_{1}tobuffer272829end for3031end for32Subroutinesum_and_update(𝐀n,𝐚1\bm{A}_{n},\bm{a}_{1})Σ←0\Sigma\leftarrow 0⊳\trianglerightSum for element(i,ℓ)(i,\ell)Σ′←0\Sigma^{\prime}\leftarrow 0⊳\trianglerightSum for element(i,N−ℓ−1)(i,N-\ell-1)σ←+1\sigma\leftarrow+1⊳\trianglerightSign betweenAi​ℓjA^{j}_{i\ell}andAi,N−ℓ−1jA^{j}_{i,N-\ell-1}33forj←0j\leftarrow 0tonndo34Σ←Σ+𝒂1​[j]\Sigma\leftarrow\Sigma+\bm{a}_{1}[j]35Σ′←Σ+σ∗𝒂1​[j]\Sigma^{\prime}\leftarrow\Sigma+\sigma*\bm{a}_{1}[j]36σ←−σ\sigma\leftarrow-\sigma37end for38WriteΣ\Sigmaat element(i,ℓ)(i,\ell)of𝑨n\bm{A}_{n}39WriteΣ′\Sigma^{\prime}at element(i,N−ℓ−1)(i,N-\ell-1)of𝑨n\bm{A}_{n}4041Algorithm 2Computation of𝑨n\bm{A}_{n}

The same line of reasoning can also be applied to
increase the degree of𝑨n\bm{A}_{n}to𝑨n+1\bm{A}_{n+1},
without having to recompute all the previousnnmatricesAi​ℓjA^{j}_{i\ell}in sum (40).
In fact, it is enough to compute the three termsA00n+1A^{n+1}_{00},A01n+1A^{n+1}_{01}, andA11n+1A^{n+1}_{11}and then propagate those recursively, while adding
eachAi​ℓn+1A^{n+1}_{i\ell}to the corresponding element
of[𝑨n]i​ℓ[\bm{A}_{n}]_{i\ell}. Numerically, the
problem is simplified by the fact that the
circular buffer is used to store and read justAℓ−2,in+1A_{\ell-2,i}^{n+1}andAℓ−1,in+1A_{\ell-1,i}^{n+1},
rather than the whole set of valuesA→ℓ−2,i\vec{A}_{\ell-2,i}andA→ℓ−1,i\vec{A}_{\ell-1,i}.

## 3.3Numerical computation of𝑩𝒏\bm{B_{n}}

In the numerical computation of𝑩𝒏\bm{B_{n}}, we
cannot longer rely on bisymmetry. Therefore, the
calculation proceeds by rows, in the same fashion
as Algorithm1.
Once again,
the idea is to buildB→i​0\vec{B}_{i0}andB→i​1\vec{B}_{i1}for each new row, and use the recursive
properties of the Chebyshev polynomials to
increase the column index. Starting fromB→i​0\vec{B}_{i0}, we notice:Bi​ℓ0=0;Bi​ℓ1=−6​(N−1−2​ℓ)N​(N2−1).B^{0}_{i\ell}=0;\qquad B^{1}_{i\ell}=-\frac{6(N-1-2\ell)}{N(N^{2}-1)}.(53)

Differentiation of equation (49)
provides the relation to obtain the values up toj=nj=n:Bi​0n=2​n+1(N+n)​n((N−1−2i)Bi​0n−1−2Ai​0n−1−(n−1)​(N−n+1)2​n−3Bi​0n−2).B^{n}_{i0}=\frac{2n+1}{(N+n)n}\left((N-1-2i)B^{n-1}_{i0}-2A^{n-1}_{i0}\vphantom{\frac{(n-1)(N-n+1)}{2n-3}}\right.\\
\left.-\frac{(n-1)(N-n+1)}{2n-3}B^{n-2}_{i0}\right).(54)

In this case, however, and in contrast with
(49), we note that the knowledge ofAi​0n−1A_{i0}^{n-1}is also required.Figure 4:Graphical representation of the
computation of the matrix𝑩n\bm{B}_{n}. Because
of symmetries (45) only the top
half needs computation. And because of
(46), entries that are symmetrical
with respect to the central axis can be
recovered from the sameB→i​ℓ\vec{B}_{i\ell}.

OnceB→i​0\vec{B}_{i0}is known,B→i​1\vec{B}_{i1}is
recovered from a relation similar to (51):Bi​1j=(1−j​(j+1)N−1)​Bi​0j.B^{j}_{i1}=\left(1-\frac{j(j+1)}{N-1}\right)B^{j}_{i0}.(55)

Any further value along the row can be computed
from the same recursive relation inℓ\ell, i.e. equation (52). In fact, and from
definition (44), the differentiation
affects the polynomial corresponding to the indexii, while the one with indexℓ\ellremains
unchanged.

As it happens for the computation of𝑨n\bm{A}_{n},
values[𝑩n]i​ℓ[\bm{B}_{n}]_{i\ell}and[𝑩n]N−1−i,ℓ[\bm{B}_{n}]_{N-1-i,\ell}are linked by relation (46).
Hence, each step gets the two values symmetrical
with respect to the central axis, and the number
of rows to be covered by the loop is justNr=⌊N/2⌋+N​mod​2N_{r}=\lfloor N/2\rfloor+N\text{mod }2(see Figure4).

## 4PerformanceFigure 5:Comparison of the accuracy of
Algorithms 0,1, and2in approximating matrix𝑨n\bm{A}_{n}.
The error distributions, quantified by the
standard deviation of the differences between
computed and true values (obtained from
Mathematica), are shown for varying polynomial
degreesnnand window lengthsNN.

In this section, we evaluate the performances of
Algorithms1(Section3.1)
and2(Section3.2). We
compare their execution time and accuracy against
direct matrix multiplication. For clarity,
we refer to the direct matrix multiplication in
Eq. (12) as Algorithm 0. For the
latter, we did not write our own routines, but
rather relied on theTMatrixDlibrary of
ROOT[6], which has the advantage of being
already tested and optimized. In order to even out
contingent factors such as memory access and
management, we use the homologous libraryTArrayDto handle the arrays in our
algorithm. The specific version of ROOT is
6.32.02, compiled with g++(GCC)
11.4.1. The calculations were performed using
Almalinux 9 on a hypervisor “Proxmox,” with
processors Intel Xeon CPU E5-2650 v3 at 2.3 GHz.

The major difference emerging from the three
methods is the level of accuracy that they can
reach, as shown in Figure5. We
compared 2500 entries of𝑨n\bm{A}_{n}as given by
Algorithms 0, 1, and 2 with the true values
obtained from Mathematica with arbitrary
precision. The difference between the computed and
true values was then analyzed by examining the
distribution of these errors. To quantify the
accuracy of each algorithm, we report the standard
deviation of the error distributions, which serves
as an indicator of the variability in the errors
across all the elements of the matrix.

As a general trend, the accuracy worsens with
increasing number of pointsNNin the window.
However, the accuracy provided by Algorithms1and2is more stable
across the values of the polynomial degreenn,
while the direct matrix multiplication hits a
maximum of∼1%\sim 1\%accuracy forn=8n=8andN=104N=10^{4}.
Algorithm1is always more accurate
than Algorithm 0, although the latter is sometimes
more precise than the faster version (Algorithm2) for lower values ofnn.Figure 6:Relative difference (56)
in the time of
computation of𝑨n\bm{A}_{n}, between the full
matrix multiplication (12) and
Algorithms1and2,
presented in this work. The left
panel shows the relative improvement as a
function of pointsNNin the window, for
different degreesnnof the polynomial fit,
while the right panel shows the behavior as a
function of the polynomial degree, for
different window lengths.

As it is understandable, the trade-off for a better
accuracy impacts the time of execution. Figure6shows the relative differenceΔ​Ti,rel\Delta T_{i,\mathrm{rel}}in execution timeTiT_{i}for
Algorithms1and2, with
respect to Algorithm 0. We define it asΔ​Ti,rel=Ti−T0min⁡(T0,Ti),with i = 1, 2.\Delta T_{i,\mathrm{rel}}=\frac{T_{i}-T_{0}}{\min(T_{0},T_{i})},\quad\text{with i = 1, 2.}(56)

The result shows that Algorithm2is
always faster than Algorithm 0 and does not depend
(or does it very mildly) on the numberNNof
points in the window. In fact, the dependency
rather concerns the polynomial degreenn, with
improving performances asnnincreases. Similar
trends are also shown by Algorithm1,
although it is generally slower than the standard
matrix multiplication. However, and going back to
the results of Figure5, the slower
time is rewarded by an increase in accuracy by
orders of magnitude. For instance, givenn=8n=8andNNbetween 100 and 1000, an increase in
computational time ofΔ​T1,rel≈0.3−0.7\Delta T_{1,\mathrm{rel}}\approx 0.3-0.7is paid
off by an increase in accuracy of 8 orders of
magnitude.

## 5Conclusion

In this work we have addressed the problem of efficiently and accurately computing local polynomial smoothing via the calculation of fitting and differentiation matrices. While they can be expressed in closed form through standard least-squares formulations, direct implementations based on monomial bases and matrix multiplication are known to suffer from numerical instability and unfavorable scaling, particularly for large window lengths and moderate-to-high polynomial degrees.

By reformulating the problem in terms of discrete orthogonal (Chebyshev) polynomials, we have derived an explicit representation of the fitting matrix𝑨n\bm{A}_{n}. Two numerical algorithms have been presented: a fully recursive approach optimized for numerical accuracy (Algorithm1), and a buffer-based variant designed to minimize computational overhead (Algorithm2). Both algorithms make use of the recursive properties of the orthogonal polynomials and the bisymmetric properties of𝑨n\bm{A}_{n}to reduce memory usage and the number of operations required for its evaluation. The same theoretical background also provides an efficient method to recursively increase the degree of the polynomial fitnn.

A detailed performance study demonstrates that the proposed methods substantially improve numerical accuracy with respect to standard Vandermonde-based matrix multiplication, especially as the polynomial degree increases. In particular, the accuracy-optimized algorithm achieves improvements of several orders of magnitude in regimes relevant to high-resolution spectral analysis. At the same time, the buffer-based implementation consistently outperforms direct matrix multiplication in execution time, with only a mild dependence on the window size and increasingly favorable scaling for higher polynomial degrees.

These properties make the proposed approach well suited for large-scale applications such as axion dark matter searches. In this context, repeated polynomial fitting is required by algorithms that optimize the Savitzky–Golay parameters in order to extract narrow-band signals from slowly varying backgrounds, while avoiding distortions that could mimic or obscure a physical signal.

The present work assumes uniformly spaced data and equal weighting of samples, as is standard in Savitzky–Golay filtering. Extensions to weighted least-squares formulations or non-uniform sampling represent natural directions for future research.

## Acknowledgments

The author acknowledges support from the Knut and
Alice Wallenberg Foundation and Olle Engkvists
Foundation.

The author would like to thank Prof. Jan Conrad
for helpful discussions and valuable insights that
contributed to this work.

The author also acknowledge the support of the
ALPHA Collaboration, whose collaborative
environment was essential to this study.

## References
- [1]D. Acharya, A. Rani, S. Agarwal, and V. Singh(2016)Application of adaptive savitzky–golay filter for eeg signal processing.Perspectives in Science8,pp. 677–679.External Links:ISSN 2213-0209,DocumentCited by:§1.
- [2]D. Adamset al.(Eds.)(2021)Axion Dark Matter.CERN Yellow Reports: School Proceedings, Vol.1,CERN,Geneva.External Links:DocumentCited by:§1.
- [3]S. Agarwal, A. Rani, V. Singh, and A. Mittal(2017-07)EEG signal enhancement using cascaded s-golay filter.Biomedical Signal Processing and Control36,pp. 194–204.Cited by:§1.
- [4]D. K. Agustika, M. R. Nawawi, R. Prasetyowati, S. H. Hidayat, D. D. Iliescu, and M. S. Leeson(2022)Savitzky-golay parameter optimization by using linear discriminant analysis for ftir spectra.In2022 IEEE 7th Forum on Research and Technologies for Society and Industry Innovation (RTSI),Vol.,pp. 123–128.External Links:DocumentCited by:§1,§1.
- [5]J. Billardet al.(2022)Direct detection of dark matter – APPEC committee report.J. Phys. G49(4),pp. 040501.External Links:Document,2104.07634Cited by:§1.
- [6]Root-project/root: v6.18/02External Links:Document,LinkCited by:§4.
- [7]P. L. Chebyshev(1853)Théorie des mécanismes connus sous le nom de parallélogrammes.Imprimerie de l’Académie Impériale des Sciences,St. Petersbourg(french).Note:ETH-Bibliothek Zürich, Rar 23506. Public Domain MarkExternal Links:LinkCited by:§1,§2.3.
- [8]R. B. Cleveland, W. S. Cleveland, J. E. McRae, and I. Terpenning(1990)STL: a seasonal-trend decomposition procedure based on loess (with discussion).Journal of Official Statistics6,pp. 3–73.Cited by:§1.
- [9]W. S. Cleveland and S. J. Devlin(1988)Locally weighted regression: an approach to regression analysis by local fitting.Journal of the American Statistical Association83(403),pp. 596–610.Cited by:§1.
- [10]W. S. Cleveland(1979)Robust locally weighted regression and smoothing scatterplots.Journal of the American Statistical Association74(368),pp. 829–836.External Links:DocumentCited by:§1.
- [11]A. C. den Brinker(2021)Controlled accuracy for discrete chebyshev polynomials.In2020 28th European Signal Processing Conference (EUSIPCO),pp. 2279–2283.External Links:DocumentCited by:§1,§2.3.
- [12]M. Dine, W. Fischler, and M. Srednicki(1981)A Simple Solution to the Strong CP Problem with a Harmless Axion.Phys. Lett. B104,pp. 199–202.External Links:DocumentCited by:§1.
- [13]P. G. Guest(1961)Numerical methods of curve fitting.Cambridge University Press.Cited by:§2.2,§2.3,§2.3.
- [14]S. Hargittai(2005)Savitzky-golay least-squares polynomial filters in ecg signal processing.InComputers in Cardiology, 2005,Vol.,pp. 763–766.External Links:DocumentCited by:§1.
- [15]A.C. Harnden-Gillis, L.G.I. Bennett, and B.J. Lewis(1994)Experiments and analysis of fission product release in heu-fuelled slowpoke-2 reactors.Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment345(3),pp. 520–527.External Links:ISSN 0168-9002,DocumentCited by:§1.
- [16]I. G. Irastorza and J. Redondo(2018)New experimental approaches in the search for axion-like particles.Prog. Part. Nucl. Phys.102,pp. 89–159.External Links:Document,1801.08127Cited by:§1.
- [17]I. G. Irastorza(2021)Laboratory searches for galactic axions.Rept. Prog. Phys.84(10),pp. 106901.External Links:Document,2103.12400Cited by:§1.
- [18]P. Jönsson and L. Eklundh(2004)TIMESAT—a program for analyzing time-series of satellite sensor data.Computers & Geosciences30(8),pp. 833–845.External Links:ISSN 0098-3004,Document,LinkCited by:§1.
- [19]H. Kennedy(2015-11)Recursive digital filters with tunable lag and lead characteristics for proportional-differential control.IEEE Transactions on Control Systems Technology23(6),pp. 2369–2374.Cited by:§1.
- [20]V. Kher, G. Khajuria, P. Prabhat, M. Kohli, and V. K. Madan(2018)Application of higham and savitzky-golay filters to nuclear spectra.InSoft Computing Applications,V. E. Balas, L. C. Jain, and M. M. Balas (Eds.),Cham,pp. 487–496.External Links:ISBN 978-3-319-62521-8Cited by:§1.
- [21]J. E. Kim(1979)Weak Interaction Singlet and Strong CP Invariance.Phys. Rev. Lett.43,pp. 103.External Links:DocumentCited by:§1.
- [22]N. R. Koluguri, G. N. Meenakshi, and P. K. Ghosh(2017-06)Spectrogram enhancement using multiple window savitzky-golay (mwsg) filter for robust bird sound detection.IEEE/ACM Transactions on Audio, Speech, and Language Processing25(6),pp. 1183–1192.Cited by:§1.
- [23]S. R. Krishnan, M. Magimai-Doss, and C. S. Seelamantula(2013-03)A savitzky-golay filtering perspective of dynamic feature computation.IEEE Signal Processing Letters20(3),pp. 281–284.Cited by:§1.
- [24]S. R. Krishnan and C. S. Seelamantula(2013)On the selection of optimum savitzky-golay filters.IEEE Transactions on Signal Processing61(2),pp. 380–391.External Links:DocumentCited by:§1,§1.
- [25]D. J. E. Marsh, I. G. Irastorza, and J. Redondo (Eds.)(2022)The Physics of Axions.Springer,Cham.External Links:DocumentCited by:§1.
- [26]Y. Menget al.(2014-12)A modified empirical mode decomposition algorithm in tdlas for gas detection.IEEE Photonics Journal6(1).Cited by:§1.
- [27]A. J. Millaret al.(2023)Searching for dark matter with plasma haloscopes.Phys. Rev. D107(5),pp. 055013.External Links:2210.00017,DocumentCited by:§1.
- [28]A. F. Nikiforov, V. B. Uvarov, and S. K. Suslov(2012)Classical orthogonal polynomials of a discrete variable.Springer Berlin,Heidelberg.External Links:ISBN 978-3642747502,LinkCited by:§2.3.
- [29]E. N. Nishida, O. O. Dutra, L. H. C. Ferreira, and G. D. Colletta(2017-05)Application of savitzky-golay digital differentiator for qrs complex detection in an electrocardiographic monitoring system.InProceedings of the IEEE International Symposium on Medical Measurements and Applications (MeMeA),pp. 233–238.Cited by:§1.
- [30]R. D. Peccei and H. R. Quinn(1977)Constraints Imposed by CP Conservation in the Presence of Instantons.Phys. Rev. D16,pp. 1791–1797.External Links:DocumentCited by:§1.
- [31]R. D. Peccei and H. R. Quinn(1977)CP Conservation in the Presence of Instantons.Phys. Rev. Lett.38,pp. 1440–1443.External Links:DocumentCited by:§1.
- [32]Md. A. Rahman, M. A. Rashid, and M. Ahmad(2019)Selecting the optimal conditions of savitzky–golay filter for fnirs signal.Biocybernetics and Biomedical Engineering39(3),pp. 624–637.External Links:ISSN 0208-5216,Document,LinkCited by:§1.
- [33]S. Rivolo, E. Nagel, N. P. Smith, and J. Lee(2014-08)Automatic selection of optimal savitzky-golay filter parameters for coronary wave intensity analysis.InProceedings of the 36th Annual International Conference of the IEEE Engineering in Medicine and Biology Society,pp. 5056–5059.Cited by:§1.
- [34]S. Rivoloet al.(2017-05)Accurate and standardized coronary wave intensity analysis.IEEE Transactions on Biomedical Engineering64(5),pp. 1187–1196.Cited by:§1.
- [35]A. G. Rosso(2026)Polfit(Website)External Links:LinkCited by:§1.
- [36]M. Sadeghi, F. Behnia, and R. Amiri(2020)Window selection of the savitzky–golay filters for signal recovery from noisy measurements.IEEE Transactions on Instrumentation and Measurement69(8),pp. 5418–5427.External Links:DocumentCited by:§1.
- [37]R. Sameni(2017-04)Online filtering using piecewise smoothness priors: application to normal and abnormal electrocardiogram denoising.Signal Processing133,pp. 52–63.Cited by:§1.
- [38]A. Savitzky and M.J.E. Golay(1964-07)Smoothing and differentiation of data by simplified least squares procedures.Analytical Chemistry36(8),pp. 1627–1639.External Links:ISSN 0003-2700,Document,LinkCited by:§1.
- [39]S. Schmidet al.(2022)Directional axion detection.Phys. Rev. D105(8),pp. 083022.External Links:Document,2202.08209Cited by:§1.
- [40]R. C. Schneider and K. Kovar(2003)Analysis of ecstasy tablets: comparison of reflectance and transmittance near infrared spectroscopy.Forensic Science International134(2),pp. 187–195.External Links:ISSN 0379-0738,DocumentCited by:§1.
- [41]S. Seifzadeh, M. Rostami, A. Ghodsi, and F. Karray(2011)Parameter selection for smoothing splines using stein’s unbiased risk estimator.InThe 2011 International Joint Conference on Neural Networks,pp. 2733–2740.External Links:DocumentCited by:§1,§1.
- [42]Y. K. Semertzidis and S. Youn(2019)Axion dark matter: How to see it?.SciPost Phys. Proc.2,pp. 021.External Links:Document,1904.04168Cited by:§1.
- [43]J. Seo, H. Ma, and T. K. Saha(2018-08)On savitzky-golay filtering for online condition monitoring of transformer on-load tap changer.IEEE Transactions on Power Delivery33(4),pp. 1689–1698.Cited by:§1.
- [44]M. A. Shifman, A. I. Vainshtein, and V. I. Zakharov(1978)Can Confinement Ensure Natural CP Invariance of Strong Interactions?.Phys. Lett. B78,pp. 443–446.External Links:DocumentCited by:§1.
- [45]J. Shohat(1934)Théorie générale des polynômes orthogonaux de tchebichef.Mémorial des sciences mathématiques, Vol.66,Gauthier-Villars.External Links:LinkCited by:§2.2,§2.3.
- [46]S. Sibiya, S. Ramroop, S. Melesse, and N. Mbatha(2026)Meteorological drought trend analysis and forecasting using a hybrid sg-ceemdan-arima-lstm model based on spi from rain gauge data.Natural Hazards and Earth System Sciences26(1),pp. 315–342.External Links:Link,DocumentCited by:§1.
- [47]P. Sikivie(1983)Experimental Tests of the Invisible Axion.Phys. Rev. Lett.51,pp. 1415–1417.Note:[Erratum: Phys.Rev.Lett. 52, 695 (1984)]External Links:DocumentCited by:§1.
- [48]P. Sikivie(1985)Detection Rates for ’Invisible’ Axion Searches.Phys. Rev. D32,pp. 2988–2991.Note:[Erratum: Phys.Rev.D 36, 974 (1987)]External Links:DocumentCited by:§1.
- [49]C. M. Stein(1981)Estimation of the Mean of a Multivariate Normal Distribution.The Annals of Statistics9(6),pp. 1135 – 1151.External Links:Document,LinkCited by:§1.
- [50]D. Suescún-Díaz, H. F. Bonilla-Londoño, and J. H. Figueroa-Jiménez(2016-07)Savitzky-golay filter for reactivity calculation.Journal of Nuclear Science and Technology53(7),pp. 944–950.Cited by:§1.
- [51]G. Szegö(1939)Orthogonal polynomials.American Mathematical Society,Providence, Rhode Island, USA.External Links:LinkCited by:§2.3.
- [52]P.L. Tchebychef(1864)Sur l’interpolation.Zapiski Akademii Nauk4.Cited by:§1,§2.3.
- [53]K. Torabi, A. Karami, S. T. Balke, and T. C. Schunk(2001)Quantitative ftir detection in size-exclusion chromatography.Journal of Chromatography A910(1),pp. 19–30.External Links:ISSN 0021-9673,Document,LinkCited by:§1.
- [54]G. Vivó-Truyols and P. J. Schoenmakers(2006)Automatic selection of optimal savitzky–golay smoothing.Analytical Chemistry78(13),pp. 4598–4608.External Links:Document,ISSN 0003-2700,LinkCited by:§1,§1.
- [55]S. Weinberg(1978)A New Light Boson?.Phys. Rev. Lett.40,pp. 223–226.External Links:DocumentCited by:§1.
- [56]F. Wilczek(1978)Problem of Strong P and T Invariance in the Presence of Instantons.Phys. Rev. Lett.40,pp. 279–282.External Links:DocumentCited by:§1.
- [57]W. Yang and W. Qi(2017-03)Spatial-temporal dynamic monitoring of vegetation recovery after the wenchuan earthquake.IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing10(3),pp. 868–876.Cited by:§1.
- [58]Z. Yi, M. Buschmann, and B. R. Safdi(2023)Directional detection of axion dark matter.Phys. Rev. D108(4),pp. 043024.External Links:Document,2301.10789Cited by:§1.
- [59]A. R. Zhitnitsky(1980)On Possible Suppression of the Axion Hadron Interactions. (In Russian).Sov. J. Nucl. Phys.31,pp. 260.Cited by:§1.
- [60]H. Ziegler(1981)Properties of digital smoothing polynomial (dispo) filters.Applied Spectroscopy35(1),pp. 88–92.External Links:DocumentCited by:§1.
- [61]B. Zimmermann and A. Kohler(2013)Optimizing savitzky–golay parameters for improving spectral resolution and quantification in infrared spectroscopy.Applied Spectroscopy67(8),pp. 892–902.External Links:Document,ISSN 0003-7028Cited by:§1,§1.

## 


- 


Major funding support from
