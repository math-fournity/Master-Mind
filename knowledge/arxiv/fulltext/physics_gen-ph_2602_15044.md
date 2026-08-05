# In models of spontaneous wave-function collapse, why only fermions collapse, not bosons?

**arXiv ID**: 2602.15044v1
**Authors**: Tejinder P. Singh
**Published**: 2026-02-04
**Categories**: physics.gen-ph, quant-ph
**Comments**: 10 pages
**HTML URL**: https://arxiv.org/html/2602.15044v1

## Abstract

Objective collapse models are often implemented so that collapse acts only on the fermionic (matter) sector, while bosonic fields do not undergo fundamental collapse. In generalized trace dynamics (GTD), spontaneous localization is expected to arise when the trace Hamiltonian has a significant anti-self-adjoint component. In this note we show, starting from the STM-atom (spacetime-matter atom) trace Lagrangian written in terms of two inequivalent matrix velocities $\dot Q_1$ and $\dot Q_2$, that the purely bosonic subsector admits a self-adjoint Hamiltonian, whereas the fermionic sector carries an intrinsic anti-self-adjoint contribution. The key structural input is that making the trace Lagrangian bosonic requires insertion of two \emph{unequal} odd-grade Grassmann elements $β_1\neq β_2$. Assuming natural adjoint properties for these elements, we compute the trace Hamiltonian explicitly via trace-derivative canonical momenta (with bosonic and fermionic variations treated separately) and isolate the resulting anti-self-adjoint term. This provides a first-principles mechanism, within GTD, for why only fermionic degrees of freedom act as collapse channels.

## Full Text

In models of spontaneous wave-function collapse, why only fermions collapse, not bosons?
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

## In models of spontaneous wave-function collapse, why only fermions collapse, not bosons?Tejinder P. Singh

## Abstract

Objective collapse models are often implemented so that collapse acts only on the
fermionic (matter) sector, while bosonic fields do not undergo fundamental collapse.
In generalized trace dynamics (GTD), spontaneous localization is expected to arise
when the trace Hamiltonian has a significant anti-self-adjoint component.
In this note we show, starting from the STM-atom (spacetime-matter atom) trace Lagrangian written in terms of
two inequivalent matrix velocitiesQ˙1\dot{Q}_{1}andQ˙2\dot{Q}_{2}, that the purely bosonic
subsector admits a self-adjoint Hamiltonian, whereas the fermionic sector carries an
intrinsic anti-self-adjoint contribution. The key structural input is that making the
trace Lagrangian bosonic requires insertion of twounequalodd-grade Grassmann
elementsβ1≠β2\beta_{1}\neq\beta_{2}. Assuming natural adjoint properties for these elements,
we compute the trace Hamiltonian explicitly via trace-derivative canonical momenta
(with bosonic and fermionic variations treated separately) and isolate the resulting
anti-self-adjoint term. This provides a first-principles mechanism, within GTD, for
why only fermionic degrees of freedom act as collapse channels.

## 1Introduction

A recurring conceptual obstacle in quantum gravity is the role of time: standard quantum
theory (and, in particular, quantum field theory) is formulated with respect to an external
classical time parameter, whereas general relativity treats spacetime geometry as dynamical.
Generalized trace dynamics (GTD)[1]addresses this tension by building on Adler’strace dynamics(TD)[2], a deterministic matrix-valued Lagrangian/Hamiltonian dynamics in which the action is the
trace of a polynomial in noncommuting matrix degrees of freedom (bosonic even-grade matrices and
fermionic odd-grade matrices). A key structural feature of TD is its global unitary invariance,
which gives rise to a novel conserved quantity—the Adler–Millard charge—with dimensions of action,C~=∑r∈B[qr,pr]−∑r∈F{qr,pr},\tilde{C}\;=\;\sum_{r\in B}\,[q_{r},p_{r}]\;-\;\sum_{r\in F}\,\{q_{r},p_{r}\}\,,(1.1)

