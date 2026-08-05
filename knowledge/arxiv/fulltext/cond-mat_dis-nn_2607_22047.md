# Multiplicity of Stable Attractors in Disordered Neural Models

**arXiv ID**: 2607.22047v1
**Authors**: Raffaele Marino, Roberto Livi, Antonio Politi
**Published**: 2026-07-24
**Categories**: cond-mat.dis-nn, cond-mat.stat-mech, cs.AI, nlin.CD
**Comments**: 7 pages
**HTML URL**: https://arxiv.org/html/2607.22047v1

## Abstract

We show how large-deviation statistics allows one to obtain reliable estimates of the multiplicity of stable fixed-points in a model of neural ordinary differential equations previously employed in computational tasks. The result is obtained by developing a suitable perturbative method in the amplitude of the disorder. It turns out that for not-too-large coupling strengths there are no qualitative differences between the symmetric case, when the dynamics is a purely gradient evolution, and the asymmetric case, when limit cycles and chaos can, in principle, arise. The selection of this specific model is dictated by pedagogical reasons, but we are confident that the approach can be extended to other many-degree-of-freedom dynamical models characterized by different classes of random coupling matrices.

## Full Text

Multiplicity of Stable Attractors in Disordered Neural Models

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.22047v1 [cond-mat.dis-nn] 24 Jul 2026

## Multiplicity of Stable Attractors in Disordered Neural ModelsRaffaele Marinoraffaele.marino@butterflydecisions.comButterfly Decisions srl, Via dei Principati 74 - 84122 Salerno, ItalyRoberto Liviroberto.livi@unifi.itUniversity of Florence, Department of Physics and Astronomy, Via G. Sansone 1 - 50019 Sesto Fiorentino (FI), ItalyIstituto dei Sistemi Complessi, CNR, Via Madonna del Piano 10 – 50019 Sesto Fiorentino (FI), ItalyAntonio Politia.politi@abdn.ac.ukIstituto dei Sistemi Complessi, CNR, Via Madonna del Piano 10 – 50019 Sesto Fiorentino (FI), ItalyInstitute of Pure and Applied Mathematics, Department of Physics, University of
Aberdeen, Aberdeen AB24 3UE,
United Kingdom(July 24, 2026)

## Abstract

We show how large-deviation statistics allows one to obtain reliable estimates
of the multiplicity of stable fixed-points in a model of neural ordinary differential equations previously employed in computational tasks.
The result is obtained by developing a suitable perturbative method in the amplitude of the disorder.
It turns out that for not-too-large coupling strengths there are no qualitative differences between the symmetric case, when
the dynamics is a purely gradient evolution, and the asymmetric case, when limit cycles and chaos can, in principle, arise.
The selection of this specific model is dictated by pedagogical reasons, but we are confident that the approach can be extended
to other many-degree-of-freedom dynamical models characterized by different classes of random coupling matrices.Stable Attractors, Disordered Neural Networks, Order-Statistics, Large-Deviation

Introduction-
Models of random neural networks defined in terms of first-order
ordinary differential equations have been recently recognized as
effective candidates for solving various computational problems. For instance, inWainrib and Touboul (2013)a continuous version of the
Sherrington-Kirkpatrick model has been investigated as a testbed of
the relations between topological and dynamical complexity. There, by tuning the varianceσ\sigmaof the i.i.d. Gaussian
entries of the random coupling matrix among the continuous variables
(neurons), one finds a phase transition from a single equilibrium state
to a chaotic one. The main result of that study is that for any finite
numberNNof neurons in the network the model
exhibits an exponentially
large number of equilibrium points.
Following quite different motivations, another class of these models,
known as Coherent Ising Machines (CIM’s), has been studied as
nonconventional architectures for finding approximate solutions of
large-scale combinatorial optimization problems (e.g.Ghimentiet al.(2026); Syed and Berloff (2023); Syedet al.(2026)). In CIM’s the continuous neural variables are subject to a local
double-well potential and they are coupled via a symmetric matrix,
whose random entries are i.i.d. Gaussian variables. Due to its gradient-dynamic structure, CIM’s are typically
employed for identifying global energy minima by making use of an
annealing process, starting from a
single trivial ground state and evolving towards stable fixed points.
Another model, inspired by Recurrent Neural NetworksKimet al.(2019); Rungratsameetaweemanaet al.(2025)and much similar to CIM’s, is the set of neural Ordinary
Differential Equations (nODEs), recently analyzed inMarinoet al.(2024).
It again deals with
continuous neural variables in a double-well local potential.
However, the coupling matrix is non-symmetric, thus allowing
for a chaotic evolution in the limit of large coupling values.
Such a model has been employed in a region of parameters space
containing spontaneous or planted stable fixed-points.
This dynamical system has been found able to perform standard learning
tasks, making use of implicit feed-forward modulesMarinoet al.(2024).
The procedure exploits the presence of
large sets of stable attractors (typically, fixed-points),
employed as targets of a learnable dynamics, where the Euler
numerical integration outlines the recurrent architecture of
deep-learning algorithms. Moreover, it has been shown that
effective training strategies can be applied to enforce the access
to planted attractors, representative of classification patternsGaglianiet al.(2026); Chicchiet al.(2025); Marinoet al.(2025).
All of these models were investigated having in mind specific
computational tasks, but no systematic effort has been devoted
to understanding the underlying dynamical structure, common to this wide class
of models of nODEs.

