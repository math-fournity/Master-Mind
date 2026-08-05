# Variational Openness

**arXiv ID**: 2605.17032v1
**Authors**: Francisco Monroy
**Published**: 2026-05-16
**Categories**: physics.class-ph, math-ph
**HTML URL**: https://arxiv.org/html/2605.17032v1

## Abstract

Variational principles in mechanics, field theory and geometric analysis are usually formulated on closed admissible classes, where boundary variations are either fixed or independently cancelled through natural boundary conditions. Variational openness is formulated here as a conservative extension of this setting. Its central premise is that stationarity requires cancellation of the total first variation, not necessarily separate cancellation of bulk and boundary contributions. Separate Euler--Lagrange and boundary equations arise only when admissible variations are independently localizable. Two regimes are distinguished. In separable open systems, bulk and boundary variations remain independently testable, and stationarity yields the usual interior equation together with an open boundary balance. In regulated open systems, admissible variations form a graph subspace in which bulk and boundary displacements are linked by a compatibility operator. Stationarity then becomes a projected balance on the admissible exchange space, allowing nontrivial bulk--boundary action exchange before total cancellation occurs. At second order, the open action defines a closed quadratic form on the admissible graph space. For pressure-like boundary couplings, the open Hessian is obtained by subtracting from the stabilizing geometric form a boundary-pressure form pulled back through the compatibility operator. A Rayleigh--Ritz criterion then yields a critical threshold at which positivity and coercivity are lost. A minimal spherical example illustrates the corresponding regulated spectral shift. The framework contains fixed-boundary, natural-boundary and classical free-boundary problems as limiting cases, while extending stationarity to regulated bulk--boundary exchange classes.

## Full Text

Variational Openness

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
- License: CC BY 4.0arXiv:2605.17032v1 [physics.class-ph] 16 May 2026

[1]\fnmFrancisco\surMonroy

[1]\orgdivDepartamento de Química Física,\orgnameUniversidad Complutense de Madrid,\orgaddress\cityMadrid,\countrySpain

## Variational Opennessmonroy@ucm.es*

## Abstract

Variational principles in mechanics, field theory and geometric analysis are usually formulated on closed admissible classes, where boundary variations are either fixed or independently cancelled through natural boundary conditions. Variational openness is formulated here as a conservative extension of this setting. Its central premise is that stationarity requires cancellation of the total first variation, not necessarily separate cancellation of bulk and boundary contributions. Separate Euler–Lagrange and boundary equations arise only when admissible variations are independently localizable. Two regimes are distinguished. In separable open systems, bulk and boundary variations remain independently testable, and stationarity yields the usual interior equation together with an open boundary balance. In regulated open systems, admissible variations form a graph subspace in which bulk and boundary displacements are linked by a compatibility operator. Stationarity then becomes a projected balance on the admissible exchange space, allowing nontrivial bulk–boundary action exchange before total cancellation occurs. At second order, the open action defines a closed quadratic form on the admissible graph space. For pressure-like boundary couplings, the open Hessian is obtained by subtracting from the stabilizing geometric form a boundary-pressure form pulled back through the compatibility operator. A Rayleigh–Ritz criterion then yields a critical threshold at which positivity and coercivity are lost. A minimal spherical example illustrates the corresponding regulated spectral shift. The framework contains fixed-boundary, natural-boundary and classical free-boundary problems as limiting cases, while extending stationarity to regulated bulk–boundary exchange classes.

## keywords:calculus of variations, free boundary problems, variational principles, natural boundary conditions, Hamilton–Jacobi theory, quadratic forms, spectral instability, mathematical physics

## pacs:[

MSC Classification]49K20, 49Q10, 58E30, 35P15, 35J20, 35B35

## 1Introduction

Hamilton’s variational principle and its field-theoretic extensions provide a standard route from stationarity of an action to equations of motion[LandauLifshitz1976]. In the elementary mechanical formulation, one considers variations with fixed endpoints and requires the first variation of the action to vanish. More generally, after integration by parts, the first variation separates into an interior Euler–Lagrange term and a boundary variational flux[Gelfand1963,Elsgoltz1969,Giaquinta1996,Dacorogna2008]. Standard formulations suppress the boundary contribution either by fixing the trace of the admissible variations or by imposing a natural boundary condition. In this sense, the admissible variational class is closed at the boundary[Lanczos1970,Goldstein2002,Kibble2004,Arnold1989].

The separate cancellation of interior and boundary terms is not, however, a primitive variational principle. It follows from a structural assumption on the admissible variations: the possibility of localizing bulk and boundary variations independently. Once this independence is available, the fundamental lemma of the calculus of variations separates the total first variation into an interior equation and a boundary equation. Without independent localization of admissible variations, this separation is no longer enforced by the variational principle itself.

Free-endpoint and transversality problems already show that boundary data may enter nontrivially into stationarity[Gelfand1963]. Geometric and free-boundary variational problems further demonstrate that admissible boundary deformations can participate directly in variational balance laws[Courant1953,Giaquinta1996]. The present work isolates the underlying structural principle. We ask what follows if the boundary sector is retained as an active variational component rather than eliminated by admissibility constraints.

We call this structurevariational openness. The term refers exclusively to the admissible variational class and does not imply stochastic forcing, dissipation or microscopic environmental coupling. An open variational problem is one for which stationarity is imposed on the total first variation,δ​Sbulk+δ​S∂=0,\delta S_{\mathrm{bulk}}+\delta S_{\partial}=0,(1)

with nontrivial admissible boundary variations.

Two regimes must then be distinguished. In aseparable open system, bulk and boundary variations remain independently testable. The open principle therefore yields a bulk Euler–Lagrange equation together with a generalized natural boundary condition. In aregulated open system, admissible variations form a proper graph subspace in which bulk and boundary displacements are linked by a compatibility operator. Stationarity is then a projected balance on the admissible graph space rather than a separate annihilation of bulk and boundary first variations. In this regime, nonzero bulk and boundary contributions may cancel only after restriction to the admissible exchange class.

The first objective of the paper is to formulate this regulated variational structure precisely. The second is to determine its second-variation and spectral consequences. Around a stationary configuration, the open action defines a quadratic form on the admissible graph space. For pressure-like boundary couplings, the corresponding open Hessian takes the form𝒬Π​[u]=𝒬G​[u]−Π​𝒬P∂​[𝒞​u].\mathcal{Q}_{\Pi}[u]=\mathcal{Q}_{G}[u]-\Pi\mathcal{Q}_{P}^{\partial}[\mathcal{C}u].(2)

The relevant stability directions are therefore not arbitrary bulk and boundary perturbations, but compatible exchange modes selected by the admissibility operator.

The main result is a Rayleigh–Ritz criterion for loss of positivity of the open Hessian. Under standard assumptions on the associated quadratic forms, there exists a critical thresholdΠc=infu≠0𝒬G​[u]𝒬P∂​[𝒞​u],\Pi_{c}=\inf_{u\neq 0}\frac{\mathcal{Q}_{G}[u]}{\mathcal{Q}_{P}^{\partial}[\mathcal{C}u]},(3)

defined on the pressure-active admissible subspace. ForΠ<Πc\Pi<\Pi_{c}, the open Hessian remains positive on the admissible graph space; forΠ>Πc\Pi>\Pi_{c}, it develops a negative direction, and, under compactness assumptions, a negative eigenvalue.

The paper is organized as follows. Section2defines closed, separable open and regulated open variational systems. Section3formulates projected stationarity and variational action exchange. The term “exchange” refers only to cancellation structure on the admissible graph space. Section4derives the corresponding Euler–Lagrange balance laws. Section5records the Hamilton–Jacobi representation. Section6gives the geometric boundary formulation. Section7introduces the open Hessian as a closed quadratic form on the admissible graph space. Section8proves the Rayleigh–Ritz instability criterion. Section9gives a minimal regulated spherical example. Section10discusses the relation with classical variational theory and free-boundary problems.

## 2Closed, separable open and regulated open variational systems

