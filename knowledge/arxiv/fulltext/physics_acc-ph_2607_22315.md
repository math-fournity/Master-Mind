# Robustness of Off-Axis Electron Vortices in Nonuniform Magnetic Fields

**arXiv ID**: 2607.22315v1
**Authors**: Hui-Dong Huang, Qi Meng, Zhi-Bin Wang, Liang Lu, Jian Chen, Li-Ping Zou
**Published**: 2026-07-24
**Categories**: physics.acc-ph, physics.plasm-ph, quant-ph
**HTML URL**: https://arxiv.org/html/2607.22315v1

## Abstract

Rotational symmetry protects the topological charge of on-axis electron vortices but not of off-axis vortices. We identify an additional SU(1,1) dynamical invariant that guarantees conservation of their intrinsic orbital angular momentum within the near-axis approximation. First-principles simulations of an off-axis electron vortex traversing a Glaser lens confirm this prediction, establishing a robust transport mechanism in axisymmetric nonuniform magnetic fields.

## Full Text

Robustness of Off-Axis Electron Vortices in Nonuniform Magnetic Fields

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- License: CC BY 4.0arXiv:2607.22315v1 [physics.acc-ph] 24 Jul 2026††thanks:These authors contributed equally to this work.††thanks:These authors contributed equally to this work.

## Robustness of Off-Axis Electron Vortices in Nonuniform Magnetic FieldsHui-Dong HuangSino-French Institute of Nuclear Engineering and Technology,Sun Yat-Sen University, Zhuhai 519082, ChinaQi MengSino-French Institute of Nuclear Engineering and Technology,Sun Yat-Sen University, Zhuhai 519082, ChinaZhi-Bin WangSino-French Institute of Nuclear Engineering and Technology,Sun Yat-Sen University, Zhuhai 519082, ChinaLiang LuSino-French Institute of Nuclear Engineering and Technology,Sun Yat-Sen University, Zhuhai 519082, ChinaJian Chenchenjian5@mail.sysu.edu.cnSino-French Institute of Nuclear Engineering and Technology,Sun Yat-Sen University, Zhuhai 519082, ChinaLi-Ping Zouzoulp5@mail.sysu.edu.cnSino-French Institute of Nuclear Engineering and Technology,Sun Yat-Sen University, Zhuhai 519082, China

## Abstract

Rotational symmetry protects the topological charge of on-axis electron vortices but not of off-axis vortices. We identify an additional SU(1,1) dynamical invariant that guarantees conservation of their intrinsic orbital angular momentum within the near-axis approximation. First-principles simulations of an off-axis electron vortex traversing a Glaser lens confirm this prediction, establishing a robust transport mechanism in axisymmetric nonuniform magnetic fields.

Introduction.—Electron vortices carrying quantized orbital angular momentum (OAM) provide a controllable internal degree of freedom for free electrons[1,2,3,4], with versatile applications ranging from electron microscopy[5], quantum information[6]and magnetic diagnostics[7]to high-energy physics[8]. To date, their dynamics have been explored predominantly under strictly on-axis propagation
in axisymmetric magnetic fields, where rotational symmetry guarantees conservation of the
canonical OAM[9,10,11,12,13,14,15].

In practice, however, electron vortices inevitably propagate with some transverse
misalignment. In axisymmetric but nonuniform magnetic fields, such as those in
Glaser lenses[16], the centroid then no longer coincides
with the symmetry axis (Fig.1). Although axial symmetry still
guarantees conservation of the total canonical OAM, the intrinsic OAM, defined
relative to the instantaneous centroid[18,19], is not guaranteed by rotational symmetry
alone. Whether it survives off-axis propagation in such nonuniform fields remains
an open question. Dynamical invariants have previously been identified for on-axis vortex modes in nonuniform magnetic fields[12], but those invariants constrain the transverse mode structure rather than the centroid motion; the intrinsic OAM of off-axis states was not addressed. More broadly, the conservation of extrinsic OAM lies outside the scope of Noether’s theorem. It emerges from an algebraic structure of the near-axis
Hamiltonian rather than from a continuous symmetry, which may explain why it
has remained unnoticed.

In this Letter, we show that, within the paraxial approximation[3],
the intrinsic OAM of an off-axis vortex is exactly conserved during propagation
through axisymmetric nonuniform magnetic fields, despite the absence of
centroid-frame symmetry protection. This conservation arises from two exact
constraints acting in concert: the axial symmetry of the external field fixes
the total canonical OAM, while a hidden SU(1,1) dynamical invariant, identified
with the extrinsic OAM, prevents any transfer of angular momentum into the
intrinsic part.

We confirm this prediction with first-principles numerical simulations of an
off-axis electron vortex traversing a Glaser lens. The simulations solve the
full three-dimensional Schrödinger equation without imposing the paraxial
approximation, while retaining only the near-axis vector potential, the latter
being far less restrictive than the paraxial condition. The results demonstrate that the wavepacket preserves both its vortex structure and intrinsic OAM over a wide range of propagation distances and transverse offsets, even under field gradients far steeper than typical experimental conditions. These findings establish a robust mechanism for vortex transport in realistic electron-optical systems,
where field inhomogeneity and beam misalignment are unavoidable.Figure 1:An off-axis vortex wavepacket propagating through a magnetic lens. The centroid follows a helical trajectory that winds around the curved magnetic field lines, while the intrinsic OAM, defined relative to the centroid, is not protected by axial symmetry alone.

