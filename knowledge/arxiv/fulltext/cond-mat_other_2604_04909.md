# Weak Solutions to the Bloch Equations with Distant Dipolar Field

**arXiv ID**: 2604.04909v1
**Authors**: Louis-S. Bouchard
**Published**: 2026-04-06
**Categories**: cond-mat.other, math.NA, physics.chem-ph
**Comments**: 28 pages, 9 figures, 3 tables
**DOI**: 10.1063/5.0325917
**HTML URL**: https://arxiv.org/html/2604.04909v1

## Abstract

The distant dipolar field (DDF) is a long-range, nonlocal contribution to liquid-state spin dynamics that arises from intermolecular dipolar couplings and can generate multiple-quantum coherences and novel MRI contrast. Its sign-changing kernel makes Bloch-DDF dynamics strongly geometry dependent, and FFT-based dipolar convolutions naturally assume periodic or padded Cartesian domains rather than bounded samples with reflective diffusion boundaries. We study the Bloch equations with the DDF on bounded domains under homogeneous Neumann diffusion conditions. We derive a finite-element weak formulation that supports spatially varying diffusion and relaxation parameters and uses a short-distance regularization of the secular DDF kernel with length a>0. For fixed a we prove boundedness of the DDF operator, establish an L2 energy balance in which precession is neutral while diffusion and transverse relaxation are dissipative, and obtain local well-posedness with continuous dependence on the data, with global existence under energy-neutral transport. For the Galerkin semi-discretization we show a discrete energy identity mirroring the continuum estimate. For computation, we evaluate the DDF in real space with a matrix-free near/far scheme and advance in time using a second-order IMEX splitting method that treats diffusion and relaxation implicitly and precession explicitly. The explicit stage applies a Rodrigues rotation at DDF quadrature points followed by an L2 projection, enabling stable multi-cycle lab-frame simulations. We validate against three closed-form benchmarks and quantify curved-boundary effects by comparing mapped finite elements with a voxel-mask finite-difference baseline on spherical Neumann eigenmode decay. These results provide an analyzable and reproducible route for Bloch-DDF dynamics on bounded domains with complex geometry.

## Full Text

Weak Solutions to the Bloch Equations with Distant Dipolar Field

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
- License: CC BY 4.0arXiv:2604.04909v1 [cond-mat.other] 06 Apr 2026

## Weak Solutions to the Bloch Equations with Distant Dipolar FieldLouis-S. Bouchardlsbouchard@ucla.eduDepartment of Chemistry and Biochemistry, University of California, Los Angeles, CA 90095

## Abstract

The distant dipolar field (DDF) is a long-range, nonlocal contribution to spin dynamics in liquids that arises from intermolecular dipolar couplings and can generate multiple-quantum coherences in liquids and produce novel MRI contrast. Its nonlocal, sign-changing kernel makes Bloch–DDF dynamics strongly geometry dependent, and common FFT-based dipolar convolutions are naturally aligned with periodic boxes or padded Cartesian grids rather than bounded samples with reflective diffusion boundaries. We study the Bloch equations with the DDF on bounded domains with homogeneous Neumann diffusion conditions. We derive a conforming finite-element weak formulation that allows spatially varying diffusion and relaxation parameters and uses a short-distance regularization of the secular DDF kernel with lengtha>0a>0. For fixedaawe prove boundedness of the induced DDF operator, establish anL2L^{2}energy balance in which precession is neutral while diffusion and transverse relaxation are dissipative, and obtain local well-posedness with continuous dependence on the data (with global existence under energy-neutral transport conditions). For the Galerkin semi-discretization we show a discrete energy identity that mirrors the continuum estimate. For computation, we evaluate the DDF in real space with a matrix-free near/far scheme and advance in time with a second-order IMEX splitting method that treats diffusion and relaxation implicitly and treats precession explicitly. The explicit stage applies a Rodrigues rotation at DDF quadrature points followed by anL2L^{2}projection, which supports stable multi-cycle lab-frame calculations. We validate against three closed-form benchmarks that isolate distinct model components and we quantify curved-boundary effects by comparing mapped-geometry finite elements with a voxel-mask finite-difference baseline on a spherical Neumann eigenmode decay. These results provide an analyzable and reproducible route for Bloch–DDF dynamics on bounded domains with complex geometry.Bloch equations; distant dipolar field; finite elements; weak solution; well-posedness; energy stability; matrix-free method; IMEX time stepping

## IIntroduction

Intermolecular dipolar couplings can generate long-range, nonlocal contributions to nuclear spin dynamics in liquids and soft matter. In many experimentally relevant regimes, these effects can be expressed as a distant dipolar field (DDF) that depends on the magnetization distribution over the sample. This mechanism underlies several families of intermolecular multiple-quantum coherence (iMQC) and related sequences, including early demonstrations of coherence pathways that couple spins over mesoscopic distances and can produce contrast mechanisms that differ from conventional local Bloch models[23,14,17,21,22,9,8,7,12]. In these settings the DDF acts as a sign-changing interaction whose net effect depends on geometry, boundary conditions, and the spatial encoding applied by gradients.

This physics has been leveraged for structural and materials characterization and for MRI contrast mechanisms. Examples include reconstruction of porous microstructure from bulk signals that depend on the dipolar field[2], vector-field and correlation-length encoding strategies for imaging and characterization[4,10], and sensitivity to internal field gradients and anisotropy in heterogeneous media such as trabecular bone[3], together with related diffusion-in-internal-field methods for trabecular bone microstructure characterization[19]. Related work has explored coherent diffraction-like phenomena in engineered structures[20]and nonlinear dynamics in strongly polarized fluids where long-range dipolar interactions can drive instabilities[16]. These applications motivate simulations of Bloch–DDF dynamics beyond idealized periodic boxes.

From a computational standpoint, Bloch–DDF models are nonlinear and nonlocal. Direct evaluation of the dipolar integral couples all source and target points and can dominate cost. Efficient approaches on structured grids often use Fourier methods or hybrid real/Fourier strategies to accelerate dipolar field evaluation[13]. Complementary numerical and perturbative studies on structured models have visualized geometry-dependent DDF patterns and analyzed susceptibility-sensitive CRAZED-type signals[15,24]. Analytical treatments have also derived steady-state longitudinal profiles for repeated DDF sequences and revisited the validity regime of approximate Bloch–Torrey-based DDF signal formulas[11,1]. However, FFT-based approaches are naturally aligned with periodic or padded rectangular domains. They can be awkward for curved boundaries, reflective diffusion conditions, and complex geometries, where boundary effects are part of the physical model rather than a numerical artifact.

In this work we develop and analyze a finite-element (FE) weak formulation for the Bloch–DDF system on bounded domains with reflective diffusion boundaries first proposed in Refs.[5,6]. The weak form reduces regularity requirements and supports complex geometries. We introduce a short-distance regularization of the secular DDF kernel with length scalea>0a>0, which yields bounded operator estimates on bounded domains. On this basis we prove boundedness of the regularized DDF operator, derive anL2L^{2}energy balance in which precession is neutral and diffusion and transverse relaxation are dissipative, and obtain existence and uniqueness of weak solutions under assumptions stated in the text. For the semi-discrete FE system we show a discrete energy identity that mirrors the continuum estimate.

Algorithmically, we apply the DDF in a matrix-free real-space near/far evaluation and use a second-order implicit–explicit (IMEX) time integrator. Diffusion and relaxation are treated implicitly, while precession (and, when present, advection) is treated explicitly. In the implementation, the explicit precession stage uses a structure-preserving update (Rodrigues rotation at DDF quadrature points followed by anL2L^{2}projection), which enables stable multi-cycle lab-frame simulations.

Validation is challenging because general closed-form solutions are not available for nonlinear, nonlocal Bloch–DDF dynamics on bounded domains. We therefore validate against three closed-form benchmarks that isolate distinct model components: a uniform-mode DDF reduction in which the DDF enters as a deterministic kernel average, a periodic plane-wave eigenmode based on the Fourier symbol of the regularized kernel, and a purely longitudinal Neumann diffusion+T1T_{1}eigenmode on a bounded domain. These benchmarks provide parameter-free checks of phase evolution, decay rates, and boundary-condition handling. We further quantify a geometry-driven advantage of the FE formulation on curved Neumann boundaries by comparing mapped-geometry FE against a voxel-mask finite-difference baseline on a spherical Neumann eigenmode decay for a boundary-sensitive mode.

The remainder of the paper recalls the Bloch–DDF model and boundary conditions, states the weak form, sets the functional framework and operator properties, presents the FE semi-discretization and its stability, describes the time integrator and implementation details, and provides validation studies and representative dynamics. Long-time lab-frame oscillations and envelope-level DDF effects are shown inSection˜VIII(seeFigures˜3,5and7).

## IIBloch equations with distant dipolar field

LetΩ⊂ℝ3\Omega\subset\mathbb{R}^{3}be a bounded sample domain. The magnetization is a vector fieldM→​(𝐫,t)\vec{M}(\mathbf{r},t)defined at every point in time onΩ\Omega. When flow is absent or whenv→⋅𝐧^=0\vec{v}\cdot\hat{\mathbf{n}}=0on∂Ω\partial\Omega, it is natural to viewM→\vec{M}as confined toΩ\Omega. Ifv→⋅𝐧^≠0\vec{v}\cdot\hat{\mathbf{n}}\neq 0, then an inflow boundary condition is required onΓin={𝐫∈∂Ω:v→⋅𝐧^<0}\Gamma_{\mathrm{in}}=\{\mathbf{r}\in\partial\Omega:\vec{v}\cdot\hat{\mathbf{n}}<0\}and magnetization is transported across∂Ω\partial\Omega.

Write𝐑=𝐫−𝐫′\mathbf{R}=\mathbf{r}-\mathbf{r}^{\prime},R=∥𝐑∥R=\lVert\mathbf{R}\rVert, and𝐑^=𝐑/R\hat{\mathbf{R}}=\mathbf{R}/R. In high magnetic fields, the secular DDF can be written asB→d​(𝐫)=∫Ω1−3​cos2⁡θ​(𝐫,𝐫′)2​R3​[3​Mz​(𝐫′)​𝐳^−M→​(𝐫′)]​d3​𝐫′,\vec{B}_{d}(\mathbf{r})=\int_{\Omega}\frac{1-3\cos^{2}\theta(\mathbf{r},\mathbf{r}^{\prime})}{2\,R^{3}}\Bigl[\,3M_{z}(\mathbf{r}^{\prime})\,\hat{\mathbf{z}}-\vec{M}(\mathbf{r}^{\prime})\Bigr]\,d^{3}\mathbf{r}^{\prime},(1)

wherecos⁡θ​(𝐫,𝐫′)=𝐳^⋅𝐑^\cos\theta(\mathbf{r},\mathbf{r}^{\prime})=\hat{\mathbf{z}}\cdot\hat{\mathbf{R}}. Without the secular approximation, the full expression isB→​(𝐫)=∫Ω1R3​[M→​(𝐫′)−3​(M→​(𝐫′)⋅𝐑^)​𝐑^]​d3​𝐫′.\vec{B}(\mathbf{r})=\int_{\Omega}\frac{1}{R^{3}}\left[\vec{M}(\mathbf{r}^{\prime})-3\bigl(\vec{M}(\mathbf{r}^{\prime})\cdot\hat{\mathbf{R}}\bigr)\hat{\mathbf{R}}\right]\,d^{3}\mathbf{r}^{\prime}.(2)

We absorb constant prefactors (such asμ0/4​π\mu_{0}/4\pi) into units. Radiation damping or other offsets can be added as extra precession terms.

## II.1Regularized secular kernel and optional diffusion-length filtering

For analysis and for bounded-domain numerics it is convenient to regularize the short-distance singularity. We introduce a length scalea>0a>0and use the regularized secular kernelKa​(𝐫−𝐫′)\displaystyle K_{a}(\mathbf{r}-\mathbf{r}^{\prime})=1−3​cos2⁡θ​(𝐫,𝐫′)2​(R2+a2)3/2,\displaystyle=\frac{1-3\cos^{2}\theta(\mathbf{r},\mathbf{r}^{\prime})}{2\,\bigl(R^{2}+a^{2}\bigr)^{3/2}},(3)B→d​(𝐫)\displaystyle\vec{B}_{d}(\mathbf{r})=∫ΩKa​(𝐫−𝐫′)​diag​(−1,−1,2)​M→​(𝐫′)​d3​𝐫′.\displaystyle=\int_{\Omega}K_{a}(\mathbf{r}-\mathbf{r}^{\prime})\,\mathrm{diag}(-1,-1,2)\,\vec{M}(\mathbf{r}^{\prime})\,d^{3}\mathbf{r}^{\prime}.(4)

The factor1/21/2is chosen so that in the formal limita→0a\to 0one recovers the standard secular kernel in (1).
At𝐫=𝐫′\mathbf{r}=\mathbf{r}^{\prime}, the direction𝐑^\hat{\mathbf{R}}is undefined.
In the continuum integral this is immaterial (a measure-zero set), but in discrete quadrature and point-sum evaluations we enforce a consistent convention by omitting self-interactions (equivalently, setting the self-kernel contribution to zero).
In this work we develop the analysis for fixeda>0a>0, for which the induced operatorM→↦B→d​[M→]\vec{M}\mapsto\vec{B}_{d}[\vec{M}]is bounded on the Sobolev spaces used below.
From a modeling perspective,aacan be interpreted as a coarse-graining length that removes sub-resolution contributions to the dipolar field.
In computations,aaalso acts as a numerical softening scale that prevents near-field singular behavior whenB→d\vec{B}_{d}is evaluated from discrete point or quadrature samples.
For the bounded-domain simulations reported here,aais chosen as a fixed fraction of the domain length scale and is held fixed under the stated validation tests (unless otherwise stated). A strict excluded-volume model can alternatively be represented by a pair-correlation factorg​(R)g(R)withg​(R)=0g(R)=0forR<aR<aandg​(R)→1g(R)\to 1asR→∞R\to\infty, in which case one replacesKaK_{a}byKa​gK_{a}g.

In many pulse sequences, diffusion during a characteristic time windowτ\tausuppresses DDF contributions from length scales below the diffusion lengthℓD=D​τ\ell_{D}=\sqrt{D\tau}. One can model this effect by replacingM→\vec{M}in (4) by a filtered fieldM→τ=𝒢τ​[M→]\vec{M}_{\tau}=\mathcal{G}_{\tau}[\vec{M}], where𝒢τ\mathcal{G}_{\tau}denotes convolution with the Neumann heat kernel onΩ\Omega(or an equivalent FE heat-step filter). This filtering is an optional extension; the numerical experiments reported in this paper use the unfiltered regularized operator (4).

## II.2Bloch–DDF dynamics

Including diffusion, relaxation, and optional flow, the Bloch–DDF dynamics are∂M→∂t\displaystyle\frac{\partial\vec{M}}{\partial t}=γ​M→×(B→d​[M→]+δ​B→​(𝐫))−(v→​(𝐫)⋅∇)​M→\displaystyle=\gamma\,\vec{M}\times\bigl(\vec{B}_{d}[\vec{M}]+\delta\vec{B}(\mathbf{r})\bigr)-\bigl(\vec{v}(\mathbf{r})\cdot\nabla\bigr)\vec{M}+∇⋅(D​(𝐫)​∇M→)−Mx​𝐱^+My​𝐲^T2​(𝐫)+M0​(𝐫)−MzT1​(𝐫)​𝐳^,\displaystyle\quad+\nabla\cdot\bigl(D(\mathbf{r})\nabla\vec{M}\bigr)-\frac{M_{x}\,\hat{\mathbf{x}}+M_{y}\,\hat{\mathbf{y}}}{T_{2}(\mathbf{r})}+\frac{M_{0}(\mathbf{r})-M_{z}}{T_{1}(\mathbf{r})}\,\hat{\mathbf{z}},(5)

whereD​(𝐫)≥0D(\mathbf{r})\geq 0is the (scalar) diffusion coefficient (a diffusion tensor can be used without changing the main ideas),T1,2​(𝐫)T_{1,2}(\mathbf{r})may vary in space,δ​B→​(𝐫)\delta\vec{B}(\mathbf{r})is a prescribed static offset field, andv→​(𝐫)\vec{v}(\mathbf{r})is a prescribed velocity field. The total effective field entering precession isB→eff​[M→]​(𝐫)=B→d​[M→]​(𝐫)+δ​B→​(𝐫)\vec{B}_{\mathrm{eff}}[\vec{M}](\mathbf{r})=\vec{B}_{d}[\vec{M}](\mathbf{r})+\delta\vec{B}(\mathbf{r}), andγ\gammais the gyromagnetic ratio.
In the analysis we retainγ\gammaexplicitly.
In the numerical experiments and implementation we instead work in angular-frequency units by absorbingγ\gammainto the fields, i.e.,Ω→d=γ​B→d\vec{\Omega}_{d}=\gamma\,\vec{B}_{d}andδ​Ω→=γ​δ​B→\delta\vec{\Omega}=\gamma\,\delta\vec{B}, so the precession term is written asM→×(Ω→d+δ​Ω→)\vec{M}\times(\vec{\Omega}_{d}+\delta\vec{\Omega}).
Accordingly, when we specify a uniform offsetω\omegaor gradientgzg_{z}, we state whether it is given in field units or in angular-frequency units; in the analytical benchmarks below,ω\omegadenotes a field offset so the corresponding angular frequency isγ​ω\gamma\,\omega.

We write the transport term in advective form,∂tM→+(v→⋅∇)​M→=⋯\partial_{t}\vec{M}+(\vec{v}\cdot\nabla)\vec{M}=\cdots,
equivalently, (5) with the advection term moved to the
left-hand side. The system is supplemented by reflective diffusion boundary
conditions in the no-flux form𝐧^⋅(D​(𝐫)​∇M→)=0\hat{\mathbf{n}}\cdot\bigl(D(\mathbf{r})\nabla\vec{M}\bigr)=0on∂Ω\partial\Omega, understood componentwise. For scalar diffusion withD​(𝐫)>0D(\mathbf{r})>0near the boundary, this reduces to𝐧^⋅∇M→=0\hat{\mathbf{n}}\cdot\nabla\vec{M}=0. If advection is included andv→⋅𝐧^≠0\vec{v}\cdot\hat{\mathbf{n}}\neq 0on∂Ω\partial\Omega, an inflow boundary
condition forM→\vec{M}is additionally required onΓin\Gamma_{\mathrm{in}}. In the numerical experiments considered here,v→≡0\vec{v}\equiv 0, so no advection term appears in the computed cases.

These equations are the basis for the weak formulation in §II.3.

## II.3Weak solutions

LetΩ⊂ℝ3\Omega\subset\mathbb{R}^{3}be a bounded Lipschitz domain with boundary∂Ω\partial\Omegaand outward unit normal𝐧^\hat{\mathbf{n}}. The magnetization is a vector fieldM→​(𝐫,t)\vec{M}(\mathbf{r},t)defined onΩ\Omega. We include static offsetsδ​B→​(𝐫)\delta\vec{B}(\mathbf{r})and the DDFB→d​[M→]\vec{B}_{d}[\vec{M}]. We allow spatial variation inT1,2​(𝐫)T_{1,2}(\mathbf{r})andD​(𝐫)D(\mathbf{r}). For reflective diffusion boundaries we impose the homogeneous no-flux condition𝐧^⋅(D​(𝐫)​∇M→)=0on​∂Ω,\hat{\mathbf{n}}\cdot\bigl(D(\mathbf{r})\nabla\vec{M}\bigr)=0\quad\text{on }\partial\Omega,(6)

understood componentwise.
For scalarD​(𝐫)D(\mathbf{r})withD​(𝐫)>0D(\mathbf{r})>0near∂Ω\partial\Omega, this is equivalent to𝐧^⋅∇M→=0\hat{\mathbf{n}}\cdot\nabla\vec{M}=0. If advection is included andv→⋅𝐧^≠0\vec{v}\cdot\hat{\mathbf{n}}\neq 0on∂Ω\partial\Omega, an inflow boundary condition onΓin={𝐫∈∂Ω:v→⋅𝐧^<0}\Gamma_{\mathrm{in}}=\{\mathbf{r}\in\partial\Omega:\vec{v}\cdot\hat{\mathbf{n}}<0\}is also required; for simplicity, the analysis below emphasizes the casev→⋅𝐧^=0\vec{v}\cdot\hat{\mathbf{n}}=0when flow is present.

In component form (i=1,2,3i=1,2,3), withB→≡B→d​[M→]\vec{B}\equiv\vec{B}_{d}[\vec{M}]andϵi​j​k\epsilon_{ijk}denoting the Levi–Civita symbol, the Bloch–DDF system
reads∂Mi∂t\displaystyle\frac{\partial M_{i}}{\partial t}=γ​ϵi​j​k​Mj​(Bk+δ​Bk)−δi​1​M1+δi​2​M2T2​(𝐫)\displaystyle=\gamma\,\epsilon_{ijk}\,M_{j}\bigl(B_{k}+\delta B_{k}\bigr)-\frac{\delta_{i1}M_{1}+\delta_{i2}M_{2}}{T_{2}(\mathbf{r})}(7)+δi​3​M0​(𝐫)−M3T1​(𝐫)\displaystyle\quad+\delta_{i3}\,\frac{M_{0}(\mathbf{r})-M_{3}}{T_{1}(\mathbf{r})}+∇⋅(D​(𝐫)​∇Mi)−(v→​(𝐫)⋅∇)​Mi,\displaystyle\quad+\nabla\cdot\bigl(D(\mathbf{r})\nabla M_{i}\bigr)-\bigl(\vec{v}(\mathbf{r})\cdot\nabla\bigr)M_{i},

for𝐫∈Ω\mathbf{r}\in\Omega. The advection sign convention in
(7) is therefore consistent with the advective form∂tMi+(v→⋅∇)​Mi=⋯\partial_{t}M_{i}+(\vec{v}\cdot\nabla)M_{i}=\cdots. If∇⋅v→=0\nabla\cdot\vec{v}=0, this is equivalent to the conservative form∂tMi+∇⋅(v→​Mi)=⋯\partial_{t}M_{i}+\nabla\cdot(\vec{v}\,M_{i})=\cdots.

LetV:=H1​(Ω)V:=H^{1}(\Omega)and take any test functionvi∈Vv_{i}\in V. Multiply (7) byviv_{i}and integrate overΩ\Omega:∫Ω∂Mi∂t​vi​d3​𝐫\displaystyle\int_{\Omega}\frac{\partial M_{i}}{\partial t}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}=γ​∑j,k=13ϵi​j​k​∫ΩMj​(Bk+δ​Bk)​vi​d3​𝐫\displaystyle=\gamma\sum_{j,k=1}^{3}\epsilon_{ijk}\int_{\Omega}M_{j}(B_{k}+\delta B_{k})\,v_{i}\,\mathrm{d}^{3}\mathbf{r}(8)−∫Ωδi​1​M1+δi​2​M2T2​(𝐫)​vi​d3​𝐫\displaystyle\quad-\int_{\Omega}\frac{\delta_{i1}M_{1}+\delta_{i2}M_{2}}{T_{2}(\mathbf{r})}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}−∫Ωδi​3​M3T1​(𝐫)​vi​d3​𝐫+∫Ω∇⋅(D​(𝐫)​∇Mi)​vi​d3​𝐫\displaystyle\quad-\int_{\Omega}\frac{\delta_{i3}M_{3}}{T_{1}(\mathbf{r})}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}+\int_{\Omega}\nabla\cdot\bigl(D(\mathbf{r})\nabla M_{i}\bigr)\,v_{i}\,\mathrm{d}^{3}\mathbf{r}−∫Ω(v→​(𝐫)⋅∇Mi)​vi​d3​𝐫+∫ΩM0​(𝐫)T1​(𝐫)​δi​3​vi​d3​𝐫.\displaystyle\quad-\int_{\Omega}\bigl(\vec{v}(\mathbf{r})\cdot\nabla M_{i}\bigr)\,v_{i}\,\mathrm{d}^{3}\mathbf{r}+\int_{\Omega}\frac{M_{0}(\mathbf{r})}{T_{1}(\mathbf{r})}\,\delta_{i3}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}.

Integrate the diffusion term by parts:∫Ω∇⋅(D​(𝐫)​∇Mi)​vi​d3​𝐫=−∫ΩD​(𝐫)​∇Mi⋅∇vi​d3​𝐫+∫∂Ωvi​𝐧^⋅(D​(𝐫)​∇Mi)​dS.\int_{\Omega}\nabla\cdot\bigl(D(\mathbf{r})\nabla M_{i}\bigr)\,v_{i}\,\mathrm{d}^{3}\mathbf{r}=-\int_{\Omega}D(\mathbf{r})\,\nabla M_{i}\cdot\nabla v_{i}\,\mathrm{d}^{3}\mathbf{r}\\
+\int_{\partial\Omega}v_{i}\,\hat{\mathbf{n}}\cdot\bigl(D(\mathbf{r})\nabla M_{i}\bigr)\,\mathrm{d}S.(9)

Under the homogeneous Neumann condition (6), the boundary term vanishes; for scalarD​(𝐫)D(\mathbf{r}),𝐧^⋅∇Mi=0\hat{\mathbf{n}}\cdot\nabla M_{i}=0implies𝐧^⋅(D​∇Mi)=0\hat{\mathbf{n}}\cdot(D\nabla M_{i})=0.

For advection we denote byaadv​(Mi,vi)a_{\mathrm{adv}}(M_{i},v_{i})the bilinear form
used in the weak formulation. In the energy-neutral case, assume∇⋅v→=0\nabla\cdot\vec{v}=0inΩ\Omegaandv→⋅𝐧^=0\vec{v}\cdot\hat{\mathbf{n}}=0on∂Ω\partial\Omega, and defineaadv​(Mi,vi):=12​∫Ω(v→⋅∇Mi)​vi​d3​𝐫−12​∫Ω(v→⋅∇vi)​Mi​d3​𝐫.a_{\mathrm{adv}}(M_{i},v_{i}):=\frac{1}{2}\int_{\Omega}(\vec{v}\cdot\nabla M_{i})\,v_{i}\,\mathrm{d}^{3}\mathbf{r}-\frac{1}{2}\int_{\Omega}(\vec{v}\cdot\nabla v_{i})\,M_{i}\,\mathrm{d}^{3}\mathbf{r}.(10)

With this choice,aadv​(Mi,Mi)=0a_{\mathrm{adv}}(M_{i},M_{i})=0for each component. If these
conditions do not hold, one may instead use the standard advective bilinear
formaadv​(Mi,vi):=∫Ω(v→⋅∇Mi)​vi​d3​𝐫,a_{\mathrm{adv}}(M_{i},v_{i}):=\int_{\Omega}(\vec{v}\cdot\nabla M_{i})\,v_{i}\,\mathrm{d}^{3}\mathbf{r},(11)

together with the appropriate inflow/outflow boundary terms.

## Definition II.1(Weak form of the Bloch–DDF system).

With reflective diffusion boundaries, the weak form is: for each componentiiand for allvi∈H1​(Ω)v_{i}\in H^{1}(\Omega),∫Ω∂Mi∂t​vi​d3​𝐫\displaystyle\int_{\Omega}\frac{\partial M_{i}}{\partial t}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}=γ​∑j,k=13ϵi​j​k​∫ΩMj​(Bk+δ​Bk)​vi​d3​𝐫\displaystyle=\gamma\sum_{j,k=1}^{3}\epsilon_{ijk}\int_{\Omega}M_{j}\bigl(B_{k}+\delta B_{k}\bigr)\,v_{i}\,\mathrm{d}^{3}\mathbf{r}(12)−∫Ωδi​1​M1+δi​2​M2T2​(𝐫)​vi​d3​𝐫\displaystyle\quad-\int_{\Omega}\frac{\delta_{i1}M_{1}+\delta_{i2}M_{2}}{T_{2}(\mathbf{r})}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}−∫Ωδi​3​M3T1​(𝐫)​vi​d3​𝐫\displaystyle\quad-\int_{\Omega}\frac{\delta_{i3}M_{3}}{T_{1}(\mathbf{r})}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}−∫ΩD​(𝐫)​∇Mi⋅∇vi​d3​𝐫\displaystyle\quad-\int_{\Omega}D(\mathbf{r})\,\nabla M_{i}\cdot\nabla v_{i}\,\mathrm{d}^{3}\mathbf{r}−aadv​(Mi,vi)\displaystyle\quad-a_{\mathrm{adv}}(M_{i},v_{i})+∫ΩM0​(𝐫)T1​(𝐫)​δi​3​vi​d3​𝐫.\displaystyle\quad+\int_{\Omega}\frac{M_{0}(\mathbf{r})}{T_{1}(\mathbf{r})}\,\delta_{i3}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}.

whereB→=B→d​[M→]\vec{B}=\vec{B}_{d}[\vec{M}]. When the skew form
(10) is used, we assume∇⋅v→=0\nabla\cdot\vec{v}=0inΩ\Omegaandv→⋅𝐧^=0\vec{v}\cdot\hat{\mathbf{n}}=0on∂Ω\partial\Omega. If the standard
advective form (11) is used instead, then the
corresponding inflow/outflow boundary terms must be included.

For the numerical approximation we use a conforming Galerkin method.

## Definition II.2(Galerkin FE formulation).

LetVh⊂H1​(Ω)V_{h}\subset H^{1}(\Omega)be a finite-dimensional space of scalar shape functions withdimVh=Nh\dim V_{h}=N_{h}. Seekuih​(𝐫,t)=∑n=1Nhwi​n​(t)​φn​(𝐫)∈Vhu_{i}^{h}(\mathbf{r},t)=\sum_{n=1}^{N_{h}}w_{in}(t)\,\varphi_{n}(\mathbf{r})\in V_{h}(i=1,2,3i=1,2,3) such that, for allvi=φm∈Vhv_{i}=\varphi_{m}\in V_{h},∫Ω∂uih∂t​vi​d3​𝐫\displaystyle\int_{\Omega}\frac{\partial u_{i}^{h}}{\partial t}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}=γ​∑j,k=13ϵi​j​k​∫Ωujh​(Bk​[uh]+δ​Bk)​vi​d3​𝐫\displaystyle=\gamma\sum_{j,k=1}^{3}\epsilon_{ijk}\int_{\Omega}u_{j}^{h}\bigl(B_{k}[u^{h}]+\delta B_{k}\bigr)\,v_{i}\,\mathrm{d}^{3}\mathbf{r}(13)−∫Ωδi​1​u1h+δi​2​u2hT2​(𝐫)​vi​d3​𝐫\displaystyle\quad-\int_{\Omega}\frac{\delta_{i1}u_{1}^{h}+\delta_{i2}u_{2}^{h}}{T_{2}(\mathbf{r})}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}−∫Ωδi​3​u3hT1​(𝐫)​vi​d3​𝐫\displaystyle\quad-\int_{\Omega}\frac{\delta_{i3}u_{3}^{h}}{T_{1}(\mathbf{r})}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}−∫ΩD​(𝐫)​∇uih⋅∇vi​d3​𝐫\displaystyle\quad-\int_{\Omega}D(\mathbf{r})\,\nabla u_{i}^{h}\cdot\nabla v_{i}\,\mathrm{d}^{3}\mathbf{r}−aadv​(uih,vi)\displaystyle\quad-a_{\mathrm{adv}}(u_{i}^{h},v_{i})+∫ΩM0​(𝐫)T1​(𝐫)​δi​3​vi​d3​𝐫.\displaystyle\quad+\int_{\Omega}\frac{M_{0}(\mathbf{r})}{T_{1}(\mathbf{r})}\,\delta_{i3}\,v_{i}\,\mathrm{d}^{3}\mathbf{r}.

