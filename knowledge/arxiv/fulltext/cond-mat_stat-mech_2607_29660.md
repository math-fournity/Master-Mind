# A Simple Necessary and Sufficient Condition for Yang--Baxter Integrability

**arXiv ID**: 2607.29660v1
**Authors**: Mizuki Sanatani, Naoto Shiraishi, Fuga Ishii
**Published**: 2026-07-31
**Categories**: cond-mat.stat-mech, hep-th, math-ph, nlin.SI, quant-ph
**Comments**: 11 pages, 4 figures, 1 table; Supplemental Material included (23 pages). Code available at https://github.com/sanatanim/reshetikhin and archived at https://doi.org/10.5281/zenodo.21721878
**HTML URL**: https://arxiv.org/html/2607.29660v1

## Abstract

Quantum integrability is a cornerstone of the exact theory of interacting quantum spin chains. In its standard formulation, however, one starts from R-matrices satisfying the Yang--Baxter equation, rather than from the Hamiltonian itself. It has therefore remained unclear how Yang--Baxter solvability can be characterized directly at the Hamiltonian level, and how it is related to the existence of local conservation laws. Here we prove that, in a broad standard setting, the Reshetikhin condition is not only necessary but also sufficient for Yang--Baxter integrability, thereby reducing the hidden algebraic structure of integrability to a Hamiltonian-level conservation law. Since the Reshetikhin condition is equivalent to conservation of the total energy current, this Hamiltonian-level criterion is also experimentally accessible. This result establishes a quantum counterpart of the Liouville--Arnold theorem for isotropic spin chains, stating that Yang--Baxter solvability is equivalent to an infinite hierarchy of local conserved quantities. Our result also simplifies substantially the search for integrable spin chains by replacing the search for R-matrices with a direct criterion on local Hamiltonians.

## Full Text

A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability

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
- License: arXiv.org perpetual non-exclusive licensearXiv:2607.29660v1 [cond-mat.stat-mech] 31 Jul 2026

## A Simple Necessary and Sufficient Condition for Yang–Baxter IntegrabilityMizuki Sanataniyamaguchi-q@g.ecc.u-tokyo.ac.jpGraduate School of Arts and Sciences, The University of Tokyo, 3-8-1 Komaba, Meguro, Tokyo 153-8902, JapanNaoto Shiraishishiraishi@phys.c.u-tokyo.ac.jpGraduate School of Arts and Sciences, The University of Tokyo, 3-8-1 Komaba, Meguro, Tokyo 153-8902, JapanFuga Ishiifuga@i-shi-i.nameCollege of Arts and Sciences, The University of Tokyo, 3-8-1 Komaba, Meguro, Tokyo 153-8902, Japan

## Abstract

Quantum integrability is a cornerstone of the exact theory of interacting quantum spin chains.
In its standard formulation, however, one starts from R-matrices satisfying the Yang–Baxter equation, rather than from the Hamiltonian itself.
It has therefore remained unclear how Yang–Baxter solvability can be characterized directly at the Hamiltonian level, and how it is related to the existence of local conservation laws.
Here we prove that, in a broad standard setting, the Reshetikhin condition is not only necessary but also sufficient for Yang–Baxter integrability, thereby reducing the hidden algebraic structure of integrability to a Hamiltonian-level conservation law.
Since the Reshetikhin condition is equivalent to conservation of the total energy current, this Hamiltonian-level criterion is also experimentally accessible.
This result establishes a quantum counterpart of the Liouville–Arnold theorem for isotropic spin chains, stating that Yang–Baxter solvability is equivalent to an infinite hierarchy of local conserved quantities.
Our result also simplifies substantially the search for integrable spin chains by replacing the search for R-matrices with a direct criterion on local Hamiltonians.

Quantum integrability provides a privileged arena in which we can analytically probe quantum many-body systems.
In one-dimensional quantum spin chains, it allows us to obtain exact results for spectra, eigenstates, correlation functions, transport and thermodynamics[5,36,54,3,4,46].
These results make integrable models a testing ground where general ideas in condensed-matter and statistical physics can be examined directly from exact solutions.
Integrable spin chains therefore serve as reference points in quantum many-body physics, where exact analytical results are otherwise difficult to obtain.

The standard route to quantum integrability starts from anRR-matrix and an auxiliary system[47,45,48,49,18].
In the Yang–Baxter framework, theRR-matrix satisfies the Yang–Baxter equation, which ensures the consistent factorization of many-body processes into two-body ones.
From such anRR-matrix, one constructs a commuting family of transfer matrices whose logarithmic derivatives generate local conserved quantities.
The Hamiltonian is then identified with the two-local quantity.
In this sense, the Hamiltonian appears only at the end of the construction, rather than serving as its starting point.
Other quantities including the spectra, eigenstates, thermodynamic properties and correlation functions are subsequently derived by exploiting this commuting transfer-matrix structure.
This construction is powerful because it provides a systematic route from an algebraic equation to exact solvability.
Consequently, research on quantum integrability has historically focused on findingRR-matrices satisfying the Yang–Baxter equation and on computing physical quantities using the Yang–Baxter structure.

ThisRR-matrix-first programme has been remarkably successful in constructing and solving integrable models, yet it also leaves several structural questions about integrability largely unresolved.
One central open problem concerns the relation between Yang–Baxter solvability and local conserved quantities.
In classical Hamiltonian mechanics, integrability is characterized by the existence of a sufficient number of independent commuting conserved quantities (first integrals), as formulated in the Liouville–Arnold theorem.
In quantum spin chains, however, whether the presence of a local integrable hierarchy implies Yang–Baxter solvability has been left unsolved.
To the best of our knowledge, all known examples exhibit these two structures together[20,40,22,52,53,44], but no general principle explaining this coincidence has been established.
Determining whether this connection is universal is fundamental, because it bears directly on what quantum integrability means.

Another limitation is the lack of a direct criterion for integrability at the level of the Hamiltonian.
A quantum spin chain is usually specified by its local Hamiltonian, rather than by anRR-matrix, whereas the Yang–Baxter construction starts from theRR-matrix and obtains the Hamiltonian only as its derivative.
In this sense, the standard framework explains how to derive Hamiltonians fromRR-matrices, but does not directly address the inverse problem: given a local Hamiltonian, how can one decide whether it originates from a Yang–Baxter structure?
In practice, establishing integrability requires finding a suitableRR-matrix, a nontrivial task that often demands considerable ingenuity[21,24,35,7,8,9,6,19,50,17,16,14,15,34].
This makes it difficult to determine Yang–Baxter solvability directly from the Hamiltonian itself.

Faced with this limitation, researchers treating quantum integrable systems have used theReshetikhin conditionas a practical, albeit incomplete, test of integrability[31].
The Reshetikhin condition is the lowest-order nontrivial constraint obtained by expanding the Yang–Baxter equation around a regular point, which is written solely in terms of the local Hamiltonian density.
In many spin-chain settings, this condition is identified with the conservation of the total energy current[57,30].
Of course, a priori the Reshetikhin condition is only a necessary condition of Yang–Baxter integrability.
Namely, a Hamiltonian could satisfy the Reshetikhin condition and nevertheless fail to admit anRR-matrix satisfying the Yang–Baxter equation, because the Yang–Baxter equation imposes infinitely many higher-order constraints in the same expansion.
However, surprisingly, all previously studied Hamiltonians satisfying the Reshetikhin condition have ultimately turned out to be Yang–Baxter integrable[25,21,29,2,24,35,7,8,9,6,50,43,17,16,14,15,34,40,22,52,53,44].
This striking coincidence led to the conjecture raised by several research groups in the early 1980s asserting that the Reshetikhin condition is also a sufficient condition for Yang–Baxter solvability[31,37,25].
Despite its conceptual importance, practical success, and repeated refrain in various papers[20,14,13,56], this ambitious conjecture has remained open for more than forty years.

Here we show that this long-standing expectation is correct.
For quantum spin chains with translation-invariant nearest-neighbour interactions, we rigorously prove that the Reshetikhin condition is not only necessary but also sufficient for Yang–Baxter integrability.
More precisely, whenever a local Hamiltonian satisfies the
Reshetikhin condition, one can always construct a regular analytic solution of the
difference-form Yang–Baxter equation order by order in the
spectral parameter.
Thus the infinitely many higher-order constraints of the Yang–Baxter equation collapse to its lowest nontrivial Hamiltonian-level condition.
This rigidity also offers a structural explanation for why the Yang–Baxter equation occupies such a privileged position in one-dimensional quantum integrability.

This result has profound implications in several directions.
First, our result substantially simplifies the search for new integrable models.
Conventionally, such searches have often required finding a suitableRR-matrix in the large space of possibleRR-matrices[32].
Usually, this is a difficult task, since theRR-matrix contains much more information than the local Hamiltonian itself.
Our theorem allows us instead to search directly in the space of local Hamiltonians, using the Reshetikhin condition as a complete Hamiltonian-level criterion for Yang–Baxter integrability.
In addition, the result suggests a possible experimental implication: conservation of the total energy current provides a direct signature of Yang–Baxter solvability, which can be probed in the laboratory.
This reveals the striking fact that the highly mathematical property of exact solvability can be diagnosed through the experimental measurement of a single physical observable.
Moreover, our result opens a programme towards identifying a universal class of local algebras whose Baxterization yields solutions of the Yang–Baxter equation.
Since the only Hamiltonian-level restriction is the Reshetikhin condition, the problem reduces to classifying algebraic relations consistent with this condition.
This provides an inverse perspective on the conventional Baxterization approach[26,27,1,9].

Our result also refines the notion of quantum integrability, by establishing a quantum analogue of the Liouville–Arnold theorem for isotropic spin chains: Yang–Baxter solvability is equivalent to the existence of an infinite family of local conserved quantities.
It thus closes the gap between the presence of local conservation laws and exact solvability in the quantum setting.
Even in general quantum spin chains, we can show a Liouville–Arnold-type connection that Yang–Baxter solvability is equivalent to the existence of an infinite family of local conserved quantities generated by the boost operator.

(a)

(b)Figure 1:Reversing the search for Yang–Baxter integrability.a,In the established algebraic framework, one starts from anRR-matrix satisfying the Yang–Baxter equation and constructs the transfer matrixT​(u)T(u).
This construction provides a mutually commuting family of local quantitiesQ2,Q3,Q4,…Q_{2},Q_{3},Q_{4},\ldots, together with access to spectra, eigenstates, correlation functions, transport coefficients and thermodynamics.
The Hamiltonian appears in this construction as the first nontrivial charge in the hierarchy,H=Q2H=Q_{2}.b,In the conventional search picture, the integrable locus is identified by solving the Yang–Baxter equation in the space ofRR-matrices, and Hamiltonian densities are then obtained by projecting these solutions down to Hamiltonian space.
The search is therefore indirect and inefficient for discovering integrable Hamiltonians.
The present work reverses this direction: the integrable locus is identified directly in Hamiltonian space by the Reshetikhin condition, and the correspondingRR-matrix is reconstructed afterwards.

## The Yang–Baxter equation and integrability

We consider a translation-invariant nearest-neighbour quantum spin chain of lengthLLwith periodic boundary conditions,H=∑i=1Lhi,i+1H=\sum_{i=1}^{L}h_{i,i+1}, where siteL+1L+1is identified with site 1.
We say that this Hamiltonian is Yang–Baxter integrable if, at the end of the following procedure, one obtains this Hamiltonian.
Suppose that there exists a regular spectral-parameter-dependentRR-matrixRi​j​(u)R_{ij}(u)on two sitesiiandjjsatisfying the following difference-formYang–Baxter equationR12​(u)​R13​(u+v)​R23​(v)=R23​(v)​R13​(u+v)​R12​(u)R_{12}(u)R_{13}(u+v)R_{23}(v)=R_{23}(v)R_{13}(u+v)R_{12}(u)(1)

in a neighborhood of(u,v)=(0,0)(u,v)=(0,0), together with the regularity conditionR​(0)=ΠR(0)=\Pi, whereΠ\Piis the two-site permutation operator.
Throughout this article, unless otherwise explicitly stated, the Yang–Baxter equation is understood in difference form, and allRR-matrices are assumed to be regular.
Introducing an auxiliary siteaa, we define the transfer matrixT​(u):=Tra​[∏i=1LRa​i​(u)]T(u):=\mathrm{Tr}_{a}[\prod_{i=1}^{L}R_{ai}(u)].
The Yang–Baxter equation implies the commutativity of transfer matrices at different spectral parameters, which confirms that their logarithmic derivatives generate a hierarchy of commuting local quantities:Qn=dn−1d​un−1​ln⁡T​(u)|u=0.Q_{n}=\left.\frac{d^{n-1}}{du^{n-1}}\ln T(u)\right|_{u=0}.(2)

Here, eachQnQ_{n}is shown to be annn-local quantity.
In particular, we identify the two-local member of this hierarchyQ2Q_{2}with the Hamiltonian;Q2=HQ_{2}=H.
This commuting transfer-matrix structure provides the algebraic basis for accessing eigenenergies and eigenstates, since the familyT​(u)T(u), which can be expressed in terms of commuting local quantities, can be diagonalized simultaneously and the Hamiltonian is obtained from it.
These local conserved quantities underlie the distinctive dynamics of integrable systems, including relaxation to generalized Gibbs ensembles[12,41]and transport described by generalized hydrodynamics[10].

Note that we have another route to the Hamiltonian from theRR-matrix.
Consider a series expansion ofΠ​R​(u)\Pi R(u)in terms ofuu.
Regularity fixes the zeroth-order term to the identity.
Namely, the local Hamiltonian is also directly obtained from the ordinary derivative of theRR-matrix ash=Π​R′​(0)h=\Pi R^{\prime}(0).
More generally, we can expand a regularRR-matrix asR​(u)=Π​(1+h​u+∑n=2∞Rˇ(n)​un).R(u)=\Pi\left(1+hu+\sum_{n=2}^{\infty}{\check{R}}^{(n)}u^{n}\right).(3)

In both routes, the Hamiltonian is obtained only as the derivative of a much richer object.
Yang–Baxter integrability is therefore not expressed as a closed condition onhhitself, which is why testing and discovering integrable Hamiltonians have been difficult tasks.

## Simple criterion for Yang–Baxter integrability

To obtain Hamiltonian-level constraints, we substitute the series expansion (3) into Eq. (1).
The second order equation can always be satisfied by choosingRˇ(2)=h2/2{\check{R}}^{(2)}=h^{2}/2.
On the other hand, whether the third order equation has a solution depends on the Hamiltonian: it admits a solution if and only if the following nested commutator can be written as a telescopic difference,[h12+h23,[h12,h23]]=X23−X12,[h_{12}+h_{23},[h_{12},h_{23}]]=X_{23}-X_{12},(4)

whereXi​jX_{ij}is a suitable operator acting on two sitesiiandjj.
This condition is called theReshetikhin condition[31].
Because the left-hand side is not generally of telescopic form, Eq. (4) is a nontrivial necessary condition for a local Hamiltonian to admit a Yang–Baxter structure.

The Reshetikhin condition has therefore been used as a practical test of integrability in searches for new integrable models.
Yet it is only the lowest-order nontrivial relation obtained from the Yang–Baxter equation, and thus a Hamiltonian could in principle satisfy the Reshetikhin condition while failing at some higher order.
Remarkably, however, all known models that pass the Reshetikhin condition have ultimately been found to admit anRR-matrix satisfying the Yang–Baxter equation.
This observation motivated the conjecture, according to which the Reshetikhin condition should already imply the full Yang–Baxter equation.
Nevertheless, this hypothesis has remained unresolved for more than four decades.

We turn this empirical coincidence into a theorem:

## Theorem 1.

Consider a one-dimensional, translation-invariant spin chain with nearest-neighbour interactions, whose local Hilbert space is finite-dimensional.
Suppose that a two-site Hamiltonian densityhhsatisfies the Reshetikhin condition (4) and thatH=∑i=1Lhi,i+1H=\sum_{i=1}^{L}h_{i,i+1}is diagonalizable.
Then there exists a regularRR-matrix, analytic nearu=0u=0, satisfying the Yang–Baxter equation (1) whose corresponding transfer matrix reproducesHHas its logarithmic derivative.

Thus the Reshetikhin condition is not merely a low-order necessary test; in this setting it is a complete Hamiltonian-level criterion for Yang–Baxter integrability.
Instead of first finding a suitableRR-matrix, one can verify integrability by checking the nested-commutator identity (4) directly.Figure 2:Energy-current conservation as an experimental certificate of Yang–Baxter integrability.The total energy current provides an experimentally accessible probe of exact solvability in an interacting quantum spin chain.
Our theorem identifies conservation of the total energy currentJE=i​∑j[hj−1,j,hj,j+1](=−i​Q3B)J_{E}=i\sum_{j}[h_{j-1,j},h_{j,j+1}](=-iQ_{3}^{B})with regular difference-form Yang–Baxter integrability.
Thus, energy-current conservation holds if and only if the Hamiltonian belongs to this Yang–Baxter-integrable class.
For cold-atom and related quantum-simulation realizations of one-dimensional spin chains, observing energy-current conservation provides a direct criterion for determining whether the implemented Hamiltonian lies on an integrable locus.

This theorem also reveals a surprising rigidity underlying Yang–Baxter integrability: the lowest-order nontrivial relation already forces the all-order relations.
This unexpected collapse suggests that the Yang–Baxter equation is highly redundant and that its essential content is far simpler than its apparent complexity.

Because the Reshetikhin condition is equivalent to conservation of the total energy current[57,30], our theorem also has a direct experimental implication. Exact solvability is usually regarded as a purely mathematical property, beyond the reach of experimental verification.
Our result challenges this view by showing a striking connection between mathematics and experiment: Yang–Baxter solvability can be diagnosed by measuring a single physical observable—the total energy current.

## Proving Yang–Baxter integrability from a Hamiltonian-level condition

To outline the proof of our main theorem, we first briefly explain another route to local conserved quantities in the Yang–Baxter framework.
Suppose that a Hamiltonian can be obtained from a regularRR-matrix satisfying the Yang–Baxter equation.
We introduce theboost operatorB:=∑jj​hj,j+1B:=\sum_{j}jh_{j,j+1}, which recursively generatesnn-local conserved quantities in a bottom-up fashion asQn+1B:=[B,QnB]Q^{\rm B}_{n+1}:=[B,Q^{\rm B}_{n}]withQ2B=HQ^{\rm B}_{2}=H.
Assuming the Yang–Baxter equation,QnBQ^{\rm B}_{n}is shown to coincide with the logarithmic-derivative chargeQnQ_{n}defined in Eq. (2), which follows from the relation[B,Qm]=Qm+1[B,Q_{m}]=Q_{m+1}.
We note that, even without assuming the Yang–Baxter equation, it has been shown that the Reshetikhin condition—or equivalently[Q3B,H]=0[Q^{\rm B}_{3},H]=0—implies[QnB,H]=0[Q^{\rm B}_{n},H]=0for allnn[23].

To prove the main theorem, we follow the standard arguments in the Yang–Baxter framework, but in a setting where the Yang–Baxter equation has not yet been established.
To this end, we start from a candidateRR-matrix of the form Eq. (3), without assuming that it satisfies the Yang–Baxter equation.
We write the discrepancy between the two sides of the Yang–Baxter equation as correction terms:R12​(u)​R13​(u+v)​R23​(v)−R23​(v)​R13​(u+v)​R12​(u)\displaystyle R_{12}(u)R_{13}(u+v)R_{23}(v)-R_{23}(v)R_{13}(u+v)R_{12}(u)=∑k,lF123k,l​uk​vl.\displaystyle=\sum_{k,l}F^{k,l}_{123}u^{k}v^{l}.(5)

The Reshetikhin condition allows us to setF1232,1=0F^{2,1}_{123}=0by a suitable choice ofRˇ(3)\check{R}^{(3)}.
Our goal is to prove that there exists a suitableRˇ(n){\check{R}}^{(n)}’s such that these correction termsF123k,lF^{k,l}_{123}can be eliminated order by order.
In this way, the usual Yang–Baxter argument is turned into a bootstrap proof of the Yang–Baxter equation itself.Figure 3:From the Reshetikhin condition to the full Yang–Baxter equation.This figure locates the Reshetikhin condition within the spectral-parameter expansion of the Yang–Baxter equation and summarizes the proof strategy.
Expanding the Yang–Baxter equation in two spectral parameters produces a two-dimensional array of order-by-order constraints.
Some of the lowest-order constraints are automatic, and the first nontrivial Hamiltonian-level constraint is the Reshetikhin condition, marked in the figure.
Step 1 shows that this single condition is sufficient to continue the one-parameter recursive construction to all orders, eliminating the constraints along the first nontrivial line.
Step 2 shows that the remaining two-parameter constraints are not independent: constraints with the same total degree are linked by a higher consistency relation.
As a result, the vanishing along the first line propagates across each diagonal of fixed total degree, leaving no higher Yang–Baxter obstruction.
Thus the low-order Reshetikhin condition forces the full Yang–Baxter equation.

We show this in the following two steps.
In the first step, we recursively show that a suitableRˇ(n){\check{R}}^{(n)}’s makeF123k,1=0F^{k,1}_{123}=0for allkk.
The induction step proceeds as follows.
Assume thatFk,1=0F^{k,1}=0for allk≤n−2k\leq n-2.
We first showQn=QnBQ_{n}=Q^{\rm B}_{n}through a careful computation of the correction terms.
We then show that∑i=1LΠi−1,i+1​Fi−1,i,i+1n−1,1=0\sum_{i=1}^{L}\Pi_{i-1,i+1}F^{n-1,1}_{i-1,i,i+1}=0by expanding[T​(u),H][T(u),H]up to orderun−1u^{n-1}in two different ways.
The first computation follows a telescopic sum of theSutherland equation, which is a derivative of the Yang–Baxter equation, with the correction terms kept.
The second uses the series expansionT​(u)∼exp⁡(u​Q2+u22​Q3+⋯)T(u)\sim\exp\left(uQ_{2}+\frac{u^{2}}{2}Q_{3}+\cdots\right)up to the global translation operator, which follows from Eq. (2).
A comparison of the two expressions yields∑i=1LΠi−1,i+1​Fi−1,i,i+1n−1,1=0\sum_{i=1}^{L}\Pi_{i-1,i+1}F^{n-1,1}_{i-1,i,i+1}=0, which impliesΠ13​F123n−1,1=X12−X23\Pi_{13}F^{n-1,1}_{123}=X_{12}-X_{23}.
The telescopic term can be absorbed by a suitable choice ofRˇ(n){\check{R}}^{(n)}, so thatF123n−1,1=0F^{n-1,1}_{123}=0.

In the second step, we show that all coefficientsF123k,lF^{k,l}_{123}withk+l=nk+l=nare proportional to a common operator.
This shows, in particular, thatF123n−1,1=0F^{n-1,1}_{123}=0for allnnimpliesF123k,l=0F^{k,l}_{123}=0for allk,lk,l, and hence that the Yang–Baxter equation holds without correction terms.

Letωn​(u,v):=∑k+l=nF123k,l​uk​vl\omega_{n}(u,v):=\sum_{k+l=n}F^{k,l}_{123}u^{k}v^{l}be the homogeneous correction term of degreennin the modified Yang–Baxter equation (5).
A careful comparison of the two sides of the four-particle factorization identity with correction terms yields the cocyclic condition:ωn​(u,v)+ωn​(u+v,w)=ωn​(v,w)+ωn​(u,v+w)\omega_{n}(u,v)+\omega_{n}(u+v,w)=\omega_{n}(v,w)+\omega_{n}(u,v+w).
Using the equivalence between the cocyclic condition and the coboundary condition, i.e.,ωn​(u,v)=g​(u+v)−g​(u)−g​(v)\omega_{n}(u,v)=g(u+v)-g(u)-g(v)with a suitableg​(x)g(x), we finally getωn​(u,v)=((u+v)n−un−vn)​K\omega_{n}(u,v)=((u+v)^{n}-u^{n}-v^{n})K.
Thus, all coefficientsF123k,lF^{k,l}_{123}withk+l=nk+l=nandk,l≥1k,l\geq 1are proportional to the same operatorKK.

## Detecting integrability and reconstructing R-matrices

Our theorem provides a practical advantage both in the search for integrable systems and in the reconstruction of the correspondingRR-matrices.
For the search problem, the advantage is direct: one can work in the space of local Hamiltonians, rather than in the much larger space of parametrizedRR-matrices.
The theorem also gives a constructive route to theRR-matrix itself.
Indeed, the proof can be read as an order-by-order algorithm for determining the coefficientsRˇ(n)\check{R}^{(n)}in the expansion (3).
At each order, the unknown two-site coefficient is fixed by matching a difference of the formRˇ23(n+1)−Rˇ12(n+1)\check{R}^{(n+1)}_{23}-\check{R}^{(n+1)}_{12}to an expression determined by lower-order coefficients.
Our theorem guarantees that, once the Reshetikhin condition is
satisfied, this matching problem has a solution at every order, and
that the resulting series converges and satisfies the full
Yang–Baxter equation.

