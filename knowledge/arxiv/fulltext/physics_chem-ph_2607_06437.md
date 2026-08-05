# An entropic bottleneck, dynamical gating, and outward redistribution of roaming in a designed Chesnavich-type model

**arXiv ID**: 2607.06437v1
**Authors**: Stephen Wiggins
**Published**: 2026-07-07
**Categories**: physics.chem-ph, math.DS
**Comments**: 19 pages, 7 figures
**HTML URL**: https://arxiv.org/html/2607.06437v1

## Abstract

Roaming reactions are organized not by potential-energy saddles but by transition states that are unstable invariant objects in phase space, periodic orbits in the two degrees of freedom studied here. To ask what controls roaming, we modify the Chesnavich model of a barrierless ion--molecule dissociation: its orientation-dependent angular hindrance is replaced by a transverse-stiffness ridge whose angular frequency peaks at an interior radius, and the classical dynamics are studied at a fixed energy just above the dissociation threshold. Comparing two ensembles that differ only in this angular interaction (same radial channel, energy, and inward initial conditions) isolates its effect. The ridge gates entry into the inner well, cutting inner capture from $57\%$ to $15\%$ and returning most of the incoming flux directly to reactants; it does not eliminate roaming but relocates it outward, suppressing it inside the ridge and switching it on farther out. The model retains analogues of the original model's three transition states (tight, free-rotor, and outer orbiting orbits), which we locate as unstable periodic orbits. The tight orbit spans a dividing surface that coincides, within numerical accuracy, with the variational minimum-flux surface, and it carries no barrier along the reaction coordinate: a deep entropic bottleneck placed at an interior radius by the stiffness maximum. Its entropic character is shared with the original model. Strength-matched monotone controls show that the gating tracks the hindrance strength at the bottleneck radius; what the interior maximum supplies is placement, concentrating that strength where it gates most effectively. The trajectories it admits roam nonstatistically, with nonexponential gap-time distributions: the entropic bottleneck governs how much is captured, not the dynamics that follow.

## Full Text

An entropic bottleneck, dynamical gating, and outward redistribution of roaming in a designed Chesnavich-type model

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
- License: CC BY 4.0arXiv:2607.06437v1 [physics.chem-ph] 07 Jul 2026

## An entropic bottleneck, dynamical gating, and outward redistribution
of roaming in a designed Chesnavich-type modelStephen Wiggins
Hetao Institute of Mathematics and Interdisciplinary Sciences, Shenzhen, China
School of Mathematics, University of Bristol, Bristol BS8 1TW, United Kingdom

## Abstract

Roaming reactions are organized not by potential-energy saddles but by transition states that
are unstable invariant objects in phase space, periodic orbits in the two degrees of freedom
studied here. To ask what controls roaming, we modify the
Chesnavich model of a barrierless ion–molecule dissociation: its orientation-dependent angular
hindrance is replaced by a transverse-stiffness ridge whose angular frequency peaks at an
interior radius, and the classical dynamics are studied at a fixed energy just above the
dissociation threshold. Comparing two ensembles that differ only in this angular interaction
(same radial channel, energy, and inward initial conditions) isolates its effect. The ridge
gates entry into the inner well, cutting inner capture from57%57\%to15%15\%and returning most
of the incoming flux directly to reactants; it does not eliminate roaming but relocates it
outward, suppressing it inside the ridge and switching it on farther out. The model retains
analogues of the original model’s three transition states (tight, free-rotor, and outer orbiting
orbits), which we locate as unstable periodic orbits. The tight orbit spans a dividing surface that coincides, within numerical
accuracy, with the variational minimum-flux surface, and it carries no barrier along the reaction
coordinate: a deep entropic
bottleneck placed at an interior radius by the stiffness maximum. Its entropic character is
shared with the original model. Strength-matched monotone controls show that the gating tracks
the hindrance strength at the bottleneck radius; what the interior maximum supplies is placement,
concentrating that strength where it gates most effectively. The trajectories it admits roam
nonstatistically, with nonexponential gap-time
distributions: the entropic bottleneck governs how much is captured, not the dynamics that
follow.

## 1Introduction

## Roaming and entropic transition states.

Conventional transition-state theory places a locally nonrecrossing dividing surface at a
rank-one saddle of the potential energy surface. Two kinds of process fall outside that picture:
barrierless bond fissions, whose transition states must be found variationally because the
potential rises monotonically along the reaction coordinate, and roaming reactions, in which a
partially dissociated fragment executes large-amplitude motion in a flat long-range region and
then reacts or escapes without following the minimum-energy path. Since H-atom roaming was
identified in formaldehyde[1]it has been documented across many systems and is
now recognized as a general feature of gas-phase dynamics[2,3,4,5,6]. For barrierless association and dissociation the
controlling loose transition state is located variationally[11,10],
and its cost is predominantly entropic rather than tied to a saddle. A related but distinct line
of work concerns the “entropic intermediate” of nonstatistical organic dynamics, a free-energy
minimum on a flat region of the surface with long residence times and heavy
recrossing[7]; we treat it here as an adjacent phenomenon rather than the same
physics. In phase space these transition states are not saddles but unstable invariant objects and the
dividing surfaces attached to them: periodic orbits in systems with two degrees of freedom, and
normally hyperbolic invariant manifolds in general[19,18,17]. The model studied
here has two degrees of freedom, so its transition states are periodic orbits, and roaming is
organized by a small set of them.

## Entropy barriers.

That a rate can be controlled by entropy rather than energy is long established: Zhou and
Zwanzig[8]gave a solvable model in which diffusion through a channel of
varying width produces a purely entropic barrier. Most relevant here, Makarov[9]showed that a localized maximum of a transverse frequency along a reaction coordinate generates
an entirely entropic free-energy barrier, one with no potential maximum along the coordinate,
because the constrained free energyF​(x)=V​(x)+kB​T​ln⁡ω⟂​(x)ω0F(x)=V(x)+k_{B}T\ln\frac{\omega_{\perp}(x)}{\omega_{0}}(1)

acquires a maximum wherever the transverse mode stiffens, even whereV​(x)V(x)is flat. Herexxis
the reaction coordinate,V​(x)V(x)the potential along it,ω⟂​(x)\omega_{\perp}(x)the transverse-mode
frequency atxx,ω0\omega_{0}a reference frequency, andkB​Tk_{B}Tthe thermal energy. In the model
studied here the reaction coordinate is the radial separationrrand the transverse mode is the
angular coordinateθ\theta. Makarov further showed that such a barrier is dynamically distinct
from what controls crossing times: transition-path-time statistics can be insensitive to a
barrier that nonetheless dominates the free-energy profile. Both points recur below. The entropic
character of such a bottleneck is not itself new: in a barrierless system any variational
bottleneck is entropic, and the Chesnavich model we build on already has one. What we add is a
deliberately deep entropic bottleneck, placed at an interior radius by an interior maximum of the
transverse stiffness, embedded in a Hamiltonian model of roaming where its dynamical consequences
can be followed.

## The Chesnavich model and the question.

Chesnavich introduced a model Hamiltonian for ion–molecule dissociation to study competition
between multiple transition states[20,21]; its planar,
zero-angular-momentum form is now a standard laboratory for roaming. Mauguière, Collins, Ezra,
Farantos and Wiggins analyzed roaming in it in phase space, identifying the tight and orbiting
transition states with dividing surfaces attached to unstable periodic orbits and associating
roaming with free-rotor orbits born in saddle–center bifurcations[22,23,24,25,26]; Krajňák and
Waalkens, and Krajňák and Wiggins, mapped these structures in detail and across parameter
space[27,28,29,30,31,32]. In that model the tight and orbiting transition
states are tied respectively to the orientation-locking angular hindrance and to the centrifugal
barrier. We ask a dynamical question. If the orientation-locking hindrance is replaced, on the
same barrierless radial channel, by a ridge in the transverse stiffness (an interior maximum of
the angular frequency, with no potential barrier along the channel), how is roaming changed? At
fixed energy, and for the same incoming ensemble, does the ridge promote roaming, suppress it, or
reorganize it? Our central finding is the last: the ridge gates entry into the inner well,
admitting only a small fraction of the incoming flux and returning most of it directly to
reactants, and it does not increase the roaming fraction but displaces it outward, suppressing it
inside the ridge and switching it on farther out.

## Three transition states.

The phase-space account of this behavior rests on three transition states, all unstable periodic
orbits located here at fixed energy: a tight orbit, a free-rotor orbit, and an outer
orbiting orbit. The tight orbit gates entry to the well; the dividing surface it spans coincides with the
variational minimum-flux surface (as verified in Sec.8by comparing the tight-orbit action with the
fixed-radius minimum flux) and carries no potential barrier along the
radial coordinate, so it is a purely entropic bottleneck, made deep and placed at an interior
radius by the transverse-stiffness maximum. The free-rotor orbit sorts direct from roaming
trajectories; the orbiting orbit gates escape to products. The tight orbit is the one the
ridge reshapes: its entropic character it shares with the Chesnavich tight transition state, but
the designed ridge makes it deep enough to control capture. The roaming it admits is
nonstatistical, with nonexponential gap-time distributions: the entropic bottleneck sets how much
is captured, not the fate of what follows.

## Organization.

