# Analytical mobility edge in nonreciprocal quasiperiodic lattices with next-nearest-neighbor hopping

**arXiv ID**: 2607.10996v1
**Authors**: Wenmin Wang, Xiaosen Yang, Xianqi Tong
**Published**: 2026-07-13
**Categories**: cond-mat.dis-nn, quant-ph
**Comments**: 9 pages, 5 figures
**HTML URL**: https://arxiv.org/html/2607.10996v1

## Abstract

We investigate localization transitions and spectral topology in a one-dimensional non-Hermitian generalization of the Aubry-André model in which both the nearest-neighbor and the next-nearest-neighbor hopping amplitudes are nonreciprocal. By extending the Fermi-surface point-matching method to nonreciprocal hopping, we derive a closed-form expression for the energy-dependent mobility edge in which the two nonreciprocity parameters are absorbed into exponentially renormalized effective hopping amplitudes. The mobility edge forms a single parabola in the energy--potential plane: nearest-neighbor nonreciprocity rigidly shifts the localization boundary toward stronger potentials, whereas next-nearest-neighbor nonreciprocity reduces the curvature of the boundary and thereby broadens the energy window in which extended and localized states coexist. Exact diagonalization confirms the analytical boundary for purely nearest-neighbor, purely next-nearest-neighbor, and combined nonreciprocity, and recovers the known Hermitian mobility edge in the reciprocal limit. We further analyze the spectral topology under periodic boundary conditions and show that the spectral winding numbers evaluated at base energies near the two band edges directly bracket the mixed phase: the winding number at the lower band edge drops when the mobility edge enters the spectrum and the first localized states appear, while the winding number at the upper band edge drops when the last extended states localize, delineating the full potential-strength window over which extended and localized states coexist. These results provide a compact analytical framework that connects energy-dependent localization, spectral topology, and nonreciprocity in quasiperiodic lattices, and they are directly testable in photonic, atomic, and electrical-circuit platforms.

## Full Text

Analytical mobility edge in nonreciprocal quasiperiodic lattices with next-nearest-neighbor hopping

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
- License: CC BY 4.0arXiv:2607.10996v1 [cond-mat.dis-nn] 13 Jul 2026

## Analytical mobility edge in nonreciprocal quasiperiodic lattices with
next-nearest-neighbor hoppingWenmin WangDepartment of Physics, Jiangsu University, Zhenjiang 212013, ChinaXiaosen Yangyangxs@ujs.edu.cnDepartment of Physics, Jiangsu University, Zhenjiang 212013, ChinaXianqi Tongxqtong@ujs.edu.cnDepartment of Physics, Jiangsu University, Zhenjiang 212013, China

## Abstract

We investigate localization transitions and spectral topology in a
one-dimensional non-Hermitian generalization of the Aubry-André model in
which both the nearest-neighbor and the next-nearest-neighbor hopping
amplitudes are nonreciprocal. By extending the Fermi-surface point-matching
method to nonreciprocal hopping, we derive a closed-form expression for the
energy-dependent mobility edge in which the two nonreciprocity parameters are
absorbed into exponentially renormalized effective hopping amplitudes. The
mobility edge forms a single parabola in the energy–potential plane:
nearest-neighbor nonreciprocity rigidly shifts the localization boundary
toward stronger potentials, whereas next-nearest-neighbor nonreciprocity
reduces the curvature of the boundary and thereby broadens the energy window
in which extended and localized states coexist. Exact diagonalization
confirms the analytical boundary for purely nearest-neighbor, purely
next-nearest-neighbor, and combined nonreciprocity, and recovers the known
Hermitian mobility edge in the reciprocal limit. We further analyze the spectral topology under periodic
boundary conditions and show that the spectral winding numbers evaluated
at base energies near the two band edges directly bracket the mixed
phase: the winding number at the lower band edge drops when the mobility
edge enters the spectrum and the first localized states appear, while
the winding number at the upper band edge drops when the last extended
states localize, delineating the full potential-strength window over
which extended and localized states coexist. These results provide a compact analytical framework that connects
energy-dependent localization, spectral topology, and nonreciprocity in
quasiperiodic lattices, and they are directly testable in photonic, atomic,
and electrical-circuit platforms.

## IIntroduction

Anderson localization, the suppression of quantum diffusion by a disordered
potential, is a cornerstone of condensed-matter
physics[4,42,20]. In one
dimension, the scaling theory of localization predicts that all
single-particle eigenstates are localized by an arbitrarily weak uncorrelated
random potential[2], which excludes a mobility edge
(ME)—an energy separating extended from localized states—in
one-dimensional random systems. Quasiperiodic potentials, which are
deterministic yet incommensurate with the underlying lattice, are not subject
to this restriction. The Aubry-André (AA)
model[27,6,32], a tight-binding chain with
a cosine potential of irrational spatial frequency, undergoes a
localization transition at a finite critical potential strength. Owing to
the exact self-duality of the model under a Fourier transformation, the
transition occurs simultaneously for all eigenstates, and the critical point
hosts nontrivial multifractal
states[39,36,64]. The AA transition has
been observed with ultracold atoms in bichromatic optical
lattices[62]and with light in quasiperiodic photonic
lattices[41].

An energy-dependent ME emerges once the AA self-duality is broken.
Established routes include slowly varying
potentials[16,17], longer-range
hopping[12,10,11,18], generalized
on-site modulations[21,70,44], and
related constructions whose critical properties can in some cases be
established rigorously through Avila’s global theory[7]. In
particular, Biddleet al.showed that adding next-nearest-neighbor
(NNN) hopping to the AA model produces an energy-dependent ME, for which an
approximate analytical expression is available in the regime of weak NNN
hopping[12,11]. Single-particle MEs and their
interplay with interactions have been observed in ultracold-atom
experiments[56,38,3,63], and a
cascade of delocalization transitions has been resolved in cavity-polariton
lattices[23]. For models that lack exact self-duality, Vu and
Das Sarma recently introduced the Fermi-surface point-matching method, which
matches high-symmetry points of the clean-lattice Fermi surface with their
duals and yields accurate analytical MEs for a broad class of
duality-breaking quasiperiodic models[68].

A parallel line of research concerns non-Hermitian lattice models, which
describe open systems with gain, loss, or nonreciprocal
transport[8,19,5,9,37]. Nonreciprocal hopping, introduced by Hatano and Nelson in the
context of vortex depinning[28,29,30], gives
rise to the non-Hermitian skin effect
(NHSE)[57,76,40,58,77,13,59]: under open boundary conditions (OBC) an
extensive number of eigenstates accumulates at one end of the chain. The
NHSE has a topological origin, being diagnosed by a nonzero spectral winding
number of the periodic-boundary spectrum around a base
energy[24,80]. Nonreciprocal lattices and their
boundary phenomena have been realized in robotic and mechanical
metamaterials[14,22], photonic quantum
walks[74], topolectrical circuits[31], optical
fiber loops[71], and ultracold atomic
gases[45].

Non-Hermitian quasiperiodic lattices combine these two threads and display a
rich phenomenology[33]. For the nonreciprocal AA model,
Longhi established that the localization transition is accompanied by a
topological transition of the complex spectrum and by a real-to-complex
spectral transition[54,53,55], and Jianget al.analyzed the competition between the NHSE and Anderson
localization in nonreciprocal quasicrystals[34]; the influence
of various forms of nonreciprocity on localization has been examined
further in Ref.[67]. Topological characterizations based on
winding numbers have been developed for broad classes of non-Hermitian
quasiperiodic models[79,78,52,65,15], and exact MEs have been obtained for models with specially
structured complex potentials or
hoppings[49,48,51,50,47,75,26,69,43,35]. Related studies have
addressed Floquet engineering[81], interaction
effects[61,25], first-order localization transitions
induced by imaginary potential domains[66], and the weakening of
the NHSE by long-range hopping in quasiperiodic
potentials[60]. On the experimental side, topological triple
phase transitions in non-Hermitian Floquet quasicrystals have been observed
in fiber-loop photonics[72], and MEs of a
non-Hermitian quasicrystal have been measured in photonic quantum
walks[46].