HereBk​[uh]B_{k}[u^{h}]is thekkth component of the DDF evaluated fromuhu^{h}via the chosen DDF kernel (e.g., (1) or the regularized form (4)).

Remarks.The Galerkin method enforces orthogonality of the residual to the test spaceVhV_{h}in the sense of (13). Under standard regularity assumptions,uhu^{h}converges to the weak solution as the mesh is refined[18]. The diffusion term is well-defined forH1​(Ω)H^{1}(\Omega)fields. For advection, one may use a conservative or skew-symmetric form (for example, (10) when admissible) and add stabilization (such as SUPG) in advection-dominated regimes without changing the structure of (13).

Choose a scalar FE basis{φn}n=1Nh⊂H1​(Ω)\{\varphi_{n}\}_{n=1}^{N_{h}}\subset H^{1}(\Omega)and expand each component asuih​(𝐫,t)\displaystyle u_{i}^{h}(\mathbf{r},t)=∑n=1Nhwi​n​(t)​φn​(𝐫),i∈{1,2,3},\displaystyle=\sum_{n=1}^{N_{h}}w_{in}(t)\,\varphi_{n}(\mathbf{r}),\quad i\in\{1,2,3\},(14)

wherewi​n​(t)w_{in}(t)are the unknown coefficients. Testing (13) withvi=φmv_{i}=\varphi_{m}defines the standard FE operatorsMm​n\displaystyle M_{mn}=∫Ωφn​(𝐫)​φm​(𝐫)​d3​𝐫,\displaystyle=\int_{\Omega}\varphi_{n}(\mathbf{r})\,\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r},(15)Km​n\displaystyle K_{mn}=∫ΩD​(𝐫)​∇φn​(𝐫)⋅∇φm​(𝐫)​d3​𝐫,\displaystyle=\int_{\Omega}D(\mathbf{r})\,\nabla\varphi_{n}(\mathbf{r})\cdot\nabla\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r},(16)(S1)m​n\displaystyle(S_{1})_{mn}=∫Ω1T1​(𝐫)​φn​(𝐫)​φm​(𝐫)​d3​𝐫,\displaystyle=\int_{\Omega}\frac{1}{T_{1}(\mathbf{r})}\,\varphi_{n}(\mathbf{r})\,\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r},(17)(S2)m​n\displaystyle(S_{2})_{mn}=∫Ω1T2​(𝐫)​φn​(𝐫)​φm​(𝐫)​d3​𝐫,\displaystyle=\int_{\Omega}\frac{1}{T_{2}(\mathbf{r})}\,\varphi_{n}(\mathbf{r})\,\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r},(18)(bT1)m\displaystyle(b_{T_{1}})_{m}=∫ΩM0​(𝐫)T1​(𝐫)​φm​(𝐫)​d3​𝐫.\displaystyle=\int_{\Omega}\frac{M_{0}(\mathbf{r})}{T_{1}(\mathbf{r})}\,\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r}.(19)

For advection, we distinguish the non-skew and skew-symmetric discrete operators. The non-skew operator associated with the strong form−(v→⋅∇)​Mi-(\vec{v}\cdot\nabla)M_{i}is(Nv)m​n=−∫Ω(v→​(𝐫)⋅∇φn​(𝐫))​φm​(𝐫)​d3​𝐫.(N_{v})_{mn}=-\int_{\Omega}\bigl(\vec{v}(\mathbf{r})\cdot\nabla\varphi_{n}(\mathbf{r})\bigr)\,\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r}.(20)

When∇⋅v→=0\nabla\cdot\vec{v}=0andv→⋅𝐧^=0\vec{v}\cdot\hat{\mathbf{n}}=0on∂Ω\partial\Omega, an energy-neutral alternative is the skew form(Nvskew)m​n=−12​∫Ω(v→⋅∇φn)​φm​d3​𝐫+12​∫Ω(v→⋅∇φm)​φn​d3​𝐫.(N_{v}^{\mathrm{skew}})_{mn}=-\frac{1}{2}\int_{\Omega}\bigl(\vec{v}\cdot\nabla\varphi_{n}\bigr)\,\varphi_{m}\,\mathrm{d}^{3}\mathbf{r}+\frac{1}{2}\int_{\Omega}\bigl(\vec{v}\cdot\nabla\varphi_{m}\bigr)\,\varphi_{n}\,\mathrm{d}^{3}\mathbf{r}.(21)

In the numerical experiments reported in this paper we takev→≡0\vec{v}\equiv 0, soNv=0N_{v}=0and advection is omitted from the computed cases; we includeNvN_{v}here to state the general weak form and to support extensions.

Letwi=(wi​1,…,wi​Nh)⊤w_{i}=(w_{i1},\dots,w_{iN_{h}})^{\top}. The semi-discrete system (with the mass matrix retained) readsM​w˙i\displaystyle M\,\dot{w}_{i}=γ​𝒫i​(w)−δi​1​S2​w1−δi​2​S2​w2\displaystyle=\gamma\,\mathcal{P}_{i}(w)-\delta_{i1}\,S_{2}\,w_{1}-\delta_{i2}\,S_{2}\,w_{2}(22)−δi​3​S1​w3−K​wi+Nv​wi+δi​3​bT1,i=1,2,3.\displaystyle\quad-\delta_{i3}\,S_{1}\,w_{3}-K\,w_{i}+N_{v}\,w_{i}+\delta_{i3}\,b_{T_{1}},\quad i=1,2,3.

where𝒫i​(w)\mathcal{P}_{i}(w)is the discrete precession contribution induced by the DDF and any static offset fieldδ​B→\delta\vec{B}. In the energy and stability results we will assume eitherNv=NvskewN_{v}=N_{v}^{\mathrm{skew}}(when admissible) or else we will explicitly account for the symmetric part ofNvN_{v}.

Given coefficient vectorsww, we proceed in three steps. First, evaluate the FE fieldsMjh​(𝐫)=∑nwj​n​φn​(𝐫)M_{j}^{h}(\mathbf{r})=\sum_{n}w_{jn}\varphi_{n}(\mathbf{r})at the chosen DDF quadrature points{𝐫q}q=1Nq\{\mathbf{r}_{q}\}_{q=1}^{N_{q}}. Second, compute the DDF fieldB→d​(𝐫q)\vec{B}_{d}(\mathbf{r}_{q})fromM→h\vec{M}^{h}using the chosen DDF kernel (e.g., (1) or the regularized form (4)). In the reference implementation,B→d\vec{B}_{d}is evaluated in real space by either a direct all-pairs sum over source points for small problem sizes or validation runs, or a Barnes–Hut octree approximation for larger problems. In the Barnes–Hut mode, source points are grouped in an octree; a target point accepts a node’s aggregated contribution when the opening criterions/d≤θs/d\leq\thetais satisfied, wheressis the node size andddis the distance from the target to the node center.
When a node is accepted, we approximate its contribution using the node’s aggregated magnetization (monopole) together with the full regularized secular kernelKa​(𝐑)K_{a}(\mathbf{R})evaluated with𝐑\mathbf{R}taken as the vector from the target point to the node center (so the angular factor1−3​cos2⁡θ1-3\cos^{2}\thetais retained).
The diagonal factordiag​(−1,−1,2)\mathrm{diag}(-1,-1,2)is applied as in (4).
When the opening criterion fails, we fall back to direct summation over the node’s children, and ultimately over leaf contents.
The user-controlled parameters are the opening angleθ\thetaand the leaf size (maximum points per leaf).
In practice, we validate these choices by comparing the tree-based fieldB→dtree​(𝐫q)\vec{B}_{d}^{\mathrm{tree}}(\mathbf{r}_{q})against the direct all-pairs fieldB→ddirect​(𝐫q)\vec{B}_{d}^{\mathrm{direct}}(\mathbf{r}_{q})on representative small meshes and choose(θ,leaf size)(\theta,\text{leaf size})so that the resulting relative field error remains below the time-discretization error in the reported runs. Third, assemble, for eachiiand each test indexmm,[𝒫i​(w)]m=∑j,k=13ϵi​j​k​∫ΩMjh​(𝐫)​Bk​(𝐫)​φm​(𝐫)​d3​𝐫.\bigl[\mathcal{P}_{i}(w)\bigr]_{m}=\sum_{j,k=1}^{3}\epsilon_{ijk}\int_{\Omega}M_{j}^{h}(\mathbf{r})\,B_{k}(\mathbf{r})\,\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r}.(23)

In the implementation, the integral in (23) is evaluated by the same quadrature rule used to define the DDF quadrature points, i.e.,[𝒫i​(w)]m≈∑j,k=13ϵi​j​k​∑q=1Nqwq​Mjh​(𝐫q)​Bk​(𝐫q)​φm​(𝐫q).\bigl[\mathcal{P}_{i}(w)\bigr]_{m}\approx\sum_{j,k=1}^{3}\epsilon_{ijk}\sum_{q=1}^{N_{q}}w_{q}\,M_{j}^{h}(\mathbf{r}_{q})\,B_{k}(\mathbf{r}_{q})\,\varphi_{m}(\mathbf{r}_{q}).

If one prefers a fully assembled representation, defineRk​n​m\displaystyle R_{k\,nm}=∫Ωδ​Bk​(𝐫)​φn​(𝐫)​φm​(𝐫)​d3​𝐫,\displaystyle=\int_{\Omega}\delta B_{k}(\mathbf{r})\,\varphi_{n}(\mathbf{r})\,\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r},(24)Tk​n​m​q\displaystyle T_{k\,nmq}=ak​∫Ω∫Ωφn​(𝐫)​φm​(𝐫)​KDDF​(𝐫,𝐫′)​φq​(𝐫′)​d3​𝐫′​d3​𝐫,\displaystyle=a_{k}\int_{\Omega}\!\int_{\Omega}\varphi_{n}(\mathbf{r})\,\varphi_{m}(\mathbf{r})\,K_{\mathrm{DDF}}(\mathbf{r},\mathbf{r}^{\prime})\,\varphi_{q}(\mathbf{r}^{\prime})\,\mathrm{d}^{3}\mathbf{r}^{\prime}\,\mathrm{d}^{3}\mathbf{r},(25)

witha1=a2=−1a_{1}=a_{2}=-1anda3=2a_{3}=2. HereKDDF​(𝐫,𝐫′)K_{\mathrm{DDF}}(\mathbf{r},\mathbf{r}^{\prime})denotes the scalar DDF kernel used in the model; for the regularized secular choice it isKa​(𝐫−𝐫′)K_{a}(\mathbf{r}-\mathbf{r}^{\prime})from (3), and for the unregularized secular kernel it is(1−3​cos2⁡θ​(𝐫,𝐫′))/(2​∥𝐫−𝐫′∥3)(1-3\cos^{2}\theta(\mathbf{r},\mathbf{r}^{\prime}))/(2\lVert\mathbf{r}-\mathbf{r}^{\prime}\rVert^{3})interpreted in the principal-value sense.

Then[𝒫i​(w)]m\displaystyle\bigl[\mathcal{P}_{i}(w)\bigr]_{m}=∑j,k=13ϵi​j​k[∑n,q=1Nhwj​nwk​qTk​n​m​q\displaystyle=\sum_{j,k=1}^{3}\epsilon_{ijk}\Biggl[\sum_{n,q=1}^{N_{h}}w_{jn}\,w_{kq}\,T_{k\,nmq}(26)+∑n=1Nhwj​nRk​n​m].\displaystyle\quad\quad\quad+\sum_{n=1}^{N_{h}}w_{jn}\,R_{k\,nm}\Biggr].

In practice we do not assembleTk​n​m​qT_{k\,nmq}; the matrix-free approach above controls memory and cost and is the implementation used inSection˜VIandSection˜II.4.

## II.4Time integration

We advance (22) with a second-order IMEX Strang splitting method. Physically, diffusion and relaxation are the stiff, dissipative processes in the Bloch–Torrey dynamics, so they are advanced implicitly to avoid a severe stability restriction. By contrast, precession is non-dissipative and acts locally as a rotation of the magnetization, which makes an explicit rotation-based update natural for this part of the dynamics. Diffusion and relaxation are treated implicitly, while precession is treated explicitly. For the precession stage, the reference implementation uses a structure-preserving update that rotates the magnetization at DDF quadrature points with a Rodrigues map and then projects back to nodal coefficients by anL2L^{2}projection (mass solve). This choice is important for stable multi-cycle lab-frame simulations such as those inFigure˜3. TheL2L^{2}projection does not formM−1M^{-1}explicitly; it only requires a
sparse solve with the SPD mass matrix.

Letw=(w1,w2,w3)w=(w_{1},w_{2},w_{3}), define the block operatorsℳ=\displaystyle\mathcal{M}=blkdiag​(M,M,M),\displaystyle\mathrm{blkdiag}(M,M,M),𝒦=\displaystyle\mathcal{K}=blkdiag​(K,K,K),\displaystyle\mathrm{blkdiag}(K,K,K),𝒮=\displaystyle\mathcal{S}=blkdiag​(S2,S2,S1),\displaystyle\mathrm{blkdiag}(S_{2},S_{2},S_{1}),

and the source vectorf=(0,0,bT1)f=(0,0,b_{T_{1}}).
One time step fromtnt^{n}totn+1=tn+Δ​tt^{n+1}=t^{n}+\Delta tproceeds as follows.(i)(ℳ+Δ​t4​(𝒦+𝒮))​w(a)=(ℳ−Δ​t4​(𝒦+𝒮))​wn+Δ​t2​f.\displaystyle\bigl(\mathcal{M}+\tfrac{\Delta t}{4}(\mathcal{K}+\mathcal{S})\bigr)\,w^{(a)}=\bigl(\mathcal{M}-\tfrac{\Delta t}{4}(\mathcal{K}+\mathcal{S})\bigr)\,w^{n}+\frac{\Delta t}{2}\,f.(27)

To describe the explicit precession stage, let{𝐫q}q=1Nq⊂Ω\{\mathbf{r}_{q}\}_{q=1}^{N_{q}}\subset\Omegabe the DDF quadrature points with weights{wq}q=1Nq\{w_{q}\}_{q=1}^{N_{q}}. Given coefficientsww, define the quadrature-point magnetizationM→q=M→h​(𝐫q)\vec{M}_{q}=\vec{M}_{h}(\mathbf{r}_{q})and the corresponding effective angular-frequency fieldΩ→q​(w)=γ​(δ​B→​(𝐫q)+B→d​[M→h]​(𝐫q)),\vec{\Omega}_{q}(w)=\gamma\Bigl(\delta\vec{B}(\mathbf{r}_{q})+\vec{B}_{d}[\vec{M}_{h}](\mathbf{r}_{q})\Bigr),

evaluated using the same quadrature rules as in (23). Letℛτ​(⋅;Ω→)\mathcal{R}_{\tau}(\cdot;\vec{\Omega})denote the Rodrigues rotation that mapsm→∈ℝ3\vec{m}\in\mathbb{R}^{3}to the solution at timeτ\tauofm→˙=m→×Ω→\dot{\vec{m}}=\vec{m}\times\vec{\Omega}with constant angular-frequency fieldΩ→∈ℝ3\vec{\Omega}\in\mathbb{R}^{3}. LetΠh\Pi_{h}denote the componentwiseL2L^{2}projection from quadrature-point values back to FE coefficients: given values{uq}q=1Nq\{u_{q}\}_{q=1}^{N_{q}}, the projected coefficientsuh=∑n=1Nhcn​φnu_{h}=\sum_{n=1}^{N_{h}}c_{n}\varphi_{n}satisfyM​c=pMc=pwithpm=∑q=1Nqwq​uq​φm​(𝐫q)p_{m}=\sum_{q=1}^{N_{q}}w_{q}\,u_{q}\,\varphi_{m}(\mathbf{r}_{q}).(ii)M→q(a)=M→h(a)​(𝐫q),Ω→q(a)=Ω→q​(w(a)),\displaystyle\vec{M}_{q}^{(a)}=\vec{M}_{h}^{(a)}(\mathbf{r}_{q}),\quad\vec{\Omega}_{q}^{(a)}=\vec{\Omega}_{q}\!\bigl(w^{(a)}\bigr),(28)M→~q=ℛΔ​t/2​(M→q(a);Ω→q(a)),w~=Πh​(M→~).\displaystyle\tilde{\vec{M}}_{q}=\mathcal{R}_{\Delta t/2}\!\bigl(\vec{M}_{q}^{(a)};\vec{\Omega}_{q}^{(a)}\bigr),\quad\tilde{w}=\Pi_{h}(\tilde{\vec{M}}).(iii)Ω→q(1/2)=Ω→q​(w~),\displaystyle\vec{\Omega}_{q}^{(1/2)}=\vec{\Omega}_{q}(\tilde{w}),(29)M→q(b)=ℛΔ​t​(M→q(a);Ω→q(1/2)),w(b)=Πh​(M→(b)).\displaystyle\vec{M}_{q}^{(b)}=\mathcal{R}_{\Delta t}\!\bigl(\vec{M}_{q}^{(a)};\vec{\Omega}_{q}^{(1/2)}\bigr),\quad w^{(b)}=\Pi_{h}(\vec{M}^{(b)}).

If advection is included, it is advanced explicitly with the same midpoint predictor, usingw~\tilde{w}as the midpoint state, and applied as an additional update tow(b)w^{(b)}. In the numerical experiments reported here we takev→≡0\vec{v}\equiv 0, so the explicit stage consists only of (28)–(29). In the implementation, a spatially uniform term inδ​B→\delta\vec{B}(for example,ω​𝐳^\omega\,\hat{\mathbf{z}}) may be applied by an exact𝐳^\hat{\mathbf{z}}-axis rotation before and after the DDF-driven rotation; this is equivalent to including it in the Rodrigues map above after converting to an angular frequency fieldΩ→=γ​(B→d+δ​B→)\vec{\Omega}=\gamma(\vec{B}_{d}+\delta\vec{B}). Accordingly, the angular-frequency quantities entering the Rodrigues map areγ​ω\gamma\,\omegaandγ​gz\gamma\,g_{z}whenω\omegaandgzg_{z}are specified in field units.(iv)(ℳ+Δ​t4​(𝒦+𝒮))​wn+1\displaystyle\Bigl(\mathcal{M}+\tfrac{\Delta t}{4}(\mathcal{K}+\mathcal{S})\Bigr)\,w^{n+1}(30)=(ℳ−Δ​t4​(𝒦+𝒮))​w(b)+Δ​t2​f.\displaystyle\quad=\Bigl(\mathcal{M}-\tfrac{\Delta t}{4}(\mathcal{K}+\mathcal{S})\Bigr)\,w^{(b)}+\tfrac{\Delta t}{2}\,f.

Steps (27) and (30) are linear solves with a symmetric positive definite left-hand side whenD​(𝐫)≥0D(\mathbf{r})\geq 0andT1,2​(𝐫)>0T_{1,2}(\mathbf{r})>0. In the reference implementation we solve these systems either by sparse direct factorization (reused across time steps when coefficients are constant) or by conjugate gradients with a preconditioner (for example, AMG or incomplete factorization). The explicit stage (28)–(29) evaluates the precession load by first computing the DDF field at quadrature points and then applying the pointwise Rodrigues map followed by anL2L^{2}projection; this uses the same quadrature rules as the matrix-free construction (23). In physical terms, this explicit substep isolates the rotational part of the dynamics: during this stage the magnetization is rotated by the local effective field rather than damped. When advection is included, its action is also applied explicitly using the midpoint statew~\tilde{w}.

The scheme is second order in time for sufficiently smooth solutions. Its
local truncation error isO​(Δ​t3)O(\Delta t^{3}), and its global error isO​(Δ​t2)O(\Delta t^{2}). The implicit Crank–Nicolson substeps are unconditionally
stable for the diffusion and relaxation terms. Accordingly, the time-step
restriction is not set by diffusion or relaxation, because those stiff
dissipative processes are handled implicitly. Instead, it is set by the
explicit part of the algorithm, namely the rate at which the effective
precession field, and any explicitly treated transport, can change the
magnetization over one time step. Thus, any time-step restriction is driven
by the explicit stage and depends on bounds for the effective precession rate
and, if advection is included, on bounds for the transport rate. In the
numerical experiments reported here we takev→≡0\vec{v}\equiv 0, so the explicit
restriction is determined only by precession. In particular, a sufficient
condition isΔ​t≤c​(|γ|​‖δ​B→‖L∞​(Ω)+|γ|​‖𝒯a‖L2→L2​supn‖wn‖M)−1,\Delta t\leq c\,\Bigl(|\gamma|\,\|\delta\vec{B}\|_{L^{\infty}(\Omega)}+|\gamma|\,\|\mathcal{T}_{a}\|_{L^{2}\to L^{2}}\,\sup_{n}\|w^{n}\|_{M}\Bigr)^{-1},

wherec>0c>0is independent of the mesh size and‖w‖M2=∑i=13wi⊤​M​wi\|w\|_{M}^{2}=\sum_{i=1}^{3}w_{i}^{\top}Mw_{i}. If advection is included, an
additional contribution proportional to‖v→‖W1,∞​(Ω)\|\vec{v}\|_{W^{1,\infty}(\Omega)}enters the sufficient condition.
This makes the role of the IMEX splitting transparent: the implicit part
removes the fast diffusive and relaxational stability barrier, while the
explicit restriction tracks only the physically nondissipative precessional
rotation and any explicitly retained transport. The stability results inSection˜VIImake the dependence on precession and transport
bounds precise. They also allow either the skew advection operator
(21), which is energy-neutral when admissible, or a
controlled contribution from the symmetric part ofNvN_{v}.

Remarks.(a) If advection is included and∇⋅v→=0\nabla\cdot\vec{v}=0andv→⋅𝐧^=0\vec{v}\cdot\hat{\mathbf{n}}=0on∂Ω\partial\Omega,
then the skew formNvskewN_{v}^{\mathrm{skew}}in (21) is
energy-neutral and reduces artificial energy growth. (b) Mass lumping is not
used by default because it perturbs theMM-inner-product identities used in
the stability analysis; it may be enabled for fully explicit variants when a
different stability argument is adopted. (c) If a far-field DDF approximation
is used, its tolerance should be coupled toΔ​t\Delta tso that the induced
defect in discrete skew-symmetry does not dominate the time discretization
error. (d) The Rodrigues map preserves|M→||\vec{M}|pointwise at the DDF
quadrature points during the explicit precession substep for fixedΩ→q\vec{\Omega}_{q}. The subsequentL2L^{2}projectionΠh\Pi_{h}preserves the
discreteL2L^{2}structure used in the energy estimates, but it does not in
general preserve the pointwise magnetization magnitude at FE nodes.(a)(b)(c)Figure 1:Uniform-mode analytical benchmark.
NumericalS​(t)=⟨Mx+i​My⟩S(t)=\langle M_{x}+iM_{y}\rangle(from the FE run), where⟨⋅⟩\langle\cdot\rangledenotes the spatial average overΩ\Omegaof the corresponding FE field, compared against the closed-form solution (42) withκeff\kappa_{\mathrm{eff}}computed directly from the regularized kernel and the stated quadrature rule.
Panels showRe​S​(t)\mathrm{Re}\,S(t),Im​S​(t)\mathrm{Im}\,S(t), and|S​(t)||S(t)|.

## IIIFunctional setting and assumptions

LetΩ⊂ℝ3\Omega\subset\mathbb{R}^{3}be a bounded Lipschitz domain with outward unit normal𝐧^\hat{\mathbf{n}}. Vector fields are treated componentwise in the standard Sobolev spacesL2​(Ω)L^{2}(\Omega)andH1​(Ω)H^{1}(\Omega).

AssumeD∈L∞​(Ω)D\in L^{\infty}(\Omega)withD​(𝐫)≥Dmin>0D(\mathbf{r})\geq D_{\min}>0almost everywhere. (A symmetric positive definite diffusion tensor𝐃​(𝐫)∈L∞​(Ω)3×3\mathbf{D}(\mathbf{r})\in L^{\infty}(\Omega)^{3\times 3}with𝐃​(𝐫)​ξ⋅ξ≥Dmin​∥ξ∥2\mathbf{D}(\mathbf{r})\xi\cdot\xi\geq D_{\min}\lVert\xi\rVert^{2}can be used without substantive changes.)
AssumeT1,2∈L∞​(Ω)T_{1,2}\in L^{\infty}(\Omega)with0<Tmin≤T1,2​(𝐫)≤Tmax<∞0<T_{\min}\leq T_{1,2}(\mathbf{r})\leq T_{\max}<\infty.
Letδ​B→∈L∞​(Ω)3\delta\vec{B}\in L^{\infty}(\Omega)^{3}andM0∈L∞​(Ω)M_{0}\in L^{\infty}(\Omega).
If advection is included, assumev→∈W1,∞​(Ω)3\vec{v}\in W^{1,\infty}(\Omega)^{3}. For the energy-neutral transport setting used in several stability statements below, we additionally assume∇⋅v→=0in​Ω,v→⋅𝐧^=0on​∂Ω.\nabla\cdot\vec{v}=0\quad\text{in }\Omega,\quad\vec{v}\cdot\hat{\mathbf{n}}=0\quad\text{on }\partial\Omega.(31)

Ifv→⋅𝐧^≠0\vec{v}\cdot\hat{\mathbf{n}}\neq 0on∂Ω\partial\Omega, then an inflow boundary condition forM→\vec{M}onΓin={𝐫∈∂Ω:v→⋅𝐧^<0}\Gamma_{\mathrm{in}}=\{\mathbf{r}\in\partial\Omega:\vec{v}\cdot\hat{\mathbf{n}}<0\}is required and additional boundary terms appear in the energy estimates.

We use the regularized secular kernel with a short-distance length scalea>0a>0,Ka​(𝐫)=1−3​cos2⁡θ2​(∥𝐫∥2+a2)3/2,𝒜=diag​(−1,−1,2),K_{a}(\mathbf{r})=\frac{1-3\cos^{2}\theta}{2\bigl(\lVert\mathbf{r}\rVert^{2}+a^{2}\bigr)^{3/2}},\quad\mathcal{A}=\mathrm{diag}(-1,-1,2),(32)

and define the linear map𝒯a:(L2​(Ω))3→(L2​(Ω))3\mathcal{T}_{a}:(L^{2}(\Omega))^{3}\to(L^{2}(\Omega))^{3}by𝒯a​[M→]​(𝐫)=∫ΩKa​(𝐫−𝐫′)​𝒜​M→​(𝐫′)​d3​𝐫′.\mathcal{T}_{a}[\vec{M}](\mathbf{r})=\int_{\Omega}K_{a}(\mathbf{r}-\mathbf{r}^{\prime})\,\mathcal{A}\,\vec{M}(\mathbf{r}^{\prime})\,d^{3}\mathbf{r}^{\prime}.(33)

The distant dipolar field isB→d=𝒯a​[M→]\vec{B}_{d}=\mathcal{T}_{a}[\vec{M}].

The angular mean of the factor(1−3​cos2⁡θ)(1-3\cos^{2}\theta)over a full sphere is zero,∫S2(1−3​cos2⁡θ)​𝑑Ω=0.\int_{S^{2}}\bigl(1-3\cos^{2}\theta\bigr)\,d\Omega=0.(34)

This fact helps interpret the DDF as a long-range, sign-changing interaction. On bounded domains, however, neighborhoods near∂Ω\partial\Omegaare not spherically symmetric, so boundary effects can bias local contributions. In this work we keep the bounded-domain integral (33) and treat boundary effects as part of the physical model. We develop the analysis for fixeda>0a>0; the singular principal-value kernel ata=0a=0requires additional arguments and is not pursued here.

An optional pair-correlation factorg​(∥𝐫−𝐫′∥)∈L∞g(\lVert\mathbf{r}-\mathbf{r}^{\prime}\rVert)\in L^{\infty}withg=0g=0near0andg→1g\to 1at large separation may be included. All statements below hold withKaK_{a}replaced byKa​gK_{a}g.

We impose reflective diffusion boundaries,𝐧^⋅(D​(𝐫)​∇M→)=0on​∂Ω,\hat{\mathbf{n}}\cdot\bigl(D(\mathbf{r})\nabla\vec{M}\bigr)=0\quad\text{on }\partial\Omega,(35)

understood componentwise. For advection we use either the skew-symmetric discretization (21) under (31), or else we retain the standard variational form and explicitly bound the contribution from the symmetric part of the discrete advection operator.

## IVProperties of the DDF operator and an energy identity

The regularized DDF operator remains bounded on the Lebesgue and Sobolev spaces used below, so the coarse-grained field does not generate additional singular growth. A detailed statement and proof are given in the Appendix. SeeProposition˜A.1.

The pointwise orthogonality identity used in the energy estimate is stated and proved inLemma˜A.5in the Appendix.

The local Lipschitz bound for the precession nonlinearity is stated and proved inLemma˜A.6in the Appendix.

The continuum energy calculation shows that precession is energy-neutral, while diffusion and relaxation are dissipative; transport contributes only through compression and boundary-flux terms. A detailed statement and proof are given in the Appendix. SeeProposition˜A.2.

## VWell-posedness of the weak problem

LetV:=(H1​(Ω))3V:=(H^{1}(\Omega))^{3},H:=(L2​(Ω))3H:=(L^{2}(\Omega))^{3}, andV′:=(H−1​(Ω))3V^{\prime}:=(H^{-1}(\Omega))^{3}. We use the Gelfand tripleV↪H≅H′↪V′V\hookrightarrow H\cong H^{\prime}\hookrightarrow V^{\prime}.
DefineX:=L2​(0,T;V)∩H1​(0,T;V′).X:=L^{2}(0,T;V)\cap H^{1}(0,T;V^{\prime}).

A weak solution on[0,T][0,T]is a functionM→∈X\vec{M}\in Xthat satisfies (12) for all test functionsvi∈H1​(Ω)v_{i}\in H^{1}(\Omega)(with the chosen DDF kernel and with any required advection boundary conditions) and the initial conditionM→​(⋅,0)=M→init∈H\vec{M}(\cdot,0)=\vec{M}_{\mathrm{init}}\in H.

The time-continuity result used in the Gelfand-triple argument is stated and proved inLemma˜A.7in the Appendix.

The local existence and uniqueness result is stated and proved inTheorem˜A.8in the Appendix.

Weak solutions depend continuously on the initial data, so perturbations in the starting magnetization remain controlled on the local existence interval. A detailed statement and proof are given in the Appendix. SeeProposition˜A.3.

When transport is absent or is imposed in an energy-neutral form, the a priori bounds extend the local weak solution to any finite time horizon. A detailed statement and proof are given in the Appendix. SeeCorollary˜A.4.

Remarks.(i) A uniformly elliptic diffusion tensor𝐃​(𝐫)\mathbf{D}(\mathbf{r})can replaceD​(𝐫)D(\mathbf{r})with minor notational changes. (ii) The analysis is developed for fixeda>0a>0, for which𝒯a\mathcal{T}_{a}is bounded on the spaces used. A principal-value treatment of the singular kernel ata=0a=0requires additional kernel analysis and is not pursued here.

