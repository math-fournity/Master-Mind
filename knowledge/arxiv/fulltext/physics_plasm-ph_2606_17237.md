# Time-dependent Trapped Plasmas: Nonlinear Dynamics, Symmetries and Invariants

**arXiv ID**: 2606.17237v1
**Authors**: Thonimar V. Alencar, Luiz Gustavo Ferreira Soares, Ronaldo Thibes
**Published**: 2026-06-15
**Categories**: physics.plasm-ph, math-ph
**HTML URL**: https://arxiv.org/html/2606.17237v1

## Abstract

We investigate the nonlinear dynamics of a single-component plasma confined in a time-dependent harmonic trap regarding aspects of symmetry and invariant functions. The system is described as a fluid in an isentropic adiabatic regime by a system of partial differential equations. A convenient change of variables, with a Gaussian ansatz for the number density distribution, allows a consistent mathematical description in terms of ordinary differential equations, from which we follow up with an analysis concerning the corresponding differential operators algebraic structure and Noether symmetries in specific physical regimes. For each studied case, proper invariants are identified. The obtained conserved quantities capture an interplay between the internal plasma dynamics and the time modulation of the trap, resulting in a sharp restriction for the system evolution.

## Full Text

Time-dependent Trapped Plasmas: Nonlinear Dynamics, Symmetries and Invariants

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2606.17237v1 [physics.plasm-ph] 15 Jun 2026

## Time-dependent Trapped Plasmas: Nonlinear Dynamics, Symmetries and InvariantsThonimar V. AlencarGrupo de Física Teórica e Computacional, Departamento de Ciências Naturais, CEUNES, Universidade Federal do Espírito Santo (UFES), Rodovia Governador Mário Covas, Km 60, São Mateus, 29932-540, ES, BrasilLuiz Gustavo Ferreira SoaresGrupo de Física Teórica e Computacional, Departamento de Ciências Naturais, CEUNES, Universidade Federal do Espírito Santo (UFES), Rodovia Governador Mário Covas, Km 60, São Mateus, 29932-540, ES, BrasilRonaldo ThibesDepartamento de Ciências Exatas e Naturais,
Universidade Estadual do Sudoeste da Bahia,
45700-000, Itapetinga BA, Brazil

## Abstract

We investigate the nonlinear dynamics of a single-component plasma confined in a time-dependent harmonic trap regarding aspects of symmetry and invariant functions. The system is described as a fluid in an isentropic adiabatic regime by a system of partial differential equations. A convenient change of variables, with a Gaussian ansatz for the number density distribution, allows a consistent mathematical description in terms of ordinary
differential equations, from which we follow up with an analysis concerning the corresponding differential operators algebraic structure and Noether symmetries in specific physical regimes. For each studied case, proper invariants
are identified. The obtained conserved quantities capture
an interplay between the internal plasma dynamics and the
time modulation of the trap,
resulting in
a sharp restriction for the system evolution.

## IIntroduction

Nonlinear dynamical systems have been spreading throughout physics and science in general for more than a couple of centuries.
Their mathematical structures and symmetries still pose countless quest challenges in present-day mathematics, physics and mathematical-physics[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,20].
In particular, in modern times, exact symmetries and controlled symmetry violations have been playing key roles concerning both their proper fundamental structures as well as specific consequences and applications. For that matter, we may mention instances of gauge[6,7,8], quantum[9,10,11,12], Galilean[13,14,15,16], Lorentz[16,17,18], conformal/dual[19,21,20]and many others perfectly realized or broken controlled symmetries in dynamical systems throughout contemporary physics. Of special importance for the present work, Lie and Noether symmetries[22,23,24,25]play a distinct role, allowing for the characterization and classification of dynamical systems and leading to conserved or invariant quantities.
Coming closer to our point, the use of symmetry methods in the physics of plasmas, Bose-Einstein condensates and related systems has produced important recent breakthrough results[26,27,28,29], promoting an approximation between distinct fields of mathematics and physics, while inviting new interdisciplinary collaborative works. Besides their intrinsic beauty, the identification of conserved quantities in such systems has practical importance, which can lead to technological applications.

Building on and extending previous works[29,30,31], we consider a quasi-one-dimensional single-component plasma, trapped by a time-dependent confining potential, described by a system of partial differential equations (pde). The problem can be formulated in a variational Lagrangian framework allowing the consideration of a simplifying realistic ansatz for the particle number density, after which the original pde system decouples into a pair of ordinary differential equations concerning the center-of-mass and spreading width modes. Turning to phase space, we reduce the order of the evolution equations, obtain the corresponding differential operator vector fields, and proceed to their algebraic analysis. By splitting the effective Lagrangian into two independent parts and considering cases of physical interest, namely thermal and cold plasmas, we obtain three invariant functions.
The latter correspond to conserved quantities configuring restrictions on plasma dynamical evolution through the confining trap’s time-modulation.

After this brief Introduction, we start our technical discussion in the remaining article with a presentation organized as follows. In Sec. II, we present the plasma model as described by a system of three coupled pdes plus a constitutive state equation and show how a convenient Gaussian ansatz for the particle number density leads to simpler ordinary differential equations. In Sec III, after the introduction of proper auxiliary variables, the differential operators commutator algebra associated with the first order odes is investigated.
The search for symmetries and conserved quantities is reserved for Sec. IV, in which we split the Lagrangian into two independent parts corresponding to the plasma center of mass and spreading width. Still in Sec. IV, by applying Noether’s invariance condition, we find the necessary odes to produce invariant quantities associated to
the remaining degrees of freedom in relevant physical regimes. We end in Sec. V with our final remarks and conclusion.

## IIThe Plasma Model

