# A note on the minimal pairwise distance in optimal Lennard-Jones $N$-body clusters

**arXiv ID**: 2511.15008v1
**Authors**: Michael K. -H. Kiessling, David J. Wales
**Published**: 2025-11-19
**Categories**: physics.atm-clus, math-ph
**Comments**: Accepted (2025) for publication in: Molecular Physics
**HTML URL**: https://arxiv.org/html/2511.15008v1

## Abstract

Good a-priori bounds on the smallest pairwise distance $r_{\rm{min}}(\mbox{LJ}_N^{\rm{gmin}})$ for a three-dimensional (3D) Lennard-Jones $N$-body cluster of globally minimal energy can significantly reduce the computational search space in the NP-hard problem to find this configuration. In this contribution the virial theorem is exploited for this purpose. We prove that if a configuration ${C}^{(N)}$ is a member of $\mbox{LJ}_N^{\rm{equ}}$ (the stationary points), then $r_{\rm{min}}({C}^{(N)}) \leq r_{\rm{min}}(\mbox{LJ}_2^{\rm{gmin}})$. It is also shown that if ${C}^{(N)}\in$ LJ$_N^{\rm{gmin}}\subset$ LJ$_N^{\rm{equ}}$, equality holds if and only if $N\in\{2,3,4\}$. We conjecture that $r_{\rm{min}}(\mbox{LJ}_N^{\rm{gmin}}) >1$ in units for which $r_{\rm{min}}(\mbox{LJ}_2^{\rm{gmin}})= 2^\frac16 \approx 1.122462048$. This conjectured lower bound, if correct, would improve the best lower bound currently known, $r_{\rm{min}}(\mbox{LJ}_N^{\rm{gmin}})\geq 0.767764$, by about 25$\%$. In these units the smallest minimal pair distance found through numerical searches for LJ$_N^{\rm{gmin}}$ with $N\leq 1000$ is $r_{\rm{min}}(\mbox{LJ}_{923}^{\rm{gmin}}) \approx 1.01361$, so the conjectured lower bound would presumably be close to optimal. From the virial theorem we obtain an identity for any ${C}^{(N)}\in \mbox{LJ}_N^{\rm{equ}}$, which expresses $r_{\rm{min}}({C}^{(N)})$ in terms of the distribution of relative distances in ${C}^{(N)}$. This result reveals interesting connections with the Erdős distance, and related problems.

## Full Text

A note on the minimal pairwise distance in optimal Lennard-Jones 𝑁-body clusters∗

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2511.15008v1 [physics.atm-clus] 19 Nov 2025

## A note on the minimal pairwise distance in
optimal Lennard-JonesNN-body clusters∗Michael K.-H. Kiessling1and David J. Wales2
1Department of Mathematics,
Rutgers, The State University of New Jersey
110 Frelinghuysen Rd., Piscataway, NJ 08854, USA
email: miki@math.rutgers.edu
2Yusuf Hamied Department of Chemistry, Lensfield Road, Cambridge CB2 1EW, UK
email: dw34@cam.ac.uk

## Abstract

Good a-priori bounds on the smallest pairwise distancermin​(LJNgmin)r_{\mbox{\tiny{min}}}(\mbox{LJ}_{N}^{\rm{gmin}})for a three-dimensional (3D) Lennard-JonesNN-body cluster of
globally minimal energy can significantly reduce the computational search space in the NP-hard problem to find this configuration.
In this contribution the virial theorem is exploited for this purpose.
We prove that if a configuration𝒞(N){\cal C}^{(N)}is a member ofLJNequ\mbox{LJ}_{N}^{\rm{equ}}(the stationary points), thenrmin​(𝒞(N))≤rmin​(LJ2gmin)r_{\mbox{\tiny{min}}}({\cal C}^{(N)})\leq r_{\mbox{\tiny{min}}}(\mbox{LJ}_{2}^{\rm{gmin}}).
It is also shown that if𝒞(N)∈{\cal C}^{(N)}\inLJ⊂Ngmin{}_{N}^{\rm{gmin}}\subsetLJequN{}_{N}^{\rm{equ}}, equality holds if and only ifN∈{2,3,4}N\in\{2,3,4\}.
We conjecture thatrmin​(LJNgmin)>1r_{\mbox{\tiny{min}}}(\mbox{LJ}_{N}^{\rm{gmin}})>1in units for whichrmin​(LJ2gmin)=216≈1.122462048r_{\mbox{\tiny{min}}}(\mbox{LJ}_{2}^{\rm{gmin}})=2^{\frac{1}{6}}\approx 1.122462048.
This conjectured lower bound, if correct, would improve the best lower bound currently known,rmin​(LJNgmin)≥0.767764r_{\mbox{\tiny{min}}}(\mbox{LJ}_{N}^{\rm{gmin}})\geq 0.767764, by about 25%.
In these units the smallest minimal pair distance found through numerical searches for LJgminN{}_{N}^{\rm{gmin}}withN≤1000N\leq 1000isrmin​(LJ923gmin)≈1.01361r_{\mbox{\tiny{min}}}(\mbox{LJ}_{923}^{\rm{gmin}})\approx 1.01361, so the conjectured lower bound would presumably be close to optimal.
From the virial theorem we obtain an identity for any𝒞(N)∈LJNequ{\cal C}^{(N)}\in\mbox{LJ}_{N}^{\rm{equ}}, which expressesrmin​(𝒞(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)})in terms of the distribution of relative distances in𝒞(N){\cal C}^{(N)}.
This result reveals interesting connections with the Erdős distance, and related problems.

∗Dedicated to Peter Schwerdtfeger on his 70th birthday.

©(2025) The authors. Reproduction, in its entirety, for non-commercial purposes is permitted.

## 1Introduction

Since the Lennard-Jones potential was introduced, just over a century ago, it has found widespread applications in diverse fields, thanks to the realistic physical behaviour captured by a simple functional form[55].
New results and improvements are still being presented[52,53],
including investigations of the lattice sums and stabilities for bulk systems[5,6,54]considered by Lennard-Jones himself.
In this article we draw attention to some intriguing geometrical aspects ofNN-body clusters with Lennard-Jones pair interactions.

Consider a configuration𝒞(N):={𝒓1,…,𝒓N}⊂ℝ3{\cal C}^{(N)}:=\{{\boldsymbol{r}}_{1},...,{\boldsymbol{r}}_{N}\}\subset{\mathbb{R}}^{3}ofN≥2N\geq 2distinct locations inℝ3{\mathbb{R}}^{3}of classical point particles (representing atoms).
For any pair of natural numbersi≠ji\neq j, each no larger thanNN,
the Euclidean distance between the particle located at𝒓i{\boldsymbol{r}}_{i}and the one at𝒓j{\boldsymbol{r}}_{j}is denoted|𝒓i−𝒓j|∈(0,∞)|{\boldsymbol{r}}_{i}-{\boldsymbol{r}}_{j}|\in(0,\infty).

Ifr>0r>0stands for the Euclidean distance of any such pair of particles under consideration, we define the Lennard-Jones interaction energy[25,26,27,28,24]asVLJ(r):=1r12−1r6;V_{\mbox{\tiny{LJ}}}(r):=\frac{1}{r^{12}}-\frac{1}{r^{6}};(1)

by a simple rescaling of distance and energy units one can recover any of the other expressions of a Lennard-Jones pair energy that are commonly used.
The total Lennard-Jones energy for a configuration ofN≥2N\geq 2atoms, denotedW​(𝒞(N))W({\cal C}^{(N)}), is given byW​(𝒞(N)):=∑∑1≤i<j≤NVLJ​(|𝒓i−𝒓j|).W({\cal C}^{(N)}):=\sum\!\!\sum_{\thinspace 1\leq i<j\leq N}V_{\mbox{\tiny{LJ}}}(|{\boldsymbol{r}}_{i}-{\boldsymbol{r}}_{j}|).(2)

A configuration𝒞(N){\cal C}^{(N)}may or may not evolve in time under Newtonian dynamics, but as long as theNNatoms remain in a bounded region for all time (after at most transforming to a Galilei frame in which the total momentum of the configuration vanishes) one speaks of a boundNN-body cluster.
We denote the family of allNN-body clusters bound by Lennard-Jones interactions as LJN.

Here we are interested in the subsets LJequN{}_{N}^{\rm{equ}}and LJgminN{}_{N}^{\rm{gmin}}of LJN, where LJgminN{}_{N}^{\rm{gmin}}denotes the global minimizers ofW​(𝒞(N))W({\cal C}^{(N)}), while LJequN{}_{N}^{\rm{equ}}denotes all stationary points ofW​(𝒞(N))W({\cal C}^{(N)}); the latter are force equilibria.
It is easy to show that for eachN≥2N\geq 2there exists a configuration𝒞gmin(N){\cal C}^{(N)}_{\rm gmin}, theoptimalNN-particle Lennard-Jones cluster, which
minimizes the total Lennard-Jones energyW​(𝒞(N))W({\cal C}^{(N)})globally over the set of allNN-point configurations.
Thus, LJgminN{}_{N}^{\rm{gmin}}is not empty whenN≥2N\geq 2, and therefore
LJequN{}_{N}^{\rm{equ}}is not empty a forteriori.

The energy of any configuration is invariant to all permutations of identical particles, inversion through the origin, and overall translation and rotation.
Structures that differ only by an overall translation or rotation are easily identified;
rotational alignment can be achieved using Lagrange multipliers[31]or quaternions[33,9].
Usually also the permutation-inversion isomers of each stationary point are lumped together for sampling purposes, since the number of distinct structures is known analytically from the point group[20,7,74].
The GMIN, OPTIM, and PATHSAMPLE programs for exploring energy landscapes employ an iterative scheme to perform optimal alignment between different local minima[72], based on the shortest augmenting path algorithm[29]for the permutational part.
This analysis provides the shortest Euclidean distance between permutational isomers of different structures, while a standard orientation scheme identifies permutation-inversion isomers in an initial filter[72,21].
For the present application, alignment is not an issue, and we can use any permutation-inversion isomer of the global minimum.

