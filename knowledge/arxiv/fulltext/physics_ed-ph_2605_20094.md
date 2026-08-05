# Introduction to Higher Order Classical Dynamics: Pais-Uhlenbeck Model and Coupled Oscillators

**arXiv ID**: 2605.20094v1
**Authors**: Cássius Anderson Miquele de Melo, Ivan Francisco de Souza
**Published**: 2026-05-19
**Categories**: physics.ed-ph, hep-th, math-ph, physics.class-ph, quant-ph
**Comments**: Version with expanded references
**DOI**: 10.1119/5.0284311
**HTML URL**: https://arxiv.org/html/2605.20094v1

## Abstract

Most of the laws of Nature involve derivatives up to the second order. Ostrogradski was the first to seek a formulation of the equations of higher-order derivatives. He extended Hamilton's equations by considering Lagrangians that depend on higher-order derivatives of generalized coordinates. The Hamilton-Ostrogradski formulation served as the basis for later studies with higher-order derivatives. However, the Hamilton-Ostrogradski formalism is rarely discussed in textbooks or the pedagogical literature. This motivated us to show how the Hamilton-Ostrogradski formalism can be applied it to the Pais-Uhlenbeck oscillator. We hope that the approach presented in this work can serve as a basis for discussion in advanced classical mechanics courses.

## Full Text

Introduction to Higher Order Classical Dynamics: Pais-Uhlenbeck Model and Coupled Oscillators

## Title:

Content selection saved. Describe the issue below:Description:arXiv is now an independent nonprofit!Learn more×
- 
- 
- 
- 
- 
- 
- 
- License: CC BY 4.0arXiv:2605.20094v1 [physics.ed-ph] 19 May 2026††thanks:cassius@unifal-mg.edu.br††thanks:ivanfrancisco2098@gmail.com

## Introduction to Higher Order Classical Dynamics: Pais-Uhlenbeck Model and Coupled OscillatorsCássius Anderson Miquele de Melohttps://orcid.org/0000-0001-5096-1297Instituto de Ciência e Tecnologia, Universidade Federal de Alfenas, BR 267 - Rodovia José Aurélio Vilela, nº 11.999, Km 533 37715-400 Cidade Universitária, Poços de Caldas, Minas Gerais, Brasil.INFN, Laboratori Nazionali del Sud (LNS), Via S. Sofia 62, 95123 Catania, ItalyUniversità di Catania, Dipartimento di Fisica e Astronomia “Ettore Majorana” (INFN-CT), Via Santa Sofia 64, 95123 Catania, ItalyIvan Francisco de Souzahttps://orcid.org/0000-0002-1679-0057Instituto de Ciência e Tecnologia, Universidade Federal de Alfenas, BR 267 - Rodovia José Aurélio Vilela, nº 11.999, Km 533 37715-400 Cidade Universitária, Poços de Caldas, Minas Gerais, Brasil.(May 19, 2026)

## Abstract

Abstract:Most of the laws of Nature involve derivatives up to the second order. Ostrogradski was the first to seek a formulation of the equations of higher-order derivatives. He extended Hamilton’s equations by considering Lagrangians that depend on higher-order derivatives of generalized coordinates. The Hamilton-Ostrogradski formulation served as the basis for later studies with higher-order derivatives. However, the Hamilton-Ostrogradski formalism is rarely discussed in textbooks or the pedagogical literature. This motivated us to show how the Hamilton-Ostrogradski formalism can be applied it to the Pais-Uhlenbeck oscillator. We hope that the approach presented in this work can serve as a basis for discussion in advanced classical mechanics courses.Suggested keywords††preprint:APS/123-QED

## IIntroduction


Many physics equations involve only first- and second-order derivatives, such as Newton’s laws, Maxwell’s equations and Schrödinger’s equation. However, nothing prevents physical systems in nature from being dependent on higher-order derivatives.

There are theoretical models that involve higher-order derivatives, such as Generalized Electrodynamics[32,11], which is a particular case of higher-order gauge theories[15]. One of the main motivations to study higher derivative theories is that they represent high-energy corrections to our known low-energy effective theories of nature. This is connected to the Wilsonian/Renormalisation group interpretation of quantum field theories[36,4]. Another common case of theories with higher-order derivatives is gravity[39,26,10,37,9,12], whose higher-order derivatives can be seen as evidence of coupling with new fields beyond the standard model[13,14]. Furthermore, there is practical interest in higher order derivatives for quantum gravity and field theory, as such derivatives naturally arise as effective corrections and candidates for fundamental theories, such as string theory[20,42,33,27,18].

There are also concrete physical examples of higher-order derivative forces. A well-known case is the Abraham–Lorentz force[1,25,16]in classical electrodynamics[23,38,35]. This force describes the reaction of a charged particle that emits radiation when accelerated. In this situation, the force depends on the derivative of the acceleration (often called the “jerk”), leading to equations of motion that are third-order in time. Such dynamics give rise to peculiar effects such as preacceleration, where the particle starts to move before the external force is applied, and runaway solutions. These features illustrate that generalizations of Newton’s second law to higher orders are indeed possible, but they come with important conceptual and practical challenges.

The first and perhaps most influential example of a higher-order system in classical mechanics is the Pais–Uhlenbeck oscillator, originally introduced in 1950 as a model for field theories with non-localized action[30]. Since then, it has become a paradigmatic system for exploring the conceptual challenges associated with higher-order dynamics. In particular, it embodies the so-called Ostrogradsky instability, the hallmark of unbounded Hamiltonians in higher-derivative theories[41]. Furthermore, the Pais-Uhlenbeck oscillator has several modern applications, such as the description of ion traps[22], circularly polarized gravitational waves[17], and dark energy[8]. These features make the Pais–Uhlenbeck oscillator not only historically relevant but also a valuable pedagogical tool to motivate the study of higher-order formalisms.

To describe physical systems with higher-order derivatives, it is necessary to have equations involving derivatives of any order. The first person to formulate equations of motion for higher orders was Mikhail Vassilievich Ostrogradsky[29]. In 1850, Ostrogradsky derived the Hamiltonian equations when considering Lagrangians that depend on higher-order time derivatives of generalized coordinates[29].

Equations of motion involving higher-order derivatives are a subject often overlooked in various textbooks and advanced mechanics courses[19,2]. In recent decades, this topic has been extensively studied, as some researchers believe that new discoveries in this area could expand our understanding of nature[6]. However, it remains relatively unknown among many physics students. With this in mind, this work aims to provide a brief introduction to higher-order equations of motion, hoping to serve as motivation and a foundation for students who wish to delve deeper and consult other references covering this subject.

In Section II, we present the Lagrange equations for a Lagrangian that depends on thenn-th time derivative of the generalized coordinates. In Section III, we discuss the transition from the Lagrangian to the Hamiltonian formalism in higher-order theories. Our aim is to apply this formalism to the Pais-Uhlenbeck oscillator, but since it is not common to deal with energies depending on second-order derivatives, understanding the Pais-Uhlenbeck oscillator may initially be challenging. For this reason, in Section IV we introduce the model of two coupled oscillators, which is easier to visualize and which, when reformulated to yield uncoupled fourth-order equations of motion, can be mapped onto the Pais-Uhlenbeck model. Finally, Section V is devoted to the Pais-Uhlenbeck oscillator, whose Lagrangian involves derivatives up to the second order and leads to a fourth-order equation of motion. In Section VI, we present our final considerations.

## IIHigher-Order Lagrange Equations

Newton’s second law is based on empirical observations of nature rather than a general mathematical principle. Therefore, it is not straightforward to extend it systematically to higher-order derivatives of position. In contrast, Lagrange’s and Hamilton’s equations can be derived from the principle of least action, providing a consistent mathematical framework for constructing higher-order equations.

In the literature and in advanced mechanics courses, usually only the first-order Lagrangian formulation is presented,L=L​(q,q˙,t)L=L(q,\dot{q},t), whereq≡q​(t)q\equiv q(t)is the generalized coordinate,q˙≡d​q/d​t\dot{q}\equiv\mathrm{d}q/\mathrm{d}tis the generalized velocity (first-order derivative) andttis time.

The Lagrange equation for this type of Lagrangian is∂L∂q−dd​t​(∂L∂q˙)=0.\frac{\partial L}{\partial q}-\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\dot{q}}\right)=0.(1)

Observe that this is an equation that involves derivatives up to the second order, which can be seen by expanding the second term of Eq.\eqrefE2. This equation is useful for the vast majority of physical systems, but for systems that might depend on derivatives of order greater than two, it is necessary to generalize the Lagrange equations.

