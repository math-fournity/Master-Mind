# Analytic Derivation of Vertical Chromaticity in the Fermilab Muon $g{-}2$ Storage Ring

**arXiv ID**: 2606.09903v1
**Authors**: Eremey Valetov, Kyoko Makino, Martin Berz
**Published**: 2026-06-05
**Categories**: physics.acc-ph, math-ph
**Comments**: 21 pages, 4 figures, 1 table. Contribution to the proceedings of the International Conference on New Frontiers in Physics (ICNFP 2025); submitted to International Journal of Modern Physics A
**HTML URL**: https://arxiv.org/html/2606.09903v1

## Abstract

We derive the vertical chromaticity $ξ_y$ of the Fermilab Muon g-2 storage ring in closed analytic form. Expanding the Hamiltonian as a Taylor polynomial in the dynamical variables and integrating the equations of motion order by order, we obtain the vertical second-order aberrations of the homogeneous magnetic dipole ($\mathtt{DI}$) and the combined-function dipole-and-electrostatic-quadrupole element ($\mathtt{DIQ}$) used in the muon $g{-}2$ ring. Composing the per-element maps over the periodic dispersion orbit yields a closed-form expression for the vertical chromaticity $\xichromy$ of the continuous-ring $\mathtt{DIQ360}$ model, in direct functional analogy with the horizontal result of our earlier work on the same ring (Ref.~\refcite{ChromCPO11}). Comparison against COSY INFINITY differential-algebra computation shows agreement at the $10^{-11}$ level across all three ring models ($\mathtt{DIQ360}$ closed form and the modular $\mathtt{DIEQ\_ON}$, $\mathtt{DIEQ}$ via per-element composition) for muon $g{-}2$ electrostatic-quadrupole (ESQ) voltages $\Vesq \in [10, 26]\,\mathrm{kV}$.

## Full Text

Analytic Derivation of Vertical Chromaticity in the Fermilab Muon 𝑔-2 Storage RingFermilab report FERMILAB-PUB-26-0333-PPD.

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2606.09903v1 [physics.acc-ph] 05 Jun 2026\catchline

## Analytic Derivation of Vertical Chromaticity in the Fermilab Muong−2g{-}2Storage Ring††thanks:Fermilab report FERMILAB-PUB-26-0333-PPD.EREMEY VALETOVKYOKO MAKINOand MARTIN BERZDepartment of Physics and Astronomy, Michigan State University,
East Lansing, MI 48824, USA
Muong−2g{-}2Collaboration, Fermi National Accelerator Laboratory,
Batavia, IL 60510, USA
evv@msu.edu (corresponding author), makino@msu.edu, berz@msu.edu

## Abstract

We derive the vertical chromaticityξy\xi_{y}of the Fermilab Muong−2g{-}2storage ring in closed analytic form. Expanding the Hamiltonian as a
Taylor polynomial in the dynamical variables and integrating the equations
of motion order by order, we obtain the
vertical second-order aberrations of the homogeneous magnetic dipole
(𝙳𝙸\mathtt{DI}) and the combined-function dipole-and-electrostatic-quadrupole
element (𝙳𝙸𝚀\mathtt{DIQ}) used in the muong−2g{-}2ring. Composing the per-element
maps over the periodic dispersion orbit yields a closed-form expression for the
vertical chromaticityξy\xi_{y}of the continuous-ring𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}model, in direct functional analogy with the horizontal
result of our earlier work on the same ring (Ref.\refciteChromCPO11).
Comparison against COSY INFINITY differential-algebra computation shows
agreement at the10−1110^{-11}level across all three ring models (𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}closed form and the modular𝙳𝙸𝙴𝚀​_​𝙾𝙽\mathtt{DIEQ\_ON},𝙳𝙸𝙴𝚀\mathtt{DIEQ}via per-element
composition) for muong−2g{-}2electrostatic-quadrupole (ESQ) voltagesVESQ∈[10,26]​kVV_{\mathrm{ESQ}}\in[10,26]\,\mathrm{kV}.{history}

## 1Introduction

The Fermilab Muong−2g{-}2Experiment (E989)[8]recently reported
the muon anomalous magnetic moment with a precision of127​ppb127\,\mathrm{ppb}[14,13], the most precise measurement ofaμa_{\mu}to date. Extractingaμa_{\mu}from the measured spin-precession
frequencyωa\omega_{a}requires beam-dynamics corrections that are sensitive
to the closed orbit, betatron tunes, and chromaticities of the storage
ring[12,20]. Among these, the vertical
chromaticityξy\xi_{y}is a fundamental beam-dynamics observable of
the muon storage ring; its analytic closed-form expression is the
subject of the present work.

We previously derived the analytic horizontal second-order aberrations
of the homogeneous magnetic dipole (𝙳𝙸\mathtt{DI}) and the
combined-function dipole-and-electrostatic-quadrupole element
(𝙳𝙸𝚀\mathtt{DIQ}) of the muong−2g{-}2ring, together with a closed-form
horizontal chromaticityξx\xi_{x}[18],
using the order-by-order Hamiltonian perturbation method.
This method, introduced in Karl Brown’s foundational
work[6,4,7,5]and developed in
the Hamiltonian treatments of
Refs.\refciteAIEP108book,IP127book, expresses the equations of
motion as truncated power series: the linear part is solved exactly
(a matrix exponential for constant-coefficient elements), and each
higher order is obtained iteratively by
treating the lower-order solution as a driving term in an aberration
integral. We have also applied it to electrostatic
deflectors in Refs.\refciteELSPHTM17,ESCPO10AIEP. The vertical
chromaticity has been computed numerically by the
differential-algebra (DA) techniques of
Refs.\refciteAIEP108book,COSYCAP04,COSYCPO11 but has lacked an
analytic counterpart. The present work supplies that counterpart: a
closed-formξy\xi_{y}for the continuous-ring𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}model, together with the full vertical second-order
aberration table for𝙳𝙸\mathtt{DI}and𝙳𝙸𝚀\mathtt{DIQ}, validated
numerically against COSY INFINITY DA across a sweep of the
muong−2g{-}2storage-ring operating voltages.

## 2The Muong−2g{-}2Storage Ring

The muong−2g{-}2storage ring at Fermilab consists of a homogeneous vertical
magnetic-dipole field of1.45​T1.45\,\mathrm{T}providing a closed circular
reference orbit of radiusR0=7.112​mR_{0}=7.112\,\mathrm{m}, and four
electrostatic-quadrupole (ESQ) stations providing vertical focusing. The reference muon momentum
is the nominal magic momentump0=3094​MeV/cp_{0}=3094\,\mathrm{MeV}/c[8],
at which the electric-field contribution to the spin-precession
frequency vanishes at first order[13]. We use the
reference Lorentz factor[11,18]γ0=29.300124824596928.\gamma_{0}=29.300124824596928.(1)

The four ESQ stations together cover approximately43%43\%of the ring azimuth.
A schematic of the storage ring is shown in Fig.2.
Three ring models are studied here. The continuous ring𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}is a
single360∘360^{\circ}𝙳𝙸𝚀\mathtt{DIQ}element with the four ESQ stations represented
by their azimuthally averaged inhomogeneity; this is the form for which a
closed-formξy\xi_{y}is obtained in Sec.5. The
simplified modular ring𝙳𝙸𝙴𝚀​_​𝙾𝙽\mathtt{DIEQ\_ON}lumps the two ESQ
elements of each quadrant into a single43∘43^{\circ}𝙳𝙸𝚀\mathtt{DIQ}element, giving four cells of𝙳𝙸​47∘+𝙳𝙸𝚀​43∘\mathtt{DI}\,47^{\circ}+\mathtt{DIQ}\,43^{\circ}per quadrant (90∘). This is the geometry used in
Ref.\refciteonkim for the horizontal chromaticity derivation, and
lies between𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}and the full modular structure. The full modular ring𝙳𝙸𝙴𝚀\mathtt{DIEQ}resolves each quadrant
into four elements (𝙳𝙸​47∘+𝙳𝙸𝚀​13∘+𝙳𝙸​4∘+𝙳𝙸𝚀​26∘\mathtt{DI}\,47^{\circ}+\mathtt{DIQ}\,13^{\circ}+\mathtt{DI}\,4^{\circ}+\mathtt{DIQ}\,26^{\circ}), reproducing the actual
short-arc / long-arc ESQ split of the ring; the closed-form modular composition
of Sec.7uses these four-element per-quadrant maps.
The element layout of the three models over one90∘90^{\circ}quadrant
cell is shown in Fig.1.Figure 1:Element layout of the three ring models over one90∘90^{\circ}quadrant cell: the combined-function dipole-and-ESQ element𝙳𝙸𝚀\mathtt{DIQ}(gray) and the homogeneous magnetic dipole𝙳𝙸\mathtt{DI}(white).𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}is a single360∘360^{\circ}𝙳𝙸𝚀\mathtt{DIQ}(here90∘90^{\circ}over one cell) with the ESQ
inhomogeneity azimuthally averaged;𝙳𝙸𝙴𝚀​_​𝙾𝙽\mathtt{DIEQ\_ON}lumps the
quadrant ESQ into one43∘43^{\circ}𝙳𝙸𝚀\mathtt{DIQ};𝙳𝙸𝙴𝚀\mathtt{DIEQ}resolves the true short/long ESQ split. The𝙳𝙸𝚀\mathtt{DIQ}gray
level is a schematic normalization, scaled inversely with the
total𝙳𝙸𝚀\mathtt{DIQ}arc so that the apparent focusing strength
(gray level×\timesarc) is visually comparable across the three
models rather than tracking arc length alone;𝙳𝙸\mathtt{DI}sections are white. The residual differences between the models
are quantified in Sec.7.Figure 2:System diagram of the muong−2g{-}2storage ring. The four
electrostatic quadrupole stations Q1–Q4 provide vertical focusing; the
fast and slow muon kickers (K1–K3) inject the beam onto the closed
orbit. (Adapted from Ref.\refciteg2PRAB21, CC BY 4.0.)

## 3Methodology

The Hamiltonian framework for arbitrary-order
charged-particle optical-element aberrations is laid out in
Ref.\refciteAIEP108book; the present formulation parallels its
application to curvilinear electrostatic elements in
Ref.\refciteESCPO10AIEP. The COSY INFINITY beamline coordinate
system(x,a,y,b,ℓ,δK)(x,a,y,b,\ell,\delta_{K})[1,10,2]is used throughout, witha=px/p0a=p_{x}/p_{0},b=py/p0b=p_{y}/p_{0}the canonical transverse
momenta normalised to the reference momentump0p_{0}, andδK=(K−K0)/K0\delta_{K}=(K-K_{0})/K_{0}the relative kinetic energy deviation. Vertical
chromaticity is taken in the momentum-based conventionξy=[∂νy/∂δp]δp=0,δp=(p−p0)/p0,\xi_{y}\;=\;\left[\partial\nu_{y}/\partial\delta_{p}\right]_{\delta_{p}=0},\qquad\delta_{p}=(p-p_{0})/p_{0},(2)