Theory.—We consider an electron vortex in a magnetic field𝐁\mathbf{B}rotationally symmetric
about thezz-axis. Let−e-e(e>0e>0) be the electron charge. Near the axis,∇⋅𝐁=0\nabla\cdot\mathbf{B}=0implies an axially varying longitudinal fieldB​(z)B(z)accompanied by a weak radial
component at𝒪​(r⟂)\mathcal{O}(r_{\perp}), while off-axis corrections toBzB_{z}enter at𝒪​(r⟂2)\mathcal{O}(r_{\perp}^{2})[20,12,14].
To leading order, the vector potential in the symmetric gauge is𝐀=12​B​(z)​r⟂​𝐞θ.\mathbf{A}=\tfrac{1}{2}B(z)\,r_{\perp}\mathbf{e}_{\theta}.(1)

The Hamiltonian isH^=𝝅^2/2​m\hat{H}=\hat{\bm{\pi}}^{2}/2mwith𝝅^=𝐩^+e​𝐀\hat{\bm{\pi}}=\hat{\mathbf{p}}+e\mathbf{A}.
The canonical OAMℒ^=(𝐫^×𝐩^)z\hat{\mathcal{L}}=(\hat{\mathbf{r}}\times\hat{\mathbf{p}})_{z}commutes withH^\hat{H}, so⟨ℒ^⟩\langle\hat{\mathcal{L}}\rangleis exactly conserved by axial symmetry.
The intrinsic OAM, defined relative to the instantaneous centroid, decomposes asℒi=⟨ℒ^⟩−ℒext,ℒext=⟨x^⟩​⟨p^y⟩−⟨y^⟩​⟨p^x⟩.\mathcal{L}_{\mathrm{i}}=\langle\hat{\mathcal{L}}\rangle-\mathcal{L}_{\mathrm{ext}},\quad\mathcal{L}_{\mathrm{ext}}=\langle\hat{x}\rangle\langle\hat{p}_{y}\rangle-\langle\hat{y}\rangle\langle\hat{p}_{x}\rangle.(2)

Henceℒi\mathcal{L}_{\mathrm{i}}evolves only through the extrinsic partℒext\mathcal{L}_{\mathrm{ext}}, which is determined by the centroid’s transverse motion. We note thatℒext\mathcal{L}_{\mathrm{ext}}involves the canonical momentum, which is not gauge-invariant; as such it has no classical
counterpart and its conservation cannot be inferred from classical theorems.

Under the paraxial approximationψ=ei​k​z​χ\psi=e^{ikz}\chiwith|∂z2χ|≪k​|∂zχ||\partial_{z}^{2}\chi|\ll k|\partial_{z}\chi|[3], the transverse dynamics obeysi​ℏ​v​∂zχ=H^eff​χi\hbar v\,\partial_{z}\chi=\hat{H}_{\mathrm{eff}}\chi(v=ℏ​k/mv=\hbar k/m). WithωL​(z)=e​B​(z)/2​m\omega_{L}(z)=eB(z)/2m, the effective Hamiltonian isH^eff=𝐩^⟂22​m+ωL​(z)​ℒ^+12​m​ωL2​(z)​r^⟂2.\hat{H}_{\mathrm{eff}}=\frac{\hat{\mathbf{p}}_{\perp}^{2}}{2m}+\omega_{L}(z)\hat{\mathcal{L}}+\tfrac{1}{2}m\omega_{L}^{2}(z)\hat{r}_{\perp}^{2}.(3)

We take the planez0z_{0}as the starting point of propagation, defineH^0≡H^eff​(z0)\hat{H}_{0}\equiv\hat{H}_{\mathrm{eff}}(z_{0}), and work in the basis that diagonalizesH^0\hat{H}_{0}. At this plane, the vector potential (1) yields a radial fieldBr=−12​r⟂​B′​(z0)B_{r}=-\tfrac{1}{2}r_{\perp}B^{\prime}(z_{0})while its linearr⟂r_{\perp}-dependence
ensures thatH^0\hat{H}_{0}retains the algebraic form of a uniform-field
Landau Hamiltonian. It is diagonalized by ladder operatorsa^≡a^​(z0)\hat{a}\equiv\hat{a}(z_{0}),b^≡b^​(z0)\hat{b}\equiv\hat{b}(z_{0}), with[a^,a^†]=[b^,b^†]=1[\hat{a},\hat{a}^{\dagger}]=[\hat{b},\hat{b}^{\dagger}]=1and[a^,b^]=[a^,b^†]=0[\hat{a},\hat{b}]=[\hat{a},\hat{b}^{\dagger}]=0. These are Schrödinger-picture operators, with allzz-dependence carried by the state.
Expectation values⟨⋅⟩\langle\cdot\rangleare understood to be taken with respect to|χ​(z)⟩|\chi(z)\rangle.