## VIDiscrete stability of the FE semi-discretization

LetM,K,S1,S2M,K,S_{1},S_{2}be as in (15)–(18) and letbT1b_{T_{1}}be as in (19). For advection, letNvN_{v}denote either the standard operator (20) or the skew-symmetric operatorNvskewN_{v}^{\mathrm{skew}}in (21) when (31) holds. Let𝒫i​(w)\mathcal{P}_{i}(w)be assembled with a quadrature that is exact on the products appearing below, or sufficiently accurate so that any quadrature defect is of higher order in the mesh sizehh. If the DDF is evaluated approximately (e.g., by a compressed far-field), define the discrete skew-symmetry defectδskew​(w):=∑i=13wi⊤​𝒫i​(w).\delta_{\mathrm{skew}}(w):=\sum_{i=1}^{3}w_{i}^{\top}\mathcal{P}_{i}(w).

We assume the approximation tolerance is chosen so that|δskew​(w)||\delta_{\mathrm{skew}}(w)|remains small compared to the time-discretization error over the time window of interest.

The discrete skew-symmetry identity for the precession operator is stated and proved inLemma˜A.9in the Appendix.

The matrix positivity properties used in the discrete energy analysis are stated and proved inLemma˜A.10in the Appendix.

The semi-discrete energy inequality and its proof are given inTheorem˜A.11in the Appendix.

## Remark 1(Non-energy-neutral advection).

If (31) does not hold or a non-skew discretization of advection is used, an extra term12​w⊤​(Nv+Nv⊤)​w\frac{1}{2}\,w^{\top}\bigl(N_{v}+N_{v}^{\top}\bigr)w

appears on the right-hand side of (233). This term can be bounded byC​‖w‖M2C\|w\|_{M}^{2}withCCdepending on‖∇⋅v→‖L∞​(Ω)\|\nabla\cdot\vec{v}\|_{L^{\infty}(\Omega)}and any boundary flux contributions, yielding a Grönwall-type inequality.

## VIITime discretization: stability and consistency

We analyze the second-order IMEX splitting scheme described in §II.4; see (27)–(30). Diffusion and relaxation are treated implicitly by Crank–Nicolson. The explicit stage uses a midpoint evaluation of the effective field. For analysis it is convenient to express this explicit stage in an algebraic midpoint form. The reference implementation realizes the same midpoint-field evaluation by a structure-preserving Rodrigues rotation at DDF quadrature points followed by anL2L^{2}projection (mass solve). The stability bound stated inTheorem˜A.13applies provided the explicit stage satisfies the discrete skew-symmetry property inLemma˜A.9and the local Lipschitz bounds stated in the Appendix proof; any quadrature or projection defects enter as higher-order perturbations and are controlled in the same way.

The nonlinear IMEX stability result and its proof are given inTheorem˜A.13in the Appendix.

The IMEX method remains second order in time for smooth solutions, and the FE spatial error retains the standard conforming approximation rates. A detailed statement and proof are given in the Appendix. SeeProposition˜A.12.

Remarks.(i) Diffusion and relaxation are unconditionally stable in the Crank–Nicolson substeps; the time-step restriction is driven by explicit precession and advection. (ii) IfB→d\vec{B}_{d}is evaluated approximately (near/far splitting with a compressed far field), the energy inequality acquires a defect term proportional to the approximation tolerance; this tolerance should be chosen so that the defect is smaller than the desired time-discretization error. (iii) If (31) does not hold, then additional transport contributions enter both the continuous and discrete energy balances via∇⋅v→\nabla\cdot\vec{v}and boundary fluxes, and the stability estimate requires corresponding bounds.

## VIIIValidation and representative dynamics

We report several validation and demonstration cases for the bounded-domain Bloch–DDF solver.
All bounded-domain runs use the real-space DDF evaluator and the structure-preserving FE precession update (Rodrigues rotation at DDF quadrature points followed by anL2L^{2}projection).
The periodic plane-wave benchmark uses FFT-based periodic convolution on a uniform grid, as described inSection˜VIII.1.2.(a)(b)Figure 2:Periodic plane-wave analytical benchmark for a single Fourier mode.
Numerical evolution of the mode amplitudeA​(t)A(t)compared against the closed-form solution (45) using the kernel symbol valueλ=−1.3889\lambda=-1.3889(regularization lengtha=0.04a=0.04, mode(mx,my,mz)=(1,0,0)(m_{x},m_{y},m_{z})=(1,0,0), and periodic boxΩ=[0,1)3\Omega=[0,1)^{3}discretized on a32×32×3232\times 32\times 32uniform grid).
Panels showRe​A​(t)\mathrm{Re}\,A(t)and|A​(t)||A(t)|.
The plotted case corresponds to the smallest time step inTable˜2.

## VIII.1Comparison against closed-form analytical benchmarks

This section compares the numerical solver against three analytical benchmarks with closed-form time dependence. Each benchmark isolates a specific subset of the Bloch–DDF dynamics.
No parameters are fitted. All constants that appear in the closed-form expressions (e.g., kernel averages or Fourier symbols) are determined directly from the chosen regularized DDF kernel and the stated geometry and discretization. A summary of the three analytical benchmarks and the observed relative errors is given in Table1.

Given a complex time seriesy​(tn)y(t_{n})sampled at the stored times{tn}n=0N\{t_{n}\}_{n=0}^{N}, we report the discrete relativeL2L^{2}errorϵrel=(∑n=0N|ynum​(tn)−yan​(tn)|2)1/2(∑n=0N|yan​(tn)|2)1/2.\epsilon_{\mathrm{rel}}=\frac{\bigl(\sum_{n=0}^{N}|y_{\mathrm{num}}(t_{n})-y_{\mathrm{an}}(t_{n})|^{2}\bigr)^{1/2}}{\bigl(\sum_{n=0}^{N}|y_{\mathrm{an}}(t_{n})|^{2}\bigr)^{1/2}}.(36)

For the longitudinal-mode test,y​(t)=c​(t)y(t)=c(t)is a real scalar coefficient.Table 1:Summary of analytical benchmarks and observed agreement.
The reportedϵrel\epsilon_{\mathrm{rel}}values are computed from the recorded numerical and analytical time series using (36).BenchmarkObservableϵrel\epsilon_{\mathrm{rel}}Uniform-mode DDF reduction (Section˜VIII.1.1)S​(t)=⟨Mx+i​My⟩S(t)=\langle M_{x}+iM_{y}\rangle6.89×10−46.89\times 10^{-4}Periodic plane-wave mode (Section˜VIII.1.2)A​(t)A(t)5.73×10−45.73\times 10^{-4}Longitudinal diffusion+T1T_{1}mode (Section˜VIII.1.3)c​(t)c(t)1.40×10−51.40\times 10^{-5}

## VIII.1.1Uniform transverse mode with regularized DDF

Assume (i) constant coefficients, (ii) no gradients (gz=0g_{z}=0), (iii) no flow, and (iv) an initially uniform magnetization.
In this setting, diffusion does not act on the uniform mode.
We model the DDF contribution to the uniform-mode dynamics by a spatially uniform effective field of the formB→d​(t)=κeff​𝒜​M→​(t),𝒜=diag​(−1,−1,2),\vec{B}_{d}(t)=\kappa_{\mathrm{eff}}\,\mathcal{A}\,\vec{M}(t),\quad\mathcal{A}=\mathrm{diag}(-1,-1,2),(37)

whereκeff=k​κ​(Ω,a)\kappa_{\mathrm{eff}}=k\,\kappa(\Omega,a)is a geometry- and regularization-dependent constant, andkkis the dimensionless DDF coupling parameter used in the numerical model. A convenient definition isκ​(Ω,a)=1|Ω|​∫Ω(∫ΩKa​(𝐫−𝐫′)​d3​𝐫′)​d3​𝐫,\kappa(\Omega,a)=\frac{1}{|\Omega|}\int_{\Omega}\left(\int_{\Omega}K_{a}(\mathbf{r}-\mathbf{r}^{\prime})\,d^{3}\mathbf{r}^{\prime}\right)d^{3}\mathbf{r},(38)

withKaK_{a}from (3). In the implementation used here,κ\kappais evaluated directly using the same DDF quadrature rule specified for the run (no fitting).

Letδ​B→=ω​𝐳^\delta\vec{B}=\omega\,\hat{\mathbf{z}}, whereω\omegais a constant field offset (so the corresponding angular frequency isγ​ω\gamma\,\omega), and define the transverse complex signalS​(t)=Mx​(t)+i​My​(t)S(t)=M_{x}(t)+iM_{y}(t).
Using (37), the transverse dynamics reduce tod​Sd​t=−1T2​S−i​(γ​ω+3​γ​κeff​Mz​(t))​S,\frac{dS}{dt}=-\frac{1}{T_{2}}\,S-i\Bigl(\gamma\,\omega+3\gamma\,\kappa_{\mathrm{eff}}\,M_{z}(t)\Bigr)S,(39)

while the longitudinal component satisfies the standardT1T_{1}recoveryd​Mzd​t=M0−MzT1,Mz​(0)=Mz​0.\frac{dM_{z}}{dt}=\frac{M_{0}-M_{z}}{T_{1}},\quad M_{z}(0)=M_{z0}.(40)

The solution of (40) isMz​(t)=M0+(Mz​0−M0)​e−t/T1.M_{z}(t)=M_{0}+\bigl(M_{z0}-M_{0}\bigr)e^{-t/T_{1}}.(41)

Substituting (41) into (39) yields the closed-form transverse signalS​(t)=S​(0)​e−t/T2​exp⁡(−i​γ​ω​t)×exp⁡(−i​3​γ​κeff​(M0​t+(Mz​0−M0)​T1​(1−e−t/T1))).S(t)=S(0)\,e^{-t/T_{2}}\,\exp\bigl(-i\,\gamma\,\omega t\bigr)\\
\times\exp\Bigl(-i\,3\gamma\,\kappa_{\mathrm{eff}}\bigl(M_{0}t+(M_{z0}-M_{0})T_{1}(1-e^{-t/T_{1}})\bigr)\Bigr).(42)

For the discretization and parameters used inFigure˜1, the DDF constantκ\kappawas computed deterministically from (38) using the same quadrature and kernel discretization as in the numerical DDF evaluation (no fitting). For this case,κ=7.8125\kappa=7.8125andκeff=39.0625\kappa_{\mathrm{eff}}=39.0625(withk=5k=5, regularization lengtha=0.04a=0.04, and a10×10×1010\times 10\times 10hexahedral discretization of the unit box).Figure˜1compares the numericalS​(t)S(t)against (42) with the same(ω,T1,T2,M0,Mz​0)(\omega,T_{1},T_{2},M_{0},M_{z0})and withκeff\kappa_{\mathrm{eff}}determined by (38). The observed relative error isϵrel=6.89×10−4\epsilon_{\mathrm{rel}}=6.89\times 10^{-4}over the reported time samples.(a)(a)Re​S​(t)\mathrm{Re}\,S(t)(b)(b)Im​S​(t)\mathrm{Im}\,S(t)(c)(c)|S​(t)||S(t)|Figure 3:Long-time lab-frame evolution of the global transverse signalS​(t)=⟨Mx+i​My⟩S(t)=\langle M_{x}+iM_{y}\ranglewith DDF enabled.
Panels show (a)Re​S​(t)\mathrm{Re}\,S(t),
(b)Im​S​(t)\mathrm{Im}\,S(t), and
(c) the envelope|S​(t)||S(t)|for the same run.

## VIII.1.2Periodic plane-wave eigenmode

This benchmark targets the DDF symbol and the phase evolution of a single Fourier mode in a periodic setting.
Consider a periodic boxΩ=[0,Lx)×[0,Ly)×[0,Lz)\Omega=[0,L_{x})\times[0,L_{y})\times[0,L_{z}), and let the transverse magnetization be a single modeMx+i​My=A​(t)​ei​𝐪⋅𝐫M_{x}+iM_{y}=A(t)e^{i\mathbf{q}\cdot\mathbf{r}}with𝐪=(2​π​mx/Lx,2​π​my/Ly,2​π​mz/Lz)\mathbf{q}=(2\pi m_{x}/L_{x},2\pi m_{y}/L_{y},2\pi m_{z}/L_{z}).
For periodic convolution, the DDF operator is diagonal in Fourier space, so𝒯a​[ei​𝐪⋅𝐫]=λ​(𝐪)​ei​𝐪⋅𝐫,\mathcal{T}_{a}\!\left[e^{i\mathbf{q}\cdot\mathbf{r}}\right]=\lambda(\mathbf{q})\,e^{i\mathbf{q}\cdot\mathbf{r}},(43)

whereλ​(𝐪)\lambda(\mathbf{q})is the Fourier symbol of the chosen regularized kernel (including the discretization weights in the discrete setting). This periodic benchmark uses FFT-based convolution on a uniform grid; it is not intended as a bounded-domain reference, since FFT-based DDF evaluation on nonperiodic domains requires padding or extensions that introduce boundary artifacts.
WithMzM_{z}held constant in the linear test, the complex amplitude satisfiesd​Ad​t=−(D​|𝐪|2+1T2)​A−i​γ​(ω+k​λ​(𝐪))​A,\frac{dA}{dt}=-\Bigl(D|\mathbf{q}|^{2}+\frac{1}{T_{2}}\Bigr)A-i\,\gamma\Bigl(\omega+k\,\lambda(\mathbf{q})\Bigr)A,(44)

and henceA​(t)=A​(0)​exp⁡(−(D​|𝐪|2+T2−1)​t)​exp⁡(−i​γ​(ω+k​λ​(𝐪))​t).A(t)=A(0)\exp\Bigl(-\bigl(D|\mathbf{q}|^{2}+T_{2}^{-1}\bigr)t\Bigr)\exp\Bigl(-i\,\gamma(\omega+k\lambda(\mathbf{q}))t\Bigr).(45)

For the case(mx,my,mz)=(1,0,0)(m_{x},m_{y},m_{z})=(1,0,0)withLx=Ly=Lz=1L_{x}=L_{y}=L_{z}=1anda=0.04a=0.04(a fixed coarse-graining/softening length used throughout unless otherwise stated), the computed symbol value wasλ=−1.3889\lambda=-1.3889.
Withω=300\omega=300,k=5k=5, andγ=1\gamma=1, this givesωeff=ω+k​λ=293.0553\omega_{\mathrm{eff}}=\omega+k\lambda=293.0553.
WithD=0D=0andT2=0.2T_{2}=0.2, the decay rate isT2−1=5T_{2}^{-1}=5.Figure˜2shows the numerical amplitude (computed by FFT-based periodic convolution and Rodrigues precession) against (45). Observed time-step dependence for this periodic plane-wave benchmark is summarized in Table2.Table 2:Plane-wave benchmark: observed time-step dependence forϵrel\epsilon_{\mathrm{rel}}inA​(t)A(t). This benchmark implementation uses a first-order operator splitting (exact decay followed by a precession update), and the measured error decreases linearly withΔ​t\Delta t. This benchmark is used to validate the kernel symbol and the associated phase and decay rates in a controlled periodic setting, rather than to demonstrate the temporal order of the full Bloch–DDF time integrator.Δ​t\Delta tϵrel\epsilon_{\mathrm{rel}}Observed order2.0×10−42.0\times 10^{-4}2.292×10−32.292\times 10^{-3}—1.0×10−41.0\times 10^{-4}1.146×10−31.146\times 10^{-3}≈1.00\approx 1.005.0×10−55.0\times 10^{-5}5.728×10−45.728\times 10^{-4}≈1.00\approx 1.00

## VIII.1.3Longitudinal diffusion plusT1T_{1}relaxation eigenmode

This benchmark targets the diffusion operator andT1T_{1}recovery under reflective (Neumann) boundaries in a rectangular box.
LetΩ=(0,Lx)×(0,Ly)×(0,Lz)\Omega=(0,L_{x})\times(0,L_{y})\times(0,L_{z})and consider a Neumann Laplacian eigenfunctionϕ​(𝐫)=cos⁡(mx​π​xLx)​cos⁡(my​π​yLy)​cos⁡(mz​π​zLz),\phi(\mathbf{r})=\cos\Bigl(\frac{m_{x}\pi x}{L_{x}}\Bigr)\cos\Bigl(\frac{m_{y}\pi y}{L_{y}}\Bigr)\cos\Bigl(\frac{m_{z}\pi z}{L_{z}}\Bigr),(46)

which satisfies−Δ​ϕ=λ​ϕ-\Delta\phi=\lambda\phiwithλ=π2​(mx2Lx2+my2Ly2+mz2Lz2).\lambda=\pi^{2}\Bigl(\frac{m_{x}^{2}}{L_{x}^{2}}+\frac{m_{y}^{2}}{L_{y}^{2}}+\frac{m_{z}^{2}}{L_{z}^{2}}\Bigr).(47)

Assume a purely longitudinal perturbation of the formMz​(𝐫,t)=M0+c​(t)​ϕ​(𝐫),Mx=My=0,M_{z}(\mathbf{r},t)=M_{0}+c(t)\phi(\mathbf{r}),\quad M_{x}=M_{y}=0,(48)

with constantDDandT1T_{1}and reflective diffusion boundaries.
Substituting (48) into thezzcomponent of (5) (with no precession terms active) yieldsd​cd​t=−(D​λ+1T1)​c,\frac{dc}{dt}=-\Bigl(D\lambda+\frac{1}{T_{1}}\Bigr)c,(49)

soc​(t)=c​(0)​exp⁡(−(D​λ+T1−1)​t).c(t)=c(0)\exp\Bigl(-\bigl(D\lambda+T_{1}^{-1}\bigr)t\Bigr).(50)

For the unit box with(mx,my,mz)=(1,1,1)(m_{x},m_{y},m_{z})=(1,1,1),λ=3​π2=29.6088\lambda=3\pi^{2}=29.6088.
WithD=10−3D=10^{-3}andT1=5T_{1}=5, the predicted decay rate isD​λ+T1−1=0.2296D\lambda+T_{1}^{-1}=0.2296.
The measured agreement isϵrel=1.40×10−5\epsilon_{\mathrm{rel}}=1.40\times 10^{-5}for the coefficient time series.Figure˜4shows the numerical and analyticalc​(t)c(t).Figure 4:Longitudinal diffusion+T1T_{1}analytical benchmark.
Time evolution of the modal coefficientc​(t)c(t)for the Neumann eigenmode (46) compared against (50).
For(1,1,1)(1,1,1)in the unit box,λ=3​π2\lambda=3\pi^{2}and the predicted decay rate isD​λ+T1−1=0.2296D\lambda+T_{1}^{-1}=0.2296.

## VIII.2Long-time lab-frame oscillations with DDF

Figure˜3shows the long-time lab-frame evolution of the global transverse signalS​(t)=⟨Mx+i​My⟩S(t)=\langle M_{x}+iM_{y}\ranglewith DDF enabled, where⟨⋅⟩\langle\cdot\rangledenotes the spatial average overΩ\Omegaof the corresponding FE field. The real and imaginary parts show multiple zero crossings over the plotted interval. The envelope|S​(t)||S(t)|decays smoothly. This run is generated using the structure-preserving explicit precession update in the implementation (Rodrigues rotation at DDF quadrature points followed by anL2L^{2}projection). The plotted observable is time-step converged in the following quantitative sense: ifSΔ​t​(tn)S_{\Delta t}(t_{n})denotes the stored time series at step sizeΔ​t\Delta tandSΔ​t/2​(tn)S_{\Delta t/2}(t_{n})denotes the stored time series at step sizeΔ​t/2\Delta t/2downsampled to the coarser grid, thenϵdt:=‖SΔ​t−SΔ​t/2‖2‖SΔ​t/2‖2\epsilon_{\mathrm{dt}}:=\frac{\|S_{\Delta t}-S_{\Delta t/2}\|_{2}}{\|S_{\Delta t/2}\|_{2}}

is small for the parameter choices shown, indicating that the displayed trace is insensitive to halvingΔ​t\Delta tat fixed spatial discretization.

## VIII.3DDF-on versus DDF-off envelope

Figure˜5isolates the effect of the DDF on the global envelope|S​(t)||S(t)|by comparing DDF off to DDF on at two DDF scalings.
Thek=0k=0curve provides a control in which only diffusion, relaxation, and the uniform offset contribute.
Increasing the DDF scaling changes the envelope measurably over the same time window (Fig.5).Figure 5:Envelope comparison with DDF off (k=0k=0) versus DDF on (k=5k=5) at otherwise fixed parameters.Figure 6:Envelope comparison with DDF off (k=0k=0) versus stronger DDF (k=20k=20) at otherwise fixed parameters.

## VIII.4Gradient dephasing with and without DDF

Figure˜7shows the envelope response under a constantzz-gradient, comparing DDF off to DDF on.
The gradient drives rapid dephasing (and partial rephasing in the bounded domain), while the DDF modifies the envelope through nonlinear nonlocal feedback.
This example is included to illustrate a regime where spatial phase structure is present, which can amplify the macroscopic impact of long-range dipolar interactions.Figure 7:Envelope|S​(t)||S(t)|under a constantzz-gradient, comparing DDF off (k=0k=0) to DDF on (k=5k=5) at otherwise fixed parameters.

## IXGeometry-driven advantages of finite elements on curved domains

This section continues the validation studies by focusing on curved Neumann boundaries, where body-fitted FE discretizations are expected to outperform voxelized FD baselines at comparable resolution. A central motivation for a FE formulation is robust treatment of curved and complex boundaries with reflective diffusion conditions. Finite-difference (FD) baselines on Cartesian grids can be accurate on simple boxes, but on curved domains they typically require either embedded-boundary technology (cut cells, ghost-fluid methods, or level-set reconstructions) or accept staircased boundaries whose discrete Neumann condition is only approximate. In this section we quantify this geometry effect by comparing FE and FD against an analytical reference on a sphere, using a benchmark that is sensitive to boundary accuracy.

## IX.1Analytical reference: Neumann diffusion plusT1T_{1}relaxation on a sphere

LetΩ={𝐫∈ℝ3:‖𝐫‖<R}\Omega=\{\mathbf{r}\in\mathbb{R}^{3}:\|\mathbf{r}\|<R\}be a ball of radiusRRwith reflective (Neumann) boundary condition∂nu=0\partial_{n}u=0on∂Ω\partial\Omega. Consider the longitudinal perturbationu​(𝐫,t):=Mz​(𝐫,t)−M0,u(\mathbf{r},t):=M_{z}(\mathbf{r},t)-M_{0},(51)

withMx=My=0M_{x}=M_{y}=0so that precession is inactive. For constantDDandT1T_{1}, the governing equation reduces to the linear problem∂tu=D​Δ​u−1T1​u,∂nu=0​on​∂Ω.\partial_{t}u=D\Delta u-\frac{1}{T_{1}}u,\quad\partial_{n}u=0\ \text{on }\partial\Omega.(52)

Separation of variables in spherical coordinates yields eigenfunctions of the formuℓ​m​n​(𝐫,t)=cℓ​m​n​(t)​jℓ​(αℓ​n​rR)​Yℓ​m​(θ,ϕ),u_{\ell mn}(\mathbf{r},t)=c_{\ell mn}(t)\,j_{\ell}\!\left(\alpha_{\ell n}\frac{r}{R}\right)Y_{\ell m}(\theta,\phi),(53)

wherejℓj_{\ell}is a spherical Bessel function andYℓ​mY_{\ell m}is a spherical harmonic. The Neumann boundary condition impliesjℓ′​(αℓ​n)=0j_{\ell}^{\prime}(\alpha_{\ell n})=0. In this work we use the radially symmetric familyℓ=0\ell=0, for whichj0​(x)=sin⁡xx,j0′​(x)=x​cos⁡x−sin⁡xx2.j_{0}(x)=\frac{\sin x}{x},\quad j_{0}^{\prime}(x)=\frac{x\cos x-\sin x}{x^{2}}.(54)

Thus the Neumann conditionj0′​(α0​n)=0j_{0}^{\prime}(\alpha_{0n})=0is equivalent totan⁡α=α,\tan\alpha=\alpha,(55)

with roots0<α1<α2<⋯0<\alpha_{1}<\alpha_{2}<\cdots. The corresponding eigenvalue isλn=(αn/R)2\lambda_{n}=(\alpha_{n}/R)^{2}, and the coefficient satisfiesd​cnd​t=−(D​λn+1T1)​cn,cn​(t)=cn​(0)​exp⁡[−(D​(αnR)2+1T1)​t].\frac{dc_{n}}{dt}=-\left(D\lambda_{n}+\frac{1}{T_{1}}\right)c_{n},\\
c_{n}(t)=c_{n}(0)\exp\left[-\left(D\left(\frac{\alpha_{n}}{R}\right)^{2}+\frac{1}{T_{1}}\right)t\right].(56)

We emphasize that (56) is a closed-form, parameter-free reference once(D,T1,R)(D,T_{1},R)and the root indexnnare specified. It is therefore well suited as a gold-standard check for boundary handling in numerical discretizations on curved domains.

## IX.2Numerical experiment: mapped-geometry FE versus voxelized FD

We compare two discretizations of (52). In the FE approach (mapped sphere), the sphere is represented by a geometry-mapped hexahedral mesh (isoparametric map from the reference cube to the sphere), and diffusion is assembled in the FE weak form with reflective boundary conditions imposed naturally through the variational formulation. The modal coefficientcn​(t)c_{n}(t)is extracted by anL2L^{2}projection onto the analytical eigenfunction evaluated on the numerical quadrature points. In the FD baseline (voxel mask), the sphere is represented as a voxel mask on a Cartesian grid, and diffusion is advanced by an explicit 7-point Laplacian restricted to the mask. At the mask boundary we use a simple no-flux treatment based on omitting fluxes to neighbors outside the mask. This voxel-mask FD is included as a straightforward Cartesian baseline; it is not an embedded-boundary or cut-cell method, and it inherits staircase boundary geometry at fixed grid resolution. The same analytical mode is used to extract the coefficient.

To stress the geometric boundary, we use the second nontrivial radial Neumann root (n=2n=2in (55)), which yields a more oscillatory mode and larger boundary gradients than the fundamental mode. Forn=2n=2, the root isα2≈7.7253\alpha_{2}\approx 7.7253and the analytic decay rate in (56) isρ=D​(α2R)2+1T1.\rho=D\left(\frac{\alpha_{2}}{R}\right)^{2}+\frac{1}{T_{1}}.(57)

## IX.3Results: FE achieves smaller error at fixed resolution

Figures˜8and9show the coefficient error|cnum​(t)−can​(t)||c_{\mathrm{num}}(t)-c_{\mathrm{an}}(t)|for the mapped-geometry FE discretization and the voxel-mask FD baseline on two challenging sphere configurations. In both cases, FE yields a smaller error over most of the time window. The aggregate relativeL2L^{2}errors confirm the visual trend: forR=0.30R=0.30andn​x=12nx=12, FE attains2.66×10−32.66\times 10^{-3}while the voxel-mask FD baseline attains8.26×10−38.26\times 10^{-3}(FD/FE≈3.1\approx 3.1). ForR=0.25R=0.25andn​x=10nx=10, FE attains5.48×10−35.48\times 10^{-3}while the voxel-mask FD baseline attains2.59×10−22.59\times 10^{-2}(FD/FE≈4.7\approx 4.7). These results indicate a geometry-driven benefit of the mapped-geometry FE formulation for boundary-sensitive Neumann diffusion modes when compared against the analytical reference (56).Table 3:Curved-boundary Neumann diffusion benchmark on a sphere using the second radial Neumann root (n=2n=2,α2≈7.7253\alpha_{2}\approx 7.7253). Errors are relativeL2L^{2}errors of the extracted modal coefficientc​(t)c(t)against the analytical decay (56). The FD method is a voxel-mask baseline with a simple no-flux treatment at the mask boundary.Caserel.L2L^{2}(FE)rel.L2L^{2}(FD)FD/FER=0.30R=0.30,n​x=12nx=122.66×10−32.66\times 10^{-3}8.26×10−38.26\times 10^{-3}3.13.1R=0.25R=0.25,n​x=10nx=105.48×10−35.48\times 10^{-3}2.59×10−22.59\times 10^{-2}4.74.7Figure 8:Sphere diffusion benchmark (R=0.30R=0.30,n​x=12nx=12, root-indexn=2n=2). Plotted is the absolute error in the extracted coefficientc​(t)c(t)relative to the analytical decay (56) for FE (mapped geometry) and the voxel-mask FD baseline.Figure 9:Sphere diffusion benchmark (R=0.25R=0.25,n​x=10nx=10, root-indexn=2n=2). Same diagnostic asFigure˜8, showing a larger separation between FE and FD as the curved boundary becomes more poorly resolved on the Cartesian grid.

On a voxelized curved boundary, the discrete no-flux condition is enforced only approximately and the effective boundary location is grid-dependent. For smooth modes this may be adequate, but for more oscillatory modes the staircased boundary geometry and boundary-condition approximation can introduce a systematic bias in the decay rate and mode shape. In contrast, the FE formulation imposes the reflective diffusion condition through the weak form on a geometry-mapped boundary, which yields smaller coefficient error for this benchmark at comparable grid resolution. These sphere results quantify the effect against the analytical reference (56) and motivate the use of FE discretizations when curved Neumann boundaries are important (Table3).

## XConclusion

We presented a FE weak formulation of the Bloch equations with the distant dipolar field and derived the semi-discrete system (22) for bounded domains with spatially varying material parameters and optional flow. Representative long-time lab-frame oscillations and envelope-level DDF effects are shown inSection˜VIII(seeFigures˜3,5and7). The formulation relies on a regularized DDF kernel with a short-distance length scalea>0a>0. The regularization yields a bounded DDF operator (Proposition˜A.1) and enables standard variational analysis on bounded domains.

We established anL2L^{2}energy balance and associated a priori estimate in which precession is neutral and diffusion and transverse relaxation are dissipative (Proposition˜A.2). We proved local well-posedness with continuous dependence on the data (Theorem˜A.8,Proposition˜A.3) and obtained global existence under additional conditions that ensure transport does not inject energy through volume compression or boundary fluxes (Corollary˜A.4). At the discrete level we showed an energy identity for the FE semi-discretization under an energy-neutral advection discretization (Theorem˜A.11) and a corresponding stability result for a second-order IMEX scheme under a time-step restriction controlled by effective precession and transport bounds (Theorem˜A.13).

A major emphasis of this work is validation and practical robustness on bounded domains. We validated the implementation against closed-form analytical benchmarks that isolate key components of the model: a uniform-mode DDF reduction with a deterministically computed kernel average, a periodic plane-wave eigenmode based on the kernel symbol, and a longitudinal Neumann diffusion+T1T_{1}mode. We also quantified a geometry-driven effect of curved Neumann boundaries by comparing mapped-geometry FE against a voxel-mask finite-difference baseline on a spherical Neumann eigenmode decay for a boundary-sensitive mode, where FE yields smaller error at comparable grid resolution (seeSection˜IX).

