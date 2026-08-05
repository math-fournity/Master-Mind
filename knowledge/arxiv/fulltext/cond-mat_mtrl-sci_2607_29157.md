# Strength-degradation phase-field regularization of cohesive fracture: the antiplane case

**arXiv ID**: 2607.29157v1
**Authors**: Blaise Bourdin, Corrado Maurini
**Published**: 2026-07-31
**Categories**: cond-mat.mtrl-sci, math-ph, physics.class-ph
**Comments**: 43 pages, 18 figures, 1 table. Submitted to Comptes Rendus. Mecanique
**HTML URL**: https://arxiv.org/html/2607.29157v1

## Abstract

Phase-field approaches to fracture, initially designed as regularization of the Griffith model of brittle fracture, are now commonly viewed as gradient-damage models whose regularization length becomes a material property driving crack nucleation. One weakness of this approach is that the strength surface cannot be arbitrary: its shape is dictated by the elastic energy, and its magnitude by the regularization length. We focus on the antiplane version of the model introduced by Bourdin, Marigo, Maurini and Zolesi (arXiv:2506.22558), which handles crack propagation along unknown paths and nucleation governed by an arbitrary convex strength surface by degrading the strength instead of the stiffness. It can be interpreted as a regularization of softening plasticity in which localization bands obey an equivalent cohesive law set by the strength domain and the toughness, while the role of the regularization length, when small compared to the elasto-cohesive length, is purely numerical. Strength, stiffness, and toughness thus become independent material data, and limit analysis, perfect plasticity, cohesive fracture, and brittle fracture merge into a single variational framework. We derive closed-form solutions for a simple shear problem, propose a numerical scheme combining alternate minimization and conic programming, and numerically verify the equivalent cohesive law, its independence of the regularization, and the size effect governed by the elasto-cohesive length. A "surfing" simulation highlights the structure of the propagating crack while a re-entrant V-notch is used to show how the model bridges small-scale yielding, cohesive fracture, and brittle fracture without a priori hypotheses.

## Full Text

Strength-degradation phase-field regularization of cohesive fracture: the antiplane case

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
- License: CC BY 4.0arXiv:2607.29157v1 [cond-mat.mtrl-sci] 31 Jul 2026

## Strength-degradation phase-field regularization of cohesive fracture: the antiplane caseBlaise Bourdin, Corrado Maurini(July 31, 2026)

## Abstract

Phase-field approaches to fracture, initially designed as regularization of the Griffith model of brittle fracture, are now commonly viewed as gradient-damage models whose regularization length becomes a material property driving crack nucleation.
One weakness of this approach is that the strength surface cannot be arbitrary: its shape is dictated by the elastic energy, and its magnitude by the regularization length.
We focus on the antiplane version of the model introduced by Bourdin, Marigo, Maurini and Zolesi (arXiv:2506.22558), which handles crack propagation along unknown paths and nucleation governed by an arbitrary convex strength surface by degrading the strength instead of the stiffness.
It can be interpreted as a regularization of softening plasticity in which localization bands obey an equivalent cohesive law set by the strength domain and the toughness, while the role of the regularization length, when small compared to the elasto-cohesive length, is purely numerical.
Strength, stiffness, and toughness thus become independent material data, and limit analysis, perfect plasticity, cohesive fracture, and brittle fracture merge into a single variational framework.
We derive closed-form solutions for a simple shear problem, propose a numerical scheme combining alternate minimization and conic programming, and numerically verify the equivalent cohesive law, its independence of the regularization, and the size effect governed by the elasto-cohesive length.
A “surfing” simulation highlights the structure of the propagating crack while a re-entrant V-notch is used to show how the model bridges small-scale yielding, cohesive fracture, and brittle fracture withouta priorihypotheses.

Keywords:Phase-field fracture, Cohesive fracture, Variational
fracture mechanics, Antiplane shear, Crack nucleation, Strength, Conic
programming

## 1Introduction

The variational approach to fracture[38,17]and its phase-field regularizations[18]have become a standard framework to predict crack nucleation and propagation in brittle materials.
Mechanically, phase-field models can be interpreted as gradient-damage models[68,67], where a scalar variableα\alphadegrades the elastic stiffness and a regularization lengthℓ\ellcontrols the width of the localization bands.
In this framework, the material strength is not an independent constitutive ingredient: it emerges from the combination of the elastic stiffness, the fracture toughness, and the regularization length, which must therefore be tuned as a material parameter to fit the observed nucleation loads[78].
This approach becomes impractical for stiff materials of modest strength, for which the required regularization length far exceeds the relevant structural sizes, and for nominally brittle materials at very large scales, where the need to resolve the regularization length with the mesh leads to prohibitively large problem sizes.
Moreover, the shape of the resulting strength surface in a multiaxial stress state is essentially dictated by the form of the elastic energy and cannot be freely prescribed, failing to reproduce the experimentally measured multiaxial strength data of common brittle materials[49].

Plasticity theory, in contrast, accommodates an arbitrary convex strength domain[41,70]. Small-scale yielding (SSY) theory applies it to fracture through near-tip plastic deformation[61,45,71].
In SSY, cracks and stress concentrators generate confined plastic zones near the tip[44,72]. Plastic deformations can also concentrate on a curve in two dimensions or on a surface in three, acting as cohesive cracks, as in the classical slit problem[33,14].
Perfect plasticity alone, however, sustains a constant stress across such a band, so that the dissipated energy grows without bound with the displacement jump: it endows the material with a strength but not with a finite toughness, since the traction across the band can vanish only if the strength itself degrades.
Degrading the strength in the bulk leads to softening plasticity, whose pathologies are well documented — deformations localize on sets of vanishing measure and numerical solutions suffer a spurious mesh dependence — and are classically mitigated by nonlocal, gradient, or micromorphic regularizations[69,64,50,12,46,37,54,9].
These regularizations, however, are conceived as localization limiters: they leave the limit properties of the localization bands and their link with sharp-interface cohesive models unidentified.
Cohesive models of fracture[11,42,65,32,31,60]take this step at the interface level, letting strength and toughness enter as independent material data through a traction-separation law acting on surfaces of displacement discontinuity.
Unfortunately, they raise difficulties of their own.
First, their direct numerical implementation through interface elements is delicate[66,47,74]: the crack is confined to the mesh facets, and the interface stiffness introduces a spurious compliance.
Second, as recently shown by[75], sharp cohesive interfaces are incompatible with a linearly elastic bulk: no solution exists in the form of a regular crack with a simple tip, the stress exceeding the cohesive strength over a finite region around the tip.
The associated variational problem then lacks lower semi-continuity[16], calling for bulk energies whose growth is consistent with the interfacial strength.
Finally, no cohesive model is to date widely accepted for crack propagation along unknown paths, and the geometric regularity of the resulting cracks remains poorly understood: the existence theory for such energies does not rule out minimizers whose “fracture” is not a set of codimension one — a curve in two dimensions, a surface in three — but a Cantor-like set of intermediate dimension.

The formulation of regularized counterparts of cohesive models, enjoying the same flexibility as the phase-field models of brittle fracture, is thus the object of active research.
Gradient-damage models recovering a cohesive response with anℓ\ell-independent strength have been obtained by a suitable tuning of the stiffness-degradation and dissipation functions[55,56], or through directional energy decompositions implementing a prescribed mixed-mode cohesive law[35], but in both cases the strength remains tied to the stiffness degradation and does not enter as a constitutive strength domain independent of the elastic properties.

We recently introduced in[19]111Closely related models were independently introduced around the same time in[80,36].a variational phase-field fracture model that incorporates arbitrary convex strength domains. Given a three-dimensional domainΩ3​D{\Omega_{\mathrm{3D}}}, a vector-valued displacement fieldu¯:x¯∈Ω3​D→u¯​(x¯)∈ℝ3\underline{u}:\underline{x}\in{\Omega_{\mathrm{3D}}}\to\underline{u}(\underline{x})\in\mathbb{R}^{3}, and a phase fieldα:x¯∈Ω3​D→α​(x¯)∈[0,1]\alpha:\underline{x}\in{\Omega_{\mathrm{3D}}}\to{\alpha}(\underline{x})\in[0,1], this model is characterized by an energy functional of the formℰℓ​(u¯,α):=∫Ω3​Dψ3​D​(ε¯¯​(u¯),α)+Dℓ​(α,∇α)​d​V,\mathcal{E}_{\ell}(\underline{u},\alpha):=\int_{\Omega_{\mathrm{3D}}}\psi_{\mathrm{3D}}(\underline{\underline{\varepsilon}}(\underline{u}),\alpha)+D_{\ell}(\alpha,\nabla\alpha)\,\mathrm{d}V,(1)

whereε¯¯​(u¯)=sym​(∇¯¯​u¯)\underline{\underline{\varepsilon}}(\underline{u})=\mathrm{sym}({\underline{\underline{\nabla}}}\,\underline{u})denotes the linearized strain tensor.

The first term in (1) is the elastic energy density, defined asψ3​D​(ε¯¯,α)=minp¯¯∈𝕄s3⁡φ3​D​(ε¯¯,p¯¯,α),φ3​D​(ε¯¯,p¯¯,α)=12​𝖠0​(ε¯¯−p¯¯)⋅(ε¯¯−p¯¯)+𝗄​(α)​𝖧𝕂0​(p¯¯),\psi_{\mathrm{3D}}(\underline{\underline{\varepsilon}},\alpha)=\min_{\underline{\underline{p}}\in\mathbb{M}^{3}_{s}}\varphi_{\mathrm{3D}}(\underline{\underline{\varepsilon}},\underline{\underline{p}},\alpha),\quad\varphi_{\mathrm{3D}}(\underline{\underline{\varepsilon}},\underline{\underline{p}},\alpha)=\dfrac{1}{2}\mathsf{A}_{0}(\underline{\underline{\varepsilon}}-\underline{\underline{p}})\cdot(\underline{\underline{\varepsilon}}-\underline{\underline{p}})+\mathsf{k}(\alpha)\mathsf{H}_{\mathbb{K}_{0}}(\underline{\underline{p}}),(2)

where𝖠0\mathsf{A}_{0}is the fourth-order elasticity tensor,𝕄s3\mathbb{M}^{3}_{s}is the space of symmetric3×33\times 3tensors,𝗄​(α)\mathsf{k}(\alpha)is a decreasing function such that𝗄​(0)=1\mathsf{k}(0)=1and𝗄​(1)=0\mathsf{k}(1)=0, the dot “⋅\cdot” standing for the usual scalar product.
The single-valued function𝖧𝕂0​(p¯¯):=supσ¯¯∈𝕂0σ¯¯⋅p¯¯\mathsf{H}_{\mathbb{K}_{0}}(\underline{\underline{p}}):=\sup_{\underline{\underline{\sigma}}\in\mathbb{K}_{0}}\underline{\underline{\sigma}}\cdot\underline{\underline{p}}(3)

denotes the support function of the convex domain𝕂0⊂𝕄s3\mathbb{K}_{0}\subset\mathbb{M}^{3}_{s}representing the material strength,i.e.the domain of admissible Cauchy stress tensors in the undamaged material.
The symmetric tensorp¯¯\underline{\underline{p}}can be regarded as the nonlinear contribution to the geometric deformationε¯¯​(u¯)\underline{\underline{\varepsilon}}(\underline{u}).

The second term in (1) represents a fracture-type dissipation, which, as in classical phase-field fracture models, includes a gradient-type regularization and is defined asDℓ​(α,∇α):=𝖦c4​𝖼𝗐​(𝗐​(α)ℓ+ℓ​∇α⋅∇α),D_{\ell}(\alpha,\nabla\alpha):=\dfrac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\left(\dfrac{\mathsf{w}(\alpha)}{\ell}+\ell\,\nabla\alpha\cdot\nabla\alpha\right),

where𝖦c\mathsf{G}_{\mathrm{c}}is the fracture energy,ℓ\ellis a regularization length scale, and𝗐​(α)\mathsf{w}(\alpha)is an increasing function satisfying𝗐​(0)=0\mathsf{w}(0)=0and𝗐​(1)=1\mathsf{w}(1)=1.
The constant𝖼𝗐:=∫01𝗐​(s)​ds\mathsf{c_{w}}:=\int_{0}^{1}\sqrt{\mathsf{w}(s)}\,\mathrm{d}sis a normalization factor ensuring that the energy dissipated to create a fully developed crack of unit area is equal to𝖦c\mathsf{G}_{\mathrm{c}}.

The nonlinear dependence ofψ3​D\psi_{\mathrm{3D}}onε¯¯\underline{\underline{\varepsilon}}endows the model with a strength domain𝕂0\mathbb{K}_{0}in the undamaged state.
The elastic energy potential is akin to the energy density of perfect plasticity[26], with the damage variableα\alphaplaying the role of a softening variable acting on the strength domain.
The model can thus be interpreted as a phase-field regularization of a softening plasticity modelà laHencky (i.e.without the irreversibility condition on the plastic strain), in contrast with classical phase-field models, where the damage variable induces stiffness degradation.

Considering quasi-static evolution governed by minimization ofℰℓ​(u¯,α)\mathcal{E}_{\ell}(\underline{u},\alpha)under an irreversibility constraint onα\alpha,[19]report analytical solutions of a three-dimensional model problem indicating that in the limitℓ→0\ell\to 0the model recovers a cohesive fracture behavior[33,11,60]with a traction-separation law directly related to the strength domain𝕂0\mathbb{K}_{0}.
The conjectured limiting cohesive model is characterized by an energy functional of the formℰ0(u¯,α^)=∫Ω3​D∖Ju¯ψ3​D(ε¯¯,0)dV+∫Ju¯ϕ(⟦u¯⟧,α^)dS,\mathcal{E}_{0}(\underline{u},\hat{\alpha})=\int_{{\Omega_{\mathrm{3D}}}\setminus J_{\underline{u}}}\psi_{\mathrm{3D}}(\underline{\underline{\varepsilon}},0)\,\mathrm{d}V+\int_{J_{\underline{u}}}\phi(\left\llbracket\underline{u}\right\rrbracket,\hat{\alpha})\,\mathrm{d}S,(4)

whereψ3​D​(ε¯¯,0)\psi_{\mathrm{3D}}(\underline{\underline{\varepsilon}},0)is the bulk elastic energy density of the undamaged material,Ju¯J_{\underline{u}}is the set of displacement discontinuities,⟦u¯⟧\left\llbracket\underline{u}\right\rrbracketis the displacement jump acrossJu¯J_{\underline{u}}, andα^:Ju¯→[0,1]\hat{\alpha}:J_{\underline{u}}\to[0,1]is a local damage variable supported onJu¯J_{\underline{u}}.
The surface energy densityϕ\phitakes the formϕ(⟦u¯⟧,α^)=𝗄^(α^)𝖧𝕂0(n¯⊙⟦u¯⟧)+𝖦cα^,\phi(\left\llbracket\underline{u}\right\rrbracket,\hat{\alpha})=\hat{\mathsf{k}}(\hat{\alpha})\mathsf{H}_{\mathbb{K}_{0}}(\underline{n}\odot\left\llbracket\underline{u}\right\rrbracket)+\mathsf{G}_{\mathrm{c}}\,\hat{\alpha},(5)

wheren¯\underline{n}is the normal to the jump setJu¯J_{\underline{u}},⊙\odotdenotes the symmetric tensor product, andα^​(α):=∫0α𝗐​(β)​dβ∫01𝗐​(β)​dβ,𝗄^​(α^):=𝗄​(α​(α^)).{\hat{\alpha}}(\alpha):=\frac{\int_{0}^{\alpha}\sqrt{\mathsf{w}(\beta)}\,\mathrm{d}\beta}{\int_{0}^{1}\sqrt{\mathsf{w}(\beta)}\,\mathrm{d}\beta},\qquad\hat{\mathsf{k}}({\hat{\alpha}}):=\mathsf{k}(\alpha({\hat{\alpha}})).

TheΓ\Gamma-convergence towards the sharp cohesive energy has been proven, for the choice𝗄​(α)=(1−α)2\mathsf{k}(\alpha)=(1-\alpha)^{2}and𝗐​(α)=α2\mathsf{w}(\alpha)=\alpha^{2}, in the spatially discrete antiplane setting by[57]; a similar result had previously been established for gradient-damage models coupled with plasticity, also in the antiplane setting, by[28].

The present work is related to several lines of research.
Sharp-interface cohesive models with bulk energies consistent with the traction-separation law have been investigated numerically in[75].
Phase-field approximations byΓ\Gamma-convergence of specific cohesive fracture energies have been established in the scalar and, more recently, vector-valued settings[22,23].
A unified framework spanning theΓ\Gamma-convergence analysis, the reconstruction of the phase-field model realizing a prescribed cohesive law, and its mechanical assessment has recently been developed in the three-part series[4,2,3].
A family of gradient models coupling damage and plasticity and where the strength is accounted for through a convex domain inherited from the variational formulation of perfect plasticity[34,79,7,77], was proposed in[6,1,5]and studied in[28,29,30].
The model that we study here differs from these in that the damage variable degrades only the strength domain, leaving the elastic stiffness unaffected, and that no irreversibility condition is imposed on the nonlinear deformation: this minimal structure makes the limit properties of the localization bands explicit, with an equivalent cohesive law independent of both the regularization length and the elastic stiffness (Section3.2).

The goal of this work is to discuss in detail the properties of this model in the simplified setting of antiplane shear and to present a first set of numerical simulations of quasi-static crack growth exhibiting a cohesive-like behavior.
The antiplane shear setting greatly simplifies the analysis since the displacement field reduces to a scalar functionu:𝐱∈Ω→u​(𝐱)∈ℝu:\mathbf{x}\in\Omega\to u(\mathbf{x})\in\mathbb{R}, the strain tensor reduces to the gradient vector∇u\nabla u, and the stress tensor is represented by a shear-stress vector inℝ2\mathbb{R}^{2}.
Moreover, the nonlinear deformation is a vector, hence always representable as𝒑=⟦u⟧𝐧\boldsymbol{p}=\left\llbracket u\right\rrbracket\,\mathbf{n}for a suitable unit normal𝐧\mathbf{n}, and its support functionτc​‖𝒑‖\tau_{c}\|\boldsymbol{p}\|is finite for every jump.
The compatibility condition between the strength domain and the admissible jumps identified in[19]is therefore always satisfied, and the limit cohesive model is well-defined.
In three dimensions, by contrast, a symmetric tensorp¯¯\underline{\underline{p}}is in general not of the formn¯⊙⟦u¯⟧\underline{n}\odot\left\llbracket\underline{u}\right\rrbracket, and𝖧𝕂0(n¯⊙⟦u¯⟧)\mathsf{H}_{\mathbb{K}_{0}}(\underline{n}\odot\left\llbracket\underline{u}\right\rrbracket)is finite only for certain relative orientations of⟦u¯⟧\left\llbracket\underline{u}\right\rrbracketandn¯\underline{n}: a strength domain unbounded along the hydrostatic axis, for instance, forces⟦u¯⟧⋅n¯=0\left\llbracket\underline{u}\right\rrbracket\cdot\underline{n}=0and thus admits no opening.

Accordingly, for an isotropic material the strength domain𝕂0\mathbb{K}_{0}reduces to the disk of radius equal to the shear strengthτc\tau_{c}, its support function reduces to𝖧𝕂0​(𝒑)=τc​‖𝒑‖\mathsf{H}_{\mathbb{K}_{0}}(\boldsymbol{p})=\tau_{c}\|\boldsymbol{p}\|with𝒑∈ℝ2\boldsymbol{p}\in\mathbb{R}^{2}, and the energy functional (1), with the nonlinear deformation𝒑\boldsymbol{p}kept as an explicit unknown, specializes toℰℓ​(u,𝒑,α)=∫Ω(μ2​‖∇u−𝒑‖2+𝗄​(α)​τc​‖𝒑‖)​dA+𝖦c4​𝖼𝗐​∫Ω(𝗐​(α)ℓ+ℓ​‖∇α‖2)​dA,\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha)=\int_{\Omega}\Big(\tfrac{\mu}{2}\|\nabla u-\boldsymbol{p}\|^{2}+\mathsf{k}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|\Big)\,\mathrm{d}A+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\int_{\Omega}\Big(\frac{\mathsf{w}(\alpha)}{\ell}+\ell\,\|\nabla\alpha\|^{2}\Big)\,\mathrm{d}A,(6)

whereμ>0\mu>0is the shear modulus.
Eliminating𝒑\boldsymbol{p}by pointwise minimization yields a nonlinear elastic energy density that is quadratic in∇u\nabla ubelow the degraded strength𝗄​(α)​τc\mathsf{k}(\alpha)\,\tau_{c}and grows linearly above it: the model is a phase-field regularization of an antiplane softening plasticity model in which the damage variableα\alphadegrades the strength while leaving the elastic stiffnessμ\muunchanged.
Consistently, the surface energy density (5) of the limit cohesive model reduces toϕ(⟦u⟧,α^)=𝗄^(α^)τc|⟦u⟧|+𝖦cα^\phi(\left\llbracket u\right\rrbracket,\hat{\alpha})=\hat{\mathsf{k}}(\hat{\alpha})\,\tau_{c}\,\left|\left\llbracket u\right\rrbracket\right|+\mathsf{G}_{\mathrm{c}}\,\hat{\alpha}, a mode-III cohesive law that is set by two independent material data, the strengthτc\tau_{c}and the toughness𝖦c\mathsf{G}_{\mathrm{c}}, and whose precise shape can be fine-tuned through the constitutive functions𝗄\mathsf{k}and𝗐\mathsf{w}.

In this setting the model problem of Section3can be solved in closed form: the homogeneous solutions fix the equivalent materialstrengthand may display a constant-stress plateau atτ=τc\tau=\tau_{c}before softening; the localized solutions yield an explicit equivalentcohesive lawset by the toughness𝖦c\mathsf{G}_{\mathrm{c}}and the strengthτc\tau_{c}, both independent of the regularization lengthℓ\ell; and the corresponding no-snap-back conditions are governed byℓ/ℓch\ell/\ell_{\mathrm{ch}}for the material response and by the size ratioL/ℓchL/\ell_{\mathrm{ch}}for the structural response of a bar, whereℓch=μ​𝖦c/τc2\ell_{\mathrm{ch}}=\mu\mathsf{G}_{\mathrm{c}}/\tau_{c}^{2}is the elasto-cohesive length.
This analysis is the antiplane specialization of the three-dimensional construction of[19]; we report it in full because the scalar setting makes every step explicit and easy to follow, giving the complete picture while factoring out the effects of multiaxiality and of the tensorial nature of stress and strain, and because it provides the exact reference solutions against which the numerical results are assessed.

The main original contributions of this paper are the following.
First, we devise a numerical scheme that exploits the separately convex, non-smooth structure of the energy: the alternate-minimization subproblems are recast as second-order cone programs and solved by conic optimization[48,15,53,8], without any smoothing or penalization of the strength term.
Second, we verify the numerical solution against the closed-form solutions: the simulations recover the equivalent cohesive law and its independence ofℓ\ell, quantify the mesh-induced toughening, and reproduce the size effect inL/ℓchL/\ell_{\mathrm{ch}}, the antiplane counterpart of the Griffith–Barenblatt transition analyzed in[59]; in the linearly rigid limitμ→∞\mu\to\infty, where the structural response coincides with the cohesive law, we measure the latter directly.
Third, we extract the effective toughness𝖦ceff\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}from a “surfing” experiment: it recovers the prescribed𝖦c\mathsf{G}_{\mathrm{c}}when𝒑\boldsymbol{p}is unconstrained, but exceeds it when𝒑\boldsymbol{p}is irreversible, because of the residual plastic wake left behind the crack tip.
Finally, we describe how, within one and the same model, the nonlinear fields at the crack tip evolve from the small-scale-yielding zone of perfect plasticity[44,72]to a cohesive crack[11]and then to a brittle crack.
Taken together, these results present limit analysis[76], perfect plasticity, cohesive fracture, and brittle fracture not as separate constitutive descriptions, but as regimes of a single variational model with one set of material data(μ,τc,𝖦c)(\mu,\tau_{c},\mathsf{G}_{\mathrm{c}}); we return to this point in Section7.

The article is organized as follows.
Section2casts the model in the antiplane shear setting and derives the constitutive law and the first-order optimality conditions.
Section3constructs the homogeneous and localized solutions of a one-dimensional model problem, the associated equivalent cohesive law, and the corresponding no-snap-back conditions.
Section4introduces the one-parameter family of constitutive functions used in all the numerical simulations, for which the results of Section3take a fully explicit form.
Section5presents the dimensionless formulation and the alternate-minimization scheme; the conic-programming solution of the two subproblems is detailed in AppendixA.
Section6compares analytical predictions and numerical simulations for three problems: a rectangular domain under simple shear, a “surfing” simulation, and a V-notch.
Section7draws conclusions and discusses the extension to the multiaxial case treated in the companion paper.

## 2The phase-field model with strength degradation in the antiplane setting

## 2.1The antiplane shear setting

Consider an isotropic homogeneous linearly elastic material occupying a cylindrical domainΩ3​D=Ω×(−H,H)\Omega_{\mathrm{3D}}=\Omega\times(-H,H)in the reference configuration withΩ⊂ℝ2\Omega\subset\mathbb{R}^{2}andH≫diam​(Ω)H\gg\mathrm{diam}(\Omega).
The position vector can be decomposed asx¯=𝐱+z​e¯3\underline{x}=\mathbf{x}+z\,\underline{e}_{3}with𝐱=x​e¯1+y​e¯2∈Ω\mathbf{x}=x\,\underline{e}_{1}+y\,\underline{e}_{2}\in\Omegaandz∈(−H,H)z\in(-H,H).
In the antiplane setting, one assumes that the displacement field is of the formu¯​(x,y,z)=u​(x,y)​e¯3\underline{u}(x,y,z)=u(x,y)\,\underline{e}_{3}

withu:(x,y)∈Ω↦u​(x,y)∈ℝu:(x,y)\in\Omega\mapsto u(x,y)\in\mathbb{R}.
Under these hypotheses, one has thatε¯¯​(u¯)=∂xu​(e¯1⊙e¯3)+∂yu​(e¯2⊙e¯3),\underline{\underline{{{\varepsilon}}}}({\underline{{u}}})=\partial_{x}u\,(\underline{e}_{1}\odot\underline{e}_{3})+\partial_{y}u\,(\underline{e}_{2}\odot\underline{e}_{3}),

wherea¯⊙b¯:=12​(a¯⊗b¯+b¯⊗a¯)\underline{a}\odot\underline{b}:=\frac{1}{2}\left(\underline{a}\otimes\underline{b}+\underline{b}\otimes\underline{a}\right).
The strain tensorε¯¯​(u¯)\underline{\underline{{{\varepsilon}}}}({\underline{{u}}})can be represented by the vector-valued function𝜺=∇u:Ω→ℝ2\boldsymbol{{\varepsilon}}=\nabla u:\Omega\to\mathbb{R}^{2}, whose components are twice the tensor ones:𝜺=2​ε13​e¯1+2​ε23​e¯2\boldsymbol{{\varepsilon}}=2\varepsilon_{13}\,\underline{e}_{1}+2\varepsilon_{23}\,\underline{e}_{2}.
Moreover, all the components of the stressσ¯¯\underline{\underline{{\sigma}}}and the nonlinear deformationp¯¯\underline{\underline{{p}}}vanish except for(σ13,σ23)(\sigma_{13},\sigma_{23})and(p13,p23)(p_{13},p_{23}), which can be collected in the vectors𝝉:=(τ1,τ2)=σ13​e¯1+σ23​e¯2\boldsymbol{\tau}:=(\tau_{1},\tau_{2})=\sigma_{13}\,\underline{e}_{1}+\sigma_{23}\,\underline{e}_{2}and𝒑:=(p1,p2)=2​p13​e¯1+2​p23​e¯2\boldsymbol{p}:=(p_{1},p_{2})=2p_{13}\,\underline{e}_{1}+2p_{23}\,\underline{e}_{2}inℝ2\mathbb{R}^{2}.
With this convention — strain-like vectors collect twice the tensor components, the stress vector the bare ones — the duality pairings coincide:σ¯¯⋅ε¯¯=𝝉⋅𝜺\underline{\underline{{\sigma}}}\cdot\underline{\underline{{{\varepsilon}}}}=\boldsymbol{\tau}\cdot\boldsymbol{{\varepsilon}}andσ¯¯⋅p¯¯=𝝉⋅𝒑\underline{\underline{{\sigma}}}\cdot\underline{\underline{{p}}}=\boldsymbol{\tau}\cdot\boldsymbol{p}.

## 2.2Strain energy density and stress-strain constitutive relation at fixedα\alpha