In terms ofa^\hat{a}andb^\hat{b},H^0=ℏ​ωL​(z0)​(2​a^†​a^+1),ℒ^=ℏ​(a^†​a^−b^†​b^).\hat{H}_{0}=\hbar\omega_{L}(z_{0})(2\hat{a}^{\dagger}\hat{a}+1),\qquad\hat{\mathcal{L}}=\hbar(\hat{a}^{\dagger}\hat{a}-\hat{b}^{\dagger}\hat{b}).(4)

The extrinsic OAM, defined in the Schrödinger picture, readsℒext=ℏ​(|⟨a^⟩|2−|⟨b^†⟩|2).\mathcal{L}_{\mathrm{ext}}=\hbar\left(|\langle\hat{a}\rangle|^{2}-|\langle\hat{b}^{\dagger}\rangle|^{2}\right).(5)

Thezz-dependent partV^​(z)≡H^eff​(z)−H^0\hat{V}(z)\equiv\hat{H}_{\mathrm{eff}}(z)-\hat{H}_{0}can be decomposed asV^​(z)=Ω​(z)​ℒ^+Λ​(z)​(2​K^0+K^−+K^+),\hat{V}(z)=\Omega(z)\hat{\mathcal{L}}+\Lambda(z)\bigl(2\hat{K}_{0}+\hat{K}_{-}+\hat{K}_{+}\bigr),(6)

withΩ=ωL​(z)−ωL​(z0)\Omega=\omega_{L}(z)-\omega_{L}(z_{0})andΛ=ℏ​[ωL2​(z)−ωL2​(z0)]/2​ωL​(z0)\Lambda=\hbar[\omega_{L}^{2}(z)-\omega_{L}^{2}(z_{0})]/2\omega_{L}(z_{0}).
HereK^0=12​(a^†​a^+b^†​b^+1),K^+=a^†​b^†,K^−=a^​b^\hat{K}_{0}=\tfrac{1}{2}(\hat{a}^{\dagger}\hat{a}+\hat{b}^{\dagger}\hat{b}+1),\quad\hat{K}_{+}=\hat{a}^{\dagger}\hat{b}^{\dagger},\quad\hat{K}_{-}=\hat{a}\hat{b}(7)

are the SU(1,1) generators, satisfying[K^0,K^±]=±K^±[\hat{K}_{0},\hat{K}_{\pm}]=\pm\hat{K}_{\pm}and[K^−,K^+]=2​K^0[\hat{K}_{-},\hat{K}_{+}]=2\hat{K}_{0}[21].

We now consider an off-axis vortex state atz0z_{0}withℒi​(z0)=ℓ​ℏ\mathcal{L}_{\mathrm{i}}(z_{0})=\ell\hbar, i.e. a state whose transverse centroid satisfies⟨𝐫⟂⟩≠0\langle\mathbf{r}_{\perp}\rangle\neq 0.
According to the decomposition in Eq. (2), the extrinsic angular momentumℒext\mathcal{L}_{\mathrm{ext}}is determined by the centroid motion.
For an on-axis state (⟨𝐫⟂⟩=0\langle\mathbf{r}_{\perp}\rangle=0),ℒext\mathcal{L}_{\mathrm{ext}}vanishes identically; in uniform fields it may remain trivially constant[19], and its dynamical role has often been overlooked. In the off-axis, nonuniform regime, however, the non-zero centroid (⟨𝐫⟂⟩≠0\langle\mathbf{r}_{\perp}\rangle\neq 0) makesℒext\mathcal{L}_{\mathrm{ext}}a genuine dynamical variable whose conservation must be examined directly.

The termH^0+Ω​(z)​ℒ^\hat{H}_{0}+\Omega(z)\hat{\mathcal{L}}can be removed by the unitary transformationU^​(z)=exp⁡[−iℏ​v​∫z0z𝑑z′​(H^0+Ω​(z′)​ℒ^)].\hat{U}(z)=\exp\!\left[-\frac{i}{\hbar v}\int_{z_{0}}^{z}dz^{\prime}\,\bigl(\hat{H}_{0}+\Omega(z^{\prime})\hat{\mathcal{L}}\bigr)\right].(8)

In the resulting interaction picture,|χI​(z)⟩=U^†​(z)​|χ​(z)⟩|\chi_{I}(z)\rangle=\hat{U}^{\dagger}(z)|\chi(z)\rangle,
the evolution is governed by the pure SU(1,1) HamiltonianH^I​(z)=Λ​(z)​(2​K^0+e−i​Φ​K^−+ei​Φ​K^+),\hat{H}_{I}(z)=\Lambda(z)\bigl(2\hat{K}_{0}+e^{-i\Phi}\hat{K}_{-}+e^{i\Phi}\hat{K}_{+}\bigr),(9)

withΦ​(z)=2​ωL​(z0)​(z−z0)v.\Phi(z)=\frac{2\omega_{L}(z_{0})(z-z_{0})}{v}.(10)