For small enoughNNthe set LJgminN{}_{N}^{\rm{gmin}}has only one element (aside from permutation-inversion isomers with the same energy), but we are not aware of a proof of uniqueness for global minimum Lennard-Jones clusters in 3D with generalNN.
In contrast, LJequN{}_{N}^{\rm{equ}}, the set of all stationary points, has almost always more than one element, and is expected to increase exponentially in size withNN[61,62,73].
The only exception, whenD=3D=3, is whenN=2N=2; it is readily seen that LJ=2equ{}_{2}^{\rm{equ}}=LJgmin2{}_{2}^{\rm{gmin}}.
Only whenD=1D=1is LJ=Nequ{}_{N}^{\rm{equ}}=LJgminN{}_{N}^{\rm{gmin}}for allN≥2N\geq 2.

Focusing on the 3D problem, we recall that forN∈{2,3,4,5}N\in\{2,3,4,5\}the optimal structure LJgminN{}_{N}^{\rm{gmin}}can be established rigorously, but for largerNNthe problem requires numerical searches on a computer, and even with the fastest available algorithms the problem becomes increasingly difficult asNNincreases because LJminN{}_{N}^{\rm{min}}, the set of all local energy minimizing Lennard-Jones clusters, appears to grow exponentially fast withNN[61,62,73], as mentioned above.
In fact, the problem of finding LJgminN{}_{N}^{\rm{gmin}}has been proved to be NP-hard[75].

In the absence of a sure-fire algorithm that locates LJgminN{}_{N}^{\rm{gmin}}in polynomial time, probabilistic searches are used.
Good a-priori bounds on the search space are desirable to eliminate as many irrelevant configurations as possible.
One important quantity that bounds the size of the search space is the minimal pairwise distancermin​(LJNgmin)r_{\mbox{\tiny{min}}}(\mbox{LJ}_{N}^{\rm{gmin}})that can occur in anyNN-body cluster global minimum.
It has been shown first in[79]that there is anNN-independent nontrivial lower bound tormin​(LJNgmin)r_{\mbox{\tiny{min}}}(\mbox{LJ}_{N}^{\rm{gmin}}), namely (rescaled into our units)rmin​(LJNgmin)≥1/256≈0.561231r_{\mbox{\tiny{min}}}(\mbox{LJ}_{N}^{\rm{gmin}})\geq 1/2^{\frac{5}{6}}\approx 0.561231.
In subsequent papers, first[71], then[50], and more recently[80], the theoretical lower bound has been improved, with the currently best estimatermin​(LJNgmin)≥0.767764r_{\mbox{\tiny{min}}}(\mbox{LJ}_{N}^{\rm{gmin}})\geq 0.767764[80].
The important question is: What is the optimal lower bound?

## 2The minimal pair distance in LJequN{}_{N}^{\mbox{\small{equ}}}and in LJgminN{}_{N}^{\mbox{\small{gmin}}}

ForN≥2N\geq 2the minimal distance among all pairs of particles in an
equilibrium configuration𝒞(N)∈{\cal C}^{(N)}\inLJequN{}_{N}^{\rm{equ}}is defined asrmin​(𝒞(N)):=min{𝒓i≠𝒓j}⊂𝒞(N)⁡|𝒓i−𝒓j|.r_{\mbox{\tiny{min}}}({\cal C}^{(N)}):=\min_{\{{\boldsymbol{r}}_{i}\neq{\boldsymbol{r}}_{j}\}\subset{\cal C}^{(N)}}|{\boldsymbol{r}}_{i}-{\boldsymbol{r}}_{j}|.(3)

In particular, whenN=2N=2the equilibrium problem is trivial, as manifestly there is only a single equilibrium configuration, which therefore is the global energy minimizer; i.e.,{𝒞gmin(2)}=\{{\cal C}^{(2)}_{\rm gmin}\}=LJequ2{}_{2}^{\rm equ}, and
the particles in𝒞gmin(2){\cal C}^{(2)}_{\rm gmin}are separated by the distancermin​(𝒞gmin(2))=216≈1.122462048.r_{\mbox{\tiny{min}}}({\cal C}^{(2)}_{\rm gmin})=2^{\frac{1}{6}}\approx 1.122462048.(4)

This dimer equilibrium configuration can be used as a building block to construct the global minima forN∈{3,4}N\in\{3,4\}, namely the equilateral triangle and the regular tetrahedral configurations, in which all pairwise distances are the same, and equal tormin​(𝒞gmin(2))r_{\mbox{\tiny{min}}}({\cal C}^{(2)}_{\rm gmin}).
Thus, if𝒞(N)∈{\cal C}^{(N)}\inLJgminN{}_{N}^{\rm gmin}, thenrmin​(𝒞(N))=216forN∈{2,3,4}.\qquad r_{\mbox{\tiny{min}}}({\cal C}^{(N)})=2^{\frac{1}{6}}\quad\mbox{for}\quad N\in\{2,3,4\}.(5)

It is an elementary geometrical fact that these global LJ energy minimizers forN∈{2,3,4}N\in\{2,3,4\}are the only LJ equilibrium configurations for which all pairs of particles in the configuration exhibit the same distance, in fact the same distance as in the LJgmin2{}_{2}^{\rm gmin}.
We will use this fact to show that these are the only three LJ equilibrium configurations inℝ3{\mathbb{R}}^{3}for which theN=2N=2equilibrium distance is the minimal pairwise distance.

A minimal interatomic distance below the pair equilibrium value of21/62^{1/6}is expected for structures based on icosahedra, since the radial distance for a regular icosahedron is1+ϕ2/2≈0.951\sqrt{1+\phi^{2}}/2\approx 0.951times the edge length, whereϕ=(5+1)/2\phi=(\sqrt{5}+1)/2, and21/6​1+ϕ2/2≈1.06752^{1/6}\sqrt{1+\phi^{2}}/2\approx 1.0675.
We will prove that the dimer equilibrium value of21/62^{1/6}is in fact a strict upper bound onrmin​(𝒞(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)})for all𝒞(N)∈{\cal C}^{(N)}\inLJequN{}_{N}^{\rm equ}withN>4N>4.

For our proofs we will invoke the virial theorem.

## 2.1The virial identity

For𝒞(N)∈{\cal C}^{(N)}\inLJequN{}_{N}^{\rm equ}we write𝒞(N)=:{𝒓1equ,…,𝒓Nequ}{\cal C}^{(N)}=:\{{\boldsymbol{r}}_{1}^{\mbox{\tiny{equ}}},...,{\boldsymbol{r}}_{N}^{\mbox{\tiny{equ}}}\}.
For such Lennard-Jones equilibrium configurations (stationary points) the virial theorem yields2​∑∑1≤i<j≤N1|𝒓iequ−𝒓jequ|12=∑∑1≤i<j≤N1|𝒓iequ−𝒓jequ|6.2\,\sum\!\!\sum_{\thinspace 1\leq i<j\leq N}\frac{1}{|{\boldsymbol{r}}_{i}^{\mbox{\tiny{equ}}}-{\boldsymbol{r}}_{j}^{\mbox{\tiny{equ}}}|^{12}}=\sum\!\!\sum_{\thinspace 1\leq i<j\leq N}\frac{1}{|{\boldsymbol{r}}_{i}^{\mbox{\tiny{equ}}}-{\boldsymbol{r}}_{j}^{\mbox{\tiny{equ}}}|^{6}}.(6)

Since2=rmin​(𝒞gmin(2))62=r_{\mbox{\tiny{min}}}({\cal C}^{(2)}_{\rm gmin})^{6}, by homogeneity
the virial theorem yields for allNN-particle Lennard-Jones equilibrium configurations the identityrmin​(𝒞(N))=rmin​(𝒞(2))​(R​(𝒞(N))A​(𝒞(N)))16,r_{\mbox{\tiny{min}}}({\cal C}^{(N)})=r_{\mbox{\tiny{min}}}({\cal C}^{(2)})\left(\frac{R({\cal C}^{(N)})}{A({\cal C}^{(N)})}\right)^{\frac{1}{6}},(7)

where𝒞(2)=𝒞gmin(2){\cal C}^{(2)}={\cal C}^{(2)}_{\rm gmin},R​(𝒞(N)):=∑∑1≤i<j≤N(rmin​(𝒞(N))|𝒓iequ−𝒓jequ|)12R({\cal C}^{(N)}):=\sum\!\!\sum_{\thinspace 1\leq i<j\leq N}\left(\frac{r_{\mbox{\tiny{min}}}({\cal C}^{(N)})}{|{\boldsymbol{r}}_{i}^{\mbox{\tiny{equ}}}-{\boldsymbol{r}}_{j}^{\mbox{\tiny{equ}}}|}\right)^{12}(8)

andA​(𝒞(N)):=∑∑1≤i<j≤N(rmin​(𝒞(N))|𝒓iequ−𝒓jequ|)6.A({\cal C}^{(N)}):=\sum\!\!\sum_{\thinspace 1\leq i<j\leq N}\left(\frac{r_{\mbox{\tiny{min}}}({\cal C}^{(N)})}{|{\boldsymbol{r}}_{i}^{\mbox{\tiny{equ}}}-{\boldsymbol{r}}_{j}^{\mbox{\tiny{equ}}}|}\right)^{6}.(9)

Note that (7) is simply a rewriting of the virial identity.
Indeed, sincermin​(𝒞(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)})can be cancelled from left and right side in (7),
one may wonder how this result provides insight intormin​(𝒞(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)})?
We now show how it is useful.

## 2.2Upper bound onrmin​(𝒞(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)})when𝒞(N)∈{\cal C}^{(N)}\inLJequN{}_{N}^{\rm{equ}}

Sincermin​(𝒞(N))≤|𝒓i−𝒓j|r_{\mbox{\tiny{min}}}({\cal C}^{(N)})\leq|{\boldsymbol{r}}_{i}-{\boldsymbol{r}}_{j}|for{𝒓i≠𝒓j}⊂𝒞(N)∈\{{\boldsymbol{r}}_{i}\neq{\boldsymbol{r}}_{j}\}\subset{\cal C}^{(N)}\inLJequN{}_{N}^{\rm{equ}},
and sincex12≤x6x^{12}\leq x^{6}for0<x≤10<x\leq 1, it follows thatR​(𝒞(N))≤A​(𝒞(N))R({\cal C}^{(N)})\leq A({\cal C}^{(N)}),
and so, for allN≥2N\geq 2, and any equilibrium configuration𝒞(N){\cal C}^{(N)}, we havermin​(𝒞(N))≤rmin​(𝒞gmin(2)).r_{\mbox{\tiny{min}}}({\cal C}^{(N)})\leq r_{\mbox{\tiny{min}}}({\cal C}^{(2)}_{\rm gmin}).(10)