absent in ordinary classical dynamics. When the statistical mechanics of TD is developed, equipartition
ofC~\tilde{C}at equilibrium yields the canonical (anti)commutation relations and an emergent unitary
quantum (field) dynamics for the canonical averages. Conversely, when the anti-self-adjoint part of
the fundamental trace Hamiltonian is not negligible, fluctuations about equilibrium can drive effective
nonunitary nonlinear stochastic dynamics and spontaneous localization[3].

GTD extends this pre-quantum framework toward quantum gravity by promoting gravitational degrees of
freedom to matrices and by replacing classical spacetime labels by a noncommutative “pre-spacetime”
(quaternionic/octonionic, in the models of interest), thereby aiming for a formulation of quantum dynamics
without reference to an external classical time (evolution may be parametrized by Connes timeτ\tau)[1].
The fundamental entities areatoms of spacetime-matter(STM atoms): matrix degrees of freedomqi=qB​i+qF​iq_{i}=q_{Bi}+q_{Fi}whose bosonic components are interpreted as “atoms of spacetime,” while the full
STM atom represents a fermion together with the bosonic fields it sources (for example, an electron together
with its electromagnetic, weak, and gravitational fields). Entanglement among many STM atoms, followed by
spontaneous localization, is conjectured to yield classical spacetime geometry and classical macroscopic
bodies[4]. In this setting, objective collapse is expected precisely in regimes where the fundamental trace
Hamiltonian develops a significant anti-self-adjoint component. This motivates the specific structural
question addressed below: whether the STM-atom trace Lagrangian underlying GTD generates an intrinsic
anti-self-adjoint contribution only in the fermionic sector—thereby explaining why collapse models
effectively act on fermions and not on bosonic degrees of freedom.

Spontaneous collapse models (e.g. CSL-type modifications of quantum dynamics)[5,6,7,8,9]are commonly set up so that the collapse-inducing nonunitarity couples to matter degrees
of freedom, while bosonic field degrees do not constitute independent collapse channels.
From the viewpoint of generalized trace dynamics (GTD), a natural structural origin of
collapse is the appearance of an anti-self-adjoint (ASA) component of the trace Hamiltonian:
when ASA effects are significant, coarse-graining can yield effective nonunitary stochastic
dynamics and spontaneous localization (as in Adler-type trace dynamics arguments[2]).

A central open issue for GTD phenomenology is then:

Does the fundamental GTD STM-atom Lagrangian generate ASA contributions only
in the fermionic sector, thereby explaining why only fermions collapse?

In this note we answer this question in the affirmative, for the STM-atom action written
in terms of two inequivalent matrix degrees of freedomQ1Q_{1}andQ2Q_{2}.
We work directly at the level of the trace Lagrangian and its Legendre transform,
using trace derivatives in the sense of Adler, and we keep variations with respect to
bosonic and fermionic variables strictly separated.

## 2STM-atom action and unified variables

## 2.1Action

We begin with the unified STM-action[1]Sℏ=12​∫d​ττPl​Tr​[λ​Q˙1†​Q˙2],λ:=LPl2L2.\frac{S}{\hbar}=\frac{1}{2}\int\frac{d\tau}{\tau_{\mathrm{Pl}}}\;\mathrm{Tr}\!\left[\lambda\,\dot{Q}_{1}^{\dagger}\,\dot{Q}_{2}\right],\qquad\lambda:=\frac{L_{\mathrm{Pl}}^{2}}{L^{2}}.(2.1)

Hereτ\tauis Connes time and†\daggerdenotes the GTD adjoint on matrices with
Grassmann entries.

The unified velocities are defined (with bosonic/fermionic splitting) byQ˙B\displaystyle\dot{Q}_{B}=1L​(i​α​qB+L​q˙B),\displaystyle=\frac{1}{L}\left(i\alpha\,q_{B}+L\dot{q}_{B}\right),Q˙F\displaystyle\dot{Q}_{F}=1L​(i​α​qF+L​q˙F),\displaystyle=\frac{1}{L}\left(i\alpha\,q_{F}+L\dot{q}_{F}\right),(2.2)Q˙1†\displaystyle\dot{Q}_{1}^{\dagger}=Q˙B†+λ​β1​Q˙F†,\displaystyle=\dot{Q}_{B}^{\dagger}+\lambda\,\beta_{1}\,\dot{Q}_{F}^{\dagger},Q˙2\displaystyle\dot{Q}_{2}=Q˙B+λ​β2​Q˙F,\displaystyle=\dot{Q}_{B}+\lambda\,\beta_{2}\,\dot{Q}_{F},(2.3)

