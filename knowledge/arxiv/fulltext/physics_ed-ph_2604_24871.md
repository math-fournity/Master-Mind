# Six textbook mistakes in quantum field theory

**arXiv ID**: 2604.24871v1
**Authors**: Alexandros Gezerlis
**Published**: 2026-04-27
**Categories**: physics.ed-ph, hep-th, nucl-th, quant-ph
**Comments**: 13 pages, 2 figures
**HTML URL**: https://arxiv.org/html/2604.24871v1

## Abstract

This article discusses incorrect statements appearing in textbooks on quantum field theory (QFT); some of these mistakes also appear in the research literature. The focus is not on errors made by an individual author, but on conceptual muddledness that is widespread in introductory textbooks. We start from a bare-bones summary of QFT, meant to establish the notation. We then turn to our six paradigmatic themes, in each case quoting a specific example of the textbook mistake, a summary of material that is known to experts but is frequently mishandled in introductory works, pointers to authoritative references where the relevant concept is handled properly, as well as a concise correction that rectifies any issues. The goal of this work is to warn readers of the existence of several pitfalls and thereby stop these errors from further propagating in the literature on QFT.

## Full Text

Six textbook mistakes in quantum field theory

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2604.24871v1 [physics.ed-ph] 27 Apr 2026

## Six textbook mistakes in quantum field theoryAlexandros GezerlisDepartment of Physics, University of Guelph, Guelph, Ontario N1G 2W1, Canada

## Abstract

This article discusses incorrect statements appearing in textbooks on quantum field theory (QFT); some of these mistakes also appear in the research literature.
The focus is not on errors made by an individual author, but on conceptual muddledness that is widespread in introductory textbooks.
We start from a bare-bones summary of QFT, meant to establish the notation.
We then turn to our six paradigmatic themes, in each case quoting a specific example
of the textbook mistake, a summary
of material that is known to experts but is frequently mishandled in
introductory works, pointers to authoritative references where the relevant concept is handled properly, as well as a concise correction that rectifies any issues.
The goal of this work
is to warn readers of the existence of several pitfalls and thereby
stop these errors from further propagating in the literature on QFT.

## IIntroduction

This is the third installment in a series of worksGezerlisWilliams1;GezerlisWilliams2tackling mistaken claims appearing in physics textbooks. The premise of these articles is that errors in the research literature are both inevitable and
understandable, but textbooks should be held to a higher standard. Not only because their writing has the benefit of hindsight (unlike journal publications, which typically deal with questions that are rapidly evolving) but also,
and even more importantly, because textbooks reach a much broader (and much more impressionable) audience.
The present article studies widespread misconceptions on themes related to quantum field theory, which we also take to include the usual preliminaries (relativistic quantum mechanics and classical field theory). Relativistic quantum field theory is typically taught in a dedicated graduate course, often over two semesters;
the misconceptions we discuss revolve around “core” aspects of QFT, so they
are mainly of relevance to the first semester (or even an undergraduate version)
of such a course.

In order to structure this work, we have employed a selection criterion:
each mistake addressed appears in at least two standard textbooks.
Another criterion is that the questions touched upon here are of wide conceptual
import, not one-off miscalculations.
Sometimes individual textbook authors make mistakes (even glaring ones), but that is not our focus here: we care about incorrect claims that are widespread, i.e.,
ones which have been propagating through the introductory literature (despite the fact
that experts would ordinarily not make such claims).
Typos or other minor issues can typically be addressed by a student on the fly,
while working through a textbook. On the other hand, conceptual misunderstanding, especially when it is not limited to a single textbook, is much more pernicious, often leading students to blame their own thought process for their inability to understand what is going on. This is even more true for a forbidding subject like quantum field theory, which already has a reputation of being expert-friendly.

The previous two installments in this series grew out of the author’s work on
writingGezerlisNumerical1(or updating)GezerlisNumerical2a physics textbook, a process which was preceded by an in-depth exploration of the introductory textbook literature. The provenance of the present article is similar,
in that the author has recently finished writing a textbook on quantum field
theory.GezerlisQFTThe six topics addressed in this work are tackled correctly in
Ref.GezerlisQFT,(in more detail than here),
but readers can always benefit from having
multiple reliable sources on a given subject, so in what follows
we will also cite authoritative works by other authors on each theme.
The motivation behind the present article is that focusing on these widespread
incorrect claims will, it is to be hoped, make it possible for future generations of students
to learn the subject right the first time.
Our intended audience is mostly composed of QFT instructors, who
may have unintentionally contributed toward the propagation of
these textbook mistakes in the past.

## IIEstablishing the notation

Many of the textbook mistakes to be discussed below
arise because the notation used in quantum field theory is often too sloppy (albeit sometimes for good reason).
For example, it is very common to denote a real classical field byϕ\phi,
but then also use the same symbol for a complex classical field,
or a quantum field in the Heisenberg picture (or in another picture).
In order to preempt any misunderstanding about such matters,
here we first go over the notation that we will be employing in the
rest of the article. We emphasize that this section is meant as reference (not pedagogical) material; trying to teach quantum field theory from scratch
in a few pages would be a doomed exercise.

As is standard in QFT, we will be working with natural units, settingℏ=c=1\hbar=c=1.
We will be using the particle physics/mostly minus metricημ​ν\eta_{\mu\nu},
with signature(+,−,−,−)(+,-,-,-),
according to whichaμ​bμ=a0​b0−𝐚⋅𝐛a^{\mu}b_{\mu}=a^{0}b^{0}-\mathbf{a}\cdot\mathbf{b}.
The LagrangianLLis related to the Lagrangian densityℒ\cal{L}viaL=∫d3​x​ℒL=\int d^{3}x\cal{L}. In what follows, we takeℒ=ℒ​(ϕ,∂μϕ){\cal L}={\cal L}(\phi,\partial_{\mu}\phi), for a real classical fieldϕ=ϕ​(t,𝐱)=ϕ​(x)\phi=\phi(t,\mathbf{x})=\phi(x). By employing an intrinsic variation:ϕ′​(x)=ϕ​(x)+δ​ϕ​(x)\phi^{\prime}(x)=\phi(x)+\delta\phi(x)(1)

we can apply Hamilton’s principle to find the Euler–Lagrange equation:∂μ∂ℒ∂(∂μϕ)−∂ℒ∂ϕ=0\partial_{\mu}\frac{\partial{\cal L}}{\partial(\partial_{\mu}\phi)}-\frac{\partial{\cal L}}{\partial\phi}=0(2)

If we now plug the Lagrangian density:ℒ=12​(∂ϕ)2−12​m2​ϕ2{\cal L}=\frac{1}{2}(\partial\phi)^{2}-\frac{1}{2}m^{2}\phi^{2}(3)

where(∂ϕ)2≡∂μϕ​∂μϕ(\partial\phi)^{2}\equiv\partial_{\mu}\phi\partial^{\mu}\phi, into the Euler–Lagrange equation, we find the
following field equation:(∂2+m2)​ϕ=0\left(\partial^{2}+m^{2}\right)\phi=0(4)

which is known as the Klein–Gordon equation. Its solutions are plane waves
with energy dispersionE2=𝐩2+m2E^{2}=\mathbf{p}^{2}+m^{2}or, more generally,
the field Fourier-mode expansion:ϕ​(t,𝐱)=∫d3​k(2​π)3​2​ω​[a​(𝐤)​e−i​k​x+a∗​(𝐤)​ei​k​x]\phi(t,\mathbf{x})=\int\frac{d^{3}k}{(2\pi)^{3}2\omega}\left[a(\mathbf{k})e^{-ikx}+a^{*}(\mathbf{k})e^{ikx}\right](5)

where we are employing a Lorentz-invariant integration measure and
the angular frequency isω=𝐤2+m2\omega=\sqrt{\mathbf{k}^{2}+m^{2}}.

Still at the level of classical field theory,
we can examine what happens under a more
general transformation than that in Eq. (1).
Specifically, we introduce the total variation:ϕ′​(x′)=ϕ​(x)+δ~​ϕ​(x)\phi^{\prime}(x^{\prime})=\phi(x)+\tilde{\delta}\phi(x)(6)

wherex′μ=xμ+δ​xμ{x^{\prime}}^{\mu}=x^{\mu}+\delta x^{\mu}(7)

A transformation wherein we go fromℒ​(ϕ​(x),∂ϕ​(x)/∂xμ){\cal L}(\phi(x),\partial\phi(x)/\partial x^{\mu})toℒ​(ϕ′​(x′),∂ϕ′​(x′)/∂x′⁣μ){\cal L}(\phi^{\prime}(x^{\prime}),\partial\phi^{\prime}(x^{\prime})/\partial x^{\prime\mu})while at the same time leaving the action functional
(𝒮=∫𝑑t​L{\cal S}=\int dtL) invariant is known as a symmetry.
A crucial result in this connection is Noether’s theorem: every continuous global symmetry transformation leads to a conserved current. Explicitly, we have:jμ≡[∂ℒ∂(∂μϕ)​∂νϕ−ηνμ​ℒ]​δ​xν−∂ℒ∂(∂μϕ)​δ~​ϕj^{\mu}\equiv\left[\frac{\partial{\cal L}}{\partial(\partial_{\mu}\phi)}\partial_{\nu}\phi-\eta_{\nu}^{\mu}{\cal L}\right]\delta x^{\nu}-\frac{\partial{\cal L}}{\partial(\partial_{\mu}\phi)}\tilde{\delta}\phi(8)

and∂μjμ=0\partial_{\mu}j^{\mu}=0.

Classically (still), we can pass to the
Hamiltonian formalism, employing
the HamiltonianHHand the Hamiltonian densityℋ\cal{H}, related viaH=∫d3​x​ℋH=\int d^{3}x\cal{H}. This is connected to the Lagrangian formalism
via the Legendre transform:ℋ​(x)≡π​(x)​ϕ˙​(x)−ℒ​(x){\cal H}(x)\equiv\pi(x)\dot{\phi}(x)-{\cal L}(x)(9)