Section2fixes the classical Chesnavich model. Section3introduces the designed transverse-stiffness model. Section4presents the
central result: two trajectory ensembles compared under identical conditions (same radial
potential, energy, and incoming ensemble), differing only in the angular interaction, so that any
difference in outcome is attributable to that term alone. Sections5,6, and7locate the three transition states, and
Sec.8relates the tight entropic bottleneck to Makarov’s picture.
Section9concludes; computational methods and the gap-time analysis are in
AppendicesAandB.

## 2The classical Chesnavich model

With zero overall angular momentum and planar geometry, Chesnavich’s two-degree-of-freedom (2-DoF) Hamiltonian
is[20,22,30]H=pr22​μ+pθ22​(1ICH3+1μ​r2)+V​(r,θ),H=\frac{p_{r}^{2}}{2\mu}+\frac{p_{\theta}^{2}}{2}\!\left(\frac{1}{I_{\mathrm{CH_{3}}}}+\frac{1}{\mu r^{2}}\right)+V(r,\theta),(2)

whererris the distance from theCH3+\mathrm{CH}_{3}^{+}center of mass to the H atom andθ\thetathe relative orientation. The potential is a barrierless radial channel plus an
orientation-dependent term that hinders free rotation of the fragment, favoring the aligned
geometryθ=0\theta=0and switching off with distance:V​(r,θ)\displaystyle V(r,\theta)=VCH​(r)+12​V0​(r)​[1−cos⁡2​θ],V0​(r)=Ve​e−α​(r−re)2,\displaystyle=V_{\mathrm{CH}}(r)+\tfrac{1}{2}V_{0}(r)\bigl[1-\cos 2\theta\bigr],\qquad V_{0}(r)=V_{e}\,e^{-\alpha(r-r_{e})^{2}},(3)VCH​(r)\displaystyle V_{\mathrm{CH}}(r)=Dec1−6​{2​(3−c2)​ec1​(1−x)−(4​c2−c1​c2+c1)​x−6−(c1−6)​c2​x−4},\displaystyle=\frac{D_{e}}{c_{1}-6}\Bigl\{2(3-c_{2})e^{c_{1}(1-x)}-(4c_{2}-c_{1}c_{2}+c_{1})x^{-6}-(c_{1}-6)c_{2}\,x^{-4}\Bigr\},(4)

withx=r/rex=r/r_{e}. Asrrdecreases andV0​(r)V_{0}(r)grows, this term stiffens and confines the
fragment near alignment; we call it theorientation lock(or Chesnavich lock) for
brevity. The parameters, phenomenological rather than fitted to data, areDe=47D_{e}=47kcal/mol,re=1.1​År_{e}=1.1~\text{\AA },c1=7.37c_{1}=7.37,c2=1.61c_{2}=1.61,Ve=55V_{e}=55kcal/mol,ICH3=2.3734​u​Å2I_{\mathrm{CH_{3}}}=2.3734~\mathrm{u\,\text{\AA }^{2}},μ=0.9445​u\mu=0.9445~\mathrm{u}, andα=1​Å−2\alpha=1~\text{\AA }^{-2}[20,22];
thex−4x^{-4}term is the ion–induced-dipole−1/r4-1/r^{4}tail.

The transition states of this surface, which has two degrees of freedom, are periodic orbits, not saddles. As established by
Mauguière, Collins, Ezra, Farantos and Wiggins and by Krajňák and Waalkens, the orbits
that organize roaming are unstable periodic orbits on a fixed energy shell, none located at a critical
point ofV​(r,θ)V(r,\theta): an inner orientation-locking (tight) orbit whoseperiodic-orbit
dividing surface(PODS), the dividing surface spanned by an unstable periodic orbit, gates
entry to the well; an outer relative-equilibrium orbit on the centrifugal barrier of the
effective radial potentialVCH​(r)+12​pθ2​(1/ICH3+1/μ​r2)V_{\mathrm{CH}}(r)+\tfrac{1}{2}p_{\theta}^{2}\bigl(1/I_{\mathrm{CH_{3}}}+1/\mu r^{2}\bigr)(the orbiting, or loose, transition state) whose PODS gates passage to the radical channel; and
an intermediate free-rotor family whose PODS is used to separate direct from roaming
trajectories[22,27,28].

A single quantity captures how tightly the orientation lock—theangular potential12​V0​(r)​[1−cos⁡2​θ]\tfrac{1}{2}V_{0}(r)[1-\cos 2\theta]—confines the fragment at each radius: theharmonic
transverse frequency. The transverse degree of freedom is the angular coordinateθ\theta,
transverse to the radial reaction coordinaterr, and near the aligned geometryθ=0\theta=0it
behaves like a vibration. Expanding the angular potential aboutθ=0\theta=0gives12​V0​(r)​[1−cos⁡2​θ]≃V0​(r)​θ2\tfrac{1}{2}V_{0}(r)[1-\cos 2\theta]\simeq V_{0}(r)\,\theta^{2},
a harmonic well whosecurvature—the second derivative inθ\theta, that is, the angular
force constant—is2​V0​(r)2V_{0}(r). The matching kinetic term in Eq. (2) is12​(1/ICH3+1/μ​r2)​pθ2\tfrac{1}{2}\bigl(1/I_{\mathrm{CH_{3}}}+1/\mu r^{2}\bigr)p_{\theta}^{2}, so the effective angular mass is(1/ICH3+1/μ​r2)−1\bigl(1/I_{\mathrm{CH_{3}}}+1/\mu r^{2}\bigr)^{-1}. A harmonic oscillator has frequencyforce constant/mass\sqrt{\text{force constant}/\text{mass}}, which here isΩCh​(r)=2​V0​(r)​(1ICH3+1μ​r2).\Omega_{\mathrm{Ch}}(r)=\sqrt{2V_{0}(r)\Bigl(\tfrac{1}{I_{\mathrm{CH_{3}}}}+\tfrac{1}{\mu r^{2}}\Bigr)}.(5)

It is a local measure of orientational stiffness: the larger it is, the more sharply the fragment
is held near alignment. Why a large transverse frequency should impede the reaction even where the
radial potential is flat is the mechanism we build the next section around; here we note only its
shape. SinceV0​(r)=Ve​e−α​(r−re)2V_{0}(r)=V_{e}\,e^{-\alpha(r-r_{e})^{2}}falls off monotonically forr>rer>r_{e}, so doesΩCh​(r)\Omega_{\mathrm{Ch}}(r), which might suggest that the channel has no interior flux minimum.
It does have one. The harmonic frequency omits both
therr-dependence of the available channel energy and the anharmonicity of the hindered rotor, and
the exact radial-surface flux computed in Sec.5has a genuine, if shallow, interior
minimum on the Chesnavich surface. The Chesnavich model therefore does possess an entropic
bottleneck; it is shallow, and arises mainly from the radial variation of channel energy together
with the angular dynamics rather than from a maximum of transverse stiffness.

## 3The designed transverse-stiffness model

We keep the kinetic energy of the Chesnavich model unchanged (the same reduced mass, moment of
inertia, andrr-dependent angular massa​(r)a(r)) and keep its long-range attraction (the
ion–induced-dipole−1/r4-1/r^{4}tail), but replace the orientation lock by a localized
transverse-stiffness ridge that wedesign, that is, construct by hand to have a prescribed
property rather than fit to a real molecule: a single interior maximum of the transverse
stiffness. The transverse stiffness is the strength of the angular restoring force, measured by
the harmonic transverse frequencyΩ​(r)\Omega(r); a stiffer transverse mode (largerΩ\Omega)
confines the angular motion more tightly. The designed Hamiltonian isH=pr22​μ+12​a​(r)​pθ2+Vrad​(r)+12​B​(r)​[1−cos⁡2​θ],a​(r)=1ICH3+1μ​r2,H=\frac{p_{r}^{2}}{2\mu}+\tfrac{1}{2}a(r)\,p_{\theta}^{2}+V_{\mathrm{rad}}(r)+\tfrac{1}{2}B(r)\bigl[1-\cos 2\theta\bigr],\qquad a(r)=\frac{1}{I_{\mathrm{CH_{3}}}}+\frac{1}{\mu r^{2}},(6)

in which the angular potential’s prefactorB​(r)B(r)—its strength as a function ofrr—is a
localized Gaussian bump centered at an interior radiusrcr_{c},B​(r)=12​a​(r)−1​Ω02​e−(r−rc)2/σ2.B(r)=\tfrac{1}{2}\,a(r)^{-1}\,\Omega_{0}^{2}\,e^{-(r-r_{c})^{2}/\sigma^{2}}.(7)

By the small-oscillation argument of Sec.2, now with the ridge amplitudeB​(r)B(r)in place of the lock amplitudeV0​(r)V_{0}(r)anda​(r)a(r)the kinetic coefficient of
Eq. (6), the harmonic transverse frequency aboutθ=0\theta=0isΩ​(r)=2​B​(r)​a​(r)=Ω0​e−(r−rc)2/2​σ2.\Omega(r)=\sqrt{2\,B(r)\,a(r)}=\Omega_{0}\,e^{-(r-r_{c})^{2}/2\sigma^{2}}.(8)

The factora​(r)−1a(r)^{-1}inB​(r)B(r)is chosen precisely to cancel therr-dependence of the angular
mass, so thatΩ​(r)\Omega(r)is an exact Gaussian with a single smooth interior maximum atr=rcr=r_{c}(Fig.1c), in contrast to the monotoneΩCh​(r)\Omega_{\mathrm{Ch}}(r)of the
Chesnavich lock.