Furthermore, thisNN-independent upper bound can be attained if and only if the distances between the particles in all pairs{𝒓i≠𝒓j}⊂𝒞(N)\{{\boldsymbol{r}}_{i}\neq{\boldsymbol{r}}_{j}\}\subset{\cal C}^{(N)}are identical, and therefore identical tormin​(𝒞(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)}),
in which caseA​(𝒞(N))=R​(𝒞(N))A({\cal C}^{(N)})=R({\cal C}^{(N)}).
We already know that this is the case for the global minima LJgminN{}_{N}^{\rm{gmin}}whenN∈{2,3,4}N\in\{2,3,4\}.
Moreover, we already noted the elementary geometrical fact that whenN>4N>4, then
there are noNNpoint configurations inℝ3{\mathbb{R}}^{3}in which all pairwise distances are the same.
However, when a distance|𝒓i−𝒓j|≠rmin​(𝒞(N))|{\boldsymbol{r}}_{i}-{\boldsymbol{r}}_{j}|\neq r_{\mbox{\tiny{min}}}({\cal C}^{(N)})for at least one pair(i≠j)(i\neq j),
thenrmin​(𝒞(N))/|𝒓iequ−𝒓jequ|<1{r_{\mbox{\tiny{min}}}({\cal C}^{(N)})}/{|{\boldsymbol{r}}_{i}^{\mbox{\tiny{equ}}}-{\boldsymbol{r}}_{j}^{\mbox{\tiny{equ}}}|}<1for that
pair, and sincex12<x6x^{12}<x^{6}whenx∈(0,1)x\in(0,1), we then have strict inequalityR​(𝒞(N))<A​(𝒞(N))R({\cal C}^{(N)})<A({\cal C}^{(N)}), which holds for any equilibrium configuration withN>4N>4.

Thus we have proved the following theorem.

Theorem:Consider the family{𝒞(N)}N≥2\left\{{\cal C}^{(N)}\right\}_{N\geq 2}of stationary points
of the Lennard-Jones energy given in equation (2), i.e. consider allNN-particle LJ equilibrium configurations.
ThenmaxN≥2⁡min{𝒓i≠𝒓j}⊂𝒞(N)⁡|𝒓i−𝒓j|=216,\max_{N\geq 2}\min_{\{{\boldsymbol{r}}_{i}\neq{\boldsymbol{r}}_{j}\}\subset{\cal C}^{(N)}}|{\boldsymbol{r}}_{i}-{\boldsymbol{r}}_{j}|=2^{\frac{1}{6}},(11)

and this maximum is attained if and only if𝒞(N)∈{\cal C}^{(N)}\inLJgminN{}_{N}^{\rm{gmin}}withN∈{2,3,4}N\in\{2,3,4\}.

## 2.3Conjectured lower bound forrmin​(𝒞(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)})when𝒞(N)∈{\cal C}^{(N)}\inLJgminN{}_{N}^{\rm{{gmin}}}

There is empirical evidence and theoretical plausibility for the

Conjecture:For allN≥2N\geq 2,if𝒞(N)∈{\cal C}^{(N)}\inLJgminN{}_{N}^{\rm{{gmin}}}inℝ3{\mathbb{R}}^{3}, thenrmin​(𝒞(N))≥1.r_{\mbox{\tiny{min}}}({\cal C}^{(N)})\geq 1.(12)

As to the empirical evidence for this Conjecture:
Inspecting first the list of putative LJNglobal energy minimizers at[68], which covers allN≤150N\leq 150, and then enlarging this list to allN≤1000N\leq 1000, we find that the smallest minimal distancermin​(𝒞gmin(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)}_{\rm gmin})occurs forN=923N=923, withrmin​(LJ923gmin)≈1.01361r_{\mbox{\tiny{min}}}(\mbox{LJ}_{923}^{\rm{gmin}})\approx 1.01361; see Figure1.

Figure1shows the minimum distance in theLJN\mathrm{LJ}_{N}clusters with lowest known energy as a function of size up to 1000 atoms.
The largest minimal pair distance occurs forN∈{2,3,4}N\in\{2,3,4\}, as proved earlier, and the smallest minimal distance observed in this range ofNNvalues occurs atN=923N=923, a centered Mackay icosahedron[36].
All the distances in this figure are larger than 1.01, supporting our Conjecture.
More important than the fact thatrmin​(𝒞gmin(N))>1r_{\mbox{\tiny{min}}}({\cal C}^{(N)}_{\rm gmin})>1for all2≤N≤10002\leq N\leq 1000is the following observation:
Although the range ofNNvalues is relatively small in this plot, Figure1visibly suggests that the monotonic decreasing (though not strictly decreasing) functionN↦minn≤N⁡rmin​(𝒞gmin(n))N\mapsto\min_{n\leq N}r_{\mbox{\tiny{min}}}({\cal C}^{(n)}_{\rm gmin}), which converges to the smallest possible minimal distance of any globally energy-minimizing LJNcluster, may well converge to a value larger than 1.
Of course this is only suggestive and does not prove that there is no value ofrmin​(𝒞gmin(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)}_{\rm gmin})smaller than 1 for someNNother than those inspected.Figure 1:Minimum distance in Lennard-Jones clusters with globally minimal energy in the size range from 2 to 1000 atoms.
The points are joined to guide the eye.
Structures based on the truncated cuboctahedron (O), the Leary tetrahedron (L)[35], and Marks decahedra (D)[40]are highlighted. In each case the minimum distance is significantly larger than for the neighbouring clusters based on Mackay icosahedra[36].

The plot also reveals some interesting, highly nonmonotonic, structure, which is related to the underlying cluster morphology.
For largerNNwe see minimum distances around 1.02, 1.04, and 1.08.
The smallest value corresponds to a distance involving the centre atom in structures based on a Mackay icosahedron[36], where there is a central 13-atom icosahedral motif.
Inspection of selected structures reveals that minimum distances around 1.04 come from icosahedral-based geometries where the centre atom is missing.
The minimum distance occurs for two atoms in the hollow 12-atom (approximately) icosahedral core.
Values around 1.08 come from the distance between the centre atom and a first shell neighbour in decahedral structures[23,40].
Here, the central motif is a centred 13-atom Ino decahedron[23].
These structural effects can be related to strain energy[13,14], which makes icosahedral packing unfavourable for larger clusters[78].
In fact, the compression around the central atom is reflected in the generally decreasing distance withNNfor the centred icosahedral structures, until we enter a size regime where alternative packings become more favourable[11].
Crystal lattice studies suggest that a a minimal distance value of≈1.09\approx 1.09is expected for very largeNNvalues.
However, before this limit is reached we expect to see structural competition punctuated by nonmonotonic excursions at particular sizes.
Entropic effects will also play a role at finite temperature, and have been investigated in previous work[11,47].
The vast majority of global minima up toN=1000N=1000can be described in terms of icosahedral packing schemes with Mackay or anti-Mackay overlayers[15,77,78].
The known exceptions are the truncated octahedron (N=38N=38), the Leary tetrahedron[35](N=98N=98) and structures based on Marks decahedra[40,49,78](N=75−77,102−104,187−192,236−238,650−664,682−691,754−762,815−823N=75-77,\ 102-104,\ 187-192,\ 236-238,\ 650-664,\ 682-691,\ 754-762,\ 815-823).
These discontinuities in packing all produce features at larger values of the minimum distance in Figure1.

Back to our Conjecture, in[34]we noted that there is also theoretical
evidence from studies of crystal structures in the thermodynamic limitN→∞N\to\infty, which we repeat here:
In[24]the minimal pair distance was computed for spatially unbounded simple cubic, bcc and fcc Lennard-Jones crystals, by minimizing their energy per monomer.
They found that the fcc crystal has the lowest energy per particle among these three regular lattices, and for a long time it was thought that fcc is the optimalcrystal structurein the limitN→∞N\to\infty.
Now we know that fcc is the optimalstandard latticestructure, with a minimal pair distance that can then be computed from the results in[24]asrminfcc≈1.090172.r_{\mbox{\tiny{min}}}^{\mbox{\tiny{fcc}}}\approx 1.090172.(13)

However, recently it was found empirically[86], and then proved rigorously[2], that the hcp structure is the true crystalline ground state configuration in the thermodynamic limit.
Note that the hcp crystal is not a regular lattice in the same sense as fcc, bcc, and simple cubic crystals, because a two atom basis is required for the repeated unit, with two atomic environments.
Using the results of[5], the minimal pair distance in the optimal crystal structure can be computed to berminhcp≈1.090167,r_{\mbox{\tiny{min}}}^{\mbox{\tiny{hcp}}}\approx 1.090167,(14)

which is just a tiny bit smaller thanrminfccr_{\mbox{\tiny{min}}}^{\mbox{\tiny{fcc}}}.
It is clear thatrminhcp>rmin​(𝒞gmin(923))r_{\mbox{\tiny{min}}}^{\mbox{\tiny{hcp}}}>r_{\mbox{\tiny{min}}}({\cal C}^{(923)}_{\rm gmin}).

Numerical simulations suggest that with growingNNthe LJNglobal minimum configurations do converge (on nested compact subsets ofℝ3{\mathbb{R}}^{3}) to an hcp lattice structure (after for a long while fcc seemed to be the attractor).
If proven true, this then means thatrmin​(𝒞gmin(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)}_{\rm gmin})has to converge to≈1.09\approx 1.09(see above).
This in turn would prove that eventually, for large enoughNN, no minimal pairwise distance will be smaller than the conjectured smallest possible pairwise distance.
A counterexample would therefore have to be found below some “large enoughNN.”

We also emphasize that we are considering the global minimum energy configurations, and smaller distances could occur in local minima, or in a saddle point configuration.
These possibilities are interesting, but beyond the scope of the present note.
However, we have checked the minimum distances for some local minima in the size range up toLJ1000\mathrm{LJ}_{1000}and confirmed that some slightly smaller pair distances do occur.

