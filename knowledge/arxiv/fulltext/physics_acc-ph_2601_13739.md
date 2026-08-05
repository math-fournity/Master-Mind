# The Hamilton-Jacobi Equation and its Application to Nonlinear Beam Dynamics: Comparison of Approaches

**arXiv ID**: 2601.13739v1
**Authors**: Stephan I. Tzenov
**Published**: 2026-01-20
**Categories**: physics.acc-ph, nlin.SI, physics.plasm-ph
**Comments**: 9 pages, 5 figures
**HTML URL**: https://arxiv.org/html/2601.13739v1

## Abstract

The rarely used Hamilton-Jacobi equation has been utilized as an elegant way to find the trajectories of mechanical systems and to derive symplectic maps. Further, the exact solution in kick approximation of Hamilton's equations of motion in interaction representation is written as a generalized one-turn twist map.   One can imagine that the nonlinear kick comes first, followed by the one-period rotation along the machine circumference, or a second alternative in which the one-period rotation occurs before the kick. There is a difference in the result of solving Hamilton's equations between the two cases, which is expressed in obtaining a standard forward twist map in the first case, or alternatively a backward map in the second one. This nontrivial and intuitively unclear peculiarity is usually ignored/overlooked in practically all specialized references on the topic.   Finally, the statistical properties and the behavior of the density distribution of a particle beam in configuration space under the influence of an isolated sextupole have been studied.

## Full Text

The Hamilton-Jacobi Equation and its Application to Nonlinear Beam Dynamics: Comparison of Approaches
- 
- 
- 
- 
- 
- 
- 
- 
- 

## The Hamilton-Jacobi Equation and its Application to Nonlinear Beam Dynamics: Comparison of ApproachesStephan I. Tzenovtzenov@jinr.ruVeksler and Baldin Laboratory for High Energy Physics, Joint Institute for Nuclear Research, 6 Joliot-Curie Street, Dubna, Moscow Region, Russian Federation, 141980

## Abstract

The rarely used Hamilton-Jacobi equation has been utilized as an elegant way to find the trajectories of mechanical systems and to derive symplectic maps. Further, the exact solution in kick approximation of Hamilton’s equations of motion in interaction representation is written as a generalized one-turn twist map.

One can imagine that the nonlinear kick comes first, followed by the one-period rotation along the machine circumference, or a second alternative in which the one-period rotation occurs before the kick. There is a difference in the result of solving Hamilton’s equations between the two cases, which is expressed in obtaining a standard forward twist map in the first case, or alternatively a backward map in the second one. This nontrivial and intuitively unclear peculiarity is usually ignored/overlooked in practically all specialized references on the topic.

Finally, the statistical properties and the behavior of the density distribution of a particle beam in configuration space under the influence of an isolated sextupole have been studied.Hamilton-Jacobi Equation, interaction representation, generalized twist map

## pacs:29.20.D, 05.45.-a, 45.20.Jj, 47.10.Df††preprint:AIP/123-QED

## IIntroduction

Although the study of chaotic motions in nonlinear mechanics has dominated the field in recent times, the study of regular motion and its stability is still a pressing issue in a number of sub-fields of plasma physics, accelerator physics, celestial mechanics, fluid mechanics and others. These important applications include wave–particle interactionschirik;meiss, magnetic field structure in magnetic confinement devicesrechest;balescu, transport and mixing in fluidsmorris;weiss, particle motion in acceleratorsberg, and long-time evolution of the solar systemwisdom. For instance, increasingly difficult problems arise daily in the design of very large particle accelerators and storage rings. In such machines, particles must be kept in tightly confined orbits for enormous time intervals.

To meet these requirements, accelerator designers rely on single-particle tracking, which involves calculating individual trajectories in external fields for a variety of initial conditions by approximately integrating Hamilton’s equations of motion. The specific nature of the problem often requires the use of unusual integration methods, such as ”kick approximation”, symplectic integration, symplectic mapping methods, etc. Much effort is put into creating numerical integration procedures valid for large time intervals, but inevitably in coexistence with limitations on accuracy, convergence and computational time. In large accelerators, it is difficult (not to say that very often impossible) to track the orbits of individual particles over sufficiently long time intervals in order to assess their stability. Moreover, one can usually afford to try only a limited number of initial conditions, or in other words, a number of particles orders of magnitude less than those actually contained in the beam itself.

The only scheme known to converge is the superconvergent Kolmogorov-Arnold-Moser (KAM) perturbation theoryarnold;gallavotti, but it has unfortunately received scant attention as a possible computational tool in both accelerator and plasma physics. Each step of the KAM iteration invokes an approximate solution to the Hamilton-Jacobi equation, usually in lowest order of perturbation. With the exception of an early paper by Robert L. Warnock and Ronald D. Ruthwarnockand a couple subsequent articles by the same authors, the Hamilton-Jacobi equation method has been practically unused in accelerator physics over the years. To the best of our knowledge, this method has received very scant attention in plasma physicspfirsch, as well.

The Hamilton-Jacobi equation provides an elegant framework for solving Lagrangian and Hamiltonian systems by transforming them into a partial differential equation, simplifying problems like finding geodesics and offering a link between classical mechanics and quantum mechanics. Its advantages include a wave-like interpretation and the ability to describe families of solutions related to conserved quantities - the second feature especially valuable when it comes to the description of regular motion. In addition, it offers a powerful approach to solving problems in analytical mechanics by transforming complex dynamics into a single partial differential equation. Among the merits of the Hamilton-Jacobi equation, it is necessary to mention the facilitation in finding optimal canonical transformations that simplify the Hamiltonian system, potentially making the equations of motion trivial in the new canonical variables. Finally, it must be pointed out that the Hamilton-Jacobi equation is not always a simplification. In many cases, the Hamilton-Jacobi approach does not inherently simplify the solution of the original Hamiltonian problem.

The method of canonical transformations and the associated Hamilton-Jacobi equation are particularly valuable for constructing Hamiltonian maps. It does not suffer from the disadvantages of other known approaches, in which the derivation (except for a known limited number of cases) restricts the possible symplectic forms of the map, thus remaining largely intangible. A good comparison between various methods for deriving symplectic maps, replete with many concrete examples, with an emphasis on the canonical transformations approach, can be found in Ref.abdul.

In the present work, we will show that the above-mentioned method is based on a canonical change of variables, which at first glance eliminates perturbations in periodic time intervals. This procedure transforms the perturbed system into a new one also known as a Hamiltonian system in interaction representation. For that new system the motion is unperturbed (well known in explicit form) throughout the entire period, except for discrete periodic time instants, where all perturbations act instantaneously as kicks.

