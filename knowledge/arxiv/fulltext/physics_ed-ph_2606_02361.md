# Spin correlations in two-particle systems: a pedagogically motivated comparison of computational approaches

**arXiv ID**: 2606.02361v2
**Authors**: S. Martins-Filho
**Published**: 2026-06-01
**Categories**: physics.ed-ph, quant-ph
**Comments**: 12 pages, 3 figures, extended version of published in Rev. Bras. Ens. Fis
**DOI**: 10.1590/1806-9126-RBEF-2026-0134
**HTML URL**: https://arxiv.org/html/2606.02361v2

## Abstract

In this work we present a pedagogically motivated analysis of spin-correlation calculations in a quantum system composed of two spin-$1/2$ particles. Rather than aiming at new physical results, our purpose is to clarify and bring attention to different strategies for evaluating expectation values of the form $\langle ψ| S^{(1)}_{\hat{\boldsymbol{u}}} S^{(2)}_{\hat{\boldsymbol{v}}} | ψ\rangle$, which play an important role in discussions of entanglement and Bell-type correlations. We compare three complementary approaches. The first follows a direct algebraic evaluation in the product basis, closely related to standard textbook methods. The second uses a matrix representation of bipartite states, in which the tensor-product structure is expressed in terms of $2\times2$ complex matrices. This representation keeps the calculation close to the familiar Pauli-matrix algebra and makes the independent action of operators on each subsystem more transparent. The third explores a symmetry-based argument, highlighting both its usefulness and its limitations when applied beyond the singlet state. We show explicitly that the singlet state is rotationally invariant, which explains why the symmetry argument successfully reproduces its correlation function, while a naive extension fails for triplet states. The discussion illustrates how entanglement, tensor-product structure, and rotational symmetry interplay in spin correlations.

## Full Text

Spin correlations in two-particle systems: a pedagogically motivated comparison of computational approaches

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
- License: CC BY 4.0arXiv:2606.02361v2 [physics.ed-ph] 17 Jun 2026

## Spin correlations in two-particle systems:
a pedagogically motivated comparison of computational approachesS. Martins-Filhos.martins-filho@unesp.brInstituto de Física Teórica, Universidade Estadual Paulista (UNESP), Rua Dr. Bento Teobaldo Ferraz 271 - Bloco II, 01140-070 São Paulo, SP, Brazil

## Abstract

In this work we present a pedagogically motivated analysis of spin-correlation calculations in a quantum system composed of two spin-1/21/2particles. Rather than aiming at new physical results, our purpose is to clarify and bring attention to different strategies for evaluating expectation values of the form⟨ψ|S𝒖^(1)​S𝒗^(2)|ψ⟩\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{\psi}, which play an important role in discussions of entanglement and Bell-type correlations. We compare three complementary approaches. The first follows a direct algebraic evaluation in the product basis, closely related to standard textbook methods. The second uses a matrix representation of bipartite states, in which the tensor-product structure is expressed in terms of2×22\times 2complex matrices. This representation keeps the calculation close to the familiar Pauli-matrix algebra and makes the independent action of operators on each subsystem more transparent. The third explores a symmetry-based argument, highlighting both its usefulness and its limitations when applied beyond the singlet state. We show explicitly that the singlet state is rotationally invariant, which explains why the symmetry argument successfully reproduces its correlation function, while a naive extension fails for triplet states. The discussion illustrates how entanglement, tensor-product structure, and rotational symmetry interplay in spin correlations.Bipartite system, spin, quantum mechanics, representation theorem

## IIntroduction

The aim of this work is to present a pedagogically motivated discussion of
spin-correlation calculations in two-particle quantum systems, focusing on
methods suitable for advanced undergraduate or introductory graduate courses in
quantum mechanics. Rather than introducing new physical results, the goal is to
compare different derivational approaches and clarify their conceptual
structure, highlighting aspects that are often implicit in standard
presentations.

A recurring difficulty in the teaching of bipartite spin systems is that
students may be able to manipulate tensor-product expressions formally, while
still lacking a clear physical interpretation of the composite state space and
the associated correlations. In particular, the transition from single-particle
spin states to the tensor-product structure of two-particle systems is often
presented in an abstract way, which may obscure the connection between
algebraic expressions and measurable quantities.

In this work, we aim to bridge this gap by providing a unified discussion of
different computational strategies for evaluating expectation values of the
form⟨ψ|S𝒖^(1)​S𝒗^(2)|ψ⟩\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{\psi}, which arise naturally in
the analysis of spin correlations and Bell-type experiments. By presenting
multiple approaches within the same framework, we seek to make explicit the
relation between formal manipulations, geometric symmetry, and physical
interpretation.

We compare three complementary approaches. The first follows a direct
algebraic evaluation in the product basis, closely related to standard textbook
treatments (see, e.g., Refs.[1,2,3,4]). The
second is based on a representation in which bipartite states are written as2×22\times 2complex matrices. This choice is pedagogically useful because
students usually encounter spin-1/21/2first through the Pauli matrices, so the
calculation remains close to familiar2×22\times 2matrix operations instead of
immediately moving to a more cumbersome4×44\times 4matrix representation. The third
explores a symmetry-based argument inspired by Griffiths[5], highlighting both
its usefulness and its limitations when applied to the triplet sector.

The pedagogical value of the comparison is that each method emphasizes a
different aspect of the problem. The direct calculation keeps the connection
with the product basis explicit; the matrix representation makes the
subsystem structure more transparent; and the symmetry-based discussion
clarifies why rotational invariance is sufficient for the singlet but not for
the triplet sector. In particular, we analyze a common source of confusion:
the implicit assumption that symmetry arguments can be applied uniformly to
all total-spin states. By showing explicitly why this reasoning succeeds for
the singlet but fails for the triplet states, we provide a concrete example of
how symmetry considerations must be applied with care.

The target reader is an advanced undergraduate or beginning graduate student
who has already encountered Pauli matrices, Dirac notation, and the basic
postulates of quantum mechanics, but who may still be developing intuition for
composite Hilbert spaces and entangled spin states. The purpose of the
alternative derivations presented here is therefore not to replace standard
textbook methods, but to address specific difficulties that commonly arise at
this level: the interpretation of tensor-product states, the organization of
lengthy algebraic calculations, and the distinction between symmetry arguments
that rely on rotational invariance and those that do not.

This paper is organized as follows. In Sec.IIwe introduce the
bipartite spin-1/21/2system, establish the notation used throughout the paper,
and provide a physical motivation for the construction of the state space,
including its connection with spin-correlation experiments.
In Sec.III, we formulate the spin-correlation problem.
SectionIVpresents the product-basis calculation and
the matrix representation of bipartite states, allowing a direct comparison
between the two derivations. In Sec. V, we discuss the symmetry-based approach
and its limitations when applied beyond the singlet state. Finally,
Sec. VI summarizes the main results and discusses their pedagogical
implications.

## IIBipartite spin system

Before introducing the formal Hilbert-space description, it is interesting to recall the physical meaning of spin-1/21/2systems and the construction of bipartite states from a more intuitive perspective. A spin-1/21/2particle is characterized by the fact that any measurement of its spin component along a given direction yields only two possible outcomes,+ℏ/2+\hbar/2or−ℏ/2-\hbar/2(see Fig.1). These two outcomes are associated with the two eigenstates of the spin operator along the chosen axis. Thus, even before introducing matrices, the essential physical content is that a spin-1/21/2system behaves as a two-outcome quantum system for each chosen measurement direction.Figure 1:The spin-1/21/2degrees of freedom. For a measurement along thezzaxis, the possible outcomes are onlySz=+ℏ/2S_{z}=+\hbar/2andSz=−ℏ/2S_{z}=-\hbar/2. The arrows represent a visual aid and should not be interpreted as classical spin vectors.

In practice, such measurements can be realized, for example, with a Stern–Gerlach apparatus[6,7], which separates a beam of particles according to the value of the spin component along a chosen axis, as depicted in Fig.2. For readers interested in the historical impact of this experiment, see Ref.[8,9,10]. The quantum state does not assign a pre-existing classical direction to the spin; rather, it encodes the probability amplitudes associated with the possible measurement outcomes.Figure 2:Schematic representation of a Stern–Gerlach measurement for a
spin-1/21/2system.
The inhomogeneous magnetic field produced by the
magnet separates particles according to the measured value of the spin
component along a selected direction. In this
case, only two outcomes are possible,+ℏ/2+\hbar/2and−ℏ/2-\hbar/2, corresponding
respectively to spin “up” and spin “down” along the chosen axis.

When two spin-1/21/2particles are considered, the physical description must include all possible joint outcomes of measurements performed on the two particles. If the spin of each particle is measured along the same quantization axis, there are four possible joint results:(+,+),(+,−),(−,+),(−,−).(+,+),\quad(+,-),\quad(-,+),\quad(-,-).

These outcomes correspond respectively to the product states|+12⟩(1)​|+12⟩(2),|+12⟩(1)​|−12⟩(2),|−12⟩(1)​|+12⟩(2),|−12⟩(1)​|−12⟩(2);\begin{split}&\ket{+\frac{1}{2}}^{(1)}\ket{+\frac{1}{2}}^{(2)},\quad\ket{+\frac{1}{2}}^{(1)}\ket{-\frac{1}{2}}^{(2)},\\
&\ket{-\frac{1}{2}}^{(1)}\ket{+\frac{1}{2}}^{(2)},\quad\ket{-\frac{1}{2}}^{(1)}\ket{-\frac{1}{2}}^{(2)};\end{split}

where the superscripts(1)(1)and(2)(2)indicate the particle to which each state refers.
Thus, the tensor-product structureℋ⊗ℋ\mathcal{H}\otimes\mathcal{H}can be understood physically as the state space generated by all possible superpositions of joint measurement outcomes. In this sense, the tensor product is not only a formal mathematical construction, but also the natural way of describing the outcomes of measurements performed on a composite quantum system.

A particularly important feature of bipartite quantum systems is the existence
of entangled states, which cannot be written as a simple product of
single-particle states. In the two-spin system, examples of such states are
superpositions of the joint outcomes(+,−)(+,-)and(−,+)(-,+), in which the two
particles do not possess independently assigned spin values before measurement.
These states exhibit correlations that cannot be interpreted as a mere lack of
knowledge about pre-existing classical values.
The formal
examples of this idea, namely the singlet and triplet states, will be introduced
in the next subsection after the notation for the bipartite Hilbert space has
been established.

The central quantity studied in this work is the correlation functionB​[ψ]≡⟨ψ|S𝒖^(1)​S𝒗^(2)|ψ⟩,B\left[{\psi}\right]\equiv\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{\psi},(1)

where|ψ⟩∈ℋ⊗ℋ\ket{\psi}\in\mathcal{H}\otimes\mathcal{H}is a state of the
bipartite system. This quantity has a direct physical interpretation: it is the
average product of spin measurements performed on particles 1 and 2 along the
directions𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}}, respectively, when the system is
prepared in the state|ψ⟩\ket{\psi}.

In a Stern-Gerlach experiment, each individual measurement gives either+ℏ/2+\hbar/2or−ℏ/2-\hbar/2, and the correlation function measures how the two outcomes are statistically related when the experiment is repeated many times under the same preparation.
Such correlations are central in discussions of quantum entanglement and
Bell-type experiments[11,12]. Pedagogical discussions of Bell
inequalities and their conceptual implications can be found, for example, in
Refs.[13,14].

From a pedagogical perspective, a common difficulty for students is to interpret the tensor-product structure purely as an abstract construction, without connecting it to measurable quantities. By framing bipartite states in terms of joint measurement outcomes, the present discussion aims to make this connection explicit and to provide a more intuitive understanding of how spin correlations arise in composite systems. This perspective also helps clarify potential misconceptions, such as the improper extension of symmetry arguments to states that are not rotationally invariant.

