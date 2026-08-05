# Analytical Charge Density Profile of Vortex Core in Weak-Coupling Superconductor

**arXiv ID**: 2608.00226v1
**Authors**: Chi-Ken Lu
**Published**: 2026-07-31
**Categories**: cond-mat.supr-con, math-ph
**HTML URL**: https://arxiv.org/html/2608.00226v1

## Abstract

Self-consistent Bogoliubov-de Gennes calculations have long shown that solving the Poisson equation inside a superconducting vortex turns a one-signed charge depletion into a modulation that alternates in sign with period $π/k_F$. We give an elementary account of that result. Taking the Caroli-de Gennes-Matricon bound states in a step-like gap, we show that the normalization of the bound-state spinor is nearly independent of angular momentum, which collapses the mode sum into closed form. Inside the core the vortex winding removes one Bessel channel from a completeness sum, so the density vanishes on the vortex line and carries Friedel-like oscillations of wavevector $2k_F$; outside it the sum gives a $1/r$ envelope decaying over a coherence length, with a residual ripple. The bound-state charge does not integrate to zero, so neutrality obliges the extended states to compensate it exactly. That compensation is complete at long wavelength but fails at the diameter of the Fermi circle, and what survives is a sign-alternating $2k_F$ modulation reduced only by $4k_F^2/(4k_F^2+k_{TF}^2)$, a factor lying between one-half and three-quarters for any metal. The oscillation is therefore not a delicate effect but a consequence of neutrality and the inefficiency of screening at large momentum transfer: in the screened total the smooth terms cancel and only the ripple is left.

## Full Text

Analytical Charge Density Profile of Vortex Core in Weak-Coupling Superconductor

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
- License: CC BY 4.0arXiv:2608.00226v1 [cond-mat.supr-con] 31 Jul 2026

## Analytical Charge Density Profile of Vortex Core in Weak-Coupling SuperconductorChi-Ken LuDepartment of Mathematics and Computer Science,
Rutgers University Newark, Newark, New Jersey 07102, USA

## Abstract

Self-consistent Bogoliubov–de Gennes calculations have long shown that
solving the Poisson equation inside a superconducting vortex turns a
one-signed charge depletion into a modulation that alternates in sign
with periodπ/kF\pi/k_{\mathrm{F}}. We give an elementary account of that result.
Taking the Caroli–de Gennes–Matricon bound states in a step-like gap,
we show that the normalization of the bound-state spinor is nearly
independent of angular momentum, which collapses the mode sum into
closed form. Inside the core the vortex winding removes one Bessel
channel from a completeness sum, so the density vanishes on the vortex
line and carries Friedel-like oscillations of wavevector2​kF2k_{\mathrm{F}}; outside
it the sum gives a1/r1/renvelope decaying over a coherence length,
with a residual ripple.
The bound-state charge does not integrate to zero, so neutrality obliges the
extended states to compensate it exactly. That compensation is
complete at long wavelength but fails at the diameter of the Fermi
circle, and what survives is a sign-alternating2​kF2k_{\mathrm{F}}modulation
reduced only by4​kF2/(4​kF2+kTF2)4k_{\mathrm{F}}^{2}/(4k_{\mathrm{F}}^{2}+k_{\mathrm{TF}}^{2}), a factor lying between
one-half and three-quarters for any metal. The oscillation is
therefore not a delicate effect but a consequence of neutrality and the
inefficiency of screening at large momentum transfer: in the screened
total the smooth terms cancel and only the ripple is left.

## IIntroduction

The electronic structure of vortex cores in type-II superconductors has
been studied since Caroli, de Gennes, and Matricon
(CdGM)[1]found discrete quasiparticle bound states
at energiesEμ=μ​Δ2/EFE_{\mu}=\mu\Delta^{2}/E_{\mathrm{F}}. In conventional type-II superconductors
such as NbSe2, and in the full-shell hybrid nanowires resolved
recently[2], the lowest in-gap state isμ=1/2\mu=1/2, whereas in
topological superconductors[3]theμ=0\mu=0vortex bound
states[4,5,6]are a signature of the underlying topological band
structure[7]. These CdGM states govern the
local spectroscopic structure of the mixed
state[8,9,10]and underlie a range of phenomena from spectral flow to vortex
dynamics[11,12,13].

The CdGM states arise in much the same way as the bound states of a
one-dimensional potential well. For the well problem, the classically
allowed region lies between the two turning points at which the
classical momentump​(x)=E−V​(x)p(x)=\sqrt{E-V(x)}vanishes, and the eigenenergyEEfollows from a quantization rule in integral
form[14]. For a simpless-wave superconductor
in two dimensions the CdGM states are two-component spinors, and they
are likewise trapped beyond a turning point set by the centrifugal
potential and the angular momentumℏ​μ\hbar\mu. What differs from the
potential-well problem is that the second turning point is implicit: it
occurs where the gapΔ​(r)\Delta(r), acting in particle-hole space, meets
the energyEE. The seminal paper of CdGM[1]and the
work of Bardeen, Kümmel, Jacobs, and Tewordt
(BKJT)[15]determine the bound-state energy by
matching the phases accumulated by the spinor wavefunction from the
vortex line and from deep inside the bulk.

The gap profileΔ​(r)\Delta(r)not only binds the CdGM states, it also
drives a charge
redistribution[16,17]. A simple
explanation for the charge transfer is that electrons lower their
energy by moving from the normal region inside the core into the
surrounding superconducting
subsystem[18]. The amount of transferred charge
has been estimated from the hole component of the extended states,n=∑Ek>0|vk|2n=\sum_{E_{k}>0}|v_{k}|^{2}[16,17].
Blatteret al.[19], in the same spirit
as the charged-vortex picture of Ref.[18],
estimated the local charge densityn​(r)n(r), derived the corresponding
Poisson equation, and proposed an experiment to detect the electric
dipole generated by the vortex.

BecauseΔ​(r)\Delta(r)varies slowly on the scalekF−1k_{\mathrm{F}}^{-1}, the densityn​(r)n(r)obtained in Ref.[19]is smooth on the
scale of the coherence lengthξ\xi. Any rapid variation of the
charge density must therefore come from the CdGM states. Hayashi,
Ichioka, and Machida[20]established
numerically that this short-wavelength inhomogeneity is encoded in the
CdGM wavefunctions and is accessible in principle by STM. Machida and
Koyama[21]performed full BdG++Poisson
calculations and found that thescreenedcharge changes
sign—an observation that still lacks an analytical explanation. Friedel oscillations associated with vortex bound states
have since been resolved by STM in the iron-based superconductor
KCa2Fe4As4F2[22]. That
experiment probes the local density of states in the extreme quantum
limitT/Tc≪Δ/EFT/T_{c}\ll\Delta/E_{\mathrm{F}}, and the accompanying self-consistent
calculation, performed atkF​ξ≃6k_{\mathrm{F}}\xi\simeq 6, finds that the order
parameter itself acquires a Friedel-like modulation which shifts the
bound-state energies away from the1:3:51\!:\!3\!:\!5ratio. The
weak-coupling regime considered here is complementary: atkF​ξ≫1k_{\mathrm{F}}\xi\gg 1the gap profile is essentially rigid, and the
oscillation resides in the density.
In a related setting, simulations of ultracold Fermi
gases[23]obtain the2​kF2k_{\mathrm{F}}Friedel
oscillation[24]analytically by summing the
squared wavefunctions confined in a quantum well. That calculation is
tractable because the infinite-well wavefunctions in one dimension are
elementary and share a common normalization constant.
For a one-dimensional well with two turning points,
Ref.[25]obtained closed-form uniform
semiclassical densities—the leading corrections to Thomas–Fermi
theory—by matching Langer–Airy forms of the WKB
wavefunction[14]across the turning points.
The resulting expressions remain valid through the classically
forbidden region and, notably, require no explicit sum over occupied
states.
The CdGM problem
is harder on all three counts: the decay function and the particle-hole
mixing angle obey a pair of coupled nonlinear differential equations
[Eqs. (4.17) and (4.18) of Ref.[15]], the
normalization constant is in principle mode-dependent, and
the semiclassical wavefunctions of Ref.[15]break down inside the turning point of the centrifugal barrier.

Our aim is explanatory rather than predictive: to recover the sign
change of Ref.[21]from arguments simple
enough to be checked by hand, and thereby to identify which features of
the vortex it actually depends on. We therefore work throughout with
the most economical model that retains those features, and take from
CdGM theory whatever can be taken rather than re-deriving it. In
particular we adopt a step-like gap profile for an isolated vortex,Δ​(r)=0\Delta(r)=0forr<ξr<\xiandΔ​(r)=Δ∞\Delta(r)=\Delta_{\infty}otherwise, and
take the spectrumEμ=μ​(Δ2/EF)E_{\mu}=\mu(\Delta^{2}/E_{\mathrm{F}})as given, withμ\murunning from1/21/2up to⌊kF​ξ⌋\lfloor k_{\mathrm{F}}\xi\rfloor, where the turning
pointμ/kF\mu/k_{\mathrm{F}}reaches the core edger=ξr=\xi. The step profile
simplifies the BdG equation inside the core considerably. In the outer
region the BKJT envelope can be linearized, with the expansion
coefficients fixed by the matching conditions atr=ξr=\xi. This yields
closed-form wavefunctions on both sides and makes the normalization
integral straightforward. We find that, through a cancellation between
competing inner and outer contributions, the normalization constant is
a weak function ofμ\mufor the majority of the CdGM ladder. This
allows the constant to be pulled out of the mode sum as an overall
prefactor, after which properties of Bessel functions deliver the
density in closed form. The resulting analyticaln​(r)n(r)agrees with
our numerics, most accurately away from the immediate vicinity of the
core edge.

The paper is organised as follows. SectionIIassembles
the bound-state wavefunctions—the radial equations with their exact
Bessel solutions inside the step-gap core and the linearized BKJT
solution outside, followed by the normalization constant, whose weak
dependence onμ\muis what makes the rest possible.
SectionIIIcarries out the mode sum, obtaining the
in-core density from a Bessel completeness identity and the outer
profile as a decaying1/r1/renvelope. SectionIVturns to the electrostatics: what enters Poisson’s equation as source,
how the screened equation is solved by treating each wavevector in the
source separately, and what charge survives the screening, checked at
each stage against direct numerical solution.
SectionVsets the result beside the numerical and
experimental literature and states what is and is not claimed, and
Sec.VIconcludes. Supplemental Material collects the
justification of the replacement trick, its error analysis, and the
verification of the solver[26].

## IIModel and bound-state wavefunctions

## II.1Radial equations and inner solutions

We consider a single vortex line in a weak-couplingss-wave
superconductor, in the notation of BKJT[15]. After
absorbing the winding phasee−i​θe^{-i\theta}of the gapΔ​(𝐫)=Δ​(r)​e−i​θ\Delta(\mathbf{r})=\Delta(r)e^{-i\theta}by the gauge rotatione−i​σz​θ/2e^{-i\sigma_{z}\theta/2}, the radial BdG equation readsσz​ℏ22​m​[d2d​r2+1r​dd​r−(μ−σz​e​rℏ​c​Aθ)2r2+kF2+σz​E]​f^=σx​Δ​(r)​f^\sigma_{z}\frac{\hbar^{2}}{2m}\!\left[\frac{d^{2}}{dr^{2}}+\frac{1}{r}\frac{d}{dr}-\frac{\bigl(\mu-\frac{\sigma_{z}er}{\hbar c}A_{\theta}\bigr)^{2}}{r^{2}}+k_{\mathrm{F}}^{2}+\sigma_{z}E\right]\!\hat{f}\\
=\sigma_{x}\Delta(r)\hat{f}(1)