Under the same hypotheses, one has that12​𝖠0​ε¯¯⋅ε¯¯=μ2​‖𝜺‖2\frac{1}{2}\mathsf{A}_{0}\underline{\underline{{{\varepsilon}}}}\cdot\underline{\underline{{{\varepsilon}}}}=\frac{\mu}{2}\|\boldsymbol{{\varepsilon}}\|^{2}, whereμ>0\mu>0is theshear modulus.
Moreover, for an isotropic strength domain𝕂0\mathbb{K}_{0}and forp¯¯\underline{\underline{{p}}}of the antiplane form above, the support function (3) reduces to𝖧𝕂0​(p¯¯)=supσ¯¯∈𝕂0σ¯¯⋅p¯¯=supσ¯¯∈𝕂0𝝉⋅𝒑=τc​‖𝒑‖,\mathsf{H}_{\mathbb{K}_{0}}(\underline{\underline{{p}}})=\sup_{\underline{\underline{{\sigma}}}\in\mathbb{K}_{0}}\underline{\underline{{\sigma}}}\cdot\underline{\underline{{p}}}=\sup_{\underline{\underline{{\sigma}}}\in\mathbb{K}_{0}}\boldsymbol{\tau}\cdot\boldsymbol{p}=\tau_{c}\|\boldsymbol{p}\|,

whereτc=supσ¯¯∈𝕂0‖𝝉‖\tau_{c}=\sup_{\underline{\underline{{\sigma}}}\in\mathbb{K}_{0}}\|\boldsymbol{\tau}\|is theshear strengthof the undamaged material.
Hence, the energy density (2) simplifies toψ​(𝜺,α)=min𝒑∈ℝ2⁡φ​(𝜺,𝒑,α),φ​(𝜺,𝒑,α)=μ2​‖𝜺−𝒑‖2+𝗄​(α)​τc​‖𝒑‖.\psi(\boldsymbol{{\varepsilon}},\alpha)=\min_{\boldsymbol{p}\in\mathbb{R}^{2}}\varphi(\boldsymbol{{\varepsilon}},\boldsymbol{p},\alpha),\quad\varphi(\boldsymbol{{\varepsilon}},\boldsymbol{p},\alpha)=\frac{\mu}{2}\|\boldsymbol{{\varepsilon}}-\boldsymbol{p}\|^{2}+\mathsf{k}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|.

Using the fact that the minimum over𝒑\boldsymbol{p}is attained by taking𝒑\boldsymbol{p}collinear to𝜺\boldsymbol{{\varepsilon}}and pointing in the same direction, in which case‖𝜺−𝒑‖2=(‖𝜺‖−‖𝒑‖)2\|\boldsymbol{{\varepsilon}}-\boldsymbol{p}\|^{2}=(\|\boldsymbol{{\varepsilon}}\|-\|\boldsymbol{p}\|)^{2}, we can also compute the energy density explicitly:ψ​(𝜺,α)=min‖𝒑‖≥0⁡μ2​(‖𝜺‖−‖𝒑‖)2+𝗄​(α)​τc​‖𝒑‖={μ2​‖𝜺‖2if​‖𝜺‖≤𝗄​(α)​τcμ,𝗄​(α)​τc​(‖𝜺‖−𝗄​(α)​τc2​μ)otherwise.\begin{split}\psi(\boldsymbol{{\varepsilon}},\alpha)&=\min_{\|\boldsymbol{p}\|\geq 0}\frac{\mu}{2}(\|\boldsymbol{{\varepsilon}}\|-\|\boldsymbol{p}\|)^{2}+\mathsf{k}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|\\
&=\begin{cases}\dfrac{\mu}{2}\|\boldsymbol{{\varepsilon}}\|^{2}&\text{ if }\|\boldsymbol{{\varepsilon}}\|\leq\mathsf{k}(\alpha)\,\dfrac{\tau_{c}}{\mu},\\
\mathsf{k}(\alpha)\,\tau_{c}\left(\|\boldsymbol{{\varepsilon}}\|-\mathsf{k}(\alpha)\,\dfrac{\tau_{c}}{2\mu}\right)&\text{ otherwise.}\end{cases}\end{split}(7)

The constitutive relation for the antiplane stress vector𝝉\boldsymbol{\tau}is obtained by differentiatingψ\psiwith respect to𝜺\boldsymbol{{\varepsilon}}:𝝉​(𝜺,α)={μ​𝜺if​‖𝜺‖≤𝗄​(α)​τcμ,𝗄​(α)​τc​𝜺‖𝜺‖otherwise.\boldsymbol{\tau}(\boldsymbol{{\varepsilon}},\alpha)=\begin{cases}\mu\boldsymbol{{\varepsilon}}&\text{ if }\|\boldsymbol{{\varepsilon}}\|\leq\mathsf{k}(\alpha)\,\dfrac{\tau_{c}}{\mu},\\
\mathsf{k}(\alpha)\,\tau_{c}\dfrac{\boldsymbol{{\varepsilon}}}{\|\boldsymbol{{\varepsilon}}\|}&\text{ otherwise.}\end{cases}(8)

The equivalent nonlinear constitutive relation and elastic energy density at fixedα\alphaare illustrated in Figure1.Figure 1:Equivalent nonlinear constitutive relation (a) and elastic energy density (b) at fixedα\alpha.

## 2.3Quasi-static variational formulation

In all that follows, we consider loadings in the form of applied displacement boundary conditionsu=u¯​(t)u=\bar{u}(t)on a part of the boundary∂uΩ\partial_{u}\Omega.
Assimilating the loading parameter to a time variable, the quasi-static evolution problem consists in finding (u​(t),α​(t)u(t),\alpha(t)) for each value oft∈[0,T]t\in[0,T].
This can be formulated in the framework of rate-independent processes[62]by assuming that the evolution is quasi-static,i.e.neglecting the effects of inertia and viscosity.
Discretizing the time variable in a sequence of loading steps0=t0<t1<…<tN=T0=t_{0}<t_{1}<\ldots<t_{N}=Tand enforcing a growth condition onα\alphato account for the irreversible nature of the damage process, we obtain an incremental formulation for the quasi-static evolution, which is amenable to a numerical implementation.
Namely, at loading stepii, the state of the system is obtained as a unilateral minimizer of the energy functional (1) which reduces toℰℓ​(u,𝒑,α)=∫Ω(μ2​‖∇u−𝒑‖2+𝗄​(α)​τc​‖𝒑‖)​dA+𝖦c4​𝖼𝗐​∫Ω(𝗐​(α)ℓ+ℓ​‖∇α‖2)​dA.\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha)=\int_{\Omega}\left(\frac{\mu}{2}\|\nabla u-\boldsymbol{p}\|^{2}+\mathsf{k}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|\right)\,\mathrm{d}A+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\int_{\Omega}\left(\frac{\mathsf{w}(\alpha)}{\ell}+\ell\|\nabla\alpha\|^{2}\right)\,\mathrm{d}A.(9)

At loading stepii, denoting byu¯i\bar{u}_{i}andα¯\bar{\alpha}prescribed displacements and damage on parts∂uΩ⊂∂Ω\partial_{u}\Omega\subset\partial\Omegaand∂αΩ⊂∂Ω\partial_{\alpha}\Omega\subset\partial\Omegarespectively, we solve(ui,𝒑i,αi)∈arg​minu∈𝒞i,α∈𝒟i,𝒑∈𝒫⁡ℰℓ​(u,𝒑,α),(u_{i},\boldsymbol{p}_{i},\alpha_{i})\in\operatorname*{arg\,min}_{\begin{subarray}{c}u\in\mathcal{C}_{i},\,\alpha\in\mathcal{D}_{i}\end{subarray},\,\boldsymbol{p}\in\mathcal{P}}\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha),(10)

where the spaces of the admissible fields are:𝒞i\displaystyle\mathcal{C}_{i}=\displaystyle={u∈B​V​(Ω):u=u¯i​on​∂uΩ},\displaystyle\{u\in BV(\Omega):u=\bar{u}_{i}\text{ on }\partial_{u}\Omega\},(11)𝒟i\displaystyle\mathcal{D}_{i}=\displaystyle={α∈H1​(Ω):αi−1≤α≤1​in​Ω,α=α¯​on​∂αΩ},\displaystyle\{\alpha\in H^{1}(\Omega):\alpha_{i-1}\leq\alpha\leq 1\text{ in }\Omega,\alpha=\bar{\alpha}\,\text{on}\,\partial_{\alpha}\Omega\},(12)𝒫\displaystyle\mathcal{P}=\displaystyle=ℳ​(Ω;ℝ2),\displaystyle\mathcal{M}(\Omega;\mathbb{R}^{2}),(13)

whereB​V​(Ω)BV(\Omega)andH1​(Ω)H^{1}(\Omega)denote respectively the space of scalar-valued functions with bounded variation and the Sobolev space of square-integrable functions with square-integrable gradient andℳ​(Ω;ℝ2)\mathcal{M}(\Omega;\mathbb{R}^{2})that ofℝ2\mathbb{R}^{2}-valued Radon measures onΩ\Omega.

Formally, because the energy functional exhibits linear growth at infinity, the nonlinear deformation𝒑\boldsymbol{p}may concentrate along regions of dimension strictly less thann=2n=2.
Moreover, since the elastic strain(∇u−𝒑)(\nabla u-\boldsymbol{p})must be square-integrable, the singular parts of the distributional derivative and the nonlinear deformation𝒑\boldsymbol{p}must coincide.
Consequently,uumay develop jump discontinuities along the setJuJ_{u}where𝒑\boldsymbol{p}concentrates.
It is therefore natural to introduce an additive decomposition of the strain fields into regular (R\mathrm{R}) and singular (S\mathrm{S}) parts∇u=∇Ru+∇Su,𝒑=𝒑R+𝒑S,\nabla u=\nabla^{\mathrm{R}}u+\nabla^{\mathrm{S}}u,\quad\boldsymbol{p}=\boldsymbol{p}^{\mathrm{R}}+\boldsymbol{p}^{\mathrm{S}},(14)

where the singular parts are supported on the jump setJuJ_{u}.
The singular parts are such that∇Su=𝒑S=⟦u⟧𝐧δJu,\nabla^{\mathrm{S}}u=\boldsymbol{p}^{\mathrm{S}}=\left\llbracket u\right\rrbracket\mathbf{n}\,\delta_{J_{u}},(15)

where⟦u⟧=u+−u−\left\llbracket u\right\rrbracket=u^{+}-u^{-}is the displacement jump acrossJuJ_{u}compatible with a unit normal vector𝐧\mathbf{n}.δJu\delta_{J_{u}}denotes a measure concentrated onJuJ_{u}such that for any continuous test functionff,∫Ωf​δJu​dA=∫Juf​ds\int_{\Omega}f\,\delta_{J_{u}}\,\mathrm{d}A=\int_{J_{u}}f\mathrm{d}s, wheressis the arc-length measure onJuJ_{u}, assuming implicitly thatJuJ_{u}is regular enough to admit a normal almost everywhere.

Using (14) and decomposing the integral onΩ\Omegainto the sum of bulk integrals onΩ∖Ju\Omega\setminus J_{u}where the strain fields are smooth and the surface integral on the jump setJuJ_{u}, the energy functional can be equivalently rewritten explicitly asℰℓ(u,𝒑,α)=∫Ω∖Ju(μ2∥∇u−𝒑∥2+𝗄(α)τc∥𝒑∥)dA+∫Ju𝗄(α)τc|⟦u⟧|ds+𝖦c4​𝖼𝗐​∫Ω(𝗐​(α)ℓ+ℓ​∇α⋅∇α)​dA.\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha)=\int_{\Omega\setminus J_{u}}\left(\frac{\mu}{2}\|\nabla u-\boldsymbol{p}\|^{2}+\mathsf{k}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|\right)\,\mathrm{d}A+\int_{J_{u}}\mathsf{k}(\alpha)\,\tau_{c}\,\left|\left\llbracket u\right\rrbracket\right|\,\mathrm{d}s\\
+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\int_{\Omega}\left(\frac{\mathsf{w}(\alpha)}{\ell}+\ell\nabla\alpha\cdot\nabla\alpha\right)\,\mathrm{d}A.(16)

## Remark 1(Irreversibility of the nonlinear deformation).

The formulation above does not include an irreversibility condition on the nonlinear deformation𝐩\boldsymbol{p}, which is then regarded as purely elastic and reversible.
Imposing an irreversibility condition on𝐩\boldsymbol{p}would lead to a more complex model, akin to a phase-field regularization of an elastoplastic model with softening.
The corresponding incremental energy minimization problem would read as(ui,𝒑i,αi)∈arg​minu∈𝒞i,α∈𝒟i,𝒑∈L1​(Ω)⁡ℰℓ​(u,𝒑,α;𝒑i−1,p¯i−1),(u_{i},\boldsymbol{p}_{i},\alpha_{i})\in\operatorname*{arg\,min}_{\begin{subarray}{c}u\in\mathcal{C}_{i},\,\alpha\in\mathcal{D}_{i}\end{subarray},\,\boldsymbol{p}\in L^{1}(\Omega)}\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha;\boldsymbol{p}_{i-1},\bar{p}_{i-1}),(17)

where the energy functional is extended toℰℓ​(u,𝒑,α;𝒑old,p¯old)=∫Ω(μ2​‖∇u−𝒑‖2+𝗄​(α)​τc​(p¯old+‖𝒑−𝒑old‖))​dA+𝖦c4​𝖼𝗐​∫Ω(𝗐​(α)ℓ+ℓ​∇α⋅∇α)​dA,\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha;\boldsymbol{p}_{\mathrm{old}},\bar{p}_{\mathrm{old}})=\int_{\Omega}\left(\frac{\mu}{2}\|\nabla u-\boldsymbol{p}\|^{2}+\mathsf{k}(\alpha)\,\tau_{c}(\bar{p}_{\mathrm{old}}+\|\boldsymbol{p}-\boldsymbol{p}_{\mathrm{old}}\|)\right)\,\mathrm{d}A\\
+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\int_{\Omega}\left(\frac{\mathsf{w}(\alpha)}{\ell}+\ell\,\nabla\alpha\cdot\nabla\alpha\right)\,\mathrm{d}A,(18)

𝒑old\boldsymbol{p}_{\mathrm{old}}andp¯old\bar{p}_{\mathrm{old}}being the nonlinear deformation and the cumulated plastic deformation at the previous loading step, as in variational approaches to fracture coupled with plasticity[6,1,5].
Given an initial state(α0,𝐩0,p¯0)(\alpha_{0},\boldsymbol{p}_{0},\bar{p}_{0}), the updating rule for the cumulated plastic deformation isp¯i:=p¯i−1+‖𝐩i−𝐩i−1‖\bar{p}_{i}:=\bar{p}_{i-1}+\|\boldsymbol{p}_{i}-\boldsymbol{p}_{i-1}\|.
Accounting for the plastic irreversibility is not necessary to obtain a cohesive fracture behavior in the limitℓ→0\ell\to 0, as shown in[19], but can be relevant to model ductile fracture.

## Remark 2(Two-field formulation).

In the absence of an irreversibility condition on𝐩\boldsymbol{p}, we can also consider a two-field formulation in terms of the displacementuuand the damageα\alphaonly, by eliminating the nonlinear deformation𝐩\boldsymbol{p}through partial minimization of the energy functional with respect to𝐩\boldsymbol{p}.
This leads to the equivalent formulation(ui,αi)∈arg​minu∈𝒞i,α∈𝒟i⁡ℰℓ​(u,α),(u_{i},\alpha_{i})\in\operatorname*{arg\,min}_{u\in\mathcal{C}_{i},\alpha\in\mathcal{D}_{i}}\mathcal{E}_{\ell}(u,\alpha),

whereℰℓ(u,α)=∫Ω∖Juψ(∇u,α)dA+∫Ju𝗄(α)τc|⟦u⟧|ds+𝖦c4​𝖼𝗐∫Ω(𝗐​(α)ℓ+ℓ∇α⋅∇α)dA,\mathcal{E}_{\ell}(u,\alpha)=\int_{\Omega\setminus J_{u}}\psi(\nabla u,\alpha)\,\mathrm{d}A+\int_{J_{u}}\mathsf{k}(\alpha)\,\tau_{c}\,\left|\left\llbracket u\right\rrbracket\right|\,\mathrm{d}s+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\int_{\Omega}\left(\frac{\mathsf{w}(\alpha)}{\ell}+\ell\nabla\alpha\cdot\nabla\alpha\right)\,\mathrm{d}A,(19)

withψ​(∇u,α)\psi(\nabla u,\alpha)being the elastic energy density defined above.

## 2.4First order optimality conditions for local minimizers

Aglobal minimizerof the energy at loading stepiisatisfies the following condition:(u,𝒑,α)∈𝒞i×𝒫×𝒟is.t.ℰℓ​(u,𝒑,α)≤ℰℓ​(u^,𝒑^,α^),∀(u^,𝒑^,α^)∈𝒞i×𝒫×𝒟i.(u,\boldsymbol{p},\alpha)\in\mathcal{C}_{i}\times\mathcal{P}\times\mathcal{D}_{i}\quad\text{s.t.}\quad\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha)\leq\mathcal{E}_{\ell}(\hat{u},\hat{\boldsymbol{p}},\hat{\alpha}),\quad\forall(\hat{u},\hat{\boldsymbol{p}},\hat{\alpha})\in\mathcal{C}_{i}\times\mathcal{P}\times\mathcal{D}_{i}.

Global minimization is useful to characterize the problem within the direct method of the calculus of variations[25].
However, computing global minimizers of non-convex functionals is typically intractable numerically, and physically questionable: it would require the system to overcome arbitrarily large energy barriers to reach the absolute minimum.

The notion of alocal minimizeris relevant from the physical point of view.
We therefore state the optimality conditions at the time steptit_{i}through thedirectional local minimalitycondition[67,52]:Find(u,𝒑,α)∈𝒞i×𝒫×𝒟isuch that∀(u^,𝒑^,α^)∈𝒞i×𝒫×𝒟i,∃h¯>0:∀0<h<h¯,ℰℓ​(u+h​(u^−u),𝒑+h​(𝒑^−𝒑),α+h​(α^−α))−ℰℓ​(u,𝒑,α)≥0.\text{Find }(u,\boldsymbol{p},\alpha)\in\mathcal{C}_{i}\times\mathcal{P}\times\mathcal{D}_{i}\text{ such that }\forall(\hat{u},\hat{\boldsymbol{p}},\hat{\alpha})\in\mathcal{C}_{i}\times\mathcal{P}\times\mathcal{D}_{i},\exists{\bar{h}>0}:\\
\forall 0<h<\bar{h},\ \mathcal{E}_{\ell}(u+h(\hat{u}-u),\boldsymbol{p}+h(\hat{\boldsymbol{p}}-\boldsymbol{p}),\alpha+h(\hat{\alpha}-\alpha))-\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha)\geq 0.(20)

A set offirst-order necessary optimality conditionsfor the minimization ofℰℓ​(u,𝒑,α)\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha)at loading stepiican be obtained by taking a first order expansion of (20) inh>0h>0.
Because of the box constraint onα∈[αi−1,1]\alpha\in[\alpha_{i-1},1], the non-smoothness of the energy functional with respect to𝒑\boldsymbol{p}and⟦u⟧\left\llbracket u\right\rrbracket, the optimality conditions are expressed as variational inequalities.
To obtain pointwise strong form of the optimality conditions, we distinguish the subsetJuJ_{u}ofΩ\Omegawhereuujumps and its complementΩ∖Ju\Omega\setminus J_{u}, whereuuis smooth enough to admit classical derivatives.
For the sake of simplicity, we assume thatJu∩∂uΩ=∅J_{u}\cap\partial_{u}\Omega=\emptyset, otherwise the Dirichlet boundary conditions should be relaxed to account for possible jumps on the Dirichlet boundary[63, seee.g.].

## 2.4.1Optimality condition for the displacement fielduu: mechanical equilibrium

Setting𝒑^=𝒑\hat{\boldsymbol{p}}=\boldsymbol{p},α^=α\hat{\alpha}=\alpha, andu^=u+v^\hat{u}=u+\hat{v}withv^\hat{v}in the vector space𝒞0:={v∈B​V​(Ω):v=0​on​∂uΩ,Jv⊆Ju}\mathcal{C}_{0}:=\{v\in BV(\Omega):v=0\text{ on }\partial_{u}\Omega,\;J_{v}\subseteq J_{u}\}of admissible variations, the perturbed displacement in (20) isuh:=u+h​v^u_{h}:=u+h\,\hat{v}, and the first order expansion inhhleads to∫Ω∖Ju𝝉⋅∇v^dA+∫Ju𝗄(α)τcsgn(⟦u⟧)⟦v^⟧ds≥0,∀v^∈𝒞0.\int_{\Omega\setminus J_{u}}\boldsymbol{\tau}\cdot\nabla\hat{v}\,\mathrm{d}A+\int_{J_{u}}\mathsf{k}(\alpha)\,\tau_{c}\,\text{sgn}\left(\left\llbracket u\right\rrbracket\right)\,\left\llbracket\hat{v}\right\rrbracket\,\mathrm{d}s\geq 0,\quad\forall\hat{v}\in\mathcal{C}_{0}.

which, since𝒞0\mathcal{C}_{0}is a vector space, must hold as an equality (variations jumping outsideJuJ_{u}only return the strength condition|𝝉⋅𝐧|≤𝗄​(α)​τc|\boldsymbol{\tau}\cdot\mathbf{n}|\leq\mathsf{k}(\alpha)\,\tau_{c}on the candidate jump surface), that can be rewritten as222Here we use that, forJu∩∂Ω=∅J_{u}\cap\partial\Omega=\emptyset,∫Ω∖Ju𝝉⋅∇vdA=−∫Ω∖Judiv(𝝉)vdA+∫∂Ω(𝝉v)⋅𝐧ds−∫Ju⟦𝝉v⟧⋅𝐧ds,\int_{\Omega\setminus J_{u}}\boldsymbol{\tau}\cdot\nabla v\,\mathrm{d}A=-\int_{\Omega\setminus J_{u}}\mathrm{div}(\boldsymbol{\tau})v\,\mathrm{d}A+\int_{\partial\Omega}(\boldsymbol{\tau}v)\cdot\mathbf{n}\,\mathrm{d}s-\int_{J_{u}}\left\llbracket\boldsymbol{\tau}v\right\rrbracket\cdot\mathbf{n}\,\mathrm{d}s,and⟦𝝉v⟧=⟦𝝉⟧{v}+{𝝉}⟦v⟧\left\llbracket\boldsymbol{\tau}v\right\rrbracket=\left\llbracket\boldsymbol{\tau}\right\rrbracket\left\{v\right\}+\left\{\boldsymbol{\tau}\right\}\left\llbracket v\right\rrbracket.−∫Ω∖Judiv(𝝉)vdA+∫∂Ω(𝝉⋅𝐧)vds−∫Ju⟦𝝉⟧⋅𝐧{v}ds+∫Ju(𝗄(α)τcsgn(⟦u⟧)−{𝝉}⋅𝐧)⟦v⟧ds=0,-\int_{\Omega\setminus J_{u}}\mathrm{div}(\boldsymbol{\tau})v\,\mathrm{d}A+\int_{\partial\Omega}(\boldsymbol{\tau}\cdot\mathbf{n})v\,\mathrm{d}s-\int_{J_{u}}\left\llbracket\boldsymbol{\tau}\right\rrbracket\cdot\mathbf{n}\left\{v\right\}\,\mathrm{d}s\\
+\int_{J_{u}}\left(\mathsf{k}(\alpha)\,\tau_{c}\,\text{sgn}\left(\left\llbracket u\right\rrbracket\right)-\left\{\boldsymbol{\tau}\right\}\cdot\mathbf{n}\right)\left\llbracket v\right\rrbracket\,\mathrm{d}s=0,

where𝝉=μ​(∇u−𝒑)\boldsymbol{\tau}=\mu(\nabla u-\boldsymbol{p})denotes the stress vector, and{(⋅)}=((⋅)++(⋅)−)/2\left\{(\cdot)\right\}=((\cdot)^{+}+(\cdot)^{-})/2.

