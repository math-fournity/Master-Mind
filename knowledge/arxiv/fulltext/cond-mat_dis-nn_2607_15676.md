# Absence of Spin-Glass Order on Migdal--Kadanoff Hierarchical Lattices near Three Dimensions

**arXiv ID**: 2607.15676v1
**Authors**: Manaka Okuyama, Masayuki Ohzeki
**Published**: 2026-07-17
**Categories**: cond-mat.dis-nn, math-ph
**Comments**: 7 pages, 1 figure
**HTML URL**: https://arxiv.org/html/2607.15676v1

## Abstract

We derive a rigorous sufficient condition for the absence of spin-glass order in the Ising spin glass with symmetric binary couplings on Migdal--Kadanoff (MK) hierarchical lattices with even branching number. The key observation is that a single exact renormalization-group step creates zero effective bonds with positive probability, thereby reducing the problem to bond percolation on the corresponding hierarchical lattice. When the induced dilution exceeds the percolation threshold, both spin-glass order and stiffness are absent at all temperatures, including zero temperature. As a consequence, our criterion gives a rigorous proof that the Ising spin glass on the square lattice does not exhibit a spin-glass phase within the MK approximation. More unexpectedly, by choosing sufficiently large scale factors and branching numbers, we construct MK hierarchical lattices whose fractal dimensions are arbitrarily close to three from below but still exhibit no spin-glass order. This sharply contrasts with numerical estimates obtained for MK hierarchical lattices with relatively small scale factors and branching numbers, which placed the lower critical dimension near \(2.52\).

## Full Text

Absence of Spin-Glass Order on Migdal–Kadanoff Hierarchical Lattices near Three Dimensions

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- License: CC BY-NC-ND 4.0arXiv:2607.15676v1 [cond-mat.dis-nn] 17 Jul 2026

## Absence of Spin-Glass Order on Migdal–Kadanoff Hierarchical Lattices near Three DimensionsManaka Okuyama1,2Masayuki Ohzeki1,3,4,51Graduate School of Information Sciences, Tohoku University, Sendai 980-8579, Japan2School of Computing, Institute of Science Tokyo, Tokyo 152-8551, Japan3Department of Physics, Institute of Science Tokyo, Tokyo 152-8551, Japan4Research and Education Institute for Semiconductors and Informatics, Kumamoto University, Kumamoto 860-0862, Japan5Sigma-i Co., Ltd., Tokyo 108-0075, Japan

## Abstract

We derive a rigorous sufficient condition for the absence of spin-glass order in the Ising spin glass with symmetric binary couplings on Migdal–Kadanoff (MK) hierarchical lattices with even branching number. The key observation is that a single exact renormalization-group step creates zero effective bonds with positive probability, thereby reducing the problem to bond percolation on the corresponding hierarchical lattice.
When the induced dilution exceeds the percolation threshold, both spin-glass order and stiffness are absent at all temperatures, including zero temperature.
As a consequence, our criterion gives a rigorous proof that the Ising spin glass on the square lattice does not exhibit a spin-glass phase within the MK approximation. More unexpectedly, by choosing sufficiently large scale factors and branching numbers, we construct MK hierarchical lattices whose fractal dimensions are arbitrarily close to three from below but still exhibit no spin-glass order.
This sharply contrasts with numerical estimates obtained for MK hierarchical lattices with relatively small scale factors and branching numbers, which placed the lower critical dimension near2.522.52.

## Introduction—

While mean-field spin-glass models are now understood with remarkable mathematical precisionParisi;Guerra;Talagrand, finite-dimensional spin-glass models remain far less tractableNS;NS2;NRS;Chatterjee;NRS2;NOO;NS3.
Even basic questions, such as the existence or absence of a spin-glass phase in low dimensions, are not rigorously settled.
Numerical studies suggest the absence of a spin-glass phase at finite temperature in two dimensions and its presence in three dimensionsMcMillan;BM2;McMillan2;BY;HY;HH;SC;KR;SP.
The lower critical dimension is estimated to bedlc≃2.5d_{\rm lc}\simeq 2.5MP;Boettcher;FPV; however, no rigorous derivation of this picture is currently available.

Hierarchical lattices provide a useful setting in which aspects of finite-dimensional spin glasses can be studied using real-space renormalization-group (RG) methods.
In particular, Migdal–Kadanoff (MK) hierarchical latticesMigdal;Kadanoff, specified by a scale factorbband a branching numberss, have long provided a standard framework for applying such RG methods to finite-dimensional spin glassesYS;MBK;SY;JCW;BM;CM;Gingras;ABD;CNC;ANC;AMMP;JK;DTB;DBMB;SM;NH;BKM;AB.
Their fractal dimension,d=1+log⁡s/log⁡bd=1+\log s/\log b, can be varied by changingssandbb, while their recursive structure makes the RG transformation exact.
This exact recursion enables numerical studies of very large systems.
Existing rigorous analyses, however, have largely been restricted to models with sufficiently large fractal dimensionsGardner;CE;Kamphorst, leaving the low-dimensional regime near the putative lower critical dimension poorly understood.
Numerical studies of MK hierarchical lattices with relatively smallssandbbhave estimated the lower critical dimension of the Ising spin glass to bedlcMK≃2.52d_{\rm lc}^{\rm MK}\simeq 2.52DTB.
By contrast, a scaling argument in the large-ss, large-bbregime identifiesd=3d=3as marginalBoettcher, suggesting that the apparent lower-critical behavior may depend not only on the fractal dimension but also on the detailed hierarchical construction.

In this Letter, we introduce a simple and rigorous mechanism for excluding spin-glass order on MK hierarchical lattices with binary couplings.
Instead of iterating the full distributional RG equation, we perform a single exact RG step for each realization.
For a symmetric binary distribution and an even branching numberss, the renormalized interaction vanishes exactly with positive probability.
These zero effective bonds induce an exact bond dilution.
The problem of excluding spin-glass order can then be reduced to bond percolation on the corresponding hierarchical lattice.
This observation yields a rigorous sufficient condition for the absence of spin-glass order.
Whenever the induced dilution exceeds the hierarchical percolation threshold, the probability that the endpoints remain connected decays exponentially with their separation.
Consequently, the endpoint spin-glass correlation vanishes at any temperature, including zero temperature, in the thermodynamic limit.
Under the same condition, we also prove the absence of stiffness.