In this Letter we provide a preliminary account of such aspects,
by focusing our attention on the dynamical and statistical complexity
of the model studied inMarinoet al.(2024).
More precisely, we describe how the exponentially large
number,2N2^{N}(NNbeing the system size), of stable fixed points
present for zero coupling,g=0g=0,
decreases, whenggis switched on. An
exponentially large number of stable fixed-points survive, at
least up to some finite value ofg∼𝒪​(1)g\sim{\mathcal{O}}(1).
In this range ofggvalues we construct
a large-deviation functional, by exploiting the extreme-value
statistics, associated with the fixed-points depletion mechanism.
All of this is achieved thanks to a perturbative criterion.
To our knowledge, this is a fully novel strategy, which discloses yet unexplored
perspectives in relating many-degree-of-freedom dynamical systems with the
statistics of disordered models, such as spin-glasses.
Final remarks about the dynamics in the large coupling limit envisage future
studies about the dynamical phases of the model, characterized by the presence
of stable limit cycles and chaotic attractors.

The model- We study a set ofNNparticles/neuronsxix_{i}, which satisfy the
following dynamical equationsd​xid​t=−xi​(xi2−1)+gN​∑j=1NAi​j​xj.\frac{dx_{i}}{dt}=-x_{i}(x_{i}^{2}-1)+\frac{g}{\sqrt{N}}\,\sum_{j=1}^{N}\,A_{ij}x_{j}\,.(1)

Each particle is subject to a local double-well potential, whose minima are located at±1\pm 1and separated by
a maximum in0, namelyV​(xi)=14​(xi2−1)2V(x_{i})=\frac{1}{4}(x_{i}^{2}-1)^{2}.
Additionally, the particles mutually interact via anN×NN\times Nrandom matrix𝐀\mathbf{A}, whileggdenotes the coupling strength.
The entriesAi​jA_{ij}follow a standard Gaussian distribution𝒩​(0,1)\mathcal{N}(0,1), so that𝐆=1N​𝐀\mathbf{G}=\frac{1}{\sqrt{N}}\,\mathbf{A}is an element of thereal Ginibre ensemble.
Given the symmetry of the nODEs, dynamics (1) is invariant under the change of sign, i.e.{xi}→{−xi}\{x_{i}\}\rightarrow\{-x_{i}\}.

Forg=0g=0the dynamics reduces to a Cartesian product of overdamped processes.
Given a generic initial condition, eachxix_{i}moves to its closest minimum and
the overall dynamical system collapses onto one of the2N2^{N}stable fixed
points (SFPs),{x→∗(k)​(0)}\{\vec{x}^{*(k)}(0)\}with1≤k≤2N1\leq k\leq 2^{N}, corresponding to all sequences of±1\pm 1.
As soon as the couplingggis switched on, mutual interactions arise
and it is natural to expect deviations of the coordinates
of the SFPs from the initial±1\pm 1values.

Results-
To build intuition on the qualitative organization of the dynamics, we first
analyze the system for small sizesNN. In this setting, the attractor
landscape can be examined systematically as a function of the coupling
parametergg.
Since we expect the number of SFPs to depend on the realization of the matrix,
the data reported in Fig.1are obtained by averaging
over different matrices.Figure 1:Fraction ofPN​(g)P_{N}(g)of SFPs as a function ofggfor several sizes.
Solid curves are simulation estimates averaged over different matrices (1010forN≤20N\leq 20,22forN=25N=25); shaded bands indicate the uncertainty on the mean (error bar on the average).
Dashed curves are the perturbative predictions obtained by integrating the minima density.

There we report the average fractionPN​(g)P_{N}(g)of
SFPs as a function ofgg, for several values ofNN.
For smallgg, the curves remain close to11suggesting that
the number of SFPs is constant.
Upon increasinggg, a significant drop (notice the logarithmic vertical
scale) is observed, and the decrease becomes progressively steeper asNNgrows.
Beyond this drop, there are much fewer SFPs, and forg>1g>1limit cycles as well as
chaotic attractors may appear (data not reported).
So long as SFPs persist, we have observed that they retain the samesign code: namely, the vectors→(k)​(g)=sign​(x→∗(k)​(g))∈{±1}N\vec{s}^{(k)}(g)\;=\;\mathrm{sign}\!\big(\vec{x}^{*(k)}(g)\big)\in\{\pm 1\}^{N}(2)

