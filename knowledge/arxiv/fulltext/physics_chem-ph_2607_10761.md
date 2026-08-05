# A Three-Degree-of-Freedom Chesnavich Model for Roaming: Derivation, Phase-Space Geometry, NHIM-Anchored Dividing Surfaces, and Roaming Transport

**arXiv ID**: 2607.10761v1
**Authors**: Stephen Wiggins
**Published**: 2026-07-12
**Categories**: physics.chem-ph, math.DS
**Comments**: 43 pages, 13 figures
**HTML URL**: https://arxiv.org/html/2607.10761v1

## Abstract

Roaming reactions, in which a dissociating fragment moves through a flat region of the potential surface rather than down the minimum-energy path, lie outside the assumptions of conventional transition state theory. The phase-space theory of roaming -- unstable periodic orbits and their invariant manifolds organizing transport -- has been developed for the Chesnavich model of $\mathrm{CH_4^+}\to\mathrm{CH_3^+}+\mathrm{H}$, which is cylindrically symmetric and reduces to two degrees of freedom (2-DoF). We construct and analyze a three-degree-of-freedom (3-DoF) extension. From the rigid-body formulation of Ezra and Wiggins, we break the symmetry with an azimuthal coupling respecting the three-fold ($C_3$) symmetry of the methyl fragment, obtaining a family $H_b$ whose planar reduction at $b=0$ is the 2-DoF model exactly and which is genuinely 3-DoF for $b>0$. This activates the out-of-plane degree of freedom at once: with the physical planar-top inertia ratio $I_z=2I_x$, arbitrarily weak coupling makes the periodic orbit on the roaming shelf transversely unstable, opening an escape route out of the reaction plane. Apart from a narrow elliptic window $0.58\lesssim b\lesssim0.63$, the instability persists across the range studied, changing type through a period-doubling at $b_c\approx0.63$. Because a periodic orbit cannot anchor a dividing surface in three degrees of freedom, we construct the objects that do -- three three-dimensional normally hyperbolic invariant manifolds, one per transition state -- at $b=0$, and prove that every compact interior piece of each persists for sufficiently small $b>0$. At $E=0.5\ \mathrm{kcal\,mol^{-1}}$ the coupling lowers the direct non-reactive fraction of a microcanonical ensemble of incoming trajectories by $0.032$ and raises the two roaming fractions by $0.040$; the effect decreases as the energy increases.

## Full Text

A Three-Degree-of-Freedom Chesnavich Model for Roaming: Derivation, Phase-Space Geometry, NHIM-Anchored Dividing Surfaces, and Roaming Transport

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
- 
- 
- 
- 
- 
- 
- 
- 
- 
- License: CC BY 4.0arXiv:2607.10761v1 [physics.chem-ph] 12 Jul 2026

## A Three-Degree-of-Freedom Chesnavich Model for Roaming:
Derivation, Phase-Space Geometry, NHIM-Anchored Dividing Surfaces, and Roaming TransportS. Wiggins
Hetao Institute of Mathematics and Interdisciplinary Sciences, Shenzhen, China
School of Mathematics, University of Bristol, Bristol BS8 1TW, United Kingdom

## Abstract

Roaming reactions, in which a dissociating fragment moves through a flat region of the potential surface rather than down the minimum-energy path, lie outside the assumptions of conventional transition state theory. The phase-space theory of roaming — unstable periodic orbits and their invariant manifolds organizing transport — has been developed for the Chesnavich model ofCH4+→CH3++H\mathrm{CH_{4}^{+}}\to\mathrm{CH_{3}^{+}}+\mathrm{H}, which is cylindrically symmetric and reduces to two degrees of freedom (2-DoF). We construct and analyze a three-degree-of-freedom (3-DoF) extension. From the rigid-body formulation of Ezra and Wiggins, we break the symmetry with an azimuthal coupling respecting the three-fold (C3C_{3}) symmetry of the methyl fragment, obtaining a familyHbH_{b}whose planar reduction atb=0b=0is the 2-DoF model exactly and which is genuinely 3-DoF forb>0b>0. This activates the out-of-plane degree of freedom at once: with the physical planar-top inertia ratioIz=2​IxI_{z}=2I_{x}, arbitrarily weak coupling makes the periodic orbit on the roaming shelf transversely unstable, opening an escape route out of the reaction plane. Apart from a narrow elliptic window0.58≲b≲0.630.58\lesssim b\lesssim 0.63, the instability persists across the range studied, changing type through a period-doubling atbc≈0.63b_{c}\approx 0.63. Because a periodic orbit cannot anchor a dividing surface in three degrees of freedom, we construct the objects that do — three three-dimensional normally hyperbolic invariant manifolds, one per transition state — atb=0b=0, and prove that every compact interior piece of each persists for sufficiently smallb>0b>0. AtE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}the coupling lowers the direct non-reactive fraction of a microcanonical ensemble of incoming trajectories by0.0320.032and raises the two roaming fractions by0.0400.040; the effect decreases as the energy increases.

## 1Introduction

In conventional transition state theory (TST) a reaction is controlled by a single recrossing-free dividing surface separating reactants from products[1,2]. Roaming reactions violate this picture: a dissociating fragment, instead of separating directly or following the minimum-energy path, moves through a flat region of the potential energy surface at wide amplitude before re-encountering its partner and reacting, often through an unexpected channel[3,4,5,6]. Roaming has been identified in a broad range of systems[7].

The phase-space (geometric) theory of reaction dynamics provides a framework for roaming. The objects that organize transport are not critical points of the potential but invariant sets of the dynamics: unstable periodic orbits (POs) in two degrees of freedom, and normally hyperbolic invariant manifolds (NHIMs) in higher dimension, together with their stable and unstable manifolds[2,9]. For the two-degree-of-freedom (2-DoF) Chesnavich model of the ion–molecule reactionCH4+→CH3++H\mathrm{CH_{4}^{+}}\to\mathrm{CH_{3}^{+}}+\mathrm{H}[10], this program has been carried through in detail: the relevant POs, their bifurcations, and the resulting roaming pathways have been mapped as functions of energy and of the potential parameters[12,13,14,15].

Chesnavich’s potential is cylindrically symmetric, so the azimuthal angular momentum is conserved and the model reduces to two degrees of freedom. Roaming in real systems has more degrees of freedom, and the phase-space theory of NHIMs has been extended to three degrees of freedom[17]. No concrete, tractable 3-DoF Chesnavich-type model has been available on which to test and develop that theory. This paper supplies one.

Section2derives the 3-DoF Chesnavich Hamiltonian from the Ezra–Wiggins rigid-body formulation[15], chooses the lowest-order smooth coupling compatible with theC3C_{3}symmetry of the methyl fragment, and describes the model’s physical and chemical content. Section3develops the configuration-space picture of roaming, states how roaming is defined — as a property of trajectories classified against three transition states — and gives the dimensional reason a periodic orbit can no longer anchor a dividing surface in three degrees of freedom. Section4presents the phase-space geometry as a function of the couplingbband the energyEE. The central object is the periodic orbit FR1, the unstable orbit lying on the roaming shelf — the flat region of the potential where roaming occurs — whose dividing surface classifies trajectories as roaming or direct in the 2-DoF theory; the central finding is that FR1 becomes unstable in the out-of-plane direction as soon as the cylindrical symmetry is broken. Section5compares this with the formaldehyde–acetaldehyde contrast and shows, through the growth of out-of-plane motion along trajectories, when a two-degree-of-freedom description suffices and when it fails. Section6constructs the three three-dimensional NHIMs explicitly in theb=0b=0limit and establishes three things about them: the topology of the dividing surface each anchors, the status of FR1 as the limiting planar member of its manifold, and the persistence of their compact interior pieces for sufficiently smallb>0b>0. These results are stated and proved as six propositions (Section6.7) resting on a single numerically verified hypothesis, the existence and smoothness of the reduced periodic-orbit family. Section7carries the trajectory classification into three dimensions and computes the class fractions and gap-time statistics as functions ofbband energy. Section8discusses the chemical and dynamical significance, and Section9concludes. Appendices document the numerical methods and the technical issues encountered, including a coordinate singularity intrinsic to body-frame spherical coordinates.Figure 1:Orientation. (a) Body-frame coordinates: the departing H atom is located relative to theCH3+\mathrm{CH_{3}^{+}}center of mass by the radial separationrr, the polar (bending) angleθ\thetameasured from theC3C_{3}symmetry axis (a co-latitude), and the azimuthal angleϕ\phiabout that axis (a longitude). Ameridionalplane is a half-plane containing the axis (a plane of constantϕ\phi, like a line of longitude); theequatoris the planeθ=π/2\theta=\pi/2. (b) The three radial regions and, on the energy lineE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}(dotted), the radial locations of the three planar orbits that generate the entrance, classifier, and reactive-gate NHIMs: the tight transition state TTS-PO (reactive gate,λ=220.5\lambda=220.5), arcing over the mouth of the well atr∈[2.38,2.64]​År\in[2.38,2.64]\ \text{\text{\AA }}, just outside the ridge crest; the roaming-shelf orbit FR1 (classifier,λ=24.6\lambda=24.6); and the orbiting transition state OTS-PO (entrance,λ=1.13\lambda=1.13) at the centrifugal barrier. Hereλ\lambdais the Floquet multiplier of the orbit — the factor by which a small displacement from it grows over one period, defined in Section3— so the reactive gate is strongly unstable and the entrance only weakly so. Each is the limiting planar (separatrix) member of a two-component NHIM family parametrized by the angular momentum (Section6). (c) TheC3C_{3}azimuthalcorrugationintroduced by the coupling: the bending ridge is rippled three-fold in azimuth,∝b​cos⁡3​ϕ\propto b\cos 3\phi, with three equivalent ridges and three intervening channels — the imprint of the three hydrogens of the methyl group.

## 2The three-degree-of-freedom model

## 2.1Coordinates and reduced Hamiltonian

Following Ezra and Wiggins[15], the Chesnavich system is modeled as a rigid symmetric top — theCH3+\mathrm{CH_{3}^{+}}fragment, with principal moments of inertiaIx=Iy≠IzI_{x}=I_{y}\neq I_{z}— coupled to a structureless particle representing the departing H atom. The H atom’s position relative to the fragment center of mass is given in molecule-fixed spherical coordinates(r,θ,ϕ)(r,\theta,\phi), whererris the radial separation,θ\thetathe polar (bending) angle measured from theC3C_{3}symmetry axis, andϕ\phithe azimuthal angle about that axis (Fig.1a). The fragment orientation is described by Euler angles. The full molecular kinetic energy is the sum of the rigid-rotor energy of the top and the kinetic energy of the H atom.

We work at zero total angular momentum,J=0J=0, the natural setting in which to isolate the internal roaming dynamics. In this case the Ezra–Wiggins reduction expresses the Hamiltonian in terms of(r,θ,ϕ)(r,\theta,\phi)and their conjugate momenta(pr,pθ,pϕ)(p_{r},p_{\theta},p_{\phi})asH=12​Ix​(pθ2+pϕ2​cot2⁡θ)+pϕ22​Iz+12​m​(pr2+pθ2r2+pϕ2r2​sin2⁡θ)+V​(r,θ,ϕ),H=\frac{1}{2I_{x}}\left(p_{\theta}^{2}+p_{\phi}^{2}\cot^{2}\theta\right)+\frac{p_{\phi}^{2}}{2I_{z}}+\frac{1}{2m}\left(p_{r}^{2}+\frac{p_{\theta}^{2}}{r^{2}}+\frac{p_{\phi}^{2}}{r^{2}\sin^{2}\theta}\right)+V(r,\theta,\phi),(1)

wheremmis theH\mathrm{H}–CH3+\mathrm{CH_{3}^{+}}reduced mass and the rotational kinetic energy usesLx2+Ly2=pθ2+pϕ2​cot2⁡θL_{x}^{2}+L_{y}^{2}=p_{\theta}^{2}+p_{\phi}^{2}\cot^{2}\theta,Lz=pϕL_{z}=p_{\phi}. Thiscot2⁡θ\cot^{2}\thetaform is the one given by the Ezra–Wiggins rigid-body reduction[15], which we follow throughout.

## 2.2Potential and the symmetry-breaking coupling

Chesnavich’s potential[10]consists of a radial term describing the C–H stretch and a hindered-rotor coupling describing the bend:VCH​(r)\displaystyle V_{\mathrm{CH}}(r)=Dec1−6​[2​(3−c2)​ec1​(1−x)−(4​c2−c1​c2+c1)​x−6−(c1−6)​c2​x−4],x=rre,\displaystyle=\frac{D_{e}}{c_{1}-6}\left[2(3-c_{2})\,e^{c_{1}(1-x)}-(4c_{2}-c_{1}c_{2}+c_{1})\,x^{-6}-(c_{1}-6)c_{2}\,x^{-4}\right],\quad x=\frac{r}{r_{e}},(2)V0​(r)\displaystyle V_{0}(r)=Ve​e−α​(r−re)2.\displaystyle=V_{e}\,e^{-\alpha(r-r_{e})^{2}}.(3)

In the original 2-DoF model the angular potential is12​V0​(r)​(1−cos⁡2​θ)\tfrac{1}{2}V_{0}(r)(1-\cos 2\theta), which depends only on the bending angleθ\thetaand not on the azimuthϕ\phi; the model is therefore cylindrically symmetric,pϕp_{\phi}is conserved, and the dynamics reduces to two degrees of freedom. The standard parameters, fitted toCH4+\mathrm{CH_{4}^{+}}, areDe=47D_{e}=47,re=1.1r_{e}=1.1,c1=7.37c_{1}=7.37,c2=1.61c_{2}=1.61,Ve=55V_{e}=55(energies inkcal​mol−1\mathrm{kcal\,mol^{-1}}, lengths inÅ),α=1​Å−2\alpha=1\,\text{\text{\AA }}^{-2},Ix=2.373409​u​Å2I_{x}=2.373409\ \mathrm{u\,\text{\text{\AA }}^{2}}, and the reduced massm=0.9445​um=0.9445\ \mathrm{u}, frommH=1.007825​um_{\mathrm{H}}=1.007825\ \mathrm{u}andmC=12.0​um_{\mathrm{C}}=12.0\ \mathrm{u}[10,12,15]. In these units (u,Å,kcal​mol−1\mathrm{kcal\,mol^{-1}}) the induced unit of time isÅ​u/(kcal​mol−1)≈48.9​fs\text{\text{\AA }}\sqrt{\mathrm{u}/(\mathrm{kcal\,mol^{-1}})}\approx 48.9\ \mathrm{fs}; all times below are quoted in this unit.

To obtain a genuine three-degree-of-freedom system we break the cylindrical symmetry by introducing azimuthal dependence. The admissible azimuthal couplings are constrained by the symmetry of the methyl fragment.CH3+\mathrm{CH_{3}^{+}}hasD3​hD_{3h}symmetry; the three hydrogen atoms lie at120∘120^{\circ}intervals, so any potential the departing H atom experiences as a function of azimuth must be invariant under the three-fold rotationϕ→ϕ+2​π/3\phi\to\phi+2\pi/3. The lowest-order azimuthal harmonic with this property iscos⁡3​ϕ\cos 3\phi. A coupling built fromcos⁡2​ϕ\cos 2\phi, by contrast, would impose a spurious two-fold symmetry inconsistent with the molecular point group. We therefore takeVcoup​(r,θ,ϕ)=V0​(r)​[sin2⁡θ+b​sin3⁡θ​cos⁡3​ϕ],V_{\mathrm{coup}}(r,\theta,\phi)=V_{0}(r)\left[\sin^{2}\theta+b\,\sin^{3}\theta\,\cos 3\phi\right],(4)

so that the total potential isV=VCH+VcoupV=V_{\mathrm{CH}}+V_{\mathrm{coup}}. The first term equals12​V0​(1−cos⁡2​θ)\tfrac{1}{2}V_{0}(1-\cos 2\theta)and reproduces the Chesnavich bend; we write it assin2⁡θ\sin^{2}\thetabecause its Cartesian form,V0​(X2+Y2)/r2V_{0}\,(X^{2}+Y^{2})/r^{2}, is a ratio of polynomials whose denominator does not vanish away from the origin, so that smoothness across the symmetry axis is manifest for both angular terms. The second term is the symmetry-breaking term, withb∈[0,1]b\in[0,1]a dimensionless coupling strength. The factorsin3⁡θ​cos⁡3​ϕ\sin^{3}\theta\cos 3\phiis the angular factor of the real solid harmonicX3−3​X​Y2X^{3}-3XY^{2}of degree three and order three: in Cartesian molecule-fixed coordinates(X,Y,Z)=(r​sin⁡θ​cos⁡ϕ,r​sin⁡θ​sin⁡ϕ,r​cos⁡θ)(X,Y,Z)=(r\sin\theta\cos\phi,\,r\sin\theta\sin\phi,\,r\cos\theta)it is(X3−3​X​Y2)/r3(X^{3}-3XY^{2})/r^{3}, which is smooth everywhere except at the origin. This smoothness is essential: a one-fold coupling of the formV0​(r)​sin2⁡θ​cos⁡ϕV_{0}(r)\sin^{2}\theta\cos\phi— Cartesian formV0​X​X2+Y2/r2V_{0}\,X\sqrt{X^{2}+Y^{2}}/r^{2}— is only once continuously differentiable on the symmetry axis, whereϕ\phiis undefined; its second derivatives, which enter the variational equations, are discontinuous there, and since the orbits constructed below cross that axis their linear stability would be ill-defined (AppendixB).

## 2.3Conserved quantities and symmetries

The Hamiltonian and coupling introduced above—their reduction, atb=0b=0on the invariant setpϕ=0p_{\phi}=0, to the 2-DoF Chesnavich model, the smoothness of the coupling across the symmetry axis, and the discrete symmetries recorded next—were confirmed in a computer-algebra system (AppendixA). Three properties ofHbH_{b}organize the analysis that follows: the exact reduction, on the invariant setpϕ=0p_{\phi}=0, to the 2-DoF Chesnavich model atb=0b=0, which anchors every subsequent result to a known limit; the loss of the azimuthal integral forb>0b>0, which makes the dynamics genuinely three-degree-of-freedom; and a set of discrete symmetries, which single out the invariant reaction plane in which the generating orbits lie and the transverse subspace whose stability governs out-of-plane escape.

(i) Reduction atb=0b=0.Forb=0b=0the Hamiltonian (1) satisfies∂H/∂ϕ=0\partial H/\partial\phi=0, soϕ\phiis cyclic andpϕp_{\phi}is conserved. Restricting to the invariant setpϕ=0p_{\phi}=0, (1) reduces identically to the 2-DoF Chesnavich Hamiltonian, withI→IxI\to I_{x}andμ→m\mu\to m. The familyHbH_{b}is therefore an exact homotopy whoseb=0b=0member carries Chesnavich’s 2-DoF model as its planar reduction.

(ii) Symmetry breaking atb>0b>0.∂H/∂ϕ=−3​b​V0​(r)​sin3⁡θ​sin⁡3​ϕ≠0\partial H/\partial\phi=-3bV_{0}(r)\sin^{3}\theta\sin 3\phi\neq 0, sopϕp_{\phi}is no longer conserved and the dynamics is genuinely three-degree-of-freedom. Energy is the only known global integral.

(iii) Discrete symmetries.The Hamiltonian is invariant under the canonical reflections(θ,pθ)→(π−θ,−pθ)(\theta,p_{\theta})\to(\pi-\theta,-p_{\theta})and(ϕ,pϕ)→(−ϕ,−pϕ)(\phi,p_{\phi})\to(-\phi,-p_{\phi})(sincecos⁡3​ϕ\cos 3\phiis even), and under theC3C_{3}rotationϕ→ϕ+2​π/3\phi\to\phi+2\pi/3. The reflection(ϕ,pϕ)→(−ϕ,−pϕ)(\phi,p_{\phi})\to(-\phi,-p_{\phi})fixes the set{Y=0,pY=0}\{Y=0,\ p_{Y}=0\}— the reaction plane — which is therefore invariant under the flow; the planar member of the FR1 family lies in the reaction plane, and out-of-plane perturbations(Y,pY)(Y,p_{Y})form a well-defined transverse subspace whose stability we analyze below.

## 2.4Physical inertia of a planar top

The moment-of-inertia ratioIz/IxI_{z}/I_{x}is not an incidental parameter of the model: it fixes the relative timescales of rotation about the symmetry axis and tumbling perpendicular to it, and it enters the transverse dynamics directly through thepϕ2/(2​Iz)p_{\phi}^{2}/(2I_{z})term in (1). In a model constructed only for mathematical convenience one might be tempted to leave this ratio free, or to setIz=IxI_{z}=I_{x}so that the top is spherical and the rotational kinetic energy is isotropic. Either choice would be physically wrong forCH3+\mathrm{CH_{3}^{+}}, and, as Section4shows, either would change the transverse stability of the orbit qualitatively; it is therefore essential that the value used be the one dictated by the geometry of the fragment rather than a tunable knob.

For a planar (laminar) rigid body the perpendicular-axis theorem states that the moment of inertia about the axis normal to the plane equals the sum of the moments about any two orthogonal in-plane axes through the same point[16].CH3+\mathrm{CH_{3}^{+}}is planar, and its three-fold symmetry makes the two in-plane principal moments equal,Ix=IyI_{x}=I_{y}, so the theorem givesIz=Ix+Iy=2​IxI_{z}=I_{x}+I_{y}=2I_{x}exactly: the ion is a planar oblate top withIz/Ix=2I_{z}/I_{x}=2. WithIx=2.373409​u​Å2I_{x}=2.373409\ \mathrm{u\,\text{\text{\AA }}^{2}}[10,15]this givesIz=4.746818​u​Å2I_{z}=4.746818\ \mathrm{u\,\text{\text{\AA }}^{2}}. We use this physical value throughout. As shown in Section4, it is, together with theC3C_{3}coupling, what produces the central bifurcation of the paper: the transverse direction is hyperbolic at weak coupling precisely because of the oblate ratioIz=2​IxI_{z}=2I_{x}, and the unphysical spherical choiceIz=IxI_{z}=I_{x}removes the effect.

## 2.5Chemical significance