whereσz\sigma_{z}andσx\sigma_{x}are Pauli matrices in particle-hole
space.
In this paper we fix the in-plane Fermi wavevector to bekFk_{\mathrm{F}}. Single-valuedness of the spinorf^=(f+,f−)𝖳\hat{f}=(f_{+},f_{-})^{\mathsf{T}}after the gauge rotation forcesμ\muto be a half-integer (2​μ2\muodd);f+f_{+}andf−f_{-}are the electron and
hole amplitudes. The azimuthal vector potentialAθA_{\theta}carries
both the quantized vortex flux and the applied fieldHHthroughr​∫𝑑θ​Aθ=Φ0+π​r2​Hr\int d\theta\,A_{\theta}=\Phi_{0}+\pi r^{2}HwithΦ0=h​c/(2​e)\Phi_{0}=hc/(2e).
BKJT[15]splitAθA_{\theta}into the singular vortex
pieceℏ​c/(2​e​r)\hbar c/(2er)and a smooth field-induced remainderAθ′A^{\prime}_{\theta}; in the dilute-vortex regimeH≪Hc2H\ll H_{c_{2}}the latter is
negligible.

The zero-temperature charge density is the sum of squared
hole amplitudes over all positive-energy bound states,n​(𝐫)=2​∑E>0|fE,−​(𝐫)|2,n(\mathbf{r})=2\sum_{E>0}|f_{E,-}(\mathbf{r})|^{2},(2)

the factor of22accounting for spin degeneracy. Continuum states
(E>Δ∞E>\Delta_{\infty}) produce a spatially uniform background that is
absorbed into the bulk densityn0n_{0}; only the localized deviationδ​n​(r)=n​(r)−n0\delta n(r)=n(r)-n_{0}due to the CdGM bound states concerns us here.
HerefE,−f_{E,-}is the radial amplitude fixed by
Eq. (4) below, the angular factorei​μ​θ/2​πe^{i\mu\theta}/\sqrt{2\pi}carrying its own normalization, so that the
areal density is Eq. (2) divided by2​π2\pi. Since the
two-dimensional bulk density iskF2/2​πk_{\mathrm{F}}^{2}/2\pi, densities quoted in
units ofkF2k_{\mathrm{F}}^{2}are then directly the modulation relative to the
bulk, and∫δ​n​r​𝑑r\int\delta n\,r\,drcounts the electrons bound to the
vortex.

To solve Eq. (1), BKJT[15]introduce
the slow-mode ansatzf^​(r)=Cμ​g​(x)​Hμ(1)​(kF​r)+c.c.,\hat{f}(r)=C_{\mu}\,g(x)\,H_{\mu}^{(1)}(k_{\mathrm{F}}r)+\mathrm{c.c.},(3)

whereHμ(1)H_{\mu}^{(1)}is the Hankel function of the first kind andg​(x)=[ei​η/2,e−i​η/2]𝖳​e−ξ1g(x)=[e^{i\eta/2},e^{-i\eta/2}]^{\mathsf{T}}e^{-\xi_{1}}is a spinor
envelope carrying the electron-hole mixing angleη\etaand the
amplitude-decay functionξ1\xi_{1}. The normalization constantCμC_{\mu}is fixed byCμ2​∫0∞r​𝑑r​(|f+|2+|f−|2)=1.C_{\mu}^{2}\int_{0}^{\infty}r\,dr\,\bigl(|f_{+}|^{2}+|f_{-}|^{2}\bigr)=1.(4)

Only the mode index need be carried: the Fermi surface is a single
circle and nokzk_{z}integration is involved, sokFk_{\mathrm{F}}is common to
every mode. What does enter parametrically iskF​ξk_{\mathrm{F}}\xi, through the
core size and the number of modes it admits. A central result
established below is that at fixedkF​ξk_{\mathrm{F}}\xithe constant depends only
weakly onμ\mu, so that it may be replaced by its mean⟨C2⟩\langle C^{2}\rangleover the ladder, which itself scales as(kF​ξ)−1(k_{\mathrm{F}}\xi)^{-1}.

The slow-mode coordinatex​(r)=Δ∞EF​kF​r2−rt2,x(r)=\frac{\Delta_{\infty}}{E_{\mathrm{F}}}k_{\mathrm{F}}\sqrt{r^{2}-r_{t}^{2}},(5)

is built from the in-plane kinetic energyEF=ℏ2​kF2/2​mE_{\mathrm{F}}=\hbar^{2}k_{\mathrm{F}}^{2}/2m. The centrifugal barrier places a
classical turning point atrt=μ/kFr_{t}=\mu/k_{\mathrm{F}}, which grows linearly withμ\muand separates the classically accessible region (r>rtr>r_{t}) from
the forbidden one (r<rtr<r_{t}). Far from the core the gap saturates toΔ∞\Delta_{\infty}, fixing the coherence lengthξ=2​EF/(π​kF​Δ∞)\xi=2E_{\mathrm{F}}/(\pi k_{\mathrm{F}}\Delta_{\infty}).

The envelope functionsη​(x)\eta(x)andξ1​(x)\xi_{1}(x)obey the coupled
first-order system [Eqs. (4.17)–(4.18) of BKJT[15]]d​ηd​x+δ​(x)​cos⁡η\displaystyle\frac{d\eta}{dx}+\delta(x)\cos\eta=Λ+F​(x),\displaystyle=\Lambda+F(x),(6)2​d​ξ1d​x\displaystyle\frac{2\,d\xi_{1}}{dx}=δ​(x)​sin⁡η,\displaystyle=\delta(x)\sin\eta,(7)

with normalized gapδ​(x)=Δ​(r)/Δ∞\delta(x)=\Delta(r)/\Delta_{\infty}, normalized
eigenenergyΛ=E/Δ∞\Lambda=E/\Delta_{\infty}, and vortex-flux termF​(x)=b/(x2+b2)F(x)=b/(x^{2}+b^{2}),b=μ​Δ∞/EFb=\mu\Delta_{\infty}/E_{\mathrm{F}}(the smoothAθ′A^{\prime}_{\theta}correction is negligible inside the core).

For the step-gap model (δ=0\delta=0forr<ξr<\xi,δ=1\delta=1forr≥ξr\geq\xi) the nonlinear coupling in
Eqs. (6)–(7) switches off inside the
core, and the interior solution is exact,η​(x)=Λ​x+arctan⁡(x/b)\eta(x)=\Lambda x+\arctan(x/b)withξ1=0\xi_{1}=0for0≤x≤xc≡x​(ξ)0\leq x\leq x_{c}\equiv x(\xi). BKJT[15]obtain
the bound-state energyE​(kF,μ)E(k_{\mathrm{F}},\mu)by integrating the ODEs outward
from the turning pointx=0x=0and inward from the London penetration
depthx=xλx=x_{\lambda}, and matching at the core edgex=xcx=x_{c}.

The BKJT ansatz is nevertheless unsuitable for the inner region, on two
counts. First,x​(r)x(r)turns imaginary forr<rt​(μ)r<r_{t}(\mu), so
Eq. (3) is ill-defined throughout the classically
forbidden region. Second, the carrierHμ(1)H_{\mu}^{(1)}cannot reproduce
the power-law behavior at the origin dictated by the vortex topology.
Both deficiencies worsen asμ\mugrows, since the forbidden regionr<rt=μ/kFr<r_{t}=\mu/k_{\mathrm{F}}then covers a larger fraction of the core.

Inside the core the gap vanishes and the BdG equations decouple. With
wavevectorsk±=kF±qk_{\pm}=k_{\mathrm{F}}\pm qandq=kF​E/(2​EF)q=k_{\mathrm{F}}E/(2E_{\mathrm{F}}), the regular
solutions are exact Bessel functionsf±​(r)=Cμ​Jμ∓1/2​(k±​r),f_{\pm}(r)=C_{\mu}\,J_{\mu\mp 1/2}(k_{\pm}r),(8)

of ordersμ∓12\mu\mp\tfrac{1}{2}, smooth everywhere—including across the
turning point—with no approximation required. The inner and outer
regions are then carried by different functions, which need not join
continuously atr=ξr=\xi; the resulting step in the density is a few
percent and is confined to a shell about the core edge, from which no
quantitative result below is drawn[27].
Figures1(a) and (b) benchmark these against the
BKJT approximation for a low-lying mode (μ=5.5\mu=5.5,rt/ξ=0.086r_{t}/\xi=0.086)
and a high-lying mode (μ=55.5\mu=55.5,rt/ξ=0.872r_{t}/\xi=0.872). Outside the core
(r>ξr>\xi,δ=1\delta=1) the envelope is linearized inδ​x=x−xc\delta x=x-x_{c},η​(x)\displaystyle\eta(x)≈ηc+η′​(xc)​δ​x,\displaystyle\approx\eta_{c}+\eta^{\prime}(x_{c})\,\delta x,(9)ξ1​(x)\displaystyle\xi_{1}(x)≈ξ1′​(xc)​δ​x,\displaystyle\approx\xi_{1}^{\prime}(x_{c})\,\delta x,(10)

subject toξ1​(xc)=0\xi_{1}(x_{c})=0. The coefficients atxc=(4/π2)−b2x_{c}=\sqrt{(4/\pi^{2})-b^{2}}follow from
Eqs. (6)–(7): for low-lying states
(E≪Δ∞E\ll\Delta_{\infty}) one findsηc\displaystyle\eta_{c}≈\displaystyle\approxπ/2−b​(π2−4)/(2​π),\displaystyle\pi/2-b(\pi^{2}-4)/(2\pi)\>,(11)ξ1′​(xc)\displaystyle\xi_{1}^{\prime}(x_{c})≈\displaystyle\approx12​cos⁡(b​(π2−4)/(2​π)).\displaystyle\frac{1}{2}\cos\bigl(b(\pi^{2}-4)/(2\pi)\bigr)\>.(12)

Truncatingξ1\xi_{1}at first order is justified by the bound|d​ξ1/d​x|≤12|d\xi_{1}/dx|\leq\frac{1}{2}implied by Eq. (7):
retaining higher-order terms would violate this constraint.