We note that for the sequence of centered Mackay icosahedra the minimal pairwise distancermin​(N)r_{\rm min}(N)decreases monotonically whenN∈{13,55,147,309,561,923}N\in\{13,55,147,309,561,923\}.
Since the strain of icosahedral packing increases with size we would expect the minimal distance to decrease further, so long as Mackay icosahedra are still local minima.
This is a purely geometric effect, independent of whether the Mackay icosahedron is the global minimum.
In fact, numerical experiments[11]show that the strain energy for isosahedral packing will probably make fcc packing more favourable aroundN≈2×105N\approx 2\times 10^{5}. The global minima based on icosahedral packing lack the centre atom for the larger clusters in Figure1. Hence, centred icosahedra can only be local minima at best in this size range, and their minimal distance is then not relevant for our Conjecture.

In the following we present a plausible, though not conclusive, strategy that could prove our Conjecture.
Consider the Baxter sticky hard sphere model with spheres of radius1/21/2.
Then any minimal energy configuration is a configuration with the maximal number of contact points (which may not be unique), and thus the minimal pairwise distance in such anNN-body cluster made of sticky hard spheres equals 1, independent ofNN.
Now pick anyN≥2N\geq 2and choose a minimal energy sticky hard sphere configuration as initial configuration for a Lennard-Jones energy minimizing gradient flow dynamics (or gradient-based minimisation algorithm), viz.∀i∈{1,…,N}:𝒓˙i​(t)=−∇iW​(𝒞(N))|𝒞(N)​(t).\forall i\in\{1,...,N\}:\ \dot{\boldsymbol{r}}_{i}(t)=-\nabla_{i}W\big({\cal C}^{(N)}\big)\Big|_{{\cal C}^{(N)}(t)}.(15)

It is generally expected, empirically tested, but not rigorously proved,
that at least one of the optimal sticky hard sphere configurations will be evolved by the gradient flow toward a global minimum𝒞gmin(N)∈{\cal C}^{(N)}_{\rm gmin}\inLJgminN{}_{N}^{\rm gmin}of the Lennard-Jones potential.
Assuming that this scenario holds, it is easy to see that any two initially touching spheres will experience a repulsive pairwise LJ force initially, which will act to increase their pairwise distance.
Of course, there will generally be additional forces exerted on these two particles by the others, and when located favorably they may initially partly or completely cancel the repulsive force between the given pair, or worse, overpower it so that the two particles move even closer to each other (temporarily at least).

Here is an example that this worst case scenario can happen in 1D: Consider a constrained minimal energy configuration of four sticky hard spheres of radius 1/2 each, constrained to a line.
The configuration is a chain with centers at{−32,−12,12,32}\{\frac{-3}{2},\frac{-1}{2},\frac{1}{2},\frac{3}{2}\}(up to overall translation or rotation).
With this initial configuration the LJ flow will initially move the two outer particles further out, and the two inner ones closer together; this is easily proved rigorously.
Hence the separation of the two inner particles becomes<1<1in the earliest phase of the evolution.
Running the LJ flow reveals that eventually the separation of the two inner particles increases to a distance>1>1, yet smaller than the outer nearest neighbor distance.

Now, such a linear chain arrangement of the four spheres is not an energy-minimizing sticky-hard-sphere configuration inℝ3{\mathbb{R}}^{3}(a regular tetrahedron is), and it is easy to see by symmetry that the regular tetrahedral initial configuration with pairwise distances all equal to 1 will uniformly and monotonically expand under the LJ flow that preserves the regular tetrahedral shape of the configuration.

Inspecting theN=5N=5LJ flow starting from the energy-minimizing sticky-hard-sphere configuration inℝ3{\mathbb{R}}^{3}also shows an expansion of all distancesinitially, but it is not uniform (due to lower symmetry than forN=4N=4), yet after a while one of the three different distances involved begins to shrink while the two others continue to expand.
This reversal from expansion to shrinking means that one cannot hope to prove a monotonic expansion for all times of all distances under an LJ flow that starts from an energy-minimizing sticky-hard-sphere configuration.
However, in the evolvingN=5N=5configurations the smallest distance at a finite time remains the smallest distance for all time, and it increases monotonically to a value>1>1.
If this observation is generic, then our Conjecture is true, and would be provable by demonstrating the monotonic increase of the smallest pairwise distance in an LJ flow that starts with a sticky hard sphere configuration of global minimal energy inℝ3{\mathbb{R}}^{3}.

This ends our theoretical plausibility reasoning in support of our Conjecture.

Our Conjecture, if true, may be difficult to prove.
In the meantime, it is certainly desirable to improve the best rigorous lower bound onrmin​(𝒞gmin(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)}_{\rm gmin})known so far, which differs by more than 25%\%from the suspected optimal lower bound.
This observation suggests that there is ample room for improvement.

## 2.4Connection ofrmin​(𝒞equ(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)}_{\rm equ})with the distance spectrum of𝒞equ(N){\cal C}^{(N)}_{\rm equ}

For anyNN-particle cluster𝒞(N){\cal C}^{(N)}there are(N2)\genfrac{(}{)}{0.0pt}{1}{N}{2}different ways of choosing a pair of two distinct particles in the cluster.
It is easy to see that there can be as many distinct pairwise distances in anNN-point configuration; for instance, placingNNpoint particles on the firstNNlocations of the sequence{0,1,3,7,12,…}⊂ℤ\{0,1,3,7,12,...\}\subset{\mathbb{Z}}(which is sequence A025582 at OEIS[57]) accomplishes this.
Yet in any particular Lennard-Jones equilibrium cluster𝒞(N)∈{\cal C}^{(N)}\inLJequN{}_{N}^{\rm equ}there typically are fewer distinct distances, because LJ stationary points often possess symmetry.
The obvious exception occurs whenN=2N=2, since(22)\genfrac{(}{)}{0.0pt}{1}{2}{2}is equal to11, trivially.

Let𝒞(N){\cal C}^{(N)}be an LJNcluster stationary point, and letν​(𝒞(N))\nu({\cal C}^{(N)})denote the number of different distances in this cluster, which we may abbreviate asν​(N)\nu(N)when the context is clear.
We note that for the global energy-minimizingNN-particle Lennard-Jones clusters LJgminN{}_{N}^{\rm gmin}one hasν​(N)=1\nu(N)=1ifN∈{2,3,4}N\in\{2,3,4\}, yetν​(N)∈{2,…,(N2)}\nu(N)\in\{2,...,\genfrac{(}{)}{0.0pt}{1}{N}{2}\}ifN>4N>4, while with general LJ equilibriaν​(N)>1\nu(N)>1is feasible already whenN>2N>2.

If𝒞(N)∈{\cal C}^{(N)}\inLJequN{}_{N}^{\rm equ}, we now abbreviate the minimal distance byrmin(𝒞(N))=:r1(N)r_{\mbox{\tiny{min}}}({\cal C}^{(N)})=:r_{1}(N), and the next smallest pairwise distance in𝒞(N){\cal C}^{(N)}byr2​(N)r_{2}(N), and so on.
We introduce the ratiosr1​(N)rk​(N):=ρk​(N)∈(0,1],k=1,…,ν​(N);\frac{r_{1}(N)}{r_{k}(N)}:=\rho_{k}(N)\in(0,1],\quad k=1,...,\nu(N);(16)

note thatρ1​(N)=1\rho_{1}(N)=1for allN≥2N\geq 2, and thatρk​(N)<1\rho_{k}(N)<1ifν​(N)>1\nu(N)>1andk>1k>1.
We also introduceCk​(N):=|{distinct pairs with ratio​ρk​(N)}|∈ℕ;C_{k}(N):=\Big|\{\mbox{distinct\ pairs\ with\ ratio}\ \rho_{k}(N)\}\Big|\,\in{\mathbb{N}};(17)

the allowed values ofCk​(N)C_{k}(N)(orbit sizes) are determined by subgroups of the point group for configuration𝒞(N){\cal C}^{(N)}, and∑k=1ν​(N)Ck​(N)=(N2).\sum_{k=1}^{\nu(N)}C_{k}(N)=\genfrac{(}{)}{0.0pt}{1}{N}{2}.(18)

Then for any LJ equilibrium cluster𝒞(N){\cal C}^{(N)}we can rewrite the ratioR​(𝒞(N))/A​(𝒞(N)){R({\cal C}^{(N)})}/{A({\cal C}^{(N)})}as follows,R​(𝒞(N))A​(𝒞(N))=∑k=1ν​(N)Ck​(N)​ρk​(N)12∑k=1ν​(N)Ck​(N)​ρk​(N)6.\frac{R({\cal C}^{(N)})}{A({\cal C}^{(N)})}=\frac{\sum\limits_{k=1}^{\nu(N)}C_{k}(N)\rho_{k}(N)^{12}}{\sum\limits_{k=1}^{\nu(N)}C_{k}(N)\rho_{k}(N)^{6}}.(19)

A final reduction is achieved by using the fact thatC1∈ℕC_{1}\in{\mathbb{N}}andρ1=1\rho_{1}=1, so we can rewrite (19) asR​(𝒞(N))A​(𝒞(N))=1+∑k=2ν​(N)ck​(N)​ρk​(N)121+∑k=2ν​(N)ck​(N)​ρk​(N)6,\frac{R({\cal C}^{(N)})}{A({\cal C}^{(N)})}=\frac{1+\sum\limits_{k=2}^{\nu(N)}c_{k}(N)\rho_{k}(N)^{12}}{1+\sum\limits_{k=2}^{\nu(N)}c_{k}(N)\rho_{k}(N)^{6}},(20)

whereck:=Ck/C1c_{k}:=C_{k}/C_{1}.
Thus, to compute the ratioR​(𝒞(N))/A​(𝒞(N)){R({\cal C}^{(N)})}/{A({\cal C}^{(N)})}only the number count ratiosCk/C1∈ℚC_{k}/C_{1}\in{\mathbb{Q}}are needed, not the actual number countsCkC_{k}, in addition to the distance ratiosρk<1\rho_{k}<1, fork∈{2,…,ν​(N)}k\in\{2,...,\nu(N)\}.

## 2.5The Conjecture revisited