whereβ1,β2\beta_{1},\beta_{2}areodd-gradeGrassmann elements inserted so that the
trace Lagrangian is bosonic. The dynamics requiresβ1≠β2\beta_{1}\neq\beta_{2}[10]. Also,α\alphais a real number which stands for the Yang-Mills coupling constant.

## 2.2Grading, adjoint, and graded cyclicity

We writeε​(X)∈{0,1}\varepsilon(X)\in\{0,1\}for the Grassmann parity:ε​(X)=0\varepsilon(X)=0for bosonic (even-grade) matrices andε​(X)=1\varepsilon(X)=1for fermionic (odd-grade) matrices.
We assumeε​(Q˙B)=0,ε​(Q˙F)=1,ε​(βa)=1(a=1,2).\varepsilon(\dot{Q}_{B})=0,\qquad\varepsilon(\dot{Q}_{F})=1,\qquad\varepsilon(\beta_{a})=1\quad(a=1,2).(2.4)

Thusβa​Q˙F\beta_{a}\dot{Q}_{F}andβa​Q˙F†\beta_{a}\dot{Q}_{F}^{\dagger}are even, soQ˙1†\dot{Q}_{1}^{\dagger}andQ˙2\dot{Q}_{2}are bosonic as required by the form of the trace action.

For matrices with Grassmann entries one uses the standard involution(A​B)†=B†​A†,Tr​(A)†=Tr​(A†),(AB)^{\dagger}=B^{\dagger}A^{\dagger},\qquad\mathrm{Tr}(A)^{\dagger}=\mathrm{Tr}(A^{\dagger}),(2.5)

together with graded cyclicity of the trace for homogeneous factors:Tr​(A​B)=(−1)ε​(A)​ε​(B)​Tr​(B​A).\mathrm{Tr}(AB)=(-1)^{\varepsilon(A)\varepsilon(B)}\,\mathrm{Tr}(BA).(2.6)

(Equivalently, a cyclic shift of a homogeneous factorXXthrough a productYYyieldsTr​(Y​X)=(−1)ε​(X)​ε​(Y)​Tr​(X​Y)\mathrm{Tr}(YX)=(-1)^{\varepsilon(X)\varepsilon(Y)}\mathrm{Tr}(XY).)

## 3Trace-derivative canonical momenta and Hamiltonian

## 3.1Trace Lagrangian

From (2.1) the trace Lagrangian density (inτ\tau) isℒ=ℏ2​τPl​Tr​[λ​Q˙1†​Q˙2].\mathcal{L}=\frac{\hbar}{2\tau_{\mathrm{Pl}}}\;\mathrm{Tr}\!\left[\lambda\,\dot{Q}_{1}^{\dagger}\dot{Q}_{2}\right].(3.1)

Crucially,ℒ\mathcal{L}depends on the bosonic velocitiesQ˙B,Q˙B†\dot{Q}_{B},\dot{Q}_{B}^{\dagger}and
fermionic velocitiesQ˙F,Q˙F†\dot{Q}_{F},\dot{Q}_{F}^{\dagger}only through (2.3).

## 3.2Trace derivatives (bosons and fermions varied separately)

Following Adler, the trace derivative is defined by placing the variation to the far right:δ​ℒ=Tr​(δ​ℒδ​O​δ​O),\delta\mathcal{L}=\mathrm{Tr}\!\left(\frac{\delta\mathcal{L}}{\delta O}\,\delta O\right),(3.2)

where for fermionicOOthe graded cyclicity (2.6) is used to moveδ​O\delta Oto the right, generating sign factors only whenδ​O\delta Opasses odd-grade factors.
In the present computation wedo notvary with respect to mixed variables;
we only vary with respect toQ˙B,Q˙B†\dot{Q}_{B},\dot{Q}_{B}^{\dagger}(bosonic) andQ˙F,Q˙F†\dot{Q}_{F},\dot{Q}_{F}^{\dagger}(fermionic).