To find a conserved quantity, we switch to the Heisenberg picture within the
interaction frame. Defininga^I​(z)=U^I†​(z)​a^​U^I​(z)\hat{a}_{I}(z)=\hat{U}_{I}^{\dagger}(z)\hat{a}\,\hat{U}_{I}(z)andb^I†​(z)=U^I†​(z)​b^†​U^I​(z)\hat{b}_{I}^{\dagger}(z)=\hat{U}_{I}^{\dagger}(z)\hat{b}^{\dagger}\,\hat{U}_{I}(z), whereU^I​(z)\hat{U}_{I}(z)is the formal evolution operator generated byH^I​(z)\hat{H}_{I}(z), i.e.i​ℏ​v​∂zU^I=H^I​U^Ii\hbar v\,\partial_{z}\hat{U}_{I}=\hat{H}_{I}\hat{U}_{I}withU^I​(z0)=I\hat{U}_{I}(z_{0})=I.
A symmetric rotationa^R=e−i​Φ/2​a^I,b^R†=ei​Φ/2​b^I†\hat{a}_{R}=e^{-i\Phi/2}\hat{a}_{I},\qquad\hat{b}_{R}^{\dagger}=e^{i\Phi/2}\hat{b}_{I}^{\dagger}(11)

then yieldsi​ℏ​v​∂z(a^Rb^R†)=ℋ​(z)​(a^Rb^R†),i\hbar v\,\partial_{z}\begin{pmatrix}\hat{a}_{R}\\
\hat{b}_{R}^{\dagger}\end{pmatrix}=\mathcal{H}(z)\begin{pmatrix}\hat{a}_{R}\\
\hat{b}_{R}^{\dagger}\end{pmatrix},(12)

withℋ​(z)=(Δ​(z)Λ​(z)−Λ​(z)−Δ​(z)),Δ​(z)=ℏ​ωL​(z0)+Λ​(z).\mathcal{H}(z)=\begin{pmatrix}\Delta(z)&\Lambda(z)\\
-\Lambda(z)&-\Delta(z)\end{pmatrix},\quad\Delta(z)=\hbar\omega_{L}(z_{0})+\Lambda(z).(13)

The expectation values⟨a^R⟩0\langle\hat{a}_{R}\rangle_{0}and⟨b^R†⟩0\langle\hat{b}_{R}^{\dagger}\rangle_{0}, taken with respect to the initial
interaction-picture state|χI​(z0)⟩|\chi_{I}(z_{0})\rangle, obey the same equation (12). Defining𝐰=(⟨a^R⟩0,⟨b^R†⟩0)T\mathbf{w}=(\langle\hat{a}_{R}\rangle_{0},\langle\hat{b}_{R}^{\dagger}\rangle_{0})^{T},
one hasi​ℏ​v​∂z𝐰=ℋ​𝐰i\hbar v\,\partial_{z}\mathbf{w}=\mathcal{H}\mathbf{w}. Taking the conjugate
transpose gives−i​ℏ​v​∂z𝐰†=𝐰†​ℋ†-i\hbar v\,\partial_{z}\mathbf{w}^{\dagger}=\mathbf{w}^{\dagger}\mathcal{H}^{\dagger},
from whichi​ℏ​v​∂z(𝐰†​σz​𝐰)=𝐰†​(σz​ℋ−ℋ†​σz)​𝐰.i\hbar v\,\partial_{z}(\mathbf{w}^{\dagger}\sigma_{z}\mathbf{w})=\mathbf{w}^{\dagger}(\sigma_{z}\mathcal{H}-\mathcal{H}^{\dagger}\sigma_{z})\mathbf{w}.(14)

Sinceℋ†​σz=σz​ℋ\mathcal{H}^{\dagger}\sigma_{z}=\sigma_{z}\mathcal{H}, the right-hand side vanishes,
so the SU(1,1) norm𝐰†​σz​𝐰=|⟨a^R⟩0|2−|⟨b^R†⟩0|2\mathbf{w}^{\dagger}\sigma_{z}\mathbf{w}=|\langle\hat{a}_{R}\rangle_{0}|^{2}-|\langle\hat{b}_{R}^{\dagger}\rangle_{0}|^{2}is conserved.

To relate this conserved quantity to a physical observable, we return to the
Schrödinger picture, whereℒext\mathcal{L}_{\mathrm{ext}}was expressed in terms
ofa^\hat{a}andb^†\hat{b}^{\dagger}in Eq. (5). Tracing the sequence
of transformations back to the original Schrödinger state, one finds that⟨a^R⟩0\langle\hat{a}_{R}\rangle_{0}and⟨b^R†⟩0\langle\hat{b}_{R}^{\dagger}\rangle_{0}differ from⟨a^⟩\langle\hat{a}\rangleand⟨b^†⟩\langle\hat{b}^{\dagger}\rangleby phases that drop out
in the norm. Hence𝐰†​σz​𝐰=|⟨a^⟩|2−|⟨b^†⟩|2=ℒext/ℏ,\mathbf{w}^{\dagger}\sigma_{z}\mathbf{w}=|\langle\hat{a}\rangle|^{2}-|\langle\hat{b}^{\dagger}\rangle|^{2}=\mathcal{L}_{\mathrm{ext}}/\hbar,(15)

which is therefore constant.

Like the classical adiabatic invariantμ=m​v⟂2/(2​B)\mu=mv_{\perp}^{2}/(2B)(the magnetic moment associated with the particle’s gyromotion, approximately conserved when the field varies slowly compared with the cyclotron period[22]),ℒext\mathcal{L}_{\mathrm{ext}}is exactly conserved within the paraxial approximation, beyond which the conservation is only approximate (as seen in the numerical simulations below), and likewise constrains the transverse motion while leaving the detailed dynamics undetermined. Unlikeμ\mu, however, it is canonical and gauge-dependent, so it represents a purely quantum version of such an invariant. Although the near-axis Hamiltonian locally preserves the Landau eigenstructure at eachzz, an off-axis state feels transverse field components as it propagates, so its wavefunction can evolve in a complex way. The existence of this invariant protects the topological charge despite such complexity.