where the canonically conjugate momentum densityπ​(x)\pi(x)is given
in terms of a functional derivative of the Lagrangian:π​(t,𝐱)≡δ​Lδ​ϕ˙​(t,𝐱)\pi(t,\mathbf{x})\equiv\frac{\delta L}{\delta\dot{\phi}(t,\mathbf{x})}(10)

Crucially, if we apply Noether’s theorem to the case of time translation,
the conserved charge is precisely the HamiltonianHH.
For the case of Eq. (3), Eq. (10) leads toπ=ϕ˙\pi=\dot{\phi}and therefore:ℋ=12​π2​(x)+12​(∇ϕ​(x))2+12​m2​ϕ2​(x)\displaystyle{\cal H}=\frac{1}{2}\pi^{2}(x)+\frac{1}{2}(\nabla\phi(x))^{2}+\frac{1}{2}m^{2}\phi^{2}(x)(11)

Observe that this is (semi-) positive definite.

The Hamiltonian formalism can be used as a stepping stone to impose
canonical quantization: we promote the fieldsϕ​(t,𝐱)\phi(t,\mathbf{x})andπ​(t,𝐱)\pi(t,\mathbf{x})to operatorsϕ^H​(t,𝐱)\hat{\phi}_{H}(t,\mathbf{x})andπ^H​(t,𝐱)\hat{\pi}_{H}(t,\mathbf{x}), respectively.
These are quantum fields (in the Heisenberg picture)
which obey the canonical
equal-time commutation relations:[ϕ^H​(t,𝐱),π^H​(t,𝐲)]\displaystyle\left[\hat{\phi}_{H}(t,\mathbf{x}),\hat{\pi}_{H}(t,\mathbf{y})\right]=i​δ(3)​(𝐱−𝐲)\displaystyle=i\delta^{(3)}(\mathbf{x}-\mathbf{y})(12)[ϕ^H​(t,𝐱),ϕ^H​(t,𝐲)]\displaystyle\left[\hat{\phi}_{H}(t,\mathbf{x}),\hat{\phi}_{H}(t,\mathbf{y})\right]=[π^H​(t,𝐱),π^H​(t,𝐲)]=0\displaystyle=\left[\hat{\pi}_{H}(t,\mathbf{x}),\hat{\pi}_{H}(t,\mathbf{y})\right]=0

Together with the Heisenberg equations of motion:i​∂∂t​ϕ^H​(t,𝐱)\displaystyle i\frac{\partial}{\partial t}\hat{\phi}_{H}(t,\mathbf{x})=[ϕ^H​(t,𝐱),H^]\displaystyle=[\hat{\phi}_{H}(t,\mathbf{x}),\hat{H}](13)i​∂∂t​π^H​(t,𝐱)\displaystyle i\frac{\partial}{\partial t}\hat{\pi}_{H}(t,\mathbf{x})=[π^H​(t,𝐱),H^]\displaystyle=[\hat{\pi}_{H}(t,\mathbf{x}),\hat{H}]

the commutation relations lead to the following field equation:[∂2∂t2−∇2+m2]​ϕ^H​(t,𝐱)=0\left[\frac{\partial^{2}}{\partial t^{2}}-\nabla^{2}+m^{2}\right]\hat{\phi}_{H}(t,\mathbf{x})=0(14)

which is an operator version of the Klein–Gordon equation from Eq. (4).
Crucially, this was aresult, not a mere promotion of the classical
field equation.
Its solution is, similarly,
an operator version of the field expansion in Eq. (5), namely the Hermitian quantum field:ϕ^H​(t,𝐱)=∫d3​k(2​π)3​2​ω​[a^​(𝐤)​e−i​k​x+a^†​(𝐤)​ei​k​x]\hat{\phi}_{H}(t,\mathbf{x})=\int\frac{d^{3}k}{(2\pi)^{3}2\omega}\left[\hat{a}(\mathbf{k})e^{-ikx}+\hat{a}^{\dagger}(\mathbf{k})e^{ikx}\right](15)

where the time-independent coefficientsa^​(𝐤)\hat{a}(\mathbf{k})anda^†​(𝐤)\hat{a}^{\dagger}(\mathbf{k})are now operators. If we now plug this field expansion
back into the Hamiltonian, we will be pleased to find out that the latter is diagonal:H^=∫d3​k(2​π)3​2​ω​ω​a^†​(𝐤)​a^​(𝐤)\hat{H}=\int\frac{d^{3}k}{(2\pi)^{3}2\omega}\omega\hat{a}^{\dagger}(\mathbf{k})\hat{a}(\mathbf{k})(16)

where we implicitly normal-ordered; the N-operation here (normal-ordering) places all creation operators
to the left of all annihilation operators.
Another important quantity to consider is the time-ordered two-point
function:ΔF​(xA−xB)≡⟨0|T​[ϕ^H​(xA)​ϕ^H​(xB)]|0⟩=∫d4​k(2​π)4​ik2−m2+i​ϵ​e−i​k​(xA−xB)\Delta_{F}(x_{A}-x_{B})\equiv\langle 0|T[\hat{\phi}_{H}(x_{A})\hat{\phi}_{H}(x_{B})]|0\rangle=\int\frac{d^{4}k}{(2\pi)^{4}}\frac{i}{k^{2}-m^{2}+i\epsilon}e^{-ik(x_{A}-x_{B})}(17)

also known as a Feynman propagator. The T-operation means “later to the left.”

The above approach (promote classical to quantum fields, impose equal-time commutation relations, use the Heisenberg equations of motion, and solve the field equation via a Fourier-mode decomposition) works fine for the non-interacting theory of Eq. (11), but gets us in trouble as soon as we turn interactions on. In the latter case, a better approach is to work in the interaction picture,
splitting the Hamiltonian into an “easy” and a “hard” part:H^0I\displaystyle\hat{H}_{0}^{I}=∫d3​x​(12​π^I2​(t,𝐱)+12​(∇ϕ^I​(t,𝐱))2+12​m2​ϕ^I2​(t,𝐱))\displaystyle=\int d^{3}x\left(\frac{1}{2}\hat{\pi}_{I}^{2}(t,\mathbf{x})+\frac{1}{2}(\nabla\hat{\phi}_{I}(t,\mathbf{x}))^{2}+\frac{1}{2}m^{2}\hat{\phi}_{I}^{2}(t,\mathbf{x})\right)(18)H^1I​(t)\displaystyle\hat{H}_{1}^{I}(t)=λ4​∫d3​x​ϕ^I4​(t,𝐱)\displaystyle=\frac{\lambda}{4}\int d^{3}x\hat{\phi}_{I}^{4}(t,\mathbf{x})

where the field expansion in Eq. (15) now applies
to the interaction-picture quantum field,ϕ^I​(t,𝐱)\hat{\phi}_{I}(t,\mathbf{x}),
and we are studying the case of a quartic interaction.
The idea, then, is to take the Dyson series for the scattering
operator:S^=∑n=0∞(−i)n​1n!​∫d4​x1​∫d4​x2​⋯​∫d4​xn​T​[ℋ^1I​(x1)​ℋ^1I​(x2)​⋯​ℋ^1I​(xn)]\displaystyle\hat{S}=\sum_{n=0}^{\infty}\left(-i\right)^{n}\frac{1}{n!}\int d^{4}x_{1}\int d^{4}x_{2}\cdots\int d^{4}x_{n}T\left[\hat{{\cal H}}_{1}^{I}(x_{1})\hat{{\cal H}}_{1}^{I}(x_{2})\cdots\hat{{\cal H}}_{1}^{I}(x_{n})\right](19)

and sandwich it between specific states,Sb​a≡⟨ub|S^|ua⟩S_{ba}\equiv\langle u_{b}|\hat{S}|u_{a}\rangle,
to produce the S-matrix (amplitude),
which is related to experimental observables.

Our task is
to evaluate the vacuum expectation value of time-ordered products
of increasingly more and more operators. This is vastly
simplified if we introduce the concept of a Wick contraction:T​[ϕ^I​(x)​ϕ^I​(y)]=N​[ϕ^I​(x)​ϕ^I​(y)]+​ϕ^I​(x)​ϕ^I​(y)T[\hat{\phi}_{I}(x)\hat{\phi}_{I}(y)]=N[\hat{\phi}_{I}(x)\hat{\phi}_{I}(y)]+\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 11.81842pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=23.41002pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.5pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 11.81842pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=23.41002pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.5pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 10.17885pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=20.24371pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 9.47401pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=18.88495pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{\phi}_{I}(x)\hat{\phi}_{I}(y)(20)

