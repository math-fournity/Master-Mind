# Supersymmetric pairing of Lambert W-kink nerve impulses

**arXiv ID**: 2607.20509v1
**Authors**: M. F. De la Rosa-López, D. M. Galván-Arellano, J. L. Larios-Ferrer, V. A. Mendoza-Millán, O. Pavón-Torres
**Published**: 2026-07-04
**Categories**: physics.bio-ph, nlin.PS
**HTML URL**: https://arxiv.org/html/2607.20509v1

## Abstract

Nerve impulses can be modelled as electromechanical density waves within the improved Heimburg-Jackson model. The inclusion of higher-order polynomial nonlinearities leads to a generalized Boussinesq equation with third and fourth order nonlinearities that, under a traveling-wave reduction, reduces to a Liénard-type equation. Applying a factorization method yields exact Lambert W-kink soliton solutions that represent localized nonlinear density waves near the membrane melting transition. Beyond providing exact solutions, the factorization uncovers an underlying supersymmetric structure. The associated operators satisfy algebraic relations analogous to those of supersymmetric quantum mechanics, thereby enabling the construction of a partner soliton. This supersymmetric pairing establishes a novel and previously unexplored connection between nonlinear electromechanical wave propagation in biological membranes and supersymmetric quantum-mechanical methods. The resulting framework offers a theoretical foundation for analysing mechanically induced perturbations and their nonlinear propagation in nerve membranes, with potential implications for understanding the biomechanical mechanisms underlying traumatic brain injury.

## Full Text

Supersymmetric pairing of Lambert 𝑊–kink nerve impulses

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.20509v1 [physics.bio-ph] 04 Jul 2026

## Supersymmetric pairing of LambertWW–kink nerve impulsesM. F. De la Rosa-López1111mrosal001@alumno.uaemex.mx, D.M. Galván-Arellano2222dulce_galvan@my.uvm.edu.mx, J. L. Larios-Ferrer3333leonel.larios@upenergia.edu.mx,
V. A. Mendoza-Millán1444vmendozam002@alumno.uaemex.mx, O. Pavón-Torres4555omar.pavon@cinvestav.mx(corresponding author)(1Facultad de Ciencias, Universidad Autónoma del Estado de México, Toluca 50200, México
2Universidad del Valle de México, Campus Toluca, Metepec 52164, Mexico
3Universidad Politécnica de la Energía, 42820, Tula de Allende, Hidalgo, México
4Physics Department, Cinvestav, POB 14-740, 07000 México City, México
)

## Abstract

Nerve impulses can be modelled as electromechanical density waves within the improved Heimburg–Jackson model. The inclusion of higher-order polynomial nonlinearities leads to a generalized Boussinesq equation with third and fourth order nonlinearities that, under a traveling-wave reduction, reduces to a Liénard-type equation. Applying a factorization method yields exact LambertWW–kink soliton solutions that represent localized nonlinear density waves near the membrane melting transition. Beyond providing exact solutions, the factorization uncovers an underlying supersymmetric structure. The associated operators satisfy algebraic relations analogous to those of supersymmetric quantum mechanics, thereby enabling the construction of a partner soliton. This supersymmetric pairing establishes a novel and previously unexplored connection between nonlinear electromechanical wave propagation in biological membranes and supersymmetric quantum-mechanical methods. The resulting framework offers a theoretical foundation for analysing mechanically induced perturbations and their nonlinear propagation in nerve membranes, with potential implications for understanding the biomechanical mechanisms underlying traumatic brain injury.

​​​​Keywords—Factorization method, Supersymmetric pairing, LambertWW-Kink solitons.{justify}

## 1Introduction

Signal propagation in excitable cells is governed not only by electrical activity but also by intrinsic physical properties such as axon diameter, myelination, elasticity, and membrane structure, which play a fundamental role in nerve impulse transmission[1,2,3,4,5,6,7,8,9,10]. To account for these features and achieve a more comprehensive description of nerve signal propagation, several theoretical frameworks beyond the classical Hodgkin–Huxley model have been proposed, in which nerve impulses are interpreted as electromechanical waves. These approaches can be broadly classified into four categories: (i) classical electrophysiological models focusing on electrical dynamics[11,12,13,14]; (ii) thermodynamic models addressing energy exchange and heat-related effects[15,16]; (iii) mechanical models incorporating membrane elasticity and density variations[17,18,19]; and (iv) hybrid electromechanical models that explicitly couple electrical and mechanical degrees of freedom[20,21]. More recently, fractal-based approaches have been introduced to capture scale-invariant behaviour and memory effects in neuronal systems, extending continuum descriptions of nerve dynamics[22,23,24]. Collectively, these frameworks have been applied to phenomena such as head-on pulse collisions, anesthesia, mechanosensory responses, phase transitions, refractory effects, and adiabatic signal propagation[25,26,27,28].

In particular, the Heimburg–Jackson (HJ) model provides a unified thermodynamic and mechanical framework for describing nerve signal propagation along the axon. This model has been extensively studied, with significant effort devoted to deriving exact travelling-wave solutions using quasi-analytical methods[29,30,31,32,33,34,35,36]. Within this framework, phase transitions in lipid membranes triggered by action potential propagation have been widely investigated[37]. The associated density waves are commonly described as hyperbolic kink solutions arising from Boussinesq-type equations in both the standard and improved HJ models[38,39,40,41]. More recently, it has been shown that introducing strong nonlinearities in extended versions of the improved HJ model deforms these hyperbolic kink into LambertWW–type kink solitons[42].

In general, such nonlinear extensions render the improved HJ model non-integrable. The resulting governing equation can be reduced to a Liénard-type equation with constant damping, a structure that plays a central role in its analytical treatment. Integrability properties of Liénard-type systems have long been recognized through their connections with scalar field theories such as theϕ4\phi^{4}andϕ6\phi^{6}models[43]. In particular, polynomial nonlinearities and BPS-type reductions allow the second-order dynamics to be mapped into first-order equations derived from energy minimization principles[44]. Alternatively, factorization methods provide a direct algebraic alternative to obtain reduced first-order systems, offering an efficient framework for solving Liénard-type equations[45,46]. This procedure reduces the Liénard equation to an Abel equation of the first kind with constant coefficients, thereby enabling the explicit construction of exact solutions. In this context, factorization under constant damping into a product of two non-commuting first-order differential operators becomes particularly relevant, since the ordering of the operators directly affects the resulting reduced equations and their solvability.

A further consequence of this non-commutative structure is the emergence of paired solution sets associated with reversed operator orderings. In this framework, the Liénard equation admits two related factorized forms, giving rise to partner equations connected through an underlying algebraic transformation[47]. This correspondence induces a structured pairing of solutions that share global dynamical properties, such as propagation velocity, while differing in their profiles and effective parameters. From this perspective, the pairing reflects an algebraic organization of the solution space generated by the nonlinear factorization scheme. Physically, such paired solutions may be interpreted as distinct electromechanical states of the membrane related through effective transformations induced by external perturbations, while the damping parameter fixes the admissible dynamical regime.

Motivated by these considerations, we show that the non-integrable structure of the Liénard equation, under suitable constraints on the nonlinear elastic coefficients, gives rise to LambertWW–type solitons whose multivalued analytic structure is consistent with the breakdown of the Painlevé property. Furthermore, we demonstrate that this structure admits a supersymmetric pairing through factorization, linking the analytic properties of the solutions with their underlying algebraic organization. The remainder of this paper is organized as follows. Section 2 outlines the improved HJ model with higher-order nonlinear terms and its reduction to a Liénard equation, together with a Painlevé integrability analysis. Section 3 presents the implementation of the factorization method and the hierarchy of factorization orders used to construct LambertWW–kink solitons and their supersymmetric partners, along with possible biological interpretations related to pathological damage and specially traumatic brain injury. Finally, Section 4 summarizes our main results and concluding remarks.

## 2Thermodynamic soliton theory of the nerve impulses

Based on the thermodynamic behaviour associated with phase transitions in lipid bilayers and biological membranes, T. Heimburg and A. D. Jackson[15], together with S. T. Andersen et al.[16], proposed a model in which the nerve impulse is described as a nonlinear mechanical density wave propagating along a cylindrical biomembrane, as schematically illustrated in Fig.1.Figure 1:Schematic representation of a cylindrical biomembrane and action potential produced by compression.

Within this framework, the essential mechanism arises from the coupling between mechanical compression and membrane thermodynamics: local variations in density drive a reversible phase transition between the disordered liquid phase and the ordered gel phase. Consequently, the action potential can be interpreted as a localized compression pulse intrinsically linked to this phase transition. Moreover, due to the thermodynamic reversibility of the process, the inverse scenario is also admissible: local cooling may induce a transition toward the ordered phase, thereby generating a propagating density perturbation[16].

In the present work, and in order to achieve our main objective, namely, to obtain and interpret the supersymmetric pairing of LambertWW–kink solitons, we adopt the following extended version of the HJ model[48]. To this end, letu=ρA−ρ0Au=\rho^{A}-\rho_{0}^{A}denote the longitudinal density change, defined as the difference between the lateral mass density of the membraneρA\rho^{A}and its empirical equilibrium valueρ0A\rho_{0}^{A}. The governing equation is given by:∂2u∂t2=∂∂x​([c02+α​u+β​u2+ϵ​u3+λ​u4]​∂u∂x)−h1​∂4u∂x4+h2​∂4u∂x2​∂t2+μ​∂2∂x2​(∂u∂t).\dfrac{\partial^{2}u}{\partial{t}^{2}}=\dfrac{\partial}{\partial x}\left(\left[c_{0}^{2}+\alpha u+\beta u^{2}+\epsilon u^{3}+\lambda u^{4}\right]\dfrac{\partial u}{\partial x}\right)-h_{1}\dfrac{\partial^{4}u}{\partial x^{4}}+h_{2}\dfrac{\partial^{4}u}{\partial x^{2}\partial t^{2}}+\mu\dfrac{\partial^{2}}{\partial x^{2}}\left(\dfrac{\partial u}{\partial t}\right).(1)