Why an interior maximum ofΩ​(r)\Omega(r)acts as a bottleneck is Makarov’s
observation[9], Eq. (1), restated here for the angular mode.
The angular motion is fast compared with the radial approach, so at eachrrit completes many
oscillations whilerrbarely changes, and one may remove it by averaging. Removing a degree of
freedom in equilibrium statistical mechanics means replacing it by its partition
function—a sum over the states it can occupy—and paying a free-energy cost−kB​T​ln⁡(that sum)-k_{B}T\ln(\text{that sum}). For a harmonic mode of frequencyΩ​(r)\Omega(r)the classical
transverse partition function, overθ\thetaandpθp_{\theta}together, isZ⟂​(r)=kB​T/ℏ​Ω​(r)Z_{\perp}(r)=k_{B}T/\hbar\Omega(r), so the free energy alongrrbecomesG​(r)=Vrad​(r)−kB​T​ln⁡Z⟂​(r)=Vrad​(r)+kB​T​ln⁡Ω​(r)+const,G(r)=V_{\mathrm{rad}}(r)-k_{B}T\ln Z_{\perp}(r)=V_{\mathrm{rad}}(r)+k_{B}T\ln\Omega(r)+\text{const},(9)

which is Eq. (1) with the angular coordinate playing the role of the transverse
mode (the constant absorbs the reference frequencyω0\omega_{0}). The added term is entropic, not
energetic:Ω\Omegaenters only throughZ⟂Z_{\perp}, the number of accessible angular states, and
not through the energy of any configuration. A stiffer angular spring (largerΩ\Omega) holds the
fragment in a narrower cone about alignment, so fewer orientations are accessible; fewer
accessible states mean lower entropy and therefore higher free energy. At fixed energy the same
statement reads: the number of transverse states below a transverse energyE⟂E_{\perp}scales asE⟂/ΩE_{\perp}/\Omega, so a stiffer mode has fewer of them[9,11]. WhereverΩ​(r)\Omega(r)is largest,G​(r)G(r)is highest.

The lock and the ridge run through thesamefrequency formula,Ω=2​A​(r)​a​(r)\Omega=\sqrt{2A(r)\,a(r)}, differing only in the angular amplitudeA​(r)A(r):A=V0​(r)A=V_{0}(r)for the
Chesnavich lock andA=B​(r)A=B(r)for the designed ridge. For the lockV0​(r)V_{0}(r)falls off
monotonically, soΩCh\Omega_{\mathrm{Ch}}and its free-energy termkB​T​ln⁡ΩChk_{B}T\ln\Omega_{\mathrm{Ch}}decrease monotonically withrr: by this mechanism alone the lock cannot place a bottleneck in the
interior. For the ridgeΩ​(r)\Omega(r)peaks atrcr_{c}[Eq. (8)], sokB​T​ln⁡Ωk_{B}T\ln\Omegapeaks there too—an entropic bottleneck placed in the interior by design, even thoughVrad​(r)V_{\mathrm{rad}}(r)has no barrier there. This is Makarov’s transverse-stiffening mechanism
built into the angular coordinate of a roaming model. The price is a larger angular amplitude:B​(r)B(r)reaches∼156\sim 156kcal/mol atrcr_{c}, against∼16\sim 16kcal/mol forV0​(rc)V_{0}(r_{c})(Fig.1b).

This canonicalkB​T​ln⁡Ωk_{B}T\ln\Omegais a heuristic: we work at fixed energy, not in a thermal bath, so
the quantity we actually compute is its microcanonical counterpart, the exact transverse flux
through a surface at radiusRR, whose interior minimum plays the role of the free-energy maximum
(Sec.5). The contrast with the lock is one of mechanism, not of outcome: the
Chesnavich model does still have a shallow interior bottleneck, but—as Sec.5shows—it comes chiefly from the way the energy available to the angular mode varies withrr,
together with the full hindered-rotor dynamics, not from a maximum of transverse stiffness. Our
ridge places the bottleneck directly, through the stiffness itself.

For the radial channel we use either the ChesnavichVCH​(r)V_{\mathrm{CH}}(r)or a Lennard-Jones LJ(8,4) form, both decaying as−1/r4-1/r^{4}at long range,VLJ​(r)=De​[(re/r)8−2​(re/r)4].V_{\mathrm{LJ}}(r)=D_{e}\Bigl[(r_{e}/r)^{8}-2(r_{e}/r)^{4}\Bigr].(10)

We use the near-identity of the results under this substitution (Sec.4) to
establish that the gating is produced by the angular ridge and is insensitive to the shape of the
barrierless radial channel: with the long-range tail and the angular term held fixed, replacingVCH​(r)V_{\mathrm{CH}}(r)byVLJ​(r)V_{\mathrm{LJ}}(r)leaves the inner-capture drop essentially unchanged.
The ridge itself is radially localized atrcr_{c}; what the substitution rules out is a dependence
on the detailed shape of the radial channel potential, not radial structure as such. The model
parameters are listed in Table1.Table 1:Parameters of the designed model, Eqs. (6)–(10). The
“sharp ridge” values are used throughout unless stated otherwise. Energies in kcal/mol,
lengths in Å, masses in u.quantitysymbolvaluereduced massμ\mu0.94450.9445CH3\mathrm{CH_{3}}moment of inertiaICH3I_{\mathrm{CH_{3}}}2.37342.3734well depth / tail scaleDe,reD_{e},\ r_{e}47,1.147,\ 1.1Chesnavich shape constantsc1,c2c_{1},c_{2}7.37,1.617.37,\ 1.61Chesnavich lock height / widthVe,αV_{e},\ \alpha55,155,\ 1ridge peak frequency squaredΩ02\Omega_{0}^{2}200200ridge center / widthrc,σr_{c},\ \sigma2.2,0.52.2,\ 0.5roaming energyEE22Figure 1:Construction of the designed model. (a) The two barrierless radial channels,VCH​(r)V_{\mathrm{CH}}(r)and the LJ(8,4) form; neither has a radial barrier along the approach, and
both decay as−1/r4-1/r^{4}at long range. (b) Angular hindrance amplitude versusrr: the monotone
Chesnavich lockV0​(r)V_{0}(r)(α=1\alpha=1) and the entropic ridgeB​(r)B(r), taller and concentrated
nearrc=2.2​År_{c}=2.2~\text{\AA }. (c) Harmonic transverse frequency:ΩCh​(r)\Omega_{\mathrm{Ch}}(r)decreases
monotonically, whereas the designedΩ​(r)\Omega(r)has a single interior maximum atrcr_{c}.

## 4The entropic ridge gates inner capture and displaces roaming outward

The model was built to ask a dynamical question, and we answer it first, before locating the
phase-space structures that explain the answer. The question is what the localized entropic
ridge does to roamingrelative tothe orientation-locking interaction of the original
Chesnavich surface. We answer it with a controlled comparison in which everything but the
angular interaction is held fixed. We fix the radial channel at the Chesnavich potentialVCH​(r)V_{\mathrm{CH}}(r), fix the energyE=2E=2, and fix the incoming fixed-energy ensemble; the
only difference between the two runs is the angular term, the Chesnavich lock12​V0​(r)​[1−cos⁡2​θ]\tfrac{1}{2}V_{0}(r)[1-\cos 2\theta]in one and the entropic ridge12​B​(r)​[1−cos⁡2​θ]\tfrac{1}{2}B(r)[1-\cos 2\theta]in
the other. The ensemble is a240×240240\times 240grid in(θ0,pθ,0)(\theta_{0},p_{\theta,0})launched inward
fromr0=6​År_{0}=6~\text{\AA }at fixedEE, with the inward radial momentum fixed by the energy constraint
and energetically inaccessible launch points removed; a trajectory is counted as reaching the
well if it crossesr<1.6​År<1.6~\text{\AA }, and the integrator and ensemble are documented in
AppendixA. This is the dynamical counterpart of the matched control at the
level of the flux (Sec.5), where the same ridge is placed onVCH​(r)V_{\mathrm{CH}}(r)at the level of the exact directional flux; here we compare its trajectory consequences against
the lock at fixed radial energetics.

## What changes.

Figure2reports the comparison, and two effects are large and unambiguous.
First, the ridgegates entry into the inner well: entry into the well
(r<1.6​År<1.6~\text{\AA }) falls from57.3%57.3\%under the monotone lock to14.7%14.7\%under the ridge, and the
fraction of the ensemble returned directly to the outer region without entering the well rises
correspondingly from37.4%37.4\%to80.3%80.3\%(Fig.2a). The mechanism is visible
in the penetration profile (Fig.2c): the monotone lock funnels incoming
trajectories towardθ=0\theta=0and into the well, so the cumulative penetrationP​(rmin<r)P(r_{\min}<r)rises steadily; the ridge instead reflects all but a narrow channel nearθ=0\theta=0, andP​(rmin<r)P(r_{\min}<r)is gated sharply just outsidercr_{c}. Second, the ridgedoes not increase the roaming fraction; itdisplaces the roaming fraction outward, where the roaming fraction counts
trajectories that cross the classifier radius three or more times, in either direction, before
reacting or escaping. At the
classifier radiusrclass=3.5​År_{\mathrm{class}}=3.5~\text{\AA }the roaming (nonreactive) fraction is
essentially unchanged,5.3%→4.9%5.3\%\to 4.9\%. But the radial profile of the statistic changes
qualitatively (Fig.2b): under the monotone lock repeated crossings are already
present at smaller radii and decay quickly outward; under the ridge they are suppressed insidercr_{c}, switch on sharply just beyond it, and persist to larger radii, exceeding the lock’s curve
at every radius beyond∼3.8​Å\sim 3.8~\text{\AA }. The two runs agree closely when the LJ(8,4) channel is
substituted forVCH​(r)V_{\mathrm{CH}}(r)(inner capture57.3%/15.1%57.3\%/15.1\%, within1%1\%), confirming
that the effect is carried by the angular interaction and not by the radial form.

