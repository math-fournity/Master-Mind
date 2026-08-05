# The History of Hilbert-Space Formulations of Classical Physics

**arXiv ID**: 2607.17408v1
**Authors**: Jacob A. Barandes
**Published**: 2026-07-19
**Categories**: physics.hist-ph, quant-ph
**Comments**: 21 pages, no figures, accepted version for publication
**DOI**: 10.1140/epjh/s13129-025-00113-x
**HTML URL**: https://arxiv.org/html/2607.17408v1

## Abstract

Hilbert-space techniques are widely used not only for quantum theory, but also for classical physics. Two important examples are the Koopman-von Neumann (KvN) formulation and the method of ``classical'' wave functions. As this paper explains, these two approaches are conceptually distinct. In particular, the method of classical wave functions was not due to Bernard Koopman and John von Neumann, but was developed independently by a number of later researchers, perhaps first by Mario Schönberg, with key contributions from Angelo Loinger, Giacomo Della Riccia, Norbert Wiener, and E. C. George Sudarshan. The primary goals of this paper are to explain these two approaches, describe the relevant history in detail, and give credit where credit is due.

## Full Text

The History of Hilbert-Space Formulations of Classical Physics

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
- License: CC BY 4.0arXiv:2607.17408v1 [physics.hist-ph] 19 Jul 2026

## The History of Hilbert-Space Formulations of Classical PhysicsJacob A. BarandesDepartments of Philosophy and Physics, Harvard University, Cambridge, MA 02138; jacob_barandes@harvard.edu; ORCID: 0000-0002-3740-4418This manuscript is the accepted version, as published inThe European Physical Journal H(DOI:10.1140/epjh/s13129-025-00113-x).

## Abstract

Hilbert-space techniques are widely used not only for quantum theory,
but also for classical physics. Two important examples are the Koopman–von
Neumann (KvN) formulation and the method of “classical” wave functions.
As this paper explains, these two approaches are conceptually distinct.
In particular, the method of classical wave functions was not due
to Bernard Koopman and John von Neumann, but was developed independently
by a number of later researchers, perhaps first by Mario Schönberg,
with key contributions from Angelo Loinger, Giacomo Della Riccia,
Norbert Wiener, and E. C. George Sudarshan. The primary goals of this
paper are to explain these two approaches, describe the relevant history
in detail, and give credit where credit is due.

## 1Introduction

In 1931, Bernard Koopman published a paper titled “Hamiltonian Systems
and Transformations in Hilbert Space” inProceedings of the
National Academy of Sciences(Koopman 1931).
Koopman’s paper laid out a novel method for identifying functions
representing observables on a classical system’s phase space as vectors
in a new kind of Hilbert space. In 1932, John von Neumann published
a pair of follow-up papers in German inAnnals of Mathematics(von Neumann 1932a, 1932b)
further developing Koopman’s method.

Koopman’s use of Greek letters and complex values for his phase-space
functions may have made it easy to confuse them with classical versions
of the state vectors or wave functions of quantum mechanics, and von
Neumann’s two papers were never translated into English. Koopman and
von Neumann’s papers, however, did not refer to classical state vectors
or wave functions, and their Hilbert spaces consisted of functions
representing classical observables, which naturally corresponded to
quantum-mechanical operators evolving in time in the Heisenberg picture.
Indeed, as Jordan and Sudarshan noted in a 1961 paper published inJournal of Mathematical Physics:

It was shown by Koopman how the dynamical transformations of classical
mechanics, considered as measure preserving transformations of the
phase space, induce unitary transformations on the Hilbert space of
functions which are square integrable with respect to a density function
over the phase space. This Hilbert space formulation of classical
mechanics was further developed by von Neumann. It is to be noted
that this Hilbert space corresponds not to the space of state vectors
in quantum mechanics but to the Hilbert space of operators on the
state vectors (with the trace of the product of two operators being
chosen as the scalar product). [Jordan, Sudarshan 1961, pp. 515–516]

Danilo Mauro wrote an innovative and influential 2002 paper titled
“On Koopman–von Neumann Waves” (Mauro 2002),
later expanding on his work in his 2003 PhD thesis, titled “Topics
in Koopman–von Neumann Theory” (Mauro 2003).
The paper and thesis replaced the observables-as-vectors method described
above with an important but different technique. This different technique
was to use complex-valued “classical” wave functionsψ\psiin
place of classical probability distributionsρ\rho, where these
classical wave functions and classical probability distributions were
explicitly related by the modulus-square operation,ρ=|ψ|2\rho=|\psi|^{2},
in analogy with the Born rule. However, this method of classical wave
functions was due to other researchers who came decades after Koopman
and von Neumann’s papers from the 1930s—perhaps the first
being Mario Schönberg, working in the 1950s.

Ever since this accidental misattribution, the “Koopman–von
Neumann (KvN) formulation” has been widely but incorrectly employed
to refer to the method of classical wave functions. For example, an
international conference in 2021 and an accompanying special issue
ofJournal of Physics Ain 2022, both titled “Koopman Methods
in Classical and Classical-Quantum Mechanics,” referred in their
abstracts to “Koopman–von Neumann wave functions” (Bondar
et al., 2021, 2022).
As of the writing of this paper, the Wikipedia entry “Koopman–von
Neumann Classical Mechanics” (Wikipedia 2025)
opens up its derivation of the framework with the following statement:

In the approach of Koopman and von Neumann (KvN), dynamics in phase
space is described by a (classical) probability density, recovered
from an underlying wavefunction—the Koopman–von
Neumann wavefunction—as the square of its absolute value
(more precisely, as the amplitude multiplied with its own complex
conjugate).

The main purpose of the present paper is to lay out the detailed history
of both the Koopman–von Neumann formulation and the method
of classical wave functions, and assign credit appropriately.

Ultimately, it turns out that the Hilbert spaces that arise from treating
observables as vectors and the Hilbert spaces that arise from classical
wave functions are mathematically equivalent. This equivalence between
the two kinds of Hilbert spaces is an elementary result of the GNS
construction (Gelfand, Naimark 1943; Segal 1947),
which takes the elementsf,g,…f,g,\dotsof a C*-algebra (representing
observables) together with a positive, normalized linear functionalω\omegain the dual space of the C*-algebra (representing a quantum
state), and combines them to form a rudimentary inner product(f,g)≡ω(f⋆g)\mathopen{}\mathclose{{\left(f,g}}\right)\equiv\omega\mathopen{}\mathclose{{\left(f^{\star}g}}\right)that eventually underwrites the definition of a Hilbert space representing
the original C*-algebra. However, despite this underlying connection
between, on the one hand, the original observables-as-vectors method
of Koopman and von Neumann, and, on the other hand, the classical-wave-function
method that came later, these are conceptually different methods.
Simply put, Koopman and von Neumann did not come up with the idea
of using classical wave functions to capture classical probability
distributions.

By analogy, Heisenberg’s matrix mechanics (Heisenberg 1925)
and Schrödinger’s wave mechanics (Schrödinger 1926)
were conceptually different frameworks. It was Schrödinger who came
up with the idea of quantum-mechanical wave functions, and it would
not be correct to give credit to Heisenberg for that idea, even though
matrix mechanics and wave mechanics were eventually connected to each
other by modern Hilbert-space formulations of quantum theory.

## 2Hilbert-Space Formulations of Classical Physics

## 2.1Bernard Koopman

Koopman began his 1931 paper with the following motivation:

In recent years the theory of Hilbert space and its linear transformations
has come into prominence. […] It is the object of this note
to outline certain investigations of our own in which the domain of
this theory has been extended in such a way as to include classical
Hamiltonian mechanics, or, more generally, systems defining a steadynn-dimensional flow of a fluid of positive density. [Koopman 1931,
p. 315]

Shortly thereafter, Koopman described his basic approach:

The starting point of our investigation is theNN-dimensional varietyΩ\Omegaand the group of automorphismsStS_{t}having the positive
integral invariant∫ρ​𝑑ω\int\rho\,d\omega, and these are considered
without reference to the problem which gave them origin. Letφ=φ(A)\varphi=\varphi\mathopen{}\mathclose{{\left(A}}\right)be a complex-valued function of the pointAAofΩ\Omega, restricted
only as follows: (i)φ\varphiis single-valued; (ii)φ\varphiis measurable; (iii) the Lebesgue integrals∫Ωρ​|φ|​𝑑ω\int_{\Omega}\rho|\varphi|d\omegaand∫Ωρ​|φ|2​𝑑ω\int_{\Omega}\rho|\varphi|^{2}d\omegaare finite. The
totality of such functionsφ\varphiconstitutes the aggregate of
points of a Hilbert spaceℌ\mathfrak{H}: the metric of which is
determined by the “inner product”(φ,ψ)=∫Ωρφψ¯dω.\mathopen{}\mathclose{{\left(\varphi,\psi}}\right)=\int_{\Omega}\rho\varphi\bar{\psi}d\omega.(1)

[Ibid., p. 316]

Notice the functionρ\rhoappearing in Koopman’s integral measures,
separate from the functionsφ\varphiandψ\psi. As Koopman wrote,
“here,ρ\rhois a positive, single-valued, analytic function onΩ\Omega. This is a consequence of the fact that∫𝑑q1​…​𝑑qn​𝑑p1​…​𝑑pn\int dq_{1}\dots dq_{n}dp_{1}\dots dp_{n}is an integral invariant of the system” (Ibid., p. 315). Later,
Koopman added: “Ifttrepresents the time,StS_{t}specifies
the steady flow of a fluid of densityρ\rhooccupying the spaceΩ\Omega” (Ibid., p. 316). After introducing Gaussian coordinatesξ1,…,ξN\xi_{1},\dots,\xi_{N}, with corresponding velocitiesΞk=d​ξk/d​t\Xi_{k}=d\xi_{k}/dt,
Koopman wrote:

The property ofρ=ρ(ξ1,…,ξN)\rho=\rho\mathopen{}\mathclose{{\left(\xi_{1},\dots,\xi_{N}}}\right)is
expressed by the “equation of continuity”∑k=1N∂(ρΞk)∂ξk=0.\sum^{N}_{k=1}\frac{\partial\mathopen{}\mathclose{{\left(\rho\Xi_{k}}}\right)}{\partial\xi_{k}}=0.(2)

These statements make clear that Koopman’s functionsφ\varphiandψ\psiwere not related to probability densities, and that his density
functionρ\rhowas a separate mathematical object that partly defined
Koopman’s Hilbert space. Koopman did not suggest that his functionsφ\varphiandψ\psishould include classical wave functions, or
be related to a probability density by the modulus-square operation.

In Koopman’s paper, he defined the time evolution of his functionsφ,ψ,…\varphi,\psi,\dotsusing a transformationUtU_{t}defined byUtφ(A)≡φ(StA),U_{t}\varphi\mathopen{}\mathclose{{\left(A}}\right)\equiv\varphi\mathopen{}\mathclose{{\left(S_{t}A}}\right),(3)

whereAAis a given phase-space point and whereSt​AS_{t}Ais the
new phase-space point after a durationttof classical Hamiltonian
time evolution. Working in coordinates for the given2​n2n-dimensional
phase space, so that one can denote a phase-space point asA=(q,p)≡(q1,…,qn;p1,…,pn)A=\mathopen{}\mathclose{{\left(q,p}}\right)\equiv\mathopen{}\mathclose{{\left(q_{1},\dots,q_{n};p_{1},\dots,p_{n}}}\right),
one has a coordinate representation of Koopman’s notion of time evolution,St(q,p)≡(q(t),p(t)),S_{t}\mathopen{}\mathclose{{\left(q,p}}\right)\equiv\mathopen{}\mathclose{{\left(q\mathopen{}\mathclose{{\left(t}}\right),p\mathopen{}\mathclose{{\left(t}}\right)}}\right),(4)

and soUtφ(A)U_{t}\varphi\mathopen{}\mathclose{{\left(A}}\right)has time derivative given bydd​tUtφ(A)\displaystyle\frac{d}{dt}U_{t}\varphi\mathopen{}\mathclose{{\left(A}}\right)=dd​tφ(StA)\displaystyle=\frac{d}{dt}\varphi\mathopen{}\mathclose{{\left(S_{t}A}}\right)=dd​tφ(q(t),p(t))\displaystyle=\frac{d}{dt}\varphi\mathopen{}\mathclose{{\left(q\mathopen{}\mathclose{{\left(t}}\right),p\mathopen{}\mathclose{{\left(t}}\right)}}\right)=∑k=1n∂φ∂qk​dqk(t)d​t+∑k=1n∂φ∂pk​dpk(t)d​t\displaystyle=\sum^{n}_{k=1}\frac{\partial\varphi}{\partial q_{k}}\frac{dq_{k}\mathopen{}\mathclose{{\left(t}}\right)}{dt}+\sum^{n}_{k=1}\frac{\partial\varphi}{\partial p_{k}}\frac{dp_{k}\mathopen{}\mathclose{{\left(t}}\right)}{dt}=∑k=1n(∂φ∂qk∂H∂pk−∂φ∂pk∂H∂qk)\displaystyle=\sum^{n}_{k=1}\mathopen{}\mathclose{{\left(\frac{\partial\varphi}{\partial q_{k}}\frac{\partial H}{\partial p_{k}}-\frac{\partial\varphi}{\partial p_{k}}\frac{\partial H}{\partial q_{k}}}}\right)={φ,H},\displaystyle=\mathopen{}\mathclose{{\left\{\varphi,H}}\right\},

which is the appropriate time-evolution equation for a function representing
a classical observable, with{φ,H}\mathopen{}\mathclose{{\left\{\varphi,H}}\right\}the usual
Poisson bracket ofφ\varphiandHH. Introducing the standard formula
for the Liouvillian operatorLL,L≡i{H,}≡i∑k=1n(∂H∂qk∂∂pk−∂H∂pk∂∂qk),L\equiv i\mathopen{}\mathclose{{\left\{H,\phantom{x}}}\right\}\equiv i\sum^{n}_{k=1}\mathopen{}\mathclose{{\left(\frac{\partial H}{\partial q_{k}}\frac{\partial}{\partial p_{k}}-\frac{\partial H}{\partial p_{k}}\frac{\partial}{\partial q_{k}}}}\right),(5)

one can recast the time-evolution equation forφ\varphias111Koopman wrote in his paper that “if the values ofφ(A)\varphi\mathopen{}\mathclose{{\left(A}}\right)be regarded as being attached to the respective pointsAAof the
fluid whent=0t=0, in the course of the flow these values will be
carried into those of the functionU−tφ(A)U_{-t}\varphi\mathopen{}\mathclose{{\left(A}}\right)”
(Koopman 1931, p. 316). This picture led Koopman to calculate instead[(∂/∂t)Utφ(A)]t=0=iPφ(A)\mathopen{}\mathclose{{\left[\mathopen{}\mathclose{{\left(\partial/\partial t}}\right)U_{t}\varphi\mathopen{}\mathclose{{\left(A}}\right)}}\right]_{t=0}=iP\varphi\mathopen{}\mathclose{{\left(A}}\right),
wherePPdiffered by an overall sign from the usual definition of
the Liouvillian operatorLLin (5). Koopman’s
equation, however, was not a time-evolution equation in the usual
sense of describing the behavior of a given function at arbitrary
timestt. Instead, Koopman treated his equation merely as a mathematical
step toward writing down a self-adjoint generatorPPfor his transformationUtU_{t}.dd​tUtφ(A)={φ,H}=iLφ.\frac{d}{dt}U_{t}\varphi\mathopen{}\mathclose{{\left(A}}\right)=\mathopen{}\mathclose{{\left\{\varphi,H}}\right\}=iL\varphi.(6)

By contrast, under the time evolutionSt(q,p)≡(q(t),p(t))S_{t}\mathopen{}\mathclose{{\left(q,p}}\right)\equiv\mathopen{}\mathclose{{\left(q\mathopen{}\mathclose{{\left(t}}\right),p\mathopen{}\mathclose{{\left(t}}\right)}}\right)expressed in (4), a time-dependent
probability densityρ(q,p,t)\rho\mathopen{}\mathclose{{\left(q,p,t}}\right)on the classical phase
space should evolve instead according to the classical Liouville equation:∂ρ∂t={H,ρ}=−iLρ.\frac{\partial\rho}{\partial t}=\mathopen{}\mathclose{{\left\{H,\rho}}\right\}=-iL\rho.(7)

Because the Liouvillian operator (5) involves
only first-order derivatives, the same should be true of any classical
wave functionψ\psiwhose modulus-square isρ\rho.

Finally, for the case of a probability densityρ\rhowithout any
explicit time-dependence, the classical Liouville equation reduces
to{H,ρ}=0,\mathopen{}\mathclose{{\left\{H,\rho}}\right\}=0,

which implies that∑k=1n∂ρ∂qk​dqk(t)d​t+∑k=1n∂ρ∂pk​dpk(t)d​t=0,\sum^{n}_{k=1}\frac{\partial\rho}{\partial q_{k}}\frac{dq_{k}\mathopen{}\mathclose{{\left(t}}\right)}{dt}+\sum^{n}_{k=1}\frac{\partial\rho}{\partial p_{k}}\frac{dp_{k}\mathopen{}\mathclose{{\left(t}}\right)}{dt}=0,

exactly in keeping with Koopman’s continuity equation (2).
These results confirm that Koopman’s functionρ\rhoreally does
correspond most closely with a classical system’s probability density,
and is conceptually distinct from Koopman’s phase-space functionsφ,ψ,…\varphi,\psi,\dots.

From Koopman’s notion of time evolution, (3),
one can see at an even deeper level why his phase-space functions
were not akin to wave functions. For any classical phase-space pointAA, letωA\omega_{A}be a positive linear functional acting on
Koopman’s functionsφ,ψ,…\varphi,\psi,\dotsaccording toωA(φ)≡φ(A),\omega_{A}\mathopen{}\mathclose{{\left(\varphi}}\right)\equiv\varphi\mathopen{}\mathclose{{\left(A}}\right),(8)

and satisfying the usual desiderata of a state map in the C*-algebraic
sense. For any timett, letgtg_{t}be the map acting onωA\omega_{A}by replacingAAwith its time-evolved counterpartSt​AS_{t}A, in
accordance with Koopman’s notion of time evolution:gt​ωA≡ωSt​A.g_{t}\omega_{A}\equiv\omega_{S_{t}A}.(9)

It follows immediately that(gtωA)(φ)=ωA(Utφ).\mathopen{}\mathclose{{\left(g_{t}\omega_{A}}}\right)\mathopen{}\mathclose{{\left(\varphi}}\right)=\omega_{A}\mathopen{}\mathclose{{\left(U_{t}\varphi}}\right).(10)