The article is organized as follows. In SectionsIIandIIIthe Hamilton-Jacobi equation has been introduced as an elegant way to find the trajectories of mechanical systems. Further, on the example of an isolated, infinitely thin magnetic sextupole, the Hamilton-Jacobi equation is being solved perturbatively. The full canonical transformation turns out to be equivalent to theHénon map in a canonical form. In SectionIVthe solution of Hamilton’s equations of motion in interaction representation has been obtained in the form of a generalized one-turn map. The difference between the case where the nonlinear kick comes first, followed by a single one-period rotation, versus the case where the rotation occurs before the kick has been stressed out. This non-obvious difference is usually tactfully omitted in almost all references devoted to the topic. In SectionVIthe statistical properties and the behavior of the density distribution of a particle beam in configuration space under the influence of an isolated sextupole have been studied. Finally, SectionVIIprovides concluding remarks and outlook.

## IIThe Classical Hamilton-Jacobi Equation

For simplicity, let us consider a single degree of freedom betatron motion in the horizontal direction of a plane transverse to the particle trajectory in the presence of a singly located sextupole and/or octupole, perturbing the linear accelerator lattice. In what follows, each of the above-mentioned nonlinearities will be considered either separately or in combination in more detail. It is important to note that in a similar way higher-order multipoles can also be included in the consideration, at the cost of increasing algebraic tediousness in the calculations with the order of the multipole. The Hamiltonian governing the single-particle dynamics is set by the expressiontzenovBOOKH=χ˙​(θ)2​(P2+X2)+𝒮0​(θ)3​X3+𝒪0​(θ)4​X4,H={\frac{{\dot{\chi}}{\left(\theta\right)}}{2}}{\left(P^{2}+X^{2}\right)}+{\frac{{\mathcal{S}}_{0}{\left(\theta\right)}}{3}}X^{3}+{\frac{{\mathcal{O}}_{0}{\left(\theta\right)}}{4}}X^{4},(1)

where𝒮0​(θ)=λ0​(θ)​β3/2​(θ)2​R2,𝒪0​(θ)=μ0​(θ)​β2​(θ)6​R3.{\mathcal{S}}_{0}{\left(\theta\right)}={\frac{\lambda_{0}{\left(\theta\right)}\beta^{3/2}{\left(\theta\right)}}{2R^{2}}},\qquad{\mathcal{O}}_{0}{\left(\theta\right)}={\frac{\mu_{0}{\left(\theta\right)}\beta^{2}{\left(\theta\right)}}{6R^{3}}}.(2)

In addition,(X,P){\left(X,P\right)}denotes the normalized transverse phase-space coordinates andθ\thetais the independent azimuthal variable matching the machine circumference, which usually plays the role of time in accelerator theory. Moreover,χ˙=R/β{\dot{\chi}}=R/\betais the derivative of the phase advance with respect to the azimuthal variable, whereRRis the mean machine radius, andβ\betais the well-known Twiss beta-function. The dimensionless quantitiesλ0​(θ)\lambda_{0}{\left(\theta\right)}andμ0​(θ)\mu_{0}{\left(\theta\right)}measure the sextupole and the octupole strengths, respectively, and are given byλ0=R2Bz​(∂2Bz∂x2)x=z=0,\displaystyle\lambda_{0}={\frac{R^{2}}{B_{z}}}{\left({\frac{\partial^{2}B_{z}}{\partial x^{2}}}\right)}_{x=z=0},(3)μ0=R3Bz​(∂3Bz∂x3)x=z=0.\displaystyle\mu_{0}={\frac{R^{3}}{B_{z}}}{\left({\frac{\partial^{3}B_{z}}{\partial x^{3}}}\right)}_{x=z=0}.(4)

The Hamilton-Jacobi equation is an elegant way to find the trajectories of mechanical systems, but unfortunately it is hardly ever used either in the theory of charged particle accelerators, or in the physics of plasmas. As is commonly knownlandau;goldstein;bahram, the basis of the Hamilton-Jacobi method is the introduction of an appropriately chosen generating function that sets the new Hamiltonian to zero. This means that the new coordinates and the new momenta are constants of motion. The Hamilton-Jacobi equation can solve for these constants of motion, providing an alternative to solving differential (Hamilton’s or Lagrange’s) equations of motion, especially in complex systems. Choosing the generating function to be of the second kindF​(X,p;θ)F{\left(X,p;\theta\right)}, we can write the Hamilton-Jacobi equation as∂θF+χ˙2​[(∂XF)2+X2]+𝒮03​X3+𝒪04​X4=0.\partial_{\theta}F+{\frac{{\dot{\chi}}}{2}}{\left[{\left(\partial_{X}F\right)}^{2}+X^{2}\right]}+{\frac{{\mathcal{S}}_{0}}{3}}X^{3}+{\frac{{\mathcal{O}}_{0}}{4}}X^{4}=0.(5)

Here,∂u\partial_{u}denotes partial derivative with respect to the variable indicated. It is convenient to pass to the phase advanceχ\chias a new independent variable playing the role of time∂χF+12​[(∂XF)2+X2]+ℱ​X3+𝒢​X4=0,\partial_{\chi}F+{\frac{1}{2}}{\left[{\left(\partial_{X}F\right)}^{2}+X^{2}\right]}+{\mathcal{F}}X^{3}+{\mathcal{G}}X^{4}=0,(6)

where the normalized sextupole and octupole strengths, respectivelyℱ​(θ)=𝒮0​(θ)​β​(θ)3​R,𝒢​(θ)=𝒪0​(θ)​β​(θ)4​R,{\mathcal{F}}{\left(\theta\right)}={\frac{{\mathcal{S}}_{0}{\left(\theta\right)}\beta{\left(\theta\right)}}{3R}},\qquad{\mathcal{G}}{\left(\theta\right)}={\frac{{\mathcal{O}}_{0}{\left(\theta\right)}\beta{\left(\theta\right)}}{4R}},(7)

are periodic in the azimuthℱ​(θ+2​π)=ℱ​(θ){\mathcal{F}}{\left(\theta+2\pi\right)}={\mathcal{F}}{\left(\theta\right)}, and𝒢​(θ+2​π)=𝒢​(θ){\mathcal{G}}{\left(\theta+2\pi\right)}={\mathcal{G}}{\left(\theta\right)}. Finding an exact solution to the above equation represents in itself a rather complex task. The fact that the multipole nonlinearity is usually sufficiently weak (much weaker than the characteristic parameters of the linear magnetic lattice) simplifies this task to some extent and the solution to the Hamilton-Jacobi equation can be sought perturbatively. Since an approximate solution with sufficient accuracy is rather satisfactory in practice, we shall adhere to such a strategy here in the subsequent exposition.

To begin with, considering the sextupole and the octupole as a first-order perturbation, the linear magnetic structure is described by the zero-order generating functionF0​(X,p;χ)=X​pcos⁡χ−tan⁡χ2​(p2+X2).F_{0}{\left(X,p;\chi\right)}={\frac{Xp}{\cos\chi}}-{\frac{\tan\chi}{2}}{\left(p^{2}+X^{2}\right)}.(8)