coincides with the sign pattern present atg=0g=0.
In this sense, the surviving fixed points can be interpreted asdescendantsof the SFPs atg=0g=0, even though the values of
their components change withgg.Figure 2:For smallgg, the stable fixed point (blue, lower branch) is a descendant of theg=0g=0sign pattern withxi∗(k)≈−1x_{i}^{*(k)}\approx-1, and the component drifts continuously asggincreases.
The unstable equilibrium branch (red) approaches the stable one and annihilates with it nearg≃0.4g\simeq 0.4. In green (orange) is presented the stable (unstable) path computed using our perturbative method.

The depletion of SFPs is due to a sequence oftangent(also calledsaddle-nodeorfold) bifurcations.
In fact, forg=0g=0there exists a much larger number of unstable fixed points
(UFPs){y→∗(k)​(0)}\{\vec{y}^{*(k)}(0)\}, usuallysaddlesof different order, corresponding to
the(3N−2N)(3^{N}-2^{N})length-NNsequences of 0s and±1\pm 1s,
containing at least one 0. For each SFP there existNNneighbouring UFP’s,
obtained by setting one of its components equal to 0.
Analogously to the SFPs, saddles can be continued analytically starting fromg=0g=0.
Upon increasinggg, it may happen that one SFPx→∗(k)​(g)\vec{x}^{*(k)}(g)approaches one of the neighbouring saddlesy→∗(l)​(g)\vec{y}^{*(l)}(g)and eventually
the two points mutually annihilate for some SFP-dependent critical valuegcg_{c}.
This scenario is clearly illustrated in Fig.2,
where one component of an SFP is reported as a function ofgg. The blue line
corresponds to the SFP; beyondgc≈0.4g_{c}\approx 0.4an initial condition in the
vicinity of the no-longer existing SFP converges towards another SFP, which
inherits the basin of attraction of the disappeared SFP.
The disappearance of the SFP could be equally monitored by following any
component of the SFP, since the bifurcation is a general phenomenon, which
implies that all components of the two colliding fixed points simultaneously
collapse with one another.
We conjecture that the bifurcation is driven by a single component, the
most sensitive to the coupling.

The bifurcation mechanism is well captured by a perturbative approach.
Given an SFP atg=0g=0with componentsxj∗​(0)∈{±1}Nx^{*}_{j}(0)\in\{\pm 1\}^{N}, we introduce the induced field
(see Eq.(2) )Si=1N​∑j=1NAi​j​sj(k)S_{i}\;=\;\frac{1}{\sqrt{N}}\sum_{j=1}^{N}A_{ij}\,s^{(k)}_{j},
and thereby approximate the dynamics of theii-th component asx˙i=xi​(1−xi2)+g​Si\dot{x}_{i}=x_{i}(1-x_{i}^{2})+g\,S_{i}.
In this approximation, the evolution still factorizes into the
independent relaxation of the various components within quartic potentials.
For a givengg, an SFP exists so long as its components correspond to a local
minimum.
Since a positive (negative)SiS_{i}tends to destabilize a negative (positive)si(k)s^{(k)}_{i},
it is convenient to introduceui=Si​si(k)u_{i}=S_{i}s^{(k)}_{i}(for the sake of simplicity we drop the indexkk).
Let us now denote withiithe component of the SFP characterized by
the most negativeuiu_{i}and beuuits value.
Givenuu, it is readily seen that the critical value where such a minimum
disappears isgc=−233/2​u,g_{c}\;=\;-\frac{2}{3^{3/2}\,u},(3)

The accuracy of this approach can be appreciated in Fig.2,
where thejj-th component (thereini=1i=1) of an SFP determined via the perturbative
approach (see the green line) can be compared with the actual exact solution. The two
curves are very close to one another up to the critical point, in spite ofgcg_{c}being not too small.
The advantage of this approximate approach is that one can infer the range of existence
of the various SFPs directly from the knowledge of the matrixAA, without the need of
performing simulations for different coupling strengths. In fact, if we denote withρN​(u)\rho_{N}(u)the normalized empirical density ofuuvalues
(averaged over disorder realizations), we can express the fractionPN​(g)P_{N}(g)of SFPs for a given value ofgg, asPN​(g)=∫uc​(g)+∞ρN​(u)​𝑑uP_{N}(g)=\int_{u_{c}(g)}^{+\infty}\rho_{N}(u)\,duwhereuc​(g)=−2/(33/2​g)u_{c}(g)=-2/(3^{3/2}g)is obtained by inverting Eq. (3).Figure 3:Main panel: the symbols denote numerical estimates ofρN​(u)\rho_{N}(u)forN=20N=20. Data have been obtained by averaging over
1000 realizations of the matrix𝐀\mathbf{A}. Full circles, crosses, and squares correspond to the Ginibre ensemble, a
uniform distribution of entries, and to the symmetric case, respectively. The solid curves identify the corresponding
theoretical predictions.
Inset: the triangles correspond toh​(u)h(u)estimated asln⁡ρN/N+ln⁡2\ln\rho_{N}/N+\ln 2for the Ginibre ensemble.
The black and red solid curves correspond to the theoretical predictions for asymmetric and symmetric matrices, respectively.