## 3.3Canonical momenta

Define the overall prefactorc:=ℏ2​τPl.c:=\frac{\hbar}{2\tau_{\mathrm{Pl}}}.(3.3)

## Bosonic momenta.

Varying (3.1) with respect toQ˙B\dot{Q}_{B}andQ˙B†\dot{Q}_{B}^{\dagger}givesΠB\displaystyle\Pi_{B}:=δ​ℒδ​Q˙B=c​λ​Q˙1†,\displaystyle:=\frac{\delta\mathcal{L}}{\delta\dot{Q}_{B}}=c\,\lambda\,\dot{Q}_{1}^{\dagger},(3.4)ΠB†\displaystyle\Pi_{B}^{\dagger}:=δ​ℒδ​Q˙B†=c​λ​Q˙2.\displaystyle:=\frac{\delta\mathcal{L}}{\delta\dot{Q}_{B}^{\dagger}}=c\,\lambda\,\dot{Q}_{2}.(3.5)

## Fermionic momenta.

UsingQ˙2=Q˙B+λ​β2​Q˙F\dot{Q}_{2}=\dot{Q}_{B}+\lambda\beta_{2}\dot{Q}_{F},ΠF:=δ​ℒδ​Q˙F=c​λ​Q˙1†⋅(λ​β2)=c​λ2​Q˙1†​β2.\Pi_{F}:=\frac{\delta\mathcal{L}}{\delta\dot{Q}_{F}}=c\,\lambda\,\dot{Q}_{1}^{\dagger}\cdot(\lambda\beta_{2})=c\,\lambda^{2}\,\dot{Q}_{1}^{\dagger}\,\beta_{2}.(3.6)

Similarly, usingQ˙1†=Q˙B†+λ​β1​Q˙F†\dot{Q}_{1}^{\dagger}=\dot{Q}_{B}^{\dagger}+\lambda\beta_{1}\dot{Q}_{F}^{\dagger}and
bringingδ​Q˙F†\delta\dot{Q}_{F}^{\dagger}to the right inside the trace using (2.6),ΠF†:=δ​ℒδ​Q˙F†=c​λ2​Q˙2​β1.\Pi_{F}^{\dagger}:=\frac{\delta\mathcal{L}}{\delta\dot{Q}_{F}^{\dagger}}=c\,\lambda^{2}\,\dot{Q}_{2}\,\beta_{1}.(3.7)

Equations (3.4)–(3.7) are the separated bosonic/fermionic canonical
momenta required for a trace-dynamics Legendre transform.

## 3.4Legendre transform and explicit Hamiltonian

We define the trace Hamiltonian by summing over all independent velocities:ℋ=Tr​(ΠB​Q˙B+ΠF​Q˙F+ΠB†​Q˙B†+ΠF†​Q˙F†)−ℒ.\mathcal{H}=\mathrm{Tr}\!\left(\Pi_{B}\dot{Q}_{B}+\Pi_{F}\dot{Q}_{F}+\Pi_{B}^{\dagger}\dot{Q}_{B}^{\dagger}+\Pi_{F}^{\dagger}\dot{Q}_{F}^{\dagger}\right)-\mathcal{L}.(3.8)