The generating function given by the above Eq. (8) is an exact solution to Eq. (6) forℱ=𝒢=0{\mathcal{F}}={\mathcal{G}}=0. The relationship between the old and new canonical variables isX=x​cos⁡χ+p​sin⁡χ,P=−x​sin⁡χ+p​cos⁡χ,X=x\cos\chi+p\sin\chi,\quad\quad P=-x\sin\chi+p\cos\chi,(9)

where as mentioned above the new canonical coordinates(x,p){\left(x,p\right)}are constants of motion. This is a well-known resulttzenovBOOKthat represents the motion of particles in an accelerator as a rotation in the normalized phase space by an angle equal to the corresponding phase advance.

## IIIPerturbation Solution of the Hamilton-Jacobi Equation

LetG​(X,p;χ)G{\left(X,p;\chi\right)}be the first-order generating function, whereF=F0+G+…F=F_{0}+G+\dotsand the dots imply higher order contributions. The equation it satisfies is written in the form∂χG+(pcos⁡χ−X​tan⁡χ)​∂XG\displaystyle\partial_{\chi}G+{\left({\frac{p}{\cos\chi}}-X\tan\chi\right)}\partial_{X}G+ℱ​(θ)​X3+𝒢​(θ)​X4=0.\displaystyle+{\mathcal{F}}{\left(\theta\right)}X^{3}+{\mathcal{G}}{\left(\theta\right)}X^{4}=0.(10)

Our goal here is to demonstrate the detailed performance and efficiency of the Hamilton-Jacobi method on the simplest example of lowest-order (cubic) nonlinearity. The solution of the first-order Hamilton-Jacobi equation (10) is sought in the form of a homogeneous polynomial of third order in the mixed canonical variablesG​(X,p;χ)=A​(χ)3​X3+B​(χ)​X2​p\displaystyle G{\left(X,p;\chi\right)}={\frac{A{\left(\chi\right)}}{3}}X^{3}+B{\left(\chi\right)}X^{2}p+C​(χ)​X​p2+D​(χ)3​p3.\displaystyle+C{\left(\chi\right)}Xp^{2}+{\frac{D{\left(\chi\right)}}{3}}p^{3}.(11)

As can be easily verified, the polynomial coefficients satisfy the system of linear first-order differential equationsd​Ad​χ−3​A​tan⁡χ+3​ℱ=0,\displaystyle{\frac{{\rm d}A}{{\rm d}\chi}}-3A\tan\chi+3{\mathcal{F}}=0,(12)d​Bd​χ−2​B​tan⁡χ+Acos⁡χ=0,\displaystyle{\frac{{\rm d}B}{{\rm d}\chi}}-2B\tan\chi+{\frac{A}{\cos\chi}}=0,(13)d​Cd​χ−C​tan⁡χ+2​Bcos⁡χ=0,d​Dd​χ+3​Ccos⁡χ=0,{\frac{{\rm d}C}{{\rm d}\chi}}-C\tan\chi+{\frac{2B}{\cos\chi}}=0,\qquad{\frac{{\rm d}D}{{\rm d}\chi}}+{\frac{3C}{\cos\chi}}=0,(14)

In order to illustrate the results obtained by the method of the Hamilton-Jacobi equation, we consider a single sextupole kick (in analogy with Ref.tzenovDV) at each successive turn in the vicinity of the locationsθ=0,2​π,4​π,…\theta=0,2\pi,4\pi,\dots. In thin lens approximation the sextupole strength𝒮0​(θ){\mathcal{S}}_{0}{\left(\theta\right)}in Eq. (2) can be written as a sampling function (also known as the Dirac comb function)𝒮0​(θ)=𝒮​∑k=−∞∞δ​(θ−2​k​π),𝒮=Ls​λ0​β03/22​R3,{\mathcal{S}}_{0}{\left(\theta\right)}={\mathcal{S}}\sum\limits_{k=-\infty}^{\infty}\delta{\left(\theta-2k\pi\right)},\qquad{\mathcal{S}}={\frac{L_{s}\lambda_{0}\beta_{0}^{3/2}}{2R^{3}}},(15)

whereLsL_{s}is the sextupole length. Taking into account the relation (2) and the properties of the Dirac delta function, we can expressℱ​(χ){\mathcal{F}}{\left(\chi\right)}in terms of the phase advanceχ\chias an independent variable as followsℱ​(χ)=𝒮3​∑k=−∞∞δ​[χ​(θ)−k​ω],ω=2​π​ν,{\mathcal{F}}{\left(\chi\right)}={\frac{\mathcal{S}}{3}}\sum\limits_{k=-\infty}^{\infty}\delta{\left[\chi{\left(\theta\right)}-k\omega\right]},\quad\quad\omega=2\pi\nu,(16)

whereν\nuis the unperturbed betatron tune. The equations (12) – (14) for determining the unknown coefficientsAA,BB,CCandDDare coupled linear first-order differential equations. Note that once the solution to a preceding one starting with the first Eq. (12) forAAis found, it automatically determines the solution to the next equation. The general solution to the equation forAAcan be written asA​(χ)=−3cos3⁡χ​∫χdτ​ℱ​(τ)​cos3⁡τ,A{\left(\chi\right)}=-{\frac{3}{\cos^{3}\chi}}\int\limits^{\chi}{\rm d}\tau{\mathcal{F}}{\left(\tau\right)}\cos^{3}\tau,(17)

with the natural initial conditionA​(0)=0A{\left(0\right)}=0. To take the above integral in explicit form, we use the well-known Fourier series expansion of the Dirac comb functiontzenovBOOK∑k=−∞∞δ​[χ​(θ)−k​ω]=1ω​∑n=−∞∞exp⁡(i​n​χν),\sum\limits_{k=-\infty}^{\infty}\delta{\left[\chi{\left(\theta\right)}-k\omega\right]}={\frac{1}{\omega}}\sum\limits_{n=-\infty}^{\infty}\exp{\left(in{\frac{\chi}{\nu}}\right)},(18)

as well as the identity∑k=−∞∞ei​k​xk+a=\displaystyle\sum\limits_{k=-\infty}^{\infty}{\frac{{\rm e}^{ikx}}{k+a}}=πsin⁡π​a​exp⁡{i​[(2​n+1)​π−x]​a}\displaystyle\!\!\!{\frac{\pi}{\sin\pi a}}\exp{\left\{i{\left[{\left(2n+1\right)}\pi-x\right]}a\right\}}(19)for​2​π​n<x<2​π​(n+1).\displaystyle{\rm for}\;2\pi n<x<2\pi{\left(n+1\right)}.

The result isA​(χ)=−ℳncos3⁡χ,\displaystyle A{\left(\chi\right)}=-{\frac{{\mathcal{M}}_{n}}{\cos^{3}\chi}},ℳn=𝒮8​[𝒟n​(3​ω)+3​𝒟n​(ω)±4],\displaystyle{\mathcal{M}}_{n}={\frac{{\mathcal{S}}}{8}}{\left[{\mathcal{D}}_{n}{\left(3\omega\right)}+3{\mathcal{D}}_{n}{\left(\omega\right)}\pm 4\right]},(20)