The resulting fractionsPNP_{N}correspond to the dashed line in Fig.1:
they agree pretty well with the direct numerical data over several decades, confirming the
validity of the perturbative scheme.

SinceρN​(u)\rho_{N}(u)contains the relevant information
to characterize the stability of the various SFPs, we now focus on its structure.
The numerical estimates forN=20N=20are reported in Fig.3(see full circles).
Notice that positiveuuvalues are irrelevant in the context of the stability analysis,
since they correspond to SFPs which become more, rather than less, stable,
under the action of the mutual coupling. Moreover, given the inverse proportionality betweenuuandgg, the very negativeuuvalues identify
the most fragile SFPs: those which disappear for very small coupling strengths.

Given the matrix𝐀\bf A,uuis the minimum value within
a set ofNNvariablesSiS_{i}, each one obtained by summingNNindependent elements,
multiplied byde factorandom independent signs
(we sum over all SFPs and hence all sign patterns).
Therefore, we can invoke order-statistics identities for generic distributions
(seeI.1).
In particular, by denoting withφ\varphi, the probability density function (PDF) of theSiS_{i}elements and withΦ\Phithe corresponding cumulative distribution function (CDF),
it is knownRoss (2020)thatρN​(u)=N​φ​(u)​(1−Φ​(u))N−1.\rho_{N}(u)=N\,\varphi(u)\,\big(1-\Phi(u)\big)^{N-1}.(4)

In the present case,ϕ​(u)\phi(u)is the unit-variance Gaussian.
There is only a doubt on the validity of general theorems. Since the minimum is
taken after multiplying the variablesSiS_{i}by the pattern of signs employed in the
definition ofSiS_{i}itself, we cannot exclude subtle correlations sneak in.
Hence, we have directly tested the validity of Eq. (4).
The comparison can be appreciated in Fig.3: the
theoretical prediction is indistinguishable from the
direct numerical results. The same is true for other values ofNN(data not shown).

It is natural to invoke the large-deviation theory and conjecture thatln⁡ρN\ln\rho_{N}is
asymptotically proportional toNN; in mathematical terms,ψ​(u)=limN→∞(ln⁡ρN​(u))/N\psi(u)=\lim_{N\to\infty}(\ln\rho_{N}(u))/N.
This is indeed correct, and from Eq. (4), we see thatψ​(u)=ln⁡(1−Φ​(u))\psi(u)=\ln(1-\Phi(u)).
In fact, it is more instructive to refer to the actual (average) numberEN​(u)=2N​PN​(u)E_{N}(u)=2^{N}P_{N}(u)of expected SFPs, rather than to their fraction.
Their growth rate ish​(u)=ln⁡2+ψ​(u)=ln⁡(2​(1−Φ​(u)))h(u)=\ln 2+\psi(u)=\ln(2(1-\Phi(u))). The resulting distribution
is shown in the inset of Fig.3(see the black solid curve).
The triangles are obtained directly from(ln⁡ρN)/N(\ln\rho_{N})/N(see the triangles): the initial
rising part is a clearcut finite-size effect.Figure 4:Comparison between the perturbative theoretical predictionh​(g)=ln⁡2+ln⁡[1−Φ​(uc​(g))]h(g)=\ln 2+\ln[1-\Phi(u_{c}(g))](black solid line) and the rate extracted from direct numerical simulations in the large-NNlimit (red squares with error bars).

Finally, we have plotted the multiplicity indexhhas a function of the coupling
strengthgg(via Eq. (3)) to allow for a comparison with direct
numerical simulations. The solid curve in Fig.4corresponds to the
perturbative estimate ofh​(g)h(g), which is
strictly larger than0for arbitrarily largeggvalues.
This is a consequence of the implicit assumption that the only way SFPs disappear
is via tangent bifurcations, which let anyhowNNSFPs survive.
This is not true, as we have spotted various homoclinic and heteroclinic bifurcations,
which lead to either the disappearance or the destabilization of some SFPs (eventually to
the onset of limit cycles and chaos).
Whether or not these additional mechanisms can lead to a vanishing or even possibly negativeh​(g)h(g)for a finite coupling strength is hard to say.
Direct numerical estimates ofh​(g)h(g), obtained via a fit in the rangeN∈[10,25]N\in[10,25], are in fact consistently
smaller than the theoretical prediction (see the red squares) and the difference becomes substantial forgglarger than 0.5. However, it is appropriate to notice that numerical data are unavoidably
affected by finite-size corrections, quite difficult to quantify.