On the algorithmic side, geometry-dependent operators (mass, diffusion, relaxation, and auxiliary structures for near/far evaluation) are assembled once. For bounded-domain runs, the nonlocal DDF is applied at each step in a matrix-free manner using a real-space near/far evaluation, so no periodicity assumptions are required. The time integrator treats diffusion and relaxation implicitly and treats precession and advection explicitly. In the implementation, a structure-preserving explicit precession stage (Rodrigues rotation at DDF quadrature points followed by anL2L^{2}projection) enables stable multi-cycle lab-frame simulations.

There are limitations. Results depend on the chosen regularization lengthaaand on the accuracy of the quadrature and far-field approximation used in the DDF evaluation. Energy-neutral transport requires∇⋅v→=0\nabla\cdot\vec{v}=0andv→⋅𝐧^=0\vec{v}\cdot\hat{\mathbf{n}}=0on∂Ω\partial\Omega(or else an appropriate inflow treatment and additional bounds). Fully rigorous error estimates for compressed far-field operators (e.g., FMM orℋ\mathcal{H}-matrices) are not included. These topics are natural targets for future work, together with adaptiveh/ph/prefinement, anisotropic diffusion tensors, a principal-value analysis of the singular kernel limita→0a\to 0, and validation against alternative nonlocal solvers on canonical geometries.

Overall, the combination of a bounded-operator setting, discrete energy structure, and validated matrix-free implementation supports Bloch–DDF simulation on bounded domains where geometry and boundaries influence the dynamics.

## Appendix ACollected theorem-like statements and proofs

In this Appendix we have collected lemma, proposition, corollary, and theorem statements as well as their proofs in order to streamline the presentation in the main body.

## A.1Continuum operator and weak-solution results

This subsection collects the continuum lemmas, propositions, corollary, and theorem used in the operator, energy, and weak-solution analysis.

## Proposition A.1(Boundedness of𝒯a\mathcal{T}_{a}).

AssumeSection˜IIIand fixa>0a>0. There exists a constantCa=C​(a,Ω)>0C_{a}=C(a,\Omega)>0such that for all1≤p≤∞1\leq p\leq\inftyand allM→∈(Lp​(Ω))3\vec{M}\in(L^{p}(\Omega))^{3},‖𝒯a​[M→]‖Lp​(Ω)≤Ca​‖M→‖Lp​(Ω).\|\mathcal{T}_{a}[\vec{M}]\|_{L^{p}(\Omega)}\leq C_{a}\|\vec{M}\|_{L^{p}(\Omega)}.(58)

Moreover, for anys∈[0,1]s\in[0,1], there existsCa,s=C​(a,Ω,s)>0C_{a,s}=C(a,\Omega,s)>0such that for allM→∈Hs​(Ω)3\vec{M}\in H^{s}(\Omega)^{3},‖𝒯a​[M→]‖Hs​(Ω)≤Ca,s​‖M→‖Hs​(Ω).\|\mathcal{T}_{a}[\vec{M}]\|_{H^{s}(\Omega)}\leq C_{a,s}\,\|\vec{M}\|_{H^{s}(\Omega)}.(59)

## Proof.

Fixa>0a>0. For𝐱≠𝟎\mathbf{x}\neq\mathbf{0}, defineKa​(𝐱):=1−3​(𝐳^⋅𝐱^)22​(‖𝐱‖2+a2)3/2,𝐱^:=𝐱/‖𝐱‖,K_{a}(\mathbf{x}):=\frac{1-3(\hat{\mathbf{z}}\cdot\hat{\mathbf{x}})^{2}}{2(\|\mathbf{x}\|^{2}+a^{2})^{3/2}},\quad\hat{\mathbf{x}}:=\mathbf{x}/\|\mathbf{x}\|,(60)

and setKa​(𝟎):=0K_{a}(\mathbf{0}):=0. The value at𝐱=𝟎\mathbf{x}=\mathbf{0}is immaterial for the integral operator.

SinceΩ⊂ℝ3\Omega\subset\mathbb{R}^{3}is bounded, there existsR>0R>0such thatΩ−Ω:={𝐫−𝐫′:𝐫,𝐫′∈Ω}⊂BR​(0).\Omega-\Omega:=\{\mathbf{r}-\mathbf{r}^{\prime}:\mathbf{r},\mathbf{r}^{\prime}\in\Omega\}\subset B_{R}(0).(61)

Chooseχ∈Cc∞​(ℝ3)\chi\in C_{c}^{\infty}(\mathbb{R}^{3})such thatχ≡1\chi\equiv 1onBR​(0)B_{R}(0), and defineGa​(𝐱):=χ​(𝐱)​Ka​(𝐱).G_{a}(\mathbf{x}):=\chi(\mathbf{x})\,K_{a}(\mathbf{x}).(62)

ThenGaG_{a}is compactly supported, and for every𝐫,𝐫′∈Ω\mathbf{r},\mathbf{r}^{\prime}\in\Omegaone hasGa​(𝐫−𝐫′)=Ka​(𝐫−𝐫′).G_{a}(\mathbf{r}-\mathbf{r}^{\prime})=K_{a}(\mathbf{r}-\mathbf{r}^{\prime}).(63)

We first show thatGa∈W1,1​(ℝ3).G_{a}\in W^{1,1}(\mathbb{R}^{3}).(64)

Indeed, for𝐱≠𝟎\mathbf{x}\neq\mathbf{0},|Ka​(𝐱)|≤1(‖𝐱‖2+a2)3/2≤a−3,|K_{a}(\mathbf{x})|\leq\frac{1}{(\|\mathbf{x}\|^{2}+a^{2})^{3/2}}\leq a^{-3},(65)

because|1−3​(𝐳^⋅𝐱^)2|≤2|1-3(\hat{\mathbf{z}}\cdot\hat{\mathbf{x}})^{2}|\leq 2. HenceKa∈L∞​(BR​(0))K_{a}\in L^{\infty}(B_{R}(0)), soGa∈L1​(ℝ3)G_{a}\in L^{1}(\mathbb{R}^{3}).

For the gradient, writeKa​(𝐱)=\displaystyle K_{a}(\mathbf{x})=q​(𝐱^)​ρa​(‖𝐱‖),\displaystyle q(\hat{\mathbf{x}})\,\rho_{a}(\|\mathbf{x}\|),q​(ω):=\displaystyle q(\omega):=1−3​(𝐳^⋅ω)22,\displaystyle\frac{1-3(\hat{\mathbf{z}}\cdot\omega)^{2}}{2},ρa​(r):=\displaystyle\rho_{a}(r):=(r2+a2)−3/2.\displaystyle(r^{2}+a^{2})^{-3/2}.

The functionqqis smooth on the unit sphere, and therefore its homogeneous extension satisfies|∇q​(𝐱^)|≤C​‖𝐱‖−1(𝐱≠𝟎).|\nabla q(\hat{\mathbf{x}})|\leq C\,\|\mathbf{x}\|^{-1}\quad(\mathbf{x}\neq\mathbf{0}).(66)

Also,|ρa​(r)|≤a−3,|ρa′​(r)|=3​r(r2+a2)5/2≤Ca.|\rho_{a}(r)|\leq a^{-3},\quad|\rho_{a}^{\prime}(r)|=\frac{3r}{(r^{2}+a^{2})^{5/2}}\leq C_{a}.(67)

By the product rule,|∇Ka​(𝐱)|≤Ca​(1+‖𝐱‖−1)(𝐱≠𝟎).|\nabla K_{a}(\mathbf{x})|\leq C_{a}\bigl(1+\|\mathbf{x}\|^{-1}\bigr)\quad(\mathbf{x}\neq\mathbf{0}).(68)

Since‖𝐱‖−1∈L1​(BR​(0))\|\mathbf{x}\|^{-1}\in L^{1}(B_{R}(0))in three dimensions, it follows that∇Ka∈L1​(BR​(0))\nabla K_{a}\in L^{1}(B_{R}(0)). Becauseχ\chiis smooth and compactly supported,∇Ga=χ​∇Ka+Ka​∇χ∈L1​(ℝ3),\nabla G_{a}=\chi\,\nabla K_{a}+K_{a}\,\nabla\chi\in L^{1}(\mathbb{R}^{3}),(69)

which proves (64).

Now letM→∈(Lp​(Ω))3\vec{M}\in(L^{p}(\Omega))^{3},1≤p≤∞1\leq p\leq\infty, and letM→~\widetilde{\vec{M}}denote its zero extension toℝ3\mathbb{R}^{3}. SetF→~:=𝒜​M→~.\widetilde{\vec{F}}:=\mathcal{A}\,\widetilde{\vec{M}}.(70)

For𝐫∈Ω\mathbf{r}\in\Omega, using (63),𝒯a​[M→]​(𝐫)\displaystyle\mathcal{T}_{a}[\vec{M}](\mathbf{r})=∫ΩKa​(𝐫−𝐫′)​𝒜​M→​(𝐫′)​d3​𝐫′\displaystyle=\int_{\Omega}K_{a}(\mathbf{r}-\mathbf{r}^{\prime})\,\mathcal{A}\,\vec{M}(\mathbf{r}^{\prime})\,\mathrm{d}^{3}\mathbf{r}^{\prime}=∫ℝ3Ga​(𝐫−𝐲)​F→~​(𝐲)​d3​𝐲=(Ga∗F→~)​(𝐫).\displaystyle=\int_{\mathbb{R}^{3}}G_{a}(\mathbf{r}-\mathbf{y})\,\widetilde{\vec{F}}(\mathbf{y})\,\mathrm{d}^{3}\mathbf{y}=(G_{a}\ast\widetilde{\vec{F}})(\mathbf{r}).(71)

Therefore, by Young’s inequality onℝ3\mathbb{R}^{3},‖𝒯a​[M→]‖Lp​(Ω)\displaystyle\|\mathcal{T}_{a}[\vec{M}]\|_{L^{p}(\Omega)}≤‖Ga∗F→~‖Lp​(ℝ3)\displaystyle\leq\|G_{a}\ast\widetilde{\vec{F}}\|_{L^{p}(\mathbb{R}^{3})}≤‖Ga‖L1​(ℝ3)​‖F→~‖Lp​(ℝ3)\displaystyle\leq\|G_{a}\|_{L^{1}(\mathbb{R}^{3})}\,\|\widetilde{\vec{F}}\|_{L^{p}(\mathbb{R}^{3})}≤‖Ga‖L1​(ℝ3)​‖𝒜‖​‖M→~‖Lp​(ℝ3)\displaystyle\leq\|G_{a}\|_{L^{1}(\mathbb{R}^{3})}\,\|\mathcal{A}\|\,\|\widetilde{\vec{M}}\|_{L^{p}(\mathbb{R}^{3})}=Ca​‖M→‖Lp​(Ω).\displaystyle=C_{a}\,\|\vec{M}\|_{L^{p}(\Omega)}.(72)

This proves theLpL^{p}bound.

We next prove theH1H^{1}estimate, in the stronger form‖𝒯a​[M→]‖H1​(Ω)≤Ca​‖M→‖L2​(Ω)​for all​M→∈(L2​(Ω))3.\|\mathcal{T}_{a}[\vec{M}]\|_{H^{1}(\Omega)}\leq C_{a}\,\|\vec{M}\|_{L^{2}(\Omega)}\,\text{for all }\vec{M}\in(L^{2}(\Omega))^{3}.(73)

By (71) and the fact thatGa∈W1,1​(ℝ3)G_{a}\in W^{1,1}(\mathbb{R}^{3}), differentiation in the sense of distributions gives∇𝒯a​[M→]=((∇Ga)∗F→~)|Ω.\nabla\mathcal{T}_{a}[\vec{M}]=\bigl((\nabla G_{a})\ast\widetilde{\vec{F}}\bigr)\big|_{\Omega}.(74)

Hence, using Young’s inequality again,‖∇𝒯a​[M→]‖L2​(Ω)\displaystyle\|\nabla\mathcal{T}_{a}[\vec{M}]\|_{L^{2}(\Omega)}≤‖(∇Ga)∗F→~‖L2​(ℝ3)\displaystyle\leq\|(\nabla G_{a})\ast\widetilde{\vec{F}}\|_{L^{2}(\mathbb{R}^{3})}≤‖∇Ga‖L1​(ℝ3)​‖F→~‖L2​(ℝ3)\displaystyle\leq\|\nabla G_{a}\|_{L^{1}(\mathbb{R}^{3})}\,\|\widetilde{\vec{F}}\|_{L^{2}(\mathbb{R}^{3})}≤‖∇Ga‖L1​(ℝ3)​‖𝒜‖​‖M→‖L2​(Ω).\displaystyle\leq\|\nabla G_{a}\|_{L^{1}(\mathbb{R}^{3})}\,\|\mathcal{A}\|\,\|\vec{M}\|_{L^{2}(\Omega)}.(75)

Combining this with the already provedL2L^{2}bound yields (73).

Now fixs∈[0,1]s\in[0,1]. Since𝒯a\mathcal{T}_{a}is bounded𝒯a:(L2​(Ω))3→(L2​(Ω))3​and​𝒯a:(L2​(Ω))3→H1​(Ω)3,\mathcal{T}_{a}:(L^{2}(\Omega))^{3}\to(L^{2}(\Omega))^{3}\,\text{and}\,\mathcal{T}_{a}:(L^{2}(\Omega))^{3}\to H^{1}(\Omega)^{3},(76)

standard interpolation on bounded Lipschitz domains gives𝒯a:(L2​(Ω))3→Hs​(Ω)3\mathcal{T}_{a}:(L^{2}(\Omega))^{3}\to H^{s}(\Omega)^{3}(77)

and‖𝒯a​[M→]‖Hs​(Ω)≤Ca,s​‖M→‖L2​(Ω)for all​M→∈(L2​(Ω))3.\|\mathcal{T}_{a}[\vec{M}]\|_{H^{s}(\Omega)}\leq C_{a,s}\,\|\vec{M}\|_{L^{2}(\Omega)}\quad\text{for all }\vec{M}\in(L^{2}(\Omega))^{3}.(78)

Finally, ifM→∈Hs​(Ω)3\vec{M}\in H^{s}(\Omega)^{3}, thenHs​(Ω)↪L2​(Ω)H^{s}(\Omega)\hookrightarrow L^{2}(\Omega)continuously becauseΩ\Omegais bounded. Therefore (78) implies‖𝒯a​[M→]‖Hs​(Ω)≤Ca,s​‖M→‖L2​(Ω)≤Ca,s​‖M→‖Hs​(Ω).\|\mathcal{T}_{a}[\vec{M}]\|_{H^{s}(\Omega)}\leq C_{a,s}\,\|\vec{M}\|_{L^{2}(\Omega)}\leq C_{a,s}\,\|\vec{M}\|_{H^{s}(\Omega)}.(79)

This proves the statedHsH^{s}bound.
∎

## Proposition A.2(Energy balance andL2L^{2}estimate).

LetM→\vec{M}be a smooth solution of (5) onΩ×(0,T)\Omega\times(0,T)satisfying reflective diffusion boundary conditions𝐧^⋅(D​(𝐫)​∇Mi)=0on​∂Ω×(0,T),i∈{x,y,z}.\hat{\mathbf{n}}\cdot\bigl(D(\mathbf{r})\nabla M_{i}\bigr)=0\quad\text{on }\partial\Omega\times(0,T),\quad i\in\{x,y,z\}.(80)

Thendd​t​12​∫Ω∥M→∥2​d3​𝐫+∫ΩD​(𝐫)​∥∇M→∥2​d3​𝐫+∫ΩMx2+My2T2​(𝐫)​d3​𝐫+∫ΩMz2T1​(𝐫)​d3​𝐫=∫ΩM0​(𝐫)​MzT1​(𝐫)​d3​𝐫+12​∫Ω(∇⋅v→)​∥M→∥2​d3​𝐫−12​∫∂Ω(v→⋅𝐧^)​∥M→∥2​dS.\frac{\mathrm{d}}{\mathrm{d}t}\,\frac{1}{2}\int_{\Omega}\lVert\vec{M}\rVert^{2}\,\mathrm{d}^{3}\mathbf{r}+\int_{\Omega}D(\mathbf{r})\,\lVert\nabla\vec{M}\rVert^{2}\,\mathrm{d}^{3}\mathbf{r}\\
+\int_{\Omega}\frac{M_{x}^{2}+M_{y}^{2}}{T_{2}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}+\int_{\Omega}\frac{M_{z}^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}\\
=\int_{\Omega}\frac{M_{0}(\mathbf{r})\,M_{z}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}+\frac{1}{2}\int_{\Omega}\bigl(\nabla\cdot\vec{v}\bigr)\,\lVert\vec{M}\rVert^{2}\,\mathrm{d}^{3}\mathbf{r}\\
-\frac{1}{2}\int_{\partial\Omega}\bigl(\vec{v}\cdot\hat{\mathbf{n}}\bigr)\,\lVert\vec{M}\rVert^{2}\,\mathrm{d}S.(81)

In particular, if∇⋅v→=0\nabla\cdot\vec{v}=0inΩ\Omegaandv→⋅𝐧^=0\vec{v}\cdot\hat{\mathbf{n}}=0on∂Ω\partial\Omega, then the transport terms vanish anddd​t​12​∫Ω∥M→∥2​d3​𝐫+∫ΩD​(𝐫)​∥∇M→∥2​d3​𝐫+∫ΩMx2+My2T2​(𝐫)​d3​𝐫+∫ΩMz2T1​(𝐫)​d3​𝐫=∫ΩM0​(𝐫)​MzT1​(𝐫)​d3​𝐫.\frac{\mathrm{d}}{\mathrm{d}t}\,\frac{1}{2}\int_{\Omega}\lVert\vec{M}\rVert^{2}\,\mathrm{d}^{3}\mathbf{r}+\int_{\Omega}D(\mathbf{r})\,\lVert\nabla\vec{M}\rVert^{2}\,\mathrm{d}^{3}\mathbf{r}\\
+\int_{\Omega}\frac{M_{x}^{2}+M_{y}^{2}}{T_{2}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}+\int_{\Omega}\frac{M_{z}^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}\\
=\int_{\Omega}\frac{M_{0}(\mathbf{r})\,M_{z}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}.(82)

Moreover, the right-hand side admits the bound∫ΩM0​MzT1​d3​𝐫≤12​∫ΩM02T1​d3​𝐫+12​∫ΩMz2T1​d3​𝐫,\int_{\Omega}\frac{M_{0}\,M_{z}}{T_{1}}\,\mathrm{d}^{3}\mathbf{r}\leq\frac{1}{2}\int_{\Omega}\frac{M_{0}^{2}}{T_{1}}\,\mathrm{d}^{3}\mathbf{r}+\frac{1}{2}\int_{\Omega}\frac{M_{z}^{2}}{T_{1}}\,\mathrm{d}^{3}\mathbf{r},(83)

which yields the a priori estimatedd​t​12​∫Ω∥M→∥2​d3​𝐫+∫ΩD​(𝐫)​∥∇M→∥2​d3​𝐫+∫ΩMx2+My2T2​(𝐫)​d3​𝐫+12​∫ΩMz2T1​(𝐫)​d3​𝐫≤12​∫ΩM0​(𝐫)2T1​(𝐫)​d3​𝐫+12​∫Ω(∇⋅v→)​∥M→∥2​d3​𝐫−12​∫∂Ω(v→⋅𝐧^)​∥M→∥2​dS.\frac{\mathrm{d}}{\mathrm{d}t}\,\frac{1}{2}\int_{\Omega}\lVert\vec{M}\rVert^{2}\,\mathrm{d}^{3}\mathbf{r}+\int_{\Omega}D(\mathbf{r})\,\lVert\nabla\vec{M}\rVert^{2}\,\mathrm{d}^{3}\mathbf{r}\\
+\int_{\Omega}\frac{M_{x}^{2}+M_{y}^{2}}{T_{2}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}+\frac{1}{2}\int_{\Omega}\frac{M_{z}^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}\\
\leq\frac{1}{2}\int_{\Omega}\frac{M_{0}(\mathbf{r})^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}+\frac{1}{2}\int_{\Omega}\bigl(\nabla\cdot\vec{v}\bigr)\,\lVert\vec{M}\rVert^{2}\,\mathrm{d}^{3}\mathbf{r}\\
-\frac{1}{2}\int_{\partial\Omega}\bigl(\vec{v}\cdot\hat{\mathbf{n}}\bigr)\,\lVert\vec{M}\rVert^{2}\,\mathrm{d}S.(84)

## Proof.

SinceM→\vec{M}is smooth, each term below is classically well defined and the integrations by parts are justified.

Take theL2​(Ω)3L^{2}(\Omega)^{3}inner product of (5) withM→\vec{M}and integrate overΩ\Omega. This gives∫ΩM→⋅∂tM→​d3​𝐫\displaystyle\int_{\Omega}\vec{M}\cdot\partial_{t}\vec{M}\,\mathrm{d}^{3}\mathbf{r}=γ​∫ΩM→⋅(M→×(B→d​[M→]+δ​B→))​d3​𝐫\displaystyle=\gamma\int_{\Omega}\vec{M}\cdot\Bigl(\vec{M}\times(\vec{B}_{d}[\vec{M}]+\delta\vec{B})\Bigr)\,\mathrm{d}^{3}\mathbf{r}−∫ΩM→⋅((v→⋅∇)​M→)​d3​𝐫\displaystyle-\int_{\Omega}\vec{M}\cdot\bigl((\vec{v}\cdot\nabla)\vec{M}\bigr)\,\mathrm{d}^{3}\mathbf{r}+∫ΩM→⋅∇⋅(D​(𝐫)​∇M→)​d3​𝐫\displaystyle\quad+\int_{\Omega}\vec{M}\cdot\nabla\cdot\bigl(D(\mathbf{r})\nabla\vec{M}\bigr)\,\mathrm{d}^{3}\mathbf{r}−∫ΩM→⋅Mx​𝐱^+My​𝐲^T2​(𝐫)​d3​𝐫\displaystyle-\int_{\Omega}\vec{M}\cdot\frac{M_{x}\,\hat{\mathbf{x}}+M_{y}\,\hat{\mathbf{y}}}{T_{2}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}+∫ΩM→⋅M0​(𝐫)−MzT1​(𝐫)​𝐳^​d3​𝐫.\displaystyle\quad+\int_{\Omega}\vec{M}\cdot\frac{M_{0}(\mathbf{r})-M_{z}}{T_{1}(\mathbf{r})}\,\hat{\mathbf{z}}\,\mathrm{d}^{3}\mathbf{r}.(85)

We evaluate the terms on the right-hand side one by one.

For the time derivative, usingM→⋅∂tM→=12​∂t|M→|2\vec{M}\cdot\partial_{t}\vec{M}=\frac{1}{2}\partial_{t}|\vec{M}|^{2}, we obtain∫ΩM→⋅∂tM→​d3​𝐫=dd​t​12​∫Ω|M→|2​d3​𝐫.\int_{\Omega}\vec{M}\cdot\partial_{t}\vec{M}\,\mathrm{d}^{3}\mathbf{r}=\frac{\mathrm{d}}{\mathrm{d}t}\,\frac{1}{2}\int_{\Omega}|\vec{M}|^{2}\,\mathrm{d}^{3}\mathbf{r}.(86)

For the precession term, the pointwise identitya→⋅(a→×b→)=0for all​a→,b→∈ℝ3\vec{a}\cdot(\vec{a}\times\vec{b})=0\quad\text{for all }\vec{a},\vec{b}\in\mathbb{R}^{3}(87)

impliesγ​∫ΩM→⋅(M→×(B→d​[M→]+δ​B→))​d3​𝐫=0.\gamma\int_{\Omega}\vec{M}\cdot\Bigl(\vec{M}\times(\vec{B}_{d}[\vec{M}]+\delta\vec{B})\Bigr)\,\mathrm{d}^{3}\mathbf{r}=0.(88)

For the advection term, sinceM→⋅((v→⋅∇)​M→)=12​v→⋅∇|M→|2,\vec{M}\cdot\bigl((\vec{v}\cdot\nabla)\vec{M}\bigr)=\frac{1}{2}\,\vec{v}\cdot\nabla|\vec{M}|^{2},(89)

the divergence theorem gives−∫ΩM→⋅((v→⋅∇)​M→)​d3​𝐫\displaystyle-\int_{\Omega}\vec{M}\cdot\bigl((\vec{v}\cdot\nabla)\vec{M}\bigr)\,\mathrm{d}^{3}\mathbf{r}=−12​∫Ωv→⋅∇|M→|2​d3​𝐫\displaystyle=-\frac{1}{2}\int_{\Omega}\vec{v}\cdot\nabla|\vec{M}|^{2}\,\mathrm{d}^{3}\mathbf{r}=−12​∫Ω∇⋅(v→​|M→|2)​d3​𝐫\displaystyle=-\frac{1}{2}\int_{\Omega}\nabla\cdot\bigl(\vec{v}\,|\vec{M}|^{2}\bigr)\,\mathrm{d}^{3}\mathbf{r}+12​∫Ω(∇⋅v→)​|M→|2​d3​𝐫\displaystyle+\frac{1}{2}\int_{\Omega}(\nabla\cdot\vec{v})\,|\vec{M}|^{2}\,\mathrm{d}^{3}\mathbf{r}=12​∫Ω(∇⋅v→)​|M→|2​d3​𝐫\displaystyle=\frac{1}{2}\int_{\Omega}(\nabla\cdot\vec{v})\,|\vec{M}|^{2}\,\mathrm{d}^{3}\mathbf{r}−12​∫∂Ω(v→⋅𝐧^)​|M→|2​dS.\displaystyle-\frac{1}{2}\int_{\partial\Omega}(\vec{v}\cdot\hat{\mathbf{n}})\,|\vec{M}|^{2}\,\mathrm{d}S.(90)

For the diffusion term, writing componentwise and integrating by parts,∫ΩM→⋅\displaystyle\int_{\Omega}\vec{M}\cdot∇⋅(D​(𝐫)​∇M→)​d3​𝐫\displaystyle\nabla\cdot\bigl(D(\mathbf{r})\nabla\vec{M}\bigr)\,\mathrm{d}^{3}\mathbf{r}(91)=∑i∈{x,y,z}∫ΩMi​∇⋅(D​(𝐫)​∇Mi)​d3​𝐫\displaystyle=\sum_{i\in\{x,y,z\}}\int_{\Omega}M_{i}\,\nabla\cdot\bigl(D(\mathbf{r})\nabla M_{i}\bigr)\,\mathrm{d}^{3}\mathbf{r}=−∑i∈{x,y,z}∫ΩD​(𝐫)​|∇Mi|2​d3​𝐫\displaystyle=-\sum_{i\in\{x,y,z\}}\int_{\Omega}D(\mathbf{r})\,|\nabla M_{i}|^{2}\,\mathrm{d}^{3}\mathbf{r}+∑i∈{x,y,z}∫∂ΩMi​𝐧^⋅(D​(𝐫)​∇Mi)​dS.\displaystyle+\sum_{i\in\{x,y,z\}}\int_{\partial\Omega}M_{i}\,\hat{\mathbf{n}}\cdot\bigl(D(\mathbf{r})\nabla M_{i}\bigr)\,\mathrm{d}S.(92)

The boundary term vanishes by (80), so∫ΩM→⋅∇⋅(D​(𝐫)​∇M→)​d3​𝐫=−∫ΩD​(𝐫)​|∇M→|2​d3​𝐫.\int_{\Omega}\vec{M}\cdot\nabla\cdot\bigl(D(\mathbf{r})\nabla\vec{M}\bigr)\,\mathrm{d}^{3}\mathbf{r}=-\int_{\Omega}D(\mathbf{r})\,|\nabla\vec{M}|^{2}\,\mathrm{d}^{3}\mathbf{r}.(93)

For the transverse relaxation term,−∫ΩM→⋅Mx​𝐱^+My​𝐲^T2​(𝐫)​d3​𝐫=−∫ΩMx2+My2T2​(𝐫)​d3​𝐫.-\int_{\Omega}\vec{M}\cdot\frac{M_{x}\,\hat{\mathbf{x}}+M_{y}\,\hat{\mathbf{y}}}{T_{2}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}=-\int_{\Omega}\frac{M_{x}^{2}+M_{y}^{2}}{T_{2}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}.(94)

For the longitudinal relaxation and recovery term,∫ΩM→⋅M0​(𝐫)−MzT1​(𝐫)​𝐳^​d3​𝐫\displaystyle\int_{\Omega}\vec{M}\cdot\frac{M_{0}(\mathbf{r})-M_{z}}{T_{1}(\mathbf{r})}\,\hat{\mathbf{z}}\,\mathrm{d}^{3}\mathbf{r}=∫Ω(M0​(𝐫)−Mz)​MzT1​(𝐫)​d3​𝐫\displaystyle=\int_{\Omega}\frac{(M_{0}(\mathbf{r})-M_{z})M_{z}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}=∫ΩM0​(𝐫)​MzT1​(𝐫)​d3​𝐫\displaystyle=\int_{\Omega}\frac{M_{0}(\mathbf{r})\,M_{z}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}(95)−∫ΩMz2T1​(𝐫)​d3​𝐫.\displaystyle\quad-\int_{\Omega}\frac{M_{z}^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}.(96)

Substituting (86), (88), (90), (93), (94), and (96) into (85) yields
(81). The stated special case∇⋅v→=0\nabla\cdot\vec{v}=0inΩ\Omegaandv→⋅𝐧^=0\vec{v}\cdot\hat{\mathbf{n}}=0on∂Ω\partial\Omegafollows immediately.

To derive (83), use the pointwise Young inequalitya​b≤12​a2+12​b2for all​a,b∈ℝ,ab\leq\frac{1}{2}a^{2}+\frac{1}{2}b^{2}\quad\text{for all }a,b\in\mathbb{R},(97)

witha=M0​(𝐫)T1​(𝐫),b=Mz​(𝐫)T1​(𝐫).a=\frac{M_{0}(\mathbf{r})}{\sqrt{T_{1}(\mathbf{r})}},\quad b=\frac{M_{z}(\mathbf{r})}{\sqrt{T_{1}(\mathbf{r})}}.(98)

BecauseT1​(𝐫)>0T_{1}(\mathbf{r})>0, this givesM0​(𝐫)​Mz​(𝐫)T1​(𝐫)≤12​M0​(𝐫)2T1​(𝐫)+12​Mz​(𝐫)2T1​(𝐫).\frac{M_{0}(\mathbf{r})\,M_{z}(\mathbf{r})}{T_{1}(\mathbf{r})}\leq\frac{1}{2}\,\frac{M_{0}(\mathbf{r})^{2}}{T_{1}(\mathbf{r})}+\frac{1}{2}\,\frac{M_{z}(\mathbf{r})^{2}}{T_{1}(\mathbf{r})}.(99)

Integrating (99) overΩ\Omegayields (83). Inserting (83) into (81) gives (84).
∎

## Proposition A.3(Continuous dependence).

LetM→(1)\vec{M}^{(1)}andM→(2)\vec{M}^{(2)}be weak solutions on[0,T∗][0,T^{\ast}]with initial dataM→init(1)\vec{M}_{\mathrm{init}}^{(1)}andM→init(2)\vec{M}_{\mathrm{init}}^{(2)}. Then, for allt∈[0,T∗]t\in[0,T^{\ast}],‖M→(1)​(t)−M→(2)​(t)‖H2≤exp⁡(C​t+C​∑ℓ=12∫0t‖M→(ℓ)​(s)‖V4/3​ds)​‖M→init(1)−M→init(2)‖H2,\|\vec{M}^{(1)}(t)-\vec{M}^{(2)}(t)\|_{H}^{2}\\
\leq\exp\Biggl(Ct+C\sum_{\ell=1}^{2}\int_{0}^{t}\|\vec{M}^{(\ell)}(s)\|_{V}^{4/3}\,\mathrm{d}s\Biggr)\|\vec{M}_{\mathrm{init}}^{(1)}-\vec{M}_{\mathrm{init}}^{(2)}\|_{H}^{2},(100)