Several consequences follow immediately.
First, the criterion applies to the MK approximation of the Ising spin glass on the square lattice.
Although the absence of a spin-glass phase in this approximation has long been expectedYS, the present result provides, to the best of our knowledge, the first rigorous proof.
Second, and more unexpectedly, by taking bothssandbbsufficiently large, we construct MK hierarchical lattices that satisfy the no-order criterion even though their fractal dimensions can be made arbitrarily close to three from below.
This result contrasts sharply with the commonly quoted estimatedlcMK≃2.52d_{\rm lc}^{\rm MK}\simeq 2.52DTBand rigorously establishes the no-order side of the scaling prediction thatd=3d=3is marginal in the large-ss, large-bbregimeBoettcher.

We also show that the same dilution mechanism is not restricted to MK hierarchical lattices.
As an example, we apply it to the simplest self-dual hierarchical lattice, whose fractal dimension isd=log⁡5/log⁡2≃2.32d=\log 5/\log 2\simeq 2.32GK;KG2;Nobre.
Previous workONbased on graph duality, the replica method, and real-space RG arguments suggested the absence of a spin-glass phase at finite temperature on this lattice; here we rigorously establish the absence of both spin-glass order and stiffness at all temperatures.

## Absence of spin-glass order on a class of Migdal–Kadanoff hierarchical lattices—

Letb≥2b\geq 2ands≥1s\geq 1denote the scale factor and the branching number, respectively.
The Migdal–Kadanoff (MK) hierarchical lattice is constructed recursively by replacing each edge withssparallel chains, each of lengthbb(see Fig.1in the End Matter).
Generation0consists of a single edge, and the distance between the two endpointsAAandBBat generationnnisrn=bnr_{n}=b^{n}.
The fractal dimension of the lattice isd=1+log⁡s/log⁡bd=1+{\log s}/{\log b}.
For a single generating unit, the Hamiltonian isℋunit=−∑α=1s∑k=0b−1Jα​k​σα,k​σα,k+1,\mathcal{H}_{\rm unit}=-\sum_{\alpha=1}^{s}\sum_{k=0}^{b-1}J_{\alpha k}\,\sigma_{\alpha,k}\sigma_{\alpha,k+1},(1)

where eachσα,k=±1\sigma_{\alpha,k}=\pm 1denotes an Ising spin, withσα,0≡σL\sigma_{\alpha,0}\equiv\sigma_{L}andσα,b≡σR\sigma_{\alpha,b}\equiv\sigma_{R}.
The couplings are independent and identically distributed random variables drawn from the symmetric binary distribution,P​(Ji​j)=δ​(Ji​j−1)/2+δ​(Ji​j+1)/2P(J_{ij})=\delta(J_{ij}-1)/2+\delta(J_{ij}+1)/2.
The Hamiltonian for the Ising spin-glass model on the MK hierarchical lattice at generationnnisHn=−∑(i​j)∈E(n)Ji​j​σi​σjH_{n}=-\sum_{(ij)\in E^{(n)}}J_{ij}\sigma_{i}\sigma_{j},
whereE(n)E^{(n)}denotes the edge set at generationnn. We impose free boundary conditions at the two endpointsAAandBB. The endpoint spin-glass correlation is defined by𝔼​[⟨σA​σB⟩n2]\mathbb{E}\!\left[\langle\sigma_{A}\sigma_{B}\rangle_{n}^{2}\right],
where⟨⋯⟩n\langle\cdots\rangle_{n}denotes the thermal average with respect toHnH_{n}, and𝔼​[⋯]\mathbb{E}[\cdots]denotes the disorder average. The absence of endpoint spin-glass order meanslimn→∞𝔼​[⟨σA​σB⟩n2]=0.\displaystyle\lim_{n\to\infty}\mathbb{E}\!\left[\langle\sigma_{A}\sigma_{B}\rangle_{n}^{2}\right]=0.(2)

Note that if the endpoint spin-glass correlation vanishes, then the square of the conventional spin-glass order parameter,1|V(n)|2​∑i,j∈V(n)𝔼​[⟨σi​σj⟩n2],\displaystyle\frac{1}{|V^{(n)}|^{2}}\sum_{i,j\in V^{(n)}}\mathbb{E}\left[\langle\sigma_{i}\sigma_{j}\rangle_{n}^{2}\right],(3)

also vanishes. Here,V(n)V^{(n)}denotes the vertex set at generationnn.
Therefore, the vanishing of the endpoint spin-glass correlation in Eq. (2) also rules out a nonzero conventional spin-glass order parameter.

Because of the recursive structure of the MK hierarchical latticeKG, summing exactly over the internal spins of a generating unit produces a single effective interactionJL​RJ_{LR}between the two endpoint spins.
At finite temperature, the exact RG equationJKisβ​JL​R\displaystyle\beta J_{LR}=\displaystyle=∑α=1stanh−1⁡(∏k=0b−1tanh⁡(β​Jα​k)),\displaystyle\sum_{\alpha=1}^{s}\tanh^{-1}\left(\prod_{k=0}^{b-1}\tanh(\beta J_{\alpha k})\right),(4)

whereβ\betadenotes the inverse temperature.
Equivalently, the probability distribution of the effective coupling is updated according to the same equation, with equality understood in distribution.

In contrast to the usual approach, which repeatedly iterates this distributional RG equation, we use only a single exact RG step for each realization.
For the symmetric binary distribution, each branch contribution in Eq. (4) has the same magnitude and an independent random sign. Hence, ifssis even, the effective interactionJL​RJ_{LR}vanishes exactly when the numbers of positive and negative branch contributions are equal. The probability of this event isps,b=(ss/2)​12s.\displaystyle p_{s,b}=\binom{s}{s/2}\frac{1}{2^{s}}.(5)

For the symmetric binary distribution, this probability is independent of the scale factorbb. This independence is special to the symmetric case; as discussed below,ps,bp_{s,b}generally depends onbbfor asymmetric binary distributions.

After applying this single RG step to every elementary unit of the MK hierarchical lattice at generationnn, we obtain an MK hierarchical lattice at generationn−1n-1in which each effective bond is absent with probabilityps,bp_{s,b}.
We now discard the values of the nonzero effective interactions and retain only their connectivity.
If the endpointsAAandBBare disconnected after the zero effective bonds are removed, then the Hamiltonian decomposes into independent components containingAAandBB, respectively.
Since there is no external field and the endpoint boundary conditions are free, this implies⟨σA​σB⟩n=0.\displaystyle\langle\sigma_{A}\sigma_{B}\rangle_{n}=0.(6)