Numerical simulation.—To verify the robustness of the vortex structure and intrinsic OAM during off-axis propagation through a Glaser magnetic lens with on-axis profileB​(z)=B0​(1+z2/a2)−1B(z)=B_{0}(1+z^{2}/a^{2})^{-1}[16,17], we solve the full Schrödinger equation. We employ an operator-splitting Fourier pseudo-spectral method combined with a semi-Lagrangian integration scheme[23,24,25]. In our simulations, a vortex-electron wavepacket traverses a Glaser lens, as sketched in Fig.1. The initial state is a Laguerre-Gaussian vortex wavepacket with a Gaussian
longitudinal envelope[26], whose toroidal
probability density|ψ|2|\psi|^{2}is shown in Figs.2(c)
and3(c).Figure 2:Dynamics of an off-axis vortex-electron wavepacket in Glaser lenses with different characteristic lengthsaa. Panel (a) shows the longitudinal magnetic-field profilesBz​(z)B_{z}(z)fora=160,80,40​wma=160,80,40\,w_{m}, and panel (b) the evolution of the intrinsic canonical OAMℒi\mathcal{L}_{\mathrm{i}}. Panels (c–f) show the corresponding probability density|ψ|2|\psi|^{2}at the initial time and att=2.0​|z0|/v0t=2.0|z_{0}|/v_{0}. The initial wavepacket has topological chargeℓ=+3\ell=+3, characteristic scalesw⟂=2​wmw_{\perp}=2\,w_{m}andwz=4​wmw_{z}=4\,w_{m}, centroid position𝐫0=(0,+2,−80)​wm{\bf r}_{0}=(0,+2,-80)\,w_{m}, and axial speedv0=(160​wm)/(6​Tc)v_{0}=(160\,w_{m})/(6T_{c}). HereB0=0.02TB_{0}=$0.02\text{\,}\mathrm{T}$, corresponding towm=2​ℏ/|e​B0|=0.256µ​mw_{m}=\sqrt{2\hbar/|eB_{0}|}=$0.256\text{\,}\mathrm{\SIUnitSymbolMicro m}$andTc=2​π​m/|e​B0|=1.786nsT_{c}=2\pi m/|eB_{0}|=$1.786\text{\,}\mathrm{ns}$.Figure 3:Dynamics of an off-axis vortex-electron wavepacket for different initial transverse offsetsy0y_{0}. Panel (a) displays the centroid trajectories𝐫¯\bar{\mathbf{r}}in thezz–yyplane fory0=+2,+4,+6​wmy_{0}=+2,+4,+6\,w_{m}, while panel (b) shows the evolution of the intrinsic canonical OAMℒi\mathcal{L}_{\mathrm{i}}. Panels (c–f) show the corresponding probability density|ψ|2|\psi|^{2}at the initial time and att=a/v0t=a/v_{0}. The initial wavepacket has topological chargeℓ=+3\ell=+3, characteristic scalesw⟂=1​wmw_{\perp}=1\,w_{m}andwz=4​wmw_{z}=4\,w_{m}, centroid position𝐫0=(0,y0,−0.5​a){\bf r}_{0}=(0,y_{0},-0.5\,a), and axial speedv0=a/(6​Tc)v_{0}=a/(6T_{c}). The Glaser field is specified bya=160​wma=160\,w_{m}andB0=0.02TB_{0}=$0.02\text{\,}\mathrm{T}$, yielding the characteristic scaleswm=0.256µ​mw_{m}=$0.256\text{\,}\mathrm{\SIUnitSymbolMicro m}$andTc=1.786nsT_{c}=$1.786\text{\,}\mathrm{ns}$.

We first examine the influence of magnetic non-uniformity, characterized by the length scaleaa, on the dynamics of an off-axis vortex electron, as shown in Fig.2. The parameter is scanned overa∈[40,160]​wma\in[40,160]\,w_{m}while keeping the initial transverse offset fixed aty0=2​wmy_{0}=2\,w_{m}. The resulting wavepacket snapshots att=2.0​|z0|/v0t=2.0\,|z_{0}|/v_{0}reveal a clear dependence on the magnetic-field variation scale. For a sufficiently smooth field profile [largeaa, Fig.2(d)], the probability density exhibits transverse breathing while maintaining an almost ideal annular structure. Asaadecreases, the sharper longitudinal field gradient gives rise to increasingly pronounced non-paraxial effects, manifested by a noticeable spatial tilt of the wavepacket in thezz–yyplane [Fig.2(e–f)]. Throughout the parameter scan, however, the vortex structure remains intact (see Supplemental Material[27]for the full time evolution). The evolution of the intrinsic canonical orbital angular momentum,ℒi\mathcal{L}_{\mathrm{i}}, is summarized in Fig.2(b). Although stronger field gradients lead to larger dynamical modulations during propagation, the deviation from its initial value,Δ​ℒi=ℒi−ℓ​ℏ\Delta\mathcal{L}_{\text{i}}=\mathcal{L}_{\text{i}}-\ell\hbarwithℓ=+3\ell=+3, remains below0.04​ℏ0.04\,\hbarover the full parameter range. Even in the most nonuniform case [(f):a=40​wma=40\,w_{m}], the maximum relative deviation,ε=max⁡|Δ​ℒi/ℓ​ℏ|\varepsilon=\max|\Delta\mathcal{L}_{\text{i}}/\ell\hbar|, is only∼1%\sim 1\%.