Different ensembles-
If the matrix entries do not follow a Gaussian distribution, the central-limit
theorem anyhow implies that, in the largeNNlimit,uushould still be distributed in a
Gaussian way, though with likely deviations in the tails.
The relevance of such deviations, can be appreciated in Fig.3(see the blue
crosses), where we report data obtained by assuming a uniform distribution
in the interval[−3,3][-\sqrt{3},\sqrt{3}](still unit variance) andN=20N=20.
Appreciable differences can be seen only foruusmaller than−4-4(i.e.g<0.1g<0.1).

Symmetric matrices represent an important class of models,
characterized by a strictly gradient dynamics, which implies
that the evolution can only converge onto an SFP.
Since the symmetryAi​j=Aj​iA_{ij}=A_{ji}introduces strong correlations among the matrix entries,
we do not expect our theory to reproduce exactly the multiplicity of SFPs.
This is confirmed by the refined perturbative arguments developed inI.2.
However, as shown in Fig.3), the numerical data obtained forN=20N=20(see the red squares) do not differ significantly from those for the Ginibre ensemble.

However, an important qualitative discrepancy can be appreciated in the inset, where
one sees that the exponential growth rateh​(u)h(u)remains strictly finite foru→0u\to 0(i.e.g→∞g\to\infty). Since in the large-gglimit, there is no guarantee that the perturbative approach
provides sufficiently accurate results, we have performed direct simulations of
the full model for increasingNNandg=5g=5. The data reported at the end ofI.2reveal a clear exponential growth, while no evidence can be found in the asymmetric case,
where periodic cycles and chaotic attractorseata large fraction of the phase space.

Conclusions and perspectives- In this Letter we have focused our attention on the survival mechanism of stable fixed points in model (1), showing that a suitable perturbative approach allows for reliable estimates,
making use of large-deviation theory.
We have also shown that such a perturbative approach is effective for different classes of random
coupling matrices, including symmetric ones. Preliminary results (to appear in a forthcoming
publication) indicate that the perturbative method is effective also when the random coupling matrix
contains planted attractors or has been passed through a training procedure for solving specific
computational tasks. In these cases, the matrix entries cannot be assumed anymore to be i.i.d.
variables and the standard order-statistics (seeI.1) does not apply.
In fact, the probability distributionsϕ​(x)\phi(x)obtained from ensembles of the above mentioned
matrices typically acquire long-tails, testifying at their intrinsic non-Gaussian nature
and to the presence of correlations among the matrix elements.
However, we can argue that the perturbative method still applies tosum of variablesand this is why it works pretty well, although providing less accurate estimates of the survival
probability of SFP’s.
In the limit of large coupling strengths, preliminary studies show the appearance of limit cycles and
even chaotic attractors (see alsoI.3).
Their relation with the survival of SFPs and with the presence of unstable
fixed points is quite an intricate problem. In order to tackle it successfully, statistical and
dynamical concepts and tools have to be suitably combined. For instance, in a more elaborated model
than (1) it has been found that in the ferromagnetic and paramagnetic chaotic phases there
is no direct correspondence between the presence of an exponentially large number of
unstable fixed points and the attractor manifold of these phasesFournieret al.(2026).