By the arbitrariness of the test functionv∈𝒞0v\in\mathcal{C}_{0}, we obtain the strong form of the mechanical equilibrium equations.
Takingvvwith⟦v⟧=0\left\llbracket v\right\rrbracket=0onJuJ_{u}gives{div​(𝝉)=0​in​Ω∖Ju,𝝉⋅𝐧=0​on​∂Ω∖∂uΩ,⟦𝝉⟧⋅𝐧=0onJu,\begin{cases}\mathrm{div}(\boldsymbol{\tau})=0\text{ in }\Omega\setminus J_{u},\\
\boldsymbol{\tau}\cdot\mathbf{n}=0\text{ on }\partial\Omega\setminus\partial_{u}\Omega,\\
\left\llbracket\boldsymbol{\tau}\right\rrbracket\cdot\mathbf{n}=0\text{ on }J_{u},\end{cases}(21a)while taking⟦v⟧\left\llbracket v\right\rrbracketarbitrary onJuJ_{u}gives:𝝉⋅𝐧=𝗄(α)τcsgn(⟦u⟧)onJu,{\boldsymbol{\tau}}\cdot\mathbf{n}=\mathsf{k}(\alpha)\,\tau_{c}\,\text{sgn}\left(\left\llbracket u\right\rrbracket\right)\text{ on }J_{u},(21b)

where𝝉={𝝉}\boldsymbol{\tau}=\left\{\boldsymbol{\tau}\right\}onJuJ_{u}because of (21a).

## 2.4.2Optimality condition for the nonlinear deformation𝒑\boldsymbol{p}

Settingu^=u\hat{u}=u,α^=α\hat{\alpha}=\alpha, and𝒑^=𝒑+𝒒\hat{\boldsymbol{p}}=\boldsymbol{p}+\boldsymbol{q}with𝒒∈ℳ​(Ω;ℝ2)\boldsymbol{q}\in\mathcal{M}(\Omega;\mathbb{R}^{2})absolutely continuous with respect to the area measure — the singular part of𝒑\boldsymbol{p}is tied to⟦u⟧\left\llbracket u\right\rrbracketby (15) and is varied throughu^\hat{u}— the perturbed field in (20) is𝒑h:=𝒑+h​𝒒\boldsymbol{p}_{h}:=\boldsymbol{p}+h\,\boldsymbol{q}, and the first order expansion inhhleads to, for all such𝒒\boldsymbol{q},∫(Ω∖Ju)∩{‖𝒑‖>0}(−𝝉+𝗄​(α)​τc​𝒑‖𝒑‖)⋅𝒒​dA+∫(Ω∖Ju)∩{‖𝒑‖=0}(−𝝉⋅𝒒+𝗄​(α)​τc​‖𝒒‖)​dA≥0,\int_{(\Omega\setminus J_{u})\cap\{\|\boldsymbol{p}\|>0\}}\left(-\boldsymbol{\tau}+\mathsf{k}(\alpha)\,\tau_{c}\dfrac{\boldsymbol{p}}{\|\boldsymbol{p}\|}\right)\cdot\boldsymbol{q}\,\mathrm{d}A+\int_{(\Omega\setminus J_{u})\cap\{\|\boldsymbol{p}\|=0\}}\left(-\boldsymbol{\tau}\cdot{\boldsymbol{q}}+\mathsf{k}(\alpha)\,\tau_{c}{\|\boldsymbol{q}\|}\right)\,\mathrm{d}A\geq 0,(22)

where we have distinguished the subsets ofΩ∖Ju\Omega\setminus J_{u}where‖𝒑‖\|\boldsymbol{p}\|is strictly positive or vanishing to account for the non-smoothness of the energy with respect to𝒑\boldsymbol{p}.
This leads to the following pointwise optimality conditions almost everywhere inΩ∖Ju\Omega\setminus J_{u}:in​Ω∖Ju:{𝝉=𝗄​(α)​τc​𝒑‖𝒑‖where​‖𝒑‖>0‖𝝉‖≤𝗄​(α)​τcwhere​‖𝒑‖=0,\text{ in }\Omega\setminus J_{u}:\begin{cases}\boldsymbol{\tau}=\mathsf{k}(\alpha)\,\tau_{c}\dfrac{\boldsymbol{p}}{\|\boldsymbol{p}\|}&\text{ where }\|\boldsymbol{p}\|>0\\
\|\boldsymbol{\tau}\|\leq\mathsf{k}(\alpha)\,\tau_{c}&\text{ where }\|\boldsymbol{p}\|=0\end{cases},

which using that𝝉=μ​(∇u−𝒑)\boldsymbol{\tau}=\mu(\nabla u-\boldsymbol{p})can be equivalently rewritten as theflow rulefor the nonlinear deformation𝒑\boldsymbol{p}:in​Ω∖Ju:𝒑={𝟎if​‖𝝉‖=μ​‖𝜺‖≤𝗄​(α)​τc,(‖𝜺‖−𝗄​(α)​τcμ)​𝜺‖𝜺‖otherwise.\text{ in }\Omega\setminus J_{u}:\boldsymbol{p}=\begin{cases}\mathbf{0}&\text{ if }\|\boldsymbol{\tau}\|=\mu\|\boldsymbol{{\varepsilon}}\|\leq\mathsf{k}(\alpha)\,{\tau_{c}},\\
\left(\ \|\boldsymbol{{\varepsilon}}\|-\mathsf{k}(\alpha)\dfrac{\tau_{c}}{\mu}\right)\dfrac{\boldsymbol{{\varepsilon}}}{\|\boldsymbol{{\varepsilon}}\|}&\text{ otherwise.}\end{cases}(23)

## 2.4.3Optimality condition for the damage fieldα\alpha

Settingu^=u\hat{u}=u,𝒑^=𝒑\hat{\boldsymbol{p}}=\boldsymbol{p}, and perturbing the damage asαh:=α+h​(α^−α)\alpha_{h}:=\alpha+h(\hat{\alpha}-\alpha)withα^∈𝒟i\hat{\alpha}\in\mathcal{D}_{i}, the first order expansion of (20) inhhleads to,∀α^∈𝒟i\forall\hat{\alpha}\in\mathcal{D}_{i},∫Ω∖Ju((𝗄′​(α)​τc​‖𝒑‖+𝖦c4​𝖼𝗐​ℓ​𝗐′​(α))​(α^−α)+(𝖦c​ℓ2​𝖼𝗐​∇α⋅∇(α^−α)))​dA+∫Ju𝗄′(α)τc|⟦u⟧|(α^−α)ds≥0.\int_{\Omega\setminus J_{u}}\left(\left(\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}\ell}{\mathsf{w}^{\prime}(\alpha)}\right)\,(\hat{\alpha}-\alpha)+\left(\frac{\mathsf{G}_{\mathrm{c}}\ell}{2\mathsf{c_{w}}}\,\nabla\alpha\cdot\nabla(\hat{\alpha}-\alpha)\right)\right)\,\mathrm{d}A\\
+\int_{J_{u}}\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\,\left|\left\llbracket u\right\rrbracket\right|\,(\hat{\alpha}-\alpha)\,\mathrm{d}s\geq 0.

Integrating by parts the term involving∇α\nabla\alphaand rearranging, we obtain∫Ω∖Ju(𝗄′​(α)​τc​‖𝒑‖+𝖦c4​𝖼𝗐​(𝗐′​(α)ℓ−2​ℓ​Δ​α))​(α^−α)​dA+∫∂Ω∖∂αΩ𝖦c​ℓ2​𝖼𝗐∇α⋅𝐧(α^−α)ds+∫Ju(𝗄′(α)τc|⟦u⟧|−𝖦c​ℓ2​𝖼𝗐⟦∇α⟧⋅𝐧)(α^−α)ds≥0,\int_{\Omega\setminus J_{u}}\left(\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\left(\frac{\mathsf{w}^{\prime}(\alpha)}{\ell}-2\ell\,\Delta\alpha\right)\right)\,(\hat{\alpha}-\alpha)\,\mathrm{d}A\\
+\int_{\partial\Omega\setminus\partial_{\alpha}\Omega}\frac{\mathsf{G}_{\mathrm{c}}\ell}{2\mathsf{c_{w}}}\,\nabla\alpha\cdot\mathbf{n}\,(\hat{\alpha}-\alpha)\,\mathrm{d}s+\int_{J_{u}}\left(\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\,\left|\left\llbracket u\right\rrbracket\right|-\frac{\mathsf{G}_{\mathrm{c}}\ell}{2\mathsf{c_{w}}}\,\left\llbracket\nabla\alpha\right\rrbracket\cdot\mathbf{n}\right)\,(\hat{\alpha}-\alpha)\,\mathrm{d}s\geq 0,

where⟦∇α⟧⋅𝐧\left\llbracket\nabla\alpha\right\rrbracket\cdot\mathbf{n}is the jump of the normal derivative ofα\alphaacrossJuJ_{u}.
This leads to the following pointwise optimality conditions inΩ∖Ju\Omega\setminus J_{u}whereverα<1\alpha<1.on​Ω∖Ju:{α−αi−1≥0,𝗄′​(α)​τc​‖𝒑‖+𝖦c4​𝖼𝗐​(𝗐′​(α)ℓ−2​ℓ​Δ​α)≥0,(α−αi−1)​(𝗄′​(α)​τc​‖𝒑‖+𝖦c4​𝖼𝗐​(𝗐′​(α)ℓ−2​ℓ​Δ​α))=0.\text{ on }\Omega\setminus J_{u}:\begin{cases}\alpha-\alpha_{i-1}\geq 0,&\\
\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|+\dfrac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\left(\dfrac{\mathsf{w}^{\prime}(\alpha)}{\ell}-2\ell\,\Delta\alpha\right)\geq 0,&\\
\left(\alpha-\alpha_{i-1}\right)\left(\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|+\dfrac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\left(\dfrac{\mathsf{w}^{\prime}(\alpha)}{\ell}-2\ell\,\Delta\alpha\right)\right)=0.&\end{cases}(24a)with the boundary conditionα−αi−1≥0\alpha-\alpha_{i-1}\geq 0,∇α⋅𝐧≥0\nabla\alpha\cdot\mathbf{n}\geq 0and(α−αi−1)​(∇α⋅𝐧)=0(\alpha-\alpha_{i-1})(\nabla\alpha\cdot\mathbf{n})=0on∂Ω∖∂αΩ\partial\Omega\setminus\partial_{\alpha}\Omega.
On the jump setJuJ_{u}, the conditions above must be read in the sense of distributions ason​Ju:{α−αi−1≥0,𝗄′(α)τc|⟦u⟧|−𝖦c​ℓ2​𝖼𝗐⟦∇α⟧⋅𝐧≥0,(α−αi−1)(𝗄′(α)τc|⟦u⟧|−𝖦c​ℓ2​𝖼𝗐⟦∇α⟧⋅𝐧)=0.\text{ on }J_{u}:\begin{cases}\alpha-\alpha_{i-1}\geq 0,&\\
\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\,\left|\left\llbracket u\right\rrbracket\right|-\dfrac{\mathsf{G}_{\mathrm{c}}\ell}{2\mathsf{c_{w}}}\,\left\llbracket\nabla\alpha\right\rrbracket\cdot\mathbf{n}\geq 0,&\\
\left(\alpha-\alpha_{i-1}\right)\left(\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\left|\left\llbracket u\right\rrbracket\right|-\dfrac{\mathsf{G}_{\mathrm{c}}\ell}{2\mathsf{c_{w}}}\,\left\llbracket\nabla\alpha\right\rrbracket\cdot\mathbf{n}\right)=0.&\end{cases}(24b)

In the regions whereα=1\alpha=1, the necessary optimality condition reduces to the reversed inequality𝗄′​(α)​τc​‖𝒑‖+𝖦c4​𝖼𝗐​(𝗐′​(α)ℓ−2​ℓ​Δ​α)≤0,\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|+\dfrac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\left(\dfrac{\mathsf{w}^{\prime}(\alpha)}{\ell}-2\ell\,\Delta\alpha\right)\leq 0,

and similarly on the Neumann boundary and the jump setJuJ_{u}.

## Remark 3.

In the damage criterion (24a), the nonlinear deformation𝐩\boldsymbol{p}is the onlydriving forcefor damage, entering through the term𝗄′​(α)​τc​‖𝐩‖\mathsf{k}^{\prime}(\alpha)\,\tau_{c}\,\|\boldsymbol{p}\|with𝗄′​(α)<0\mathsf{k}^{\prime}(\alpha)<0. In turn, the flow rule (23) yields𝐩≠𝟎\boldsymbol{p}\neq\mathbf{0}only where the norm of the stress‖𝛕‖=μ​‖𝛆‖\|\boldsymbol{\tau}\|=\mu\|\boldsymbol{{\varepsilon}}\|exceeds the current strength𝗄​(α)​τc\mathsf{k}(\alpha)\,\tau_{c}. The two conditions combine into a stress criterion for damage nucleation: damage cannot grow until the stress attains the strength𝗄​(α)​τc\mathsf{k}(\alpha)\,\tau_{c}.

## 2.5Specific constitutive models

The properties of the model depend on the strength degradation function𝗄\mathsf{k}and the dissipation function𝗐\mathsf{w}.
We ask that they satisfy the following minimal requirements.

## Hypothesis 1(Constitutive assumption: strength degradation and dissipation function).

We assume that the strength domain degrades homothetically,i.e.𝕂​(α)=𝗄​(α)​𝕂0\mathbb{K}(\alpha)=\mathsf{k}(\alpha)\,\mathbb{K}_{0}, and that the constitutive functions𝗄:α∈[0,1]→[0,1]\mathsf{k}:\alpha\in[0,1]\to[0,1]and𝗐:α∈[0,1]→[0,1]\mathsf{w}:\alpha\in[0,1]\to[0,1]are continuous on[0,1][0,1]and differentiable on(0,1)(0,1), with𝗐′​(α)>0,𝗄′​(α)<0∀α∈(0,1),\mathsf{w}^{\prime}(\alpha)>0,\quad\mathsf{k}^{\prime}(\alpha)<0\qquad\forall{\alpha\in(0,1)},(25)

with𝗄​(0)=1\mathsf{k}(0)=1,𝗄​(1)=0\mathsf{k}(1)=0,𝗐​(0)=0\mathsf{w}(0)=0, and𝗐​(1)=1\mathsf{w}(1)=1.
We further assume the monotonicity conditions(SH):\displaystyle\textnormal{{(SH)}}:α↦𝗐′​(α)𝗄′​(α)​is strictly decreasing on(0,1),\displaystyle\alpha\mapsto\dfrac{{\mathsf{w}^{\prime}(\alpha)}}{\mathsf{k}^{\prime}(\alpha)}\ \text{is strictly decreasing on $(0,1)$},(26)(SS):\displaystyle\textnormal{{(SS)}}:α↦𝗐​(α)𝗄′​(α)​is strictly decreasing on(0,1).\displaystyle\alpha\mapsto\dfrac{\sqrt{\mathsf{w}(\alpha)}}{\mathsf{k}^{\prime}(\alpha)}\ \text{is strictly decreasing on $(0,1)$}.

When𝗄\mathsf{k}and𝗐\mathsf{w}are twice differentiable, conditions (26) take the explicit formdd​α​𝗐′​(α)𝗄′​(α)=𝗐′′​(α)​𝗄′​(α)−𝗐′​(α)​𝗄′′​(α)𝗄′​(α)2<0,dd​α​𝗐​(α)𝗄′​(α)=𝗐′​(α)​𝗄′​(α)−2​𝗐​(α)​𝗄′′​(α)2​𝗐​(α)​𝗄′​(α)2<0,∀α∈(0,1).\begin{aligned} &\dfrac{\mathrm{d}}{\mathrm{d}\alpha}\dfrac{{\mathsf{w}^{\prime}(\alpha)}}{\mathsf{k}^{\prime}(\alpha)}=\frac{\mathsf{w}^{\prime\prime}(\alpha)\mathsf{k}^{\prime}(\alpha)-\mathsf{w}^{\prime}(\alpha)\mathsf{k}^{\prime\prime}(\alpha)}{\mathsf{k}^{\prime}(\alpha)^{2}}<0,\\
&\dfrac{\mathrm{d}}{\mathrm{d}\alpha}\dfrac{\sqrt{\mathsf{w}(\alpha)}}{\mathsf{k}^{\prime}(\alpha)}=\frac{\mathsf{w}^{\prime}(\alpha)\mathsf{k}^{\prime}(\alpha)-2\,\mathsf{w}(\alpha)\mathsf{k}^{\prime\prime}(\alpha)}{2\sqrt{\mathsf{w}(\alpha)}\,\mathsf{k}^{\prime}(\alpha)^{2}}<0,\end{aligned}\qquad\forall\alpha\in(0,1).(27)

Under Hypothesis1, the model exhibitsstrain hardening(SH) in the homogeneous response andstress softening(SS) in the equivalent cohesive law, as will be shown in Sections3.1and3.2, respectively. The reader can refer to[67]for the definition of analogous conditions in the context of gradient damage models.
In the twice-differentiable case, under (25),(SS)holds whenever𝗄\mathsf{k}is convex (𝗄′′≥0\mathsf{k}^{\prime\prime}\geq 0); if in addition𝗐\mathsf{w}is convex, with𝗐′′\mathsf{w}^{\prime\prime}and𝗄′′\mathsf{k}^{\prime\prime}not simultaneously vanishing,(SH)holds as well. Convexity is however not necessary.

## 3Analysis of a simple shear problem

To investigate the behavior of the model, we consider a simple shear model problem consisting of a rectangular domainΩ=(−L/2,L/2)×(−H/2,H/2)\Omega=(-L/2,L/2)\times(-H/2,H/2)clamped on the left side and subjected to a prescribed displacementu¯\bar{u}on the right side, with free boundary conditions on the other sides and an initial undamaged stateα0=0\alpha_{0}=0.

This problem can be interpreted as a shear test on a rectangular specimen of heightHHand lengthLL.
It is the antiplane analogue of the traction test considered in[67]and related works.

In this setting, we look for families of solutions (utu_{t},𝒑t\boldsymbol{p}_{t},αt\alpha_{t}) parametrized byt>0t>0333Symmetric solutions would be obtained by consideringt<0t<0., with the imposed displacementu¯=t​L\bar{u}=t\,L.
To this end, we compute solutions of the first-order optimality conditions for the following static problem:(ut,𝒑t,αt)∈arg​minu∈𝒞t,α∈𝒟0,𝒑∈𝒫⁡ℰℓ​(u,𝒑,α),(u_{t},\boldsymbol{p}_{t},\alpha_{t})\in\operatorname*{arg\,min}_{\begin{subarray}{c}u\in\mathcal{C}_{t},\,\alpha\in\mathcal{D}_{0}\end{subarray},\,\boldsymbol{p}\in\mathcal{P}}\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha),(28)

with𝒞t\displaystyle\mathcal{C}_{t}=\displaystyle={u∈B​V​(Ω):u​(−L/2,y)=0​and​u​(L/2,y)=t​L,∀y∈(−H/2,H/2)},\displaystyle\{u\in BV(\Omega):u(-{L}/{2},y)=0\text{ and }u({L}/{2},y)=t\,L,\quad\forall y\in(-H/2,H/2)\},(29)𝒟0\displaystyle\mathcal{D}_{0}=\displaystyle={α∈H1​(Ω):0≤α≤1​in​Ω}.\displaystyle\{\alpha\in H^{1}(\Omega):0\leq\alpha\leq 1\text{ in }\Omega\}.(30)

In particular, to allow for solutions with a non-zero homogeneous damage field, we do not impose Dirichlet boundary conditions on the damage.
Moreover, we only imposeα≥0\alpha\geq 0in the construction of the solutions.
We will then check the irreversibility conditionαt≥αs\alpha_{t}\geq\alpha_{s}fort≥st\geq sa posteriori.

We will look for two classes of solutions: (i)homogeneous solutions, where the fields are constant in space, and (ii)localized solutions, where the nonlinear deformation and damage localize along a band across the specimen.
The homogeneous solutions will provide insight into the equivalent local material response and thestrength, while the localized solutions will shed light on crack nucleation and the equivalenttoughness.

In all that follows, we look for fields that are invariant along theyy-direction.
With an abuse of notation, we writeu​(x)=u​(x,0)u(x)=u(x,0)andα​(x)=α​(x,0)\alpha(x)=\alpha(x,0), and denote byε​(x)=u′​(x)\varepsilon(x)=u^{\prime}(x)the strain field, where the prime denotes the derivative with respect toxx.
The stress and nonlinear deformation fields are of the form𝝉​(x,0)=τ​(x)​e¯1\boldsymbol{\tau}(x,0)=\tau(x)\,\underline{e}_{1}and𝒑​(x,0)=p​(x)​e¯1\boldsymbol{p}(x,0)=p(x)\,\underline{e}_{1}, which defines the one-dimensional fieldsτ​(x)\tau(x)andp​(x)p(x).

## 3.1Homogeneous solutions: material response

We first investigate homogeneous solutions,i.e.solutions where the deformations, the stress and the damage fields are constant in space, which is equivalent to focusing on a material point subjected to a prescribed strain.

For the given geometry and boundary conditions, the displacement field must be of the formu​(x)=u¯​x/Lu(x)=\bar{u}\,x/L, so that the strain field isε=u¯/L=t>0{\varepsilon}=\bar{u}/L=t>0.
Mechanical equilibrium (21a) and constitutive relation (8) together with the flow rule then givep=max⁡(ε−𝗄​(α)​τcμ,0),τ=μ​(ε−p)=min⁡(μ​ε,𝗄​(α)​τc).p=\max\left({\varepsilon}-\mathsf{k}(\alpha)\dfrac{\tau_{c}}{\mu},\,0\right),\qquad\tau=\mu({\varepsilon}-p)=\min\left(\mu\,{\varepsilon},\;\mathsf{k}(\alpha)\,\tau_{c}\right).(31a)The damage criterion (24a) reduces to the following pointwise condition:τc​𝗄′​(α)​|p|+𝖦c​𝗐′​(α)4​𝖼𝗐​ℓ​{≥0if​α=0,=0if​0<α<1,≤0if​α=1.\tau_{c}\,\mathsf{k}^{\prime}(\alpha)\,|p|+\dfrac{\mathsf{G}_{\mathrm{c}}\,\mathsf{w}^{\prime}(\alpha)}{4\mathsf{c_{w}}\ell}\begin{cases}\geq 0&\text{if }\alpha=0,\\
=0&\text{if }0<\alpha<1,\\
\leq 0&\text{if }\alpha=1.\end{cases}(31b)

Since𝗄′​(0)<0\mathsf{k}^{\prime}(0)<0and𝗐′​(0)≥0\mathsf{w}^{\prime}(0)\geq 0, we get thatα=0\alpha=0as long as|p|≤pc:=−𝖦cℓ​τc​𝗐′​(0)4​𝖼𝗐​𝗄′​(0)⇔t≤εc:=τcμ−𝖦cℓ​τc​𝗐′​(0)4​𝖼𝗐​𝗄′​(0),|p|\leq p_{c}:=-\dfrac{\mathsf{G}_{\mathrm{c}}}{\ell\,\tau_{c}}\dfrac{\mathsf{w}^{\prime}(0)}{4\mathsf{c_{w}}\mathsf{k}^{\prime}(0)}\quad\Leftrightarrow\quad t\leq{\varepsilon}_{c}:=\dfrac{\tau_{c}}{\mu}-\dfrac{\mathsf{G}_{\mathrm{c}}}{\ell\,\tau_{c}}\dfrac{\mathsf{w}^{\prime}(0)}{4\mathsf{c_{w}}\mathsf{k}^{\prime}(0)},(32)

andp=0p=0as long ast≤εe:=τcμ≤εct\leq{\varepsilon}_{e}:=\frac{\tau_{c}}{\mu}\leq{\varepsilon}_{c}.

Fort>εet>{\varepsilon}_{e}, undamaged solutions are no longer admissible andα∈(0,1)\alpha\in(0,1)must satisfy the following condition obtained by combining (31b) and (31a):t=τcμ​𝗄​(α)−𝖦cτc​ℓ​𝗐′​(α)4​𝖼𝗐​𝗄′​(α).t=\dfrac{\tau_{c}}{\mu}\mathsf{k}(\alpha)-\dfrac{\mathsf{G}_{\mathrm{c}}}{\tau_{c}\ell}\dfrac{\mathsf{w}^{\prime}(\alpha)}{4\mathsf{c_{w}}\mathsf{k}^{\prime}(\alpha)}.(33)

Summarizing the above, the homogeneous response is composed of four regimes:{Elastic:t∈[0,εe),α=0,p=0,τ=μ​εConstant-stress:t∈[εe,εc),α=0,p≤pc,τ=τcStrength softening:t∈[εc,εu),α​solves(33),p=ε−𝗄​(α)​τcμ,τ=𝗄​(α)​τc,Fully damaged:t≥εu,α=1,p=ε,τ=0,\begin{cases}\text{Elastic}&:t\in[0,{\varepsilon}_{e}),\quad\alpha=0,\;p=0,\;\tau=\mu{\varepsilon}\vskip 3.0pt plus 1.0pt minus 1.0pt\\
\text{Constant-stress}&:t\in[{\varepsilon}_{e},{\varepsilon}_{c}),\quad\alpha=0,\;p\leq p_{c},\;\tau=\tau_{c}\vskip 3.0pt plus 1.0pt minus 1.0pt\\
\text{Strength softening}&:t\in[{\varepsilon}_{c},{\varepsilon}_{u}),\quad\alpha\text{ solves }\eqref{eq:elasticDomain2},\;p={\varepsilon}-\mathsf{k}(\alpha)\dfrac{\tau_{c}}{\mu},\;\tau=\mathsf{k}(\alpha)\tau_{c},\vskip 3.0pt plus 1.0pt minus 1.0pt\\
\text{Fully damaged}&:t\geq{\varepsilon}_{u},\quad\alpha=1,\quad p={\varepsilon},\quad\tau=0,\end{cases}(34)

where the critical strains are given byεe:=τcμ,εc:=τcμ−𝖦cℓ​τc​𝗐′​(0)4​𝖼𝗐​𝗄′​(0),εu:={−𝖦cτc​ℓ​𝗐′​(1)4​𝖼𝗐​𝗄′​(1),if​𝗄′​(1)<0,+∞,if​𝗄′​(1)=0,{\varepsilon}_{e}:=\dfrac{\tau_{c}}{\mu},\quad{\varepsilon}_{c}:=\dfrac{\tau_{c}}{\mu}-\dfrac{\mathsf{G}_{\mathrm{c}}}{\ell\,\tau_{c}}\dfrac{\mathsf{w}^{\prime}(0)}{4\mathsf{c_{w}}\mathsf{k}^{\prime}(0)},\quad{\varepsilon}_{u}:=\begin{cases}-\dfrac{\mathsf{G}_{\mathrm{c}}}{\tau_{c}\ell}\dfrac{\mathsf{w}^{\prime}(1)}{4\mathsf{c_{w}}\mathsf{k}^{\prime}(1)},\quad&\text{if }\mathsf{k}^{\prime}(1)<0,\\
+\infty,&\text{if }\mathsf{k}^{\prime}(1)=0,\end{cases}(35)

using the fact that𝗄​(1)=0\mathsf{k}(1)=0.

Note that (33) admits a unique solutionα​(t)\alpha(t)satisfying the irreversibility condition if and only if its right-hand side is an increasing function ofα\alpha, and that a snap-back occurs otherwise.
Assuming that𝗐′/𝗄′\mathsf{w}^{\prime}/\mathsf{k}^{\prime}is differentiable, this implies thatτcμ​𝗄′​(α)−𝖦cτc​ℓ​14​𝖼𝗐​dd​α​(𝗐′​(α)𝗄′​(α))>0\frac{\tau_{c}}{\mu}\mathsf{k}^{\prime}(\alpha)-\frac{\mathsf{G}_{\mathrm{c}}}{\tau_{c}\ell}\frac{1}{4\mathsf{c_{w}}}\frac{\mathrm{d}}{\mathrm{d}\alpha}\left(\frac{\mathsf{w}^{\prime}(\alpha)}{\mathsf{k}^{\prime}(\alpha)}\right)>0

almost everywhere on(0,1)(0,1).
We rewrite this condition asℓℓch<14​𝖼𝗐​𝗄′​(α)​dd​α​(𝗐′​(α)𝗄′​(α)),\frac{\ell}{\ell_{\mathrm{ch}}}<\frac{1}{4\mathsf{c_{w}}\mathsf{k}^{\prime}(\alpha)}\frac{\mathrm{d}}{\mathrm{d}\alpha}\left(\frac{\mathsf{w}^{\prime}(\alpha)}{\mathsf{k}^{\prime}(\alpha)}\right),(36)

withℓch:=μ​𝖦cτc2\ell_{\mathrm{ch}}:=\frac{\mu\mathsf{G}_{\mathrm{c}}}{\tau^{2}_{c}}denoting theelasto-cohesive lengthof the material, the antiplane analogue of Hillerborg’s characteristic length[42].
A necessary (but not sufficient) condition is thatdd​α​(𝗐′​(α)𝗄′​(α))<0\frac{\mathrm{d}}{\mathrm{d}\alpha}\left(\frac{\mathsf{w}^{\prime}(\alpha)}{\mathsf{k}^{\prime}(\alpha)}\right)<0, which is hypothesis(SH)in (26).

## Remark 4(Snap-back and convexity of the bulk energy density at given strain).

In the strength-softening regime, we have𝛆−p=𝗄​(α)​τcμ\boldsymbol{{\varepsilon}}-p=\mathsf{k}(\alpha)\frac{\tau_{c}}{\mu}so that the total energy density isW​(ε,α):=ψ​(ε,α)+𝖦c4​𝖼𝗐​ℓ​𝗐​(α)=𝗄​(α)​τc​ε−𝗄​(α)2​τc22​μ+𝖦c4​𝖼𝗐​ℓ​𝗐​(α).W({\varepsilon},\alpha):=\psi({\varepsilon},\alpha)+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}\ell}\mathsf{w}(\alpha)=\mathsf{k}(\alpha)\,\tau_{c}\,{\varepsilon}-\frac{\mathsf{k}(\alpha)^{2}\tau_{c}^{2}}{2\mu}+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}\ell}\mathsf{w}(\alpha).

Differentiating with respect toα\alphafor a fixed𝛆\boldsymbol{{\varepsilon}}and noticing that∂p∂α=−𝗄′​(α)​τcμ\frac{\partial p}{\partial\alpha}=-\mathsf{k}^{\prime}(\alpha)\frac{\tau_{c}}{\mu}, we get that∂W∂α​(𝜺,α)=𝗄′​(α)​τc​p+𝖦c4​𝖼𝗐​ℓ​𝗐′​(α),\frac{\partial W}{\partial\alpha}(\boldsymbol{{\varepsilon}},\alpha)=\mathsf{k}^{\prime}(\alpha)\tau_{c}p+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}\ell}\mathsf{w}^{\prime}(\alpha),

and∂2W∂α2​(𝜺,α)=𝗄′′​(α)​τc​p−𝗄′​(α)2​τc2μ+𝖦c4​𝖼𝗐​ℓ​𝗐′′​(α).\frac{\partial^{2}W}{\partial\alpha^{2}}(\boldsymbol{{\varepsilon}},\alpha)=\mathsf{k}^{\prime\prime}(\alpha)\tau_{c}p-\frac{\mathsf{k}^{\prime}(\alpha)^{2}\tau_{c}^{2}}{\mu}+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}\ell}\mathsf{w}^{\prime\prime}(\alpha).

Substituting𝗐′′=𝗄′′​𝗐′/𝗄′+𝗄′​dd​α​(𝗐′/𝗄′)\mathsf{w}^{\prime\prime}=\mathsf{k}^{\prime\prime}\mathsf{w}^{\prime}/\mathsf{k}^{\prime}+\mathsf{k}^{\prime}\,\tfrac{\mathrm{d}}{\mathrm{d}\alpha}(\mathsf{w}^{\prime}/\mathsf{k}^{\prime}), and using the fact that since0<α<10<\alpha<1, optimality with respect toα\alphaimplies that∂W∂α​(𝛆,α)=0\frac{\partial W}{\partial\alpha}(\boldsymbol{{\varepsilon}},\alpha)=0, we can obtain that∂2W​(𝜺,α)∂α2\displaystyle\frac{\partial^{2}W(\boldsymbol{{\varepsilon}},\alpha)}{\partial\alpha^{2}}=𝖦c4​𝖼𝗐​ℓ​𝗄′​(α)​dd​α​(𝗐′​(α)𝗄′​(α))−τc2​𝗄′​(α)2μ\displaystyle=\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}\ell}\mathsf{k}^{\prime}(\alpha)\frac{\mathrm{d}}{\mathrm{d}\alpha}\left(\frac{\mathsf{w}^{\prime}(\alpha)}{\mathsf{k}^{\prime}(\alpha)}\right)-\frac{\tau_{c}^{2}\mathsf{k}^{\prime}(\alpha)^{2}}{\mu}(37)=𝗄′​(α)2​𝖦cℓ​(14​𝖼𝗐​𝗄′​(α)​dd​α​(𝗐′​(α)𝗄′​(α))−ℓℓch)\displaystyle=\frac{\mathsf{k}^{\prime}(\alpha)^{2}\mathsf{G}_{\mathrm{c}}}{\ell}\left(\frac{1}{4\mathsf{c_{w}}\mathsf{k}^{\prime}(\alpha)}\frac{\mathrm{d}}{\mathrm{d}\alpha}\left(\frac{\mathsf{w}^{\prime}(\alpha)}{\mathsf{k}^{\prime}(\alpha)}\right)-\frac{\ell}{\ell_{\mathrm{ch}}}\right)