where𝒟n​(ξ)=∑k=−nnei​k​ξ=sin⁡[(n+1/2)​ξ]sin⁡(ξ/2),{\mathcal{D}}_{n}{\left(\xi\right)}=\sum\limits_{k=-n}^{n}{\rm e}^{ik\xi}={\frac{\sin{\left[{\left(n+1/2\right)}\xi\right]}}{\sin{\left(\xi/2\right)}}},(21)

is the well-known Dirichlet kernel. The interested reader is referred to Ref.dirichlet, where the mathematical details concerning the Dirichlet kernel are presented in a good, consistent and understandable form. In addition, the sign ”++” must be adopted in case the zero phase advance count starts in a smallϵ\epsilon-neighborhood including the zero(0−ϵ){\left(0-\epsilon\right)}, while the ”−-” sign is taken if the count starts from0+ϵ0+\epsilonexcluding the zeroth kick. Next, the solutions forBB,CCandDDare obtained in a straightforward manner and are expressed as followsB​(χ)=ℳncos2⁡χ​tan⁡χ,C​(χ)=−ℳncos⁡χ​tan2⁡χ,B{\left(\chi\right)}={\frac{{\mathcal{M}}_{n}}{\cos^{2}\chi}}\tan\chi,\qquad C{\left(\chi\right)}=-{\frac{{\mathcal{M}}_{n}}{\cos\chi}}\tan^{2}\chi,(22)D​(χ)=ℳn​tan3⁡χ.D{\left(\chi\right)}={\mathcal{M}}_{n}\tan^{3}\chi.(23)

At this point we need to clarify what the subscriptnnrepresents in the definition (20) of the quantityℳn{\mathcal{M}}_{n}. The discrete nature of the sextupole nonlinearity given by the Dirac comb (16), causes discreteness in the solution of the Hamilton-Jacobi equation, so the subscriptnndenotes the ordinal number of the revolution.

Let us now explain in detail what the value of the just obtained solution to the Hamilton-Jacobi equation is and what the direct consequence of it is. From Eqs. (8) and (11), we obtain the canonical transformationx=Xcos⁡χ−p​tan⁡χ+B​X2+2​C​X​p+D​p2,x={\frac{X}{\cos\chi}}-p\tan\chi+BX^{2}+2CXp+Dp^{2},(24)P=pcos⁡χ−X​tan⁡χ+A​X2+2​B​X​p+C​p2.P={\frac{p}{\cos\chi}}-X\tan\chi+AX^{2}+2BXp+Cp^{2}.(25)

The first thing that catches the eye is the resonant nature of the canonical transformations (24) and (25) embedded in the quantityℳn{\mathcal{M}}_{n}entering the corresponding polynomial coefficients. The reason is the specific behavior of the Dirichlet kernel𝒟n​(3​ω){\mathcal{D}}_{n}{\left(3\omega\right)}for values of the betatron tune close to third-order resonance, and for large values of the number of turnsnn. For small values of the sextupole strength𝒮{\mathcal{S}}and for a small number of revolutions, the quantityℳn{\mathcal{M}}_{n}remains sufficiently small. In such a case, equations (24) and (25) can be solved approximately in explicit form by successive iterations of the zero-order canonical transformation (9). As a result, we obtainX⟶x​cos⁡χ+(p−ℳn​x2)​sin⁡χ,X\longrightarrow x\cos\chi+{\left(p-{\mathcal{M}}_{n}x^{2}\right)}\sin\chi,(26)p−ℳn​x2⟶X​sin⁡χ+P​cos⁡χ.p-{\mathcal{M}}_{n}x^{2}\longrightarrow X\sin\chi+P\cos\chi.(27)

As we shall see in the next Section, the above canonical transformations are equivalent to the Hénon map in a canonical form.

## IVHamilton’s Equations of Motion in Interaction Representation and the Hénon Map

## IV.1Hamilton’s Equations of Motion

The generating function (8) eliminates the part in the Hamiltonian (1) responsible for the linear structure of the accelerator, thus emphasizing the influence of the relevant nonlinearities. Such a representation is known in classical (and quantum) mechanics as the interaction representation. The new Hamiltonian is written as followsH1​(x,p;θ)=𝒮0​(θ)3​(x​cos⁡χ+p​sin⁡χ)3\displaystyle H_{1}{\left(x,p;\theta\right)}={\frac{{\mathcal{S}}_{0}{\left(\theta\right)}}{3}}{\left(x\cos\chi+p\sin\chi\right)}^{3}+𝒪0​(θ)4​(x​cos⁡χ+p​sin⁡χ)4.\displaystyle+{\frac{{\mathcal{O}}_{0}{\left(\theta\right)}}{4}}{\left(x\cos\chi+p\sin\chi\right)}^{4}.(28)

The Hamilton’s equations of motion in terms of the new canonical variables(x,p){\left(x,p\right)}acquire rather symmetric formd​xd​θ=[𝒮0(xcosχ+psinχ)2\displaystyle{\frac{{\rm d}x}{{\rm d}\theta}}={\left[{\mathcal{S}}_{0}{\left(x\cos\chi+p\sin\chi\right)}^{2}\right.}+𝒪0(xcosχ+psinχ)3]sinχ,\displaystyle{\left.+{\mathcal{O}}_{0}{\left(x\cos\chi+p\sin\chi\right)}^{3}\right]}\sin\chi,(29)d​pd​θ=−[𝒮0(xcosχ+psinχ)2\displaystyle{\frac{{\rm d}p}{{\rm d}\theta}}=-{\left[{\mathcal{S}}_{0}{\left(x\cos\chi+p\sin\chi\right)}^{2}\right.}+𝒪0(xcosχ+psinχ)3]cosχ,\displaystyle{\left.+{\mathcal{O}}_{0}{\left(x\cos\chi+p\sin\chi\right)}^{3}\right]}\cos\chi,(30)

Let us consider as above a single multipole kick at each successive turn in the vicinity of the locationsθ=0,2​π,4​π,…\theta=0,2\pi,4\pi,\dots.

In the subsequent exposition worked out in detail will be the case of an isolated infinitely thin sextupole with a strength𝒮0​(θ){\mathcal{S}}_{0}{\left(\theta\right)}as in Eq. (2), written again as a sampling function (15). Similar arguments and considerations are valid in the case of a single octupole kick, or a higher-order-multipole kick.

## IV.2The Standard and the Backward Henon Map