Letℳ\mathcal{M}be a smooth compact orienteddd-dimensional manifold with smooth boundary∂ℳ\partial\mathcal{M}. LetE→ℳE\to\mathcal{M}be a smooth vector bundle and letϕ\phibe a section ofEE. For definiteness, we consider first-order Lagrangians,Sbulk​[ϕ]=∫ℳL​(j1​ϕ)​dV,S_{\mathrm{bulk}}[\phi]=\int_{\mathcal{M}}L(j^{1}\phi)\,\mathrm{d}V,(4)

wherej1​ϕj^{1}\phiis the first jet ofϕ\phi.

Letγ​ϕ\gamma\phidenote the trace ofϕ\phion∂ℳ\partial\mathcal{M}. In the Sobolev setting,γ:H1​(ℳ;E)⟶H1/2​(∂ℳ;E|∂ℳ),\gamma:H^{1}(\mathcal{M};E)\longrightarrow H^{1/2}(\partial\mathcal{M};E|_{\partial\mathcal{M}}),(5)

and we writeφ:=γ​ϕ\varphi:=\gamma\phi(6)

for the induced boundary field.

A closed variational problem restricts admissible variations byγ​v=0,\gamma v=0,(7)

or, for free boundary values, requires the boundary variational flux to vanish through a natural boundary condition. In both cases, the boundary does not define an independent exchange channel for stationarity.

To unfold the bulk–boundary structure, let𝒱bulk⊂H1​(ℳ;E),𝒱∂⊂H1/2​(∂ℳ;E|∂ℳ)\mathscr{V}_{\mathrm{bulk}}\subset H^{1}(\mathcal{M};E),\qquad\mathscr{V}_{\partial}\subset H^{1/2}(\partial\mathcal{M};E|_{\partial\mathcal{M}})(8)

be the bulk and boundary test spaces, and define𝒱prod:=𝒱bulk⊕𝒱∂.\mathscr{V}_{\mathrm{prod}}:=\mathscr{V}_{\mathrm{bulk}}\oplus\mathscr{V}_{\partial}.(9)

Elements of𝒱prod\mathscr{V}_{\mathrm{prod}}are denoted(v,w)(v,w), wherevvis a bulk variation andwwis a boundary variation. This product representation is an unfolded form of the variational derivative; admissibility is imposed by selecting either independent tests or a constrained graph.

## Definition 1(Separable open variational system).

A separable open variational system has actionS​[ϕ]=Sbulk​[ϕ]+S∂​[φ],φ=γ​ϕ,S[\phi]=S_{\mathrm{bulk}}[\phi]+S_{\partial}[\varphi],\qquad\varphi=\gamma\phi,(10)

withS∂​[φ]=∫∂ℳℬ​(j∂1​φ,h)​dAh.S_{\partial}[\varphi]=\int_{\partial\mathcal{M}}\mathcal{B}(j^{1}_{\partial}\varphi,h)\,\mathrm{d}A_{h}.(11)

Stationarity is imposed for admissible variations whose bulk and boundary components are independently testable. No fixed-trace condition is imposed a priori.

## Definition 2(Regulated open variational system).

A regulated open variational system is an open variational problem in which admissible bulk and boundary variations are linked by a bounded linear compatibility operator𝒞:𝒱bulk⟶𝒱∂.\mathcal{C}:\mathscr{V}_{\mathrm{bulk}}\longrightarrow\mathscr{V}_{\partial}.(12)

The admissible variation space is the graph𝒱op:=Graph⁡(𝒞)={(v,𝒞​v):v∈𝒱bulk}⊂𝒱prod.\mathscr{V}_{\mathrm{op}}:=\operatorname{Graph}(\mathcal{C})=\{(v,\mathcal{C}v):v\in\mathscr{V}_{\mathrm{bulk}}\}\subset\mathscr{V}_{\mathrm{prod}}.(13)

It is equipped with the graph norm‖(v,𝒞​v)‖𝒱op2=‖v‖𝒱bulk2+‖𝒞​v‖𝒱∂2.\|(v,\mathcal{C}v)\|_{\mathscr{V}_{\mathrm{op}}}^{2}=\|v\|_{\mathscr{V}_{\mathrm{bulk}}}^{2}+\|\mathcal{C}v\|_{\mathscr{V}_{\partial}}^{2}.(14)

Stationarity is imposed only after restriction to this graph:δ​Sbulk​[ϕ]​(v)+δ​S∂​[φ]​(𝒞​v)=0,φ=γ​ϕ,∀(v,𝒞​v)∈𝒱op.\delta S_{\mathrm{bulk}}[\phi](v)+\delta S_{\partial}[\varphi](\mathcal{C}v)=0,\qquad\varphi=\gamma\phi,\quad\forall(v,\mathcal{C}v)\in\mathscr{V}_{\mathrm{op}}.(15)

The boundedness of𝒞\mathcal{C}makes𝒱op\mathscr{V}_{\mathrm{op}}a closed admissible subspace of𝒱prod\mathscr{V}_{\mathrm{prod}}in the standard graph-norm sense[Conway1990,Brezis2011]. This is the regulation condition: the boundary sector cannot cancel arbitrary bulk variations, but only those transmitted through the specified compatibility channel.

Closed, separable and regulated problems correspond to different admissible classes. If𝒞=0\mathcal{C}=0, the unfolded boundary component is suppressed; the usual fixed-boundary problem is recovered when𝒱bulk\mathscr{V}_{\mathrm{bulk}}is additionally chosen with fixed trace,γ​v=0\gamma v=0. If boundary trace directions are independently testable, one obtains the separable natural-boundary case. If𝒞\mathcal{C}defines a nontrivial graph, stationarity is a projected condition onGraph⁡(𝒞)\operatorname{Graph}(\mathcal{C}), not separate annihilation on𝒱bulk\mathscr{V}_{\mathrm{bulk}}and𝒱∂\mathscr{V}_{\partial}.

## 3Action exchange and projected stationarity

The unfolded first variation is a functional on𝒱prod=𝒱bulk⊕𝒱∂\mathscr{V}_{\mathrm{prod}}=\mathscr{V}_{\mathrm{bulk}}\oplus\mathscr{V}_{\partial}. For(v,w)∈𝒱prod(v,w)\in\mathscr{V}_{\mathrm{prod}}, writeδ​S​[ϕ]​(v,w)=𝒥bulk​[ϕ]​(v)+𝒥∂​[ϕ]​(w),\delta S[\phi](v,w)=\mathcal{J}_{\mathrm{bulk}}[\phi](v)+\mathcal{J}_{\partial}[\phi](w),(16)

with𝒥bulk​[ϕ]​(v):=∫ℳ⟨EL​(ϕ),v⟩​dV,\mathcal{J}_{\mathrm{bulk}}[\phi](v):=\int_{\mathcal{M}}\left\langle E_{L}(\phi),v\right\rangle\,\mathrm{d}V,(17)

and𝒥∂​[ϕ]​(w):=∫∂ℳ⟨ΠL​(ϕ)+E∂ℬ​(γ​ϕ),w⟩​dAh,\mathcal{J}_{\partial}[\phi](w):=\int_{\partial\mathcal{M}}\left\langle\Pi_{L}(\phi)+E_{\partial\mathcal{B}}(\gamma\phi),w\right\rangle\,\mathrm{d}A_{h},(18)

up to corner terms. In a regulated open system the admissible pairs are restricted to(v,w)=(v,𝒞​v).(v,w)=(v,\mathcal{C}v).

Thus the first variation pulled back to the graph is𝔉ϕ​(v):=δ​S​[ϕ]​(v,𝒞​v)=𝒥bulk​[ϕ]​(v)+𝒥∂​[ϕ]​(𝒞​v).\mathfrak{F}_{\phi}(v):=\delta S[\phi](v,\mathcal{C}v)=\mathcal{J}_{\mathrm{bulk}}[\phi](v)+\mathcal{J}_{\partial}[\phi](\mathcal{C}v).(19)

Regulated stationarity is𝔉ϕ=0in​𝒱bulk′.\mathfrak{F}_{\phi}=0\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime}.(20)

Since𝒞:𝒱bulk→𝒱∂\mathcal{C}:\mathscr{V}_{\mathrm{bulk}}\to\mathscr{V}_{\partial}is bounded, its adjoint𝒞∗:𝒱∂′⟶𝒱bulk′\mathcal{C}^{*}:\mathscr{V}_{\partial}^{\prime}\longrightarrow\mathscr{V}_{\mathrm{bulk}}^{\prime}(21)

