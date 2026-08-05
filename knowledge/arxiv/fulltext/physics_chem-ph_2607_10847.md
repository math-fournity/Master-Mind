# Thawed Gaussian Ehrenfest dynamics

**arXiv ID**: 2607.10847v2
**Authors**: Jiří J. L. Vaníček
**Published**: 2026-07-12
**Categories**: physics.chem-ph, quant-ph
**Comments**: Various minor revisions, added Fig. 3, compiled as a reprint
**HTML URL**: https://arxiv.org/html/2607.10847v2

## Abstract

Ehrenfest dynamics is a widely used mixed quantum--classical approach for nonadiabatic molecular dynamics, whereas thawed Gaussian wavepacket dynamics provides an efficient semiclassical description of adiabatic nuclear quantum dynamics. Here we describe thawed Gaussian Ehrenfest dynamics (TGED), which unifies and generalizes these two methods to capture both electronic nonadiabaticity and nuclear quantum effects within a single framework. The fully variational formulation of TGED is derived by applying the time-dependent variational principle to a Hartree product of electronic and Gaussian nuclear wavepackets. Replacing the effective locally quadratic molecular potential obtained from this variational treatment by alternative effective locally quadratic potentials yields an infinite family of TGED methods, of which we present several members. We analyze the limiting cases of the general formalism and show, in particular, that it reduces to conventional Ehrenfest dynamics in the classical limit for the nuclei and to thawed Gaussian wavepacket dynamics in the absence of electronic coupling. Finally, we present explicit geometric integrators for the entire family of methods and identify the conditions under which the different approximations become exact.

## Full Text

Thawed Gaussian Ehrenfest dynamics

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
- 
- 
- 
- 
- 
- License: CC BY 4.0arXiv:2607.10847v2 [physics.chem-ph] 16 Jul 2026

## Thawed Gaussian Ehrenfest dynamicsJiří Vaníčekjiri.vanicek@epfl.chLaboratory of Theoretical Physical Chemistry, Institut des Sciences et
Ingénierie Chimiques, Ecole Polytechnique Fédérale de Lausanne (EPFL),
CH-1015, Lausanne, Switzerland

## Abstract

Ehrenfest dynamics is a widely used mixed quantum–classical approach for
nonadiabatic molecular dynamics, whereas thawed Gaussian wavepacket dynamics
provides an efficient semiclassical description of adiabatic nuclear quantum
dynamics. Here we describe thawed Gaussian Ehrenfest dynamics (TGED), which
unifies and generalizes these two methods to capture both electronic
nonadiabaticity and nuclear quantum effects within a single framework. The
fully variational formulation of TGED is derived by applying the
time-dependent variational principle to a Hartree product of electronic and
Gaussian nuclear wavepackets. Replacing the effective locally quadratic
molecular potential obtained from this variational treatment by alternative
effective locally quadratic potentials yields an infinite family of TGED
methods, of which we present several members. We analyze the limiting cases of
the general formalism and show, in particular, that it reduces to conventional
Ehrenfest dynamics in the classical limit for the nuclei and to thawed
Gaussian wavepacket dynamics in the absence of electronic coupling. Finally,
we present explicit geometric integrators for the entire family of methods and
identify the conditions under which the different approximations become exact.

## IIntroduction

Due to their vastly different masses, nuclei and electrons in molecules evolve
on very different time scales, which often permits their separation within the
Born–Oppenheimer approximation.[1,2]This approximation, however, breaks down near conical intersections and, more
generally, whenever adiabatic potential-energy surfaces become nearly
degenerate.[3]In such situations, an accurate
description of molecular quantum dynamics requires nonadiabatic simulations
that explicitly account for the coupling between electronic and nuclear
motion.[4]

Because exact quantum simulations in either the
adiabatic[5]or diabatic[6]electronic representation, as well as exact-factorization
approaches,[7]remain limited to systems with only a few
degrees of freedom, more efficient low-rank-tensor-based methods have been
developed, most notably the multiconfigurational time-dependent Hartree
(MCTDH) method.[8]Although such methods substantially
reduce the exponential scaling with system size, they remain prohibitively
expensive for on-the-flyab initiosimulations. This limitation has
motivated the development of multi-trajectory Gaussian-basis methods,
including multiple spawning,[9]variational
multiconfigurational Gaussians,[10]and
multiconfigurational Ehrenfest dynamics.[11]While these
approaches can, in principle, converge to the exact quantum solution,
practical convergence typically requires a large number of trajectories and is
complicated by numerical difficulties associated with the nonorthogonality of
Gaussian basis functions.

For greater computational efficiency, albeit at the expense of accuracy, many
researchers have turned to mixed quantum–classical
methods,[12,13,14,15]which treat electrons quantum mechanically while describing nuclei
classically. On the one hand, numerous
extensions[16,17,18]of Tully’s fewest-switches surface-hopping method[19]were
developed to describe nonadiabatic transitions between electronic states as
well as the correlation between the nuclear and electronic degrees of freedom.
On the other hand, there exist various mean-field approaches, including the
single-trajectory Ehrenfest dynamics,[20]and locally
mean-field methods, such as the multi-trajectory Ehrenfest
dynamics.[21]More recently, the single-potential-evaluation
Ehrenfest dynamics (SPEED) was introduced to reduce the computational cost of
multi-trajectory Ehrenfest dynamics to that of propagating a singleab
initiotrajectory while retaining some non-mean-field
effects.[22]Despite its mean-field nature,
Ehrenfest dynamics has proved useful in many
applications[23,24,25]because it captures some nonadiabatic effects and is known to be exact under
well-defined conditions (see Sec.VII.4).

A major limitation of mixed quantum–classical methods, including both surface
hopping and Ehrenfest dynamics, is that they neglect nuclear quantum effects
altogether. Such effects can instead be approximately described using
semiclassical approximations, including initial-value
representation[26]of the Van Vleck propagator,[27]the Herman-Kluk propagator[28]and their
extensions.[29]Among semiclassical approaches, the
simplest is Heller’s single-trajectory thawed Gaussian wavepacket dynamics
(TGWD)[30,31]and its
variants.[32,33,34,35]TGWD incorporates nuclear quantum effects while accounting, at least
approximately, for anharmonicity. Combined with on-the-flyab initioelectronic-structure calculations, it has been successfully applied to
vibrationally resolved electronic spectroscopy at both
zero[36,37]and
finite[38,39]temperatures, as well
as to studies of electronic coherence and
decoherence.[40,41,42]Moreover, TGWD is exact for globally harmonic potentials
(Sec.VII.2).

Motivated by the complementary strengths of Ehrenfest dynamics and TGWD, here
we describe “thawed Gaussian Ehrenfest
dynamics” (TGED), which unifies and generalizes both
approaches. Whereas Ehrenfest dynamics captures nonadiabatic effects but
neglects nuclear quantum effects, TGWD includes nuclear quantum effects but is
restricted to a single potential energy surface. TGED combines these two
complementary descriptions within a single framework. Although the resulting
method remains a mean-field approximation and is therefore necessarily
approximate, it captures both nonadiabatic and nuclear quantum effects (see
Fig.1) while retaining the computational efficiency
of single-trajectory propagation. Whereas the severe limitations of mean-field
methods are well known, Fig.1intentionally shows the
results for a system, in which the mean-field TGED is exact, but neither TGWD
nor Ehrenfest dynamics is. The system, which consists of ten vertically
displaced two-dimensional harmonic potentials coupled with constant couplings,
is simple because the dynamics of nuclei and electrons is uncorrelated, yet
there exist realistic systems whose Hamiltonians are not very different. The
TGED method possesses well-defined limiting cases
(Sec.V) and becomes exact for clearly identifiable
classes of Hamiltonians (Sec.VII.3). The strengths and
limitations of TGED in applications to nonadiabatic dynamics in the vicinity
of conical intersections will be explored
elsewhere.[43]

The remainder of this paper is organized as follows.
SectionIIreviews the time-dependent Hartree approximation
for the molecular wavefunction and specializes it to the diabatic
representation and separable Hamiltonians. In Sec.III, we derive
the general thawed Gaussian Ehrenfest dynamics by combining the time-dependent
Hartree approximation with a Gaussian ansatz for the nuclear wavepacket.
SectionIVintroduces an infinite family of TGED methods
that differ in the choice of the effective local quadratic potential-energy
matrix. In Sec.V, we show how different limits of the
TGED recover Gaussian wavepacket dynamics, Ehrenfest dynamics, or classical
nuclear dynamics. SectionVIpresents geometric integrators
for the general TGED equations of motion, while Sec.VIIestablishes the conditions under which the various approximations become
exact. Finally, Sec.VIIIconcludes the paper.Figure 1:Comparison
of thawed Gaussian Ehrenfest dynamics (TGED) with Ehrenfest dynamics, thawed
Gaussian wavepacket dynamics (TGWD), and purely classical dynamics in a
system of ten vertically displaced two-dimensional harmonic oscillators
coupled by a coordinate-independent electronic coupling. The exact quantum results
are indicatd by the dashed line. The upper panels (a)–(d)
quantify the nonadiabatic dynamics by showing the time-dependent populationP0​(t)P_{0}(t)of
the ground electronic state, whereas the lower panels (e)–(h) illustrate nuclear
quantum effects through the expectation value⟨V⟩\langle V\rangleof the potential energy. For
this model system, TGED is exact (see Sec.VII.3). [The
single-Hessian (SH) TGED from Sec.IV.4was used, but all TGED
variants from Sec.IVwould be exact here.]
Ehrenfest dynamics reproduces the nonadiabatic dynamics exactly but fails to
capture nuclear quantum effects. Conversely, TGWD accurately describes the
nuclear quantum dynamics but cannot account for nonadiabatic transitions.
Purely classical dynamics captures neither nonadiabatic nor nuclear quantum
effects.

## IITheoretical background

Let us recall the time-dependent Hartree (TDH) approximation for the
molecular wavefunction, because its mixed quantum-semiclassical treatment will
yield the TGED in the next section.

## II.1Molecular Schrödinger equation

Quantum evolution of a molecule is governed by the time-dependent
Schrödinger equation (TDSE)i​ℏ​Ψ˙​(t)=ℋ​Ψ​(t),i\hbar\dot{\Psi}(t)=\mathcal{H}\Psi(t),(1)

whereΨ​(t)\Psi(t)denotes the molecular state at timettandℋ\mathcal{H}is
the molecular Hamiltonian. (In general, operators acting on both nuclei and
electrons will be denoted by a calligraphic font, whereas operators acting
only on nuclei or only on electrons will have a hat^~\hat{}.) It will be
convenient to express the molecular Hamiltonian as the sumℋ=ℋ​(q^,p^)=T​(p^)+𝒱​(q^)\mathcal{H}=\mathcal{H}(\hat{q},\hat{p})=T(\hat{p})+\mathcal{V}(\hat{q})(2)

of the nuclear kinetic energy operatorT​(p^)T(\hat{p})and the “remainder”𝒱\mathcal{V}, which includes the electronic
kinetic energy as well as the potential energy due to electron-electron
repulsion, nucleus-electron attraction, and nucleus-nucleus repulsion.
Although𝒱\mathcal{V}is sometimes called the “electronic
Hamiltonian,” the calligraphic font is used because𝒱\mathcal{V}still acts on both nuclear and electronic degrees of freedom. We
will assume that the nuclear kinetic energy is a quadratic formT​(p)=pT⋅m−1⋅p/2T(p)=p^{T}\cdot m^{-1}\cdot p/2(3)

of the nuclear momentumpp. In a system withDDnuclear degrees of freedom,
the nuclear positionqqand momentumppareDD-dimensional vectors, whereas
the massmmcan, in general, be a real symmetricD×DD\times Dmatrix.

## II.2Time-dependent Hartree approximation

The TDH approximation[44,45,46]provides the best approximate solution of the molecular TDSE
(1) among those, in which the molecular state can be written
as theHartree productΨ​(t)=a​(t)​ψ​(t)​φ​(t)\Psi(t)=a(t)\psi(t)\varphi(t)(4)