The timettevolution of a one-dimensional single-component plasma, composed of constituent particles of massmmand chargeeemoving along a linear directionzz, can be described in terms of its linear corpuscle number densityn​(z,t)n(z,t), velocity fieldv​(z,t)v(z,t), and self-consistent potentialϕ​(z,t)\phi(z,t). We consider the model recently discussed in[29], in which those three real functions are interrelated through the pde system∂n∂t+∂∂z​(n​v)\displaystyle\frac{\partial n}{\partial t}+\frac{\partial}{\partial z}(nv)=\displaystyle=0,\displaystyle 0\,,(1)∂v∂t+v​∂v∂z+Σ⟂m​n​∂p∂z+em​∂ϕ∂z\displaystyle\frac{\partial v}{\partial t}+v\frac{\partial v}{\partial z}+\frac{\Sigma_{\perp}}{mn}\frac{\partial p}{\partial z}{+}\frac{e}{m}\frac{\partial\phi}{\partial z}=\displaystyle=−1m​∂∂z​Vc​(z,t),\displaystyle-\frac{1}{m}\frac{\partial}{\partial z}V_{c}(z,t)\,,(2)∂2ϕ∂z2+e​nε0​Σ⟂\displaystyle\frac{\partial^{2}\phi}{\partial z^{2}}{+}\frac{en}{\varepsilon_{0}\Sigma_{\perp}}=\displaystyle=0,\displaystyle 0\,,(3)

complemented by the isentropic equation of statep​Σ⟂=n0​kB​T0​(nn0)3,p\Sigma_{\perp}=n_{0}k_{B}T_{0}\left(\frac{n}{n_{0}}\right)^{3}\,,(4)

in whichϵ0\epsilon_{0}andkBk_{B}represent physical universal constants,n0n_{0}andT0T_{0}fixed reference values,Σ⟂\Sigma_{\perp}denotes the surface area perpendicular to thezzdirection andVc​(z,t)V_{c}(z,t)stands for a given control potential function. The last four equations form a closed system. For an adiabatic cooling regime, common in many relevant realistic models[32,33],
we consider a slow-time-dependent harmonic potentialVc=m​ω2​(t)​z22,V_{c}=\frac{m\omega^{2}(t)z^{2}}{2}\,,(5)

with a time-decreasing frequencyω​(t)=ω0(1+Ω​t)β,\omega(t)=\frac{\omega_{0}}{(1+\Omega t)^{\beta}}\,,(6)

for positive constantsω0\omega_{0},Ω\Omegaandβ≤1\beta\leq 1. We also requireβ​Ω≪ω0\beta\Omega\ll\omega_{0}, leading to|ω˙|≪ω2|\dot{\omega}|\ll\omega^{2},
ensuring a slowly varying energy regime. A proper discussion of the physics involved in (1)-(3) can be found in[29,30].

As a mathematical model, the pde system (1)-(3) can be obtained from a variational principle. In fact, we may define an action functional𝒮​[n,ϕ,θ]\displaystyle{\cal S}[n,\phi,\theta]=\displaystyle=∫dtdz{m​n2(∂θ∂z)2+mn∂θ∂t+n(Vc+eϕ)\displaystyle\int dt\,dz\,\bigg\{\frac{mn}{2}\bigg(\frac{\partial\theta}{\partial z}\bigg)^{2}+mn\frac{\partial\theta}{\partial t}+n(V_{c}{+}e\phi)(7)−ϵ0​Σ⟂2(∂ϕ∂z)2+Σ⟂∫dn∫d​pn},\displaystyle-\frac{\epsilon_{0}\Sigma_{\perp}}{2}\bigg(\frac{\partial\phi}{\partial z}\bigg)^{2}+\Sigma_{\perp}\int dn\int\frac{dp}{n}\bigg\}\,,

in terms of the three two-variable real functionsn​(z,t),ϕ​(z,t),θ​(z,t),n(z,t),\penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \phi(z,t),\penalty 10000\ \penalty 10000\ \penalty 10000\ \penalty 10000\ \theta(z,t)\,,(8)

withn​(z,t)n(z,t)andϕ​(z,t)\phi(z,t)as before, andθ​(z,t)\theta(z,t)satisfyingv=∂θ/∂z{v}=\partial\theta/\partial z, demanding its stationarity with respect to first order functional variations in (8). Then, taking (4) into account, the corresponding Euler-Lagrange field equations lead to the system of partial differential equations (1)-(3).

In most situations of physical interest, the plasma linear density follows a Gaussian distribution along thezz-direction, with time-dependent mean and variance. Hence, we consider a collective behaviorn​(z,t)=N2​π​α​(t)​exp⁡(−(z−d​(t))22​α2​(t)),\displaystyle n(z,t)=\frac{N}{\sqrt{2\pi}\alpha(t)}\exp\bigg({-\frac{(z-d(t))^{2}}{2\alpha^{2}(t)}}\bigg)\,,(9)

leading to a dynamical description in terms of the two degrees of freedomd​(t)d(t)andα​(t)\alpha(t), characterizing the plasma distribution center and spreading as functions of time.
The normalization constantNNin (9)
represents the total number of constituent units for the confined plasma. Once (9) is given, on account of the original differential equations system (1)-(3), the plasma dynamics is characterized through the remaining two-variable real functions asϕ​(z,t)\displaystyle\phi(z,t)=\displaystyle=−e​Nϵ0​Σ⟂[α​(t)2​πexp(−(z−d​(t))22​α2​(t))\displaystyle{-}\frac{eN}{\epsilon_{0}\Sigma_{\perp}}\bigg[\frac{\alpha(t)}{\sqrt{2\pi}}\exp\bigg({-\frac{(z-d(t))^{2}}{2\alpha^{2}(t)}}\bigg)(10)+\displaystyle+z−d​(t)2erf(z−d​(t)2​α​(t))],\displaystyle\frac{z-d(t)}{2}{\mbox{erf}}\bigg({\frac{z-d(t)}{\sqrt{2}\alpha(t)}}\bigg)\bigg]\,,θ​(z,t)=α˙​(t)2​α​(t)​(z−d​(t))2+d˙​(z−d​(t)),\theta(z,t)=\frac{\dot{\alpha}(t)}{2\alpha(t)}(z-d(t))^{2}+\dot{d}(z-d(t))\,,(11)

andv​(z,t)=α˙​(t)α​(t)​(z−d​(t))+d˙.v(z,t)=\frac{\dot{\alpha}(t)}{\alpha(t)}(z-d(t))+\dot{d}\,.(12)