Substituting (3.4)–(3.7) and using (2.3), one findsTr​(ΠB​Q˙B+ΠF​Q˙F)\displaystyle\mathrm{Tr}(\Pi_{B}\dot{Q}_{B}+\Pi_{F}\dot{Q}_{F})=c​Tr​(λ​Q˙1†​(Q˙B+λ​β2​Q˙F))=c​Tr​(λ​Q˙1†​Q˙2)=ℒ,\displaystyle=c\,\mathrm{Tr}\!\left(\lambda\,\dot{Q}_{1}^{\dagger}(\dot{Q}_{B}+\lambda\beta_{2}\dot{Q}_{F})\right)=c\,\mathrm{Tr}\!\left(\lambda\,\dot{Q}_{1}^{\dagger}\dot{Q}_{2}\right)=\mathcal{L},(3.9)Tr​(ΠB†​Q˙B†+ΠF†​Q˙F†)\displaystyle\mathrm{Tr}(\Pi_{B}^{\dagger}\dot{Q}_{B}^{\dagger}+\Pi_{F}^{\dagger}\dot{Q}_{F}^{\dagger})=c​Tr​(λ​(Q˙B†+λ​β1​Q˙F†)​Q˙2)=c​Tr​(λ​Q˙1†​Q˙2)=ℒ,\displaystyle=c\,\mathrm{Tr}\!\left(\lambda\,(\dot{Q}_{B}^{\dagger}+\lambda\beta_{1}\dot{Q}_{F}^{\dagger})\dot{Q}_{2}\right)=c\,\mathrm{Tr}\!\left(\lambda\,\dot{Q}_{1}^{\dagger}\dot{Q}_{2}\right)=\mathcal{L},(3.10)

where in the second line we used thatQ˙2\dot{Q}_{2}is bosonic and applied graded cyclicity.
Thereforeℋ=ℒ=ℏ2​τPlTr[λQ˙1†Q˙2].\boxed{\mathcal{H}=\mathcal{L}=\frac{\hbar}{2\tau_{\mathrm{Pl}}}\;\mathrm{Tr}\!\left[\lambda\,\dot{Q}_{1}^{\dagger}\dot{Q}_{2}\right].}(3.11)

This is the trace-dynamics analog of the Bateman-type cross-kinetic structure:
the Hamiltonian equals the Lagrangian, but need not be self-adjoint becauseQ˙1\dot{Q}_{1}andQ˙2\dot{Q}_{2}are inequivalent.

## 4Bosonic vs fermionic contributions and the anti-self-adjoint part

## 4.1Decomposition of the Hamiltonian

Expanding (3.11) using (2.3) givesℋ=ℋB​B+ℋB​F+ℋF​F,\mathcal{H}=\mathcal{H}_{BB}+\mathcal{H}_{BF}+\mathcal{H}_{FF},(4.1)

whereℋB​B\displaystyle\mathcal{H}_{BB}=c​Tr​(λ​Q˙B†​Q˙B),\displaystyle=c\,\mathrm{Tr}\!\left(\lambda\,\dot{Q}_{B}^{\dagger}\dot{Q}_{B}\right),(4.2)ℋB​F\displaystyle\mathcal{H}_{BF}=c​Tr​(λ2​Q˙B†​β2​Q˙F+λ2​β1​Q˙F†​Q˙B),\displaystyle=c\,\mathrm{Tr}\!\left(\lambda^{2}\,\dot{Q}_{B}^{\dagger}\beta_{2}\dot{Q}_{F}+\lambda^{2}\,\beta_{1}\dot{Q}_{F}^{\dagger}\dot{Q}_{B}\right),(4.3)ℋF​F\displaystyle\mathcal{H}_{FF}=c​Tr​(λ3​β1​Q˙F†​β2​Q˙F).\displaystyle=c\,\mathrm{Tr}\!\left(\lambda^{3}\,\beta_{1}\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F}\right).(4.4)

## 4.2Adjoint assumptions forβ1,β2\beta_{1},\beta_{2}

We now impose the following adjoint properties:β1†=−β1,β2†=−β2,β1≠β2,ε(β1)=ε(β2)=1.\boxed{\beta_{1}^{\dagger}=-\beta_{1},\qquad\beta_{2}^{\dagger}=-\beta_{2},\qquad\beta_{1}\neq\beta_{2},\qquad\varepsilon(\beta_{1})=\varepsilon(\beta_{2})=1.}(4.5)

We also assume the natural graded (anti)commutation with dynamical variables:βa\beta_{a}commutes with bosonic variables and anticommutes with fermionic variables.

## 4.3Self-adjointness of the purely bosonic sector