Within this body of work, the model closest to ours is the non-Hermitiant1t_{1}–t2t_{2}chain of Xiaet al., in which the NNN hopping is
reciprocal and the non-Hermiticity enters through a complex
parity-time-symmetric potential, allowing an exact ME via a generalized
duality[73]. Fornonreciprocalhopping, however, no
analytical ME is available for the generalized AA model with NNN hopping:
the existing exact results rely on symmetries that nonreciprocity destroys,
while the Hermitian point-matching analysis[68]does not address
complex spectra. In this paper we fill this gap by extending the
point-matching method to nonreciprocal hopping. The central result is that
the two nonreciprocity parameters are absorbed into effective NN and NNN
hopping amplitudes that grow exponentially with the respective
nonreciprocity strengths, leading to a closed-form parabolic ME in the
energy–potential plane. NN nonreciprocity rigidly shifts the parabola
toward larger potential strength, whereas NNN nonreciprocity reduces its
curvature. We verify the analytical boundary by exact diagonalization for
all three nonreciprocal configurations, recover the Hermitian ME of Biddleet al.[11]in the reciprocal limit, and map out the
relation between the ME and the spectral topology: winding numbers
evaluated at base energies near the two band edges bracket the mixed
phase, dropping at the potential strengths where the energy-dependent ME
enters and exits the spectrum.

The remainder of the paper is organized as follows.
SectionIIintroduces the model and the diagnostics.
SectionIIIderives the point-matching ME.
SectionIVpresents the numerical results: the Hermitian
baseline, the three nonreciprocal configurations, and the skin-effect
topology.
SectionVdiscusses the effective-hopping picture and
summarizes our conclusions. The solvable limits, the
imaginary-gauge analysis of the lineδ=2​β\delta=2\beta, and the numerical
methods are presented in AppendixesA–D.

## IIModel and diagnostics

We consider a one-dimensional non-Hermitian generalized AA model described
by the HamiltonianH=\displaystyle H={}∑iV​cos⁡(2​π​α​i+ϕ)​ci†​ci\displaystyle\sum_{i}V\cos(2\pi\alpha i+\phi)\,c_{i}^{\dagger}c_{i}+t​∑i(eβ​ci+1†​ci+e−β​ci†​ci+1)\displaystyle+t\sum_{i}\!\big(e^{\beta}c_{i+1}^{\dagger}c_{i}+e^{-\beta}c_{i}^{\dagger}c_{i+1}\big)+J​∑i(eδ​ci+2†​ci+e−δ​ci†​ci+2),\displaystyle+J\sum_{i}\!\big(e^{\delta}c_{i+2}^{\dagger}c_{i}+e^{-\delta}c_{i}^{\dagger}c_{i+2}\big),(1)

whereci†c_{i}^{\dagger}(cic_{i}) creates (annihilates) a particle at siteii.
The on-site potential of strengthVVis quasiperiodic with irrational
frequencyα=(5−1)/2\alpha=(\sqrt{5}-1)/2and phaseϕ\phi. The amplitudesttandJJdenote the nearest-neighbor (NN) and NNN hopping, and the real parametersβ\betaandδ\deltacontrol the nonreciprocity: the rightward hopping
amplitudes aret​eβt\,e^{\beta}andJ​eδJ\,e^{\delta}, while the leftward ones
aret​e−βt\,e^{-\beta}andJ​e−δJ\,e^{-\delta}. Forβ=δ=0\beta=\delta=0,
Eq. (II) reduces to the Hermitian generalized AA model with NNN
hopping studied by Biddleet al.[12,11]; forJ=0J=0andβ≠0\beta\neq 0it reduces to the nonreciprocal AA model of
Hatano-Nelson type analyzed by
Longhi[54,53]. Nonreciprocity rendersHHnon-Hermitian, with generally complex eigenvalues; under OBC it produces the
NHSE, an extensive accumulation of eigenstates at the boundary selected by
the direction of the stronger hopping.

To characterize bulk localization independently of the skin effect, we
evaluate the fractal dimension of each normalized right eigenstateψm​(i)\psi_{m}(i),D2=−ln​∑i|ψm​(i)|4ln⁡L,D_{2}=-\frac{\ln\sum_{i}|\psi_{m}(i)|^{4}}{\ln L},(2)

under periodic boundary conditions (PBC), for which the skin effect is
absent. Extended states yieldD2→1D_{2}\to 1and localized states yieldD2→0D_{2}\to 0as the system sizeLLincreases, while critical states take
intermediate values.

The topological content of the NHSE is captured by the spectral winding
number[24,80]W​(EB)=12​π​i​∫02​π𝑑θ​∂θln​det[H​(θ)−EB],W(E_{B})=\frac{1}{2\pi i}\int_{0}^{2\pi}\!d\theta\,\partial_{\theta}\ln\det\!\big[H(\theta)-E_{B}\big],(3)

whereH​(θ)H(\theta)is the Hamiltonian with a fluxθ\thetathreaded through
the PBC ring. A nonzero integerWWindicates that the complex PBC spectrum
winds around the base energyEBE_{B}and implies the existence of skin modes
at that energy under OBC;W=0W=0indicates that the spectrum does not
encloseEBE_{B}and no skin effect occurs at that energy.

## IIIAnalytical mobility edge

We begin by constructing an effective dispersion for the clean lattice.
ForV=0V=0and PBC, the Bloch ansatzψi∝ei​κ​i\psi_{i}\propto e^{i\kappa i}applied to
Eq. (II) yields the dispersionE​(κ)=2​t​cos⁡(κ−i​β)+2​J​cos⁡(2​κ−i​δ).E(\kappa)=2t\cos(\kappa-i\beta)+2J\cos(2\kappa-i\delta).(4)

The nonreciprocity therefore enters as imaginary shifts of the momentum,κ→κ−i​β\kappa\to\kappa-i\betafor the NN term and2​κ→2​κ−i​δ2\kappa\to 2\kappa-i\deltafor
the NNN term. For a state that propagates around the ring, these imaginary
shifts amplify the effective hopping amplitudes by the factorse|β|e^{|\beta|}ande|δ|e^{|\delta|}, respectively. Absorbing the amplification into the
amplitudes defines a real effective dispersion (see AppendixA)ε​(κ)=2​teff​cos⁡κ+2​Jeff​cos⁡2​κ,\varepsilon(\kappa)=2t_{\rm eff}\cos\kappa+2J_{\rm eff}\cos 2\kappa,(5)

with effective hoppingsteff=t​e|β|,Jeff=J​e|δ|.t_{\rm eff}=t\,e^{|\beta|},\qquad J_{\rm eff}=J\,e^{|\delta|}.(6)

The nonreciprocity parameters appear only through their absolute values:
the signs ofβ\betaandδ\delta, which select the boundary at which skin
modes accumulate under OBC, do not affect the bulk dispersion. This is
consistent with the invariance of the bulk spectrum under the imaginary
gauge transformation that reverses the direction of the skin effect.

With the effective dispersion in hand, we locate the ME by means of the
Fermi-surface point-matching method[68], which exploits the AA
duality. In the dual representation, the quasiperiodic
potential plays the role of a hopping of strengthVVon a dual lattice,
while the dispersionε​(κ)\varepsilon(\kappa)becomes the dual on-site energy.
The method postulates that at the ME, where the localization length
diverges, the high-symmetry points of the Fermi surface in the two
representations satisfy a matching condition that survives as a remnant of
the exact self-duality of the pure AA model.

Writingx=cos⁡κx=\cos\kappaand usingcos⁡2​κ=2​x2−1\cos 2\kappa=2x^{2}-1, the effective
dispersion becomesε=4​Jeff​x2+2​teff​x−2​Jeff\varepsilon=4J_{\rm eff}x^{2}+2t_{\rm eff}x-2J_{\rm eff}.
The point-matching condition identifies the dual hoppingVVwith the
effective NN hopping renormalized by the NNN term at the critical
momentum[68],V=2​teff+4​Jeff​cos⁡κc,V=2t_{\rm eff}+4J_{\rm eff}\cos\kappa_{c},(7)