which is the convention used internally by the Muong−2g{-}2Experiment
analysis chain[12,20].
All chromaticities below are evaluated for the on-momentum-designed
lattice at the off-momentum dispersive closed orbit (fixed-lattice
convention); the alternative scaling convention, in which the lattice
is rescaled with momentum, gives a numerically and conceptually
different quantity that omits the dispersion-orbit-coupling contribution.
The conversion betweenδK\delta_{K}- andδp\delta_{p}-based chromaticities is
the exact factorξy(p)=ξy(K)⋅(1+γ0)/γ0\xi_{y}^{(p)}=\xi_{y}^{(K)}\cdot(1+\gamma_{0})/\gamma_{0},
which differs from unity by about3%3\%at the magic momentum.

We adopt the multiplicity-factorial aberration coefficient convention of
Ref.\refciteAIEP108book: for output coordinateziz_{i}and input monomialzj1k1​⋯​zjmkmz_{j_{1}}^{k_{1}}\cdots z_{j_{m}}^{k_{m}}with distinct coordinate indicesj1,…,jmj_{1},\ldots,j_{m}and multiplicitieskp≥1k_{p}\geq 1,(zi|zj1k1​⋯​zjmkm)=1k1!​⋯​km!​∂k1+⋯+kmℳ​(𝐳)i∂zj1k1​⋯​∂zjmkm|𝐳=0.\left(z_{i}|z_{j_{1}}^{k_{1}}\cdots z_{j_{m}}^{k_{m}}\right)\;=\;\frac{1}{k_{1}!\cdots k_{m}!}\;\frac{\partial^{k_{1}+\cdots+k_{m}}\mathcal{M}(\mathbf{z})_{i}}{\partial z_{j_{1}}^{k_{1}}\cdots\partial z_{j_{m}}^{k_{m}}}\bigg|_{\mathbf{z}=0}.(3)

Reference\refciteChromCPO11 derived the horizontal second-order
aberrations of the homogeneous magnetic dipole (𝙳𝙸\mathtt{DI}) and the
combined-function dipole-and-electrostatic-quadrupole element (𝙳𝙸𝚀\mathtt{DIQ})
used in the muong−2g{-}2ring via order-by-order perturbation of the
canonical equations of motion; the vertical second-order coefficients
were not derived there. The present work supplies them.

The Hamiltonian is expanded as a Taylor polynomial in the dynamical
variables,H=H2+H3+⋯,H=H_{2}+H_{3}+\cdots,(4)

where the constant termH0H_{0}is omitted because it does not enter the
equations of motion, and the first-order termH1H_{1}vanishes for an
expansion about the reference orbit. The quadratic partH2H_{2}governs
the linear motion; within each element its coefficients are constant, so
the linear mapLLis obtained by exponentiating the constant linear
generator, and the full-ring map follows by composition of the
per-element maps. The cubic partH3H_{3}drives the second-order map
through the aberration integralR2​(s)=L​(s)​∫0sL−1​(s′)​Q2​(s′,𝐳lin​(s′))​𝑑s′,R_{2}(s)\;=\;L(s)\,\int_{0}^{s}L^{-1}(s^{\prime})\,Q_{2}\bigl(s^{\prime},\mathbf{z}_{\mathrm{lin}}(s^{\prime})\bigr)\,ds^{\prime},(5)

withQ2Q_{2}the second-order driving evaluated on the linear trajectory𝐳lin​(s)=L​(s)​𝐳0\mathbf{z}_{\mathrm{lin}}(s)=L(s)\,\mathbf{z}_{0}.
The curvilinear(1+h​x)(1{+}hx)factor inHHalready encodes the
Frenet–Serret rotating reference frame, so no additional Coriolis or
centripetal term is introduced when expanding about the design orbit.

A Wolfram Language implementation of the order-by-order procedure of
Refs.\refciteAIEP108book,ESCPO10AIEP generates the5×205{\times}20second-order aberration coefficients for𝙳𝙸\mathtt{DI}and𝙳𝙸𝚀\mathtt{DIQ}in the COSY INFINITY beamline coordinates. Its horizontal
subset reproduces all 27 coefficients of Ref.\refciteChromCPO11 underFullSimplify; the vertical(y,b)(y,b)-row coefficients are obtained from the same
pipeline. Algorithm1summarises the procedure; the COSY INFINITY DA validation program
is shown in Listing3.Algorithm 1Order-by-order Hamiltonian aberration computation, as
implemented for the muong−2g{-}2ring elements. Coefficients are returned
in the multiplicity-factorial convention of Eq.3.0:HamiltonianH​(𝐳;s)H(\mathbf{z};s)in curvilinear coordinates𝐳=(x,a,y,b,δK)\mathbf{z}=(x,a,y,b,\delta_{K})(the longitudinalℓ\ellcoordinate
of the full COSY INFINITY system is omitted from𝐳\mathbf{z}because the
ring is time-independent (no RF cavities or other time-varying elements),
so the transverse motion is independent ofℓ\ell); element arc lengths0s_{0}; desired
truncation orderNN(hereN=2N=2).0:Aberration table𝒞={(zi,m,ci,m)}\mathcal{C}=\{(z_{i},m,c_{i,m})\}for all
output coordinatesziz_{i}and input monomialsmmup to total orderNN.1:ExpandH=H2+H3+…H=H_{2}+H_{3}+\ldotsas a Taylor polynomial in𝐳\mathbf{z}.{H2H_{2}generates the linear map}2:Form linear generatorA2A_{2}fromH2H_{2}via Hamilton’s equations;
solveL′​(s)=A2​L​(s)L^{\prime}(s)=A_{2}L(s),L​(0)=IL(0)=I, by matrix exponential.3:Substitute𝐳lin​(s′)=L​(s′)​𝐳0\mathbf{z}_{\mathrm{lin}}(s^{\prime})=L(s^{\prime})\mathbf{z}_{0}into
theH3H_{3}-driven equations of motion to obtain the second-order drivingQ2​(s′,𝐳0)Q_{2}(s^{\prime},\mathbf{z}_{0}).4:fork=2k=2toNNdo5:SolveRk​(s0)=L​(s0)​∫0s0L−1​(s′)​Qk​(s′,𝐳lin​(s′))​𝑑s′R_{k}(s_{0})=L(s_{0})\int_{0}^{s_{0}}L^{-1}(s^{\prime})\,Q_{k}(s^{\prime},\mathbf{z}_{\mathrm{lin}}(s^{\prime}))\,ds^{\prime}symbolically.6:Read(zi|m)(z_{i}|m)as the coefficient of∏zjlkl\prod z_{j_{l}}^{k_{l}}in theii-th component ofL​𝐳0+RkL\,\mathbf{z}_{0}+R_{k}, divided by the
multiplicity factorial∏vl!\prod v_{l}!{Eq.3}7:end for8:return𝒞\mathcal{C}.⬇PROCEDUREG2RING;DIG2ANGML;EQG2ANGES;DIG2ANGMS;EQG2ANGEL;DIG2ANGML;EQG2ANGES;DIG2ANGMS;EQG2ANGEL;DIG2ANGML;EQG2ANGES;DIG2ANGMS;EQG2ANGEL;DIG2ANGML;EQG2ANGES;DIG2ANGMS;EQG2ANGEL;ENDPROCEDURE;LOOPIV1NV;VE0:=VARR(IV);INO:=3;IND:=2;IFR:=0;OVINOIND1;WSETDE;RPMPMU*PARA(1)MMU1;UMG2MODELIFR;G2RING;CONO;TPMU;WRITE6’CSV:’&S(VE0)&’’&S(CONS(MU(1)))&’’&S(CONS(MU(2)))&’’&S(CONS(DER(5,MU(1))))&’’&S(CONS(DER(5,MU(2))));ENDLOOP;\@makecaption

Listing 1COSY INFINITY DA program for the modular muong−2g{-}2ring (excerpt fromsweep_v.fox, adapted from G2run-chrom by K. Makino, 2023). For each ESQ voltage in the sweep, the procedure builds the four-fold quadrant lattice (G2RING:47∘47^{\circ}𝙳𝙸\mathtt{DI},13∘13^{\circ}𝙳𝙸𝚀\mathtt{DIQ},4∘4^{\circ}𝙳𝙸\mathtt{DI},26∘26^{\circ}𝙳𝙸𝚀\mathtt{DIQ}per quadrant), finds the closed orbit, prints the one-turn map, and extracts the linear chromaticities∂νx/∂δp\partial\nu_{x}/\partial\delta_{p}and∂νy/∂δp\partial\nu_{y}/\partial\delta_{p}via the COSY INFINITY differential operatorDER(5, MU(k)).

## 4Vertical Aberrations of𝙳𝙸\mathtt{DI}and𝙳𝙸𝚀\mathtt{DIQ}

The dimensionless ESQ field indexnnis defined relative to the
magnetic rigidity,n=E~y′​R0/(β0​c​B0),n=\tilde{E}^{\prime}_{y}\,R_{0}/(\beta_{0}cB_{0}),(6)

withE~y′\tilde{E}^{\prime}_{y}the ESQ-region transverse electric-field gradient
andB0B_{0}the bending magnetic field;n>0n>0in the muong−2g{-}2vertical-focusing ESQ polarity. Across theVESQ∈[10,26]​kVV_{\mathrm{ESQ}}\in[10,26]\,\mathrm{kV}sweep used in
this paper, the local ESQ field indexnnranges over0.13≲n≲0.340.13\lesssim n\lesssim 0.34, while the ring-average value⟨n⟩=1330​n\langle n\rangle=\tfrac{13}{30}\,nthat sets the continuous-ring vertical
tune (Sec.5) ranges over0.06≲⟨n⟩≲0.150.06\lesssim\langle n\rangle\lesssim 0.15, comfortably within the
half-integer-stable interval0<⟨n⟩<1/40<\langle n\rangle<1/4(vertical ring
tuneνy=⟨n⟩<1/2\nu_{y}=\sqrt{\langle n\rangle}<1/2).

The𝙳𝙸𝚀\mathtt{DIQ}electrostatic-quadrupole main field carries
higher-order transverse multipoles beyond the quadrupole. For the
muong−2g{-}2ESQ these were obtained from an OPERA field
map[16,15,21]; we subsequently computed them to
high order by conformal mapping[17,19],
which is fully Maxwellian and free of the near-field discretisation
error (typically0.10.1–1%1\%) of finite-element solvers. Their
detailed treatment is given in the horizontal-counterpart
work[18], where
the full multipole set is found to shift the storage-ring observables
only at the∼10​ppb{\sim}10\,\mathrm{ppb}level. This field content is
inert for the present result: the ESQ has quadrupole symmetry, so
its allowed transverse harmonics arem=2,6,10,…m=2,6,10,\ldots, and a2​m2m-pole feeds an effective quadrupole through the off-momentum
orbitx≈[R0/(1−n)]​δpx\approx[R_{0}/(1-n)]\,\delta_{p}only at orderδpm−2\delta_{p}^{\,m-2}; the
higher ESQ multipoles therefore first enter atξy(3)\xi_{y}^{(3)}(the1212-pole,m=6m=6) and leave the linear chromaticityξy(0)\xi_{y}^{(0)}exactly determined by the quadrupole component, while the∼10​ppb{\sim}10\,\mathrm{ppb}full-field effect is a tracking-level
correction outside the scope of the closed-form derivation.