The computational cost of this procedure is modest.
This recursion process requires storing only two-site coefficients in the memory and evaluating the components needed to determine the next two-site operator.
This reduction is what makes the Hamiltonian-level search substantially efficient compared with a direct search overRR-matrices.
The resulting time and memory costs are summarized in Table1.
Detailed algorithms and the implementation are provided in the Supplementary Information and in the accompanying code package.Table 1:Computational complexity of the proposed algorithm.TaskTimeMemoryReshetikhin testO​(d8)O(d^{8})O​(d6)O(d^{6})RR-matrix reconstructionO​(n2​d6)O(n^{2}d^{6})O​(n​d4)O(nd^{4})

Hered=dimVd=\dim Vis the dimension of the local Hilbert space, andnnis the reconstruction order of theRR-matrix. The estimates assume standard cubic matrix multiplication and a generic dense two-site Hamiltonian densityh∈End​(V⊗V)h\in\mathrm{End}(V\otimes V).

## Toward refinement of quantum integrability

The definition of quantum integrability has long been elusive, unlike the case of classical Hamiltonian integrability[51,11]. In classical systems, the Liouville–Arnold theorem establishes an equivalence between the existence of sufficiently many independent, mutually commuting conserved quantities and solvability in terms of action-angle variables.
For quantum systems, however, no comparable equivalence has been established, leaving the notion of integrability without an equally firm foundation.
The Yang–Baxter equation provides a mathematical characterization of solvability, while infinitely many local conserved quantities provide a physical characterization. This gap between mathematical and physical characterizations has been one reason why the definition of quantum integrability has remained subtle.Figure 4:A quantum counterpart of the Liouville–Arnold theorem.In classical Hamiltonian mechanics, the Liouville–Arnold theorem establishes an equivalence between conserved quantities and solvability: for a system withnndegrees of freedom, the existence ofnnindependent mutually commuting conserved quantities is equivalent to solvability in the Hamilton–Jacobi sense.
In quantum systems, an analogous equivalence between local conserved quantities and Yang–Baxter solvability has long been missing.
The present work establishes such a correspondence in isotropic nearest-neighbour spin chains.
The known conservation-law structure in the isotropic class and the theorem proved here together show that a model has only two possibilities: either it has no nontrivial local conserved quantity and no Yang–Baxter structure, or it has infinitely many local conserved quantities together with Yang–Baxter solvability.
Thus, within this class, the appearance of even a single nontrivial local conserved quantity forces the full hierarchy and identifies the model as Yang–Baxter solvable.
We expect this quantum Liouville–Arnold-type picture to extend to broader classes of quantum systems.

Our result establishes the desired correspondence in the standard setting of translation-invariant nearest-neighbour spin chains.
More precisely, the existence of a regular solution of the difference-form Yang–Baxter equation is equivalent to the conservation of the hierarchy of local quantities generated by the standard boost operator.
This shows that Yang–Baxter solvability and the conservation hierarchy are two manifestations of the same integrable structure, although the present correspondence is restricted to this particular boost-generated hierarchy.

This correspondence becomes particularly sharp when combined with existing classification results for isotropic nearest-neighbour spin chains[42].
In this class, local conservation laws exhibit an all-or-nothing structure: a model possesses either infinitely many nontrivial local conserved quantities or none at all.
Moreover, the former case occurs exactly when the Reshetikhin condition is satisfied.
Together with the present result, this implies that, within this class, Yang–Baxter solvability is equivalent to the existence of infinitely many local conserved quantities, and even to the existence of a single nontrivial local conserved quantity.
In this sense, our result provides a quantum counterpart of the Liouville–Arnold theorem for this class of spin chains.

A complete quantum counterpart of the Liouville–Arnold theorem will require extending this correspondence beyond the difference-form setting.
Models solvable by non-difference-form Yang–Baxter equations need not satisfy the Reshetikhin condition, and their local conserved quantities are generated not by the standard boost operator but by a generalized one[33,14].
In this framework, one generally obtains a one-parameter family of integrable Hamiltonians, with the Hamiltonian of interest appearing as a particular member of that family.
Extending our result to this broader setting is challenging, but would be an important step towards a general characterization of quantum integrability.

## Methods

Here we briefly review some useful properties of Yang–Baxter integrable models and outline the proof of our main theorem.

## Local conserved quantities from the Yang–Baxter equation

We first explain how the Yang–Baxter equation (1) provides an infinite family of commuting local quantities.
Introducing a single-site auxiliary systemaa, we construct a transfer matrixT​(u)T(u)onLLspins asT​(u):=Tra​[∏i=1LRa​i​(u)]=Tra​[Ra​L​(u)​⋯​Ra​2​(u)​Ra​1​(u)].\displaystyle T(u):=\mathrm{Tr}_{a}[\prod_{i=1}^{L}R_{ai}(u)]=\mathrm{Tr}_{a}[R_{aL}(u)\cdots R_{a2}(u)R_{a1}(u)].(6)

After insertingRa​b​(u−v)​Ra​b−1​(u−v)R_{ab}(u-v)R_{ab}^{-1}(u-v), we repeatedly apply the Yang–Baxter equationRa​b​(u−v)​Ra​i​(u)​Rb​i​(v)=Rb​i​(v)​Ra​i​(u)​Ra​b​(u−v)R_{ab}(u-v)R_{ai}(u)R_{bi}(v)=R_{bi}(v)R_{ai}(u)R_{ab}(u-v).
This yields the commutativity of transfer matrices,[T​(u),T​(v)]=0\displaystyle[T(u),T(v)]=0(7)

for sufficiently smalluuandvv.
Then, a commuting family ofnn-local quantitiesQnQ_{n}is provided byQn=dn−1d​un−1​ln⁡T​(u)|u=0.Q_{n}=\left.\frac{d^{n-1}}{du^{n-1}}\ln T(u)\right|_{u=0}.(8)

In particular, we identifyQ2Q_{2}withHH.
Since[ln⁡T​(u),ln⁡T​(v)]=0[\ln T(u),\ln T(v)]=0in this neighborhood, the coefficients ofun−1u^{n-1}inln⁡T​(u)\ln T(u)andvm−1v^{m-1}inln⁡T​(v)\ln T(v)commute with each other, meaning[Qn,Qm]=0\displaystyle[Q_{n},Q_{m}]=0(9)

for anynnandmm.

## Boost operator

Consider a Hamiltonian obtained from a regularRR-matrix satisfying the Yang–Baxter equation.
To construct local conserved quantities in a bottom-up fashion, we introduce theboost operatorB:=∑jj​hj,j+1.B:=\sum_{j}jh_{j,j+1}.(10)

Using this boost operator, we recursively construct the local quantitiesQnBQ^{\rm B}_{n}asQn+1B:=[B,QnB],Q2B=H.Q^{\rm B}_{n+1}:=[B,Q^{\rm B}_{n}],\hskip 10.0ptQ^{\rm B}_{2}=H.(11)

Assuming the Yang–Baxter equation, the boost-generated quantitiesQnBQ^{\rm B}_{n}coincide with the logarithmic-derivative chargesQnQ_{n}defined in Eq. (8).
This equivalence can be shown by using theSutherland equation(dd​u​R13​(u))​R12​(u)−R13​(u)​(dd​u​R12​(u))\displaystyle\left(\frac{d}{du}R_{13}(u)\right)R_{12}(u)-R_{13}(u)\left(\frac{d}{du}R_{12}(u)\right)=\displaystyle=[R13​(u)​R12​(u),h23].\displaystyle[R_{13}(u)R_{12}(u),h_{23}].(12)

The Sutherland equation is obtained by differentiating the Yang–Baxter equation (1) with respect tovvand then settingv=0v=0.
Using the Sutherland equation along the chain, the resulting terms telescope and give[B,T​(u)]=dd​u​T​(u),\displaystyle[B,T(u)]=\frac{d}{du}T(u),(13)

which leads to[B,Qm]=Qm+1.\displaystyle[B,Q_{m}]=Q_{m+1}.(14)

Starting fromQ2B=Q2=HQ^{\rm B}_{2}=Q_{2}=H, repeated application of this relation yieldsQnB=QnQ^{\rm B}_{n}=Q_{n}for alln≥2n\geq 2.

We note that, even without assuming the Yang–Baxter equation, it has been shown that the Reshetikhin condition—or equivalently[Q3B,H]=0[Q^{\rm B}_{3},H]=0—implies[QmB,QnB]=0[Q^{\rm B}_{m},Q^{\rm B}_{n}]=0for allmmandnn.
This means that the presence of a 3-local conserved quantity given by the boost operator implies an infinite family of local conserved quantities.

## Lemma 2(Hokkyo[23]).

Consider a nearest-neighbor translation-invariant HamiltonianH=∑ihi,i+1H=\sum_{i}h_{i,i+1}. Suppose thatHHis diagonalizable and that[Q3B,H]=0[Q^{\rm B}_{3},H]=0, whereQ3BQ^{\rm B}_{3}is given by Eq. (11).
Then,QnBQ^{\rm B}_{n}satisfies[QmB,QnB]=0[Q^{\rm B}_{m},Q^{\rm B}_{n}]=0for allm,n≥2m,n\geq 2.

## Expansion ofRR-matrix and Reshetikhin condition

We here examine a series expansion of a regularRR-matrix.
For this purpose, it is useful to introduce thebraidedRR-matrixRˇ​(u):=Π​R​(u)\check{R}(u):=\Pi R(u)with the permutation operatorΠ\Pi, instead ofR​(u)R(u)itself.
By construction,Rˇ​(0)=I\check{R}(0)=Iis satisfied.
The Yang–Baxter equation in terms ofRˇ\check{R}readsRˇ12​(u)​Rˇ23​(u+v)​Rˇ12​(v)=Rˇ23​(v)​Rˇ12​(u+v)​Rˇ23​(u).\check{R}_{12}(u)\check{R}_{23}(u+v)\check{R}_{12}(v)=\check{R}_{23}(v)\check{R}_{12}(u+v)\check{R}_{23}(u).(15)

We expandRˇ​(u)\check{R}(u)asRˇ​(u)=I+h​u+∑n=2∞Rˇ(n)​un.\check{R}(u)=I+hu+\sum_{n=2}^{\infty}{\check{R}}^{(n)}u^{n}.(16)

Plugging this expansion (16) into the Yang–Baxter equation (15) and comparing the coefficients of eachuk​vlu^{k}v^{l}, we obtain various nontrivial relations onRˇ(n){\check{R}}^{(n)}’s.

Comparison at orderu​vuvin Eq. (15) gives2​Rˇ23(2)−h232=2​Rˇ12(2)−h122,\displaystyle 2\check{R}^{(2)}_{23}-h^{2}_{23}=2\check{R}^{(2)}_{12}-h^{2}_{12},(17)

which can always be satisfied by choosingRˇ(2)=12​h2.\displaystyle\check{R}^{(2)}=\frac{1}{2}h^{2}.(18)

Comparison at orderu​v2uv^{2}givesRˇ12(3)−Rˇ23(3)+16​[h12+h23,[h12,h23]]−16​h123+16​h233=0.\displaystyle\check{R}^{(3)}_{12}-\check{R}^{(3)}_{23}+\frac{1}{6}[h_{12}+h_{23},[h_{12},h_{23}]]-\frac{1}{6}h^{3}_{12}+\frac{1}{6}h^{3}_{23}=0.(19)

This equation does not always admit a solution forRˇ(3)\check{R}^{(3)}.
It has a solution if and only if the commutator term is written as a telescopic difference,[h12+h23,[h12,h23]]=X23−X12,[h_{12}+h_{23},[h_{12},h_{23}]]=X_{23}-X_{12},(20)

whereXi​jX_{ij}is a suitable two-site operator acting on sitesiiandjj.
This condition is called theReshetikhin condition.
If this condition is satisfied, thenRˇ(3)=(X+h3)/6{\check{R}}^{(3)}=(X+h^{3})/6gives a solution of the relation at orderu​v2uv^{2}.

In general, the equation obtained from theu​vnuv^{n}coefficient can be shown to admit a solution forRˇ(n+1)\check{R}^{(n+1)}for all oddnn.
On the other hand, for evennn, whether this equation admits a solution forRˇ(n+1)\check{R}^{(n+1)}is highly nontrivial.
The second nontrivial condition is obtained from theu​v4uv^{4}coefficient:[h123+h233+3​(X12+X23),[h12,h23]]\displaystyle[h_{12}^{3}+h_{23}^{3}+3(X_{12}+X_{23}),[h_{12},h_{23}]]+3​(h12​[[h12,h23],h12]​h12+h23​[[h12,h23],h23]​h23)\displaystyle+3(h_{12}[[h_{12},h_{23}],h_{12}]h_{12}+h_{23}[[h_{12},h_{23}],h_{23}]h_{23})+(h12​h23+h23​h12)​Δ​X+Δ​X​(h12​h23+h23​h12)\displaystyle+(h_{12}h_{23}+h_{23}h_{12})\mathit{\Delta}X+\mathit{\Delta}X(h_{12}h_{23}+h_{23}h_{12})−2​(h12​Δ​X​h23+h23​Δ​X​h12)\displaystyle-2(h_{12}\mathit{\Delta}Xh_{23}+h_{23}\mathit{\Delta}Xh_{12})=\displaystyle=Y23−Y12.\displaystyle Y_{23}-Y_{12}.(21)

Here, we have definedΔ​X:=X23−X12\mathit{\Delta}X:=X_{23}-X_{12}.
This condition is sometimes called thesecond integrability test[8].

## Proof outline of main theorem

We now outline the proof that, for any local Hamiltonian densityhhsatisfying the Reshetikhin condition (20), there exists anRR-matrix of the form Eq. (3) satisfying the Yang–Baxter equation (1).
Consider anRR-matrix of the form Eq. (3) which does not necessarily satisfy the Yang–Baxter equation.
If we compute both sides of the Yang–Baxter equation with thisRR, their difference may be nonzero.
We expand this difference asR12​(u)​R13​(u+v)​R23​(v)−R23​(v)​R13​(u+v)​R12​(u)\displaystyle R_{12}(u)R_{13}(u+v)R_{23}(v)-R_{23}(v)R_{13}(u+v)R_{12}(u)=\displaystyle=∑k,lF123k,l​uk​vl.\displaystyle\sum_{k,l}F^{k,l}_{123}u^{k}v^{l}.(22)

Correspondingly, in terms of the braidedRR-matrix, we writeRˇ12​(u)​Rˇ23​(u+v)​Rˇ12​(v)−Rˇ23​(v)​Rˇ12​(u+v)​Rˇ23​(u)\displaystyle\check{R}_{12}(u)\check{R}_{23}(u+v)\check{R}_{12}(v)-\check{R}_{23}(v)\check{R}_{12}(u+v)\check{R}_{23}(u)=\displaystyle=∑k,lFˇ123l,k​ul​vk,\displaystyle\sum_{k,l}\check{F}^{l,k}_{123}u^{l}v^{k},(23)

where we definedFˇa​b​cl,k:=−Πa​c​Fa​b​ck,l\check{F}^{l,k}_{abc}:=-\Pi_{ac}F^{k,l}_{abc}for later convenience.
The Reshetikhin condition states thatFˇ1231,2=−Π13​F1232,1\check{F}^{1,2}_{123}=-\Pi_{13}F^{2,1}_{123}takes a telescopic form.
This telescopic term can be eliminated by choosing a suitableRˇ(3)\check{R}^{(3)}.
Our goal is to prove that there exists a suitableRˇ(n){\check{R}}^{(n)}’s such that allF123k,lF^{k,l}_{123}vanish.
We shall show this by proving the following two lemmas:

## Lemma 3.

Suppose that a given Hamiltonianhhsatisfies the Reshetikhin condition (20) and thatH=∑ihi,i+1H=\sum_{i}h_{i,i+1}is diagonalizable.
Then, there exists suitableRˇ(n){\check{R}}^{(n)}’s which makeF123k,1=0F^{k,1}_{123}=0for allkk.

## Lemma 4.

Suppose thatF123k,l=0F^{k,l}_{123}=0for allkkandllwithk+l≤n−1k+l\leq n-1.
Then, allF123k,lF^{k,l}_{123}’s withk+l=nk+l=nandk,l≥1k,l\geq 1are proportional to each other.

## From Reshetikhin to Sutherland (Lemma3)

Assume inductively that the coefficientsRˇ(2),…​Rˇ(n−1){\check{R}}^{(2)},\dots\check{R}^{(n-1)}have been chosen so thatFˇ1231,k=0\check{F}^{1,k}_{123}=0(equivalently,F123k,1=0F^{k,1}_{123}=0) for1≤k≤n−21\leq k\leq n-2.
We then showFˇ1231,n−1=Z23−Z12.\displaystyle\check{F}^{1,n-1}_{123}=Z_{23}-Z_{12}.(24)

This telescopic term can be canceled by choosing suitableRˇ(n){\check{R}}^{(n)}in terms ofZZ, and hence we obtainFˇ1231,n−1=−Π13​F123n−1,1=0\check{F}^{1,n-1}_{123}=-\Pi_{13}F^{n-1,1}_{123}=0.

To prove this, we first show the following lemma:

## Lemma 5.

Suppose thatFk,1=0F^{k,1}=0for all1≤k≤n−21\leq k\leq n-2,
after suitably choosingRˇ(2),…,Rˇ(n−1)\check{R}^{(2)},\dots,\check{R}^{(n-1)}.
Then, we haveQm=QmBQ_{m}=Q^{\rm B}_{m}for2≤m≤n2\leq m\leq n.

This lemma is shown as follows.
Differentiating the Yang–Baxter equation with correction terms, Eq. (22), with respect tovvand then settingv=0v=0, we obtain the Sutherland equation with correction terms of orderO​(un−1)O(u^{n-1}):(dd​u​R13​(u))​R12​(u)−R13​(u)​(dd​u​R12​(u))\displaystyle\left(\frac{d}{du}R_{13}(u)\right)R_{12}(u)-R_{13}(u)\left(\frac{d}{du}R_{12}(u)\right)=\displaystyle=[R13​(u)​R12​(u),h23]−∑k=n−1∞Π23​F123k,1​uk.\displaystyle[R_{13}(u)R_{12}(u),h_{23}]-\sum_{k={n-1}}^{\infty}\Pi_{23}F^{k,1}_{123}u^{k}.(25)

Here, lower-degree terms are absent becauseFk,1=0F^{k,1}=0for allk≤n−2k\leq n-2by supposition.
Following the standard derivation ofQnB=QnQ^{\rm B}_{n}=Q_{n}with the Sutherland equation replaced by the above modified one, we arrive at[B,T​(u)]=dd​u​T​(u)+O​(un−1).\displaystyle[B,T(u)]=\frac{d}{du}T(u)+O(u^{n-1}).(26)

Applying the commutator term by term to a formal power-series
representation oflog⁡T​(u)\log T(u), Eq. (26) gives[B,log⁡T​(u)]=dd​u​log⁡T​(u)+O​(un−1).\displaystyle[B,\log T(u)]=\frac{d}{du}\log T(u)+O(u^{n-1}).(27)

Using the definition Eq. (8) and comparing the coefficients ofum−2u^{m-2}for3≤m≤n3\leq m\leq n,
we obtain[B,Qm−1]=Qm.\displaystyle[B,Q_{m-1}]=Q_{m}.(28)

SinceQ2=Q2B=HQ_{2}=Q_{2}^{B}=H, this
recursively impliesQm=QmB,2≤m≤n,\displaystyle Q_{m}=Q_{m}^{B},\qquad 2\leq m\leq n,(29)

and proves Lemma5.

We now return to the proof of Lemma3.
Summing the modified Sutherland equation (25) along the chain, the derivative terms cancel telescopically, giving0\displaystyle 0=[∏i=1LRa​i​(u),H]\displaystyle=\left[\prod_{i=1}^{L}R_{ai}(u),H\right]−∑i=1L∑k=n−1∞[∏j=i+2LRa​j​(u)]​Πi,i+1​Fa,i,i+1k,1​[∏j=1i−1Ra​j​(u)]​uk.\displaystyle-\sum_{i=1}^{L}\sum_{k=n-1}^{\infty}\left[\prod_{j=i+2}^{L}R_{aj}(u)\right]\Pi_{i,i+1}F^{k,1}_{a,i,i+1}\left[\prod_{j=1}^{i-1}R_{aj}(u)\right]u^{k}.(30)

After taking the trace over the auxiliary space, the leading correction is obtained by settingk=n−1k=n-1and replacing every remainingR​(u)R(u)byR​(0)=ΠR(0)=\Pi.
Tracking the permutation operators then gives[T​(u),H]=−S​∑i=1LFˇi−1,i,i+11,n−1​un−1+O​(un).[T(u),H]=-S\sum_{i=1}^{L}\check{F}_{i-1,i,i+1}^{1,n-1}u^{n-1}+O(u^{n}).(31)

On the other hand, the definition Eq. (8) and Lemma5yieldT​(u)\displaystyle T(u)=S​exp⁡(∑m=2num−1(m−1)!​Qm)+O​(un)\displaystyle=S\exp\left(\sum_{m=2}^{n}\frac{u^{m-1}}{(m-1)!}Q_{m}\right)+O(u^{n})=S​exp⁡(∑m=2num−1(m−1)!​QmB)+O​(un).\displaystyle=S\exp\left(\sum_{m=2}^{n}\frac{u^{m-1}}{(m-1)!}Q^{\rm B}_{m}\right)+O(u^{n}).(32)

All the boost-generated chargesQmBQ^{\rm B}_{m}commute withH=Q2BH=Q^{\rm B}_{2}by Lemma2, and translation invariance gives[S,H]=0[S,H]=0.
It follows that[T​(u),H]=O​(un).[T(u),H]=O(u^{n}).(33)

Comparing Eq. (31) and Eq. (33), we obtain∑i=1LFˇi−1,i,i+11,n−1=0.\displaystyle\sum_{i=1}^{L}\check{F}_{i-1,i,i+1}^{1,n-1}=0.(34)

The standard local telescoping argument then implies the existence of a two-site operatorZZsuch thatFˇ1231,n−1=Z23−Z12,\displaystyle\check{F}_{123}^{1,n-1}=Z_{23}-Z_{12},(35)

which is the required telescopic form and completes the proof of Lemma3.

## From Sutherland to Yang–Baxter (Lemma4)

We next show that allFˇ123l,k\check{F}^{l,k}_{123}withl+k=nl+k=nare proportional to each other.
This confirms thatFˇ1231,n−1=0\check{F}^{1,n-1}_{123}=0for allnn(Lemma3) impliesFˇ123l,k=−Π13​F123k,l=0\check{F}^{l,k}_{123}=-\Pi_{13}F_{123}^{k,l}=0for allkkandll, meaning the Yang–Baxter equation without any correction term.

Letωn​(u,v):=∑k+l=nFˇ123l,k​ul​vk\omega^{n}(u,v):=\sum_{k+l=n}\check{F}^{l,k}_{123}u^{l}v^{k}(36)

be the sum of thenn-th order correction terms in the modified Yang–Baxter equation (23).
With the notationA=Rˇ12A=\check{R}_{12},B=Rˇ23B=\check{R}_{23}, andC=Rˇ34C=\check{R}_{34}, repeated use of the Yang–Baxter equation (without any correction), together with the far-commutativity relationA​(x)​C​(y)=C​(y)​A​(x)A(x)C(y)=C(y)A(x), gives the four-particle factorization identityA​(u)​B​(u+v)​A​(v)​C​(u+v+w)​B​(v+w)​A​(w)\displaystyle A(u)B(u+v)A(v)C(u+v+w)B(v+w)A(w)=\displaystyle=C​(w)​B​(v+w)​A​(u+v+w)​C​(v)​B​(u+v)​C​(u).\displaystyle C(w)B(v+w)A(u+v+w)C(v)B(u+v)C(u).(37)

Importantly, there are two distinct ways to prove this identity by successive applications of the Yang–Baxter equation. These two sequences correspond to the two sides of theZamolodchikov tetrahedron equation, which expresses the consistency of different orders of applying the Yang–Baxter equation[55,28]. When correction terms are included, comparison of the two sequences yields the cocycle condition:ωn​(u,v)+ωn​(u+v,w)=ωn​(v,w)+ωn​(u,v+w).\displaystyle\omega^{n}(u,v)+\omega^{n}(u+v,w)=\omega^{n}(v,w)+\omega^{n}(u,v+w).(38)

A standard result applicable in the present setting, whereu,v,wu,v,ware scalar parameters, states that this cocycle is a coboundary. Thus, there exists a functionggsuch thatωn​(u,v)=g​(u+v)−g​(u)−g​(v).\displaystyle\omega^{n}(u,v)=g(u+v)-g(u)-g(v).(39)