so that condition (36) is equivalent to the strict convexity of the total energy with respect toα\alphain the strength softening phase.
It is also equivalent to mandating a negative tangential stiffness,d​τd​t<0\frac{\mathrm{d}\tau}{\mathrm{d}t}<0.

Note that (37) can be seen as the outcome of the competition between elastic softeningτc2​𝗄′​(α)2/μ{\tau_{c}^{2}\mathsf{k}^{\prime}(\alpha)^{2}/\mu}, which is always destabilizing, and strain hardening𝖦c4​𝖼𝗐​ℓ​𝗄′​(α)​dd​α​(𝗐′​(α)𝗄′​(α))\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}\ell}\mathsf{k}^{\prime}(\alpha)\frac{\mathrm{d}}{\mathrm{d}\alpha}\left(\frac{\mathsf{w}^{\prime}(\alpha)}{\mathsf{k}^{\prime}(\alpha)}\right).

## 3.2Localized solutions: equivalent cohesive law

Assume now that the damage fieldα​(x)\alpha(x)is not constant in space and attains a maximumα∗\alpha^{*}at a single pointx∗∈(−L/2,L/2)x^{*}\in(-L/2,L/2).
In this setting, mechanical equilibrium implies that the shear stressτ​(x)\tau(x)must be constant in space:τ=μ​(ε​(x)−p​(x))=constant.\tau=\mu\left({\varepsilon}(x)-p(x)\right)=\text{constant}.(38)

Thestrength criterionwith𝗄′​(α)<0\mathsf{k}^{\prime}(\alpha)<0andα∗>0\alpha^{*}>0implies thatτ≤𝗄​(α∗)​τc<τc,τ≤𝗄​(α∗)​τc<𝗄​(α​(x))​τc,∀x≠x∗,\tau\leq\mathsf{k}(\alpha^{*})\tau_{c}<\tau_{c},\qquad\tau\leq\mathsf{k}(\alpha^{*})\tau_{c}<\mathsf{k}(\alpha(x))\tau_{c},\quad\forall x\neq x^{*},(39)

since𝗄\mathsf{k}is decreasing andα​(x)<α∗\alpha(x)<\alpha^{*}forx≠x∗x\neq x^{*}.
Because of the flow rule (23), the nonlinear strainp​(x)p(x)can be non-zero only atx=x∗x=x^{*}whereτ≤𝗄​(α∗)​τc\tau\leq\mathsf{k}(\alpha^{*})\tau_{c}, whileτ<𝗄​(α​(x))​τc\tau<\mathsf{k}(\alpha(x))\tau_{c}everywhere else.
Moreover, the displacement field must verify theloading condition:t=u​(L/2)−u​(−L/2)L=1L​∫−L/2L/2ε​(x)​dx=1L​∫−L/2L/2(τμ+p​(x))​dx=τμ+⟦u⟧L,t=\frac{u(L/2)-u(-L/2)}{L}=\frac{1}{L}\int_{-L/2}^{L/2}{\varepsilon}(x)\,\mathrm{d}x=\frac{1}{L}\int_{-L/2}^{L/2}\left(\frac{\tau}{\mu}+p(x)\right)\,\mathrm{d}x=\frac{\tau}{\mu}+\frac{\left\llbracket u\right\rrbracket}{L},(40)

where we used the fact thatp=0p=0for allx≠x∗x\neq x^{*}and that (15) mandates that⟦u⟧(x∗)=pS(x∗)≠0\left\llbracket u\right\rrbracket(x^{*})=p^{S}(x^{*})\not=0,i.e.that the regular part ofppis identically zero andp(x)=pS(x)=⟦u⟧δx∗(x),p(x)=p^{S}(x)=\left\llbracket u\right\rrbracket\,\delta_{x^{*}}(x),(41)

whereδx∗\delta_{x^{*}}is the Dirac delta distribution centered atx=x∗x=x^{*}.
Normalizing the load byεe{\varepsilon}_{e}, the loading condition above readst/εe=τ/τc+(⟦u⟧τc/𝖦c)(ℓch/L)t/{\varepsilon}_{e}=\tau/\tau_{c}+\left(\left\llbracket u\right\rrbracket\,\tau_{c}/\mathsf{G}_{\mathrm{c}}\right)\,(\ell_{\mathrm{ch}}/L), so that the global response of the bar depends on the brittleness ratioL/ℓchL/\ell_{\mathrm{ch}}alone.

In theregular regionsx∈(−L/2,x∗)∪(x∗,L/2)x\in(-L/2,x^{*})\cup(x^{*},L/2), whereα​(x)<α∗≤1\alpha(x)<\alpha^{*}\leq 1is smooth andp​(x)=0p(x)=0, the damage criterion reduces toα​(x)≥0,𝗐′​(α​(x))−2​ℓ2​α′′​(x)≥0,(𝗐′​(α​(x))−2​ℓ2​α′′​(x))​α​(x)=0.\alpha(x)\geq 0,\quad\mathsf{w}^{\prime}(\alpha(x))-2\ell^{2}\,\alpha^{\prime\prime}(x)\geq 0,\quad\left(\mathsf{w}^{\prime}(\alpha(x))-2\ell^{2}\,\alpha^{\prime\prime}(x)\right)\alpha(x)=0.(42)

The solution of this problem is classical in phase-field fracture models[67, seee.g.].
Since by regularity, either𝗐′​(α​(x))=2​ℓ2​α′′​(x)\mathsf{w}^{\prime}(\alpha(x))=2\ell^{2}\,\alpha^{\prime\prime}(x)orα​(x)=α′​(x)=0\alpha(x)=\alpha^{\prime}(x)=0forx≠x∗x\neq x^{*},(𝗐′​(α​(x))−2​ℓ2​α′′​(x))​α′​(x)=0\left(\mathsf{w}^{\prime}(\alpha(x))-2\ell^{2}\,\alpha^{\prime\prime}(x)\right)\alpha^{\prime}(x)=0

holds everywhere in the regular regions, which yields the first integralℓ2​α′​(x)2=𝗐​(α​(x))−c0,∀x∈(−L/2,x∗)∪(x∗,L/2),\ell^{2}\,\alpha^{\prime}(x)^{2}={\mathsf{w}(\alpha(x))}-c_{0},\quad\forall x\in(-L/2,x^{*})\cup(x^{*},L/2),(43)

which is nothing but theoptimal profileproblem for the Ambrosio–Tortorelli surface energy term (see[58]for instance).
We look for solutions where the damage is non-zero only in an interval of widthD<LD<Lcentered atx=x∗x=x^{*}, withα​(x)=0\alpha(x)=0for|x−x∗|≥D/2|x-x^{*}|\geq D/2.
For such solutions, the constantc0c_{0}can be computed in the region whereα=0\alpha=0, givingc0=0c_{0}=0.
Hence, the integration of (43) provides the profile ofα​(x)\alpha(x)in the regular regions and the width of the damaged interval:|x−x∗|=ℓ​∫α​(x)α∗d​α𝗐​(α),D​(α∗)=2​ℓ​∫0α∗d​α𝗐​(α).|x-x^{*}|=\ell\int^{\alpha^{*}}_{\alpha(x)}\frac{\,\mathrm{d}\alpha}{\sqrt{\mathsf{w}(\alpha)}},\quad D(\alpha^{*})=2\ell\int^{\alpha^{*}}_{0}\frac{\,\mathrm{d}\alpha}{\sqrt{\mathsf{w}(\alpha)}}.(44)

The widthD​(α∗)D(\alpha^{*})is finite if and only if∫0dα/𝗐​(α)<∞\int_{0}\mathrm{d}\alpha/\sqrt{\mathsf{w}(\alpha)}<\infty,i.e.if𝗐′​(0)>0\mathsf{w}^{\prime}(0)>0.
When𝗐′​(0)=0\mathsf{w}^{\prime}(0)=0, as for the model𝖬𝟣\mathsf{M1}withζ=1\zeta=1, the optimal profile has unbounded support with exponential tails of width of orderℓ\ell, andc0=0c_{0}=0holds only in the limitL/ℓ→∞L/\ell\to\infty; the closed-form expressions below remain valid up to corrections of ordere−L/ℓe^{-L/\ell}, negligible for the values ofL/ℓL/\ellused in Section6.

At the displacement jumpx=x∗x=x^{*}, whereα​(x∗)=α∗>0\alpha(x^{*})=\alpha^{*}>0by hypothesis, the damage criterion reads as𝗄′(α∗)τc⟦u⟧−𝖦c​ℓ2​𝖼𝗐⟦α′⟧=0\mathsf{k}^{\prime}(\alpha^{*})\tau_{c}\,\left\llbracket u\right\rrbracket-\frac{\mathsf{G}_{\mathrm{c}}\ell}{2\mathsf{c_{w}}}\left\llbracket\alpha^{\prime}\right\rrbracket=0(45)

while the first integral (43) givesℓ⟦α′⟧=−2𝗐​(α∗).\ell\,\left\llbracket\alpha^{\prime}\right\rrbracket=-2\sqrt{\mathsf{w}(\alpha^{*})}.(46)

Eliminating⟦α′⟧\left\llbracket\alpha^{\prime}\right\rrbracketfrom (45)–(46), the flow rule atx=x∗x=x^{*}gives the followingcohesive lawrelating the stressτ\tauto the displacement jump⟦u⟧\left\llbracket u\right\rrbracketatx=x∗x=x^{*}, parametrized via the maximal damage valueα∗\alpha^{*}:τ=𝗄(α∗)τc,with⟦u⟧=−𝖦c𝖼𝗐​τc𝗐​(α∗)𝗄′​(α∗).\tau=\mathsf{k}(\alpha^{*})\tau_{c},\quad\text{with}\quad{\left\llbracket u\right\rrbracket}=-\frac{\mathsf{G}_{\mathrm{c}}}{\mathsf{c_{w}}\tau_{c}}\frac{\sqrt{\mathsf{w}(\alpha^{*})}}{\mathsf{k}^{\prime}(\alpha^{*})}.(47)

The global force-displacement response of the bar can then be obtained by combining the cohesive law (47) with the loading condition:t=τμ+⟦u⟧L=𝗄​(α∗)​τcμ−1L​𝖦c𝖼𝗐​τc​𝗐​(α∗)𝗄′​(α∗).t=\frac{\tau}{\mu}+\frac{\left\llbracket u\right\rrbracket}{L}=\frac{\mathsf{k}(\alpha^{*})\tau_{c}}{\mu}-\frac{1}{L}\frac{\mathsf{G}_{\mathrm{c}}}{\mathsf{c_{w}}\tau_{c}}\frac{\sqrt{\mathsf{w}(\alpha^{*})}}{\mathsf{k}^{\prime}(\alpha^{*})}.(48)

Again, (48) admits a unique solution satisfying the irreversibility condition if and only if its right-hand side is an increasing function ofα∗\alpha^{*}.
Assuming again that𝗐/𝗄′\sqrt{\mathsf{w}}/\mathsf{k}^{\prime}is differentiable, this implies that𝗄′​(α∗)​τcμ−1L​𝖦c𝖼𝗐​τc​dd​α∗​𝗐​(α∗)𝗄′​(α∗)>0\frac{\mathsf{k}^{\prime}(\alpha^{*})\,\tau_{c}}{\mu}-\frac{1}{L}\frac{\mathsf{G}_{\mathrm{c}}}{\mathsf{c_{w}}\tau_{c}}\frac{\mathrm{d}}{{\mathrm{d}}\alpha^{*}}\frac{\sqrt{\mathsf{w}(\alpha^{*})}}{\mathsf{k}^{\prime}(\alpha^{*})}>0

or equivalently thatLℓch<1𝖼𝗐​𝗄′​(α∗)​dd​α∗​(𝗐​(α∗)𝗄′​(α∗)).\frac{L}{\ell_{\mathrm{ch}}}<\frac{1}{\mathsf{c_{w}}\mathsf{k}^{\prime}(\alpha^{*})}\frac{\mathrm{d}}{\mathrm{d}\alpha^{*}}\left(\frac{\sqrt{\mathsf{w}(\alpha^{*})}}{\mathsf{k}^{\prime}(\alpha^{*})}\right).(49)

As in the homogeneous response case, a necessary (but not sufficient) condition for (49) is thatdd​α∗​(𝗐​(α∗)𝗄′​(α∗))<0\frac{\mathrm{d}}{\mathrm{d}\alpha^{*}}\left(\frac{\sqrt{\mathsf{w}(\alpha^{*})}}{\mathsf{k}^{\prime}(\alpha^{*})}\right)<0, which is the stress softening hypothesis (SS).

## Cohesive surface energy

Because the nonlinear deformation is concentrated atx∗x^{*}and the damage profile is determined byα∗\alpha^{*}through (44), the energy of the localized solution splits, per unit length in theyy-direction, into one term coming from the bulk and two surface contributions:ℰ(⟦u⟧,α∗)=μ​L2(t−⟦u⟧L)2+ϕ(⟦u⟧,α∗),\mathcal{E}(\left\llbracket u\right\rrbracket,\alpha^{*})=\frac{\mu\,L}{2}\left(t-\frac{\left\llbracket u\right\rrbracket}{L}\right)^{2}+\phi(\left\llbracket u\right\rrbracket,\alpha^{*}),(50)

the first term being the elastic energy of the bar, whose elastic strainε−p=t−⟦u⟧/L=τ/μ{\varepsilon}-p=t-\left\llbracket u\right\rrbracket/L=\tau/\muis uniform.
Writingδ:=⟦u⟧\delta:=\left\llbracket u\right\rrbracketfor the opening, we further decompose the surface term in an elastic and a dissipated part, as in (5):ϕ​(δ,α∗)=𝗄​(α∗)​τc​δ⏟ϕcoh+𝖦c​α^​(α∗)⏟ϕdmg,withα^​(α∗)=1𝖼𝗐​∫0α∗𝗐​(β)​dβ.\phi(\delta,\alpha^{*})=\underbrace{\mathsf{k}(\alpha^{*})\,\tau_{c}\,\delta}_{\textstyle\phi_{\mathrm{coh}}}+\underbrace{\mathsf{G}_{\mathrm{c}}\,\hat{\alpha}(\alpha^{*})}_{\textstyle\phi_{\mathrm{dmg}}},\qquad{\text{with}}\qquad\hat{\alpha}(\alpha^{*})=\dfrac{1}{\mathsf{c_{w}}}\int_{0}^{\alpha^{*}}\sqrt{\mathsf{w}(\beta)}\,\mathrm{d}\beta.(51)

This is precisely the surface energy density (5) of the conjectured limit cohesive model, here parametrized byα∗\alpha^{*}rather than byα^=α^​(α∗)\hat{\alpha}=\hat{\alpha}(\alpha^{*}); in particular, it depends neither on the regularization lengthℓ\ellnor on the shear modulusμ\mu.

## Qualitative properties of the surface energy and of the traction law

Theeffective surface energyΦ​(δ)\Phi(\delta)of a cohesive crack and the associatedtraction lawτ​(δ)\tau(\delta)are obtained by minimizing the surface energy density (51) with respect toα∗\alpha^{*}at fixed openingδ\delta:Φ​(δ):=minα∗∈[0,1]⁡ϕ​(δ,α∗)=minα^∈[0,1]⁡(𝗄^​(α^)​τc​δ+𝖦c​α^),τ​(δ):=𝗄​(α∗​(δ))​τc,\Phi(\delta):=\min_{\alpha^{*}\in[0,1]}\phi(\delta,\alpha^{*})=\min_{\hat{\alpha}\in[0,1]}\Big(\hat{\mathsf{k}}(\hat{\alpha})\,\tau_{c}\,\delta+\mathsf{G}_{\mathrm{c}}\,\hat{\alpha}\Big),\qquad\tau(\delta):=\mathsf{k}\big(\alpha^{*}(\delta)\big)\,\tau_{c},(52)

whereα∗​(δ)\alpha^{*}(\delta)denotes the minimizer.
The stationarity condition ofϕ\phiwith respect toα∗\alpha^{*}at fixedδ\delta,∂ϕ∂α​(δ,α∗)=𝗄′​(α∗)​τc​δ+𝖦c𝖼𝗐​𝗐​(α∗)=0,\frac{\partial\phi}{\partial\alpha}(\delta,\alpha^{*})=\mathsf{k}^{\prime}(\alpha^{*})\,\tau_{c}\,\delta+\frac{\mathsf{G}_{\mathrm{c}}}{\mathsf{c_{w}}}\sqrt{\mathsf{w}(\alpha^{*})}=0,(53)

is precisely the damage criterion (45) on the jump set combined with the first integral (46), and its solutionα∗=α∗​(δ)\alpha^{*}=\alpha^{*}(\delta)is the cohesive law (47).
Under(SS)the mapα^↦ϕ​(δ,α^)\hat{\alpha}\mapsto\phi(\delta,\hat{\alpha})is convex, so the minimizer in (52) isα^=0\hat{\alpha}=0forδ≤δ0\delta\leq\delta_{0}, the interior stationary point (53) forδ0<δ<δu\delta_{0}<\delta<\delta_{u}, andα^=1\hat{\alpha}=1forδ≥δu\delta\geq\delta_{u}, withδ0:=−𝖦cτc​𝗄^′​(0+)≥0,δu:=−𝖦cτc​𝗄^′​(1−).\delta_{0}:=-\frac{\mathsf{G}_{\mathrm{c}}}{\tau_{c}\,\hat{\mathsf{k}}^{\prime}(0^{+})}\geq 0,\qquad\delta_{u}:=-\frac{\mathsf{G}_{\mathrm{c}}}{\tau_{c}\,\hat{\mathsf{k}}^{\prime}(1^{-})}.(54)

Since𝗄^′​(α^)=𝖼𝗐​𝗄′​(α)/𝗐​(α)\hat{\mathsf{k}}^{\prime}(\hat{\alpha})=\mathsf{c_{w}}\,\mathsf{k}^{\prime}(\alpha)/\sqrt{\mathsf{w}(\alpha)}, one hasδ0=0\delta_{0}=0whenever𝗐​(α)/|𝗄′​(α)|→0\sqrt{\mathsf{w}(\alpha)}/|\mathsf{k}^{\prime}(\alpha)|\to 0asα→0+\alpha\to 0^{+}, and the cohesive branch then emanates from the origin.
A finite𝗄^′​(0+)\hat{\mathsf{k}}^{\prime}(0^{+}), which Hypothesis1does not exclude, gives insteadδ0>0\delta_{0}>0and an initial Dugdale-like plateauτ≡τc\tau\equiv\tau_{c}on[0,δ0][0,\delta_{0}].
Three properties follow, for every admissible pair(𝗄,𝗐)(\mathsf{k},\mathsf{w}).

(i)Φ\Phiis concave.It is the infimum of a family of affine functions ofδ\delta. ConsequentlyΦ\Phidepends on𝗄^\hat{\mathsf{k}}only through its convex envelope, and(SS), which is exactly the convexity of𝗄^\hat{\mathsf{k}}, see Remark7, is the condition under which the entire branch parametrized byα∗\alpha^{*}is attained, so that the cohesive law is single-valued.

(ii) The traction law is the derivative of the surface energy.By the envelope theorem,Φ′​(δ)=∂ϕ/∂δ=𝗄​(α∗​(δ))​τc=τ​(δ)\Phi^{\prime}(\delta)=\partial\phi/\partial\delta=\mathsf{k}(\alpha^{*}(\delta))\,\tau_{c}=\tau(\delta), whenceΦ​(δ)=∫0δτ​(s)​ds,d​τd​δ=Φ′′​(δ)=τc2​𝗄^′​(α^)3𝖦c​𝗄^′′​(α^)≤0\Phi(\delta)=\int_{0}^{\delta}\tau(s)\,\mathrm{d}s,\qquad\frac{\mathrm{d}\tau}{\mathrm{d}\delta}=\Phi^{\prime\prime}(\delta)=\frac{\tau_{c}^{2}\,\hat{\mathsf{k}}^{\prime}(\hat{\alpha})^{3}}{\mathsf{G}_{\mathrm{c}}\,\hat{\mathsf{k}}^{\prime\prime}(\hat{\alpha})}\leq 0(55)

on the softening branch, the last identity following from the second derivative (59) ofϕ\phicomputed in Remark7:
the surface energy is the area under the traction–separation law, and concavity ofΦ\Phiis the softening ofτ\tau.

(iii) Strength and toughness are the only material constants.Since𝗄​(0)=1\mathsf{k}(0)=1, the traction starts atτ​(0+)=τc\tau(0^{+})=\tau_{c}; complete decohesion is reached atα∗=1\alpha^{*}=1, that is at the openingδu\delta_{u}of (54), which in terms of(𝗄,𝗐)(\mathsf{k},\mathsf{w})readsδu=−𝖦c𝖼𝗐​τc​𝗄′​(1)∈(0,+∞],\delta_{u}=-\frac{\mathsf{G}_{\mathrm{c}}}{\mathsf{c_{w}}\,\tau_{c}\,\mathsf{k}^{\prime}(1)}\in(0,+\infty],(56)

using𝗐​(1)=1\mathsf{w}(1)=1; it is finite if𝗄′​(1)<0\mathsf{k}^{\prime}(1)<0and infinite if𝗄′​(1)=0\mathsf{k}^{\prime}(1)=0. Thereτ​(δu)=0\tau(\delta_{u})=0andΦ​(δu)=𝖦c\Phi(\delta_{u})=\mathsf{G}_{\mathrm{c}}; beyond itτ≡0\tau\equiv 0andΦ≡𝖦c\Phi\equiv\mathsf{G}_{\mathrm{c}}.

HenceΦ\Phiis a Barenblatt-type cohesive energy: increasing, concave, vanishing at the origin, with initial slope thestrengthτc\tau_{c}and plateau thetoughness𝖦c\mathsf{G}_{\mathrm{c}},Φ​(0)=0,Φ′​(0+)=τc,Φ​(δ)≤min⁡(τc​δ,𝖦c),∫0δuτ​(s)​ds=𝖦c,\Phi(0)=0,\qquad\Phi^{\prime}(0^{+})=\tau_{c},\qquad\Phi(\delta)\leq\min\left(\tau_{c}\,\delta,\;\mathsf{G}_{\mathrm{c}}\right),\qquad\int_{0}^{\delta_{u}}\tau(s)\,\mathrm{d}s=\mathsf{G}_{\mathrm{c}},(57)

the last two bounds following from (52) by testing withα^=0\hat{\alpha}=0andα^=1\hat{\alpha}=1.
Both constants are inherited from the regularized model independently ofℓ\ellandμ\mu, while the shape ofτ​(δ)\tau(\delta)in between is set by the pair(𝗄,𝗐)(\mathsf{k},\mathsf{w}); the Griffith model[40]is recovered in the limitδu→0\delta_{u}\to 0.

## Remark 5.

A stronger condition ensuring that (49) is satisfied isL<Lc:=ℓch𝖼𝗐​infα∈(0,1)(1|𝗄′​(α)|​dd​α​𝗐​(α)|𝗄′​(α)|).L<L_{c}:=\frac{\ell_{\mathrm{ch}}}{\mathsf{c_{w}}}\inf_{\alpha\in(0,1)}\left(\frac{1}{|\mathsf{k}^{\prime}(\alpha)|}\frac{\mathrm{d}}{\mathrm{d}\alpha}\frac{\sqrt{\mathsf{w}(\alpha)}}{|\mathsf{k}^{\prime}(\alpha)|}\right).(58)

## Remark 6(Elastic and dissipated part of the surface energy).

The two contributions to the surface energy (51) are of different nature.
The damage termϕdmg=𝖦c​α^​(α∗)\phi_{\mathrm{dmg}}=\mathsf{G}_{\mathrm{c}}\,\hat{\alpha}(\alpha^{*})is dissipated, damage being irreversible.
The cohesive termϕcoh=τ​δ\phi_{\mathrm{coh}}=\tau\,\deltais instead a state function of(δ,α∗)(\delta,\alpha^{*}): since the present formulation enforces no irreversibility condition on the nonlinear deformation (Remark1),𝐩\boldsymbol{p}is reversible andϕcoh\phi_{\mathrm{coh}}is entirely recovered upon unloading at frozen damage, so that onlyϕdmg\phi_{\mathrm{dmg}}is dissipated.
If instead𝐩\boldsymbol{p}is assumed irreversible, the work spent in the band is dissipated incrementally,∫𝗄​(α∗)​τc​dp¯\int\mathsf{k}(\alpha^{*})\,\tau_{c}\,\mathrm{d}\bar{p}, and not through the state functionτ​δ\tau\,\delta; along the cohesive branch it accumulates to∫0δτ​(s)​ds=ϕcoh+ϕdmg\int_{0}^{\delta}\tau(s)\,\mathrm{d}s=\phi_{\mathrm{coh}}+\phi_{\mathrm{dmg}}by (55), so that the whole surface energyϕ\phiis dissipated,ϕdmg\phi_{\mathrm{dmg}}being already included in it.
The two conventions differ only away from complete decohesion: asα∗→1\alpha^{*}\to 1the traction vanishes,ϕcoh→0\phi_{\mathrm{coh}}\to 0, and both giveϕ→𝖦c\phi\to\mathsf{G}_{\mathrm{c}}, in agreement with (57).
In the notation of Section6the bulk term of (50) isEelE_{\mathrm{el}}, whileϕcoh=Epl\phi_{\mathrm{coh}}=E_{\mathrm{pl}}andϕdmg=Edmg\phi_{\mathrm{dmg}}=E_{\mathrm{dmg}}; the energy plots of the bar report the bulk term aselasticand the whole surface energyϕ\phiasdissipated.

## Remark 7(Stress softening as convexity of the surface energy).

Differentiating (53) once more at fixed opening and evaluating the resultalong the cohesive branch,i.e.substitutingτc​δ=−𝖦c𝖼𝗐​𝗐​(α∗)/𝗄′​(α∗)\tau_{c}\,\delta=-\tfrac{\mathsf{G}_{\mathrm{c}}}{\mathsf{c_{w}}}\sqrt{\mathsf{w}(\alpha^{*})}/\mathsf{k}^{\prime}(\alpha^{*})into∂α∗​α∗2ϕ=𝗄′′​(α∗)​τc​δ+𝖦c𝖼𝗐​𝗐′​(α∗)2​𝗐​(α∗)\partial^{2}_{\alpha^{*}\alpha^{*}}\phi=\mathsf{k}^{\prime\prime}(\alpha^{*})\,\tau_{c}\,\delta+\tfrac{\mathsf{G}_{\mathrm{c}}}{\mathsf{c_{w}}}\tfrac{\mathsf{w}^{\prime}(\alpha^{*})}{2\sqrt{\mathsf{w}(\alpha^{*})}}, gives∂2ϕ∂α∗2|δ=𝖦c𝖼𝗐​𝗄′​(α∗)​dd​α∗​(𝗐​(α∗)𝗄′​(α∗))>0⟺(SS),\frac{\partial^{2}\phi}{\partial{\alpha^{*}}^{2}}\bigg|_{\delta}=\frac{\mathsf{G}_{\mathrm{c}}}{\mathsf{c_{w}}}\,\mathsf{k}^{\prime}(\alpha^{*})\,\frac{\mathrm{d}}{\mathrm{d}\alpha^{*}}\left(\frac{\sqrt{\mathsf{w}(\alpha^{*})}}{\mathsf{k}^{\prime}(\alpha^{*})}\right)>0\quad\Longleftrightarrow\quad\textnormal{{(SS)}},(59)

since𝗄′<0\mathsf{k}^{\prime}<0. The statement is sharper in the intrinsic damage variableα^\hat{\alpha}, in which the
dissipation is linear,ϕ=𝗄^​(α^)​τc​δ+𝖦c​α^\phi=\hat{\mathsf{k}}(\hat{\alpha})\,\tau_{c}\,\delta+\mathsf{G}_{\mathrm{c}}\,\hat{\alpha}, so that∂α^​α^2ϕ|δ=𝗄^′′​(α^)​τc​δ\partial^{2}_{\hat{\alpha}\hat{\alpha}}\phi\big|_{\delta}=\hat{\mathsf{k}}^{\prime\prime}(\hat{\alpha})\,\tau_{c}\,\delta:
condition(SS)is exactly the convexity of𝗄^\hat{\mathsf{k}}, hence the strict
convexity ofϕ​(δ,⋅)\phi(\delta,\cdot)inα^\hat{\alpha}foreveryδ>0\delta>0. (In the variableα∗\alpha^{*}, instead, (59) holds only along the branch, andϕ​(δ,⋅)\phi(\delta,\cdot)need not be convex.)
By the envelope relationdτ/d⟦u⟧=−(𝗄′(α∗)τc)2/∂α∗​α∗2ϕ\mathrm{d}\tau/\mathrm{d}\left\llbracket u\right\rrbracket=-\left(\mathsf{k}^{\prime}(\alpha^{*})\,\tau_{c}\right)^{2}\big/\,\partial^{2}_{\alpha^{*}\alpha^{*}}\phi, this is in turn equivalent to a strictly softening cohesive law,
which motivates the name of the condition.