which fixes the critical momentum throughcos⁡κc=V−2​teff4​Jeff.\cos\kappa_{c}=\frac{V-2t_{\rm eff}}{4J_{\rm eff}}.(8)

The ME energy isEc=ε​(κc)E_{c}=\varepsilon(\kappa_{c}). Substituting
Eq. (8) into Eq. (5) and simplifying
(AppendixA) gives the central result of this work,Ec=V2−2​V​teff4​Jeff−2​Jeff.\;E_{c}=\frac{V^{2}-2V\,t_{\rm eff}}{4J_{\rm eff}}-2J_{\rm eff}\;.(9)

Equation (9) describes a parabola in the energy–potential plane
with curvature1/(4​Jeff)1/(4J_{\rm eff})and vertex atV=teffV=t_{\rm eff},Ecmin=−teff2/(4​Jeff)−2​JeffE_{c}^{\rm min}=-t_{\rm eff}^{2}/(4J_{\rm eff})-2J_{\rm eff}. The vertex lies
below the bottom of the effective band, since the difference between the
two is−(teff−4​Jeff)2/(4​Jeff)≤0-(t_{\rm eff}-4J_{\rm eff})^{2}/(4J_{\rm eff})\leq 0. Consequently, the
physical (rising) branch of the parabola,V≥teffV\geq t_{\rm eff}, enters the
spectrum through the lower band edge: asVVincreases, the ME sweeps
upward through the band, states below the ME localize, and states above it
remain extended. The matching momentumκc\kappa_{c}is real for|V−2​teff|≤4​Jeff|V-2t_{\rm eff}|\leq 4J_{\rm eff}, so the ME exists forV∈[2​teff−4​Jeff,2​teff+4​Jeff]V\in[2t_{\rm eff}-4J_{\rm eff},\;2t_{\rm eff}+4J_{\rm eff}];
outside this interval all states are either extended (VVtoo small) or
localized (VVtoo large), and the interval between these two bounds
defines the mixed phase in which extended and localized states coexist.
The two nonreciprocity parameters act geometrically on the
parabola: NN nonreciprocity shifts the vertex to largerVVthroughtefft_{\rm eff}, whereas NNN nonreciprocity reduces the curvature throughJeffJ_{\rm eff}and thereby widens the mixed phase. As a point-matching estimate,
Eq. (9) is expected to be accurate when the NNN hopping is a
perturbation to the NN hopping,Jeff≪tJ_{\rm eff}\ll t, which is the regime
considered in the numerical tests below.

In the reciprocal limitβ=δ=0\beta=\delta=0, Eq. (9) becomesEc=(V2−2​t​V)/(4​J)−2​JE_{c}=(V^{2}-2tV)/(4J)-2J, the point-matching ME of the Hermitian generalized
AA model with NNN hopping. This expression is structurally different from
the result of Biddleet al.[12,11],EcH=V2​(tJ+Jt)−t2J,E_{c}^{\rm H}=\frac{V}{2}\!\left(\frac{t}{J}+\frac{J}{t}\right)-\frac{t^{2}}{J},(10)

which was obtained from a Lyapunov-exponent analysis in the limitt≫Jt\gg J.
As shown below (Fig.1), the two expressions give numerically
similar boundaries forJ≪tJ\ll t. Both are analytical approximations to the
same fractal localization boundary, for which no exact closed form is
known; the point-matching form Eq. (9) is the one that
generalizes to the nonreciprocal case.

## IVNumerical results

We test the analytical predictions by exact diagonalization of
Eq. (II) under PBC witht=1t=1andJ=0.1J=0.1, for whichJeff≪tJ_{\rm eff}\ll tand the point-matching estimate is expected to hold. All
system sizes are Fibonacci numbers, which provide the optimal rational
approximants to the golden-ratio frequencyα\alpha: the Hermitian baseline
is computed atL=987L=987, the nonreciprocal phase diagrams atL=610L=610, the
winding number atL=377L=377, and the complex spectra atL=987L=987(PBC) andL=89L=89(OBC). In all phase
diagrams the analytical ME is drawn along its physical branch where it lies
within the spectrum at the same potential strength.Figure 1:Hermitian limitβ=δ=0\beta=\delta=0(t=1t=1,J=0.1J=0.1,L=987L=987,
PBC). The color scale shows the fractal dimensionD2D_{2}(bright:
extended,D2→1D_{2}\to 1; dark: localized,D2→0D_{2}\to 0). The Biddle ME of
Eq. (10) (black solid line) and the point-matching ME of
Eq. (9) (red dashed line) are two analytical approximations to
the same extended–localized boundary; both follow the numerical
transition closely forJ≪tJ\ll t.

Figure1shows the Hermitian phase diagram in the
energy–potential plane. For smallVVall states are extended
(D2→1D_{2}\to 1); asVVincreases, the spectrum localizes progressively, and
the energy-dependent boundary reflects the breaking of self-duality by the
NNN hopping. Both the Biddle line of Eq. (10) and the
point-matching parabola of Eq. (9) track this boundary as it
rises through the spectrum from the lower band edge. The two curves are
numerically close but not identical, in accordance with their different
analytical origins, and they agree best in the central part of the
spectrum, where thet≫Jt\gg Japproximation is most reliable. This figure
establishes the Hermitian baseline against which the nonreciprocal shifts
are measured.Figure 2:Nonreciprocal phase diagrams (t=1t=1,J=0.1J=0.1,L=610L=610, PBC)
together with the point-matching ME of Eq. (9) (red dashed
lines). (a) NN nonreciprocity only,β=0.25\beta=0.25,δ=0\delta=0(teff=e0.25≈1.28t_{\rm eff}=e^{0.25}\approx 1.28,Jeff=0.1J_{\rm eff}=0.1): the boundary
shifts rigidly to largerVV. (b) NNN nonreciprocity only,β=0\beta=0,δ=0.25\delta=0.25(teff=1t_{\rm eff}=1,Jeff=0.1​e0.25≈0.13J_{\rm eff}=0.1\,e^{0.25}\approx 0.13): the curvature of the boundary
decreases and the parabola widens. (c)
Combined case,β=δ=0.5\beta=\delta=0.5: the shift and the widening superpose. In all three
panels the analytical parabola, with no adjustable parameters, follows
the extended–localized boundary.

Turning to the nonreciprocal regime, Fig.2presents the
three physically distinct configurations. In panel (a), only the NN hopping is
nonreciprocal (β=0.25\beta=0.25,δ=0\delta=0), so thatteff=t​e0.25≈1.28t_{\rm eff}=t\,e^{0.25}\approx 1.28whileJeff=JJ_{\rm eff}=J. The boundary
shifts rigidly toward larger potential strength: the vertex of the parabola
moves fromV=1V=1(the Hermitian value) toV=teff≈1.28V=t_{\rm eff}\approx 1.28, while
the curvature1/(4​Jeff)=2.51/(4J_{\rm eff})=2.5is unchanged. Physically, the
nonreciprocal NN hopping enhances the effective bandwidth, so a stronger
potential is required to localize the states.

In panel (b), only the NNN hopping is nonreciprocal (β=0\beta=0,δ=0.25\delta=0.25), so thatteff=tt_{\rm eff}=tandJeff=J​e0.25≈0.13J_{\rm eff}=J\,e^{0.25}\approx 0.13. The vertex position is unchanged atV=1V=1, but the curvature decreases from2.52.5to1/(4×0.13)≈1.91/(4\times 0.13)\approx 1.9, which widens the parabola and broadens the
range of potential strengths over which extended and localized states
coexist. The same parameter set is used for the spectral-topology analysis
of Fig.3below.