We next investigate the influence of the initial transverse displacementy0y_{0}, as shown in Fig.3. Here the lens profile is fixed ata=160​wma=160\,w_{m}, while the initial offset is varied overy0∈[+2,+6]​wmy_{0}\in[+2,+6]\,w_{m}. The centroid trajectories𝐫¯\bar{\mathbf{r}}in thezz–yyplane are shown in Fig.3(a), exhibiting the characteristic undulating cyclotron motion superimposed on the overall guiding motion along the curved magnetic field lines (gray curves). Although larger offsets expose the electron to stronger transverse field components, the transverse probability density consistently preserves its circular symmetry and annular vortex profile for all cases considered [Figs.3(d–f); see also Supplemental Material[27]]. Likewise, the intrinsic OAM remains remarkably stable [Fig.3(b)], with the maximum relative deviation reaching onlyε≃0.3%\varepsilon\simeq 0.3\%for the largest offset [(f):y0=+6​wmy_{0}=+6\,w_{m}], corresponding to|Δ​ℒi|<0.01​ℏ|\Delta\mathcal{L}_{\text{i}}|<0.01\,\hbarthroughout the evolution.

To verify that these small residual variations are not numerical artifacts, we performed grid-refinement tests for the results shown in Figs.2(b) and3(b). The percent-level residuals remain essentially unchanged under both coarser and finer spatial meshes (see Supplemental Material[27]), indicating that the observed fluctuations inℒi\mathcal{L}_{\text{i}}originate from the underlying quantum dynamics rather than numerical discretization errors.

We further examine the dependence on the initial intrinsic OAM by fixing the lens profile ata=160​wma=160\,w_{m}and the initial offset aty0=+2​wmy_{0}=+2\,w_{m}, while changing the topological charge overℓ∈[−5,+5]\ell\in[-5,+5]. The maximum relative deviation remains belowε≲0.1%\varepsilon\lesssim 0.1\%for all values ofℓ\ell, with no clear scaling relationship with respect toℓ\ell(see Supplemental Material[27]).

Taken together, these simulations confirm that neither magnetic-field non-uniformity nor off-axis beam injection significantly affects the intrinsic OAM. Both the vortex structure and the intrinsic canonical OAM remain remarkably robust during electron transport through the magnetic lens.

Discussion.—From a topological perspective, the vortex is characterized by the phase winding number around a closed contourCCenclosing the phase singularity at the beam centroid[28],12​π​∮C∇⟂arg⁡ϕ⋅d​𝒍=ℓ.\frac{1}{2\pi}\oint_{C}\bm{\nabla}_{\perp}\arg\phi\cdot d\bm{l}=\ell.For the quadratic axisymmetric Hamiltonian (3), the wave function remains in the same azimuthal sector during propagation due to the hidden SU(1,1) dynamics, so the contour can be continuously transported without crossing a zero of the wave function. Consequently, the winding number cannot change, and the integerℓ\ellis a genuine conserved quantum number. In this model, the topological charge and the centroid-relative intrinsic OAM are represented by the same integerℓ\ell, so intrinsic-OAM conservation is accompanied by exact preservation of the vortex topology.

The small residual evolution ofℒi\mathcal{L}_{\mathrm{i}}observed in our simulations
follows from the full three-dimensional quantum dynamics. From the Heisenberg
equations for𝐫^\hat{\mathbf{r}}and𝐩^\hat{\mathbf{p}}, one obtainsdℒextdt=\displaystyle\derivative{\mathcal{L}_{\mathrm{ext}}}{t}=m​[⟨y^⟩​Cov​(ω^L2,x^)−⟨x^⟩​Cov​(ω^L2,y^)]\displaystyle\;\;m\bigl[\langle\hat{y}\rangle\,\mathrm{Cov}(\hat{\omega}_{L}^{2},\hat{x})-\langle\hat{x}\rangle\,\mathrm{Cov}(\hat{\omega}_{L}^{2},\hat{y})\bigr](16)+[⟨x^⟩​Cov​(ω^L,p^x)−⟨p^x⟩​Cov​(ω^L,x^)]\displaystyle+\bigl[\langle\hat{x}\rangle\,\mathrm{Cov}(\hat{\omega}_{L},\hat{p}_{x})-\langle\hat{p}_{x}\rangle\,\mathrm{Cov}(\hat{\omega}_{L},\hat{x})\bigr]+[⟨y^⟩​Cov​(ω^L,p^y)−⟨p^y⟩​Cov​(ω^L,y^)],\displaystyle+\bigl[\langle\hat{y}\rangle\,\mathrm{Cov}(\hat{\omega}_{L},\hat{p}_{y})-\langle\hat{p}_{y}\rangle\,\mathrm{Cov}(\hat{\omega}_{L},\hat{y})\bigr],