The mode structure follows a clear pattern shown in the top two panels of Fig.1.
The componentsfE,±f_{E,\pm}rise from the origin asrμ∓1/2r^{\mu\mp 1/2}, oscillate with period2​π/kF2\pi/k_{\mathrm{F}}in the classically allowed windowrt<r<ξr_{t}<r<\xi, and then
decay exponentially beyond the core edge.
The fact thatf−​(0)=Jν−​(0)=0f_{-}(0)=J_{\nu_{-}}(0)=0for every mode
(ν−=μ+12≥1\nu_{-}=\mu+\tfrac{1}{2}\geq 1) is a direct consequence of the vortex
winding while the electron component reaches the origin only forμ=12\mu=\tfrac{1}{2}, wheref+​(0)=J0​(0)=1f_{+}(0)=J_{0}(0)=1.
The deacying into the bulk beyond the core edge is controlled by,κμ≡ξ1′​(xc)​(kF​Δ∞/2​EF)=sin⁡ηcπ​ξ\kappa_{\mu}\equiv\xi_{1}^{\prime}(x_{c})(k_{\mathrm{F}}\Delta_{\infty}/2E_{\mathrm{F}})=\frac{\sin\eta_{c}}{\pi\xi}\,(13)

From the panel (c), the CdGM modes
decay on the scaleπ​ξ\pi\xiand the weaklyμ\mu-dependent functionsin⁡ηc\sin\eta_{c}.
The inset of Fig.1(d) plotsξ1′​(xc)=12​sin⁡ηc\xi_{1}^{\prime}(x_{c})=\tfrac{1}{2}\sin\eta_{c}andηc/π\eta_{c}/\piagainstμ/N\mu/N,
confirming thatκμ​ξ\kappa_{\mu}\xistays near1/π1/\piacross most of the
ladder and departs appreciably only forμ/N≳0.7\mu/N\gtrsim 0.7.
The spread in
outer decay rates is illustrated in Figs.1(c)
and (d): panel (c) shows the hole-component WKB envelope±2/π​kF​r​e−κμ​(r−ξ)\pm\sqrt{2/\pi k_{\mathrm{F}}r}\,e^{-\kappa_{\mu}(r-\xi)}for two representative
modes just past the core edge, while panel (d) extends the comparison
to five modes acrossξ≤r≤30​ξ≈λL\xi\leq r\leq 30\xi\approx\lambda_{L}.
Those characters of the CdGM modes
are crucial for the discussion of normalization constant.Figure 1:CdGM bound-state wavefunctions computed withkF=1k_{\mathrm{F}}=1,m=12m=\tfrac{1}{2},Δ/EF=0.01\Delta/E_{\mathrm{F}}=0.01, givingξ≈63.7​kF−1\xi\approx 63.7\,k_{\mathrm{F}}^{-1}andN≡kF​ξ≈63.7N\equiv k_{\mathrm{F}}\xi\approx 63.7modes.(a)Electron (f+f_{+}, solid blue) and hole (f−f_{-}, solid red)
components alongside the BKJT inner approximation (dashed) forμ=5.5\mu=5.5(rt/ξ=0.086r_{t}/\xi=0.086).
The classically forbidden regionr<rtr<r_{t}is shaded grey; the turning
point (dotted vertical) lies deep inside the core.
The exact Bessel and BKJT solutions overlap closely over most of the
classically allowed region[28].(b)Same forμ=55.5\mu=55.5(rt/ξ=0.867r_{t}/\xi=0.867).
The viewing window crosses the core edger=ξr=\xi(vertical dashed
line); forr>ξr>\xithe Taylor-linearized outer BKJT solution is
appended (dashed curves).
The large forbidden region leaves only a narrow classically allowed
inner interval, and the electron and hole envelopes separate
immediately pastr=ξr=\xias the gap turns on.(c)Hole componentf−f_{-}in the outer regionr>ξr>\xifor
two representative modes (faint curves), with the WKB amplitude
envelopes shown prominently (thick curves).
The inner WKB envelope±2/π​kF​r\pm\sqrt{2/\pi k_{\mathrm{F}}r}(grey) is displayed
for one period inside the core; the outer envelopes±2/π​kF​r​e−κμ​(r−ξ)\pm\sqrt{2/\pi k_{\mathrm{F}}r}\,e^{-\kappa_{\mu}(r-\xi)}(colored) separate
immediately at the core edge because the decay rateκμ=12​sin⁡ηc⋅kF​Δ/EF\kappa_{\mu}=\tfrac{1}{2}\sin\eta_{c}\cdot k_{\mathrm{F}}\Delta/E_{\mathrm{F}}is larger for
the low-lying mode (μ/N=0.16\mu/N=0.16,sin⁡ηc≈1\sin\eta_{c}\approx 1, navy
envelope) than for the high-lying mode (μ/N=0.87\mu/N=0.87,sin⁡ηc≈0.71\sin\eta_{c}\approx 0.71, brown envelope).(d)Normalized outer envelopesA​(r)=e−κμ​(r−ξ)​ξ/rA(r)=e^{-\kappa_{\mu}(r-\xi)}\sqrt{\xi/r}for five modes spanningμ/N=0.09\mu/N=0.09–0.950.95, plotted out to30​ξ≈λL30\xi\approx\lambda_{L}.
Low-μ\mumodes are confined within a few coherence lengths of the
core, while the highest mode barely decays over the entire London
length, illustrating the order-of-magnitude variation inκμ\kappa_{\mu}across the CdGM ladder.Inset: outer-decay coefficientξ1′​(xc)=12​sin⁡ηc\xi_{1}^{\prime}(x_{c})=\tfrac{1}{2}\sin\eta_{c}(solid blue) and normalized
phaseηc/π\eta_{c}/\pi(dotted orange) versusμ/N\mu/N.
The horizontal dashed line marks the exact low-μ\mulimitξ1′=12\xi_{1}^{\prime}=\tfrac{1}{2}, corresponding toκμ​ξ=1/π\kappa_{\mu}\xi=1/\pi; vertical dashed lines indicate the five
modes shown in the main panel, demonstrating thatκμ​ξ\kappa_{\mu}\xistays near1/π1/\pifor the majority of the ladder.

## II.2Normalization of the modes

Asμ\muincreases along the ladder, the classically allowed windowξ−rt\xi-r_{t}narrows, which reduces the inner contribution to the norm,
whileκμ\kappa_{\mu}decreases assin⁡ηc→0\sin\eta_{c}\to 0, which increases the
outer contribution. These two trends largely cancel. Approximating
the oscillating integrands by their asymptotic cycle averages,⟨Jν2​(kF​r)⟩→1/(π​kF​r)\langle J_{\nu}^{2}(k_{\mathrm{F}}r)\rangle\to 1/(\pi k_{\mathrm{F}}r)inside and⟨f+2+f−2⟩→2​e−2​κμ​(r−ξ)/(π​kF​r)\langle f_{+}^{2}+f_{-}^{2}\rangle\to 2e^{-2\kappa_{\mu}(r-\xi)}/(\pi k_{\mathrm{F}}r)outside, the normalization integral Eq. (4) splits intoIin​(μ)\displaystyle I_{\mathrm{in}}(\mu)≈2​(ξ−rt)π​kF=2​ξπ​kF​(1−μN),\displaystyle\approx\frac{2(\xi-r_{t})}{\pi k_{\mathrm{F}}}=\frac{2\xi}{\pi k_{\mathrm{F}}}\!\left(1-\frac{\mu}{N}\right),(14)Iout​(μ)\displaystyle I_{\mathrm{out}}(\mu)≈1π​kF​κμ=2​EFπ​kF2​Δ∞​sin⁡ηc.\displaystyle\approx\frac{1}{\pi k_{\mathrm{F}}\kappa_{\mu}}=\frac{2E_{\mathrm{F}}}{\pi k_{\mathrm{F}}^{2}\Delta_{\infty}\sin\eta_{c}}.(15)

Fig.2displays the numerical results for computing the normalization constantCμ2C^{2}_{\mu}along with the analytical estimates. SinceIout>IinI_{\mathrm{out}}>I_{\mathrm{in}}for all modes
[Fig.2(b)], the outer integral dominates1/Cμ21/C_{\mu}^{2}, and its
near-constancy forμ/N≲0.7\mu/N\lesssim 0.7is the chief reason thatCμ2=1/(Iin+Iout)C_{\mu}^{2}=1/(I_{\mathrm{in}}+I_{\mathrm{out}})stays within6%6\%of its mean⟨C2⟩≈9.3×10−3\langle C^{2}\rangle\approx 9.3\times 10^{-3}forμ/N≲0.75\mu/N\lesssim 0.75. Only near the top of the ladder, whereκμ→0\kappa_{\mu}\to 0and the linearized outer solution breaks down, doesCμ2C_{\mu}^{2}deviate noticeably, as Fig.2confirms.Figure 2:Normalization constantCμ2C_{\mu}^{2}and its decomposition into inner and
outer partial integrals, computed withkF=1k_{\mathrm{F}}=1,m=12m=\tfrac{1}{2},Δ/EF=0.01\Delta/E_{\mathrm{F}}=0.01(N≈63.7N\approx 63.7modes).(a)Cμ2C_{\mu}^{2}versusμ/N\mu/N.
The solid blue curve (numerical: exact Bessel inner++Taylor-linearized BKJT outer, integrated to30​ξ30\xi) remains within6%6\%of the mean⟨C2⟩≈9.3×10−3\langle C^{2}\rangle\approx 9.3\times 10^{-3}(dotted line) forμ/N≲0.75\mu/N\lesssim 0.75, confirming the weak dependence
onμ\mu.
The dashed red curve is the WKB analytical estimate(Iin+Iout)−1(I_{\mathrm{in}}+I_{\mathrm{out}})^{-1}from
Eqs. (14)–(15), which captures the qualitative
trend but overestimatesCμ2C_{\mu}^{2}at intermediateμ\mubecause the WKB
cycle average underestimatesIinI_{\mathrm{in}}by neglecting the Bessel
function’s exponentially small tail in the classically forbidden
regionr<rtr<r_{t}.
Both curves drop sharply forμ/N≳0.8\mu/N\gtrsim 0.8asκμ→0\kappa_{\mu}\to 0and the outer wavefunction ceases to be normalizable within30​ξ30\xi.(b)Partial integralsIinI_{\mathrm{in}}(blue, decreasing) andIoutI_{\mathrm{out}}(red, increasing) versusμ/N\mu/N, alongside the WKB
analytical estimates (dashed,
Eqs. (14)–(15)).
The solid black curve is the totalIin+Iout=1/Cμ2I_{\mathrm{in}}+I_{\mathrm{out}}=1/C_{\mu}^{2},
which is nearly flat forμ/N≲0.75\mu/N\lesssim 0.75, making the cancellation
mechanism directly visible.
The analyticalIinI_{\mathrm{in}}lies below the numerical values
(dashed vs. solid blue) because the WKB average ignores the
non-negligible contribution of the exponentially decaying Bessel tail
in the forbidden region.

## IIICharge density profile

## III.1Mode sum inside the core

WithCμ2C_{\mu}^{2}nearly constant andk−≈kFk_{-}\approx k_{\mathrm{F}}(valid to leading
order inΔ∞/EF\Delta_{\infty}/E_{\mathrm{F}}), the in-core density sum
Eq. (2) reduces toδ​n​(r<ξ)⟨C2⟩=2​∑μ=1/2N−12Jμ+122​(kF​r).\frac{\delta n(r<\xi)}{\langle C^{2}\rangle}=2\sum_{\mu=1/2}^{N-\tfrac{1}{2}}J_{\mu+\tfrac{1}{2}}^{2}(k_{\mathrm{F}}r).(16)