## What this is, and what it is not.

The result carries four qualifications.(i) “Reactive” means entry into the well, not committed product.A trajectory is counted as reactive if its closest approach reachesr<1.6​År<1.6~\text{\AA }. The flow is
volume-preserving and the well is not an attractor, so this denotes entry into the molecular
well, not a committed product yield: a captured trajectory may recross and redissociate. The
gating result is a statement about inner-well capture (AppendixA), and the same
definition is used for the classifier ensemble of Sec.7.(ii) Amplitude and localization, separated by a control.The two angular interactions differ inamplitudeas well as in radial profile: the
ridge reaches∼156\sim 156kcal/mol atrcr_{c}, against∼16\sim 16kcal/mol for the lock at the same
radius. To separate the two effects we ran strength-matched monotone controls: the same lock
formVe​e−(r−re)2V_{e}\,e^{-(r-r_{e})^{2}}withVeV_{e}raised, on the same channel and ensemble. Capture falls
monotonically with the hindrance strength at the bottleneck radius,V0​(rc)V_{0}(r_{c}): raising it from
the standard16.416.4to46.546.5,8080, and156156kcal/mol gives capture57.3%57.3\%,33.0%33.0\%,24.9%24.9\%, and17.8%17.8\%. Thercr_{c}-matched monotone lock (V0​(rc)=156V_{0}(r_{c})=156, requiringVe=523V_{e}=523)
also displaces roaming outward much as the ridge does (switching on near3.8​Å3.8~\text{\AA }), and its
capture transfers between radial channels (17.8%17.8\%on bothVCHV_{\mathrm{CH}}and LJ). Both
headline effects therefore follow from strong orientational hindrance in the region of the
bottleneck radius and are not unique to an interior maximum. What the interior maximum supplies
is placement and economy: it concentrates the hindrance at the gating radius, so the ridge gates
far more effectively than a monotone profile of equal global peak strength (14.7%14.7\%against33.0%33.0\%) and does so without imposing a very large hindrance at all smaller radii; the residual
difference between the ridge and thercr_{c}-matched control (14.7%14.7\%against17.8%17.8\%) is the
contribution of the localized profile itself.(iii) The roaming fraction is parameter-dependent; the redistribution is not.The roaming fraction is sensitive to the Chesnavich switching parameterα\alpha. For the
early-switching lock (α=4\alpha=4), whose hindrance has all but vanished byr≃2​År\simeq 2~\text{\AA },
almost the entire incoming ensemble is captured (∼99.9%\sim 99.9\%) and the baseline roaming
fraction is tiny (∼0.2%\sim 0.2\%); against that baseline the ridge both reduces capture andincreasesthe measured roaming fraction. It would therefore be misleading to speak of
“the” roaming fraction of the Chesnavich model. The robust result, common toα=1\alpha=1andα=4\alpha=4, is the inner-well gating; the outward redistribution is demonstrated explicitly
for theα=1\alpha=1comparison through the full classifier-radius sweep of
Fig.2b, while the raw roaming percentage at any single classifier radius
changes strongly withα\alpha.(iv) This is conditional-on-entry intermediate dynamics.The launch surfacer0=6​År_{0}=6~\text{\AA }liesinsidethe outer orbiting transition state
(rOTS≃7.48​År_{\mathrm{OTS}}\simeq 7.48~\text{\AA }, Sec.6); this is a comparison of
intermediate-region dynamics conditional on inward entry, not a complete reactant-to-product
scattering calculation.Figure 2:The controlled comparison atE=2E=2. The radial channelVCH​(r)V_{\mathrm{CH}}(r), the
energy, and the inward fixed-energy ensemble are identical in the two runs; only the angular
term differs, set to the Chesnavich lock (the orientation-locking term of the original model)
in one and to the entropic ridge (the localized transverse-stiffness maximum atrcr_{c}) in the
other. (a) Inner-capture outcome: the ensemble partitioned into inner capture (entry tor<1.6​År<1.6~\text{\AA }), roaming nonreactive, and direct nonreactive. The ridge cuts inner capture from57.3%57.3\%to14.7%14.7\%and raises direct nonreactive return from37.4%37.4\%to80.3%80.3\%, while the
roaming (nonreactive) fraction is nearly unchanged (5.3%→4.9%5.3\%\to 4.9\%). (b) The roaming fraction versus classifier radius: under the ridge it is suppressed insidercr_{c},
switches on beyond it, and persists farther out than under the lock, crossing above the lock’s
curve beyond∼3.8​Å\sim 3.8~\text{\AA }. The variational bottleneckr∗=2.47​År^{*}=2.47~\text{\AA }for this channel is
marked. (c) Cumulative inner penetrationP​(rmin<r)P(r_{\min}<r): the lock funnels trajectories into the
well; the ridge gates them just outsidercr_{c}.

The remaining sections locate the phase-space structures that explain this behavior: a
variational flux bottleneck just outside the ridge, an invariant dynamical transition state far
outside it, and a classifier between the two that tracks neither.

## 5The variational flux bottleneck

The statistical bottleneck is the dividing surface spanned by the tight orbit. For a radial dividing surfacer=Rr=Rat energyEE, the exact fixed-energy directional flux is[19]ΦR​(E)=∮02​π2​2​[ε​(R)−Uang​(R,θ)]+a​(R)​𝑑θ,ε​(R)=E−Vrad​(R),\Phi_{R}(E)=\oint_{0}^{2\pi}\!2\sqrt{\frac{2\,[\,\varepsilon(R)-U_{\mathrm{ang}}(R,\theta)\,]_{+}}{a(R)}}\,d\theta,\qquad\varepsilon(R)=E-V_{\mathrm{rad}}(R),(11)

withUang​(R,θ)=12​B​(R)​[1−cos⁡2​θ]U_{\mathrm{ang}}(R,\theta)=\tfrac{1}{2}B(R)[1-\cos 2\theta]and[⋅]+[\cdot]_{+}the positive
part;ΦR​(E)\Phi_{R}(E)is the area of the transverse (angular) phase space(θ,pθ)(\theta,p_{\theta}), on
the energy shell atr=Rr=R, that is energetically able to cross outward. The variational
bottleneckr∗r^{*}minimizesΦR​(E)\Phi_{R}(E)overRR[11,13,14];
we work at fixed energy throughout, andr∗r^{*}is the fixed-energy analogue of the maximum of
the canonical constrained free energy of Eq. (1), which is why we describe it as
entropic. We also define the angular confinement factorC​(R,E)=ΦR​(E)ΦRfree​(E),ΦRfree​(E)=2​π⋅2​2​ε​(R)/a​(R),C(R,E)=\frac{\Phi_{R}(E)}{\Phi_{R}^{\mathrm{free}}(E)},\qquad\Phi_{R}^{\mathrm{free}}(E)=2\pi\cdot 2\sqrt{2\,\varepsilon(R)/a(R)},(12)

the fraction of the free-rotor transverse phase space that remains accessible; normalizing a
hindered quantity by its free-rotor value follows the hindered-rotor treatment of Pitzer and
Gwinn[12].

Figure3reports these quantities atE=2E=2. The designed model has a deep, narrow
flux minimum atr∗≃2.46​År^{*}\simeq 2.46~\text{\AA }(designed channel), withΦR∗/Φ∞≃0.15\Phi_{R^{*}}/\Phi_{\infty}\simeq 0.15and confinementC≃0.10C\simeq 0.10: a deep entropic bottleneck on an otherwise barrierless
channel, in the sense that only about a tenth of the free transverse phase space still crosses
(C≃0.10C\simeq 0.10). The Chesnavich surface, by contrast, has only a shallow interior minimum atr∗≃2.24​År^{*}\simeq 2.24~\text{\AA }withC≃0.35C\simeq 0.35, confirming the point of Sec.2that the Chesnavich channeldoespossess an entropic bottleneck, but a weak one. The
matched control at the level of the flux (the ridge placed on the Chesnavich channelVCH​(r)V_{\mathrm{CH}}(r)) reproduces the deep constriction almost exactly (r∗≃2.47​År^{*}\simeq 2.47~\text{\AA },C≃0.10C\simeq 0.10; dashed curve in Fig.3b), demonstrating that the deep statistical
bottleneck is produced by the designed transverse stiffness and transfers between radial
channels. The same designed transverse stiffness produces both this deep flux minimum and the
dynamical gating of Sec.4, at their respective radii.