is well defined. LetB∂​(ϕ):=ΠL​(ϕ)+E∂ℬ​(γ​ϕ)∈𝒱∂′B_{\partial}(\phi):=\Pi_{L}(\phi)+E_{\partial\mathcal{B}}(\gamma\phi)\in\mathscr{V}_{\partial}^{\prime}(22)

be the total boundary variational flux. Then𝒥∂​[ϕ]​(𝒞​v)=⟨B∂​(ϕ),𝒞​v⟩∂=⟨𝒞∗​B∂​(ϕ),v⟩bulk.\mathcal{J}_{\partial}[\phi](\mathcal{C}v)=\left\langle B_{\partial}(\phi),\mathcal{C}v\right\rangle_{\partial}=\left\langle\mathcal{C}^{*}B_{\partial}(\phi),v\right\rangle_{\mathrm{bulk}}.(23)

Therefore regulated stationarity is equivalentlyEL​(ϕ)+𝒞∗​[ΠL​(ϕ)+E∂ℬ​(γ​ϕ)]=0in​𝒱bulk′.E_{L}(\phi)+\mathcal{C}^{*}\left[\Pi_{L}(\phi)+E_{\partial\mathcal{B}}(\gamma\phi)\right]=0\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime}.(24)

This is the projected Euler–Lagrange balance. The boundary flux contributes only after pullback by the admissibility operator.

## Lemma 1(Failure of separate cancellation).

Let𝒱op=Graph⁡(𝒞)⊂𝒱bulk⊕𝒱∂\mathscr{V}_{\mathrm{op}}=\operatorname{Graph}(\mathcal{C})\subset\mathscr{V}_{\mathrm{bulk}}\oplus\mathscr{V}_{\partial}

be a proper graph subspace. If𝒱op\mathscr{V}_{\mathrm{op}}does not contain arbitrary independent directions(v,0)(v,0)and(0,w)(0,w), then𝒥bulk​(v)+𝒥∂​(𝒞​v)=0∀v∈𝒱bulk\mathcal{J}_{\mathrm{bulk}}(v)+\mathcal{J}_{\partial}(\mathcal{C}v)=0\quad\forall v\in\mathscr{V}_{\mathrm{bulk}}(25)

does not imply, in general,𝒥bulk=0,𝒥∂=0\mathcal{J}_{\mathrm{bulk}}=0,\qquad\mathcal{J}_{\partial}=0(26)

on𝒱bulk\mathscr{V}_{\mathrm{bulk}}and𝒱∂\mathscr{V}_{\partial}, respectively.

## Proof.

Equation (25) states that the product functional(v,w)↦𝒥bulk​(v)+𝒥∂​(w)(v,w)\mapsto\mathcal{J}_{\mathrm{bulk}}(v)+\mathcal{J}_{\partial}(w)

vanishes only after restriction tow=𝒞​vw=\mathcal{C}v. Since(v,0)(v,0)and(0,w)(0,w)are not arbitrary admissible tests on the graph, the two components cannot be separated by the fundamental lemma. Equivalently, a nonzero pair satisfying𝒥bulk=−𝒞∗​𝒥∂in​𝒱bulk′\mathcal{J}_{\mathrm{bulk}}=-\mathcal{C}^{*}\mathcal{J}_{\partial}\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime}

has zero total variation onGraph⁡(𝒞)\operatorname{Graph}(\mathcal{C})without requiring either component to vanish on the unconstrained product space.
∎

## Corollary 2(Nontrivial exchange).

IfB∂≠0B_{\partial}\neq 0andEL=−𝒞∗​B∂in​𝒱bulk′,E_{L}=-\mathcal{C}^{*}B_{\partial}\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime},(27)

then the total first variation vanishes onGraph⁡(𝒞)\operatorname{Graph}(\mathcal{C}), although the bulk and boundary variational contributions need not vanish separately.

## Definition 3(Variational action exchange).

A stationary regulated open configuration exhibits variational action exchange if, for some admissible graph variation(v,𝒞​v)(v,\mathcal{C}v),𝒥bulk​[ϕ]​(v)≠0,𝒥∂​[ϕ]​(𝒞​v)≠0,𝒥bulk​[ϕ]​(v)=−𝒥∂​[ϕ]​(𝒞​v).\mathcal{J}_{\mathrm{bulk}}[\phi](v)\neq 0,\qquad\mathcal{J}_{\partial}[\phi](\mathcal{C}v)\neq 0,\qquad\mathcal{J}_{\mathrm{bulk}}[\phi](v)=-\mathcal{J}_{\partial}[\phi](\mathcal{C}v).(28)

Thus regulated action exchange is the restricted stationarity condition(Sbulk+S∂)′|Graph⁡(𝒞)=0,(S_{\mathrm{bulk}}+S_{\partial})^{\prime}|_{\operatorname{Graph}(\mathcal{C})}=0,(29)

rather than separate stationarity of the two terms.

## 4Open Euler–Lagrange balance

We now record the Euler–Lagrange consequences of separable and regulated admissibility. The bulk first variation has the standard decompositionδ​Sbulk​[ϕ]​(v)=∫ℳ⟨EL​(ϕ),v⟩​dV+∫∂ℳ⟨ΠL​(ϕ),γ​v⟩​dAh,\delta S_{\mathrm{bulk}}[\phi](v)=\int_{\mathcal{M}}\left\langle E_{L}(\phi),v\right\rangle\,\mathrm{d}V+\int_{\partial\mathcal{M}}\left\langle\Pi_{L}(\phi),\gamma v\right\rangle\,\mathrm{d}A_{h},(30)

whereEL​(ϕ)E_{L}(\phi)is the Euler–Lagrange expression andΠL​(ϕ)\Pi_{L}(\phi)is the boundary variational flux. The boundary action satisfiesδ​S∂​[φ]​(w)=∫∂ℳ⟨E∂ℬ​(φ),w⟩​dAh+∫∂(∂ℳ)Θ∂ℬ​(φ,w),\delta S_{\partial}[\varphi](w)=\int_{\partial\mathcal{M}}\left\langle E_{\partial\mathcal{B}}(\varphi),w\right\rangle\,\mathrm{d}A_{h}+\int_{\partial(\partial\mathcal{M})}\Theta_{\partial\mathcal{B}}(\varphi,w),(31)

withw∈𝒱∂w\in\mathscr{V}_{\partial}. We assume that the corner term either vanishes or is cancelled by admissibility conditions or by an additional corner functional.

For a general unfolded pair(v,w)∈𝒱bulk⊕𝒱∂(v,w)\in\mathscr{V}_{\mathrm{bulk}}\oplus\mathscr{V}_{\partial},δ​S​[ϕ]​(v,w)=∫ℳ⟨EL​(ϕ),v⟩​dV+∫∂ℳ⟨ΠL​(ϕ)+E∂ℬ​(γ​ϕ),w⟩​dAh.\delta S[\phi](v,w)=\int_{\mathcal{M}}\left\langle E_{L}(\phi),v\right\rangle\,\mathrm{d}V+\int_{\partial\mathcal{M}}\left\langle\Pi_{L}(\phi)+E_{\partial\mathcal{B}}(\gamma\phi),w\right\rangle\,\mathrm{d}A_{h}.(32)

The equations obtained from (32) depend on the admissible test class.

## Theorem 3(Separable open Euler–Lagrange equations).

Letϕ\phibe a stationary point of the separable open action (10). If bulk and boundary variations are independently localizable, thenEL​(ϕ)\displaystyle E_{L}(\phi)=0\displaystyle=0in​ℳ,\displaystyle\text{in }\mathcal{M},(33)ΠL​(ϕ)+E∂ℬ​(γ​ϕ)\displaystyle\Pi_{L}(\phi)+E_{\partial\mathcal{B}}(\gamma\phi)=0\displaystyle=0on​∂ℳ.\displaystyle\text{on }\partial\mathcal{M}.(34)