## References
- L. Chicchi, D. Fanelli, D. Febbe, L. Buffoni, F. Di Patti, L. Giambagli, and R. Marino (2025)Deterministic versus stochastic dynamical classifiers: opposing random adversarial attacks with noise.6(3),pp. 035054.External Links:Document,LinkCited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- S. J. Fournier, A. Pacco, V. Ros, and P. Urbani (2026)Nonreciprocal interactions and high-dimensional chaos: comparing dynamics and statistics of equilibria in a solvable class of models.113,pp. 044139.External Links:Document,LinkCited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- S. Gagliani, F. Giuseppe Pacifico, L. Chicchi, D. Fanelli, D. Febbe, L. Buffoni, and R. Marino (2026)Train stochastic non linear coupled odes to classify and generate.7(2),pp. 025020.External Links:Document,LinkCited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- F. Ghimenti, A. Sriram, A. Yamamura, H. Mabuchi, and S. Ganguli (2026)Geometry and dynamics of annealed optimization in the coherent ising machine with hidden and planted solutions.Phys. Rev. E113,pp. 054123.External Links:Document,LinkCited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- R. Kim, Y. Li, and T. J. Sejnowski (2019)Simple framework for constructing functional spiking recurrent neural networks.Proceedings of the National Academy of Sciences116(45),pp. 22811–22820.External Links:Document,Link,https://www.pnas.org/doi/pdf/10.1073/pnas.1905926116Cited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- R. Marino, L. Buffoni, L. Chicchi, L. Giambagli, and D. Fanelli (2024)Stable attractors for neural networks classification via ordinary differential equations (sa-node).Machine Learning: Science and TechnologyMachine Learning: Science and TechnologyPhys. Rev. EMachine Learning: Science and TechnologyNeural Computation5(3),pp. 035087.External Links:Document,LinkCited by:Multiplicity of Stable Attractors in Disordered Neural Models,Multiplicity of Stable Attractors in Disordered Neural Models.
- R. Marino, L. Buffoni, L. Chicchi, F. D. Patti, D. Febbe, L. Giambagli, and D. Fanelli (2025)Learning in wilson-cowan model for metapopulation.37(4),pp. 701–741.External Links:ISSN 0899-7667,Document,Link,https://direct.mit.edu/neco/article-pdf/37/4/701/2506385/neco_a_01744.pdfCited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- S. M. Ross (2020)A first course in probability.10th edition,Pearson Benelux.External Links:ISBN 978-1292269207Cited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- N. Rungratsameetaweemana, R. Kim, T. Chotibut, and T. J. Sejnowski (2025)Random noise promotes slow heterogeneous synaptic dynamics important for robust working memory computation.Proceedings of the National Academy of Sciences122(3),pp. e2316745122.External Links:Document,Link,https://www.pnas.org/doi/pdf/10.1073/pnas.2316745122Cited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- M. Syed and N. G. Berloff (2023)Physics-enhanced bifurcation optimisers: all you need is a canonical complex network.IEEE Journal of Selected Topics in Quantum Electronics29(2: Optical Computing),pp. 1–6.External Links:DocumentCited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- M. Syed, R. Z. Wang, and N. G. Berloff (2026)Soft vector spins with dimensional annealing for combinatorial optimization.arXiv preprint arXiv:2604.01003.Cited by:Multiplicity of Stable Attractors in Disordered Neural Models.
- G. Wainrib and J. Touboul (2013)Topological and dynamical complexity of random neural networks.Phys. Rev. Lett.110,pp. 118101.External Links:Document,LinkCited by:Multiplicity of Stable Attractors in Disordered Neural Models.

## IEND MATTER

## I.1Mean and variance of the minima distribution

Here, we summarize analytical formulae about the distribution of the minimau≡min1≤i≤N⁡Siu\equiv\min_{1\leq i\leq N}S_{i}(5)

that enters the perturbative scheme.
The key point is that, for a stable fixed point atg=0g=0, theSiS_{i}are i.i.d. Gaussian variables.
As a consequence,uuis the minimum ofNNi.i.d. standard normal variables, whose distribution,
mean, and variance are controlled by classical order-statistics and extreme-value theory.

## I.1.1From Ginibre to i.i.d. Gaussians

Let𝐆∈ℝN×N\mathbf{G}\in\mathbb{R}^{N\times N}be a real Ginibre matrix withAi​j∼i.i.d.𝒩​(0,1)A_{ij}\stackrel{{\scriptstyle\mathrm{i.i.d.}}}{{\sim}}\mathcal{N}(0,1), i.e.,𝐆=𝐀/N\mathbf{G}=\mathbf{A}/\sqrt{N}.
For a stable fixed point atg=0g=0we sets→∈{±1}N\vec{s}\in\{\pm 1\}^{N}and defineSi≡∑j=1NGi​j​sj=1N​∑j=1NAi​j​sj,u≡min1≤i≤N⁡Si.S_{i}\;\equiv\;\sum_{j=1}^{N}G_{ij}s_{j}\;=\;\frac{1}{\sqrt{N}}\sum_{j=1}^{N}A_{ij}s_{j},\qquad u\;\equiv\;\min_{1\leq i\leq N}S_{i}.(6)

For each fixedii,SiS_{i}is a linear combination of independent Gaussians, hence Gaussian.
Moreover,𝔼​[Si]=0,Var​(Si)=1N​∑j=1NVar​(Ai​j)=δi​i,\mathbb{E}[S_{i}]=0,\qquad\mathrm{Var}(S_{i})=\frac{1}{N}\sum_{j=1}^{N}\mathrm{Var}(A_{ij})=\delta_{ii},(7)

so thatSi∼𝒩​(0,1).S_{i}\sim\mathcal{N}(0,1).(8)

Since different rows of𝐀\mathbf{A}are independent,{Si}i=1N\{S_{i}\}_{i=1}^{N}are independent as well.
Therefore, for any stable fixed points→\vec{s}, the random variableuuis the minimum ofNNi.i.d. standard normal variables.

## I.1.2Exact finite-NNdistribution ofuu

LetΦ\Phiandφ\varphidenote the CDF and PDF of the standard normal.
By independence, the probability of the minimum in a sample ofNNi.i.d. random variables from a standard normal is𝐏​(u<x)=1−(1−Φ​(x))N.\mathbf{P}(u<x)=1-\big(1-\Phi(x)\big)^{N}.(9)