The analytic derivation in this paper uses the hard-edge model of the
combined-function elements (COSY INFINITY’s𝙵𝚁​0\mathtt{FR}\ \mathtt{0}mode[3,1]), in which the field makes a
sharp transition from full strength to zero at the physical electrode
edge. In the electrostatic case, surface-charge concentrations near the
electrode ends make the effective field longer than the physical
electrode. The Effective Field Boundary (EFB) accounts for this by
defining a beam-physics-based cutoff at which a sharp transition
reproduces the integrated effect of the actual continuous fringe field.
For the muong−2g{-}2𝙳𝙸𝚀\mathtt{DIQ}quadrupole the EFB was previously
obtained[17,19]by integrating the falloff
of the quadrupole strengthM2,2M_{2,2}computed from an OPERA field
map[16,15,21],
giving an outward shift ofzEFB=1.22​cmz_{\mathrm{EFB}}=1.22\,\mathrm{cm}per
electrode edge (against a5​cm5\,\mathrm{cm}aperture); this lengthens
each quadrupole by∼2.44​cm{\sim}\,2.44\,\mathrm{cm}and increases the ESQ
azimuthal coverage of the ring by∼1%{\sim}\,1\%. The realistic falloff
is represented by an Enge functionF​(z)=11+exp⁡(a1+a2​(z/D)+⋯+a6​(z/D)6),F(z)=\frac{1}{1+\exp\!\left(a_{1}+a_{2}(z/D)+\cdots+a_{6}(z/D)^{6}\right)},(7)

wherez=0z=0at the EFB (positive outside, negative inside),DDis
the full aperture, and the coefficientsaja_{j}were fitted to the quadrupole
fringe-field falloff computed by the COULOMB boundary-element
solver[9,17,19]. The fringe-field
shift ofξy(p)\xi_{y}^{(p)}is sub-percent at the muong−2g{-}2operating
point. The
numerical validation in Sec.7additionally compares
the hard-edge result against the COSY INFINITY𝙵𝚁​3\mathtt{FR}\ \mathtt{3}treatment (Enge-function fringe field) with the EFB extension, using
the same Enge coefficients and EFB calibration as the
horizontal-counterpart work[18].
The vertical and horizontal wavenumbers in𝙳𝙸𝚀\mathtt{DIQ}areϑy=h​n,ϑx=h​1−n,\vartheta_{y}=h\sqrt{n},\qquad\vartheta_{x}=h\sqrt{1-n},(8)

withh=1/R0h=1/R_{0}the dipole curvature;ϑx\vartheta_{x}is reserved for
cross-references to the horizontal counterpart[18]. The convention of
Eq.3(multiplicity-factorial weights) is applied throughout.

## 4.1First-Order Aberrations

Homogeneous magnetic dipole𝙳𝙸\mathtt{DI}:vertical motion is a
pure drift, and the first-order(y|⋅)(y|\cdot)and(b|⋅)(b|\cdot)aberrations are(y|x)\displaystyle\left(y|x\right)=(y|a)=(y|δK)=0,\displaystyle=\left(y|a\right)=\left(y|\delta_{K}\right)=0,(y|y)\displaystyle\qquad\left(y|y\right)=1,(y|b)=s,\displaystyle=1,\quad\left(y|b\right)=s,(9a)(b|x)\displaystyle\left(b|x\right)=(b|a)=(b|y)=(b|δK)=0,\displaystyle=\left(b|a\right)=\left(b|y\right)=\left(b|\delta_{K}\right)=0,(b|b)\displaystyle\qquad\left(b|b\right)=1.\displaystyle=1.(9b)

The horizontal first-order aberrations of𝙳𝙸\mathtt{DI}are given in
the horizontal-counterpart paper[18].

Combined-function quadrupole𝙳𝙸𝚀\mathtt{DIQ}:integrating the
linear vertical equation of motion under combined dipole curvaturehhand ESQ vertical-focusing strengthh​nh\sqrt{n}gives the
first-order(y|⋅)(y|\cdot)and(b|⋅)(b|\cdot)aberrations of𝙳𝙸𝚀\mathtt{DIQ}:(y|x)\displaystyle\left(y|x\right)=(y|a)=(y|δK)=0,\displaystyle=\left(y|a\right)=\left(y|\delta_{K}\right)=0,(10a)(y|y)\displaystyle\left(y|y\right)=cos⁡(ϑy​s),(y|b)=sin⁡(ϑy​s)ϑy,\displaystyle=\cos(\vartheta_{y}s),\qquad\left(y|b\right)=\frac{\sin(\vartheta_{y}s)}{\vartheta_{y}},(10b)(b|x)\displaystyle\left(b|x\right)=(b|a)=(b|δK)=0,\displaystyle=\left(b|a\right)=\left(b|\delta_{K}\right)=0,(10c)(b|y)\displaystyle\left(b|y\right)=−ϑy​sin⁡(ϑy​s),(b|b)=cos⁡(ϑy​s).\displaystyle=-\vartheta_{y}\sin(\vartheta_{y}s),\qquad\left(b|b\right)=\cos(\vartheta_{y}s).(10d)

The horizontal–vertical sub-blocks decouple at first order, and the
absence of vertical dispersion
((y|δK)=(b|δK)=0\left(y|\delta_{K}\right)=\left(b|\delta_{K}\right)=0)
follows from the bend plane being horizontal.

## 4.2Second-Order Aberrations

The aberration integral (5) evaluated to second
order with the curvilinear (Maxwellian) expansion of the ideal𝙳𝙸𝚀\mathtt{DIQ}quadrupole field yields the second-order(y|⋅)(y|\cdot)and(b|⋅)(b|\cdot)aberrations. Because the lattice is symmetric under midplane
reflection,(x,a,y,b,δK)→(x,a,−y,−b,δK)(x,a,y,b,\delta_{K})\to(x,a,-y,-b,\delta_{K})(horizontal bend plane, reference orbit in the midplane, no skew
or solenoidal coupling), the vertical coordinatesyyandbbare odd
functions of the vertical inputs; every second-order(y|⋅)(y|\cdot)aberration with zero or two vertical input factors therefore vanishes:(y|x​x)=(y|x​a)=(y|a​a)=(y|y​y)=(y|y​b)=(y|b​b)=0,\displaystyle\left(y|xx\right)=\left(y|xa\right)=\left(y|aa\right)=\left(y|yy\right)=\left(y|yb\right)=\left(y|bb\right)=0,(11)(y|x​δK)=(y|a​δK)=(y|δK​δK)=0,\displaystyle\left(y|x\delta_{K}\right)=\left(y|a\delta_{K}\right)=\left(y|\delta_{K}\delta_{K}\right)=0,

and the same identities hold for the(b|⋅)(b|\cdot)row,(b|m)=0\left(b|m\right)=0for eachmmlisted in
Eq.11. The remaining six second-order(y|⋅)(y|\cdot)and six(b|⋅)(b|\cdot)coefficients are non-zero.

𝙳𝙸\mathtt{DI}second-order vertical aberrations:settingn→0n\to 0in the𝙳𝙸𝚀\mathtt{DIQ}formulas below collapses all𝙳𝙸𝚀\mathtt{DIQ}second-order(b|⋅)(b|\cdot)coefficients and most of the(y|⋅)(y|\cdot)coefficients to zero. The only non-vanishing𝙳𝙸\mathtt{DI}second-order vertical aberrations are(y|b​x)\displaystyle\left(y|b\,x\right)=sin⁡(h​s),\displaystyle=\sin(hs),(y|b​a)\displaystyle\qquad\left(y|b\,a\right)=1−cos⁡(h​s)h,\displaystyle=\frac{1-\cos(hs)}{h},(12a)(y|b​δK)\displaystyle\left(y|b\,\delta_{K}\right)=−γ0γ0+1​sin⁡(h​s)h;\displaystyle=-\frac{\gamma_{0}}{\gamma_{0}+1}\,\frac{\sin(hs)}{h};(12b)

the remaining twelve(y|⋅)(y|\cdot)coefficients of𝙳𝙸\mathtt{DI}[i.e., those listed in Eq.11, together with(y|x​y)\left(y|xy\right),(y|a​y)\left(y|ay\right),(y|y​δK)\left(y|y\delta_{K}\right)]
all vanish, as do all fifteen second-order(b|⋅)\left(b|\cdot\right)entries of𝙳𝙸\mathtt{DI}.