Conversely, if (33)–(34) hold and the corner contribution in (31) vanishes, thenδ​S​[ϕ]​(v,w)=0\delta S[\phi](v,w)=0for all separable admissible variations.

## Proof.

Independent tests of the form(v,0)(v,0), withvvcompactly supported inℳ\mathcal{M}, give (33). Independent boundary tests(0,w)(0,w)give (34). The converse follows by substitution in (32).
∎

## Theorem 4(Regulated open Euler–Lagrange balance).

Letϕ\phibe stationary on the regulated graph𝒱op=Graph⁡(𝒞).\mathscr{V}_{\mathrm{op}}=\operatorname{Graph}(\mathcal{C}).

Then∫ℳ⟨EL​(ϕ),v⟩​dV+∫∂ℳ⟨ΠL​(ϕ)+E∂ℬ​(γ​ϕ),𝒞​v⟩​dAh=0∀v∈𝒱bulk.\int_{\mathcal{M}}\left\langle E_{L}(\phi),v\right\rangle\,\mathrm{d}V+\int_{\partial\mathcal{M}}\left\langle\Pi_{L}(\phi)+E_{\partial\mathcal{B}}(\gamma\phi),\mathcal{C}v\right\rangle\,\mathrm{d}A_{h}=0\quad\forall v\in\mathscr{V}_{\mathrm{bulk}}.(35)

Equivalently,EL​(ϕ)+𝒞∗​[ΠL​(ϕ)+E∂ℬ​(γ​ϕ)]=0in​𝒱bulk′.E_{L}(\phi)+\mathcal{C}^{*}\left[\Pi_{L}(\phi)+E_{\partial\mathcal{B}}(\gamma\phi)\right]=0\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime}.(36)

## Proof.

On the graph,w=𝒞​vw=\mathcal{C}v. Substitution into (32) gives (35). Since𝒞\mathcal{C}is bounded,𝒞∗:𝒱∂′→𝒱bulk′\mathcal{C}^{*}:\mathscr{V}_{\partial}^{\prime}\to\mathscr{V}_{\mathrm{bulk}}^{\prime}is well defined, and the boundary term is the dual pairing of𝒞∗​[ΠL+E∂ℬ]\mathcal{C}^{*}[\Pi_{L}+E_{\partial\mathcal{B}}]withvv. This gives (36).
∎

## Corollary 5(Exchange form).

In a regulated open system,EL​(ϕ)=−𝒞∗​[ΠL​(ϕ)+E∂ℬ​(γ​ϕ)]in​𝒱bulk′.E_{L}(\phi)=-\mathcal{C}^{*}\left[\Pi_{L}(\phi)+E_{\partial\mathcal{B}}(\gamma\phi)\right]\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime}.(37)

Thus the Euler–Lagrange residual is not required to vanish separately; it is balanced by the boundary variational flux pulled back through the admissibility operator.

## Remark 1(Limits).

If𝒞=0\mathcal{C}=0, the fixed-boundary problem is recovered. If boundary directions are independently testable, the regulated balance separates into (33)–(34). For a nontrivial graph, stationarity remains the projected exchange condition (37).

## 5Open Hamilton–Jacobi representation

The open variational principle also admits a Hamilton–Jacobi representation. No additional dynamical assumption is introduced; this section rewrites the first-variation balance of Section4at the level of Hamilton’s principal function.

Consider the finite-dimensional actionS​[q]=∫t0t1L​(q,q˙,t)​dt+B​(q​(t1),t1),S[q]=\int_{t_{0}}^{t_{1}}L(q,\dot{q},t)\,\mathrm{d}t+B(q(t_{1}),t_{1}),(38)

with fixed initial endpoint. Let𝒮​(q,t)\mathcal{S}(q,t)be Hamilton’s principal function. In the interior it satisfies∂t𝒮​(q,t)+H​(q,∇q𝒮,t)=0.\partial_{t}\mathcal{S}(q,t)+H(q,\nabla_{q}\mathcal{S},t)=0.(39)

For freely testable terminal variations, the natural endpoint condition isDq​𝒮​(q,t1)+Dq​B​(q,t1)=0.D_{q}\mathcal{S}(q,t_{1})+D_{q}B(q,t_{1})=0.(40)

This is the Hamilton–Jacobi counterpart of the separable boundary condition
(34).

For a regulated endpoint class, terminal variations are restricted byδ​q​(t1)=𝒞​v.\delta q(t_{1})=\mathcal{C}v.(41)

The endpoint stationarity condition is⟨Dq​𝒮+Dq​B,𝒞​v⟩=0for all admissible​v,\left\langle D_{q}\mathcal{S}+D_{q}B,\mathcal{C}v\right\rangle=0\quad\text{for all admissible }v,(42)

or, equivalently,𝒞∗​(Dq​𝒮+Dq​B)=0on the admissible endpoint space.\mathcal{C}^{*}\left(D_{q}\mathcal{S}+D_{q}B\right)=0\quad\text{on the admissible endpoint space}.(43)

Thus the regulated Hamilton–Jacobi condition is the pullback analogue of
(36).

In field form, let𝒮​[Σ,φ]\mathcal{S}[\Sigma,\varphi]be the on-shell action evaluated on a boundary hypersurfaceΣ\Sigmawith boundary fieldφ=γ​ϕ\varphi=\gamma\phi. Its first variation with respect to the boundary datum is denotedDφ​𝒮​[Σ,φ]∈𝒱∂′.D_{\varphi}\mathcal{S}[\Sigma,\varphi]\in\mathscr{V}_{\partial}^{\prime}.

The separable open Hamilton–Jacobi boundary condition isDφ​𝒮​[Σ,φ]+Dφ​S∂​[φ]=0in​𝒱∂′.D_{\varphi}\mathcal{S}[\Sigma,\varphi]+D_{\varphi}S_{\partial}[\varphi]=0\quad\text{in }\mathscr{V}_{\partial}^{\prime}.(44)

For a regulated admissible graphw=𝒞​vw=\mathcal{C}v, this becomes⟨Dφ​𝒮​[Σ,φ]+Dφ​S∂​[φ],𝒞​v⟩=0∀v∈𝒱bulk,\left\langle D_{\varphi}\mathcal{S}[\Sigma,\varphi]+D_{\varphi}S_{\partial}[\varphi],\mathcal{C}v\right\rangle=0\quad\forall v\in\mathscr{V}_{\mathrm{bulk}},(45)

or𝒞∗​(Dφ​𝒮​[Σ,φ]+Dφ​S∂​[φ])=0in​𝒱bulk′.\mathcal{C}^{*}\left(D_{\varphi}\mathcal{S}[\Sigma,\varphi]+D_{\varphi}S_{\partial}[\varphi]\right)=0\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime}.(46)

Equation (46) is the Hamilton–Jacobi form of regulated action exchange.

## 6Open variation of the boundary geometry

For geometric variational problems, openness may also act through the induced boundary metricha​bh_{ab}. The boundary part of the first variation containsδ​S=⋯+12​∫∂ℳ|h|​𝒯a​b​δ​ha​b​dd−1​x,\delta S=\cdots+\frac{1}{2}\int_{\partial\mathcal{M}}\sqrt{|h|}\,\mathcal{T}^{ab}\delta h_{ab}\,\mathrm{d}^{d-1}x,(47)

where𝒯a​b:=2|h|​δ​Sδ​ha​b\mathcal{T}^{ab}:=\frac{2}{\sqrt{|h|}}\frac{\delta S}{\delta h_{ab}}(48)

is the boundary variational stress. IfS=SG+S∂S=S_{G}+S_{\partial}, then𝒯a​b=𝒯Ga​b+𝒯∂a​b.\mathcal{T}^{ab}=\mathcal{T}_{G}^{ab}+\mathcal{T}_{\partial}^{ab}.(49)

## Proposition 6(Projected geometric boundary balance).

If boundary metric variations are independently testable, stationarity gives the pointwise balance𝒯Ga​b+𝒯∂a​b=0on​∂ℳ.\mathcal{T}_{G}^{ab}+\mathcal{T}_{\partial}^{ab}=0\quad\text{on }\partial\mathcal{M}.(50)