This physical picture provides the basis for the formal developments presented in the following sections. The different computational approaches discussed below should therefore be understood not merely as algebraic alternatives, but as complementary ways of organizing the same physical information: the relation between the preparation of a two-particle spin state and the correlations observed in joint spin measurements.

## II.1Formal Hilbert space

To proceed, we establish the notation that will be used throughout the paper.
Let us denote, respectively,𝑺(1)\bm{S}^{(1)}and𝑺(2)\bm{S}^{(2)}as the spin operators of particles 1 and 2. Formally, the system spaceℋ^\hat{\mathcal{H}}is given by the tensor productℋ⊗ℋ\mathcal{H}\otimes\mathcal{H}, whereℋ\mathcal{H}is a two-dimensional complex Hilbert space[2,3,1]. Thus,𝑺(1)≡𝗦⊗𝟙\bm{S}^{(1)}\equiv\bm{\mathsf{S}}\otimes\mathds{1}and𝑺(2)≡𝟙⊗𝗦\bm{S}^{(2)}\equiv\mathds{1}\otimes\bm{\mathsf{S}}. Note that𝗦≡ℏ​𝝈/2\bm{\mathsf{S}}\equiv\hbar\bm{\sigma}/2is the well-known spin operator of a single spin-1/21/2particle, and𝝈\bm{\sigma}is the Pauli vector defined by the following components111The components are known as the Pauli matrices[4]. They are conveniently labeled by numbers since the Einstein summation convention will be used throughout.σ1=(0110),σ2=(0−ii0),andσ3=(100−1).\sigma_{1}=\begin{pmatrix}0&1\\
1&0\end{pmatrix},\quad\sigma_{2}=\begin{pmatrix}0&-i\\
i&0\end{pmatrix},\quad\textrm{and}\quad\sigma_{3}=\begin{pmatrix}1&0\\
0&-1\end{pmatrix}.(2)

In general, the operatorA(1)≡A⊗𝟙A^{(1)}\equiv A\otimes\mathds{1}whileA(2)≡𝟙⊗AA^{(2)}\equiv\mathds{1}\otimes A, whereAAbelongs to the set of all linear operators onℋ\mathcal{H}, denoted byℒ​(ℋ)\mathcal{L}(\mathcal{H}). Clearly, whenA∈ℒ​(ℋ)A\in\mathcal{L}(\mathcal{H}), the operatorA^≡A⊗A∈ℒ​(ℋ⊗ℋ)\hat{A}\equiv A\otimes A\in\mathcal{L}(\mathcal{H}\otimes\mathcal{H}).

The components of𝗦\bm{\mathsf{S}}satisfy the𝔰​𝔲​(2)\mathfrak{su}(2)algebra, that is,[15][𝖲j,𝖲k]=i​ℏ​ϵj​k​l​𝖲l,[{\mathsf{S}}_{j},\,{\mathsf{S}}_{k}]=i\hbar\epsilon_{jkl}{\mathsf{S}}_{l},(3)

where the Einstein summation convention, with indices running from11to33, is used and will be adopted throughout the text.

The eigenstates of𝖲z{\mathsf{S}}_{z}are|12⟩≡χ+=(10),and|−12⟩≡χ−=(01),\ket{\frac{1}{2}}\equiv\chi_{+}=\begin{pmatrix}1\\
0\end{pmatrix},\quad\text{and}\quad\ket{-\frac{1}{2}}\equiv\chi_{-}=\begin{pmatrix}0\\
1\end{pmatrix},(4)

with𝖲z​χ±=±ℏ2​χ±.{\mathsf{S}}_{z}\chi_{\pm}=\pm\frac{\hbar}{2}\chi_{\pm}.(5)

They form a basis forℋ\mathcal{H}, while their tensor products form a basis
forℋ^\hat{\mathcal{H}}, commonly referred to as theproduct basis.

Henceforth, we denote the total spin operator𝑺(1)+𝑺(2)\bm{S}^{(1)}+\bm{S}^{(2)}simply by𝑺\bm{S}. That is,𝑺≡𝑺(1)+𝑺(2)=ℏ2​(𝝈⊗𝟙+𝟙⊗𝝈).\bm{S}\equiv\bm{S}^{(1)}+\bm{S}^{(2)}=\frac{\hbar}{2}\left(\bm{\sigma}\otimes\mathds{1}+\mathds{1}\otimes\bm{\sigma}\right).(6)

We are particularly interested in the total-spin basis formed by the simultaneous eigenstates ofSz≡Sz(1)+Sz(2)S_{z}\equiv S_{z}^{(1)}+S_{z}^{(2)}and𝑺2\bm{S}^{2}. These eigenstates consist of the singlet|0⟩\ket{0}, with total spins=0s=0, and the triplet states|1,1⟩\ket{1,1},|1,0⟩\ket{1,0}, and|1,−1⟩\ket{1,-1}withs=1s=1. In this basis, the singlet satisfiesSz​|0⟩=S2​|0⟩=0​|0⟩,S_{z}\ket{0}=S^{2}\ket{0}=0\ket{0},(7)

while the triplet states satisfySz​|1,1⟩\displaystyle S_{z}\ket{1,1}=ℏ​|1,1⟩,\displaystyle=\hbar\ket{1,1},(8)Sz​|1,0⟩\displaystyle S_{z}\ket{1,0}=0​|1,0⟩,and\displaystyle=0\ket{1,0},\quad\textrm{and}(9)Sz​|1,−1⟩\displaystyle S_{z}\ket{1,-1}=−ℏ​|1,−1⟩.\displaystyle=-\hbar\ket{1,-1}.(10)

Thus, the possible measurement outcomes of the total spin componentSzS_{z}are+ℏ+\hbar,0, and−ℏ-\hbar, respectively.

If we generalize the notation such thatA⊗B≡A(1)​B(2)A\otimes B\equiv A^{(1)}B^{(2)}, the eigenstates in the standard basis can be written as|1,1⟩\displaystyle\ket{1,1}=χ+(1)​χ+(2),\displaystyle=\chi_{+}^{(1)}\chi_{+}^{(2)},(11a)|1,−1⟩\displaystyle\ket{1,-1}=χ−(1)​χ−(2),\displaystyle=\chi_{-}^{(1)}\chi_{-}^{(2)},(11b)|1,0⟩\displaystyle\ket{1,0}=χ+(1)​χ−(2)+χ−(1)​χ+(2)2,and\displaystyle=\frac{\chi_{+}^{(1)}\chi_{-}^{(2)}+\chi_{-}^{(1)}\chi_{+}^{(2)}}{\sqrt{2}},\quad\textrm{and}(11c)|0⟩\displaystyle\ket{0}=χ+(1)​χ−(2)−χ−(1)​χ+(2)2.\displaystyle=\frac{\chi_{+}^{(1)}\chi_{-}^{(2)}-\chi_{-}^{(1)}\chi_{+}^{(2)}}{\sqrt{2}}.(11d)

This notation is particularly convenient when decomposing operators into the
two independent sectors associated with particles 1 and 2. IfC^=A(1)​B(2)\hat{C}=A^{(1)}B^{(2)}, withC(1)=A⊗𝟙C^{(1)}=A\otimes\mathds{1}andA(2)=𝟙⊗BA^{(2)}=\mathds{1}\otimes B, then the two operators commute,[A(1),B(2)]=0,[A^{(1)},B^{(2)}]=0,(12)

(even when[A,B]≠0[A,B]\neq 0)
because they act on different factors of the tensor-product space. More
explicitly, for a product stateχα(1)​χβ(2)\chi_{\alpha}^{(1)}\chi_{\beta}^{(2)}, withα,β=±\alpha,\beta=\pm, one hasA(1)​B(2)​χα(1)​χβ(2)=(A​χα(1))​(B​χβ(2)).A^{(1)}B^{(2)}\chi_{\alpha}^{(1)}\chi_{\beta}^{(2)}=(A\chi_{\alpha}^{(1)})(B\chi_{\beta}^{(2)}).(13)

Thus, for example, the operatorC^\hat{C}acts on the singlet state asA(1)​B(2)​|0⟩=(A​χ+(1))​(B​χ−(2))−(A​χ−(1))​(B​χ+(2))2.A^{(1)}B^{(2)}\ket{0}=\frac{(A\chi_{+}^{(1)})(B\chi_{-}^{(2)})-(A\chi_{-}^{(1)})(B\chi_{+}^{(2)})}{\sqrt{2}}.(14)

## IIIStatement of the problem

Let us define the spin operator along the direction𝒖^\hat{\bm{u}}, denoted by𝖲𝒖^\mathsf{S}_{\hat{\bm{u}}}. We adopt spherical coordinates for convenience, see Fig.3.Figure 3:Geometrical representation of the measurement directions𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}}in a unit sphere (r2=1r^{2}=1) using spherical coordinates. The polar anglesθu\theta_{u}andθv\theta_{v}are measured from the positivezz-axis, while the azimuthal anglesφu\varphi_{u}andφv\varphi_{v}are measured in thex​yxy-plane from the positivexx-axis to the projections of𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}}, respectively.

The unit vector𝒖^\hat{\bm{u}}can be written ascos⁡(φu)​sin⁡(θu)​ı^+sin⁡(φu)​sin⁡(θu)​ȷ^+cos⁡(θu)​𝒌^,{\cos{\varphi_{u}}}{\sin{\theta_{u}}}\hat{\bm{\imath}}+{\sin{\varphi_{u}}}{\sin{\theta_{u}}}\hat{\bm{\jmath}}+{\cos{\theta_{u}}}\hat{\bm{k}},(15)

so that the spin operator along this direction assumes, in the usual basis, the form𝖲𝒖^=𝗦⋅𝒖^=ℏ2​(cos⁡θusin⁡θu​e−i​φusin⁡θu​ei​φu−cos⁡θu).\mathsf{S}_{\hat{\bm{u}}}=\bm{\mathsf{S}}\cdot\hat{\bm{u}}=\frac{\hbar}{2}\begin{pmatrix}\cos\theta_{u}&\sin\theta_{u}e^{-i\varphi_{u}}\\
\sin\theta_{u}e^{i\varphi_{u}}&-\cos\theta_{u}\end{pmatrix}.(16)

Our goal is to compare different approaches for evaluating the expectation value (1), whereS𝒖^(1)≡𝖲𝒖^⊗𝟙S^{(1)}_{\hat{\bm{u}}}\equiv\mathsf{S}_{\hat{\bm{u}}}\otimes\mathds{1}andS𝒗^(2)≡𝟙⊗𝖲𝒗^S^{(2)}_{\hat{\bm{v}}}\equiv\mathds{1}\otimes\mathsf{S}_{\hat{\bm{v}}}.
This requires computingB​[ψ]B[\psi]for the states of the total-spin basis. Such quantities naturally arise in spin–correlation measurements, including discussions of Bell-type inequalities.

## IVEvaluation of the spin correlationB​[ψ]B[\psi]

There are several ways to evaluateB​[ψ]B\left[{\psi}\right]shown in equation (1), reflecting different representations of the𝔰​𝔲​(2)⊗𝔰​𝔲​(2)\mathfrak{su}(2)\otimes\mathfrak{su}(2)algebra. In the following sections, we present some alternative procedures. We begin with a direct and effective, although not particularly concise, method for computingBB.

## IV.1Product-basis resolution

Rather than working in the standard basis, it is convenient to use the eigenvectors of the operatorsS𝒖^(1)S_{\hat{\bm{u}}}^{(1)}andS𝒗^(2)S_{\hat{\bm{v}}}^{(2)}.
Solving the eigenvalue problem associated with the matrix in equation (16) is straightforward. One finds thatχ+(𝒖^)=(cos⁡(θu2)ei​φu​sin⁡(θu2))andχ−(𝒖^)=(e−i​φu​sin⁡(θu2)−cos⁡(θu2))\chi^{(\hat{\bm{u}})}_{+}=\begin{pmatrix}\cos{\frac{\theta_{u}}{2}}\\
e^{i\varphi_{u}}\sin{\frac{\theta_{u}}{2}}\end{pmatrix}\quad\textrm{and}\quad\chi^{(\hat{\bm{u}})}_{-}=\begin{pmatrix}e^{-i\varphi_{u}}\sin{\frac{\theta_{u}}{2}}\\
-\cos{\frac{\theta_{u}}{2}}\end{pmatrix}(17)

