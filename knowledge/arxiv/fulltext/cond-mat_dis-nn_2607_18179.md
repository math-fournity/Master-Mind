# Semi-fractality and localization on a chiral Cayley tree

**arXiv ID**: 2607.18179v1
**Authors**: Carlo Vanoni, Vladimir E. Kravtsov, Boris L. Altshuler
**Published**: 2026-07-20
**Categories**: cond-mat.dis-nn, cond-mat.stat-mech, quant-ph
**Comments**: 12 pages, 13 figures. Comments are welcome!
**HTML URL**: https://arxiv.org/html/2607.18179v1

## Abstract

We study a quantum particle hopping on an infinite Cayley tree with nearest-neighbor hopping amplitudes drawn from a distribution singular as $|t|^{-a}$ near weak links and no on-site disorder. Because the graph is bipartite, the model has chiral symmetry, which strongly affects the statistics of eigenstates at the center of the spectrum. Using population dynamics to solve the cavity equations for the propagator, we analyze the distribution of the local density of states and show that it develops broad power-law tails. These tails imply an unusual form of wave-function statistics, which we call semi-fractality: the eigenstates occupy an extensive fraction of the system, but their higher moments behave as in a multifractal state. We find that the symmetry properties of the local-density-of-states distribution are not fixed only by the symmetry class, but vary continuously with the exponent controlling the power-law hopping distribution. As this exponent is changed, the system crosses from a semi-fractal regime to a localized one. At the transition, the wave functions realize an extreme intermediate form that we call semi-localized, simultaneously extended in their support but localized according to higher moments.

## Full Text

Semi-fractality and localization on a chiral Cayley tree

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.18179v1 [cond-mat.dis-nn] 20 Jul 2026

## Semi-fractality and localization on a chiral Cayley treeCarlo Vanonicvanoni@princeton.eduDepartment of Physics, Princeton University, Princeton, New Jersey, 08544, USAVladimir E. Kravtsovkravtsov@ictp.itThe Abdus Salam ICTP, Strada Costiera 11, 34151, Trieste, ItalyBoris L. AltshulerDepartment of Physics, Columbia University, 538 West 120th Street, New York, New York 10027, USA

## Abstract

We study a quantum particle hopping on an infinite Cayley tree with nearest-neighbor hopping amplitudes drawn from a distribution singular as|t|−a|t|^{-a}near weak links and no on-site disorder. Because the graph is bipartite, the model has chiral symmetry, which strongly affects the statistics of eigenstates at the center of the spectrum. Using population dynamics to solve the cavity equations for the propagator, we analyze the distribution of the local density of states and show that it develops broad power-law tails. These tails imply an unusual form of wave-function statistics, which we call semi-fractality: the eigenstates occupy an extensive fraction of the system, but their higher moments behave as in a multifractal state. We find that the symmetry properties of the local-density-of-states distribution are not fixed only by the symmetry class, but vary continuously with the exponent controlling the power-law hopping distribution. As this exponent is changed, the system crosses from a semi-fractal regime to a localized one. At the transition, the wave functions realize an extreme intermediate form that we call semi-localized, simultaneously extended in their support but localized according to higher moments.

## IIntroduction

The extended and non-ergodic phases in single-particle[9,4,21]and many-body localization[7,13,34,2,38]have generated renewed interest in the condensed matter community[19,39,6,28,40,38]. The old paradigm stating that the only non-ergodic phase is the one in which eigenfunctions are exponentially localized in the real space (for a single-particle localization) or in the Hilbert space (for many-body localization) has changed in light of progress made recently.
In fact, a handful of works demonstrated that the non-ergodic wave functions may be extended, exhibiting mono- or multi-fractal properties[14,19,6,28,37,44]. The corresponding measure that quantifies such properties is the set of fractal dimensionsDq=d​Sq/d​ln⁡ND_{q}=dS_{q}/d\ln N, whereNNis the Hilbert space dimension andSqS_{q}is the Rényi (q≠1q\neq 1) or Shannon-von Neumann (q=1q=1) entropy associated with the wave function coefficients[25,36]. Note thatDqD_{q}is a non-increasing function ofqq.

In terms of the set of fractal dimensionsDqD_{q}, the extended and non-ergodic phases can be classified as follows. Thelocalized phaseis such thatD1=0D_{1}=0, implying thatDq=0D_{q}=0for allq>1q>1. Themono/multi-fractal phaseare such that0<D1<10<D_{1}<1(and thus0<Dq<10<D_{q}<1for allq>1q>1). Theergodic phaseis defined byDq=1D_{q}=1forallq≥0q\geq 0(as happens, e.g., for the Porter-Thomas distribution).
The fractal dimensionD1D_{1}plays a special role in this classification, as it determines the support set of the wave function𝒮∝ND1\mathcal{S}\propto N^{D_{1}}, which is the minimal number of sites that gives the normalization∑r∈𝒮|ψ​(r)|2=1−ϵ\sum_{r\in\mathcal{S}}|\psi(r)|^{2}=1-\epsilonwith any prescribed accuracyϵ≪1\epsilon\ll 1[29]. The fractal dimensions can be used in place of the conductivity[4]to construct the scaling theory of Anderson localization on expander graphs[42]and in high-dimensional lattices[8,11].

However, the above classification does not cover all the possible options. The missing case is what we namesemi-fractal phase, in whichD1=1D_{1}=1butDq<1D_{q}<1, forq>β≥1q>\beta\geq 1.
The support set of wave functions in such a phase is proportional toNN, but other important measures, e.g., the return probability,R​(t)R(t), which is determined by the fractal dimensionD2D_{2}, may show a typical multifractal behaviorRt∝t−D2R_{t}\propto t^{-D_{2}}[16,21,26].

According to its definition,DqD_{q}in the semi-fractal phase must benon-analytic, generally with a jump of the derivatived​Dq/d​qdD_{q}/dqatq=β>1q=\beta>1. Such a jump may only happen when the spectrum of fractal dimensionsf​(α)f(\alpha)has a linear segment with the slopeβ>1\beta>1.
Asβ\betatends to11from above, the fractal dimensionDqD_{q}tends to zero forq>1q>1, remaining equal to11forq≤1q\leq 1. In this limit, the semi-fractal phase reaches its extreme form whenDqD_{q}jumps from11to0atq=1q=1. Such a limiting case was discussed as a certain curiosity in Ref.[29], which did not have model or experimental realizations known at that time.

The situation drastically changed very recently when some works on seemingly different systems have reported what we call here thesemi-fractal phase. One of them is the experiment of Google Quantum AI on the distribution of wavefunction coefficients in the Hilbert space of a set of qubits with XY interaction in a two-dimensional setting[30]. The distribution of the logarithm of wave function amplitudeln⁡|ψ|2\ln|\psi|^{2}measured in this work for moderate and strong disorder demonstrates a power-law behavior that corresponds to a linear segment with the slopeβ>1\beta>1in the spectrum of fractal dimensionsf​(α)f(\alpha). This slope depends on disorder strength and approaches the limiting valueβ=1\beta=1at very strong disorder.
The second model with similar behavior is the tight-binding model on the Erdős-Rényi graph with distributed strengths of random links studied recently within the cavity method[17]. Such a semi-fractal behavior was attributed by the authors to the clusters connected to the remaining part of the graph by a few links that may be very weak.
The third, seemingly unrelated model, is the so-calledβ\beta-ensemble of random matrices whose level statistics is identical to that of classical particles of a logarithmically interacting plasma at an arbitrary temperature[20,18].
Finally, the limitingβ→1\beta\rightarrow 1behavior appears[10]in the random matrix ensemble with power-law deterministic hoppingtn​m∼|n−m|−st_{nm}\sim|n-m|^{-s}for the ground state wave function in the momentum basis at1<s<3/21<s<3/2.