In contrast with the homogeneous case (37), no destabilizing elastic term
appears and the equivalence holds for everyμ\muandℓ\ell: at the jump point the opening fixes the
singular part of𝐩\boldsymbol{p}directly, cf. (41), whereas in the bulk the
splitp=ε−𝗄​(α)​τc/μp={\varepsilon}-\mathsf{k}(\alpha)\tau_{c}/\mushifts withα\alphaand produces the elastic softening term−τc2​𝗄′​(α)2/μ-\tau_{c}^{2}\mathsf{k}^{\prime}(\alpha)^{2}/\mu. The elastic energy stored in the bulk enters only through the structural
coupling with the rest of the bar: eliminatingδ\deltaat fixedttin the total energy (50),
which adds toϕ\phithe bulk contributionμ2​L​(t​L−δ)2\tfrac{\mu}{2L}(tL-\delta)^{2}, one obtains, along the branch,d2​ℰd​α∗2|t=𝗄′​(α∗)2​𝖦c​(1𝖼𝗐​𝗄′​(α∗)​dd​α∗​(𝗐​(α∗)𝗄′​(α∗))−Lℓch),\frac{\mathrm{d}^{2}\mathcal{E}}{\mathrm{d}{\alpha^{*}}^{2}}\bigg|_{t}=\mathsf{k}^{\prime}(\alpha^{*})^{2}\,\mathsf{G}_{\mathrm{c}}\left(\frac{1}{\mathsf{c_{w}}\,\mathsf{k}^{\prime}(\alpha^{*})}\frac{\mathrm{d}}{\mathrm{d}\alpha^{*}}\left(\frac{\sqrt{\mathsf{w}(\alpha^{*})}}{\mathsf{k}^{\prime}(\alpha^{*})}\right)-\frac{L}{\ell_{\mathrm{ch}}}\right),(60)

whose positivity is exactly the no-snap-back condition (49), of
which (58) is theα∗\alpha^{*}-uniform sufficient version. The
destabilizing elastic term is now proportional to the specimen lengthLLrather than toℓ\ellas
in (37): this is the origin of the size effect, and(SS)alone rules out snap-back only in the rigid limitL/ℓch→0L/\ell_{\mathrm{ch}}\to 0.

## Remark 8.

The homogeneous condition involves the regularization lengthℓ\ell, while the localized one involves the structural sizeLL: for sufficiently smallℓ\ellthe homogeneous branch is always free of snap-back, whereas the brittleness of the global response is controlled by the ratioL/ℓchL/\ell_{\mathrm{ch}}only.

## Remark 9(Selection between the homogeneous and the localized branch).

The homogeneous and localized branches are two competing solutions of the same evolution problem.
The localized branch emanates from the end of the elastic phase: asα∗→0\alpha^{*}\to 0,⟦u⟧→0\left\llbracket u\right\rrbracket\to 0andt→𝗄​(0)​τc/μ=εet\to\mathsf{k}(0)\tau_{c}/\mu={\varepsilon}_{e}in (48).
Differentiating the energy along either branch, the terms proportional tod​α/d​t\mathrm{d}\alpha/\mathrm{d}tcancel — by (31b) on the homogeneous branch,
by the cohesive law (47) on the localized one — leaving the energy balance
of the hard device,d​ℰ/d​t=L​τ​(t)\mathrm{d}\mathcal{E}/\mathrm{d}t=L\,\tau(t). Since both branches leave the
same elastic state att=εet={\varepsilon}_{e}, and since on the constant-stress plateauτloc=𝗄​(α∗)​τc<τc=τhom\tau_{\mathrm{loc}}=\mathsf{k}(\alpha^{*})\tau_{c}<\tau_{c}=\tau_{\mathrm{hom}},ℰloc(t)−ℰhom(t)=L∫εet(τloc(s)−τhom(s))ds<0,t>εe:\mathcal{E}_{\mathrm{loc}}(t)-\mathcal{E}_{\mathrm{hom}}(t)=L\int_{{\varepsilon}_{e}}^{t}\left(\tau_{\mathrm{loc}}(s)-\tau_{\mathrm{hom}}(s)\right)\mathrm{d}s<0,\qquad t>{\varepsilon}_{e}:(61)

the plateau is never a global minimizer. It is nonetheless a genuine stationary point: withp=t−εep=t-{\varepsilon}_{e}uniform, the damage criterion (31b) atα=0\alpha=0reads𝖦c​𝗐′​(0)/(4​𝖼𝗐​ℓ)−τc​|𝗄′​(0)|​p≥0\mathsf{G}_{\mathrm{c}}\,\mathsf{w}^{\prime}(0)/(4\mathsf{c_{w}}\ell)-\tau_{c}|\mathsf{k}^{\prime}(0)|\,p\geq 0and isstrictlysatisfied fort<εct<{\varepsilon}_{c}, so that an evolution started from the unperturbed homogeneous state remains on it up
toεc{\varepsilon}_{c}. Its stability is however degenerate: since𝗄​(0)=1\mathsf{k}(0)=1, the energy of the plateau state
depends onpponly through the integralP=∫p​dxP=\int p\,\mathrm{d}x, and not on the distribution ofppalong the bar,
so that concentrating the nonlinear deformation costs nothing, and growing damage on the resulting
jump is then favourable at first order in its amplitude. The plateau state is thus joined to states
of strictly lower energy by a path along which the energy never increases, and is not a local
minimizer. Any imperfection breaks the degeneracy strictly: with a non-uniform initial damageα0\alpha_{0}the term∫𝗄​(α0)​τc​p​dx\int\mathsf{k}(\alpha_{0})\,\tau_{c}\,p\,\mathrm{d}xis minimized by concentratingppwhereα0\alpha_{0}is largest — so that the load at which localization sets in is
imperfection-sensitive whereas the peak stressτc\tau_{c}is not, as observed numerically in
Section6.1.Figure 2:Snap-back phase diagrams for the family𝖬𝟣\mathsf{M1}in the plane(ζ,ℓ/ℓch)(\zeta,\ell/\ell_{\mathrm{ch}})for the homogeneous response (a) and(ζ,L/ℓch)(\zeta,L/\ell_{\mathrm{ch}})for the localized response (b). The solid lines are the critical valuesℓ/ℓch=ζ/(2​𝖼𝗐)\ell/\ell_{\mathrm{ch}}=\zeta/(2\mathsf{c_{w}})of (65) andLc/ℓch=(1+ζ)/(2​𝖼𝗐)L_{c}/\ell_{\mathrm{ch}}=(1+\zeta)/(2\mathsf{c_{w}})of (70), with𝖼𝗐=𝖼𝗐​(ζ)\mathsf{c_{w}}=\mathsf{c_{w}}(\zeta); atζ=1\zeta=1they take the valuesℓ/ℓch=1\ell/\ell_{\mathrm{ch}}=1andLc/ℓch=2L_{c}/\ell_{\mathrm{ch}}=2. The shaded regions correspond to snap-back of the corresponding branch under displacement control.

## 4A one-parameter family of models

The following family of constitutive laws𝖬𝟣\mathsf{M1}, depending on a scalar parameterζ\zeta, was introduced in[19].
It is defined by𝗄​(α)=1−α,𝗐​(α)=(1−ζ)​α+ζ​α2,ζ∈(0,1].\mathsf{k}(\alpha)=1-\alpha,\qquad\mathsf{w}(\alpha)=(1-\zeta)\alpha+\zeta\alpha^{2},\qquad\zeta\in(0,1].(62)

The normalization constant𝖼𝗐=∫01𝗐​(s)​ds\mathsf{c_{w}}=\int_{0}^{1}\sqrt{\mathsf{w}(s)}\,\mathrm{d}sis𝖼𝗐=4​ζ3/2+2​ζ1/2​(1−ζ)+(1−ζ)2​log⁡(1−ζ1+ζ)8​ζ3/2,\mathsf{c_{w}}=\frac{4\,\zeta^{3/2}+2\,\zeta^{1/2}\left(1-\zeta\right)+\left(1-\zeta\right)^{2}\log{\left(\dfrac{1-\sqrt{\zeta}}{1+\sqrt{\zeta}}\right)}}{8\,\zeta^{3/2}},

a decreasing function ofζ\zeta, ranging from𝖼𝗐=2/3\mathsf{c_{w}}=2/3asζ→0\zeta\to 0to𝖼𝗐=1/2\mathsf{c_{w}}=1/2atζ=1\zeta=1.
Hypotheses(SS)and(SH)hold for0<ζ≤10<\zeta\leq 1; asζ→0\zeta\to 0the hardening function𝗐′/𝗄′\mathsf{w}^{\prime}/\mathsf{k}^{\prime}becomes constant, so that the inequality in(SH)degenerates into a non-strict one.
We nevertheless report the limit caseζ=0\zeta=0below and in the figures, as it admits particularly simple closed forms.

Forζ=1\zeta=1,𝗄​(α)=1−α,𝗐​(α)=α2,𝖼𝗐=12,\mathsf{k}(\alpha)=1-\alpha,\quad\mathsf{w}(\alpha)=\alpha^{2},\quad\mathsf{c_{w}}=\frac{1}{2},(63)

the last term of (9) is the damage energy of the classicalAT2phase-field model.

The homogeneous response of Section3.1is characterized byεe=τcμ,εc=τcμ+𝖦cℓ​τc​1−ζ4​𝖼𝗐,εu=𝖦cℓ​τc​1+ζ4​𝖼𝗐,{\varepsilon}_{e}=\dfrac{\tau_{c}}{\mu},\qquad{\varepsilon}_{c}=\dfrac{\tau_{c}}{\mu}+\dfrac{\mathsf{G}_{\mathrm{c}}}{\ell\tau_{c}}\dfrac{1-\zeta}{4\mathsf{c_{w}}},\qquad{\varepsilon}_{u}=\dfrac{\mathsf{G}_{\mathrm{c}}}{\ell\tau_{c}}\dfrac{1+\zeta}{4\mathsf{c_{w}}},(64)

so that the constant-stress regime[εe,εc)[{\varepsilon}_{e},{\varepsilon}_{c})is present for everyζ<1\zeta<1and closes atζ=1\zeta=1.
Condition (36) for the absence of snap-back is independent ofα\alphaand becomesℓℓch<ζ2​𝖼𝗐,\frac{\ell}{\ell_{\mathrm{ch}}}<\frac{\zeta}{2\mathsf{c_{w}}},(65)

which is represented in the(ζ,ℓ/ℓch)(\zeta,\ell/\ell_{\mathrm{ch}})plane in Figure2(a).
The thresholdζ/(2​𝖼𝗐)\zeta/(2\mathsf{c_{w}})increases monotonically from0asζ→0\zeta\to 0to11atζ=1\zeta=1: the smallerζ\zeta, the more prone to snap-back the homogeneous branch, the limitζ→0\zeta\to 0snapping back for everyℓ>0\ell>0.
The corresponding stress-strain response is plotted in Figure3forℓch/ℓ=5\ell_{\mathrm{ch}}/\ell=5, a value for which the threshold is crossed atζ≃0.25\zeta\simeq 0.25: the softening branch snaps back forζ=0\zeta=0and, marginally, forζ=1/4\zeta=1/4, sinceℓ/ℓch=0.2\ell/\ell_{\mathrm{ch}}=0.2is just aboveζ/(2​𝖼𝗐)≃0.198\zeta/(2\mathsf{c_{w}})\simeq 0.198; it does not forζ=2/3\zeta=2/3andζ=1\zeta=1.

In the strength-softening regime, the loading parameter, the damage and the stress are affine functionst=εc+α​(εu−εc),α=t−εcεu−εc,τ=εu−tεu−εc​τc,t={\varepsilon}_{c}+\alpha\,({\varepsilon}_{u}-{\varepsilon}_{c}),\qquad\alpha=\frac{t-{\varepsilon}_{c}}{{\varepsilon}_{u}-{\varepsilon}_{c}},\qquad\tau=\frac{{\varepsilon}_{u}-t}{{\varepsilon}_{u}-{\varepsilon}_{c}}\,\tau_{c},(66)

the branch being described byα∈[0,1]\alpha\in[0,1]and snapping back wheneverεu<εc{\varepsilon}_{u}<{\varepsilon}_{c}, which is precisely the failure of (65).
The corresponding total energy densityWWof Remark4isWhom=τc​εu−tεu−εc​(t−εe2​εu−tεu−εc)+𝖦c4​𝖼𝗐​ℓ​t−εcεu−εc​((1−ζ)+ζ​t−εcεu−εc),W_{\rm hom}=\tau_{c}\frac{{\varepsilon}_{u}-t}{{\varepsilon}_{u}-{\varepsilon}_{c}}\left(t-\frac{{\varepsilon}_{e}}{2}\frac{{\varepsilon}_{u}-t}{{\varepsilon}_{u}-{\varepsilon}_{c}}\right)+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}\ell}\frac{t-{\varepsilon}_{c}}{{\varepsilon}_{u}-{\varepsilon}_{c}}\left((1-\zeta)+\zeta\,\frac{t-{\varepsilon}_{c}}{{\varepsilon}_{u}-{\varepsilon}_{c}}\right),(67)

the two terms being respectively the strain energy densityψ\psiof (7) and the damage energy𝖦c​𝗐​(α)/(4​𝖼𝗐​ℓ)\mathsf{G}_{\mathrm{c}}\,\mathsf{w}(\alpha)/(4\mathsf{c_{w}}\ell).
Since∂W/∂α=0\partial W/\partial\alpha=0along the branch,WhomW_{\rm hom}is also the work∫0tτ​dε\int_{0}^{t}\tau\,\mathrm{d}{\varepsilon}of the applied load.Figure 3:Homogeneous (material-point) responsefor the family𝖬𝟣\mathsf{M1}, for
several values ofζ\zetaand length-scale ratioℓch/ℓ=5\ell_{\mathrm{ch}}/\ell=5:
(a) normalized total energy densityWhom/(τc​εe)W_{\rm hom}/(\tau_{c}{\varepsilon}_{e})of (67) and
(b) normalized stressτ/τc\tau/\tau_{c},versusthe applied strainε\varepsilonin units of the elastic-limit strainεe=τc/μ{\varepsilon}_{e}=\tau_{c}/\mu.
The constant-stress plateauεe≤ε<εc{\varepsilon}_{e}\leq\varepsilon<{\varepsilon}_{c}is present only
forζ<1\zeta<1, and the softening branch snaps back forζ=0\zeta=0andζ=1/4\zeta=1/4.