If the nonlinear magnetic elements can be regarded as concentrated in a point resembling infinitely thin lenses, Hamilton’s equations (29) and (30) can be solved exactly within one revolution. This is a standard procedure where the solution is represented as a recurrent symplectic map. The solutions of the Hamilton’s equations can be sought in two alternative intervalsθ∈(−ϵ,2​π−ϵ)\theta\in{\left(-\epsilon,\;\;\;2\pi-\epsilon\right)}orθ∈(ϵ,2​π+ϵ)\theta\in{\left(\epsilon,\;\;\;2\pi+\epsilon\right)}both covering one complete revolution period. In the first case, the lap revolution is counted starting in the epsilon-neighborhood before the nonlinear kick (to be included), while in the second case, the count starts immediately after the previous (uncounted) kick and ends immediately after the corresponding next-in-order kick is performed. In other words, in the first case the nonlinear kick comes first, followed by the one-turn rotation, while in the second case, the one-period rotation occurs before the kick. There is a difference in the result of solving Hamilton’s equations between the two cases, which is usually ignored or silenced tactfully in practically all dedicated references on this topic. We will dwell on this difference in more detail here.

Consider an isolated nonlinear element, say a sextupole - higher-order nonlinear elements can be treated in a completely analogous way. First, we solve Hamilton’s equations of motion in the intervalθ∈(−ϵ,2​π−ϵ)\theta\in{\left(-\epsilon,\;\;\;2\pi-\epsilon\right)}and obtainx=x0=const,p=p0−𝒮​x02.x=x_{0}={\rm const},\qquad p=p_{0}-{\mathcal{S}}x_{0}^{2}.(31)

Generalizing the above result for each successivenn-th turn and taking into account the relations of Eqs. (9), the one-turn map can be written asXn+1=Xn​cos⁡ω+(Pn−𝒮​Xn2)​sin⁡ω,\displaystyle X_{n+1}=X_{n}\cos\omega+{\left(P_{n}-{\mathcal{S}}X_{n}^{2}\right)}\sin\omega,Pn+1=−Xn​sin⁡ω+(Pn−𝒮​Xn2)​cos⁡ω.\displaystyle P_{n+1}=-X_{n}\sin\omega+{\left(P_{n}-{\mathcal{S}}X_{n}^{2}\right)}\cos\omega.(32)

Here,(Xn,Pn){\left(X_{n},P_{n}\right)}are the initial values(x0,p0){\left(x_{0},p_{0}\right)}of the canonical variables before the respectivenn-th lap, while(Xn+1,Pn+1){\left(X_{n+1},P_{n+1}\right)}are the corresponding values after performing the rotation. The two-dimensional mapping (32) is known as the Hénon maphenon;tzenovBOOK.Figure 1:Phase portrait of the canonical Hénon map (33) close to the third-order nonlinear resonance3​ν=integer3\nu={\rm integer}. The particular value of the fractional part of the unperturbed betatron tune is taken to be0.311140.31114.

In dimensionless variables(X^,P^)=𝒮​(X,P){\left({\widehat{X}},{\widehat{P}}\right)}={\mathcal{S}}{\left(X,P\right)}the Hénon map acquires the canonical formX^n+1=X^n​cos⁡ω+(P^n−X^n2)​sin⁡ω,\displaystyle{\widehat{X}}_{n+1}={\widehat{X}}_{n}\cos\omega+{\left({\widehat{P}}_{n}-{\widehat{X}}_{n}^{2}\right)}\sin\omega,P^n+1=−X^n​sin⁡ω+(P^n−X^n2)​cos⁡ω.\displaystyle{\widehat{P}}_{n+1}=-{\widehat{X}}_{n}\sin\omega+{\left({\widehat{P}}_{n}-{\widehat{X}}_{n}^{2}\right)}\cos\omega.(33)

Let us now obtain the solution of Hamilton’s equations (29) and (30) in the intervalθ∈(ϵ,2​π+ϵ)\theta\in{\left(\epsilon,\;\;\;2\pi+\epsilon\right)}. The result isx=x0+𝒮​(x0​cos⁡ω+p0​sin⁡ω)2​sin⁡ω,\displaystyle x=x_{0}+{\mathcal{S}}{\left(x_{0}\cos\omega+p_{0}\sin\omega\right)}^{2}\sin\omega,p=p0−𝒮​(x0​cos⁡ω+p0​sin⁡ω)2​cos⁡ω.\displaystyle p=p_{0}-{\mathcal{S}}{\left(x_{0}\cos\omega+p_{0}\sin\omega\right)}^{2}\cos\omega.(34)

Taking again into account the relations of Eqs. (9), the one-turn map can be written alternativelyXn+1=Xn​cos⁡ω+Pn​sin⁡ω,\displaystyle X_{n+1}=X_{n}\cos\omega+P_{n}\sin\omega,Pn+1=−Xn​sin⁡ω+Pn​cos⁡ω−𝒮​Xn+12.\displaystyle P_{n+1}=-X_{n}\sin\omega+P_{n}\cos\omega-{\mathcal{S}}X_{n+1}^{2}.(35)

This is thebackward Hénon map, which can be flipped over (reversed) and written like thisXn=Xn+1​cos⁡ω−(Pn+1+𝒮​Xn+12)​sin⁡ω,\displaystyle X_{n}=X_{n+1}\cos\omega-{\left(P_{n+1}+{\mathcal{S}}X_{n+1}^{2}\right)}\sin\omega,Pn=Xn+1​sin⁡ω+(Pn+1+𝒮​Xn+12)​cos⁡ω.\displaystyle P_{n}=X_{n+1}\sin\omega+{\left(P_{n+1}+{\mathcal{S}}X_{n+1}^{2}\right)}\cos\omega.(36)

The backward map is basically the same Hénon map, but with the difference that the motion takes place in the opposite direction, equivalent to reversing time.Figure 2:Phase portrait of the backward canonical Hénon map counterpart of Eqs. (36) close to the third-order resonance3​ν=integer3\nu={\rm integer}. Similar to Fig.1, the particular value of the fractional part of the unperturbed betatron tune is taken to be0.311140.31114.

The result just obtained is quite interesting, to some extent non-trivial, and in addition, rather intuitively unexpected.

Figures (1) and (2) present the typical phase portraits of the standard Hénon map (33) and the backward Hénon map, respectively. It is clearly visible that apart from a rotation in phase space by an angle ofπ/2\pi/2, the two phase portraits are identical.

## VThe General Twist Map

Consider now a combination of nonlinear magnetic elements, say a sextupole (located atθs=0\theta_{s}=0) and an octupole located atθo\theta_{o}along the machine circumference. Similar to Eq. (15), in the thin lens approximation the corresponding octupole strength𝒪0​(θ){\mathcal{O}}_{0}{\left(\theta\right)}can be written as𝒪0​(θ)=𝒪​∑k=−∞∞δ​(θ−2​k​π),𝒪=Lo​μ0​β026​R4,{\mathcal{O}}_{0}{\left(\theta\right)}={\mathcal{O}}\sum\limits_{k=-\infty}^{\infty}\delta{\left(\theta-2k\pi\right)},\qquad{\mathcal{O}}={\frac{L_{o}\mu_{0}\beta_{0}^{2}}{6R^{4}}},(37)