The model represents the post-transition-state dynamics ofCH4+→CH3++H\mathrm{CH_{4}^{+}}\to\mathrm{CH_{3}^{+}}+\mathrm{H}once the departing H atom has reached the flat, long-range region of the potential where roaming occurs. Fragmentation ofCH4+\mathrm{CH_{4}^{+}}toCH3++H\mathrm{CH_{3}^{+}}+\mathrm{H}is an established decay channel of the methane cation — seen, for instance, when aCH4+\mathrm{CH_{4}^{+}}intermediate formed by charge transfer ejects a hydrogen atom[8]— and the wide-amplitude, non-minimum-energy-path character of such dissociations is the hallmark of roaming[5,6]. The long-range ion–neutral interaction that governs this regime, comprising the ion-induced-dipole attraction and the higher anisotropic terms of the charge–molecule potential, is precisely the interaction whose central-field and orbiting-transition-state treatment underlies the phase-space theory of ion–molecule capture and reaction[11,8].

The radial coordinaterris the dissociating C–H distance; the bending angleθ\thetameasures the departure of the H atom from theCH3+\mathrm{CH_{3}^{+}}symmetry axis; and the azimuthal angleϕ\phimeasures rotation of the H atom about that axis relative to the methyl frame.CH3+\mathrm{CH_{3}^{+}}is planar (point groupD3​hD_{3h}), so the charge distribution it presents to the departing H atom carries an intrinsic three-fold azimuthal structure. In the cylindrically symmetric limit the azimuthal motion is decoupled by an exact integral:pϕp_{\phi}is conserved and each trajectory is confined to itspϕp_{\phi}-leaf. The symmetry-breaking parameterbbmeasures the strength with which this three-fold structure couples to the azimuthal motion of the roaming H atom; physically it interpolates between an idealized axially averaged interaction (b=0b=0) and one that resolves the discrete three-fold structure of the methyl group (b>0b>0). That molecular orientation and geometry — and not merely the stationary points of the potential — can control the outcome of ion–molecule reactions is by now well documented[8], which is what makes resolving this structure physically consequential. The question the model is designed to answer is how this three-fold azimuthal structure, present in the real molecule but suppressed in the 2-DoF model, reshapes the phase-space structures that control roaming.

## 3The geometry of roaming in three degrees of freedom

Roaming is a reaction mechanism: a fragment leaves the well and, rather
than dissociating directly, moves through a flat part of the potential energy surface
before it reacts or separates. Its description in phase space rests on three parts of
the surface with distinct chemical meaning — the deep well, the roaming shelf, and
the dissociation asymptote — and on the transition states whose dividing surfaces
gate transport between them. This section fixes the three parts of the surface and
their chemical content; the transition states of Section3.2are then
interpreted as the gates between them. Two features distinguish the 3-DoF surface
from the 2-DoF model:V​(r,θ,ϕ)V(r,\theta,\phi)is defined on a three-dimensional
configuration space, so no single planar contour plot represents it, and the
structures that gate transport are no longer periodic orbits
(Section3.2).

## 3.1The configuration-space landscape and the meaning of roaming

In the 2-DoF Chesnavich model the three parts of the surface are identified from the
contours ofV​(r,θ)V(r,\theta)[24,12]. At smallrra deep
well holds the H atom bound to the fragment. At intermediate-to-largerrthe
Chesnavich lockV0​(r)V_{0}(r)has decayed and the angular potential is shallow, so the H
atom moves through wide ranges ofθ\thetaat nearly constant radial energy. In the
radial coordinate this part of the surface is a ledge:VCH​(r)V_{\mathrm{CH}}(r)rises
steeply out of the well and then levels off, sloping gently outward onto the
dissociation asymptoteV→0V\to 0, so thatrrvaries by severalÅat nearly constant
potential energy (Fig.2b, on-axis cut). We call this feature of
the potential theroaming shelf, the term making explicit the radial flatness
that is the geometric condition for roaming: a trajectory can persist at largerrwithout descending a radial slope. Roaming is motion that, having left the well,
remains on the shelf rather than crossing inward to the well or outward to
dissociation; its operational definition — a classification of trajectories by
their crossings of three dividing surfaces — is given in Section3.2.

The 3-DoF model has the same three parts. BecauseV​(r,θ,ϕ)V(r,\theta,\phi)is defined on a
three-dimensional configuration space, we represent it by two-dimensional cuts
(Fig.2). Atb=0b=0the potential is cylindrically symmetric, and a
single meridional cut — the half-plane of constantϕ\phicontaining the symmetry
axis, coordinates(ρ,Z)(\rho,Z)withρ=X2+Y2\rho=\sqrt{X^{2}+Y^{2}}— carries the whole
surface; this is the 2-DoF landscape of[12,24](Fig.2a). The well
sits on the axis atr=rer=r_{e}, the collinearCH3+​⋯\mathrm{CH_{3}^{+}}\cdotsH geometry at which
the bending termV0​(r)​sin2⁡θV_{0}(r)\sin^{2}\thetavanishes. Away from the axis this term raises
the potential into a ridge at the equatorθ=π/2\theta=\pi/2— the bending ridge —
which hinders changes in the polar angle whereV0​(r)V_{0}(r)is appreciable. The radial
cuts of Fig.2b make the energetics explicit: on the axis
(θ=0\theta=0) the potential isVCH​(r)V_{\mathrm{CH}}(r)alone, the well with no bend; at
the equator (θ=π/2\theta=\pi/2) it carries the bending ridge; both flatten onto the
roaming shelf beyondr≈3r\approx 3Å, and FR1 lies atr≈3.2r\approx 3.2–3.653.65Å(Section3.2).

The 3-DoF content absent from the 2-DoF model is the dependence on the azimuthϕ\phi. Forb>0b>0the couplingb​V0​(r)​sin3⁡θ​cos⁡3​ϕb\,V_{0}(r)\sin^{3}\theta\cos 3\phimodulates the bending
ridge three-fold inϕ\phi: at the equator it addsb​V0​(r)​cos⁡3​ϕb\,V_{0}(r)\cos 3\phito the ridge
height, lowering the ridge in three channels nearϕ=π/3,π,5​π/3\phi=\pi/3,\ \pi,\ 5\pi/3(wherecos⁡3​ϕ=−1\cos 3\phi=-1) and raising it in the three directions between. The bending ridge —
the barrier between the well and the roaming shelf — is therefore corrugated
three-fold around the axis, following the three hydrogens of the methyl fragment;bbis the depth of the corrugation. Because the modulation is carried byV0​(r)V_{0}(r),
it is largest at the inner edge of the shelf, whereV0V_{0}is of order the roaming
energy, and vanishes asV0→0V_{0}\to 0at largerr. Figure2c shows
the modulation on the sphere of directions(θ,ϕ)(\theta,\phi)atr=3.1r=3.1Åforb=0.8b=0.8.Figure 2:The configuration-space landscape of the 3-DoF Chesnavich model. (a) Meridional cut of the potential atb=0b=0(cylindrically symmetric, identical to the 2-DoF landscape), in the half-plane containing the symmetry axis; the wells sit on the axis atr=rer=r_{e}(markers), the equatorial bending ridge is the raised region off-axis, and the flat roaming shelf lies beyond, with the dashed curve theE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}equipotential. The closed loops are the computed FR1 orbit (the action-13.75513.755branch) atb=0,0.3,0.57b=0,0.3,0.57(Section4), whose invariant plane is this meridional plane; the loop deforms, breaking its up–down symmetry, as the coupling increases. The star marks theCH3+\mathrm{CH_{3}^{+}}center of mass. (b) Radial cuts: on the symmetry axis (θ=0\theta=0, the well, with no bend) and at the equator (θ=π/2\theta=\pi/2) for two azimuths,ϕ=0\phi=0andϕ=π/3\phi=\pi/3, whose separation is the three-fold modulation; the shaded band is the radial range of FR1 and the dotted line the energyE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}. (c) The angular landscape on the sphere of directions(θ,ϕ)(\theta,\phi)at a representative roaming radiusr=3.1​År=3.1\ \text{\text{\AA }}forb=0.8b=0.8: the equatorial bending ridge carries a three-fold azimuthal corrugation, with the favored channels (triangles) nearϕ=π3,π,5​π3\phi=\tfrac{\pi}{3},\pi,\tfrac{5\pi}{3}.

With the landscape established, the meaning of roaming in the model is fixed: motion at energies in the roaming window that stays on the shelf, wandering in(θ,ϕ)(\theta,\phi)at largerr, rather than crossing inward to the well or outward to dissociation. The phase-space structures that separate these outcomes, and the effect of the corrugation on them, are the subject of the rest of the paper.

## 3.2The phase-space structures that organize roaming

Roaming is a property of trajectories: a trajectory roams or does not according to
how it crosses three dividing surfaces, defined below. Each dividing surface is
anchored on an invariant manifold of the flow. In the 2-DoF model these manifolds
are the three periodic orbits of Mauguière, Collins, Ezra, Farantos, and Wiggins[12]; in the
3-DoF model they are three-dimensional manifolds, constructed in
Section6. This section reviews the 2-DoF structures, states the
trajectory classification, and gives the dimension count that determines what the
corresponding 3-DoF objects must be.

Dimension counts are taken in the energy surfaceΣE\Sigma_{E}unless stated otherwise;
all dividing surfaces in this paper are isoenergetic, constructed within a singleΣE\Sigma_{E}, since the conserved energy confines every trajectory to its own energy
surface and energy enters the construction only as a parameter. Fornndegrees of
freedom the phase space is2​n2n-dimensional and the energy surfaceΣE={H=E}\Sigma_{E}=\{H=E\}is(2​n−1)(2n-1)-dimensional. A dividing surface must locally separateΣE\Sigma_{E}into two components, so its dimension is2​n−22n-2: codimension one inΣE\Sigma_{E}. The dividing surfaces of phase-space transition state theory are
anchored on a normally hyperbolic invariant manifold (NHIM) of dimension2​n−32n-3,
codimension two inΣE\Sigma_{E}, whose stable and unstable manifolds have dimension2​n−22n-2and channel trajectories through the bottleneck[2,9]. These counts follow from the separation requirement alone and hold for
everynn; the dimensions of the objects satisfying them grow withnn(Table1).2 DoF (energy surface33-D)3 DoF (energy surface55-D)dividing surface  (codim 1)22-D44-Danchoring NHIM  (codim 2)11-D:a periodic orbit33-D: not an orbititsWs,WuW^{s},\,W^{u}(codim 1)22-D44-Da periodic orbitisthe NHIM11-D (codim 4)itsWs,WuW^{s},\,W^{u}(the codim-1 separatrices)33-D (codim 2): cannot divideTable 1:The codimension of the dividing surface and of its anchoring NHIM is the same in two and three degrees of freedom; the dimension is not. In a three-dimensional energy surface the codimension-two NHIM is one-dimensional, a periodic orbit. In a five-dimensional energy surface it is three-dimensional; a periodic orbit there has codimension four, its stable and unstable manifolds codimension two, and neither separates the energy surface.

## Two degrees of freedom.

Forn=2n=2the energy surface is three-dimensional and a codimension-two NHIM is
one-dimensional: a periodic orbit. This is why periodic orbits organize the 2-DoF
theory. The model has three, named by their roles[12,24].

The linear stability of a periodic orbit is measured by its Floquet multipliers[32], the
eigenvalues of the monodromy matrix — the linearization of the flow over one
period (AppendixC). The orbit is hyperbolic when a reciprocal pair{λ,λ−1}\{\lambda,\lambda^{-1}\}lies off the unit circle;λ>1\lambda>1is the factor by
which a transverse perturbation grows over one period. We quoteλ\lambdafor each
orbit because these rates recur in Section6: the normal expansion rate
of each three-dimensional manifold is theλ\lambdaof its generating orbits, and
the persistence of the manifolds forb>0b>0(Proposition6) requires these rates
to dominate the tangential growth.

OTS-PO, the entrance.A relative equilibrium at the centrifugal barrier
(r0≈13.4r_{0}\approx 13.4Å; Fig.3b), withλOTS=1.13\lambda_{\mathrm{OTS}}=1.13— weakly hyperbolic because the barrier is shallow. Its dividing surface
gates the entrance: a trajectory crossing outward dissociates toCH3++H\mathrm{CH_{3}^{+}}+\mathrm{H}.

FR1, the classifier.The free-rotor orbit on the roaming shelf
(r≈3.18r\approx 3.18–3.653.65Å; Fig.3a), associated with a 2:1
stretch–bend resonance born in a center–saddle bifurcation[12];λFR1=24.57\lambda_{\mathrm{FR1}}=24.57. Its dividing surface does
not separate reactants from products; it is the surface whose crossings are counted.

TTS-PO, the reactive gate.A libration through the symmetry axis, arcing
across the mouth of the well just outside the ridge crest
(r≈2.38r\approx 2.38–2.642.64Å; Fig.3a);λTTS=220.5\lambda_{\mathrm{TTS}}=220.5, the most unstable of the three. Its dividing surface
gates capture into the well.

Trajectories are classified against these three surfaces[12,13]. Initial conditions are sampled on the
inward-crossing half of the OTS surface (pr<0p_{r}<0) and integrated until they cross
the TTS surface (reactive) or recross the OTS surface outward (non-reactive);
crossings of the FR1 surface are counted along the way. A trajectory roams when it
crosses the FR1 surface at least three times (reactive; the count is odd) or at
least four times (non-reactive; even), and is direct otherwise. The classification
refers only to the three surfaces; the orbits enter as their anchors. All
computations in this paper are atE=0.5E=0.5kcal mol-1above the dissociation
threshold, the regime of the 2-DoF studies[12,24]; the one exception is
Section7.3, where the energy dependence of the corrugation effect is computed,
the corrugation depthb​V0b\,V_{0}being comparable to the available energy only near
threshold.

## Three degrees of freedom.

Forn=3n=3the energy surface is five-dimensional and a codimension-two NHIM is
three-dimensional: not a periodic orbit. A periodic orbit is one-dimensional and
therefore has codimension four inΣE\Sigma_{E}; its stable and unstable manifolds have
dimension at most three, codimension two, and cannot separateΣE\Sigma_{E}(Table1). The three orbits above therefore cannot anchor dividing
surfaces in the 3-DoF model.

Section6constructs the three-dimensional NHIMs from theb=0b=0symmetry. Atb=0b=0the azimuthϕ\phiis cyclic andpϕp_{\phi}is conserved; at each
fixedpϕp_{\phi}the reduced system is a two-degree-of-freedom system carrying reduced
counterparts of the three orbits. The union of these reduced orbits overpϕ∈(−p∗,p∗)p_{\phi}\in(-p_{*},p_{*}), each carrying its azimuthal circle, is a three-dimensional
invariant manifold, and it — not the periodic orbit — anchors the
four-dimensional dividing surface. The planar orbit is recovered in the limitpϕ→0p_{\phi}\to 0; the precise sense in which it is a distinguished member of its family
is treated in Section6.5. The trajectory classification is
unchanged: the same three surfaces and the same crossing counts, with initial
conditions on the OTS surface now sampled overpϕp_{\phi}as well as over the incoming
directions.

What remains computable from a periodic orbit directly is its linear stability
transverse to the plane of motion: whether the couplingbbmakes the out-of-plane
direction unstable. That computation occupies Sections 4–5. FR1 is located on the
reaction plane{Y=0,pY=0}\{Y=0,\,p_{Y}=0\}(Section2(iii)) by symmetric shooting and continued inbbandEE(AppendixC); atb=0b=0it reduces to the 2-DoF orbit,X0=3.179X_{0}=3.179Å,
periodT=5.929T=5.929, action13.75513.755.Figure 3:The three periodic orbits of the 2-DoF model atb=0b=0,pϕ=0p_{\phi}=0,E=0.5E=0.5kcal mol-1. In three degrees of freedom each is the planar limit (pϕ→0p_{\phi}\to 0) of a three-dimensional NHIM (Section6) and does not itself anchor a dividing surface. (a) TTS-PO (red), librating through the symmetry axis and arcing across the mouth of the well just outside the ridge crest,r≈2.38r\approx 2.38–2.642.64Å, and FR1 (blue),r≈3.18r\approx 3.18–3.653.65Å; the marker at the origin is theCH3+\mathrm{CH_{3}^{+}}center of mass. (b) OTS-PO (green) at the centrifugal barrier,r0≈13.4r_{0}\approx 13.4Å; FR1 shown for scale. (c) On-axis potentialVCH​(r)V_{\mathrm{CH}}(r)with the radial range of each orbit shaded;E=0.5E=0.5kcal mol-1dashed. (d) Floquet multiplierλ\lambda(defined in Section3.2): the FR1 family overpϕp_{\phi}, decreasing fromλ=24.57\lambda=24.57atpϕ=0p_{\phi}=0(Section6), and, on the logarithmic scale, the values for TTS-PO (λ=220.5\lambda=220.5) and OTS-PO (λ=1.13\lambda=1.13) atpϕ=0p_{\phi}=0.

## 3.3Linear stability and the transverse direction

Whether the third degree of freedom is dynamically active is decided by the linear stability of the orbit FR1 in the out-of-plane direction — the direction opened up by that degree of freedom and absent from the 2-DoF problem. The monodromy matrix of the orbit, obtained by integrating the variational equations over one period, block-decomposes because the orbit lies in the reaction plane: an in-plane block (the coordinatesr,θr,\thetaand their conjugates, inherited from the 2-DoF dynamics) and a transverse block (the out-of-plane pairY,pYY,p_{Y}). The transverse block is the new content. The trace of the transverse block decides whether a trajectory nudged off the reaction plane is restored to it — elliptic motion, the perturbation bounded and quasiperiodic, the out-of-plane direction inert — or departs from it: hyperbolic motion, the perturbation growing exponentially, the out-of-plane direction an escape direction. The value−2-2marks the transverse period-doubling between them.

## 4Results: phase-space geometry versus coupling and energy

## 4.1The FR1 orbit and its action

AtE=0.5E=0.5kcal mol-1andb=0b=0the planar orbit coincides with the 2-DoF
orbit by the reduction of Section2: the computed abbreviated actionW=∮p⋅𝑑qW=\oint p\cdot dq, evaluated along the orbit as∮2​T​𝑑t\oint 2T\,dt, is13.75513.755,
against the 2-DoF value13.75513.755, with matching period and turning points. The
action also discriminates between the two branches admitted by the symmetric
shooting: the correct orbit and a spurious wide branch of smaller action
(≈12.6\approx 12.6) onto which over-large continuation steps can jump
(AppendixC). Continued inbbwithin the reaction plane, the orbit deforms
smoothly: byb≈0.57b\approx 0.57the inner turning point has moved from3.183.18to2.672.67Å, the outer staying near3.653.65Å, and the action rises from13.813.8to14.414.4, about four percent. The reaction plane is invariant for everybb(Section2(iii)), and within it the dynamics is a
two-degree-of-freedom system in which FR1 anchors a periodic-orbit dividing surface
whose flux is this action. The four-percent change states that the coupling barely
alters the planar subsystem; its decisive effect is transverse to the plane, to
which we now turn.

## 4.2The transverse period-doubling bifurcation

The transverse trace (Fig.4) equals+2+2exactly atb=0b=0, as
conservation ofpϕp_{\phi}requires, and rises above+2+2immediately: the
out-of-plane direction is hyperbolic for allb>0b>0outside the narrow elliptic
window0.58≲b≲0.630.58\lesssim b\lesssim 0.63, which is terminated by a transverse
period-doubling atbc≈0.63b_{c}\approx 0.63. Arbitrarily weak coupling produces positive transverse hyperbolicity, so the
initial instability has no finite threshold; after the narrow elliptic
restabilization window, the crossing oftr​M⟂=−2\mathrm{tr}\,M_{\perp}=-2atbcb_{c}marks
the onset of negative hyperbolicity through a period-doubling bifurcation. With the spherical ratioIz=IxI_{z}=I_{x}the small-bbbehavior is instead elliptic: the transverse character is fixed jointly by theC3C_{3}coupling and the oblate inertiaIz=2​IxI_{z}=2I_{x}, and neither alone suffices.

The four multipliers normal to the flow within the energy surface make this quantitative: atb=0.30b=0.30the hyperbolic pair of the planar orbit is{24.6,0.041}\{24.6,\ 0.041\}— the normal rate that Section6inherits — and the transverse pair is{2.40,0.42}\{2.40,\ 0.42\}, quantifying the instability.

Hyperbolic or not, the orbit is one-dimensional; its stable and unstable manifolds
are three-dimensional, codimension two in the five-dimensional energy surface, and
do not separate it. What the transverse instability supplies is the ingredient the
planar orbit lacks — a genuine out-of-plane expanding direction. How that
direction relates to the three-dimensional manifold of the FR1 transition state is
answered by constructing the manifold (Section6); the relationship
between the orbit and its family is made precise in Section6.5.

Figure5in Section5shows the consequence directly: a trajectory displaced out of the reaction plane has a bounded out-of-plane excursion atb=0b=0and a geometrically growing one for representativeb>0b>0outside the elliptic window.Figure 4:Trace of the transverse block of the monodromy matrix of the FR1 orbit versus the azimuthal couplingbb, atE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}with the physical inertia ratioIz=2​IxI_{z}=2I_{x}and the methyl (cos⁡3​ϕ\cos 3\phi) coupling of Eq. (4). The shaded band|trace|<2|\mathrm{trace}|<2is the elliptic (transverse-stable) regime. The trace rises above+2+2immediately aboveb=0b=0— the out-of-plane direction is hyperbolic, and the orbit a NHIM — reaches its maximum of≈3.6\approx 3.6nearb≈0.45b\approx 0.45, turns elliptic in the narrow window nearb≈0.6b\approx 0.6, and undergoes a transverse period-doubling (trace=−2=-2) atbc≈0.63b_{c}\approx 0.63.

## 5Dimensionality of roaming: the formaldehyde–acetaldehyde contrast

Whether roaming requires a three-dimensional description, or a planar model captures
it, distinguishes the two systems in which roaming has been studied since its
identification: formaldehyde and acetaldehyde[3,20]. Setting the present model
against that contrast motivates its construction and fixes the chemical reading of
the transverse instability found above.

In formaldehyde, a reduced two-degree-of-freedom phase-space model — the roaming H atom moving in a plane relative to a rigid HCO fragment — reproduces the roaming mechanism inH2​CO\mathrm{H_{2}CO}decomposition[3,18], and the reduction has been validated against full-dimensional quasiclassical trajectory studies[19]. The reduction is faithful for a dynamical reason rather than by accident: at the large fragment separations where roaming occurs the relevant angular momentum is nearly conserved on an essentially fixed plane, the angular and radial motions decouple, and a centrifugal barrier provides the gatekeeping. Formaldehyde is thus the prototype in which roaming is in-plane and centrifugal-barrier-mediated, and in which the out-of-plane direction is not where the mechanism resides.