Going further, considering a Lagrangian that can also depend onq¨\ddot{q}, the generalized acceleration, by imposing certain conditions and performing some mathematical procedures (see Appendix A), one obtains the following Lagrange equation:∂L∂q−dd​t​(∂L∂q˙)+d2d​t2​(∂L∂q¨)=0.\frac{\partial L}{\partial q}-\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\dot{q}}\right)+\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}}\left(\frac{\partial L}{\partial\ddot{q}}\right)=0.(2)

Note that now it is an equation that may involve derivatives up to the fourth order. It is possible to generalize the Lagrange equations that depend on thenn-th order derivative. The higher-order Lagrange equation is∑k=0n(−1)k​dkd​tk​(∂L∂q(k))=0.\sum_{k=0}^{n}(-1)^{k}\frac{\mathrm{d}^{k}}{\mathrm{d}t^{k}}\left(\frac{\partial L}{\partial q^{(k)}}\right)=0.(3)

We write the index indicating the order of the derivative in parentheses “( )” to avoid confusion with exponents. For example,(−1)k(-1)^{k}means−1-1raised to thekk-th power, whileq(k)q^{(k)}refers to thekk-th order derivative of the generalized coordinate. Forn=1n=1, the higher-order equation reduces to Eq.\eqrefE2.

If the system hasNNdegrees of freedom, there will beNNgeneralized coordinates andNNhigher-order Lagrange equations:∑k=0n(−1)k​dkd​tk​(∂L∂qi(k))=0(i=1,…,N).\sum_{k=0}^{n}(-1)^{k}\frac{\mathrm{d}^{k}}{\mathrm{d}t^{k}}\left(\frac{\partial L}{\partial q_{i}^{(k)}}\right)=0\quad(i=1,...,N).(4)

Eq.\eqrefE5 is an equation that may involve derivatives up to order2​n2n.
We can define a matrix, called theHessian, which plays a central role in the analysis of higher-order systems. Its elements are given byWi​j=∂2L∂qi(n)​∂qj(n)(i,j=1,…,N).W_{ij}=\frac{\partial^{2}L}{\partial q_{i}^{(n)}\partial q_{j}^{(n)}}\quad(i,j=1,\dots,N).(5)

If this matrix is non-singular, that is, if its determinant is nonzero, it becomes possible to isolate the highest-order termsqi(2​n)q_{i}^{(2n)}from the Lagrange equation, yieldingWi​jqj(2​n)=Fi(qi,…,qi(2​n−1),t)(i,j=1,…,N),W_{ij}q_{j}^{(2n)}=F_{i}(q_{i},...,q_{i}^{(2n-1)},t)\quad(i,j=1,...,N),(6)

whereFi​(qi,…,qi(2​n−1),t)F_{i}(q_{i},...,q_{i}^{(2n-1)},t)collects all the terms involving derivatives of lower order.

In this work, we deal only with regular systems. In the case of systems where the Hessian matrix is singular, one of the established methods to construct the Hamiltonian formulation must be applied[6,3,5].

## IIIHigher-Order Hamilton Equations

In this section, we will review Hamilton’s equations as they are usually presented, considering the Lagrangian of Eq.\eqrefE2. We will then consider a Lagrangian with second-order derivatives and, present the general formulation of Hamilton’s equations.

As seen in the previous section, Eq.\eqrefE2 contains derivatives only up to the second order, which is sufficient for many physical systems. The advantage of moving from the Lagrangian formalism to the Hamiltonian formalism is that Hamilton’s equations are first-order equations. In return, the number of variables and equations is doubled, since generalized momenta are introduced, defined bypi=∂L∂q˙i(i=1,…,N).p_{i}=\frac{\partial L}{\partial\dot{q}_{i}}\quad(i=1,...,N).(7)

To construct the Hamiltonian function, the Legendre transformation is used:H​(qi,pi,t)=∑i=1Npi​q˙i−L​(qi,q˙i,t).H(q_{i},p_{i},t)=\sum_{i=1}^{N}p_{i}\dot{q}_{i}-L(q_{i},\dot{q}_{i},t).(8)

Again, the condition that the Hessian matrix is regular must be satisfied so that it is possible to invert theNNequations of the type Eq.\eqrefE8 and express theq˙s\dot{q}_{s}as functions ofqsq_{s},psp_{s}, andtt. Thus, the Hamiltonian formulation has a set of2​N2Nequations that can be solved to determine the2​N2Nindependent variables. The usual Hamilton equations are:{aligned}​q˙i=∂H∂pi,p˙i=−∂H∂qi.\aligned\dot{q}_{i}=\frac{\partial H}{\partial p_{i}},\\
\dot{p}_{i}=-\frac{\partial H}{\partial q_{i}}.(9)

When considering higher-order Lagrangians, the Legendre transformation as presented in Eq.\eqrefE9 does not generate the corresponding Hamilton equations for higher orders[34]. The transition between formalisms when higher-order derivatives are considered is somewhat more subtle, as new coordinates and momenta must be defined. We will see that such definitions will imply constraints, which are unavoidable when considering Lagrangians depending on derivatives of order greater than one, and because of that, not all variables will be mutually independent. Therefore, a more general Legendre transformation is necessary for higher-order equations. The first to obtain the Hamiltonian formulation for higher-order Lagrangians was Ostrogradsky[29]. This formulation became known as the Hamilton-Ostrogradsky formalism.

We will take a simpler approach to the Hamilton-Ostrogradsky formalism, considering that the system has only one degree of freedom and that its Lagrangian does not explicitly depend on time. Considering the case of a Lagrangian of the typeL​(q,q(1),q(2))L(q,q^{(1)},q^{(2)}), we saw that the Lagrange equation takes the form of Eq.\eqrefE3. Firstly, the canonical variables introduced by Ostrogradsky, for a Lagrangian that depends up to the second time derivative ofq​(t)q(t), are defined as{split}​Q1=q,Q2=q(1),P1=∂L∂Q1˙−dd​t​(∂L∂Q1¨),P2=∂L∂Q˙2,\split Q_{1}&=q,\\
Q_{2}&=q^{(1)},\\
P_{1}&=\frac{\partial L}{\partial\dot{Q_{1}}}-\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\ddot{Q_{1}}}\right),\\
P_{2}&=\frac{\partial L}{\partial\dot{Q}_{2}},(10)

whereQ1Q_{1}andQ2Q_{2}are the new generalized coordinates, andP1P_{1}andP2P_{2}are the corresponding conjugate momenta.

These definitions are not arbitrary: mathematically, the purpose of Ostrogradsky’s formalism is to recast the dynamics of higher-order systems into a set of first-order differential equations. For a Lagrangian of the formL=L​(q,q˙,q¨)L=L(q,\dot{q},\ddot{q}), the corresponding Euler-Lagrange equation is of fourth order inq​(t)q(t). By introducing the variables(Q1,Q2,P1,P2)(Q_{1},Q_{2},P_{1},P_{2}), the problem is reformulated in an extended phase space, where the temporal evolution can be described by the standard Hamiltonian formalism, although in a higher dimension.

From a physical point of view,Q1=qQ_{1}=qrepresents the position, while itQ2=q˙Q_{2}=\dot{q}corresponds to the velocity promoted to an independent coordinate, necessary to describe the dynamics of a fourth-order system. The momenta also acquire an enriched interpretation:P2=∂L/∂q¨P_{2}=\partial L/\partial\ddot{q}plays the role of the momentum conjugate to the velocity, capturing the sensitivity of the Lagrangian to the acceleration, whileP1P_{1}includes not only the usual contribution∂L/∂q˙\partial L/\partial\dot{q}, but also an additional term coming from the time variation of∂L/∂q¨\partial L/\partial\ddot{q}. This demonstrates how the canonical momentum in higher-order theories encodes the system’s reaction to variations in generalized velocities rather than just being the rate at which the Lagrangian varies in relation to velocity

Notice that, due to the definition of momentum, constraints arise, such as:P1+P˙2−∂L∂q(1)=0.P_{1}+\dot{P}_{2}-\frac{\partial L}{\partial q^{(1)}}=0.(11)