Recalling the virial identity (7), our rewriting ofR​(𝒞(N))/A​(𝒞(N)){R({\cal C}^{(N)})}/{A({\cal C}^{(N)})}as (20) for any𝒞(N)∈{\cal C}^{(N)}\inLJequN{}_{N}^{\rm equ}has an interesting application for the problem of estimating the minimal pairwise distance in any global minimum Lennard-JonesNN-body cluster.
Namely, our conjectured lower bound onrmin​(𝒞(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)})for when𝒞(N)∈{\cal C}^{(N)}\inLJgminN{}_{N}^{\rm gmin}, which readsrmin​(𝒞(N))≥1r_{\mbox{\tiny{min}}}({\cal C}^{(N)})\geq 1in units wherermin​(𝒞(2))=216r_{\mbox{\tiny{min}}}({\cal C}^{(2)})=2^{\frac{1}{6}}, would be true if one could show thatR​(𝒞(N))/A​(𝒞(N))≥1/2{R({\cal C}^{(N)})}/{A({\cal C}^{(N)})}\geq 1/2for all𝒞(N)∈{\cal C}^{(N)}\inLJgminN{}_{N}^{\rm gmin}.
Equivalently, the estimateR​(𝒞(N))/A​(𝒞(N))≥1/2{R({\cal C}^{(N)})}/{A({\cal C}^{(N)})}\geq 1/2for all𝒞(N)∈{\cal C}^{(N)}\inLJgminN{}_{N}^{\rm gmin}would imply thatrmin​(𝒞(N))/rmin​(𝒞(2))≥1/216{r_{\mbox{\tiny{min}}}({\cal C}^{(N)})}/{r_{\mbox{\tiny{min}}}({\cal C}^{(2)})}\geq{1}/{2^{\frac{1}{6}}}in any units of energy and distance for these Lennard-Jones global minima.

To obtain good upper and lower estimates on theρk​(N)\rho_{k}(N)and theck​(N)c_{k}(N), and onν​(N)\nu(N), may not be any easier than obtaining good lower estimates onrmin​(𝒞(N))r_{\mbox{\tiny{min}}}({\cal C}^{(N)})directly.
Yet the connections between these superficially different types of questions are worth exploring further.

## 2.5.1Erdős-type distance problems

Estimatingν​(N)\nu(N)from below is a special case of the “Erdős distinct distances problem”[16]which asks for the smallest number of distinct distances that can occur in anNN-point configuration, written asd​(N)d(N).
Clearly, if𝒞(N)∈{\cal C}^{(N)}\inLJgminN{}_{N}^{\rm gmin}, thenν​(𝒞(N))≥d​(N)\nu({\cal C}^{(N)})\geq d(N), and so lower bounds ond​(N)d(N)give lower bounds onν​(𝒞(N))\nu({\cal C}^{(N)}).
The answer depends on the dimension of Euclidean space, but having applications to chemistry in mind, we are primarily interested in the problem for three-dimensional Euclidean space.
However, answers obtained by considering one-, or two-dimensional Euclidean space may well yield insights into the problem in three dimensions.

It is intuitively plausible that anNN-point configuration exhibiting the smallest number of distinct distances among all possibleNN-point configurations is one of high symmetry, so that most if not all of the distinct distances in it occur more than once.
This expectation is readily confirmed for smallNN.
Recall that a regular simplex inℝD{\mathbb{R}}^{D}is a geometrical shape withN=D+1N=D+1vertices (locations of point particles) and(D+12)\genfrac{(}{)}{0.0pt}{1}{D+1}{2}edges that all have the same length.
It follows that the dimer, the equilateral trimer, and the regular tetrahedral tetramer areD=3D=3configurations with the smallest possible number of distinct pairwise distances, namely 1; i.e.d​(N)=1d(N)=1whenN∈{2,3,4}N\in\{2,3,4\}— inD=3D=3dimensions.
WhenN>4N>4, thend​(N)>1d(N)>1inD=3D=3dimensions, and since the problem to determined​(N)d(N)for eachNNis NP-hard, the goal is to find good lower and upper bounds ond​(N)d(N).

The trivial upper boundd​(N)≤(N2)d(N)\leq\genfrac{(}{)}{0.0pt}{1}{N}{2}is readily improved in one dimension by placingNNpoint particles consecutively on (a subset of) the integersℤ{\mathbb{Z}}, which yieldsd​(N)≤N−1d(N)\leq N-1.
Forℝ2{\mathbb{R}}^{2}, from aN×N\sqrt{N}\times\sqrt{N}lattice (assumingN∈ℕ\sqrt{N}\in{\mathbb{N}}), Erdős proved that for largeNNone hasd​(N)≤c​N/log⁡Nd(N)\leq cN/\sqrt{\log N}for somecc.
Since linear and planar configurations are embeddable inℝ3{\mathbb{R}}^{3}, these bounds are automatically upper bounds ond​(N)d(N)inℝ3{\mathbb{R}}^{3}.

As for lower bounds inℝ3{\mathbb{R}}^{3}, it has been conjectured that whenNNis sufficiently large, thend​(N)≥c​N2/3d(N)\geq cN^{2/3}; the best result currently known seems to bed​(N)≥c​N3/5d(N)\geq cN^{3/5}, proved in[58].
Henceν​(𝒞(N))≥c​N3/5\nu({\cal C}^{(N)})\geq cN^{3/5}whenNNis large enough, for somec>0c>0.

Remark:In 2023 Alon et al.[1]proved that for generic norms any set ofNNpoints inℝ3{\mathbb{R}}^{3}defines at least(1−o​(1))​N(1-o(1))Ndistinct distances, thusd​(N)≥(1−o​(1))​Nd(N)\geq(1-o(1))N.
Since the Erdős upper bound on planar configurations is sublinear, it follows that the Euclidean norm is not a typical norm in the sense of Alon et al. (as they themselves point out), so that their results have no bearing on the distance spectrum for LJN.

Erdős[16]also asked for the largest number of times that some distance between two points can occur in a cluster ofNNpoints, without any constraints on whether it is the smallest one, or the largest one, or any ranking inbetween.
The particular distance in question (i.e. the one that occurs most often) can be taken to be the reference distance, by rescaling if necessary.
Thus this problem is known as the “Erdős unit distance problem.”
We refer to this quantity asu​(N)u(N).
As for the Erdős distinct distances problem, the answer depends on the dimension.
It is trivial forℝ{\mathbb{R}}(whereu​(N)=N−1u(N)=N-1) but highly nontrivial in dimensionsD≥2D\geq 2.
For the problem in the planeℝ2{\mathbb{R}}^{2}the sequence is known for smallNNand found as A186705 at[57].
For smallNNthe answer is also easy to find forℝ3{\mathbb{R}}^{3}; e.g. whenN∈{2,3,4}N\in\{2,3,4\}then all possible pairs can have the same distance andu​(N)=(N2)u(N)=\genfrac{(}{)}{0.0pt}{1}{N}{2}, and whenN=5N=5thenu​(N)=(N2)−1u(N)=\genfrac{(}{)}{0.0pt}{1}{N}{2}-1.
Yet for largerNNthe trueNN-dependence ofu​(N)u(N)inℝD{\mathbb{R}}^{D}will be hard to identify for anyD≥2D\geq 2.

Asymptotically for largeNNsome sharp estimates may be feasible.
For the planar case Erdős proved thatu​(N)>N1−ϵu(N)>N^{1-\epsilon}for anyϵ>0\epsilon>0, and he challenged his peers to find out whether there is a corresponding upper bound; as per[1]the best upper bound forNNpoints inℝ2{\mathbb{R}}^{2}currently known isu​(N)<C​N43u(N)<CN^{\frac{4}{3}}, proved in the 1980s by Spencer, Szemerédi, and Trotter.
For configurations inℝ3{\mathbb{R}}^{3}Erdős conjectured thatu​(N)>C​N4/3​log⁡log⁡Nu(N)>CN^{4/3}\log\log Nfor someCC.
Recently Zahl[85]obtained the upper boundu​(N)<C​N295/197+ϵu(N)<CN^{295/197+\epsilon}in the 3D case.

Remark:In[1]Alon et al. also proved that for generic distances inℝ3{\mathbb{R}}^{3}one has the upper boundu​(N)≤32​N​log2⁡Nu(N)\leq\frac{3}{2}N\log_{2}N, and that for sufficiently largeNNone can always find a 3D configuration𝒞​(N){\mathcal{C}}(N)for whichu​(𝒞​(N))=(1−o​(1))​N​log2⁡Nu({\mathcal{C}}(N))=(1-o(1))N\log_{2}N.
Again, since the Euclidean distance is not generic, the result by Alon et al. has no bearing on the distance spectrum for equilibrium, or even minimal energy configurations in LJN.

Since for the Erdős unit distance problem inℝ3{\mathbb{R}}^{3}no demand is made on the cluster being an LJNglobal energy minimum,u​(N)u(N)for this problem is an upper bound to any of ourCk​(N)C_{k}(N).
Unfortunately, if his conjectured lower bound is true, thenu​(N)u(N)grows superlinearly inNN.
To settle our conjecture about the minimal pairwise distance for the LJNglobal energy minima, better estimates of theCk​(N)C_{k}(N)for Lennard-Jones equilibria, or at least the global LJNenergy minima, are needed.

Some estimates can be extracted from the well-known thermodynamic stability of the Lennard-Jones pair interaction, which implies that the limit, asN→∞N\to\infty, of the minimal Lennard-Jones energy divided byNNexists.
Thus, if any particular distance, different from the one for which the Lennard-Jones pair energy yields zero, occurs superlinearly often along a sequence in the set of all LJminN{}_{N}^{\rm{min}}, then it has to be compensated by another superlinear sequence for which the pair energy takes the opposite sign.
The crystal lattice results for the thermodynamic limit of the LJNground states reveal that this situation is impossible, because in that limit all pairwise distances that occur yield a negative LJ energy.
This observation establishes that the minimal distance, and any other, for the configurations in LJminN{}_{N}^{\rm{min}}, cannot occur more thanc​NcNtimes for some constantcc.