In acetaldehyde the third degree of freedom is essential. Roaming in the photodissociation ofCH3​CHO\mathrm{CH_{3}CHO}toCH4+CO\mathrm{CH_{4}}+\mathrm{CO}was identified experimentally by Houston and Kable, from CO product-state distributions the conventional transition state cannot account for[26], and corroborated by slice-imaging measurements[27]; combined experiment and full-dimensional quasiclassical trajectories on a global potential energy surface then established roaming as the dominant channel to the molecular products, proceeding by abstraction of an H atom from HCO by the methyl group[28,29]. Here the roaming partner is a methyl group rather than a hydrogen atom, and full-dimensional trajectory studies, supplemented by a restricted two-degree-of-freedom model, reveal two disjoint roaming pathways[20]: a long-range channel, with maximumCH3\mathrm{CH_{3}}–HCO separations of roughly14.514.5–22.9​a.u.22.9\ \mathrm{a.u.}, that the in-plane model reproduces and that proceeds, formaldehyde-like, through a centrifugal barrier; and a short-range channel, near99–11.5​a.u.11.5\ \mathrm{a.u.}, that the in-plane model cannot produce and in which the fragment undergoes substantially more rotation — the signature of active out-of-plane motion. That the heavier roaming fragment is not by itself the explanation is established within Chesnavich’sCH4+\mathrm{CH_{4}^{+}}model itself: varying the mass of the roaming fragment does not significantly change the roaming propensity[14]. What distinguishes acetaldehyde is therefore not mass but the presence of a second, out-of-plane pathway absent from the planar description.

The one-parameter familyHbH_{b}interpolates between these two situations along precisely the axis the contrast identifies. Atb=0b=0the model is cylindrically symmetric,pϕp_{\phi}is conserved, and the azimuthal degree of freedom is decoupled, each trajectory confined to itspϕp_{\phi}-leaf — the analog of the in-plane, angular-momentum-conserving regime in which formaldehyde is effectively two-dimensional. Increasingbbresolves the three-fold azimuthal structure of the methyl frame and couples the out-of-plane motion in — the analog of activating the out-of-plane participation that acetaldehyde displays. The spatial structure of the coupling reinforces the parallel. The corrugation it introduces is strongest at the inner edge of the roaming shelf, whereV0V_{0}remains of order the roaming energy, and fades asV0→0V_{0}\to 0at largerr(Section3.1); the model therefore carries its out-of-plane structure at short range and leaves the long-range motion in-plane — the same short-range/long-range division of labour that separates the two acetaldehyde channels.

What the model contributes beyond the empirical contrast is a direct, quantitative measure — computed within a single tractable system — of when the third degree of freedom becomes dynamically active. We probe it with trajectories launched from initial conditions displaced a small distanceδ\deltaout of the reaction plane from a point of the FR1 orbit, following the out-of-plane excursion|Y​(t)||Y(t)|(Fig.5). Atb=0b=0the excursion remains bounded, oscillating at fixed amplitude: the out-of-plane direction is marginal and a trajectory nudged out of the plane is neither restored nor expelled, as the conservedpϕp_{\phi}requires. Once the corrugation is switched on the excursion grows, and it grows faster as the coupling increases — already by an order of magnitude over a few roaming periods atb=0.15b=0.15, and far more steeply byb=0.45b=0.45. The growth is geometric: the excursion grows by the transverse Floquet multiplier of the orbit each period, and this multiplier rises from unity atb=0b=0toλ≈3.6\lambda\approx 3.6nearb≈0.45b\approx 0.45(Section4). Switching on the corrugation thus converts the marginal out-of-plane direction into an unstable one. The single bounded curve atb=0.60b=0.60in Fig.5is the exception that the transverse-stability analysis predicts — the narrow window of transverse re-stabilization just below the period-doubling atbcb_{c}(Section4) — and it does not alter the dominant trend, that the out-of-plane direction is unstable across most of the coupling range.

The computation locates the effect of the corrugation. It is not on the in-plane
reactive flux: the FR1 action rises about four percent byb≈0.57b\approx 0.57and under
seven percent up tobcb_{c}, and the in-plane instability that governs residence on
the shelf (multiplier of order twenty) is essentially unchanged. The effect is the
opening of an out-of-plane component to the roaming motion. The third degree of
freedom does not confine trajectories to the reaction plane; outside the narrow
elliptic window it is transversely unstable, an additional route by which a roaming
trajectory leaves the plane, with no finite threshold inbb(Section4). The model makes concrete what the
formaldehyde–acetaldehyde comparison shows empirically: resolving the discrete
azimuthal structure of the roaming partner activates an out-of-plane degree of
freedom a planar model cannot represent, and it is this activation — not a change
in the in-plane bottleneck — that separates three-dimensional roaming from its
planar reduction.

The correspondence is structural, not quantitative. The model is theCH4+\mathrm{CH_{4}^{+}}system, not formaldehyde or acetaldehyde; the coupling strengthbband the bifurcation valuebcb_{c}have no counterpart in any particular molecule.
And the physical origin of the out-of-plane activation differs: in acetaldehyde the
short-range channel is attributed to short-range repulsive structure absent from the
reduced model, whereas here the coupling arises from theC3C_{3}corrugation of the
attractive bending ridge. What the systems share is the role of the methyl group’s
discrete symmetry and the participation of out-of-plane motion at short range.Figure 5:The model’s internal measure of the dimensional transition. A trajectory is launched from an initial condition displaced a small distanceδ\deltaout of the reaction plane from a point of the FR1 orbit, and the out-of-plane excursion|Y​(t)||Y(t)|is followed over eight periods, atE=0.5E=0.5kcal mol-1with the physical inertia ratioIz=2​IxI_{z}=2I_{x}. Atb=0b=0(cylindrically symmetric,pϕp_{\phi}conserved) the excursion is bounded: the out-of-plane direction is marginal and the dynamics is effectively two-dimensional. Forb>0b>0the excursion grows geometrically and more steeply with increasing coupling (b=0.15,0.30,0.45b=0.15,0.30,0.45), the trajectory leaving the plane geometrically, by the transverse Floquet multiplier each period. The bounded curve atb=0.60b=0.60lies in the narrow window of transverse re-stabilization just below the period-doubling atbcb_{c}(cf. Fig.4).

## 6The NHIMs and their dividing surfaces: explicit construction atb=0b=0and persistence

Section3.2established what each of the three transition states must be in
three degrees of freedom: a four-dimensional dividing surface, anchored on a
three-dimensional NHIM whose four-dimensional stable and unstable manifolds
partition the energy surface[9,17]. A periodic orbit —
one-dimensional, with two-dimensional stable and unstable manifolds — is not that
object. This section constructs the three NHIMs and the dividing surfaces they
anchor, and proves that every compact interior piece of each survives
sufficiently small coupling.

The construction rests on theb=0b=0symmetry. Atb=0b=0the azimuthϕ\phiis cyclic
andpϕp_{\phi}is conserved; fixingpϕp_{\phi}and discardingϕ\phireduces the
dynamics to two degrees of freedom (Section6.1). For each fixedpϕp_{\phi}the reduced system carries three unstable periodic orbits, the counterparts
at that angular momentum of the three orbits of Section 3. Collecting the orbits of
one type over the admissible range ofpϕp_{\phi}, and restoring the azimuthal angle
that the reduction removed, yields a three-dimensional invariant manifold — one
for each transition state (Section6.2).
Section6.3verifies that each manifold is normally hyperbolic.
Section6.4constructs the dividing surface each manifold anchors and
determines its topology, following at each fixedpϕp_{\phi}the construction of
Mauguière, Collins, Kramer, Carpenter, Ezra, Farantos, and Wiggins for ozone[13]; what is taken from that work and
what the present setting adds is stated there. Section6.5settles
the relation between the planar orbit FR1 and the manifold it generates: the orbit
is a distinguished member of its family, in a sense made precise there, and the
marginal transverse stability found in Section4is the signature of
that status. Section6.6proves persistence of the compact interior
pieces for sufficiently smallb>0b>0; the trajectory study of Section 7
stands on its own measurements, theb=0b=0construction supplying the
surface placement it uses (Section7.6).

We carry out each step for FR1 in detail; the OTS and TTS manifolds follow by the
same construction, and the points at which they differ are recorded where they
occur.

## 6.1Symmetry reduction atb=0b=0

Atb=0b=0the coupling (4) reduces toV0​(r)​sin2⁡θV_{0}(r)\sin^{2}\theta, the
potential depends on(r,θ)(r,\theta)alone, the azimuthϕ\phiis cyclic, and the
azimuthal angular momentumpϕ=Lzp_{\phi}=L_{z}is conserved. Conservation ofpϕp_{\phi}is
exact, and we use it as a check on the numerical integration and on the coded
equations of motion: on a generic non-planar, non-axial trajectory the integrator
holdspϕp_{\phi}constant to1×10−111\times 10^{-11}, and the energy to3×10−103\times 10^{-10},
over an integration time of6060. Fixingpϕp_{\phi}and discarding the cyclic angleϕ\phiyields the two-degree-of-freedom reduced Hamiltonian, obtained directly from
(1):Hred​(r,θ,pr,pθ;pϕ)=12​Ix​(pθ2+pϕ2​cot2⁡θ)+pϕ22​Iz+12​m​(pr2+pθ2r2+pϕ2r2​sin2⁡θ)+VCH​(r)+V0​(r)​sin2⁡θ.H_{\mathrm{red}}(r,\theta,p_{r},p_{\theta};p_{\phi})=\frac{1}{2I_{x}}\left(p_{\theta}^{2}+p_{\phi}^{2}\cot^{2}\theta\right)+\frac{p_{\phi}^{2}}{2I_{z}}+\frac{1}{2m}\left(p_{r}^{2}+\frac{p_{\theta}^{2}}{r^{2}}+\frac{p_{\phi}^{2}}{r^{2}\sin^{2}\theta}\right)+V_{\mathrm{CH}}(r)+V_{0}(r)\sin^{2}\theta.(5)

Collecting the terms inpϕ2p_{\phi}^{2}, the angular momentum enters only through the
effective centrifugal potentialU​(r,θ;pϕ)=pϕ2​[12​m​r2​sin2⁡θ+cot2⁡θ2​Ix+12​Iz]U(r,\theta;p_{\phi})=p_{\phi}^{2}\!\left[\frac{1}{2mr^{2}\sin^{2}\theta}+\frac{\cot^{2}\theta}{2I_{x}}+\frac{1}{2I_{z}}\right],
which diverges at the polesθ=0,π\theta=0,\piforpϕ≠0p_{\phi}\neq 0, vanishes identically
atpϕ=0p_{\phi}=0, and contains the only appearance ofIzI_{z}(Section2.4).

Atpϕ=0p_{\phi}=0equation (5) is the two-degree-of-freedom Chesnavich model
of Section2[24,12], whose orbits are those of
Sections 3–5.

## 6.2The families of reduced orbits and the two-component
manifolds

For each fixedpϕp_{\phi}the reduced system (5) possesses, in each of the
three regions, an unstable periodic orbit — the counterpart, at that angular
momentum, of the corresponding planar orbit of Section 3. We denote the FR1-type
reduced orbit byγpϕ\gamma_{p_{\phi}}, reserving the names FR1, OTS-PO, TTS-PO for the
planar orbits atpϕ=0p_{\phi}=0; we treat the FR1 family explicitly and return to the
other two below. Each orbit is located by symmetric shooting
(AppendixC). Forpϕ≠0p_{\phi}\neq 0it is arelativeperiodic orbit:
it closes in the reduced variables(r,θ,pr,pθ)(r,\theta,p_{r},p_{\theta})after the periodT​(pϕ)T(p_{\phi})of the reduced orbit, while the azimuth advances, so the full-space
motion need not close. Because (5) depends onpϕp_{\phi}only throughpϕ2p_{\phi}^{2}, the reduced orbits at±pϕ\pm p_{\phi}coincide and differ only in the sense
of the azimuthal drift: they form a counter-precessing pair. (These components are
the analog of the counter-propagating pair of[13], though their
role here differs — Section6.4.)

Continuation inpϕp_{\phi}generates a one-parameter family, every member computed at
the same total energyHred=EH_{\mathrm{red}}=E(the isoenergetic convention of
Section3.2). As|pϕ||p_{\phi}|increases, the centrifugal potentialU​(r,θ;pϕ)U(r,\theta;p_{\phi})of Section6.1diverges at the polesθ=0,π\theta=0,\piand confines the orbit away from the axis. Letθ−​(pϕ)\theta_{-}(p_{\phi})denote the smallest polar angle attained on the orbit — the polar turning angle,
at whichpθ=0p_{\theta}=0; by the reflection symmetryθ→π−θ\theta\to\pi-\thetathe orbit
occupies[θ−,π−θ−][\theta_{-},\pi-\theta_{-}]. The turning angle increases monotonically with|pϕ||p_{\phi}|: for the FR1 family from0atpϕ=0p_{\phi}=0to roughly44∘44^{\circ}atpϕ=1.7p_{\phi}=1.7, the radial extent remaining on the roaming shelf,r∈[3.18,3.65]r\in[3.18,3.65]Å, throughout (Fig.6a).

Lifting a member back to the full phase space restores the azimuthal circleϕ∈S1\phi\in S^{1}that the reduction removed. Forpϕ≠0p_{\phi}\neq 0the orbit remains at a
distanceρmin=rt​sin⁡θ−>0\rho_{\min}=r_{t}\sin\theta_{-}>0from the axis, so under the rotation each
point of the orbit sweeps a circle of positive radius, and the lift is a two-torus,𝕋​(pϕ)=⋃ϕ∈S1{reduced orbit at​pϕ,rotated by​ϕ},\mathbb{T}(p_{\phi})=\bigcup_{\phi\in S^{1}}\big\{\text{reduced orbit at }p_{\phi},\ \text{rotated by }\phi\big\},(6)

the product of two circles: the reduced orbit itself, a closed
curve parametrized by the time along it, and the azimuthal circle. The torus is
invariant: the reduced orbit is invariant under the reduced flow, the azimuthal
rotation is a symmetry atb=0b=0, andpϕp_{\phi}is conserved. The candidate NHIM —
the manifold on which the dividing surface will be anchored — is the union of
these tori over the angular momentum,ℳ0=⋃0<|pϕ|<p∗𝕋​(pϕ),\mathcal{M}_{0}=\bigcup_{0<|p_{\phi}|<p_{*}}\mathbb{T}(p_{\phi}),(7)

Every member is computed at the
same total energy and the lift leavesHHunchanged, soℳ0\mathcal{M}_{0}lies in the
single five-dimensional energy surfaceΣE\Sigma_{E}; it is three-dimensional, exactly
the2​n−3=32n-3=3required forn=3n=3(Section3.2).

The union is taken over0<|pϕ|<p∗0<|p_{\phi}|<p_{*}for two reasons. At|pϕ|=p∗|p_{\phi}|=p_{*}the
reduced orbit loses hyperbolicity: its Floquet multiplierλ​(pϕ)\lambda(p_{\phi}),
computed along the family in Section6.3, decreases monotonically
from24.5724.57atpϕ=0p_{\phi}=0to11atp∗=1.799p_{*}=1.799(Fig.3d), and
normal hyperbolicity fails there. Atpϕ=0p_{\phi}=0the construction degenerates: the
centrifugal potential vanishes identically, the orbit reaches the poles, and the
azimuthal circle shrinks to a point on the axis.

Consequentlyℳ0\mathcal{M}_{0}has two disjoint components,ℳ0+={q∈ℳ0:pϕ​(q)>0},ℳ0−={q∈ℳ0:pϕ​(q)<0},\mathcal{M}_{0}^{+}=\{q\in\mathcal{M}_{0}:p_{\phi}(q)>0\},\qquad\mathcal{M}_{0}^{-}=\{q\in\mathcal{M}_{0}:p_{\phi}(q)<0\},

the counter-precessing components, each homeomorphic toT2×(0,p∗)T^{2}\times(0,p_{*}). The argument
is direct:pϕp_{\phi}is continuous onℳ0\mathcal{M}_{0}and never zero there, so a path
inℳ0\mathcal{M}_{0}fromℳ0+\mathcal{M}_{0}^{+}toℳ0−\mathcal{M}_{0}^{-}would carrypϕp_{\phi}continuously from a positive to a negative value and would have to pass throughpϕ=0p_{\phi}=0, whichℳ0\mathcal{M}_{0}excludes. The two components are exchanged by the
map(ϕ,pϕ)↦(−ϕ,−pϕ)(\phi,p_{\phi})\mapsto(-\phi,-p_{\phi}), a symmetry ofHH—pϕp_{\phi}enters
only aspϕ2p_{\phi}^{2}, and the coupling is even inϕ\phi— which carries one
component onto the other. Parametrising each reduced curveγpϕ\gamma_{p_{\phi}}by a
phases∈S1s\in S^{1}, the time along the orbit moduloT​(pϕ)T(p_{\phi}), each component is, in
the variables(s,pϕ)(s,p_{\phi}), the open annulusS1×(0,p∗)S^{1}\times(0,p_{*}); the wordannularbelow refers to one component in this sense.

The exclusion ofpϕ=0p_{\phi}=0is a genuine singularity of the family, not a coordinate
artifact. Near the axis the centrifugal potential grows aspϕ2/(2​m​r2​θ2)p_{\phi}^{2}/(2mr^{2}\theta^{2}), so the turning angle at which it balances the available
energy scales linearly in the momentum,θ−​(pϕ)=k​|pϕ|+O​(pϕ2)\theta_{-}(p_{\phi})=k|p_{\phi}|+O(p_{\phi}^{2}); Proposition4makes this
precise. The closest approach to the axis is thenρmin=rt​sin⁡θ−≃rt​k​|pϕ|≃1.69​|pϕ|\rho_{\min}=r_{t}\sin\theta_{-}\simeq r_{t}k|p_{\phi}|\simeq 1.69\,|p_{\phi}|, with the
outer radial turning pointrt≈3.65r_{t}\approx 3.65Ånearly constant across the family.
In body-frame Cartesian coordinates the locus the family traces near a polar turning
point is therefore the double coneX2+Y2≃(1.69​pϕ)2X^{2}+Y^{2}\simeq(1.69\,p_{\phi})^{2}, whose apex, on
the axis atpϕ=0p_{\phi}=0, is a conical singularity; a quadratic lawθ−∝pϕ2\theta_{-}\propto p_{\phi}^{2}would give a smooth tangency instead. The two nappes of
the cone are the two components, meeting only at the excluded apex.

The structure just described is afibration, and we fix the vocabulary here
because it is used throughout Sections 6.3–6.6. For a functionffand a valuecc,
thepreimagef−1​(c)f^{-1}(c)is the set of points at whichfftakes the valuecc. Onℳ0\mathcal{M}_{0}the function is the conserved momentumpϕp_{\phi}, and the
preimage of a single value is the single torus𝕋​(pϕ)\mathbb{T}(p_{\phi}): thefiberover that value. The essential property of a fiber is that it is a
regular, interchangeable member of its family: near any value ofpϕp_{\phi}the
manifold is a product, torus×\timesinterval, and varyingpϕp_{\phi}deforms each
torus smoothly into its neighbors, every member alike in kind. (In the reduced
variables the same picture is the family of curvesγpϕ\gamma_{p_{\phi}}over the
momentum interval — the open annulus above — with the curves as fibers.) The
valuepϕ=0p_{\phi}=0is excluded from (7), and the natural question is whether
the planar orbit FR1 completes the family there, as the fiber overpϕ=0p_{\phi}=0.
Section6.5shows that it does not: FR1 is related to the family
not as a fiber but as aseparatrix— not a member of the family but a
boundary between the two, and what it separates, in which variables, is made precise
there.

## 6.3Normal hyperbolicity of each component

For a point onℳ0\mathcal{M}_{0}the three tangent directions are the flow, the
infinitesimal azimuthal rotation, and the family direction∂/∂pϕ\partial/\partial p_{\phi}; normal hyperbolicity requires the remaining directions — normal toℳ0\mathcal{M}_{0}, i.e. transverse to it — to expand and contract at rates that
strictly dominate any tangential growth[21,22,23]. The
instrument is the monodromy matrix of each reduced relative orbit, computed in the
full six-dimensional phase space: the6×66\times 6matrixMRPO=R​(−Δ​ϕ)​D​ΦTM_{\mathrm{RPO}}=R(-\Delta\phi)\,D\Phi_{T}, whereD​ΦTD\Phi_{T}is the linearization of
the flow over one periodT​(pϕ)T(p_{\phi})of the reduced orbit, obtained by integrating
the variational equations of (1) along the orbit
(AppendixC),Δ​ϕ\Delta\phiis the azimuthal advance accumulated
over that period, andR​(−Δ​ϕ)R(-\Delta\phi)is the rotation about the symmetry axis
through−Δ​ϕ-\Delta\phi— the rotation that closes the relative orbit. Its
eigenvalues are{λ,λ−1,1,1,1,1},\{\lambda,\ \lambda^{-1},\ 1,\ 1,\ 1,\ 1\},(8)

the algebraic multiplicity of the eigenvalue11being exactly four.

The count of unit eigenvalues encodes the geometry, and is worth setting out once:
each conserved quantity contributes two, in a2×22\times 2block. For the energy: the
flow direction returns to itself after one period — an eigenvector with eigenvalue11— and paired with it is the direction of increasing energy, along which the
orbit continues as a one-parameter family; because the period varies withEE, this
paired direction is in general not an eigenvector but completes a2×22\times 2Jordan
block. For the angular momentum: the rotation direction is likewise an eigenvector,
the rotation commuting with the flow atb=0b=0, and the family direction∂/∂pϕ\partial/\partial p_{\phi}completes the second block, the period varying withpϕp_{\phi}. The two conserved quantitiesHHandpϕp_{\phi}thus account for the four
unit eigenvalues — algebraic multiplicity four, geometric multiplicity two — and
the remaining pair{λ,λ−1}\{\lambda,\lambda^{-1}\}, reciprocal becauseMRPOM_{\mathrm{RPO}}is symplectic, is the normal pair. The monodromy matrix is
computed in the full six-dimensional phase space; of the four unit directions, the
energy direction is transverse to the energy surfaceΣE\Sigma_{E}and is set aside,
and normal hyperbolicity is the statement about the remaining directions withinΣE\Sigma_{E}(Section3.2).