To obtain the canonical equations, it is necessary that the Hessian matrix be regular so that the highest-order derivative can be written in terms of the new variables,111In this case,q(2)q^{(2)}as a function ofQ1Q_{1},Q2Q_{2}, andP2P_{2}.thus allowing the Hamiltonian to be written for this case (cf. Appendix B). Otherwise, it would be necessary to use the Dirac-Bergmann method[5]to handle the constraints that arise from these definitions. We will not address the Dirac-Bergmann method here; instead, we will consider cases where the Hessian matrix is regular. After some mathematical procedures (cf. Appendix B), the Legendre transformation obtained is:{aligned}​H​(Q1,Q2,P1,P2)=P1​Q˙1+P2​Q2˙​(Q1,Q2,P2)−L​(Q1,Q2,P1,P2,q(2)​(Q1,Q2,P2)).\aligned H(Q_{1},Q_{2},P_{1},P_{2})=P_{1}\dot{Q}_{1}+P_{2}\dot{Q_{2}}(Q_{1},Q_{2},P_{2})\\
-L(Q_{1},Q_{2},P_{1},P_{2},q^{(2)}(Q_{1},Q_{2},P_{2})).\,(12)

Thus, the Hamilton equationsare:{aligned}​Q˙1=∂H∂P1,Q˙2=∂H∂P2,P˙1=−∂H∂Q1,P˙2=−∂H∂Q2.\aligned\dot{Q}_{1}=\frac{\partial H}{\partial P_{1}},\\
\dot{Q}_{2}=\frac{\partial H}{\partial P_{2}},\\
\dot{P}_{1}=-\frac{\partial H}{\partial Q_{1}},\\
\dot{P}_{2}=-\frac{\partial H}{\partial Q_{2}}.\,(13)

Even considering only one degree of freedom, when transitioning to the Hamiltonian formulation, four variables are defined, requiring four Hamilton equations. Appendix B shows how these results are obtained. It is important to emphasize that these equations can only be derived if a non-degenerate Lagrangian is considered, that is, one whose Hessian matrix is invertible.

The most general form used by Ostrogradsky to define the canonical variables is:Qk=q(k−1)(k=1,…,n),Q_{k}=q^{(k-1)}\quad(k=1,...,n),(14)Pk=∑l=kn(−1)l−k​dl−kd​tl−k​(∂L∂q(l))(k=1,…,n),P_{k}=\sum_{l=k}^{n}(-1)^{l-k}\frac{\mathrm{d}^{l-k}}{\mathrm{d}t^{l-k}}\left(\frac{\partial L}{\partial q^{(l)}}\right)\quad(k=1,...,n),(15)

whereQkQ_{k}is thekk-th coordinate andPkP_{k}is thekk-th momentum. A total of2​n2nvariables are defined, although not all of them are independent because of the constraints arising from these definitions. The general Legendre transformation has the following form:H=∑k=1n−1Pk​Qk+1+Pn​q(n)−L=∑k=1nPk​Q˙k−L,H=\sum_{k=1}^{n-1}P_{k}Q_{k+1}+P_{n}q^{(n)}-L=\sum_{k=1}^{n}P_{k}\dot{Q}_{k}-L,(16)

and the2​n2nHamilton equations are:{aligned}Q˙k=∂H∂Pk,P˙k=−∂H∂Qk.(k=1,…,n)\aligned\dot{Q}_{k}=\frac{\partial H}{\partial P_{k}},\\
\dot{P}_{k}=-\frac{\partial H}{\partial Q_{k}}.\,\quad(k=1,...,n)(17)

For a system withNNdegrees of freedom, each of them of ordernn, there will be a total ofN×2​nN\times 2nequations forN×2​nN\times 2nvariables:{aligned}​Q˙i,k=∂H∂Pi,k,P˙i,k=−∂H∂Qi,k,\aligned\dot{Q}_{i,k}=\frac{\partial H}{\partial P_{i,k}},\\
\dot{P}_{i,k}=-\frac{\partial H}{\partial Q_{i,k}},\,(18)

wherei=1,…,Ni=1,...,Nandk=1,…,nk=1,...,n.

## IVCoupled Oscillators

An interesting model that can be used as a first approach to higher-order equations is that of two coupled oscillators. We will see that it is not necessary to resort to higher-order Lagrange or Hamilton–Ostrogradsky equations to obtain the equations of motion for these oscillators, since the Lagrangian of this system depends only on first-order derivatives. Nevertheless, it can also be shown that the solutions of the second-order equations of motion for the coupled oscillators form a subset of the solutions of the fourth-order equation of motion of the Pais–Uhlenbeck oscillator, for which higher-order equations are required[24].

To begin the discussion, consider two oscillators of massesm1m_{1}andm2m_{2}attached to walls by springs of constantsk1k_{1}andk2k_{2}, respectively; between the two masses there is a third spring of constantkkcoupling them, as shown in Figure1:Figure 1:Schematic diagram of two coupled oscillators

Letx1​(t)x_{1}(t)andx2​(t)x_{2}(t)denote the displacements of massesm1m_{1}andm2m_{2}from their respective equilibrium positions.
The Lagrangian of the coupled oscillators isL=m1​x˙122+m2​x˙222−k1​x122−k2​x222−k​(x2−x1)22.L=\frac{m_{1}\dot{x}_{1}^{2}}{2}+\frac{m_{2}\dot{x}_{2}^{2}}{2}-\frac{k_{1}x_{1}^{2}}{2}-\frac{k_{2}x_{2}^{2}}{2}-\frac{k(x_{2}-x_{1})^{2}}{2}.(19)