are eigenvectors ofS𝒖^(1)S_{\hat{\bm{u}}}^{(1)}with eigenvalues+ℏ2+\frac{\hbar}{2}and−ℏ2-\frac{\hbar}{2}, respectively. SinceS𝒗^(2)S_{\hat{\bm{v}}}^{(2)}has the same structure asS𝒖^(1)S_{\hat{\bm{u}}}^{(1)}under the replacementu→vu\rightarrow v, the corresponding eigenvectors areχ+(𝒗^)=(cos⁡(θv2)ei​φv​sin⁡(θv2))andχ−(𝒗^)=(e−i​φv​sin⁡(θv2)−cos⁡(θv2)),\chi^{(\hat{\bm{v}})}_{+}=\begin{pmatrix}\cos{\frac{\theta_{v}}{2}}\\
e^{i\varphi_{v}}\sin{\frac{\theta_{v}}{2}}\end{pmatrix}\quad\textrm{and}\quad\chi^{(\hat{\bm{v}})}_{-}=\begin{pmatrix}e^{-i\varphi_{v}}\sin{\frac{\theta_{v}}{2}}\\
-\cos{\frac{\theta_{v}}{2}}\end{pmatrix},(18)

with identical eigenvalues.

The next step consists of constructing the eigenstates in this new basis. From equation. (17) and (18), we obtainχ+(1)\displaystyle\chi_{+}^{(1)}=χ+(𝒖^)​cos⁡(θu2)+χ−(𝒖^)​ei​φu​sin⁡(θu2),\displaystyle=\chi_{+}^{(\hat{\bm{u}})}\cos{\frac{\theta_{u}}{2}}+\chi_{-}^{(\hat{\bm{u}})}e^{i\varphi_{u}}\sin{\frac{\theta_{u}}{2}},(19a)χ+(2)\displaystyle\chi_{+}^{(2)}=χ+(𝒗^)​cos⁡(θv2)+χ−(𝒗^)​ei​φv​sin⁡(θv2),\displaystyle=\chi_{+}^{(\hat{\bm{v}})}\cos{\frac{\theta_{v}}{2}}+\chi_{-}^{(\hat{\bm{v}})}e^{i\varphi_{v}}\sin{\frac{\theta_{v}}{2}},(19b)χ−(1)\displaystyle\chi_{-}^{(1)}=χ+(𝒖^)​e−i​φu​sin⁡(θu2)−χ−(𝒖^)​cos⁡(θu2),and\displaystyle=\chi_{+}^{(\hat{\bm{u}})}e^{-i\varphi_{u}}\sin{\frac{\theta_{u}}{2}}-\chi_{-}^{(\hat{\bm{u}})}\cos{\frac{\theta_{u}}{2}},\quad\textrm{and}(19c)χ−(2)\displaystyle\chi_{-}^{(2)}=χ+(𝒗^)​e−i​φv​sin⁡(θv2)−χ−(𝒗^)​cos⁡(θv2).\displaystyle=\chi_{+}^{(\hat{\bm{v}})}e^{-i\varphi_{v}}\sin{\frac{\theta_{v}}{2}}-\chi_{-}^{(\hat{\bm{v}})}\cos{\frac{\theta_{v}}{2}}.(19d)

Substituting equation. (19) into the standard-basis eigenstates given in equation (11), we obtain that|0⟩=12(c11​χ+(𝒖^)​χ+(𝒗^)+c12​χ+(𝒖^)​χ−(𝒗^)−c¯12χ−(𝒖^)χ+(𝒗^)−c¯11χ−(𝒖^)χ−(𝒗^)),\begin{split}\ket{0}=\frac{1}{\sqrt{2}}\big(&c_{11}\chi^{(\hat{\bm{u}})}_{+}\chi^{(\hat{\bm{v}})}_{+}+c_{12}\chi^{(\hat{\bm{u}})}_{+}\chi^{(\hat{\bm{v}})}_{-}\\
&-\bar{c}_{12}\chi^{(\hat{\bm{u}})}_{-}\chi^{(\hat{\bm{v}})}_{+}-\bar{c}_{11}\chi^{(\hat{\bm{u}})}_{-}\chi^{(\hat{\bm{v}})}_{-}\big),\end{split}(20)

withc11\displaystyle c_{11}=e−i​φv​cos⁡(θu2)​sin⁡(θv2)−e−i​φu​sin⁡(θu2)​cos⁡(θv2),\displaystyle=e^{-i\varphi_{v}}\cos{\frac{\theta_{u}}{2}}\sin{\frac{\theta_{v}}{2}}-e^{-i\varphi_{u}}\sin{\frac{\theta_{u}}{2}}\cos{\frac{\theta_{v}}{2}},(21a)andc12\displaystyle c_{12}=−cos⁡(θu2)​cos⁡(θv2)−e−i​(φu−φv)​sin⁡(θu2)​sin⁡(θv2).\displaystyle=-\cos{\frac{\theta_{u}}{2}}\cos{\frac{\theta_{v}}{2}}-e^{-i(\varphi_{u}-\varphi_{v})}\sin{\frac{\theta_{u}}{2}}\sin{\frac{\theta_{v}}{2}}.(21b)

While the triplet is given by:|1,1⟩\displaystyle\ket{1,1}=c21​χ+(𝒖^)​χ+(𝒗^)+c22​χ+(𝒖^)​χ−(𝒗^)\displaystyle=c_{21}\chi^{(\hat{\bm{u}})}_{+}\chi^{(\hat{\bm{v}})}_{+}+c_{22}\chi^{(\hat{\bm{u}})}_{+}\chi^{(\hat{\bm{v}})}_{-}+c23​χ−(𝒖^)​χ+(𝒗^)+c24​χ−(𝒖^)​χ−(𝒗^),\displaystyle+{c}_{23}\chi^{(\hat{\bm{u}})}_{-}\chi^{(\hat{\bm{v}})}_{+}+{c}_{24}\chi^{(\hat{\bm{u}})}_{-}\chi^{(\hat{\bm{v}})}_{-},(22a)|1,−1⟩\displaystyle\ket{1,-1}=c¯24​χ+(𝒖^)​χ+(𝒗^)−c¯23​χ+(𝒖^)​χ−(𝒗^)\displaystyle=\bar{c}_{24}\chi^{(\hat{\bm{u}})}_{+}\chi^{(\hat{\bm{v}})}_{+}-\bar{c}_{23}\chi^{(\hat{\bm{u}})}_{+}\chi^{(\hat{\bm{v}})}_{-}−c¯22​χ−(𝒖^)​χ+(𝒗^)+c21​χ−(𝒖^)​χ−(𝒗^),and\displaystyle-\bar{c}_{22}\chi^{(\hat{\bm{u}})}_{-}\chi^{(\hat{\bm{v}})}_{+}+{c}_{21}\chi^{(\hat{\bm{u}})}_{-}\chi^{(\hat{\bm{v}})}_{-},\quad\text{and}(22b)|1,0⟩\displaystyle\ket{1,0}=c41​χ+(𝒖^)​χ+(𝒗^)+c42​χ+(𝒖^)​χ−(𝒗^)\displaystyle=c_{41}\chi^{(\hat{\bm{u}})}_{+}\chi^{(\hat{\bm{v}})}_{+}+c_{42}\chi^{(\hat{\bm{u}})}_{+}\chi^{(\hat{\bm{v}})}_{-}−c¯42​χ−(𝒖^)​χ+(𝒗^)−c¯41​χ−(𝒖^)​χ−(𝒗^);\displaystyle-\bar{c}_{42}\chi^{(\hat{\bm{u}})}_{-}\chi^{(\hat{\bm{v}})}_{+}-\bar{c}_{41}\chi^{(\hat{\bm{u}})}_{-}\chi^{(\hat{\bm{v}})}_{-};(22c)

wherec21=\displaystyle c_{21}={}cos⁡(θu2)​cos⁡(θv2),\displaystyle\cos{\frac{\theta_{u}}{2}}\cos{\frac{\theta_{v}}{2}},(23a)c22=\displaystyle c_{22}={}e−i​φv​cos⁡(θu2)​sin⁡(θv2),\displaystyle e^{-i\varphi_{v}}\cos{\frac{\theta_{u}}{2}}\sin{\frac{\theta_{v}}{2}},(23b)c23=\displaystyle c_{23}={}ei​φu​sin⁡(θu2)​cos⁡(θv2),\displaystyle e^{i\varphi_{u}}\sin{\frac{\theta_{u}}{2}}\cos{\frac{\theta_{v}}{2}},(23c)c24=\displaystyle c_{24}={}ei​(φu+φv)​sin⁡(θu2)​sin⁡(θv2);\displaystyle e^{i(\varphi_{u}+\varphi_{v})}\sin{\frac{\theta_{u}}{2}}\sin{\frac{\theta_{v}}{2}};(23d)c41=\displaystyle c_{41}={}e−i​φv​cos⁡(θu2)​sin⁡(θv2)+e−i​φu​sin⁡(θu2)​cos⁡(θv2),\displaystyle e^{-i\varphi_{v}}\cos{\frac{\theta_{u}}{2}}\sin{\frac{\theta_{v}}{2}}+e^{-i\varphi_{u}}\sin{\frac{\theta_{u}}{2}}\cos{\frac{\theta_{v}}{2}},(23e)c42=\displaystyle c_{42}={}−cos⁡(θu2)​cos⁡(θv2)+e−i​(φu−φv)​sin⁡(θu2)​sin⁡(θv2).\displaystyle-\cos{\frac{\theta_{u}}{2}}\cos{\frac{\theta_{v}}{2}}+e^{-i(\varphi_{u}-\varphi_{v})}\sin{\frac{\theta_{u}}{2}}\sin{\frac{\theta_{v}}{2}}.(23f)

The action ofS𝒖^(1)​S𝒗^(2)S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}on these eigenstates follows directly from equation. (13) (withA=B=𝖲A=B=\mathsf{S}). SinceS𝒖^(1)​χ±(𝒖^)=±ℏ2​χ±(𝒖^)andS𝒗^(2)​χ±(𝒗^)=±ℏ2​χ±(𝒗^),S^{(1)}_{\hat{\bm{u}}}\chi_{\pm}^{(\hat{\bm{u}})}=\pm\frac{\hbar}{2}\chi_{\pm}^{(\hat{\bm{u}})}\quad\textrm{and}\quad S^{(2)}_{\hat{\bm{v}}}\chi_{\pm}^{(\hat{\bm{v}})}=\pm\frac{\hbar}{2}\chi_{\pm}^{(\hat{\bm{v}})},(24)

it implies that⟨0|S𝒖^(1)​S𝒗^(2)|0⟩\displaystyle\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{0}=−ℏ24​cos⁡θ,\displaystyle=-\frac{\hbar^{2}}{4}\cos\theta,(25a)⟨1,0|S𝒖^(1)​S𝒗^(2)|1,0⟩\displaystyle\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{1,0}=ℏ24​[cos⁡(θ)−2​cos⁡(θu)​cos⁡(θv)],\displaystyle=\frac{\hbar^{2}}{4}[\cos{\theta}-2\cos{\theta_{u}}\cos{\theta_{v}}],(25b)⟨1,1|S𝒖^(1)​S𝒗^(2)|1,1⟩\displaystyle\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{1,1}=ℏ24​cos⁡θu​cos⁡θv,and\displaystyle=\frac{\hbar^{2}}{4}\cos\theta_{u}\cos\theta_{v},\quad\textrm{and}(25c)⟨1,−1|S𝒖^(1)​S𝒗^(2)|1,−1⟩\displaystyle\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{1,-1}=ℏ24​cos⁡θu​cos⁡θv;\displaystyle=\frac{\hbar^{2}}{4}\cos\theta_{u}\cos\theta_{v};(25d)