Atpϕ=0p_{\phi}=0the computation recovers the planar orbit of
Section4— multipliers{24.57,0.0407,1,1,1,1}\{24.57,\,0.0407,\,1,1,1,1\}, inner
turning pointX0=3.17907X_{0}=3.17907, periodT=5.92863T=5.92863, action13.754813.7548against13.75513.755from the 2-DoF computation[24], orbit closure3.5×10−143.5\times 10^{-14}. The
two computations must agree there, since atpϕ=0p_{\phi}=0the reduced system is the
2-DoF model (Section6.1); the agreement checks the six-dimensional
machinery at the one point where the answer is known independently. That the
hyperbolic pair is normal — acting transversally toℳ0\mathcal{M}_{0}, not along it
— is confirmed by the spectral projector onto the hyperbolic eigenspace: the flow
and rotation directions are eigenvectors of eigenvalue11to residuals∼10−14\sim 10^{-14}, and all three tangent directions have components≲10−13\lesssim 10^{-13}in the hyperbolic eigenspace (∼10−5\sim 10^{-5}for the
finite-difference family direction), so the expanding and contracting directions are
transverse toℳ0\mathcal{M}_{0}.MRPOM_{\mathrm{RPO}}is symplectic —D​ΦTD\Phi_{T}because the variational flow of a Hamiltonian system is symplectic,R​(−Δ​ϕ)R(-\Delta\phi)because rotations are canonical transformations — and, as
numerical checks of this,detMRPO=1\det M_{\mathrm{RPO}}=1and the eigenvalues occur in
reciprocal pairs (AppendixE).

The hyperbolic pair persists, real and bounded away from unity, across the FR1
family:λ​(pϕ)\lambda(p_{\phi})decreases monotonically from24.5724.57atpϕ=0p_{\phi}=0to≈2.1\approx 2.1atpϕ=1.7p_{\phi}=1.7, reaching11atp∗=1.799p_{*}=1.799, where the orbit turns
elliptic and normal hyperbolicity is lost (Fig.6b). At every interior
value ofpϕp_{\phi}the multiplier is real and greater than one, so the family loses
hyperbolicity only at its endpoint. The tangential rate is identically zero atb=0b=0— the tangential dynamics is a periodic flow, a rigid rotation, and the neutral
sweep ofpϕp_{\phi}— and in particular the out-of-plane pair(Y,pY)(Y,p_{Y})lies in the
unit eigenspace, tangent toℳ0\mathcal{M}_{0}. With the tangential rate exactly zero,
the normal rates dominate any power of tangential growth, and each component ofℳ0\mathcal{M}_{0}is normally hyperbolic on every closed sub-annulusε≤|pϕ|≤p∗−δ\varepsilon\leq|p_{\phi}|\leq p_{*}-\deltabounded away from both ends, the normal rateν=ln⁡λ/T\nu=\ln\lambda/Trunning from0.540.54near the center to zero atp∗p_{*}(Fig.6c).Figure 6:The two-component NHIM of FR1 atb=0b=0,E=0.5E=0.5. (a) The family of reduced orbits in the meridional plane(ρ,Z)(\rho,Z),ρ=X2+Y2\rho=\sqrt{X^{2}+Y^{2}}, for several values of the angular momentumpϕp_{\phi}; markers show the polar turning points, which move away from the symmetry axis (the poles) aspϕp_{\phi}increases while the orbits stay on the roaming shelf. Lifting this family over the azimuthal circle and assembling overpϕ∈(0,p∗)p_{\phi}\in(0,p_{*})(plus the−pϕ-p_{\phi}counterpart) produces the two-component three-dimensional manifold (7). (b) The normal Floquet multiplierλ​(pϕ)\lambda(p_{\phi})(logarithmic scale): real and bounded away from unity throughout,λ\lambdareal and greater than one at every interiorpϕp_{\phi}, decreasing toλ=1\lambda=1at the boundaryp∗=1.799p_{*}=1.799where the orbit turns elliptic. (c) The spectral gap: the normal Lyapunov rateν=ln⁡λ/T\nu=\ln\lambda/T(shaded) is strictly positive on the interior while the tangential rate is identically zero, so the gap is open everywhere inside|pϕ|<p∗|p_{\phi}|<p_{*}.

## 6.4The dividing surface and its topology

The construction of the dividing surface at the level of the reduced
two-degree-of-freedom system is due to Mauguière, Collins, Kramer,
Carpenter, Ezra, Farantos, and Wiggins, who developed it in their phase-space
analysis of roaming in ozone[13]— a system of the same
structural type as the present model atb=0b=0: three degrees of freedom
reducing to two at each fixed value of a decoupling parameter, there the
adiabatically conserved energy of the third mode, here the exactly conservedpϕp_{\phi}. Since this subsection leans on their results, we state precisely
what is taken from that work, what is adapted from it, and what does not
arise there. From[13]we take the complete reduced theory:
for an unstable periodic orbit of a two-degree-of-freedom system of this
kinetic form, at fixed energy, (i) the topology of the dividing surface is
decided by whether the generating orbitlibrates— oscillating
between two turning points at which its momentum ellipse degenerates to a
point — orcirculates, never meeting such a degeneration (their
type 1 and type 2 orbits, respectively); (ii) a librating orbit yields a
dividing surface that is a two-sphere, on which the orbit is a dividing
equator separating the two hemispheres, the forward and backward crossing
directions; (iii) a circulating orbit yields instead a two-torus, and —
the subtle point of that work — a single circulating orbit doesnotseparate its torus: the dividing surface must be assembled from the orbitand its counter-precessing component, and only the pair divides; and
(iv) a flux form certifies that the Hamiltonian vector field is transverse
to the surface everywhere off the generating orbit, so the surface is
locally free of recrossing. Both types occur in their ozone analysis. The
assembly over the third degree of freedom is likewise adapted from that
work: there the four-dimensional dividing surface is a union of leaves over
the adiabatic partition of energy between the reactive pair and the
decoupled vibration; here it is a union of leaves over the exactly conserved
momentumpϕp_{\phi}, each leaf the lift of a reduced surface over the
reconstructed azimuthal circle. What does not arise there follows from the
difference in parameter: their energy partition runs over a half-line, whilepϕp_{\phi}runs over a signed interval, producing the two counter-precessing
components and the conical center with its separatrix orbit
(Sections6.2,6.5); and since their third
degree of freedom decouples adiabatically rather than through an exact
symmetry broken by a coupling, the persistence question of
Section6.6has no analog there.

The reduced theory applies verbatim because the reduced system
(5) is, in form, identical to the one analyzed there: withq1=rq_{1}=r,q2=θq_{2}=\theta, reduced massmm, and the inertiaIxI_{x}, the reduced
kinetic energypθ2​(12​Ix+12​m​r2)p_{\theta}^{2}(\tfrac{1}{2I_{x}}+\tfrac{1}{2mr^{2}})is exactly the
form treated in[13], with the centrifugal terms folding
into the effective potentialU​(r,θ;pϕ)U(r,\theta;p_{\phi})of (5). For
everypϕ≠0p_{\phi}\neq 0the reduced FR1 orbit librates between twoθ\theta-turning points at whichbothreduced momenta vanish — the
degeneration of the momentum ellipse that the sphere case requires,
established numerically in AppendixE— so its
reduced dividing surface is a two-sphere with the orbit as a dividing
equator through the two degenerate points. The flux form — Eq. (B12c) of[13], written in the present variables —φ=1−m​pθI1​(r)​pr​d​rd​θ|PO,1I1=1Ix+1m​r2,\varphi\;=\;1-\frac{m\,p_{\theta}}{I_{1}(r)\,p_{r}}\,\frac{dr}{d\theta}\bigg|_{\mathrm{PO}},\qquad\frac{1}{I_{1}}=\frac{1}{I_{x}}+\frac{1}{mr^{2}},(9)

in which the momenta are those of the surface point under test while the
derivatived​r/d​θdr/d\thetais taken along the orbit’s configuration-space
projection, vanishes precisely at the orbit’s two momentum points on each
momentum ellipse — the inbound and outbound crossings — and is nonzero
elsewhere, so the Hamiltonian vector field is transverse to the surface off
the orbit and there is no local recrossing.

Restoring the azimuthal circle lifts this picture by one dimension
(Fig.7). At a fixed nonzero angular momentumpϕp_{\phi}every point
of the reduced dividing surface is carried around the azimuthal angleϕ\phi,
which itself runs over a circleS1S^{1}; because the reduced surface lies entirely
off the symmetry axis,ϕ\phiis a single-valued coordinate there and the lift
is a global product (6) (Proposition3). The
reduced dividing surface is a two-sphereS2S^{2}(the surface of a ball), so its
lift is the productS2×S1S^{2}\times S^{1}: a sphere’s worth of points, each carried
once around a circle. On that sphere the reduced orbit is an equator; carried
around the azimuthal circle it sweeps out a two-torus𝕋​(pϕ)\mathbb{T}(p_{\phi})(the
surface of a doughnut), which is the slice of the NHIM. Cutting a sphere along
its equator leaves two caps, each a diskD2D^{2}; performing the same cut once the
azimuthal circle has been attached separatesS2×S1S^{2}\times S^{1}along the NHIM
torus into twosolid tori(solid doughnutsD2×S1D^{2}\times S^{1}),(S2×S1)∖(equator×S1)=(S2∖equator)×S1=(D2⊔D2)×S1,(S^{2}\times S^{1})\setminus(\text{equator}\times S^{1})=(S^{2}\setminus\text{equator})\times S^{1}=(D^{2}\sqcup D^{2})\times S^{1},

where⊔\sqcupdenotes disjoint union. The two pieces are the forward and
backward halves of the dividing surface, each bounded by the NHIM and each
carrying one crossing direction. The full
four-dimensional dividing surface is the union of these three-dimensional
slices over each component of the manifold. Two features distinguish this
from the two-degree-of-freedom case. First, the NHIM torus at a single value
ofpϕp_{\phi}already divides its own slice — the reduced surface is a
sphere, and an equator separates a sphere — so the counter-precessing component
isnotneeded to obtain a dividing surface at fixedpϕp_{\phi}, in
contrast to the circulating (type-2) case of[13]. Second,
the pairing is global rather than local: the+pϕ+p_{\phi}and−pϕ-p_{\phi}components are the two disjoint components ofℳ0\mathcal{M}_{0},
meeting only through the excluded singular apex.

A reader of[13]might expect both types to appear among the
three transition states, as they do in ozone, where the tight orbits librate
and the orbiting orbit circulates. The realization here is different, and
the geometry forces it. Forpϕ≠0p_{\phi}\neq 0no coordinate of the reduced
system is periodic: the centrifugal barrier walls off both poles, confiningθ\thetato an interval, andrris not an angle. Circulation is therefore
impossible, and every member of all three families librates, with two
genuine turning points at which both reduced momenta vanish
(AppendixE): the FR1- and OTS-type members across the
equator, between the polar turning anglesθ−​(pϕ)\theta_{-}(p_{\phi})andπ−θ−​(pϕ)\pi-\theta_{-}(p_{\phi}); the TTS-type members on one side of the equator,
their planar limit librating through the axis withθmax≈41∘\theta_{\max}\approx 41^{\circ}. Each reduced dividing surface is a
two-sphere, and every lifted slice isS2×S1S^{2}\times S^{1}cut into two solid
tori, uniformly across the three families and the whole momentum interval.
The circulating type is nonetheless present in the model — precisely at
the excluded center. Atpϕ=0p_{\phi}=0the planar FR1rotates:θ\thetaadvances by2​π2\pieach period whilerroscillates twice — the2:12{:}1resonance — andpθp_{\theta}never vanishes; the planar OTS-PO is the
orbiting relative equilibrium at the centrifugal barrier, a rotation
likewise[12,24].
Only the planar TTS-PO librates, through the axis. For FR1 and OTS the type
classification is thus realized across the singular center rather than
across the families: circulating exactly on the excluded planar orbit,
librating on every member — one more respect in which the generating orbit
differs in kind from the family it bounds. That difference — membership
against boundary, fiber against separatrix — has no analog in the
reduced theory, and it, rather than any distinction of surface topology, is
what organizes this model. We turn to it now.Figure 7:Lifting the dividing surface from two to three degrees of freedom.
(a) In two degrees of freedom the dividing surface attached to a librating
periodic orbit is a two-sphereS2S^{2}, with the orbit (a NHIM) as a dividing
equator splitting it into forward and backward halves[13].
(b) In three degrees of freedom, at fixed angular momentumpϕ≠0p_{\phi}\neq 0,
the azimuthal circle lifts the sphere to the productS2×S1S^{2}\times S^{1}; the
NHIM slice is now the two-torus𝕋​(pϕ)\mathbb{T}(p_{\phi})— the equator, that
is, the reduced orbit, crossed with the azimuthal circle — and it cutsS2×S1S^{2}\times S^{1}into two solid toriD2×S1D^{2}\times S^{1}, the forward and
backward halves. (c) Assembling overpϕ∈(−p∗,0)∪(0,p∗)p_{\phi}\in(-p_{*},0)\cup(0,p_{*})produces
a two-component NHIM, one component per precession sense
(ℳ0±\mathcal{M}_{0}^{\pm}), each open at both ends: at the inner boundary, the
excluded singular center atpϕ=0p_{\phi}=0, where each transition state has its
own axis-crossing planar orbit — the separatrix of
Section6.5— and at the outer boundary|pϕ|=p∗|p_{\phi}|=p_{*},
where normal hyperbolicity fails.

## 6.5The orbit FR1 as a separatrix, not a fiber

The families of Section6.2are parametrized over the open
interval0<|pϕ|<p∗0<|p_{\phi}|<p_{*}; the orbit FR1 lies atpϕ=0p_{\phi}=0, outside both
components. Whether FR1 could nonetheless serve as a central fiber
completingℳ0\mathcal{M}_{0}is decided by the limitpϕ→0+p_{\phi}\to 0^{+}, which we
now compute; the precise statements are
Propositions4–5, and the reading of the
marginal transverse multipliers in Section4depends on the
answer. If the family closed up smoothly with FR1 as itspϕ=0p_{\phi}=0fiber,
the polar turning states of the members — whose positions converge to
FR1’s axis-crossing point(rt,θ=0)(r_{t},\theta=0),rt=3.6507r_{t}=3.6507— would converge
to states of FR1. At a polar turning point both reduced momenta vanish
(hypothesis (H)(i)), so energy conservation there readsE=U​(rt,θ−;pϕ)+V​(rt,θ−)E=U(r_{t},\theta_{-};p_{\phi})+V(r_{t},\theta_{-}), and expanding the effective
centrifugal potential for smallθ\thetaand insertingθ−=k​pϕ\theta_{-}=k\,p_{\phi}gives, aspϕ→0p_{\phi}\to 0,E−VCH(rt)=12​k2(1m​rt2+1Ix)=:ℰ0.E-V_{\mathrm{CH}}(r_{t})\;=\;\frac{1}{2k^{2}}\Big(\frac{1}{mr_{t}^{2}}+\frac{1}{I_{x}}\Big)\;=:\;\mathcal{E}^{0}.

Read one way, this identity determines the constant of the linear law of
Section6.2:k=0.4619k=0.4619, withℰ0=1.1737\mathcal{E}^{0}=1.1737, andρmin=rt​k​|pϕ|=1.686​|pϕ|\rho_{\min}=r_{t}k\,|p_{\phi}|=1.686\,|p_{\phi}|. Read the other way, it states
what the turning states converge to: their canonical momenta all vanish in
the limit —pr=pθ=0p_{r}=p_{\theta}=0exactly,pϕ→0p_{\phi}\to 0— while their
kinetic energy tends toℰ0\mathcal{E}^{0}, because the coefficient ofpϕ2p_{\phi}^{2}inUUdiverges asθ−−2\theta_{-}^{-2}; the limiting states sit at(rt,θ=0)(r_{t},\theta=0)with zero momentum, reached along circulation about the
axis on the shrinking circleρmin\rho_{\min}at azimuthal frequencyϕ˙=2​ℰ0/|pϕ|+O​(1)\dot{\phi}=2\mathcal{E}^{0}/|p_{\phi}|+O(1). On FR1 the axis crossing carries|pθ|=pmax=2.165|p_{\theta}|=p_{\max}=2.165. The turning states therefore do not converge
to states of FR1.

The dynamical name for this situation is a separatrix, and the contrast
promised in Section6.2can now be drawn exactly. Afiber, as defined there, is a regular member of the parametrized
family: interchangeable with its neighbors, deformed smoothly into them by
varyingpϕp_{\phi}, with the manifold locally a product of the fiber and the
parameter interval. Aseparatrixis not a member of a family but a
boundary between families of different character. The canonical picture is
the pendulum, whose phase portrait contains two families of qualitatively
different motion — librations, oscillating between turning points, and
circulations, passing over the top — divided by one exceptional orbit
whose own motion is unlike every neighbor on either side. Membership
against boundary is the whole distinction.

FR1 is a boundary in both available senses. In the parameter:pϕ=0p_{\phi}=0is
the boundary between the two counter-precessing componentsℳ0+\mathcal{M}_{0}^{+}andℳ0−\mathcal{M}_{0}^{-}— the only value at which the
precession sense could change, and precisely the value excluded from both;
the conserved-quantity reading of the same fact, withpϕ=0p_{\phi}=0as the
level set dividing the two senses, is drawn in Section6.6.
In the motion: every member of either family reflects at its polar turning
points — forpϕ≠0p_{\phi}\neq 0the effective centrifugal potentialUUis an
infinite wall at the poles, and the orbit turns atθ−​(pϕ)>0\theta_{-}(p_{\phi})>0without reaching the axis — whereas atpϕ=0p_{\phi}=0the wall vanishes
identically andθ=0\theta=0is simply the minimum of the bending potentialV0​sin2⁡θV_{0}\sin^{2}\theta, the collinear well direction. (This wall is unrelated to
the Chesnavich lock, which is the ridge of the same potential at the
equator.) The planar orbit crosses the axis with maximal|pθ||p_{\theta}|—
indeed it rotates,θ\thetaadvancing monotonically
(Section6.4). Reflection on every fiber; crossing on the
boundary alone. The motion on FR1 differs in kind from the motion on every
member of the family it bounds — the defining property of a separatrix,
exactly as the pendulum’s separatrix passes over the top that every
libration turns back from.

The comparison with the pendulum also locates what is singular here. The
pendulum separatrix is the Hausdorff limit of its neighboring orbits, and
it is an object of the same kind as they are — a solution curve. Here the
limit exists but is of the wrong kind. By Proposition4(b),
the Hausdorff limit of the family is the folded planar orbit together with
the two momentum segments{(rt,θ=0orπ,0,pθ,0):|pθ|≤pmax}\{(r_{t},\theta{=}0\ \text{or}\ \pi,\,0,\,p_{\theta},\,0):|p_{\theta}|\leq p_{\max}\}: a singular set, not an orbit and not a torus. The members do
converge onto FR1 away from the axis; the failure is confined to a polar
layer of angular widthO​(|pϕ|)O(|p_{\phi}|), inside which the centrifugal force
diverges and smooth dependence onpϕp_{\phi}breaks down, and it is there
that the momenta sweep out the extra segments. What fails at the center is
therefore not attainment but fiber structure: the tori converge to no
torus, and the fibration has no fiber overpϕ=0p_{\phi}=0that FR1 could be.
The sharp separation between orbit and family is directional and is made
explicit by the blow-up (Proposition5): on the exceptional
divisor the family lands on two latitude circles, one per precession sense,
while the planar orbits lift to the equator, disjoint from both. FR1 is
excluded fromℳ0\mathcal{M}_{0}by definition — it is not a member of
either family — and no smooth completion exists that could admit it.

This is also the correct reading of the marginal transverse multipliers(+1,+1)(+1,+1)of FR1 atb=0b=0(Section4): at the equatorial
crossing the azimuthal-rotation and family directions span the transverse
plane(Y,pY)(Y,p_{Y}), and both are neutral; the identification degenerates at
the poles, where the rotation field vanishes (the apex), and the
marginality is the linear-stability signature of sitting at the singular
center rather than evidence that the out-of-plane direction is dynamically
inert. The orbit’s genuine instability is the reduced hyperbolic pair{24.57,0.0407}\{24.57,\,0.0407\}. The same statements hold for the entrance and the
reactive gate: each planar orbit crosses the axis through the identical
centrifugal structure — the OTS-PO as a rotation atr≈13.4r\approx 13.4, the
orbiting relative equilibrium, and the TTS-PO as a libration through the
axis over the mouth of the well — so each family carries its own conical
center and its own separatrix orbit, with the per-family constants of
Proposition4(k=0.651k=0.651and0.3040.304). For the TTS one
refinement applies: its planar orbit closes only after two circuits of the
limiting reduced arc, so the family’s period and multiplier converge to
half and to the square root of the planar values
(Proposition4(b)).

## 6.6Persistence and the fate of the two components forb>0b>0

Switching on the coupling breaks the azimuthal symmetry: forb>0b>0the
momentumpϕp_{\phi}is no longer conserved andℳ0\mathcal{M}_{0}is no longer
invariant. What survives is governed by normal hyperbolicity, and the
hypothesis is verified where the manifold exists exactly, atb=0b=0. WithinΣE\Sigma_{E}the manifoldℳ0\mathcal{M}_{0}is three-dimensional; at a point of
the torus𝕋​(pϕ)\mathbb{T}(p_{\phi})its tangent space is spanned by the flow
direction, the azimuthal rotation∂ϕ\partial_{\phi}, and the family direction∂pϕ\partial_{p_{\phi}}, so exactly two directions remain, and these — the
normal bundle — are the stable and unstable directions of the reduced
orbit, the pair{λ​(pϕ),λ​(pϕ)−1}\{\lambda(p_{\phi}),\lambda(p_{\phi})^{-1}\}(Proposition2). The normal rate isln⁡λ​(pϕ)\ln\lambda(p_{\phi})per
period, decreasing fromln⁡24.57≈3.20\ln 24.57\approx 3.20at the inner edge to0atp∗p_{*}; the tangential rate is zero, because the internal motion lies on
invariant tori and separates at most polynomially. Two exclusions define the
domain of the statement, one per boundary: the outer edge is excluded
becauseλ→1\lambda\to 1atp∗p_{*}, where the normal rate vanishes; the center
is excluded because it belongs to neither component — the components are
open there, and FR1 was never inside the manifold whose persistence is at
issue. On any closed sub-annulusε≤|pϕ|≤p∗−δ\varepsilon\leq|p_{\phi}|\leq p_{*}-\deltaeach
component is therefore compact and normally hyperbolic of every order, and
the standard theorems[21,22,23,9]give
persistence: for each smoothness classCrC^{r}there is a range ofbbon
which each component survives as a locally invariantCrC^{r}manifold-with-boundary, together with its stable and unstable manifolds and
the dividing surfaces it carries (Proposition6).