This is a system with two degrees of freedom. In this case, we can use Eq.\eqrefE2 to obtain the equations of motion:{{aligned}m1x¨1+k1x1−k(x2−x1)=0,m2x¨2+k2x2−k(x1−x2)=0.\left\{\aligned m_{1}\ddot{x}_{1}+k_{1}x_{1}-k(x_{2}-x_{1})&=0,\\
m_{2}\ddot{x}_{2}+k_{2}x_{2}-k(x_{1}-x_{2})&=0.\right.(20)

Note that in these two equations of motion the oscillators’ motions are not independent due to the coupling constantkk. In the first equation (oscillator 1) the coordinate of oscillator 2 appears, and vice versa in the second equation. To find the solutions of these two equations, one method is the order-raising technique: differentiate one equation twice and substitute the other into it, yielding a single fourth-order equation involving only one oscillator’s coordinate. Applying this method (see Ref.[27]), the pair in Eq.\eqrefE21 reduces to:{aligned}m1\ddddotx1+[m2​(k1+k)+m1​(k2+k)m2]x¨1++[k1​k2+k​(k1+k2)m2]x1=0,\aligned m_{1}\ddddot{x_{1}}+\left[\frac{m_{2}(k_{1}+k)+m_{1}(k_{2}+k)}{m_{2}}\right]\ddot{x}_{1}+\\
+\left[\frac{k_{1}k_{2}+k(k_{1}+k_{2})}{m_{2}}\right]x_{1}=0,(21)

The fourth-order equation for oscillator 2 is analogous, obtained by swapping indices 1 and 2 in Eq.\eqrefE22.

The general solution of Eq.\eqrefE22 is{aligned}x1(t)=A1cos(ω1t)+B1sin(ω1t)++A2cos(ω2t)+B2sin(ω2t),\aligned x_{1}(t)=A_{1}\cos(\omega_{1}t)+B_{1}\sin(\omega_{1}t)+\\
+A_{2}\cos(\omega_{2}t)+B_{2}\sin(\omega_{2}t),(22)

whereω1\omega_{1}andω2\omega_{2}areω1=α+β2eω2=α−β2\omega_{1}=\sqrt{\frac{\alpha+\beta}{2}}\quad\mathrm{e}\quad\omega_{2}=\sqrt{\frac{\alpha-\beta}{2}}(23)

in which,α\alphaandβ\betaare defined as follows:α≡k2+km2+k1+km1,\alpha\equiv\frac{k_{2}+k}{m_{2}}+\frac{k_{1}+k}{m_{1}},β≡(k2+km2−k1+km1)2−4​k2m1​m2.\beta\equiv\sqrt{\left(\frac{k_{2}+k}{m_{2}}-\frac{k_{1}+k}{m_{1}}\right)^{2}-\frac{4k^{2}}{m_{1}m_{2}}}.

The constantsA1A_{1},A2A_{2},B1B_{1}, andB2B_{2}depend on the initial conditions:{aligned}​A1=ω22​x1​(0)+x¨1​(0)ω22−ω12,A2=−ω12​x1​(0)+x¨1​(0)ω22−ω12,B1=ω22​x˙1​(0)+x˙˙˙1​(0)ω1​(ω22−ω12),B2=−ω12​x˙1​(0)+x˙˙˙1​(0)ω2​(ω22−ω12).\aligned A_{1}=\frac{\omega_{2}^{2}x_{1}(0)+\ddot{x}_{1}(0)}{\omega_{2}^{2}-\omega_{1}^{2}},\\
A_{2}=-\frac{\omega_{1}^{2}x_{1}(0)+\ddot{x}_{1}(0)}{\omega_{2}^{2}-\omega_{1}^{2}},\\
B_{1}=\frac{\omega_{2}^{2}\dot{x}_{1}(0)+\dddot{x}_{1}(0)}{\omega_{1}(\omega_{2}^{2}-\omega_{1}^{2})},\\
B_{2}=-\frac{\omega_{1}^{2}\dot{x}_{1}(0)+\dddot{x}_{1}(0)}{\omega_{2}(\omega_{2}^{2}-\omega_{1}^{2})}.(24)

Thus, by using this method, the two second-order equations reduce to one fourth-order equation. Oncex1​(t)x_{1}(t)is determined, one isolatesx2x_{2}from the first line of Eq.\eqrefE21 and substitutesx1​(t)x_{1}(t)andx¨1​(t)\ddot{x}_{1}(t)to find the solution for oscillator 2.

In the next section, we will present the Lagrangian of the Pais–Uhlenbeck oscillator, which yields a fourth-order equation of motion. We will also show that the solutions for the coupled oscillators satisfy the Pais–Uhlenbeck oscillator’s equation of motion.

## VPais-Uhlenbeck Oscillator

The Pais-Uhlenbeck oscillator is a model that yields extensive analysis, with one particular case being that of coupled oscillators. Therefore, in this section, we will focus on discussing how the two-coupled-oscillators model seen in the previous section is equivalent to the Pais-Uhlenbeck oscillator.

The Lagrangian of the Pais-Uhlenbeck oscillator isLPU=12​[x¨2+(Ω12+Ω22)​x˙2+Ω12​Ω22​x2],L_{\mathrm{PU}}=\frac{1}{2}\left[\ddot{x}^{2}+(\Omega_{1}^{2}+\Omega_{2}^{2})\dot{x}^{2}+\Omega_{1}^{2}\Omega_{2}^{2}x^{2}\right],(25)

whereΩ1\Omega_{1}andΩ2\Omega_{2}are constants.

This is a Lagrangian that depends on a second-order derivative, which requires the use of a higher-order Lagrange equation to obtain the equation of motion. Applying Eq.\eqrefE3 to this Lagrangian, we obtain:\ddddot​x+(Ω12+Ω22)​x¨+Ω12​Ω22​x=0.\ddddot{x}+(\Omega_{1}^{2}+\Omega_{2}^{2})\ddot{x}+\Omega_{1}^{2}\Omega_{2}^{2}x=0.(26)

We have a fourth-order equation of motion. If we divide Eq.\eqrefE22 bym1m_{1}, we can notice the similarity between Eq.\eqrefE22 and Eq.\eqrefE27. For them to be equivalent, the following relations must be satisfied:{aligned}​Ω12+Ω22=k1+km1+k2+km2,Ω12​Ω22=k1​k+k2​k+k1​k2m1​m2.\aligned\Omega_{1}^{2}+\Omega_{2}^{2}=\frac{k_{1}+k}{m_{1}}+\frac{k_{2}+k}{m_{2}},\\
\Omega_{1}^{2}\Omega_{2}^{2}=\frac{k_{1}k+k_{2}k+k_{1}k_{2}}{m_{1}m_{2}}.(27)

Solving these two equations to determineΩ1\Omega_{1}andΩ2\Omega_{2}, we haveΩ1=α+β2eΩ2=α−β2\Omega_{1}=\sqrt{\frac{\alpha+\beta}{2}}\quad\mathrm{e}\quad\Omega_{2}=\sqrt{\frac{\alpha-\beta}{2}}(28)

The right-hand sides of Eq.\eqrefE29 and Eq.\eqrefE24 are exactly the same, implying thatΩ1=ω1\Omega_{1}=\omega_{1}andΩ2=ω2\Omega_{2}=\omega_{2}. Sincex1​(t)x_{1}(t)andx2​(t)x_{2}(t)are solutions of the coupled oscillators, we have an equivalence between the Pais-Uhlenbeck oscillator and the coupled oscillators:L=12​[x¨i2+(ω12+ω22)​x˙i2+ω12​ω22​xi2],L=\frac{1}{2}\left[\ddot{x}_{i}^{2}+(\omega_{1}^{2}+\omega_{2}^{2})\dot{x}_{i}^{2}+\omega_{1}^{2}\omega_{2}^{2}x_{i}^{2}\right],(29)

wherei={1,2}i=\{1,2\}so that each one of the coupled oscillators can be taken as an unique Pais-Uhlenbeck oscillator.

Despite the formal equivalence of the Lagrangians, it is crucial to draw attention to some nuances related to the order elevation method. First, the fourth-order equations require a larger number of initial conditions than the original second-order system, which gives rise to additional nonphysical (spurious) solutions that must be properly identified and discarded through an analysis of the boundary conditions. Furthermore, in higher-order formulations, the variational principle naturally imposes boundary conditions, and translating these into initial conditions is not always straightforward, requiring careful consideration[28]. A more detailed analysis of these aspects lies beyond the scope of the present work but could be pursued in future studies.

For a Hamiltonian approach to the Pais-Uhlenbeck oscillator, we must first write the new coordinates and momenta from the Ostrogradsky definition. Through Eq.\eqrefE11, we have:{split}​Q1=x1,Q2=x˙1,P1=∂L∂q(1)−dd​t​(∂L∂q(2))=(ω12+ω22)​x˙1−x˙˙˙1,P2=x¨1.\split Q_{1}&=x_{1},\\
Q_{2}&=\dot{x}_{1},\\
P_{1}&=\frac{\partial L}{\partial q^{(1)}}-\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial q^{(2)}}\right)=(\omega_{1}^{2}+\omega_{2}^{2})\dot{x}_{1}-\dddot{x}_{1},\\
P_{2}&=\ddot{x}_{1}.(30)

The Hamiltonian can be obtained from Eq.\eqrefE13:H=P1​Q2+P222−12​[(ω12+ω22)​Q22+ω12​ω22​Q12].H=P_{1}Q_{2}+\frac{P_{2}}{2}^{2}-\frac{1}{2}\left[(\omega_{1}^{2}+\omega_{2}^{2})Q^{2}_{2}+\omega_{1}^{2}\omega_{2}^{2}Q_{1}^{2}\right].(31)

It is important to emphasize that the Hamiltonian of Eq. (31) is not bounded from below, since it is linear inP1P_{1}. This feature reflects the well-known Ostrogradsky instability, which has been extensively discussed in the literature in the context of higher-order theories. In particular, the Pais–Uhlenbeck oscillator has served as a toy model to explore such instabilities and the appearance of so-called ghost degrees of freedom[41,31,40].

Using the Hamilton-Ostrogradsky equations from Eq.\eqrefE14, we have:{split}​Q˙1=∂H∂P1=Q2,Q˙2=∂H∂P2=P2,P˙1=−∂H∂Q1=ω12​ω22​Q1,P˙2=−∂H∂Q2=−P1+(ω12+ω22)​Q2.\split\dot{Q}_{1}&=\frac{\partial H}{\partial P_{1}}=Q_{2},\\
\dot{Q}_{2}&=\frac{\partial H}{\partial P_{2}}=P_{2},\\
\dot{P}_{1}&=-\frac{\partial H}{\partial Q_{1}}=\omega_{1}^{2}\omega_{2}^{2}Q_{1},\\
\dot{P}_{2}&=-\frac{\partial H}{\partial Q_{2}}=-P_{1}+(\omega_{1}^{2}+\omega_{2}^{2})Q_{2}.\,(32)