From (4.2) and (2.5),ℋB​B†=c​Tr​(λ​(Q˙B†​Q˙B)†)=c​Tr​(λ​Q˙B†​Q˙B)=ℋB​B.\mathcal{H}_{BB}^{\dagger}=c\,\mathrm{Tr}\!\left(\lambda\,(\dot{Q}_{B}^{\dagger}\dot{Q}_{B})^{\dagger}\right)=c\,\mathrm{Tr}\!\left(\lambda\,\dot{Q}_{B}^{\dagger}\dot{Q}_{B}\right)=\mathcal{H}_{BB}.(4.6)

Hence the bosonic subsector has a self-adjoint Hamiltonian and does not by itself
supply an ASA contribution.

## 4.4An intrinsic ASA fermionic contribution

Consider the fermionic term (4.4). Using (2.5) and (4.5),ℋF​F†\displaystyle\mathcal{H}_{FF}^{\dagger}=c​Tr​((λ3​β1​Q˙F†​β2​Q˙F)†)=c​Tr​(λ3​Q˙F†​β2†​Q˙F​β1†)\displaystyle=c\,\mathrm{Tr}\!\left((\lambda^{3}\beta_{1}\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F})^{\dagger}\right)=c\,\mathrm{Tr}\!\left(\lambda^{3}\,\dot{Q}_{F}^{\dagger}\beta_{2}^{\dagger}\dot{Q}_{F}\beta_{1}^{\dagger}\right)=c​Tr​(λ3​Q˙F†​(−β2)​Q˙F​(−β1))=c​Tr​(λ3​Q˙F†​β2​Q˙F​β1).\displaystyle=c\,\mathrm{Tr}\!\left(\lambda^{3}\,\dot{Q}_{F}^{\dagger}(-\beta_{2})\dot{Q}_{F}(-\beta_{1})\right)=c\,\mathrm{Tr}\!\left(\lambda^{3}\,\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F}\beta_{1}\right).(4.7)

Now apply graded cyclicity (2.6) to cyclically shift the final odd factorβ1\beta_{1}to the front. Sinceβ1\beta_{1}is odd and the productQ˙F†​β2​Q˙F\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F}is also odd (three odd factors), we obtain a minus sign:Tr​(Q˙F†​β2​Q˙F​β1)=−Tr​(β1​Q˙F†​β2​Q˙F).\mathrm{Tr}(\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F}\beta_{1})=-\,\mathrm{Tr}(\beta_{1}\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F}).(4.8)

Combining (4.7) and (4.8) yieldsℋF​F†=−ℋF​F.\boxed{\mathcal{H}_{FF}^{\dagger}=-\,\mathcal{H}_{FF}.}(4.9)

ThusℋF​F\mathcal{H}_{FF}ispurely anti-self-adjoint. In particular, it provides an explicit
ASA contribution to the Hamiltonian, and this contribution vanishes identically when the
fermionic sector is absent.

## Role ofβ1≠β2\beta_{1}\neq\beta_{2}.

If one attempted to setβ1=β2=β\beta_{1}=\beta_{2}=\beta, the fermionic contribution collapses:
becauseβ\betais odd,β​Q˙F†​β=−β​β​Q˙F†=0\beta\dot{Q}_{F}^{\dagger}\beta=-\beta\beta\dot{Q}_{F}^{\dagger}=0,
soℋF​F\mathcal{H}_{FF}would vanish. Hence the requirementβ1≠β2\beta_{1}\neq\beta_{2}is not only
dynamically necessary[10]; it is also structurally responsible for a nontrivial ASA fermionic term.

## 4.5ASA part of the full Hamiltonian

Define the self-adjoint and anti-self-adjoint parts of the trace Hamiltonian byℋsa:=12​(ℋ+ℋ†),ℋasa:=12​(ℋ−ℋ†).\mathcal{H}_{\mathrm{sa}}:=\frac{1}{2}(\mathcal{H}+\mathcal{H}^{\dagger}),\qquad\mathcal{H}_{\mathrm{asa}}:=\frac{1}{2}(\mathcal{H}-\mathcal{H}^{\dagger}).(4.10)