The theorems do not name the range ofbb; the computed rates indicate it.
One identification must be kept straight, because “plane” is doing two
jobs. The normal directions ofℳ0\mathcal{M}_{0}liewithineach
reduced slice — they are the hyperbolic directions of the reduced saddle
— while the out-of-plane directions(Y,pY)(Y,p_{Y})at the planar limit are
spanned by∂ϕ\partial_{\phi}and∂pϕ\partial_{p_{\phi}}and aretangenttoℳ0\mathcal{M}_{0}(Section6.5). The out-of-plane instability
that the coupling generates is therefore growth along the manifold, not
across it, and it is the quantity the tangential rate must be tested
against. The computed values: the multiplier of the planar orbit, which
monitors the normal rate at the manifold’s inner edge, stays atln⁡λ≈3.2\ln\lambda\approx 3.2per period essentially unchanged over the range
studied, while the out-of-plane growth does not exceedln≈1.2\ln\approx 1.2per
period (Section4); the gap3.2>2×1.23.2>2\times 1.2required for
classC2C^{2}stays open throughb≈0.3b\approx 0.3. For the other two families:ln⁡λTTS=5.4\ln\lambda_{\mathrm{TTS}}=5.4per period against a tangential rate of at
most0.250.25forb≤0.4b\leq 0.4, the widest gap of the three; andln⁡λOTS=0.12\ln\lambda_{\mathrm{OTS}}=0.12against a perturbation that is itself
negligible at the orbit, the coupling atr≈13.4r\approx 13.4being proportional
toV0​(13.4)∼10−66V_{0}(13.4)\sim 10^{-66}.

The orbit FR1 requires no persistence theorem: it lies in the reaction
plane for everybb(Section2(iii)), so we continue it fromb=0b=0and compute its stability directly — the central computation of
Section4: transversely hyperbolic forb>0b>0outside the
elliptic window, with the period-doubling atbc≈0.63b_{c}\approx 0.63.

The remaining question is what the symmetry breaking does to the structure
the manifolds organize, and here the wordseparatrixcarries its
classical meaning. Atb=0b=0the sign ofpϕp_{\phi}is conserved, and the level
setpϕ=0p_{\phi}=0separates two qualitatively distinct families of motion —
the two precession senses — exactly as the pendulum separatrix separates
its two senses of rotation; the planar orbit lies in the dividing level set,
and its own motion differs in kind from every member of the families it
bounds (rotation against libration, Section6.4). Forb>0b>0nothing conservespϕp_{\phi}:p˙ϕ=−∂H∂ϕ=3​b​V0​(r)​sin3⁡θ​sin⁡3​ϕ,\dot{p}_{\phi}=-\frac{\partial H}{\partial\phi}=3bV_{0}(r)\sin^{3}\theta\sin 3\phi,

identically zero atb=0b=0and on the plane, nonzero as soon as a trajectory
acquires out-of-plane displacement. The level set no longer separates, and
the two senses communicate. The computation shows the opening directly: a
trajectory launched on a torus𝕋​(pϕ)\mathbb{T}(p_{\phi})of the family
holdspϕp_{\phi}rigid to the printed precision atb=0b=0, haspϕp_{\phi}spread
over0.140.14atb=0.05b=0.05, and atb=0.30b=0.30spreads over more than unity —
crossingpϕ=0p_{\phi}=0within twelve roaming periods, with energy conserved to
one part in10910^{9}. No invariance is contradicted: the persisted sub-annuli
are locally invariant, manifolds-with-boundary through whose edges
trajectories may leave, and the crossing is exit through the inner edge and
passage across the region where the excluded center was. The invariant tori
that foliate each component atb=0b=0do not survive individually; the drift
inpϕp_{\phi}that replaces them is the out-of-plane escape of
Section4seen from the manifold’s side, and it is what the
trajectory classification of Section7measures.

Two remarks close the construction. Roaming has no index-one saddle of the
potential: the manifolds sit over the roaming shelf, the centrifugal
barrier, and the mouth of the well, not over critical points, so the
normal-form construction of a NHIM at a saddle[2]does not apply; the manifolds are instead
exhibited in the symmetric integrable limit and continued, which is why theb=0b=0verification is the load-bearing step. And the period-doubling atbcb_{c}is a bifurcation of the flowonthe manifold, not of the
manifold: it reorganizes the internal dynamics while the normal directions
keep their gap. The rigorous statements — existence and smoothness of the
sub-annuli, their normal hyperbolicity of every order, the leaf topology,
the separatrix structure at the center, and persistence — are collected
and proved in Section6.7. The classification of trajectories
at finitebbis the subject of Section7; the flux
question is not treated in this paper; an entropy-based flux analysis for two-degree-of-freedom Chesnavich-type models is given in[24].

## 6.7Rigorous statements and proofs

The construction of the preceding subsections rests on one input that we
establish numerically and otherwise reason from rigorously. We isolate it as
a standing hypothesis, state the structural results as propositions, and
prove them. Throughout,ΣE⊂ℝ6\Sigma_{E}\subset\mathbb{R}^{6}is the energy surface{H0=E}\{H_{0}=E\}atb=0b=0(five-dimensional),U​(r,θ;pϕ)U(r,\theta;p_{\phi})is the
effective centrifugal potential of (5), andγpϕ\gamma_{p_{\phi}}denotes the symmetric reduced periodic orbit of (5) at angular
momentumpϕp_{\phi}in the FR1 (respectively OTS or TTS) family. The planar
orbits are not members of the families: atpϕ=0p_{\phi}=0the planar FR1 and
OTS-PO rotate and have no turning points (Section6.4), so each
family lives on an open interval and the planar orbit enters only as its
singular limit (Proposition4).

## Standing Hypothesis (H).

AtE=0.5E=0.5andb=0b=0, for each familyF∈{FR1,OTS,TTS}F\in\{\mathrm{FR1},\mathrm{OTS},\mathrm{TTS}\}there isp∗F>0p_{*}^{F}>0such that on the open interval(0,p∗F)(0,p_{*}^{F})the reduced Hamiltonian (5) admits a periodic orbitγpϕ\gamma_{p_{\phi}}dependingC∞C^{\infty}onpϕp_{\phi}, with the following
properties.
- (i)

γpϕ\gamma_{p_{\phi}}is a brake orbit: it has exactly
two turning points, at each of which both reduced momenta vanish,pr=pθ=0p_{r}=p_{\theta}=0.
- (ii)

The reduced monodromy matrix ofγpϕ\gamma_{p_{\phi}}has exactly one pair of multipliers off the unit circle,{λ​(pϕ),λ​(pϕ)−1}\{\lambda(p_{\phi}),\lambda(p_{\phi})^{-1}\}, withλ\lambdareal and greater
than one at everypϕ∈(0,p∗F)p_{\phi}\in(0,p_{*}^{F}).
- (iii)

Along the family,d​T/d​E≠0dT/dE\neq 0andd​Δ​ϕ/d​pϕ≠0d\Delta\phi/dp_{\phi}\neq 0, whereT​(pϕ)T(p_{\phi})is the period andΔ​ϕ​(pϕ)\Delta\phi(p_{\phi})the azimuthal advance of the reconstructed orbit over
one period.
- (iv)

At the endpoints: aspϕ→0+p_{\phi}\to 0^{+},λ\lambdaandTTconverge to the planar values for FR1 and OTS, and toλplanar\sqrt{\lambda_{\mathrm{planar}}}andTplanar/2T_{\mathrm{planar}}/2for TTS. Aspϕ→p∗F−p_{\phi}\to p_{*}^{F-}: for FR1,λ→1\lambda\to 1at finite orbit amplitude; for
OTS and TTS,λ\lambdaremains bounded away from11and the orbit’s
amplitude tends to zero, the family terminating on a saddle-center
equilibrium of the reduced system.

Local existence and smoothness are not assumptions but
consequences of the implicit function theorem: at anypϕp_{\phi}withλ≠1\lambda\neq 1the symmetric-return (Poincaré) map has a transverse,
non-degenerate fixed point, which persists and varies smoothly inpϕp_{\phi}.
What the hypothesis adds beyond the IFT is global and quantitative, and it
is exactly what the computations establish
(AppendixE). For FR1:λ\lambdadecreases from24.5724.57to11, withp∗=1.799p_{*}=1.799; the unit eigenvalue of the monodromy
matrix has multiplicity four with geometric multiplicity two, verified by
spectral projector, and (iii) is verified directly (Δ​ϕ\Delta\phistrictly
decreasing from2​π2\piat the center,d​T/d​E=−3.16dT/dE=-3.16atpϕ=0.5p_{\phi}=0.5). For
OTS:λ\lambdaincreases from1.1311.131to1.2691.269, and the family terminates
atp∗=2.150p_{*}=2.150on the azimuthal relative equilibrium at the centrifugal
barrier (r=9.600r=9.600); the endpoint multiplier is predicted by the
equilibrium’s linearized rates,eμr​2​π/ωθ=1.269e^{\mu_{r}\,2\pi/\omega_{\theta}}=1.269, and
matched by the family. For TTS:λ\lambdaincreases from its inner-edge limit220.46=14.848\sqrt{220.46}=14.848to15.9015.90, and the family terminates atp∗=1.317p_{*}=1.317on the saddle-center equilibrium that the centrifugal term
creates in the mouth of the well (r=2.446r=2.446,θ=29.4∘\theta=29.4^{\circ}; the bare
potential has no critical point there), again with the endpoint multipliereμr​2​π/ωθ=15.90e^{\mu_{r}\,2\pi/\omega_{\theta}}=15.90matched by the family. We therefore
treat (H) as established for the model and prove the rest from it.

## Proposition 1(The two-component manifold).

Under(H), fix0<ε<p∗0<\varepsilon<p_{*}andδ>0\delta>0withε≤p∗−δ\varepsilon\leq p_{*}-\delta. The setℳ0[ε,δ]=⋃ε≤|pϕ|≤p∗−δ⋃ϕ∈S1{γpϕ​rotated by​ϕ}\mathcal{M}_{0}^{[\varepsilon,\delta]}=\bigcup_{\varepsilon\leq|p_{\phi}|\leq p_{*}-\delta}\ \bigcup_{\phi\in S^{1}}\ \big\{\gamma_{p_{\phi}}\ \text{rotated by }\phi\big\}

is the disjoint union of two compact,C∞C^{\infty}, flow-invariant
three-dimensional submanifolds-with-boundary ofΣE\Sigma_{E}— one for each
sign ofpϕp_{\phi}— each with two boundary tori at|pϕ|=ε|p_{\phi}|=\varepsilonand|pϕ|=p∗−δ|p_{\phi}|=p_{*}-\delta, hence four boundary tori in total.

## Proof.

For|pϕ|≥ε>0|p_{\phi}|\geq\varepsilon>0the effective centrifugal potentialU​(r,θ;pϕ)U(r,\theta;p_{\phi})in (5) diverges asθ→0,π\theta\to 0,\pi, soγpϕ\gamma_{p_{\phi}}has turning angles bounded away from the poles and lies in
the open off-axis region{0<θ<π}\{0<\theta<\pi\}, where the azimuthalS​O​(2)SO(2)actionϕ↦ϕ+α\phi\mapsto\phi+\alphais free. Parametriseℳ0[ε,δ]\mathcal{M}_{0}^{[\varepsilon,\delta]}by(s,ϕ,pϕ)(s,\phi,p_{\phi}),s∈ℝ/T​(pϕ)​ℤs\in\mathbb{R}/T(p_{\phi})\mathbb{Z}the phase alongγpϕ\gamma_{p_{\phi}}. By
(H) the map(s,ϕ,pϕ)↦(s,\phi,p_{\phi})\mapstophase point isC∞C^{\infty}; it is an
immersion (∂s\partial_{s}is the reduced flow,∂ϕ\partial_{\phi}the rotation,∂pϕ\partial_{p_{\phi}}the transverse family direction, andpϕp_{\phi}is a
submersion onto the momentum interval) and injective (distinct|pϕ||p_{\phi}|lie on distinct values of the conserved momentum; at fixedpϕp_{\phi}distinct(s,ϕ)(s,\phi)give distinct points since the action is free andγpϕ\gamma_{p_{\phi}}is a simple closed curve), hence an embedding of the
compact manifold-with-boundary[ε,p∗−δ]×S1×S1[\varepsilon,p_{*}-\delta]\times S^{1}\times S^{1}forpϕ>0p_{\phi}>0, and independently of its−pϕ-p_{\phi}copy forpϕ<0p_{\phi}<0; the two embeddings have disjoint images sincepϕp_{\phi}separates them. Invariance:γpϕ\gamma_{p_{\phi}}is invariant under the
reduced flow, the rotation is a symmetry ofH0H_{0}, andpϕp_{\phi}is
conserved, so the full flow carries each lifted torus to itself; the union
is invariant. The boundary is the union of four tori, two per
sign-component.
∎

## Proposition 2(Floquet spectrum and normal hyperbolicity).

Under(H), for eachpϕ∈(0,p∗)p_{\phi}\in(0,p_{*})the
relative-periodic-orbit monodromy matrixMRPO=R​(−Δ​ϕ)​D​ΦTM_{\mathrm{RPO}}=R(-\Delta\phi)\,D\Phi_{T}has spectrum{λ,λ−1,1,1,1,1}\{\lambda,\lambda^{-1},1,1,1,1\}, the eigenvalue11having algebraic
multiplicity four and geometric multiplicity two (two2×22\times 2Jordan
blocks: flow–energy and symmetry–momentum). WithinΣE\Sigma_{E}the
manifoldℳ0[ε,δ]\mathcal{M}_{0}^{[\varepsilon,\delta]}has tangent bundle spanned
by the flow, the azimuthal rotation, and the family direction, all with
zero Lyapunov exponent, and normal bundle the pair{λ,λ−1}\{\lambda,\lambda^{-1}\}— the normal pair of the reduced orbit —
with rateν​(pϕ)=ln⁡λ​(pϕ)/T​(pϕ)\nu(p_{\phi})=\ln\lambda(p_{\phi})/T(p_{\phi})bounded away from
zero. Consequentlyℳ0[ε,δ]\mathcal{M}_{0}^{[\varepsilon,\delta]}isrr-normally
hyperbolic for everyr≥1r\geq 1.

## Proof.

Four eigenvalue-11directions are forced by structure. (i) The flow
directionXH0X_{H_{0}}is a fixed vector of the time-TTmap, hence a+1+1eigenvector. (ii) The period varies with energy,d​T/d​E≠0dT/dE\neq 0by
(H)(iii), so the energy-gradient direction is a generalised+1+1eigenvector partnering the flow in a2×22\times 2Jordan block (the
standard trivial pair). (iii) The infinitesimal azimuthal rotationξϕ=∂ϕ\xi_{\phi}=\partial_{\phi}generates theS​O​(2)SO(2)symmetry, which commutes
with the flow and mapsγpϕ\gamma_{p_{\phi}}to its own rotation; henceξϕ\xi_{\phi}is a+1+1eigenvector. (iv) The family direction∂pϕ\partial_{p_{\phi}}is mapped by the linearized return to itself plus a
multiple ofξϕ\xi_{\phi}, becaused​Δ​ϕ/d​pϕ≠0d\Delta\phi/dp_{\phi}\neq 0by
(H)(iii); this is a generalised+1+1eigenvector partneringξϕ\xi_{\phi}in a second2×22\times 2Jordan block (the symmetry–momentum
pair). These four directions span the generalised eigenspace at11. By
(H)(ii) the reduced normal pair contributes the only
multipliers off the unit circle, so the algebraic multiplicity of11is
exactly four and the geometric multiplicity two. OnΣE\Sigma_{E}the energy
direction is quotiented, leaving the flow, rotation, and family as the
three tangent directions ofℳ0\mathcal{M}_{0}— all neutral, tangential
exponent0— and the normal pair as the two-dimensional normal bundle,
withν​(pϕ)∈[νmin,νmax]⊂(0,∞)\nu(p_{\phi})\in[\nu_{\min},\nu_{\max}]\subset(0,\infty)on the closed
sub-annulus. Normal hyperbolicity of orderrrrequires the normal rate to
exceedrrtimes the tangential rate; the two Jordan blocks contribute only
polynomial (sub-exponential) drift alongℳ0\mathcal{M}_{0}, so the tangential
Lyapunov rate is exactly0and the inequality holds for everyr≥1r\geq 1.
∎

## Proposition 3(Dividing-surface topology).

Under(H), for eachpϕ∈(0,p∗)p_{\phi}\in(0,p_{*})the dividing surface
anchored on thepϕp_{\phi}-slice ofℳ0\mathcal{M}_{0}is homeomorphic toS2×S1S^{2}\times S^{1}, and the slice of the NHIM (a two-torus) separates it into
two components, each homeomorphic to the solid torusD2×S1D^{2}\times S^{1}. The
same holds for the OTS and TTS families. The circulating (toroidal)
dividing surface of[13]does not occur for
any member of the three families.

## Proof.

Written with(q1,q2)=(r,θ)(q_{1},q_{2})=(r,\theta), the reduced Hamiltonian
(5) is of the two-degree-of-freedom form treated in[13], the centrifugal terms folding into the effective
potentialU​(r,θ;pϕ)U(r,\theta;p_{\phi}). By (H)(i) the reduced orbitγpϕ\gamma_{p_{\phi}}is a brake orbit: at its two turning points both reduced
momenta vanish, which is precisely the degeneration of the momentum ellipse
that defines the librating (type-1) case; by (H)(ii) it is
hyperbolic. The construction of[13]then gives a reduced
dividing surfaceDred≅S2D_{\mathrm{red}}\cong S^{2}on whichγpϕ\gamma_{p_{\phi}}is
a separating equator through the two degenerate points. Restoring the
azimuth: at fixed(E,pϕ)(E,p_{\phi})the full slice fibers overDredD_{\mathrm{red}}with fiber the azimuthal circleS1S^{1}. Becauseγpϕ\gamma_{p_{\phi}}andDredD_{\mathrm{red}}lie in the off-axis region, the angleϕ\phiis a global
coordinate on the fiber, so the bundle is trivial and the slice isDred×S1≅S2×S1D_{\mathrm{red}}\times S^{1}\cong S^{2}\times S^{1}, with NHIM slice(equator)×S1≅T2(\text{equator})\times S^{1}\cong T^{2}. SinceS2S^{2}minus an equator is two
open disks,(S2×S1)∖T2=(D2×S1)⊔(D2×S1)(S^{2}\times S^{1})\setminus T^{2}=(D^{2}\times S^{1})\sqcup(D^{2}\times S^{1}). For
OTS and TTS the generating orbit is likewise a brake orbit by
(H)(i) — the OTS-type members librating across the equator,
the TTS-type members on one side of it — soDred≅S2D_{\mathrm{red}}\cong S^{2}and the conclusion is identical. The toroidal case of[13]requires a circulating generating orbit; forpϕ≠0p_{\phi}\neq 0no coordinate of
the reduced system is periodic (the centrifugal barrier walls off both
poles andrris not an angle), so no member of any family circulates and
that case does not arise — the circulating type is realized in this model
only by the planar FR1 and OTS-PO at the excluded center
(Section6.4). The full four-dimensional dividing surface inΣE\Sigma_{E}is the union of these three-dimensional leaves overpϕ∈(0,p∗)p_{\phi}\in(0,p_{*})together with the corresponding−pϕ-p_{\phi}union; the fibration overpϕp_{\phi}and the leaf-by-leaf description are exact only atb=0b=0, wherepϕp_{\phi}is conserved. For sufficiently smallb>0b>0, the dividing surfaces carried by each
compact interior subannulus deform smoothly with the corresponding locally
persisted NHIM branch (Proposition6); no global
continuation through the singularpϕ=0p_{\phi}=0limit is asserted, andpϕp_{\phi}survives only as a local label on each branch, not as an invariant that
foliates the surface.
∎

## Proposition 4(Separatrix structure at the center).

Under(H), letrtr_{t}denote the radius of polar approach of
the family andℰ0=E−VCH​(rt)>0\mathcal{E}^{0}=E-V_{\mathrm{CH}}(r_{t})>0the kinetic energy
there. Aspϕ→0+p_{\phi}\to 0^{+}:
- (a)

the polar turning angle satisfiesθ−​(pϕ)=k​pϕ+O​(pϕ2)\theta_{-}(p_{\phi})=k\,p_{\phi}+O(p_{\phi}^{2})withk=[Ix−1+m−1​rt−22​ℰ0]1/2;k=\Big[\tfrac{\,I_{x}^{-1}+m^{-1}r_{t}^{-2}\,}{2\,\mathcal{E}^{0}}\Big]^{1/2};

henceρmin​(pϕ)=rt​sin⁡θ−=rt​k​pϕ+O​(pϕ2)\rho_{\min}(p_{\phi})=r_{t}\sin\theta_{-}=r_{t}k\,p_{\phi}+O(p_{\phi}^{2})is
linear inpϕp_{\phi}, and the family meets the symmetry axis in a double cone
with a genuine conical (non-manifold) singularity at the apex;
- (b)

the turning states converge to the phase points(rt,θ=0​or​π,p=0)(r_{t},\theta=0\ \text{or}\ \pi,\,p=0), which do not lie on the planar
orbitγ0\gamma_{0}(which crosses the axis with|pθ|=pmax=ℰ0/κ​(rt)|p_{\theta}|=p_{\max}=\sqrt{\mathcal{E}^{0}/\kappa(r_{t})},κ=12​Ix+12​m​r2\kappa=\tfrac{1}{2I_{x}}+\tfrac{1}{2mr^{2}}),
while away from the axis the members converge to the folded planar curve.
The Hausdorff limit of the family is therefore the folded planar orbit
together with the two momentum segments{(rt,θ=0orπ,0,pθ,0):|pθ|≤pmax}\{(r_{t},\theta{=}0\ \text{or}\ \pi,\,0,\,p_{\theta},\,0):|p_{\theta}|\leq p_{\max}\}— a singular set strictly containingγ0\gamma_{0}. The family
consequently has nopϕ=0p_{\phi}=0fiber: the torus fibration degenerates at
the center, andγ0\gamma_{0}is the separatrix carrier in the sense of
Section6.6— the zero level set of the conserved momentum,
dividing the two precession senses — its own motion differing in kind
from every member. For FR1 and OTS the members’ periods and multipliers
converge to the planar values; for TTS the planar orbit closes only after
two circuits of the limiting reduced arc, soT​(pϕ)→Tplanar/2T(p_{\phi})\to T_{\mathrm{planar}}/2andλ​(pϕ)→λplanar\lambda(p_{\phi})\to\sqrt{\lambda_{\mathrm{planar}}}.