whereCCdepends only onDmin−1D_{\min}^{-1},Ω\Omega, the Sobolev and trace
constants ofΩ\Omega, and‖𝒯a‖L2​(Ω)3→L2​(Ω)3\|\mathcal{T}_{a}\|_{L^{2}(\Omega)^{3}\to L^{2}(\Omega)^{3}},
and, in the non-skew advection formulation, also on‖∇⋅v→‖L∞​(Ω)\|\nabla\cdot\vec{v}\|_{L^{\infty}(\Omega)},‖v→⋅𝐧^‖L∞​(∂Ω)\|\vec{v}\cdot\hat{\mathbf{n}}\|_{L^{\infty}(\partial\Omega)},
and the chosen advection boundary conditions.

Consequently, sinceM→(1),M→(2)∈L2​(0,T∗;V)\vec{M}^{(1)},\vec{M}^{(2)}\in L^{2}(0,T^{\ast};V), there exists a constantC∗=C∗​(T∗,‖M→(1)‖L2​(0,T∗;V),‖M→(2)‖L2​(0,T∗;V))C_{\ast}=C_{\ast}\Bigl(T^{\ast},\|\vec{M}^{(1)}\|_{L^{2}(0,T^{\ast};V)},\|\vec{M}^{(2)}\|_{L^{2}(0,T^{\ast};V)}\Bigr)(101)

such that‖M→(1)​(t)−M→(2)​(t)‖H2≤C∗​eC∗​t​‖M→init(1)−M→init(2)‖H2\|\vec{M}^{(1)}(t)-\vec{M}^{(2)}(t)\|_{H}^{2}\leq C_{\ast}e^{C_{\ast}t}\|\vec{M}_{\mathrm{init}}^{(1)}-\vec{M}_{\mathrm{init}}^{(2)}\|_{H}^{2}(102)

for allt∈[0,T∗]t\in[0,T^{\ast}].

## Proof.

SetW→:=M→(1)−M→(2),B→(ℓ):=𝒯a​[M→(ℓ)]+δ​B→,ℓ∈{1,2}.\vec{W}:=\vec{M}^{(1)}-\vec{M}^{(2)},\quad\vec{B}^{(\ell)}:=\mathcal{T}_{a}[\vec{M}^{(\ell)}]+\delta\vec{B},\quad\ell\in\{1,2\}.(103)

SinceM→(1),M→(2)∈X∩C​([0,T∗];H)\vec{M}^{(1)},\vec{M}^{(2)}\in X\cap C([0,T^{\ast}];H), we haveW→∈X∩C​([0,T∗];H).\vec{W}\in X\cap C([0,T^{\ast}];H).(104)

Subtract the two weak formulations. Then, for almost everyt∈(0,T∗)t\in(0,T^{\ast})and everyΦ→∈V\vec{\Phi}\in V,⟨∂tW→,Φ→⟩V′,V\displaystyle\langle\partial_{t}\vec{W},\vec{\Phi}\rangle_{V^{\prime},V}+∫ΩD​(𝐫)​∇W→:∇Φ→​d3​𝐫\displaystyle+\int_{\Omega}D(\mathbf{r})\,\nabla\vec{W}:\nabla\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}+∫Ω(W1​Φ1+W2​Φ2T2​(𝐫)+W3​Φ3T1​(𝐫))​d3​𝐫\displaystyle+\int_{\Omega}\left(\frac{W_{1}\Phi_{1}+W_{2}\Phi_{2}}{T_{2}(\mathbf{r})}+\frac{W_{3}\Phi_{3}}{T_{1}(\mathbf{r})}\right)\mathrm{d}^{3}\mathbf{r}+∑i=13aadv​(Wi,Φi)\displaystyle+\sum_{i=1}^{3}a_{\mathrm{adv}}(W_{i},\Phi_{i})=γ​∫Ω(M→(1)×B→(1)−M→(2)×B→(2))⋅Φ→​d3​𝐫.\displaystyle=\gamma\int_{\Omega}\Bigl(\vec{M}^{(1)}\times\vec{B}^{(1)}-\vec{M}^{(2)}\times\vec{B}^{(2)}\Bigr)\cdot\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}.(105)

The inhomogeneous recovery term cancels because it is the same in both
equations.

ChooseΦ→=W→​(t)\vec{\Phi}=\vec{W}(t). SinceW→∈L2​(0,T∗;V)∩H1​(0,T∗;V′)\vec{W}\in L^{2}(0,T^{\ast};V)\cap H^{1}(0,T^{\ast};V^{\prime}), the Lions–Magenes
identity yields⟨∂tW→​(t),W→​(t)⟩V′,V=12​dd​t​‖W→​(t)‖H2\langle\partial_{t}\vec{W}(t),\vec{W}(t)\rangle_{V^{\prime},V}=\frac{1}{2}\frac{\mathrm{d}}{\mathrm{d}t}\|\vec{W}(t)\|_{H}^{2}(106)

for almost everyt∈(0,T∗)t\in(0,T^{\ast}). Therefore12​dd​t​‖W→​(t)‖H2\displaystyle\frac{1}{2}\frac{\mathrm{d}}{\mathrm{d}t}\|\vec{W}(t)\|_{H}^{2}+∫ΩD​(𝐫)​|∇W→|2​d3​𝐫\displaystyle+\int_{\Omega}D(\mathbf{r})\,|\nabla\vec{W}|^{2}\,\mathrm{d}^{3}\mathbf{r}+∫ΩW12+W22T2​(𝐫)​d3​𝐫+∫ΩW32T1​(𝐫)​d3​𝐫\displaystyle+\int_{\Omega}\frac{W_{1}^{2}+W_{2}^{2}}{T_{2}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}+\int_{\Omega}\frac{W_{3}^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}=γ​∫Ω(M→(1)×B→(1)−M→(2)×B→(2))⋅W→​d3​𝐫\displaystyle=\gamma\int_{\Omega}\Bigl(\vec{M}^{(1)}\times\vec{B}^{(1)}-\vec{M}^{(2)}\times\vec{B}^{(2)}\Bigr)\cdot\vec{W}\,\mathrm{d}^{3}\mathbf{r}−∑i=13aadv​(Wi,Wi).\displaystyle\quad-\sum_{i=1}^{3}a_{\mathrm{adv}}(W_{i},W_{i}).(107)

We first estimate the nonlinear precession term. UsingM→(1)×B→(1)−M→(2)×B→(2)=W→×B→(1)+M→(2)×𝒯a​[W→],\vec{M}^{(1)}\times\vec{B}^{(1)}-\vec{M}^{(2)}\times\vec{B}^{(2)}=\vec{W}\times\vec{B}^{(1)}+\vec{M}^{(2)}\times\mathcal{T}_{a}[\vec{W}],(108)

and the pointwise identityW→⋅(W→×B→(1))=0,\vec{W}\cdot\bigl(\vec{W}\times\vec{B}^{(1)}\bigr)=0,(109)

we obtain|∫Ω(M→(1)×B→(1)−M→(2)×B→(2))⋅W→​d3​𝐫|\displaystyle\left|\int_{\Omega}\Bigl(\vec{M}^{(1)}\times\vec{B}^{(1)}-\vec{M}^{(2)}\times\vec{B}^{(2)}\Bigr)\cdot\vec{W}\,\mathrm{d}^{3}\mathbf{r}\right|=|∫Ω(M→(2)×𝒯a​[W→])⋅W→​d3​𝐫|\displaystyle\quad=\left|\int_{\Omega}\bigl(\vec{M}^{(2)}\times\mathcal{T}_{a}[\vec{W}]\bigr)\cdot\vec{W}\,\mathrm{d}^{3}\mathbf{r}\right|≤‖M→(2)‖L6​(Ω)​‖W→‖L3​(Ω)​‖𝒯a​[W→]‖L2​(Ω).\displaystyle\quad\leq\|\vec{M}^{(2)}\|_{L^{6}(\Omega)}\|\vec{W}\|_{L^{3}(\Omega)}\|\mathcal{T}_{a}[\vec{W}]\|_{L^{2}(\Omega)}.(110)

By Sobolev embedding, interpolation, and theL2L^{2}boundedness of𝒯a\mathcal{T}_{a},‖M→(2)‖L6​(Ω)\displaystyle\|\vec{M}^{(2)}\|_{L^{6}(\Omega)}≤C​‖M→(2)‖V,\displaystyle\leq C\|\vec{M}^{(2)}\|_{V},‖W→‖L3​(Ω)\displaystyle\|\vec{W}\|_{L^{3}(\Omega)}≤C​‖W→‖H1/2​‖W→‖V1/2,\displaystyle\leq C\|\vec{W}\|_{H}^{1/2}\|\vec{W}\|_{V}^{1/2},‖𝒯a​[W→]‖L2​(Ω)\displaystyle\|\mathcal{T}_{a}[\vec{W}]\|_{L^{2}(\Omega)}≤C​‖W→‖H.\displaystyle\leq C\|\vec{W}\|_{H}.

Hence|γ​∫Ω(M→(1)×B→(1)−M→(2)×B→(2))⋅W→​d3​𝐫|≤C​‖M→(2)‖V​‖W→‖H3/2​‖W→‖V1/2.\left|\gamma\int_{\Omega}\Bigl(\vec{M}^{(1)}\times\vec{B}^{(1)}-\vec{M}^{(2)}\times\vec{B}^{(2)}\Bigr)\cdot\vec{W}\,\mathrm{d}^{3}\mathbf{r}\right|\\
\leq C\|\vec{M}^{(2)}\|_{V}\|\vec{W}\|_{H}^{3/2}\|\vec{W}\|_{V}^{1/2}.(111)

Applying Young’s inequality with exponents44and4/34/3gives, for everyε>0\varepsilon>0,C​‖M→(2)‖V​‖W→‖H3/2​‖W→‖V1/2≤ε​‖W→‖V2+Cε​‖M→(2)‖V4/3​‖W→‖H2.C\|\vec{M}^{(2)}\|_{V}\|\vec{W}\|_{H}^{3/2}\|\vec{W}\|_{V}^{1/2}\leq\varepsilon\|\vec{W}\|_{V}^{2}+C_{\varepsilon}\|\vec{M}^{(2)}\|_{V}^{4/3}\|\vec{W}\|_{H}^{2}.(112)

Since‖W→‖V2=‖W→‖H2+‖∇W→‖L2​(Ω)2\|\vec{W}\|_{V}^{2}=\|\vec{W}\|_{H}^{2}+\|\nabla\vec{W}\|_{L^{2}(\Omega)}^{2}(113)

andD​(𝐫)≥Dmin>0D(\mathbf{r})\geq D_{\min}>0, we may chooseε\varepsilonsmall enough
to obtain|γ​∫Ω(M→(1)×B→(1)−M→(2)×B→(2))⋅W→​d3​𝐫|≤Dmin4​‖∇W→‖L2​(Ω)2+C​(1+‖M→(2)‖V4/3)​‖W→‖H2.\left|\gamma\int_{\Omega}\Bigl(\vec{M}^{(1)}\times\vec{B}^{(1)}-\vec{M}^{(2)}\times\vec{B}^{(2)}\Bigr)\cdot\vec{W}\,\mathrm{d}^{3}\mathbf{r}\right|\\
\leq\frac{D_{\min}}{4}\|\nabla\vec{W}\|_{L^{2}(\Omega)}^{2}+C\Bigl(1+\|\vec{M}^{(2)}\|_{V}^{4/3}\Bigr)\|\vec{W}\|_{H}^{2}.(114)

Interchanging the roles ofM→(1)\vec{M}^{(1)}andM→(2)\vec{M}^{(2)}gives the
symmetric bound|γ​∫Ω(M→(1)×B→(1)−M→(2)×B→(2))⋅W→​d3​𝐫|≤Dmin4​‖∇W→‖L2​(Ω)2+C​(1+‖M→(1)‖V4/3+‖M→(2)‖V4/3)​‖W→‖H2.\left|\gamma\int_{\Omega}\Bigl(\vec{M}^{(1)}\times\vec{B}^{(1)}-\vec{M}^{(2)}\times\vec{B}^{(2)}\Bigr)\cdot\vec{W}\,\mathrm{d}^{3}\mathbf{r}\right|\\
\leq\frac{D_{\min}}{4}\|\nabla\vec{W}\|_{L^{2}(\Omega)}^{2}\\
+C\Bigl(1+\|\vec{M}^{(1)}\|_{V}^{4/3}+\|\vec{M}^{(2)}\|_{V}^{4/3}\Bigr)\|\vec{W}\|_{H}^{2}.(115)

We next estimate the advection contribution. If advection is written in the
skew-symmetric form under (31), thenaadv​(Wi,Wi)=0,i=1,2,3.a_{\mathrm{adv}}(W_{i},W_{i})=0,\quad i=1,2,3.(116)

If instead one uses the standard advective formaadv​(Wi,Wi)=∫Ω(v→⋅∇Wi)​Wi​d3​𝐫,a_{\mathrm{adv}}(W_{i},W_{i})=\int_{\Omega}(\vec{v}\cdot\nabla W_{i})\,W_{i}\,\mathrm{d}^{3}\mathbf{r},(117)

then integration by parts yields−∑i=13aadv​(Wi,Wi)=12​∫Ω(∇⋅v→)​|W→|2​d3​𝐫−12​∫∂Ω(v→⋅𝐧^)​|W→|2​dS.-\sum_{i=1}^{3}a_{\mathrm{adv}}(W_{i},W_{i})=\frac{1}{2}\int_{\Omega}(\nabla\cdot\vec{v})\,|\vec{W}|^{2}\,\mathrm{d}^{3}\mathbf{r}\\
-\frac{1}{2}\int_{\partial\Omega}(\vec{v}\cdot\hat{\mathbf{n}})\,|\vec{W}|^{2}\,\mathrm{d}S.(118)

The volume term satisfies|12​∫Ω(∇⋅v→)​|W→|2​d3​𝐫|≤12​‖∇⋅v→‖L∞​(Ω)​‖W→‖H2.\left|\frac{1}{2}\int_{\Omega}(\nabla\cdot\vec{v})\,|\vec{W}|^{2}\,\mathrm{d}^{3}\mathbf{r}\right|\leq\frac{1}{2}\|\nabla\cdot\vec{v}\|_{L^{\infty}(\Omega)}\|\vec{W}\|_{H}^{2}.(119)

For the boundary term, the trace inequality gives‖W→‖L2​(∂Ω)2≤Ctr​‖W→‖H​‖W→‖V.\|\vec{W}\|_{L^{2}(\partial\Omega)}^{2}\leq C_{\mathrm{tr}}\|\vec{W}\|_{H}\|\vec{W}\|_{V}.(120)

Hence, for everyε>0\varepsilon>0,‖W→‖L2​(∂Ω)2≤ε​‖W→‖V2+Cε,Ω​‖W→‖H2,\|\vec{W}\|_{L^{2}(\partial\Omega)}^{2}\leq\varepsilon\|\vec{W}\|_{V}^{2}+C_{\varepsilon,\Omega}\|\vec{W}\|_{H}^{2},(121)

and therefore|12​∫∂Ω(v→⋅𝐧^)​|W→|2​dS|≤ε​‖W→‖V2+Cε,Ω​‖v→⋅𝐧^‖L∞​(∂Ω)​‖W→‖H2.\left|\frac{1}{2}\int_{\partial\Omega}(\vec{v}\cdot\hat{\mathbf{n}})\,|\vec{W}|^{2}\,\mathrm{d}S\right|\\
\leq\varepsilon\|\vec{W}\|_{V}^{2}+C_{\varepsilon,\Omega}\|\vec{v}\cdot\hat{\mathbf{n}}\|_{L^{\infty}(\partial\Omega)}\|\vec{W}\|_{H}^{2}.(122)

Substituting (115) into
(107), and, in the non-skew advection case,
also using (119) and
(122), we chooseε>0\varepsilon>0sufficiently
small so that all gradient terms are absorbed by the diffusion term. Since
the relaxation terms are nonnegative, they may be discarded. We obtain, for
almost everyt∈(0,T∗)t\in(0,T^{\ast}),dd​t​‖W→​(t)‖H2≤g​(t)​‖W→​(t)‖H2,\frac{\mathrm{d}}{\mathrm{d}t}\|\vec{W}(t)\|_{H}^{2}\leq g(t)\,\|\vec{W}(t)\|_{H}^{2},(123)

where one may takeg​(t)=C​(1+‖M→(1)​(t)‖V4/3+‖M→(2)​(t)‖V4/3)g(t)=C\Bigl(1+\|\vec{M}^{(1)}(t)\|_{V}^{4/3}+\|\vec{M}^{(2)}(t)\|_{V}^{4/3}\Bigr)(124)

in the skew-advection case, and in the non-skew case one adds the constant
terms coming from‖∇⋅v→‖L∞​(Ω)\|\nabla\cdot\vec{v}\|_{L^{\infty}(\Omega)}and‖v→⋅𝐧^‖L∞​(∂Ω)\|\vec{v}\cdot\hat{\mathbf{n}}\|_{L^{\infty}(\partial\Omega)}.

BecauseM→(1),M→(2)∈L2​(0,T∗;V)\vec{M}^{(1)},\vec{M}^{(2)}\in L^{2}(0,T^{\ast};V)and4/3<24/3<2, we haveg∈L1​(0,T∗)g\in L^{1}(0,T^{\ast}). Grönwall’s inequality therefore yields‖W→​(t)‖H2≤exp⁡(∫0tg​(s)​ds)​‖W→​(0)‖H2=exp⁡(∫0tg​(s)​ds)​‖M→init(1)−M→init(2)‖H2,0≤t≤T∗.\|\vec{W}(t)\|_{H}^{2}\leq\exp\left(\int_{0}^{t}g(s)\,\mathrm{d}s\right)\|\vec{W}(0)\|_{H}^{2}\\
=\exp\left(\int_{0}^{t}g(s)\,\mathrm{d}s\right)\|\vec{M}_{\mathrm{init}}^{(1)}-\vec{M}_{\mathrm{init}}^{(2)}\|_{H}^{2},\quad 0\leq t\leq T^{\ast}.(125)

This proves (100).

Finally, Hölder’s inequality gives∫0t‖M→(ℓ)​(s)‖V4/3​ds≤t1/3​‖M→(ℓ)‖L2​(0,t;V)4/3≤(T∗)1/3​‖M→(ℓ)‖L2​(0,T∗;V)4/3,\int_{0}^{t}\|\vec{M}^{(\ell)}(s)\|_{V}^{4/3}\,\mathrm{d}s\leq t^{1/3}\|\vec{M}^{(\ell)}\|_{L^{2}(0,t;V)}^{4/3}\\
\leq(T^{\ast})^{1/3}\|\vec{M}^{(\ell)}\|_{L^{2}(0,T^{\ast};V)}^{4/3},

so the exponential factor in (100) is bounded byC∗​eC∗​tC_{\ast}e^{C_{\ast}t}for a suitable constantC∗C_{\ast}depending onT∗T^{\ast}and the twoL2​(0,T∗;V)L^{2}(0,T^{\ast};V)norms. This proves the final stated
estimate.
∎

## Corollary A.4(Global existence under additional conditions).

AssumeSection˜IIIand fixa>0a>0. If eitherv→≡0\vec{v}\equiv 0or (31) holds and advection is imposed in an
energy-neutral form, then the weak solution inTheorem˜A.8extends to[0,T][0,T]for anyT>0T>0.

## Proof.

Let[0,Tmax)[0,T_{\max})denote the maximal interval of existence of the unique
weak solution furnished byTheorem˜A.8. We prove thatTmax=∞T_{\max}=\infty. Suppose, for contradiction, thatTmax<∞T_{\max}<\infty.

Under the hypotheses of the corollary, the advection contribution is either
absent or energy-neutral. Therefore the weak solution satisfies the same
a priori estimate as in (84), with the transport
terms omitted. More precisely, this estimate follows by the standard
regularization and density argument for weak solutions: one first derives
the energy identity for sufficiently smooth approximants and then passes to
the limit using weak lower semicontinuity. Hence, for almost everyt∈(0,Tmax)t\in(0,T_{\max}),dd​t​12​‖M→​(t)‖H2+∫ΩD​(𝐫)​|∇M→​(t)|2​d3​𝐫+∫ΩM1​(t)2+M2​(t)2T2​(𝐫)​d3​𝐫+12​∫ΩM3​(t)2T1​(𝐫)​d3​𝐫≤12​∫ΩM0​(𝐫)2T1​(𝐫)​d3​𝐫.\frac{\mathrm{d}}{\mathrm{d}t}\,\frac{1}{2}\|\vec{M}(t)\|_{H}^{2}+\int_{\Omega}D(\mathbf{r})\,|\nabla\vec{M}(t)|^{2}\,\mathrm{d}^{3}\mathbf{r}\\
+\int_{\Omega}\frac{M_{1}(t)^{2}+M_{2}(t)^{2}}{T_{2}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}+\frac{1}{2}\int_{\Omega}\frac{M_{3}(t)^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}\\
\leq\frac{1}{2}\int_{\Omega}\frac{M_{0}(\mathbf{r})^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}.(126)

Integrating (126) from0toτ<Tmax\tau<T_{\max}yields12​‖M→​(τ)‖H2+∫0τ∫ΩD​(𝐫)​|∇M→​(t)|2​d3​𝐫​dt+∫0τ∫ΩM1​(t)2+M2​(t)2T2​(𝐫)​d3​𝐫​dt+12​∫0τ∫ΩM3​(t)2T1​(𝐫)​d3​𝐫​dt≤12​‖M→init‖H2+τ2​∫ΩM0​(𝐫)2T1​(𝐫)​d3​𝐫.\frac{1}{2}\|\vec{M}(\tau)\|_{H}^{2}+\int_{0}^{\tau}\!\!\int_{\Omega}D(\mathbf{r})\,|\nabla\vec{M}(t)|^{2}\,\mathrm{d}^{3}\mathbf{r}\,\mathrm{d}t\\
+\int_{0}^{\tau}\!\!\int_{\Omega}\frac{M_{1}(t)^{2}+M_{2}(t)^{2}}{T_{2}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}\,\mathrm{d}t\\
+\frac{1}{2}\int_{0}^{\tau}\!\!\int_{\Omega}\frac{M_{3}(t)^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}\,\mathrm{d}t\\
\leq\frac{1}{2}\|\vec{M}_{\mathrm{init}}\|_{H}^{2}+\frac{\tau}{2}\int_{\Omega}\frac{M_{0}(\mathbf{r})^{2}}{T_{1}(\mathbf{r})}\,\mathrm{d}^{3}\mathbf{r}.(127)

It follows thatsup0≤t<Tmax‖M→​(t)‖H2≤CTmax,\sup_{0\leq t<T_{\max}}\|\vec{M}(t)\|_{H}^{2}\leq C_{T_{\max}},(128)

whereCTmaxC_{T_{\max}}depends only onTmaxT_{\max},‖M→init‖H\|\vec{M}_{\mathrm{init}}\|_{H}, and‖M0/T1‖L2​(Ω)\|M_{0}/\sqrt{T_{1}}\|_{L^{2}(\Omega)}. SinceD​(𝐫)≥Dmin>0D(\mathbf{r})\geq D_{\min}>0, (127) also
implies∫0Tmax‖∇M→​(t)‖L2​(Ω)2​dt≤CTmax.\int_{0}^{T_{\max}}\|\nabla\vec{M}(t)\|_{L^{2}(\Omega)}^{2}\,\mathrm{d}t\leq C_{T_{\max}}.(129)

Combining (128) and (129), we
obtainM→∈L∞​(0,Tmax;H)∩L2​(0,Tmax;V).\vec{M}\in L^{\infty}(0,T_{\max};H)\cap L^{2}(0,T_{\max};V).(130)

We next estimate∂tM→\partial_{t}\vec{M}inL2​(0,Tmax;V′)L^{2}(0,T_{\max};V^{\prime}). LetΦ→∈V\vec{\Phi}\in V. Using the weak formulation (12), we have,
for almost everyt∈(0,Tmax)t\in(0,T_{\max}),|⟨∂tM→​(t),Φ→⟩V′,V|\displaystyle\left|\langle\partial_{t}\vec{M}(t),\vec{\Phi}\rangle_{V^{\prime},V}\right|≤|γ|​|∫Ω(M→​(t)×𝒯a​[M→​(t)])⋅Φ→​d3​𝐫|\displaystyle\leq|\gamma|\left|\int_{\Omega}\bigl(\vec{M}(t)\times\mathcal{T}_{a}[\vec{M}(t)]\bigr)\cdot\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}\right|+|γ|​|∫Ω(M→​(t)×δ​B→)⋅Φ→​d3​𝐫|\displaystyle+|\gamma|\left|\int_{\Omega}\bigl(\vec{M}(t)\times\delta\vec{B}\bigr)\cdot\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}\right|+|∫ΩD(𝐫)∇M→(t):∇Φ→d3𝐫|\displaystyle+\left|\int_{\Omega}D(\mathbf{r})\,\nabla\vec{M}(t):\nabla\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}\right|+|∫Ω(M1​(t)​Φ1+M2​(t)​Φ2T2​(𝐫)\displaystyle+\Biggl|\int_{\Omega}\Bigl(\frac{M_{1}(t)\Phi_{1}+M_{2}(t)\Phi_{2}}{T_{2}(\mathbf{r})}+M3​(t)​Φ3T1​(𝐫))d3𝐫|\displaystyle\quad+\frac{M_{3}(t)\Phi_{3}}{T_{1}(\mathbf{r})}\Bigr)\mathrm{d}^{3}\mathbf{r}\Biggr|+|∑i=13aadv​(Mi​(t),Φi)|\displaystyle+\left|\sum_{i=1}^{3}a_{\mathrm{adv}}(M_{i}(t),\Phi_{i})\right|+|∫ΩM0​(𝐫)T1​(𝐫)​Φ3​d3​𝐫|.\displaystyle\quad+\left|\int_{\Omega}\frac{M_{0}(\mathbf{r})}{T_{1}(\mathbf{r})}\,\Phi_{3}\,\mathrm{d}^{3}\mathbf{r}\right|.(131)

Each term on the right-hand side is bounded by a multiple of‖Φ→‖V\|\vec{\Phi}\|_{V}. For the DDF term, Sobolev embedding,V↪L3​(Ω)3V\hookrightarrow L^{3}(\Omega)^{3}, and boundedness of𝒯a\mathcal{T}_{a}onL2​(Ω)3L^{2}(\Omega)^{3}yield|∫Ω(M→×𝒯a​[M→])⋅Φ→​d3​𝐫|\displaystyle\left|\int_{\Omega}\bigl(\vec{M}\times\mathcal{T}_{a}[\vec{M}]\bigr)\cdot\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}\right|≤‖M→‖L6​(Ω)​‖𝒯a​[M→]‖L2​(Ω)​‖Φ→‖L3​(Ω)\displaystyle\leq\|\vec{M}\|_{L^{6}(\Omega)}\|\mathcal{T}_{a}[\vec{M}]\|_{L^{2}(\Omega)}\|\vec{\Phi}\|_{L^{3}(\Omega)}≤C​‖M→‖V​‖M→‖H​‖Φ→‖V.\displaystyle\leq C\,\|\vec{M}\|_{V}\,\|\vec{M}\|_{H}\,\|\vec{\Phi}\|_{V}.(132)

For the offset-field term,|∫Ω(M→×δ​B→)⋅Φ→​d3​𝐫|≤‖δ​B→‖L∞​(Ω)​‖M→‖H​‖Φ→‖H≤C​‖M→‖H​‖Φ→‖V.\left|\int_{\Omega}\bigl(\vec{M}\times\delta\vec{B}\bigr)\cdot\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}\right|\leq\|\delta\vec{B}\|_{L^{\infty}(\Omega)}\|\vec{M}\|_{H}\|\vec{\Phi}\|_{H}\\
\leq C\,\|\vec{M}\|_{H}\|\vec{\Phi}\|_{V}.(133)

For diffusion,|∫ΩD(𝐫)∇M→:∇Φ→d3𝐫|≤∥D∥L∞​(Ω)∥M→∥V∥Φ→∥V.\left|\int_{\Omega}D(\mathbf{r})\,\nabla\vec{M}:\nabla\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}\right|\leq\|D\|_{L^{\infty}(\Omega)}\|\vec{M}\|_{V}\|\vec{\Phi}\|_{V}.(134)

For relaxation,|∫Ω(M1​Φ1+M2​Φ2T2​(𝐫)+M3​Φ3T1​(𝐫))​d3​𝐫|\displaystyle\left|\int_{\Omega}\left(\frac{M_{1}\Phi_{1}+M_{2}\Phi_{2}}{T_{2}(\mathbf{r})}+\frac{M_{3}\Phi_{3}}{T_{1}(\mathbf{r})}\right)\mathrm{d}^{3}\mathbf{r}\right|≤C​‖M→‖H​‖Φ→‖H\displaystyle\leq C\,\|\vec{M}\|_{H}\|\vec{\Phi}\|_{H}≤C​‖M→‖H​‖Φ→‖V.\displaystyle\leq C\,\|\vec{M}\|_{H}\|\vec{\Phi}\|_{V}.(135)

Ifv→≡0\vec{v}\equiv 0, the advection term is absent. If advection is imposed
in the skew form under (31), then|aadv​(Mi,Φi)|≤C​‖Mi‖H1​(Ω)​‖Φi‖H1​(Ω),i=1,2,3,|a_{\mathrm{adv}}(M_{i},\Phi_{i})|\leq C\,\|M_{i}\|_{H^{1}(\Omega)}\|\Phi_{i}\|_{H^{1}(\Omega)},\quad i=1,2,3,(136)

so the total advection contribution is bounded byC​‖M→‖V​‖Φ→‖VC\|\vec{M}\|_{V}\|\vec{\Phi}\|_{V}. Finally,|∫ΩM0​(𝐫)T1​(𝐫)​Φ3​d3​𝐫|≤‖M0T1‖L2​(Ω)​‖Φ→‖H≤C​‖Φ→‖V.\left|\int_{\Omega}\frac{M_{0}(\mathbf{r})}{T_{1}(\mathbf{r})}\,\Phi_{3}\,\mathrm{d}^{3}\mathbf{r}\right|\leq\left\|\frac{M_{0}}{T_{1}}\right\|_{L^{2}(\Omega)}\|\vec{\Phi}\|_{H}\leq C\|\vec{\Phi}\|_{V}.(137)

Combining
(131)–(137)
and taking the supremum overΦ→∈V\vec{\Phi}\in Vwith‖Φ→‖V=1\|\vec{\Phi}\|_{V}=1, we
obtain‖∂tM→​(t)‖V′≤C​(‖M→​(t)‖V​‖M→​(t)‖H+‖M→​(t)‖V+‖M→​(t)‖H+1)\|\partial_{t}\vec{M}(t)\|_{V^{\prime}}\leq C\Bigl(\|\vec{M}(t)\|_{V}\|\vec{M}(t)\|_{H}+\|\vec{M}(t)\|_{V}+\|\vec{M}(t)\|_{H}+1\Bigr)(138)