Expandggas a formal power series with operator-valued coefficients,g​(x)=∑m=0∞Km​xm.g(x)=\sum_{m=0}^{\infty}K_{m}x^{m}.The contribution ofKmK_{m}to the coboundary is homogeneous of total degreemminuuandvv.
Sinceωn​(u,v)\omega^{n}(u,v)is homogeneous of total degreenn, comparison of the degree-nncomponents givesωn​(u,v)=Kn​((u+v)n−un−vn).\displaystyle\omega^{n}(u,v)=K_{n}\left((u+v)^{n}-u^{n}-v^{n}\right).(40)

For everyk,l≥1k,l\geq 1withk+l=nk+l=n, the coefficient oful​vku^{l}v^{k}is a nonzero scalar multiple of the same operatorKnK_{n}.
Hence all the coefficientsFˇ123l,k\check{F}^{l,k}_{123}withl+k=nl+k=nare mutually proportional and vanish simultaneously. This proves Lemma4.

## Data availability

No datasets were generated or analysed during the current study.

## Code availability

A Python reference implementation of the algorithms described in this work
is available athttps://github.com/sanatanim/reshetikhin.
Version 1.0.0 is archived on Zenodo athttps://doi.org/10.5281/zenodo.21721878.

## Acknowledgements

We thank Hosho Katsura for valuable comments.
We also thank Atsuo Kuniba, Yuuya Chiba, and Akihiro Hokkyo for fruitful discussions.
This work was assisted by GPT-5.4 Pro through ChatGPT (OpenAI).
This work was supported by JSPS KAKENHI Grant Number JP25KJ0815, Grant-in-Aid for Early-Career Scientists 26K17048, Grant-in-Aid for Transformative Research Areas (B) 26K00021, and JST ERATO Grant Number JPMJER2302.

## Author contributions

M.S. and N.S. contributed equally to this work and are listed in alphabetical order.
N.S. worked on the proof of Lemma3, and
M.S. worked on the proof of Lemma4.
F.I. and M.S. developed the code.
All authors contributed to the design of the project and preparation of the manuscript.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information is available for this paper.

## References
- [1]F. C. Alcaraz, M. Droz, M. Henkel, and V. Rittenberg(1994)Reaction-diffusion processes, critical dynamics, and quantum chains.Annals of Physics230(2),pp. 250–302.External Links:Document,hep-th/9302112,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [2]M. T. Batchelor and C. M. Yung(1994)Integrable SU(2)-invariant spin chains and the Haldane conjecture.External Links:cond-mat/9406072,Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [3]R. J. Baxter(1972)Partition function of the eight-vertex lattice model.Annals of Physics70(1),pp. 193–228.External Links:Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [4]R. J. Baxter(1985)Exactly solved models in statistical mechanics.InIntegrable systems in statistical mechanics,pp. 5–63.External Links:Document,LinkCited by:A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [5]H. Bethe(1931)Zur Theorie der Metalle. I. Eigenwerte und Eigenfunktionen der linearen Atomkette.Zeitschrift für Physik71(3–4),pp. 205–226.External Links:Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [6]P. N. Bibikov and A. G. Nuramatov(2014)RR-matrices for integrable axially symmetricS=1S=1spin chains.External Links:1408.4385,Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [7]P. N. Bibikov(2000)Derivation ofRR-matrix from local hamiltonian density.External Links:nlin/0006040,Document,LinkCited by:§II.1,§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [8]P. N. Bibikov(2003)How to solve Yang–Baxter equation using the taylor expansion ofRR-matrix.Physics Letters A314(3),pp. 209–213.External Links:Document,nlin/0112001,LinkCited by:§I.4,§II.1,§II.2,Expansion ofRR-matrix and Reshetikhin condition,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [9]P. N. Bibikov(2007)Defining relations on the hamiltonians of XXX and XXZRR-matrices and new integrable spin-orbital chains.Journal of Mathematical Sciences143,pp. 2723–2728.External Links:Document,nlin/0703017,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [10]O. A. Castro-Alvaredo, B. Doyon, and T. Yoshimura(2016)Emergent hydrodynamics in integrable quantum systems out of equilibrium.Physical Review X6(4),pp. 041065.External Links:Document,1605.07331,LinkCited by:The Yang–Baxter equation and integrability.
- [11]J. Caux and J. Mossel(2011)Remarks on the notion of quantum integrability.Journal of Statistical Mechanics: Theory and Experiment2011(02),pp. P02023.External Links:Document,1012.3587,LinkCited by:§II.1,Toward refinement of quantum integrability.
- [12]M. A. Cazalilla(2006)Effect of suddenly turning on interactions in the Luttinger model.Physical Review Letters97(15),pp. 156403.External Links:Document,cond-mat/0606236,LinkCited by:The Yang–Baxter equation and integrability.
- [13]L. Corcoran and M. de Leeuw(2024)All regular4×44\times 4solutions of the Yang–Baxter equation.SciPost Physics Core7(3),pp. 045.External Links:Document,2306.10423,LinkCited by:A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [14]M. de Leeuw, C. Paletta, A. Pribytok, A. L. Retore, and P. Ryan(2021)Yang–Baxter and the Boost: splitting the difference.SciPost Physics11(3),pp. 069.External Links:Document,2010.11231,LinkCited by:§I.4,§II.2,§IV.2,Toward refinement of quantum integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [15]M. de Leeuw and V. Posch(2024)All4×44\times 4solutions of the quantum Yang–Baxter equation.External Links:2411.18685,Document,LinkCited by:A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [16]M. de Leeuw, A. Pribytok, A. L. Retore, and P. Ryan(2020)New integrable 1D models of superconductivity.Journal of Physics A: Mathematical and Theoretical53(38),pp. 385201.External Links:Document,1911.01439,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [17]M. de Leeuw, A. Pribytok, and P. Ryan(2019)Classifying integrable spin-1/2 chains with nearest neighbour interactions.Journal of Physics A: Mathematical and Theoretical52(50),pp. 505201.External Links:Document,1904.12005,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [18]L. Faddeev(1996)How algebraic Bethe ansatz works for integrable model.External Links:hep-th/9605187,Document,LinkCited by:A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [19]T. Fonseca, L. Frappat, and E. Ragoucy(2015)RRmatrices of three-state hamiltonians solvable by coordinate Bethe ansatz.Journal of Mathematical Physics56(1),pp. 013503.External Links:Document,1406.3197,LinkCited by:§II.1,§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [20]M. P. Grabowski and P. Mathieu(1995)Integrability test for spin chains.Journal of Physics A: Mathematical and General28(17),pp. 4777–4798.External Links:Document,hep-th/9412039,LinkCited by:§I.3,§II.1,§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [21]J. Hietarinta(1992)All solutions to the constant quantum Yang–Baxter equation in two dimensions.Physics Letters A165(3),pp. 245–251.External Links:Document,hep-th/9210067,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [22]A. Hokkyo, M. Yamaguchi, and Y. Chiba(2025)Absence of nontrivial local conserved quantities in the spin-1 bilinear-biquadratic chain and its anisotropic extensions.Physical Review Research7(4),pp. 043297.External Links:Document,2411.04945,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [23]A. Hokkyo(2026)Integrability from a single conservation law in quantum spin chains.Physical Review B114(5),pp. 055108.External Links:Document,2508.20713,LinkCited by:§II.2,§II.2,Proving Yang–Baxter integrability from a Hamiltonian-level condition,Lemma S.1,Lemma 2.
- [24]M. Idzumi, T. Tokihiro, and M. Arai(1994)Solvable nineteen-vertex models and quantum spin chains of spin one.Journal de Physique I4(8),pp. 1151–1159.External Links:Document,LinkCited by:§II.2,§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [25]M. Jimbo and T. Miwa(1984)Some remarks on the differential approach to the star-triangle relation.Letters in Mathematical Physics8(6),pp. 529–537.External Links:Document,LinkCited by:§II.1,§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [26]M. Jimbo(1986)Aqq-analogue ofU​(gl​(N+1))U(\mathrm{gl}(N+1)), Hecke algebra, and the Yang–Baxter equation.Letters in Mathematical Physics11(3),pp. 247–252.External Links:Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [27]V. F. R. Jones(1991)Baxterization.International Journal of Modern Physics A6(12),pp. 2035–2043.External Links:Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [28]M. M. Kapranov and V. A. Voevodsky(1994)2-categories and Zamolodchikov tetrahedra equations.InProceedings of Symposia in Pure Mathematics,Vol.56,pp. 177–259.Cited by:§II.5,From Sutherland to Yang–Baxter (Lemma4).
- [29]T. Kennedy(1992)Solutions of the Yang–Baxter equation for isotropic quantum spin chains.Journal of Physics A: Mathematical and General25(10),pp. 2809–2817.External Links:Document,LinkCited by:§I.4,§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [30]A. Klümper and K. Sakai(2002)The thermal conductivity of the spin-1/21/2XXZ chain at arbitrary temperature.Journal of Physics A: Mathematical and General35(9),pp. 2173–2182.External Links:Document,cond-mat/0112444,LinkCited by:§II.1,Simple criterion for Yang–Baxter integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [31]P. P. Kulish and E. K. Sklyanin(1982)Quantum spectral transform method. recent developments.InIntegrable Quantum Field Theories,J. Hietarinta and C. Montonen (Eds.),Lecture Notes in Physics, Vol.151,pp. 61–119.External Links:Document,LinkCited by:§I.4,§II.1,§II.2,§II.2,Simple criterion for Yang–Baxter integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [32]S. Lal, S. Majumder, and E. Sobko(2025)Deep learning based discovery of integrable systems.External Links:2503.10469,Document,LinkCited by:§II.1,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [33]J. Links, H. Zhou, R. H. McKenzie, and M. D. Gould(2001)Ladder operator for the one-dimensional Hubbard model.Physical Review Letters86(22),pp. 5096.External Links:Document,cond-mat/0011368,LinkCited by:Toward refinement of quantum integrability.
- [34]S. Maity, V. K. Singh, P. Padmanabhan, and V. Korepin(2024)Algebraic classification of Hietarinta’s solutions of Yang–Baxter equations: invertible4×44\times 4operators.Journal of High Energy Physics2024(12),pp. 67.External Links:Document,2409.05375,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [35]K.-H. Mütter and A. Schmitt(1995)Solvable spin-1 models in one dimension.Journal of Physics A: Mathematical and General28(8),pp. 2265–2276.External Links:Document,LinkCited by:§II.1,§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [36]L. Onsager(1944)Crystal statistics. I. a two-dimensional model with an order-disorder transition.Physical Review65(3–4),pp. 117–149.External Links:Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [37]H. C. Öttinger and J. Honerkamp(1982)Note on the Yang–Baxter equations for generalized Baxter models.Physics Letters A88(7),pp. 339–343.External Links:Document,LinkCited by:§II.1,§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [38]C. Paletta and T. Prosen(2026)On the integrability structure of the deformed rule-54 reversible cellular automaton.External Links:2603.25424,Document,LinkCited by:§II.2.
- [39]C. Paletta(2023)Yang–Baxter integrable open quantum systems.External Links:2312.00064,Document,LinkCited by:§II.2.
- [40]H. K. Park and S. Lee(2025)Proof of nonintegrability of the spin-1 bilinear-biquadratic chain model.Physical Review B111(13),pp. 134444.External Links:Document,2410.23286,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [41]M. Rigol, V. Dunjko, V. Yurovsky, and M. Olshanii(2007)Relaxation in a completely integrable many-body quantum system: an ab initio study of the dynamics of the highly excited states of 1D lattice hard-core bosons.Physical Review Letters98(5),pp. 050405.External Links:Document,cond-mat/0604476,LinkCited by:The Yang–Baxter equation and integrability.
- [42]N. Shiraishi and M. Yamaguchi(2026)Dichotomy theorem separating complete integrability and nonintegrability of isotropic spin chains.Physical Review B113(24),pp. L241111.External Links:Document,2504.14315,LinkCited by:§II.1,Toward refinement of quantum integrability.
- [43]N. Shiraishi(2019)Proof of the absence of local conserved quantities in the XYZ chain with a magnetic field.EPL (Europhysics Letters)128(1),pp. 17002.External Links:Document,1803.02637,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [44]N. Shiraishi(2025)Complete classification of integrability and non-integrability ofS=1/2S=1/2spin chains with symmetric next-nearest-neighbor interaction.Journal of Statistical Physics192,pp. 170.External Links:Document,2501.15506,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [45]E. K. Sklyanin, L. A. Takhtajan, and L. D. Faddeev(1980)Quantum inverse problem method. I.Theoretical and Mathematical Physics40(2),pp. 688–706.External Links:Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [46]M. Takahashi(1999)Thermodynamics of one-dimensional solvable models.Cambridge university press Cambridge.External Links:Document,LinkCited by:A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [47]L. A. Takhtajan and L. D. Faddeev(1979)The quantum method of the inverse problem and the Heisenberg XYZ model.Russian Mathematical Surveys34(5),pp. 11–68.External Links:Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [48]M. Tetel’man(1982)Lorentz group for two-dimensional integrable lattice systems.Soviet Journal of Experimental and Theoretical Physics55(2),pp. 306.Cited by:§I.3,§II.2,§IV.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [49]H. B. Thacker(1986)Corner transfer matrices and Lorentz invariance on a lattice.Physica D: Nonlinear Phenomena18(1–3),pp. 348–359.External Links:Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [50]R. S. Vieira(2018)Solving and classifying the solutions of the Yang–Baxter equation through a differential approach. two-state systems.Journal of High Energy Physics2018(10),pp. 110.External Links:Document,1712.02341,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [51]S. Weigert(1992)The problem of quantum integrability.Physica D: Nonlinear Phenomena56(1),pp. 107–119.Cited by:§II.1,Toward refinement of quantum integrability.
- [52]M. Yamaguchi, Y. Chiba, and N. Shiraishi(2026)Complete classification of integrability and non-integrability for spin-1/2 chain with symmetric nearest-neighbor interaction.Physical Review Research.Note:in pressExternal Links:2411.02162,Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [53]M. Yamaguchi, Y. Chiba, and N. Shiraishi(2026)Proof of the absence of local conserved quantities in general spin-1/2 chains with symmetric nearest-neighbor interaction.Physical Review B.Note:in pressExternal Links:2411.02163,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [54]C. Yang(1967)Some exact results for the many-body problem in one dimension with repulsive delta-function interaction.Physical Review Letters19(23),pp. 1312–1315.External Links:Document,LinkCited by:§II.2,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [55]A. B. Zamolodchikov(1980)Tetrahedra equations and integrable systems in three-dimensional space.Soviet Physics JETP52(2),pp. 325–336.Note:[Zh. Eksp. Teor. Fiz. 79, 641–664 (1980)]Cited by:§II.5,From Sutherland to Yang–Baxter (Lemma4).
- [56]Z. Zhang(2026)Bootstrapping theRR-matrix.SciPost Physics20(4),pp. 102.External Links:Document,2504.17773,LinkCited by:§I.4,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.
- [57]X. Zotos, F. Naef, and P. Prelovsek(1997)Transport and conservation laws.Physical Review B55(17),pp. 11029.External Links:Document,cond-mat/9611007,LinkCited by:§II.1,Simple criterion for Yang–Baxter integrability,A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability.

Supplemental Material for
“A Simple Necessary and Sufficient Condition for Yang–Baxter Integrability”
Mizuki Sanatani, Naoto Shiraishi, and Fuga Ishii

Graduate School of Arts and Sciences / College of Arts and Sciences, The University of Tokyo

## IReview of Yang–Baxter integrable models

In this section, we briefly review basic results on the Yang–Baxter equation and integrable models.

## I.1Yang–Baxter equation and the quantum inverse scattering method

In the standard approach to integrable systems, we first construct a goodRR-matrix satisfying the Yang–Baxter equation.
ThisRR-matrix induces an infinite family of commuting local quantities, and we assign the 2-local quantity in this family to the integrable HamiltonianHH.
Below we explain this standard approach.

Consider a one-parameter family of matricesRi​j​(u)R_{ij}(u)on two sitesiiandjjcalledRR-matrix.
IfR​(0)R(0)is the swap operatorΠ\Pi, we call thisRR-matrixregular.
The parameteruuis called thespectral parameter.
The Yang–Baxter equation is expressed asR12​(u)​R13​(u+v)​R23​(v)=R23​(v)​R13​(u+v)​R12​(u).R_{12}(u)R_{13}(u+v)R_{23}(v)=R_{23}(v)R_{13}(u+v)R_{12}(u).(S.1)

Note that in a more general context, one considers a two-parameter family ofRR-matricesRi​j​(a,b)R_{ij}(a,b)and the non-difference-form Yang–Baxter equationR12​(a,b)​R13​(a,c)​R23​(b,c)=R23​(b,c)​R13​(a,c)​R12​(a,b).R_{12}(a,b)R_{13}(a,c)R_{23}(b,c)=R_{23}(b,c)R_{13}(a,c)R_{12}(a,b).(S.2)

To distinguish from the above one, Eq. (S.1) is also called the difference-form Yang–Baxter equation.
Throughout this Supplemental Material, we consider a one-parameter family of regularRR-matrices and the difference-form Yang–Baxter equation unless otherwise explicitly noted.

If there exists anRR-matrix satisfying the Yang–Baxter equation, we can construct an infinite family of commuting local quantities.
Consider a one-dimensional system withLLsites.
To construct a transfer matrix, we introduce an auxiliary siteaawhose Hilbert-space dimension is the same as that of a single site of the system.
Using theRR-matrix, we construct the monodromy matrixM​(u)M(u)on sites1,2,…,L1,2,\ldots,Landaa, and the transfer matrixT​(u)T(u)on sites1,2,…,L1,2,\ldots,LasM​(u)\displaystyle M(u):=∏i=1LRa​i​(u)=Ra​L​(u)​⋯​Ra​2​(u)​Ra​1​(u),\displaystyle:=\prod_{i=1}^{L}R_{ai}(u)=R_{aL}(u)\cdots R_{a2}(u)R_{a1}(u),(S.3)T​(u)\displaystyle T(u):=Tra​[M​(u)].\displaystyle:=\mathrm{Tr}_{a}[M(u)].(S.4)

Here and in what follows, when the product symbol∏i=1L\prod_{i=1}^{L}is applied toRRmatrices or related operators, it is understood to be ordered with increasing indices from right to left.
Using the regularity assumptionR​(0)=ΠR(0)=\Piand a simple relationTrj​[Πi​j]=Ii\mathrm{Tr}_{j}[\Pi_{ij}]=I_{i}, the transfer matrix atu=0u=0is equal to the shift operatorSSwhich maps1→21\to 2,2→32\to 3,3→4​…,L→13\to 4\ldots,L\to 1:T​(0)=Tra​[∏i=1LΠa​i]=Tra​[Πa​L​⋯​Πa​2​Πa​1]=S.\displaystyle T(0)=\mathrm{Tr}_{a}\left[\prod_{i=1}^{L}\Pi_{ai}\right]=\mathrm{Tr}_{a}[\Pi_{aL}\cdots\Pi_{a2}\Pi_{a1}]=S.(S.5)

We note that the shift operator can be expressed asS=Π1,2​Π2,3​⋯​ΠL−1,L.\displaystyle S=\Pi_{1,2}\Pi_{2,3}\cdots\Pi_{L-1,L}.(S.6)

A key property of the transfer matrix is its commutativity at different spectral parameters, i.e., for sufficiently smalluuandvvwe have[T​(u),T​(v)]\displaystyle[T(u),T(v)]=0.\displaystyle=0.(S.7)

We derive this relation by insertingI=Ra​b−1​(u−v)​Ra​b​(u−v)I=R^{-1}_{ab}(u-v)R_{ab}(u-v)and applying the Yang–Baxter equation (S.1) repeatedly.
The first step in this procedure isTra,b​[∏iRa​i​(u)​Rb​i​(v)]=\displaystyle\mathrm{Tr}_{a,b}[\prod_{i}R_{ai}(u)R_{bi}(v)]=Tra,b​[Ra​b−1​(u−v)​Ra​b​(u−v)​Ra​L​(u)​Rb​L​(v)​⋯​Ra​2​(u)​Rb​2​(v)​Ra​1​(u)​Rb​1​(v)]\displaystyle\mathrm{Tr}_{a,b}[R^{-1}_{ab}(u-v)R_{ab}(u-v)R_{aL}(u)R_{bL}(v)\cdots R_{a2}(u)R_{b2}(v)R_{a1}(u)R_{b1}(v)]=\displaystyle=Tra,b​[Ra​b−1​(u−v)​Rb​L​(v)​Ra​L​(u)​Ra​b​(u−v)​⋯​Ra​2​(u)​Rb​2​(v)​Ra​1​(u)​Rb​1​(v)],\displaystyle\mathrm{Tr}_{a,b}[R^{-1}_{ab}(u-v)R_{bL}(v)R_{aL}(u)R_{ab}(u-v)\cdots R_{a2}(u)R_{b2}(v)R_{a1}(u)R_{b1}(v)],where we have used the Yang–Baxter equation in the form ofRa​b​(u−v)​Ra​L​(u)​Rb​L​(v)=Rb​L​(v)​Ra​L​(u)​Ra​b​(u−v)R_{ab}(u-v)R_{aL}(u)R_{bL}(v)=R_{bL}(v)R_{aL}(u)R_{ab}(u-v).
By repeating this procedure, we obtain=\displaystyle=Tra,b​[Ra​b−1​(u−v)​Rb​L​(v)​Ra​L​(u)​Rb,L−1​(v)​Ra,L−1​(u)​Ra​b​(u−v)​⋯​Ra​1​(u)​Rb​1​(v)]\displaystyle\mathrm{Tr}_{a,b}[R^{-1}_{ab}(u-v)R_{bL}(v)R_{aL}(u)R_{b,L-1}(v)R_{a,L-1}(u)R_{ab}(u-v)\cdots R_{a1}(u)R_{b1}(v)]⋮\displaystyle\vdots\=\displaystyle=Tra,b​[Ra​b−1​(u−v)​Rb​L​(v)​Ra​L​(u)​⋯​Rb​2​(v)​Ra​2​(u)​Rb​1​(v)​Ra​1​(u)​Ra​b​(u−v)]\displaystyle\mathrm{Tr}_{a,b}[R^{-1}_{ab}(u-v)R_{bL}(v)R_{aL}(u)\cdots R_{b2}(v)R_{a2}(u)R_{b1}(v)R_{a1}(u)R_{ab}(u-v)]=\displaystyle=Tra,b​[Rb​L​(v)​Ra​L​(u)​⋯​Rb​2​(v)​Ra​2​(u)​Rb​1​(v)​Ra​1​(u)​Ra​b​(u−v)​Ra​b−1​(u−v)]\displaystyle\mathrm{Tr}_{a,b}[R_{bL}(v)R_{aL}(u)\cdots R_{b2}(v)R_{a2}(u)R_{b1}(v)R_{a1}(u)R_{ab}(u-v)R^{-1}_{ab}(u-v)]=\displaystyle=Tra,b​[∏iRb​i​(v)​Ra​i​(u)],\displaystyle\mathrm{Tr}_{a,b}[\prod_{i}R_{bi}(v)R_{ai}(u)],(S.8)

which impliesT​(u)​T​(v)=Tra,b​[∏iRa​i​(u)​Rb​i​(v)]=Tra,b​[∏iRb​i​(v)​Ra​i​(u)]=T​(v)​T​(u).\displaystyle T(u)T(v)=\mathrm{Tr}_{a,b}[\prod_{i}R_{ai}(u)R_{bi}(v)]=\mathrm{Tr}_{a,b}[\prod_{i}R_{bi}(v)R_{ai}(u)]=T(v)T(u).(S.9)

In the last step, we have used the cyclicity of the partial trace.

It follows from Eq. (S.7) that[f​(T​(u)),f​(T​(v))]=0[f(T(u)),f(T(v))]=0(S.10)

for anyff.
Expandingf​(T​(u))f(T(u))asf​(T​(u))=∑n=0∞Gn​un\displaystyle f(T(u))=\sum_{n=0}^{\infty}G_{n}u^{n}(S.11)

and comparing the coefficient ofun​vmu^{n}v^{m}in Eq. (S.10), we find[Gn,Gm]=0.\displaystyle[G_{n},G_{m}]=0.(S.12)

In the quantum inverse scattering method, we setf​(x)=ln⁡xf(x)=\ln x.
Then,Gn−1G_{n-1}serves as a conserved quantity, which is computed simply by differentiatingln⁡T​(u)\ln T(u)asQn=(n−1)!​Gn−1=dn−1d​un−1​ln⁡T​(u)|u=0.Q_{n}=(n-1)!G_{n-1}=\left.\frac{d^{n-1}}{du^{n-1}}\ln T(u)\right|_{u=0}.(S.13)

In particular, we regardQ2Q_{2}as the HamiltonianHHand the obtainedQnQ_{n}as thenn-local conserved quantity ofHH.
The conserved quantityQnQ_{n}is indeednn-local for a wide class ofRR-matrices, which is confirmed by the boost operator argument presented in Sec.I.3.