To obtain an estimate for the constantccwe revisit systems composed of sticky hard spheres.
We recall thatWshs​(N)W_{\mbox{\tiny shs}}(N), the ground state energy achieved by optimal clusters ofNNsticky hard spheres, by definition is the negative of the largest possible number of contacts thatNNcongruent spheres can have.
It is easy to see that whenN≥2N\geq 2, then a lower bound is−Wshs​(N)≥2​N−3-W_{\mbox{\tiny shs}}(N)\geq 2N-3(diagonal penny pair chain) and an upper bound is−Wshs​(N)<12​N-W_{\mbox{\tiny shs}}(N)<12N(the number of hard spheres multiplied with the maximal number of contacts a single sphere can have with congruent other spheres[51], and this overcounts the total number of contacts that can possibly exist in anNNbody cluster of hard spheres).
In[3]it was proved that−Wshs​(N)≤6​N−0.926​N23-W_{\mbox{\tiny shs}}(N)\leq 6N-0.926N^{\frac{2}{3}}for allNN, and the factor 6 of the linear term is sharp.
Recalling now our discussion of the LJ gradient flows that start with such an optimal hard-sphere configuration, we suspect thatC1​(N)C_{1}(N)for LJgminN{}_{N}^{\rm gmin}clusters is not larger than−Wshs​(N)-W_{\mbox{\tiny shs}}(N).
Thus we expect thatC1​(N)≤6​NC_{1}(N)\leq 6N.

## 3The distance spectra of selected LJequN{}_{N}^{\rm{{equ}}}minima

Our approach of using the virial theorem to gain insight into the minimal pairwise distancermin​(LJNgmin)r_{\mbox{\tiny{min}}}(\mbox{LJ}_{N}^{\rm{gmin}})inLJN\mathrm{LJ}_{N}global minima has revealed an interesting connection with the spectrum of pair distances.
While much is known about the spectrum of distances in regular crystal lattices, see e.g. Born’s classic[4], we are not aware of a systematic study of the spectrum of distances in LJgminN{}_{N}^{\rm{gmin}}.
In this section we consider some numerically computed distance spectra of putative global minima for a sample ofNNvalues, includingN=923N=923where the shortest distance was observed, which belongs to the centered icosahedral sequence{1,13,55,147,309,561,923,…}\{1,13,55,147,309,561,923,...\}(sequence A005902 at[57]).
Except for the uninteresting single atom, the other configurations withNNin this sequence are either Mackay icosahedra[36]or cuboctahedra.
The Mackay icosahedra yield global LJ energy minima whenNNis not too large; with increasingNNthe non-crystallographic packing and strain energy can make them uncompetitive with truncated crystal structures.

Figure2shows the distance spectra as a histogram forN∈{12,13,14}N\in\{12,13,14\}, top-down in this ordering.
The bin width is 0.02 and the bin areas sum to 1.
Clearly visible is a clustering of distances around 1.15,
around 1.85, and near 2.2.
As expected, the highly symmetricalN=13N=13Mackay icosahedron features the least number of distinct distances compared to the maximal possible number(N2)\genfrac{(}{)}{0.0pt}{1}{N}{2}, namely 4 out of 78, while theN=12N=12cluster features 7 out of 66 distinct distances, and theN=14N=14cluster 11 out of 91;
these ratios, in decimal expansion, are:0.1​06¯0.1\overline{06},0.051282¯0.\overline{051282}, and0.120879¯0.\overline{120879}.Figure 2:Distance spectra of the LJNglobal minima forN∈{12,13,14}N\in\{12,13,14\}(top-down).
Visibly no distance is smaller than 1.Figure 3:Distance spectra of the LJNglobal minima forN∈{54,55,56}N\in\{54,55,56\}(top-down).
Again, no distance is smaller than 1.

Figure3shows the distance spectra forN∈{54,55,56}N\in\{54,55,56\}.
The ratio of the number of distinct distances in LJNcompared to the number of distinct distances maximally possible in anNNbody cluster is, respectively,32/(542)≈0.02236232/\genfrac{(}{)}{0.0pt}{1}{54}{2}\approx 0.022362,27/(552)=1/55=0.0​18¯27/\genfrac{(}{)}{0.0pt}{1}{55}{2}=1/55=0.0\overline{18}, and43/(562)=0.02​792207¯43/\genfrac{(}{)}{0.0pt}{1}{56}{2}=0.02\overline{792207}.
This result is in line with the expectation that the magic numberN=55N=55implies a cluster with higher symmetry than its neighbors withN=54N=54andN=56N=56.

Another feature, prominently visible for the tripleN∈{54,55,56}N\in\{54,55,56\}, yet not for the tripleN∈{12,13,14}N\in\{12,13,14\}, is this:
The spectrum forN=55N=55appears less “vertically noisy” than the one forN=54N=54orN=56N=56, in the sense that theN=55N=55cluster has the largest number of distinct distances that are occupied by the same percentage number of particles.
This will be noticeable also for the next triple near Mackay numberN=147N=147.

The histograms forN∈{54,55,56}N\in\{54,55,56\}are easy to compare, and so are those forN∈{12,13,14}N\in\{12,13,14\}, but the comparison of these two groups against each other is also revealing.
Naturally, with increasingNNthe range of distances in an LJNcluster increases, which is obvious by comparing the two triples of spectra.
Interestingly, though, in the distance spectra of theN∈{54,55,56}N\in\{54,55,56\}clusters there also appears a notable isolated peak at≈1.6\approx 1.6where no such peak was visible for whenN∈{12,13,14}N\in\{12,13,14\}.
The previously visible peaks remain visible, too.

Usually, the dimension of a symmetry group is used as an absolute measure to decide which group has the higher symmetry.
By that measure the Mackay icosahedron withN=55N=55has the same symmetry as the one withN=13N=13.
However, if as arelative symmetry metricwe use the reciprocal of the ratio of the actual number of distinct distances in a cluster to the maximally possible number of distances in any cluster with the same number of atoms, then the metric for LJgmin55{}_{55}^{\rm gmin}is larger than for LJgmin13{}_{13}^{\rm gmin}by this relative metric.
This rational symmetry measure might be useful analogously to a continuous symmetry measure[82,17,83,84,81,32].

Inspired by these first observations we inspect the next triple associated with the magic numbers of the Mackay icosahedra.
TheN=147N=147distance spectrum and that of its two neighbors is shown in Figure4.
Again, not only are there fewer distinct distances in theN=147N=147spectrum than for its two adjacent neighbors, there also are noticeably more distinct distances with equal occupation numbers than in the two spectra for the neighbours ofN=147N=147.
Also, the previously visible spectral peaks a little bit to the right of 1, near 1.6, a little bit below 2 and a little bit above 2, are all still visible.Figure 4:Distance spectra of putative LJNglobal minima forN∈{146,147,148}N\in\{146,147,148\}.Figure 5:Distance spectra of putative LJNglobal minima forN∈{309,561,923}N\in\{309,561,923\}.

Going beyondN=200N=200, Figure5shows the histograms for the putative LJgminN{}_{N}^{\rm gmin}clusters with magic Mackay icosahedral numbersN∈{309,561,923}N\in\{309,561,923\}:
Since the distance histogram scales with system size, and we include the full spectrum, the resolution is lower for the larger clusters.
Nevertheless the short-distance peaks a little above 1, at roughly 1.6, and a little below and above 2, are still clearly visible.
Also noticeable is the emergence of a broad peak feature to the right of distance 2.2.

These trends are also visible in the distance spectra shown in Figure6for the truncated octahedralLJ38\mathrm{LJ}_{38}and the decahedralLJ75\mathrm{LJ}_{75}global minimum.Figure 6:Distance spectra for theLJ38\mathrm{LJ}_{38}andLJ75\mathrm{LJ}_{75}global minima (top to bottom). These normalised histograms correspond to a bin width of 0.02.

In Figure7we compare them with the corresponding results for a system with periodic boundary conditions taken from a previous study of crystallisation[10].Figure 7:Distance spectra for the fcc minimum and a local minimum from the liquid in a system of 864 atoms with periodic boundary conditions and number density 1.05[10](top to bottom). These normalised histograms correspond to a bin width of 0.02. The horizontal scale is extended to zero for the periodic systems to highlight the first peak in the liquid configuration.

The behavior of the spectrum for the global minima of finite clusters (as opposed to bulk) with increasing size is intriguing.
As for the radial distribution function (pair correlation function) the pair distance distribution encodes a great deal of structural information, as well as the energetics, as discussed below.

All the histograms shown above feature small-distance peaks at a little above 1 and a little below and above 2, and all histograms withN≥54N\geq 54also feature a peak roughly at 1.6.
These distances can all be assigned from analysis of the underlying structures.

The pair correlation function,g​(r)g(r), and structure factor sampled over local minima were first used to gain new insights by Stillinger and Weber for condensed phases[63,64].
Common neighbour analysis provides a useful way to approach the distance spectrum.
For example, a split second peak ing​(r)g(r)is often associated with supercooled liquids and glasses and polytetrahedral packing[70,12], arising from the apex-to-apex distance in a trigonal bipyramid and approximate colinear triatomic arrangements[22,30,8].
The smallest distance in the spectra of course corresponds to nearest-neighbour atoms, and contributions to peaks around 1.6 arise from next-nearest distances for polytetrahedral packing (1.633 for regular tetrahedra) and atoms sharing four neighbours at opposite vertices of an octahedron.
The distances a little below 2 come from the opposite vertices in triangles that share an edge, while the distance a little above 2 results from atoms in roughly collinear arrangements with a common neighbour between them.

An interesting feature in the histograms forN∈{12,14}N\in\{12,14\}is that a unique highest peak is found very close to 1, while for all other inspectedNNwith unique highest peak it occurs atr>2r>2for the selected bin width of 0.02.
We comment further on the distance distributions and connections between structure and energetics in our Conclusions below.

## 4Conclusions

In this article we have inquired into the minimal distance that occurs inNN-body clusters that globally minimize the Lennard-Jones energy defined in equation (2), or are merely stationary points.
We have given a rigorous proof that the dimer equilibrium distance is the largest possible minimal distance, and that it occurs if and only if theNN-body cluster is a Lennard-Jones global minimum forN∈{2,3,4}N\in\{2,3,4\}.
We have also given plausibility arguments, though no rigorous proof, for our conjecture that the minimal distance between the particles in any Lennard-JonesNN-body cluster global minimum is always bigger than 1 in units where the dimer equilibrium distance is2162^{\frac{1}{6}}.

A rigorous proof is desirable, for it would significantly reduce the search space when looking for Lennard-Jones cluster global minima.
The currently best known provable lower bound is about 25% above the conjectured lower bound.