Therefore, the spin-glass correlation is bounded above by the probability thatAAandBBremain connected through nonzero effective bonds.
This reduces the problem to bond percolation on the MK hierarchical lattice.
For a single MK generating unit, the probability that no path connects its two endpoints is[1−(1−ps,b)b]s[1-(1-p_{s,b})^{b}]^{s}.
Thus, if the initial vacancy probabilityps,bp_{s,b}satisfiesps,b<[1−(1−ps,b)b]s,\displaystyle p_{s,b}<\left[1-(1-p_{s,b})^{b}\right]^{s},(7)

then the vacancy probability increases under the hierarchical percolation recursion.
Equivalently, the endpoint connectivity probability decreases under iteration.
A detailed proof, including the fixed-point analysis of the percolation recursion and the derivation of the exponential bound, is given in the End Matter.
This yields the following sufficient condition for the absence of spin-glass order.

## Theorem 1.

Letssbe even. Suppose thatps,bp_{s,b}satisfies condition (7). Then there exist constantsC>0C>0andc>0c>0, independent ofnn, such that𝔼​[⟨σA​σB⟩n2]≤C​exp⁡(−c​rn)\mathbb{E}\!\left[\langle\sigma_{A}\sigma_{B}\rangle_{n}^{2}\right]\leq C\exp(-cr_{n}).
In particular,limn→∞𝔼​[⟨σA​σB⟩n2]=0.\displaystyle\lim_{n\to\infty}\mathbb{E}\!\left[\langle\sigma_{A}\sigma_{B}\rangle_{n}^{2}\right]=0.(8)

Hence there is no spin-glass order at any finite temperature.

Condition (7) has several immediate consequences.
For fixedss, the right-hand side of condition (7) increases withbb. Since the fractal dimensiondddecreases asbbincreases, the no-order criterion becomes easier to satisfy at lower fractal dimensions.

Fors=bs=b, corresponding tod=2d=2, condition (7) is satisfied for any evenss.
This case includes the MK approximation to the Ising spin glass on the square lattice, and Theorem 1 therefore gives a rigorous proof of the absence of spin-glass order within this approximation.
By contrast, fors=b2s=b^{2}, corresponding tod=3d=3, condition (7) is not satisfied for any evenbb. This is consistent with previous studies indicating the existence of a spin-glass phase in three dimensions within the MK approximationSY. We emphasize, however, that condition (7) is only sufficient: when it fails, our method does not imply the presence of spin-glass order.

For example, condition (7) is satisfied for(s,b)=(6,5)(s,b)=(6,5)and(s,b)=(8,6)(s,b)=(8,6), corresponding tod≃2.11d\simeq 2.11andd≃2.16d\simeq 2.16, respectively.
On the other hand, it is not satisfied for(s,b)=(6,3)(s,b)=(6,3), corresponding tod≃2.63d\simeq 2.63.
This pattern is consistent with the commonly quoted estimatedlcMK≃2.52d_{\rm lc}^{\rm MK}\simeq 2.52, which was inferred from numerical studies of MK hierarchical lattices with relatively small values ofssandbbDTB.

However, the criterion is not sharp.
For instance, condition (7) is not satisfied for(s,b)=(4,3)(s,b)=(4,3),(s,b)=(6,4)(s,b)=(6,4), or(s,b)=(8,5)(s,b)=(8,5), although these lattices have fractal dimensionsd≃2.26d\simeq 2.26,d≃2.29d\simeq 2.29, andd≃2.29d\simeq 2.29, respectively.
Previous studies suggest the absence of a spin-glass phase in such casesDTB, but the present one-step dilution criterion is not strong enough to establish this absence.
One possible way to improve the criterion is to perform two or more exact RG steps before making the percolation comparison, thereby increasing the probability that the effective interaction vanishes.
This refinement is useful in the analysis of the self-dual hierarchical lattice discussed below.

The same condition leads to a more striking consequence.
For large evenss, Stirling’s formula givesps,b≃2/(π​s)p_{s,b}\simeq\sqrt{{2}/{(\pi s)}}.
We then choosebbto be of the formb≃s​π/2​(log⁡s−log⁡log⁡s+C)b\simeq\sqrt{{s\pi}/{2}}\bigl(\log s-\log\log s+C\bigr),
whereCCis a constant independent ofss. Any fixedC>log⁡2C>\log 2ensures that condition (7)
is satisfied for all sufficiently large evenss.
The corresponding fractal dimension isd=1+log⁡slog⁡b≃3−4​log⁡log⁡s+O​(1)log⁡s.\displaystyle d=1+\frac{\log s}{\log b}\simeq 3-\frac{4\log\log s+O(1)}{\log s}.(9)

Thus, by takingssandbbsufficiently large, one can construct MK hierarchical lattices that satisfy the no-order criterion even though their fractal dimensions are arbitrarily close to three from below.
This contrasts with the numerical estimatedlcMK≃2.52d_{\rm lc}^{\rm MK}\simeq 2.52DTB, obtained from MK hierarchical lattices with relatively small scale factors and branching numbers.
Our result therefore shows that, within the family of MK hierarchical lattices, the lower-critical behavior of Ising spin glasses depends not only on the fractal dimension but also on the detailed hierarchical construction.

A simple scaling argumentBoettcheroffers a heuristic interpretation.
For sufficiently largebb, a single RG step reduces the characteristic interaction scale along each branch by a factor of1/b1/b, while summing the approximately independent contributions froms=bd−1s=b^{d-1}branches enhances it by a factor ofs\sqrt{s}.
The net rescaling factor is therefores/b=b(d−3)/2{\sqrt{s}}/{b}=b^{(d-3)/2}, so thatd=3d=3is marginal in the large-ss, large-bbregime.
Our proof rigorously establishes the no-order side of this scaling argument.
This scaling reflects a connectivity effect specific to the MK hierarchical construction and should not be interpreted as a direct statement about regular lattices in Euclidean space, for which the lower critical dimension is estimated to bedlc≃2.5d_{\rm lc}\simeq 2.5MP;Boettcher;FPV.