From (4.1), (4.6), and (4.9),ℋasa=12(ℋB​F−ℋB​F†)+ℋF​F.\boxed{\mathcal{H}_{\mathrm{asa}}=\frac{1}{2}(\mathcal{H}_{BF}-\mathcal{H}_{BF}^{\dagger})+\mathcal{H}_{FF}.}(4.11)

Independently of the detailed adjoint properties of the mixed termℋB​F\mathcal{H}_{BF},
the key point is thateverycontribution toℋasa\mathcal{H}_{\mathrm{asa}}contains fermionic variables:
ifQ˙F=Q˙F†=0\dot{Q}_{F}=\dot{Q}_{F}^{\dagger}=0, thenℋasa=0\mathcal{H}_{\mathrm{asa}}=0identically.

## Remark (adjoint convention forβ1,2\beta_{1,2}).

The anti-self-adjoint character of the purely fermionic contributionℋF​F=c​Tr​(λ3​β1​Q˙F†​β2​Q˙F)\mathcal{H}_{FF}=c\,\mathrm{Tr}\!\big(\lambda^{3}\,\beta_{1}\,\dot{Q}_{F}^{\dagger}\,\beta_{2}\,\dot{Q}_{F}\big)does not rely on takingβa†=−βa\beta_{a}^{\dagger}=-\beta_{a}individually. More generally, assumeβa†=ηa​βa,ηa∈{+1,−1},a=1,2,\beta_{a}^{\dagger}=\eta_{a}\,\beta_{a},\qquad\eta_{a}\in\{+1,-1\},\qquad a=1,2,

withε​(βa)=1\varepsilon(\beta_{a})=1and the standard GTD involution(A​B)†=B†​A†(AB)^{\dagger}=B^{\dagger}A^{\dagger}.
ThenℋF​F†\displaystyle\mathcal{H}_{FF}^{\dagger}=c​λ3​Tr​((β1​Q˙F†​β2​Q˙F)†)=c​λ3​η1​η2​Tr​(Q˙F†​β2​Q˙F​β1)\displaystyle=c\,\lambda^{3}\,\mathrm{Tr}\!\Big((\beta_{1}\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F})^{\dagger}\Big)=c\,\lambda^{3}\,\eta_{1}\eta_{2}\,\mathrm{Tr}\!\Big(\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F}\beta_{1}\Big)=−c​λ3​η1​η2​Tr​(β1​Q˙F†​β2​Q˙F)=−(η1​η2)​ℋF​F,\displaystyle=-\,c\,\lambda^{3}\,\eta_{1}\eta_{2}\,\mathrm{Tr}\!\Big(\beta_{1}\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F}\Big)=-(\eta_{1}\eta_{2})\,\mathcal{H}_{FF},

where the minus sign arises from graded cyclicity when moving the odd factorβ1\beta_{1}past the odd productQ˙F†​β2​Q˙F\dot{Q}_{F}^{\dagger}\beta_{2}\dot{Q}_{F}.
HenceℋF​F\mathcal{H}_{FF}is purely anti-self-adjoint wheneverη1​η2=+1\eta_{1}\eta_{2}=+1(i.e. bothβ1,β2\beta_{1},\beta_{2}are self-adjoint, or both are anti-self-adjoint).
In particular, the choiceβ1†=β1\beta_{1}^{\dagger}=\beta_{1}andβ2†=β2\beta_{2}^{\dagger}=\beta_{2}yields the same
ASA fermionic term (and thus the same collapse channel) as the choiceβa†=−βa\beta_{a}^{\dagger}=-\beta_{a}.

## 5Interpretation for spontaneous localization

In trace dynamics, coarse-graining around statistical equilibrium yields two distinct regimes:
(i) if the Hamiltonian is effectively self-adjoint, one recovers emergent unitary quantum dynamics;
(ii) if the anti-self-adjoint component is significant, coarse-graining yields effective nonunitary
(stochastic) dynamics with spontaneous localization[3].

The computation above provides a structural mechanism for “fermion-only collapse” in GTD:
- •

The purely bosonic HamiltonianℋB​B\mathcal{H}_{BB}is self-adjoint and thus does not generate ASA-driven
collapse by itself.
- •