We finally make two technical remarks.
The first concerns the normalization of the transfer matrix atu=0u=0by inserting the shift operatorSS.
SinceT​(0)=ST(0)=S, it is natural to insert the inverse shift operatorS−1S^{-1}and considerln⁡S−1​T​(u)\ln S^{-1}T(u)rather thanln⁡T​(u)\ln T(u)so thatln⁡S−1​T​(0)=0.\displaystyle\ln S^{-1}T(0)=0.(S.14)

This normalization does not affect the local conserved quantities obtained from logarithmic derivatives, since the translation invariance ofT​(u)T(u), namely[S,T​(u)]=0[S,T(u)]=0, impliesln⁡T​(u)=ln⁡S+ln⁡(S−1​T​(u)).\displaystyle\ln T(u)=\ln S+\ln(S^{-1}T(u)).(S.15)

The first term is independent ofuu, and thereforedn−1d​un−1​ln⁡T​(u)|u=0=dn−1d​un−1​ln⁡S−1​T​(u)|u=0\displaystyle\left.\frac{d^{n-1}}{du^{n-1}}\ln T(u)\right|_{u=0}=\left.\frac{d^{n-1}}{du^{n-1}}\ln S^{-1}T(u)\right|_{u=0}(S.16)

holds for alln≥2n\geq 2.

Thus we can use whichever form is more convenient.

The second remark concerns the normalization of each local conserved quantity.
IfQnQ_{n}andQmQ_{m}commute,a​QnaQ_{n}andb​QmbQ_{m}also commute for arbitrary constantsaaandbb, implying that the normalization of each local conserved quantity is arbitrary.
For physical quantum many-body systems, physical conserved quantities should be Hermitian.
IfQ2=Π​RQ_{2}=\Pi R(i.e., Hamiltonian) is Hermitian,
the chargesQnQ_{n}defined in Eq. (S.13) are Hermitian for evennnand anti-Hermitian for oddnn.111This fact follows from the relation with the boost operator:(Qn+1B)†=([B,QnB])†=[(QnB)†,B](Q^{\rm B}_{n+1})^{\dagger}=([B,Q^{\rm B}_{n}])^{\dagger}=[(Q^{\rm B}_{n})^{\dagger},B].Therefore, for oddnn, we should multiplyQnQ_{n}by the imaginary unit in order to obtain a Hermitian conserved quantity.
We define physical conserved quantitiesQnphysQ^{\rm phys}_{n}asQnphys:=−(i)n​Qn=−(i)n​dn−1d​un−1​ln⁡T​(u)|u=0.\displaystyle Q^{\rm phys}_{n}:=-(i)^{n}Q_{n}=-(i)^{n}\left.\frac{d^{n-1}}{du^{n-1}}\ln T(u)\right|_{u=0}.(S.17)

Here, the remaining overall sign or constant factor is a matter of convention, as discussed above.
Some works use the above Hermitian normalizationQnphysQ^{\rm phys}_{n}for the local conserved quantities obtained from the Yang–Baxter equation, or equivalently write them asQnphys=−i​dn−1d​un−1​ln⁡T​(i​u)|u=0.\displaystyle Q^{\rm phys}_{n}=-i\left.\frac{d^{n-1}}{du^{n-1}}\ln T(iu)\right|_{u=0}.(S.18)

## I.2Simple example:R​(u)=Π+u​IR(u)=\Pi+uI

To illustrate how the quantum inverse scattering method works, we present here the simplest nontrivial example:R​(u)=Π+u​I.\displaystyle R(u)=\Pi+uI.(S.19)

As we will see later, thisRR-matrix corresponds to the Heisenberg model forS=1/2S=1/2and the Uimin–Lai–Sutherland model forS=1S=1.
ThisRR-matrix satisfies the Yang–Baxter equation (S.1), as can be verified by the following direct calculation:(Π12+u​I12)​(Π13+(u+v)​I13)​(Π23+v​I23)\displaystyle(\Pi_{12}+uI_{12})(\Pi_{13}+(u+v)I_{13})(\Pi_{23}+vI_{23})=\displaystyle=(123321)+(u+v)​(123231)+(u+v)​(123312)+v​(u+v)​Π12+v​u​Π13+(u+v)​u​Π23+v​(u+v)​u\displaystyle\left(\begin{smallmatrix}1&2&3\\
3&2&1\end{smallmatrix}\right)+(u+v)\left(\begin{smallmatrix}1&2&3\\
2&3&1\end{smallmatrix}\right)+(u+v)\left(\begin{smallmatrix}1&2&3\\
3&1&2\end{smallmatrix}\right)+v(u+v)\Pi_{12}+vu\Pi_{13}+(u+v)u\Pi_{23}+v(u+v)u=\displaystyle=(Π23+v​I23)​(Π13+(u+v)​I13)​(Π12+u​I12),\displaystyle(\Pi_{23}+vI_{23})(\Pi_{13}+(u+v)I_{13})(\Pi_{12}+uI_{12}),(S.20)

where(123∗∗∗)\left(\begin{smallmatrix}1&2&3\\
*&*&*\end{smallmatrix}\right)denotes the permutation operator on three elements.

With thisR​(u)R(u), the term linear inuuinT​(u)T(u)corresponds to the case where, at one site, the identity operator is inserted instead of the swap with the auxiliary siteaa.
Equivalently, this term is obtained by omitting one swap in the cyclic product.
Thus, defining the translation operator that skips site n byUn(1):=Π1,2​Π2,3​⋯​Πn−2,n−1​Πn−1,n+1​Πn+1,n+2​⋯​ΠL−1,L,\displaystyle U^{(1)}_{n}:=\Pi_{1,2}\Pi_{2,3}\cdots\Pi_{n-2,n-1}\Pi_{n-1,n+1}\Pi_{n+1,n+2}\cdots\Pi_{L-1,L},(S.21)

the coefficient ofuuinT​(u)T(u)is given byT(1)=T′​(0)=∑iUi(1).\displaystyle T^{(1)}=T^{\prime}(0)=\sum_{i}U^{(1)}_{i}.(S.22)

Hence, the 2-local conserved quantityQ2Q_{2}associated with thisRR-matrix readsQ2=dd​u​ln⁡T​(u)|u=0=T−1​(0)​T′​(0)=S−1​∑iUi(1)=∑iΠi−1,i.\displaystyle Q_{2}=\left.\frac{d}{du}\ln T(u)\right|_{u=0}=T^{-1}(0)T^{\prime}(0)=S^{-1}\sum_{i}U^{(1)}_{i}=\sum_{i}\Pi_{i-1,i}.(S.23)

Here, the last equality can be checked by tracking the permutation of sites:1,2,⋯,\displaystyle 1,2,\cdots,n−2,n−1,n,n+1,n+2​⋯,L\displaystyle n-2,n-1,n,n+1,n+2\cdots,L→L,1,⋯,\displaystyle\to L,1,\cdots,n−3,n−2,n,n−1,n+1​⋯,L−1\displaystyle n-3,n-2,n,n-1,n+1\cdots,L-1(applying​Un(1))\displaystyle(\text{applying}\ U^{(1)}_{n})→1,2,⋯,\displaystyle\to 1,2,\cdots,n−2,n,n−1,n+1,n+2​⋯,L,\displaystyle n-2,n,n-1,n+1,n+2\cdots,L,(applying​S−1)\displaystyle(\text{applying}\ S^{-1})

which showsS−1​Un(1)=Πn,n+1S^{-1}U^{(1)}_{n}=\Pi_{n,n+1}.

We express the HamiltonianH=Q2phys=Q2=∑iΠi,i+1H=Q^{\rm phys}_{2}=Q_{2}=\sum_{i}\Pi_{i,i+1}in terms of spin operators.
In the case ofS=1/2S=1/2, the Hamiltonian is expressed asH=∑iΠi,i+1=∑i2​𝑺i⋅𝑺i+1+12​Ii,i+1,\displaystyle H=\sum_{i}\Pi_{i,i+1}=\sum_{i}2\bm{S}_{i}\cdot\bm{S}_{i+1}+\frac{1}{2}I_{i,i+1},(S.24)

which is the Heisenberg model up to an overall normalization and an additive constant.
In the case ofS=1S=1, the Hamiltonian is expressed asH=∑iΠi,i+1=∑i𝑺i⋅𝑺i+1+(𝑺i⋅𝑺i+1)2−Ii,i+1,\displaystyle H=\sum_{i}\Pi_{i,i+1}=\sum_{i}\bm{S}_{i}\cdot\bm{S}_{i+1}+(\bm{S}_{i}\cdot\bm{S}_{i+1})^{2}-I_{i,i+1},(S.25)

which is the Uimin–Lai–Sutherland model up to an additive constant.

We next computeQ3Q_{3}associated with thisRR-matrix, which is given byQ3=d2d​u2​ln⁡T​(u)|u=0=T−1​(0)​T′′​(0)−T−2​(0)​T′2​(0).Q_{3}=\left.\frac{d^{2}}{du^{2}}\ln T(u)\right|_{u=0}=T^{-1}(0)T^{\prime\prime}(0)-T^{-2}(0){T^{\prime}}^{2}(0).(S.26)

HereT′′​(0)T^{\prime\prime}(0)is the second derivative ofTTwhich consists of terms where the identity operator is inserted at two sites, while the permutation operator acts between each of the remaining sites and the auxiliary site.
To handle these terms, we defineUn,m(11):=\displaystyle U^{(11)}_{n,m}:=Π1,2​Π2,3​⋯​Πn−2,n−1​Πn−1,n+1​Πn+1,n+2​⋯​Πm−2,m−1​Πm−1,m+1​Πm+1,m+2​⋯​ΠL−1,L\displaystyle\Pi_{1,2}\Pi_{2,3}\cdots\Pi_{n-2,n-1}\Pi_{n-1,n+1}\Pi_{n+1,n+2}\cdots\Pi_{m-2,m-1}\Pi_{m-1,m+1}\Pi_{m+1,m+2}\cdots\Pi_{L-1,L}(n≠m,m±1)\displaystyle(n\neq m,\ m\pm 1)(S.27)Un(2):=\displaystyle U^{(2)}_{n}:=Π1,2​Π2,3​⋯​Πn−2,n−1​Πn−1,n+2​Πn+2,n+3​⋯​ΠL−1,L.\displaystyle\Pi_{1,2}\Pi_{2,3}\cdots\Pi_{n-2,n-1}\Pi_{n-1,n+2}\Pi_{n+2,n+3}\cdots\Pi_{L-1,L}.(S.28)

After multiplying these operators byS−1S^{-1}from the left, they becomeS−1​Un,m(11)=\displaystyle S^{-1}U^{(11)}_{n,m}=Πn−1,n​Πm−1,m,\displaystyle\Pi_{n-1,n}\Pi_{m-1,m},(S.29)S−1​Un(2)=\displaystyle S^{-1}U^{(2)}_{n}=(n−1nn+1nn+1n−1).\displaystyle\left(\begin{smallmatrix}n-1&n&n+1\\
n&n+1&n-1\end{smallmatrix}\right).(S.30)

Using these symbols, the first term in Eq. (S.26) is calculated asT−1​(0)​T′′​(0)=∑n,m​(n≠m,m±1)S−1​Un,m(11)+2​∑nS−1​Un(2)=∑n,m​(n≠m,m±1)Πn,n+1​Πm,m+1+2​∑n(n−1nn+1nn+1n−1).\displaystyle T^{-1}(0)T^{\prime\prime}(0)=\sum_{n,m(n\neq m,m\pm 1)}S^{-1}U^{(11)}_{n,m}+2\sum_{n}S^{-1}U^{(2)}_{n}=\sum_{n,m(n\neq m,m\pm 1)}\Pi_{n,n+1}\Pi_{m,m+1}+2\sum_{n}\left(\begin{smallmatrix}n-1&n&n+1\\
n&n+1&n-1\end{smallmatrix}\right).(S.31)

We next calculate the second term of Eq. (S.26):T−2​(0)​T′2​(0)=S−2​(∑iUi(1))​(∑jUj(1)).\displaystyle T^{-2}(0){T^{\prime}}^{2}(0)=S^{-2}\left(\sum_{i}U^{(1)}_{i}\right)\left(\sum_{j}U^{(1)}_{j}\right).(S.32)