whereθ\thetais the angle between𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}}, such thatcos⁡θ\displaystyle\cos\theta=𝒖^⋅𝒗^\displaystyle=\hat{\bm{u}}\cdot\hat{\bm{v}}=cos⁡θu​cos⁡θv+sin⁡θu​sin⁡θv​cos⁡((φu−φv)).\displaystyle=\cos\theta_{u}\cos\theta_{v}+\sin\theta_{u}\sin\theta_{v}\cos{(\varphi_{u}-\varphi_{v})}.(26)

Since the four total-spin eigenstates form a complete basis ofℋ^\hat{\mathcal{H}}, their equal-weight sum corresponds to the maximally
mixed state𝟙/4\mathds{1}/4, on which the correlation vanishes
because each single-particle spin operator is traceless. Hence, for any
measurement directions𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}},B​[0]+B​[1,1]+B​[1,−1]+B​[1,0]=0,B[0]+B[1,1]+B[1,-1]+B[1,0]=0,(27)

which is satisfied by our results (25).
This provides a consistency check on the four correlation functions.

This approach provides a direct solution to the problem. All expectation values
are obtained explicitly, and the final expressions are compact. However, the
derivation itself is rather lengthy, especially forB​[0]B\left[{0}\right]andB​[1,0]B\left[1,0\right]. In these cases, several intermediate algebraic steps
are needed before the simple structure of the result becomes apparent. From a
pedagogical point of view, this is a limitation: the calculation is completely
correct, but the amount of algebra may obscure the tensor-product structure of
the problem and the physical origin of the correlations.

This motivates the search for a shorter and more organized derivation. The
purpose is not to replace the direct calculation, which remains useful as a
first explicit approach, but to complement it with a method that makes the
bipartite structure more transparent and reduces the possibility of algebraic
errors. This comparison also helps to identify which parts of the calculation
are essential to the physics and which are merely consequences of the chosen
representation.

## IV.2Matrix representation approach

As stated at the beginning of SectionIV, there are several ways to obtain the previous result. In this section we present a more concise method for evaluating the expression (1). The approach is based on a matrix representation of the tensor-product structure, allowing bipartite states to be expressed in terms of complex matrices.

Henceforth we denote a general spinor inℋ\mathcal{H}by|a⟩\ket{a}, whereaais any lowercase Latin letter, possibly primed when necessary. Its components are|a⟩1=a1\ket{a}_{1}=a_{1}and|a⟩2=a2\ket{a}_{2}=a_{2}. The composite state|a⟩⊗|b⟩∈ℋ^\ket{a}\otimes\ket{b}\in\mathcal{\hat{H}}will be referred to as apure c-state(where “c-state” stands for composite state). A linear superposition of pure c-states, such as the singlet, will be referred to as amixed c-state.

The c-state|a⟩⊗|b⟩\ket{a}\otimes\ket{b}is represented as the2×22\times 2complex matrixΣa​b=|a⟩​⟨b|∗,\Sigma^{ab}=\ket{a}\bra{b}^{*},(28)

whose elements in the standard basis are(Σa​b)=j​kajbk,withj,k∈{1,2}.(\Sigma^{ab}){}_{jk}=a_{j}b_{k},\quad\text{with }j\text{, }k\in\{1,\,2\}.(29)

Note thatA∗A^{*}denotes the complex conjugate of the matrixAA, whilea¯\bar{a}denotes the complex conjugate of the complex numberaa. In addition,A†A^{\dagger}denotes the Hermitian transpose ofAA.

It is important to distinguish the tensor product|a⟩⊗|b⟩\ket{a}\otimes\ket{b},
which defines a state in a composite Hilbert space, from the outer product|a⟩​⟨b|\ket{a}\bra{b}, which defines a linear operator acting on a single Hilbert space.
In the present work, we make use of an isomorphism that allows the tensor-product
structure to be represented in terms of2×22\times 2complex matrices,
thereby representing composite states by matrices with outer-product-like components.

The standard basis of the44-dimensional Hilbert spaceℋ^\mathcal{\hat{H}}defined through this product coincides with the standard basis of the vector spaceℂ2×2\mathbb{C}^{2\times 2}. From the definition (28) this can be verified directly:Σ++\displaystyle\Sigma^{++}=χ+​χ+𝖳=(1000),\displaystyle=\chi_{+}\chi_{+}^{\mathsf{T}}=\begin{pmatrix}1&0\\
0&0\end{pmatrix},(30a)Σ+−\displaystyle\Sigma^{+-}=χ+​χ−𝖳=(0100),\displaystyle=\chi_{+}\chi_{-}^{\mathsf{T}}=\begin{pmatrix}0&1\\
0&0\end{pmatrix},(30b)Σ−+\displaystyle\Sigma^{-+}=χ−​χ+𝖳=(0010),and\displaystyle=\chi_{-}\chi_{+}^{\mathsf{T}}=\begin{pmatrix}0&0\\
1&0\end{pmatrix},\quad\text{and}(30c)Σ−−\displaystyle\Sigma^{--}=χ−​χ−𝖳=(0001).\displaystyle=\chi_{-}\chi_{-}^{\mathsf{T}}=\begin{pmatrix}0&0\\
0&1\end{pmatrix}.(30d)

These matrices clearly form the standard basis ofℂ2×2\mathbb{C}^{2\times 2}. In fact, any basis ofℂ2×2\mathbb{C}^{2\times 2}also constitutes a basis for our four-dimensional Hilbert space. Therefore,ℋ^\mathcal{\hat{H}}is isomorphic toℂ2×2\mathbb{C}^{2\times 2}.

Before performing any calculations, it is useful to understand how operators act within this formulation. To this end, we recall the defining property of the tensor product. The operatorP⊗QP\otimes Qacts independently on a pure c-state|a⟩⊗|b⟩\ket{a}\otimes\ket{b}, namely(P⊗Q)​|a⟩⊗|b⟩=(P​|a⟩)⊗(Q​|b⟩).\left(P\otimes Q\right)\ket{a}\otimes\ket{b}=\left(P\ket{a}\right)\otimes\left(Q\ket{b}\right).(31)

We take this property as the starting point to define the action ofP⊗QP\otimes Qin the matrix representation. By bilinearity of the tensor product, this definition extends naturally to mixed c-states. Substituting equation (28) into equation (31) yields(P⊗Q)​Σa​b=P​Σa​b​Q𝖳,\left(P\otimes Q\right)\Sigma^{ab}=P\Sigma^{ab}Q^{\mathsf{T}},(32)

## Proof.

From equation (29), the right-hand side of equation (31) is a matrix whose elements are[(P|a⟩)⊗(Q|b⟩)]=j​k(P|a⟩)(Q|b⟩)j=kPj​lalQk​mbm.\left[\left(P\ket{a}\right)\otimes\left(Q\ket{b}\right)\right]{}_{jk}=(P\ket{a}){}_{j}(Q\ket{b}){}_{k}=P_{jl}a_{l}Q_{km}b_{m}.(33)

Rearranging this expression we obtainPj​lalbmQk​m=Pj​l(Σa​b)(Q𝖳)l​m=m​k(PΣa​bQ𝖳).j​k∎P_{jl}a_{l}b_{m}Q_{km}=P_{jl}(\Sigma^{ab}){}_{lm}(Q^{\mathsf{T}}){}_{mk}=(P\Sigma^{ab}Q^{\mathsf{T}}){}_{jk}.\qed(34)

The inner product between two pure c-states is defined as⟨Σa′​b′,Σa​b⟩≡Tr⁡[(Σa′​b′)†​Σa​b].\left\langle\Sigma^{a^{\prime}b^{\prime}},\Sigma^{ab}\right\rangle\equiv\Tr\!\left[(\Sigma^{a^{\prime}b^{\prime}})^{\dagger}\Sigma^{ab}\right].(35)

This definition extends straightforwardly to mixed c-states. When|a′⟩=|a⟩\ket{a^{\prime}}=\ket{a}and|b′⟩=|b⟩\ket{b^{\prime}}=\ket{b}, it reduces to the squared norm of|a⟩⊗|b⟩\ket{a}\otimes\ket{b}:‖|a⟩⊗|b⟩‖2≡Tr⁡[(Σa​b)†​Σa​b],\big\|\ket{a}\otimes\ket{b}\big\|^{2}\equiv\Tr\!\left[(\Sigma^{ab})^{\dagger}\Sigma^{ab}\right],(36)

which corresponds to the squared norm of the tensor product|a⟩⊗|b⟩\ket{a}\otimes\ket{b}in this matrix representation.

Taking into account the isomorphism mentioned above, this definition naturally suggests itself as the inner product inℋ^\mathcal{\hat{H}}. Indeed, it coincides with the standard inner product, as we show below.

## Proof.

The inner product inℋ^\mathcal{\hat{H}}is⟨|a′⟩⊗|b′⟩,|a⟩⊗|b⟩⟩≡⟨a′|a⟩​⟨b′|b⟩.\left<\ket*{a^{\prime}}\otimes\ket*{{b}{{}^{\prime}}},\,\ket{a}\otimes\ket{b}\right>\equiv\innerproduct*{a{{}^{\prime}}}{a}\innerproduct*{b^{\prime}}{b}.(37)

This agrees with⟨a′|⊗⟨b′|​(|a⟩⊗|b⟩)\displaystyle\bra*{a^{\prime}}\otimes\bra*{{b}{{}^{\prime}}}\big(\ket{a}\otimes\ket{b}\big)≡(|a′⟩⊗|b′⟩)†​(|a⟩⊗|b⟩)\displaystyle\equiv\big(\ket*{a^{\prime}}\otimes\ket*{{b}{{}^{\prime}}}\big)^{\dagger}\big(\ket{a}\otimes\ket{b}\big)=⟨a′|a⟩​⟨b′|b⟩.\displaystyle=\innerproduct*{a{{}^{\prime}}}{a}\innerproduct*{b^{\prime}}{b}.(38)

Using the definition of the trace we writeTr[(Σa′​b′)†Σa​b]=(Σa′​b′)j​i∗(Σa​b).j​i\Tr[(\Sigma^{a^{\prime}b^{\prime}})^{\dagger}\Sigma^{ab}]=(\Sigma^{a^{\prime}b^{\prime}})^{*}_{ji}(\Sigma^{ab}){}_{ji}.(39)

Substituting the matrix elements from equation (29) we obtainTr⁡[(Σa′​b′)†​Σa​b]\displaystyle\Tr[(\Sigma^{a^{\prime}b^{\prime}})^{\dagger}\Sigma^{ab}]=a′¯j​b′¯i​aj​bi\displaystyle=\bar{a^{\prime}}_{j}\bar{b^{\prime}}_{i}a_{j}b_{i}=a′¯j​aj​b′¯i​bi\displaystyle=\bar{a^{\prime}}_{j}a_{j}\bar{b^{\prime}}_{i}b_{i}=⟨a′|a⟩​⟨b′|b⟩.\displaystyle=\innerproduct*{a^{\prime}}{a}\innerproduct*{b^{\prime}}{b}.(40)

Therefore equation (35) is equivalent to the standard inner product ofℋ^\mathcal{\hat{H}}defined in equation (37).
∎

With equation (32) and the inner product (35) we are ready to address the problem. We start by using this formalism with the standard basis defined in equation (30). The eigenstates of the total-spin operator are|1,1⟩≡Σ+=Σ++,\displaystyle\ket{1,1}\equiv\Sigma^{+}=\Sigma^{++},(41a)|1,−1⟩≡Σ−=Σ−−,\displaystyle\ket{1,-1}\equiv\Sigma^{-}=\Sigma^{--},(41b)|1,0⟩≡Σ0¯=Σ+−+Σ−+2,and\displaystyle\ket{1,0}\equiv\Sigma^{\bar{0}}=\frac{\Sigma^{+-}+\Sigma^{-+}}{\sqrt{2}},\quad\text{and}(41c)|0⟩≡Σ0=Σ+−−Σ−+2.\displaystyle\ket{0}\equiv\Sigma^{0}=\frac{\Sigma^{+-}-\Sigma^{-+}}{\sqrt{2}}.(41d)