We next consider the zero-temperature limit. AtT=0T=0, the exact RG equationNobreisJL​R=∑α=1ssgn⁡(∏k=0b−1Jα​k)​min0≤k≤b−1⁡|Jα​k|.\displaystyle J_{LR}=\sum_{\alpha=1}^{s}\operatorname{sgn}\left(\prod_{k=0}^{b-1}J_{\alpha k}\right)\min_{0\leq k\leq b-1}|J_{\alpha k}|.(10)

For the symmetric binary distribution, each branch contribution again has the same magnitude and an independent random sign.
Therefore, for evenss, the probability that the effective interaction vanishes after one RG step is againps,bp_{s,b}. The same percolation argument then gives the zero-temperature counterpart of Theorem 1.

## Theorem 2.

Letssbe even and suppose that condition (7) holds.
Then there exist constantsC>0C>0andc>0c>0, independent ofnn,
such thatlimβ→∞𝔼​[⟨σA​σB⟩n2]≤C​exp⁡(−c​rn)\lim_{\beta\to\infty}\mathbb{E}\left[\langle\sigma_{A}\sigma_{B}\rangle_{n}^{2}\right]\leq C\exp(-cr_{n}).
In particular,limn→∞limβ→∞𝔼​[⟨σA​σB⟩n2]=0.\lim_{n\to\infty}\lim_{\beta\to\infty}\mathbb{E}\left[\langle\sigma_{A}\sigma_{B}\rangle_{n}^{2}\right]=0.(11)

Thus there is no spin-glass order even at zero temperature.

The same exponential bound implies that, in this regime, the zero-temperature correlation length is finite.
The system is therefore noncritical and lies in the paramagnetic regime even at zero temperature, in agreement with previous numerical studiesGingras;ANC.
This conclusion relies crucially on the discreteness of the binary coupling distribution and on the branching number being even.
For oddssor continuous coupling distributions such as the Gaussian distribution, systems below the lower critical dimension are instead generally expected to be critical at zero temperature: the correlation length diverges, and the low-temperature behavior is governed by a zero-temperature fixed pointJK.

We finally discuss stiffness.
At zero temperature, stiffness is characterized by the boundary-condition energy differenceΔ​En=En++−En+−\Delta E_{n}=E_{n}^{++}-E_{n}^{+-}; at finite temperature, the analogous
quantity isΔ​Fn=Fn++−Fn+−\Delta F_{n}=F_{n}^{++}-F_{n}^{+-}.
Here, the superscripts(++)(++)and(+−)(+-)denote the boundary conditions(σA,σB)=(1,1)(\sigma_{A},\sigma_{B})=(1,1)and(1,−1)(1,-1), respectively.
If|Δ​En|∼rnθ|\Delta E_{n}|\sim r_{n}^{\theta},θ\thetais the stiffness exponent.
A positive value,θ>0\theta>0, indicates that large-scale domain-wall excitations become increasingly costly and is commonly regarded as evidence for a stable spin-glass phase.
Below the lower critical dimension, Gaussian couplings typically yieldθ<0\theta<0, whereas binary couplings exhibit an apparent pinning near
zero because of ground-state degeneracyAMMP.

In the present setting, our dilution argument gives a stronger conclusion.
If no path of nonzero effective interactions connectsAAandBB, changing the boundary condition atBBcannot affect the component containingAA.
By spin-flip symmetry, the component containingBBhas the same energy at zero temperature, or the same free energy at finite temperature, forσB=1\sigma_{B}=1andσB=−1\sigma_{B}=-1.
Thus, on the disconnection event,Δ​En=0\Delta E_{n}=0at zero temperature andΔ​Fn=0\Delta F_{n}=0at finite temperature.
Combining this observation with Theorems 1 and 2 gives the following result.

## Theorem 3.

Letssbe even and suppose that condition (7) holds.
Then there exist constantsC>0C>0andc>0c>0, independent ofnn, such that, at zero temperature,Pr⁡[Δ​En=0]≥1−C​e−c​rn\Pr[\Delta E_{n}=0]\geq 1-Ce^{-cr_{n}},
and at finite temperature,Pr⁡[Δ​Fn=0]≥1−C​e−c​rn\Pr[\Delta F_{n}=0]\geq 1-Ce^{-cr_{n}}.
Therefore, the boundary-condition response vanishes in probability in the thermodynamic limit, and the system has no stiffness at any temperature.

This result is stronger than the apparentθ≃0\theta\simeq 0behavior often observed for discrete coupling distributions below the lower critical dimensionAMMP.
In the present regime, the probability that the boundary-condition energy difference vanishes at zero temperature, or that the corresponding free-energy difference vanishes at finite temperature, approaches one exponentially fast as the endpoint distance increases.
Thus, the conventional power-law definition of a stiffness exponent is not appropriate. Formally, one may regard the behavior as corresponding toθ=−∞\theta=-\infty, rather than to genuine power-law scaling withθ=0\theta=0.
This extreme behavior appears to be a special consequence of combining a discrete coupling distribution with an even branching number and is not expected to persist when the branching number is odd or the coupling distribution is continuous.

## Extensions and limitations of the dilution criterion—

So far, we have focused on the symmetric binary distribution. The same dilution argument can be extended to an asymmetric binary distribution,P​(Ji​j)=ρ​δ​(Ji​j−1)+(1−ρ)​δ​(Ji​j+1)P(J_{ij})=\rho\delta(J_{ij}-1)+(1-\rho)\delta(J_{ij}+1)\quad(0≤ρ≤1)(0\leq\rho\leq 1).
For evenss, the probability that the renormalized interaction vanishes after one RG step isps,b​(ρ)=(ss/2)​[1−(2​ρ−1)2​b4]s/2.\displaystyle p_{s,b}(\rho)=\binom{s}{s/2}\left[\frac{1-(2\rho-1)^{2b}}{4}\right]^{s/2}.(12)

Unlike in the symmetric case, this probability depends on bothssandbb.
The percolation criterion itself is unchanged. Namely, ifps,b​(ρ)<[1−{1−ps,b​(ρ)}b]sp_{s,b}(\rho)<\left[1-\{1-p_{s,b}(\rho)\}^{b}\right]^{s},
then the induced dilution exceeds the corresponding percolation threshold, and the endpoint connectivity probability decays exponentially with the distance between the endpoints.
Consequently, both spin-glass order and stiffness are absent at all temperatures.
Moreover, in the asymmetric case, the same argument also rules out ferromagnetic long-range order as diagnosed by the endpoint correlation, because|𝔼​[⟨σA​σB⟩n]|\left|\mathbb{E}[\langle\sigma_{A}\sigma_{B}\rangle_{n}]\right|is bounded by the probability that the two endpoints are connected through nonzero effective interactions.