The model is grounded on two key physical assumptions: (i) the existence of a phase transition in lipid bilayers, and (ii) the analogy between nerve impulse propagation and sound waves in a compressible membrane. The latter is evident from Eq. (1), which reduces to a linear wave equation upon neglecting the terms proportional toα\alpha,β\beta,ϵ\epsilon,λ\lambda,h1h_{1},h2h_{2}andμ\mu. In the present limit of Eq. (1), the propagation velocityccis directly linked to the lateral compressibility, consistent with the original HJ hypothesis. Specifically, the sound speed in the fluid phase of the membrane is given byc0=1/KsA​ρ0Ac_{0}=1/\sqrt{K_{s}^{A}\rho_{0}^{A}}, whereKsAK_{s}^{A}is the lateral compressibility. The nonlinear elastic coefficientsα\alpha,β\beta,ϵ\epsilon, andλ\lambdaare empirically determined parameters that encode distinct mechanical contributions, including lateral compressibility and membrane stretching, lipid rarefaction, compositional heterogeneity arising from lipid–protein interactions, and large-scale deformations induced by compressive and tensile stresses. The term proportional toh1h_{1}represents the intrinsic elastic response of the biomembrane, whereas theh2h_{2}term accounts for the inertial effects associated with lipid motion. Its inclusion promotes the HJ equation to a double-dispersion model, thereby mitigating the instabilities that typically emerge in formulations involving only spatial dispersion. Finally, the term proportional toμ\mumodels viscous dissipation due to the surrounding axoplasmic fluid.

## 2.1Density wave equation

In order to study the supersymmetric pairing of LambertWW-kink soliton solutions, we consider the following re-parametrization:z=uρ0A,ζ=c0​xh1,and​t~=c02​th1,z=\dfrac{u}{\rho_{0}^{A}},\quad\zeta=\dfrac{c_{0}x}{\sqrt{h_{1}}},\quad\text{and}\quad\tilde{t}=\dfrac{c_{0}^{2}t}{\sqrt{h_{1}}},(2)

together withp=α​ρ0Ac02;q=β​(ρ0A)2c02;r=ϵ​(ρ0A)3c02;s=λ​(ρ0A)4c02;p=\dfrac{\alpha\rho_{0}^{A}}{c_{0}^{2}};\quad q=\dfrac{\beta(\rho_{0}^{A})^{2}}{c_{0}^{2}};\quad r=\dfrac{\epsilon(\rho_{0}^{A})^{3}}{c_{0}^{2}};\quad s=\dfrac{\lambda(\rho_{0}^{A})^{4}}{c_{0}^{2}};γ=μh1​and​δ=h2​c02h1,\gamma=\dfrac{\mu}{\sqrt{h_{1}}}\quad\text{and}\quad\delta=\dfrac{h_{2}c_{0}^{2}}{h_{1}},(3)

which leads to the following dimensionless form of Eq. (1)∂2z∂t~2=∂∂ζ​([1+p​z+q​z2+r​z3+s​z4]​∂z∂ζ)−∂4z∂ζ4+δ​∂4z∂ζ2​∂t~2+γ​∂3z∂ζ2​∂t~.\dfrac{\partial^{2}z}{\partial\tilde{t}^{2}}=\dfrac{\partial}{\partial\zeta}\left(\left[1+pz+qz^{2}+rz^{3}+sz^{4}\right]\dfrac{\partial z}{\partial\zeta}\right)-\dfrac{\partial^{4}z}{\partial\zeta^{4}}+\delta\dfrac{\partial^{4}z}{\partial\zeta^{2}\partial\tilde{t}^{2}}+\gamma\dfrac{\partial^{3}z}{\partial\zeta^{2}\partial\tilde{t}}.(4)

To find travelling wave solutions of Eq. (4), we considerz​(ξ)z(\xi)withξ=k​ζ−v​t~\xi=k\zeta-v\tilde{t}, wherekkandvvare real constants. After two successive integrations, followed by an appropriate rescaling and setting the integration constants to zero without loss of generality, we obtaind2​yd​ξ2+γ~​d​yd​ξ−a1​y+a2​y2−a3​y3−a4​y4−y5=0,\dfrac{d^{2}y}{d\xi^{2}}+\tilde{\gamma}\dfrac{dy}{d\xi}-a_{1}y+a_{2}y^{2}-a_{3}y^{3}-a_{4}y^{4}-y^{5}=0,(5)

where the rescaled dependent variable is given byz=1s~1/4​y.z=\dfrac{1}{\tilde{s}^{1/4}}y.(6)

Additionally, the re-parameterized and rescaled constantsγ~\tilde{\gamma},s~\tilde{s}andaia_{i}(i=1,…,4i=1,...,4) are defined byγ~=v​γΛ;a1=k2−v2Λ​k2;a2=p2​Λ​s~1/4;\displaystyle\tilde{\gamma}=\dfrac{v\gamma}{\Lambda};\qquad a_{1}=\dfrac{k^{2}-v^{2}}{\Lambda k^{2}};\qquad a_{2}=\dfrac{p}{2\Lambda\tilde{s}^{1/4}};a3=q3​Λ​s~1/2;a4=r4​Λ​s~3/4;s~=s5​Λ,\displaystyle a_{3}=\dfrac{q}{3\Lambda\tilde{s}^{1/2}};\qquad a_{4}=\dfrac{r}{4\Lambda\tilde{s}^{3/4}};\qquad\tilde{s}=\dfrac{s}{5\Lambda},(7)

withΛ=k2−δ​v2\Lambda=k^{2}-\delta v^{2}.

The density-wave equation given in Eq. (5) constitutes a generalized Liénard-type equation with higher-order nonlinearities, thereby providing a natural framework for the emergence of nontrivial travelling-wave solutions. It is worth noting that the reduced form of the improved HJ model, obtained by neglecting theϵ\epsilonandλ\lambdaterms in Eq. (1), has been extensively studied in the literature over a wide range of nonlinear elastic parameters, including regimes lacking physical relevance. In the present work, however, we restrict our analysis to parameter ranges appropriate for biomembranes, namelyp<0p<0andq>0q>0in Eq. (7). These values correspond to a nonlinear equation of state capable of supporting density-driven phase transitions between the fluid and gel phases, a feature encoded in the polynomial structure of Eq. (5). A detailed discussion of the physical significance and values of these parameters can be found in[42].

In particular, the polynomial structure of Eq. (5) admits a factorization procedure that underlies a supersymmetric pairing of solutions, among them LambertWW–kink solitons. Prior to constructing this supersymmetric framework, we examine the integrability properties of Eq. (5) through the Painlevé test in the Kovalevskaya form, as originally proposed by S. V. Kovalevskaya[49,50].

## 2.2Painlevé test of integrability

The Painlevé analysis begins by assuming a local solution of Eq. (5) in the form of a Laurent seriesy​(ξ)=∑k¯=0∞a¯k¯​(ξ−ξ0)k¯−p¯,y(\xi)=\sum_{\bar{k}=0}^{\infty}\bar{a}_{\bar{k}}(\xi-\xi_{0})^{\bar{k}-\bar{p}},(8)

whereξ0\xi_{0}denotes the location of the movable singularity,p¯\bar{p}characterizes the leading-order behaviour, anda¯k¯\bar{a}_{\bar{k}}are expansion coefficients.

The Painlevé test can be summarized in the following three steps[51]:
- 1.

We determine the leading-order behaviour of the solution near a movable singularity by performing a dominant balance666If the leading exponentp¯\bar{p}is not an integer, the expansion becomes of Puiseux type, indicating the presence of movable branch points rather than poles; consequently, the equation fails the Painlevé test..
- 2.

We compute the Fuchs indices (resonances) associated with this leading-order behaviour.
- 3.

We substitute the corresponding Laurent expansion into the original equation to verify the consistency of the recursion relations at the resonance levels.

To implement this procedure, we first shift the singularity to the origin by introducingξ→ξ−ξ0\xi\to\xi-\xi_{0}. We then seek the dominant behaviour in the formy​(ξ)=a¯0​ξ−p¯,y(\xi)=\bar{a}_{0}\xi^{-\bar{p}},(9)

and substitute it into the dominant part of Eq. (5), namelyd2​yd​ξ2−y5=0.\dfrac{d^{2}{y}}{d\xi^{2}}-y^{5}=0.(10)

This yields(a¯0,p¯)=(±344,12)(\bar{a}_{0},\bar{p})=\left(\pm\sqrt[4]{\dfrac{3}{4}},\dfrac{1}{2}\right). Sincep¯=1/2\bar{p}=1/2is non-integer, the movable singularity is a branch point rather than a pole. Consequently, Eq. (5) fails the Painlevé test and is therefore non-integrable in the Painlevé sense. This suggests that globally meromorphic solutions are not expected in general and that alternative analytical techniques may be required.

Although the failure occurs already at the level of the leading-order analysis, it is still informative to compute the associated resonances, as they provide insight into the structure of the local (generally multivalued) solutions. The Painlevé test provides information about the analytic structure of solutions rather than a definitive criterion for solvability.

In particular, the Fuchs indices (resonances) indicate the positions at which arbitrary constants may enter the local expansion and whether compatibility conditions are satisfied. If the leading-order exponent and all resonances are integer-valued, and the recursion relations are compatible at every resonance level, then the equation may possess the Painlevé property and admit locally single-valued expansions around movable singularities.