Explicitly,|1,±1⟩=12​[(1001)±(100−1)],|1,0⟩=12​(0110)and|0⟩=12​(01−10).\begin{split}&\ket{1,\pm 1}=\frac{1}{2}\left[\begin{pmatrix}1&0\\
0&1\end{pmatrix}\pm\begin{pmatrix}1&0\\
0&-1\end{pmatrix}\right],\\
&\ket{1,0}=\frac{1}{\sqrt{2}}\begin{pmatrix}0&1\\
1&0\end{pmatrix}\quad\text{and}\quad\ket{0}=\frac{1}{\sqrt{2}}\begin{pmatrix}0&1\\
-1&0\end{pmatrix}.\end{split}(42)

In the matrix representation, we immediately observe that2​|1,0⟩\sqrt{2}\ket{1,0}is represented byσ1\sigma_{1}. Similarly, depending on the
phase convention chosen for the singlet state,2​|0⟩\sqrt{2}\ket{0}is represented
by±i​σ2\pm i\sigma_{2}. With the convention used here, this gives2​|0⟩=i​σ2\sqrt{2}\ket{0}=i\sigma_{2}. This observation motivates the use of the basis{𝟙,𝝈}\{\mathds{1},\bm{\sigma}\}, which is particularly convenient because the
spin operators are proportional to the Pauli matrices. In this basis, the
states become|1,1⟩=𝟙+σ32,\displaystyle\ket{1,1}=\frac{\mathds{1}+\sigma_{3}}{2},(43a)|1,−1⟩=𝟙−σ32,\displaystyle\ket{1,-1}=\frac{\mathds{1}-\sigma_{3}}{2},(43b)|1,0⟩=σ12,and\displaystyle\ket{1,0}=\frac{\sigma_{1}}{\sqrt{2}},\quad\text{and}(43c)|0⟩=i​σ22.\displaystyle\ket{0}=i\frac{\sigma_{2}}{\sqrt{2}}.(43d)

Returning to the expectation value (1),B​[ψ]\displaystyle B\left[{\psi}\right]=⟨ψ|S𝒖^(1)​S𝒗^(2)|ψ⟩\displaystyle=\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{\psi}=uj​vk​⟨ψ|Sj(1)​Sk(2)|ψ⟩\displaystyle=u_{j}{v}_{k}\expectationvalue{S_{j}^{(1)}S_{k}^{(2)}}{\psi}=ℏ24​uj​vk​Kj​k​[ψ],\displaystyle=\frac{\hbar^{2}}{4}u_{j}{v}_{k}K_{jk}[\psi],(44)

we defineKj​k​[ψ]≡⟨ψ|σj(1)​σk(2)|ψ⟩.K_{jk}\left[{\psi}\right]\equiv\expectationvalue{\sigma_{j}^{(1)}\sigma_{k}^{(2)}}{\psi}.(45)

Using the inner product (35),Kj​k​[ψ]K_{jk}[\psi]can be expressed asTr⁡[(Σψ)​σj(1)†​σk(2)​Σψ],\Tr[(\Sigma^{\psi}){}^{\dagger}\sigma_{j}^{(1)}\sigma^{(2)}_{k}\Sigma^{\psi}],(46)

whereΣψ\Sigma^{\psi}is the matrix representing the c-stateψ\psi. Using equation (32), we obtainKj​k​[ψ]=Tr⁡[(Σψ)​σj†​Σψ​σk𝖳].K_{jk}\left[{\psi}\right]=\Tr[(\Sigma^{\psi}){}^{\dagger}\sigma_{j}\Sigma^{\psi}\sigma_{k}^{\mathsf{T}}].(47)

In general, for any operatorA⊗B∈ℒ​(ℋ^)A\otimes B\in\mathcal{L}(\mathcal{\hat{H}}), we have⟨ψ|A⊗B|ψ⟩=Tr⁡[(Σψ)​A†​Σψ​B𝖳].\expectationvalue{A\otimes B}{\psi}=\Tr[(\Sigma^{\psi}){}^{\dagger}A\Sigma^{\psi}B^{\mathsf{T}}].(48)

## IV.2.1Singlet

We start with the singlet state. Since we already know the answer, it is
straightforward to anticipate thatKKmust be equal to−δj​k-\delta_{jk}for the
singlet, that is, when|ψ⟩=|0⟩\ket{\psi}=\ket{0}. However, our interest here lies in
the method leading to this result. Once equation (47) has been obtained,
the calculation becomes almost immediate. Replacing|ψ⟩\ket{\psi}with the
singlet state we haveΣ0=i​σ2/2\Sigma^{0}=i\sigma_{2}/\sqrt{2}, so that
equation (47) becomes2​Kj​k​[0]=Tr⁡[σ2​σj​σ2​σk𝖳],2K_{jk}\left[{0}\right]=\Tr[\sigma_{2}\sigma_{j}\sigma_{2}\sigma_{k}^{\mathsf{T}}],(49)

where the Hermiticity of the Pauli matrices has been used.
We will also employ other well-known properties of the Pauli matrices.
For clarity, they are listed in the Appendix.

Let us begin withσ2​σj​σ2\sigma_{2}\sigma_{j}\sigma_{2}. Applying Property 2 several
times, we getσ2​σj​σ2\displaystyle\sigma_{2}\sigma_{j}\sigma_{2}=σ2​(δ2​j​𝟙+i​ϵj​2​l​σl)\displaystyle=\sigma_{2}(\delta_{2j}\mathds{1}+i\epsilon_{j2l}\sigma_{l})=σ2​δ2​j+i​ϵj​2​l​(δ2​l​𝟙+i​ϵ2​l​n​σn)\displaystyle=\sigma_{2}\delta_{2j}+i\epsilon_{j2l}(\delta_{2l}\mathds{1}+i\epsilon_{2ln}\sigma_{n})=σ2​δj​2+ϵj​2​l​ϵn​2​l​σn\displaystyle=\sigma_{2}\delta_{j2}+\epsilon_{j2l}\epsilon_{n2l}\sigma_{n}=σ2​δj​2+(δj​2​δ2​n−δ22​δj​n)​σn\displaystyle=\sigma_{2}\delta_{j2}+(\delta_{j2}\delta_{2n}-\delta_{22}\delta_{jn})\sigma_{n}=2​σ2​δj​2−σj,\displaystyle=2\sigma_{2}\delta_{j2}-\sigma_{j},(50)

where in the penultimate line we usedϵj​k​l​ϵm​n​l=δj​m​δk​n−δj​n​δk​m.\epsilon_{jkl}\epsilon_{mnl}=\delta_{jm}\delta_{kn}-\delta_{jn}\delta_{km}.(51)