By examining the minimal pairwise distance in (mostly) numerically computed putatively energy-optimal Lennard-JonesNN-body clusters for2≤N≤10002\leq N\leq 1000we found numerical evidence in support of our conjecture.
The plot of the minimal pairwise distance versusNNin addition has revealed some interesting features that suggest that the minimal pairwise distance of globally energy-minimizing LJNclusters is a useful indicator of some structural information of the cluster.
We were able to map these features into centered icosahedral, icosahedral without central atom, and decahedral structures.
It should be interesting to explore this structural information map also for largerNNvalues.

Our approach to the minimial pairwise distance invoked the virial theorem for equilibrium configurations.
This framework provided an interesting expression for the minimal pairwise distance in an equilibrium cluster in terms of the ratio of the repulsive over the attractive part of equation (2) for the cluster, which we then expressed in terms of features of the distance spectrum of the cluster.
This result in turn raised questions of the type known as Erdős distance problems.

Inspecting the numerically computed histograms of the pair distances for some of the putativeLJN\mathrm{LJ}_{N}global minima suggested a symmetry metric, given by the reciprocal of the number of distinct distances in the cluster relative to the maximal possible number of distinct distances, which assigns more symmetry to theN=55N=55than to theN=13N=13Mackay icosahedron, while their point groups are of course the same.

Another feature highlighted by the distance histograms is the variation
in the occupation numbers of the most probable distances that feature in a distance spectrum.
As expected from the maximal point group symmetry, the distributions for the Mackay icosahedral clusters are visibly more bunched than their neighbors.

The structure encodes the pair distance distribution, and hence the energy, in a unique mapping.
Connections between structure and energetics can be further analysed by defining a strain energy in terms of the deviation of pair distances from the ideal value[13,14].
The Morse potential[41]has proved particularly insightful here, since it has an additional adjustable parameter compared to the Lennard-Jones representation.
This extra degree of freedom can be interpreted in terms of the range of the pair interaction, which can help to explain the energetic competition between different packing schemes[13,14].
Polytetrahedral packing schemes, associated with local fivefold symmetry, can be interpreted in terms of disclinations, while quasiperiodic packings are associated with quasicrystals[56,42,45,60,46].
The topological defects in polytetrahedral structures are associated with disclination lines[44,43], leading to Frank-Kasper phases[18,19]and Kasper polyhedra.
Common neighbour[22], Voronoi[67], and bond
order[59]analysis have proved to be very useful in
decomposing atomic structures, while topological cluster classification[38,76]has been
successfully applied to a variety of atomic[66,69,48,37]and colloidal[65,39]clusters.

We hope that further work along the lines we have presented here might be combined with such schemes to provide new insight into the fascinating connections between structure, energetics, and emergent physical properties.

Acknowledgement: We thank Prof. Paddy Royall and Prof. Jonathan Doye for helpful discussions and suggestions.