In this manner, the original problem of solving the pde system (1-3) has been conveyed to finding the two time-dependent functionsd​(t)d(t)andα​(t)\alpha(t).

In order to derive the dynamical behavior of the time-dependent coordinates, we may integrate out thezzspace-dependence in the action functional (7) to obtain an effective Lagrangian per unit mass and particle number, defined asL​(d,α,d˙,α˙)≡−1m​N​∫ℒ​𝑑z,L(d,\alpha,\dot{d},\dot{\alpha})\equiv-\frac{1}{mN}\int\mathcal{L}dz\,,(13)

withℒ\cal Lcharacterized by the integrand of (7). In this fashion, using
equations (9), (10) and (11), and performing the correspondingzz-integration in (13), we obtainL​(d,α,d˙,α˙)=12​(d˙2+α˙2)−Ud−Uα,L(d,\alpha,\dot{d},\dot{\alpha})=\frac{1}{2}(\dot{d}^{2}+\dot{\alpha}^{2})-U_{d}-U_{\alpha}\,,(14)

with the two time-dependent effective potentialsUdU_{d}andUαU_{\alpha}written asUd≡ω2​(t)2​d2U_{d}\equiv\frac{\omega^{2}(t)}{2}d^{2}(15)

andUα≡ω2​(t)2​α2+a2​α2−b​α,U_{\alpha}\equiv\frac{\omega^{2}(t)}{2}\alpha^{2}+\frac{a}{2\alpha^{2}}-b\alpha\,,(16)

in terms of the parametersa≡kB​T0​N2/(2​3​π​m​n02)a\equiv{k_{B}T_{0}N^{2}}/({2\sqrt{3}\pi mn_{0}^{2}})(17)

andb≡N​e2/(2​π​ϵ0​m​Σ⟂).b\equiv{Ne^{2}}/(2\sqrt{\pi}\epsilon_{0}m\Sigma_{\perp})\,.(18)

The effective potentials aboveUdU_{d}andUαU_{\alpha}correspond, respectively, to the system’s dipole center-of-mass and spreading width oscillating modes, with the constants (17) and (18) characterizing thermal and electric effects. The external time-dependent frequencyω​(t)\omega(t)present in equations (15) and (16) controls the harmonic confinement as given by (6).

Associated with (14), we have the two non-autonomous ordinary differential equationsd¨+ω​(t)​d=0\ddot{d}+\omega(t)d=0(19)

andα¨+ω2​(t)​α−aα3=b.\ddot{\alpha}+\omega^{2}(t)\alpha-\frac{a}{\alpha^{3}}=b\,.(20)

The first one, equation (19), corresponds to a time-dependent harmonic oscillator and has been extensively investigated in the literature[34,35,36,37,38,39,40], while (20) can be understood as a generalized or forced Pinney equation[41]due to the presence of the constant termbbin its right hand side.

We are interested in the subjacent plasma dynamics described by the odes (19) and (20),
whose analytical behavior, differential operator structures, symmetries, and invariants we discuss and contextualize in the remaining sections.

## IIIDifferential Operators Algebra

In this section, we study the differential operator commutator structure associated with the plasma dynamics described by odes (19) and (20). As is well-known, given a system of second-order ordinary differential equations, by introducing auxiliary intermediate variables, it can be reduced to first-order, being written asd​xrd​t=yr​(x,t),x=(xr),r=1,…,n,\frac{dx^{r}}{dt}=y^{r}(x,t)\,,\quad x=(x^{r})\,,\quad\quad r=1,\dots,n\,,(21)

for specific functionsyr​(x,t)y^{r}(x,t)and a fixedn∈ℕn\in\mathbb{N}. Once cast in the form (21), we can associate it with the vector field𝐗=∑r=1nyr​(x,t)​∂∂xr.\mathbf{X}=\sum_{r=1}^{n}y^{r}(x,t)\frac{\partial}{\partial x^{r}}\,.(22)

We say that𝐗\mathbf{X}admits a superposition rule in terms of a set ofmmlinearly independent (li) operatorsXiX_{i},i=1,…,mi=1,\dots,m, withm∈ℕm\in\mathbb{N}, when it can be locally written as𝐗​(x,t)=∑i=1mpi​(t)​Xi​(x),\mathbf{X}(x,t)=\sum_{i=1}^{m}p^{i}(t)X_{i}(x)\,,(23)

for somepi​(t)p^{i}(t).
The differential operatorsXiX_{i},i=1,…,mi=1,\dots,m, possibly li completed withXjX_{j},j=m+1,…,dj=m+1,\dots,d,d≥md\geq m, generate add-dimensional Lie algebraΛd\Lambda^{d}if there existci​jkc_{ij}^{\,\,\,\,k},i,j,k=1,…,di,j,k=1,\dots,d, such that[Xi,Xj]=∑k=1dci​jk​Xk,[X_{i},X_{j}]=\sum_{k=1}^{d}c_{ij}^{\,\,\,\,k}X_{k}\,,(24)

with the square bracket denoting the usual commutator, i.e.,[Xi,Xj]≡Xi​Xj−Xj​Xi.[X_{i},X_{j}]\equiv X_{i}\,X_{j}-X_{j}\,X_{i}\,.(25)

In the following, we investigate the vector field𝐗\mathbf{X}and the corresponding superposition rule structure for specific cases of (19) and (20) of physical interest.

## III.1Center of Mass