Turning to the localized solutions, the relation⟦u⟧=𝖦c𝗐​(α∗)/(𝖼𝗐τc)\left\llbracket u\right\rrbracket=\mathsf{G}_{\mathrm{c}}\sqrt{\mathsf{w}(\alpha^{*})}/(\mathsf{c_{w}}\,\tau_{c})of (47) is a quadratic equation forα∗\alpha^{*}and is inverted explicitly, so that the cohesive lawτ=𝗄​(α∗)​τc=(1−α∗)​τc\tau=\mathsf{k}(\alpha^{*})\tau_{c}=(1-\alpha^{*})\tau_{c}reads asτ=τc​{1−4​τc29​𝖦c2⟦u⟧2,ζ→0,1−12​ζ​((1−ζ)2+4ζ(𝖼𝗐​τc𝖦c⟦u⟧)2−(1−ζ)),0<ζ<1,1−τc2​𝖦c⟦u⟧,ζ=1,\tau=\tau_{c}\begin{cases}\displaystyle 1-\dfrac{4\tau_{c}^{2}}{9\mathsf{G}_{\mathrm{c}}^{2}}\left\llbracket u\right\rrbracket^{2},&\zeta\to 0,\\[10.0pt]
\displaystyle 1-\frac{1}{2\zeta}\Bigg(\sqrt{(1-\zeta)^{2}+4\zeta\Big(\dfrac{\mathsf{c_{w}}\tau_{c}}{\mathsf{G}_{\mathrm{c}}}\left\llbracket u\right\rrbracket\Big)^{2}}-(1-\zeta)\Bigg),&0<\zeta<1,\\[10.0pt]
\displaystyle 1-\frac{\tau_{c}}{2\mathsf{G}_{\mathrm{c}}}\left\llbracket u\right\rrbracket,&\zeta=1,\end{cases}(68)

where in each line the quantity subtracted from unity is the maximal damageα∗(⟦u⟧)\alpha^{*}(\left\llbracket u\right\rrbracket), and where𝖼𝗐=2/3\mathsf{c_{w}}=2/3in the first line and𝖼𝗐=1/2\mathsf{c_{w}}=1/2in the third.
The corresponding cohesive surface energyΦ=𝗄(α∗)τc⟦u⟧+𝖦cα^(α∗)\Phi=\mathsf{k}(\alpha^{*})\,\tau_{c}\left\llbracket u\right\rrbracket+\mathsf{G}_{\mathrm{c}}\,\hat{\alpha}(\alpha^{*})of (51) reads asΦ(⟦u⟧)={τc⟦u⟧−4​τc327​𝖦c2⟦u⟧3,ζ→0,𝖦c𝖼𝗐​[(1−α∗)​(1−ζ)​α∗+ζ​α∗2+∫0α∗(1−ζ)​β+ζ​β2​dβ],0<ζ<1,τc⟦u⟧−τc24​𝖦c⟦u⟧2,ζ=1,\Phi(\left\llbracket u\right\rrbracket)=\begin{cases}\tau_{c}\left\llbracket u\right\rrbracket-\dfrac{4\tau_{c}^{3}}{27\mathsf{G}_{\mathrm{c}}^{2}}\left\llbracket u\right\rrbracket^{3},&\zeta\to 0,\\[6.0pt]
\dfrac{\mathsf{G}_{\mathrm{c}}}{\mathsf{c_{w}}}\!\left[(1-\alpha^{*})\sqrt{(1-\zeta)\alpha^{*}+\zeta{\alpha^{*}}^{2}}+\displaystyle\int_{0}^{\alpha^{*}}\!\sqrt{(1-\zeta)\beta+\zeta\beta^{2}}\,\mathrm{d}\beta\right],&0<\zeta<1,\\[6.0pt]
\tau_{c}\left\llbracket u\right\rrbracket-\dfrac{\tau_{c}^{2}}{4\mathsf{G}_{\mathrm{c}}}\left\llbracket u\right\rrbracket^{2},&\zeta=1,\end{cases}(69)

the middle line being expressed through the sameα∗(⟦u⟧)\alpha^{*}(\left\llbracket u\right\rrbracket)as in (68).
In all casesΦ\Phiis concave, withΦ′​(0+)=τc\Phi^{\prime}(0^{+})=\tau_{c}andΦ​(δu)=𝖦c\Phi(\delta_{u})=\mathsf{G}_{\mathrm{c}}at the critical openingδu=𝖦c/(𝖼𝗐​τc)\delta_{u}=\mathsf{G}_{\mathrm{c}}/(\mathsf{c_{w}}\tau_{c})of (56), in agreement with (57).

The infimum in the critical length (58) is attained atα∗=1\alpha^{*}=1, since𝗐′/𝗐\mathsf{w}^{\prime}/\sqrt{\mathsf{w}}is non-increasing, so that the conditionL<LcL<L_{c}is here necessary as well as sufficient for the localized branch to be free of snap-back, withLc=1+ζ2​𝖼𝗐​ℓch.L_{c}=\frac{1+\zeta}{2\,\mathsf{c_{w}}}\,\ell_{\mathrm{ch}}.(70)

As shown in Figure2(b),LcL_{c}increases monotonically withζ\zeta, fromLc=3​ℓch/4L_{c}=3\ell_{\mathrm{ch}}/4in the limitζ→0\zeta\to 0toLc=2​ℓchL_{c}=2\ell_{\mathrm{ch}}atζ=1\zeta=1.

Figure4summarizes the properties of the localized solution for the same values ofζ\zetaas the homogeneous response of Figure3.
It presents the cohesive surface energyΦ(⟦u⟧)\Phi(\left\llbracket u\right\rrbracket), the cohesive tractionτ(⟦u⟧)\tau(\left\llbracket u\right\rrbracket), and the resulting global response of a bar of lengthL=ℓchL=\ell_{\mathrm{ch}}.
Note the snap-back for the two smallest values ofζ\zeta, for whichL>LcL>L_{c}, see (70).Figure 4:Localized solutionfor the family𝖬𝟣\mathsf{M1}, for the same values of the
shape parameterζ\zetaas in Figure3:
(a) equivalent cohesive surface energyΦ/𝖦c\Phi/\mathsf{G}_{\mathrm{c}}and
(b) cohesive tractionτ/τc\tau/\tau_{c}, both as functions of the normalized crack
openingδ​τc/𝖦c\delta\,\tau_{c}/\mathsf{G}_{\mathrm{c}}, withδ=⟦u⟧\delta=\left\llbracket u\right\rrbracket;
(c) stressτ/τc\tau/\tau_{c}versusthe normalized end loadt​μ/τct\,\mu/\tau_{c}, witht=u​(L)/Lt=u(L)/L, for a bar of lengthL=ℓchL=\ell_{\mathrm{ch}}, combining the elastic loading branch with
the localized softening branch (48), drawn dashed across
the snap-back; the constant-stress plateau (ζ<1\zeta<1) is deliberately
not drawn.

## 5Numerical implementation

The numerical implementation is based on the minimization of the energy functionalℰℓ​(u,𝒑,α)\mathcal{E}_{\ell}(u,\boldsymbol{p},\alpha)at each time step, under a prescribed time-dependent displacement on∂uΩ\partial_{u}\Omegaand the irreversibility condition on the damageα\alpha.
Before presenting the numerical results, we first introduce the dimensionless formulation of the model and then describe the numerical solution strategy.

## 5.1Dimensionless formulation

Besides the constitutive functions𝗄\mathsf{k}and𝗐\mathsf{w}, the energy functional depends on the shear modulusμ\mu, the shear strengthτc\tau_{c}, the fracture energy𝖦c\mathsf{G}_{\mathrm{c}}, and the regularization length scaleℓ\ell; we denote byLLa characteristic length of the domainΩ\Omega.
The number of independent parameters can be reduced by rewriting the energy functional (16) in a dimensionless form.
Settingx=L​x∗,u=u0​u∗,∇=1L​∇∗,𝒑=u0L​𝒑∗,d​A=L2​d​A∗,ℰℓ=𝖦c​L​ℰℓ∗,x=Lx^{*},\quad u=u_{0}u^{*},\quad\nabla=\frac{1}{L}\nabla^{*},\quad\boldsymbol{p}=\frac{u_{0}}{L}\boldsymbol{p}^{*},\quad\,\mathrm{d}A=L^{2}\,\mathrm{d}A^{*},\quad\mathcal{E}_{\ell}=\mathsf{G}_{\mathrm{c}}L\mathcal{E}_{\ell}^{*},(71)

whereLLandu0u_{0}are characteristic length and displacement scales, we obtainℰℓ∗​(u∗,𝒑∗,α)=∫Ω∗μ​u022​𝖦c​L​‖∇∗u∗−𝒑∗‖2+τc​u0𝖦c​𝗄​(α)​‖𝒑∗‖+14​𝖼𝗐​(Lℓ​𝗐​(α)+ℓL​‖∇∗α‖2)​d​A∗.\mathcal{E}_{\ell}^{*}(u^{*},\boldsymbol{p}^{*},\alpha)=\int_{\Omega^{*}}\frac{\mu u_{0}^{2}}{2\mathsf{G}_{\mathrm{c}}L}\|\nabla^{*}u^{*}-\boldsymbol{p}^{*}\|^{2}+\frac{\tau_{c}u_{0}}{\mathsf{G}_{\mathrm{c}}}\mathsf{k}(\alpha)\|\boldsymbol{p}^{*}\|+\frac{1}{4\mathsf{c_{w}}}\left(\frac{L}{\ell}\mathsf{w}(\alpha)+\frac{\ell}{L}\|\nabla^{*}\alpha\|^{2}\right)\,\mathrm{d}A^{*}.(72)

Setting without loss of generalityu0:=𝖦c/τcu_{0}:={\mathsf{G}_{\mathrm{c}}}/{\tau_{c}}, we get the following non-dimensional expression of the energyℰℓ∗​(u∗,𝒑∗,α)=∫Ω∗ℓch2​L​‖∇∗u∗−𝒑∗‖2+𝗄​(α)​‖𝒑∗‖+14​𝖼𝗐​(Lℓ​𝗐​(α)+ℓL​‖∇∗α‖2)​d​A∗.\mathcal{E}_{\ell}^{*}(u^{*},\boldsymbol{p}^{*},\alpha)=\int_{\Omega^{*}}\frac{\ell_{\mathrm{ch}}}{2L}\|\nabla^{*}u^{*}-\boldsymbol{p}^{*}\|^{2}+\mathsf{k}(\alpha)\|\boldsymbol{p}^{*}\|+\frac{1}{4\mathsf{c_{w}}}\left(\frac{L}{\ell}\mathsf{w}(\alpha)+\frac{\ell}{L}\|\nabla^{*}\alpha\|^{2}\right)\,\mathrm{d}A^{*}.(73)

When written in this form, it is clear that the problem depends on the two dimensionless numbersbrittleness parameter:Lℓch=τc2​Lμ​𝖦c,regularization parameter:ℓL.\text{{brittleness parameter}}:\quad\frac{L}{\ell_{\mathrm{ch}}}=\frac{\tau_{c}^{2}L}{\mu\mathsf{G}_{\mathrm{c}}},\qquad\text{{regularization parameter}}:\quad\frac{\ell}{L}.(74)

The brittleness parameter is the antiplane form of the dimensionless brittleness number that governs size effects in quasi-brittle fracture[21,13].
In the numerical simulations below, each test is specified by the two dimensionless groups (74), together with the constitutive parameterζ\zetaand the numerical parameters (h/ℓh/\ell,α0\alpha_{0},NN), and all results are reported in dimensionless form: stresses are normalized by the strengthτc\tau_{c}, displacements byu0=𝖦c/τcu_{0}=\mathsf{G}_{\mathrm{c}}/\tau_{c}, and strains — including the loadtt— byεe=τc/μ{\varepsilon}_{e}=\tau_{c}/\mu, except in the rigid limitμ→∞\mu\to\infty, whereεe→0{\varepsilon}_{e}\to 0and the load is reported astL/u0=⟦u⟧τc/𝖦ct\,L/u_{0}=\left\llbracket u\right\rrbracket\,\tau_{c}/\mathsf{G}_{\mathrm{c}}. For the sake of readability, we drop the superscript∗*from now on.

## 5.2Discretization and solvers

At each loading stepii, corresponding to the load parametertit_{i}, we solve the incremental minimization problem (10), in which the lower boundαi−1\alpha_{i-1}entering𝒟i\mathcal{D}_{i}, the damage field at the previous loading step, enforces the irreversibility condition.
The energy is separately convex with respect to the pair(u,𝒑)(u,\boldsymbol{p})at fixedα\alphaand with respect toα\alphaat fixed(u,𝒑)(u,\boldsymbol{p}), but not jointly convex.
We exploit this structure through an alternate minimization scheme[18], a fixed-point algorithm where we iteratively solve the two subproblems until convergence:
- 1.

Minimize the energy with respect to(u,𝒑)(u,\boldsymbol{p})at fixedα\alpha.
- 2.

Minimize the energy with respect toα\alphaat fixed(u,𝒑)(u,\boldsymbol{p})and under the bound constraintsαi−1≤α≤1\alpha_{i-1}\leq\alpha\leq 1.

We discretize the fields using finite elements with triangular cells.
For the displacementuuand the damageα\alphawe use linear simplicial Lagrange elements.
The nonlinear deformation𝒑\boldsymbol{p}is discretized using a quadrature space that retains as the degrees of freedom only the values𝒑g=𝒑​(xg)\boldsymbol{p}^{g}=\boldsymbol{p}(x_{g})of𝒑\boldsymbol{p}at the quadrature points; in this paper, we use a simple one-point Gauss integration rule.
We denote by𝖯\mathsf{P}thengn_{g}-dimensional vector collecting the values of the nonlinear deformation at the quadrature points and by𝖴\mathsf{U}and𝖣\mathsf{D}thennn_{n}-dimensional vectors collecting the degrees of freedom for the displacement and damage fields, such thatu​(x)=∑k=1nn𝖴k​χk​(x)u(x)=\sum_{k=1}^{n_{n}}\mathsf{U}_{k}\chi_{k}(x)andα​(x)=∑k=1nn𝖣k​χk​(x)\alpha(x)=\sum_{k=1}^{n_{n}}\mathsf{D}_{k}\chi_{k}(x), where theχk\chi_{k}’s are the finite-element basis functions andnnn_{n}andngn_{g}are the number of nodes and quadrature points in the mesh.
We use the finite element framework FEniCSx/DOLFINx for the discretization and the data management[10].

Both subproblems are convex and are solved to high accuracy with the conic interior-point optimizer of MOSEK[8]: the first through the second-order cone programming (SOCP) reformulation of AppendixA.1, the second through the bound-constrained conic reformulation of AppendixA.2.
The alternate minimization loop is stopped when the increment of the damage field between two successive iterations is smaller, in the infinity norm, than a tolerancetolAM\mathrm{tol}_{\mathrm{AM}}, set to10−310^{-3}unless otherwise stated.
The scheme extends without modification to the variant in which the nonlinear deformation is subject to an irreversibility condition (Remark1), used in Section6.2: it suffices to replace‖𝒑‖\|\boldsymbol{p}\|by‖𝒑−𝒑i−1‖\|\boldsymbol{p}-\boldsymbol{p}_{i-1}\|in the cone constraint of the(u,𝒑)(u,\boldsymbol{p})subproblem, and by the cumulated deformationp¯i=p¯i−1+‖𝒑i−𝒑i−1‖\bar{p}_{i}=\bar{p}_{i-1}+\|\boldsymbol{p}_{i}-\boldsymbol{p}_{i-1}\|in the damage subproblem.
Similarly, the rigid limitμ→∞\mu\to\inftyused in Section6.1is obtained by dropping the elastic term from the objective and enforcing∇u=𝒑\nabla u=\boldsymbol{p}pointwise as an equality constraint, the stress being recovered as the associated Lagrange multiplier (AppendixA.1).Algorithm 1Incremental alternate minimization scheme.1:𝖣0←\mathsf{D}_{0}\leftarrownodal values of the initial damage fieldα0\alpha_{0}2:fori=1,…,Ni=1,\ldots,Ndo⊳\trianglerightloading steps3:update the imposed displacementu¯​(ti)\bar{u}(t_{i}); set𝖣(0)←𝖣i−1\mathsf{D}^{(0)}\leftarrow\mathsf{D}_{i-1}4:forj=1,2,…j=1,2,\ldots, up to maxiterdo⊳\trianglerightalternate minimization5:(𝖴(j),𝖯(j))←(\mathsf{U}^{(j)},\mathsf{P}^{(j)})\leftarrowsolution of the SOCP (84) with𝖣=𝖣(j−1)\mathsf{D}=\mathsf{D}^{(j-1)}6:𝖣(j)←\mathsf{D}^{(j)}\leftarrowsolution of the SOCP (87) with𝖯=𝖯(j)\mathsf{P}=\mathsf{P}^{(j)}and bounds𝖣i−1≤𝖣≤1\mathsf{D}_{i-1}\leq\mathsf{D}\leq 17:ifmax⁡|𝖣(j)−𝖣(j−1)|≤tolAM\max|\mathsf{D}^{(j)}-\mathsf{D}^{(j-1)}|\leq\mathrm{tol}_{\mathrm{AM}}thenbreak8:endif9:endfor10:(𝖴i,𝖯i,𝖣i)←(𝖴(j),𝖯(j),𝖣(j))(\mathsf{U}_{i},\mathsf{P}_{i},\mathsf{D}_{i})\leftarrow(\mathsf{U}^{(j)},\mathsf{P}^{(j)},\mathsf{D}^{(j)})11:endfor

## 6Numerical simulations

All the simulations of this section use the constitutive family𝖬𝟣\mathsf{M1}of (62):𝗄​(α)=1−α,𝗐​(α)=(1−ζ)​α+ζ​α2,\mathsf{k}(\alpha)=1-\alpha,\qquad\mathsf{w}(\alpha)=(1-\zeta)\,\alpha+\zeta\,\alpha^{2},

withζ∈(0,1]\zeta\in(0,1]controlling the shape of the cohesive law and of the homogeneous material response, as shown in Sections3.1–3.2and Figures3and4.
We adopt the dimensionless setting of Section5.1, so thatℓch=1\ell_{\mathrm{ch}}=1andεe=1{\varepsilon}_{e}=1, except in Figure18, whereℓch\ell_{\mathrm{ch}}is varied.
Each test is then characterized by the brittleness ratioL/ℓchL/\ell_{\mathrm{ch}}, the regularization ratioℓ/ℓch\ell/\ell_{\mathrm{ch}}, and the constitutive parameterζ\zeta.
In all the figures of this section, markers denote numerical results and lines the corresponding analytical predictions or reference curves.

## 6.1Simple shear

We begin by focusing on the simple shear problem introduced in Section3, for which the homogeneous and localized solutions constructed in Sections3.1and3.2provide closed-form references.
The aim is twofold: to verify that the alternate minimization scheme of Section5correctly captures the localized solutions and the associated equivalent cohesive law, and to illustrate the structural responses predicted by the model when varying the dimensionless parameters identified in Section5.1.

We imposeα=0\alpha=0on the loaded end points, so that solutions with localization at the boundary or non-zero homogeneous damage are not admissible.
Unless otherwise stated, the localization point is selected by a small initial damage fieldα0​cos2⁡(π​x/L)\alpha_{0}\cos^{2}(\pi x/L), imposed as an irreversible lower bound.
All runs use unstructured triangular meshes of sizeh<ℓh<\ell, generated by the mesh generator Gmsh[39].
The boundary displacements are applied in 50 to 100 time-increments.
The discretization and the solver settings are those of Section5.
The values specific to each test (L/ℓchL/\ell_{\mathrm{ch}},ℓ/ℓch\ell/\ell_{\mathrm{ch}},ζ\zeta,α0\alpha_{0}, andNN) are reported in the figure captions.
In all the figures, the analytical reference curves are the homogeneous response (34) and the localized response obtained by combining the equivalent cohesive law (47) with the loading condition (48).

We first focus on the caseζ=1\zeta=1in which the constant-stress regime of the homogeneous solution disappears (εc=εe{\varepsilon}_{c}={\varepsilon}_{e}, see (64)) and the equivalent cohesive law (68) is linear with the stress vanishing at the ultimate openingδuf:=⟦u⟧|α∗=1=2𝖦c/τc\delta_{u}^{f}:=\left\llbracket u\right\rrbracket\big|_{\alpha^{*}=1}={2\mathsf{G}_{\mathrm{c}}}/{\tau_{c}}.

Figure5(a) shows the global response of a bar of lengthL=ℓchL=\ell_{\mathrm{ch}}withℓ/ℓch=0.05\ell/\ell_{\mathrm{ch}}=0.05for decreasing discretization sizesh=ℓ/2h=\ell/2,ℓ/5\ell/5, andℓ/10\ell/10.
The evolution of the total, elastic (the bulk term∫Ωμ2​‖∇u−𝒑‖2​dA\int_{\Omega}\frac{\mu}{2}\|\nabla u-\boldsymbol{p}\|^{2}\,\mathrm{d}A), and dissipated (the plastic and damage terms, see Remark6) energies are shown in Figure5(b), together with the exact solution from Section3.
We observe that in all cases the numerical solution bifurcates from the homogeneous response at the onset of the strength-softening brancht=εc=εe=1t={\varepsilon}_{c}={\varepsilon}_{e}=1, and the stresses vanish att≃δuf/Lt\simeq\delta_{u}^{f}/L, the final failure load inheriting the mesh-induced toughening discussed below (visible forh=ℓ/2h=\ell/2).
As expected, the energy dissipated along the crack is overestimated by a factor1+h/(4​𝖼𝗐​ℓ)1+{h}/{(4\mathsf{c_{w}}\ell)}, which could be counteracted by using a numerical fracture toughness𝖦cnum=𝖦c/(1+h/(4​𝖼𝗐​ℓ))\mathsf{G}_{\mathrm{c}}^{\mathrm{num}}=\mathsf{G}_{\mathrm{c}}/\left(1+{h}/({4\mathsf{c_{w}}\ell})\right)accounting for this mesh-induced toughening[17].

These observations are made quantitative in Table1. The peak strengthτmax\tau_{\max}, which sets the critical load for crack nucleation (t=εc=εe=1t={\varepsilon}_{c}={\varepsilon}_{e}=1), is matched within1%1\%and is insensitive to the mesh; the final failure load followsδuf/L=2\delta_{u}^{f}/L=2amplified by the same mesh-toughening factor as the dissipated energy, sinceδuf\delta_{u}^{f}is proportional to𝖦c\mathsf{G}_{\mathrm{c}}; the residual gap onτmax\tau_{\max}merely reflects the finite load incrementΔ​t≃0.02\Delta t\simeq 0.02and the initial imperfectionα0=10−3\alpha_{0}=10^{-3}, the last step before nucleation being still elastic. The normalized dissipated energyℰdiss/(𝖦c​H)\mathcal{E}_{\mathrm{diss}}/(\mathsf{G}_{\mathrm{c}}H)is overestimated by an amount that follows the analytical mesh-toughening factor1+h/(4​𝖼𝗐​ℓ)1+h/(4\mathsf{c_{w}}\ell)to better than1%1\%forh≤ℓ/5h\leq\ell/5, and to within2%2\%at the coarsest meshh=ℓ/2h=\ell/2, where the bar is not yet fully broken at the last computed load.Dissipated energyℰdiss/(𝖦c​H)\mathcal{E}_{\mathrm{diss}}/(\mathsf{G}_{\mathrm{c}}H)Strengthτmax/τc\tau_{\max}/\tau_{c}h/ℓh/\ellnumerical1+h4​𝖼𝗐​ℓ1+\tfrac{h}{4\mathsf{c_{w}}\ell}numerical0.10.11.0491.0491.0501.0500.9940.9940.20.21.0961.0961.1001.1000.9940.9940.50.51.2221.2221.2501.2500.9960.996Table 1:Dissipated fracture energy and strength as a function of the mesh size for the simple-shear test of Figure5.Figure 5:Simple shear, reference case:L/ℓch=1L/\ell_{\mathrm{ch}}=1,ζ=1\zeta=1,ℓ/ℓch=0.05\ell/\ell_{\mathrm{ch}}=0.05,α0=10−3\alpha_{0}=10^{-3},N=80N=80load steps, for uniform meshesh/ℓ∈{0.1,0.2,0.5}h/\ell\in\{0.1,0.2,0.5\}. (a) Stressτ/τc\tau/\tau_{c}versus end loadt/εet/{\varepsilon}_{e}; (b) total, elastic and dissipated energies normalized by𝖦c​H\mathsf{G}_{\mathrm{c}}H, against the exact solution (50).

The damage and nonlinear deformation fieldsα\alphaand‖𝒑‖​h\|\boldsymbol{p}\|hafter failure are shown in Figure6, using a coarse discretization in order to make the mesh visible.
As expected, they are invariant in theyydirection,up to the discretization size.
The crack can be identified as the one-element wide band along which𝒑\boldsymbol{p}localizes, andα=1\alpha=1.

Figure7shows snapshots in time of one-dimensional profiles ofuu,α\alpha, and𝒑\boldsymbol{p}along the symmetry axisy=0y=0.
We observe the elastic phase (α=0\alpha=0, linear displacement field), followed by the nucleation of a cohesive crack indicated by a non-zero damage in a strip of width of orderℓ\ellcentered at 0 along which‖𝒑‖>0\|\boldsymbol{p}\|>0and the displacement field is discontinuous.
Unlike classical damage models based on stiffness degradation, where the displacement can be discontinuous only whenα=1\alpha=1, it jumps even whenα<1\alpha<1: the jump is the singular part𝒑S=⟦u⟧𝐧δJu\boldsymbol{p}^{\mathrm{S}}=\left\llbracket u\right\rrbracket\,\mathbf{n}\,\delta_{J_{u}}of (15), obtained by concentration of the nonlinear deformation on the localization line.
Since𝒑\boldsymbol{p}concentrates on a single band of elements, where it scales as1/h1/h, we report the scaled field‖𝒑‖​h\|\boldsymbol{p}\|h, which for the one-point quadrature discretization is the discrete transverse integral of‖𝒑‖\|\boldsymbol{p}\|across the band and converges to|⟦u⟧|\left|\!\left\llbracket u\right\rrbracket\!\right|ash→0h\to 0, rather than the mesh-dependent‖𝒑‖\|\boldsymbol{p}\|.
Residual forces along the crack faces result in non-constant displacement in each ligament and vanish after the ultimate failure loadt=δuf/Lt=\delta_{u}^{f}/L.Figure 6:Damageα\alpha(top) and nonlinear deformation scaled by the mesh size,‖𝒑‖​h\|\boldsymbol{p}\|h(bottom), at the end of loading for the test of Figure5withH/L=0.1H/L=0.1and a deliberately coarse mesh,h/ℓ=0.2h/\ell=0.2, to make the triangulation visible.Figure 7:Reference test of Figure5ath/ℓ=0.1h/\ell=0.1: profiles along the mid-liney=0y=0of (a) the damageα\alpha, (b) the displacementuuand (c) the scaled nonlinear deformation‖𝒑‖​h\|\boldsymbol{p}\|h, versusx/Lx/Land colored by the loadt/εet/{\varepsilon}_{e}. Thick lines: onset of localizationt=εc=1t={\varepsilon}_{c}=1and ultimate failuret=δuf/L=2t=\delta_{u}^{f}/L=2.

In Figure8(a), we explore the effect of the brittleness parameterL/ℓchL/\ell_{\mathrm{ch}}on the post-peak global response at fixedℓ/ℓch=0.05\ell/\ell_{\mathrm{ch}}=0.05.
The remaining parameters areζ=1\zeta=1,α0=10−3\alpha_{0}=10^{-3},h/ℓ=0.1h/\ell=0.1, andN=80N=80.
The numerical results match the analytical expression (48): after an elastic regime for0<t<10<t<1, we observe the creation of a cohesive branch forL<Lc=2​ℓchL<L_{c}=2\,\ell_{\mathrm{ch}}(see (70) and Figure2(b)). ForL>LcL>L_{c}, since one cannot follow the snap-back in a displacement-controlled setting, we observe the sudden nucleation of a crack with full release of the elastic energy,i.e.a brittle crack.

This is consistent with the structural size effects of cohesive models: short bars fail gradually, long bars fail in a brittle manner, the transition being governed by the ratioL/ℓchL/\ell_{\mathrm{ch}}.

Figure8(b) highlights the influence of the regularization lengthℓ/ℓch\ell/\ell_{\mathrm{ch}}when the ratioL/ℓch=1L/\ell_{\mathrm{ch}}=1is fixed.
All other parameters are similar to those of the previous case.
Asℓ/ℓch\ell/\ell_{\mathrm{ch}}decreases from0.20.2down to0.0250.025, we observe that the overall response is virtually unaffected by changes inℓ\elland matches the localized branch from Section3.2.
Both behaviors are consistent with[81]for standard phase-field models with stiffness degradation.
This test confirms numerically a key property of the model: in contrast with the standard phase-field models, where the equivalent strength scales asμ​𝖦c/ℓ\sqrt{\mu\mathsf{G}_{\mathrm{c}}/\ell}, here both the strength and the equivalent cohesive law areℓ\ell-independent, andℓ\ellacts as a pure numerical regularization parameter.

In Figure8(c), we consider the caseζ=0.75\zeta=0.75, where the homogeneous response exhibits a constant-stress phase, shown in Figure3(b), and study the impact of the magnitude of the initial perturbationα0∈{0,10−3,10−2}\alpha_{0}\in\{0,10^{-3},10^{-2}\}.
The other parameters areL/ℓch=1L/\ell_{\mathrm{ch}}=1,ℓ/ℓch=0.05\ell/\ell_{\mathrm{ch}}=0.05,N=100N=100load steps, and the alternate-minimization tolerance was tightened to10−510^{-5}.
In this situation, the critical load at which we observe the bifurcation from the constant-stress to the localized regime depends on the magnitude of the small perturbationα0\alpha_{0}, but the peak stress remains unaffected.
This is the numerical counterpart of Remark9and is again consistent with[19]: since𝗄​(α)​τc​‖𝒑‖\mathsf{k}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|is homogeneous of degree one, the second variation of the energy is degenerate along redistributions of𝒑\boldsymbol{p}on the constant-stress branch, so that its stability is decided by higher-order terms and the load at which localization sets in by the imperfection.Figure 8:Stress–strain response of the simple shear test: influence of (a) the brittlenessL/ℓch∈{0.5,1,2,4}L/\ell_{\mathrm{ch}}\in\{0.5,1,2,4\}atℓ/ℓch=0.05\ell/\ell_{\mathrm{ch}}=0.05, the localized branch dashed across its snap-back; (b) the regularization lengthℓ/ℓch∈{0.025,0.05,0.1,0.2}\ell/\ell_{\mathrm{ch}}\in\{0.025,0.05,0.1,0.2\}atL/ℓch=1L/\ell_{\mathrm{ch}}=1; (c) the imperfectionα0∈{0,10−3,10−2}\alpha_{0}\in\{0,10^{-3},10^{-2}\}atζ=0.75\zeta=0.75,N=100N=100. Other parameters as in Figure5, withh/ℓ=0.1h/\ell=0.1.

Finally, Figure9deals with the rigid limitμ→∞\mu\to\infty.
In this case, minimizers of the total energy satisfy∇u=𝒑\nabla u=\boldsymbol{p}and the elastic energy is always 0.
The(u,𝒑)(u,\boldsymbol{p})subproblem reduces to the minimization of∫Ω𝗄​(α)​τc​‖∇u‖​dA\int_{\Omega}\mathsf{k}(\alpha)\,\tau_{c}\|\nabla u\|\,\mathrm{d}A.
Since the bar carries no elastic strain, the imposed displacement coincides with the displacement jump,tL=⟦u⟧t\,L=\left\llbracket u\right\rrbracket, and the measured force–displacement response is the equivalent cohesive law itself.
This test isolates the cohesive response and provides the most direct numerical verification of the equivalence between the phase-field model and the cohesive law of Section3.2.Figure 9:Simple shear in the rigid limitμ→∞\mu\to\infty(ζ=1\zeta=1,L​τc/𝖦c=1L\,\tau_{c}/\mathsf{G}_{\mathrm{c}}=1,ℓ/L=0.05\ell/L=0.05,h/ℓ=0.05h/\ell=0.05,α0=0\alpha_{0}=0,N=80N=80load steps), for which the imposed load is the opening,tL=⟦u⟧t\,L=\left\llbracket u\right\rrbracket: (a) equivalent cohesive law (68), (b) dissipated energy normalized by𝖦c​H\mathsf{G}_{\mathrm{c}}H, (c) displacementuualong the bar; color scale: the load⟦u⟧τc/𝖦c\left\llbracket u\right\rrbracket\,\tau_{c}/\mathsf{G}_{\mathrm{c}}.

## 6.2Surfing problem

## 6.2.1Geometry and loading

Our second set of numerical simulations is based on the “surfing problem” from[43].
We consider a rectangular domain(0,W)×(−H/2,H/2)(0,W)\times(-H/2,H/2)with an initial crack(0,L0]×{0}(0,L_{0}]\times\{0\}(see Figure10).
Along the outer boundary of the domain, we prescribe a displacement of the formusurfK,xc​(x,y)=2​K​(t)μ​r2​π​sin⁡θ2,r=(x−xc​(t))2+y2,θ=atan2⁡(y,x−xc​(t)),u_{\mathrm{surf}}^{K,x_{c}}(x,y)=\frac{2K(t)}{\mu}\sqrt{\frac{r}{2\pi}}\,\sin\frac{\theta}{2},\quad r=\sqrt{(x-x_{c}(t))^{2}+y^{2}},\quad\theta=\operatorname{atan2}(y,\,x-x_{c}(t)),(75)

withK​(t)={ttramp​K∞if​t<tramp,K∞otherwise,xc​(t)={L0if​t<tramp,L0+(t−tramp)otherwiseK(t)=\begin{cases}\frac{t}{t_{\mathrm{ramp}}}K_{\infty}&\text{ if }t<t_{\mathrm{ramp}},\\
K_{\infty}&\text{ otherwise}\end{cases},\qquad x_{c}(t)=\begin{cases}L_{0}&\text{ if }t<t_{\mathrm{ramp}},\\
L_{0}+(t-t_{\rm ramp})&\text{ otherwise}\end{cases}(76)

while the pre-existing crack edges are left stress free.
Past an initial stage fort<trampt<t_{\rm ramp}, this boundary displacement is a translation of the mode-III asymptotic field associated with a stress intensity factorK∞K_{\infty}along thexx-axis at unit speed and is fully characterized by the dimensionless parameterG/𝖦c=K∞2/(2​μ​𝖦c)G/\mathsf{G}_{\mathrm{c}}=K_{\infty}^{2}/(2\mu\mathsf{G}_{\mathrm{c}}).
Owing to the symmetry of the problem, one expects a crack growing along thexx-axis, and we performed our simulations on a half domain.Figure 10:Geometry and loading of the two antiplane test cases. Half-domain for the (left) Surfing, (right) Pac-Man simulations.

While𝒑\boldsymbol{p}was introduced as a nonlinear deformation, it is equally natural to view it as a plastic strain and subject it to an irreversibility constraint, as in the theory of perfect plasticity (Remark1).
We therefore performed two series of simulations with theM1model atζ=1\zeta=1, without and with this constraint — referred to in the sequel as thereversibleandirreversiblecases — the latter requiring only a minor modification of the two convex subproblems (Section5).
As we shall see, plastic irreversibility barely affects the damage field but changes the crack-tip fields and the energy balance appreciably: the work spent in the cohesive band, entirely recoverable when𝒑\boldsymbol{p}is reversible, is then dissipated (Remark6), and a residual plastic wake is left behind, and dragged along with, the advancing tip.
The two settings thus realize two distinct fracture phenomenologies: with𝒑\boldsymbol{p}reversible, dissipation is carried by damage alone and the macroscopic toughness reduces to the prescribed𝖦c\mathsf{G}_{\mathrm{c}}, as for brittle cohesive fracture; with𝒑\boldsymbol{p}irreversible, the plastic work accumulated in the wake adds to it and the effective toughness exceeds𝖦c\mathsf{G}_{\mathrm{c}}, the mechanism by which plastic dissipation inflates the measured fracture energy in ductile failure.

In the field computations below (Figures11–13), the domain size isW=8W=8,H=5H=5and the initial crack length isL0=1/4L_{0}=1/4, in units ofℓch\ell_{\mathrm{ch}}; the load is applied in121121increments, the first1515forming the ramp, withG/𝖦c=1.2G/\mathsf{G}_{\mathrm{c}}=1.2in the reversible case andG/𝖦c=1.55G/\mathsf{G}_{\mathrm{c}}=1.55in the irreversible one — the latter must exceed the effective toughness𝖦ceff≃1.3​𝖦c\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}\simeq 1.3\,\mathsf{G}_{\mathrm{c}}measured below for the crack to propagate.
The regularization and mesh sizes (ℓ/ℓch\ell/\ell_{\mathrm{ch}},h/ℓh/\ell) are reported in the figure captions.

## 6.2.2Simulation results

After the loading ramp phase, we observed progressive crack propagation associated with self-similar profiles forα\alpha,𝒑\boldsymbol{p}and𝝉\boldsymbol{\tau}, translating along thexx-axis at unit speed.
False-color plots of these fields in the reversible and irreversible cases are shown in Figure11, while Figure12represents their profiles along thexx-axis and along a vertical line through the fully developed crack.
Since we solved the problem on a half-domain anduuis pinned to 0 along thexx-axis, in Figure12(bottom left),uuis sampled aty=ℓc​h/10y=\ell_{\mathrm{c}h}/10.Figure 11:Crack-tip fields at the finest mesh (ℓ/ℓch=1/6\ell/\ell_{\mathrm{ch}}=1/6,h/ℓ=0.1h/\ell=0.1): damageα\alpha(top), plastic slip‖𝒑‖​h\|\boldsymbol{p}\|h(middle), normalized stress‖𝝉‖/τc\|\boldsymbol{\tau}\|/\tau_{c}(bottom), for the reversible (left) and irreversible (right) run. Note the residual plastic wake behind the irreversible tip.Figure 12:1-D field profiles alongy=0y=0(left) and the tip normalx=xPx=x_{P}(right). Top: damageα\alpha, plastic slip‖𝒑‖​h\|\boldsymbol{p}\|h(log); bottom: displacementuu, stress‖𝝉‖/τc\|\boldsymbol{\tau}\|/\tau_{c}. Solid: reversible, dashed: irreversible.

The propagation appears to be smooth in time, as observed in[75]for sharp-interface cohesive models and in contrast to the “jerky” motion, where a crack grows intermittently, which has been observed and analyzed in[6,20,27,29].

As expected, we observe that the damage fieldα\alphais similar in both cases (Figure11(top)).
Along vertical cross sections in the crack wake, the localization width is of order𝒪​(ℓ)\mathcal{O}(\ell)and the profile consistent with the exponential optimal profile for the AT2 model (Figure12(top right)).
Ahead of the crack however, we observe an elongated area withα>0\alpha>0(Figure12(top left)).
In both figures, we quantify this region by marking three points on thexx-axis:C=(xc,0)C=(x_{c},0), as given by (76) andP=(xP,0)P=(x_{P},0)andQ=(xQ,0)Q=(x_{Q},0)corresponding to the region in whichα\alphatransitions from 1 to 0 along thexx-axis, so thatQQis also the maximum extent of the region‖𝒑‖>0\|\boldsymbol{p}\|>0.
As shown in Figure13(right), after a transition region corresponding to the loading ramp,PPandQQmove along withCC.
In Figure12(bottom left) we see that in both cases, the crack edges are stress-free while the stress attains its maximum nearQQ.
We thus think ofPPas the “brittle crack tip” and ofQQas the “cohesive crack tip”.
The length of the cohesive crack|P​Q||PQ|is slightly larger in the irreversible case with|P​Q|≃ℓch|PQ|\simeq\ell_{\mathrm{ch}}.
The displacement profile along the crack edges (Figure12(bottom left)) transitions from the parabolic opening of a traction-free brittle crack to a convex profile decaying to zero within the cohesive crack.

The main difference between the reversible and irreversible cases consists in the presence of a residual plastic wake along the brittle crack edges in the irreversible case (Figure11(middle right)), while the inelastic strain𝒑\boldsymbol{p}returns to 0 outside of a strip of width 1 element along which it localizes (Figure11(middle left)).
This has a significant impact on the balance between stored elastic energy and that dissipated during crack growth.

Figure13reports the evolution of the elastic energyEelE_{\mathrm{el}}, the plastic workEplE_{\mathrm{pl}}, and the damage dissipationEdmgE_{\mathrm{dmg}},Eel=∫Ωμ2​‖∇u−𝒑‖2​dAEpl=∫Ω𝗄​(α)​τc​p¯​dAEdmg=𝖦c4​𝖼𝗐​∫Ω(𝗐​(α)ℓ+ℓ​‖∇α‖2)​dAE_{\mathrm{el}}=\int_{\Omega}\frac{\mu}{2}\|\nabla u-\boldsymbol{p}\|^{2}\,\mathrm{d}A\qquad E_{\mathrm{pl}}=\int_{\Omega}\mathsf{k}(\alpha)\,\tau_{c}\,\bar{p}\,\,\mathrm{d}A\qquad E_{\mathrm{dmg}}=\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\int_{\Omega}\left(\frac{\mathsf{w}(\alpha)}{\ell}+\ell\|\nabla\alpha\|^{2}\right)\,\mathrm{d}A

wherep¯\bar{p}is the cumulated nonlinear deformation of Remark1, reducing to‖𝒑‖\|\boldsymbol{p}\|in the reversible case; the plastic work is recoverable in the reversible case and dissipated when𝒑\boldsymbol{p}is irreversible (Remark6).
Past the loading ramp, in the reversible case the damage dissipation grows at a constant rate while the plastic work remains constant.
In the irreversible case, however, the plastic work grows linearly as well, which is consistent with the presence of a residual plastic wake behind a crack tip translating at constant speed.Figure 13:Energy and crack-tip evolution vs. crack advancexc−L0x_{c}-L_{0}(solid: reversible,
dashed: irreversible). (left) Energy components.
(right) Position of the brittle and cohesive crack tipsPP(α≥0.95\alpha\geq 0.95) andQQ(α≤0.02\alpha\leq 0.02).

Figure14shows the rate of energy dissipated per unit of crack length𝖦ceff:=d​𝒟/d​a=∂(Edmg+Epl)∂a\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}:=\mathrm{d}\mathcal{D}/\mathrm{d}a=\frac{\partial(E_{\rm dmg}+E_{\rm pl})}{\partial a}

as the crack grows through the region shown in gray in Figure13for multiple values of the ratiosℓ/ℓch\ell/\ell_{\mathrm{ch}}andh/ℓh/\ellin order to compensate for mesh size-induced toughening in the reversible (left) and irreversible (right) cases.
The average and standard deviation of𝖦ceff\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}while the crack propagates through this area are denoted by colored markers and shaded areas respectively.
In the reversible case𝖦ceff\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}matches the classical correction𝖦c​(1+h/(4​𝖼𝗐​ℓ))\mathsf{G}_{\mathrm{c}}\left(1+h/(4\mathsf{c_{w}}\ell)\right)and approaches𝖦c\mathsf{G}_{\mathrm{c}}ash/ℓ→0h/\ell\to 0, independently ofℓch\ell_{\mathrm{ch}}, so that𝖦c\mathsf{G}_{\mathrm{c}}can be interpreted as the rate at which energy is dissipated during the fracture growth process; this is not the case in the irreversible one.
Instead, we observe that in the limit ofh→0h\to 0,𝖦ceff≃1.3​𝖦c\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}\simeq 1.3\mathsf{G}_{\mathrm{c}}.
This is consistent with the fact that in order to grow a crack by an increment of lengthd​a\mathrm{d}a, one needs to propagate the damage profile by the same amount (at a cost of𝖦c​d​a\mathsf{G}_{\mathrm{c}}\,\mathrm{d}a, up to discretization effects) and also the plastic zone, at a cost that remains to be identified analytically.
We argue that in this case, the material’s fracture toughness is𝖦ceff\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}and not𝖦c\mathsf{G}_{\mathrm{c}}, which only accounts for the damage dissipation, and would need to be evaluated numerically by estimatingd​Epl/d​a{\mathrm{d}E_{\rm pl}}/{\mathrm{d}a}, perhaps using this surfing experiment.Figure 14:Effective toughness𝖦ceff=d​𝒟/d​a\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}=\mathrm{d}\mathcal{D}/\mathrm{d}aversush/ℓh/\ell(steady-state slope, one series perℓ/ℓch\ell/\ell_{\mathrm{ch}}; domain lengthW=4​ℓchW=4\,\ell_{\mathrm{ch}}, mesh refined in a band of half-widthℓch/2\ell_{\mathrm{ch}}/2around the crack path) for reversible (left) and irreversible (right) plasticity. Dashed: fitsG0​(1+h/(4​𝖼𝗐​ℓ))G_{0}\,(1+h/(4\mathsf{c_{w}}\ell))with𝖼𝗐=12\mathsf{c_{w}}=\tfrac{1}{2}, the value of𝖬𝟣\mathsf{M1}atζ=1\zeta=1; red: the same law withG0=𝖦cG_{0}=\mathsf{G}_{\mathrm{c}},i.e.the classical mesh-induced toughening. Bands and error bars: one standard deviation.