The topological constraintν−=μ+12≥1\nu_{-}=\mu+\tfrac{1}{2}\geq 1excludes theν−=0\nu_{-}=0Bessel channel and enforcesn​(0)=0n(0)=0exactly. For modes withμ≥N+12\mu\geq N+\tfrac{1}{2}the classically forbidden region covers the entire
core, so their contribution at any fixedr<ξr<\xiis negligible and the
sum in Eq. (16) may be extended to infinity.Figure 3:Charge-density perturbationδ​n​(r)\delta n(r)computed withkF=1k_{\mathrm{F}}=1,m=12m=\tfrac{1}{2},Δ/EF=0.01\Delta/E_{\mathrm{F}}=0.01(ξ≈63.7​kF−1\xi\approx 63.7\,k_{\mathrm{F}}^{-1},N≈63N\approx 63modes).
Solid blue: numerical sum2​∑μCμ2​|fμ,−​(r)|22\sum_{\mu}C_{\mu}^{2}|f_{\mu,-}(r)|^{2}over all CdGM hole amplitudes; dashed red: analytical closed form.(a)Inner regionr<ξr<\xi: analytical approximation⟨C2⟩​[1−J02​(kF​r)]\langle C^{2}\rangle[1-J_{0}^{2}(k_{\mathrm{F}}r)][Eq. (18)].
The two curves agree closely; the residual discrepancy reflects the≈6%\approx 6\%mode-to-mode variation ofCμ2C_{\mu}^{2}about its mean⟨C2⟩≈9.3×10−3\langle C^{2}\rangle\approx 9.3\times 10^{-3}[Fig.2(a)].(b)Outer regionr>ξr>\xi: the factored envelope2​⟨C2⟩​ξ/(π​r)​e−2​(r−ξ)/π​ξ2\langle C^{2}\rangle\xi/(\pi r)\,e^{-2(r-\xi)/\pi\xi}[Eq. (22)].
The closed form captures the smooth1/r1/renvelope. Two distinct
effects meet atr=ξr=\xiand should not be conflated: the offset
between the dashed and solid curves there is the∼36%\sim 36\%WKB
artifact of the closed form at the classical turning point, discussed
in the text, whereas the small step in the numerical curve itself
(2.6%2.6\%here) is the discontinuity between the exact-Bessel inner and
BKJT outer constructions[27].
In both panels the bound-state density is positive definite;
sign-alternating oscillations appear only in the screened charge, after
the Poisson equation is solved.

Equation (16) is a partial Bessel–Parseval sum.
Applying the completeness identityJ02​(x)+2​∑ν=1∞Jν2​(x)=1,J_{0}^{2}(x)+2\sum_{\nu=1}^{\infty}J_{\nu}^{2}(x)=1,(17)

which follows from Parseval’s theorem applied to the generating
functionei​x​sin⁡θ=∑νJν​(x)​ei​ν​θe^{ix\sin\theta}=\sum_{\nu}J_{\nu}(x)e^{i\nu\theta}[29],
the topologically missingν−=0\nu_{-}=0term immediately yields the central
result forr<ξr<\xi:δ​n​(r<ξ)⟨C2⟩≈1−J02(kFr).\boxed{\frac{\delta n(r<\xi)}{\langle C^{2}\rangle}\approx 1-J_{0}^{2}(k_{\mathrm{F}}r).}(18)

This satisfiesn​(0)=0n(0)=0by construction and evaluates toδ​n​(ξ−)/⟨C2⟩=1−J02​(2​EF/π​Δ∞)≈1\delta n(\xi^{-})/\langle C^{2}\rangle=1-J_{0}^{2}(2E_{\mathrm{F}}/\pi\Delta_{\infty})\approx 1at the core edge in the weak-coupling limit. The point worth
emphasizing is that two physically motivated simplifications—constantCμ2C_{\mu}^{2}andk−≈kFk_{-}\approx k_{\mathrm{F}}—are exactly what is needed to bring an
exact mathematical identity into play, collapsing an otherwise
intractable finite Bessel sum into a single closed form.
Figure3(a) tests Eq. (18) against the full
numerical CdGM sum; the two curves agree closely throughout the core.
The density is positive definite everywhere, being a sum of squared
amplitudes with positive weightsCμ2>0C_{\mu}^{2}>0; sign reversal appears
only in thescreenedcharge, after the Poisson equation is
solved.

Two limiting forms of Eq. (18) are instructive. Near the
vortex axis (r≪1/kFr\ll 1/k_{\mathrm{F}}), expandingJ0​(x)=1−x2/4+⋯J_{0}(x)=1-x^{2}/4+\cdotsgives the quadratic onsetδ​n/⟨C2⟩≈(kF​r)2/4\delta n/\langle C^{2}\rangle\approx(k_{\mathrm{F}}r)^{2}/4, which
is invisible to any coarse-grained probe. Over most of the core
interior (r≲0.85​ξr\lesssim 0.85\,\xi), the large-argument asymptoticsJ0​(x)∼2/(π​x)​cos⁡(x−π/4)J_{0}(x)\sim\sqrt{2/(\pi x)}\cos(x-\pi/4)give oscillations at
wavevector2​kF2k_{\mathrm{F}},δ​n​(r)⟨C2⟩≈1−1π​kF​r−sin⁡(2​kF​r)π​kF​r,\frac{\delta n(r)}{\langle C^{2}\rangle}\approx 1-\frac{1}{\pi k_{\mathrm{F}}r}-\frac{\sin(2k_{\mathrm{F}}r)}{\pi k_{\mathrm{F}}r},(19)

in which the smooth background and the oscillation carry equal weight.

## III.2Outside the core

Forr>ξr>\xithe hole amplitude is given by the Taylor-linearized BKJT
outer solution, Eqs. (9)–(10),fμ,−​(r)∝e−κμ​r​[cos⁡(ημ/2)​Jμ​(kF​r)+sin⁡(ημ/2)​Yμ​(kF​r)],f_{\mu,-}(r)\propto e^{-\kappa_{\mu}r}\bigl[\cos(\eta_{\mu}/2)\,J_{\mu}(k_{\mathrm{F}}r)+\sin(\eta_{\mu}/2)\,Y_{\mu}(k_{\mathrm{F}}r)\bigr],(20)

withκμ\kappa_{\mu}from Eq. (13). Squaring and applying
the large-argument Bessel forms leaves a common exponential envelope
multiplying a smooth term∝1/kF​r\propto 1/k_{\mathrm{F}}rand a term oscillating at2​kF2k_{\mathrm{F}}.

Becauseμ\muis half-integer, adjacent modes enter the oscillating
term with opposite signs and the mode sum largely cancels it. The
cancellation is substantial but incomplete, sinceκμ\kappa_{\mu}and the
mixing angle both drift along the ladder: a2​kF2k_{\mathrm{F}}ripple survives past
the core edge and decays over a few coherence lengths. What follows is
therefore the smooth envelope of the outer density, with the ripple
riding on it, as Fig.3(b) shows.

ReplacingCμ2C_{\mu}^{2}by its mode average leaves a sum over envelopes
alone,δ​n​(r>ξ)≃2​⟨C2⟩π​kF​r​∑μe−2​κμ​(r−ξ).\delta n(r>\xi)\simeq\frac{2\langle C^{2}\rangle}{\pi k_{\mathrm{F}}r}\sum_{\mu}e^{-2\kappa_{\mu}(r-\xi)}\>.(21)

From above expression, it can be seen that the mode indexμ\muonly enterssin⁡ηc\sin\eta_{c}in the decaying factorκμ\kappa_{\mu}in Eq.(13). Over the bulk of the
ladder it stays close to unity:κμ​π​ξ\kappa_{\mu}\pi\xiruns from11atμ=12\mu=\tfrac{1}{2}down to0.260.26at the top, so all but the last few modes decay
at nearly the same rate. The sum therefore factorises, leaving a
common exponential,δ​n​(r>ξ)≃2​⟨C2⟩​ξπ​r​e−2​(r−ξ)/π​ξ,\delta n(r>\xi)\;\simeq\;\frac{2\langle C^{2}\rangle\xi}{\pi r}\,e^{-2(r-\xi)/\pi\xi},(22)

a1/r1/renvelope falling on the scaleπ​ξ/2\pi\xi/2. This is the whole
of what the outer region contributes qualitatively: the bound-state
charge is not confined tor<ξr<\xibut leaks out over roughly a
coherence length.

At the edge Eq. (22) returns2​⟨C2⟩/π2\langle C^{2}\rangle/\pi,
about a third below the inner boundary value⟨C2⟩\langle C^{2}\rangle. The shortfall belongs to the closed form
rather than to the mode sum: the large-argument expansion discards the
turning-point enhancement ofJμJ_{\mu}andYμY_{\mu}, which is largest for
precisely the high-μ\mumodes that dominate atr≃ξr\simeq\xi. It is
unrelated to, and much larger than, the step carried by the numerical
sum itself[27].

In passing, the amount of charge carried by the vortex is computed
quite differently from the consideration of mass merons/Skyrmions in two-dimensional Dirac fermion systems
in which the topological objects are formed by the elementary vortex carrying1/21/2net electron and the total
charge is determined by the representation of the involved order parameters[30].

## IVElectrostatics of the core charge

## IV.1The source term

Far from the core the electron density is that of a uniform
superconductor,n=2​Nμ​[EF+Δ24​EF],n=2N_{\mu}\Bigl[E_{\mathrm{F}}+\frac{\Delta^{2}}{4E_{\mathrm{F}}}\Bigr],(23)

with2​Nμ2N_{\mu}the density of states[17]. The
ionic background is rigid and cancels this exactly, so the vortex
problem is one of deviations. Writingδ​ntotal\delta n_{\rm total}for the
departure from Eq. (23), the ions never appear again,
andδ​ntotal\delta n_{\rm total}is the charge a local probe would measure.
It is the source of Poisson’s equation in its bare form,∇2ϕ=−4​π​eε​δ​ntotal.\nabla^{2}\phi=-\frac{4\pi e}{\varepsilon}\,\delta n_{\rm total}.(24)

Equation (23) already fixes one contribution. Inside the vortex core
the gap is suppressed so the density falls by2​Nμ​Δ2/4​EF=14​n​(Δ/EF)22N_{\mu}\Delta^{2}/4E_{\mathrm{F}}=\tfrac{1}{4}n(\Delta/E_{\mathrm{F}})^{2},
leaving the core positively charged
as the charged-vortex picture
requires[18].
Since Eq. (23)
depends on position only throughΔ​(r)\Delta(r), which varies on the scaleξ\xi, it only contributes smooth variation in charge density. All rapid variation of the
density must therefore come from the bound states.
The bound-state share is given by Eqs. (18)
and (22). It is positive definite at every radius, being a
sum of squared hole amplitudes with positive weightsCμ2>0C_{\mu}^{2}>0.