The argument also applies, in principle, to more general discrete coupling distributions whenever a single RG step produces an atom atJL​R=0J_{LR}=0with probabilityp>0p>0. In such cases, the same percolation comparison gives a sufficient condition for the absence of spin-glass order, withppreplacingps,bp_{s,b}.

By contrast, the present argument does not apply to continuous coupling distributions such as the Gaussian distribution.
The percolation comparison requires an atom of positive mass atJL​R=0J_{LR}=0, because only bonds that vanish exactly can be removed without changing the Hamiltonian.
For a continuous distribution, exact cancellation occurs with probability zero, so the induced vacancy probability is zero.
A similar obstruction arises for binary couplings whenssis odd: an odd number of equal-magnitude branch contributions cannot cancel exactly.
The one-step criterion therefore yields no conclusion in either case.

## Absence of spin-glass order on a self-dual hierarchical lattice—

We next apply the same dilution mechanism to the Ising spin-glass model on the self-dual hierarchical lattice, whose fractal dimension isd=log⁡5/log⁡2≃2.32d=\log 5/\log 2\simeq 2.32.
The generating unit consists of two external spins,σL\sigma_{L}andσR\sigma_{R}, two internal spins,σ1\sigma_{1}andσ2\sigma_{2}, and five bonds.
Its Hamiltonian isℋunit\displaystyle\mathcal{H}_{\rm unit}=\displaystyle=−JL​1​σL​σ1−J1​R​σ1​σR−JL​2​σL​σ2−J2​R​σ2​σR\displaystyle-J_{L1}\sigma_{L}\sigma_{1}-J_{1R}\sigma_{1}\sigma_{R}-J_{L2}\sigma_{L}\sigma_{2}-J_{2R}\sigma_{2}\sigma_{R}(13)−J12​σ1​σ2.\displaystyle-J_{12}\sigma_{1}\sigma_{2}.

Compared with the generating unit of the MK hierarchical lattice withs=b=2s=b=2, the present generating unit contains an additional bondJ12J_{12}connecting the two internal spins.
By summing exactly over the internal spinsσ1\sigma_{1}andσ2\sigma_{2}, we obtain an effective interaction betweenσL\sigma_{L}andσR\sigma_{R}.
The explicit RG equations at finite and zero temperature are given in the End Matter.
Here we use only the vacancy probabilities resulting from these exact RG steps.

On the self-dual hierarchical lattice, letqqdenote the probability that a given effective bond is absent. For a single generating unit, the probability that no path connects the two endpoints isΨ​(q)=q2​(2+2​q−5​q2+2​q3)\Psi(q)=q^{2}(2+2q-5q^{2}+2q^{3}).
Thus, ifq<Ψ​(q)q<\Psi(q), the vacancy probability increases under successive iterations of the hierarchical percolation recursion.
In this case, the absence of spin-glass order and stiffness follows from the same connectivity argument used in Theorem 1.
The mapq↦Ψ​(q)q\mapsto\Psi(q)has an unstable fixed point atq=1/2q=1/2, and any initial valueq>1/2q>1/2flows toq=1q=1under iteration.
It therefore remains to show that the vacancy probability exceeds1/21/2after finitely many exact RG steps.

For the symmetric binary distribution, direct enumeration using the exact RG equations givesq1=1/2q_{1}=1/2after one RG step, at every finite temperature and at zero temperature. This value is exactly the percolation threshold and is therefore not sufficient by itself.
We therefore perform a second exact RG step.
The proof of Theorem 4 in the End Matter givesq2=261/512q_{2}=261/512at finite temperature andq2=2255/4096q_{2}=2255/4096atT=0T=0.
Both are strictly larger than1/21/2.
Hence, the vacancy probability flows to one under further hierarchical iterations, and the same connectivity argument used in Theorem 1 proves the absence of spin-glass order and stiffness.

## Theorem 4.

In the thermodynamic limit, the Ising spin glass with symmetric binary couplings on the self-dual hierarchical lattice withd=log⁡5/log⁡2d=\log 5/\log 2exhibits neither spin-glass order nor stiffness at any temperature, including zero temperature.

## Conclusions—

Rigorous analysis of finite-dimensional spin glasses remains a challenging problem.
In this Letter, we addressed this problem through an exact real-space RG analysis on hierarchical lattices. We introduced a rigorous dilution criterion for excluding spin-glass order.
For symmetric binary couplings and an even branching number, a single exact RG step creates zero effective bonds with positive probability.
When this induced dilution exceeds the corresponding hierarchical percolation threshold, the endpoint connectivity probability decays exponentially with distance.
Consequently, both spin-glass order and stiffness are absent at all temperatures, including zero temperature.

This criterion proves the absence of spin-glass order and stiffness in the Ising spin-glass model on the square lattice within the MK approximation.
In the asymptotic large-ss, large-bbregime, the criterion applies to families of MK hierarchical lattices whose fractal dimensions approach three from below, thereby providing rigorous support for earlier scaling arguments identifyingd=3d=3as the marginal dimensionBoettcher.
Because this result emerges only for sufficiently largessandbb, it does not conflict with the commonly quoted estimatedlcMK≃2.52d_{\rm lc}^{\rm MK}\simeq 2.52, obtained from MK hierarchical lattices with relatively smallbbandss.
Rather, it shows that the lower-critical behavior within the family of MK hierarchical lattices depends sensitively on the detailed lattice construction and not on the fractal dimension alone.
The numerical proximity of the MK estimate todlc≃2.5d_{\rm lc}\simeq 2.5for regular lattices in Euclidean spaceMP;Boettcher;FPVshould not be interpreted as evidence for a simple quantitative correspondence between the two settings.

This mechanism also proves the absence of endpoint spin-glass order and stiffness on the self-dual hierarchical lattice withd=log⁡5/log⁡2d=\log 5/\log 2.
Several important cases remain open, including the case of an odd branching number, continuous coupling distributions, and even-branching MK lattices for which the sufficient condition is not satisfied.