We stress once again that the non-analytic behavior ofDqD_{q}is only possible when there is a linear segment inf​(α)f(\alpha), a feature that until very recently was observed only in the localized phase of the Anderson model on Random Regular Graph (RRG)[19], where the slope wassmallerthan1/21/2. Until the works[17,30,18], all the studies of multifractality[21]resulted in a non-linear (often close to a parabolic)f​(α)f(\alpha)in the non-localized phase. The reason is that in most (if not all) of these studies, the system considered belongs to one of the three Dyson symmetry classes.

In this work, we present evidence that the chiral symmetry (explicit or hidden, exact or approximate) is responsible for the semi-fractal phase observed in Refs.[17,30]. To support this claim, we consider a system that explicitly obeys the chiral symmetry, namely, the bulk of an infinite Cayley tree with only link disorder and zero on-site disorder at zero energy. It is well-known that such a system is best studied by the cavity method (population dynamics numerics)[3,31,35,12]or by exact diagonalization considering the corresponding Anderson model on RRG with only link disorder at the observation energyE=0E=0.

Our main finding is that in both systems (infinite Cayley tree and finite RRG) the distributionP​(ρ)P(\rho)of the local density of states (LDoS)ρ​(E;r)=∑n|ψn​(r)|2​δ​(E−En)\rho(E;r)=\sum_{n}|\psi_{n}(r)|^{2}\,\delta(E-E_{n})behaves as a power-law both at small and largeρ\rho, with different exponents. Although the system we study belongs to the chiral class BDI[5,43], we believe that such power laws whose exponents are connected by the Mirlin-Fyodorov symmetry[32]are tied to the chiral symmetry. We checked that the departure fromE=0E=0that breaks the chiral symmetry spoils the power-laws and invalidates all the principal results presented below. We show that the presence of the power-law regions inP​(ρ)P(\rho)leads to the linear segment inf​(α)f(\alpha)and thus to a non-analytic behavior of fractal dimensionsDqD_{q}and to the semi-fractal phase in a certain region of parameters of the link disorder distribution. As the parameteraathat controls the abundance of weak links increases, a transition to a localized phase happens. At the transition pointa=aca=a_{c}, the slope off​(α)f(\alpha)takes the critical valueβ=1\beta=1and a jump inDqD_{q}from 1 to 0 happens atq=1q=1. This peculiarhalf-ergodic, half-localized phaseis an extreme form of semi-fractality, first anticipated in[29].
Finally, exact diagonalization reveals a complementary eigenstate-level signature of semi-fractality. When the site probabilities of an eigenstate are ordered by magnitude, their disorder-averaged profile displays a broad rank-dependent power law. This provides a possible microscopic interpretation of semi-fractality as arising from a hierarchy of eigenstate weights.

The paper is organized as follows. In Sec.II, we introduce the chiral Cayley-tree model and derive the relation between finite-broadening moments of the local density of states and finite-size moments of wave-function amplitudes. In Sec.IIIwe use the power-law form of the LDoS distribution to obtain the corresponding multifractal spectrum and to distinguish the semi-fractal regime from the localized one. In Sec.IV, we present the population-dynamics solution of the cavity equations and extract the exponents controlling the LDoS tails. In Sec.V, we compare these predictions with exact-diagonalization results on finite random regular graphs. We also examine the rank-ordered eigenstate probabilities and present finite-size evidence for a power-law hierarchy of weights that leads to semi-fractality. We conclude in Sec.VIwith a summary of the main results and open questions.

## IIModel and formalism for the chiral orthogonal symmetry class

As anticipated in the Introduction, we consider the problem of a quantum particle hopping on a Cayley tree with branching numberk=2k=2, described by the HamiltonianH=∑⟨i,j⟩ti​j(ci†cj+h.c.)H=\sum_{\langle i,j\rangle}t_{ij}(c^{\dagger}_{i}c_{j}+\mathrm{h.c.})(1)

whereci†c^{\dagger}_{i}andcic_{i}are the creation and annihilation operators at siteii, the sum runs over nearest neighbor sites on the tree (denoted by⟨⋅,⋅⟩\langle\cdot,\cdot\rangle), and the random numbersti​j=tj​it_{ij}=t_{ji}are distributed according to the distributionp​(t)=1Γ​(1−a2)​e−t2|t|a,(a<1),p(t)=\frac{1}{\Gamma\left(\frac{1-a}{2}\right)}\frac{e^{-t^{2}}}{|t|^{a}},\quad(a<1),(2)

which reduces to a Gaussian fora=0a=0. In the infinite system-size limit, the Cayley tree is a bipartite graph, meaning that it can be divided into two sublattices such that a site from one sublattice is linked only to sites belonging to the other. The bipartite nature of the graph endows the problem with a chiral symmetry preserving both the time-reversal and particle-hole symmetries with𝒯2=+1{\cal T}^{2}=+1and𝒫2=+1{\cal P}^{2}=+1, respectively. This means, in particular, that each eigenstate with the eigenvalueEnE_{n}and eigenfunctionψEn​(r)\psi_{E_{n}}(r)has a counterpart with the eigenvalue−En-E_{n}and eigenfunction having opposite sign in one of the two sublattices (therefore,|ψEn​(r)|2=|ψ−En​(r)|2|\psi_{E_{n}}(r)|^{2}=|\psi_{-E_{n}}(r)|^{2}).

Consequently, the single-point retarded/advanced Green’s functionsGR/A​(E;r,r;η)≡GR/AG^{R/A}(E;r,r;\eta)\equiv G^{R/A}atE=0E=0obey the symmetry:GR/A\displaystyle G^{R/A}=∑n|ψn|2−En±i​η=∑n|ψn|2+En±i​η\displaystyle=\sum_{n}\frac{|\psi_{n}|^{2}}{-E_{n}\pm i\eta}=\sum_{n}\frac{|\psi_{n}|^{2}}{+E_{n}\pm i\eta}(3)=∓i​η​∑n|ψn|2En2+η2,\displaystyle=\mp i\eta\sum_{n}\frac{|\psi_{n}|^{2}}{E_{n}^{2}+\eta^{2}},(4)

i.e., the Green’s functionsGR/AG^{R/A}(GR=GA∗G^{R}={G^{A}}^{*}) are pure imaginary.

In the remainder of this section, we derive the relation between the moments of the LDoS at finite broadeningη\etain the infinite system and the moments of wave-function amplitudes in a finite Hermitian system. This relation provides the bridge from the LDoS distributionP​(ρ)P(\rho)to the multifractal spectrum of eigenfunctions: once the tail exponents ofP​(ρ)P(\rho)determine the scaling of⟨ρq⟩\langle\rho^{q}\rangle, Eq. (13) gives the corresponding scaling ofIq=N​⟨|ψ|2​q⟩I_{q}=N\langle|\psi|^{2q}\rangle, from whichDqD_{q}andf​(α)f(\alpha)follow.
We start by consideringGR=−i​π​ρG^{R}=-i\pi\rho, whereρ\rhois the local density of states (LDoS). We have atE=0E=0:ρq\displaystyle\rho^{q}=(ηπ)q​(∑n|ψn|2En2+η2)q\displaystyle=\left(\frac{\eta}{\pi}\right)^{q}\,\left(\sum_{n}\frac{|\psi_{n}|^{2}}{E_{n}^{2}+\eta^{2}}\right)^{q}=(ηπ)q​∑n1​…​nq∏i=1q|ψni|2​q(Eni2+η2)q\displaystyle=\left(\frac{\eta}{\pi}\right)^{q}\,\sum_{n_{1}...n_{q}}\prod_{i=1}^{q}\frac{|\psi_{n_{i}}|^{2q}}{(E_{n_{i}}^{2}+\eta^{2})^{q}}≈(ηπ)q​∑n|ψn|2​q(En2+η2)q.\displaystyle\approx\left(\frac{\eta}{\pi}\right)^{q}\,\sum_{n}\frac{|\psi_{n}|^{2q}}{(E_{n}^{2}+\eta^{2})^{q}}.(5)