To determine the associated resonances, we substitute the valuesa¯0\bar{a}_{0}andp¯\bar{p}obtained from the preceding step in Eq. (8) to yieldy​(ξ)=±344​ξ−1/2+a¯j​ξj−1/2.y(\xi)=\pm\sqrt[4]{\dfrac{3}{4}}\xi^{-1/2}+\bar{a}_{j}\xi^{j-1/2}.(11)

Substituting Eq. (11) into Eq. (10) and collecting terms linear ina¯j\bar{a}_{j}yieldsj2−2​j−3=0j^{2}-2j-3=0(12)

and, consequently, the resonances arej1=−1j_{1}=-1andj2=3j_{2}=3. The resonancej=−1j=-1corresponds to the arbitrariness of the singularity positionξ0\xi_{0}, whilej=3j=3indicates the presence of a free parameter entering the local Puiseux expansion. Despite the non-integer leading exponent, these resonances suggest a structured local behaviour of solutions near movable singularities. From this result, it is clear that the coefficienta¯3\bar{a}_{3}remains arbitrary in the local Puiseux expansion. The failure of the Painlevé property indicates that Eq. (5) is not integrable in the Painlevé sense. Nevertheless, this does not exclude the existence of particular exact solutions. Instead, it suggests that alternative approaches, such as suitable ansätze[52], parameter constraints, or factorization methods, are more appropriate for constructing explicit solutions. In this context, the emergence of LambertWW-function solutions is particularly natural, since the branch-point structure of the LambertWWfunction mirrors the multivalued local behaviour predicted by the Painlevé analysis.

## 3Electromechanical waves in the nerve membranes

## 3.1The factorization method

As previously mentioned, the factorization method provides a systematic and efficient framework for treating ordinary differential equations with polynomial nonlinearities that are not integrable in the Painlevé sense, such as Eq. (5). Its effectiveness has been demonstrated in a wide range of nonlinear problems whose governing equations possess a polynomial structure. In contrast to quasi-analytical techniques and approaches based on the inverse scattering transform, the method is more straightforward to implement while still capturing the essential features of the nonlinear dynamics. Consequently, it has found numerous applications in gravitation, biophysics, integrability theory, and mathematical physics[53,54,55,56].

To outline the method, consider a nonlinear differential equation of the formd2​yd​ξ2+γ~​d​yd​ξ+f​(y)=0,\dfrac{d^{2}y}{d\xi^{2}}+\tilde{\gamma}\dfrac{dy}{d\xi}+f(y)=0,(13)

which can be interpreted as a damped nonlinear oscillator, whereγ~\tilde{\gamma}is a dissipation parameter andf​(y)f(y)is a nonlinear polynomial function.
The key idea consists in factorizing Eq. (13) as a product of first-order differential operators:[dd​ξ−ϕ2​(y)]​[dd​ξ−ϕ1​(y)]​y=0.\left[\dfrac{d}{d\xi}-\phi_{2}(y)\right]\left[\dfrac{d}{d\xi}-\phi_{1}(y)\right]y=0.(14)

Expanding Eq. (14) and matching coefficients with Eq. (13) leads to the consistency conditionsϕ1​(y)​ϕ2​(y)=f​(y)y,\phi_{1}(y)\phi_{2}(y)=\dfrac{f(y)}{y},(15a)ϕ1​(y)+ϕ2​(y)+y​d​ϕ1d​y=−γ~.\phi_{1}(y)+\phi_{2}(y)+y\dfrac{d\phi_{1}}{dy}=-\tilde{\gamma}.(15b)

A particularly tractable class of solutions is obtained by imposing the first-order compatibility condition[dd​ξ−ϕ1​(y)]​y=0,\left[\dfrac{d}{d\xi}-\phi_{1}(y)\right]y=0,(16)

which reduces the original second-order equation to a nonlinear first-order equation. Although this choice corresponds to the simplest factorization branch, it already yields nontrivial solution families.

It is worth emphasizing that Eq. (16) is not unique: alternative factorizations may generate different solution branches, potentially involving functions ofξ\xialone or extended dependencies (e.g.,ξ\xiandtt)[57,58]. This framework has been previously explored in the context of the Liénard equation, particularly in cases where commutativity of the factorizing operators leads to significant simplifications and, in special instances, to isochronous systems[59].

## 3.2LambertWW-Kink-type solitons

Following the ideas of our previous work[42], and in order to obtain directly the LambertWW-Kink solitons, we consider the following form of Eq. (5):d2​yd​ξ2+γ~​d​yd​ξ+(y−α)2​(−y2+A​y+B)​y=0,\dfrac{d^{2}y}{d\xi^{2}}+\tilde{\gamma}\dfrac{dy}{d\xi}+(y-\alpha)^{2}(-y^{2}+Ay+B)y=0,(17)

whereAA,BBandα\alphaare obtained by solving the following overdetermined system of equations:−a4=A+2​α;-a_{4}=A+2\alpha;(18a)−a3=B−2​α​A−α2;-a_{3}=B-2\alpha A-\alpha^{2};(18b)a2=−2​α​B+A​α2;a_{2}=-2\alpha B+A\alpha^{2};(18c)−a1=α2​B.-a_{1}=\alpha^{2}B.(18d)

Moreover, sinceα\alphaappears explicitly in Eqs. (18a)-(18d), the coefficientsAAandBBcan be parametrized in terms of this quantity, so that determiningα\alphacompletely characterizes the factorized polynomial structure. It is particularly convenient to expressα\alphasolely in terms of the coefficientsa2a_{2},a3a_{3}anda4a_{4}, as these parameters are directly associated with the elastic properties of the nerve membrane. To this end, substituting Eqs. (18a) and (18b) into Eq. (18c) yields the following cubic algebraic equation forα\alpha:α3+34​a4​α2+12​a3​α−14​a2=0,\alpha^{3}+\dfrac{3}{4}a_{4}\alpha^{2}+\dfrac{1}{2}a_{3}\alpha-\dfrac{1}{4}a_{2}=0,(19)

and generally admits multiple roots. In the present work, we restrict our attention to real and non-vanishing values ofα\alphato exclude complex and trivial solutions that lack a direct physical interpretation. The nature of the roots of Eq. (19) is fully determined by its discriminant. To characterize the admissible parameter regions, we employ Cardano’s method and introduce the invariantsPPandQQ, defined asP=12​a3−316​a42P=\dfrac{1}{2}a_{3}-\dfrac{3}{16}a_{4}^{2}(20)

andQ=132​a43−18​a4​a3−14​a2Q=\dfrac{1}{32}a_{4}^{3}-\dfrac{1}{8}a_{4}a_{3}-\dfrac{1}{4}a_{2}(21)

whereaia_{i}(i=1,2,3,4i=1,2,3,4) can be expressed in terms of the original elastic coefficients by means of Eqs.(7)(\ref{arthur1}). Additionally, we express its discriminant as:D=(Q2)2+(P3)3,D=\left(\dfrac{Q}{2}\right)^{2}+\left(\dfrac{P}{3}\right)^{3},(22)

According to the trichotomy of the cubic discriminant, we know thatDDmay be either positive (D>0D>0), negative (D<0D<0) or zero (D=0D=0), which yields one real root, three real roots or multiple real root (double or triple). The conditionD<0D<0guarantees three distinct real solutions for the parameterα\alpha. Through the factorization (17), these solutions determine distinct real configurations of the polynomial nonlinearity and therefore generate multiple admissible equilibrium structures for the reduced dynamical system. Such multistability is a necessary condition for the construction of heteroclinic trajectories connecting different asymptotic states[60]. Since LambertWW-kink solitons arise precisely from these heteroclinic connections, the regionD<0D<0defines a necessary existence domain for this class of solutions. In contrast, the regimeD>0D>0yields a single real solution forα\alpha, corresponding to a monostable polynomial structure in which heteroclinic connections between distinct equilibrium states cannot be constructed. Consequently, the conditionD=0D=0represents the coalescence of real roots and may therefore be interpreted as a critical threshold separating the soliton-supporting (D<0D<0) and monostable (D>0D>0) regimes.
Thus, once an admissible real root forα\alpha, given by the Cardano formulaα=−a44+−Q2+D3+−Q2−D3,\alpha=-\dfrac{a_{4}}{4}+\sqrt[3]{-\dfrac{Q}{2}+\sqrt{D}}+\sqrt[3]{-\dfrac{Q}{2}-\sqrt{D}},(23)

has been selected, the coefficientsAAandBBare uniquely determined, thereby completely specifying the factorized representation in (17). As will become evident in the following sections, an additional constraint onAAandBBarises from the commutation relations between the differential factors. For the particular form of Eq. (17), preserving a constant damping coefficient in Eq. (15b) restricts the nonlinear polynomial functionf​(y)/yf(y)/y, factorized asϕ1​(y)​ϕ2​(y)\phi_{1}(y)\phi_{2}(y)in Eq. (15a), to two admissible factorizations.

## 3.2.1Case I.

Under the choice ofϕ1​(y)\phi_{1}(y)andϕ2​(y)\phi_{2}(y)ϕ1​(y)=±13​(y−α)2;ϕ2​(y)=±3​(−y2+A​y+B),\phi_{1}(y)=\pm\dfrac{1}{\sqrt{3}}(y-\alpha)^{2};\qquad\phi_{2}(y)=\pm\sqrt{3}(-y^{2}+Ay+B),(24)

the first allowed factorization is defined. Consequently,AA,BBandγ~1\tilde{\gamma}_{1}can be obtained from the factorization condition (15b), yieldingA=43​α;B=−a3+113​α2;A=\dfrac{4}{3}\alpha;\qquad B=-a_{3}+\dfrac{11}{3}\alpha^{2};(25a)andγ~1=±3​[a3−4​α2].\tilde{\gamma}_{1}=\pm\sqrt{3}\left[a_{3}-4\alpha^{2}\right].(25b)