for almost everyt∈(0,Tmax)t\in(0,T_{\max}). By (130), the
right-hand side belongs toL2​(0,Tmax)L^{2}(0,T_{\max}). Therefore∂tM→∈L2​(0,Tmax;V′).\partial_{t}\vec{M}\in L^{2}(0,T_{\max};V^{\prime}).(139)

Together with (130), this givesM→∈L2​(0,Tmax;V)∩H1​(0,Tmax;V′).\vec{M}\in L^{2}(0,T_{\max};V)\cap H^{1}(0,T_{\max};V^{\prime}).(140)

ByLemma˜A.7,M→\vec{M}admits anHH-continuous representative on[0,Tmax][0,T_{\max}]. In particular, the one-sided limitM→∗:=limt↑TmaxM→​(t)\vec{M}_{\ast}:=\lim_{t\uparrow T_{\max}}\vec{M}(t)(141)

exists inHH.

We now restart the local theory at timeTmaxT_{\max}. Since the equation is
autonomous and the coefficients are time-independent, the same argument as
inTheorem˜A.8applies with initial timeTmaxT_{\max}and initial datumM→∗\vec{M}_{\ast}. Therefore there existε>0\varepsilon>0and a weak solutionM→~∈L2​(Tmax,Tmax+ε;V)∩H1​(Tmax,Tmax+ε;V′)∩C​([Tmax,Tmax+ε];H)\widetilde{\vec{M}}\in L^{2}(T_{\max},T_{\max}+\varepsilon;V)\cap H^{1}(T_{\max},T_{\max}+\varepsilon;V^{\prime})\\
\cap C([T_{\max},T_{\max}+\varepsilon];H)

such thatM→~​(Tmax)=M→∗.\widetilde{\vec{M}}(T_{\max})=\vec{M}_{\ast}.(142)

DefineM→^​(t):={M→​(t),0≤t≤Tmax,M→~​(t),Tmax≤t≤Tmax+ε.\widehat{\vec{M}}(t):=\begin{cases}\vec{M}(t),&0\leq t\leq T_{\max},\\
\widetilde{\vec{M}}(t),&T_{\max}\leq t\leq T_{\max}+\varepsilon.\end{cases}(143)

Because both pieces satisfy the weak formulation on their respective time
intervals and coincide att=Tmaxt=T_{\max}inHH, the functionM→^\widehat{\vec{M}}is a weak solution on[0,Tmax+ε][0,T_{\max}+\varepsilon]. This
contradicts the maximality ofTmaxT_{\max}.

HenceTmax=∞T_{\max}=\infty. Therefore the weak solution extends to[0,T][0,T]for
every finiteT>0T>0.
∎

## Lemma A.5(Precession isL2L^{2}-neutral).

For anyM→,B→∈(L2​(Ω))3\vec{M},\vec{B}\in(L^{2}(\Omega))^{3},∫ΩM→⋅(M→×B→)​d3​𝐫=0.\int_{\Omega}\vec{M}\cdot\bigl(\vec{M}\times\vec{B}\bigr)\,\mathrm{d}^{3}\mathbf{r}=0.(144)

## Proof.

SinceM→,B→∈(L2​(Ω))3\vec{M},\vec{B}\in(L^{2}(\Omega))^{3}, all component functions are
measurable, and therefore𝐫↦M→​(𝐫)⋅(M→​(𝐫)×B→​(𝐫))\mathbf{r}\mapsto\vec{M}(\mathbf{r})\cdot\bigl(\vec{M}(\mathbf{r})\times\vec{B}(\mathbf{r})\bigr)(145)

is measurable onΩ\Omega, being a polynomial expression in the components
ofM→\vec{M}andB→\vec{B}.

For almost every𝐫∈Ω\mathbf{r}\in\Omega, the vectorsM→​(𝐫)\vec{M}(\mathbf{r})andB→​(𝐫)\vec{B}(\mathbf{r})are defined, and the algebraic
identitya→⋅(a→×b→)=0for all​a→,b→∈ℝ3\vec{a}\cdot(\vec{a}\times\vec{b})=0\quad\text{for all }\vec{a},\vec{b}\in\mathbb{R}^{3}(146)

givesM→​(𝐫)⋅(M→​(𝐫)×B→​(𝐫))=0for a.e.​𝐫∈Ω.\vec{M}(\mathbf{r})\cdot\bigl(\vec{M}(\mathbf{r})\times\vec{B}(\mathbf{r})\bigr)=0\quad\text{for a.e. }\mathbf{r}\in\Omega.(147)

Hence the integrand vanishes almost everywhere, so its integral is zero.
∎

## Lemma A.6(Lipschitz estimate for the precession nonlinearity).

Define𝒩​(M→)=M→×(𝒯a​[M→]+δ​B→).\mathcal{N}(\vec{M})=\vec{M}\times\Bigl(\mathcal{T}_{a}[\vec{M}]+\delta\vec{B}\Bigr).(148)

There exists a constantC>0C>0, depending only onaa,Ω\Omega, and‖δ​B→‖L∞​(Ω)\|\delta\vec{B}\|_{L^{\infty}(\Omega)}, such that for allM→,N→∈H1​(Ω)3\vec{M},\vec{N}\in H^{1}(\Omega)^{3},‖𝒩​(M→)−𝒩​(N→)‖H−1​(Ω)3≤C​(‖M→‖H1​(Ω)+‖N→‖H1​(Ω)+1)​‖M→−N→‖H1​(Ω).\bigl\|\mathcal{N}(\vec{M})-\mathcal{N}(\vec{N})\bigr\|_{H^{-1}(\Omega)^{3}}\\
\leq C\Bigl(\|\vec{M}\|_{H^{1}(\Omega)}+\|\vec{N}\|_{H^{1}(\Omega)}+1\Bigr)\|\vec{M}-\vec{N}\|_{H^{1}(\Omega)}.(149)

## Proof.

LetW→:=M→−N→.\vec{W}:=\vec{M}-\vec{N}.(150)

Then𝒩​(M→)−𝒩​(N→)\displaystyle\mathcal{N}(\vec{M})-\mathcal{N}(\vec{N})=W→×(𝒯a​[M→]+δ​B→)+N→×𝒯a​[W→].\displaystyle=\vec{W}\times\Bigl(\mathcal{T}_{a}[\vec{M}]+\delta\vec{B}\Bigr)+\vec{N}\times\mathcal{T}_{a}[\vec{W}].(151)

We estimate theH−1​(Ω)3H^{-1}(\Omega)^{3}norm through the duality withH1​(Ω)3H^{1}(\Omega)^{3}:‖F→‖H−1​(Ω)3=supv→∈H1​(Ω)3‖v→‖H1​(Ω)=1|∫ΩF→⋅v→​d3​𝐫|.\|\vec{F}\|_{H^{-1}(\Omega)^{3}}=\sup_{\begin{subarray}{c}\vec{v}\in H^{1}(\Omega)^{3}\\
\|\vec{v}\|_{H^{1}(\Omega)}=1\end{subarray}}\left|\int_{\Omega}\vec{F}\cdot\vec{v}\,\mathrm{d}^{3}\mathbf{r}\right|.(152)

Fixv→∈H1​(Ω)3\vec{v}\in H^{1}(\Omega)^{3}with‖v→‖H1​(Ω)=1\|\vec{v}\|_{H^{1}(\Omega)}=1.

We begin with the first term in (151). By the pointwise
bound|(a→×b→)⋅c→|≤|a→|​|b→|​|c→|,|(\vec{a}\times\vec{b})\cdot\vec{c}|\leq|\vec{a}|\,|\vec{b}|\,|\vec{c}|,(153)

followed by Hölder’s inequality with exponents(6,3,2)(6,3,2), we obtain|∫Ω(W→×(𝒯a​[M→]+δ​B→))⋅v→​d3​𝐫|\displaystyle\left|\int_{\Omega}\Bigl(\vec{W}\times\bigl(\mathcal{T}_{a}[\vec{M}]+\delta\vec{B}\bigr)\Bigr)\cdot\vec{v}\,\mathrm{d}^{3}\mathbf{r}\right|≤‖W→‖L6​(Ω)​(‖𝒯a​[M→]‖L3​(Ω)+‖δ​B→‖L3​(Ω))​‖v→‖L2​(Ω).\displaystyle\quad\leq\|\vec{W}\|_{L^{6}(\Omega)}\Bigl(\|\mathcal{T}_{a}[\vec{M}]\|_{L^{3}(\Omega)}+\|\delta\vec{B}\|_{L^{3}(\Omega)}\Bigr)\|\vec{v}\|_{L^{2}(\Omega)}.(154)

SinceΩ\Omegais bounded and Lipschitz,‖W→‖L6​(Ω)\displaystyle\|\vec{W}\|_{L^{6}(\Omega)}≤C​‖W→‖H1​(Ω),\displaystyle\leq C\|\vec{W}\|_{H^{1}(\Omega)},(155)‖v→‖L2​(Ω)\displaystyle\|\vec{v}\|_{L^{2}(\Omega)}≤C​‖v→‖H1​(Ω)=C.\displaystyle\leq C\|\vec{v}\|_{H^{1}(\Omega)}=C.(156)

Also, byProposition˜A.1,‖𝒯a​[M→]‖L3​(Ω)≤C​‖M→‖L3​(Ω)≤C​‖M→‖H1​(Ω),\|\mathcal{T}_{a}[\vec{M}]\|_{L^{3}(\Omega)}\leq C\|\vec{M}\|_{L^{3}(\Omega)}\leq C\|\vec{M}\|_{H^{1}(\Omega)},(157)

and sinceδ​B→∈L∞​(Ω)3\delta\vec{B}\in L^{\infty}(\Omega)^{3}andΩ\Omegais bounded,‖δ​B→‖L3​(Ω)≤|Ω|1/3​‖δ​B→‖L∞​(Ω).\|\delta\vec{B}\|_{L^{3}(\Omega)}\leq|\Omega|^{1/3}\|\delta\vec{B}\|_{L^{\infty}(\Omega)}.(158)

Substituting these bounds into (154) gives|∫Ω(W→×(𝒯a​[M→]+δ​B→))⋅v→​d3​𝐫|≤C​(‖M→‖H1​(Ω)+1)​‖W→‖H1​(Ω).\left|\int_{\Omega}\Bigl(\vec{W}\times\bigl(\mathcal{T}_{a}[\vec{M}]+\delta\vec{B}\bigr)\Bigr)\cdot\vec{v}\,\mathrm{d}^{3}\mathbf{r}\right|\\
\leq C\Bigl(\|\vec{M}\|_{H^{1}(\Omega)}+1\Bigr)\|\vec{W}\|_{H^{1}(\Omega)}.(159)

For the second term in (151), the same pointwise bound
and the same Hölder exponents give|∫Ω(N→×𝒯a​[W→])⋅v→​d3​𝐫|\displaystyle\left|\int_{\Omega}\bigl(\vec{N}\times\mathcal{T}_{a}[\vec{W}]\bigr)\cdot\vec{v}\,\mathrm{d}^{3}\mathbf{r}\right|≤‖N→‖L6​(Ω)​‖𝒯a​[W→]‖L3​(Ω)​‖v→‖L2​(Ω).\displaystyle\quad\leq\|\vec{N}\|_{L^{6}(\Omega)}\|\mathcal{T}_{a}[\vec{W}]\|_{L^{3}(\Omega)}\|\vec{v}\|_{L^{2}(\Omega)}.(160)

Using again the Sobolev embeddingH1​(Ω)↪L6​(Ω)H^{1}(\Omega)\hookrightarrow L^{6}(\Omega),
the boundedness of𝒯a\mathcal{T}_{a}onL3​(Ω)3L^{3}(\Omega)^{3}, and the embeddingH1​(Ω)↪L3​(Ω)H^{1}(\Omega)\hookrightarrow L^{3}(\Omega), we obtain‖N→‖L6​(Ω)\displaystyle\|\vec{N}\|_{L^{6}(\Omega)}≤C​‖N→‖H1​(Ω),\displaystyle\leq C\|\vec{N}\|_{H^{1}(\Omega)},(161)‖𝒯a​[W→]‖L3​(Ω)\displaystyle\|\mathcal{T}_{a}[\vec{W}]\|_{L^{3}(\Omega)}≤C​‖W→‖L3​(Ω)≤C​‖W→‖H1​(Ω),\displaystyle\leq C\|\vec{W}\|_{L^{3}(\Omega)}\leq C\|\vec{W}\|_{H^{1}(\Omega)},(162)‖v→‖L2​(Ω)\displaystyle\|\vec{v}\|_{L^{2}(\Omega)}≤C.\displaystyle\leq C.(163)

Therefore|∫Ω(N→×𝒯a​[W→])⋅v→​d3​𝐫|≤C​‖N→‖H1​(Ω)​‖W→‖H1​(Ω).\left|\int_{\Omega}\bigl(\vec{N}\times\mathcal{T}_{a}[\vec{W}]\bigr)\cdot\vec{v}\,\mathrm{d}^{3}\mathbf{r}\right|\\
\leq C\|\vec{N}\|_{H^{1}(\Omega)}\|\vec{W}\|_{H^{1}(\Omega)}.(164)

Combining (159) and (164), we find|∫Ω(𝒩​(M→)−𝒩​(N→))⋅v→​d3​𝐫|≤C​(‖M→‖H1​(Ω)+‖N→‖H1​(Ω)+1)​‖M→−N→‖H1​(Ω).\left|\int_{\Omega}\bigl(\mathcal{N}(\vec{M})-\mathcal{N}(\vec{N})\bigr)\cdot\vec{v}\,\mathrm{d}^{3}\mathbf{r}\right|\\
\leq C\Bigl(\|\vec{M}\|_{H^{1}(\Omega)}+\|\vec{N}\|_{H^{1}(\Omega)}+1\Bigr)\|\vec{M}-\vec{N}\|_{H^{1}(\Omega)}.(165)

Taking the supremum over allv→∈H1​(Ω)3\vec{v}\in H^{1}(\Omega)^{3}with‖v→‖H1​(Ω)=1\|\vec{v}\|_{H^{1}(\Omega)}=1and using
(152) proves (149).
∎

## Lemma A.7(Time continuity).

IfM→∈X\vec{M}\in X, thenM→∈C​([0,T];H)\vec{M}\in C([0,T];H).

## Proof.

Recall thatV=H1​(Ω)3,H=L2​(Ω)3,V′=H−1​(Ω)3,V=H^{1}(\Omega)^{3},\quad H=L^{2}(\Omega)^{3},\quad V^{\prime}=H^{-1}(\Omega)^{3},(166)

and thatV↪HV\hookrightarrow His continuous and dense, whileH↪V′H\hookrightarrow V^{\prime}continuously via the canonical identification ofHHwith a subspace ofV′V^{\prime}. HenceV↪H↪V′V\hookrightarrow H\hookrightarrow V^{\prime}(167)

is a Gelfand triple.

By definition,X=L2​(0,T;V)∩H1​(0,T;V′).X=L^{2}(0,T;V)\cap H^{1}(0,T;V^{\prime}).(168)

The classical Lions–Magenes continuity theorem for Hilbert triples states
thatL2​(0,T;V)∩H1​(0,T;V′)↪C​([0,T];H)L^{2}(0,T;V)\cap H^{1}(0,T;V^{\prime})\hookrightarrow C([0,T];H)(169)

continuously. Therefore everyM→∈X\vec{M}\in Xadmits anHH-continuous representative on[0,T][0,T]. In particular,M→∈C​([0,T];H).\vec{M}\in C([0,T];H).(170)

∎

## Theorem A.8(Local existence and uniqueness).

AssumeSection˜IIIand fixa>0a>0. For anyM→init∈H\vec{M}_{\mathrm{init}}\in Hthere existsT∗>0T^{\ast}>0and a unique weak
solutionM→∈X∩C​([0,T∗];H)\vec{M}\in X\cap C([0,T^{\ast}];H)(171)

on[0,T∗][0,T^{\ast}].

## Proof.

ForT>0T>0, defineXT:=L2​(0,T;V)∩H1​(0,T;V′),X_{T}:=L^{2}(0,T;V)\cap H^{1}(0,T;V^{\prime}),(172)

andYT:=XT∩C​([0,T];H),‖U→‖YT:=‖U→‖L2​(0,T;V)+‖∂tU→‖L2​(0,T;V′)+‖U→‖C​([0,T];H).Y_{T}:=X_{T}\cap C([0,T];H),\quad\|\vec{U}\|_{Y_{T}}:=\|\vec{U}\|_{L^{2}(0,T;V)}\\
+\|\partial_{t}\vec{U}\|_{L^{2}(0,T;V^{\prime})}+\|\vec{U}\|_{C([0,T];H)}.

SinceXT↪C​([0,T];H)X_{T}\hookrightarrow C([0,T];H)byLemma˜A.7, the spaceYTY_{T}is a Banach space with the above norm.

We write the weak problem in the semilinear form∂tM→+A​M→=γ​𝒩​(M→)+F→in​V′,\partial_{t}\vec{M}+A\vec{M}=\gamma\,\mathcal{N}(\vec{M})+\vec{F}\quad\text{in }V^{\prime},(173)

where𝒩​(M→)=M→×(𝒯a​[M→]+δ​B→),\mathcal{N}(\vec{M})=\vec{M}\times\bigl(\mathcal{T}_{a}[\vec{M}]+\delta\vec{B}\bigr),(174)

andF→∈V′\vec{F}\in V^{\prime}is defined by⟨F→,Φ→⟩V′,V=∫ΩM0​(𝐫)T1​(𝐫)​Φ3​d3​𝐫.\langle\vec{F},\vec{\Phi}\rangle_{V^{\prime},V}=\int_{\Omega}\frac{M_{0}(\mathbf{r})}{T_{1}(\mathbf{r})}\,\Phi_{3}\,\mathrm{d}^{3}\mathbf{r}.(175)

The linear operatorA:V→V′A:V\to V^{\prime}is induced by the bilinear forma​(U→,Φ→)\displaystyle a(\vec{U},\vec{\Phi}):=∫ΩD​(𝐫)​∇U→:∇Φ→​d3​𝐫\displaystyle:=\int_{\Omega}D(\mathbf{r})\,\nabla\vec{U}:\nabla\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}+∫Ω(U1​Φ1+U2​Φ2T2​(𝐫)+U3​Φ3T1​(𝐫))​d3​𝐫\displaystyle\quad+\int_{\Omega}\left(\frac{U_{1}\Phi_{1}+U_{2}\Phi_{2}}{T_{2}(\mathbf{r})}+\frac{U_{3}\Phi_{3}}{T_{1}(\mathbf{r})}\right)\mathrm{d}^{3}\mathbf{r}+∑i=13aadv​(Ui,Φi),\displaystyle\quad+\sum_{i=1}^{3}a_{\mathrm{adv}}(U_{i},\Phi_{i}),(176)

through⟨A​U→,Φ→⟩V′,V=a​(U→,Φ→).\langle A\vec{U},\vec{\Phi}\rangle_{V^{\prime},V}=a(\vec{U},\vec{\Phi}).(177)

By the assumptions onDD,T1T_{1},T2T_{2}, andv→\vec{v}, the formaais
bounded onV×VV\times V:|a​(U→,Φ→)|≤CA​‖U→‖V​‖Φ→‖Vfor all​U→,Φ→∈V.|a(\vec{U},\vec{\Phi})|\leq C_{A}\|\vec{U}\|_{V}\|\vec{\Phi}\|_{V}\quad\text{for all }\vec{U},\vec{\Phi}\in V.(178)

Moreover, there exist constantsαA>0\alpha_{A}>0andλA≥0\lambda_{A}\geq 0such thata​(U→,U→)+λA​‖U→‖H2≥αA​‖U→‖V2for all​U→∈V.a(\vec{U},\vec{U})+\lambda_{A}\|\vec{U}\|_{H}^{2}\geq\alpha_{A}\|\vec{U}\|_{V}^{2}\quad\text{for all }\vec{U}\in V.(179)

Indeed, the diffusion and relaxation terms are coercive, while the
advection term is either skew and contributes nothing toa​(U→,U→)a(\vec{U},\vec{U}), or else is controlled by‖v→‖W1,∞​(Ω)\|\vec{v}\|_{W^{1,\infty}(\Omega)}, the trace theorem, and the prescribed
advection boundary conditions.

FixT0>0T_{0}>0. By the Lions–Magenes theory for linear parabolic equations
associated with bounded bilinear forms satisfying
(179), for everyG→∈L2​(0,T0;V′)\vec{G}\in L^{2}(0,T_{0};V^{\prime})and everyM→init∈H\vec{M}_{\mathrm{init}}\in Hthere exists a unique solutionU→∈XT0\vec{U}\in X_{T_{0}}of∂tU→+A​U→=G→+F→,U→​(0)=M→init.\partial_{t}\vec{U}+A\vec{U}=\vec{G}+\vec{F},\quad\vec{U}(0)=\vec{M}_{\mathrm{init}}.(180)

ByLemma˜A.7, this solution belongs toYT0Y_{T_{0}}, and there exists a
constantCT0>0C_{T_{0}}>0such that‖U→‖YT0≤CT0​(‖M→init‖H+‖G→‖L2​(0,T0;V′)+‖F→‖L2​(0,T0;V′)).\|\vec{U}\|_{Y_{T_{0}}}\\
\leq C_{T_{0}}\Bigl(\|\vec{M}_{\mathrm{init}}\|_{H}+\|\vec{G}\|_{L^{2}(0,T_{0};V^{\prime})}+\|\vec{F}\|_{L^{2}(0,T_{0};V^{\prime})}\Bigr).(181)

We next estimate the nonlinear term. LetZ→∈YT\vec{Z}\in Y_{T}with0<T≤T00<T\leq T_{0}. For anyΦ→∈V\vec{\Phi}\in Vwith‖Φ→‖V=1\|\vec{\Phi}\|_{V}=1,|⟨𝒩​(Z→),Φ→⟩V′,V|\displaystyle\left|\langle\mathcal{N}(\vec{Z}),\vec{\Phi}\rangle_{V^{\prime},V}\right|=|∫Ω(Z→×(𝒯a​[Z→]+δ​B→))⋅Φ→​d3​𝐫|\displaystyle=\left|\int_{\Omega}\bigl(\vec{Z}\times(\mathcal{T}_{a}[\vec{Z}]+\delta\vec{B})\bigr)\cdot\vec{\Phi}\,\mathrm{d}^{3}\mathbf{r}\right|≤‖Z→‖L2​(Ω)​‖𝒯a​[Z→]‖L6​(Ω)​‖Φ→‖L3​(Ω)\displaystyle\leq\|\vec{Z}\|_{L^{2}(\Omega)}\|\mathcal{T}_{a}[\vec{Z}]\|_{L^{6}(\Omega)}\|\vec{\Phi}\|_{L^{3}(\Omega)}+‖δ​B→‖L∞​(Ω)​‖Z→‖L2​(Ω)​‖Φ→‖L2​(Ω).\displaystyle\quad+\|\delta\vec{B}\|_{L^{\infty}(\Omega)}\|\vec{Z}\|_{L^{2}(\Omega)}\|\vec{\Phi}\|_{L^{2}(\Omega)}.(182)

ByProposition˜A.1,𝒯a:H1​(Ω)3→H1​(Ω)3\mathcal{T}_{a}:H^{1}(\Omega)^{3}\to H^{1}(\Omega)^{3}continuously. Hence, by Sobolev embedding,‖𝒯a​[Z→]‖L6​(Ω)≤C​‖𝒯a​[Z→]‖H1​(Ω)≤C​‖Z→‖H1​(Ω).\|\mathcal{T}_{a}[\vec{Z}]\|_{L^{6}(\Omega)}\leq C\|\mathcal{T}_{a}[\vec{Z}]\|_{H^{1}(\Omega)}\leq C\|\vec{Z}\|_{H^{1}(\Omega)}.(183)

Also,‖Φ→‖L3​(Ω)+‖Φ→‖L2​(Ω)≤C​‖Φ→‖V=C.\|\vec{\Phi}\|_{L^{3}(\Omega)}+\|\vec{\Phi}\|_{L^{2}(\Omega)}\leq C\|\vec{\Phi}\|_{V}=C.(184)

Therefore‖𝒩​(Z→)‖V′≤C​(‖Z→‖H​‖Z→‖V+‖Z→‖H)for a.e.​t∈(0,T),\|\mathcal{N}(\vec{Z})\|_{V^{\prime}}\leq C\Bigl(\|\vec{Z}\|_{H}\|\vec{Z}\|_{V}+\|\vec{Z}\|_{H}\Bigr)\quad\text{for a.e. }t\in(0,T),(185)

and thus‖𝒩​(Z→)‖L2​(0,T;V′)≤C​‖Z→‖C​([0,T];H)​(‖Z→‖L2​(0,T;V)+T1/2).\|\mathcal{N}(\vec{Z})\|_{L^{2}(0,T;V^{\prime})}\\
\leq C\,\|\vec{Z}\|_{C([0,T];H)}\Bigl(\|\vec{Z}\|_{L^{2}(0,T;V)}+T^{1/2}\Bigr).(186)

Now letZ→(1),Z→(2)∈YT\vec{Z}^{(1)},\vec{Z}^{(2)}\in Y_{T}, and setW→:=Z→(1)−Z→(2).\vec{W}:=\vec{Z}^{(1)}-\vec{Z}^{(2)}.(187)

Then𝒩​(Z→(1))−𝒩​(Z→(2))=W→×(𝒯a​[Z→(1)]+δ​B→)+Z→(2)×𝒯a​[W→].\mathcal{N}(\vec{Z}^{(1)})-\mathcal{N}(\vec{Z}^{(2)})=\vec{W}\times\bigl(\mathcal{T}_{a}[\vec{Z}^{(1)}]+\delta\vec{B}\bigr)+\vec{Z}^{(2)}\times\mathcal{T}_{a}[\vec{W}].(188)

Arguing as above, for anyΦ→∈V\vec{\Phi}\in Vwith‖Φ→‖V=1\|\vec{\Phi}\|_{V}=1,|⟨𝒩​(Z→(1))−𝒩​(Z→(2)),Φ→⟩V′,V|\displaystyle\left|\langle\mathcal{N}(\vec{Z}^{(1)})-\mathcal{N}(\vec{Z}^{(2)}),\vec{\Phi}\rangle_{V^{\prime},V}\right|≤‖W→‖L2​(Ω)​‖𝒯a​[Z→(1)]‖L6​(Ω)​‖Φ→‖L3​(Ω)\displaystyle\quad\leq\|\vec{W}\|_{L^{2}(\Omega)}\|\mathcal{T}_{a}[\vec{Z}^{(1)}]\|_{L^{6}(\Omega)}\|\vec{\Phi}\|_{L^{3}(\Omega)}+‖δ​B→‖L∞​(Ω)​‖W→‖L2​(Ω)​‖Φ→‖L2​(Ω)\displaystyle\quad\quad+\|\delta\vec{B}\|_{L^{\infty}(\Omega)}\|\vec{W}\|_{L^{2}(\Omega)}\|\vec{\Phi}\|_{L^{2}(\Omega)}+‖Z→(2)‖L6​(Ω)​‖𝒯a​[W→]‖L2​(Ω)​‖Φ→‖L3​(Ω)\displaystyle\quad\quad+\|\vec{Z}^{(2)}\|_{L^{6}(\Omega)}\|\mathcal{T}_{a}[\vec{W}]\|_{L^{2}(\Omega)}\|\vec{\Phi}\|_{L^{3}(\Omega)}≤C​(1+‖Z→(1)‖V+‖Z→(2)‖V)​‖W→‖H.\displaystyle\quad\leq C\Bigl(1+\|\vec{Z}^{(1)}\|_{V}+\|\vec{Z}^{(2)}\|_{V}\Bigr)\|\vec{W}\|_{H}.(189)

Hence, for almost everyt∈(0,T)t\in(0,T),‖𝒩​(Z→(1))−𝒩​(Z→(2))‖V′≤C​(1+‖Z→(1)‖V+‖Z→(2)‖V)​‖W→‖H,\|\mathcal{N}(\vec{Z}^{(1)})-\mathcal{N}(\vec{Z}^{(2)})\|_{V^{\prime}}\leq C\Bigl(1+\|\vec{Z}^{(1)}\|_{V}+\|\vec{Z}^{(2)}\|_{V}\Bigr)\|\vec{W}\|_{H},(190)

and therefore‖𝒩​(Z→(1))−𝒩​(Z→(2))‖L2​(0,T;V′)≤C​(T1/2+‖Z→(1)‖L2​(0,T;V)+‖Z→(2)‖L2​(0,T;V))×‖Z→(1)−Z→(2)‖C​([0,T];H).\|\mathcal{N}(\vec{Z}^{(1)})-\mathcal{N}(\vec{Z}^{(2)})\|_{L^{2}(0,T;V^{\prime})}\\
\leq C\Bigl(T^{1/2}+\|\vec{Z}^{(1)}\|_{L^{2}(0,T;V)}+\|\vec{Z}^{(2)}\|_{L^{2}(0,T;V)}\Bigr)\\
\times\|\vec{Z}^{(1)}-\vec{Z}^{(2)}\|_{C([0,T];H)}.(191)

LetU→0∈YT0\vec{U}_{0}\in Y_{T_{0}}denote the unique solution of the linear problem∂tU→0+A​U→0=F→,U→0​(0)=M→init\partial_{t}\vec{U}_{0}+A\vec{U}_{0}=\vec{F},\quad\vec{U}_{0}(0)=\vec{M}_{\mathrm{init}}(192)

on[0,T0][0,T_{0}]. For0<T≤T00<T\leq T_{0}, we still denote byU→0\vec{U}_{0}its
restriction to[0,T][0,T].

Fixρ>0\rho>0and define the closed ball𝔹ρ​(T):={Z→∈YT:‖Z→−U→0‖YT≤ρ}.\mathbb{B}_{\rho}(T):=\left\{\vec{Z}\in Y_{T}:\|\vec{Z}-\vec{U}_{0}\|_{Y_{T}}\leq\rho\right\}.(193)

BecauseYTY_{T}is Banach,𝔹ρ​(T)\mathbb{B}_{\rho}(T)is complete.

ForZ→∈𝔹ρ​(T)\vec{Z}\in\mathbb{B}_{\rho}(T), defineΨ​(Z→)=U→\Psi(\vec{Z})=\vec{U}, whereU→∈YT\vec{U}\in Y_{T}is the unique solution of∂tU→+A​U→=γ​𝒩​(Z→)+F→,U→​(0)=M→init\partial_{t}\vec{U}+A\vec{U}=\gamma\,\mathcal{N}(\vec{Z})+\vec{F},\quad\vec{U}(0)=\vec{M}_{\mathrm{init}}(194)

on[0,T][0,T]. This is well defined by (180),
(181), and (186).

SetKH​(T,ρ):=\displaystyle K_{H}(T,\rho):=‖U→0‖C​([0,T];H)+ρ,\displaystyle\|\vec{U}_{0}\|_{C([0,T];H)}+\rho,KV​(T,ρ):=\displaystyle K_{V}(T,\rho):=‖U→0‖L2​(0,T;V)+ρ.\displaystyle\|\vec{U}_{0}\|_{L^{2}(0,T;V)}+\rho.(195)