The remaining piece ofδ​ntotal\delta n_{\rm total}is the response of the
density in Eq.23to the potential they generate. Following
Ref.[19]this is(∂n/∂EF)​e​ϕ(\partial n/\partial E_{\mathrm{F}})e\phi,
which is Thomas–Fermi screening:kTF2=4​π​e2​(∂n/∂μ)/εk_{\mathrm{TF}}^{2}=4\pi e^{2}(\partial n/\partial\mu)/\varepsilon. Moving it to the left-hand
side of Eq. (24) gives the screened form(∇2−kTF2)​ϕ​(r)=−4​π​eε​δ​nbound​(r),\bigl(\nabla^{2}-k_{\mathrm{TF}}^{2}\bigr)\phi(r)=-\frac{4\pi e}{\varepsilon}\,\delta n_{\rm bound}(r),(25)

withδ​ntotal=δ​nbound−(ε​kTF2/4​π​e)​ϕ\delta n_{\rm total}=\delta n_{\rm bound}-(\varepsilon k_{\mathrm{TF}}^{2}/4\pi e)\phi. The two equations are one, written
either with the measured charge as source or with the bound-state part
alone.

## IV.2Screened response

The operator on the left of Eq. (25) is a low-pass
filter. In momentum space its
inverse is1/(q2+kTF2)1/(q^{2}+k_{\mathrm{TF}}^{2}): a response of strength1/kTF21/k_{\mathrm{TF}}^{2}atq→0q\to 0, falling off beyond the cutoffq∼kTFq\sim k_{\mathrm{TF}}. Consequentlyϕ\phireproduces the source profile itself, divided bykTF2k_{\mathrm{TF}}^{2},
wherever the source varies slowly on the scale1/kTF1/k_{\mathrm{TF}}, and smooths
any feature sharper than that. This is the entire content of the
screening problem, and it is what makes the answer elementary.

Inside the core the source is, from Eq. (18),δ​nbound=⟨C2⟩​[1−J02​(kF​r)]\delta n_{\rm bound}=\langle C^{2}\rangle[1-J_{0}^{2}(k_{\mathrm{F}}r)], and forkF​r≫1k_{\mathrm{F}}r\gg 1the Bessel asymptotics separate it into two pieces of
sharply different character,δ​nbound≃⟨C2⟩​[1−1π​kF​r⏟smooth−sin⁡2​kF​rπ​kF​r⏟2​kF​ripple].\delta n_{\rm bound}\;\simeq\;\langle C^{2}\rangle\Bigl[\underbrace{1-\tfrac{1}{\pi k_{\mathrm{F}}r}}_{\text{smooth}}\;-\;\underbrace{\tfrac{\sin 2k_{\mathrm{F}}r}{\pi k_{\mathrm{F}}r}}_{2k_{\mathrm{F}}\ \text{ripple}}\Bigr].(26)

The smooth part varies on the scalerr; the ripple oscillates atq=2​kFq=2k_{\mathrm{F}}. Each drives its own response, and the responses inherit therr-dependence of the terms that drive them. Solving
Eq. (25) for each in turn—so that∇2\nabla^{2}acting
on the smooth response may be dropped, while on the oscillating one∇2sin⁡2​kF​r=−4​kF2​sin⁡2​kF​r\nabla^{2}\sin 2k_{\mathrm{F}}r=-4k_{\mathrm{F}}^{2}\sin 2k_{\mathrm{F}}r—gives directlyϕ​(r)≃4​π​e​⟨C2⟩ε​{1kTF2−1π​kF​r​[1kTF2+sin⁡2​kF​r4​kF2+kTF2]},\phi(r)\;\simeq\;\frac{4\pi e\langle C^{2}\rangle}{\varepsilon}\left\{\frac{1}{k_{\mathrm{TF}}^{2}}-\frac{1}{\pi k_{\mathrm{F}}r}\left[\frac{1}{k_{\mathrm{TF}}^{2}}+\frac{\sin 2k_{\mathrm{F}}r}{4k_{\mathrm{F}}^{2}+k_{\mathrm{TF}}^{2}}\right]\right\},(27)

for1kF≪r≲ξ\tfrac{1}{k_{\mathrm{F}}}\ll r\lesssim\xi.
Each of the three terms of Eq. (26) is simply divided byq2+kTF2q^{2}+k_{\mathrm{TF}}^{2}at its own wavevector—kTF2k_{\mathrm{TF}}^{2}for the first two,4​kF2+kTF24k_{\mathrm{F}}^{2}+k_{\mathrm{TF}}^{2}for the ripple—so every response carries the sign
of the source that produced it. The constant is not a spectator: it is
the response to the uniform part of the bound charge, and it is what
removes that charge from the screened total below.
The replacement∇2→−4​kF2\nabla^{2}\to-4k_{\mathrm{F}}^{2}is not exact, sincesin⁡(2​kF​r)/r\sin(2k_{\mathrm{F}}r)/ris not an eigenfunction of the radial Laplacian. The
leading correction is in quadrature with the term it corrects, so it
shifts the phase at order(kF​r)−1(k_{\mathrm{F}}r)^{-1}but the amplitude only at
order(kF​r)−2(k_{\mathrm{F}}r)^{-2}[26].

The lower limit onrris enforced twice over. The separation
(26) is itself asymptotic: asr→0r\to 0the bound-state
density vanishes as12​(kF​r)2\tfrac{1}{2}(k_{\mathrm{F}}r)^{2}, while the1/π​kF​r1/\pi k_{\mathrm{F}}rterms
that represent it diverge. Independently, dropping∇2\nabla^{2}from
the smooth response requires the source to vary slowly on the screening
length, which fails whereδ​nbound\delta n_{\rm bound}turns over on the
scalekF−1k_{\mathrm{F}}^{-1}. BecausekTFk_{\mathrm{TF}}andkFk_{\mathrm{F}}are comparable in a metal
the two conditions bite at the same radius[26].Figure 4:Screening of the CdGM charge, computed withkF=1k_{\mathrm{F}}=1,Δ/EF=0.01\Delta/E_{\mathrm{F}}=0.01(kF​ξ≈64k_{\mathrm{F}}\xi\approx 64), using thenumericalmode sum2​∑μCμ2​|fμ,−|22\sum_{\mu}C_{\mu}^{2}|f_{\mu,-}|^{2}as the source rather than the
closed forms.(a)The bare bound-state density (black) is positive definite
and carries a net charge; the screened totalδ​nbound−kTF2​ϕ\delta n_{\rm bound}-k_{\mathrm{TF}}^{2}\phi(red) carries none and alternates
in sign. Screening removes the net charge and leaves the ripple.(b)The surviving charge against the closed form of
Eq. (28), with no adjustable parameter.(c)The surviving fraction versuskTF/kFk_{\mathrm{TF}}/k_{\mathrm{F}}: curve, the
predicted4​kF2/(4​kF2+kTF2)4k_{\mathrm{F}}^{2}/(4k_{\mathrm{F}}^{2}+k_{\mathrm{TF}}^{2}); open circles, numerical
solution with the analytic sourceJ02​(kF​r)J_{0}^{2}(k_{\mathrm{F}}r); filled squares,
numerical solution with the full numerical CdGM density. The two
symbol sets test the two approximations separately—the closed-form
density and the two-term potential—and agree with the prediction to0.04%0.04\%and1%1\%respectively. The latter offset is the
mode-average⟨C2⟩\langle C^{2}\ranglestanding in for aμ\mu-dependentCμ2C_{\mu}^{2}.

## IV.3The surviving charge

The screened charge now follows without further work. Inserting
Eq. (27) intoδ​ntotal=δ​nbound−(ε​kTF2/4​π​e)​ϕ\delta n_{\rm total}=\delta n_{\rm bound}-(\varepsilon k_{\mathrm{TF}}^{2}/4\pi e)\phi,
the smooth parts cancel identically
while the ripple survives with a reduced weight,δ​ntotal​(r)≃−⟨C2⟩​4​kF24​kF2+kTF2​sin⁡2​kF​rπ​kF​r\delta n_{\rm total}(r)\;\simeq\;-\,\langle C^{2}\rangle\,\frac{4k_{\mathrm{F}}^{2}}{4k_{\mathrm{F}}^{2}+k_{\mathrm{TF}}^{2}}\;\frac{\sin 2k_{\mathrm{F}}r}{\pi k_{\mathrm{F}}r}(28)

in the window1/kF≪r≲ξ1/k_{\mathrm{F}}\ll r\lesssim\xi. The physical content is a
single statement: Thomas–Fermi screening neutralises charge completely
at long wavelength but is ineffective at the largest momentum transfer
the Fermi surface allows, so the2​kF2k_{\mathrm{F}}component of the bound-state
charge is the only part that is not compensated. The factor4​kF2/(4​kF2+kTF2)4k_{\mathrm{F}}^{2}/(4k_{\mathrm{F}}^{2}+k_{\mathrm{TF}}^{2})is the fraction that escapes, and it is
bounded below for any metal. In the free-electron estimatekTF/kF=0.815​rs/aBk_{\mathrm{TF}}/k_{\mathrm{F}}=0.815\sqrt{r_{s}/a_{\rm B}}, and the density parameterrs/aBr_{s}/a_{\rm B}lies between roughly two and six across the metallic
range[31], sokTF/kFk_{\mathrm{TF}}/k_{\mathrm{F}}is confined to about1.21.2–2.02.0and the surviving fraction to between three-quarters and
one-half. The2​kF2k_{\mathrm{F}}modulation can therefore be neither screened away
nor enhanced: it is a fixed fraction of order unity of the bare
bound-state ripple, whatever the material. This insensitivity is a
direct consequence ofkTFk_{\mathrm{TF}}andkFk_{\mathrm{F}}being set by the same electron
density.

Figure4tests this against direct numerical solution
of Eq. (25). Two independent approximations are involved
and are checked separately. Using the closed-form sourceJ02​(kF​r)J_{0}^{2}(k_{\mathrm{F}}r)isolates the two-term potential
Eq. (27), which reproduces the predicted suppression
to0.04%0.04\%over0.25≤kTF/kF≤30.25\leq k_{\mathrm{TF}}/k_{\mathrm{F}}\leq 3. Using instead the full
numerical mode sum—exact Bessel functions inside the core, matched
BKJT amplitudes outside, and theμ\mu-dependentCμ2C_{\mu}^{2}—tests
the closed-form density as well, and reproduces it to1%1\%, the
residual being the mode-average⟨C2⟩\langle C^{2}\rangle. The solver
itself was verified against three problems with known closed-form
solutions and by two independent solution methods.

## VDiscussion

It is worth separating this mechanism from the one that produces
Friedel oscillations around an impurity, since the two give the same
periodicity by opposite routes. There the source is structureless—a
point charge, flat inqq, as in the classic treatment of an impurity
in a superconductor[32]—and the oscillation is generated
entirely by the response, through the non-analyticity of the static Lindhard
function atq=2​kFq=2k_{\mathrm{F}}. Recovering the real-space decay in that case is
delicate: it rests on the behaviour of the transform near the
singularity, and is obtained by Lighthill’s theorem[33],
with the decay exponent fixed by
the order of the non-analyticity[24,34,35].
Here the roles are exchanged. The response is Thomas–Fermi and
carries no structure whatever, while the source itself is peaked at2​kF2k_{\mathrm{F}}. Both routes lead to the same wavevector for the same reason,
that2​kF2k_{\mathrm{F}}is the largest momentum the Fermi surface can supply, but
only in the present case is the oscillation already present in the
charge that is being screened. That is what allows the elementary
treatment above: no property of the dielectric function beyond its
value at two wavevectors is required.