whereLoL_{o}is the octupole length. Repeating the arguments used in the derivation of the Henon map, successively for the sextupole and for the octupole, we can write the canonical (dimensionless) one-turn map in the form of a generalized twist mapXn+1=(Xn+Fn)​cos⁡ω+(Pn+Gn)​sin⁡ω,\displaystyle X_{n+1}={\left(X_{n}+F_{n}\right)}\cos\omega+{\left(P_{n}+G_{n}\right)}\sin\omega,Pn+1=−(Xn+Fn)​sin⁡ω+(Pn+Gn)​cos⁡ω,\displaystyle P_{n+1}=-{\left(X_{n}+F_{n}\right)}\sin\omega+{\left(P_{n}+G_{n}\right)}\cos\omega,(38)

whereFn=F​(Xn,Pn)F_{n}=F{\left(X_{n},P_{n}\right)}andGn=G​(Xn,Pn)G_{n}=G{\left(X_{n},P_{n}\right)}are certain functions ofXnX_{n}andPnP_{n}. In our case these functions are expressed asF​(X,P)=Λo​[X​cos⁡ωo+(P−X2)​sin⁡ωo]3\displaystyle F{\left(X,P\right)}=\Lambda_{o}{\left[X\cos\omega_{o}+{\left(P-X^{2}\right)}\sin\omega_{o}\right]}^{3}×sin⁡ωo,\displaystyle\times\sin\omega_{o},(39)G(X,P)=−X2−Λo[Xcosωo\displaystyle G{\left(X,P\right)}=-X^{2}-\Lambda_{o}{\left[X\cos\omega_{o}\right.}+(P−X2)sinωo]3cosωo.\displaystyle{\left.+{\left(P-X^{2}\right)}\sin\omega_{o}\right]}^{3}\cos\omega_{o}.(40)

Hereωo\omega_{o}is the phase advance in the location of the octupole, whileΛo=𝒪/𝒮2\Lambda_{o}={\mathcal{O}}/{\mathcal{S}}^{2}is a dimensionless parameter comparing in terms of order-of-magnitude the strengths of the sextupole and the octupole. It can be easily verified that the generalized twist map (38) is symplectic if∂F∂X+∂G∂P+{F,G}=0,{\frac{\partial F}{\partial X}}+{\frac{\partial G}{\partial P}}+{\left\{F,G\right\}}=0,(41)

where{F,G}=∂F∂X​∂G∂P−∂F∂P​∂G∂X,{\left\{F,G\right\}}={\frac{\partial F}{\partial X}}{\frac{\partial G}{\partial P}}-{\frac{\partial F}{\partial P}}{\frac{\partial G}{\partial X}},(42)

is the Poisson bracket.Figure 3:Phase portrait of the generalized twist map of Eqs. (38) close to the fourth-order resonance4​ν=integer4\nu={\rm integer}. The octupole location is taken to beθo=π\theta_{o}=\pi, while its relative strength isΛo∼1\Lambda_{o}\sim 1. The particular value of the fractional part of the unperturbed betatron tune is taken to be0.2430.243.

Figure (3) shows the phase portrait of the generalized twist map presented by Eqs. (38). The fourfold symmetry of the islands of stability, manifested near the fourth-order resonance driven by the octupole nonlinearity, is clearly visible. The outer envelope (separatrix) of the phase-space curves has a triangular symmetry, caused by the leading sextupole nonlinearity.

## VIStatistical Description of Nonlinear Dynamics

Statistical theory is always associated with a specific dynamical model of some kind, the evolution of which is most often governed by equations of motion. Among the preserved quantities characterizing a given dynamical model, one of particular importance is a quantity possessing classical probabilistic properties, called the distribution function. For Hamiltonian systems of the type (1) the distribution functionf​(X,P;θ)f{\left(X,P;\theta\right)}satisfies the Liouville equation∂f∂θ+{f,H}=0.{\frac{\partial f}{\partial\theta}}+{\left\{f,H\right\}}=0.(43)

It can be showntzenovBOOK;davidsonthat a possible solution of the Liouville equation is a distribution functionf​(X,P;θ)f{\left(X,P;\theta\right)}, which is constant (independent ofXX,PPandθ\theta) inside a region in phase space confined by the simply connected boundary curvesP(+)​(X;θ)P_{(+)}{\left(X;\theta\right)}andP(−)​(X;θ)P_{(-)}{\left(X;\theta\right)}, and zero outside. In other wordsf(X,P;θ)=𝒞{ℋ[P−P(−)(X;θ)]\displaystyle f{\left(X,P;\theta\right)}={\mathcal{C}}{\left\{{\mathcal{H}}{\left[P-P_{(-)}{\left(X;\theta\right)}\right]}\right.}−ℋ[P−P(+)(X;θ)]},\displaystyle{\left.-{\mathcal{H}}{\left[P-P_{(+)}{\left(X;\theta\right)}\right]}\right\}},(44)

whereℋ​(z){\mathcal{H}}{\left(z\right)}is the well-known Heaviside function. Defining further the hydrodynamic densityϱ​(X;θ)\varrho{\left(X;\theta\right)}and the current velocityV​(X;θ)V{\left(X;\theta\right)}according to the relationsϱ​(X;θ)=𝒞​[P(+)​(X;θ)−P(−)​(X;θ)],\varrho{\left(X;\theta\right)}={\mathcal{C}}{\left[P_{(+)}{\left(X;\theta\right)}-P_{(-)}{\left(X;\theta\right)}\right]},(45)V​(X;θ)=12​[P(+)​(X;θ)+P(−)​(X;θ)],V{\left(X;\theta\right)}={\frac{1}{2}}{\left[P_{(+)}{\left(X;\theta\right)}+P_{(-)}{\left(X;\theta\right)}\right]},(46)

the Liouville equation (43) can be cast into completely equivalent system of hydrodynamic equations∂ϱ∂χ+∂∂X​(ϱ​V)=0,{\frac{\partial\varrho}{\partial\chi}}+{\frac{\partial}{\partial X}}{\left(\varrho V\right)}=0,(47)∂V∂χ+V​∂V∂X+vT2​∂∂X​(ϱ2)=−X−3​ℱ​X2−4​𝒢​X3.{\frac{\partial V}{\partial\chi}}+V{\frac{\partial V}{\partial X}}+v_{T}^{2}{\frac{\partial}{\partial X}}{\left(\varrho^{2}\right)}=-X-3{\mathcal{F}}X^{2}-4{\mathcal{G}}X^{3}.(48)

The quantityvT2=18​𝒞2,v_{T}^{2}={\frac{1}{8{\mathcal{C}}^{2}}},(49)

is the normalized thermal speed-squared. The above system of hydrodynamic equations supplemented with the field equations for the self-consistent potentials has been widely studied in describing collective processes in intense space-charge dominated beams and beam-plasma systemstzenovBOOK;davidson;tzenvol.Figure 4:Unperturbed density profileϱ0​(X)\varrho_{0}{\left(X\right)}according to Eq. (50).