If, instead, admissible boundary metric variations are induced by bulk variations through a bounded operator𝒞h:𝒱bulk→𝒮∂,δ​ha​b=(𝒞h​v)a​b,\mathcal{C}_{h}:\mathscr{V}_{\mathrm{bulk}}\to\mathscr{S}_{\partial},\qquad\delta h_{ab}=(\mathcal{C}_{h}v)_{ab},(51)

then stationarity is the projected balance𝒥bulkgeom​[v]+12​∫∂ℳ|h|​(𝒯Ga​b+𝒯∂a​b)​(𝒞h​v)a​b​dd−1​x=0∀v∈𝒱bulk.\mathcal{J}_{\mathrm{bulk}}^{\mathrm{geom}}[v]+\frac{1}{2}\int_{\partial\mathcal{M}}\sqrt{|h|}\left(\mathcal{T}_{G}^{ab}+\mathcal{T}_{\partial}^{ab}\right)(\mathcal{C}_{h}v)_{ab}\,\mathrm{d}^{d-1}x=0\quad\forall v\in\mathscr{V}_{\mathrm{bulk}}.(52)

Equivalently,𝒥bulkgeom+12​𝒞h∗​[|h|​(𝒯G+𝒯∂)]=0in​𝒱bulk′.\mathcal{J}_{\mathrm{bulk}}^{\mathrm{geom}}+\frac{1}{2}\mathcal{C}_{h}^{*}\left[\sqrt{|h|}\left(\mathcal{T}_{G}+\mathcal{T}_{\partial}\right)\right]=0\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime}.(53)

## Proof.

The separable case follows by testing (47) with arbitraryδ​ha​b\delta h_{ab}. In the regulated case, substituteδ​ha​b=(𝒞h​v)a​b\delta h_{ab}=(\mathcal{C}_{h}v)_{ab}. Boundedness of𝒞h\mathcal{C}_{h}gives the adjoint map𝒞h∗:𝒮∂′→𝒱bulk′\mathcal{C}_{h}^{*}:\mathscr{S}_{\partial}^{\prime}\to\mathscr{V}_{\mathrm{bulk}}^{\prime}, yielding (53).
∎

Thus boundary geometry obeys the same structure as the field variation: pointwise balance is recovered only when boundary metric variations are independently testable; otherwise the stress balance is pulled back to the admissible bulk deformation space.

## 7The open Hessian as a quadratic form

Letϕ0\phi_{0}be a stationary configuration of the open action, and let𝒱op=Graph⁡(𝒞)\mathscr{V}_{\mathrm{op}}=\operatorname{Graph}(\mathcal{C})

be the regulated admissible variation space, after imposing the bulk–boundary compatibility relation and quotienting null directions. We regard𝒱op\mathscr{V}_{\mathrm{op}}as a Hilbert graph space, with the functional-analytic structure inherited from𝒱bulk⊕𝒱∂\mathscr{V}_{\mathrm{bulk}}\oplus\mathscr{V}_{\partial}[Conway1990,Brezis2011]. The second variation restricted to this graph definesδ2​S​[ϕ0]​((u,𝒞​u),(u,𝒞​u))=12​𝒬op​[u],(u,𝒞​u)∈𝒱op.\delta^{2}S[\phi_{0}]\bigl((u,\mathcal{C}u),(u,\mathcal{C}u)\bigr)=\frac{1}{2}\mathcal{Q}_{\mathrm{op}}[u],\qquad(u,\mathcal{C}u)\in\mathscr{V}_{\mathrm{op}}.(54)

Thus𝒬op\mathcal{Q}_{\mathrm{op}}is the pullback of the full Hessian to the admissible exchange space.

In general,𝒬op​[u]=𝒬bulk​[u]+𝒬∂​[𝒞​u]+2​𝒬mix​[u,𝒞​u],\mathcal{Q}_{\mathrm{op}}[u]=\mathcal{Q}_{\mathrm{bulk}}[u]+\mathcal{Q}_{\partial}[\mathcal{C}u]+2\mathcal{Q}_{\mathrm{mix}}[u,\mathcal{C}u],(55)

where𝒬mix\mathcal{Q}_{\mathrm{mix}}collects mixed second-variation terms. For an additively split action with fixed compatibility operator, this reduces to𝒬op​[u]=𝒬bulk​[u]+𝒬∂​[𝒞​u].\mathcal{Q}_{\mathrm{op}}[u]=\mathcal{Q}_{\mathrm{bulk}}[u]+\mathcal{Q}_{\partial}[\mathcal{C}u].(56)

The pressure-like case considered below has the form𝒬Π​[u]=𝒬G​[u]−Π​𝒬P∂​[𝒞​u],\mathcal{Q}_{\Pi}[u]=\mathcal{Q}_{G}[u]-\Pi\mathcal{Q}_{P}^{\partial}[\mathcal{C}u],(57)

where𝒬G\mathcal{Q}_{G}is the stabilizing bulk or geometric form and𝒬P∂\mathcal{Q}_{P}^{\partial}is a non-negative boundary-pressure form. For compactness we write𝒬P​[u]:=𝒬P∂​[𝒞​u],𝒬Π​[u]=𝒬G​[u]−Π​𝒬P​[u],\mathcal{Q}_{P}[u]:=\mathcal{Q}_{P}^{\partial}[\mathcal{C}u],\qquad\mathcal{Q}_{\Pi}[u]=\mathcal{Q}_{G}[u]-\Pi\mathcal{Q}_{P}[u],(58)

always understood on𝒱op\mathscr{V}_{\mathrm{op}}.

## Assumption 1(Quadratic-form setting).

The following hypotheses are assumed in Sections7–8.
- 1.

𝒱op\mathscr{V}_{\mathrm{op}}is a dense subspace of a Hilbert spaceℋ\mathscr{H}, or a closed admissible graph subspace after quotienting null modes.
- 2.

𝒬G:𝒱op→ℝ\mathcal{Q}_{G}:\mathscr{V}_{\mathrm{op}}\to\mathbb{R}is symmetric, closed and bounded from below.
- 3.

𝒬G\mathcal{Q}_{G}is coercive on𝒱op\mathscr{V}_{\mathrm{op}}: there existscG>0c_{G}>0such that𝒬G​[u]≥cG​‖u‖𝒱op2.\mathcal{Q}_{G}[u]\geq c_{G}\|u\|_{\mathscr{V}_{\mathrm{op}}}^{2}.(59)
- 4.

𝒬P:𝒱op→ℝ\mathcal{Q}_{P}:\mathscr{V}_{\mathrm{op}}\to\mathbb{R}is symmetric, non-negative, and either𝒬G\mathcal{Q}_{G}-bounded with relative bound strictly smaller than one or compact with respect to the𝒬G\mathcal{Q}_{G}-form norm.
- 5.

There existsu∈𝒱opu\in\mathscr{V}_{\mathrm{op}}such that𝒬P​[u]>0\mathcal{Q}_{P}[u]>0.

Under Assumption1,𝒬Π\mathcal{Q}_{\Pi}is a closed semibounded form in the range ofΠ\Piconsidered. By the standard representation theorem for closed semibounded quadratic forms, it defines a unique self-adjoint operatorℒΠ\mathcal{L}_{\Pi}[Kato1995,ReedSimon1978]:𝒬Π​[u,v]=⟨u,ℒΠ​v⟩ℋ,v∈Dom⁡(ℒΠ)⊂𝒱op,u∈𝒱op.\mathcal{Q}_{\Pi}[u,v]=\left\langle u,\mathcal{L}_{\Pi}v\right\rangle_{\mathscr{H}},\qquad v\in\operatorname{Dom}(\mathcal{L}_{\Pi})\subset\mathscr{V}_{\mathrm{op}},\quad u\in\mathscr{V}_{\mathrm{op}}.(60)

When the forms are represented by operators, this is written formally asℒΠ=ℒG−Π​ℒP.\mathcal{L}_{\Pi}=\mathcal{L}_{G}-\Pi\mathcal{L}_{P}.(61)

This expression is an operator representation of the pulled-back graph form (58), not an unconstrained subtraction of independent bulk and boundary Hessians.

## Definition 4(Open Hessian).