For integerqqin the r.h.s., the most divergent terms with allnin_{i}(i=1,2,…​qi=1,2,...q) equal to each other make the main contribution in the limitη→0\eta\to 0. We now introduce:ρq​(ξ)=N−1​∑n|ψ|2​q​δ​(ξ−En).\rho_{q}(\xi)=N^{-1}\sum_{n}|\psi|^{2q}\,\delta(\xi-E_{n}).(6)

Then the summation in Eq. (II) can be replaced by integration. After averaging over disorder, we obtain:⟨ρq⟩=N​(ηπ)q​∫−∞+∞𝑑ξ​⟨ρq​(ξ)⟩(ξ2+η2)q.\langle\rho^{q}\rangle=N\left(\frac{\eta}{\pi}\right)^{q}\int_{-\infty}^{+\infty}d\xi\,\frac{\langle\rho_{q}(\xi)\rangle}{(\xi^{2}+\eta^{2})^{q}}.(7)

Theδ\delta-function in Eq. (6) should be regularized, e.g.:δ(x)→δη(x)={1/(2​η),|x|<η0,otherwise\delta(x)\rightarrow\delta_{\eta}(x)=\left\{\begin{matrix}1/(2\eta),&|x|<\eta\cr 0,&{\rm otherwise}\end{matrix}\right.(8)

To make contact with the exact diagonalization calculations, in which only the level closest toE=0E=0is taken into account, we have to chooseη=ηc\eta=\eta_{c}such that inside the energy box of the widthηc\eta_{c}there areone or a fewlevels. The condition for that is:ηc​N​ρ¯​(ηc)∼1,\eta_{c}\,N\bar{\rho}(\eta_{c})\sim 1,(9)

whereρ¯​(E)\bar{\rho}(E)is the mean DoS:ρ¯​(η)=⟨N−1​∑nδη​(En)⟩\bar{\rho}(\eta)=\left\langle N^{-1}\sum_{n}\delta_{\eta}(E_{n})\right\rangle(10)

Assuming that the mean DoS is of the same order of magnitude as the mean LDoS111The mean LDoS is equal to the mean DoS exactly if the eigenfunction amplitude and the DoS fluctuations are statistically independent. This happens both for the fully delocalized and for the localized states and is supposed to be valid by the order of magnitude in all the phases., we obtain a condition forη\etathat should be found self-consistently:ηc​N​⟨ρ⟩|η=ηc∼1.\eta_{c}\,N\,\langle\rho\rangle|_{\eta=\eta_{c}}\sim 1.(11)

The solution of the above condition gives the value ofη=ηc\eta=\eta_{c}that has to be substituted into theη\eta-dependent moments of the LDoS obtained from population dynamics to convert the distribution of the LDoS atN=∞N=\inftyand a finiteη\etainto the distribution ofψ2\psi^{2}atη=0\eta=0and a finiteNN.

Under the condition in Eq. (11), Eq. (6) provides the following relationship between the moment of LDoS and that of the wave function amplitude:⟨ρq⟩=(N​ηc)−1​⟨|ψ|2​q⟩.\langle\rho_{q}\rangle=(N\eta_{c})^{-1}\,\langle|\psi|^{2q}\rangle.(12)

Finally, from Eq. (7) we obtain the desired relation:Iq≡N​⟨|ψ|2​q⟩∼(N​ηc)​ηcq−1​⟨ρq⟩|η=ηc,I_{q}\equiv N\langle|\psi|^{2q}\rangle\sim(N\eta_{c})\,\eta_{c}^{q-1}\,\langle\rho^{q}\rangle|_{\eta=\eta_{c}},(13)

whereηc\eta_{c}is found from Eq. (11).

## IIIDistribution of the LDoS and eigenfunction statistics

Using the population dynamics results in the chiral case presented in Sec.IV, we can express the distribution of LDoS atE=0E=0as a piecewise power-law function (see Fig.1for a representation):P​(ρ)∼{ρ1+β−γ,η≪ρ≪1ρ−(1+β),η−1≫ρ≫1.P(\rho)\sim\begin{cases}\rho^{1+\beta-\gamma},&\eta\ll\rho\ll 1\cr\rho^{-(1+\beta)},&\eta^{-1}\gg\rho\gg 1.\end{cases}(14)

It is easy to check that atβ>0\beta>0andβ>γ−2\beta>\gamma-2the normalization factorc−1=∫ηη−1P​(ρ)​𝑑ρ∼1c^{-1}=\int_{\eta}^{\eta^{-1}}P(\rho)\,d\rho\sim 1inP​(ρ)P(\rho)of the form Eq. (14) is independent ofη→+0\eta\rightarrow+0.Figure 1:Schematic representation of the distribution of the LDoS, based on the population dynamics result (see Sec.IV). The small-ρ\rhoregime is described by a power-lawρβ+1−γ\rho^{\beta+1-\gamma}, while the large-ρ\rhoregime is described byρ−(β+1)\rho^{-(\beta+1)}.

The parameterβ\betacontrols the tail of the distribution for largeρ\rho, whileγ\gammacontrols the symmetry of the distribution:P​(1/ρ)=ργ​P​(ρ).P(1/\rho)=\rho^{\gamma}\,P(\rho).(15)

For all three Dyson symmetry classes,γ=3\gamma=3. It also takes a universal (independent of the further details of the system) value for the class CI (γ=4\gamma=4) and the class C (γ=5\gamma=5). However, for thechiral symmetry classesstudied here, the parameterγ\gammamay depend on the details of the system and can be even a continuous function of the parameter characterizing the strength of disorder[24]. Indeed, population dynamics shows that bothγ=γ​(a)\gamma=\gamma(a)andβ=β​(a)\beta=\beta(a)depend onaain our model. However, the relationsγ−2<β,β>0\gamma-2<\beta,\qquad\beta>0(16)

remain true for all values ofa<1a<1. ForE≠0E\neq 0, and in particular when the diagonal contributionE​(N/2)E(N/2)is compatible with the off-diagonal weight given by the hopping, the chiral symmetry is completely absent, and the Mirlin-Fyodorov symmetry withγ=3\gamma=3is restored (see Fig.2). For intermediate energies, such that the diagonal norm is smaller than the off-diagonal, there is a crossover regime, in which the LDoS can display power-law tails despite the chiral symmetry being broken. The energy range of this intermediate crossover increases asaadecreases.Figure 2:Top panel: comparison betweenP​(ρ)P(\rho)(black) andργ​P​(1/ρ)\rho^{\gamma}P(1/\rho)(red) fora=0a=0andE=0E=0. The collapse of the two curves signals the validity of Eq. (15) forγ​(a=0)=2.44\gamma(a=0)=2.44, a value obtained from fitting the power-law tails of the LDoS distribution.Bottom panel: same comparison fora=0a=0andE=2E=2. Away fromE=0E=0, there is no chiral symmetry and the Dysonγ=3\gamma=3value is restored, with the LDoS distribution not displaying two power-law tails at small and largeρ\rho.

Integratingρq\rho^{q}with the distribution functionP​(ρ)P(\rho), Eq. (14), one obtains[17]⟨ρq⟩∼{η0,q<βηβ−q,q>β\langle\rho^{q}\rangle\sim\left\{\begin{matrix}\eta^{0},&q<\beta\cr\eta^{\beta-q},&q>\beta\end{matrix}\right.(17)

We observe that, forq=1q=1,⟨ρ⟩∼{O​(1),β>1ηβ−1,β<1\langle\rho\rangle\sim\left\{\begin{matrix}O(1),&\beta>1\cr\eta^{\beta-1},&\beta<1\end{matrix}\right.(18)

We see that the casesβ>1\beta>1andβ<1\beta<1are fundamentally different. In the former case, the mean LDoS (and the mean DoS) is finite in the limitη→0\eta\rightarrow 0, while in the latter it is divergent atE=0E=0. Such zero-energy singularities are a familiar feature of chiral random hopping problems and their field-theory descriptions[33]. We will consider these two cases separately.Figure 3:Top panel: Example of a semi-fractalDqD_{q}withβ=1.5\beta=1.5. The solid line corresponds toDqD_{q}with the rare events with large wave function amplitudes (shown by the dashed line in the inset) taken into account, while the dashed line corresponds toDqD_{q}deduced from the typical average of the moments. In the inset, the corresponding spectrum of fractal dimensions is shown, which has a linear segmentf​(α)=β​(α−1)+1f(\alpha)=\beta(\alpha-1)+1with the slopeβ=1.5\beta=1.5forα<1\alpha<1and the reciprocal linear segment with the slopeγ−β−2=−1.4\gamma-\beta-2=-1.4that corresponds to the Mirlin-Fyodorov symmetry withγ=2.1\gamma=2.1.Bottom panel:DqD_{q}forβ<1\beta<1, corresponding to the localized case. The inset shows the correspondingf​(α)f(\alpha).

## III.1Caseβ>1\beta>1.

In this case, Eq. (11) gives a usualηc∼N−1\eta_{c}\sim N^{-1}, and thus from Eq. (13) we obtain:Iq∼{N1−q,0<q<βN1−β,q>β>1.I_{q}\sim\left\{\begin{matrix}N^{1-q},&0<q<\beta\cr N^{1-\beta},&q>\beta>1\end{matrix}\right..(19)

The fractal dimensionDqD_{q}is then given by[17]:Dq=−d​ln⁡Iqd​ln⁡N1q−1={1,q<ββ−1q−1<1,q>β>1.D_{q}=-\frac{d\ln I_{q}}{d\ln N}\frac{1}{q-1}=\left\{\begin{matrix}1,&q<\beta\cr\frac{\beta-1}{q-1}<1,&q>\beta>1\end{matrix}\right..(20)

This is a very peculiar dependence ofqq, as the dimension of the support setD1=1D_{1}=1, but the fractal dimension forq>βq>\beta(e.g., the fractal dimensionD2D_{2}) may be smaller than 1 [see Fig.3]. This phase will be referred to assemi-fractal. A totally abnormal situation happens whenβ→1\beta\rightarrow 1; all the fractal dimensionsDqD_{q}withq>1q>1are equal to zero, whereas all the fractal dimensions forq<1q<1are equal to11. We will call this phase asemi-localized phase.

## III.2Caseβ<1\beta<1.

Now consider the caseβ<1\beta<1. In this case,ηc\eta_{c}should be found self-consistently from Eq. (11). Using⟨ρ⟩∼ηβ−1\langle\rho\rangle\sim\eta^{\beta-1}we obtain:ηc∼N−1β.\eta_{c}\sim N^{-\frac{1}{\beta}}.(21)

Therefore, Eq. (13) gives:Iq=N⟨|ψ|2​q⟩∼{N1−qβ,q<βO​(1),q>βI_{q}=N\langle|\psi|^{2q}\rangle\sim\left\{\begin{matrix}N^{1-\frac{q}{\beta}},&q<\beta\cr O(1),&q>\beta\end{matrix}\right.(22)

This corresponds to the localized state [see Fig.3]:Dq={1−q1−q​1−ββ,q<β<10,q>βD_{q}=\left\{\begin{matrix}1-\frac{q}{1-q}\frac{1-\beta}{\beta},&q<\beta<1\cr 0,&q>\beta\end{matrix}\right.(23)

sinceD1=0D_{1}=0.

## IVPopulation dynamics numericsFigure 4:Distribution function of the LDoSP​(ρ)P(\rho)at different values ofaa.Figure 5:LDoS distribution fora=−1,0,0.5a=-1,\,0,\,0.5(from left to right), with the power-law fits atρ≪1\rho\ll 1andρ≫1\rho\gg 1indicated in blue and red, respectively.

A direct finite-size study at the band center is complicated by the boundary structure of a Cayley tree. For a tree of depthLLand branching numberk=2k=2, the two sublatticesAAandBBcontain different numbers of sites,|NA−NB|=2L\lvert N_{A}-N_{B}\rvert=2^{L}. This imbalance produces at least2L2^{L}eigenstates at exactly zero energy[15]. Since this number is extensive in the total system size, exact diagonalization atE=0E=0is dominated by boundary-induced zero modes and does not provide a faithful probe of the bulk infinite-tree problem.

We therefore employ the cavity method, which works directly in the thermodynamic limit and avoids the boundary-induced sublattice imbalance.
Writingz=E+i​ηz=E+i\eta, the cavity Green’s functions satisfy (the diagonal part entries are all vanishing for the chiral case studied here,ϵi=0\epsilon_{i}=0)Gi→j​(z)=(−z−∑a∈∂i∖jti​a2​Ga→i​(z))−1.G_{i\to j}(z)=\left(-z-\sum_{a\in\partial i\setminus j}t_{ia}^{2}G_{a\to i}(z)\right)^{-1}.(24)

We solve this recursion by population dynamics: the distribution of cavity fields is represented by a large population of complex numbers, which is iteratively updated by drawingkkincoming fields and independent hopping amplitudes. After equilibration, diagonal Green’s functions are reconstructed using the full coordinationk+1k+1,Gi​i​(z)=(−z−∑j∈∂iti​j2​Gj→i​(z))−1.G_{ii}(z)=\left(-z-\sum_{j\in\partial i}t_{ij}^{2}G_{j\to i}(z)\right)^{-1}.(25)

We then sample the LDoS populationρi​(E,η)=Im⁡Gi​i​(E+i​η)/π\rho_{i}(E,\eta)=\operatorname{Im}G_{ii}(E+i\eta)/\piduring the measurement sweeps and construct the corresponding distributionP​(ρ)P(\rho).

For the results presented in this work, we use a population ofn=106n=10^{6}cavity fields. We perform50005000warm-up sweeps, with each sweep
consisting ofnncavity updates according to
Eq. (24). This is followed by80008000measurement sweeps. During each measurement sweep, the cavity population is updated once and80008000diagonal Green’s functions are independently reconstructed according to Eq. (25).
We have verified that our results are robust with respect to changes in the population size, the number of sweeps, and the random seed. We have also checked that the stationary distribution is independent of whether the initial population is purely imaginary or has a nonzero real part.

In Fig.4, we show the results of the population dynamics numerics for the distribution of LDoSP​(ρ)P(\rho). The main feature of the distribution at all values ofaain Eq. (2) is that we have two power-law segments atρ≪1\rho\ll 1and atρ≫1\rho\gg 1. The fit of the right tail ofP​(ρ)P(\rho)to the power-lawP​(ρ)∝ρ−(1+β)P(\rho)\propto\rho^{-(1+\beta)}gives the value of the exponentβ\beta, see Fig.5. As it is shown in Sec.III(Fig.3),β\betais equal to the slope of the linear segment of the spectrum of fractal dimensionsf​(α)f(\alpha). This slope also determines the exponent of the power-law tail in the distribution functionF​(ln⁡(|ψ|2))F(\ln(|\psi|^{2})):F​(ln⁡(|ψ|2))=C​Nf​(α)−1∼1|ψ|2​β,α=−ln⁡(|ψ|2)ln⁡N,F(\ln(|\psi|^{2}))=C\,N^{f(\alpha)-1}\sim\frac{1}{|\psi|^{2\beta}},\;\;\;\;\alpha=\frac{-\ln(|\psi|^{2})}{\ln N},(26)

whereCCis the normalization constant.

The fit to the left tailP​(ρ)∼ρβ+1−γP(\rho)\sim\rho^{\beta+1-\gamma}atρ≪1\rho\ll 1(see Fig.5) gives the exponentγ\gammain the symmetry relation Eq. (15). Bothβ\betaandγ\gammaappear to be functions ofaa, see Fig.6.Figure 6:The fitted values ofβ\beta,γ\gammaandβ−γ+2\beta-\gamma+2vs.aa. The dashed vertical line indicates the value ofaafor whichβ=1\beta=1.

Figure6demonstrates that at all values ofa<1a<1studied we haveβ≥0\beta\geq 0,2≤γ≤32\leq\gamma\leq 3andβ≥γ−2\beta\geq\gamma-2. We remind here once again that in the chiral classes the symmetry parameterγ\gammais not fixed by the symmetry class but may depend on the details of the system[24]. In our case, it depends on the parameteraain the distribution of hopping strengths (see Eq. (2)).

From the data presented in Fig.6one can determinea=aca=a_{c}whereβ=1\beta=1. According to the analytical results of Sec.III, this value ofaacorresponds to the transition from the semi-fractal to the localized phase. For our model, it isac≈0.25a_{c}\approx 0.25, so that the Gaussian distributionp​(t)p(t)of hopping strengths is still in the semi-fractal phase but very close to the transition point. At this point a very unusual set of fractal dimensionsDqD_{q}is realized whenDq=1D_{q}=1forq<1q<1andDq=0D_{q}=0forq>1q>1[29][see Fig.7]. This dependence ofDqD_{q}is an extreme form of semi-fractality: it is half-ergodic and half-localized.Figure 7:DqD_{q}forβ=0.98\beta=0.98(blue) andβ=1.02\beta=1.02(orange) and for the critical state (semi-localized)β=1\beta=1(green, dashed).Figure 8:Most probable value ofρ\rhovs.aa. The vertical dashed line corresponds to the value ofa=aca=a_{c}, where the fit to the tail ofP​(ρ)P(\rho)atρ≫1\rho\gg 1givesβ=1\beta=1.

The transition from the semi-fractal to the localized phase ata=aca=a_{c}predicted above is reflected by a dramatic change in the most probable value ofρ\rho. Figures4,8show that it drops by1010orders of magnitude from the value of order0.10.1to the value∼η∼10−12\sim\eta\sim 10^{-12}just over the interval ofΔ​a≈0.5\Delta a\approx 0.5.

## VComparison between theory, population dynamics, and exact diagonalization numerics.

## V.1P​(ρ)P(\rho)from population dynamics and exact diagonalization

First of all, we compare the distribution of LDoSP​(ρ)P(\rho)computed by matrix inversion for a finite “chiral random regular graph" and that obtained by population dynamics. The “chiral RRG" is constructed as follows. We take two groups ofN/2N/2points each and then connect each point of one group with three points of the other. There is no on-site disorder and the strengths of the links are i.i.d. according to Eq. (2). Such a graph is bipartite by construction, in contrast to the usual RRG with link disorder.
However, further inspection showed that there is a little difference between them in numerics. This implies that long loops do not spoil the chiral (sublattice) symmetry at sizesN=2LN=2^{L},L=4,…,12L=4,\dots,12in consideration. We will therefore use the usual RRG in the numerical results presented below.Figure 9:Comparison of the LDoS distribution functions obtained in population dynamics (red dashed-dotted line) and by the exact diagonalization fora=0a=0and the sizes indicated, withη=N−1=2−L\eta=N^{-1}=2^{-L}.

The result of the comparison in Fig.9shows thatP​(ρ)P(\rho)obtained by the exact diagonalization is quantitatively similar to that of population dynamics, albeit the power laws in the latter are much more accurate.

Note that fora>aca>a_{c}, the coincidence ofP​(ρ)P(\rho)computed by exact diagonalization with that computed in population dynamics depends on the value ofη\eta. The point is that the population dynamics corresponds toN=∞N=\inftyand thus to an infinite number of levels insideη\eta. On the other hand, in the exact diagonalization and in the theory of Sec.IV, only one state with the energyEEclosest toE=0E=0is studied. These are quite different limits in the caseβ<1\beta<1when the mean DoS is singular atE=0E=0.

In Fig.10, we checked that the change of regime occurs at approximatelyη=ηc∼N−1β\eta=\eta_{c}\sim N^{-\frac{1}{\beta}}when less than one level is, on average, in the energy interval ofη\etaaroundE=0E=0. As a result, the value ofβ\betaincreases by approximately0.10.1compared to the results of population dynamics. It is thisincreasedvalue ofβ\betathat should be used in Eq. (23) to findDqD_{q}andf​(α)f(\alpha)forβ<1\beta<1.Figure 10:LDoS distribution obtained for the RRG withN=212N=2^{12}(solid lines) anda=0.7a=0.7and different values ofη\eta, compared with the Cayley tree result (red dash-dotted line). The exponentβ\betadepends onη\etain the exact diagonalization numerics: forη≫N−1/β∼10−13\eta\gg N^{-1/\beta}\sim 10^{-13}, the slope in the power-law tail ofP​(ρ)P(\rho)coincides with that in population dynamics, since in this case there are many levels insideη\eta. However, forη≲10−13\eta\lesssim 10^{-13}, the slope of the tail atρ≫1\rho\gg 1increases by approximately0.10.1, which implies thatβ\betaincreases by the same amount compared to the results of population dynamics.

## V.2Exact diagonalization results for the distribution ofln⁡|ψ|2\ln|\psi|^{2}and their correspondence to theoryFigure 11:Left Panel:f​(α)f(\alpha)fora=−0.5a=-0.5;Central panel: the dependence of initial slope onLLand the1/L1/Lextrapolation. The extrapolated value≈2.13\approx 2.13is very close toβ≈2.07\beta\approx 2.07(filled square) obtained fromP​(ρ)P(\rho)computed in population dynamics;Right panel:1/L1/Lextrapolation of the maximal value off​(α)f(\alpha).Figure 12:Left Panel:f​(α)f(\alpha)fora=0.6a=0.6;Central panel: the dependence of initial slope onLLand the1/L1/Lextrapolation. The extrapolated value≈0.61\approx 0.61is very close to the value ofβ\betaonce it is adjusted to the ED result (see Fig.10)β+0.1≈0.62\beta+0.1\approx 0.62. The population dynamics result is shown as a filled square, while the exact diagonalization result for smallη∼N−1/β\eta\sim N^{-1/\beta}is reported as an empty square;Right panel:1/L1/Lextrapolation of the position of maximal value off​(α)f(\alpha), close to1/β≈1.621/\beta\approx 1.62.

Now we check numerically the correspondence off​(α)f(\alpha)to the theory of Sec.III. We do it by exact diagonalization of the Anderson model on the RRG with i.i.d. link strengths determined by Eq. (2). By collecting statistics of|ψ|2|\psi|^{2}corresponding to the level with the minimal|En||E_{n}|and finding the distribution function ofln⁡|ψ|2\ln|\psi|^{2}, one can infer information about the spectrum of fractal dimensionsf​(α)f(\alpha). The correspondence of this distribution tof​(α)f(\alpha)is given by Eq. (26).

The examples of the distributionsF​(ln⁡|ψ|2)F(\ln|\psi|^{2})and correspondingf​(α)f(\alpha)are shown below. We start by studying the caseβ>1\beta>1.
In the left panel of Fig.11we present the plot off​(α)=1+ln⁡[F​(ln⁡|ψ|2)]/ln⁡Nf(\alpha)=1+\ln[F(\ln|\psi|^{2})]/\ln Nvsα=−ln⁡|ψ|2/ln⁡N\alpha=-\ln|\psi|^{2}/\ln Nwhich in the limitL=ln⁡N/ln⁡2→∞L=\ln N/\ln 2\rightarrow\inftyshould represent the spectrum of fractal dimensionsf​(α)f(\alpha). In this limit, the theory of Sec.IIIpredicts that the slope of the linear segment atα<1\alpha<1should be equal toβ\beta, and the maximum of the plot should be atα=1\alpha=1and should be equal to 1. We verified that all the extrapolations are consistent with the predictions. The central and the right panels of Fig.11show the1/L1/Lextrapolation of data from finite values of1/L1/L(black points) to1/L→01/L\rightarrow 0and the corresponding target following from the theory (black square). Note that the nodes of the wave function heavily influence the part of the plot corresponding toα>1\alpha>1due to fast De Broglie oscillations and reflect the statistics of the nodes rather than the envelope ofψ2\psi^{2}, which (by definition) determines the spectrum of fractal dimensions.
It is only after rectifying the effect of the nodes that this part will be in quantitative correspondence withf​(α)f(\alpha)depicted in the inset of Fig.3.

Now we turn to a more difficult caseβ<1\beta<1, reported in Fig.12. The difficulty in this case is related to the singularity of the mean DoS and LDoS atE=0E=0. As it is demonstrated in Fig.10and the corresponding discussion, to reach a correspondence betweenf​(α)f(\alpha)obtained from exact diagonalization and the theoretical expectation, one should use the value ofβ\betathat is larger than the one obtained from the population dynamics. This value should be obtained from the tail ofP​(ρ)P(\rho)computed by exact diagonalization in the regime when there are few levels in the energy intervalη\etacentered atE=0E=0.

## V.3Power-law distributed eigenstate probabilities

It was shown in Ref.[41]that a deterministic power-law deformation of the Gaussian Unitary Ensemble (GUE) can generate eigenstates with a power-law profile, leading to semi-fractality (referred to as frozen multifractality in Ref.[41]). It is therefore natural to ask whether the semi-fractality found in the LDoS distribution has a direct manifestation in the spatial structure of individual eigenstates. In this section, we present finite-size evidence that the rank-ordered eigenstate probabilities atE=0E=0form a power-law hierarchy. We then show that this hierarchy reproduces the piecewise-linear participation spectrum derived in Sec.III.

We consider the RRG model introduced in the previous section, and for each eigenstate, we order the probabilitieswi=|⟨i|ψ⟩|2w_{i}=|\langle i|\psi\rangle|^{2}(27)

in decreasing magnitude,w(1)≥w(2)≥⋯≥w(N),w_{(1)}\geq w_{(2)}\geq\cdots\geq w_{(N)},(28)

and average the resulting rank-ordered profiles over a few eigenstates nearE=0E=0and over disorder realizations. As shown in Fig.13(top panel), the rank-ordered eigenstate probabilities exhibit a broad power-law regime,⟨w(r)⟩∼N−(1−μ)rμ,0<μ<1.\langle w_{(r)}\rangle\sim\frac{N^{-(1-\mu)}}{r^{\mu}},\qquad 0<\mu<1.(29)Figure 13:Top panel: Rank-ordered eigenstate probabilities, averaged over several eigenstates nearE=0E=0and over100100disorder realizations in RRGs of sizeN=212N=2^{12}witha=−0.5a=-0.5. The rankrrdenotes the position of a probability after the eigenstate weights have been sorted in decreasing order. The dashed lines are guides to the eye, with slopes obtained from log–log fits over1≤r≤1001\leq r\leq 100.Bottom panel: Distribution of the eigenstate probabilities for fixed rankrr, collected from1010eigenstates nearE=0E=0and over500500disorder realizations, fora=−0.5a=-0.5. The probabilitiesw(r)w_{(r)}are narrowly distributed for fixed rankr>1r>1, whilew(1)w_{(1)}is broadly distributed.

The eigenstate probability distributions at fixed rank provide information beyond that contained in the averaged profile. As shown in Fig.13(bottom panel), the distributions ofw(r)w_{(r)}for ranks within the power-law regime,r>1r>1, are narrow, without power-law tails. Correspondingly, for fixedqq,⟨w(r)q⟩∼⟨w(r)⟩q,r>1,\langle w_{(r)}^{q}\rangle\sim\langle w_{(r)}\rangle^{q},\qquad r>1,(30)

up to anNN-independent factor. Thus, the scaling of the participation moments arising from the power-law background can be inferred directly from the mean rank-ordered profile.

Substituting Eq. (29) intoIq=∑r=1N⟨w(r)q⟩I_{q}=\sum_{r=1}^{N}\langle w_{(r)}^{q}\rangle(31)

gives, for the power-law background,Iqbg∼N−q​(1−μ)​∑rr−μ​q.I_{q}^{\mathrm{bg}}\sim N^{-q(1-\mu)}\sum_{r}r^{-\mu q}.(32)

Consequently,Iqbg∼{N1−q,q<1/μ,N−q​(1−μ),q>1/μ.I_{q}^{\mathrm{bg}}\sim\begin{cases}N^{1-q},&q<1/\mu,\\[3.0pt]
N^{-q(1-\mu)},&q>1/\mu.\end{cases}(33)

Equation (33) refers to typical participation moments. Indeed, the negative-f​(α)f(\alpha)part of the disorder-averaged spectrum describes rare events whose expected multiplicity,Nf​(α)N^{f(\alpha)}, vanishes in a typical realization. The spectrum governing typical moments therefore terminates atα=α∗\alpha=\alpha_{*}, wheref​(α∗)=0f(\alpha_{*})=0, rather than continuing into the regionf​(α)<0f(\alpha)<0. The corresponding Legendre transform gives the dashedDqD_{q}curve in Fig.3, whereas retaining the negative-f​(α)f(\alpha)branch yields the mean-moment result shown by the solid curve.
Comparing the crossover atq=1/μq=1/\muwith the crossover atq=βq=\betaobtained from the LDoS distribution in Sec.III.1identifiesβ=1/μ\beta=1/\mu.
This power-law hierarchy therefore produces a piecewise-linear spectrumτ​(q)\tau(q), characteristic of semi-fractality.

The maximal weightw(1)w_{(1)}requires separate consideration because its distribution is much broader than those of the weights atr>1r>1.
Consequently, its contribution to the participation moments must be computed from⟨w(1)q⟩\langle w_{(1)}^{q}\rangle; in general, it cannot be inferred from⟨w(1)⟩q\langle w_{(1)}\rangle^{q}.
Two different asymptotic behaviors are possible. Ifw(1)w_{(1)}decreases with increasingNN, so that it does not remain of order unity, the eigenstate contains no isolated localized component. Its moments are then governed by the power-law hierarchy Eq. (33) of the rank-ordered weights, leading to semi-fractality.
If, instead,w(1)w_{(1)}remains of order unity asN→∞N\to\infty, while the weights atr>1r>1form the power-law-decaying background of Eq. (29), the eigenstate consists of a singular peak above an extended background. The singular peak dominatesIqI_{q}forq>1q>1, whereas the extensive power-law background dominates forq<1q<1. The resulting spectrum isτ​(q)={q−1,q<1,0,q>1,\tau(q)=\begin{cases}q-1,&q<1,\\[3.0pt]
0,&q>1,\end{cases}(34)

corresponding to semi-localization.

These results suggest that the semi-fractality of the chiral Cayley tree is connected to the emergence of a power-law hierarchy in the eigenstate weights, which we conjecture originates from chirality. The calculations presented here were performed on an RRG with approximate chiral symmetry, since the eigenstates of a finite Cayley tree are strongly affected by the boundary, as discussed above. Nevertheless, the observed power-law profiles, together with the relatively narrow fixed-rank distributions forr>1r>1, support the conjecture that chirality generates a power-law-decaying hierarchy of eigenstate weights.

## VIDiscussion and Conclusions

The main result of this paper is the identification of two new classes of eigenfunction statistics, termedsemi-fractalandsemi-localized, and their connection to the chiral symmetry of the Hamiltonian. The semi-fractal regime exhibits an unusual hybrid behavior:Dq=1D_{q}=1forq<βq<\beta, withβ>1\beta>1, as in an ergodic system, whereasDq<1D_{q}<1forq>βq>\beta, as in a multifractal system. At the limiting valueβ=1\beta=1, the semi-localized state hasDq=1D_{q}=1forq<1q<1andDq=0D_{q}=0forq>1q>1, thus combining ergodic and localized behavior.

Although similar statistics have been reported previously, their connection to chirality has not been recognized. We argue that an exact or approximate chiral structure is present in each of these examples.
For instance, theβRM\beta_{\mathrm{RM}}-ensemble in theβRM→∞\beta_{\mathrm{RM}}\rightarrow\inftylimit[20,18]is chiral, as in the equivalent one-dimensional representation, the diagonal disorder vanishes in this limit and the deterministic hopping connects only opposite sublattices; equivalently, the only nonzero off-diagonal matrix elements lie on the first off-diagonals.
In the recent work Ref.[17], an approximate chirality emerges in the vicinity of the percolation transition due to the structure of the Erdős-Rényi graph. Finally, and most notably, in the recent experiment of Google Quantum AI on the 2D XY model, the Hamiltonian is manifestly chiral, as the chiral-symmetry-breaking terms are small in the experimental setting[27].

In this discussion, it is worth mentioning the work[10], in which the ground state of the Malyshev problem in the momentum space has been studied. Here, chirality appears because the ground state of any Hamiltonian ofNNdegrees of freedom can be associated with the center-of-band (E=0E=0) state of the equivalent Hamiltonian of2​N2Ndegrees of freedom with block off-diagonal (chiral) structure.
As a matter of fact, this model, which in real space has random diagonal matrix elements and the deterministic hopping to any site with the power-law decreasing amplitudet∼|n−m|−st\sim|n-m|^{-s}, appears to be very instructive.
In momentum space, the diagonal matrix elements (which are the Fourier transform of the hopping terms in real space) are simply the spectrumE​(p)E(p)of the clean system and thus are non-triviallypp-dependent, whereppis the momentum.
At weak disorder, the clean dispersion near its minimum behaves asE​(p)−E0∼ps−1E(p)-E_{0}\sim p^{s-1}. Therefore, asp→0p\rightarrow 0, for1<s<21<s<2, one gets a vanishing density of statesρ​(E)∼(E−E0)2−ss−1\rho(E)\sim(E-E_{0})^{\frac{2-s}{s-1}}atE=E0E=E_{0}.
This makes thep=0p=0state special and eventually leads to thesemi-localizedground state at1<s<3/21<s<3/2[10]. An important point is that, under these conditions, the eigenfunction weights|ψ​(p)|2|\psi(p)|^{2}arenaturally sortedby the value of momentum.

The two problems share two features. First, the fixed-rank distributions ofw​(r)w(r)in our model and the fixed-momentum distributions of|ψ​(p)|2|\psi(p)|^{2}in Ref.[10]are narrow. Second, their mean profiles obey analogous power laws,⟨w​(r)⟩∼Nμ−1​r−μ\langle w(r)\rangle\sim N^{\mu-1}r^{-\mu}and⟨|ψ​(p)|2⟩∼Nμ−1​p−μ\langle|\psi(p)|^{2}\rangle\sim N^{\mu-1}p^{-\mu}, with0<μ<10<\mu<1. The narrow distributions imply moment factorization, e.g.,⟨w​(r)q⟩∼⟨w​(r)⟩q\langle w(r)^{q}\rangle\sim\langle w(r)\rangle^{q}, up to anNN-independent factor. Summing these moments produces a piecewise-linearτ​(q)\tau(q)and hence a linear segment off​(α)f(\alpha). This is, in fact, the key property leading to semi-fractal and semi-localized phases.

There is, however, an important difference between our model and that of Ref.[10]. In our case, the largest eigenstate weight,w​(1)w(1), is of the same order as that resulting from the power-law fitr−μr^{-\mu}of the states withr>1r>1.
In the model of Ref.[10], it is not so: the weight of thep=0p=0state is of order11, while the power-law fit would give the weight∼Nμ−1\sim N^{\mu-1}withμ<1\mu<1. This anomaly stabilizes the semi-localized state for all1<s<3/21<s<3/2, while in our case it is realized only at the transition between the semi-fractal and the truly localized states ata=aca=a_{c}.

Besides the relation of the semi-fractal and semi-localized states to chirality, we would also like to recall a result reported in Fig.6, namely, the validity of the Mirlin-Fyodorov symmetry Eq. (15) of the LDoS distribution. In our chiral model, the exponentγ\gammadepends continuously on the parameteraaof the model Eq. (2). This dependence on the chiral classes was anticipated in Ref.[24]but did not receive a systematic study.

Finally, another significant result of the paper is that, in the presence of chiral symmetry, the LDoS distribution consists of two power-law segments with the exponents constrained by the Mirlin-Fyodorov symmetry. Breaking the effective chiral symmetry—for example, by probing states away from the band center,E≠0E\neq 0—destroys these power-law regimes.
Furthermore, we report on the power-law dependence of the disorder-averaged rank-ordered weights⟨w​(r)⟩\langle w(r)\rangleon the rankrr. In our opinion, these power laws are signatures of a certain critical nature of chiral systems, which is not present in systems of the usual Dyson symmetry classes. The first evidence of such a criticality, which is the absence of renormalization of conductance to all loop orders, was present already in the first works of F. Wegner and R. Gade[22,23], where the chiral classes were discovered. We leave the further investigation of these issues for future work.

## Acknowledgements

VEK is grateful to M. V. Feigel’man and I. M. Khaymovich for multiple illuminating discussions.

## Data availability

Some of the numerical analysis and plotting code used in this work was developed with assistance from OpenAI Codex. The authors designed the algorithms, reviewed and modified the generated code, and verified the numerical outputs. The code is made available in the GitHub repository in Ref.[1].

## References
- [1]Note:GitHub repository athttps://github.com/CarloVanoni/Chiral_Cayley_Tree.gitCited by:Data availability.
- [2]D. A. Abanin, E. Altman, I. Bloch, and M. Serbyn(2019-05)Colloquium: many-body localization, thermalization, and entanglement.Rev. Mod. Phys.91,pp. 021001.External Links:Document,LinkCited by:§I.
- [3]R. Abou-Chacra, D. J. Thouless, and P. W. Anderson(1973-05)A selfconsistent theory of localization.Journal of Physics C: Solid State Physics6(10),pp. 1734.External Links:Document,LinkCited by:§I.
- [4]E. Abrahams, P. W. Anderson, D. C. Licciardello, and T. V. Ramakrishnan(1979)Scaling theory of localization: absence of quantum diffusion in two dimensions.Physical Review Letters42(10),pp. 673.Cited by:§I,§I.
- [5]A. Altland and M. R. Zirnbauer(2001-04)Novel symmetry classes in mesoscopic normal-superconducting hybrid structures.arXiv.External Links:Document,cond-mat/9602137Cited by:§I.
- [6]B. L. Altshuler, E. Cuevas, L. B. Ioffe, and V. E. Kravtsov(2016-10)Nonergodic phases in strongly disordered random regular graphs.Phys. Rev. Lett.117,pp. 156601.External Links:Document,LinkCited by:§I.
- [7]B. L. Altshuler, Y. Gefen, A. Kamenev, and L. S. Levitov(1997-04)Quasiparticle lifetime in a finite system: a nonperturbative approach.Physical Review Letters78(14),pp. 2803–2806.External Links:ISSN 1079-7114,Link,DocumentCited by:§I.
- [8]B. L. Altshuler, V. E. Kravtsov, A. Scardicchio, P. Sierant, and C. Vanoni(2025-08)Renormalization group for anderson localization on high-dimensional lattices.Proceedings of the National Academy of Sciences of the United States of America122(35),pp. e2423763122.External Links:Document,LinkCited by:§I.
- [9]P. W. Anderson(1958)Absence of diffusion in certain random lattices.Phys. Rev.109(5),pp. 1492–1505.External Links:DocumentCited by:§I.
- [10]M. S. Bahovadinov, F. N. Jalolov, V. E. Kravtsov, B. L. Altshuler, and G. V. Shlyapnikov(2026)Semi-localized ground state in a 1d system with long-range hopping.To be posted.Cited by:§I,§VI,§VI,§VI.
- [11]F. Balducci, G. B. Testasecca, J. Niedda, A. Scardicchio, and C. Vanoni(2025-06)Scaling analysis and renormalization group on the mobility edge in the quantum random energy model.Physical Review B111(21),pp. 214206.External Links:Document,LinkCited by:§I.
- [12]M. Baroni, G. G. Lorenzana, T. Rizzo, and M. Tarzia(2024-05)Corrections to the bethe lattice solution of anderson localization.Phys. Rev. B109,pp. 174216.External Links:Document,LinkCited by:§I.
- [13]D.M. Basko, I.L. Aleiner, and B.L. Altshuler(2006-05)Metal–insulator transition in a weakly interacting many-electron system with localized single-particle states.Ann. Phys. (N. Y.)321(5),pp. 1126–1205.External Links:ISSN 0003-4916,LinkCited by:§I.
- [14]G. Biroli, A. Ribeiro-Teixeira, and M. Tarzia(2012)Difference between level statistics, ergodicity and localization transitions on the Bethe lattice.preprint.External Links:1211.7334Cited by:§I.
- [15]P. W. Brouwer, E. Racine, A. Furusaki, Y. Hatsugai, Y. Morita, and C. Mudry(2002-07)Zero modes in the random hopping model.Physical Review B66(1),pp. 014204.External Links:Document,LinkCited by:§IV.
- [16]J. T. Chalker and G. J. Daniell(1988-08)Scaling, diffusion, and the integer quantized hall effect.Phys. Rev. Lett.61,pp. 593–596.External Links:Document,LinkCited by:§I.
- [17]L. F. Cugliandolo, G. Schehr, M. Tarzia, and D. Venturelli(2024-11)Multifractal phase in the weighted adjacency matrices of random erdös-rényi graphs.Physical Review B110(17),pp. 174202.External Links:Document,LinkCited by:§I,§I,§I,§III.1,§III,§VI.
- [18]A. K. Das, A. Ghosh, and I. M. Khaymovich(2025-07)Emergent multifractality in power-law decaying eigenstates.Physical Review B112(2),pp. 024201.External Links:Document,LinkCited by:§I,§I,§VI.
- [19]A. De Luca, B. L. Altshuler, V. E. Kravtsov, and A. Scardicchio(2014-07)Anderson localization on the Bethe lattice: nonergodicity of extended states.Phys. Rev. Lett.113,pp. 046806.External Links:Document,LinkCited by:§I,§I.
- [20]I. Dumitriu and A. Edelman(2002-11)Matrix models for beta ensembles.Journal of Mathematical Physics43(11),pp. 5830–5847.External Links:Document,LinkCited by:§I,§VI.
- [21]F. Evers and A. D. Mirlin(2008)Anderson transitions.Reviews of Modern Physics80(4),pp. 1355.Cited by:§I,§I,§I.
- [22]R. Gade and F. Wegner(1991-08)The n = 0 replica limit of u(n) and u(n)so(n) models.Nuclear Physics B360(2-3),pp. 213–218.External Links:DocumentCited by:§VI.
- [23]R. Gade(1993-06)Anderson localization for sublattice models.Nuclear Physics B398(3),pp. 499–515.External Links:DocumentCited by:§VI.
- [24]I. A. Gruzberg, A. W. W. Ludwig, A. D. Mirlin, and M. R. Zirnbauer(2011-08)Symmetries of multifractal spectra and field theories of anderson localization.Physical Review Letters107(8),pp. 086403.External Links:Document,LinkCited by:§III,§IV,§VI.
- [25]M. Janssen(1994-04)MULTIFRACTAL analysis of broadly-distributed observables at criticality.International Journal of Modern Physics B8(08),pp. 943–984.External Links:Document,LinkCited by:§I.
- [26]V. E. Kravtsov, A. Ossipov, and O. M. Yevtushenko(2011-06)Return probability and scaling exponents in the critical random matrix ensemble.Journal of Physics A: Mathematical and Theoretical44(30),pp. 305003.External Links:Document,LinkCited by:§I.
- [27]V. E. Kravtsov, L. B. Ioffe, A. V. Lunkin, and M. V. Feigel’man(2026)Uncovering chiral symmetry in quantum simulator of two-dimensional spin-1/21/2XY array in a random filed.To be posted.Cited by:§VI.
- [28]V.E. Kravtsov, B.L. Altshuler, and L.B. Ioffe(2018)Non-ergodic delocalized phase in Anderson model on Bethe lattice and regular graph.Ann. Phys.389,pp. 148–191.External Links:ISSN 0003-4916,Document,LinkCited by:§I.
- [29]A. D. Luca, A. Scardicchio, V. E. Kravtsov, and B. L. Altshuler(2013)Support set of random wave-functions on the Bethe lattice.preprint.External Links:1401.0019Cited by:§I,§I,§I,§IV.
- [30]A. Lukin et al.(2026)Hilbert space signatures of non-ergodic glassy dynamics.External Links:2601.01309,LinkCited by:§I,§I,§I.
- [31]M. Mézard, G. Parisi, and M. Virasoro(1987)Spin glass theory and beyond: an introduction to the replica method and its applications.Vol.9,World Scientific Publishing.Cited by:§I.
- [32]A. D. Mirlin, Y. V. Fyodorov, A. Mildenberger, and F. Evers(2006-07)Exact relations between multifractal exponents at the anderson transition.Physical Review Letters97(4),pp. 046803.External Links:Document,LinkCited by:§I.
- [33]C. Mudry, S. Ryu, and A. Furusaki(2003-02)Density of states for theπ\pi-flux state with bipartite real random hopping only: a weak disorder approach.Physical Review B67(6),pp. 064202.External Links:Document,LinkCited by:§III.
- [34]V. Oganesyan and D. A. Huse(2007-04)Localization of interacting fermions at high temperature.Phys. Rev. B75,pp. 155111.External Links:Document,LinkCited by:§I.
- [35]G. Parisi, S. Pascazio, F. Pietracaprina, V. Ros, and A. Scardicchio(2019-12)Anderson transition on the bethe lattice: an approach with real energies.Journal of Physics A: Mathematical and Theoretical53(1),pp. 014003.External Links:ISSN 1751-8121,Link,DocumentCited by:§I.
- [36]A. Rodriguez, L. J. Vasquez, K. Slevin, and R. A. Römer(2011-10)Multifractal finite-size scaling and universality at the Anderson transition.Phys. Rev. B84,pp. 134209.External Links:Document,LinkCited by:§I.
- [37]S. Savitz, C. Peng, and G. Refael(2019-09)Anderson localization on the Bethe lattice using cages and the Wegner flow.Phys. Rev. B100,pp. 094201.External Links:Document,LinkCited by:§I.
- [38]P. Sierant, M. Lewenstein, A. Scardicchio, L. Vidmar, and J. Zakrzewski(2025-01)Many-body localization in the age of classical computing*.Reports on Progress in Physics88(2),pp. 026502.External Links:ISSN 1361-6633,Link,DocumentCited by:§I.
- [39]K. S. Tikhonov, A. D. Mirlin, and M. A. Skvortsov(2016-12)Anderson localization and ergodicity on random regular graphs.Phys. Rev. B94,pp. 220203.External Links:Document,LinkCited by:§I.
- [40]K.S. Tikhonov and A.D. Mirlin(2021-12)From anderson localization on random regular graphs to many-body localization.Annals of Physics435,pp. 168525.External Links:ISSN 0003-4916,Link,DocumentCited by:§I.
- [41]K. Truong and A. Ossipov(2016-02)Statistics of eigenvectors in the deformed gaussian unitary ensemble of random matrices.Journal of Physics A: Mathematical and Theoretical49(14),pp. 145005.External Links:Document,LinkCited by:§V.3.
- [42]C. Vanoni, B. L. Altshuler, V. E. Kravtsov, and A. Scardicchio(2024-07)Renormalization group analysis of the anderson model on random regular graphs.Proceedings of the National Academy of Sciences of the United States of America121(29),pp. e2401955121.External Links:Document,LinkCited by:§I.
- [43]M.R. Zirnbauer(2006-01)Symmetry classes in random matrix theory.InEncyclopedia of Mathematical Physics,pp. 204–212.External Links:DocumentCited by:§I.
- [44]M. R. Zirnbauer(2023)Wegner model in high dimension: u(1) symmetry breaking and a non-standard phase of disordered electronic matter, I. One-replica theory.preprint.External Links:2309.17323Cited by:§I.

## 


- 


Major funding support from