IfZ→∈𝔹ρ​(T)\vec{Z}\in\mathbb{B}_{\rho}(T), then‖Z→‖C​([0,T];H)≤KH​(T,ρ),‖Z→‖L2​(0,T;V)≤KV​(T,ρ).\|\vec{Z}\|_{C([0,T];H)}\leq K_{H}(T,\rho),\quad\|\vec{Z}\|_{L^{2}(0,T;V)}\leq K_{V}(T,\rho).(196)

Subtracting (192) from (194) and
using (181) gives‖Ψ​(Z→)−U→0‖YT\displaystyle\|\Psi(\vec{Z})-\vec{U}_{0}\|_{Y_{T}}≤CT0​|γ|​‖𝒩​(Z→)‖L2​(0,T;V′)\displaystyle\leq C_{T_{0}}|\gamma|\,\|\mathcal{N}(\vec{Z})\|_{L^{2}(0,T;V^{\prime})}≤CT0​|γ|​KH​(T,ρ)​(KV​(T,ρ)+T1/2).\displaystyle\leq C_{T_{0}}|\gamma|\,K_{H}(T,\rho)\Bigl(K_{V}(T,\rho)+T^{1/2}\Bigr).(197)

Likewise, ifZ→(1),Z→(2)∈𝔹ρ​(T)\vec{Z}^{(1)},\vec{Z}^{(2)}\in\mathbb{B}_{\rho}(T), then∥Ψ(Z→(1))\displaystyle\|\Psi(\vec{Z}^{(1)})−Ψ​(Z→(2))∥YT\displaystyle-\Psi(\vec{Z}^{(2)})\|_{Y_{T}}(198)≤CT0​|γ|​‖𝒩​(Z→(1))−𝒩​(Z→(2))‖L2​(0,T;V′)\displaystyle\leq C_{T_{0}}|\gamma|\,\|\mathcal{N}(\vec{Z}^{(1)})-\mathcal{N}(\vec{Z}^{(2)})\|_{L^{2}(0,T;V^{\prime})}≤CT0​|γ|​(T1/2+2​KV​(T,ρ))\displaystyle\leq C_{T_{0}}|\gamma|\Bigl(T^{1/2}+2K_{V}(T,\rho)\Bigr)×‖Z→(1)−Z→(2)‖C​([0,T];H)\displaystyle\quad\times\|\vec{Z}^{(1)}-\vec{Z}^{(2)}\|_{C([0,T];H)}≤CT0​|γ|​(T1/2+2​KV​(T,ρ))​‖Z→(1)−Z→(2)‖YT.\displaystyle\leq C_{T_{0}}|\gamma|\Bigl(T^{1/2}+2K_{V}(T,\rho)\Bigr)\|\vec{Z}^{(1)}-\vec{Z}^{(2)}\|_{Y_{T}}.(199)

SinceU→0∈C​([0,T0];H)∩L2​(0,T0;V)\vec{U}_{0}\in C([0,T_{0}];H)\cap L^{2}(0,T_{0};V), we have‖U→0‖C​([0,T];H)≤‖U→0‖C​([0,T0];H),‖U→0‖L2​(0,T;V)→0\|\vec{U}_{0}\|_{C([0,T];H)}\leq\|\vec{U}_{0}\|_{C([0,T_{0}];H)},\quad\|\vec{U}_{0}\|_{L^{2}(0,T;V)}\to 0(200)

asT↓0T\downarrow 0. Therefore, for fixedρ>0\rho>0, we may chooseT∗∈(0,T0]T^{\ast}\in(0,T_{0}]so small
thatCT0​|γ|​KH​(T∗,ρ)​(KV​(T∗,ρ)+(T∗)1/2)≤ρC_{T_{0}}|\gamma|\,K_{H}(T^{\ast},\rho)\Bigl(K_{V}(T^{\ast},\rho)+(T^{\ast})^{1/2}\Bigr)\leq\rho(201)

andCT0​|γ|​((T∗)1/2+2​KV​(T∗,ρ))<1.C_{T_{0}}|\gamma|\Bigl((T^{\ast})^{1/2}+2K_{V}(T^{\ast},\rho)\Bigr)<1.(202)

Then (197) shows thatΨ:𝔹ρ​(T∗)→𝔹ρ​(T∗)\Psi:\mathbb{B}_{\rho}(T^{\ast})\to\mathbb{B}_{\rho}(T^{\ast}), and
(199) together with
(202) shows thatΨ\Psiis a contraction on𝔹ρ​(T∗)\mathbb{B}_{\rho}(T^{\ast})with respect to theYT∗Y_{T^{\ast}}norm.

By Banach’s fixed-point theorem, there exists a uniqueM→∈𝔹ρ​(T∗)\vec{M}\in\mathbb{B}_{\rho}(T^{\ast})such thatΨ​(M→)=M→.\Psi(\vec{M})=\vec{M}.(203)

By construction,M→∈YT∗=XT∗∩C​([0,T∗];H),\vec{M}\in Y_{T^{\ast}}=X_{T^{\ast}}\cap C([0,T^{\ast}];H),(204)

and (194) shows thatM→\vec{M}satisfies the weak
formulation (12) on[0,T∗][0,T^{\ast}]with initial conditionM→​(0)=M→init.\vec{M}(0)=\vec{M}_{\mathrm{init}}.(205)

Thus a weak solution exists on[0,T∗][0,T^{\ast}].

Finally, uniqueness among weak solutions on[0,T∗][0,T^{\ast}]follows fromProposition˜A.3: if two weak solutions have the same initial datum,
then their difference vanishes identically on[0,T∗][0,T^{\ast}].
∎

## A.2Semi-discrete FE results

This subsection collects the discrete lemmas and theorem used in the FE energy analysis.

## Lemma A.9(Discrete skew-symmetry of precession).

For any coefficient vectorw=(w1,w2,w3)∈(ℝNh)3,w=(w_{1},w_{2},w_{3})\in(\mathbb{R}^{N_{h}})^{3},(206)

the discrete precession load vectors satisfy∑i=13wi⊤​𝒫i​(w)=0.\sum_{i=1}^{3}w_{i}^{\top}\mathcal{P}_{i}(w)=0.(207)

## Proof.

Let{φn}n=1Nh\{\varphi_{n}\}_{n=1}^{N_{h}}be the FE basis onΩ\Omega.
Fori∈{1,2,3}i\in\{1,2,3\}, writewi=((wi)1,…,(wi)Nh)⊤∈ℝNh,w_{i}=((w_{i})_{1},\dots,(w_{i})_{N_{h}})^{\top}\in\mathbb{R}^{N_{h}},(208)

and define the discrete magnetization fieldM→h​(𝐫)=∑i=13∑n=1Nh(wi)n​φn​(𝐫)​𝐞^i.\vec{M}_{h}(\mathbf{r})=\sum_{i=1}^{3}\sum_{n=1}^{N_{h}}(w_{i})_{n}\,\varphi_{n}(\mathbf{r})\,\hat{\mathbf{e}}_{i}.(209)

Equivalently, if we setMh,i​(𝐫):=∑n=1Nh(wi)n​φn​(𝐫),i=1,2,3,M_{h,i}(\mathbf{r}):=\sum_{n=1}^{N_{h}}(w_{i})_{n}\,\varphi_{n}(\mathbf{r}),\quad i=1,2,3,(210)

thenM→h​(𝐫)=∑i=13Mh,i​(𝐫)​𝐞^i.\vec{M}_{h}(\mathbf{r})=\sum_{i=1}^{3}M_{h,i}(\mathbf{r})\,\hat{\mathbf{e}}_{i}.(211)

Let{𝐫q}q=1Nq⊂Ω\{\mathbf{r}_{q}\}_{q=1}^{N_{q}}\subset\Omegabe the quadrature points and{ωq}q=1Nq\{\omega_{q}\}_{q=1}^{N_{q}}the associated quadrature weights used in the
matrix-free definition (23). For each quadrature point,
letB→h​(𝐫q)\vec{B}_{h}(\mathbf{r}_{q})denote the discrete DDF field obtained from the
same coefficient vectorwwby the same discrete kernel evaluation used in
(23).

By the definition of𝒫i​(w)\mathcal{P}_{i}(w), for each basis indexm∈{1,…,Nh}m\in\{1,\dots,N_{h}\},(𝒫i​(w))m=∑q=1Nqωq​(M→h​(𝐫q)×B→h​(𝐫q))⋅𝐞^i​φm​(𝐫q).(\mathcal{P}_{i}(w))_{m}=\sum_{q=1}^{N_{q}}\omega_{q}\,\bigl(\vec{M}_{h}(\mathbf{r}_{q})\times\vec{B}_{h}(\mathbf{r}_{q})\bigr)\cdot\hat{\mathbf{e}}_{i}\,\varphi_{m}(\mathbf{r}_{q}).(212)

Therefore,wi⊤​𝒫i​(w)\displaystyle w_{i}^{\top}\mathcal{P}_{i}(w)=∑m=1Nh(wi)m​(𝒫i​(w))m\displaystyle=\sum_{m=1}^{N_{h}}(w_{i})_{m}\,(\mathcal{P}_{i}(w))_{m}=∑m=1Nh(wi)m​∑q=1Nqωq​(M→h​(𝐫q)×B→h​(𝐫q))⋅𝐞^i​φm​(𝐫q)\displaystyle=\sum_{m=1}^{N_{h}}(w_{i})_{m}\sum_{q=1}^{N_{q}}\omega_{q}\,\bigl(\vec{M}_{h}(\mathbf{r}_{q})\times\vec{B}_{h}(\mathbf{r}_{q})\bigr)\cdot\hat{\mathbf{e}}_{i}\,\varphi_{m}(\mathbf{r}_{q})=∑q=1Nqωq​(M→h​(𝐫q)×B→h​(𝐫q))⋅𝐞^i​∑m=1Nh(wi)m​φm​(𝐫q)\displaystyle=\sum_{q=1}^{N_{q}}\omega_{q}\,\bigl(\vec{M}_{h}(\mathbf{r}_{q})\times\vec{B}_{h}(\mathbf{r}_{q})\bigr)\cdot\hat{\mathbf{e}}_{i}\,\sum_{m=1}^{N_{h}}(w_{i})_{m}\,\varphi_{m}(\mathbf{r}_{q})=∑q=1Nqωq​(M→h​(𝐫q)×B→h​(𝐫q))⋅𝐞^i​Mh,i​(𝐫q).\displaystyle=\sum_{q=1}^{N_{q}}\omega_{q}\,\bigl(\vec{M}_{h}(\mathbf{r}_{q})\times\vec{B}_{h}(\mathbf{r}_{q})\bigr)\cdot\hat{\mathbf{e}}_{i}\,M_{h,i}(\mathbf{r}_{q}).(213)

Summing overi=1,2,3i=1,2,3gives∑i=13wi⊤​𝒫i​(w)\displaystyle\sum_{i=1}^{3}w_{i}^{\top}\mathcal{P}_{i}(w)=∑q=1Nqωq​∑i=13(M→h​(𝐫q)×B→h​(𝐫q))⋅𝐞^i​Mh,i​(𝐫q)\displaystyle=\sum_{q=1}^{N_{q}}\omega_{q}\sum_{i=1}^{3}\bigl(\vec{M}_{h}(\mathbf{r}_{q})\times\vec{B}_{h}(\mathbf{r}_{q})\bigr)\cdot\hat{\mathbf{e}}_{i}\,M_{h,i}(\mathbf{r}_{q})=∑q=1Nqωq​M→h​(𝐫q)⋅(M→h​(𝐫q)×B→h​(𝐫q)).\displaystyle=\sum_{q=1}^{N_{q}}\omega_{q}\,\vec{M}_{h}(\mathbf{r}_{q})\cdot\bigl(\vec{M}_{h}(\mathbf{r}_{q})\times\vec{B}_{h}(\mathbf{r}_{q})\bigr).(214)

For each quadrature point𝐫q\mathbf{r}_{q}, the scalar triple product vanishes:M→h​(𝐫q)⋅(M→h​(𝐫q)×B→h​(𝐫q))=0,\vec{M}_{h}(\mathbf{r}_{q})\cdot\bigl(\vec{M}_{h}(\mathbf{r}_{q})\times\vec{B}_{h}(\mathbf{r}_{q})\bigr)=0,(215)

becausea→⋅(a→×b→)=0for all​a→,b→∈ℝ3.\vec{a}\cdot(\vec{a}\times\vec{b})=0\quad\text{for all }\vec{a},\vec{b}\in\mathbb{R}^{3}.(216)

Hence every summand in (214) is zero, and therefore∑i=13wi⊤​𝒫i​(w)=0.\sum_{i=1}^{3}w_{i}^{\top}\mathcal{P}_{i}(w)=0.(217)

This proves (207).
∎

## Lemma A.10(SPD and positivity).

The mass matrixM∈ℝNh×NhM\in\mathbb{R}^{N_{h}\times N_{h}}is symmetric positive
definite. IfD​(𝐫)≥Dmin>0D(\mathbf{r})\geq D_{\min}>0almost everywhere, thenK∈ℝNh×NhK\in\mathbb{R}^{N_{h}\times N_{h}}is symmetric positive semidefinite and, for
everyw∈ℝNhw\in\mathbb{R}^{N_{h}},w⊤​K​w=∫ΩD​(𝐫)​|∇uh|2​d3​𝐫≥Dmin​∫Ω|∇uh|2​d3​𝐫,uh=∑n=1Nhwn​φn.w^{\top}Kw=\int_{\Omega}D(\mathbf{r})\,|\nabla u_{h}|^{2}\,\mathrm{d}^{3}\mathbf{r}\\
\geq D_{\min}\int_{\Omega}|\nabla u_{h}|^{2}\,\mathrm{d}^{3}\mathbf{r},\quad u_{h}=\sum_{n=1}^{N_{h}}w_{n}\varphi_{n}.(218)

The relaxation matricesS1,S2∈ℝNh×NhS_{1},S_{2}\in\mathbb{R}^{N_{h}\times N_{h}}are symmetric
positive semidefinite and satisfyw1⊤​S2​w1+w2⊤​S2​w2+w3⊤​S1​w3≥0w_{1}^{\top}S_{2}w_{1}+w_{2}^{\top}S_{2}w_{2}+w_{3}^{\top}S_{1}w_{3}\geq 0(219)

for allw1,w2,w3∈ℝNhw_{1},w_{2},w_{3}\in\mathbb{R}^{N_{h}}. If
(31) holds andNv=NvskewN_{v}=N_{v}^{\mathrm{skew}}, thenw⊤​Nv​w=0for all​w∈ℝNh.w^{\top}N_{v}w=0\quad\text{for all }w\in\mathbb{R}^{N_{h}}.(220)

## Proof.

We begin with the mass matrix. By definition,Mm​n=∫Ωφn​(𝐫)​φm​(𝐫)​d3​𝐫,1≤m,n≤Nh,M_{mn}=\int_{\Omega}\varphi_{n}(\mathbf{r})\,\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r},\quad 1\leq m,n\leq N_{h},(221)

soMMis symmetric. Letw∈ℝNhw\in\mathbb{R}^{N_{h}}and defineuh=∑n=1Nhwn​φn.u_{h}=\sum_{n=1}^{N_{h}}w_{n}\varphi_{n}.(222)

Thenw⊤​M​w\displaystyle w^{\top}Mw=∑m,n=1Nhwm​wn​∫Ωφn​φm​d3​𝐫\displaystyle=\sum_{m,n=1}^{N_{h}}w_{m}w_{n}\int_{\Omega}\varphi_{n}\varphi_{m}\,\mathrm{d}^{3}\mathbf{r}=∫Ω(∑n=1Nhwn​φn)​(∑m=1Nhwm​φm)​d3​𝐫\displaystyle=\int_{\Omega}\left(\sum_{n=1}^{N_{h}}w_{n}\varphi_{n}\right)\left(\sum_{m=1}^{N_{h}}w_{m}\varphi_{m}\right)\mathrm{d}^{3}\mathbf{r}=∫Ωuh​(𝐫)2​d3​𝐫.\displaystyle=\int_{\Omega}u_{h}(\mathbf{r})^{2}\,\mathrm{d}^{3}\mathbf{r}.(223)

Hencew⊤​M​w≥0w^{\top}Mw\geq 0. Ifw⊤​M​w=0w^{\top}Mw=0, thenuh=0u_{h}=0almost everywhere inΩ\Omega. Sinceuhu_{h}is continuous and belongs to the FE space spanned by the linearly independent basis{φn}n=1Nh\{\varphi_{n}\}_{n=1}^{N_{h}}, this impliesuh≡0u_{h}\equiv 0and thereforew=0w=0. ThusMMis positive definite.

Next consider the diffusion matrixKm​n=∫ΩD​(𝐫)​∇φn​(𝐫)⋅∇φm​(𝐫)​d3​𝐫.K_{mn}=\int_{\Omega}D(\mathbf{r})\,\nabla\varphi_{n}(\mathbf{r})\cdot\nabla\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r}.(224)

Symmetry is immediate. Forw∈ℝNhw\in\mathbb{R}^{N_{h}}and the associated fielduh=∑nwn​φnu_{h}=\sum_{n}w_{n}\varphi_{n},w⊤​K​w\displaystyle w^{\top}Kw=∑m,n=1Nhwm​wn​∫ΩD​(𝐫)​∇φn⋅∇φm​d3​𝐫\displaystyle=\sum_{m,n=1}^{N_{h}}w_{m}w_{n}\int_{\Omega}D(\mathbf{r})\,\nabla\varphi_{n}\cdot\nabla\varphi_{m}\,\mathrm{d}^{3}\mathbf{r}=∫ΩD​(𝐫)​|∑n=1Nhwn​∇φn|2​d3​𝐫\displaystyle=\int_{\Omega}D(\mathbf{r})\,\left|\sum_{n=1}^{N_{h}}w_{n}\nabla\varphi_{n}\right|^{2}\mathrm{d}^{3}\mathbf{r}=∫ΩD​(𝐫)​|∇uh|2​d3​𝐫.\displaystyle=\int_{\Omega}D(\mathbf{r})\,|\nabla u_{h}|^{2}\,\mathrm{d}^{3}\mathbf{r}.(225)

SinceD​(𝐫)≥0D(\mathbf{r})\geq 0almost everywhere, this shows thatKKis
positive semidefinite. If in additionD​(𝐫)≥Dmin>0D(\mathbf{r})\geq D_{\min}>0almost
everywhere, thenw⊤​K​w≥Dmin​∫Ω|∇uh|2​d3​𝐫.w^{\top}Kw\geq D_{\min}\int_{\Omega}|\nabla u_{h}|^{2}\,\mathrm{d}^{3}\mathbf{r}.(226)

For the relaxation matrices,(S1)m​n\displaystyle(S_{1})_{mn}=∫ΩT1​(𝐫)−1​φn​(𝐫)​φm​(𝐫)​d3​𝐫,\displaystyle=\int_{\Omega}T_{1}(\mathbf{r})^{-1}\,\varphi_{n}(\mathbf{r})\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r},(S2)m​n\displaystyle(S_{2})_{mn}=∫ΩT2​(𝐫)−1​φn​(𝐫)​φm​(𝐫)​d3​𝐫.\displaystyle=\int_{\Omega}T_{2}(\mathbf{r})^{-1}\,\varphi_{n}(\mathbf{r})\varphi_{m}(\mathbf{r})\,\mathrm{d}^{3}\mathbf{r}.

These matrices are symmetric. Letz∈ℝNhz\in\mathbb{R}^{N_{h}}and definezh=∑n=1Nhzn​φnz_{h}=\sum_{n=1}^{N_{h}}z_{n}\varphi_{n}. Thenz⊤​S1​z\displaystyle z^{\top}S_{1}z=∫ΩT1​(𝐫)−1​zh​(𝐫)2​d3​𝐫,\displaystyle=\int_{\Omega}T_{1}(\mathbf{r})^{-1}\,z_{h}(\mathbf{r})^{2}\,\mathrm{d}^{3}\mathbf{r},z⊤​S2​z\displaystyle z^{\top}S_{2}z=∫ΩT2​(𝐫)−1​zh​(𝐫)2​d3​𝐫.\displaystyle=\int_{\Omega}T_{2}(\mathbf{r})^{-1}\,z_{h}(\mathbf{r})^{2}\,\mathrm{d}^{3}\mathbf{r}.

Under the standing assumptions,T1−1,T2−1≥0T_{1}^{-1},T_{2}^{-1}\geq 0almost
everywhere, and thereforeS1S_{1}andS2S_{2}are positive semidefinite.
Applying these identities tow1,w2,w3∈ℝNhw_{1},w_{2},w_{3}\in\mathbb{R}^{N_{h}}givesw1⊤​S2​w1+w2⊤​S2​w2+w3⊤​S1​w3=∫ΩT2​(𝐫)−1​((w1)h2+(w2)h2)​d3​𝐫+∫ΩT1​(𝐫)−1​(w3)h2​d3​𝐫≥0.w_{1}^{\top}S_{2}w_{1}+w_{2}^{\top}S_{2}w_{2}+w_{3}^{\top}S_{1}w_{3}\\
=\int_{\Omega}T_{2}(\mathbf{r})^{-1}\bigl((w_{1})_{h}^{2}+(w_{2})_{h}^{2}\bigr)\,\mathrm{d}^{3}\mathbf{r}\\
+\int_{\Omega}T_{1}(\mathbf{r})^{-1}(w_{3})_{h}^{2}\,\mathrm{d}^{3}\mathbf{r}\geq 0.(227)

Finally, assume (31) holds andNv=NvskewN_{v}=N_{v}^{\mathrm{skew}}. By definition of the skew discretization,(Nvskew)m​n=−12​∫Ω(v→⋅∇φn)​φm​d3​𝐫+12​∫Ω(v→⋅∇φm)​φn​d3​𝐫.(N_{v}^{\mathrm{skew}})_{mn}=-\frac{1}{2}\int_{\Omega}(\vec{v}\cdot\nabla\varphi_{n})\,\varphi_{m}\,\mathrm{d}^{3}\mathbf{r}+\frac{1}{2}\int_{\Omega}(\vec{v}\cdot\nabla\varphi_{m})\,\varphi_{n}\,\mathrm{d}^{3}\mathbf{r}.(228)

Interchangingmmandnnin (228) yields(Nvskew)n​m=−(Nvskew)m​n,(N_{v}^{\mathrm{skew}})_{nm}=-(N_{v}^{\mathrm{skew}})_{mn},(229)

soNvskewN_{v}^{\mathrm{skew}}is skew-symmetric. Therefore, for everyw∈ℝNhw\in\mathbb{R}^{N_{h}},w⊤​Nv​w=w⊤​Nvskew​w=(w⊤​Nvskew​w)⊤=w⊤​(Nvskew)⊤​w=−w⊤​Nvskew​w,w^{\top}N_{v}w=w^{\top}N_{v}^{\mathrm{skew}}w=\bigl(w^{\top}N_{v}^{\mathrm{skew}}w\bigr)^{\top}\\
=w^{\top}(N_{v}^{\mathrm{skew}})^{\top}w=-\,w^{\top}N_{v}^{\mathrm{skew}}w,(230)

and hencew⊤​Nv​w=0.w^{\top}N_{v}w=0.(231)

This completes the proof.
∎

## Theorem A.11(Semi-discrete energy inequality).

Assume eitherv→≡0\vec{v}\equiv 0or (31) holds
and advection is discretized by the skew operatorNvskewN_{v}^{\mathrm{skew}}so thatz⊤​Nvskew​z=0for all​z∈ℝNh.z^{\top}N_{v}^{\mathrm{skew}}z=0\quad\text{for all }z\in\mathbb{R}^{N_{h}}.(232)

Then any solution of (22) satisfiesdd​t​12​∑i=13wi⊤​M​wi+∑i=13wi⊤​K​wi+w1⊤​S2​w1+w2⊤​S2​w2+w3⊤​S1​w3=w3⊤​bT1.\frac{\mathrm{d}}{\mathrm{d}t}\,\frac{1}{2}\sum_{i=1}^{3}w_{i}^{\top}M\,w_{i}+\sum_{i=1}^{3}w_{i}^{\top}K\,w_{i}\\
+w_{1}^{\top}S_{2}w_{1}+w_{2}^{\top}S_{2}w_{2}+w_{3}^{\top}S_{1}w_{3}=w_{3}^{\top}b_{T_{1}}.(233)

Consequently, for allt≥0t\geq 0,12​∑i=13wi​(t)⊤​M​wi​(t)+∫0t∑i=13wi​(s)⊤​K​wi​(s)​d​s+∫0t(w1​(s)⊤​S2​w1​(s)+w2​(s)⊤​S2​w2​(s)+w3​(s)⊤​S1​w3​(s))​ds≤12​∑i=13wi​(0)⊤​M​wi​(0)+∫0tw3​(s)⊤​bT1​ds.\frac{1}{2}\sum_{i=1}^{3}w_{i}(t)^{\top}M\,w_{i}(t)+\int_{0}^{t}\sum_{i=1}^{3}w_{i}(s)^{\top}K\,w_{i}(s)\,\mathrm{d}s\\
+\int_{0}^{t}\Bigl(w_{1}(s)^{\top}S_{2}w_{1}(s)+w_{2}(s)^{\top}S_{2}w_{2}(s)+w_{3}(s)^{\top}S_{1}w_{3}(s)\Bigr)\,\mathrm{d}s\\
\leq\frac{1}{2}\sum_{i=1}^{3}w_{i}(0)^{\top}M\,w_{i}(0)+\int_{0}^{t}w_{3}(s)^{\top}b_{T_{1}}\,\mathrm{d}s.(234)

## Proof.

LetEh​(t):=12​∑i=13wi​(t)⊤​M​wi​(t).E_{h}(t):=\frac{1}{2}\sum_{i=1}^{3}w_{i}(t)^{\top}M\,w_{i}(t).(235)

Since the semi-discrete system (22) is a finite-
dimensional ODE system, any solution is differentiable in time. Because the
mass matrixMMis constant and symmetric, we havedd​t​Eh​(t)=∑i=13wi⊤​M​w˙i.\frac{\mathrm{d}}{\mathrm{d}t}E_{h}(t)=\sum_{i=1}^{3}w_{i}^{\top}M\,\dot{w}_{i}.(236)

Write the three component equations in (22) asM​w˙1\displaystyle M\,\dot{w}_{1}=γ​𝒫1​(w)−K​w1−S2​w1−Nvskew​w1,\displaystyle=\gamma\,\mathcal{P}_{1}(w)-K\,w_{1}-S_{2}\,w_{1}-N_{v}^{\mathrm{skew}}\,w_{1},(237)M​w˙2\displaystyle M\,\dot{w}_{2}=γ​𝒫2​(w)−K​w2−S2​w2−Nvskew​w2,\displaystyle=\gamma\,\mathcal{P}_{2}(w)-K\,w_{2}-S_{2}\,w_{2}-N_{v}^{\mathrm{skew}}\,w_{2},(238)M​w˙3\displaystyle M\,\dot{w}_{3}=γ​𝒫3​(w)−K​w3−S1​w3−Nvskew​w3+bT1.\displaystyle=\gamma\,\mathcal{P}_{3}(w)-K\,w_{3}-S_{1}\,w_{3}-N_{v}^{\mathrm{skew}}\,w_{3}+b_{T_{1}}.(239)

Multiply theiith equation on the left bywi⊤w_{i}^{\top}and sum overi=1,2,3i=1,2,3. Using (236), we obtaindd​t​Eh​(t)\displaystyle\frac{\mathrm{d}}{\mathrm{d}t}E_{h}(t)=γ​∑i=13wi⊤​𝒫i​(w)−∑i=13wi⊤​K​wi\displaystyle=\gamma\sum_{i=1}^{3}w_{i}^{\top}\mathcal{P}_{i}(w)-\sum_{i=1}^{3}w_{i}^{\top}K\,w_{i}−w1⊤​S2​w1−w2⊤​S2​w2−w3⊤​S1​w3\displaystyle\quad-w_{1}^{\top}S_{2}w_{1}-w_{2}^{\top}S_{2}w_{2}-w_{3}^{\top}S_{1}w_{3}−∑i=13wi⊤​Nvskew​wi+w3⊤​bT1.\displaystyle\quad-\sum_{i=1}^{3}w_{i}^{\top}N_{v}^{\mathrm{skew}}\,w_{i}+w_{3}^{\top}b_{T_{1}}.(240)

We now evaluate the terms on the right-hand side.

First, byLemma˜A.9,∑i=13wi⊤​𝒫i​(w)=0.\sum_{i=1}^{3}w_{i}^{\top}\mathcal{P}_{i}(w)=0.(241)

Second, byLemma˜A.10, the stiffness matrixKKis symmetric positive
semidefinite, sowi⊤​K​wi≥0for​i=1,2,3.w_{i}^{\top}K\,w_{i}\geq 0\quad\text{for }i=1,2,3.(242)

Likewise,Lemma˜A.10givesw1⊤​S2​w1+w2⊤​S2​w2+w3⊤​S1​w3≥0.w_{1}^{\top}S_{2}w_{1}+w_{2}^{\top}S_{2}w_{2}+w_{3}^{\top}S_{1}w_{3}\geq 0.(243)

Third, by the skew-advection assumption,wi⊤​Nvskew​wi=0for​i=1,2,3,w_{i}^{\top}N_{v}^{\mathrm{skew}}\,w_{i}=0\quad\text{for }i=1,2,3,(244)

and hence∑i=13wi⊤​Nvskew​wi=0.\sum_{i=1}^{3}w_{i}^{\top}N_{v}^{\mathrm{skew}}\,w_{i}=0.(245)

Substituting (241) and
(244) into (240) yieldsdd​t​Eh​(t)+∑i=13wi⊤​K​wi+w1⊤​S2​w1+w2⊤​S2​w2+w3⊤​S1​w3=w3⊤​bT1,\frac{\mathrm{d}}{\mathrm{d}t}E_{h}(t)+\sum_{i=1}^{3}w_{i}^{\top}K\,w_{i}\\
+w_{1}^{\top}S_{2}w_{1}+w_{2}^{\top}S_{2}w_{2}+w_{3}^{\top}S_{1}w_{3}=w_{3}^{\top}b_{T_{1}},(246)

which is exactly (233).

Integrating (233) from0tottgives the
stronger identityEh​(t)−Eh​(0)+∫0t∑i=13wi​(s)⊤​K​wi​(s)​d​s+∫0t(w1​(s)⊤​S2​w1​(s)+w2​(s)⊤​S2​w2​(s)+w3​(s)⊤​S1​w3​(s))​ds=∫0tw3​(s)⊤​bT1​ds.E_{h}(t)-E_{h}(0)+\int_{0}^{t}\sum_{i=1}^{3}w_{i}(s)^{\top}K\,w_{i}(s)\,\mathrm{d}s\\
+\int_{0}^{t}\Bigl(w_{1}(s)^{\top}S_{2}w_{1}(s)+w_{2}(s)^{\top}S_{2}w_{2}(s)+w_{3}(s)^{\top}S_{1}w_{3}(s)\Bigr)\,\mathrm{d}s\\
=\int_{0}^{t}w_{3}(s)^{\top}b_{T_{1}}\,\mathrm{d}s.(247)