of the nuclear wavepacketψ​(t)\psi(t)and electronic wavepacketφ​(t)\varphi(t).
The complex numbera​(t)a(t)is inserted for convenience. We further assume that
the initial molecular state is normalized, i.e.,‖Ψ​(0)‖=1\left\|\Psi(0)\right\|=1, thata​(0)=1a(0)=1, and that nuclear and electronic states are
normalized at all timestt,‖ψ​(t)‖=‖φ​(t)‖=1\left\|\psi(t)\right\|=\left\|\varphi(t)\right\|=1.

The optimal solution is found by applying the time-dependent variational
principle (TDVP)[44,45,46]to the
ansatz (4). The TDVP requires that an arbitrary
variationδ​Ψ\delta\Psiof the solutionΨ\Psisatisfy the relation⟨δ​Ψ|i​ℏ​dd​t−ℋ|Ψ⟩=0.\langle\delta\Psi|i\hbar\frac{d}{dt}-\mathcal{H}|\Psi\rangle=0.(5)

The solution, called the TDH
approximation,[44,45,46]conserves
both the total energyE≡⟨ℋ⟩Ψ​(t)=⟨Ψ​(t)|ℋ|Ψ​(t)⟩=constE\equiv\langle\mathcal{H}\rangle_{\Psi(t)}=\langle\Psi(t)|\mathcal{H}|\Psi(t)\rangle=\operatorname{const}(6)

and the norm‖Ψ​(t)‖=1\left\|\Psi(t)\right\|=1of the molecular wavefunction.
Whereas both conservation laws are enforced by the
TDVP,[47]energy conservation obviously requires
Hamiltonianℋ\mathcal{H}to be time-independent and norm conservation is
guaranteed by including prefactora​(t)a(t)in the
ansatz (4).[46]This prefactor
evolves asa​(t)=ei​E​t/ℏ,a(t)=e^{iEt/\hbar},(7)

while the nuclear and electronic states satisfy the systemi​ℏ​ψ˙\displaystyle i\hbar\dot{\psi}=H^n​ψ,\displaystyle=\hat{H}_{n}\psi,(8)i​ℏ​φ˙\displaystyle i\hbar\dot{\varphi}=H^e​φ\displaystyle=\hat{H}_{e}\varphi(9)

of coupled nonlinear Schrödinger equations with mean-field nuclear and
electronic Hamiltonian operatorsH^n\displaystyle\hat{H}_{n}:=⟨ℋ⟩e≡⟨φ​(t)|ℋ|φ​(t)⟩,\displaystyle:=\langle\mathcal{H}\rangle_{e}\equiv\langle\varphi(t)|\mathcal{H}|\varphi(t)\rangle,(10)H^e\displaystyle\hat{H}_{e}:=⟨ℋ⟩n≡⟨ψ​(t)|ℋ|ψ​(t)⟩,\displaystyle:=\langle\mathcal{H}\rangle_{n}\equiv\langle\psi(t)|\mathcal{H}|\psi(t)\rangle,(11)

where⟨⋅⟩e:=⟨φ|⋅|φ⟩\langle\cdot\rangle_{e}:=\langle\varphi|\cdot|\varphi\rangleand⟨⋅⟩n:=⟨ψ|⋅|ψ⟩\langle\cdot\rangle_{n}:=\langle\psi|\cdot|\psi\rangledenote the averages
over the electronic and nuclear states, respectively. These mean-field
operators satisfy the obvious identity⟨H^e⟩e=⟨H^n⟩n=E\langle\hat{H}_{e}\rangle_{e}=\langle\hat{H}_{n}\rangle_{n}=E(12)

and—in contrast to the standard TDSE—the differential equations forψ\psiandφ\varphiare (i) coupled and (ii) nonlinear, due to the dependence of the
mean-field HamiltoniansH^n\hat{H}_{n}andH^e\hat{H}_{e}on the state of the
other subsystem. The solution expressed by Eqs. (7)-(9) is unique except for an obvious gauge
freedom in distributing the phases among the three factorsaa,ψ\psi, andφ\varphi.

## II.3Diabatic representation of the electronic state

To express the TDH approximation in the diabatic representation, let us
expand the electronic stateφ​(t)\varphi(t)in an orthonormal diabatic basis|k⟩|k\rangleas|φ​(t)⟩=∑kck​(t)​|k⟩,|\varphi(t)\rangle=\sum_{k}c_{k}(t)|k\rangle,(13)

where⟨j|k⟩=δj​k\langle j|k\rangle=\delta_{jk}. The basis is called “diabatic” because the electronic basis states|k⟩|k\rangleare assumed to be independent of nuclear coordinatesqq. More precisely,
electronic states|k⟩|k\ranglemay depend on nuclear coordinatesqqweakly,
but thisqq-dependence can be neglected in the action of the nuclear kinetic
energy operator on the electronic
states.[48,49]

In the diabatic basis, the time-dependent Hartree
Eqs. (8) and (9) are
equivalent to the equationsi​ℏ​ψ˙\displaystyle i\hbar\dot{\psi}=Hn​(q^,p^;𝐜)​ψ,\displaystyle=H_{n}(\hat{q},\hat{p};\mathbf{c})\psi,(14)i​ℏ​𝐜˙\displaystyle i\hbar\dot{\mathbf{c}}=𝐇e​(ψ)​𝐜,\displaystyle=\mathbf{H}_{e}(\psi)\mathbf{c},(15)

where the mean-field nuclear HamiltonianHn​(q^,p^;𝐜):=𝐜†​𝐇​(q^,p^)​𝐜H_{n}(\hat{q},\hat{p};\mathbf{c}):=\mathbf{c}^{{\dagger}}\mathbf{H}(\hat{q},\hat{p})\mathbf{c}(16)

is the average over the electronic state𝐜\mathbf{c}of the matrix operator𝐇​(q^,p^)\mathbf{H}(\hat{q},\hat{p}), which consists of matrix elementsHj​k​(q^,p^):=⟨j|ℋ​(q^,p^)|k⟩H_{jk}(\hat{q},\hat{p}):=\langle j|\mathcal{H}(\hat{q},\hat{p})|k\rangle(17)

of the molecular Hamiltonianℋ​(q^,p^)\mathcal{H}(\hat{q},\hat{p})and where the
electronic mean-field matrix Hamiltonian𝐇e​(ψ):=⟨ψ|𝐇​(q^,p^)|ψ⟩\mathbf{H}_{e}\left(\psi\right):=\langle\psi|\mathbf{H}(\hat{q},\hat{p})|\psi\rangle(18)

is the average of𝐇​(q^,p^)\mathbf{H}(\hat{q},\hat{p})over the nuclear stateψ\psi.

## II.4Separable Hamiltonian

Until now, we have not taken advantage of the separable form (2)
of the molecular Hamiltonianℋ\mathcal{H}in the diabatic representation.
Sinceℋ\mathcal{H}is a sum (2) of a function of nuclear momenta
and a function of nuclear coordinates, the electronic matrix representation ofℋ\mathcal{H}is𝐇​(q^,p^)=T​(p^)​𝟏+𝐕​(q^),\mathbf{H}(\hat{q},\hat{p})=T(\hat{p})\mathbf{1}+\mathbf{V}(\hat{q}),(19)

where𝐕​(q^)\mathbf{V}(\hat{q})is composed of electronic matrix elementsVj​k​(q^):=⟨j|𝒱​(q^)|k⟩V_{jk}(\hat{q}):=\langle j|\mathcal{V}(\hat{q})|k\rangle(20)

of the diabatic potential energy operator. The nuclear mean-field Hamiltonian
(10) then becomesH^n=T​(p^)+Vn​(q^;𝐜),\hat{H}_{n}=T(\hat{p})+V_{n}(\hat{q};\mathbf{c}),(21)

with the mean-field nuclear potentialVn​(q^;𝐜):=𝐜†​𝐕​(q^)​𝐜,V_{n}(\hat{q};\mathbf{c}):=\mathbf{c}^{{\dagger}}\mathbf{V}(\hat{q})\mathbf{c,}(22)

while the electronic mean-field Hamiltonian, expressed in the electronic
basis, is the matrix𝐇e​(ψ)=⟨T​(p^)⟩n​𝟏+⟨𝐕​(q^)⟩n.\mathbf{H}_{e}(\psi)=\langle T(\hat{p})\rangle_{n}\mathbf{1}+\langle\mathbf{V}(\hat{q})\rangle_{n}.(23)

As a result, the coupled Schrödinger equations
(14) and (15) may be
written asi​ℏ​ψ˙\displaystyle i\hbar\dot{\psi}=[T​(p^)+Vn​(q^;𝐜)]​ψ,\displaystyle=\left[T(\hat{p})+V_{n}(\hat{q};\mathbf{c})\right]\psi,(24)i​ℏ​𝐜˙\displaystyle i\hbar\dot{\mathbf{c}}=[⟨T​(p^)⟩n+⟨𝐕​(q^)⟩n]​𝐜.\displaystyle=[\langle T(\hat{p})\rangle_{n}+\langle\mathbf{V}(\hat{q})\rangle_{n}]\mathbf{c}.(25)

Even if only a few electronic states are involved in the dynamics,
implementation of the mean-field TDH for a general nuclear wavefunction has a
high computational cost because it scales exponentially withDD. As we will
now see, in the TGED, the nuclear wavefunction is a Gaussian, with only a few
parameters. The TGED therefore scales very favorably withDDand is
applicable to polyatomic molecules.

## IIIThawed Gaussian Ehrenfest dynamics

To derive the TGED, let us assume that the nuclear stateψ​(t)\psi(t)in
Eq. (4) is a Gaussian wavepacketψ​(q,t)=exp⁡[iℏ​(12​xT⋅At⋅x+ptT⋅x+γt)],\psi(q,t)=\exp\left[\frac{i}{\hbar}\left(\frac{1}{2}x^{T}\cdot A_{t}\cdot x+p_{t}^{T}\cdot x+\gamma_{t}\right)\right],(26)

wherex:=q−qtx:=q-q_{t}, in “A​γA\gamma” parametrization[50,51,47]or
byψ​(q,t)\displaystyle\psi(q,t)=(π​ℏ)−D/4​(detQt)−1/2\displaystyle=\left(\pi\hbar\right)^{-D/4}\left(\det Q_{t}\right)^{-1/2}×exp⁡[iℏ​(12​xT⋅Pt⋅Qt−1⋅x+ptT⋅x+St)]\displaystyle\times\exp\left[\frac{i}{\hbar}\left(\frac{1}{2}x^{T}\cdot P_{t}\cdot Q_{t}^{-1}\cdot x+p_{t}^{T}\cdot x+S_{t}\right)\right](27)

in “Q​P​SQPS” parametrization.[52,53,54,46,55,47]The real vector parametersqtq_{t}andptp_{t}are the expectation values of
position and momentum. The complex symmetricD×DD\times DmatrixAtA_{t}with
positive-definite imaginary part controls the width of the Gaussian and
position-momentum correlation, while the real and imaginary parts of the
complex scalarγt\gamma_{t}control, respectively, the phase and norm of the
wavepacket. In theQ​P​SQPSparametrization,QtQ_{t}andPtP_{t}are complexD×DD\times Dmatrices, which satisfy certain symplecticity
conditions,[46]andStS_{t}is a real parameter
generalizing the classical action.

In the absence of coupling to electronic degrees of freedom, a Gaussian
nuclear wavepacket remains Gaussian if it is propagated with the standard
quadratic kinetic energy operator (3) and with a potential energy
operator that is at most quadratic inqq, but that can depend both on time
and state.[34]Motivated by this observation, let us
approximate the potential energy matrix𝐕​(q^)\mathbf{V}(\hat{q})with an
effective state-dependent potential that is at most quadratic inq^\hat{q}.
While the nuclear mean-field potentialVn​(q^;𝐜)=𝐜†​𝐕​(q^)​𝐜V_{n}(\hat{q};\mathbf{c})=\mathbf{c}^{{\dagger}}\mathbf{V}(\hat{q})\mathbf{c}in
Eq. (21) already depends on the state of the system
via the electronic wavefunction𝐜\mathbf{c}, the effective potential𝐕eff​(q^;ψ)\mathbf{V}_{\text{eff}}(\hat{q};\psi)may also depend on the nuclear stateψ\psi. Therefore, let us assume that𝐕(q^)≈𝐕eff(q^;ψ)=𝐕0+𝐕1⋅Tx^+x^T⋅𝐕2⋅x^/2,\mathbf{V}(\hat{q})\approx\mathbf{V}_{\text{eff}}(\hat{q};\psi)=\mathbf{V}_{0}+\mathbf{V}_{1}{}^{T}\cdot\hat{x}+\hat{x}^{T}\cdot\mathbf{V}_{2}\cdot\hat{x}/2,(28)