Two features deserve emphasis. First, the flux minimum is genuinely entropic: there is no
radial potential barrier along the channel (Fig.1a), so the constriction
is entirely an effect of angular confinement, the reduction of the accessible transverse phase
space toC≃0.10C\simeq 0.10, not of any radial potential barrier. Second, the flux minimumr∗≃2.46​År^{*}\simeq 2.46~\text{\AA }doesnotcoincide with the maximum of the
designed transverse stiffness atrc=2.20​År_{c}=2.20~\text{\AA }; it sits a little outside it. The decomposition in
Fig.3c shows why: the harmonic approximation1/Ω​(R)1/\Omega(R)is minimized atrcr_{c}, but
the exact flux carries the additional factor of available channel energyε​(R)\varepsilon(R), which
rises withRRalong the attractive channel and shifts the true minimum outward. The surface that
actually constricts the flux is therefore this radius, a little outside the stiffness maximum.Figure 3:The variational flux bottleneck atE=2E=2. (a) Exact directional fluxΦR/Φ∞\Phi_{R}/\Phi_{\infty}, Eq. (11), for the designed (LJ+ridge) and Chesnavich
surfaces; the designed model has a deep, narrow minimum where the Chesnavich surface has only
a shallow one. (b) Angular confinementC​(R,E)C(R,E), Eq. (12): the designed
constriction (C≃0.10C\simeq 0.10) is reproduced by the matched control (ridge on the Chesnavich
channel, dashed), well below the Chesnavich value (C≃0.35C\simeq 0.35). (c) Decomposition of the
designed-model flux: the harmonic approximation1/Ω1/\Omegais minimized atrc=2.20​År_{c}=2.20~\text{\AA }, but
the exact flux minimum sits atr∗=2.46​År^{*}=2.46~\text{\AA }because the available channel energyε​(R)/Ω\varepsilon(R)/\Omegashifts it outward.

## 6The dynamical transition-state structure

The designed model’s three transition states are all unstable periodic orbits, located atE=2E=2and shown in Fig.4: the tight orbit atr∗≃2.46​År^{*}\simeq 2.46~\text{\AA }, a libration of±12∘\pm 12^{\circ}about the aligned axis, at the flux-minimum radius of Sec.5; the
free-rotor orbit over3.53.5–3.7​Å3.7~\text{\AA }, used to classify roaming in Sec.7; and the
outer orbiting orbit atrOTS=7.48​År_{\mathrm{OTS}}=7.48~\text{\AA }. This section locates the last of these.Figure 4:The three transition states of the designed model atE=2E=2, all unstable periodic orbits,
in the configuration plane(x,y)=(r​cos⁡θ,r​sin⁡θ)(x,y)=(r\cos\theta,r\sin\theta). (a) All three: the orbiting orbit
(circle,rOTS=7.48​År_{\mathrm{OTS}}=7.48~\text{\AA }), the free-rotor orbit (loop,r∈[3.5,3.7]​År\in[3.5,3.7]~\text{\AA }), and the
tight orbit (short arc near the aligned axis,r∗≃2.46​År^{*}\simeq 2.46~\text{\AA }; itsθ=π\theta=\pimirror is
shown faintly). (b) The inner region: the tight orbit is a libration of±12∘\pm 12^{\circ}about the
aligned axis at the flux minimumr∗r^{*}, where the radial channel is barrierless; the free-rotor
orbit is a rotation. The ridge centerrc=2.2​År_{c}=2.2~\text{\AA }is marked in both panels. (c) The
fixed-radius directional flux per aligned window,ΦR/2\Phi_{R}/2, against the action∮p​𝑑q=2.902\oint p\,dq=2.902of the tight orbit (dashed line): the minimum,2.9072.907atR∗R^{*}, agrees with
the orbit’s dividing-surface flux to0.15%0.15\%.

The invariant phase-space object is the outer orbiting transition state that
gates escape. The long-range tail supports an orbiting relative equilibrium on the centrifugal
barrier of the rotationally averaged effective radial potentialVeff​(r;L)=Vrad​(r)+12​L2​a​(r)+12​B​(r)V_{\mathrm{eff}}(r;L)=V_{\mathrm{rad}}(r)+\tfrac{1}{2}L^{2}a(r)+\tfrac{1}{2}B(r).
Figure5shows that atE=2E=2this potential has a barrier maximum atrOTS≃7.48​År_{\mathrm{OTS}}\simeq 7.48~\text{\AA }with angular momentumL=pθ=3.047L=p_{\theta}=3.047, the internal rotational momentum (the total angular momentum is zero); the maximum has negative
radial curvature, so the orbit is unstable. The full model is not globally rotationally
symmetric whenB≠0B\neq 0, so rotational averaging does not in general define an exact orbit; here,
however, the ridge is negligible at this radius (B​(rOTS)∼10−47B(r_{\mathrm{OTS}})\sim 10^{-47}), so
rotational averaging is exact to numerical precision and this is the asymptotic orbiting relative
equilibrium. The orbiting transition state is the standard centrifugal (Langevin) barrier,
produced by the centrifugal term12​L2​a​(r)\tfrac{1}{2}L^{2}a(r)against the−1/r4-1/r^{4}attraction with no
contribution from the ridge. The dividing surface attached to it is defined at this energy and
angular momentum (E=2E=2,L=3.047L=3.047); it is not a fixed radius crossed by every trajectory, since
the orbiting-barrier location depends on angular momentum. We do not launch trajectories from
this surface: the inward ensemble of Sec.7starts atr0=6​År_{0}=6~\text{\AA }, insiderOTSr_{\mathrm{OTS}}, and its largest angular momentum equalsL=3.047L=3.047, so the launch grid is
bounded in angular momentum by the orbiting transition state while lying radially inside it.

This is the second of the three radii. The dynamical transition state that gates escape, the
orbiting orbit atrOTS≃7.48​År_{\mathrm{OTS}}\simeq 7.48~\text{\AA }, lies well outside the variational flux
bottleneckr∗≃2.46​År^{*}\simeq 2.46~\text{\AA }. These are different physical objects, an inner entropic
constriction and an outer centrifugal escape barrier, so their separation is expected; the
substantive point, completed in Sec.8, is that neither coincides with the
classifier, and no single radius summarizes the dynamics.Figure 5:The outer orbiting transition state of the designed model (LJ(8,4) channel).
Outer-region effective radial potentialVeff​(r;L)V_{\mathrm{eff}}(r;L)atE=2E=2: atL=3.047L=3.047the
orbiting transition state is the unstable centrifugal barrier maximum atrOTS=7.48​År_{\mathrm{OTS}}=7.48~\text{\AA }. The ridge is negligible in this region, so the orbiting transition
state is the standard centrifugal (Langevin) barrier.

## 7The roaming classifier

Mauguière, Collins, Ezra, Farantos and Wiggins constructed phase-space dividing surfaces from
the periodic orbits of the Chesnavich model and classified trajectories by how many times they
cross them[22]. Krajňák and Waalkens computed the stable and unstable
manifolds of those orbits and described the transport through their lobes[27];
Krajňák and Wiggins obtained the same structures with Lagrangian descriptors, computationally
simpler than the manifold construction[28]. We adopt their distinction between
direct and roaming trajectories. In the phase-space picture the surface that draws this distinction
is the free-rotor periodic-orbit dividing surface; in the designed model atE=2E=2this is a genuine
hyperbolic orbit, a rotational orbit oscillating radially overr∈[3.52,3.68]​År\in[3.52,3.68]~\text{\AA }, and we count
crossings of a surface of fixed radiusrclass=3.5​År_{\mathrm{class}}=3.5~\text{\AA }, at its inner turning point, as
a practical stand-in.

For the classifier analysis below we use the LJ(8,4) radial channel, for which the inner-capture
fractions quoted in Sec.4are57.3%57.3\%and15.1%15.1\%. We integrate the inward
ensemble of Sec.4, here on this channel, and classify each trajectory two ways.
A trajectory isreactiveif its closest approach reaches the well (r<1.6​År<1.6~\text{\AA }) andnonreactiveotherwise; it isroamingif it crossesrclassr_{\mathrm{class}}three or more
times, in either direction, before escaping, anddirectotherwise. This differs from the
original scheme in one respect: there the crossing count alone carries both roaming and reactivity,
through the opposite crossing parity of trajectories ending inside versus outside; we read
reactivity directly from the closest approach and use a single crossing threshold for roaming. The
four combinations are direct-reactive, direct-nonreactive, roaming-reactive, and roaming-nonreactive.
Trajectories are integrated to escape or to the time limit, and are not stopped at the well; the two
roaming classes therefore come from the same calculation.

Passing both angular interactions through this classifier on the same radial channel isolates what
the ridge does. Under the ridge the ensemble divides into14.9%14.9\%direct-reactive,78.9%78.9\%direct-nonreactive,6.0%6.0\%roaming-nonreactive, and0.13%0.13\%roaming-reactive; under the lock, into55.7%55.7\%,36.8%36.8\%,6.0%6.0\%, and1.6%1.6\%. The total reactive fraction,57.3%57.3\%for the lock and15.1%15.1\%for the ridge, reproduces the LJ-channel inner-capture numbers quoted in Sec.4, since
reaching the well is the event scored there; the classifier and the capture partition are two
readings of one calculation. The roaming fraction is comparable between the two models (7.6%7.6\%for
the lock,6.2%6.2\%for the ridge at3.5​Å3.5~\text{\AA }), but its radial location is not: under the lock roaming
already appears at smaller radii (1.6%1.6\%at2.5​Å2.5~\text{\AA }, rising to7.6%7.6\%by3.0​Å3.0~\text{\AA }), whereas under
the ridge it is negligible inside3.0​Å3.0~\text{\AA }(below0.2%0.2\%) and switches on sharply near3.5​Å3.5~\text{\AA }(Fig.2b). The ridge does not suppress roaming; it displaces it outward, to just
beyond the stiffness maximum.