In addition, from the compatibility condition, given by Eq. (16), we haved​yd​ξ=±13​(y−α)2​y\dfrac{dy}{d\xi}=\pm\dfrac{1}{\sqrt{3}}(y-\alpha)^{2}y(26)

and, upon integrating, we obtain the following form of the LambertWW-kink solitony1(1)​(ξ)=α​(1−11+W​[φ1​(ξ)]),y_{1}^{(1)}(\xi)=\alpha\left(1-\dfrac{1}{1+W\left[\varphi_{1}(\xi)\right]}\right),(27)

whereφ1​(ξ)=exp⁡(±α23​ξ−1)\varphi_{1}(\xi)=\exp\left(\pm\dfrac{\alpha^{2}}{\sqrt{3}}\xi-1\right)(28)

withW​(φ1​(ξ))W(\varphi_{1}(\xi))being the LambertWWfunction, defined as the inverse function off​(W)=W​eWf(W)=We^{W}andα\alphais determined by the real roots of Eq. (23), whose graphical representation is presented in Fig.4. The expressions of Eq. (27) for large values ofξ\xiare{y1(1)​(ξ)→α​(1−3α2​ξ)if​ξ→∞,y1(1)​(ξ)→α​exp⁡(α23​ξ−1)if​ξ→−∞,\begin{cases}y_{1}^{(1)}(\xi)\to\alpha\left(1-\dfrac{\sqrt{3}}{\alpha^{2}\xi}\right)&\text{if}\qquad\xi\to\infty,\\
\\
y_{1}^{(1)}(\xi)\to\alpha\exp\left(\dfrac{\alpha^{2}}{\sqrt{3}}\xi-1\right)&\text{if}\qquad\xi\to-\infty,\\
\end{cases}

which are consistent with those obtained within the framework of theϕ6\phi^{6}model. In the large-ξ\xiregime, the LambertWW-kink soliton exhibits a long-range, power-law decay, in contrast to the opposite side, where the asymptotic behaviour is exponential[44]. It is clear that the asymptotic behaviour of the LambertWW-kink soliton in the limit of largeξ\xiis determined by the choice of sign inφ1​(ξ)\varphi_{1}(\xi), given by Eq. (28), which effectively interchanges the corresponding asymptotic expressions.

## 3.2.2Case II.

Alternatively, choosing the inverted order ofϕ1​(y)\phi_{1}(y)andϕ2​(y)\phi_{2}(y)from Eq. (15a), with explicit forms obtained from the factorization of Eq. (17), yieldsϕ1​(y)=±13​(−y2+A​y+B);ϕ2​(y)=±3​(y−α)2.\phi_{1}(y)=\pm\dfrac{1}{\sqrt{3}}(-y^{2}+Ay+B);\qquad\phi_{2}(y)=\pm\sqrt{3}(y-\alpha)^{2}.(29)

Consequently, the factorization condition(15b)(\ref{ferrer6})determinesAA,BBandγ~2\tilde{\gamma}_{2}asA=3​α;B=−a3+7​α2A=3\alpha;\qquad B=-a_{3}+7\alpha^{2}(30a)andγ~2=±13​[a3−10​α2].\tilde{\gamma}_{2}=\pm\dfrac{1}{\sqrt{3}}\left[a_{3}-10\alpha^{2}\right].(30b)

Thus, the compatibility condition, given by Eq. (16), can be expressed asd​yd​ξ=±13​(−y2+A​y+B)​y,\dfrac{dy}{d\xi}=\pm\dfrac{1}{\sqrt{3}}(-y^{2}+Ay+B)y,(31)

which yields three distinct solution classes, depending on the parameter values.1B​ln⁡[y2>(1)−(y2>(1))2+A​y2>(1)+B]−AΔ​B​arctanh​(2​y2>(1)−AΔ)=±13​(ξ−ξ0),if​Δ>0;\dfrac{1}{B}\ln\left[\dfrac{y_{2>}^{(1)}}{\sqrt{-\left(y_{2>}^{(1)}\right)^{2}+Ay_{2>}^{(1)}+B}}\right]-\dfrac{A}{\sqrt{\Delta}B}\text{arctanh}\left(\dfrac{2y_{2>}^{(1)}-A}{\sqrt{\Delta}}\right)=\pm\dfrac{1}{\sqrt{3}}(\xi-\xi_{0}),\quad\text{if }\quad\Delta>0;(32a)1B​ln⁡[y2<(1)−(y2<(1))2+A​y2<(1)+B]+AΔ​B​arctan⁡(2​y2<(1)−AΔ)=±13​(ξ−ξ0),if​Δ<0;\dfrac{1}{B}\ln\left[\dfrac{y_{2<}^{(1)}}{\sqrt{-\left(y_{2<}^{(1)}\right)^{2}+Ay_{2<}^{(1)}+B}}\right]+\dfrac{A}{\sqrt{\Delta}B}\arctan\left(\dfrac{2y_{2<}^{(1)}-A}{\sqrt{\Delta}}\right)=\pm\dfrac{1}{\sqrt{3}}(\xi-\xi_{0}),\quad\text{if}\quad\Delta<0;(32b)y2=(1)​(ξ)=3​α2​(1−11+W​[φ2​(ξ)])​with​φ2​(ξ)=exp⁡(∓3​34​α2​ξ−1),if​Δ=0;y_{2=}^{(1)}(\xi)=\dfrac{3\alpha}{2}\left(1-\dfrac{1}{1+W\left[\varphi_{2}(\xi)\right]}\right)\quad\text{with}\quad\varphi_{2}(\xi)=\exp\left(\mp\dfrac{3\sqrt{3}}{4}\alpha^{2}\xi-1\right),\quad\text{if }\quad\Delta=0;(32c)

whereΔ=A2+4​B\Delta=A^{2}+4B, denotes the discriminant of the quadratic polynomial−y2+A​y+B-y^{2}+Ay+B, withAAandBBgiven by Eqs. (30a), which explicity can be expressed asΔ=α2−4​a3/37\Delta=\alpha^{2}-{4a_{3}}/{37}.

As it is evident from the case yielded by Eq. (32c) whereΔ=0\Delta=0, the arising of the LambertWW-kink-type solitons is not restricted to the particular choice of a given form of the polynomial nonlinearity in Eq. (17), the restrictions to yield LambertWW-kink solitons will appear directly as a particular case of the product of two second order general polynomial of the formA2​y2+A1​y+A0A_{2}y^{2}+A_{1}y+A_{0}such as the mentioned in[42](footnote pag. 8). The other remaining casesΔ>0\Delta>0andΔ<0\Delta<0, depicted in Figs.2a and2b, for which we obtain the transcendental functions Eq. (32a) and Eq. (32b) are known solutions of the Abel equation of first type with constant coefficients. As it can be seen represented graphically these solutions will lead to a kink-like behaviour (Eq. (32a)) or to a periodic behaviour (32b) forΔ>0\Delta>0andΔ<0\Delta<0, correspondingly.

Again for large values ofξ\xithe LambertWW-kink soliton, expressed by Eq. (32c) and depicted in Fig.7, is{y2=(1)​(ξ)→32​α​(1−43​3​α2​ξ)if​ξ→∞,y2=(1)​(ξ)→32​α​exp⁡(3​34​α2​ξ−1)if​ξ→−∞,\begin{cases}y_{2=}^{(1)}(\xi)\to\dfrac{3}{2}\alpha\left(1-\dfrac{4}{3\sqrt{3}\alpha^{2}\xi}\right)&\text{if}\qquad\xi\to\infty,\\
\\
y_{2=}^{(1)}(\xi)\to\dfrac{3}{2}\alpha\exp\left(\dfrac{3\sqrt{3}}{4}\alpha^{2}\xi-1\right)&\text{if}\qquad\xi\to-\infty,\\
\end{cases}

which are similar to the previously obtained for the LambertWW-kink soliton of Case I.

(a)(b)Figure 2:(a) Graphical representation of the transcendental functions corresponding toΔ>0\Delta>0(y2>(1)​(ξ)y_{2>}^{(1)}(\xi)) andΔ<0\Delta<0(y2<(1)​(ξ)y_{2<}^{(1)}(\xi)) provided by Eqs. (32a) and (32b), correspondingly. The chosen parameters fory2>(1)​(ξ)y_{2>}^{(1)}(\xi)arep=q=500p=q=500,s=135s=135,r=−250r=-250,k=2k=2,δ=v=1\delta=v=1andξ0=0\xi_{0}=0and fory2<(1)​(ξ)y_{2<}^{(1)}(\xi)arep=q=500p=q=500,s=60s=60,r=−170r=-170,k=2k=2,δ=v=1\delta=v=1andξ0=0\xi_{0}=0. (b) Region of existence at(r,s)(r,s)fory2>(1)​(ξ)y_{2>}^{(1)}(\xi)andy2<(1)​(ξ)y_{2<}^{(1)}(\xi).

We remark that, throughout this and the following section, we adopt the simplified notationy1>(1)y^{(1)}_{1>}. In accordance with the standard supersymmetric quantum mechanics (SUSY QM) convention, the first subscript labels the solution corresponding to case I or II, the second subscript indicates the relevant branch when applicable, and the superscript specifies the associated potential. In the present section, the superscript (1) refers to the potential defined by Eq. (17); the supersymmetric partner solutions associated with the second potential will be denoted by the superscript (2).

## 3.3Supersymmetric pairing of LambertWW-kink-type solitons

In the previous section, we have implicitly shown that the factorization conditions Eqs.(15a)(\ref{ferrer5})and(15b)(\ref{ferrer6})are not commutative. Thus, the ordering of the differential operators in Eq. (14) is essential. Consequently, a direct reversing ofϕ1​(y)\phi_{1}(y)andϕ2​(y)\phi_{2}(y), maintaining the damping coefficient constant, eitherγ~1\tilde{\gamma}_{1}for the case I orγ~2\tilde{\gamma}_{2}for the case II, will lead to a system described by a completely different equation. This property was termed, by the authors of the factorization method for nonlinear differential equations, assupersymmetric pairing[47]. However, their analysis was restricted to conventional kink solitons, without exploring in detail the physical interpretation of the associated partner equations. Therefore, in the present section we extend this idea to the LambertWW-kink solitons obtained from the extended HJ model and offer a possible physical interpretation relevant to traumatic brain injury for the additional terms that appear.

## 3.3.1Case I.

By direct reversingϕ1​(y)\phi_{1}(y)andϕ2​(y)\phi_{2}(y), given by Eqs. (24), namely,ϕ1​(y)=±3​(−y2+A​y+B);ϕ2​(y)=±13​(y−α)2,\phi_{1}(y)=\pm\sqrt{3}(-y^{2}+Ay+B);\qquad\phi_{2}(y)=\pm\dfrac{1}{\sqrt{3}}(y-\alpha)^{2},(33)

andAA,BBandγ~1\tilde{\gamma}_{1}, given by Eqs. (25a) and Eq. (25b). The compatibility condition (16) now reads as:d​yd​ξ=±3​(−y2+A​y+B)​y.\dfrac{dy}{d\xi}=\pm\sqrt{3}(-y^{2}+Ay+B)y.(34)

Thus, depending on the values of the constantsAAandBBdefined in (25a), we obtain three solutions:1B​ln⁡[y1>(2)−(y1>(2))2+A​y1>(2)+B]−AΔ​B​arctanh​(2​y1>(2)−AΔ)=±3​(ξ−ξ0),if​Δ>0;\dfrac{1}{B}\ln\left[\dfrac{y_{1>}^{(2)}}{\sqrt{-\left(y_{1>}^{(2)}\right)^{2}+Ay_{1>}^{(2)}+B}}\right]-\dfrac{A}{\sqrt{\Delta}B}\text{arctanh}\left(\dfrac{2y_{1>}^{(2)}-A}{\sqrt{\Delta}}\right)=\pm\sqrt{3}(\xi-\xi_{0}),\quad\text{if }\quad\Delta>0;(35a)1B​ln⁡[y1>(2)−(y1>(2))2+A​y1>(2)+B]+AΔ​B​arctan⁡(2​y1>(2)−AΔ)=±3​(ξ−ξ0),if​Δ<0;\dfrac{1}{B}\ln\left[\dfrac{y_{1>}^{(2)}}{\sqrt{-\left(y_{1>}^{(2)}\right)^{2}+Ay_{1>}^{(2)}+B}}\right]+\dfrac{A}{\sqrt{\Delta}B}\arctan\left(\dfrac{2y_{1>}^{(2)}-A}{\sqrt{\Delta}}\right)=\pm\sqrt{3}(\xi-\xi_{0}),\quad\text{if }\quad\Delta<0;(35b)y1=(2)​(ξ)=2​α3​(1−11+W​[φ1′​(ξ)])​with​φ1′​(ξ)=exp⁡(∓43​3​α2​ξ−1),if​Δ=0y_{1=}^{(2)}(\xi)=\dfrac{2\alpha}{3}\left(1-\dfrac{1}{1+W\left[\varphi_{1^{\prime}}(\xi)\right]}\right)\quad\text{with}\quad\varphi_{1^{\prime}}(\xi)=\exp\left(\mp\dfrac{4}{3\sqrt{3}}\alpha^{2}\xi-1\right),\quad\text{if }\quad\Delta=0(35c)

withΔ=A2+4​B\Delta=A^{2}+4B, whereAAandBBare defined in Eqs. (25a). The solutions given by Eqs. (35a), (35b) and (35c) constitute supersymmetric partners of the LambertWW-kink soliton (27).

To make the supersymmetric pairing more transparent in its original formulation, namely, by considering the same wavefront velocity in the diffusion equation (13), we focus on the LambertWW-kink solutions given by Eqs. (27) and (35c). This representation enables a direct comparison of how the fundamental soliton parameters are transformed between the two supersymmetric partners. As shown in Fig.4, both LambertWW-kink solutions preserve the damping coefficientγ~\tilde{\gamma}, which is associated with the axoplasmic fluid, while differing only in the direction of propagation.

To compare solitons propagating in the same direction, opposite sign conventions must be adopted in Eqs. (27) and (35c). The resulting correspondence is illustrated schematically in Fig.5. Under this convention, the supersymmetric transformation produces significant changes in the soliton amplitude and width. By contrast, the supersymmetric partner solutions of the LambertWW-kink soliton (27), given by Eq. (35a) forΔ>0\Delta>0and Eq. (35b) forΔ<0\Delta<0, exhibit a considerably stronger deformation. As illustrated in Figs.3a and3b, this behaviour reflects the deformation of the corresponding effective potential and is manifested through their transcendental profiles and regions of existence.

(a)(b)Figure 3:(a) Graphical representation of the transcendental functions corresponding toΔ>0\Delta>0(y1>(2)​(ξ)y_{1>}^{(2)}(\xi)) andΔ<0\Delta<0(y1<(2)​(ξ)y_{1<}^{(2)}(\xi)) provided by Eqs. (35a) and (35b), correspondingly. The chosen parameters fory1>(2)​(ξ)y_{1>}^{(2)}(\xi)arep=q=300p=q=300,s=250s=250,r=−400r=-400,k=2k=2,δ=v=1\delta=v=1andξ0=0\xi_{0}=0and fory1<(2)y_{1<}^{(2)}arep=q=300p=q=300,s=100s=100,r=200r=200,k=2k=2,δ=v=1\delta=v=1andξ0=0\xi_{0}=0. (b) Region of existence at(r,s)(r,s)fory1>(2)​(ξ)y_{1>}^{(2)}(\xi)andy1<(2)​(ξ)y_{1<}^{(2)}(\xi).

This modified effective potential can be obtained through a direct substitution of Eq. (33) into Eq. (14), withγ~1\tilde{\gamma}_{1}given by Eq. (25b). The resulting expression yields the supersymmetric partner equation, which can be written asd2​yd​ξ2∓γ~1​d​yd​ξ+(9​y2−8​α​y+α2)​(−y2+A​y+B)​y=0.\dfrac{d^{2}y}{d\xi^{2}}\mp\tilde{\gamma}_{1}\dfrac{dy}{d\xi}+(9y^{2}-8\alpha y+\alpha^{2})(-y^{2}+Ay+B)y=0.(36)

In general, this reversing in the order ofϕ1​(y)\phi_{1}(y)andϕ2​(y)\phi_{2}(y)and its corresponding partner equation, can be seen as a modulation of the original potential, which causes the potential to modified or, in a more drastic case, may be interpreted as an effective modulation of the membrane potential induced by external mechanical perturbations. Considering Eq. (36), together with the mechanical analogy, we can find the potentialV1​(y)V_{1}(y)and the supersymmetric partner potentialV2​(y)V_{2}(y)forγ~1\tilde{\gamma}_{1}, given by Eq. (25b), to have the explicit formsV1​(y)=16​y6−A+2​α5​y5+α2+2​A​α−B4​y4+2​α​B−A​α23​y3−B​α22​y2V_{1}(y)=\dfrac{1}{6}y^{6}-\dfrac{A+2\alpha}{5}y^{5}+\dfrac{\alpha^{2}+2A\alpha-B}{4}y^{4}+\dfrac{2\alpha B-A\alpha^{2}}{3}y^{3}-\dfrac{B\alpha^{2}}{2}y^{2}(37a)V2​(y)=32​y6−9​A+8​α5​y5+α2+8​A​α−9​B4​y4+8​α​B−A​α23​y3−B​α22​y2V_{2}(y)=\dfrac{3}{2}y^{6}-\dfrac{9A+8\alpha}{5}y^{5}+\dfrac{\alpha^{2}+8A\alpha-9B}{4}y^{4}+\dfrac{8\alpha B-A\alpha^{2}}{3}y^{3}-\dfrac{B\alpha^{2}}{2}y^{2}(37b)

withAAandBBgiven by Eqs. (25a), correspondingly. Once we depict the potentialsV1​(y)V_{1}(y)andV2​(y)V_{2}(y), see Fig.6, and considering the local minimum as phase transition. It is natural to interpret the first local minimum (located in the negativeyy-region) as the first phase, the second local minimum (located in the positiveyy-region) as the second phase, and the intermediate region as the transition front[61]. From this perspective, the commutation-induced reversal of the LambertWW-kinks, described by Eqs. (27) and (35c), corresponds to the reversal of the phase-transition front. Thus, the original gel-to-liquid transition remains intact, while its propagation direction is reversed.Figure 4:LambertWW-kink soliton (y1(1)​(ξ)y_{1}^{(1)}(\xi)) and supersymmetric paired LambertWW-kink soliton (y1=(2)​(ξ)y_{1=}^{(2)}(\xi)) given by Eq. (27) and Eq. (35c), correspondingly, with the chosen parametersp=q=300p=q=300,s=27s=27,r=−141r=-141,k=2k=2,δ=v=1\delta=v=1.(a)(b)Figure 5:(a) LambertWW-kink soliton (y1(1)​(ξ)y_{1}^{(1)}(\xi)) and supersymmetric paired LambertWW-kink soliton (y1=(2)​(ξ)y_{1=}^{(2)}(\xi)) given by Eq. (27) and Eq. (35c) with interchanged signs, respectively, (b) LambertWW-kink soliton and supersymmetric paired LambertWW-kink soliton given by Eq. (27) and Eq. (35c) with interchanged signs with opposite direction, correspondingly. For (a) and (b) the chosen parameters arep=q=300p=q=300,s=27s=27,r=−141r=-141,k=2k=2,δ=v=1\delta=v=1.Figure 6:PotentialV1​(y)V_{1}(y)and supersymmetric partner potentialV2​(y)V_{2}(y)given by Eq. (17) and Eq. (36), correspondingly. For both potentials the illustrative physical parameters werep=8p=8,k=2k=2,v=δ=1,q=6v=\delta=1,q=6,r=−9.5r=-9.5ands=10.8s=10.8.

It is worth emphasizing that the sextic potentialsVi​(y)V_{i}(y)withi=1,2i=1,2, defined by Eqs. (37a) and (37b), arise not only in the framework of theϕ6\phi^{6}model but also in a variety of quantum-mechanical problems, including tunnelling, Wigner entropy, and the analysis of supersymmetric quantum states[62,63,64]. Even these potentials seem to graphically satisfy theshape invariancecondition (see Fig.6), from the SUSY QM, defined asV2​(y;a1)=V1​(y;a2)+R​(a1),V_{2}(y;a_{1})=V_{1}(y;a_{2})+R(a_{1}),(38)

wherea1a_{1}is a set of parameters, anda2=f​(a1)a_{2}=f(a_{1}), andR​(a1)R(a_{1})is independent of the variableyy[65], a direct computation shows that the potentialsVi​(y)V_{i}(y)are not shape invariant in a strict sense. This condition is essential to decide if the potentials do or do not belong to the same family of potentials.

## 3.3.2Case II.

Now, similar to previously analysed case, reversing the order ofϕ1​(y)\phi_{1}(y)andϕ2​(y)\phi_{2}(y)in Eq. (29) yieldsϕ1​(y)=±3​(y−α)2;ϕ2​(y)=±13​(−y2+A​y+B).\phi_{1}(y)=\pm\sqrt{3}(y-\alpha)^{2};\qquad\phi_{2}(y)=\pm\dfrac{1}{\sqrt{3}}(-y^{2}+Ay+B).(39)

Consequently,γ~2\tilde{\gamma}_{2},AAandBBare determined from the factorization conditions in Eq. (30a),d​yd​ξ=±3​(y−α)2​y.\dfrac{dy}{d\xi}=\pm\sqrt{3}(y-\alpha)^{2}y.(40)

Once we solve foryy, we obtainy2(2)​(ξ)=α​(1−11+W​[φ2′​(ξ)]),y_{2}^{(2)}(\xi)=\alpha\left(1-\dfrac{1}{1+W[\varphi_{2^{\prime}}(\xi)]}\right),(41)

whereφ2′​(ξ)=exp⁡(±3​α2​ξ−1),\varphi_{2^{\prime}}(\xi)=\exp\left(\pm\sqrt{3}\alpha^{2}\xi-1\right),(42)

andW​[φ2′]W[\varphi_{2^{\prime}}]is the LambertWWfunction.

The LambertWW-kink soliton (41) acts as the supersymmetric partner of (32c), with modified physical properties such as width and amplitude. Clearly, for the supersymmetric pairs withΔ>0\Delta>0andΔ<0\Delta<0, corresponding to Eq. (32b) and Eq. (32c), the LambertWW-kink soliton profile undergoes a complete modification. Similar to the previously analyzed case, plotting the LambertWW-kink soliton given by Eq. (32c) alongside its corresponding supersymmetric partner (41) reveals that both solutions preserve the same damping coefficient while their directions of propagation are reversed (see Fig.7). However, it is instructive to note that interchanging the sign conventions recovers both the LambertWW-kink soliton and its supersymmetric partner propagating in the same direction, as illustrated in Figs.8a and8b. In this representation, the modifications to the soliton width and amplitude become clearly evident.Figure 7:LambertWW-kink soliton (y2=(1)​(ξ)y_{2=}^{(1)}(\xi)) and supersymmetric paired LambertWW-kink soliton (y2(2)​(ξ)y_{2}^{(2)}(\xi)) given by Eq. (32c) and Eq. (41), correspondingly, with the chosen parametersp=q=500p=q=500,s=437s=437,r=−429r=-429,k=2k=2,δ=v=1\delta=v=1.(a)(b)Figure 8:(a) LambertWW-kink soliton (y2=(1)​(ξ)y_{2=}^{(1)}(\xi)) and supersymmetric paired LambertWW-kink soliton (y22​(ξ)y_{2}^{2}(\xi)) given by Eq. (32c) and Eq. (41) with interchanged signs, respectively, (b) LambertWW-kink soliton (y2=(1)​(ξ)y_{2=}^{(1)}(\xi)) and supersymmetric paired LambertWW-kink soliton (y22​(ξ)y_{2}^{2}(\xi)) given by Eq. (32c) and Eq. (41) with interchanged signs with opposite direction, correspondingly. For (a) and (b) the chosen parameters arep=q=500p=q=500,s=437s=437,r=−429r=-429,k=2k=2,δ=v=1\delta=v=1.

Similar to the previous case, the direct inversion ofϕ1​(y)\phi_{1}(y)andϕ2​(y)\phi_{2}(y), given by(39)(\ref{newo2}), for the damping coefficientγ~2\tilde{\gamma}_{2}leads to a Liénard equation with modulated potential:d2​yd​ξ2∓γ~2​d​yd​ξ+(−9​y2+12​α​y+B)​(y−α)2​y=0.\dfrac{d^{2}y}{d\xi^{2}}\mp\tilde{\gamma}_{2}\dfrac{dy}{d\xi}+(-9y^{2}+12\alpha y+B)(y-\alpha)^{2}y=0.(43)

Again by mechanical analogy, we can determine the potentialV1​(y)V_{1}(y)alongside its supersymmetric partner potentialV2​(y)V_{2}(y)for the damping coefficientγ~2\tilde{\gamma}_{2}:V1​(y)=16​y6−A+2​α5​y5+α2+2​A​α−B4​y4+2​α​B−A​α23​y3−B​α22​y2V_{1}(y)=\dfrac{1}{6}y^{6}-\dfrac{A+2\alpha}{5}y^{5}+\dfrac{\alpha^{2}+2A\alpha-B}{4}y^{4}+\dfrac{2\alpha B-A\alpha^{2}}{3}y^{3}-\dfrac{B\alpha^{2}}{2}y^{2}(44a)V2​(y)=32​y6−21​α5​y5+33​α2−B4​y4+2​α​B−12​α23​y3−B​α22​y2V_{2}(y)=\dfrac{3}{2}y^{6}-\dfrac{21\alpha}{5}y^{5}+\dfrac{33\alpha^{2}-B}{4}y^{4}+\dfrac{2\alpha B-12\alpha^{2}}{3}y^{3}-\dfrac{B\alpha^{2}}{2}y^{2}(44b)

withAAandBBdefined from Eqs. (30a). Similar to the case of potentialsVi​(y)V_{i}(y), withi=1,2i=1,2, of the previous subsection, we can see that the potentials(44a)(\ref{aaa1})and(44b)(\ref{aaa2})do not satisfy the shape invariance condition (38).(a)(b)Figure 9:(a) PotentialV1​(y)V_{1}(y)given by Eq. (17), and (b) and supersymmetric partner potentialV2​(y)V_{2}(y)given by Eq. (43). For both potentials the illustrative physical parameters werep=8p=8,k=2k=2,v=δ=1,q=6v=\delta=1,q=6,r=−9.5r=-9.5ands=10.8s=10.8.

We could delve deeper in the physiological significance of the supersymmetric paired potentials, given in Eqs. (37b) and (44b), and its associated exact travelling wave solutions, interpreting them as alterations in the physiological conditions governing signal transmission, potentially associated with neural anomalies, injuries, or pathological damage[66,67]. For instance, during seizure episodes or neuronal paroxysmal discharges, variations in pulse width and amplitude, together with partial distortion or breakdown of the propagating profiles, naturally arise. Such modifications of pulse width, amplitude, and profile shape are qualitatively reminiscent of alterations observed in abnormal neural activity. Although the present model does not directly describe specific neurological disorders, it suggests that changes in the effective nonlinear potential may provide a useful framework for exploring how pathological conditions influence electromechanical signal propagation[68,69].

In particular, challenges remain in accurately accounting for myelination effects, membrane heterogeneity, and the mechanical properties of realistic biomembranes[70,71,72]. These limitations, however, do not undermine the underlying physical picture; rather, they highlight the need for systematic extensions of the model. In this context, incorporating fractional-order dynamics together with position- and time-dependent coefficients provides a natural pathway toward a more realistic, non-autonomous generalization capable of capturing multiscale behaviour and memory effects inherent to neuronal systems. Such developments offer a promising direction for future research.
As a final remark, it is important to emphasize that, independently of the validity of the extended HJ model analyzed in the present work, action potentials triggered by mechanosensory processes are not a new concept. Similar phenomena have long been observed in several biological systems, particularly inMimosa pudica, one of the best-known examples[73,74]. Investigating these comparatively simpler systems could provide valuable physical insight into the mechanisms underlying nerve impulse generation and propagation in more complex excitable media.

## 4Conclusion

In this work, we considered an improved HJ model with strong polynomial nonlinearities, leading to a richer description of electromechanical wave dynamics in axonal membranes. In particular, the proposed extension naturally captures asymmetric pulse profiles, a feature that is not reproduced by the standard improved HJ model. This increased physical realism is accompanied by a significant mathematical consequence: the resulting Liénard equation loses its integrability in the Painlevé sense, thereby placing the analysis within a genuinely non-integrable regime.

Despite this loss of integrability, we demonstrated that exact travelling-wave solutions can still be obtained through the factorization method. The resulting LambertWW-kink solitons constitute a new class of analytical solutions for the extended HJ framework and reveal the persistence of coherent nonlinear structures under strong polynomial nonlinearities. Two distinct families of solutions were identified, each associated with different values of the axoplasmic fluid constant (or damping coefficient), thereby providing alternative dynamical regimes for pulse propagation.

Furthermore, by exploiting the analogy between factorization methods and SUSY QM, we constructed supersymmetric partner Liénard equations and their corresponding solutions. This approach generates modulated effective potentials, which are not shape invariant, and establishes a systematic mechanism for producing new waveforms from known solutions while preserving the underlying mathematical structure. The partner solutions exhibit significant variations in amplitude, width, and overall profile, while maintaining the same damping coefficient as the original waves. In extreme cases, the supersymmetric transformation leads to qualitatively distinct pulse morphologies, suggesting the existence of a broader family of electromechanical excitations than previously considered within the HJ framework.

The analytical and numerical investigation of the existence regions of these solutions further supports their robustness and reveals a rich parameter landscape. Moreover, a possible biological interpretation was proposed in which the supersymmetric potentials are associated with external mechanical loads or environmental perturbations acting on the membrane, while the partner solutions represent the corresponding cellular response. Within this perspective, the supersymmetric construction provides a mathematically consistent framework for studying how mechanical modulation may alter the characteristics of propagating nerve pulses.

More broadly, the present results demonstrate that LambertWW-kink solitons can emerge in non-integrable extensions of the HJ model and that supersymmetric techniques offer a powerful tool for generating and classifying families of electromechanical waves in nonlinear biological media. These findings open new avenues for investigating mechanically modulated nerve signals and their interactions with heterogeneous cellular environments. Future investigations should focus on the stability and experimental relevance of these supersymmetric electromechanical structures, as well as on their potential role in the regulation and adaptation of biological signal propagation in non-homogeneous media and in the presence of non-constant elastic coefficients.

## Acknowledgments

OPT acknowledges SECIHTI for a postdoctoral fellowship.

Data Availability StatementData sharing not applicable to this article as no datasets were generated or analyzed during the current study.

## References
- [1]Drukarch B, Holland H A, Velichkov M, Geurts J J G, Voorn P, Glas G and de Regt H W 2018 Thinking about the nerve impulse: a critical analysis of the electricity-centered conception of nerve excitability Progress in Neurobiology 169 172185.
- [2]Fields R D 2011 Signaling by neuronal swelling Science Signaling 4.
- [3]Tamm, K., Peets, T. & Engelbrecht, J. The modelling of the action potentials in myelinated nerve fibres. Biomech Model Mechanobiol 25, 13 (2026).
- [4]Karami, G., Grundman, N., Abolfathi, N., Naik, A., Ziejewski, M., 2009. A micromechanical hyperelastic modeling of brain white matter under large deformation. J. Mech. Behav. Biomed. 2, 243–254.
- [5]Cloots, R.J.H., Nyberg, T., Kleiven, S., van Dommelen, J.A.W., Geers, M.G.D., 2011. Micromechanics of diffuse axonal injury: influence of axonal orientation and anisotropy. Biomech. Model. Mechanobiol. 10, 413–422.
- [6]Abolfathi, N., Naik, A., Chafi, M.S., Karami, G., Ziejewski, M., 2009. A micromechanical procedure for modelling the anisotropic mechanical properties of brain white matter. Comput. Method Biomec. 12, 249–262.
- [7]Faller R 2020 UCD Biophysics 241: Membrane Biology (LibreTexts).
- [8]Doman, E.A., Ovenden, N.C., Phillips, J.B. et al. Biomechanical modelling infers that collagen content within peripheral nerves is a greater indicator of axial Young’s modulus than structure. Biomech Model Mechanobiol 24, 297–309 (2025).
- [9]Smruta Koppaka, Allison Hess-Dunning, Dustin J. Tyler. Biomechanical characterization of isolated epineurial and perineurial membranes of rabbit sciatic nerve. Journal of Biomechanics 136 (2022) 111058.
- [10]Singh A, Kozin S and Balasubramanian S (2025) Biomechanical responses of peripheral nerves in human, pig and rat: a comparative study. Front. Bioeng. Biotechnol. 13:1641386. doi: 10.3389/fbioe.2025.1641386
- [11]Hodgkin A L and Huxley A F 1952 A quantitative description of membrane current and its application to conduction and excitation in nerve The Journal of Physiology 117 500544.
- [12]Hodgkin A L and Huxley A F 1952 Currents carried by sodium and potassium ions through the membrane of the giant axon of loligo The Journal of Physiology 116 449472.
- [13]FitzHugh R 1961 Impulses and physiological states in theoretical models of nerve membrane Biophysical Journal 1 445466.
- [14]Nagumo J, Arimoto S and Yoshizawa S 1962 An active pulse transmission line simulating nerve axon Proceedings of the IRE 50 20612070.
- [15]Heimburg T and Jackson A D 2007 On the action potential as a propagating density pulse and the role of anesthetics Biophysical Reviews and Letters 02 5778.
- [16]Andersen S S L, Jackson A D and Heimburg T 2009 Towards a thermodynamic theory of nerve pulse propagation Progress in Neurobiology 88 104113.
- [17]El Hady A and Machta B B 2015 Mechanical surface waves accompany action potential propagation Nature Communications 6.
- [18]Rvachev M M 2010 On axoplasmic pressure waves and their possible role in nerve impulse propagation Biophysical Reviews and Letters 05 7388.
- [19]Marat M. Rvachev and Benjamin Drukarch. Surface Waves and Axoplasmic Pressure Waves in Action Potential Propagation: Fundamentally Different Physics or Two Sides of the Same Coin? Biophysical Reviews and Letters Vol. 20, No. 4 (2025) 283–289.
- [20]Alexander Mengnjo, Alain M. Dikandé, Gideon A. Ngwa. Model of the nerve impulse with account of mechanosensory processes: Stationary solutions. J Appl Math Phys, 8 (2020), pp. 2091-2102.
- [21]Alexander Mengnjo, Jake Leonard Nkeck. On the hybrid model of nerve pulse: Mathematical analysis and numerical results. J Appl Math Phys, 11 (2023), pp. 2373-2396.
- [22]R.A. El-Nabulsi. Emergence of lump-like solitonic waves in Heimburg–Jackson biomembranes and nerves fractal model. J R. Soc Interface, 19 (2022), Article 20220079.
- [23]Laura R. González-Ramírez. Fractional-Order Traveling Wave Approximations for a Fractional-Order Neural Field Model. Front. Comput. Neurosci., 23 March 2022.
- [24]Aly R. Seadawy, Asghar Ali, Ahmet Bekir. Solitary wave solutions of the nonlinear fractional soliton neuron model via application of five mathematical methods. Modern Phys Lett B (2025), Article 2550098 (20 pages).
- [25]Edgar Villagran Vargas, Andrei Ludu, Reinhold Hustert, Peter Gumrich, Andrew D. Jackson, Thomas Heimburg, Periodic solutions and refractory periods in the soliton theory for nerves and the locust femoral nerve, Biophysical Chemistry, Volume 153, Issues 2–3, 2011, Pages 159-167, ISSN 0301-4622,https://doi.org/10.1016/j.bpc.2010.11.001.
- [26]F. Contreras, F. Ongay, O. Pavón, M. Aguero. Non-topological solitons as travelling pulses along the nerve. Int J Mod Nonlinear Theory Appl, 02 (2013), Article 195200.
- [27]O. Pavón-Torres, M.A. Agüero-Granados, M.E. Maguiña-Palma. Interaction and adiabatic evolution of orthodromic and antidromic impulses in the axoplasmic fluid. Phys Lett A, 521 (2024), Article 129740.
- [28]Pavón-Torres, M.A. Agüero-Granados, Valencia-Torres. R. Adiabatic evolution of solitons embedded in lipid membranes. Phys Scr, 99 (2024), Article 125256.
- [29]Rani, A.; Shakeel, M.; Kbiri Alaoui, M.; Zidan, A.M.; Shah, N.A.; Junsawang, P. Application of theE​x​p−φ​ξExp-\varphi\xi-Expansion Method to Find the Soliton Solutions in Biomembranes and Nerves. Mathematics 2022, 10, 3372.
- [30]Razzaq, W., Akbulut, A., Zafar, A. et al. Solitary wave solutions of coupled nerve fibers model based on two analytical techniques. Opt Quant Electron 55, 591 (2023).
- [31]González-Gaxiola, O.; Biswas, A.; Moraru, L.; Alghamdi, A.A. Solitons in Neurosciences by the Laplace–Adomian Decomposition Scheme. Mathematics 2023, 11, 1080.
- [32]Shahzad T, Baber M Z, Qasim M, Sulaiman T A, Yasin M W and Ahmed N 2024 Explicit solitary wave profiles and stability analysis of biomembranes and nerves Modern Physics Letters B 38.
- [33]Tahira Jamal, Adil Jhangeer, Malik Zawwar Hussain. An anatomization of pulse solitons of nerve impulse model via phase portraits, chaos and sensitivity analysis. Chinese Journal of Physics 87 (2024) 496–509.
- [34]Ozsahin D U, Ceesay B, baber M Z, Ahmed N, Raza A, Rafiq M, Ahmad H, Awwad F A and Ismail E A A 2024 Multiwaves, breathers, lump and other solutions for the heimburg model in biomembranes and nerves Scientific Reports 14.
- [35]Younas, U., Muhammad, J., Almutairi, D.K. et al. Analyzing the neural wave structures in the field of neuroscience. Sci Rep 15, 7181 (2025).
- [36]Attia Rani, Muhammad Shakeel, Muhammad Sohail, Ibrahim Mahariq. The generalizing riccati equation mapping method’s application for detecting soliton solutions in biomembranes and nerves, Partial Differential Equations in Applied Mathematics, Volume 15, 2025, 101300, ISSN 2666-8181,https://doi.org/10.1016/j.padiff.2025.101300.
- [37]C.S. Fedosejevs, & M.F. Schneider, Sharp, localized phase transitions in single neuronal cells, Proc. Natl. Acad. Sci. U.S.A. 119 (8) e2117521119 (2022).
- [38]Jüri Engelbrecht, Kert Tamm, Tanel Peets. On mathematical modelling of solitary pulses in cylindrical biomembranes. Biomech Model Mechanobiol (2015) 14:159–167.
- [39]Tanel Peets, Kert Tamm, Jüri Engelbrecht. On the role of nonlinearities in the Boussinesq-type wave equations. Wave Motion 71 (2017) 113–119.
- [40]Jüri Engelbrecht, Kert Tamm & Tanel Peets (2017) On solutions of a Boussinesq-type equation with displacement-dependent nonlinearities: the case of biomembranes, Philosophical Magazine, 97:12, 967-987.
- [41]Tanel Peets, Kert Tamm, Päivo Simson, Jüri Engelbrecht. On solutions of a Boussinesq-type equation with displacement-dependent nonlinearity: A soliton doublet. Wave Motion 85(2019) 10–17.
- [42]V.A. Mendoza-Millán, J.L. Larios-Ferrer, J. Samuel Millán, M.A. Agüero-Granados, D.M. Galván-Arellano, O. Pavón-Torres. Lambert W-Kink solitons arising from higher-order nonlinearities of lipid membranes. Chaos, Solitons & Fractals, Volume 201, Part 2, 2025, 117260, ISSN 0960-0779, https://doi.org/10.1016/j.chaos.2025.117260.
- [43]Demirkaya, A., Decker, R., Kevrekidis, P.G. et al. Kink dynamics in a parametricϕ6\phi^{6}system: a model with controllably many internal modes. J. High Energ. Phys. 2017, 71 (2017). https://doi.org/10.1007/JHEP12(2017)071.
- [44]Amado, A., Mohammadi, A. Aϕ6\phi^{6}soliton with a long-range tail . Eur. Phys. J. C 80, 576 (2020). https://doi.org/10.1140/epjc/s10052-020-8162-9
- [45]O. Cornejo-Pérez and H. C. Rosu. Nonlinear Second Order Ode’s -factorization and particular solutions- Progress of Theoretical Physics, Vol. 114, No. 3 (2005).
- [46]González, H.C. Rosu, O. Cornejo-Pérez, S.C. Mancas, Factorization conditions for nonlinear second-order differential equations, in: S. Manukure, W.-X. Ma (Eds.), Nonlinear and Modern Mathematical Physics-Proceedings 2022, Springer, USA, 2024, pp. 81–99.
- [47]H. C. Rosu and O. Cornejo-Pérez. Supersymmetric pairing of kinks for polynomial nonlinearities. Phys. Rev. E 71, 046607 (2005).
- [48]J. A. Onana Inouga, S. E. Mkam Tchouobiap, M. Siewe Siewe, and F. M. Moukam Kakmeni. Action potential-like modes as modulated waves in an extended soliton model for biomembranes and nerves. AIP Advances 15, 015035 (2025).
- [49]Kowalevski, S.: Sur le probleme de la rotation d’un corps solide autour d’un point fixe. Acta Math. 12(1), 177–232 (1889). https://doi.org/10.1007/BF02592182.
- [50]Kowalevski, S.: Sur une propriété du systém d’uations différentielles qui définit la rotation d’un corps solide autour d’un point fixe. Acta Math. 14(1), 81–93 (1890). https://doi.org/10.1007/BF02413316.
- [51]Nikolay A. Kudryashov. Painlevé Test, First Integrals and Exact Solutions of Nonlinear Dissipative Differential Equations. Regular and Chaotic Dynamics, 2025, Vol. 30, No. 5, pp. 819–836.
- [52]Abdul-Majid Wazwaz, Compactons, solitons and periodic solutions for some forms of nonlinear Klein–Gordon equations, Chaos, Solitons & Fractals, Volume 28, Issue 4, 2006, Pages 1005-1013, ISSN 0960-0779,https://doi.org/10.1016/j.chaos.2005.08.145.
- [53]Norman Cruz, A. Hernández-Almada, Octavio Cornejo-Pérez. Constraining a causal dissipative cosmological model. Physical Review D 100, 083524 (2019).
- [54]Belinchón, J.A., Cornejo-Pérez, O. & Cruz, N. Exact solutions of a causal viscous FRW cosmology within the Israel–Stewart theory through factorization. Gen Relativ Gravit 54, 10 (2022).
- [55]Dragana Rankovic, DraganPrekrat, Anna Batova, and Slobodan Zdravkovic. Stability of subsonic and supersonic solitons in DNA. Chaos 36, 013147 (2026); doi: 10.1063/5.0277901.
- [56]Stefan C. Mancas, Haret C. Rosu. Integrable dissipative nonlinear second order differential equations via factorizations and Abel equations. Physics Letters A 377 (2013) 1434–1438.
- [57]Tamaghna Hazra, V. K. Chandrasekar, R. Gladwin Pradeep, and M. Lakshmanan. Exact solutions of coupled Liénard-type nonlinear systems using factorization technique. J. Math. Phys. 53, 023511 (2012); doi: 10.1063/1.3684956.
- [58]Ajey K. Tiwari, S.N. Pandey, V.K. Chandrasekar, M. Lakshmanan. Factorization technique and isochronous condition for coupled quadratic and mixed Liénard-type nonlinear systems. Applied Mathematics and Computation 252 (2015) 457–472.
- [59]G.González, O.Cornejo-Pérez, J.de la Cruz, H. C.Rosu. Isochronous waveforms of Liénard equations via commutative factorization. Physics Letters A 564 (2025) 131087.
- [60]Yousef AbuHour, Mohammed Banikhalid and Amirah Azmi. Solutions of the generalized Heimburg–Jackson model for membrane pulses. Z. Angew. Math. Phys. (2026) 77:193.
- [61]H. Yasuda, L.M.Korpas, and J.R.Raney. Transition Waves and Formation of Domain Walls in Multistable Mechanical Metamaterials. Physical Review Applied 13, 054067 (2020).
- [62]Escobar Ruiz, A.M., Mendoza Tavera, A.N., Sagar, R.P. et al. Wigner-entropy and negativity signatures of tunneling in a sextic double well. Eur. Phys. J. Plus 141, 240 (2026).
- [63]Mendoza Tavera, A.N., Escobar Ruiz, A.M. & Sagar, R.P. Entropic Characterization of Tunneling and State Pairing in a Quasi-exactly Solvable Sextic Potential. Int J Theor Phys 64, 322 (2025).
- [64]Alonso Contreras-Astorga, Adrian M Escobar-Ruiz and Román Linares. The SUSY partners of the QES sextic potential revisited. Phys. Scr. 99 (2024) 025223.
- [65]E Cooper et al. Supersymmetry and quantum mechanics. Physics Reports 251 (1995) 267-385.
- [66]R.J.H. Cloots, J.A.W. van Dommelen, M.G.D. Geers. A tissue-level anisotropic criterion for brain injury based on microstructural axonal deformation. Journal of the mechanical behavior of biomedical materials 5 (2012) 41-52.
- [67]Delteil C, Manlius T, Bailly N, Godio-Raboutet Y, Piercecchi-Marti MD, Tuchtan L, Hak JF, Velly L, Simeone P, Thollon L. Traumatic axonal injury: Clinic, forensic and biomechanics perspectives. Leg Med (Tokyo). 2024 Sep;70:102465. doi: 10.1016/j.legalmed.2024.102465. Epub 2024 Jun 2. PMID: 38838409.
- [68]Arévalo, E., Gaididei, Y. & Mertens, F. Soliton dynamics in damped and forced Boussinesq equations. Eur. Phys. J. B 27, 63–74 (2002). https://doi.org/10.1140/epjb/e20020130.
- [69]Fan, Kai, Zhou, Cunlong, Exact Solutions of Damped Improved Boussinesq Equations by Extended (G’/G)-Expansion Method, Complexity, 2020, 4128249, 14 pages, 2020. https://doi.org/10.1155/2020/4128249.
- [70]Guirland, C., Zheng, J.Q. (2007). Membrane Lipid Rafts and Their Role in Axon Guidance. In: Bagnard, D. (eds) Axon Growth and Guidance. Advances in Experimental Medicine and Biology, vol 621. Springer, New York, NY.
- [71]P.C. Bressloff, Waves in Neural Media (Springer, Berlin, 2014).
- [72]Mareš, J.J., Špička, V. & Hubík, P. On physical processes controlling nerve signalling. Eur. Phys. J. Spec. Top. 232, 3561–3576 (2023).
- [73]Volkov, A.G., Foster, J.C., Ashby, T.A., Walker, R.K., Johnson, J.A. and Markin, V.S. (2010), Mimosa pudica: Electrical and mechanical stimulation of plant movements. Plant, Cell & Environment, 33: 163-173.
- [74]Stolarz, M. & Trebacz, K. (2021) Spontaneous rapid leaf movements and action potentials in Mimosa pudica L. Physiologia Plantarum, 173(4), 1882–1888.

## 


- 


Major funding support from