We could substitute this result directly into equation (49), but
there is a more convenient way. Listing all cases of the last equality yieldsσ2​σj​σ2={σ2,if​j=2,−σj,if​j≠2,\sigma_{2}\sigma_{j}\sigma_{2}=\begin{cases}\sigma_{2},&\text{if }j=2,\\
-\sigma_{j},&\text{if }j\neq 2,\end{cases}(52)

which is equal to the transpose of−σj-\sigma_{j}(see Property 5), that is,σ2​σj​σ2=−σj𝖳.\sigma_{2}\sigma_{j}\sigma_{2}=-\sigma_{j}^{\mathsf{T}}.(53)

Combining this result with equation (49) we obtainTr⁡[σ2​σj​σ2​σk𝖳]=−Tr⁡[σj𝖳​σk𝖳]=−Tr⁡[σk​σj],\Tr[\sigma_{2}\sigma_{j}\sigma_{2}\sigma_{k}^{\mathsf{T}}]=-\Tr[\sigma_{j}^{\mathsf{T}}\sigma_{k}^{\mathsf{T}}]=-\Tr[\sigma_{k}\sigma_{j}],(54)

and using Property 2 once more we find−Tr⁡[σk​σj]=−Tr⁡[𝟙​δj​k+i​ϵk​j​l​σl]=−2​δj​k,-\Tr[\sigma_{k}\sigma_{j}]=-\Tr[\mathds{1}\delta_{jk}+i\epsilon_{kjl}\sigma_{l}]=-2\delta_{jk},(55)

since the Pauli matrices are traceless. Therefore,Kj​k​[0]=−δj​k.K_{jk}\left[{0}\right]=-\delta_{jk}.(56)

Substituting this result into equation (IV.2) we obtain the expectation
value for the singlet:B​[0]\displaystyle B\left[0\right]=ℏ24​uj​vk​⟨0|σj(1)​σk(2)|0⟩\displaystyle=\frac{\hbar^{2}}{4}u_{j}{v}_{k}\expectationvalue{\sigma_{j}^{(1)}\sigma_{k}^{(2)}}{0}=−ℏ24​uj​vk​δj​k\displaystyle=-\frac{\hbar^{2}}{4}u_{j}v_{k}\delta_{jk}=−ℏ24​𝒖^⋅𝒗^=−ℏ24​cos⁡(θ),\displaystyle=-\frac{\hbar^{2}}{4}\hat{\bm{u}}\cdot\hat{\bm{v}}=-\frac{\hbar^{2}}{4}\cos{\theta},(57)

which agrees with our earlier result  (25a).

Equation (55) shows that the Pauli matrices are orthogonal.
Denoting the identity matrix byσ0\sigma_{0}, that isσ0≡𝟙\sigma_{0}\equiv\mathds{1}, it is well known thatTr⁡[σα​σβ]=2​δα​β,\Tr[\sigma_{\alpha}\sigma_{\beta}]=2\delta_{\alpha\beta},(58)

where, as in General Relativity, the Greek indices run from0to33.
Therefore the basis{𝟙,𝝈}\{\mathds{1},\,\bm{\sigma}\}is orthogonal.

## IV.2.2Triplet

We now turn to the triplet states. We begin with|ψ⟩=|1,0⟩\ket{\psi}=\ket{1,0}, since it is similar to the singlet case. In this caseΣ0¯=σ1/2\Sigma^{\bar{0}}=\sigma_{1}/\sqrt{2}, hence2​Kj​k​[1,0]=Tr⁡[σ1​σj​σ1​σk𝖳].2K_{jk}\left[1,0\right]=\Tr[\sigma_{1}\sigma_{j}\sigma_{1}\sigma_{k}^{\mathsf{T}}].(59)

Following the same strategy as before, we first computeσ1​σj​σ1\sigma_{1}\sigma_{j}\sigma_{1}. One can easily verify thatσ1​σj​σ1=2​σ1​δj​1−σj,\sigma_{1}\sigma_{j}\sigma_{1}=2\sigma_{1}\delta_{j1}-\sigma_{j},(60)

which is analogous to equation (50), and its demonstration is
similar. A similar relation holds forσ3​σj​σ3\sigma_{3}\sigma_{j}\sigma_{3}after
replacing11with33.

Substituting equation (60) intoKKyields2​Kj​k​[1,0]=2​δj​1​Tr⁡[σ1​σk𝖳]−Tr⁡[σj​σk𝖳].2K_{jk}\left[1,0\right]=2\delta_{j1}\Tr[\sigma_{1}\sigma_{k}^{\mathsf{T}}]-\Tr[\sigma_{j}\sigma_{k}^{\mathsf{T}}].(61)

Sinceσ1\sigma_{1}is symmetric, the first term follows from the orthogonality
of the Pauli matrices,Tr⁡[σ1​σk]=2​δk​1\Tr[\sigma_{1}\sigma_{k}]=2\delta_{k1}, and therefore the first term equals4​δj​1​δk​14\delta_{j1}\delta_{k1}. For the second term we use Property 5,−Tr⁡[σj​σk𝖳]={2​δj​2,when​j=2;−2​δj​k,when​j≠2.-\Tr[\sigma_{j}\sigma_{k}^{\mathsf{T}}]=\begin{cases}2\delta_{j2},&\text{when }j=2;\\
-2\delta_{jk},&\text{when }j\neq 2.\end{cases}(62)

Thus,Kj​k​[1,0]=δj​1​δk​1+δj​2​δk​2−δj​3​δk​3.K_{jk}\left[1,0\right]=\delta_{j1}\delta_{k1}+\delta_{j2}\delta_{k2}-\delta_{j3}\delta_{k3}.(63)

Substituting this intoBB[see equation (IV.2)] givesB​[1,0]\displaystyle B\left[1,0\right]=ℏ24​uj​vk​(δj​1​δk​1+δj​2​δk​2−δj​3​δk​3)\displaystyle=\frac{\hbar^{2}}{4}u_{j}{v}_{k}\left(\delta_{j1}\delta_{k1}+\delta_{j2}\delta_{k2}-\delta_{j3}\delta_{k3}\right)=ℏ24​(u1​v1+u2​v2−u3​v3)\displaystyle=\frac{\hbar^{2}}{4}\left(u_{1}v_{1}+u_{2}v_{2}-u_{3}v_{3}\right)=ℏ24​(sin⁡θu​sin⁡θv​cos⁡((φu−φv))−cos⁡θu​cos⁡θv).\displaystyle=\frac{\hbar^{2}}{4}\left(\sin\theta_{u}\sin\theta_{v}\cos{(\varphi_{u}-\varphi_{v})}-\cos\theta_{u}\cos\theta_{v}\right).(64)

As expected, this agrees with the value obtained using the first approach shown in equation (25b) [in which, we have used equation (IV.1)].

We now proceed to the states|1,1⟩\ket{1,1}and|1,−1⟩\ket{1,-1}. We treat them
together by setting|ψ⟩=|1,±1⟩\ket{\psi}=\ket{1,\pm 1}and carrying the double signs
(±\pmand∓\mp) throughout the calculation. The matrices representing these states can be written compactly asΣ±=(𝟙±σ3)/2\Sigma^{\pm}=(\mathds{1}\pm\sigma_{3})/2. Thus,4​Kj​k​[1,±1]=Tr⁡[(𝟙±σ3)​σj​(𝟙±σ3)​σk𝖳].4K_{jk}[1,\pm 1]=\Tr[(\mathds{1}\pm\sigma_{3})\sigma_{j}(\mathds{1}\pm\sigma_{3})\sigma_{k}^{\mathsf{T}}].(65)

Following the previous procedure, we compute(𝟙±σ3)​σj​(𝟙±σ3)(\mathds{1}\pm\sigma_{3})\sigma_{j}(\mathds{1}\pm\sigma_{3})first. Using
Property 2 repeatedly, the expression reduces to a linear combination of{𝟙,𝝈}\{\mathds{1},\,\bm{\sigma}\}. In general, the product of Pauli matrices
(or any linear combination of them) remains an element of the linear spaceℂ2×2\mathbb{C}^{2\times 2}and can therefore be expressed in the basis{σα}\{\sigma_{\alpha}\}.

Thus,(𝟙±σ3)​σj​(𝟙±σ3)\displaystyle(\mathds{1}\pm\sigma_{3})\sigma_{j}(\mathds{1}\pm\sigma_{3})=(σj±σ3​σj)​(𝟙±σ3)\displaystyle=(\sigma_{j}\pm\sigma_{3}\sigma_{j})(\mathds{1}\pm\sigma_{3})=σj±σj​σ3±σ3​σj+σ3​σj​σ3\displaystyle=\sigma_{j}\pm\sigma_{j}\sigma_{3}\pm\sigma_{3}\sigma_{j}+\sigma_{3}\sigma_{j}\sigma_{3}=σj+σ3​σj​σ3±{σ3,σj}\displaystyle=\sigma_{j}+\sigma_{3}\sigma_{j}\sigma_{3}\pm\{\sigma_{3},\,\sigma_{j}\}=2​(σ3​δj​3±δ3​j​𝟙),\displaystyle=2(\sigma_{3}\delta_{j3}\pm\delta_{3j}\mathds{1}),(66)

where the anticommutator{σ3,σj}\{\sigma_{3},\,\sigma_{j}\}equals2​δj​3​𝟙2\delta_{j3}\mathds{1}andσ3​σj​σ3=2​σ3​δj​3−σj\sigma_{3}\sigma_{j}\sigma_{3}=2\sigma_{3}\delta_{j3}-\sigma_{j}.

Substituting equation (66) into equation (65) yields2​Kj​k​[1,±1]=δj​3​Tr⁡[σ3​σk𝖳]±Tr⁡[σk𝖳],2K_{jk}[1,\pm 1]=\delta_{j3}\Tr[\sigma_{3}\sigma_{k}^{\mathsf{T}}]\pm\Tr[\sigma_{k}^{\mathsf{T}}],(67)

and the second term vanishes because Pauli matrices are traceless. Using
equation (62) withj=3j=3, we obtainKj​k​[1,±1]=δj​3​δk​3.K_{jk}[1,\pm 1]=\delta_{j3}\delta_{k3}.(68)

Substituting this result into equation (IV.2) givesB​[1,±1]\displaystyle B[1,\pm 1]=ℏ24​uj​vk​δj​3​δk​3\displaystyle=\frac{\hbar^{2}}{4}u_{j}v_{k}\delta_{j3}\delta_{k3}=ℏ24​cos⁡(θu)​cos⁡(θv),\displaystyle=\frac{\hbar^{2}}{4}\cos{\theta_{u}}\cos{\theta_{v}},(69)

which coincides with the result obtained using the first approach equations (25c) and (25d).

This second approach is more formal than the product-basis calculation,
but it provides a clearer and more efficient route to the spin correlations.
Once its basic ingredients are established, in particular the action of
operators in equation (32) and the inner product in
Eq. (35), the evaluation of the correlation function becomes
considerably simpler. This is one of the main pedagogical advantages of the
method: it reorganizes the calculation in terms of familiar2×22\times 2matrix
operations, making the tensor-product structure of the bipartite system more
transparent and reducing the amount of algebra needed to reach the final
results.

In comparison with the direct approach, the matrix representation reduces the
amount of algebra required and avoids several trigonometric substitutions that
can obscure the physical meaning of the result. The required identities are
either standard consequences of the tensor-product structure or can be derived
in a few steps once a basis is chosen. Thus, while the method requires a short
preliminary discussion, it offers a more compact and conceptually organized
derivation of the correlation function.

## VSymmetry-based approach

The third approach is based on symmetry considerations. It is inspired by
the argument used by Griffiths in Problem 4.50 ofIntroduction to Quantum Mechanics[5], where the spin
correlation is evaluated for the singlet state.

The main idea is to exploit the freedom to choose convenient axes. For the
singlet, one may choose𝒖^\hat{\bm{u}}along𝒌^\hat{\bm{k}}, so thatS𝒖^=SzS_{\hat{\bm{u}}}=S_{z}, and take𝒗^\hat{\bm{v}}in thex​zxz-plane, namelyS𝒗^=sin⁡θ​Sx+cos⁡θ​Sz,S_{\hat{\bm{v}}}=\sin\theta\,S_{x}+\cos\theta\,S_{z},

whereθ\thetais the angle between𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}}. This procedure gives
the correct result for the singlet,B​[0]=−ℏ24​cos⁡θ.B[0]=-\frac{\hbar^{2}}{4}\cos\theta.

The reason is that the singlet is rotationally invariant. Therefore, rotating
the measurement directions does not change the state.

However, a common pitfall is to extend this same reasoning directly to the
triplet states. If one applies the same shortcut to the triplet sector, one
findsB​[1,±1]=−B​[1,0]=ℏ24​cos⁡θ.B[1,\pm 1]=-B\left[1,0\right]=\frac{\hbar^{2}}{4}\cos\theta.(70)

This result is rotationally invariant, since it depends only on the relative
angle between𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}}. It therefore disagrees with the results
obtained by the direct and matrix-based methods.

The failure of the naive symmetry argument can be seen already for the state|1,1⟩\ket{1,1}. The correct result isB​[1,1]=ℏ24​cos⁡θu​cos⁡θv.B[1,1]=\frac{\hbar^{2}}{4}\cos\theta_{u}\cos\theta_{v}.(71)

If one chooses𝒖^=𝒌^,𝒗^=sin⁡θ​ı^+cos⁡θ​𝒌^,\hat{\bm{u}}=\hat{\bm{k}},\qquad\hat{\bm{v}}=\sin\theta\,\hat{\bm{\imath}}+\cos\theta\,\hat{\bm{k}},

then equation (71) givesB​[1,1]=ℏ24​cos⁡θ.B[1,1]=\frac{\hbar^{2}}{4}\cos\theta.

A student might then incorrectly conclude that the triplet correlation depends
only on the relative angle between the two measurement directions. This is not
the case. Consider instead𝒖^=ı^,𝒗^=cos⁡θ​ı^+sin⁡θ​𝒌^.\hat{\bm{u}}=\hat{\bm{\imath}},\qquad\hat{\bm{v}}=\cos\theta\,\hat{\bm{\imath}}+\sin\theta\,\hat{\bm{k}}.

The relative angle between𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}}is againθ\theta, but nowcos⁡θu=0\cos\theta_{u}=0, and thereforeB​[1,1]=0.B[1,1]=0.

Thus, two configurations with the same relative angle lead to different
correlations. This counterexample shows where the naive symmetry reasoning
fails: it treats the triplet state as if it were rotationally invariant.

The origin of the disagreement is therefore not a failure of symmetry itself,
but an incomplete use of it. When the axes are rotated, the state must also be
transformed. For the singlet this point is hidden, because|0⟩\ket{0}is rotationally invariant. For triplet states, however, the state changes
under the same rotation. Thus, rotating the measurement directions while
keeping the triplet state fixed changes the physical problem.

Next, we will see that to apply the symmetry-based approach consistently, one must rotate both the
operators and the state. For the singlet,|ψ′⟩=|0⟩\ket{\psi^{\prime}}=\ket{0}, so the shortcut works immediately.
For triplet states,|ψ′⟩\ket{\psi^{\prime}}is generally a linear combination of triplet
states, and this transformation must be taken into account.

## V.1Extending the symmetry approach

It is not difficult to understand the origin of this disagreement. We restate
the argument in a clearer form. To choose the axes while keeping an equivalent
system, both subsystems must be rotated in the same way. Therefore, if we set𝒖^=𝒌^\hat{\bm{u}}=\hat{\bm{k}}and𝒗^=sin⁡θ​ı^+cos⁡θ​𝒌^\hat{\bm{v}}=\sin\theta\hat{\bm{\imath}}+\cos\theta\hat{\bm{k}},
we must find a unitary operatorUUsuch thatU​S𝒖^​U†=SzandU​S𝒗^​U†=cos⁡θ​Sz+sin⁡(θ)​Sx,US_{\hat{\bm{u}}}U^{\dagger}=S_{z}\quad\text{and}\quad US_{\hat{\bm{v}}}U^{\dagger}={\cos\theta}S_{z}+{\sin{\theta}}S_{x},(72)

that is,U^​S𝒖^⊗S𝒗^​U^†=Sz⊗(cos⁡θ​Sz+sin⁡(θ)​Sx)\hat{U}S_{\hat{\bm{u}}}\otimes S_{\hat{\bm{v}}}\hat{U}^{\dagger}=S_{z}\otimes\left({\cos\theta}S_{z}+{\sin{\theta}}S_{x}\right),
whereU∈S​U​(2)U\in SU(2). Since the operators transform in this manner while
the spin operators themselves remain unchanged, the basis must also transform.
A state|a⟩⊗|b⟩\ket{a}\otimes\ket{b}must transform as(|a⟩⊗|b⟩)′≡U^​|a⟩⊗|b⟩\left(\ket{a}\otimes\ket{b}\right)^{\prime}\equiv\hat{U}\ket{a}\otimes\ket{b}(remind thatU^=U⊗U\hat{U}=U\otimes U)
in order to preserve the inner product.