Rearranging (247) yields
(234). In fact, the integrated identity is
stronger than the stated inequality.
∎

## A.3Time-discretization results

This subsection collects the IMEX stability and consistency results used in the time-discretization analysis.

## Proposition A.12(Consistency and convergence).

Assume that the exact solution satisfiesM→∈C3​([0,T];L2​(Ω)3)∩C2​([0,T];Hp+1​(Ω)3),\vec{M}\in C^{3}([0,T];L^{2}(\Omega)^{3})\cap C^{2}([0,T];H^{p+1}(\Omega)^{3}),(248)

and that the usual elliptic regularity required for optimalL2L^{2}finite-
element error estimates holds onΩ\Omega. Assume further that the
matrix-free or quadrature-based DDF evaluation is spatially consistent with
the regularized operator𝒯a\mathcal{T}_{a}at the same order as the finite-
element space, and that the explicit Rodrigues–projection stage
(28)–(29) is a second-order
realization of the midpoint explicit flow, in the sense that its one-step
local defect isO​(Δ​t3)O(\Delta t^{3})uniformly on boundedMM-balls.

Then the IMEX scheme has local truncation errorO​(Δ​t3)O(\Delta t^{3}). Moreover,
its global time-discretization error relative to the semi-discrete FE
solution isO​(Δ​t2)O(\Delta t^{2})on[0,T][0,T]in the discreteL2​(Ω)3L^{2}(\Omega)^{3}norm.

Moreover, letM→h​(t)\vec{M}_{h}(t)denote the conforming semi-discretePpP_{p}FE
solution with initial data chosen by the standard elliptic projection ofM→​(⋅,0)\vec{M}(\cdot,0). Then, under the above regularity assumptions,‖M→h−M→‖L2​(0,T;H1​(Ω))\displaystyle\|\vec{M}_{h}-\vec{M}\|_{L^{2}(0,T;H^{1}(\Omega))}≤C​hp,\displaystyle\leq Ch^{p},(249)sup0≤t≤T‖M→h​(⋅,t)−M→​(⋅,t)‖L2​(Ω)\displaystyle\sup_{0\leq t\leq T}\|\vec{M}_{h}(\cdot,t)-\vec{M}(\cdot,t)\|_{L^{2}(\Omega)}≤C​hp+1.\displaystyle\leq Ch^{p+1}.(250)

Consequently, ifM→hn\vec{M}_{h}^{n}denotes the fully discrete IMEX solution attn=n​Δ​tt^{n}=n\Delta t, then‖M→hn−M→​(⋅,tn)‖L2​(Ω)≤C​(Δ​t2+hp+1),0≤tn≤T.\|\vec{M}_{h}^{n}-\vec{M}(\cdot,t^{n})\|_{L^{2}(\Omega)}\leq C\bigl(\Delta t^{2}+h^{p+1}\bigr),\quad 0\leq t^{n}\leq T.(251)

HereCCis independent ofhh,Δ​t\Delta t, andnn, provided the
assumptions ofTheorem˜A.13hold.

## Proof.

We divide the argument into three parts.

First, we establish the temporal consistency of the IMEX scheme for the
fixed semi-discrete system. Letwh​(t)∈(ℝNh)3w_{h}(t)\in(\mathbb{R}^{N_{h}})^{3}(252)

denote the coefficient vector of the semi-discrete FE solution. Thenwhw_{h}satisfies the autonomous ODEℳ​w˙h=−(𝒦+𝒮)​wh+f+ℛh​(wh),\mathcal{M}\dot{w}_{h}=-(\mathcal{K}+\mathcal{S})w_{h}+f+\mathcal{R}_{h}(w_{h}),(253)

whereℛh​(w)\mathcal{R}_{h}(w)denotes the discrete precession load, together with
any explicitly treated transport contribution if present. Because𝒯a:H1​(Ω)3→H1​(Ω)3\mathcal{T}_{a}:H^{1}(\Omega)^{3}\to H^{1}(\Omega)^{3}is bounded byProposition˜A.1, and becauseVh3V_{h}^{3}is finite dimensional, the mapw↦ℛh​(w)w\mapsto\mathcal{R}_{h}(w)(254)

isC2C^{2}on every bounded subset of(ℝNh)3(\mathbb{R}^{N_{h}})^{3}. Hence the
semi-discrete flow isC3C^{3}in time on[0,T][0,T]under the stated regularity
assumptions.

Write the right-hand side of (253) as the
sum of an implicit linear part and an explicit nonlinear part:FI,h​(w)\displaystyle F_{I,h}(w)=−ℳ−1​(𝒦+𝒮)​w+ℳ−1​f,\displaystyle=-\mathcal{M}^{-1}(\mathcal{K}+\mathcal{S})w+\mathcal{M}^{-1}f,(255)FE,h​(w)\displaystyle F_{E,h}(w)=ℳ−1​ℛh​(w).\displaystyle=\mathcal{M}^{-1}\mathcal{R}_{h}(w).(256)

LetΦI,hτ\Phi_{I,h}^{\tau}denote the exact flow of the linear systemw˙=FI,h​(w)\dot{w}=F_{I,h}(w)andΦE,hτ\Phi_{E,h}^{\tau}the exact flow ofw˙=FE,h​(w)\dot{w}=F_{E,h}(w). The Crank–Nicolson half-step
(27) is a second-order approximation ofΦI,hΔ​t/2\Phi_{I,h}^{\Delta t/2}, and likewise
(30) is a second-order approximation of the
second half-step. More precisely, for every bounded set in coefficient
space,‖ℐΔ​t/2​(w)−ΦI,hΔ​t/2​(w)‖M≤C​Δ​t3,\bigl\|\mathcal{I}_{\Delta t/2}(w)-\Phi_{I,h}^{\Delta t/2}(w)\bigr\|_{M}\leq C\Delta t^{3},(257)

whereℐΔ​t/2\mathcal{I}_{\Delta t/2}denotes one Crank–Nicolson half-step.

By hypothesis, the explicit Rodrigues–projection stage
(28)–(29) is a second-order
realization of the midpoint explicit flow. Therefore its one-step mapℰΔ​t\mathcal{E}_{\Delta t}satisfies‖ℰΔ​t​(w)−ΦE,hΔ​t​(w)‖M≤C​Δ​t3\bigl\|\mathcal{E}_{\Delta t}(w)-\Phi_{E,h}^{\Delta t}(w)\bigr\|_{M}\leq C\Delta t^{3}(258)

uniformly forwwin boundedMM-balls.

Now define the full IMEX one-step map by the symmetric composition𝒮Δ​t,h:=ℐΔ​t/2∘ℰΔ​t∘ℐΔ​t/2.\mathcal{S}_{\Delta t,h}:=\mathcal{I}_{\Delta t/2}\circ\mathcal{E}_{\Delta t}\circ\mathcal{I}_{\Delta t/2}.(259)

Since both submaps are second-order consistent and the composition is
symmetric, standard composition theory for one-step methods gives‖𝒮Δ​t,h​(w)−ΦhΔ​t​(w)‖M≤C​Δ​t3\bigl\|\mathcal{S}_{\Delta t,h}(w)-\Phi_{h}^{\Delta t}(w)\bigr\|_{M}\leq C\Delta t^{3}(260)

forwwin bounded sets, whereΦhΔ​t\Phi_{h}^{\Delta t}denotes the exact
semi-discrete flow of (253). This proves
theO​(Δ​t3)O(\Delta t^{3})local truncation error.

We next pass from local to global temporal error. Leten:=whn−wh​(tn),tn=n​Δ​t.e^{n}:=w_{h}^{n}-w_{h}(t^{n}),\quad t^{n}=n\Delta t.(261)

Thenen+1\displaystyle e^{n+1}=𝒮Δ​t,h​(whn)−ΦhΔ​t​(wh​(tn))\displaystyle=\mathcal{S}_{\Delta t,h}(w_{h}^{n})-\Phi_{h}^{\Delta t}(w_{h}(t^{n}))=(𝒮Δ​t,h​(whn)−𝒮Δ​t,h​(wh​(tn)))+τn+1,\displaystyle=\Bigl(\mathcal{S}_{\Delta t,h}(w_{h}^{n})-\mathcal{S}_{\Delta t,h}(w_{h}(t^{n}))\Bigr)+\tau^{n+1},(262)

whereτn+1:=𝒮Δ​t,h​(wh​(tn))−ΦhΔ​t​(wh​(tn))\tau^{n+1}:=\mathcal{S}_{\Delta t,h}(w_{h}(t^{n}))-\Phi_{h}^{\Delta t}(w_{h}(t^{n}))(263)

is the local truncation defect. By (260),‖τn+1‖M≤C​Δ​t3.\|\tau^{n+1}\|_{M}\leq C\Delta t^{3}.(264)

Because the exact semi-discrete trajectory is bounded on[0,T][0,T]and the
numerical trajectory satisfies the stability estimate
(284), both remain in a common boundedMM-ball on[0,T][0,T]. On that ball the one-step map is locally Lipschitz:‖𝒮Δ​t,h​(u)−𝒮Δ​t,h​(v)‖M≤(1+C​Δ​t)​‖u−v‖M\bigl\|\mathcal{S}_{\Delta t,h}(u)-\mathcal{S}_{\Delta t,h}(v)\bigr\|_{M}\leq(1+C\Delta t)\|u-v\|_{M}(265)

for allu,vu,vin that ball. Applying (265) in
(262) yields‖en+1‖M≤(1+C​Δ​t)​‖en‖M+C​Δ​t3.\|e^{n+1}\|_{M}\leq(1+C\Delta t)\|e^{n}\|_{M}+C\Delta t^{3}.(266)

Sincee0=0e^{0}=0, the discrete Grönwall lemma givesmax0≤n≤T/Δ​t⁡‖en‖M≤C​Δ​t2.\max_{0\leq n\leq T/\Delta t}\|e^{n}\|_{M}\leq C\Delta t^{2}.(267)

On the FE space, the coefficient norm∥⋅∥M\|\cdot\|_{M}is exactly the discreteL2​(Ω)3L^{2}(\Omega)^{3}norm of the associated FE field, somax0≤n≤T/Δ​t⁡‖M→hn−M→h​(⋅,tn)‖L2​(Ω)≤C​Δ​t2.\max_{0\leq n\leq T/\Delta t}\|\vec{M}_{h}^{n}-\vec{M}_{h}(\cdot,t^{n})\|_{L^{2}(\Omega)}\leq C\Delta t^{2}.(268)

This proves theO​(Δ​t2)O(\Delta t^{2})global time-discretization error.

It remains to establish the spatial error. LetRh​M→R_{h}\vec{M}denote the
standard elliptic projection ofM→\vec{M}into the conforming FE spaceVh3V_{h}^{3}, defined componentwise with respect to the coercive bilinear form of
the diffusion–relaxation operator. Write the semi-discrete error asM→h−M→=θh+ρh,θh:=M→h−Rh​M→,ρh:=Rh​M→−M→.\vec{M}_{h}-\vec{M}=\theta_{h}+\rho_{h},\quad\theta_{h}:=\vec{M}_{h}-R_{h}\vec{M},\quad\rho_{h}:=R_{h}\vec{M}-\vec{M}.(269)

By the standard approximation properties of conformingPpP_{p}elements,‖ρh​(⋅,t)‖H1​(Ω)\displaystyle\|\rho_{h}(\cdot,t)\|_{H^{1}(\Omega)}≤C​hp​‖M→​(⋅,t)‖Hp+1​(Ω),\displaystyle\leq Ch^{p}\|\vec{M}(\cdot,t)\|_{H^{p+1}(\Omega)},(270)‖ρh​(⋅,t)‖L2​(Ω)\displaystyle\|\rho_{h}(\cdot,t)\|_{L^{2}(\Omega)}≤C​hp+1​‖M→​(⋅,t)‖Hp+1​(Ω).\displaystyle\leq Ch^{p+1}\|\vec{M}(\cdot,t)\|_{H^{p+1}(\Omega)}.(271)

Subtract the projected continuous weak equation from the semi-discrete weak
equation. Testing the resulting equation withθh\theta_{h}yields the standard
error identity12​dd​t​‖θh‖L2​(Ω)2+c0​‖θh‖H1​(Ω)2≤C​‖θh‖L2​(Ω)2+C​Ξh​(t),\frac{1}{2}\frac{\mathrm{d}}{\mathrm{d}t}\|\theta_{h}\|_{L^{2}(\Omega)}^{2}+c_{0}\|\theta_{h}\|_{H^{1}(\Omega)}^{2}\leq C\|\theta_{h}\|_{L^{2}(\Omega)}^{2}+C\Xi_{h}(t),(272)

whereΞh​(t)\Xi_{h}(t)collects the projection defects and the spatial DDF
consistency defect. By the boundedness of𝒯a\mathcal{T}_{a}fromProposition˜A.1, the local Lipschitz estimate for the precession
nonlinearity, and the assumed consistency of the discrete DDF evaluation,
one hasΞh​(t)≤C​(‖ρh​(⋅,t)‖H1​(Ω)2+‖∂tρh​(⋅,t)‖H−1​(Ω)2+h2​p+2).\Xi_{h}(t)\leq C\Bigl(\|\rho_{h}(\cdot,t)\|_{H^{1}(\Omega)}^{2}+\|\partial_{t}\rho_{h}(\cdot,t)\|_{H^{-1}(\Omega)}^{2}+h^{2p+2}\Bigr).(273)

Using (270), the analogous estimate for∂tρh\partial_{t}\rho_{h}, and Grönwall’s inequality in
(272), we obtainsup0≤t≤T‖θh​(⋅,t)‖L2​(Ω)+‖θh‖L2​(0,T;H1​(Ω))≤C​hp.\sup_{0\leq t\leq T}\|\theta_{h}(\cdot,t)\|_{L^{2}(\Omega)}+\|\theta_{h}\|_{L^{2}(0,T;H^{1}(\Omega))}\leq Ch^{p}.(274)

Combining (269), (270), and
(274) yields (249). Under the usual
elliptic regularity hypothesis, the optimalL∞​(0,T;L2​(Ω))L^{\infty}(0,T;L^{2}(\Omega))estimate (250) follows by
the standard Aubin–Nitsche duality argument.

Finally, combine the temporal and spatial estimates by the triangle
inequality:‖M→hn−M→​(⋅,tn)‖L2​(Ω)\displaystyle\|\vec{M}_{h}^{n}-\vec{M}(\cdot,t^{n})\|_{L^{2}(\Omega)}≤‖M→hn−M→h​(⋅,tn)‖L2​(Ω)\displaystyle\leq\|\vec{M}_{h}^{n}-\vec{M}_{h}(\cdot,t^{n})\|_{L^{2}(\Omega)}+‖M→h​(⋅,tn)−M→​(⋅,tn)‖L2​(Ω).\displaystyle\quad+\|\vec{M}_{h}(\cdot,t^{n})-\vec{M}(\cdot,t^{n})\|_{L^{2}(\Omega)}.(275)

Applying (268) and (250)
gives‖M→hn−M→​(⋅,tn)‖L2​(Ω)≤C​(Δ​t2+hp+1),\|\vec{M}_{h}^{n}-\vec{M}(\cdot,t^{n})\|_{L^{2}(\Omega)}\leq C\bigl(\Delta t^{2}+h^{p+1}\bigr),(276)

which is (251).
∎

## Theorem A.13(Nonlinear stability of the IMEX step).

Let‖w‖M2:=∑i=13wi⊤​M​wi.\|w\|_{M}^{2}:=\sum_{i=1}^{3}w_{i}^{\top}Mw_{i}.(277)

Assume eitherv→≡0\vec{v}\equiv 0or (31)
holds and advection is discretized by the skew operatorNvskewN_{v}^{\mathrm{skew}}so thatz⊤​Nvskew​z=0for all​z∈ℝNh.z^{\top}N_{v}^{\mathrm{skew}}z=0\quad\text{for all }z\in\mathbb{R}^{N_{h}}.(278)

Assume also that the discrete precession load satisfiesLemma˜A.9. Define the block operatorsℳ:=blkdiag​(M,M,M),\mathcal{M}:=\mathrm{blkdiag}(M,M,M),(279)𝒜:=blkdiag​(K,K,K)+blkdiag​(S2,S2,S1),\mathcal{A}:=\mathrm{blkdiag}(K,K,K)+\mathrm{blkdiag}(S_{2},S_{2},S_{1}),(280)

and the source vectorf:=(0,0,bT1).f:=(0,0,b_{T_{1}}).(281)

Suppose the explicit midpoint stage fromw(a)w^{(a)}tow(b)w^{(b)}satisfiesE​(w(b))−E​(w(a))=δn,E​(w):=12​‖w‖M2,E(w^{(b)})-E(w^{(a)})=\delta_{n},\quad E(w):=\frac{1}{2}\|w\|_{M}^{2},(282)

with defect bound|δn|\displaystyle|\delta_{n}|≤C​|γ|​(1+Λn)​Δ​t3,\displaystyle\leq C\,|\gamma|\,(1+\Lambda_{n})\,\Delta t^{3},Λn\displaystyle\Lambda_{n}:=max⁡{‖wn‖M,‖w(a)‖M,‖w~‖M},\displaystyle:=\max\bigl\{\|w^{n}\|_{M},\,\|w^{(a)}\|_{M},\,\|\tilde{w}\|_{M}\bigr\},(283)

whereCCis independent of the mesh sizehh. In the exact discrete
skew-symmetric case,δn=0\delta_{n}=0.

Then one IMEX step
(27)–(30) satisfies‖wn+1‖M2−‖wn‖M22​Δ​t+18​(w(a)+wn)⊤​𝒜​(w(a)+wn)+18​(wn+1+w(b))⊤​𝒜​(wn+1+w(b))≤14​f⊤​(w(a)+wn)+14​f⊤​(wn+1+w(b))+C​|γ|​(1+Λn)​Δ​t2.\frac{\|w^{n+1}\|_{M}^{2}-\|w^{n}\|_{M}^{2}}{2\,\Delta t}+\frac{1}{8}\,(w^{(a)}+w^{n})^{\top}\mathcal{A}\,(w^{(a)}+w^{n})\\
+\frac{1}{8}\,(w^{n+1}+w^{(b)})^{\top}\mathcal{A}\,(w^{n+1}+w^{(b)})\\
\leq\frac{1}{4}\,f^{\top}\bigl(w^{(a)}+w^{n}\bigr)+\frac{1}{4}\,f^{\top}\bigl(w^{n+1}+w^{(b)}\bigr)+C\,|\gamma|\,(1+\Lambda_{n})\,\Delta t^{2}.(284)

In particular, in the exact skew caseδn=0\delta_{n}=0, the perturbation term
vanishes and (284) holds with equality. The bound is
uniform in the mesh sizehh.

## Proof.

We proceed by analyzing the two implicit half-steps and the explicit middle
step separately.

First consider the initial Crank–Nicolson half-step
(27). In block form it may be written asℳ​(w(a)−wn)+Δ​t4​𝒜​(w(a)+wn)=Δ​t2​f.\mathcal{M}\,(w^{(a)}-w^{n})+\frac{\Delta t}{4}\,\mathcal{A}\,(w^{(a)}+w^{n})=\frac{\Delta t}{2}\,f.(285)

Take the Euclidean inner product of (285) with12​(w(a)+wn)\frac{1}{2}(w^{(a)}+w^{n}). Sinceℳ\mathcal{M}is symmetric, we have the
polarization identity(w(a)−wn)⊤​ℳ​(w(a)+wn)=‖w(a)‖M2−‖wn‖M2.(w^{(a)}-w^{n})^{\top}\mathcal{M}\,(w^{(a)}+w^{n})=\|w^{(a)}\|_{M}^{2}-\|w^{n}\|_{M}^{2}.(286)

ThereforeE​(w(a))−E​(wn)Δ​t+18​(w(a)+wn)⊤​𝒜​(w(a)+wn)=14​f⊤​(w(a)+wn).\frac{E(w^{(a)})-E(w^{n})}{\Delta t}+\frac{1}{8}\,(w^{(a)}+w^{n})^{\top}\mathcal{A}\,(w^{(a)}+w^{n})\\
=\frac{1}{4}\,f^{\top}(w^{(a)}+w^{n}).(287)

Next consider the second Crank–Nicolson half-step
(30), which in block form readsℳ​(wn+1−w(b))+Δ​t4​𝒜​(wn+1+w(b))=Δ​t2​f.\mathcal{M}\,(w^{n+1}-w^{(b)})+\frac{\Delta t}{4}\,\mathcal{A}\,(w^{n+1}+w^{(b)})=\frac{\Delta t}{2}\,f.(288)

Taking the Euclidean inner product with12​(wn+1+w(b))\frac{1}{2}(w^{n+1}+w^{(b)})yieldsE​(wn+1)−E​(w(b))Δ​t+18​(wn+1+w(b))⊤​𝒜​(wn+1+w(b))=14​f⊤​(wn+1+w(b)).\frac{E(w^{n+1})-E(w^{(b)})}{\Delta t}+\frac{1}{8}\,(w^{n+1}+w^{(b)})^{\top}\mathcal{A}\,(w^{n+1}+w^{(b)})\\
=\frac{1}{4}\,f^{\top}(w^{n+1}+w^{(b)}).(289)

We now analyze the explicit stage. By definition,E​(w(b))−E​(w(a))=δn.E(w^{(b)})-E(w^{(a)})=\delta_{n}.(290)

In the ideal discrete skew-symmetric midpoint update, the precession term
and the skew advection term do not change theMM-energy, soδn=0\delta_{n}=0. More generally, under the stated hypothesis
(283), the explicit-stage defect is
bounded by|E​(w(b))−E​(w(a))Δ​t|=|δn|Δ​t≤C​|γ|​(1+Λn)​Δ​t2.\left|\frac{E(w^{(b)})-E(w^{(a)})}{\Delta t}\right|=\frac{|\delta_{n}|}{\Delta t}\leq C\,|\gamma|\,(1+\Lambda_{n})\,\Delta t^{2}.(291)

Add (287) and (289). Using
(290), we obtainE​(wn+1)−E​(wn)Δ​t+18​(w(a)+wn)⊤​𝒜​(w(a)+wn)\displaystyle\frac{E(w^{n+1})-E(w^{n})}{\Delta t}+\frac{1}{8}\,(w^{(a)}+w^{n})^{\top}\mathcal{A}\,(w^{(a)}+w^{n})+18​(wn+1+w(b))⊤​𝒜​(wn+1+w(b))\displaystyle\quad+\frac{1}{8}\,(w^{n+1}+w^{(b)})^{\top}\mathcal{A}\,(w^{n+1}+w^{(b)})=14​f⊤​(w(a)+wn)+14​f⊤​(wn+1+w(b))\displaystyle=\frac{1}{4}\,f^{\top}(w^{(a)}+w^{n})+\frac{1}{4}\,f^{\top}(w^{n+1}+w^{(b)})(292)+E​(w(b))−E​(w(a))Δ​t.\displaystyle\quad+\frac{E(w^{(b)})-E(w^{(a)})}{\Delta t}.(293)

Invoking (291) givesE​(wn+1)−E​(wn)Δ​t+18​(w(a)+wn)⊤​𝒜​(w(a)+wn)+18​(wn+1+w(b))⊤​𝒜​(wn+1+w(b))≤14​f⊤​(w(a)+wn)+14​f⊤​(wn+1+w(b))+C​|γ|​(1+Λn)​Δ​t2.\frac{E(w^{n+1})-E(w^{n})}{\Delta t}+\frac{1}{8}\,(w^{(a)}+w^{n})^{\top}\mathcal{A}\,(w^{(a)}+w^{n})\\
+\frac{1}{8}\,(w^{n+1}+w^{(b)})^{\top}\mathcal{A}\,(w^{n+1}+w^{(b)})\\
\leq\frac{1}{4}\,f^{\top}\bigl(w^{(a)}+w^{n}\bigr)+\frac{1}{4}\,f^{\top}\bigl(w^{n+1}+w^{(b)}\bigr)+C\,|\gamma|\,(1+\Lambda_{n})\,\Delta t^{2}.(294)

SinceE​(w)=12​‖w‖M2E(w)=\frac{1}{2}\|w\|_{M}^{2}, this is exactly
(284).

It remains only to note that the bound is uniform inhh. The half-step
identities (287) and (289) are
purely algebraic and involve only the symmetric block operatorsℳ\mathcal{M}and𝒜\mathcal{A}. The mesh dependence enters only through the
assumed defect bound (283), whose
constant is taken to be uniform inhh. Therefore the constant in
(284) is uniform in the mesh size.
∎

## Remark 2.

If the explicit middle stage is implemented by a discrete update that is
exactlyMM-energy preserving, thenδn=0\delta_{n}=0in
(282). In that case,
(284) becomes an exact discrete energy identity, and all
dissipation is produced by the two Crank–Nicolson half-steps through the
diffusion and relaxation operators.

If the explicit stage is realized only approximately, for example through a
quadrature-based field evaluation together with a projected Rodrigues
rotation, then the quantityδn\delta_{n}measures the defect from exact
energy preservation. The theorem shows that as long as this defect is of
higher order inΔ​t\Delta tand uniform inhh, it enters the stability
estimate only as a perturbative remainder.

A stronger estimate written purely in terms of endpoint dissipation,
involving onlywnw^{n}andwn+1w^{n+1}, generally requires additional control of
the intermediate statesw(a)w^{(a)}andw(b)w^{(b)}relative to the endpoints.
Such a refinement can be obtained under stronger assumptions on the
explicit-stage map, but is not needed for the mesh-uniform stability bound
used here.

## Data Availability Statement

Data sharing is not applicable to this article as no new experimental data were created or analyzed in this study. The numerical results reported were generated from deterministic calculations of the model described in the manuscript. The code used to produce the numerical results is not publicly available; it can be obtained from the corresponding author upon reasonable request.

## References
- [1]W. Barros Jr, D. F. Gochberg, and J. C. Gore(2009)Nuclear magnetic resonance signal dynamics of liquids in the presence of distant dipolar fields, revisited.J Chem Phys130(17),pp. 174506.External Links:DocumentCited by:§I.
- [2]L.-S. Bouchard and W.S. Warren(2004)Reconstruction of porous material geometry by stochastic optimization based on NMR measurements of the dipolar field.J Magn Reson170,pp. 299–309.Cited by:§I.
- [3]L.-S. Bouchard, F.W. Wehrli, C.-L. Chin, and W.S. Warren(2005)Structural anisotropy and internal magnetic fields in trabecular bone: coupling solution and solid dipolar interactions.J Magn Reson176,pp. 27–36.Cited by:§I.
- [4]Louis-S. Bouchard and W. S. Warren(2005)Multiple-quantum vector field imaging by magnetic resonance.Journal of Magnetic Resonance177(1),pp. 9–21.Cited by:§I.
- [5]L. Bouchard(2007)Finite element formulation of the bloch equations with dipolar field effects.arXiv preprint arXiv:0706.3540.Cited by:§I.
- [6]L. Bouchard(2005)Characterization of material microstructure using intermolecular multiple-quantum coherences.Princeton University.Cited by:§I.
- [7]R. Bowtell, S. Gutteridge, and C. Ramanathan(2001)Imaging the long-range dipolar field in structured liquid state samples.J Magn Reson150,pp. 147–155.Cited by:§I.
- [8]R. Bowtell and P. Robyr(1996)Structural investigations with the dipolar demagnetizing field in solution NMR.Phys Rev Lett76,pp. 4971–4974.Cited by:§I.
- [9]R. Bowtell(1992)Indirect detection via the dipolar demagnetizing field.J Magn Reson100,pp. 1–17.Cited by:§I.
- [10]C. Chin, X. Tang, Louis-S. Bouchard, P. K. Saha, W. S. Warren, and F. W. Wehrli(2003)Isolating quantum coherences in structural imaging using intermolecular double-quantum coherence mri.Journal of Magnetic Resonance165(2),pp. 309–314.Cited by:§I.
- [11]C. A. Corum and A. F. Gmitro(2004)Spatially varying steady state longitudinal magnetization in distant dipolar field-based sequences.J Magn Reson171(1),pp. 131–134.External Links:DocumentCited by:§I.
- [12]G. Deville, M. Bernier, and J.M. Delrieux(1979)NMR multiple echoes observed in solid He-3.Phys Rev B19,pp. 5666–5688.Cited by:§I.
- [13]T. Enss, S. Ahn, and W.S. Warren(1999)Visualization of the dipolar field in solution NMR and MR imaging: three-dimensional structure simulations.Chem Phys Lett305,pp. 101–108.Cited by:§I.
- [14]Q.H. He, W. Richter, S. Vathyam, and W.S. Warren(1993)Intermolecular multiple-quantum coherences and cross-correlations in solution nuclear magnetic resonance.J Chem Phys98,pp. 6779–6780.Cited by:§I.
- [15]S. Kirsch and P. Bachert(2009)Visualization of the distant dipolar field: a numerical study.Concepts Magn Reson Part A34A(6),pp. 357–364.External Links:DocumentCited by:§I.
- [16]M.P. Ledbetter, I.M. Savukov, L.-S. Bouchard, and M.V. Romalis(2004)Numerical and experimental studies of long-range magnetic dipolar interactions.J Chem Phys121,pp. 1454–1465.Cited by:§I.
- [17]S. Lee, W. Richter, S. Vathyam, and W.S. Warren(1996)Quantum treatment of the effects of dipole-dipole interactions in liquid nuclear magnetic resonance.J Chem Phys105,pp. 874–900.Cited by:§I.
- [18]A. Quarteroni, R. Sacco, and F. Saleri(2000)Numerical mathematics.Springer-Verlag,New York.Cited by:§II.3.
- [19]E. E. Sigmund, H. Cho, P. Chen, S. Byrnes, Y.-Q. Song, X. E. Guo, and T. R. Brown(2008)Diffusion-based MR methods for bone structure and evolution.Magn Reson Med59(1),pp. 28–39.External Links:DocumentCited by:§I.
- [20]X.-P. Tang, C.-L. Chin, L.-S. Bouchard, F. W. Wehrli, and W. S. Warren(2004)Observing bragg-like diffraction via multiple coupled nuclear spins.Physics Letters A326(1-2),pp. 114–125.Cited by:§I.
- [21]S. Vathyam, S. Lee, and W.S. Warren(1996)Homogeneous NMR spectra in inhomogeneous fields.Science272,pp. 92–96.Cited by:§I.
- [22]W.S. Warren, S. Ahn, M. Mescher, M. Garwood, K. Ugurbil, W. Richter, R.R. Rizi, J. Hopkins, and J.S. Leigh(1998)MR imaging contrast enhancement based on intermolecular zero quantum coherences.Science281,pp. 247–252.Cited by:§I.
- [23]W.S. Warren, W. Richter, A. Hamilton Andreotti, and B.T. Farmer(1993)Generation of impossible cross-peaks between bulk water and biomolecules in solution NMR.Science262,pp. 2005–2009.Cited by:§I.
- [24]C. K. Wong(2010)Theoretical analysis of the sensitivity of dipolar field signal to local field variations by perturbative expansion of the magnetization.J Magn Reson203(1),pp. 29–43.External Links:DocumentCited by:§I.

## 


- 


Major funding support from