whereω^L=ωL​(z^)\hat{\omega}_{L}=\omega_{L}(\hat{z})andCov​(o^1,o^2)≡⟨o^1​o^2⟩−⟨o^1⟩​⟨o^2⟩\mathrm{Cov}(\hat{o}_{1},\hat{o}_{2})\equiv\langle\hat{o}_{1}\hat{o}_{2}\rangle-\langle\hat{o}_{1}\rangle\langle\hat{o}_{2}\rangle.
As⟨ℒ^⟩\langle\hat{\mathcal{L}}\rangleis conserved by axial symmetry, the residual
evolution ofℒi\mathcal{L}_{\mathrm{i}}seen in our simulations must originate from
the right-hand side of Eq. (16).

To see when these covariance terms become appreciable, expandωL​(z^)≃ωL​(zc)+ωL′​(zc)​(z^−zc)\omega_{L}(\hat{z})\simeq\omega_{L}(z_{c})+\omega_{L}^{\prime}(z_{c})(\hat{z}-z_{c})around the centroidzc≡⟨z^⟩z_{c}\equiv\langle\hat{z}\rangle. To leading order,Cov​(ω^L,o^)≃ωL′​Cov​(z^,o^)\mathrm{Cov}(\hat{\omega}_{L},\hat{o})\simeq\omega_{L}^{\prime}\,\mathrm{Cov}(\hat{z},\hat{o}),Cov​(ω^L2,o^)≃2​ωL​ωL′​Cov​(z^,o^)\mathrm{Cov}(\hat{\omega}_{L}^{2},\hat{o})\simeq 2\omega_{L}\omega_{L}^{\prime}\,\mathrm{Cov}(\hat{z},\hat{o})foro^=x^,y^,p^x,p^y\hat{o}=\hat{x},\hat{y},\hat{p}_{x},\hat{p}_{y}.
For a wavepacket of longitudinal extentwzw_{z}and transverse extentw⟂w_{\perp},Cov​(z^,r^⟂)∼wz​w⟂\mathrm{Cov}(\hat{z},\hat{r}_{\perp})\sim w_{z}w_{\perp}andCov​(z^,p^⟂)∼wz​ℏ/w⟂\mathrm{Cov}(\hat{z},\hat{p}_{\perp})\sim w_{z}\,\hbar/w_{\perp}, as these covariances
measure the characteristic longitudinal–transverse correlations within the
wavepacket.

Inserting these estimates into Eq. (16), each of the six terms
scales as|ωL′|​wz​ℏ|\omega_{L}^{\prime}|w_{z}\hbar(theωL2\omega_{L}^{2}terms carry an extra factorm​ωL​w⟂2/ℏ∼(w⟂/wm)2m\omega_{L}w_{\perp}^{2}/\hbar\sim(w_{\perp}/w_{m})^{2}, which isO​(1)O(1)sincew⟂∼wmw_{\perp}\sim w_{m}in our simulations).
Withℒext∼ℏ\mathcal{L}_{\mathrm{ext}}\sim\hbarand dividing by the natural frequency scaleωL\omega_{L}yields the
dimensionless control parameter|d​ℒext/d​t|/ℒextωL∼|ωL′|​wzωL∼B′​wzB,\frac{|d\mathcal{L}_{\mathrm{ext}}/dt|/\mathcal{L}_{\mathrm{ext}}}{\omega_{L}}\sim\frac{|\omega_{L}^{\prime}|w_{z}}{\omega_{L}}\sim\frac{B^{\prime}w_{z}}{B},(17)

which measures the fractional field variation across the wavepacket.
WhenB′​wz/B≪1B^{\prime}w_{z}/B\ll 1, the field is nearly uniform and the covariance terms
are frozen out; when it approaches unity, the wavepacket resolves the
inhomogeneity andℒext\mathcal{L}_{\mathrm{ext}}can evolve appreciably.
For the Glaser fieldB​(z)=B0​(1+z2/a2)−1B(z)=B_{0}(1+z^{2}/a^{2})^{-1},B′/B∼1/aB^{\prime}/B\sim 1/a, so the
ratio reduces towz/aw_{z}/a.

In our simulations this ratio reacheswz/a≲10−1w_{z}/a\lesssim 10^{-1}(the field changes by∼10%\sim 10\%over the wavepacket), a regime far more extreme
than typical electron-optical conditions, chosen deliberately to expose any
beyond-paraxial corrections. Even under this strict test,ℒi\mathcal{L}_{\mathrm{i}}deviates by only a few percent. In practical settings,
wherewz≪B/B′w_{z}\ll B/B^{\prime}, the field is effectively uniform across the wavepacket,
the covariances are negligible, andℒi\mathcal{L}_{\mathrm{i}}is conserved.
Importantly, the theoretical results rely only on the near-axis vector potential
of Eq. (1), not on the specific Glaser profile used in the numerical simulation. The mechanism thus applies generally to axisymmetric magnetic systems described by the same near-axis
model, including magnetic mirrors and solenoids[14,20,26].

Beyond electron optics, the demonstrated robustness also supports emerging proposals for off-axis vortex-particle scattering employing transverse beam-center offsets as tunable impact parameters[29], by preserving the intrinsic OAM during transport through axisymmetric nonuniform magnetic fields.