Evidently, the time evolution of state mapsωA\omega_{A}is opposite
to the time evolution of functionsφ\varphi, in an abstraction of
the usual distinction between Schrödinger-picture time evolution and
Heisenberg-picture time evolution. According to Koopman’s transformationUtU_{t}, his phase-space functions time-evolve as Heisenberg-picture
observables, not as Schrödinger-picture wave functions.

## 2.2John von Neumann

Koopman did not mention wave functions at all in his paper. By contrast,
von Neumann did mention wave functions, but only in the first of his
two 1932 papers (von Neumann 1932a),
and only to suggest an analogy between Koopman’s time-evolution operatorUtU_{t}and the time evolution appearing in quantum mechanics:

Finally, we would like to point out the interesting analogy between
Koopman’s operatorsUt=ei​t​AU_{t}=e^{itA}and the operators
of quantum mechanics. The Schrödinger wave functionφ\varphi(defined
in the state space of the mechanical system and not like ourffin phase space!) obeys, as is well known, in its dependence on the
time parameterttthe differential equationh2​π​i​∂φ∂t=H​φ\frac{h}{2\pi i}\frac{\partial\varphi}{\partial t}=H\varphi.
Herehhis Planck’s quantum of action andHHthe
energy operator. From this it follows at onceφ=ei​t⋅2​πh​H​φ(t=0)\varphi=e^{it\cdot\frac{2\pi}{h}H}\varphi_{\mathopen{}\mathclose{{\left(t=0}}\right)}[footnote in the original: This relationship is usually written
with−H-Hinstead ofHH.], so that here the unitary operatorsU^t=ei​t⋅2​πh​H\hat{U}_{t}=e^{it\cdot\frac{2\pi}{h}H}play a fundamental role.
The analogy, which arises from the juxtaposition ofAAand2​πh​H{\displaystyle\frac{2\pi}{h}H},
is striking [footnote in the original: A closer look shows that
it becomes more perfect if one replaces the differential equation
of the wave function with that of the so-called statistical operator
(cf., for example, J. v. Neumann,Mathematische Grundlagen der
Quantenmechanik, Berlin 1932, p. 186). However, it is constructed
in the same way, and what will be said below also applies to it.],
and it is even possible to exhibit the continuous passage of quantum
mechanics into the classical (ash→0h\to 0). Nevertheless, there seem
to be essential mathematical differences between these two families
of operators. For a mechanical system confined to a finite volume,
quantum mechanics always appears to exhibit a pure point spectrum,
whereas in the classical-mechanical problem a pure continuous spectrum
seems to be the generic case (cf. § VI). [Ibid., pp. 594–595]222In the original German:Zum Schluß sei noch auf die interessante Analogie zwischen Koopmans
OperatorenUt=ei​t​AU_{t}=e^{itA}und den Operatoren der Quantenmechanik
hingewiesen. Die Schrödingersche Wellenfunktionφ\varphi(definiert
im Zustandsraume des mechanischen Systems und nicht wie unsereffim Phasenraume!) gehorchtbekanntlich in ihrer Abhängigkeit vom Zeitparameter
t der Differentialgleichungh2​π​i​∂∂t​φ=H​φ\frac{h}{2\pi i}\frac{\partial}{\partial t}\varphi=H\varphi.
Hier isthhdas Plancksche Wirkungsquantum underHHder Energieoperator.
Hieraus folgt sofortφ=ei​t⋅2​πh​H​φ(t=0)\varphi=e^{it\cdot\frac{2\pi}{h}H}\varphi_{\mathopen{}\mathclose{{\left(t=0}}\right)}[Meistens wird diese Beziehung mit -H statt H geschrieben], so
daß hier die unitären OperatorenU^t=ei​t⋅2​πh​H\hat{U}_{t}=e^{it\cdot\frac{2\pi}{h}H}eine fundamentale Rolle spielen. Die Analogie, die durch das Nebeneinanderstellen
vonAAund2​πh​H\frac{2\pi}{h}Hentsteht, ist auffallend [Eine genauere
Überlegung zeigt, daß sie vollkommener wird, wenn man die Differentialgleichung
der Wellenfunktion durch diejenige des sog. statistischen Operators
ersetzt (vgl. z. B. J. v. Neumann, Mathematische Grundlagen der Quantenmechanik,
Berlin 1932, S. 186). Dieselbe ist aber ebenso gebaut und das weiter
unten zu Sagende gilt auch für sie.], und es ist möglich, sie zum
Nachweis des stetigen Übergehens der Quantenmechanik in die klassische
(fürh→0h\to 0) auszubauen. Trotzdem scheinen wesentliche mathematische
Unterschiede zwischen diesen Operatorenscharen zu bestehen. Denn für
ein mechanisches System, das in ein endliches Volumen eingesperrt
ist, scheint in der Quantenmechanik stets ein reines Punktspektrum
vorzuliegen, während im klassisch-mechanischen Problem das reine Streckenspektrum
der allgemeine Fall zu sein scheint (vgl.§\SVI).

Notice the footnote in which von Neumann pointed out that his phase-space
functionffshould evolve under−H-Hrather thanHH. Once again,
this reversed time evolution is due toffbeing akin to an observable,
and not a wave function.

## 2.3Mario Schönberg

In the early 1950s, Mario Schönberg published a pair of papers inIl Nuovo Cimento(Schönberg 1952, 1953)
in which he introduced the method of classical wave functions, an
idea that did not appear in the 1930s papers by Koopman or von Neumann.
Again, a classical wave function is a complex-valued function whose
modulus-square gives the probability density for a classical system.