The many-operator generalization of the above is known as Wick’s theorem:T​[A^​B^​C^​D^​E^​F^​⋯​Z^]\displaystyle T[\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]=N​[A^​B^​C^​D^​E^​F^​⋯​Z^]\displaystyle=N[\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+N​[​A^​B^​C^​D^​E^​F^​⋯​Z^]+N​[​A^​B^​C^​D^​E^​F^​⋯​Z^]+N​[​A^​B^​C^​D^​E^​F^​⋯​Z^]+⋯\displaystyle\quad+N[\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+N[\mathchoice{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+N[\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+\cdots+N​[​A^​B^​C^​D^​E^​F^​⋯​Z^]+N​[​A^​B^​C^​D^​E^​F^​⋯​Z^]+N​[​A^​B^​C^​D^​E^​F^​⋯​Z^]+⋯\displaystyle\quad+N[\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\mathchoice{\vbox{\hbox to0.0pt{\kern 11.11115pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 11.11115pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 11.11115pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 11.11115pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+N[\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\mathchoice{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+N[\mathchoice{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+\cdots+N​[​A^​B^​C^​D^​E^​F^​⋯​Z^]+N​[​A^​B^​C^​D^​E^​F^​⋯​Z^]+N​[​A^​B^​C^​D^​E^​F^​⋯​Z^]+⋯\displaystyle\quad+N[\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\mathchoice{\vbox{\hbox to0.0pt{\kern 11.11115pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 11.11115pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 11.11115pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 11.11115pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\mathchoice{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+N[\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\mathchoice{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=11.11115pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\mathchoice{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+N[\mathchoice{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 5.55557pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt\vrule width=16.66672pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=8.61108pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\mathchoice{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 22.22229pt\kern 2.77779pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=5.55557pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\hat{F}\cdots\hat{Z}]+\cdots+N​[higher contractions]\displaystyle\quad+N[\text{higher contractions}](21)

This expresses the time-ordered product of a set of operators as the sum of contracted normal-ordered products of the same operators.(a)(b)(c)Figure 1:Connected, momentum-space, second-order Feynman diagrams representing the S-matrix in a2→22\rightarrow 2process (for a quartic interaction) in thess,tt, anduuchannels.

Consider a specific physical setting, where you have two particles
in the initial state and two in the final state. The S-matrix then becomes:S𝐩1​𝐩2,𝐪1​𝐪2=⟨0|a^​(𝐩1)​a^​(𝐩2)​S^​a^†​(𝐪1)​a^†​(𝐪2)|0⟩\displaystyle S_{\mathbf{p}_{1}\mathbf{p}_{2},\mathbf{q}_{1}\mathbf{q}_{2}}=\langle 0|\hat{a}(\mathbf{p}_{1})\hat{a}(\mathbf{p}_{2})\hat{S}\hat{a}^{\dagger}(\mathbf{q}_{1})\hat{a}^{\dagger}(\mathbf{q}_{2})|0\rangle=⟨0|a^​(𝐩1)​a^​(𝐩2)​a^†​(𝐪1)​a^†​(𝐪2)|0⟩+(−i)​λ4​∫d4​x​⟨0|T​[a^​(𝐩1)​a^​(𝐩2)​ϕ^I4​(x)​a^†​(𝐪1)​a^†​(𝐪2)]|0⟩\displaystyle=\langle 0|\hat{a}(\mathbf{p}_{1})\hat{a}(\mathbf{p}_{2})\hat{a}^{\dagger}(\mathbf{q}_{1})\hat{a}^{\dagger}(\mathbf{q}_{2})|0\rangle+(-i)\frac{\lambda}{4}\int d^{4}x\langle 0|T\left[\hat{a}(\mathbf{p}_{1})\hat{a}(\mathbf{p}_{2})\hat{\phi}^{4}_{I}(x)\hat{a}^{\dagger}(\mathbf{q}_{1})\hat{a}^{\dagger}(\mathbf{q}_{2})\right]|0\rangle+(−i)2​12!​(λ4)2​∫d4​x​d4​y​⟨0|T​[a^​(𝐩1)​a^​(𝐩2)​ϕ^I4​(x)​ϕ^I4​(y)​a^†​(𝐪1)​a^†​(𝐪2)]|0⟩+⋯\displaystyle\quad+(-i)^{2}\frac{1}{2!}\left(\frac{\lambda}{4}\right)^{2}\int d^{4}xd^{4}y\langle 0|T\left[\hat{a}(\mathbf{p}_{1})\hat{a}(\mathbf{p}_{2})\hat{\phi}^{4}_{I}(x)\hat{\phi}^{4}_{I}(y)\hat{a}^{\dagger}(\mathbf{q}_{1})\hat{a}^{\dagger}(\mathbf{q}_{2})\right]|0\rangle+\cdots(22)

which can be evaluated using Wick’s theorem.
At second order, the contributions can be summarized graphically via
the (momentum-space) Feynman diagrams of Fig.1.
Symbolically, all three contributions take the form of the following
loop integral:J​(l2)\displaystyle J(l^{2})=∫d4​k(2​π)4​1k2−m2+i​ϵ​1(k−l)2−m2+i​ϵ\displaystyle=\int\frac{d^{4}k}{(2\pi)^{4}}\frac{1}{k^{2}-m^{2}+i\epsilon}\frac{1}{(k-l)^{2}-m^{2}+i\epsilon}(23)

where our notation reflects the fact that this quantity is Lorentz invariant.
We can combine the two denominators using the following
identity:1a​b=∫01d​x[(1−x)​a+x​b]2\displaystyle\frac{1}{ab}=\int_{0}^{1}\frac{dx}{[(1-x)a+xb]^{2}}(24)

wherexxis known as Feynman parameter. This leads to:J​(l2)\displaystyle J(l^{2})=∫01𝑑x​∫d4​k(2​π)4​1[k2−Δ+i​ϵ]2\displaystyle=\int_{0}^{1}dx\int\frac{d^{4}k}{(2\pi)^{4}}\frac{1}{\left[k^{2}-\Delta+i\epsilon\right]^{2}}(25)

whereΔ≡m2−x​(1−x)​l2\Delta\equiv m^{2}-x(1-x)l^{2}.

## IIIMistakes and corrections

Just like in Refs.GezerlisWilliams1,andGezerlisWilliams2,, our goal is to discuss how certain
reasonably subtle topics
should be correctly understood, not to criticize authors who toiled
hard to produce respected textbooks on a given subject. Thus,
we will now cite a superset of references, containing standard textbooks
that all discuss related
topics.Aitchison;Alvarez;Banks;Baulieu;Bogoliubov;Brown;Coleman;Das;Donoghue;Folland;Fradkin;Gelis;Greiner;Gross;Hatfield;Itzykson;Kleinert;Lancaster;Maggiore;Mandl;Nastase;Padmanabhan;Peskin;Radovanovic;Ramond;Ryder;Schwartz;Srednicki;Stone;Talagrand;Williams;Zee;Zinn-Justin(We have shared detailed bibliographic
information with the Editor and Referees of the present manuscript on specific instances from the literature where the incorrect claims appear.)
For each theme that is to follow, we first provide some context,
then give a specific quote from a QFT textbook (themistake),
proceed to discuss how and why
the physics going into the quote is wrong, and in the end provide a few-sentence improved version
(thecorrection).
To keep the coverage from ballooning, some of these misconceptions are touched upon
but not explored in detail (after all, this work addresses not one, butsixmistakes); with that in mind, we cite works by acknowledged experts, where the reader can discover more on each subject.
In some of the excerpts we have tweaked the notation, in order to keep
things consistent with sectionII; the original
quotes have not been modified in other ways (unless explicitly marked).

## III.1Relativistic quantum mechanics

Textbooks on quantum mechanics (QM) typically start with a brief quasi-historical overview of the old quantum theory. Similarly, textbooks on quantum field theory often have an introductory chapter on relativistic quantum mechanics, pointing out that it is difficult to set up a consistent theory that way, thereby motivating the alternative approach of quantum field theory. While that is reasonable enough, one should not go overboard: it doesn’t help readers to
claim that an old approach is more diseased than it actually is.
The methodological principle of charity is not merely a matter of
principle: some of the alleged problems with relativistic QM re-appear in
the context of QFT, but they are typically passed over in silence. A careful reader/student is then left with the discomfort of not fully understanding
why one approach is bad and the other good.

Mistake #1“Thus, negative energiesE=−𝐩2+m2E=-\sqrt{\mathbf{p}^{2}+m^{2}}are on the same footing as the physical onesE=+𝐩2+m2E=+\sqrt{\mathbf{p}^{2}+m^{2}}. This is a severe difficulty
because the spectrum is no longer bounded
from below. It seems that an arbitrarily large
amount of energy may be extracted from the
system […] This is clearly a failure of the
concept of stable stationary states.”

The claim here is that the negative energy solutions of the Klein–Gordon
equation, cf. Eq. (4), in its guise as a single-particle relativistic generalization of
the Schrödinger equation:[∂2∂t2−∇2+m2]​ψ​(t,𝐱)=0\left[\frac{\partial^{2}}{\partial t^{2}}-\nabla^{2}+m^{2}\right]\psi(t,\mathbf{x})=0(26)

are a conceptual blight, which forces us to stop
studying relativistic QM. To be explicit, this refers to the plane-wave
solutions:ψ​(t,𝐱)=N​ei​(𝐩⋅𝐱−E​t)\psi(t,\mathbf{x})=Ne^{i(\mathbf{p}\cdot\mathbf{x}-Et)}(27)

for whichE=±𝐩2+m2E=\pm\sqrt{\mathbf{p}^{2}+m^{2}}.

A connection is typically also made with the continuity equation:∂ρ∂t+∇⋅𝐣=0\frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf{j}=0(28)

where, for our problem:ρ\displaystyle\rho=i2​m​(ψ∗​∂ψ∂t−ψ​∂ψ∗∂t),𝐣\displaystyle=\frac{i}{2m}\left(\psi^{*}\frac{\partial\psi}{\partial t}-\psi\frac{\partial\psi^{*}}{\partial t}\right),\quad\mathbf{j}=12​m​i​(ψ∗​∇ψ−ψ​∇ψ∗)\displaystyle=\frac{1}{2mi}\left(\psi^{*}\nabla\psi-\psi\nabla\psi^{*}\right)(29)

If we plug in the plane waves of Eq. (27), this gives:ρ=|N|2​Em,𝐣=|N|2​𝐩m\displaystyle\rho=|N|^{2}\frac{E}{m},\quad\mathbf{j}=|N|^{2}\frac{\mathbf{p}}{m}(30)

The alleged issue is that the
probability density containsEEbut, sinceE=±𝐩2+m2E=\pm\sqrt{\mathbf{p}^{2}+m^{2}}tells us thatEEcan be either positive or negative,ρ\rhoisn’t positive definite.
Crucially, the conclusions on bothEEandρ\rhoare drawn still
at the level of a single, non-interacting particle.

In classical mechanics, the existence of unphysical solutions is typically
sidestepped by noting that they can simply be omitted, precisely because
they are unphysical.
Unlike what so many modern textbooks claim, exactly the same thing can be
done in a relativistic quantum mechanical theory.
Negative energy solutions are not an issue, if all we’re dealing with
is a free particle:
a particle in a positive-energy stateE=+𝐩2+m2E=+\sqrt{\mathbf{p}^{2}+m^{2}}that doesn’t experience any interactions will simply remain in that state.
Similarly, sinceE>0E>0we see from Eq. (30) thatρ\rhowill also remain positive at all times. As pointed out
in the early classic QFT textbook by S. Schweber
(Ref.Schweber,, p. 56):
“a consistent theory can be developed for a free particle if we adopt the manifold of positive energy solutions as the set of states which are physically realizable by a free particle.”
A similar argument can be put forward in terms of wave packets,
modifying Eq. (5)—see also sectionIII.4below.

You may be experiencing minor discomfort at this stage: can one just
arbitrarily drop one half of our solutions? Isn’t that conceptually unsatisfying?
In other words, perhaps onedoesneed to give up on relativistic QM in
favor of a more advanced theory (namely QFT) that doesn’t suffer from this
arbitrariness? The part of the story that the texbooks typically leave out
is that we are faced with a similar arbitrariness in field theory:
we mentioned above that when applying the current coming from
Noether’s theorem, Eq. (8)
to the case of time translation, the conserved charge is precisely the HamiltonianHH. But why did we pickthatsign in the current of Eq. (8) in the first place? After all,
if∂μjμ=0\partial_{\mu}j^{\mu}=0then∂μ(−jμ)=0\partial_{\mu}(-j^{\mu})=0also holds.
The answer is simply that we wrote the Noether current in that specific
form in order to ensure that we would end up with a positive definite Hamiltonian.
In other words, wechoseto work with a positive energy even in a field theoretic context.

Correction #1There is nothing wrong with using the Klein-Gordon equation to describe a single relativistic particle, provided there are no interactions/perturbations involved. A particle that starts in
a positive energy state will remain in that state. A similarly arbitrary choice in favor of positive energy is also made in field theory.
The relativistic QM story is, indeed, complicated if you turn on the interactions but, then again, interacting QFT isn’t child’s play, either.

## III.2Noether’s theorem

In sectionIIwe stated Noether’s theorem in words
(every continuous global symmetry transformation leads to a conserved current)
and then showed the Noether current, Eq. (8), without
proof. This was given in the general case where both internal and spacetime symmetry transformations are being considered at the same time. Many standard
textbooks study these two scenarios separately (or even worse, examine
special cases without a general derivation), thereby obscuring the physics
behind this most important theorem. As we will now see, sometimes even
the sources thatdogo into a general derivation of Noether’s theorem
use notation that ranges from impenetrable to flat-out wrong.

Mistake #2“We now show how to derive [the field equation] from a variational principle applied to an action:𝒮=∫ℒ​(ϕ,∂μϕ)​d4​x\mathcal{S}=\int\mathcal{L}(\phi,\partial_{\mu}\phi)d^{4}x(31)

[…] We now subject both the field variable and the coordinates to a variation
which vanishes on the boundary∂R\partial R:xμ\displaystyle x^{\mu}→x′μ=xμ+δ​xμ,\displaystyle\rightarrow{x^{\prime}}^{\mu}=x^{\mu}+\delta x^{\mu},ϕ​(x)\displaystyle\phi(x)→ϕ′​(x)=ϕ​(x)+δ​ϕ​(x)\displaystyle\rightarrow\phi^{\prime}(x)=\phi(x)+\delta\phi(x)

It is convenient to consider the case whereℒ\mathcal{L}depends explicitly onxμx^{\mu}:ℒ=ℒ​(ϕ,∂μϕ,xμ)\mathcal{L}=\mathcal{L}(\phi,\partial_{\mu}\phi,x^{\mu})(32)

this happens ifϕ\phiinteracts with an external source, and so does not describe
a closed system.”

Let us briefly summarize what is at stake: like all textbooks studying
scalar QFT, this one makes the reasonable assumption that the main focus
of study will be theories of the formℒ​(ϕ,∂μϕ)\mathcal{L}(\phi,\partial_{\mu}\phi)—e.g., a theory made up of a kinetic term and a quartic
self-interaction. However, instead of making that assumption and sticking
to it when the time comes to derive Noether’s theorem, this introductory
textbook feels the need to soften the requirement
of translation invariance (which forbids an explicitxμx^{\mu}dependence)
for a single section, only to return to the usualℒ​(ϕ,∂μϕ)\mathcal{L}(\phi,\partial_{\mu}\phi)later on. Similarly, other references go even farther when deriving
Noether’s theorem,
writing the Lagrangian density simply
asℒ​(x)\mathcal{L}(x), without any reference to fields.

The discomfort of these authors arises when they try to generalize the
intrinsic and total variations of Eq. (1) and Eq. (6) to the Lagrangian density, namely:ℒ​(ϕ′​(x′),∂ϕ′​(x′)/∂x′⁣μ)=ℒ​(ϕ​(x),∂ϕ​(x)/∂xμ)+δ~​ℒ{\cal L}(\phi^{\prime}(x^{\prime}),\partial\phi^{\prime}(x^{\prime})/\partial x^{\prime\mu})={\cal L}(\phi(x),\partial\phi(x)/\partial x^{\mu})+\tilde{\delta}{\cal L}(33)

andℒ​(ϕ′​(x),∂ϕ′​(x)/∂xμ)=ℒ​(ϕ​(x),∂ϕ​(x)/∂xμ)+δ​ℒ{\cal L}(\phi^{\prime}(x),\partial\phi^{\prime}(x)/\partial x^{\mu})={\cal L}(\phi(x),\partial\phi(x)/\partial x^{\mu})+\delta{\cal L}(34)

The crucial part in the argument emerges when one tries to relate
the two variations via the formula:δ~​ℒ=δ​ℒ+∂ℒ∂xμ​δ​xμ\tilde{\delta}{\cal L}=\delta{\cal L}+\frac{\partial{\cal L}}{\partial x^{\mu}}\delta x^{\mu}(35)

The issue has to do with the presence of the∂ℒ/∂xμ\partial\mathcal{L}/\partial x^{\mu}term: if there is no explicit dependence onxμx^{\mu}, one would
naively think that the derivative vanishes, in which case the two
variations coincide. Hence, some authors choose to introduce anad hocxx-dependence just to provide surface respectability to Eq. (35).

The resolution comes from considering the Lagrangian density without
any extraneous assumptions:ℒ=ℒ​(ϕ​(x),∂ϕ​(x)/∂xν){\cal L}={\cal L}(\phi(x),\partial\phi(x)/\partial x^{\nu}).
In Eq. (35), we are faced with the chain rule
in partial differentiation, when there are four independent variables (thexμx^{\mu}’s):∂ℒ​(ϕ​(x),∂ϕ​(x)/∂xν)∂xμ=∂ℒ​(ϕ​(x),∂ϕ​(x)/∂xν)∂ϕ​∂ϕ​(x)∂xμ+∂ℒ​(ϕ​(x),∂ϕ​(x)/∂xν)∂(∂ϕ​(x)/∂xν)​∂2ϕ​(x)∂xν​∂xμ\frac{\partial{\cal L}(\phi(x),\partial\phi(x)/\partial x^{\nu})}{\partial x^{\mu}}=\frac{\partial{\cal L}(\phi(x),\partial\phi(x)/\partial x^{\nu})}{\partial\phi}\frac{\partial\phi(x)}{\partial x^{\mu}}+\frac{\partial{\cal L}(\phi(x),\partial\phi(x)/\partial x^{\nu})}{\partial(\partial\phi(x)/\partial x^{\nu})}\frac{\partial^{2}\phi(x)}{\partial x^{\nu}\partial x^{\mu}}(36)

as shown (though not emphasized) on p. 12 of the very
careful textbook by G. Sterman.StermanIf you’re thinking that one should have been using the total derivative,d/d​xμd/dx^{\mu}, here—or, say, in the Euler-Lagrange Eq. (2)—you will be disappointed:
that notation is relevant only when there is asingleindependent variable, whereas we are dealing with four inxμx^{\mu}.
According to Salam’s criterion,Salamone’s goal is always “to find a notation which is both concise and intelligible to at least two people of whom one may be the author.”

Correction #2When dealing with a theoryℒ​(ϕ,∂μϕ)\mathcal{L}(\phi,\partial_{\mu}\phi), we don’t get to introduce an explicitxx-dependence by hand just because we feel uncomfortable about the presence of the derivative∂ℒ/∂xμ\partial\mathcal{L}/\partial x^{\mu}in the derivation of Noether’s theorem.
The notation reflects the chain rule in partial differentiation. There is no need for an explicitxx-dependence and that’s a good thing, because Noether’s theorem
applies to translation-invariant theories.

## III.3Lagrangians and canonical quantization

Our crash course on QFT in sectionIIfollowed
a pretty standard route: classical field theory in the Lagrangian
formalism, a transition to the Hamiltonian formalism (still at the classical level),
and then canonical quantization (using the Hamiltonian formalism and promoting
classical fields to operators). In our exposition we were clear that
the Euler–Lagrange equations are a classical (and Lagrangian-based) construct,
whereas the Heisenberg equations of motion were a quantum (and Hamiltonian-based) construct.
While the result in both cases was the same (the Klein–Gordon equation, for
a non-interacting theory), the flavor of the two arguments was very different.
The narrative is complicated by authors who, without much fanfare, go on to
discuss a linear combination of the two approaches:

Mistake #3“The Hamiltonian and Lagrangian density operators have the same relationship as their classical counterparts and are related by a Legendre transformation,H^≡∫d3​x​ℋ^≡∫d3​x​π^​(x)​ϕ^˙​(x)−L^=∫d3​x​(π^​(x)​ϕ^˙​(x)−ℒ^)\hat{H}\equiv\int d^{3}x\hat{\mathcal{H}}\equiv\int d^{3}x\hat{\pi}(x)\dot{\hat{\phi}}(x)-\hat{L}=\int d^{3}x\left(\hat{\pi}(x)\dot{\hat{\phi}}(x)-\hat{{\cal L}}\right)(37)

where the canonical momentum density operatorπ^​(x)\hat{\pi}(x)is defined asπ^​(x)≡δ​L^δ​ϕ^˙​(x)=∂ℒ^∂ϕ^˙​(x)\hat{\pi}(x)\equiv\frac{\delta\hat{L}}{\delta\dot{\hat{\phi}}(x)}=\frac{\partial\hat{{\cal L}}}{\partial\dot{\hat{\phi}}(x)}(38)

Since the operator equations of motion are the same as their classical equivalents, then the operators
must also obey the Euler-Lagrange equations […] at the operator level for the Heisenberg
picture operatorϕ^​(x)\hat{\phi}(x), […]∂μ∂ℒ^∂(∂μϕ^)​(x)−∂ℒ^∂ϕ^​(x)=0\partial_{\mu}\frac{\partial\hat{{\cal L}}}{\partial(\partial_{\mu}\hat{\phi})(x)}-\frac{\partial\hat{{\cal L}}}{\partial\hat{\phi}(x)}=0(39)

”

This quote (and many others like it) is mixing the two general
philosophies which we were careful to distinguish above: in canonically
quantized QFT, quantum fields appear only in the Hamiltonian formalism,
while the Lagrangian formalism involves only classical fields.
(Admittedly, Schwinger’s quantum action formalism—see section 2.1 of P. Roman’s
unjustly forgotten textbookRoman—indeed combines the two,
but does so consistently, unlike discussions which
promote classical to quantum fields
in selected equationsby fiat. Most notably, such an approach
motivates the equal-time commutation relations of Eq. (12).)
Thus, the fact that one ends up with the same field equation is aresult, whereas in the quote this is
essentially a starting assumption.

The main issue here is that it is far from clear why
one should abandon the clear path discussed above (and in all QFT textbooks) for
a mixing approach if one doesn’t introduce any added benefits.
At a more detailed level,
there are three main reasons why it is ill-advised for one to
promote classical to quantum fields in the Lagrangian formalism,
thereby ending up with a Lagrangian density which is an operator,ℒ^\hat{{\cal L}}. First, there is the principle of the matter:
as S. Weinberg points out on p. 300 of his classic textbook,Weinbergin all our theories we require that the action𝒮\mathcal{S}be real.
If the Lagrangian density is an operator, then its spacetime integral
(the action) is also an operator, but then it cannot be a real number.
Second, in the path-integral approach to quantum field theory
(not further touched upon in this article) one is faced
with the action and quantum fields that are
c-number functions (not operators). Thus,
it is very confusing to beginners, who are still trying to figure out
what is an operator and what is not, to be told that
quantum fields show up as operators in a Lagrangian context,
despite the fact that we only talk about Lagrangians before we start the canonical
quantization program (and quantum fields are not operators in the path integral
program).

Third, one must be careful in handling
classical vs quantum fieldseven whenstudying the Hamiltonian
formalism in the canonical quantization setting. The prototypical case
in this connection is that of derivative couplings; let’s take
the theory of scalar electrodynamics:ℒ=∂μφ∗​∂μφ−m2​φ∗​φ−14​Fμ​ν​Fμ​ν−i​q​(φ∗​∂μφ−φ​∂μφ∗)​Aμ+q2​Aμ​Aμ​φ∗​φ{\cal L}=\partial_{\mu}\varphi^{*}\partial^{\mu}\varphi-m^{2}\varphi^{*}\varphi-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}-iq(\varphi^{*}\partial^{\mu}\varphi-\varphi\partial^{\mu}\varphi^{*})A_{\mu}+q^{2}A_{\mu}A^{\mu}\varphi^{*}\varphi(40)

involving a complex scalar field and a gauge field.
The corresponding canonically conjugate momentum densities are:ϖ=φ˙∗−i​q​φ∗​A0,ϖ∗=φ˙+i​q​φ∗​A0,\varpi=\dot{\varphi}^{*}-iq\varphi^{*}A^{0},\qquad\varpi^{*}=\dot{\varphi}+iq\varphi^{*}A^{0},(41)

Crucially, you can’t willy-nilly promote classical fields to operators here.
Instead, one must employ the equation of motion
for an operatorO^I​(t)\hat{O}_{I}(t)in the interaction picture, namely:i​∂∂t​O^I​(t)=[O^I​(t),H^0I]i\frac{\partial}{\partial t}\hat{O}_{I}(t)=[\hat{O}_{I}(t),\hat{H}_{0}^{I}](42)

This leads to:ϖ^I​(t,𝐱)=∂∂t​φ^I†​(t,𝐱),ϖ^I†​(t,𝐱)=∂∂t​φ^I​(t,𝐱)\hat{\varpi}_{I}(t,\mathbf{x})=\frac{\partial}{\partial t}\hat{\varphi}_{I}^{\dagger}(t,\mathbf{x}),\qquad\hat{\varpi}_{I}^{\dagger}(t,\mathbf{x})=\frac{\partial}{\partial t}\hat{\varphi}_{I}(t,\mathbf{x})(43)

which clearly look different than what we had in Eq. (41).

Correction #3When canonically quantizing field theory, there is no need to promote fields to operators in the Lagrangian formalism. This helps you avoid ending up with an action that is not
a real number. It is much more natural to always start with the Lagrangian density,
move to the Hamiltonian formulation, and then impose canonical quantization.

## III.4Particle localization

The question of what a quantum fieldreally isis left
far too vague in far too many introductory treatments. Students
spend a good chunk of their undergraduate education learning
that quantum mechanics is different from classical mechanics, only
to be told upon taking graduate QFT that everything is a quantum field
and particles (and the associated mechanics) are just the associated excitations.
This sounds like a pretty important point, but given the complexity of the calculations involved (as well as the need to study scalar, fermionic, and gauge fields), the core ideas in a QFT course
are typically given short shrift. It is therefore
commendable that some authors employ analogies with non-relativistic
physics in order to put forward an interpretation of the quantum field; unfortunately, as we will soon see,
an interpretation resulting from such an analogy is misleading.

Mistake #4“[ϕ^S​(𝐱),ϕ^S​(𝐲)]=[π^S​(𝐱),π^S​(𝐲)]=0\left[\hat{\phi}_{S}(\mathbf{x}),\hat{\phi}_{S}(\mathbf{y})\right]=\left[\hat{\pi}_{S}(\mathbf{x}),\hat{\pi}_{S}(\mathbf{y})\right]=0(44)

(For now we work in the Schrödinger picture whereϕ\phiandπ\pido not
depend on time.) […]
Finally let us consider the interpretation of the stateϕ^S​(𝐱)​|0⟩\hat{\phi}_{S}(\mathbf{x})|0\rangle. From the expansionϕ^S​(𝐱)=∫d3​k(2​π)3​2​ω​[a^​(𝐤)​ei​𝐤⋅𝐱+a^†​(𝐤)​e−i​𝐤⋅𝐱]\hat{\phi}_{S}(\mathbf{x})=\int\frac{d^{3}k}{(2\pi)^{3}2\omega}\left[\hat{a}(\mathbf{k})e^{i\mathbf{k}\cdot\mathbf{x}}+\hat{a}^{\dagger}(\mathbf{k})e^{-i\mathbf{k}\cdot\mathbf{x}}\right](45)

we see thatϕ^S​(𝐱)​|0⟩=∫d3​k(2​π)3​2​ω​e−i​𝐤⋅𝐱​|𝐤⟩\hat{\phi}_{S}(\mathbf{x})|0\rangle=\int\frac{d^{3}k}{(2\pi)^{3}2\omega}e^{-i\mathbf{k}\cdot\mathbf{x}}|\mathbf{k}\rangle(46)

is a linear superposition of single-particle states that have well-defined momentum. Except for the factor1/2​ω1/2\omega, this is the same as the familiar nonrelativistic expression for the eigenstate of position|𝐱⟩|\mathbf{x}\rangle); in fact the extra factor is nearly constant for small (nonrelativistic)𝐤\mathbf{k}. We will therefore put forward the same interpretation, and claim that the operatorϕ^S​(𝐱)\hat{\phi}_{S}(\mathbf{x}), acting on the vacuum,creates a particle at position𝐱\mathbf{x}.”

As just mentioned, the motivation behind trying to interpretϕ^S​(𝐱)​|0⟩\hat{\phi}_{S}(\mathbf{x})|0\rangleis excellent. The operatora^†​(𝐤)\hat{a}^{\dagger}(\mathbf{k})acting on the vacuum
creates a state|𝐤⟩|\mathbf{k}\rangle,
so it is worthwhile to investigate what the effect ofϕ^S​(𝐱)\hat{\phi}_{S}(\mathbf{x})is. We can
see from Eq. (46) that the right-hand side integrates
over single-particle states|𝐤⟩|\mathbf{k}\rangle, so it is quite
reasonable to assume that the left-hand side is a single-particle state itself. The problems
arise when authors take an extra step, ignoring the1/2​ω1/2\omegain the denominator,
thereby concluding thatϕ^S​(𝐱)​|0⟩\hat{\phi}_{S}(\mathbf{x})|0\rangleis
a particleat position𝐱\mathbf{x}.

Particle localization in relativistic theories is more complicated than
that.SchweberTo give a flavor of what’s involved, let us introduce
the Newton–Wigner position operator and a new localized field operator:𝐱^n​w≡−i​∇𝐤+i2​𝐤𝐤2+m2,ϕ^L​(𝐱)≡∫d3​k(2​π)3​12​ω​ei​𝐤⋅𝐱​a^​(𝐤)\hat{\mathbf{x}}_{nw}\equiv-i\nabla_{\mathbf{k}}+\frac{i}{2}\frac{\mathbf{k}}{\mathbf{k}^{2}+m^{2}},\qquad\hat{\phi}_{L}(\mathbf{x})\equiv\int\frac{d^{3}k}{(2\pi)^{3}}\frac{1}{\sqrt{2\omega}}e^{i\mathbf{k}\cdot\mathbf{x}}\hat{a}(\mathbf{k})(47)

Crucially,ϕ^L​(𝐱)\hat{\phi}_{L}(\mathbf{x})contains only a single plane-wave contribution.
It is straightforward to see that these two operators work together:𝐱^n​w​⟨0|ϕ^L​(𝐲)|𝐤⟩=𝐲​⟨0|ϕ^L​(𝐲)|𝐤⟩\displaystyle\hat{\mathbf{x}}_{nw}\langle 0|\hat{\phi}_{L}(\mathbf{y})|\mathbf{k}\rangle=\mathbf{y}\langle 0|\hat{\phi}_{L}(\mathbf{y})|\mathbf{k}\rangle(48)

to take the form of a position-eigenvalue equation. Crucially,
this new operator obeys the commutation relation:[ϕ^L​(𝐱),ϕ^L†​(𝐲)]=δ(3)​(𝐱−𝐲)[\hat{\phi}_{L}(\mathbf{x}),\hat{\phi}_{L}^{\dagger}(\mathbf{y})]=\delta^{(3)}(\mathbf{x}-\mathbf{y})(49)

which is clearly that of creation and annihilation operators in coordinate
space. One can certainly not say as much about the[ϕ^S​(𝐱),ϕ^S​(𝐲)]=0\left[\hat{\phi}_{S}(\mathbf{x}),\hat{\phi}_{S}(\mathbf{y})\right]=0of Eq. (44).

It is also worthwhile in this regard to examine the relationship betweenϕ^L​(𝐱)\hat{\phi}_{L}(\mathbf{x})and the usual quantum fieldϕ^S​(𝐱)\hat{\phi}_{S}(\mathbf{x}).
One can combine Eq. (45) and the corresponding relationship
givingπ^S​(𝐱)\hat{\pi}_{S}(\mathbf{x})in terms ofa^​(𝐤)\hat{a}(\mathbf{k})anda^†​(𝐤)\hat{a}^{\dagger}(\mathbf{k}), thereby deriving an equation which
givesa^​(𝐤)\hat{a}(\mathbf{k})in terms ofϕ^S​(𝐱)\hat{\phi}_{S}(\mathbf{x})andπ^S​(𝐱)\hat{\pi}_{S}(\mathbf{x}). Plugging that result into Eq. (47)
gives:ϕ^L​(𝐱)=12​∫d3​y​ϕ^S​(𝐲)​∫d3​k(2​π)3​ei​𝐤⋅(𝐱−𝐲)​[𝐤2+m2]1/4+i​12​∫d3​y​π^S​(𝐲)​∫d3​k(2​π)3​ei​𝐤⋅(𝐱−𝐲)​[𝐤2+m2]−1/4\displaystyle\hat{\phi}_{L}(\mathbf{x})=\frac{1}{\sqrt{2}}\int d^{3}y\hat{\phi}_{S}(\mathbf{y})\int\frac{d^{3}k}{(2\pi)^{3}}e^{i\mathbf{k}\cdot(\mathbf{x}-\mathbf{y})}\left[\mathbf{k}^{2}+m^{2}\right]^{1/4}+i\sqrt{\frac{1}{2}}\int d^{3}y\hat{\pi}_{S}(\mathbf{y})\int\frac{d^{3}k}{(2\pi)^{3}}e^{i\mathbf{k}\cdot(\mathbf{x}-\mathbf{y})}\left[\mathbf{k}^{2}+m^{2}\right]^{-1/4}(50)

If we do the integrals over𝐤\mathbf{k}, we will find
some modified Bessel functions. The essential point here is thatϕ^L​(𝐱)\hat{\phi}_{L}(\mathbf{x})is a spatial integral ofϕ^S​(𝐲)​f​(|𝐱−𝐲|)\hat{\phi}_{S}(\mathbf{y})f(|\mathbf{x}-\mathbf{y}|)andπ^S​(𝐲)​g​(|𝐱−𝐲|)\hat{\pi}_{S}(\mathbf{y})g(|\mathbf{x}-\mathbf{y}|), namely
a non-local function of the quantum fields; at large|𝐱−𝐲||\mathbf{x}-\mathbf{y}|, the
functionf​(|𝐱−𝐲|)f(|\mathbf{x}-\mathbf{y}|)goes asexp⁡(−m​|𝐱−𝐲|)/|𝐱−𝐲|9/4\exp(-m|\mathbf{x}-\mathbf{y}|)/|\mathbf{x}-\mathbf{y}|^{9/4},
whileg​(|𝐱−𝐲|)g(|\mathbf{x}-\mathbf{y}|)goes asexp⁡(−m​|𝐱−𝐲|)/|𝐱−𝐲|7/4\exp(-m|\mathbf{x}-\mathbf{y}|)/|\mathbf{x}-\mathbf{y}|^{7/4}.
As R. Haag (of Haag’s theorem fame) says on p. 33 of his monograph:Haag“for a massive particle the ambiguity in defining the localization is small, namely of the order of the Compton wavelength.”
As we will now see, small is quite different from zero. If
in Eq. (50) we
take|𝐤|≪m|\mathbf{k}|\ll m,
we can drop the𝐤2\mathbf{k}^{2}inside the square brackets,
so both integrals give aδ(3)​(𝐱−𝐲)\delta^{(3)}(\mathbf{x}-\mathbf{y}),
allowing us to carry out the integration over𝐲\mathbf{y}. Then,
the operatorϕ^L†​(𝐱)\hat{\phi}_{L}^{\dagger}(\mathbf{x})would be alocalfunction ofϕ^S​(𝐱)\hat{\phi}_{S}(\mathbf{x})andπ^S​(𝐱)\hat{\pi}_{S}(\mathbf{x}). Thus, non-relativisticallyϕ^L​(𝐱)\hat{\phi}_{L}(\mathbf{x})doescorrespond to a particle at a fixed position𝐱\mathbf{x}, but things
are different in the general case, where we care about Lorentz (rather
than Galilean) invariance.

Correction #4The quantum field corresponds
to a fixed position𝐱\mathbf{x}only in the non-relativistic problem. In the relativistic
case, one needs to introduce a Newton–Wigner position operator as well as
a new operatorϕL†​(𝐱)\phi_{L}^{\dagger}(\mathbf{x})creating particles at a fixed position𝐱\mathbf{x}, which does not coincide with the usual quantum fieldϕS​(𝐱)\phi_{S}(\mathbf{x}).

## III.5Wick’s theorem vs normal-ordering

In a typical textbook treatment, the tool of normal ordering
is first introduced when discussing the energy of the vacuum, for a non-interacting theory: a simple re-arrangement leads to the elimination of the zero-point motion.
Of course, interactions are (rightly) at the heart of any textbook treatment of
quantum field theory. The N-operation re-appears in that context, as part of
Wick’s theorem,
which re-expresses a T-product (needed for the Dyson expansion giving us the
S-matrix) as a sum of N-products. What’s often lost in this discussion is
whether we should be normal-ordering the entire Hamiltonian (and if not, why).
As part of the next mistake, we have therefore combined quotes from earlier and
later parts of a texbook (corresponding to non-interacting and interacting QFT,
respectively):

Mistake #5“Congratulations, you are now the proud owner of a working quantum field theory, provided you remember the normal ordering interpretation. […]
Wick’s theorem can be illustrated for the case of four operators […]
In particular⟨0|T​[ϕ^I​(x1)​ϕ^I​(x2)​ϕ^I​(x3)​ϕ^I​(x4)]|0⟩=ΔF​(x1−x2)​ΔF​(x3−x4)+ΔF​(x1−x3)​ΔF​(x2−x4)+ΔF​(x1−x4)​ΔF​(x2−x3)\langle 0|T[\hat{\phi}_{I}(x_{1})\hat{\phi}_{I}(x_{2})\hat{\phi}_{I}(x_{3})\hat{\phi}_{I}(x_{4})]|0\rangle=\Delta_{F}(x_{1}-x_{2})~\Delta_{F}(x_{3}-x_{4})+\Delta_{F}(x_{1}-x_{3})~\Delta_{F}(x_{2}-x_{4})+\Delta_{F}(x_{1}-x_{4})~\Delta_{F}(x_{2}-x_{3})(51)

where we have used the Feynman propagatorΔF​(x1−x2)=⟨0|T​[ϕ^I​(x1)​ϕ^I​(x2)]|0⟩\Delta_{F}(x_{1}-x_{2})=\langle 0|T[\hat{\phi}_{I}(x_{1})\hat{\phi}_{I}(x_{2})]|0\rangle.
[…]
Using Wick’s theorem on the string⟨0|a^​(𝐤)​ϕ^4​(x)​a^†​(𝐤)|0⟩=⟨0|a^​(𝐤)​ϕ^​(x)​ϕ^​(x)​ϕ^​(x)​ϕ^​(x)​a^†​(𝐤)|0⟩\langle 0|\hat{a}(\mathbf{k})\hat{\phi}^{4}(x)\hat{a}^{\dagger}(\mathbf{k})|0\rangle=\langle 0|\hat{a}(\mathbf{k})\hat{\phi}(x)\hat{\phi}(x)\hat{\phi}(x)\hat{\phi}(x)\hat{a}^{\dagger}(\mathbf{k})|0\rangle, will yield up two sorts of term.

There is much to unpack here. First, we are told that we need to normal-order
the Hamiltonian. Then, we see an application of Wick’s theorem, for a
case where the time-ordered product of quantum fields is evaluated at four different
positions. This is fine so far as it goes, but the next excerpt shows an
interaction of the typeϕ^4​(x)\hat{\phi}^{4}(x), which according to the previous
excerpt would lead to Feynman propagators evaluated at zero argumentΔF​(0)\Delta_{F}(0).
These diverge, but that’s not the main issue: the question is that
the toy application of Wick’s theorem is given fordifferentpositions, whereas
the actual interaction involves multiple quantum fields evaluated at thesameposition. These give rise to bubbles (also known as tadpoles):
unlike the Feynman diagrams of Fig.1, for bubbles
a single initial particle and a single final particle are associated
with a loop.

We noted above that normal-ordering a non-interacting Hamiltonian
eliminates the divergences associated with the
zero-point motion; normal-ordering the interaction only
eliminatessomedivergences. But there is a deeper reason
we should normal-order the interaction, one that is rarely
discussed in textbook treatments (p. 158 of Ref.Duncan,being one of
the very few exceptions): the interaction term in a Hamiltonianneedsto be normal-ordered if the cluster decomposition principle
(a pillar of the QFT edifice) is to be respected. In other words,
the string appearing in the last excerpt should, strictly speaking,
not be⟨0|a^​(𝐤)​ϕ^4​(x)​a^†​(𝐤)|0⟩\langle 0|\hat{a}(\mathbf{k})\hat{\phi}^{4}(x)\hat{a}^{\dagger}(\mathbf{k})|0\rangle, but⟨0|a^​(𝐤)​N​[ϕ^4​(x)]​a^†​(𝐤)|0⟩\langle 0|\hat{a}(\mathbf{k})N[\hat{\phi}^{4}(x)]\hat{a}^{\dagger}(\mathbf{k})|0\rangle.

As a perceptive reader may be deducing, we are going to need
a new version of Wick’s theorem for
what are known asmixedT-products, i.e., T-products which contain some (or all)
terms in normal-products, e.g.T​[A^​N​[B^​C^​D^]​E^​⋯​Z^]T[\hat{A}~N[\hat{B}\hat{C}\hat{D}]~\hat{E}\cdots\hat{Z}],
whereB^\hat{B},C^\hat{C}, andD^\hat{D}have the same time label.
As it so happens, G. Wick was well aware of this issue already when
proposing his (now) eponymous theorem:Wickhe put forward a “Theorem 2,” precisely to handle this situation.
Wick’s trick was to interpretT​[A^​N​[B^​C^​D^]​E^​⋯​Z^]T[\hat{A}~N[\hat{B}\hat{C}\hat{D}]~\hat{E}\cdots\hat{Z}]as the limit ofT​[A^​B^​C^​D^​E^​⋯​Z^]T[\hat{A}\hat{B}\hat{C}\hat{D}\hat{E}\cdots\hat{Z}]when the creation
operators amongB^\hat{B},C^\hat{C}, andD^\hat{D}have a time label that is infinitesimally later than
the time label of the annihilation operators amongB^\hat{B},C^\hat{C}, andD^\hat{D}.
Basically, he rewrote equal-time normal-ordered products in terms of unequal-time
non-normal-ordered products. This automatically implies that contractions between equal-time normal-ordered operators vanish,

This version of Wick’s theorem (sometimes calledWick’s corollary)
is most easily grasped via an example:T​[ϕ^I​(x)​N​[ϕ^I​(y)​ϕ^I​(y)]]\displaystyle T\left[\hat{\phi}_{I}(x)N\left[\hat{\phi}_{I}(y)\hat{\phi}_{I}(y)\right]\right]=N​[ϕ^I​(x)​ϕ^I​(y)​ϕ^I​(y)]+N​[​ϕ^I​(x)​ϕ^I​(y)​ϕ^I​(y)]+N​[​ϕ^I​(x)​ϕ^I​(y)​ϕ^I​(y)]\displaystyle=N\left[\hat{\phi}_{I}(x)\hat{\phi}_{I}(y)\hat{\phi}_{I}(y)\right]+N\left[\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 11.81842pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=23.41002pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.5pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 11.81842pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=23.41002pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.5pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 10.17885pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=20.24371pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 9.47401pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=18.88495pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{\phi}_{I}(x)\hat{\phi}_{I}(y)\hat{\phi}_{I}(y)\right]+N\left[\mathchoice{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 11.81842pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=46.5932pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.5pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 11.81842pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=46.5932pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.5pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 10.17885pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=40.37344pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}{\vbox{\hbox to0.0pt{\kern 0.0pt\kern 9.47401pt\hbox{\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt\vrule width=37.70682pt,height=0.0pt,depth=0.50003pt\vrule width=0.50003pt,height=0.0pt,depth=4.30554pt}\hss}\vskip 2.15277pt\vskip 7.22223pt}}\hat{\phi}_{I}(x)\hat{\phi}_{I}(y)\hat{\phi}_{I}(y)\right](52)

What this is showing is the application of
Wick’s theorem
to a mixed T-product of equal-time normal-ordered operators, with the crucial
proviso that contractions between factors that were already in normal product form (i.e., had the same time label) are being omitted
on the right-hand side: there is no contraction here
connectingyywithyy. Thisipso factoeliminates all bubbles from consideration. Intriguingly, the modified
version of Wick’s theorem was typically addressed in early standard
textbooks, e.g., see p. 184 of the classic work by Bjorken & Drell.Bjorken

Correction #5One must normal-order the interaction,
with a view to respecting the cluster decomposition
principle. In order to handle
normal-ordered interactions involving multiple quantum fields at the same position, one needs a modified version of Wick’s theorem, wherein contractions that
involve terms that were already normal-ordered are omitted. This eliminates
all bubbles.

## III.6Wick rotation

Given how much material needs to fit into a one-semester course on QFT,
students are sometimes disappointed to find out that all the machinery
on the S-matrix, Feynman diagrams, etc. doesn’t actually lead to any
practical conclusions until the following semester.
Regardless of when they are introduced, calculations like that leading
up to Eq. (25) are very important, because
they go beyond just writing down an integral and onto the question
of what the result actually is. A crucial step in that process
is the so-called “Wick rotation”; incidentally, this is a misnomer,
since F. Dyson introduced this idea years before G. Wick.Dyson;Wick2The specific argument involved will be discussed below, but qualitatively,
the main takeaway is that one can trade Minkowski 4-vectors for
Euclidean 4-vectors.

Mistake #6“By applying the Feynman parametrization, the integral becomesI=∫01𝑑x​∫d4​k(2​π)4​1[(l+p​x)2−Δ]2\displaystyle I=\int_{0}^{1}dx\int\frac{d^{4}k}{(2\pi)^{4}}\frac{1}{\left[(l+px)^{2}-\Delta\right]^{2}}(53)

whereΔ≡m2−x​(1−x)​l2\Delta\equiv m^{2}-x(1-x)l^{2}. By making the change of variablek=l+p​xk=l+pxand going to Euclidean space (k0=i​kE0k^{0}=ik^{0}_{E},𝐤=𝐤E\mathbf{k}=\mathbf{k}_{E}) we getI=i​∫01𝑑x​∫d4​kE(2​π)4​1(kE2+Δ)2I=i\int_{0}^{1}dx\int\frac{d^{4}k_{E}}{(2\pi)^{4}}\frac{1}{\left(k_{E}^{2}+\Delta\right)^{2}}(54)

”

There are two sub-fallacies here, both quite widespread. First,
we are told that the transition to Euclidean
space is a simplechange of variables:k0=i​kE0k^{0}=ik^{0}_{E},𝐤=𝐤E\mathbf{k}=\mathbf{k}_{E}. To see why this is wrong,
let us spell out the integration measure and the square of the Minkowski 4-vector
in the denominator of the integrand in Eq. (25):J​(l2)\displaystyle J(l^{2})=∫01𝑑x​∫d3​k(2​π)4​∫−∞+∞𝑑k0​1[(k0)2−𝐤2−Δ+i​ϵ]2\displaystyle=\int_{0}^{1}dx\int\frac{d^{3}k}{(2\pi)^{4}}\int_{-\infty}^{+\infty}dk^{0}\frac{1}{\left[(k^{0})^{2}-\mathbf{k}^{2}-\Delta+i\epsilon\right]^{2}}(55)

If we carried out the change of variablesk0=i​kE0k^{0}=ik^{0}_{E}here, the
denominator would look prettier, but the integration limits would not:
we would be stuck with imaginary integration limits,∫−i​∞+i​∞𝑑kE0\int_{-i\infty}^{+i\infty}dk_{E}^{0}. In other words, we’d have a nicely symmetric sum of two
positive terms in the denominator,(kE0)2+𝐤2(k_{E}^{0})^{2}+\mathbf{k}^{2}, but the integration
over𝐤\mathbf{k}would be in real space whereas that overkE0k_{E}^{0}would
be over imaginary values. Nothing gained.(a)(b)Figure 2:Contour of integration for Wick rotation, relevant to the2→22\rightarrow 2process of Fig.1for the cases of: (a)𝐤2+Δ>0\mathbf{k}^{2}+\Delta>0,
and (b)𝐤2+Δ<0\mathbf{k}^{2}+\Delta<0.

To make further progress, there is an extra idea needed here.
For concreteness, let us consider the case𝐤2+Δ>0\mathbf{k}^{2}+\Delta>0,
when our integrand has poles at±𝐤2+Δ∓i​ϵ\pm\sqrt{\mathbf{k}^{2}+\Delta}\mp i\epsilon.
The issue is that asϵ→0+\epsilon\rightarrow 0^{+}we get in trouble: the poles approach the contour
of integration (which here is the real line). Dyson’s insight was
to work on the complex-k0k^{0}plane and
to replace the contour
of integration by one which does not include the poles even whenϵ→0+\epsilon\rightarrow 0^{+}: this is precisely what is shown
in the left panel of Fig.2.
The contour does not contain any poles, so we can use Cauchy’s residue theorem
(splitting our curve into two simple closed curves).
Thus, this leads to:∫−∞+∞𝑑k0​1[(k0)2−𝐤2−Δ+i​ϵ]2=∫−i​∞+i​∞𝑑k0​1[(k0)2−𝐤2−Δ]2\int_{-\infty}^{+\infty}dk^{0}\frac{1}{\left[(k^{0})^{2}-\mathbf{k}^{2}-\Delta+i\epsilon\right]^{2}}=\int_{-i\infty}^{+i\infty}dk^{0}\frac{1}{\left[(k^{0})^{2}-\mathbf{k}^{2}-\Delta\right]^{2}}(56)

Observe that on the right-hand side our integral is over the imaginary axis and the
poles never approach the imaginary axis, so we can safely take
theϵ→0+\epsilon\rightarrow 0^{+}limit there.
This counter-clockwise rotation from the real axis to the imaginary axis is now
called aWick rotation. At this point (but not earlier!)
we can introduce the change of variablesk0≡i​kE0k^{0}\equiv ik_{E}^{0}in order to go back to the real axis:∫−i​∞+i​∞𝑑k0​1[(k0)2−𝐤2−Δ]2=i​∫−∞+∞𝑑kE0​1[−(kE0)2−𝐤2−Δ]2\int_{-i\infty}^{+i\infty}dk^{0}\frac{1}{\left[(k^{0})^{2}-\mathbf{k}^{2}-\Delta\right]^{2}}=i\int_{-\infty}^{+\infty}dk_{E}^{0}\frac{1}{\left[-(k_{E}^{0})^{2}-\mathbf{k}^{2}-\Delta\right]^{2}}(57)

We are gratified that we have been able to produce the nicely symmetric
term(kE0)2+𝐤2(k_{E}^{0})^{2}+\mathbf{k}^{2}, but also nice (real) integration limits.

We now turn to the second sub-fallacy in our quote: this revolves
around the absence of theϵ\epsilonin Eq. (53).
It is possible that𝐤2+Δ<0\mathbf{k}^{2}+\Delta<0, in which case
the poles±i​|𝐤2+Δ|∓ϵ\pm i\sqrt{|\mathbf{k}^{2}+\Delta|}\mp\epsilonare close to the imaginary axis, as illustrated in the right panel of Fig.2.
This means that, while we are free to carry out the same rotation
of the integration contour, we are not allowed to drop theϵ\epsilonon
the right-hand side like we did in Eq. (56).
This issue is related (yet distinct from) another
complication, also quite prevalent in QFT textbooks, namely that whenΔ<0\Delta<0dropping theϵ\epsilonleads to the logarithm of a negative number (not a pleasant sight). By keeping theϵ\epsilon, we can treat this as the natural logarithm of a complex number
and thereby follow the right branch, i.e.,ln⁡(x−i​ϵ)=ln⁡|x|−i​π\ln(x-i\epsilon)=\ln|x|-i\piforx<0x<0.

Correction #6Wick rotation is an idea put forward by Freeman Dyson in 1949 to simplify the evaluation of loop integrals, by rotating the contour counter-clockwise. It is not a simple change of variables. You can often drop the infinitesimal in the denominator after you’ve carried out the Wick rotation but, if you always do so, you will get in trouble (e.g., having to take the logarithm of a negative number).

## IVSummary and conclusion

In this article, we have discussed in some detail several
conceptual misunderstandings that arise in introductory textbook treatments
of quantum field theory. They range from themes relevant to classical field
theory (or relativistic QM), to the relationship between classical and
quantum field theory formulations, all the way to QFT proper. Some of them
can be grasped even by a beginner, while others require a bit of background
in order to be appreciated properly.
A unifying
thread is that these are all topics that a student cannot be reasonably
expected to figure out on their own, especially when the standard modern
textbook discussions are either silent or erroneous
on the conceptual core of each theme.

We now tentatively put forward some conjectures on
why these mistakes arose in the first place.
Some are the result of swiftly dispatching the subject’s
preliminaries (Mistake #1),
while others are the result of sloppiness (Mistake #6). At least one of them feels
like an individual author’s understandable discomfort getting the better of them
(Mistake #2), with the error later propagating through the literature. Most result
from not sticking to conceptual distinctions consistently (Mistakes #3 and #4)
or sometimes not taking the time to wonder why a given distinction should
be made in the first place (Mistake #5). Of course, the (hypothetical) history of these misconceptions is much less interesting than the task of eliminating them.

A common theme, visible in the references that we cited while
correcting each misconception, is that works that were published several decades ago are typically more careful than the textbooks currently used
to teach the subject.
Ours is not a treatise on sociology, but it is not unreasonable to propose that part of the problem comes from a culture valorizing novelty, often at the expense
of depth of understanding. More mundanely, some of the
pressure working against a profound understanding of the fundamentals of QFT
probably comes from the need to
cover new material without significantly increasing a textbook’s page count.
In the study of neural networks, one encounters
the concept of “catastrophic forgetting;” clearly, this is an idea that has
wider applicability. We hope that the present article, by going over some fairly subtle yet foundational
issues, will help instructors remember
(or even just learn) correct approaches to
these themes, thereby indirectly advancing the
quality of the education available to students of QFT.

## Acknowledgements.This work was supported by the Natural Sciences and
Engineering Research Council (NSERC) of Canada and the
Canada Foundation for Innovation (CFI).

## References
- (1)A. Gezerlis and M. Williams, “Six textbook mistakes in computational physics”, Am. J. Phys.89, 51-60, (2021).
- (2)A. Gezerlis and M. Williams, “Six textbook mistakes in data analysis”, Eur. Phys. J. Plus138, 19, (2023).
- (3)A. Gezerlis,Numerical Methods in Physics with Python, (Cambridge University Press, 2020).
- (4)A. Gezerlis,Numerical Methods in Physics with Python, 2nd ed. (Cambridge University Press, 2023).
- (5)A. Gezerlis,A Gentle Introduction to Quantum Field Theory(Cambridge University Press, 2026).
- (6)I. J. R. Aitchison and A. J. G. Hey,Gauge Theories in Particle Physics, Vol. I (Institute of Physics Publishing, 2003).
- (7)L. Álvarez–Gomé and M. Á. Vázquez-Mozo,An Invitation to Quantum Field Theory(Springer, 2012).
- (8)T. Banks,Modern Quantum Field Theory(Cambridge University Press, 2008).
- (9)L. Baulieu, J. Iliopoulos, and R. Sénéor,From Classical to Quantum Fields(Oxford University Press, 2017).
- (10)N. N. Bogoliubov and D. V. Shirkov,Introduction to the Theory of Quantized Fields(Interscience Publishers, 1959).
- (11)L. S. Brown,Quantum Field Theory(Cambridge University Press, 1992).
- (12)S. Coleman,Quantum Field Theory Lectures of Sidney Coleman(World Scientific, 2019).
- (13)A. Das,Lectures on Quantum Field Theory(World Scientific, 2008).
- (14)J. Donoghue and L. Sorbo,A Prelude to Quantum Field Theory(Princeton University Press, 2022).
- (15)G. P. Folland,Quantum Field Theory: a Tourist Guide for Mathematicians(American Mathematical Society, 2008).
- (16)E. Fradkin,Quantum Field Theory: an Integrated Approach(Princeton University Press, 2021).
- (17)F. Gelis,Quantum Field Theory: From Basics to Modern Topics(Cambridge University Press, 2019).
- (18)W. Greiner and J. Reinhardt,Field Quantization(Springer, 1996).
- (19)F. Gross,Relativistic Quantum Mechanics and Field Theory(Wiley, 2004).
- (20)B. Hatfield,Quantum Field Theory Of Point Particles And Strings(CRC Press, 1992).
- (21)C. Itzykson and J.-B. Zuber,Quantum Field Theory(McGraw-Hill, 1980).
- (22)H. Kleinert,Particles and Quantum Fields(World Scientific, 2016).
- (23)T. Lancaster and S. J. Blundell,Quantum Field Theory for the Gifted Amateur(Oxford University Press, 2014).
- (24)M. Maggiore,A Modern Introduction to Quantum Field Theory(Oxford University Press, 2005).
- (25)F. Mandl and G. Shaw,Quantum Field Theory, 2nd ed. (John Wiley & Sons, 2010).
- (26)H. Năstase,Introduction to Quantum Field Theory(Cambridge University Press, 2020).
- (27)T. Padmanabhan,Quantum Field Theory(Springer, 2016).
- (28)M. E. Peskin and D. V. Schroeder,An Introduction to Quantum Field Theory(CRC Press, 2018).
- (29)V. Radovanović,Problem Book in Quantum Field Theory, 2nd ed. (Springer, 2008).
- (30)P. Ramond,Field Theory: A Modern Primer, 2nd ed. (Westview Press, 1990).
- (31)L. H. Ryder,Quantum Field Theory, 2nd ed. (Cambridge University Press, 1996).
- (32)M. D. Schwartz,Quantum Field Theory and the Standard Model(Cambridge University Press, 2014).
- (33)M. Srednicki,Quantum Field Theory(Cambridge University Press, 2007).
- (34)M. Stone,The Physics of Quantum Fields(Springer, 2000).
- (35)M. Talagrand,What is a Quantum Field Theory?(Cambridge University Press, 2022).
- (36)A. Williams,Introduction to Quantum Field Theory(Cambridge University Press, 2023).
- (37)A. Zee,Quantum Field Theory in a Nutshell, 2nd ed. (Princeton University Press, 2010).
- (38)J. Zinn-Justin,Quantum Field Theory and Critical Phenomena, 5th ed. (Oxford University Press, 2021).
- (39)S. S. Schweber,An Introduction to Relativistic Quantum Field Theory(Harper & Row, 1961).
- (40)G. Sterman,An Introduction to Quantum Field Theory(Cambridge University Press, 1993).
- (41)P. T. Matthews and A. Salam, “The Renormalization of Meson Theories”, Rev. Mod. Phys.,23, 311 (1951).
- (42)P. Roman,Introduction to Quantum Field Theory(John Wiley & Sons, 1969).
- (43)S. Weinberg,The Quantum Theory of Fields, Vol. I: Foundations (Cambridge University Press, 1995).
- (44)R. Haag,Local Quantum Physics, 2nd ed. (Springer, 1996).
- (45)A. Duncan,The Conceptual Framework of Quantum Field Theory(Oxford University Press, 2012).
- (46)G. C. Wick “The Evaluation of the Collision Matrix”, Phys. Rev.,80, 268 (1950).
- (47)J. D. Bjorken and S. D. Drell,Relativistic Quantum Fields(McGraw-Hill, 1965).
- (48)F. J. Dyson, “TheSSMatrix in Quantum Electrodynamics”, Phys. Rev.,75, 1736 (1949).
- (49)G. C. Wick “Properties of Bethe–Salpeter Wave Functions”, Phys. Rev.,96, 1124 (1954).

## 


- 


Major funding support from