𝙳𝙸𝚀\mathtt{DIQ}second-order vertical aberrations:the eight
horizontal–vertical mixed coefficients, generated by the(1+x/ρ)(1+x/\rho)Jacobian and the−2​h3​n​x​y-2h^{3}n\,xyterm inb˙\dot{b}from the curvilinear
ESQ Hamiltonian of the muong−2g{-}2combined-function element[18],
are(y|x​y)\displaystyle\left(y|xy\right)=h​[2​n​(1−n)​cos⁡(ϑy​s)​sin2⁡(ϑx​s/2)+(1−7​n)​sin⁡(ϑx​s)​sin⁡(ϑy​s)](5​n−1)​(1−n)/n,\displaystyle=\frac{h\bigl[\,2\sqrt{n(1-n)}\,\cos(\vartheta_{y}s)\sin^{2}(\vartheta_{x}s/2)+(1-7n)\sin(\vartheta_{x}s)\sin(\vartheta_{y}s)\,\bigr]}{(5n-1)\,\sqrt{(1-n)/n}},(13a)(y|x​b)\displaystyle\left(y|xb\right)=(7​n−1)​cos⁡(ϑy​s)​sin⁡(ϑx​s)/1−n−2​n​cos2⁡(ϑx​s/2)​sin⁡(ϑy​s)5​n−1,\displaystyle=\frac{(7n-1)\cos(\vartheta_{y}s)\sin(\vartheta_{x}s)/\sqrt{1-n}\;-\;2\sqrt{n}\,\cos^{2}(\vartheta_{x}s/2)\sin(\vartheta_{y}s)}{5n-1},(13b)(y|a​y)\displaystyle\left(y|ay\right)=1−n​n​cos⁡(ϑy​s)​sin⁡(ϑx​s)+n​[8​n−2+(1−7​n)​cos⁡(ϑx​s)]​sin⁡(ϑy​s)(n−1)​(5​n−1),\displaystyle=\frac{\sqrt{1-n}\,n\,\cos(\vartheta_{y}s)\sin(\vartheta_{x}s)+\sqrt{n}\,\bigl[\,8n-2+(1-7n)\cos(\vartheta_{x}s)\,\bigr]\sin(\vartheta_{y}s)}{(n-1)(5n-1)},(13c)(y|a​b)\displaystyle\left(y|ab\right)=−2​(1−7​n)​1−n​cos⁡(ϑy​s)​sin2⁡(ϑx​s/2)−(n−1)​n​sin⁡(ϑx​s)​sin⁡(ϑy​s)h​(1−n)3/2​(5​n−1),\displaystyle=-\frac{2(1-7n)\sqrt{1-n}\,\cos(\vartheta_{y}s)\sin^{2}(\vartheta_{x}s/2)-(n-1)\sqrt{n}\,\sin(\vartheta_{x}s)\sin(\vartheta_{y}s)}{h\,(1-n)^{3/2}(5n-1)},(13d)(b|x​y)\displaystyle\left(b|xy\right)=−h2​n​[2​(4​n−1)​cos⁡(ϑy​s)​sin⁡(ϑx​s)+n​(1−n)​(1+cos⁡(ϑx​s))​sin⁡(ϑy​s)]1−n​(5​n−1),\displaystyle=-\frac{h^{2}n\,\bigl[\,2(4n-1)\cos(\vartheta_{y}s)\sin(\vartheta_{x}s)+\sqrt{n(1-n)}\,\bigl(1+\cos(\vartheta_{x}s)\bigr)\sin(\vartheta_{y}s)\,\bigr]}{\sqrt{1-n}\,(5n-1)},(13e)(b|x​b)\displaystyle\left(b|xb\right)=−2​h​[n​(1−n)​cos⁡(ϑy​s)​sin2⁡(ϑx​s/2)+(4​n−1)​sin⁡(ϑx​s)​sin⁡(ϑy​s)](5​n−1)​(1−n)/n,\displaystyle=-\frac{2h\,\bigl[\,\sqrt{n(1-n)}\,\cos(\vartheta_{y}s)\sin^{2}(\vartheta_{x}s/2)+(4n-1)\sin(\vartheta_{x}s)\sin(\vartheta_{y}s)\,\bigr]}{(5n-1)\,\sqrt{(1-n)/n}},(13f)(b|a​y)\displaystyle\left(b|ay\right)=h​n​[4​(4​n−1)​cos⁡(ϑy​s)​sin2⁡(ϑx​s/2)+n​(1−n)​sin⁡(ϑx​s)​sin⁡(ϑy​s)](1−n)​(1−5​n),\displaystyle=\frac{hn\,\bigl[\,4(4n-1)\cos(\vartheta_{y}s)\sin^{2}(\vartheta_{x}s/2)+\sqrt{n(1-n)}\,\sin(\vartheta_{x}s)\sin(\vartheta_{y}s)\,\bigr]}{(1-n)(1-5n)},(13g)(b|a​b)\displaystyle\left(b|ab\right)=(n−1)​n​cos⁡(ϑy​s)​sin⁡(ϑx​s)+n​(1−n)​[7​n−1+(2−8​n)​cos⁡(ϑx​s)]​sin⁡(ϑy​s)(1−5​n)​(1−n)3/2.\displaystyle=\frac{(n-1)n\,\cos(\vartheta_{y}s)\sin(\vartheta_{x}s)+\sqrt{n(1-n)}\,\bigl[\,7n-1+(2-8n)\cos(\vartheta_{x}s)\,\bigr]\sin(\vartheta_{y}s)}{(1-5n)(1-n)^{3/2}}.(13h)

In the composite modular-ring map, the first-order horizontal dispersion
orbitx=1Dx​δKx=_{1}D_{x}\,\delta_{K}(using the equality-at-order-nnrelation
of Ref.\refciteAIEP108book:f=ngf=_{n}giffffandggagree at the origin
through ordernn) converts(y|x​y)(y|xy)and(y|x​b)(y|xb)into effective(y|y​δK)(y|y\delta_{K})and(y|b​δK)(y|b\delta_{K})contributions, making these mixed entries essential
to the vertical chromaticity; the higher-order dispersion enters only
atξy(j≥1)\xi_{y}^{(j\geq 1)}. The four
direct chromatic(⋅|⋅δK)(\cdot|\cdot\,\delta_{K})coefficients depend on both
wavenumbers through the curvilinear coupling; writing𝒬​(s)\displaystyle\mathcal{Q}(s)=n​(1−n)​h​s​[5​n2−6​n+1+γ02​(5​n2+9​n−2)],\displaystyle=\sqrt{n(1-n)}\,hs\left[5n^{2}-6n+1+\gamma_{0}^{2}(5n^{2}+9n-2)\right],(14a)𝒫7​(s)\displaystyle\mathcal{P}_{7}(s)=𝒬​(s)+2​γ02​(1−7​n)​n​sin⁡(ϑx​s),\displaystyle=\mathcal{Q}(s)+2\gamma_{0}^{2}(1-7n)\sqrt{n}\,\sin(\vartheta_{x}s),(14b)𝒫4​(s)\displaystyle\mathcal{P}_{4}(s)=𝒬​(s)+4​γ02​(1−4​n)​n​sin⁡(ϑx​s),\displaystyle=\mathcal{Q}(s)+4\gamma_{0}^{2}(1-4n)\sqrt{n}\,\sin(\vartheta_{x}s),(14c)

they are(y|y​δK)\displaystyle\left(y|y\,\delta_{K}\right)=2​sin⁡(ϑy​s)​𝒫7/1−n−4​γ02​n​(cos⁡(ϑx​s)−1)​cos⁡(ϑy​s)4​γ0​(γ0+1)​(n−1)​(5​n−1),\displaystyle=\frac{2\sin(\vartheta_{y}s)\,\mathcal{P}_{7}/\sqrt{1-n}-4\gamma_{0}^{2}n\bigl(\cos(\vartheta_{x}s)-1\bigr)\cos(\vartheta_{y}s)}{4\gamma_{0}(\gamma_{0}+1)(n-1)(5n-1)},(15a)(b|b​δK)\displaystyle\left(b|b\,\delta_{K}\right)=2​sin⁡(ϑy​s)​𝒫4/1−n+4​γ02​n​(cos⁡(ϑx​s)−1)​cos⁡(ϑy​s)4​γ0​(γ0+1)​(n−1)​(5​n−1),\displaystyle=\frac{2\sin(\vartheta_{y}s)\,\mathcal{P}_{4}/\sqrt{1-n}+4\gamma_{0}^{2}n\bigl(\cos(\vartheta_{x}s)-1\bigr)\cos(\vartheta_{y}s)}{4\gamma_{0}(\gamma_{0}+1)(n-1)(5n-1)},(15b)(y|b​δK)\displaystyle\left(y|b\,\delta_{K}\right)=−n2​γ0​(γ0+1)​h​[(1−n)​n]3/2​(5​n−1)[1−nsin(ϑys)(5n2−6n+1\displaystyle=\frac{-n}{2\gamma_{0}(\gamma_{0}+1)\,h\,[(1-n)n]^{3/2}(5n-1)}\Bigl[\sqrt{1-n}\,\sin(\vartheta_{y}s)\bigl(5n^{2}-6n+1+γ02((9−5n)n−2)−2γ02ncos(ϑxs))−cos(ϑys)𝒫7],\displaystyle\quad{}+\gamma_{0}^{2}\bigl((9-5n)n-2\bigr)-2\gamma_{0}^{2}n\cos(\vartheta_{x}s)\bigr)-\cos(\vartheta_{y}s)\,\mathcal{P}_{7}\Bigr],(15c)(b|y​δK)\displaystyle\left(b|y\,\delta_{K}\right)=ϑy4​γ0​(γ0+1)​(n−1)​(5​n−1)[2​cos⁡(ϑy​s)​𝒫41−n\displaystyle=\frac{\vartheta_{y}}{4\gamma_{0}(\gamma_{0}+1)(n-1)(5n-1)}\Bigl[\frac{2\cos(\vartheta_{y}s)\,\mathcal{P}_{4}}{\sqrt{1-n}}−2sin(ϑys)(2γ02ncos(ϑxs)+γ02(n(5n−9)+2)+(6−5n)n−1)].\displaystyle\quad{}-2\sin(\vartheta_{y}s)\bigl(2\gamma_{0}^{2}n\cos(\vartheta_{x}s)+\gamma_{0}^{2}\bigl(n(5n-9)+2\bigr)+(6-5n)n-1\bigr)\Bigr].(15d)

The twelve non-zero coefficients listed in
Listings7.1and7.1, which are geometric and
carry no relativistic kinematic factor, agree with COSY INFINITY DA
at the double-precision floor (|Δ|≲10−15|\Delta|\lesssim 10^{-15}) at the
nominal muong−2g{-}2operating point (𝙳𝙸𝚀​26∘\mathtt{DIQ}\,26^{\circ},VESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}) when the analytic expressions are
evaluated at COSY INFINITY’s exact effective field indexn=0.23816484010681533,n=0.23816484010681533,(16)

paralleling the geometric rows of the
horizontal listings[18]; theγ0\gamma_{0}-dependent
chromatic coefficients of Eq.15are
discussed below.

Consistency check.The bare-dipole limitn→0n\to 0of
Eq.15recovers the𝙳𝙸\mathtt{DI}second-order
chromatic coefficient(y|b​δK)𝙳𝙸=−[γ0/(γ0+1)]​sin⁡(h​s)/h(y|b\delta_{K})_{\mathtt{DI}}=-[\gamma_{0}/(\gamma_{0}+1)]\sin(hs)/hof Eq.12(its further straight-drift limith→0h\to 0giving−[γ0/(γ0+1)]​s-[\gamma_{0}/(\gamma_{0}+1)]\,s), and the four-column Wronskian∂δK[(y|y)​(b|b)−(y|b)​(b|y)]=0\partial_{\delta_{K}}[(y|y)(b|b)-(y|b)(b|y)]=0holds
to first order inδK\delta_{K}, confirming symplecticity.

## 5Closed-Form Result for the Continuous-Ring Model

For the continuous ring𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}, a single360∘360^{\circ}𝙳𝙸𝚀\mathtt{DIQ}element in which the ring-average inhomogeneity⟨n⟩\langle n\ranglereplaces the
modular ESQ structure, the vertical tune satisfies(y|y)+(b|b)=2​cos⁡(2​π​νy)(y|y)+(b|b)=2\cos(2\pi\nu_{y}). Differentiating with respect toδp\delta_{p}at the periodic
dispersion orbit, where(y|δK)=(b|δK)=0(y|\delta_{K})=(b|\delta_{K})=0(no vertical
dispersion in the bend plane), gives the linear vertical chromaticity directly
from the second-order chromatic coefficients of the one-turn map:ξy=(y|y​δK)+(b|b​δK)4​π​sin⁡(2​π​νy),\xi_{y}\;=\;\frac{(y|y\,\delta_{K})+(b|b\,\delta_{K})}{4\pi\,\sin(2\pi\nu_{y})},(17)