The solutions to these equations are given by:{aligned}​Q1​(t)=A1​cos⁡(ω1​t)+B1​sin⁡(ω1​t)+A2​cos⁡(ω2​t)+B2​sin⁡(ω2​t),\aligned Q_{1}(t)=A_{1}\cos(\omega_{1}t)+B_{1}\sin(\omega_{1}t)\\
+A_{2}\cos(\omega_{2}t)+B_{2}\sin(\omega_{2}t),(33){aligned}​Q2​(t)=ω1​[−A1​sin⁡(ω1​t)+B1​cos⁡(ω1​t)]+ω2​[−A2​sin⁡(ω2​t)+B2​cos⁡(ω2​t)],\aligned Q_{2}(t)=\omega_{1}\left[-A_{1}\sin(\omega_{1}t)+B_{1}\cos(\omega_{1}t)\right]\\
+\omega_{2}\left[-A_{2}\sin(\omega_{2}t)+B_{2}\cos(\omega_{2}t)\right],(34){aligned}​P1​(t)=[−A1​sin⁡(ω1​t)+B1​cos⁡(ω1​t)]​ω1​(2​ω12+ω22)+[−A2​sin⁡(ω2​t)+B2​cos⁡(ω2​t)]​ω2​(ω12+2​ω22),\aligned P_{1}(t)=\left[-A_{1}\sin(\omega_{1}t)+B_{1}\cos(\omega_{1}t)\right]\omega_{1}(2\omega_{1}^{2}+\omega_{2}^{2})\\
+\left[-A_{2}\sin(\omega_{2}t)+B_{2}\cos(\omega_{2}t)\right]\omega_{2}(\omega_{1}^{2}+2\omega_{2}^{2}),(35){aligned}​P2​(t)=[−A1​cos⁡(ω1​t)−B1​sin⁡(ω1​t)]​ω12+[−A2​cos⁡(ω2​t)−B2​sin⁡(ω2​t)]​ω22.\aligned P_{2}(t)=\left[-A_{1}\cos(\omega_{1}t)-B_{1}\sin(\omega_{1}t)\right]\omega_{1}^{2}\\
+\left[-A_{2}\cos(\omega_{2}t)-B_{2}\sin(\omega_{2}t)\right]\omega_{2}^{2}.(36)

These solutions are easily obtained knowing thatQ1​(t)=x1​(t)Q_{1}(t)=x_{1}(t), simply by using the relations that appear in Eq.\eqrefE33. Similarly, the same can be done forx2​(t)x_{2}(t), although we do not present it here since the results are similar and there is no need to repeat the mathematical procedures.

Note that these solutions satisfy the constraint given by Eq.\eqrefE12. A more direct calculation can be carried out by writingP1+P2˙−∂L∂x˙=(ω12+ω22)​Q2−(ω12+ω22)​x˙=0P_{1}+\dot{P_{2}}-\frac{\partial L}{\partial\dot{x}}=(\omega_{1}^{2}+\omega_{2}^{2})Q_{2}-(\omega_{1}^{2}+\omega_{2}^{2})\dot{x}=0

where we have used the last equation of\eqrefE33 together with the fact thatQ2=x˙Q_{2}=\dot{x}. This means that the constraints arising from the Hamilton-Ostrogradsky formulation are already satisfied in Eqs.\eqrefE34 to\eqrefE37.

Finally, it can be said that the Pais-Uhlenbeck oscillator model is not so simple to visualize in a first study, as we are not used to dealing with energies that depend on accelerations as seen inLPUL_{\mathrm{PU}}. However, the coupled oscillator model is easier to interpret and visualize. Due to the equivalence that coupled oscillators have with the Pais-Uhlenbeck oscillator, it becomes a good model to be given as an example in an initial approach to higher-order equations.

This work serves as a brief introduction to the Ostrogradsky formulation, emphasizing key aspects such as the Lagrange and Hamilton equations for higher-order systems. The interested reader can consult references[34,21,41,40]for a deeper understanding of the Ostrogradsky formulation for higher-order equations. For a more in-depth reading on the Pais-Uhlenbeck oscillator, refer to[27,31].

For the reader interested in practicing Ostrogradski’s method, we have provided a suggested exercise in Appendix C, the so-calledSnap Oscillator, a toy model whose Lagrangian depends on the acceleration squared[41]. This system leads to a fourth-order equation of motion in a straightforward way, making it suitable as an exercise for students to practice the use of higher-order Euler–Lagrange equations and the Ostrogradsky formalism. For this reason, we propose it as a pedagogical complement to the Pais–Uhlenbeck oscillator, providing a simpler entry point to the study of higher-order dynamics.

## VIConclusion

In this work, we provide a brief introduction to higher-order equations of motion. We then introduced the approach used by Ostrogradski to transition from the Lagrangian formalism with higher-order derivatives to the Hamiltonian formalism, which is known as the Hamilton-Ostrogradski formalism. Finally, we presented the model of two coupled oscillators and the Pais-Uhlenbeck model, whose Lagrangians are equivalent. The Lagrangian of the Pais-Uhlenbeck oscillator depends on second-order derivatives, which is not common in physics. On the other hand, the Lagrangian of two coupled oscillators depends on derivatives up to the first order and is a model that is easier to interpret.

It is an interesting issue that Nature, in general, is as far as we know described by laws that only involve derivatives up to second order. This issue has motivated several scholars to seek physical situations described by higher-order derivatives. It is believed that if such theoretical models can be experimentally proven, this would expand our understanding of nature.

We believe that the approach presented here can serve as an introductory basis to spark the curiosity of students interested in delving deeper into the Lagrangian and Hamiltonian formulations in the higher-order regime. Furthermore, this study can be extended in future works to address topics such as generalizations of Poisson brackets, conservation laws, Noether’s theorem, Liouville’s equation, and symplectic group symmetries in higher-order systems.

As a result, we hope that this work may help to stimulate interest in higher-order systems and encourage further studies that consolidate their role both in teaching and in research in theoretical physics.

## Acknowledgements

CAMM is grateful to FAPEMIG-Brazil (Grants APQ-00544- 23 and APQ-05218-23) for partial financial support and to DFA of UniCT and INFN-LNS-CT for the hospitality. This study was financed in part by the Coordenação de Aperfeiçoamento de Pessoal de Nível Superior – Brazil (CAPES) – Finance Code 001, Process No. 88887.820319/2023-00. Both authors are very grateful to the reviewers and editors, whose comments and suggestions helped to greatly improve this work.

## Appendix

## Appendix A: Higher-Order Lagrange Equations

For simplicity, let us assume that the system has only one degree of freedom and that the Lagrangian does not explicitly depend on time. Consider the LagrangianL=L​(q,q(1),q(2))L=L(q,q^{(1)},q^{(2)}), where we use the notationq(n)=dn​q/d​tnq^{(n)}=d^{n}q/dt^{n}to indicate thenn-th temporal derivative of the generalized coordinate. Thus,q(1)q^{(1)}andq(2)q^{(2)}are the first and second-order derivatives, respectively.

From the principle of least action, we can obtain the Lagrange equation for this type of Lagrangian:δ​S=δ​∫t1t2L​(q,q(1),q(2))​dt=0.\delta S=\delta\int_{t_{1}}^{t_{2}}L(q,q^{(1)},q^{(2)})\mathrm{d}t=0.(37)

By applying the variation to the right-hand side of Eq.\eqrefA2, we get:∫t1t2(∂L∂q​δ​q+∂L∂q˙​δ​q˙+∂L∂q¨​δ​q¨)​dt=0.\int_{t_{1}}^{t_{2}}\left(\frac{\partial L}{\partial q}\delta q+\frac{\partial L}{\partial\dot{q}}\delta\dot{q}+\frac{\partial L}{\partial\ddot{q}}\delta\ddot{q}\right)\mathrm{d}t=0.(38)

By imposing the condition thatδ​q​(t1)=δ​q​(t2)=δ​q˙​(t1)=δ​q˙​(t2)=0\delta q(t_{1})=\delta q(t_{2})=\delta\dot{q}(t_{1})=\delta\dot{q}(t_{2})=0, we can perform integration by parts to eliminateδ​q˙\delta\dot{q}andδ​q¨\delta\ddot{q}:{aligned}∫t1t2∂L∂q˙δq˙dt=∂L∂q˙δq|t1t2−∫t1t2dd​t(∂L∂q)δqdt==−∫t1t2dd​t(∂L∂q)δqdt.\aligned\int_{t_{1}}^{t_{2}}\frac{\partial L}{\partial\dot{q}}\,\delta\dot{q}\,\mathrm{d}t&=\left.\frac{\partial L}{\partial\dot{q}}\,\delta q\right|_{t_{1}}^{t_{2}}-\int_{t_{1}}^{t_{2}}\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial q}\right)\delta q\,\mathrm{d}t=\\
&=-\int_{t_{1}}^{t_{2}}\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial q}\right)\delta q\,\mathrm{d}t.(39){aligned}∫t1t2∂L∂q¨δq¨dt=∂L∂q¨δq˙|t1t2−∫t1t2dd​t(∂L∂q¨)δq˙dt==−∫t1t2dd​t(∂L∂q¨)δq˙dt==−dd​t(∂L∂q¨)δq|t1t2+∫t1t2d2d​t2(∂L∂q¨)δqdt==∫t1t2d2d​t2(∂L∂q¨)δqdt.\aligned\int_{t_{1}}^{t_{2}}\frac{\partial L}{\partial\ddot{q}}\,\delta\ddot{q}\,\mathrm{d}t&=\left.\frac{\partial L}{\partial\ddot{q}}\,\delta\dot{q}\right|_{t_{1}}^{t_{2}}-\int_{t_{1}}^{t_{2}}\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\ddot{q}}\right)\delta\dot{q}\,\mathrm{d}t=\\
&=-\int_{t_{1}}^{t_{2}}\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\ddot{q}}\right)\delta\dot{q}\,\mathrm{d}t=\\
&=-\left.\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\ddot{q}}\right)\delta q\right|_{t_{1}}^{t_{2}}+\int_{t_{1}}^{t_{2}}\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}}\left(\frac{\partial L}{\partial\ddot{q}}\right)\delta q\,\mathrm{d}t=\\
&=\int_{t_{1}}^{t_{2}}\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}}\left(\frac{\partial L}{\partial\ddot{q}}\right)\delta q\,\mathrm{d}t.(40)