Panel (c) combines both nonreciprocities (β=δ=0.5\beta=\delta=0.5), and the
resulting boundary is simultaneously shifted and widened. In all three
configurations, the single formula Eq. (9), with no adjustable
parameters, reproduces the numerically determined extended–localized
boundary across the spectrum. A quantitative comparison at fixed energies
shows that the predicted critical potential agrees with the numerical
boundary to within a few percent over the central and upper parts of the
spectrum, while the largest deviations, of order ten percent, occur near
the lower band edge. The same trend is already present in the Hermitian
limit (Fig.1), reflecting the fact that the point-matching
construction anchors the boundary at the high-symmetry points of the band
and is least constrained at its edges.Figure 3:Skin-effect topology for NNN nonreciprocity (β=0\beta=0,δ=0.25\delta=0.25,t=1t=1,J=0.1J=0.1). (a) Spectral winding numbersW​(EB)W(E_{B})at two base energies near the band edges,EB=−2.0E_{B}=-2.0(red) andEB=2.8E_{B}=2.8(blue), as a function ofVV.
The winding number at the lower band edge drops atV1≈1.6V_{1}\approx 1.6, marking the onset of the mixed phase where the
ME enters the spectrum and the first localized states appear. The
winding number at the upper band edge drops atV2≈2.6V_{2}\approx 2.6,
marking the end of the mixed phase where the last extended states
localize. The interval[V1,V2][V_{1},V_{2}]defines the mixed phase in which
extended and localized states coexist at different energies.
(b)–(d) Complex energy spectra under PBC (blue dots) and OBC
(red crosses) atV=0.8V=0.8,1.51.5, and3.03.0(L=987L=987).
AtV=0.8V=0.8the PBC spectrum forms loops that enclose the origin
while the OBC spectrum collapses onto the real axis, which is the
spectral hallmark of the NHSE. AtV=1.5V=1.5, near the onset of the
mixed phase, the loops are shrinking.
AtV=3.0V=3.0nearly the entire spectrum is real under both boundary
conditions; the NHSE is suppressed and all states are localized.

Figure3examines the fate of the NHSE as the potential
localizes the spectrum, for the same parameters as in
Fig.2(b) (β=0\beta=0,δ=0.25\delta=0.25). Panel (a) shows
the spectral winding numbersW​(EB)W(E_{B})evaluated at two base energies
near the band edges,EB=−2.0E_{B}=-2.0andEB=2.8E_{B}=2.8, as a function ofVV.
For smallVVboth winding numbers equal one: the complex PBC spectrum
forms loops that enclose both base energies and the NHSE is active at
those energies. AsVVincreases, the energy-dependent ME enters the
spectrum from the lower band edge, and the winding number at the lower
base energyEB=−2.0E_{B}=-2.0drops to zero atV1≈1.6V_{1}\approx 1.6, marking the
onset of the mixed phase. The winding number at the upper base energyEB=2.8E_{B}=2.8drops atV2≈2.6V_{2}\approx 2.6, marking the end of the mixed phase
where the last extended states at the upper band edge localize.
The interval[V1,V2][V_{1},V_{2}]thus defines the mixed phase in which
localized and extended states coexist at different energies, a
characteristic feature of systems with energy-dependent MEs.

Panels (b)–(d) display the corresponding complex spectra. AtV=0.8V=0.8[panel (b)], the PBC spectrum forms loops that enclose the origin, while
the OBC spectrum collapses onto the real axis; this extreme sensitivity of
the spectrum to the boundary conditions is the defining signature of the
NHSE. AtV=1.5V=1.5[panel (c)], near the onset of the mixed phase, the
spectral loops are shrinking. AtV=3.0V=3.0[panel (d)], well aboveV2V_{2},
nearly the entire spectrum is real under both boundary conditions; the
NHSE is suppressed and all states are localized.

The physical picture is as follows. Extended states sample the entire
ring and experience the net nonreciprocal flow, thereby acquiring complex
energies; localized states are confined to a region much smaller than the
ring and are insensitive to the boundary, so their energies remain real.
The vanishing of the eigenvalue imaginary parts at a given energy
therefore coincides with the localization of the corresponding states and
is predicted quantitatively by the ME of Eq. (9). The two
winding numbers at the band-edge base energies directly bracket the
mixed phase:V1V_{1}marks the appearance of the first localized states at
the lower band edge, whileV2V_{2}marks the localization of the last
extended states at the upper band edge.

## VConclusion

We have derived a closed-form mobility edge for the non-Hermitian
generalized Aubry-André model with nonreciprocal nearest-neighbor and
next-nearest-neighbor hopping by extending the Fermi-surface
point-matching method to nonreciprocal systems. The central result is an
effective-hopping description: the ME is the Hermitian point-matching
parabola with the bare hoppings replaced byteff=t​e|β|t_{\rm eff}=t\,e^{|\beta|}andJeff=J​e|δ|J_{\rm eff}=J\,e^{|\delta|}. The skin
effect amplifies the apparent hopping, so a stronger potential is required
to localize the states, and the ME shifts to largerVV. Because only|β||\beta|and|δ||\delta|enter, the direction of the nonreciprocity does
not affect the bulk ME. The effective hoppings also account for the
solvable limits:Jeff→0J_{\rm eff}\to 0gives the nonreciprocal AA chain
(Vc=2​teffV_{c}=2t_{\rm eff})[28,54], whileteff→0t_{\rm eff}\to 0gives decoupled nonreciprocal sublattices
(Vc=2​JeffV_{c}=2J_{\rm eff}); on the lineδ=2​β\delta=2\betaan imaginary gauge
transformation removes the nonreciprocity under OBC, but the
transformation is not single valued on a ring, so the PBC bulk ME
remains shifted (AppendixC). Two caveats delimit the
validity: the generalized AA model is not exactly self-dual and its
spectrum is fractal, so Eq. (9) is an analytical estimate
accurate forJeff≪tJ_{\rm eff}\ll t; and the independent treatment of|β||\beta|and|δ||\delta|applies to the bulk ME under PBC, whereas the
OBC properties depend onδ~=δ−2​β\tilde{\delta}=\delta-2\beta.

Exact diagonalization confirms the analytical boundary for all three
nonreciprocal configurations and recovers the Hermitian result in the
reciprocal limit. The analysis of the spectral topology shows that the spectral winding
numbers evaluated at base energies near the two band edges directly
bracket the mixed phase, dropping at the potential strengths where the
energy-dependent ME enters and exits the spectrum.

Non-Hermitian quasiperiodic lattices have been realized in optical fiber
loops[71,72], photonic quantum
walks[74,46], topolectrical circuits[31],
active mechanical metamaterials[14,22], and
ultracold atomic gases[45]. The ME predicted here can be
probed through the energy-resolved participation ratio, and the winding
number through the boundary dependence of the spectrum. Natural extensions
include longer-range nonreciprocal hopping, higher dimensions, and the
interplay of energy-dependent MEs with Floquet
driving[81,72]and many-body
interactions[25,61].

## Acknowledgements.This work was supported by the Natural Science Foundation of Jiangsu
Province (Grant No. BK20231320).

## DATA AVAILABILITY

The data that support the findings of this article are not publicly available. The data are available from the authors upon reasonable request.

## Appendix ADerivation of the point-matching mobility edge

ForV=0V=0and PBC, the Bloch ansatzψi∝ei​κ​i\psi_{i}\propto e^{i\kappa i}applied
to Eq. (II) givesE​(κ)=2​t​cos⁡(κ−i​β)+2​J​cos⁡(2​κ−i​δ)E(\kappa)=2t\cos(\kappa-i\beta)+2J\cos(2\kappa-i\delta). The imaginary
gauge transformationci→e−β​i​cic_{i}\to e^{-\beta i}c_{i}removes the NN
nonreciprocity and shifts the NNN one toδ~=δ−2​β\tilde{\delta}=\delta-2\beta(AppendixC); the amplification of the NN and NNN hopping
experienced by a state propagating around the ring has magnitudee|β|e^{|\beta|}ande|δ|e^{|\delta|}, respectively. Absorbing these factors
into the amplitudes yields the effective dispersion of
Eqs. (5) and (6).