Hence, the CDF and PDF ofuuareFN​(u)\displaystyle F_{N}(u)=𝐏​(u≤x)=1−(1−Φ​(u))N,\displaystyle=\mathbf{P}(u\leq x)=1-\big(1-\Phi(u)\big)^{N},(10)ρN​(u)\displaystyle\rho_{N}(u)=FN′​(u)=N​φ​(x)​(1−Φ​(x))N−1.\displaystyle=F_{N}^{\prime}(u)=N\,\varphi(x)\,\big(1-\Phi(x)\big)^{N-1}.(11)

These are standard order-statistics identities.

## I.2Symmetric Matrices

Here, we sketch the extension to the case of symmetric matrices of the perturbative criterion discussed in the manuscript for asymmetric ones.

Let𝐀\mathbf{A}be anN×NN\times Nsymmetric Gaussian matrix with off-diagonal
entriesAi​j=Aj​i∼𝒩​(0,1)A_{ij}=A_{ji}\sim\mathcal{N}(0,1)(i≠ji\neq j) and diagonal varianced=Var​(Ai​i)d=\text{Var}(A_{ii}). The two conventions of interest ared=0​(Ai​i=0)d=0\ (A_{ii}=0), andd=1​(Ai​i∼𝒩​(0,1))d=1\ (A_{ii}\sim\mathcal{N}(0,1)).

For a stable fixed point atg=0g=0we sets→∈{±1}N\vec{s}\in\{\pm 1\}^{N}.
Let𝐃s=diag​(s1,…,sN)\mathbf{D}_{s}=\text{diag}(s_{1},\dots,s_{N})and𝐀~=𝐃s​𝐀​𝐃s\tilde{\mathbf{A}}=\mathbf{D}_{s}\,\mathbf{A}\,\mathbf{D}_{s}, i.e.A~i​j=si​Ai​j​sj\tilde{A}_{ij}=s_{i}A_{ij}s_{j}. The map𝐀↦𝐀~\mathbf{A}\mapsto\tilde{\mathbf{A}}leaves the
symmetric Gaussian ensemble invariant (gauge invariance), and we haveui=si​Si=1N​∑jA~i​j.u_{i}=s_{i}S_{i}=\frac{1}{\sqrt{N}}\sum_{j}\tilde{A}_{ij}.(12)

Hence, the joint law of{ui}\{u_{i}\}does not depend on the patterns→\vec{s},
which also justifies averaging over all2N2^{N}patterns.

In this case, the only source of correlation is the symmetry constraintA~i​k=A~k​i\tilde{A}_{ik}=\tilde{A}_{ki}. Fori≠ki\neq k, the double sumCov​(ui,uk)=1N​∑j,l𝔼​[A~i​j​A~k​l]\text{Cov}(u_{i},u_{k})=\frac{1}{N}\sum_{j,l}\mathbb{E}[\tilde{A}_{ij}\tilde{A}_{kl}]receives a single nonvanishing contribution (j=k,l=ij=k,\ l=i), so thatCov​(ui,uk)=Ci​j=1N(i≠k),Var​(ui)=Ci​i=(N−1)⋅1+dN=1+d−1N.\begin{split}&\text{Cov}(u_{i},u_{k})=C_{ij}=\frac{1}{N}\quad(i\neq k),\qquad\\
&\text{Var}(u_{i})=C_{ii}=\frac{(N-1)\cdot 1+d}{N}=1+\frac{d-1}{N}.\end{split}(13)

In a more compact form we can writeCi​j=σN2​δi​j+1N,σN2=1+d−2N,C_{ij}=\sigma_{N}^{2}\,\delta_{ij}+\frac{1}{N},\qquad\sigma_{N}^{2}=1+\frac{d-2}{N},(14)

which admits the exact representationui=σN​vi+z/Nu_{i}=\sigma_{N}v_{i}+z/\sqrt{N}withv1,…,vN,zv_{1},\dots,v_{N},zi.i.d.𝒩​(0,1)\mathcal{N}(0,1).
Since the common shiftz/Nz/\sqrt{N}factors out of the minimummN=mini⁡vim_{N}=\min_{i}v_{i}, we haveu=dσN​mN+zN,z⟂mN.u\stackrel{{\scriptstyle d}}{{=}}\sigma_{N}\,m_{N}+\frac{z}{\sqrt{N}},\qquad z\perp m_{N}.(15)

By convolving Eq. (15), we obtain the probability density function
(PDF)ρNsym​(u)=∫−∞+∞𝑑z​N2​π​e−N​z2/2​1σN​ρN​(u−zσN).\rho_{N}^{\mathrm{sym}}(u)=\int_{-\infty}^{+\infty}\!dz\,\sqrt{\frac{N}{2\pi}}\,e^{-Nz^{2}/2}\,\frac{1}{\sigma_{N}}\,\rho_{N}\!\left(\frac{u-z}{\sigma_{N}}\right).\\(16)