where the matrix elements are those of the composite one-turn map and the
overall normalisation matches the horizontal-counterpart treatment of
Ref.\refciteChromCPO11. The derivatived/d​δpd/d\delta_{p}in
Eq.17is taken about the dispersive closed orbitx=1Dx​δKx=_{1}D_{x}\,\delta_{K},
not about the on-momentum reference
orbitx=0x=0; evaluation at the latter removes the dispersion-orbit-coupling contribution carried by the mixed(y|x​y)(y|xy),(y|x​b)(y|xb),(b|x​y)(b|xy),(b|x​b)(b|xb)aberrations of
Eq.13. The dispersion orbitx=1Dx​δKx=_{1}D_{x}\,\delta_{K}contributes to the effective second-order chromatic coefficients via the
mixed entries of Eq.13, as discussed below.
Evaluating Eq.17with the𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}linear
map of Eq.10and the chromatic and mixed second-order
aberrations of Eqs.13and15ats=2​π​R0s=2\pi R_{0},n→⟨n⟩n\to\langle n\rangle, yieldsξy(p)​(2​π,n)=sgn​(sin⁡(2​π​n))​n​(γ02​(n+2)+n−1)2​γ02​(1−n),\xi_{y}^{(p)}(2\pi,n)\;=\;\mathrm{sgn}\!\left(\sin(2\pi\sqrt{n})\right)\,\frac{\sqrt{n}\,\bigl(\gamma_{0}^{2}(n+2)+n-1\bigr)}{2\,\gamma_{0}^{2}\,(1-n)}\,,(18)

in direct functional correspondence with the horizontal counterpart[18],ξx(p)​(2​π,n)=sgn​(sin⁡(2​π​1−n))​n​(γ02​(n+2)+n−1)2​γ02​(1−n)3/2.\xi_{x}^{(p)}(2\pi,n)\;=\;\mathrm{sgn}\!\left(\sin(2\pi\sqrt{1-n})\right)\,\frac{n\,\bigl(\gamma_{0}^{2}(n+2)+n-1\bigr)}{2\,\gamma_{0}^{2}\,(1-n)^{3/2}}.(19)

The two formulas share the same kinematic factor(γ02​(n+2)+n−1)/γ02(\gamma_{0}^{2}(n+2)+n-1)/\gamma_{0}^{2}but differ in their dependence on the
field indexnn, reflecting the distinct roles of horizontal curvature-based
focusing (strength∝1−n\propto\sqrt{1-n}) and vertical electrostatic focusing
(strength∝n\propto\sqrt{n}). Taking absolute values and dividing
Eq.18by Eq.19, the kinematic
factor and theγ0\gamma_{0}-dependence cancel, giving|ξy(p)​(2​π,n)||ξx(p)​(2​π,n)|=n/(1−n)n/(1−n)3/2=1−nn=νxνy,\frac{|\xi_{y}^{(p)}(2\pi,n)|}{|\xi_{x}^{(p)}(2\pi,n)|}\;=\;\frac{\sqrt{n}/(1-n)}{n/(1-n)^{3/2}}\;=\;\sqrt{\frac{1-n}{n}}\;=\;\frac{\nu_{x}}{\nu_{y}},(20)

i.e. the inverse of the linear-tune ratio. Vertical chromaticity is
amplified relative to horizontal in proportion to how weakly the vertical
plane is focused: at⟨n⟩≈0.103\langle n\rangle\approx 0.103,νx/νy≈2.95\nu_{x}/\nu_{y}\approx 2.95, so|ξy|≈3​|ξx||\xi_{y}|\approx 3\,|\xi_{x}|, with
opposite sign becausesgn​(sin⁡(2​π​n))=+1\mathrm{sgn}(\sin(2\pi\sqrt{n}))=+1whilesgn​(sin⁡(2​π​1−n))=−1\mathrm{sgn}(\sin(2\pi\sqrt{1-n}))=-1throughout the operating range0<n<1/40<n<1/4. The chromatic effect is delivered to the vertical
sub-block through the off-momentum closed orbit. The dispersion orbit
isx=1Dx​δKx=_{1}D_{x}\,\delta_{K}, withDx=[γ0/(γ0+1)]​R0/(1−n)D_{x}=[\gamma_{0}/(\gamma_{0}+1)]\,R_{0}/(1-n)for the continuous-ring𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}model, the momentum dispersionR0/(1−n)R_{0}/(1-n)rescaled to the kinetic-energy variableδK\delta_{K}used here. For the modular ring the same first-orderδK\delta_{K}structure holds, with the coefficient renormalised by the
modular geometry. Composing the per-element augmented horizontal maps
over a𝙳𝙸𝙴𝚀\mathtt{DIEQ}quadrant and imposing periodicity gives the
modular first-order dispersion in closed matrix-product form,Dx(1)=[(I2−Mq,h)−1​𝐝q]1D_{x}^{(1)}=\bigl[\,(I_{2}-M_{q,h})^{-1}\,\mathbf{d}_{q}\,\bigr]_{1}, whereMqM_{q}is the product of the four per-element maps of a quadrant,Mq,hM_{q,h}its(x,a)(x,a)block, and𝐝q\mathbf{d}_{q}itsδK\delta_{K}column;
the four-fold symmetry makes this quadrant-periodic value equal to the
full-ring one. AtVESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}it matches the COSY
INFINITY one-turn map at the double-precision floor
(|Δ|≲10−15|\Delta|\lesssim 10^{-15}) and renormalisesDxD_{x}by
only0.19%0.19\%relative to its continuous-ring value (a
convention-independent ratio). The leading vertical chromaticityξy(0)\xi_{y}^{(0)}depends onDxD_{x}only through this first-order coefficient,
so the modular renormalisation entersξy(0)\xi_{y}^{(0)}only at this0.19%0.19\%level. The ring
dispersion is treated in more detail, in the smooth-ring approximation,
in Ref.\refciteg2PRAB25.
This dispersion converts the second-order cross-coupling aberrations(y|x​y)(y|xy),(y|x​b)(y|xb),(b|x​y)(b|xy),(b|x​b)(b|xb)of𝙳𝙸𝚀\mathtt{DIQ}into effective(y|y​δK)(y|y\delta_{K}),(y|b​δK)(y|b\delta_{K}),(b|y​δK)(b|y\delta_{K}),(b|b​δK)(b|b\delta_{K})contributions in the composite
map. These cross-coupling aberrations originate in the(1+x/ρ)(1+x/\rho)Jacobian of the curvilinear ESQ Hamiltonian and its−2​h3​n​x​y-2h^{3}n\,xyterm inb˙\dot{b}.
The simplified(y,b)(y,b)-only derivation, which setsx=0x=0throughout, gives both an incorrect sign and an incorrect magnitude.

For the𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}continuous ring, the local ESQ field indexnESQn_{\mathrm{ESQ}}is replaced by the ring-average⟨n⟩=13∘+26∘90∘​nESQ=1330​nESQ\langle n\rangle=\tfrac{13^{\circ}+26^{\circ}}{90^{\circ}}\,n_{\mathrm{ESQ}}=\tfrac{13}{30}\,n_{\mathrm{ESQ}}, the prefactor being the azimuthal
fill-fraction of the ESQ arcs within one90∘90^{\circ}quadrant (the same
convention as the horizontal counterpart[18]). At the
nominal Run 3–6 voltageVESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}this gives⟨n⟩=0.1032047640462866,\langle n\rangle=0.1032047640462866,(21)

written⟨n⟩≈0.103\langle n\rangle\approx 0.103below.
Equation18is then evaluated atn→⟨n⟩n\to\langle n\rangle,
and the corresponding kinetic-energy-based form follows fromξy(K)=ξy(p)⋅γ0/(γ0+1)\xi_{y}^{(K)}=\xi_{y}^{(p)}\cdot\gamma_{0}/(\gamma_{0}+1).

## 6Limits and Consistency Checks

Ultrarelativistic limit.Asγ0→∞\gamma_{0}\to\inftythe
kinematic factor of Eq.18tends ton+2n+2, and the
closed form reduces toξy(p)​(2​π,n)|γ0→∞=sgn​(sin⁡(2​π​n))​n​(n+2)2​(1−n).\xi_{y}^{(p)}(2\pi,n)\big|_{\gamma_{0}\to\infty}\;=\;\mathrm{sgn}\!\left(\sin(2\pi\sqrt{n})\right)\,\frac{\sqrt{n}\,(n+2)}{2(1-n)}.(22)

The deviation from this limit is, in absolute terms,ξy(p)​(2​π,n)−ξy(p)​(2​π,n)|γ0→∞=−sgn​(sin⁡(2​π​n))​n2​γ02,\xi_{y}^{(p)}(2\pi,n)-\xi_{y}^{(p)}(2\pi,n)\big|_{\gamma_{0}\to\infty}=-\mathrm{sgn}\!\left(\sin(2\pi\sqrt{n})\right)\,\frac{\sqrt{n}}{2\gamma_{0}^{2}},(23)

and at theg−2g{-}2magic momentum (γ0≈29.30\gamma_{0}\approx 29.30,⟨n⟩≈0.103\langle n\rangle\approx 0.103) is of order⟨n⟩/(2​γ02)≈2×10−4\sqrt{\langle n\rangle}/(2\gamma_{0}^{2})\approx 2\times 10^{-4}, i.e. a∼0.05%\sim 0.05\%relative correction. Theγ0−2\gamma_{0}^{-2}term is small but non-negligible for the analytic form,
paralleling the corresponding horizontal discussion[18].

Sign and stability.For0<n<10<n<1, the denominator(1−n)>0(1-n)>0and the kinematic factorγ02​(n+2)+n−1>0\gamma_{0}^{2}(n+2)+n-1>0. The sign ofξy(p)\xi_{y}^{(p)}is therefore set bysgn​(sin⁡(2​π​n))\mathrm{sgn}(\sin(2\pi\sqrt{n})), which equals+1+1throughout the half-integer-stable range0<n<1/40<n<1/4(νy=n<1/2\nu_{y}=\sqrt{n}<1/2) and reverses acrossn=1/4n=1/4where the vertical tune crosses the half-integer resonance. The muong−2g{-}2nominal Run 3–6 operating point (⟨n⟩≈0.103\langle n\rangle\approx 0.103,2​π​n≈2.0182\pi\sqrt{n}\approx 2.018) lies well inside thesgn=+1\mathrm{sgn}=+1branch and yields the positive vertical chromaticity reported by COSY INFINITY for the ring. This contrasts with the horizontal case (Eq.19), wheresin⁡(2​π​1−n)<0\sin(2\pi\sqrt{1-n})<0for the samennandξx(p)\xi_{x}^{(p)}is negative.