An important further problem is whether the present method can be extended to spin-glass models in two dimensions, where no spin-glass phase is expected at finite temperature.
Previous work has provided analytical evidence for the absence of such a phase on both the self-dual hierarchical lattice studied here and the square lattice by combining graph duality, the replica method, and real-space RG argumentsON.
The approach based on exact dilution may provide a useful new route toward a rigorous understanding of this problem.

This work was supported by JST BOOST, Japan (Grant No. JPMJBY24B6), and JSPS KAKENHI (Grant No. 24K16973).
This work was was supported by the Cross-ministerial Strategic Innovation Promotion Program (SIP) of the Cabinet Office (No. 23836436).

## References
- (1)G. Parisi,
A sequence of approximated solutions to the S-K model for spin glasses,
J. Phys. A13,L115 (1980).
- (2)F. Guerra,
Broken replica symmetry bounds in the mean field spin glass model,
Comm. Math. Phys.233,1 (2003).
- (3)M. Talagrand,
The Parisi formula,
Ann. Math.163,221 (2006).
- (4)C. M. Newman and D. L. Stein,
Non-Mean-Field Behavior of Realistic Spin Glasses,
Phys. Rev. Lett.76,515 (1996).
- (5)C. M. Newman and D. L. Stein,
Nature of Ground State Incongruence in Two-Dimensional Spin Glasses,
Phys. Rev. Lett.84,3966 (2000).
- (6)C. M. Newman, N. Read, and D. L. Stein,
Proof of single-replica equivalence in short-range spin glasses,
Phys. Rev. Lett.130,077102 (2023).
- (7)C. M. Newman, N. Read, and D. L. Stein,
inSpin Glass Theory and Far Beyond - Replica Symmetry Breaking after 40 Years, edited by P. Charbonneau, E. Marinari, G. Parisi, F. Ricci-Tersenghi, G. Sicuro, F. Zamponi, and M. Mezard (World Scientific, Singapore, 2023).
- (8)S. Chatterjee,
Spin glass phase at zero temperature in the Edwards-Anderson model,
arXiv:2301.04112.
- (9)H. Nishimori, M. Ohzeki, and M. Okuyama,
Temperature chaos as a logical consequence of the reentrant transition in spin glasses,
Phys. Rev. E112,044140 (2025).
- (10)C. M. Newman and D. L. Stein,
Ground State Excitations and Energy Fluctuations in Short-Range Spin Glasses,
J. Stat. Phys.193,70 (2026).
- (11)W. L. McMillan,
Domain-wall renormalization-group study of the two-dimensional random Ising model,
Phys. Rev. B29,4026 (1983).
- (12)A. J. Bray and M. A. Moore,
Lower critical dimension of Ising spin glasses: a numerical study,
J. Phys. C17,L463 (1984).
- (13)W. L. McMillan,
Domain-wall renormalization-group study of the three-dimensional random Ising model,
Phys. Rev. B30,476 (1984).
- (14)R. N. Bhatt and A. P. Young,
Numerical studies of Ising spin glasses in two, three, and four dimensions,
Phys. Rev. B37,5606 (1988).
- (15)A. K. Hartmann and A. P. Young,
Lower Critical Dimension of Ising Spin Glasses,
Phys. Rev. B64,180404 (2001).
- (16)J. Houdayer and A. K. Hartmann,
Low-temperature behavior of two-dimensional Gaussian Ising spin glasses,
Phys. Rev. B70,014418 (2004).
- (17)R. R. P. Singh and S. Chakravarty,
Critical Behavior of an Ising Spin-Glass,
Phys. Rev. Lett.57,245 (1986).
- (18)N. Kawashima and H. Rieger,
Finite-size scaling analysis of exact ground states for±J\pm Jspin glass models in two dimensions,
Europhys. Lett.39,85 (1997).
- (19)R. Sungthong and J. Poulter,
The critical temperature of the two-dimensional±J\pm JIsing spin glass,
J. Phys. A: Math. Gen.36,6675 (2003).
- (20)S. Franz, G. Parisi, and M. A. Virasoro,
Interfaces and lower critical dimension in a spin glass model,
J. Phys. I (France) 4, 1657 (1994).
- (21)S. Boettcher,
Stiffness of the Edwards-Anderson Model in all Dimensions,
Phys. Rev. Lett.95,197205 (2005).
- (22)A. Maiorano and G. Parisi,
Support for the value 5/2 for the spin glass lower critical dimension at zero magnetic field,
Proc. Natl. Acad. Sci. USA115, 5129 (2018).
- (23)A. A. Migdal,
Phase transitions in gauge and spin-lattice systems,
Zh. Eksp. Teor. Fiz.69,1457 (1975).
- (24)L. P. Kadanoff,
Notes on Migdal’s recursion formulas,
Ann. Phys.100,359 (1976).
- (25)A. P. Young and R. B. Stinchcombe,
Real-space renormalization group calculations for spin glasses and dilute magnets,
J. Phys. C: Solid State Phys.9,4419 (1976).
- (26)B. W. Southern and A. P. Young,
Real space rescaling study of spin glass behaviour in three dimensions,
J. Phys. C: Solid State Phys.10,2179 (1977).
- (27)C. Jayaprakash, J. Chalupa, and M. Wortis,
Spin-glass behavior from Migdal’s recursion relations,
Phys. Rev. B15,1495 (1977).
- (28)S. R. McKay, A. N. Berker, and S. Kirkpatrick,
Spin-Glass Behavior in Frustrated Ising Models with Chaotic Renormalization-Group Trajectories,
Phys. Rev. Lett.48,767 (1982).
- (29)A. J. Bray and M. A. Moore,
Chaotic Nature of the Spin-Glass Phase,
Phys. Rev. Lett.58,57 (1987).
- (30)E. M. F. Curado and J.-L. Meunier,
Spin-glass in low dimensions and the Migdal-Kadanoff approximation,
Physica (Amsterdam)149A,164 (1988).
- (31)M. J. P. Gingras,
Degenerate and nondegenerate ground states in bimodal vector spin glasses,
Phys. Rev. B46,14900 (1992).
- (32)M. Nifle and H. J. Hilhorst,
New critical-point exponent and new scaling laws for short-range Ising spin glasses,
Phys. Rev. Lett.68,2992 (1992).
- (33)M. A. Moore, H. Bokil, and B. Drossel,
Evidence for the Droplet Picture of Spin Glasses,
Phys. Rev. Lett.81,4252 (1998).
- (34)E. M. F. Curado, F. D. Nobre, and S. Coutinho,
Ground-state degeneracies of Ising spin glasses on diamond hierarchical lattices,
Phys. Rev. E60,3761 (1999).
- (35)B. Drossel, H. Bokil, M. A. Moore, and A. J. Bray,
The link overlap and finite size effects for the 3D Ising spin glass,
Eur. Phys. J. B13,369 (2000).
- (36)R. F. S. Andrade, E. Nogueira, Jr., and S. Coutinho,
Ising spin glass by the transfer matrix approach,
Phys. Rev. B68,104523 (2003).
- (37)C. Amoruso, E. Marinari, O. C. Martin, and A. Pagnani,
Scalings of Domain Wall Energies in Two Dimensional Ising Spin Glasses,
Phys. Rev. Lett.91,087201 (2003).
- (38)M. Sasaki and O. C. Martin,
Temperature Chaos, Rejuvenation and Memory in Migdal-Kadanoff Spin Glasses,
Phys. Rev. Lett.91,097201 (2003).
- (39)J.-P. Bouchaud, F. Krzakala, and O. C. Martin,
Energy exponents and corrections to scaling in Ising spin glasses,
Phys. Rev. B68,224404 (2003).
- (40)T. Jörg and F. Krzakala,
The nature of the different zero-temperature phases in discrete two-dimensional spin glasses: Entropy, universality, chaos and cascades in the renormalization group flow,
J. Stat. Mech. L01001 (2012).
- (41)M. C. Angelini and G. Biroli,
Spin Glass in a Field: A New Zero-Temperature Fixed Point in Finite Dimensions,
Phys. Rev. Lett.114,095701 (2015).
- (42)M. Demirtaş, A. Tuncer, and A. N. Berker,
Lower-critical spin-glass dimension from 23 sequenced hierarchical models,
Phys. Rev. E92,022136 (2015).
- (43)E. Gardner,
A spin glass model on a hierarchical lattice,
J. Phys. (Paris)45,1755 (1984).
- (44)P. Collet and J. P. Eckmann,
A spin-glass model with random couplings,
Commun. Math. Phys.93,379 (1984).
- (45)S. O. Kamphorst,
A mixed phase transition for a hierarchical spin glass,
J. Stat. Phys.45,369 (1986).
- (46)R. B. Griffiths and M. Kaufman,
Spin systems on hierarchical lattices. Introduction and thermodynamic limit,
Phys. Rev. B26,5022 (1982).
- (47)M. Kaufman and R. B. Griffiths,
Spin systems on hierarchical lattices. II. Some examples of soluble models,
Phys. Rev. B30, 244 (1984).
- (48)F. D. Nobre,
Real-space renormalization-group approaches for two-dimensional Gaussian Ising spin glass,
Phys. Lett. A250,163 (1998).
- (49)M. Ohzeki and H. Nishimori,
Analytical evidence for the absence of spin glass transition on self-dual lattices,
J. Phys. A: Math. Theor.42,332001 (2009).
- (50)M. Kaufman and R. B. Griffiths,
Exactly soluble Ising models on hierarchical lattices,
Phys. Rev. B24,496 (1981).