## 6.3V-notch

## 6.3.1Geometry and loading

Our last set of numerical experiments focuses on crack growth from a V-notch and, in doing so, bridges two classical descriptions of failure at a stress concentrator: the small-scale yielding (SSY) solution of perfect plasticity at the notch tip[44,72]and the cohesive crack of Dugdale[33]and Barenblatt[11].

We consider the “Pac-Man” geometry from[78], consisting of a disk of radiusRRwith a re-entrant V-notch with complementary half-angleπ/2≤ω≤π\pi/2\leq\omega\leq\pioccupied by an isotropic homogeneous material (see Figure10, right).

The dominant terms in a power series expansion of the antiplane mode-III elastic displacement and stress fields are given in[73]byu​(ρ,θ)=tμ​λ​(2​π​ρ)λ−1​ρ​sin⁡(λ​θ),𝝉​(ρ,θ)=t​(2​π​ρ)λ−1​(sin⁡(λ​θ)​e¯ρ+cos⁡(λ​θ)​e¯θ),u(\rho,\theta)=\frac{t}{\mu\,\lambda}\,(2\pi\rho)^{\lambda-1}\,\rho\,\sin(\lambda\theta),\qquad\boldsymbol{\tau}(\rho,\theta)=t\,(2\pi\rho)^{\lambda-1}\bigl(\sin(\lambda\theta)\,\underline{e}_{\rho}+\cos(\lambda\theta)\,\underline{e}_{\theta}\bigr),(77)

where(ρ,θ)(\rho,\theta)denotes polar coordinates emanating from the notch tip withθ=0\theta=0corresponding to the ligament andθ=±ω\theta=\pm\omegathe notch faces.
The loading magnitude istt, andλ=π2​ω∈(12,1)\lambda=\frac{\pi}{2\omega}\in\bigl(\tfrac{1}{2},1\bigr)is the exponent of the displacement singularity at the notch tip.
The magnitude of the stress field nearρ=0\rho=0is therefore independent ofθ\theta:‖𝝉​(ρ,θ)‖=t​(2​π​ρ)λ−1\|\boldsymbol{\tau}(\rho,\theta)\|=t(2\pi\rho)^{\lambda-1}, so that𝝉​(ρ,0)=t​(2​π​ρ)λ−1​e¯θ\boldsymbol{\tau}(\rho,0)=t\,(2\pi\rho)^{\lambda-1}\,\underline{e}_{\theta}.
It is customary to define the generalized stress intensity factor (GSIF) of the notch:KV=limr→0+(2​π​r)1−λ​τ​(r,0)=t,K_{V}=\lim_{r\to 0^{+}}(2\pi r)^{\,1-\lambda}\,\tau(r,0)=t,

which reduces to the classical mode-III stress-intensity factor in the limitω→π\omega\to\pi, corresponding to a crack, withλ=12\lambda=\tfrac{1}{2}.

On the circular part of the boundary of the domain, we prescribe the boundary displacement given by (77) so thatKV=tK_{V}=ti.e.the magnitude of the prescribed displacement is the V-notch GSIF, while the notch edges are left stress-free.
In this setting, the critical loading parametertc=KV∗t_{c}=K_{V}^{*}plays the role of a notch toughness whose physical dimensionτc​ℓ1−λ\tau_{c}\,\ell^{\,1-\lambda}varies withω\omega, and which interpolates, as in the plane-elasticity coupled criterion of[51,24], between the strengthτc\tau_{c}in the limit (ω→π/2\omega\to\pi/2,λ→1\lambda\to 1) of a straight edge and the Griffith toughnessKc=2​μ​𝖦cK_{c}=\sqrt{2\mu\mathsf{G}_{\mathrm{c}}}when the notch degenerates into a crack (ω=π\omega=\pi,λ=12\lambda=\tfrac{1}{2}).
Again, we assume symmetry (or anti-symmetry) of the solution with respect to thexx-axis and perform our computations on a half-domain.

While the elastic solution admits a singularity at the notch tip, in the small-scale yielding regime, this singularity gives way to a process zone where the stress constraint‖𝝉‖=τc\|\boldsymbol{\tau}\|=\tau_{c}is saturated.
Following the construction of[72,73], it is a lobe of the curve defined byr​(θ)=a0​cos⁡(m​θ),|θ|≤π2​m,m=λ1−λ,a0=1π​(|t|τc)1/(1−λ),r(\theta)=a_{0}\cos(m\theta),\quad|\theta|\leq\frac{\pi}{2m},\qquad m=\frac{\lambda}{1-\lambda},\quad a_{0}=\frac{1}{\pi}\left(\frac{|t|}{\tau_{c}}\right)^{1/(1-\lambda)},(78)

and depends only on the notch angleω\omegaand the loading parametertt.
Note that in the limit of a crack (ω=π\omega=\pi,λ=12\lambda=\tfrac{1}{2},m=1m=1) it degenerates to the Hult–McClintock circle through the tip[44]while as the wedge blunts (ω→π/2\omega\to\pi/2) the lobe narrows into a needle along the ligament.
The amplitudea0a_{0}is the forward reach of this lobe (the value ofrratθ=0\theta=0), andb0=2​a0​max|θ|≤π/2​m⁡cos⁡(m​θ)​sin⁡θb_{0}=2a_{0}\max_{|\theta|\leq\pi/2m}\cos(m\theta)\sin\thetaits full transverse width, the small-scale yielding counterparts of the measured process-zone extentsaaandbb. For a crack the lobe is circular anda0=b0a_{0}=b_{0}, while the aspect ratiob0/a0b_{0}/a_{0}falls to0.710.71atω=5​π/6\omega=5\pi/6and vanishes asω→π/2\omega\to\pi/2.

## 6.3.2Simulation results

As in the rest of this section we adopt the𝖬𝟣\mathsf{M1}family withζ=1\zeta=1, for which the equivalent cohesive law is linear and the homogeneous response has no constant-stress plateau, and we keepμ=τc=1\mu=\tau_{c}=1, so that the elasto-cohesive lengthℓch=μ​𝖦c/τc2=𝖦c\ell_{\mathrm{ch}}=\mu\mathsf{G}_{\mathrm{c}}/\tau_{c}^{2}=\mathsf{G}_{\mathrm{c}}is set by the toughness alone.
The nonlinear deformation𝒑\boldsymbol{p}is taken reversible, as in the first series of simulations of Section6.2.
The domain radius isR=10R=10and we set the regularization lengthℓ=0.4\ell=0.4.
The mesh is refined along the expected crack path, withh≃0.02h\simeq 0.02(h/ℓ=0.05h/\ell=0.05) in a band of half-width1.5​ℓ1.5\ellaround the ligament, coarsening toh=2h=2atρ=R\rho=R; the loading is applied in151151increments and the alternate-minimization tolerance is10−310^{-3}.
Two critical loads are reported below: the peak-force loadtc≡KV∗t_{c}\equiv K_{V}^{*}, and the loadt∗t^{*}at which localization is first detected (maxΩ⁡α≥0.95\max_{\Omega}\alpha\geq 0.95).
They are separated by1.51.5load increments (Δ​t≃0.014​τc\Delta t\simeq 0.014\,\tau_{c}),i.e.they coincide to within the load discretization.

We focus first on the degenerate case of a crack (ω=179​π180≃π\omega=\frac{179\pi}{180}\simeq\pi).
Figure15(top row) shows the evolution of the reaction force and of the strength zone{‖𝝉‖=𝗄​(α)​τc}\{\|\boldsymbol{\tau}\|=\mathsf{k}(\alpha)\tau_{c}\}as a function of the loading parameter, while the bottom rows show snapshots in time of the damage variable, inelastic strain, and magnitude of the stress.
In all the field maps that follow, the white solid line is the boundary‖𝝉‖=𝗄​(α)​τc\|\boldsymbol{\tau}\|=\mathsf{k}(\alpha)\,\tau_{c}of the strength zone and the white dashed line the small-scale-yielding lobe (78).
The snapshotsAAandBBare taken att=0.80​t∗t=0.80\,t^{*}andt=0.93​t∗t=0.93\,t^{*},CCat the last converged step before localization, andDDat the first localized one.

We identify three regimes.
In a first phase, until a point labeled asAAin Figure15, we observe a circular plastic zone closely matching the Hult–McClintock circle.
We observe a small damaged region near the crack tip.
In this region, we have‖𝝉‖=𝗄​(α)​τc<τc\|\boldsymbol{\tau}\|=\mathsf{k}(\alpha)\,\tau_{c}<\tau_{c}which explains why the magnitude of the stress is not constant.

FromAAonward, the strength zone becomes progressively elongated, with a forward reachaaand a transverse widthbbsuch thata>ba>b,bbexceedingb0b_{0}by2020–25%25\%.
Damage near the notch tip increases significantly.
This is the precursor to crack growth, where the solution progressively departs from the classical elastic / perfectly plastic one.
The snapshots att=Bt=Bandt=Ct=Cconfirm this trend: a significant increase of the damage near the notch and a plastic zone becoming more elongated.
The stresses do not vanish ahead of the pre-existing crack, so that we interpret this phase as the progressive growth of a cohesive crack.

Finally, att=Dt=Dwe observe a sudden bifurcation in the solution with the nucleation of a brittle crack, characterized by the classical phase-field crack profile forα\alpha, the localization of𝒑\boldsymbol{p}on a strip along thexx-axis in which stresses vanish, and the sudden fall of the reaction force.
We view this instant as the sudden nucleation of a brittle crack.

Note that the onset of both cohesive and brittle cracks exceeds the threshold at which a brittle crack would nucleate in a classical phase-field model, even when using undamaged boundary conditions applied to crack edges, as seen in[78].

Note that throughout the evolution, the sizeaaof the process zone remains small compared to the domain size, but grows to be of the order ofℓch\ell_{\mathrm{ch}}when the brittle crack nucleates, reachinga/R≃0.13a/R\simeq 0.13: the hypotheses of the small-scale yielding theory are therefore only marginally satisfied at nucleation.Figure 15:Near-crack overview,ω=179∘\omega=179^{\circ}(ℓ=0.4\ell=0.4,ℓch=1\ell_{\mathrm{ch}}=1,R=10R=10;tc=1.616t_{c}=1.616,t∗=1.637t^{*}=1.637). Top: (a) forceF/(τc​ℓch)F/(\tau_{c}\ell_{\mathrm{ch}})versus the GSIFt=KVt=K_{V}, withtc=KV∗t_{c}=K_{V}^{*}(dashed), the Griffith loadKcK_{c}(gray) and the snapshotsAA–CC; (b) extentsa,ba,bof the strength zone against the SSYa0=b0a_{0}=b_{0}(78), up to nucleation. Bottom: tip-zoom maps ofα\alpha,‖𝒑‖​h/ℓch\|\boldsymbol{p}\|\,h/\ell_{\mathrm{ch}}(log) and‖𝝉‖/τc\|\boldsymbol{\tau}\|/\tau_{c}atAA–DD(rows),DDthe first localized state.

Figure16focuses on the last phase of the evolution.
Just as in the surfing computations, we observe a brittle crack ending at pointxPx_{P}followed by a cohesive tip extending tox=xQx=x_{Q}, clearly indicated by the slow transition ofα\alphafrom 1 to 0 along thexx-axis and the elongated plastic zone originating fromxPx_{P}(xPx_{P}is the last point ony=0y=0where‖𝝉‖<0.05​τc\|\boldsymbol{\tau}\|<0.05\,\tau_{c}, andxQx_{Q}the first one whereα<0.05\alpha<0.05).
Stresses vanish along the edges of the brittle crack but not of the cohesive one, and reach a maximum of the order ofτc\tau_{c}near its tip (see Figure15(bottom)).
Half the crack opening is estimated by integrating‖𝒑‖\|\boldsymbol{p}\|over0<y<3​ℓ/20<y<3\ell/2on the computed half-domain, so thatδ=⟦u⟧/2\delta=\left\llbracket u\right\rrbracket/2.
We see that along the length of the brittle crack, this measure compares to the value ofuutaken aty=3​ℓ/2y=3\ell/2, which is consistent with a stress-free crack, and decays down to 0 within the cohesive crack, forming a convex curve, a key feature of a cohesive crack as compared to the parabolic profile of a brittle crack.Figure 16:Nucleated state atω=179​π180\omega=\tfrac{179\pi}{180}(179∘179^{\circ};t=t∗=1.637t=t^{*}=1.637; crack lengthLcrack=1.83L_{\mathrm{crack}}=1.83, tip process-zone lengthℓtip=1.34\ell_{\mathrm{tip}}=1.34). Top: tip-zoom maps as in Figure15, with the crack tipPPand the process-zone tipQQatxP=Lcrackx_{P}=L_{\mathrm{crack}}andxQ=xP+ℓtipx_{Q}=x_{P}+\ell_{\mathrm{tip}}. Bottom: profiles alongy=0y=0ofα\alphaand‖𝝉‖/τc\|\boldsymbol{\tau}\|/\tau_{c}(left axis) and of the openingδ=∫‖𝒑‖​dy\delta=\int\|\boldsymbol{p}\|\,\mathrm{d}y(right axis); the gray band is the process zoneP​QPQ.

As the notch angle decreases, we observe a qualitatively similar scenario (see Figure17for a notch angle of150∘150^{\circ}).
Up to the load labeledAAin the figure, damage is limited and the forward reachaaof the strength zone follows the SSY prediction (78) to within7%7\%up tot≃τct\simeq\tau_{c}, while its transverse width exceedsb0b_{0}by about30%30\%throughout.
From pointAAonward, we observe the growth of a cohesive crack, while the plastic zone becomes increasingly elongated, up to the critical loadKV=KV∗K_{V}=K^{*}_{V}at which a brittle crack is suddenly nucleated, as indicated by the sudden drop in reaction force in Figure17(top left) and the change in the geometry of the plastic zone (Figure17(top right)).
Note how the geometry of the plastic zone becomes similar to that observed at the crack tip in the surfing problem (Figure11).Figure 17:Blunt-wedge overview,ω=5​π6\omega=\tfrac{5\pi}{6}(150∘150^{\circ};ℓ=0.4\ell=0.4,ℓch=1\ell_{\mathrm{ch}}=1,R=10R=10;tc=1.456t_{c}=1.456,t∗=1.475t^{*}=1.475). Same panels, fields and colormaps as Figure15, with the Rice petal (78) (a0≠b0a_{0}\neq b_{0}) in place of the Hult–McClintock circle; here the three snapshotsAA–CCall precede nucleation, so there is no rowDD.

Figure18(left) shows the critical loadKV∗K^{*}_{V}as a function of the notch angle and of the elasto-cohesive lengthℓch\ell_{\mathrm{ch}}, compared to that computed using the sharp-interface model of[75]; these simulations useℓ=0.1\ell=0.1, with a mesh sizeh=ℓ/5h=\ell/5in the refined band, rather than theℓ=0.4\ell=0.4of the field computations above.
Asω→90∘\omega\to 90^{\circ}, we observe nucleation atKV∗=τcK_{V}^{*}=\tau_{c}, which is consistent with our one-dimensional analysis and the tearing simulations.
As in Figure15, for sharp cracks, we observe that re-nucleating a crack from an existing notch requiresKV∗>Kc=2​μ​𝖦cK_{V}^{*}>K_{c}=\sqrt{2\mu\mathsf{G}_{\mathrm{c}}}.
While this is consistent with the fact that some energy is dissipated creating a plastic zone near the crack tip before re-nucleation, we cannot rule out that our numerical scheme may overshoot the nucleation threshold.
However, based on the experience gained in[78], we argue that this overshoot is typically small and would not account for the discrepancy observed here.

Figure18(right) shows the same data through the dimensionless groupk=1λ​(2​π​ℓch)λ−1​KV∗τc,k=\frac{1}{\lambda}\left(2\pi\ell_{\mathrm{ch}}\right)^{\lambda-1}\frac{K_{V}^{*}}{\tau_{c}},

normalized so thatk=1k=1in the strength-dominated limit (ω=π/2\omega=\pi/2,λ=1\lambda=1,KV∗=τcK_{V}^{*}=\tau_{c}) andk=2/π≃1.13k=2/\sqrt{\pi}\simeq 1.13in the Griffith limit (ω=π\omega=\pi,λ=12\lambda=\tfrac{1}{2},KV∗=KcK_{V}^{*}=K_{c}).
All the simulations collapse on a single curve, independent ofℓch\ell_{\mathrm{ch}}, following the “universal law” suggested in[60].
The collapsed curve reachesk≃1.26k\simeq 1.26in the crack limit, about12%12\%above the sharp-interface value of[75]; about half of this excess is accounted for by the mesh-induced toughening factor(1+h/(4​𝖼𝗐​ℓ))1−λ≃1.05(1+h/(4\mathsf{c_{w}}\ell))^{1-\lambda}\simeq 1.05at the discretization used here, the remaining≃6%\simeq 6\%being attributable to the plastic dissipation preceding re-nucleation.Figure 18:Critical load at the onset of the brittle crack,ℓ=0.1\ell=0.1,ℓch∈{0.5,1,2}\ell_{\mathrm{ch}}\in\{0.5,1,2\}(one color per series), against the sharp-interface model of[75](solid lines, crosses). (left) Peak-force loadtc=KV∗t_{c}=K_{V}^{*}versusω\omega. (right) Same data through the groupkk, which collapses the series (gray dashed: cubic fit throughℓch=1\ell_{\mathrm{ch}}=1); dotted: the strength and Griffith limitsk=1k=1,2/π≃1.132/\sqrt{\pi}\simeq 1.13.

## 7Conclusions and extensions

We have presented a mathematical analysis and carefully tailored numerical simulations of the model (1), introduced in[19], in the antiplane setting. Its variational structure is the basis of our formulation and our numerical algorithm, which alternates the minimization of the total energy with respect to the displacement and the nonlinear deformation, and with respect to the damage variable, each subproblem being reformulated as a second-order cone program and solved to global optimality.

In the antiplane setting, one of the most delicate features of the full model disappears: since the nonlinear deformation is a vector, every localized deformation is a compatible jump, and the strength domain no longer restricts the admissible jump directions as it does in three dimensions.
This is precisely what makes this simplified setting precious: it allows us to study all the other properties of the model independently of the jump compatibility condition, and to highlight the most fundamental aspect of this family of models — its ability to bridge the gap between limit analysis, perfect plasticity, cohesive fracture, and brittle fracture.
In particular, we have shown that the small-scale yielding crack-tip plastic zone can localize along a line, leading to the propagation of a cohesive crack which, as the opening becomes larger, degenerates into a Griffith-like brittle crack.
Our numerical results thus disclose the missing path for unifying small-scale-yielding analysis with cohesive crack-band approaches within a single consistent nonlinear model, able to predict both crack nucleation and propagation.

The numerical simulations substantiate these claims quantitatively.
We have focused our investigations on simple geometries of universal interest, to disclose the fundamental behavior of the proposed model.
On the simple shear problem, the computed evolutions reproduce the closed-form solutions of Sections3and4: the equivalent cohesive law and the associated energy balance are recovered independently ofℓ\ell, the dissipated energy exceeds𝖦c\mathsf{G}_{\mathrm{c}}only by the mesh-toughening factor1+h/(4​𝖼𝗐​ℓ)1+h/(4\mathsf{c_{w}}\ell), matched to better than1%1\%forh≤ℓ/5h\leq\ell/5, and the size effect — the transition from progressive failure to snap-back — is governed by the ratioL/ℓchL/\ell_{\mathrm{ch}}; in the linearly rigid limit, the measured force–displacement curve is the cohesive law itself.
The surfing simulations measure the energy dissipated per unit crack advance: the effective toughness𝖦ceff\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}coincides with the prescribed𝖦c\mathsf{G}_{\mathrm{c}}when𝒑\boldsymbol{p}is unconstrained, while an irreversibility constraint on𝒑\boldsymbol{p}leaves a residual plastic wake behind the tip and raises𝖦ceff\mathsf{G}_{\mathrm{c}}^{\mathrm{eff}}to about1.3​𝖦c1.3\,\mathsf{G}_{\mathrm{c}}.
At the V-notch, a single monotonic loading drives the tip fields through three classical regimes — the confined small-scale-yielding plastic zone of Hult and McClintock, a Barenblatt-type cohesive crack, and a stress-free brittle crack — and the nucleation loads for all notch angles and material lengths collapse onto the “universal law” of[60], interpolating between the strength-dominated limitKV∗=τcK_{V}^{*}=\tau_{c}and the toughness-dominated Griffith limitKV∗=2​μ​𝖦cK_{V}^{*}=\sqrt{2\mu\mathsf{G}_{\mathrm{c}}}, within about6%6\%of the sharp-interface computations of[75], once the mesh-induced toughening of the regularized model is discounted.
Taken together, these results exhibit limit analysis, perfect plasticity, cohesive fracture, and brittle fracture as asymptotic regimes of a single variational model with one set of material data(μ,τc,𝖦c)(\mu,\tau_{c},\mathsf{G}_{\mathrm{c}}), the transitions between them selected by the loading and by the ratiosℓ/ℓch\ell/\ell_{\mathrm{ch}}andL/ℓchL/\ell_{\mathrm{ch}}, rather than by a change of constitutive description.

Unlike conventional phase-field models, originally introduced in[18]and the subject of countless extensions since then, our model accounts for a strength surface that is fully independent of the elastic properties and of the regularization parameterℓ\ell.
As such, the parameterℓ\ell, which is often interpreted as an internal length in classical phase-field models, can be chosen as a purely numerical regularization parameter with little impact on the computational results, provided that it is small compared to the dimensions of the structure and to the characteristic size of the patterns it develops.

Viewed as a regularized model of softening plasticity, the present model also achieves what, to our knowledge, other softening-plasticity approaches[69,64,50,12,46,37,54,9]have not reached: the identification of a clear underlying sharp-interface model, the cohesive energy (4).

Finally, the model we studied and the numerical implementation we proposed extend naturally to two- and three-dimensional elasticity[19], where the choice of strength surface, constitutive relation, and cohesive law will lead to a broader gamut of behaviors that remain to be explored.
In this vectorial setting, with tensorial strains and stresses, the jump compatibility condition comes into play: a careful analysis of its practical implications is the subject of ongoing work and will be presented in a separate paper.
Similarly, minor modifications, such as the irreversibility constraint on𝒑\boldsymbol{p}already explored in the surfing example of Section6.2, open the way to more complex material behaviors, including ductile fracture or fatigue.
However, while the present model offers a promising starting point, it is still far from a complete theory of ductile fracture: this would require substantial long-term developments, including a proper account of permanent plastic deformations, the modeling of a hardening regime, and multiaxial strength surfaces — a program to which our future work will be devoted.

## Acknowledgements

BB acknowledges the support of the Natural Sciences and
Engineering Research Council of Canada (NSERC), RGPIN-2022-04536 and the Canada
Research Chair program.
CM received funding from the European Union’s Horizon 2020 research and
innovation program under the Marie Skłodowska-Curie grant agreement
No. 861061 — NEWFRAC Project.

## Appendices

## Appendix AConic reformulations of the alternate-minimization subproblems

This appendix details the conic-programming reformulations of the two convex subproblems solved at each iteration of the alternate-minimization scheme of Section5(Algorithm1).

## A.1Convex-cone reformulation of the(u,𝒑)(u,\boldsymbol{p})subproblem

The first subproblem consists in minimizing the energy with respect to(u,𝒑)(u,\boldsymbol{p})at fixedα\alpha:minu,𝒑​∫Ωφ​(∇u,𝒑,α)​dA,φ​(∇u,𝒑,α)=μ2​‖∇u−𝒑‖2+𝗄​(α)​τc​‖𝒑‖.\min_{u,\boldsymbol{p}}\int_{\Omega}\varphi(\nabla u,\boldsymbol{p},\alpha)\,\mathrm{d}A,\qquad\varphi(\nabla u,\boldsymbol{p},\alpha)=\frac{\mu}{2}\|\nabla u-\boldsymbol{p}\|^{2}+\mathsf{k}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|.(79)

The non-smooth term‖𝒑‖\|\boldsymbol{p}\|limits the effectiveness of standard gradient-based optimization algorithms.
Following[15], we reformulate (79) as a Second-Order Cone Programming (SOCP) problem[53], which can be solved robustly and efficiently using the MOSEK software[8], without the need for smoothing.
This approach is also flexible and can be extended to vector-valued displacements and non-smooth multiaxial strength domains.

Introducing auxiliary scalar variablesssandzz, the energy density can be equivalently expressed as the partial minimizationφ​(∇u,𝒑,α)\displaystyle\varphi(\nabla u,\boldsymbol{p},\alpha)=mins,z≥0⁡μ​s+𝗄​(α)​τc​z\displaystyle=\min_{s,z\geq 0}\;\mu\,s+\mathsf{k}(\alpha)\,\tau_{c}\,z(80)subject to2​s≥‖∇u−𝒑‖2,\displaystyle\qquad 2s\geq\|\nabla u-\boldsymbol{p}\|^{2},z≥‖𝒑‖,\displaystyle\qquad z\geq\|\boldsymbol{p}\|,

which turns the non-smooth objective into a linear one at the cost of introducing cone constraints.
These constraints are expressed using the second-order cone𝒬n+1\mathcal{Q}^{n+1}and the rotated second-order cone𝒬rn+2\mathcal{Q}_{\mathrm{r}}^{n+2}, standard types natively supported by MOSEK[8]:𝒬n+1\displaystyle\mathcal{Q}^{n+1}:={(r,x)∈ℝ×ℝn:r≥‖x‖},\displaystyle=\{(r,x)\in\mathbb{R}\times\mathbb{R}^{n}:r\geq\|x\|\},(81)𝒬rn+2\displaystyle\mathcal{Q}_{\mathrm{r}}^{n+2}:={(r1,r2,x)∈ℝ2×ℝn:2​r1​r2≥‖x‖2,r1,r2≥0}.\displaystyle=\{(r_{1},r_{2},x)\in\mathbb{R}^{2}\times\mathbb{R}^{n}:2\,r_{1}r_{2}\geq\|x\|^{2},\;r_{1},r_{2}\geq 0\}.

Settingei:=u,i−pie_{i}:=u_{,i}-p_{i}fori=1,2i=1,2, the constraintz≥‖𝒑‖z\geq\|\boldsymbol{p}\|reads(z,p1,p2)∈𝒬3(z,p_{1},p_{2})\in\mathcal{Q}^{3}and the constraint2​s≥‖∇u−𝒑‖22s\geq\|\nabla u-\boldsymbol{p}\|^{2}reads(s,1,e1,e2)∈𝒬r4(s,1,e_{1},e_{2})\in\mathcal{Q}_{\mathrm{r}}^{4}.