Substituting the results from Eq.\eqrefA4 and\eqrefA5 into Eq.\eqrefA3, we get:∫t1t2(∂L∂q−dd​t​∂L∂q˙+d2d​t2​∂L∂q¨)​δ​q​dt=0.\int_{t_{1}}^{t_{2}}\left(\frac{\partial L}{\partial q}-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial\dot{q}}+\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}}\frac{\partial L}{\partial\ddot{q}}\right)\delta q\mathrm{d}t=0.(41)

Sinceδ​q\delta qis an arbitrary variation, we extract the Lagrange equation:∂L∂q−dd​t​(∂L∂q˙)+d2d​t2​(∂L∂q¨)=0.\frac{\partial L}{\partial q}-\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\dot{q}}\right)+\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}}\left(\frac{\partial L}{\partial\ddot{q}}\right)=0.(42)

To generalize the Lagrange equation to higher orders, consider a Lagrangian that depends on derivatives up to ordernn:L=L​(q,q(1),q(2),…,q(n)).L=L(q,q^{(1)},q^{(2)},...,q^{(n)}).(43)

To obtain the higher-order Lagrange equations, it is necessary to impose that222When the Lagrangian has the formL​(q,q˙,t)L(q,\dot{q},t), one must to impose the conditionsδ​q​(t1)=δ​q​(t2)=0\delta q(t_{1})=\delta q(t_{2})=0in order to obtain the Lagrange equations. If the Lagrangian depends on higher-order derivatives,L​(q,q˙,q¨,…,q(n),t)L(q,\dot{q},\ddot{q},\ldots,q^{(n)},t), analogous conditions must also be imposed for the variations of the derivatives up to ordern−1n-1, namelyδ​q(k)​(t1)=δ​q(k)​(t2)=0\delta q^{(k)}(t_{1})=\delta q^{(k)}(t_{2})=0fork=0,1,…,n−1k=0,1,\ldots,n-1.:δ​q(k)​(t1)=δ​q(k)​(t2)=0(k=1,…,n−1).\delta q^{(k)}(t_{1})=\delta q^{(k)}(t_{2})=0\quad(k=1,...,n-1).(44)

This will allow integration by parts such that onlyδ​q\delta qcoefficients appear. Following similar steps to then=2n=2case, the higher-order Lagrange equation is:∑k=0n(−1)k​dkd​tk​(∂L∂q(k))=0.\sum_{k=0}^{n}(-1)^{k}\frac{\mathrm{d}^{k}}{\mathrm{d}t^{k}}\left(\frac{\partial L}{\partial q^{(k)}}\right)=0.(45)

For a system withNNdegrees of freedom, there will be a set ofNNgeneralized coordinates andNNhigher-order Lagrange equations:∑k=0n(−1)k​dkd​tk​(∂L∂qi(k))=0(i=1,…,N).\sum_{k=0}^{n}(-1)^{k}\frac{\mathrm{d}^{k}}{\mathrm{d}t^{k}}\left(\frac{\partial L}{\partial q_{i}^{(k)}}\right)=0\quad(i=1,...,N).(46)

Here it is assumed that theNNgeneralized coordinates are all independent, meaning that theδ​qi\delta q_{i}are mutually independent and arbitrary.

## Appendix B: Higher-Order Hamilton Equations

In Appendix A we showed how to derive the Lagrange equation for a Lagrangian depending on up to second-order derivatives, and then, with some considerations, presented the general form of the Lagrange equation for derivatives up to ordernn.

In this appendix, we will show how to derive Hamilton’s equations for a Lagrangian depending on up to second-order derivatives, and then present the generalization of Hamilton’s equations to thenn-th order.

It is known that to switch from the Lagrangian formalism to the Hamiltonian formalism one uses the Legendre transformation. In the common case where the Lagrangian isL​(qi,q˙i,t)L(q_{i},\dot{q}_{i},t), the Legendre transformation takes the form:H​(qi,pi,t)=∑i=1N(pi​q˙i)−L​(qi,q˙i,t),H(q_{i},p_{i},t)=\sum_{i=1}^{N}(p_{i}\dot{q}_{i})-L(q_{i},\dot{q}_{i},t),(47)

wherepip_{i}is the conjugate momentum, defined as:pi=∂L∂q˙i(i=1,…,N).p_{i}=\frac{\partial L}{\partial\dot{q}_{i}}\quad(i=1,\dots,N).(48)

Let the Hessian matrix be formed by elementsWi​jW_{ij}, given by:Wi​j=∂2L∂q˙i​∂q˙j(i,j=1,…,N).W_{ij}=\frac{\partial^{2}L}{\partial\dot{q}_{i}\,\partial\dot{q}_{j}}\quad(i,j=1,\dots,N).(49)

If the Hessian matrix is regular, i.e., has nonzero determinant, then one can solve theNNequations of Eq.\eqrefB2 to express theq˙i\dot{q}_{i}as functions ofqiq_{i},pip_{i}, andtt. Substituting these expressions into Eq.\eqrefB1 yields the Hamiltonian.

Hamilton’s equations form a set of2​N2Nfirst-order differential equations:q˙i=∂H∂pi,p˙i=−∂H∂qi(i=1,…,N).\dot{q}_{i}=\frac{\partial H}{\partial p_{i}},\quad\dot{p}_{i}=-\frac{\partial H}{\partial q_{i}}\quad(i=1,\dots,N).(50)

Like the Lagrange equations, Hamilton’s equations yield the equations of motion, but whereas the Lagrange equations are second order, Hamilton’s equations are first order. The Lagrangian formalism deals withNNequations inNNgeneralized coordinates(q1,…,qN)(q_{1},\dots,q_{N}), while the Hamiltonian formalism involves2​N2Nequations in the2​N2Nvariables(q1,…,qN,p1,…,pN)(q_{1},\dots,q_{N},p_{1},\dots,p_{N}).

When considering higher-order derivatives, the Legendre transformation as given in Eq.\eqrefB1 is no longer sufficient. One must generalize the Legendre transformation to handle new coordinates and momenta.

For simplicity, let us again consider a system with a single degree of freedom. If the Lagrangian is of the typeL​(q,q˙,q¨)L(q,\dot{q},\ddot{q}), the Lagrange equation reads:∂L∂q−dd​t​(∂L∂q˙)+d2d​t2​(∂L∂q¨)=0.\frac{\partial L}{\partial q}-\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\dot{q}}\right)+\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}}\left(\frac{\partial L}{\partial\ddot{q}}\right)=0.(51)

New canonical variables are then defined as:{aligned}​Q1=q,Q2=q˙,P1=∂L∂q˙−dd​t​(∂L∂q¨),P2=∂L∂q¨.\aligned Q_{1}&=q,&\quad Q_{2}&=\dot{q},\\
P_{1}&=\frac{\partial L}{\partial\dot{q}}-\frac{\mathrm{d}}{\mathrm{d}t}\!\left(\frac{\partial L}{\partial\ddot{q}}\right),&\quad P_{2}&=\frac{\partial L}{\partial\ddot{q}}.(52)

whereQ1Q_{1}andQ2Q_{2}are the new generalized coordinates andP1P_{1}andP2P_{2}are the corresponding momenta. Note that these definitions introduce constraints, for example:∂L∂q˙=P1+P˙2.\frac{\partial L}{\partial\dot{q}}=P_{1}+\dot{P}_{2}.(53)

Hence, the coordinates and momenta are not all independent. BecauseP2P_{2}depends onqq,q˙\dot{q}, andq¨\ddot{q}, to invert this relation and expressq¨\ddot{q}as a function ofqq,q˙\dot{q}, andP2P_{2}, the Hessian must be regular. In this higher-order case the Hessian matrix is formed by derivatives with respect to the generalized accelerations:Wi​j=∂2L∂q¨i​∂q¨j(i,j=1,…,N).W_{ij}=\frac{\partial^{2}L}{\partial\ddot{q}_{i}\,\partial\ddot{q}_{j}}\quad(i,j=1,\dots,N).(54)