## IEnd Matter

## Proof of Theorem 1—

We prove Theorem 1.
After one exact RG step, each effective bond in the reduced hierarchical lattice is absent with probabilityps,bp_{s,b}.
We useps,bp_{s,b}as the initial vacancy probability for the percolation recursion.

Letyny_{n}denote the probability that no path of nonzero effective interactions connects the endpointsAAandBBin a generation-nnMK hierarchical lattice.
Then, by the hierarchical construction,yn≥[1−(1−yn−1)b]s,y1=ps,b.\displaystyle y_{n}\geq\left[1-(1-y_{n-1})^{b}\right]^{s},\qquad y_{1}=p_{s,b}.(14)

Equivalently, in terms of the connectivity probabilityxn=1−ynx_{n}=1-y_{n}, we havexn≤f​(xn−1),x1=1−ps,b,\displaystyle x_{n}\leq f(x_{n-1}),\qquad x_{1}=1-p_{s,b},(15)

wheref​(x)=1−(1−xb)s.\displaystyle f(x)=1-\left(1-x^{b}\right)^{s}.(16)

The functionffis strictly increasing on[0,1][0,1].
We next show thatffhas a unique nontrivial fixed point in(0,1)(0,1)fors>1s>1.
Indeed, a nontrivial fixed pointx∈(0,1)x\in(0,1)satisfiesx=1−(1−xb)s,\displaystyle x=1-(1-x^{b})^{s},(17)

or equivalentlyRb​(x):=log⁡(1−x)log⁡(1−xb)=s.\displaystyle R_{b}(x):=\frac{\log(1-x)}{\log(1-x^{b})}=s.(18)

The functionRbR_{b}is strictly decreasing on(0,1)(0,1).
Moreover,limx↓0Rb​(x)=∞,limx↑1Rb​(x)=1.\displaystyle\lim_{x\downarrow 0}R_{b}(x)=\infty,\qquad\lim_{x\uparrow 1}R_{b}(x)=1.(19)

Hence, fors>1s>1, the equationRb​(x)=sR_{b}(x)=shas exactly one solution in(0,1)(0,1).
Thus,ffhas exactly one nontrivial fixed point in(0,1)(0,1), in addition to the trivial fixed points0and11.

Condition (7) is equivalent tof​(x1)<x1.\displaystyle f(x_{1})<x_{1}.(20)

Therefore,x1x_{1}lies below the unique nontrivial fixed point.
Sincef​(x)<xf(x)<xbelow the nontrivial fixed point andffis increasing, the sequence(xn)(x_{n})decreases monotonically to zero.
Since the endpoint spin correlation vanishes on the disconnection event and is bounded in absolute value by one otherwise, we have𝔼​[⟨σA​σB⟩n2]≤xn.\displaystyle\mathbb{E}\!\left[\langle\sigma_{A}\sigma_{B}\rangle_{n}^{2}\right]\leq x_{n}.(21)

It follows thatlimn→∞𝔼​[⟨σA​σB⟩n2]≤limn→∞xn=0.\displaystyle\lim_{n\to\infty}\mathbb{E}\!\left[\langle\sigma_{A}\sigma_{B}\rangle_{n}^{2}\right]\leq\lim_{n\to\infty}x_{n}=0.(22)Figure 1:First two generations of the MK hierarchical lattice fors=b=2s=b=2. Each bond is replaced by two parallel chains of two bonds.