The two routes leave different fingerprints in the amplitude. When
the oscillation comes from the response, it originates in the
derivative of1/ε​(q)1/\varepsilon(q)at the singular point and the
amplitude therefore carries the transfer functionsquared;
Stern’s result for a point charge in two dimensions has precisely this
form,[2​kF/(2​kF+kTF)]2\bigl[2k_{\mathrm{F}}/(2k_{\mathrm{F}}+k_{\mathrm{TF}})\bigr]^{2}in the present
notation[34]. Here the oscillation is filtered
once rather than differentiated, and the transfer function appears to
the first power.

The quantity of focus here is the density—a sum of squared amplitudes over
occupied states—rather than a spectral function or a Green’s
function.
Density is one of the primary variables of
density-functional theory, including its extension to the
superconducting state[36], and closed-form results for it are
scarce even in one dimension, as the calculations cited in
Sec.Iillustrate.
Equations (18) and (22) provide the
corresponding statement for a vortex core, a geometry in which the
density varies on the scalekF−1k_{\mathrm{F}}^{-1}and local-density
approximations are therefore least reliable. Self-consistent numerical
treatments of this geometry exist[37], but without
an analytic density there has been nothing to check them against. Whether a functional can
reproduce a density that vanishes at the origin for topological reasons
and oscillates at2​kF2k_{\mathrm{F}}thereafter seems a natural test, and one that
does not require solving the pairing problem self-consistently.

Equation (28) is the analytical counterpart of
the sign change reported numerically by Machida and
Koyama[21]. Their Fig. 1(b) contrastsρ​(r)−ρ∞\rho(r)-\rho_{\infty}computed with and without the Poisson equation
and finds sign alternation only in the charged case, i.e.e≠0e\neq 0, with the
oscillation periodπ/kF\pi/k_{\mathrm{F}}and an amplitude that decreases with
increasingkF​ξk_{\mathrm{F}}\xi. All three features follow from
Eq. (28): the period is set by2​kF2k_{\mathrm{F}}; the
alternation follows from neutrality; and since⟨C2⟩∝(kF​ξ)−1\langle C^{2}\rangle\propto(k_{\mathrm{F}}\xi)^{-1}, the amplitude scales as(kF​ξ​kF​r)−1(k_{\mathrm{F}}\xi\,k_{\mathrm{F}}r)^{-1}, which we have verified numerically betweenkF​ξ=10k_{\mathrm{F}}\xi=10and6464. Their remark that “simple screening of the
Thomas–Fermi type does not work in the vortex state” can be sharpened:
Thomas–Fermi screening does apply, but only its fullqq-dependence;
using theq→0q\to 0limit alone would neutralise the ripple along with
everything else.

The analysis is meant to complement rather than replace self-consistent
BdG calculations such as those of Machida and
Koyama[21]. Self-consistency reshapes the gap
profile and shifts quantitative details, but the mechanism identified
here rests only on a sharp Fermi surface, the exclusion of theν=0\nu=0channel, andkF​ξ≫1k_{\mathrm{F}}\xi\gg 1, and is therefore robust against smooth
deformations ofΔ​(r)\Delta(r). Equations (18),
(22) and (28) accordingly provide an
analytical benchmark against which self-consistent numerical densities
can be checked in the weak-coupling limit.

## VISummary

Under two approximations valid to leading order inΔ/EF\Delta/E_{\mathrm{F}}—a
mode-independent normalisation constant andk−≈kFk_{-}\approx k_{\mathrm{F}}—the
Bessel completeness identity applied to the CdGM hole basis yields the
inner density profile, Eq. (18), while a WKB treatment of
the BKJT amplitude outside the core gives the outer envelope,
Eq. (22). Theν=0\nu=0Bessel
channel is excluded by the vortex winding number, which fixesn​(0)=0n(0)=0exactly within the approximation and imprints2​kF2k_{\mathrm{F}}oscillations on
the core density.

The bound-state charge does not integrate to zero, so overall
neutrality requires the extended states to compensate it exactly. That compensation is complete at long wavelength but
ineffective atq=2​kFq=2k_{\mathrm{F}}, and the residue is the screened charge of
Eq. (28): a sign-alternating2​kF2k_{\mathrm{F}}oscillation of
amplitude4​kF2/(4​kF2+kTF2)4k_{\mathrm{F}}^{2}/(4k_{\mathrm{F}}^{2}+k_{\mathrm{TF}}^{2})relative to the bare ripple.
Direct numerical solution of the Poisson equation with the full CdGM
mode sum as source confirms this to better than1%1\%. Natural extensions includedd-wave pairing, finite temperature, and multi-band Fermi surfaces.

## References
- [1]C. Caroli, P.G. De Gennes, and J. Matricon.Bound fermion states on a vortex line in a type ii superconductor.Physics Letters, 9(4):307–309, 1964.
- [2]M. T. Deng, Carlos Payá, Pablo San-Jose, Elsa Prada, C. M. Marcus, and
S. Vaitiekėnas.Caroli–de Gennes–Matricon analogs in full-shell hybrid nanowires.Phys. Rev. Lett., 134:206302, May 2025.
- [3]Masatoshi Sato and Yoichi Ando.Topological superconductors: a review.Reports on Progress in Physics, 80(7):076501, may 2017.
- [4]N. B. Kopnin and M. M. Salomaa.Mutual friction in superfluidHe3{}^{3}\mathrm{He}: Effects of bound
states in the vortex core.Phys. Rev. B, 44:9667–9677, Nov 1991.
- [5]Chi-Ken Lu and Sungkit Yip.Zero-energy vortex bound states in noncentrosymmetric
superconductors.Phys. Rev. B, 78:132502, Oct 2008.
- [6]Satoshi Fujimoto.Topological order and non-abelian statistics in noncentrosymmetricss-wave superconductors.Phys. Rev. B, 77:220501(R), Jun 2008.
- [7]Andreas P. Schnyder, Shinsei Ryu, Akira Furusaki, and Andreas W. W. Ludwig.Classification of topological insulators and superconductors in three
spatial dimensions.Phys. Rev. B, 78:195125, Nov 2008.
- [8]Thomas Gozlinski, Qili Li, Rolf Heid, Ryohei Nemoto, Roland Willa, Toyo Kazu
Yamada, Jörg Schmalian, and Wulf Wulfhekel.Band-resolved Caroli–de Gennes–Matricon states of
multiple-flux-quanta vortices in a multiband superconductor.Science Advances, 9(36):eadh9163, 2023.
- [9]Mingyang Chen, Xiaoyu Chen, Huan Yang, Zengyi Du, Xiyu Zhu, Enyu Wang, and
Hai-Hu Wen.Discrete energy levels of Caroli-de Gennes-Matricon states in
quantum limit in fete0.55se0.45.Nature Communications, 9(1):970, 2018.
- [10]Ivan Maggio-Aprile, Tejas Parasram Singar, Christophe Berthod, Tim Gazdić,
Jens Bruér, and Christoph Renner.Vortex-core spectroscopy of d-wave cuprate high-temperature
superconductors.Physica C: Superconductivity and its Applications, 615:1354386,
2023.
- [11]Gianni Blatter, Mikhail Feigel’man, Vadim Geshkenbein, Anatoli Larkin, and
Valerii Vinokur.Vortices in high-temperature superconductors.Rev. Mod. Phys., 66:1125–1388, 1994.
- [12]Anne van Otterlo, Mikhail Feigel’man, Vadim Geshkenbein, and Gianni Blatter.Vortex dynamics and the Hall anomaly: A microscopic analysis.Phys. Rev. Lett., 75:3736–3739, Nov 1995.
- [13]N. B. Kopnin.Vortex dynamics and mutual friction in superconductors and Fermi
superfluids.Rep. Prog. Phys., 65(11):1633, 2002.
- [14]Carl M Bender and Steven A Orszag.Advanced mathematical methods for scientists and engineers:
Asymptotic methods and perturbation theory.Springer, 1999.
- [15]John Bardeen, R. Kümmel, A. E. Jacobs, and L. Tewordt.Structure of vortex lines in pure superconductors.Phys. Rev., 187:556–569, Nov 1969.
- [16]D. Van der Marel.Anomalous behaviour of the chemical potential in superconductors with
a low density of charge carriers.Physica C: Superconductivity, 165(1):35–43, 1990.
- [17]Daniil I. Khomskii and Feodor V. Kusmartsev.Charge redistribution and properties of high-temperature
superconductors.Phys. Rev. B, 46:14245–14248, Dec 1992.
- [18]D. I. Khomskii and A. Freimuth.Charged vortices in high temperature superconductors.Phys. Rev. Lett., 75:1384–1386, Aug 1995.
- [19]Gianni Blatter, Mikhail Feigel’man, Vadim Geshkenbein, Anatoli Larkin, and Anne
van Otterlo.Electrostatics of vortices in Type-II superconductors.Phys. Rev. Lett., 77:566–569, Jul 1996.
- [20]Nobuhiko Hayashi, Masanori Ichioka, and Kazushige Machida.Relation between vortex core charge and vortex bound states.Journal of the Physical Society of Japan, 67(10):3368–3371,
1998.
- [21]M. Machida and T. Koyama.Friedel oscillation in charge profile and position dependent
screening around a superconducting vortex core.Phys. Rev. Lett., 90:077003, Feb 2003.
- [22]Xiaoyu Chen, Wen Duan, Xinwei Fan, Wenshan Hong, Kailun Chen, Huan Yang,
Shiliang Li, Huiqian Luo, and Hai-Hu Wen.Friedel oscillations of vortex bound states under extreme quantum
limit inKCa2​Fe4​As4​F2{\mathrm{KCa}}_{2}{\mathrm{Fe}}_{4}{\mathrm{As}}_{4}{\mathrm{F}}_{2}.Phys. Rev. Lett., 126:257002, Jun 2021.
- [23]Keno Riechers, Klaus Hueck, Niclas Luick, Thomas Lompe, and Henning Moritz.Detecting Friedel oscillations in ultracold Fermi gases.The European Physical Journal D, 71(9):232, 2017.
- [24]AM Gabovich, LG Il’Chenko, EA Pashitskiǐ, and Yu A Romanov.Screening of charges and Friedel oscillations of the electron
density in metals having differently shaped fermi surfaces.Soviet Journal of Experimental and Theoretical Physics,
48(124), 1978.
- [25]Raphael F. Ribeiro, Donghyung Lee, Attila Cangi, Peter Elliott, and Kieron
Burke.Corrections to Thomas-Fermi densities at turning points and beyond.Phys. Rev. Lett., 114:050401, Feb 2015.
- [26]See Supplemental Material for the validity of the replacement used to solve the
screened Poisson equation, the verification of the numerical solver against
exactly solvable cases, and an error analysis of the replacement.
- [27]The replacement is not optional. The slow-mode coordinatex​(r)x(r)is imaginary
forr<rtr<r_{t}, so the slow-mode ansatz is undefined throughout the classically
forbidden region, which occupies a fractionμ/N\mu/Nof the core radius—one
half on average over the ladder, and0.990.99for the highest mode. That region
is not negligible: it supplies22–11%11\%ofIinI_{\rm in}for typical modes
and up to76%76\%forμ/N→1\mu/N\to 1. Moreover the BKJT carrier containsYμ​(kρ​r)Y_{\mu}(k_{\rho}r), which diverges asr−μr^{-\mu}at the origin, whereas the
physical hole amplitude must vanish asrμ+1/2r^{\mu+1/2}—the behaviour that
enforcesn​(0)=0n(0)=0and hence makes the closed-form inner density available at
all. The price is that the inner and outer regions are represented by
different functions, which therefore need not join continuously atr=ξr=\xi;
used consistently on both sides, the BKJT ansatz is continuous there by
construction. Numerically the resulting step inδ​n\delta nis2.6%2.6\%atkF​ξ=64k_{\mathrm{F}}\xi=64and9%9\%atkF​ξ=10k_{\mathrm{F}}\xi=10, confined to a shell of a few percent
ofξ\xiabout the core edge, and no quantitative result of this work is
drawn from that shell. We note also that the single constantCCin the inner
Bessel solutions is a choice: inside the coreΔ=0\Delta=0decouples the two
components, so their amplitudes could be taken independent, and doing so
restores continuity off−f_{-}exactly. We retain the common constant because
the near mode-independence ofC2C^{2}is what makes the closed forms of this
work possible, and relaxing it makesC2​(μ)C^{2}(\mu)more stronglyμ\mu-dependent. More fundamentally, continuity of both spinor components and
their derivatives is four conditions, and these are met automatically only at
the exact eigenvalue, where regularity at the origin and decay at infinity
intersect. Taking the CdGM spectrum as given therefore over-determines the
matching, and some residual is unavoidable within any outer solution carrying
two free constants.
- [28]The exception is the immediate neighbourhood ofrtr_{t}, where the two BKJT
components visibly separate: the hole component dips before turning up while
the electron component rises monotonically. The mixing angle is pinned toη​(rt)=0\eta(r_{t})=0becauseYμ​(kρ​r)Y_{\mu}(k_{\rho}r)is the exponentially growing
solution inside the turning point, so any admixture would destroy regularity
at the origin. It then switches on asη≃(Λ+b−1)​x\eta\simeq(\Lambda+b^{-1})xwithx≃(Δ∞​kρ/Eρ)​2​rt​r−rtx\simeq(\Delta_{\infty}k_{\rho}/E_{\rho})\sqrt{2r_{t}}\sqrt{r-r_{t}}, givingf±​(r)≃Jμ​(kρ​r)∓12​(Λ+b−1)​(Δ∞​kρ​2​rt/Eρ)​r−rt​Yμ​(kρ​rt)f_{\pm}(r)\simeq J_{\mu}(k_{\rho}r)\mp\frac{1}{2}(\Lambda+b^{-1})(\Delta_{\infty}k_{\rho}\sqrt{2r_{t}}/E_{\rho})\sqrt{r-r_{t}}\,Y_{\mu}(k_{\rho}r_{t}), a correction of infinite slope atrtr_{t}. SinceYμ​(μ)≃−0.775​μ−1/3<0Y_{\mu}(\mu)\simeq-0.775\,\mu^{-1/3}<0whileJμ​(μ)≃0.447​μ−1/3>0J_{\mu}(\mu)\simeq 0.447\,\mu^{-1/3}>0, it pullsf−f_{-}down and pushesf+f_{+}up. Forμ=5.5\mu=5.5:Jμ​(μ)=0.253J_{\mu}(\mu)=0.253,Yμ​(μ)=−0.439Y_{\mu}(\mu)=-0.439, andf−f_{-}dips to0.2250.225nearr−rt≃0.15r-r_{t}\simeq 0.15before recovering. The exact solutions
show no such feature; this is the BKJT ansatz failing at the centrifugal
turning point, and is why the inner carrier is replaced by exact Bessel
functions.
- [29]NIST digital library of mathematical functions.https://dlmf.nist.gov/.Release 1.2.4 of 2025-03-15; F. W. J. Olver, A. B. Olde Daalhuis,
D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller,
B. V. Saunders, H. S. Cohl, and M. A. McClain, eds.
- [30]Chi-Ken Lu and Igor F. Herbut.Zero modes and charged Skyrmions in graphene bilayer.Phys. Rev. Lett., 108:266402, Jun 2012.
- [31]N.W. Ashcroft and N.D. Mermin.Solid State Physics.HRW international editions. Holt, Rinehart and Winston, 1976.
- [32]Alexander L. Fetter.Spherical impurity in an infinite superconductor.Phys. Rev., 140:A1921–A1936, Dec 1965.
- [33]Michael J Lighthill.An introduction to Fourier analysis and generalised functions.Cambridge University Press, 1958.
- [34]Frank Stern.Polarizability of a two-dimensional electron gas.Phys. Rev. Lett., 18:546–548, Apr 1967.
- [35]Chi-Ken Lu.Friedel oscillation near a van Hove singularity in
two-dimensional Dirac materials.Journal of Physics: Condensed Matter, 28(6):065001, jan 2016.
- [36]L. N. Oliveira, E. K. U. Gross, and W. Kohn.Density-functional theory for superconductors.Phys. Rev. Lett., 60:2430–2433, Jun 1988.
- [37]Fran çois Gygi and Michael Schlüter.Self-consistent electronic structure of a vortex line in a type-II
superconductor.Phys. Rev. B, 43:7609–7621, Apr 1991.