In the one-dimensional case, this reduces to a single element:W=∂2L∂q¨2.W=\frac{\partial^{2}L}{\partial\ddot{q}^{2}}.(55)

Ifdet(W)≠0\det(W)\neq 0, one can write:q¨=q¨​(q,q˙,P2)=q¨​(Q1,Q2,P2).\ddot{q}=\ddot{q}(q,\dot{q},P_{2})=\ddot{q}(Q_{1},Q_{2},P_{2}).(56)

To derive the Legendre transformation, start from the differential of the Lagrangian:d​L=∂L∂q​d​q+∂L∂q˙​d​q˙+∂L∂q¨​d​q¨.\mathrm{d}L=\frac{\partial L}{\partial q}\,\mathrm{d}q+\frac{\partial L}{\partial\dot{q}}\,\mathrm{d}\dot{q}+\frac{\partial L}{\partial\ddot{q}}\,\mathrm{d}\ddot{q}.(57)

Using the definitions in Eq.\eqrefB6, this becomes:d​L=P˙1​d​Q1+(P1+P˙2)​d​Q2+P2​d​q¨.\mathrm{d}L=\dot{P}_{1}\,\mathrm{d}Q_{1}+(P_{1}+\dot{P}_{2})\,\mathrm{d}Q_{2}+P_{2}\,\mathrm{d}\ddot{q}.(58)

To obtain only differentials ofQiQ_{i}andPiP_{i}, apply the identityq¨​d​P=d​(P​q¨)−P​d​q¨\ddot{q}\,dP=d(P\,\ddot{q})-P\,d\ddot{q}, yielding:d​L=d​(P1​Q2+q¨​P2)+P˙1​d​Q1−Q2​d​P1+P˙2​d​Q2−q¨​d​P2.\mathrm{d}L=\mathrm{d}\bigl(P_{1}Q_{2}+\ddot{q}\,P_{2}\bigr)+\dot{P}_{1}\,\mathrm{d}Q_{1}-Q_{2}\,\mathrm{d}P_{1}+\dot{P}_{2}\,\mathrm{d}Q_{2}-\ddot{q}\,\mathrm{d}P_{2}.(59)

Equation\eqrefB13 can now be used to define the differential of the Hamiltonian function for a higher order theory:{aligned}dH=d(P1Q2+q¨P2−L)==−P˙1dQ1+Q2dP1−P˙2dQ2+q¨dP2.\aligned\mathrm{d}H&=\mathrm{d}\bigl(P_{1}Q_{2}+\ddot{q}\,P_{2}-L\bigr)=\\
&=-\dot{P}_{1}\,\mathrm{d}Q_{1}+Q_{2}\,\mathrm{d}P_{1}-\dot{P}_{2}\,\mathrm{d}Q_{2}+\ddot{q}\,\mathrm{d}P_{2}.(60)

This last equation provides the precise expression for the differential of the Hamiltonian in terms of the canonical variables. The relevance of this formulation lies in ensuring that the formalism preserves the canonical structure of Hamiltonian mechanics, allowing the time evolution to be described through the generalized Hamilton equations. With this result in hand, the Legendre transformation can be written as:H​(Q1,Q2,P1,P2)=P1​Q2+P2​q¨−L​(Q1,Q2,q¨).H(Q_{1},Q_{2},P_{1},P_{2})=P_{1}Q_{2}+P_{2}\ddot{q}-L(Q_{1},Q_{2},\ddot{q}).(61)

whereq¨=q¨​(Q1,Q2,P2)\ddot{q}=\ddot{q}(Q_{1},Q_{2},P_{2}). Note also thatQ2=d​qd​t=Q˙1,q¨=d​q˙d​t=Q˙2Q_{2}=\frac{\mathrm{d}q}{\mathrm{d}t}=\dot{Q}_{1},\quad\ddot{q}=\frac{\mathrm{d}\dot{q}}{\mathrm{d}t}=\dot{Q}_{2}(62)

Hence, for a Lagrangian depending onq¨\ddot{q}, the Legendre transformation reads:H=P1​Q˙1+P2​Q˙2−L.H=P_{1}\dot{Q}_{1}+P_{2}\dot{Q}_{2}-L.(63)

From Eq.\eqrefB14 we then read off Hamilton’s equations:Q˙1=∂H∂P1,Q˙2=∂H∂P2,P˙1=−∂H∂Q1,P˙2=−∂H∂Q2.\dot{Q}_{1}=\frac{\partial H}{\partial P_{1}},\quad\dot{Q}_{2}=\frac{\partial H}{\partial P_{2}},\quad\dot{P}_{1}=-\frac{\partial H}{\partial Q_{1}},\quad\dot{P}_{2}=-\frac{\partial H}{\partial Q_{2}}.(64)

Note that Eq.\eqrefB5 is a single fourth-order equation in one variable, whereas Eq.\eqrefB18 is a system of four first-order equations in four variables.

For the general case of a Lagrangian depending on derivatives up to ordernn:L=L​(q,q(1),q(2),…,q(n)),L=L(q,q^{(1)},q^{(2)},\dots,q^{(n)}),(65)

withq(1)=q˙q^{(1)}=\dot{q},q(2)=q¨q^{(2)}=\ddot{q}, etc., one defines:Qk=q(k−1)(k=1,…,n)Q_{k}=q^{(k-1)}\quad(k=1,\dots,n)(66)

andPk=∑m=kn(−1)m−k​dm−kd​tm−k​(∂L∂q(m))(k=1,…,n).P_{k}=\sum_{m=k}^{n}(-1)^{m-k}\frac{\mathrm{d}^{m-k}}{\mathrm{d}t^{m-k}}\left(\frac{\partial L}{\partial q^{(m)}}\right)\qquad(k=1,\dots,n).(67)

The general Legendre transformation is:H=∑k=1nPk​Q˙k−L,H=\sum_{k=1}^{n}P_{k}\dot{Q}_{k}-L,(68)

and the higher-order Hamilton equations take the form:Q˙k=∂H∂Pk,P˙k=−∂H∂Qk(k=1,…,n).\dot{Q}_{k}=\frac{\partial H}{\partial P_{k}},\quad\dot{P}_{k}=-\frac{\partial H}{\partial Q_{k}}\quad(k=1,\dots,n).(69)

## Appendix C: Proposed Exercise

This appendix presents a didactic exercise designed for the student to apply and consolidate some of the concepts discussed in this work. We introduce here a simple model that we call theSnap Oscillator[41], since its equation of motion involves time derivatives up to fourth order. Its Lagrangian is defined asL​(x,x˙,x¨)=−ϵ​m2​ω2​x¨2+m2​x˙2−m​ω22​x2,L(x,\dot{x},\ddot{x})=-\frac{\epsilon m}{2\omega^{2}}\ddot{x}^{2}+\frac{m}{2}\dot{x}^{2}-\frac{m\omega^{2}}{2}x^{2},(70)

whereϵ>0\epsilon>0is a constant parameter.
- 1.

Using the higher-order Euler–Lagrange equation, derive the equation of motion for the Snap Oscillator.
- 2.

Solve the resulting equation of motion. Discuss the limitϵ→0\epsilon\to 0, and verify explicitly whether the solution reduces to that of the simple harmonic oscillator. Note that the most appropriate way to do this limit is using theSingular Perturbation Theory[7,OMalley1991SingularPM].
- 3.

Apply Ostrogradsky’s formalism to this problem. In particular, determine the canonical variables:{aligned}​Q1=x,Q2=x˙,P1=∂L∂x˙−dd​t​(∂L∂x¨),P2=∂L∂x¨.\aligned Q_{1}&=x,&\quad Q_{2}&=\dot{x},\\
P_{1}&=\frac{\partial L}{\partial\dot{x}}-\frac{d}{dt}\!\left(\frac{\partial L}{\partial\ddot{x}}\right),&\quad P_{2}&=\frac{\partial L}{\partial\ddot{x}}.

ComputeP1P_{1}andP2P_{2}explicitly.
- 4.

Construct the HamiltonianH​(Q1,Q2,P1,P2)H(Q_{1},Q_{2},P_{1},P_{2})using the generalized Legendre transformation.