## Proof.

At a polar turning point both reduced momenta vanish
((H)(i)), so the energy relation (5) readsE=U​(rt,θ−;pϕ)+V​(rt,θ−)E=U(r_{t},\theta_{-};p_{\phi})+V(r_{t},\theta_{-}). Asθ→0\theta\to 0,U​(r,θ;pϕ)=pϕ22​θ2​(Ix−1+m−1​r−2)+O​(pϕ2)U(r,\theta;p_{\phi})=\tfrac{p_{\phi}^{2}}{2\theta^{2}}\big(I_{x}^{-1}+m^{-1}r^{-2}\big)+O(p_{\phi}^{2})andV​(rt,θ)=VCH​(rt)+O​(θ2)V(r_{t},\theta)=V_{\mathrm{CH}}(r_{t})+O(\theta^{2}).
Substituting and keeping leading order,pϕ22​θ−2​(Ix−1+m−1​rt−2)=ℰ0+O​(θ−2),\frac{p_{\phi}^{2}}{2\theta_{-}^{2}}\big(I_{x}^{-1}+m^{-1}r_{t}^{-2}\big)=\mathcal{E}^{0}+O(\theta_{-}^{2}),

which givesθ−=k​pϕ+O​(pϕ2)\theta_{-}=k\,p_{\phi}+O(p_{\phi}^{2})withkkas stated. The set
traced near the apex,{X2+Y2=(rt​k)2​pϕ2}\{X^{2}+Y^{2}=(r_{t}k)^{2}p_{\phi}^{2}\}, is a double cone,
which is not a smooth manifold at the apex (its tangent cone is the cone
itself, not a plane). For (b): the turning states have both reduced
momenta zero andpϕ→0p_{\phi}\to 0, so they converge to(rt,θ=0,0,0,0)(r_{t},\theta{=}0,\,0,0,0); onγ0\gamma_{0}the axis crossing carries|pθ|=pmax≠0|p_{\theta}|=p_{\max}\neq 0, so this limit point is not onγ0\gamma_{0}.
Inside the polar layer the momenta sweep the full segment: at the point ofγpϕ\gamma_{p_{\phi}}withθc=θ−/1−c2\theta_{c}=\theta_{-}/\sqrt{1-c^{2}},c∈(0,1)c\in(0,1), the
energy relation with the same expansion givespθ2​κ​(rt)=ℰ0​(1−θ−2/θc2)+o​(1)=ℰ0​c2+o​(1)p_{\theta}^{2}\,\kappa(r_{t})=\mathcal{E}^{0}\big(1-\theta_{-}^{2}/\theta_{c}^{2}\big)+o(1)=\mathcal{E}^{0}c^{2}+o(1), sopθ→c​pmaxp_{\theta}\to c\,p_{\max}, whiler→rtr\to r_{t}andpr→0p_{r}\to 0(the radial variation across the layer isO​(θ2)O(\theta^{2})); every point of the segment is thus a limit of family
points. Away from any fixed neighborhood of the poles the reduced vector
field depends smoothly onpϕp_{\phi}down to0, so the members converge
there to the folded planar curve. Together these give the stated Hausdorff
limit, which containsγ0\gamma_{0}and strictly more; since the limit is not
a torus — not even a manifold — the fibration has no fiber overpϕ=0p_{\phi}=0. The covering statement is forced by the pole count: the planar
FR1 and OTS-PO cross both poles per period, so one circuit of the folded
curve closes them; the planar TTS-PO crosses one pole per half-swing,
exchanging meridional half-planes at each crossing, so two circuits are
required, halving the limiting period and taking the square root of the
multiplier.
∎

The constants are quantitatively confirmed for all three
families (AppendixE): measuredθ−/pϕ\theta_{-}/p_{\phi}against the formula forkkgives0.46190.4619(FR1:rt=3.6507r_{t}=3.6507,ℰ0=1.1736\mathcal{E}^{0}=1.1736),0.6510.651(OTS:rt=13.37r_{t}=13.37,ℰ0=0.5035\mathcal{E}^{0}=0.5035), and0.3040.304(TTS:rt=2.6444r_{t}=2.6444,ℰ0=3.105\mathcal{E}^{0}=3.105); for FR1,ρmin/|pϕ|=1.686\rho_{\min}/|p_{\phi}|=1.686againstrt​k=1.6863r_{t}k=1.6863; and the TTS covering relation fixes the inner-edge limits exactly,T​(0+)=Tplanar/2=1.1139T(0^{+})=T_{\mathrm{planar}}/2=1.1139andλ​(0+)=220.46=14.848\lambda(0^{+})=\sqrt{220.46}=14.848;
the smallest-momentum member computed (pϕ=0.05p_{\phi}=0.05) hasT=1.1140T=1.1140andλ=14.84\lambda=14.84, approaching both limits to three digits.

## Proposition 5(The blow-up separates the directions of approach).

Letβ:N~→N\beta:\widetilde{N}\to Nbe the oriented (spherical) blow-up of the
apex in the three transverse directions(X,Y,pϕ)(X,Y,p_{\phi}). The proper
transform of the cone of Proposition4is two disjoint smooth
circles on the exceptional divisorS2S^{2}— the latitude circlesp^=±c/1+c2\hat{p}=\pm c/\sqrt{1+c^{2}},c=rt​kc=r_{t}k, one per precession sense — while
every planar orbit lies in{pϕ=0}\{p_{\phi}=0\}and lifts to the equatorp^=0\hat{p}=0: the orbitγ0\gamma_{0}meets the divisor in two antipodal
equatorial points (its approach and departure directions), and its rotated
copies fill the equator. The family and the planar orbits therefore reach
the apex along separated directions.

## Proof.

In blow-up coordinates(X,Y,pϕ)=ρ​(X^,Y^,p^)(X,Y,p_{\phi})=\rho\,(\hat{X},\hat{Y},\hat{p})with(X^,Y^,p^)∈S2(\hat{X},\hat{Y},\hat{p})\in S^{2}andρ≥0\rho\geq 0, the coneX2+Y2=c2​pϕ2X^{2}+Y^{2}=c^{2}p_{\phi}^{2}becomesX^2+Y^2=c2​p^2\hat{X}^{2}+\hat{Y}^{2}=c^{2}\hat{p}^{2}, i.e.p^=±c/1+c2\hat{p}=\pm c/\sqrt{1+c^{2}}: two latitude circles, symmetric about the
equator, disjoint from it and from each other forc>0c>0, and smooth. They
are the proper transforms of the two nappes (the±pϕ\pm p_{\phi}components). The
orbitγ0\gamma_{0}approaches the apex within{pϕ=0}\{p_{\phi}=0\}, crossing the
axis along a meridional direction with(X,Y)→0(X,Y)\to 0; its lift hasp^=0\hat{p}=0and meets the equator at the two antipodal points given by the
azimuths of approach and departure, and theS​O​(2)SO(2)-rotated copies ofγ0\gamma_{0}sweep the whole equator. Since the latitude circles sit atp^≠0\hat{p}\neq 0, the two sets are disjoint.
∎

## Proposition 6(Persistence).

For eachr≥1r\geq 1there isb0​(r)>0b_{0}(r)>0such that for|b|<b0​(r)|b|<b_{0}(r)each of the
two components of each closed sub-annulusℳ0[ε,δ]\mathcal{M}_{0}^{[\varepsilon,\delta]}persists as aCrC^{r}normally
hyperboliclocallyinvariant manifold-with-boundaryℳb[ε,δ]\mathcal{M}_{b}^{[\varepsilon,\delta]}, together with itsCrC^{r}local
stable and unstable manifolds, on which the four-dimensional dividing
surfaces of Proposition3deform smoothly. The orbit FR1
persists independently, as an exact periodic orbit in the reaction plane,
and is not contained inℳb[ε,δ]\mathcal{M}_{b}^{[\varepsilon,\delta]}.

## Proof.

By Proposition2,ℳ0[ε,δ]\mathcal{M}_{0}^{[\varepsilon,\delta]}is
compact andrr-normally hyperbolic for everyrr, the tangential rate
being0. Atb=0b=0the boundary tori are invariant (pϕp_{\phi}is
conserved), so the manifold is neither overflowing nor inflowing; this is
handled in the standard way by modifying the vector field in a collar of
the boundary so that the manifold becomes overflowing invariant
(respectively inflowing, for the stable version), the modification being
supported away from the interior. The persistence theorem for overflowing
invariant manifolds[21,22,23]then
yields, for perturbations that areCrC^{r}-small, a nearbyCrC^{r}manifold
with the same dimension and normal splitting, carrying its local stable and
unstable manifolds; undoing the collar modification, the persisted object
is locally invariant for the original flow — trajectories may leave only
through its boundary. The perturbationHb−H0=b​V0​(r)​sin3⁡θ​cos⁡3​ϕH_{b}-H_{0}=bV_{0}(r)\sin^{3}\theta\cos 3\phiisC∞C^{\infty}andO​(b)O(b)in everyCrC^{r}norm on the compact
sub-annulus, so the smallness requirement fixesb0​(r)>0b_{0}(r)>0; the required
smallness grows withrr, whence the dependence ofb0b_{0}onrr. The planeY=0Y=0is invariant for allbb(Section2), so FR1 persists
there as an exact periodic orbit. Finally,ℳb[ε,δ]\mathcal{M}_{b}^{[\varepsilon,\delta]}lies in anO​(b)O(b)neighborhood ofℳ0[ε,δ]\mathcal{M}_{0}^{[\varepsilon,\delta]}, which is bounded away from the
planepϕ=0p_{\phi}=0containing FR1 by the distance corresponding to|pϕ|≥ε|p_{\phi}|\geq\varepsilon; for|b||b|small the neighborhood does not reach
that plane, so FR1 is not contained in either component.
∎

## 7Trajectory classification and the out-of-plane channel

This section carries out the transport computation that Section3.2sets up: sampling the entrance dividing surface, classifying trajectories against the three surfaces, and recording class fractions and gap-time statistics. Two protocols are fixed at the outset. The coupling takes the two valuesb=0b=0andb=0.3b=0.3, and the organizing contrast is between them: atb=0b=0the momentumpϕp_{\phi}is conserved and the dynamics decomposes into a one-parameter family of two-degree-of-freedom subsystems; atb=0.3b=0.3it does not. The energy isE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}, as everywhere in this paper; the class fractions alone are in addition recomputed at five higher energies, up toE=2.0​kcal​mol−1E=2.0\ \mathrm{kcal\,mol^{-1}}, for one purpose — to find where the effect of the coupling dies away. Reactive fluxes are not computed in this paper; an entropy-based flux analysis for two-degree-of-freedom Chesnavich-type models is given in[24].

## 7.1The classification protocol

Initial conditions are sampled on the inward-crossing half (pr<0p_{r}<0) of the entrance section, the sphererOTS=13.386​År_{\mathrm{OTS}}=13.386\ \text{\text{\AA }}— the radial realization of the OTS dividing surface. This radius is that of the planar orbiting transition state, and it is the radius at which Mauguière, Collins, Ezra, Farantos, and Wiggins place the entrance dividing surface of the planar problem[12]; the value carries over, while the surface at this radius is here four-dimensional rather than two-dimensional. Each trajectory is integrated until one of two things happens. Eitherrrfalls belowrreact=2.0​År_{\mathrm{react}}=2.0\ \text{\text{\AA }}— inside the ridge crestrc=2.2​År_{c}=2.2\ \text{\text{\AA }}and below the radial range of the TTS orbit (Section6.4) — and the trajectory is reactive: it is captured into the well. Or the trajectory returns outward through the entrance surface and dissociates: it is non-reactive. Along the way, its crossings of the classifier (FR1) surface are counted. On a fixed-pϕp_{\phi}leaf the reduced FR1 orbit librates, its dividing surface is a two-sphere whose equator is the orbit (Section6.4), and a crossing of that surface is a passage through the radial bottleneck of the roaming shelf. The count is therefore taken as the number of crossings of the radiusrFR1=3.40​År_{\mathrm{FR1}}=3.40\ \text{\text{\AA }}; Section7.6shows that the principal redistribution is robust over the tested range of placements of this radius.

Five classes result. A reactive trajectory ends inside the classifier, so it crosses an odd number of times: once (direct reactive) or three or more times (roaming reactive). A non-reactive trajectory ends outside, so it crosses an even number of times: twice (direct non-reactive), four or more times (roaming non-reactive), or not at all, turning around before ever reaching the classifier. Mauguière, Collins, Ezra, Farantos, and Wiggins note this last case as possible but do not observe it in the planar model[12]. It does occur here: no such trajectory appears atE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}, but they reach22–3%3\%of the ensemble atE=2.0​kcal​mol−1E=2.0\ \mathrm{kcal\,mol^{-1}}, and we count them as their own class rather than folding them into the roaming count. No trajectory in any ensemble remained unclassified at the integration limit.

The sample is uniform in the four canonical surface coordinates(θ,ϕ,pθ,pϕ)(\theta,\phi,p_{\theta},p_{\phi})over the energetically allowed region, withpr<0p_{r}<0fixed byH=EH=E. AppendixDverifies that this uniform sample weights each initial condition by the rate at which trajectories cross the surface there — the correct ensemble for an incoming stream. Becausepϕp_{\phi}is one of the sampled coordinates, every value ofpϕp_{\phi}enters the ensemble in its natural proportion, and no separate average overpϕp_{\phi}is required. Atb=0b=0the sample decomposes over the conserved-pϕp_{\phi}leaves; atb=0.3b=0.3it does not.

## 7.2The classification plane and thepϕp_{\phi}stack

Figure8shows the trajectory class over the(θ,pθ)(\theta,p_{\theta})plane of entrance initial conditions, atE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}, for four settings of(b,pϕ)(b,p_{\phi}). Panel (a), the in-plane leafb=0,pϕ=0b=0,\ p_{\phi}=0, reproduces the planar classification: diagonal bands of direct-reactive trajectories cut by strips of roaming and of direct non-reactive trajectories,88.1%88.1\%direct and11.9%11.9\%roaming on the computed grid. Panel (b), stillb=0b=0but on the leafpϕ=0.8p_{\phi}=0.8, shows that the leaves are far from interchangeable. The roaming fraction roughly doubles, to24.3%24.3\%; the band geometry changes from diagonal stripes to concentric shells; and the polar region becomes energetically forbidden, excluded by the centrifugal part of the effective potentialU​(r,θ;pϕ)U(r,\theta;p_{\phi})in Eq. (5). The cylindrically symmetric three-degree-of-freedom problem is therefore a one-parameter family of two-degree-of-freedom subsystems that differ substantially from one another, and the microcanonical fractions are thepϕp_{\phi}average over this family, not any single member.

Panels (c) and (d) isolate the effect of the coupling. Panel (c),b=0.3b=0.3on the in-plane leafpϕ=0p_{\phi}=0, is nearly identical to panel (a): a launch withpϕ=0p_{\phi}=0andϕ=0\phi=0lies in the reaction plane{Y=0,pY=0}\{Y=0,\,p_{Y}=0\}, which is invariant for everybb(Section3.2), so such trajectories never sample the out-of-plane direction. Sampling restricted to the reaction plane, as in the planar studies, would therefore miss the three-degree-of-freedom effect entirely. Panel (d),b=0.3b=0.3on the off-plane leafpϕ=0.8p_{\phi}=0.8, is where the coupling acts. Relative to panel (b), the roaming non-reactive class grows by53%53\%, the roaming reactive and direct non-reactive classes shrink (by25%25\%and10%10\%), and the direct reactive class rises slightly (+5%+5\%): the coupling redistributes the population toward roaming escape without closing the direct reactive channel.Figure 8:Trajectory classification on the entrance dividing surface over the(θ,pθ)(\theta,p_{\theta})plane of incoming initial conditions (ϕ=0\phi=0),E=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}; white is energetically forbidden. (a)b=0,pϕ=0b=0,\ p_{\phi}=0: the planar leaf,88.1%88.1\%direct,11.9%11.9\%roaming. (b)b=0,pϕ=0.8b=0,\ p_{\phi}=0.8: roaming24.3%24.3\%, the polar regions excluded by the centrifugal part ofUUin Eq. (5). (c)b=0.3,pϕ=0b=0.3,\ p_{\phi}=0: in-plane, hence insensitive to the coupling — nearly identical to (a) because the launch lies in the reaction plane{Y=0,pY=0}\{Y=0,\,p_{Y}=0\}. (d)b=0.3,pϕ=0.8b=0.3,\ p_{\phi}=0.8: the roaming non-reactive class (pink) grows by53%53\%at the expense of the roaming reactive and direct non-reactive classes. Classes: direct reactive (red), roaming reactive (green), direct non-reactive (blue), roaming non-reactive (pink).

## 7.3Microcanonical fractions versus energy

Figure9shows the microcanonical fraction of each class against energy, forb=0b=0andb=0.3b=0.3, with sample sizes of1500015000per coupling value atE=0.5E=0.5,50005000atE=0.7E=0.7, and12001200at each higher energy. Three findings. First, thepϕp_{\phi}-averaged ensemble is far less reactive than the planar slice: atE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}the direct-reactive fraction of the incoming ensemble is0.360.36, against0.610.61on the planar leaf, and atb=0b=0the direct non-reactive fraction rises from0.410.41atE=0.5E=0.5to0.660.66atE=2.0​kcal​mol−1E=2.0\ \mathrm{kcal\,mol^{-1}}while the roaming reactive fraction collapses from0.0920.092to0.0010.001. The planar problem is not representative of the three-degree-of-freedom microcanonical ensemble. Second, the effect of the coupling is concentrated at the low end of the window. AtE=0.5E=0.5, switching onb=0.3b=0.3lowers the direct non-reactive fraction from0.4140.414to0.3820.382, a decrease of0.032±0.0060.032\pm 0.006; the roaming non-reactive fraction rises by0.030±0.0040.030\pm 0.004and the roaming reactive by0.011±0.0030.011\pm 0.003, while the direct-reactive fraction falls by0.008±0.0060.008\pm 0.006, within its sampling error. AtE=0.7E=0.7the total roaming gain is0.024±0.0080.024\pm 0.008; fromE=1.0​kcal​mol−1E=1.0\ \mathrm{kcal\,mol^{-1}}the two couplings agree within the sampling uncertainty. The reason is kinematic: faster trajectories cross the roaming region in fewer periods of the roaming motion than the transverse instability needs to act. Third, the direct-reactive fraction is unchanged by the coupling within error at every energy (|Δ|=0.008±0.006|\Delta|=0.008\pm 0.006atE=0.5E=0.5), consistent with, though not determined by, thebb-insensitivity of the FR1 action (Section4). The zero-crossing non-reactive class is absent atE=0.5E=0.5and grows slowly with energy, reaching0.0240.024(b=0b=0) and0.0290.029(b=0.3b=0.3) atE=2.0E=2.0; folding it into the roaming non-reactive count, as a pure parity rule would, would overstate the high-energy roaming fraction by up to a third.Figure 9:Left: microcanonical class fractions versus energy forb=0b=0(filled symbols, solid lines) andb=0.3b=0.3(open symbols, dashed lines); error bars are binomial; the gray dotted curve is the zero-crossing non-reactive class. Sample sizes:1500015000per coupling value atE=0.5E=0.5,50005000atE=0.7E=0.7,12001200otherwise. Right: the difference between theb=0.3b=0.3and theb=0b=0fraction of each class. The coupling transfers0.040±0.0050.040\pm 0.005of the ensemble into the two roaming classes atE=0.5E=0.5,0.024±0.0080.024\pm 0.008atE=0.7E=0.7, and nothing beyond the sampling uncertainty fromE=1.0​kcal​mol−1E=1.0\ \mathrm{kcal\,mol^{-1}}. Same color code as Figure8.

## 7.4Gap-time statistics

The gap time of a non-reactive trajectory is the time between its entry through the entrance dividing surface and its exit back through it[12]. We measure it at the surface defined in Section7.1— the same placement as the planar study. The reactive analog, the time from entry to capture, is a different quantity and is reported in AppendixD. Mauguière, Collins, Ezra, Farantos, and Wiggins showed for the planar model that the gap-time distribution of the roaming region is not exponential: escape is not a memoryless, single-rate process[12]. The same conclusion, using the diagnostics applied below, is reached in[24]. We take this as established, and ask how the coupling changes the distribution.

Figure10first shows the gap time along a one-parameter scan of the entrance momentumpθp_{\theta}at fixedθ\thetaon the in-plane leaf. The direct bands sit at short, regular times, and the roaming trajectories cluster at the band edges with times that increase sharply toward the band boundaries — the band structure of the planar roaming region[12], recovered inside the three-degree-of-freedom model.

One geometric fact must be stated before distributions are compared. No gap can be shorter than the direct flight: a trajectory entering atrOTS=13.386​År_{\mathrm{OTS}}=13.386\ \text{\text{\AA }}must travel inward to the interaction region and back out, and the purely radial flight to the shelf bottleneck and back takes18.118.1time units. The shortest gap in the ensemble is19.119.1. The distribution therefore begins abruptly near this value, and that onset is a property of the geometry, not of the escape dynamics. For reference, the figures show an exponential distribution with the same mean, shifted to begin at the observed minimum; an unshifted exponential would put weight at gap times shorter than the flight itself. Because the coupling term is negligible beyond8​Å8\ \text{\text{\AA }}(V0<10−19V_{0}<10^{-19}there), the inward and outward flights are identical forb=0b=0andb=0.3b=0.3, and any difference between the two distributions arises in the interaction region.