The open Hessian at a stationary configuration is the self-adjoint operator associated with the closed quadratic form𝒬Π\mathcal{Q}_{\Pi}obtained by restricting the second variation of the total action to𝒱op\mathscr{V}_{\mathrm{op}}. Positivity and coercivity are defined on this admissible exchange space.

The spectrum ofℒΠ\mathcal{L}_{\Pi}is therefore the spectrum of the Hessian projected onto admissible exchange directions. Modes outside the graph of𝒞\mathcal{C}are not tested by the regulated variational problem.

## 8Spectral instability theorem

We now state the instability criterion on the regulated admissible graph. Throughout this section,𝒬P​[u]≡𝒬P∂​[𝒞​u],u∈𝒱op.\mathcal{Q}_{P}[u]\equiv\mathcal{Q}_{P}^{\partial}[\mathcal{C}u],\qquad u\in\mathscr{V}_{\mathrm{op}}.

Thus all Rayleigh quotients are computed only over admissible exchange directions.

Define the pressure-active cone𝒱P:={u∈𝒱op:𝒬P​[u]>0},\mathscr{V}_{P}:=\{u\in\mathscr{V}_{\mathrm{op}}:\mathcal{Q}_{P}[u]>0\},(62)

and, foru∈𝒱Pu\in\mathscr{V}_{P},ℛ​[u]=𝒬G​[u]𝒬P​[u].\mathcal{R}[u]=\frac{\mathcal{Q}_{G}[u]}{\mathcal{Q}_{P}[u]}.(63)

The critical pressure isΠc:=infu∈𝒱Pℛ​[u]=infu:𝒬P∂​[𝒞​u]>0𝒬G​[u]𝒬P∂​[𝒞​u].\Pi_{c}:=\inf_{u\in\mathscr{V}_{P}}\mathcal{R}[u]=\inf_{u:\,\mathcal{Q}_{P}^{\partial}[\mathcal{C}u]>0}\frac{\mathcal{Q}_{G}[u]}{\mathcal{Q}_{P}^{\partial}[\mathcal{C}u]}.(64)

## Theorem 7(Regulated boundary-pressure loss of positivity).

Assume Assumption1. Let𝒬Π=𝒬G−Π​𝒬P\mathcal{Q}_{\Pi}=\mathcal{Q}_{G}-\Pi\mathcal{Q}_{P}

be defined on𝒱op\mathscr{V}_{\mathrm{op}}, and letℒΠ\mathcal{L}_{\Pi}be the self-adjoint operator associated with𝒬Π\mathcal{Q}_{\Pi}. Then:Π<Πc\displaystyle\Pi<\Pi_{c}⇒𝒬Π​[u]>0∀u≠0,\displaystyle\Rightarrow\mathcal{Q}_{\Pi}[u]>0\quad\forall u\neq 0,(65)Π=Πc\displaystyle\Pi=\Pi_{c}⇒infu∈𝒱P𝒬Π​[u]𝒬P​[u]=0,\displaystyle\Rightarrow\inf_{u\in\mathscr{V}_{P}}\frac{\mathcal{Q}_{\Pi}[u]}{\mathcal{Q}_{P}[u]}=0,(66)Π>Πc\displaystyle\Pi>\Pi_{c}⇒∃u∗∈𝒱op​such that​𝒬Π​[u∗]<0.\displaystyle\Rightarrow\exists u_{*}\in\mathscr{V}_{\mathrm{op}}\text{ such that }\mathcal{Q}_{\Pi}[u_{*}]<0.(67)

Consequently, forΠ>Πc\Pi>\Pi_{c}, the stationary configuration is not a strict local minimum relative to the regulated exchange space. If, in addition, the embedding of the𝒬G\mathcal{Q}_{G}-form domain intoℋ\mathscr{H}is compact, or more generally ifinfspec⁡(ℒΠ)\inf\operatorname{spec}(\mathcal{L}_{\Pi})

is attained as an eigenvalue, thenℒΠ\mathcal{L}_{\Pi}has a negative eigenvalue on𝒱op\mathscr{V}_{\mathrm{op}}[Kato1995,ReedSimon1978,Davies1995].

## Proof.

For anyu∈𝒱opu\in\mathscr{V}_{\mathrm{op}},𝒬Π​[u]=𝒬G​[u]−Π​𝒬P​[u].\mathcal{Q}_{\Pi}[u]=\mathcal{Q}_{G}[u]-\Pi\mathcal{Q}_{P}[u].(68)

If𝒬P​[u]=0\mathcal{Q}_{P}[u]=0, coercivity gives𝒬Π​[u]=𝒬G​[u]>0(u≠0).\mathcal{Q}_{\Pi}[u]=\mathcal{Q}_{G}[u]>0\qquad(u\neq 0).

If𝒬P​[u]>0\mathcal{Q}_{P}[u]>0, then𝒬Π​[u]=𝒬P​[u]​(ℛ​[u]−Π).\mathcal{Q}_{\Pi}[u]=\mathcal{Q}_{P}[u]\bigl(\mathcal{R}[u]-\Pi\bigr).(69)

ForΠ<Πc\Pi<\Pi_{c}, one hasℛ​[u]≥Πc>Π\mathcal{R}[u]\geq\Pi_{c}>\Pi, hence𝒬Π​[u]>0\mathcal{Q}_{\Pi}[u]>0. AtΠ=Πc\Pi=\Pi_{c}, the normalized infimum vanishes. ForΠ>Πc\Pi>\Pi_{c}, the definition of the infimum yieldsu∗∈𝒱Pu_{*}\in\mathscr{V}_{P}such thatℛ​[u∗]<Π,\mathcal{R}[u_{*}]<\Pi,

and therefore𝒬Π​[u∗]<0.\mathcal{Q}_{\Pi}[u_{*}]<0.

This proves loss of positivity of the second variation on𝒱op\mathscr{V}_{\mathrm{op}}. Ifinfspec⁡(ℒΠ)\inf\operatorname{spec}(\mathcal{L}_{\Pi})is attained as an eigenvalue, the min–max principle implies that this eigenvalue is negative.
∎

## Corollary 8(Loss of coercivity on the exchange space).

Under the hypotheses of Theorem7, ifΠ>Πc\Pi>\Pi_{c}, the quadratic form𝒬Π\mathcal{Q}_{\Pi}is not coercive on𝒱op\mathscr{V}_{\mathrm{op}}. IfΠ↗Πc\Pi\nearrow\Pi_{c}from below along a compact minimizing branch, the coercivity constant tends to zero.

## Remark 2(Regulation of the instability channel).

The thresholdΠc\Pi_{c}is not computed on the unconstrained boundary space. It is computed only over boundary perturbations reachable as𝒞​u\mathcal{C}u. Thus𝒞\mathcal{C}regulates both the first-order exchange channel and the second-order instability channel.

## Remark 3(Negative direction versus negative eigenvalue).

Equation (67) proves loss of positivity of the second variation on the admissible graph. The stronger statement thatℒΠ\mathcal{L}_{\Pi}possesses a negative eigenvalue requires additional spectral hypotheses ensuring thatinfspec⁡(ℒΠ)\inf\operatorname{spec}(\mathcal{L}_{\Pi})is attained as an eigenvalue.

## 9Minimal spherical example

We give a minimal example illustrating how the compatibility operator regulates the spectral instability channel. Let∂ℳ=SR2\partial\mathcal{M}=S_{R}^{2}, and letu=∑ℓ,muℓ​m​Yℓ​mu=\sum_{\ell,m}u_{\ell m}Y_{\ell m}

be a normal deformation. Consider the stabilizing quadratic form𝒬G​[u]=σG​∫SR2(|∇Σu|2+2R2​u2)​dA,σG>0,\mathcal{Q}_{G}[u]=\sigma_{G}\int_{S_{R}^{2}}\left(|\nabla_{\Sigma}u|^{2}+\frac{2}{R^{2}}u^{2}\right)\mathrm{d}A,\qquad\sigma_{G}>0,(70)

and the boundary pressure form𝒬P∂​[w]=2R​∫SR2w2​dA.\mathcal{Q}_{P}^{\partial}[w]=\frac{2}{R}\int_{S_{R}^{2}}w^{2}\,\mathrm{d}A.(71)