The plasma center of mass motion is described by the non-autonomous linear homogeneous ordinary differential equation (ode) (19), with an external time-dependent frequencyω​(t)\omega(t)given by (6). Introducing the auxiliary variablevv, by demandingv=d˙v=\dot{d}, the second-order ode (19) can be rewritten as{d˙=v,v˙=−ω​(t)2​d,\begin{cases}\dot{d}=v\,,\\
\dot{v}=-\omega(t)^{2}d\,,\end{cases}(26)

with the associated vector field𝐗​(d,v,t)=v​∂∂d−ω​(t)2​d​∂∂v.\mathbf{X}(d,v,t)=v\frac{\partial}{\partial d}-\omega(t)^{2}d\frac{\partial}{\partial v}\,.(27)

This is clearly in the form (23)
withp1=−ω2​(t)p_{1}=-\omega^{2}(t),p2=1p_{2}=1, andX1≡d​∂∂v,X2≡v​∂∂d.X_{1}\equiv d\frac{\partial}{\partial v}\,,\,\,\,\,X_{2}\equiv v\frac{\partial}{\partial d}\,.(28)

The two operators in (28) above satisfy the commutation relation[X1,X2]=d​∂∂v​(v​∂∂d)−v​∂∂d​(d​∂∂v)=X3,[X_{1},X_{2}]=d\frac{\partial}{\partial v}\bigg(v\frac{\partial}{\partial d}\bigg)-v\frac{\partial}{\partial d}\bigg(d\frac{\partial}{\partial v}\bigg)=X_{3}\,,(29)

where we have definedX3≡d​∂∂d−v​∂∂v.X_{3}\equiv d\frac{\partial}{\partial d}-v\frac{\partial}{\partial v}\,.(30)

Furthermore, we have[X1,X3]=d​∂∂v​[(d​∂∂d−v​∂∂v)]−(d​∂∂d−v​∂∂v)​(d​∂∂v)=−2​X1,[X_{1},X_{3}]=d\frac{\partial}{\partial v}\bigg[\bigg(d\frac{\partial}{\partial d}-v\frac{\partial}{\partial v}\bigg)\bigg]-\bigg(d\frac{\partial}{\partial d}-v\frac{\partial}{\partial v}\bigg)\bigg(d\frac{\partial}{\partial v}\bigg)=-2X_{1}\,,(31)

and[X2,X3]=v​∂∂d​[(d​∂∂d−v​∂∂v)]−(d​∂∂d−v​∂∂v)​(v​∂∂d)=2​X2.[X_{2},X_{3}]=v\frac{\partial}{\partial d}\bigg[\bigg(d\frac{\partial}{\partial d}-v\frac{\partial}{\partial v}\bigg)\bigg]-\bigg(d\frac{\partial}{\partial d}-v\frac{\partial}{\partial v}\bigg)\bigg(v\frac{\partial}{\partial d}\bigg)=2X_{2}\,.(32)

From these results, we see that the first-order system (26) closes a three dimensional Lie algebra (24) with non-null structure constantsc123=1,c131=−2,c232=2.c_{12}^{\,\,\,\,\,\,3}=1\,,\quad c_{13}^{\,\,\,\,\,\,1}=-2\,,\quad c_{23}^{\,\,\,\,\,\,2}=2\,.(33)

## III.2Spreading Width

Concerning the plasma spreading widthα​(t)\alpha(t)introduced in (9) as a standard deviation for the particle density distribution, we split our analysis into the particular cases of thermal and cold plasmas, respectively described byb=0b=0anda=0a=0.

## III.2.1Thermal Plasma

In this case, as we haveb=0b=0anda≠0a\neq 0, the second-order ode (20) is non-linear and can be rewritten in first order as{α˙=v,v˙=−ω​(t)2​α+aα3,\begin{cases}\dot{\alpha}=v\,,\\
\displaystyle\dot{v}=-\omega(t)^{2}\alpha+\frac{a}{\alpha^{3}}\,,\end{cases}(34)

withvvrepresenting an auxiliary variable. We associate to (34) the vector field𝐍=v​∂∂α−(ω​(t)2​α−aα3)​∂∂v,\mathbf{N}=v\frac{\partial}{\partial\alpha}-\bigg(\omega(t)^{2}\alpha-\frac{a}{\alpha^{3}}\bigg)\frac{\partial}{\partial v}\,,(35)

which is of the form (23)
withp1=−ω2​(t)p_{1}=-\omega^{2}(t),p2=1p_{2}=1, andN1≡α​∂∂v,N2≡aα3​∂∂v+v​∂∂α.N_{1}\equiv\alpha\frac{\partial}{\partial v}\,,\,\,\,N_{2}\equiv\frac{a}{\alpha^{3}}\frac{\partial}{\partial v}+v\frac{\partial}{\partial\alpha}\,.(36)

For the commutation relations, definingN3≡α​∂∂α−v​∂∂v,N_{3}\equiv\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\,,(37)

we have[N1,N2]=α​∂∂v​(aα3​∂∂v+v​∂∂α)−(aα3​∂∂v+v​∂∂α)​α​∂∂v=N3,[N_{1},N_{2}]=\alpha\frac{\partial}{\partial v}\bigg(\frac{a}{\alpha^{3}}\frac{\partial}{\partial v}+v\frac{\partial}{\partial\alpha}\bigg)-\bigg(\frac{a}{\alpha^{3}}\frac{\partial}{\partial v}+v\frac{\partial}{\partial\alpha}\bigg)\alpha\frac{\partial}{\partial v}=N_{3}\,,(38)[N1,N3]=α​∂∂v​[(α​∂∂α−v​∂∂v)]−(α​∂∂α−v​∂∂v)​(α​∂∂v)=−2​N1,[N_{1},N_{3}]=\alpha\frac{\partial}{\partial v}\bigg[\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)\bigg]-\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)\bigg(\alpha\frac{\partial}{\partial v}\bigg)=-2N_{1}\,,(39)

and[N2,N3]=(aα3​∂∂v+v​∂∂α)​(α​∂∂α−v​∂∂v)−(α​∂∂α−v​∂∂v)​(aα3​∂∂v+v​∂∂α)=2​N2.[N_{2},N_{3}]=\bigg(\frac{a}{\alpha^{3}}\frac{\partial}{\partial v}+v\frac{\partial}{\partial\alpha}\bigg)\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)-\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)\bigg(\frac{a}{\alpha^{3}}\frac{\partial}{\partial v}+v\frac{\partial}{\partial\alpha}\bigg)=2N_{2}\,.(40)

Thus, the commutation relations above for the non-autonomous non-linear system (34) also characterize a Lie algebra with structure constants (33).

## III.2.2Cold Plasma