Whether the intermediate dynamics is statistical is tested by the gap time, the residence time
between entering and leaving the interaction region: a statistical (Rice–Ramsperger–Kassel–Marcus, RRKM) population decays as a
single exponential, so any departure from one shows that a single rate through the bottleneck does
not capture the dynamics. The distribution is non-exponential for both the lock and the ridge
(AppendixB), consistent with the nonstatistical roaming region found by Mauguière,
Collins, Ezra, Farantos and Wiggins[22,15,16].

The classifier radius is not sharply determined: the roaming fraction againstrclassr_{\mathrm{class}}has a broad maximum near3.43.4–3.5​Å3.5~\text{\AA }, so radii across that range classify almost identically, and
we take3.5​Å3.5~\text{\AA }as representative. Figure6b shows the corresponding LJ(8,4)-channel roaming fraction over the full
radial range, together with the flux minimumr∗r^{*}, the ridge
region, and the orbiting radiusrOTSr_{\mathrm{OTS}}, to place the classifier radius among the
transition-state radii. Figure6a shows the launch grid colored by class. The reactive trajectories fall into bands, centrifugal-trapping
bands separated by thin roaming sets, whose arrangement can be fractal[33]. A
separate inner feature near2​Å2~\text{\AA }comes from trajectories oscillating in the inner region, inside
the ridge but above1.6​Å1.6~\text{\AA }, so never reaching the well, and is not outer roaming. Toward large
radius the roaming fraction dies out as trajectories escape past the orbiting orbit atrOTS=7.48​År_{\mathrm{OTS}}=7.48~\text{\AA }.Figure 6:Roaming on the designed surface atE=2E=2(LJ(8,4) channel;240×240240\times 240inward grid atr0=6​År_{0}=6~\text{\AA }). (a) Launch grid(θ0,pθ,0)(\theta_{0},p_{\theta,0})colored by trajectory class: reactive
trajectories form centrifugal-trapping bands, roaming sets are thin, and most trajectories are
direct and nonreactive. The classification is that of the non-absorbing run, in which a small
roaming-reactive class appears. (b) Roaming fraction versus classifier radiusrclassr_{\mathrm{class}}:
suppressed inside the ridge (shaded), switching on near3.5​Å3.5~\text{\AA }, and decaying toward zero past the
orbiting radiusrOTS=7.48​År_{\mathrm{OTS}}=7.48~\text{\AA }. The flux minimumr∗=2.46​År^{*}=2.46~\text{\AA }and the orbiting
radius are marked; the classifier radius is where this statistic is maximal, not a periodic-orbit
dividing surface.

## 8The tight transition state

The designed model carries analogues of the three transition states that organize the Chesnavich model, all
of them unstable periodic orbits located here atE=2E=2: the tight orbit atr≃2.46​År\simeq 2.46~\text{\AA }, the
free-rotor orbit spanning3.523.52–3.68​Å3.68~\text{\AA }, and the orbiting orbit atrOTS=7.48​År_{\mathrm{OTS}}=7.48~\text{\AA },
introduced in Sec.1. The tight orbit gates entry to the well and
is the tight transition state of the original model, present here in the same kind: a hindered-rotor
orbit librating within±12∘\pm 12^{\circ}of the aligned axis (Fig.4). Chesnavich’s
original study concerned exactly the competition among such transition states; here we ask what has
changed about the innermost one.

Both models place the tight transition state at a flux minimum where the radial channel is
barrierless: the crossing is constricted not by a potential maximum alongrrbut because angular
hindrance narrows the accessible transverse phase space. In this sense the tight transition state is
entropic in the Chesnavich model as much as in the designed model, and Chesnavich’s transition-state
switching is a competition between entropic bottlenecks, neither anchored to a potential saddle. The
flux-minimizing dividing surface is moreover the surface spanned by the tight periodic orbit, since the minimum-flux dividing
surface is bounded by an unstable periodic orbit[13]: the variational
bottleneckr∗≃2.46​År^{*}\simeq 2.46~\text{\AA }of Sec.5sits at the tight orbit. We verify
this directly rather than assume it: in two degrees of freedom the flux through the dividing
surface spanned by a periodic orbit equals the orbit’s action∮p​𝑑q\oint p\,dq[13,19]; for the numerically located tight orbit this action is2.9022.902, and the
fixed-radius flux minimum per aligned window isΦR∗/2=2.907\Phi_{R^{*}}/2=2.907, an agreement of0.15%0.15\%(Fig.4c; the factor of two counts the two aligned windowsθ=0,π\theta=0,\pi, each
spanned by one tight orbit). The fixed-radius family thus attains the periodic-orbit flux, and the
identification of the variational bottleneck with the tight orbit’s dividing surface is a computed
result, not an assumption. What the
designed model changes is the depth and location of this entropic bottleneck. The interior maximum ofΩ\Omegaplaces a deep constriction at an interior radius (r∗≃2.46​År^{*}\simeq 2.46~\text{\AA },C≃0.10C\simeq 0.10),
where the monotone stiffness of the Chesnavich lock, largest at the inner edge and falling outward,
gives only a shallow one (C≃0.35C\simeq 0.35, Sec.5). It is this deep, interior entropic
bottleneck, not the entropic character as such, that gates inner capture and displaces roaming
outward (Secs.4,7).

A statistical rate theory would place the bottleneck atr∗r^{*}and compute a rate through it. But
the tight transition state gates only entry; the trajectories it admits do not settle into a single
complex, they roam, sorted by the free-rotor surface and released past the orbiting surface, with
non-exponential gap-time distributions (Sec.7). The entropic bottleneck locates
where capture is controlled; it does not by itself describe the roaming and escape that follow. That
the controlling bottleneck is entropic rather than energetic is the point of contact with Makarov.

## Relation to Makarov.

Makarov[9]considered a reaction coordinate crossing a region where a transverse
mode stiffens, with no potential barrier along the coordinate; integrating out the transverse mode
yields a free-energy barrierG​(x)=V​(x)+kB​T​ln⁡[ω⟂​(x)/ω0]G(x)=V(x)+k_{B}T\ln[\omega_{\perp}(x)/\omega_{0}]located at the stiffness
maximum, a purely entropic barrier. Our fixed-energyΩ​(r)\Omega(r)is the microcanonical counterpart of
hisω⟂​(x)\omega_{\perp}(x), and Eq. (1) is the same relation. Makarov further
observed that at such a barrier different observables need not agree: the reaction rate is well
described by transition-state theory while the distribution of transition-path times is not, because
the slow transverse mode carries dynamics that a single rate does not capture. In his model the
entropic maximum, the geometric constriction, and the rate-controlling surface all sit at one
location. Here the tight transition state is likewise entropic, but it is one of several transition
states at separated radii, and the roaming it admits is the nonstatistical dynamics that a rate
through it does not describe: a Hamiltonian roaming realization of the same rate-versus-dynamics
distinction.

## 9Conclusions

We constructed a designed Chesnavich-type roaming model in which the orientation-locking angular
hindrance is replaced by a localized maximum of the transverse frequency, a transverse-stiffness
ridge on an otherwise barrierless channel, and compared two fixed-energy trajectory ensembles that
differ only in the angular interaction, the Chesnavich lock in one and the entropic ridge in the
other, with the same radial channel, energy, and inward initial conditions. The central result is
dynamical: with the same radial channel, energy, and inward fixed-energy ensemble, the entropic
ridge gates entry into the inner well and converts most of the incoming flux into direct nonreactive
return; it does not increase the roaming fraction at the classifier radius but spatially reorganizes
it, suppressing it inside the ridge and displacing it outward relative to the Chesnavich lock.
Inner-well capture falls from57.3%57.3\%to14.7%14.7\%and direct nonreactive return rises from37.4%37.4\%to80.3%80.3\%, while the nonreactive roaming fraction at3.5​Å3.5~\text{\AA }is essentially unchanged
(5.3%→4.9%5.3\%\to 4.9\%) but is pushed outward in radius. The gating is robust across the Chesnavich
switching parameterα\alpha, and is essentially
unchanged when the Chesnavich radial potential is replaced by an LJ(8,4) channel with the same−1/r4-1/r^{4}tail; the outward displacement is established for theα=1\alpha=1comparison.
Strength-matched monotone controls separate amplitude from localization: capture tracks the
hindrance strength at the bottleneck radius, and a monotone lock matched to the ridge there
reproduces both the gating (17.8%17.8\%capture) and the outward displacement, while at equal global peak
amplitude the ridge gates far more effectively than a monotone profile (14.7%14.7\%against33.0%33.0\%). The interior maximum supplies placement, concentrating the hindrance strength at the
gating radius.