Writingx=cos⁡κx=\cos\kappaand usingcos⁡2​κ=2​x2−1\cos 2\kappa=2x^{2}-1, the effective
dispersion readsε=4​Jeff​x2+2​teff​x−2​Jeff\varepsilon=4J_{\rm eff}x^{2}+2t_{\rm eff}x-2J_{\rm eff}.
The point-matching ansatz[68]identifies the dual hoppingVVwith the effective NN hopping renormalized by the NNN term at the critical
momentum,V=2​teff+4​Jeff​xcV=2t_{\rm eff}+4J_{\rm eff}x_{c}, which givesxc=(V−2​teff)/(4​Jeff)x_{c}=(V-2t_{\rm eff})/(4J_{\rm eff}), i.e., Eq. (8).
Substituting intoEc=ε​(κc)E_{c}=\varepsilon(\kappa_{c}),Ec\displaystyle E_{c}=4​Jeff​xc2+2​teff​xc−2​Jeff\displaystyle=4J_{\rm eff}x_{c}^{2}+2t_{\rm eff}x_{c}-2J_{\rm eff}=(V−2​teff)24​Jeff+teff​(V−2​teff)2​Jeff−2​Jeff\displaystyle=\frac{(V-2t_{\rm eff})^{2}}{4J_{\rm eff}}+\frac{t_{\rm eff}(V-2t_{\rm eff})}{2J_{\rm eff}}-2J_{\rm eff}=V2−2​V​teff4​Jeff−2​Jeff,\displaystyle=\frac{V^{2}-2Vt_{\rm eff}}{4J_{\rm eff}}-2J_{\rm eff},(11)

which reproduces Eq. (9). The matching momentumκc\kappa_{c}is
real for|xc|≤1|x_{c}|\leq 1, i.e., for|V−2​teff|≤4​Jeff|V-2t_{\rm eff}|\leq 4J_{\rm eff}; outside
this windowκc\kappa_{c}becomes complex and the ME continues analytically.
The physical branch is the rising branch withV≥teffV\geq t_{\rm eff}.

## Appendix BSolvable limitsJ=0J=0andt=0t=0Figure 4:Solvable limits (L=610L=610, PBC). (a)J=0J=0,t=1t=1,β=0.25\beta=0.25: the localization transition is energy independent and
occurs atVc=2​t​e|β|≈2.57V_{c}=2t\,e^{|\beta|}\approx 2.57(red dashed vertical line).
(b)t=0t=0,J=1J=1,δ=0.5\delta=0.5: the transition is energy independent
and occurs atVc=2​J​e|δ|≈3.30V_{c}=2J\,e^{|\delta|}\approx 3.30(red dashed vertical
line). In both limits the ME degenerates into a vertical line, and no
energy-dependent boundary exists. In (b) each eigenstate extends over a
single sublattice, so the fractal dimension of extended states is
slightly reduced,D2≈1−ln⁡2/ln⁡LD_{2}\approx 1-\ln 2/\ln L.

## Nonreciprocal AA chain (J=0J=0).

The eigenvalue equation reduces toE​ψi=Vi​ψi+t​eβ​ψi−1+t​e−β​ψi+1E\psi_{i}=V_{i}\psi_{i}+t\,e^{\beta}\psi_{i-1}+t\,e^{-\beta}\psi_{i+1}, withVi=V​cos⁡(2​π​α​i+ϕ)V_{i}=V\cos(2\pi\alpha i+\phi). The imaginary gauge transformationψi=e−β​i​ui\psi_{i}=e^{-\beta i}u_{i}maps this equation to the Hermitian AA modelE​ui=Vi​ui+t​(ui−1+ui+1)Eu_{i}=V_{i}u_{i}+t(u_{i-1}+u_{i+1}), whose Lyapunov exponentγ=max⁡[0,ln⁡(V/2​t)]\gamma=\max[0,\ln(V/2t)]is independent of energy. On a ring, an
eigenstate of the Hermitian model survives the gauge transformation only
ifγ>|β|\gamma>|\beta|, so the global transition shifts toVc=2​t​e|β|V_{c}=2t\,e^{|\beta|}[Fig.4(a)], an energy-independent
vertical line without an ME, in agreement with
Refs.[28,54,34].

## Decoupled sublattices (t=0t=0).

Settingt=0t=0in Eq. (II) decouples the even and odd sublattices.
For the even sublattice, withn=2​mn=2m,E​u2​m=V​cos⁡(4​π​α​m+ϕ)​u2​m+J​eδ​u2​m−2+J​e−δ​u2​m+2,Eu_{2m}=V\cos(4\pi\alpha m+\phi)\,u_{2m}+J\,e^{\delta}u_{2m-2}+J\,e^{-\delta}u_{2m+2},(12)

and analogously for the odd sublattice with a shifted phase. Each
sublattice is a nonreciprocal AA chain with hoppingJJ, nonreciprocityδ\delta, and frequency2​α2\alpha. The gauge argument of theJ=0J=0case,
witht→Jt\to Jandβ→δ\beta\to\delta, givesVc=2​J​e|δ|V_{c}=2J\,e^{|\delta|}[Fig.4(b)]. Both limits are degenerations of
Eq. (9): asJeff→0J_{\rm eff}\to 0orteff→0t_{\rm eff}\to 0the parabola
collapses to a vertical line atV=2​teffV=2t_{\rm eff}orV=2​JeffV=2J_{\rm eff},
respectively.

## Appendix CImaginary gauge transformation and the lineδ=2​β\delta=2\betaFigure 5:Gauge-related caseδ=2​β\delta=2\beta(β=0.25\beta=0.25,δ=0.50\delta=0.50,δ~=0\tilde{\delta}=0;t=1t=1,J=0.1J=0.1,L=610L=610, PBC). The
color scale shows the fractal dimensionD2D_{2}. The red dashed line is
the point-matching ME of Eq. (9) withteff=e0.25t_{\rm eff}=e^{0.25}andJeff=0.1​e0.50J_{\rm eff}=0.1\,e^{0.50}. Although the
imaginary gauge transformation maps the open chain to the Hermitian
model, it is not single valued on the PBC ring: the bulk boundary is
shifted to largerVVrelative to the Hermitian Biddle line [whoseE=0E=0crossing lies atV≈1.98V\approx 1.98, versusV≈2.65V\approx 2.65for the
parabola] and is well described by the effective-hopping parabola.

Insertingψi=e−β​i​ui\psi_{i}=e^{-\beta i}u_{i}into the eigenvalue equation of
Eq. (II) yieldsE​ui=Vi​ui+t​(ui+1+ui−1)+J​eδ~​ui+2+J​e−δ~​ui−2,Eu_{i}=V_{i}u_{i}+t(u_{i+1}+u_{i-1})+J\,e^{\tilde{\delta}}u_{i+2}+J\,e^{-\tilde{\delta}}u_{i-2},(13)

with the residual NNN nonreciprocityδ~=δ−2​β\tilde{\delta}=\delta-2\beta: the NN
hopping becomes reciprocal, the potential is unchanged, and only the NNN
hopping retains nonreciprocity. On the lineδ=2​β\delta=2\betaone hasδ~=0\tilde{\delta}=0, and the transformed model is Hermitian.

Under OBC the transformation is an exact similarity transformation, so the
OBC localization properties on this line are those of the Hermitian model.
On a ring, however, the factore−β​ie^{-\beta i}is not single valued: the
gauge maps PBC onto a chain with a boundary defect of strengthe∓β​Le^{\mp\beta L}, and the Hatano-Nelson
argument[28,30,54]shows that an eigenstate
of the Hermitian model with Lyapunov exponentγH​(E)\gamma_{\rm H}(E)survives
on the ring only ifγH​(E)>|β|\gamma_{\rm H}(E)>|\beta|; states withγH​(E)<|β|\gamma_{\rm H}(E)<|\beta|delocalize around the ring and acquire complex
energies. The PBC mobility edge on the lineδ=2​β\delta=2\betais therefore
determined byγH​(Ec)=|β|,\gamma_{\rm H}(E_{c})=|\beta|,(14)