In this second case, consideringa=0a=0andb≠0b\neq 0, we may rewrite (20) in first order as{α˙=vv˙=−ω​(t)2​α+b\begin{cases}\dot{\alpha}=v\\
\dot{v}=-\omega(t)^{2}\alpha+b\end{cases}(41)

with an associated vector field𝐌=v​∂∂α−(ω​(t)2​α−b)​∂∂v.\mathbf{M}=v\frac{\partial}{\partial\alpha}-(\omega(t)^{2}\alpha-b)\frac{\partial}{\partial v}\,.(42)

Again,vvis an auxiliary variable connecting the two first-order equations (41) that ensure equivalence to (20).
DefiningM1=α​∂∂v,M2=v​∂∂x,M4=b​∂∂v.\displaystyle M_{1}=\alpha\frac{\partial}{\partial v}\,,\,\,\,M_{2}=v\frac{\partial}{\partial x}\,,\,\,\,\,\,M_{4}=b\frac{\partial}{\partial v}\,.(43)

we may rewrite (42) as𝐌=M2−ω​(t)2​M1+M4,\mathbf{M}=M_{2}-\omega(t)^{2}M_{1}+M_{4}\,,(44)

which is in the form (23) withp1=−ω2​(t)p_{1}=-\omega^{2}(t),p2=p4=1p_{2}=p_{4}=1, evincing a superposition rule admission.
By defining furtherM3≡α​∂∂α−v​∂∂v,M_{3}\equiv\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\,,(45)M5≡b​∂∂α,M_{5}\equiv b\frac{\partial}{\partial\alpha}\,,(46)

it is straightforward to obtain the non-null commutation relations[M1,M2]=α​∂∂v​(v​∂∂α)−v​∂∂α​(α​∂∂v)=M3,[M_{1},M_{2}]=\alpha\frac{\partial}{\partial v}\bigg(v\frac{\partial}{\partial\alpha}\bigg)-v\frac{\partial}{\partial\alpha}\bigg(\alpha\frac{\partial}{\partial v}\bigg)=M_{3}\,,(47)[M1,M3]=α​∂∂v​[(α​∂∂α−v​∂∂v)]−(α​∂∂α−v​∂∂v)​(α​∂∂v)=−2​M1,[M_{1},M_{3}]=\alpha\frac{\partial}{\partial v}\bigg[\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)\bigg]-\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)\bigg(\alpha\frac{\partial}{\partial v}\bigg)=-2M_{1}\,,(48)[M2,M3]=v​∂∂α​[(α​∂∂α−v​∂∂v)]−(α​∂∂α−v​∂∂v)​(v​∂∂α)=2​M2.[M_{2},M_{3}]=v\frac{\partial}{\partial\alpha}\bigg[\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)\bigg]-\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)\bigg(v\frac{\partial}{\partial\alpha}\bigg)=2M_{2}\,.(49)[M4,M2]=b​∂∂v​(v​∂∂α)−v​∂∂α​(b​∂∂v)=b​∂∂α=M5,[M_{4},M_{2}]=b\frac{\partial}{\partial v}\bigg(v\frac{\partial}{\partial\alpha}\bigg)-v\frac{\partial}{\partial\alpha}\bigg(b\frac{\partial}{\partial v}\bigg)=b\frac{\partial}{\partial\alpha}=M_{5}\,,(50)[M4,M3]=b​∂∂v​(α​∂∂α−v​∂∂v)−(α​∂∂α−v​∂∂v)​(b​∂∂v)=−M4.[M_{4},M_{3}]=b\frac{\partial}{\partial v}\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)-\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)\bigg(b\frac{\partial}{\partial v}\bigg)=-{M_{4}}\,.(51)[M5,M1]=b​∂∂α​(α​∂∂v)−α​∂∂v​(b​∂∂α)=M4,[M_{5},M_{1}]=b\frac{\partial}{\partial\alpha}\bigg(\alpha\frac{\partial}{\partial v}\bigg)-\alpha\frac{\partial}{\partial v}\bigg(b\frac{\partial}{\partial\alpha}\bigg)=M_{4}\,,(52)

and[M5,M3]=b​∂∂α​(α​∂∂α−v​∂∂v)−(α​∂∂α−v​∂∂v)​(b​∂∂α)=M5.[M_{5},M_{3}]=b\frac{\partial}{\partial\alpha}\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)-\bigg(\alpha\frac{\partial}{\partial\alpha}-v\frac{\partial}{\partial v}\bigg)\bigg(b\frac{\partial}{\partial\alpha}\bigg)={M_{5}}\,.(53)

Hence, the previous results can be summarized in the form (24) withc123=1,c131=−2,c154=−1,c232=2,c245=−1,c344=1,c355=−1,\begin{gathered}c_{12}^{\,\,\,\,\,\,3}=1\,,\,\,\,c_{13}^{\,\,\,\,\,\,1}=-2\,,\,\,\,c_{15}^{\,\,\,\,\,\,4}=-1\,,\,\,\,c_{23}^{\,\,\,\,\,\,2}=2\,,\,\,\,\\
c_{24}^{\,\,\,\,\,\,5}=-1\,,\,\,\,c_{34}^{\,\,\,\,\,\,4}=1\,,\,\,\,c_{35}^{\,\,\,\,\,\,5}=-1\,,\,\,\,\end{gathered}(54)

showing that, in the cold plasma case, the differential operators close a5−5-dimensional Lie algebra.

## IVNOETHER INVARIANTS

Since the two relevant variablesddandα\alphaare not coupled to each other in (14), it is possible to split the Lagrangian function asL​(d,α,d˙,α˙)=L1​(d,d˙)+L2​(α,α˙),L(d,\alpha,\dot{d},\dot{\alpha})=L_{1}(d,\dot{d})+L_{2}(\alpha,\dot{\alpha})\,,(55)

withL1​(d,d˙)=d˙22−UdandL2​(α,α˙)=α˙22−Uα,L_{1}(d,\dot{d})=\frac{\dot{d}^{2}}{2}-U_{d}\quad\mbox{and}\quad L_{2}(\alpha,\dot{\alpha})=\frac{\dot{\alpha}^{2}}{2}-U_{\alpha}\,,(56)