Let the compatibility operator act diagonally on spherical harmonics,𝒞​Yℓ​m=cℓ​Yℓ​m.\mathcal{C}Y_{\ell m}=c_{\ell}Y_{\ell m}.(72)

Then the admissible boundary displacement isw=𝒞​u=∑ℓ,mcℓ​uℓ​m​Yℓ​m,w=\mathcal{C}u=\sum_{\ell,m}c_{\ell}u_{\ell m}Y_{\ell m},

and the pulled-back pressure form is𝒬P​[u]=𝒬P∂​[𝒞​u]=2R​∑ℓ,m|cℓ|2​|uℓ​m|2.\mathcal{Q}_{P}[u]=\mathcal{Q}_{P}^{\partial}[\mathcal{C}u]=\frac{2}{R}\sum_{\ell,m}|c_{\ell}|^{2}|u_{\ell m}|^{2}.(73)

Using−ΔΣ​Yℓ​m=ℓ​(ℓ+1)R2​Yℓ​m,-\Delta_{\Sigma}Y_{\ell m}=\frac{\ell(\ell+1)}{R^{2}}Y_{\ell m},

the regulated open quadratic form diagonalizes as𝒬Π​[u]=∑ℓ,m[σG​ℓ​(ℓ+1)+2R2−2​ΠR​|cℓ|2]​|uℓ​m|2.\mathcal{Q}_{\Pi}[u]=\sum_{\ell,m}\left[\sigma_{G}\frac{\ell(\ell+1)+2}{R^{2}}-\frac{2\Pi}{R}|c_{\ell}|^{2}\right]|u_{\ell m}|^{2}.(74)

Thus the regulated eigenvalue shift isλℓ𝒞​(Π)=σG​ℓ​(ℓ+1)+2R2−2​ΠR​|cℓ|2.\lambda_{\ell}^{\mathcal{C}}(\Pi)=\sigma_{G}\frac{\ell(\ell+1)+2}{R^{2}}-\frac{2\Pi}{R}|c_{\ell}|^{2}.(75)

The mode-dependent threshold isΠc,ℓ𝒞=σG2​R​ℓ​(ℓ+1)+2|cℓ|2,cℓ≠0.\Pi_{c,\ell}^{\mathcal{C}}=\frac{\sigma_{G}}{2R}\frac{\ell(\ell+1)+2}{|c_{\ell}|^{2}},\qquad c_{\ell}\neq 0.(76)

Modes withcℓ=0c_{\ell}=0are not coupled to the boundary-pressure channel. Therefore the regulated critical pressure isΠc𝒞=infℓ∈ℐadm,cℓ≠0σG2​R​ℓ​(ℓ+1)+2|cℓ|2,\Pi_{c}^{\mathcal{C}}=\inf_{\ell\in\mathcal{I}_{\mathrm{adm}},\,c_{\ell}\neq 0}\frac{\sigma_{G}}{2R}\frac{\ell(\ell+1)+2}{|c_{\ell}|^{2}},(77)

whereℐadm\mathcal{I}_{\mathrm{adm}}denotes the harmonics retained after constraints such as volume fixing or quotienting of rigid modes.

This example shows explicitly that𝒞\mathcal{C}does more than restrict admissible variations: it selects which boundary modes can exchange action with the bulk and therefore which spectral channels can lose positivity.

## 10Discussion

The construction developed here changes the role of the boundary in variational mechanics. In the closed formulation, the boundary is removed from the admissible variation class by fixing traces or by imposing independently testable natural conditions. In the regulated open formulation, the boundary remains part of the variational system, but only through an admissible graph𝒱op=Graph⁡(𝒞).\mathscr{V}_{\mathrm{op}}=\operatorname{Graph}(\mathcal{C}).

This is the main structural distinction: openness is neither arbitrary boundary forcing nor unconstrained nonlocal cancellation. It is stationarity after restriction to a specified compatibility channel.

The compatibility operator𝒞\mathcal{C}is therefore the object that regulates bulk–boundary exchange. It determines which boundary variations are coupled to a given bulk variation, and its adjoint pulls boundary variational fluxes back to the bulk test space. The projected balanceEL+𝒞∗​(ΠL+E∂ℬ)=0in​𝒱bulk′E_{L}+\mathcal{C}^{*}\left(\Pi_{L}+E_{\partial\mathcal{B}}\right)=0\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime}

is the weak form of this exchange. It does not modify the Euler–Lagrange operator by an external force; rather, it states that the total first variation vanishes on the admissible graph.

This viewpoint clarifies the relation with classical boundary conditions. Fixed-boundary problems correspond to a trivial boundary channel. Natural boundary conditions correspond to independently testable boundary directions. Regulated open problems lie between these limits: boundary degrees of freedom are active, but only through the operator that defines admissibility. Thus the generalized natural condition is not discarded; it is recovered as the separable limit of graph-space stationarity.

The Hamilton–Jacobi and geometric stress formulations follow the same pattern. In action space, the boundary derivative of the on-shell action is pulled back by𝒞∗\mathcal{C}^{*}. In geometric problems, boundary stress is either balanced pointwise when metric variations are independent, or pulled back through a metric compatibility operator when they are not. These formulations are not additional assumptions; they are equivalent representations of the same regulated admissible class.

At second order, the decisive object is not the unconstrained Hessian but its restriction to𝒱op\mathscr{V}_{\mathrm{op}}. For pressure-like boundary couplings, this produces the pulled-back form𝒬Π​[u]=𝒬G​[u]−Π​𝒬P∂​[𝒞​u].\mathcal{Q}_{\Pi}[u]=\mathcal{Q}_{G}[u]-\Pi\mathcal{Q}_{P}^{\partial}[\mathcal{C}u].

The Rayleigh threshold is therefore computed only over exchange-compatible directions. This explains why the compatibility operator controls both first-order action exchange and second-order loss of positivity.

The spherical example makes this control explicit. When𝒞\mathcal{C}is diagonal in spherical harmonics, the coefficientscℓc_{\ell}select which modes couple to the boundary-pressure sector. Modes outside the range of𝒞\mathcal{C}do not enter the instability quotient; modes with stronger coupling destabilize at lower pressure. The example is not intended as a model of a specific elastic surface, but as a transparent realization of the general graph-space criterion.

The framework remains close to classical variational analysis. It uses standard first variations, natural boundary terms, closed quadratic forms and Rayleigh–Ritz arguments[Courant1953,ReedSimon1978,Evans2010]. The new ingredient is the admissible exchange space. Once that space is specified, the rest of the construction follows by restriction, pullback and spectral analysis on the resulting graph.

## 11Conclusion

Variational openness has been formulated as a conservative extension of closed variational mechanics. The extension leaves the variational calculus unchanged, but changes the admissible class on which stationarity is imposed. Its central object is the regulated graph𝒱op=Graph⁡(𝒞),\mathscr{V}_{\mathrm{op}}=\operatorname{Graph}(\mathcal{C}),

which encodes the admissible exchange channel between bulk and boundary variations.

On this graph, stationarity is a projected condition rather than a separate annihilation of the bulk and boundary variations. The first variation closes through the pullback balanceEL+𝒞∗​(ΠL+E∂ℬ)=0in​𝒱bulk′,E_{L}+\mathcal{C}^{*}\left(\Pi_{L}+E_{\partial\mathcal{B}}\right)=0\quad\text{in }\mathscr{V}_{\mathrm{bulk}}^{\prime},

which gives the variational meaning of bulk–boundary action exchange.

At second order, the open Hessian is the self-adjoint operator associated with the closed quadratic form obtained by restricting the second variation to𝒱op\mathscr{V}_{\mathrm{op}}. For pressure-like boundary couplings this gives a pulled-back form, and the Rayleigh–Ritz criterion on the regulated graph determines the threshold at which positivity and coercivity are lost. Boundary degrees of freedom enter not as auxiliary constraints or external forces, but as regulated contributors to stationarity and stability. The framework is not a modification of variational calculus, but a reformulation of admissibility and stationarity on regulated exchange spaces.
\bmhead

Supplementary information

No supplementary information is included in this draft.\bmhead

Acknowledgements

The author thanks José A. Santiago and Jesús Fernández-Castillo for fruitful discussions.