Figure11shows the density and the survival function of the non-reactive gap time atE=0.5E=0.5andE=1.0​kcal​mol−1E=1.0\ \mathrm{kcal\,mol^{-1}}, for both couplings. Neither distribution is exponential. A convenient summary is the coefficient of variation — the standard deviation divided by the mean, equal to11for an exponential distribution and used for this purpose in[24]— computed on the gaps in excess of the minimum: atE=0.5E=0.5it is1.561.56atb=0b=0and1.221.22atb=0.3b=0.3, both above11. The effect of the coupling is two-sided. Through the bulk of the distribution the gaps lengthen: the median rises from30.230.2to31.431.4, the mean from40.840.8to41.341.3, the 90th percentile from6969to7373, and the fraction of trajectories with gap beyond8080rises from7.3%7.3\%to8.0%8.0\%. These are the trajectories that wander out of the reaction plane before escaping — the same population that swells the roaming non-reactive class. Conditioned on the roaming non-reactive class itself, the median gap is nearly unchanged (51.451.4to53.653.6) and the mean falls (69.569.5to63.563.5), so the shift of the pooled distribution reflects the larger roaming population rather than longer individual roaming gaps. In the extreme tail the ordering reverses: the 99th percentile falls from193193to153153, with non-overlapping bootstrap95%95\%confidence intervals[181,209][181,209]and[146,162][146,162]. The rare, very long trappings of the symmetric limit are supported by conserved-pϕp_{\phi}structure that the coupling destroys. The coupling therefore shifts the pooled distribution toward longer typical gaps by enlarging the roaming population, leaves the typical roaming gap itself nearly unchanged, and cuts off the longest trappings; the region remains non-statistical at both couplings. AtE=1.0E=1.0the two distributions are close (means28.728.7and30.630.6), consistent with the fractions. Measuring the gap between crossings of an inner surface atr=9.5​År=9.5\ \text{\text{\AA }}, which more than halves the deterministic flight, leads to the same conclusions (AppendixD).Figure 10:Gap time versus the launch momentumpθp_{\theta}atθ=π/2\theta=\pi/2on the in-plane leaf (b=0,pϕ=0b=0,\ p_{\phi}=0), on a logarithmic scale: direct bands at short, regular times; roaming trajectories at the band edges with sharply increasing times. The strip beneath records the class. Same color code as Figure8.Figure 11:Non-reactive gap times measured at the entrance dividing surface: density (left) and survival function (right, semi-logarithmic) atE=0.5E=0.5(top) andE=1.0​kcal​mol−1E=1.0\ \mathrm{kcal\,mol^{-1}}(bottom),b=0b=0versusb=0.3b=0.3. The dashed curve is an exponential distribution with the same mean, shifted to begin at the observed minimum gap (dotted vertical line), which is set by the flight time from the entrance surface to the interaction region and back. AtE=0.5E=0.5the coupling shifts the body of the distribution toward longer gaps while shortening the extreme tail.

## 7.5The mechanism: transport ofpϕp_{\phi}between the counter-precessing components

The mechanism behind the redistribution can be measured directly. Figure12follows an ensemble of trajectories launched off the plane, atpϕ=0.8p_{\phi}=0.8, over a scan of the launch momentumpθp_{\theta}; for each trajectory we record the excursion of the azimuthal momentum along it,max⁡pϕ−min⁡pϕ\max p_{\phi}-\min p_{\phi}. Atb=0b=0the excursion is zero for every trajectory:pϕp_{\phi}is conserved, and each trajectory remains on its initial leaf. Atb=0.3b=0.3the median excursion over the ensemble is0.710.71, the largest is9.09.0, and22%22\%of the trajectories crosspϕ=0p_{\phi}=0— they reverse their sense of precession about the symmetry axis, passing between the two components of the manifold family that the symmetric limit keeps disjoint (Section6.2). The trajectories thus show directly the mechanism established for the manifolds in Section6.6: forb>0b>0the conservation ofpϕp_{\phi}fails, the conserved-momentum tori break up, and motion passes between the counter-precessing components.Figure 12:The excursion of the azimuthal momentum,max⁡pϕ−min⁡pϕ\max p_{\phi}-\min p_{\phi}, along each trajectory of an ensemble launched off the plane (θ=π/2\theta=\pi/2,pϕ=0.8p_{\phi}=0.8), versus the launch momentumpθp_{\theta}. Atb=0b=0the excursion is zero for every trajectory. Atb=0.3b=0.3the median excursion is0.710.71and22%22\%of the trajectories crosspϕ=0p_{\phi}=0, reversing their sense of precession about the symmetry axis.

## 7.6Placement of the classification surfaces and robustness

Section6constructs the three dividing surfaces as four-dimensional objects. The classification does not detect crossings of these surfaces directly; it uses fixed radii —13.386​Å13.386\ \text{\text{\AA }}for entry and exit,3.40​Å3.40\ \text{\text{\AA }}for the classifier count,2.0​Å2.0\ \text{\text{\AA }}for capture — and this subsection shows, in three steps, that the fixed radii represent the surfaces correctly and that the principal redistribution is robust over the tested range of surface placements.

The first step is the reduced family, computed atb=0b=0(Figure13). The radial extent of the FR1 orbit varies little across the family: the inner turning radius moves from3.183.18to3.35​Å3.35\ \text{\text{\AA }}and the outer from3.653.65to3.52​Å3.52\ \text{\text{\AA }}over the admissible interval ofpϕp_{\phi}, so the radius3.40​Å3.40\ \text{\text{\AA }}lies inside the orbit’s radial range on every leaf, and a single threshold serves the whole family. This is also why the threshold remains adequate atb=0.3b=0.3, wherepϕp_{\phi}changes along trajectories (Section7.5): for instantaneous|pϕ||p_{\phi}|within the admissibleb=0b=0family the bottleneck remains at essentially the same radius, and trajectories leaving that range account for most of the observed classifier disagreements (Section7.6). The entrance orbit moves inward from13.39​Å13.39\ \text{\text{\AA }}atpϕ=0+p_{\phi}=0^{+}to9.71​Å9.71\ \text{\text{\AA }}atpϕ=2.10p_{\phi}=2.10, approaching the family endpoint (Section6.2), so the launch surface at the planar value13.386​Å13.386\ \text{\text{\AA }}lies at or outside the entrance orbit of every leaf. One caveat is stated rather than assumed away. For smallpϕp_{\phi}, the centrifugal barrier of the effective potentialUUin Eq. (5) lies beyond the launch surface — at25.6​Å25.6\ \text{\text{\AA }}forpϕ=0.8p_{\phi}=0.8, moving inward aspϕp_{\phi}grows and crossing13.386​Å13.386\ \text{\text{\AA }}nearpϕ≈1.5p_{\phi}\approx 1.5— so an outward crossing of the launch surface is not, for those trajectories, a crossing of their outermost barrier. The barrier is, however, very low: its top exceeds the potential at the launch surface by at most0.0015​kcal​mol−10.0015\ \mathrm{kcal\,mol^{-1}}over the admissible interval atE=0.5E=0.5. A trajectory that has crossed the launch surface outward can be turned back only if its outward radial kinetic energy there is below this value, and such trajectories are a negligible part of the ensemble.

The second step is direct measurement. Each trajectory is integrated once, the crossing times of all candidate surfaces are recorded, and the ensemble is reclassified under varied thresholds. AtE=0.5E=0.5, moving the classifier radius across the shelf (3.253.25–3.55​Å3.55\ \text{\text{\AA }}) or the capture radius across the well mouth (1.81.8–2.2​Å2.2\ \text{\text{\AA }}) shifts every class fraction by at most0.0110.011— about a quarter of the0.0400.040effect of the coupling. Repeating the full computation with the launch surface at14​Å14\ \text{\text{\AA }}(50005000samples per coupling value) reproduces every fraction and theE=0.5E=0.5transfer within one standard error. The principal redistribution is robust over the tested range of surface placements.

The third step tests the radial classifier count against the dividing surface it stands in for. Atb=0b=0the leaf of the FR1 dividing surface at angular momentumpϕp_{\phi}is the two-sphere over the reduced orbit (Section6.4); since the reduced orbit has its minimum radius at the equator and its maximum at the polar turning, its configuration arc is a graphr=R​(θ;pϕ)r=R(\theta;p_{\phi}), and a crossing of the surface is a sign change ofr−R​(θ;|pϕ|)r-R(\theta;|p_{\phi}|)withθ\thetainside the arc, the polar caps closing in momentum at the turning points. A passage of the radius3.40​Å3.40\ \text{\text{\AA }}near a pole, outside the arc, is not a crossing of the surface. Each trajectory of a subset of theE=0.5E=0.5ensemble (25002500per coupling value) was classified both ways from one integration: by the radial count and by crossings of the leafwise surface, evaluated at the instantaneous|pϕ||p_{\phi}|; forb=0.3b=0.3the unperturbedb=0b=0surface serves as a frozen-pϕp_{\phi}reference classifier (no finite-bbsurface is computed). The two classifications agree for97.4%97.4\%of trajectories atb=0b=0and94.5%94.5\%atb=0.3b=0.3; the reactive classes agree for99.8%99.8\%. The disagreements concentrate in the trajectories whosepϕp_{\phi}exceeds the family endpointp∗=1.799p_{*}=1.799on the shelf, where theb=0b=0surface is not defined (6565of6666disagreements atb=0b=0,123123of138138atb=0.3b=0.3); the remainder atb=0.3b=0.3are1313direct/roaming parity swaps that nearly cancel. Table2gives the class fractions under both classifications. The reactive fractions are identical to three decimals at both couplings. The one systematic difference is that the surface count assigns a fraction of the ensemble (0.0260.026atb=0b=0,0.0050.005atb=0.3b=0.3) to the zero-crossing non-reactive class — trajectories whose only crossings of the radius3.40​Å3.40\ \text{\text{\AA }}occur near the poles, outside every leaf surface — a class the radial count leaves essentially empty at this energy (Section7.3). The paired comparison is the test of the transfer: on this subset the radial estimate is noisier than the full-ensemble value (+0.020+0.020against+0.040±0.005+0.040\pm 0.005, with a subset standard error of0.0120.012), and the same trajectories give a roaming gain of+0.023+0.023under the surface count — the two classifications agree on the transfer to within0.0030.003at the displayed precision. On this subset the frozen-pϕp_{\phi}reference classifier reproduces the roaming transfer obtained from the radial count within the sampling uncertainty, supporting the radial count as a robust realization of the transition-state geometry.Table 2:Class fractions from the same25002500trajectories per coupling value atE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}, classified against the fixed radii (radial) and against the leafwise dividing surface. Atb=0b=0the surface column uses the actual leafwise dividing surface; atb=0.3b=0.3it uses the unperturbedb=0b=0surface as a frozen-pϕp_{\phi}reference. The roaming gain is the change ofRR+RN\mathrm{RR}+\mathrm{RN}fromb=0b=0tob=0.3b=0.3.radial,b=0b=0surface,b=0b=0radial,b=0.3b=0.3frozen ref.,b=0.3b=0.3direct reactive0.3510.3510.3510.3510.3410.3410.3400.340roaming reactive0.0960.0960.0960.0960.1020.1020.1020.102direct non-reactive0.4010.4010.3830.3830.3910.3910.3920.392roaming non-reactive0.1510.1510.1430.1430.1650.1650.1600.160zero-crossing non-reactive0.0000.0000.0260.0260.0000.0000.0050.005roaming gain+0.020+0.020(radial)+0.023+0.023(surface)Figure 13:Placement of the classification radii against the reduced family, computed atb=0b=0. Left: the radial range and mean radius of the FR1 orbit versuspϕp_{\phi}; the fixed classifier radius3.40​Å3.40\ \text{\text{\AA }}(dotted) lies inside the orbit’s radial range on every leaf. Right: the radius of the entrance orbit versuspϕp_{\phi}, from13.39​Å13.39\ \text{\text{\AA }}at the planar limit to9.71​Å9.71\ \text{\text{\AA }}near the family endpoint; the launch surface at the planar value (dotted) lies at or outside the entrance orbit of every leaf.

## 8Discussion

The analysis yields a coherent picture of how azimuthal corrugation reshapes roaming. The in-plane reactive bottleneck — the FR1 action — is essentially unaffected by the coupling, so the symmetry breaking does not change the rate at which trajectories pass through the roaming region in the reaction plane. What it changes is the transverse organization: breaking the cylindrical symmetry makes the out-of-plane direction hyperbolic, so that resolving the three-fold methyl corrugation opens an out-of-plane escape route to the roaming dynamics rather than confining motion to the plane. The transition is immediate rather than threshold-controlled: the out-of-plane direction is unstable for arbitrarily weak coupling and remains unstable across most of the range studied; after the narrow elliptic restabilization window0.58≲b≲0.630.58\lesssim b\lesssim 0.63, the period-doubling atbc≈0.63b_{c}\approx 0.63marks the onset of negative hyperbolicity. The objects that organize transport in the full space are not the one-dimensional orbits but three three-dimensional NHIMs, one for each transition state. Atb=0b=0, Section6explicitly constructs the three NHIMs as two-component families of invariant tori and proves that every compact interior piece persists for sufficiently small coupling. Each anchors a four-dimensional dividing surface. At fixedpϕp_{\phi}the leaf of that surface is a copy ofS2×S1S^{2}\times S^{1}, and the corresponding torus of the NHIM cuts the leaf into two solid tori; this holds for all three transition states because all three reduced orbits librate. In the analysis of Section6.6, the mechanism of the escape route is the loss of conservation ofpϕp_{\phi}onceb>0b>0: the separatrix structure at the center of each family is destroyed and the conserved-momentum tori break up.

Section7carries out the transport computation based on these surfaces. The orbit and manifold analysis of Sections4–6is carried out at the single energyE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}; the classification of Section7is in addition repeated across the roaming windowE=0.5E=0.5–2.0​kcal​mol−12.0\ \mathrm{kcal\,mol^{-1}}, for one purpose: to locate where the effect of the coupling survives. The findings are as follows. Thepϕp_{\phi}-averaged microcanonical ensemble is far less reactive than the planar (pϕ=0p_{\phi}=0) slice — atE=0.5E=0.5the direct-reactive fraction of the incoming ensemble is0.360.36, against0.610.61on the planar leaf — so the two-degree-of-freedom problem is not representative of the three-degree-of-freedom one. The coupling leaves the direct-reactive fraction unchanged within sampling error but redistributes the non-reactive population: atE=0.5E=0.5, switching onb=0.3b=0.3lowers the direct non-reactive fraction from0.4140.414to0.3820.382, a decrease of0.032±0.0060.032\pm 0.006; the roaming non-reactive fraction rises by0.0300.030and the roaming reactive by0.0110.011, while the direct-reactive fraction falls by0.0080.008, within sampling error; the pooled non-reactive gap distribution shifts toward longer typical times as the roaming population grows, while the longest trappings of the symmetric limit are cut off. Across the window the effect decays — the transfer is0.0240.024atE=0.7E=0.7and zero within sampling error fromE=1​kcal​mol−1E=1\ \mathrm{kcal\,mol^{-1}}— because faster trajectories traverse the roaming region in fewer periods of the roaming motion than the transverse instability needs. The trajectories show the same mechanism that Section6.6establishes for the manifolds:pϕp_{\phi}is no longer constant along trajectories, and about a fifth of the off-plane launches reverse their sense of precession about the symmetry axis, passing between the two components that the symmetric limit keeps disjoint (Section7.5).

The relation to the ozone recombination study of Mauguière, Collins, Kramer, Carpenter, Ezra, Farantos, and Wiggins[13]— a three-degree-of-freedom roaming study in the same phase-space framework — is complementary. There the third degree of freedom, the diatomic vibration, decouples adiabatically, and the three-degree-of-freedom computation validates the two-degree-of-freedom reduction; here the third degree of freedom is activated by the symmetry-breaking coupling, and the reduction fails in a controlled, quantifiable way. Both are families of two-degree-of-freedom subsystems parametrized by a momentum — conserved there in an adiabatic approximation, conserved here exactly atb=0b=0and destroyed forb>0b>0. Two limitations delimit the present study. The analysis is carried out at zero total angular momentum; the rotating (J≠0J\neq 0) case introduces Coriolis coupling and centrifugal terms that enlarge the accessible phase space and may support trapping mechanisms absent here. And we have not examined behavior near the upper edge of the roaming energy window.

## 9Conclusion

We have constructed and analyzed a concrete, tractable three-degree-of-freedom Chesnavich model designed for the phase-space analysis of roaming. The model is derived from the Ezra–Wiggins rigid-body formulation, breaks the cylindrical symmetry of Chesnavich’s model with a coupling that respects the physicalC3C_{3}symmetry of the methyl fragment, uses the physically mandated planar-top inertia ratioIz=2​IxI_{z}=2I_{x}, and recovers the 2-DoF model atb=0b=0as its planar reduction.

Its central dynamical feature is the immediate activation of the out-of-plane degree of freedom when the cylindrical symmetry is broken. With the physical inertia ratio and theC3C_{3}coupling, the roaming-shelf orbit FR1 is transversely hyperbolic for essentially allb>0b>0: below the narrow elliptic window0.58≲b≲0.630.58\lesssim b\lesssim 0.63the transverse multiplier pair is real and positive; beyond the period-doubling atbc≈0.63b_{c}\approx 0.63it is real and negative, so that neighboring trajectories alternate sides of the reaction plane on successive periods. FR1 is positive-hyperbolic below the elliptic window, elliptic within it, and negative-hyperbolic beyond the period-doubling atbcb_{c}.

A dividing surface in the five-dimensional energy surface must be four-dimensional, and it must be anchored on a three-dimensional invariant manifold — two dimensions more than a periodic orbit provides. We therefore identified and explicitly constructed the anchoring objects: three three-dimensional normally hyperbolic invariant manifolds, one for each transition state, exhibited in theb=0b=0limit as two-component families of invariant tori over the conserved angular momentumpϕp_{\phi}. Three results about these manifolds are established in Sections6and6.7, as six propositions resting on a single numerically established hypothesis: the topology of the dividing surface each manifold anchors; the status of each generating orbit as the separatrix member of its family; and the persistence of every compact interior piece of each manifold for sufficiently smallb>0b>0.

Building on these surfaces, we carried the classification of Mauguière, Collins, Ezra, Farantos, and Wiggins into three degrees of freedom (Section7). Atb=0b=0the dynamics decomposes into a one-parameter family of two-degree-of-freedom subsystems, and these subsystems differ substantially from one another: the roaming fraction of a leaf grows with its angular momentum, doubling betweenpϕ=0p_{\phi}=0andpϕ=0.8p_{\phi}=0.8. Breaking the symmetry opens an out-of-plane escape route. At the base energyE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}it moves0.0320.032of the incoming ensemble out of direct non-reactive escape, the two roaming classes gaining0.0400.040, and shifts the pooled gap-time distribution toward longer typical times through the larger roaming population, while leaving the direct-reactive fraction unchanged; the effect dies away across the roaming energy window. Along trajectories the route appears as the loss of constancy ofpϕp_{\phi}: about a fifth of the off-plane launches reverse their sense of precession about the symmetry axis, passing between the two family components that the symmetric limit keeps disjoint. The model provides a concrete, tractable setting in which the three-degree-of-freedom phase-space theory of roaming can be developed and tested.

## Appendix ASymbolic derivation and verification

The reduced Hamiltonian (1) and the properties (i)–(iii) of Section2were verified with a computer-algebra system. The rotational kinetic energy was checked against the Ezra–Wiggins reduction[15]. Theb=0b=0reduction to the 2-DoF Chesnavich Hamiltonian was verified to vanish identically in the difference of the two expressions. The discrete symmetries were verified by direct substitution. The Cartesian form of the coupling,V0​[(X2+Y2)/r2+b​(X3−3​X​Y2)/r3]V_{0}[(X^{2}+Y^{2})/r^{2}+b(X^{3}-3XY^{2})/r^{3}], was confirmed to be smooth away from the origin and to reproduce (4) under(X,Y,Z)=r​(sin⁡θ​cos⁡ϕ,sin⁡θ​sin⁡ϕ,cos⁡θ)(X,Y,Z)=r(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta).

## Appendix BThe body-frame coordinate singularity

Body-frame spherical coordinates(r,θ,ϕ)(r,\theta,\phi)are singular on the symmetry axisθ=0,π\theta=0,\pi, whereϕ\phiis undefined. Two distinct difficulties arise there, and both must be handled because every generating orbit crosses the axis twice per period: the planar FR1 and OTS orbits rotate, passing through both poles each period, and the planar TTS orbit librates, crossing a single pole twice per period (the axis is met to within∼2×10−4​rad\sim 2\times 10^{-4}\ \mathrm{rad}in our computations).

First, the kinetic coefficient of the azimuthal variational equation contains a factorcsc2⁡θ\csc^{2}\theta, which diverges on the axis. A transverse stability computation carried out naively in(ϕ,pϕ)(\phi,p_{\phi})therefore returns spurious, integrator-tolerance-dependent multipliers as large as10910^{9}. The resolution is to compute the transverse dynamics in Cartesian body-frame coordinates(X,Y,Z)(X,Y,Z), in which the out-of-plane pair(Y,pY)(Y,p_{Y})is smooth across the axis; the transverse block of the monodromy matrix is then finite and well behaved (the values reported in Fig.4).

Second, and more fundamentally, the potential coupling must itself be smooth across the axis for the dynamics to be well defined there. A one-fold coupling of the formsin2⁡θ​cos⁡ϕ\sin^{2}\theta\cos\phihas Cartesian form proportional toX​X2+Y2/r2X\sqrt{X^{2}+Y^{2}}/r^{2}, which is continuous but only once differentiable on the axis; its second derivatives, which enter the variational equation, are discontinuous. This is why theC3C_{3}couplingsin3⁡θ​cos⁡3​ϕ=(X3−3​X​Y2)/r3\sin^{3}\theta\cos 3\phi=(X^{3}-3XY^{2})/r^{3}, the angular factor of a solid harmonic and smooth away from the origin, is required: it is both physically appropriate (respecting the methyl three-fold symmetry) and analytically smooth across the axis the orbits traverse. The axis crossing also underlies the conical center of each two-component NHIM family (Section6.5): the closest approach of the FR1 family to the axis scales linearly with the angular momentum,ρmin≃1.69​|pϕ|\rho_{\min}\simeq 1.69\,|p_{\phi}|, so the family meets the axis in a cone rather than tangentially; the OTS and TTS families have their own linear constants (Section6.5).

## Appendix CPeriodic-orbit location, continuation, and stability