In order to discretize (80), we introduce the discrete gradient matrix𝖡\mathsf{B}of size2​ng×nn2n_{g}\times n_{n}, defined by𝖡g​k:=∇χk​(xg),so that𝖡𝖴={∇u​(xg)}g=1ng,\mathsf{B}_{gk}:=\nabla\chi_{k}(x_{g}),\qquad\text{so that}\qquad\mathsf{B}\mathsf{U}=\left\{\nabla u(x_{g})\right\}_{g=1}^{n_{g}},(82)

mapping the nodal values of the discretization𝖴\mathsf{U}of the displacement byℙ1\mathbb{P}_{1}simplicial Lagrange finite elements to its gradient at all quadrature points.
Dirichlet boundary conditions are enforced as equality constraints on the nodal values:𝖴k=u¯​(xk),∀k∈ℐ∂uΩ,\mathsf{U}_{k}=\bar{u}(x_{k}),\quad\forall\,k\in\mathcal{I}_{\partial_{u}\Omega},(83)

whereℐ∂uΩ\mathcal{I}_{\partial_{u}\Omega}denotes the set of indices of nodes on∂uΩ\partial_{u}\Omega.
Applying the local reformulation (80) pointwise at each quadrature pointxgx_{g}and assembling over the mesh with the quadrature weightsρg\rho_{g}(equal to the cell areas for the one-point rule), the discrete elastoplastic subproblem becomes the SOCP:min𝖴,𝖯,𝗌,𝗓\displaystyle\min_{\mathsf{U},\mathsf{P},\mathsf{s},\mathsf{z}}∑g=1ngρg​(μ​sg+𝗄​(αg)​τc​zg)\displaystyle\sum_{g=1}^{n_{g}}\rho_{g}\left(\mu\,s^{g}+\mathsf{k}(\alpha^{g})\,\tau_{c}\,z^{g}\right)(84)subject toeig=(𝖡𝖴)ig−pig,i=1,2,g=1,…,ng,\displaystyle e_{i}^{g}=(\mathsf{B}\mathsf{U})_{i}^{g}-p_{i}^{g},\quad i=1,2,\;g=1,\ldots,n_{g},(sg,1,e1g,e2g)∈𝒬r4,g=1,…,ng,\displaystyle(s^{g},1,\,e_{1}^{g},\,e_{2}^{g})\in\mathcal{Q}_{\mathrm{r}}^{4},\quad g=1,\ldots,n_{g},(zg,p1g,p2g)∈𝒬3,g=1,…,ng,\displaystyle(z^{g},\,p_{1}^{g},\,p_{2}^{g})\in\mathcal{Q}^{3},\quad g=1,\ldots,n_{g},𝖴k=u¯​(xk),∀k∈ℐ∂uΩ.\displaystyle\mathsf{U}_{k}=\bar{u}(x_{k}),\quad\forall\,k\in\mathcal{I}_{\partial_{u}\Omega}.

In the implementation, the strength degradation function is replaced by𝗄​(α)+𝗄res\mathsf{k}(\alpha)+\mathsf{k}_{\mathrm{res}}with a small residual strength (𝗄res=10−6\mathsf{k}_{\mathrm{res}}=10^{-6}for the simple-shear computations,10−410^{-4}for the surfing and V-notch ones), so that the coefficient ofzgz^{g}in the objective never vanishes whenα→1\alpha\to 1and the conic problem remains well-posed.
The SOCP is solved with the interior-point conic optimizer of MOSEK[8]with feasibility and relative-gap tolerances set to10−810^{-8}.

The formulation above extends directly to the rigid limitμ→∞\mu\to\infty, used in Section6.1to compute the response of a rigid bar.
In this case the elastic strain must vanish: the auxiliary variablessgs^{g}and the rotated-cone constraints are dropped, and the elastic strain definition is replaced by the pointwise kinematic constraintρg​((𝖡𝖴)ig−pig)=0,i=1,2,g=1,…,ng,\rho_{g}\left((\mathsf{B}\mathsf{U})_{i}^{g}-p_{i}^{g}\right)=0,\quad i=1,2,\;g=1,\ldots,n_{g},(85)

so that the objective reduces to the plastic term∑gρg​𝗄​(αg)​τc​zg\sum_{g}\rho_{g}\,\mathsf{k}(\alpha^{g})\,\tau_{c}\,z^{g}.
The stress at the quadrature points is then recovered as the dual (Lagrange) multiplier of the equality constraints (85), directly provided by the conic optimizer.

## A.2Minimization with respect to the damage field

The second subproblem consists in minimizing the energy with respect toα\alphaat fixed(u,𝒑)(u,\boldsymbol{p}), under the bound constraints given by irreversibility and the upper boundα≤1\alpha\leq 1:minα​∫Ω𝗄​(α)​τc​‖𝒑‖+𝖦c4​𝖼𝗐​(𝗐​(α)ℓ+ℓ​‖∇α‖2)​d​A,subject toαi−1≤α≤1.\min_{\alpha}\int_{\Omega}\mathsf{k}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|+\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\left(\frac{\mathsf{w}(\alpha)}{\ell}+\ell\,\|\nabla\alpha\|^{2}\right)\,\mathrm{d}A,\qquad\text{subject to}\quad\alpha_{i-1}\leq\alpha\leq 1.(86)

Under Hypothesis1with𝗄\mathsf{k}convex and𝗐\mathsf{w}convex, this is a convex optimization problem with simple pointwise bound constraints.
For the family𝖬𝟣\mathsf{M1}, where𝗄\mathsf{k}is affine and𝗐\mathsf{w}is quadratic inα\alpha, we also discretize the damage field withℙ1\mathbb{P}_{1}simplicial Lagrange finite elements and cast it directly in conic form.
Let𝖣\mathsf{D}collect the nodal values of the damage field, so that the damageα​(xg)=∑k𝖣k​χk​(xg)\alpha(x_{g})=\sum_{k}\mathsf{D}_{k}\chi_{k}(x_{g})and its gradient∇α​(xg)\nabla\alpha(x_{g})are determined at the quadrature points.
The subproblem then readsmin𝖣,z\displaystyle\min_{\mathsf{D},\,z}z+𝖻T​𝖣\displaystyle z+\mathsf{b}^{T}\mathsf{D}(87)subject to(z,12,𝖫𝖣)∈𝒬r,𝖣i−1,k≤𝖣k≤1,∀k=1,…,nn,\displaystyle(z,\,\tfrac{1}{2},\,\mathsf{L}\mathsf{D})\in\mathcal{Q}_{\mathrm{r}},\qquad\mathsf{D}_{i-1,k}\leq\mathsf{D}_{k}\leq 1,\quad\forall\,k=1,\ldots,n_{n},

where the auxiliary scalarzzand the rotated cone𝒬r\mathcal{Q}_{\mathrm{r}}of (81) enforcez≥‖𝖫𝖣‖2z\geq\|\mathsf{L}\mathsf{D}\|^{2}, turning the quadratic damage energy into a linear objective.
We do not factorize a global stiffness matrix: since with one-point quadrature the quadratic damage energy is already a sum of squares over the quadrature points, the vector𝖫𝖣\mathsf{L}\mathsf{D}is built point by point by stacking the damage and its gradient at eachxgx_{g}, each scaled by the square root of the corresponding (positive, scalar) energy weight,𝖫𝖣={cg​α​(xg),dg​∂1α​(xg),dg​∂2α​(xg)}g=1ng,cg=𝖦c​ζ​ρg4​𝖼𝗐​ℓ,dg=𝖦c​ℓ​ρg4​𝖼𝗐,\mathsf{L}\mathsf{D}=\Big\{\,\sqrt{c_{g}}\;\alpha(x_{g}),\;\;\sqrt{d_{g}}\;\partial_{1}\alpha(x_{g}),\;\;\sqrt{d_{g}}\;\partial_{2}\alpha(x_{g})\,\Big\}_{g=1}^{n_{g}},\qquad c_{g}=\frac{\mathsf{G}_{\mathrm{c}}\,\zeta\,\rho_{g}}{4\mathsf{c_{w}}\ell},\quad d_{g}=\frac{\mathsf{G}_{\mathrm{c}}\,\ell\,\rho_{g}}{4\mathsf{c_{w}}},(88)

withρg\rho_{g}the quadrature weights (cell areas) of AppendixA.1.
By construction‖𝖫𝖣‖2=∑g(cg​α​(xg)2+dg​‖∇α​(xg)‖2)=𝖦c4​𝖼𝗐​∫Ω(ζℓ​α2+ℓ​‖∇α‖2)​dA\|\mathsf{L}\mathsf{D}\|^{2}=\sum_{g}\big(c_{g}\,\alpha(x_{g})^{2}+d_{g}\,\|\nabla\alpha(x_{g})\|^{2}\big)=\frac{\mathsf{G}_{\mathrm{c}}}{4\mathsf{c_{w}}}\int_{\Omega}\big(\tfrac{\zeta}{\ell}\,\alpha^{2}+\ell\,\|\nabla\alpha\|^{2}\big)\,\mathrm{d}A,i.e.the quadratic part of the damage energy.
The load vector𝖻k=𝖦c​(1−ζ)4​𝖼𝗐​ℓ​∫Ωχk​dA−τc​∫Ω‖𝒑‖​χk​dA\mathsf{b}_{k}=\frac{\mathsf{G}_{\mathrm{c}}(1-\zeta)}{4\mathsf{c_{w}}\ell}\int_{\Omega}\chi_{k}\,\mathrm{d}A-\tau_{c}\int_{\Omega}\|\boldsymbol{p}\|\,\chi_{k}\,\mathrm{d}A(89)

collects the linear part of𝗐​(α)\mathsf{w}(\alpha)and the non-smooth coupling term𝗄​(α)​τc​‖𝒑‖\mathsf{k}(\alpha)\,\tau_{c}\|\boldsymbol{p}\|with𝗄′​(α)=−1\mathsf{k}^{\prime}(\alpha)=-1, respectively.
The program is solved with the conic interior-point optimizer of MOSEK[8], with maximal tolerances set to10−810^{-8}.

## References
- [1]R. Alessi, J.-J. Marigo, and S. Vidoli(2015)Gradient damage models coupled with plasticity: variational formulation and main properties.80(B),pp. 351–367.External Links:DocumentCited by:§1,Remark 1.
- [2]R. Alessi, F. Colasanto, and M. Focardi(2025)Phase-field modelling of cohesive fracture. Part II: reconstruction of the cohesive law.External Links:2507.12172,LinkCited by:§1.
- [3]R. Alessi, F. Colasanto, and M. Focardi(2025)Phase-field modelling of cohesive fracture. Part III: from mathematical results to engineering application.External Links:2507.22072,LinkCited by:§1.
- [4]R. Alessi, F. Colasanto, and M. Focardi(2026)Phase-field modeling of cohesive fracture. Part I:Γ\Gamma-convergence results.58(1),pp. 513–546.External Links:DocumentCited by:§1.
- [5]R. Alessi, J. Marigo, C. Maurini, and S. Vidoli(2018)Coupling damage and plasticity for a phase-field regularisation of brittle, cohesive and ductile fracture: One-dimensional examples.149,pp. 559–576.External Links:Document,ISSN 0020-7403Cited by:§1,Remark 1.
- [6]R. Alessi, J. Marigo, and S. Vidoli(2014-11-01)Gradient damage models coupled with plasticity and nucleation of cohesive cracks.214(2),pp. 575–615.External Links:Document,ISSN 1432-0673Cited by:§1,§6.2.2,Remark 1.
- [7]G. Anzellotti and M. Giaquinta(1980-03)Existence of the displacements field for an elasto-plastic body subject to hencky’s law and von mises yield condition.32(1-2),pp. 101–136.External Links:DocumentCited by:§1.
- [8]M. ApS(2024)The mosek fusion api for python.Vol.10.External Links:LinkCited by:§A.1,§A.1,§A.1,§A.2,§1,§5.2.
- [9]G. Bacquaert, J. Bleyer, and C. Maurini(2025-01)Regularization of softening plasticity with the cumulative plastic strain-rate gradient.194,pp. 105923.External Links:DocumentCited by:§1,§7.
- [10]I. A. Baratta, J. P. Dean, J. S. Dokken, M. Habera, J. S. Hale, C. N. Richardson, M. E. Rognes, M. W. Scroggs, N. Sime, and G. N. Wells(2023)DOLFINx: the next generation FEniCS problem solving environment.Note:preprintExternal Links:DocumentCited by:§5.2.
- [11]G. I. Barenblatt(1962-01-01)The Mathematical Theory of Equilibrium Cracks in Brittle Fracture.InAdvances in Applied Mechanics,H. L. Dryden, Th. von Kármán, G. Kuerti, F. H. van den Dungen, and L. Howarth (Eds.),Vol.7,pp. 55–129.External Links:DocumentCited by:§1,§1,§1,§6.3.1.
- [12]Z. P. Bažant and M. Jirásek(2002-11)Nonlocal integral formulations of plasticity and damage: survey of progress.128(11),pp. 1119–1149.External Links:DocumentCited by:§1,§7.
- [13]Z. P. Bažant and J. Planas(1998)Fracture and size effect in concrete and other quasibrittle materials.CRC Press.Note:The DOI 10.1201/9780203756799 registered for this title refers to the 2019 Routledge reissueExternal Links:ISBN 0-8493-8284-XCited by:§5.1.
- [14]B. A. Bilby, A. H. Cottrell, and K. H. Swinden(1963-03)The spread of plastic yield from a notch.272(1350),pp. 304–314.External Links:DocumentCited by:§1.
- [15]J. Bleyer(2020-09)Automating the formulation and resolution of convex variational problems: applications from image processing to computational mechanics.ACM Transactions on Mathematical Software46(3).External Links:Document,ISSN 0098-3500Cited by:§A.1,§1.
- [16]G. Bouchitté, A. Braides, and G. Buttazzo(1995)Relaxation results for some free discontinuity problems.458,pp. 1–18.External Links:DocumentCited by:§1.
- [17]B. Bourdin, G. A. Francfort, and J.-J. Marigo(2008)The variational approach to fracture.91(1-3),pp. 5–148.External Links:DocumentCited by:§1,§6.1.
- [18]B. Bourdin, G.A. Francfort, and J.-J. Marigo(2000)Numerical experiments in revisited brittle fracture.48(4),pp. 797–826.External Links:Document,ISSN 0022-5096Cited by:§1,§5.2,§7.
- [19]B. Bourdin, J. Marigo, C. Maurini, and C. Zolesi(2025)A variational approach to fracture incorporating any convex strength criterion.External Links:2506.22558,LinkCited by:§1,§1,§1,§1,§4,§6.1,§7,§7,Remark 1.
- [20]S. Brach, E. Tanné, B. Bourdin, and K. Bhattacharya(2019)Phase-field study of crack nucleation and propagation in elastic-perfectly plastic bodies.Computer Methods in Applied Mechanics and Engineering353,pp. 44–65.External Links:DocumentCited by:§6.2.2.
- [21]A. Carpinteri(1982)Notch sensitivity in fracture testing of aggregative materials.16(4),pp. 467–481.External Links:DocumentCited by:§5.1.
- [22]S. Conti, M. Focardi, and F. Iurlano(2016-08)Phase field approximation of cohesive fracture models.33(4),pp. 1033–1067.External Links:Document,ISSN 0294-1449, 1873-1430Cited by:§1.
- [23]S. Conti, M. Focardi, and F. Iurlano(2024-04)Phase-Field Approximation of a Vectorial, Geometrically Nonlinear Cohesive Fracture Energy.248(2),pp. 21.External Links:Document,ISSN 0003-9527, 1432-0673Cited by:§1.
- [24]P. Cornetti, N. Pugno, A. Carpinteri, and D. Taylor(2006-09-01)Finite fracture mechanics: A coupled stress and energy failure criterion.73(14),pp. 2021–2033.External Links:Document,ISSN 0013-7944Cited by:§6.3.1.
- [25]B. Dacorogna(1989)Direct methods in the calculus of variations.Applied Mathematical Sciences, Vol.78,Springer-Verlag,Berlin.External Links:ISBN 3-540-50491-5,MathReview (R. C. Varma)Cited by:§2.4.
- [26]G. Dal Maso, A. DeSimone, and M. G. Mora(2006)Quasistatic evolution problems for linearly elastic–perfectly plastic materials.Archive for Rational Mechanics and Analysis180(2),pp. 237–291.External Links:DocumentCited by:§1.
- [27]G. Dal Maso and L. Heltai(2021)A numerical study of the jerky crack growth in elastoplastic materials with localized plasticity.Journal of Convex Analysis28(2),pp. 535–548.Cited by:§6.2.2.
- [28]G. Dal Maso, G. Orlando, and R. Toader(2016-06)Fracture models for elasto-plastic materials as limits of gradient damage models coupled with plasticity: the antiplane case.55(3),pp. 45.External Links:Document,ISSN 0944-2669, 1432-0835Cited by:§1,§1.
- [29]G. Dal Maso and R. Toader(2020-08)On the jerky crack growth in elastoplastic materials.59(4),pp. 107.External Links:Document,ISSN 0944-2669, 1432-0835Cited by:§1,§6.2.2.
- [30]G. Dal Maso and R. Toader(2022-01)On the pure jump nature of crack growth for a class of pressure-sensitive elasto-plastic materials.214,pp. 112539.External Links:Document,ISSN 0362546XCited by:§1.
- [31]G. Del Piero and L. Truskinovsky(2009-05)Elastic bars with cohesive energy.21(2),pp. 141–171.External Links:DocumentCited by:§1.
- [32]G. Del Piero(1999)One-dimensional ductile-brittle transition, yielding, and structured deformations.InIUTAM Symposium on Variations of Domain and Free-Boundary Problems in Solid Mechanics,pp. 203–210.External Links:Document,ISBN 978-94-011-4738-5Cited by:§1.
- [33]D. S. Dugdale(1960-05-01)Yielding of steel sheets containing slits.8(2),pp. 100–104.External Links:Document,ISSN 0022-5096Cited by:§1,§1,§6.3.1.
- [34]G. Duvaut and J. Lions(1976)Inequalities in mechanics and physics.Grundlehren der mathematischen Wissenschaften,Springer.Note:Translated from the French by C. W. John; French originalLes inéquations en mécanique et en physique, Dunod, Paris, 1972External Links:DocumentCited by:§1.
- [35]Y. Feng and J. Li(2023-01)A unified regularized variational cohesive fracture theory with directional energy decomposition.182,pp. 103773.External Links:Document,ISSN 00207225Cited by:§1.
- [36]Y. Feng and J. Li(2026)Convergence of phase-field models with emergent discontinuities to CZMs in multidimensional space: a proof via cohesive laws and sharp-crack energy limits.215,pp. 106705.External Links:DocumentCited by:footnote 1.
- [37]S. Forest and E. Lorentz(2004)Localization phenomena and regularization methods.InLocal Approach to Fracture,J. Besson (Ed.),pp. 311–371.Note:Lecture notes of the MEALOR summer school, July 2004Cited by:§1,§7.
- [38]G. A. Francfort and J.-J. Marigo(1998)Revisiting brittle fracture as an energy minimization problem.46(8),pp. 1319–1342.External Links:DocumentCited by:§1.
- [39]C. Geuzaine and J. Remacle(2009)Gmsh: a 3-D finite element mesh generator with built-in pre- and post- processing facilities.International Journal for Numerical Methods in Engineering79(11),pp. 1309–1331.External Links:DocumentCited by:§6.1.
- [40]A. A. Griffith(1921-01-01)The phenomena of rupture and flow in solids.221(582-593),pp. 163–198.Note:The registered title is prefixed “VI.”, the article number within the volumeExternal Links:DocumentCited by:§3.2.
- [41]R. Hill(1950)The mathematical theory of plasticity.Clarendon Press.Note:Reissued 1998 in Oxford Classic Texts in the Physical Sciences; the DOI refers to that reissueExternal Links:Document,ISBN 978-0-19-850367-5Cited by:§1.
- [42]A. Hillerborg, M. Modéer, and P.-E. Petersson(1976-11)Analysis of crack formation and crack growth in concrete by means of fracture mechanics and finite elements.6(6),pp. 773–781.External Links:DocumentCited by:§1,§3.1.
- [43]M. Z. Hossain, C.-J. Hsueh, B. Bourdin, and K. Bhattacharya(2014)Effective toughness of heterogeneous media.Journal of the Mechanics and Physics of Solids71,pp. 15–32.External Links:DocumentCited by:§6.2.1.
- [44]J. A. H. Hult and F. A. McClintock(1956)Elastic–plastic stress and strain distribution around sharp notches under repeated shear.InProceedings of the 9th International Congress of Applied Mechanics,Vol.8,pp. 51–58.Cited by:§1,§1,§6.3.1,§6.3.1.
- [45]J. W. Hutchinson(1968-01)Singular behaviour at the end of a tensile crack in a hardening material.16(1),pp. 13–31.External Links:DocumentCited by:§1.
- [46]M. Jirásek and S. Rolshoven(2003-08)Comparison of integral-type nonlocal plasticity models for strain-softening materials.41(13-14),pp. 1553–1602.External Links:DocumentCited by:§1,§7.
- [47]P. A. Klein, J. W. Foulk, E. P. Chen, S. A. Wimmer, and H. J. Gao(2001)Physics-based modeling of brittle fracture: cohesive formulations and the application of meshfree methods.37(1-3),pp. 99–166.External Links:DocumentCited by:§1.
- [48]K. Krabbenhøft, A. V. Lyamin, and S. W. Sloan(2007-03)Formulation and solution of some plasticity problems as conic programs.44(5),pp. 1533–1549.External Links:DocumentCited by:§1.
- [49]A. Kumar, B. Bourdin, G. A. Francfort, and O. Lopez-Pamies(2020)Revisiting nucleation in the phase-field approach to brittle fracture.142,pp. 104027.External Links:DocumentCited by:§1.
- [50]J. B. Leblond, G. Perrin, and J. Devaux(1994-06)Bifurcation effects in ductile metals with nonlocal damage.61(2),pp. 236–242.External Links:DocumentCited by:§1,§7.
- [51]D. Leguillon(2002-01)Strength or toughness? A criterion for crack onset at a notch.21(1),pp. 61–72.External Links:Document,ISSN 0997-7538Cited by:§6.3.1.
- [52]A. A. León Baldelli and C. Maurini(2021-07-01)Numerical bifurcation and stability analysis of variational gradient-damage models for phase-field fracture.152,pp. 104424.External Links:Document,ISSN 0022-5096Cited by:§2.4.
- [53]M. S. Lobo, L. Vandenberghe, S. Boyd, and H. Lebret(1998-11)Applications of second-order cone programming.284(1-3),pp. 193–228.External Links:DocumentCited by:§A.1,§1.
- [54]E. Lorentz, J. Besson, and V. Cano(2008-04)Numerical simulation of ductile fracture with the Rousselier constitutive law.197(21-24),pp. 1965–1982.External Links:DocumentCited by:§1,§7.
- [55]E. Lorentz, S. Cuvilliez, and K. Kazymyrenko(2011)Convergence of a gradient damage model toward a cohesive zone model.339(1),pp. 20–26.External Links:Document,ISSN 1631-0721Cited by:§1.
- [56]E. Lorentz, S. Cuvilliez, and K. Kazymyrenko(2012-11)Modelling large crack propagation: from gradient damage to cohesive zone models.178(1-2),pp. 85–95.External Links:Document,ISSN 0376-9429, 1573-2673Cited by:§1.
- [57]E. Maggiorelli, M. Negri, F. Vicentini, and L. De Lorenzis(2025)Gamma convergence for a phase-field cohesive energy.External Links:2511.00016,LinkCited by:§1.
- [58]J.-J. Marigo, C. Maurini, and K. Pham(2016)An overview of the modelling of fracture by gradient damage models.Meccanica51(12),pp. 3107–3128.External Links:DocumentCited by:§3.2.
- [59]J.-J. Marigo and L. Truskinovsky(2004-05-01)Initiation and propagation of fracture in the models of Griffith and Barenblatt.16(4),pp. 391–409.External Links:Document,ISSN 1432-0959Cited by:§1.
- [60]J. Marigo(2023-11-01)Modelling of fracture by cohesive force models: A path to pursue.102,pp. 105088.External Links:Document,ISSN 0997-7538Cited by:§1,§1,§6.3.2,§7.
- [61]F. A. McClintock and G. R. Irwin(1965)Plasticity aspects of fracture mechanics.InFracture Toughness Testing and Its Applications,ASTM STP 381,pp. 84–113.External Links:Document,ISBN 978-0-8031-0105-0Cited by:§1.
- [62]A. Mielke and T. Roubíček(2015)Rate-independent systems: theory and application.Applied Mathematical Sciences, Vol.193,Springer,New York.External Links:Document,ISBN 978-1-4939-2705-0Cited by:§2.3.
- [63]M. G. Mora(2016)Relaxation of the hencky model in perfect plasticity.Journal de Mathématiques Pures et Appliquées106(4),pp. 725–743.External Links:Document,ISSN 0021-7824Cited by:§2.4.
- [64]H.-B. Mühlhaus and E.C. Aifantis(1991)A variational principle for gradient plasticity.28(7),pp. 845–857.External Links:DocumentCited by:§1,§7.
- [65]A. Needleman(1987-09)A continuum model for void nucleation by inclusion debonding.54(3),pp. 525–531.External Links:DocumentCited by:§1.
- [66]M. Ortiz and A. Pandolfi(1999)Finite-deformation irreversible cohesive elements for three-dimensional crack-propagation analysis.44(9),pp. 1267–1282.External Links:DocumentCited by:§1.
- [67]K. Pham, J.-J. Marigo, and C. Maurini(2011)The issues of the uniqueness and the stability of the homogeneous response in uniaxial tests with gradient damage models.59(6),pp. 1163–1190.External Links:Document,ISSN 0022-5096Cited by:§1,§2.4,§2.5,§3.2,§3.
- [68]K. Pham and J.-J. Marigo(2010)Approche variationnelle de l’endommagement : I. les concepts fondamentaux.C. R. Mécanique338(4),pp. 191–198.External Links:Document,ISSN 1631-0721Cited by:§1.
- [69]G. Pijaudier-Cabot and Z. P. Bažant(1987-10)Nonlocal damage theory.113(10),pp. 1512–1533.External Links:DocumentCited by:§1,§7.
- [70]W. Prager and P. G. Hodge(1951)Theory of perfectly plastic solids.John Wiley & Sons.Cited by:§1.
- [71]J. R. Rice and G. F. Rosengren(1968-01)Plane strain deformation near a crack tip in a power-law hardening material.16(1),pp. 1–12.External Links:DocumentCited by:§1.
- [72]J. R. Rice(1966)Contained plastic deformation near cracks and notches under longitudinal shear.2(2),pp. 426–447.External Links:DocumentCited by:§1,§1,§6.3.1,§6.3.1.
- [73]J. R. Rice(1967-06)Stresses due to a sharp notch in a work-hardening elastic–plastic material loaded by longitudinal shear.34(2),pp. 287–298.External Links:DocumentCited by:§6.3.1,§6.3.1.
- [74]J. J. Rimoli and J. J. Rojas(2015-05)Meshing strategies for the alleviation of mesh-induced effects in cohesive element models.193(1),pp. 29–42.External Links:Document,ISSN 0376-9429, 1573-2673Cited by:§1.
- [75]A. Rodella, J.-J. Marigo, C. Maurini, and S. Vidoli(2026)Sharp-interface cohesive fracture models with consistent bulk energies: Numerical investigations.211,pp. 106543.External Links:DocumentCited by:§1,§1,Figure 18,§6.2.2,§6.3.2,§6.3.2,§7.
- [76]J. Salençon(2013-05)Yield design.Wiley.External Links:Document,ISBN 978-1-84821-540-5Cited by:§1.
- [77]P. M. Suquet(1981)Sur les équations de la plasticité: existence et régularité des solutions.20,pp. 3–39.Cited by:§1.
- [78]E. Tanné, T. Li, B. Bourdin, J.-J. Marigo, and C. Maurini(2018)Crack nucleation in variational phase-field models of brittle fracture.110,pp. 80–99.External Links:DocumentCited by:§1,§6.3.1,§6.3.2,§6.3.2.
- [79]R. Temam and G. Strang(1980-03)Functions of bounded deformation.75(1),pp. 7–21.External Links:DocumentCited by:§1.
- [80]F. Vicentini, J. Heinzmann, P. Carrara, and L. De Lorenzis(2026)Variational phase-field modeling of cohesive fracture with flexibly tunable strength surface.207,pp. 106424.External Links:DocumentCited by:footnote 1.
- [81]C. Zolesi and C. Maurini(2024)Stability and crack nucleation in variational phase-field models of fracture: effects of length-scales and stress multi-axiality.192,pp. 105802.External Links:DocumentCited by:§6.1.

## 


- 


Major funding support from