The productUi(1)​Uj(1)U^{(1)}_{i}U^{(1)}_{j}takes different forms depending on the relative positions ofiiandjj.
We therefore distinguish the following cases:S−2​Ui(1)​Uj(1)={S−1​Ui−1,j(11)=Πi−2,i−1​Πj−1,ji≠j,j+1,j+2S−2​(Uj(1))2=(j−2j−1jjj−2j−1)i=jS−2​Uj+1(1)​Uj(1)=Ii=j+1S−2​Uj+2(1)​Uj(1)=(j−1jj+1jj+1j−1)i=j+2\displaystyle S^{-2}U^{(1)}_{i}U^{(1)}_{j}=\begin{cases}S^{-1}U^{(11)}_{i-1,j}=\Pi_{i-2,i-1}\Pi_{j-1,j}&i\neq j,j+1,j+2\\
S^{-2}(U^{(1)}_{j})^{2}=\left(\begin{smallmatrix}j-2&j-1&j\\
j&j-2&j-1\end{smallmatrix}\right)&i=j\\
S^{-2}U^{(1)}_{j+1}U^{(1)}_{j}=I&i=j+1\\
S^{-2}U^{(1)}_{j+2}U^{(1)}_{j}=\left(\begin{smallmatrix}j-1&j&j+1\\
j&j+1&j-1\end{smallmatrix}\right)&i=j+2\end{cases}(S.33)

Combining them, we arrive atQ3=T−1​(0)​T′′​(0)−T−2​(0)​T′2​(0)=∑j[(j−1jj+1j+1j−1j)−(j−1jj+1jj+1j−1)],\displaystyle Q_{3}=T^{-1}(0)T^{\prime\prime}(0)-T^{-2}(0){T^{\prime}}^{2}(0)=\sum_{j}\left[\left(\begin{smallmatrix}j-1&j&j+1\\
j+1&j-1&j\end{smallmatrix}\right)-\left(\begin{smallmatrix}j-1&j&j+1\\
j&j+1&j-1\end{smallmatrix}\right)\right],(S.34)

where we dropped an additive constant proportional to the identity operator.

In the case ofS=1/2S=1/2, the physical 3-local conserved quantityQ3physQ^{\rm phys}_{3}is expressed in terms of spin operators asQ3phys=i​Q3=−4​∑j𝑺j−1⋅(𝑺j×𝑺j+1),\displaystyle Q^{\rm phys}_{3}=iQ_{3}=-4\sum_{j}\bm{S}_{j-1}\cdot(\bm{S}_{j}\times\bm{S}_{j+1}),(S.35)

where×\timesis the cross product.

## I.3Boost operator

As seen in the preceding subsections, the local conserved quantities are obtained from the logarithmic derivatives of the transfer matrix.
However, as also seen in the same subsections, their computations are complicated, particularly for largenn.
We here provide an alternative method to obtain local conserved quantities; the boost operator method.
The boost operatorBBis defined asB=∑jj​hj,j+1.\displaystyle B=\sum_{j}jh_{j,j+1}.(S.36)

Here, following the usual convention[48]we do not care about the effect of boundaries since it is irrelevant to our analysis (see Sec.IV.2on this point).

We first suppose that a Hamiltonian has a correspondingRR-matrix satisfying the Yang–Baxter equation (S.1).
We differentiate the Yang–Baxter equation (S.1) with respect tovvand setv=0v=0.
Multiplying the resulting equation byΠ23\Pi_{23}from the left, we obtain theSutherland equation(dd​u​R13​(u))​R12​(u)−R13​(u)​(dd​u​R12​(u))=[R13​(u)​R12​(u),h23],\left(\frac{d}{du}R_{13}(u)\right)R_{12}(u)-R_{13}(u)\left(\frac{d}{du}R_{12}(u)\right)=[R_{13}(u)R_{12}(u),h_{23}],(S.37)

where we usedR​(0)=ΠR(0)=\Pianddd​u​R​(u)|u=0=Π​h\left.\frac{d}{du}R(u)\right|_{u=0}=\Pi h, which is shown in the next subsection (Sec.I.4).
We next relabel the spaces as1→a1\to a,2→i2\to i, and3→i+13\to i+1.
Multiplying the resulting equation by∏j≤i−1Ra​j​(u)\prod_{j\leq i-1}R_{aj}(u)from the right and by∏j≥i+2Ra​j​(u)\prod_{j\geq i+2}R_{aj}(u)from the left, we have∏j≥i+2Ra​j​(u)​(dd​u​Ra,i+1​(u))​∏j≤iRa​j​(u)−∏j≥i+1Ra​j​(u)​(dd​u​Ra​i​(u))​∏j≤i−1Ra​j​(u)=[∏jRa​j​(u),hi,i+1].\displaystyle\prod_{j\geq i+2}R_{aj}(u)\left(\frac{d}{du}R_{a,i+1}(u)\right)\prod_{j\leq i}R_{aj}(u)-\prod_{j\geq i+1}R_{aj}(u)\left(\frac{d}{du}R_{ai}(u)\right)\prod_{j\leq i-1}R_{aj}(u)=[\prod_{j}R_{aj}(u),h_{i,i+1}].(S.38)

Finally, multiplying byiiand summing overii, we finddd​u​∏jRa​j​(u)=[B,∏jRa​j​(u)].\displaystyle\frac{d}{du}\prod_{j}R_{aj}(u)=[B,\prod_{j}R_{aj}(u)].(S.39)

Here we used the telescoping cancellation.
Ignoring boundary terms and taking its trace overaa, we arrive at[B,T​(u)]=dd​u​T​(u).[B,T(u)]=\frac{d}{du}T(u).(S.40)

The obtained relation (S.40) directly implies[B,Tm​(u)]=∑l=0m−1Tl​(u)​[B,T​(u)]​Tm−l−1​(u)=∑l=0m−1Tl​(u)​dd​u​T​(u)​Tm−l−1​(u)=dd​u​Tm​(u).[B,T^{m}(u)]=\sum_{l=0}^{m-1}T^{l}(u)[B,T(u)]T^{m-l-1}(u)=\sum_{l=0}^{m-1}T^{l}(u)\frac{d}{du}T(u)T^{m-l-1}(u)=\frac{d}{du}T^{m}(u).(S.41)

Thus, in particular we find[B,ln⁡T​(u)]=dd​u​ln⁡T​(u),[B,\ln T(u)]=\frac{d}{du}\ln T(u),(S.42)

which is demonstrated by expandingln⁡T\ln Twith respect toTTand applying Eq. (S.41) to each order.
Using the definition Eq. (S.13), we obtain the following recursive relation for the local conserved quantities:[B,Qm]=dm−1d​um−1​[B,ln⁡T​(u)]|u=0=dmd​um​ln⁡T​(u)|u=0=Qm+1.[B,Q_{m}]=\left.\frac{d^{m-1}}{du^{m-1}}[B,\ln T(u)]\right|_{u=0}=\left.\frac{d^{m}}{du^{m}}\ln T(u)\right|_{u=0}=Q_{m+1}.(S.43)

This relation guarantees thatQmQ_{m}is indeed anmm-local quantity.

We next consider a general HamiltonianHHfor which the existence of the Yang–Baxter equation is not assumed.
In this case, the quantityQmQ_{m}obtained by Eq. (S.43) is no longer proven to be a conserved quantity.
To distinguish the quantities obtained by the boost operator from those obtained by the logarithmic derivatives of the transfer matrix, we denote the former ones byQmBQ^{\rm B}_{m}:Qm+1B:=[B,QmB],Q2B:=H.Q^{\rm B}_{m+1}:=[B,Q^{\rm B}_{m}],\hskip 15.0ptQ^{\rm B}_{2}:=H.(S.44)

The first boost-generated charge isQ3B=[B,H]=−∑i[hi,i+1,hi+1,i+2].\displaystyle Q^{\rm B}_{3}=[B,H]=-\sum_{i}[h_{i,i+1},h_{i+1,i+2}].(S.45)

For a general Hamiltonian,Q3BQ^{\rm B}_{3}is not necessarily conserved.
The conservation ofQ3BQ^{\rm B}_{3}is expressed as[[B,H],H]=0.[[B,H],H]=0.(S.46)

This condition is equivalent to the Reshetikhin condition (S.62)[20].

If Eq. (S.46) holds, thenQ4BQ^{\rm B}_{4}is also the 4-local conserved quantity, which is proven as[Q4B,H]=[[B,Q3B],H]=[B,[Q3B,H]]−[Q3B,[B,H]]=0,\displaystyle[Q^{\rm B}_{4},H]=[[B,Q^{\rm B}_{3}],H]=[B,[Q^{\rm B}_{3},H]]-[Q^{\rm B}_{3},[B,H]]=0,(S.47)

where we used the Jacobi identity:[[a,b],c]+[[b,c],a]+[[c,a],b]=0.\displaystyle[[a,b],c]+[[b,c],a]+[[c,a],b]=0.(S.48)

Similarly, if we have already established[QkB,QlB]=0[Q^{\rm B}_{k},Q^{\rm B}_{l}]=0for allk+l≤pk+l\leq p, then for anyn+m=p+1n+m=p+1we have[QnB,QmB]=[[B,Qn−1B],QmB]=[B,[Qn−1B,QmB]]−[Qn−1B,[B,QmB]]=−[Qn−1B,Qm+1B].\displaystyle[Q^{\rm B}_{n},Q^{\rm B}_{m}]=[[B,Q^{\rm B}_{n-1}],Q^{\rm B}_{m}]=[B,[Q^{\rm B}_{n-1},Q^{\rm B}_{m}]]-[Q^{\rm B}_{n-1},[B,Q^{\rm B}_{m}]]=-[Q^{\rm B}_{n-1},Q^{\rm B}_{m+1}].(S.49)

In particular,Qp−1BQ^{\rm B}_{p-1}conserves ifp+1p+1is even, which is shown as[Qp−1B,H]=−[Qp−2B,Q3B]=⋯=(−1)(p+1)/2​[Q(p+1)/2B,Q(p+1)/2B]=0.\displaystyle[Q^{\rm B}_{p-1},H]=-[Q^{\rm B}_{p-2},Q^{\rm B}_{3}]=\cdots=(-1)^{(p+1)/2}[Q^{\rm B}_{(p+1)/2},Q^{\rm B}_{(p+1)/2}]=0.(S.50)

The conservation ofQmBQ^{\rm B}_{m}with generalm≥5m\geq 5has recently been demonstrated by Hokkyo.

## Lemma S.1(Hokkyo[23](same as Lemma2in the main article)).

Consider a translation-invariant nearest-neighbor interaction HamiltonianH=∑ihi,i+1H=\sum_{i}h_{i,i+1}, whose eigenstates span the state space in consideration.
Suppose thatQ3B=[B,H]Q^{\rm B}_{3}=[B,H]is a conserved quantity;[Q3B,H]=0[Q^{\rm B}_{3},H]=0.
Then,QmBQ^{\rm B}_{m}given by Eq. (S.44) are translation-invariant and commute with each other;[QmB,QnB]=0[Q^{\rm B}_{m},Q^{\rm B}_{n}]=0for anym,n≥2m,n\geq 2.

Although the original proof by Hokkyo applies only to Hermitian systems with a finite-dimensional local Hilbert space, we here present a slightly generalized proof.
In the following proof, we require that the set of the eigenstates of the total HamiltonianHHspans the entire state space in consideration.
This covers not only Hermitian spin systems but also bosonic systems with the conservation of the particle number and diagonalizable non-Hermitian systems.

## Proof.

We prove thatQmBQ^{\rm B}_{m}is translation-invariant and[QmB,H]=0[Q^{\rm B}_{m},H]=0by induction onmm.

We first show the translation invariance ofQm+1BQ^{\rm B}_{m+1}under the assumption of[QmB,H]=0[Q^{\rm B}_{m},H]=0and[S,QmB]=0[S,Q^{\rm B}_{m}]=0, whereSSis the one-site shift operator.
This follows immediately from[S,Qm+1B]=[S,[B,QmB]]=[[S,B],QmB]+[B,[S,QmB]]=[−H​S,QmB]=0,\displaystyle[S,Q^{\rm B}_{m+1}]=[S,[B,Q^{\rm B}_{m}]]=[[S,B],Q_{m}^{B}]+[B,[S,Q_{m}^{B}]]=[-HS,Q^{\rm B}_{m}]=0,(S.51)

where we used[B,S]=H​S[B,S]=HSin the third equality.

We next show the conservation ofQm+1BQ^{\rm B}_{m+1}under the assumption of[QmB,H]=0[Q^{\rm B}_{m},H]=0and[S,Qm+1B]=0[S,Q^{\rm B}_{m+1}]=0.
Using the Jacobi identity, we have[H,[H,Qm+1B]]=[H,[H,[B,QmB]]]=[H,[[H,B],QmB]]=−[[H,Q3B],QmB]−[Q3B,[H,QmB]]=0.\displaystyle[H,[H,Q^{\rm B}_{m+1}]]=[H,[H,[B,Q^{\rm B}_{m}]]]=[H,[[H,B],Q^{\rm B}_{m}]]=-[[H,Q^{\rm B}_{3}],Q^{\rm B}_{m}]-[Q^{\rm B}_{3},[H,Q^{\rm B}_{m}]]=0.(S.52)

Here, we notice that[H,[H,Qm+1B]]=0[H,[H,Q^{\rm B}_{m+1}]]=0implies[H,Qm+1B]=0[H,Q^{\rm B}_{m+1}]=0, since the action of[H,⋅][H,\cdot\ ]maps nonzero off-diagonal elements with respect to the eigenstates ofHHonto nonzero ones (i.e., ifQm+1BQ^{\rm B}_{m+1}has a nonzero off-diagonal element, then the same off-diagonal element of[H,Qm+1B][H,Q^{\rm B}_{m+1}]is still nonzero, implying[H,[H,Qm+1B]]≠0[H,[H,Q^{\rm B}_{m+1}]]\neq 0).
To prove this in a more rigorous manner, we employ the energy eigenbasis{|ψi⟩}\{\ket{\psi_{i}}\}which spans the entire state space in consideration.
(In the non-Hermitian case, we employ the bases of left and right energy eigenstates{⟨ψi|}\{\bra{\psi_{i}}\}and{|ψi⟩}\{\ket{\psi_{i}}\}, which are not necessarily conjugate to each other.)
Let|ψi⟩\ket{\psi_{i}}and|ψj⟩\ket{\psi_{j}}be energy eigenstates with eigenenergiesEiE_{i}andEjE_{j}(Ei≠EjE_{i}\neq E_{j}).
Then we have⟨ψi|​[H,[H,Qm+1B]]​|ψj⟩=⟨ψi|H2​Qm+1B+Qm+1B​H2−2​H​Qm+1B​H|ψj⟩=(Ei−Ej)2​⟨ψi|Qm+1B|ψj⟩.\displaystyle\bra{\psi_{i}}[H,[H,Q^{\rm B}_{m+1}]]\ket{\psi_{j}}=\braket{\psi_{i}|H^{2}Q^{\rm B}_{m+1}+Q^{\rm B}_{m+1}H^{2}-2HQ^{\rm B}_{m+1}H|\psi_{j}}=(E_{i}-E_{j})^{2}\braket{\psi_{i}|Q^{\rm B}_{m+1}|\psi_{j}}.(S.53)

Assuming[H,[H,Qm+1B]]=0[H,[H,Q^{\rm B}_{m+1}]]=0, we find⟨ψi|Qm+1B|ψj⟩=0\braket{\psi_{i}|Q^{\rm B}_{m+1}|\psi_{j}}=0wheneverEi≠EjE_{i}\neq E_{j}.
This implies thatQm+1BQ^{\rm B}_{m+1}has no off-diagonal blocks with respect to the energy eigenspaces, meaning[Qm+1B,H]=0[Q^{\rm B}_{m+1},H]=0.
Hence, assuming[Q3B,H]=0[Q^{\rm B}_{3},H]=0, we recursively obtain[QmB,H]=0[Q^{\rm B}_{m},H]=0for allmm, which completes the proof.
∎

Note that Hokkyo also showed a sufficient condition forQmBQ^{\rm B}_{m}to be anmm-local conserved quantity.
We first decompose the local Hamiltonianhhinto two-site termsh(2)h^{(2)}and one-site termsh(1)h^{(1)}.
Consider a mapf​(A):=[A⊗I,h(2)]f(A):=[A\otimes I,h^{(2)}], which maps an operator on a single site onto that on two sites.
Require that the kernel of this map is{c​I|c∈ℂ}\{cI|c\in\mathbb{C}\}.
In other words, the mapffis injective up to a constant multiple of the identity operator.
Then, it is shown thatQmBQ^{\rm B}_{m}is indeed anmm-local quantity, i.e.,QmBQ^{\rm B}_{m}is a shift sum of a quantity whose contiguous support is strictlymmsites.

## I.4Expansion ofRR-matrix and Reshetikhin condition

Consider anRR-matrix satisfying the Yang–Baxter equation (S.1).
We consider a series expansion of theRR-matrix in terms ofuu.
Since the zeroth order is the permutation operator due to the regularity, it is useful to introduce an alternate form ofRR-matrixRˇ​(u):=Π​R​(u),\displaystyle\check{R}(u):=\Pi R(u),(S.54)

whose series expansion is given asRˇ​(u)=I+∑n=1∞Rˇ(n)​un.\displaystyle\check{R}(u)=I+\sum_{n=1}^{\infty}\check{R}^{(n)}u^{n}.(S.55)

The relationQ2=T−1​(0)​T′​(0)=∑iRˇi,i+1(1)Q_{2}=T^{-1}(0)T^{\prime}(0)=\sum_{i}\check{R}^{(1)}_{i,i+1}impliesRˇ(1)=h,\displaystyle\check{R}^{(1)}=h,(S.56)

where we denoteQ2=H=∑ihi,i+1Q_{2}=H=\sum_{i}h_{i,i+1}.
Thus, the series expansion ofRˇ​(u)\check{R}(u)readsRˇ​(u)=I+u​h+u2​Rˇ(2)+u3​Rˇ(3)+⋯.\check{R}(u)=I+uh+u^{2}\check{R}^{(2)}+u^{3}\check{R}^{(3)}+\cdots.(S.57)

This braidedRR-matrix satisfies a modulated version of the Yang–Baxter equationRˇ12​(u)​Rˇ23​(u+v)​Rˇ12​(v)=Rˇ23​(v)​Rˇ12​(u+v)​Rˇ23​(u).\check{R}_{12}(u)\check{R}_{23}(u+v)\check{R}_{12}(v)=\check{R}_{23}(v)\check{R}_{12}(u+v)\check{R}_{23}(u).(S.58)

We insert Eq. (S.57) into the Yang–Baxter equation (S.58) and compare the coefficients ofuuandvv.

The coefficient ofu​vuvin Eq. (S.58) reads2​Rˇ23(2)−h232=2​Rˇ12(2)−h122,\displaystyle 2\check{R}^{(2)}_{23}-h^{2}_{23}=2\check{R}^{(2)}_{12}-h^{2}_{12},(S.59)

which impliesRˇ(2)=12​h2.\displaystyle\check{R}^{(2)}=\frac{1}{2}h^{2}.(S.60)

The coefficients ofu​v2uv^{2}readsRˇ12(3)−Rˇ23(3)+16​[h12+h23,[h12,h23]]−16​h123+16​h233=0.\check{R}^{(3)}_{12}-\check{R}^{(3)}_{23}+\frac{1}{6}[h_{12}+h_{23},[h_{12},h_{23}]]-\frac{1}{6}h^{3}_{12}+\frac{1}{6}h^{3}_{23}=0.(S.61)

Defining unknown 2-support operatorX:=6​Rˇ(3)−h3X:=6\check{R}^{(3)}-h^{3}, we arrive at theReshetikhin condition[31,29][h12+h23,[h12,h23]]=X23−X12.[h_{12}+h_{23},[h_{12},h_{23}]]=X_{23}-X_{12}.(S.62)

Since not every local Hamiltonianhhadmits a solution toXX(i.e., the left-hand side of Eq. (S.62) is not necessarily telescopic), the Reshetikhin condition is thus the lowest-order nontrivial relation of the Yang–Baxter equation.
If a local Hamiltonianhhsatisfies the Reshetikhin condition, Eq. (S.61) can be solved by choosingRˇ(3)=16​(h3+X).\displaystyle\check{R}^{(3)}=\frac{1}{6}(h^{3}+X).(S.63)

On the other hand, if a local Hamiltonianhhdoes not satisfy the Reshetikhin condition, then noRˇ(3)\check{R}^{(3)}satisfies the equation (S.61), meaning that this local Hamiltonianhhcannot be obtained from anRR-matrix satisfying the Yang–Baxter equation.
Thus, the Reshetikhin condition (S.62) provides a useful test, namely a necessary condition, for Yang–Baxter solvability.

Of course, the Reshetikhin condition only ensures the presence ofRˇ(3)\check{R}^{(3)}, and thus there may exist a local Hamiltonianhhwhich has a solution toRˇ(3)\check{R}^{(3)}but does not have a solution to a higher coefficientRˇ(n)\check{R}^{(n)}.
In this case, this local Hamiltonianhhpasses the Reshetikhin condition but does not have anRR-matrix satisfying the Yang–Baxter equation.
It can be shown thatRˇ(n)\check{R}^{(n)}for evennnalways has a solution if all the lower conditions thannnare satisfied.
On the other hand, whetherRˇ(n)\check{R}^{(n)}for oddnnhas a solution is highly nontrivial, which appears to provide further additional conditions on the local Hamiltonianhh.

We see what happens in the case ofn=4n=4and 5.
Theu​v3uv^{3}coefficient always admits the solutionRˇ(4)=124​(h4+2​(h​X+X​h))\displaystyle\check{R}^{(4)}=\frac{1}{24}(h^{4}+2(hX+Xh))(S.64)

as long as the Reshetikhin condition is satisfied, whereXXis the operator employed in the Reshetikhin condition.
In other words, theu​v3uv^{3}coefficient does not impose an additional constraint onhh.

The second nontrivial condition is given as the coefficients ofu​v4uv^{4}, which reads[h123+h233+3​(X12+X23),[h12,h23]]+3​(h12​[[h12,h23],h12]​h12+h23​[[h12,h23],h23]​h23)\displaystyle[h_{12}^{3}+h_{23}^{3}+3(X_{12}+X_{23}),[h_{12},h_{23}]]+3(h_{12}[[h_{12},h_{23}],h_{12}]h_{12}+h_{23}[[h_{12},h_{23}],h_{23}]h_{23})+(h12​h23+h23​h12)​Δ​X+Δ​X​(h12​h23+h23​h12)−2​(h12​Δ​X​h23+h23​Δ​X​h12)\displaystyle+(h_{12}h_{23}+h_{23}h_{12})\mathit{\Delta}X+\mathit{\Delta}X(h_{12}h_{23}+h_{23}h_{12})-2(h_{12}\mathit{\Delta}Xh_{23}+h_{23}\mathit{\Delta}Xh_{12})=\displaystyle=Y23−Y12.\displaystyle Y_{23}-Y_{12}.(S.65)

Here, we definedΔ​X:=X23−X12\mathit{\Delta}X:=X_{23}-X_{12}.
This condition is sometimes called thesecond integrability test[8], in contrast to the Reshetikhin condition as the first integrability test.
If the second Reshetikhin condition is satisfied, we have a solution toRˇ(5)\check{R}^{(5)}asRˇ(5)=1120​(h5+Y+2​(X​h2+h2​X)+6​h​X​h).\displaystyle\check{R}^{(5)}=\frac{1}{120}(h^{5}+Y+2(Xh^{2}+h^{2}X)+6hXh).(S.66)

Similarly, the coefficients ofu​v2​muv^{2m}provide a nontrivial constraint onhh, which is sometimes referred to as themm-th integrability test.

It is noteworthy that the higher-order Reshetikhin conditions including the original one do not manifestly imply the Yang–Baxter equation.
All the higher-order Reshetikhin conditions are equivalent to the Sutherland equation (S.37).
The Sutherland equation is obtained by differentiating the Yang–Baxter equation with respect to one of its two parameters and then setting that parameter to zero.
In this process, some information may be lost.
More precisely, the Sutherland equation is equivalent only to theu​vnuv^{n}coefficients of the Yang–Baxter equation for allnn.
Thus, theuk​vlu^{k}v^{l}coefficients withk,l≥2k,l\geq 2are, in principle, not captured by the Sutherland equation or by the higher-order Reshetikhin conditions.

In summary, although the equivalence of the Sutherland equation and the Yang–Baxter equation is strongly expected[14]and declared without proof[56], there remains a gap between these two.
One of our results (Lemma4) fills this gap and establishes the equivalence of the Sutherland equation and the Yang–Baxter equation.

## IIEquivalence of the Reshetikhin condition and the Yang–Baxter equation

## II.1Main theorem

As seen in the preceding section, whether a given local Hamiltonianhhhas a correspondingRR-matrix is a highly nontrivial problem.
Since the Reshetikhin condition is a simple necessary condition, higher-order integrability tests, which come from the coefficients ofu​vkuv^{k}with evenkkin the Yang–Baxter equation, appear to impose additional constraints onhh[8,7,19,35].
More seriously, even if all the higher-order Reshetikhin conditions are satisfied, conditions coming from the coefficients ofuk​vlu^{k}v^{l}withl,k≥2l,k\geq 2may impose further constraints.

Surprisingly, we establish that the Reshetikhin condition is the only constraint on the local Hamiltonianhhto fulfill the Yang–Baxter equation.
In other words, the lowest-order Yang–Baxter equation and the full-order Yang–Baxter equation impose the same constraints onhh, and all the higher-order Reshetikhin conditions and further conditions coming from the coefficients ofuk​vlu^{k}v^{l}are in fact redundant.

## Theorem S.2(Theorem1in the main article).

Consider a one-dimensional, translation-invariant spin chain with nearest-neighbour interactions, whose local Hilbert space is finite-dimensional.
Suppose that a two-site Hamiltonian densityhhsatisfies the Reshetikhin condition (4) and that the eigenstates ofH=∑i=1Lhi,i+1H=\sum_{i=1}^{L}h_{i,i+1}span the state space under consideration.
Then there exists a regularRR-matrix, analytic nearu=0u=0, satisfying the Yang–Baxter equation (1) whose corresponding transfer matrix reproducesHHas its logarithmic derivative.

This theorem establishes that the Reshetikhin condition and the Yang–Baxter equation are equivalent, resolving conjectures raised independently by Kulish and Sklyanin[31], Öttinger and Honerkamp[37], and Jimbo and Miwa[25], and later reformulated by Grabowski and Mathieu[20]in the affirmative.
In other words, the Reshetikhin condition is a simple necessary and sufficient condition for the Yang–Baxter equation, which greatly reduces the work required to search for and identify novel integrable models compared to computational search ofRR-matrix[32].

The latter condition, namely the completeness of the set of energy eigenstates, is satisfied for a wide class of Hamiltonians.
The simplest example is a Hermitian Hamiltonian with a finite-dimensional local Hilbert space, since the total Hilbert space is then finite-dimensional.
Even for a non-Hermitian Hamiltonian, the same condition is satisfied whenever the Hamiltonian is diagonalizable.

This theorem has implications in various directions.
The first concerns a refinement of the notion of quantum integrability.
In classical Hamiltonian systems, the Liouville–Arnold theorem establishes a fundamental connection between solvability and the existence of sufficiently many conserved quantities.
By contrast, no universally accepted definition of integrability has been established for quantum many-body systems[51,11], and the connection between Yang–Baxter solvability and the existence of local conserved quantities has not yet been fully clarified.
Our theorem bridges the Yang–Baxter solvability and local conserved quantities, since the Reshetikhin condition is equivalent to the conservation of the three-local quantityQ3BQ^{\rm B}_{3}generated by the boost operator, namely[Q3B,H]=0[Q^{\rm B}_{3},H]=0.
A particularly important case is an isotropic spin chain.
In this setting, combining the present result with the dichotomy theorem[42]shows that Yang–Baxter solvability is equivalent to the existence of an infinite family of local conserved quantities, providing a quantum counterpart of the Liouville–Arnold theorem, whereas for general quantum chains, the analogous but slightly weaker equivalence holds between Yang–Baxter solvability and the existence of an infinite hierarchy of local conserved quantities generated recursively by the boost operator.

The second implication concerns the experimental verification of solvability.
Solvability is usually regarded as a purely mathematical notion, and hence as being inaccessible to direct experimental tests.
However, our result establishes that Yang–Baxter integrability can be tested experimentally through measurements of the total energy current[57,30](i.e., whether the total energy current is conserved in time or not).
This provides an unexpected route to testing Yang–Baxter solvability in the laboratory.

## II.2Historical Background and Related Works

Over the past century, the study of exactly solvable models developed along several initially distinct lines, including the Bethe ansatz[5], two-dimensional lattice models[36,3], factorized scattering[54], and the classical inverse scattering method.
The establishment of the quantum inverse scattering method[47,45,31]brought these developments into a common algebraic framework.
In this framework, anRR-matrix satisfying the Yang–Baxter equation generates a commuting family of transfer matrices.
Their spectral problem can be treated using the algebraic Bethe ansatz, while the Hamiltonian and an infinite family of local conserved charges are obtained from logarithmic derivatives of the transfer matrix.
Within the quantum inverse scattering method, the local conserved chargesQnQ_{n}are obtained as logarithmic derivatives of the transfer matrix.
The boost operator, introduced and developed by Tetel’man[48]and Thacker[49], provided a complementary description of the same hierarchy by relating the charges directly throughQn+1B=[B,QnB].Q_{n+1}^{B}=[B,Q_{n}^{B}].For models constructed from the Yang–Baxter equation, these operators coincide, up to normalization conventions, with the charges generated by the transfer matrix and mutually commute.
Thus, the quantum inverse scattering method not only unified techniques that had previously appeared specific to individual solvable models, but also identified the Yang–Baxter equation as their common underlying structure.

Once this framework had been established, it was natural to ask the converse question: whether the lowest nontrivial condition obtained by expanding the Yang–Baxter equation around the regular point, namely the Reshetikhin condition (S.62), already implies the full Yang–Baxter equation.
This question was independently raised in several forms in the early 1980s.
Reshetikhin derived the lowest nontrivial compatibility condition for reconstructing a regular Yang–Baxter family from its Hamiltonian density, though this observation was not published separately by Reshetikhin.
This idea appeared in the paper by Kulish and Sklyanin[31], where it was attributed to Reshetikhin as a private communication.
Kulish and Sklyanin explicitly stated that whether the Reshetikhin condition is sufficient for the Yang–Baxter equation remained an open problem.
Öttinger and Honerkamp[37]studied a system with aℤ2×ℤ2\mathbb{Z}_{2}\times\mathbb{Z}_{2}state space.
Based on a comparison between the number of independent equations and the number of unknown variables, they argued that the Reshetikhin condition is sufficient for the Yang–Baxter equation in this setting.
They further suggested that the Reshetikhin condition might remain sufficient beyond this particular class.
Jimbo and Miwa[25]also conjectured that the Reshetikhin condition is sufficient for the Yang–Baxter equation.

We here clarify the relation between the above conjecture and the name “tangential star–triangle hypothesis.”
For this purpose, it is useful to distinguish the following two related but qualitatively different questions:
- (A)

We do not assume the existence of anRR-matrix satisfying the Yang–Baxter equation.
Given a local Hamiltonian densityhhsatisfying the Reshetikhin condition, we ask whether there exists a suitableRR-matrix satisfying the Yang–Baxter equation that reproduces the HamiltonianH=∑ihi,i+1H=\sum_{i}h_{i,i+1}.
- (B)

We assume the existence of anRR-matrix satisfying the Yang–Baxter equation.
From thisRR-matrix, we obtain the HamiltonianH=∑ihi,i+1H=\sum_{i}h_{i,i+1}.
We then ask whether theRR-matrix can be reconstructed from the information of the HamiltonianHH.

These are qualitatively different questions.
Indeed, if the existence of a suitableRR-matrix is presupposed, then the orderuk​vlu^{k}v^{l}of the Yang–Baxter equation necessarily admits the corresponding coefficientRˇ(l+k)\check{R}^{(l+k)}as a solution.
Thus, the reconstruction of allRˇ(n)\check{R}^{(n)}from the local Hamiltonian densityhhalways succeeds once the existence of the underlyingRR-matrix is assumed.
In this sense, question (B) has an affirmative answer essentially by construction.
In contrast, the nontrivial issue in question (A) is whether, starting only from a Hamiltonian density satisfying the Reshetikhin condition, the orderuk​vlu^{k}v^{l}of the Yang–Baxter equation admits a consistent solution forRˇ(l+k)\check{R}^{(l+k)}for allllandkk.
The conjectures raised by Öttinger and Honerkamp and by Jimbo and Miwa concern question (A).
The terminology used in the literature is, however, somewhat ambiguous.
Idzumi, Tokihiro, and Arai[24]formulated question (B) and referred to it as the tangential star–triangle hypothesis, while at the same time attributing the hypothesis to Jimbo and Miwa.
Somewhat puzzlingly, however, they also sought to determine all Yang–Baxter-solvableRR-matrices within a certain class, which is closer in spirit to question (A).
More recent papers have likewise used the term in both senses.
Hokkyo[23]and Paletta and Prosen[38]use the term “tangential star–triangle hypothesis” in the sense of question (A).
We note that Paletta[39]uses it in the sense of question (B), although the broader objective of that work is again closely related to question (A).
Thus, question (A) appears to be more closely aligned with the original conjectural problem associated with the Reshetikhin condition, whereas the term “tangential star–triangle hypothesis” has also been used for the formally distinct question (B).
To avoid this terminological ambiguity, we do not use the term tangential star–triangle hypothesis in this paper.

Beyond the terminological issue, the Reshetikhin condition was subsequently used as a practical first test for Yang–Baxter solvability in the classification of Hamiltonians and the search for new integrable models.
A typical procedure is first to test candidate Hamiltonians against the Reshetikhin condition, and if a Hamiltonian passes this test, one then attempts to construct a correspondingRR-matrix satisfying the Yang–Baxter equation.
Kennedy[29]and Batchelor and Yung[2]numerically examined all isotropic nearest-neighbor spin chains for spinsS≤13.5S\leq 13.5.
They found that every model satisfying the Reshetikhin condition belonged to one of four known infinite Yang–Baxter-solvable families, together with one exceptional model atS=3S=3.
Similar classification programs were carried out for several classes of symmetricS=1S=1spin chains[24,35,6,19]and for4×44\times 4Hamiltonians[21,7,8,50,17,14,16,34].
For these classification problems, Bibikov[7]and Fonseca et al.[19]developed a systematic procedure for comparing the Yang–Baxter equation order by order in its series expansion.
Vieira[50]supposed the Sutherland equation and solved it to obtainRR-matrices satisfying the Yang–Baxter equation.
This approach was subsequently employed and further developed in a series of works by de Leeuw and collaborators.
More recently, a method for proving the absence of nontrivial local conserved quantities was developed[43], and using this method, direct classifications were obtained for inversion-symmetric nearest-neighbor spin-1/21/2chains[52,44,53]and for spin-11bilinear-biquadratic chains[40,22].
Motivated by this accumulated evidence from old to new, de Leeuw et al.[14]reiterated the conjecture that the Reshetikhin condition provides a sufficient condition for the Yang–Baxter equation, and identified a proof of this statement in full generality as an important open problem.

Toward resolving this conjecture, various studies have sought to bridge the remaining gap in this converse problem.
Grabowski and Mathieu[20]focused on local conserved quantities and revisited the Reshetikhin condition in the form[Q2,Q3B]=0[Q_{2},Q_{3}^{B}]=0, namely, as the conservation of the first nontrivial charge generated by the boost operator.
They thereby re-emphasized its usefulness as a practical test of integrability and highlighted its connection to the existence of an infinite family of local conserved quantities.
More recently, Hokkyo[23]proved that this single conservation law implies the conservation of all boost-generated quantitiesQnBQ_{n}^{B}, as well as their mutual commutativity.
For a historical review of this approach, we refer the reader to ref.[23].
Hokkyo’s result plays an important role in our reconstruction of anRR-matrix satisfying the Yang–Baxter equation.

Another important approach is Baxterization, in which anRR-matrix satisfying the Yang–Baxter equation is constructed from a suitable local algebra generated by the local Hamiltonian.
A pioneering result in this direction was obtained by Jimbo[26].
He constructed anRR-matrix satisfying the Yang–Baxter equation from a generator of the Hecke algebra.
Jones[27]formulated this idea as a general procedure and coined the term “Baxterization”.
This algebraic framework was connected explicitly to local Hamiltonians by Alcarazet al.[1].
They assumed that the local Hamiltonian density generates a representation of the Hecke algebra and derived anRR-matrix satisfying the Yang–Baxter equation through Baxterization.
Bibikov[9]further developed this approach and obtained several sufficient algebraic conditions on the local Hamiltonian density for the existence of anRR-matrix satisfying the Yang–Baxter equation.
Compared with our result, these approaches require substantially stronger and model-dependent algebraic assumptions than the Reshetikhin condition.

In the present work, we construct a solution of the Sutherland equation directly from the Reshetikhin condition and further prove that this solution satisfies the full difference-form Yang–Baxter equation.
This gives an affirmative resolution of the conjecture proposed in the early 1980s and supported by several decades of model construction and classification.
Previous results bridged only part of the gap, either by imposing additional assumptions or by restricting the class of Hamiltonians under consideration.
By contrast, our result bridges the entire gap from a Hamiltonian-level condition to anRR-matrix satisfying the Yang–Baxter equation.
It requires no additional algebraic assumptions beyond the conditions stated in our theorem and applies to general quantum chains within this setting.
This result substantially advances our understanding of the foundations of quantum integrability.

Our result brings previous classification programs to a more advanced and refined stage.
In earlier classification studies, one first tested candidate Hamiltonians against the Reshetikhin condition, and if a Hamiltonian passed this test, one then attempted to reconstruct a correspondingRR-matrix by solving differential equations or carrying out recursive algebraic calculations.
Our theorem shows that the initial Reshetikhin test is already sufficient and that the subsequent cumbersome reconstruction of theRR-matrix is, in principle, unnecessary.
This striking simplification makes the classification of Yang–Baxter-solvable Hamiltonians substantially more tractable.

Our result is also suggestive to the Baxterization approach.
Traditional Baxterization starts from a suitable algebraic structure and uses its relations to construct anRR-matrix satisfying the Yang–Baxter equation.
Since each construction relies on a particular algebra, it can access only a restricted subset of Yang–Baxter-integrable models.
By contrast, our finding says that, within the setting of our result, the essential requirement is only the Reshetikhin condition.
Therefore, any algebraic structure whose local Hamiltonian representation satisfies the Reshetikhin condition must admit a corresponding Yang–BaxterRR-matrix.
This observation motivates the search for a universal algebraic framework encompassing all local algebraic structures compatible with the Reshetikhin condition.

## II.3Proof of TheoremS.2

In proving TheoremS.2, we expand the Yang–Baxter equation (S.1) in terms ofuuandvv.
Consider a two-site operatorRRwhich does not necessarily satisfy the Yang–Baxter equation.
Then, inserting thisRRinto both sides of the Yang–Baxter equation, we may have finite discrepancy, which can be expanded asR12​(u)​R13​(u+v)​R23​(v)−R23​(v)​R13​(u+v)​R12​(u)=\displaystyle R_{12}(u)R_{13}(u+v)R_{23}(v)-R_{23}(v)R_{13}(u+v)R_{12}(u)=∑k,lF123k,l​uk​vl.\displaystyle\sum_{k,l}F^{k,l}_{123}u^{k}v^{l}.(S.67)

In terms of the braidedRRmatrixRˇ\check{R}, the above expansion readsRˇ12​(u)​Rˇ23​(u+v)​Rˇ12​(v)−Rˇ23​(v)​Rˇ12​(u+v)​Rˇ23​(u)=∑k,lFˇ123l,k​ul​vk,\check{R}_{12}(u)\check{R}_{23}(u+v)\check{R}_{12}(v)-\check{R}_{23}(v)\check{R}_{12}(u+v)\check{R}_{23}(u)=\sum_{k,l}\check{F}^{l,k}_{123}u^{l}v^{k},(S.68)

where we definedFˇa​b​cl,k=−Πa​c​Fa​b​ck,l.\displaystyle\check{F}^{l,k}_{abc}=-\Pi_{ac}F^{k,l}_{abc}.(S.69)

As clearly seen from above, if one ofFa​b​ck,lF^{k,l}_{abc}orFˇa​b​cl,k\check{F}^{l,k}_{abc}is shown to be zero, then the other is also zero.
As explained in Subsec.I.4,Fˇ1231,1\check{F}^{1,1}_{123}(and thusF1231,1F^{1,1}_{123}) can always be set to zero by choosing a properRˇ(2)\check{R}^{(2)}.
On the other hand,Fˇ1231,2\check{F}^{1,2}_{123}cannot necessarily be made to vanish by a suitable choice ofRˇ(3)\check{R}^{(3)}.
This can vanish if and only ifFˇ1231,2\check{F}^{1,2}_{123}takes a telescopic form:Fˇ1231,2=X23−X12\check{F}^{1,2}_{123}=X_{23}-X_{12}, which is the Reshetikhin condition.

Our goal is to prove that ifFˇ1231,2\check{F}^{1,2}_{123}can be made to vanish by a suitable choice ofRˇ(3)\check{R}^{(3)}, then allFˇ123l,k\check{F}^{l,k}_{123}can be made to vanish by a suitable choice ofRˇ(n){\check{R}}^{(n)}’s.
We shall show this by proving the following two lemmas:

## Lemma S.3(Same as Lemma3in the main article).

Suppose that a given Hamiltonianhhsatisfies the Reshetikhin condition (S.62) and thatH=∑ihi,i+1H=\sum_{i}h_{i,i+1}is diagonalizable.
Then, there exists suitableRˇ(n){\check{R}}^{(n)}’s which makeF123k,1=0F^{k,1}_{123}=0(equivalently,Fˇ1231,k=0\check{F}^{1,k}_{123}=0) for allkk.

## Lemma S.4(Same as Lemma4in the main article).

Suppose thatFˇ123l,k=0\check{F}^{l,k}_{123}=0for allkkandllwithk+l≤n−1k+l\leq n-1.
Then, allFˇ123l,k\check{F}^{l,k}_{123}’s withk+l=nk+l=nandk,l≥1k,l\geq 1are proportional to each other.

LemmaS.3establishes that the Reshetikhin condition is equivalent to the presence of the Sutherland equation (S.37) without any correction.
LemmaS.4establishes the equivalence between the Sutherland equation and the Yang–Baxter equation.
Below, we prove these two lemmas.

## II.4Proof of LemmaS.3

To prove LemmaS.3, we first show the following lemma:

## Lemma S.5(Same as Lemma5in the main article).

Suppose thatFk,1=0F^{k,1}=0for allk≤n−2k\leq n-2with suitableRˇ(2),…,Rˇ(n−1){\check{R}}^{(2)},\dots,{\check{R}}^{(n-1)}.
Then, we haveQm=QmBQ_{m}=Q^{\rm B}_{m}for2≤m≤n2\leq m\leq n.

In the following proof, we do not care about the boundary effect, similarly to Sec.I.3.
The detailed treatment of the boundary is discussed in Sec.IV.2.

## Proof.

We differentiate the modified Yang–Baxter equation with correction terms (S.67) with respect tovvand then setv=0v=0, which leads to a modified Sutherland equation with correction terms of orderO​(un−1)O(u^{n-1}):(dd​u​R13​(u))​R12​(u)−R13​(u)​(dd​u​R12​(u))=[R13​(u)​R12​(u),h23]−∑k=n−1∞Π23​F123k,1​uk.\displaystyle\left(\frac{d}{du}R_{13}(u)\right)R_{12}(u)-R_{13}(u)\left(\frac{d}{du}R_{12}(u)\right)=[R_{13}(u)R_{12}(u),h_{23}]-\sum_{k=n-1}^{\infty}\Pi_{23}F^{k,1}_{123}u^{k}.(S.70)

Here, lower-degree terms are absent becauseFk,1=0F^{k,1}=0for all1≤k≤n−21\leq k\leq n-2by supposition.
We shall follow the standard derivation ofQnB=QnQ^{\rm B}_{n}=Q_{n}seen in Sec.I.3, but with replacing the Sutherland equation by the above modified one.
By relabeling the subscripts of Eq. (S.70) as1→a1\to a,2→i2\to i, and3→i+13\to i+1, and multiplying the resulting relation by∏j≤i−1Ra​j​(u)\prod_{j\leq i-1}R_{aj}(u)from right and by∏j≥i+2Ra​j​(u)\prod_{j\geq i+2}R_{aj}(u)from left, we obtain∏j≥i+2Ra​j​(u)​(dd​u​Ra,i+1​(u))​∏j≤iRa​j​(u)−∏j≥i+1Ra​j​(u)​(dd​u​Ra​i​(u))​∏j≤i−1Ra​j​(u)=[∏jRa​j​(u),hi,i+1]+O​(un−1).\displaystyle\prod_{j\geq i+2}R_{aj}(u)\left(\frac{d}{du}R_{a,i+1}(u)\right)\prod_{j\leq i}R_{aj}(u)-\prod_{j\geq i+1}R_{aj}(u)\left(\frac{d}{du}R_{ai}(u)\right)\prod_{j\leq i-1}R_{aj}(u)=[\prod_{j}R_{aj}(u),h_{i,i+1}]+O(u^{n-1}).(S.71)

Here, the precise description ofO​(un−1)O(u^{n-1})term is−∑k=n−1∞∏j≥i+2Ra​j​(u)​Πi,i+1​Fa,i,i+1k,1​∏j≤i−1Ra​j​(u)​uk.\displaystyle-\sum_{k={n-1}}^{\infty}\prod_{j\geq i+2}R_{aj}(u)\Pi_{i,i+1}F^{k,1}_{a,i,i+1}\prod_{j\leq i-1}R_{aj}(u)u^{k}.(S.72)

Multiplying byiiand summing overii, we arrive atdd​u​∏jRa​j​(u)=[B,∏jRa​j​(u)]+O​(un−1).\displaystyle\frac{d}{du}\prod_{j}R_{aj}(u)=[B,\prod_{j}R_{aj}(u)]+O(u^{n-1}).(S.73)

Taking the trace overaa, we arrive at[B,T​(u)]=dd​u​T​(u)+O​(un−1).[B,T(u)]=\frac{d}{du}T(u)+O(u^{n-1}).(S.74)

Following a similar argument in Sec.I.3, Eq. (S.74) implies[B,ln⁡T​(u)]=dd​u​ln⁡T​(u)+O​(un−1).[B,\ln T(u)]=\frac{d}{du}\ln T(u)+O(u^{n-1}).(S.75)

Expanding the logarithm asln⁡T​(u)=ln⁡S+∑m=2∞um−1(m−1)!​Qm,\displaystyle\ln T(u)=\ln S+\sum_{m=2}^{\infty}\frac{u^{m-1}}{(m-1)!}Q_{m},(S.76)

and comparing the coefficients ofum−2u^{m-2}in Eq. (S.75), for3≤m≤n3\leq m\leq n, we obtain[B,Qm−1]=Qm.\displaystyle[B,Q_{m-1}]=Q_{m}.(S.77)

SinceQ2=Q2B=HQ_{2}=Q^{\rm B}_{2}=H, this recursively givesQm=QmB,2≤m≤n,\displaystyle Q_{m}=Q^{\rm B}_{m},\qquad 2\leq m\leq n,(S.78)

proving LemmaS.5.
∎

## Proof of LemmaS.3.

We shall show∑i=1LFˇi−1,i,i+11,n−1=0\sum_{i=1}^{L}\check{F}^{1,n-1}_{i-1,i,i+1}=0by expanding[T​(u),H][T(u),H]up to orderun−1u^{n-1}in two different ways.

In the first evaluation, we sum Eq. (S.71) overii.
This calculation is similar to the derivation of Eq. (S.74), but in this case we do not multiply byii.
Since the left-hand side vanishes in a telescopic manner, we have0=[∏jRa​j​(u),H]−∑i∑k=n−1∞[∏j≥i+2Ra​j​(u)]​Πi,i+1​Fa,i,i+1k,1​[∏j≤i−1Ra​j​(u)]​uk.\displaystyle 0=[\prod_{j}R_{aj}(u),H]-\sum_{i}\sum_{k=n-1}^{\infty}\left[\prod_{j\geq i+2}R_{aj}(u)\right]\Pi_{i,i+1}F^{k,1}_{a,i,i+1}\left[\prod_{j\leq i-1}R_{aj}(u)\right]u^{k}.(S.79)

Its partial trace over the auxiliary spaceaareads0=[T​(u),H]−∑i∑k=n−1∞Tra​[[∏j≥i+2Ra​j​(u)]​Πi,i+1​Fa,i,i+1k,1​[∏j≤i−1Ra​j​(u)]]​uk.\displaystyle 0=[T(u),H]-\sum_{i}\sum_{k=n-1}^{\infty}\mathrm{Tr}_{a}\left[\left[\prod_{j\geq i+2}R_{aj}(u)\right]\Pi_{i,i+1}F^{k,1}_{a,i,i+1}\left[\prod_{j\leq i-1}R_{aj}(u)\right]\right]u^{k}.(S.80)

Since the second term starts at orderun−1u^{n-1}, its leading contribution is obtained by settingk=n−1k=n-1and replacing all the remainingR​(u)R(u)’s byR​(0)=ΠR(0)=\Pi. We therefore have[T​(u),H]=\displaystyle[T(u),H]=∑iTra​[[∏j≥i+2Πa,j]​Πi,i+1​Fa,i,i+1n−1,1​[∏j≤i−1Πa,j]]​un−1+O​(un).\displaystyle\sum_{i}\mathrm{Tr}_{a}\left[\left[\prod_{j\geq i+2}\Pi_{a,j}\right]\Pi_{i,i+1}F^{n-1,1}_{a,i,i+1}\left[\prod_{j\leq i-1}\Pi_{a,j}\right]\right]u^{n-1}+O(u^{n}).(S.81)

The permutation product appearing in the leading term satisfiesTra​[[∏j≥i+2Πa,j]​Πi,i+1​Fa,i,i+1n−1,1​[∏j≤i−1Πa,j]]=\displaystyle\mathrm{Tr}_{a}\left[\left[\prod_{j\geq i+2}\Pi_{a,j}\right]\Pi_{i,i+1}F^{n-1,1}_{a,i,i+1}\left[\prod_{j\leq i-1}\Pi_{a,j}\right]\right]=S​Πi−1,i+1​Fi−1,i,i+1n−1,1=−S​Fˇi−1,i,i+11,n−1.\displaystyle S\Pi_{i-1,i+1}F^{n-1,1}_{i-1,i,i+1}=-S\check{F}^{1,n-1}_{i-1,i,i+1}.(S.82)

The first equality is shown as follows.
The rightmost operator∏j≤i−1Πa,j\prod_{j\leq i-1}\Pi_{a,j}maps the labels asa→1,1→2,2→3,…,i−2→i−1,i−1→a.\displaystyle a\to 1,\quad 1\to 2,\quad 2\to 3,\quad\ldots,\quad i-2\to i-1,\quad i-1\to a.(S.83)

We next applyFa,i,i+1n−1,1F^{n-1,1}_{a,i,i+1}.
Since the original sitei−1i-1is mapped onto the auxiliary spaceaaat this stage, the operatorFa,i,i+1n−1,1F^{n-1,1}_{a,i,i+1}acts on the original sites asFi−1,i,i+1n−1,1.F^{n-1,1}_{i-1,i,i+1}.After the preceding operations, applying[∏j≥i+2Πa,j]​Πi,i+1\left[\prod_{j\geq i+2}\Pi_{a,j}\right]\Pi_{i,i+1}gives the following total permutation:r→r+1(r≠i−1,i,i+1,L),r\to r+1\qquad(r\neq i-1,i,i+1,L),(S.84)

while the exceptional labels are mapped asa→1,i−1→i+2,i→i+1,i+1→i,L→a.\displaystyle a\to 1,\quad i-1\to i+2,\quad i\to i+1,\quad i+1\to i,\quad L\to a.(S.85)

The partial trace overaayieldsL→1,\displaystyle L\to 1,(S.86)

which is consistent with the general permutation rule (S.84).
Thus, on the physical sites, the resulting permutation is the one-site shiftSSfollowed by the exchange of sitesi−1i-1andi+1i+1. We therefore obtainS​Πi−1,i+1​Fi−1,i,i+1n−1,1.S\Pi_{i-1,i+1}F^{n-1,1}_{i-1,i,i+1}.The second equality follows directly from the definitionFˇa​b​cl,k=−Πa​c​Fa​b​ck,l.\displaystyle\check{F}^{l,k}_{abc}=-\Pi_{ac}F^{k,l}_{abc}.(S.87)

Substituting the above relation into the partial trace, we obtain[T​(u),H]=−S​∑iFˇi−1,i,i+11,n−1​un−1+O​(un).\displaystyle[T(u),H]=-S\sum_{i}\check{F}^{1,n-1}_{i-1,i,i+1}u^{n-1}+O(u^{n}).(S.88)

In the second evaluation, sinceS−1​T​(0)=IS^{-1}T(0)=I, we regard Eq. (S.13) as the series expansion ofln⁡S−1​T​(u)\ln S^{-1}T(u)with respect touu:ln⁡S−1​T​(u)=∑m=2∞Qm(m−1)!​um−1.\displaystyle\ln S^{-1}T(u)=\sum_{m=2}^{\infty}\frac{Q_{m}}{(m-1)!}u^{m-1}.(S.89)

Up to orderun−1u^{n-1}, this givesT​(u)=\displaystyle T(u)=S​exp⁡(∑m=2nQm(m−1)!​um−1)+O​(un)\displaystyle S\exp\left(\sum_{m=2}^{n}\frac{Q_{m}}{(m-1)!}u^{m-1}\right)+O(u^{n})=\displaystyle=S​exp⁡(∑m=2nQmB(m−1)!​um−1)+O​(un).\displaystyle S\exp\left(\sum_{m=2}^{n}\frac{Q^{\rm B}_{m}}{(m-1)!}u^{m-1}\right)+O(u^{n}).(S.90)

In the second equality, we used LemmaS.5, which states thatQm=QmBQ_{m}=Q^{\rm B}_{m}form≤nm\leq n.
Since the shift operatorSScommutes with the translation-invariant HamiltonianHH, and sinceQmBQ^{\rm B}_{m}commutes withH=Q2BH=Q^{\rm B}_{2}by LemmaS.1, we obtain[T​(u),H]=O​(un).\displaystyle[T(u),H]=O(u^{n}).(S.91)

Combining the two evaluations, we arrive at the desired relation∑i=1LFˇi−1,i,i+11,n−1=0.\displaystyle\sum_{i=1}^{L}\check{F}^{1,n-1}_{i-1,i,i+1}=0.(S.92)

∎

## II.5Proof of LemmaS.4

We next show LemmaS.4, stating that allFˇ123l,k\check{F}^{l,k}_{123}withk+l=nk+l=nare proportional to each other.
Combining LemmaS.3(claimingFˇ1231,n−1=0\check{F}^{1,n-1}_{123}=0for allnn) and LemmaS.4, we find thatFˇ123l,k=0\check{F}^{l,k}_{123}=0for allkkandll, which implies the Yang–Baxter equation.

Let us denote the sum of thenn-th order correction terms in the braided Yang–Baxter equation (S.58) byωn​(u,v):=∑k+l=nFˇ123l,k​ul​vk.\omega^{n}(u,v):=\sum_{k+l=n}\check{F}^{l,k}_{123}u^{l}v^{k}.(S.93)

To prove LemmaS.4, we first show the following lemma.

## Lemma S.6.

Suppose thatωm​(u,v)=0\omega^{m}(u,v)=0for anym≤n−1m\leq n-1.
Then, we have the following cocycle condition:ωn​(u,v)+ωn​(u+v,w)=ωn​(v,w)+ωn​(u,v+w).\omega^{n}(u,v)+\omega^{n}(u+v,w)=\omega^{n}(v,w)+\omega^{n}(u,v+w).(S.94)

## Proof.

Let us denoteA=Rˇ12A=\check{R}_{12},B=Rˇ23B=\check{R}_{23}, andC=Rˇ34C=\check{R}_{34}.
Then, the braided Yang–Baxter equation on sites 123 and sites 234 respectively readA​(x)​B​(x+y)​A​(y)\displaystyle A(x)B(x+y)A(y)=B​(y)​A​(x+y)​B​(x)+ω123n​(x,y)+O​((x,y)n+1),\displaystyle=B(y)A(x+y)B(x)+\omega_{123}^{n}(x,y)+O((x,y)^{n+1}),(S.95)B​(x)​C​(x+y)​B​(y)\displaystyle B(x)C(x+y)B(y)=C​(y)​B​(x+y)​C​(x)+ω234n​(x,y)+O​((x,y)n+1),\displaystyle=C(y)B(x+y)C(x)+\omega_{234}^{n}(x,y)+O((x,y)^{n+1}),(S.96)

whereO​((x,y)n+1)O((x,y)^{n+1})is then+1n+1-th order or higher polynomials ofxxandyy(i.e.,xa​ybx^{a}y^{b}terms witha+b≥n+1a+b\geq n+1).
In addition, we have the far commutativityA​(x)​C​(y)=C​(y)​A​(x).\displaystyle A(x)C(y)=C(y)A(x).(S.97)

Using these relations, we can convertA​B​A​C​B​AABACBAtoC​B​A​C​B​CCBACBCby two ways,A​B​A​C​B​A\displaystyle ABACBA→B​A​B​C​B​A→B​A​C​B​C​A→B​C​A​B​A​C→B​C​B​A​B​C→C​B​C​A​B​C→C​B​A​C​B​C,\displaystyle\to BABCBA\to BACBCA\to BCABAC\to BCBABC\to CBCABC\to CBACBC,(S.98)A​B​A​C​B​A\displaystyle ABACBA→A​B​C​A​B​A→A​B​C​B​A​B→A​C​B​C​A​B→C​A​B​A​C​B→C​B​A​B​C​B→C​B​A​C​B​C,\displaystyle\to ABCABA\to ABCBAB\to ACBCAB\to CABACB\to CBABCB\to CBACBC,(S.99)

where we temporarily drop the arguments ofAA,BB, andCCfor brevity.
These two sequences correspond to the two sides of theZamolodchikov tetrahedron equation, which expresses the consistency of different orders of applying the Yang–Baxter equation[55,28].
By supplementing arguments, these two conversions readA​(u)​B​(u+v)​A​(v)​C​(u+v+w)​B​(v+w)​A​(w)\displaystyle A(u)B(u+v)A(v)C(u+v+w)B(v+w)A(w)=\displaystyle=B​(v)​A​(u+v)​B​(u)​C​(u+v+w)​B​(v+w)​A​(w)+O​((u,v,w)n)\displaystyle B(v)A(u+v)B(u)C(u+v+w)B(v+w)A(w)+O((u,v,w)^{n})=\displaystyle=B​(v)​A​(u+v)​C​(v+w)​B​(u+v+w)​C​(u)​A​(w)+O​((u,v,w)n)\displaystyle B(v)A(u+v)C(v+w)B(u+v+w)C(u)A(w)+O((u,v,w)^{n})=\displaystyle=B​(v)​C​(v+w)​A​(u+v)​B​(u+v+w)​A​(w)​C​(u)+O​((u,v,w)n)\displaystyle B(v)C(v+w)A(u+v)B(u+v+w)A(w)C(u)+O((u,v,w)^{n})=\displaystyle=B​(v)​C​(v+w)​B​(w)​A​(u+v+w)​B​(u+v)​C​(u)+O​((u,v,w)n)\displaystyle B(v)C(v+w)B(w)A(u+v+w)B(u+v)C(u)+O((u,v,w)^{n})=\displaystyle=C​(w)​B​(v+w)​C​(v)​A​(u+v+w)​B​(u+v)​C​(u)+O​((u,v,w)n)\displaystyle C(w)B(v+w)C(v)A(u+v+w)B(u+v)C(u)+O((u,v,w)^{n})=\displaystyle=C​(w)​B​(v+w)​A​(u+v+w)​C​(v)​B​(u+v)​C​(u)+O​((u,v,w)n)\displaystyle C(w)B(v+w)A(u+v+w)C(v)B(u+v)C(u)+O((u,v,w)^{n})(S.100)

andA​(u)​B​(u+v)​A​(v)​C​(u+v+w)​B​(v+w)​A​(w)\displaystyle A(u)B(u+v)A(v)C(u+v+w)B(v+w)A(w)=\displaystyle=A​(u)​B​(u+v)​C​(u+v+w)​A​(v)​B​(v+w)​A​(w)+O​((u,v,w)n)\displaystyle A(u)B(u+v)C(u+v+w)A(v)B(v+w)A(w)+O((u,v,w)^{n})=\displaystyle=A​(u)​B​(u+v)​C​(u+v+w)​B​(w)​A​(v+w)​B​(v)+O​((u,v,w)n)\displaystyle A(u)B(u+v)C(u+v+w)B(w)A(v+w)B(v)+O((u,v,w)^{n})=\displaystyle=A​(u)​C​(w)​B​(u+v+w)​C​(u+v)​A​(v+w)​B​(v)+O​((u,v,w)n)\displaystyle A(u)C(w)B(u+v+w)C(u+v)A(v+w)B(v)+O((u,v,w)^{n})=\displaystyle=C​(w)​A​(u)​B​(u+v+w)​A​(v+w)​C​(u+v)​B​(v)+O​((u,v,w)n)\displaystyle C(w)A(u)B(u+v+w)A(v+w)C(u+v)B(v)+O((u,v,w)^{n})=\displaystyle=C​(w)​B​(v+w)​A​(u+v+w)​B​(u)​C​(u+v)​B​(v)+O​((u,v,w)n)\displaystyle C(w)B(v+w)A(u+v+w)B(u)C(u+v)B(v)+O((u,v,w)^{n})=\displaystyle=C​(w)​B​(v+w)​A​(u+v+w)​C​(v)​B​(u+v)​C​(u)+O​((u,v,w)n),\displaystyle C(w)B(v+w)A(u+v+w)C(v)B(u+v)C(u)+O((u,v,w)^{n}),(S.101)

whereO​((u,v,w)n)O((u,v,w)^{n})is thenn-th order polynomials ofuu,vv, andww, which includeωn\omega^{n}terms.

The first, second, fourth, and fifth equalities in Eq. (S.100) accompany correction termsω123n​(u,v)\omega^{n}_{123}(u,v),ω234n​(u,v+w)\omega^{n}_{234}(u,v+w),ω123n​(u+v,w)\omega^{n}_{123}(u+v,w), andω234n​(v,w)\omega^{n}_{234}(v,w), respectively.
In a similar manner, the second, third, fifth, and sixth equalities in Eq. (S.101) accompany correction termsω123n​(v,w)\omega^{n}_{123}(v,w),ω234n​(u+v,w)\omega^{n}_{234}(u+v,w),ω123n​(u,v+w)\omega^{n}_{123}(u,v+w), andω234n​(u,v)\omega^{n}_{234}(u,v), respectively.
These two correction terms of the ordernnshould be equal, which readsω123n​(u,v)+ω123n​(u+v,w)−ω123n​(v,w)−ω123n​(u,v+w)=ω234n​(u,v)+ω234n​(u+v,w)−ω234n​(v,w)−ω234n​(u,v+w).\displaystyle\omega^{n}_{123}(u,v)+\omega^{n}_{123}(u+v,w)-\omega^{n}_{123}(v,w)-\omega^{n}_{123}(u,v+w)=\omega^{n}_{234}(u,v)+\omega^{n}_{234}(u+v,w)-\omega^{n}_{234}(v,w)-\omega^{n}_{234}(u,v+w).(S.102)

This means that the three-site operatorωn​(u,v)+ωn​(u+v,w)−ωn​(v,w)−ωn​(u,v+w)\omega^{n}(u,v)+\omega^{n}(u+v,w)-\omega^{n}(v,w)-\omega^{n}(u,v+w)is an identity operator on three sites expressed asωn​(u,v)+ωn​(u+v,w)−ωn​(v,w)−ωn​(u,v+w)=f​(u,v,w)​I,\omega^{n}(u,v)+\omega^{n}(u+v,w)-\omega^{n}(v,w)-\omega^{n}(u,v+w)=f(u,v,w)I,(S.103)

wheref​(u,v,w)f(u,v,w)is a scalar polynomial of degreenn.

We finally show thatf​(u,v,w)f(u,v,w)is in fact zero.
We compare the determinants of both sides of the braided Yang–Baxter equation with correction terms (S.68).
Since the determinant of anRR-matrix is independent of its support, the determinant of the left-hand side is computed asdetRˇ12​(u)​Rˇ23​(u+v)​Rˇ12​(v)\displaystyle\det\check{R}_{12}(u)\check{R}_{23}(u+v)\check{R}_{12}(v)=detRˇ12​(u)​detRˇ23​(u+v)​detRˇ12​(v)\displaystyle=\det\check{R}_{12}(u)\det\check{R}_{23}(u+v)\det\check{R}_{12}(v)(S.104)=detRˇ23​(u)​detRˇ12​(u+v)​detRˇ23​(v)\displaystyle=\det\check{R}_{23}(u)\det\check{R}_{12}(u+v)\det\check{R}_{23}(v)(S.105)=detRˇ23​(v)​Rˇ12​(u+v)​Rˇ23​(u),\displaystyle=\det\check{R}_{23}(v)\check{R}_{12}(u+v)\check{R}_{23}(u),(S.106)

where we used the multiplicativity of the determinant.
DefiningX​(u,v):=Rˇ23​(v)​Rˇ12​(u+v)​Rˇ23​(u)X(u,v):=\check{R}_{23}(v)\check{R}_{12}(u+v)\check{R}_{23}(u), the determinant of the right-hand side of (S.68) up toO​((u,v)n)O((u,v)^{n})is computed asdet[X​(u,v)+ωn​(u,v)+O​((u,v)n+1)]=\displaystyle\det[X(u,v)+\omega^{n}(u,v)+O((u,v)^{n+1})]=detX​(u,v)​det[I+X−1​(u,v)​ωn​(u,v)+O​((u,v)n+1)]\displaystyle\det X(u,v)\det[I+X^{-1}(u,v)\omega^{n}(u,v)+O((u,v)^{n+1})]=\displaystyle=detX​(u,v)​det[I+ωn​(u,v)+O​((u,v)n+1)]\displaystyle\det X(u,v)\det[I+\omega^{n}(u,v)+O((u,v)^{n+1})]=\displaystyle=(detX​(u,v))​(1+Tr​[ωn​(u,v)]+O​((u,v)n+1)).\displaystyle(\det X(u,v))(1+\mathrm{Tr}[\omega^{n}(u,v)]+O((u,v)^{n+1})).(S.107)

In the second equality, we usedX​(u,v)=I+O​((u,v)1)X(u,v)=I+O((u,v)^{1}).
Comparing both sides, we findTr​[ωn​(u,v)]=0.\displaystyle\mathrm{Tr}[\omega^{n}(u,v)]=0.(S.108)

Taking the trace of both sides of Eq. (S.103), we arrive at0=f​(u,v,w)​d3,\displaystyle 0=f(u,v,w)d^{3},(S.109)

which implies the desired cocycle condition:ωn​(u,v)+ωn​(u+v,w)−ωn​(v,w)−ωn​(u,v+w)=0.\displaystyle\omega^{n}(u,v)+\omega^{n}(u+v,w)-\omega^{n}(v,w)-\omega^{n}(u,v+w)=0.(S.110)

∎

We shall use the equivalence of the cocycle condition and thecoboundary condition.

## Lemma S.7.

Suppose thatωn​(u,v)\omega^{n}(u,v)satisfies the cocycle condition (S.94) andωn​(u,0)=0\omega^{n}(u,0)=0for alluu.
Then,ωn​(u,v)\omega^{n}(u,v)satisfies the coboundary condition, claiming that there is a suitableg​(u){g}(u)such thatωn​(u,v)=g​(u+v)−g​(u)−g​(v).\omega^{n}(u,v)={g}(u+v)-{g}(u)-{g}(v).(S.111)

## Proof.

Let∂2ωn\partial_{2}\omega^{n}denote the derivative ofωn\omega^{n}with respect to its second argument.
Differentiating Eq. (S.94) with respect towwand settingw=0w=0, we have0+∂2ωn​(u+v,0)=∂2ωn​(v,0)+∂2ωn​(u,v).0+\partial_{2}\omega^{n}(u+v,0)=\partial_{2}\omega^{n}(v,0)+\partial_{2}\omega^{n}(u,v).(S.112)

Definingg​(x)=∫0x𝑑y​∂2ωn​(y,0),\displaystyle{g}(x)=\int_{0}^{x}dy\partial_{2}\omega^{n}(y,0),(S.113)

integrating Eq. (S.112) with respect tovvfromv=0v=0tov=u′v=u^{\prime}givesg​(u+u′)−g​(u)=g​(u′)+ωn​(u,u′),\displaystyle{g}(u+u^{\prime})-{g}(u)={g}(u^{\prime})+\omega^{n}(u,u^{\prime}),(S.114)

where we usedωn​(u,0)=0\omega^{n}(u,0)=0.
This is the desired coboundary condition.
∎

## Proof of LemmaS.4.

Expandggas an operator-valued formal power series,g​(x)=∑m=0∞Km​xm.g(x)=\sum_{m=0}^{\infty}K_{m}x^{m}.(S.115)

The contribution ofKmK_{m}to the coboundary is homogeneous of total degreemm. Sinceωn​(u,v)\omega^{n}(u,v)is homogeneous of total degreenn, comparison of homogeneous components givesωn​(u,v)=Kn​((u+v)n−un−vn).\omega^{n}(u,v)=K_{n}\bigl((u+v)^{n}-u^{n}-v^{n}\bigr).(S.116)

For everyk,l≥1k,l\geq 1withk+l=nk+l=n, the coefficient oful​vku^{l}v^{k}is(nl)​Kn\binom{n}{l}K_{n}, a nonzero scalar multiple of the same operatorKnK_{n}. Hence allFˇ123l,k\check{F}_{123}^{l,k}withk+l=nk+l=nare mutually proportional and vanish simultaneously. This proves LemmaS.4.
∎

## IIIAlgorithms for testing integrability and reconstructing R-matrices

## III.1Setup

In this section we describe the algorithmic aspects of the integrability test and the reconstruction procedure for a given two-site Hamiltonian densityh∈End​(V⊗V),dimV=d.\displaystyle h\in\mathrm{End}(V\otimes V),\qquad\dim V=d.(S.117)

Throughout this section, we assume standard cubic dense matrix multiplication, i.e.,ω=3\omega=3, and do not impose any additional sparsity or symmetry assumptions onhh.

We use the braidedRR-matrix convention introduced in Sec.I.4and consider a regularRR-matrix of the formRˇ​(u)=I+h​u+∑n≥2Rˇ(n)​un.\displaystyle\check{R}(u)=I+hu+\sum_{n\geq 2}\check{R}^{(n)}u^{n}.(S.118)

In the reconstruction problem, the coefficientsRˇ(n)\check{R}^{(n)}are determined only up to an additive scalar multiple of the identity.
We fix this freedom by working in the traceless gaugeTr​Rˇ(n)=0,n≥2,\displaystyle\mathrm{Tr}\check{R}^{(n)}=0,\qquad n\geq 2,(S.119)

where the trace is taken overV⊗VV\otimes V.

The main claims of this section are summarized in the following two lemmas.

## Lemma S.8(Integrability test).

For a givenh∈End​(V⊗V)h\in\mathrm{End}(V\otimes V), whether the Reshetikhin condition holds can be determined inO​(d8)O(d^{8})time andO​(d6)O(d^{6})memory.

## Lemma S.9(Reconstruction).

For a givenhhsatisfying the assumptions of Theorem1.
Assume thatH=∑ihi,i+1H=\sum_{i}h_{i,i+1}is diagonalizable.
Then, the coefficientsRˇ(2),…,Rˇ(n)\check{R}^{(2)},\ldots,\check{R}^{(n)}of a regular braidedRR-matrixRˇ​(u)=I+h​u+∑m≥2Rˇ(m)​um\displaystyle\check{R}(u)=I+hu+\sum_{m\geq 2}\check{R}^{(m)}u^{m}(S.120)

can be reconstructed inO​(n2​d6)O(n^{2}d^{6})time andO​(n​d4)O(nd^{4})memory.

Below, Sec.III.2describes the algorithmic test of the Reshetikhin condition, corresponding to LemmaS.8.
The reconstruction procedure, corresponding to LemmaS.9, is summarized in Sec.III.3.

## III.2Integrability test

To test whether a givenhhsatisfies the Reshetikhin condition, we first computeY123:=[h12+h23,[h12,h23]].\displaystyle Y_{123}:=[h_{12}+h_{23},[h_{12},h_{23}]].(S.121)

The Reshetikhin condition is equivalent to the existence of a two-site operatorX∈End​(V⊗V)X\in\mathrm{End}(V\otimes V)such thatY123=X23−X12.\displaystyle Y_{123}=X_{23}-X_{12}.(S.122)

To express this condition in a form better suited for implementation, we decomposeY123Y_{123}according
to the support on which each component acts nontrivially. Splitting the one-site operator space asEnd​(V)=ℂ​I⊕End0​(V),\displaystyle\mathrm{End}(V)=\mathbb{C}I\oplus\mathrm{End}_{0}(V),(S.123)

any three-site operator admits a unique decomposition into its0-site,11-site,22-site, and33-site components.
SinceY123Y_{123}is a commutator, its scalar (0-site) part vanishes.
We may therefore writeY123=\displaystyle Y_{123}={}Y1[1]⊗I2⊗I3+I1⊗Y2[2]⊗I3+I1⊗I2⊗Y3[3]+Y12[12]⊗I3+I1⊗Y23[23]+Y123[res],\displaystyle Y^{[1]}_{1}\otimes I_{2}\otimes I_{3}+I_{1}\otimes Y^{[2]}_{2}\otimes I_{3}+I_{1}\otimes I_{2}\otimes Y^{[3]}_{3}+Y^{[12]}_{12}\otimes I_{3}+I_{1}\otimes Y^{[23]}_{23}+Y^{[\mathrm{res}]}_{123},(S.124)

whereY[1],Y[2],Y[3]∈End0​(V)Y^{[1]},Y^{[2]},Y^{[3]}\in\mathrm{End}_{0}(V),Y[12],Y[23]∈End0​(V)⊗End0​(V)Y^{[12]},Y^{[23]}\in\mathrm{End}_{0}(V)\otimes\mathrm{End}_{0}(V), andY123[res]∈End0​(V)⊗End​(V)⊗End0​(V)Y^{[\mathrm{res}]}_{123}\in\mathrm{End}_{0}(V)\otimes\mathrm{End}(V)\otimes\mathrm{End}_{0}(V).

In this decomposition, the Reshetikhin condition is equivalent to requiring the11-site and nearest-neighbour22-site sectors to be telescopic and the residual sector to vanish. To make this explicit, we introduceΣ(1):=Y[1]+Y[2]+Y[3]∈End0​(V),Σ(2):=Y[12]+Y[23]∈End0​(V)⊗End0​(V).\displaystyle\Sigma^{(1)}:=Y^{[1]}+Y^{[2]}+Y^{[3]}\in\mathrm{End}_{0}(V),\qquad\Sigma^{(2)}:=Y^{[12]}+Y^{[23]}\in\mathrm{End}_{0}(V)\otimes\mathrm{End}_{0}(V).(S.125)

Then the Reshetikhin condition is equivalent toΣ(1)=0,Σ(2)=0,Y123[res]=0.\displaystyle\Sigma^{(1)}=0,\qquad\Sigma^{(2)}=0,\qquad Y^{[\mathrm{res}]}_{123}=0.(S.126)

Indeed, if Eq. (S.122) holds, thenX23X_{23}andX12X_{12}are the same two-site operator placed one site
apart. Hence the11-site and nearest-neighbour22-site sectors necessarily cancel in Eq. (S.125), and the residual component inEnd0​(V)⊗End​(V)⊗End0​(V)\mathrm{End}_{0}(V)\otimes\mathrm{End}(V)\otimes\mathrm{End}_{0}(V)is absent. Conversely, if
Eq. (S.126) holds, then the11-site and22-site sectors are both of telescopic form; explicitly,X=−Y[12]−Y[1]⊗I+I⊗Y[3]X=-Y^{[12]}-Y^{[1]}\otimes I+I\otimes Y^{[3]}satisfies Eq. (S.122).

The practical test of the Reshetikhin condition is therefore as follows: decomposeY123Y_{123}as in
Eq. (S.124) and check Eq. (S.126).
In computations, these sectors can be extracted by partial traces. The11-site sector is obtained from double partial
traces. After this contribution has been subtracted, the nearest-neighbour22-site sector is read off from
single partial traces.

We now estimate the computational cost. A naive implementation would explicitly constructh12h_{12}andh23h_{23}asd3×d3d^{3}\times d^{3}matrices onV⊗3V^{\otimes 3}and then evaluate Eq. (S.121) by dense matrix multiplication.
This gives a time complexity ofO​(d9)O(d^{9})and a memory cost ofO​(d6)O(d^{6}).

In practice, however, one can exploit the fact thath12h_{12}andh23h_{23}act only on neighbouring legs. The inner
commutatorC123:=[h12,h23]\displaystyle C_{123}:=[h_{12},h_{23}](S.127)

has components(C123)a​b​ca′​b′​c′=∑xha​ba′​x​hx​cb′​c′−∑xhb​cx​c′​ha​xa′​b′.\displaystyle(C_{123})_{abc}^{a^{\prime}b^{\prime}c^{\prime}}=\sum_{x}h_{ab}^{a^{\prime}x}h_{xc}^{b^{\prime}c^{\prime}}-\sum_{x}h_{bc}^{xc^{\prime}}h_{ax}^{a^{\prime}b^{\prime}}.(S.128)

For each choice of external indices, Eq. (S.128) contains only a single internal summation;
computing all components therefore costsO​(d7)O(d^{7}).

The outer commutatorY123=[h12+h23,C123]\displaystyle Y_{123}=[h_{12}+h_{23},C_{123}](S.129)

is handled similarly. For example,(h12​C123)a​b​ca′​b′​c′=∑x,yhx​ya′​b′​(C123)a​b​cx​y​c′.\displaystyle(h_{12}C_{123})_{abc}^{a^{\prime}b^{\prime}c^{\prime}}=\sum_{x,y}h_{xy}^{a^{\prime}b^{\prime}}(C_{123})_{abc}^{xyc^{\prime}}.(S.130)

The same contraction pattern appears in the termsh23​C123h_{23}C_{123},C123​h12C_{123}h_{12}, andC123​h23C_{123}h_{23}.
These contractions contain two internal summations for each choice of external indices, as illustrated in
Eq. (S.130), so this stage costsO​(d8)O(d^{8})and dominates the computation.
As a result, the full construction ofY123Y_{123}costsO​(d8)O(d^{8}).

The bottleneck of the overall Reshetikhin test is therefore the construction ofY123Y_{123}rather than the subsequent
difference-form check. OnceY123Y_{123}has been computed, the sector decomposition, the extraction of the11-site
and nearest-neighbour22-site components, and the checks in Eq. (S.126) all cost at mostO​(d6)O(d^{6})and do not affect the leading asymptotics.
The overall complexity of the integrability test is thusTtest​(d)=O​(d8),Stest​(d)=O​(d6).\displaystyle T_{\mathrm{test}}(d)=O(d^{8}),\qquad S_{\mathrm{test}}(d)=O(d^{6}).(S.131)

## III.3Reconstruction algorithm

Given a two-site operatorhhsatisfying the Reshetikhin condition, one can reconstruct the coefficients of a regular braidedRR-matrixRˇ​(u)=I+h​u+∑m≥2Rˇ(m)​um\displaystyle\check{R}(u)=I+hu+\sum_{m\geq 2}\check{R}^{(m)}u^{m}(S.132)

order by order. Rather than solving the full two-parameter Yang–Baxter equation coefficientwise, we use the one-variable recursion coming from the braided Sutherland equation.

The braided Sutherland equation used in this subsection isRˇ12​(u)​Rˇ23′​(u)−Rˇ12′​(u)​Rˇ23​(u)=h23​Rˇ12​(u)​Rˇ23​(u)−Rˇ12​(u)​Rˇ23​(u)​h12.\displaystyle\check{R}_{12}(u)\check{R}^{\prime}_{23}(u)-\check{R}^{\prime}_{12}(u)\check{R}_{23}(u)=h_{23}\check{R}_{12}(u)\check{R}_{23}(u)-\check{R}_{12}(u)\check{R}_{23}(u)h_{12}.(S.133)

SubstitutingRˇ​(u)=∑m≥0Rˇ(m)​um\check{R}(u)=\sum_{m\geq 0}\check{R}^{(m)}u^{m},Rˇ(0)=I\check{R}^{(0)}=I, andRˇ(1)=h\check{R}^{(1)}=h,
and comparing the coefficients ofunu^{n}, one obtains(n+1)​(Rˇ23(n+1)−Rˇ12(n+1))=Φn,\displaystyle(n+1)\bigl(\check{R}^{(n+1)}_{23}-\check{R}^{(n+1)}_{12}\bigr)=\Phi_{n},(S.134)

whereGn:=∑j=0nRˇ12(n−j)​Rˇ23(j)\displaystyle G_{n}:=\sum_{j=0}^{n}\check{R}^{(n-j)}_{12}\check{R}^{(j)}_{23}(S.135)

andΦn=h23​Gn−Gn​h12+∑j=1n(n+1−2​j)​Rˇ12(n+1−j)​Rˇ23(j).\displaystyle\Phi_{n}=h_{23}G_{n}-G_{n}h_{12}+\sum_{j=1}^{n}(n+1-2j)\check{R}^{(n+1-j)}_{12}\check{R}^{(j)}_{23}.(S.136)

At this stage, a naive implementation would treat each term in Eq. (S.136) as ad3×d3d^{3}\times d^{3}matrix product onV⊗3V^{\otimes 3}. Since the right-hand side containsO​(n)O(n)terms, the update of the(n+1)(n+1)st coefficient would then costO​(n​d9)O(nd^{9}), and the cumulative cost up to ordernnwould beO​(n2​d9)O(n^{2}d^{9}).

The key point is that one never needs to construct the full three-site operatorΦn\Phi_{n}. As shown in the previous subsection, to recover the corresponding two-site operator from a difference-form three-site operator, it is enough to computeP3​(Φn)P_{3}(\Phi_{n})withPi:=1d​TriP_{i}:=\frac{1}{d}\mathrm{Tr}_{i}.
Thus, at each step, the actual task is to evaluateP3​(Φn)P_{3}(\Phi_{n})rather thanΦn\Phi_{n}itself.

The computation ofP3​(Φn)P_{3}(\Phi_{n})is performed term by term. First, defineρ2(j):=P3​(Rˇ23(j)).\displaystyle\rho^{(j)}_{2}:=P_{3}(\check{R}^{(j)}_{23}).(S.137)

ThenP3​(Rˇ12(n−j)​Rˇ23(j))=Rˇ12(n−j)​ρ2(j),\displaystyle P_{3}\!\left(\check{R}^{(n-j)}_{12}\check{R}^{(j)}_{23}\right)=\check{R}^{(n-j)}_{12}\,\rho^{(j)}_{2},(S.138)

so the second and third terms on the right-hand side of Eq. (S.136) can be evaluated directly as two-site operators usingρ2(j)\rho^{(j)}_{2}.

By contrast, the terms coming from the first term in Eq. (S.136),P3​(h23​Rˇ12(n−j)​Rˇ23(j)),\displaystyle P_{3}\!\left(h_{23}\check{R}^{(n-j)}_{12}\check{R}^{(j)}_{23}\right),(S.139)

do not factorize in this way. For these, define a superoperator acting on site22by𝒦2(j)​(M2):=P3​(h23​M2​Rˇ23(j)).\displaystyle\mathcal{K}^{(j)}_{2}(M_{2}):=P_{3}\!\left(h_{23}M_{2}\check{R}^{(j)}_{23}\right).(S.140)

Writing its action on the matrix units(|α⟩​⟨β|)2(|\alpha\rangle\langle\beta|)_{2}as𝒦2(j)​((|α⟩​⟨β|)2)=∑α′,β′(𝒦2(j))α​βα′​β′​(|α′⟩​⟨β′|)2,\displaystyle\mathcal{K}^{(j)}_{2}\bigl((|\alpha\rangle\langle\beta|)_{2}\bigr)=\sum_{\alpha^{\prime},\beta^{\prime}}(\mathcal{K}^{(j)}_{2})_{\alpha\beta}^{\alpha^{\prime}\beta^{\prime}}(|\alpha^{\prime}\rangle\langle\beta^{\prime}|)_{2},(S.141)

its matrix elements are(𝒦2(j))α​βα′​β′=1d​∑γ,δhα​δα′​γ​(Rˇ(j))β′​γβ​δ.\displaystyle(\mathcal{K}^{(j)}_{2})_{\alpha\beta}^{\alpha^{\prime}\beta^{\prime}}=\frac{1}{d}\sum_{\gamma,\delta}h_{\alpha\delta}^{\alpha^{\prime}\gamma}\,(\check{R}^{(j)})_{\beta^{\prime}\gamma}^{\beta\delta}.(S.142)

By linear extension,𝒦2(j)\mathcal{K}^{(j)}_{2}acts on the site-22factor of a general two-site operator. In this notation,P3​(Φn)=∑j=0n𝒦2(j)​(Rˇ12(n−j))−∑j=0nRˇ12(n−j)​ρ2(j)​h12+∑j=1n(n+1−2​j)​Rˇ12(n+1−j)​ρ2(j).\displaystyle P_{3}(\Phi_{n})=\sum_{j=0}^{n}\mathcal{K}^{(j)}_{2}\!\left(\check{R}^{(n-j)}_{12}\right)-\sum_{j=0}^{n}\check{R}^{(n-j)}_{12}\,\rho^{(j)}_{2}h_{12}+\sum_{j=1}^{n}(n+1-2j)\check{R}^{(n+1-j)}_{12}\,\rho^{(j)}_{2}.(S.143)

In practice, one stores the dataRˇ(j)\check{R}^{(j)},ρ2(j)\rho^{(j)}_{2},𝒦2(j)\mathcal{K}^{(j)}_{2}for eachjj. One first computesP3​(Φn)P_{3}(\Phi_{n})from Eq. (S.143), and then reconstructsRˇ(n+1)\check{R}^{(n+1)}by the same difference-form extraction used in the previous subsection. Concretely, applyingP3P_{3}to Eq. (S.134) givesRˇ(n+1)=−1n+1​P3​(Φn)−1n+1​I⊗P2​(P3​(Φn)),\displaystyle\check{R}^{(n+1)}=-\frac{1}{n+1}P_{3}(\Phi_{n})-\frac{1}{n+1}I\otimes P_{2}(P_{3}(\Phi_{n})),(S.144)

where the traceless gauge fixes the scalar freedom.

We now estimate the computational complexity. Let us first discuss the dependence on the ordernn. Updating the(n+1)(n+1)st coefficient requires processing theO​(n)O(n)terms withj=0,…,nj=0,\dots,n, so the cumulative cost up to ordernnisO​(n2)O(n^{2}). This is dramatically smaller than what one obtains by expanding the full Yang–Baxter equation directly.

Next we examine the dependence ondd. There are three tasks to consider: constructingRˇ(n+1)\check{R}^{(n+1)}, constructingρ2(j)\rho^{(j)}_{2}, and constructing𝒦2(j)\mathcal{K}^{(j)}_{2}.

First, consider the construction ofRˇ(n+1)\check{R}^{(n+1)}. This includes the computation ofP3​(Φn)P_{3}(\Phi_{n})through Eq. (S.143). The second and third terms in Eq. (S.143) are handled throughρ2(j)\rho^{(j)}_{2}. Sinceρ2(j)\rho^{(j)}_{2}is ad×dd\times dmatrix on site22, multiplyingRˇ12(n−j)​ρ2(j)\check{R}^{(n-j)}_{12}\,\rho^{(j)}_{2}costsO​(d5)O(d^{5}), so these contributions are lower-order. The dominant contribution comes from the first term in Eq. (S.143),𝒦2(j)​(Rˇ12(n−j))\mathcal{K}^{(j)}_{2}\!\left(\check{R}^{(n-j)}_{12}\right).
A single application of𝒦2(j)\mathcal{K}^{(j)}_{2}to an operator on site22costsO​(d4)O(d^{4}), whileRˇ12(n−j)\check{R}^{(n-j)}_{12}is a general two-site operator carryingd2d^{2}degrees of freedom on site11. Therefore the total cost of applying𝒦2(j)\mathcal{K}^{(j)}_{2}toRˇ12(n−j)\check{R}^{(n-j)}_{12}isO​(d6)O(d^{6}). It follows that the update cost forRˇ(n+1)\check{R}^{(n+1)}isO​(n​d6),O(nd^{6}),and this is the bottleneck at each step.

Next, the construction ofρ2(j)=P3​(Rˇ23(j))\rho^{(j)}_{2}=P_{3}(\check{R}^{(j)}_{23})is just a partial trace of a two-site operator. The output hasd2d^{2}components, and each component is computed with a single internal summation, so the cost isO​(d3)O(d^{3}).

Finally, consider the construction of𝒦2(j)\mathcal{K}^{(j)}_{2}. For fixedα,β\alpha,\beta, the image𝒦2(j)​((|α⟩​⟨β|)2)\mathcal{K}^{(j)}_{2}\bigl((|\alpha\rangle\langle\beta|)_{2}\bigr)is an operator on site22withd2d^{2}output components. Each output component is given by a double sum, so the cost of computing this single image isO​(d4)O(d^{4}). Doing this for alld2d^{2}pairs(α,β)(\alpha,\beta)givesO​(d6)O(d^{6})for the full construction of𝒦2(j)\mathcal{K}^{(j)}_{2}.

Therefore the total time complexity up to ordernnisTconstruct​(n,d)=O​(n2​d6),\displaystyle T_{\mathrm{construct}}(n,d)=O(n^{2}d^{6}),(S.145)

while the memory usage is dominated by storingRˇ(1),…,Rˇ(n),\check{R}^{(1)},\dots,\check{R}^{(n)},and the superoperators𝒦(0),…,𝒦(n)\mathcal{K}^{(0)},\dots,\mathcal{K}^{(n)}, each of which hasO​(d4)O(d^{4})components. HenceSconstruct​(n,d)=O​(n​d4).\displaystyle S_{\mathrm{construct}}(n,d)=O(nd^{4}).(S.146)

In conclusion, once the Reshetikhin condition is satisfied, the corresponding braidedRR-matrix can be reconstructed by the braided Sutherland recursion inO​(n2​d6)O(n^{2}d^{6})time andO​(n​d4)O(nd^{4})memory.

## IVRemarks

## IV.1Convergence of the reconstructedRR-matrix

The formal series reconstructed above has a nonzero radius of
convergence. Indeed, letrn:=‖Rˇ(n)‖,c:=‖h‖,\displaystyle r_{n}:=\|\check{R}^{(n)}\|,\qquad c:=\|h\|,(S.147)

where∥⋅∥\|\cdot\|is the operator norm. Since the normalized partial
trace is contractive, Eq. (S.144) givesrn+1≤2n+1​‖Φn‖.\displaystyle r_{n+1}\leq\frac{2}{n+1}\|\Phi_{n}\|.(S.148)

Using Eq. (S.136), submultiplicativity, and|n+1−2​j|≤n+1|n+1-2j|\leq n+1, we obtainrn+1≤4​c​∑j=0nrj​rn−j+2​∑j=1nrj​rn+1−j,n≥1.\displaystyle r_{n+1}\leq 4c\sum_{j=0}^{n}r_{j}r_{n-j}+2\sum_{j=1}^{n}r_{j}r_{n+1-j},\qquad n\geq 1.(S.149)

Leta0=1a_{0}=1,a1=ca_{1}=c, and definean​(n≥2)a_{n}(n\geq 2)by replacing the inequality (S.149) with equality.
Multiplying the recurrence byzn+1z^{n+1}and summing overn≥1n\geq 1,
the Cauchy product formula givesA​(z)−1−c​z=4​c​z​(A​(z)2−1)+2​(A​(z)−1)2,\displaystyle A(z)-1-cz=4cz\bigl(A(z)^{2}-1\bigr)+2\bigl(A(z)-1\bigr)^{2},(S.150)

whereA​(z)A(z)is the generating functionA​(z)=∑n≥0an​znA(z)=\sum_{n\geq 0}a_{n}z^{n}.
Equivalently,A​(z)A(z)formally satisfiesF​(A​(z),z)=0,F​(w,z):=w−1−c​z−4​c​z​(w2−1)−2​(w−1)2.\displaystyle F(A(z),z)=0,\qquad F(w,z):=w-1-cz-4cz(w^{2}-1)-2(w-1)^{2}.(S.151)

SinceF​(1,0)=0F(1,0)=0,∂wF​(1,0)=1≠0,\partial_{w}F(1,0)=1\neq 0,the analytic implicit-function theorem yields a unique analytic
solutionA​(z)A(z)withA​(0)=1A(0)=1in a neighborhood ofz=0z=0.
Its Taylor coefficients coincide with the recursively defined
coefficientsana_{n}. Hence the majorant series has a nonzero radius
of convergence. Thusrn≤anr_{n}\leq a_{n}implies thatRˇ​(u)=∑n≥0Rˇ(n)​un\check{R}(u)=\sum_{n\geq 0}\check{R}^{(n)}u^{n}converges for sufficiently
small|u||u|.

Consequently, the formal Yang–Baxter identity becomes an analytic identity for sufficiently smallu,vu,vwith|u|+|v||u|+|v|inside the convergence disk.

## IV.2Technical remarks on boundary terms associated with the boost operator

In the main text, we treat the boost operatorBBwithout keeping track of boundary terms.
In the standard treatment of the boost operator, one often first considers an infinite system, where boundary effects are absent, and then regards the resulting relation as the corresponding relation in a finite periodic system.
This procedure is conventional and widely used in the literature[48,14].
Nevertheless, since the treatment of boundary terms may deserve some clarification, we briefly explain below why this procedure is eventually justified.

The boost operatorB=∑jj​hj,j+1B=\sum_{j}jh_{j,j+1}is not directly compatible with the periodic boundary condition, because the coefficientjjis discontinuous across the boundary.
Thus, commutators involvingBB, such as[B,Q][B,Q], should not be interpreted literally as commutators of well-defined finite-size operators.
Rather, they should be regarded as a formal prescription for extracting the corresponding bulk local operator.

This idea is most easily understood for quantities that are sums of local quantities.
Consider a large system of lengthLLwith periodic boundary conditions and akk-local quantityA=∑i=1LAiA=\sum_{i=1}^{L}A_{i}, whereAiA_{i}is supported on thekkconsecutive sitesi,i+1,…,i+k−1i,i+1,\ldots,i+k-1.
Since the boost operatorBBis a sum of two-site terms andAAis a sum ofkk-local terms, the local terms appearing in their commutator[B,A]=[∑jj​hj,j+1,∑iAi]=∑i,jj​[hj,j+1,Ai]\displaystyle[B,A]=[\sum_{j}jh_{j,j+1},\sum_{i}A_{i}]=\sum_{i,j}j[h_{j,j+1},A_{i}](S.152)

are supported on at mostk+1k+1consecutive sites in the bulk.
Far from the boundary, all computations are well defined, and boundary terms do not affect the result.
In particular, as shown in the first part of Lemma2, ifAAis conserved (i.e.,[A,H]=0[A,H]=0), the resulting bulk quantity is translationally invariant.
Keeping this in mind, we may regard the commutator[B,A][B,A]as a prescription for extracting the bulk quantity computed in this way.

From these arguments, we can determine which types of calculations are justified and which are not.
For example, nested commutators involving the boost operator and local operators can be justified, because the commutator of the boost operator with a local operator is again local.
Hence, the derivation of Lemma2given in Sec.I.3(except for the last step concerning[H,[H,Q]]=0[H,[H,Q]]=0) is harmless.
On the other hand, arguments based on energy eigenstates are more subtle.
In infinite-size systems, the set of energy eigenstates does not necessarily span the entire state space and eigenenergies might be ill-defined (unbounded), while in finite-size systems the commutator[B,A][B,A]cannot be interpreted literally without specifying how the boundary terms are treated.
For example, let|ψi⟩\ket{\psi_{i}}be an energy eigenstate satisfyingH​|ψi⟩=Ei​|ψi⟩H\ket{\psi_{i}}=E_{i}\ket{\psi_{i}}.
One might be tempted to compute⟨ψi|Q3B|ψi⟩=⟨ψi|[B,H]|ψi⟩​=?​⟨ψi|B​H|ψi⟩−⟨ψi|H​B|ψi⟩=(Ei−Ei)​⟨ψi|B|ψi⟩=0(?)\displaystyle\braket{\psi_{i}|Q^{\rm B}_{3}|\psi_{i}}=\braket{\psi_{i}|[B,H]|\psi_{i}}\overset{?}{=}\braket{\psi_{i}|BH|\psi_{i}}-\braket{\psi_{i}|HB|\psi_{i}}=(E_{i}-E_{i})\braket{\psi_{i}|B|\psi_{i}}=0\hskip 10.0pt(?)(S.153)

This computation, however, is not justified.
The relationQ3B=[B,H]Q^{\rm B}_{3}=[B,H]should be understood as a bulk relation obtained after discarding boundary terms, and not as an operator identity involving a well-defined boost operatorBBon the finite periodic chain.
Therefore, one cannot insert finite-size energy eigenstates into this formal commutator in the above manner.

A more delicate issue arises when we consider commutators between the boost operatorBBand the transfer matrixT​(u)T(u), which is a nonlocal operator.
Such commutators appear in the arguments in Sec.I.3(in the case with the Yang–Baxter equation) and Sec.II.4(in the derivation of LemmaS.5).
In this case, the above justification is not directly applicable.
Nevertheless, the relation between the two local quantitiesQnQ_{n}andQnBQ^{\rm B}_{n}, which is the main point of these subsections, can still be justified.

To keep track of boundary contributions, we first assign independent spectral parametersu1,…,uLu_{1},\ldots,u_{L}to theLLlocalRR-matricesRa​1,…,Ra​LR_{a1},\ldots,R_{aL}.
At the end of the calculation, we setu1=u2=⋯=uL=uu_{1}=u_{2}=\cdots=u_{L}=u.
Accordingly, we introduce the inhomogeneous transfer matrixT​(u)=Tra​[∏i=1LRa​i​(ui)]T(u)=\mathrm{Tr}_{a}[\prod_{i=1}^{L}R_{ai}(u_{i})].
After the homogeneous specializationu1=⋯=uL=uu_{1}=\cdots=u_{L}=u, the ordinary derivative with respect touuis given bydd​u=∑idd​ui.\displaystyle\frac{d}{du}=\sum_{i}\frac{d}{du_{i}}.(S.154)

Following the argument in Sec.I.3, we obtain Eq. (S.40) with an explicit boundary term:[B,T​(u)]=dd​u​T​(u)−L​dd​u1​T​(u).[B,T(u)]=\frac{d}{du}T(u)-L\frac{d}{du_{1}}T(u).(S.155)

Unlike the bulk relation without the boundary term, this relation is an exact finite-size identity for anyLL.
When we consider the Sutherland equation with a correction term (S.70) in Sec.II.4, this relation acquires an additionalO​(un−1)O(u^{n-1})correction.
Following the argument in Sec.I.3, we obtain[B,ln⁡T​(u)]=dd​u​ln⁡T​(u)−L​dd​u1​ln⁡T​(u).[B,\ln T(u)]=\frac{d}{du}\ln T(u)-L\frac{d}{du_{1}}\ln T(u).(S.156)

For our purpose, we considerln⁡S−1​T​(u)\ln S^{-1}T(u)instead ofln⁡T​(u)\ln T(u)itself.
To this end, we first consider a counterpart of Eq. (S.155), which is expressed as[B,S−1​T​(u)]=dd​u​S−1​T​(u)−L​dd​u1​S−1​T​(u)−(H−L​hL,1)​S−1​T​(u).[B,S^{-1}T(u)]=\frac{d}{du}S^{-1}T(u)-L\frac{d}{du_{1}}S^{-1}T(u)-(H-Lh_{L,1})S^{-1}T(u).(S.157)

To further transform this relation, we writeY=ln⁡S−1​T​(u)Y=\ln S^{-1}T(u)for brevity and introduce the adjoint actionadY​(X):=[Y,X]{\rm ad}_{Y}(X):=[Y,X].
A useful identity of the adjoint action ise−adY​X=e−Y​X​eY,\displaystyle e^{-{\rm ad}_{Y}}X=e^{-Y}Xe^{Y},(S.158)

where the exponential of the adjoint action is defined through its Taylor expansion:e−adY=∑n=0∞(−1)nn!​(adY)ne^{-{\rm ad}_{Y}}=\sum_{n=0}^{\infty}\frac{(-1)^{n}}{n!}({\rm ad}_{Y})^{n}.
Other functions ofadY{\rm ad}_{Y}are defined analogously.
In particular, we use the following two functions;K​(adY):=1−e−adYadY,Φ​(adY):=adYeadY−1,\displaystyle K({\rm ad}_{Y}):=\frac{1-e^{-{\rm ad}_{Y}}}{{\rm ad}_{Y}},\hskip 15.0pt\Phi({\rm ad}_{Y}):=\frac{{\rm ad}_{Y}}{e^{{\rm ad}_{Y}}-1},(S.159)

which satisfyK−1​(adY)​e−adY=Φ​(adY).\displaystyle K^{-1}({\rm ad}_{Y})e^{-{\rm ad}_{Y}}=\Phi({\rm ad}_{Y}).(S.160)

Using these functions, we obtain the identitiese−Y​∂∂ui​eY\displaystyle e^{-Y}\frac{\partial}{\partial u_{i}}e^{Y}=K​(adY)​∂∂ui​Y,\displaystyle=K({\rm ad}_{Y})\frac{\partial}{\partial u_{i}}Y,(S.161)e−Y​X​eY\displaystyle e^{-Y}Xe^{Y}=e−adY​X\displaystyle=e^{-{\rm ad}_{Y}}X(S.162)e−Y​[X,eY]\displaystyle e^{-Y}[X,e^{Y}]=K​(adY)​[X,Y],\displaystyle=K({\rm ad}_{Y})[X,Y],(S.163)

which follow directly from their Taylor expansions.

We now substituteS−1​T​(u)=eYS^{-1}T(u)=e^{Y}into Eq. (S.157) and multiply the resulting equation byK−1​(adY)​e−YK^{-1}({\rm ad}_{Y})e^{-Y}from the left.
Using the above identities ofadY{\rm ad}_{Y}, we obtain[B,Y]=dd​u​Y−L​dd​u1​Y−Φ​(adY)​(H−L​hL,1)=dd​u​Y−L​dd​u1​Y−H+L​Φ​(adY)​hL,1,\displaystyle[B,Y]=\frac{d}{du}Y-L\frac{d}{du_{1}}Y-\Phi({\rm ad}_{Y})(H-Lh_{L,1})=\frac{d}{du}Y-L\frac{d}{du_{1}}Y-H+L\Phi({\rm ad}_{Y})h_{L,1},(S.164)

where in the second equality we usedadY​H=[Y,H]=0{\rm ad}_{Y}H=[Y,H]=0andΦ​(adY)=1−12​adY+⋯\Phi({\rm ad}_{Y})=1-\frac{1}{2}{\rm ad}_{Y}+\cdots.
We then use the series expansion ofY=ln⁡S−1​T​(u)Y=\ln S^{-1}T(u):ln⁡S−1​T​(u)=Q2​u+Q3​u22+Q4​u36+⋯.\ln S^{-1}T(u)=Q_{2}u+Q_{3}\frac{u^{2}}{2}+Q_{4}\frac{u^{3}}{6}+\cdots.(S.165)

When the inhomogeneous parametersu1,…,uLu_{1},\ldots,u_{L}are introduced, each power ofuuin this expansion is replaced by a product of the corresponding local parameters, according to the support of the local density of the charge.
For example, the third termQ3​u2/2Q_{3}u^{2}/2becomes∑iQ3,i​ui​ui+1/2\sum_{i}Q_{3,i}{u_{i}u_{i+1}}/{2}, whereQ3,iQ_{3,i}denotes the local density ofQ3Q_{3}supported on sitesii,i+1i+1, andi+2i+2.

Importantly, a direct calculation shows thatQnQ_{n}is annn-local quantity even without assuming the Yang–Baxter equation.
Thus, the boundary termL​dd​u1​ln⁡S−1​T​(u)L\frac{d}{du_{1}}\ln S^{-1}T(u)is supported near the boundary around site11.
More precisely, the contribution ofQnQ_{n}toL​dd​u1​ln⁡S−1​T​(u)L\frac{d}{du_{1}}\ln S^{-1}T(u)is supported only near the boundary, namely on sites1≤i≤n1\leq i\leq nandL−n+3≤i≤LL-n+3\leq i\leq L, because a nonvanishing local density ofQnQ_{n}contributing to∂/∂u1\partial/\partial u_{1}must have its support including sites11and22.
Since taking a commutator withBBcan enlarge the support of a local operator by at most one site, repeated commutators of a boundary term withBBremain supported near the boundary.
For the same reason, the other boundary termL​Φ​(adY)​hL,1L\Phi({\rm ad}_{Y})h_{L,1}is also localized near the boundary at any fixed order inuu, sincehL,1h_{L,1}is supported on the boundary bond and the contribution of orderun−1u^{n-1}fromadY{\rm ad}_{Y}is a commutator with thenn-local operatorQnQ_{n}.

Hence, we conclude thatQm=\displaystyle Q_{m}=dm−1d​um−1​ln⁡S−1​T​(u)|u=0=dm−2d​um−2​([B,ln⁡S−1​T​(u)]−L​dd​u1​ln⁡S−1​T​(u)−H+L​Φ​(adY)​hL,1)|u=0=⋯\displaystyle\left.\frac{d^{m-1}}{du^{m-1}}\ln S^{-1}T(u)\right|_{u=0}=\left.\frac{d^{m-2}}{du^{m-2}}\left([B,\ln S^{-1}T(u)]-L\frac{d}{du_{1}}\ln S^{-1}T(u)-H+L\Phi({\rm ad}_{Y})h_{L,1}\right)\right|_{u=0}=\cdots=\displaystyle=[B,⋯,[B⏟m−2​copies,dd​ulnS−1T(u)]⋯]−Ldm−2d​um−2dd​u1lnS−1T(u)|u=0+Ldm−3d​um−3[B,dd​u1lnS−1T(u)]|u=0\displaystyle\underbrace{[B,\cdots,[B}_{m-2\ \text{copies}},\frac{d}{du}\ln S^{-1}T(u)]\cdots]-L\left.\frac{d^{m-2}}{du^{m-2}}\frac{d}{du_{1}}\ln S^{-1}T(u)\right|_{u=0}+L\left.\frac{d^{m-3}}{du^{m-3}}[B,\frac{d}{du_{1}}\ln S^{-1}T(u)]\right|_{u=0}+L​dm−4d​um−4​[B,[B,dd​u1​ln⁡S−1​T​(u)]]|u=0+⋯+L​dm−2d​um−2​Φ​(adY)​hL,1|u=0\displaystyle+L\left.\frac{d^{m-4}}{du^{m-4}}[B,[B,\frac{d}{du_{1}}\ln S^{-1}T(u)]]\right|_{u=0}+\cdots+L\left.\frac{d^{m-2}}{du^{m-2}}\Phi({\rm ad}_{Y})h_{L,1}\right|_{u=0}=\displaystyle=QmB+(terms around the boundary).\displaystyle Q^{\rm B}_{m}+(\text{terms around the boundary}).(S.166)

Here, we used the fact that, since we setu=0u=0after differentiating at mostm−1m-1times, the terms of orderunu^{n}withn≥mn\geq min Eq. (S.165) do not contribute.
Therefore, all boundary contributions are supported near the boundary bond between sitesLLand11.

The derivation of LemmaS.5given in Sec.II.4can be justified by a similar argument, since theO​(um−1)O(u^{m-1})correction and the boundary terms can be treated independently.
After applying the above transformation the required number of times, the correction term still remains of orderO​(u)O(u)and hence vanishes when we setu=0u=0.
In the case of the modified Sutherland equation with anO​(um−1)O(u^{m-1})correction, given in (S.70), the relation (S.75) with an explicit boundary term becomes[B,ln⁡S−1​T​(u)]=dd​u​ln⁡S−1​T​(u)−L​dd​u1​ln⁡S−1​T​(u)−H+L​Φ​(adY)​hL,1+O​(um−1).\displaystyle[B,\ln S^{-1}T(u)]=\frac{d}{du}\ln S^{-1}T(u)-L\frac{d}{du_{1}}\ln S^{-1}T(u)-H+L\Phi({\rm ad}_{Y})h_{L,1}+O(u^{m-1}).(S.167)

Using this relation, the calculation in (S.166) is modified asQm=\displaystyle Q_{m}=dm−1d​um−1​ln⁡S−1​T​(u)|u=0=dm−2d​um−2​([B,ln⁡S−1​T​(u)]−L​dd​u1​ln⁡S−1​T​(u)−H+L​Φ​(adY)​hL,1+O​(um−1))|u=0=⋯\displaystyle\left.\frac{d^{m-1}}{du^{m-1}}\ln S^{-1}T(u)\right|_{u=0}=\left.\frac{d^{m-2}}{du^{m-2}}\left([B,\ln S^{-1}T(u)]-L\frac{d}{du_{1}}\ln S^{-1}T(u)-H+L\Phi({\rm ad}_{Y})h_{L,1}+O(u^{m-1})\right)\right|_{u=0}=\cdots=\displaystyle=[B,⋯,[B⏟m−2​copies,dd​ulnS−1T(u)]⋯]−Ldm−2d​um−2dd​u1lnS−1T(u)|u=0+Ldm−3d​um−3[B,dd​u1lnS−1T(u)]|u=0\displaystyle\underbrace{[B,\cdots,[B}_{m-2\ \text{copies}},\frac{d}{du}\ln S^{-1}T(u)]\cdots]-L\left.\frac{d^{m-2}}{du^{m-2}}\frac{d}{du_{1}}\ln S^{-1}T(u)\right|_{u=0}+L\left.\frac{d^{m-3}}{du^{m-3}}[B,\frac{d}{du_{1}}\ln S^{-1}T(u)]\right|_{u=0}+L​dm−4d​um−4​[B,[B,dd​u1​ln⁡S−1​T​(u)]]|u=0+⋯+L​dm−2d​um−2​Φ​(adY)​hL,1|u=0+O​(u)|u=0\displaystyle+L\left.\frac{d^{m-4}}{du^{m-4}}[B,[B,\frac{d}{du_{1}}\ln S^{-1}T(u)]]\right|_{u=0}+\cdots+L\left.\frac{d^{m-2}}{du^{m-2}}\Phi({\rm ad}_{Y})h_{L,1}\right|_{u=0}+\left.O(u)\right|_{u=0}=\displaystyle=QmB+(terms around the boundary).\displaystyle Q^{\rm B}_{m}+(\text{terms around the boundary}).(S.168)

Thus, the correction termO​(um−1)O(u^{m-1})in the modified Sutherland equation does not contribute to this calculation.
Consequently, the bulk part ofQmQ_{m}agrees withQmBQ^{\rm B}_{m}.

## 


- 


Major funding support from