Supplemental Material

## S1Validity of the replacement trick in solving screened Poisson equation

The screened Poisson equation of the main text,(∇2−kTF2)​ϕ=−4​π​eε​δ​nbound,\bigl(\nabla^{2}-k_{\mathrm{TF}}^{2}\bigr)\phi=-\frac{4\pi e}{\varepsilon}\,\delta n_{\rm bound},(S1)

is linear, so a source written as a sum is answered by the sum of the
separate responses. ForkF​r≫1k_{\mathrm{F}}r\gg 1the bound-state density separates into a smooth part and a
part oscillating atq=2​kFq=2k_{\mathrm{F}},δ​nbound≃⟨C2⟩​[1−1π​kF​r−sin⁡2​kF​rπ​kF​r].\delta n_{\rm bound}\simeq\langle C^{2}\rangle\Bigl[1-\tfrac{1}{\pi k_{\mathrm{F}}r}-\tfrac{\sin 2k_{\mathrm{F}}r}{\pi k_{\mathrm{F}}r}\Bigr].(S2)

What makes each piece elementary is a single step: where the source
oscillates at wavevectorqq, the corresponding potential is obtained from replacing the
differential operator∇2\nabla^{2}by−q2-q^{2}. As such, the
differential equation collapses to an algebraic one,(q2+kTF2)​ϕq=4​π​eε​δ​nq.\bigl(q^{2}+k_{\mathrm{TF}}^{2}\bigr)\phi_{q}=\frac{4\pi e}{\varepsilon}\,\delta n_{q}.(S3)

For the smooth partq≃0q\simeq 0, so−q2-q^{2}vanishes,∇2\nabla^{2}is simply dropped, and the potential is then the source divided
bykTF2k_{\mathrm{TF}}^{2}.
Adding the two gives the following approximate solution to the screened Poisson equation,ϕ​(r)≃4​π​e​⟨C2⟩ε​{1kTF2−1π​kF​r​[1kTF2+sin⁡2​kF​r4​kF2+kTF2]}.\phi(r)\simeq\frac{4\pi e\langle C^{2}\rangle}{\varepsilon}\left\{\frac{1}{k_{\mathrm{TF}}^{2}}-\frac{1}{\pi k_{\mathrm{F}}r}\left[\frac{1}{k_{\mathrm{TF}}^{2}}+\frac{\sin 2k_{\mathrm{F}}r}{4k_{\mathrm{F}}^{2}+k_{\mathrm{TF}}^{2}}\right]\right\}.(S4)

Obviously, the replacement trick is not exact. The oscillating potential inherits the
formsin⁡(q​r)/r\sin(qr)/rfrom its source, andsin⁡(q​r)/r\sin(qr)/ris not an
eigenfunction of the radial Laplacian. To see the validity of the replacement trick,
we differentiateei​q​r/re^{iqr}/rand get,(∇2−kTF2)​(ei​q​rr)=−(q2+kTF2+i​qr−1r2)​(ei​q​rr).(\nabla^{2}-k_{\mathrm{TF}}^{2})\!\left(\frac{e^{iqr}}{r}\right)=-\Bigl(q^{2}+k_{\mathrm{TF}}^{2}+\frac{iq}{r}-\frac{1}{r^{2}}\Bigr)\left(\frac{e^{iqr}}{r}\right).(S5)

The trick keeps the constantq2+kTF2q^{2}+k_{\mathrm{TF}}^{2}in the parentheses and
discardsi​q/r−1/r2iq/r-1/r^{2}, so one criterion covers both cases,|i​qr−1r2|≪q2+kTF2.\left|\frac{iq}{r}-\frac{1}{r^{2}}\right|\;\ll\;q^{2}+k_{\mathrm{TF}}^{2}.(S6)

(i) For the ripple,q=2​kFq=2k_{\mathrm{F}}dominates the right-hand side andq/rq/rthe left, so the condition isq​r≫1qr\gg 1.
(ii) For the smooth part,q=0q=0annihilatesq2q^{2}andi​q/riq/rtogether, leaving1/r2≪kTF21/r^{2}\ll k_{\mathrm{TF}}^{2},
that iskTF​r≫1k_{\mathrm{TF}}r\gg 1.

## S2Validation for numerical solver

The mode sum is evaluated with the exact inner Bessel solutions and the
Taylor-linearised BKJT outer solution, withCμ2C_{\mu}^{2}obtained by
quadrature to30​ξ30\xi. The screened Poisson equation is solved on a
uniform radial grid by a second-order finite-difference scheme withϕ′​(0)=0\phi^{\prime}(0)=0andϕ→0\phi\to 0at the outer boundary.

In order to validate the numerical solver for screened Poisson equation, we shall
consider a simple example for which the closed-form solution is available. Moreover, we
can also check if the numerical results agree with the solutions obtained from the replacement trick.
Assume the source of charge is a uniform disc,S=S0​Θ​(a−r)S=S_{0}\Theta(a-r). A constant particular
solution together withI0I_{0}inside andK0K_{0}outside, matched in
value and slope atr=ar=a, givesϕin\displaystyle\phi_{\rm in}=S0kTF2−S0​a​K1​(kTF​a)kTF​I0​(kTF​r),\displaystyle=\frac{S_{0}}{k_{\mathrm{TF}}^{2}}-\frac{S_{0}aK_{1}(k_{\mathrm{TF}}a)}{k_{\mathrm{TF}}}\,I_{0}(k_{\mathrm{TF}}r),ϕout\displaystyle\phi_{\rm out}=S0​a​I1​(kTF​a)kTF​K0​(kTF​r).\displaystyle=\frac{S_{0}aI_{1}(k_{\mathrm{TF}}a)}{k_{\mathrm{TF}}}\,K_{0}(k_{\mathrm{TF}}r).(S7)