## Appendix AClassical free-boundary problems as separable limits

Classical free-boundary and transversality problems are recovered as separable limits of graph-space stationarity. ConsiderS​[q]=∫t0t1L​(q,q˙,t)​dt+B​(q​(t1),t1),S[q]=\int_{t_{0}}^{t_{1}}L(q,\dot{q},t)\,\mathrm{d}t+B(q(t_{1}),t_{1}),(78)

withq​(t0)q(t_{0})fixed. Its first variation isδ​S=∫t0t1(∂L∂q−dd​t​∂L∂q˙)​δ​q​dt+[p​(t1)+∇B​(q​(t1),t1)]​δ​q​(t1),\delta S=\int_{t_{0}}^{t_{1}}\left(\frac{\partial L}{\partial q}-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial\dot{q}}\right)\delta q\,\mathrm{d}t+\left[p(t_{1})+\nabla B(q(t_{1}),t_{1})\right]\delta q(t_{1}),(79)

wherep=∂L/∂q˙p=\partial L/\partial\dot{q}. Ifδ​q​(t1)\delta q(t_{1})is independently testable, stationarity givesdd​t​∂L∂q˙−∂L∂q=0,p​(t1)+∇B​(q​(t1),t1)=0.\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial\dot{q}}-\frac{\partial L}{\partial q}=0,\qquad p(t_{1})+\nabla B(q(t_{1}),t_{1})=0.(80)

This is the finite-dimensional analogue of
(33)–(34).

If the endpoint variation is constrained byδ​q​(t1)=𝒞​η,\delta q(t_{1})=\mathcal{C}\eta,(81)

then stationarity gives∫t0t1(∂L∂q−dd​t​∂L∂q˙)​η​dt+[p​(t1)+∇B​(q​(t1),t1)]​𝒞​η=0∀η.\int_{t_{0}}^{t_{1}}\left(\frac{\partial L}{\partial q}-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial\dot{q}}\right)\eta\,\mathrm{d}t+\left[p(t_{1})+\nabla B(q(t_{1}),t_{1})\right]\mathcal{C}\eta=0\quad\forall\eta.(82)

Equivalently,EL+𝒞∗​[p​(t1)+∇B​(q​(t1),t1)]=0E_{L}+\mathcal{C}^{*}\left[p(t_{1})+\nabla B(q(t_{1}),t_{1})\right]=0(83)

on the admissible variation space. Thus the classical transversality condition is the separable endpoint limit of the regulated balance.

## Appendix BSpherical second variation

For a normal deformationr=R+ur=R+uofSR2S_{R}^{2}, the area and volume expansions areA​[u]\displaystyle A[u]=4​π​R2+∫SR2(u2R2+12​|∇Σu|2)​dA+O​(u3),\displaystyle=4\pi R^{2}+\int_{S_{R}^{2}}\left(\frac{u^{2}}{R^{2}}+\frac{1}{2}|\nabla_{\Sigma}u|^{2}\right)\mathrm{d}A+O(u^{3}),(84)V​[u]\displaystyle V[u]=4​π​R33+∫SR2u​dA+1R​∫SR2u2​dA+O​(u3).\displaystyle=\frac{4\pi R^{3}}{3}+\int_{S_{R}^{2}}u\,\mathrm{d}A+\frac{1}{R}\int_{S_{R}^{2}}u^{2}\,\mathrm{d}A+O(u^{3}).(85)

After removal of the mean mode, or under a fixed-volume constraint, the linear volume term vanishes. With the conventionδ2​S=(1/2)​𝒬​[u]\delta^{2}S=(1/2)\mathcal{Q}[u], the pressure contribution gives𝒬P∂​[u]=2R​∫SR2u2​dA.\mathcal{Q}_{P}^{\partial}[u]=\frac{2}{R}\int_{S_{R}^{2}}u^{2}\,\mathrm{d}A.(86)

For a regulated boundary displacementw=𝒞​uw=\mathcal{C}u,𝒬P​[u]=𝒬P∂​[𝒞​u]=2R​∫SR2(𝒞​u)2​dA.\mathcal{Q}_{P}[u]=\mathcal{Q}_{P}^{\partial}[\mathcal{C}u]=\frac{2}{R}\int_{S_{R}^{2}}(\mathcal{C}u)^{2}\,\mathrm{d}A.(87)

If𝒞​Yℓ​m=cℓ​Yℓ​m,\mathcal{C}Y_{\ell m}=c_{\ell}Y_{\ell m},

then𝒬P​[u]=2R​∑ℓ,m|cℓ|2​|uℓ​m|2,\mathcal{Q}_{P}[u]=\frac{2}{R}\sum_{\ell,m}|c_{\ell}|^{2}|u_{\ell m}|^{2},(88)

which yields the regulated eigenvalues and thresholds in
(75)–(77).

## Appendix CQuadratic-form interpretation of the open Hessian

Let𝒬\mathcal{Q}be a densely defined, closed, semibounded symmetric quadratic form on a Hilbert spaceℋ\mathscr{H}. In the regulated setting, its form domain is the graph space𝒱op=Graph⁡(𝒞)={(u,𝒞​u):u∈𝒱bulk},\mathscr{V}_{\mathrm{op}}=\operatorname{Graph}(\mathcal{C})=\{(u,\mathcal{C}u):u\in\mathscr{V}_{\mathrm{bulk}}\},(89)

or an equivalent closed admissible subspace after quotienting null modes. The graph norm and the closedness of the graph are understood in the standard functional-analytic sense[Conway1990,Brezis2011].

By the representation theorem for closed semibounded quadratic forms,𝒬\mathcal{Q}determines a unique self-adjoint operatorLLsatisfying[Kato1995,ReedSimon1978]𝒬​[u,v]=⟨u,L​v⟩ℋ,u∈𝒱op,v∈Dom⁡(L)⊂𝒱op.\mathcal{Q}[u,v]=\left\langle u,Lv\right\rangle_{\mathscr{H}},\qquad u\in\mathscr{V}_{\mathrm{op}},\quad v\in\operatorname{Dom}(L)\subset\mathscr{V}_{\mathrm{op}}.(90)

The operator domain consists of thosev∈𝒱opv\in\mathscr{V}_{\mathrm{op}}for which the mapu↦𝒬​[u,v]u\mapsto\mathcal{Q}[u,v]

is continuous in theℋ\mathscr{H}-norm.

If the second variation decomposes into bulk, boundary and mixed parts, restriction to the graph gives𝒬op​[u]=𝒬bulk​[u]+𝒬∂​[𝒞​u]+2​𝒬mix​[u,𝒞​u].\mathcal{Q}_{\mathrm{op}}[u]=\mathcal{Q}_{\mathrm{bulk}}[u]+\mathcal{Q}_{\partial}[\mathcal{C}u]+2\mathcal{Q}_{\mathrm{mix}}[u,\mathcal{C}u].(91)

In the additive pressure-like case,𝒬Π​[u]=𝒬G​[u]−Π​𝒬P∂​[𝒞​u].\mathcal{Q}_{\Pi}[u]=\mathcal{Q}_{G}[u]-\Pi\mathcal{Q}_{P}^{\partial}[\mathcal{C}u].(92)

ThusℒΠ=ℒG−Π​ℒP\mathcal{L}_{\Pi}=\mathcal{L}_{G}-\Pi\mathcal{L}_{P}

is an operator representation of the pulled-back graph form, not an unconstrained subtraction of independent bulk and boundary operators.

## Declarations\bmhead

Funding
Financial support was provided by the Agencia Estatal de Investigación (AEI, Spain)
under Grants TED2021-132296B-C52 and CPP2024-011880, and by Fundación
BBVA–Programa Fundamentos 2025.\bmhead

Competing interests
The author declares no competing interests.\bmhead

Ethics approval and consent to participate
Not applicable.\bmhead

Consent for publication
Not applicable.\bmhead

Data availability
No datasets were generated or analysed during the current study.\bmhead

Materials availability
Not applicable.\bmhead

Code availability
Not applicable.\bmhead

Author contribution
F.M. conceived the framework, developed the mathematical formulation and wrote the manuscript.

## References

## 


- 


Major funding support from