Hence the disagreement arises because we were not solving the same problem.
The obtained values are not the general quantityBB, but correspond to the
special caseθu=0\theta_{u}=0. Nevertheless, this approach gives the correct
result for the singlet. This immediately suggests the existence ofUUand
also indicates that the singlet is invariant under such rotations,
namelyU⊗U​|0⟩=|0⟩U\otimes U\ket{0}=\ket{0}.
Instead of proving invariance under a specificUU, we prove the stronger
statement that the singlet is rotationally invariant.

## Proof.

LetD=(D11D12D21D22),D=\begin{pmatrix}D_{11}&D_{12}\\
D_{21}&D_{22}\end{pmatrix},(73)

be an element ofS​L​(2,ℂ)SL(2,\mathbb{C}), the group of all2×22\times 2matrices
with unit determinant under matrix multiplication and inversion.
In physics,DDis usually taken to be unitary and therefore restricted to
the subgroupS​U​(2)SU(2).222SinceS​U​(2)SU(2)is a compact connected Lie group,
it represents spin rotations in quantum mechanics. (see Ref.[16,17]for a discussion of group theory.

Although it suffices to consider unitary transformations, this restriction
does not simplify the proof. The transformed basis vectors areD​χ+=(D11D21)andD​χ−=(D12D22),D\chi_{+}=\begin{pmatrix}D_{11}\\
D_{21}\end{pmatrix}\quad\text{and}\quad D\chi_{-}=\begin{pmatrix}D_{12}\\
D_{22}\end{pmatrix},(74)

and therefore2​|0⟩′=(D11D21)⊗(D12D22)−(D12D22)⊗(D11D21).\sqrt{2}\ket{0}^{\prime}=\begin{pmatrix}D_{11}\\
D_{21}\end{pmatrix}\otimes\begin{pmatrix}D_{12}\\
D_{22}\end{pmatrix}-\begin{pmatrix}D_{12}\\
D_{22}\end{pmatrix}\otimes\begin{pmatrix}D_{11}\\
D_{21}\end{pmatrix}.(75)

Using the matrix representation, we have(Σ0)′\displaystyle(\Sigma^{0})^{\prime}=12​(D11​D12−D12​D11D11​D22−D12​D21D21​D12−D22​D11D21​D22−D22​D21)\displaystyle=\frac{1}{\sqrt{2}}\begin{pmatrix}D_{11}D_{12}-D_{12}D_{11}&D_{11}D_{22}-D_{12}D_{21}\\
D_{21}D_{12}-D_{22}D_{11}&D_{21}D_{22}-D_{22}D_{21}\end{pmatrix}=det⁡(D)​Σ0.\displaystyle=\det(D)\Sigma^{0}.(76)

Sincedet⁡(D)=1\det(D)=1forS​L​(2,ℂ)SL(2,\mathbb{C}),(Σ0)′=Σ0⇔|0⟩′=|0⟩.(\Sigma^{0})^{\prime}=\Sigma^{0}\iff\ket{0}^{\prime}=\ket{0}.(77)

∎

This explains why the symmetry argument yields the correct value forB​[0]B[0]and whyB​[0]B[0]depends only on the angle between𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}}.

Repeating the same procedure for the triplet gives(Σ+)′=\displaystyle(\Sigma^{+})^{\prime}={}(D112D11​D21D11​D21D212)\displaystyle\begin{pmatrix}D_{11}^{2}&D_{11}D_{21}\\
D_{11}D_{21}&D_{21}^{2}\end{pmatrix}=\displaystyle={}D112​Σ++D11​D21​2​Σ0¯+D212​Σ−,\displaystyle D_{11}^{2}\Sigma^{+}+D_{11}D_{21}\sqrt{2}\Sigma^{\bar{0}}+D_{21}^{2}\Sigma^{-},(78a)(Σ−)′=\displaystyle(\Sigma^{-})^{\prime}={}(D122D12​D22D12​D22D222)\displaystyle\begin{pmatrix}D_{12}^{2}&D_{12}D_{22}\\
D_{12}D_{22}&D_{22}^{2}\end{pmatrix}=\displaystyle={}D222​Σ−+D12​D22​2​Σ0¯+D122​Σ+,\displaystyle D_{22}^{2}\Sigma^{-}+D_{12}D_{22}\sqrt{2}\Sigma^{\bar{0}}+D_{12}^{2}\Sigma^{+},(78b)(Σ0¯)′=\displaystyle(\Sigma^{\bar{0}})^{\prime}={}12​(D11​D12+D12​D11D11​D22+D12​D21D21​D12+D22​D11D21​D22+D22​D21)\displaystyle\frac{1}{\sqrt{2}}\begin{pmatrix}D_{11}D_{12}+D_{12}D_{11}&D_{11}D_{22}+D_{12}D_{21}\\
D_{21}D_{12}+D_{22}D_{11}&D_{21}D_{22}+D_{22}D_{21}\end{pmatrix}=\displaystyle={}2​D11​D12​Σ++(D11​D22+D12​D21)​Σ0¯\displaystyle\ \sqrt{2}D_{11}D_{12}\Sigma^{+}+(D_{11}D_{22}+D_{12}D_{21})\Sigma^{\bar{0}}+2​D21​D22​Σ−.\displaystyle+\sqrt{2}D_{21}D_{22}\Sigma^{-}.(78c)

These expressions show that the triplet is not rotationally invariant.
However, ifD=exp⁡(−i​φ​σ3/2)D=\exp(-i\varphi\sigma_{3}/2)represents a rotation
about thezz-axis, then|1,1⟩′\displaystyle\ket{1,1}^{\prime}=ei​φ​|1,1⟩,\displaystyle=e^{i\varphi}\ket{1,1},(79a)|1,−1⟩′\displaystyle\ket{1,-1}^{\prime}=e−i​φ​|1,−1⟩,\displaystyle=e^{-i\varphi}\ket{1,-1},(79b)|1,0⟩′\displaystyle\ket{1,0}^{\prime}=|1,0⟩.\displaystyle=\ket{1,0}.(79c)

Hence the triplet is physically invariant under rotations about thezz-axis. Since both|0⟩\ket{0}and|1,0⟩\ket{1,0}remain unchanged under
such rotations, any superposition of them is also invariant, whereas
superpositions of|1,1⟩\ket{1,1}and|1,−1⟩\ket{1,-1}generally acquire a physically
relevant relative phase.

We now determineUUsatisfying the condition (72).
Using the relationS​O​(3)≅S​U​(2)/Z2SO(3)\cong SU(2)/Z_{2}[17], we haveU​Sj​U†=𝒰j​k​SkUS_{j}U^{\dagger}=\mathcal{U}_{jk}S_{k}, where𝒰\mathcal{U}is anS​O​(3)SO(3)rotation matrix. LetD𝒘​(φ)=exp⁡(−i​φ​𝒘⋅S)D_{\bm{w}}(\varphi)=\exp(-i\varphi\bm{w}\cdot S)denote a spin rotation.
ThenD𝒘​(φ)​Sj​D𝒘†​(φ)=[R𝒘​(φ)]j​k​Sk,D_{\bm{w}}(\varphi)S_{j}D_{\bm{w}}^{\dagger}(\varphi)=\left[R_{\bm{w}}(\varphi)\right]_{jk}S_{k},(80)

whereR𝒘​(φ)R_{\bm{w}}(\varphi)is the correspondingS​O​(3)SO(3)rotation matrix.

ForUz​(φ)=exp⁡(−i​φ​σ3/2)U_{z}(\varphi)=\exp(-i\varphi\sigma_{3}/2),𝒰=Rz​(φ)=(cos⁡φsin⁡φ0−sin⁡φcos⁡φ0001),\mathcal{U}=R_{z}(\varphi)=\begin{pmatrix}\cos\varphi&\sin\varphi&0\\
-\sin\varphi&\cos\varphi&0\\
0&0&1\end{pmatrix},(81)

while forexp⁡(−i​φ​σ2/2)\exp(-i\varphi\sigma_{2}/2), we haveRy​(φ)=(cos⁡φ0−sin⁡φ010sin⁡φ0cos⁡φ).R_{y}(\varphi)=\begin{pmatrix}\cos\varphi&0&-\sin\varphi\\
0&1&0\\
\sin\varphi&0&\cos\varphi\end{pmatrix}.(82)

If a rotation𝒰\mathcal{U}exists such that𝒰​𝒖^=𝒌^,𝒰​𝒗^=cos⁡θ​𝒌^+sin⁡θ​ı^,\mathcal{U}\hat{\bm{u}}=\hat{\bm{k}},\qquad\mathcal{U}\hat{\bm{v}}=\cos\theta\,\hat{\bm{k}}+\sin\theta\,\hat{\bm{\imath}},(83)

then the correspondingUUexists. Such𝒰\mathcal{U}is obtained as a
composition of rotations. Using Euler angles,𝒰=Rz​(γ)​Ry​(β)​Rz​(α)\mathcal{U}=R_{z}(\gamma)R_{y}(\beta)R_{z}(\alpha), withα=φu\alpha=\varphi_{u},β=θu\beta=\theta_{u}, andtan⁡γ=ℐ/ℛ\tan\gamma=\mathcal{I}/\mathcal{R}, whereℛ\displaystyle\mathcal{R}=cos⁡θu​sin⁡θv​cos⁡(φv−φu)−sin⁡θu​cos⁡θv,\displaystyle=\cos\theta_{u}\sin\theta_{v}\cos(\varphi_{v}-\varphi_{u})-\sin\theta_{u}\cos\theta_{v},(84)ℐ\displaystyle\mathcal{I}=sin⁡θv​sin⁡(φv−φu).\displaystyle=\sin\theta_{v}\sin(\varphi_{v}-\varphi_{u}).(85)

The useful relations areℛ=cos⁡γ​sin⁡θandℐ=sin⁡γ​sin⁡θ,\displaystyle\mathcal{R}=\cos\gamma\sin\theta\quad\text{and}\quad\mathcal{I}=\sin\gamma\sin\theta,(86)

implyingsin⁡θ=ℛ2+ℐ2\sin\theta=\sqrt{\mathcal{R}^{2}+\mathcal{I}^{2}}.

HenceRz​(γ)=csc⁡θ​(ℛℐ0−ℐℛ000sin⁡θ),R_{z}(\gamma)=\csc\theta\begin{pmatrix}\mathcal{R}&\mathcal{I}&0\\
-\mathcal{I}&\mathcal{R}&0\\
0&0&\sin\theta\end{pmatrix},(87)

andU=Dz​(γ)​Dy​(θu)​Dz​(φu).U=D_{z}(\gamma)D_{y}(\theta_{u})D_{z}(\varphi_{u}).(88)

The singlet is the only invariant eigenstate,|0⟩′=|0⟩,\ket{0}^{\prime}=\ket{0},(89)

while the triplet transforms as|1,1⟩′\displaystyle\ket{1,1}^{\prime}=U112​|1,1⟩+U11​U21​2​|1,0⟩+U212​|1,−1⟩,\displaystyle=U_{11}^{2}\ket{1,1}+U_{11}U_{21}\sqrt{2}\ket{1,0}+U_{21}^{2}\ket{1,-1},(90a)|1,−1⟩′\displaystyle\ket{1,-1}^{\prime}=U222​|1,−1⟩+U12​U22​2​|1,0⟩+U122​|1,1⟩,\displaystyle=U_{22}^{2}\ket{1,-1}+U_{12}U_{22}\sqrt{2}\ket{1,0}+U_{12}^{2}\ket{1,1},(90b)|1,0⟩′\displaystyle\ket{1,0}^{\prime}=2​U11​U12​|1,1⟩+(U11​U22+U12​U21)​|1,0⟩\displaystyle=\sqrt{2}U_{11}U_{12}\ket{1,1}+(U_{11}U_{22}+U_{12}U_{21})\ket{1,0}+2​U21​U22​|1,−1⟩.\displaystyle\quad+\sqrt{2}U_{21}U_{22}\ket{1,-1}.(90c)