wherex^=q^−qt\hat{x}=\hat{q}-q_{t}is a shifted position operator and𝐕0\mathbf{V}_{0},𝐕1\mathbf{V}_{1}, and𝐕2\mathbf{V}_{2}are possiblyψ\psi-dependent realS×SS\times Ssymmetric matrices ofDD-dimensional scalars,
vectors, and symmetric matrices, respectively. In this case, the mean-field
nuclear potentialVn​(q^;𝐜)V_{n}(\hat{q};\mathbf{c}), appearing in the mean-field
nuclear TDSE (24), will also be approximated asVn​(q^;𝐜)≈Vn,eff​(q^;ψ,𝐜):=𝐜†​𝐕eff​(q^;ψ)​𝐜V_{n}(\hat{q};\mathbf{c})\approx V_{n,\text{eff}}(\hat{q};\psi,\mathbf{c}):=\mathbf{c}^{{\dagger}}\mathbf{V}_{\text{eff}}(\hat{q};\psi)\mathbf{c}(29)

with an effective quadratic potentialVn,eff(q^;ψ,𝐜)=Vn,0+Vn,1⋅Tx^+x^T⋅Vn,2⋅x^/2,V_{n,\text{eff}}(\hat{q};\psi,\mathbf{c})=V_{n,0}+V_{n,1}{}^{T}\cdot\hat{x}+\hat{x}^{T}\cdot V_{n,2}\cdot\hat{x}/2,(30)

whereVn,0V_{n,0},Vn,1V_{n,1}, andVn,2V_{n,2}are, respectively, theDD-dimensional scalar, vector, and symmetric matrixVn,j:=𝐜†​𝐕j​𝐜.V_{n,j}:=\mathbf{c}^{{\dagger}}\mathbf{V}_{j}\mathbf{c}.(31)

Remarkably, the nuclear factorψ​(t)\psi(t)of the Hartree product will remain
Gaussian because the effective mean-field nuclear potential (30)
is quadratic inq^\hat{q}. This will hold as long as the molecular potential𝐕​(q^)\mathbf{V}(\hat{q})is approximated by a possibly state- and time-dependent,
but at most quadratic potential𝐕eff​(q^;ψ)\mathbf{V}_{\text{eff}}(\hat{q};\psi). We
thus obtain a family ofthawed Gaussian Ehrenfest dynamicsmethods,
which differ only by the choice of the quadratic effective potential𝐕eff​(q^;ψ)\mathbf{V}_{\text{eff}}(\hat{q};\psi). As in the single-surface, purely
nuclear case,[34]one can consider the
variational,[56]local
harmonic,[57]single-Hessian,[33]global harmonic, local cubic
variational,[58]single quartic
variational,[34]and other approximations; we shall do so in
the next section.

With the effective quadratic potential, the equations of motion for nuclei and
electrons becomei​ℏ​ψ˙\displaystyle i\hbar\dot{\psi}=[T​(p^)+Vn,eff​(q^;ψ,𝐜)]​ψ,\displaystyle=[T(\hat{p})+V_{n,\text{eff}}(\hat{q};\psi,\mathbf{c})]\psi,(32)i​ℏ​𝐜˙\displaystyle i\hbar\dot{\mathbf{c}}=[⟨T​(p^)⟩n+⟨𝐕eff​(q^;ψ)⟩n]​𝐜.\displaystyle=[\langle T(\hat{p})\rangle_{n}+\langle\mathbf{V}_{\text{eff}}(\hat{q};\psi)\rangle_{n}]\mathbf{c}.(33)

Moreover, the nuclear expectation values of kinetic and potential energies,
appearing in the electronic TDSE (33), can be evaluated
analytically as⟨T​(p^)⟩n\displaystyle\langle T(\hat{p})\rangle_{n}=T​(pt)+Trn⁡[m−1⋅Cov⁡(p)]/2,\displaystyle=T(p_{t})+\operatorname{Tr}_{n}[m^{-1}\cdot\operatorname{Cov}(p)]/2,(34)⟨𝐕eff​(q^;ψ)⟩n\displaystyle\langle\mathbf{V}_{\text{eff}}(\hat{q};\psi)\rangle_{n}=𝐕0+Trn⁡[𝐕2⋅Cov⁡(q)]/2,\displaystyle=\mathbf{V}_{0}+\operatorname{Tr}_{n}[\mathbf{V}_{2}\cdot\operatorname{Cov}(q)]/2,(35)

whereTrn\operatorname{Tr}_{n}denotes a matrix trace overDDnuclear degrees
of freedom [Trn⁡(A)=∑j=1DAj​j\operatorname{Tr}_{n}(A)=\sum_{j=1}^{D}A_{jj}]
and[34]Cov⁡(q^)\displaystyle\operatorname{Cov}(\hat{q})=(ℏ/2)​(Im⁡At)−1=(ℏ/2)​Qt⋅Qt†,\displaystyle=(\hbar/2)\left(\operatorname{Im}A_{t}\right)^{-1}=(\hbar/2)Q_{t}\cdot Q_{t}^{{\dagger}},(36)Cov⁡(p^)\displaystyle\operatorname{Cov}(\hat{p})=(ℏ/2)​At⋅(Im⁡At)−1⋅At∗=(ℏ/2)​Pt⋅Pt†\displaystyle=(\hbar/2)A_{t}\cdot\left(\operatorname{Im}A_{t}\right)^{-1}\cdot A_{t}^{\ast}=(\hbar/2)P_{t}\cdot P_{t}^{{\dagger}}(37)

are the position and momentum covariance matrices.

As follows from the general thawed Gaussian wavepacket dynamics for a purely
nuclear wavepacket,[34]the nuclear TDSE (32) is equivalent to the systemq˙t\displaystyle\dot{q}_{t}=m−1⋅pt,\displaystyle=m^{-1}\cdot p_{t},(38)p˙t\displaystyle\dot{p}_{t}=−Vn,1,\displaystyle=-V_{n,1},(39)A˙t\displaystyle\dot{A}_{t}=−At⋅m−1⋅At−Vn,2,\displaystyle=-A_{t}\cdot m^{-1}\cdot A_{t}-V_{n,2}\,,(40)γ˙t\displaystyle\dot{\gamma}_{t}=T​(pt)−Vn,0+(i​ℏ/2)​Tr(m−1⋅At).\displaystyle=T(p_{t})-V_{n,0}+(i\hbar/2)\operatorname*{Tr}\left(m^{-1}\cdot A_{t}\right).(41)

of ordinary differential equations for the Gaussian’s parameters. In theQ​P​SQPSparametrization, Eqs. (40) and (41) forAtA_{t}andγt\gamma_{t}are replaced withQ˙t\displaystyle\dot{Q}_{t}=m−1⋅Pt,\displaystyle=m^{-1}\cdot P_{t},(42)P˙t\displaystyle\dot{P}_{t}=−Vn,2⋅Qt,\displaystyle=-V_{n,2}\cdot Q_{t},(43)S˙t\displaystyle\dot{S}_{t}=T​(pt)−Vn,0.\displaystyle=T(p_{t})-V_{n,0}.(44)