## References
- [1]N. Alon, M. Bucić, and L. Sauermann(2023)Unit and distinct distances in typical norms.arXiv:2302.09058.Cited by:§2.5.1,§2.5.1,§2.5.1.
- [2]L. Bétermin, L. Šamaj, and Travěnec(2023)Three-dimensional lattice ground states for Riesz and Lennard-Jones–type energies.Stud. Appl. Math.150,pp. 69–91.Cited by:§2.3.
- [3]K. Bezdek and S. Reid(2013)Contact graphs for unit sphere packings revisited.J. Geom.104,pp. 57–83.Cited by:§2.5.1.
- [4]M. Born(1915)Dynamik der Kristallgitter.B.G. Teubner,Leipzig.Cited by:§3.
- [5]A. Burrows, S. Cooper, E. Pahl, and P. Schwerdtfeger(2020)Analytical methods for fast converging lattice sums for cubic and hexagonal close-packed structures.J. Math. Phys.61,pp. 123503, 1–35.Cited by:§1,§2.3.
- [6]A. Burrows, S. Cooper, and P. Schwerdtfeger(2021)Instability of the body-centered cubic lattice within the sticky hard sphere and Lennard-Jones model obtained from exact lattice summations.Phys. Rev. E104,pp. 035306.External Links:Document,LinkCited by:§1.
- [7]M. E. Cates and V. N. Manoharan(2015)Celebrating soft matter’s 10th anniversary: testing the foundations of classical entropy: colloid experiments.Soft Matter11,pp. 6538–6546.Cited by:§1.
- [8]A. S. Clarke and H. Jónsson(1993)Structural changes accompanying densification of random hard-sphere packings.Phys. Rev. E47,pp. 3975–3984.Cited by:§3.
- [9]E. A. Coutsias, C. Seok, and K. A. Dill(2004)Using quaternions to calculate RMSD.J. Comput. Chem.25,pp. 1849–1857.Cited by:§1.
- [10]V. K. de Souza and D. J. Wales(2016)The potential energy landscape for crystallisation of a lennard-jones fluid.J. Stat. Mech.2016,pp. 074001.Cited by:Figure 7,§3.
- [11]J. P. K. Doye and F. Calvo(2002)Entropic effects on the structure of Lennard-Jones clusters.J. Chem. Phys.116,pp. 8307–8317.Cited by:§2.3,§2.3.
- [12]J. P. K. Doye, D. J. Wales, F. H. M. Zetterling, and M. Dzugutov(2003)The favored cluster structures of model glass formers.J. Chem. Phys.118,pp. 2792–2799.Cited by:§3.
- [13]J. P. K. Doye and D. J. Wales(1995)MAGIC numbers and growth sequences of small face-centered-cubic and decahedral clusters.Chem. Phys. Lett.247,pp. 339–347.Cited by:§2.3,§4.
- [14]J. P. K. Doye and D. J. Wales(1996)THE structure and stability of atomic liquids — from clusters to bulk.Science271,pp. 484–487.Cited by:§2.3,§4.
- [15]J. P. K. Doye and D. J. Wales(1997)Structural consequences of the range of the interatomic potential - a menagerie of clusters.J. Chem. Soc., Faraday Trans.93,pp. 4233–4243.Cited by:§2.3.
- [16]P. Erdős(1946)On sets of distances ofnnpoints.Amer. Math. Monthly53,pp. 248–250.Cited by:§2.5.1,§2.5.1.
- [17]P. W. Fowler(1992)Vocabulary for fuzzy symmetry.Nature360,pp. 626.Cited by:§3.
- [18]F. C. Frank and J. S. Kasper(1958)Complex alloy structures regarded as sphere packings. I. Definitions and basic principles.Acta Cryst.11,pp. 184–190.Cited by:§4.
- [19]F. C. Frank and J. S. Kasper(1959)Complex alloy structures regarded as sphere packings. II. Analysis and classification of representative structures.Acta Cryst.12,pp. 483–499.Cited by:§4.
- [20]D. Frenkel and D. J. Wales(2011)Colloidal self-assembly — designed to yield.Nature Materials10,pp. 410–411.Cited by:§1.
- [21]M. Griffiths, S. P. Niblett, and D. J. Wales(2017)Optimal alignment of structures for finite and periodic systems.J. Chem. Theory Comput.13,pp. 4914–4931.Cited by:§1.
- [22]J. D. Honeycutt and H. C. Andersen(1987)Molecular dynamics study of melting and freezing of small Lennard-Jones clusters.J. Phys. Chem.91,pp. 4950–4963.Cited by:§3,§4.
- [23]S. Ino(1969)Stability of multiply-twinned particles.J. Phys. Soc. Jpn.27,pp. 941–953.Cited by:§2.3.
- [24]J. E. Jones and A. E. Ingham(1925)On the calculation of certain crystal potential constants, and on the cubic crystal of least potential energy.Proc. Royal Soc. Lond. A107,pp. 636–653.Cited by:§1,§2.3.
- [25]J. E. Jones(1924)On the determination of molecular fields. i. From the variation of the viscosity of a gas with temperature.Proc. R. Soc. Lond. A106,pp. 441–462.Note:External Links:DocumentCited by:§1.
- [26]J. E. Jones(1924)On the determination of molecular fields. ii. From the equation of state of a gas.Proc. R. Soc. Lond. A106,pp. 463–477.Cited by:§1.
- [27]J. E. Jones(1924)On the determination of molecular fields. iii.—From crystal measurements and kinetic theory data.Proc. R. Soc. Lond. A106(740),pp. 709–718.External Links:Document,https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.1924.0098Cited by:§1.
- [28]J. E. Jones(1925)On the atomic fields of helium and neon.Proc. R. Soc. Lond. A107(741),pp. 157–170.External Links:Document,https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.1925.0012Cited by:§1.
- [29]R. Jonker and A. Volgenant(1987)A shortest augmenting path algorithm for dense and sparse linear assignment problems.Computing38,pp. 325–340.Cited by:§1.
- [30]H. Jónsson and H. C. Andersen(1988)Icosahedral ordering in the Lennard-Jones liquid and glass.Phys. Rev. Lett.60,pp. 2295ff.Cited by:§3.
- [31]W. Kabsch(1978)A discussion of the solution for the best rotation to relate two sets of vectors.Acta Crystallogr. Sect. A34,pp. 827–828.Cited by:§1.
- [32]O. Katzenelson, H. Z. Hel-Or, and D. Avnir(1996)Chirality of large random supramolecular structures.Chem. Eur. J.2,pp. 174.Cited by:§3.
- [33]S. K. Kearsley(1989)ON the orthogonal transformation used for structural comparisons.Acta Cryst. A45,pp. 208–210.Cited by:§1.
- [34]M. K.-H. Kiessling and D. J. Wales(2024)On the global minimum of the classical potential energy for clusters bound by many-body forces.J. Statist. Phys.191,pp. 8,26pp..Cited by:§2.3.
- [35]R. H. Leary(1997)Global optima of Lennard-Jones clusters.J. Global Optim.11,pp. 35–53.Cited by:Figure 1,§2.3.
- [36]A. L. Mackay(1962)A dense non-crystallographic packing of equal spheres.Acta Cryst.15,pp. 916–918.Cited by:Figure 1,§2.3,§2.3,§3.
- [37]A. Malins, J. Eggers, C. P. Royall, S. R. Williams, and H. Tanaka(2013)Identification of long-lived clusters and their link to slow dynamics in a model glass former.J. Chem. Phys.138(12),pp. 12A535.External Links:DocumentCited by:§4.
- [38]A. Malins, S. R. Williams, J. Eggers, and C. P. Royall(2013)Identification of structure in condensed matter with the topological cluster classification.J. Chem. Phys.139(23),pp. 234506.External Links:Link,DocumentCited by:§4.
- [39]A. Malins, S. R. Williams, J. Eggers, H. Tanaka, and C. P. Royall(2011)The effect of inter-cluster interactions on the structure of colloidal clusters.Journal of Non-Crystalline Solids357,pp. 760–766.External Links:DocumentCited by:§4.
- [40]L. D. Marks(1984)Surface structure and energetics of multiply twinned particles.Phil. Mag. A49,pp. 81–93.Cited by:Figure 1,§2.3.
- [41]P. M. Morse(1929)Diatomic molecules according to the wave mechanics. II. Vibrational levels.Phys. Rev.34,pp. 57–64.Cited by:§4.
- [42]D. R. Nelson and B. I. Halperin(1985)Pentagonal and icosahedral order in rapidly cooled metals.Science229,pp. 233–238.Cited by:§4.
- [43]D. R. Nelson(1983)Liquids and glasses in spaces of incommensurate curvature.Phys. Rev. Lett.50,pp. 982ff.Cited by:§4.
- [44]D. R. Nelson(1983)Order, frustration, and defects in liquids and glasses.Phys. Rev. B28,pp. 5515ff.Cited by:§4.
- [45]D. R. Nelson(1986)Quasicrystals.Sci. Amer.255,pp. 42–51.Cited by:§4.
- [46]D. R. Nelson(1989)Polytetrahedral order in condensed matter.Solid State Phys.42,pp. 1–90.Cited by:§4.
- [47]E. G. Noya and J. P. K. Doye(2006)Structural transitions in the 309-atom magic number lennard-jones cluster (6 pages)..J. Chem. Phys.124,pp. 104503.Cited by:§2.3.
- [48]L. Ortlieb, T. S. Ingebrigtsen, J. E. Hallett, F. Turci, and C. P. Royall(2023)Probing excitations and cooperatively rearranging regions in deeply supercooled liquids.Nature Commun.14,pp. 2621.Cited by:§4.
- [49]D. Romero, C. Barrón, and S. Gómez(1999)The optimal geometry of lennard-jones clusters: 148–309.Computer Physics Communications123,pp. 87–96.External Links:DocumentCited by:§2.3.
- [50]W. Schachinger, B. Addis, I. M. Bomze, and F. Schoen(2007)New results for molecular formation under pairwise potential minimization.Comput. Optim. Appl.38,pp. 329–349.Cited by:§1.
- [51]K. Schütte and B. L. Van der Waerden(1953)Das Problem der dreizehn Kugeln.Math. Ann.125,pp. 325–334.Cited by:§2.5.1.
- [52]P. Schwerdtfeger, N. Gaston, R. P. Krawczyk, R. Tonner, and G. E. Moyano(2006)Extension of the Lennard-Jones potential: theoretical investigations into rare-gas clusters and crystal lattices of He, Ne, Ar and Kr using many-body interaction expansions.Phys. Rev. B73,pp. 064112–1–064112–19.Note:External Links:DocumentCited by:§1.
- [53]P. Schwerdtfeger, A. Burrows, and O. R. Smits(2021)The Lennard-Jones potential revisited: analytical expressions for vibrational effects in cubic and hexagonal close-packed lattices.J. Phys. Chem. A125,pp. 3037–3057.Note:doi: 10.1021/acs.jpca.1c00012External Links:Document,ISBN 1089-5639Cited by:§1.
- [54]P. Schwerdtfeger and A. Burrows(2022)Cuboidal bcc to fcc transformation of Lennard-Jones phases under high pressure derived from exact lattice summations.J. Phys. Chem. C126(20),pp. 8874–8882.External Links:Document,https://doi.org/10.1021/acs.jpcc.2c01255,LinkCited by:§1.
- [55]P. Schwerdtfeger and D. J. Wales(2024)100 years of the Lennard-Jones potential.J. Chem. Theory Comput.20,pp. 3379–3405.External Links:DocumentCited by:§1.
- [56]D. Shechtman, I. Blech, D. Gratias, and J. W. Cahn(1984)Phys. Rev. Lett.53,pp. 1951.Cited by:§4.
- [57]N. J. A. SloaneThe Online Encyclopedia of Integer Sequences.Note:https://oeis.orgCited by:§2.4,§2.5.1,§3.
- [58]J. Solymosi and V. H. Vu(2008)Near optimal bounds for the Erdős distinct distances problem in high dimensions.Combinatorica28,pp. 113–125.Cited by:§2.5.1.
- [59]P. J. Steinhardt, D. R. Nelson, and M. Ronchetti(1983)Bond-orientational order in liquids and glasses.Phys. Rev. B28,pp. 784–805.Cited by:§4.
- [60]P. J. Steinhardt(1987)Icosahedral solids: A new phase of matter?.Science238,pp. 1242–1247.Cited by:§4.
- [61]F. H. Stillinger and T. A. Weber(1982)Hidden structure in liquids.Phys. Rev. A25,pp. 978–989.Cited by:§1,§1.
- [62]F. H. Stillinger and T. A. Weber(1984)Packing structures and transitions in liquids and solids.Science225,pp. 983–989.Cited by:§1,§1.
- [63]F. H. Stillinger and T. A. Weber(1985)Computer simulation of local order in condensed phases of silicon.Phys. Rev. B31,pp. 5262.Cited by:§3.
- [64]F. H. Stillinger and T. A. Weber(1985)Inherent structure theory of liquids in the hard-sphere limit.J. Chem. Phys.83,pp. 4767–4775.Cited by:§3.
- [65]J. Taffs, A. Malins, S. R. Williams, and C. P. Royall(2010)A structural comparison of models of colloid-polymer mixtures.J. Phys.: Cond. Matt.22,pp. 104119.Cited by:§4.
- [66]J. Taffs, A. Malins, S. R. Williams, and C. P. Royall(2010)The effect of attractions on the local structure of liquids and colloidal fluids.J. Chem. Phys.133,pp. 244901.External Links:DocumentCited by:§4.
- [67]M. Tanemura, Y. Hiwatari, H. Matsuda, T. Ogawa, N. Ogita, and A. Ueda(1977)Geometrical analysis of crystallization of the soft-core model.Prog. Theor. Phys.58,pp. 1079–1095.External Links:DocumentCited by:§4.
- [68]The Cambridge Landscape Database.Note:https://www-wales.ch.cam.ac.uk/CCD.htmlCited by:§2.3.
- [69]F. Turci, C. P. Royall, and T. Speck(2017)Nonequilibrium phase transition in an atomistic glassformer: the connection to thermodynamics.Phys. Rev. X7,pp. 031028.External Links:DocumentCited by:§4.
- [70]B. W. van de Waal(1995)On the origin of second-peak splitting in the static structure factor of metallic glasses.J. Non-Cryst. Solids189,pp. 118–128.Cited by:§3.
- [71]T. Vinkó(2005)Minimal inter-particle distance in atom clusters.Acta Cybern.17,pp. 105–119.Cited by:§1.
- [72]D. J. Wales and J. M. Carr(2012)Quasi-continuous interpolation scheme for pathways between distant configurations.J. Chem. Theory Comput.8(12),pp. 5020–5034.Cited by:§1.
- [73]D. J. Wales and J. P. K. Doye(2003)Stationary points and dynamics in high-dimensional systems.J. Chem. Phys.119,pp. 12409–12416.Cited by:§1,§1.
- [74]D. J. Wales(2003)Energy landscapes.Cambridge University Press,Cambridge.Cited by:§1.
- [75]L. T. Wille and J. Vennik(1985)Computational complexity of the ground-state determination of atomic clusters.J. Phys. A: Math. Gen.18,pp. L419–422.Cited by:§1.
- [76]X. Wu, K. Skipper, Y. Yang, F. J. Moore, F. C. Meldrum, and C. P. Royall(2025)Tuning higher order structure in colloidal fluids.Soft Matter21,pp. 2787–2802.External Links:DocumentCited by:§4.
- [77]Y. Xiang, H. Jiang, W. Cai, and X. Shao(2004)An effective method based on lattice construction and the genetic algorithm for optimization of large Lennard-Jones clusters.J. Chem. Phys.108,pp. 3586–3592.Cited by:§2.3.
- [78]Y. Xiang, L. Cheng, W. Cai, and X. Shao(2004)Structural distribution of lennard-jones clusters containing 562 to 1000 atoms.J. Phys. Chem. A108(44),pp. 9516–9520.External Links:DocumentCited by:§2.3.
- [79]G. L. Xue(1997)Minimum inter-particle distance at global minimizers of Lennard-Jones clusters.J. Global Optim.11,pp. 83–90.Cited by:§1.
- [80]S. A. Yuhjtman(2015)A sensible estimate for the stability constant of the Lennard-Jones potential.J. Statist. Phys.160,pp. 1684–1695.Cited by:§1.
- [81]H. Zabrodsky and D. Avnir(1995)Continuous symmetry measures. 4. Chirality.J. Am. Chem. Soc.117,pp. 462–473.Cited by:§3.
- [82]H. Zabrodsky, S. Peleg, and D. Avnir(1992)Continuous symmetry measures.J. Am. Chem. Soc.114,pp. 7843–7851.Cited by:§3.
- [83]H. Zabrodsky, S. Peleg, and D. Avnir(1993)Continuous symmetry measures. 2. Symmetry groups and the tetrahedron.J. Am. Chem. Soc.115,pp. 8278–8289.Cited by:§3.
- [84]H. Zabrodsky, S. Peleg, and D. Avnir(1993)Erratum to: Continuous symmetry measures. 2. Symmetry groups and the tetrahedron.J. Am. Chem. Soc.115,pp. 11656.Cited by:§3.
- [85]J. Zahl(2019)Breaking the 3/2 barrier for unit distances in three dimensions.Int. Math. Res. Notices2019,pp. 6235–6284.Cited by:§2.5.1.
- [86]M. Zschornak, T. Leisegang, F. Meutzner, H. Stöcker, T. Lemser, T. Tauscher, C. Funke, C. Cherkouk, and D. C. Meyer(2018)Harmonic principles of elemental crystals — From atomic interaction to fundamental symmetry.Symmetry10,pp. 228, 1–14.Cited by:§2.3.

## 


- 


Major funding support from