The corresponding cumulative density function (CDF) readsP​(u≤x)=1−∫−∞+∞𝑑z​N2​π​e−N​z2/2​(1−Φ​(x−zσN))N.P(u\leq x)=1-\int_{-\infty}^{+\infty}\!dz\,\sqrt{\frac{N}{2\pi}}\,e^{-Nz^{2}/2}\,\left(1-\Phi\!\left(\frac{x-z}{\sigma_{N}}\right)\right)^{N}.(17)

Since the dominant common-mode fluctuation isz=c​Nz=c\sqrt{N}, withc=O​(1)c=O(1),
the diagonal convention drops out and the growth rate of the expected
number of surviving SFPs,h​(u)=limN→∞1N​ln⁡(2N​ρN​(u))h(u)=\lim_{N\to\infty}\frac{1}{N}\ln\!\bigl(2^{N}\rho_{N}(u)\bigr), becomeshsym​(u)=ln⁡2+maxc≥0⁡[ln(1−Φ​(u−c))−c22],h_{\mathrm{sym}}(u)=\ln 2+\max_{c\geq 0}\left[\ln\bigl(1-\Phi(u-c)\bigr.)-\frac{c^{2}}{2}\right],(18)

which coincides in the limitu→−∞u\to-\inftywith the resultln⁡[2​(1−Φ​(u))]\ln[2(1-\Phi(u))]obtained for asymmetric matrices. On the other hand, at variance with the
asymmetric case,hsym​(u)h_{\mathrm{sym}}(u)does not vanish atu=0u=0(see the inset of Fig.3in the manuscript):hsym​(0)=ln⁡2+ln⁡Φ​(c∗)−c∗22=0.1992​…,φ​(c∗)=c∗​Φ​(c∗)⇒c∗≃0.5061.\begin{split}&h_{\mathrm{sym}}(0)=\ln 2+\ln\Phi(c^{*})-\frac{c^{*2}}{2}=0.1992\ldots,\\
&\varphi(c^{*})=c^{*}\Phi(c^{*})\ \Rightarrow\ c^{*}\simeq 0.5061.\end{split}(19)

Note that these analytic formulae hold in the limitN→∞N\to\infty. In order
to appreciate the reliability of the perturbative criterion,
in Fig.5we
report an example of the exponential growth of the number of SFPs of model
(1) with symmetric coupling matrices forg=5g=5, i.e. a coupling value quite far from the perturbative regime.
Taking into account that this numerical estimate of the growth rate,
0.159, is unavoidably affected by hard-to-quantify finite size effects, it
is remarkable its closeness to the theoretical prediction 0.1992.Figure 5:Number of stable fixed points (SFP) as a function of the system sizeNN,
shown on a linear–log scale. Blue markers denote the mean SFP averaged over
disorder realizations, with error bars. The red line is a least-squares fit that confirms an exponential growthSFP∼e0.159​N\mathrm{SFP}\sim e^{0.159N}.

## I.3Large-gglimit

In order to analyze dynamics (1) in the limit of large values ofggit is worth rescalingxi→g​xix_{i}\to\sqrt{g}x_{i}andt→g​tt\to gt, thus
obtainingd​xid​t=−xi​(xi2−1g)+1N​∑j=1NAi​j​xj,i=1,2,⋯,N\frac{dx_{i}}{dt}=-x_{i}(x_{i}^{2}-\frac{1}{g})+\frac{1}{\sqrt{N}}\,\sum_{j=1}^{N}\,A_{ij}x_{j},\,i=1,2,\cdots,N\,(20)

In the limit ofg→+∞g\to+\infty, while inducing also the asymptotic limitt→+∞t\to+\infty, this set of equations simplifies tod​xid​t=−xi3+1N​∑j=1NAi​j​xj,i=1,2,⋯,N\frac{dx_{i}}{dt}=-x_{i}^{3}+\frac{1}{\sqrt{N}}\,\sum_{j=1}^{N}\,A_{ij}x_{j},\,i=1,2,\cdots,N\,(21)

If the coupling matrixAi​jA_{ij}would be diagonal with real eigenvalues{λi}i=1N\{\lambda_{i}\}_{i=1}^{N}these equations represent a set ofNNDuffing
oscillators, with stable fixed point in0ifλi<0\lambda_{i}<0or in±λi\pm\sqrt{\lambda_{i}}ifλi>0\lambda_{i}>0. In the case of asymmetric
coupling matrices we have found numerically that dynamics (21)
yields an asymptotic evolution converging to a low-dimensional chaotic attractor (data not shown).

## 


- 


Major funding support from