It remains to estimate the rate of decay.
Sincexn→0x_{n}\to 0, we can choosen0n_{0}sufficiently large so thatλ:=s1/(b−1)​xn0<1.\displaystyle\lambda:=s^{1/(b-1)}x_{n_{0}}<1.(23)

Usingf​(x)=1−(1−xb)s≤s​xb,\displaystyle f(x)=1-\left(1-x^{b}\right)^{s}\leq sx^{b},(24)

we obtain, for alln≥n0n\geq n_{0},xn≤sbn−n0−1b−1​xn0bn−n0=s−1b−1​(s1/(b−1)​xn0)bn−n0.\displaystyle x_{n}\leq s^{\frac{b^{n-n_{0}}-1}{b-1}}x_{n_{0}}^{b^{n-n_{0}}}=s^{-\frac{1}{b-1}}\left(s^{1/(b-1)}x_{n_{0}}\right)^{b^{n-n_{0}}}.(25)

Thus,xn≤C0​λbn−n0,C0=s−1/(b−1).\displaystyle x_{n}\leq C_{0}\lambda^{b^{n-n_{0}}},\qquad C_{0}=s^{-1/(b-1)}.(26)

Sincern=bnr_{n}=b^{n}, this bound can be written asxn≤C​e−c​rn\displaystyle x_{n}\leq Ce^{-cr_{n}}(27)

for some constantsC>0C>0andc>0c>0. Therefore,𝔼​[⟨σA​σB⟩n2]≤xn≤C​e−c​rn,\displaystyle\mathbb{E}\!\left[\langle\sigma_{A}\sigma_{B}\rangle_{n}^{2}\right]\leq x_{n}\leq Ce^{-cr_{n}},(28)

which proves Theorem 1.

## Proof of Theorem 4—

We first record the exact RG equations used in the direct enumeration.
For the self-dual generating unit defined in the main text, summing over
the two internal spins givestL​R=tL​1​t1​R+tL​1​t12​t2​R+tL​2​t12​t1​R+tL​2​t2​R1+tL​1​tL​2​t12+t12​t1​R​t2​R+tL​1​tL​2​t1​R​t2​R,t_{LR}=\frac{t_{L1}t_{1R}+t_{L1}t_{12}t_{2R}+t_{L2}t_{12}t_{1R}+t_{L2}t_{2R}}{1+t_{L1}t_{L2}t_{12}+t_{12}t_{1R}t_{2R}+t_{L1}t_{L2}t_{1R}t_{2R}},(29)

whereti​j=tanh⁡(β​Ji​j)t_{ij}=\tanh(\beta J_{ij})andtL​R=tanh⁡(β​JL​R)t_{LR}=\tanh(\beta J_{LR}). At zero temperature, the corresponding
exact RG equationNobreisJL​R=\displaystyle J_{LR}={}12max(J12+|JL​1+JL​2+J1​R+J2​R|,\displaystyle\frac{1}{2}\max\Bigl(J_{12}+\left|J_{L1}+J_{L2}+J_{1R}+J_{2R}\right|,−J12+|JL​1−JL​2+J1​R−J2​R|)\displaystyle\hskip 79.6678pt-J_{12}+\left|J_{L1}-J_{L2}+J_{1R}-J_{2R}\right|\Bigr)−12max(J12+|JL​1+JL​2−J1​R−J2​R|,\displaystyle-\frac{1}{2}\max\Bigl(J_{12}+\left|J_{L1}+J_{L2}-J_{1R}-J_{2R}\right|,−J12+|JL​1−JL​2−J1​R+J2​R|).\displaystyle\hskip 79.6678pt-J_{12}+\left|J_{L1}-J_{L2}-J_{1R}+J_{2R}\right|\Bigr).(30)

For bond percolation on the self-dual hierarchical lattice, the vacancy
probability transforms asΨ​(q)=q2​(2+2​q−5​q2+2​q3).\Psi(q)=q^{2}(2+2q-5q^{2}+2q^{3}).(31)

SinceΨ​(q)−q=q​(q−1)​(2​q−1)​(q2−q−1),\Psi(q)-q=q(q-1)(2q-1)(q^{2}-q-1),(32)

we haveΨ​(q)>q\Psi(q)>qfor1/2<q<11/2<q<1.
Hence, onceq>1/2q>1/2, the vacancy probability flows to one under further hierarchical iterations.

We now summarize the direct enumeration.
For the symmetric binary distribution, the RG equation at finite temperature yieldstL​R=0\displaystyle t_{LR}=0(33)

for1616of the252^{5}bond configurations.
The remaining configurations yield four nonzero values,tL​R=±t+,±t−,\displaystyle t_{LR}=\pm t_{+},\ \pm t_{-},(34)

each occurring with probability1/81/8, wheret+=2​t2​(1+t)1+2​t3+t4,t−=2​t2​(1−t)1−2​t3+t4,t=tanh⁡β.t_{+}=\frac{2t^{2}(1+t)}{1+2t^{3}+t^{4}},\qquad t_{-}=\frac{2t^{2}(1-t)}{1-2t^{3}+t^{4}},\qquad t=\tanh\beta.(35)

Thus, the vacancy probability after one RG step isq1=12.q_{1}=\frac{1}{2}.(36)

A direct enumeration of the second RG step, using the above five-point distribution, givesq2=261512>12.q_{2}=\frac{261}{512}>\frac{1}{2}.(37)

Therefore, at any finite temperature, two RG steps produce a vacancy probability that exceeds the percolation threshold.

At zero temperature, the first RG step yieldsJL​R=0,±1,±2\displaystyle J_{LR}=0,\ \pm 1,\ \pm 2(38)

with probabilities12,18,18,18,18,\displaystyle\frac{1}{2},\quad\frac{1}{8},\quad\frac{1}{8},\quad\frac{1}{8},\quad\frac{1}{8},(39)

respectively.
Applying the zero-temperature RG equation once more yieldsq2=22554096>12.q_{2}=\frac{2255}{4096}>\frac{1}{2}.(40)

Thus, the vacancy probability again exceeds the threshold after two RG steps.
This proves the absence of endpoint spin-glass order and stiffness on the self-dual hierarchical lattice.

## 


- 


Major funding support from