and, accordingly, look for conserved quantities associated with the symmetries of each separate constituent part.
As Noether has taught us in her beautiful theorems[42,43,44], invariance of the action under continuous transformations leads to conserved quantities.
Along that line, following a well-established standard route[28,36,45,46,47], we considerϵ\epsilon-parametrized transformations of the form{t⟶t′=t+ϵ​T​(x,t),x⟶x′=x+ϵ​η​(x,t),\begin{cases}t\penalty 10000\ \penalty 10000\ \longrightarrow\penalty 10000\ \penalty 10000\ t^{\prime}=t+\epsilon T(x,t)\,,\\
x\penalty 10000\ \penalty 10000\ \longrightarrow\penalty 10000\ \penalty 10000\ x^{\prime}=x+\epsilon\eta(x,t)\,,\end{cases}(57)

withx=d,αx=d\,,\alpha, and demand invariance of the action functionalS=∫𝑑t​L,S=\int dtL\,,(58)

withL=L1,L2L=L_{1}\,,L_{2}.
Associated with(57), we define the zero-order point symmetry generatorG[0]=T​∂∂t+η​∂∂xG^{[0]}=T\frac{\partial}{\partial t}+\eta\frac{\partial}{\partial x}(59)

and its corresponding first-order prolongation[23,24]G[1]=G[0]+(η˙−T˙​x˙)​∂∂x˙.G^{[1]}=G^{[0]}+(\dot{\eta}-\dot{T}\dot{x})\frac{\partial}{\partial\dot{x}}\,.(60)

The requirement of invariance of (58) under (57) leads to the existence of a functionF=F​(x,t)F=F(x,t)satisfying the Noether conditionG[1]​L+T˙​L=∂F∂t+x˙​∂F∂xG^{[1]}L+\dot{T}L=\frac{\partial F}{\partial t}+\dot{x}\frac{\partial F}{\partial x}(61)

and to the consequent time invariant (conserved quantity) combinationI=T​(x˙​∂L∂x˙−L)−η​∂L∂x˙+F.I=T\bigg(\dot{x}\frac{\partial L}{\partial\dot{x}}-L\bigg)-\eta\frac{\partial L}{\partial\dot{x}}+F\,.(62)

To proceed further,
similarly to the previous section, it is convenient to separate the symmetry analysis into specific cases of physical interest.

## IV.1Center of Mass

Concerning the center of mass mode, we first restrict our attention to transformations which do not affectα\alphaand apply (57) toL1L_{1}withx=dx=d. Imposing Noether’s symmetry condition (61), we obtainT=T​(t),η​(d,t)=T˙​(t)​d2−g​(t),T=T(t)\,,\quad\eta(d,t)=\frac{{\dot{T}}(t)d}{2}-g(t)\,,(63)

andF​(d,t)=T¨​d24−g˙​d,F(d,t)=\frac{\ddot{T}d^{2}}{4}-\dot{g}d\,,(64)

withg​(t)g(t)denoting a new time-dependent function that satisfiesg¨+ω2​(t)​g=0.\ddot{g}+{\omega}^{2}(t)g=0\,.(65)

As a further consequence of (61),TTmust also satisfyT˙˙˙+4​ω2​T˙+4​ω˙​ω​T=0.\dddot{T}+4\omega^{2}\dot{T}+4{\dot{\omega}}\omega T=0\,.(66)

This last equation may be further simplified by means of a change of variablesT=ρ2T=\rho^{2}allowing a time integration and consequent order reduction in terms of an integration constantkk, toρ¨+ω2​ρ=kρ3,\ddot{\rho}+\omega^{2}\rho=\frac{k}{\rho^{3}}\,,(67)

which is recognized as the famous Pinney111Equation (67) is also more properly known as the Ermakov-Milne-Pinney equation[41,48,49].nonlinear equation[50,51,52].
The complete symmetry group of (67) has been worked out by Nucci and Leach on[53].

Eventually, from (62) applied toL1L_{1}withx=dx=d,
we obtain an invariant quantity given byI=12​[T​d˙2−T˙​d˙​d+(T¨+2​ω2​T)​d22]+g​d˙−g˙​d,I=\frac{1}{2}\bigg[T\dot{d}^{2}-\dot{T}\dot{d}d+(\ddot{T}+2\omega^{2}T)\frac{d^{2}}{2}\bigg]+g\dot{d}-\dot{g}d\,\,,(68)

which, in terms of the auxiliary variableρ\rhosatisfying (67), can be rewritten asI=12​(ρ​d˙−ρ˙​d)2+k2​(dρ)2+g​d˙−g˙​d.I=\frac{1}{2}(\rho\dot{d}-\dot{\rho}d)^{2}+\frac{k}{2}\bigg(\frac{d}{\rho}\bigg)^{2}+g\dot{d}-\dot{g}d\,.(69)

Sinceggis any solution to (65), we may takeg=0g=0for simplicity and obtain a first conserved quantity associated with the center-of-mass modeI0I_{0}given byI0=12​(ρ​d˙−ρ˙​d)2+k2​(dρ)2.I_{0}=\frac{1}{2}(\rho\dot{d}-\dot{\rho}d)^{2}+\frac{k}{2}\bigg(\frac{d}{\rho}\bigg)^{2}\,.(70)

## IV.2Plasma’s spreading width

To next discuss the plasma spreading width modeα​(t)\alpha(t), we apply the transformation (57) withx=αx=\alphatoL2L_{2}, and the potential subdivides into the thermal and cold plasma cases.

## IV.2.1Thermal Plasma

With a null chargee=0e=0for the constituent particles, a thermal plasma is characterized byb=0b=0in the effective potential (16). For this physical realization, we look forL2L_{2}corresponding symmetries generated by (57) withx=αx=\alpha.
In this case, the Noether symmetry condition (59) leads toT=T​(t),η=T˙​α2,F=T¨​α24,T=T(t)\,,\quad\eta=\frac{\dot{T}\alpha}{2}\,,\quad F=\frac{\ddot{T}\alpha^{2}}{4}\,,(71)

withTTsatisfying the same previous third-order differential equation (66).

Hence, associated with the thermal plasma spreading width, using equation (62), we obtain the conserved quantityI=T2​(α˙2+ω2​α2+a​α−2)−T˙​α​α˙2+T¨​α24.I=\frac{T}{2}\left(\dot{\alpha}^{2}+\omega^{2}{\alpha}^{2}+a\alpha^{-2}\right)-\frac{\dot{T}\alpha\dot{\alpha}}{2}+\frac{\ddot{T}\alpha^{2}}{4}\,.(72)

With a change of variablesT=ρ2T=\rho^{2}, after a time integration introducing a constantkk, the invariant (72) can be reshaped asI1=12​(ρ​α˙−ρ˙​α)2+k2​(αρ)2+a2​(ρα)2,I_{1}=\frac{1}{2}(\rho\dot{\alpha}-\dot{\rho}\alpha)^{2}+\frac{k}{2}\bigg(\frac{\alpha}{\rho}\bigg)^{2}+\frac{a}{2}\bigg(\frac{\rho}{\alpha}\bigg)^{2}\,,(73)

withρ\rhostanding for a solution of the Pinney equation (67) with a correspondingkk. By using the equations of motion, it can be explicitly checked that the above quantity is conserved along the time evolution.

## IV.2.2Cold Plasma

Finally, we consider the cold plasma situation in which we havekB​T0=0k_{B}T_{0}=0, resulting ina=0a=0in (16). In this case, Noether’s symmetry condition forL2L_{2}under (61) leads toT=T​(t),η=T˙​α2−h​(t),F=T¨​α24−h˙​α+m​(t),T=T(t)\,,\quad\eta=\frac{\dot{T}\alpha}{2}-h(t)\,,\quad F=\frac{\ddot{T}\alpha^{2}}{4}-\dot{h}\alpha+m(t)\,,(74)

with the time-dependent functionsh​(t)h(t)andm​(t)m(t)satisfying the differential equationsh¨+ω2​h=−3​b​T˙2,m˙+b​h=0,\ddot{h}+{\omega}^{2}h=-\frac{3b\dot{T}}{{2}}\,,\quad\dot{m}+bh=0\,,(75)

andTTstands for a solution of (66).
The corresponding invariant, obtained from (62), readsI\displaystyle I=\displaystyle=12​(T​α˙2−T˙​α˙)​α+14​(T¨+2​ω2​T)​α2\displaystyle\frac{1}{2}\left(T\dot{\alpha}^{2}-\dot{T}\dot{\alpha}\right)\alpha+\frac{1}{4}\left(\ddot{T}+2\omega^{2}T\right){\alpha^{2}}(76)+h​α˙−h˙​α−b​α​T+m.\displaystyle+h\dot{\alpha}-\dot{h}\alpha-b\alpha T+m\,\,.

Similar to the previous cases, the transformation of variablesT=ρ2T=\rho^{2}allows for a first integration in terms of an integration constantkkwithρ\rhosatisfying the Pinney equation (67). In terms ofρ\rho, we can rewrite the above invariant asI2=12​(ρ​α˙−α​ρ˙)2+k2​(αρ)2−h˙​α+h​α˙−b​α​ρ2+m.I_{2}={\frac{1}{2}(\rho\dot{\alpha}-\alpha\dot{\rho})^{2}}+\frac{k}{2}\bigg(\frac{\alpha}{\rho}\bigg)^{2}-\dot{h}\alpha+h\dot{\alpha}-b\alpha\rho^{2}+m\,.(77)

Thus, we have found an invariant corresponding to the cold plasma which is conserved along the system time evolution.

## VConclusion

The mathematical structure of differential equations describing dynamical systems, particularly related to symmetries and invariants, can be successfully applied to hydrodynamic and thermodynamic systems. In this paper, we have seen an explicit example related to plasma dynamics. Starting from a pde model interrelating the relevant field variables describing a trapped one dimensional plasma under adiabatic evolution, we have shown that under some simplifying assumptions, the dynamics can be characterized by the time evolution of two time-dependent functions related to the plasma center-of-mass and spreading width through the mean variance of a Gaussian distribution for the linear particle density. This allowed us to study the symmetries of simpler Lagrangians leading to corresponding Noether invariants. We have also analyzed the algebraic aspects of the corresponding differential operators in terms of Lie algebras. This route could also have been used to investigate the associated invariants, leading to the same obtained invariants in an equivalent way. With the Lagrangians at hand, we have chosen to follow Noether’s more intuitive approach directly associated with the invariance of the action under a set of parametrized infinitesimal transformations. Further analysis concerning the mathematical structure of the ode system, as well as the relaxation of some of the simplifying assumptions for the pde systems are currently under analysis.

## Acknowledgements

R.T. gratefully acknowledges Prof Maria Clara Nucci for her two invited talks given at VI Ciclo de Seminários de Física em Itapetinga, which motivated a systematic follow up search for lost symmetries in Nature.

## References
- [1]J. E. Marsden and T. S. Ratiu,Introduction to Mechanics and Symmetry,
2nd ed. (Springer, New York, 1999).
- [2]N. Euler,Nonlinear Systems and their Remarkable Mathematical Structures:Volume 1 (CRC Press, 2020).
- [3]N. Euler and M. C. Nucci,Nonlinear Systems and their Remarkable Mathematical Structures:Volume 2 (CRC Press, 2020).
- [4]N. Euler and D. Zhang,Nonlinear Systems and their Remarkable Mathematical Structures:Volume 3 (Chapman & Hall, 2024).
- [5]S. G. Rajeev,Physics Through Symmetries(World Scientific, 2025).
- [6]M. Henneaux and C. Teitelboim,Quantization of gauge systems, Princeton University Press (1992).
- [7]G. ’t Hooft,Under the spell of the gauge principle,
Adv. Ser. Math. Phys.19(WSPC, 1994).
- [8]P. Berghofer, J. François, S. Friederich, H. Gomes, G. Hetzroni, A. Maas and R. Sondenheimer,Gauge Symmetries, Symmetry Breaking, and Gauge-Invariant Approaches, Cambridge University Press (2023).
- [9]S. P. Sorella,
J. Phys. A44, 135403 (2011).
- [10]A. Reshetnyak,
Int. J. Mod. Phys. A29, 1450184 (2014).
- [11]B. P. Mandal, S. K. Rai and R. Thibes,
EPL144, no.1, 14001 (2023).
- [12]B. P. Mandal, S. K. Rai and R. Thibes,
Nucl. Phys. B1023, 117306 (2026).
- [13]A. Saha,
Phys. Rev. D81, 125002 (2010).
- [14]D. Chernyavsky and D. Sorokin,
JHEP07, 156 (2019).
- [15]H. Belich, E. S. Santos and C. Valcarcel,
Eur. Phys. J. C85, no.3, 288 (2025).
- [16]C. Batlle, J. Gomis, S. Ray and J. Zanelli,
Phys. Rev. D99, no.6, 064015 (2019).
- [17]J. A. A. S. Reis, M. Schreck and R. Thibes,
“Alternative classical Lagrangians for the Standard-Model Extension,”
[arXiv:2603.06714 [hep-ph]] (2026).
- [18]W. Cesar e Silva, J. P. S. Melo and J. A. Helayël-Neto,
“Extending the Euler-Heisenberg action to include effects of local Lorentz-symmetry violating backgrounds,”
[arXiv:2603.20880 [hep-th]] (2026).
- [19]I. L. Shapiro,
Eur. Phys. J. Plus140, no.6, 534 (2025).
- [20]V. G. Krechet, V. B. Oshurko and I. V. Sinilshchikova,
Russ. Phys. J.57, no.9, 1195-1200 (2015).
- [21]P. Pasti, D. P. Sorokin and M. Tonin,
Phys. Rev. D52, R4277 (1995).
- [22]P. G. L. Leach and A. Paliathanasis,Noether’s Theorem and Symmetry, Symmetry Special Issue (2020).
- [23]P. J. Olver,Applications of Lie Groups to Differential Equations(Springer, New York, 1993).
- [24]G. W. Bluman and S. C. Anco,Symmetry and Integration Methods for Differential Equations(Springer, 2002).
- [25]B. J. Cantwell,Introduction to symmetry analysis, (Cambridge University Press, 2002).
- [26]F. Haas,
Phys. Rev. A65, 3, 033603 (2002).
- [27]H. Qin and R. C. Davidson,
Phys. Rev. ST Accel. Beams9, 054001 (2006).
- [28]F. Haas, Phys. Lett. A,482, 129034 (2023).
- [29]L. G. F. Soares, T. V. Alencar and R. Thibes,
Phys. Rev. E113, no.3, 035206 (2026).
- [30]L. G. F. Soares and F. Haas,
Phys. Plasmas27, no.6, 062307 (2020).
- [31]L. G. F. Soares and F. Haas,
Phys. Plasmas28, no.7, 074502 (2021).
- [32]G. Gabrielse, W. S. Kolthammer, R. McConnell, P. Richerme, R. Kalra, E. Novitski, D. Grzonka, W. Oelert, T. Sefzick and M. Zielinski,
D. Fitzakerley, M. C. George, E. A. Hessels, C. H. Storry, M. Weel, A. Müllers and J. Walz,
Phys. Rev. Lett.106, no.7, 073002 (2011),
- [33]G. Manfredi and P. Herviex, Phys. Rev. Lett,109, 255005 (2012).
- [34]H. R. Lewis, Jr,
Phys. Rev. Lett.18, no.13, 510 (1967),
- [35]H. R. Lewis,
J. Math. Phys.9, 1976 (1968).
- [36]M. Lutzky, Phys. Lett. A,68(1974).
- [37]P. G. L. Leach,
J. Math. Phys.18, 1902 (1977).
- [38]P. G. Leach,
J. Math. Phys.21, 300 (1980),
- [39]M. C. Bertin, B. M. Pimentel and J. A. Ramirez, J. Math. Phys.53, 4, 042104 (2012).
- [40]M. C. Bertin, J. R. Peleteiro and B. M. Pimentel, Braz. J. Phys.50, 5, 534 (2020).
- [41]E. Pinney, Proc. Amer. Math. Soc. 1, 681 (1950).
- [42]E. Noether, Nachrichten der Königlichen Gesellschaft der Wissenschaften zu Göttingen, 235 (1918).
- [43]Y. Kosmann-Schwarzbach,The Noether Theorems. Sources and Studies in the History of Mathematics and Physical Sciences(Springer, New York, NY, 2011).
- [44]A. K. Halder, A. Paliathanasis and P. G. L. Leach,
Symmetry10, no.12, 744 (2018).
- [45]J. Ray and J. L. Reid, J. Math. Phys.20, 2054,10(1979).
- [46]J. Ray and J. L. Reid, Phys. Rev. A,26, 2 1042, (1982).
- [47]W. Sarlet and F. Cantrijn, SIAM Rev.23, U6T-U9U (1981).
- [48]V. P. Ermakov,
Univ. Izv. Kiev20, 1 (1880)
[translated: Appl. Anal. Discrete Math.2, 123 (2008)].
- [49]W. E. Milne,
Phys. Rev.35, 863 (1930).
- [50]J. F. Carinẽna, J. Lucas and M. F. Ranãda,
SIGMA,4, 031, (2008).
- [51]J. F. Carinena, J. de Lucas and M. F. Ranada,Nonlinear superpositions and Ermakov systems, in
Differential Geometric Methods in Mechanics and Field Theory, pp.15–33, eds F. Cantrijn, M. Crampin and B. Langerock, Academia Press, 2007.
- [52]R. M. Morris and P. G. Leach,
Appl. Anal. Discrete Math.,11, 62 (2017).
- [53]M. C. Nucci and P. G. L. Leach, Journal of Nonlinear Mathematical Physics 12, 2, 305 (2005).

## 


- 


Major funding support from