Vanishing voltage / field index.Asn→0n\to 0,ξy→0\xi_{y}\to 0(no vertical focusing) and the vertical tuneνy=n→0\nu_{y}=\sqrt{n}\to 0approaches the integer-resonance boundary. Asn→1n\to 1, the prefactor(1−n)(1-n)in Eq.18drives a divergence corresponding toνx=1−n→0\nu_{x}=\sqrt{1-n}\to 0(loss of horizontal focusing); this is well outside the muong−2g{-}2operating range (⟨n⟩≈0.103\langle n\rangle\approx 0.103at the nominal voltage).

Bare-dipole field index.Reference\refciteChromCPO11 treats the casend=0n_{d}=0for the bare𝙳𝙸\mathtt{DI}field. A residualnd≠0n_{d}\neq 0slightly shifts the vertical focusing in both the𝙳𝙸\mathtt{DI}arcs and the ESQ sections; for theg−2g{-}2ringnd≲10−4n_{d}\lesssim 10^{-4}and the correction is below the systematic uncertainty floor.

## 7Numerical Validation

The analytic results of Sec.5and the per-element vertical
aberrations of Sec.4are validated against COSY INFINITY
DA numerics[10]across the three ring
models introduced in Sec.2: the continuous ring𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}, the simplified modular ring𝙳𝙸𝙴𝚀​_​𝙾𝙽\mathtt{DIEQ\_ON}(four
cells of𝙳𝙸​47∘+𝙳𝙸𝚀​43∘\mathtt{DI}\,47^{\circ}+\mathtt{DIQ}\,43^{\circ}), and the full
modular ring𝙳𝙸𝙴𝚀\mathtt{DIEQ}(four cells of𝙳𝙸​47∘+𝙳𝙸𝚀​13∘+𝙳𝙸​4∘+𝙳𝙸𝚀​26∘\mathtt{DI}\,47^{\circ}+\mathtt{DIQ}\,13^{\circ}+\mathtt{DI}\,4^{\circ}+\mathtt{DIQ}\,26^{\circ}).

## 7.1Per-Element Aberrations

Element-level vertical aberrations of𝙳𝙸𝚀\mathtt{DIQ}derived by the
order-by-order procedure of Sec.3are compared against
COSY INFINITY DA at the nominal Run 3–6 operating point of the muong−2g{-}2ring (𝙳𝙸𝚀​26∘\mathtt{DIQ}\,26^{\circ},VESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV},h=1/(7.112​m)h=1/(7.112\,\mathrm{m}),γ0\gamma_{0}from Eq.1, and the
COSY INFINITY internally computed effective field indexnnof
Eq.16). The ANALYTIC column lists values from the
closed-form expressions of Sec.4(and the full5×205{\times}20symbolic table generated as ancillary material); the
COSY INFINITY column shows the differential-algebraic transfer-map
output at the same reference parameters; the DIFF column is their
difference. The five EXPONENTS columns are the input-monomial
multiplicities in the coordinates(x,a,y,b,δK)(x,a,y,b,\delta_{K}).⬇(y|...)IANALYTICCOSYINFINITYDIFFORDEREXPONENTS10.97557843881433910.9755784388143393-1.11E-1610010023.20100811161010633.20100811161010594.44E-161000103-.1003765953673937E-01-.1003765953673937E-01-3.47E-182101004-.1453757360977295E-01-.1453757360977294E-01-5.20E-1820110050.42761410305780410.42761410305780382.78E-1621001060.69918907612735170.6991890761273519-2.22E-16201010(b|...)IANALYTICCOSYINFINITYDIFFORDEREXPONENTS1-.1507234847221572E-01-.1507234847221572E-011.73E-1810010020.97557843881433910.9755784388143393-1.11E-161000103-.4077869216179440E-02-.4077869216179440E-020.0E+002101004-.6667697789759871E-02-.6667697789759875E-023.47E-182011005-.9948884277916866E-02-.9948884277916863E-02-3.47E-182100106-.1814229593807335E-01-.1814229593807334E-01-1.39E-17201010\@makecaption

Listing 2Vertical aberrations of a𝙳𝙸𝚀​26∘\mathtt{DIQ}\,26^{\circ}element atVESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}, hard-edge model (FR 0). ANALYTIC values evaluated at COSY INFINITY’s internally computed effective field indexnnof Eq.16; residuals at the double-precision floor.

The mixed cross-coupling aberrations(b|x​b)(b|xb),(b|x​y)(b|xy),(b|a​y)(b|ay),(b|a​b)(b|ab)arise from the−2​h3​n​x​y-2h^{3}n\,xyterm inb˙\dot{b}generated by the curvilinear ESQ Hamiltonian.
They are correctly reproduced and are essential
to the final modular-ring chromaticity.
The displayed residuals are at the double-precision floor
(|Δ|≲10−15|\Delta|\lesssim 10^{-15}for all twelve listed coefficients,
none of which carry the relativistic kinematic factorγ0/(1+γ0)\gamma_{0}/(1+\gamma_{0})), paralleling the geometric, non-chromatic
rows of the horizontal per-element listings of
Ref.\refciteChromCPO11. Theγ0\gamma_{0}-dependent chromatic(⋅|⋅δK)(\cdot|\cdot\,\delta_{K})coefficients of
Eq.15are not listed here; they carry the
small difference between the analytic model and COSY INFINITY,
quantified for the continuous-ring closed form in Sec.5below, which is
exact within the analytic model and not a kinematic-factor
approximation. The analogous comparison at the short-arc𝙳𝙸𝚀​13∘\mathtt{DIQ}\,13^{\circ}element of the full modular𝙳𝙸𝙴𝚀\mathtt{DIEQ}ring is shown in Listing7.1.⬇(y|...)IANALYTICCOSYINFINITYDIFFORDEREXPONENTS10.99387585714070430.99387585714070430.0E+0010010021.61036616827534831.61036616827534812.22E-161000103-.2566630610425008E-02-.2566630610425004E-02-3.90E-182101004-.1845179661310498E-02-.1845179661310520E-022.19E-1720110050.22357178428686960.22357178428686958.33E-1721001060.18097647448959670.18097647448959665.55E-17201010(b|...)IANALYTICCOSYINFINITYDIFFORDEREXPONENTS1-.7582611230530127E-02-.7582611230530126E-02-8.67E-1910010020.99387585714070430.99387585714070430.0E+001000103-.2111934605405531E-02-.2111934605405528E-02-2.60E-182101004-.1709564918748637E-02-.1709564918748637E-022.17E-192011005-.2561017801500153E-02-.2561017801500152E-02-1.30E-182100106-.2305539692531015E-02-.2305539692531048E-023.30E-17201010\@makecaption

Listing 3Vertical aberrations of a𝙳𝙸𝚀​13∘\mathtt{DIQ}\,13^{\circ}element atVESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}, hard-edge model (FR 0), parallel to Listing7.1; same field-index value,s=13∘⋅R0=1.61366​ms=13^{\circ}\cdot R_{0}=1.61366\,\mathrm{m}.

## 7.2Continuous-Ring Chromaticity

For the𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}model atVESQ=20.4​kVV_{\mathrm{ESQ}}=20.4\,\mathrm{kV}(the
muong−2g{-}2Run 1b/c storage voltage),⟨n⟩=0.1156800651947388,\langle n\rangle=0.1156800651947388,(24)

and, withγ0\gamma_{0}from Eq.1,
the closed-form result (18) gives (the superscriptsana\mathrm{ana}andCOSY\mathrm{COSY}denote the present analytic closed
form and the COSY INFINITY DA reference, respectively)ξy(p),ana\displaystyle\xi_{y}^{(p),\,\mathrm{ana}}=0.4066570870121702,\displaystyle=0.4066570870121702,(25)ξy(p),COSY\displaystyle\xi_{y}^{(p),\,\mathrm{COSY}}=0.4066570870432928,\displaystyle=0.4066570870432928,(26)

with absolute residual|Δ|≈3×10−11|\Delta|\approx 3\times 10^{-11}(relative difference of order10−1010^{-10}), matching the relative
analytic-numerical agreement reported for the horizontal closed-form
result of Ref.\refciteChromCPO11. The closed
form (18) is exact within the analytic hard-edge
model. The per-element geometric coefficients agree to the
double-precision floor
(Listings7.1,7.1).

## 7.3Modular-Ring Chromaticity

For the modular models, the per-element DA transfer mapsMiM_{i}(truncated at order 2) are composed via the standard DA compositionMf=M2∘M1M_{f}=M_{2}\circ M_{1}(withM1M_{1}applied first,M2M_{2}second), which
at second order reads(Lf,Qf)=(L2L1,L2Q1+Q2(L1⋅,L1⋅))(L_{f},Q_{f})=(L_{2}L_{1},\;L_{2}Q_{1}+Q_{2}(L_{1}\,\cdot,\,L_{1}\,\cdot)). Iterating yields the four-fold ring
mapMring=Mquad∘4M_{\mathrm{ring}}=M_{\mathrm{quad}}^{\circ 4}. The vertical chromaticity is extracted from the composite map via
Eq.17at the periodic dispersion orbit. AcrossVESQ∈[10,26]​kVV_{\mathrm{ESQ}}\in[10,26]\,\mathrm{kV}and atγ0\gamma_{0}of Eq.1,
Table7.3reports the analytic vs COSY INFINITY comparison.
Residuals are uniformly at the3×10−113\times 10^{-11}absolute level
(relative difference of order10−1010^{-10}) for both𝙳𝙸𝙴𝚀​_​𝙾𝙽\mathtt{DIEQ\_ON}and the full modular𝙳𝙸𝙴𝚀\mathtt{DIEQ}, the same
scale as the𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}result reported above and as the
relative analytic-numerical agreement of Ref.\refciteChromCPO11
for the horizontal case.
The DA-extracted vertical chromaticity expansion inδp\delta_{p}to order 9
follows from the same COSY INFINITY run that produced these reference values; the
higher-order chromaticity coefficients are not analysed further here, as the
present analytic derivation targets the leadingξy(0)=ξy\xi_{y}^{(0)}=\xi_{y}.\tbl