The phase-space explanation is the set of unstable periodic orbits and their dividing surfaces that
control capture and roaming: the tight orbit that gates the well, the free-rotor orbit that sorts
direct from roaming, and the orbiting orbit that gates escape, atr∗≃2.46​År^{*}\simeq 2.46~\text{\AA },rclass≃3.5​År_{\mathrm{class}}\simeq 3.5~\text{\AA }, andrOTS≃7.48​År_{\mathrm{OTS}}\simeq 7.48~\text{\AA }. The variational flux minimum
is not a separate statistical surface; it is the dividing surface spanned by the tight periodic orbit, the
orbit that gates entry to the well. In one sentence: a localized interior maximum of the transverse
stiffness reshapes roaming, gating inner capture and displacing roaming outward, by placing a deep
entropic bottleneck at an interior radius. That bottleneck is the tight transition state, an
unstable periodic orbit whose dividing surface is the variational minimum-flux surface, barrierless along the reaction
coordinate. Its entropic character it shares with the Chesnavich tight transition state; what the
interior maximum supplies is the concentration of hindrance strength at the gating radius that
makes it control capture. The mechanism is the angular
analogue of Makarov’s transverse-stiffening entropic barrier, here placed in a roaming Hamiltonian
with a long-range tail and an outer centrifugal transition state, and the roaming it admits is
nonstatistical.

## Appendix AComputational methods

## Trajectory ensemble.

Trajectories of Eq. (6) are integrated with a fixed-step fourth-order Runge–Kutta (RK4) scheme
(Δ​t=0.005\Delta t=0.005in model time units,τ=0.0489\tau=0.0489ps per unit) atE=2E=2kcal/mol. The
fixed-energy ensemble is a240×240240\times 240grid in(θ0,pθ,0)(\theta_{0},p_{\theta,0})launched inward fromr0=6​År_{0}=6~\text{\AA }. At each grid point the inward radial momentum is fixed by the energy constraint,pr=−2​μ​[E−Vrad​(r0)−12​B​(r0)​(1−cos⁡2​θ0)−12​a​(r0)​pθ,02],p_{r}=-\sqrt{2\mu\bigl[E-V_{\mathrm{rad}}(r_{0})-\tfrac{1}{2}B(r_{0})(1-\cos 2\theta_{0})-\tfrac{1}{2}a(r_{0})p_{\theta,0}^{2}\bigr]},

and grid points for which the radicand is non-positive (energetically
inaccessible) are removed; reported fractions are over the energetically accessible set. A trajectory
is integrated until it escapes, crossingr=8​År=8~\text{\AA }outward, or reaches the time limittmax=320t_{\max}=320model units (≈15.6\approx 15.6ps).

## The meaning of “reactive.”

Trajectories are not stopped at the inner boundary. Each is integrated until it escapes (crossesr=8​År=8~\text{\AA }outward) or reaches the time limittmax=320t_{\max}=320model units, and its closest approachrminr_{\min}and its crossings ofr=3.5​År=3.5~\text{\AA }are recorded along the way. A trajectory isreactiveifrmin<1.6​År_{\min}<1.6~\text{\AA }, that is, if it enters the well, androamingif it
crossesr=3.5​År=3.5~\text{\AA }three or more times in either direction. Because capture is registered by the
closest approach, the inner-capture fractions of Sec.4do not depend on whether
integration is continued past the well: stopping there would affect only trajectories that enter
and later re-emerge. Continuing resolves that small class (0.13%0.13\%of trajectories enter the well,
cross back outward, and roam, the roaming-reactive class, alongside the6.04%6.04\%that roam without
entering) and both come from the same run. “Reactive” therefore denotes entry into the well, not
committed product formation: the flow is volume-preserving and a captured trajectory may in
principle redissociate.

## Switching-parameter dependence.

The Chesnavich lock widthα\alphacontrols how early the angular hindrance switches off. The
comparisons of Sec.4use the standard valueα=1\alpha=1; the early-switching caseα=4\alpha=4is reported there to show that the roaming fraction is parameter-dependent while
the inner-well gating is not; the outward redistribution is demonstrated explicitly only for
theα=1\alpha=1classifier-radius sweep.

## Exact directional flux.

The flux Eq. (11) and confinement Eq. (12) are evaluated by adaptive
quadrature inθ\thetaon a dense grid inRR; the integrand’s positive-part support is resolved by
refining near the turning angles. The reported minima are stable to grid refinement at the∼0.01​Å\sim 0.01~\text{\AA }level, which is the resolution to whichr∗r^{*}is quoted.

## Outer boundary.

Capture and classifier statistics use an outer removal radiusr=8​År=8~\text{\AA }; the orbiting transition
state and the effective-potential construction of Sec.6were checked against an
extended boundaryr=12​År=12~\text{\AA }, with no change torOTSr_{\mathrm{OTS}}or to the reported fractions
beyond the last quoted digit.

## Numerical validation.

The reported fractions are converged in grid, step, and integration time. On the Chesnavich
channel the inner-capture fractions move from57.11%/14.68%57.11\%/14.68\%(lock/ridge) on a120×120120\times 120launch grid to57.27%/14.75%57.27\%/14.75\%on the240×240240\times 240production grid, a shift below0.10.1percentage points; the capture fraction is identical to two decimals atΔ​t=0.01\Delta t=0.01,0.0050.005,
and0.00250.0025. The fixed-step RK4 integrator conserves energy to|H−E|≲2×10−7|H-E|\lesssim 2\times 10^{-7}kcal/mol over complete trajectories, and attmax=320t_{\max}=320model units (≈15.6\approx 15.6ps) only0.085%0.085\%of trajectories (4949of57,60057{,}600) remain unclassified inside the interaction region.

## Tight-orbit dividing-surface flux.

The tight periodic orbit is located by a Newton search on thesin⁡θ=0\sin\theta=0surface of section
(converged initial condition(r,pr,θ,pθ)=(2.4689,0,0,4.3505)(r,p_{r},\theta,p_{\theta})=(2.4689,0,0,4.3505), periodT=0.5134T=0.5134atE=2E=2). The flux through the dividing surface it spans equals its action∮p​𝑑q\oint p\,dq,
accumulated along one period by RK4 atΔ​t=T/1.2×105\Delta t=T/1.2\times 10^{5}; the orbit closes to|y​(T)−y​(0)|<10−4|y(T)-y(0)|<10^{-4}with|H−E|≤10−4|H-E|\leq 10^{-4}along it. The resulting action,2.9022.902, agrees with
the per-window fixed-radius flux minimumΦR∗/2=2.907\Phi_{R^{*}}/2=2.907to0.15%0.15\%(Fig.4c).

## Appendix BGap-time analysis

Thegap timeof a trajectory is the residence time between one inward crossing of the launch
surfacer0=6​År_{0}=6~\text{\AA }and the next outward crossing. Its distribution is a classical diagnostic of
statistical versus nonstatistical decay: in the statistical (RRKM) picture escape is memoryless, and
the survival functionS​(t)S(t), the fraction of the entering ensemble still inside at timett, is a
single exponential set by one rate-limiting bottleneck. A departure from a single exponential
indicates that the escape is not memoryless: the residence times carry structure that a single rate
does not capture, either a tail heavier than exponential (trapping and recrossing) or a short-time
shoulder with a lighter tail (fast, direct transits on a characteristic crossing time). The gap-time
formulation is due to Thiele[15], following Slater’s dynamical theory of
unimolecular reactions[34,35], and was cast in the phase-space
transition-state setting by Ezra, Waalkens and Wiggins[16]; Mauguière, Collins, Ezra, Farantos and
Wiggins applied it to the roaming region of the Chesnavich model and likewise found nonstatistical
behavior[22].

The criterion deserves emphasis. Statisticality is a hypothesis about dynamics—memoryless escape
at a single rate—and the gap-time distribution tests it directly on the trajectories themselves.
Nonstatisticality in roaming is sometimes framed instead in terms of ergodic exploration of the
long-range region[5]; but the energy shell here is unbounded and trajectories escape
through the radical channel, so ergodicity in its standard sense is not defined for this flow,
whereas the gap-time test is constructed for precisely such open systems.

We computeS​(t)S(t)on the same fixed-energy ensemble used throughout, the240×240240\times 240inward
grid launched fromr0=6​År_{0}=6~\text{\AA }(AppendixA), so that the diagnostic describes the
very trajectories whose capture and roaming Secs.4and7characterize, not a separately launched set. For each nonreactive trajectory we record the time
from its inward launch atr0=6​År_{0}=6~\text{\AA }until it escapes, crossingr=8​År=8~\text{\AA }outward. Becauser0=6​År_{0}=6~\text{\AA }lies inside the orbiting transition state (rOTS≃7.48​År_{\mathrm{OTS}}\simeq 7.48~\text{\AA }), these are
conditional-on-entry residence times, not full collision lifetimes; the non-exponential character
found below holds for other launch surfaces as well, sor0=6​År_{0}=6~\text{\AA }is fixed by consistency with
the rest of the paper rather than to obtain the result. Two caveats on the construction itself.
Conditioning on the nonreactive outcome means this is not the gap-time distribution of the
complete incoming flux through a dividing surface; it is the conditional distribution of
nonreactive return times, and it is that distribution we test. And part of the short-time
behavior is deterministic: no trajectory can exit before the minimum transit time fromr0r_{0}in
and back out, so the flat shoulder at smallttis guaranteed, and the informative comparison
with an exponential is the shape of the decay beyond that direct-transit interval.