Following Schönberg and his notation, he considered a system ofnnparticles with positions𝐱1,…,𝐱n\mathbf{x}_{1},\dots,\mathbf{x}_{n}and momenta𝐩1,…,𝐩n\mathbf{p}_{1},\dots,\mathbf{p}_{n}, as well as a probability densityfnf_{n}.
Schönberg called his new complex-valued functionΘn\Theta_{n}, and
then his equation (16) from his 1952 paper took the form:fn(𝐱1,…,𝐱n;𝐩1,…,𝐩n)=|Θn(𝐱1,…,𝐱n;𝐩1,…,𝐩n)|2[Schönberg’s eq.(16)].f_{n}\mathopen{}\mathclose{{\left(\mathbf{x}_{1},\dots,\mathbf{x}_{n};\mathbf{p}_{1},\dots,\mathbf{p}_{n}}}\right)=|\Theta_{n}\mathopen{}\mathclose{{\left(\mathbf{x}_{1},\dots,\mathbf{x}_{n};\mathbf{p}_{1},\dots,\mathbf{p}_{n}}}\right)|^{2}\qquad\mathopen{}\mathclose{{\left[\textrm{Sch\"{o}nberg's eq. }\mathopen{}\mathclose{{\left(16}}\right)}}\right].(11)

Earlier in his paper, in his equation (8), Schönberg had noted that
the probability densityfnf_{n}obeyed the classical Liouville equation,
in accord with (7),∂fn∂t=(Hn,fn)n=−iLnfn[Schönberg’s eq.(8)],\frac{\partial f_{n}}{\partial t}=\mathopen{}\mathclose{{\left(H_{n},f_{n}}}\right)_{n}=-iL_{n}f_{n}\qquad\mathopen{}\mathclose{{\left[\textrm{Sch\"{o}nberg's eq. }\mathopen{}\mathclose{{\left(8}}\right)}}\right],(12)

whereLnL_{n}is thenn-particle Liouville operator, and where
Schönberg used the following notation for Poisson brackets:(F,G)n=∑l=1n{∂F∂𝐱l∂G∂𝐩l−∂F∂𝐩l∂G∂𝐱l}[Schönberg’s eq.(9)].\mathopen{}\mathclose{{\left(F,G}}\right)_{n}=\sum^{n}_{l=1}\mathopen{}\mathclose{{\left\{\frac{\partial F}{\partial\mathbf{x}_{l}}\frac{\partial G}{\partial\mathbf{p}_{l}}-\frac{\partial F}{\partial\mathbf{p}_{l}}\frac{\partial G}{\partial\mathbf{x}_{l}}}}\right\}\qquad\mathopen{}\mathclose{{\left[\textrm{Sch\"{o}nberg's eq. }\mathopen{}\mathclose{{\left(9}}\right)}}\right].(13)

As Schönberg then explained, “since the square of the absolute
value of a solution of the Liouville equation is also a solution of
the same equation,” it followed that his new complex-valued functionΘn\Theta_{n}satisfied the same equation:∂Θn∂t=(Hn,Θn)n=−iLnΘn[Schönberg’s eq.(17)].\frac{\partial\Theta_{n}}{\partial t}=\mathopen{}\mathclose{{\left(H_{n},\Theta_{n}}}\right)_{n}=-iL_{n}\Theta_{n}\qquad\mathopen{}\mathclose{{\left[\textrm{Sch\"{o}nberg's eq. }\mathopen{}\mathclose{{\left(17}}\right)}}\right].(14)

In the paragraph that followed this equation, Schönberg wrote:

Thus we are led to a kind of wave function in classical statistical
mechanics. Equation (17) may be considered as the classical wave equation,
the [H]ermitian operatorLnL_{n}playing the part of [a]
classical [H]amiltonian operator. [Schönberg 1952, p. 1142]

In the opening of his 1953 paper, Schönberg wrote:

In the preceding part of [Schönberg 1952] we have shown that it
is possible to develop in the classical mechanics a wave formalism
in phase space which presents many of the features of the quantum
wave mechanics. […] [W]e may introduce a wave functionΘ(q,p)\Theta\mathopen{}\mathclose{{\left(q,p}}\right),
in general complex, such that the probability density be the square
of its absolute value:f(q,p)=|Θ(q,p)|2[Schönberg’s eq.(3)].f\mathopen{}\mathclose{{\left(q,p}}\right)=|\Theta\mathopen{}\mathclose{{\left(q,p}}\right)|^{2}\qquad\mathopen{}\mathclose{{\left[\textrm{Sch\"{o}nberg's eq. }\mathopen{}\mathclose{{\left(3}}\right)}}\right].(15)

The consideration of the wave function gives some essential new possibilities,
because it is not restricted to have only real and positive values,
as the probability density. [Schönberg 1953, p. 419]

In that 1953 paper, Schönberg made only a single reference to Koopman’s
1931 paper, pointing to the underlying mathematical equivalence between
Schönberg’s Hilbert spaces and Koopman’s Hilbert spaces that was described
in Section1of the present paper:

The introduction of the classical functions clarifies the meaning
of the unitary transformations in Hilbert space associated with the
motion of a classical system, which were introduced by Koopman. The
Koopman Hilbert-space can be taken as that of the classical wave functions.
[Schönberg 1953, p. 425]

It is unclear whether Schönberg meant something more by these remarks,
such as asserting not just a correspondence between underlying Hilbert
spaces, but a closer relationship between his classical wave functions
and Koopman’s phase-space functions. The answer may be lost to history.

## 2.4Angelo Loinger

In 1962, Angelo Loinger published a paper titled “Galilei Group
and Liouville Equation” inAnnals of Physics(Loinger 1962).
The paper explicitly distinguished between the original Koopman–von
Neumann construction and Schönberg’s work. In his introduction, Loinger
wrote:

In Section I the Hilbert space formulation of classical mechanics,
according to the viewpoints developed respectively by Koopman and
by Schönberg, is briefly reviewed in a convenient form and the intimate
relationship existing between the two conceptions is pointed out.
[Ibid., p. 132]

Loinger then went on to review the original Koopman–von
Neumann approach in Section I.A. of the paper (“Preliminaries and
Koopman’s Viewpoint”). In that section, Loinger slightly altered
the definition of the inner product (1),
writing:

We then consider the Hilbert space𝔎\mathfrak{K}of the complex
square integrable functionsf(ω)f\mathopen{}\mathclose{{\left(\omega}}\right)of the points
ofΩ2​n\Omega_{2n}[the classical system’s2​n2n-dimensional phase
space], in which an inner product is defined as follows:(f,g)=Def.∫Ωf∗(ω)g(ω)dω[Loinger’s eq.(9)].\mathopen{}\mathclose{{\left(f,g}}\right)\overset{\textrm{Def.}}{=}\int_{\Omega}f^{\ast}\mathopen{}\mathclose{{\left(\omega}}\right)g\mathopen{}\mathclose{{\left(\omega}}\right)\,d\omega\qquad\mathopen{}\mathclose{{\left[\textrm{Loinger's eq. }\mathopen{}\mathclose{{\left(9}}\right)}}\right].(16)

[Ibid., p. 134]

Note the absence of the phase-space probability densityρ\rhoin
this definition, as compared with Koopman’s original definition (1).
Loinger then wrote:

We put, with a bra and ket notation:(f,g)≡(f|g)[Loinger’s eq.(11)]\mathopen{}\mathclose{{\left(f,g}}\right)\equiv\mathopen{}\mathclose{{\left(f|g}}\right)\qquad\mathopen{}\mathclose{{\left[\textrm{Loinger's eq. }\mathopen{}\mathclose{{\left(11}}\right)}}\right](17)

and consider the extension𝔎D\mathfrak{K}_{D}of𝔎\mathfrak{K}in Dirac’s sense. [Ibid., p. 134]

Next, Loinger turned to a review of Schönberg’s framework in Section
II.A (“Schönberg’s Viewpoint”), writing:

The formulation of the classical mechanics given in Section I, A is
formally analogous to a formulation of quantum mechanics, which was
first studied by von Neumann. In this von Neumann quantal scheme the
operators of the conventional formulation are considered as vectors
of a new Hilbert space. One may ask whether even in the classical
case it is possible to introduce a Hilbert space, sayℌD\mathfrak{H}_{D},
analogous to the state-vector space of quantum mechanics. It can easily
be seen that such a space exists and stays in a very simple relationship
with𝔎D\mathfrak{K}_{D}. [Ibid., pp. 134–135]

Loinger added parenthetically that he would show later that the two
Hilbert spaces were mathematically equivalent, writing:

(Actually, as will be apparent presently,ℌD\mathfrak{H}_{D}and𝔎D\mathfrak{K}_{D}are the same space.) [Ibid., p. 135]

However, throughout the paper, Loinger emphasized that despite the
isomorphism betweenℌD\mathfrak{H}_{D}and𝔎D\mathfrak{K}_{D}, they
had conceptually different meanings. For example, he included the
following additional parenthetical note:

(We distinguish here the vectors of𝔎D\mathfrak{K}_{D}from those
ofℌD\mathfrak{H}_{D}, reserving for the first ones the bra and ket
notation with round parentheses.) [Ibid., p. 135]

## 2.5Giacomo Della Riccia and Norbert Wiener

In 1966,Journal of Mathematical Physicspublished a paper
by Giacomo Della Riccia and (posthumously)333The paper included the following note, at the end of its introductory
section: “Because of the sad demise of Norbert Wiener in March 1964,
the treatment given in this paper is due to the first-named author.
For the same reason it seemed desirable that the results should be
presented, however incomplete they may be.”Norbert Wiener (Della Riccia, Wiener 1966),
titled “Wave Mechanics in Classical Phase Space, Brownian Motion,
and Quantum Theory.” In their abstract, the authors wrote:

A wave dynamics of fieldsφ(p,q;t)∈L2(Γ)\varphi\mathopen{}\mathclose{{\left(p,q;t}}\right)\in L_{2}\mathopen{}\mathclose{{\left(\Gamma}}\right)over the phase spaceΓ(p,q)\Gamma\mathopen{}\mathclose{{\left(p,q}}\right)of a classical system𝒮\mathcal{S}is derived from the Liouville theorem. […] From
this it follows that we can regard normalized fieldsφ(p,q;t)\varphi\mathopen{}\mathclose{{\left(p,q;t}}\right)as “probability amplitudes” leading to a probability density functionρ(p,q;t)=φφ∗\rho\mathopen{}\mathclose{{\left(p,q;t}}\right)=\varphi\varphi^{\ast}in the sense of Gibbs’
statistical mechanics. [Ibid., p. 1372]

In their introductory material, Della Riccia and Wiener wrote:

In Gibbs statistical mechanics the basic quantity is a probability
density functionρ(p,q;t)\rho\mathopen{}\mathclose{{\left(p,q;t}}\right)defined over the phase
space of the mechanical system𝒮\mathcal{S}under observation. In
our work we introduce in phase space a new quantityφ(p,q;t)\varphi\mathopen{}\mathclose{{\left(p,q;t}}\right),
which by definition is a normalized square-integrable, real, or complex-valued
function. We call it a “probability amplitude” field.φ(p,q;t)\varphi\mathopen{}\mathclose{{\left(p,q;t}}\right)is required to satisfy the usual equation of continuity derived from
the Liouville theorem.

[…]

In the last part of our work we are concerned with the problem of
constructing probabilities out of “probability amplitudes.” We
use known results based on Wiener’s mathematical theory of Brownian
motion to derive probabilities which agree with those obtained from
Born’s statistical postulate. The desired result is that it is possible
to interpret the quantityρ(p,q;t)=φφ∗\rho\mathopen{}\mathclose{{\left(p,q;t}}\right)=\varphi\varphi^{\ast}as a probability density in the sense of Gibbs. [Ibid., pp. 1372–1373]

Della Riccia and Wiener made no mention of the 1930s papers by Koopman
or von Neumann, nor did they cite Schönberg or Loinger. It may be
that they did not see a connection between their classical probability
amplitudes and the Koopman–von Neumann formulation, and
might not have been aware of Schönberg and Loinger’s papers. Nevertheless,
Della Riccia and Wiener recapitulated Schönberg’s derivation of the
time-evolution equation (14),
which they wrote as−i(∂φ/∂t)=ℒφ,φ∈L2[Della Riccia and Wiener’s eq.(4)],-i\mathopen{}\mathclose{{\left(\partial\varphi/\partial t}}\right)=\mathcal{L}\varphi,\qquad\varphi\in L_{2}\qquad\mathopen{}\mathclose{{\left[\textrm{Della Riccia and Wiener's eq. }\mathopen{}\mathclose{{\left(4}}\right)}}\right],(18)

with their Liouville operator defined, as usual, according toℒ=i[H,⋅]\mathcal{L}=i\mathopen{}\mathclose{{\left[H,\cdot}}\right],
where the right-hand side is Della Riccia and Wiener’s notation for
the Poisson bracket with the HamiltonianHH.

## 2.6E. C. George Sudarshan

In 1976, E. C. George Sudarshan laid out a very similar method in
a paper published in the journalPramana, titled “Interaction
between Classical and Quantum Systems and the Measurement of Quantum
Observables” (Sudarshan 1976).
In the paper, Sudarshan described his motivation as trying to find
a better way to capture how classical systems and quantum systems
could interact with each other, especially during a measurement process.
In Sudarshan’s own words:

I introduce a direct method of dealing with the interaction of classical
and quantum systems. It is made possible by the discovery that a classical
system can be embedded in a quantum system with a continuum of superselection
sectors. [Ibid., p. 118]

In the second section of his paper, in defining a “quantum system”
with this continuum of superselection sectors, whose eventual purpose
was to represent a classical system with canonical coordinatesω=(x,p)\omega=\mathopen{}\mathclose{{\left(x,p}}\right),
Sudarshan wrote:

State vectors for the quantum system are given, in the Schrödinger
representation, by their wave functionsψ(ω)\psi\mathopen{}\mathclose{{\left(\omega}}\right).
But because of the superselection principle, the relative phase of
the distinct ideal eigenstates of coordinate operators is unmeasurable
and, therefore, irrelevant. Hence, we are led to the equivalenceψ(ω)∼ψ(ω)exp{iϕ(ω)}[Sudarshan’s eq.(2.8)].\psi\mathopen{}\mathclose{{\left(\omega}}\right)\sim\psi\mathopen{}\mathclose{{\left(\omega}}\right)\exp\mathopen{}\mathclose{{\left\{i\phi\mathopen{}\mathclose{{\left(\omega}}\right)}}\right\}\qquad\mathopen{}\mathclose{{\left[\textrm{Sudarshan's eq. }\mathopen{}\mathclose{{\left(2.8}}\right)}}\right].(19)

Therefore, only the absolute value ofψ(ω)\psi\mathopen{}\mathclose{{\left(\omega}}\right)is relevant and may be taken as the positive square root of the phase
space densityψ(ω)=ρ(ω)[Sudarshan’s eq.(2.9)].\psi\mathopen{}\mathclose{{\left(\omega}}\right)=\sqrt{\rho\mathopen{}\mathclose{{\left(\omega}}\right)}\qquad\mathopen{}\mathclose{{\left[\textrm{Sudarshan's eq. }\mathopen{}\mathclose{{\left(2.9}}\right)}}\right].(20)

The ideal eigenstates of the coordinate operators is [sic] identified
with the classical state corresponding to a point in phase space.
[Ibid., p. 120]

Crucially, Sudarshan included the following bracketed note:

[This construction of a quantum theory embedding the classical theory
is to be contrasted with the work of Coopman [sic] 1931; see also,
Jordan and Sudarshan 1961]. [Ibid., p. 120]

Sudarshan did not cite von Neumann, Schönberg, Loinger, Della Riccia,
or Wiener in his paper. In a later paper that further developed these
methods, published inPhysical Review Din 1978, Sudarshan
and his co-author, Tom Sherry, left out those names again, and did
not cite Koopman, either (Sherry, Sudarshan 1978).
Sudarshan was clearly familiar with von Neumann’s work, as the first
of von Neumann’s 1932 papers was cited in Sudarshan’s earlier 1961
paper with Jordan (Jordan, Sudarshan 1961),
as quoted in Section1of the present paper.
Perhaps the other papers were simply unknown to Sudarshan at the time.

## 2.7Ennio Gozzi

Danilo Mauro’s PhD supervisor at the University of Trieste was Ennio
Gozzi. Gozzi had been working on formal connections between classical
mechanics and quantum theory as far back as 1988, when he published
a paper inPhysical Letters B, titled “Hidden BRS Invariance
in Classical Mechanics,” in which he derived a path-integral representation
of classical mechanics (Gozzi 1988). In
that paper, Gozzi also introduced a classical probability distribution
on phase space, writing, in a footnote, “I owe this idea to a crucial
discussion with E. [Erhard] Seiler.” As Gozzi wrote:

This classical path-integral formalism has, as the quantum one, a
parallel operatorial version that is already well known. It is the
Liouville version of classical mechanics in which one introduces a
classical probability densityρ(p,q)\rho\mathopen{}\mathclose{{\left(p,q}}\right)which evolves
in time as any other classical observables∂ρ∂t={ρ,H}P​B,\frac{\partial\rho}{\partial t}=\mathopen{}\mathclose{{\left\{\rho,H}}\right\}_{PB},(21)

where{P,B}P​B\mathopen{}\mathclose{{\left\{P,B}}\right\}_{PB}are the usual Poisson brackets
andHHthe [H]amiltonian. This equation can be put in the form∂ρ∂t=L^ρ[Gozzi’s eq.(6)],\frac{\partial\rho}{\partial t}=\hat{L}\rho\qquad\mathopen{}\mathclose{{\left[\textrm{Gozzi's eq. }\mathopen{}\mathclose{{\left(6}}\right)}}\right],(22)

whereL^=∂H∂p​∂∂q−∂H∂q​∂∂p,\hat{L}=\frac{\partial H}{\partial p}\frac{\partial}{\partial q}-\frac{\partial H}{\partial q}\frac{\partial}{\partial p},(23)

which is known as the Liouville operator (Liouville). [Ibid., p.
526]

In this paper, Gozzi did not cite any of the authors discussed in
the present work—Koopman, von Neumann, Schönberg, Loinger,
Della Riccia, Wiener, or Sudarshan.

Gozzi first brought up links between these path-integral representations
of classical mechanics and the methods of Koopman and von Neumann
in a follow-up paper inPhysical Review Din 1989, titled “Hidden
BRS Invariance in Classical Mechanics. II” and co-authored with
Martin Reuter and William Thacker (Gozzi, Reuter, Thacker 1989).
Starting with this 1989 paper, Gozzi began citing Koopman’s papers
and von Neumann’s papers, but, again, without any mention of classical
wave functions. In the abstract, Gozzi and his co-authors wrote:

Associated with this path integral there is an operatorial formalism
that turns out to be an extension of the well-known operatorial approach
of Liouville, Koopman, and von Neumann. [Ibid., p. 3363]

In listing the virtues of Gozzi’s path-integral formulation of classical
mechanics, the authors included:

Second, long ago Koopman and von Neumann, influenced by the invention
of quantum mechanics, gave anoperatorialformulation of CM
[classical mechanics]. [Ibid., p. 3363, emphasis in the original]

Later on, the authors wrote:

The crucial elements of the operatorial formalism mentioned above
are the “classical commutation relations” which follow from the
classical path integral. This formalism naturally embeds the standard
operator approach to CM pioneered by Liouville, Koopman and von Neumann.
[Ibid., p. 3364]

In these papers in the late 1980s and well into the 1990s, Gozzi consistently
referred to Koopman and von Neumann’s method quite reasonably as “the
operatorial approach to classical mechanics.”

Gozzi began writing papers with Danilo Mauro in the late 1990s, starting
with a preprint extending Gozzi’s work on path-integral representations
of classical mechanics. This preprint appeared on the arXiv on July
9, 1999, and was eventually published inJournal of Mathematical
Physicsin 2000 (Gozzi, Mauro 2000).
The paper began with the following introductory statement, which remained
fully in keeping with Gozzi’s phrasing of Koopman and von Neumann’s
methods as providing an “operatorial” approach to classical mechanics:

Some time ago apath-integralformulation of classical mechanics
(CM) appeared in the literature. This formulation was nothing else
than the path-integral counterpart of theoperatorialversion
of CM provided long ago by Koopman and von Neumann. [Ibid., p. 1916,
emphasis in the original]

As with Gozzi’s previous papers, this paper did not mention classical
wave functions.

Shortly thereafter, Gozzi and Mauro co-authored their next manuscript,
this time with Enrico Deotto. The preprint was titled “Supersymmetry
in Classical Mechanics” and showed up on the arXiv on January 18,
2001. It was published as part of a book,A Concise Encyclopaedia
of Supersymmetry, in 2003 (Deotto, Gozzi, Mauro 2003).
The article began with the following statements:

In 1931 Koopman and von Neumann proposed anoperatorialformulation
of Classical Mechanics (CM) expanding earlier work of Liouville. Their
approach is basically the following: given a dynamical system with
a phase spaceℳ\mathcal{M}labelled by coordinatesφa=(qi,pi)\varphi^{a}=\mathopen{}\mathclose{{\left(q^{i},p^{i}}}\right);a=1,…,2​na=1,\dots,2n;i=1,…,ni=1,\dots,n, with HamiltonianHHand symplectic
matrixωa​b\omega^{ab}, the evolution of a probability densityρ(φ)\rho\mathopen{}\mathclose{{\left(\varphi}}\right)can be given either via the Poisson brackets{,}\mathopen{}\mathclose{{\left\{\ ,\ }}\right\}or via the Liouville operator:∂ρ∂t={H,ρ}=−L^ρ;L^=ωa​b∂bH∂a[Deotto, Gozzi, and Mauro’s eq.(1)].\frac{\partial\rho}{\partial t}=\mathopen{}\mathclose{{\left\{H,\rho}}\right\}=-\hat{L}\rho;\qquad\hat{L}=\omega^{ab}\partial_{b}H\partial_{a}\qquad\mathopen{}\mathclose{{\left[\textrm{Deotto, Gozzi, and Mauro's eq. }\mathopen{}\mathclose{{\left(1}}\right)}}\right].(24)

The evolution via the Liouville operator is basically what is called
the operatorial approach to CM. The natural question to ask is whether
we can associate to theoperatorialformalism of CM apath
integralone, like it is done in quantum mechanics. The answer is
yes. [Ibid., emphasis in the original]

The article cited the work of Koopman and von Neumann from the 1930s,
but, again, did not cite any of the other authors discussed in previous
sections of the present work.

## 2.8Danilo Mauro

On May 23, 2001, a preprint appeared on the arXiv, titled “On Koopman–von
Neumann Waves” and authored by Danilo Mauro. The paper was later
published inInternational Journal of Modern Physicsin 2002
(Mauro 2002). The paper’s opening statements
were consistent with the research literature:

In their standard formulation classical and quantum mechanics are
written in two completely different mathematical languages: for example
in classical mechanics observables arefunctionsof a 2n-dimensional
phase space, while in quantum mechanics they are self-adjointoperatorsacting on an [sic] Hilbert space. In the literature there are
a lot of attempts to reformulate classical and quantum mechanics in
similar forms. In this paper we shall concentrate on the work of Koopman
and von Neumann (KvN) who proposed, in 1931-32, an operatorial formulation
of classical mechanics. [Ibid., p. 1, emphasis in the original]

The statements that immediately followed, however, were historically
inaccurate, because they asserted that Koopman and von Neumann began
their approach by introducing classical wave functions:

The starting point of their work is the possibility of defining an
[sic] Hilbert space ofcomplexandsquare integrableclassical “wave” functionsψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right)such thatρ(φ)≡|ψ(φ)|2\rho\mathopen{}\mathclose{{\left(\varphi}}\right)\equiv|\psi\mathopen{}\mathclose{{\left(\varphi}}\right)|^{2}can be interpreted as a probability density of finding a particle
at the pointφ=(q,p)\varphi=\mathopen{}\mathclose{{\left(q,p}}\right)of the phase space. Thisρ\rhohas to evolve in time according to the well-known Liouville
equation:i∂∂tρ(q,p)=ℋ^ρ(q,p)[Mauro’s eq.(1.1)]i\frac{\partial}{\partial t}\rho\mathopen{}\mathclose{{\left(q,p}}\right)=\hat{\mathcal{H}}\rho\mathopen{}\mathclose{{\left(q,p}}\right)\qquad\mathopen{}\mathclose{{\left[\textrm{Mauro's eq. }\mathopen{}\mathclose{{\left(1.1}}\right)}}\right](25)

whereℋ^\hat{\mathcal{H}}is the Liouville operatorℋ^=−i​∂pH​∂q+i​∂qH​∂p\hat{\mathcal{H}}=-i\partial_{p}H\partial_{q}+i\partial_{q}H\partial_{p}andHHis the Hamiltonian of the standard phase space. In order
to obtain (1.1) Koopman and von Neumann postulated the same evolution
forψ\psi:i∂∂tψ(q,p)=ℋ^ψ(q,p)[Mauro’s eq.(1.2)]i\frac{\partial}{\partial t}\psi\mathopen{}\mathclose{{\left(q,p}}\right)=\hat{\mathcal{H}}\psi\mathopen{}\mathclose{{\left(q,p}}\right)\qquad\mathopen{}\mathclose{{\left[\textrm{Mauro's eq. }\mathopen{}\mathclose{{\left(1.2}}\right)}}\right](26)

[Ibid., p. 1, emphasis in the original]

Notice, furthermore, that although the formula for the Liouville operatorℋ^\hat{\mathcal{H}}appearing in (25) was
in agreement with the usual definition (5),
the evolution equation (26) forψ\psiwas off by a crucial minus sign as compared with the equation
(6) satisfied by
Koopman’s phase-space functions.

Later, after reviewing the equations for time evolution in textbook
quantum mechanics, the paper continued as follows:

The situation is completely different in the Hilbert space of classical
mechanics. In fact, following Koopman and von Neumann, we postulate
that the wave functionsψ(φ,t)=ψ(q,p,t)\psi\mathopen{}\mathclose{{\left(\varphi,t}}\right)=\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)evolve in time with the Liouvillian operator:ℋ^=−i∂piH∂qi+i∂qiH∂pi[Mauro’s eq.(2.5)]\hat{\mathcal{H}}=-i\partial_{p_{i}}H\partial_{q_{i}}+i\partial_{q_{i}}H\partial_{p_{i}}\qquad\mathopen{}\mathclose{{\left[\textrm{Mauro's eq. }\mathopen{}\mathclose{{\left(2.5}}\right)}}\right](27)

according to the following equation:i∂∂tψ=ℋ^ψ⇒∂∂tψ=(−∂piH∂qi+∂qiH∂pi)ψ[Mauro’s eq.(2.6)]i\frac{\partial}{\partial t}\psi=\hat{\mathcal{H}}\psi\quad\Rightarrow\quad\frac{\partial}{\partial t}\psi=\mathopen{}\mathclose{{\left(-\partial_{p_{i}}H\partial_{q_{i}}+\partial_{q_{i}}H\partial_{p_{i}}}}\right)\psi\qquad\mathopen{}\mathclose{{\left[\textrm{Mauro's eq. }\mathopen{}\mathclose{{\left(2.6}}\right)}}\right](28)

We can think of (2.6) as the analogue of the quantum Schrödinger
equation, i.e. as the fundamental equation governing the evolution
of the vectors in the Hilbert space of classical mechanics. These
vectors are the complex wave functions on the phase space obeying
the normalizability condition∫dqdpψ∗(q,p)ψ(q,p)=1\int dqdp\,\psi^{\ast}\mathopen{}\mathclose{{\left(q,p}}\right)\psi\mathopen{}\mathclose{{\left(q,p}}\right)=1.
[Ibid., p. 3]

As the present work has established, Koopman and von Neumann did not
introduce classical wave functions, nor did they postulate that any
such classical wave functions evolved according to the Liouville equation.
These ideas were, in fact, originally due to Schönberg, and then developed,
in some cases independently, by other researchers, including Loinger,
Della Riccia, Wiener, and Sudarshan. As such, this method of classical
wave functions should not properly be called “Koopman–von
Neumann classical mechanics.”

This incorrect history showed up again in a preprint authored by Mauro
and Gozzi that appeared on the arXiv on the same day—May
23, 2001. The preprint was titled “Minimal Coupling in Koopman–von
Neumann Theory,” and was published inAnnals of Physicsin
2002 (Gozzi, Mauro 2002). The opening
remarks began with:

In 1931, Koopman and von Neumann (KvN)postulatedthe same
evolution equation for complex distributionsψ(q,p)\psi\mathopen{}\mathclose{{\left(q,p}}\right)making up anL2L^{2}Hilbert space:∂tψ(q,p)=−L^ψ(q,p)[Gozzi and Mauro’s eq.(1.2)].\partial_{t}\psi\mathopen{}\mathclose{{\left(q,p}}\right)=-\hat{L}\psi\mathopen{}\mathclose{{\left(q,p}}\right)\qquad\mathopen{}\mathclose{{\left[\textrm{Gozzi and Mauro's eq. }\mathopen{}\mathclose{{\left(1.2}}\right)}}\right].(29)

If we postulate [this equation] forψ(q,p)\psi\mathopen{}\mathclose{{\left(q,p}}\right),
then it is easy to prove that functionsρ\rhoof the formρ=|ψ|2[Gozzi and Mauro’s eq.(1.3)]\rho=|\psi|^{2}\qquad\mathopen{}\mathclose{{\left[\textrm{Gozzi and Mauro's eq. }\mathopen{}\mathclose{{\left(1.3}}\right)}}\right](30)

evolve with the same equation asψ\psi. This is so because the
operatorL^\hat{L}contains only firs [sic] order derivatives.
This is not what happens in quantum mechanics (QM) where the evolution
of theψ(q)\psi\mathopen{}\mathclose{{\left(q}}\right)is via the Schrödinger operatorH^\hat{H}while that of the associatedρ=|ψ|2\rho=|\psi|^{2}is via a totally
different operator. The reason is that the Schrödinger operatorH^\hat{H},
differently than [sic] the Liouville operatorL^\hat{L}, contains
second order derivatives. [Ibid., pp. 152–153, emphasis
in the original]

An equation resembling (29)
does appear in Koopman’s 1931 paper, though it is intended for describing
the time evolution of observables in a classical phase space. The
next statement in the 2002 paper is also historically incorrect:

By postulating the relations (1.3) and (1.2) for theψ\psi, KvN
managed to build an operatorial formulation for classical mechanics
(CM) equipped with a Hilbert space structure and producing the same
results as the Liouville formulation. [Ibid.]

Koopman and von Neumann did not postulate either of Gozzi and Mauro’s
equations (1.2) or (1.3). As with Mauro’s previous paper, the 2002
paper cites Koopman and von Neumann, but does not cite Schönberg or
any of the other developers of the method of classical wave functions.

Soon after, Deotto, Gozzi, and Mauro collaborated on another paper,
which appeared on the arXiv on August 7, 2002. The paper, titled “Hilbert
Space Structures in Classical Mechanics. I,” was published inJournal
of Mathematical Physicsin 2003 (Deotto, Gozzi, Mauro 2003).
The paper began with the following statements:

In the 1930s Koopman and von Neumann (KvN) gave an operatorial formulation
ofclassical mechanics(CM). They first introduced square-integrable
functionsψ(φa)\psi\mathopen{}\mathclose{{\left(\varphi^{a}}}\right)on the phase spaceℳ\mathcal{M}of a classical system with HamiltonianH(φ)H\mathopen{}\mathclose{{\left(\varphi}}\right)(withφa\varphi^{a}we indicate the 2nnphase-space coordinates of the
systemφa=q1​⋯​qn,p1​⋯​pn\varphi^{a}=q^{1}\cdots q^{n},p^{1}\cdots p^{n}). According
to KvN the Liouville phase-space distributions are obtained fromψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right)asρ(φ)=|ψ(φ)|2[Deotto, Gozzi, and Mauro’s eq.(1.1)].\rho\mathopen{}\mathclose{{\left(\varphi}}\right)=|\psi\mathopen{}\mathclose{{\left(\varphi}}\right)|^{2}\qquad\mathopen{}\mathclose{{\left[\textrm{Deotto, Gozzi, and Mauro's eq. }\mathopen{}\mathclose{{\left(1.1}}\right)}}\right].(31)

The introduction of theψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right)is an acceptable
assumption considering thatρ(φ)\rho\mathopen{}\mathclose{{\left(\varphi}}\right), having the
meaning of a probability density, is always positive semidefiniteρ(φ)⩾0\rho\mathopen{}\mathclose{{\left(\varphi}}\right)\geqslant 0, and so one can always take
its “square root” and obtainψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right). Moreover,
asψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right)is square integrable, i.e.,ψ(φ)∈L2\psi\mathopen{}\mathclose{{\left(\varphi}}\right)\in L^{2},
it turns out thatρ(φ)\rho\mathopen{}\mathclose{{\left(\varphi}}\right)is integrable as it
should be∫d2​nφψ∗(φ)ψ(φ)=∫d2​nφρ(φ)<∞[Deotto, Gozzi, and Mauro’s eq.(1.2)].\int\mathrm{d}^{2n}\varphi\,\psi^{\ast}\mathopen{}\mathclose{{\left(\varphi}}\right)\psi\mathopen{}\mathclose{{\left(\varphi}}\right)=\int\mathrm{d}^{2n}\varphi\,\rho\mathopen{}\mathclose{{\left(\varphi}}\right)<\infty\qquad\mathopen{}\mathclose{{\left[\textrm{Deotto, Gozzi, and Mauro's eq. }\mathopen{}\mathclose{{\left(1.2}}\right)}}\right].(32)

KvNpostulatedthe following evolution forψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right):i∂ψ(φ,t)∂t=L^ψ(φ,t)[Deotto, Gozzi, and Mauro’s eq.(1.3)]i\frac{\partial\psi\mathopen{}\mathclose{{\left(\varphi,t}}\right)}{\partial t}=\hat{L}\psi\mathopen{}\mathclose{{\left(\varphi,t}}\right)\qquad\mathopen{}\mathclose{{\left[\textrm{Deotto, Gozzi, and Mauro's eq. }\mathopen{}\mathclose{{\left(1.3}}\right)}}\right](33)

whereL^\hat{L}, defined asL^=i∂H∂qi∂∂pi−i∂H∂pi∂∂qi[Deotto, Gozzi, and Mauro’s eq.(1.4)]\hat{L}=i\frac{\partial H}{\partial q^{i}}\frac{\partial}{\partial p^{i}}-i\frac{\partial H}{\partial p^{i}}\frac{\partial}{\partial q^{i}}\qquad\mathopen{}\mathclose{{\left[\textrm{Deotto, Gozzi, and Mauro's eq. }\mathopen{}\mathclose{{\left(1.4}}\right)}}\right](34)

is the Liouville operator. This equation of motion forψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right)and (1.1) lead to the same evolution forρ(φ)\rho\mathopen{}\mathclose{{\left(\varphi}}\right),i∂ρ(φ,t)∂t=L^ρ(φ,t)[Deotto, Gozzi, and Mauro’s eq.(1.5)].i\frac{\partial\rho\mathopen{}\mathclose{{\left(\varphi,t}}\right)}{\partial t}=\hat{L}\rho\mathopen{}\mathclose{{\left(\varphi,t}}\right)\qquad\mathopen{}\mathclose{{\left[\textrm{Deotto, Gozzi, and Mauro's eq. }\mathopen{}\mathclose{{\left(1.5}}\right)}}\right].(35)

This is the well-known Liouville equation satisfied by the classical
probability densities. Note thatρ(φ)\rho\mathopen{}\mathclose{{\left(\varphi}}\right)obeys
the same equation asψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right)becauseL^\hat{L}is first order in the derivatives. The same does not happen in quantum
mechanics where the analog of (1.3) is the Schrödinger equation whose
evolution operator is second order in the derivatives. We will not
spend more time here in explaining the interplay between the quantum
mechanical wave functionsψ(q)\psi\mathopen{}\mathclose{{\left(q}}\right)and these “KvN
waves”ψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right).
The interested reader can consult Ref. 2 [which refers to the two
2002 papers cited above] where many details have been worked out.
[Ibid., pp. 5902–5903, emphasis in the original]

Again, the paper attributed the introduction of classical wave functions,
related to classical probability distributions by the modulus-squaring
operation, and the introduction of a time-evolution equation for classical
wave functions, to Koopman and von Neumann.

Mauro’s PhD thesis appeared on the arXiv on January 30, 2003, and
was titled “Topics in Koopman–von Neumann Theory” (Mauro
2003). The introduction, in describing attempts
to connect the formalism of classical mechanics with the formalism
of quantum mechanics, contained this text:

Another, even older, direction is to reformulate CM in an operatorial
language by using a Hilbert space of square integrable functions on
the phase space and by replacing the Poisson brackets with some suitable
classical commutators. This is what has been done in the 30’s
by Koopman and von Neumann (KvN). [Ibid., p. 1]

These statements were consistent with the historical record. However,
a few sentences later, one finds:

The starting point of KvN is the introduction of a Hilbert space of
square integrable and complex functionsψ(q,p)\psi\mathopen{}\mathclose{{\left(q,p}}\right)whose
modulus square are just the usual probability densities in phase spaceρ(q,p)=|ψ(q,p)|2\rho\mathopen{}\mathclose{{\left(q,p}}\right)=|\psi\mathopen{}\mathclose{{\left(q,p}}\right)|^{2}. [Ibid.,
p. 1]

Shortly thereafter, the paper stated:

In fact KvN postulated that the evolution of theψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right)must be given by the Liouvillian which, containing only first order
derivatives, evolves also the probability densitiesρ(φ)\rho\mathopen{}\mathclose{{\left(\varphi}}\right),
differently than [sic] what happens in QM. [Ibid., pp. 1–2]

As the present work has shown, these last two statements were not
in keeping with the historical record. Similar statements showed up
elsewhere in the thesis, in whichψ(φ)\psi\mathopen{}\mathclose{{\left(\varphi}}\right)was
called the “KvN wave” and its Liouville equation was called the
“KvN equation.” Although the thesis did not cite most of the researchers
discussed in the present work, the thesis did cite Sherry and Sudarshan’s
1978 paper (Sherry, Sudarshan 1978),
albeit without crediting the use of classical wave functions to Sudarshan.

The introduction to Mauro’s 2003 paper “A New Quantization Map”
(Mauro 2003) contained this text:

KvN formulated classical mechanics in a Hilbert space made up of complex
square integrable functions over the phase space variablesψ(q,p,t)\psi\mathopen{}\mathclose{{\left(q,p,t}}\right).
In particular they postulated, as equation of evolution forψ(q,p,t)\psi\mathopen{}\mathclose{{\left(q,p,t}}\right),
the Liouville equation itselfi∂∂tψ(q,p,t)=L^ψ(q,p,t)[Mauro’s eq.(3)].i\frac{\partial}{\partial t}\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)=\hat{L}\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)\qquad\mathopen{}\mathclose{{\left[\textrm{Mauro's eq. }(3)}}\right].(36)

Starting from (3) it is easy to prove that, since the LiouvillianL^\hat{L}contains only first order derivatives, the Liouville equation
(1) for the probability densitiesρ(q,p,t)\rho\mathopen{}\mathclose{{\left(q,p,t}}\right)can be
derived via the postulateρ(q,p,t)=|ψ(q,p,t)|2\rho\mathopen{}\mathclose{{\left(q,p,t}}\right)=|\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)|^{2}.
Finally KvN imposed on the states of their Hilbert space the following
scalar product:⟨ψ|τ⟩=∫dqdpψ∗(q,p)τ(q,p)[Mauro’s eq.(4)].\langle\psi|\tau\rangle=\int dq\,dp\,\psi^{\ast}\mathopen{}\mathclose{{\left(q,p}}\right)\tau\mathopen{}\mathclose{{\left(q,p}}\right)\qquad\mathopen{}\mathclose{{\left[\textrm{Mauro's eq. }(4)}}\right].(37)

With this choice the LiouvillianL^\hat{L}is a Hermitian operator.
Therefore⟨ψ|ψ⟩=∫dqdp|ψ(q,p)|2\langle\psi|\psi\rangle=\int dq\,dp\,|\psi\mathopen{}\mathclose{{\left(q,p}}\right)|^{2}is a conserved quantity and|ψ(q,p)|2|\psi\mathopen{}\mathclose{{\left(q,p}}\right)|^{2}can
be consistently interpreted as the probability density of finding
a particle in a point of the phase space. [Ibid., p. 28]

Despite the incorrect claim that Koopman and von Neumann postulated
the specific equation (36),
notice the careful language in these introductory statements, which
otherwise said only that Koopman and von Neumann identifiedψ(q,p,t)\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)as “complex square integral functions over the phase space variables”
with a specific scalar product, and did not claim that Koopman or
von Neumann themselves interpretedψ(q,p,t)\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)as a
classical wave function. In the quoted text above, the paper switched
to the passive voice in assigning this interpretation toψ(q,p,t)\psi\mathopen{}\mathclose{{\left(q,p,t}}\right),
both in the sentence immediately following (36),
and in the last sentence of the quoted text. The scalar product appearing
in (37), however, was missing the phase-space
probability densityρ(q,p)\rho\mathopen{}\mathclose{{\left(q,p}}\right)that appeared in the inner
product (1) as defined in Koopman’s
1931 paper, and that also appeared in the integral measures used both
in Koopman’s 1931 paper and in von Neumann’s two 1932 papers.

Similar statements showed up in a 2004 paper co-authored by Gozzi
and Mauro, titled “On Koopman–von Neumann Waves II”
(Gozzi, Mauro 2004). In the abstract, the authors wrote:

In particular we show that the introduction of the KvN Hilbert space
of complex and square integrable “wave functions”
requires an enlargement of the set of the observables of ordinary
classical mechanics. [Ibid.]

The introduction included:

In a previous paper we stressed that KvN did not use the space of
theρ\rhobut introduced instead a Hilbert space made up of complexsquare integrablefunctionsψ(q,p)∈L2\psi\mathopen{}\mathclose{{\left(q,p}}\right)\in L^{2}over phase space. Theseψ\psiare “the KvN waves”
we indicated in the title. Next theypostulatedfor everyψ(q,p,t)\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)an equation of evolution which is the Liouville equation itself:i∂∂tψ(q,p,t)=ℋ^ψ(q,p,t)[Gozzi and Mauro’s eq.(1.3)].i\frac{\partial}{\partial t}\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)=\hat{\mathcal{H}}\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)\qquad\mathopen{}\mathclose{{\left[\textrm{Gozzi and Mauro's eq. }\mathopen{}\mathclose{{\left(1.3}}\right)}}\right].(38)

Because the Liouvillianℋ^\hat{\mathcal{H}}contains only first
order derivatives, it is easy to prove that the Liouville equation
(1.1) for the probability densitiesρ(q,p,t)\rho\mathopen{}\mathclose{{\left(q,p,t}}\right)can
be derived from (1.3) by postulating thatρ(q,p,t)=|ψ(q,p,t)|2\rho\mathopen{}\mathclose{{\left(q,p,t}}\right)=|\psi\mathopen{}\mathclose{{\left(q,p,t}}\right)|^{2}.
[Ibid., emphasis in the original]

Although the paper did not attribute the modulus-squaring relationship
to Koopman and von Neumann, it did refer toψ\psias a “KvN wave”
and said that Koopman and von Neumann postulated its time-evolution
equation.

## 3Conclusion

The present paper was intended to clarify the history behind the formulation
of classical mechanics developed by Bernard Koopman and John von Neumann,
and to show that the method of “classical” wave functions was
due not to Koopman and von Neumann, but perhaps first due to Mario
Schönberg, with later contributions from Alfred Loinger, Giacomo Della
Riccia, Norbert Wiener, and E.C. George Sudarshan. Of course, even
this historical assessment may be incorrect, and other researchers
may have come up with the idea before Schönberg.

The method of classical wave functions has proved to be important
and highly useful, and this historical misattribution should not be
taken to suggest otherwise. However, getting the history right matters,
especially when those responsible for an influential idea would otherwise
not be given the credit that they deserve.

## Acknowledgments

The author would especially like to thank Ennio Gozzi, John Norton,
and Miklos Redei for helpful and informative communications.

## References
- [1]“Koopman Methods in Classical and Classical-Quantum Mechanics”.In D. I. Bondar, I. Burghardt, F. Gay-Balmaz, I. Mezic, and C. Tronci, editors,Proceedings of the 746th WE-Heraeus Seminar. Wilhelm und Else Heraeus Stiftung, April 2021.19–23 April 2021.URL:https://www.we-heraeus-stiftung.de/veranstaltungen/seminare/2021/koopman-methods-in-classical-and-classical-quantum-mechanics.
- [2]Koopman Methods in Classical and Quantum-Classical Mechanics, Volume 55, Bristol, UK, July 2022. IOP Publishing.Special Collection on Koopman Methods.doi:10.1088/1751.
- [3]E. Deotto, E. Gozzi, and D. Mauro.“Hilbert Space Structure in Classical Mechanics. I”.Journal of Mathematical Physics, 44:5902–5936, August 2003.arXiv:quant-ph/0208046v3,doi:10.1063/1.1623333.
- [4]E. Deotto, E. Gozzi, and D. Mauro.“Supersymmetry in Classical Mechanics”.In J. Bagger, S. Duplij, and W. Siegel, editors,A Concise Encyclopaedia of Supersymmetry, pages 462–464. Kluwer Academic Publishers, Dordrecht, Boston, London, 2003.URL:https://hdl.handle.net/11368/1713693,arXiv:hep-th/0101124.
- [5]G. Della Riccia and N. Wiener.“Wave Mechanics in Classical Phase Space, Brownian Motion, and Quantum Theory”.Journal of Mathematical Physics, 7(8):1372–1383, August 1966.doi:10.1063/1.1705047.
- [6]E. Gozzi and D. Mauro.“A New Look at the Schouten-Nijenhuis, Fr\\backslash" olicher-Nijenhuis and Nijenhuis-Richardson Brackets for Symplectic Spaces”.Journal of Mathematical Physics, 41(4):1916–1933, April 2000.arXiv:hep-th/9907065,doi:10.1063/1.533218.
- [7]E. Gozzi and D. Mauro.“Minimal Coupling in Koopman–von Neumann Theory”.Annals of Physics, 296(2):152–186, March 2002.arXiv:quant-ph/0105113,doi:10.1006/aphy.2001.6206.
- [8]I. M. Gelfand and M. A. Naimark.“On the Imbedding of Normed Rings into the Ring of Operators on a Hilbert Space”.Matematicheskii Sbornik, 12(54)(2):197–217, 1943.URL:https://mi.mathnet.ru/msb6155.
- [9]E. Gozzi.“Hidden BRS Invariance in Classical Mechanics”.Physics Letters B, 201(4):525–528, February 1988.doi:10.1016/0370-2693(88)90611-9.
- [10]E. Gozzi, M. Reuter, and W. D. Thacker.“Hidden BRS Invariance in Classical Mechanics. II”.Physical Review D, 40(10):3363, November 1989.doi:10.1103/PhysRevD.40.3363.
- [11]W. Heisenberg.“Über quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen”.Zeitschrift für Physik, 33:879–893, December 1925.doi:10.1007/BF01328377.
- [12]T. F. Jordan and E. C. G. Sudarshan.“Lie Group Dynamical Formalism and the Relation between Quantum Mechanics and Classical Mechanics”.Reviews of Modern Physics, 33(4):515–524, October 1961.URL:https://cds.cern.ch/record/436528;https://doi.org/10.1103/RevModPhys.33.515,doi:10.1103/RevModPhys.33.515.
- [13]B. O. Koopman.“Hamiltonian Systems and Transformations in Hilbert Space”.Proceedings of the National Academy of Sciences, 17(5):315–318, 1931.doi:10.1073/pnas.17.5.315.
- [14]A. Loinger.“Galilei Group and Liouville Equation”.Annals of Physics, 20(1):132–144, 1962.doi:10.1016/0003-4916(62)90119-7.
- [15]D. Mauro.“On Koopman–von Neumann Waves”.International Journal of Modern Physics A, 17(09):1301–1325, 2002.arXiv:quant-ph/0105112,doi:10.1142/S0217751X02009680.
- [16]D. Mauro.“A New Quantization Map”.Physics Letters A, 315(1):28–35, August 2003.arXiv:quant-ph/0305063,doi:10.1016/S0375-9601(03)00996-4.
- [17]D. Mauro.Topics in Koopman-von Neumann Theory.PhD thesis, 2003.arXiv:quant-ph/0301172.
- [18]E. Schrödinger.“An Undulatory Theory of the Mechanics of Atoms and Molecules”.Physical Review, 28(6):1049–1070, December 1926.doi:10.1103/PhysRev.28.1049.
- [19]M. Schönberg.“Application of Second Quantization Methods to the Classical Statistical Mechanics”.Il Nuovo Cimento, 9(12):1139–1182, Dec. 1952.doi:10.1007/BF02782925.
- [20]M. Schönberg.“Application of Second Quantization Methods to the Classical Statistical Mechanics (II)”.Il Nuovo Cimento, 10(4):419–472, Apr. 1953.doi:10.1007/BF02781980.
- [21]I. E. Segal.“Irreducible Representations of Operator Algebras”.Bulletin of the American Mathematical Society, 53:73–88, 1947.doi:10.1090/S0002-9904-1947-08742-5.
- [22]T. N. Sherry and E. C. G. Sudarshan.“Interaction Between Classical and Quantum Systems: A New Approach to Quantum Measurement. I”.Physical Review D, 18(12):4580, December 1978.doi:10.1103/PhysRevD.18.4580.
- [23]E. C. G. Sudarshan.“Interaction between Classical and Quantum Systems and the Measurement of Quantum Observables”.Pramana, 6(3):117–126, March 1976.doi:10.1007/BF02847120.
- [24]J. von Neumann.“Zur Operatorenmethode In Der Klassischen Mechanik”.Annals of Mathematics, 33(3):587–642, 1932.doi:10.2307/1968537.
- [25]J. von Neumann.“Zusatze Zur Arbeit ‘Zur Operatorenmethode…’ ”.Annals of Mathematics, 33(4):789–791, 1932.doi:10.2307/1968225.
- [26]Wikipedia contributors.“Koopman–von Neumann Classical Mechanics”, June 2025.URL:https://en.wikipedia.org/wiki/Koopman%E2%80%93von_Neumann_classical_mechanics.


## 


- 


Major funding support from