Vertical chromaticityξy(p)\xi_{y}^{(p)}for the modular muong−2g{-}2ring across an ESQ-voltage sweep. Analytic results from the present
Hamiltonian framework; COSY INFINITY DA reference. The Residual column gives|Δ|=|ξy(p),ana−ξy(p),COSY||\Delta|=|\xi_{y}^{(p),\,\mathrm{ana}}-\xi_{y}^{(p),\,\mathrm{COSY}}|at the precision of the underlying1616-digit floating-point computation; the displayed table values are
truncated to1010digits for column width.𝙳𝙸𝙴𝚀​_​𝙾𝙽\mathtt{DIEQ\_ON}𝙳𝙸𝙴𝚀\mathtt{DIEQ}VESQV_{\mathrm{ESQ}}(kV)AnalyticCOSYAnalyticCOSY|Δ||\Delta|10.00.27529966690.27529966690.27529966690.27529966690.25978237230.25978237230.25978237230.25978237232.2×10−112.2{\times}10^{-11}14.00.33889803060.33889803060.33889803060.33889803060.31856956360.31856956360.31856956360.31856956362.6×10−112.6{\times}10^{-11}18.20.40305176500.40305176500.40305176500.40305176500.37730575900.37730575900.37730575900.37730575903.0×10−113.0{\times}10^{-11}18.30.40456684130.40456684130.40456684130.40456684130.37868604420.37868604420.37868604420.37868604423.0×10−113.0{\times}10^{-11}20.40.43636468470.43636468470.43636468470.43636468470.40758257970.40758257970.40758257970.40758257973.2×10−113.2{\times}10^{-11}22.00.46063649870.46063649870.46063649870.46063649870.42954742790.42954742790.42954742790.42954742793.3×10−113.3{\times}10^{-11}26.00.52192956290.52192956290.52192956290.52192956290.48466468280.48466468280.48466468280.48466468283.6×10−113.6{\times}10^{-11}

The agreement across three ring models and theVESQV_{\mathrm{ESQ}}sweep of
Table7.3parallels the validation reported in
Ref.\refciteChromCPO11 for the horizontal case.
Figure4summarises the comparison graphically: the
closed-form𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}result tracks both modular COSY INFINITY models across
theVESQV_{\mathrm{ESQ}}range. The𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}continuous-ring closed-formξy(p)\xi_{y}^{(p)}agrees with the full modular𝙳𝙸𝙴𝚀\mathtt{DIEQ}values
to within≲0.3%{\lesssim}\,0.3\%and lies∼6{\sim}\,6–7%7\%below the𝙳𝙸𝙴𝚀​_​𝙾𝙽\mathtt{DIEQ\_ON}values across theVESQV_{\mathrm{ESQ}}range, a structural
difference between the ring models rather than a numerical residual;
the residual between the analytic and COSY INFINITY values within
each model is at the3×10−113\times 10^{-11}level (Table7.3).

Cross-check against Ref.\refciteChromCPO11.The horizontal
chromaticity of the same modular𝙳𝙸𝙴𝚀\mathtt{DIEQ}ring (no fringe fields, Method 1C of
Ref.\refciteChromCPO11) is reproduced from the samesweep_v.foxrun via∂νx/∂δp\partial\nu_{x}/\partial\delta_{p}:ξx(p)​(VESQ=18.2​kV)=−0.12339043\xi_{x}^{(p)}(V_{\mathrm{ESQ}}=18.2\,\mathrm{kV})=-0.12339043, matching the
published value of Ref.\refciteChromCPO11 (entryMethod 1C:−0.1233904305126808-0.1233904305126808analytic,−0.1233904305225122-0.1233904305225122COSY INFINITY) to all eight printed digits.

## 7.4Higher-Order Chromaticities

The chromaticitiesξx,y(j)\xi^{(j)}_{x,y},j≥0j\geq 0, are the coefficients of
the Taylor expansion of the tune in the relative momentum offset about
the on-momentum value,νx,y​(δp)=νx,y​(0)+∑j≥1ξx,y(j−1)​δpjj!.\nu_{x,y}(\delta_{p})=\nu_{x,y}(0)+\sum_{j\geq 1}\xi^{(j-1)}_{x,y}\,\frac{\delta_{p}^{j}}{j!}.(27)

The on-momentum tuneνx,y​(0)\nu_{x,y}(0)is not itself a chromaticity. The
order-zero coefficientsξx,y(0)=ξx,ξy\xi^{(0)}_{x,y}=\xi_{x},\xi_{y}are the
linear chromaticities of
Eqs.18–19, andξx,y(j)\xi^{(j)}_{x,y}forj≥1j\geq 1are the higher-order (nonlinear) chromaticities. While closed-form
expressions forξ(j)\xi^{(j)}atj≥1j\geq 1become unwieldy, the COSY INFINITY DA
framework computes them numerically up to arbitrary order. Listing7.4shows the DA series ofνx\nu_{x}andνy\nu_{y}up to order 9 for the full modular𝙳𝙸𝙴𝚀\mathtt{DIEQ}ring atVESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}, generated bychrom_o9.fox(a single-voltage variant ofsweep_v.foxwithINO := 9). The order-1 coefficient is
the linear chromaticityξx,ξy\xi_{x},\xi_{y}already discussed; higher
orders give the nonlinear momentum dependence of the tune. The horizontal
linear coefficient−0.1233904305-0.1233904305matches Ref.\refciteChromCPO11 Method 1C to all printed digits, as noted above; the corresponding
horizontal/vertical higher-order coefficients are not analysed further
in this paper, since the closed-form derivation targets the leadingξy(0)\xi^{(0)}_{y}only.⬇===DIEQring,V_ESQ=18.2kV,INO=9,FR0===Lineartunes:nu_x=0.9473764793755017nu_y=0.3221602847213103MU(1)(=nu_xasDApolynomialindp):ICOEFFICIENTORDEREXPONENTS10.94737647937550170000002-.12339043052251201000013-.3681733087546968E-012000024-.1562867245937842E-013000035-.4751272809210552E-024000046-.7538863441833791E-0250000570.3282165942661314E-026000068-.7480427768855409E-0270000790.6825853021849857E-02800008-------------------------------------------MU(2)(=nu_yasDApolynomialindp):ICOEFFICIENTORDEREXPONENTS10.322160284721310300000020.37730575902269441000013-.105541525232909820000240.17092548680271523000035-.194545765293216040000460.29612994922321985000057-.450514011923516560000680.73270064418416267000079-1.221230140912835800008-------------------------------------------\@makecaption

Listing 4DA series of the horizontal and vertical tunes for the full modular DIEQ ring at the reference voltage 18.2 kV, COSY INFINITY DA order 9, hard-edge model (FR 0). The order-1 coefficient is the linear chromaticity; the order-j coefficient gives the next higher-order chromaticity divided by j factorial, in the convention of the horizontal-counterpart paper.⬇===DIEQring,V_ESQ=18.2kV,INO=9,FR3+EFB===Lineartunes:nu_x=0.9468320541358946nu_y=0.3237823954147181MU(1)(=nu_xasDApolynomialindp):ICOEFFICIENTORDEREXPONENTS10.94683205413589460000002-.12489970018137021000013-.3778730608464986E-012000024-.1624903747627255E-013000035-.5219741601567675E-024000046-.7608998866056834E-0250000570.2768541237848285E-026000068-.7060010158752530E-0270000790.6203705978249155E-02800008-------------------------------------------MU(2)(=nu_yasDApolynomialindp):ICOEFFICIENTORDEREXPONENTS10.323782395414718100000020.37983642053078331000013-.104660705748808320000240.140690614992586130000354.8215953206022054000046-6.279906728002484500005712.013681251268246000068-19.551008163148627000079-3.481140292129433800008-------------------------------------------\@makecaption

Listing 5DA series of the horizontal and vertical tunes for the full modular DIEQ ring atVESQ=18.2V_{\mathrm{ESQ}}=18.2kV, COSY INFINITY DA order 9, realistic Enge-function fringe field with EFB extension (FR 3+ EFB; same Enge coefficients andzEFB=1.22​cmz_{\mathrm{EFB}}=1.22\,\mathrm{cm}calibration as the horizontal-counterpart paper). Parallel to Listing7.4but with the realistic fringe-field treatment. The linear vertical chromaticity differs from the hard-edge value of Listing7.4by∼0.7%\sim 0.7\%, consistent with the prior fringe-contribution estimate from the Weisskopf dissertation integrated over the full ring.

The linear vertical chromaticity under the two fringe-field treatments
is compared across the full operating range in
Fig.3, paralleling the linear-chromaticity
voltage scan of the horizontal-counterpart work[18]. All
COSY INFINITY chromaticities reported here are converged in the
computational order of the DA transfer map: the hard-edge
(𝙵𝚁​0\mathtt{FR}\ \mathtt{0}) linear chromaticities are already
converged at computational order 3, whereas the realistic Enge-fringe
(𝙵𝚁​3\mathtt{FR}\ \mathtt{3}+ EFB)verticalchromaticity is
converged only at order 9 and is computed at that order here
(Listing7.4; its order-3 value differs from the
converged result by∼4×10−2%{\sim}\,4\times 10^{-2}\,\%), while the
horizontal chromaticity is
order-3 converged in both fringe models.

The nonlinear vertical chromaticitiesξy(j)\xi_{y}^{(j)}reported here, in
both fringe models, are obtained with the𝙳𝙸𝚀\mathtt{DIQ}pure-quadrupole
main field; in the𝙵𝚁​3\mathtt{FR}\ \mathtt{3}+ EFB case this is the
single quadrupole Enge falloff and its EFB. The allowed higher ESQ
multipoles (1212-pole and above), which by the feed-down argument above
first contribute atξy(3)\xi_{y}^{(3)}and each carry their own effective
field boundary and Enge falloff, are not included in this series.
Incorporating them requires a per-multipole falloff extraction and a
separate Enge calibration for each harmonic in COSY INFINITY; this is
left to future work (Sec.9).

The realistic𝙵𝚁​3\mathtt{FR}\ \mathtt{3}+ EFB curve lies slightly above
the hard-edge𝙵𝚁​0\mathtt{FR}\ \mathtt{0}curve throughout, the offset
growing smoothly with voltage; at the nominal Run 3–6 pointVESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}the two differ by∼0.7%{\sim}\,0.7\%, of the
order of the fringe-field contribution estimated previously for the
muong−2g{-}2ring[20].Figure 3:Linear vertical chromaticityξy(p)\xi_{y}^{(p)}of the full
modular𝙳𝙸𝙴𝚀\mathtt{DIEQ}muong−2g{-}2ring vs ESQ voltage, COSY
INFINITY DA: hard-edge model (𝙵𝚁​0\mathtt{FR}\ \mathtt{0}, circles,
solid) and the realistic Enge-function fringe field with EFB
extension (𝙵𝚁​3\mathtt{FR}\ \mathtt{3}+ EFB, squares, dashed; same
Enge coefficients andzEFB=1.22​cmz_{\mathrm{EFB}}=1.22\,\mathrm{cm}calibration as the horizontal-counterpart paper[18]).
Vertical dashed gridlines mark the storage operating voltagesVESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}(Runs 3–6),18.3​kV18.3\,\mathrm{kV}(Runs 1a/d, Run 2), and20.4​kV20.4\,\mathrm{kV}(Runs 1b/c).Figure 4:Vertical chromaticityξy(p)\xi_{y}^{(p)}vs ESQ voltage. Top:
the closed-form𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}result (Eq.18,
solid line) and COSY INFINITY DA values for the simplified modular𝙳𝙸𝙴𝚀​_​𝙾𝙽\mathtt{DIEQ\_ON}ring (squares, hard-edge model𝙵𝚁​0\mathtt{FR\ 0}), the full modular𝙳𝙸𝙴𝚀\mathtt{DIEQ}ring (circles,𝙵𝚁​0\mathtt{FR\ 0}), and the full modular𝙳𝙸𝙴𝚀\mathtt{DIEQ}ring with
the realistic Enge fringe-field model and EFB extension (diamonds,𝙵𝚁​3\mathtt{FR\ 3}+ EFB). Vertical dashed gridlines mark the three
muong−2g{-}2storage operating points:VESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}(Runs 3–6),18.3​kV18.3\,\mathrm{kV}(Runs 1a/d, Run 2), and20.4​kV20.4\,\mathrm{kV}(Runs 1b/c briefly). Bottom: absolute residuals|Δ​ξy(p)|=|ξy(p),ana−ξy(p),COSY||\Delta\xi_{y}^{(p)}|=|\xi_{y}^{(p),\,\mathrm{ana}}-\xi_{y}^{(p),\,\mathrm{COSY}}|between the analytic
chromaticity and the COSY INFINITY DA reference, for the two
modular models in the hard-edge regime.