This explains why the symmetry approach fails for the triplet but succeeds
for the singlet.

Moreover, for a general state|ψ⟩\ket{\psi}, we haveB​[ψ]\displaystyle B[\psi]=⟨ψ|S𝒖^(1)​S𝒗^(2)|ψ⟩\displaystyle=\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{\psi}=⟨ψ′|Sz(1)​(sin⁡θ​Sx(2)+cos⁡θ​Sz(2))|ψ′⟩,\displaystyle=\expectationvalue{S_{z}^{(1)}\left(\sin\theta S_{x}^{(2)}+\cos\theta S_{z}^{(2)}\right)}{\psi^{\prime}},(91)

where|ψ′⟩=U^​|ψ⟩\ket{\psi^{\prime}}=\hat{U}\ket{\psi}. Since|ψ⟩\ket{\psi}can be decomposed in the eigenstate basis333For a normalized state|c0|2+|c0¯|2+|c−|2+|c+|2=1|c_{0}|^{2}+|c_{\bar{0}}|^{2}+|c_{-}|^{2}+|c_{+}|^{2}=1.|ψ⟩=c0​|0⟩+c0¯​|1,0⟩+c−​|1,−1⟩+c+​|1,1⟩,\ket{\psi}=c_{0}|0\rangle+c_{\bar{0}}|1,0\rangle+c_{-}|1,-1\rangle+c_{+}|1,1\rangle,(92)

its transformation follows as|ψ′⟩=c0​|0⟩+c0¯​|1,0⟩′+c−​|1,−1⟩′+c+​|1,1⟩′,\ket{\psi^{\prime}}=c_{0}|0\rangle+c_{\bar{0}}|1,0\rangle^{\prime}+c_{-}|1,-1\rangle^{\prime}+c_{+}|1,1\rangle^{\prime},(93)

where the primed states are shown in equation (90).

A limited use of symmetry is still possible in the triplet sector. Consider,
for example, the states|1,±1⟩\ket{1,\pm 1}and the special case in which one of
the measurement directions is thezz-axis,B𝒌^,𝒗^​[1,±1]=⟨1,±1|S𝒌(1)​S𝒗^(2)|1,±1⟩.B_{\hat{\bm{k}},\hat{\bm{v}}}[1,\pm 1]=\expectationvalue{S^{(1)}_{\bm{k}}S^{(2)}_{\hat{\bm{v}}}}{1,\pm 1}.(94)

WritingS𝒗^(2)=sin⁡θv​cos⁡φv​Sx(2)+sin⁡θv​sin⁡φv​Sy(2)+cos⁡θv​Sz(2),S^{(2)}_{\hat{\bm{v}}}=\sin\theta_{v}\cos\varphi_{v}\,S_{x}^{(2)}+\sin\theta_{v}\sin\varphi_{v}\,S_{y}^{(2)}+\cos\theta_{v}\,S_{z}^{(2)},(95)

one may use the fact that|1,±1⟩\ket{1,\pm 1}are eigenstates of the totalSzS_{z}operator. Under a rotation around thezz-axis, these states acquire
only an overall phase [see equation (79)], which cancels in the expectation value. Therefore, one may choose the azimuthal angle of𝒗^\hat{\bm{v}}to be zero444This is possible by choosingUz=exp⁡(i​φv​σ3/2)U_{z}=\exp(i\varphi_{v}\sigma_{3}/2), which corresponds to a rotation of angle−φv-\varphi_{v}around thezz-axis., so thatS𝒗^(2)⟶sin⁡θv​Sx(2)+cos⁡θv​Sz(2).S^{(2)}_{\hat{\bm{v}}}\longrightarrow\sin\theta_{v}\,S_{x}^{(2)}+\cos\theta_{v}\,S_{z}^{(2)}.(96)

Thus,B𝒌^,𝒗^​[1,±1]\displaystyle B_{\hat{\bm{k}},\hat{\bm{v}}}[1,\pm 1]=⟨1,±1|Sz(1)​(sin⁡θv​Sx(2)+cos⁡θv​Sz(2))|1,±1⟩\displaystyle=\expectationvalue{S_{z}^{(1)}\left(\sin\theta_{v}\,S_{x}^{(2)}+\cos\theta_{v}\,S_{z}^{(2)}\right)}{1,\pm 1}=ℏ24​cos⁡θv.\displaystyle=\frac{\hbar^{2}}{4}\cos\theta_{v}.(97)

This agrees with Eqs. (25c) and (25d) forθu=0\theta_{u}=0, namely𝒖^=𝒌^\hat{\bm{u}}=\hat{\bm{k}}.

It is important, however, that this is only a special use of symmetry. It works
because|1,±1⟩\ket{1,\pm 1}transform by an overall phase under rotations around
thezz-axis [see equation (79)]. For a superposition such as|1,1⟩+|1,−1⟩\ket{1,1}+\ket{1,-1}, the two components acquire different phases under the
same rotation. The relative phase of the state is therefore changed, and the
above simplification can no longer be applied without also transforming the
state explicitly.

This shows that extending Griffiths’s approach to other states requires transforming it according to equation (93), so thatBBremains invariant under the transformation ofS𝒖^S_{\hat{\bm{u}}}andS𝒗^S_{\hat{\bm{v}}}, as in equation (91).

## VIConclusion

In this work we presented a pedagogical discussion of spin correlations in a
two–particle spin-1/21/2quantum system, emphasizing different strategies for
evaluating expectation values of the form⟨ψ|S𝒖^(1)​S𝒗^(2)|ψ⟩\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{\psi}.
Rather than introducing new physical results, the objective was to compare
distinct derivational approaches and clarify their conceptual content.

The direct calculation in the product basis provides an explicit and accessible
procedure, although it may become algebraically lengthy. The formulation based
on a matrix representation of bipartite states leads to a more concise
treatment and makes transparent the independent action of operators on each
subsystem. In contrast, the symmetry argument inspired by Griffiths,
while successful for the singlet state, was shown to fail when naively extended
to the triplet sector. This difference was traced to the rotational invariance
of the singlet state and to the transformation properties of the triplet
states under spin rotations.

From a pedagogical perspective, the comparison between these approaches helps
to connect algebraic manipulation, geometric symmetry, and physical
interpretation. In particular, the analysis clarifies a common source of
difficulty for students: the implicit assumption that symmetry arguments
apply equally to all states. By exhibiting explicitly the failure of this
reasoning in the triplet sector, the discussion highlights the importance of
distinguishing between transformations of measurement axes and transformations
of the quantum state.

Moreover, the matrix-based representation provides a more transparent view of
the tensor-product structure, allowing the calculation to be organized in terms
of independent contributions from each subsystem. This can be especially useful
for students encountering bipartite systems for the first time, as it reduces
the reliance on lengthy algebraic manipulations and makes the structure of
entangled states more explicit.

Finally, the quantities studied here have a direct experimental interpretation.
The expectation value⟨ψ|S𝒖^(1)​S𝒗^(2)|ψ⟩\expectationvalue{S^{(1)}_{\hat{\bm{u}}}S^{(2)}_{\hat{\bm{v}}}}{\psi}corresponds
to the average product of spin measurements performed along directions𝒖^\hat{\bm{u}}and𝒗^\hat{\bm{v}}, as in Stern–Gerlach or Bell-type experiments. In this
sense, the different methods discussed in this work not only provide alternative
computational tools, but also offer complementary perspectives that connect
formal calculations with physically measurable correlations.

We hope that the discussion presented here may serve as a complementary resource
for undergraduate and introductory graduate courses in quantum mechanics,
especially in topics related to spin systems[2,5], quantum entanglement[1,4], and Bell-type correlations[11,12].

The third method is particularly effective for the singlet, although less
useful for the triplet due to its reduced symmetry. For the singlet, it combines
simplicity and conciseness and therefore provides a useful introduction for
undergraduate students to the EPR paradox and Bell’s inequalities, especially
in connection with Bell’s original work[11]. In this respect,
the pedagogical presentation in Ref.[18]is also especially useful,
as it emphasizes the conceptual content of Bell-type correlations with minimal
formal machinery.

## Acknowledgements.The author thanks Gastão Krein for his encouragement, which motivated the completion of this work.
The author also thanks Prof. Jeferson L. Tomazelli for useful comments and helpful suggestions.
S. M.-F. thanks FAPESP for partial financial support. This study was financed, in part, by the São Paulo Research Foundation (FAPESP), Brasil. Process Number #2025/16156-7.

## Appendix APauli Matrices

Here we will list some of the properties of the Pauli matrices[2,4]. These
well-known properties were used extensively in this work, but specially in the
SectionIV.2:
- Property 1.

Hermiticity:σj†=σj\sigma_{j}^{\dagger}=\sigma_{j}.
- Property 2.

Pauli algebra:σj​σk=𝟙​δj​k+i​ϵj​k​l​σl\sigma_{j}\sigma_{k}=\mathds{1}\delta_{jk}+i\epsilon_{jkl}\sigma_{l}.
- Property 3.

Involution:σj2=𝟙\sigma_{j}^{2}=\mathds{1}.
- Property 4.

Tracelessness:Tr⁡[σj]=0\Tr[\sigma_{j}]=0.
- Property 5.

Transposition:σj𝖳={−σ2,if​j=2,+σj,if​j≠2.\sigma_{j}^{\mathsf{T}}=\begin{cases}-\sigma_{2},&\text{if }j=2,\\
+\sigma_{j},&\text{if }j\neq 2.\end{cases}

## References
- [1]M. A. Nielsen and I. L. Chuang,Quantum Computation and Quantum Information(Cambridge University Press, Cambridge, 2010).
- [2]J. J. Sakurai and J. Napolitano,Modern Quantum Mechanics,
2nd ed. (Cambridge University Press, Cambridge, 2017).
- [3]C. Cohen-Tannoudji, B. Diu, and F. Laloë,Quantum Mechanics, Vols. 1 and 2
(Wiley, New York, 1977).
- [4]L. E. Ballentine,Quantum Mechanics: A Modern Development(World Scientific, Singapore, 1998).
- [5]D. J. Griffiths,Introduction to Quantum Mechanics,
2nd ed. (Pearson Prentice Hall, Upper Saddle River, NJ, 2005).
- [6]O. Stern,Zeitschrift für Physik7(1), 249 (1921).
- [7]W. Gerlach and O. Stern,Annalen der Physik379, 673 (1924).
- [8]Friedel Weinert,Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics26, 75 (1995).
- [9]G. G. Gomes and M. Pietrocola,Rev. Bras. Ens. Fís.33(2), 2604 (2011)[in portuguese].
- [10]R. Grossi,
Lucas L. Brugger,
B.F. Rizzuti,
C. Duarte;Rev. Bras. Ens. Fis.45, e20220227 (2023).
- [11]J. S. Bell,Physics Physique Fizika1, 195 (1964).
- [12]J. F. Clauser and A. Shimony,Rep. Prog. Phys.41, 1881 (1978).
- [13]R. R. Machado and C. E. Aguiar,Rev. Bras. Ens. Fis.45, e20220324 (2023).
- [14]G. B. Pimentel, L. A. M. Souza, R. Rossi Jr. and B. Amaral,Rev. Bras. Ens. Fis.47(3), e20250442 (2025).
- [15]A. R. Edmonds,Angular Momentum in Quantum Mechanics(Princeton University Press, Princeton, NJ, 1996).
- [16]M. Nakahara,Geometry, Topology and Physics,
2nd ed. (CRC Press, Boca Raton, FL, 2003).
- [17]H. Georgi,Lie Algebras in Particle Physics,
2nd ed. (Westview Press, Boulder, CO, 1999).
- [18]N. D. Mermin,Am. J. Phys.58, 731 (1990).

## 


- 


Major funding support from