Here it is worth noting in the first place, that in the spirit of Eqs. (9) for the linear unperturbed accelerator lattice, we haveP2+X2=x2+p2=const,P^{2}+X^{2}=x^{2}+p^{2}={\rm const},

implying thatP(±)​(X;θ)∼±const−X2P_{(\pm)}{\left(X;\theta\right)}\sim\pm{\sqrt{{\rm const}-X^{2}}}. With this reasoning in hand, it is convenient to write the solution of the hydrodynamic system (47) and (48) in the formϱ02​(X)=𝒥−X22​vT2,V0=0,\varrho_{0}^{2}{\left(X\right)}={\mathcal{J}}-{\frac{X^{2}}{2v_{T}^{2}}},\qquad\qquad V_{0}=0,(50)

which is exact in the case of an unperturbed linear machine structure. Here𝒥=const{\mathcal{J}}={\rm const}denotes the linear betatron invariant. This solution will serve us further as a basic zero-order approximation. Considering the nonlinear elements as first-order contributions in magnitude, we write the linearized hydrodynamic equations as∂ϱ1∂χ+∂∂X​(ϱ0​V1)=0,{\frac{\partial\varrho_{1}}{\partial\chi}}+{\frac{\partial}{\partial X}}{\left(\varrho_{0}V_{1}\right)}=0,(51)∂V1∂χ+2​vT2​∂∂X​(ϱ0​ϱ1)=−3​ℱ​X2−4​𝒢​X3.{\frac{\partial V_{1}}{\partial\chi}}+2v_{T}^{2}{\frac{\partial}{\partial X}}{\left(\varrho_{0}\varrho_{1}\right)}=-3{\mathcal{F}}X^{2}-4{\mathcal{G}}X^{3}.(52)

Manipulate these in an obvious manner, we end up with a single equation forϱ1\varrho_{1}expressed as∂2ϱ1∂χ2−2​vT2​∂∂X​[ϱ0​∂∂X​(ϱ0​ϱ1)]\displaystyle{\frac{\partial^{2}\varrho_{1}}{\partial\chi^{2}}}-2v_{T}^{2}{\frac{\partial}{\partial X}}{\left[\varrho_{0}{\frac{\partial}{\partial X}}{\left(\varrho_{0}\varrho_{1}\right)}\right]}=∂∂X​[ϱ0​(3​ℱ​X2+4​𝒢​X3)].\displaystyle={\frac{\partial}{\partial X}}{\left[\varrho_{0}{\left(3{\mathcal{F}}X^{2}+4{\mathcal{G}}X^{3}\right)}\right]}.(53)

It is reasonable to assume that the effect of the nonlinearity on the density functionϱ0​(X)\varrho_{0}{\left(X\right)}is limited only to varying the linear invariant𝒥\mathcal{J}. Thus, we conjecture a tentative solution to the above equation of the formϱ1​(X;χ)=12​ϱ0​𝒥1​(X;χ).\varrho_{1}{\left(X;\chi\right)}={\frac{1}{2\varrho_{0}}}{\mathcal{J}}_{1}{\left(X;\chi\right)}.(54)

The new unknown function𝒥1{\mathcal{J}}_{1}satisfies the following equation∂2𝒥1∂χ2−2​vT2​ϱ02​∂2𝒥1∂X2+X​∂𝒥1∂X\displaystyle{\frac{\partial^{2}{\mathcal{J}}_{1}}{\partial\chi^{2}}}-2v_{T}^{2}\varrho_{0}^{2}{\frac{\partial^{2}{\mathcal{J}}_{1}}{\partial X^{2}}}+X{\frac{\partial{\mathcal{J}}_{1}}{\partial X}}=2​ϱ02​(6​ℱ​X+12​𝒢​X2)\displaystyle=2\varrho_{0}^{2}{\left(6{\mathcal{F}}X+12{\mathcal{G}}X^{2}\right)}−1vT2​(3​ℱ​X3+4​𝒢​X4).\displaystyle-{\frac{1}{v_{T}^{2}}}{\left(3{\mathcal{F}}X^{3}+4{\mathcal{G}}X^{4}\right)}.(55)

Consider again an isolated infinitely thin sextupole; octupoles and other higher-order nonlinear elements can be treated in a similar manner. It is clear that the solution to Eq. (55) can be written as follows𝒥1​(X;χ)=𝒜​(χ)​X+ℬ​(χ)​X3.{\mathcal{J}}_{1}{\left(X;\chi\right)}={\mathcal{A}}{\left(\chi\right)}X+{\mathcal{B}}{\left(\chi\right)}X^{3}.(56)

where the unknowns𝒜​(χ){\mathcal{A}}{\left(\chi\right)}andℬ​(χ){\mathcal{B}}{\left(\chi\right)}satisfy the equationsd2​ℬd​χ2+9​ℬ=−9​ℱvT2,{\frac{{\rm d}^{2}{\mathcal{B}}}{{\rm d}\chi^{2}}}+9{\mathcal{B}}=-{\frac{9{\mathcal{F}}}{v_{T}^{2}}},(57)d2​𝒜d​χ2+𝒜=12​𝒥​(ℱ+vT2​ℬ).{\frac{{\rm d}^{2}{\mathcal{A}}}{{\rm d}\chi^{2}}}+{\mathcal{A}}=12{\mathcal{J}}{\left({\mathcal{F}}+v_{T}^{2}{\mathcal{B}}\right)}.(58)

Utilizing the Fourier series expansion of the Dirac comb function (18) the solution of Eq. (57) in a Fourier series decomposition is found to beℬ​(χ)=𝒮4​π​vT2​∑n=−∞∞(1n−3​ν−1n+3​ν)\displaystyle{\mathcal{B}}{\left(\chi\right)}={\frac{{\mathcal{S}}}{4\pi v_{T}^{2}}}\sum\limits_{n=-\infty}^{\infty}{\left({\frac{1}{n-3\nu}}-{\frac{1}{n+3\nu}}\right)}×exp⁡(i​n​χν),\displaystyle\times\exp{\left(in{\frac{\chi}{\nu}}\right)},(59)

Taking into account the identity (19), we can convert the Fourier representation (59) into a closed form. The result isℬ​(χ)=−𝒮2​vT2​sin⁡(3​ω/2)​cos⁡3​[χ−(n+1/2)​ω],{\mathcal{B}}{\left(\chi\right)}=-{\frac{{\mathcal{S}}}{2v_{T}^{2}\sin{\left(3\omega/2\right)}}}\cos 3{\left[\chi-{\left(n+1/2\right)}\omega\right]},(60)