Trajectories were integrated with the explicit adaptive Runge–Kutta method of order eight, DOP853[25], with relative and absolute tolerances of10−1210^{-12}and10−1310^{-13}; energy was conserved to one part in101210^{12}or better along all reported orbits. The FR1 and OTS orbits were located in the reaction plane by shooting from the symmetric equatorial launch (θ=π/2\theta=\pi/2,pr=0p_{r}=0) and imposing the symmetric-return conditionpr=0p_{r}=0at the first axis crossing. The launch radius is determined by this condition:r0r_{0}is a root of the scalar functionr0↦pr​(taxis;r0)r_{0}\mapsto p_{r}(t_{\mathrm{axis}};r_{0}), located by bisection. Atpϕ=0p_{\phi}=0the FR1 and OTS orbits rotate —θ\thetaadvances monotonically andpθp_{\theta}has no zeros — so for these two orbits aθ\theta-turning cannot serve as the return event. The shooting returns FR1 atr0≈3.18r_{0}\approx 3.18and OTS atr0≈13.4r_{0}\approx 13.4. The TTS orbit crosses the axis rather than the equator and was located by shooting from the axis (θ=0\theta=0,pr=0p_{r}=0), with the return conditionpr=0p_{r}=0imposed at the first zero ofpθp_{\theta}: it librates through the axis withθmax≈41∘\theta_{\max}\approx 41^{\circ}overr∈[2.38,2.64]r\in[2.38,2.64], arcing across the mouth of the well just outside the ridge crestrc=2.2r_{c}=2.2, with periodT=2.228T=2.228and multiplierλTTS=220.5\lambda_{\mathrm{TTS}}=220.5. The same axis-shooting condition admits three further periodic orbits interior to the well, with axis crossings atr0≈0.98r_{0}\approx 0.98,1.191.19, and1.521.52andθmax≈49∘\theta_{\max}\approx 49^{\circ},67∘67^{\circ}, and50∘50^{\circ}; continuation steps that are too large can cause the continuation to jump onto these, and the orbit atr0≈1.19r_{0}\approx 1.19loses hyperbolicity entirely forb≳0.05b\gtrsim 0.05, so a jump is detectable by a collapse of the multiplier. Each orbit was continued inpϕp_{\phi}, inbb, and inEEby using the solution at one parameter value as the initial guess at the next[31]. The monodromy matrix was obtained by integrating the6×66\times 6variational system over one period with the analytic Jacobian[30,32]; the transverse block was extracted in the(Y,pY)(Y,p_{Y})coordinates, and the elliptic/hyperbolic classification follows from whether its trace lies within or outside[−2,2][-2,2]. The bifurcation threshold was located by bracketing the transverse trace to the value−2-2, givingbc=0.632b_{c}=0.632both from the variational monodromy matrix and from a finite-difference monodromy matrix of the time-TTflow, stable under tightening the integrator tolerance from10−1110^{-11}to10−1310^{-13}. The equatorial shooting condition admits a second periodic-orbit solution besides FR1, with action≈12.6\approx 12.6; FR1 is the solution with action13.75513.755, identified by its reduction to the 2-DoF orbit atb=0b=0, and continuation steps ofΔ​b≲0.03\Delta b\lesssim 0.03keep the continuation on it.

## Appendix DTrajectory classification: sampling, gap times, and robustness

Trajectories for the classification of Section7were integrated with the same DOP853 scheme as the orbits (AppendixC), at relative and absolute tolerances10−1010^{-10}and10−1210^{-12}, with the reduced massm=0.9445m=0.9445(frommH=1.007825m_{\mathrm{H}}=1.007825andmC=12.0m_{\mathrm{C}}=12.0); energy was conserved to better than one part in10810^{8}, ample for counting surface crossings. The classification was performed for two values of the coupling,b=0b=0andb=0.3b=0.3, and repeated across the roaming energy window for one purpose: to locate where the effect of the coupling dies away. Sample sizes:1500015000per coupling value atE=0.5E=0.5,50005000atE=0.7E=0.7, and12001200at each ofE∈{1.0,1.25,1.5,2.0}​kcal​mol−1E\in\{1.0,1.25,1.5,2.0\}\ \mathrm{kcal\,mol^{-1}}; the classification planes of Fig.8used an80×11080\times 110grid in(θ,pθ)(\theta,p_{\theta})atϕ=0\phi=0. All other computations in the paper are atE=0.5​kcal​mol−1E=0.5\ \mathrm{kcal\,mol^{-1}}.

Initial conditions were sampled on the entrance surface atrOTS=13.386​År_{\mathrm{OTS}}=13.386\ \text{\text{\AA }}, uniformly in the canonical surface coordinates(θ,ϕ,pθ,pϕ)(\theta,\phi,p_{\theta},p_{\phi})over the energetically allowed region withθ∈(0.05,π−0.05)\theta\in(0.05,\pi-0.05), andpr<0p_{r}<0fixed byH=EH=E. The omitted polar caps carry≈1.0×10−3\approx 1.0\times 10^{-3}of the surface measure, computed by quadrature of the allowed(pθ,pϕ)(p_{\theta},p_{\phi})area overθ<0.05\theta<0.05— an order of magnitude below the smallest class shift reported in Section7. This uniform sample realizes the flux-weighted microcanonical measure — the ensemble in which initial conditions on the surface are weighted by the rate at which trajectories cross it, the appropriate ensemble for an incoming stream of trajectories. The identification holds because the crossing-rate factor cancels the Jacobian of the energy constraint: on the section{r=r0}\{r=r_{0}\}the magnitude of the directional flux isℱ​(E)=∫δ​(H−E)​δ​(r−r0)​|r˙|​Θ​(−r˙)​𝑑𝐪​𝑑𝐩=∫allowed𝑑θ​𝑑ϕ​𝑑pθ​𝑑pϕ,\mathcal{F}(E)=\int\delta(H-E)\,\delta(r-r_{0})\,|\dot{r}|\,\Theta(-\dot{r})\,d\mathbf{q}\,d\mathbf{p}=\int_{\mathrm{allowed}}d\theta\,d\phi\,dp_{\theta}\,dp_{\phi},

with|r˙|=|pr|/m|\dot{r}|=|p_{r}|/mcanceling the Jacobian ofδ​(H−E)\delta(H-E)on integrating outprp_{r}.

In the computation the three surfaces are realized as radial thresholds: a crossing of the classifier is a crossing ofrFR1=3.40​År_{\mathrm{FR1}}=3.40\ \text{\text{\AA }}; a trajectory is reactive whenrrfalls belowrreact=2.0​År_{\mathrm{react}}=2.0\ \text{\text{\AA }}and non-reactive when it returns outward through the launch surface. Classes follow the parity rule of Section7.1, with zero-crossing non-reactive trajectories reported as their own class. No trajectory remained unclassified at the integration limittmax=500t_{\max}=500.

The gap time of Section7.4is measured at the entrance dividing surface, between entry and exit. Two times were in fact recorded for every trajectory: the gap at the entrance surface, and the time between the first inward and last outward crossing of an inner surface atr=9.5​År=9.5\ \text{\text{\AA }}. The purely radial flights from the two surfaces to the shelf bottleneck and back take18.118.1and10.610.6time units respectively atE=0.5E=0.5(the shortest observed gaps are19.119.1and11.611.6); the corrugation satisfiesV0​(r)<10−19V_{0}(r)<10^{-19}forr>8​År>8\ \text{\text{\AA }}, so the inward and outward flights are identical for the two couplings, and anybb-dependence of the statistics arises inside the interaction region. The distributions of Section7.4are conditioned on the non-reactive outcome. The reactive capture times, measured from entry at the entrance surface to arrival below the capture radius, have means19.019.0(b=0b=0) and20.420.4(b=0.3b=0.3) atE=0.5E=0.5. The inner-surface gap statistics lead to the same conclusions as the entrance-surface statistics reported in the text: atE=0.5E=0.5the non-reactive means are25.525.5(b=0b=0) and26.226.2(b=0.3b=0.3), the coefficients of variation beyond the minimum are1.91.9and1.41.4, the 90th percentile rises from4141to4747, and the extreme tail shortens.

The robustness scan integrates each trajectory once, recording the crossing times of all candidate surfaces, and reclassifies. AtE=0.5E=0.5, over the gridrFR1∈{3.25,3.40,3.55}​År_{\mathrm{FR1}}\in\{3.25,3.40,3.55\}\ \text{\text{\AA }}andrreact∈{1.8,2.0,2.2}​År_{\mathrm{react}}\in\{1.8,2.0,2.2\}\ \text{\text{\AA }}, every class fraction moves by at most0.0110.011, about a quarter of the0.0400.040out-of-plane effect; repeating the full computation with the launch surface at14​Å14\ \text{\text{\AA }}(50005000samples per coupling value) reproduces every fraction and theE=0.5E=0.5transfer within one standard error. The centrifugal barrier that lies beyond the launch surface for smallpϕp_{\phi}(Section7.6) exceeds the potential at the launch radius by at most0.0015​kcal​mol−10.0015\ \mathrm{kcal\,mol^{-1}}over the admissiblepϕp_{\phi}, so only trajectories leaving the launch surface with outward radial kinetic energy below0.0015​kcal​mol−10.0015\ \mathrm{kcal\,mol^{-1}}can be turned back — a negligible subset of the ensemble.

## Appendix ENumerical verification

The results were re-derived by methods independent of those that produced them, and all checks pass.

For the planar orbits: FR1 was recovered as a fixed point of a Poincaré return map on the section{Z=0,pZ>0}\{Z=0,\,p_{Z}>0\}(residual∼10−13\sim 10^{-13}). This computation imposes no symmetry: the launch is not restricted topr=0p_{r}=0on the equator, yet the converged fixed point satisfies that condition, independently confirming the symmetric construction of AppendixC. The transverse block of the monodromy matrix from the analytic Jacobian agrees with a finite-difference monodromy matrix of the time-TTflow to∼10−12\sim 10^{-12}in the trace at every value ofbbin the continuation grid of Fig.4; the full monodromy matrix is symplectic (det=1\det=1) with reciprocal eigenvalue pairs, the hyperbolic pair being{24.57,0.0407}\{24.57,\ 0.0407\}. The abbreviated action computed as∮2​(E−V)​𝑑t\oint 2(E-V)\,dtagrees with∮p​𝑑q\oint p\,dqat everybbin the same grid. The TTS orbit was additionally verified by a computation that involves no trajectory integration at all: a discrete-variational solution of Hamilton’s principle on a periodic lattice, with the multiplier obtained from the block product of the discrete-action Hessian. Along the TTS family the abbreviated actionW=∮p​𝑑qW=\oint p\,dqand the periodTTwere checked against the classical identityd​W/d​E=TdW/dE=T(the derivative taken along the family at fixedpϕp_{\phi}), and the integration-free and shooting routes agree to five significant figures.

For the two-component manifolds of Section6the following were verified independently. (i) The azimuthal momentum is conserved to10−1110^{-11}on a generic trajectory atb=0b=0. (ii) The reduced family is normally hyperbolic with the algebraic multiplicity of the eigenvalue11equal to four and the tangent directions (flow, azimuthal rotation, the family direction∂/∂pϕ\partial/\partial p_{\phi}) carrying no component in the hyperbolic eigenspace (spectral-projector residuals≲10−13\lesssim 10^{-13}); the normal multiplier of FR1 decreases monotonically from24.624.6to unity atp∗=1.799p_{*}=1.799,λ\lambdareal and greater than one at every interiorpϕp_{\phi}. (iii) The closest approach of the FR1 family to the axis scaleslinearlywith the angular momentum,ρmin=1.686​|pϕ|\rho_{\min}=1.686\,|p_{\phi}|to four figures over0<pϕ<0.40<p_{\phi}<0.4— a cone, not a smooth tangency. The measured slope agrees with the prediction of Section6.5: withθ−=k​|pϕ|\theta_{-}=k\,|p_{\phi}|the linear law for the polar turning angle andrtr_{t}the radius there, the closest approach isρmin≈rt​sin⁡θ−≈rt​k​|pϕ|\rho_{\min}\approx r_{t}\sin\theta_{-}\approx r_{t}\,k\,|p_{\phi}|, andrt​k=1.6863r_{t}\,k=1.6863. (iv) Along the FR1 family the kinetic energy at the polar turning point tends to a finite nonzero limit,E−V→1.1736E-V\to 1.1736aspϕ→0+p_{\phi}\to 0^{+}, carried entirely by the azimuthal motion — the signature of the momentum segments in the limit of the family (Section6.5). (v) The reduced dividing surface is a two-sphere for all three orbits (each reduced orbit librates), and the flux form (9) vanishes only at the two periodic-orbit momenta on each momentum ellipse. (vi) The invariance of theb=0b=0tori and their breakup forb>0b>0were checked directly on a single trajectory started on an interior torus and followed for twelve periods of the roaming motion. Atb=0b=0itspϕp_{\phi}is constant to10−1110^{-11}, as it must be on an invariant torus. Atb=0.05b=0.05the value ofpϕp_{\phi}along the same trajectory ranges over an interval of width0.1360.136, and atb=0.30b=0.30of width1.021.02; energy is conserved to∼10−9\sim 10^{-9}throughout, so the spread is dynamical, not numerical — the tori are gone.

The quantities established for the reduced families in Section6.2are load points of the paper: the endpoint behavior of each family and the nondegeneracy conditions enter the propositions of Section6.7as hypotheses, and the family radii enter Section7as the placement data for the classification surfaces. Each was therefore re-derived independently of the continuation that produced it, with the machinery first validated on FR1 against theλ​(pϕ)\lambda(p_{\phi})curve and the endpointp∗=1.799p_{*}=1.799. The termination mechanisms: the OTS family terminates atp∗=2.1495p_{*}=2.1495by amplitude collapse onto the azimuthal relative equilibrium atr=9.600r=9.600, and the TTS family atp∗=1.3168p_{*}=1.3168on the saddle–center equilibrium that the centrifugal term creates in the mouth of the well (r=2.446r=2.446,θ=29.4∘\theta=29.4^{\circ}) — in both cases the endpoint multiplier is predicted from the linearized rates of the limiting equilibrium,eμr⋅2​π/ωθe^{\mu_{r}\cdot 2\pi/\omega_{\theta}}, giving1.26851.2685and15.9015.90, and matched by the family; this confirms that these two families end on caps with normal hyperbolicity intact, as the per-family statements of Sections6.2and6.4require. The TTS inner-edge limitsT​(0+)=Tplanar/2T(0^{+})=T_{\mathrm{planar}}/2andλ​(0+)=λplanar\lambda(0^{+})=\sqrt{\lambda_{\mathrm{planar}}}confirm the double-cover relation between the reduced TTS family and the planar orbit. The linear lawθ−=k​|pϕ|\theta_{-}=k\,|p_{\phi}|holds per family withkkgiven by the turning-point formula of Section6.5(FR10.46190.4619, OTS0.6510.651, TTS0.3040.304), confirming the cone constants. And the two nondegeneracy hypotheses of Proposition2were verified directly: the azimuthal advanceΔ​ϕ​(pϕ)\Delta\phi(p_{\phi})is monotone (from2​π2\pito4.6134.613across the FR1 family) andd​T/d​E=−3.16≠0dT/dE=-3.16\neq 0atpϕ=0.5p_{\phi}=0.5.

For the trajectory classification (Section7): the integrating core reproduces the published planar FR1 values atm=0.9445m=0.9445(r0=3.1791r_{0}=3.1791,W=13.7547W=13.7547,λ=24.5732\lambda=24.5732, transverse trace+2+2to2×10−112\times 10^{-11}); the planar classification leaf reproduces the two-degree-of-freedom fractions (88.1%88.1\%direct,11.9%11.9\%roaming); theE=0.5E=0.5transfer is established at1500015000samples per coupling value, the direct non-reactive and roaming non-reactive shifts significant at six and seven standard errors, the roaming reactive shift at three, and the direct-reactive shift within1.51.5standard errors; and the threshold and launch-radius scans of AppendixDbound the placement sensitivity at a quarter of the effect. Finally, the planar TTS orbit, both family caps and endpoint multipliers, the FR1 endpoint, the cone constants, and the double-cover limits were reproduced by a second, fully disjoint implementation — potential and derivatives regenerated from the published formulas, a fixed-step implicit-midpoint symplectic integrator in place of DOP853, multipliers from finite-difference monodromy matrices, cap predictions by root-finding and linearization without integration — together with the classical identitiesd​W/d​E=TdW/dE=Tandd​W/d​pϕ=−Δ​ϕdW/dp_{\phi}=-\Delta\phi, satisfied to10−610^{-6}or better.

## References
- [1]D. G. Truhlar, B. C. Garrett, and S. J. Klippenstein, “Current status of transition-state theory,” J. Phys. Chem.100, 12771–12800 (1996).
- [2]H. Waalkens, R. Schubert, and S. Wiggins, “Wigner’s dynamical transition state theory in phase space: classical and quantum,” Nonlinearity21, R1–R118 (2008).
- [3]D. Townsend, S. A. Lahankar, S. K. Lee, S. D. Chambreau, A. G. Suits, X. Zhang, J. Rheinecker, L. B. Harding, and J. M. Bowman, “The roaming atom: Straying from the reaction path in formaldehyde decomposition,” Science306, 1158–1161 (2004).
- [4]J. M. Bowman and A. G. Suits, “Roaming reactions: The third way,” Phys. Today64(11), 33–37 (2011).
- [5]J. M. Bowman, “Roaming,” Mol. Phys.112, 2516–2528 (2014).
- [6]F. A. L. Mauguière, P. Collins, Z. C. Kramer, B. K. Carpenter, G. S. Ezra, S. C. Farantos, and S. Wiggins, “Phase space structures explain the roaming mechanism in chemical reaction dynamics: a review,” Annu. Rev. Phys. Chem.68, 499–524 (2017).
- [7]A. G. Suits, “Roaming reactions and dynamics in the van der Waals region,” Annu. Rev. Phys. Chem.71, 77–100 (2020).
- [8]J. Meyer and R. Wester, “Ion–molecule reaction dynamics,” Annu. Rev. Phys. Chem.68, 333–353 (2017).
- [9]S. Wiggins, “The role of normally hyperbolic invariant manifolds (NHIMs) in the context of the phase space setting for chemical reaction dynamics,” Regul. Chaotic Dyn.21, 621–638 (2016).
- [10]W. J. Chesnavich, “Multiple transition states in unimolecular reactions,” J. Chem. Phys.84, 2615–2619 (1986).
- [11]W. J. Chesnavich and M. T. Bowers, “Theory of ion-neutral interactions: application of transition state theory concepts to both collisional and reactive properties of simple systems,” Prog. React. Kinet.11, 137–267 (1982).
- [12]F. A. L. Mauguière, P. Collins, G. S. Ezra, S. C. Farantos, and S. Wiggins, “Roaming dynamics in ion-molecule reactions: Phase space reaction pathways and geometrical interpretation,” J. Chem. Phys.140, 134112 (2014).
- [13]F. A. L. Mauguière, P. Collins, Z. C. Kramer, B. K. Carpenter, G. S. Ezra, S. C. Farantos, and S. Wiggins, “Phase space barriers and dividing surfaces in the absence of critical points of the potential energy: Application to roaming in ozone,” J. Chem. Phys.144, 054107 (2016).
- [14]V. Krajňák and S. Wiggins, “Influence of mass and potential energy surface geometry on roaming in Chesnavich’sCH4+\mathrm{CH_{4}^{+}}model,” J. Chem. Phys.149, 094109 (2018).
- [15]G. S. Ezra and S. Wiggins, “The Chesnavich model for ion-molecule reactions: a rigid body coupled to a particle,” Int. J. Bifurcation Chaos29, 1950025 (2019).
- [16]H. Goldstein, C. P. Poole, and J. L. Safko,Classical Mechanics, 3rd ed. (Addison-Wesley, San Francisco, 2002), Chap. 5.
- [17]V. Krajňák, V. J. García-Garrido, and S. Wiggins, “Reactive islands for three degrees-of-freedom Hamiltonian systems,” Physica D425, 132976 (2021).
- [18]F. A. L. Mauguière, P. Collins, Z. C. Kramer, B. K. Carpenter, G. S. Ezra, S. C. Farantos, and S. Wiggins, “Phase space structures explain hydrogen atom roaming in formaldehyde decomposition,” J. Phys. Chem. Lett.6, 4123–4128 (2015).
- [19]P. L. Houston, R. Conte, and J. M. Bowman, “Roaming under the microscope: Trajectory study of formaldehyde dissociation,” J. Phys. Chem. A120, 5103–5114 (2016).
- [20]V. Krajňák and S. Wiggins, “Roaming in acetaldehyde,” J. Chem. Phys.160, 244104 (2024).
- [21]N. Fenichel, “Persistence and smoothness of invariant manifolds for flows,” Indiana Univ. Math. J.21, 193–226 (1971).
- [22]M. W. Hirsch, C. C. Pugh, and M. Shub,Invariant Manifolds, Lecture Notes in Mathematics Vol. 583 (Springer, Berlin, 1977).
- [23]S. Wiggins,Normally Hyperbolic Invariant Manifolds in Dynamical Systems(Springer, New York, 1994).
- [24]S. Wiggins, “An entropic bottleneck, dynamical gating, and outward redistribution of roaming in a designed Chesnavich-type model,” arXiv:2607.06437 (2026).
- [25]E. Hairer, S. P. Nørsett, and G. Wanner,Solving Ordinary Differential Equations I: Nonstiff Problems, 2nd ed. (Springer, Berlin, 1993).
- [26]P. L. Houston and S. H. Kable, “Photodissociation of acetaldehyde as a second example of the roaming mechanism,” Proc. Natl. Acad. Sci. U.S.A.103, 16079–16082 (2006).
- [27]L. Rubio-Lago, G. A. Amaral, A. Arregui, J. G. Izquierdo, F. Wang, D. Zaouris, T. N. Kitsopoulos, and L. Bañares, “Slice imaging of the photodissociation of acetaldehyde at 248 nm: evidence of a roaming mechanism,” Phys. Chem. Chem. Phys.9, 6123–6127 (2007).
- [28]B. R. Heazlewood, M. J. T. Jordan, S. H. Kable, T. M. Selby, D. L. Osborn, B. C. Shepler, B. J. Braams, and J. M. Bowman, “Roaming is the dominant mechanism for molecular products in acetaldehyde photodissociation,” Proc. Natl. Acad. Sci. U.S.A.105, 12719–12724 (2008).
- [29]B. C. Shepler, B. J. Braams, and J. M. Bowman, “Roaming dynamics inCH3​CHO\mathrm{CH_{3}CHO}photodissociation revealed on a global potential energy surface,” J. Phys. Chem. A112, 9344–9351 (2008).
- [30]T. S. Parker and L. O. Chua,Practical Numerical Algorithms for Chaotic Systems(Springer, New York, 1989).
- [31]E. L. Allgower and K. Georg,Numerical Continuation Methods: An Introduction, Springer Series in Computational Mathematics Vol. 13 (Springer, Berlin, 1990).
- [32]K. R. Meyer, G. R. Hall, and D. Offin,Introduction to Hamiltonian Dynamical Systems and theNN-Body Problem, 2nd ed., Applied Mathematical Sciences Vol. 90 (Springer, New York, 2009).

## 


- 


Major funding support from