Figure7a showsS​(t)S(t)for the Chesnavich lock and the entropic ridge, each with the
matched single exponential overlaid. Both are manifestly non-exponential andnarrowerthan
exponential: coefficient of variation (CV, the ratio of standard deviation to mean)0.680.68for the lock and0.750.75for the ridge, against11for a memoryless decay, with tails lighter than exponential beyond the transit shoulder.
Figure7b resolves the ridge ensemble into its direct and roaming-classified
components, and this is the sharper statement. The two populations are well separated—mean
return times0.2570.257ps (direct) and0.8780.878ps (roaming)—and each is itself narrow (CV0.450.45and0.490.49); the lock decomposes the same way (0.3020.302and0.7750.775ps, CV0.440.44and0.490.49). The
full distribution is therefore a bimodal mixture of fast direct returns and slower roaming
returns, not a memoryless decay at any single rate. In particular the roaming-classified
subset—the population whose statisticality is at issue—has return times tightly clustered
about a characteristic value where a statistical (RRKM) escape would give CV=1=1and an
exponential tail: the roaming is nonstatistical in the direct sense that its residence times are
inconsistent with memoryless single-rate escape. The entropic bottleneck sets how much enters,
not the pace of what crosses: the transit-time-versus-rate decoupling Makarov identifies for an
entropic barrier. The mean nonreactive gap times over the full ensembles are0.3680.368ps (lock)
and0.3010.301ps (ridge).Figure 7:Nonreactive gap-time survival (r0=6​År_{0}=6~\text{\AA }launch, conditional on inward entry).
(a) Chesnavich lock and entropic ridge; dotted curves are matched single exponentials. Both
distributions are narrower than exponential, with a delayed onset set by the minimum transit
time. (b) The ridge ensemble resolved into direct and roaming-classified returns: the two
populations are individually narrow (coefficient of variation CV=0.45=0.45and0.490.49) and well separated in time; the full
distribution is their bimodal mixture, inconsistent with memoryless single-rate decay.

## Data availability

This study reports no experimental data. All results were generated by trajectory
integration of the classical Hamiltonian models defined in
Sections2and3, with the parameters of
Table1and the integrator of AppendixA. The
scripts that reproduce every figure and reported quantity are available from the author upon reasonable request.

## References
- [1]D. Townsend, S. A. Lahankar, S. K. Lee, S. D. Chambreau,
A. G. Suits, X. Zhang, J. Rheinecker, L. B. Harding, and J. M. Bowman,The roaming atom: straying from the reaction path in formaldehyde decomposition,
Science306, 1158–1161 (2004).
- [2]A. G. Suits,Roaming atoms and radicals: a new mechanism in molecular dissociation,
Acc. Chem. Res.41, 873–881 (2008).
- [3]J. M. Bowman,Roaming, Mol. Phys.112, 2516–2528 (2014).
- [4]J. M. Bowman and B. C. Shepler,Roaming radicals, Annu. Rev. Phys. Chem.62, 531–553 (2011).
- [5]A. G. Suits,Roaming reactions and dynamics in the van der Waals region,
Annu. Rev. Phys. Chem.71, 77–100 (2020).
- [6]R. Fernando, A. Dey, B. M. Broderick, B. Fu, Z. Homayoon,
J. M. Bowman, and A. G. Suits,Visible/infrared dissociation ofNO3\mathrm{NO_{3}}: roaming in the dark or roaming on
the ground?, J. Phys. Chem. A119, 7163–7168 (2015).
- [7]D. J. Tantillo,Beyond transition state theory—non-statistical dynamic effects for organic
reactions, Adv. Phys. Org. Chem.55, 1–16 (2021).
- [8]H.-X. Zhou and R. Zwanzig,A rate process with an entropy barrier, J. Chem. Phys.94,
6147–6152 (1991). doi:10.1063/1.460427.
- [9]D. E. Makarov,Reconciling transition path time and rate measurements in reactions with large
entropic barriers, J. Chem. Phys.146, 071101 (2017). doi:10.1063/1.4977177.
- [10]Y. Georgievskii and S. J. Klippenstein,Long-range transition state theory,
J. Chem. Phys.122, 194103 (2005).
- [11]D. G. Truhlar, B. C. Garrett, and S. J. Klippenstein,Current status of transition-state theory, J. Phys. Chem.100,
12771–12800 (1996).
- [12]K. S. Pitzer and W. D. Gwinn,Energy levels and thermodynamic functions for molecules with internal rotation.
I. Rigid frame with attached tops, J. Chem. Phys.10, 428–440 (1942).
- [13]E. Pollak and P. Pechukas,Transition states, trapped trajectories, and classical bound states embedded in the
continuum, J. Chem. Phys.69, 1218–1226 (1978).
- [14]P. Pechukas and E. Pollak,Classical transition state theory is exact if the transition state is unique,
J. Chem. Phys.71, 2062–2068 (1979).
- [15]E. Thiele,Comparison of the classical theories of unimolecular reactions,
J. Chem. Phys.36, 1466–1472 (1962).
- [16]G. S. Ezra, H. Waalkens, and S. Wiggins,Microcanonical rates, gap times, and phase space dividing surfaces,
J. Chem. Phys.130, 164118 (2009).
- [17]S. Wiggins,The role of normally hyperbolic invariant manifolds (NHIMs) in the phase-space
setting for chemical reaction dynamics, Regul. Chaotic Dyn.21, 621–638 (2016).
- [18]H. Waalkens and S. Wiggins,Geometrical models of the phase space structures governing reaction dynamics,
Regul. Chaotic Dyn.15(1), 1–39 (2010).
- [19]H. Waalkens, R. Schubert, and S. Wiggins,Wigner’s dynamical transition state theory in phase space: classical and quantum,
Nonlinearity21(1), R1–R118 (2008).
- [20]W. J. Chesnavich,Multiple transition states in unimolecular reactions,
J. Chem. Phys.84, 2615 (1986).
- [21]T. Su and W. J. Chesnavich,Parametrization of the ion–polar molecule collision rate constant by trajectory
calculations, J. Chem. Phys.76, 5183 (1982).
- [22]F. A. L. Mauguière, P. Collins, G. S. Ezra, S. C. Farantos,
and S. Wiggins,Roaming dynamics in ion-molecule reactions: phase space reaction
pathways and geometrical interpretation, J. Chem. Phys.140, 134112 (2014).
- [23]F. A. L. Mauguière, P. Collins, G. S. Ezra, S. C. Farantos,
and S. Wiggins,Multiple transition states and roaming in ion-molecule reactions: a
phase space perspective, Chem. Phys. Lett.592, 282 (2014).
- [24]F. A. L. Mauguière, P. Collins, Z. C. Kramer, B. K. Carpenter,
G. S. Ezra, S. C. Farantos, and S. Wiggins,Phase space structures explain hydrogen
atom roaming in formaldehyde decomposition, J. Phys. Chem. Lett.6, 4123–4128
(2015).
- [25]F. A. L. Mauguière, P. Collins, Z. C. Kramer, B. K. Carpenter,
G. S. Ezra, S. C. Farantos, and S. Wiggins,Phase space barriers and dividing
surfaces in the absence of critical points of the potential energy: application to roaming in
ozone, J. Chem. Phys.144, 054107 (2016).
- [26]F. A. L. Mauguière, P. Collins, Z. C. Kramer, B. K. Carpenter,
G. S. Ezra, S. C. Farantos, and S. Wiggins,Roaming: a phase space perspective,
Annu. Rev. Phys. Chem.68, 499–524 (2017).
- [27]V. Krajňák and H. Waalkens,The phase space geometry underlying roaming reaction dynamics,
J. Math. Chem.56(8), 2341–2378 (2018). doi:10.1007/s10910-018-0895-4.
- [28]V. Krajňák and S. Wiggins,Influence of mass and potential energy surface geometry on roaming in Chesnavich’sCH4+\mathrm{CH_{4}^{+}}model, J. Chem. Phys.149(9), 094109 (2018).
doi:10.1063/1.5044532.
- [29]V. Krajňák and S. Wiggins,Roaming in acetaldehyde, J. Chem. Phys.160, 244104 (2024).
doi:10.1063/5.0212443.
- [30]G. S. Ezra and S. Wiggins,The Chesnavich model for ion–molecule reactions: a rigid body coupled to a
particle, Int. J. Bifurcation Chaos29(2), 1950025 (2019).
doi:10.1142/S0218127419500251.
- [31]V. Krajňák, G. S. Ezra, and S. Wiggins,Roaming at constant kinetic energy: Chesnavich’s model and the Hamiltonian
isokinetic thermostat, Regul. Chaotic Dyn.24(6), 615–627 (2019).
doi:10.1134/S1560354719060030.
- [32]V. Krajňák, G. S. Ezra, and S. Wiggins,Using Lagrangian descriptors to uncover invariant structures in Chesnavich’s
isokinetic model with application to roaming, Int. J. Bifurcation Chaos30,
2050076 (2020).
- [33]M. E. Grice, B. K. Andrews, and W. J. Chesnavich,A threshold study of the classical dynamics of collision-induced dissociation in
collinearH+H2\mathrm{H+H_{2}}, J. Chem. Phys.87, 959–968 (1987).
- [34]N. B. Slater,New formulation of gaseous unimolecular dissociation rates,
J. Chem. Phys.24, 1256 (1956).
- [35]N. B. Slater,Theory of Unimolecular Reactions(Cornell University Press, Ithaca, NY, 1959).

## 


- 


Major funding support from