rather than byγH=0\gamma_{\rm H}=0. SinceγH​(E)\gamma_{\rm H}(E)vanishes
linearly at the Hermitian ME,γH​(E)≃κ​(E−EcH)\gamma_{\rm H}(E)\simeq\kappa(E-E_{c}^{\rm H})withκ=d​γH/d​E|EcH>0\kappa=d\gamma_{\rm H}/dE|_{E_{c}^{\rm H}}>0, the leading nonreciprocal
correction isEc≈EcH+|β|κ.E_{c}\approx E_{c}^{\rm H}+\frac{|\beta|}{\kappa}.(15)

BecauseγH​(E)\gamma_{\rm H}(E)of the NNN model has no simple closed form,κ\kappamust be evaluated numerically, and the effective-hopping parabola
of Eq. (9) provides the practical closed-form alternative.
Figure5confirms this picture forβ=0.25\beta=0.25,δ=0.50\delta=0.50: the PBC fractal-dimension boundary is shifted away from the
Hermitian Biddle line (whoseE=0E=0crossing lies atV≈1.98V\approx 1.98) and
follows Eq. (9), whose crossing ofE=0E=0atV≈2.65V\approx 2.65agrees with the numerical boundary ofD2D_{2}.

## Appendix DNumerical methods

The phase diagrams are obtained by exact diagonalization of
Eq. (II) under PBC for Fibonacci sizesLL, which provide the best
rational approximants to the frequencyα\alpha. The fractal dimensionD2D_{2}is computed from the normalized right eigenvectors via
Eq. (2). For Hermitian parameters the spectrum is obtained with
a Hermitian eigensolver; for non-Hermitian parameters a full complex
eigendecomposition is performed. PBC is used throughout so thatD2D_{2}reflects bulk localization rather than the skin effect, and the numerical
ME is identified as the boundary whereD2D_{2}drops from values near one to
values near zero. The phase diagrams in
Figs.1,2,4, and5are computed at a fixed representative phaseϕ=0\phi=0.

The winding number of Eq. (3) is computed by discretizingθ∈[0,2​π]\theta\in[0,2\pi]intoN≥120N\geq 120points, distributing the flux uniformly
over the ring (each NN link acquires a factorei​θ/Le^{i\theta/L}and each NNN
link a factore2​i​θ/Le^{2i\theta/L}), evaluatingdet[H​(θj)−EB]\det[H(\theta_{j})-E_{B}]through a stabilized LU factorization, unwrapping
the accumulated argument, and dividing the total phase winding by2​π2\pi.
The result is integer valued for convergedNNand is robust with respect
to the system size and the potential phase. In Fig.3(a) the
winding numbers are evaluated at two base energies near the band edges,EB=−2.0E_{B}=-2.0andEB=2.8E_{B}=2.8; their drop pointsV1V_{1}andV2V_{2}are located
by bisection inVVto an accuracy of10−310^{-3}. The complex spectra in
Fig.3are obtained by direct diagonalization atL=987L=987under PBC andL=89L=89under OBC; the small OBC size is dictated by the
condition number, of ordere|δ~|​L/2e^{|\tilde{\delta}|L/2}, of the similarity
transformation connecting the open chain to its reciprocal counterpart,
which renders the OBC spectrum of a long nonreciprocal chain numerically
unreliable in double precision.