The only difference from the equations for a purely nuclear wavepacket[34]is that Eqs. (38)–(44) are
coupled to the electronic propagation (33) via the
coefficientsVn,jV_{n,j}defined in Eq. (31) from the effective
potential (28). Figure2visualizes the TGED by
displaying a trajectory of the nuclear wavepacketψ​(q,t)\psi(q,t)as well as the
original and effective potentials.Figure 2:Example of thawed Gaussian Ehrenfest dynamics of the molecular wavepacketΨ​(q,t)=a​(t)​ψ​(q,t)​φ​(t)\Psi(q,t)=a(t)\psi(q,t)\varphi(t)moving in the molecular matrix potential𝐕​(q)\mathbf{V}(q)[Eq. (20)], diagonal elements of which are shown as blue curves. The nuclear
wavepacketψ​(q,t)\psi(q,t)(black thin line) is
a Gaussian (26) that exactly solves Eq. (32) with an effective nuclear
potentialVn,eff​(q^;ψ,𝐜)V_{n,\text{eff}}(\hat{q};\psi,\mathbf{c})[Eq. (30), indicated
by green thick line at instant 2], which is obtained from the effective molecular
potential𝐕eff​(q^;ψ)\mathbf{V}_{\text{eff}}(\hat{q};\psi)by Eq. (29), whose coefficients
are here given by the single-Hessian approximation [Eqs. (68) and (69]
to the original, coupled
Morse system𝐕​(q)\mathbf{V}(q). The electronic wavepacketφ​(t)\varphi(t), expanded in the diabatic
basis [Eq. (13)], follows the coupled Eq. (33). The
red dashed line indicates the evolution of the zeroth-order coefficientVn,0V_{n,0}of the nuclear
effective potential (30) from instant 1 to 3.

From the construction of the TGED, it is clear that the method conserves the
norm of both nuclear and electronic states, i.e.,‖ψt‖=‖𝐜t‖=1\left\|\psi_{t}\right\|=\left\|\mathbf{c}_{t}\right\|=1. This can also be
seen explicitly from the Hermitian property of both electronic and nuclear
mean-field Hamiltonians. Because the prefactora​(t)a(t)is a complex unit, the
norm of the molecular wavefunction is also conserved:‖Ψ​(t)‖=1\left\|\Psi(t)\right\|=1. By construction, the TGED is reversible, as are the
thawed Gaussian wavepacket and Ehrenfest dynamics individually. When the
effective quadratic potential is obtained by the variational principle, also
the exact energy is conserved; the resulting “variational
TGED” is discussed in Sec.IV.1.

## IVFamily of thawed Gaussian Ehrenfest dynamics
methods

By choosing different effective locally quadratic
potentials (28), one obtains different thawed Gaussian
Ehrenfest dynamics methods. As in the single-surface case,[34]there is an infinite family of such methods. In the nonadiabatic setting, the
effective potential  (28) can be thought of as a local and
state-dependent variant of the popular second-order vibronic coupling
model.[59,60]

## IV.1Variational thawed Gaussian Ehrenfest dynamics

The most accurate TGED method is obtained by applying the variational
principle. Remarkably, for a fully variational treatment of the Hartree
product of an electronic and Gaussian nuclear wavepackets, one does not need
to do any extra work. The electronic TDSE (33) is already
fully variational, while the mean-field nuclear TDSE (32)
can be thought of as a standard nuclear TDSE driven by a time-dependent
external potentialVn​(q^,t):=Vn​(q^;𝐜t)≡𝐜t†​𝐕​(q^)​𝐜t.V_{n}(\hat{q},t):=V_{n}(\hat{q};\mathbf{c}_{t})\equiv\mathbf{c}_{t}^{{\dagger}}\mathbf{V}(\hat{q})\mathbf{c}_{t}\mathbf{.}(45)

Applying the TDVP to the mean-field nuclear TDSE (24)
with a Gaussian ansatz (26) or (27) yields a
quadratic effective nuclear potentialVn,var(q^)=Vn,0+Vn,1⋅Tx^+x^T⋅Vn,2⋅x^/2,V_{n,\text{var}}(\hat{q})=V_{n,0}+V_{n,1}{}^{T}\cdot\hat{x}+\hat{x}^{T}\cdot V_{n,2}\cdot\hat{x}/2,(46)

with scalar, vector, and matrix coefficientsVn,0\displaystyle V_{n,0}=⟨Vn​(q^,t)⟩n−Trn⁡[⟨Vn′′​(q^,t)⟩n⋅Cov⁡(q)]/2,\displaystyle=\langle V_{n}(\hat{q},t)\rangle_{n}-\operatorname{Tr}_{n}[\langle V_{n}^{\prime\prime}(\hat{q},t)\rangle_{n}\cdot\operatorname{Cov}(q)]/2,\text{
}(47)Vn,1\displaystyle V_{n,1}=⟨Vn′​(q^,t)⟩n,\displaystyle=\langle V_{n}^{\prime}(\hat{q},t)\rangle_{n},(48)Vn,2\displaystyle V_{n,2}=⟨Vn′′​(q^,t)⟩n,\displaystyle=\langle V_{n}^{\prime\prime}(\hat{q},t)\rangle_{n},(49)

as shown for the variational TGWD in the one-surface
case.[32,34]To find the coefficients𝐕j\mathbf{V}_{j}of the effective molecular potential𝐕var​(q^)\mathbf{V}_{\text{var}}(\hat{q})in Eq. (28), we note that⟨Vn(j)​(q^,t)⟩n=𝐜t†​⟨𝐕(j)​(q^)⟩n​𝐜t=⟨𝐕(j)​(q^)⟩.\langle V_{n}^{(j)}(\hat{q},t)\rangle_{n}=\mathbf{c}_{t}^{{\dagger}}\langle\mathbf{V}^{(j)}(\hat{q})\rangle_{n}\mathbf{c}_{t}=\langle\mathbf{V}^{(j)}(\hat{q})\rangle.(50)

HenceVn,j=𝐜t†​𝐕j​𝐜tV_{n,j}=\mathbf{c}_{t}^{{\dagger}}\mathbf{V}_{j}\mathbf{c}_{t}, as in
Eq. (31), where𝐕0\displaystyle\mathbf{V}_{0}=⟨𝐕​(q^)⟩n−Trn⁡[⟨𝐕′′​(q^)⟩n⋅Cov⁡(q)]/2,\displaystyle=\langle\mathbf{V}(\hat{q})\rangle_{n}-\operatorname{Tr}_{n}[\langle\mathbf{V}^{\prime\prime}(\hat{q})\rangle_{n}\cdot\operatorname{Cov}(q)]/2,\text{ }(51)𝐕1\displaystyle\mathbf{V}_{1}=⟨𝐕′​(q^)⟩n,\displaystyle=\langle\mathbf{V}^{\prime}(\hat{q})\rangle_{n},(52)𝐕2\displaystyle\mathbf{V}_{2}=⟨𝐕′′​(q^)⟩n.\displaystyle=\langle\mathbf{V}^{\prime\prime}(\hat{q})\rangle_{n}.(53)

We have thus obtained thevariational thawed Gaussian Ehrenfest
dynamics, which is a generalization of Heller’s and Coalson and Karplus’s
variational thawed Gaussian wavepacket
dynamics[50,32]to nonadiabatic systems.

## IV.2Local harmonic thawed Gaussian Ehrenfest
dynamics

Evaluating expectation values⟨𝐕(j)​(q^)⟩n\langle\mathbf{V}^{(j)}(\hat{q})\rangle_{n},
needed in the variational TGED may be difficult in practical calculations with
non-polynomial potential energy surfaces. In the limit of smallℏ\hbar, it
pays off to approximate the potential energy by its local harmonic
(LH) approximation, a quadratic expansion about the centerqtq_{t}of the
wavepacket, as was done by Heller in the single-surface
setting.[30]Here, one simply replaces matrix coefficients𝐕j\mathbf{V}_{j}in Eq. (28) with the diabatic potential
energy matrix, its gradient, and Hessian at the wavepacket’s center:𝐕j=𝐕(j)​(qt)​for​j=0,1,2\mathbf{V}_{j}=\mathbf{V}^{(j)}(q_{t})\text{ \ \ for }j=0,1,2(54)

The mean-field potential energy operator (35) needed in the
electronic TDSE (33) then becomes⟨𝐕LH​(q^;ψ)⟩n=𝐕​(qt)+Trn⁡[𝐕′′​(qt)⋅Cov⁡(q)]/2.\langle\mathbf{V}_{\text{LH}}(\hat{q};\psi)\rangle_{n}=\mathbf{V}\left(q_{t}\right)+\operatorname{Tr}_{n}[\mathbf{V}^{\prime\prime}\left(q_{t}\right)\cdot\operatorname{Cov}(q)]/2.(55)

Although Eq. (54) together with the general TGED
Eqs. (33) and (38)-(44) describe the
local harmonic version of TGED completely, let us write the new equations of
motion for the electronic wavefunction and nuclear position and momentum
explicitly:i​ℏ​𝐜˙t\displaystyle i\hbar\dot{\mathbf{c}}_{t}=[⟨T​(p^)⟩n+⟨𝐕LH​(q^;ψ)⟩n]​𝐜t,\displaystyle=[\langle T(\hat{p})\rangle_{n}+\langle\mathbf{V}_{\text{LH}}(\hat{q};\psi)\rangle_{n}]\mathbf{c}_{t},(56)q˙t\displaystyle\dot{q}_{t}=m−1⋅pt,\displaystyle=m^{-1}\cdot p_{t},(57)p˙t\displaystyle\dot{p}_{t}=−Vn′​(qt).\displaystyle=-V_{n}^{\prime}(q_{t}).(58)

The width and phase of the nuclear wavepacket evolve according to the
equationsA˙t\displaystyle\dot{A}_{t}=−At⋅m−1⋅At−Vn′′​(qt),\displaystyle=-A_{t}\cdot m^{-1}\cdot A_{t}-V_{n}^{\prime\prime}(q_{t}),(59)γ˙t\displaystyle\dot{\gamma}_{t}=T​(pt)−Vn​(qt)+(i​ℏ/2)​Tr(m−1⋅At)\displaystyle=T(p_{t})-V_{n}(q_{t})+(i\hbar/2)\operatorname*{Tr}\left(m^{-1}\cdot A_{t}\right)(60)

in theA​γA\gammaparametrization and according to equationsQ˙t\displaystyle\dot{Q}_{t}=m−1⋅Pt,\displaystyle=m^{-1}\cdot P_{t},(61)P˙t\displaystyle\dot{P}_{t}=−Vn′′​(qt)⋅Qt,\displaystyle=-V_{n}^{\prime\prime}(q_{t})\cdot Q_{t},(62)S˙t\displaystyle\dot{S}_{t}=T​(pt)−Vn​(qt)\displaystyle=T(p_{t})-V_{n}(q_{t})(63)

in theQ​P​SQPSparametrization. This system of differential equations expresses
thelocal harmonic thawed Gaussian Ehrenfest dynamics, which is a
generalization of Heller’s original thawed Gaussian
approximation[30]to the setting with multiple electronic states.

## IV.3Global harmonic thawed Gaussian Ehrenfest
dynamics

A cruder, yet more efficient,harmonic thawed Gaussian Ehrenfest
dynamicsis obtained by replacing the molecular potential energy operator𝐕​(q^)\mathbf{V}(\hat{q})with its global harmonic approximation𝐕harm​(q^)=𝐕​(qr)+𝐕′​(qr)T⋅x^r+x^rT⋅𝐕′′​(qr)⋅x^r/2,\mathbf{V}_{\text{harm}}(\hat{q})=\mathbf{V}\left(q_{r}\right)+\mathbf{V}^{\prime}\left(q_{r}\right)^{T}\cdot\hat{x}_{r}+\hat{x}_{r}^{T}\cdot\mathbf{V}^{\prime\prime}\left(q_{r}\right)\cdot\hat{x}_{r}/2,(64)

wherex^r:=q^−qr\hat{x}_{r}:=\hat{q}-q_{r}is the displacement from a a fixed
reference positionqrq_{r}. This is equivalent to setting the coefficients of
the effective molecular potential (28) to𝐕0\displaystyle\mathbf{V}_{0}=𝐕harm​(qt),\displaystyle=\mathbf{V}_{\text{harm}}(q_{t}),(65)𝐕1\displaystyle\mathbf{V}_{1}=𝐕harm′​(qt)=𝐕′​(qr)+𝐕′′​(qr)⋅(qt−qr),\displaystyle=\mathbf{V}_{\text{harm}}^{\prime}(q_{t})=\mathbf{V}^{\prime}(q_{r})+\mathbf{V}^{\prime\prime}\left(q_{r}\right)\cdot(q_{t}-q_{r}),(66)𝐕2\displaystyle\mathbf{V}_{2}=𝐕harm′′​(qt)=𝐕′′​(qr).\displaystyle=\mathbf{V}_{\text{harm}}^{\prime\prime}(q_{t})=\mathbf{V}^{\prime\prime}(q_{r}).(67)

Harmonic approximation (64) to the molecular potential is an
example of the quadratic vibronic coupling
model,[59,60]widely used for
nonadiabatic simulations.

## IV.4Single-Hessian thawed Gaussian Ehrenfest
dynamics

To include some anharmonicity beyond the harmonic TGED but avoid the costly
evaluation of the Hessians needed in the local harmonic TGED, one can
generalize the single-Hessian thawed Gaussian wavepacket
dynamics[33,61,62]and obtain thesingle-Hessian thawed Gaussian Ehrenfest dynamics, where
the coefficients of the effective potential (28) are set to𝐕j\displaystyle\mathbf{V}_{j}=𝐕(j)​(qt)​for​j=0​and​1,\displaystyle=\mathbf{V}^{(j)}(q_{t})\text{ \ \ for }j=0\text{ and
}1,(68)𝐕2\displaystyle\mathbf{V}_{2}=𝐕′′​(qr).\displaystyle=\mathbf{V}^{\prime\prime}(q_{r}).(69)

The effective potential has the exact value and gradient but its Hessian
(curvature) is kept constant. Besides its efficiency, in the one-surface
setting the single-Hessian TGWD was shown to conserve both the symplectic
structure and effective
energy.[33,62]

## IV.5Local cubic variational TGED

To include effects beyond the local harmonic approximation, it is useful to
apply the variational TGED to a local cubic approximation for the potential
and obtain thelocal cubic variational thawed Gaussian Ehrenfest
dynamics, for which the coefficients of𝐕eff\mathbf{V}_{\text{eff}}are𝐕j\displaystyle\mathbf{V}_{j}=𝐕(j)​(qt)​for​j=0​and​2,\displaystyle=\mathbf{V}^{(j)}(q_{t})\text{ \ \ for }j=0\text{ and }2,(70)𝐕1,k\displaystyle\mathbf{V}_{1,k}=𝐕′(qt)k+12∑l,m=1D𝐕′′′(qt)k​l​mCov(q)l​m.\displaystyle=\mathbf{V}^{\prime}(q_{t})_{k}+\frac{1}{2}\sum_{l,m=1}^{D}\mathbf{V}^{\prime\prime\prime}(q_{t})_{klm}\operatorname{Cov}(q)_{lm}.(71)

In the single-surface setting, this approximation (called “extended semiclassical,” “symplectic
semiclassical,” or “local cubic
variational” TGWD),[63,55,58]has been shown to conserve the symplectic structure, effective energy, and can
qualitatively capture tunneling without requiring the expectation values of
the potential energy derivatives needed in the variational TGWD.

## IV.6Single quartic variational TGED

The limitation of the local cubic variational TGED is that the local cubic
potential is necessarily unbounded from below. To avoid the resulting
numerical issues but keep approximately the same computational cost, the
single-quartic variational TGWD was proposed in the single-surface
setting.[34]In this method, the variational principle is
applied to the single-quartic approximation of the potential, which has the
exact local derivative up to the third order but keeps a single constant
positive definite fourth derivative tensor. Remarkably, like the
single-Hessian variant, this method is symplectic and conserves the effective
energy, neither of which is true for the local harmonic or the much more
expensive local quartic approximations. Generalizing the results to the
nonadiabatic setting, the coefficients of the effective potential of thesingle-quartic variational TGEDare𝐕2,i​j\displaystyle\mathbf{V}_{2,}{}_{ij}=𝐕′′​(qt)i​j+∑k,l=1D𝐕(4)​(qr)i​j​k​l​Σk​l/2,\displaystyle=\mathbf{V}^{\prime\prime}(q_{t})_{ij}+\sum_{k,l=1}^{D}\mathbf{V}^{(4)}(q_{r})_{ijkl}\Sigma_{kl}/2,(72)𝐕1,i\displaystyle\mathbf{V}_{1,i}=𝐕′​(qt)i+∑j,k=1D𝐕′′′​(qt)i​j​k​Σj​k/2,\displaystyle=\mathbf{V}^{\prime}(q_{t})_{i}+\sum_{j,k=1}^{D}\mathbf{V}^{\prime\prime\prime}(q_{t})_{ijk}\Sigma_{jk}/2,(73)𝐕0\displaystyle\mathbf{V}_{0}=𝐕​(qt)−∑i,j,k,l=1D𝐕(4)​(qr)i​j​k​l​Σi​j​Σk​l/8,\displaystyle=\mathbf{V}(q_{t})-\sum_{i,j,k,l=1}^{D}\mathbf{V}^{(4)}(q_{r})_{ijkl}\Sigma_{ij}\Sigma_{kl}/8,(74)

whereΣ≡Cov⁡(q)\Sigma\equiv\operatorname{Cov}(q)is the shorthand notation for the
position covariance matrix (36). Because only a single fourth
derivative is needed, if this derivative is evaluated by finite differences,
the increase in cost over the local cubic variational TGED would be negligible
in typical simulations, where the number of time steps is much larger than the
number of degrees of freedom. Because the single-quartic potential can always
be bounded from below, the single-quartic variational TGWD appears to be the
method of choice if one wants to improve accuracy beyond the local harmonic
TGED but avoid the cost of the fully variational TGED.

## VSpecial limits of TGED

Let us explore various limits of the thawed Gaussian Ehrenfest dynamics (see
Fig.3). Note that in Secs.V.1,V.2, andV.4,cs​(t)c_{s}(t)denotes the component of the electronic vector𝐜​(t)\mathbf{c}(t)in thessth
electronic state; the timettis therefore not in the subscript (as in𝐜t\mathbf{c}_{t}), but in the argument. Comparison of the TGED with three of
its limits (Ehrenfest dynamics, TGWD, and classical dynamics) in a simple
system, where TGED is exact, was shown in Fig.1.Figure 3:Relation of thawed Gaussian Ehrenfest dynamics to exact
molecular quantum dynamics and to other approximations.

## V.1TGED with constant electronic
populations

If the electronic states are not coupled,𝐕​(q)\mathbf{V}(q)is a diagonal matrix
[Vr​s​(q)=0V_{rs}(q)=0forr≠sr\neq s], the electronic phase on each surface evolves
independently, the population of each electronic state remains constant, and
the mean-field potential for nuclear motion is determined by the initial
populations. Equations (24)-(25) reduce toi​ℏ​ψ˙\displaystyle i\hbar\dot{\psi}=[T​(p^)+∑s=1SVs​s​(q^)​|cs​(t=0)|2]​ψ,\displaystyle=[T(\hat{p})+\sum_{s=1}^{S}V_{ss}(\hat{q})|c_{s}(t=0)|^{2}]\psi,(75)i​ℏ​c˙s\displaystyle i\hbar\dot{c}_{s}=[⟨T​(p^)⟩n+⟨Vs​s​(q^)⟩n]​cs,s=1,…,S\displaystyle=[\langle T(\hat{p})\rangle_{n}+\langle V_{ss}(\hat{q})\rangle_{n}]c_{s},~~~s=1,\ldots,S(76)

The nuclear wavepacket still feels the mean-field potential energy, but the
weights of all surfaces remain unchanged. [To derive
Eqs. (75) and (76), we did not
have to assume the nuclear wavepacket to be Gaussian.]

## V.2Thawed Gaussian wavepacket dynamics

If the electronic states are uncoupled, and, in addition, the electrons are
initially in a single statess[cr​(0)=δr​sc_{r}(0)=\delta_{rs}], the preceding
equations further reduce toi​ℏ​ψ˙\displaystyle i\hbar\dot{\psi}=[T​(p^)+Vs​s​(q^)]​ψ,\displaystyle=[T(\hat{p})+V_{ss}(\hat{q})]\psi,(77)i​ℏ​c˙s\displaystyle i\hbar\dot{c}_{s}=[⟨T​(p^)⟩n+⟨Vs​s​(q^)⟩n]​cs=E​cs.\displaystyle=[\langle T(\hat{p})\rangle_{n}+\langle V_{ss}(\hat{q})\rangle_{n}]c_{s}=Ec_{s}.(78)

Thereforecs​(t)=exp⁡(−i​E​t/ℏ)c_{s}(t)=\exp(-iEt/\hbar), and the cancellation between the
electronic coefficientcs​(t)c_{s}(t)and the prefactora​(t)=exp⁡(i​E​t/ℏ)a(t)=\exp(iEt/\hbar)reduces the molecular state toΨ​(t)=a​(t)​ψ​(t)​cs​(t)​|s⟩=ψ​(t)​|s⟩.\Psi(t)=a(t)\psi(t)c_{s}(t)|s\rangle=\psi(t)|s\rangle.(79)

In other words, dynamics reduces to Born-Oppenheimer nuclear dynamics on a
single surfacess. Moreover, because the nuclear wavepacketψ​(t)\psi(t)in TGED
is Gaussian, one obtains the thawed Gaussian wavepacket dynamics. Depending on
the choice of the molecular effective potential used in TGED, one obtains the
corresponding member of the TGWD family, such as the variational, local
harmonic, single-Hessian, global harmonic, local cubic variational, or the
single quartic variational TGWD.[34]

## V.3Ehrenfest dynamics

The classical limit for nuclei is achieved by letting the effective Planck
constant approach zero,ℏ→0\hbar\rightarrow 0. In this limit, the position and
momentum covariances [Eqs. (36) and (37)], which are
proportional toℏ\hbar, vanish, and as a result, the contributions to𝐕var,j\mathbf{V}_{\text{var},j},⟨T​(p^)⟩n\langle T(\hat{p})\rangle_{n}, and⟨𝐕(j)​(q^)⟩n\langle\mathbf{V}^{(j)}(\hat{q})\mathbf{\rangle}_{n}from the finite width
of the wavepacket become negligible in Eqs. (51)–(53) and in Eqs. (34) and (35).
Because the wavepacket becomes increasingly localized, the classical limit can
be accomplished formally by using alocal linear (LL) approximationfor
the potential and kinetic energies:𝐕​(q^)\displaystyle\mathbf{V}(\hat{q})≈𝐕LL​(q^)=𝐕​(qt)+𝐕′​(qt)T⋅(q^−qt),\displaystyle\approx\mathbf{V}_{\text{LL}}(\hat{q})=\mathbf{V}\left(q_{t}\right)+\mathbf{V}^{\prime}\left(q_{t}\right)^{T}\cdot(\hat{q}-q_{t}),(80)T​(p^)\displaystyle T(\hat{p})≈TLL​(p^)=T​(pt)+T′​(pt)T⋅(p^−pt).\displaystyle\approx T_{\text{LL}}(\hat{p})=T\left(p_{t}\right)+T^{\prime}\left(p_{t}\right)^{T}\cdot(\hat{p}-p_{t}).(81)

With this approximation, the effective potential coefficients of the
variational TGED and the expectation values of kinetic and potential energies
become𝐕var,2\displaystyle\mathbf{V}_{\text{var},2}→ℏ→0​𝐕LL,2=0,\displaystyle\overset{\hbar\rightarrow 0}{\rightarrow}\mathbf{V}_{\text{LL},2}=0,(82)𝐕var,​1\displaystyle\mathbf{V}_{\text{var,}1}→ℏ→0​𝐕LL,1=𝐕′​(qt),\displaystyle\overset{\hbar\rightarrow 0}{\rightarrow}\mathbf{V}_{\text{LL},1}=\mathbf{V}^{\prime}(q_{t}),(83)𝐕var,​0\displaystyle\mathbf{V}_{\text{var,}0}→ℏ→0​𝐕LL,​0=𝐕​(qt),\displaystyle\overset{\hbar\rightarrow 0}{\rightarrow}\mathbf{V}_{\text{LL,}0}=\mathbf{V}(q_{t}),(84)⟨T​(p^)⟩n\displaystyle\langle T(\hat{p})\rangle_{n}→ℏ→0​⟨TLL​(p^)⟩n=T​(pt),\displaystyle\overset{\hbar\rightarrow 0}{\rightarrow}\langle T_{\text{LL}}(\hat{p})\rangle_{n}=T(p_{t}),(85)⟨𝐕var​(q^)⟩n\displaystyle\langle\mathbf{V}_{\text{var}}(\hat{q})\rangle_{n}→ℏ→0​⟨𝐕LL​(q^)⟩n=𝐕​(qt).\displaystyle\overset{\hbar\rightarrow 0}{\rightarrow}\langle\mathbf{V}_{\text{LL}}(\hat{q})\rangle_{n}=\mathbf{V}(q_{t}).(86)

The electronic TDSE (33) and Eqs. (38) and
(39) for nuclear positions and momenta reduce to the equations of
standard mixed quantum-classicalEhrenfest dynamics:i​ℏ​𝐜˙t\displaystyle i\hbar\dot{\mathbf{c}}_{t}=[T​(pt)+𝐕​(qt)]​𝐜t,\displaystyle=[T(p_{t})+\mathbf{V}(q_{t})]\mathbf{c}_{t},(87)q˙t\displaystyle\dot{q}_{t}=m−1⋅pt,\displaystyle=m^{-1}\cdot p_{t},(88)p˙t\displaystyle\dot{p}_{t}=−Vn′​(qt).\displaystyle=-V_{n}^{\prime}(q_{t}).(89)

As for the evolution of the other parameters,A˙t\displaystyle\dot{A}_{t}=Q˙t=P˙t=0,\displaystyle=\dot{Q}_{t}=\dot{P}_{t}=0,(90)γ˙t\displaystyle\dot{\gamma}_{t}=S˙t=T​(pt)−Vn​(qt).\displaystyle=\dot{S}_{t}=T(p_{t})-V_{n}(q_{t}).(91)

The Gaussian wavepacket becomes “frozen” because its width matrix remains constant (At=A0A_{t}=A_{0}orQt=Q0Q_{t}=Q_{0}andPt=P0P_{t}=P_{0}). Moreover, the increment ofγt\gamma_{t}along the
trajectory is equal to the increment of Ehrenfest-averaged classical actionStS_{t}. Although the nuclear actionStS_{t}is usually ignored in Ehrenfest
dynamics, propagatingStS_{t}is important if one is interested in the
time-dependent overall phase of the wavepacket needed, e.g., in the
calculations of spectra. The conserved total energy isE=𝐜t†​[T​(pt)+𝐕​(qt)]​𝐜t=T​(pt)+Vn​(qt),E=\mathbf{c}_{t}^{{\dagger}}[T(p_{t})+\mathbf{V}(q_{t})]\mathbf{c}_{t}=T(p_{t})+V_{n}(q_{t}),(92)

which also reflects that the wavepacket width is ignored in the classical limit.

## V.4Classical nuclear dynamics

By taking the classical limit of TGWD or the single-surface limit (on surfacess) of Ehrenfest dynamics, one obtains the single-surface classical nuclear
dynamicscs​(t)\displaystyle c_{s}(t)=exp⁡(−i​E​t/ℏ),\displaystyle=\exp(-iEt/\hbar),(93)q˙t\displaystyle\dot{q}_{t}=m−1⋅pt,\displaystyle=m^{-1}\cdot p_{t},(94)p˙t\displaystyle\dot{p}_{t}=−Vs​s′​(qt),\displaystyle=-V_{ss}^{\prime}(q_{t}),(95)A˙t\displaystyle\dot{A}_{t}=Q˙t=P˙t=0,\displaystyle=\dot{Q}_{t}=\dot{P}_{t}=0,(96)γ˙t\displaystyle\dot{\gamma}_{t}=S˙t=T​(pt)−Vs​s​(qt),\displaystyle=\dot{S}_{t}=T(p_{t})-V_{ss}(q_{t}),(97)

whereE=T​(pt)+Vs​s​(qt)E=T(p_{t})+V_{ss}(q_{t})is the conserved classical energy on thessth surface.

## V.5Independent electronic dynamics and free-particle nuclear thawed
Gaussian wavepacket dynamics

Now let us consider the limit in which the potential energy operator does not
depend on nuclear coordinates:𝐕​(q^)≈𝐕=const.\mathbf{V}(\hat{q})\approx\mathbf{V}=\operatorname{const}.(98)

The electronic TDSE (33) can be solved exactly, giving𝐜t=exp⁡{−i​t​[⟨T​(p^)⟩n,t=0​𝟏+𝐕]/ℏ}​𝐜0.\mathbf{c}_{t}=\exp\{-it[\langle T(\hat{p})\rangle_{n,t=0}\mathbf{1}+\mathbf{V}]/\hbar\}\mathbf{c}_{0}.(99)

The mean-field nuclear potential (29) isVn=𝐜t†​𝐕𝐜t=𝐜0†​𝐕𝐜0=Vn,t=0V_{n}=\mathbf{c}_{t}^{{\dagger}}\mathbf{Vc}_{t}=\mathbf{c}_{0}^{{\dagger}}\mathbf{Vc}_{0}=V_{n,t=0}(100)

since the exponential in𝐜t\mathbf{c}_{t}commutes with𝐕\mathbf{V}.
Equations for Gaussian parameters have exact solutions[34]qt\displaystyle q_{t}=q0+t​m−1⋅p0,\displaystyle=q_{0}+tm^{-1}\cdot p_{0},(101)pt\displaystyle p_{t}=p0=const,\displaystyle=p_{0}=\operatorname{const},(102)At\displaystyle A_{t}=A0⋅(IdD+t​m−1⋅A0)−1,\displaystyle=A_{0}\cdot\left(\operatorname{Id}_{D}+tm^{-1}\cdot A_{0}\right)^{-1},(103)γt\displaystyle\gamma_{t}=γ0+t​[T​(p0)−Vn,t=0]\displaystyle=\gamma_{0}+t[T(p_{0})-V_{n,t=0}]+(i​ℏ/2)​ln​det(IdD+t​m−1⋅A0),\displaystyle~~~+(i\hbar/2)\ln\det\left(\operatorname{Id}_{D}+tm^{-1}\cdot A_{0}\right),(104)Qt\displaystyle Q_{t}=Q0+t​m−1⋅P0,\displaystyle=Q_{0}+tm^{-1}\cdot P_{0},(105)Pt\displaystyle P_{t}=P0=const,\displaystyle=P_{0}=\operatorname{const},(106)St\displaystyle S_{t}=S0+t​[T​(p0)−Vn,t=0].\displaystyle=S_{0}+t[T(p_{0})-V_{n,t=0}].(107)

Equations for the position, momentum, and width matrix (AtA_{t}orQtQ_{t}andPtP_{t}) are the same as for a Gaussian free particle (see
Sec.VI.1on kinetic propagation), but the equation forγt\gamma_{t}(orStS_{t}) contains a potential termVnV_{n}.

## VIGeometric integrators

Not all numerical integration schemes preserve the geometric properties of the
exact or approximate solution of the molecular Schrödinger
equation.[64]There is, however, a general strategy
to preserve energy conservation approximately and all other properties
exactly. If the Hamiltonianℋ=𝒯+𝒱\mathcal{H}=\mathcal{T}+\mathcal{V}is separable
into two terms,𝒯\mathcal{T}and𝒱\mathcal{V}, the propagation with each of
which can be performed exactly, one can obtain structure-preserving
integrators of arbitrary even order of accuracy by symmetrically composing the
Strang splitting of the evolution operator.[64]Such
integrators were obtained for the exact quantum solution of the nonadiabatic
Schrödinger equation in
Refs.5,6, for the
representation-free Ehrenfest dynamics in
Ref.65, and for the generalized TGWD in
Ref.34. Using the same procedure, one can obtain
geometric integrators of arbitrary even order of accuracy for the TGED. In
particular, we only need to find the exact solutions of the ordinary
differential equations for the kinetic and potential propagations of the
Gaussian’s parametersqtq_{t},pt,Atp_{t},A_{t},γt\gamma_{t},QtQ_{t},PtP_{t},
andStS_{t}and for the electronic wavefunction𝐜t\mathbf{c}_{t}. We do so next.

## VI.1Kinetic propagation

During the kinetic propagation step, the effective Hamiltonian𝐇^eff=T​(p^)​𝟏\mathbf{\hat{H}}_{\text{eff}}=T(\hat{p})\mathbf{1}contains only the kinetic energy. As a
result, the electronic TDSE becomesi​ℏ​𝐜˙t=T​(ψt)​𝐜t,i\hbar\mathbf{\dot{c}}_{t}=T(\psi_{t})\mathbf{c}_{t},(108)

where the nuclear kinetic energyT​(ψt):=⟨T​(p^)⟩nT(\psi_{t}):=\langle T(\hat{p})\rangle_{n}is given by Eq. (34), while the equations of motion for the
nuclear wavepacket reduce toq˙t\displaystyle\dot{q}_{t}=m−1⋅pt,\displaystyle=m^{-1}\cdot p_{t},(109)p˙t\displaystyle\dot{p}_{t}=0,\displaystyle=0,(110)A˙t\displaystyle\dot{A}_{t}=−At⋅m−1⋅At,\displaystyle=-A_{t}\cdot m^{-1}\cdot A_{t}\,,(111)γ˙t\displaystyle\dot{\gamma}_{t}=T​(pt)+(i​ℏ/2)​Trn⁡(m−1⋅At),\displaystyle=T(p_{t})+(i\hbar/2)\operatorname{Tr}_{n}(m^{-1}\cdot A_{t}),(112)Q˙t\displaystyle\dot{Q}_{t}=m−1⋅Pt,\displaystyle=m^{-1}\cdot P_{t},(113)P˙t\displaystyle\dot{P}_{t}=0,\displaystyle=0,(114)S˙t\displaystyle\dot{S}_{t}=T​(pt).\displaystyle=T(p_{t}).(115)

To solve the electronic TDSE analytically, we note that not only the momentum
covariance (37) but also the kinetic energy (34)
remains constant since neitherptp_{t}norPtP_{t}evolves during the kinetic
propagation. Hence the propagation of the electronic wavefunction is a simple
multiplication with a scalar exponential:𝐜t=exp⁡[−i​t​T​(ψ0)/ℏ]​𝐜0.\mathbf{c}_{t}=\exp[-itT(\psi_{0})/\hbar]\mathbf{c}_{0}.(116)

Analytical solution for the Gaussian parameters is the same as in the
single-surface TGWD:[34]qt\displaystyle q_{t}=q0+t​m−1⋅p0,\displaystyle=q_{0}+tm^{-1}\cdot p_{0},(117)pt\displaystyle p_{t}=p0,\displaystyle=p_{0},(118)At\displaystyle A_{t}=(A0−1+t​m−1)−1=A0⋅(IdD+t​m−1⋅A0)−1\displaystyle=\left(A_{0}^{-1}+tm^{-1}\right)^{-1}=A_{0}\cdot\left(\operatorname{Id}_{D}+tm^{-1}\cdot A_{0}\right)^{-1}=(IdD+t​A0⋅m−1)−1⋅A0,\displaystyle=\left(\operatorname{Id}_{D}+tA_{0}\cdot m^{-1}\right)^{-1}\cdot A_{0},(119)γt\displaystyle\gamma_{t}=γ0+t​T​(p0)+i​ℏ2​ln​det(IdD+t​m−1⋅A0),\displaystyle=\gamma_{0}+tT(p_{0})+\frac{i\hbar}{2}\ln\det\left(\operatorname{Id}_{D}+tm^{-1}\cdot A_{0}\right),(120)Qt\displaystyle Q_{t}=Q0+t​m−1⋅P0,\displaystyle=Q_{0}+tm^{-1}\cdot P_{0},(121)Pt\displaystyle P_{t}=P0,\displaystyle=P_{0},(122)St\displaystyle S_{t}=S0+t​T​(p0).\displaystyle=S_{0}+tT(p_{0}).(123)

## VI.2Potential propagation

During the potential propagation step, the effective Hamiltonian𝐇^eff=𝐕eff​(q^;ψ)\mathbf{\hat{H}}_{\text{eff}}=\mathbf{V}_{\text{eff}}(\hat{q};\psi)contains
only the potential energy. Therefore, the electronic TDSE becomesi​ℏ​𝐜˙t=𝐕eff​(ψt)​𝐜t,i\hbar\mathbf{\dot{c}}_{t}=\mathbf{V}_{\text{eff}}(\psi_{t})\mathbf{c}_{t},(124)

where the electronic potential energy matrix𝐕eff​(ψ):=⟨𝐕eff​(q^;ψ)⟩n\mathbf{V}_{\text{eff}}(\psi):=\langle\mathbf{V}_{\text{eff}}(\hat{q};\psi)\rangle_{n}is given by
Eq. (35), while the nuclear Gaussian wavepacket evolves according
to the equationsq˙t\displaystyle\dot{q}_{t}=0\displaystyle=0(125)p˙t\displaystyle\dot{p}_{t}=−Vn,1,\displaystyle=-V_{n,1},(126)A˙t\displaystyle\dot{A}_{t}=−Vn,2,\displaystyle=-V_{n,2}\,,(127)γ˙t\displaystyle\dot{\gamma}_{t}=−Vn,0,\displaystyle=-V_{n,0},(128)Q˙t\displaystyle\dot{Q}_{t}=0,\displaystyle=0,(129)P˙t\displaystyle\dot{P}_{t}=−Vn,2⋅Qt,\displaystyle=-V_{n,2}\cdot Q_{t},(130)S˙t\displaystyle\dot{S}_{t}=−Vn,0.\displaystyle=-V_{n,0}.(131)

The electronic equation is easy to solve if𝐕j\mathbf{V}_{j}does not change
during the potential propagation. Since𝐕eff\mathbf{V}_{\text{eff}}is assumed
to depend only on the nuclear and not on the electronic state, we only need to
worry about the dependence of𝐕j\mathbf{V}_{j}on the Gaussian wavepacket’s
parameters. As we now show,𝐕j\mathbf{V}_{j}will not depend on time as long
as𝐕j\mathbf{V}_{j}depends only on parametersqtq_{t}andQtQ_{t}(orqtq_{t}andIm⁡At\operatorname{Im}A_{t}). Note that this assumption holds for all
discussed methods: e.g.,𝐕LH,​j\mathbf{V}_{\text{LH,}j}depends only onqtq_{t}and𝐕var,​j\mathbf{V}_{\text{var,}j}depends only onqtq_{t}andQtQ_{t}orIm⁡At\operatorname{Im}A_{t}(which appear in the coordinate-space density needed
in evaluating expectation values). As neitherqtq_{t}norQtQ_{t}changes
during the potential propagation,𝐕j\mathbf{V}_{j}and𝐕eff\mathbf{V}_{\text{eff}}also remain constant. The electronic wavefunction is thus
obtained by multiplying the initial state with a matrix exponential:𝐜t=exp⁡[−i​t​𝐕eff​(ψ0)/ℏ]​𝐜0.\mathbf{c}_{t}=\exp[-it\mathbf{V}_{\text{eff}}(\psi_{0})/\hbar]\mathbf{c}_{0}.(132)

Although𝐕j\mathbf{V}_{j}remains constant during the potential propagation,
the nuclear effective potential energy coefficientsVn,jV_{n,j}from
Eq. (31) change due to their dependence on the electronic
wavefunction𝐜t\mathbf{c}_{t}, which evolves according to
Eq. (132). The evolved Gaussian’s parameters can be written
asqt\displaystyle q_{t}=q0,\displaystyle=q_{0},(133)pt\displaystyle p_{t}=p0−t​V¯n,1,\displaystyle=p_{0}-t\bar{V}_{n,1},(134)At\displaystyle A_{t}=A0−t​V¯n,2,\displaystyle=A_{0}-t\bar{V}_{n,2},(135)γt\displaystyle\gamma_{t}=γ0−t​V¯n,0,\displaystyle=\gamma_{0}-t\bar{V}_{n,0},(136)Qt\displaystyle Q_{t}=Q0,\displaystyle=Q_{0},(137)Pt\displaystyle P_{t}=P0−t​V¯n,2⋅Q0,\displaystyle=P_{0}-t\bar{V}_{n,2}\cdot Q_{0},(138)St\displaystyle S_{t}=S0−t​V¯n,0,\displaystyle=S_{0}-t\bar{V}_{n,0},(139)

but we still need to evaluate the time averagesV¯n,j:=1t​∫0tVn,j​(t′)​𝑑t′=1t​∫0t𝐜t′†​𝐕j​𝐜t′​𝑑t′\bar{V}_{n,j}:=\frac{1}{t}\int_{0}^{t}V_{n,j}(t^{\prime})dt^{\prime}=\frac{1}{t}\int_{0}^{t}\mathbf{c}_{t^{\prime}}^{{\dagger}}\mathbf{V}_{j}\mathbf{c}_{t^{\prime}}dt^{\prime}(140)

of the expectation values of𝐕j\mathbf{V}_{j}over an evolving electronic
state𝐜t\mathbf{c}_{t}forj=0,1,2j=0,1,2. All of the time averagesV¯n,j\bar{V}_{n,j}require evaluating the integralI=∫0t𝐜0†​exp⁡(i​t′​𝐕eff/ℏ)​𝐁​exp⁡(−i​t′​𝐕eff/ℏ)​𝐜0​𝑑t′,I=\int_{0}^{t}\mathbf{c}_{0}^{{\dagger}}\exp(it^{\prime}\mathbf{V}_{\text{eff}}/\hbar)\mathbf{B}\exp(-it^{\prime}\mathbf{V}_{\text{eff}}/\hbar)\mathbf{c}_{0}dt^{\prime},(141)

where theS×SS\times Smatrix𝐁\mathbf{B}is𝐕0\mathbf{V}_{0}(forV¯n,0\bar{V}_{n,0}) or one of theDDcomponents of vector𝐕1\mathbf{V}_{1}(forV¯n,1\bar{V}_{n,1}), or one of theD×DD\times Dmatrix elements of𝐕2\mathbf{V}_{2}(forV¯n,2\bar{V}_{n,2}). Using a formula for a derivative of an
exponential with respect to a parameter,[66]one can
recognize thatI=d​f​(λ)/d​λ|λ=0,I=\left.df\left(\lambda\right)/d\lambda\right|_{\lambda=0},(142)

wheref​(λ)f\left(\lambda\right)is the functionf​(λ):=𝐜0†​exp⁡{t​[i​𝐕eff​(ψ0)/ℏ+λ​𝐁]}​𝐜t.f\left(\lambda\right):=\mathbf{c}_{0}^{{\dagger}}\exp\{t[i\mathbf{V}_{\text{eff}}(\psi_{0})\mathbf{/\hbar}+\lambda\mathbf{B]\}c}_{t}.(143)

Equation (142) is much more convenient for evaluatingIIthan is the integral in Eq. (141), because it is easier to
evaluate a derivative by finite difference than an integral. E.g., one can
approximate the result by considering small yet finiteλ\lambdain the
expressionI=limλ→0[f​(λ)−1]/λ.I=\lim_{\lambda\rightarrow 0}[f(\lambda)-1]/\lambda.(144)

However, there exist much more accurate, higher-order numerical methods to
estimate the derivative of the functionf​(λ)f(\lambda), which have been used for
analogous potential propagation of standard Ehrenfest
dynamics.[67]

## VIIExactness of various approximations

Let us discuss the conditions, under which various approximations become exact.

## VII.1Time-dependent Hartree approximation

The TDH approximation [Eqs. (4) and (7)–(11)] is exact if electronic and nuclear dynamics
are independent, which happens when molecular Hamiltonianℋ\mathcal{H}is a
sumℋ=H^nu⊗1^el+1^nu⊗H^el=H^nu+H^el\mathcal{H}=\hat{H}_{\text{nu}}\otimes\hat{1}_{\text{el}}+\hat{1}_{\text{nu}}\otimes\hat{H}_{\text{el}}=\hat{H}_{\text{nu}}+\hat{H}_{\text{el}}(145)

of noninteracting nuclear and electronic terms.

Proof. The TDH equations (7)–(9), which rely on the mean-field HamiltoniansH^n\displaystyle\hat{H}_{n}:=⟨φ|ℋ|φ⟩=H^nu+⟨H^el⟩e,\displaystyle:=\langle\varphi|\mathcal{H}|\varphi\rangle=\hat{H}_{\text{nu}}+\langle\hat{H}_{\text{el}}\rangle_{e},(146)H^e\displaystyle\hat{H}_{e}:=⟨ψ|ℋ|ψ⟩=⟨H^nu⟩n+H^el,\displaystyle:=\langle\psi|\mathcal{H}|\psi\rangle=\langle\hat{H}_{\text{nu}}\rangle_{n}+\hat{H}_{\text{el}},(147)

givei​ℏ​Ψ˙\displaystyle i\hbar\dot{\Psi}=i​ℏ​[a​(ψ˙​φ+ψ​φ˙)+a˙​ψ​φ]\displaystyle=i\hbar[a(\dot{\psi}\varphi+\psi\dot{\varphi})+\dot{a}\psi\varphi]=a​[(H^n+H^e)−E]​ψ​φ\displaystyle=a[(\hat{H}_{n}+\hat{H}_{e})-E]\psi\varphi=[(H^nu+H^el)+⟨H^nu+H^el⟩Ψ−E]​Ψ\displaystyle=[(\hat{H}_{\text{nu}}+\hat{H}_{\text{el}})+\langle\hat{H}_{\text{nu}}+\hat{H}_{\text{el}}\rangle_{\Psi}-E]\Psi=(ℋ+E−E)​Ψ=ℋ​Ψ,\displaystyle=(\mathcal{H}+E-E)\Psi=\mathcal{H}\Psi,(148)

and therefore solve the molecular TDSE exactly.

Remark. Contrary to common intuition, whenℋ\mathcal{H}is expressed
in a diabatic basis as𝐇​(q^,p^)\mathbf{H}(\hat{q},\hat{p}), the validity of the
TDH approximation, requiring form (145) ofℋ\mathcal{H},allows𝐇​(q^,p^)\mathbf{H}(\hat{q},\hat{p})to contain constant couplings
between different electronic states. Also surprisingly, even if𝐇​(q^,p^)\mathbf{H}(\hat{q},\hat{p})is a diagonal matrix and contains no offdiagonal coupling
terms, the form (145)does not allownuclear potential
energy surfaces in the diagonal terms of𝐇​(q^,p^)\mathbf{H}(\hat{q},\hat{p})to
differ more than by a constant vertical shift. Both statements become clear by
expressing Eq. (145) in diabatic basis:𝐇​(q^,p^)=Hnu​(q^,p^)​𝟏+1^​𝐇el.\mathbf{H}(\hat{q},\hat{p})=H_{\text{nu}}(\hat{q},\hat{p})\mathbf{1}+\hat{1}\mathbf{H}_{\text{el}}.(149)

In summary, the TDH approximation is exact if all potential energy surfaces
are only vertically displaced and the couplings between these surfaces are constant.

## VII.2Thawed Gaussian wavepacket dynamics

The single-surface, purely nuclear TGWD from Sec.V.2is
exact[30,2,47,34]if
the nuclear potential is a quadratic functionVn​(q)=v0+v1T⋅xr+xrT⋅v2⋅xr/2V_{n}(q)=v_{0}+v_{1}^{T}\cdot x_{r}+x_{r}^{T}\cdot v_{2}\cdot x_{r}/2(150)

of nuclear coordinates.[34,47]As in
Sec.IV.3,xr:=q−qrx_{r}:=q-q_{r}is the displacement from a reference
positionqrq_{r}, andvj:=V(j)​(qr)v_{j}:=V^{(j)}(q_{r})is thejjth derivative of the
potential atqrq_{r}.

## VII.3Thawed Gaussian Ehrenfest dynamics

The TGED is exact if the molecular Hamiltonianℋ\mathcal{H}has the form of
Eq. (145), whereH^nu=T​(p^)+Vnu​(q^),\hat{H}_{\text{nu}}=T(\hat{p})+V_{\text{nu}}(\hat{q}),(151)

andT​(p)T(p)andVnu​(q)V_{\text{nu}}(q)are at most quadratic functions. In diabatic
representation, this means that the potential energy surfaces are vertically
displaced harmonic potentials and the couplings between the surfaces are constant.

Proof. In Sec.VII.1, we already showed that the
TDH was exact for any Hamiltonianℋ\mathcal{H}of the form of
Eq. (145). It remains to show that the Gaussian wavepacket
dynamics solves exactly the nuclear equation of the TDH approximation. The
condition onT​(p)T(p)is satisfied because we assume a standard, quadratic
kinetic energy (3). If, in addition,Vnu​(q)V_{\text{nu}}(q)is at most
quadratic, i.e., of the form of the right-hand side of
Eq. (150), then the mean-field potentialVn​(q)V_{n}(q)will
retain the same form, except that the constant coefficientv0v_{0}will be
replaced withv0+Eelv_{0}+E_{\text{el}}, which is independent of time because⟨H^el⟩e=𝐜t†​𝐇el​𝐜t=𝐜0†​𝐇el​𝐜0=Eel\langle\hat{H}_{\text{el}}\rangle_{e}=\mathbf{c}_{t}^{{\dagger}}\mathbf{H}_{\text{el}}\mathbf{c}_{t}=\mathbf{c}_{0}^{{\dagger}}\mathbf{H}_{\text{el}}\mathbf{c}_{0}=E_{\text{el}}

is the conserved electronic energy. Here, we used the fact that the electronic
and nuclear Hamiltonians commute forℋ\mathcal{H}of Eq. (145).
Because the mean-field nuclear potentialVn​(q^)=Eel+Vnu​(q^)V_{n}(\hat{q})=E_{\text{el}}+V_{\text{nu}}(\hat{q})(152)

is quadratic of the form (150), by
Sec.VII.2the corresponding nuclear Gaussian wavepacket
dynamics is exact.

## VII.4Ehrenfest dynamics

Under the conditions of exactness of the TGED from
Sec.VII.3, the nuclear positions and momenta satisfy
Eqs. (38) and (39) withVn,1=Vn′​(qt)V_{n,1}=V_{n}^{\prime}(q_{t}), which are already equivalent to the corresponding
Eqs. (88) and (89) of Ehrenfest
dynamics. In the limitℏ→0\hbar\rightarrow 0(for nuclei only!) used in deriving
the Ehrenfest dynamics from a general TGED in Sec.V.3,
both position and momentum widths of the wavepacket vanish and, as a
consequence, the expectation values of kinetic and potential energies converge
to their classical valuesTn​(pt)T_{n}(p_{t})andVn​(qt)V_{n}(q_{t})at the center of
the wavepacket [see Eqs. (85)–(86)].

For nonzeroℏ\hbar, the equalities⟨Tn​(p^)⟩n=T​(pt)​and​⟨Vn​(q^)⟩n=Vn​(qt)\langle T_{n}(\hat{p})\rangle_{n}=T(p_{t})\text{ \ \ and \ \ }\langle V_{n}(\hat{q})\rangle_{n}=V_{n}(q_{t})(153)

will be guaranteed only if both kinetic and potential energies are linear
(rather than quadratic) functions of momenta and positions. In other words,
the local linear approximation used for deriving the Ehrenfest dynamics in
Sec.V.3must be replaced with a global linear kinetic
(this is unusual) and potential energies:Tn​(p)\displaystyle T_{n}(p)=t0+t1T⋅p,\displaystyle=t_{0}+t_{1}^{T}\cdot p,(154)Vn​(q)\displaystyle V_{n}(q)=v0+v1T⋅(q−qr).\displaystyle=v_{0}+v_{1}^{T}\cdot(q-q_{r}).(155)

Of course, these give rather trivial equations of motionq˙t=t1​and​p˙t=−v1\dot{q}_{t}=t_{1}\text{ \ \ and \ \ }\dot{p}_{t}=-v_{1}(156)

with analytical solutionsqt\displaystyle q_{t}=q0+t​t1,\displaystyle=q_{0}+t\,t_{1},(157)pt\displaystyle p_{t}=p0−t​v1.\displaystyle=p_{0}-t\,v_{1}.(158)

For such a Hamiltonian, the Ehrenfest evolution of even the electronic
wavefunction (87) is exact since it is equivalent to the
electronic TDSE (33) in the TGED.

## VIIIConclusion

In conclusion, we have described the single-trajectory thawed Gaussian
Ehrenfest dynamics, which combines the strengths of mixed quantum–classical
Ehrenfest dynamics and semiclassical Gaussian wavepacket dynamics. The method
captures both electronic nonadiabaticity and nuclear quantum effects within a
unified framework while retaining the computational efficiency of a
single-trajectory approach. At the same time, it inherits the principal
limitations of its parent methods: as a mean-field approximation, it cannot
describe wavepacket branching, and, like thawed Gaussian wavepacket dynamics,
it is most accurate for weakly anharmonic systems. These limitations become
particularly apparent near conical intersections. Whereas TGED fails for
conical intersections between electronic states of different symmetry, it
performs surprisingly well for conical intersections involving states of the
same symmetry.[43]

The TGED is not constrained to coupled electronic-nuclear dynamics; the
underlying formalism is applicable more generally to systems containing both
quantum and more classical-like degrees of freedom. Owing to its simple
structure, the method can be naturally extended to mixed states by replacing
wavefunctions with density matrices. It may also be systematically improved by
incorporating spin-mapping techniques, analogous to recent advances that have
enhanced Ehrenfest dynamics through spin mapping[68]and nonadiabatic-field methods.[15]Finally, although this work
has focused primarily on population dynamics, the mean-field character of TGED
suggests that, like Ehrenfest dynamics, it should perform better for
electronic coherences, making it a promising tool for the simulations of spectra.

## Acknowledgements.The author acknowledges the financial support from EPFL and thanks Alan
Scheidegger for useful discussions and producing
Figs.1and2.

## Author declarations

## Conflict of interest

The author has no conflicts to disclose.

## Data availability

This study did not generate any data.

## References
- Born and Oppenheimer [1927]M. Born and R. Oppenheimer,Ann. d. Phys.389, 457 (1927).
- Tannor [2007]D. J. Tannor,Introduction to Quantum
Mechanics: A Time-Dependent Perspective(University Science Books, Sausalito, 2007).
- Domcke and Yarkony [2012]W. Domcke and D. R. Yarkony,Annu. Rev. Phys. Chem.63, 325 (2012).
- Agostini and Curchod [2019]F. Agostini and B. F. E. Curchod,WIREs Comput. Mol. Sci.9, e1417 (2019).
- Choi and Vaníček [2019]S. Choi and J. Vaníček,J. Chem. Phys.150, 204112 (2019).
- Roulet, Choi, and Vaníček [2019]J. Roulet, S. Choi, and J. Vaníček,J. Chem. Phys.150, 204113 (2019).
- Abedi, Maitra, and Gross [2010]A. Abedi, N. T. Maitra, and E. K. Gross, Phys. Rev. Lett.105, 123002
(2010).
- Meyer, Manthe, and Cederbaum [1990]H.-D. Meyer, U. Manthe, and L. S. Cederbaum,Chem. Phys. Lett.165, 73 (1990).
- Martínez and Levine [1997]T. J. Martínez and R. D. Levine,J. Chem. Soc., Faraday Trans.93, 941 (1997).
- Worth, Robb, and Burghardt [2004]G. A. Worth, M. A. Robb, and I. Burghardt,Faraday Discuss.127, 307 (2004).
- Shalashilin [2009]D. V. Shalashilin,J. Chem. Phys.130, 244101 (2009).
- Kapral and Ciccotti [1999]R. Kapral and G. Ciccotti,J. Chem. Phys.110, 8919 (1999).
- Huo and Coker [2011]P. Huo and D. F. Coker,J. Chem. Phys.135, 201101 (2011).
- Runeson and Richardson [2020]J. E. Runeson and J. O. Richardson,J. Chem. Phys.152, 084110 (2020).
- Wuet al.[2025]B. Wu, B. Li, X. He, X. Cheng, J. Ren, and J. Liu,J. Chem. Theory Comput.21, 3775 (2025).
- Belyaev, Lasser, and Trigila [2014]A. K. Belyaev, C. Lasser, and G. Trigila,J. Chem. Phys.140, 224108 (2014).
- Subotniket al.[2016]J. E. Subotnik, A. Jain,
B. Landry, A. Petit, W. Ouyang, and N. Bellonzi,Annu. Rev. Phys. Chem.67, 387 (2016).
- Mannouch and Richardson [2023]J. R. Mannouch and J. O. Richardson,J. Chem. Phys.158, 104111 (2023).
- Tully [1990]J. C. Tully,J. Chem. Phys.93, 1061 (1990).
- Ehrenfest [1927]P. Ehrenfest, Z.
Phys45, 455 (1927).
- Tully [1998]J. C. Tully, Faraday
Discuss.110, 407
(1998).
- Scheidegger and Vaníček [2025a]A. Scheidegger and J. J. L. Vaníček,J. Chem. Phys.163, 044105 (2025a).
- Zeiri and Kosloff [1990]Y. Zeiri and R. Kosloff,J. Chem. Phys.93, 6890 (1990).
- Akimov, Long, and Prezhdo [2014]A. V. Akimov, R. Long, and O. V. Prezhdo,J. Chem. Phys.140, 194107 (2014).
- Gherib, Ryabinkin, and Izmaylov [2015]R. Gherib, I. G. Ryabinkin, and A. F. Izmaylov,J. Chem. Theory Comput.11, 1375 (2015).
- Miller [2001]W. H. Miller,J. Phys. Chem. A105, 2942 (2001).
- Vleck [1928]J. H. V. Vleck, Proc. Nat. Acad. Sci. USA14, 178 (1928).
- Herman and Kluk [1984]M. F. Herman and E. Kluk,Chem. Phys.91, 27 (1984).
- Ceotto, Di Liberto, and Conte [2017]M. Ceotto, G. Di Liberto, and R. Conte,Phys. Rev. Lett.119, 010401 (2017).
- Heller [1975]E. J. Heller,J. Chem. Phys.62, 1544 (1975).
- Heller [2018]E. J. Heller,The semiclassical way to
dynamics and spectroscopy(Princeton University
Press, Princeton, NJ, 2018).
- Coalson and Karplus [1990]R. D. Coalson and M. Karplus,J. Chem. Phys.93, 3919 (1990).
- Begušić, Cordova, and Vaníček [2019]T. Begušić, M. Cordova, and J. Vaníček,J. Chem. Phys.150, 154117 (2019).
- Vaníček [2023]J. J. L. Vaníček,J. Chem. Phys.159, 014114 (2023).
- Burkhardet al.[2024]S. Burkhard, B. Dörich, M. Hochbruck, and C. Lasser,Journal of Physics A: Mathematical and
Theoretical57, 295202
(2024).
- Wehrle, Šulc, and Vaníček [2014]M. Wehrle, M. Šulc, and J. Vaníček,J. Chem. Phys.140, 244114 (2014).
- Klētnieks, Alonso, and Vaníček [2023]E. Klētnieks, Y. C. Alonso, and J. J. L. Vaníček,J. Phys. Chem. A127, 8117 (2023).
- Begušić and Vaníček [2020]T. Begušić and J. Vaníček,J. Chem. Phys.153, 024105 (2020).
- Begušić and Vaníček [2021]T. Begušić and J. Vaníček,J. Phys. Chem. Lett.12, 2997 (2021).
- Golubev, Begušić, and Vaníček [2020]N. V. Golubev, T. Begušić, and J. Vaníček,Phys. Rev. Lett.125, 083001 (2020).
- Scheidegger, Vaníček, and Golubev [2022]A. Scheidegger, J. Vaníček, and N. V. Golubev,J. Chem. Phys.156, 034104 (2022).
- Scheidegger, Golubev, and Vaníček [2025]A. Scheidegger, N. V. Golubev, and J. J. L. Vaníček,Proc. Nat. Acad. Sci. USA122, e2501319122 (2025).
- Scheidegger and Vaníček [2025b]A. Scheidegger and J. J. L. Vaníček,“Thawed Gaussian Ehrenfest dynamics at conical
intersections: When can a single mean-field trajectory capture internal
conversion?”(2025b),arXiv:2504.05922 [physics.chem-ph].
- Dirac [1930]P. A. M. Dirac,Math. Proc. Camb. Phil. Soc.26, 376 (1930).
- Frenkel [1934]J. Frenkel,Wave mechanics(Clarendon Press, Oxford, 1934).
- Lubich [2008]C. Lubich,From Quantum to
Classical Molecular Dynamics: Reduced Models and Numerical Analysis, 12th ed. (European Mathematical
Society, Zürich, 2008).
- Lasser and Lubich [2020]C. Lasser and C. Lubich,Acta Numer.29, 229 (2020).
- Choi and Vaníček [2020]S. Choi and J. Vaníček,J. Chem. Phys.153, 211101 (2020).
- Choi and Vaníček [2021a]S. Choi and J. Vaníček,J. Chem. Phys.154, 124119 (2021a).
- Heller [1976a]E. J. Heller,J. Chem. Phys.64, 63 (1976a).
- Patoz, Begušić, and Vaníček [2018]A. Patoz, T. Begušić, and J. Vaníček,J. Phys. Chem. Lett.9, 2367 (2018).
- Heller [1976b]E. J. Heller,J. Chem. Phys.65, 4979 (1976b).
- Hagedorn [1980]G. A. Hagedorn,Commun. Math. Phys.71, 77 (1980).
- Hagedorn [1998]G. A. Hagedorn,Ann. Phys. (NY)269, 77 (1998).
- Ohsawa and Leok [2013]T. Ohsawa and M. Leok,J. Phys. A46, 405201 (2013).
- Moghaddasi Fereidani and Vaníček [2023]R. Moghaddasi Fereidani and J. J. L. Vaníček,J. Chem. Phys.159, 094114 (2023).
- Klētnieks and Vaníček [2026]E. Klētnieks and J. J. L. Vaníček, “Time-reversible and norm-conserving high-order integrators for the ab initio
thawed Gaussian approximation,” (2026), not published.
- Moghaddasi Fereidani and Vaníček [2023]R. Moghaddasi Fereidani and J. J. L. Vaníček,J. Chem. Phys.160, 044113 (2023).
- Köppel, Domcke, and Cederbaum [1984]H. Köppel, W. Domcke, and L. S. Cederbaum,Adv. Chem. Phys.57, 59 (1984).
- Domcke, Yarkony, and Köppel [2004]W. Domcke, D. Yarkony, and H. Köppel,Conical intersections: electronic
structure, dynamics & spectroscopy, Vol. 15 (World Scientific, 2004).
- Begušić, Tapavicza, and Vaníček [2022]T. Begušić, E. Tapavicza, and J. Vaníček,J. Chem. Theory Comput.18, 3065 (2022).
- Barbiero and Vaníček [2026]D. Barbiero and J. J. L. Vaníček,J. Chem. Phys.164, 234114 (2026).
- Pattanayak and Schieve [1994]A. K. Pattanayak and W. C. Schieve,Phys. Rev. E50, 3601 (1994).
- Hairer, Lubich, and Wanner [2006]E. Hairer, C. Lubich, and G. Wanner,Geometric Numerical
Integration: Structure-Preserving Algorithms for Ordinary Differential
Equations(Springer Berlin Heidelberg New York, 2006).
- Choi and Vaníček [2021b]S. Choi and J. Vaníček,J. Chem. Phys.155, 124104 (2021b).
- Petersen and Pedersen [2012]K. B. Petersen and M. S. Pedersen,“The matrix cookbook,”(2012).
- Vaníček and Choi [2026]J. J. L. Vaníček and S. Choi, “High-order geometric integrators for Ehrenfest dynamics,” (2026), not published.
- Runeson and Richardson [2019]J. E. Runeson and J. O. Richardson,J. Chem. Phys.151, 044119 (2019).

## 


- 


Major funding support from