## References
- [1]M. Abraham(1905)Theorie der elektrizität: elektromagnetische theorie der strahlung.Teubner,Leipzig.Cited by:§I.
- [2]V. I. Arnol’d(2013)Mathematical methods of classical mechanics.Vol.60,Springer Science & Business Media.Cited by:§I.
- [3]M. Bertin, B. Pimentel, and P. Pompeia(2008)Formalismo de hamilton-jacobi à la carathéodory. parte 2: sistemas singulares.Revista Brasileira de Ensino de Física30,pp. 3310–1.Cited by:§II.
- [4]L. Borges, F. Barone, C. de Melo, and F. Barone(2019)Higher order derivative operators as quantum corrections.Nuclear Physics B944,pp. 114634.Cited by:§I.
- [5]J. D. Brown(2023-03)Singular lagrangians and the dirac–bergmann algorithm in classical mechanics.American Journal of Physics91(3),pp. 214–224.External Links:ISSN 0002-9505,Document,Link,https://pubs.aip.org/aapt/ajp/article-pdf/91/3/214/20103652/214_1_5.0107540.pdfCited by:§II,§III.
- [6]L. Caro, B. Pimentel, and G. Zambrano(2021)Método de faddeev-jackiw na mecânica clássica.Revista Brasileira de Ensino de Física43,pp. e20210273.Cited by:§I,§II.
- [7]L. Y. Chen, N. Goldenfeld, and Y. Oono(1995)Renormalization group and singular perturbations: multiple scales, boundary layers, and reductive perturbation theory..Physical review. E, Statistical physics, plasmas, fluids, and related interdisciplinary topics54 1,pp. 376–394.External Links:LinkCited by:item 2.
- [8]D. Comelli, M. Di Giambattista, and L. Pilo(2022)Classical and quantum dynamics of gyroscopic systems and dark energy.Journal of Cosmology and Astroparticle Physics2022(11),pp. 017.Cited by:§I.
- [9]R. R. Cuzinatto, C. A. de Melo, L. G. Medeiros, and P. J. Pompeia(2011)Cosmic acceleration from second order gauge gravity.Astrophysics and Space Science332(1),pp. 201–208.Cited by:§I.
- [10]R. Cuzinatto, C. de Melo, L. Medeiros, and P. Pompeia(2008)Gauge formulation for higher order gravity.The European Physical Journal C53(1),pp. 99–108.Cited by:§I.
- [11]R. Cuzinatto, C. De Melo, L. Medeiros, and P. Pompeia(2011)How can one probe podolsky electrodynamics?.International Journal of Modern Physics A26(21),pp. 3641–3651.Cited by:§I.
- [12]R. Cuzinatto, C. De Melo, L. Medeiros, and P. Pompeia(2015)Observational constraints on a phenomenologicalf​(R,∂R)f(R,\partial R)-model.General Relativity and Gravitation47(3),pp. 29.Cited by:§I.
- [13]R. Cuzinatto, C. De Melo, L. Medeiros, and P. Pompeia(2016)Scalar-multi-tensorial equivalence for higher orderf​(R,∇μR,∇μ1∇μ2⁡R,…,∇μ1…​∇μnR)f(R,{\nabla}_{\mu}R,{\nabla}_{{\mu}_{1}}{\nabla}_{{\mu}_{2}}R,\dots{},{\nabla}_{{\mu}_{1}}\dots{}{\nabla}_{{\mu}_{n}}R)theories of gravity.Physical Review D93(12),pp. 124034.Cited by:§I.
- [14]R. Cuzinatto, C. De Melo, L. Medeiros, and P. Pompeia(2019)f​(R,∇μ1R,…,∇μ1…​∇μnR)f(R,{\nabla}_{{\mu}_{1}}R,\dots{},{\nabla}_{{\mu}_{1}}\dots{}{\nabla}_{{\mu}_{n}}R)Theories of gravity in einstein frame: a higher order modified starobinsky inflation model in the palatini approach.Physical Review D99(8),pp. 084053.Cited by:§I.
- [15]R. Cuzinatto, C. De Melo, and P. Pompeia(2007)Second order gauge theory.Annals of Physics322(5),pp. 1211–1232.Cited by:§I.
- [16]P. A. M. Dirac(1938)Classical theory of radiating electrons.Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences167(929),pp. 148–169.Cited by:§I.
- [17]M. Elbistan(2022)Circularly polarized periodic gravitational wave and the pais-uhlenbeck oscillator.Nuclear Physics B.External Links:LinkCited by:§I.
- [18]D. A. Eliezer and R. P. Woodard(1989-07)Instability of higher-difference initial-value theories.Phys. Rev. D40,pp. 465–472.External Links:Document,LinkCited by:§I.
- [19]H. Goldstein, C. Poole, and J. Safko(2002)Classical mechanics.American Association of Physics Teachers.Cited by:§I.
- [20]M. B. Green, J. H. Schwarz, and E. Witten(1987)Superstring theory.Vol.1 and 2,Cambridge University Press.Cited by:§I.
- [21]C. Grosse-Knetter(1993)Effective lagrangians with higher order derivatives.arXiv preprint hep-ph/9306321.Cited by:§V.
- [22]P. Guha(2020)Curl forces and their role in optics and ion trapping.The European Physical Journal D74,pp. 1–12.External Links:LinkCited by:§I.
- [23]J. D. Jackson(1999)Classical electrodynamics.3rd edition,Wiley,New York.Cited by:§I.
- [24]F. Kleefeld(2023)On the equivalence of the pais-uhlenbeck oscillator model and two non-hermitian harmonic oscillators.arXiv preprint arXiv:2302.14621.Cited by:§IV.
- [25]H. A. Lorentz(1909)The theory of electrons and its applications to the phenomena of light and radiant heat.Teubner,Leipzig.Cited by:§I.
- [26]H. Lü, A. Perkins, C. Pope, and K. S. Stelle(2015)Spherically symmetric solutions in higher-derivative gravity.Physical Review D92(12),pp. 124019.Cited by:§I.
- [27]L. O. Mendes(2017)Um estudo de teorias com derivadas superiores: o oscilador de pais-uhlenbeck.Master’s Thesis,Universidade Estadual de Maringá.Cited by:§I,§IV,§V.
- [28]V. Mukhanov and A. Wipf(1995)On the symmetries of hamiltonian systems.International Journal of Modern Physics A10(04),pp. 579–610.Cited by:§V.
- [29]M. Ostrogradsky(1850)Memoires sur les equations differentielles relatives au probleme des isoperimetres.Mem. Acad. St. Petersbourg6(4),pp. 385–517.Cited by:§I,§III.
- [30]A. Pais and G. Uhlenbeck(1950)On field theories with non-localized action.Physical Review79(1),pp. 145.Cited by:§I.
- [31]M. Pavšič(2016)Pais–uhlenbeck oscillator and negative energies.International Journal of Geometric Methods in Modern Physics13(09),pp. 1630015.Cited by:§V,§V.
- [32]B. Podolsky(1942)A generalized electrodynamics part i—non-quantum.Physical Review62(1-2),pp. 68.Cited by:§I.
- [33]J. Polchinski(2007-12)String theory. Vol. 1: An introduction to the bosonic string.Cambridge Monographs on Mathematical Physics,Cambridge University Press.External Links:Document,ISBN 978-0-511-25227-3, 978-0-521-67227-6, 978-0-521-63303-1Cited by:§I.
- [34]M. Rashid and S. Khalil(1996)Hamiltonian description of higher order lagrangians.International Journal of Modern Physics A11(25),pp. 4551–4559.Cited by:§III,§V.
- [35]F. Rohrlich(2007)Classical charged particles.3rd edition,World Scientific,Singapore.Cited by:§I.
- [36]I. L. Shapiro(2008)Effective action of vacuum: the semiclassical approach.Classical and Quantum Gravity25(10),pp. 103001.Cited by:§I.
- [37]T. Sotiriou and V. Faraoni(2008)F(r) theories of gravity.Reviews of Modern Physics82,pp. 451–497.External Links:LinkCited by:§I.
- [38]H. Spohn(2004)Dynamics of charged particles and their radiation field.Cambridge university press.Cited by:§I.
- [39]K. Stelle(1978)Classical gravity with higher derivatives.General Relativity and Gravitation9(4),pp. 353–371.Cited by:§I.
- [40]E. Svanberg(2022)Theories with higher-order time derivatives and the ostrogradsky ghost.arXiv preprint arXiv:2211.14319.Cited by:§V,§V.
- [41]R. P. Woodard(2015)The theorem of ostrogradsky.arXiv preprint arXiv:1506.02210.Cited by:§I,§V,§V,§V,Appendix C: Proposed Exercise.
- [42]B. Zwiebach(2009)A first course in string theory.2 edition,Cambridge University Press.Cited by:§I.

## 


- 


Major funding support from