## References
- [1]Cited by:Analytical mobility edge in nonreciprocal quasiperiodic lattices with
next-nearest-neighbor hopping.
- [2]E. Abrahams, P. W. Anderson, D. C. Licciardello, and T. V. Ramakrishnan(1979)Scaling theory of localization: absence of quantum diffusion in two dimensions.Phys. Rev. Lett.42,pp. 673–676.External Links:DocumentCited by:§I.
- [3]F. A. An, K. Padavić, E. J. Meier, S. Hegde, S. Ganeshan, J. H. Pixley, S. Vishveshwara, and B. Gadway(2021)Interactions and mobility edges: observing the generalized Aubry-André model.Phys. Rev. Lett.126,pp. 040603.External Links:DocumentCited by:§I.
- [4]P. W. Anderson(1958)Absence of diffusion in certain random lattices.Phys. Rev.109,pp. 1492–1505.External Links:DocumentCited by:§I.
- [5]Y. Ashida, Z. Gong, and M. Ueda(2020)Non-hermitian physics.Adv. Phys.69,pp. 249–435.External Links:DocumentCited by:§I.
- [6]S. Aubry and G. André(1980)Analyticity breaking and anderson localization in incommensurate lattices.Ann. Israel Phys. Soc.3,pp. 133–164.Cited by:§I.
- [7]A. Avila(2015)Global theory of one-frequency Schrödinger operators.Acta Math.215,pp. 1–54.External Links:DocumentCited by:§I.
- [8]C. M. Bender and S. Boettcher(1998)Real spectra in non-hermitian Hamiltonians having𝒫​𝒯\mathcal{PT}symmetry.Phys. Rev. Lett.80,pp. 5243–5246.External Links:DocumentCited by:§I.
- [9]E. J. Bergholtz, J. C. Budich, and F. K. Kunst(2021)Exceptional topology of non-Hermitian systems.Rev. Mod. Phys.93,pp. 015005.External Links:DocumentCited by:§I.
- [10]J. Biddle and S. Das Sarma(2010)Predicted mobility edges in one-dimensional incommensurate optical lattices: an exactly solvable model of anderson localization.Phys. Rev. Lett.104,pp. 070601.External Links:DocumentCited by:§I.
- [11]J. Biddle, D. J. Priour, B. Wang, and S. Das Sarma(2011)Localization in one-dimensional lattices with non-nearest-neighbor hopping: generalized Anderson and Aubry-André models.Phys. Rev. B83,pp. 075105.External Links:DocumentCited by:§I,§I,§II,§III.
- [12]J. Biddle, B. Wang, D. J. Priour, and S. Das Sarma(2009)Localization in one-dimensional incommensurate lattices beyond the Aubry-André model.Phys. Rev. A80,pp. 021603(R).External Links:DocumentCited by:§I,§II,§III.
- [13]D. S. Borgnia, A. J. Kruchkov, and R. Slager(2020)Non-hermitian boundary modes and topology.Phys. Rev. Lett.124,pp. 056802.External Links:DocumentCited by:§I.
- [14]M. Brandenbourger, X. Locsin, E. Lerner, and C. Coulais(2019)Non-reciprocal robotic metamaterials.Nat. Commun.10,pp. 4608.External Links:DocumentCited by:§I,§V.
- [15]X. Cai(2022)Localization transitions and winding numbers for non-Hermitian Aubry-André-Harper models with off-diagonal modulations.Phys. Rev. B106,pp. 214207.External Links:DocumentCited by:§I.
- [16]S. Das Sarma, S. He, and X. C. Xie(1988)Mobility edge in a model one-dimensional potential.Phys. Rev. Lett.61,pp. 2144–2147.External Links:DocumentCited by:§I.
- [17]S. Das Sarma, S. He, and X. C. Xie(1990)Localization, mobility edges, and metal-insulator transition in a class of one-dimensional slowly varying deterministic potentials.Phys. Rev. B41,pp. 5544–5565.External Links:DocumentCited by:§I.
- [18]X. Deng, S. Ray, S. Sinha, G. V. Shlyapnikov, and L. Santos(2019)One-dimensional quasicrystals with power-law hopping.Phys. Rev. Lett.123,pp. 025301.External Links:DocumentCited by:§I.
- [19]R. El-Ganainy, K. G. Makris, M. Khajavikhan, Z. H. Musslimani, S. Rotter, and D. N. Christodoulides(2018)Non-hermitian physics and𝒫​𝒯\mathcal{PT}symmetry.Nat. Phys.14,pp. 11–19.External Links:DocumentCited by:§I.
- [20]F. Evers and A. D. Mirlin(2008)Anderson transitions.Rev. Mod. Phys.80,pp. 1355–1417.External Links:DocumentCited by:§I.
- [21]S. Ganeshan, J. H. Pixley, and S. Das Sarma(2015)Nearest neighbor tight binding models with an exact mobility edge in one dimension.Phys. Rev. Lett.114,pp. 146601.External Links:DocumentCited by:§I.
- [22]A. Ghatak, M. Brandenbourger, J. van Wezel, and C. Coulais(2020)Observation of non-hermitian topology and its bulk-edge correspondence in an active mechanical metamaterial.Proc. Natl. Acad. Sci. U.S.A.117,pp. 29561–29568.External Links:DocumentCited by:§I,§V.
- [23]V. Goblot, A. Štrkalj, N. Pernet, J. L. Lado, C. Dorow, A. Lemaître, L. Le Gratiet, A. Harouri, I. Sagnes, S. Ravets, A. Amo, J. Bloch, and O. Zilberberg(2020)Emergence of criticality through a cascade of delocalization transitions in quasiperiodic chains.Nat. Phys.16,pp. 832–836.External Links:DocumentCited by:§I.
- [24]Z. Gong, Y. Ashida, K. Kawabata, K. Takasan, S. Higashikawa, and M. Ueda(2018)Topological phases of non-hermitian systems.Phys. Rev. X8,pp. 031079.External Links:DocumentCited by:§I,§II.
- [25]R. Hamazaki, K. Kawabata, and M. Ueda(2019)Non-hermitian many-body localization.Phys. Rev. Lett.123,pp. 090603.External Links:DocumentCited by:§I,§V.
- [26]W. Han and L. Zhou(2022)Dimerization-induced mobility edges and multiple reentrant localization transitions in non-hermitian quasicrystals.Phys. Rev. B105,pp. 054204.External Links:DocumentCited by:§I.
- [27]P. G. Harper(1955)Single band motion of conduction electrons in a uniform magnetic field.Proc. Phys. Soc. London Sect. A68,pp. 874–878.External Links:DocumentCited by:§I.
- [28]N. Hatano and D. R. Nelson(1996)Localization transitions in non-hermitian quantum mechanics.Phys. Rev. Lett.77,pp. 570–573.External Links:DocumentCited by:Appendix B,Appendix C,§I,§V.
- [29]N. Hatano and D. R. Nelson(1997)Vortex pinning and non-Hermitian quantum mechanics.Phys. Rev. B56,pp. 8651–8673.External Links:DocumentCited by:§I.
- [30]N. Hatano and D. R. Nelson(1998)Non-Hermitian delocalization and eigenfunctions.Phys. Rev. B58,pp. 8384–8390.External Links:DocumentCited by:Appendix C,§I.
- [31]T. Helbig, T. Hofmann, S. Imhof, M. Abdelghany, T. Kiessling, L. W. Molenkamp, C. H. Lee, A. Szameit, M. Greiter, and R. Thomale(2020)Generalized bulk-boundary correspondence in non-hermitian topolectrical circuits.Nat. Phys.16,pp. 747–750.External Links:DocumentCited by:§I,§V.
- [32]D. R. Hofstadter(1976)Energy levels and wave functions of bloch electrons in rational and irrational magnetic fields.Phys. Rev. B14,pp. 2239–2249.External Links:DocumentCited by:§I.
- [33]A. Jazaeri and I. I. Satija(2001)Localization transition in incommensurate non-Hermitian systems.Phys. Rev. E63,pp. 036222.External Links:DocumentCited by:§I.
- [34]H. Jiang, L. Lang, C. Yang, S. Zhu, and S. Chen(2019)Interplay of non-hermitian skin effects and anderson localization in nonreciprocal quasiperiodic lattices.Phys. Rev. B100,pp. 054301.External Links:DocumentCited by:Appendix B,§I.
- [35]X. Jiang, M. Xu, and L. Pan(2025)Generic non-hermitian mobility edges in a class of duality-breaking quasicrystals.Results Phys.70,pp. 108146.External Links:DocumentCited by:§I.
- [36]S. Ya. Jitomirskaya(1999)Metal-insulator transition for the almost Mathieu operator.Ann. Math.150,pp. 1159–1175.External Links:DocumentCited by:§I.
- [37]K. Kawabata, K. Shiozaki, M. Ueda, and M. Sato(2019)Symmetry and topology in non-hermitian physics.Phys. Rev. X9,pp. 041015.External Links:DocumentCited by:§I.
- [38]T. Kohlert, S. Scherg, X. Li, H. P. Lüschen, S. Das Sarma, I. Bloch, and M. Aidelsburger(2019)Observation of many-body localization in a one-dimensional system with a single-particle mobility edge.Phys. Rev. Lett.122,pp. 170403.External Links:DocumentCited by:§I.
- [39]M. Kohmoto(1983)Metal-insulator transition and scaling for incommensurate systems.Phys. Rev. Lett.51,pp. 1198–1201.External Links:DocumentCited by:§I.
- [40]F. K. Kunst, E. Edvardsson, J. C. Budich, and E. J. Bergholtz(2018)Biorthogonal bulk-boundary correspondence in non-hermitian systems.Phys. Rev. Lett.121,pp. 026808.External Links:DocumentCited by:§I.
- [41]Y. Lahini, R. Pugatch, F. Pozzi, M. Sorel, R. Morandotti, N. Davidson, and Y. Silberberg(2009)Observation of a localization transition in quasiperiodic photonic lattices.Phys. Rev. Lett.103,pp. 013901.External Links:DocumentCited by:§I.
- [42]P. A. Lee and T. V. Ramakrishnan(1985)Disordered electronic systems.Rev. Mod. Phys.57,pp. 287–337.External Links:DocumentCited by:§I.
- [43]S. Li and Z. Li(2024)Ring structure in the complex plane: a fingerprint of a non-hermitian mobility edge.Phys. Rev. B110,pp. L041102.External Links:DocumentCited by:§I.
- [44]X. Li, X. Li, and S. Das Sarma(2017)Mobility edges in one-dimensional bichromatic incommensurate potentials.Phys. Rev. B96,pp. 085119.External Links:DocumentCited by:§I.
- [45]Q. Liang, D. Xie, Z. Dong, H. Li, H. Li, B. Gadway, W. Yi, and B. Yan(2022)Dynamic signatures of non-hermitian skin effect and topology in ultracold atoms.Phys. Rev. Lett.129,pp. 070401.External Links:DocumentCited by:§I,§V.
- [46]Q. Lin, T. Li, L. Xiao, K. Wang, W. Yi, and P. Xue(2022)Topological phase transitions and mobility edges in non-hermitian quasicrystals.Phys. Rev. Lett.129,pp. 113601.External Links:DocumentCited by:§I,§V.
- [47]T. Liu, S. Cheng, H. Guo, and G. Xianlong(2021)Fate of Majorana zero modes, exact location of critical states, and unconventional real-complex transition in non-Hermitian quasiperiodic lattices.Phys. Rev. B103,pp. 104203.External Links:DocumentCited by:§I.
- [48]T. Liu, H. Guo, Y. Pu, and S. Longhi(2020)Generalized Aubry-André self-duality and mobility edges in non-hermitian quasiperiodic lattices.Phys. Rev. B102,pp. 024205.External Links:DocumentCited by:§I.
- [49]Y. Liu, X. Jiang, J. Cao, and S. Chen(2020)Non-hermitian mobility edges in one-dimensional quasicrystals with parity-time symmetry.Phys. Rev. B101,pp. 174205.External Links:DocumentCited by:§I.
- [50]Y. Liu, Y. Wang, Z. Zheng, and S. Chen(2021)Exact non-Hermitian mobility edges in one-dimensional quasicrystal lattice with exponentially decaying hopping and its dual lattice.Phys. Rev. B103,pp. 134208.External Links:DocumentCited by:§I.
- [51]Y. Liu, Y. Wang, X. Liu, Q. Zhou, and S. Chen(2021)Exact mobility edges,𝒫​𝒯\mathcal{PT}-symmetry breaking, and skin effect in one-dimensional non-hermitian quasicrystals.Phys. Rev. B103,pp. 014203.External Links:DocumentCited by:§I.
- [52]Y. Liu, Q. Zhou, and S. Chen(2021)Localization transition, spectrum structure, and winding numbers for one-dimensional non-Hermitian quasicrystals.Phys. Rev. B104,pp. 024201.External Links:DocumentCited by:§I.
- [53]S. Longhi(2019)Metal-insulator phase transition in a non-Hermitian Aubry-André-Harper model.Phys. Rev. B100,pp. 125157.External Links:DocumentCited by:§I,§II.
- [54]S. Longhi(2019)Topological phase transition in non-hermitian quasicrystals.Phys. Rev. Lett.122,pp. 237601.External Links:DocumentCited by:Appendix B,Appendix C,§I,§II,§V.
- [55]S. Longhi(2021)Phase transitions in a non-Hermitian Aubry-André-Harper model.Phys. Rev. B103,pp. 054203.External Links:DocumentCited by:§I.
- [56]H. P. Lüschen, S. Scherg, T. Kohlert, M. Schreiber, P. Bordia, X. Li, S. Das Sarma, and I. Bloch(2018)Single-particle mobility edge in a one-dimensional quasiperiodic optical lattice.Phys. Rev. Lett.120,pp. 160404.External Links:DocumentCited by:§I.
- [57]V. M. Martínez Alvarez, J. E. Barrios Vargas, and L. E. F. Foa Torres(2018)Non-hermitian robust edge states in one dimension: anomalous localization and eigenspace condensation at exceptional points.Phys. Rev. B97,pp. 121401(R).External Links:DocumentCited by:§I.
- [58]N. Okuma, K. Kawabata, K. Shiozaki, and M. Sato(2020)Topological origin of non-hermitian skin effects.Phys. Rev. Lett.124,pp. 086801.External Links:DocumentCited by:§I.
- [59]N. Okuma and M. Sato(2023)Non-hermitian topological phenomena: a review.Annu. Rev. Condens. Matter Phys.14,pp. 83–107.External Links:DocumentCited by:§I.
- [60]D. Peng, S. Cheng, and G. Xianlong(2025)Long-range hopping in a quasiperiodic potential weakens the non-hermitian skin effect.Phys. Rev. B111,pp. 094204.External Links:DocumentCited by:§I.
- [61]T. Qian, Y. Gu, and L. Zhou(2024)Correlation-induced phase transitions and mobility edges in an interacting non-hermitian quasicrystal.Phys. Rev. B109,pp. 054204.External Links:DocumentCited by:§I,§V.
- [62]G. Roati, C. D’Errico, L. Fallani, M. Fattori, C. Fort, M. Zaccanti, G. Modugno, M. Modugno, and M. Inguscio(2008)Anderson localization of a non-interacting Bose-Einstein condensate.Nature (London)453,pp. 895–898.External Links:DocumentCited by:§I.
- [63]M. Schreiber, S. S. Hodgman, P. Bordia, H. P. Lüschen, M. H. Fischer, R. Vosk, E. Altman, U. Schneider, and I. Bloch(2015)Observation of many-body localization of interacting fermions in a quasirandom optical lattice.Science349,pp. 842–845.External Links:DocumentCited by:§I.
- [64]A. Szabó and U. Schneider(2018)Non-power-law universality in one-dimensional quasicrystals.Phys. Rev. B98,pp. 134201.External Links:DocumentCited by:§I.
- [65]L. Tang, G. Zhang, L. Zhang, and D. Zhang(2021)Localization and topological transitions in non-hermitian quasiperiodic lattices.Phys. Rev. A103,pp. 033325.External Links:DocumentCited by:§I.
- [66]X. Tong and S. Kou(2024)First-order localization and quantum phase transition induced by quasicrystal imaginary domain.Phys. Rev. Research6,pp. 013314.External Links:DocumentCited by:§I.
- [67]X. Tong, Y. Zhang, B. Li, and X. Yang(2025)Impact of nonreciprocal hopping on localization in non-hermitian quasiperiodic systems.Phys. Rev. B111,pp. 214202.External Links:DocumentCited by:§I.
- [68]D. Vu and S. Das Sarma(2023)Generic mobility edges in several classes of duality-breaking one-dimensional quasiperiodic potentials.Phys. Rev. B107,pp. 224206.External Links:DocumentCited by:Appendix A,§I,§I,§III,§III.
- [69]L. Wang, J. Liu, Z. Wang, and S. Chen(2024)Exact complex mobility edges and flagellate-like spectra for non-hermitian quasicrystals with exponential hoppings.Phys. Rev. B110,pp. 144205.External Links:DocumentCited by:§I.
- [70]Y. Wang, X. Xia, L. Zhang, H. Yao, S. Chen, J. You, Q. Zhou, and X. Liu(2020)One-dimensional quasiperiodic mosaic lattice with exact mobility edges.Phys. Rev. Lett.125,pp. 196604.External Links:DocumentCited by:§I.
- [71]S. Weidemann, M. Kremer, T. Helbig, T. Hofmann, A. Stegmaier, M. Greiter, R. Thomale, and A. Szameit(2020)Topological funneling of light.Science368,pp. 311–314.External Links:DocumentCited by:§I,§V.
- [72]S. Weidemann, M. Kremer, S. Longhi, and A. Szameit(2022)Topological triple phase transition in non-hermitian Floquet quasicrystals.Nature (London)601,pp. 354–359.External Links:DocumentCited by:§I,§V.
- [73]X. Xia, K. Huang, S. Wang, and X. Li(2022)Exact mobility edges in the non-Hermitiant1​–​t2t_{1}\text{--}t_{2}model: theory and possible experimental realizations.Phys. Rev. B105,pp. 014207.External Links:DocumentCited by:§I.
- [74]L. Xiao, T. Deng, K. Wang, G. Zhu, Z. Wang, W. Yi, and P. Xue(2020)Non-hermitian bulk-boundary correspondence in quantum dynamics.Nat. Phys.16,pp. 761–766.External Links:DocumentCited by:§I,§V.
- [75]Z. Xu, X. Xia, and S. Chen(2022)Exact mobility edges and topological phase transition in two-dimensional non-hermitian quasicrystals.Sci. China Phys. Mech. Astron.65,pp. 227211.External Links:DocumentCited by:§I.
- [76]S. Yao and Z. Wang(2018)Edge states and topological invariants of non-hermitian systems.Phys. Rev. Lett.121,pp. 086803.External Links:DocumentCited by:§I.
- [77]K. Yokomizo and S. Murakami(2019)Non-Bloch band theory of non-Hermitian systems.Phys. Rev. Lett.123,pp. 066404.External Links:DocumentCited by:§I.
- [78]Q. Zeng and Y. Xu(2020)Winding numbers and generalized mobility edges in non-hermitian systems.Phys. Rev. Research2,pp. 033052.External Links:DocumentCited by:§I.
- [79]Q. Zeng, Y. Yang, and Y. Xu(2020)Topological phases in non-hermitian Aubry-André-Harper models.Phys. Rev. B101,pp. 020201(R).External Links:DocumentCited by:§I.
- [80]K. Zhang, Z. Yang, and C. Fang(2020)Correspondence between winding numbers and skin modes in non-hermitian systems.Phys. Rev. Lett.125,pp. 126402.External Links:DocumentCited by:§I,§II.
- [81]L. Zhou(2021)Floquet engineering of topological localization transitions and mobility edges in one-dimensional non-hermitian quasicrystals.Phys. Rev. Research3,pp. 033184.External Links:DocumentCited by:§I,§V.


## 


- 


Major funding support from