Summary.—We have shown that off-axis vortex electrons possess a previously unrecognized robustness in nonuniform axisymmetric magnetic fields. Although rotational symmetry alone does not protect the intrinsic OAM defined with respect to the instantaneous centroid, its conservation follows from the combined action of this geometric symmetry and a hidden dynamical invariant associated with the SU(1,1) algebra within the near-axis approximation. Numerical simulations of vortex-electron propagation through Glaser magnetic lenses verify this prediction and demonstrate stable transport of the vortex structure under magnetic-field inhomogeneity and beam misalignment. The mechanism is expected to extend to a broad class of axisymmetric electron-optical systems.

Acknowledgments.—We thank Pengming Zhang for valuable comments. The work was supported by the National Key R&D Program of China (No. 2024YFE0109802), the National Natural Science Foundation of China (Grant No. 12175320), and the Guangdong Basic and Applied Basic Research Foundation (Grant No.2026A1515010999).

## References
- [1]K. Y. Bliokh, Y. P. Bliokh, S. Savel’ev, and F. Nori,Phys. Rev. Lett.99, 190404 (2007).
- [2]J. Verbeeck, H. Tian, and P. Schattschneider,Nature467, 301 (2010).
- [3]K. Y. Bliokh, I. P. Ivanov, G. Guzzinati, L. Clark, R. Van Boxem, A. Béché, R. Juchtmans, M. A. Alonso, P. Schattschneider, F. Nori, and J. Verbeeck,Phys. Rep.690, 1 (2017).
- [4]S. M. Lloyd, M. Babiker, G. Thirunavukkarasu, and J. Yuan,Rev. Mod. Phys.89, 035004 (2017).
- [5]R. Juchtmans, A. Béché, A. Abakumov, M. Batuk, and J. Verbeeck,Phys. Rev. B91, 094112 (2015).
- [6]S. Löffler, T. Schachinger, P. Hartel, P.-H. Lu, R. E. Dunin-Borkowski, M. Obermair, M. Dries, D. Gerthsen, and P. Schattschneider,Quantum7, 1050 (2023).
- [7]F. Barrows, A. K. Petford-Long, and C. Phatak,Commun. Phys.5, 1 (2022).
- [8]I. P. Ivanov,Prog. Part. Nucl. Phys.127, 103987 (2022).
- [9]K. Y. Bliokh, P. Schattschneider, J. Verbeeck, and F. Nori,Phys. Rev. X2, 041011 (2012).
- [10]C. R. Greenshields, R. L. Stamps, S. Franke-Arnold, and S. M. Barnett,Phys. Rev. Lett.113, 240404 (2014).
- [11]L.-P. Zou, P.-M. Zhang, and A. J. Silenko,Phys. Rev. A103, L010201 (2021).
- [12]A. Melkani, and S. J. van Enk,Phys. Rev. Res.3, 033060 (2021).
- [13]D. Karlovets, D. Grosman, and I. Pavlov,Phys. Rev. Lett.136, 085002 (2026).
- [14]N. V. Filina, and S. S. Baturin,Phys. Rev. A113, L021302 (2026).
- [15]N. V. Filina and S. S. Baturin,Phys. Rev. A113, 053315 (2026).
- [16]M. Szilagyi,Electron and Ion Optics,
(Springer, New York, US, 2012).
- [17]S. A. Khan and R. Jagannathan,Optik229, 166303 (2021).
- [18]A. T. O’Neil, I. MacVicar, L. Allen, and M. J. Padgett,Phys. Rev. Lett.88, 053601 (2002).
- [19]C. R. Greenshields, S. Franke-Arnold, and R. L. Stamps,New J. Phys.17, 093015 (2015).
- [20]L.-P. Zou, and P.-M. Zhang, and A. J. Silenko,J. Phys. B: At. Mol. Opt. Phys.57, 045401 (2024).
- [21]C. C. Gerry,J. Opt. Soc. Am. B8, 685 (1991).
- [22]T. G. Northrop,The Adiabatic Motion of Charged Particles(Interscience Publishers, New York, 1963).
- [23]S. Jin, and Z.-N. Zhou,Commun. Info. Syst.13, 247 (2013).
- [24]M. Caliari, A. Ostermann, and C. Piazzola,J. Comput. Appl. Math.316, 74 (2017).
- [25]T. S. Gutleb, N. J. Mauser, M. Ruggeri, and H. P. Stimming,Comput. Meth. Appl. Math.24, 407 (2024).
- [26]G. K. Sizykh, A. D. Chaikovskaia, D. V. Grosman, I. I. Pavlov, and D. V. Karlovets,Prog. Theor. Exp. Phys.2024, 053A02 (2024).
- [27]See Supplemental Material at [URL to be inserted by publisher] for
derivations of the Landau-level algebra, the SU(1,1) structure, and the
time evolution of the extrinsic canonical OAM, along with the numerical
method, additional simulations, and movies of the wavepacket evolution.
- [28]A. Lubk, L. Clark, G. Guzzinati, and J. Verbeeck,Phys. Rev. A87, 033834 (2013).
- [29]Y. Yang, and I. P. Ivanov,Phys. Rev. D113, 116020 (2026).

## 


- 


Major funding support from