On the other hand, we can apply the replacement trick: treating the stepinsteadas
smooth and setting∇2→0\nabla^{2}\to 0gives at onceϕ=S0kTF2​Θ​(a−r),\phi=\frac{S_{0}}{k_{\mathrm{TF}}^{2}}\,\Theta(a-r)\>,(S8)

namely, the potential simply copies the source.

Fig.S1demonstrates that the numerical solutions match well with the
exact solution for both conditions: in panel (a) where the parameterkTF​a=10k_{\mathrm{TF}}a=10and
panel (b) wherekTF​a=0.3k_{\mathrm{TF}}a=0.3. Thus, the evidence validates the numerical solver for
screened Poisson equation.
Moreover, the solutionϕ\phiobtained from the replacement
trick agrees well with numerical and analytical ones for most of the regions in panel (a)
except for a narrow region of width of about(1/kTF)(1/k_{\mathrm{TF}}).
However, the replacement-trick solution for the case in panel (b) completely fails.
Below, we shall discuss why and where should the replacement trick fail.

Where should this fail? The criterion (S6) is general,
but the conditionkTF​r≫1k_{\mathrm{TF}}r\gg 1drawn from it in
Sec.S1was obtained by evaluating it on the sourcea​ei​q​r/ra\,e^{iqr}/r.
The replacement discards∇2ϕ\nabla^{2}\phiagainstkTF2​ϕk_{\mathrm{TF}}^{2}\phi, and on the trick’s own answer
Eq. (S8) the discarded term vanishesidenticallywhereverϕ\phiis constant, and is
singular atr=ar=a.
The failure is thus confined to the rim, with no condition onrrat all—in
particular none at the centre. Its width follows from the operator
alone: the homogeneous solutions of(∇2−kTF2)​ϕ=0(\nabla^{2}-k_{\mathrm{TF}}^{2})\phi=0vary
ase±kTF​re^{\pm k_{\mathrm{TF}}r}asymptotically, so a mismatch created atr=ar=acan only heal over1/kTF1/k_{\mathrm{TF}}, and the interior error should fall off ase−kTF​(a−r)e^{-k_{\mathrm{TF}}(a-r)}. The exact solution confirms both statements and
supplies the coefficient. Writing it against
Eq. (S8),ϕin​(r)S0/kTF2=1−z​K1​(z)​I0​(kTF​r),\frac{\phi_{\rm in}(r)}{S_{0}/k_{\mathrm{TF}}^{2}}=1-z\,K_{1}(z)\,I_{0}(k_{\mathrm{TF}}r),(S9)

withz≡kTF​az\equiv k_{\mathrm{TF}}a. Equation (S9) is valid inside the disc, so the error made
by Eq. (S8) is
the single productz​K1​(z)​I0​(kTF​r)zK_{1}(z)I_{0}(k_{\mathrm{TF}}r). Two limits settle the
question.Figure S1:The smooth replacement∇2→0\nabla^{2}\to 0tested on a uniform disc, for
which the screened Poisson equation is solvable in closed form,
Eq. (S7). The replacement predicts thatϕ\phicopies
the source, Eq. (S8) (dashed).(a)kTF​a=10k_{\mathrm{TF}}a=10: the prediction holds through the interior and
fails only in a layer of width1/kTF1/k_{\mathrm{TF}}at the rim (shaded), where the
potential passes through exactly half the interior value.(b)kTF​a=0.3k_{\mathrm{TF}}a=0.3: the layer is wider than the disc, and the
replacement overestimates the potential twelvefold at the origin.
Circles are the finite-difference solution, which also serves to verify
the solver against Eq. (S7).

Forz≫1z\gg 1the deviation is exponentially suppressed by the factor,z​K1​(z)∼z​e−z​π/2​zzK_{1}(z)\sim z\,e^{-z}\sqrt{\pi/2z}, and grows only on approaching
the rim, whereI0​(kTF​r)/I0​(z)≃e−kTF​(a−r)I_{0}(k_{\mathrm{TF}}r)/I_{0}(z)\simeq e^{-k_{\mathrm{TF}}(a-r)}. The
error is therefore confined to a boundary layer,1−ϕinS0/kTF2≃12​e−kTF​(a−r),1-\frac{\phi_{\rm in}}{S_{0}/k_{\mathrm{TF}}^{2}}\;\simeq\;\tfrac{1}{2}\,e^{-k_{\mathrm{TF}}(a-r)},(S10)

of width1/kTF1/k_{\mathrm{TF}}: the screening length is the distance over which the
potential can heal a discontinuity in the source.
Everywhere deeper than a few1/kTF1/k_{\mathrm{TF}}inside,
Eq. (S8) is accurate—at the centre itself to2×10−42\times 10^{-4}forz=10z=10, althoughkTF​rk_{\mathrm{TF}}rvanishes there.

Forz≲1z\lesssim 1the same product behaves oppositely. Nowz​K1​(z)→1zK_{1}(z)\to 1andI0​(kTF​r)→1I_{0}(k_{\mathrm{TF}}r)\to 1together, so the right-hand
side of Eq. (S9) approaches zeroeverywhere,
the origin included: the boundary layer is wider than the disc and has
nothing left to be a boundary layer of. The replacement then fails not
by a correction but by an order of magnitude.

## S3Error analysis of the replacement trick

Write any radial function oscillating at wavevectorqqasϕ=Im​[Ψ​(r)​ei​q​r]\phi=\mathrm{Im}\!\left[\Psi(r)e^{iqr}\right], separating a rapid
phase from a slowly varying complex envelopeΨ\Psi. This is the same
device that underlies the BKJT ansatz for the wavefunction, where the
Hankel functionHμ(1)​(kρ​r)H^{(1)}_{\mu}(k_{\rho}r)carries the oscillation and the
spinorg​(x)g(x)the slow variation; here we apply it to the potential.
Using∇2=d2/d​r2+r−1​d/d​r\nabla^{2}=d^{2}/dr^{2}+r^{-1}d/drand(Ψ​ei​q​r)′\displaystyle\bigl(\Psi e^{iqr}\bigr)^{\prime}=(Ψ′+i​q​Ψ)​ei​q​r,\displaystyle=\bigl(\Psi^{\prime}+iq\Psi\bigr)e^{iqr},(S11)(Ψ​ei​q​r)′′\displaystyle\bigl(\Psi e^{iqr}\bigr)^{\prime\prime}=(Ψ′′+2​i​q​Ψ′−q2​Ψ)​ei​q​r,\displaystyle=\bigl(\Psi^{\prime\prime}+2iq\Psi^{\prime}-q^{2}\Psi\bigr)e^{iqr},(S12)

one obtains, exactly,(∇2−kTF2)​ϕ=Im​{ei​q​r​[Ψ′′+(2​i​q+1r)​Ψ′−(q2+kTF2−i​qr)​Ψ]}.\bigl(\nabla^{2}-k_{\mathrm{TF}}^{2}\bigr)\phi\\
=\mathrm{Im}\Bigl\{e^{iqr}\Bigl[\Psi^{\prime\prime}+\Bigl(2iq+\tfrac{1}{r}\Bigr)\Psi^{\prime}-\Bigl(q^{2}+k_{\mathrm{TF}}^{2}-\tfrac{iq}{r}\Bigr)\Psi\Bigr]\Bigr\}.(S13)

Equation (S5) is the special case of
Eq. (S13) withΨ=1/r\Psi=1/randkTF=0k_{\mathrm{TF}}=0: substitutingΨ′=−1/r2\Psi^{\prime}=-1/r^{2},Ψ′′=2/r3\Psi^{\prime\prime}=2/r^{3}gives[1/r3−i​q/r2−q2/r]​ei​q​r\bigl[1/r^{3}-iq/r^{2}-q^{2}/r\bigr]e^{iqr}, whose imaginary part
reproduces Eq. (S5) term by term. The advantage of
Eq. (S13) is thatΨ\Psiis now free: instead of checking
what the operator does to a guessed function, we can solve for the
function the source demands.

Assume that the oscillating part of the source isIm​[a​ei​q​r/r]\mathrm{Im}\!\left[a\,e^{iqr}/r\right], so
Eq. (S13) requiresΨ′′+(2​i​q+1r)​Ψ′−(q2+kTF2−i​qr)​Ψ=−ar.\Psi^{\prime\prime}+\Bigl(2iq+\tfrac{1}{r}\Bigr)\Psi^{\prime}-\Bigl(q^{2}+k_{\mathrm{TF}}^{2}-\tfrac{iq}{r}\Bigr)\Psi=-\frac{a}{r}.(S14)

TryingΨ=A/r\Psi=A/rand usingΨ′=−A/r2\Psi^{\prime}=-A/r^{2},Ψ′′=2​A/r3\Psi^{\prime\prime}=2A/r^{3}, therr-dependence collects into1r2−i​qr−(q2+kTF2)=−aA,\frac{1}{r^{2}}-\frac{iq}{r}-\bigl(q^{2}+k_{\mathrm{TF}}^{2}\bigr)=-\frac{a}{A},(S15)

that isA​(r)=a(q2+kTF2)+i​qr−1r2≃A01+i​ε1−ε2,A(r)=\frac{a}{\bigl(q^{2}+k_{\mathrm{TF}}^{2}\bigr)+\dfrac{iq}{r}-\dfrac{1}{r^{2}}}\;\simeq\;\frac{A_{0}}{1+i\varepsilon_{1}-\varepsilon_{2}},(S16)

with therr-independentA0=a/(q2+kTF2)A_{0}=a/(q^{2}+k_{\mathrm{TF}}^{2})and the
correctionsε1=q/[(q2+kTF2)​r]\varepsilon_{1}=q/[(q^{2}+k_{\mathrm{TF}}^{2})r]andε2=1/[(q2+kTF2)​r2]\varepsilon_{2}=1/[(q^{2}+k_{\mathrm{TF}}^{2})r^{2}], which carry smooth spatial
variation. The denominator of Eq. (S16) is the bracket of
Eq. (S5) itself, andε1,ε2\varepsilon_{1},\varepsilon_{2}are
just its two discarded terms divided by the term retained: this section
solves the same equation that Sec.S1only inspected.
Settingε1=ε2=0\varepsilon_{1}=\varepsilon_{2}=0recovers the result of the
main text.

The two corrections sit at different orders inrr:ε1∼(r)−1\varepsilon_{1}\sim(r)^{-1}whileε2∼(r)−2\varepsilon_{2}\sim(r)^{-2}.
Expanding in powers of1/r1/raccordingly, and discardingε22=𝒪​(r−4)\varepsilon_{2}^{2}=\mathcal{O}(r^{-4}),|A|A0=1+ε2−12​ε12+…,arg⁡A=−ε1+…\frac{|A|}{A_{0}}=1+\varepsilon_{2}-\tfrac{1}{2}\varepsilon_{1}^{2}+\dots,\qquad\arg A=-\varepsilon_{1}+\dots(S17)

Replacing∇2\nabla^{2}by−q2-q^{2}thus displaces the phase at leading
order but costs nothing in amplitude until second—and the suppression
factor of the main text is a statement about amplitude.

## 


- 


Major funding support from