wheren​ω<χ<(n+1)​ωn\omega<\chi<{\left(n+1\right)}\omega. In a similar way, one can proceed with the analysis of Eq. (58), the solution of which is expressed as follows𝒜​(χ)=2​𝒥​𝒮sin⁡(ω/2)​cos⁡[χ−(n+1/2)​ω]\displaystyle{\mathcal{A}}{\left(\chi\right)}={\frac{2{\mathcal{J}}{\mathcal{S}}}{\sin{\left(\omega/2\right)}}}\cos{\left[\chi-{\left(n+1/2\right)}\omega\right]}+3​𝒥​𝒮4​sin⁡(3​ω/2)​cos⁡3​[χ−(n+1/2)​ω].\displaystyle+{\frac{3{\mathcal{J}}{\mathcal{S}}}{4\sin{\left(3\omega/2\right)}}}\cos 3{\left[\chi-{\left(n+1/2\right)}\omega\right]}.(61)Figure 5:Density profileϱ0​(X,χ)\varrho_{0}{\left(X,\chi\right)}, where𝒥{\mathcal{J}}has been replaced by𝒥+𝒥1{\mathcal{J}}+{\mathcal{J}}_{1}according to Eq. (56). The particular value of the fractional part of the unperturbed betatron tune is taken to be0.33332650.3333265, that is close to the third-order resonance.

Figure (4) presents the density function in the linear accelerator structure, while Fig.5shows the structural effect of the isolated sextupole. The distortion and the periodicity of the density distribution are clearly visible at values of the unperturbed betatron tune close to third-order resonance. It is important to note that at values of the betatron tune increasingly close to the third-order resonance, unpopulated islands (holes) appear in the density distribution.

## VIIConcluding Remarks and Outlook

The main cornerstone of the present article is the introduction of the Hamilton-Jacobi equation as an elegant way to explicitly compute the trajectories of mechanical systems. The application of the canonical transformation approach is particularly advantageous in deriving recurrence maps, since the latter are necessarily symplectic by construction. In particular, on the example of an isolated, infinitely thin magnetic sextupole, the Hamilton-Jacobi equation is solved perturbatively. It turns out that the full canonical transformation thus obtained is equivalent to the Hénon map in canonical form.

The elimination of the unperturbed part of the overall dynamical system, whose dynamics are assumed to be known, a procedure also known as the interaction representation, is extremely convenient. In addition, if the nonlinear magnetic elements can be considered as infinitely thin lenses, the Hamiltonian equations can be solved exactly within a single one period. Thus, the solution of the equations of motion in the interaction representation is obtained in the form of a generalized one-turn symplectic twist map.

Two cases are considered in detail: in the first case, the full rotation along the machine circumference is counted starting from an epsilon-neighborhood before the nonlinear kick (to be included). In the second case, the counting of one period starts immediately after the previous (uncounted) kick and ends immediately after the corresponding next kick is performed and counted in. The difference in solving Hamilton’s equations between the two cases is that the first case yields the classical Hénon map, while in the second case the backward Hénon map is obtained. This non-trivial peculiarity is usually ignored or tactfully omitted in practically all specialized references on this topic.

Finally, a study of the statistical properties and behavior of the density distribution of a particle beam in configuration space under the influence of an isolated sextupole is carried out.

## Acknowledgements

It is a pleasure to express my gratitude to Profs. Jie Gao and Yuan Zhang for making useful comments and suggestions. Fruitful discussions on topics touched upon in the present article with Dr. Yiwei Wang are also gratefully acknowledged.

## References
- [1]Boris V. Chirikov.A universal instability of many-dimensional oscillator systems.Physics Reports, 52(5):263–379, 1979.
- [2]R.S. MacKay and J.D. Meiss (ed).Hamiltonian Dynamical Systems: A Reprint Selection.Hilger, Bristol, (1987).
- [3]A. B. Rechester, M. N. Rosenbluth and R. B. White.Fourier-space paths applied to the calculation of diffusion for the chirikov-taylor model.Physical Review A, 23:2664–2672, 1981.
- [4]R. Balescu, M. Vlad, and F. Spineanu.Tokamap: A hamiltonian twist map for magnetic field lines in a toroidal geometry.Physical Review E, 58(1):951–964, 1998.
- [5]Diego del‐Castillo‐Negrete and P. J. Morrison.Chaotic transport by rossby waves in shear flow.Physics of Fluids, 5(4):948–965, 1993.
- [6]Jeffrey B. Weiss.Hamiltonian maps and transport in structured fluids.Physica D, 76(1–3):230–238, 1994.
- [7]J. S. Berg, R. L. Warnock, R. D. Ruth, and E. Forest.Construction of symplectic maps for nonlinear motion of particles in accelerators.Physical Review E, 49(1):722–743, 1994.
- [8]J. Wisdom, M. Holman and J. Touma.Integration algorithms for classical mechanics,Fields Institute Communications, vol. 10, eds. J. E. Marsden, G. W. Patrick and W. F. Shadwick,pp. 217–244.American Mathematical Society, Providence, RI, (1996).
- [9]V. I. Arnold.Mathematical Methods of Classical Mechanics.Springer, Berlin, (1978).
- [10]G. Gallavotti.The Elements of Mechanics.Springer, Berlin, (1983).
- [11]R. L. Warnock and R. D. Ruth.Invariant tori through direct solution of the hamilton-jacobi equation.Physica D, 26(1):1–36, 1987.
- [12]D. Pfirsch.Hamilton-jacobi theory applied to vlasov’s equation.Nuclear Fusion, 6(4):301–306, 1966.
- [13]Sadrilla S. Abdullaev.Construction of Mappings for Hamiltonian Systems and Their Applications.Springer, Berlin, (2006).
- [14]Stephan I. Tzenov.Contemporary Accelerator Physics.World Scientific, Singapore, (2004).
- [15]L.D. Landau and E.M. Lifshitz.Mechanics.Elsevier, Amsterdam, (1975).
- [16]H. Goldstein, C.P. Poole and J.L. Safko.The Classical Mechanics.Addison Wesley, San Francisco, Munich, (2008).
- [17]Bahram Houchmandzadeh.The hamilton-jacobi equation: an alternative approach.American Journal of Physics, 88(5):353–359, 2020.
- [18]Stephan I. Tzenov.The method of formal series: Applications to nonlinear beam dynamics and invariants of motion.Journal of Nonlinear Sciences and Applications, 18(1):1–19, 2025.
- [19]Temple H. Fay and P. Hendrik Kloppers.The gibbs’ phenomenon.International Journal of Mathematical Education in Science and Technology, 32(1):73–89, 2001.
- [20]M. Hénon.Numerical study of quadratic area-preserving mappings.Quart. Appl. Math., 27(4):291–312, 1969.
- [21]Ronald C. Davidson, Hong Qin, Stephan I. Tzenov, and Edward A. Startsev.Kinetic description of intense beam propagation through a periodic focusing field for uniform phase-space density.Physical Review ST Accelerators and Beams, 5:084402, 2002.
- [22]S.I. Tzenov and A.A. Volodin.Nonlinear cnoidal waves and formation of patterns and coherent structures in intense charged particle beams.Journal of Technological and Space Plasmas, 5(1):181–193, 2024.