The fermionic sector carries an intrinsic anti-self-adjoint termℋF​F\mathcal{H}_{FF}, present precisely becauseβ1\beta_{1}andβ2\beta_{2}are unequal odd Grassmann elements inserted to make the unified trace Lagrangian bosonic.

Therefore, in regimes where ASA effects drive localization, the fundamental collapse channel is
naturally associated with fermionic degrees of freedom. Bosonic fields can still become classicalindirectly, because in the STM-atom picture an STM atom consists of a fermion together with its
associated bosonic fields, so localization of the fermionic degrees forces classicality of the
associated bosonic sector through correlations/entanglement, without requiring independent bosonic collapse.

## 6Conclusions

Starting from the unified STM-atom GTD trace Lagrangian, we computed the trace Hamiltonian via
trace-derivative canonical momenta, with bosonic and fermionic variations treated separately.
We found:
- 1.

The trace Hamiltonian equals the trace Lagrangian (Bateman-type cross-kinetic structure),
but it need not be self-adjoint becauseQ1Q_{1}andQ2Q_{2}are inequivalent.
- 2.

The purely bosonic contributionℋB​B\mathcal{H}_{BB}is self-adjoint.
- 3.

Assuming natural adjoint properties for the odd Grassmann elementsβ1,β2\beta_{1},\beta_{2},
the fermionic contributionℋF​F\mathcal{H}_{FF}is purely anti-self-adjoint, providing an explicit ASA component
of the Hamiltonian that vanishes in the bosonic subsector.

This provides a first-principles explanation, within GTD, for why spontaneous localization acts
fundamentally on fermionic degrees of freedom and not on bosonic degrees of freedom.

## Outlook.

The next steps are to connect the magnitude ofℋF​F\mathcal{H}_{FF}(and fluctuations about equilibrium) to
collapse phenomenology (rates, noise kernels, and effective CSL parameters), and to embed the analysis
into the multi-STM-atom setting where entanglement and interactions become operative.

## References
- [1]Tejinder P. Singh.Trace dynamics, octonions and unification: Ane8×e8e_{8}\times e_{8}theory of unification.Journal of Physics: Conference Series, 2912(1):012009, 2024 arXiv:2501.18139 [physics.gen-ph].Contribution to ISQS-28.
- [2]S. L. Adler.Quantum theory as an emergent phenomenon: The statistical mechanics of matrix models as the precursor of quantum field theory.Cambridge University Press, 2004.
- [3]Kartik Kakade, Avnish Singh, and Tejinder P. Singh.Spontaneous localisation from a coarse-grained deterministic and non-unitary dynamics.Physics Letters A, 490:129191, 2023 arXiv:2305.06706 [quant-ph].
- [4]Tejinder P. Singh.Space-time from Collapse of the Wave-function.Z. Naturforsch. A, 74(2):147–152, 2019 arXiv:1809.03441 [gr-qc].
- [5]G. C. Ghirardi, A. Rimini, and T. Weber.Unified dynamics for microscopic and macroscopic systems.Phys. Rev. D, 34:470–491, Jul 1986.
- [6]Gian Carlo Ghirardi, Philip Pearle, and Alberto Rimini.Markov processes in hilbert space and continuous spontaneous localization of systems of identical particles.Phys. Rev. A, 42:78–89, Jul 1990.
- [7]L. Diósi.Models for universal reduction of macroscopic quantum fluctuations.Phys. Rev. A, 40:1165–1174, Aug 1989.
- [8]Angelo Bassi and GianCarlo Ghirardi.Dynamical reduction models.Phys. Rept., 379:257, 2003.
- [9]Matteo Carlesso, Sandro Donadi, Luca Ferialdi, Mauro Paternostro, Hendrik Ulbricht, and Angelo Bassi.Present status and future challenges of non-interferometric tests of collapse models.Nature Physics, 18(3):243–250, 2022.
- [10]Palemkota Maithresh and Tejinder P. Singh.Proposal for a New Quantum Theory of Gravity III: Equations for Quantum Gravity, and the Origin of Spontaneous Localisation.Z. Naturforsch. A, 75(2):143–154, 2020 arXiv:1908.04309 [gr-qc].