## 8Application to Muong−2g{-}2

The muong−2g{-}2Experiment operated at three storage voltages
across Runs 1–6:VESQ=18.2​kVV_{\mathrm{ESQ}}=18.2\,\mathrm{kV}(Runs 3–6 nominal,
the primary physics dataset;⟨n⟩≈0.103\langle n\rangle\approx 0.103),VESQ=18.3​kVV_{\mathrm{ESQ}}=18.3\,\mathrm{kV}(Runs 1a/d and Run 2;⟨n⟩≈0.104\langle n\rangle\approx 0.104), andVESQ=20.4​kVV_{\mathrm{ESQ}}=20.4\,\mathrm{kV}(Runs 1b and 1c, briefly;⟨n⟩≈0.116\langle n\rangle\approx 0.116)[12,20].
At the Run 3–6 nominal operating point, the closed-form
result (18) gives the vertical chromaticityξy(p)≈0.3765(𝙳𝙸𝚀𝟹𝟼𝟶),ξy(p)≈0.3773(full modular​𝙳𝙸𝙴𝚀),\xi_{y}^{(p)}\;\approx\;0.3765\quad(\mathtt{DIQ360}),\qquad\xi_{y}^{(p)}\;\approx\;0.3773\quad(\text{full modular }\mathtt{DIEQ}),(28)

consistent with prior numerical results
of Ref.\refciteweisskopfphd. The vertical chromaticity bears on the
pitch correctionCpC_{p}[13,12]: a finiteξy\xi_{y}broadens the vertical tune spread over the stored-muon momentum
distribution and thereby the averageCpC_{p}. This analyticξy\xi_{y}is not
an input to the publishedCpC_{p}correction, which is determined from tracker
measurements of the stored-beam distribution; the closed-form result instead
serves as an independent lattice diagnostic and a tool for systematic studies
away from the nominal operating lattice. Its uncertainty is negligible on the
scale of the78​ppb78\,\mathrm{ppb}total systematic uncertainty of the final
muong−2g{-}2measurement[14].

## 9Conclusion and Outlook

We have derived the vertical chromaticity of the Fermilab muong−2g{-}2storage
ring in closed form for the continuous ring𝙳𝙸𝚀𝟹𝟼𝟶\mathtt{DIQ360}model and via
modular composition for the𝙳𝙸𝙴𝚀​_​𝙾𝙽\mathtt{DIEQ\_ON}and full𝙳𝙸𝙴𝚀\mathtt{DIEQ}ring models, using the Hamiltonian order-by-order perturbation
framework of Refs.\refciteAIEP108book,ESCPO10AIEP. The closed-formξy(p)​(2​π,n)\xi_{y}^{(p)}(2\pi,n)in Eq.18is in direct
functional correspondence with the horizontal counterpart[18],
exhibiting the same kinematic prefactor and a complementarynn-dependent
geometric factor. The full set of vertical second-order aberrations of𝙳𝙸\mathtt{DI}and𝙳𝙸𝚀\mathtt{DIQ}in Sec.4, together with the modular
composition of Sec.7, completes the vertical
analogue of the horizontal-plane analytic treatment[18]for the muong−2g{-}2ring.

Agreement with COSY INFINITY DA at the10−1110^{-11}level across all
three ring models
confirms the analytic framework. The framework extends
naturally to the analogous derivation of the analyticEE-field correctionCeC_{e}and pitch correctionCpC_{p}via a DA normal-form algorithm; this,
and the extension of the reported nonlinear vertical chromaticity to the
full ESQ multipole content (with separately calibrated fringe fields per
allowed multipole, first contributing atξy(3)\xi_{y}^{(3)}), is deferred to
follow-up work.

## Acknowledgments

This work was supported by the U.S. Department of Energy under
Contract No. DE-FG02-08ER41546 and Contract No. DE-SC0018636. We
gratefully acknowledge our colleagues in the Beam Dynamics team of
the Fermilab Muong−2g{-}2Experiment, where we have collaborated since
2016. This work was produced by Fermi Forward Discovery Group, LLC
under Contract No. 89243024CSC000002 with the U.S. Department of
Energy, Office of Science, Office of High Energy Physics. Publisher
acknowledges the U.S. Government license to provide public access
under the DOE Public Access Plan
(https://www.energy.gov/doe-public-access-plan).

## References
- [1]M. Berz and K. Makino(2023)COSY INFINITY Version 10.2 beam physics manual.Technical reportTechnical ReportMSUHEP20221202,Michigan State University,East Lansing, MI 48824.Note:See also https://cosyinfinity.orgCited by:§3,§4.
- [2]M. Berz and K. Makino(2026)COSY INFINITY and its use for singlepass and multipass systems.Microscopy.External Links:DocumentCited by:§3.
- [3]M. Berz(1999)Modern map methods in particle beam physics.Academic Press,San Diego.Note:Also available at https://www.bmtdynamics.org/pubExternal Links:ISBN 9780120147502Cited by:§4.
- [4]K. L. Brown, R. Belbeoch, and P. Bounin(1964)First- and second-order magnetic optics matrix equations for the midplane of uniform-field wedge magnets.Rev. Sci. Instrum.35,pp. 481.Cited by:§1.
- [5]K. L. Brown and R. Servranckx(1985)First- and second-order charged particle optics.AIP Conf. Proc.127,pp. 62–138.Note:Also SLAC-PUB-3381Cited by:§1.
- [6]K. L. Brown(1968)A first and second order matrix theory for the design of beam transport systems and charged particle spectrometers.Adv. Part. Phys.1,pp. 71–134.Note:Also SLAC-R-075, SLAC-75Cited by:§1.
- [7]K. L. Brown(1981)Beam envelope matching for beam guidance systems.Nucl. Instrum. Meth.187,pp. 51.Cited by:§1.
- [8]J. Grangeet al.(2015)Muongg–2 technical design report.Fermilab Rep.Technical ReportFERMILAB-FN-0992-E,Fermi National Accelerator Laboratory,Batavia, IL 60510.Note:Fermilab Muon g-2, GM2-doc-2055Cited by:§1,§2.
- [9]INTEGRATED Engineering Software(2022)COULOMB.Note:Integrated Engineering Software, Winnipeg, CanadaCited by:§4.
- [10]K. Makino and M. Berz(2006)COSY INFINITY version 9.Nucl. Instrum. Meth.558,pp. 346–350.Cited by:§3,§7.
- [11]K. Makino, E. Valetov, and M. Berz(2017)Detailed linear optics and tunes of theg−2g{-}2ring.Fermilab Rep.Technical ReportFERMILAB-FN-1289-PPD,Fermi National Accelerator Laboratory,Batavia, IL 60510.Note:Fermilab Muon g-2, E989 Note 104, GM2-doc-5715Cited by:§2.
- [12]Muon g-2 Collaboration(2021)Beam dynamics corrections to the run-1 measurement of the muon anomalous magnetic moment at fermilab.Phys. Rev. Accel. Beams24,pp. 044002.External Links:DocumentCited by:§1,§3,§8,§8.
- [13]Muon g-2 Collaboration(2024)Detailed report on the measurement of the positive muon anomalous magnetic moment to 0.20 ppm.Phys. Rev. D110,pp. 032009.Note:Also arXiv:2402.15410, FERMILAB-PUB-24-0084-AD-CSAID-PPDExternal Links:DocumentCited by:§1,§2,§8.
- [14]Muon g-2 Collaboration(2025)Measurement of the positive muon anomalous magnetic moment to 127 ppb.Phys. Rev. Lett.135,pp. 101802.External Links:DocumentCited by:§1,§8.
- [15](2025)Opera simulation software.Dassault Systèmes SIMULIA,Vélizy-Villacoublay, France.Cited by:§4,§4.
- [16]Y. K. Semertzidis, G. Bennett, E. Efstathiadis, F. Krienen, R. Larsen, Y. Y. Lee, W. M. Morse, Y. Orlov, C. S. Ozben, B. L. Roberts, L. P. Snydstrup, and D. S. Warburton(2003)The Brookhaven muon (g−2g-2) storage ring high voltage quadrupoles.Nucl. Instrum. Meth. A503(3),pp. 458–484.Cited by:§4,§4.
- [17]E. Valetov, M. Berz, and K. Makino(2019)Computation of the main and fringe fields for the electrostatic quadrupoles of the Muon g-2 storage ring.Int. J. Mod. Phys. A34(36),pp. 1942041–1–16.Note:Also FERMILAB-PUB-19-092-PPDExternal Links:DocumentCited by:§4,§4,§4.
- [18]E. Valetov, K. Makino, and M. Berz(2026)Analytic chromaticity formulas for the Muong−2g{-}2Experiment at Fermilab.Microscopy.External Links:DocumentCited by:§1,§2,§4.1,§4.2,§4.2,§4,§4,§4,§5,§5,§6,Figure 3,§7.4,§9.
- [19]E. Valetov(2017)Field modeling, symplectic tracking, and spin decoherence for EDM and Muon g-2 lattices.Ph.D. Thesis,Michigan State University,East Lansing, Michigan, USA.Note:Also FERMILAB-THESIS-2017-21Cited by:§4,§4,§4.
- [20]A. Weisskopf(2021)Application of rigorous high-order methods and normal forms to nonlinear systems.Ph.D. Thesis,Michigan State University,East Lansing, Michigan, USA.Cited by:§1,§3,§7.4,§8.
- [21]W. Wu(2018)The beam dynamics and beam related uncertainties in the fermilab muong​-​2g\textrm{-}2experiment.Ph.D. thesisUniversity of Mississippi,Oxford, MS.Note:Fermilab report FERMILAB-THESIS-2018-08Cited by:§4,§4.

## 


- 


Major funding support from
